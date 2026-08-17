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
<img src="https://cdn4.telesco.pe/file/F-SGYdIGiiwuCQU0fLQ65rX84GkT9Z69kfbu4EscahQXjuZUgEj8eUGfEIjBufSyGZ2POu7svTMdXrDP6gK2fu2F7ZZkDzZjTLBGsiKI2AhEE5ZnHv53OB4E0mkM9T2zujZTUh11ZK1nA_9i8c4n9RdAhqENsFU_l4x3RZ724lpAgDZjwQez-msEDP0e4haZWH8XY0ojo04KM-rRCD3ixoecWLlc0E_TQ9ateStcBWXzIuU_T-YeOfjqzo5qSwg38WX3yOLgbgNA86wHsl2eYn2h9jsBnfDsPkGKmyvgFHCMDiXj3oX0T7Ychbvr25KcIcIaJPkKlTF9FwB9yCOrRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 21:22:11</div>
<hr>

<div class="tg-post" id="msg-21119">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سنتکام : تا امروز، نیروهای ما ۶۴ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/withyashar/21119" target="_blank">📅 20:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21118">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اتاق جنگ با یاشار : یک سر اگه به لایک های دو پست اخر نوید محمدزاده بزنید و ببینید چه کسانی ‌لایک کردن ، کمی بهتر با آدمهای اطرافتون آشنا میشوید.
@WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/21118" target="_blank">📅 20:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مارک لوین : رژیم ایران قصد تسلیم شدن نداره؛ ما قبلا هم با دشمنانی مثل ژاپن روبه‌رو شدیم که حاضر به تسلیم نبودن و مجبور شدیم برای تسلیم‌شدنشون از دو بمب اتم استفاده کنیم. البته الان قصد چنین کاری رو نداریم، اما رژیم ایران هم حاضر به تسلیم نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/withyashar/21117" target="_blank">📅 20:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f0c900572.mp4?token=gCe2svM8wVU9FlQNFSg76LCbyAG4mnkgpU_6t9BVuHkSwyaPMqZ4hQzr-D2xiTSiQlF5RX1XVMSRacWyyJM3OYVqm71xY9DU4Z52K6ov3rCyryBX2uqMSFaNVw-UpSZ-vDvfA07gA-zFbtnIch6pXSJrFNZPUhBgYJ1-jBupcTnPONwWPMd-tIldAkmb4kzrOqq9bCp6CMyADUFMPljK3_1TcMQPWA-hWq9uQsUJQlM97O6tTRpTB7Hy1Vjh9XnhKQGE1qwRBEybapjuJiRSJYtAvncU0TJazgA86Ukv840cd7uPieHWzwn--ardeTfnZKvwhTV7zBIAzTMEBrxMuaPJ_Z537ijCo8kUlLUtS67Zi1qMSPOhbbLobzIAwNbv-MTshrMuJScYSfVyi0R0kx-emPvn0N84bXCM0aQ6cgNDFQIuXcNmeE004eqsGgvMxMiDQWV9R1NkGiazlTxK1zn7Qeb-Asew-YSWDBIgdvUDgkPDiNiGy_SSBXbV-W_BRcff3nRSMoU6o5Pu4P9I4LjOhz1FOIjmt8CqQR3THIuYBZ_KpZ3NvCnIoN_Vg2j4ZXFoxizRWxSuzr0CB0WydhnS7wrRiQ4xLY7qoi19oovEo6DWbp1OURc0ASYQpDZDGHZbcSelx2-wjzTRdu9pUgHGfOB3RFnJUf57H1FLyiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f0c900572.mp4?token=gCe2svM8wVU9FlQNFSg76LCbyAG4mnkgpU_6t9BVuHkSwyaPMqZ4hQzr-D2xiTSiQlF5RX1XVMSRacWyyJM3OYVqm71xY9DU4Z52K6ov3rCyryBX2uqMSFaNVw-UpSZ-vDvfA07gA-zFbtnIch6pXSJrFNZPUhBgYJ1-jBupcTnPONwWPMd-tIldAkmb4kzrOqq9bCp6CMyADUFMPljK3_1TcMQPWA-hWq9uQsUJQlM97O6tTRpTB7Hy1Vjh9XnhKQGE1qwRBEybapjuJiRSJYtAvncU0TJazgA86Ukv840cd7uPieHWzwn--ardeTfnZKvwhTV7zBIAzTMEBrxMuaPJ_Z537ijCo8kUlLUtS67Zi1qMSPOhbbLobzIAwNbv-MTshrMuJScYSfVyi0R0kx-emPvn0N84bXCM0aQ6cgNDFQIuXcNmeE004eqsGgvMxMiDQWV9R1NkGiazlTxK1zn7Qeb-Asew-YSWDBIgdvUDgkPDiNiGy_SSBXbV-W_BRcff3nRSMoU6o5Pu4P9I4LjOhz1FOIjmt8CqQR3THIuYBZ_KpZ3NvCnIoN_Vg2j4ZXFoxizRWxSuzr0CB0WydhnS7wrRiQ4xLY7qoi19oovEo6DWbp1OURc0ASYQpDZDGHZbcSelx2-wjzTRdu9pUgHGfOB3RFnJUf57H1FLyiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما رژیم اومده یه برنامه تلویزیونی طنز ساخته که ترامپ رو توش مسخره میکنن
@WarRoom</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/withyashar/21116" target="_blank">📅 20:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فارس: یک نفتکش با مالکیت یکی از کشور های حوزه خلیج فارس در تنگه هرمز در نزدیکی قشم توقیف شد
@WarRoom</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/21115" target="_blank">📅 19:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اتاق جنگ با یاشار : در جریان جنگ ایران و عراق، اسرائیل برخلاف مواضع علنی جمهوری اسلامی، به‌صورت محرمانه به ایران سلاح و تجهیزات نظامی می‌فروخت؛ از جمله
موشک‌های ضدتانک تاو، موشک‌های هاوک، موشک‌های لنس، مهمات و قطعات یدکی هواپیما و تانک
. در سال ۱۹۸۱ نیز یک قرارداد
۱۳۶ میلیون دلاری
شامل موشک‌های لنس، هاوک و مهمات هدایت‌شونده
کوپرهد
میان طرفین انجام شد ، حسین شیخ‌الاسلام، قائم‌مقام وقت وزارت امور خارجه و از افراد درگیر در مذاکرات ایران با هیئت آمریکایی مک‌فارلین در یک مصاحبه درباره کمک‌های تسلیحاتی اسرائیل به ایران گفت :
فتح فاو بدون موشک‌های تاو و هاوکِ به‌دست‌آمده از این معاملات ممکن نبود.
هم‌زمان، اسرائیل برای تضعیف عراق مستقیماً وارد عمل شد؛ یکی از مهم‌ترین اهداف،
راکتور هسته‌ای اوسیراک در نزدیکی بغداد
بود. ابتدا
ایران به این تأسیسات حمله کرد
و در ۳۰ سپتامبر ۱۹۸۰ جنگنده‌های ایرانی راکتور را هدف قرار دادند، اما آن حمله نتوانست تأسیسات را به‌طور کامل نابود کند. حدود هشت ماه بعد، در ۷ ژوئن ۱۹۸۱، اسرائیل در
عملیات اپرا
با جنگنده‌های F-16 و F-15 به اوسیراک حمله کرد و راکتور را به‌طور کامل منهدم کرد؛ به این ترتیب، حمله اسرائیل عملاً کار نیمه‌تمام حمله ایران را به پایان رساند. بعدها ابعاد همکاری محرمانه تسلیحاتی ایران و اسرائیل با انتشار گزارش‌ها و اسناد و سپس در جریان
ماجرای ایران-کنترا
آشکارتر شد. به خمینی گفته شد محموله سلاحی که ایران به آن دست یافته اسرائیلی است، خمینی پس از مکثی گفت :
«اگر این سلاح‌ها را به دست آورده ایم ، آیا لازم است بپرسید فروشنده چه کسی است؟»
و وقتی پاسخ شنید «نه»، گفت :
«پس مشکل حل شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/21114" target="_blank">📅 19:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">Flower 3
@WarRoom</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/21113" target="_blank">📅 19:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پروژه
فلاور (Project Flower)
در سال ۱۹۷۷ میان ایران و اسرائیل آغاز شد؛ یک همکاری محرمانه موشکی که ایران هزینه و نفت پروژه را تأمین می‌کرد و اسرائیل فناوری و دانش فنی را در اختیار ایران می‌گذاشت.
در فاز نخست، توسعه یک موشک پیشرفته دریابه‌دریا با برد حدود ۲۰۰ کیلومتر
دنبال می‌شد و در
فاز دوم، توسعه موشک بالستیک جریکو-۲ با برد حدود ۱٬۵۰۰ کیلومتر
در برنامه قرار داشت. برای اجرای پروژه، ایران در نزدیکی
سیرجان
تأسیسات مونتاژ موشک و در حوالی
رفسنجان
محل آزمایش در نظر گرفته بود و بخش‌هایی از زیرساخت و همکاری فنی نیز ایجاد شده بود. ایران همچنین در سال ۱۹۷۸ حدود
۲۸۰ میلیون دلار نفت
به‌عنوان پیش‌پرداخت پروژه در اختیار اسرائیل قرار داد. با وقوع انقلاب ۱۳۵۷، پروژه متوقف شد و متخصصان و کارشناسان اسرائیلی ایران را ترک کردند؛ در نتیجه بخش قابل‌توجهی از تأسیسات و زیرساخت‌های ایجادشده برای پروژه، بدون تکمیل نهایی برنامه باقی ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/21112" target="_blank">📅 19:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Flower 2
@WarRoom</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/21111" target="_blank">📅 19:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">Flower 1
@WarRoom</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/21110" target="_blank">📅 19:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتاق جنگ با یاشار : در ماه‌های پایانی اتحاد شوروی، جورج اچ. دبلیو. بوش برخلاف انتظار، نه‌تنها از شوروی و گورباچف با ادبیات تهاجمی سخن نمی‌گفت، بلکه از اصلاحات او، شجاعت سیاسی‌اش و دستاوردهایش تمجید می‌کرد و تأکید داشت که آمریکا خواهان حفظ روابط نزدیک با دولت شوروی است. بوش حتی در اوت ۱۹۹۱ در کی‌یف، استقلال‌طلبان اوکراینی را از جدایی شتاب‌زده برحذر داشت و از ادامه اتحاد اصلاح‌شده شوروی حمایت کرد؛ تنها ۱۴۵ روز بعد، اتحاد شوروی برای همیشه فروپاشید. این همان نقطه‌ای است که مفهوم «فریب راهبردی» اهمیت پیدا می‌کند: قدرت بزرگ لزوماً قدرت واقعی خود را به رخ نمی‌کشد؛ گاهی با تعریف از رقیب، اطمینان‌بخشی، مذاکره و ایجاد احساس امنیت، او را از درک کامل موازنه واقعی بازمی‌دارد. امروز نیز می‌توان همین الگو را در برابر جمهوری اسلامی مشاهده کرد؛ آمریکا از مذاکره و توافق سخن می‌گوید، اما هم‌زمان فشار اقتصادی و نظامی خود را حفظ می‌کند. اگر این یک راهبرد آگاهانه باشد، هدف این نیست که تهران صرفاً تصور کند آمریکا ضعیف است؛ هدف این است که
نتواند بفهمد آمریکا واقعاً چه مقدار قدرت، صبر و گزینه‌های پنهان برای مرحله بعد در اختیار دارد.
همان بازی‌ای که در ماه‌های پایانی شوروی، با خویشتن‌داری و اطمینان‌بخشی پیش رفت و سرانجام جهان را با فروپاشی یکی از دو ابرقدرت آن دوره روبه‌رو کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/21109" target="_blank">📅 18:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21108">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">متکی ,نماینده تهران در مجلس :
۹۰ روز آینده بسیار مهم است
نظم آینده منطقه به نتیجه این جنگ بستگی دارد چون نتیجه جنگ مشخص می‌کند آرایش منطقه‌ای چگونه خواهد بود.بنای آمریکا اجرای تفاهم‌نامه نیست و قرار است ما فقط مشغول مذاکره باشیم تا آنها انتخابات را ببرند.
@WarRoom</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/21108" target="_blank">📅 18:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21107">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ادعای سی‌ان‌ان : کوشنر بیش از چهار ساعت نتانیاهو را تحت فشار قرار داد تا طرح آتش‌بس ترامپ برای غزه را پیش ببرد،  اما نتانیاهو در برابر این فشار مقاومت کرد و با اشاره به انتخابات اکتبر، تأکید کرد که پیش از هرگونه عقب‌نشینی اسرائیل، حماس باید به‌طور کامل خلع…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/21107" target="_blank">📅 18:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21106">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک منبع دیپلماتیک پس از ملاقات کوشنر و نتانیاهو: در این ملاقات، به طور مشخص توافق شد که بازسازی نوار غزه قبل از خلع سلاح کامل حماس آغاز نشود. همچنین، تاکید شد که سیاست پیشگیری (حمله پیش از وقوع) در مواردی که خطر آسیب رساندن به نیروهای ارتش اسرائیل وجود داشته…</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/21106" target="_blank">📅 18:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21105">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کلودفلر :
ترافیک اینترنت بین الملل ایران از ۹۰ درصد به ۵۹ درصد رسیده ،وضعیت الان اینترنت ایران دقیقا مثل روزای قبل از قطعی ۸۸ روزه ی اینترنته و با اختلالات بسیار سنگین همراه شده.
@WarRoom</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/21105" target="_blank">📅 17:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21104">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ظریف : قرار بود بعد رفتن آمریکا از افغانستان، نظام شاهنشاهی اونجا مجدد برگرده اما ما نزاشتیم و کمک کردیم طالبان قدرت بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/21104" target="_blank">📅 17:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21103">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/21103" target="_blank">📅 17:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21102">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رویترز : ایران به آمریکا ضرب‌الاجل داد
ایران از طریق پاکستان به آمریکا وقت داده که در عرض یک یا حداکثر دو هفته محاصره دریایی رو رفع و سر دیپلماسی برنگرده وضعیت براشون بد میشه
سپاه گفته در صورت تمام شدن ضرب‌الاجل جنگ رو گسترده و تمامی منافع نظامی و سیاسی و اقتصادی آمریکا در کل منطقه موشک باران میشن
@WarRoom</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/21102" target="_blank">📅 17:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21101">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک منبع دیپلماتیک پس از ملاقات کوشنر و نتانیاهو:
در این ملاقات، به طور مشخص توافق شد که بازسازی نوار غزه قبل از خلع سلاح کامل حماس آغاز نشود.
همچنین، تاکید شد که سیاست پیشگیری (حمله پیش از وقوع) در مواردی که خطر آسیب رساندن به نیروهای ارتش اسرائیل وجود داشته باشد علیه تروریست‌ها ، ادامه داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/21101" target="_blank">📅 17:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21100">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رسوایی برای نخست‌وزیر جدید بریتانیا: او با فردی که خود را به عنوان یک مقام ارشد در کاخ سفید جا زده بود، مکاتبه کرد
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/21100" target="_blank">📅 17:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21099">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیروی دریایی ایالات متحده قراردادی به ارزش 22.9 میلیارد دلار با شرکت "RTX" بست تا موشک‌های "تاماهاک" تولید کند
@WarRoom</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/21099" target="_blank">📅 16:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21098">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرگزاری ولت آلمان: اگر ترامپ بیشتر از این برای حمله معطل کند، ایران رسما برنده جنگ می شود
@WarRoom</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/21098" target="_blank">📅 16:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21097">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: محاصره دریایی آمریکا همچنان فشار اقتصادی جدیدی بر نظام ایران وارد می‌کند.
ما انباری بزرگی از سلاح‌های میان‌برد داریم که می‌توان در آینده، در صورت لزوم، از آن‌ها استفاده کرد.
مقداری از سلاح‌هایی که تا کنون از ذخایر موجود استفاده کرده‌ایم، ناچیز است.
انتخابات میان دوره‌ای آمریکا کوچکترین اثری در مورد دیدگاه و نظر من در مورد ایران ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/21097" target="_blank">📅 16:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21096">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حوثی‌های یمن اعلام کردند که با موشک، «یک کشتی نظامی سعودی و چهار شناور همراه آن» را در دریای سرخ هدف قرار داده‌اند.
عربستان سعودی هنوز واکنشی نشان نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/21096" target="_blank">📅 16:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی سپاه: ادعای امروز ترامپ درباره گفتگوی پشت‌پرده با سپاه، توهمات ناشی از شکست است
@WarRoom</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/21095" target="_blank">📅 16:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رویترز:
یک مقام ارشد ایرانی اعلام کرد ایران از موضع دفاعی به سیاستی «کاملاً تهاجمی» تغییر مسیر داده است. تهران چند هفته به واشنگتن فرصت داده تا تفاهم‌نامه موجود را به‌طور کامل اجرا کند. این مقام هشدار داد ایران محاصره دریایی نامحدود آمریکا را تحمل نخواهد کرد و در صورت شکست دیپلماسی، برای تشدید تنش‌ها در تنگه هرمز و سراسر منطقه آماده است. قرار است این ضرب‌الاجل از طریق میانجی‌ها به آمریکا و دولت‌های منطقه منتقل شود؛ موضوعی که در صورت نرسیدن به توافق، خطر تشدید درگیری نظامی را افزایش می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/21094" target="_blank">📅 16:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک مقام ارشد ایرانی : ایران تا ابد منتظر ماندن زیر محاصره دریایی آمریکا نخواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/21093" target="_blank">📅 16:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ: من عجله‌ای برای مذاکره با ایران ندارم و جدول زمانی مشخصی برای این کار تعیین نکرده‌ام.
@WarRoom</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/21092" target="_blank">📅 15:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21090">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: ایران باید پرچم تسلیم را برافرازد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/21090" target="_blank">📅 15:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21089">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ در مورد حماس : ما یک کانال ارتباطی متفاوت با حماس داریم و در نهایت آن‌ها سلاح‌های خود را زمین می‌گذارند
اسرائیلی‌ها نباید در غزه حمله کنند، زیرا حماس موافقت کرده است که سلاح‌های خود را زمین بگذارد!
@WarRoom</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/21089" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21088">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143fd65f66.mp4?token=KuTIrbYOYaAwMhovBoE-2tSXiUyY51VD9FL0x3qrqwPOc_rpztzSJbiRern6orh_xn6IVBOjrf_fCGou6VsYSXH_bgF6gQ82y9crTUvzc9IcVrprlMXtuVYtMyLLTM2rFvWsHrN1KASabG-1yp6ZCyc7EvnmcyxHZs_PUF7OUlfxUxroyEllnKqiWQ4vJ7D5BZdz4X5yv-9dsOFTEt4E-qG-X-DgWTyZq6WQOXlaakw7GgC1sUjMmNYunVPL6mQiig4nxxt_X6I9PsKmatAeszi-2ECPzwipKziGhdRJuz7xberixPyCKmV42dYTU0wdQJEysBU-OENsn2ar5mbLJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143fd65f66.mp4?token=KuTIrbYOYaAwMhovBoE-2tSXiUyY51VD9FL0x3qrqwPOc_rpztzSJbiRern6orh_xn6IVBOjrf_fCGou6VsYSXH_bgF6gQ82y9crTUvzc9IcVrprlMXtuVYtMyLLTM2rFvWsHrN1KASabG-1yp6ZCyc7EvnmcyxHZs_PUF7OUlfxUxroyEllnKqiWQ4vJ7D5BZdz4X5yv-9dsOFTEt4E-qG-X-DgWTyZq6WQOXlaakw7GgC1sUjMmNYunVPL6mQiig4nxxt_X6I9PsKmatAeszi-2ECPzwipKziGhdRJuz7xberixPyCKmV42dYTU0wdQJEysBU-OENsn2ar5mbLJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما با سپاه پاسداران انقلاب اسلامی یک کانال ارتباطی داریم.
ما مستقیماً با مقامات سپاه در ایران صحبت می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/21088" target="_blank">📅 14:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21087">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ممکن است در انتخابات اسرائیل از شخص خاصی حمایت کنم
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/21087" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21086">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ در فاکس‌نیوز هشدار داد که اگر عمان مانع منافع آمریکا شود، این کشور را بمباران خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/21086" target="_blank">📅 14:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21085">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به فاکس نیوز:
یک کانال ارتباطی محرمانه با مقام‌های سپاه پاسداران ایران داریم
@WarRoom</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/21085" target="_blank">📅 14:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ادعای العربیه : گزارش‌ها حاکی از آن است که با تمدید دوره ۶۰ روزه بین ایران و آمریکا موافقت شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/21084" target="_blank">📅 14:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21083">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیروهای مسلح یمن با شلیک ده‌ها موشک بالستیک و پهپاد، مواضع نظامی و انبارهای تسلیحاتی نیروهای وابسته به عربستان را در المخا و مأرب هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/21083" target="_blank">📅 14:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21082">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyORjRoTjt_lqDkvlSUC-nq7Td4ZOg3pfvS1ZXJZD-XpfGQwEf4OM98M2Lns06DdANgFRIfmsNOQJHmcrVSMRUesIaiyW8UNVoyLSj_Q1TjWDF0XI_HJ4xnOS_rgC2Edyd4FDVNpZqq52iUYXKBPwe6ytt5aHV9ke66k5kAM3ehBtd-ECR7oJz5RlrTR_1zdqPEvne2aiB2UjGZoI-7AWODcacKaVGvJNauRyVXFzwGDS89ceimZQuYH_5Gg2POnxXwP7iHCwzL47udk7bbOxc0s0icxQgCWi3Vv8Vlben0ktUS598AkbwHvoiWG9ROWc8v3jhIjGVhvxwFbYQI0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : هدف شماره یک، و همیشه همین خواهد بود، این است که ایران تحت هیچ شرایطی، به هیچ شکل و صورتی، نتواند سلاح هسته‌ای داشته باشد. از توجه شما به این موضوع سپاسگزارم!
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/21082" target="_blank">📅 14:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21081">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حمله پهپادی ایران به دفتر بارزانی
مسعود بارزانی: در پی تحقیقات واحد ضدتروریسم کردستان، دفتر شخصی من و منزل رئیس سازمان امنیت و اطلاعات، امروز هدف حملات پهپادی ایران قرار گرفتند. من این حملات بی‌پروا و غیرقابل‌قبول را به شدیدترین شکل ممکن محکوم می‌کنم. این یک تشدید خطرناک و تهدیدی مستقیم علیه امنیت و ثبات اقلیم کردستان است. این حملات ما را از انجام وظایفمان و حفاظت از شهروندانمان بازنخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21081" target="_blank">📅 13:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21080">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنگوی وزارت خارجه ایران:
تفاهم‌نامه‌ای که با طرف آمریکایی امضا کردیم، هیچ مهلت ۶۰ روزه‌ای را تعیین نکرده است.  آمریکا چند هفته پس از امضای تفاهم‌نامه، مفاد آن را نقض کرد.
گفتگوها با عمان به دلیل پیچیدگی موضوع، دخالت بازیگران متعدد و کشورهایی که به دنبال تضعیف این روند هستند، مدت زیادی است که به تعویق افتاده است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21080" target="_blank">📅 12:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وال‌ااستریت ژورنال به نقل از مقام‌های ایرانی و عرب گزارش داده است که تهران در وقفه دوماهه اخیر به‌جای کاهش تنش، برای
گسترش جنگ و درگیری طولانی‌تر
آماده شده است. طبق این گزارش، سپاه هماهنگی با نیروهای همسو در
یمن، عراق و لبنان
را افزایش داده، تولید موشک و پهپاد را بالا برده و همزمان فشار بر کشتیرانی در تنگه هرمز و دریای سرخ را تشدید کرده است. مقام‌های عرب نگران‌اند که در صورت آغاز دور جدید درگیری، این نیروها علیه
نیروهای آمریکایی، اسرائیل و زیرساخت‌های انرژی منطقه
وارد عمل شوند
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21079" target="_blank">📅 11:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21078">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGEMPx5nES8WHGS2DY1VhjjT3kerUTRRsAq2zhzQSxdYwnRlN2XTC-7zO2N_K7jgqPp1x7CmLcq72Uwg5m69iiet4B2Fa69cq-mYpF-biTVTtXY36YoM1jUpZ-XOdzUlo15Il0F-oTUt6mbAnuUnFQrQnR6TeFSGNiRkSZEluy7vSd2tIyZwT7PUIF7lU4n0HOIT3i-SKc8NXNECl8Z3WoVnMTPNPWdQMhRyk-g-N-5Wo1JQknmIggIzWBcso7yfNxKXLdUuSQ8vd59EXDEmA2xuEvbLcHwXiyAJGqvw3m00XFeIbTgPISRBktAeEqmtRkzqRmD9Ks8FUF7g7PP4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بررسی داده‌های پرواز فعالیت همزمان دو فروند هواپیمای E6B-Mercury فرماندهی و کنترل راهبردی آمریکا در آسمان خبر می‌دهند.این هواپیما ها بخشی از سامانه ارتباطی آمریکا برای حفظ ارتباط با زیردریایی‌های حامل موشک و نیروهای راهبردی است و لزوماً به معنی آغاز حمله هسته‌ای نیست. اما ولی حضور همزمان دو فروند می‌تواند نشان‌دهنده
فعالیت یا آمادگی بالاتر
از معمول و
در سطح فرماندهی راهبردی
باشد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21078" target="_blank">📅 11:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وای نت : حوزه‌های رأی‌گیری در سراسر اسرائیل برای انتخابات مقدماتی حزب لیکود باز شده‌اند. حدود ۱۴۰ هزار رأی‌دهنده از بین ۱۲۴ نامزد، که ۷۹ نفر از آنها در فهرست ملی و ۴۵ نفر در حوزه‌های انتخابیه هستند، انتخاب خواهند کرد. حدود ۸۰ حوزه رأی‌گیری حزبی در شهرهای بزرگ و همچنین در مناطق حاشیه‌ای، از جمله در هیخال شلومو در تل‌آویو، حیفا، ریشون لتصیون، ایلات، اوفاکیم و بنیامین هائوما در اورشلیم، جایی که بنیامین نتانیاهو، نخست وزیر، نیز رأی خواهد داد، برپا شده است. حوزه‌های رأی‌گیری ساعت ۱۰ شب بسته خواهند شد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21077" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وال‌استریت ژورنال: به نظر می‌رسد رهبران ایران به‌جای تکیه بر دیپلماسی با آمریکا، خود را برای یک درگیری گسترده‌تر و طولانی‌تر آماده می‌کنند. تهران در فاصله آرامش پس از توافق ژوئن، توان موشکی و پهپادی خود را بازسازی، سپاه را تقویت و نیروهای نیابتی منطقه‌ای را برای عملیات تهاجمی هماهنگ کرده است. فشار بر کشتیرانی در تنگه هرمز و دریای سرخ و تهدید زیرساخت‌های انرژی خلیج فارس نیز افزایش یافته است. هم‌زمان، تندروها کنترل بیشتری بر ساختار نظامی و امنیت داخلی پیدا کرده‌اند. هدف این راهبرد، بالا بردن هزینه حمله به ایران و بازدارندگی آمریکا، اسرائیل و کشورهای خلیج فارس از حملات آینده است؛ به‌طوری‌که تهران ظاهراً موقعیت کنونی را پایان جنگ نمی‌داند، بلکه آن را آماده‌سازی برای رویارویی بزرگ‌تر می‌بیند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21076" target="_blank">📅 10:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیویورک تایمز به نقل از منابع آگاه:مهلت ۶۰ روزه توافق اسلام‌آباد بدون نتیجه پایان یافت و جنگ وارد مرحله فرسایشی اقتصادی شده است.
واشنگتن خواستار بازگشایی هرمز است و ایران آزادسازی دارایی‌هایش را شرط آن می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21075" target="_blank">📅 10:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e2168088.mp4?token=dVKOyK78sCh-RVVd-jxmtA8JZPTfjNa7QhVqwKdxrnnGGJ052hnicPt8xwS20BeaZepYcscCcFOrixxZ8DjhwBRSr_-2CCz1sRwqrp4MJubkjBphxJO9BCZjRvIlhpcAWAUkUC0YmM9AyRBhA7rviWpEAwuVKApVK3Wt_Y_MfchSyuaUAhsdTIwnOgQyCUE9ApwutTX8aDqbuVf99KDFE8QVid-4ci5PsruyOG6eHJKN8T8YKwSXvL-Yy5UEkBfHej4vJEf7XxiU--h1gJVoFwxTRwl3sWedHWQsCDt4EW6MWSG52DgGsMZ2ZfDoYHYyhb4qe0epcm_xGTNINknTVBnra1NLol3t_AzPdChGiznozNls86gpj-ixqivTZObgjX9C6Fes5bvDB06C6ZeTdrX2k7sKHoE7OLJj8qGx8Mn98c_Wn0N2qydekNIeLxZBanjgYXhZu5tumdNYIm3WRx4B1tDipvHIQCtLrwULhJDsZ9PPmvHDoPVkUTSnN_pZXUqkemawtNFrb69fVaXZAFsvJXVrbxOfzOLfQCd7L9Klyv7FEE3LEmufHwn9W_ImtFZUwyPaxiCVigTAWlydqkCQEERxiBb4hG1twUtYewBGQYItwQy3UMk5G7BtJGg91bKpUn4DoVBBeiD3Kiq8reSLAA8ZlV0bTzHQfR33iNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e2168088.mp4?token=dVKOyK78sCh-RVVd-jxmtA8JZPTfjNa7QhVqwKdxrnnGGJ052hnicPt8xwS20BeaZepYcscCcFOrixxZ8DjhwBRSr_-2CCz1sRwqrp4MJubkjBphxJO9BCZjRvIlhpcAWAUkUC0YmM9AyRBhA7rviWpEAwuVKApVK3Wt_Y_MfchSyuaUAhsdTIwnOgQyCUE9ApwutTX8aDqbuVf99KDFE8QVid-4ci5PsruyOG6eHJKN8T8YKwSXvL-Yy5UEkBfHej4vJEf7XxiU--h1gJVoFwxTRwl3sWedHWQsCDt4EW6MWSG52DgGsMZ2ZfDoYHYyhb4qe0epcm_xGTNINknTVBnra1NLol3t_AzPdChGiznozNls86gpj-ixqivTZObgjX9C6Fes5bvDB06C6ZeTdrX2k7sKHoE7OLJj8qGx8Mn98c_Wn0N2qydekNIeLxZBanjgYXhZu5tumdNYIm3WRx4B1tDipvHIQCtLrwULhJDsZ9PPmvHDoPVkUTSnN_pZXUqkemawtNFrb69fVaXZAFsvJXVrbxOfzOLfQCd7L9Klyv7FEE3LEmufHwn9W_ImtFZUwyPaxiCVigTAWlydqkCQEERxiBb4hG1twUtYewBGQYItwQy3UMk5G7BtJGg91bKpUn4DoVBBeiD3Kiq8reSLAA8ZlV0bTzHQfR33iNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران شد: اتفاقات خوبی خیلی زود رخ خواهد داد. در واقع، آنها همین حالا هم رخ داده‌اند، چون یک کاری هست که ما نمی‌توانیم اجازه دهیم انجام شود: ما نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21074" target="_blank">📅 02:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKzxkE94Fi0xZFcnx7ShtS7HoTcNadPLcSkf6i34KcLx-i4E1sJLiM6gYBS3_ZNyCVJb2PFo4vrA55nhoRwvJn7EbK0v2DHai3rMJ5o6DgrcE-CpPUyUPWvdn_6BsVYHTpPFW_rYJWX77SEhYzVPlptlTrp8L_AHe_13HV6qwApQCIW79jNKnXDwSRcjYNLy8NLotOMD12lnV7DZk6ishEG9sYJYZFK4DE3CDF0KKKxy4iBpu7ZZVP2KDJyUFHM3ZIwvawUrQW0retn4oavfkBDSqxyyvND_7y2JNLOhTiutytBt9n7uk8OO8OBPh5hU5RoSK0F1NX3O2CJ3xPFg1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :با توجه به رابطه بسیار خوبی که با کیم جونگ اون، رهبر کره شمالی، دارم، از اینکه ایالات متحده مدت‌ها پیش با برگزاری رزمایش‌های نظامی مشترک با کره جنوبی موافقت کرده، خوشحال نیستم. این رزمایش‌ها نه‌تنها پرهزینه هستند و بخش زیادی از هزینه‌هایشان، مثل همیشه، بر عهده آمریکا است، بلکه پیامی کاملاً نامناسب و خصمانه به کشوری ارسال می‌کنند که تا زمانی که دونالد جی. ترامپ رئیس‌جمهور بوده، رفتاری تهدیدآمیز نداشته و محترمانه رفتار کرده است. بنابراین، و با توجه به اینکه دیگر برای لغو آنها خیلی دیر شده است، به پیت هگست، وزیر جنگ، دستور داده‌ام رزمایش‌های نظامی مشترک را به میزان قابل‌توجهی کاهش دهد! البته این موضوع تا حدی بی‌ارتباط است (؟)، اما اخیراً از رئیس‌جمهور کره جنوبی پرسیدم که آیا مایل هستند به ما در خلع سلاح هسته‌ای جمهوری اسلامی ایران بپیوندند و آنها گفتند: «نه، ممنون!» از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21073" target="_blank">📅 02:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ از نیوجرسی پرواز کرده و در راه واشنگتن است. او به طور خلاصه به خبرنگاران گفت: «آخر هفته فوق‌العاده‌ای بود. جلسات زیادی داشتیم.» وقتی خبرنگاران از او پرسیدند که آیا این جلسات درباره ایران بوده است، پاسخی نداد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21072" target="_blank">📅 01:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ در تروث‌ :بسیار خوشحالم که عربستان سعودی، ترکیه و پاکستان سرانجام و اخیراً توافق دفاعی مشترک مکه را امضا کرده‌اند. این نشان می‌دهد که خاورمیانه در حال متحد شدن است و کشورها سرانجام خواهند توانست به شکلی مؤثرتر و معنادارتر از خود دفاع کنند.به رهبران بزرگ این سه کشور تبریک می‌گویم. این یک گام نخست بزرگ، جسورانه و مهم است , واو!
@WarRoom
واکنش بی بی : فقط کسی توضیح بده دقیقاً قرار است از چه کسی در برابر چه کسی دفاع کنند!
😂</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21071" target="_blank">📅 00:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ در تروث به‌شدت از برنامه شنون بیم در فاکس‌نیوز انتقاد کرده و آن را هم‌سطح «بدترین بخش‌های سی‌ان‌ان» دانسته است. او می‌گوید این برنامه دائماً مهمان‌ها و نظرسنجی‌های منفی علیه دولتش انتخاب می‌کند و دستاوردهای دولتش را نادیده می‌گیرد. ترامپ همچنین از خوان ویلیامز و جسیکا تارلوف انتقاد کرده و پیش‌بینی کرده رتبه بینندگان برنامه شنون سقوط خواهد کرد. او در پایان تأکید کرده که خودش در دفتر بیضی مشغول ادامه کار برای «پیروزی‌ها و موفقیت‌های بیشتر» است
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21070" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21069" target="_blank">📅 00:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21068" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21067" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سیریک موشک بلند شد
🤠
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21066" target="_blank">📅 00:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سیریک موشک بلند شد
🤠
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21065" target="_blank">📅 23:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">داریوش اقبالی با انتشار ترانه جدیدی به نام «توهم توطئه» و کنایه به شاهزاده رضا پهلوی به کمپین آنفالو توسط مردم پیوست. در صدر این جدول نوید محمدزاده با نزدیک به یک میلیون آنفالو قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21064" target="_blank">📅 23:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رویترز : جرد کوشنر، فرستاده ویژه ترامپ، فردا دوشنبه ۱۷ اوت با بنیامین نتانیاهو دیدار خواهد کرد. این دیدار در چارچوب تلاش واشنگتن برای پیشبرد طرح صلح غزه انجام می‌شود؛ طرحی که شامل خلع سلاح حماس، توقف عملیات نظامی و خروج تدریجی نیروهای اسرائیلی از غزه است.…</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21063" target="_blank">📅 23:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال 12 اسرائیل: اعضای حزب الله و سپاه در زیر زمین در ارتفاعات علی الطاهر گیر افتاده اند و تعداد آنهابیش از ده هانفر تخمین زده می شود.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21062" target="_blank">📅 22:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام به وال استریت ژورنال: گروه ضربت ناو هواپیمابر لینکلن تیمی قوی از آمریکایی‌های با دستاوردهای بالا است که با غرور فراوان و موجه به هر آنچه که به دست آورده‌اند، ایستاده‌اند.
تاریخ این استقرار را به عنوان یکی از فشرده‌ترین و مهم‌ترین استقرارهای دوران مدرن ثبت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21061" target="_blank">📅 22:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8429c9c845.mp4?token=iypi_2Pfu9iAQZoTliZTxIYcyfL-7eioNHwUFHBPHFdwhsgsrJMmbDVwIA-Yx21G1fpx0ehqSjJFf3J08TgwxYPylFoqgBjoOuqUckICOm0tIKZlchf0bscQ-25g3Lqa3o5OyeYIYCa6idlJWHX53ZmPzY17iXJKvTq20NZz7T45cWAWNXvqvT88C2pq6DQSfgArdUXknTsnUMOfelzt9x8Nnh6Yr7TipGNUbXSg5p_vCJiGS98J7jNS8zQEDvuHvrfjZPTwe0lszJ_p1WnSzrfOKuomRnXH4hFYl_wPwEWBzwr438XlgSGiUbTn0sl54WE_niU6MhLibcOYW8qNEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8429c9c845.mp4?token=iypi_2Pfu9iAQZoTliZTxIYcyfL-7eioNHwUFHBPHFdwhsgsrJMmbDVwIA-Yx21G1fpx0ehqSjJFf3J08TgwxYPylFoqgBjoOuqUckICOm0tIKZlchf0bscQ-25g3Lqa3o5OyeYIYCa6idlJWHX53ZmPzY17iXJKvTq20NZz7T45cWAWNXvqvT88C2pq6DQSfgArdUXknTsnUMOfelzt9x8Nnh6Yr7TipGNUbXSg5p_vCJiGS98J7jNS8zQEDvuHvrfjZPTwe0lszJ_p1WnSzrfOKuomRnXH4hFYl_wPwEWBzwr438XlgSGiUbTn0sl54WE_niU6MhLibcOYW8qNEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ‌ درباره سخنگوی ‌کاخ سفید:
من متوجه شدم که کارولین لیویت فرزندانش را بیشتر از ترامپ دوست دارد، من از این بابت بسیار نگران هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21060" target="_blank">📅 21:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اورشلیم پست :
حماس بخش مهمی از فعالیت‌های خود را از قطر به ترکیه منتقل کرده است.
بر اساس گزارش‌های تازه، بخش عمده فعالیت‌های محرمانه حماس، از جمله واحدهای برنامه‌ریزی و سایبری، به ترکیه منتقل شده و بسیاری از رهبران این گروه نیز بیشتر در ترکیه حضور دارند. با این حال،
دفتر سیاسی و فعالیت‌های علنی حماس همچنان در قطر ادامه دارد
و هنوز انتقال کامل دفتر سیاسی به ترکیه تأیید نشده است. این جابه‌جایی در حالی انجام شده که حماس همزمان برای مذاکرات مربوط به آینده غزه، از کانال‌های قطر، ترکیه و مصر استفاده می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21058" target="_blank">📅 21:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش پرتاب موشک از قشم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21057" target="_blank">📅 20:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رویترز : جرد کوشنر، فرستاده ویژه ترامپ، فردا دوشنبه ۱۷ اوت با بنیامین نتانیاهو دیدار خواهد کرد. این دیدار در چارچوب تلاش واشنگتن برای پیشبرد طرح صلح غزه انجام می‌شود؛ طرحی که شامل
خلع سلاح حماس، توقف عملیات نظامی و خروج تدریجی نیروهای اسرائیلی از غزه
است. نتانیاهو پیش‌تر با بخش‌هایی از این طرح مخالفت کرده بود و کوشنر برای نزدیک‌کردن مواضع دو طرف به اسرائیل سفر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21056" target="_blank">📅 20:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c8cf686.mp4?token=Njxy1XIQcHqt0i3H0FfSC7ZkR3yeGzafGq2fKi8qLOV_DNEseA-jPcmWLlCM1knltI-X_iap4aHdJGgnX0LBpUFQfTVJ4i_l8F2UsLx2aNODnW7_nOBf5iPPbI--MQVkuJWBhzc44jQYaXKUakJiOQEcTRe793zF7D1wotvyY5vqRD6u1J7NMF8cYk2CjsS4TrftTtzCdR-UTWyl3-DFPA0y4fF81DVJLgmOAYmRLFly7DMA2ttfPzJLyXZdCtdiF3C0KwGpwGBALnBT_oBCNlQfYGMes1yw2oFUn00Zv6rlozxwF22ydD8lwNXIBzwsuxF5elSCYsRl8Bz9whogRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c8cf686.mp4?token=Njxy1XIQcHqt0i3H0FfSC7ZkR3yeGzafGq2fKi8qLOV_DNEseA-jPcmWLlCM1knltI-X_iap4aHdJGgnX0LBpUFQfTVJ4i_l8F2UsLx2aNODnW7_nOBf5iPPbI--MQVkuJWBhzc44jQYaXKUakJiOQEcTRe793zF7D1wotvyY5vqRD6u1J7NMF8cYk2CjsS4TrftTtzCdR-UTWyl3-DFPA0y4fF81DVJLgmOAYmRLFly7DMA2ttfPzJLyXZdCtdiF3C0KwGpwGBALnBT_oBCNlQfYGMes1yw2oFUn00Zv6rlozxwF22ydD8lwNXIBzwsuxF5elSCYsRl8Bz9whogRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرش دعوا شد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21055" target="_blank">📅 20:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏کارزار انتخاباتی جدید نتانیاهو؛ «آنها می‌خواهند نتانیاهو شکست بخورد، اجازه ندهید پیروز شوند» مجتبی خامنه ای، زهران ممدانی ، اردوغان ، نعیم قاسم @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21054" target="_blank">📅 19:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDR0AnUa-YBOIxSZfeEbg-V250ZofCkLNCfzbihS6ld4cFvGnh0lO7zG7ND0w5-x4P1B1iGEU5cbmse5LtWIn8he0n0C-jji8VKRhPX83H6gdEhDhxgtpqqijYeeOJdsIz6nap-uJ9PV8GRZ4CKLBRBLIm2IBidsGeKoNXxb339NZ7ouK04W-tgT0ELG1oY3xRwz6120yt2Q-rLtGk2BJ1GQ2_2aEcFSVqMlSGRYlPolBdGeEGIIq1XGlwFhLyOWWn7CNAuDoicBy_rJNfTVy4ABbo2uYdUvk0TWy6v78ztQV836BQnSgGdXuOsALqiKicY6n1tYihqb7ARoROHymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏کارزار انتخاباتی جدید نتانیاهو؛ «آنها می‌خواهند نتانیاهو شکست بخورد، اجازه ندهید پیروز شوند»
مجتبی خامنه ای، زهران ممدانی ، اردوغان ، نعیم قاسم
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21053" target="_blank">📅 19:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فاکس‌نیوز: مهلت ۶۰ روزه تفاهم‌نامه آمریکا و ایران فردا به پایان می‌رسد.
بر اساس گزارش فاکس‌نیوز، تفاهم‌نامه ۱۷ ژوئن میان واشنگتن و تهران یک بازه ۶۰ روزه برای مذاکره درباره برنامه هسته‌ای و موشکی ایران، تحریم‌ها و آزادی کشتیرانی در تنگه هرمز تعیین کرده بود که مهلت آن
۱۷ اوت
است
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21052" target="_blank">📅 17:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">افسر قطری در گفت‌وگو با الجزیره درباره خلبانان ایرانی اظهارنظر کرده است.
در این گفت‌وگو، سرهنگ دوم
ناصر محمد الکبیسی
از وزارت دفاع قطر درباره سرنگونی دو فروند سوخو-۲۴ ایرانی گفت که هواپیماها بمب حمل می‌کردند و در توضیح منبع اطلاعات، به «تأیید خلبان» اشاره کرد؛ در حالی که قطر پیش‌تر گفته بود خلبانان به تماس‌های رادیویی پاسخ نداده‌اند. این اظهارات دوپهلو اکنون در کنار ادعای ایران درباره زنده‌بودن و اسارت سه خلبان ایرانی، مورد توجه قرار گرفته است، زیرا قطر می‌گوید هیچ خلبان ایرانی زنده‌ای را در اختیار ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21051" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آکسیوس: پیام‌ها میان تهران و واشنگتن همچنان ردوبدل می‌شود، اما مذاکرات در بن‌بست است.
آکسیوس گزارش داده آمریکا و ایران از طریق
پاکستان و قطر
همچنان پیام‌هایی را ردوبدل می‌کنند، اما تاکنون پیشرفت قابل‌توجهی حاصل نشده است. در پشت پرده نیز دولت ترامپ برای ارتباط مستقیم‌تر با
سپاه
یک کانال محرمانه از طریق
بارزانی
ایجاد کرده بود و چند پیشنهاد و پاسخ میان دو طرف ردوبدل شد؛ حتی یک تفاهم اولیه شکل گرفت، اما خیلی زود فروپاشید. اکنون میانجی‌ها همچنان فعال‌اند و بارزانی نیز اخیراً به کاخ سفید پیشنهاد داده برای ازسرگیری مذاکرات آمریکا و ایران کمک کند
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21050" target="_blank">📅 17:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رویترز: ترامپ به دنبال تشدید فشار اقتصادی بر ایران است؛ محاصره زمینی هم به‌عنوان یک گزینه مطرح شده است.
رویترز گزارش داده آمریکا علاوه بر محاصره دریایی و تحریم‌های گسترده، گزینه
محاصره زمینی ایران
را نیز بررسی کرده؛ اقدامی که به همکاری عراق، ترکیه، پاکستان، افغانستان، ترکمنستان، جمهوری آذربایجان و ارمنستان نیاز دارد و به‌دلیل دشواری‌های جغرافیایی و سیاسی، اجرای آن بسیار سخت ارزیابی می‌شود. واشنگتن همچنین در حال بررسی تحریم پالایشگاه‌ها و بانک‌های چینیِ مرتبط با نفت ایران و اعمال فشار بر کشورهایی است که به تجارت یا تأمین تسلیحات ایران کمک می‌کنند. رویترز می‌گوید از آغاز دور دوم ریاست‌جمهوری ترامپ،
بیش از ۱۰۰۰ فرد، کشتی و هواپیما
تحریم شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21049" target="_blank">📅 17:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd67bb941.mp4?token=AGkoXMd_dJQELdkJZFFt_kgq7pfBOGwP6eQvXN8GdbyhrwSsAz-_jilUAky7VADpotJqAtFhRpbS6UXFuQgjSqdM7Ki0zuqTqDLVeUknTPjEkN2HMoGoDLubMI5ZvFUheHdqD_1XPWNIv-U7ZlFWZxZFcThYSzB8sdI7dUoYfNexmm2lMXUuJT5RmBk3DujBfhkeAAqJGl1HFG6wUveCZbfR4sak8NDDN-5Rv3c2tDIVaBlduP0n9SqSw5Q9hj-a1_FeZb2cug9lNxNinKH7Wed-BT4OoEEaxdfSHJZc33dLOlM17aB66bg1a5I-hCA2X4q2CSxerv0VpS1OwO40ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd67bb941.mp4?token=AGkoXMd_dJQELdkJZFFt_kgq7pfBOGwP6eQvXN8GdbyhrwSsAz-_jilUAky7VADpotJqAtFhRpbS6UXFuQgjSqdM7Ki0zuqTqDLVeUknTPjEkN2HMoGoDLubMI5ZvFUheHdqD_1XPWNIv-U7ZlFWZxZFcThYSzB8sdI7dUoYfNexmm2lMXUuJT5RmBk3DujBfhkeAAqJGl1HFG6wUveCZbfR4sak8NDDN-5Rv3c2tDIVaBlduP0n9SqSw5Q9hj-a1_FeZb2cug9lNxNinKH7Wed-BT4OoEEaxdfSHJZc33dLOlM17aB66bg1a5I-hCA2X4q2CSxerv0VpS1OwO40ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه اصلی ویدی منتشر شد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21048" target="_blank">📅 16:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/057d64cb85.mp4?token=CMe8Lq3CTaS78TdeRgkG9zBOdkjNDJSZMIew_0uuJK4w_G6AiPeU608u-RbqWoS4YKaSVo-RQIm2mj8a5UNlNRUCEljzkdKPxGicT2jnm25uPj-0WnJwv6kGygrAcERWqP-QtIxX6yDbAfpKZAy0KI4bDBcsUehlUDxQMBFBHaaLvoszrzl1MlzDZnYzWHcOY4QMbkJxTU_pVr2t47ZR1x38N05Ug2qbxdUSbfEm8n8xBWfe1lnbVDxEGZrGMvU3w3G4u2hXlPd3tdr2iKPFU5qHaIk8-pwT9ySXrWrDUOJ8owE9S5ubRJA4XjttvXXNKE595WWKszqvws2grG_avw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/057d64cb85.mp4?token=CMe8Lq3CTaS78TdeRgkG9zBOdkjNDJSZMIew_0uuJK4w_G6AiPeU608u-RbqWoS4YKaSVo-RQIm2mj8a5UNlNRUCEljzkdKPxGicT2jnm25uPj-0WnJwv6kGygrAcERWqP-QtIxX6yDbAfpKZAy0KI4bDBcsUehlUDxQMBFBHaaLvoszrzl1MlzDZnYzWHcOY4QMbkJxTU_pVr2t47ZR1x38N05Ug2qbxdUSbfEm8n8xBWfe1lnbVDxEGZrGMvU3w3G4u2hXlPd3tdr2iKPFU5qHaIk8-pwT9ySXrWrDUOJ8owE9S5ubRJA4XjttvXXNKE595WWKszqvws2grG_avw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان رژیم ویدئویی با عنوان «دیدار رئیس جمهور مسعود پزشکیان و مجتبی خامنه‌ای»، رهبر ایران منتشر کردند.
@WarRoom
یاشار : شک نکنید فیکه اگه اصل‌ بود فارس اینا میدادن بیرون نه اینکه یه پیج مداحی تا الان منبع اصلی باشه !</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21047" target="_blank">📅 16:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21046">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فرمانده کل ارتش: تنگه مقدس هرمز یکی از لازمه‌های خاتمه جنگ است؛ با همه توان حفظش می‌کنیم
سرلشکر حاتمی:این اهرم یکی از لازمه‌های خاتمه جنگ، به نحوی است که سایه جنگ از سر ایران برداشته شود.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21046" target="_blank">📅 16:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21045">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ادعای اکسیوس: ترامپ از طریق بارزانی با سپاه تماس می‌گرفت
مقامات دولت ترامپ کاری غیرمتعارف انجام دادند آنها مذاکره‌کنندگان ایران را دور زدند و مستقیماً با رهبری سپاه تماس گرفتند.
فردی که آنها برای کانال ارتباطی انتخاب کردند، نچیروان بارزانی، رئیس منطقه کردستان عراق بود که چیزی داشت که کمتر کسی دارد؛ اعتماد رهبران ایالات متحده و سپاه.
بارزانی در طول جنگ ایران و عراق در ایران زندگی می‌کرد و در دانشگاه تهران تحصیل می‌کرد.
او به زبان فارسی مسلط است و روابط شخصی با بسیاری از اعضای ارشد ایران، از جمله اعضای ارشد سپاه پاسداران دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21045" target="_blank">📅 13:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نیویورک‌تایمز: جنگ آمریکا با ایران وارد مرحله‌ای اقتصادی شده است؛ واشنگتن در کنار فشار نظامی، تلاش می‌کند با ضربه زدن به درآمدهای نفتی و منابع مالی جمهوری اسلامی، توان تهران برای ادامه جنگ و تأمین هزینه‌های آن را کاهش دهد. این رویکرد یادآور سیاست فشار اقتصادی سال‌های گذشته است که هدفش وادار کردن ایران به محدود کردن برنامه هسته‌ای و بازگشت به مذاکره بود. گزارش می‌گوید این فشار اقتصادی می‌تواند برای آمریکا یک اهرم مهم در مذاکرات آینده باشد، هرچند تجربه گذشته نشان داده که تحریم‌ها به‌تنهایی الزاماً ایران را وادار به تغییر سیاست نکرده‌اند. در نتیجه، مسئله اصلی اکنون این است که آیا فشار اقتصادی همراه با حمله نظامی می‌تواند کار آمد باشد یا نه
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21044" target="_blank">📅 13:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسکای‌نیوز در گزارشی افشا کرده بیش از ۱٬۳۰۰ کاربر استراوا (اپلیکیشن ثبت و اشتراک‌گذاری فعالیت‌های ورزشی و موقعیت مکانی) از پایگاه‌های نظامی آمریکا در خاورمیانه اطلاعات منتشر کرده‌اند؛ اطلاعاتی که مسیر رفت‌وآمد، برنامه روزانه و جابه‌جایی نیروها را آشکار می‌کرد.
کارشناسان امنیتی می‌گویند ایران می‌توانسته این داده‌ها را در کنار اطلاعات دیگر برای رصد نیروهای آمریکایی و شناسایی اهداف استفاده کند. در مواردی در
بحرین و اردن
، تغییر فعالیت‌های ثبت‌شده ظاهراً جابه‌جایی نیروها را نشان داده و مناطقی که این افراد در آن حضور داشتند، بعداً هدف حمله ایران قرار گرفته‌اند. پنتاگون از سال
۲۰۱۸
درباره خطر چنین اطلاعاتی هشدار داده بود و این مشکل همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21043" target="_blank">📅 12:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29877262ff.mp4?token=cUupUiYaHSzCvawdRrzKOd7-oDeGJ2eg0rO7Q2jtReCJoeZKtrXeDLzlJPMFv9ZKoWDpmnhjpd8tTKXlMi66J2Uo95YHn5bUb9nD9pensgkcPMBuWD4aqHebORBX16YmEMR_nj6KsIIFlWN0AjvNI8Vff-ABLm97eLWLwVW2VM-fSItSlLGR6n0qT6vGCLLF8fbMe_GxWfu0nkK8n8fWmqP8msc_C0paGUrX06JTqv9mM_hfhw6_9A6Q4x_N-zIUrmgHr17S8H4d3HChYvTBmw65YSSqXKkWJIT5v4OP0pnh1BS-qJ1NM3BWotV03YCnqxCX0qXNPlh0HbxVQPEhtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29877262ff.mp4?token=cUupUiYaHSzCvawdRrzKOd7-oDeGJ2eg0rO7Q2jtReCJoeZKtrXeDLzlJPMFv9ZKoWDpmnhjpd8tTKXlMi66J2Uo95YHn5bUb9nD9pensgkcPMBuWD4aqHebORBX16YmEMR_nj6KsIIFlWN0AjvNI8Vff-ABLm97eLWLwVW2VM-fSItSlLGR6n0qT6vGCLLF8fbMe_GxWfu0nkK8n8fWmqP8msc_C0paGUrX06JTqv9mM_hfhw6_9A6Q4x_N-zIUrmgHr17S8H4d3HChYvTBmw65YSSqXKkWJIT5v4OP0pnh1BS-qJ1NM3BWotV03YCnqxCX0qXNPlh0HbxVQPEhtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : پاملا براون گزارشگر سی‌ان‌ان، همین یک ماه پیش در ناو هواپیمابر آبراهام لینکلن حضور داشت و آنها حتی هنگام بازدید از کشتی بستنی هم خوردند و بسیار شاد بودند ! با توجه به این که پنج روز قبل از شروع جنگ ۴۰ روزه و کشته شدن علی خامنه‌ای، خبری پخش شده بود که ناو جرال فورد مشکل توالت و حمام دارد و تمام کارکنان بسیار ناراضی هستند و شرایط خیلی بدی دارند. اکنون با تکرار همان الگو، ممکن است این بار هم یک استراتژی برای حمله دوباره باشد…
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21042" target="_blank">📅 11:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کاخ سفید : موشک کافی برای ادامه جنگ با ایران داریم
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21041" target="_blank">📅 11:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ستادکل نیروهای مسلح: تا شکست کامل دشمنان آمریکایی اسرائیلی در منطقه و احقاق حق ملت قهرمان ایران و تسلیم دشمن، از خواست مشروع مردم و مطالبات رهبر عزیزمان، در برابر آمریکای متجاوز کوتاه نخواهیم آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21040" target="_blank">📅 10:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">منم مشکلات زیادی دارم ولی برای شما شاد هستم
😍
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21039" target="_blank">📅 10:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رویترز⁠ گزارش داده که حزب «یاشار!» به رهبری گادی آیزنکوت، ژنرال پیشین و رئیس سابق ستاد ارتش اسرائیل، با شعار مبارزه با فساد و تغییر مسیر سیاسی اسرائیل شکل گرفته است. نام
«یاشار» (ישר)
در عبری به معنای
«راست، مستقیم و درستکار»
است و ارتباطی با نام ترکی «Yaşar» ندارد. انتخاب این نام نیز حامل یک پیام سیاسی است: معرفی حزب به‌عنوان جریانی که می‌خواهد «مستقیم و درست» عمل کند. آیزنکوت از چهره‌های بسیار سختگیر در برابر جمهوری اسلامی و تهدیدهای امنیتی منطقه است,
یاشار در نظرسنجی‌های اخیر به لیکود نتانیاهو نزدیک شده و حتی در برخی نظرسنجی‌ها جلو افتاده است.
رویترز آیزنکوت را یکی از جدی‌ترین رقبای نتانیاهو معرفی کرده و گزارش کرده که حزب او توان بالقوه تشکیل ائتلاف گسترده‌تری نسبت به لیکود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21038" target="_blank">📅 10:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏مارک لوین به وعده خود عمل کرد و نظر سنجی‌را  انتشار داد و گفت : ‏بر اساس یک نظرسنجی اخیر (۱۰ اوت) که توسط تنها نظرسنجی‌کننده‌ای انجام شده که دو دوره انتخاباتی اخیر را درست پیش‌بینی کرده بود، حزب لیکود نتانیاهو پیش‌بینی می‌شود ۳۳ کرسی در کنست به دست آورد و…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21034" target="_blank">📅 10:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21032">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suwytoz9dtIClxYYjL3CDrje-FtLRvmCQyPEa87TMt2cf83zFPtW24dmBUGrfENnu0RwLAazsOXSblVup1z-aSWu1m_oxG2oyvY9QrAHIDekRSLcHY9CyLzKe0DZ18N_QhD_kV-QFUloFx6dbr1KXzbMZLpIiSOB_dZFVvah-JLL0F88RoW4wQowksIApdX95fkDE7c5Gm759I9DqdfaEk2kYAEFXxyXZ__zKE9tB7pBfQTw5h6MROqa_rQAQNIlUSXRt53PtHzA0l2bLPPHZN0NMb-cY4IKklM5TP-cWX61rIcwYfpmI5t727-w-XCMLlDU-DpYkRUrm-ZgiZP7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : من قویاً معتقدم که پرزیدنت ترامپ باید از نتانیاهو حمایت کند، چون در مقطعی برای ادامه مقابله با ایران به او نیاز خواهد داشت. به احتمال زیاد، نتانیاهو در هر صورت پیروز خواهد شد. اما بر اساس اطلاعات منابع من، در دیدار آنها هیچ توطئه یا زدوبندی در…</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21032" target="_blank">📅 09:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21031">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مانوک : رژیم پاشیده
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21031" target="_blank">📅 09:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21030">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b22325bf.mp4?token=KUQAOrVBxbVbJcYVVHTb9c79ZL_00heL7FgZuBRvHT1hFOJ7UvlgNmJmfBMOcYLGTyE-oW15R59lqWIFenSHn7-aEyrB9D1Jqdx0JhnkrmOzB2_C7j6BD7MuaShuNVjpo9EWuoE8mwr0tGJIybRUxCend3JaxdyRNdS2fei2kYasuhmGN_gmVrI0FVjRbsoRIOE-T2IeJLuJsH1arRWPLJ2GdOvft5AkXy52NoEE-yFRmIn25eXi-8iDfEC59FJcnW5fIL_qE4To-N2nb0XmzqStg0EWrVYWv7zaqxEzNu-QH3LDSevsjvWF6uilIKwvmyHVRoyGBW8iSbyWILS1sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b22325bf.mp4?token=KUQAOrVBxbVbJcYVVHTb9c79ZL_00heL7FgZuBRvHT1hFOJ7UvlgNmJmfBMOcYLGTyE-oW15R59lqWIFenSHn7-aEyrB9D1Jqdx0JhnkrmOzB2_C7j6BD7MuaShuNVjpo9EWuoE8mwr0tGJIybRUxCend3JaxdyRNdS2fei2kYasuhmGN_gmVrI0FVjRbsoRIOE-T2IeJLuJsH1arRWPLJ2GdOvft5AkXy52NoEE-yFRmIn25eXi-8iDfEC59FJcnW5fIL_qE4To-N2nb0XmzqStg0EWrVYWv7zaqxEzNu-QH3LDSevsjvWF6uilIKwvmyHVRoyGBW8iSbyWILS1sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز با دسترسی نادر به یک پایگاه ارتش اسرائیل، مجموعه بزرگی از سلاح‌های ضبط‌شده از حماس و حزب‌الله را به نمایش گذاشته است؛ مجموعه‌ای شامل راکت، پهپاد، خمپاره، موشک ضدزره، تفنگ تک‌تیرانداز و مسلسل. به گفته اسرائیل، بخشی از این تسلیحات ساخت ایران است و سلاح‌هایی از روسیه و چین نیز در میان آنها دیده می‌شود؛ حتی یک مسلسل آلمان نازی
MG34 مربوط به جنگ جهانی دوم
نیز در این انبار وجود دارد. این مجموعه تصویری از گستردگی و تنوع تسلیحاتی را نشان می‌دهد که اسرائیل می‌گوید از گروه‌های مورد حمایت ایران از زمان ۷ اکتبر کشف و ضبط کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21030" target="_blank">📅 09:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21029">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرگزاری قوه قضائیه : شهرام صادقی که در ۱۸ دی ماه پس از حمله به مامورین با خودروی پراید ۷ مامور را زیر گرفت به اتهام اقدام عملیاتی به نفع اسرائیل و آمریکا، بعد از اذان صبح امروز، حکم وی اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21029" target="_blank">📅 08:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21027">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سنتکام :
فرمانده سنتکام پس از سفری ۱۰ روزه به خاورمیانه بازگشت.
دریادار
برد کوپر
در این سفر به
بحرین، عراق، اسرائیل، اردن، عربستان سعودی و امارات
رفت و با مقام‌های ارشد سیاسی و نظامی این کشورها دیدار کرد و همچنین از نیروهای آمریکایی مستقر در منطقه بازدید داشت؛ سنتکام می‌گوید بیش از
۵۰ هزار نیروی آمریکایی
در خاورمیانه مشغول مأموریت هستند. کوپر در جریان سفر خود همچنین برای دومین بار در سال جاری از ناو هواپیمابر
USS Abraham Lincoln
در دریای عرب بازدید کرد. سنتکام اعلام کرده این ناوگروه تاکنون
هزاران پرواز رزمی
در پشتیبانی از عملیات «Epic Fury»، مأموریت‌های امنیت منطقه‌ای و
محاصره دریایی آمریکا علیه ایران
انجام داده است. کوپر درباره استقرار آبراهام لینکلن گفت این مأموریت از نظر شدت و پیامدهای عملیاتی، یکی از مهم‌ترین مأموریت‌های دوران مدرن بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21027" target="_blank">📅 07:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عراقچی می‌گوید اساساً چیزی به نام
«آتش‌بس ۶۰روزه برای تمدید
بعد از نقض آن توسط آمریکا
وجود ندارد»
و تفاهم اسلام‌آباد از نگاه ایران
پایان جنگ بوده، نه آتش‌بس ۶۰روزه
. با این حال، اگر مبنا را همان دوره ۶۰روزه و پایان آن در
۱۷ اوت
بگیریم، با فرض ساعت ۰۰:۰۰ واشنگتن، موعد پایان آن در ایران
ساعت ۷:۳۰ صبح ؛ یکشنبه
(اگر مبنا آغاز روز) و
دوشنبه ۲۶ مرداد
(اگر مبنا پایان روز) باشد پایان میابد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/21026" target="_blank">📅 23:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قطر ادعای ایران دربارهٔ به اسارت گرفته شدن سه خلبان ایرانی توسط این کشور را قاطعانه تکذیب کرد
و گفت تهران تاکنون به دعوت دوحه برای اعزام هیئتی به قطر و بررسی جزئیات عملیات جست‌وجو و نجات پاسخ نداده است.
سوخو-۲۴ ایران روز ۱۱ اسفند ۱۴۰۴ برای انجام مأموریتی علیه یک پایگاه نظامی در قطر اعزام شدند و هنگام بازگشت هدف پدافند قرار گرفتند.
بر اساس روایت ایران، چهار خلبان این دو جنگنده اجکت کردند که یکی از آن‌ها، مجید کاظمی، کشته شد و سه نفر دیگر به نام‌های جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان «زنده توسط نیروهای قطری به اسارت گرفته شدند».
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/21025" target="_blank">📅 22:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21024">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دیدبان اتاق جنگ : سیریک هرشب قبل اینکه بزنن یک ساعت برق قطع میکنن بعد که وصل کردن شروع میکنن شلیک
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/21024" target="_blank">📅 22:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21023">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش صدای ۳ انفجار/شلیک در‌ سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/21023" target="_blank">📅 22:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏دونالد ترامپ در تروث‌سوشال ویدیویی را منتشر کرد که در آن بهنام طالب‌لو، مدیر ارشد برنامه ایران در بنیاد دفاع از دموکراسی‌ها، بر تاثیر محاصره دریایی آمریکا در کاهش صادرات نفت ایران تاکید کرده و می‌گوید محدود کردن حکومت ایران از نظر بودجه‌ای پس از پایان درگیری‌ها، در کنار محاصره، به آمریکا اجازه می‌دهد از دلار به‌عنوان یک سلاح استفاده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/21022" target="_blank">📅 22:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21021">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/21021" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21020">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اندی بیکر، یکی از نزدیک‌ترین چهره‌های امنیتی به جی‌دی ونس، در هفته‌های آینده کاخ سفید را ترک می‌کند.
بیکر که سال‌ها مشاور امنیت ملی ونس بوده و در دولت ترامپ نیز در تصمیم‌گیری‌های مهم سیاست خارجی و امنیت ملی نقش داشته،
مستقیماً در مذاکرات آمریکا و ایران حضور داشت
و به جناح مخالف جنگ شناخته می‌شد.  خروج او در حالی رخ می‌دهد که جنگ ایران همچنان موضوعی حساس است؛ هرچند دلیل رسمی برای رفتنش، تمایل به وقت بیشتر با خانواده و سرمایه گزاری های شخصی عنوان شده ، همچنین
در مورد شایعه افشای اطلاعات محرمانه نیز اتهام مستندی علیه بیکر منتشر نشده، اما با توجه به دسترسی او به پرونده‌های حساس و نقش مستقیمش در مذاکرات، این گمانه‌زنی درباره علت واقعی خروجش مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/21020" target="_blank">📅 19:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21019">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مارک لوین : من قویاً معتقدم که پرزیدنت ترامپ باید از نتانیاهو حمایت کند، چون در مقطعی برای ادامه مقابله با ایران به او نیاز خواهد داشت. به احتمال زیاد، نتانیاهو در هر صورت پیروز خواهد شد. اما بر اساس اطلاعات منابع من، در دیدار آنها هیچ توطئه یا زدوبندی در کار نبوده است. آکسیوس این گزارش‌های منفی را با هدف تأثیرگذاری بر سیاست‌گذاری و انتخابات اسرائیل، از دیدگاهی چپ‌گرایانه و افراطی، در زمان‌بندی خاصی منتشر می‌کند.
همچنین نتانیاهو بر اساس آخرین نظرسنجی‌ای که در انتخابات قبلی واقعاً نتیجه را درست پیش‌بینی کرده بود، وضعیت خوبی دارد. آن نظرسنجی را پیدا می‌کنم و جداگانه منتشر خواهم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/21019" target="_blank">📅 19:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21018">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بیانیه دفتر نتانیاهو : امروز صبح، حزب‌الله توافق آتش‌بس در لبنان را نقض کرد، زمانی که به سربازان ما در منطقه امنیتی که از شهرک‌های اسرائیلی واقع در نزدیکی مرز محافظت می‌کند، حمله کرد. در این حمله، سه تن از سربازان ما به شدت مجروح شدند. ارتش اسرائیل با بمباران مقر فرماندهی حزب‌الله که دستور حمله را صادر کرده بود، پاسخ داد
…
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/21018" target="_blank">📅 18:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21017">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">واشنگتن پست : هیچ توافق خوب و قابل‌قبولی با ایران نمی‌توان منعقد کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/21017" target="_blank">📅 17:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21016">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اردوغان به شبکه الجزیره: اولویت ما بازگشایی تنگه هرمز است، زیرا ادامه بسته بودن آن به نفع هیچ‌کس نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/21016" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21015">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ستاد کل نیروهای مسلح ایران اعلام کرده است سه خلبان ایرانی به نام‌های
جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان
که در جریان حملات اسفندماه جنگنده‌های سوخو-۲۴ آنها سقوط کرده، زنده مانده و حدود شش ماه است در
قطر به اسارت نیروهای قطری
درآمده‌اند. محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین، گفته این خلبانان هنگام بازگشت از یک مأموریت رزمی پس از هدف قرار گرفتن جنگنده‌ها توسط پدافند، اجکت کرده‌اند. او با استناد به کنوانسیون سوم ژنو خواستار دسترسی کمیته بین‌المللی صلیب سرخ به آنها شده و گفته قطر تاکنون اجازه تماس یا دیدار خلبانان با خانواده‌ها و مقام‌های ایرانی را نداده است.
قطر تاکنون به این ادعا واکنش رسمی نشان نداده است
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/21015" target="_blank">📅 16:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH7dZqG-hdVnE8hjdbBgi_qX3vB8JEftyziIT8mdcYOW3whfBr4dzOzlOxTgbPDeNLhQxnCn8WFD7EEkT7LHx657bzIyeB1khzDHd02CuZdNxdpEiyLogaKXE7krvB0yujE0Dg6nWhn929OoHAIMFLfKJx5oRXviMYeN5i5VAusDPPJgViNc-NQMTUDn7Q7_dX-pCNp08_EAfyg003RztushIr6bfD9pLESTeo3sbvVrZqQmIjbhBsmzxCLbrQK-0thywFWYxb0EPjzhX9UJS4qVV3DedpEsknqgfZA8QgACd8VdCeBsdWjC3WtS0uWEEAnAKA5HJR2VQ0oRMU7Big.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : اندازه هواپیما هایی که ما در اتاق جنگ زیاد سروکار داریم
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/21014" target="_blank">📅 15:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21013" target="_blank">📅 14:15 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
