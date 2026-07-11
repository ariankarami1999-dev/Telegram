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
<img src="https://cdn4.telesco.pe/file/tg0MAjgGs4mlescbrKN-mtaa_NO9Pzt2woI6bSaS3DgCfLVP2bWkmjmyfHVIU39-p81wl-vbLx7UTxLVXlCySS0LIkGzE7ECkNnF9OcJrbH4NQNik2Ur2m-9n2dNBrUG0O4PFVuNHJ8NIe52t-XE1KOgpEpfgKR714Hun1Eck0LSpRIbASQlSd0hXwhHv8B3cGW8-4s7ds3GoNMxsM5mqeVcSQCByd2PA5_V1p1MTlc2DJAHB-PUgdtzrqfp9IC9kSKh7k-oldDz0AD-rMtnRCPxH700GwcI4qa_iBJdvdtdBZWrZbMjdcRLha_ibUMyoF_gNGFVZZPlTG3BBiQ0Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.83K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 10:37:55</div>
<hr>

<div class="tg-post" id="msg-6860">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ArchiveTel
pinned «
🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6860" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6859">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Tr - infinity.npvt</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6859" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">روز خوبیو توی این دوران سخت براتون ارزو میکنم
😜
🥰
Password :
@ArchiveTell</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/ArchiveTell/6859" target="_blank">📅 05:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6858">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔥
دریافت API رایگان بدون ثبت‌نام! اگر برای پروژه‌ها یا ربات‌های خود به یک API رایگان نیاز دارید، این سایت می‌تواند گزینه جالبی باشد.  ؛Dahl Inference بدون نیاز به ثبت‌نام، تنها با چند کلیک یک API Key در اختیارتان قرار می‌دهد که می‌توانید از آن برای استفاده…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/6858" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6857">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔥
دریافت API رایگان بدون ثبت‌نام!
اگر برای پروژه‌ها یا ربات‌های خود به یک
API رایگان
نیاز دارید، این سایت می‌تواند گزینه جالبی باشد.
؛
Dahl Inference
بدون نیاز به ثبت‌نام، تنها با چند کلیک یک
API Key
در اختیارتان قرار می‌دهد که می‌توانید از آن برای استفاده از مدل‌های مختلف هوش مصنوعی استفاده کنید.
ویژگی‌ها:
• بدون نیاز به ساخت حساب • دریافت فوری API Key • دسترسی به مدل‌های مختلف • مناسب برای تست، توسعه و پروژه‌های شخصی
هر کلید 100 میلیون توکن رایگان میده
😁
🔗
دریافت API:
https://inference.dahl.global/chatKeys#models
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6857" target="_blank">📅 01:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6856">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">؛
🎨
Lake: اپلیکیشن آرامش‌بخش رنگ‌آمیزی برای بزرگسالان
اگر بعد از یک روز پرمشغله دنبال راهی برای استراحت و دور شدن از استرس هستید،
Lake
یکی از بهترین گزینه‌هاست.
این اپلیکیشن مجموعه بزرگی از طرح‌های رنگ‌آمیزی را که توسط هنرمندان واقعی طراحی شده‌اند در اختیارتان قرار می‌دهد. از
مناظر و طبیعت
گرفته تا
معماری، دکوراسیون، حیوانات و پرتره
، برای هر سلیقه‌ای طرحی پیدا می‌شود.
✨
امکانات: •
🖌️
صدها طرح باکیفیت •
🎯
حالت هوشمند برای جلوگیری از خروج رنگ از خطوط •
🎨
ابزارها و پالت‌های رنگ متنوع
🆓
کلی طرح رایگان برای شروع
اگر به دنبال یک سرگرمی ساده و آرامش‌بخش هستید، Lake ارزش امتحان کردن را دارد.
نکته: فعلا فقط برای آیفون در دسترسه
🔗
سایت:
https://lakecoloring.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/6856" target="_blank">📅 01:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6854">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_mZQ9ppRJX1CF9OJsa_MOqDVphag-LlofFhLTZDUNOSm1zfVEbDBceV2UFimaDQQofdyFQxQElYLCtnwRb2ZtVPuPGghaLPhrLODz7ABmt8CHzJpSoIBrSkyexhbpHOLZpJTI8E-oFjkS08V16l533T4hfn7ZrYO4lL1VhUVo2ATYJa4qsgtc6tyiiYj_hstQA_7x-gnxCqvKR4tpllif29vRi0j-t7dLSN9u5C4ktNBVvUnbcOLaFem3qv-BXWOU-lg0mKulLu6muF5fl39Cy6W15jF7iqwFaU-kOA8XkFJiHQzD0NDTSHOmGnTwgnGiHG3xd2vucu6u-MZmkbtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SerbABpcPQcG9VshN5Emu-XIm1OS4XsULWCSd6-MPt6S8iYD0u6v_gg-yLmlaYZbSkGcCEuwKWistmAf24o1mcaZh4hHP6TA4WljLGK6l2ZLDqQ6v4WjEcz9BP8rrSF2Gxx5JhECbNog-UG3JPsMamR8_qX7d4smVZPpLToogtnOZWTqhS9XwdJmphj7ZLoUYBXW-qPq0ffFz2iuG21pPxck7HTt_de9G90oZkh0BUYRydms-OU_wMyQt-iQMHJcVN8Wtdzkn4MhItydjChnL72Nd2eC3Ed5bkS9NWCvYmzNJzGVYts2g5wL9n3gYvaOtKFShXxmEABcNChP-H1BJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/6854" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6853">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0
(اسکنر آیپی تمیز کلودفلر)
به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر کنم. امروز با افتخار نسخه اول
Archive Scanner
را به شما تقدیم می‌کنم.
🔥
قابلیت‌های فنی و تخصصی:
✅
اسکن پیشرفته SNI + TLS:
ما به پینگ ساده اکتفا نکردیم! با شبیه‌سازی کامل TLS Handshake، آی‌پی‌هایی را پیدا می‌کنیم که "واقعاً" کار می‌کنند.
⚡️
سرعتِ خیره‌کننده:
طراحی‌شده برای اسکن‌های فوق‌سریع که زمان شما را هدر نمی‌دهد.
🎯
حذف هوشمندِ آی‌پی‌های مرده (Dead-End Elimination):
فیلتر کردنِ آی‌پی‌هایی که پورتشان باز است اما عملاً ترافیک را رد نمی‌کنند.
✨
طراحی مهندسی‌شده:
طراحی و توسعه کامل توسط
Bachelor
⚡️
با تمرکز بر UI/UX مدرن (Material Design 3).
🛠
شفافیت و آینده پروژه:
من تمام تلاشم را کرده‌ام تا این نسخه در پایدارترین حالت ممکن باشد، اما چون در ابتدای مسیر هستیم (v1.0.0)، ممکن است باگ‌های جزئی وجود داشته باشد. من متعهد هستم که در آپدیت‌های بعدی این موارد را سریعاً برطرف کنم.
💡
خبر خوب:
این نسخه از
آپدیت درون‌برنامه‌ای (In-App Update)
پشتیبانی می‌کند؛ بنابراین به محض انتشار نسخه جدید، شما باخبر خواهید شد و نیاز به دانلودِ دستیِ مجدد نخواهید داشت.
📥
لینک دانلود مستقیم (گیت‌هاب)
این اپلیکیشن حاصل روزها تلاش مستمر من برای ارتقای استانداردهای جامعه شبکه است. اگر باگی دیدید، حتماً اطلاع دهید تا در آپدیت‌های آینده برطرف شود.</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/6853" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6847">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVr18DkdbZW74GLK5RxXU2lZh2Sp5igzLvr0aWcOSkPXpFIDMOJp1FMDKsa_2WXn86qLFuAZDKUZLroEysj4vH-Qz1FubSiAJC7nvK8zESLzbX7vDb2wjaZfz0MznDrqerUhOx6Xa9MfSUJ0a6HL2bwph_knHyAfaBi3LhjGFKwdTGFUpsNYmvxAJOo0VkQUiYK1cbq14Z_442lLljo6LOKhX_N3zTJBn9pOWLitz-UR3o0Ka_HnvRwbKpEUSloRoIDCwFILADkxyTjgUTTvL6b0TAP9ptkH9fJHB-CYIpFVR7iMi8Ibu4DKaEYQs9wMJ7ehKdUAWAAGVDyw6eQH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
‏
🎮
آیا ‌GTA 6⁩ زودتر از موعد به کامپیوترها می‌آید؟**
🖥️
🔥
‏شاید غیرممکن به نظر برسد، اما توسعه‌دهندگان امولاتور ‌SharpEmu⁩ در حال برداشتن قدم‌های بزرگی برای اجرای بازی‌های ‌PS5⁩ روی ویندوز هستند!
🛠️
‏
✅
چه اتفاقی افتاده؟
‏تیم سازنده موفق شده بازی سنگین ‌Demon's Souls⁩ را تا مرحله لودینگ و صفحه اصلی روی کامپیوتر اجرا کند. این یعنی معماری ‌PS5⁩ در حال رمزگشایی است.
‏اگر این روند با همین سرعت پیش برود، برخی امیدوارند که بتوانند ‌GTA 6⁩ را قبل از انتشار رسمی نسخه ‌PC⁩، از طریق این شبیه‌ساز روی سیستم‌های قدرتمند تجربه کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6847" target="_blank">📅 22:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6846">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
۱۰۰۰ اعتبار رایگان در Flashloop برای ساخت ویدیوهای هوش مصنوعی!
🎥
اگر به ساخت ویدیو با هوش مصنوعی علاقه دارید، می‌توانید با ثبت‌نام در Flashloop، ۱۰۰۰ اعتبار رایگان دریافت کنید.
مراحل دریافت اعتبار:
1️⃣
وارد سایت شوید:
https://www.flashloop.app
2️⃣
با حساب گوگل (یا سایر روش‌ها) ثبت‌نام کنید.
3️⃣
هنگام ثبت‌نام یا در بخش مربوطه، کد زیر را وارد کنید:
Z36ZT9
🎉
با وارد کردن این کد، ۱۰۰۰ اعتبار رایگان به حساب شما اضافه می‌شود.
با Flashloop می‌توانید انواع ویدیوهای AI در سبک‌های مختلف تولید کنید و از ابزارهای ویرایش و افکت‌های متنوع آن استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6846" target="_blank">📅 20:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6845">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKV5uRLYveRqNaE2eIEf9YlRWhPmlPUTBrxFmkGriMJZHHMbuotOwmDzx4pWiHgUexedAky0kESfJ-VNK2k2nsSN_6-ZF0-z-enXER15qGm38hV1rRz8atB0bl1snv7UBvIAkf2Jra8SraiWJ4OxHQIv82XOh_NeT0qtqf7wCgpjvg6w63qonh9RzBgtGiKX3kd2EpHO1U1mqThwYnMQgqXElYk08iibncwxxhjAEeZVbCGE3sJ75pkmpoZfy7r5Cc2lBiqjlQSZozrlVV2FWVDmSaDwVUH0t_LvpPFH9yiRcz_ikwgsVnzLnBB5N6lvkldOWz2_iOCYpXvYb3NiKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐧
GameShell
GameShell
یک پروژه
متن‌باز
برای یادگیری دستورات لینوکس و
Bash
است که به‌جای آموزش سنتی، مفاهیم را در قالب مراحل و مأموریت‌های تعاملی آموزش می‌دهد
🔹
اگر قصد دارید کار با ترمینال و دستورات لینوکس را به‌صورت عملی و سرگرم‌کننده یاد بگیرید،
GameShell
می‌تواند نقطه شروع مناسبی باشد
◾️
🔺
GitHub
✔️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6845" target="_blank">📅 20:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6844">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نامحدود
🫡
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprMWRCT21PQjRvcWk3VW1wMzdhMWJR@82.38.31.189:8080#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6844" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6843">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نامحدود
🔥
vmess://771a590c-5eac-5732-b796-17251132f8d2@47.83.221.185:80?encryption=auto&security=none&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6843" target="_blank">📅 18:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6842">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏
💎
گنجینه‌ای از ۱۰,۰۰۰ پرامپت طلایی!
🍌
✨
‏اگر به دنبال خلق تصاویر خیره‌کننده با هوش مصنوعی هستید، این مخزن دقیقاً همان چیزی است که نیاز دارید!
🎨
🚀
‏
✅
ویژگی‌های این مجموعه:
🔹
بیش از ۱۰ هزار پرامپت منتخب و تست‌شده
‏
🔹
بهینه‌شده برای
‌Nano Banana Pro (Google Gemini)⁩
‏
🔹
سازگاری کامل با ۸ مدل برتر دنیا (از جمله ‌Midjourney⁩، ‌DALL-E⁩ و ‌Flux)⁩
‏
🔹
همراه با پیش‌نمایش تصاویر برای درک بهتر خروجی
‏
🔹
کاملاً متن‌باز (‌Open Source)⁩ و رایگان
‏
🔗
https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6842" target="_blank">📅 16:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6841">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416755798a.mp4?token=RsOiJW_x3GWwUoRMspsPKNx3ZeRJsz9xYNDNnPcuH3zhBrowBFXNRNHjm-cedD9rtPMUZqZ_dvMu4AAp-FJGwjDOrOS7eRCZmH2X7TLAFXphG3h6hzmpOSudI2_Yne5MCNmzngZffPtjdq65Fsd9-2UgaCvDu6664PICb7AIpIGl3vRIJixuDoVN8SDrjpy9Y836H3T0eD4HRVl7r1rl1qyFOOJ2Fi4BN4Hb9_e9QyMm7ZCjn12DflB9lRRRSXiVpme7Fs9keM1joJUnRewY6vEtmJtIDAz0unD1aWR5_NoTSSL6JPZ1vCKlYc74bwTsQDDfXKo7hEG2xw9BLyCkCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416755798a.mp4?token=RsOiJW_x3GWwUoRMspsPKNx3ZeRJsz9xYNDNnPcuH3zhBrowBFXNRNHjm-cedD9rtPMUZqZ_dvMu4AAp-FJGwjDOrOS7eRCZmH2X7TLAFXphG3h6hzmpOSudI2_Yne5MCNmzngZffPtjdq65Fsd9-2UgaCvDu6664PICb7AIpIGl3vRIJixuDoVN8SDrjpy9Y836H3T0eD4HRVl7r1rl1qyFOOJ2Fi4BN4Hb9_e9QyMm7ZCjn12DflB9lRRRSXiVpme7Fs9keM1joJUnRewY6vEtmJtIDAz0unD1aWR5_NoTSSL6JPZ1vCKlYc74bwTsQDDfXKo7hEG2xw9BLyCkCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
؛Traycer Desktop App منتشر شد!
رایگان، متن‌باز و ساخته‌شده برای AI Orchestration.
✨
قابلیت‌های جدید:
• استفاده از اشتراک‌های فعلی مثل Claude، Codex، Opencode و...
• ارتباط Agent-to-Agent و Loops
• ؛Workspaceهای دائمی با Tab و Sub-tab
• اشتراک‌گذاری Taskها و همکاری با اعضای تیم
امروز دیگر توانایی مدل‌های هوش مصنوعی چالش اصلی نیست.
چالش واقعی، ساخت محیطی است که Agentها بتوانند به‌صورت هماهنگ با هم کار کنند، حافظه مشترک داشته باشند و از هر جایی ادامه‌ی کار را از سر بگیرند.
؛Traycer دقیقاً برای حل همین مسئله ساخته شده است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6841" target="_blank">📅 15:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6839">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚀
تبدیل Qwen Chat به API رایگان!
اگر همیشه دوست داشتید از
Qwen
داخل پروژه‌ها، ربات‌ها یا برنامه‌های خود استفاده کنید، این پروژه دقیقاً برای همین ساخته شده است.
؛
FreeQwenApi
سایت
Qwen Chat
را به یک
API رایگان و سازگار با OpenAI
تبدیل می‌کند؛ یعنی می‌توانید بدون تغییر زیاد در کد، از مدل‌های Qwen داخل پروژه‌های خود استفاده کنید.
✨
قابلیت‌ها
✅
تبدیل Qwen Chat به API
✅
سازگار با OpenAI API
✅
پشتیبانی از Streaming
✅
پشتیبانی از فایل، تصویر و Web Search (در مدل‌های پشتیبانی‌شده)
✅
قابل استفاده در Open WebUI، LobeChat، Dify، Claude Code و...
🛠️
آموزش راه‌اندازی
1️⃣
پروژه را دانلود کنید
git clone https://github.com/y13sint/FreeQwenApi cd FreeQwenApi
2️⃣
وابستگی‌ها را نصب کنید
npm install
3️⃣
پروژه را اجرا کنید
npm start
4️⃣
وارد حساب Qwen شوید
توکن (Session Token) اکانت Qwen خود را داخل پروژه قرار دهید؛ از این به بعد می‌توانید از Qwen مثل یک API معمولی استفاده کنید.
⚠️
این پروژه API جدیدی ایجاد نمی‌کند؛ بلکه از دسترسی رایگان حساب Qwen شما استفاده کرده و آن را به یک API سازگار با OpenAI تبدیل می‌کند.
🔗
GitHub:
https://github.com/y13sint/FreeQwenApi
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6839" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6838">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">vless://c44c7433-5460-4269-a7de-0af05e27a48f@64.90.7.33:8080?type=kcp&headerType=none&seed=SwbMceiT2H&security=none#%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86
نامحدود
اگه دیدید قطع شد ip فیلتر شده
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6838" target="_blank">📅 14:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6837">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJ-I2_zaI7SrVVLVFcdY9MaH2H5KlVv-dvNbGHiZxuwBPnyL7QWUEKCRDmq88QW93nYCcDf_3sOPnLqjTRwtYMAYIi2h90SlXZlgsNe9vJr_jp448k_Lkn41_1Np8t4IiZrceOAeIsThJcHBT0k91E9RQIhwjVNiy_1NY8m33R7zoRglwwNviGGwMfSQTREbFBuGj9UEz_TUZ21DlUU6rLqqqt7HC0zoqtKJPJyVql4ebkJ5bS8oSbGPFgseUX0H7eS-5sErX2NnyWXeEsdPxGLcZOWB7D8Hm1meIFruFcubltISQ51F_fPSAkhR-XJJUGTCm7sNSbhgo-SkLJ4JMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
یک ابزار جذاب برای کار با ویدیو!
معرفی Frame؛ رابط گرافیکی بومی برای FFmpeg ساخته‌شده با Rust
🦀
؛FFmpeg فوق‌العاده قدرتمنده، اما کار با خط فرمانش برای خیلی‌ها سخت است. Frame همان قدرت را با یک رابط ساده و زیبا در اختیار می‌گذارد.
🔥
امکانات:
⚡
ارتقای کیفیت تصویر با AI (Real-ESRGAN)
🚀
شتاب‌دهی سخت‌افزاری (Apple Silicon و NVIDIA)
📦
مدیریت چند پردازش همزمان
🔒
کاملاً لوکال؛ بدون تله‌متری و بدون نیاز به حساب کاربری
💻
پشتیبانی از macOS، Windows و Linux
﻿
یک انتخاب عالی برای کسانی که با تبدیل، فشرده‌سازی و پردازش ویدیو سروکار دارند.
🎥
github.com/66HEX/frame
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6837" target="_blank">📅 04:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6836">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
؛Grok 4.5 رایگان شد!
مدل جدید کدنویسی Grok 4.5 از xAI برای مدت محدودی به‌صورت رایگان در ابزارهای Agent قابل استفاده است.
✨
ویژگی‌ها:
🧠
پنجره متنی 500K برای پروژه‌های بزرگ
⚡️
مناسب برای Agentهای کدنویسی و جلسات طولانی
🔌
سازگار با Hermes، Aider، OpenCode، Cline، Claude Code و تمام ابزارهای سازگار با OpenAI API
⚙️
راه‌اندازی در کمتر از ۲ دقیقه:
curl -fsSL https://x.ai/cli/install.sh | bash
سپس:
• آدرس
localhost:8000/v1
را به ابزار خود معرفی کنید.
• مدل grok-4.5 را انتخاب کنید.
• یا از API Key در کنسول xAI با آدرس پایه
https://api.x.ai/v1
استفاده کنید.
⚠️
این دسترسی محدود و موقتی است و شامل Rate Limit می‌شود. (شاید ۱۲ ساعت مونده باشه ازش) (تست نشده)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6836" target="_blank">📅 04:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6835">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmw3KWIgc7fGKpJ75QfQC8oiHNfX_LVjmsnklnM9cIn-zjTN9D1NIkDh4JAckZgpU_M-Qeq5OzuGqCF7T4dRKriDUgXaH5aizyckwwg0l77gUy6mwD0sNA8CSWhR3jmBEKizlaqq8nJDumDBXmOuY3DHT1EZa8-fV3Vs3EnHFlSb4Iq-mXNbP9KrMWwgxhA-Nh504o292lejuwtOJDqZTWBgeKsvKD1hV_e5Bki9zpg8Q4KYOta8HrV9vJIL7aXn0FcDfESM-whmNnrMOPLwaG4_iOZCT2b5rcGYhHSielxM_wNMFtN3G5Kk9UWE6QJPGifr82Up8dHatUN8oKmYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧭
؛MBCompass؛ قطب‌نما و مسیریاب متن‌باز برای اندروید
یک اپلیکیشن سبک و رایگان برای طبیعت‌گردی، کوهنوردی و استفاده روزمره؛ بدون تبلیغات، بدون ردیابی و بدون وابستگی به سرویس‌های گوگل.
✨
امکانات:
🧭
قطب‌نمای دقیق (شمال مغناطیسی و واقعی)
📍
نمایش موقعیت لحظه‌ای روی OpenStreetMap
🗺️
پشتیبانی از نقشه‌های آفلاین و آنلاین
🥾
ضبط مسیر و خروجی GPX
🔋
حجم کم (~۲ مگابایت) و مصرف باتری پایین
🔒
بدون تبلیغات، بدون جمع‌آوری داده‌های شخصی
یک گزینه عالی برای علاقه‌مندان به سفر، طبیعت‌گردی و مسیر‌یابی.
🌿
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6835" target="_blank">📅 03:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6833">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter وارد سایت Agentrouter شوید با حساب Github ثبت‌نام کنید بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key وارد سایت شوید…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6833" target="_blank">📅 00:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6831">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4CwenYnIKDmMU-FuhZWmptiIny2DbPrOVCAYLxFy5sfK-RZExs5trrTxg5VGW-4dd4GmWxs-k2_6A_vWcDegenGrwUfTsNgu9RLemE9h42u_jZ_VnmiS3V7y5fWeny67yoCYp2Va0Rxr53SoDLKSOQ1cZC53CZZnhYo-DmVKcZDaTbhx9mjnBb4Jt_e0U1nBfHszbkD--RbiAYW9MvrQZSkXVUaQhLY9dTj8F4XgbDeVoeQ1NDyFby_bpOsQUiOwz-C54BF9O-D0hYYLWkqhc8dqQadFDohgtElF_kOc8nIi3eAoT6DtxdVg3KsZ-odZRd3oRp9l21tZEci5suxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
🚀
؛Cloudflare Drop؛ انتشار سایت در چند ثانیه!
کافی است پوشه پروژه‌تان را داخل مرورگر Drag & Drop کنید تا سایت فوراً روی شبکه Cloudflare منتشر شود.
✨
ویژگی‌ها:
⚡
بدون نیاز به ثبت‌نام
🌍
دسترسی جهانی با تأخیر بسیار کم
📁
مناسب برای دمو، نمونه‌کار و پروژه‌های آزمایشی
⏳
نسخه‌های بدون حساب تا ۶۰ دقیقه فعال می‌مانند و سپس حذف می‌شوند؛ با ثبت‌نام می‌توانید آن‌ها را دائمی کنید.
https://cloudflare.com/drop/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6831" target="_blank">📅 00:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6829">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWYnpqrIahDeGoNOqU4EjMRwgLGdavqQojNwnn3EIN4SfZzQJ3pmATfk8-o9yFU5W4jdnGSpw21r8SvgjG2VIi0IAu9id-mmQrDNmpHmZjy7KrX5piN0oFxNyHK-XdoYNiFtbUnh0gTjStv57Me7osYjUIparNR-G45uflJ70kwgOl2c52WCtXvbvZTo9eOhtgXpQeVtMtNIGf0hGv1AWKeMyhbN01TN0eVde005JXt2rdHW0TzUg9b1AkfuBt_qX9XW6oLwIWgnEy2TcvSJV2BpKD9srvkWMyitzXV8aboMjrlyL35miCZ9lT_upM9GPDA8oiG6SYK-Ot5ObrYdZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6829" target="_blank">📅 23:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6828">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🧩
؛CanvasMind | ساخت و استقرار ورک‌فلوهای AI با بوم بصری
✨
یه ابزار متن‌باز و Low-Code برای طراحی و اجرای ورک‌فلوهای هوش مصنوعی! دیگه فقط دمو نیست، مستقیم به پروژه قابل استقرار تبدیلش کن
🚀
⚡
ویژگی‌ها:
🎨
بوم گرافیکی با Drag & Drop
🔀
شرط، حلقه و منطق کنترلی
💻
اجرا محلی یا از راه دور via SSH
🤖
دستیار هوشمند داخلی
🚀
خروجی CLI، API، Docker و Server
🔗
https://github.com/buyaka/canvasmind
#هوش_مصنوعی
#LowCode
#ورک‌فلو
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6828" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6827">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📱
💿
؛EtchDroid؛ ساخت فلش بوتیبل با گوشی اندروید
اگر کامپیوتر در دسترس ندارید، EtchDroid به شما اجازه می‌دهد فایل‌های ISO سیستم‌عامل‌های لینوکسی را مستقیماً از طریق گوشی روی فلش USB رایت کنید و یک فلش بوتیبل بسازید.
✨
ویژگی‌ها:
🔹
متن‌باز و رایگان
🔹
پشتیبانی از اکثر توزیع‌های لینوکس و Raspberry Pi
🔹
مناسب برای مواقعی که سیستم بالا نمی‌آید و فقط گوشی در دسترس است
⚠️
این برنامه از ISO رسمی ویندوز و فایل‌های DMG مک پشتیبانی نمی‌کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6827" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6826">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🤖
؛Cogny | دستیار هوش مصنوعی بازاریابی
✨
یه ابزار فوق‌العاده که بازاریابی رو با هوش مصنوعی انجام میده! سئو، تبلیغات، تحلیل رقبا و کلی کار دیگه
🚀
⚡
ویژگی‌ها:
🎯
سئو و بهینه‌سازی محتوا
📊
تحلیل کمپین‌های تبلیغاتی
🔍
آنالیز رقبا و بازار
✍️
تولید متن تبلیغاتی
📈
اتصال به ۱۳ کانال بازاریابی
💻
کار با Claude، Cursor و Codex
💰
رایگان برای شروع · ۹ دلار برای استفاده نامحدود
🔗
https://cogny.com
#هوش_مصنوعی
#بازاریابی
#سئو
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6826" target="_blank">📅 21:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6825">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wkvg4sMClycW5d14nwb3JmvamtEigDZXwuhVsnT6Ae1BN3Vxz7mKkm5w28ZP5Upwvwyw0gGDpAGhkZPakE5-TQSAiTfl3OFsVh7NCNGEsE6oqDaYYQtLWQFmIN8u4JaD7MPrHcnsmXiivot93wQh7cQKuyfU8qFKv4aI5CzwzGg5P8Z2VjolLQ55CllGDPlR1Un3N59cGh6gwuZLxcXJFfkEXttp-dD5CZ20K9S5Dg5LMMPbaTyYlcTvMOR8Nec2hJembwKqiqQyLsECN-OdI7NgLLIPNx_aiReqhRn-gP6fU2JqJApQ0uZ4hIz7nNLTutz_MMEQtkzXx5gYsBrAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6825" target="_blank">📅 20:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6824">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">104.17.14.0
104.25.49.102
ایپی تمیز کلودفلر
تست کنین
❤️
با لایک و دیسلایک و کامنت اعلام کنین
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6824" target="_blank">📅 20:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6821">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqlzlKMnQtFEoxCXOJ_6KJEi6TePAVFtYodrYI-ZNCpPkvfkX8sUP-MGT22Rsf-Uw9jYRQE0BdPX7gsA7Ma76J5bi9GKdVLpPWDVs9FXW92oOsK2htrK-1YIHcwjJqpLbRiUEE4pUZ8mTfySIJ78-VguUXoWTXXa59xex6BDVGOL89MxP7AWbr6AbRug_Bncqvybki5LXcaxZKy7OCnAow3JODE1wbQ5ZazrSf1m7J-w_LzdUUx_nm8AkbEAJ549TQPW7oUax202Yde9EFOwSoW0Wl5GXL4uFGm9mgCyYpR2Am96tgznMkHPfIUbJAQaFuHqJLHNTTRU9zeXX-ca3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vj4c2D8O4yVxKvBMh8dG0bLB2c39K07Aheiw33ROyxVBKKQk3c8ZqDTOWOef3O2KFQzd7HRGHoh7gAxoht2weFGgI88XTrJvrZSCinuU88XqE_9nzyL3_RjBksFZ8vXPh_o2Z8XC4yofjGk6q59Iv0-9DOxfyakusuv4qQnO0e8KYZ6g6Ol4s5oD8-vmaUHDmTbkcqZl6gkwWm3jEgD46FsUDGvxWPcymxksfizp2YW6i78ZaflBI-hucML8BIyOQjFoSDgbzAlxSsfFdbr_vxASbIqAtMakrcXXZJG9WyH67hU1c33ZmhUlESkwPGaQ18CCas-RZhg_yPrJzYoaHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏‌
Imgfree⁩: ابزار رایگان تولید تصویر و ویدیو با هوش مصنوعی
🤖
‏
🌐
پلتفرمی که مدل‌های پیشرفته هوش مصنوعی مانند ‌‌Midjourney⁩، ‌GPT-Image⁩ ، ‌Kling⁩ ، Nano Banana و Flux را گرد هم آورده است
📈
‏
✨
تولید تصویر و ویدیو بدون نیاز به تنظیمات پیچیده
📺
‏
🔗
لینک: ‌
https://www.imgfree.co
⁩
‏
💻
دسترسی رایگان و نامحدود برای تولید محتوای با کیفیت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6821" target="_blank">📅 19:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6820">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP6mFC7Lnc1ZF-A4kA8kd0-SA6c0x8qe-6cRJybYy795qU5UtlgdZrAYOE5DLQpAYDJkFezYP4lTSK5JbOGhhX9MrOb3M-O3WEHCsFIpxLLjgT5LfcYBCBFyGYt4bf-WyK53v65uA7wwDZ80__8WzOgmi6w7h0YoL7Jz7PKYBTH23NDiRAiOwmzmmSu9CFHvDar-5PMUeqSLPHc6YN3AJmxlKLa4LlPlNv6wvYvJRER9i9TgZ3qb6kzkxxgLe3NFMQgy3_O7yUYb75U-zbdrrvFcOftaEcDrZ7bLClVCME82RBlf5JcGOS8xAPbWK1uxplWF7vV380yBrlJj_bSOrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛
🎬
CapCut Web؛ ادیت ویدیو با هوش مصنوعی
اگر تولید محتوا می‌کنید یا برای شبکه‌های اجتماعی ویدیو می‌سازید،
CapCut Web
یکی از کامل‌ترین ابزارهای آنلاین برای تدوین سریع و حرفه‌ای است.
با قابلیت‌های هوش مصنوعی این پلتفرم می‌توانید:
•
🪄
حذف خودکار پس‌زمینه و نویز صدا
•
📝
ساخت زیرنویس خودکار (حتی برای فارسی)
•
✂️
تبدیل ویدیوهای طولانی به کلیپ‌های کوتاه مناسب ریلز و شورتز
•
🎨
استفاده از افکت‌ها، قالب‌ها و ابزارهای هوشمند ادیت
🔗
سایت:
https://www.capcut.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6820" target="_blank">📅 18:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6819">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌐
دانلود کامل هر وب‌سایت با Website Downloader
اگر می‌خواهید یک وب‌سایت را برای استفاده آفلاین یا بررسی کدهای آن دانلود کنید(فرانت اند)،
Website Downloader
ابزار مناسبی است.
✨
قابلیت‌ها: •
📥
دانلود کامل
HTML، CSS، JavaScript، تصاویر و فونت‌ها
•
🔗
بازنویسی لینک‌ها برای اجرای آفلاین •
📦
خروجی به‌صورت فایل ZIP •
⚡
متن‌باز با لایسنس MIT
این ابزار برای
کلون کردن سایت‌ها، تهیه نسخه آفلاین و یادگیری ساختار پروژه‌های وب
بسیار کاربردی است.
🔗
GitHub
:
https://github.com/AhmadIbrahiim/Website-downloader
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6819" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6818">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=dYfI3Ege1E6YiQQtZ-pPtTJa0igtsNP466wU27GW6Ao8F-05wiBEazCYJZSL7st0l6aZgbWqcqBcN_t5yR-RlZ4ETM0nSPWp7lKdiI_jFMypr_G2oFEG3B6CpX2R_5kZB1o6CW1IeMIJ5ouKu1d_Ps0BJUdq7fkQIZPPcJldjI-Z5xaHlhLUVnOMgepq5V7AbOY-e0DCq80gQzmD0v2CiFaNp70Y8lLl-lPUslDELp-z-Ko9Kz4OwBgrXX8UGLT5J880qQW5HP2iqnztvpblRjXNsLEh-DfWDKB7c0oUY-HS6bZDu9SLjFMzRZU3vI3qKgkJTr85nzLE5MLeUjjo0jTof4-NDLDT-zR0L-92qmdqSh99Tma5d6pLCI2QxI4oOhmrrgtn1iP_-_Gpk7GwiprjP52xfz4RzwFq3Py5xl9F8XFnr2zy1V2LGBZflP2bYuVr8HwN0Wp-lPhngBtkfIt3GoEND9JUYS6TwmmgBNofZVv2BB8CAAJZQWBZJviTz4Y7qAiz27oSZaP0Q_BtHDveGP_uatJUa38USGxJ_AZqiN6r2-cZhkyGv4SYWtG63-cQO7SiNLRwnQ23iKSganFeaCV5zNCjuUZeC5T9Wv_BPT063dNKaYpqXL_5AYqNTr2xajbuers1R46Llum0QjczylKzdtBoKpMsbkBzcBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=dYfI3Ege1E6YiQQtZ-pPtTJa0igtsNP466wU27GW6Ao8F-05wiBEazCYJZSL7st0l6aZgbWqcqBcN_t5yR-RlZ4ETM0nSPWp7lKdiI_jFMypr_G2oFEG3B6CpX2R_5kZB1o6CW1IeMIJ5ouKu1d_Ps0BJUdq7fkQIZPPcJldjI-Z5xaHlhLUVnOMgepq5V7AbOY-e0DCq80gQzmD0v2CiFaNp70Y8lLl-lPUslDELp-z-Ko9Kz4OwBgrXX8UGLT5J880qQW5HP2iqnztvpblRjXNsLEh-DfWDKB7c0oUY-HS6bZDu9SLjFMzRZU3vI3qKgkJTr85nzLE5MLeUjjo0jTof4-NDLDT-zR0L-92qmdqSh99Tma5d6pLCI2QxI4oOhmrrgtn1iP_-_Gpk7GwiprjP52xfz4RzwFq3Py5xl9F8XFnr2zy1V2LGBZflP2bYuVr8HwN0Wp-lPhngBtkfIt3GoEND9JUYS6TwmmgBNofZVv2BB8CAAJZQWBZJviTz4Y7qAiz27oSZaP0Q_BtHDveGP_uatJUa38USGxJ_AZqiN6r2-cZhkyGv4SYWtG63-cQO7SiNLRwnQ23iKSganFeaCV5zNCjuUZeC5T9Wv_BPT063dNKaYpqXL_5AYqNTr2xajbuers1R46Llum0QjczylKzdtBoKpMsbkBzcBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌎
نقشه آینده زمین برای زندگی!
‏این پروژه خیلی جالب و مهمه! یه نقشه تعاملی به نام ‌Farmland Atlas⁩ ساخته شده که پیش‌بینی می‌کنه مناطق مختلف زمین چقدر برای زندگی مناسب خواهند بود تا سال ‌2100⁩.
🤔
‏این پلتفرم با تحلیل بیش از ‌5⁩ میلیون نقطه، چندین سناریو رو بررسی می‌کنه، از خوش‌بینانه تا بدبینانه. برای هر مکان، پیش‌بینی آب و هوا، ارزیابی کیفیت منابع آب، وضعیت خاک و خطرات اجتماعی رو هم در نظر می‌گیره.
🌟
🔗
https://farmlandatlas.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6818" target="_blank">📅 14:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6817">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📊
معرفی ابزار CodexBar
اگر از
Claude Code، OpenAI Codex، Cursor، Gemini، OpenRouter، GitHub Copilot
یا سایر ابزارهای AI استفاده می‌کنید، احتمالاً بارها با محدودیت استفاده یا تمام شدن سهمیه مواجه شده‌اید.
؛
CodexBar
یک ابزار متن‌باز برای macOS است که تمام این اطلاعات را مستقیماً در نوار منو نمایش می‌دهد تا همیشه بدانید چقدر از سهمیه‌تان باقی مانده است.
ویژگی‌ها:
• نمایش میزان استفاده و سهمیه باقی‌مانده
• نمایش زمان دقیق ریست شدن محدودیت‌ها
• پشتیبانی از Claude، Codex، Cursor، Gemini، OpenRouter، GitHub Copilot، Groq، Deepgram، MiniMax،
z.ai
و ده‌ها سرویس دیگر
• نمایش هزینه، اعتبار و میزان مصرف API در سرویس‌های پشتیبانی‌شده
• نمایش وضعیت آنلاین سرویس‌ها و اختلالات احتمالی
• حالت تجمیعی برای مدیریت چندین سرویس از یک پنل
• بدون ذخیره رمز عبور؛ از نشست‌ها و لاگین‌های موجود شما استفاده می‌کند.
🔗
GitHub:
https://github.com/steipete/CodexBar
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6817" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6816">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
چند ابزار متن‌باز و رایگان برای برنامه‌نویس‌ها و سازنده‌ها:
🎨
Text Effects
افکت‌های جذاب CSS برای طراحی متن و رابط وب.
📧
SESPulse
داشبورد متن‌باز برای مدیریت و بررسی ایمیل‌های Amazon SES.
🔎
API Finder
مخزن APIهای عمومی برای پیدا کردن سرویس‌های آماده.
🛡
Tirreno
فریم‌ورک امنیتی متن‌باز برای شناسایی رفتارهای مشکوک کاربران.
💻
OpenTUI
کتابخانه ساخت رابط‌های کاربری زیبا در ترمینال.
✨
ابزارهای کوچک، کاربردهای بزرگ برای ساخت سریع‌تر پروژه‌ها.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6816" target="_blank">📅 13:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6815">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://ac7e7b41-0dc0-4bec-a285-3266ecbb87c8@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6815" target="_blank">📅 13:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6814">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📸
ساخت عکس پرسنلی ۳×۴ با هوش مصنوعی
اگر یک عکس معمولی از خودتان دارید، می‌توانید با پرامپت زیر آن را به یک
عکس پرسنلی رسمی
تبدیل کنید.
✨
ویژگی‌ها:
✅
پس‌زمینه سفید یا خاکستری ساده
✅
نورپردازی طبیعی و یکنواخت
✅
حذف اشیای اضافی و اکسسوری‌ها
✅
افزایش کیفیت و وضوح تصویر
✅
مناسب برای عکس پرسنلی و پاسپورت
📝
Prompt:
Convert this photo into a professional ID/passport photo.
- Neutral plain background (light gray or white, evenly lit, no texture).
- Centered face and shoulders visible, crop from top of head to chest.
- Natural skin tone, balanced lighting, no shadows.
- Neutral facial expression (slight smile allowed).
- Professional look, no accessories (remove hats, sunglasses, background objects).
- Enhance sharpness and clarity.
- High resolution, suitable for official use.
💡
برای بهترین نتیجه، یک عکس با نور مناسب و کیفیت خوب به مدل بدهید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6814" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6813">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📄
olmOCR | تبدیل هوشمند PDF به Markdown با هوش مصنوعی
یک ابزار متن‌باز برای تبدیل فایل‌های PDF، PNG و JPEG به متن و Markdown تمیز با حفظ ساختار اسناد؛ مناسب برای مقالات، کتاب‌ها و فایل‌های اسکن‌شده.
🚀
⚡
ویژگی‌ها:
📝
تبدیل PDF و تصاویر به Markdown خوانا
📊
پشتیبانی از جدول‌ها، فرمول‌ها، دست‌خط و قالب‌بندی‌های پیچیده
🧹
حذف خودکار هدر و فوتر صفحات
📚
حفظ ترتیب طبیعی متن حتی در اسناد چندستونه و دارای شکل
⚡
دقت بالا با پشتیبانی از پردازش محلی یا سرورهای vLLM
🔓
متن‌باز با لایسنس Apache 2.0
🔗
https://github.com/allenai/olmocr
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6813" target="_blank">📅 10:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6812">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">؛
🛠️
OfficeCLI؛ هوش مصنوعی برای Word، Excel و PowerPoint
؛
OfficeCLI
یک ابزار متن‌باز جدید است که به دستیارهای هوش مصنوعی امکان کار مستقیم با فایل‌های
Word، Excel و PowerPoint
را می‌دهد.
✨
قابلیت‌ها: •
📄
ساخت و ویرایش اسناد Word •
📊
ایجاد و تحلیل فایل‌های Excel •
📽️
ساخت و ویرایش ارائه‌های PowerPoint •
✅
بررسی و اصلاح خودکار خروجی‌ها
نکته جالب اینکه
بدون نیاز به نصب Microsoft Office
کار می‌کند و از محیط‌هایی مثل
Claude Code، Cursor و Codex
نیز پشتیبانی می‌کند.
🔗
GitHub:
https://github.com/iOfficeAI/OfficeCLI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6812" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6809">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=V0gJjkacoe3WO3oZ8QtM7SqcWdG5rmxS0GKK4g3Jy2ug15HGVVrd_SFJZTsX8Agok5ah-PUQQZSPMpBFvLxjn9LdHonnvP7-RtWUp818KrmjMyMmOPJCfC5T6yNiMRTZUvVkCaqHf3PSkiZWkIejgheEYxwP2Uv33WzlpCqXHNyPgzFFjT9fwZWmNzo60rtgkXEQ9THZeK1cCjJThSV1eIr-Q_9PgRvIN43frCM58Nk0-J0SG0ugPEg4k8V1fkLgL6WtqmoG7zuNVipzo4JyHNOOo7o59nNpEVxAdw822IQeDzndeCPhgUC-jiJFihS6VNK9AF_jpHb4wIZz5oT4vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=V0gJjkacoe3WO3oZ8QtM7SqcWdG5rmxS0GKK4g3Jy2ug15HGVVrd_SFJZTsX8Agok5ah-PUQQZSPMpBFvLxjn9LdHonnvP7-RtWUp818KrmjMyMmOPJCfC5T6yNiMRTZUvVkCaqHf3PSkiZWkIejgheEYxwP2Uv33WzlpCqXHNyPgzFFjT9fwZWmNzo60rtgkXEQ9THZeK1cCjJThSV1eIr-Q_9PgRvIN43frCM58Nk0-J0SG0ugPEg4k8V1fkLgL6WtqmoG7zuNVipzo4JyHNOOo7o59nNpEVxAdw822IQeDzndeCPhgUC-jiJFihS6VNK9AF_jpHb4wIZz5oT4vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">؛‌OpenAI⁩ مدل جدید ‌GPT-Live-1⁩ رو معرفی کرده که مکالمات صوتی با هوش مصنوعی رو به سطح جدیدی می‌بره!
🎙️
‏این مدل میتونه تغییر لحن بده، بخنده و حتی وقتی که کاربر ناگهان حرفش رو قطع می‌کنه، طبیعی‌تر واکنش نشون بده
🗣️
‏و اما یه قابلیت خیلی جالب دیگه: میتونه به صورت آنی به حرف‌های کاربر واکنش نشون بده و حتی به عنوان مترجم همزمان کار کنه!
🌎
‏همین حالا از طریق ‌
ChatGPT Voice⁩
قابل دسترسه!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6809" target="_blank">📅 08:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎯
RankGrow | دستیار هوش مصنوعی برای سئو
ابزاری هوشمند که با اتصال به Google Search Console، مشکلات سئوی سایت را شناسایی کرده و لیستی از مهم‌ترین کارهایی که باید انجام دهید را ارائه می‌دهد.
🚀
⚡
ویژگی‌ها:
📊
اتصال مستقیم به Google Search Console
🤖
۷ دستیار تخصصی هوش مصنوعی برای سئو
📝
پیشنهاد بهبود محتوا، لینک‌سازی و سئوی فنی
🎯
لیست اولویت‌بندی‌شده از کارهای ضروری SEO
📈
تحلیل رقبا و کشف فرصت‌های رشد
🎁
۵ اعتبار رایگان برای شروع (بدون نیاز به کارت بانکی)
🔗
https://rankgrow.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6808" target="_blank">📅 07:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کد نویسی رایگان با ابزار هوش مصنوعی FREEBUFF
💻
ابتدا به
سایت
بروید و اکانت بسازید سپس ابزار را اجرا کنید
🚀
— نصب آسان با دستور npm install -g freebuff
🛠️
— بدون نیاز به کلید، کارت یا اشتراک ماهانه
🆓
— مدل‌های پیشرفته از جمله DeepSeek V4 pro و Mimo 2.5 pro و Minimax M3
🧠
— دارای یک وب سایت برای تولید و استقرار برنامه‌ها به صورت رایگان
🌐
کد نویسی خود را با هوش مصنوعی و به صورت رایگان انجام دهید!
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6807" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6806">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎉
Claude Opus 4.8 رایگان در
Supercode (فقط یک روز)
به مناسبت لانچ Supercode در Product Hunt، این ابزار دسترسی رایگان یک‌روزه به مدل Claude Opus 4.8 را برای همه کاربران فراهم کرده است.
🚀
⚡
جزئیات:
🆓
دسترسی رایگان به Claude Opus 4.8 برای یک روز
🤖
استفاده از AI Agent در ترمینال
💻
مناسب برای کدنویسی، توسعه و مدیریت پروژه‌ها
📈
؛Supercode
تاکنون به بیش از ۹,۵۰۰ دانلود، ۸۲ ستاره GitHub و ۲۲۰ کاربر رسیده است.
اگر قصد دارید Supercode را امتحان کنید، امروز بهترین فرصت است.
🔗
https://supercode.sh
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6806" target="_blank">📅 02:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6798" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اقا سرعتی slipnet رو اپدیت کنید
😁
😁</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6797" target="_blank">📅 00:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎬
FreeCut | تدوین ویدیو با هوش مصنوعی
یک ابزار متن‌باز که با کمک مدل‌های هوش مصنوعی، ویدیوهای خام را به‌صورت خودکار تدوین می‌کند؛ بدون نیاز به API پولی.
🚀
⚡
ویژگی‌ها:
✂️
حذف مکث‌ها، تپق‌ها و بخش‌های اضافی
🎨
اصلاح رنگ خودکار و افزودن زیرنویس
🎥
ساخت انیمیشن و افکت‌های تصویری
🧠
پشتیبانی از Whisper محلی (بدون API Key)
💻
سازگار با Claude Code، Codex و سایر AI Agentها
🔗
https://github.com/Moh4696/freecut
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6796" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6795" target="_blank">📅 23:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromlocalhost(Yousef Taheri)</strong></div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6794" target="_blank">📅 23:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9TgrL-DzicqZQW9_0NKgGXDgYSzeFy35CXyXtUtNrFmnXkjoNcsZ4YppRr2hDy4A5zi4ZH0xh5VrcuurwiZbm6pmTG9-ukA94bUZKmmTYtwhpTHTIe6FRk448kBanxteXyve5IXLwKI2PxJ070CTMFWH58cUVq1yjyBEZe97XgeEdX0KB2E_SqNV3U24dVx8McpnwzE9vOizDakIJFn0l_vdRIX-2HviJyu6eRLpUJtQNVYYweuQ8ADL77j3Pg3eftigpMlKB_g0HTQTxniEUH09DRPkGzPOyFAZgT0OSNpJbzE9NchfoJnJjhxytBshCyZvKFzs49Yk2KoOeFy1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Grok 4.5 منتشر شد
⚡️
این نسخه محصولی ویژه از ایلان ماسک است که به‌طور خاص برای برنامه‌نویسی و توسعه‌ی ربات‌ها طراحی شده است.
نکات مهم:
• این مدل به طور مشترک با شرکت Cursor توسعه داده شده و با استفاده از داده‌های واقعی میلیون‌ها برنامه‌نویس آموزش داده شده است.
• سرعت بسیار بالا: 80 توکن در ثانیه.
• قیمت بسیار مناسب: 4 برابر ارزان‌تر از Opus 4.8.
در حال حاضر، به صورت
رایگان
در Cursor و Grok Build در دسترس است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6793" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#اختصاصی
شبیه‌سازهای پلی‌استیشن
🎮
PS1:
duckstation.org
PS2:
pcsx2.net
PS3:
rpcs3.net
PS4:
shadps4.net
PSP:
ppsspp.org
PSV:
vita3k.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6791" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://878fa338-f275-4bf6-93ea-ef47d8865f59@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6790" target="_blank">📅 19:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=mibfTtNqn0qh939tIfziUnmhk4LP6vygDXHAU-O6WcD5EkidOFdCJ9-ZxtOYNZcvbU6JyUnMpnHmoAZuyDSopCajjms6B26bISNzL7V9q4pDGitu_OlEai2xyvr7pmMJ7P5L1WUMwfJvlXezBELBzEh4G4b-VSQ3XAXTlXf_KTZm5RYKB2VCloQqJUDXG_HpRHG0Fz1CTwQglzsiXa3KlSmnh77d2RwbWXLdbNNK-Q22TzbnFa3XysTKdXni5dgB6MzXttYQFvJ2Oet5k5m4MN8QQ2BKYr_iuim0S-pS86SchaPkr8hmPoK1j--XAClM_wmEq34kmB8sg4SEUDMgmQTPgC1mVXSc7WjaGJ7tzwcbsq_qeM27uJrO5CW3Et1QsV-De_E0oMmTF4bTEhyWiib74rlcR_MF0sfnD4iqJMJJkURJg8WS_Ejs_IWA5g-2SEjOlFzsv2vI4x0xwni7Tep895J_Zx_tnfOM2iDLlHh2GdDpiZdWUsVO_2LH5Mbo31fIfuYDFasn57D5AcxnHntX_LSAGCRn-JF3EgILLTF76UyYCpwok3jW9hEZAGzmu--lzmkiSoAVTbyWGrUDG0IGLqDoGYcRGp7MCtHJ422Gt-oCFPDtQ4gp9dC6pu1lMiO-J5KvY79-qggQhDs_H5RZdTkdbET_-cN0oFRn8yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=mibfTtNqn0qh939tIfziUnmhk4LP6vygDXHAU-O6WcD5EkidOFdCJ9-ZxtOYNZcvbU6JyUnMpnHmoAZuyDSopCajjms6B26bISNzL7V9q4pDGitu_OlEai2xyvr7pmMJ7P5L1WUMwfJvlXezBELBzEh4G4b-VSQ3XAXTlXf_KTZm5RYKB2VCloQqJUDXG_HpRHG0Fz1CTwQglzsiXa3KlSmnh77d2RwbWXLdbNNK-Q22TzbnFa3XysTKdXni5dgB6MzXttYQFvJ2Oet5k5m4MN8QQ2BKYr_iuim0S-pS86SchaPkr8hmPoK1j--XAClM_wmEq34kmB8sg4SEUDMgmQTPgC1mVXSc7WjaGJ7tzwcbsq_qeM27uJrO5CW3Et1QsV-De_E0oMmTF4bTEhyWiib74rlcR_MF0sfnD4iqJMJJkURJg8WS_Ejs_IWA5g-2SEjOlFzsv2vI4x0xwni7Tep895J_Zx_tnfOM2iDLlHh2GdDpiZdWUsVO_2LH5Mbo31fIfuYDFasn57D5AcxnHntX_LSAGCRn-JF3EgILLTF76UyYCpwok3jW9hEZAGzmu--lzmkiSoAVTbyWGrUDG0IGLqDoGYcRGp7MCtHJ422Gt-oCFPDtQ4gp9dC6pu1lMiO-J5KvY79-qggQhDs_H5RZdTkdbET_-cN0oFRn8yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چینی‌ها یک "غول" جدید برای تولید تصاویر معرفی کردند: Seedream 5.0 Pro.
ویژگی‌های این ابزار:
🔹
ویرایش لایه‌ای تصاویر
📦
‏
🔹
ترکیب چندین تصویر در یک طرح کلی
📚
‏
🔹
تنظیمات جداگانه برای سبک هر شیء
🎨
‏
🔹
ویرایش محلی مناطق انتخابی
🔍
‏
🔹
تغییر تصاویر بر اساس دستورات متنی
📝
‏
🔹
تطابق دقیق‌تر خروجی با درخواست
📊
‏
🔹
بهبود عملکرد در کار با متن داخل تصاویر
📚
‏
🔹
تولید اینفوگرافیک، نمودارها و سایر مواد بصری
📊
‏
نسخه ‌Lite⁩ رایگان در ‌
Higgsfield⁩
و ‌
Dreamina⁩
قابل آزمایشه
📦
👀
‏نسخه ‌Pro⁩ از طریق ‌API⁩ در دسترسه
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6788" target="_blank">📅 19:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plLUtIL5cN2KRRVuGgD3o64LKN-ZELN1frkGqMCw2cw5aRLqDsHO_U0KW1RiE4m225pgvCHHOKFGKV6iSM4TGpsVZoIGsZZ-xXPgsB2EaPGteooMts_j6W6rgtizI1cF2z8XCONUbSP7z0bpSrlZO0t7n0BL25oDOPzpxTAT2WXpcMv8qsJ7wG4yG3APkiGRFG_pENKjIlwCcgeHls3ze4GyT5cy16LxqxpCCe7rZXB68VywXb4Z9gob8G1zYMlDThfyPB7cUUmrZ9JzcLeIyliJdD84UDXdg217ipbliGTif07YpknzUgu95iWigpxvNfgOZMzTboo-NY-ETHX7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرورگر
DuckDuckGo
در جدیدترین به‌روزرسانی خود قابلیتی اضافه کرده که امکان
حذف تبلیغات ویدیوهای یوتیوب
را فراهم می‌کند
🌐
این ویژگی با استفاده از فیلترهای
uBlock Origin
کار می‌کند. هرچند ممکن است در برخی مواقع
زمان بارگذاری
یا
بافر شدن
ویدیوها کمی بیشتر شود، اما در عوض می‌تواند تجربه‌ای بدون
تبلیغات
و روان‌تر هنگام تماشای ویدیوهای یوتیوب ارائه د
هد
😎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6787" target="_blank">📅 18:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
Recordly | ضبط و ویرایش حرفه‌ای صفحه‌نمایش
✨
یک نرم‌افزار متن‌باز برای ضبط صفحه نمایش که ابزارهای ویرایش را هم در خودش دارد؛ مناسب ساخت ویدیوهای آموزشی، دمو و معرفی محصول.
🚀
⚡
ویژگی‌ها:
🎬
ضبط صفحه، پنجره و صدا
🖱️
زوم خودکار، افکت‌های موس و حباب وب‌کم
✂️
تایم‌لاین ویرایش، برش و افزودن متن
📤
خروجی MP4 و GIF
💻
پشتیبانی از ویندوز، لینوکس و macOS
🔗
https://github.com/webadderallorg/Recordly
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6786" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🛡
Dangerzone | تبدیل فایل‌های خطرناک به PDF امن
یک ابزار متن‌باز برای باز کردن امن فایل‌های مشکوک مثل PDF، فایل‌های آفیس و تصاویر؛ بدون نیاز به اعتماد به فایل اصلی.
🛡
⚡️
نحوه کار:
🗂
فایل داخل یک محیط ایزوله (Sandbox) پردازش می‌شود
🖼
محتوا به پیکسل تبدیل شده و دوباره به PDF جدید ساخته می‌شود
🚫
کدهای مخفی و عناصر فعال فایل اصلی حذف می‌شوند
✨
پشتیبانی از:
📄
PDF
📝
Word / Excel / PowerPoint
🖼
فرمت‌های تصویری مختلف
💻
قابل استفاده در:
Windows | macOS | Linux
📎
https://github.com/freedomofpress/dangerzone
🐍
زبان: Python
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6785" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYwi4bx5xKPD0A3FeDqp3e_Qotfbs-09045hUF_plRhzV59eKWz3WSZKNNI9v2zz_j5xFTumqSDKWjA9kB0_tH_ksOqGUglfBd_SjX2cvFOLN50F3DPgWCAoHo5-Y7bGcp-vzmQOMBwdZqfFXspheXE-V9SlZWXBnZb4kDLrtH1WP9rLrV4VCe9sy9UCxRI1e9yUIipV1lURtnVLFGrj_5vi__FsexdRA1k9yfb7CiA66sqA9ZK-shNj8_wuqlqqExfuoogzi15lcip5LNIHez1MESHwXvXf7-a1-T1aG7eqfCLAQN1BYfWKlbZVjskozbGb0Q1uLy3w0N4691cobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SubFarsiPro v5.0
📹
این ابزار، یک دستیار حرفه‌ای، پرسرعت و متن‌باز برای استخراج زیرنویس از ویدیوها و ترجمه دقیق اون‌ها به زبان فارسی (با لحن طبیعی و محاوره‌ای) هست
GitHub
🐱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6783" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">📊
دنبال معتبرترین رتبه‌بندی مدل‌های هوش مصنوعی هستی؟
اگر می‌خواهی عملکرد واقعی مدل‌های هوش مصنوعی را مقایسه کنی، این دو سایت را از دست نده:
🌐
Artificial Analysis
📈
یکی از کامل‌ترین لیدربوردها برای مقایسه مدل‌ها از نظر کیفیت، سرعت، هزینه، کدنویسی و ده‌ها بنچمارک معتبر.
🔗
https://artificialanalysis.ai
💻
DeepSWE
🧑‍💻
یکی از بهترین بنچمارک‌ها برای سنجش توانایی برنامه‌نویسی مدل‌ها با استفاده از پروژه‌های واقعی و جدید، نه سؤالات قدیمی و حفظ‌شده.
🔗
https://deepswe.datacurve.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6782" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6780" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارسالی یکی از یوزرای گل
👇</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6779" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6778" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔥
دسترسی رایگان به هوش مصنوعی قدرتمند Fable 5
اگر دنبال تست مدل‌های پیشرفته هوش مصنوعی برای
برنامه‌نویسی، تحلیل و کارهای پیچیده
هستید، این روش می‌تواند جالب باشد.
🌐
پلتفرم
Tasklet.ai
امکان استفاده محدود رایگان از این مدل را فراهم کرده:
✅
۵۶۰۰ کردیت ماهانه
✅
۳۰۰ کردیت روزانه
✅
مناسب برای تست و استفاده‌های روزمره
📌
روش استفاده:
1️⃣
با ایمیل ثبت‌نام کنید
2️⃣
وارد پنل شوید
3️⃣
از بخش انتخاب مدل،
Fable 5
را انتخاب کنید
هر بار کردیتتون تموم شد میتونید اکانت جدید بزنید
🤝🏻
لینک
🔗
:
Tasklet.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6777" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🗂
نام‌گذاری هوشمند فایل‌ها با هوش مصنوعی (
Renamer.ai
)
پایانی برای کابوس فایل‌های بی‌نام‌و‌نشان مثل
Scan_001.pdf
. این ابزار به جای تغییر ساده متنِ اسم فایل، محتوای متنی و تصویری داخل آن را آنالیز کرده و نام‌های دقیق و جستجوپذیر پیشنهاد می‌دهد.
🔥
ویژگی‌های مهم:
*
🧠
درک محتوای فایل:
استخراج فاکتورها، تاریخ‌ها، نام شرکت‌ها و موضوعات داخل اسناد، تصاویر، اکسل و PDF به کمک فناوری OCR.
*
📸
سیستم پیش‌نمایش:
امکان بررسی و تایید اسامی پیشنهادی قبل از اعمال نهایی روی سیستم برای جلوگیری از خطا.
*
📂
پوشه جادویی (Magic Folders):
مانیتور خودکار پوشه‌های انتخابی (مثل Downloads) و نام‌گذاری آنی و اتوماتیک فایل‌های جدید.
*
⚠️
نکته:
نسخه رایگان محدود به ۲۵ فایل در ماه است. همچنین به دلیل پردازش ابری، بهتر است برای اسناد فوق‌محرمانه و اطلاعات حساس مالی استفاده نشود.
🔗
لینک وب‌سایت ابزار
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6776" target="_blank">📅 12:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌐
وب‌گردی و انجام خودکار کارها با هوش مصنوعی (Browser Use)
یک فریم‌ورک اوپن‌سورس (پایتون) که مرورگر شما رو در اختیار مدل‌های هوش مصنوعی (مثل GPT و Claude) قرار میده تا کارهای اینترنتی رو دقیقاً مثل یک انسان براتون انجام بدن.
🔥
ویژگی‌های مهم:
🤖
اجرای خودکار وظایف:
کافیه با زبان طبیعی بهش دستور بدید (مثلاً "این فرم استخدام رو با اطلاعات رزومه من پر کن" یا "این لیست رو به سبد خریدم اضافه کن").
🧠
پشتیبانی از انواع LLMها:
کاملاً سازگار با مدل‌های معروف و حتی مدل‌های آفلاین/لوکال.
💻
ابزار CLI حرفه‌ای:
قابلیت اتصال مستقیم و راحت به ایجنت‌های کدنویسی.
⚡️
جایگزین مدرن:
بدون نیاز به درگیری با ابزارهای قدیمی مثل سلنیوم، خودش با المان‌های سایت تعامل می‌کنه.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6775" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRUEhqQoVslrFumnN62JAcOw7xemjomi8woTQ42NbnZl-KvTB6aNqpKw-vZWS0cKXj1qUFPIftOG8sHRhGQlq1xXVOk52uHYuXOdscYaVkEHxhbimoFZEDjiYjZC9ptddEqkDXnWUITtAsD_x_d8sOZt2rKltcQYEqZYts4PvSR1Ch6As93LbkUnV96aR_cRw30wTnNFAP1XzUy3jrq3Kuoa_TdSV5MEgvucevlQiZUzFlgj08t75PPXYjYx2S1kAOtLfZbVuOVgq46SXbHbLrVZAWsiST4ll9Iq3FAZ91cYzux7kq1T653fwx43PgwMymOEa9_uHxt36gbQ4mFY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
معرفی Google Flow
این سایت جدیدی نیست ولی خب بعضی دوستان دیدم نمیشناسنش گفتم معرفیش کنم
😁
اگه دنبال یه ابزار رایگان و قدرتمند برای ساخت تصویر با هوش مصنوعی هستی،
Google Flow
یکی از بهترین گزینه‌هاست.
ویژگی‌ها:
✨
تولید تصاویر با مدل‌های
NanoBanana 2
و
NanoBanana Pro
🖼️
ویرایش تصاویر (چه ساخته‌شده و چه آپلودی) با پرامپت
🪙
ساخت تصویر با
۰ سکه
(رایگان)
📚
امکان ساخت همزمان چند تصویر و ادامه ویرایش روی بهترین نتیجه
🎥
قابلیت تولید ویدیو (با محدودیت بیشتر)
📌
لینک:
https://labs.google/fx/tools/flow
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6774" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6773">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiTHIv2XlfCFDduJJg0uZ6-6KUfItOOcckH9RNdoO6y8CRXXHP8FXdWGR-Z_c_K0XuUTq8B9zIoj7cxhV0LCw_KKRLX3-jsRkE5HlGTvAz3HDPZmH86BiQYY6vRfcA6rjh3uIMLkbujAmrj4M414i9IfQa-RfN53QLax3m5EedB6Pt0foGu_tK8jDXs7oU2qhb_962B1tZbrEz0MB0yF1GROyiu5UnZCFvccOKEaOfVK5s5OtVXVjpFJj27AuPMu3B6s2Q9GPXsRL3KaRkpAMHguFo-N86a5jKyYOVMJNMRnLL6mjakUgB2xNIPBKMzHs8oMENbY2oMUfUqhU_LA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
WLLPR | ژنراتور والپیپرهای مینیمال
اگه از والپیپرهای تکراری خسته شدی، با
WLLPR
می‌تونی توی چند ثانیه والپیپرهای مینیمال و جذاب بسازی؛ اونم دقیقاً با رنگ و استایلی که دوست داری.
🎨
⚡
ویژگی‌ها:
• ساخت والپیپر برای
📱
موبایل و
🖥
دسکتاپ (4K)
• انتخاب رنگ، طرح و استایل دلخواه
• تولید نامحدود والپیپر با یک کلیک
• هماهنگ شدن رنگ رابط کاربری گوشی با والپیپر در بسیاری از گوشی‌های اندرویدی
🌐
لینک سایت:
https://bypedroneres.github.io/ai/
➖
➖
➖
➖
➖
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6773" target="_blank">📅 10:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6772">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGAyaC0ceYsyhoIeS3HAEknfLonEyJH5HO5mLlTnnPaiyfEqF_Zadxj88RBxsBUce3nBsiPlBC4RJDAnrmv4y3pgzhpKZZX70U049FG7NSLicx_g7IPf9lMvlpxFp5QplmpRPMKPOklyWqFQtVDq_oHC44uE94uaXqJSIYvT8-GWaVVbuKwMqzJ7jJhhHHYKbf3jGtVfFRSKMi98E-vvIUC1OYp9B5IUzW79ebUb4RlFmkWW1fEUWiMLly1qRDU1SMBh5LKb8kvfjtbsHhHSIivj7Iq2ORDng2wVXGiCW-vyGgPFWzyJqthFTBJl-8KLSDMiTITa6xsdaYReGJogSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت OpenAI
نسخه‌ی GPT-5.6 را برای Sol، Terra و Luna از فردا راه‌اندازی می‌کند!
🚀
دسترسی زودهنگام از همین حالا برای کاربران در سراسر جهان فراهم شده، می‌توانید با خیال راحت وارد شوید و آن را بررسی کنید.
🌍
🔍
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6772" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrZJ9y7IUFEqDARed5kBXYCGYebqI7BlEioSUU8i643nl9jxLLQITiw4Pwx2sQ7pTgl3my5lkO1Liyc-OHHo80xvuvW8m7XVWVAzCmlz9nZwuMi-2owKKPeDgeiT_Qbsjv5bk6A72Zi9ObM5ZbjO0uFMjBn5m8uk9VhJSwqOmxxjLI4OeOFL_D5leJORm-jNeTqr4tXFqx4qpxBj7_NEvhzgTzTmlSNhr69lZeg6jNmebIoLtvW9sLoGe6K5jlaeXGd6ZDl-1PQwUoBTt3f9vcS6SlOKkeESWdSWUIiNV7uTbtBxuhqx9wh-WOv71SCXFByR9cgXOBw60MXqtUQYow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Constrict ناجی شما در فشرده‌سازی ویدیو!
📹
- ویدیو را آپلود کنید و اندازه مورد نظر را انتخاب کنید.
- بدون نیاز به سرویس‌های آنلاین و دستکاری‌های پیچیده در کدگذاری.
ساده، سریع و کاربردی!
https://github.com/Wartybix/Constrict
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6771" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dui24MKA2SgW_qcKAzcdiDIUb0RT9vsw4syZxUYudhVj219gJJ9fAFydnGV-DhiNuYbddVRsZvzwCx15s9rJZuJHLCfnk04ING1CqDJrBThjLWIL1QQEjMKhmS2_Lk49XLRmbbEH4ZI-B2LlZBHhFozsRSM9mzeHZf1N6wopyNc8qimEKp6VmLt4wbX3Q2uXv01uadotXxDAne68pDVL7JjJw2kY0JBz5FUMqz6rv03uct32ldANflikZ6i-cON4KQjHZTZTbHSjWLp_PcHl7N9v11ycKLky_AQDFK67iuwMfwDdSr4yHjfnqamps7Azhw-JsqCCuCtAFVM00cY_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تحلیل ویدیوهای یوتیوب، تیک‌تاک و فایل‌های محلی با هوش مصنوعی
؛
Claude Video
یک ابزار متن‌باز است که امکان تحلیل ویدیوها را برای دستیارهای هوش مصنوعی فراهم می‌کند. کافی است لینک یک ویدیو یا فایل محلی را به آن بدهید تا فریم‌های تصویر و متن گفتار را استخراج کرده و در اختیار مدل قرار دهد؛ سپس می‌توانید درباره محتوای ویدیو سؤال بپرسید یا خلاصه آن را دریافت کنید.
⚡️
ویژگی‌های کلیدی:
-
🎬
پشتیبانی از ویدیوهای
YouTube، TikTok، X، Instagram، Loom
و صدها وب‌سایت دیگر
-
📂
تحلیل فایل‌های محلی مانند
MP4، MOV، MKV
و
WebM
-
🖼
استخراج خودکار فریم‌های مهم و متن گفتار (Transcript)
-
🧠
امکان پرسش درباره بخش‌های خاص ویدیو، خلاصه‌سازی و تحلیل محتوای تصویری
-
🤖
سازگار با
Claude Code، Claude Web، Codex
و ابزارهای مشابه
-
🔓
متن‌باز با
لایسنس MIT
🔗
گیت‌هاب پروژه:
https://github.com/bradautomates/claude-video
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6770" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#Android
#Gaming
🎮
MuMuPlayer 6.0 منتشر شد
نسخه جدید شبیه‌ساز اندروید MuMuPlayer با تمرکز بر عملکرد بهتر و سازگاری بیشتر برای اجرای بازی‌های اندرویدی عرضه شد.
ویژگی‌های جدید:
•
🤖
پشتیبانی هم‌زمان از Android 12 و Android 15
•
🚀
عملکرد روان‌تر و FPS بالاتر
•
🖥
بهبود اجرای چندین Instance
•
🎯
سازگاری بیشتر با بازی‌های جدید
•
⚡
ارتقا بدون از دست رفتن تنظیمات و Macroها
مناسب برای اجرای بازی‌هایی مانند Roblox، استفاده از چند حساب کاربری و تست برنامه‌ها روی نسخه‌های مختلف اندروید.
🔗
https://www.mumuplayer.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6769" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2Xf3K2mWtJFmF2BFCTcB8YIhcTdyuRR7jmTIwtsMC3rnkemvQs_wk5qf2topDc87dTfjQ53QknXRRCKktFg9B-6dMxJ4lGVx-WZIMEIMR1a5WCm_ltbLecDihEruKeOC3WRaEsLWu-bdRiX4tfZZcQoE_4_tQheLe6YeH5l2r5O5GazGE5UJTngylvprmgkuBVWQcsQ7AYWqS_rJDf2_pEcz_zokJDi1slvFdPzRXayRfDS_OJZaU5qnXh7-X9ZtdE4N4mWwI8-OEVy0SlGsSZnD47s8IUtrzz9YhRuZiCcH0qbwP9arNOndifIMmm73hK-ZH_0loL5JzN67XzQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
یادگیری شخصی با هوش مصنوعی
موضوع رو بهش بده؛ بر اساس سطح و درک شما آموزش می‌سازه.
✅
آموزش مرحله‌به‌مرحله
✅
امکان پرسیدن سؤال حین آموزش
✅
مناسب هر سطحی
🔗
https://peras.app/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6768" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
🎁
100 هزار توکن رایگان ( 3 روزه )
‏دسترسی به مدل‌های زیر و صدها مدل دیگر برای کدنویسی :
🔹
‌GLM-5.2⁩
🔹
‌Qwythos⁩
🔹
‌Deepseek 4 pro⁩
🔹
‌Kimi k2.7⁩
🔹
‌Minimax M3⁩
🔹
‌Mimo 2.5⁩
‏
💡
ویژگی خاص:
امکان استفاده از مدل‌های ترکیبی ساخته‌شده توسط کاربران (مثل ترکیب ‌Qwen + Fable)⁩
🔗
‌featherless.ai
⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6767" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvjApec1jW9Qi6KDdOfvC9jdv-Pp1EgkCDJ4FhhyEXpAW68mYP2emozLmIErw2hboBat9r7ajNjGC7_PmelMuEDZBA_mYVeZfAeJFaGZCcrwO-1keDtrjg8R6UlGsIxwaAPyY-EpUxr_2bo0qftvyGj9qKOU8bwlHvFfyiGTpDbwYKe3WlP9kEqD4BLjHrr8gVU9snvJfOqb-kQSjepSoyCm8CB-gcFIOdKHn8QA4ezxVCmfzIUaMOeQgK0oNu5oTlhWSyWx31568XpI2aMwSpAOAs8rX3F97__7e-l-Y4eJVWnwqtGrVtkJEPSlMECPJi5UNzTM_RMwZyrtNhDCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
PixelRAG
یک پروژه متن‌باز برای Visual RAG که به‌جای متن، اسناد، صفحات وب و PDFها را به اسکرین‌شات تبدیل می‌کند و جستجو را بر اساس محتوای بصری انجام می‌دهد؛ بنابراین جدول‌ها، نمودارها و چیدمان صفحه حفظ می‌شوند.
ویژگی‌ها:
•
🖼
جستجوی مبتنی بر تصویر صفحات
•
📄
پشتیبانی از وب، PDF و تصاویر
•
🤖
سازگار با مدل‌های چندوجهی (Vision)
•
⚡
ابزار CLI برای ساخت و جستجوی ایندکس
•
🌍
API و نسخه دمو آماده استفاده
🔗
https://github.com/StarTrail-org/PixelRAG
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6765" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔐
VoidAuth
یک سرویس متن‌باز برای
SSO
و مدیریت کاربران در محیط‌های Self-Hosted.
ویژگی‌ها:
•
🌐
OIDC Provider
•
📖
LDAP Server
•
👥
مدیریت کاربران و گروه‌ها
•
🔑
MFA
و
Passkeys
•
📨
دعوت و ثبت‌نام کاربران
•
🎨
شخصی‌سازی رابط کاربری
•
🔒
رمزنگاری داده‌ها (
PostgreSQL
/
SQLite
)
⚠️
هنوز Audit امنیتی نشده؛ برای Production با بررسی کافی استفاده کنید.
🔗
https://github.com/voidauth/voidauth
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6764" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🖼
جستجوی معکوس تصویر با TinEye
اگر می‌خواهید منبع اصلی یک تصویر را پیدا کنید، نسخه‌های باکیفیت‌تر آن را ببینید یا وب‌سایت‌هایی که از آن استفاده کرده‌اند را پیدا کنید،
TinEye
یکی از بهترین موتورهای جستجوی معکوس تصویر است.
⚡️
قابلیت‌ها:
-
🔍
جستجو با آپلود تصویر یا وارد کردن لینک آن
-
🌐
پیدا کردن صفحات وبی که تصویر در آن‌ها منتشر شده است
-
🖼
شناسایی نسخه‌های ویرایش‌شده، برش‌خورده یا تغییر اندازه‌یافته
-
📈
مرتب‌سازی نتایج بر اساس اولین انتشار، جدیدترین، بزرگ‌ترین یا بیشترین تغییر
-
🔒
حفظ حریم خصوصی؛ تصاویر آپلودشده ذخیره یا ایندکس نمی‌شوند. TTinEye+1
🔗
وب‌سایت:
https://tineye.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6763" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6762">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li9oTptI2xj2lLBkuSdDGcWeJLGYOOJ62aAaMIqvQ3aQ53RYCXolQu2JbPqIZySjV1GBqjxPsc2c-flNr1JHUaE0AIGevVySZkvMpu6jLqvp5nXo529iJuPWPbEovleZToTT9k4PFEYuESQ-xa8LEUHLuSLUNeaq1CdhorCXTt3-ob1nu7e0fZEAzhhKliZ8uBhEZ4wQ1jNtf0fH0Wpg6Sgm8qH9Cq3Q_3TCyjOp7j6Qe26uNKhJljSow3qCGAvjrJAdhKSDcxd2lEXcWEahNBZWrUUzkFe_LSZ016X-Lk6O6DguRMei29mrVUSQX3H8H0VbT2729JaqLb9lIqwgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تولید صدا با Pocket TTS روی پردازنده معمولی (CPU)
این ابزار یک مدل
تبدیل متن به گفتار (TTS)
بسیار سبک با
۱۰۰ میلیون پارامتر
است که بدون نیاز به
GPU
، پرداخت هزینه
API
یا وابستگی به سرویس‌های ابری اجرا می‌شود.
⚡️
ویژگی‌های کلیدی:
-
🚀
تولید اولین بخش صدا در حدود
۲۰۰ میلی‌ثانیه
و تا
۶ برابر سریع‌تر از زمان واقعی
روی پردازنده‌های مک.
-
🎙
امکان
شبیه‌سازی صدا (Voice Cloning)
تنها با یک نمونه صدای
۵ ثانیه‌ای
.
-
🌍
پشتیبانی پیش‌فرض از
۶ زبان
: انگلیسی، فرانسوی، آلمانی، پرتغالی، ایتالیایی و اسپانیایی.
-
🔓
کاملاً
متن‌باز (Open Source)
با
لایسنس MIT
و آموزش‌دیده فقط با داده‌های عمومی.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6762" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucfoZv9BqHUcjSdblQOAeh7j0nlW5PEvw5pxaRq9DyMqLnUpqInca36lHspwMSPn1w3wahUEjLzV0QrlimbHu6NVKVObX_zWCR7882rnXMPrqBTfd_ynzTDL9vVvpw4ToWLKYfqGVNrhpJLBikskSIoQDL55WIJoZzwUQ04ZPXaxUN-h9ghB2ZvUUwIIQDN5NQAi3R6V0OBdNE5xNqvqf2tpKIW7V1I3P2QV2RaFzoeAOhO8Ym5GYo_UdObax3k_ZGbwcAA2eE8OfaAKb9V7_cNY1vytu2jd2rWWBEuLJZts_7A2ncq-mIZYxacUnIMLD-alvftuk6Q1vsh6NUmQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به دنیای تکنولوژی، لینوکس، شبکه، سرور و ابزارای خفن علاقه‌مندین، یه سر به کانال لوکال هاست بزنین
توی localhost کلی آموزش، نکته کاربردی و تجربه واقعی از کار با سیستم‌ها هست. خلاصه هر چی از دل پروژه‌ها درمیاد، باهاتون به اشتراک می‌ذاره!
🅰
t.me/localhost_ir</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6761" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGPt4S4PBnuqealFySizBxcyHkrFYxvyG7v68C9ncLoubwxG7SWniqdffgKepnE_x3N4QLc9vk6yB_adNolTk9N9IPBvQvSz9ggcHXKEGUUT6IQDvQrr_PM3THg_W1QpaCf2ojTKzG4m_IuB9mQ__dPiPuWvS1vo0my9LskmhOooT99_vLjGDmSMdziCxbBz8oQni4iNZdVxodbw0kQGxnAKrN4npsJzAuw6ziqylY49jhBlm_H1OQVNowrw_mVLlM55xJnIzU6sO_XI9bE6buvq4Or0CBG2PQTDuW7oUtd18F1BiT9JUhshleNU6ZbIUVZTxevF6rFsHcjdCijz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود و مدیریت فایل‌های تلگرام با TDL
یک ابزار متن‌باز و قدرتمند برای دانلود و مدیریت محتوای تلگرام است که امکاناتی فراتر از یک دانلودر ساده ارائه می‌دهد. این برنامه با مصرف کم منابع، سرعت بالا و قابلیت اجرای مستقل، گزینه‌ای مناسب برای کاربران حرفه‌ای تلگرام محسوب می‌شود.
⚡️
ویژگی‌های کلیدی:
📦
اجرای برنامه به‌صورت تک‌فایل (بدون نیاز به نصب)
-
🚀
مصرف بسیار کم منابع سیستم و استفاده حداکثری از پهنای باند
-
⚡️
سرعت دانلود بالاتر از کلاینت رسمی تلگرام
-
🔒
دانلود فایل‌ها از چت‌های محافظت‌شده (Protected Chats)
-
🔄
فوروارد پیام‌ها با مسیریابی هوشمند و جایگزینی خودکار در صورت خطا
-
⬆️
امکان آپلود فایل به تلگرام
-
📄
خروجی گرفتن از پیام‌ها، اعضا و مشترکین در قالب JSON
-
🌐
متن‌باز با لایسنس AGPL-3.0
🔗
گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6760" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM5BobzCqbL0aqr1g3ItvBDedsIzV_qpFwspjAEFt5fVp5YX5MG7QVDSf5mrrT6CB21QoBuIle9Pu6twRsroCY_gQPXLw1e2fRiV37eaWYdrNszXZ3kZCX2NY_ZZeV3G8elE8mGRlrVzXe4C-o1XKWQJ2EUCAssiLWb5JcvMFHvTv83pP67NDEyyIirOPvuPEzI3bcfKwG0lXL78FBfGB0zlskormIEIP3lP1v7nC1autNGgK7LEKiYvjvTJY0l2tzGgp0M33ioiYNBcFC_hxtpt9fzFe2gBBVHvwU3Wk9C7XDsJS5qFwYHYjmhJNIA51QMiyVUgzDEpX0hTXqZWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهبود کیفیت عکس‌ها تا رزولوشن 4K با استفاده از ChatGPT
عکس شما را بهبود می بخشد و جزئیات را تا حد امکان حفظ میکند.
😮
پرامپت :
Restore and enhance an old damaged photo. Remove scratches, stains, and noise. Reconstruct faded or torn areas while preserving original details. Slightly sharpen the image for better clarity, but keep it realistic. Apply natural and era-appropriate colors to skin, hair, and clothing. Use a soft, balanced background color without being too striking. The final result should look like an old photo that has been realistically restored and colorized, while respecting its original appearance.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6759" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlORv41VlXNxDN1qSc5fnXQaPvdRISlNXp6OnTEhJSCVWhOqkslXaR-qz4lmprzmlzN8-Vmc2VlqiMb0BAQ_brPSzWNYN4_z7ZL2RAvxKEjIz155u8lowL4uJyPkRYCH04jFlrKoXu8RPe5biS5Pl3Pga7w03aRtz-EmDdp4KHr6wyNqXyFFaqA7fP9m_Z1giE_frfoGhrEpEAE_ba6Q9GesbfXjQBl_A-B6sgWbqr-e3CixQWLFx0P4MYEdYJpLp0F1uesgr5a-u1UK8atatctyFq8NwWHk3gCaqTU2LWM7ZHwq_rBtCOVWGz4-8wHs4t8YbyPAerp5y1kSM6THMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اپ‌استور متن‌باز و جایگزین Appteka برای اندروید
یک مارکت رایگان برای دانلود، مدیریت و به اشتراک‌گذاری برنامه‌های اندرویدی که بر پایه مشارکت کاربران (Community-driven) فعالیت می‌کند.
🔥
ویژگی‌های مهم:
*
📦
استخراج APK:
خروجی گرفتن از برنامه‌های نصب‌شده (حتی برنامه‌های سیستمی) بدون نیاز به روت (Root).
*
💾
مدیریت فایل‌ها:
قابلیت بکاپ‌گیری، بازیابی و نصب مستقیم اپلیکیشن‌ها از داخل خود استور.
*
💬
تعامل کاربری:
دارای چت گروهی، سیستم نقد و بررسی، لیست علاقه‌مندی‌ها و دریافت نوتیفیکیشن آپدیت‌ها.
*
🔒
امنیت:
اسکن خودکار برنامه‌های آپلود شده (از آنجا که محتوا توسط کاربران قرار می‌گیرد، بررسی منبع قبل از نصب پیشنهاد می‌شود).
*مناسب برای توسعه‌دهندگانی که می‌خواهند برنامه‌هایشان را راحت منتشر کنند یا کاربرانی که به دنبال یک استور بدون محدودیت و ابزاری برای استخراج APK هستند.*
🔗
[لینک دانلود یا گیت‌هاب پروژه
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6757" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675041278d.mp4?token=MAXmycrKV4Cgl_hUK_C2V0H8Oaz18CsDCev9ylUpsAeIrZ97-kFzEzgrVkU2uV_tcTORLigSRyPvXA8yHOvtpIfd_SMJonWqAVrGEIYZXoFS4mU9KpgLB6RkT10Yw9FBfgjxqLr4qu1_fXcV5obtgDvYxT9xPPvWoV7P2T-zD2LBErWlZuJ79lv_Oppvo5Dt2t-1HRLYPVR_WEAxOes5zSSh5QZKTeE00BESjGX6GMdFcGtCRgalUkNZg_URzBVYXatuYWMiTX6q92H_6TRCqHyrxyPK8yI983Bq4u6Nj1NpLuzBLoc7-ZVxJ9edgLikzVcVmKrkuxdOPTBErt-iWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675041278d.mp4?token=MAXmycrKV4Cgl_hUK_C2V0H8Oaz18CsDCev9ylUpsAeIrZ97-kFzEzgrVkU2uV_tcTORLigSRyPvXA8yHOvtpIfd_SMJonWqAVrGEIYZXoFS4mU9KpgLB6RkT10Yw9FBfgjxqLr4qu1_fXcV5obtgDvYxT9xPPvWoV7P2T-zD2LBErWlZuJ79lv_Oppvo5Dt2t-1HRLYPVR_WEAxOes5zSSh5QZKTeE00BESjGX6GMdFcGtCRgalUkNZg_URzBVYXatuYWMiTX6q92H_6TRCqHyrxyPK8yI983Bq4u6Nj1NpLuzBLoc7-ZVxJ9edgLikzVcVmKrkuxdOPTBErt-iWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6756" target="_blank">📅 10:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">📱
تست خودکار رابط کاربری و اپلیکیشن‌ها با Maestro
یک فریم‌ورک متن‌باز فوق‌العاده برای تست End-to-End (E2E) در اندروید، iOS و وب. با این ابزار نیازی به کدهای پیچیده تست (مثل Appium یا Selenium) ندارید و سناریوها رو خیلی راحت با فرمت ساده و خوانای YAML می‌نویسید.
🔥
ویژگی‌های مهم:
*
📱
کراس‌پلتفرم:
پشتیبانی از برنامه‌های Native، فلاتر و React Native.
*
⚡️
اجرای هوشمند:
بدون نیاز به کامپایل فایل‌ها، همراه با سیستم کنترل تاخیر (Smart Waiting) برای جلوگیری از خطای لود نشدن المان‌ها.
*
🖥
ابزار بصری:
دارای یک محیط رایگان (Maestro Studio) برای ساخت و رکورد تست‌ها به صورت ویژوال و بدون نیاز به ترمینال.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6755" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
۳۰ سایت رایگان ساخت ویدیو با هوش مصنوعی
#اختصاصی
اگر دنبال
Veo 3، Sora 2، Kling
و سایر مدل‌های ساخت ویدیو هستید، این لیست را از دست ندهید.
⭐️
بهترین‌ها
VeoAIFree
→
https://veoaifree.com
(بدون ثبت‌نام و واترمارک)
Vixdo
→
https://vixdo.art
(۱۷۰ اعتبار رایگان + بدون ثبت‌نام)
Pollo AI
→
https://pollo.ai/m/google-veo-3
(چندین مدل در یک پلتفرم)
GlobalGPT
→
https://www.glbgpt.com
(Veo، Sora، Kling و Wan)
Leonardo AI
→
https://leonardo.ai
(اعتبار رایگان هفتگی)
🎁
بدون ثبت‌نام
VeoAIFree • TryVeo3 • AIVideoGenerator • Veo3Free • Videomaker
💰
اعتبار رایگان روزانه
VeoE • EaseMate •
Veo3.us
• AIEase • Aitubo • Pixnova • SeaArt
🧩
پلتفرم‌های چندمدلی
Veo3AI • Pollo AI • GlobalGPT •
Media.io
• Novi AI
🎬
ابزارهای تخصصی
Digen
→ Lip Sync
MindVideo
→ انتخاب نسبت تصویر
DomoAI
→ تبدیل تصویر به ویدیو
Klap
→ تبدیل ویدیوهای بلند به Shorts و Reels
Fal.ai
و
Eachlabs
→ مناسب توسعه‌دهندگان
💾
این پست را ذخیره کنید؛ احتمالاً بخشی از این سرویس‌ها در آینده پولی یا محدود خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6754" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L84wsfLs8z5xpxxoXk7PTBUQ3OInPsHxZUxeTVDGGcZA3_phxp7v4DqlQL7jrUYHyGk1dmlF-0-yXZboXijT6piqPVzu7QibqqYchRFIa3oOZWZZVUFzGlPXMMI2-8xQI1367vkb1la_IjbwyLCHOiAcReVyqvU9ydLiiur9f-1FaJC-B1qp6duovGK0yww5EFAmM-I1mB4h8Fo57Ay0opz_laYFkrZK58Z8p_g8mZD1RRvYnWoCLhouS4grLtF7NxOJM1A3w7Rnn-d6HDkNLIo23pG9kRbbhvJhSGxtq9V9bORJkovh73URN_pJxfpkqeQ19RESYKkZw4dtJg1ycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بقول نیچه
در چنین گفت زرتشت
«من از خردِ خویش به جان آمده‌ام، چون زنبوری که انگبین [عسل] بسیار گرد آورده باشد. نیازمندِ دست‌هایی هستم که به سویم دراز شوند. می‌خواهم ارزانی دارم و بخش کنم...»
بیاین مثه نیچه باشین و این عسل و انگبین چنل رو به سوی دستان دراز بسپارید
نیاز داریم به حمایت شما
❤️‍🔥
https://t.me/ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6752" target="_blank">📅 01:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6751" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor
لینک ویدیو آموزش:
https://youtu.be/pN3LxWzDtKI
خود پروژه:
https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6750" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نیاز داری سورس کد کامل یه سایت (به همراه تمام فایل‌ها، تصاویر و CSS) رو یکجا برای استفاده آفلاین دانلود کنی؟
💾
🕸
ابزار اوپن‌سورس Website-Downloader با استفاده از قدرت wget کل سایت رو میرور (Mirror) می‌کنه و یک فایل فشرده بهت تحویل میده.
🧵
👇
#توسعه_وب
#اوپن_سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6749" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnxqfiPkRz5EY8zjUyCu7AB7FmVJ0aWaPm9SshNE64XUcPYvFkRSjPHQbpuMB20fAeZ8WV2imhzoXO736opS94E2YDrBhHKylfjSHrZEVY5MXIGcobELzlf25rPSEJYZeVfH8iWXYALIwxoCd4U7bPAoONVxUjrox2SDFQaTWwn0-5EfEm0Hu0BdeEPOG1tqIFKaF_OVhfGkJTxaZcbnvpM5-Sg995JBFMeMea_NoQvYI_z0rS4_QHgQUh8FH8B9jKCmtbu-I-Yd1yzK-X-6ypQ56y2lxzwkdg_ON9z6k59XhLoelVXCdxDrqfp4RYgN0OjjbfKYSa5TkNgna9bIjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074191361432035554</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6748" target="_blank">📅 21:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGszY95tlm1N-UGkEP6Ui68tIMvS8EN257fGNPitxv4NV3vR0MJyO7jdx0rrIW3x47EWcXOgx86Wo2PwswcyOEIHfEfknrvngQB2FV6gZfiOJmmMh7zZ9vfZSKVYCWxtJU2qfoyRYzL_5sNBEtUZT8sLLsEfQQ6mgdRfaGyforgQZtzLZHmlTfyJhMn9feykmMJ9vvm6eTEHZmxgQyQEetUt1OjVJbyfQoRj6INloFoVaBIfCa7fCS-Z-F0_boJEmNTxy-JanUZSN467RhP7BPQiVFZlTYo9V5K5QIvsQ3FSkEMmFOOirZ5yN-f3yob96NmHD9Pn8MK49KvaSudzpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🗣️
هوش مصنوعی‌ها دارن با هم «زبان راز» می‌سازن!
🤫
🤖
‏تا حالا فکر کردی اگه ‌AI⁩ها یه زبانی داشته باشن که ما متوجهش نشیم، چی میشه؟
🤔
‏پروژه جدید
‌GLOSSOPETRAE⁩
دقیقاً همین کار رو انجام میده:
🔹
تولید خودکار زبان‌های مصنوعی (از آواشناسی تا دستور زبان)
‏
🔹
ارتباطات غیرقابل‌فهم برای انسان
‏
🔹
کدنویسی خالص با جاوااسکریپت (بدون وابستگی خارجی)
🚫
📦
‏این فقط یه ابزار نیست؛ یه پنجره به دنیای ارتباطات پنهان ماشین‌هاست.
🔍
🧠
‏
🔗
لینک پروژه:
github.com/elder-plinius/GLOSSOPETRAE
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6747" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0NOHd_Pex_o7birzYNRGDhq-OLCHMkWqWzkaV-B4vwHsyjBrtdH-mIduFNTmlh8_RetCzySNOGVtwgGUIOlB7J3aHiU1Fp-Ru7JNXiYZNrWtUFFF7MkYPivmHY2q3UeF-V8tPVB4FYXjXS0ztgqd3-ngO-ELi39NDt0o3FuUK9C2BIYvZzQ2lkUxcASOnKbu8dHyApQW9NUwazPJbZ8ccd2qSu3Ly-O8AXsV_ZG08BlGuo0dfK6QlH2LD7YnPu_RMUGdzRR2EVveMLVDEjU4Q0WqH344Mv5ELwwl7VVXC1ZRToXqjLSWnaF3Vzx7FYQu7szzorMcpmtI55G36pMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆓
دسترسی رایگان به غول‌های هوش مصنوعی!
🤖
‏‌یه گنجینه از ‌API⁩های رایگان روی ‌GitHub⁩
💎
🔹
مدل‌های قدرتمند: ‌Gemini Flash⁩، ‌Qwen3⁩، ‌DeepSeek⁩ و ‌gpt-oss⁩
‏
🔹
سرویس‌های متنوع: ‌Google AI Studio⁩، ‌OpenRouter⁩، ‌Cloudflare⁩ و ‌GitHub Models⁩
‏
🔹
یکپارچه‌سازی آسان: اتصال راحت به ‌Cursor⁩ برای کدنویسی سریع‌تر
🚀
‏فقط یادت باشه محدودیت تعداد درخواست (‌Rate Limit)⁩ رو رعایت کنی تا سرویس‌ها قطع نشن.
⚠️
⏳
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6746" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_K6zfYPqA0pCR5y9al2LX1EjnWYWgIpp1bPl8bbNrjC5BuHoD7u-9ZEBy5_CllIPgAcugipb11znXPsz2jmWnxVQL946DrlUMW4dPmqffUZS6_cAg9pa39eFNpyfNl-WdNgfxpxQjo0WwLorI7E-4dKUmKhY7xVCn5yqzfzOyFQQWtj9r_xZfKLsmWULAl4BUkuVuvvXLCcIMyIuEINW-8XjbGafyxX31vnNNFLMI3ecrvih7OVI_49vteDBQGgOGv02CLWTTI99j3MT72aVMwiqE4N-qKeEFWgquZRwNiG0OZWjMPL-q8S6CF2TSj05zkOdAf1QQr6Fe4RwSZZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
حذف پس‌زمینه با یک کلیک!
🖱️
‏این ابزار وب پس‌زمینه عکس‌ها رو با دقت بالا جدا می‌کنه و کیفیت اصلی رو حفظ می‌کنه.
✅
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=Q0OquxlrFP3_qNTYQlDiEV0ieMwLVsw2Fi5bNQ3BOKhJXsS4z1CihFyYRRyLar0mTWV1f-aQ-2L0o5CpzMPsuIMU9oSD6XyUCI0kpxOBScpe-yG-JNumeunGQdxMvdSlqHvl55rh6IIur0XWiWwSM50HfenyyU_5-G5pAyIN7m3_MUxRXhWzXpL8Zqzt7d9bw6Px-2J_cm1IuAnK-d7Ml3aHLXudHTc3EXyCTGZyJ2vzIJHSWarwBelL6ImF8zWpVqhsKp2uuuySS_ckzvINNb0nOiZGTdYWGLKO2vsSb-aTzGfOBNBOEOYvzbChyZfeyox7MVwxO1FdmaPC7lfv3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=Q0OquxlrFP3_qNTYQlDiEV0ieMwLVsw2Fi5bNQ3BOKhJXsS4z1CihFyYRRyLar0mTWV1f-aQ-2L0o5CpzMPsuIMU9oSD6XyUCI0kpxOBScpe-yG-JNumeunGQdxMvdSlqHvl55rh6IIur0XWiWwSM50HfenyyU_5-G5pAyIN7m3_MUxRXhWzXpL8Zqzt7d9bw6Px-2J_cm1IuAnK-d7Ml3aHLXudHTc3EXyCTGZyJ2vzIJHSWarwBelL6ImF8zWpVqhsKp2uuuySS_ckzvINNb0nOiZGTdYWGLKO2vsSb-aTzGfOBNBOEOYvzbChyZfeyox7MVwxO1FdmaPC7lfv3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
کالکشن ۱۷۰ ابزار کاربردی و متن‌باز
تمام این ابزارها تحت وب هستند و نیازی به دانلود فایل یا ساخت اکانت ندارند:
🎬
مدیا: ویرایش حرفه‌ای ویدیو و صدا
🖼
تصویر: فشرده‌سازی، تغییر سایز و افکت
🔄
مبدل‌ها: تغییر سریع فرمت فایل‌ها
📄
اسناد: ادغام، جداسازی و ویرایش PDF
📰
داده: پارسرها و پنل‌های مانیتورینگ
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWG-9tnwhKqV-IV2Pshu1Vm8OEEbWwGeRN4H66n86_2gkClmkXcWMSy8FOxNpD0wWMSfEgN7mdUvPAUPv-zL37ngchckyM-Au2GaaiSKUNzt40zdn4Kv3Mdzko_fHY287kOrUons1XxU7VNvKyaDrFw3Ox7wiYsov8I-tY-ssrSTuJiCAGk1RmCliU-WIA5yLJK6ZjYiOuSGzoGs0SOA0kDG9s0UMiWZjmBgKAK_pk70AuU_mzWnRkvR1FWoBb071HmrfiEevFdz3MnLrU_WIBK86wP4aagjNThyxMbKweAbCy1wMaQkOCEgO0MBB7L5COl7CC7tt8H2Xv8M5hvBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهکارهای اتصال پایدار و پرسرعت برای اینترنت آزاد
🔹
پشتیبانی از V2RayNG، WireGuard، SlipNet و ArgoVPN
🔹
ارائه اشتراک‌های عادی و گیمینگ متناسب با نیاز کاربران
🔹
انتشار کانفیگ‌های رایگان، آموزش و پشتیبانی
🔹
تست کیفیت اتصال قبل از استفاده
📢
TirexNet؛ همراه شما برای دسترسی بهتر به اینترنت
🤖
Bot:
@TirexNetBot
💬
Support:
@HRMP1386</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
🚀
دسترسی رایگان به غول‌های هوش مصنوعی!
‏اگر دنبال جایگزینی برای ‌Agent Router⁩ هستید،
سایت ‌
Bluesminds⁩
فوق‌العاده است. با ثبت‌نام، 100 دلار اعتبار اولیه هدیه بگیرید و با مدل‌های قدرتمندی مثل:
🔹
‌GLM 5.2
🔹
‌Qwen 3.6
🔹
‌Minimax M2.7⁩
🔹
‌Mimo 2.5
‏کار کنید. همین حالا امتحانش کنید و پروژه‌هاتون رو به سطح جدیدی ببرید!
✨
🔗
Docs
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6740" target="_blank">📅 12:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون فضولی میکنه. یکی میفروشه به دلال های داده (مثه گوگل و مایکروسافت و...) یسریا هم که حریم خصوصی محورن.
الان هرمس اینا رو واقعا نمیدونم. هر چی بیشتر این مدلا رو بیشتر وارد چیزاتون میکنین، ریسکش بالاتر میره در کل. باز این شرکتا اروپایی نظارت بالاتر هست ولی نمیدونم طرف خوشش میاد از ی مدل میگه به به چ مدلی چقد قابلیت بذارم چنل، ملت کلی ویو میزنن استفاده میکنن. طرف به تلگرامش و... هم وصل میکنه بعد اخر بعد چند روز میگه ببخشید هرمس رو شخصی ران نزنید
اینو میخواستم چند روز پیش بذارم ولی گفتم ولش. ولی حس کردم بهتره بگم تا پیشگیری بشه بهرحال</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6739" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kr9ARxfdsJ_CqlmLrf06_cs7KE5E2KJOK0_I--4vABgIvn36mcnCVKL_cgOuIsrWihOiQ1N721axjOunAkY6766yDzNgoOTlXySRanileQBoto0K4kn5rO5JIkwJ6RkmtrMNv1GXa2oFXK998UHC7akMtFGrr0Tyo-yu2LoYgLhsooMp1-ONqsl2nzvYbarlx9CiTc-noBKETAl3gdN7JvhqiJ02LwtCLmlOD-hBfLG5Iq6f-bptXmQgD-igshrmNMDLDP--T6SEf1PiUFvlSBVvB8BdLzHXOZ4ZDFMPerd-iiRMz50wUoH82sAefdTihlIxE7fIhyxY_vCRqu_gzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074039784629014892?s=20</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6738" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePxhS608GvWHgjgvIYds5ytJeVjGiF4slWHTwaleIgdAG662UjRZzX8AXlj8cO5GTs3exYSGav9fKWtB1se9dkKqHtj4H_tozo4vySetVrIfm0tk1D4lKQRkTl6KMBpcegNSbAt1TCe3VcDlEEvKuI6nS7LImH-MabSYhWwWbGTcQ_webPONzFvkcIZIcRPm45i-yPNB5LDoowgcT5kr36HokrOUVszuJPUg3sh4O4Znw7lVeu-6dbOq7rkjJOdOq8y5ZG_nPlW-5nLJxYCrevwYsz53D1PRgpKpofluA3JI2y-cMWuI6758U03q0BtHLiC6aaR0-JY1JCfYfxaJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
اجرای هر بازی اندرویدی مستقیماً روی کامپیوتر
یک شبیه‌ساز رسمی از گوگل که واقعاً سریع است و به راحتی از رقبا پیشی می‌گیرد.
🔹
پشتیبانی کامل از اندروید 14، از همان ابتدا.
🔹
عملکرد از طریق Hyper-V — همه چیز پایدار و سریع است.
🔹
هر فایل APK را بدون هیچ مشکلی اجرا می‌کند.
🔹
بدون هیچ بنری یا تبلیغ مزاحم.
🔹
بازی‌ها بدون هیچ‌گونه کندی یا تأخیر اجرا می‌شوند.
دستورالعمل به زبان فارسی
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6737" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYBl6EgpZzdzLugBKItUHFnW1hKYdmDKr-KHyfdj2qQBvjkOaUw519_tibl3mgX9P_1V-4yqGr6NIr_akIMqSY45Rak2TzT9MYKO43_4C4yZ3-fHzYDGbyF0CgK1LQIdP2lP8zfS3P4gbSvv82scvT-NI71kNPZVk1HklEhrlZ1RPglyvHbgzHWTvWtgX7FEiqgbhEU2d8rqkUMFInHM5_Aw8QOENKwbGnwnUotv-o5JauSUcuZl-g3dGBPlrNJXU0i53prRFfF9JqZgndXndvjtlaDYnmnikjiwnCuR5KvoXY_fLOyHBSEdqTNtxue5EMaNXdG0FXJ9peLims1ftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
کپ‌کات رو فراموش کنید؛ این ابزار رایگان و بدون نیاز به نصب جادو می‌کند!
‏اگر برای ادیت ویدیوهای خود به دنبال یک ابزار سبک، همه‌فن‌حریف و کاملاً رایگان هستید، پروژه متن‌باز ‌OpenReel⁩ دقیقاً همان چیزی است که نیاز دارید. این ادیتور قدرتمند مستقیماً درون مرورگر شما اجرا می‌شود و نیازی به نصب هیچ برنامه‌ای ندارد.
‏
💡
چرا ‌OpenReel⁩ یک جایگزین بی‌نظیر است؟
‏
🔹
ادیت چند لایه حرفه‌ای: قابلیت ویرایش همزمان چندین لایه ویدیو و صدا همراه با پیش‌نمایش زنده و بدون افت سرعت.
‏
🔹
امکانات کامل کپ‌کات: دسترسی به افکت‌های متنوع، ترنزیشن‌ها، پرده سبز (‌Chroma Key)⁩، کنترل سرعت و فریم‌های کلیدی (‌Keyframes)⁩.
‏
🔹
ابزارهای جانبی کاربردی: قابلیت ضبط صفحه نمایش، کار با متن و زیرنویس، و خروجی گرفتن سریع با فرمت‌های ‌MP4⁩ و ‌WebM⁩.
‏
🔹
کاملاً رایگان و امن: بدون نیاز به ثبت‌نام‌های پیچیده، پرداخت درون‌برنامه‌ای یا واترمارک روی ویدیوها.
‏بدون درگیر کردن حافظه سیستم یا گوشی، همین حالا ادیت ویدیوهای خود را در سطح حرفه‌ای شروع کنید!
🔗
Site
|
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6736" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6735">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrT6eMLwNNVbazpUdVTgPHemabJdYdM9h7PqQQtIMjdNgnrj6e_dOh3ZK-s4CFt_YHsYi3sb1B9XiIuQJXE1LNtuucJD9ksqaGsyjclbu8gJChVq9NxFZ8gcti7E8wROUvoUilZb4W2vF-kCoHRL2SFs-EfYm2_7iw__yh-WPTCAy8GLiEhPEZr7NveA4Hv6knHdfXYBeBztkAjNMkePjOvf0D8hY-H7rk2l-p4fMnF91UMvTlAsvQqAfz481GhVBNo3Ra74uPzRxkSWJMQI4eCSx1L_0LPnJmBWnz0a_PNhsD-gAWP3AqYxk1NEA6PHnIRaOnWdjZZooKX6qUNYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تمام غول‌های هوش مصنوعی دنیا، زیر یک سقف!
‏دیگه نیازی نیست برای تولید متن، کد، ویدیو یا عکس، بین ده تا سایت مختلف چرخ بزنی و کلی اکانت پولی بخری. این پلتفرم همه‌چیز رو برات یک‌جا جمع کرده!
‏
✨
چرا این ابزار بازی رو عوض می‌کنه؟
🔹
تیم رویایی در یک پنجره:
به راحتی و با یک کلیک بین قوی‌ترین مدل‌های دنیا یعنی ‌ChatGPT⁩، ‌Claude⁩، ‌Gemini⁩، ‌Grok⁩ و ‌Kimi⁩ جابجا شو.
‏
🔹
تولید همه‌جانبه:
از نوشتن کدهای پیچیده و متن‌های خلاقانه تا خلق تصاویر و ویدیوهای جذاب، همه در یک محیط واحد.
‏
🔹
سهمیه رایگان روزانه:
هر روز کلی توکن رایگان بگیر و پروژه‌هات رو جلو ببر.
https://www.easemate.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6735" target="_blank">📅 10:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6734">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qML-PnW8nCG96RtPcgTQt7WrwhtRGQO2RRC9ZloNJt29HzMGIOkr4HikBxxvBMXa4UWQO_sed-_IRwF41VqHXxYD2gOpqSwt9qiq0e_JSx_uPsVPYwep5bm8ktYgqsNW50ectK0yEjxwDhALUy-bcAcKm054o2ahB04pZh1zauZU_Bl_-Pr7yoNtddWHy1BH0zC16QLGtSwqhcyMrvRiYeMfyTAFJgrGFMAuX74yy2brL3q9FiwPdhgbf4rzn53QdO5Bw5HMskpwW_vSb0xLXrkypdyNAybL5fH93UfDS5QbBbsepFzJUEvssx-cx-I5_ENEieCROLkyPGHBPb8phg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
غول هوش مصنوعی، بالاخره رایگان و بی‌دردسر!
‏دیگه نیازی به خرید اکانت پرمیوم یا دردسرهای ست کردن ‌API⁩ نیست؛ از امروز می‌تونید به صورت کاملاً رایگان توی پلتفرم ‌Tabbit⁩ با شاهکار جدید ‌Anthropic⁩ یعنی Claude Sonnet 5 گفتگو کنید!
💻
✨
‏
💡
چرا این خبر بمبه؟
سونت ۵ در حال حاضر یکی از باهوش‌ترین و دقیق‌ترین مدل‌های دنیاست که حالا بدون هیچ محدودیتی در دسترستون قرار گرفته. فقط کافیه وارد سایت بشید و چت رو شروع کنید
https://tabbit.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6734" target="_blank">📅 09:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🗂
هیچ‌چیز رو دور ننداز! معرفی Karakeep؛ بهشتِ آرشیوکارها و خوره‌های اطلاعات
🧠
اگر شما هم از اون دسته‌اید که روزانه ده‌ها لینک، مقاله و ویدیو رو برای «بعداً خوندن» ذخیره می‌کنید و در نهایت بینشون گم می‌شید،
Karakeep
(با نام قبلی Hoarder) دقیقاً برای شما ساخته شده. این ابزار یک جایگزین فوق‌العاده، سلف‌هاست و متن‌باز برای برنامه‌هایی مثل Pocket هست که با جادوی هوش مصنوعی ترکیب شده!
🔥
چرا Karakeep بی‌نظیره؟
🤖
تگ‌گذاری خودکار با AI:
با استفاده از LLMها (حتی مدل‌های لوکال مثل Ollama)، محتوای شما رو بررسی کرده و به صورت خودکار تگ‌گذاری و خلاصه‌نویسی می‌کنه.
🗄
آرشیو ابدی صفحات و ویدیوها:
برای جلوگیری از حذف شدن لینک‌ها (Link rot)، کل صفحه وب رو به صورت آفلاین ذخیره می‌کنه و حتی ویدیوها رو به کمک yt-dlp دانلود و آرشیو می‌کنه!
🔎
جستجوی قدرتمند و OCR:
متن داخل عکس‌ها رو استخراج می‌کنه و می‌تونید در کل محتوای ذخیره‌شده (فول‌تکست) جستجو کنید.
📱
همه‌جا در دسترس:
دارای افزونه برای کروم، فایرفاکس و سافاری، به همراه اپلیکیشن اختصاصی برای iOS و اندروید.
🔌
تعامل با ایجنت‌ها:
کاملاً سازگار با ایجنت‌های هوش مصنوعی (مثل OpenClaw) برای مدیریت خودکار اطلاعات از طریق CLI.
اسم این برنامه از کلمه عربی «کراکيب» (Karakeeb) الهام گرفته شده؛ به معنی خرت‌و‌پرت‌هایی که شلوغ به نظر می‌رسن اما پر از ارزش و خاطره‌ان و نمیشه دور ریختشون!
🔗
لینک مخزن گیت‌هاب پروژه:
https://github.com/karakeep-app/karakeep
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝑒𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6733" target="_blank">📅 08:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.  اینطوریه که ازت آی‌پی و پس رو میگیره  بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ... خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌  دیگه نیاز نیست دستور های ترمینال رو بدونی…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6732" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
