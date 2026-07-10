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
<img src="https://cdn4.telesco.pe/file/H4bqKjD4rdv_c84_ZlYevoNSNt5Fbx56UKNzSnNDexAwB1uzk08dXaCerJV5s8WXWYgntjm-lSDZga0IL0uM88ref8ablTkhJ5niu3LgjILmiPhWJma3IlZW1JdByzkdoLOiLWjxuFnTqkmHlkP6djCOtkRxZqMJ6aeQZqRcX4KiVexo6tSTJtjj9sXtGcNm8O0RpXt5vWT3oImsjpRGxbI2Pg47vP5yEQ64ax_UGtGcHvej7wqs3q3GevQ5Mt1jli29MSBRZbOooOIJ4UWWLV-oUj7WJO1kv-MwgXX_xOfFuDljjiFnzQfAA0Zvirb8rGilM5VpxPpqqHc9D78tOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 361K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 13:54:21</div>
<hr>

<div class="tg-post" id="msg-17262">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بابک زنجانی: در خصوص (راه آهن) آق قلا حرف و حدیث‌هایی از خرابکاری به جای حمله دشمن البته وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/17262" target="_blank">📅 13:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17261">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/withyashar/17261" target="_blank">📅 13:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17260">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اتاق جنگ با یاشار : عمو اگه امتحان دار‌ی خواهش میکنم درست رو بخون
🙌🏾
این خودش ضد خواسته رژیمه اونا میخوان تو بیسواد باشی ، این خودش گارد جاویدان بودنه ، ترس رو تو وجودت راه نده سنگر رو نگهدار ، ترمیناتور باش مثل شیررررر باش نسل بعدی ما نباید روح و روان خراب…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/withyashar/17260" target="_blank">📅 13:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17259">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">زیرنویس شبکه خبر: ازمون های نهایی بدون تغییر و طبق برنامه ابلاغی از 21 تیر شروع میشه @withyashar</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/withyashar/17259" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17258">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یکی از کشته های تیراندازی در مشهد
🚨
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/withyashar/17258" target="_blank">📅 13:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17257">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اسرائیل‌هیوم گزارش داد آمریکا، اسرائیل و برخی کشورهای منطقه در حال بررسی گزینه‌های سرنگونی جمهوری اسلامی هستن
و ازسرگیری هرچه سریع‌تر محاصره اقتصادی ایران رو یکی از راه‌های رسیدن به این هدف می‌دانند
یکی از مقام‌هایی که اسرائیل‌هیوم اونو آگاه از تحولات داخلی ایران معرفی کرده، گفته اختلافات داخلی در جمهوری اسلامی تشدید شده و سپاه ممکنه کنترل رهبری غیرنظامی رو در دست بگیرد
@withyashar</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/17257" target="_blank">📅 13:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17256">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نیویرک تایمز : محدودیت‌های تصاویر ماهواره‌ای ایالات متحده، روزنامه‌نگاران را در پوشش جنگ ایران با مشکل مواجه کرده است. اما منابع دیگر راه‌حل‌هایی ارائه می‌دهند که پنهان کردن اقدامات ارتش‌ها را دشوارتر می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/17256" target="_blank">📅 13:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17255">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بلومبرگ: روسیه به دلیل فروش نفت در جریان جنگ ایران، کسری بودجه نادر خود را جبران کرد
پس از امضای تفاهم‌نامه بین ایران و آمریکا قیمت نفت خام روسیه از ۸۶.۵۲ دلار در ماه مه به ۶۳.۵۲ دلار در هر بشکه کاهش یافت
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/17255" target="_blank">📅 12:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17254">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTFSE8OAO1GZD_6CFrFBXdoOW9UMMQmglaooR6YXOipPBdimZuzCJqCy4pcfT-9kAdlV9-fmdGNrSRVTdNJJnYc-JgAI-7KteAhF7cmqrX2Nyqv30wrE7Jx8IKIN-W4i5e8yLgXePa8CYFhxzFsa7Le2srDj29ApEUmDfdqSpbj4NPhOAhG6ITaJJarqTuhtB5mzjpUM3jazlKNPHqIFXgjbjH8GahiMerl8K_AWDD-3qtBTIrySw4_YCm9auj-Cu56m-S4WLh8zcrjhAtnWLA_7Z1tCz7yt-_xDpZEawcCGj7jwJpA4DgQIFSZnTqDWUYu-hiI-HMC1g11hcVb-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر: ازمون های نهایی بدون تغییر و طبق برنامه ابلاغی از 21 تیر شروع میشه
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/17254" target="_blank">📅 12:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17253">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سیتی ژورنال: وزارت خارجه آمریکا جلوی دیدار مقام ارشد تیم زهران ممدانی با سفیر ایران در سازمان ملل را گرفت
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/17253" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17252">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترکیه برای دریافت جنگنده F35 آمریکا، پدافند های S400 روسی خود را فروخت منابع ترکیه‌ای مدعی هستند که ترکیه سامانه‌های دفاع هوایی اس۴۰۰ ساخت روسیه را به یک کشور ثالث فروخته است و نام کشور امروز اعلام خواهد شد. پیشتر آمریکا به عنوان شرط فروش F35 به ترکیه اعلام…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/17252" target="_blank">📅 12:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17251">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز: جنگ ایران، جهان را تا آستانه یک بحران غذایی پیش برد
درگیری بعدی در خلیج فارس نیز می‌تواند همین پیامد را داشته باشد.
کشاورزی مدرن به کودهای شیمیایی ارزان‌ قیمت وابسته است. این جنگ با گرفتار شدن کشتی‌ها، تعطیلی کارخانه‌های تولید کود، هراس کشاورزان و افزایش شدید بهای کودهای شیمیایی، تولید جهانی غذا را در معرض خطری جدی قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/17251" target="_blank">📅 11:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17250">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مسئول آمریکایی: واشنگتن عمداً حملات متناوب را انجام می‌دهد و سپس متوقف می‌شود تا از تشدید تنش‌ها جلوگیری کند و فرصتی برای دیپلماسی فراهم شود.
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/17250" target="_blank">📅 11:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17249">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ_igjkJp6UfhXMgjllDXBMvAj-tLvRkqGALozVzOaBOwybYhwTjTegZVnBJ0_CltwqpqPg3Ibm_feufjQszyqA3ix8wDxk8zZZjQD8N4pN2TtRxtQdTd8zjcZT_V4TlI0HaQVinprLIE7QoQRjEeFApt4xyZcsEwhoIHqcWadkS_1BxnoBoEgzZheVMZhB3IpsvA-pdQmz6LWx-KWxY88BdqlM_F9xTOeCLkRKO8YpeKw77Ur3O6hLuqe9J97lAm60TRqarCjr65k_-Dq2gNUodzPo_VfMcteiPpYxpf3hT9yooC6oWuaT61DRzypkwPU-k5eo2gWODModRo-Ep6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه اردوغان به سران کشورهای ناتو که در اجلاس آنکارا شرکت کرده بودند.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/17249" target="_blank">📅 11:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17248">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یاشار : خیلی از‌ اخبار که امروز پخش میشه من دیشب پست کردم
🤒
قبل فرستادن خبر‌ در ‌دایرکت چنل رو کامل اسکرول کنید و ببینید
😩
❤️‍🩹</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/17248" target="_blank">📅 11:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17247">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkXBJTon6Cd9X8CIwNze049INk-enKvrbq-QVD_GohQjW-gxWn5nJqPArRdwtFAp-Vd60o7PcYF1o1d7KatJgKcwm7fx7q62op9sPNII0nnWQIRiSKGDZCXUNzwLZGCP2S9Ksik3gnN5IkROeB_n9V9xJsRQzy996aDPAKG4RPmmkYMAM0KcE-_T35rKPLS5tXe6AxUog87spzUAnTy6Ezu8QfXsmkcGbVg_tqA87IOGr-D_LIZZrG1tuQyR_WUGHGYlXy2eDJ8mqPZOsOyhQe1ey-EpMudIv02DV9u5rew3hjmfYQNWEBxCpxEINpL9pO9NXDFtIivlqK9donoVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ اسرائیل: ایران با جذب شهروندان و اتباع خارجی، اطلاعات و تصاویر مراکز حساس از جمله اطراف وزارت جنگ و مجموعه نظامی‌«کریا» را جمع‌آوری کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/17247" target="_blank">📅 11:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17246">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwraGLRofR68gvSatYyiycctgLiGHXsI3KIUAEZkTRmIsqqWiKU79xxcFJ8kAAVnwsYvsedMwGPFI5KRFrppvJ4py7BHqWv89S2htiUwqkSO3LFAVKKu_AJlQ8U2yM6qb_ZAHpGMZ1ix2YwuqnCjYnf758b420q8Bl40nZERPYM9jQ08kJzsxph61MZUfkmo36CAqtUGZD3vkuLDfZb_lGEa6DgW5kQ4aGhFsnd0KjOjymAF0CA4u8W8ZfNHfSvZ5Ua-zWibbmiEXk7pLnGXoz2skMrroW4PtvnZaACTNRBB51GBj3TdOk2D-XBLwMceMMSnLxlFuUlLby_eEikUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه برای دریافت جنگنده F35 آمریکا، پدافند های S400 روسی خود را فروخت
منابع ترکیه‌ای مدعی هستند که ترکیه سامانه‌های دفاع هوایی اس۴۰۰ ساخت روسیه را به یک کشور ثالث فروخته است و نام کشور امروز اعلام خواهد شد.
پیشتر آمریکا به عنوان شرط فروش F35 به ترکیه اعلام کرده بود که برای خرید F35 باید سامانه های پدافندی S400 روسی را نداشته باشد
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/17246" target="_blank">📅 11:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17245">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شبکه اسرائیلی کان: اسرائیل میخواد به ایران حمله کنه اما منتظر چراغ سبز ترامپه. مقامات در اورشلیم برآورد می‌کنن حملات متقابل میان آمریکا و جمهوری اسلامی در چند روز آینده ادامه پیدا کنه.
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/17245" target="_blank">📅 11:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17244">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">احمد وحیدی، فرمانده کل سپاه پاسداران، در پیامی به مناسبت خاکسپاری علی خامنه‌ای رهبر پیشین جمهوری اسلامی نوشت خونخواهی علی خامنه‌ای و مجازات عاملان و آمران آن، مطالبه‌ای «قطعی، مشروع و فراموش‌نشدنی» خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/17244" target="_blank">📅 11:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17243">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ در ‌تروث: امروز روز بسیار مهمی در پالم بیچ، فلوریدا بود، و افتخار بزرگی برای من بود که فرودگاه بین‌المللی پالم بیچ، با رأی قاطع، به نام "فرودگاه بین‌المللی دونالد جی. ترامپ" تغییر نام داد. به زودی این یکی از بزرگترین و باشکوه‌ترین فرودگاه‌های جهان خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/17243" target="_blank">📅 10:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17242">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک مقام آمریکایی: ناو هواپیمابر آبراهام لینکلن در دریای عرب در حالت آماده‌باش کامل قرار گرفته؛ واشنگتن تأکید کرد در صورت لزوم، حملات از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/17242" target="_blank">📅 10:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17241">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الجزیره: تردد کشتیرانی در هرمز به دلیل ازسرگیری درگیری‌های آمریکا و ایران متوقف شده
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/17241" target="_blank">📅 10:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17240">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اکسیوس : ایران و امریکا دوباره باهم توافق کردن که همدیگه رو نزنن و فعلا دست نگه دارن.
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/17240" target="_blank">📅 10:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17239">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">lسی‌ان‌ان به نقل از مقامات آمریکایی ادعا کرد: در صورت نیاز
،همکنون مقدمات حمله به ایران در حال انجام است، اما تمرکز در حال حاضر بر دیپلماسی است.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/17239" target="_blank">📅 10:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17238">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وال استریت ژورنال : ایران قصد داشته تو ترکیه، ترامپ ترور کنه که نتانیاهو میفهمه و سریع اطلاع میده
همین باعث میشه ترامپ عصبی بشه و تنش ها شکل بگیره
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/17238" target="_blank">📅 10:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17237">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرنگار فاکس نیوز: یک مقام آمریکایی به من گفت مذاکرات با ایران در هفته پیش رو ادامه خواهدیافت
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/17237" target="_blank">📅 10:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17236">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اکسیوس: ترامپ روز پنجشنبه بعدازظهر با تیم ارشد امنیت ملی خود درباره تنش‌ها با ایران و مسیر پیش‌رو جلسه برگزار کرد
پس از این جلسه، یک مقام آمریکایی گفت دولت ترامپ «همچنان متعهد به یافتن یک راه‌حل است و مذاکرات در سطح فنی برای رسیدن به یک توافق هسته‌ای ادامه دارد.»
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/17236" target="_blank">📅 10:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17235">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpmv2l3MsPQiAQ7kyz5XyQ5vH6b3ctSaSZfIfUIRdoZa7IwNgdQy1FUUCfRKammtHyo2ZjSYHHx1ei0BbdM_vPGLzx9q9yCYvwehZ41I4FBHNfTpSQqt750NoLxmg8ZoEU3aN29jZUwx1jhuLZLPBd_TICyNTZUstz3tWbCDZDisfSpC-skpb5kXssItgykyVEc0QJ_MBLvSfMpwjKCtcuuPwQai6EDl2GKohc05zrCS45Uq7TLacM2TGRaIkKVoUmjWr2CmchfSYpH9o0h_r1erLLJowA8NhONRslrIzECUEMh10Zkxehs6l4ux_NmDoS_tpl1ftts9RcGd-bB9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سوشی را مجانی میکنیم حتی برای طبقه‌ی سامورایی ها.
@withyashar
🍱</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17235" target="_blank">📅 04:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17234">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75f4d1ccf4.mp4?token=PQwggdAog1XATj4oHgP7qjrZAr0ZNaC0HpUpz3YVK2jhpEvf0NSSENyEcvuCI7cw9iRxr1nZXw5zRLfmv9kfserEzaVHHEO8nN6pypbpH5v_UlWynh6oHtXFLWL5eXuRh0TV1Id1luHfoXrcldLtxMmqogtAjb24IfJY8NYMtkxFYee6H1NRiUhzSmx8B0eehU4-cUF9IvmTbmchcnJCplJg8pbqCn0Z3-Pe4joy4oKuECJ5QeEjvyRd0hug3_TMQ_4TUZJ4RlkKiP69FYNsrT9NNbcpQsMIV9Awtrv8lO66Qp2FgImkfnzxVY9dJAKFvND9b1rFBg7LKAuJ0GhkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75f4d1ccf4.mp4?token=PQwggdAog1XATj4oHgP7qjrZAr0ZNaC0HpUpz3YVK2jhpEvf0NSSENyEcvuCI7cw9iRxr1nZXw5zRLfmv9kfserEzaVHHEO8nN6pypbpH5v_UlWynh6oHtXFLWL5eXuRh0TV1Id1luHfoXrcldLtxMmqogtAjb24IfJY8NYMtkxFYee6H1NRiUhzSmx8B0eehU4-cUF9IvmTbmchcnJCplJg8pbqCn0Z3-Pe4joy4oKuECJ5QeEjvyRd0hug3_TMQ_4TUZJ4RlkKiP69FYNsrT9NNbcpQsMIV9Awtrv8lO66Qp2FgImkfnzxVY9dJAKFvND9b1rFBg7LKAuJ0GhkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا رأس ساعت ۳ صبح هم زمان با مشاهده این پهپاد در سمت غرب تهران و کرج، صدای جنگنده هم بسیار گزارش شد. که ممکنه به هم ربط داشته باشند و جنگنده به دنبال پهپاد آمده باشد
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17234" target="_blank">📅 03:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17233">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یک مقام امریکایی در گفتگو با آکسیوس:
حملات اخیر ایران به کشتی‌های تجاری در تنگه هرمز، توسط گروه‌هایی در داخل ایران صورت گرفته است که با تفاهم نامه شدیدا مخالفت دارند و قصد دارند آن را تضعیف کنند
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17233" target="_blank">📅 03:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17232">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بر اساس گزارش نشریه "اکسیوس"، یک مقام آمریکایی اعلام کرد که عدم انجام حملات جدید توسط ارتش آمریکا به ایران در امروز ، نتیجه تلاش‌های منطقه‌ای برای کاهش تنش‌ها بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/17232" target="_blank">📅 02:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17231">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/17231" target="_blank">📅 02:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17230">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وال‌استریت ژورنال: اسرائیل اخیراً اطلاعات جدیدی را با ایالات متحده به اشتراک گذاشت که به گفته این کشور، نشان‌دهنده یک طرح جدید سپاه برای ترور رئیس‌جمهور ترامپ است.
ترامپ روز چهارشنبه، در سخنرانی خود در اجلاس ناتو در آنکارا، ترکیه، به تهدیدهای ایران علیه جان خود اشاره کرد و گفت: «آنها می‌خواهند رهبر آمریکا—من—را از بین ببرند... من در تمام لیست‌های آنها هستم.
@withyashar</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/17230" target="_blank">📅 01:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17229">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حکومت رمال ها  ، بت لگویی ترامپ را آتش زد !
@withyashar</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17229" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17228">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">باقیمانده خامنه ای دفن شد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/17228" target="_blank">📅 01:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17227">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnOzVf5fzuxkEreKA2Kd98JkxclDCulnCWApFu6_44oG-MbmnRHBW8KgpfyzrPv51G-lnAgB8I4B3O_vOkJQeEFq-uzeVK2EAZHBA3XU0gepPOm2XisRruZQmLLehQSnsR12uG_SwEzLvef2FrAEKN0_y_LXnFW3K46WQH25xuM1_Ps3-ewyKwhaxf6utbx3wdzK21Bcm1wAzFy7aI699xUMi0id_yS9AjaPdX5ijW7WBny_K26Vu5Ji9rIftsclQJ4gCpbo6aMqRiR21QQUMz0ga2nJkj8krY3FsUf0U2TYefiq1CfXb8lCp5UvYcgK86IezG-asD4kknQVw-qqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب اتاق جنگ
⚠️
این عکس هم هوش مصنوعی است !
@withyashar</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/17227" target="_blank">📅 01:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17226">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حقیقت یاب اتاق جنگ
⚠️
این عکس هوش مصنوعی است !
@withyashar</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/17226" target="_blank">📅 01:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17224">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بیانیه جدید سنتکام:
ادعا: رسانه‌های دولتی ایران مدعی هستند که عبور و مرور از تنگه هرمز فقط از مسیرهایی مجاز است که ایران تعیین کرده است.
واقعیت: ایران کنترل تنگه هرمز را در اختیار ندارد. از اوایل ماه مه، نیروهای ایالات متحده به عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از این گذرگاه حیاتی تجارت بین‌المللی کمک کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/17224" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17223">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6EaISfVcBgH8L0T5Etxe3rTDt-2EnxTD_468amIid34wfWES2af5A2t0BB3LVzqgTHmXr_R3ik8sf_0IRA1D91VVtGcpDcMYhDPOV5oyqMAvWaTcisSsIKTxx9RSIqK91FWNssDIHwC_oFASyi9ZNCjC6B4rrPCiprkyBNEmjYxi0O_FOCm6FWcSp6L9APfYjBBqO7UaDIneZOrX1mCbozDWWHxMz7-k39r2EvsQ4H-BFYmEuFsKhx941Ffv0E_X1FMxqm-2l5PyBnUp64ypVg4r9PHHcgbA3Lyi_7hlRvTqSmDGTqiEnxh5wFxm7s_JnfTKrNeyoYd9UTNqjQNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای آواکس به همراه ۱۰ سوخترسان  ، فقط نشونه اینه که منتظر تایید نهایی هستند… یک جرقه
💥
@withyashar</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/17223" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17222">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اومدن گلگی کنم گیفت و استار نمیاد دیدم نه بعضی ها هستن که روحیه بدم بهم هنوز
🙌🏾
دمتون گرم حواسم هست بهتون روز آزادی پیغام میدم تک تکتون جمع میشیم
😭
❤️‍🩹
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/17222" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17221">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شرحه واقعه از یک شاهد بیار‌ عرزشی :
شهیدان علوی و هنرور به ضارب مشکوک میشوند که او هم با لباس بسیجی بوده و قصد انجام یک ترور را داشته است، بعد از نزدیک شدن به تروریست دست به اسلحه می‌برد و به سمت شهدا شلیک می‌کند و به سرعت از محل متواری میشود
@withyashar</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/17221" target="_blank">📅 00:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17219">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به گزارش رسانه های‌ رژیم:
بر اساس اطلاعات، دو فرد ناشناس با لباس نظامی‌و با استفاده از اسلحه کمری، شماری از بسیجیان را مورد هدف قرار دادند که طی این اقدام، یکی از بسیجیان در صحنه و دیگری در بیمارستان به هلاکت رسید
ضاربین متواری هستند تلاش نیروهای امنیتی برای شناسایی و دستگیری عوامل این اقدام ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/17219" target="_blank">📅 00:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17218">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارشها ۸-۱۰ نفر در‌ تیر اندازی های مشهد کشته شدند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/17218" target="_blank">📅 00:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17216">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یکی از کشته های تیراندازی در مشهد
🚨
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/17216" target="_blank">📅 00:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17215">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دیدبان اتاق جنگ : من دور حرمم نیرو های بسیج و سپاهی دارن خیابونارو ول میکنن میرن با موتور سرعتشونم زیاده
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/17215" target="_blank">📅 00:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17214">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مشهد - ایست‌بازرسی منطقه سرفرازان  توسط افراد ناشناس به رگبار بسته شد
یک درگیری مسلحانه در اطراف حرم امام رضا.... و دومی افرادی که امشب به ایست بازرسی مشهد حمله کردن لباس نظامی به تن داشتند و بعد از زدن نیروهای امنیتی فرار کردن.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/17214" target="_blank">📅 00:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17213">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlP1ZugjZkpbQYxOKpgrPaurEvG4n6Stzmem0wVIXEZaXIk9vP_HEPepYJ4aCOrn8JXqTNSLBGDBYmp3bbRNGQ5ncQkYahihTt2-M2CIV8qeqyO7YttjpoxCv2qBg6FWFO_X1yuzIdOCwQwnzyhCbJBHzdostCBI101D2PvzQ4GzkoTwfgJctZExwPmp-jOmEt4QCGAzk_uMNigpuheDxC8qZkFFMmPCMyIFEP3boB_BajIuxyRuL7a3k5qIVTEdaBBvp_kvsIhbGy7JYgyPr1a5Z7GR644C0GaX6mhzCE5jKMLVHLnHik0w0YLtuYFKYiOkcdp-Ad3vH8belQsqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کشته های تیراندازی در مشهد
🚨
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/17213" target="_blank">📅 00:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17212">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGfHD2Pg-XZ8OW7PCzkyUBIT_NJAbhFWjsFQhaOH9GSkiYIMfP3HKfUo0EDtuWWBoBvyYmZoEVrg5DsfaY6Jay3XH3c424hY81ICearJePpjc3zSp8HXfvnXMuAkFvTE-2cv-sSPJLPjSRWNb54-Kj8ctPXY0SUqD3ZyyuzcyPsrqVWpaEkqXE1tUsVR0d8PfOoU68-w7Wl6_urJwfGNag5RJnTvSVxLy6DwEDesYKPP9-tpz2mVwubVTxxIoyKmKS_bhCxZ2SDqdN_NsSRTu00EwDJhxcjr2NE3qH5Lzovk-ZJzMdYnh13D6h76dELdHAB2Iixy7YKy2WPSX73KQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری در ‌مشهد از حجازی از چهره های مخوف علی خامنه ای در کنار ممباقر ، بیگلی بیگلی هم او پشته
@withyashar
🤣</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/17212" target="_blank">📅 00:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17211">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارشاتی از حمله به یک ایست بازرسی در مشهد
@withyashar</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/17211" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17210">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رسانه های عربی: یک فرد مسلح به سمت اعضای سپاه پاسداران آتش گشود.
@withyashar</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/17210" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17209">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آی۲۴ عبری:  عربستان سعودی در تلاش است تا اسرائیل را از پروژه کریدور اقتصادی هند -خاورمیانه-اروپا (IMEC) کنار گذاشته و مسیر آن را به سمت سوریه و ترکیه تغییر دهد
@withyashar</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/17209" target="_blank">📅 00:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17208">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزیر عمور خارجه ترکیه
فیدان: با آقای عراقچی صحبت کردم و ایشان نیز با من موافق بودند که آتش‌بس هنوز به پایان نرسیده است
@withyashar</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/17208" target="_blank">📅 00:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17207">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSadeq</strong></div>
<div class="tg-text">پهپاد هم داره میچرخه توی آسمون
مشهد</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/17207" target="_blank">📅 00:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17206">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommaryam</strong></div>
<div class="tg-text">از وکیل اباد هم شنیده شد</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/17206" target="_blank">📅 00:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17205">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐦𝐢𝐫𝐬𝐚𝐥𝐚𝐫</strong></div>
<div class="tg-text">یاشار منم مشهدم، صدای تیراندازی از سمت میدون پارک‌ملت میومد</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/17205" target="_blank">📅 00:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17204">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش تایید نشده ((تیر اندازی در مشهد))
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/17204" target="_blank">📅 23:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17203">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فرماندار شهر کنارک : یک پایگاه نظامی متعلق به نیروی دریایی، در دو مرحله مورد حملات هوایی دشمن قرار گرفت. @withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/17203" target="_blank">📅 23:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17202">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb4117500.mp4?token=IuLqk6BM3-eCsBQb7W1DLqH7xS3p1-XTfSpTWtkQ7fksEvFYMsbLuksV0du5DEi2i5NLSDci1Dp93k2H4oTGQIi8MM9RhZovnOEwFIbMr0Jlq1HSqHILo5ZndvzlmdhTmLIcDMiv5y3XgBjtXm57slGTBYQN4wAtbBdga_VWMFBoTjhiBkypiyPdPEnl5GAaKzp347Kyp2cxAQQBtD9TprmPbSJSa63gulOf0LfowU6WY_sxz-SDV-9NcBxc8sfQu8yyoEEemWcqlZNXq1hNMka3fQ1WrVfIaFyfLU-T3qdhH9g-bgKbcIBBkX_a5yWwCt879kR65TNN0u64SsAAlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb4117500.mp4?token=IuLqk6BM3-eCsBQb7W1DLqH7xS3p1-XTfSpTWtkQ7fksEvFYMsbLuksV0du5DEi2i5NLSDci1Dp93k2H4oTGQIi8MM9RhZovnOEwFIbMr0Jlq1HSqHILo5ZndvzlmdhTmLIcDMiv5y3XgBjtXm57slGTBYQN4wAtbBdga_VWMFBoTjhiBkypiyPdPEnl5GAaKzp347Kyp2cxAQQBtD9TprmPbSJSa63gulOf0LfowU6WY_sxz-SDV-9NcBxc8sfQu8yyoEEemWcqlZNXq1hNMka3fQ1WrVfIaFyfLU-T3qdhH9g-bgKbcIBBkX_a5yWwCt879kR65TNN0u64SsAAlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مراسم تشییع جنازه امشب یکی داشت علیه مذاکره کننده ها شعار میداد که یهو یک نفر که احتمال زیاد نیرو امنیتی بود ، جلوی دهن طرف گرفت
@withyashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/17202" target="_blank">📅 23:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17201">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فرماندار شهر کنارک : یک پایگاه نظامی متعلق به نیروی دریایی، در دو مرحله مورد حملات هوایی دشمن قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17201" target="_blank">📅 23:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17200">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل : نتانیاهو و ترامپ گفتگو کردند ، رئیس‌جمهور آمریکا از تحولات آمریکا در خلیج فارس اطلاع داد.
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17200" target="_blank">📅 23:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17199">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ به اتاق جنگ گفت به عشق ماکرون و عینک قشنگش امشب اول فوتبال رو میبینیم و بعد خواهیم دید چه خواهد شد ، کلی اسپانسر داره جام جهانی پول دادن پول متوجه هستی ؟!صداشون در میاد ، ممد چی چی هم سر معدن داره مته میزنه بگو ول کنه بازی رو ببینه
😂
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17199" target="_blank">📅 23:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17198">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسانه عراقی تندرو شیعه : از دوستان خبرگزاری تسنیم خواهش می‌کنیم ما رو دنبال کنن و برای انتشار خبرها عجله نکنن. همون‌طور که قبلاً هم گفتیم، این حمله از خاک کویت انجام شده و با
پشتیبانی اطلاعاتی پایگاه آمریکایی الظهران در عربستان صورت گرفته.
@withyashar
یاشار : تسنیم رو دیس کرده و
ولی هر چی‌گفته آخرش رسیده به حرف‌ من
😂</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17198" target="_blank">📅 23:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17197">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfsTz8xNR9tWMBxepsX6K16halkBisuD9FsJjx-t0A1aettmKs6Rr07leUvmQHkC-sMNqjjKGXT1Kj1h9x1Wmwlbp5tKt0Fnv941ZTjMULSLmAUTsQDx31Avv2XY1Od7jeZrg-izlAH4LYReGuwaUKftOFX7zniThjARayvEGCr7RAfJNV72copdwr0mpLTcbWtIF-yUgOE0_gLrAION6WB0b4RBoaoggx2Xgc1OtDGPGgMqakmE7wUXnXU5YhUKIiyNhKE1KYekLcdtcWqoopGgIyyNyEx-4IQblvw0PE-MkbdEEor18tNK1_pN7efati631M5KSzWVvcNQlt2hlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رؤیت اتش سوزی در بندر عسلویه توسط ماهواره
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17197" target="_blank">📅 23:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17196">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7-g8X1cFq1sUEXbXd5eV7G1uBuBRomZErT6knoU_eW-Pc6OZ5NjYc8rN_BHK-YJ9XlxkrvreY6OBGjv56e3C9KLoPvJ7rDnrOMAtZAJItdhh769OGNw5092frTPjBFQLVz5HidH1kJ_mxqHvw3tBZvybO7RexeXDo5QxpqV0lGyjwM1fL-AVc4NhUCUQDzz4NvgB5zaGrMXQ6eFi_EHH1Ikc1sQWygR3wT1hyk4mJTAJavh7GRuF8M_cSiuPm0rB9agmFZFIVOE-PkZaeDMSQ25J5dQ3PLuz0-FBW9jTqw6DFTvpMctr-YeDTJOqLFd1tdNllVWMVMWVohmmYMzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیروز کریمی رفت جم تیوی
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17196" target="_blank">📅 23:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17195">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24e89d01f.mp4?token=ITV5KWmKb-eVElFUvHAUDgZou1zP06OJ7eCgRwJ1_Ehej9804FcadAEcuM8IYuPHEBicOOewlz0RG7jrdGrn0WwJTkdJiSPuiqNVkn2GeVRZXZ_qG9280CTcgxtxpbmOYdYXPWycLDjIfwX1kfkIuMcGk7VQXjRAZvYXVDSGBGbsP3Y_e5D1A2wRwdmq91CMzipA1j_2R6TNnevXerCUpfsdn-OseExcslw6wH-MqPG-85Jc2LiGgOWgqovhSvM-Jqge8LluQ1f4xAHgvy0YoN8cwmWQ3UEaXZEFpoSZaobC-jj-GhQ6-ARQaObtyAayHxUnECFtXZyXoawmHmWO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24e89d01f.mp4?token=ITV5KWmKb-eVElFUvHAUDgZou1zP06OJ7eCgRwJ1_Ehej9804FcadAEcuM8IYuPHEBicOOewlz0RG7jrdGrn0WwJTkdJiSPuiqNVkn2GeVRZXZ_qG9280CTcgxtxpbmOYdYXPWycLDjIfwX1kfkIuMcGk7VQXjRAZvYXVDSGBGbsP3Y_e5D1A2wRwdmq91CMzipA1j_2R6TNnevXerCUpfsdn-OseExcslw6wH-MqPG-85Jc2LiGgOWgqovhSvM-Jqge8LluQ1f4xAHgvy0YoN8cwmWQ3UEaXZEFpoSZaobC-jj-GhQ6-ARQaObtyAayHxUnECFtXZyXoawmHmWO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چغادک بوشهر بعد از حمله
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17195" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17194">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارش کانال ۱۴:
سپاه پاسداران استراتژی خود را در برابر ترامپ تغییر
داده و با تشدید تنش‌ها در تنگه هرمز، گارد انقلابی از رویارویی نظامی به یک کمپین رسانه‌ای علیه ترامپ و افکار عمومی آمریکایی در آستانه انتخابات میانی روی آورده است.
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17194" target="_blank">📅 23:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17193">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">معاون سیاسی و امنیتی استاندار بوشهر:
صدای انفجار شنیده شده لحظاتی پیش در شهر بوشهر متاثر از واکنش به موقع پدافند هوایی است.
واکنش به موقع پدافند هوایی مانع از اقدام عملی تجاوز هوایی پهپادهای آمریکا شد.
همچنین لحظاتی قبل یک مقر نظامی‌در حاشیه شهر بوشهر مورد تجاوز و اصابت پرتابه  آمریکایی- اسرائیلی قرار گرفت.
تاکنون گزارشی از تلفات انسانی متاثر از این اقدام دشمن دریافت نشده است‌
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17193" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17192">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرگزاری شین اسرائیل :
ترور هدفمندی که در اهواز رخ داد، علیرضا خدادادی، مشاور قراردادهای استانی سپاه ولی‌عصر در اهواز بود.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17192" target="_blank">📅 22:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17191">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانال ۱۱ عبری: کشورهای خلیج فارس (احتمالاً کویت و بحرین) یک عملیات مشترک نظامی محدود علیه ایران انجام داده‌اند.
بر اساس گزارش‌های شاهدان عینی، پرتاب موشک از خاک کویت مشاهده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17191" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17190">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صداوسیما
: امشب به بندرعباس، قشم، سیریک و جاسک حمله نشده و ما تکذیب میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17190" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17189">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIAwJo_XDIeVYNXadTLmtzyTYDnQWaRpVyBM9nFy1sUCi8_S7Gc4NnQBA3iZgYMCnP6vEF-du66GtapLnljMe4TdnpgP7SwJcz1BBFz72Ix00DJTmpHGp0jo_Qpi5AgSe6Bub19XowcNLqWPW3473oqhjjrc-85bbsHWa6V_w-kvtCt9rwBFRRIxKUZ-RlE-k6Q31G3ORLQUKosQVMbDOc-V1fL7aIeJPYJQ7S8Rq_5RZzX7Ph29WR_xEIVRYZK2nTkAU11mWA2wKooK8fq6XQhnZwIqJT5OTxdgP6coy_490Vp2iejbAlScrJCSsUmeKKn4eu4lXxYt-Ft6vqJpIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه ایران، عراقچی، تهران را به مقصد نامعلومی ترک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17189" target="_blank">📅 22:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17188">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تحلیلگران رژیم
: احتمالا حملات امشب کار کویت و بحرین است
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17188" target="_blank">📅 22:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17187">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">العربیه: ارتش ایالات متحده مسئول حملات اخیر در ایران نیست
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17187" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17186">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با یاشار : میپرسین بگم که ، نظر من اینه که هر کی هم بزنه بدون همکاری اطلعاتی و زیرساخت جنگی امریکا و اسرائیل و کسب اجازه امکان نداره بزنه… پس در نتیجه چه سوألیه
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17186" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17185">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کارشناسان تلگرام : گویا حملات از سمت کویت بوده
@withyashar
😁
🤒</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17185" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17184">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d6bd72f1.mp4?token=TcMAGY_3i2gus0WUuF9adZb6VMoVNd7-VG796WbRVsZu6J5cwJ_IJ1tBSE1l3xGuphApLVQnWDunNF1BsKvZHxH7tC8G9kSZb_PF4THjJrBN5t3nP7hB3LAH8KIom6h8uTYWsAvOUnaEdx9XjhupXBdz2X0yLM0lFrfMZY5ecmR2tUNzOQfMB7GX3v2s6Y6McMD2J30Xdx89UOgGpQQGxkXC0QJrx9YycBrSYcL079K-X8_i-n9q92VIUCdrFL7lWwXjIw9z8fKQlLD2sbSB_HvJyAc91M-AEkphid5aXRzJw9ChpfpBJD97ZQFGw3h8rqSFX56rYj0-AW2C51jrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d6bd72f1.mp4?token=TcMAGY_3i2gus0WUuF9adZb6VMoVNd7-VG796WbRVsZu6J5cwJ_IJ1tBSE1l3xGuphApLVQnWDunNF1BsKvZHxH7tC8G9kSZb_PF4THjJrBN5t3nP7hB3LAH8KIom6h8uTYWsAvOUnaEdx9XjhupXBdz2X0yLM0lFrfMZY5ecmR2tUNzOQfMB7GX3v2s6Y6McMD2J30Xdx89UOgGpQQGxkXC0QJrx9YycBrSYcL079K-X8_i-n9q92VIUCdrFL7lWwXjIw9z8fKQlLD2sbSB_HvJyAc91M-AEkphid5aXRzJw9ChpfpBJD97ZQFGw3h8rqSFX56rYj0-AW2C51jrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهده لگو غول‌آسای ترامپ در مشهد/ هنوز مشخص نیست این مجسمه با چه هدفی ساخته شده است
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17184" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17183">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اکسیوس: یک مقام ارشد آمریکایی ادعا کرده است که ارتش ایالات متحده در ساعات اخیر حمله‌ای را در ایران انجام نداده است!
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17183" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17182">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آتش‌نشانی اهواز : انفجار ناشی از نشت گاز شهری در یک ساختمان مسکونی دوطبقه در منطقه حصیرآباد اهواز است @withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17182" target="_blank">📅 22:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17181">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در‌کیش‌فقط صدای جنگنده شنیده میشود ولی هیچ خبری‌ نیست</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17181" target="_blank">📅 22:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17180">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">من هیچ گزارشی از قشم ، کیش و ابوموسی ندارم. نمی‌دونم چرا همه جا دارن این خبر رو میزنن. حتما اشتباهه.</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17180" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17179">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش انفجار ‌جدید بندر عباس @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17179" target="_blank">📅 22:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17178">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صدای انفجار‌ جدید اهواززز
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17178" target="_blank">📅 22:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17177">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شنیده شدن صدای ۲ انفجار در بوشهر و چغادک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17177" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17176">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش انفجار ‌جدید بندر عباس
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17176" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17175">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulH4ltvLf5i7QFrbKRbADnr35puY4_wuI60XvssmO1XmkE3c7gpcnMdNUcUx1H1qX73exq8EeybmIiUwEohJBbVZ-ITqR-NHSAb2ZXVgUqX9R2JKwT7CrPm8xqpGjaIglYMG9eqetQAJ3hyb1NqFl2JVzqEpBpVWX52vkXD95aoZZAb7_7syeuv5D_5vVY6xRSIUbEZnKfn1r4uVntb8iJag4z2ZEjxsydNWnQuRkmLWf_2mKml2qJmt5vxC-QDPQ4dqKofcdZNZxzRMiKDyTBPb9I6Gl0iEzaxt3vm3zPaiBO2_1uwknRd7ljpp34DM1lu98_JPu_z8qDPqN7YvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر بزرگه داره نماز میت رو اقامه میکنه
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17175" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17174">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش انفجار‌ در اسکله چابهار
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17174" target="_blank">📅 21:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17173">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مهر : شنیده شدن سه انفجار در کنارک
دقایق قبل سه انفجار  در کنارک شنیده شد.
از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17173" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17172">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM M</strong></div>
<div class="tg-text">یاشار من بچه اهوازم ، اونجایی که خبر دادی زده ( حصیر آباد ) دو سه تا دکل مخابراتی هست که روی کوهه ، احتمالا اونارو زده</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17172" target="_blank">📅 21:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17171">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آتش‌نشانی اهواز : انفجار ناشی از نشت گاز شهری در یک ساختمان مسکونی دوطبقه در منطقه حصیرآباد اهواز است
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17171" target="_blank">📅 21:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17170">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اهواز ارسالی :ماشین اتشنشانی و آمبولانس زیاد داره توی شهر میره به یک سمت ولی نمیدونم کجا میرن
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17170" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17169">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش تایید نشده انفجار در اهواز
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17169" target="_blank">📅 21:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17168">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28fdd7b746.mp4?token=cZJ2VaFOXK-EwfyiZsMv69xKwrcXDntP6LBzlhUaqrizu0ItqAWndLPWpqZV7-WDu8uhBJpycYUOa2YCESmgKSttmRRXpjNvFvnag_e6rJnajGz7_CUDjBnoqq6x_yVwRkqIuLSbX6wNRJi55148vF7ocTn5BRAKWpHG-eVQ2WdfDw4c0RcDfwBDXuOxnnclq44gZj2Pp3TPbggmAoLmYf_6YUt1wRFBPZ9cFnd7ukdp2kJE0LIbe7q8MdDlnWnPVL-AtdTak0th_wi9zbFDiORZSli38m1mZYbtGEFxV3XU72fhRFpW3mAusSFr2uJhqCgefDo18uKad7nhoiDG4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28fdd7b746.mp4?token=cZJ2VaFOXK-EwfyiZsMv69xKwrcXDntP6LBzlhUaqrizu0ItqAWndLPWpqZV7-WDu8uhBJpycYUOa2YCESmgKSttmRRXpjNvFvnag_e6rJnajGz7_CUDjBnoqq6x_yVwRkqIuLSbX6wNRJi55148vF7ocTn5BRAKWpHG-eVQ2WdfDw4c0RcDfwBDXuOxnnclq44gZj2Pp3TPbggmAoLmYf_6YUt1wRFBPZ9cFnd7ukdp2kJE0LIbe7q8MdDlnWnPVL-AtdTak0th_wi9zbFDiORZSli38m1mZYbtGEFxV3XU72fhRFpW3mAusSFr2uJhqCgefDo18uKad7nhoiDG4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشیاء ناشناسی در آسمان جنوب عراق مشاهده شدند که به سمت ایران در حرکت هستند، اما ماهیت آنها و اینکه آیا موشک بودند یا پهپاد یا دیگر، هنوز تأیید نمیتوان کرد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17168" target="_blank">📅 21:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17167">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فعالیت پدافند  چابهار
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17167" target="_blank">📅 21:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17166">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from♱ ᴀᴍɪʀ︎ ♱</strong></div>
<div class="tg-text">آ‌واکس
❌
یاشار
✅</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17166" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17165">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تو نوار ساحلی میرم میام هرچی نفر اول بگم</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17165" target="_blank">📅 21:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17164">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from۞۩ ¥𝕒z∂𝓐Ｎ۩ ②①:②⑧</strong></div>
<div class="tg-text">تو نوار ساحلی میرم میام هرچی نفر اول بگم</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17164" target="_blank">📅 21:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17163">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پدافند بوشهر درگیر شد
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17163" target="_blank">📅 21:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17162">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دو سوخت رسان از رامون و بن گوریون به سمت تنگه هرمز به پرواز در آمدن
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17162" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17161">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiPQmw0Tejb9L_NMv6DRglNnSoBKAXrN9BQrfJKRXBGM9Izw1j69EWlFXX4VZaSdc46z5VOXD1rCAwPDTTXsoyg7_V-6cIGKRW0hkfucjFre5Ew8eKzhAtVaCPxoU0JLj4qgm93OVVzOt41pUVG-neCU8pdAeWT2tyD1IzEr2hp7JjFNa89_LsRNtAgjeGH5-sxujGUstVtxFOqoJGeKC9saYSnxl4vxtwOYG_YshPW48IyLi60p-exrv_GYjGrLuSEV3oDo37g64D-h_6CU4AxZuApV0Tkf6YkY_aL8VY_YQU4XsbY1UDY2Tc-Tabg7d9nOhSSjhL-CFbC4osxpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پدافند سلمان حاجی آباد هرمزگان زدن
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17161" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17160">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش انفجار چابهار
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17160" target="_blank">📅 21:16 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
