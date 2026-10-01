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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Al-4AbUO2HClh-_1tHd0P_XExuCneNX3BT4bYIZsbQmiDr-3aysI1bPNL0wL8Xo3j4cLqkU2qHS3mHP8blr_rFiIP5M6fuBdz5IX9hNq4r4qoIWf7O76iGZVHyQigA_DiuxpvejKqkIt0215RDzex8hFXckMFSbdQL8ErNzqGqa0cytVglCODUeueVwjWlzF_6VmNzTmFgiDX6wHNXLJireA0ZnIdO5Q2u44f8xoUPkiSihfBWloJ9tQrpah9_X0irzhVCZ_SPRwa_a-LW5MsZsNyh9BW8N3yFJvpridqYN2Tcrve7FF1uDGLf5_Y-4_LEu5xGMbHyjOsnbfMMwYuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNiZwtbcT4J2zEniOn53QvoPTgFrFkwJvGNMPn52HIVxeZ5XZALrNXfrHxh6OIzL8mOpLsogOTXHQk1ZpxjouZnNqX66PaXhRvJuTXNt3PDaBpQfHvx4q-XQvxH0OwMfNn-u6BamrvcmZpzviODZpje8SmQ71t43lcv6RCMhQf60XnRHkVPMw9KL07aRW4K8POSz8BDv8S5Sch9GIwrogFwLNxpWfw-vTqj7-Mj7KFr8B_8BBDyOJMoeIyga62WiD4zAhoEJRB_nYBq7Ap1WqzMWXWg-xru_iXh6t_Gz2cupTk0PGm37hleYW9h2Z2fH0YYwvUTz2ozuy2YRTKrhpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EkzZNQpvp8D5kldd1SYcYOC-w--9-nfDhOKfUzuql4jLYGISYsFvJiQrhGRceYUkWs9XrDf3XH_0fhMmu6bUHzsH8q2hoW06NMum0UYxzuHMpaGcFocExajVwrw47j692O7Ut0ereRMV4LMFIhKD4RroDRQ6HNgN2MhNO8uuZ8MfyeE3VAowe5Ybx-f91zcqOyYK2Z5N7YGP9LcHJcqfGj3Ik9hWp0_lftAkpUEyDhGp0KlSI809478jUQ_OV5K5xZwngAs3kJQG1WBs5V0v9zvoZKgWNXKavMyYoyUE-ZUVCJ6XqGtK4HJ0JHlYPalvsi03Q56Ed_KciWi6n6ZqiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kpt5q1ne0GV2aPGH_goPsZCeEal6baETeU0aok1MpYW0M8ciMZUc7fO0h36ck5_uts1mVu-0cr580n65FxnbuXRYE1l3x9lzEwY2X9qFmxEn2HsWujgyoZGYVaZb9ifUsaOaR8GKj13ixv5Xi4-TqOMGFFz_PmC-xIzL6BHua0Ira8of1oDMqg2UkAJAq-oJ56TFiFB4Ps1PLAfGpIfEt9eaE_XWWEpA_QEwllOb_sgJZHm1KErsxPrcYE83HXtogfSS-jwCSfvd3_VJteG1Xhwb8LsIlyPcz7yAVmNL7gA0Cd1erixrU94OZ1XIBRYUvwb7WOcUqtVjEAwn0BgYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uuD0fYNPXk8QkBXnXlrELek_3YiarNCsS5nlAj5ifdlStygRIaYceMI72wHn6Jw9wcoPctWUtQsDV6xrSnoUShk27FXxHjFpaqv3ywDO7B0eE1H2VXN0b2Cu2DZmu4WDYkqKg6O6e63HDPUHMYP0CgC-BX4b4JUEZIdN1L9RDrldQ_mIfCDgT7ZTU0eynznF_1qBWMnEB8uL0fufEBRMF69DjUX5dDE347gSTAQg-X8jwArjhUZE9y-TYCU8u7Tyo0Zs0EAU-ecex4SsoEyeJAU2VAh8Mm4Fge-BJTlYesmeByCXBpX728fQcyE-fn8-WJbtIX_RM6uiUAkz7IVqxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jsFhhRAR7zVM92gRUzGtDwrndFYHzRZy5xF51zA-QmgmZzjge-OA5XmpNudJfOHLvDT2BmUT9Ued4Ly5czDUWLb69dReI4IU4wf2wJix_zC3eChGp72rmXzuCJ2_QtVFpq4pvcJuCHxbAOYXcFL5w5iv6fjuIpOVhs8vo44fh3Apy4RBPz2HbqzDcnJq-8-_MG_esA__VQatScTiIxIcBt72mSyJmpmLp0XElUlkfkd1tLApcCayTA7ZMCcOdMvx3Y7i4vARfwqNLu0UOJtfcvoQcKMXwtWnYqZYISAKZX0KUV5ESgB_j5rxNXp9E-oBwuW4uQsUOvQlkB5kP68LvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lm23Hwxbnl0jSNTj0d1q5Z6wvaT8WBcu1Au0pz0Dm0QE-Xgdb4pfCIf6_Br7bESzt40iIgt6rapnUJUkCM0xusl1-oV6o03fDjh9itsvd3SiNZkMe5US50s0gFUcHwXVtl3Ip6yUHZzuBW6WspjkwqsAK8_OkYvX_FO_Jdk9XDErsNBM6binkhgZg8a6euJmV-E9O38rqfEOIt_2Zm0fulqm7nxypdsP55YiivQxhcAAMAV4dcmHSmrcfMIiHZ8cYecWBSIGSZBqyzq8k7y09rettwwewX_fMJ2Fx7IkjzBnTovpq5xkzZyt-mD79BKjxdugknQB0gm_SpHvd9UV5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qwDT-GrkGkVIFECzFklZfett5m2AdrRDlpRm-4Xh-4Mncfh7bxX8Ca8iFoCnhnwPQa4rqtkvTebGhPGuuwgeOEGPt1OEscbMnAKK7IN3Y5ET3q40-diUzFKY2o5fV6jEWgelqCPn3qtJZjrmb-aAyOfY--QsqF-D6z0Ep7mQaKQ94aKPxKf04rNbWtbUH9i17DaTOC5btM3U0ZeQJNemXxUsxNS3xTuGWoztSY25jeE5vbGl0VdTZhVqYoCtNHRJiaQPdgFYJGzJxNQep--N5oWOVxWiVNH9Z2APjSiG60FUBtYgehu1W971DZysh6k0jUTcKam24SUJ5N7wba0L9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bYU58khZmdOhv3YrCKqDmF_Zp7DZDHJ1WHOTQ_6s6VRrtnAn8hhemGWXG0R5dSqn12_bIPVqSFoB1UgiPxdcsUN4MzxefDYPwNmgAD9lp2Di1nJ8qAV-HUbvuaW1cV_fnTc_FLX3Kw09809dc-PDwApHbiMxpZkWJJlrEn0Pj0VnKxOGc42inyfZq4I5gsgc7KzGjPKCaNlvBDqDUOFxmG_t3kK4xgrFggCPoS6U9ge-zp97ELZ5keAmZe-H00ajOAu6Drp_BCQ7wD0qisEKrjVIJxnY3w3aEKkRRsdhUslTjznvPnDp6mu5SFNQLtXg9fhxMS2XkUhGcmOj24MDkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aZe3sfcaveZ5qS0Fi56farIDhaasQmj4xLz_CL3D8IFOHV4Tkj2oO2d4ymetqXXKErI-i_wKiYmk6yvoNB-sdEYQpd5kSQVyoCxKGyH1m7f2UVh-mkMVoIQS5l_qi6uM7dg08w3oQ4eIn-BfgXvUvGXuvQxsD0gfvpqidYAm19eS498PJ1DKuCQ_klHwRf92sd12kTS3_zFr-eXxMzii5jwOD2MXRiXkg1cPfx0FUbMLSrSAcosP2IdUyDMVfA58XgjtBNxwtBKO3ctfS8qqHhuYubgllPQEYcAnaMAvc0x5uC348FXoWeKis5tDx2nLwuuiUVvl6ineVZngHqQsvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T8aMuIRJY88Dfbs-3PtnL1OTREb-dke8nW6aZtnw6NSvCwoG01Wn5oZSWHDshSor8X5xiu41dhuJ_Gaz5dwTl8-eCNk2mJpHEGrpSXrJK5J54eIgSuEQX4W-plguOjcJfAH2Xa6EbK3qllVBI27NAK8SKsZ_9okR7Sd3-xxwo7GMY8-oqtesAOl7UidmzSuQsLa6ClVTByW8_Xo8hxpSR6hzv4W-uqan6m0OSUR8lIlEGwzIVkq8l82dp9cY961TYox2iZ8M0FGsB3hOxPMaDq9Ok8KUQjBM7Jlvy8s0AAAIAIMZEKWxdRaJjUAnaNOVXaiQTy5X8xg9MERBa1v3dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cBWnW4hm5l34XBtD83YcNWDAc36ckFZYk8c2unl6ErPZeWVrIkPmpfj4LwW-KbjIlNuznbjnxFMJV_P5_jVQl304GtzU5LMrVh9R6CFcGAh8XlZBZZK0QTHF5fNjzW9K23SY4bjkWQuPozqIktxnyCQEQ3V2rsBBM41DYzLhBmnUWKxS77SUl-HTRniqXFG1gTfi163flEmWOQ4gqaidNAwQKJbS5ncmVgwFAsG89cAYXhB-GpwOR2ITYvdxQqH_gzw7KwVdoJP0Yio5qwyXLEcRX972NrkUfp1trIFZppBQr5fIAVHpYB0a6XT1VE1vSFCYueleV4rESrr_PQE3Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BQ8d5-uaBSdYOtv2QiG-GYNNW9moGL5E8BuVh0Qz05GiVhGuaUZDhwFk-Ib18zdNo0Nzf7u90KSfXofwK8smRiJTscZlqs_85Dxb2djeK4rFyieEoy82ZCvDf2bOD5l56HboGnU969lg1PI3A_Gh59WpJsVmla6dM2EjtlGaFU4I1rIddUFAGXpsSKl2Rx31G2kSKIs_agnpilqLx1-uki7yAgFmk6Ad6HFeC1wIhlm3WkUDVj7NjtxeLI_GoUM4VaQqrKkejdnA0X9DRXGua_tZWn4a6Kbkt6wQ-r10CfwzrcKdEu_x4XtgDBdRh9TV-FQj_9SBJqGh-NoSTT6bwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZekzqiE_X1rLkeIIAv2F61FgXilKUk4vKk0-VUVizZNbNhDnxmV0exZx7gLq_BUlTkoHQO6xux-cfJfpt2U-8O69EJe5E_rCze5n6-FSmkncY6TxEJxcDPDkmMrvGH_P_d0Fu0eK63nudOF2O05UyYOefpBCiYfVzwkBVn9rXp_N5LPhlrLlxP3MMrwPn4QDnd2pB2a-9zkvOo8Jc1LGe9Or5bwsHrbf8O0UXyJQjAi9M0rL2ONuHJWUe7JMDXcLlxp1OBpVAApyX1ZM9fQwSCiwUuFWurvxLTwWjAdbCLMGWU67xFnw5dkfSJ44mI8fOcnARktGrBUy0AxVmya34w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E3fQvSKmYAjwDlx7yoB_BjLpYG9YReV8C3pPb-d4oX-DZuReQ6lzExw59oJCZRrzJpDFyX9hKKFT7qwIrdmTCqvTohKCrZCeFSwJ4tmtuk466kAU6EHnKD3LAel-INsIuBajZqZ3niwTcMwKwh611a3sYT_FAWcxXmtILkY7zjhjD_ehlD72Ss5V-tiqHUMxuRlUFqy94_bJCGKdJJ_z6hgnpvKVtKRiZ5v5l78UdteeJO94_ATboU4kVAH8neO9O7Ay1H4grYBJbwiKb5y8aZ1lzmp3l3BqL4t9l33DDGKqoCJMxQm57X-Thd9S5VZdWDFKmtzguIBFSo4_lnOEpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oSGJUGeWiNwz9HQLsRO67FFTlFODZBX1zNKbHrpnZH7otX1SZm8aBwKwbQSG1uhfAlRRuyOjxp5STfePoLToWo3fZ0S6VwvHF54nYYf4P1J-BbE8zpbxao30GxmLHEBgEpQCOKnGB-u98E81UwSyU7MJe6AOEnaTRC7U5Q4OV57VWFwOIhyi5RxijUSSI_dDESorknpEOUC8u1E8ORchHXMArI2OPh7fOas9AP9VxEZIRRckUcHx_vMJchS98A5gq_8DADxSMTpwstdiI9lPQEKqcb_FQpw1XDZm4vb7o5ER2GM3HzmW4Nkn2D7METgqbh3xPb0xcMnExMP_Wfw89g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/leQDhO1hNypSYoHJV3Kr5l8YUu0c0KfVT5XvDzLeV7EuC2DYnimw_c6yxyjHBAhv-IB6m1XrjGv2rUeGwNVvKX723wJePPWIpFQylqme_UZYt8w1d90SfJMakN-b6pyCorNCFpKEsQDXsydyof2zAH_cVIqz5snMe-Zh-W0IeAVR_D1IzEZmUTWahOIfLUp3y53FCfOYnuCs5CTWBwWb1LQrls88ovT3zFDLb38_9JvjXuwoU245MOZxuN9aJh3NuCu8JWJG8mtdLHQUagkiG7IapzzWGi7dSdeX5BDFKTsPjn6N0hPaFAa2McS1YTrfk-yB9Wys4PXxvo2r3Vx5kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YVmqV69ZKX_zB4w_6oQth2eNmFIY-ddn2yWJZ3iA2qaC6r22ZZAPFUYDf-TXYxd5Ai62b4_ZoMfCAt5ZnxdbxxSHgdIHducjI7GDGTja0z71ppD5aJfUPoHmUzLEdTsD-2Rrzy11A4vK8TQG1vEb1IBYC9JMb8dSDtpTDENKGxy76d9ZVmrO11aukLoBeTSXd4lyPBl7eEVDd49HAmBCkl6z9D4SWWa_shGNOWsE6Kva4x9PviZCgnluBoGZwlLOaGCN8J58JvIQX1wSr1WpD3lj3ImjZPCGbf4CdBqlLzwtBVdTa-s14o6DaX2c6ZjAPEH_NTl2lpOovVBwrA9JVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/de5eS99qxhVrpuxi7-Nn-BroQ4Sq8NfPhjovFTN-Tsvrn4oEZlKai4V828ICUCeWicdv_x0X_jK8ezeQWw8S4DygIwn46wmqjecZQoQacwujlT0br-8vhpn9jB_ThVXuTLi-FDcY-Q9C2WBPKPPDhGpJczGpyYmfe6uIDGQvM5IjlnIPf9OKijsPg88QcqfPKmz170TYpufNlQ6V6-aC3HhhgRTt9-Vml-xjYB3AHFLQtIkEWmSIWcMntd57steB4BJewyjIcN_E5iBN4ukpVpp6mm72dJYnc2pFAp0zjIfaIwo9wjfLcHAr_TMclRkLeF3TxEfkNBT__wnnaQNRLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sojKH8iQjj-sqZ547Ts4TYRtS_wwLiGijmEonmDWuP111vDB-hbaZT5EphVdIN87qGQmPWnypMdKjD4NmlYNKQTROx2U04j1qcBH7CPVLuYBrG29FwYHTtVeur-Kqftukmz1eM1Fy0Itk89UkgCSJ4hAOvmYdo1B4VmP9GzhS_VgTdRUQAxBHz5Mk17RN1X4FIluK2hYsqueWJQIUqgC4d5NX5gHC4pXchq9qH9zp9jlwFSw5guSeIIlLmE2oLDym6Y1xBMTnryUTiRJH4hBOR6Xv0Zuy-78zvDoOdL2zXB61-JQuF3JiqWasL5Dzrnu2Y7iRuztW7r8fOdhf-GKkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ACLoAaV0oppng4cwUT0yD-wyxgijzJwI1-5MD5UKnP0i7ylQaUeS9xRhZfhL-StIRe0XOzOUpX_nbGGy4Yq0ZKN9rD3j8NS3lCQkBQzC9vsqYGhksHl_UoPLJCcDKNqtN3ejBc2PZ46YdDgQGQVPjf6dYkGP2V70EtlNwp0Vq5uahbbBzzHFzV3EbCk5-gKVijPYitbs7Kset3-pXL_wL4GzhAnQQdPoIotQR67BswDXE8bhREPIhYBSldNOcoCc4hX-NOIsGByLBGAIeVvnUivUlF0f6C0BgrfInKwkCqryD_dPY8_EwKhneo7Rw_7fzFWmiMk1OJZfftugDBTo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1XxY8l_9ugJPv4EPA4VUO0-8lYNkwObaiVywpG_lTM_aTY343V3FAlKW7qSi46SFlE33IqNxFFNOCncb5NVd83jYKJLt8Y1ZqMFJwtzf85pJCmPj8_k8Os94sUb-1ZKTlk00c3-xNJByv2kY-mMZo2xgf1xTF4kBKo-cB28GAErs272Lf2mex973SUDxJhxka1mKuwV1Ov9pKtSIPQJDepO4RkI9QAASjyhA_YYrF5VRUmFw7Lvxl2LGaOBL9vcvQXznStR8JV5qOr1bsGxs8pDZLD-r5bq5RXgJ-tqW3DfH2oUzn3SBsS7Qh4OiEtyD1ikyX4t0kbR0DwCmtdkvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VTZDpsGp8BSHBGkPTqJnJaNLX0-HtnWCFmRk5pMvWIoZddoq6_-nFURJqIvICsrXCXG2vlP8zjofA7DljEYTxvgQ-nTkVY5t5A8EmKPs3ZWQvxxZ_Gvn9ETRtiMeAxbrWIASb14370PnFlGR0kiwkMyOBAt1avAKw5F395cyZbQ2_28XcxAw-czwqhOLTUVh5GlP39CTqH6hgS13MpQu7W_RoJ2Z-4RzGreqRf4vJipSzZ2UWaUaNRlbIppY-f3U0_Po3Op53qs2nlVIyC1geBDEZiQSb2PiwZmLOAIOs4NWNhdgcCNLW7B1D2HslV4Tyo8kaq5N14hshs-aB9FX1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m7UZutSldkY4gT0RZcTNK_DBxv5kIQKuZaJIJ3o8__LDuhr2zKvvKzL-UzlH722pnAXHnttnR7KKOpopD2A2BzjR2Ne1SqulP_7GalF9agB8j_MZL8moLRSS7lG0M-l2p9bUkRk7xvPnrean152cgCMYGanG4NXLu7wyYj_iEwUb2tNrG4fg8-7vMisxdBtdfPXSEiNeXrcAAWnvQzYV3_jOgABUv2pVn1GlhtQIHOKymVybZN8UnPQ3gaTJCAk2SXdpxAECyhuoBhdMAdEJMAffrkDTGGjO-3Zc1kSJqhiz1uIFmH6JpH8IAFLeMNISk5kR3Sbeqs_o9_xK6n_Uuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dhTIcuOhC08I9N38QTN3RGIqHs9ifQXPODZ5DSqxBb9elKkBxIzaLphHXgWdFNYH9mg_CaLp9ZBSeeiBZ07b_2GzpgAvhyA0pWcACPGM_fvIDD87aDIU0w6inrAo_EgnYNHlB-wQyHKTbnnnn-PSUHkFbawN5j7JD1CEI38sifiHD4GyMKc-xdIecH8JnZ6KJpiRRjb0UGaLCeRIYo69Bh4Uic0ABXTbFJvWMBWC03PChF_7Doiq__QSzDSsUAf8OorP86sn_w4AoRF9c7Hj6h_ivE0CfcJVBmDzog-pMSUWzcsnTwR_bRwxJFxPXcw-JFgZzaEn8CpNFnDKKzSqNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NW8CJuLHvfwbTx_PFqWccsfEMIJlGX_sDthRDa9q4Fw4aYRJFlgbIEl9G3nmVpkL-oj-vP27MF2qUaVdhtZB21FrqbQIVFJU9eQvNK8lk2qY0vxOQ9z2xIV01UMMeKktY4CEEqvGUg2gFZbkAtQVukeQLd8h64Z_31WHZF2MJWpCwwo6BHlO9JdBifMKcJxjzj4MfSITyyBoXc_w9Mstq-S4VIzO5LnN3k1dgL7IUhNKj4GiapptOHV7YxuLzdI4K9AkesBi7BYVuL-DM_8jYzNAiHL6ROdiY04DgtPFqOoAKsUplQdJe0ZNfQSiE_hDUjeP1AH4LnIAXCwavDu0TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXCAf4wAc8xE0A4D5zlJLsZs7fPrL3MX0JumcZRYpMkbpoCb6UAh9gmHmaTuVPgQVttXFBH6-OsYXCI95YuBzwuNrnEOcNvOg-W9-06uAqf2ASh7B_C6P7nn3NRUl7bOQkcSEueFFaC6xHcFAjQT1FDVxPiDkoINthy3b13RjxBnurRvWpNno44J3C7ryLS16iwC1eJM_b67PF0jAnZ6HGHYs1P-07Hypj8m6wmT5KaM7gRyvW_vgYrXrxO1IFOiLtNiuFdzs37mW_gTgSWnk8Z0jH-tX1Pw4uom6qD71uWmiWxn1r4KCLLwxwBHUJN6QURyhVCgYBpSy4F5iUbivA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PK5ypoZp4EsdykIO6JQkhus8WcEprYRU5jF5muOAjJ1mRuXSH6_tDvrUNDlTU6rY9o-fNOXGqUS-qFRkVhp6YpQCTviQhkY8uz976ppb8PXkKSTLxBu092mCzziGdegBikBIxDEbitqhz3skhot3hj69XHDqhkSDAVi0CGaNBouI_nhJYAh_6-z-dCboZUddH7BwToNG5zGkFec--TPKIhWfqejwUefrhBERZrRdH9lfVA0fsWZNTmUZErHJEwsWVcIgjzeEaMzBDMiHBUWdwWEc2Kt50zHr5V1A_yDq4kL0oSkfgt1-y328yLKXrUOXC_KWGNap_NLeQmpMkB6dAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r4foJpvcQw3mwHFCUg4KpXONnZXD3tnu7aguJKRc_ngictWTK_10N2poUSO8yeRdGirIGdMAPBEjptNQrdXmbaDitCiJ5HgscmWnBC4YfRbjuqgcT29yKYqizd8fdAzZaJtuKpBYtGJholsh3GiJUO5_m4NTbM_mYPvSM5NobamOwj7qkVHNJCbGR5Jy3R06jRI5aew7H2-b3hPCk3fGpkKXyFfvuJD2F3jgu5u4LrASog6dMXf3hSj3tGO97uWg0I57EPNyHWKoDnaSqB9OHwioTPVdyE0vdlIF1qPKf0316xvVvRMhBzMrVTw0DBGBYCK0kxXcCfzpZ6l8bT09kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2Lo0rbpaOdLw-6CKYExbkuBkA13tNe9DyXlN0vYBScq9z91vGc9gH_j0s-bRl-Ij_ec0SZhmDSbOe4jiqg6Wzt4QeMHeGPmIICz6w6l_FVRBHs8jA7lW_7A37AugHr9pD1h3QBPQZ_4-Uqwb5s_o89gNBzogI2wX1YETPZw19o5Qeoe-UBdqHJACz-TjBicdfXu8mhnx1cY0t_uUeT6daBjJ0bvTdK38kG7HA1sioENom_6GGkRW0DKU-mDZXZ-8dTr6yvkjfI1vnt1yjEmvJ6bNJ5WDK2At4NZfPNRzNHHFHY7tpCevMDRsDL7aKdR8jGy0RCx4mUTdp0BEHkwlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eiF5S0cLLyGC7lPsxIJPNJna5yaqHSJHr9uZkjUvt8THccYfRtC9FFRmo80vZSd1SINEIuv7C-s5uUCil1AMWj7m58NeoNGjHJP4LSDg917Sd35xSIgjXJ8e1LRdKUow6QzNyJ652ZzO6Qc8KVIEnMi--KcvEM8FbajzPzQLAebTmTvPCm78Wrn0Wgua1ddlXH4LeMGoJjeVx5hzPEdfTXl8-5O4hko_oQHef3jCyOc6sWOvT-gBPRT7-ymtgU731g0fQpXsankBZta9fQ4AsqSwB9KYGtOVf-2L9x0cZ2OAd14Ccs3cTIiEQx5cX4EnktOv3hOSLpmmg2kYDzAAnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hH3OidbSmmn58FSh3Qdvx-J14kZErsEX9hgW9x-ZlFyhJM0H8FaYsIhBt77qV8e9XYD21H_X36hlB9YvCY0IrrZGBjPmm3YmAcDtCF50wYE197e-qgp69UzcWiSshS07NPwCrjycuR0FTQ9c-Ch-RzhhFBooQGmY_H_q8OjqEpVphFFi2pum6l5GE7qIsYQPNMHWmSb2Qt5Id4hA6F3yxw3Pge_KldZfR9RyajtFFr3tE68CVhk3i3SR80-Udq5-R4NWEDfMmRlu-MIqLh29ONDaEd1s44_jdqPNqeQvuMl-Y1EewUBjyFqDNa7QZiE4w-yUgbbXPmHYn_HI3p5qdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jXfeyZVAKcUUgDiC8Fb9tl-AqWe4WaYeNGR8kQyjjrorEOhwX8p9Ube7vMtqWqToI0HMDXEQm6gGjorGaZSECpBDtbIfISUG-sPgnDqWvni2rV5n7W802JEJduh-9-Lap7LgPDOnfM2Boy33BY4BLlOVmSaJ2CUADoH2vgcxrtkOjzubp22ewweH_aXjHsDHU_5HV_f0XI1aPWiGJSoTK-gQKeXJX3bI-Tdy8_AgUkDcAfxwGf-AScwi9YzKjM5rGjVJDGO2Qn5NjBbcT5lSSD1hMSVOMqhqSLHh489CpI2HqMv7E7J4NQw567t2kJcAlMl5Uz8HANqFxyna66-z9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rcva_ORS_Uq3ho8Qt_csVroAQF-jxtnAbgdT44iQoDZpvekj7__SUXNd5XmeI5qg33gmZVk6-_5JZRrSW2_IlDN-EooWHsQmisOiLI9jGCvH1D83fPC-fVF32pGUh5XjAPomAaDwbHiU44GEICqLgfZfKHLjY4iFTq3OeFYgLMKai4eXZk073WKhwBVKA2gH4LrXF3pPvJjcvzU6LvrQ6M2BxeZxsv5bGjV9HDHnMoMGDntLtQfi3v6j6kdpnSUBEOfveTR77n0ovJbni-gUX3cQpHkOBBhdlMePUBoOLpyOO6JAO28lC_A-5G8ePvpjJ7xnlucj8wt8_ncP2FAkoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VkKcxFPt8tNSIosZr9Hjzf4kWoIVmH5Cn3jbOAlawaodMozqTkL_gvXMk09jLQ6uKsowdFd6KJTA2ylC6-sFKI-p4QRQF4v5yoHu30v-hUvsjXleiRlYZ7JXthp8nO7VdUkA043l3l5qhtkjFWFHXpobbhAXqUL43BGXCN4ANlbppFGCVWByKG7CrSONkxJK3RqUpLv9164BkKfqaZI1iPG05mhanUL1VBOs-StKgRJduvbWyWQUtHjRmiZgNTROXZjvGPkFAJrFNswo0nNN0acUGqc-wOly9-89gTWdfczdS-u0ia4QzhlVUbdZ4Q-uc6DV4eXnJCdrhes6nbYYkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iIRsF40P-kmXJG1yNrXd27fJZ-fa7ATBeEWdLCfaZc1ieyffha-iw04guc2UGlcMmWrhOGTQYoE1FeDZLJ1037390AJkAwrOC7Rvmxym7iUdG_NhUcMJradCkg_R93kl3ez6hpbbc4DjgmMWfBUzpNUwq0bcCJ8wcphW3-TkW6yC2Avw5HKkug5r0C9_tKI2WUYoGcIgMxLPsn6_OizRW_-BRZp1xbx1wyhiV9L8Nb20X7wpDIlKDUBvUvmm4dGET5aVIVjTL5QHAdjIZxzhkTAH1bc4rg7S8T2IswGUKMFgOr_AztQtO07VF-j-i1nLoQfgGageDyLNcAqcKB7j9g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Qpz0xb67s4tFUQFs5RkXsElG_0Zr0i9BLqAR1raOG68FqsD9cBLkCB7nMHXrNiULuIm6w54qPLAIIgFG2_XJWGrG7-4Luj3k8u7VlyjvzyuClVKsn0kHv1L3wvYGzKlD5NXjNyHUrz3RjLJ-Rl0QRng0_oUlGBdQCV4Cs3rJcjaHcHx6pApQ76aMqWlLu-9rNTM05GyHQSI_F7gBpgJUgbdc-RBHGVFqoXRUurTtzIstnIEj5_7FlyvFbOL4fqY4mdHVAlAANtBLrDbLyrurllmyos5cvGudgznqZ6WBI3mcZ6tPDnObiGAwjMXHSHeIQxnVbgVj0DnU-D0X-mcAxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Qpz0xb67s4tFUQFs5RkXsElG_0Zr0i9BLqAR1raOG68FqsD9cBLkCB7nMHXrNiULuIm6w54qPLAIIgFG2_XJWGrG7-4Luj3k8u7VlyjvzyuClVKsn0kHv1L3wvYGzKlD5NXjNyHUrz3RjLJ-Rl0QRng0_oUlGBdQCV4Cs3rJcjaHcHx6pApQ76aMqWlLu-9rNTM05GyHQSI_F7gBpgJUgbdc-RBHGVFqoXRUurTtzIstnIEj5_7FlyvFbOL4fqY4mdHVAlAANtBLrDbLyrurllmyos5cvGudgznqZ6WBI3mcZ6tPDnObiGAwjMXHSHeIQxnVbgVj0DnU-D0X-mcAxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FsWZCKDVV4XuhldnvNnGWl1yQ1uFp8AM22uGJP1SUyQHs_1Bb06x53LhXuWz8S_6-hWoF8rroKNebvn6zCabd_pRl5EDd2gJ44OtyYcwFL5QA34BWiL7BRgaZRu48SzNcnPIO5GB7l1KcaSogKpDvlDpYGbf3cuyv6Kf62A6-jQED9pO_alxJXL_8_Oa-eQOj9_Apc853Kcn9QXEpgPWGLmqJnCyuzxRFJvD6chbhIWGouYx3ZdpgnflqtTFSed1XE066WwJjQcR9Ew5M249y1-S6jq6vzUYwU8rkapk8ihMOx0Il7BUcmDUFw87EF6io91w4hcPxWD1dwFJHEj_9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gV5qCUicJGzaKskDNc3H042UxH_ODUY-k35psll3praoHcXum6JjvWXrSfZaQV9DdeHrHppMPZC-HbVwQXOcKuazCtuNp96o_DDf00CSJa2GMpOdygvkou3J2_dHCmM93dpzoX5fakViqGdyv191HUgKoLgIJYyCX8HNjycNqOPG9mYqqLE6xQquYC8utCBCD8Rhnf2Xjmjgr8fEcUUHmwJ7Pw2ej-KrtG6Nb9EiEjsaQMIn7gAMMIfF2TcuvgNw4TsYakwck65KGL05CtuoEuzzPKZ14LjV8-w1_B0iMH_KIW7AkdG4H3xpcRCjuLH5RF9vhH4N1-FilQqdZ77a_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GGm3FbqtMwxmv9ygiUrDVmJhuwt5dci_frQVYCWO0ZQlZGUOu0RsOArELq75f9Xq-kp3rlxUPlhWrThIzwogvBA7ALPEb80LZHJMtKYSbCFVUp-kNIe_ub9ASGQ-d1I1C2VF9qqDSaFsi8J5jYqD_wmo_e7-K_K2ewwfrSSTnOKTnnhVSvJoBNDLA7YH1KypYVRkDo39cX-KlZw0Li2uG6H8qu4BT0-jFGZ-jN3DFFN8ELoxtHZcnrsbejqmGvgf7ssmewtDYnjZhTIuJc8Ipodr78KDTlMPoM9Q5q0ivqWltK5Dl2Z5E86jKavg3iYyQ4rZUzHGXEHEnYSg7K0gpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TQRAwmzF4avDfwfIfGMZY8jOrNvKdIIOYRQPv-tvsZhzIXPM9Cvjavmp4IFHGAnb2yndtDd0WepWM24QQCM64GGoa3Z_f01ME3Qa_DkoGW5IK2pU1r3adbbTd-scO39yRcrUfhbQvl5n6ilXiTf0BN5Nr-1WZ0HIq9fyLuwp-ldA32pHX1nVwY-caGekTOz30HkMDAQK5EL2-fMm57RsCy5AatXaP0Ra6ol49Utizy61RpIV0EbZ5FAR_JwpppYKqM7hbtUFtEnKtwYWi7fw20cCQrYII8LkcCMENllTJYJM2WmbLX8YyTUYQyqBf2Q0ttNGK15Pz7fB3TY9yfVNLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BOVa-GeO4S9qCk9fw06s14bBYmqfZLTkf545nYebv8iJVYp5zkRNsJ5gNHS9hxC1NrwEze94QHZ6w4ZLebnr5_ktw5xE8yFtfyjbFrXcu1r1YeEZgsXw4JmWzlOJHKkUCxaT-79uUzstZ1vXzNm8cV-a6OY2oKwb0VeOmWIbpT9XC1J9z-jvKuolbjV4jxcuIkE9vneInPovaR5SbDOYsJKFSdKjIJoqS9NsgCJaWHMfrm3TQTmII_FELupS0e96uOBeob2MMdL_o4ywzaWEEeJoZmxwTSBUeWW1cHv57dNQpxnl-6KjE4tRculAc-uJe58Y0Ck9FEKIENhXfY6KMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GY6ZXSIfJPk3Lq5awGUeVzMMN2Ag2zECBTkaVlv68shYPETUn8aWLed6yI1ZYwTbm--yaQUv2-mZgbHBWIxYdusp922hXeynTtgJwB2Dhlpf9QYrRjKrFL22caZ41WY-kCaNl8PsC6LqeB94_kBcqVimGfkI571uljIO4zoD9kSH4xDvXid7lY_5IToXAOsGtIQxUC3Dii5AX5Sd6EG2DE48GKeAcVBH8_CKv10H_jgCPwFPxymE-Wi8alBSLpyex5Dq2Wp87bB8Do78QldGukeXC5e3XtdisuI-eVEhEZtuj_3C5yvVIlFyZjVgZDSdH--7cLJ9ZfxKM4gHVxf-bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IvcemM7KyH9d6WeQyHKtgW5NRgLdL5OhIfA1o3H3u7B9538tGquUJYaSC8Xyo7ZhV-qqGMJfFUhzMJa9wox-eQvFVfIYu7ZH9zrMb5t8-kfX1BP2EDO3E5hez5QV3y4RLTiv0cDS2t4HDuMmAVbK_f4ZSLxDrBGHEyHjZ6z82ofIJrcYn8e5XLJrIs5Oj5unn6K36-65THQylnTu6QmZsJ6CtOQ6pYBLpuKODWXKYCUVSLouE8qOcCODPM6rZB22uWXjnwzNre6QpIGNwzO3QpP1nsc5EQ_STn-_OPmzlg9zcr20ET3ijztsbP6uVedHk0LxHHVRL6eQd2y6gr6x3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eM_2B6dxABqpGNTMX0JPc5m3VTjUSB8NB1ESOxUoDL3xfE51IhjFudIyZn5d_D6tcHVOuFL5DrA2QGr4t9ziM3fgh7I-EZHZT1DscklA918wEADpkEbznnKFA2oRTy5wyipGsFHo98NjlQSOdsaWaWwpaqdPaKe_TAl8_tmPFP05ywaPLvxgMHK8Y1bRfsTOiXrENAuqR8ZmA2WXCZZ7Yf69XqBEi7nTHPYxV7hxO3p5lmuW8rgVbT5oWGuBC9mcLvE43aIs1KC94PM3VFt3DW_s1wAibGOr9TUySSX1jS9Q9SfFUZrvnjcawGU54Qoy5c_vsIS5MPmx5Jqg8BdlJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2dA2GM3ToydUBrBcNQEW2ytrbdxGW72rLVX_eox01ue_0p-8hCV0O-aVRQekGtZoXwna-raxWUgbIgfDZzhSfKQV2llufs6oMfePbVl8VXsD9XwANALqcJ1lvCRIdSs77u4iG30zIOFbEAOOP2z5q9wGLf3ZVn6dkt-MyuL_KAm38GLUXkAfbewSa_ffyr_Alq1CJrDeW2OxMQi1Af2ZsHRVtqreKRb3pGjCMjl8EyElPCdKdu7t154TxLAq3MfDEJx1jtLDVFCJd3bd2AF2okfxQNCMP2IUt6DFCsErz9RIDxGfOQBauORlaIobwyQaYISuSrHpCpYtvCPbfZtHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XYxHrYmAAnefxty3XGwPnzuMc8-VPki5R-O_9sL9-o5ChWivA72nWyUeBSO7tk6nh6_EVXxQXeqc4BI0IzSHXOindX_iDLoQxHmxN0sIEysbhIk9MrxXGr57FZsFAmmGmPZcsBYtaZRJVYWv7toVaHGi_fg8ryYiFpyxjuREUCYJDbW81s_POPIWoIaALhf98lkO0a9EeVdterJIfZ2xiQ9N3MsKq8SBgyrcg4t7kHBJJSRwr0r90kCTDmD5R2osk5ICKa9nuqkUtCmL5LLgfW4xOcbi9w3qukp4l9h5asFq766TajIohI0oMzhYAvFFnM-za2Qek4HBLWrLv2PkjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rwLyYGbB9LHiuQFY_OEMaA25IRc7INf9j45FpTBzcDMgJ57WzYF9mwwOwgLvyh-viGuGNeaaHSU0hqBGbXM50sL75CsdsDt3lDl7Z-avnax1iE1-wAEIiqAR81bNS5GV6q7kWnbkSserpiCD3vki-gKldRF9MoCrYmbJqt9YCfdPPJFfFf1o79ZWJyN2_kAvZLIUto7vuNCocmk8cG1wOjX3sYBdqHa7qD0Nm2VM2V0qj11O1kWDzSrlEbjcakrrWyHBLyPDMyE3VOZpX0roCEkm3z64J2Yi6bFNSXZnuB5PFcLH8N2XzlxU-CykgS1NUBhDGCRnQKrsRYnQsS4cpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rm2ldDsysFa0x1d4OJiwh2xR8zBZ2Ak-KfFSRpRV7RlUdu12LHgPovukDPH1kSwoZOvu11Jbcv_BWXTyx6QIxPLXqF5tyN1g_nbPvHK5V7I95LyeoI2pojjCMOf7i7NAh9ZqFtd0kY4yo0DPv3HUrzECH8NzfDcfJtitiBUdq1CjqbUaz6flxaKqq3qbEJqYn9YSo9NyDp-JXKnYo6oGebwKUrqK10Aej2XPMjIjBIF9R4ozPe_HCzBXENFQU_W1GwDsPZa4f5kt_lugjjacU429hUxtJvFv7yOEfOuDayVII65dUl0IrBCL3RKf_B_lRgecbdYv65uaUdnkCUcmwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BbJtQw9coDsb02ae7h4EgBkoGFfk7UpMoVUBU-vt4pGOFzWpfA4gBcs91vDZTyjJ7uRWo7ZG5CfqNhrAqHE13ThHIx2w2xFppMNFHk02N9k35cuFttP4TV61yvfCS0id8iaAjQ22-wBHx87myu_YYokNT-HH58DVo1gk3GPmMuj5MjgihgrSWxre-fD3HmWTKjKy74qAe8OphOfT-PDG01ZVXg9Rj_Dun3QcKL3-hOys8kUTJeXH8pGsLM1QT0DoxMDAip7Hw66QVI9jPJsYECgiF_4NC18c5ZMr8yoeDxx4Xouq_eD5mTOmQuWSNKkXKdBrayJwOVwCnoCEY1mBFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qEP1fReO-fyJ0xwF2BpTX0H70HqN-rUtwhQZXnCrAPGsg9ZoCQm1BsirBpu4fPQ90gtQb3imBizWE1jnrBJGoog3P115PZTRpcbhY2ou91hFJpU0mZNJUa96BTYbUax6XM8jPFsINiBXNIWCjHc1fbQxZxnzpsS05WC-IwZsNH03HNRZ1xCA8_xeP2ka8_bzERY08FUcB1ttI4pyC6-g_Z0ucxpF8_Ja9-CNRRCV4Z8eZmhvEqz7G5SXt5q0Vq1Ss5VAPkeF1pkhc25GN3AvB83TjzI4WZ_t4w96HiIc_Ls8_tNqR6KJm4aiPonzQLiWMrsaU1tbVBZ9_WqYZqpPtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EC5JHqmmHF1UIivuE-yR-ijDOLoSpIe45Guc_8Fvwt4VzkJsOWwZKqH4TvBKlH0jpifzu-Lkax_sQFq94MZaejhYbqDkVpXYG6waiPYmhfcrnvU6iJ_6A0tctBSggoNxuo9yhLvv68wKQq_1yjLS2D1CVErOnwhJUwtxUDYF1G_BAx9PS1GorCbevN_YvHblN48aJGQ6gXk2Z0Wxon6wP6bQy_yp986ugMhjCJROR7iTVFqYGaHjOC661mk-7DzGXf2Q0ZaIfI-4tQC8TZHY1IdLNq49CIn9_qhZeqaEBgCR82AToAEiR821gc6-d5zy7PWd8TFs6O5M4f5M8oGpaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ghb23aH4mZOAXI0YeOhQmf1B4tDj3ohWoKiEl2bdz6tE6eQv54ToZP2D8MGXszp03T9N1IR5A1BmaknY47vHmRub5WOULkaaD46_WnWXiGUTpvI-kQQ9U7LBmsw_Y5nb7UdgUERMBfQRCzE8kMXrBg48gRahfyKdvj385l4VgILXq2D81zYBo_uYg1ba4mW5odKPzBUlzCEEcvVnRNOrY4vh-unGfqcYCbKfDf6qkZJ29QKYBJbe88jCF8Fv8mmU_hUitX7nbkcbqItFH7uzEaWqmfSna0INAwxjG6gQCANk07MVVm3WI2ppYA2UH3AwbQlsLVZ15dTcBwzrQCEiYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Km0NxH8hbykHjMgSjxVZh6JSNsj7-chU7TZyFnQ45AhHy_r-HfMLn3c-GtnwUETzy756HqKZ0pCQ8mxtUuC8vNt7g_HOaMrIXpgzErlIYP1EOvKaKFSTJxQagFrMSK4gGVoOMCejjk7HhdzkZzqZCLg8JkTvKdLuizhmIwFZRts7Mb86O8uDyA3H1w_VogBxILfpBg7vkw7YVruUmB3CCGyx_6OpYEaUrL4jVizqtMJUXZA5VNrP1QkmTRc-VDxoPcaYBmDqxwGWo8bfPAL45rXeeT34eq6I1b8cNG_5ni6vURU8Pd6PoAUQq9koI8YBliIdsvp4ARHffM33AVoQQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QxnPa_TeLrNHKDI8ZrS9-37J-EmHv3WabP0niZiBFMNA7Cm8wvL9ocifvvO8tkffnu8n1yFUVdQIs1I5KIyM26t1mwFIRpLQwNZFN3LR9abTA8CLUZOmQ1k3x4UoJdvD3DSCFvKqC6aYtkBlbGpLwNYsP4UOd_kJ_AE_qb-Uu1rcvNNe2uU5AL3OiWzG89V1Jm4ZLiPEoXP9-SFBlk7S2zg0ZKLfzHL-YtpT2MnnyXFzRqds9A7ah-OGrjhWlp3DuTjbWk1RHkrjmvaeAOgrV8mMEETYzf_PbloDnBpq-EiVedAQHqmur4XAWzULNap8JaHhtE9dMF5Md8RDFS-VUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BWnfaBgi6OGXdsczULeOiIAOQSi6KouEWsZv8wTfk8XnJPnW8trjAa0q3USOP4mzIBYtDZ_RfHcUFvfq0UNUXsW65RdHp_rwJijyl6c3QmuKGdhh6WrX1PO4725olHfbrKZQtik45JJrQrKnWhoI-OTWyr2EUZUVdz3qo1kHWr8FwjJ4qogrjDeHLh9Q6nZvp6NkhtsPHfAcYjRrhB0Wp49Tek7BaJPpSL_vf2imRrAk3f9dbXhlH0ovuP4LR4SAaNHCpR-vRhZ-38gN6bpvnPLNHljdviHyPkgPCJaE2Kgd7xCwfqXnouJNJtmbw9QSPHtr0YllFknNcRIF8dmizw.jpg" alt="photo" loading="lazy"/></div>
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
