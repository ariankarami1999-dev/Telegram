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
<img src="https://cdn1.telesco.pe/file/heOoY3_McBTL0amQCrm4SV0jPgq0kQ7GxhNBeSJJKkaqqSBw9ekfiy9PFyFuQeAwAJK_EEW8BJYuu18GCL7cLznA5ZEIA9K8IyymRUtZQC0SnD8RVlPRE3oKJoiurw6o8ngsKtsLgy92ObgRcRgkmHAF6IwT5DPSbZcLuvvAm76Tq8IlPinCLFAjGQQdbsTU-v80gDsA5U_KlDARxs_Wfs1I-wYST_mg1oouBy7Y1b1GUTl6KR-QDbG-k7bBaGo-yojAiOuIAQW797y3v51iSefwIe30m0KDpikNoM3pK7ap25nmLABdLYIIro77pPXcjHTgocdYWZi7stZinyrk_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 00:24:30</div>
<hr>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i50afXEuOB3KYVpdwA3c9DoNQGYwo2SAjHdw932mn1_W4NCTWlXQJUJCZotcuKgI-JLZ7kXeeArsmicidZz6vsdYb3xJa3L_DDszDitPXfteqiDBwoJbr2cWQbs6RiiCaS9KNpyft9-NZX2Wt_ecczW3OtQmOLeF5nAYQLMwv02vaIZ9L35yndt8oQFDN4PXngTdHuflGXd-tzovUrSFn4H9y_t9iFnzlnRJHY_WpenhAAe1SiOEwCLwS8t5Lw-YENJfY51a-a2HRR7Y9LNsQrukBngmp8SjvO8P7yuHvtqXtzsBYqs3tgMaqGX2_l5QPXYq6Pf0nm7bLGpbBqla_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YsMxZGqPdE37arpeNfdDAF1WyoaYAOtxUeCvZomgwyL-VJ1_rg7ABwBXSXDQRN32B19o35KvQq5YhqMPb1zoLhcsQWFyGkcravkhtGj5LpEzvSU8Kha2Vfw7Gl7IHXilT9ApSCazrY6g5AUEadCInZvcCxCORXoKF2Z5W-kgeNT-ko5iIf-nSK0mEsaQVG4gx9w1fCPpCwebJZCamE8_e2-XD3TehkJ8512wurNtQ0jUsnK68_NSL_itwXgriTMwa05e32pE4HvnRthcr2kVedd_aqN4vCa-9uw13zU7Pi-7RRJczc2zvZ15_20-iVDuWEUsa7WAr_1hJWiEHjcXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BqOpBrai-RR61hCmLNf17sHEu2Js9kdzfNjYvLQwa4Z1DCulLPZZnOV_z47Z1PZbq4GNhjCCtKdYp4-bKVhvZDWqJYU2qz1fFOvhrAHVFFnJhYc_qWv_uxgofQ-WaT0PSqPzr1k5RhHEIk1aCQKjeDxKA47hGVOa9Kt3NQ3EQMpkiZlLJT9XqAjuepkmA-0CPltmvvgA8HJP9JQGQqP_5-MX-d425i3lfYXA4jMrB2KFcD2BSFNPkfO8tbFLmgRwhw_axdHySbGk8QHBTD4qI-MpLEMZOnIeLLoNdyArT2m1vPTeoFimPd5I23ysMUg56t4K7atbpfA36WW8AA9xYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nAlADZBJ8MhNdtQGnUogjk_8LCELw_mZ-yaS71vtMZtaGXPsN85NyJwW9dNx_fL6bWxVbao3LzZ1Mp2vtAVV_Qlz-U22BUjQkZvpOY2L60yjRbIgzTw_I8V_sJzgd21uGmFYm_GPePftU8rBP9cGNYrqtBqVjQMktmGSvBvWP4jKhEK8bC13kafRn2keNycjYwaFqOfSdBM5ikKq2wkxOIdO-rS0M--qH0ySIjbXxGgOc-DVsdxJBPRRBSxL3_vCtV_MCpv3AHrtArl-LEwZkHXSWvrfANJg-N-U58GkpgLBjAU5Rv7a-gRUwq8hYt0If7iyXMVYvRpKxNCGLtkNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/biMfMO2C95UwPWmGFVa84IuQMlYeXzyzCSck1B0G13jdTaQIeicXKSbEuy0e5A1K4vrOGzsXqV4g3-rV3OG1KtJWiBivlD-2qWjV6S6q20uBvYSVPoaG8644VM4-QC0CbiB2PZfBgsm4VztIl6jCzKNEnkngyp24i2NjSdlbGaphaoN5MI-lZ_5cj9wzNdrUUr4JLvT8qQtmS7Vc_UQF2XaYklChSSPo35Uhj27F4Qeqb8jP8zeS7dRooackHOaawSqshzviK7M0EZ3DetM--wQY9X5A4PwbPT81V-_aCl3FEowpyAXhaa7nvQBPzXxcBceOICz3kkyy3j3yPBig_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iV7eZ0zTRuXnhm1213qcjN0n-TJiVr1SBCLjGryWoA9eREn_JIe3B10NHhy8xoMF5J3A9AK1uwsZzfwU0XPfBUdDTM5-EAA4Zxfqzx8G7aKXB2LA9-OBGDnrJM91rbx8lxSJ4rvwfjXYx2rw8WgIhANqECd2i63TYhzUAs-_rMVTwnbXt2jQFwndmHq_jrGEbBdW6OgCHNA0I1HJSopm0_XaOAYjlqIpqO6D8NQiALH03W592fAgyfFgaevWoEZS8OoETHYvxqid-gdHfge5QCXdO7k3ryEiC1Y7IE0agTdPW7biA1gC3m-AVHjH_hefeGqxwoz75wTRfSRI4scjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/csZVdT2aFgwls_Vxg6Ua-7H0sn-j0qOOnZI86slf9XUu8pSF5E8IjkBNsfE2QJhTZeEEQa7fGV3cXWZ3q1w01CCWHOwfXHZZ--J-Qs1K8ZSfJB7R983KoF4662kh31Y3nQacMUv8in0TBJtIQ82znJFkG8ADJRsxhULgXEd_lo8L9vVEFemvFHKqqtivslmycnJc9Yt5pTA4yceh9jf6EkwbY6W5y1Xd-fB4DDNr75AeZbJwJ-LE6FlperSOzp7-2RQDqcsmlz777wmUFX07Mf-adun53QVM6RxZ_hhiG2ybDIUVCRTRLnZa7FHfxHCr38mCabsNMTjHjsAtJmiKOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hXU8hy-wJfufIQwTwEtS_7LOFMzIH-5MgWCSFAQdqHaALc7ReN_o3e65Lwde326WgilcVvyWJFiW_4dKbo9rwKhUPlQcMTH7awzqLQSwwnecBKcgfjiZKuykNe7QpgzG-hqfSXseKPfzY1wV6Li6oftZVPBHxyJ62-4K4Wyd9WyizIN8T-WODiV7yvvlF2c550HYjoBB0CdBHNDvfDpEAhPZsSM7GhfNykq16hu8yD5EOFl8CZnUeIqcB6twE7QQ1evslCIwshECfirAgMsDg9bi-3_tI8_W4Sf6Qz3EFrkMWsPAERY5EIR-bO76dUxULKCEwzRR9MrS7ThuSt3AUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CBWtcBEejYbID7LWuwujy66CLs6bDU10Dz3n4u6HOT8D0LOB0mXaGGN-XRFe0f3fhuu2XHUZde5ympgJccWKr93SSREyyC21PINHrveJmmbJTAxgKDQeNUDk4D5MZioUjNucHlijxz_Aj_sl2r_j7PdoQvnAx4ia86z9PA1xPjPM8Ln5hLp5IEnczTIKD6_BeW2hN_F-wnboRTGDNRyYhiVy9ue51TTSrkLrpz-QvLm-GG_lE9SONTYtkf1B_ux2lvq3-dAeDiLNh6XrgckQ6oJDfg8Gp4urNooWvk_Jv6HPZEq2XSA_p8kwcopqMvEAsgQPAG84ZSHmtlSkxP7WZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1NBNQZrvlWfzc0_zehcS3WmeUTr2NawRZXsbbvoGZQNM_sYYBsFQoDDHo3R44c8xaFhVzopC-TMd8kOpyhnFkUKtaR6O6g-ZAOBGOPZJPvmfAHYcHGYFsGJsCttYBmBKkZrThhxeLkZt_XTgpCG13NJtqR2TepF_7N-maxGyYWTp2lhzOox1dxPNy1SW5VvlByFC6IqbghYRdNrVPVmm8jxinSWngcS4HWgkJTDYhq0SpO54Jq01xOhcHYsYMB_O09JL_tZdVFWH7u_ZCzYpvr1TDSm7wVnTf5DKLOz2D2JFvKtGsWZWgS4QPSjxGfP3yig1BUqmei-fbgkOjanEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ak7O9wEBwJNGH-6E_Hosl7QEZX8oykCVO3liT1dFR7d1ad0W5C8bTJbsAZm-Gg04yqevIgBaeKOvxx4gCIRU4lBDUJUykzyRisMB13RLBfZe83AkK7ybr24xkD2Dvv0I_fASq4i9tLKOx7AlxWwZWpwFvTw3OyYm2LetBmgH1QMvTJNj_T7uQrC-SDQZGYKzXesSbnpzmT5Wj6Sa9P6R-QHF5sObBveCxaV7AsDTLbG4376ebYcQCCSK4S9eNeYq89b6xeOCYgfesyg-XB1GRol4lNrGWRKyKjGEPIJ7iZuv4iDpjE5zt0Vu8KxamrHuyicFAUKrOuHPns46IPH25g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LRxzz2A4jfeNFfPsoUfO8X6ZIIYLck6uiH1fAlAG7UyUleKLi7leoNyXQQ6CRQRIPyz-_YMJD-YI9qgEZL9g2vER9l6UCGLUgHy9tKHC6mQg65cizJHkNHmjyHxUOeAd1N3LnVA154Y3DBYK9HjW2KGB3d8pFHJ0oHr69iqYSqjVCNNpWZz2bxZQnA0j5whJ14TOptw6lzJt6cExt5DTvUjMAwVkWF9VTnP_Qvf0LFEHJXRm4DT2CnxckfrsVKegv41TiCqCc_plL3QCQbc3ysd3v9QzIB3uJJRRsKK8ixTqs-oRBUUTAY7ojKryDzJVPclzMyLLN0zb5ooQp7d7rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKvamzCKjpCfD8oaOKBpvBDMwhvI2Gyxj5hPBf77MidoWATzS0aPK-XtNTmoqMm8CQIH82ZNZN_AQbbP3K60wgQE9p5xUG82l7culnjo2vQfNdFFyw3tEy3-dch4z9Y73MEJfV9bqv3Ugd-Yj3MGJXuHbiPPE77JFgVuROmvY0Z8KKfRG-rhLUWH8lvQ4LVdxprT4fEK3vaeai9Jo7m6We_nDISg4odO1rljVE79rFFSqP7n2T79j5iGGhLtGGfDYonwwN14n0hYFuZWLLrEPCFLrTovcr7jqjhw-VhBFKCbAg07tCG3HohNFmK0M78bq8Q2JT0mXenI4DWvBiiykQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9cUT33SyyzH7x2030bw-_iQdIG7274YlpJS9LeDo8OboFPazkT-intmucFQj2AbcJGzciVKtaeBiCNs9zED73KILz-vBVuHk_zJqWkw8LHI6dY-Co8AVJai4jmsV8QwvPNg7yE5QEP1y6PTJ89ZLxAFOb6wFBRCYDrwPhKAKADbrP1iEOCgn1hBXjm9tcCa8L8eYrIR_0A2AxF9t_D0NfWmlGOqOF0e_lng0hYWz2U1ZmU2gCFGvJxv71P9dF1rO1HMQZ_IvFYk_E9A3szlbeqLj7bTVgxkj6BMq4RxQNh9QQLU_bkY-Zrt7kkJdUkEf6x-8thAVLHbChCCYYOKwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OaTJhbnGfO9XvXCK0MR9Bh8EdaAAewJSu78L9k0agCT8Bxo759vTHq_ui1dM6xhfHoqSpoWofT6GtJ-yYcLr-0L6VyOKkiKzxSIYWWtB79w0PmbGKjbN1I3rxRPVX2wO7BOaV14jBJAGVr0iroyLSzTnyXq_WbeCfVFvmaMGA-cZicMraI9MXZ_HU_wjZsdU3H9Vz1UWcgheegEHRMJIfP1N5WF0-znXh7roT2zCHbWMC928BhWcbHSVN3SOJAx_o-f8zx7UMPHjKSKcVa2JQZRr7bGnPSB0m7QCl3kIXuX4IrV7obEYV1jHlBEUlee9DUrUGKLjotaPUCghRU8yXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NkApnw0Ww05dSFI48JtquTXhdlyqy7l2zmtFWEj-qWszXYhGZdaZy3EIlm_s1VQJd_aH3JwxO6hw-VIQ6KSkXQN2fWsK0vdcCstPbQwOpZAiGDkw3OaC6n8RYZBOyU-Kipilu_1nFsZsJLDcksu909yvdcabKEfQ86B0VdTMK50hVTQTCF0pVCbZA2FUkCTuoiyW9NgYYSzGTaRC8UJnreV_6SZh6PG9LCLu6nH_txSOFMBluAmPUayYaBLpI5Z2gIPsjs8fAO11t1pDlMdwk_psGpBKGdV0A0OZlcLhuRfkeg_eCBH5OZ2aBsmgxHBMtUU7fVxF5VE6ZsRKzhXAfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-HZeGqjMefql4DYRu7nDdb2YDkAz36czlT9Q3dWSIWjxIG6dFXcuegHRRE-3KCtkn9-no-l8kp1Tl6JXi1rTjfVe14qmfeFjAUxyILldpTiATgo5EKMtmK3Xmg3bnG2JLw5aRxgrstkQsdUQReME3wNxEZtg6ebJbqeP0gWh1gqAkFY-ihWZO-_BAc-0DmBJyPIrHR80IrT1Clt1xomLFh8gOHlmSJS5EHKk49aOYz89g_f1IMWojNk1RhFdgN6eH-ode84RGZgNHXWzFqPrGu5TndFPfsiW97EG_dUiz5Bbhk_UuGYzP4NzLLF-9YIyBDuYWmH6Jw73zcbuIBVjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W8oKqryQqXdb0APeK1HJEMOi6kiqXPynZs6UsCQvk0jniwI28BMk4_EQko4ItvM40PLEFqTJDGBKw1G94jl_Po51afuyCYRJEvrz2tqdmBwniU5g4oSz5I5gcEg4E7MZbrLu7KQIuq3kayRGwzNfgQ4FVOV5yE0MQ6B9B3lxPwdKQtr5SlSW3u0yx0U4NotwNrX5NpC3fGvtzH1lmtCEncxJ8J4eGaWGoOUV2C5DczpXKSOYjNdovI6NS6yNDEK6u14IQ8gPEFglV5rfoucgX1T5QWIQ5l_bWzJQGd5uSCZ2I0pn9v1JBaSqbWMT2KJtfgjSyqsUiQmZxBN_Wd7V2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EuBXOjs_X4r24dCUgofapmal7o4Sk4S6VJZQ37pxPXPJmirXEx9it9hcS2I38WWwMJXLw4rr5uFmVYHuF_YPR7iXOoIguhHmsckoM0gZ-13igJ_ibegpPGa46-TYnpLCQ_lnkB5vFKd98j7nkQOHJy9OiWE0h2f7yH6Rh5fHB6Ed-K9N5D0TNZF5Y9DLR2HfmXJ2GYp8cHS7f-EBslcm5rimAOWO2V1YRwTMQ_Npb9VWNtmWKqtD_DzyNR7CVNnPN3R-gd399rMu56827Ckr3exBECJ1K582uML_STNB6DzWntsRDfqzOpML-MtX6203GcqMYfc7JATAivghLRMFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DJEOeXBA6gWluShV2Yt-yxvW3q0nhK3-DvkQ9ELNx-8B6AS3y-l5tKOvcZysczZbTNDcflDHSCFapmbyQ9PShDM89TdGAxyf8qXZGDikBTaxSbPmxMoHIui_7USUxXT1ilsLGh4jn0nXKPsaBvIOhJ4SYNf3uS1gX7mGYL2twdaShmS6XUKTVFD7zvRz0icrzXqDXo_7D6_tEBioXIATLJb_rgq39Grddem9diR1xkSHympnbl-sLsWuciCPws2BUgDamxHou8ip92qfWU8iRrTeE57k8oo1uu51BDMzQrYPC0N6BZlLUbh32LKB6aL0cxDf3iyYVg0Mw-TSnY-ljA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vnsbovS_LMrfrwM05EEVbpkCx5psv7_4EoBQ5dZVNBaPKY0CpgkcSu9Dl1trkLHio4QjlMUGQz57Xy04dKDx3rVltcqEcP_619eiMH64sUh3ojReHz4j3O8uK6G54V4DGHGATCVmCufIVp7LRgnlLl5iFVzlkNCKtxb-63sLEAVhHglbAzeH4hhoc6i2qcaOIlwZ-7phmaD3ED_uATaa-XbSO1DtsVY1UgGQ2fJQA7jjCFGqFW505f-XIySC47Pxzw5n40CItQ5fOsUfiLPMFtdyXQ2YveIXIxxWr7RmIr4apU6wJrrXnzEHQw1jibAbAxVNcbP2yR78-RCBGJHprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8XJqB_T8pEKxSLdMlPsQe1LJAMaJNQGmu8OJHtAsa1LdX0p1VTPjiOD6Y5jheOp1c_SZaUfmur8fgjaoeQlsszw_Wq_5BFc7kIAExFZ-6ty1V-mZpo1VQ8Bfj5Wie08gWQ8tNvo0ULy7jZjoaZMBNRf5iIu_kabBnr0r3fkNmihd67tvYDte3eelsmVCqIKEYc9TB20qTZMxD2pVpbI3qHbAotObcxxAkY84opgTVbWD5h7Iw5tz_kQNf921AEtJrIWYuqARImp7rWxHHkU8fnDfhcHRBlrNassmVROpqrdTD0UBwq53RUhMdgV0MkaijziCa_Uvb1q9EEgXUxFEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M0O20h62CQH_lXqvh0mbuwcJDEbGsIspn2QlZaRobBzeB_WOlDjrwBXFvnp7jMNYQm3xG1aNQ4g4rt1JuoHmfe7wDghgWPij6KXAKQ9rLkcRFR2tD9z0nZw6KbsNSHtw7r5N524aW-SzgByiMqfjnEn9MnkypgyLbO4nzr7_5rl30CP94anOT1Q5TO5OLqXfUfX5vGk1AUCYvAswP1__WopjImlOJTyEFaM7BpItW8e-egDnr1Q-7Z9M5_h6bzUT7J3PYGf0w5UjeZUoPO8LfH6fQxxEqLVgKPbqgbsphLiswEhuQg1VcMG5S-NeDBSlh2EmNuDlzHGSTD9Ii2DtwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVbGNJyYAHdjojwerGK3m9qFkXvqynFNmNHVS86sGxJkHxcq9iJjSswD5QlNY8KxddTVvwb2sR0RHp23ajLi_2SLaht7Ud9hWMVOMD_wN74kJjNL8MRY3_NVkhBMYRj9l7F0LCujv1Ny7VzxWQQxuEjd88dJ1tt6DTknq9qx5io-IEnZO8C0EgEeWyg11naZNnfN6yOEGvPcrrmzaVCVT-rlLrsq6ijunJwP2PATo-PaFcLgjh1kJbnGRIC1EqqS95IfmPrVG0pFe0tSJi3zUbtaYqfK2nUbZfcEKKDyrOWjFL2CnKR_k2F5q7oMhdYyO105oUFS7NdaTJBPIdZz7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ejHsABukoZ6q7kcE2xc1G99mVAi5PXHSOh_iQuXo6VeozO20NrJSW7-1BIQVb4L7KvTw_oHvc7qdNmlDHdABMZEyn_odgQZvOK1l7d_Fm3BCS2NExRQcdkmGGfLHp8vAXYDpB1d5rFmg-lCiS3LaQVXJmKuqDDR4KD0Xk31DP4N3i9IFvjy-bU6iwjXADDa6j1E4Qxx-yKEuvLZ2h8r_KmnrCrjNstQ6A7EWK0wnYvSRCwr-eKrzSLTsr15HdEg3pohg8hIeNecEf-JARfgoWmVapY9rJaeL4UDo08FHNCeJsfhgOLYQWDVnBwnahks1SHBZQkUa8SDJ877VORutEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NHcDVuvg5uDyB2ryaNwoFv57tysca08fxEICQgx958lZIvw8QQzOh5O-Anzvga_ge5G5j9XVRxjJCVhWBnWTqs0TpCCfBj5sqrwGRFleXkbDCwj69qIhOm5oPhAkHQ2QmSt76hXygeijq1f4CQ1SPP1inU8zPuKKEbJia9U4zBwaK_Y2mBduzAPJmuV1K8vfrnlYaZYq5w7qUG7TUEMhqGPrOW3_WczrSrtYH9WJbvretlbqX9SdQEs-DR41FDTABAoB_tFS0CHwoWkvFFGt9bv9jLoH_MKk7rJmmG9GtRCd61IlOX2XgM_DrjQFlsOfXoJPaGLFMtkaquV4lTQKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R3KGakiJrpA8uicmd5lGcCLfqB5ZS_7D69TD-R20H9v6RopjjtVKDa4r2KQlBEzSztJDbODvF35KV-Z913Ff5kBBd-snHD2SpAq7YNBI240XTPYmSRC02c5VMH24icq7d_IKE8IWVLJzccOtfjMYsyv-c8hED9EUeSnh3kyRjZvFzS9h55630d-XwFKY67L89qk-6RZcMW3ysQf0H9gVFIzTm8sXhf2OD4ubFGGc2YLArZ3gbDEL5rXuxStq7x3-SPy75Aln0wE7bcLNSkn_XGvzhCTvitI8XDqkMTbXDnNqfejtAip03qSu-LZKaqwmCswy_Yy2pZaTh8qsIPkNdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mhsMnoqNfs47EPDJYxSYrhlVJM_EfwaGPPtCHti8Rp83fvvc-sV8DP9KI8t9ygNd05MAOKkyLasoFqunnAcx-EGQFKZqwaWqKagRX0uMPzQyFErMPG4B0JHWY4Mtd7sANaAHk4KqaoH3x9bZLcFx6nMRw0gUHGiv1AflQEQPN4TzaSlvTR16P6sLgbsYL3I8a-TumuLnI2MX_PR_xCWBv-R0cvl0zwVKW0g_coYQYxDo9au_DadF34vL10twc6VD4TgJt_kYZe_Afg0V9DVWJ9NxKpn7BXLEFpEbUWTU_JyzhHs7kKE9OJdd_OY7dEVGyzTZSpbQDqDeYiuezxuWZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWPHsLISvu27F-tDi2kGKrH30bNuj76u7ndyBemTuMX8AcKPsLzgjNwG4BXDg7w2-Z1IoeGMFOwQHOT56CZVg0byrjKrZyeigL8MVNM_dRcwcbeUu5Gu_GLCZbmzrXCeac8DewZWwWZSerEobfTaSXD95S-FvKJoCmn7au0GnQ5M3HxOTTaZFiZ-3ck6yzu0MEZnqSDH0BU42O4Fn3yxZe7b0zQZA__bBuiqk8UAN8t7JzGnPVNglHKHNhTNrazywMB9mNNHZhcYrQ-ZIj0Z0KFZkqgfQjO9A4C6yqJL1YbsiOLUe1JyxdSGCG8gq5llWUeJgbRX0g36HlSwON62Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WagnVPyLZX3s6I0waFigqYYnWEcZiKRjS2aDLWyvcji98jO8voYHUi-akjldQAxul0qX_vEODDjfEk2StLg119c_RaCZvkuEfuKdByZpRwvOlyPBcV_HlBf8OQLdjIbeDnmBB1MVF_UCfPMykTXvhQNULVCUejX1jqo-7imBKHVW589pfIb6k67lT_zuUUfY_vIF8odWEiHmz6CZ7BT_gYSidIsM36TP44-vjE2mnu1dxXywwf8NzPK-57QJ7aRyV0_QP0KCRe9tHq31sBxBQKo1hU2val3zsJakWUJ-F6-u_PUCmMRdXur_hO5O_-LYul3wQsxdGl5dvwz4CDtw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c07TBlKjbThju__E7p-j6TOYytuT1lydaOAM4XYuOU_fY4W76Bnro10YerNFK-KAZIVHG_5sYuHy7eGTh9wPUMHe04_HIKCZRGMCmvTYLoVeX_Duy25wuySJ7aG4tPZn-vYXHcofbR9CjXLiM3JXhQX1j5GEmT1JskEi2WDAqmJEYwyo6BNhrgRXtzgQqs2gTrB5miPAx6dRs9lBKrT-PgWDhkFLx3-8R5fcWd8sb0CEJngVjifiXMlbKP1hHHuBzV2RGbKe5_seD4KI9Lw3-fHV_aHATSkSx3tIzootm6u9GIGHdsycig8WdrvGqk0MZVcqam_q_8ImsU2qeK7i1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBrZYp38hOWxien6A_htm8DrXblRjUohlxN2rMDTqTJx9EFo1nJkm0D0rGKWR94wHCGYFLKCWgDw1ohjqjk67baKPhReFVyXjvpJObai1jyiLVE95R1CtwRGaMOzNSEGFnEQWzmIu9PwbtLeVIyOOmBBp39LjCU8AGxtrGgHIAHXLvhwmZzYh5BBWSe2O4_o08at2mMfvYjzPCLJQ9yneXXj32SAECxQKNC8veGGblaiC_zxkt8f1JUlB-VX5H1MYoyANv5DKyejqDWlL2UabeDW533TH-KgJ6CjrysXtGVzRsX5O1Za59fptaDabpIH2wZg2dnybSwrPmRbOk8c9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ai_P3AIYVpzJPDbs-PAvZHSgZYk-M2VZqIrx-klkODumnDf2AaCHTDjvTb8B2CZlPGltjV_BoQcqhjsv-6Z8ZPvxFtUZB6feDcPl8BqiTc7KXJ7c5m_olYtSlNwoxWsrKKA7IGRRyG-Cinx6iU55xBDN0kXgCHjl-ZSp0kOCm7zzttehk1sOEB7KLmNIhtJ0y50wGZxNPjFs0rpwgstb6VA7eK4KEGQd-w7mpfgxQj0bHtvJBORErIDNBBmv2lYI8yQSqEdt5JosGutzE7WiyE1gAe2W7IfPlDLtQRzAxoQk3ceuApJ-l0wOS3jve_-Z8P4-9VaABr8y-xd27aILNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b8nIxQWvkXHwYQ016mmTZlqUZBHSuPLzWDG7xteq--LJsxG6A_RqIgxuShBSJvPcECL9suytuIlrgGl1XA9a8M1xmtEjUHoK1RdvjSS_Pzi30wp2pkfANuPuabd7EwpLj_KnUrtNsjAnZSWhJj-TphROV-_wLXJEFh-3uyq2-M_JpCYwjQiLOcINvv2s1ePUt91JPNTj0kYT4mL5l2BZxbzhNpyBaupKqcb5bWKfl80v4FLmGx95p86AfSE3bcOWbjn3R_yqz9EFebKk1-Mukqulhxwjny8nMAAyALo0SMk9gvXi8HBjODwo1kika-YS3lFr6CooVfsMm8vq8eoY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eo2CBbetEjrjoC59VRsmNVqy-ggbSzERAeOzXT5NYZpp43oHzh3qAeF9NJ6Tncae6V0_gwkXrLPD6tjIGJVQYAKjOHDcmLblMtc1oo6HX7VFlV9XaWTO35ClKxi3-ZlIe2d5JtG7C4CEiyT9HOupmUoK-Q2XAOJHUYY_uUTJuXbHIkQomQ-RH99dcFq2YBWtaS0f9zgwhJMCDz0A3RkjtYsSv_pFqXUz0K13GVvSfZEjRM8_n2KOfZw-fgaIr_GZAeXio5sn-wJg0MxE--hrfNxlcy1QpJl3Dq85D5SouQYDBs96lYD60Cc-aXIbgUnEhhEgm2WGR8n2QZnUHMjbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MV2P77NjmEj8YJjwmXZZ8b-4toPnZ-KxtHCyDkH4kufS2XiZTNJdVblXADhK8rGoafRJZCfM7-g_BTjryVKEqZX3rgNjcdImvtrbXa9dK0UdoXujNGeGeBy0fTpf_joamX_LXl6yzNVq5GuXzAgdVh31OwTD_3CKCY53ja0oRCErbnPBG9dkTO3jEurys7J6RENVY17nTmVini0mgVtWisMHd1hGWS36cxo3S4um2QNm-r-V_S2hj8IspJkzNLJ8-gtV2wUnWowyvO1wcNolBgKxcoB8KHusAQKqg-vrSg3vNsYkaWcT5MJGH0SebZlPdvjHuKWbX3dcLRt81AF1Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jV7B8bUd7NO5hs_SdA-vCmjhE5RKxf0WXUxNFWuyp3NNN45BRgTF9tR0uGmg-JkTSVHdtUcSVToRMP6AKSs6yH1DAb8rEj6S-bmdcB8FJ57YT2otWsPnkRgDQwBTkV-0tUtPDDtUja8C6YFbZ8DQ6jxZ77Xni1JxUIdhQvK2cPAE9F9FCVQdfEHRs-Fe_VOYcFg4qbiu-iWj8op8N19CQ9a3Huris3hrjXbVzCBD7hEqW5iW_WkpRLqjjxdgpY-Vn2qh5apzQAZjsrcllVo2-yBWYgZfVRlyFviBjY5Y5Le8oOOlEECYU1rEvdwoILtoOlIBgt-hYUqUz-UxvGn8rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LmUEHFuW6441Fjq1PswWPfzSJV2HGstlWgFggKpDeK_BiU6DtSWEqK2T4saYriiFcWxcoayYeWQaTWkHhEVKpbV5tUBGO2eOccPu80uutm7ZUwULOslahHX8jLZPcxxQoCPTiuOtwleGiL4TTZ_bOv2GeDh_OrqLi7swmCNrHXjA1ZfLOlBecueHIoIkoGsrG_7m7P8xAFansBJIUJkf0-189vzAQHbvrE1ACV8FPbaomLPaRa488tByMQwUIfe_vwtIjFjEyVatgp_tjIBsbz9OdBR3nrKHubSMjD47vld3dS4R097l7XMwxZyf_2nUal0KRFlYinnFwCurXm1L1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dk7aiRC1V46gq0jUxh_Cw7ZE0AT2wAdzuo7RgrI4QEf10SaoVExKLXuTY7N-YQbwh7pL8DZ2x6_-o1oDJiVMwx8XJMW6L8CRlKn9M5WnajeIYSE9a4SVQCVJrn7UZcE--bVVqMR6j6mnabldFwuGzp5Hf74D0Fd8mb2P9aS-tCLyoGt5GzXlclXcc6Nr_pFJANY-5cW1IZYMRI9P2b7fFR4OJswbuJqF1zpcrwBQmzCTbs9inbE8uf0v-IW5P0jvQ2K8aXviJIOB5Soe1ybJGagVnoyAwhiMrazhAcBa2ldrCkdYrPpgBmxJmdZpBxIw-RC4iaH1ghSxA-VqZykJ3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KFx_vdE118cQk2lYoaZ8VasG1J8gGk6982RrVewrAR7L-lOv9FOlhto_oeq3uUR-GPCHUnUf8MY9N4GOZnc5Yc-Sd7kK10Eb_vwa0xQ1uR-OCzWKKGzVsw96ddF4gWwHP72RxzNuZvQxYMJKfjW52g-6ma6A1JqfbjsBc5-DkwOGGxl9S1UuRq4AwqwJUeMuVsRcIOsk_XvzkUh9Wxb8payRGLh91AdTZ-A4xW0dKnH7YM5hkjT3Liioby5VuaNhndwunS1Ddgw-z8WXuiXWG86P9B0vkQdVTpHnTGLqb1SH6pO-v9BwzI6fQv6xikUTbU3R-DypFTaf8JWpAXRsXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UdE1p8FlfAqp6nKw8NgrkUvcqWTP-XNIEy_4SG_Dw3_cv5gOu9kidoacyQwC4ea1y19eko5NhIbZPbxIKikOYNlpuDBE0zfnoWq070vuDxZ-Dez9rMy4NjRfhv6fJwmxMc9GnxDS51b4bjn24B0_H9eEmT_bxt2AO6395vNT8xTWkv4MrKHsA7nbF3eJBIX1Rt7jAEP59iJTn8KdSHMQ0hpoEdyyeGIkDHiQeXfVWv5ibfeOhmCXP-_dYox8oh-b7rxh2fnXA1k8gsM2yiAHkYqbTezH4PGeDNz9HYfUjl7ZPSYdbDTiyKePTuwwsbaSSsjtCf4cgu46Be_Dcc1T7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HU8iKWvelev_O5EX8_r9O9cc5-O2llrUv86LyEQBqzx2ggVBouFYxqipqGXqK_4R-acSRuJeunvN3SkUs-qAX1N-6_mPbejsspTZYdL5fGo8Vfw_0Ct5lk3IS_db5HQsL42Pkdy_J_xYDZjRbfrdKn1H-EcSVSVLbJ29Vglw4HU-Nz1_cdIUpLQjCKTHviegB85LG7ukMSw0qVM5h55-XyHnJm1N9bn-WBJm7FWVoyH8bWJKn2ni7XA0Ya1rTy7luDxUgCfJHhRlSs_aCTqUYgSWyGu1AUm_Pg1gjufcNUUUkhWxBNZlaVjorfg0lhzqGNvBty13y9_oIZTtlNos4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DWpPDb-3VfQFCRGSQHyARxlGhfkKhYFX8wXlnQkEvJzMMuvfk-FUmjs8-d-dqoN6M9VeluuD7qOK_65rxXQa1dea0zM-Ecufpn6Qw5ALTK38H_3hhBPbRXUJAUOxpNhcQsnJBolVLmDtQMJLaLvQGAGjSYxJR1EhU16Tn4l0m4pLkeyBEpmoonS0dWsLR-x_7C49Z9IQOdMyqhnY_mVWldQWxcCStBHhYgdViKcaA8SbDgOQm25EZOVyxw03wAapRzH05SBmGP_Zv_QPoEDO20U1L1uI38BfYkX_ZC1LhRuyyiM80A1U_L_EndnKmWSlsZBMd5swD_CUj1zPGQLU4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpbKl9X8v13nFpN6qfZKj7RZkrcu12C7h8WInB-ZOndA6Fij7GdrflP-ZlLPkBxeNrBikxXJA81fnBO6TSXyqAVzUG6Z2yyhMRdQRyH2LElsEuH-m_0jkrDX0M0nd928BUqu6TlXjWcVT2l6EyC8mdqlsguYhaUBiV4F2YlG67waSSykeiaSvnVLnzIgz5z44pzc83RoGqWTEGjTSb5oSvfPIBk96-HVpMLaLqFf9-STc8Crmcn5ZCvAcTof6z8gOCOK0MJPWuEsWFvewosn5CH23rYM1doZH4XDuSgAe8jfxA0_fvBH5WKxrDj8eIuk2bRBk6P_O_qDKzwBYkoPqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/efsqK_Eo2S-pc68eA50H85KcktcbDsTzKVCST4qeyoiUe8fachINt3uuJX--Nsui29poeewQFsNGDa64fgq7kw-snJdmgrNKMDLi1LBUuji5_upJkXu526o8I_xb4kC1TtFT9dHRuSYEzOks7BktQBHJq3R_KB8wixv6voCyT3rx_BS7_RIx90gi5yfl-M9nAwzIVVRmZoTMOUFxrjZ4i2ed7hDR5ttJnI25zJC4AUrD6-orqs7XqiDRmyFu7jB-rJUffbfCbdWwPs1Jn_0zGkGCWIOraTF6k910UFpNB4FKVOOgmoU0pdrPIWHDDOUrnZQkjVnxoGH2RwBizItTOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WHIhKmlg5OC4YGfBzQ5cpL1hbz3HarE1wrN8Y6dyPMozJ9YR7gzUV47NvIQKFXNoO8QSaosnhA3CdmNjSWbk3bqfaSLkYq8QmMsTfXVJq4R9Mr4CdjbxRhs8FhOjgsgBnJOH_Alfazhy9atFMKmypRVQcWEZHEjuFrLdx69OPbRmy9j-R42AlqyhhI5dxgQ8L-0S6LYN9m-x9pI0JhhpDYnAJm99oqSEdnUPtSXxCyjjHp9UTZvpsUHUU8QgL3w_tZ085EZOSsq_wKRLN2D4vC50-qkAKqIrG0goM5ZG3MFI18_l2YeN9jBGucwjaQGe_rsY0UQhM0Ui3yxWcEMzUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VSMm-QsQrdWnwr8RAA4Ub_HNMGnCUzi0U16dqPBoA5n4xdaFEYyLTowJrwGXmvmMSwfvV9ht0AalHJVaTDPGLTWkmdti-Khd2zIkaXnWAbRdmH0HuUlH_-7hNByczyDg9ZnnXAt3xKGOfM7ZyITy8pETUvDbuSIwopOs9nSdDNd2zaRz1Id6k4e6tZyH_hgBAWisgGl5B7lLjr2L63KBzUzfBE4oqMyNpLFxvH2IgxoxR2Rl7uBkDczGqIBzNCambLbPE9h8RsMondq4HPUFyu9k5q2_6AGaI2tXJyJsnID4_zOZ2eNpprfV7vTQKUjzrPyHzSVcn_1xJDPq0cl3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PT2AkvPWF8kRJNo1auiCtVInkJ0TY4seLJYxdadk4EKuYeAoUGWrL6zMEDYaRmk5dKDJLGMIm78lCBEy2Is-oq_ESaCE7e8Sxbo3GFlw81Yurqf3qYBbQy1eVNKpDS7v9d7_jveiq_HArJQUnW4OGo9OEeKO9QQAIq-CV_ugOu8dN_mCONJhkPw07G1i5Cdlvzipz_ikRmco3n_Gj0l1yUfZNvUiWBWa-LqNjsrxsVopcljXPme4iyaRzvZku9M0wfG-hnnk0cddfg-J_1WxF6b65rB9Zh_X-VLuZafsXWG1JHc82jI4gaTZDRRYeuplFrgUOYoEfFUeQx2CRoImTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LJn9qr7l84HNekz9aUfC16CWp5g6D2ksWVC1kCSzuEz20CIW2M_Mk55MfbC7diQ2Oa8szpgabHi9dnE_1pDcNXGIJsBndlDW14qbinq2-jvqE1CcP-pRO6rXvAf4A3SmHMKqPGBHEA2wVURDHnA5LFsPx6CjvFevcsvw9Tl7CIivkKSJH77Z97UBjgGcTzIIjUPsogGi6hTPHhe3bw7wXq04_Z0pBrVnKQJeHlohRa5EKGwwU6j2zYwi6X9s_GfKFiF2rD52l3vVsiVEjeg0XkfC5c12rfFLa138UW0n4yMux8_9NNSPfK-IYqvAUcyY_ns8Q9Dr-6PLmzn6706FKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HYtD9vUWXg3Q4nLZjw3IAX-YPKxaIWZ2y5seUrhTDtEhdMzlAddb5gUJijo9Px-ay2Bv1mEhHMebw72_ByGSa6cFARiRYh_5kqLGz3H6-OrP7BXt1rE0USTMvF4TwJ1pLuEPO4yDlJD-owGYpXLlt640ZmZZzTrodFF438xYwnxv84jrt6uE16vkm-4hsL7Rvc3CeU5bewPOe_gmb3J2gPipvkrOwI6qRtARo9qo4rd3avxWI2YTNHzfbfVPlvLcjgcyjEHJr9c5qy0rkhMOM6JfRFBCqiqFhNVXw6DZqyFTYtujJQNs0kFdE79035tlPhD9p41N9bP9AD__QvDOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JPKwaz5KQBVlKycdpovMBrmnKvuNbIKjzPRPorqt5JKkXZgk1tuEikq6A1AQWo5SM0Ftuvbpq90SJCmaye9PnNfUXNmjsVNmnOFGwp08rcI-H8bTaaD3NEvcxX0CZAK9huS2B1JxTBg87Wgdx4c166Sc_2tPh-Nj8wXvzYLzeiDYRC_lOsPVrZDOeuliA8gisglptIesW8b3yGH5CGOEeF7X8gS74mN-anVvwRd0RqXit7BFw8fslgBVYbI8BPqNFaUglAPVZX7oFqUQ5Pm5X_hAL8tESfbpmEYCIPQx9hVie6xvU_y6Fdo9COVrv7y6iBUaqZsO4ozkGjtHY8_EsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dI8mrIRiYmNyHZ3fqVViEXK2CCTmeeZke3DqVWzd9WDPcBuy-zqIuR2qcUy8lYFvlosUElJK7Ny20BAfnyFRXcyVlC_-rO4nDXLN_OCwhayy_GDk7tHgbkQhDQnmKulhcIdW7inzLYiM72rmuRG8fkgq9V0CiM3nL1ljRw4KAAIjPP_0Kiz69jtlT1hDmwp551uQrilWliYAXIj5pLPsGAVD1pjm6hxAJ57H8b62lpOVPIAKJaBgnlQxzV9LZSfLRnKlAWFsHvPAQgOQVBNW_J-3dhzt9YB7A4jVJxyfI-iGg1ZP1Ozya69M-8EeB_KQuqaPR7fcb0-Gi63jLBZHlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/skdlGRs1CjAw4zmPrjM5kuORQsVBuWnA_0SIPjSQvnptYpEV8BmbHq4wOG_tSmlqxLlCxZGtfNOGoNoMywUCrz-fpFQLeJNa13jSpGiNORzF0sEAdQjGdACwZaa1G87eGGLYYFxRdENiLLdGbBeLrhvKMjJgKV8nWWyVk94q0i5ZpLY_IJWmAHpW5himgxeQ_cr1MbJpv_uPjF_me1TtJ-MQzCbWEbe2PpKW1Bxf7jUSotXCHj6zGor3Z-fH14ESvkXQGprt2PwWJgc9tEczU_Ur5F7t2UTi-0b89j5AW-BMr7criviztOvu5vHVi9vpKVYwPCXfdvhcS0X-xWLlfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KevzP-htJ4w1GhtMvvcarim5Y_aIEY19iA2bnbcW6v0icXmb-dm4uQunPpca6znsqFHRs29iA-Kxc8kBN7KUuWtHsaT8RBG8_JiVDNirRy6MDEN9qQPjb4CqpcqeK65j7Gi9_S5sVNfdptLedH5u1jt13OmHMpA_Tq3gEWX7w--5mET7FarzWybktjrsyJo3QDAfBekfkM3RRBV7V7HHY7tvARLEEf9qu9bHO05KAxy5o1oxpfzcSd-axg7cXEFeWTS59qc_zgaJKMmmPhORbDTXCoetR-vhzntjZcjTf7dOnNKJEsXzI0nYM8q8f-lTKzCT415tJ9ZGmpqsgKJmdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VEdeah9TOVoHfoAZ7Ik8PubTxLUmZFnuRQdfFagrS2g_czkOJNzpG5C8rv3D2ETMZours6NKN7uTM4nFFpoPQlPmAJryJKFXO2LcGFgbl8lusBiZkPYYWCyWrastxdrvs3_-u_CcLz1qujKfqdsOpUNPo3ntzpxYJF-fBYMOJPd6J9P0d6a09BFIIVo9HGYQX2B1LCvh94vIENB92qJvSwLj8b8cUEYwn20Z14SZdNmPtdQnJnhsLodhLMfG1gWVmfKeEhUyXM00qrhI4h2fD87MMVMY7JNjN0eINn2Ep7IdD8LNUUEHcZymszc9XQ2NKrnByUjdOVry1CDv8UsMYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EUlgrxL7lVp6NL6bMJT81kYwR0YmBs_U0WcP33c72scKub45Q37PeV33ndY_sQg0DEc0ZNbOU3nbUJatc_GwReIINN-MVc3RffjrxWdHJl-5tzSvYe0xNVzPp_3l24kCsNyB76xXJ_ZT84U-ynqQQxJzuCCy9VpY7RP5RL3Zgkr-1QndpNOajdIJ_GnGsBTbL8aqc5uC2CEVANg0KEHd47mKvef5iI-HgX4UbYxB10R49SOYg-657n8qac3QDgQd76O4F0xom0LyGCDC63d4QhChUcj4pR_R6TO7JFd-wQw5rwBGK7XYyd5YFybYAwM0OxVSC3Z_WVyeSGi3ek0uXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2uSBu4YDGBnaepLLiOVp8NVnEliUQTRpjR29RJbhvjfgIJRKWxWmryaUl0ZJ_fMk15SJQEEbBcoiFXTAGCZAPO9LYoIL9shz1UsWfRZ9-8_OkBjyziPZ2EOUOtwlJBffLafPThsevmo4Dg1W7FINMVEx67ZR01kDRBy8GJfXWUuqfjQlv3XKWMEByBU4IHp3JFX3Orge44NHgVM1YbPO7rTF643isEe8fPpW2nYvDwHYGV3auwBN9Y0IWW3Vtw4evwRh7NCaDGhJiU7BBUb1BesCN83BOFXlHJvm9ta0Mhq81qgmPNvs3bL89OPW_VuvDI6FO7nSUMToC4dj4YS6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=oxLr7swxQG-JliQPw3BGmo4E1yKimKAHcmIQVgPiJFiV8TJv71AT7w0vHwopbq2jrwIaPyT86k-MyQvyDqAGoV4Bub-ks8EE20qL1hBItNx01xlofmU5xWEU5C40CYs007TC_aUBrp1lIyykBoN3ICJEEocOvhyoUpNIhBBow2KWv-qB1SEr8T60Ymr3XpgUTsQHghdgkAPpzN3oM-IbtTuvrVAQG1Npl8UbjX8qGed-mYjgGhdx3GO8--sMj0lojsIPMZpC8sYMy8lIeD8g-CvzmxxXP5f_-IOauE3p-7q5OtZKIQ5oMJPltoGEtBit2HEVh4Cbeuhj0jOf_RuLNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=oxLr7swxQG-JliQPw3BGmo4E1yKimKAHcmIQVgPiJFiV8TJv71AT7w0vHwopbq2jrwIaPyT86k-MyQvyDqAGoV4Bub-ks8EE20qL1hBItNx01xlofmU5xWEU5C40CYs007TC_aUBrp1lIyykBoN3ICJEEocOvhyoUpNIhBBow2KWv-qB1SEr8T60Ymr3XpgUTsQHghdgkAPpzN3oM-IbtTuvrVAQG1Npl8UbjX8qGed-mYjgGhdx3GO8--sMj0lojsIPMZpC8sYMy8lIeD8g-CvzmxxXP5f_-IOauE3p-7q5OtZKIQ5oMJPltoGEtBit2HEVh4Cbeuhj0jOf_RuLNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rKsf4kNTUDWVmrAHZLP3b-pkKtHGrAaZeG6qkpnft5UXFP2eMKNstols5-47CIRuOhoki6DCbVuXLhn5MkK9ZDD_yYUIk7KyvlgLa2DJIcHj9pmE2kw6vFlYV6hb7etWZO8F1pX6uA30zfJVyDWBtwc8xLgD6lyiOsTQx44o1ZNHjdmpY87MvLOvDgl48rnrKuTTFsaMmLqIOksT9i52UNGQfUvFlw4ExwWcQZvoJxIhkBl2fsABHaJ2eXusjyvfZrM5qTXEYBzWp3EI9dW_uTpZugmp3-MasrP8Xj45OP3suWUPEwTbJru1F8L5gjUL0GyeP8oGGDhiM2fR-L2YCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CtDuXE2j4V3v-vOxfAeTMEcUHfYh1A2R3_N0Ry9dlk0GXAoK5jZWtunuZbOLPiO_Rl4GFLuLnQwvbqecF3slhvsmaEHRBgb5sQdDf29dghed0NNjhsuFwfKSZ9loG4-ym4o27dL2XGg-ulS1U0kOX_CkrxI3kckxUGMyDiHvG9sAHbt1S1e5-oQMECv_wd7otYeLt32VoqZzDPPLeuKx3IqoIZHZo1XLbbNiEWAO9RbW7GBYvpWe97QEXMgJdpKGOP2gxk3rmBeTcLo5_nRCwHj12nZYhpF2cORKMuR2KdiVomt-H73CPl2W3xvZUF2tCCPfludRqC-50CTnaW66yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FXdVz6wdo45AMBBEXYwvzrRMcQREUlJdvFG21peZH52vlB4xuFVUdToK18U9ihz1c85NYqY6ZZT-2gShiJJvd0YN0kxCi50ySFCFU5KA_RB3DHZwnk67hqgFNCuu67CctzjmU09gtNcheLIb4Jchvf_WZe8pd5PkLjXO3d8rzm5_s9jzpgTgbWW3LK8YtMtgKGuS8MAffzIY6Z6v6r-a_GJbDR2WlrecFZM80rfFlfHD2M9dUbq2W6KGg8prs6aS5eG7agQ_LKLizpvO7Li0mMzk6yM93YxT85WZ_MRqkwOPnmuHv106sVEhhaP2AckEWRAgomYljIjNWeztul1UFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZsIi76FNaE0wV_tu03tyuSHFWXqy7-oWXeAOtTKu5cem-gZ7UAfhyIE3vb1_8Y_lczQnOgR5WLACPjP13u9uGP2j3DUpDcAN6gfEVf8ZVnr7IulpDUnlb55WoQB0m-_exBKeAUShKydfEDuBHw-pca-u5KXzS9m3aKpM4tBvBcSKoa5KtfJkmT9IdpJOPaHEw_y4jgmyV29oiRhzm5_wc9lpmdhAIomELRJc95DPNeS6Qeu1sqiQCq9LfCLrt0jbExWlcRvAZ9qMiM4Ku5URS8HBZGDzujMssI5z99J7DLOnpOzzYNjDGmr0Jshhi9vsWR-MgavVjdOWnxohH3XbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rrLobon8_2oFhzdtV-6KKl4IfkGb_iutL0DKCVudXqUPHCxpvd3peh9b8V9DTYJNzNVuqkukr859JVZf-tzZIoOqXJTo73DFHVYQM6miqEzatmqmZmrga5cJs_qBq11ZE9JfFSQJ7NWPFWn2cauFrW9M4s4VONbX3iotaVk9ObfLTv0ry9upqUD83z1ull08eaCKvj7kjDIg0TRFHbiWz1BYPNowjugfdcXJfjYsZy_JUZNhicCLQt8a7XrJF3Iep__yec5zumweTSTO56GFSk4NztuV4kRjPQYg9YW-0WRcTdhbNKWXi-w1ZsK_ltscLOFr2A5raCeH9Z4Xa0kOWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/slQRHJFKxraSYH4PjfeFlIZS8j3n120dkQBwHma0Sa9R4YO1Jr437OZ6PX1sY9dCRpmafP4LZe0H2e4Lzrx01PfQ2XwS_T3spu5rIEOZMDCrMXM1T2VC2FSeZewHYekI4SF48tDol5iSxHcDshKKtUCXYgCnvJxvb4ajgZv0-lUYxh6gLcdNl7jpN4XbcfGRsOo-3dvTCCLNMHm8rbrwEFcWmQhoBj2B8KV-uVvos8PwsNzltYAeuR7mE0EvbREn4yj_7ylKUy4PLka7D_8VTpb9NEeBs2LeFLtyAmYxSOUdIIXdC86z6S9zilmOm_KGMTFwKpwnmt0zwJNwaMZU_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XGGdgw8qPUKMh2mjlzpdohaX0Y-PLaA3AbF6LfnpokBpaASI1MXH0qwGxX-AVDMfCORm1tdUtJvrjqQDp8qTOU1gnkJqSmYcBKxp_-EjUHE-nQztKP149XPIZTUruDfPJPzIkxY7VyqZEjiEBgse8nAQrbPWfE8IAkY0RQ5nqO9CdPXStJ1tuM8oc3zwIciq-L4pJEA01EDIYxbIahtCfVJGcp9EmMKavAjmVAswP9MJfXnW_MYtweunCg2ZiQDRTdnIJ1_w0LeoM9SGuXoLg3LykEuYf3pUKp_E7wRwkHIUHZg9XM93vTOAZcdCguW_DQ6AT4iLGwAvUFjVvGe0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gNT8bYU0YFNIcpDf2QcHUOETQHMeUgExR89KyB9D4JESgFAu_NhWHv2iHX7lNoCYprxMc40F_LZBC1A5GT7j3oss2kXFazB9kIl8NnMyTxnJ1dV4oULK1Crg97RCHUkmhXZBj236YZovUhiqXL4UuIE4C5AIUtBEvZ8XU3ZtcPg9nEepzQx6cv_BLja6PALYNjw0CJp58cV68CyRT8tBLJfFpxXw165DnyIEZElMiZ0xt1fe3KIXjh7DLkjJ-Thx1RN-xYQWXw_8J4aI2EkfL2KR_LzD-v9O23uwOIsE4Z7JNnv3ymP8_bDI5Upv2ls7K7jsZX8GzuDGk5tleMNxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nl9AmByqlIQDXsfJIMOFbGV94UssLvys2CJDt3ejRIKoVEyj3PxYWQNQRWWw8aSPUUQy20iXyOoPOyIz4LgzDHwnCDhfuv5qhElWMvs9wzSo4_3ILC_1zc1Ksuj6HEgQ37qFE52aC8iXqTrjDyPGN4BwHK3BXn4vCBPbKcJDVjZwymD2rQ9WzhafMRKsuBxlRLClyTF88uXUZ3xHg1whAzGOxFwuMRZN5jRDV6emXN8vWfsabPksrJkO7qV53IzBJBnbV_l_LGSFylgzZ9ULucm-uIElmsDWp_IgM_ixwL0R58LODTlFvYPzgBccKA4Bon251nOzfsAYPeKOAwiYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TqJqDLc3wlgOmz5mM8rhxeBPAmBuQvKrRC-qMNewQqB-J_mB-hMX5rr2EgcZ5XY2qAQ2XXULTF7vRSIkq9biZhOzx7utb8ysclydzLGvDouq85tNXd4TqhsDbK5gT83SusnJE_lCoGmwOkkfUQAKk6m88x6Orh5ScVJ07dgzQTVAkt2nAq5gqkk4sqMPzRQewaNGCF1V_wlYThJEL9VgcwociAmpAlfmOMcWJVNUtwYeIy-C8Ph1AxIaF7On0Tc0ghf4drQuzTt13EF_ze1CUCeoo9tkSdpmxkn5PcwIf3SrbwoWNu2ElepjMiPYkC0sQpE6pYuF0BjITJkRn5w-AQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UEUUkKDUy5JKvJ7qCSynyGoX8wcRJKmAwmjkUxDiNRPqawdVwuK-ojEbhGOkyxHistr869bqQe1ErNyPAxK30YG-EyMZCFeZHsYwenFckuL_xq_5ZREuIDOMNF7k8kMmrmKqTA7Nvpw1A3_rJVC3_UAVuSbtffal3L5NHSe4AfkA0SJrYSPSm3Y_dHZnMWLrn8O65o7VHjaValmGb-XFh6jiV1RgKJmk6OQrWXXijuM0xiHBLTtJno3uIRuEPcRqdF3YhyLFouImSnS7-fwfQGs_ByDAs9JkHa_igUXgERY1J99R6TmgGTdU8OHq4NWnPHJTcHXvT_n38KAkBEz_TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BkgyERUUneJGkHSSNYi4Yvuomnd-E6a0RV79Nv1iGnX-oRC0zjJBj5gMwxFz7wJkVKeerzbZcqbhaOP5dYBq7ErHXoS79R0IWqf0d_kcqM5ARDsEJSwbO2TXd52s6Gb6ym-sujLUO8x9dPOpEm5v1hdC7Tvtz2H9yOWEKna78LxrKQeHJvExm46i7CatVwh8OpPC8nu3RnXRW9CJOcj1-W4eek3ByhKi6AEf_oXvNGpZpOCAKJTHhBuQbWkQrnrqKaTBZiRNGkbZguLLG9dFrtfMmf2i_r8-9mqgx3TbGZonsCT-JfVF6pxcZEtHhAKgWQHNylS8FZCsIig7qMYDgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b-v_Ezg-_o1UzEvsEpaVuHR7eYtkg0_tnF5ulDC5enrQ3bCOlL2uq29SHgVfwZXist81vSEGGr_WfdE-FVPVHe3kmbyPpWwwExZkXnvSEubK6uO0lrtDWLIH31XX0cQtm0ZvH3PXA00GetUpWGmvzBwZ5bzSRVRoN1rZQ3x11QhDmB8OFX6l8l0KfoFa7Ww4Bemgw5dj2sHUnbdQClxSRFa9TXMqIwLDwt7MxSc657IZ2ucAetBik4Yvzfw6H8Fg1PyR3JOKgTKYsfawYUyv_RzPBebBrmDh5W_ZjO-bpRNzJrs1FMUmoNbQktaOIzDYZP6xWwOUIgiVeoW_IyouWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tp3iRFYBM3BTVPlYqA_y1oykWJBq5jqGFfQaXfN2lmHjNq5G_ZTo9-tWGEyW58nO6VDXgyAYYhRVo4HtnnBqRTc26Dyo9ceW9aewecza_t76HeVsnJhRQXjEg1OrxOUiUM2A4SWk9kCsv4THiEkwv4TJ9jYhqTtnIBrEADC2PtfWgtwhU7M0AYAECmzDljzNLIqcWomMTmOWkUYeY4unPynL-yYAl09KQGsQR3WYsMAoymnNE85jd5zyab-ZJ9wHMSOIAjrl4Gq6rsIMqbY5af7w_O3Vbq5HRdutImU0wMSTcfzWwsUxOe5d947FycTrJMitg31pfsJLArGQWPYZzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s4ryOMSlbJfVSRjmdJ6ASD8SCIxBNUzX9KKvOIolK9AVJfIrbnLDIUkKf42jMt5L5kv-wn23UuCoj-g3lrg_KVzog_gVc4bMvsUSTXt4dTvcAhkI4nlbMRzx0uf00gw0uwXwqRd2i3lcqq1tMw4QoP_ipNLi88Su8GlqlE1BpVRkmSt8WTWypMHJfMyxrjXTGV3D9IdSd-nmWgWceTEwJAnA4sj1o6FsTaoHGezJ6DB5JIPqEX1IW83qx5HZNBfkxgbgS8Tg33nTTdzbrvL2Su77x8lLexai9wOfD6dDx4I3g8GtTH65N_qQMdtMACEBqQxykORJCO4VZ3wB5-zWKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ndlCzwtxW3KyADTE6azCa9AjZpvMjbaEwJHa4QNa7rcv3htfziXdQkHK599nvpK31LO8JZ9jabVOvCaMTz8CMixi2LSxhgMe4iOTvH87AwqBmOMoVX3blexznGHvORAEhSa7YYnHYjZ6pOAACQ00I4Y8VMqyTr6bQgCso4bN99UGKJjeb9fjTswNPFL7iuc_yYEQs8S0eIuRb_RMdh00Q4t3xFsnia79PVPQ3BO4OgD6sjhrCZ3AR-fO-KgE84c6hgbaolcJAwnTdR6mP7MfGQPU3EbLrfejZ_eV4gm_YBITyUKzEcR99jGzQrebhGQ0J0vs6c7g4eOdXO-BE5TGlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
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

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GRe-bgCG51whrn0QgfrGAoFjNgOFTLWM01kjNVqqcp6KmdbL_aFsjrk4Nu75BaJ1DWuoPd2OJHxQ3Nxx2RzBnGpc_x7l2nqxg8wwuSviIFv4w6laQWbXuAEVmO7yV4d-Jl5_VA_Tl4Z3snjYhr-BWWW0aoaWEfUt7BNBIjP1Q11QkcpBy7olbC9WBIeawfKi123vwUJ_DfliXA2BIOmCXlRj_NPfbM1-yURlSaEH5RIPknh6zvqmEFX1k7i0kmgDvqhP57phT_dJXJ2Hfubtimp8b6uxs61H6hk8AltAbtr3bVVHzbw8bkru-RCiZq2Rat7JKH8-7NZVjCHa_S4MUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oLwidKvJtFJg4KvkDNCafJDbnTru4kbatnkIya_F7yPDWY6oDW6JjqpmHyoeaDsKOgGvssvoI7Xt1IwsDbGywUu4S9IefRkf_vjDNGchoNTppLbcB9pboib6u2E9vDoFY2FuEzzlrkpEb4YeejRqktq5O6WFwGq2Ce3ppb4q2ep4HBWdM4_NlgwHKbliRFV7MrZZR9Gzs7W2JyiutZ_meCxWmuTFyR-Vt03eT12Wen9ulXKJigjzQsQkhxfMAffhizvxSOcm0yVOTAikQr9sWtGI0EcO6uag3k1EZZVOaB6mzkXktDugEBG7YWNW7kKZUZUQcto5E-ZueTcBZILJMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HHzGXvfttCaFRCvEXY1-qBWsKzjc9dum0O24kKe6ltByfaQ0fR4rLSk_YNI8WjT93N-3XSgP5x3sWbtV4isMxzPaT1itanHVOjc6M29nriyreLMn7xYK424iYrILwN3h-OdPeuK96TA1EiYcH5Ks2Isz3DYQHKmqIeGaBuvoY9B3h81SmTgl1hx7kQdozZXnniP_c7jctH6Y05aIW4RXSWBgROtTtaVi67Or9Szx-96pYXaA0KwpWPl3gUeC9ip_0D78KnuyDF8F9HOjkOe84JucTrxxdneK4WRTrZBXNLwYQuWqeoZ3gOK-wuZ6o4ZyXdkhNKJODm-udHTHw4yIOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
