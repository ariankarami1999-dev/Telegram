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
<img src="https://cdn4.telesco.pe/file/hz1dAJAz7YUKMn4vI8n8wN7bI4_Yn8SDCs5GkSkVTmPAybU9qVca62UqqtJOxMys8T4hAMqvcnAURn6BduFGp4A8J_BtUWJCYByslbIfZez0ErOErVGwMizN13ur4TQFdBtWRdRt_hFwALlKUrFZMeatzWOeGSxt1psgIZLMHai5861tOwfEvRQP7WSmciPjZXQQEG_oLQkRYnrtKIhmotdp62tZKGKMBzqIGcBkLRm4IMM044TJlmSV_aXyAEgaRMLLbfKBbP0gO83345hIdGmxTrNOn6Q8KVwyjBRFYJf-QV0cmkfd5XfgA-vcMApwGCMGYju-3NLkjUSJRZ4R9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.6M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 02:32:53</div>
<hr>

<div class="tg-post" id="msg-658623">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔹
فرصت محدود
🔹
دوستان تنها کانالی که وقتی دلار ۹۰ هزار تومن بود با قطعیت گفت دلار ۱۵۰ هزار تومن رو میبینه…
تنها کانالی که وقتی طلا حوالی ۸ میلیون بود از طلا ۱۵ میلیونی صحبت میکرد…
تنها کانالی که ماه‌ها قبل از اتفاقات اخیر درباره رسیدن درگیری‌ها به ایران هشدار داده بود…
✅
بیش از ۱۰۰۰ تحلیل منتشر کرده
✅
حتی یک تحلیل پیدا نمیکنید که به واقعیت تبدیل نشده باشه
✅
حتی یک تحلیل حذف نشده
✅
حتی یک تحلیل ویرایش نشده
✅
حتی یک تحلیل پیدا نمیکنید که با تحلیل‌های قبلی در تناقض باشه
اگه میخوای چند ماه جلوتر از بقیه باشی همین الان بزن روی لینک زیر و عضو شو                               .
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/658623" target="_blank">📅 01:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658621">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88480d9614.mp4?token=G8BX4WUbjsPT-ClJYvfCLEdkS9moahZLAl_6R8ALWKQcppgWkk5mEVGrK9mDlOWmO_TvQqnC6RCD8KhA0uoElcCvDgQW28BWjJfE_ilPz0p0KdvaoUrfkH9tdYB3JZwu8bPsxIdSKqvmHlnT6qU5EpYOiVJ53RfQpeRPgcQ6noUFGlKKuDAyfAWdCO-WBcC4SefEVKTwlcZemdJIAg6yY8Gotnzr1X7LzG30DWYNwBnKvOsHW13XH9P9PNVvq39zD6hxXPnh32-Xm3O6nVfyXq16Vjl7lRLBlahM2mvcf4t2XvDaoxhF7BF8--yor8QwIRoT5juAw2k-6-8wKY9HiTaopAbJIbRCHEJnvUkvGBv5LQjeDHB__dGu0DSLqU9f0vNQhe1_iT63Zs5q6aUkzkI0qhW_MA1dIzcRNBNUiPWGDHq71wuOgHr9XYYfKHzaRg8OGOkLr6-xcLlO8sMDQj4n49UKfNQJOEhXPzGFOkdF0QxdSRgzQxUF6wsq9Zg9XonAC10PA1hJeFlLzMvRk8CI83NFqxYlc-pGvIIleyl3JIzkBlPl5YQMCTTq10syHc74aHn-yHG-UoC3VtTo_NMRNaa1KAGK0rK40V459Qqa8pSDotu1SbUKnCV0qMJAY_KvAirm833xQ7vVck7k447h8tyGINwRNTCaKqESrt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88480d9614.mp4?token=G8BX4WUbjsPT-ClJYvfCLEdkS9moahZLAl_6R8ALWKQcppgWkk5mEVGrK9mDlOWmO_TvQqnC6RCD8KhA0uoElcCvDgQW28BWjJfE_ilPz0p0KdvaoUrfkH9tdYB3JZwu8bPsxIdSKqvmHlnT6qU5EpYOiVJ53RfQpeRPgcQ6noUFGlKKuDAyfAWdCO-WBcC4SefEVKTwlcZemdJIAg6yY8Gotnzr1X7LzG30DWYNwBnKvOsHW13XH9P9PNVvq39zD6hxXPnh32-Xm3O6nVfyXq16Vjl7lRLBlahM2mvcf4t2XvDaoxhF7BF8--yor8QwIRoT5juAw2k-6-8wKY9HiTaopAbJIbRCHEJnvUkvGBv5LQjeDHB__dGu0DSLqU9f0vNQhe1_iT63Zs5q6aUkzkI0qhW_MA1dIzcRNBNUiPWGDHq71wuOgHr9XYYfKHzaRg8OGOkLr6-xcLlO8sMDQj4n49UKfNQJOEhXPzGFOkdF0QxdSRgzQxUF6wsq9Zg9XonAC10PA1hJeFlLzMvRk8CI83NFqxYlc-pGvIIleyl3JIzkBlPl5YQMCTTq10syHc74aHn-yHG-UoC3VtTo_NMRNaa1KAGK0rK40V459Qqa8pSDotu1SbUKnCV0qMJAY_KvAirm833xQ7vVck7k447h8tyGINwRNTCaKqESrt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیزر فصل جدید «حسینیه معلی» ویژه ماه محرم ۱۴۰۵ منتشر شد.
حاج سید مجید بنی‌فاطمه، حاج مهدی رسولی، حاج سیدرضا نریمانی، حجت‌الاسلام سیدحسین آقامیری و کربلایی امیر برومند در میز ذاکران این فصل حضور دارند.
🔹
نجم‌الدین شریعتی نیز همچون فصول گذشته اجرای برنامه را برعهده دارد.
📺
«حسینیه معلی» از دوشنبه ۲۵ خرداد از شبکه سه سیما روی آنتن می‌رود.</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/akhbarefori/658621" target="_blank">📅 01:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658620">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
فارس: ایران اجازه عبور نفتکش متخلف از تنگه هرمز را نداد
🔹
دقایقی قبل نیروهای ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه شده بود را ندادند.
🔹
گزارش‌های مردمی نیز از شنیده شدن صدای سه انفجار در فاصله حدود دو کیلومتری ساحل از سیریک حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/658620" target="_blank">📅 01:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658619">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
شنیده شدن دو صدای انفجار در شهر بندرعباس
🔹
دقایقی پیش، صدای دو انفجار در شهر بندرعباس توسط مردم و منابع محلی گزارش شده است.
🔹
منشا صدا هنوز مشخص نیست اما پیگیری برای کسب اطلاع دقیق ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/658619" target="_blank">📅 01:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658617">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88480d9614.mp4?token=gYCiJUh-ndBSCIQHho1uZqGilSrRIX5nb7UxnrAIGDnA4uiV7QFRIZygphTWOMHXcjZkot1BQJHDrHHFlagHJYdUflVuHk61AlMIAsZSVlNz5qW1P4srDNVqsl_gieSxIJPhOTHApmECEkqNsdI88DJEDxAF4nlevmONrXzyPwM2to_M-P24yEtSVpBz9rgbP0_gWx3wWv7ejwXDYFA76uRwXp7IocQviYhOE7QOQM8VE2uGLwaP16K6urtaiNXtZvxRzUU0vYlERsfSCG0_dFDlkHto-ako_ASImJJQlxGp2bJydag32U7B8I1ZkS1rdals03o2_WGu0Nhe7H4hmSAsmMmBXzvahIHh_obElxGB7-f0fZDw2TmaiNMnSAoAZz2LSz4Ghk4pyvvDNN6_4w0Q_MtIcPDORDtXG61NrmBDXiMyrrvGPQhzIlmjkzWf4fMEgGfRtG3t8EPrhnEhRCvyycyjtx03UPpwJDnJj7ujtCcH7ke7NUpJavgHASYK7anXTX4z7hO0CU2ce0b4cFthH63zY_Dux1pFiUNl8BZg1NGR1u-QYEbqouFld_GZ3NzugkIvBSN-VmbRbpvLxHmcxE178h-OZfXkt1Q9RwyOU1P-6YCkYWHaz4ZZ-9rIPAM1r80uUruRIPD9Z5el-7A5qNL5b-q9c4mYGNKvLjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88480d9614.mp4?token=gYCiJUh-ndBSCIQHho1uZqGilSrRIX5nb7UxnrAIGDnA4uiV7QFRIZygphTWOMHXcjZkot1BQJHDrHHFlagHJYdUflVuHk61AlMIAsZSVlNz5qW1P4srDNVqsl_gieSxIJPhOTHApmECEkqNsdI88DJEDxAF4nlevmONrXzyPwM2to_M-P24yEtSVpBz9rgbP0_gWx3wWv7ejwXDYFA76uRwXp7IocQviYhOE7QOQM8VE2uGLwaP16K6urtaiNXtZvxRzUU0vYlERsfSCG0_dFDlkHto-ako_ASImJJQlxGp2bJydag32U7B8I1ZkS1rdals03o2_WGu0Nhe7H4hmSAsmMmBXzvahIHh_obElxGB7-f0fZDw2TmaiNMnSAoAZz2LSz4Ghk4pyvvDNN6_4w0Q_MtIcPDORDtXG61NrmBDXiMyrrvGPQhzIlmjkzWf4fMEgGfRtG3t8EPrhnEhRCvyycyjtx03UPpwJDnJj7ujtCcH7ke7NUpJavgHASYK7anXTX4z7hO0CU2ce0b4cFthH63zY_Dux1pFiUNl8BZg1NGR1u-QYEbqouFld_GZ3NzugkIvBSN-VmbRbpvLxHmcxE178h-OZfXkt1Q9RwyOU1P-6YCkYWHaz4ZZ-9rIPAM1r80uUruRIPD9Z5el-7A5qNL5b-q9c4mYGNKvLjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیزر فصل جدید «حسینیه معلی» ویژه ماه محرم ۱۴۰۵ منتشر شد.
حاج سید مجید بنی‌فاطمه، حاج مهدی رسولی، حاج سیدرضا نریمانی، حجت‌الاسلام سیدحسین آقامیری و کربلایی امیر برومند در میز ذاکران این فصل حضور دارند.
🔹
نجم‌الدین شریعتی نیز همچون فصول گذشته اجرای برنامه را برعهده دارد.
📺
«حسینیه معلی» از دوشنبه ۲۵ خرداد از شبکه سه سیما روی آنتن می‌رود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/658617" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658615">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در نزدیکی ساحل سیریک؛ جزئیات همچنان مبهم
🔹
منابع محلی در استان هرمزگان از شنیده شدن صدای انفجاری در دریا، حدود دو کیلومتری ساحل سیریک، خبر می‌دهند. هنوز علت و منبع این صدا تأیید نشده است.
🔹
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/658615" target="_blank">📅 01:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658614">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از یک منبع: نتانیاهو هیچ اطلاع قبلی نداشت و وقتی ترامپ بیانیه اولیه خود را در مورد توافق با ایران صادر کرد، غافلگیر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/658614" target="_blank">📅 00:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658613">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای دفتر نتانیاهو: ترامپ با نخست وزیر در مورد یادداشت تفاهمی که با ایران در حال آماده سازی برای شروع مذاکرات است، صحبت کرد
🔹
اسرائیل طرف این یادداشت تفاهم نیست، اما نخست وزیر از تعهد رئیس جمهور ترامپ به اسرائیل قدردانی کرد.
🔹
ترامپ متعهد به حذف مواد غنی‌شده، برچیدن زیرساخت‌های غنی‌سازی، محدود کردن تولید موشک و پایان دادن به حمایت ایران از نیروهای نیابتی خود است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/658613" target="_blank">📅 00:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658612">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در نزدیکی ساحل سیریک؛ جزئیات همچنان مبهم
🔹
منابع محلی در استان هرمزگان از شنیده شدن صدای انفجاری در دریا، حدود دو کیلومتری ساحل سیریک، خبر می‌دهند. هنوز علت و منبع این صدا تأیید نشده است.
🔹
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد.
🔹
با این حال، این فرضیه تاکنون به طور رسمی تأیید نشده است/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/658612" target="_blank">📅 00:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658611">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ترامپ ادعای خارج کردن نفت از تنگه هرمز را تکرار کرد
دونالد ترامپ، بار دیگر مدعی شد که کشورش کشتی‌های زیاد و «صدها میلیون بشکه نفت» را از تنگه هرمز خارج کرده است.
🔹
ترامپ روز گذشته هم مدعی شده بود که ارتش آمریکا در عملیاتی مخفیانه دو میلیون بشکه نفت را از تنگه هرمز خارج کرده است؛ ادعایی که به گفته کارشناسان با آمارها و داده‌های منتشرشده در تناقض قرار دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/658611" target="_blank">📅 00:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658610">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvgK2Uz_KcD3I2X6QWo7xMdzRjKnjy6ked9CC8kooooSTwSNobejnF4AL8HQRI1KgDO6y9R9mgQjaHB7iXDKPcBef0IR4_nUo57H6iO79zHgT3DWU_iS71P_fe14ECOcgTVxnQI_k4MZF-AD6-VLBbl7USpw8QI_ye5is5l-E_k5cFAgLTUt_vOa556cs6fUJN-O03o_NQmzSY6UKnj52YLqfmJrsfWBGjvKFzUpU_7-DYtXHeTRHps0UDuqRNjB3Rdr6QsFQ64qDD8mitNjKx6bpaJw9Ao6ZqcsAwc9JoYWvFdIp-BNUBdNwTP7sEAX59Tc0RlMDh-SL1WPkHaTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد تماشاچیان حاضر در بازی افتتاحیه جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/658610" target="_blank">📅 00:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658609">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ابتدا باید مراجع ذی‌ربط نظام دربارهٔ جزءبه‌جزء هرگونه تفاهمی به جمع‌بندی برسند‌
🔹
به‌محض اینکه به جمع‌بندی نهایی برسیم رسماً اعلام می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/658609" target="_blank">📅 00:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658608">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: اعلام تاریخ برای امضای تفاهم، گمانه‌زنی رسانه‌ای است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/658608" target="_blank">📅 00:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658607">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: به‌دلیل اقدامات غیرقانونی آمریکا در تعرض به ایران، روند دیپلماتیک هم تحت تأثیر قرار گرفته است
🔹
میانجی‌ها فعال هستند و ما خیلی شفاف به آن‌ها [مواضع‌مان] اعلام کرده‌ایم‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658607" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658606">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: اگر قرار بود ایران تحت فشار و تهدید از مواضع اصولی خود کوتاه بیاید، یک‌سال قبل این کار را انجام می‌داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/658606" target="_blank">📅 00:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658605">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUuAOX1sQZ5-rAw5v27VMDIP9SAP5in9TLiX-ojwn8TdGEqjMJnBUiILLyN9PlrR0-YzkElsG1J3j3jUq3EP3SimDBoxurma8zlMIon-pTts70MuokEMlU9FzumXc2SDH7eXeJDBc3z_JE3CKTm-Td-vgASaJKXb5KBCH6dIJTM1mWyf7nJYtnogXEbfSJkQVMik9BkZaowGallE82zxw9WBvi7geJZzGc4KmO6Hoc2tTJPD8LLo7txTHrMnW5GeluEXq9yL5au0aJadnzHi_w8vGEEI9VbSR7duSOWwYGX3gOT5ACGxDIXFh7sEgF8PLTQFliI6EkbqO14cK3OKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز عادی نخواهید داشت. هر روزتان را تبدیل به کابوس میکنیم
לא יהו לכם יום רגיל. אנחנו נהפוך כל יום שלכם לסיוט.
#WillPayThePrice
#تقاص_خواهید_داد</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/658605" target="_blank">📅 00:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658604">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بقایی: وضعیت مذاکرات از نظر ما این بود که بخش عمده متن تقریباً نهایی شده بود اما آمریکایی‌ها زیاده‌خواهی می‌کردند و درخواست‌های جدیدی مطرح می‌کردند
🔹
آن‌ها در حال القا هستند که جمهوری اسلامی تحت فشار به توافق رضایت داده است، در حالی که ما به هیچ عنوان از…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/658604" target="_blank">📅 00:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658603">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c497468ed.mp4?token=Fzyi_i-20fm4s0ZrLTaSI50dOtgZ7-QatMV6qFNOviWcStG2zOwTkgBDnjQ1RmrrMwEL8LcXzBpcHNoloIvcCNudpk5s83gr64_VUwoj3VYirMscGRClchyZbAXwym7JsQFDMFioTGc2X5zU0Zm41CVTL291ok8GIX9iqIhca050yMUl1F5UFmpazXwDFIaiVxBxaZdrXL1VZz4DbRwv1jvC1ehx2PhK9vursmi_DwPyyyd338g-J2cCpuHvkGBYRz8amCBm6LpSJe4N1q59d8Y90fWjvLCWGZ8Dsq355NEGECr4E9DUDBVRjrPerdjXIRaLzzil-scUKhGWxcKyqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c497468ed.mp4?token=Fzyi_i-20fm4s0ZrLTaSI50dOtgZ7-QatMV6qFNOviWcStG2zOwTkgBDnjQ1RmrrMwEL8LcXzBpcHNoloIvcCNudpk5s83gr64_VUwoj3VYirMscGRClchyZbAXwym7JsQFDMFioTGc2X5zU0Zm41CVTL291ok8GIX9iqIhca050yMUl1F5UFmpazXwDFIaiVxBxaZdrXL1VZz4DbRwv1jvC1ehx2PhK9vursmi_DwPyyyd338g-J2cCpuHvkGBYRz8amCBm6LpSJe4N1q59d8Y90fWjvLCWGZ8Dsq355NEGECr4E9DUDBVRjrPerdjXIRaLzzil-scUKhGWxcKyqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم مکزیک روی ارسال دیدنی
خیمنز دقیقه ۶۷
🔹
مکزیک ۲ - ۰ آفریقای جنوبی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/658603" target="_blank">📅 00:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658602">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73ad01da8.mp4?token=jh-BXK11EySnUctJigVZypCoSWc1J9c_-IeEcbbLM7dm7D-eM3CWLn_qq0PyGgGPRKifcdduvTRFh6kYAR32oQ94sEcgW7fK2hIT2HX094bACiNH48ZU_asjukCeFVzxQ7Kp76suTFZlUV1L0gqf8TrzI6qp6Dtovj9OgKpQoaZLS2KHReVrUskmksoYTHeqogJx3HjwFTE6YkDm8fLRPptr6XgYZKxe5rFUc-GUWzxkyWQsx-phZx45R0gAFvXZmFk7Tvo_FIT9fFg6m52VYyrpuQj398wkyfsWQ_qyQQWG_3lZZ3Yj6qITjkCdv98iYHb-ZmYn-u8AQsz7xiAJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73ad01da8.mp4?token=jh-BXK11EySnUctJigVZypCoSWc1J9c_-IeEcbbLM7dm7D-eM3CWLn_qq0PyGgGPRKifcdduvTRFh6kYAR32oQ94sEcgW7fK2hIT2HX094bACiNH48ZU_asjukCeFVzxQ7Kp76suTFZlUV1L0gqf8TrzI6qp6Dtovj9OgKpQoaZLS2KHReVrUskmksoYTHeqogJx3HjwFTE6YkDm8fLRPptr6XgYZKxe5rFUc-GUWzxkyWQsx-phZx45R0gAFvXZmFk7Tvo_FIT9fFg6m52VYyrpuQj398wkyfsWQ_qyQQWG_3lZZ3Yj6qITjkCdv98iYHb-ZmYn-u8AQsz7xiAJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش فوری کاربران فضای مجازی به توییت ترامپ
🔹
دونالد ترامپ در توییتی ایران و آمریکا را مقابل هم قرار داد.
🔹
کاربران فضای مجازی هم این توییت را بی‌پاسخ نگذاشتند و با الهام گرفتن از کارتن معروف فوتبالیست‌ها و به بهانه شروع جام جهانی ۲۰۲۶ به رییس جمهور مغضوب آمریکا اینطور واکنش نشان دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/658602" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658601">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
🔹
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
🔹
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/658601" target="_blank">📅 00:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658600">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsTLDiCawPNC9tNot15od0nKr9b1KGsLPaNhMAwEnvptnA5sdsdvB9s3WKa-nOTWRbGFdUZHcbw7SwaOMN3UGG83hay73R5Q_87cFTIQlYS5jM6jIlwtqsYFAfzv3G9jxQPUmFSVFW93pwp9A_DPFvZyjU2ZTYZ3aF7-TlVFke_0ya_G1UuZTkI_QsAQYVwW4ratVAcO1WoPQQaY-sSR3fX6PSfoMP-M1rS77rWzF5d4OsEOdrwVIdYA2-k19tzUH5hrE4MVMcLdQlZxqF1Y8Fg1FUvnlEuQUsLR65Te_uGZzpNjdTLwSgX678FjaDosTUtJ6dAYZuBld-XOMhwp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/658600" target="_blank">📅 00:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658599">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
🔹
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
🔹
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی ندارد. مواردی که درباره توافق مطرح می‌شود گمانه‌زنی است و موضوعی نهایی نشده است/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/658599" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658598">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e6aafc5a.mp4?token=M5RPnTZFhNVMWrHrBCxtlgTnw4Lz9vB_RUVJi-ab7pc2-yya829tLGvMI5yeJpWiN6YEBBGv70CHlYPwXFDMY_HuKPraKxqIaaGMg7nhoFF8L-8YntKxRAewRbmInfXKNhxZBEOVSJxGLMb40KQW16qmjyQt3SASji7hKYm2e8MsFKrxyR7sGG2Z5ArCvs0vrZWfEyDgLRLTSkFNqEhQ0iWPvZ1OI78xj9GqeoDtdVmEtdL8H-te8JuB19j78S2xdazOQW3Psl151HPWCJJN1qOEt0EjhC1M7lBCLmJpAnHPFbewDKp6EPmT0LrRszGT7Abu6bF1ZBmZf6g4gpkeiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e6aafc5a.mp4?token=M5RPnTZFhNVMWrHrBCxtlgTnw4Lz9vB_RUVJi-ab7pc2-yya829tLGvMI5yeJpWiN6YEBBGv70CHlYPwXFDMY_HuKPraKxqIaaGMg7nhoFF8L-8YntKxRAewRbmInfXKNhxZBEOVSJxGLMb40KQW16qmjyQt3SASji7hKYm2e8MsFKrxyR7sGG2Z5ArCvs0vrZWfEyDgLRLTSkFNqEhQ0iWPvZ1OI78xj9GqeoDtdVmEtdL8H-te8JuB19j78S2xdazOQW3Psl151HPWCJJN1qOEt0EjhC1M7lBCLmJpAnHPFbewDKp6EPmT0LrRszGT7Abu6bF1ZBmZf6g4gpkeiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: مهلت شما برای رسیدن از این مرحله به یک توافق نهایی چیست؟
🔹
ترامپ: نمی‌خواهم مهلتی بگویم چون بعد می‌گویید من مهلت را رعایت نکردم. خیلی مهم نخواهد بود چون قرار است امضا شود.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/658598" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658597">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
عقب نشینی ترامپ و وعده امضای توافق با ایران پس از تهدیدهای تند
👇
khabarfoori.com/fa/tiny/news-3222314
🔹
مروری بر حملات آمریکا به ایران در شبانه روز گذشته؛ از جنوب تا تهران
👇
khabarfoori.com/fa/tiny/news-3222174
🔹
حمله سپاه به ۱۸ هدف مهم متعلق به ارتش آمریکا طی ۲ موج عملیاتی
👇
khabarfoori.com/fa/tiny/news-3222176
🔹
شلیک مستقیم طالبان به یک خانم تنها بخاطر شرکت در تجمعات اعتراضی حجاب و تحصیل/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3222289
🔹
آقای تاج بابت دیپورت شدن از کانادا هم دستاورد‌سازی می‌کند
👇
khabarfoori.com/fa/tiny/news-3222313
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/658597" target="_blank">📅 23:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658596">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای ترامپ: تعداد زیادی کشتی و صدها میلیون بشکه نفت را از تنگه هرمز خارج کردیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/658596" target="_blank">📅 23:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658595">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
گراهام، سناتور آمریکایی: هر توافق هسته‌ای با ایران باید به تصویب کنگره برسد
🔹
مانند گذشته، هرگونه توافقی که با ایران در رابطه با برنامه هسته‌ای آنها حاصل شود، برای بررسی و تصویب به کنگره ارائه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/658595" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658594">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای نورالدین الدغیر خبرنگار الجزیره در تهران: دیگر همه چیز قطعی و تمام شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/658594" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای ترامپ: تعداد زیادی کشتی و صدها میلیون بشکه نفت را از تنگه هرمز خارج کردیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/658593" target="_blank">📅 23:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
توهم جدید ترامپ: به ایرانی‌ها می‌ گوییم... ما از نظر نظامی در جنگ پیروز شدیم
!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/658592" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdc227ec7.mp4?token=ZbgBjEZO6DK0USlePwpNFx1X8Y0XRuNbaPeEeJ4HAgbpygCrm20lRkklL7O-3NcQ6QRWqweBpl7FnIkN6OF2Lgz-A-A2ObRBDdM8J8RVNJg1NL9FIGhhB2nYacyXSBDAxO62gZCLg9LYDWJk48uyTsIZfsw7rPjQeQdakVtBcCs32c3mXsuJuIVzlr6AEUTNe72Tc3SKIpjpDIrFYXBW45Lwm1pMNE3Sg6wrMjRYRVH0ZcDo_xLNcxCvFZ4kaofUD-G4AqK2tfPmh9IpZ9GqoNLDeAazQqYBAL9drZihmHhY8c2OLBD537j3QzSuKxOQigJQ09cNRY5KWDQ-OKyKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdc227ec7.mp4?token=ZbgBjEZO6DK0USlePwpNFx1X8Y0XRuNbaPeEeJ4HAgbpygCrm20lRkklL7O-3NcQ6QRWqweBpl7FnIkN6OF2Lgz-A-A2ObRBDdM8J8RVNJg1NL9FIGhhB2nYacyXSBDAxO62gZCLg9LYDWJk48uyTsIZfsw7rPjQeQdakVtBcCs32c3mXsuJuIVzlr6AEUTNe72Tc3SKIpjpDIrFYXBW45Lwm1pMNE3Sg6wrMjRYRVH0ZcDo_xLNcxCvFZ4kaofUD-G4AqK2tfPmh9IpZ9GqoNLDeAazQqYBAL9drZihmHhY8c2OLBD537j3QzSuKxOQigJQ09cNRY5KWDQ-OKyKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا رهبر معظم ایران این توافق را تأیید کرده است؟
🔹
ترامپ: تا جایی که می‌دانم پاسخ بله است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658591" target="_blank">📅 23:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f17a9b2ac.mp4?token=qB0sgBzs73JBv85yHX-2XmcaOrdu2WWk9FzktyxzZbj6RaZcNw4rexiiO51FXBhrUnJj6ZTL1J3EXS9-GeLrl8YclzfT1XRXvoARqAIcaD-KRDKHpP7x0JVOrfpwIBMKGfNTuwuoIi4ONky_iRKJQEcjdkA7GCQGHzUKD_1RyYeF3VnQ6RqpHiwFrijo28y5FF2NcjRCT9-rhRrHl3tuiMh_IWkwxXMPK5ep-ugW7C1uFnww04t9mH0IPAi7j-8drCXPD-P02Nlq8czOFMiGwY6XIC2HvLPoOptOxxWKqdt_CTSrwZxITsls8yMb78NAVW9skc7lz4cTgHyBQ0FtkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f17a9b2ac.mp4?token=qB0sgBzs73JBv85yHX-2XmcaOrdu2WWk9FzktyxzZbj6RaZcNw4rexiiO51FXBhrUnJj6ZTL1J3EXS9-GeLrl8YclzfT1XRXvoARqAIcaD-KRDKHpP7x0JVOrfpwIBMKGfNTuwuoIi4ONky_iRKJQEcjdkA7GCQGHzUKD_1RyYeF3VnQ6RqpHiwFrijo28y5FF2NcjRCT9-rhRrHl3tuiMh_IWkwxXMPK5ep-ugW7C1uFnww04t9mH0IPAi7j-8drCXPD-P02Nlq8czOFMiGwY6XIC2HvLPoOptOxxWKqdt_CTSrwZxITsls8yMb78NAVW9skc7lz4cTgHyBQ0FtkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: وقتی این توافق امضا شود، آیا آمریکا بلافاصله محاصره را برمی‌دارد؟
🔹
ترامپ: بله، این بخشی از توافق است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/658590" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff61170c7.mp4?token=XqFMR6VaSEbRNv4RG6Xx5CnL2bbpfELMWeK_NR64LYjGnyvzdvK3l16rkMDEFAfPQawjGV1DxEiflwPoWBxAeFMB_OMAxTAHjd3hMShY91UeIO_2aTusjCj_0aLev9oQl2HcLx543RfEM6EKJ08nN_6QZ4waZKCv-TlORMgX-HO7mgWATiUyYUSgmK1b6RfNbbFTyZHA4RfgXly27Bp5YrYziIi0zPZ6wxgg_dzW0lrqhuZq0n5LmHkRX25BHEYVWNAmb90-gFYpRQsIr-MOEaU4VT3bWmKeZQlCWvN8SSzcqF0HJSYHbYXOaoXatJzBZ5M_he7YkWtmWOjBQsqcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff61170c7.mp4?token=XqFMR6VaSEbRNv4RG6Xx5CnL2bbpfELMWeK_NR64LYjGnyvzdvK3l16rkMDEFAfPQawjGV1DxEiflwPoWBxAeFMB_OMAxTAHjd3hMShY91UeIO_2aTusjCj_0aLev9oQl2HcLx543RfEM6EKJ08nN_6QZ4waZKCv-TlORMgX-HO7mgWATiUyYUSgmK1b6RfNbbFTyZHA4RfgXly27Bp5YrYziIi0zPZ6wxgg_dzW0lrqhuZq0n5LmHkRX25BHEYVWNAmb90-gFYpRQsIr-MOEaU4VT3bWmKeZQlCWvN8SSzcqF0HJSYHbYXOaoXatJzBZ5M_he7YkWtmWOjBQsqcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رودی فولر، پویول، داوید سیلوا، ماتراتزی و کولینا از دیگر چهره‌های حاضر در جایگاه ویژه استادیوم آزتکا هستند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/658589" target="_blank">📅 23:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b10fe89a2.mp4?token=O2KaUdyr38ofub3raoehcBkL8HxinuNm6FEThzXDw8oB1-a0uzpr4HZZn2Fj_AJeBpWteBqw70UkNgRgLVgMJ6dD27Nw6UlK80OuLHYWwuM1i9aX8zCMBMqRxy50BGCxdhygTErNaHX_ez5ZcKR1YcxY9ULSKYVYGcZRlsCJlHePt7CCXIW4mPEghHlYgLlP_luW1_mBRVEINL0u-rQqK7UQk58TW73YI43afnbKdKaqo9x2wtf_G-nJ2NbgPWuTW3581exPqaZx9pivJ48atRrAh0004R5Rhsz49fdyEAGZztoC3Hp9twSmmjkgD3GexDTr0V-Uk5rv-gnnQjGmCQK98Cghbn4jHWpz9idWIhC4cIObzoLqVJdQgo7pLOskOhpqe137IA9weFjY8JQlmF6Fuv2xBmCyH4v7tUeamv_UFFTl7EAVDyfhUDFDZRqfIhMN_MaJ7OUzlXqJdWAVaFwarwCHZS-gO4Y2eVtcZsK7OBSyEYze65fAcScKGDQMonBQFNBtzYDI853GU7oA9KUiVuNdku3WENEWNN6wsdOgoCvG0Kx-bnvbkVx7l1FBR2ciEnYTeJZ11QUjLveRBOZoScw0uriGVfVbMttzx37T8KFsHBVndi2SrCJ2DK9YRY5qc1rRwPMuKYE2oG3eLo5NqB8ump_BLEjad7duMsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b10fe89a2.mp4?token=O2KaUdyr38ofub3raoehcBkL8HxinuNm6FEThzXDw8oB1-a0uzpr4HZZn2Fj_AJeBpWteBqw70UkNgRgLVgMJ6dD27Nw6UlK80OuLHYWwuM1i9aX8zCMBMqRxy50BGCxdhygTErNaHX_ez5ZcKR1YcxY9ULSKYVYGcZRlsCJlHePt7CCXIW4mPEghHlYgLlP_luW1_mBRVEINL0u-rQqK7UQk58TW73YI43afnbKdKaqo9x2wtf_G-nJ2NbgPWuTW3581exPqaZx9pivJ48atRrAh0004R5Rhsz49fdyEAGZztoC3Hp9twSmmjkgD3GexDTr0V-Uk5rv-gnnQjGmCQK98Cghbn4jHWpz9idWIhC4cIObzoLqVJdQgo7pLOskOhpqe137IA9weFjY8JQlmF6Fuv2xBmCyH4v7tUeamv_UFFTl7EAVDyfhUDFDZRqfIhMN_MaJ7OUzlXqJdWAVaFwarwCHZS-gO4Y2eVtcZsK7OBSyEYze65fAcScKGDQMonBQFNBtzYDI853GU7oA9KUiVuNdku3WENEWNN6wsdOgoCvG0Kx-bnvbkVx7l1FBR2ciEnYTeJZ11QUjLveRBOZoScw0uriGVfVbMttzx37T8KFsHBVndi2SrCJ2DK9YRY5qc1rRwPMuKYE2oG3eLo5NqB8ump_BLEjad7duMsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقایان مسئول نترسید!! / با صلابت در ادبیات سیاسی کلید واژه انتقام و خونخواهی استفاده کنید
🔹
بیانیه بدید که این جنگ ادامه پیدا خواهد کرد تا وجود تمام فرماندهانی که دستور ترور رهبری را دادند از دنیا پاکسازی بشه
🔹
ما امام از دست ندادیم که دلار بگیریم!
آمریکا با لگد ما باید از خاورمیانه بیرون برود تا آرمان رهبر شهید محقق شود.
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/658588" target="_blank">📅 23:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سریال استعفای وزرای انگلیسی ادامه دارد
🔹
پس از وزیر دفاع، وزیر نیروهای مسلح انگلیس ال کارنز نیز از سِمت خود استعفا داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/658587" target="_blank">📅 23:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPWM-sW2lY0zpDNF9BYn6poDMDirEFRd3vN1IfZodk7Jgs-Bu51-Db07GoxP9m4ICWoQejFhUMBhwWktaym-QPGbn3Nxcbort84QoNnOGWPTaaWgRJZW5isAHUfoMVvntScFAxvt8ea08dtHMLoG1AJ7GEzISlxM5QaBJ7p7e0LCPWp-hISmqjaNnSsBhPc18fFPwadjGCMRF3_rJBqn0CER3QntBdnfHx00dG1TZO5u-rOlDz2MooY47zbAah8lvNyOwC7FYEUQ91VZgHwYz90LdGnETXUOdVX2sD2jJ6aDBlfPrt5JoBK2oEc_c1mrvUXcbfV9lT_ELiGrxwbmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری عجیب از وضعیت دست دونالد ترامپ در جلسه دفتر بیضی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/658586" target="_blank">📅 23:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658584">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مراسم وداع و تشییع رهبر شهید انقلاب پس از دهه اول محرم برگزار می‌شود    ستاد بزرگداشت عروج رهبر شهید انقلاب:
🔹
زمان و جزئیات منتشرشده درباره مراسم وداع، تشییع و تدفین رهبر شهید انقلاب و شهدای خانواده ایشان در فضای رسانه‌ای معتبر نیست.
🔹
با توجه به ایام…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658584" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658583">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم: ترامپ و نتانیاهو تلفنی گفتگو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/658583" target="_blank">📅 23:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شبکه الحدث: توافق برای تمدید آتش‌بس به مدت ۶۰ روز، بازگشایی تنگه هرمز و پایان عملیات نظامی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/658582" target="_blank">📅 23:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
‌
ادعای ترامپ: توافق به زودی امضا می‌شود، شاید در این تعطیلات (شنبه و یکشنبه)
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/658581" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf783a3f29.mp4?token=Xbf-NwnlPFc6drmnWiiiqMw-WZbyH6eUsfsfvKD2WXURWrADyXK24CV73kjrXoEkZqIkXG7iMBgJoUfpFyIXEdd4dfuUfNlnzhDX9MKOIZKmsOT4e67R0WlEBKmV-FmeJNMtkDcKcTXfSbgR171UyQlmDoxvarWjUixCkVTEin3LopQm5B2rPDuGFHBZy-xGmTQi9ldg95SxRKUNAh6IzOaZ3JzyG6dZcxKqPVpidS5-U4EUXLS-IyynKcOGbM3HxUc19wprln9tbnCpSt_Cu4mqpxVnaF0EcHcYOcSWXRaQbJ7ali9hgLhqqbF_0NTy3Pm_0OlSKcbkykg70wYDlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf783a3f29.mp4?token=Xbf-NwnlPFc6drmnWiiiqMw-WZbyH6eUsfsfvKD2WXURWrADyXK24CV73kjrXoEkZqIkXG7iMBgJoUfpFyIXEdd4dfuUfNlnzhDX9MKOIZKmsOT4e67R0WlEBKmV-FmeJNMtkDcKcTXfSbgR171UyQlmDoxvarWjUixCkVTEin3LopQm5B2rPDuGFHBZy-xGmTQi9ldg95SxRKUNAh6IzOaZ3JzyG6dZcxKqPVpidS5-U4EUXLS-IyynKcOGbM3HxUc19wprln9tbnCpSt_Cu4mqpxVnaF0EcHcYOcSWXRaQbJ7ali9hgLhqqbF_0NTy3Pm_0OlSKcbkykg70wYDlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزخرفات
ترامپ درباره ایران: ما در برخی شب‌ها ۲۵ کشتی، در برخی شب‌ها ۱۵ کشتی را هدف قرار دادیم. در ۴ یا ۵ شب گذشته، به ترتیب ۲۵، ۲۲، ۲۱، ۲۶، ۱۸ و ۱۴ کشتی را زدیم
🔹
چه کسی دیگر این اعداد را به یاد خواهد داشت؟ هیچ‌کس.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/658580" target="_blank">📅 23:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658579">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2bd57c2ed.mp4?token=SuBwQxTellaqpECNj_nw8MTyBVh36d7aIUNGZwAsEQYKxK91PE9lTdRkNxLbz01E7rRU2TCehC6gj_TWuarUv-Grl-9J7EwhOaNtpzorK90Y6gjlSc3ogdHrYAOlByAvTq_R5_IfYZhE1mxaUAmmkSOHK-tv6_a_wdM4hcpRuJLLmHVgH_nx5q8GnPxSAvhy20d4dyeWT2m9IFZS8ybSPvV7R3iz9aNl2uhxRixbyCc67hKptfGo2oCqiwwSOoRNcAxWl8g4ciRc6lT7vEVucfLJkituxG5O86KJDhx28ZRY-7w2lOuH0ri3_m0OF3IkjEmILTBMggHBBHNc2ZSpGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2bd57c2ed.mp4?token=SuBwQxTellaqpECNj_nw8MTyBVh36d7aIUNGZwAsEQYKxK91PE9lTdRkNxLbz01E7rRU2TCehC6gj_TWuarUv-Grl-9J7EwhOaNtpzorK90Y6gjlSc3ogdHrYAOlByAvTq_R5_IfYZhE1mxaUAmmkSOHK-tv6_a_wdM4hcpRuJLLmHVgH_nx5q8GnPxSAvhy20d4dyeWT2m9IFZS8ybSPvV7R3iz9aNl2uhxRixbyCc67hKptfGo2oCqiwwSOoRNcAxWl8g4ciRc6lT7vEVucfLJkituxG5O86KJDhx28ZRY-7w2lOuH0ri3_m0OF3IkjEmILTBMggHBBHNc2ZSpGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: به‌زودی توافقی (با ایران) امضا خواهد شد و اسناد آن تقریبا نهایی شده‌اند/ انتظار دارم این روند خیلی سریع به سرانجام برسد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/658579" target="_blank">📅 23:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658578">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
منابع شبکه العربیه: طبق توافق، آمریکا تحریم‌ها علیه ایران را کاهش می‌دهد و محاصره را برمی‌دارد
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/658578" target="_blank">📅 23:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای ترامپ: تنگه هرمز به محض امضای توافق به صورت رسمی باز خواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/658577" target="_blank">📅 23:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658576">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای ترامپ درباره توافق با ایران: همه بسیار خوشحال هستند. کل خاورمیانه خوشحال است. و فراتر از خاورمیانه نیز همین‌طور #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658576" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658575">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ترامپ کودک‌کش: من قادر به حضور در مراسم امضای توافق‌نامه نخواهم بود، اما معاونم جی‌دی ونس در اروپا حضور خواهد داشت #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658575" target="_blank">📅 23:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658574">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
فوری| ترامپ: توافق بزودی در اروپا امضا می‌شود #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/658574" target="_blank">📅 23:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658573">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvObDIOqkaImIKpXELjoU0_ALr4-8hk30tySFKO_C2dmkcVaqBLXlRsZZZY8bkgYTcrFO6UoWR98dvx5W95tAO9D0mAHmm8Kb1xTcyCtQWGNp1Wfr6Qcx-QodbH2EvWUKaEvheiDIx-EUHr9KB4t-5v6BDaG7-zx0qlCMD8CKi-ux7qNb9eDDoUqNGBhIADiGC9vwVqWH32eGqK0lWzXYNiOiRP3QM3Y3JoJdJ36dQA5nRpr-F2mej-c7AB8lFmo24o6m9WTlsluQjfd21iVHTdAOIDxCnL1OlARMTzZvTOehCY9YWufDjhrie6QQOsWbnQNRCYTUO2v4fr3qyKVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت معنادار سخنگوی وزارت خارجه
:
از شبیخون حوادث لشکرش در هم شکست
هر که صائب در مقام صلح طبل جنگ زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/658573" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658572">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
فوری| ترامپ: توافق بزودی در اروپا امضا می‌شود
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658572" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658571">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
روایت ترامپ از «پذیرش ایران» در برابر واقعیت میدانی
🔹
همزمان با عقب‌نشینی تاکتیکی آمریکا از اضافه‌بندهای جدید به پیش‌نویس توافق، دونالد ترامپ با افزایش لحن تهدیدآمیز در شبکه‌های اجتماعی، تلاش می‌کند روایت «تسلیم ایران در برابر بمباران» را بسازد؛ روایتی که با واقعیت میدانی مذاکرات فاصله دارد.
🔹
حدود دو هفته پیش متن پیش‌نویس تفاهم‌نامه میان تیم‌های مذاکره‌کننده تقریباً نهایی شده بود و تنها منتظر تأیید نهایی در تهران و واشنگتن بود. اما در خلال این بررسی، ترامپ بار دیگر برخلاف توافق مذاکره‌کنندگان آمریکایی که پیش‌نویس ایران را پذیرفته بودند، خواستار اضافه شدن چند جزئیات جدید شد. در واکنش، ایران اعلام کرد که آن متن جدید را بررسی نمی‌کند و عملاً پاسخ آمریکا را نداد.
🔹
پس از آن، تنش‌های پراکنده در تنگه هرمز و جنوب ایران و همچنین حمله به ضاحیه عملاً پرونده مذاکره را مسکوت گذاشت. اما از روز چهارشنبه، تیم قطری با میانجی‌گری وارد میدان شد و خبر از عقب‌نشینی آمریکا از همان اضافه‌ بندهای جدید داد؛ یعنی بازگشت به همان متن اولیه‌ای که هنوز منتظر تأیید نهایی در ایران بود.
🔹
همزمان با این عقب‌نشینی محسوس آمریکا، ترامپ با راه‌اندازی عملیات رسانه‌ای و ادبیات تهدیدی کوشید القا کند ایران زیر فشار بمباران عقب‌نشینی کرده است. اما واقعیت آن است که تا این لحظه، نه تنها ایران پاسخ نهایی نداده، بلکه این آمریکا بوده که به خواسته قبلی خود بازگشته است. البته بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال بررسی مجدد این متن وجود دارد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658571" target="_blank">📅 23:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658570">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APSCKho6Jf3tMgwcsUA5UM2lSFYGcz0_ma2d-aKB4HGtR8a_5MiQS9rw1jRCNo-_2f06e0JcaQ106FXs1X591ct0k2hpjOaplvaTiOfwA4q46lLnPZ0MB91DOxM57Zf9djq8a6db3WLi6Hl6-pN2OiIXhlcXUgG_eR41Mza33ayB0xb65DXNXGV2uJttiAgtPyTcNV7gSQY8_p2uaKmt5S7SmsgZ019ZP80xqX_lEeKcKcXrusgrP1sRHWn2utBqn97k8kNeXMK0SIb--pAqQ-xY7-sGxVjEvrtfQi6d0OWrTlP9hCTsHlSZylISSFlY5RFGf2GBpue9xKQpy-UVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روغن طی یکسال به طور تقریبی ۳۰۰ درصد رشد داشته است!
/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/658570" target="_blank">📅 22:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658569">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYPXKkRvZSXdzMvg8ooPZBL32-sdnwFhURjBRmrvV0zXqfFEIoffcBopvGoQdYuSGPqWfLFMgXvX8DUIRM7oG_zB9pkLQFugsSR4Oan6Up28rfk6Yrt3iwkCKkWkbse5bPcpor2cUhU6ZFXvhKr_Q8VDm95zPDzFcuUcUyDwZvchdRCJ1SlPFuVg9wN62N66H4bzPXN54qaGrdDpk78st-3QuQhM8SJ04mlF_N27WqK4zUJS3rxM8LZtkOYAq85kW2fDfMja7jBCDEP6dXsiJ4g6H6WLCI3uy2YekVsN7-kkhDnvIGYUIGJyHerwov4qamjf7VO27SxHTx1BJTiS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهدی مهدوی‌کیا، میهمان مراسم افتتاحیه جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/658569" target="_blank">📅 22:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658568">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8484037c82.mp4?token=YCJ7tRQmkXAfB4vOwESjdbZkFyNfyqld4y4rl4IZ_N1wx4wxCpblB54Z4JJHaMLL1_mjEtPKDLYONerRhOrNXVckMVnMDht1Byxsg_hIgk0RrhryqbRd_p1pV_1KKlF4WmnLrWoFnALb7gt1R_whSG30opvXn4TinCzTR7W5a1ePk6THgXj1WYDFO2YxOMeozAd6Pj4cSlCewgnxES9sVIFcn0Q3BRX6Tq-Dopy98QWYFT1_Hx2H6TktN-qcvgU6kSoSS2W66AI6avMuEkPNgF-VRMEw0x0rJ2TSo3wTr8tpX8zpohJSW7HkSV-HkkSGplcmdURahkq7SnVqG_3iyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8484037c82.mp4?token=YCJ7tRQmkXAfB4vOwESjdbZkFyNfyqld4y4rl4IZ_N1wx4wxCpblB54Z4JJHaMLL1_mjEtPKDLYONerRhOrNXVckMVnMDht1Byxsg_hIgk0RrhryqbRd_p1pV_1KKlF4WmnLrWoFnALb7gt1R_whSG30opvXn4TinCzTR7W5a1ePk6THgXj1WYDFO2YxOMeozAd6Pj4cSlCewgnxES9sVIFcn0Q3BRX6Tq-Dopy98QWYFT1_Hx2H6TktN-qcvgU6kSoSS2W66AI6avMuEkPNgF-VRMEw0x0rJ2TSo3wTr8tpX8zpohJSW7HkSV-HkkSGplcmdURahkq7SnVqG_3iyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین گل جام جهانی ۲۰۲۶ به ثمر رسید
🔹
مکزیک ۱ - ۰ آفریقای جنوبی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/658568" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ec7ef88a.mp4?token=B_ocDs2FeJR6gyHRAZYTL4L_ITsaoTVCBIZ0Ecxr18qSNAt-Igt_25Ql82rYnwMpjevYANY_sHjewl1NuGCTHXMmWwtyjw_ZXIB0fWHVHn0UWR_YSIkaWCDIImaIfFoSi_AlkIWUNXXVUd2hDPMD7j3S7NeYi3P3XaY4NMacpUtmffXdQe8_qM0hP_CcEv7AkrHuPFsIcj8-NZvQylBBKqEcAUuTjl8xt9mJbaUkeotuleiEDg8JmJ_-XELlLnu3L78qG1IhYLEkM0YaQMgEGTI6xLLCr7YYsTWQsdWXvuO0uX_lcv6k8qkA6HMm8r6NemgN-LpTLka2vcjo1rJZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ec7ef88a.mp4?token=B_ocDs2FeJR6gyHRAZYTL4L_ITsaoTVCBIZ0Ecxr18qSNAt-Igt_25Ql82rYnwMpjevYANY_sHjewl1NuGCTHXMmWwtyjw_ZXIB0fWHVHn0UWR_YSIkaWCDIImaIfFoSi_AlkIWUNXXVUd2hDPMD7j3S7NeYi3P3XaY4NMacpUtmffXdQe8_qM0hP_CcEv7AkrHuPFsIcj8-NZvQylBBKqEcAUuTjl8xt9mJbaUkeotuleiEDg8JmJ_-XELlLnu3L78qG1IhYLEkM0YaQMgEGTI6xLLCr7YYsTWQsdWXvuO0uX_lcv6k8qkA6HMm8r6NemgN-LpTLka2vcjo1rJZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقدام جدید در جام جهانی ۲۰۲۶؛ بازیکنان ذخیره هم در مراسم پیش از شروع بازی شرکت می‌کنند و سرود می‌خوانند
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658567" target="_blank">📅 22:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf7c74853.mp4?token=k57gG8nkJVWhdmmbM7mkLBXcLi-rbTrCCX79-FDyWUk1gNTm7JFjEadmOFjXquNDG7QTIJi9VrM37VbHvkO2WL2oH8lexQxWHBHfQi7FhJF82dQT44L0MZ6-Qvp6P8_sw7M3ePqPSfX-7txAkwrgVtmW2gUA1JmudhpvEv7imZwpRDQXZu2NahqG1ivdWAxSpb-PR8EBjVsAVqcWPaob4g_i0eSUWEoawE5gBE1e3RizG1XN2KQcD8Olz3qgZchQrk-ax-I1zvvaRzZr4GNKKIkfT-p4T04SmRLICNjJj-xWobJ48wTGwHN_zD6kBlDMy8s4jDAYQU9YoFLerEX0vFhZrIvhwwqqvYHPRdHNcIXJ_RU5E9j07L-Dg6FHGR1xP0VHF0KofIbocwWMP9Q8tMCjfR3u1dFM5jrJnfz-k_x381dpdoz-NCTpxTluXZ0MVN_LrTGMdrUlVfrS_Udp0yTMOsyos_UR5GbNr94AAyDaELYROGS1lUBTOajkBg4hlyDWS8WbgLon0R7tu0ACRwWxS1_ej2-c6BLw42SKZdR2fDHqQm0JD9fJdeYHDUcUK8MHVnKfNE807CgcPxPBEJHbNPl6HgAq7uH4AWRK_uaDZzYTHt7OhMIhbhnBsXAJig6rAGT5KIQBvNFni44gmS-zRZmGfSNgru6GZSGtCMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf7c74853.mp4?token=k57gG8nkJVWhdmmbM7mkLBXcLi-rbTrCCX79-FDyWUk1gNTm7JFjEadmOFjXquNDG7QTIJi9VrM37VbHvkO2WL2oH8lexQxWHBHfQi7FhJF82dQT44L0MZ6-Qvp6P8_sw7M3ePqPSfX-7txAkwrgVtmW2gUA1JmudhpvEv7imZwpRDQXZu2NahqG1ivdWAxSpb-PR8EBjVsAVqcWPaob4g_i0eSUWEoawE5gBE1e3RizG1XN2KQcD8Olz3qgZchQrk-ax-I1zvvaRzZr4GNKKIkfT-p4T04SmRLICNjJj-xWobJ48wTGwHN_zD6kBlDMy8s4jDAYQU9YoFLerEX0vFhZrIvhwwqqvYHPRdHNcIXJ_RU5E9j07L-Dg6FHGR1xP0VHF0KofIbocwWMP9Q8tMCjfR3u1dFM5jrJnfz-k_x381dpdoz-NCTpxTluXZ0MVN_LrTGMdrUlVfrS_Udp0yTMOsyos_UR5GbNr94AAyDaELYROGS1lUBTOajkBg4hlyDWS8WbgLon0R7tu0ACRwWxS1_ej2-c6BLw42SKZdR2fDHqQm0JD9fJdeYHDUcUK8MHVnKfNE807CgcPxPBEJHbNPl6HgAq7uH4AWRK_uaDZzYTHt7OhMIhbhnBsXAJig6rAGT5KIQBvNFni44gmS-zRZmGfSNgru6GZSGtCMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرگزاری شهر | اهدای گل به خانواده‌هایی که از هتل‌، به خانه‌های خود بازگشتند
🔹
نمایندگان شهرداری تهران با حضور در منازل بازسازی‌شده شهروندان جنگ‌زده که پس از مدتی اسکان در هتل به منازل خود بازگشتند، با اهدای گل از آنها دلجویی کرده و جویای احوال آنها شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/658566" target="_blank">📅 22:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
خشم پرنده‌های ما این‌بار برای پیروزی در یک رقابت ساده نبود؛ ما به یاد و به نام کودکان معصوم و پاک
#میناب
پرواز کردیم و بردیم
This time, our birds’ rage wasn't just for winning a simple game; we took flight and conquered in memory of the innocent and pure children of
#Minab
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/658564" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
عصبانیت وزیر جنگ آمریکا از مقاومت ایرانی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/658563" target="_blank">📅 22:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: قطر نقشی تعیین کننده در نهایی شدن توافق داشت
ادعای سی‌ان‌ان:
🔹
به گفته یک منبع آگاه، مقامات آمریکایی معتقدند که جلسات این هفته بین مقامات ایرانی و قطری در تهران به حل برخی از نکات مورد اختلاف باقی مانده در توافق با آمریکا کمک کرده است.
🔹
نکات مورد اختلاف شامل جزئیات چگونگی پیشبرد مذاکرات آینده بر سر برنامه هسته‌ای ایران و ترتیب اعطای کمک‌های مالی به ایران بود. به گفته یک منبع آگاه، ایران آخرین پیش‌نویس توافق پیشنهادی با ایالات متحده را از طریق میانجیگران قطری ارائه کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/658562" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بیکاری ۲ میلیون ایرانی بر اثر جنگ
گلپور، رئیس کانون انجمن‌های صنفی کارگران:
🔹
آمار واقعی بیکاران بسیار بیشتر از ثبت‌نام‌کنندگان بیمه بیکاری است. به گفته او، با وجود ثبت‌نام ۲۹۰ هزار نفر، برآوردها از نابودی بیش از یک میلیون شغل و بیکاری مستقیم و غیرمستقیم حدود ۲ میلیون نفر حکایت دارد. همچنین تا خرداد ۱۴۰۵ فقط برای ۶۶ هزار نفر بیمه بیکاری برقرار شده است./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/658561" target="_blank">📅 22:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua5y8yvNhEYn2XW31vXSkl1BKy_dMwCBRc4VJYFRgbFYe1nypbM_QXHJ5oSsvmYe62KxNXXzO743ORVJVdO1ps5wZlbg_OtB693mCob21bUYOK_NXcbCdVQOXRpPx2wpSV8rdR0tLrmFkisIutaCVdH300_FBaJuCRHSRVefo5E7IR_NgvAX7xs8OZv2VIc6ZC-I97cVs0pcPxjAzFPvn9aSo0dsEStaJlGVdNddJDi6ctice800ogQcHJlPr4I1B1WNCm-F3afIQG1Epyo6cacW3f55HFLpzdU69mk84A_p-9IlhfqM6iBg0x_QSu-2A5rwEu-BsEqz2W2QqHn5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Danger doesn’t always come from the front; it comes from where you least expect it.
خطر همیشه از روبه‌رو نمی‌آید؛ از جایی می‌آید که هرگز انتظارش را نداری.
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/658560" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e986ed42f.mp4?token=OKl5AsOZtTLDuhkgVXYm_VIyXPzkVBUZGdGFe8tjOo7x9QcEHz29GDWbcVnfmLfgHflMYF4Jg6HvpvNuqt0Giv1DrmAUVZ5NdHXsz5yaXmZ-u-xZh-TtTQ9qI232xiXZRHHyCvPkl33LvOHDVFmO7BnpT9u4wxOfgfTy5ugrovGFtqhaaCrQjzhoABVG4LMpOr9wcIQ4p8NaTpJ4beRBYnBC-mSMQA1rcDsa0x83ECWyNZS9zfi-12tJlU9AjaFkAtsbzmNsNNxXWbLpTb0MDJlQoZPZjkc3_J2aPjnv3Y9qAEUtZMybsAjsz66uxAuzGquFVK2fHpdmNOcv4YTRPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e986ed42f.mp4?token=OKl5AsOZtTLDuhkgVXYm_VIyXPzkVBUZGdGFe8tjOo7x9QcEHz29GDWbcVnfmLfgHflMYF4Jg6HvpvNuqt0Giv1DrmAUVZ5NdHXsz5yaXmZ-u-xZh-TtTQ9qI232xiXZRHHyCvPkl33LvOHDVFmO7BnpT9u4wxOfgfTy5ugrovGFtqhaaCrQjzhoABVG4LMpOr9wcIQ4p8NaTpJ4beRBYnBC-mSMQA1rcDsa0x83ECWyNZS9zfi-12tJlU9AjaFkAtsbzmNsNNxXWbLpTb0MDJlQoZPZjkc3_J2aPjnv3Y9qAEUtZMybsAjsz66uxAuzGquFVK2fHpdmNOcv4YTRPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جام جهانیه
⚽
اونایی که فوتبال دوست دارن منتظر بازی هستن،
اونایی که دوست ندارن، منتظر سوت پایان!!!
⚡️
تا اون موقع هم، کولر روی ۲۵ درجه
«۲۵ درجه؛ قرار همدلی ماست»
#صنعت_برق_عرصه_تلاش_و_خدمت
#برق_خدمتی_مستمر
#شرکت_توزیع_نیروی_برق_استان_تهران
#پویش_۲۵درجه_قرار_همدلی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/658559" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf9e93ae7.mp4?token=dsD2JABBvle1rOzUFD5jIZtqpQlzSEwH0aaD08hYlj6OqKjPntLKwDsQs6dZWaiKf1WJXqZzGJVV--DwQcORHCana-RXT48FQdFzmFhOqjBhHAtsebwiUxVJkpgO62A458SpngYcmJjl0wjY2HXy5V0OkR559fwQ7ud3a684CbHwNpJnZ6YMNHMLLcLlQXTRwFnK2KdADBqsTuMRh40gNaGIzficjRqFTL9Lsf07obFAifQo-SUomp3KHiLksz_YuyKCO1ilHDlMSDcm-9FegAyZnU2bzds-_wezFrLU1p_52B8IvcTmaW_DNVH9wuvwLLVnrHfM8aCbcGh9EU-SXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf9e93ae7.mp4?token=dsD2JABBvle1rOzUFD5jIZtqpQlzSEwH0aaD08hYlj6OqKjPntLKwDsQs6dZWaiKf1WJXqZzGJVV--DwQcORHCana-RXT48FQdFzmFhOqjBhHAtsebwiUxVJkpgO62A458SpngYcmJjl0wjY2HXy5V0OkR559fwQ7ud3a684CbHwNpJnZ6YMNHMLLcLlQXTRwFnK2KdADBqsTuMRh40gNaGIzficjRqFTL9Lsf07obFAifQo-SUomp3KHiLksz_YuyKCO1ilHDlMSDcm-9FegAyZnU2bzds-_wezFrLU1p_52B8IvcTmaW_DNVH9wuvwLLVnrHfM8aCbcGh9EU-SXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از پرچم ایران در مراسم افتتاحیه جام جهانی ۲۰۲۶ در استادیوم آزتکا
🔹
طرح
طلای
بیمه زندگی
پارسیان
▪️
آینده‌ای طلایی با سود طلایی
▪️
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/658558" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb76d0e87.mp4?token=CBQyYnwlrPJ44qLhN_hA6raPotCT7LfzIwwgEF3nuTV7TiSFZU1MO3hmlHpoVNLwsMSQx7lEPHEFxm75_xzJIDgvcJax21RTRzwONzLrdoTZc20sPT_itpWS1kvk1tnjEbSyuA9GT_4lVa3J8Ne95WgFu5xEYAaMIs0bSbV_Rz7hAWVYe-INv2vZUu3r60OvT7jdkUlxO8ipY_aDozqpg2OR0wvKT4Xn8b98qjoxvmooWsksOkTHke_OREIPII7FoOdKPeI_qRVzOzglRx_HzVxyprToCadYkBuH_iC0Rpfb4B0iwXME7OMMSl-Z8KMpV6oHP4wmfZxGm-Zwoix5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb76d0e87.mp4?token=CBQyYnwlrPJ44qLhN_hA6raPotCT7LfzIwwgEF3nuTV7TiSFZU1MO3hmlHpoVNLwsMSQx7lEPHEFxm75_xzJIDgvcJax21RTRzwONzLrdoTZc20sPT_itpWS1kvk1tnjEbSyuA9GT_4lVa3J8Ne95WgFu5xEYAaMIs0bSbV_Rz7hAWVYe-INv2vZUu3r60OvT7jdkUlxO8ipY_aDozqpg2OR0wvKT4Xn8b98qjoxvmooWsksOkTHke_OREIPII7FoOdKPeI_qRVzOzglRx_HzVxyprToCadYkBuH_iC0Rpfb4B0iwXME7OMMSl-Z8KMpV6oHP4wmfZxGm-Zwoix5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای بیرونی و فوق العاده زیبای استادیوم مرسدس بنز توی شهر آتلانتای آمریکا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/658557" target="_blank">📅 22:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
تسنیم: تا زمانی که موضوع تفاهم احتمالی، از سوی ایران اعلام نشود، هرگونه اخبار ترامپ در این زمینه را باید به حساب پیامهای قبلی او گذاشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/658556" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658554">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
فارس: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
🔹
هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تایید نشده است؛ این را یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران  گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/658554" target="_blank">📅 22:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eheEAyXKWl3_lD35AyGzIrtE6VGpLo64OtgFCcobla7XhDe0NxQK8xb7OX2UBAoRcoDWlJY_AnyWMjR6KBnlKo8UwDZQCfuyutr-b5pFa4Vsy2N0__RjOiCXwH0xyQSK9DAbk0_gaol93VN2GOWhNcJCAykuQ02LtKxinkkbgGFO3oUB9LK9J_M8UA4EqPoGz_gG67A1vPXyk7OmvVdpB3P8RfyvEAWZaeZwWCAPvveVgeVMANyKWcaITXiltX-2_FddEH7dMMILJFK_qruQEmV2igIeLa4WYh2RvOX7QZVy9Bfwgdr0R9CjkdDAqhSRldHbswk4nkf0FML2WzOUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pf_1KECv4MufljAN92TJlUKie6vuKwf8krjYlkTxiDJTqTfG-2WG-M59CUbkTWmelGsfw-ETHfhHIePHg32og-XEsrCpL69Cu8Mmd-IbZFZy9eVhaoNYq3vxvx_7SYFwtkMzGGY9zoBp4aGgGWbGqF1anE6avKh5DM3A5LYF3Xh_PLO-_UFUwe-FVxOXmDFrcrgGW9u0zHpEiNm0fNezgTOunR2R86i5h8KNUvjSlpjfsoq1uu_Jzy68ZlsXzhKX5VJAKfBi7ZypSMKVg3mHoS8eoqCaycn8uZ4HR0MLQhmAbv31BM6pnkYxUsDhiLW4rsGQ9omAtHMKSVE24HqBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Imeo1Gp4jt2XtqzukdHg4pDyufsV1kTGuwz-TlLUf-YureA9yEzCaBqlwEUoiG7eEGU-YK0d_cUCTVhV3Rxr_46S3BSkv6xy_p8a4LAxXXrFU98N1GXTg7fWKetFl2qAdMjOzePBFUxjKp3mgE4dgWa7WW4lKTPjgrtt0T_ZH8livrkYckyjt_K7ESr2P8KpTjXpLrZhgC0xGlwqpbGuPTrHaTYGbazGz69Jgy96ImXd9NiBbZLaTSETcjST_RqzfmgREZGnWXISVzkZOhPKdwJ_oTslP1ZHdUfMDeKXLcv1HC65SczRwXN8Fa7VXLzL2aA84POwDPARfMgyaRDa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTsEm511po6mCc3GRRZHKoT0FCv9H_pAwxDCWuB_WpUoXdVnNsiDUR0OWnRjtHX0Agsc7qA0sRhbWr1PXHLxQVOsERKcMSvh5CubbLr7LfZGRMcjvlKjQXoBhKx2IfGglqrIqJ-dofgNUyH6jnhixjlH5Q3B1aqxuyykc9DVPI-HiIVgfc4Hr1E5--5_UtanX6FIqRDkIqOUYV5jgg16pclW4elJd1iHLjdOrPln0g4Q0ym8XrtJTLH3EOco_NS1T7IhTs0IMH0s5rkdyNy_UztGDjJl4b2Z5FhCcIlh0o10ui8koROUG3rfP143dx2Qesy_ug-sos_Iu9X7UPNaAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری دیگر از مراسم افتتاحیه جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/658550" target="_blank">📅 21:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23fb166215.mp4?token=NVnhenlaeXEZBFyyjzz9EKl_N28f6hTJJkdBLaV5VBf1SSXz1t-M-ooEcOgRp7qjibUKdQe91Mi3hbIvcZXLGV9FWSiApBWL-MezilthJQyhN_-VoPjDIl7SbX1sGVMjYidBopkLvs5Kwk0gIB5dXkyouV6M7_F9ETE2uHZNfN9sDMWvf6dEfOwrF1TwZ6mLZzFh5sMMT-WsFnjVZyfdRbvWxKeKxgLnWPWBdxo3YKgPpb1ouqg5VDd5wTg8YJLDY5hdroW6JjYPD6stwZ7b3YdoCO-TSSYvq1I4m0_oLsWaAOPVd2Je5ngJgtBSfvi50uHj9qktF5F-k17UCN-EiS0YyZIYyRfph8gj1iEjoi3CiU48pgjCFPAEuc_Rf4IMWIDvfKwLVEiexkSAAn1JM_C1jf-bdYiXKf48GXQ6kwsPZnpsinphdkC_iiA4RmwKLsG0rwy8ZsY9-09spwnCUeUl66bncgiLCF31shX936wKfUxp4Ba43qHxomNbexnLxARGDw2dpYg9MK8taW31T2kJPJtJQdoCdEnPunTEHAbJPHoVXyVz4Tnb1VvfqAdL3TfOZQ9kU3PaX9Po0aXi1W_hls6XWpzEddhrMsJmeUheP82AENNFR80zc3-F8eRxnXLRfL1m1Qx4MUcy5BQEiAEc3diZU9ZuQRzZR2y81Hk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23fb166215.mp4?token=NVnhenlaeXEZBFyyjzz9EKl_N28f6hTJJkdBLaV5VBf1SSXz1t-M-ooEcOgRp7qjibUKdQe91Mi3hbIvcZXLGV9FWSiApBWL-MezilthJQyhN_-VoPjDIl7SbX1sGVMjYidBopkLvs5Kwk0gIB5dXkyouV6M7_F9ETE2uHZNfN9sDMWvf6dEfOwrF1TwZ6mLZzFh5sMMT-WsFnjVZyfdRbvWxKeKxgLnWPWBdxo3YKgPpb1ouqg5VDd5wTg8YJLDY5hdroW6JjYPD6stwZ7b3YdoCO-TSSYvq1I4m0_oLsWaAOPVd2Je5ngJgtBSfvi50uHj9qktF5F-k17UCN-EiS0YyZIYyRfph8gj1iEjoi3CiU48pgjCFPAEuc_Rf4IMWIDvfKwLVEiexkSAAn1JM_C1jf-bdYiXKf48GXQ6kwsPZnpsinphdkC_iiA4RmwKLsG0rwy8ZsY9-09spwnCUeUl66bncgiLCF31shX936wKfUxp4Ba43qHxomNbexnLxARGDw2dpYg9MK8taW31T2kJPJtJQdoCdEnPunTEHAbJPHoVXyVz4Tnb1VvfqAdL3TfOZQ9kU3PaX9Po0aXi1W_hls6XWpzEddhrMsJmeUheP82AENNFR80zc3-F8eRxnXLRfL1m1Qx4MUcy5BQEiAEc3diZU9ZuQRzZR2y81Hk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
⁨ ⁨ سوت آغاز جام جهانی به صدادراومد
⚽️
آماده‌اید برای روزهایی پر از هیجان، رقابت
وشگفتی؟
🎁
این بار هیجان فقط به مستطیل سبز محدودنمیشه
💫
بانک شهر با برنامه‌های ویژه، جوایز جذاب واتفاقات متفاوت، قراره حال‌وهوای جام جهانی را برای شما هیجان‌انگیزتر از همیشه بکنه!
🔴
همراه ماباشید تازه شروع بازیه…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/658549" target="_blank">📅 21:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658547">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
درک مرگ اطرافیان از جمله همسرم و .....
🔹
00:07:20 رازهای مگویی که از گفتنش منع شده بودم
🔹
00:18:40 لحظه‌ای که متوجه مردنم شدم
🔹
00:27:30 نشان‌هایی از حضور روح من در کنار خانواده
🔹
00:33:30 واگذاری مغازه و امتناع از فروشندگی بعد از تجربه نزدیک به مرگ
🔹
00:39:30 رؤیت مرگ همسرم در برزخ و به وقوع پیوستن آن در این دنیا
🔹
00:59:20 رسیدن به پوچی در پی افکار علت خلق شدنم
🔹
قسمت دوازدهم (صدای سخن عشق)، فصل چهارم
🔹
#تجربه‌گر
: مسعود نبی چنانی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/658547" target="_blank">📅 21:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658546">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
عراقچی شنبه راهی پاکستان می‌شود
ادعای الحدث:
♦️
وزیر امور خارجه ایران احتمالاً روز شنبه به پاکستان سفر خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/658546" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658545">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قهرمان جام‌جهانی ۲۰۲۶ معرفی شد!
🔹
یک اقتصاددان مطرح آلمانی که قهرمان سه دوره گذشته جام‌جهانی را بر اساس مدلی اقتصادی درست پیش‌بینی کرده بود، قهرمان این دوره را هم معرفی کرد.
🔹
بر چه اساسی و با چه مدلی؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658545" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658544">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای نیویورک پست: ایران پیش‌نویس یک توافقنامه را از طریق میانجی‌های قطری به ایالات متحده ارائه کرده است
🔹
منابع می‌گویند این متن نهایی‌سازی و برای بررسی به واشنگتن ارسال شده است.
🔹
یک منبع آمریکایی دریافت این پیش‌نویس را تأیید کرده است، هرچند جزئیاتی فاش…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/658544" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658543">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
عقب‌نشینی ترامپ: حمله امشب لغو شد  ادعای ترامپ در شبکه اجتماعی تروث سوشال:
🔹
با توجه به اینکه مذاکرات با ایران به بالاترین سطح ایران رسیده و مورد تأیید قرار گرفته است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده امشب علیه…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/658543" target="_blank">📅 21:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658542">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084dc07fe2.mp4?token=V6-Wuwgd1RFrHl6ZYalNqFe2eVtlOQhytzlJ4Ypz9Syiw_-PcjlLxcJAMSvLq2uBqwH_Qcnt35qxs3lSl2fjKF3P1dD1ZM57WKtAI2NgXfmIYylR-EQinm6ft0mAbx9rns3FI4dH9WxCYVwyHIR2dlWkADe08_-Ua4PMHEyF7NfBZUr3MN008gFJ5Zc41wE3XsJ9632HC1cgTBgM0GRHMTt4OLuYHYCSvH9wzlVvhZPOrAljGbun2zaz86FAssplBpbiIF2r19eckZwk7e_doUWbH6CQq_1oyI2c6jZ83-nk_frPUWfvRBBsMAqGomqb-2OfsGrmKCDRSlwcMKoeWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084dc07fe2.mp4?token=V6-Wuwgd1RFrHl6ZYalNqFe2eVtlOQhytzlJ4Ypz9Syiw_-PcjlLxcJAMSvLq2uBqwH_Qcnt35qxs3lSl2fjKF3P1dD1ZM57WKtAI2NgXfmIYylR-EQinm6ft0mAbx9rns3FI4dH9WxCYVwyHIR2dlWkADe08_-Ua4PMHEyF7NfBZUr3MN008gFJ5Zc41wE3XsJ9632HC1cgTBgM0GRHMTt4OLuYHYCSvH9wzlVvhZPOrAljGbun2zaz86FAssplBpbiIF2r19eckZwk7e_doUWbH6CQq_1oyI2c6jZ83-nk_frPUWfvRBBsMAqGomqb-2OfsGrmKCDRSlwcMKoeWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم افتتاحیه جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/658542" target="_blank">📅 21:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658541">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSWnCS_GCkODUnaCK2tK3rmM7l-l39Kl2BiOmCjKRckHmQs4VjrXF_6MAKIb6nl0K1dPXs34U-LEiG5vWJKjqrKxe74373SVoILIknpYxuxcAHg5dJ-37lVEhwHusuNcpKILqxhFIk2RFGFPJffr1EcNaTAIjF_k2I1l13q4-P38PH1wpkowUaYokMmbw22V7g4DUxJFxHzbKK2XmiZU6YR1knj0ToLcdJRXtyim-WeQe7eQAnxxtgjkIki-rLcA51YmwcR-HSXuCSj98m8mRqZNgk1OCINSr6BHZF0clsLCvpoPpKUdRW2VyMfATLleEcnu1VwtxGGTsu1myI2YHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تبعات دادن امتیاز میزبانی جام جهانی به آمریکا
🔹
ورود هواداران از کشورهای سنگال، غنا، کنگو، ایران، اردن، کیپ ورد، ازبکستان، اکوادور، هائیتی، مصر و الجزایر به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/658541" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658540">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtZ3mVuy0c9Fr6adl2JjJyMj-8NwUNRZt6oh4ITzdfftHdhK9fdTQ6M2pYnt4JPcibN0NmwQaB__zvCjeQTyvmXnpuF68WzC8Z316Ot2Qhj7kcLNnPNQ-egvg5UK_MU4JLu3KpWadPBDJt1RrKkwTSCMojmiTdGTv7fBclyUk2CkuWrAhGn24aVnIEM-XWxONUNoxtUnjXcFX0LPpMANUwkGPtiX5QlKIY51uNOhK_B2ANr2ZhBGJv7pVkAQcOBHX4BW_J_UW84yEeV-ttZxDSLHMRjNZXsKAZoy5iWhteamlQEKIMP0Q2yXpo289y1TAfqHpyePqiK1Ywr8-f_WPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت به زیر ۹۰ دلار رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/658540" target="_blank">📅 21:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658539">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oh6VVWdna3U9kMq4tPhuPfR5uERw3gW_aaYCl4Tug3Gao5Zhm4p2ooNYfCtW3lhz9IatKHL_IanjvHCzTrvM6rhUEWltVxD6AcwHN6Cohq7GDS1wQ_43hFgHBo8Vu4V9YzJfwdN1-GbkHtJa7UGh2LPpY1x-ULulb55o_WCcL50FohK7hpO-cISgYUWM91Wf-X2Th89-oREA3sR__DRa6qKISJSpjjYWnMOm49xv94FneN-bVT_g-beJ_0w3t7aANGQ25tMuc1_HnIRj2lqLYSTcoWVMvvSE8n0FjuJP7SO6BBdOq061FltVDuIxYVGcjAhQwNCPn-95LlBOFO8WWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موقعیت رادار هشدار زود هنگام AR-۳۲۷ که گفته میشود در کوه دخان در بحرین مورد اصابت پرتابه نیروهای مسلح ایران طی حملات امروز قرار گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/658539" target="_blank">📅 21:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658533">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gh_NL9PIGjuTxIujMdII-UG16X23CkWJFpJHG_lgyAWz4LPpCpCI860QT1hh6rB9N6iqeYiwOxXHIVPvHSvM9oAhBAF8Q-I07wcVd9zzb9YINvaGMh03M5olk3510-TmUXcE9V4GFA9dZ6QI2zYmeEaYyUv01pBxcL9n7PDQ0FMvlGbUfCfyF6qVUdk0Imwg1Ej_10G9x38vEVRBHqARUVmHuMhxrs6wnCLa7Udar-gsdYELakOkuMi-Rpmelwpj18kzkniTBdhDxx2aN10ZQ0NK3tSiYNzzPwsnCDvygFmMWSHtwVkbEqnxoG-bGsK95Uw-2btoTovE85dVyMYE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-AqESLEClToB1ywUoU3ReQe1XsOgpKMQlFJ134lgwo9My8mcfMjBQZtlJIG28oB4rCUznI8G9Wa1ZMFUOPC0W2i-YUR-LoadT3tQTFvGrK2Hqa2Z2X19r4YEkPGIMaP2hYymYX7Vv4GyHrbjhUXuKmEC08jUsTJ_2zsKf6jF7TEdqtxzXklO3-8_thNOgLNI2qyyidNKDOmmfzUhBtuaBFIxLGYS043G8TIYQulyXUf2QpB-3FDwpuujfPNaJdRgNrqwq5C4QFIsAIxLxDWKgY1WXEm5xQVN0nEiPCylt_7IsBGRW6VC2f3lEsHMpnTQA9WjcRGmcw55_fTqDKnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxsW3Hn7fWyceL3fgfAGwwpH_8ju72SJO0bbCK-ZvPmQMs5klwjpWODeElhEiniMQnur4Sn1nZNOsQ8sJ2k4JawSPrJmbfFFdquzC3aJ3x4vcpVDFryae45p2A5qZ4pzOTtrxcQX8w6psMwu10DW-hL3_MgwDQy0jdKLKza69lCQt8MR4tateVjVHUsPqyblWtf8JqJlNsDSP33eOg1mHq3FPA-F-IpPJnefo0ApRUS0OPBdCKpdgZFDxc3eYfL8Lc4BPeLS1LGt41W-RnsBByd3ALjjh-v9FGzMYShUSvf3yQvqnzxwYwi7hFVmmbsyfeSk2i7Hs4Cy5XuGyaVcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOXYYeEkv85Fwk8K_xuZy6HtVBRVOgjq7TbG1YIjoMjJDls7ubEXUTdm9Yid2e5rI5Hgcg28CYzOjwQFhxgiOdNoSBX_L4OXhCcaK7WU-ybLqlL9sI6KYAwDPngRG-14IQ9UXySZL_0xzch1aylX3mdjHylLHUcwpShnhy2PMp8VSo6XTuGG9Dmw6yXL2yHJwWNFGfKekRGEpokUpLsvDejPlIFQGfWCz7Cz1GMu1CRBm_iIcjxcgiEG60FVK4q6iDgRytJXgLf32rgKW_XFdWXqwzUIjKuN4O4BHyE83_196Q2IrWEe4Z0HirxNrCd4NI06bDwUcCyjflVYIaZ5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vD7JZQmY-fbsZ7Dj2GTC42FGJHwE7gzqM9NoSfdqBjyUDvq3RuyBg_lNieFGmH8CE90QBt0H764Xc1wNxtY5zcS6AbcYR7qzWMF8Tg1Q4XrisfZavPphx5z5ha4LqfZbjMsMKyH4v5NhAEhbJadODIvTGj7qNmadNeA7f6rs0lbiIuknGS_bUd41NEH3rURGFNit-Mrm7at5eBxF3rQgv2eiAO32pWQIHzE0qG5W4M2LFwgEitYC_TEZ297xjNmPnYHSaXOgwjGfuSrnBz6LlBPFUWjppcM7-137iAnjCxh1CJ3v2pA_rPxDkpbQDaUYxbTkCUy9efxVZ0KT5HDLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dT4xfRooQa8siHd5FAVZa627wwUOAgVGdGNoPNzOWMOnT5tZOtglc_4h5UCOUuC7P_6GeUrm_M3mZ17OHrFzEjpPi1HEFEBjNdUosULJ8R2oanWRxUHkZatIZIP1FT16GS6LoiPxcZALUPhN7MwR-rm3EN825ucvxRAFhyD2S_nM6c_i3iHQNQ3mUnnm9-azoBjFwQ4TR6zfcuPD_W2Xw6TobvTiuv2WVzXWEXH2q2yek8_kH4CKXAVU648yvr91miCiLc6WKjG8rXETPDgO2ObNoR8fYQ1bMKTltm9lmq_CRplieYXFP49c7ECt6UOA1kJeGWQBZkyht6p1ZVqazw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از هواداران فوتبال در حاشیه بازی افتتاحیه جام جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/658533" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658532">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
عقب‌نشینی ترامپ: حمله امشب لغو شد
ادعای ترامپ در شبکه اجتماعی تروث سوشال:
🔹
با توجه به اینکه مذاکرات با ایران به بالاترین سطح ایران رسیده و مورد تأیید قرار گرفته است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده امشب علیه ایران را لغو کردم.
🔹
مذاکرات و نکات نهایی، هم از نظر چارچوب کلی و هم در جزییات کامل، توسط همه طرف‌های درگیر شامل ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران تأیید شده است.
🔹
محاصره دریایی تا زمان نهایی شدن این توافق به طور کامل و با قدرت به قوت خود باقی خواهد ماند
🔹
زمان و مکان امضای این توافق به زودی اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/658532" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658531">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB6cqKr_rPbFi9rf2pC9zPqvlOhbTTyyYchNZOUrtv2w4_vUiRyQ1XPBpjlj6FbLbHsoNrEJlaYE8Z4S1Fg6y-fWlFAHCmwE2_UYe3iX84K-WFd9b4lR4U8l-sz4Cn9_VU7MYrtooMXDmkpJn9FgZAmg0BznRwDUKPMiYCXw4UV_F0wlZwO-vfpvGErIwh3OltBph2m5ib73FqQDB6V88_fjMe--MUOE6w20KtSEoF3ibF7U3VY3OqaAkHmYjMD8NxAOgGdE6-dixRS-X992N0Vsw5bqKBYysq299POKfooQpzKvXiZMFzzsYvX4Mh1cDw5V4p41BnKEIJvEwPwNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین رتبه بندی شبکه های صدا و سیما در میزان مخاطب/ سه؛ آی فیلم ،خبر
🔹
جدیدترین نظرسنجی در خصوص پرمخاطب‌ترین شبکه‌های تلویزیونی  توسط مرکز افکار سنجی متا  در سراسر کشور برگزار منتشر شد
🔹
مطابق  این نظرسنجی‌ شبکه سه در رتبه اول پربیننده‌ترین شبکه‌های تلویزیونی حضور دارد.
🔹
شبکه آی‌فیلم و شبکه خبر نیز  با فاصله کمی در جایگاه دوم و سوم قرار دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/658531" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658530">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciZK72UTUGxpjfNI4MkXx1a2IialHq4PwMo-IvJWJxVxnKMP_tY3fTbTICAVexIFz1epdJ_xi_KKBgIGWr0EkaeOHPJlXNK7nkM-EjqrRE_GE3qy4zZuueLCkumjSWqNJBG-yXQrAQ9QHCI4ohtW0DVtnzKfQtQX_RmowhMiMYSUfRjSWLUv57mAJF2xJp3K7rTspt-gifQzjczxeoJAjyf_jJrzF1dY4CMDyuUEfe8dFjJVMuX5LkoyDeWUBdqkUuNED56ehEJevw7uNl0Q82VICn7GOoJOXNseBvjR4nmU07VHc4lqGvbtEJmPEAHY3oMoeyHcg9yosdfcWg7bEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جوان‌ترین بازیکنان جام جهانی ۲۰۲۶
🔹
ژیلبرتو مورا، هافبک مکزیک با ۱۷ سال و ۲۴ روز سن، جوان‌ترین بازیکن جام جهانی ۲۰۲۶ است.
🔹
رکورد نورمن وایت‌ساید، بازیکن ایرلند شمالی در این جام هم شکسته نخواهد شد. او با ۱۷ سال و ۴۱ روز سن، در جام ۱۹۸۲ مقابل یوگوسلاوی به میدان رفت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/658530" target="_blank">📅 20:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658529">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
هرگونه خطای محاسباتی دشمن پاسخی فراتر از تصور خواهد داشت
وزارت دفاع و پشتیبانی نیروهای مسلح:
🔹
بی‌تردید نیروهای مسلح جمهوری اسلامی ایران امروز از آمادگی، توانمندی و قدرت دفاعی قوی‌تر از گذشته برخوردارند و هرگونه خطای محاسباتی یا تعرض به امنیت و تمامیت ارضی کشور با پاسخی قاطع، پشیمان‌کننده و فراتر از تصور غلط دشمنان مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/658529" target="_blank">📅 20:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658528">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv9r0CZzeSlki153tR_NQ5EG4kUnj7BFMGxnNd7niNM5hecKpMTmtGqrxsk9FzldEZP4TmQcbmmrb6Q83-xffW9AOqmgHNXafOPk4eh4zt7zulVLb-vRWaODQ_jZibF6FuJB3jQZvNTVcg1KJRV2BNhWZ7dLdHKtk8l0jLA2Wztsb95rgklCFBTco4rYjPmCxT2NvJPKWaqHVn_xjbpuPDyUHsgbtt9AZC253FcTljp3uJGwWqw1Tz21NicBtIUKd2XaVvNJTaQ2pOWx8QKY3iTQy697W2GIFkgcoKXlrJIpyHlMuJCNcu6ZNu8sRijcVGwe7IDOhzyG1XY36tmVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دوره "جنگ ضربتی شبانه" میان ایران و آمریکا/ آیا جنگ‌های کوچک به جنگ بزرگ می انجامند؟
🔹
ضربات محدود و کنترل شده به راحتی می‌توانند از کنترل خارج شوند. خروج از کنترل به راحتی می تواند سبب ازسرگیری جنگ بزرگ شود و دو طرف را به عصر جنگ سخت (مانند جنگ ۴۰ روزه) بازگرداند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3222279</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658528" target="_blank">📅 20:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658527">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbAdJzfPQ9Xuy4l_z4hsXazq6Gn0ftAPYIjWfDOGmwukYJhDrJ8MHyRpvViEi5CisgPYcDf3R4ZavfUjM1Sj3OHGyzgIEjYpauoUATgiC20OOq0pcjcUjDxRmmLHOUHkC7xR_Uj4Yzh7QfunrffNulN0rhxhmBYWCZ1-gE35NKjnJJ1QZdfNl8rlSRsfd9-m6YoaTnaGkT7JuvOM0jmje4TeAgFZtnROtR43VGNuwZ8LYILxzQkaF2U-njaRMlruRmHoi5aS2cYyqb2tP4P_XZN3i92MIZCmLDThSN7naF_-E5P3ks6DGGnSuqfyiXU-SYdF4TeggK29tkeMnS1M9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطر هجوم مار و تمساح به کمپ تمرینی تیم‌ها در جام جهانی!
🔹
به گزارش نشریه مارکا، ‏پس از اینکه تیم ملی سوئیس هشدارهایی درباره وجود مارها دریافت کرد، ‏تیم ملی نروژ نیز از وجود تمساح‌ها و حیوانات وحشی در نزدیکی اردوگاهشان مطلع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/658527" target="_blank">📅 20:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7619da40.mp4?token=A__IsvJY9K3KI_7yVgfuKcnmQneWkBZecpAYBWw49a7d0vkgsZHBdY_pG3IFXKQPVgrPpBVHJbYJUBrZQVuwc45sF0DugEQr21sddCW0WOWTDFausUoCjRgxpNCWoBnToycZpIOusqhRTAA2nLzof8JCWAOACkwezOwOLe7hHek-8-NMSRtszokrxgMUHAh4Alblco81wBl1XYX7FR9VB0q9HFJlNGnuDQrCFlQm4j0mD4Uj1YBh5L5sswGlJhAk4lkmSx3x34bQ2mPOykMBPt4_nUq-2V40342I5RxTZrquQhyQ_WKOBOyDZJ5RIpkWLkvwOaZ-o2RK0Tq8uw0T-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7619da40.mp4?token=A__IsvJY9K3KI_7yVgfuKcnmQneWkBZecpAYBWw49a7d0vkgsZHBdY_pG3IFXKQPVgrPpBVHJbYJUBrZQVuwc45sF0DugEQr21sddCW0WOWTDFausUoCjRgxpNCWoBnToycZpIOusqhRTAA2nLzof8JCWAOACkwezOwOLe7hHek-8-NMSRtszokrxgMUHAh4Alblco81wBl1XYX7FR9VB0q9HFJlNGnuDQrCFlQm4j0mD4Uj1YBh5L5sswGlJhAk4lkmSx3x34bQ2mPOykMBPt4_nUq-2V40342I5RxTZrquQhyQ_WKOBOyDZJ5RIpkWLkvwOaZ-o2RK0Tq8uw0T-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درب‌های ورزشگاه تاریخی آزتکا مکزیکوسیتی میزبان افتتاحیه جام جهانی ۲٠۲۶ برای ورود هواداران باز شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/658524" target="_blank">📅 20:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658522">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromtalasea_mag</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0zXdJ1sZlpPpx9COgVKtdclheorwImHiC8W5YM5H8EyDeVdfeTsMJpVjO5BMLfmgnk8-WQUcenf0O3EICLQrVQ79fI1pZhlrzwLcFmCDoSwce6PrYhdp8QUwzUDT1XB5u2rHYIeDe4HKiwscVzdiKP9Lz2NJaK0aXvQMprhPUXdceSAKdqN9LmN9PVZJGUdOGkrGcnjw6be9b-tBEF1f-3ieU_lxuFEFNHuH-0jGUBwMOBXjjG-O_gBh49YvjE72ZJSXK_AAewsOVwuB-C4LGYH5BLSOl_9dRsBEQHmz2Ucr5NevAGoiFNtByIf988KP_6TuGLan3L-uYzoIXJz8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/658522" target="_blank">📅 20:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658520">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794ea7d026.mp4?token=DH3eBA4zRJpS7gwJOxNOYNBbNWYE3KlfH2MPrh9uf-i1VpRfTZSK6wYYPFkglD4w2cCtzjq1G6-5O5EI5klYjmUTnh5fDGDbOvmJnKFcwummxye_I0dxPqEG7alWG2228s6yut_Q5elfSU2WUDK5bSVuj2K-WiVidRoZiO-_U1B1wiYyGFWd7dldOOCsL5fo0R4irf-vqdSWzKMYFOdHxcdP3aT0UwpvaxzRr3qlSdszQVjTUKgdC1WJj7Hu_totmYaVMM1RjuipDDTfRsv59VI8VTPl8X1_pHqE6tBu8j6vbFPk3QdyoZSOFLR5milM5epr_gnr-8i1J9yltFUXFXIWlvqhvUOCwvFXw6xrrmd1WwVVo31krtKF5J7evqUWm9TrGqrE51Di80JUPVwiJ3PCAVZPy9rAL-ZBkVy9IzfReng2b39bvkcGvLYYBBJPN9klMEijYv7eiCGUytPCLnWdJIQtQ1uBLjYU0M6yYck1ncsGC2O8zjen-2ZbON2lTmeV-7h6GEnsXgn5v0JJooVnEIe_cgNJBVOP1rZHYxnTy9Qp_mcoT88PKSfFix9IWCPR2xz0ZP4igZagBKcwM4LBek2YKP9VZT7CAKegSGHjS58sL8BbgsL9nloDM6ZfxBCcnFIDmwVhn9dZFwdVtYm94vPE2WAtBbnTd47FIQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794ea7d026.mp4?token=DH3eBA4zRJpS7gwJOxNOYNBbNWYE3KlfH2MPrh9uf-i1VpRfTZSK6wYYPFkglD4w2cCtzjq1G6-5O5EI5klYjmUTnh5fDGDbOvmJnKFcwummxye_I0dxPqEG7alWG2228s6yut_Q5elfSU2WUDK5bSVuj2K-WiVidRoZiO-_U1B1wiYyGFWd7dldOOCsL5fo0R4irf-vqdSWzKMYFOdHxcdP3aT0UwpvaxzRr3qlSdszQVjTUKgdC1WJj7Hu_totmYaVMM1RjuipDDTfRsv59VI8VTPl8X1_pHqE6tBu8j6vbFPk3QdyoZSOFLR5milM5epr_gnr-8i1J9yltFUXFXIWlvqhvUOCwvFXw6xrrmd1WwVVo31krtKF5J7evqUWm9TrGqrE51Di80JUPVwiJ3PCAVZPy9rAL-ZBkVy9IzfReng2b39bvkcGvLYYBBJPN9klMEijYv7eiCGUytPCLnWdJIQtQ1uBLjYU0M6yYck1ncsGC2O8zjen-2ZbON2lTmeV-7h6GEnsXgn5v0JJooVnEIe_cgNJBVOP1rZHYxnTy9Qp_mcoT88PKSfFix9IWCPR2xz0ZP4igZagBKcwM4LBek2YKP9VZT7CAKegSGHjS58sL8BbgsL9nloDM6ZfxBCcnFIDmwVhn9dZFwdVtYm94vPE2WAtBbnTd47FIQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک مرکزی مخالف افزایش قیمت کالابرگ نیست
🔹
منابع نزدیک به بانک مرکزی می‌گویند بانک مرکزی معتقد است حمایت از معیشت مردم ضروری است و تقویت قدرت خرید مردم باید در اولویت باشد.
🔹
به گفته این منابع بانک مرکزی مخالف افزایش کالابرگ نیست؛ بلکه مخالف تورم است و معتقد است منابع کالابرگ نباید از محل چاپ پول باشد‌‌.
🔹
حمایت از مردم وقتی اثرگذار است که از جیب تورم پرداخت نشود. اگر منابع کالابرگ با چاپ پول تأمین شود، افزایش قیمت‌ها خیلی زود اثر این حمایت را خنثی می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/658520" target="_blank">📅 20:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658518">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB0mBF7Ns33VTyZVPSxWTvG0YuLaRAMe4za1YqxHxCfpW5iXAy1Ae4RYUBxmb03wbfXQYzXc08ix5c0AvJVSRKlod2LZ6VyDJLYeB1USfawHZj3J_Zs9PHPmOw2LS4vlBsP6Q0stCwhtcCCfnQlscOAagvDqc92GtJXwt_HqIpkwyoFHmdqN3mSqMh082tWxRieYHx5ANi_PPqxKdqO4O8hfMYKyjbQGy2eQH7l5mUKscl10sUfdTBxK7Hn_UE8ju0Acamz3SoH-aDWn5RT4cOqYGuJfJmd0epP3IEOWWKN_pKILH2dJ1IeDFykN9huN7obLTa2SNrRKemHuHmbp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خارک ما
🔹
با وجود اعلام آتش‌بس میان ایران و آمریکا، در مدت اجرای آن موارد متعددی از نقض تعهدات از سوی آمریکا گزارش شد. آخرین مورد نیز شب گذشته رخ داد که طی آن، حملات نظامی آشکار و گسترده‌ای علیه خاک ایران انجام گرفت. با این حال، این اقدامات نتوانست اهداف اعلامی مقامات آمریکایی را محقق کند. رئیس‌جمهور گستاخ آمریکا امروز در پستی تازه مدعی شد که در آینده نزدیک جزیره خارک و سایر زیرساخت‌های نفتی ایران را تحت کنترل خواهد گرفت. این در حالی است که ملت ایران در طول تاریخ بارها ثابت کرده‌اند در دفاع از تمامیت ارضی و حاکمیت ملی خود استوار هستند. جزیره خارک بخش جدایی‌ناپذیر خاک ایران بوده و خواهد ماند و هیچ قدرت خارجی قادر نخواهد بود حتی کوچک‌ترین بخش از سرزمین ایران را تصرف کند.
🔹
هفتصدوهفتادودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/658518" target="_blank">📅 20:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658517">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d7dac072.mp4?token=bgnYfdzn-toFUVzVZdPsi3f2jd2Ezg8dCS5l7Q4CYtj9Jm3Z75U9MmVH8wHQZkTkNvqpRT30ZI5DfgIVv--dlshHQi64Degb6QxFpl-aRpg6mAIvID2gfcL23Yhaz-wY0hNpZbTFzaGpHTA6QjFpjDi7Whdh7G_YZW988Lwx6cFrbdl1XkhrQJsaoHyv8s3dc2q4wxsQdd-tRlZ9RzFA517e8Gxkuz3j0Rca_LBZTDssLUWjOpKmYFv_SlW0v9OmOREOw3Jt3A7E0S0fVhgDt8WEHh2VuaJt2Dhmezc7gBD3vJS-_tLN6pUweBnF5V9LIWwDN-NrZr-t6roKk_gepj9wvKbll59jtNGzs1uAV-V9y51qlH7ZY1tB19SLtJR_WSo9f7-JJaduQZTZzpNogEnsxbr9h2-3zDLDo_tsupWoFN_WUQWbMpia0m0VYXYGqnCy_G_ABEKqIIPsMCV2CrsG91W-AWRAFc9VdYEu2vjGTq7velAn6U-HOt2vL3bORVR6j5PmFKLdIgwbz9BE8RaWILLIXZP6q_CB7--noPh-KRl7mRQBdbeDnHgp0C-kRFg8VSf_bN5l-F-PCfnFn5mxL0roVj-YsXk40JWn1njv6_KKkSb1iufo6YmBKxKUcwmkElMzBUa5rMhHBZ-hSQSphj6fpooAq8j9E0AGVGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d7dac072.mp4?token=bgnYfdzn-toFUVzVZdPsi3f2jd2Ezg8dCS5l7Q4CYtj9Jm3Z75U9MmVH8wHQZkTkNvqpRT30ZI5DfgIVv--dlshHQi64Degb6QxFpl-aRpg6mAIvID2gfcL23Yhaz-wY0hNpZbTFzaGpHTA6QjFpjDi7Whdh7G_YZW988Lwx6cFrbdl1XkhrQJsaoHyv8s3dc2q4wxsQdd-tRlZ9RzFA517e8Gxkuz3j0Rca_LBZTDssLUWjOpKmYFv_SlW0v9OmOREOw3Jt3A7E0S0fVhgDt8WEHh2VuaJt2Dhmezc7gBD3vJS-_tLN6pUweBnF5V9LIWwDN-NrZr-t6roKk_gepj9wvKbll59jtNGzs1uAV-V9y51qlH7ZY1tB19SLtJR_WSo9f7-JJaduQZTZzpNogEnsxbr9h2-3zDLDo_tsupWoFN_WUQWbMpia0m0VYXYGqnCy_G_ABEKqIIPsMCV2CrsG91W-AWRAFc9VdYEu2vjGTq7velAn6U-HOt2vL3bORVR6j5PmFKLdIgwbz9BE8RaWILLIXZP6q_CB7--noPh-KRl7mRQBdbeDnHgp0C-kRFg8VSf_bN5l-F-PCfnFn5mxL0roVj-YsXk40JWn1njv6_KKkSb1iufo6YmBKxKUcwmkElMzBUa5rMhHBZ-hSQSphj6fpooAq8j9E0AGVGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای که به وضوح نشان می‌دهد تعدادی موشک مستقیماً بر روی پایگاه موفق السلطی سقوط می‌کنند و از تمام لایه‌های دفاع هوایی عبور می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/658517" target="_blank">📅 20:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658516">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
هشدار قرارگاه مرکزی حضرت خاتم الانبیاء(ص): یا صادرات نفت و گاز برای همه است و یا برای هیچ کس امکان نخواهد داشت
فرمانده قرارگاه مرکزی حضرت خاتم‌الانبیاء(ص):
🔹
آمریکا از یک سو حرف از توافق و مذاکره می‌زند و از سوی دیگر شرارت می‌کند و این تناقض آشکار در رفتار و گفتار آمریکا عامل اصلی ناامنی در منطقه است و به همین دلیل امنیت تجارت و اقتصاد بین‌المللی و کشورها، بویژه تنگه هرمز را به خطر انداخته است.
🔹
هشدار می‌دهیم چنانچه آمریکا بار دیگر بخواهد حملاتی را علیه ایران قهرمان انجام دهد، پاسخی شدیدتر از قبل دریافت خواهد کرد و آتش جنگ علاوه بر ناامنی در منطقه، فراگیر و گسترده تر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/658516" target="_blank">📅 20:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658515">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmdwrZ1qzt6v6I0XM04HrqSQCNApsoHBkpyi7TvaYJcmOwszS0fIttJedu7ZEghdtb-N5whWyA2Otj_--qEmtYPtYrvlCkDD9Xc0bWFpbp-pmVHIoKjrjvpW3oeFPlaBzfKs4wf4WpwjmypkwwUZ78ce5_HPDkhA4U-PPfXaoU85XQ7Hq8ZoFRbOp2WXA6-3_sYg4qz5fTPGfpJGC-BqQAxSy1-isktS2uEdKH8O55a1oX_cn42YCbKBmwe-5AT59ALN9AG1TOipgmOXKVTajyJP1-riLQCcdeyVV7ywV_pk57J-Bw-8EtA43ySFTeoHjcQEr-Qe9Fd10fWMb_2R-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: اگر آمریکا می‌خواهد شکست‌های قبلی خود را دوباره تجربه کند، پشیمان خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/658515" target="_blank">📅 20:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658514">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHsTGAMmFLyJlJnMkzYk3X57WPlvZLhhlgsEb4fFjJHL-2HqwMs1QVQ4l_0HLLR57p4DlGvij37KEiWuMYMA__BbxPHU4lVUK60hm7bE9yfIu7N4YbHD_LoJAs6oqND8sA2Yopoi2fLY588tIauvTveLWsoqmPj8zf8ujK3qMsJfrOZvbLkfIu5rq3qAyzBuDVBJb_d-SqbQdGsgfPyMgjKPz8eA4rCmo7SrI74SJTpOADuLBaSIT_hmxGs01GxT5SxFZkGSC0L6nhakTVU0JWCdQVgtmgtTWnmGB_HGgsYKkn2wpMI4ytqHu4QbI-jIYLi6m-y-h_jc0u_djJgKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعت شنیِ انتقام به کار افتاده و عقربه‌های زمان شهادت می‌دهند که هیچ جنایتی بدون هزینه باقی نمی‌ماند
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/658514" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K51X_3DMilvECRNca77_3ZU4Fs9JHPFNsUnYJ93VGk5xO3sNrgEcsbs3PByPgf5yJxqQTbh_9UNxdebKxNPZWRV4BErnfttseLaA2pK202kfUnshC9CJrAHZ3CL7etdd-oq5hyHyomCAG4_96rYB7oCGFN2zFnORZeDOrwyrSZTdJoSzIO97M6Ocb0q9czu_sHgHyk_lFJamQGZBvsQQf86x2ZzXXJji3xMjlxlgododWxZvnXGznqCnqIvK6NO5OFZYTXnK2lU5DvwK2gPeHEQHcZlWamUFBCtzkwduVFwrqj5gag4vKWbqIdbiOVnphudHK9-gJW5mOqzF5Eeddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWRd_U-YNgBNt1Rrd0ki9bND5d1zNi0sqfv4Sy6xt9Z07OX8t71dd3Jxse6FAklKLNZM294_BkglRuDoIIbTCC2j5m0F6ih18pje3xuJbUeFhdoLsBaOuzAd9VpWUCGcyT_AS99JfQcF0zFAFa0R5dvfW7r9Gt_ORtbI13wpFnj6oBNn3KE4aNjf9xAR_ePrFhOfR0hy8SPwtnMHuEU4wzWSlhqM6Lc94UEsfVmkjXOHxHqv8yXxBBB1rTMdKefVOlcKXkTpZhyBzcWS3FGna5jczwwGrV9G76boQ4CHBJvb-ZMOna9-ypD5y1lduMaHe4UNzVzLbXkggeV2lO_Mow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: نازنین
🖋
نویسنده: فئودور داستایوفسکی
🔹
«نازنین» داستانی کوتاه اما عمیق درباره عشق، سوءظن، تنهایی و خودفریبی است؛ جایی که راویِ نامطمئن، حقیقت رابطه و فاجعه‌ای پنهان را لایه‌به‌لایه آشکار می‌کند. اثری رازآلود و تأثیرگذار.
🔹
مطالعه این کتاب به کسانی…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658512" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658509">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf43df983.mp4?token=m4cz5-d18QHWmA0uCeo38KHo-Av9Xme67R6cru7UB_Hu6Qr9P92-Qim_fX8YnkgJeqQQVr_2vzdGXSvG6QSnyNeEeDFVcNonbfpY0t46cNgcW65evBr22Knd1i-GilhqVKD8emR--FeHOBogramoBt0b2G91hUWJmwqZxzWkYt9cTNo9QSDE5sdoWLnQaatFOxePvBDxh5BlAI1E2PXYDHcPDWmQY_IHjOX94KImXcQDZJVAAjWVHRPp3oKSY3E0UzGWu80kiVjcE3G2uy4pg3hsgdAu_G_jtBh-4sA0OpGCz22a_yjVmVtvE0Cy5ZO-5QCRjo1xGx_j7Su6kzYqHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf43df983.mp4?token=m4cz5-d18QHWmA0uCeo38KHo-Av9Xme67R6cru7UB_Hu6Qr9P92-Qim_fX8YnkgJeqQQVr_2vzdGXSvG6QSnyNeEeDFVcNonbfpY0t46cNgcW65evBr22Knd1i-GilhqVKD8emR--FeHOBogramoBt0b2G91hUWJmwqZxzWkYt9cTNo9QSDE5sdoWLnQaatFOxePvBDxh5BlAI1E2PXYDHcPDWmQY_IHjOX94KImXcQDZJVAAjWVHRPp3oKSY3E0UzGWu80kiVjcE3G2uy4pg3hsgdAu_G_jtBh-4sA0OpGCz22a_yjVmVtvE0Cy5ZO-5QCRjo1xGx_j7Su6kzYqHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلدینگ تبلیغاتی رسانه‌ای باران برگزار می‌کند؛
"نقطه تصمیم "
🤝
همراه با مدیران و فعالان کسب‌وکار، از تجربه عبور از بحران و ساختن آینده بشنویم.
📅
یکشنبه ۲۴ خرداد | ساعت ۱۶
📍
هتل نوین پلاس
🔗
ثبت‌نام از طریق ایوند
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658509" target="_blank">📅 20:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658508">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llYlFW3H615aARj46dzYcv7Q474GvR1ZWqWt1RfrqjzcOQ1-akHE6JbcXKHl8H1wLmIZ8wuIHn9Mh-032UBvdvbBopUePUotaWiWr1JH7E_ITmOdY_OyZvY4vaUqmQ-WD_fUrjBR-Uzz_K8P7eWfqWAnhifKtpjVNUYWHg46CdSLCKIUgAnWDc-8c0CAP4ZAxOO-zSrL8Gor1yOfG2x83d8DyQxKAuIbfZ1jWAY51y0eXvPy-_5ESZ8YVvo5cdAr0PYczeclJ8cmoqhSqYZ4-sG5NmzuHlXIm1flu9nCeCgMYeBKdKTv8V77b_FHexBRIb8RV2D22gCMINru-dQGTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام پایگاه‌ها دیشب هدف موشک‌های ایران قرار گرفت؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/658508" target="_blank">📅 19:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658505">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSJ8YGUO-uwTPuJRRFrxQnk9wWPSFblz6MwM4fnHVz-_efDlY-YHD_WxBnCt1OygWKPoeJFQMpzUeZZZ9w05UdWXomIB6YJsqEtDUQ9WSpvyj4JEjO0oggGSiHO0YHhPAVmN3c4SZR_uS2Vx3YQmMHs3iYmD5SVwZVqDnzrfeYavxZxTEZBG_lYGGdJQTOHe92EHWL8pZ5FAyUJtzDA4mA2206hzT2HNL5wJVrVm6s9aL0narjT2XrU7REMozdj2PLzNgeRoBN4YveAfR9wRWpsa9DlYcfoiatwtDv_9q4sqVK7pFR901Fh3E51bh655B7VU0j-I0YbwDWj0Wxz-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده نیروی قدس سپاه پاسداران: پیروزی نهایی از آن حزب‌الله است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/658505" target="_blank">📅 19:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658503">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fefa4eec1c.mp4?token=b4DCIXFwCgivN13PDDPobLTVGSUJLbRU-PGU2ImFGb1bH9XRna5fIojlEGS5jSAWnzswJClApRoBBRYV9B2Rf-jmi1jzY6QSUXvD-bytyxomBDlrFvJDcKIy07XM_4ERvAjxenRc5S4zbE3lMriNP9tckpzmF4TeZn7u37HCs-U3zyYO0adKpcc4TuTO-bsYGlkTmhx6UlVIUI7Q26dTGmfWL18aQVxhFl4BhNBn5ELIol2kwp8ltTChYmdGS5dcfTEUcmdO7OicXOngv5HxYiYod_HULfwXWuj8ujJTWZXVy0afW2cZwZ9cpufY3IL1R1Olf0xpRFP7EgAcbJ0-GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fefa4eec1c.mp4?token=b4DCIXFwCgivN13PDDPobLTVGSUJLbRU-PGU2ImFGb1bH9XRna5fIojlEGS5jSAWnzswJClApRoBBRYV9B2Rf-jmi1jzY6QSUXvD-bytyxomBDlrFvJDcKIy07XM_4ERvAjxenRc5S4zbE3lMriNP9tckpzmF4TeZn7u37HCs-U3zyYO0adKpcc4TuTO-bsYGlkTmhx6UlVIUI7Q26dTGmfWL18aQVxhFl4BhNBn5ELIol2kwp8ltTChYmdGS5dcfTEUcmdO7OicXOngv5HxYiYod_HULfwXWuj8ujJTWZXVy0afW2cZwZ9cpufY3IL1R1Olf0xpRFP7EgAcbJ0-GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سردار رادان به تهدیدهای ترامپ
🔹
رزمندگان بلدند زبان تهدید را چگونه پاسخ دهند، تا جایی که [دشمنان] مقابل ایران سر تعظیم خم کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/658503" target="_blank">📅 19:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658501">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
خروج قطار مسافربری تبریز ـ مشهد از ریل در میانه
🔹
قطار مسافربری تبریز ـ مشهد در محدوده ترکمنچای (اطراف جاده ورزقان) از ریل خارج شد.
🔹
در پی این حادثه، تیم‌های امدادی و عملیاتی هلال‌احمر میانه بلافاصله به محل اعزام شدند.
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/658501" target="_blank">📅 19:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658500">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/093d33fe81.mp4?token=JI8NteIh8o7w2FUjwtO72H2QiwnBWWRUdfcWtyLKfw6i3gf_fsIwrZX-Mvn9-j5C_zux0k8LWzfmmAEoCtzMxUQFmeiK87Q2cu-twDRTt22Bb9d6KW2nuEPeX-lylHj7t_Y98hK334HWTPer3Y5GUhsmFE_lA60W8CMQySegNXiVXF-PX2SEC_plETDElBHyATLJI8ZofRoFC_f577DgEEKcMfFrBbskTrQe74v8e_6L75WATx46mmimr-IO1hecegP_rPSIawG5rGA6pqQlhxizFfxGb1x41DwNjkBxaYPGcmDwo-hik1T1Z-o8fqcMRqRVJX5FWwsnxxH-IInMpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/093d33fe81.mp4?token=JI8NteIh8o7w2FUjwtO72H2QiwnBWWRUdfcWtyLKfw6i3gf_fsIwrZX-Mvn9-j5C_zux0k8LWzfmmAEoCtzMxUQFmeiK87Q2cu-twDRTt22Bb9d6KW2nuEPeX-lylHj7t_Y98hK334HWTPer3Y5GUhsmFE_lA60W8CMQySegNXiVXF-PX2SEC_plETDElBHyATLJI8ZofRoFC_f577DgEEKcMfFrBbskTrQe74v8e_6L75WATx46mmimr-IO1hecegP_rPSIawG5rGA6pqQlhxizFfxGb1x41DwNjkBxaYPGcmDwo-hik1T1Z-o8fqcMRqRVJX5FWwsnxxH-IInMpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای مرد آزاده راهت ادامه خواهد داشت و قاتلینت به سزای اعمالشان خواهند رسید...
#WillPayThePrice
‎
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/658500" target="_blank">📅 19:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658499">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aebd782004.mp4?token=js8T2aUQ7ihMx2sLJDyQ9vhrFpffUFDuNYs1wucBJVSsO7WggBSzZONSKdsxjMYgRo77Z7YkO20cdsJ0CDSM4MA4_5r_4xUPjzHfK4nGiqmv27cCzi-UzvBXaffUzhrFwU-ExAz697rMujnD98gx53O8FTW0BULxEU_z3qh0oFjcbYf9xuNvuT3TbrgoQ3-RSPT5T7fSzNJrwzRIoxymRVRGHqWjwLIj2W6piSSmNvoUDLxUvZij8BvyuZCNOIKJoX-olOmK5DpSFUWDJ1Oj-PwM1WjrEdLEH30Gfa_L6REe_NfhWYXE7hVKYjyD-IIj93sT6AMwQl0V122hye8ZSMAk-IeO7R-IcmDn59Pxo0Ez6PiBJ6OT9GsGrd_my4ck5Og-aL-fOKunmCbeq6ZPwoOd-1hyrkvF9_Fe2CBIrJ5iUGwuFCniuwfwm9XKLPIa-T3lA_6rMlOZLyT6jYP-jCF5hBiQKs6YEi7SOFjiC5gnU8DDFswa35WTcqe0XGltR3YI9eaBQa_bDimRzJOV12BOPI4ZBTG0OZI-aATDeHEMzALrYa38XJTH-ZtnbxZzDjTmImMtZFfzy9wqD-Xd482TDVWNFPgtnKp0taXwP6XiO1nWN6dMmRQJ-p60xVXJcebJh5Ax5i7CzLNJtzo7xyLPAAAu0SNjkGIdmjvIPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aebd782004.mp4?token=js8T2aUQ7ihMx2sLJDyQ9vhrFpffUFDuNYs1wucBJVSsO7WggBSzZONSKdsxjMYgRo77Z7YkO20cdsJ0CDSM4MA4_5r_4xUPjzHfK4nGiqmv27cCzi-UzvBXaffUzhrFwU-ExAz697rMujnD98gx53O8FTW0BULxEU_z3qh0oFjcbYf9xuNvuT3TbrgoQ3-RSPT5T7fSzNJrwzRIoxymRVRGHqWjwLIj2W6piSSmNvoUDLxUvZij8BvyuZCNOIKJoX-olOmK5DpSFUWDJ1Oj-PwM1WjrEdLEH30Gfa_L6REe_NfhWYXE7hVKYjyD-IIj93sT6AMwQl0V122hye8ZSMAk-IeO7R-IcmDn59Pxo0Ez6PiBJ6OT9GsGrd_my4ck5Og-aL-fOKunmCbeq6ZPwoOd-1hyrkvF9_Fe2CBIrJ5iUGwuFCniuwfwm9XKLPIa-T3lA_6rMlOZLyT6jYP-jCF5hBiQKs6YEi7SOFjiC5gnU8DDFswa35WTcqe0XGltR3YI9eaBQa_bDimRzJOV12BOPI4ZBTG0OZI-aATDeHEMzALrYa38XJTH-ZtnbxZzDjTmImMtZFfzy9wqD-Xd482TDVWNFPgtnKp0taXwP6XiO1nWN6dMmRQJ-p60xVXJcebJh5Ax5i7CzLNJtzo7xyLPAAAu0SNjkGIdmjvIPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از خوشحالی یک الاغ پس از دیدن صاحبش بعد از مدت‌ها در لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/658499" target="_blank">📅 19:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658497">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gewL4GgfGBbXbaW8UNUed7c-aKPGth0GWSC4XfUjWPIi6xpqIjr2xLELHcHI4qS0iKfZqUbKYcXHaJ2A0LrNPoaCLcaWtrcXSclkduOFsoUL1Vf87T6Xwdiv4oG7DBiBCmWrIbIAR6j6YGYe_f9TDerG17XNSMLq4LPeAnQlE3I7yc5ZLMWU45HdqfZA4gbF_0C80H_oxXZ2VALFFDxNDPokp4GKVVWVRzDXJRqIRMLcDS28yGH_w5mir9PGuMZZN4XqCo0-iOyQTbxzZBKf7k8C3tXLxHb_LZJv9x-sQ9fdWqPvbZUmyY96o05lVS_KrpSKSacfEAxjteVGxd_x8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس مجلس: ایرانی متفاوت خواهید دید!
قالیباف:
استراتژی‌های اشتباه و تصمیمات بدون فکر، صحنه بازی را به شکلی فاجعه‌بار به نقطه صفر برمی‌گرداند؛ زیرساخت‌های انرژی و بازارها را به انفجار می‌کشاند و مردابی بی‌پایان پدید می‌آورد که سال‌ها در آن گرفتار خواهید شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/658497" target="_blank">📅 19:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658495">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای الحدث: نشست قریب‌الوقوع کشورهای میانجی‌گر واشنگتن و تهران
الحدث:
🔹
پاکستان، قطر، عربستان سعودی، مصر و ترکیه برای ارزیابی تلاش‌های میانجی‌گری تشکیل جلسه می‌دهند.
🔹
نشست پنج‌جانبه به دنبال یافتن تضمین‌هایی برای اجرای توافق بین آمریکا و ایران است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/658495" target="_blank">📅 18:54 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
