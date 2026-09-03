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
<img src="https://cdn4.telesco.pe/file/D8SVRKDX2tCCo42UXZo82YZccSi1ZnzwhQC-jwFr-aYitVhesNp5M0ZartY1hZcWbUA8A3LFprTU__cLwPM7hJM_AHcIPwRdRuLRlTQguqdMjNylyvahdq9RCT1PEBk_XY-j3gxFcMio_FBRuJf8t0PQHa1qG1hGWq6CXL5u6oM685Xn0L5kveYom6t2Fu3IWffjcBqASEdc3nsxDeD2LsuaWgXqSXrGv8VOr-GkYejwt2B-n0m6YvWBBpGEaN43yVmJbE8ZHksyE9u2EoRNOLF_lZoJwOIvIL8EkUKdsP9qRAHl2meVUdall0vWMdIWM1994hpkXMy083AL4do06w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 949K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 12:48:51</div>
<hr>

<div class="tg-post" id="msg-145331">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
بلومبرگ: صادرات نفت خام عربستان در ماه گذشته به پایین‌ترین سطح در ۹ سال اخیر سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/145331" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145330">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
واشنگتن‌پست: پنتاگون دسترسی به اطلاعات طبقه‌بندی‌شده را محدود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/145330" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145329">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217c2cc494.mp4?token=mIFzmDTRHrSwDsjbYd2DOoK746mBlD6S8wuwaoUtASxfJVJtTsc_VVeTbVtN_plLk2iy5FDEAGx_Vt1OMFkMEobNwauo06wPU5m-Haw5a_rHvM-ou0-U3jg2lnTL82iND1sQnqzweaNzb_KA-DP0taG2IEp8opqqOIia_ecasVnW4RGo_NySEAzX3wXaXD-37Z27ILFlRoVaLf0_Ghr2tCYkcZaNJGy0jkfRYKE4i1Wml_UwlmZWAx2dmTzDIDAyiM1iG6Mok8JUxTTqK0YsbKQDZejbM-kSdSX0xbtjdBR_StGZIxjBopLuR0yKN0HRqDZzxBWCEq3wBlOWVpVhKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217c2cc494.mp4?token=mIFzmDTRHrSwDsjbYd2DOoK746mBlD6S8wuwaoUtASxfJVJtTsc_VVeTbVtN_plLk2iy5FDEAGx_Vt1OMFkMEobNwauo06wPU5m-Haw5a_rHvM-ou0-U3jg2lnTL82iND1sQnqzweaNzb_KA-DP0taG2IEp8opqqOIia_ecasVnW4RGo_NySEAzX3wXaXD-37Z27ILFlRoVaLf0_Ghr2tCYkcZaNJGy0jkfRYKE4i1Wml_UwlmZWAx2dmTzDIDAyiM1iG6Mok8JUxTTqK0YsbKQDZejbM-kSdSX0xbtjdBR_StGZIxjBopLuR0yKN0HRqDZzxBWCEq3wBlOWVpVhKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پیرزن پرچمی: از مسئولین هیچی نمیخوایم نه پول نه چیزی، گرونی و بدبختی رو تحمل میکنیم فقط حجاب رو درست کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/145329" target="_blank">📅 12:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145328">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بلومبرگ: شانگهای می‌تواند یک «ببر کاغذی» باشد و نگذارد تهران توسط واشنگتن منزوی شود، زیرا این سازمان با آمریکا نیست، با ایران است؛ با اروپای غربی یا اوکراین نیست، با روسیه است
🔴
«یا با ما هستید یا علیه ما»؛ این سخن وزیر خزانه‌داری آمریکا در مورد همکاری بین‌المللی علیه ایران در سال ۲۰۲۶، محکوم به شکست است، زیرا هدف مشترک شانگهای کنار زدن هژمونی ایالات متحده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/145328" target="_blank">📅 12:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145327">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
موسسه‌ی پیرسون، که برگزار کننده‌ی آزمون‌های مختلفی از جمله AMC MCQ و Oman OMSB هست هم از امروز خدمات دهی به ساکنین ایران را لغو کرد.
🔴
تمام کسانی که ساکن ایران هستند، از تاریخ ۸ سپتامبر امکان ثبت‌نام و شرکت در امتحان را ندارند، حتی اگر از قبل ثبت‌نام کرده باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/145327" target="_blank">📅 12:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145326">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
دو مقام ارشد دولت آمریکا مدعی شده‌اند شرکت کشتیرانی دولتی چین COSCO از برخی کشتی‌های خود برای جمع‌آوری اطلاعات سیگنالی و رصد ارتباطات نظامی در نزدیکی سواحل کشورهای مختلف از جمله آمریکا، استفاده می‌کند.
🔴
به گفته این مقام‌ها، تجهیزات پیشرفته و مخفی‌شده در برخی کشتی‌ها قادر به جمع‌آوری اطلاعات درباره ارتباطات نظامی، فناوری‌های رمزنگاری و تحرکات در مسیرهای مهم دریایی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/145326" target="_blank">📅 12:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145325">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزارت بازرگانی چین، در رابطه با تحریم‌های آمریکا علیه ایران: از آمریکا می‌خواهیچ که فوراً "رفتار نادرست" خود را اصلاح کند و تحریم‌هایی را که علیه شرکت‌ها و شهروندان چینی اعمال شده است، لغو کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/145325" target="_blank">📅 12:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145324">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raL7y5IP3V6dYF6dmjHZuDjcZh68VeXNRT0YXg1v0F5m3WUK9jsQe38ChtpmoyJkPlEraEQSOvaHcTZe--wd-vO5-dkzlKj8bOf7Kq5FVNF6E9U9EjZol7vDeobNkDO9Qtse-lHkDUvde0_4uWBgxceC7gY1DAAXCkyiCP3tevCfPO-tjLZck6cMC56_T0YeV8WMvmiQs2f1cb2LbpjdoHqUoCUmYjcMVDZcOHskT24udp61m9hJn5hmZ1Utgydq_2e375H93XcBYdHdlvEkMgYSos_VmA77emrnsi6FcDsBLTxXKAtAzZUmIRcYC9i6jZz8M8p6o4niI-eD70UOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گوشی شیائومی ۴۱۸ میلیون تومان!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/145324" target="_blank">📅 11:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145323">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOMccvfCCGEIlDz8JpJBtgoqO0D5N8m5y8yvLq85vDnhIz3GxiguD1_GIyYlnKxY9XClIzFJR7qML8kGbDC0qi8Mc3E4LnJuErTzhMAvSP6IlnbLqr2dnfMMmD4vFKUx_AbL0ZpL0NcH5q6KgxTH0f0dRp-jLTmqHtmTWS2GaVLUbjph6ZMZ6OX24l-DMppsb6L88w_dW25S4Ju55ul4edixd8a4ugTJ8UBcLDeV11q4jG5n1PIT-DmembZruDhFqS4wB3YYY3Vbj57Ukm9VV_Q903nmSbRUmEX-d7Fo1WttgJo9zI5qK9j6ULmRydxzNIRO0yZscWRo7l6h1DxbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت سایپا در اصلاحیه جدید شرایط فروش خود، قیمت چانگان CS55 پلاس، سیتروئن C3-XR، کوییک S و سهند S را افزایش داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/145323" target="_blank">📅 11:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145322">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سردار کوثری نماینده ۴ درصدی مجلس: گرانی و تورم وجود دارد، اما مردم هر شب شاداب‌تر به میدان می‌آیند
🔴
ما دقیقاً بلدیم چگونه مسائل اقتصادی و حتی جنگ را مدیریت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/145322" target="_blank">📅 11:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145321">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
عزیزی، رئیس کمیسیون امنیت ملی مجلس: تنگه هرمز بدون اراده ایران باز نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/145321" target="_blank">📅 11:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145320">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رویترز و رسانه‌های اسرائیلی: ایران به آمریکا هشدار داد در صورت حمله اسرائیل به رشته‌کوه «علی طاهر» در جنوب لبنان با قدرت پاسخ خواهد داد
🔴
بر اساس این گزارش‌ها، شماری از نیروها و فرماندهان ارشد سپاه پاسداران همراه با نیروهای حزب‌الله در تأسیسات و شبکه تونل‌های زیرزمینی این ارتفاعات مستقر بوده و تحت محاصره قرار دارند. ایران تأکید کرده است هرگونه حمله همه‌جانبه برای تصرف این ارتفاعات، پاسخ مستقیم و گسترده تهران را به دنبال خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/145320" target="_blank">📅 11:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145319">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
مقامات آمریکایی به وال استریت ژورنال گفتند که ترامپ در حال مذاکرات خصوصی با دستیاران ارشد خود برای اعلام پایان جنگ با ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145319" target="_blank">📅 11:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145318">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
دلار هم اکنون 222,500 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/145318" target="_blank">📅 11:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145317">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be29f820c8.mp4?token=oq_gK638sBce8Ch_YSELkA9oBG209ul0xLYwKynXBhlI9ESCfbja2lMBI-lWCUE_vWk1A8KrJ61dhkm634RvE_S8JU6BO5KMwJPDqmH6JulgoUdw0P89ye0pmoNc9bKrjqdN2rHQX6gyiBzAjRsFWiHXuaDuinuRD_6WvRzSeax6RACpHjRK3d3N2LsHNvOlnuAjNTsbgI878yAYaFOTmK5m6QnGxrFvRMMbadiCD146Tgg7-oE_azdVAXbuCbcIzhTLx9Oz4gYxGiMf5PZFcgWeRYKNsLqEAIC7JCy8-09kCDtuk2kHVVruS2me9h5A1NmDenOfFFnRBHszMy7ZppZN8jl4jLm4dqS6xF-KAVdZTMXsCb7s1Da9252REsdujFPcKeS3xKv97GUVSV9k71M0zkZYOqqZIIrLMdJYAZEp3cHJDvUSGkjeS596olZ-eSXlNa4Vz9KRIBUOa2q0w05tC5OweFUTDXmwbRBpnJ2Eqo09fRHf0t9iryAUZQTN8VTOYntyVGddKnZgPt4_I06QVhmGCRyHGXOKAszXFEYm-dGdVmIsu4GtbfS3xQLMdRmYibUwQTVeKWgXM41V3tKbx7iwVrwPfZqGBw5rhIQ9VRGYS4ieIsYpVVDtXhrPtV2tyI2ZXCy51gmYuEmBiTBrjzMBq_OXp5wfhyCaTwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be29f820c8.mp4?token=oq_gK638sBce8Ch_YSELkA9oBG209ul0xLYwKynXBhlI9ESCfbja2lMBI-lWCUE_vWk1A8KrJ61dhkm634RvE_S8JU6BO5KMwJPDqmH6JulgoUdw0P89ye0pmoNc9bKrjqdN2rHQX6gyiBzAjRsFWiHXuaDuinuRD_6WvRzSeax6RACpHjRK3d3N2LsHNvOlnuAjNTsbgI878yAYaFOTmK5m6QnGxrFvRMMbadiCD146Tgg7-oE_azdVAXbuCbcIzhTLx9Oz4gYxGiMf5PZFcgWeRYKNsLqEAIC7JCy8-09kCDtuk2kHVVruS2me9h5A1NmDenOfFFnRBHszMy7ZppZN8jl4jLm4dqS6xF-KAVdZTMXsCb7s1Da9252REsdujFPcKeS3xKv97GUVSV9k71M0zkZYOqqZIIrLMdJYAZEp3cHJDvUSGkjeS596olZ-eSXlNa4Vz9KRIBUOa2q0w05tC5OweFUTDXmwbRBpnJ2Eqo09fRHf0t9iryAUZQTN8VTOYntyVGddKnZgPt4_I06QVhmGCRyHGXOKAszXFEYm-dGdVmIsu4GtbfS3xQLMdRmYibUwQTVeKWgXM41V3tKbx7iwVrwPfZqGBw5rhIQ9VRGYS4ieIsYpVVDtXhrPtV2tyI2ZXCy51gmYuEmBiTBrjzMBq_OXp5wfhyCaTwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به هگ‌ست در مورد ایران
:
شما شب گذشته کار بسیار خوبی در مورد ایران انجام دادید. شما آن‌ها را به شدت شکست دادید. بسیار عالی.
🔴
ما در این زمینه، به هر حال، پیروز می‌شویم. ما باید این را بگوییم، زیرا رسانه‌ها از گفتن آن خودداری می‌کنند.
🔴
با این حال، حتی روزنامه نیویورک تایمز هم گفت که ایران اخیراً وضعیت خوبی ندارد. این یک خبر تکان‌دهنده بود وقتی آن‌ها این را گفتند.
🔴
آن‌ها هیچ هواپیمایی، هیچ چیز مربوط به هواپیما یا کشتی ندارند. همه آن‌ها در اعماق دریا یا در انتهای باند فرودگاه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/145317" target="_blank">📅 11:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145316">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ در یک تماس تلفنی با شیخ محمد بن زاید آل نهیان، رئیس‌جمهور امارات متحده عربی، درباره تقویت همکاری‌ها و روابط میان امارات و  ایالات متحده گفت‌وگو کرد
🔴
آن‌ها همچنین درباره منافع مشترک، به‌ویژه «تحولات در خاورمیانه» و تلاش‌های جاری برای رسیدگی به این تحولات، گفت‌وگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/145316" target="_blank">📅 10:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145315">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
همزمان با کاهش تنش بین ایران و آمریکا و توقف درگیری‌ها در شب گذشته، قیمت نفت مجددا نزولی شد.
🔴
قیمت نفت خام برنت و WTI به ترتیب به اعداد ۹۴.۳۹ و ۸۹.۹۸ دلار بر بشکه کاهش یافتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/145315" target="_blank">📅 10:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145314">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
رویترز: دولت آمریکا ممکن است تشدید حملات علیه ایران را پس از انتخابات میان‌ دوره‌ای بررسی کند، اما هنوز تصمیم نهایی گرفته نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/145314" target="_blank">📅 10:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145313">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
مالک خبرگزاری رویترز در بیانیه‌ای مطبوعاتی اعلام کرد یکی از واحد هایش با حادثه امنیت سایبری مواجه شده است.
🔴
این حادثه امنیت سایبری در پلتفرم مدیریت پرونده‌های قضایی C-Track که برای مدیریت دیجیتالی پرونده‌ها و اسناد دادگاهی استفاده می‌شود، رخ داده است.
🔴
این حادثه ۳۰ ژوئن (۹ تیر) شناسایی شد و سامانه‌های قضایی در ۱۱ ایالت آمریکا و جزایر ویرجین آمریکا و کانادا را تحت تأثیر قرار داد­.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/145313" target="_blank">📅 10:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145312">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCjwGlHf1O7pu8z91DaSuMcG5ed6WLvQtI_uhjAyFcI21n-S1DA2UAZNJFNSnhI0QIPdvr37FzfWQESlB8aTjUprBQ4CqKcUFBjOCmUzNkIUtjIuLiE2XUrGXCTin2IGYacqLiEh4k2OjPS8JVeZ61q8-_wDJjwWN7xVOIqbKxfphCyw5o-NG2E7Hyll1xG7HsHL_mVWKZMzd-OwCC-htdMhDSol56iS5yjYaK9D5ocN3tp8vtrfgtqRrdU11g_GECTXkfsqIwCSQj8wr_HqtBmv-1uFebrUxGr9dl-30bWmlCeB-C6khsOLqTQ4jTusN5-KyIavnhCUti8taj4r7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت در پی حمله به پایگاه‌های آمریکایی در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/145312" target="_blank">📅 10:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145311">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بابک زنجانی: کسایی که بهم فحش میدن سایبری هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/145311" target="_blank">📅 10:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145310">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کپلر: روز چهارشنبه تنها ۶ کشتی حامل کالا از تنگه هرمز عبور کردند؛ این رقم یک روز پیش از آن، ۱۱ کشتی بود
🔴
بر اساس جدیدترین داده‌های ردیابی کشتی‌ها از شرکت کپلر که رویترز به آن استناد کرده، روز چهارشنبه تنها شش کشتی حامل کالا از تنگه هرمز عبور کردند؛ این رقم یک روز پیش از آن ۱۱ کشتی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145310" target="_blank">📅 10:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145309">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=G8OLRiM86Pow5j8oQzxtUz7Iqb1fSh3favn8UnqReoIkDD7OfK0pBR9cfGTityqhrE6Mb6VmqcZ-2j4GFv-57w9_QnKtrZNf9pfXiJRcVnIUEpJ1qhk2o6VbCbNfOb8kBcbPtvaVtdSlmhWYHjpHKg4PQNtYFO5dUW5SmIvp9nlC3yief5gD3cDEFW3k1o-bY67YoCL-1pbSWYVuhqZMk8YnAwhrd0J3YeJ1rqCT4Bb0I1i-nkc_TOF2QgpDEW_K2HOuE76tqzGrH0ATfTNSPpo-8Idxn0uLEeDT5t0b__dlGlnab7HW4_SGaJXDrrX2RRmsVuC6E9ZyC5p_UKMjuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=G8OLRiM86Pow5j8oQzxtUz7Iqb1fSh3favn8UnqReoIkDD7OfK0pBR9cfGTityqhrE6Mb6VmqcZ-2j4GFv-57w9_QnKtrZNf9pfXiJRcVnIUEpJ1qhk2o6VbCbNfOb8kBcbPtvaVtdSlmhWYHjpHKg4PQNtYFO5dUW5SmIvp9nlC3yief5gD3cDEFW3k1o-bY67YoCL-1pbSWYVuhqZMk8YnAwhrd0J3YeJ1rqCT4Bb0I1i-nkc_TOF2QgpDEW_K2HOuE76tqzGrH0ATfTNSPpo-8Idxn0uLEeDT5t0b__dlGlnab7HW4_SGaJXDrrX2RRmsVuC6E9ZyC5p_UKMjuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 225هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145309" target="_blank">📅 10:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145308">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/131e4d5002.mp4?token=NxJEpImDROnQbrL4VIs1kHWYYnppOACHL5gZCBBn_jFO_X1ODVBx8S0QBCZIHdGhf6i2bT4uEX0CRYRn3vEVORwH5uY91VnS64y8oodPEabAMv86W9xplHAHmn2eXCCJgR-AgguHhcupdVgQ5i2McEyygaB6Uk894asl8hmNbL74Ol8nnokWHhUtX35u7zdfLSHHdfT5DthdXUl-cnbH7Ug51Mx5ICXaN3c6lgPnhZoT3PP2vqfX3mZVOz_mVptgBZuTj7lkiZ6Z2fGhuZaXQOpy0Wp7ECfhtIOyVjaAM7IXsRz5wzqWtErPxJzvW3A-5jYBwlNhT2HZE6rkW5b2BjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/131e4d5002.mp4?token=NxJEpImDROnQbrL4VIs1kHWYYnppOACHL5gZCBBn_jFO_X1ODVBx8S0QBCZIHdGhf6i2bT4uEX0CRYRn3vEVORwH5uY91VnS64y8oodPEabAMv86W9xplHAHmn2eXCCJgR-AgguHhcupdVgQ5i2McEyygaB6Uk894asl8hmNbL74Ol8nnokWHhUtX35u7zdfLSHHdfT5DthdXUl-cnbH7Ug51Mx5ICXaN3c6lgPnhZoT3PP2vqfX3mZVOz_mVptgBZuTj7lkiZ6Z2fGhuZaXQOpy0Wp7ECfhtIOyVjaAM7IXsRz5wzqWtErPxJzvW3A-5jYBwlNhT2HZE6rkW5b2BjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحید خزایی: زن سپهر حیدری یبار منو برد خونشون و منم ترتیبش دادم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145308" target="_blank">📅 10:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145307">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
به گزارش رویترز، دست‌کم سه پالایشگاه هندی و یک شرکت بزرگ جهانی انرژی قصد دارند به دلیل نگرانی‌های امنیتی در تنگه هرمز، استفاده از کشتی‌های موجود در فهرست تحریم‌های ایران را متوقف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145307" target="_blank">📅 10:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145306">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=jVvORPAM8CyhtI79QWU2jv4xzX9Te2-hYcnS9rhZQWn87D8XG6-m26kTuNXREbQgRTiil6JiExyTp_joSqNAMZI39H7xf5go3-IdToKCxomhFg5XbEw7Og4gCiBnlyxLGq3E7U_bvfghT9FIsqJNt81LzEHU7cZMiHorFKXUrgajxFJ_xA7hS-2Nxp-BehA_P5lfuJKUNgZpmf5irM-G1o12uEsNRj6zagBlEsd4oz9yWb5FfWfFP-Wk7pOtHRzQEwvhXIBtUHN6dqzikWvwFAN32c3hJ77PwDfkbn6nxrEEtSIdadp3JAlCi2tH7UdHJXNTW4skPcqZuWQ6TecDfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=jVvORPAM8CyhtI79QWU2jv4xzX9Te2-hYcnS9rhZQWn87D8XG6-m26kTuNXREbQgRTiil6JiExyTp_joSqNAMZI39H7xf5go3-IdToKCxomhFg5XbEw7Og4gCiBnlyxLGq3E7U_bvfghT9FIsqJNt81LzEHU7cZMiHorFKXUrgajxFJ_xA7hS-2Nxp-BehA_P5lfuJKUNgZpmf5irM-G1o12uEsNRj6zagBlEsd4oz9yWb5FfWfFP-Wk7pOtHRzQEwvhXIBtUHN6dqzikWvwFAN32c3hJ77PwDfkbn6nxrEEtSIdadp3JAlCi2tH7UdHJXNTW4skPcqZuWQ6TecDfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سکه 231 میلیون
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/145306" target="_blank">📅 09:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145305">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
زهران ممدانی، هوش مصنوعی را در مدارس نیویورک ممنوع اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/145305" target="_blank">📅 09:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145304">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شریعتمداری به ارتش و سپاه: کابل‌های اینترنت جهانی را که از خلیج فارس و تنگه هرمز می‌گذرند قطع کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145304" target="_blank">📅 09:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deba41468f.mp4?token=lvqF2swBKgeZ7DPTTI7hPzyjxXMqCRWeJ0XqgDkWPD_NEmGKVu4J5-HDnqPNVtUSC-fjJT-lQ7-hEA69pFe9sb2pWs_8ERXIZZ_vwEz7Z2t5RiEW8s6xaaScqTcBvffJnKSj1CIb4nq0xXk8doaMo8VwUTdxyf2imn-5LMZUqv-3HWBNirPHJNbwB3v5I5SFkFebeI4blpZlcMFY7Khdg1O8qeOuYVT34g-JdqdfyL3U9vp-RJhsecRqM3v8HW3Nh3xnnSdqOyv3JeTwawPt3RqSY2jDBFIY-HhIau6BvVf0j93dVSvWoA_AOCpmXardUoFMf7Vys-QoWv_jGJcaTnRiwNsprdSMPCDFdJ6j5IqV-YYZXwAMGAFqfV6aTZ_icnF5z_nHVlg9hHoU4jkiDAGyBIcpUz3vSeAobJDvLMUDUuxjNwCgt5bCaKchl5dQEBF7mdBTWATM3cvQVuZQzc03T0-NUxKzbwuH2KgJlgrYJAarSuusgWlksFlZGnwrIItYgAZc87uxstynzgy_1EKVsIAbteOoqFPzjADr1nCZz_FcLwBZx-ENKfmZzTw9cx-WhSTvNv6z42IjcAxLLb7nK3OF34VshFyynSGZk2-oVpa0qvGH2Gs7aAFb3PZujepiGTupIwUjUyyTWMQP2l-lElA2ELfVFeK29H86zqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deba41468f.mp4?token=lvqF2swBKgeZ7DPTTI7hPzyjxXMqCRWeJ0XqgDkWPD_NEmGKVu4J5-HDnqPNVtUSC-fjJT-lQ7-hEA69pFe9sb2pWs_8ERXIZZ_vwEz7Z2t5RiEW8s6xaaScqTcBvffJnKSj1CIb4nq0xXk8doaMo8VwUTdxyf2imn-5LMZUqv-3HWBNirPHJNbwB3v5I5SFkFebeI4blpZlcMFY7Khdg1O8qeOuYVT34g-JdqdfyL3U9vp-RJhsecRqM3v8HW3Nh3xnnSdqOyv3JeTwawPt3RqSY2jDBFIY-HhIau6BvVf0j93dVSvWoA_AOCpmXardUoFMf7Vys-QoWv_jGJcaTnRiwNsprdSMPCDFdJ6j5IqV-YYZXwAMGAFqfV6aTZ_icnF5z_nHVlg9hHoU4jkiDAGyBIcpUz3vSeAobJDvLMUDUuxjNwCgt5bCaKchl5dQEBF7mdBTWATM3cvQVuZQzc03T0-NUxKzbwuH2KgJlgrYJAarSuusgWlksFlZGnwrIItYgAZc87uxstynzgy_1EKVsIAbteOoqFPzjADr1nCZz_FcLwBZx-ENKfmZzTw9cx-WhSTvNv6z42IjcAxLLb7nK3OF34VshFyynSGZk2-oVpa0qvGH2Gs7aAFb3PZujepiGTupIwUjUyyTWMQP2l-lElA2ELfVFeK29H86zqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بابک زنجانی: الآن کافه‌های مردم را می‌بندید بعد شب آدم می‌فرستید که بیاید تعامل کند. می‌خواهم فیلم و مستند درباره این موضوع تهیه کنم... آن شخص (رشوه گیر) هم [به اشتباه] فکر می‌کند که با ۱۰، ۲۰ سکه زندگی‌اش را گذرانده
🔴
بیکار کردن ۸۰ نفر در منِ بابک زنجانی چه اثری دارد؟! اصلاً فردا بیایید آتشَش بزنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/145303" target="_blank">📅 09:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a98021678c.mp4?token=HhbE71tghMXmNEnUoNFtva3SralSAM2gP3MoeLyHoeKW9DSY0mWL_FvyOdY-wJdDXUxOjpBP5Yu7hH_-N4r-KY9Y-6ousND1P1TbKxffT_pkn-hMEClXnNtPSIwCcxQHvRwoFYCyhYDUSXLj4yknVCpGgDEDb1KwWRNIXGwwBmcTETBzJVBaNx-FTBbC4kFoRNKr_S4-NdtwUOqswneunvypJ3QFItQAGVGjiAFBJOo2nfqM15lye4eZoOWSPrjhyQDpY0Prik1c2vBe9z7n7QO6l46rhNGCRRQNmMCFPBMEVSMrTELACkksdPDoIGH8Wj2NPGQvJJO0Z9GdP5-SXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a98021678c.mp4?token=HhbE71tghMXmNEnUoNFtva3SralSAM2gP3MoeLyHoeKW9DSY0mWL_FvyOdY-wJdDXUxOjpBP5Yu7hH_-N4r-KY9Y-6ousND1P1TbKxffT_pkn-hMEClXnNtPSIwCcxQHvRwoFYCyhYDUSXLj4yknVCpGgDEDb1KwWRNIXGwwBmcTETBzJVBaNx-FTBbC4kFoRNKr_S4-NdtwUOqswneunvypJ3QFItQAGVGjiAFBJOo2nfqM15lye4eZoOWSPrjhyQDpY0Prik1c2vBe9z7n7QO6l46rhNGCRRQNmMCFPBMEVSMrTELACkksdPDoIGH8Wj2NPGQvJJO0Z9GdP5-SXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اقتصاد آن‌ها بدترین اقتصاد در کل جهان است. پول آن‌ها بی‌ارزش است.
🔴
و بنابراین، این فقط یک مسئله زمان است. فقط یک مسئله زمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/145302" target="_blank">📅 09:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145301">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
حکم ساعدی‌نیا در دیوان عالی کشور تایید شد ، ۱۲ سال و ۶ ماه و یک روز حبس و مصادره کلیه اموال
🔴
حکم پرونده صادق ساعدی‌نیا در دیوان عالی کشور تایید و وی به حبس و مصادره کلیه اموال منقول و غیر منقول محکوم شد.
🔴
پس از رسیدگی به این پرونده در دادگاه صادق ساعدی نیا به اتهام فعالیت رسانه‌ای و تبلیغی علیه امنیت کشور به ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال منقول و غیر منقول به نفع دولت محکوم شد.
🔴
همچنین به منظور جبران خسارت وارده به اماکن و اموال عمومی در استان قم به منع اشتغال در شغل کافه‌داری به مدت ۲ سال پس از اتمام حبس محکوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/145301" target="_blank">📅 09:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145300">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وال‌استریت ژورنال: هگست استقرار نیروهای آمریکایی در خاورمیانه را تا سال ۲۰۲۷ تمدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/145300" target="_blank">📅 09:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9e4206fda.mp4?token=lvOxuMouVizQimbVfCzj8fj4j4Ta81eOmolC9l7e1OdDKKBPNrCywNjLG0tIlvW7ulFZk1JyvliFZ3u_Oy-ahRcjp1aO0KR9M0At77G-uAf2e_oKmXW2d9I0Et9JrT8T2Y4VC13BvGQgN2TQq-dGnATxfZZV-U9xe8DS_q8Q3GpsSbma9Pdn7qKMGR8XFY0mI0YbtBO64cbWWhHrBkMcxoBTTAUhS4I8eb_whv_sBWJlj5Yf0m5ahEyGmY8lfoW6c5cse1BaqUnj0vxjX4al8YSQOGg1q8yZ-nBT3Kx8cNkCvLi2w_cJQmcGk_-XVM7aeBho7miynfyz5WIbdFPAqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9e4206fda.mp4?token=lvOxuMouVizQimbVfCzj8fj4j4Ta81eOmolC9l7e1OdDKKBPNrCywNjLG0tIlvW7ulFZk1JyvliFZ3u_Oy-ahRcjp1aO0KR9M0At77G-uAf2e_oKmXW2d9I0Et9JrT8T2Y4VC13BvGQgN2TQq-dGnATxfZZV-U9xe8DS_q8Q3GpsSbma9Pdn7qKMGR8XFY0mI0YbtBO64cbWWhHrBkMcxoBTTAUhS4I8eb_whv_sBWJlj5Yf0m5ahEyGmY8lfoW6c5cse1BaqUnj0vxjX4al8YSQOGg1q8yZ-nBT3Kx8cNkCvLi2w_cJQmcGk_-XVM7aeBho7miynfyz5WIbdFPAqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که در یک پایگاه نظامی آمریکایی در نزدیکی فرودگاه بین‌المللی اربیل در کردستان عراق، به دلیل حملات ایران، آثار سوختگی مشاهده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/145299" target="_blank">📅 08:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رویترز به نقل از منابعی گزارش داد؛ پس از اعلام فهرست اولیه کشتی‌ های ممنوعه ایران، دست‌کم سه پالایشگاه نفت هند و یک شرکت بزرگ بین‌المللی انرژی قصد دارند به‌دلیل نگرانی‌ های امنیتی، استفاده از کشتی‌ های قرارگرفته در این فهرست را متوقف کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/145298" target="_blank">📅 08:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145297">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696c66d269.mp4?token=pnoCwFf0a0eDOEtcXy4sFzHFMBd9l8oJgbl7m8PALBS7W926RaPmyogEU4Edln6Cynkv9fLfB1lArzIGY7pk73X2pnb7ZsOJMPbbm2OxsGCOJHW3MkWfCzr3P296PZwcl1XtPThK-TmBOAVJmRIRczSW9sj3_UCwmnpDEpmAqfgZUb69_yf1gRyR_eF7Iqd16QUWSW6ei_7Lz3YKCVvYN10r-PuA9bmgTnlhjTPMExW9uIdCae_2h1GklwH-GZp0Qs2938lqFDMLZoA6r9fnwgUOJpRV5RZUK7HOXAr3nQ6X_KQ2IIYYI9giVgyo6wMwvEG7qkNiFuJtMnjh-BrLgzZzE3J1iLA7Ya6eddohhM9Je_-diXdRgFILmn8i8mmSorB2f8WSZOE7cwCYjl_42fRu04GsKRxHRLQpH3xSZH4oHFRgzXPezWBsYQNCPFbpxuwus6tYd56FNxJNVqAkYy1Pq8fphTIi5H5puR9SZKZf-wKumvQm-UTokP9p0pZUO5Jc4h7V46r_NIWX2d8rGry9UuysDQKK-f_gmZDrsNO4K8dxhR-Ypr8MWxotLVBNHxKO9suze5IdvWJ3CisGCBC0hWLcLrO60m2sKdoSKS3h68q0ccC9mT_vqVTU_s92dZezqybQxx84KxmNkkwXfiyZ10DQRVx0NSlGFew4yRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696c66d269.mp4?token=pnoCwFf0a0eDOEtcXy4sFzHFMBd9l8oJgbl7m8PALBS7W926RaPmyogEU4Edln6Cynkv9fLfB1lArzIGY7pk73X2pnb7ZsOJMPbbm2OxsGCOJHW3MkWfCzr3P296PZwcl1XtPThK-TmBOAVJmRIRczSW9sj3_UCwmnpDEpmAqfgZUb69_yf1gRyR_eF7Iqd16QUWSW6ei_7Lz3YKCVvYN10r-PuA9bmgTnlhjTPMExW9uIdCae_2h1GklwH-GZp0Qs2938lqFDMLZoA6r9fnwgUOJpRV5RZUK7HOXAr3nQ6X_KQ2IIYYI9giVgyo6wMwvEG7qkNiFuJtMnjh-BrLgzZzE3J1iLA7Ya6eddohhM9Je_-diXdRgFILmn8i8mmSorB2f8WSZOE7cwCYjl_42fRu04GsKRxHRLQpH3xSZH4oHFRgzXPezWBsYQNCPFbpxuwus6tYd56FNxJNVqAkYy1Pq8fphTIi5H5puR9SZKZf-wKumvQm-UTokP9p0pZUO5Jc4h7V46r_NIWX2d8rGry9UuysDQKK-f_gmZDrsNO4K8dxhR-Ypr8MWxotLVBNHxKO9suze5IdvWJ3CisGCBC0hWLcLrO60m2sKdoSKS3h68q0ccC9mT_vqVTU_s92dZezqybQxx84KxmNkkwXfiyZ10DQRVx0NSlGFew4yRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی ایالات متحده، درباره ایران: مسیرهای جایگزین نیز وجود خواهد داشت. نمی‌توان همه تخم‌مرغ‌ها را در یک سبد گذاشت.
🔴
شاید جهان قبلاً چنین وضعیتی را با تنگه هرمز داشت، اما رئیس‌جمهور ترامپ این را تغییر می‌دهد.
🔴
خطوط لوله جدید ساخته خواهند شد و خطوط لوله موجود گسترش خواهند یافت تا اهرم‌های آینده ایران برای استفاده مجدد از تنگه هرمز کاهش یابد.
🔴
اما نیروی دریایی ایالات متحده در حال حاضر حملات ایران را خنثی می‌کند و امروز نفت و گاز را به بازار می‌رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/145297" target="_blank">📅 08:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145296">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: تا من هستم، اسرائیل نباید نگران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145296" target="_blank">📅 08:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145295">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ru4ZfIoMIeP5OYLjadFUQpov724j57KRza9lCr-K94AlbAjBZUfLGmG5xtO80dkVjx3LsMluilyd1RakZqw0W40P8WuER9ZQWIuVrluzoAhCh7iAfKg-cDjKLSOU9LbjpVNn80DwBojy2050baQ3eTgJaNcbUDhncxpUBOje8VZd_ZsvQyaxUfVEjhsnzqYUCZjpEIVc1Uun5wf1FFVzpvA071rKapiuF_s8IMww6GLgIBbiYBnXD-wgZX4IEjCq3I_FDP6XZ0FknS0Ye5tw3X98mCMDE0Osmny00gTnRdUAQxHNMtshisEBXMo5VStVIwZB4mDswnR1U7aXuEVYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / هشدارها در کویت به دلیل حمله موشک‌های بالستیک و پهپادها
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/145295" target="_blank">📅 08:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145294">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
اکسیوس به نقل از منابع: ویتکاف آخر هفته گذشته با مشاور امنیت ملی امارات دیدار کرد و درباره گام‌های بعدی در قبال ایران ایده‌پردازی و رایزنی کردند
🔴
طی همان روز، واشنگتن دسترسی شعب اماراتی «بانک مصر» به نظام مالی آمریکا را به دلیل تجارت با تهران، قطع کرد
🔴
وزیر خزانه‌داری آمریکا هم پیش از اعلام تحریم‌های جدید علیه ایران، با طحنون گفت‌و‌گو کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/145294" target="_blank">📅 08:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145293">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
آکسیوس: وزیر خارجه آمریکا از سفارتخانه‌ های این کشور خواسته به دولت‌های میزبان برای قطع فوری تجارت با ایران فشار بیاورند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/145293" target="_blank">📅 08:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رویترز: کاخ سفید تشدید اقدام نظامی علیه ایران پس از انتخابات میان‌دوره‌ای را منتفی نمی‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/145292" target="_blank">📅 08:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145291">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وال استریت ژورنال: توافق هسته‌ای عربستان می‌تواند راه را برای غنی‌سازی اورانیوم تا ۲۰ درصد هموار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/145291" target="_blank">📅 07:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/145290" target="_blank">📅 01:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145289">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
صدای انفجارها در جنوب ایران شنیده می‌شه
🔴
گزارش های تأیید نشده از حمله به یک نفتکش
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/145289" target="_blank">📅 01:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145288">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
دلیگانی نماینده مجلس: امارات باید کشورش را به عنوان غرامت به ما بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/145288" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I65xsPS0X3IMbuRrCPMlyH89k0NNnsflkvq_D-ojL-ff7LS41Mb7vJ4bEwoRh4jZ2OOz4spkrcJcKqoSdsHY5PdSot-TJLtJI523BT5NERtWq9UZiaiaV0Zn8W_ySaq6x9EP3DNAZBHK1KvgWNKczv9iRr-2uNOqv7rd7NzDE09E9BvPeRidsQct07W0HaAkJW9sfaQf9-Xo2dEWgT1Mj3yqin6NElohj1AD-RzkXNykyTS8sEUcFhvbBnRm-1pP8iI6TVguiO_bTdwWeMj8UJ4nCrA7tw2nTSQtHkeoykZZJ-2KwiGK8awBIoyxKo9RdNrpyHaG-JKFLXJ62Cwl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پهپادی گسترده اوکراین به روسیه با شلیک بیش از 250 پهپاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/145286" target="_blank">📅 01:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">حالا درسته که با هوش مصنوعی داره خیلی از شغل ها به خطر میوفته
ولی تو نگران نباش
هوش مصنوعی خایه مالی بلد نیست
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/145285" target="_blank">📅 01:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145284">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/145284" target="_blank">📅 01:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
امام جمعه رشت:
مردم مشکل معیشتی ندارند. شما خیابان هارو ببینید! ایا این زنان لختی که میبینید فقیر هستند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/145283" target="_blank">📅 00:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af9792bdd.mp4?token=H14I3e3oqhqUqyHP5SwC48cxBjml1cCW6EqtTv8HFNEi1fHpRwnRfVPwPrHY2L5Jq_wr7rj57vzd7PEWRYSkF1zpvnyk20B_-DO7iwHRCRPmoEZA9t0Wm3h6RwtN_fCN1-8_0tF2SHTIaIvKGwzSBuo_oOHGw13weJkmR1XSqulCe-I7vU0xnZteN8bVMYFrVfS-6YK_I7XK9k0NPppdXwSQa_-RCKXxhZcC6cnBAYOIhDB_mZCTc0yuZWkZfajOxwM0STksO67elbnrbyn9Z4EEm8kHivKKuJn1WkugwNDCt7AYlC4ry1p20u-MlRQMCpmALv38-dLs-cXx-WeK_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af9792bdd.mp4?token=H14I3e3oqhqUqyHP5SwC48cxBjml1cCW6EqtTv8HFNEi1fHpRwnRfVPwPrHY2L5Jq_wr7rj57vzd7PEWRYSkF1zpvnyk20B_-DO7iwHRCRPmoEZA9t0Wm3h6RwtN_fCN1-8_0tF2SHTIaIvKGwzSBuo_oOHGw13weJkmR1XSqulCe-I7vU0xnZteN8bVMYFrVfS-6YK_I7XK9k0NPppdXwSQa_-RCKXxhZcC6cnBAYOIhDB_mZCTc0yuZWkZfajOxwM0STksO67elbnrbyn9Z4EEm8kHivKKuJn1WkugwNDCt7AYlC4ry1p20u-MlRQMCpmALv38-dLs-cXx-WeK_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صداوسیما: صحبت های یاسمین پهلوی زنِ تام .... رضا پهلوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/145282" target="_blank">📅 00:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dv4EsX0FjQUltfTAZR61pUOT6dNB3PqQL1E0HwM_PMUI2qoPqhVMN1c-dPwsaX8A0UWmoR1lMt5-jL-OLDmwJf4OXzT1FQn6S_LV-gougthiJK61G7BKyCz_OO2PVOiBdH_YNB57iwLQSeDxFIctqwskl3-CHUbbDLYyWpd-QSIIwEixRIKT-O0gpsMewi-Y8-7XtR2gai_5uHnaGbIuNCgSIxNp9mx-Q76thycLJiwNAMDcX7rDp7MTOm8nIDYpiGW9RFusUBW6VNvCbIwUR1OcCTIv8V3qzGRm_rbVrL3QLD25vuJLvwi-g3zd1_QObzcK-VcrwpRpqMWhfuIHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا موشک‌های کروز تاماهاوک را در نروژ مستقر کرده است
🔴
بر اساس گزارش‌های منتشرشده، آمریکا موشک‌های کروز تاماهاوک را در نروژ و پرتابگرهای دیگری را در جزیره «یان ماین» مستقر کرده است.
🔴
با توجه به برد این موشک‌ها، بخش‌هایی از خاک روسیه می‌تواند در محدوده برد آنها قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/145281" target="_blank">📅 00:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145280">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnJ0J1SIDRNbojA1vUkJn4X1xCfU6GoVRjMA4AIb-kxD4R7RAmL-agZ1A8XfR-pT4QefRNMU-KuRrsbvA3AC-EuIak73AneP059c3PGPTSmIIXMGoiEEVW_Kzvjq26B8ICI9PRZ18zg5odumBAaCXb0atSJU6K2qGGce-3ppvgjc_ufu8qDnTqpIL2BzewzLzlyVnXDzRR3tjvZA8D2VuV4C-g_0-kbq3ZViSPz1z_mwYcmfCUA8DqAyAtaiA37wzLcnYU6Pot_1rkzKIkS_QgDERw3gH_Ht7iSYrLdmGs8ISLtyJo3jeYj_1kPJWifQ17AP4bxoN7CGnT4gEFFPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میدل ایست آی : تونی بلر، نخست‌وزیر اسبق انگلیس، رسماً از تشکیلات خودگردان خواسته است نام «فلسطین» را از کتاب‌های آموزشی حذف و نام عبری «سامره» در این کتاب‌ها جایگزین شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/145280" target="_blank">📅 00:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145279">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
لودر کوماتسو لجستیک سپاه که مورد اصابت موشک آمریکایی قرارگرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/145279" target="_blank">📅 00:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145278">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رئیس‌جمهور مصر، السیسی: تایوان بخشی جدایی‌ناپذیر از چین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/145278" target="_blank">📅 00:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145277">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtgzVGHqbIpIEhNrbjBEgX2zLRK8E1VFN7rEWn18obyo3kr3lQB2akpgZVpxBdcDfgcumLPe0PsRuHkE69I2h779LXD2Be_abiuukvvkAjr40walUd5F6R7N-sq8mgRbkDxh3YPEZE7lxDMSGrYlZiESv7qmqs1EPe_F7OonGbuaEJxH_z63GFuffmHhHsTiZ-d-IMi4GDC90aWV-vARzKMzcRM0CXrr160gOQK5P9kigZnsEIwJTnYTFLWQ6jpSIQqtWi0e5dzURpWZWCLgi0CUNywrUU_OD3td68fC0Us6pT7A04_nj7umu5NueClK5RchRpda9BaGmi7ukZlgLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌ها حاکی از آن است که عبدالحمید الدبیبه، نخست‌وزیر دولت واحد ملی لیبی، دستگیر مصطفی الماجدوب، نخست‌وزیر خودخوانده لیبی که در ژنو در کنار اعضای دولت خود و سایر همراهانش فعالیت می‌کرد، را دستور داده است
🔴
محمد امهانی عبدالرحمن، عضو دولت الماجدوب، دستگیر شد
🔴
دولت تحت رهبری الماجدوب در بیانی‌ای از دستگیری محمد امهانی عبدالرحمن محکوم کرد و از سازمان ملل متحد خواست اقدام کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/145277" target="_blank">📅 00:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145276">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlU9LFgVN-voLsq6wp5XXG39fabTWjouuygrFMWgKjH7fbCpdadlGZujBjfxNX3J7BXGwEce8U5h6ehWFj9CPc6fhxLG1wMi_FzebHy3Foc3TdEJk7j_hGz-Ocm80fIHMOWOwMPP2AmE1Yxy1B52YOV9kMvTm4DxnDjS0Nk5Ixgw6iLOfUXA0fcYdQihxudOfC1L4w97WUTq62WS3CwfhgTR1jtQPoQ8HDj78YGFiILpFazKAYCjXDqR2yFXkfsTL7ZplWK92x1BtfO7MDMKR6FbWhtTzjB5zel_VkhwhXI3Aap-7K2P2ms1F3rwnZobh2Ez802o7GTiPFLHyYiQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید نقشه تنگه هرمز را منتشر کرده و اسم تنگه هرمز به «تنگه ترامپ» تغییر داده است. عکس ترامپ نیز وسط تنگه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/145276" target="_blank">📅 00:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145275">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKeOnd6Yo3EYni71xJ1cuX8yAGPE8lgl4MoronLeTVasjLlLHfoW3mWebilWBqZtM0lkFs7orRpbnMvzv6yU47Ka3PbMa48hrOPIK93gcaxScMqHCQ7BhIbDrSc38xvxKWYyg9LwQYsEaIkiLLKjuW8AF6wCijLzT_sqIqx44mqqH4B1uHas-e9Jn28xEuSYyunRJ6_iTQKRXs9pqPUJqpnqmSR6PmdF_WfF0ltBMpqnM_T9ehMJsrAcwkQV5f4kN_jrFbwarmvDDcouzhLORzL3a9XR9TlkN0Bg_MwLaedivLGQrz8LO1jOruldhdD_yrjSKjubhHEwmCSE5J6OMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
اپل مپز به تازگی اعلام کرده‌اند که نام دریاچه انتاریو را به دریاچه آمریکا تغییر داده‌اند، بنابراین اکنون آن تغییر بسیار مهم نام‌گذاری، بین گوگل مپز و اپل مپز، کامل، تصویب‌شده و الزام‌آور است
🔴
پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/145275" target="_blank">📅 23:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145274">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203ad1760d.mp4?token=GoVUukXysTTLnVrHE7NHw46HAiHD-dJ690ngL5BwZJVDtW3l-GM2zPjIeuybo88_eXjYMX3khUuuAB_pPoRkszxs70EuuX4slUmUq24zPrdVqkzCYBnMzYdm9_mN1iEdtaYkRBcVpf5eTM8d7qCOGFD142JSDFj2YaXHAZgQRb4ePBOrPiMzlzQq65IZZLo-bEtMV3uyyyezVCrr4L4uHOCyH8-4igkNACfIJDMmWd1ZKmf6Bifui3sfGFs_abyRpzpP2ku8h4lWADtFOb2-DLUQhvBy2MBXgXxk67t0w5CTPhTcUMgBE6wOj3u52-2sWjBmGPJrmqkZRNISfITryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203ad1760d.mp4?token=GoVUukXysTTLnVrHE7NHw46HAiHD-dJ690ngL5BwZJVDtW3l-GM2zPjIeuybo88_eXjYMX3khUuuAB_pPoRkszxs70EuuX4slUmUq24zPrdVqkzCYBnMzYdm9_mN1iEdtaYkRBcVpf5eTM8d7qCOGFD142JSDFj2YaXHAZgQRb4ePBOrPiMzlzQq65IZZLo-bEtMV3uyyyezVCrr4L4uHOCyH8-4igkNACfIJDMmWd1ZKmf6Bifui3sfGFs_abyRpzpP2ku8h4lWADtFOb2-DLUQhvBy2MBXgXxk67t0w5CTPhTcUMgBE6wOj3u52-2sWjBmGPJrmqkZRNISfITryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
راننده جنسیس که توی مشهد تجمعات رو زیر گرفته بود: عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/145274" target="_blank">📅 23:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145273">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
قیمت آیفون ۱۷ پرومکس ۲۵۶ گیگ به ۴۳۰ میلیون تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/145273" target="_blank">📅 23:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145272">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
دلیگانی نماینده مجلس : امارات باید کشورش را به عنوان غرامت به ما بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/145272" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145271">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رویترز: ونس و روبیو نگران تأثیر جنگ ایران بر شانس جمهوری‌خواهان در انتخابات میان‌دوره‌ای آمریکا هستند و به دنبال جلوگیری از تشدید درگیری تا پس از انتخابات می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/145271" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145270">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز گزارش داده هواپیمای حامل وزیر امنیت داخلی آمریکا و شماری از مقام‌های ارشد، پس از از کار افتادن یکی از موتورها، در حومه واشنگتن فرود اضطراری انجام داده است.
🔴
وزیر امنیت داخلی آمریکا گفته خلبانان گارد ساحلی با «حرفه‌ای‌گری کامل» هواپیما را با یک موتور سالم فرود آورده‌اند.
🔴
گزارشی از آسیب‌دیدگی سرنشینان منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/145270" target="_blank">📅 23:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145269">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85bf582674.mp4?token=mBxxd_m4CVj8s6JppWWDJ8F4Rze6nsUlOviOoJGIXvRptBgBIsoz227HWCUJBGFndBEkKDO0kg32xt4_6oBG2G6ww4JHduZcJ0DDmGhne4GjqsqiRUFvajV0oFn3Ot5Uc2QSjGBRFtT0A-kUeQ5WjqzZszLeYY4e7JmvId0dCN8WvC7PzrfDVlqujhOKJBROvGZDapPxjVnLe50G0roqzwtIokrOgaui0pHHfEuTw6Gu2uDDuDDksYhgQM42cZWcvUsYJngq0Ft1CEJaPf6NbItf5Jb_ncPQC64re4W4V3w9mSAVfPChXE12CgbDQRKrlaVnsw2A2rjjjRkFm3bsl0bpbqB3lT9A5pGmxsr13CmH5koLyDp4OptlO6CIERKVIoDslX3YwxWQXCljMHbBpYPOGvMLVSqNMUBgKcgz7NmqtXKHcmmBmOTgxwSK5QFWZLX72DFhqy4pd15lF9Pf6h1ofiWG_OcAeQ0YFb_n5bC7ebBfIP2V5xEYe89UdGSnvPAs81wfwPtZEfA8C8yvqd7k_cihQKNQ4dAgfruun6aQE1Vcocdoj5G8Tn2LtSWzoIzqu8q71xqPgSETOpOaF1K9DM4-JXRAuvit75xde_Zeq0ZIqp3Pq0kABDvYjpwKyymZu__ZdFetaB0ncS6AlcL3yZFsGO73FsO3dL2Oj1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85bf582674.mp4?token=mBxxd_m4CVj8s6JppWWDJ8F4Rze6nsUlOviOoJGIXvRptBgBIsoz227HWCUJBGFndBEkKDO0kg32xt4_6oBG2G6ww4JHduZcJ0DDmGhne4GjqsqiRUFvajV0oFn3Ot5Uc2QSjGBRFtT0A-kUeQ5WjqzZszLeYY4e7JmvId0dCN8WvC7PzrfDVlqujhOKJBROvGZDapPxjVnLe50G0roqzwtIokrOgaui0pHHfEuTw6Gu2uDDuDDksYhgQM42cZWcvUsYJngq0Ft1CEJaPf6NbItf5Jb_ncPQC64re4W4V3w9mSAVfPChXE12CgbDQRKrlaVnsw2A2rjjjRkFm3bsl0bpbqB3lT9A5pGmxsr13CmH5koLyDp4OptlO6CIERKVIoDslX3YwxWQXCljMHbBpYPOGvMLVSqNMUBgKcgz7NmqtXKHcmmBmOTgxwSK5QFWZLX72DFhqy4pd15lF9Pf6h1ofiWG_OcAeQ0YFb_n5bC7ebBfIP2V5xEYe89UdGSnvPAs81wfwPtZEfA8C8yvqd7k_cihQKNQ4dAgfruun6aQE1Vcocdoj5G8Tn2LtSWzoIzqu8q71xqPgSETOpOaF1K9DM4-JXRAuvit75xde_Zeq0ZIqp3Pq0kABDvYjpwKyymZu__ZdFetaB0ncS6AlcL3yZFsGO73FsO3dL2Oj1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده در ناتو، متیو ویتاکر
:
روسیه در حال حاضر در اوکراین گرفتار شده است. آن‌ها نمی‌توانند پیشرفتی در جبهه داشته باشند و بنابراین تهدید آن‌ها علیه ناتو در کوتاه‌مدت پایین است.
🔴
با این حال، آن اقدامات تهاجمی، آن حمله به اوکراین و الحاق قبلی کریمه، ما را به این باور می‌رساند که روسیه غیرقابل پیش‌بینی است و ممکن است حاضر به انجام اقداماتی علیه یک کشور عضو ناتو باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/145269" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145268">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f1fb5173.mp4?token=NFxPkwhGW1qV99PiBfhHNcq3I7m5Rer2w7Uuj37iCsb0lLvlBubLQQZvWemN1xCi9lTwEsCQqL2mAkBzXJEbr61a201RyrMLy-xgzjnroBRY6jqaWp-5O7JGTS-6ar3WBIwnadPjmne_KNxz0z3xFOn0YFW0eRm9MKDGJzy6a7S6huVa6KtvjASKniP-aG9pDgmbNCtG2sGYwlYokdspRbO81PONX-Q_QcjFkPwup5WCG0uVimxxW9wf2UKie6YuiBuNicGIMq4kpAZ0x-zl7p1xGlTau0pdfHTAfdQhUP2ZMzv-_BM1LpVWH0vvN5vGIbl4ZLaZiPhIlHefN7p-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f1fb5173.mp4?token=NFxPkwhGW1qV99PiBfhHNcq3I7m5Rer2w7Uuj37iCsb0lLvlBubLQQZvWemN1xCi9lTwEsCQqL2mAkBzXJEbr61a201RyrMLy-xgzjnroBRY6jqaWp-5O7JGTS-6ar3WBIwnadPjmne_KNxz0z3xFOn0YFW0eRm9MKDGJzy6a7S6huVa6KtvjASKniP-aG9pDgmbNCtG2sGYwlYokdspRbO81PONX-Q_QcjFkPwup5WCG0uVimxxW9wf2UKie6YuiBuNicGIMq4kpAZ0x-zl7p1xGlTau0pdfHTAfdQhUP2ZMzv-_BM1LpVWH0vvN5vGIbl4ZLaZiPhIlHefN7p-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متیو ویتاکر، سفیر ایالات متحده در ناتو، درباره ایران:
به عنوان یک کشور ورشکسته، آن‌ها قادر نخواهند بود به هیچ‌کس در ارتش، هیچ‌کس در خدمات مدنی، یا هیچ‌کس در دولتشان حقوق بپردازند و نخواهند توانست از جامعه خود حمایت مالی کنند.
🔴
بنابراین قطعاً مردم ایران از وضعیت فعلی راضی نخواهند بود و باید مسئولیت آن را بر عهده دولت خود بدانند.
🔴
آن‌ها باید این رژیم را مقصر بدانند و قطعاً باید برای تغییر و یک مسیر متفاوت مطالبه‌گر باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/145268" target="_blank">📅 23:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سفیر آمریکا در ناتو: اقدام تهاجمی روسیه به اوکراین و الحاق کریمه باعث می‌شود ما به این نتیجه برسیم که مسکو می‌تواند غیرقابل پیش‌بینی باشد و ممکن است علیه یکی از کشور‌های ناتو دست به اقدام بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/145267" target="_blank">📅 23:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
به گزارش بلومبرگ، روسیه در آستانه زمستان پیش‌رو شرایط را برای دستیابی به پیشروی‌های قابل‌توجه در اوکراین مهیا کرده است.
🔴
هم‌زمان، نگرانی در اروپا نسبت به گسترش دامنه جنگ و سرایت آن به خارج از مرزهای اوکراین افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/145266" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4307eed19b.mp4?token=raShOdK3wJeNwy-SUyM-aekFQYKD09JeJeSaRA1f1PvZZl7YswO5tTYAscdVnn_IZH1yGdO3T2g3QnFdlTUKfwgL4WyjX4AWhmOQHL4weLPwpJPnrn9RIMZyddjcQfAs3dlw09JhiSVPnqyCVQlWjwpSuyv-uaNV7LwG-INcS1cDfgLRE1bf71BjMXOKfEO8Q1ICAhYo59jVXibdUUEalKTPNj1YNVE8BBXEI9hoIh_t1EjYDrhGSca_YIUsl8HHGHvjNyeNCX0jeNWkdeiqW8RR_lWjvEJKAK4yjiapJVD_Gzis4k1ORHWpWO5RVp3F_Lyda3jV799tR-6Eanct_K1g4tF4BZGhbEJxGoCeQXjzWWV_rqO4LXuZmaVB_ex-3d1ofxYjVvzQmoTGspmjfaN5QUWi94veogcyBtUFIO9lsrsfRllH7ekOvouu4F1mjDBrX-BsLsTVXJ8st1jObUDHkgRfdO08x9Ie4mUnncYJKO4Av_D4Zi3vwLkV2E944im_mizJP3bXNjO7O3eqkYV6Qf6iTswxz-NxOiqSNn0sYEP6W4UPl_oNwdrLoo5ulAlSm6ckfOpIzrlI_fQ0zMByZLut8iWRp0EPZ4xaZPE3i6exT0VPAdhh8vTvBt3q6FFf1bXjrSojhxX9qW8NTPqlFqk1PTye-LCZSDwAmIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4307eed19b.mp4?token=raShOdK3wJeNwy-SUyM-aekFQYKD09JeJeSaRA1f1PvZZl7YswO5tTYAscdVnn_IZH1yGdO3T2g3QnFdlTUKfwgL4WyjX4AWhmOQHL4weLPwpJPnrn9RIMZyddjcQfAs3dlw09JhiSVPnqyCVQlWjwpSuyv-uaNV7LwG-INcS1cDfgLRE1bf71BjMXOKfEO8Q1ICAhYo59jVXibdUUEalKTPNj1YNVE8BBXEI9hoIh_t1EjYDrhGSca_YIUsl8HHGHvjNyeNCX0jeNWkdeiqW8RR_lWjvEJKAK4yjiapJVD_Gzis4k1ORHWpWO5RVp3F_Lyda3jV799tR-6Eanct_K1g4tF4BZGhbEJxGoCeQXjzWWV_rqO4LXuZmaVB_ex-3d1ofxYjVvzQmoTGspmjfaN5QUWi94veogcyBtUFIO9lsrsfRllH7ekOvouu4F1mjDBrX-BsLsTVXJ8st1jObUDHkgRfdO08x9Ie4mUnncYJKO4Av_D4Zi3vwLkV2E944im_mizJP3bXNjO7O3eqkYV6Qf6iTswxz-NxOiqSNn0sYEP6W4UPl_oNwdrLoo5ulAlSm6ckfOpIzrlI_fQ0zMByZLut8iWRp0EPZ4xaZPE3i6exT0VPAdhh8vTvBt3q6FFf1bXjrSojhxX9qW8NTPqlFqk1PTye-LCZSDwAmIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور فرانسه، ماکرون: اگر اروپا می‌خواهد در رقابت باقی بماند، باید زنجیره‌های تولید را در اروپا منسجم کند.
🔴
باید رویکردی عمل‌گرایانه در قبال این رقبای بزرگ بین‌المللی توسعه دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/145265" target="_blank">📅 23:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145264">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063d19a17b.mp4?token=LCND03wgQ5h7fkih24CHBqKlvl1-CaEdyFBaTUsLus7YbK7NTJNJ5YnAnzlljzNcJpOAzxJeoFo1bbHvn02_Z89KmexQ4aTgw3U3PYzUa4myCSGupjuzP1sTsAtODtccgUbg8sx-ud9F0dD5r33qeVVInLvv-WOAN7VbNdQXZfF1Koz1c-m_0F6lKU1vhPPXRda1qGdmi5wXp3vajkVkg_LpmQaamybnk7L8Ae_KANH63_TE7p263Zp7JuEXNqaqy8UQkYvy9o6fkr-l6sKhbs0eSVXKKoYtYEnl8C4mbu3-2CtpJinWkAs2nGRQ5Ymr54dal6kURpR1izVHDWF6CRmDJGrLrWRf7JapqdnBXDB1tFOGXwCzdtFCIcQd7O9--ZVx3JIwAQ08w9aKZLs9lS5LMOy4qQeBGKhOOr_ZBdDQp84jEcGH-ee6jsy4aUa4bM4A7SjpeOibRN9Em7hOWFL38POYyfGzEKt8ROZDyXYDSVSbFv-Tuiow9CxsDXYU56aIu1dq9C4x-hvc94bhAj8kGt8IWqDozo656VFg8HFGaUxHrCt5PNvfh2gkwToxYt8uQ0FVkmPsdwpMbdxNZtne-NcgZLx6X1lpL0HGsoQ5n0K5r1kRi-7-AnBSMUF_NPpUU5YpST5WwQMc--GVtcwsDjDbTk-NuHahGbPFydM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063d19a17b.mp4?token=LCND03wgQ5h7fkih24CHBqKlvl1-CaEdyFBaTUsLus7YbK7NTJNJ5YnAnzlljzNcJpOAzxJeoFo1bbHvn02_Z89KmexQ4aTgw3U3PYzUa4myCSGupjuzP1sTsAtODtccgUbg8sx-ud9F0dD5r33qeVVInLvv-WOAN7VbNdQXZfF1Koz1c-m_0F6lKU1vhPPXRda1qGdmi5wXp3vajkVkg_LpmQaamybnk7L8Ae_KANH63_TE7p263Zp7JuEXNqaqy8UQkYvy9o6fkr-l6sKhbs0eSVXKKoYtYEnl8C4mbu3-2CtpJinWkAs2nGRQ5Ymr54dal6kURpR1izVHDWF6CRmDJGrLrWRf7JapqdnBXDB1tFOGXwCzdtFCIcQd7O9--ZVx3JIwAQ08w9aKZLs9lS5LMOy4qQeBGKhOOr_ZBdDQp84jEcGH-ee6jsy4aUa4bM4A7SjpeOibRN9Em7hOWFL38POYyfGzEKt8ROZDyXYDSVSbFv-Tuiow9CxsDXYU56aIu1dq9C4x-hvc94bhAj8kGt8IWqDozo656VFg8HFGaUxHrCt5PNvfh2gkwToxYt8uQ0FVkmPsdwpMbdxNZtne-NcgZLx6X1lpL0HGsoQ5n0K5r1kRi-7-AnBSMUF_NPpUU5YpST5WwQMc--GVtcwsDjDbTk-NuHahGbPFydM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام اعلام کرد که نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۸۶ کشتی تجاری را به مسیر دیگری هدایت کرده، ۳ کشتی را غیرفعال کرده و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کرده‌اند.
🔴
این آمار نسبت به به‌روزرسانی روز سه‌شنبه، ۲ کشتی بیشتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/145264" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145263">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
الجزیره: حتی تهدید مین‌های دریایی هم برای اختلال در تردد کشتی‌ها در تنگه هرمز کافی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/145263" target="_blank">📅 22:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145262">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت خارجه آمریکا با لحنی تند پیشنهاد حکومت طالبان برای سرمایه‌گذاری ایالات متحده در بخش معادن افغانستان را رد کرد.
🔴
تامی پیگوت، سخنگوی وزارت خارجه آمریکا در مصاحبه با شبکه «صدای آمریکا»، طالبان را بار دیگر یک گروه «دهشت‌افگن جهانی» خوانده و پیشنهاد این گروه را رد کرد.
🔴
پیگوت گفت، سرمایه‌گذاری در معادن افغانستان تحت حاکمیت طالبان، در نهایت منابع مالی بیشتری در اختیار این گروه قرار می‌دهد و می‌تواند به ادامه آنچه او «رفتار وحشتناک طالبان با مردم افغانستان» خواند، کمک کند.
🔴
او تاکید کرد که واشنگتن برنامه‌ای برای همکاری با طالبان در زمینه توسعه منابع معدنی افغانستان ندارد.
🔴
امیرخان متقی، وزیر خارجه طالبان اخیراً در مصاحبه‌ای با خبرگزاری ژاپنی «کیودو» اعلام کرد که این گروه در پی عادی‌سازی روابط با ایالات متحده است و دو طرف می‌توانند بر اساس احترام متقابل و منافع مشترک با یکدیگر تعامل داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/145262" target="_blank">📅 22:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145261">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دلار می‌ره بالا و خیلیا فکر می‌کنن خریدش حتماً پول درشت می‌خواد!
من خودم از «صراف» هر لحظه که بخوام، حتی با ۵۰ هزار تومن دلار می‌خرم. با ۳ تا مجوز رسمی و دفتر تهران، خیالمم از امنیتش کاملاً راحته.
اینم لینک ثبت‌نامش
👇
https://B2n.ir/bx3845</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/145261" target="_blank">📅 22:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145260">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ درباره ایران : به محض اینکه تمام شود، که فکر نمی‌کنم خیلی طول بکشد، نمی‌دانم چقدر بیشتر می‌توانند تحمل کنند.
🔴
من تحت تأثیر انتخابات نیستم. من کاندیدای انتخابات نیستم. حزب من کاندیداهای خود را معرفی کرده و من قصد دارم به حزبی‌ام کمک کنم.
🔴
فکر می‌کنم حزبی‌ام این واقعیت را محترم می‌شمارد که ما به ایران اجازه نمی‌دهیم سلاح هسته‌ای داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/145260" target="_blank">📅 22:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145259">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ درباره ایران : ما شب گذشته بسیار بیشتر از رادارشان را منفجر کردیم.
🔴
حمله شب گذشته بسیار سنگین بود و ما آماده‌ایم هر زمان که بخواهیم، حمله دیگری را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/145259" target="_blank">📅 22:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145258">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: تحت تاثیر انتخابات نیستم؛ من نامزد نیستم، حزبم در انتخابات شرکت می‌کند و حزبم درک می‌کند که نباید به ایران اجازه دهیم به سلاح هسته‌ای برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/145258" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145257">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=Hi5lgQawLf925rWvJBVRXNMaU0hYH8K2MgfdRVbJjvKg6QEgfRk46qwd-z7hav-DzV__BnQQ2F0LtA6YknUnWrgPkBAiXKO9Lah1xENlJWbSCGHjcVFwDHW5Tzwk8BKYEhCYXulpRBqianmoNmU5yx_JXMIDwxUuXRSMNMJSRhvpeiy2eFXIgBwGyZfWAwhl4GeHm-t19M2qbrdXU67N_A7fuZkHl83YAY4hdU9jNmYllLMepycooLkqCu1vXsdTtVR7MFy1lEAcjmq6sIlAMdN1iVznvwSz5hifTLTTizzAXj-13NemigJMfnkD1Lr-IonZtRBrpMl9ZpE5WPN1Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=Hi5lgQawLf925rWvJBVRXNMaU0hYH8K2MgfdRVbJjvKg6QEgfRk46qwd-z7hav-DzV__BnQQ2F0LtA6YknUnWrgPkBAiXKO9Lah1xENlJWbSCGHjcVFwDHW5Tzwk8BKYEhCYXulpRBqianmoNmU5yx_JXMIDwxUuXRSMNMJSRhvpeiy2eFXIgBwGyZfWAwhl4GeHm-t19M2qbrdXU67N_A7fuZkHl83YAY4hdU9jNmYllLMepycooLkqCu1vXsdTtVR7MFy1lEAcjmq6sIlAMdN1iVznvwSz5hifTLTTizzAXj-13NemigJMfnkD1Lr-IonZtRBrpMl9ZpE5WPN1Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
دیروز شب یک حمله بسیار سنگین بود و ما آماده‌ایم هر زمان که بخواهیم حمله دیگری را انجام دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/145257" target="_blank">📅 22:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145256">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4657840e2.mp4?token=pTy60mY9vJdw8XU7QjWk84uMd3LyIuSGY6gsewU37F5BRkGkplxF6WQHRNCY5ky2NqU9Z3Y7iF8-qnmpTrf9Er-o69EIqVSBCQpmsxPZrvFIJU42qw7eHX0qE-MeVOlDnfPg56CxXVeaSirdGhjZPMIIBAAMtt0-_rfiVT0caGt12rfX7WgAMPS0Ub33QyKhvCA4ztbeHv0MSNcOoB5itqudYivKxmho5TRw6Awk49Vd34YwiEoHh2fpcLG38BzlPKLXdFnJmNFywFp8Ecdnz3YlznZI5EjJ_EXaJWubWeKEj-MYKDTiina3UpiaTdwCS9WxQTq51DcsYZqVRs6tLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4657840e2.mp4?token=pTy60mY9vJdw8XU7QjWk84uMd3LyIuSGY6gsewU37F5BRkGkplxF6WQHRNCY5ky2NqU9Z3Y7iF8-qnmpTrf9Er-o69EIqVSBCQpmsxPZrvFIJU42qw7eHX0qE-MeVOlDnfPg56CxXVeaSirdGhjZPMIIBAAMtt0-_rfiVT0caGt12rfX7WgAMPS0Ub33QyKhvCA4ztbeHv0MSNcOoB5itqudYivKxmho5TRw6Awk49Vd34YwiEoHh2fpcLG38BzlPKLXdFnJmNFywFp8Ecdnz3YlznZI5EjJ_EXaJWubWeKEj-MYKDTiina3UpiaTdwCS9WxQTq51DcsYZqVRs6tLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
بسیاری از افراد می‌پرسند، با چه کسی سخت‌تر است معامله کرد؟ آیا چین است؟ ویتنام؟
🔴
در واقع، کانادا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/145256" target="_blank">📅 22:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145255">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3af85c20.mp4?token=gyeNDR1aks-fTr7Qvru_ELFJ9Zaps0VWUHMLafXmi2RhDCXWCo-DPPFncVimci1CbDmoLKONoVzTc7zdwwlNaeXN_H8-VF0AceIO7f5PfiYHAh0Ma1ggDQMti1G5nEA2SlnljuYD3WNgloUX9h1v8qW_-bKkwm1uUQGcPz3ycvOFUIi2YIE2Polg1OvXPqIhoXvs6r1g6rHW3Xny6wZ88wA0IE26yaWYZFQSKLbUfBxs9mY1AmTbm4z0lxIMGnjjcVWU98Ewm1wzY6Twraj3nXH6-Uukd6TavkgaLF1OlXYCNe7CxXEx-FNQBXjK7QsAwcalyaeiT1v1DxK6VjTNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3af85c20.mp4?token=gyeNDR1aks-fTr7Qvru_ELFJ9Zaps0VWUHMLafXmi2RhDCXWCo-DPPFncVimci1CbDmoLKONoVzTc7zdwwlNaeXN_H8-VF0AceIO7f5PfiYHAh0Ma1ggDQMti1G5nEA2SlnljuYD3WNgloUX9h1v8qW_-bKkwm1uUQGcPz3ycvOFUIi2YIE2Polg1OvXPqIhoXvs6r1g6rHW3Xny6wZ88wA0IE26yaWYZFQSKLbUfBxs9mY1AmTbm4z0lxIMGnjjcVWU98Ewm1wzY6Twraj3nXH6-Uukd6TavkgaLF1OlXYCNe7CxXEx-FNQBXjK7QsAwcalyaeiT1v1DxK6VjTNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چقدر جدی هستید در مورد تغییر نام تنگه هرمز به «تنگه ترامپ»؟
🔴
ترامپ: من فقط این پیشنهاد را مطرح کردم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/145255" target="_blank">📅 22:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145254">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced80d268f.mp4?token=TfLlLd21yGCUDzHO_tLI8KnJSLJ9qncVZisaq1Phv3yrc8gv_p_BARnAxiD7ykfCMwRn8aCuDDdZHow6zQvclkM_QW6-CTiGPZKol-jSUlLAlQrZCu5XkTKVDHrDhNe9g5ypwnQCj-ZtULlmLZHjTTAm-q2UgQnOyobMJavWkUXoKAaY5X5ZcNj2dxPSR9i5DGQFBxSvFuu82t5FxuiRPscN0EiR_-NI43uD97RYut8TZ0o5kX3TV2ub6dT9XeE3GAd_ALsvbzVD-82vrcg362hIILwytuMpKX3L-IMFZyHPFMKJUGuFmafYtBzhuPnVdqRipByvlXyjaiBW4clTWkmRU7EhWLIJORk-eljyI55slMChVJUP3Kqg2vRKJrXo0VX0KQ3q4XqA2ghmSwMdjnu_uEP1sTwSmoDi5mSFUMsWAO7f_9nn5j8z193QDXHaVDWUZbkuMiYRoOGSSddj8dwQGKGmGeun2qRoY3rT72gVuoPCPa-dalgVwfId0ImCs_h0aLoWxrdRUxCnGaUMsFeo7EGu-aeQvmvcTzurArKtM_qHlkxxzPMFfMb6CGq-5rT-l8Y1Y_gLX7dfIS5lAqShInCgdRPTk0YW-6WKcHi-rn1muD3O3UlwXs4szgbKH27sei4TOleZ93YZ0nr__KFEc1vlLZ-gR76-PCdHgSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced80d268f.mp4?token=TfLlLd21yGCUDzHO_tLI8KnJSLJ9qncVZisaq1Phv3yrc8gv_p_BARnAxiD7ykfCMwRn8aCuDDdZHow6zQvclkM_QW6-CTiGPZKol-jSUlLAlQrZCu5XkTKVDHrDhNe9g5ypwnQCj-ZtULlmLZHjTTAm-q2UgQnOyobMJavWkUXoKAaY5X5ZcNj2dxPSR9i5DGQFBxSvFuu82t5FxuiRPscN0EiR_-NI43uD97RYut8TZ0o5kX3TV2ub6dT9XeE3GAd_ALsvbzVD-82vrcg362hIILwytuMpKX3L-IMFZyHPFMKJUGuFmafYtBzhuPnVdqRipByvlXyjaiBW4clTWkmRU7EhWLIJORk-eljyI55slMChVJUP3Kqg2vRKJrXo0VX0KQ3q4XqA2ghmSwMdjnu_uEP1sTwSmoDi5mSFUMsWAO7f_9nn5j8z193QDXHaVDWUZbkuMiYRoOGSSddj8dwQGKGmGeun2qRoY3rT72gVuoPCPa-dalgVwfId0ImCs_h0aLoWxrdRUxCnGaUMsFeo7EGu-aeQvmvcTzurArKtM_qHlkxxzPMFfMb6CGq-5rT-l8Y1Y_gLX7dfIS5lAqShInCgdRPTk0YW-6WKcHi-rn1muD3O3UlwXs4szgbKH27sei4TOleZ93YZ0nr__KFEc1vlLZ-gR76-PCdHgSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چه چیزی مانع از آن می‌شود که از ونزوئلا بخواهید تاریخ برگزاری انتخابات را تعیین کند؟
🔴
ترامپ: من فقط فکر نمی‌کنم که هنوز آماده باشند.
🔴
ما آن‌ها را از یک دیکتاتوری بیرون آوردیم. ما انتخابات می‌خواهیم. دلسی هم آن را می‌خواهد، اما آن‌ها هنوز آماده نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/145254" target="_blank">📅 22:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145253">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
خبرنگار: چقدر در مورد تغییر نام «تنگه هرمز» به «تنگه ترامپ» جدی هستید؟
🔴
ترامپ: به جون مادرم همین‌طوری گفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/145253" target="_blank">📅 22:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc96f06d0.mp4?token=g2vtE58mtmMIAZ2f_IsyX2zGb2AAbo5rkqRo5bV_03Mq075azJBkDumVXS0XTwZ0einjk3GfjQoZfFcu56Y-UjDU6mkciPODvVRy_rBqmmd7S5eaUslUE6aiqu_anry-wOFlSunRbcUrAiKPo_43P3cnH4Al2gdafnpuSccK5fvgefRWZqOeRsZriGGFdgRXqKhJVlle5WCU8O1nM4xWyDYvxLDBzXi50P0BUxtQoGUVHZHOapM4AvQPp-CfrQkOovTubHWr2nIpSw5ZhXsTVS01K24ZlTtFzSHrhz0dV7CeMjQRZm8Nnh0MfqBtSDsWK_a4802WvJp1Vn1x62Hjog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc96f06d0.mp4?token=g2vtE58mtmMIAZ2f_IsyX2zGb2AAbo5rkqRo5bV_03Mq075azJBkDumVXS0XTwZ0einjk3GfjQoZfFcu56Y-UjDU6mkciPODvVRy_rBqmmd7S5eaUslUE6aiqu_anry-wOFlSunRbcUrAiKPo_43P3cnH4Al2gdafnpuSccK5fvgefRWZqOeRsZriGGFdgRXqKhJVlle5WCU8O1nM4xWyDYvxLDBzXi50P0BUxtQoGUVHZHOapM4AvQPp-CfrQkOovTubHWr2nIpSw5ZhXsTVS01K24ZlTtFzSHrhz0dV7CeMjQRZm8Nnh0MfqBtSDsWK_a4802WvJp1Vn1x62Hjog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جنگ اوکراین
:
آن‌ها باید آن جنگ احمقانه را متوقف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/145252" target="_blank">📅 22:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145251">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29831a49d3.mp4?token=oTnffKFsLaQf80KoA5GonxiB87dO5FMEZuxChsOaSil5xo81F1XdeCQxB87IaFAXDpQOjljv9thsPgeEVeLg8aFkUYBuYx_jjK51VrE3Y5hqxiO-k6TQXMNeUs9QQ_Ypnbs6SoEmP74TIs4nhNk2O9bQiaMV3m9CC2ihl0ifvzucAG4c3guot1J3XpYzhCFmgdF2n4WdxWuhhle_BM53hra5HC_RYKupeQ4uNL42RRQR8fVbz3ILit--ownqzZ-xPt3eLKwqzCzbmuJEEEHgtFcXtcPEKuds414uhZf9r3mlutc_JXKWajJJga93JWWIkTQaHDW0L4KdOdKeCtfqTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29831a49d3.mp4?token=oTnffKFsLaQf80KoA5GonxiB87dO5FMEZuxChsOaSil5xo81F1XdeCQxB87IaFAXDpQOjljv9thsPgeEVeLg8aFkUYBuYx_jjK51VrE3Y5hqxiO-k6TQXMNeUs9QQ_Ypnbs6SoEmP74TIs4nhNk2O9bQiaMV3m9CC2ihl0ifvzucAG4c3guot1J3XpYzhCFmgdF2n4WdxWuhhle_BM53hra5HC_RYKupeQ4uNL42RRQR8fVbz3ILit--ownqzZ-xPt3eLKwqzCzbmuJEEEHgtFcXtcPEKuds414uhZf9r3mlutc_JXKWajJJga93JWWIkTQaHDW0L4KdOdKeCtfqTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره روسیه
:
ما می‌خواهیم روابط خوبی با روسیه، اوکراین و همه داشته باشیم.
🔴
این برای کسب‌وکار عالی خواهد بود. روسیه زمین‌های بزرگی دارد، زمین‌های بسیار ارزشمند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145251" target="_blank">📅 22:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765fb2cdb4.mp4?token=WeE96EuQ2AYmHFOlEg8WEcGwmXjSRxFDqvJW35JH_9KyKLR9voA528fp-O9EfgHzqTUIuxy0GO_UQ9Su0WDY9VxvBfrcIN3VQCAY0XgeVMYDBvnzu5lYxNe0yjLBhIEl8wakI6adXbeaQDP0cF5OAZ7HMXwIwSsJjwEi-uZH7Fwm845MjnfRdB36A7b9DfxPAPa67Px5QbKU_1eT6KrQs13MFKXwZ3tOqMPGlr2o9kJnKXUSv1B_TczK-rIHeMxjwwURUdewnQ0lS4xF6Aj3osk9axPwkEtIQtbWsxVc3vgU9pG6ibJdAwCaM1ipoEmG5fwtXZImKI5-qxmY6Pi8_WAmJjAWOnve_wC45SnWWabXfbHMBf26rHEN3CheYVZ6ZYoqKG7V-QAiAETkZ8NUwMmzhGjEjwfWGgNxaB8PYaF3_kDXH4dNsbUuF2uXFuOgzsXqaoxgMYkOZx8n9VjNSjmc0ATY5cxMd76tawQrN7aR2IEwjLQqPqUn1pxkLwKLvSZ05SAPDDH0eOKWYeGgUSfkhC1w_1UqVFnYUFCQXbzNaiK9_bpR7q90xeBFWi0VNVOK_bfdAuAFsqlwZY5Tice6IlB1SQ4NOAnlNtqCE_T4IsnYTHDrC6AmNVqm03A2cb5d0_nklKyDHEHXYNuB8zAjUMN1CktpjxiNqTjL3vY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765fb2cdb4.mp4?token=WeE96EuQ2AYmHFOlEg8WEcGwmXjSRxFDqvJW35JH_9KyKLR9voA528fp-O9EfgHzqTUIuxy0GO_UQ9Su0WDY9VxvBfrcIN3VQCAY0XgeVMYDBvnzu5lYxNe0yjLBhIEl8wakI6adXbeaQDP0cF5OAZ7HMXwIwSsJjwEi-uZH7Fwm845MjnfRdB36A7b9DfxPAPa67Px5QbKU_1eT6KrQs13MFKXwZ3tOqMPGlr2o9kJnKXUSv1B_TczK-rIHeMxjwwURUdewnQ0lS4xF6Aj3osk9axPwkEtIQtbWsxVc3vgU9pG6ibJdAwCaM1ipoEmG5fwtXZImKI5-qxmY6Pi8_WAmJjAWOnve_wC45SnWWabXfbHMBf26rHEN3CheYVZ6ZYoqKG7V-QAiAETkZ8NUwMmzhGjEjwfWGgNxaB8PYaF3_kDXH4dNsbUuF2uXFuOgzsXqaoxgMYkOZx8n9VjNSjmc0ATY5cxMd76tawQrN7aR2IEwjLQqPqUn1pxkLwKLvSZ05SAPDDH0eOKWYeGgUSfkhC1w_1UqVFnYUFCQXbzNaiK9_bpR7q90xeBFWi0VNVOK_bfdAuAFsqlwZY5Tice6IlB1SQ4NOAnlNtqCE_T4IsnYTHDrC6AmNVqm03A2cb5d0_nklKyDHEHXYNuB8zAjUMN1CktpjxiNqTjL3vY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: در اوکراین، مردم در خیابان‌ها ربوده می‌شوند. آیا آن ویدیوها را دیده‌اید؟ اگر آن‌ها را ندیده‌اید، آیا می‌توانم آن‌ها را برای کارکنان شما ارسال کنم؟
🔴
ترامپ: آن‌ها را نشان دهید و من آن‌ها را منتشر خواهم کرد. من از ویدیوها باخبرم. من به‌شدت درباره آن شنیده‌ام.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/145250" target="_blank">📅 22:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما کنترل تنگه هرمز را در دست داریم
🔴
آن‌ها تلاش می‌کردند موشکی بسازند که مین‌های دریایی را پرتاب کند. چه کسی چنین کاری می‌کند؟ من هرگز چنین چیزی نشنیده بودم، اما آن‌ها داشتند همین کار را انجام می‌دادند.
🔴
ما دیدیم که در حال ساخت آن بودند. ما هر کاری را که انجام می‌دهند، می‌بینیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145249" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ: کارزار جدید علیه ایران طولانی نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/145248" target="_blank">📅 22:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145247">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922e39bcdb.mp4?token=bhr5AvT6wp9zwH4L3JB8MOktn2B0QW2aeTySzbdNMzs5UhXfWAjztc6Q1y1DqYsKv1E9NNs8A2LQR-GWSoYpvWLhyAKrJNoTTGTWX-Y1l2lEY6SXQ-s2ZradoA5CD5YaTSy82SroJEP2X4C7nmShIEUFwiyW8NuJixSmiw4chM-gWkzJxjg_oGjC4gm1CbZRnmQ5XKjYVBnMnZxF3N3c_uDrB7a6xyU8F_ypoGh_V951gjIlt6Gc-rbpd2GyeiwjmVwDGqn3HUtH-Or7bgk7a8o124un8v7SF7QVlB4Hluw6MF-4E7JOGb54-D1teFGyG0g-BmHSnGzUwGjm07sGn3gfM-TNAJIx7IqB_4UDq362zIlfosUjxqJqVlsiRh590u9AbVuZpJ96wNuOBUDgbk_MZzlLERjAoc2GRIbvZWafYMuF-K9LW7zDPEBkh0VSMzj_Rb227zeT1dZRhJFRwM8oKNnyMNB8SBdM-04l2EudoVRx8XSfwqUWZUjv2eomlIN-DnstkU1dpQZ9B47I768oIzAinx1488r4ENVlcEfg8-yTPArwMeLAWeIFk29UHdh76JSQbNqBnSBF5ZqMxlEjpYe8f8ZSswlVDw--L3dB2acwATqv84QCho5N3_cYQktP7iB-5Nk1Owb8EJYfoomMwHPlb3P5JKbeCH888OI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922e39bcdb.mp4?token=bhr5AvT6wp9zwH4L3JB8MOktn2B0QW2aeTySzbdNMzs5UhXfWAjztc6Q1y1DqYsKv1E9NNs8A2LQR-GWSoYpvWLhyAKrJNoTTGTWX-Y1l2lEY6SXQ-s2ZradoA5CD5YaTSy82SroJEP2X4C7nmShIEUFwiyW8NuJixSmiw4chM-gWkzJxjg_oGjC4gm1CbZRnmQ5XKjYVBnMnZxF3N3c_uDrB7a6xyU8F_ypoGh_V951gjIlt6Gc-rbpd2GyeiwjmVwDGqn3HUtH-Or7bgk7a8o124un8v7SF7QVlB4Hluw6MF-4E7JOGb54-D1teFGyG0g-BmHSnGzUwGjm07sGn3gfM-TNAJIx7IqB_4UDq362zIlfosUjxqJqVlsiRh590u9AbVuZpJ96wNuOBUDgbk_MZzlLERjAoc2GRIbvZWafYMuF-K9LW7zDPEBkh0VSMzj_Rb227zeT1dZRhJFRwM8oKNnyMNB8SBdM-04l2EudoVRx8XSfwqUWZUjv2eomlIN-DnstkU1dpQZ9B47I768oIzAinx1488r4ENVlcEfg8-yTPArwMeLAWeIFk29UHdh76JSQbNqBnSBF5ZqMxlEjpYe8f8ZSswlVDw--L3dB2acwATqv84QCho5N3_cYQktP7iB-5Nk1Owb8EJYfoomMwHPlb3P5JKbeCH888OI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا شما سازمان سیا را برای مسلح کردن ایرانیان اعزام خواهید کرد؟
🔴
ترامپ: من نمی‌خواهم این را به شما بگویم، مناسب نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/145247" target="_blank">📅 22:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145246">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
🔴
@mahaneconomy
🔴
@mahaneconomy</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/145246" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145245">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: ما روزانه کشتی‌های متعددی را که حامل میلیون‌ها بشکه نفت هستند، از تنگه هرمز عبور می‌دهیم و در بیشتر موارد این کار را بدون مشکل انجام می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/145245" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145244">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
🔴
@mahaneconomy
🔴
@mahaneconomy</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/145244" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145243">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12570cf37a.mp4?token=WGUkKpL9zVZxN-cBHqL_0yMI-853-2vpbDHY-snPs51luIn_iqsUWdtLJKIOW_D9Q9pNdp2bcReLL51QTUJ0LS4kmZwBUrP_V8P-itxVL6KdlFaG5ALDmXPlsN3LxT7hso_dq6AKeX8e8_IyQ5KUFl43xxM7Q-vr-o0_WR1OIv3J5pbaqhajrcyMRyVT1MKrrLw-CQH-NQQ0kNZoayRpZf0QLJs-4XOIu5f55cljmj97b52_Ht0LYUGrt0ukw1M9cbqHyetesISNiErjsLF6jwTVB2ITOTnLUa1Q2k31qvcLFsaL8EoO1ZmZk1KU7XHfXmH1jqtyErzq3u95oEqamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12570cf37a.mp4?token=WGUkKpL9zVZxN-cBHqL_0yMI-853-2vpbDHY-snPs51luIn_iqsUWdtLJKIOW_D9Q9pNdp2bcReLL51QTUJ0LS4kmZwBUrP_V8P-itxVL6KdlFaG5ALDmXPlsN3LxT7hso_dq6AKeX8e8_IyQ5KUFl43xxM7Q-vr-o0_WR1OIv3J5pbaqhajrcyMRyVT1MKrrLw-CQH-NQQ0kNZoayRpZf0QLJs-4XOIu5f55cljmj97b52_Ht0LYUGrt0ukw1M9cbqHyetesISNiErjsLF6jwTVB2ITOTnLUa1Q2k31qvcLFsaL8EoO1ZmZk1KU7XHfXmH1jqtyErzq3u95oEqamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من نام یک دریاچه خاص را به دریاچه آمریکا تغییر دادم، درست مانند زمانی که نام خلیج مکزیک را به خلیج آمریکا تغییر دادم و مردم این کشور از آن خوششان می‌آید.
🔴
ما کارهایی از این دست را انجام می‌دهیم زیرا برای کشورمان می‌جنگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145243" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=Pyx9mn-6AaOfV9SATTiofr-1vbcqbi25RWuZDs15UK5crUabfUaYwIxA2McV-BSQSh_o4GwreDpvaV92o8hCEwhsCgSN7Bt2boYdClkZ7hvq7IeaNpvKpRMQJHHKu1fqcI1E9DhYhjr9jqYoF73E0wIc-j-WEkTXos5lxDKT5Z_V5SbEOsYOgTZPs5aJdRbYaJ3465EgsU6pQRrXMZuZQxCTLJi8SeSUssPvAFZ3kqGGf1QOLcCXAv7D3iRvwLZ6HsSVk7f4k1_1MZJrtp1ujDz21fY3eLpxWCn36Dqnn7GxFO-1Wo4Oljqq8Tz-2Tb787D1m0O8_ZZ9hQWWWhoMyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=Pyx9mn-6AaOfV9SATTiofr-1vbcqbi25RWuZDs15UK5crUabfUaYwIxA2McV-BSQSh_o4GwreDpvaV92o8hCEwhsCgSN7Bt2boYdClkZ7hvq7IeaNpvKpRMQJHHKu1fqcI1E9DhYhjr9jqYoF73E0wIc-j-WEkTXos5lxDKT5Z_V5SbEOsYOgTZPs5aJdRbYaJ3465EgsU6pQRrXMZuZQxCTLJi8SeSUssPvAFZ3kqGGf1QOLcCXAv7D3iRvwLZ6HsSVk7f4k1_1MZJrtp1ujDz21fY3eLpxWCn36Dqnn7GxFO-1Wo4Oljqq8Tz-2Tb787D1m0O8_ZZ9hQWWWhoMyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مقامات جمهوری اسلامی:
ما همه چیزهایی را که آن‌ها انجام می‌دهند می‌بینیم.
🔴
آن‌ها حتی نمی‌توانند بدون اینکه ما ببینیم به دستشویی بروند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/145241" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145240">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری / ترامپ: آماده حمله دیگری به ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/145240" target="_blank">📅 21:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504db2064f.mp4?token=CW_JghVyzyHP-snkyFnyamz5Ysowr8jAjpvZJMS0qOQRqp5laxckCLfVROuSZft6eY1IsoMKg3M478Qd90v77mqoFHK8EWJp4xOYHJ_StCz2hIiV-9dOPGFPJtxldjIiPUdPqW34kTRYtAbI84MzHzI0FP1Dlvbp6Xa5mLHt_9cmflVl9g72ZSb6s0ITnDpn6COLdlhgd72dPEgGpXbY30YWOpdeSVP3fwV-2fh49EFX-TFV4c7HJizpYAaO_Mz5IHimM1eRS-XjlVlppHhMTkGoRKxDgpyauzA_xfXM2TyxLDNu_k8B0tfCGFCdKtIeFxa6gCqhGI80Ujteg-Y0KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504db2064f.mp4?token=CW_JghVyzyHP-snkyFnyamz5Ysowr8jAjpvZJMS0qOQRqp5laxckCLfVROuSZft6eY1IsoMKg3M478Qd90v77mqoFHK8EWJp4xOYHJ_StCz2hIiV-9dOPGFPJtxldjIiPUdPqW34kTRYtAbI84MzHzI0FP1Dlvbp6Xa5mLHt_9cmflVl9g72ZSb6s0ITnDpn6COLdlhgd72dPEgGpXbY30YWOpdeSVP3fwV-2fh49EFX-TFV4c7HJizpYAaO_Mz5IHimM1eRS-XjlVlppHhMTkGoRKxDgpyauzA_xfXM2TyxLDNu_k8B0tfCGFCdKtIeFxa6gCqhGI80Ujteg-Y0KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جمهوري اسلامي : آن‌ها وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند.
🔴
آن‌ها دقیقاً از بین چشم‌هایشان به آن‌ها شلیک می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/145239" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145238">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891d8a84ce.mp4?token=S2bGhaVjd2aYYQE8w6H7ajCFjlM35jJmaXUyte0ySgDPcfy6AdQ8NzP7mK0Ed6R3DFIAYdJZdFaedUwkhD8KwQL3C6K51kviUDbzzpiFQRcib5TkLoCVbgLTTUoFThT0Uamm3-6CY-stYFpXXSOv0oxEpIjuhP8YNPOs2aBTt1OAQmqP6kQBoD-Tw6_XZBFVb5xt_Q5FCJIR5bZsX_OW0Km-xAixThVV2q8FMYutviES_ppsgOuXM6m4bYH9wYGXrkSvpA2TNk_OLahVMXczydcWxWVhsexd22CWu_avGLoKCB8iPBX7C3pOZNoTck_pXZQEmNWhMbjkgXaqIhm-k7k4Qo3t-YO8x5o4XkfWy1I-jD63VnZO0XVmbO-MiLFunewHaNr4ruWgbcdDSCwUpMCTcEMzWByIgeoSTOyOVVZIBtcZeBE8YI8XMjGzdANKFSclC0fxrn1hxMVESpU_v4ResT3eCpRPVW1dN7Uq9Q4Txw77a_039Ggm0FMD_HmNTMsaCWKdTWh9IvvwJKoQw7w6VtXH_VvWFirJ2yMZijhJzZdL4O2xFhf7DQbW9wrvtDKqDmoQCQVNpmpivD-C9TenMzao9UiEEGv-t29M3ve2GH3xZBVv7_17nGILAZJ1TnCWtp39tdBSNIVXbFq914UiFkOmIU9XFBVYa6RZ2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891d8a84ce.mp4?token=S2bGhaVjd2aYYQE8w6H7ajCFjlM35jJmaXUyte0ySgDPcfy6AdQ8NzP7mK0Ed6R3DFIAYdJZdFaedUwkhD8KwQL3C6K51kviUDbzzpiFQRcib5TkLoCVbgLTTUoFThT0Uamm3-6CY-stYFpXXSOv0oxEpIjuhP8YNPOs2aBTt1OAQmqP6kQBoD-Tw6_XZBFVb5xt_Q5FCJIR5bZsX_OW0Km-xAixThVV2q8FMYutviES_ppsgOuXM6m4bYH9wYGXrkSvpA2TNk_OLahVMXczydcWxWVhsexd22CWu_avGLoKCB8iPBX7C3pOZNoTck_pXZQEmNWhMbjkgXaqIhm-k7k4Qo3t-YO8x5o4XkfWy1I-jD63VnZO0XVmbO-MiLFunewHaNr4ruWgbcdDSCwUpMCTcEMzWByIgeoSTOyOVVZIBtcZeBE8YI8XMjGzdANKFSclC0fxrn1hxMVESpU_v4ResT3eCpRPVW1dN7Uq9Q4Txw77a_039Ggm0FMD_HmNTMsaCWKdTWh9IvvwJKoQw7w6VtXH_VvWFirJ2yMZijhJzZdL4O2xFhf7DQbW9wrvtDKqDmoQCQVNpmpivD-C9TenMzao9UiEEGv-t29M3ve2GH3xZBVv7_17nGILAZJ1TnCWtp39tdBSNIVXbFq914UiFkOmIU9XFBVYa6RZ2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
تا سه ماه پیش، ۵۲,۰۰۰ معترض ایرانی کشته شده بودند. و حالا می‌شنوم که احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم به این تعداد اضافه شده است.
🔴
تقریباً ۶۵,۰۰۰ معترض کشته شده‌اند. تنها پاسخ این است که به آن‌ها شلیک شده است.
🔴
رژیم هر روز ضعیف‌تر می‌شود و در نهایت به جایی خواهند رسید که دیگر نمی‌توانند به‌راحتی شلیک کنند، زیرا فکر می‌کنم مردم دیگر این موضوع را تحمل نخواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/145238" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145237">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36fc6764c.mp4?token=eSHc-jRj_j8_bY-QCbMZq-2DAe9iEmHgdh0Ks3GwVUmjaiYNNn2WFg0fnadPys3KXAUuI9acMhcDvEcI7DvU8kOTu4QbxLhI73mVFAzR80VXxxs10oxTZZYgq1q9oC_6kXK-oB4mmHcjD9EOzADUGB6yuMuTMU09GhE1rozZyugtLKpLv_1Q4tkPWE2VzbniwnQoTHefPx0jciHdXQDQoazgm45ElYB0Ctrlm5JJ6L_DcKJ_o-s5uAF8Rjh8jbqEd4D4Y1xTxOL4EsYtbcEf9l676E3JkyBhxRY48n3nvrk7CyRTmCP7_pm4tj53qdZgXPEsWLjoPRLfEy_esq08KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36fc6764c.mp4?token=eSHc-jRj_j8_bY-QCbMZq-2DAe9iEmHgdh0Ks3GwVUmjaiYNNn2WFg0fnadPys3KXAUuI9acMhcDvEcI7DvU8kOTu4QbxLhI73mVFAzR80VXxxs10oxTZZYgq1q9oC_6kXK-oB4mmHcjD9EOzADUGB6yuMuTMU09GhE1rozZyugtLKpLv_1Q4tkPWE2VzbniwnQoTHefPx0jciHdXQDQoazgm45ElYB0Ctrlm5JJ6L_DcKJ_o-s5uAF8Rjh8jbqEd4D4Y1xTxOL4EsYtbcEf9l676E3JkyBhxRY48n3nvrk7CyRTmCP7_pm4tj53qdZgXPEsWLjoPRLfEy_esq08KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
آمریکای جنوبی از چپ به راست رفته است.
🔴
ما رابطه خوبی با برزیل داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/145237" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145236">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: حکومت ایران هر روز ضعیف‌تر می‌شود و در نهایت دیگر نخواهند توانست به‌راحتی شلیک کنند.
🔴
مردم دیگر این وضعیت را تحمل نخواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/145236" target="_blank">📅 21:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145235">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=AtfJ1JDRRERKmRRtl25oxv2dom42XFBASB82NUGMylKBYFuP9phK8wwlrtNeOOxZPuon4Pm2lQrnwF-vTtfr6zgiYmrbtKbHDdiBG0E-VREMKleGcyvkxw8gmYtoPAbyE_v5TeSl4gbWsvdjedCTk-IsNLW5y88wqLJA1V6iQB19gDmIe-hx0iyC6rsQ7wUh6qfCBZBko0jILYtvQiTzfKc7J3KeVV-GwoY97c140MwYzuBZ80Kv4xoxPDrgHHPs0b9CTFQuZ919hokRh9xzoQu13Ec-9YQ2TiRq6sCr8MLf6nh5s58lDWK39NC71fxlCfzK0J9ibKAHQiGUzGtsgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=AtfJ1JDRRERKmRRtl25oxv2dom42XFBASB82NUGMylKBYFuP9phK8wwlrtNeOOxZPuon4Pm2lQrnwF-vTtfr6zgiYmrbtKbHDdiBG0E-VREMKleGcyvkxw8gmYtoPAbyE_v5TeSl4gbWsvdjedCTk-IsNLW5y88wqLJA1V6iQB19gDmIe-hx0iyC6rsQ7wUh6qfCBZBko0jILYtvQiTzfKc7J3KeVV-GwoY97c140MwYzuBZ80Kv4xoxPDrgHHPs0b9CTFQuZ919hokRh9xzoQu13Ec-9YQ2TiRq6sCr8MLf6nh5s58lDWK39NC71fxlCfzK0J9ibKAHQiGUzGtsgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اگر می‌خواهید مردم ایران قیام کنند، آیا سی‌آی‌ای را برای تسلیح ایرانیان می‌فرستید؟
🔴
پرزیدنت ترامپ: نمی‌خواهم این را بگویم. گفتن آن مناسب نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145235" target="_blank">📅 21:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145234">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e112f19f61.mp4?token=AeORq944vWCFdk5pFzXIrpA3NS8jBHQFUuUKgBmnoks6WKqJ7lzLx6DTn0beCm4NAWVzf92eIjb6Qtt1tD98_p3v0UI0FLU-oPoyFcknO3SXHJpIbhgDOEBEU7_XNqoHNrHa__gVkYfpB2ou5dMSSeLmqbbZSg-_YJCtmc81DZv8N5An2eDIqH3YNzzdhBBsAuy1Xtu6PCNCR6JcSt8w0sg-qMN0vRbrzfQ26mPaIUhnqNP679RFuoiVqZDtR3OgyG3v-zCJfWBMJuiNbElp61ds1_dnDDY1fJVeii9D8B0yr9CzhVrOQLIE2nmW0LiWpDM2am2EjCWmsxV_bofFhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e112f19f61.mp4?token=AeORq944vWCFdk5pFzXIrpA3NS8jBHQFUuUKgBmnoks6WKqJ7lzLx6DTn0beCm4NAWVzf92eIjb6Qtt1tD98_p3v0UI0FLU-oPoyFcknO3SXHJpIbhgDOEBEU7_XNqoHNrHa__gVkYfpB2ou5dMSSeLmqbbZSg-_YJCtmc81DZv8N5An2eDIqH3YNzzdhBBsAuy1Xtu6PCNCR6JcSt8w0sg-qMN0vRbrzfQ26mPaIUhnqNP679RFuoiVqZDtR3OgyG3v-zCJfWBMJuiNbElp61ds1_dnDDY1fJVeii9D8B0yr9CzhVrOQLIE2nmW0LiWpDM2am2EjCWmsxV_bofFhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو از غزه بازدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/145234" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145233">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نتانیاهو: به عنوان منطقه‌ای که هیچ‌کس حتی به فکر حمله به ما نمی‌افتد، زیرا ما از منظر امنیتی با کنترل مطلق بر آن مسلط هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/145233" target="_blank">📅 21:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145232">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">پایان بازی
استقلال 1-1 پرسپولیس
@AloSport</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/145232" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145231">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
آژانس اتمی: ما ناتوانی خود را در تأیید عدم انحراف مواد هسته‌ای ایران به سمت اهداف نظامی تأیید می‌کنیم/ فعالیت منظم خودروها را در ورودی تونل اصفهان که اورانیوم با غنای ۶۰ درصد در آنجا ذخیره می‌شود، شناسایی کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/145231" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145230">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
پاکستان: تفاهم‌نامه اسلام‌آباد همچنان چارچوبی عملی برای گفت‌و‌گو بین آمریکا و ایران باقی مانده
🔴
این سؤال مطرح نیست که این تفاهم‌نامه زنده است یا مرده یا نیمه‌مرده؛ این تفاهمنامه برای صلح وجود دارد
🔴
همچنان امیدواریم وقتی تشدید تنش به پایان رسید، طرفین به میز مذاکره بازگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/145230" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
