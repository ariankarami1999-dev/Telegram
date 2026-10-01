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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 09:45:22</div>
<hr>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YsMxZGqPdE37arpeNfdDAF1WyoaYAOtxUeCvZomgwyL-VJ1_rg7ABwBXSXDQRN32B19o35KvQq5YhqMPb1zoLhcsQWFyGkcravkhtGj5LpEzvSU8Kha2Vfw7Gl7IHXilT9ApSCazrY6g5AUEadCInZvcCxCORXoKF2Z5W-kgeNT-ko5iIf-nSK0mEsaQVG4gx9w1fCPpCwebJZCamE8_e2-XD3TehkJ8512wurNtQ0jUsnK68_NSL_itwXgriTMwa05e32pE4HvnRthcr2kVedd_aqN4vCa-9uw13zU7Pi-7RRJczc2zvZ15_20-iVDuWEUsa7WAr_1hJWiEHjcXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BqOpBrai-RR61hCmLNf17sHEu2Js9kdzfNjYvLQwa4Z1DCulLPZZnOV_z47Z1PZbq4GNhjCCtKdYp4-bKVhvZDWqJYU2qz1fFOvhrAHVFFnJhYc_qWv_uxgofQ-WaT0PSqPzr1k5RhHEIk1aCQKjeDxKA47hGVOa9Kt3NQ3EQMpkiZlLJT9XqAjuepkmA-0CPltmvvgA8HJP9JQGQqP_5-MX-d425i3lfYXA4jMrB2KFcD2BSFNPkfO8tbFLmgRwhw_axdHySbGk8QHBTD4qI-MpLEMZOnIeLLoNdyArT2m1vPTeoFimPd5I23ysMUg56t4K7atbpfA36WW8AA9xYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EuBXOjs_X4r24dCUgofapmal7o4Sk4S6VJZQ37pxPXPJmirXEx9it9hcS2I38WWwMJXLw4rr5uFmVYHuF_YPR7iXOoIguhHmsckoM0gZ-13igJ_ibegpPGa46-TYnpLCQ_lnkB5vFKd98j7nkQOHJy9OiWE0h2f7yH6Rh5fHB6Ed-K9N5D0TNZF5Y9DLR2HfmXJ2GYp8cHS7f-EBslcm5rimAOWO2V1YRwTMQ_Npb9VWNtmWKqtD_DzyNR7CVNnPN3R-gd399rMu56827Ckr3exBECJ1K582uML_STNB6DzWntsRDfqzOpML-MtX6203GcqMYfc7JATAivghLRMFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MAzX5P-q_-w8EjEgz7EBXjudW9VSAA3Tpj5grPJVuAULkAbGeqR8Y_vOFyUPYWpMZUQQxl6rmQZ67f5GBjceSukNq5uls_txEUSjYf47IVThsEX_10VSKGqC4GxYgPsGokbU7aGEzm87PbOmk_MKjQf_CB056giam9F7AgCEOHoTxhH-vtwysMcVHECnjlyc78NQ_L9cQH67XTdsM5tiPrHEhkz1Q12SgUEfirN3Krf-vlFxtKEN_h-zaw7EBcxIMoo6a0IDsd9oaUQBwqI3eoW8MIIGYDCPdJuaFvY3GyczYe_3naJ-r0CPWS9G4GDqLeE9QKL-rt5_KLNfvgXSPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cV_ZsMOHsR1d0JcYOT4-RMAvEjOrjsVak72tDm-jaq90OXzchGYbyJ6clCFpeKhFKmB_3_JU5z0h1qn5-x69Dz8QHaV3ZHiJ-Fx_6uSvutbQ-FZncNgsbfOqGnHW0hV5Zu7k-iMsduuGWvczUCdgqBJjuFphvqtpwxosP35HrwySyUI95Lo4CDvIb3CW7nXFNqmAy2jFd0lT4h9u0FHV6HnDw7VxC7ujUHHlbeuFNNPZ0v9YHQ-Is3qupJRdxBm_MjVkj83GyJTod19zqoslvjO7ChilnYHe58PSvZTN_1NVnkKo3tZBmTCJgdfaz8zEvNCguqkObw-6tVPyYdGQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MKToAL18tfWNieR3lWtb-TWiLHX5j-bSi63MFRK8atWBCWBeEPLQGXRlBdtG0g24Zy55yPEcqxO3ecMUD85x9f7UbK8iLNqLzeJGlv8K-q6NhbI9APrJJVv5-4DZb2o8HQWr3AdDWJwQf0Duat4PUnrcdJuU_Ug3ZtcYbTFNdTobeFbtZLW5eYBOrPkMiAspOuY5Kivu1Yd2aetuNgRHb6noa51FC6wuv1dXfBh_7RtmbFn7C2cCyrlwOnkR6QXjvk2z0SV2ura25AyhUbsWOi571fe4Y4agz5dOzN3Obiv9Lur0M0hcv0rw3xGPNKjSuHHFeH8KM2EQr1Dh3Jl_wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sUgwaKnQLccxaZwLnu9y9n6XQmuvJW9afpIB2-bz2eEN54k8gob1N0mWMnSQ4b848xgDDBaRo4x0r2GSOR9I_tGdPAryS1P8-0lafPDloGwWz1NdcVBx3q-LjjZdFW1z73CVE_F7FVUc-mDebCitRemZA1_PgSigyL4pqO8-pN0Bq92QBwvFJhodlqHMhYXwzl8wxaVV95ig1CDJnRW260sbcpZXwZH13JGbcgzb36h6ooWhd8o-1qyclW07uSv1TAQ38pghnVgWADed3Lf9X5KtHIExKY8T5OHgHsoy7pOfaFiM9vCthi__zFUDDOnYqsGV_K4I5z9wfCmTnfN5Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vxh5BSuzt_Ky0cciLjlBD6ck0pP9FRNNYcwHHgVi8z3DfGhgzKub-r28hE1f2_1CQcJyIpfvGBu8_UEsc_NpmTpjTpX_elv4ggXDFPsIba6KC08mGUMEvX9QFHnEDL3z8fVfnUzaiQZxUXdKmckr864YRdCWiIKxFay6HDCnqP0iaN6uDwL27H-fq20C7gKdbYxSuRB9Svkb7b_e7l9YdnT0bZwVMdz1DpG4AKM45lX9T3v8zj_Fgx6ZK4L7NpZW0raeCKwE-PdRTMPmpBXssOufiqvVSgXWwpCxiTixGkSX4HLps53vNVlGDnFZy0CogjJ0nnHJb0d94TFShxZBLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DLrxApXLiQ1xcfPvVmCz025PJeBmAv9ha10_M5-JdrvJoQUj2iFkfclIjj5NzFJVMiFdMoFrfT_qBhXpGdxniMlzdiwk1pNyxYsXtAcOSh3GBiVk5ZA0CmAE314ruDhkRXqJCBBaFX6fpWn1x4zOpCYv_1zJTUiivkuYVI0-oRvdIVrDk8pgYCQ84B88YFmZW0IR-K855R3Y6r6l8dqEFjOI2n-K3j8oStDqAxun8uEWI5QzjG4LbVIVr4kQQzbxik4s_5pup-LABgoWTgAL_820Y1A9YLxUuOp1UFDJ2KUzTseQP4QBxFtCtCJwJxDZInGwbF_HqkI_bQZiORMcvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i0X3FQBlLl532VyT8RtR84FFn6BInGHz9AKvNbiMrY_B8Tu0_cz0SMmwI98TLGJsy3aCMhkg0Mo15jSyi04-JX9-Bs0Xe3BLZZGTCGzlM_ihYl16kkhYar9wBoaSO_caSwaEqkeDWdaSMaBnX1fjgk--jsnVeaytyb4iei3odI__BgXaH1zyL5NDXFDJJnJeHVwesaTCMliVmnk1vvq2-tnFqyfaf2B5W0BjqdWsVA_9lW-_NZRR819G26RFYSNMdNGw8lEAHb_vPhYD4q4xexcsjBMcTIBxSnYIBd5XREh_9XKNRtW6WR26_2FeaDXPYZaxWRPSLmW5OiQ92R-6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GM3pKFUnvtq0CMogpH7EUs0_22Cl70dAt8UkWAOV_YW0OtCL8ElS42dUk-erVqvDaoDzzEv1-W7xW6z5-jB0e9MRiGV7wHrfmGJnkX0qYKqyCAI-eAraeXwvIsOIKfCInzI_w29ClxssG0AX7sQsUV8V_vXwQNBknq1Uh5c4F9Q80Y6V5jw8EuFz9QI8tfqrFJRQu89SGwB_zbMZsCsRetOeFR8v9xIgUytZUJRHA-AtEyleRwb2fULK5HRnsGEF-JSH0g3lt6tdUeOYK-iYTG5Fh98HgwHnspDnMsVMW3UggUrmX6goVI6bCYsVyDgQJo9K9DuQbxUI84yhfrwcFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U90lihevcd1rbzMHdjDAN9Zuz2dsmY_enVzxvP2luNLCyYkk1TT70e2Cl1odZqBR1-9pFM8b_pVY54-URQbWIwVJBZPPpOAANPbUDmVLMDuFpWj6Cn5Wy7o1vVGHYtlthU6K597IAUyJGLnlQtl4a0p_Lb4oGUtCvOLoB6Sz_oMpL_pApxnQUeVcfJUTyHmf4cDlZTnxS6LMBf_R379YqT8c5LENIsYck6fbTSQdXi5fEHOfmZqHNKbvvATVcdAcMG2OtI4Jqj69V_vcbzPZzBmC8fV3JPBMYR__3eja2ewAj9RfOtj-yrma6Pjag3G_u54wgOVmjiBwHiv_F_8AYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zbp7BrogSwig66a4uYrRECrMF2kVmn3DMXr-gWWh_QUKsB0b7FE5Ue2pvHH4gDPIziYzcxGz8B0en4KfuLIz5rk54NEgDpWjKT52sujrUh_ZS5N2lEWc-Qo0fUIYUmNw75WLZT_Vr9sRxWwWX4EhQgDWgJnyhTcGfWUmFB7I2l3iRRYR4hEfHdzpmsvQauEzS1ekj8IzhrmxZAUhJ8MN2RfAPvSluL7kF574vnEK_sRnsb_M9kVoXJqf4t2FXRcIoUF3lXgm6eYpTWCG98I0V_w-Ap-H0AMUVJiA76krTX_9EM0jVFsCfCxvqApFEtftEOjkUYdBhmmGW4i5frMhNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rf8r7mHuPWt4VcbyrMtVpK8dmwiZINfQb2w9lemdEG5I4iOLKK_grExd2zOuM320uCCfaDUgk9g68oCpz-jP8z0tFPvVbHmtWFvVTpqax7xI6g6rq92CLspwDoVbcRT8vNzeUEhN-7H1o1TP3fL_lOugUQOyLosYyPjtIpYcB2sFL3WrZVV_hWaRMgpQTX92cLDUU69Ic8LQblJoc7jCWformd0inID84Rq5C0q2oFopAg0RZD5xAenPoY_ygQQqYIKjGo0KVuoGFbRRhptjDt7ofi0cpG0N7VPxP2hJkXwG_gRilnxWwPMxzKOfKZ3FZiTb9TDwzcDKZIVboum0Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fXKkynhwxUaISfe6z6FYJ6CyuuiPgL0obOwiu66P8uqW0nwbUV8bjRLCvubB4Nsub0z1umYicTgeKO0un32VMvK9ENuAD23vata98drQ9FfsJKbwVDHaG0306Eg4N0yNEHHGEWKCvmzJmoPJ2bYbbkOiDEQ8CpNQmo22IAhdSAOZGR5WJ_ADjsM2JwQ8nCQ3uOF51grrFw9LM6_HaaVSWVQqbVe7HswCUrKxufMD5WEisPCOPVuiQDzKwyf4LsBO_3UJiTjQqgqQqN57UL68fLwqmGxG-LSlo_mof9rZm0cp6hOUEqkq_dGCMZCph-lVfvK6flSgeQCSjIn32Bc8Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HvqaaY-YxPaUG9pqIM1HzMTCWGVrEAOwHJ5P1Y9L5z_vm6Q77TemoB6IFjQtqpXxWWuQwhjS8jSt57Kgk1RLeC_nRHib5zbVBxydkwZpi3cU7XNOSwKgIIHPpqT6iL5WAADE8pTfwB8nHzSqmN-FEQg6_KEeU3QN2eWBA9SaTbAD1nnvG-q2CbOMezKvKyiO5XKpTT7-qzcnyz-D7jK7nJv23FP1pJpZDliw6Hxv2hISglY2Wjt7Pkbs4RnRxGWZe5IMOx6fb8ZXtDEyDnkqgbaUfwpW-jByyB0u39GS_AqTSCP1ByxP2dxg8gFTEOUrPjnUS1qm-ZhYqWHrcNgasw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RIH_Eh_0FJQwG0Br59tlznn3FMHCRz1wGRbsQOGBzW-Gns8LtHUANH6XSolNhE7QGWntnQ2eaWoQrZx1-mW6S3yU40xm-RVGuaxFYtSLEo05ufoOo94exwF5_B9KL8lwYbqCeXVudAuLdTFM9vau1Sh5iPXPsPvC_WvkZ_B_a3fjviGzp3kz-QVbchrFN1O0KqMqIPb5duhJgj6xQyUaZ1TgkcW7nOkUDzdkE1zu8txDQ1TEDvCNm5c8hQU08GGLe8viZhVE51pC1HMBI4DXx8H9jakM8svEdr2HBlMgMzmgkXiW3LLTgp0wSp22wCEwPKS2miey-X8Cjjy8rm4Myw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f2UvKcrTA0LLUe-sH8geWGopUpNCBy3RlVPj7-AOOO5Erxqpsn2Bvugptuqq148tNzkgv4MyXexT-_QMtFk38ElD08lyT9o1aM8g98cp2RnBlIFKtd_TVEK3WENhZL_GOMEWghEQgAOMk1YhLVcjPtjKXnCiNF02GWdI46M3PEt5Ih_EiT3Njy_iLMLUKoXnfzZP4KWW46_ndLsLTwEHYR53FzRFYLKmGsxN-2NC4mRxBJlTgNlJ3wbZhOusa6nwCOPK4aQowxM2NvuP9PSpKKbyzIlrvblS5UviCvo1IF0h_Jqm0yF4I9pqUJM84i2E55X8oNrJHeWq9H-UMHzbwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PHZp00vljsaHE1AbftdsaGWI0ZmFERcknDBYBHZ2sXZhHE_y2A4oT57n2B7ozHnlPiy-1CmVjA6VBLQVianKqwqzfAL8q4epqr2GdxkWTnRQw5921MkK53kpCHj_Sp9FfaVFWt7cR-Cnb3PbxLbucXd3e9U6lrrXjff7P8gZQPgYjXkw2PZ0b23F80_Uqxm5iMHPos-NOdU6ENPvN4JMyH-py-IpLzRDHnQ6Q1JpRcpT-0w71i7PP419koKOdY7rBvn_TdW7-Zq81iKXb_QP83btDZZrbm3HfzOABTVt8rMW2jOhVTjvq4Av-kUEZstxCYooWZkvnGWm5ehGeblZeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MNsG9w_fa50E8l-4D7rqhzRan3Q-JRs0bXty_DBbrZFko06LIrkK5t3Q3HpHL_SR2GOGs5i95k5CAih3S0fOYsykyrcNPyXYC0pQtL_ByR_tC8zueLWUMh0a0PPzYmzmhZ5foUgWLXnVHSifaEPgt9s00yCC2HrL04XkePhcSkzGNi1q8LU6DeBGHWQrB4LRJpG92sInx7_v-q3ReU8Dkqt_OOBS7O0KOKCBWK-VwZjeNUPmlA0L_OOqPe7xb9fWA5jV17F2qiePXntIpWvur1SKSAHAwvbK2SNA74u5n0a2qtAsKqapda-osrFrFfsuup2Fp7huZ8Ib6pDLbxJFFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NUpQA9fFkBqXJD3N_NEort6vXfDbOyGpRec47CDW9n2VBKrSdn-oN3kqBb-Asviewiio28wWq3iW5gNib1npD-zWhydJgREb01xC5LXYdoJF6WU-kD6GEdURuPBQkH-sYUZVha6IseQp1vE0lMh-khzuqjqXwVvowapJ-oiyhPHo1Gar1qDawWvEKi_bJbb7uzHFHexpM1LTYqW5uIQfTirueYZY2El-SBpPsGfm-CygC0XNHyHlqnZE31N3Dn22DizMSJgz6dgzaecuCX4pdCptUFJsdfcJ4auBGD8VRTyhVqEaGVtNv8OMKgUwH4XEN4IILBT-HkHw1OYD1vQO_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tsIUOUTntoNyNdwE5LvI9ndvWpM7XbgQNR4WmgfStRxPRDBoUoRXzOHgQoeipqqutbBnHOa42TcD4bjpLX9eABSDQTs__jG0Nq7AeBVYV_gH_uYFmYi905Br6sgtrtg9a-7_YPdxRTNlF4Iy723HBV3I6nftyoX9MhP3fStdMMA5I6vJ8CqiQ4rmXLkuZNFl465l2kfxV8xvDVF6BC4mKfZPabTwUqX2gFTk2SwaFHpZY4TZw19lqN1qRCT4V7LxdcZrrvKn0abBxCc3vpQS4Tdb-PXXCflM5yubGvLJABTnQcd54gPJ4WTsm7LAOoh9NHWSkJqAkLIz7hgfLYxv3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ha3DNr3AEH-UBeD4CDfGOTgvWIABh_bQypbqN6PCOjD-WpansW1PhEok9FESjTFlLkbFoIAneYqouODfx3UTq_Ybr23niWHgc-pa-CDnYvknXsOKa5Gf2bhuEbrpbWjIgg-rirRS6uXZJslRaB0Ohe0kPsaI27r79x3dhlE85STpGDxh-C76J6femUpFwgoqAH22uaetp91QUWAy36OyIcHqLsEfXXPTiCqfoI9EotJ_-7LxQrXJrLX5vMN_0aIkd8M78sCEuAbRI5_1xXq-oIVY25LiiEh0Y_vxqAhuNeAdyBbgPJ2IUWR2mOfu8xabQthRuwbjxsXB5NLC-27JoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YD4oxoZBQb1F-b2petJnV1uCLlZ1gyV0gy2tSXSVSIfEZ4ivHGpgoQExM5mrQspwRQNSkjK39sRkby-ddnwN_AYHlgyPF7rXSGKbCmWA4-OXXYrgGNQp1FhFoVbCkx3FFK-csa7JZsLWv1pigrQPKUBzQsN5swC_vYT8XNLELH7osJ_thJNIXX04xDXN0XnwCekvm63H_pHGeXMZp12Kf1Bb99Ru8vsvoxF7tCwbVuVvZQQ-UGhiw_EZSpNhr-cevIJSGvVxaTEDKeM_luPpQ41d57WGAN3gX55t-Iy0niP92AcNUHtTZ9ky4DUk4PhCrqYYlRWlcmDdpyLBt7McRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fd6QvUxHpkDvO9RI7-s_WYtxFTxtlP-kosLeuJAft21IVzlQXgLoL56TXUKDxJDGDderAwsEFhngorqGgboBa9oInhoHUG8pk9AuiirjLYIKQTEZX4RtNxySOFIPuyQfEAe6fptWrtXvMW2OIjBy5YAGUlinZTARivhuD4AZyIVMiyWk-JAlLV1FPNrpKu2_Fjb2OyTcafkaqNaBPmCIBPhbMHVnq56BTPkyHpxypdPCMlfEi2IfN3OzNAvq8djXfaQWNBPYrsIlHDtOk3fx49KAYrb6m8jTjMg03UzETZ5F5roREY8or3eYchyNHr2BcPqK9_KyA18zi2QJl-lZJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aMmkGKKjjHzrbGL1eQUhnwXXYDsN9IcpwVjpk5qKkP38A7Brk1FY6zMtkHIKcrtvNT3zWI9ph3ZGIshOZNwVHFivAfNQd9ierSmcUgper7vGYgUcWq6LifxcJCI4yTVKOgpxQjkcFvRpfbKI4lQG7_v_yg5W5qYhFRAmGqhf5NyWak_WieW4gWcNP_N0EpoZKmeXeLxG0kNCUzx4h8OxaGtcOXKr07tshVQXp6rbfIt6XaLdqawvk2T1u1m6a7ZX369XnDxO2HVWwjnaQa01J1ia6QEZk_C1XblsVgzVdKJHgEGW0Y7diw42KHY8VdFkJFXkOvGVHiGRpcNC3xb9JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RARpb2oA0SwSuaJItiJAZF6pT3rqUyEbnQb_7g0zquE9ZzjqutYapJFgp__mynoAZBFcqq2btGt6poQi0kpeJx_GBdB5xAh-Xj34upuAoEpin3f_vUP1Cl8eBJEez7C42_GiBs7sGAkl1V7uwWkuDMaCXPvDpzwS15O10TWvCWAMQBySEDLHCUF1TUQnhgXb24gCkgWV7Sbl44pjg5Nrd8_V4iD0h2_yYZ07m0-guPLVHbFznGjkRB7s_rm5kSKOUl2BPrVGOGcT-RrZv2CXDIyuoLCC9-RgZNXRd6M4pV27D-SJmQqd6THMoQUPflHrCMyapNMW_thZkiB9ubW1wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=omNAJKmkBil-cglwwK5tsOFasa1Y1p_WhS9AIqpVLhuYTddAJ4J1VAolNEAuKZjCT2EBi_jRmevcrSrNGVymL4Xbb8Xx4A08JSCZ_dIpqfyw_FSLTgmnOsfzdapSNjhb2JWVZmv4BL-vistc7NElevqj1Mo1O75HCDvefq0PsH1ycAMwzAxNEMlEcpJiuhaX3hoGYm_8QtJ99k6xuz3zmF8SNgoetMirp4iOchrUZ1SZApwUNrL0ArvGvJJ0AMw9WhPR3aIa1RvY3F6oniLfmd8cgThQ09Qu6uFGkwBO_sVzF8A49hpcvq9P-L8GZbNPQK2N3Ka5LJZ7QfpTnzTXQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=omNAJKmkBil-cglwwK5tsOFasa1Y1p_WhS9AIqpVLhuYTddAJ4J1VAolNEAuKZjCT2EBi_jRmevcrSrNGVymL4Xbb8Xx4A08JSCZ_dIpqfyw_FSLTgmnOsfzdapSNjhb2JWVZmv4BL-vistc7NElevqj1Mo1O75HCDvefq0PsH1ycAMwzAxNEMlEcpJiuhaX3hoGYm_8QtJ99k6xuz3zmF8SNgoetMirp4iOchrUZ1SZApwUNrL0ArvGvJJ0AMw9WhPR3aIa1RvY3F6oniLfmd8cgThQ09Qu6uFGkwBO_sVzF8A49hpcvq9P-L8GZbNPQK2N3Ka5LJZ7QfpTnzTXQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hy64Y3Vd9KWPKj5UQD7q7BQ4yZ6D_JeRAB3zm3OhXbUpFk4FWXCOSajvXSBr-WPSywhiMAxsmRGqx4AjtU0BFjTn3gT6tSZTuvj-epYNJwJiPmaBkXCmtnkW0mN30inVk0HSnURicc4xG_XOtApKFMoSqcjT1X5Giqsa0Qvq0OTfWrCt1SKAzUr1D1YWUNE9_YZmQpw2KMIZSAi_4ULTc230BK0BqypJdY3N2lMbqw6jsFLY_c8ez5CPojlW2A2unwu7rlD4XEuqzTdSMlB1cTHviKM-__tJHSMfT8QoyuJGM1BL75NMDTVQkZYggtj8M1adEuKmEpfVQ6cizU1-bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t7m2cUblW1LraMFb-5WggDA1nDc2cbhjWqdsSMuapWvCjir6u54nIrOnyJgopaU-1HEGPZrqF5CuLFyuaemIrcH--XmYU6OoZcYKFqicplxgqmRSv7TYPwxbOTptEelwrlpabHUCPSQpxfdsorPxici4eMlzmbBUFP27whA15dvt1PBYZPfIXkRaWG6wZr6t-WM0XXkszZrWern4kgEHoFPSFcQUIwGA2wo25cqzUuY-_NpJ15YVIG1lsY1I8Tsb3u1fB1WNK9wkPHR0esM4nzylSdq315F_xuxd08jcuWkQQWwvIzBb60G3HeAKzGj3DEJoyUrneJK1rlqUmNYe_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMlpbgOATe-DxrvWn7weuKI9md0NOMGLVdeJ1kQp02vBzlzxoBxtL8mBAPHxn0Xjul6EGBdIlv0HND49O5F75Jpn-vvn8C-gcRGuH0NufQxbOdizxUxbCQEwvbieR0O_eh2cLdgh2ie-hxjKSRNP1HudtOXwlyQ52KIIwhHVys0AnMXkLD50tey9xCgosG599I6vM3__ruHl8iI2TMjszzApy18S2mo6yc_5MM-8P1qy57_LJMW3BaJuNIBy8ub9ITS380_mtHqTQYNWB67FeuUrjDiunkgOfEPrjk9qBqn8tDEfbiIdwxZPQLVW5nNHHZALF-USXICXpapEBvIxfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vbRRjpfIY0i3ZQAee6P9p0ZXG-KSxAV-ANo6uQ8FHD0OuVrsDG7PvhEVJ3xtyf1EOfv7x3X0Gf7zC7jqYGoyLFziKnyZoBeXi9gGDZedsOZl5NidHBiABQw7iAVii6z5Cp0ZHJfx2lYagQ2YSIsJdcfIvVj3uSAXdLNXP_XHEGNWELkM4de20KEmgIwmudaeD6uPcPy1cliASN5LWVtFPiTKN76mkad2R-UxsGJxxHqfW0YhxOsinzoKsYBcSvqiKkwIuly2WY6d86wTgLFKx2nL7HtEMHs-XJ9xyxraoeVoMIXPfaTuEFTxPHmVvq2MYeFmBld-Q8p3XYea9lzQhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bd-LkdfEY85RzBs8Wc2rpO8mXICf9FqNZ8t09V2VuR5eK8qlTuHZuw89XkwjmdxZWd_KyTuYmCfGDRBRXsdSi5QJZIZlgPsfO4stBCeO_WXTOlFApNP8sHJpvFuIrk2dRZA73dPAVhUzD2rQv1_WAHw-ZIdp_Ow8y-d6ChoCxtQLfQ3Oag31u4ANskEJ4RmEUXEg2p7gnx-7evZWAlmAqjL48Kq8HlB2X-YBja9kzgdh_Sx7XNBzsJPrZR14S2Y4NB5GSs3uxaTZ__6_mpMJWztZTpuo1FToPxnGYv7A7rfyNDq-IcK-LOeCl4I_XpBdtThkQRLuPI_kkOiIbPF9rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aSZgcHO3kjGRLlEjq-VdeNE0fRADRDrqBxDN6oQetNwjSq1vF-06nHFs6dIPIbxJbPru6KN0x-X1a1J44vOOlOwwQeA8QQhstZOj6si1oqjWcdTqPZqOfd-ecxx_iloG8p2Sx0WTtCpea90IePjW5wuTNUpFhHq1LnWaf4hn27BggdUB_5BGXafhFcZVXINtyOubMA6ZvxMxcWcmUaHzXJ_gIEpyePVlQnZG6wJ5-EKNjtdjW3oOECnlVszKo3ts4HQz_PJflSeSFOjXO9iSgJ-zZoa2e2ENi4TOTMTWdwxSAKg6nQAjwuEIf4UPC5Fdmm6Cf2iVxhnmh033Aa3ZYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kAlp0c5XxrrWRC7BB6QRq4cXPD_lYtxJoYSHvG4geFmjxOIMuw537ro8wbQ2rrmkGVidHkBaf_ms2qc5ZGq8zyWUmvvUjaJcpS31xFXaWeGvvxjrS9z-Q5ALbISTBFmSFRDzzaFjE0kME-UA7g1H2XlobW0zNT1EI2ig-UaOjHcvXmV_aNheqSyN7x315UPEt3QL_P-wI-8DjWYUCEseyo8jtS7Vod9au1f_K4maIdR-H3FIRcu7fhx0A2b1BStI9ZDso4uZSisJIjuNivoXm4VfFrgCYqx_rHkxS15l3-_9jasMN7cb9EZTK0fUFnoWboKoXXug9fh-YQyyUGVU6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lW8o8W8rbsfyqYn60X83mCyaLBjPAkv_a8jgVenmuzLssjvB1wR1RMWyI00T0odfpLWMLH_0L6Z1GmKmVay3dfAi1ZTmGd9ebbGtmShsoQ2Co6bk2c9vjeDNSbS88wWagjRMKr7GdClasMk5PxbVTk2z5lC6d6z9IumRY7XhUvtn80bvFdWnPj38b9P2gd90IuLUaQYpSWZBc67pmTpznvjMTX2-PitHIH76vxV8eDPKlIezSwCzLLVuYt3zf1hCxzLOI0oTD60tvjv8wPlj3RZH3v89-PdRYg_VCHDAQxKx2Ek794lFElAIqOYb_nQC_7aExmbYRW5yss9TACf4LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oVLfNZe0PbYVzG3UmdK4hcCF7oyFQp4XwKIN8hzou8iWudtxcAoPU_YBf3VDvLRPhxjOvRL1vOyXgmP0KOZh4dih7tL_1e4e2aCVOknumnGvm2alh412nPPsgUkc_bq4vnsJ-uEmKYk0SUvUWNVK-H5eUfFQBholwgcm2rOrKKRbTGHQ37qPZHGstjelPK_dfvl_JmoPSrUVKDmcrKfVEZOKIKRJ8_YPAj0_dI1Pf2-Px0VkXcYlNJgccQ3tURs-vVRTJ01cDDbtMWYzJm-7R0W4AYB861yO4eGDnAQ_H1nGjlX1n3QZ9nHwtHvvxOhVy2XIMRwfnYwGBP65zKDUhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
