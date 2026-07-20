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
<img src="https://cdn4.telesco.pe/file/muQNAevQnzCpyE6TwLUaFcwc77yvDswawaAvRoEzAL3HdtvFRZScQv13OhImWgsuf5x0mwx-UzPHflXzdcvU8nPHxIIWyMd2SG96HhcbUDIYKAedV1F1PpoAZd3Tm88smepCgW_NMPlxOo7KV1pjtDvQ9nZQbGB5ehnxS909mhc2Kq72TtqHLMnpt9CvMAPJLsAagcqsHsbpswbcjUZ9w0yRBZP98hn01ev_RVhD6fWZO5F2eYK7azai4gWO_TYkQtNRMh_yNta26tRTLNxNE0CeOr67MEFXL67RA8Av3R_QDN-UhhjZeJyhDh2Rcws2L6OGgmRPm54QcY4dWRAIwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 20:21:39</div>
<hr>

<div class="tg-post" id="msg-136113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
وزیر کشور پاکستان: امیدوارم وزیر کشور ایران خبرهای خوشی به همراه داشته باشد
🔴
محسن نقوی، وزیر کشور پاکستان با استقبال از اسکندر مؤمنی، وزیر کشور ایران و هیئت همراه، نسبت به این سفر ابراز خوش‌بینی کرد.
🔴
او گفت که امیدوار است وزیر ایرانی «خبرهای خوشی» به همراه داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/alonews/136113" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
پوتین رئیس‌جمهور روسیه فرمانی را امضا کرد که بر اساس آن مقررات ورود بدون روادید شهروندان چین را تا پایان سال ۲۰۲۷ میلادی (دی‌ماه ۱۴۰۶) تمدید می‌کند.
🔴
عبارت تا ۳۱ دسامبر ۲۰۲۷ جایگزین عبارتی در فرمان قبلی شد که تا ۱۴ سپتامبر ۲۰۲۶ میلادی (۲۳ شهریور ۱۴۰۵) مجوز ورود بدون روادید شهروندان چینی را صادر می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/alonews/136112" target="_blank">📅 20:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnWy-vlWUHZvG5Y6AmzJ1aU2y6jeOVbtKT9vZATQ2ebPyntBnSGcHhdutiQFymOrM8FwXU3zLAw1_YLCv1xD44aiTohn_X7sTEg2XvaVjH4ZcBNObOablHUiiAh_WsxLJ6mXKFpzAZBIXlRMRjUOgSqpA3kcmOZzOSEZ19pxxUkeJ_jGC222Ho135XPTimgaL1-ty7VsLtgQKHM1jcsvHKF_UVCoXAJGI3wGx5s7GbeyRqj6QVMYcC3QX84aOlb7prO2RA6V2tPoCYOUStyjNTk_cy2aWs2E4WoypNMgkfBq-cp5TZwtFBr_vqxZdTmt9mHF1fj9MmNYIz4SuFe59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ: هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این قتل را چندین برابر پرداخت خواهد کرد!
🔴
این دستورالعمل به پیتر هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک نیروهای مسلح، و تمام فرماندهان ارشد نظامی ابلاغ شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/136111" target="_blank">📅 20:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
تعلیق پروازهای ایرفرانس به منطقه
🔴
این شرکت هواپیمایی اعلام کرد که پروازها به ریاض و از ریاض تا ۲۵ ژوئیه و خدمات به دبی و از دبی تا ۲۸ ژوئیه را به حالت تعلیق درآورده است
🔴
همچنین تعلیق پروازها به بیروت و از بیروت را تا ۲ اوت تمدید کرد، این پروازها از اول مارس به حالت تعلیق درآمده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/136110" target="_blank">📅 20:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136108">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
روسیه: اوکراین به دنبال بی‌ثبات کردن بازارهای جهانی نفت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/136108" target="_blank">📅 20:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136107">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqpDSxohTgDB2RK0pP0CpxVFSsszXuFgE3r9sGO_xf5hrOScIeCDWZpKZbak6_VHxsBtjhwMVh9kFnkrYWsceWBkz6hojG7w1nV4q-Vm1Ag1kMddNc8Z6n50jbZnrIr_quf3AYMaYLSlBA5U1I7DhTc0r2sd1T5OXnlPq9JWLmRVlHnKxi05C3PUOBUFsqCfavoP546tun3R1ETWi4IPXpdCEqkv-Ig6gBXkPMQJRwCxdeD0Xr8jvbPliI_OFGnWvgGVbqq39Z-I-Cr_dZyLzANobmfsNW_dyRAFYSrV_ENQvripqGSgXoqCWqcBWK6aYS21E70F7g40ceNv8T6TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی منابع: تصاویر ماهواره ای تایید می کند که سپاه به پایگاه "برج 22" ایالات متحده در شرق اردن در مرز سوریه حمله کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/136107" target="_blank">📅 20:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136106">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نیویورک‌تایمز: «اردن» به کانون تازه رویارویی نظامی ایران و آمریکا تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/136106" target="_blank">📅 20:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136105">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
یان برمر تحلیلگر و مدیر موسسه تحلیل ریسک اوراسیا گروپ:ایالات متحده می‌تواند تنگه را با هزینه‌ها و پیامدهایی برای همگان محاصره کند، اما بدون یک توافق نمی‌تواند تنگه را باز نگه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/136105" target="_blank">📅 20:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136104">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca576a26d.mp4?token=ijMYw44HqhgDLjNHZD0EdiI5K1UifwJyC1fmSP17tAYV8dVq-2wqSCv_xVYpSMQUIZtepSLF_RuZXNCPXZjI9He4bQC5RBiniiaweQDMMCo9RUkkpvOvpjwOurPvpcSmBexYaKX2TqWc-_JhsRdKGzvfE73aAt_PVuQBaQqDIOYe81ZiQ2C0mCgDJgsXXp8oTqAQr-VojALQj5XgMGES8aLI0bfXeIAB3TPvkaIZQ6Q7LqyIFfp_jBn7MEhnM92cBwqJ9wVr3ITHcPclCDMx7HrVkGokmAPi4DWTHZO0uj1SDYds-YFhdIO5veMRnys_TUerC8lOVsX91ZmvtwOg1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca576a26d.mp4?token=ijMYw44HqhgDLjNHZD0EdiI5K1UifwJyC1fmSP17tAYV8dVq-2wqSCv_xVYpSMQUIZtepSLF_RuZXNCPXZjI9He4bQC5RBiniiaweQDMMCo9RUkkpvOvpjwOurPvpcSmBexYaKX2TqWc-_JhsRdKGzvfE73aAt_PVuQBaQqDIOYe81ZiQ2C0mCgDJgsXXp8oTqAQr-VojALQj5XgMGES8aLI0bfXeIAB3TPvkaIZQ6Q7LqyIFfp_jBn7MEhnM92cBwqJ9wVr3ITHcPclCDMx7HrVkGokmAPi4DWTHZO0uj1SDYds-YFhdIO5veMRnys_TUerC8lOVsX91ZmvtwOg1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداسیما: چندروز پیش این ما بودیم که آتش‌بس رو نقض کردیم و آمریکا بعدش به سیریک حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/136104" target="_blank">📅 20:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136103">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
گزارش اولیه از وقوع یک حادثه دریایی در سواحل امارات
🔴
برخی منابع از وقوع حادثه‌ای برای یک شناور در آب‌های نزدیک سواحل امارات متحده عربی خبر داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/136103" target="_blank">📅 20:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136102">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d906443db.mp4?token=SaSSJTnvbBS4LwITkPFlmKoFaIGlWQ_I_IVzZ3F24U24gVuvh3WP09RHSo1zTnjJwzaHy-qLBmYJXwZU1COqwfkQhoDXQmn31OMLqXcfTMhk6Hc3_B1flCSFONnnoxQRC7-niAZ_MMWOz6kvsJQ2E3OPRTGmCw1shwIaaS2NjjlxqW8TsqyQw6OiTncqDFa8n7lK71EGwVM_D3nGJjyAi0-JfZgVUGyQt-ZxrBTkw7T1gPo5pas-uDabtej-99NhV4sZFQUzznXxi8qesz7mtC_VG1GUGThV2EPOynvISF3zXLuY0YRIBY7MxU8UeWke3wNlJPEnG9SG2IYE49J1OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d906443db.mp4?token=SaSSJTnvbBS4LwITkPFlmKoFaIGlWQ_I_IVzZ3F24U24gVuvh3WP09RHSo1zTnjJwzaHy-qLBmYJXwZU1COqwfkQhoDXQmn31OMLqXcfTMhk6Hc3_B1flCSFONnnoxQRC7-niAZ_MMWOz6kvsJQ2E3OPRTGmCw1shwIaaS2NjjlxqW8TsqyQw6OiTncqDFa8n7lK71EGwVM_D3nGJjyAi0-JfZgVUGyQt-ZxrBTkw7T1gPo5pas-uDabtej-99NhV4sZFQUzznXxi8qesz7mtC_VG1GUGThV2EPOynvISF3zXLuY0YRIBY7MxU8UeWke3wNlJPEnG9SG2IYE49J1OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد انتحاری مدل "گران-4" متعلق به روسیه امروز به یک قطار اوکراینی در نزدیکی ایستگاه راه آهن سولنویه در منطقه زاپوریژیا حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/136102" target="_blank">📅 20:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136101">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
ما رو از جنگ نترسونید. ما جنگ رو به چشم دیدیم. تو شهر و محله‌های خودمون. تو ۱۸ و ۱۹ و ۲۰ و ۲۱ دیماه.
🔴
تو کدوم جنگی اینطور رگبار مسلسل رو به سمت مردم بی‌دفاع میگیرند؟ کدوم دشمنی بجز جمهوری اسلامی ممکنه اینطور مردممون رو قتل‌عام کنه؟!
💔
صداها رو گوش کنید. رگبارها کلاشینکف است. تک‌صداها قناصه. با هر کدوم از اون گلوله‌ها مغز و قلب یک جوان ایرانی را متلاشی کردند.
🤔
ما ملت ایران یک دشمن داریم و اونم جمهوری اسلامیه به همراه طرفدارهای حرام زاده اش. دشمن دیگه‌ای نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/136101" target="_blank">📅 20:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136100">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
گزارش اولیه از وقوع یک حادثه دریایی در سواحل امارات
🔴
برخی منابع از وقوع حادثه‌ای برای یک شناور در آب‌های نزدیک سواحل امارات متحده عربی خبر داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/136100" target="_blank">📅 20:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136099">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdjSUNPjxeAHtBi7cxnVK6TAkALMwwSokbEe5DiVblMRf88Uepxku-1AdyiseUUNgN5yPXbgUhUgSUOASzc5t0mKf99IPgW4PI5aoKYIJGrisiN1uhptyZksqINsN-859eP-wTpBqu7ntKiQxEEm56rdwkkMIOvFK8FyySxq9xqW2gpkFBRIfXBM8ip93kK7MqYvVEuCWYaPGfLxr_S_wyDvp92IhSY81KMjyyQT4wm1ilgKCMbAn6XJ4u0249Ow3WuvS024D_8kXd80T09R_KI8cA1caalbXN-yg8v4MJxjhFsXGCgBHM5qbEuxWDllsobsh9eFYRJphCIDLhBQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دمای ثبت شده در شهر های ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/136099" target="_blank">📅 20:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136098">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
توانیر: بین ۷۰۰ تا ۸۰۰ هزار ماینر غیرمجاز کشف نشده وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/136098" target="_blank">📅 19:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136097">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارش اولیه از هدف‌قرارگرفتن یک کارخانه در خمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/136097" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136096">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
گزارش اولیه از هدف‌قرارگرفتن یک کارخانه در خمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/136096" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136095">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuxgLRSofXKEqMr4lsfwXNILDQnFxA8gzkjlWvbm3MYh8nzh1g89wrI8zdlPkRuAiIJ1LyS2lHxv-zk3zvTn1drQFeefU5BpAnu91SFcGnNK2-ng0hrqAmfzqdVHqZMQPssyyCAT5W1DG9aLuyH0frwRyciBq4nZFJQq26RZR0ZI5QmoCgEhiG7lVDJPGK_E407wfVPsjSfa2qEJXzFfYWIbCcd1qsOqupHmimcFRyBQ8Gbedzwgz9DpvYGHGA4xMxjoVik9AEMYXxrU3HPgCaZ5IdEB1bQxmztyhs0H1e8UKEuoD1ycBvTaFuBfqd52JMslAyv38guu0UZmcSMkkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ دستگیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/136095" target="_blank">📅 19:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136094">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد که نیروهای آمریکایی مسیر حرکت ۷ فروند کشتی تجاری را تغییر داده و یک فروند دیگر را از کار انداخته‌اند، از زمانی که این کشور محاصره بنادر ایران را از سر گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/136094" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136093">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFWJk3ACWC6uiXaua3KacaXvI-9ipebYGKeRq-UB_5XBHeDBGNvH7IVZF4o7kXQE1CGhKBIOlBvamDRrvjfrI81gwyUAK3N8pnykwiU-9wDFPV75kesmYASujbfKNH2tkHwPADW0gVRplyryUL--BxfheDkj483tsiRLfvoVC_KmuCSDjs90DyKfR31eFaqOzx90dyJuweLSqoX9bCuRRvH3P8EOzUp-BwIlNgpiQr-iIbfmxTHNxWiR6GU2OxbJJSYBMEEXWXYtEY5_0Mqdsgw8bU-Ytl1LIE1OnMcUWPYU2kbJ_DOgS18SyDDNWaSkiT5ylxxHWSI6ji_x_4Cvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید: آمریکایی‌ها با قاطعیت از توافق صلح ایران حمایت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/136093" target="_blank">📅 19:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136092">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: میانجی‌های جنگ آمریکا و ایران در تلاش برای پیشبرد آتش‌بس جدید
🔴
قدرت‌های منطقه‌ای با نگرانی از افزایش خسارت‌های اقتصادی و خطر تشدید درگیری‌ها، در تلاش‌اند زمینه دستیابی به یک آتش‌بس جدید را فراهم کنند، اما همچنان با چالش همراه کردن طرف‌های درگیر با این روند روبه‌رو هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/136092" target="_blank">📅 19:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136091">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / صدای انفجار در سیریک و غرب شیراز شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/136091" target="_blank">📅 19:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136090">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وضعیت در بحرین عادی است. موشک‌های بالستیک مورد هدف قرار گرفتند و منهدم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136090" target="_blank">📅 19:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136089">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7b5813d2dc.mp4?token=pjmY0YS2rIByGQhSUpVOvJ5hIt6rZcH6zp_6XXsNm4_OtpmDrlFNraL8OUv3tLGy755SjXwbCSm1a-RDUZbvfxzlH4eu4UI4djgTR_W8b7g2-d0DaWcooRmYFRrniw3OkWluzj7sI-lOuzIeAO_3-2owyoA66mg1FgApURDgSbwZsXtZKIhEC7c4jgl9L66Z6TbzvK3kygTQg6cH9hrUyKz4aq6uIiLjjbmb5Rp1STRV3LRip89P-_NGXiGngs5YhcV48Ht1dhdnNY0I00Z7MF084AADKdQQs-Rm2_fza9lS0ObUxLX8Tzddo9kW6WtBJBAEX-r3AgzF0AsGNFsqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7b5813d2dc.mp4?token=pjmY0YS2rIByGQhSUpVOvJ5hIt6rZcH6zp_6XXsNm4_OtpmDrlFNraL8OUv3tLGy755SjXwbCSm1a-RDUZbvfxzlH4eu4UI4djgTR_W8b7g2-d0DaWcooRmYFRrniw3OkWluzj7sI-lOuzIeAO_3-2owyoA66mg1FgApURDgSbwZsXtZKIhEC7c4jgl9L66Z6TbzvK3kygTQg6cH9hrUyKz4aq6uIiLjjbmb5Rp1STRV3LRip89P-_NGXiGngs5YhcV48Ht1dhdnNY0I00Z7MF084AADKdQQs-Rm2_fza9lS0ObUxLX8Tzddo9kW6WtBJBAEX-r3AgzF0AsGNFsqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دریایی انصارالله، یک پیام رادیویی با فرکانس بسیار بالا (VHF) برای کشتی‌هایی که در مسیر به عربستان سعودی قرار دارند، ارسال کرده و به آن‌ها هشدار داده است که مسیر خود را تغییر دهند، در غیر این صورت ممکن است هدف قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136089" target="_blank">📅 19:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136088">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
احتمال تاثیرگذاری در بحرین. ممکن است یک برخورد رخ دهد یا یک رهگیری در ارتفاع پایین صورت گیرد. این موضوع در حال بررسی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136088" target="_blank">📅 19:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136087">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رئیس سازمان آتش‌نشانی و خدمات ایمنی شهرداری بندرعباس از جان‌باختن ۶ نفر در پی وقوع آتش‌سوزی یک منزل مسکونی در محله اسلام‌آباد این شهر خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/136087" target="_blank">📅 19:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136086">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2b37b047.mp4?token=TJw1iO_Yax2cijDexUcn_ZDX9oQe1pT1Qs9AjL5PCpbP58Ysp_DVvCJyfPnKS348i4Hv9LSw42miB9RW2BqE3Sn6rk-onDUp2pE04Zbe6Js_mQ-tv8u9xOcLkOsjoZpXkiFkfDDAYbSlwWvlyk91-PisZxt6MkdXIVRTGrzECu92X0XDAcpVFNQOdD0ezBisGF_lGOigF_PRpIy7lJdt2dq_KBAY0GD8e1Gj5Zo6QWRMWtZSrvIRUC5IjSqvbFvE2S3fEAJJXi2W6-ZazHwm-06GvAmN1uGmEUN7ei4iO_KcBedXUDCEY8XmgGdDfHp1LfVEgufzFJ8NcCGwBHzlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2b37b047.mp4?token=TJw1iO_Yax2cijDexUcn_ZDX9oQe1pT1Qs9AjL5PCpbP58Ysp_DVvCJyfPnKS348i4Hv9LSw42miB9RW2BqE3Sn6rk-onDUp2pE04Zbe6Js_mQ-tv8u9xOcLkOsjoZpXkiFkfDDAYbSlwWvlyk91-PisZxt6MkdXIVRTGrzECu92X0XDAcpVFNQOdD0ezBisGF_lGOigF_PRpIy7lJdt2dq_KBAY0GD8e1Gj5Zo6QWRMWtZSrvIRUC5IjSqvbFvE2S3fEAJJXi2W6-ZazHwm-06GvAmN1uGmEUN7ei4iO_KcBedXUDCEY8XmgGdDfHp1LfVEgufzFJ8NcCGwBHzlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی‌ از شلیک موشک بالستیک از لار فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136086" target="_blank">📅 19:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136085">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
اسکندر مومنی» وزیر کشور به دعوت همتای پاکستانی خود و با هدف پیشبرد همکاری‌های دوجانبه وارد اسلام‌آباد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136085" target="_blank">📅 19:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136084">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/beRZ_kNON8eNjpA6GVWaW7pmtQ6IRMQ6l8SHdfI2VHmBuw5C-t5Cd5QVi7JObZUKV1j7SoLLaV05TudZG8HwRJVDZvL8qQxtIsrjMM9LpqTQP7v-pFnxY9w8f8r_oAU6hq46JMG6RLNzBKtgUmTINdlamZL1hgx6KnYi-1n98qvEZAlocNJhUjG_N6-i13jziuvAyvib_grOm_Rr7Li3lgsMU9OMzdlyVETuk-vGCt3owOVRga7HIg9wvaWp6T6LaLqgy6gNpPa6RPvfp61iPITKHJK2Mp4DIebMqITGkBHLQjWgheF04Zkk-vT9BAjtAAPM52NrrRSEK-Rg1emHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک موشک بالستیک از شهر لار، استان فارس، به سمت بحرین شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136084" target="_blank">📅 19:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136083">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
آژیر های هشدار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136083" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136082">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
آژیر های هشدار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136082" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136081">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b09189c2.mp4?token=B4sWECbny9pJUKvfQsd7wnDGOdae-FZzizpfJDHPtC5lhBI5cC28c93mOMicERSrseTJn56aLXNLlDmzAliS5ZZCYG-NL-OxyYf3C--rDoSIia-RIYrnOhB_d5rebUjYmPl7kQXcdBsPDCYH9V1b36Y2Hu1VmBOKDABAA3AbdIVCasgQoKz-wnxH_vnpzXE2n8yEFaqj9q6TpM6pp6LdxRgK5qo1W8hGVCd-nzKFHPxdBvkPA6NkI5er0ylxrtjFpadvO_VcghvA9PJV28wyssTBBNovovAwjj633ucuS1oVGvxzDUtskY4mpao2QZCt5iY4DU2prVhjWqewgnAs_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b09189c2.mp4?token=B4sWECbny9pJUKvfQsd7wnDGOdae-FZzizpfJDHPtC5lhBI5cC28c93mOMicERSrseTJn56aLXNLlDmzAliS5ZZCYG-NL-OxyYf3C--rDoSIia-RIYrnOhB_d5rebUjYmPl7kQXcdBsPDCYH9V1b36Y2Hu1VmBOKDABAA3AbdIVCasgQoKz-wnxH_vnpzXE2n8yEFaqj9q6TpM6pp6LdxRgK5qo1W8hGVCd-nzKFHPxdBvkPA6NkI5er0ylxrtjFpadvO_VcghvA9PJV28wyssTBBNovovAwjj633ucuS1oVGvxzDUtskY4mpao2QZCt5iY4DU2prVhjWqewgnAs_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: ایران یک هفته پیش قرار بود بیانیه‌ای صادر کند مبنی بر اینکه تنگه هرمز باز شده و دیگر به کشتیرانی حمله نخواهد کرد. اما به جای این کار، به سه کشتی حمله کردند.
🔴
رفتار آن‌ها باید تغییر کند تا رفتار ما تغییر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136081" target="_blank">📅 19:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136080">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ژان-نوئل باروت، وزیر اروپا و امور خارجه فرانسه، اعلام کرد که روز یکشنبه شب، دو کارمند سفارت فرانسه در ایران بازداشت و به مدت چند ساعت بازجویی شدند، و یکی از این کارمندان مورد ضرب و شتم قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/136080" target="_blank">📅 19:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136079">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878063c52a.mp4?token=jq4wv2xc00lbJCsxVhljF4Cz5bridSsQPxuTtA3W1v8SgGtkAb8kTLpzvyrdpBz_ZlKpas9-xCDX8vuFzEUna3sUBKGZQas48yckpBSBKUMyMSX8JHsLUVv0a9PPjZm2_bPB95-XL-uY_XJYEKa7j5h3LkGGp6n_jNFJXKHVbk-ad6xnyls73jt9ZGSsmU3nC8hKwB_Xr4rLZ8hXdjOPOh3MPvqJDlBVmG7L_mz3XxXRsKlGJIh0jwctuJvtqiNTSWWx9sbFuPb6TtOpT6hjfAgNNAWPeiP1y1kLEbHqPpyC9DrwHSs3BERpRKfQvyf7FnxgVD3n1eIO_vrHBkOW7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878063c52a.mp4?token=jq4wv2xc00lbJCsxVhljF4Cz5bridSsQPxuTtA3W1v8SgGtkAb8kTLpzvyrdpBz_ZlKpas9-xCDX8vuFzEUna3sUBKGZQas48yckpBSBKUMyMSX8JHsLUVv0a9PPjZm2_bPB95-XL-uY_XJYEKa7j5h3LkGGp6n_jNFJXKHVbk-ad6xnyls73jt9ZGSsmU3nC8hKwB_Xr4rLZ8hXdjOPOh3MPvqJDlBVmG7L_mz3XxXRsKlGJIh0jwctuJvtqiNTSWWx9sbFuPb6TtOpT6hjfAgNNAWPeiP1y1kLEbHqPpyC9DrwHSs3BERpRKfQvyf7FnxgVD3n1eIO_vrHBkOW7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما منتشر کرد: تشکیل زنجیره انسانی ده‌ها هزار هرمزگانی در نوار ساحلی استان هرمزگان و جزایر ایرانی و اعلام آمادگی برای دفاع از تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136079" target="_blank">📅 19:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136078">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E85zTiUOA50APvYfVNHJtJOvsfmoo9jgplYKc-ydQ56_iEMZgXxKTCa6BQFPh9gAciFmONuueqB8HpIE-xfik_CncKvnzWkBwY1uqvpS7o_0oMoVeCZxqgUBO8kdDNrAe-8p2lLt4bJ6IQFoLsPo4hPzuW-c4TsWqIv2troK3D4Jdq1GCEbqB9xie9anEV46xtvlbgACL_yD0cC_FSDL3pswC0wN8xApuh8wq8UXNDkqZeitwLlCTql3rF4sJFfq3c3IOo5EQhfI50bVdir0Fc0Zz9uTqXimI7LV8-vyTV64Xbiu9QBz7t9zp58UCOMHo4_icATTD3jDRzytSgK3uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرکت هواپیمای عراقچی به سمت پاکستان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/136078" target="_blank">📅 19:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136077">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRYIpw3cw5IiMEl0E5ODgNZmdket3za-tGPYOuxZocUyzztCDdITjfwfI8NOeswdGVP-cxndbmWGrNLzcn-yx_oES2NUIpn_ushmc930oxtf5CCW8c2txMZzz29JcsAsQYRtrC2PfHTa7EKsmA6Xbxq15IIXk1rIR-dcQa_HSqMg5_xcmCn3V38_5S11mu4PK4JvJ9uahA_mYB5QJOYq6uRmoINt041Ii7izR1xEW85RQdA2yANLEhUzNil_tFH6MMIeGaPO4PD_xmt_boPUsN3gw4wQxGpLe8uEt25oaglPLNGuSXAxZMuScdf6Ak9hYPVv4HcmmPTVj-8IhWmoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاتریوت یک موشک بالستیک سپاه را برفراز بحرین رهگیری کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/136077" target="_blank">📅 18:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136076">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2pcvFyC51Aqj6M3WBznu4PFbuCNXC2HWvvek2iGhwvChhUGUtVyKbDQjo98p0j0zQdMjhLBB_Vaz47KhpOkfr5KOtQj6dYuATrkRGk4tAy94eAzhmONDWFS-uISIoZkbsYBiqHk6VxCJpVQUKwVFkLjzLetPm59veeWK7euJZe8RslV5E5gK4zIOYOyyDlDxmrrr_FO80oHom4mLVuXfaPUEiP2oUV0be5oGzHYtgt-zc1UOA7madFCIog_Bxh9ZBqsqq8e1xbCmhR6kRx2Re3vpMubaaCM3GQFbscuy859olU01haa9HWJHgusZ7GaUOn_ITWteER63jfQg_xYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
⚽️
رتبه‌بندی جدید ۱۰ تیم برتر فیفا پس از پایان مسابقات جام جهانی.
@AloSport</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/136076" target="_blank">📅 18:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136075">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defffab074.mp4?token=kIBgylHh8zU7CVq3GXk7fSPPkcbS8xN3upjiMXcJLdzGDKFVYNTlzA9DDr3ldoEHUuNx8hDlOy2_Rb4r0QS7mueT2kZPZLkoUJGC2aognDxjpnmL0omdwEPqDCK3EAv2Z9P4UwFyFhOxKvCq4UCLLXwlKudJ74hKE0kMadugGqLa_RgB27b6jJopjHmXGfA3Kg-VAazMSmQ2-1xRrVmQmXC0nzPXj-WzIj7Xssc7Z4qn6wOwcjvQZg5YuLSfpB3ISA9ffx6SJmvUbIqpG6PowoLS2L7wes3zcb1X2Vi545u8SpWFf9RGfLWrt_PBwg2KWpuSMCEi7qvy27674ome8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defffab074.mp4?token=kIBgylHh8zU7CVq3GXk7fSPPkcbS8xN3upjiMXcJLdzGDKFVYNTlzA9DDr3ldoEHUuNx8hDlOy2_Rb4r0QS7mueT2kZPZLkoUJGC2aognDxjpnmL0omdwEPqDCK3EAv2Z9P4UwFyFhOxKvCq4UCLLXwlKudJ74hKE0kMadugGqLa_RgB27b6jJopjHmXGfA3Kg-VAazMSmQ2-1xRrVmQmXC0nzPXj-WzIj7Xssc7Z4qn6wOwcjvQZg5YuLSfpB3ISA9ffx6SJmvUbIqpG6PowoLS2L7wes3zcb1X2Vi545u8SpWFf9RGfLWrt_PBwg2KWpuSMCEi7qvy27674ome8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سلاخی کردن جوان ایرانی توسط حرام زاده های طرفدار حکومت تو بندرعباس رو ما فراموش نکردیم
🤔
سگ آمریکا شرف داره به شما حرام زاده ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136075" target="_blank">📅 18:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136074">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
خبرنگار الحدث: پیشنهاد جدید توافق میان آمریکا و ایران شامل توقف خصومت‌هاست
🔴
پیشنهاد جدید توافق میان آمریکا و ایران شامل اجرای تفاهم‌نامه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136074" target="_blank">📅 18:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136073">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d3c1d446.mp4?token=Bm3G9Wrcg5peSFlDV83gRjM2VqfWNtayUt1RE5-Rm9xdwhO6Y_zbZ3k9iqjrW3hwMWpJKKyFqctOBoL_n2qdlasUXm-nY2k8XH3oxHZrh8jYhpS7kVNX3ExTRATmXApBpE2EUeT6c3Ih7t8h55AN-XzbYFngxZxeKB7FaexQKUMYYRVX9UT6oyEih1PqbDWB9NU9fpoKKP4SzjOahCabpKuS_VIG6yHFEHANFrRuUFyhuSSvmNK8txiPoKJ0YK7B4BwzpEJRFlYclDmPkub0XyfWUo-bQX29gc1fkzt6WAiuSpvepi6s0aIVuEHrHCJsWIc5d-R7yXq825j9VUkKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d3c1d446.mp4?token=Bm3G9Wrcg5peSFlDV83gRjM2VqfWNtayUt1RE5-Rm9xdwhO6Y_zbZ3k9iqjrW3hwMWpJKKyFqctOBoL_n2qdlasUXm-nY2k8XH3oxHZrh8jYhpS7kVNX3ExTRATmXApBpE2EUeT6c3Ih7t8h55AN-XzbYFngxZxeKB7FaexQKUMYYRVX9UT6oyEih1PqbDWB9NU9fpoKKP4SzjOahCabpKuS_VIG6yHFEHANFrRuUFyhuSSvmNK8txiPoKJ0YK7B4BwzpEJRFlYclDmPkub0XyfWUo-bQX29gc1fkzt6WAiuSpvepi6s0aIVuEHrHCJsWIc5d-R7yXq825j9VUkKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرمربی نایب‌قهرمان ده نفره جهان اینگونه با گریه از مردم کشورش عذرخواهی کرد، مثل بعضی‌ها از حذف در گروهی جام جهانی دستاورد نساخت و پیشنهاد مجسمه سازی نداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136073" target="_blank">📅 18:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136072">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxax57wR9ZEg67CZfFK3Q01o10GhCxc_GzDII_1llcoD_f7aVxgcEQVnLT_HZ3A4Y-WgR6n6qCd1pfxvXp95h29vetLslVHea17Y0vqnZJ0OspE1stp0LfWpIX8RMuTsNZDwEqfYquQUzRgL-cG4KvHbIFQoZa3QwDfMgodX68QNe1UTYYbwF6oDnYAjpVpRbJhHYDYkpLihhac78gN_R9PRPQJ1ymuG2GlgKm-ES87OZlJZ7-yAUt2RS7oqlco1tQ9gyt1zyYMp4-P7OViWp8dbUFekhjZOCL_-GTY0LdwF9cNpHpC-v8ZymKkHMKr_YFS8DWw5rlhQTwZZ8jvW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرکت هواپیمای عراقچی به سمت پاکستان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136072" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136071">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5o1cxNIKxf0lbLJQSX4fB9mXJWiszoH52UH_CLD6TntdBeZbken_OO-64R5PoDALCZb2QCC24QrleA6BP0XN1J77EWMuwrJrarFA2rQFfwLblEgYxqIX8IxwN960hgGiZ0nM4yDmnU0kIeQToyrWh533vZuMgbmuSstz6-y8KcbauXVIpH1AX3kYyCETl2KTuE7oeUf2h0adzoCSUhdSlh3oeqvrUttHscmOvi9wIkWWvqPpUXvq1AnAPkIjTLyqqQJBXaE3tfKaUIR9XbRNxKkmM9IGyVRKZngF3i7Ox5Ho0l_hpll7JiBEDEOOEOGLV5rhJQjToPPjPyKZ2I6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ یه عکس دوتایی با لیندسی گراهام پست کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136071" target="_blank">📅 18:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136070">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
یک مقام اسرائیلی به خبرگزاری Axios گفت که عقب‌نشینی نیروهای دفاعی اسرائیل از مناطق آزمایشی در جنوب لبنان از روز سه‌شنبه آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/136070" target="_blank">📅 18:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136069">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فارس: دولت با ناترازی جدی بنزین روبه‌روست و گرفتن تصمیم دشوار اقتصادی طبیعی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136069" target="_blank">📅 18:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136068">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
صدای انفجارهای مهیب در جزیره ستره بحرین شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136068" target="_blank">📅 18:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136067">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfRiXpaBLS4HEDlG6_1-XrqlAeAQ_6EA8eKLOX4lLOpdeA_BJb_lF8Ob20amEX-mlaQq4YV_WsW5hub6khwcqGkPF7e6cw5LJJg8nFx-uKlxYPWwnseGYCXSSK-mcxD8ec54fqjfusKl-YtR2iFJz-RkYwZyAjBxSH-1XkYpPScmUdA4pco88R944vnT1dMT7diFpAYWFPzpBKS8VSHvLXDuWLQRemFLbus015ixqno8yVVqp3AQz4ysKySB7jmWW_1rr3NX6PziTDDoYrgnLpHDjUxUMDhBpC0hqNdwh0JVa3R5BpBfV9t91zD2v64Yrmkd22uszM1Jx72_liicoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمون شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136067" target="_blank">📅 18:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136066">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
العربیه: دوباره آژیرهای خطر در بحرین به صدا درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136066" target="_blank">📅 18:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136065">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3Ne83jjbgEJXnvJtP-dFdMlrY11dm6vVqdU1wbv9KTuxXtZ-zztOZbPYs_LNI8VP7HLZfA1u_AFah9-5DeOatOnaL10ogr_RT9Etg3U_kz52xWGXXM3tm6g9ceM9yQ3EejUcRoUwmc-ysDTNFEA_v1PjNs9zNM7y690B7iJIH6famLphFO9-r9JjMZoLRt3QBrH-sjDw4Bkg0Kx5dDP8Wa0ibJTfp0O2QKMB0YmaKDn-vV6sSTtOaazwVeszc1R9l52sMWvMzumnZ7CBoRTJx2z22PPyL4md17GcNbc81U4cnVzgoOcyliTGNN654AbXlfQzHgXQBbsr_lzYz7ZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از رد موشک بالستیک شلیک شده در آسمان شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136065" target="_blank">📅 18:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136064">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ویدیویی از ستون دودی که در شیراز نمایان شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136064" target="_blank">📅 18:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136063">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
الحدث به نقل از منابع خبری:
وزیر کشور ایران فردا با فرمانده ارتش پاکستان در اسلام‌آباد دیدار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136063" target="_blank">📅 18:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136062">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJoH7pQm59-tuyJbXJ31OEUH70UqlQmUnZB4Q6nSOj64ycZisCrXqLSj_b2hlsWAdm7BhL8sSAM_UQVMSDxlAE7S6P2u_eOCTJqyyvlbABUcZVSPN9CyWLURBbJGRboAsCt4MkW7pfu69ERxhKSGxYflsSDugGxnoY6GW-Ar7HUh5CiCIsTBlxPY2pl9D8x2MVWrjfTEWMcwXhRXLmwLhuDp5lcSuE5MfumWZqDTB997PRJ7ToR_IGTSvrnsIm_ocd-xs4G2Jbj8VfLI8RXs45ukUpIa53K31qPQzOyqUtwYvNGEzHXkh_GzQFaKAKSGwxzqoDT5V-xUOph7Da3QXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا: یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136062" target="_blank">📅 18:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136061">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gj8auJqCFFi8Q51AITr-Zje6oEIl1VGuraXyBaNkjH7TrJTW6NJ1xf3hMl3EuowEHeWAjMbHOIH-us1_atRZEYGhgAvGztCHmp1VAqigDNj7V5oEtZmIL8AwoNNVrgJuI67OTyzY7yLh_PloFTJIVkt0qEEKHWeZe-c-H1Y72b4G7N2GbqVBMaOXNULHnCGdej2Cl-R4MfGFD6LDKNBWO-qbjyrO8w3IdclONxYR2Szu5gcu7kL6B7goMOx1Nj1F77-SUU5GRwfbyohkI8XfkEd9C0w7kFC6SHjVJ9w0atqBECiStTmpGVnMenecOS94o22VLQXRSFze4goz1HDjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علوم پزشکی لرستان: دودی که در خرم آباد مشاهده می‌شود مربوط به آتش‌سوزی در بیمارستان نیایش خرم‌آباد است مردم نگران نباشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136061" target="_blank">📅 18:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136060">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ویدیویی از ستون دودی که در شیراز نمایان شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136060" target="_blank">📅 18:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136059">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9QyZf8uXUq7TyZxLKu_NzBWgfodPy-2wyHgeT9VmHA8UsaqTjF9ZHXsYOyjqZe0U4lRtH7g1dEb5ZY6WBOv8yaXssJTEZkjs2IWRzUfndDF3rdZDIFZV9UgYd-SYTATTk2NkEwY6Z5hxdcB9KsmD71B82V6XDYeFjiBC2i0qrsoH8ObpcWnASlSPIpas8x6e9mRNwPzdhUah15nsnmZOY83j4ZsGdQadimyA5qSVDCcFHp97ld8KjFNIppSt7-IXJbBEpVV5dRBXl32XfENURjsLi7xrNFy5OZGMphPPqkVSQgVcw_xmGkseLNUoAWrar5DR3FuEOxw_rFTCgsxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش شبکه سی‌ان‌ان، ایالات متحده قصد دارد تعداد بیشتری از جنگنده‌های F-16 و F-35 را از پایگاه‌های مستقر در اروپا به خاورمیانه اعزام کند، و همچنین هواپیماهای تانکر سوخت‌رسانی بیشتری را نیز به این منطقه بفرستد. این در حالی است که دونالد ترامپ در حال بررسی گسترش دامنه جنگ علیه ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136059" target="_blank">📅 18:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136058">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3186bd6880.mp4?token=oRCY6Y3i-aKdImzUH4uL2MR8p7A32YJs4c74TzAod__lVgO4cS2xTwxKeCSgH5Pe3jX8N3VeBvXARL8aXj0YTDf5nrfzP8RJFO_vkzw5Okmjh0eI2jRKF8B4fbo_eyPwz3SR06Dc1hbh7OFgrYdHz68Eepw8d16jcV-MwCJB5SKP5k6Hq_82UXXmzoBw4SZHzcCwfLbNe9frMYlOjkE_o6ociKmfdDV0ff_5nJ3GIfB75yYY_b1GW0xCrWm5NweKiiH3rOpUh1d54s2IPQiuaILBuciNmlqoDWfxNr1p2b-yWjxuVYwX32QYgPDjkPyt1s3TMBox99sl-T3zi4jfEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3186bd6880.mp4?token=oRCY6Y3i-aKdImzUH4uL2MR8p7A32YJs4c74TzAod__lVgO4cS2xTwxKeCSgH5Pe3jX8N3VeBvXARL8aXj0YTDf5nrfzP8RJFO_vkzw5Okmjh0eI2jRKF8B4fbo_eyPwz3SR06Dc1hbh7OFgrYdHz68Eepw8d16jcV-MwCJB5SKP5k6Hq_82UXXmzoBw4SZHzcCwfLbNe9frMYlOjkE_o6ociKmfdDV0ff_5nJ3GIfB75yYY_b1GW0xCrWm5NweKiiH3rOpUh1d54s2IPQiuaILBuciNmlqoDWfxNr1p2b-yWjxuVYwX32QYgPDjkPyt1s3TMBox99sl-T3zi4jfEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از ستون دودی که در شیراز نمایان شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136058" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136057">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1xhMEEwZhv_eEDOUf_nVrsbAdFQlS1EqrKOtkCMuZnZ4WMGdORjZomSZPyPJACJfZ1oL20arM-tNjSbZEG4bFwH68S5Vnnn8qYdPbSgyk3pDTqrcs_qsTx9fHTzTZhg_FbN7Ek-v-x-IQ-yunH9UUXV94WMAUksKafS-g68B0Phh4Z2WVdgxDN3P1KhITjRci_H3EzQjDVKQhelku1pN-kS9VFlr0LuYdHAL-HpcI1ELCklRATVJLJY206E5kg4TceVIoggDHqOvIaLL07ltzALyaqXFnqH1dzGv0pLJvB5JD4dVw2Tj9k0XLSpGnsVvLPdiHFyWV5UHJzPXisMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136057" target="_blank">📅 17:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136056">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / گزارش هایی از شنیده شدن صدای انفجار در شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136056" target="_blank">📅 17:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
به گزارش نشریه "گاردین"، نخست‌وزیر بریتانیا، اندی برنهام، برای اولین بار با رئیس‌جمهور ترامپ گفتگو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136055" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری / رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا: یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136054" target="_blank">📅 17:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزیر کشور (مومنی) عازم پاکستان شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136053" target="_blank">📅 17:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136051">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtVBju3NtXcUxRu3WOFkr0UVaDICXPVONc6L0vRnGOMUHwI1YATagsUZ9g9TI7amMALjb17-3h4UPzVC0QwpgmjvjfctUefYjH76-QEix1Dr_dmNGCNr8gHj1HAbpPCXhRJS0HryJLaudHXSXuCOy1eZ5P07P1lAmT_c2_Wwr6dW9rmB9WS3ypB3E9P89psio1oCt22ziDK8NVXCqlBWVKSvp98Z2FC5xG--jXdean5S_3bkKrnSFEGRrL5yqhCRvukELDNo1yF88QFTwvPOCk8aN8gnII22pucZSZb1A62wCSadpOmBUAlXrPF5XvkQf29vGja3UZl0BWAVIakk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/289f1a32da.mp4?token=gpVb7XpBNl6gGHS5OCbCmD52EXdMllLu2hXALk2Ed-ynFLg2lT96qLhLLY47zot06IrMrWyMxxKxFFVuMop0jWaxCP4XLzNZ4yH_6BjxpSxUTGUjdtObDaAUv7BbOcY-E2O3R0gjf5z6GgDB_ZIDZ7TAyFfkrpIPb4M0Bg7r_THP2ADfIXrF3ih6tdjxAuPMDlYSK0WHaGG9peWCiITrYU532OZ5jw70Vmik0si52rp2zLDOifrApuEAX5YwcFleJ0fm6LWTat9MioyuOMkUdMXpdWxMgmPSAlK_nw85A9aeYRidACj8-qUfCvtoDESP-Jq-EB2zqsHr7RBpKJ9zow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/289f1a32da.mp4?token=gpVb7XpBNl6gGHS5OCbCmD52EXdMllLu2hXALk2Ed-ynFLg2lT96qLhLLY47zot06IrMrWyMxxKxFFVuMop0jWaxCP4XLzNZ4yH_6BjxpSxUTGUjdtObDaAUv7BbOcY-E2O3R0gjf5z6GgDB_ZIDZ7TAyFfkrpIPb4M0Bg7r_THP2ADfIXrF3ih6tdjxAuPMDlYSK0WHaGG9peWCiITrYU532OZ5jw70Vmik0si52rp2zLDOifrApuEAX5YwcFleJ0fm6LWTat9MioyuOMkUdMXpdWxMgmPSAlK_nw85A9aeYRidACj8-qUfCvtoDESP-Jq-EB2zqsHr7RBpKJ9zow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کشتی ای که ایران اخیرا بهش حمله کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136051" target="_blank">📅 17:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136050">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDeR1r_hKnB_dA3OiO1rIvaWh4sohKpd7nmHShDzQenqa_tfKeX-zj-ti2c0DaMm8tA65S0okCNNCv5A66C_06dE9PhwcHHZ7B0OTF1-zy1xicnQnx6QWGhyY_76FkRS5u_v7zKuJLPONsQhUamFJ9f-an9B5AmGjnhZ94QQ3K3aLaQgzBpRGtAJxqA19zxiZ9nTehFk-sQI0yxHJa8Rwru87psVQ3aXQ9NdAmohwmy2tTU7XqcbGKDaPXA0t02hN1rqaKDZ6NSM_Lssy51WN9UzFHOUlrQr3hDbRoctTK4FnkIMuO3h-IldeI310au-frQQZ4M864t849pQwj_NUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه، پلتفرم "پولیمارکت" (Polymarket) را به دلیل فعالیت‌های قمار غیرقانونی مسدود کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136050" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136049">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9085a568d.mp4?token=iKtsegUc-0qt2NEqYoiEKaGGvFPA1k9Xpl0LEFSQ3BDArRr-MdrUTK21_MFRevPjrj7-ukKQIbyUU4sHlX2TbHdD5ci_p8VnxM2Mf0s_6EG5YU3sQ_TIwsaagBAW0YPOTdspTjcOuLny-qVISNW_ehKmVPv0qV3wTTbca-twU78qOe8VK_vwvRgsOu0WLx8PEk6whVsANx1y72XDrskxHJsvhh_fsi5NtWKhP8r25svOsX0ZJu6xEzS8WB7Bf5RZ5z0ze2iDvtDBoKUaWAOJNLcoLoqTewqffZW4Rj18g_8JrYCxi1Nl3Zs-d6EWC1-CzYAE1Yz-OrkvY0BQJ9oDkT8ufrubaIZbz861vBLlGUVvj-3KCwV6iJLXSIaephkyb2APFZD5QDtP0UzN8IuD77bQX2azyYr4G4dvn-8F_04gFdMhpghfMqN0dMbmmT_WbVjNqgZUKqYdOZv2ZJ5k2BwhWks6-BSCfYWdS4yR7P9K3flo-ztyA-6T6muyv0GbGaeonuEBokY7z6idlnLseleBaIT5iNaKK0T8bBa9ZwQhkAe7o9mBsc-ZZkbe3uHFE4BDyolEBkssItY8bjHKW1uFf6jFxASicYAceHgtb2OqM-Paxf_hOxF4YXTpgba3An-BCL45nyktPD9iDTd7sKmosPZzx3jGPToraqVqQH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9085a568d.mp4?token=iKtsegUc-0qt2NEqYoiEKaGGvFPA1k9Xpl0LEFSQ3BDArRr-MdrUTK21_MFRevPjrj7-ukKQIbyUU4sHlX2TbHdD5ci_p8VnxM2Mf0s_6EG5YU3sQ_TIwsaagBAW0YPOTdspTjcOuLny-qVISNW_ehKmVPv0qV3wTTbca-twU78qOe8VK_vwvRgsOu0WLx8PEk6whVsANx1y72XDrskxHJsvhh_fsi5NtWKhP8r25svOsX0ZJu6xEzS8WB7Bf5RZ5z0ze2iDvtDBoKUaWAOJNLcoLoqTewqffZW4Rj18g_8JrYCxi1Nl3Zs-d6EWC1-CzYAE1Yz-OrkvY0BQJ9oDkT8ufrubaIZbz861vBLlGUVvj-3KCwV6iJLXSIaephkyb2APFZD5QDtP0UzN8IuD77bQX2azyYr4G4dvn-8F_04gFdMhpghfMqN0dMbmmT_WbVjNqgZUKqYdOZv2ZJ5k2BwhWks6-BSCfYWdS4yR7P9K3flo-ztyA-6T6muyv0GbGaeonuEBokY7z6idlnLseleBaIT5iNaKK0T8bBa9ZwQhkAe7o9mBsc-ZZkbe3uHFE4BDyolEBkssItY8bjHKW1uFf6jFxASicYAceHgtb2OqM-Paxf_hOxF4YXTpgba3An-BCL45nyktPD9iDTd7sKmosPZzx3jGPToraqVqQH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم مربوط به انفجار در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/136049" target="_blank">📅 17:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136048">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/صدای انفجار و درگیری در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136048" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136047">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTA2Qmgb-lmFZ42h30v4d3Z_GF63l0svvn6Jx5hsDs7TvHOBYpv81lpmO1d-goD3jOmOjP1fwaPDrjCv8KHFA8oI2tk7qezzB8NMrLLT8Zf_DDfaNl4EQprZvGB6PE8A5sg1Uv1SQpMulZFbfdE7772oI489FqFiAQtUVy7lg5hF-3Y2IBpK1K-nttUYqF5G-HmIPGk0Q5Zawu6BB2ADVXzCqia_Ci7BLwq5hWMGdg4UTTyJodw5V-bU4tGF95ZUmdai5s1aNBuMHuUq4DosGbIdoc_IlESPVHFjcM_PXGgMbDgCzU7ZIDVGBcV9-r-2sfw69nJHEjFLRDT5SS-rNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوال عجیب بخش ترجمه امتحان عربی یازدهم که امروز برگزار شد.
🔴
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
🔴
ترجمه :  نقشه دانش آموزان برای تعویق شکست خورد !
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136047" target="_blank">📅 17:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136046">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345c5a30b6.mp4?token=Uw8g_ZNo7CMdeCx4n1QHpBiBvdFiI239SnywDNPdTvUOEkBPGmJ7dnlp1amOgh5HIj-3IUVei6a1L77gtclM_-ZBCoTI4JAybjEtfV05_obqJeM9Fum_9NSj-Q5cl_n-ABSMbjbQPEkow_ZZ4Q3qJb8LV4P1BwqDLc9E69znlQKiQYdmgniVik6K0G_h4lB_-FWHPdAktSKeweamcjkSUPhSiYkU4hHLmWnEpVi2C0E7n9iMSYuO6h0IWnNHwcMSUc8WD9QshILqpzmmS7MKA7dxoKFcBC2P1resv23SoAMrpk0PPaY7hCuA9Q98Z0FF1-GhJYT1Ev8FRx0CcyMXU01_zO9U4iGk6EL9Doejhm4sNn73ENGnOx8WEVFbSLQhE1YjSsbLzdLpIvntNeIXVdWADJr0ox466cECfEtpVRiYmIn2eXupJnswVXKQPbfaBGVmDtCpwJFLPLIL01tJ6g9KURQaE5KkdVTwMs9LGXAOlAfm8tn0z3Yx9LA5hCfxaUBZEs0_nhUB9QZL3LAUlJX4Ww0rX0eoMEmhw3TW6-48nMKaBNbDC4qpnNNo3MYTYKMIrKb975F4E-IHeuVcW9dqrgOiDPJqip-U9ZBRRIyn_rJMiGIb-CsBeqapMMQ64EORkFQUfNKg7_waNmPu-k5NtpXVb_JjK_-gtZgpxs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345c5a30b6.mp4?token=Uw8g_ZNo7CMdeCx4n1QHpBiBvdFiI239SnywDNPdTvUOEkBPGmJ7dnlp1amOgh5HIj-3IUVei6a1L77gtclM_-ZBCoTI4JAybjEtfV05_obqJeM9Fum_9NSj-Q5cl_n-ABSMbjbQPEkow_ZZ4Q3qJb8LV4P1BwqDLc9E69znlQKiQYdmgniVik6K0G_h4lB_-FWHPdAktSKeweamcjkSUPhSiYkU4hHLmWnEpVi2C0E7n9iMSYuO6h0IWnNHwcMSUc8WD9QshILqpzmmS7MKA7dxoKFcBC2P1resv23SoAMrpk0PPaY7hCuA9Q98Z0FF1-GhJYT1Ev8FRx0CcyMXU01_zO9U4iGk6EL9Doejhm4sNn73ENGnOx8WEVFbSLQhE1YjSsbLzdLpIvntNeIXVdWADJr0ox466cECfEtpVRiYmIn2eXupJnswVXKQPbfaBGVmDtCpwJFLPLIL01tJ6g9KURQaE5KkdVTwMs9LGXAOlAfm8tn0z3Yx9LA5hCfxaUBZEs0_nhUB9QZL3LAUlJX4Ww0rX0eoMEmhw3TW6-48nMKaBNbDC4qpnNNo3MYTYKMIrKb975F4E-IHeuVcW9dqrgOiDPJqip-U9ZBRRIyn_rJMiGIb-CsBeqapMMQ64EORkFQUfNKg7_waNmPu-k5NtpXVb_JjK_-gtZgpxs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاشار سلطانی: جمهوری اسلامی هرجا پاگذاشته بدبختی براشون برده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136046" target="_blank">📅 17:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136045">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtncL9f2_txys11DxA4huCdwdIoWXlvt8IaQgdIdB7IQhTOB4sDlFdZj2RohI0JdfjixMrn7ZxHFZtTHfCn7LYVYHogO2mv7T_nX01fuQ-xm529r4MRG15nR9SSdhNQsAjncXkH-Ub7LSi8Pm2XodZN7GQ7JCp3hZEok-P-IwJZUGo1Ai-6Zp0_G4X-VGH8NuujAn3Nza79Qj_vvN4PAyqO3DJyS2r_rZ5oOjcUmK1V-xq4Ix62-jb_F3Y5bjNt9goI7hajtley9RpRvtwK1YbA0DwF8nynT8ylgk2-bSamyy6gfz8xpkjZlmXZTxtjx0rghrwwDmvbm2fJdImA4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه مصر حملات ایران به کویت و بحرین را به شدت محکوم کرد و آن را نقض حاکمیت این دو کشور دانست و اعلام کرد حملات ایران باعث بی ثباتی و آشوب در منطقه شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136045" target="_blank">📅 17:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136044">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
گزارش انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136044" target="_blank">📅 17:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136043">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4hYlMHuq0gV0VgjUbBtEam8zUKo-1wH8bmWcjsFZWdXkkaVx0pZDfQqq3sVcY893mqgvx2ILP4olPP2XZpuyWh5Ho8GHUw7W5YottSofQUzpEfcFRFOrmQriesvJtYrjlvYtEapN84M62PUp__66eFGqLpiPiRlqdAyrmP5HMfhK-xyZsOQ6GND6njtUT0YvCQ1cJZzYSeEOKfWBaev6FcojsPm0APvUr9wNXbYRctLzUJ9N9m8C1r9XVWe-LmthBlg8ooIoRR5a6LZh_G-ea88adhW5p0LcDZ8qgyJylW8LJP2AKRr-vUJ-XZ_ZrDewVhqTgbOpi6sRJKT60Phdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت: درحال رهگیری حملات موشکی و پهپادی از طرف سپاه هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136043" target="_blank">📅 17:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136042">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZeNNlylGFY3_2rqUDwcS0dN8K1wepUIjVkjKw_bQRYp07okWFnfw-de3OlC6ZmX0C-HgN2AGF0VPvn88xfE-1TD2TgYL8Sq_e2OC9Lg_sPzu4vnmqsk26NYpoQsIKQuCAXDVpofi9R0jgXQp86M4TjcSgMfuCe_gZYmuHL8ZM17JnoPss1KUK_KPm46ROax2XrLGqKI5PvFXeT4HMSI7um7NgNDjgXYBy-Yj4oresMHdlpUEFkKQuJlchHrtzOHZgPs4jea2PnVk4LBFESyCwpmhnaPIWLPla9zFXfQgIr5pd8N-NNYmQn236usEC52ZFEbijuzUK3wErjUmtTc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت شونه تخم‌مرغ یه‌شبه ۸۰ هزار تومن رفت بالا
🔴
دیگه املت که ساده‌ترین غذاست زیر ۲۰۰ هزار درنمیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136042" target="_blank">📅 16:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136041">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
گزارش صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136041" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136040">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flaH2AZ7EkZv71Luwy55y9BZVUB6PbuCEzqTW41EcbzFjJPDZUPSW3qBXVqnXR8-T6kuBXGqVnHAjEbpYLAlDOuPLJdSV4FRgvv4rLbxhZswlrYwD6is-uhj0Hd-Z4fXzv2tixOaRHPUIvUe8APtv9nRf6O6HbuKdkH5gTLqkehAubcTZmzHQ9sFaHStXp3fSETsv-CSUyvns7uI0YOKbzDA8BGaWW8GxsJiI6z_BP5P4qlTfdBmfToFMjQabxuNsZipu1BB-FAm5YmHy7FZkko8isJWASJG9rYzal6zJJSPrlfTlqsW3MEBtqpUHylkJaAHOzrNzHFqiZ64syJ9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستوان یکم تایلر جیمز فیهان، ۲۵ ساله، اهل اوا بیچ، هاوایی، به عنوان یکی از سربازانی که روز شنبه در اردن کشته شدند، شناسایی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136040" target="_blank">📅 16:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136039">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/empD6fwNIFBlAOvVtsFcwArV6wdbR41fpbHDJ39-n-9PuHjKQ4SUgSztE-PDl6K-r4fWBS4CNANl9avgf2kSHqphu_wQ4I2ReXeHsIBcnEQV5IWXtYOLasfaFOa8Ma1jrXD9Us4WfyFeDH8heskX5ElQmctfMuNh1YOlZbtO1VupuMIgE8Jx-p7N1gwU_Q1cb5FoudMOOT5WgB6HFMGpdHaJhHLr14zfUUl_UjhbVbEpAyo_5jE0Vo--GJE6OWgFOhjSvKfQXeqcN53qed0fG3XblY_sNxv7J_nPZrpWZGGSZCSa2Mt_xU7T7zzpYLlYQqfWNZWRo9B3pMFMD35T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی: حملات آمریکا نباید متوقف بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/136039" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136038">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4x59ofCjLQkoK2Xy2mGZvitIjkTj3wte7T23dvfDRASNceRxX8dyimPBoslZjQsQi7g6zNkuy7p_vA5v87v2VI2SzbCOM5xvC5DGeEDsN8ircxKG8SQ85WFr_1lMF1mW0IEUhz1YAOpRmu0xVlO-I6DY7o02MehB3NDH9YbQxraxCNt_KZe0-R2xj00O96nTNFbLFojtf5RCvPqUCELW3kfU-oqzImuRPseZ55e1xm_jaFwZIggbTj5xvYf_H4UzBWT8szqFHpWjJ5-HbVjg9LoEkuxA4wh6moucUVJijghsSs_xoCQtCQcvq1csqEJJMBZw8-VnagfDwz00xqktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از سرباز آمریکایی ۱۹ ساله که در حمله ایران به اردن کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136038" target="_blank">📅 16:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136037">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldp_dMZ0DPYn9UuxTLcPau43zKzQQvqOTOlrqBSVgwarmQm3qwbvEKIEHwYhEdRMW4KaB8huNGdCcuaZl0J7xZBvCkEAkW4tt6l0WlE8x5EWCTbs5SNZ1FjX7MMs3lcanXxBYFnKHyo2TT36Flci6S8YE_K2Jvba2e33I4I1jxUwrkPBd-_XLzBuhszTzEmMFPjqfeKdOqj3B8MpEQfAn0zycQjfXzjLM-hho5HpgTwjmaRIomoYrH9566cKixxEesBu1dFmrA-OH7m1coYoCGCRkjKIFCOWBmAT_7CI3jTIqswZetYtoB86yATJYwBzyHYx5zOLqCQPnxKuc_FWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت معاملات آتی نفت همچنان در حال کاهش است و قیمت نفت برنت از مرز 87 دلار به ازای هر بشکه پایین‌تر رفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136037" target="_blank">📅 16:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136036" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
👈
فرماندهی کل سپاه: با همه وجود، هم‌صدا با ملت بزرگ ایران، فریاد «لبیک یا خامنه‌ای» را از ژرفای جان سر می‌دهیم
🔴
ما سبزپوشان حریم ولایت در سپاه پاسداران انقلاب اسلامی، پیام حضرت‌عالی را فرمانی نافذ، میثاقی الهی و نقشه راهی روشن برای استمرار رسالت دفاع از عزت و استقلال کشور می‌دانیم و با همه وجود، هم‌صدا با ملت بزرگ ایران، فریاد «لبیک یا خامنه‌ای» را از ژرفای جان سر می‌دهیم.
🔴
میثاق می بندیم که پیوسته امنیت، استقلال، عزت و پیشرفت این ملت را ستون‌های ایمان، توکل، خوداتکایی، اقتدار ملی و تبعیت از ولایت پاسدار باشیم و هرگز سرنوشت این سرزمین را به وعده دشمنی کودک‌کش که کارنامه او آکنده از عهدشکنی، فریب و کینه با ملت ایران است، گره نزنیم. تجربه‌های بزرگ این ملت، ایمان ما را به این حقیقت راسخ‌تر ساخته است که راه عزت، از مسیر مقاومت، هوشیاری و اقتدار می‌گذرد.
🔴
فرمان حکیمانه حضرت‌عالی را نصب‌العین قرار داده‌ایم و اینک که آمریکای جنایتکار بار دیگر راه خطا، تجاوز و ماجراجویی را برگزیده است بر این میثاق استواریم که ، «درس فراموش‌نشدنی» را که نوید آن را فرمودید، با قدرت، قاطعیت، حکمت و اقتدار به او خواهیم آموخت؛ درسی که هر متجاوزی را از تکرار خطا بازدارد، هر طمع‌ورزی را در هم بشکند و حقیقت اراده شکست‌ناپذیر ملت ایران را در حافظه تاریخ و ثبت کند و مسیر حکومت جهانی مستضعفان را هموار سازد.
🔴
در اجرای تأکید حضرت‌عالی بر حفظ وحدت و انسجام ملی سپاه پاسداران انقلاب اسلامی در کنار سایر نیروهای مسلح، صیانت از همدلی ملت، استحکام جبهه داخلی، پاسداری از سرمایه اجتماعی انقلاب و جلوگیری از هرگونه رخنه دشمن در صفوف به‌هم‌پیوسته مردم و نظام اسلامی را از مهمترین وظایف در منشور پاسداری از انقلاب می‌شمارد و بر این باور است که اقتدار دفاعی، در پرتو وحدت ملی، استوار و نافذ خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136035" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136034">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری/آژیر حمله موشکی در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136034" target="_blank">📅 16:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136033">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gwq__qZVu1YIhAXeJEA97tE9QwYyE7Pl7fZkp5GyoFEzSrjK5-5bibACLaS9ZKMPHVChwKtsJlDlQuCgbsWu0g76-4D-UYBkdhuJAyBvWEsnF-3IyfPqyOARDykrridNEcbEF6bUX-pATkG42CpiKQz9SazPibxWtm3ONYW3-LED0BpgQKGSyIn0FXILboEN9RzWZbAXqZoiRyzApoeJownuQOjHN2QY256Fi44LPqNxCEHuplGEhx2nFxWEDsdmH4JJJJ9NBnA9NZrZEpiwEwnoW81Sdru5iZGILSru-9V9CUOJXyef4YdRAms0bYAH4Twf-1rO-PB6H0SORUJpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری تند حامد لک علیه بیرانوند
@AloSport</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/136033" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136032">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYMncsJXheDGBy9rFU-tyuO5W7t68C9trAjcfPMLKRu4vQ9nFMQzVjuM4bm4aomX94EJrleK2pAtVswhxu4QZzGPN9VhtkvRA-LZ_Fqa5Yfmj1FcPXQzc2_sp9Ry4r-2-GO2nDDqSshw9v0le9an-N7f4_uJp0gj1QNspO5IvJTBvSPiv659rEDQM-fum5THYOhXZVM1E2Pxu2tdUkp-mbqtLG-V7Mz3rr5myv7iw68k8jp7v_p78XAmW4MDGpvdPljHrvWUVSMf9-NZ_L5saTdiNdFLj5mEnK_juYbs9VhyBKCYvYfaxvQ8RTBVztsQ1kvASEHXFytMGmkzggcnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلمب تعدادی از کافه رستوران‌های خیابان‌های سنایی و ایرانشهر در تهران
🔴
از صبح امروز تعدادی از کافه رستوران‌ های خیابان‌های سنایی و ایرانشهر در تهران پلمب شدند.
🔴
جو کافه، ۱۴۰۱، سام کافه، دو بار، نووک و تئوری از جمله مجموعه‌هایی هستند که تعطیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136032" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136030">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مارکو روبیو ساعاتی قبل : ایران کشوری بسیار غنی و با پتانسیل بالایی است اما حکومت آنها علاقه زیادی به حمایت از گروه های تروریستی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136030" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136029">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEMwaPhazZ6hesxqbFIhM2e8RUedFxviywVnZqytbuwLeY0BbSl0rZaTeh06akBpZX713txW6vBhg7ZC8wSnMdlZ7SIDe1M2BVbWRctYd2dPGBvfSdw7dnh1bqJWZCzrXRnR3TXsXaGbG6llfaPgcOXmpLrKrvgzbmdXkqwohi6jfUV0hVPfVdCAXttiQOMTGHNV2sYHoNsj5yOaaEneWv1_b7Y5KyMyRjZ_U6ooYHjXX8YkO69TRegiB40vkEDWGwLoYpJ82rw4ZIZG7AjlPyCWWikIUuGMUdci9nDy_sF_Ek6KAOQHAIZQiPAyxTjvu5cQE6YJgvj8UAvXpZfPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیلی‌بست: ترامپ بالاخره مجبور شد اعتراف کند که هواپیمای ۴۰۰ میلیون دلاری که قطر برای استفاده به عنوان ایر فورس وان به او داده است، به اندازه مدل‌های قدیمی‌تری که بارها از آنها انتقاد کرده بود، امن نیست
🔴
️پیش از این وزارت دادگستری آمریکا دو خبرنگار نیویورک‌تایمز را به خاطر افشای این موضوع، احضار کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136029" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136028">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
دلار تا کجا میریزه؟
این تحلیل عجیب رو بخون
😳
/
کلیک کنید</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136028" target="_blank">📅 16:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136027">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlS1bds-lvJ65hvcMTSp_g538xPUgjSvNBdwUv5f4HdV_P1zZrVPrKbdlSYLPxYSzNMzeaAEUHGq4eyG1iAbFDBZYInEinIwLw19SeZjauoCPTHQ_v4NJR4Bm_vK9mryN6TXDTY0wvRy5iK8c6b-O653kS82u2Z5vpucK7lHhDa5cDBAlmPeK1a4twOiVvitehChNl2jEiZeGnkuusX3IGN7oKRxSgulEEFkaIwQEasEnZfjfn1FIpF3pdfoIZ_fRB2OXhFRO34nPDR2edVtQd14TVIT3bFAbVSyT-S-luQFHKEHBmr9mqgvYauNbEO1X12GUAi1C9YeUgEr1quXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه: پس از آنکه ایران اعلام کرد به دنبال ازسرگیری مذاکرات با آمریکا است، قیمت نفت برنت و نفت خام آمریکا کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136027" target="_blank">📅 16:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136026">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
دلار در بازار آزاد تهران: 188,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136026" target="_blank">📅 15:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136024">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Kv10zWldvzx3uPp03QQd-HbCnCFNbcvzx7B4JrsYCv-qvpD7YJYP3sqISGWMwMLX6Gqja__GzzcSJ4xTT7vH-ECJpFYVI9NVR9bm4LTzhmS1pJDXN3si80x5CLpYKyBk4DIS4z8EtySKcezPQmkmR_JZ6vO-w0U_jT9mwWZ8fHWCklHHZ1MzWtfdCiUYDuQRrvWPzGgsgFZpcQSq8oyZm0uvThtlIw27uByLE1ypt48cS8kBxi2OuGRvisOw9uWzGFqWwwWIGItKUbiTySx_sxzeGEFMSdilVMjnhlEOOfPVSG4BMj4DNy8D1s8yTAvLWcFkqmhFnimg1t53raqpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/txjBB87yTIKBd9kWAkAgBE78UaZG0xHeOgPjoJ-k78Df9i-a8lm-MszIn8ISmRT7tEFrz6B8EKy6U1t60uZLAdxJHcVToUgQH26J5JFeR6x9WBUCTX-lfpl0z9-J0fwXkzXcM0J2aDVAJuqYmlwYAUr8biJdCDy42McHfiLW7hyYbWTjvm1cQHBTCO5aGMnFOZ6AVftk7lRF3gK23cVNEAsy5mV_7VBllCxx_faHOSggS8vkkPc5DaUSZruD7ThdEepBomNqit0MC344_90t55uG2sqYVxO_h95MWgNrA9IzaeNQduSlgf5Ad1KuKaEMSyU3vQspW4QVH8pS8NtHng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
داده‌های تصویری افزایش چشمگیر فعالیت پهپادهای شناسایی اسرائیل بر فراز لبنان، به‌ویژه جنوب این کشور و ضاحیه جنوبی بیروت را تأیید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136024" target="_blank">📅 15:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136023">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0efe0662e9.mp4?token=Zi98If2CSQEnF9WL5pSaTerHTtIuOCe2oZVBELOfrbnUVzCgmXRas43Ou3qX8pW4ieHZabBDiN9AQQ6MF3MS7qZNRaYYDvelanJ5_r03nQ7OeegZ68qe6DNlkCKh9dtpjlCZTQ6G_js4769aNMs7efQ3nvv_sfQQ333yTGJXT065L1JqOFWZdXrLrvIvMDH-z5zbnzkGsn6TgPcBrxFUqB0x3WiX-ukhGnKvUKNCuZXSUmKh8QCqiKiYUg38RppPimvBa0inpUTNiePKzNbhrWIJdCpt5-bjQP9CAK4FbjsRxofizkGDarHCJN3TjszRgXzoevr2LOYGYFM5mu7895RkrTvD6dIHYyg5MlH0okNn6l3liVqWg0V1FBr2W6IDwpZPxFEpdcZWoovfHAYag5UGp4rFNsvN5-Rf6kgz3czMmNbFQPnTkvybtrEOCBoYs1eNYeitROnvXhGu5dpHIhCQ3doJ0rzUiV8xUjJmHxZHjxH5Ewy44KXpNGlkzSjaZ-d78mZJD31INdx8rVHrGsFy25eazx38CzAZewdrTOd5Pc6aLNt6PTOhv_hhOAY7zw67RMYaEKzqKdFLveu4ZhHVeANu8gfIKihDTUhcqM1WoTFZc-hpSqFrIWAJbWI2m-T0uwzoISpNWXRtu0qYjL10bTenFrcOHISHdtD4tSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0efe0662e9.mp4?token=Zi98If2CSQEnF9WL5pSaTerHTtIuOCe2oZVBELOfrbnUVzCgmXRas43Ou3qX8pW4ieHZabBDiN9AQQ6MF3MS7qZNRaYYDvelanJ5_r03nQ7OeegZ68qe6DNlkCKh9dtpjlCZTQ6G_js4769aNMs7efQ3nvv_sfQQ333yTGJXT065L1JqOFWZdXrLrvIvMDH-z5zbnzkGsn6TgPcBrxFUqB0x3WiX-ukhGnKvUKNCuZXSUmKh8QCqiKiYUg38RppPimvBa0inpUTNiePKzNbhrWIJdCpt5-bjQP9CAK4FbjsRxofizkGDarHCJN3TjszRgXzoevr2LOYGYFM5mu7895RkrTvD6dIHYyg5MlH0okNn6l3liVqWg0V1FBr2W6IDwpZPxFEpdcZWoovfHAYag5UGp4rFNsvN5-Rf6kgz3czMmNbFQPnTkvybtrEOCBoYs1eNYeitROnvXhGu5dpHIhCQ3doJ0rzUiV8xUjJmHxZHjxH5Ewy44KXpNGlkzSjaZ-d78mZJD31INdx8rVHrGsFy25eazx38CzAZewdrTOd5Pc6aLNt6PTOhv_hhOAY7zw67RMYaEKzqKdFLveu4ZhHVeANu8gfIKihDTUhcqM1WoTFZc-hpSqFrIWAJbWI2m-T0uwzoISpNWXRtu0qYjL10bTenFrcOHISHdtD4tSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی ها (انصارالله) اعلام کرد که به عنوان پاسخی به محاصره و حملات انجام شده توسط ائتلاف تحت رهبری عربستان سعودی، فورا یک تحریم دریایی علیه این کشور اعمال خواهد کرد.
🔴
جنبش حوثی همچنین هشدار داد که هرگونه تشدید تنش بیشتر از سوی عربستان سعودی، با یک واکنش "جامع و قاطع" مواجه خواهد شد، و در عین حال خواستار بسیج سراسری شد و از حامیان خود خواست تا برای تمامی سناریوهای ممکن آماده شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136023" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136022">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206a60f2dc.mp4?token=NKEr3EFTt9dFj8r2MUg4WoK3tcBD2cW6_D08fu1rRDSxOW8qeHw8wgu6dQAXVFZbfkV4pPY1gMhTxLi6BOLc12BUtbOphANfCOvqmzEzNsiXhCKzV704jZVMsdboYoxdxUMz81tzcE_NXaQ0d-Lfczb2hdvaq9Ew-LUXp6k-ApEnUMO12H7CQJYfKArWQuMs7XzMukMkCugikbNjxBDqofTGFDHgFVbzKta-H9dON4Ud9rhH7PAkpkrcInSuNRZ4JIQCttVIO3FhfVk8N18V9mXs_xU2Wso16RvA9HpH_Tpc_ppqkJmAtLuadGgmUXdKnVvS_ktVb8r_9yBcOEGcbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206a60f2dc.mp4?token=NKEr3EFTt9dFj8r2MUg4WoK3tcBD2cW6_D08fu1rRDSxOW8qeHw8wgu6dQAXVFZbfkV4pPY1gMhTxLi6BOLc12BUtbOphANfCOvqmzEzNsiXhCKzV704jZVMsdboYoxdxUMz81tzcE_NXaQ0d-Lfczb2hdvaq9Ew-LUXp6k-ApEnUMO12H7CQJYfKArWQuMs7XzMukMkCugikbNjxBDqofTGFDHgFVbzKta-H9dON4Ud9rhH7PAkpkrcInSuNRZ4JIQCttVIO3FhfVk8N18V9mXs_xU2Wso16RvA9HpH_Tpc_ppqkJmAtLuadGgmUXdKnVvS_ktVb8r_9yBcOEGcbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / نیروهای مسلح یمن محاصره دریایی علیه عربستان سعودی اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136022" target="_blank">📅 15:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136021">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
حوثی‌ها از هوادارانشون خواستن برای همه سناریوها آماده باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136021" target="_blank">📅 15:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136020">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع آگاه: پیشنهاد آتش‌بس و بازگشایی تنگه هرمز به مدت ۱۰ روز تا دو هفته، هم‌اکنون در دست بررسی و بحث است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136020" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136019">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
شمار مصدومان زلزلهٔ کرمانشاه به ۱۰ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136019" target="_blank">📅 15:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136018">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سخنگوی ارتش: جنگ تا دست‌یابی به بازدارندگی کامل ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136018" target="_blank">📅 15:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136017">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_Q9CenPnn1PsoIOkaQEYWAHmjmZp2ejvFXSasdSVir8BpbzrDHshjuq5K0B6sDGFD-7ujV0pXe690cAa_PQPlmtq1sFyaNtSbpoO8GZy2CRgJxBDoPtvx6qYvnyLZ7ZVBkZ-HQnzWv7S97YRD3rjndzgEA2Zycm_LYv6DOALjvRuHvAgkReAmQOWyR1oNVy2T8q_ohKgr6QZ7n7z0h0TKCSwtZlEnDdmFMt50hrB8zAwXinasMoSnDx6lS8crPW0Ai2pj-1Y1zK5y6kqo1o46OTMiL8mfwGe3PF-4RbNX_qtXQsf2uYHHTrbUHANiwPv7kCxILyilg2A9tOihyiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماس خليل الحيه را به عنوان رئیس دفتر سیاسی حماس و جانشینی یحیی السنوار را اعلام کرد.‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136017" target="_blank">📅 15:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136016">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک‌تایمز: پنتاگون اطلاعات مربوط به حملات اخیر ایران به اردن را که منجر به زخمی شدن ده‌ها نظامی آمریکایی و آسیب دیدن بالگردها شد، مخفی نگه داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136016" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136015">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پاکستان و قطر امروز دوشنبه پیشنهاد مشترکی ارائه کردند و در آن از ایران و آمریکا خواستند به عنوان گام اول برای ازسرگیری مذاکرات، به مواضع خود قبل از ۹ ژوئیه (۱۸ تیر) بازگردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136015" target="_blank">📅 15:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136014">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سخنگوی ارتش: جنگ تا دست‌یابی به بازدارندگی کامل ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136014" target="_blank">📅 15:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136013">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e7c4c5e6.mp4?token=i367gjp_aqwasy2rzqfgCMB4O4hx8p5MWRsM4saXjESFbDxByUvQPqc5f9-qo7_CWfWJLoAv0mTv5efIexXYTk7QqJSg3I_djMmXk0V6PtjHMuFB8c-nBtNPZW9FIWC3V4cRAOmxYS9dqM7nmdyR-AuuZRORaPOO8ApjykNxWY31veLsknOIFA78gn4IVvWulwseKWj36Ym_r3t6ggt-itPZ84E_RX0z7GUQz6_r04qx1k5iiLnW-hUpF7iZNh-tBocmJ48kkWKeUQtBnLpywL4EU7iWJNs0jguyyMnJ1I84Pmtzjl8dc4veMxFJ1pl37xgYrOIxLVxit4TrE6iW_k0L8U3sZDzdZDUCGtK0LN3vf4ReNu2GG9M2DdKqJRgAIn3iA3PZAUPmVVn1-AWEnvQe5lFGsgysJbpmjBkKVBlIiKWOlbF6yX-GpeSEtUPHePG8fGPOkQjsoP3rHlWL1OeWLjs1MSj7uivJPBInSQECfEO6iqIJ6wkDzvgViiN3orfWV9phlac1gC6BHt30GsU-dAe5Fr-qhHncVQpuyE_HOr2ZUXVVCED1_Sn6YsUcA7whqGKre-svmGiUR3ptfHZCYIWLVWDiz27cHa2Ed_jC4VWrGzRUlMAkspHnOCZe0bWDsh5pDwFT82env_zx0opLSKTdsiUPsZlU3l75edA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e7c4c5e6.mp4?token=i367gjp_aqwasy2rzqfgCMB4O4hx8p5MWRsM4saXjESFbDxByUvQPqc5f9-qo7_CWfWJLoAv0mTv5efIexXYTk7QqJSg3I_djMmXk0V6PtjHMuFB8c-nBtNPZW9FIWC3V4cRAOmxYS9dqM7nmdyR-AuuZRORaPOO8ApjykNxWY31veLsknOIFA78gn4IVvWulwseKWj36Ym_r3t6ggt-itPZ84E_RX0z7GUQz6_r04qx1k5iiLnW-hUpF7iZNh-tBocmJ48kkWKeUQtBnLpywL4EU7iWJNs0jguyyMnJ1I84Pmtzjl8dc4veMxFJ1pl37xgYrOIxLVxit4TrE6iW_k0L8U3sZDzdZDUCGtK0LN3vf4ReNu2GG9M2DdKqJRgAIn3iA3PZAUPmVVn1-AWEnvQe5lFGsgysJbpmjBkKVBlIiKWOlbF6yX-GpeSEtUPHePG8fGPOkQjsoP3rHlWL1OeWLjs1MSj7uivJPBInSQECfEO6iqIJ6wkDzvgViiN3orfWV9phlac1gC6BHt30GsU-dAe5Fr-qhHncVQpuyE_HOr2ZUXVVCED1_Sn6YsUcA7whqGKre-svmGiUR3ptfHZCYIWLVWDiz27cHa2Ed_jC4VWrGzRUlMAkspHnOCZe0bWDsh5pDwFT82env_zx0opLSKTdsiUPsZlU3l75edA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرویس امنیت ملی اوکراین (SBU) اعلام کرد که یک حمله با استفاده از پهپادها علیه یک مرکز متعلق به سرویس امنیت فدرال روسیه (FSB) در منطقه خرسون انجام داده است.
🔴
این حمله شامل استفاده از 13 پهپاد بود که به این محل امنیتی مورد توجه، که گفته می‌شود حدود 100 نفر پرسنل و بیش از 70 خودرو در آن مستقر بودند، حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136013" target="_blank">📅 15:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136012">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نیویورک تایمز: تهران و واشنگتن در آستانه یک «لحظه سرنوشت‌ساز»  بر سر جنگ قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136012" target="_blank">📅 15:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136010">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TC6gBMAG8FYSeb8w-1sixRPtn5HQ7eX4yAjgVeRy79xZknK2iZ1lU4_eunU5ULM--hynKGEEMeYdJ06dV_nNvrONhyRZkyGw0a82k0AHeulqHl2jDGvkNi4-AZMBqhomd_bHQRH8KEn8lE5Qp64RS-eFIIpYw7RRvC-Bixu0KrpDTj0qMSUjgCEeSAuBWXeQLWFHlahJAIgliatX-F8tOFhRPFk8sS5XomNRR5U-fWCE1KS914l7rdkdbajl6CJhOEItn44leL0vk1_CLHmnXHQ2fwOpIiC43gLim9bT6t6CMwRyIgnl9oZUsm9A0QN-MI60GR9ZPU6W9I2lWG4Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0vweA4-xejzDWpSBgXlKXdZvRN9FBPIm53kpBqtQv8b2B3EpspWAUtXwcD1Guxop5Xlf4BcIMqPfxFrnNaSSrkvbcNJwDtGBnijNYc2rIHKuVtlvzmm2RxkUgsQdwRC-dG04w4eCzMHX8zZrrdhefjW-dNCMQHVNCRBi3cFcnuXFVKubSbeQI7AQCc4jjOyJoR-2ib_7lIeSDz2Hw1Q_Lz1bsZFnB7tns-hjdmlKWjhUPJ8nFYB_34ZBGAI-zwmebu5ArV2sa6JcT4MLShNgIFsJkMgxc3pg463ZDnSqX52plvkwz3mSp6oFw-u3tXKtf6BYvnuNrrFzMFYewhaPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تغییر  مسیر پرواز های MQ-4   تریتون ، یکی از نتایج حملات ایران به اردن !
🔴
طی حملات گذشته ایران به پایگاه شاهزاده حسن واقع در اردن ، این پایگاه برای استقرار هواگرد هایی همچون MQ-4  تریتون ناامن شده و آمریکا دست به تغییر محل استقرار این هواگرد زده و آنها را به  پایگاه سیگونلا  سیسیل ایتالیا منتقل کرده !
🔴
تا قبل از این حملات ایران به پایگاه شاهزاده حسن ، پهپاد های تریتون از این پایگاه پرواز و بر فراز خلیج فارس گشت زنی میکردند و اطلاعات جمع آوری میکردند.
🔴
برای اولین بار پس یک هفته توقف در عملیات پهپاد تریتون ، این پهپاد از سیسیل ایتالیا به خلیج فارس برای جمع آوری اطلاعات برمیگردد. در نتیجه پرواز های بلند مدت این پهپاد و مسافت طولانی بین ایتالیا تا خلیج فارس ، باعث میشود که زمان جمع آوری اطلاعات در خلیج فارس کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136010" target="_blank">📅 15:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccca6e59cf.mp4?token=PnNEY_dbF80PIrQY8w-nDxo9jb3kN3TrynnQQsCKXlSC4Iuqc7Sb2MYrs5LE6QbrWZBdCi3RHkvzhpgRfHIxwcRlc_EUJk72OpqH0GvkddClDqko9HnBSlMcyZ1X9lZE-zvLr7gtqoxkETj_8KiZZrY-n8vEpzppxmXLhki7O2_uO8gaK5Npe8-ypPbWdOoUv-i48qrXcKVEKQQ9VBfAxTIVgr_2dI0vIqCkkruY9-r3uGYu1N_oZIhM7IlgqP9P8qZLPmOQ8aDTK6kbxF1LGmEKNFgY_HU2t7QpDw3yV57Uqd9VzMV3p6WPOpVVaR_TyQzYUm59vDaeR-y4AeVNxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccca6e59cf.mp4?token=PnNEY_dbF80PIrQY8w-nDxo9jb3kN3TrynnQQsCKXlSC4Iuqc7Sb2MYrs5LE6QbrWZBdCi3RHkvzhpgRfHIxwcRlc_EUJk72OpqH0GvkddClDqko9HnBSlMcyZ1X9lZE-zvLr7gtqoxkETj_8KiZZrY-n8vEpzppxmXLhki7O2_uO8gaK5Npe8-ypPbWdOoUv-i48qrXcKVEKQQ9VBfAxTIVgr_2dI0vIqCkkruY9-r3uGYu1N_oZIhM7IlgqP9P8qZLPmOQ8aDTK6kbxF1LGmEKNFgY_HU2t7QpDw3yV57Uqd9VzMV3p6WPOpVVaR_TyQzYUm59vDaeR-y4AeVNxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پدیدار شدن و حرکت علنی زیردریایی هسته‌ای اسرائیلی در آب‌های تحت سیطره این دولت، شگفتی و نگرانی اسرائیلی‌ها از رویدادهای پیش رو را در پی داشته است.
🔴
موقعیت و تحرکات زیردرایی‌های اسرائیلی، محرمانه و غیرعلنی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136009" target="_blank">📅 15:06 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
