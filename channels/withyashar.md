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
<img src="https://cdn4.telesco.pe/file/qGMXDaoF75qI9a-zqKD5k1Yk2Gncm4-ShobwB9pMgJz8dR9sR3eSf3Tr-0cRkU8622HrG5LLsjevrEzRR0fcmjfFPDkz8aLJWyYJCO_vw5UeXTaSVu7vnSE2RWzYDpRnwlQQ11zFJBuCz_VPUTynaOjegf2ul_6YOz6bLe7dqXGRm6zNiTzQhWrlAoS702TCM2n1fhN3NkS2xtRaWIkNotNpgymCN1ACIO_HIdvqpAsOp5fJcjSSBLHhopgHark9uKDA_NFUj0x6yQvaS_yERx2khFnTkflznojm-wukjpjfoD8FjnEfWsGNqEbwi9Vyb-GajYXgE-F7J6Pf9vUZ0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 435K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 06:17:17</div>
<hr>

<div class="tg-post" id="msg-20118">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">روزنامه تایمز : سیا و موساد دنبال پیدا کردن مجتبی خامنه‌ای هستن.
گفته میشه رهبر جدید زخمی شده و بالایِ 150 روزه که از هیچ وسیله الکترونیکی استفاده نکرده و احتمالاً تو یه پناهگاه زیرزمینی تو تهران یا اطراف قم مخفی شده. چون ردیابی از طریق شنود و ابزارهای الکترونیکی نتیجه نداده، سرویس‌های اطلاعاتی تمرکزشون ر‌ روی جاسوسیِ انسانی گذاشتن.
طبق ادعای مقام‌های سابق موساد، مجتبی خامنه‌ای پیام‌هاش رو از طریق چندین واسطه و نامه‌های دست‌نویس منتقل می‌کنه؛ پس تنها راه پیدا کردنش، نفوذ به حلقه نزدیکانشه. بعضی منابع اطلاعاتی احتمال میدن سپاه مرگِ مجتبی خامنه‌ای رو مخفی کرده باشه و بعضی دیگه میگن، ممکنه حکومت واسه گمراه کردن بقیه، از بدل استفاده کنه!
@WarRoom</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/withyashar/20118" target="_blank">📅 04:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20117">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a76d99f52.mp4?token=jTFP3JxF4_PHP8bbqaxT6JQmxy5fJaeoYvs-fv_rP5AgHOheKL_WI_HNf2ngDJr0NmMl_q7HkBgfVLHDMGDNRS8caSrenELhQkH08iYy6iE4cCV118H6gdGl1gsMu6IrwC6DGGUGQvDuMUe0VlWXM_w73_eGHkiRgZUhy3NYn9wV9pxRzhnq4i5NQPl6fmFd-XVUzLmGJ9pFkznkp0A_PTqjZA_zgN2ySBjQjv0w9C6hIhLnAv0tSHL6_3lBhIm6jfG0QCOYskaYaFeN7s-czmLv_3SxpfC4T4ZNQImjE7BFXNf_NbomxhZs6vC1h1IJstKbeLfba4nod9j2iN1ZFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a76d99f52.mp4?token=jTFP3JxF4_PHP8bbqaxT6JQmxy5fJaeoYvs-fv_rP5AgHOheKL_WI_HNf2ngDJr0NmMl_q7HkBgfVLHDMGDNRS8caSrenELhQkH08iYy6iE4cCV118H6gdGl1gsMu6IrwC6DGGUGQvDuMUe0VlWXM_w73_eGHkiRgZUhy3NYn9wV9pxRzhnq4i5NQPl6fmFd-XVUzLmGJ9pFkznkp0A_PTqjZA_zgN2ySBjQjv0w9C6hIhLnAv0tSHL6_3lBhIm6jfG0QCOYskaYaFeN7s-czmLv_3SxpfC4T4ZNQImjE7BFXNf_NbomxhZs6vC1h1IJstKbeLfba4nod9j2iN1ZFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای اخیر، چند شهر اسپانیا شاهد ناآرامی‌های مرتبط با مهاجرت بوده‌اند.
مهم‌ترین درگیری‌ها در شهر
توره پاچکو
در منطقه مورسیا، واقع در جنوب‌شرق اسپانیا، رخ داد. این ناآرامی‌ها پس از حمله به یک مرد سالمند و انتشار ادعاهایی درباره مهاجر بودن عاملان آغاز شد و به درگیری میان گروه‌های راست افراطی، مهاجران عمدتاً مراکشی و نیروهای پلیس انجامید. در این حوادث چندین نفر بازداشت و تعدادی نیز زخمی شدند.
هم‌زمان، در شهرهای مرزی
سئوتا
و
ملیلیا
در شمال آفریقا، که تحت حاکمیت اسپانیا هستند، تلاش هزاران مهاجر برای ورود به خاک اسپانیا باعث افزایش تدابیر امنیتی و تشدید تنش‌ها شده است
بخش قابل توجهی از مهاجرانی که تلاش می‌کنند وارد
سئوتا
و
ملیلیا
شونداز
مراکش
و برخی کشورهای مسلمان شمال و غرب آفریقا هستند
@WarRoom</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/20117" target="_blank">📅 04:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20116">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1e208199.mp4?token=FJuiitBOEVdnUa9b-EaBYBQLdVV817rcbYjUhZMMM-L-jvZ8eHNvL0KJ9P0aOqYGUL0dEXz7e368HeStLM1_roM3LRCNutbyIWTEYNLnDZt8RlLCXwvjDxqeyALtjnl1orTFp5baNtXvroZ87c395b9wpV__ZEuj4k5kFFOsAgcV058eLCCEG4uiQfB5vV4dRKKB4Mqafbt4lKTCIPgvcj9-Bgm4uu8oHe97eL2Omn5xV5ionAb9d4z_SrlOA57EjtO_5iio0R97ss06JEVWJZa3nk8kp--qLkNV7cMC15z0w4XGz7fVXwZBbGNF4nXkdMNQY74UP2Saf21jFuffbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1e208199.mp4?token=FJuiitBOEVdnUa9b-EaBYBQLdVV817rcbYjUhZMMM-L-jvZ8eHNvL0KJ9P0aOqYGUL0dEXz7e368HeStLM1_roM3LRCNutbyIWTEYNLnDZt8RlLCXwvjDxqeyALtjnl1orTFp5baNtXvroZ87c395b9wpV__ZEuj4k5kFFOsAgcV058eLCCEG4uiQfB5vV4dRKKB4Mqafbt4lKTCIPgvcj9-Bgm4uu8oHe97eL2Omn5xV5ionAb9d4z_SrlOA57EjtO_5iio0R97ss06JEVWJZa3nk8kp--qLkNV7cMC15z0w4XGz7fVXwZBbGNF4nXkdMNQY74UP2Saf21jFuffbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون حملات پهپادی مستمر به پایگاه‌های گروه‌های کورد مخالف رژیم ایران در اربیل
@WarRoom</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/20116" target="_blank">📅 03:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20115">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apItdsmCotKSsK3mVPQDfFLPCdFIGiOllqk0m_jmHqGZcSQBE_rAu2IsEVgRysPWDUh3_t77idr2HbrPeQ9QeUJUt6oJeaX2LliYALNZshrdExaBBaPM6py6qJjdHwkLt8pw1DJ9jFhuyUm2lr81hVGep7XYmgEQ47PicQwVNASzrhPQuSwsBfh2D294rVmF1YRXRerglH-SJxLXl0oVGk2AylqGeJbCKtK7ANaHQKdwBFxGFaA8L0Qhvjc1cdD_-G-WaPAptWPOKscwZdlZ00J7WkpGSOwMGS6gwj_Jj9AMk3Zqf5oYvpr4gQT8LgOweHEPT1NZsZdAcUFvJkqodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مدعی شد توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه حاصل شده است. به گفته او، این توافق به‌صورت مرحله‌ای اجرا خواهد شد و پس از تکمیل خلع سلاح، نیروهای اسرائیلی از غزه خارج شده و اداره این منطقه به یک دولت جدید فلسطینی با حمایت یک نیروی بین‌المللی و پلیس جدید فلسطینی واگذار می‌شود. ترامپ همچنین از مصر، قطر و ترکیه به‌عنوان میانجی‌های این توافق قدردانی کرد و آن را گامی مهم در جهت صلح و امنیت پایدار دانست.
@WarRoom</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/20115" target="_blank">📅 03:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20114">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ممباقر : حمله تروریستی به منازل مسکونی غیرنظامیان در جزیره قشم، ادامه جنایت در میناب و لامرد است.
امریکایی‌ها عادت کردن که سیلی‌هایی که در میدان نبرد می‌خورن رو با ریختن خون بی‌گناهان جبران کنند؛ تاوان خواهند داد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20114" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K27Y0uxZvbp_rLwJFfpAP9Hepjuot_CrWRX7NCKXnj3BV_xvQRK-Ithi_ORGUSJ-poIpagLGA7dQrMOvwlL5-y-TY6yGYSMDdmPFUF6t01MmjpIZQ79QqqZC_x2qoiyaJ3V4NavWVlaEiiZJ98iwOlccANQSN9XCCwmECY1VctD2s9HIGKZhvbE48lQi8URXqzVzgrCeg_hHk1oEfBYDAJgJJhWv-vCCW_BpthqHaVsSd0zvQZptNSZfglQUtXB59NBaMbo76usTYvpadU679PcC-A932826L51fIuu-_SKDrts2rsLhnjXwOnSmJPkmPjv071TCR6bdQPwfS9gZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : حوادث ۲۴ ساعت گذشته:
حملات آمریکا به ایران: آبادان، اهواز، شادگان و اروندکنار: شلیک موشک‌های HIMARS؛ کازرون و پراش‌بند در فارس: حمله هوایی بدون گزارش تلفات؛ بوشهر و کیش: گزارش انفجار؛ قشم: حمله به یک خانه و کشته شدن دو ۳ نفر
حملات ایران به پایگاه‌های آمریکایی: پایگاه موافق‌السلتی در اردن: طبق ادعای ایران که آکریکا تکذیب کرده، ۳ فروند F-35 نابود و ۳ فروند دیگر آسیب دیدند و تعدادی از نیروهای آمریکایی کشته شدند؛ پایگاه علی‌السلام در کویت: دو انبار پهپاد و مخازن سوخت هواپیما و هلیکوپترها آسیب دیدند.
در عرصه دریایی: در تنگه هرمز، دو کشتی هنگام عبور با حادثه روبه‌رو شدند؛ در یکی آتش‌سوزی بزرگی رخ داد و هر دو بازگشتند. همچنین یک تانکر LNG قطری برای نخستین بار در سه هفته گذشته از مسیر تأییدشده ایران عبور کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20113" target="_blank">📅 23:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">جمهوری اسلامی یک موج جدید از حملات موشک/پهپاد را به بحرین آغاز کرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20112" target="_blank">📅 22:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا نام یک فرد و ۵ شرکت مرتبط با شرکت هواپیمایی ماهان را در فهرست تحریم‌ها قرار داده است.
بسنت، وزیر خزانه‌داری آمریکا :
هر کسی به سپاه یا ماهان‌ایر خدمات مالی، لجستیکی یا تجاری بده، به حفظ یک سازمان تروریستی کمک کرده
ما این افراد و شرکت‌ها رو شناسایی می‌کنیم، معرفی می‌کنیم و دسترسی‌شان رو به سیستم مالی آمریکا قطع می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20111" target="_blank">📅 21:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ارتش رژیم جمهوری اسلامی :
پایگاه شیخ عیسی در بحرین را با پهپاد هدف قرار دادیم
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20110" target="_blank">📅 21:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لیست کشورهایی که اعلام کرده‌اند از ائتلاف دریایی عربستان برای حفاظت از کشتیرانی در دریای سرخ حمایت می‌کنند، به گفته عربستان  آن‌ها به این ائتلاف پیوسته‌اند :
کویت، بحرین، قطر، اردن، مصر، یمن، ترکیه، پاکستان، بنگلادش، سودان، جیبوتی، سومالی و نیجریه.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20109" target="_blank">📅 21:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">روند خلع سلاح حماس : ایالات متحده تمایل دارد پیشنهاد حماس مبنی بر تفکیک سلاح‌های سنگین و سبک در فرآیند "غیر مسلح کردن" این سازمان تروریستی را بپذیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20108" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شبکه i24 پیام اسرائیل به آمریکا:
بدون یک اقدام نظامی "معنادار" در ایران، تغییری حاصل نخواهد شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20107" target="_blank">📅 21:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8772ccba1.mp4?token=Ik5fmdVipf4E56Tz4mTRgCDc5pabCnKP3vd26GEFhg6sAcYyFh_JflXkg1d66JoATgt9fTp_mZM3w74ZwdaMCv-gBIVXB_2HmbWIdoQqLZmV-cSL10gIsDbBln6j8FEBBUIF8G5sDDOgdQowoeB2Y_37Ec_jdzlfnLi_vgFwc-KN_usTxjVYuG-Oq3F5c1YGIY2tjVVRmXOOgyYGE2LcaBel1oLyUa75LV6Yz8sHZi5Gv-L3ZUx-5YAlcEgPmzpzmld2OXdtz6-xgBskafk_YN2ZAkZrWB305v31FuLX_-SIAy8chKxGsF0JVJkLs25rQ1YvVrcFVVg2TsLowZrg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8772ccba1.mp4?token=Ik5fmdVipf4E56Tz4mTRgCDc5pabCnKP3vd26GEFhg6sAcYyFh_JflXkg1d66JoATgt9fTp_mZM3w74ZwdaMCv-gBIVXB_2HmbWIdoQqLZmV-cSL10gIsDbBln6j8FEBBUIF8G5sDDOgdQowoeB2Y_37Ec_jdzlfnLi_vgFwc-KN_usTxjVYuG-Oq3F5c1YGIY2tjVVRmXOOgyYGE2LcaBel1oLyUa75LV6Yz8sHZi5Gv-L3ZUx-5YAlcEgPmzpzmld2OXdtz6-xgBskafk_YN2ZAkZrWB305v31FuLX_-SIAy8chKxGsF0JVJkLs25rQ1YvVrcFVVg2TsLowZrg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنای آمریکا با
۵۰ رأی مخالف
در برابر ۴۹ رأی موافق
طرح محدود کردن اختیارات ترامپ برای اقدام نظامی علیه ایران رو رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20106" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رویترز به نقل از مقام‌های فدرال و ایالتی آمریکا گزارش داد که بازرسان در حال حاضر احتمال می‌دهند هکرهای مرتبط با ایران مسئول حمله سایبری هماهنگ به سامانه‌های آب شهری در ایالت مینه‌سوتا باشند، اما تأکید کرده‌اند که هنوز به نتیجه‌گیری قطعی نرسیده‌اند و تحقیقات ادامه دارد. به گفته این مقام‌ها، این احتمال نیز وجود دارد که مهاجمان برای افزایش تنش‌ها، خود را به جای هکرهای ایرانی معرفی کرده باشند. در این حمله بیش از ۳۰ سامانه آب شهری هدف قرار گرفت، دست‌کم یک چاه و یک تأسیسات تصفیه آب به‌طور موقت از مدار خارج شد و چندین سامانه نیز به کنترل دستی منتقل شدند، اما مقام‌ها اعلام کردند که کیفیت آب آشامیدنی تحت تأثیر قرار نگرفته و هیچ موردی از آلودگی آب گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20105" target="_blank">📅 20:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو : ممدانی، شهردار نیویورک، ایران و حزب الله و حماس رو حمایت می کنه!
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20104" target="_blank">📅 19:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رویترز، با استناد به دو مقام در غرب آسیا، گزارش داد که انصارالله این هفته از خاک عراق و با هماهنگی گروه‌های مسلح عراقی و نظارت از سوی سپاه ، به عربستان سعودی حمله کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20103" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سنتکام ادعای ایران مبنی بر انهدام سه فروند جنگنده رادارگریز اف-۳۵ لایتنینگ ۲ در پایگاه هوایی موفق سالتی، اردن را تکذیب کرد؛ و ادعای رسانه‌های ایرانی مبنی بر اینکه نفتکش ام/تی نورا محاصره آمریکا را شکسته است را نیز رد کرد.
سنتکام همچنین بار دیگر ادعا کرده است که تهدید اصلی برای کشتیرانی تجاری در تنگه هرمز، رژیم ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20102" target="_blank">📅 19:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش وقوع چندین انفجار در صنعا ، یمن
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20101" target="_blank">📅 18:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">«فاکس نیوز»: همکنون دولت آمریکا گزینه‌های انجام عملیات نظامی گسترده علیه ایران را به ترامپ ارائه داد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20100" target="_blank">📅 17:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Bitcoin : 65000$
Tether : 193000T
Brent oil :91.5$
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20099" target="_blank">📅 17:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اواخر شب گذشته، دو فروند بمب‌افکن B-1B Lancer با شناسه‌های LANE90/91 از پایگاه RAF Fairford برای یک مأموریت آموزشی کوتاه بر فراز سواحل جنوب‌غربی بریتانیا به پرواز درآمدند و با پشتیبانی هواپیمای سوخت‌رسان CLEAN71 عملیات را آغاز کردند. این بمب‌افکن‌ها سپس برای تعویض خدمه به فرفورد بازگشتند و حدود ساعت ۰۱:۴۵ بامداد با شناسه‌های HARPO40/41 دوباره به پرواز درآمدند تا با سه فروند هواپیمای سوخت‌رسان CLEAN91، CLEAN92 و CLEAN93 از پایگاه Lajes تمرین سوخت‌گیری هوایی انجام دهند. به نظر می‌رسد این تمرین، شبیه‌سازی سناریوی عدم دسترسی به حریم هوایی فرانسه و پرواز به سمت ایران از مسیر جبل‌الطارق بوده؛ مسیری که پیش‌تر در عملیات Operation Epic Fury نیز استفاده شده بود. این مأموریت حدود ساعت ۰۴:۱۵ بامداد با بازگشت بمب‌افکن‌ها به RAF Fairford و هواپیماهای سوخت‌رسان به Lajes پایان یافت
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20098" target="_blank">📅 16:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20097">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfpUjydJSryPcLB5z7TPuI4x4CnP665E6sB2MsXcIgCHCbC34YurdjS1qRQl0p16Tf9cWwzQCbjWF-0AxhvM7-F5aeF7ikYeofZ11k2JONxkxhvr4chIrFUyHs4f5QZn3IYcGUUSl_-f0azbT1_gB6xpskvZLzQQYDuUWfEkgKDot6xPqksqseggK-Y8yHeKSxe4DUUz_5wgVwQaTZFNifOWckMfA12eQ3l3sanETwtusDsmIfapuQ53vi9mwEsqWvoDsj5EvYMdoP4KLmrzBRc5QKcdPANBRZ0T6_r_ib_3LqCqMZnkk2QghjdpkgnOyqkhCtoTJhckvzJ_JItd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۳ تا از کثافتهای رسما گی حشدالشعبی که در حمله عربستان کشته شدند (عکس رسمی) همین افراد دی ماه در ایران قتلعام کردند. @WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20097" target="_blank">📅 16:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20096">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش کانال ۱۴ : درون کوه کلنگ گزلا - مستحکم‌ترین سایت هسته‌ای ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20096" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20095">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اکسیوس : چین با ۴۰ درصد کاهش خرید نفت موجب
جلوگیری از جهش شدید قیمت‌ها در پی جنگ و بسته شدن تنگه هرمز شد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20095" target="_blank">📅 15:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20094">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سپاه زنجان: در حمله موشکی دیشب آمریکا، 3 پاسدار کشته شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20094" target="_blank">📅 15:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20093">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزیر دارایی اسرائیل، بزالئل اسموتریچ:
«غزه بزرگترین زندان جهان است. مردم به زور و برخلاف میلشان در آنجا نگهداری می‌شوند و اجازه خروج ندارند. این یک چیز وحشتناک است. فقط دروازه‌ها را باز کنید و بگذارید غزه‌ای‌ها بروند.»
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20093" target="_blank">📅 15:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20092">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خانه ای که در محله مينابي در قشم موشک خورد گزارشات بومی میگن که محله مينابي ها همشون جز بسيج و سپاهن و عادی نیستند ، ویدیو خبرنگار رژیم این گزارش رو تایید میکنه و نشون میده عکس قاسم کتلت هم بر دیوار بوده @WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20092" target="_blank">📅 14:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20091">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ارسالی : در قشم گروه پهپادی نیرو دریایی سپاه و هوافضا سپاهاز طریق آنتن مخابراتی شهری پهپاد کنترل میکنند خود اتاق کنترل پهپاد رو توسط شبکه به خونه‌های مردم منتقل کردن بین روستاها خونه کرایه کردند و داخلش کنترل پهپاد انجام میدن... هیچکدام از مردم روستا اطلاع…</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20091" target="_blank">📅 14:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20090">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خانه ای که در محله مينابي در قشم موشک خورد گزارشات بومی میگن که محله مينابي ها همشون جز بسيج و سپاهن و عادی نیستند ، ویدیو خبرنگار رژیم این گزارش رو تایید میکنه و نشون میده عکس قاسم کتلت هم بر دیوار بوده @WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20090" target="_blank">📅 14:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اطلاعیه شماره ۵۵ گروه تروریستی سپاه: تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در در پاسخ به حملات آمریکایی در قشم
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20088" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20087">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9ea42418.mp4?token=dKQRnRVio882kOGbNgV_qfZ7ouO7iDQ7Xl-EAWQshgDn5ZojJli5qEFzUDlBaM1rgndHUF7xAWQLAsJjf6IOr3GyRvFq_Xj6ICcX4Wv_XS2hA1xGVCyu3CeDCy1UFbiQbo71EgdGJTJ31mr9Ej_gQV433VXSRCs5SQisMm4iMcG61LcV3KijjGs4PVWRgX3vKJiGzuRnhGQiRNUf295gHoT9W2IlFOmnIauHRbjx_idXf6607tEGuH8r65fbukxYIOxvKMN6FWIL6y8eoSzdZqMuPR6VuKYwD6RHQIF2fFJKXhjEtXEpzxIahHGbxmZXwVxot4jJ5RbGw-rJNRavckHEUV7fROT0mnLPbz4QwbtBhqn0iLOxflPjoGZ590rstWmvQsCT8zly23XQiN4S22mU14TBAvTMcxFzGzvKhsgzV5eMu4cHG_do2JCF9yO0VwbU3dMpZxtq0kY1UHUeY4URhiHnLUxhwGsrRPYvaotDm-Mbn5ke2RuTRTpuiZBrznq8o7tiHLPM-Z4MTFQ3uzPGP71g9Eh5FHE38Jor1hrt_nTElNlFvSFZk0PhyM438O0selnZTDyu51ZRcHCqYBTH-3apIyu4NamfmMN0Ynq7kjknKFj2wbVlV3x0hLnIcyqsqWRw3T2ZcRXlLrmzqEn5q5H8f6IZcFtyDReAeFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9ea42418.mp4?token=dKQRnRVio882kOGbNgV_qfZ7ouO7iDQ7Xl-EAWQshgDn5ZojJli5qEFzUDlBaM1rgndHUF7xAWQLAsJjf6IOr3GyRvFq_Xj6ICcX4Wv_XS2hA1xGVCyu3CeDCy1UFbiQbo71EgdGJTJ31mr9Ej_gQV433VXSRCs5SQisMm4iMcG61LcV3KijjGs4PVWRgX3vKJiGzuRnhGQiRNUf295gHoT9W2IlFOmnIauHRbjx_idXf6607tEGuH8r65fbukxYIOxvKMN6FWIL6y8eoSzdZqMuPR6VuKYwD6RHQIF2fFJKXhjEtXEpzxIahHGbxmZXwVxot4jJ5RbGw-rJNRavckHEUV7fROT0mnLPbz4QwbtBhqn0iLOxflPjoGZ590rstWmvQsCT8zly23XQiN4S22mU14TBAvTMcxFzGzvKhsgzV5eMu4cHG_do2JCF9yO0VwbU3dMpZxtq0kY1UHUeY4URhiHnLUxhwGsrRPYvaotDm-Mbn5ke2RuTRTpuiZBrznq8o7tiHLPM-Z4MTFQ3uzPGP71g9Eh5FHE38Jor1hrt_nTElNlFvSFZk0PhyM438O0selnZTDyu51ZRcHCqYBTH-3apIyu4NamfmMN0Ynq7kjknKFj2wbVlV3x0hLnIcyqsqWRw3T2ZcRXlLrmzqEn5q5H8f6IZcFtyDReAeFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : در قشم گروه پهپادی نیرو دریایی سپاه و هوافضا سپاهاز طریق آنتن مخابراتی شهری پهپاد کنترل میکنند خود اتاق کنترل پهپاد رو توسط شبکه به خونه‌های مردم منتقل کردن بین روستاها خونه کرایه کردند و داخلش کنترل پهپاد انجام میدن... هیچکدام از مردم روستا اطلاع…</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20087" target="_blank">📅 14:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20086">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارشات از آغاز موج جدید حملات پهپادی / موشکی سپاه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20086" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20085">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دادستانی اسرائیل علیه یک راننده آمبولانس به نام فارس ابو‌الهیجا کیفرخواست صادر کرده و او را متهم کرده است که به دستور یک عامل اطلاعاتی ایران، اقدام به جمع‌آوری اطلاعات و عکس درباره مقامات بلندپایه اسرائیل کرده است.
بر اساس کیفرخواست:او از محل حضور و تردد اسحاق هرتزوگ فیلم و عکس تهیه کرده است. همچنین مأمور شده بود رفت‌وآمد و محل حضور یوآو گالانت را زیر نظر بگیرد و اطلاعات مربوط به او را جمع‌آوری کند.دادستانی اسرائیل مدعی است که این اطلاعات برای یک رابط یا مأمور وابسته به ایران ارسال می‌شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20085" target="_blank">📅 13:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20084">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرگزاری رویترز در گزارشی ادعا کرد که بنیامین نتانیاهو، نخست‌وزیر اسرائیل طرحی را شامل پیشنهاد ترور هدفمند فرماندهان ارشد سپاه پاسداران و ارتش جمهوری اسلامی ایران به دونالد ترامپ ارائه کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20084" target="_blank">📅 12:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20083">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی:
آخرین خواسته امیرحسین صفری از مادرش پیش از اجرای حکم اعدام این بود که به همه بگه ویدیویی که جمهوری اسلامی از اون منتشر کرده، اعتراف اجباری بوده و اون کسی رو نکشته.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20083" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20082">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرگزاری رژیم : نتانیاهو به ترامپ پیشنهاد داده یه لایه دیگه از رهبران و‌ فرماندهان جمهوری اسلامی رو بزنند.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20082" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20081">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jx9mhQEwrIDg00-pK0sJF9e80OQX3HnkgGbMmu0-L67_s5ZMl381PcPpAMhO-WPssPta2_Z1D-HUOzZsvbx3GkA2CrRAR5EF_dyrWDge36-r8gBglml98zuOAoo8Np068DWuEvGWPqEtLXBPm8fyHBbSCGoRvdZEMNWKUHfzOc2YSc1MYZ3Leftq7px47nq12shMA6gYl1VpODcEDzyy-XyZgGrg8pWx1ckgr_4ugUHiUkCFPJjuTikYEocjojii9vl0wxdiFhu-ZkcN29eMV-XhF61Df88QfO_hkls2H_9G8U-CJ2SPwd7YYbfF8XLBhsfyjjyNxhqaNeJ7e3D1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۳ تا از کثافتهای رسما گی حشدالشعبی که در حمله عربستان کشته شدند (عکس رسمی)
همین افراد دی ماه در ایران قتلعام کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20081" target="_blank">📅 11:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20080">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتانیاهو به شبکه ABC:
حماس باید منحل شود و غزه باید از سلاح‌ها پاکسازی شود.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20080" target="_blank">📅 11:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20079">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه: متجاوز همین امروز تنبیه خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20079" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وزارت دفاع کویت : یک ساختمان متعلق به یک شرکت چینی در شمال کویت مورد حمله موشکی ایران قرار گرفته و منجر به کشته شدن یک کارگر و وارد شدن خسارات قابل توجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20078" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سنتکام : در ساعت ۵:۳۰ صبح پنج‌شنبه ۳۰ ژوئیه به وقت تهران، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) با موفقیت یک موج سنگین از حملات را علیه ایران، در پاسخ به تلاش روز گذشته برای حمله موشکی به نیروهای آمریکایی، به پایان رساندند. دارایی‌ها و تجهیزات سنتکام…</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20077" target="_blank">📅 10:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20076">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتانیاهو به ای‌بی‌سی: «رژیم ایران همیشه دروغ می‌گوید، تقلب می‌کند و با زمان بازی می‌کند»
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20076" target="_blank">📅 10:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20075">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5647d258de.mp4?token=V9CIRCM_SjxHOrDmyns3Ge1UXXzcEMYvepNjuwHrpTA8i_VrwHCZ9VcI547-3VtS4htJImmpfOU0t_w02CncnDLGojnv6M-XnROx5BcoIXeFxYenMEq1SGpVX8Z1VXNzQmUFWkVjjfAzNxQnrgv-OmaxIvG6rEtHJRWIsaGETF6Rrwf_OznsKzjYwm_s3fpE1g4gq4vti5yb4nitEIurNoq83-YDDWGJsP-DbB8z7nFKlUc_DdQbg72p3zrd_VL-8IYYwFRsjn6ol4x2HS9ZEy5xk62zE8hpEK3TK0Zz1HuFFG9jarBRRQBPi7Fwrh8lqICI1AiuWLDWbdTz3elmBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5647d258de.mp4?token=V9CIRCM_SjxHOrDmyns3Ge1UXXzcEMYvepNjuwHrpTA8i_VrwHCZ9VcI547-3VtS4htJImmpfOU0t_w02CncnDLGojnv6M-XnROx5BcoIXeFxYenMEq1SGpVX8Z1VXNzQmUFWkVjjfAzNxQnrgv-OmaxIvG6rEtHJRWIsaGETF6Rrwf_OznsKzjYwm_s3fpE1g4gq4vti5yb4nitEIurNoq83-YDDWGJsP-DbB8z7nFKlUc_DdQbg72p3zrd_VL-8IYYwFRsjn6ol4x2HS9ZEy5xk62zE8hpEK3TK0Zz1HuFFG9jarBRRQBPi7Fwrh8lqICI1AiuWLDWbdTz3elmBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به ای بی سی: بعد از پایان این جنگ، فکر نمی‌کنم تنگه هرمز اهرم قدرتمندی باشد، زیرا خطوط لوله انرژی را از تنگه به ​​دریای سرخ و از آنجا به اسرائیل و مدیترانه منتقل خواهند کرد.
ما می‌توانیم این گلوگاه را باز کنیم و این کار را خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20075" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20074">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3061f41fa2.mp4?token=tqBLxAuGaSabQBjdEcO741Y6aLO-7T2svYqFTwyx4IBF_0sVH2TCNuJxUHOy0asFmWX7lw_m9TZNswPHW3MVcY3QrH0SrNo4PprrADVdFbqb8PkjiMg1nLFCBA2pRaSBPGZzLNFwF3Cqs3zv_spDcSVO8937bniUog3uwnH7ctfXv-jG1pSUI95mH_X-OzlEOByQHr4nuQ3eirM00GRwB7p-OF3-uy00KpdsqWFum2THNO4DrpyXC36ah1dDGo9DDxIQncpn2deiGryXwIJG0DqWUDXi9tDtNSMer9ZP-81TCj7rkwyQcj1NcSVr5xcMBpIh5UqLyMkVYfdB3n1ZjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3061f41fa2.mp4?token=tqBLxAuGaSabQBjdEcO741Y6aLO-7T2svYqFTwyx4IBF_0sVH2TCNuJxUHOy0asFmWX7lw_m9TZNswPHW3MVcY3QrH0SrNo4PprrADVdFbqb8PkjiMg1nLFCBA2pRaSBPGZzLNFwF3Cqs3zv_spDcSVO8937bniUog3uwnH7ctfXv-jG1pSUI95mH_X-OzlEOByQHr4nuQ3eirM00GRwB7p-OF3-uy00KpdsqWFum2THNO4DrpyXC36ah1dDGo9DDxIQncpn2deiGryXwIJG0DqWUDXi9tDtNSMer9ZP-81TCj7rkwyQcj1NcSVr5xcMBpIh5UqLyMkVYfdB3n1ZjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری ای‌بی‌سی نیوز: وقتی در کاخ سفید با ترامپ ملاقات کردید، آیا سعی کردید او را متقاعد کنید که حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک کاریکاتور یا تصویر کارتونی است. این درست نیست.
ما در واقع هر سه احتمال را بررسی کردیم و فکر می‌کنم این کار را به صورت علنی بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20074" target="_blank">📅 10:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20073">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDnpRloS4Iqbqda4tgVA-wM3XM0B8oCm6s6R-r0Dhlwtd8eELQnZYkvfLyUaoKI-aL2MWrJA1t_tiEelWfFR9ROiY9_va1XPUz7rqs0yBuy4Bvz2MdOGDAIBxud8zAsUAKE3107FGOX5idVK2b9lGwkCOP-Lff9QOAP4qchh4q2dmT2kDWjLKRswmji0eNkQ9nSA_mNYwxL_89_eY1Ecb8KgUOZgxI8t-gYkSHbi1SHBr7zie8sSLyHJ7pw1EJFMUGPwT0_quVJ7MEZMqnsQEqbCP8NkETtm9hkdrosEO5sNzt2u-sgEdyuJaFnEPMEiQIYdUMgDbHTlhfUfzb5kIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه حملات بامداد ۵شنبه ۸ مرداد
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20073" target="_blank">📅 09:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20072">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ارسالی : در قشم گروه پهپادی نیرو دریایی سپاه و هوافضا سپاهاز طریق آنتن مخابراتی شهری پهپاد کنترل میکنند خود اتاق کنترل پهپاد رو توسط شبکه به خونه‌های مردم منتقل کردن بین روستاها خونه کرایه کردند
و داخلش کنترل پهپاد انجام میدن...
هیچکدام از مردم روستا اطلاع ندارن که خونه بغلیشون چه خبره فقط میبینن تردد میشه در صورتیکه داخلش سیستم‌های کنترل پهپاد قرار داره
لطفا اگر هم قراره اطلاع رسانی بشه
فوروارد مستقیم نکن یاشار جان
آیدیم به فنا نره
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20072" target="_blank">📅 09:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20071">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">معاون سیاسی امنیتی و اجتماعی استاندار بوشهر از حمله هوایی به اطراف شهرهای بوشهر، جم و خورموج در شب گذشته خبر داد.
در این خصوص تلفات جانی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20071" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20070">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe63b4dfd0.mp4?token=qiWF3EpXRsUtlHg_I3uGhtUPNOQcFwrWx-oVo9z9T1tODIZjwzQPSrwTHD3Sj8NAZ5EmFUfBtL_wy1ZCHFvJrX2FamUBBZDX68UOlGDarhBZMCRBVMso-Y5XUTjfsV8tYh49MmNgKDk-eRtJ7q5OH_1xSrzNiIqLxhvpK_FPcYtysdgRKSZMTIRaS3z0npjiTEXE2nQvqVkXyLR0FCysN0-q1yxMb0mH_iCK_3RcDQ6YC9TIsMug_Z3VOIY9_fSNvhT_y-bv6P2pRJmbUsaOSgfSY6lWGuOdhreMj-kNSkZNFmHQS43M_Z90ofqtFomxsR1tdoqgQXoqsmM1tF_GMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe63b4dfd0.mp4?token=qiWF3EpXRsUtlHg_I3uGhtUPNOQcFwrWx-oVo9z9T1tODIZjwzQPSrwTHD3Sj8NAZ5EmFUfBtL_wy1ZCHFvJrX2FamUBBZDX68UOlGDarhBZMCRBVMso-Y5XUTjfsV8tYh49MmNgKDk-eRtJ7q5OH_1xSrzNiIqLxhvpK_FPcYtysdgRKSZMTIRaS3z0npjiTEXE2nQvqVkXyLR0FCysN0-q1yxMb0mH_iCK_3RcDQ6YC9TIsMug_Z3VOIY9_fSNvhT_y-bv6P2pRJmbUsaOSgfSY6lWGuOdhreMj-kNSkZNFmHQS43M_Z90ofqtFomxsR1tdoqgQXoqsmM1tF_GMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خمین
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20070" target="_blank">📅 07:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8b1wchIjHQuV0HrtCUULVySIU4pSx0rJ5WG5TSLh84uNM3XIf_yWSAuY7vNV-HqhwXAL93ZIRQwbvakE7OwsO2GADAkRcHJPE_PNY4Ryoym3RVmaNAuOu2nLjBF9gdcKuBVR54_LNQXaGVu4210B5PkyvXwGzNm9-wNU91UdzL5FinbxnjAvkPvorN5ljG0A96D9-a-IBnM_k_23IaNaodmcQfAQGPd2KcUc6Sd1B5iAZk5lQxhd5BIeeqQu592ilRijS4hdSSR-Shrbz9qTC6Cfw3QYD5Y0xRlIsYuCdFf4LygcBgVrrdDqNWc6JNJWNKDEAIyEVtmz_C12s_6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulWQxSI4BBinrW55rwdFL3Ygxk2v9QUHUXhiL1Lf2Xjt3dpGRdt5d7ZazF3jTi74QELaZAwOSVYYXkzBl94mnde587cF1KqsCTJpdS6_NK6i_m26XquBgWd5jMUwANJQ0smKogtF1-zWtf8FRPfKy_xEFj8Pyq9r1ylMaY04RYTwWRWmqXCmbfnx2LSA6uk3nJAtXdy1l2GzdfxD5cpsEPFKD0xqJVj8f9wfvC9aT5WzU7HZPTXTIc0-Xr7C4tqkVMSLtWuHrGPvRHNJi6XRIURFDaXuGCEqcltZ7XqqnvPNcfLCW0yhl67aNmgojK4dMkm0QjjODchEKTN2ODAVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bE9daluvhVyarE5nx0WpJHEN1WrfCJO90o67aCSBkNGANNswuxa4-hZHGUBodXJKLxZEvq4_g_sPuosrASy2wV1QpUTOQrN9sM9f5LMHB18TGR3wDroIqQmgsshCqJdJEfi0yJke-lbfUk1SUCN-i4fsEeBi1iwp-hCH0SnjOQX3S1S-9xgDw17ycBVo9WSABwpdN5tvHoSsqrGrXpPOSLV7FQuF4qSiMMI9HFFLfeNVbUlktXas0N3ZWvMMyqA9UG3qnx3aMkRvHxr5HYMxkms4ruozlorwCbpiLqKFUZnLlmvPe0OUeeNLqgT4mAHP3njRjkBbr3IBkQjV2zGPyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قشم ( از پارچه های یا حسین به نظر میاد یک پایگاه بوده )
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20067" target="_blank">📅 07:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739655b0d2.mp4?token=Oxzf5K8RnALq8cIge8pwJqPYFjP-RndsUINdwClLjuAylyf4fukHBX7C6OH1BlYXQk5TIT2--B2Ee990VUwyBKjAQjMuHdd19xBzaMNiuOc_kphRn8eL6V_kNt_VQfvXLxIbEB9VYDCk8z6zQxrZtT31b2FV-f6R_mhQIE92nPm7FV4V39frTPlLkWaRVCxn9mFJxTcfliEFjWHAv-4LRixqHGFXc4cKqR5z-AUSyIMdKC2KaPZklzZk7LTv7bjmnEgyMlrGKAPHYsyrj3Hv8y5fj6skZilIxXRgIXRga0loj9aUVZT-WbC3Apnu8Om1WlfKvR0qaRdv6wc8N1vgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739655b0d2.mp4?token=Oxzf5K8RnALq8cIge8pwJqPYFjP-RndsUINdwClLjuAylyf4fukHBX7C6OH1BlYXQk5TIT2--B2Ee990VUwyBKjAQjMuHdd19xBzaMNiuOc_kphRn8eL6V_kNt_VQfvXLxIbEB9VYDCk8z6zQxrZtT31b2FV-f6R_mhQIE92nPm7FV4V39frTPlLkWaRVCxn9mFJxTcfliEFjWHAv-4LRixqHGFXc4cKqR5z-AUSyIMdKC2KaPZklzZk7LTv7bjmnEgyMlrGKAPHYsyrj3Hv8y5fj6skZilIxXRgIXRga0loj9aUVZT-WbC3Apnu8Om1WlfKvR0qaRdv6wc8N1vgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشم
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20066" target="_blank">📅 07:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20062">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NueG9NpZsman0w-p59iXu4g1laMAb9MtEeV45-PrvtmAqoefLGwE6_E484xyvzluj7Nt1gdSz3gZoxHTpt5zhMTJhBEzuY4dRAPGMQXeZM4Q3tY4T4-h6_WT2pciHcujxcJBG-0Egai0w84H5Ymzi8yMAEZXUoEuA-TXL8tXhXQTYbAnwPuYnNLze1oCByxzS_AmDptQkZRD8uMCp-5dY3S2OSsZIJ3-WGu2Hw6dcSUODxONF9WPiRaw1kkne66S3Bm8WUh3opRz2xl4AP2PVX7Hq38b0Fwbpuabr2sNdLLcKbIUZvUNz9now8mcgrd4IWTA5my96UdfejF_Khhzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_VQ_bvyR0Xaim3HryUfEm6yQv6rD5ovJj-QXhSqCbUurQcejQ39zZeSaobYANM4UGShlYWThaaC5K0KakIKx3D3OS6yiyJnq-zhCM60jiHIY0ff7dLnbqBxGlfxeOrRTHr9TmVu1B4f78MUbLRfejvC_3CNbJViMxgaNv8gus7EFzQiwZsqhYsB86MYwmerMvzX5tX9_kSHFMK8KRtkOk3cXqWMVublR8UEggLBRh4LYBOdYzZUsrb76bopCzyPej77HCrD5EMAKi3vrAsB5R0cC1fn-2enBi5edj2qMjRJKEvz1tGqhpnXBBuSWmg0bzlPIZeBiHhQ2uhLUgZ8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ponJysv5VlMbXrgRO5rNyFffnIhTO8ki74lFfrtP2ufOWAKSXbiJsRPYtLbNkAIsCKqThtVHV1148ZkFNXFyKD5TGH7pv1XVnRWlsEsuagl8ZsOAAtoOtoc4fpedXUKMbOsPIoOHzprxFsVwTBEYSSiGBh56fths5cRDZCR5PhnTgdrsFRfuOhnYLk9pf_2vU8j_1buYqfxf2gdMh9FwuBjaTeO6xAkzk7RbKP6lPVMeenF7Pb_401_Fb2SEah8q37fH_rEGTFBguZQ8iGsHb4Xg0QdXsGHA9RgWE1-xN3GxbO0QtXNlCJ_JzBUAyal-fDKOh75Ws_AmVR6X6h2C8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5v9elWlmest05G0YgIm-qM8rkvQW2LD4yhUvRm2Dfja3x_VztMXpv-wWO6qULIAgNNFPl26PjS5RSmeVTBrO6jK8ba_0LJkcmRMrE_rrYc5MDteej6rqbmYmzlQldR7wiSGi4DiCLTckLuGqDY4M792iaExksESVsBW8hG5X8UKQ2OiDJp6bEUN5WyR1Lwb3E9ZJbqosFHJyX6VuZnjznzqcwWLnsaApQYz02AHrwk3l_LQmQg5z3RStYa3IkCYKogvVC_8oBcbelRGFjh4CDp4gs6u0UMbG1PSdyvVNhALuYYxVUTfcfbNbK6tq1h_tyxTSOrr2DxUWtdows0zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرتاب موشک از یزد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20062" target="_blank">📅 07:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20061">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c918aabbfc.mp4?token=OvTvh3IWT3gijyNCIIGQx7zQgR1hBOToZH6uad-p8E3nzNjcre2gWiey8SLZ5hTdbi4RIEQ4nxV4ryf-gA0z4Sm93BZp0ey2ji-5YYh4Cm0YwDEwnCfc8ES2PGcMCr2MFc-UHwvWuiCEBLYKkunM7L-qeFSRw-oVoLI-o8FBqq4P5HioXLyQ2cKhusP4fTIIRxCwx2reZwiyVQ95j9TbZFMCC06uHdi3MkvXrqQn66DxSYSk0J_Vvv_g2xSWnPVgfKAprWTO1f36wuB2rsVlnx2ArfDT1aZIbeKu01nSaIMNLip9ZroV5GdtPnOXuH-Ojaozb_lMjGPoHS7H0OqGUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c918aabbfc.mp4?token=OvTvh3IWT3gijyNCIIGQx7zQgR1hBOToZH6uad-p8E3nzNjcre2gWiey8SLZ5hTdbi4RIEQ4nxV4ryf-gA0z4Sm93BZp0ey2ji-5YYh4Cm0YwDEwnCfc8ES2PGcMCr2MFc-UHwvWuiCEBLYKkunM7L-qeFSRw-oVoLI-o8FBqq4P5HioXLyQ2cKhusP4fTIIRxCwx2reZwiyVQ95j9TbZFMCC06uHdi3MkvXrqQn66DxSYSk0J_Vvv_g2xSWnPVgfKAprWTO1f36wuB2rsVlnx2ArfDT1aZIbeKu01nSaIMNLip9ZroV5GdtPnOXuH-Ojaozb_lMjGPoHS7H0OqGUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریز شبستر دو تا موشک رفت
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20061" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20060">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7bInDAeRBLw7T4M9ZlZO_7tWJvHpT-7Hna8dYDexDQNery02U1EfssW8k4cUgIslFQduLAad3poDBKbOdbtJgH1F4iSPzOY0OcparN4GK39_Xl2I3GpvMthPmTAA684m_nf_1hmZPpV-qoVTFTsArhpn1CKM_9hKCQFSsW-6F5oHhWwABUN8cwr9aX7foeImg_a4T1-C32edtI72Cul9BUTNcVmJ_TFFbqFxNdS8ubdjMoZkzagntreXdZm6CbDsB_BEHCRnKeHIqSnBpR93ePDz4SSbMZAdyrZQ9HD68_ofBa5giSSj5sPhz8VshakH5vJ0QVsEwdjEQHSkpK9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان پرتاب موشک از خمین
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20060" target="_blank">📅 07:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20059">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a4989fd2.mp4?token=GEA-b17lLvocGWHmg6Hp-FV_qY8HPdHOKbjJZ2M2lgM6XEruS_VQAy4duhIyXavOrSpNMWhQ3SJ2B2V1ANuDTw6EHXi1VvsnpuBBDhAT0DOEBoQ5Doqhvx-in2HK3rLXXgLl68LQQEcyBoezS2mP_4G9oiIYrKTSW7Iu331WohvFYF09SL9aT4z-tAvpLO-FU27z2Pe_iORGLN-0c2xhWwOjicnnS799SqOoiZOugrGeYD--fXYpP5m_F6XxS2-nZh3HQ9m_WdnrOlK2-k5ajoL22FvCB1rRUPPi_0oSXQ-p8Qk3NGuxH2HWcjxvuRDjKab9cn1XMPZ1rFy0U0L4ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a4989fd2.mp4?token=GEA-b17lLvocGWHmg6Hp-FV_qY8HPdHOKbjJZ2M2lgM6XEruS_VQAy4duhIyXavOrSpNMWhQ3SJ2B2V1ANuDTw6EHXi1VvsnpuBBDhAT0DOEBoQ5Doqhvx-in2HK3rLXXgLl68LQQEcyBoezS2mP_4G9oiIYrKTSW7Iu331WohvFYF09SL9aT4z-tAvpLO-FU27z2Pe_iORGLN-0c2xhWwOjicnnS799SqOoiZOugrGeYD--fXYpP5m_F6XxS2-nZh3HQ9m_WdnrOlK2-k5ajoL22FvCB1rRUPPi_0oSXQ-p8Qk3NGuxH2HWcjxvuRDjKab9cn1XMPZ1rFy0U0L4ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز حدود ۴ صبح
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20059" target="_blank">📅 07:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20058">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc7049e361.mp4?token=Po4_jhKMT3ij3ZAHwgQ_IDZVtiiQDy1UZ6JnRnKr2GwGBlYDHOaIbc5TIotVLolygnsm9gVtjOASo34sZSPsH1xwB-1W793NUblrLbzJ903ZVqbN2fVzvACGC8TPkdNHskUEKhRJv1r3e1OiFU3iz1BWDKljpsyQyxufvvbzVg1qQmS9zB2jjHkRit3gB_jcHBz1v4qr_X9NXWwK3CWSsfp8o7maHY5axsUqHEobEtd0SNAU6low3vd_j22wQAuefntyPB62jG2JTXXjeFnOoxuCaGS6mpV9o8q6ugtX3p0PxWOyz1aNneTUxWgsfaOz3qzI7qRbbh5dtuxw-QySjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc7049e361.mp4?token=Po4_jhKMT3ij3ZAHwgQ_IDZVtiiQDy1UZ6JnRnKr2GwGBlYDHOaIbc5TIotVLolygnsm9gVtjOASo34sZSPsH1xwB-1W793NUblrLbzJ903ZVqbN2fVzvACGC8TPkdNHskUEKhRJv1r3e1OiFU3iz1BWDKljpsyQyxufvvbzVg1qQmS9zB2jjHkRit3gB_jcHBz1v4qr_X9NXWwK3CWSsfp8o7maHY5axsUqHEobEtd0SNAU6low3vd_j22wQAuefntyPB62jG2JTXXjeFnOoxuCaGS6mpV9o8q6ugtX3p0PxWOyz1aNneTUxWgsfaOz3qzI7qRbbh5dtuxw-QySjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس ۳:۴۵ بامداد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20058" target="_blank">📅 07:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20057">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b11a9cf.mp4?token=Q0NgIWPR3pKpyy83cezV0DaTAkU9JfnQu-Qa5OxY6aicDqWdjJ4g7Yf56EKFt3xld4aHYp3VJTs4W2eYxKQbbWoN_VOHi1WpEb16ilyUmmRADqG0w6Kt0sRZ_zWM8-17UxmtZN6poH04IrEXSAg9u9W0VAMOKmlSx_4VdY5Ikx7tgd95-ISWcYsxZCx8DJzDQ73WzSzm_NH9iDXAypfDFVKw3o698wYVmhAiIuIdX6Z-eb8amQkvjAZfHOORY71WK7mQ9k8C02p5uJLGU8VVcVGD_3G3LMjmWt9BS4YJ34PPsUFVtUEHUyTPfL25zx0fp46ZuJ85wNj-oKAH0p9Tsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b11a9cf.mp4?token=Q0NgIWPR3pKpyy83cezV0DaTAkU9JfnQu-Qa5OxY6aicDqWdjJ4g7Yf56EKFt3xld4aHYp3VJTs4W2eYxKQbbWoN_VOHi1WpEb16ilyUmmRADqG0w6Kt0sRZ_zWM8-17UxmtZN6poH04IrEXSAg9u9W0VAMOKmlSx_4VdY5Ikx7tgd95-ISWcYsxZCx8DJzDQ73WzSzm_NH9iDXAypfDFVKw3o698wYVmhAiIuIdX6Z-eb8amQkvjAZfHOORY71WK7mQ9k8C02p5uJLGU8VVcVGD_3G3LMjmWt9BS4YJ34PPsUFVtUEHUyTPfL25zx0fp46ZuJ85wNj-oKAH0p9Tsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">4 صبح آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20057" target="_blank">📅 07:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20056">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فاکس نیوز : هدف سفر نتانیاهو به امریکا تکرار 9 اسفند و بمباران تمام سایت های هسته ای و موشکی و نیروگاه های رژیم تروریست اسلامی ایران بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20056" target="_blank">📅 06:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Woyjr9bWX8pokFn_Xhy-WsuxCNjhQnVwNs_BsIT8iH5tfIyfY7oAgxjfBXZVg9Iq-3mhKJWLrKEfNfpI2XRMEZiB59ZpC97HfJudIWaDcIRkd_RDaoCR_qxoN2BE9A7xmx6xZrW4B1FX9whZMdqvC0wpkfNmKatjW3cng52NQ3PBmrP-4FRdeNh3ihlV2H1ZDi4bpTAoCaU21YW91aMB4R12b8ro7Hp6hzQB8u_VjeAPjg4p2Q8yPxlX4H9wKCu92q3v4wKONarI0bzupev3IYHcmOZ-Heuipg099rBWsagttA_O9tpGKwBuu2VkF66NcpWWfX6Yf7bI7IRERtBfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ : ده‌ها موشک ATACMS برد بلند آمریکا از کویت به سمت تأسیسات نظامی در داخل ایران شلیک شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20055" target="_blank">📅 06:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc88dc378.mp4?token=kSash5yKyfMmE5F9cXWuCogvGGVBW9AHyCdmAiTXen9-9LDuHP0ErjA3Tmf1EYF6iWj7R5PrZVGczEgSY095HFu5ag2mnEE5y74l5bGOaweW6Tqdez3oggpy7rNTkVileE5_jQWeJSoz5_MBON2iFMoKlnPKQUsANzmb-NJk7gmqr-5d0UTWWF8Ggpu18EFn1BXGLqJRqwOjkWVHj0de6Idoz8pNN8PzNdEgDuxkGFRw_IChVB10BGYSeTNBCGUUXCnT8ZWSDeHs4vEpYnxUQtlnmNq6_uws_1p9VsUdCpOD-F-jO0rfisN3aZpE65MWaLY2mwz4pDKSYbHQv3E5Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc88dc378.mp4?token=kSash5yKyfMmE5F9cXWuCogvGGVBW9AHyCdmAiTXen9-9LDuHP0ErjA3Tmf1EYF6iWj7R5PrZVGczEgSY095HFu5ag2mnEE5y74l5bGOaweW6Tqdez3oggpy7rNTkVileE5_jQWeJSoz5_MBON2iFMoKlnPKQUsANzmb-NJk7gmqr-5d0UTWWF8Ggpu18EFn1BXGLqJRqwOjkWVHj0de6Idoz8pNN8PzNdEgDuxkGFRw_IChVB10BGYSeTNBCGUUXCnT8ZWSDeHs4vEpYnxUQtlnmNq6_uws_1p9VsUdCpOD-F-jO0rfisN3aZpE65MWaLY2mwz4pDKSYbHQv3E5Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت اطلاعات سپاه گلستان اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20054" target="_blank">📅 06:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aabd75843.mp4?token=pgf_k0gYFYiarbTruMnxzbRcjNHsOdIyJqxxkIrnzYirELpE-yiVIzq91P4AoV295TXnDCkiia5A8oSO1rhRk5M1a_W9qHRkzXmlyH-6HQ8Z7G7IrVebSDS3l-nOzoOpaOHWywRkIEo4jLELHfIRkRxZNohEhcpof3jJJCt8J_DRPGWtO8Ah3XSZ4W57YcSVu6eI_AITcpo0ZJeK3OH-BBpScYN6mNdJNfNHYZuvvLamAjeWlQ5LWBkdC6mJyVE0snqHetjaspyB_g40J2ziXu5hEnofF3TLDB5vxSygaL5yctyoMRGFZ9KVR52DhULKv0jaSLR4xHl7DVWJ4vkM9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aabd75843.mp4?token=pgf_k0gYFYiarbTruMnxzbRcjNHsOdIyJqxxkIrnzYirELpE-yiVIzq91P4AoV295TXnDCkiia5A8oSO1rhRk5M1a_W9qHRkzXmlyH-6HQ8Z7G7IrVebSDS3l-nOzoOpaOHWywRkIEo4jLELHfIRkRxZNohEhcpof3jJJCt8J_DRPGWtO8Ah3XSZ4W57YcSVu6eI_AITcpo0ZJeK3OH-BBpScYN6mNdJNfNHYZuvvLamAjeWlQ5LWBkdC6mJyVE0snqHetjaspyB_g40J2ziXu5hEnofF3TLDB5vxSygaL5yctyoMRGFZ9KVR52DhULKv0jaSLR4xHl7DVWJ4vkM9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در
ساعت ۵:۳۰ صبح پنج‌شنبه ۳۰ ژوئیه به وقت تهران
، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) با موفقیت یک موج سنگین از حملات را علیه ایران، در پاسخ به تلاش روز گذشته برای حمله موشکی به نیروهای آمریکایی، به پایان رساندند.
دارایی‌ها و تجهیزات سنتکام ده‌ها هدف متعلق به سپاه را در ایران هدف قرار دادند؛ از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، سایت‌های دیده‌بانی و دفاع ساحلی، و توانمندی‌های دریایی. هدف از این حملات، کاهش بیشتر تهدیدهای ناشی از ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه حوزه خلیج فارس عنوان شده است
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20053" target="_blank">📅 06:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20052">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس به نقل از مقام ارشد آمریکایی :
آمریکا هم اکنون در حال انجام حملاتی در ایران هست.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20052" target="_blank">📅 02:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20051">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بوست کم شده داریم لول میایم پایین یه کمک کنیدد بریم بالا استیکر شاه برگرده به دوستاتون که پرکیوم دارن هم بگین
https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20051" target="_blank">📅 02:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20050">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش‌ها از شنیده شدن چند انفجار سنگین در نورآباد ممسنی فارس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20050" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، در ماه فوریه تخمین زده بود که کمپین علیه ایران برای دستیابی به اهدافش ممکن است شش هفته یا بیشتر زمان نیاز داشته باشد.
کوپر در ۳۱ مارس ارزیابی کرد که هنوز حدود ۲۰ روز دیگر برای تکمیل عملیات نیاز دارد.
با این حال، سرنگونی یک فروند جنگنده F-15E Strike Eagle آمریکایی در ۳ آوریل بر فراز جنوب غربی ایران، علیرغم نجات موفقیت‌آمیز هر دو خدمه در تصمیم ترامپ برای پیگیری آتش‌بس تنها در چند روز بعد نقش داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20049" target="_blank">📅 02:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش صدای انفجار سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20048" target="_blank">📅 02:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رویترز: انفجارهای شدید و پیاپی، کیف پایتخت اوکراین را به لرزه درآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20047" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به گفته روزنامه وال‌استریت ژورنال ، ارتش ایالات متحده قراردادی به ارزش ۵۸.۶ میلیارد دلار با شرکت لاکهید مارتین برای افزایش تولید موشک‌های دفاع هوایی پاتریوت امضا کرده است؛ بزرگ‌ترین قرارداد تاریخ برای موشک‌های پاتریوت.
این قرارداد بر تولید موشک‌های پیشرفته
PAC-3 MSE
تمرکز دارد؛ موشک‌هایی که برای رهگیری موشک‌های بالستیک، موشک‌های کروز، هواپیماها و پهپادها استفاده می‌شوند. هدف این برنامه، افزایش ذخایر موشکی آمریکا و متحدانش و بالا بردن ظرفیت مقابله با حملات گسترده موشکی پس از تجربه جنگ اوکراین و افزایش تهدیدهای موشکی در جهان است
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20046" target="_blank">📅 01:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آسوشیتدپرس : ایالات متحده تمام مذاکرات را رد کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20045" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b45ec100a.mp4?token=AM6Yx-nFftcxIrKJYFvIka5pKU0lGGBClt6gmg9PGuOWSBsnOP7Z4pJvIFfLNMY7Pq7o5PP85LtFQpBiTnt_beVL5TtTzqn5RTTB-oh94-bhTkkaUsQo5wlfurGtKNfv1GCZAvm9r7p9akb6DFfdkQ-p168xRB9-GPNM_34S7jErCn793ZNJ3biI0eFHt7kM0lADfgdsTYVRR5JvRvB-PwyTHoGGGfrCjdFkG1auJPU6X1PBdoW1Su2o_qt9bjcLzzAmlNhv16nsRoZb3_C9k8xCRQXOqsC2BovzQMuXyYVxGMfPQrrmHZdWcjNpkUGxJewoO9zmb47S143iMxcDuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b45ec100a.mp4?token=AM6Yx-nFftcxIrKJYFvIka5pKU0lGGBClt6gmg9PGuOWSBsnOP7Z4pJvIFfLNMY7Pq7o5PP85LtFQpBiTnt_beVL5TtTzqn5RTTB-oh94-bhTkkaUsQo5wlfurGtKNfv1GCZAvm9r7p9akb6DFfdkQ-p168xRB9-GPNM_34S7jErCn793ZNJ3biI0eFHt7kM0lADfgdsTYVRR5JvRvB-PwyTHoGGGfrCjdFkG1auJPU6X1PBdoW1Su2o_qt9bjcLzzAmlNhv16nsRoZb3_C9k8xCRQXOqsC2BovzQMuXyYVxGMfPQrrmHZdWcjNpkUGxJewoO9zmb47S143iMxcDuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش خوردن عنبه
😁
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20044" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20039">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20039" target="_blank">📅 01:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20038">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار در تبریز و بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20038" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20037">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرگزاری صدا و سیما : شنیده‌شدن صدای انفجار در پایتخت عربستان
منابع عربی می‌گویند لحظاتی پیش صدای ۲ انفجار نامشخص، به وضوح در ریاض شنیده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20037" target="_blank">📅 01:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20036">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تیک تاک ، تیک تاک ، تیک تاک
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20036" target="_blank">📅 01:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20035">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">همان طور که دیروز گفتم، اینستاگرام و چنل تلگرام رو میخوام پرایوت کنم. این آخرین فرصت برای کسایی هست که ممکنه دیروز این پیام رو ندیده باشن !سریع عضو بشین تا پشت در پیش عرزشیه ها نمونین
🌐
instagram.com/yashar
🌐
t.me/WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20035" target="_blank">📅 00:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20034">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هم‌اکنون ۵ هواپیمای سوخت‌رسان از اسرائیل و ۵ هواپیمای سوخت‌رسان از عربستان سعودی، به سمت خلیج فارس بلند شدند، دو سوخت‌رسان هم‌ در آسمان خلیج فارس با فرستنده روشن مشغول عملیات هستند. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20034" target="_blank">📅 00:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20033">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIhj5ZL2hbyGaP9MFBhfD2hb0HjVtvw_voCh1oQWi1t38xt2Fx0Y8COSle9zQVLW-8jen0nuZIRfgW6bN47F9aBulnBAglahhrP7J6HdgqHCuW8ycfGNPtduBvXPXevQ97ZCvXECAXjC2xwhJszuIlbVMETB9bKpaqbjKoaVm3F-Cxsw54bctSB6LF8IdTh0EMfOaho1vS7HZEz-TctXrH7UysuP3BMjt6km3QtERWa5kw9T9wPGHsrYSXNBYTwbLQSffXTG8Mt026zjPVTNGLcZQ6Mt63Dhf03eknVD6AQTU03jLbaant1ZBwHNHUO1XQ23p3y6zUoiZuiv0q1VzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون ۵ هواپیمای سوخت‌رسان از اسرائیل و ۵ هواپیمای سوخت‌رسان از عربستان سعودی، به سمت خلیج فارس بلند شدند، دو سوخت‌رسان هم‌ در آسمان خلیج فارس با فرستنده روشن مشغول عملیات هستند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20033" target="_blank">📅 00:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20032">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وال استریت جورنال:
ترامپ با وعده انتقام از ایران، از یک دور جدید از حملات "بسیار شدید" خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20032" target="_blank">📅 00:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20031">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20031" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20030">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش شلیک موشک بالستیک از ایران
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20030" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تا آخر گوش کن</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20029" target="_blank">📅 00:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">از دایرکت مشخصه امشب هیجان به اوج رسیده</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20028" target="_blank">📅 00:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مقام ارشد اسرائیلی به الجزیره : پاسخ گسترده آمریکا به ایران محتمل‌تر از فقط یک حمله تلافی‌جویانه است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20027" target="_blank">📅 23:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20025">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ در مورد ایران:
من دوست دارم تعرفه‌هایی علیه ایران اعمال شود.
لیندسی این را می‌خواست.
خبرنگار: آیا می‌خواهید مجلس نمایندگان قبل از ۳۱ آگوست برای بررسی لایحه تحریم‌های روسیه و ایران بازگردد؟
ترامپ: راستش را بخواهید، نباید لازم باشد، اما اگر لازم باشد، دوست دارم ایران را به عنوان تعرفه اضافه کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20025" target="_blank">📅 23:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20024">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4981a0c73.mp4?token=kgbrgisvHLAwWf1iOFcZPssODHYnJWyDK6HGP43xNBL0FFtDFNoAlVh9SL5YNg3FRqH0SEkpxKzLrkWR3CYsdCNLQI_8upAaTDjnnw49c1Wwe-2896XxGkJlUG9TxdUu5EuqscOB8VEsMqD46d2RlhPl-ptYx6ds3Y4h_Xs105C86SF9d45EBL5XX6IPwogGYq69Pf32Jg0FI5tHNZxprofmF2kofqieu3tZSQerMMJZ3QvRRWJcfmLWbcblBS2B3pgJUAj82WomjbD75kdm86igj8iujNtn161r7dSgyZkwzg-EYo6coD8Ga-mptvAKLpBqiC-ojr6Q-l8C3aUg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4981a0c73.mp4?token=kgbrgisvHLAwWf1iOFcZPssODHYnJWyDK6HGP43xNBL0FFtDFNoAlVh9SL5YNg3FRqH0SEkpxKzLrkWR3CYsdCNLQI_8upAaTDjnnw49c1Wwe-2896XxGkJlUG9TxdUu5EuqscOB8VEsMqD46d2RlhPl-ptYx6ds3Y4h_Xs105C86SF9d45EBL5XX6IPwogGYq69Pf32Jg0FI5tHNZxprofmF2kofqieu3tZSQerMMJZ3QvRRWJcfmLWbcblBS2B3pgJUAj82WomjbD75kdm86igj8iujNtn161r7dSgyZkwzg-EYo6coD8Ga-mptvAKLpBqiC-ojr6Q-l8C3aUg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد حملات ایران:
این گروه با گروهی که ما با آن سر و کار داریم متفاوت بود.
آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، ما باید کمی آنها را تنبیه کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20024" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20023">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364b88f4c7.mp4?token=kp3VZaRYSQW-QAD-TxdnKVK0cDODMwmIlVBmxHaSRXCUdCw4nD0xYZR8-RIFvKidBqVxVjv5j0TmTsbfF5NQgHUprQEwlgKzcUq2lQXeaqnmV8gzd7531QqQ8Ugv5q2WXF0X_XN0_MkZ8zKq1Gkw8ooL4Is6yRmv_6RqgM1Nuu1jzD3jMiH9-vJNuq0ljK9K0andltyWaSgfRfRq4Ym897OWFXe3IzWeEB1zHosUFQDIpKQEqSR4_96Q9H62wcUKhuoxGzeQgSmnyBdS1ZBqQKuOFuvMsFjqAoKBa1j8I9AjD4Gevmxl3k4H9Ybqx3Z8MPI1W7RfzBiGm7R3Qu-r8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364b88f4c7.mp4?token=kp3VZaRYSQW-QAD-TxdnKVK0cDODMwmIlVBmxHaSRXCUdCw4nD0xYZR8-RIFvKidBqVxVjv5j0TmTsbfF5NQgHUprQEwlgKzcUq2lQXeaqnmV8gzd7531QqQ8Ugv5q2WXF0X_XN0_MkZ8zKq1Gkw8ooL4Is6yRmv_6RqgM1Nuu1jzD3jMiH9-vJNuq0ljK9K0andltyWaSgfRfRq4Ym897OWFXe3IzWeEB1zHosUFQDIpKQEqSR4_96Q9H62wcUKhuoxGzeQgSmnyBdS1ZBqQKuOFuvMsFjqAoKBa1j8I9AjD4Gevmxl3k4H9Ybqx3Z8MPI1W7RfzBiGm7R3Qu-r8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: چه چیزی می‌توانید درباره حمله به نفتکش در مصر به ما بگویید؟ آیا این موضوع به ایران مربوط است؟
ترامپ: من در جریان قرار گرفته‌ام. این کمی بیشتر از همان چیزهای تکراری است.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20023" target="_blank">📅 23:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20022">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b410c8b1ad.mp4?token=RoGN2wFscdm7YblwgfU0ewRi5drOrYSY8ao66hAAa_PdZrVOMrPRnUh8Q8EYh-3p_IWJPKhT7vrJIyUZ8rQgYzdl4eHFCk5O810WsEtbv4NHStcQTouTghucIWhpQgt3DmlnZGnQ38XZho5AV-5j03YmZKLuptshzRTt7XAlxwD19Z_bM68tHVEtF2LjxE2mKb9CPM5QG1eFgjMJOjLHD9vfelvTl9Q7gBdOd-Q4B0KtsC0SK-2L7fFbZDvJPJeqonecFe-WWz1Fn3e6vvO7vN3c6xtox-uvIaDp-OsVWkoR1bIYHScwLWIwJnRbMjux_13uDyq4TE_Gy0-hL87KlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b410c8b1ad.mp4?token=RoGN2wFscdm7YblwgfU0ewRi5drOrYSY8ao66hAAa_PdZrVOMrPRnUh8Q8EYh-3p_IWJPKhT7vrJIyUZ8rQgYzdl4eHFCk5O810WsEtbv4NHStcQTouTghucIWhpQgt3DmlnZGnQ38XZho5AV-5j03YmZKLuptshzRTt7XAlxwD19Z_bM68tHVEtF2LjxE2mKb9CPM5QG1eFgjMJOjLHD9vfelvTl9Q7gBdOd-Q4B0KtsC0SK-2L7fFbZDvJPJeqonecFe-WWz1Fn3e6vvO7vN3c6xtox-uvIaDp-OsVWkoR1bIYHScwLWIwJnRbMjux_13uDyq4TE_Gy0-hL87KlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:ما می‌خواهیم آن‌ها را بسیار سخت بزنیم زیرا نوبت ماست که آن‌ها را بزنیم.
آن‌ها می‌دانند که این در راه است. آن‌ها از ما می‌خواهند که این کار را نکنیم.
آن‌ها دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20022" target="_blank">📅 23:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20021">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اکسیوس دربار دیدار ترامپ و نتانیاهو :
نتانیاهو در دیدار با ترامپ نسبت به احتمال دستیابی به توافق با ایران ابراز تردید کرد و گفت‌وگوی ۹۰ دقیقه‌ای دو طرف عمدتاً بر ایران متمرکز بود. به گفته یک مقام اسرائیلی، سه گزینه برای ادامه مسیر بررسی شد: دستیابی به توافق با ایران، ادامه محاصره دریایی و تشدید فشار اقتصادی، یا ازسرگیری و گسترش حملات نظامی. این مقام گفت ترامپ درباره پیامدهای جنگ بر بازار انرژی و اقتصاد جهانی ابراز نگرانی کرد، اما نتانیاهو تأکید داشت جمهوری اسلامی در تلاش است با استفاده از تنگه هرمز آمریکا را وادار به امتیازدهی کند و باید فشار اقتصادی از طریق ابزارهای نظامی و غیرنظامی افزایش یابد. او همچنین مدعی شد ایران با کمبود سوخت، صف‌های طولانی بنزین، کمبود گازوئیل و نارضایتی عمومی روبه‌رو است و حکومت از احتمال گسترش اعتراضات مردمی نگران است. این مقام اسرائیلی همچنین ادعا کرد که اگر ایران به اسرائیل حمله کند، پاسخ اسرائیل فوری
و بسیار شدید خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20021" target="_blank">📅 22:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20020">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آسوشیتدپرس : ۶ نیروی مشاور سپاه قدس در حمله مشترک آمریکا و عربستان سعودی کشته شدند. @WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20020" target="_blank">📅 21:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20019">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارشات از‌ پرتاب موشک از شازند اراک  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20019" target="_blank">📅 21:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارشات از‌ پرتاب موشک از شازند اراک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20018" target="_blank">📅 21:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به گزارش واشنگتن تایمز، وزارت خزانه‌داری آمریکا اعلام کرد دو نهادی را که به گفته این وزارتخانه از سوی ایران برای کنترل تردد در تنگه هرمز مورد استفاده قرار می‌گیرند، تحریم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20017" target="_blank">📅 20:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به گزارش وای نت عبری به نقل از یک منبع ارشد سیاسی، گفت‌وگوی میان بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و دونالد ترامپ، رئیس‌جمهور آمریکا، عمدتاً بر موضوع جمهوری اسلامی متمرکز بوده و به عنوان «یک رایزنی واقعی و تبادل نظر» توصیف شده است.
این منبع اعلام کرد که رئیس‌جمهور آمریکا با سه گزینه راهبردی روبه‌رو است:  دستیابی به یک توافق، ادامه محاصره دریایی، یا «از سرگیری و تشدید حملات». همچنین تأیید کرد که مجتبی خامنه‌ای، زنده است و افزود: با اطمینان این را می‌گویم
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20016" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارشات اولیه: صدای انفجارهای شدیدی در اردن شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20015" target="_blank">📅 20:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20014">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cee18be9c.mp4?token=fJA-ZVrhneE0fzqzqIMJvUF12jIXAT5AwVHTcXMwmaQ4H5SFe-dzJaCZkNge3CJmi6Xe_XflhqPJbFMmANrTGGiE0SrWVsD5lP0neIGqZ5qGFQNjsuSUWXlsOc9TPAp3wAOd8YSUmNSUOlhUIrtBHYbqsJizj97hfg1si__Q2KQoQKP0DeDJ-gcm3nW66vmT5fgBrmt-OxmhX4tvwW62Nfl6ddKoR0Sz9BapIY5dyLBaiZm0I3rlQGk40kLsHM__yqpovS75HNT5QfcKpBYs-C00l33UAisJHwSTWZSIHRaRfborHaRDMFd-1W9jHpXftJgEjaxzNp80RzEWOLj7qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cee18be9c.mp4?token=fJA-ZVrhneE0fzqzqIMJvUF12jIXAT5AwVHTcXMwmaQ4H5SFe-dzJaCZkNge3CJmi6Xe_XflhqPJbFMmANrTGGiE0SrWVsD5lP0neIGqZ5qGFQNjsuSUWXlsOc9TPAp3wAOd8YSUmNSUOlhUIrtBHYbqsJizj97hfg1si__Q2KQoQKP0DeDJ-gcm3nW66vmT5fgBrmt-OxmhX4tvwW62Nfl6ddKoR0Sz9BapIY5dyLBaiZm0I3rlQGk40kLsHM__yqpovS75HNT5QfcKpBYs-C00l33UAisJHwSTWZSIHRaRfborHaRDMFd-1W9jHpXftJgEjaxzNp80RzEWOLj7qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:من همین الان گفتگویی را با وزیر دفاع، پیت هگست، به پایان رساندم.
او چیز جالبی به من گفت. او به من گفت: "ما به جهان نگاه می‌کنیم، کشورهایی هستند که اراده جنگیدن در کنار ایالات متحده را دارند، اما فاقد توانایی هستند. و کشورهایی هستند که توانایی دارند، اما اراده ندارند."
او گفت: "فقط در اسرائیل است که هم اراده و هم توانایی را می‌بینیم."
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20014" target="_blank">📅 20:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20013">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الجزیره: شرکت امنیت دریایی امبری گفت که حداقل یک حمله پهپادی به یک تأسیسات ذخیره‌سازی گاز طبیعی مایع ایالات متحده در دمیاط، مصر اتفاق افتاد
تأسیسات ذخیره‌سازی شناور مورد هدف قرار گرفته متعلق به یک شرکت آمریکایی در دمیاط مصر است و توسط آن اداره می‌شود.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20013" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20012">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سنتکام : تنگه هرمز یک آبراه بین‌المللی است.  سپاه پاسداران انقلاب اسلامی هیچ اختیاری برای تعیین مسیرهای تردد برای جریان آزاد و باز ندارد. کشتی‌های تجاری همچنان از این تنگه با حمایت نظامی ایالات متحده استفاده می‌کنند.  از اوایل ماه مه، نیروهای سنتکام به عبور تقریباً ۱۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20012" target="_blank">📅 19:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20011">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آسوشیتدپرس : ۶ نیروی مشاور سپاه قدس در حمله مشترک آمریکا و عربستان سعودی کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20011" target="_blank">📅 19:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20010">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea64fcfef1.mp4?token=HP7jWXCsKMqQGn9WW4O1qNDTNX6vLwPLp-0t0HgIYU3-87mH24nthwrYOzct8y1zSPzcK5STnnFJNaJUxLKZeuGw4A2etCyZdmxdDO5Xvx01thtygzI-8xtmFE5cgKaKSFvAu6jY7zKmbiV61WQPlt2_Ol5X1jToBjoLlg5kJLcJUkTKhT0dIu_HTgZfiZMj4C6Y7u3fjZGBYGSLf_hNR1N4kGNYgLUZ2tjJwRNDuoo_D-w8G-Nrg6nOLy--jHad3OFVR9yqFD5lt8XfwTXbMPya_M-g6mnuRKc9tb8filKL3ElWN2b4iXquTmbNZaZpQ9J4kvVti_w7geateYpsFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea64fcfef1.mp4?token=HP7jWXCsKMqQGn9WW4O1qNDTNX6vLwPLp-0t0HgIYU3-87mH24nthwrYOzct8y1zSPzcK5STnnFJNaJUxLKZeuGw4A2etCyZdmxdDO5Xvx01thtygzI-8xtmFE5cgKaKSFvAu6jY7zKmbiV61WQPlt2_Ol5X1jToBjoLlg5kJLcJUkTKhT0dIu_HTgZfiZMj4C6Y7u3fjZGBYGSLf_hNR1N4kGNYgLUZ2tjJwRNDuoo_D-w8G-Nrg6nOLy--jHad3OFVR9yqFD5lt8XfwTXbMPya_M-g6mnuRKc9tb8filKL3ElWN2b4iXquTmbNZaZpQ9J4kvVti_w7geateYpsFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیتر هگست، وزیر جنگ، در واشنگتن دیدار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20010" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20009">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نتانیاهو : جمهوری اسلامی، فرایند غنی‌سازی اورانیوم را در کوه کلنگ اصفهان آغاز کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20009" target="_blank">📅 18:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20008">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641e67f8eb.mp4?token=ouXjXNgbhqZw1oeFPVYiMQPt-iWSBzgbB69EuJZ5ze5O9EK85Gywl4664kSX-yLpCK_A674NnofmK7TXvNmaNTRts1qpC6LV_IyCBqssqIo-wK-BxXyQ8fp5-mOHQ3BV3_05gMMLG6olMkSuIS4l_WdDXJMICSnXQzhXx66L9xc13OPv1eBqcwNL7k-6qZA-Td8iQ-3NKgITV38TPWQXk9dmDHlsc7bH63tgyQY-cqoeFQnU-1Jkf1wbphgdfrT6CIYUP1j1vJkoIsiqtd8NVBRQInybnoE4VdBmLf7RxRrJXlrH6mAsvXHiOFtEDVBzgp4qWMyd1o0jpwkY4K9EVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641e67f8eb.mp4?token=ouXjXNgbhqZw1oeFPVYiMQPt-iWSBzgbB69EuJZ5ze5O9EK85Gywl4664kSX-yLpCK_A674NnofmK7TXvNmaNTRts1qpC6LV_IyCBqssqIo-wK-BxXyQ8fp5-mOHQ3BV3_05gMMLG6olMkSuIS4l_WdDXJMICSnXQzhXx66L9xc13OPv1eBqcwNL7k-6qZA-Td8iQ-3NKgITV38TPWQXk9dmDHlsc7bH63tgyQY-cqoeFQnU-1Jkf1wbphgdfrT6CIYUP1j1vJkoIsiqtd8NVBRQInybnoE4VdBmLf7RxRrJXlrH6mAsvXHiOFtEDVBzgp4qWMyd1o0jpwkY4K9EVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20008" target="_blank">📅 18:27 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
