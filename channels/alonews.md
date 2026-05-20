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
<img src="https://cdn4.telesco.pe/file/GH370c3CoXfxxNOC_9z81wb50K6ayQ_3evKGfxtXiDv1_rvqF-b45Yp-8xjtB9z0ruJAaI_DXJzQ6eMQ17ZkyaSyaWwhkgDuOD5fM7wjVsDJbyampl6_ofJUxN1Le77qIgppXOXodv5EYvJ9iRqztQKo8fQ_QGb_y9ZG0468Ysn-5pz78RGerWQyZGEsyIOZT1HzQjeSWt5fgXcUMUNixH-QgoPuDbwfHcuf3cc_GjdtQg2TcXJudnGiKqmwH8s5lkFIg41KqgDktoxHjiAV7nvRjKt6klU0k5nMk24fo1qYnVq0-GJ6IZdMFVUbtVvvG_4QOcJ-YEtKS_RjIumGtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 945K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 21:07:19</div>
<hr>

<div class="tg-post" id="msg-121383">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در این مرحله متمرکز هستیم بر خاتمه جنگ در همه جبهه‌ها، از جمله لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/alonews/121383" target="_blank">📅 21:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121382">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
طبق گزارش کانال ۱۵ اسرائیل به نقل از منابع، پیشرفت‌هایی در پیش‌نویس یادداشت تفاهم و اصول بین ایران و ایالات متحده وجود دارد، اگرچه شکاف‌هایی باقی مانده است.
🔴
در همین حال، اسرائیل هماهنگی نظامی با آمریکایی‌ها را در پیش‌بینی حمله احتمالی ترامپ حفظ می‌کند، به طوری که نتانیاهو مستقیماً با ترامپ صحبت می‌کند و گفت‌وگوها در سطح نظامی با سنتکام ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/alonews/121382" target="_blank">📅 21:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121381">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQjYH5vVTzBlyTSYUWeNLe03o81kfnZPYk15pmdKNNiUDSRTdL67_P1oC-aBkMJ4f5UtyNrWnwwl5Ow_C7fa96MZaZwoeX1P3g1xstWC9iD4QwtlG0OqPcxBXbRhHdeIKxK6hd6z2I5MfzYXyJmuPwtATvZE3VHKsazFPIHgrUfErKcVU7xZzInoD3Bn8hX5SWo3hxe46FqzQ36kuUGNZL3mtNGd_Bp3LJaR-882uncmqS1oQ9qMtrJSpjFSDiULJ5h3TJORY-gORsbOOUWNc8mIphvqgOevXzVa5bfaGGDt2REc-VxwjvcLdXjMxF3E5WNY_mhTj3qAgrkt2-TjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش رئیس کمیسیون امنیت ملی در پاسخ به حرفای به ترامپ: ایران شگفتی‌های زیادی برای آمریکا دارد؛ برای هر سناریو آماده هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/alonews/121381" target="_blank">📅 20:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121380">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et2PRqFjZHB0AaVtRNHzccumAgEOb0TRwad0Iq_mHel0eAwVJzzB5jQHMCkNdQBMbRo4_ad1se_dXO2DYdGDJzxn934X2pRKKYRRKJGF3D9lpW9Ylyr3A30VqD32i4CrbWNyriEU6B5hMX5HTXwC_h0FX5JEMfPxSv0iFgYPLGXZSCGpc3PBIlDWjR-x-bc8Q1v2gZ96g84C_Y1Yt_VifXHv2ZVMV8U6wQt0knFqvSHfo-L1BFhKqCLl4f7G01tG0bkB834NIOpQkgXYIN8ojP8mzrb5p3LsBd4ZbQmBmYXzUjyvGPQT__O1rMq2EINv0UgLDhLn1fiMCShbL2kTnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور لیندزی گراهام: شنیده‌ام که فیلد مارشال پاکستان ممکن است به ایران سفر کند - چه چیزی ممکن است اشتباه پیش برود؟! شاید او وضعیت هواپیماهای نظامی ایران را که در پایگاه‌های هوایی پاکستان مستقر هستند، گزارش دهد؟
🔴
مانند بسیاری دیگر، من از نزدیک شاهد اتفاقات مربوط به تلاش دیگری برای دستیابی به توافق با رژیم ایران هستم. برای همه افراد درگیر آرزوی موفقیت واقعی دارم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/alonews/121380" target="_blank">📅 20:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121379">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یه مقام ارشد اسرائیلی : اطرافیان ترامپ دارن روش فشار میارن که به توافق برسه
🔴
نتانیاهو هم باهاش درباره این موضوع صحبت کرده، و از نظر ترامپ گزینه حمله وجود داره که فقط بحث زمانشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/alonews/121379" target="_blank">📅 20:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121378">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سازمان رادیو و تلویزیون اسرائیل: نتانیاهو تلاش می‌کند تا ترامپ را به دادن چراغ سبز برای ازسرگیری حملات به ایران متقاعد سازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/alonews/121378" target="_blank">📅 20:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121377">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
اکسیوس گزارش می‌دهد که رئیس جمهور ترامپ و نخست وزیر نتانیاهو دیشب تماس تلفنی پرتنشی داشتند و در مورد مسیر پیش رو در مورد ایران اختلاف نظر داشتند.
🔴
طبق گزارش‌ها، سفیر اسرائیل در واشنگتن به اعضای کنگره گفته است که نتانیاهو از مکالمه مربوطه خارج شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/alonews/121377" target="_blank">📅 20:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121376">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده :
اوایل امروز در خلیج عمان، تفنگداران دریایی ایالات متحده از واحد ۳۱ اعزامی دریایی، نفتکش M/T Celestial Sea با پرچم ایران را که مظنون به تلاش برای نقض تحریم‌های ایالات متحده با حرکت به سمت یک بندر ایرانی بود، توقیف کردند.
🔴
نیروهای آمریکایی پس از بازرسی کشتی و دستور تغییر مسیر به خدمه، آن را آزاد کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/alonews/121376" target="_blank">📅 20:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121375">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: اگر روند [مذاکرات] بر اساس مطالبات به‌حق ایران پیش برود، می‌توانیم بگوییم که دیپلماسی توفیق داشته است.
🔴
در غیر این صورت، اگر طرف مقابل کماکان اصرار کند بر زیاده‌خواهی و خواسته‌های نامشروعش، قاعدتاً توفیقی نخواهیم داشت
🔴
همان‌طور که مقام‌های مختلف کشور نیز اعلام کرده‌اند، از جمله رئیس محترم هیئت مذاکره‌کننده، دکتر قالیباف، ما برای هر سناریویی باید همواره آماده باشیم؛ در عین اینکه دیپلماسی هم، به‌عنوان ادامه مبارزه مردم ایران برای احقاق حقوق و منافع ملی‌شان، باید حداکثر استفاده را از آن ببریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/alonews/121375" target="_blank">📅 20:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121374">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
واکنش سخنگوی وزارت خارجه به تهدیدات اخیر ترامپ: اولتیماتوم‌ها در برابر ایران مضحک است
✅
@AloNwws
خبر جنگ</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/alonews/121374" target="_blank">📅 20:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121373">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: درحال بررسی نقطه نظرات تیم آمریکایی هستیم و حضور تیم پاکستانی برای تسهیل این پیام هاست
🔴
استفاده از ادبیات «اولتیماتوم و ضرب‌الاجل» علیه جمهوری اسلامی ایران مضحک است و چنین فشارهایی هرگز کارگر نخواهد بود.
🔴
ایران فارغ از رفتارهای تهدیدآمیز و انواع فشارهای سیاسی و نظامی، مسیر خود را برای تأمین منافع ملی و احقاق حقوق حقه خود با جدیت پیش می‌برد.
🔴
تمرکز اصلی تهران صرفاً بر اهداف و منافع ملی است و این‌گونه لفاظی‌های تهدیدآمیز تأثیری در تصمیم‌گیری‌ها و سیاست‌های کلان کشور ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/alonews/121373" target="_blank">📅 20:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121372">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: مقامات اسرائیلی معتقدند تقریباً هیچ شکافی بین اسرائیل و آمریکا در مورد خواسته‌های مطرح شده به ایران در مذاکرات جاری باقی نمانده است، اگرچه شک و تردیدهای عمده‌ای درباره اینکه آیا تهران واقعاً می‌تواند تحت فشار قرار گیرد تا آن‌ها را بپذیرد، وجود دارد.
🔴
ایران همچنان فقط به بخش‌هایی از پیشنهادات پاسخ می‌دهد و در مورد خواسته‌های باقی‌مانده تأخیر می‌کند، و اسرائیل مذاکرات را تلاشی از سوی تهران برای خرید زمان و کش دادن روند می‌داند. بازگشت احتمالی به اقدام نظامی به طور جدی در پس‌زمینه در نظر گرفته شده است و گفته می‌شود آماده‌سازی‌ها نیز در حال انجام است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/alonews/121372" target="_blank">📅 20:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121371">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6cb439e9d.mp4?token=ninHUS6OFYu4mt5p4s6hlapMy_7yzjJ1OGIa7P7jv6Qz7Tx4IDeNMpR5QMKEuC6VjzIlN_vp0gKibDFnMdiZ9GF_6FyECFyMn7lyI6vIFhX2CDFWHk-ncl7_4auC8oswRY1-quTfnYiGXWgRdyZ_W41evfp6KKLyZtVywf_AAVA3qB9K0cPFdp-zP1VxR_F0noH6WUisCLN-jFR3EHzEcebogEupUSghPGTYZSayclQs04ofR2mj0sb9jyuecCmLzZ4m-psiGkiRsXghD6y68h68aoC3XKNCfS-uhs8wb3ZWt6TBiUwIJLRqoNdevhnXo90iNYLS0xrEXHhh3tug-BkNzHoskJlQNFLzAlw5ozn7MR347_0WS26Se4_gG3gO3hpMxIOzx_Jr5MctYbE0rv2iq81bqSRnLL7Xh3CIJLcG-XAqhAnz1tjPfWm65yt0r0kkkJ1MLmiQWEHrhv2qe9Mv55XbBy7bSEVeETdq2OCEbjVVcMSUYhajSGiXMgVo6NpXkRg4IzSYrdLxrXFGCaiCo1LkRCxsPDe9qcRNPBLs0MF6DyYpETPig5nyomaILpNMTdXriOe0_YOiXi_chAuBvIHXP8IVnPabFWmNOlXAX3Y82oiG25Ye5SwfTTX83Cr1_iMXVXKGEj4_KKU39wmnQd1GRcRpSe4xV30aVXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6cb439e9d.mp4?token=ninHUS6OFYu4mt5p4s6hlapMy_7yzjJ1OGIa7P7jv6Qz7Tx4IDeNMpR5QMKEuC6VjzIlN_vp0gKibDFnMdiZ9GF_6FyECFyMn7lyI6vIFhX2CDFWHk-ncl7_4auC8oswRY1-quTfnYiGXWgRdyZ_W41evfp6KKLyZtVywf_AAVA3qB9K0cPFdp-zP1VxR_F0noH6WUisCLN-jFR3EHzEcebogEupUSghPGTYZSayclQs04ofR2mj0sb9jyuecCmLzZ4m-psiGkiRsXghD6y68h68aoC3XKNCfS-uhs8wb3ZWt6TBiUwIJLRqoNdevhnXo90iNYLS0xrEXHhh3tug-BkNzHoskJlQNFLzAlw5ozn7MR347_0WS26Se4_gG3gO3hpMxIOzx_Jr5MctYbE0rv2iq81bqSRnLL7Xh3CIJLcG-XAqhAnz1tjPfWm65yt0r0kkkJ1MLmiQWEHrhv2qe9Mv55XbBy7bSEVeETdq2OCEbjVVcMSUYhajSGiXMgVo6NpXkRg4IzSYrdLxrXFGCaiCo1LkRCxsPDe9qcRNPBLs0MF6DyYpETPig5nyomaILpNMTdXriOe0_YOiXi_chAuBvIHXP8IVnPabFWmNOlXAX3Y82oiG25Ye5SwfTTX83Cr1_iMXVXKGEj4_KKU39wmnQd1GRcRpSe4xV30aVXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
اوایل امروز در خلیج عمان، تفنگداران دریایی ایالات متحده از واحد تفنگداران دریایی ۳۱ام بر روی کشتی نفتکش تجاری پرچم‌دار ایران M/T Celestial Sea سوار شدند که مظنون به تلاش برای نقض محاصره ایالات متحده با عبور به سمت یک بندر ایرانی بود.
🔴
نیروهای آمریکایی پس از بازرسی و هدایت خدمه کشتی برای تغییر مسیر، کشتی را آزاد کردند.
🔴
نیروهای ایالات متحده به اجرای کامل محاصره ادامه می‌دهند و تاکنون ۹۱ کشتی تجاری را برای اطمینان از رعایت قوانین هدایت کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/alonews/121371" target="_blank">📅 20:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121370">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
حضور وزیر کشور پاکستان برای تسهیل تبادل پیام‌ها و ارائه توضیحات تکمیلی جهت شفاف‌سازی متون ارسالی میان طرفین انجام می‌شود.
🔴
ایران با وجود سابقه منفی طرف مقابل در یک سال و نیم گذشته، با جدیت و حسن نیت مسیر مذاکره را دنبال می‌کند اما نسبت به عملکرد آمریکا «سوءظن شدید و منطقی» دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/alonews/121370" target="_blank">📅 20:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121369">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEuGxHOKuGK6urovPxyRFH-17ShVwq4P7EjI4V6KUgr1dzU2Bl1xv57PdBsxf_sztjwnjPIOrfUmR-aKUR4825bOCJN6a8-h4Vb6nOnI7ElJY01agp8zoNVIvx9GXm05SlnWNVjvWpxq76KaPNsXhS0ubochfFGcT5nIPtAJJzudfSGHe51FIddOBZYpptuIwzsfTiyfqVufkmD3Pq_9PTmXuFcdD0kKeDgGmbJylBeyrjTnPWyQMVjw8s0YekFds0efMFt9cyGGOBNNTJCgbFHoBsk6ouiSa2aw25OsVEszfpIm-UTh9DDsQjnWBL5zGJi7t9T3p0RX_ulIvKgQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های تازه کلودفلر رادار نشان می‌دهد ترافیک اینترنت ایران طی ۲۴ ساعت گذشته افزایش محسوسی داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/alonews/121369" target="_blank">📅 20:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121368">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تبادل پیام‌ها بین طرف ایرانی و آمریکایی براساس متن ۱۴بندی ایران ادامه دارد.
🔴
حضور وزیر کشور پاکستان برای تسهیل مبادلۀ پیام‌هاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/alonews/121368" target="_blank">📅 20:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121367">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ادعای ای ۲۴ نیوز به نقل از بک منبع آگاه: پیشرفت‌هایی در گفتگو با ایرانی‌ها درباره «یادداشت تفاهم و اصول» که زیرساخت مذاکرات را می‌سازد، وجود دارد. اما اختلافات هنوز زیاد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/alonews/121367" target="_blank">📅 20:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121365">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c28ce6a5.mp4?token=Nx1Y19YT2rchiC-yvWrhdBNaLH9Y4iWwP9t1Cg31LJjauDS_tHfRMKE7FlXDBIO4TINAflqWPxy_KVA83S1tPmtDO77GyjEwBXJpsZhGE0rpmGFq6Jt00lr7WnCSt9Qn_VAr1ft6s3rNWfsWC7zejqEQlvUryZlCn9aWlQvnuNa3xvkQfjGHXmp8CLPGoYZBZH5_c_psx_yEgFy0eR1oRp3DBzvtLWUWRUL3zCYAsMHQKxTGyG5Zv6qcpBPnpQv4SagFy3BqseqlbhMqcYthUPo0uNMb4sSBYQUJEVrEf3XIZdZuZOYwl6cvNKyfQmgPJv_te6OIQnKoXY3tCZ9pCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c28ce6a5.mp4?token=Nx1Y19YT2rchiC-yvWrhdBNaLH9Y4iWwP9t1Cg31LJjauDS_tHfRMKE7FlXDBIO4TINAflqWPxy_KVA83S1tPmtDO77GyjEwBXJpsZhGE0rpmGFq6Jt00lr7WnCSt9Qn_VAr1ft6s3rNWfsWC7zejqEQlvUryZlCn9aWlQvnuNa3xvkQfjGHXmp8CLPGoYZBZH5_c_psx_yEgFy0eR1oRp3DBzvtLWUWRUL3zCYAsMHQKxTGyG5Zv6qcpBPnpQv4SagFy3BqseqlbhMqcYthUPo0uNMb4sSBYQUJEVrEf3XIZdZuZOYwl6cvNKyfQmgPJv_te6OIQnKoXY3tCZ9pCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : جنگ های بیشتری در راهه مگر اینکه ایران عاقل بشه - گارد ساحلی سه تا کشتی ایرانی رو گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121365" target="_blank">📅 20:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121364">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8faeb92d.mp4?token=ShyKbDmaHXx2t7QBQTY7_CJt7sXAnkL7rm-z5w7qFx0_9kj6fvJgq_cro0v-bF9m120lvOg_aW6ljwm1X89FX3710gfIbV64lgSPiOtuVJfEuCYbfdQP801kOhod8FriyxRO2YVAWD2LVfuonm1KkJ3KWFYFb-qe1kwKI1eynt88xFWrkOU-OQhCXcoY6mjqa2AWdIM4MWCueOkQpuIlEqwH9R8PHgTKfdrvXGmxxITLp0WBqwcVPedSGAL-R4Hprz0ThZSIZY5u2MLvKSBhnxzTSPdIXqYUllh7uAyxeE0Z3XLH6l4EEWSKkFyGGCaa0bQYJuCdbrdOrMcoT3-5qTTP9hYFmUpwDvivZhTUcuy-myzO9eUljwUyzUKoBNJgoGhdveXk2Yp3KRbt_nDEaXM3JPFE-bruqafJ6F6ZU980cSDnF_G7vYpAeTUn6k70meBPGTgiA7s-wadtxHOUTySehYP____BRQUIAelXW2OpbomxTW1SFiVjfjgiYQYT-OEw1eVD4q-f0wtm0PXJwq0hzlaJnZRpsRJCwBQBKilmpryN5ag4Uyun4X53KXoW-tzZcPlgxUXBIhpasVEwcySdcHQBHIeRH2bdUdZmrL5JKs8RL2VKl2jWYzB6ynRXchlrRGYwvoIepuz8qPtRk-7Kpkp_umwZmiPpabXKi10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8faeb92d.mp4?token=ShyKbDmaHXx2t7QBQTY7_CJt7sXAnkL7rm-z5w7qFx0_9kj6fvJgq_cro0v-bF9m120lvOg_aW6ljwm1X89FX3710gfIbV64lgSPiOtuVJfEuCYbfdQP801kOhod8FriyxRO2YVAWD2LVfuonm1KkJ3KWFYFb-qe1kwKI1eynt88xFWrkOU-OQhCXcoY6mjqa2AWdIM4MWCueOkQpuIlEqwH9R8PHgTKfdrvXGmxxITLp0WBqwcVPedSGAL-R4Hprz0ThZSIZY5u2MLvKSBhnxzTSPdIXqYUllh7uAyxeE0Z3XLH6l4EEWSKkFyGGCaa0bQYJuCdbrdOrMcoT3-5qTTP9hYFmUpwDvivZhTUcuy-myzO9eUljwUyzUKoBNJgoGhdveXk2Yp3KRbt_nDEaXM3JPFE-bruqafJ6F6ZU980cSDnF_G7vYpAeTUn6k70meBPGTgiA7s-wadtxHOUTySehYP____BRQUIAelXW2OpbomxTW1SFiVjfjgiYQYT-OEw1eVD4q-f0wtm0PXJwq0hzlaJnZRpsRJCwBQBKilmpryN5ag4Uyun4X53KXoW-tzZcPlgxUXBIhpasVEwcySdcHQBHIeRH2bdUdZmrL5JKs8RL2VKl2jWYzB6ynRXchlrRGYwvoIepuz8qPtRk-7Kpkp_umwZmiPpabXKi10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هرگز تسلیم نشوید. هر اتفاقی بیفتد، مهم نیست کجا در زندگی هستید یا در چه وضعیتی قرار دارید، به پیش رفتن ادامه دهید.
🔴
همیشه به جلو حرکت کنید. هرگز از پیش رفتن دست نکشید.
🔴
به مبارزه ادامه دهید و بگذارید دشمن اول تسلیم شود. بگذارید آنها تسلیم شوند. اگر شما ادامه دهید، آنها تسلیم خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/121364" target="_blank">📅 20:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121363">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634f6fb417.mp4?token=hLzR-1-LAZRIFQl1FU-9es5EgL7X2ViTOscDdbkc84dpF3krm558gFOcDGMWG_FHR9DRcUMhwr_MGR5r0WcQom_Om7CqSC8rjdr7cvJDE4NzJspmNrF6vv1WVv5bBbuxxdTYqd3PV4sEXSneQvOYzLRzVOQbjKroTLyfK7cUYwiiI79GSfqCLxn_ibch92Tep2FGE9BBOkqELnswH-NtxXq628_yq8HsM0Iu_zyqpGvoswIalVzQOsT8jwmq6_ywM6vk6ekHkF8fAwtbxFLsViUbJKMzMvEJnK4lDybWP3w4VQnPULz8zFpyv8hcUhSzziZ-SNNXc8mYNS6Pe4c8JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634f6fb417.mp4?token=hLzR-1-LAZRIFQl1FU-9es5EgL7X2ViTOscDdbkc84dpF3krm558gFOcDGMWG_FHR9DRcUMhwr_MGR5r0WcQom_Om7CqSC8rjdr7cvJDE4NzJspmNrF6vv1WVv5bBbuxxdTYqd3PV4sEXSneQvOYzLRzVOQbjKroTLyfK7cUYwiiI79GSfqCLxn_ibch92Tep2FGE9BBOkqELnswH-NtxXq628_yq8HsM0Iu_zyqpGvoswIalVzQOsT8jwmq6_ywM6vk6ekHkF8fAwtbxFLsViUbJKMzMvEJnK4lDybWP3w4VQnPULz8zFpyv8hcUhSzziZ-SNNXc8mYNS6Pe4c8JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ونزوئلا ۲۰ سال پیش کشور واقعاً بزرگی بود — اما مسیر اشتباهی را رفت.
🔴
این مسیری است که آن‌ها دوست دارند این کشور را به آن سمت ببرند — برخی دیوانه‌ها می‌خواهند این کشور را به سمت چپ بسیار شدید ببرند و آن را نابود کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/121363" target="_blank">📅 20:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121362">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521ea7f530.mp4?token=nAVROhWi0N7To8CnPp6GI-fd1ZGOA-7h8gIqTSx3pUqNx_W27G9OkfJ0w121Npo8qR_r8BwaWSuXDJoXnjdMV2KNLEIK7L9KGLHwJUToJCfKt6Fc0kQ_rXjt8wDN-sfPn8Ef3Rnww-eLoAd3gI90hd8zEkwzH2V8_tlZW6xhMOGwK3_rkUpxlo7qeXk5ubSAoNKAKo6D1ixtHit6DkzEWxWH2qI7ruZjdoPXRiV1q-aYA2TcQfr0LIKxwVKdcqBhoQqgkoMKd_5Pm9pLwi-twFtKeSEh2KSiwOrdnDqzM2lrajW_jdJRmaKWUIkBLJRjmiJ2iiRmodiGsgTOMpxczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521ea7f530.mp4?token=nAVROhWi0N7To8CnPp6GI-fd1ZGOA-7h8gIqTSx3pUqNx_W27G9OkfJ0w121Npo8qR_r8BwaWSuXDJoXnjdMV2KNLEIK7L9KGLHwJUToJCfKt6Fc0kQ_rXjt8wDN-sfPn8Ef3Rnww-eLoAd3gI90hd8zEkwzH2V8_tlZW6xhMOGwK3_rkUpxlo7qeXk5ubSAoNKAKo6D1ixtHit6DkzEWxWH2qI7ruZjdoPXRiV1q-aYA2TcQfr0LIKxwVKdcqBhoQqgkoMKd_5Pm9pLwi-twFtKeSEh2KSiwOrdnDqzM2lrajW_jdJRmaKWUIkBLJRjmiJ2iiRmodiGsgTOMpxczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما عملاً قاچاق مواد مخدر از طریق دریا را متوقف کرده‌ایم. و حالا بخش آسان‌تر، یعنی زمین. این هم به همان سرعت انجام خواهد شد.
🔴
قاچاق مواد مخدر ۶۱٪ کاهش یافته است، اما ما می‌خواهیم آن را تقریباً به صفر برسانیم چون این مواد خانواده‌ها، افراد و زندگی‌های زیادی را نابود کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/121362" target="_blank">📅 20:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121361">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ed4a2ba7.mp4?token=aVIJFTmKT_h7q2ijUNuILkjCSmOW9ah2o5XluIvhOBZoyCbLwBuknGx54lhs0V2D77Pptly736LMLSXe5SbGlI75511MymgPXc0eKxzXWwxFvP0orvMp_nOgefs8qY4jrGA5H6o45VEMHjkvoX0N4LECwlW7e6_Gc5eOhmDPxCHR_vAmvqH3sK5daSLeDJQS0NWl3ffVqaTHAyAokch-XIMH08n43-0UdH6nKxd3XGBplBuObTY1uKWSdYe3jMjBBoUmnBp-ZPwAp5w0vT4ES05_OiEU64vuZGQAovN6EDtqXAeQnJg7qlROdnQ-l66wK7NQu2pysc51qHNKIM1wTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ed4a2ba7.mp4?token=aVIJFTmKT_h7q2ijUNuILkjCSmOW9ah2o5XluIvhOBZoyCbLwBuknGx54lhs0V2D77Pptly736LMLSXe5SbGlI75511MymgPXc0eKxzXWwxFvP0orvMp_nOgefs8qY4jrGA5H6o45VEMHjkvoX0N4LECwlW7e6_Gc5eOhmDPxCHR_vAmvqH3sK5daSLeDJQS0NWl3ffVqaTHAyAokch-XIMH08n43-0UdH6nKxd3XGBplBuObTY1uKWSdYe3jMjBBoUmnBp-ZPwAp5w0vT4ES05_OiEU64vuZGQAovN6EDtqXAeQnJg7qlROdnQ-l66wK7NQu2pysc51qHNKIM1wTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ببینید الان من میگم آیران من اونجوری نمیگم چون تلفظ درستش مشخصه ما برمیگردیم به آیران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/121361" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121360">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ebe48c29.mp4?token=amKTme57mgrHmoAbeOJqoXQNsxMN5EG126KLdLx-6t3IDDVfeY6PnocnH2fS2hqMQH7sagnvJVediysk2rTKHGbj_oyZ8uEpd5JcIfpquKyX72sks3HJH05OC9rCTf5QIXYMcmswewzmhQshLroeVEKrETyr1Im2Cs2d23YL-BrYzBoFXvgUDqThBy-SJp1QOJPH-nPXUdPyXGOOzfkQOtjuN9G63F2Mx9ukLfeY-ViOFqaMMiyxkSscy-ZVib6R9AWWYhYIU-uXeutet2O1DpEQKKr4dQSNpWYDomUlIWPvuDzNmLvWzZvHwdJJbG34VFcTesq6rjTKEVQQZWHbzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ebe48c29.mp4?token=amKTme57mgrHmoAbeOJqoXQNsxMN5EG126KLdLx-6t3IDDVfeY6PnocnH2fS2hqMQH7sagnvJVediysk2rTKHGbj_oyZ8uEpd5JcIfpquKyX72sks3HJH05OC9rCTf5QIXYMcmswewzmhQshLroeVEKrETyr1Im2Cs2d23YL-BrYzBoFXvgUDqThBy-SJp1QOJPH-nPXUdPyXGOOzfkQOtjuN9G63F2Mx9ukLfeY-ViOFqaMMiyxkSscy-ZVib6R9AWWYhYIU-uXeutet2O1DpEQKKr4dQSNpWYDomUlIWPvuDzNmLvWzZvHwdJJbG34VFcTesq6rjTKEVQQZWHbzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما خیلی سخت بهشون ضربه زدیم شاید مجبور بشیم حتی سخت تر هم بزنیم ولی شاید هم نه!
🔴
سلطه آمریکا تو نیمکره غربی تحت هیچ شرایطی تهدید نخواهد شد ایران هم هرگز نباید سلاح هسته ای داشته باشه
🔴
ما اجازه نمیدیم ایران سلاح هسته ای بگیره و کل خاورمیانه و اسرائیل رو نابود کنه و بعد بیاد سراغ شما و این اتفاق نمی اوفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/121360" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121359">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db7d50a7db.mp4?token=kAfBW12u-cEi0CHesKE0ukpXdtI1S1CMjon7ZckfDGMGPdVbBR8NO3Uc7yC1FTuBGHxxJnTjUBK2fQZUySByUcl217kTERLZD_VHFwiLtGXcae_-GWIpK7Uz1SD5zjQxMcbHh-QhBeYoeb1vr5UjEcKJ47OACc54Twoy3oJxxO-OusJhkO_FvUhslCWOHuQLKO2xjz88qlsSGu7G7I5nHT452SHrcWWC0RHgc_ualHrc7vI7s4-dHugKP3-iwaE7p4RPsmrjnyxJLtjc55GiAhWERh13bkR8lw7cdn9x_knYypsDeqaSrja2tpX7ZThwhFV1TDcdP5L86CyAZWZrgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db7d50a7db.mp4?token=kAfBW12u-cEi0CHesKE0ukpXdtI1S1CMjon7ZckfDGMGPdVbBR8NO3Uc7yC1FTuBGHxxJnTjUBK2fQZUySByUcl217kTERLZD_VHFwiLtGXcae_-GWIpK7Uz1SD5zjQxMcbHh-QhBeYoeb1vr5UjEcKJ47OACc54Twoy3oJxxO-OusJhkO_FvUhslCWOHuQLKO2xjz88qlsSGu7G7I5nHT452SHrcWWC0RHgc_ualHrc7vI7s4-dHugKP3-iwaE7p4RPsmrjnyxJLtjc55GiAhWERh13bkR8lw7cdn9x_knYypsDeqaSrja2tpX7ZThwhFV1TDcdP5L86CyAZWZrgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : صنعت تراشه ما توسط تایوان برداشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121359" target="_blank">📅 19:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121357">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0da6120d.mp4?token=io8CgwUwA3ZVo71EObTAjn8BUkdIal4sGJLc2NVYtzH8JGBn0qdj_t1-g8Uutd1_BTBm7jWEtSQm6O6AT1E0XzapPZxXy0HHrM8HKGTmtw-8U_XJI9wbVn3JTNG2qQo8wRiE1IK1NslDqnQmeSA3SA3R4wbYo8y06gp7vHxDeoTS3dpkC5EjKBzdwWfglvBdOEEgjMLZgQ1XCX9K5laLkcbfyzb6D5SvQp9fs0uEkrPGqbkQyUAm6nAOjou7j-1RxZxdhjNGmmHGr0hFykZXvX2Xxd2qDN4C_Xkkcvvh0cOlIqrkBrsSRL2Akg2D6FDXCc-tWFo0quo_E1eu4AHpyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0da6120d.mp4?token=io8CgwUwA3ZVo71EObTAjn8BUkdIal4sGJLc2NVYtzH8JGBn0qdj_t1-g8Uutd1_BTBm7jWEtSQm6O6AT1E0XzapPZxXy0HHrM8HKGTmtw-8U_XJI9wbVn3JTNG2qQo8wRiE1IK1NslDqnQmeSA3SA3R4wbYo8y06gp7vHxDeoTS3dpkC5EjKBzdwWfglvBdOEEgjMLZgQ1XCX9K5laLkcbfyzb6D5SvQp9fs0uEkrPGqbkQyUAm6nAOjou7j-1RxZxdhjNGmmHGr0hFykZXvX2Xxd2qDN4C_Xkkcvvh0cOlIqrkBrsSRL2Akg2D6FDXCc-tWFo0quo_E1eu4AHpyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ بعد از دست دادن با یکی از دانشجوهای نظامی:
🔴
از مردای خوشتیپ بدم میاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/121357" target="_blank">📅 19:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121356">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0799862f1.mp4?token=BzOIaxh43D5c2VoRf4A9QM_CVyIesM2GXKrwgvGsvsCF03ydh7vnmCPFf4qqngvMKKFR7pxnFfR9TzTLeegYSq_ADdb0RZIFXfThUAkv3cFKE0h_y__maQZtsmuTqxWaLzAz8ssR7Z4LTw8spMOQnwYKYdUt2pz7cnT8h0IqFW9X3-squ72R26f5OnSs7ITOl2hvE62lmSqf4wY_HAIPeq3TCU-vG3pe-T7zjlwBbFIL_9B5FTDFE6ok3lTIOdwZPrIpJ65gW0dFxQ-W0-Y-KYtVCmWLkahH7ePI-JijMvZQaSVKnuE6krCeMdzsYg0GicjGcrgKjTj7Pbxa6RH7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0799862f1.mp4?token=BzOIaxh43D5c2VoRf4A9QM_CVyIesM2GXKrwgvGsvsCF03ydh7vnmCPFf4qqngvMKKFR7pxnFfR9TzTLeegYSq_ADdb0RZIFXfThUAkv3cFKE0h_y__maQZtsmuTqxWaLzAz8ssR7Z4LTw8spMOQnwYKYdUt2pz7cnT8h0IqFW9X3-squ72R26f5OnSs7ITOl2hvE62lmSqf4wY_HAIPeq3TCU-vG3pe-T7zjlwBbFIL_9B5FTDFE6ok3lTIOdwZPrIpJ65gW0dFxQ-W0-Y-KYtVCmWLkahH7ePI-JijMvZQaSVKnuE6krCeMdzsYg0GicjGcrgKjTj7Pbxa6RH7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : برای موفقیت هیچ وقت احساس گناه نکن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/121356" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121355">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
افراد مسلح در خودرویی به سمت یک خودروی پلیس در جاده‌ای در شهرستان سراوان در جنوب شرق ایران تیراندازی کردند که منجر به کشته شدن یک افسر پلیس شد، گزارش تسنیم.
🔴
عملیات امنیتی و انتظامی در منطقه در جریان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/121355" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121354">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58dc1edc3b.mp4?token=E4MSV1-asszmvBsA6kMKaE-ogUqkW4Zs9QEIvBzSSikITCHRu5ymZ6Ypo4ZbnxaMEyxVL4mduYUP0vNd8EFdFF1TcZA-O0TzXjrMpuj33GlsAkyy2oYaTgDTWesVMp2GfO0Vd1bVSpjoidyV99dVu3OqCaJn4WDTb2kQT4UWqhZ5uJlui3PND71o4UtzYT1WaHEa4Vcb36PM6HnhdZlXAM5mzUyE0pXEW9CUBzuBGKW82W6367Z8COhlYABXd057Z-1k4Adl3ssERjyu7nyCJSrX7d-K9ouk-ka1m1fgpq_zzkWCY6e3MUMkJlsRecK41eDGcMvK7qXRlJhLPzG0UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58dc1edc3b.mp4?token=E4MSV1-asszmvBsA6kMKaE-ogUqkW4Zs9QEIvBzSSikITCHRu5ymZ6Ypo4ZbnxaMEyxVL4mduYUP0vNd8EFdFF1TcZA-O0TzXjrMpuj33GlsAkyy2oYaTgDTWesVMp2GfO0Vd1bVSpjoidyV99dVu3OqCaJn4WDTb2kQT4UWqhZ5uJlui3PND71o4UtzYT1WaHEa4Vcb36PM6HnhdZlXAM5mzUyE0pXEW9CUBzuBGKW82W6367Z8COhlYABXd057Z-1k4Adl3ssERjyu7nyCJSrX7d-K9ouk-ka1m1fgpq_zzkWCY6e3MUMkJlsRecK41eDGcMvK7qXRlJhLPzG0UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: همه چیز از بین رفته است.
🔴
تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سندی را امضا کنند؟ ببینیم چه پیش می‌آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/121354" target="_blank">📅 19:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121353">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
معاون وزیر خارجه روسیه: مسکو آماده است برای مذاکرات بین ایران و آمریکا «دست یاری» دراز کند، اما قصد ندارد خدمات خود را تحمیل کند
🔴
سرگئی ریابکوف، معاون وزیر امور خارجه روسیه، می‌گوید مسکو در صورت لزوم آماده است برای مذاکرات بین ایران و آمریکا «دست یاری» دراز کند، اما قصد ندارد خدمات خود را تحمیل نماید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121353" target="_blank">📅 19:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121352">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بن‌گیور، وزیر امنیت ملی اسرائیل، از فعالان بازداشت‌شده در کاروان جهانی صمود غزه در بندر آشدود بازدید کرد.
🔴
به اسرائیل خوش آمدید، ما اینجا در کنترل هستیم. این همان چیزی است که باید باشد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121352" target="_blank">📅 19:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121351">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
الجزیره به نقل از منابع دیپلماتیک: تعداد کشورهای حامی پیش نویس قطعنامه تنگه هرمز در شورای امنیت به ۱۳۶ کشور رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/121351" target="_blank">📅 19:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121350">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سفیر اسرائیل در واشنگتن: هر توافقی با ایران لزوماً باید بر پایۀ اصل عدم اعتماد باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/121350" target="_blank">📅 19:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121349">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miqWJDyGJEXTLFE4wcw19pzLZGuMbJVbfIjU2UdGPiDR-NlXYCIWVH0DU5y_YXYrg1i5b-pzo3-5nqyKZ0tOL15IuA-eRQTX1163dWghQgCJR-g-_cOsxN3rX2Fx0uzRbIab1ZZCHdJI-foT5iQBusH_BpXNQ_iR1Z_hracuprvOr50w9g2MvsIvqBV6KTPJ2SLXXc90p4YY4dZuOSbWlf6M-o9uj4gjybpn-10FOYNPCWvpOvKbMASADGzmKyz68CZ-jnJDOyK6lMvJYUpMheEoZnzkR7Qz7UH86t1ddGwK6cmuW9O0uHbdSLEibIo_itbQ3dXPUlQB8RtGH77w6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور سابق کوبا، رائول کاسترو، طبق گزارش رویترز و به نقل از یک مقام ارشد دولت ترامپ، در ایالات متحده متهم شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/121349" target="_blank">📅 19:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121348">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
لارنس نورمن خبرنگار وال استریت ژورنال، با اشاره به خبر العربیه: حس من این است که اتفاق مهمی در جریان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/121348" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121347">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚀
فروش کانفیگ استارلینک و VIP با سرعت بالا و اتصال پایدار
💎
پلن‌های VIP
📍
1 گیگ — 200 هزار تومان
📍
3 گیگ — 600 هزار تومان
⭐️
پلن‌های Starlink
🔸
5 گیگ — 1.500 میلیون تومان
🔸
10 گیگ — 2.900 میلیون تومان
✅️
آی‌پی ثابت
✅️
پشتیبانی ۲۴ ساعته
✅️
کیفیت تضمینی…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/121347" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121346">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uts1tosu3cv01nQnOwA4jJGr6h7hpFdCb4flCb_DElN-cliHDEMoqoGBAI-LbOiSXEj80LTaVghVOds6N_hW8i65bptlh8nO3tFG5wDhfiosKu1Ve9nSTW9lFPUv4iI6oYgiJ8MQ0YdetqtHs-bgpQA_-eFZc4njRvrRVMFBZ9eBLudNqXGX5gr6KRuiZT13lllj7A4B-omTCDU7p2kS1ePEGe9Hijtp8AKsD_Ymqgq4G9eOWghdeBEf3tYpgtC6it--feKkHLvSZD2Jnnna7g8h31jvpWqb2HTfAg8lZXyyOnPbmj68V12AKXT8BvDt7qywxepzAynqVO7LXs5Nzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فروش کانفیگ استارلینک و VIP با سرعت بالا و اتصال پایدار
💎
پلن‌های VIP
📍
1 گیگ — 200 هزار تومان
📍
3 گیگ — 600 هزار تومان
⭐️
پلن‌های Starlink
🔸
5 گیگ — 1.500 میلیون تومان
🔸
10 گیگ — 2.900 میلیون تومان
✅️
آی‌پی ثابت
✅️
پشتیبانی ۲۴ ساعته
✅️
کیفیت تضمینی
✅️
دارای ساب باقیمانده لحظه ای
✅️
متصل در تمامی دستگاه ها و اپراتور ها
🛫
خرید و پشتیبانی:
🏠
@expressuport
🤖
ربات خرید:
💻
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/121346" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121345">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ادعای سفیر اسرائیل در واشنگتن: هرگونه توافق احتمالی با ایران باید بر اساس اصل بی‌اعتمادی کامل و راستی‌آزمایی باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/121345" target="_blank">📅 19:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121344">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: شگفت‌آور است که جمهوری‌خواهان موقعیت بسیار مهم «پارلمانی» را در دست زنی به نام الیزابت مک‌دونو نگه داشته‌اند، کسی که مدت‌ها پیش توسط باراک حسین اوباما و دیوانه شرور شناخته‌شده به نام سناتور هری رید، که مجلس سنا را برای دموکرات‌ها با «مشت آهنین» اداره می‌کرد، منصوب شده بود. در طول سال‌ها، او برای جمهوری‌خواهان بی‌رحم بود، اما برای دموکرات‌ها این‌گونه نبود - پس چرا جایگزینش نکردند؟ افراد عادل زیادی وجود دارند که برای آن موقعیت حیاتی واجد شرایط هستند.
🔴
جمهوری‌خواهان بازی بسیار نرم‌تری نسبت به دموکرات‌ها انجام می‌دهند. این بزرگ‌ترین عیب در سیاست است. دموکرات‌ها تقلب می‌کنند، دروغ می‌گویند و می‌دزدند، به‌ویژه وقتی که موضوع آرا در انتخابات است، اما به هم وفادارند، در حالی که جمهوری‌خواهان اجازه می‌دهند الیزابت مک‌دونو در قدرت بماند و بی‌رحمی ما ادامه یابد. ما باید قانون نجات آمریکا را تصویب کنیم، و همین حالا - و همچنین باید تعلل را از بین ببریم، که همه چیز را به ما خواهد داد! اگر حداقل یکی از این دو قانون را سریع تصویب نکنیم، دیگر هرگز رئیس‌جمهور جمهوری‌خواهی نخواهید دید. دموکرات‌ها دو ایالت اضافی، پایتخت و پورتوریکو، و همه پیامدهای آن، از جمله
🔴
۴ عضو در مجلس سنا، چندین عضو کنگره، چندین رای انتخاباتی اضافی، و همچنین رویای خود را برای دادگاه عالی ایالات متحده با ۲۱ قاضی مورد علاقه‌شان به دست خواهند آورد.
🔴
دموکرات‌ها در اولین روزی که فرصت داشته باشند، تعلل را از بین خواهند برد.
🔴
جمهوری‌خواهان این کار را نمی‌کنند چون می‌گویند دموکرات‌ها هرگز این کار را نخواهند کرد، اما جمهوری‌خواهان اشتباه می‌کنند. هوشمند و سخت باشید، وگرنه خیلی زودتر از آنچه فکر می‌کنید همه‌تان دنبال کار خواهید گشت!
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121344" target="_blank">📅 18:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121343">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / ترامپ: آمریکا در «مراحل نهایی» مذاکرات با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/121343" target="_blank">📅 18:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121342">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUMqteHUIJhD_ZuCpumt8lSK6w9-eghy4x4kJftl177pCC0PWRXdQ-ZmAQwQYAuJZHARxfPQuA-umGen4jNhrMqOUutEFYsIgwCpwVfpT3dhYIDvEbR57yzViOHvOq7ObzbEDN3NFT4tqzS7iYQStwkxATDQYXV2ZyvQ-OId5SZWLDjXy99xuqlDdrO4oYwk_GzQFl2MPosuBRxcOgpcCIFPnw0Bp2KD0X8WJP8gefD9N1I9fSPpVk232qpOBpFGwByhsQvEP49SZxYxOSglJjrFHhP11DAP2fangJd4BDWVdhI1TaeN40nWCUBLJWdJdC1FRhYNQLc4MIsGc0RD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تحرکات سنگین نظامی آمریکا به سمت خاورمیانه همچنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/121342" target="_blank">📅 18:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121341">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، روز چهارشنبه گفت که کاهش تدریجی نیروهای آمریکایی در اروپا به صورت ساختاریافته انجام خواهد شد که برنامه‌های دفاعی ناتو را تحت تأثیر قرار نخواهد داد و این تعدیلات را پاسخی منطقی به افزایش هزینه‌های دفاعی توسط متحدان اروپایی و کانادا توصیف کرد، به گزارش رویترز.
🔴
روت افزود که بحث‌ها درباره سهم آمریکا در ناتو در مواقع بحران بیش از یک سال پیش آغاز شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121341" target="_blank">📅 18:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121340">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
معاون وزیر خارجه روسیه: مسکو آماده است برای مذاکرات بین ایران و آمریکا «دست یاری» دراز کند، اما قصد ندارد خدمات خود را تحمیل کند
🔴
سرگئی ریابکوف، معاون وزیر امور خارجه روسیه، می‌گوید مسکو در صورت لزوم آماده است برای مذاکرات بین ایران و آمریکا «دست یاری» دراز کند، اما قصد ندارد خدمات خود را تحمیل نماید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/121340" target="_blank">📅 18:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121339">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر امور خارجه عربستان سعودی:
ما از واکنش رئیس جمهور آمریکا در اعطای فرصت به مذاکرات برای دستیابی به توافقی که به جنگ پایان دهد، بسیار قدردانی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121339" target="_blank">📅 18:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121338">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل هشدار تخلیه برای حبوبش و دیر الزهرانی در جنوب لبنان صادر کرده‌اند پیش از حملات اسرائیل در پاسخ به «نقض آتش‌بس توسط حزب‌الله».
🔴
از ساکنان خواسته شده حداقل ۱ کیلومتر از روستا فاصله بگیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/121338" target="_blank">📅 18:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121337">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ درباره کوبا: آمریکا تحمل یک دولت سرکش که عملیات نظامی، اطلاعاتی و تروریستی خصمانه را تنها نود مایل از خاک آمریکا پناه می‌دهد، نخواهد داشت و تا زمانی که مردم کوبا دوباره آزادی‌ای را که اجدادشان بیش از ۱۰۰ سال پیش با شجاعت برای آن جنگیدند به دست نیاورند، آرام نخواهیم نشست
🔴
رژیم هاوانا امروز خیانت مستقیم به ملتی است که پدران بنیان‌گذار آن برایش خون دادند و جان باختند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/121337" target="_blank">📅 18:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121336">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw7SqBwLdLD5NON_jTXuC6Y19CPzCLUiDAm1UGJMn2tffTb4-zgYoetV0_mwUC-thWIZjyMVWoSpH8x2JjjK22JzF9hbWWRQJQ09q-v6EMytZR56HLhpmkjSzQrCS2BZwL20_rn5XkMxbFDOpw-zbVgJhb_AjIjtjyGzjKg6QJVOWjNrOsHnPzQKaEJo6IuBv89JB4x5nq1x52S8IwBXN33ZH07fERcjQHhYr3YOzrDQx1s-1Cn83xR5TZg8x3uYXUkuwau9dBv2qHyf4tR4t3JWB2ZKHcB6TqiLTlkksXpFRfU95JpjMjquhDbWkYu0LWABj7RIkd1GAft8YgWVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت سقوط کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/121336" target="_blank">📅 18:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121335">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزارت امور خارجه: ایران اورانیوم خود را به هیچ کشوری منتقل نمیکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121335" target="_blank">📅 18:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121334">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بن‌گیور، وزیر امنیت ملی اسرائیل، از فعالان بازداشت‌شده در کاروان جهانی صمود غزه در بندر آشدود بازدید کرد.
🔴
به اسرائیل خوش آمدید، ما اینجا در کنترل هستیم. این همان چیزی است که باید باشد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/121334" target="_blank">📅 18:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUIkt1Z5AgG6eR2Ri08AwZoaHqewglgrxg8YZp0ul3Usm3jdT9M9oQPpooPq2ixeRbkvT3aziEMNQG9d4Cjq7JTbuJH0XvgYcVdOWcReIfeOxBJwQyZ3bYA56wcnKGULkqCBgqhXC9PN7obppmTSvmqos0ywSsAlSc27RkugKI1wqcuIWg-setXtqgyOjJLJxvcN8rZ3G-w6iCT43soDF-pQjl4RcJdZVGaRGv1Pa43guqtdpYN7P72ntExC_zNh4kBRdbGZ6uVqjdx45lfod9m4FdovUcQ173YUWfxCsllW95obCIgml__i-lJbWs3JcLN4r19CVCNAI9m_ZOCdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fw9es0V2Hd8brhN4kzPeydjtvu1QTP1U9mk5k0DnVIzbHQJ-kW_diSjgjRIVXgBMQ-eSGyKqdoMUQAXEac2oyssrn5peCOcrnVq4cpxuFmvKz49M4sOan3YlbSOkfwtArAcgyR_y5t0iqiwe1ugigjbXBrSxHOMS9xSrSHdMg_nyZeFCYma6MAC_L8ySgtg_wsJ4NTH5H7kOgQUXRJ1mypIHHq_rG1d13mE3UgVRzu9UgwfGbIC3W8aasUSGrdxdmidKXcQRWSesVtT2BsGRZ9vSBQy3W_D6bIi6pTNhqoQg4P5nVk7y70b-9Ya9kNSdYtRJ8AuBQW1UBwcyvbTTXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اوکراین صبح امروز یکی از بزرگ‌ترین پالایشگاه‌های نفت روسیه، پالایشگاه لوک‌اوئیل-نیژگورودورگسینتز، واقع در نزدیکی شهر کستوو در منطقه نیژنی نووگورود را هدف قرار داد که این دومین حمله به این تأسیسات در طول یک هفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121332" target="_blank">📅 18:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پهپاد انتحاری Hornet ایالات متحده با استفاده از یک سیستم پرتاب کمکی با بادکنک آزمایش شده است که در آن بادکنک پهپاد را ۴۲ کیلومتر حمل می‌کند و سپس آن را از ارتفاع ۸ کیلومتری رها می‌کند، در حالی که تنها از ۵٪ باتری خود استفاده می‌کند.
🔴
این مفهوم با ترکیب مسافت طی شده بادکنک، رها کردن از ارتفاع بالا و صرفه‌جویی در باتری ناشی از اجتناب از پرواز با نیروی محرکه در حین صعود، برد عملیاتی پهپاد را به طور قابل توجهی افزایش می‌دهد.
🔴
ادغام با یک پایانه Starlink می‌تواند برد حمله پهپاد را از حدود ۱۰۰ تا ۱۲۰ کیلومتر به اندازه ۱.۵ تا ۲ برابر بیشتر افزایش دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121331" target="_blank">📅 18:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرنگار: نظر شما درباره دیدار شی جین پینگ با پوتین این هفته چیست؟
🔴
ترامپ: فکر می‌کنم کار خوبی است. من با هر دوی آنها روابط خوبی دارم. نمی‌دانم مراسمشان به اندازه مراسم من درخشان بود یا نه. من تماشا کردم. فکر می‌کنم ما از آنها بهتر بودیم. تیم خوبی هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121330" target="_blank">📅 18:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سلطان الجابر، مدیرعامل شرکت ادنوک (ADNOC)، ادعا کرد که خط لوله جدید امارات متحده عربی برای دور زدن تنگه هرمز، ۵۰ درصد پیشرفت فیزیکی داشته و تا سال ۲۰۲۷ به اتمام خواهد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121329" target="_blank">📅 17:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فووووری/العربیه: فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند.
🔴
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121328" target="_blank">📅 17:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121327">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
العربیه: ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121327" target="_blank">📅 17:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121326">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوووووووووری</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121326" target="_blank">📅 17:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121325">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوووووووووری</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121325" target="_blank">📅 17:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121324">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkiURoVxZ1ve61emcy2Q2_mrvE0sAgMp3LOyntV_xrzi7uA9w9X6g8IOe0a7SVFzcRBGFSpZrszXEC_fPsGicwzPgLnqbjs6g4Ag4__Vlvn_xldX_MJJ0IrFMeXs2Oas4gzhOLe7dUXDbI_ODSBm_3hzkO40RdZNLlM6Uypj4yj68A8IjMpNdflkSEjSQbhaA7jAcXu5QICb02GCFk7_jjI2oxWawdvln0AqkNIHG9el6-kjvmYCux-S7R2nAEzujpcqqwSNN_Spgz1JQCflKe9CT7kplf2J_xLkEtIM9GDNnnPdHLxjed9u6h33Kru5snimm4d-kvaq1U-0NzIY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی انجمن صنایع فرآورده‌های لبنی:
قراره لبنیات از اول خرداد 20 درصد گرون بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121324" target="_blank">📅 17:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121323">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f6765942.mp4?token=iixAwdI_qkyrNlAGt80QIt5a1ReEGioeSzHtrIEMaBuE3LaOOIDm_T-3nZVpoi1GSnBogZiVN6jhBYGNC8MoGIVQTaSlo7ELWeaE9xz1cCdY89W_vQnHtCDAWkvYh5wtp86qqylLLKKDLeWf-Mrl8cLKKticTVrIzf6qcPpqbaVo3iFZ8d185okJVyWJJZEIZQspw3fuHwRYWRMLCK99WvmHFK0IIgI-Xr5jSSTCHvJQi_Kw2gv-0YTxnZpW4qYhGicq0v-X85lRpXajWLFhuBPg4YTjscclE5OFIKBgoqy_Gan4m2U65K6-vw_iQUPB48N_kNpbUDRlhOH5B5OmhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f6765942.mp4?token=iixAwdI_qkyrNlAGt80QIt5a1ReEGioeSzHtrIEMaBuE3LaOOIDm_T-3nZVpoi1GSnBogZiVN6jhBYGNC8MoGIVQTaSlo7ELWeaE9xz1cCdY89W_vQnHtCDAWkvYh5wtp86qqylLLKKDLeWf-Mrl8cLKKticTVrIzf6qcPpqbaVo3iFZ8d185okJVyWJJZEIZQspw3fuHwRYWRMLCK99WvmHFK0IIgI-Xr5jSSTCHvJQi_Kw2gv-0YTxnZpW4qYhGicq0v-X85lRpXajWLFhuBPg4YTjscclE5OFIKBgoqy_Gan4m2U65K6-vw_iQUPB48N_kNpbUDRlhOH5B5OmhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره خودش:
شما در نهایت خواهید گفت: «او بزرگترین رئیس‌جمهوری است که زندگی کرده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121323" target="_blank">📅 17:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121322">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/753b6e158c.mp4?token=uXf3Xs4rMNiHTi0kgGBlFmPFkNLErxI-j4QZ-A1ivXeBzkOHSaazp7DtAjvuzQcIIRAkt8FLDYEyRXz-GDw9mkRQHpJLt6xYPYXkQ3w9MPVjJdCaK7eV39HhR8l69DWxR72VNIH2nxWheDBf1wYpM9AsQy-2HQ2quzHvnj-BWXFXGup5HLEl6nl5bqEdO1ErmlR7VMwwjFt3_TN-xEmj1oEQXh9Xhl_dsCzgSHEYI3QjHZt0y0bHA_Nwa3uvudKv9sZwaUhlABCv53TNlWHAak1M17bqEBdnmH5yp0IZ2rf9apv2RsaE_w5f0Cus0jCFVS7tSGxFet56nh3FctCps4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/753b6e158c.mp4?token=uXf3Xs4rMNiHTi0kgGBlFmPFkNLErxI-j4QZ-A1ivXeBzkOHSaazp7DtAjvuzQcIIRAkt8FLDYEyRXz-GDw9mkRQHpJLt6xYPYXkQ3w9MPVjJdCaK7eV39HhR8l69DWxR72VNIH2nxWheDBf1wYpM9AsQy-2HQ2quzHvnj-BWXFXGup5HLEl6nl5bqEdO1ErmlR7VMwwjFt3_TN-xEmj1oEQXh9Xhl_dsCzgSHEYI3QjHZt0y0bHA_Nwa3uvudKv9sZwaUhlABCv53TNlWHAak1M17bqEBdnmH5yp0IZ2rf9apv2RsaE_w5f0Cus0jCFVS7tSGxFet56nh3FctCps4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «در اسرائیل، میزان محبوبیت من ۹۹ درصد است. شاید به اسرائیل بروم و برای نخست وزیری نامزد شوم.».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121322" target="_blank">📅 17:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121321">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: رژیم ایران رو عوض کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/121321" target="_blank">📅 17:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121320">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ab0a1951.mp4?token=XeST0lQWu3rUHyEkg1WmOOMEl2KeprNI5nyoPwgJvnbLRUu_xQvwa7lE9utYp1keHwkt3S7n0cEQrtGxHSKGjEalisS09-RnFV2WDRQN5rhTeEgFjQpvyv5yZIqirpEruSsnAT6s6wCsaRVXCs-EuhMtcjrva-mvm-2_VApnVG_5NLLOrDe1o1fHhIfG1toZfOARh2jiPxATWlcQBbxR9vcirmu_N-2Im97ukxkljj6g004KTHVSgzHOmoRMgojaO4oQDZhyyQoJJNn73gU8XQyu-C5cTuddA2xAK0Y_XtDfcYIjwEUNSN0FlILhXnZG5Iuq9bXw9rWHaTwh-P5GBZIgcDkx5DysZlCQ1CrKGN2HVxPknPINkAUyYtIFU3bbDOj1FqOz_VbVmqoTfOzMdFQ_E8W_VDPzDpdy8P872Tpt9i_u1WaBXXtaUw7Ei-rlgrWS5siafzwwsToF4NfshV1wWYlrYXflTsaF_5x1NDbOF8vSCjZ4vVQTPzs4xS2Nw6F8hxPiMN754trlO1fWPn8wUlRIbbeHkR6YvUIPjQVLBeSSp4YKI7ufHK5GRkoZmOuSLzaJ_c0d8p5lpzQ866noqaUU79D_dAXxNNHZJwfnweOnmXr3adD3HWE7NegH8JGJZ7ICQphqX2z7hqjJakFuxzA-Q0n4PveUOHHyZDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ab0a1951.mp4?token=XeST0lQWu3rUHyEkg1WmOOMEl2KeprNI5nyoPwgJvnbLRUu_xQvwa7lE9utYp1keHwkt3S7n0cEQrtGxHSKGjEalisS09-RnFV2WDRQN5rhTeEgFjQpvyv5yZIqirpEruSsnAT6s6wCsaRVXCs-EuhMtcjrva-mvm-2_VApnVG_5NLLOrDe1o1fHhIfG1toZfOARh2jiPxATWlcQBbxR9vcirmu_N-2Im97ukxkljj6g004KTHVSgzHOmoRMgojaO4oQDZhyyQoJJNn73gU8XQyu-C5cTuddA2xAK0Y_XtDfcYIjwEUNSN0FlILhXnZG5Iuq9bXw9rWHaTwh-P5GBZIgcDkx5DysZlCQ1CrKGN2HVxPknPINkAUyYtIFU3bbDOj1FqOz_VbVmqoTfOzMdFQ_E8W_VDPzDpdy8P872Tpt9i_u1WaBXXtaUw7Ei-rlgrWS5siafzwwsToF4NfshV1wWYlrYXflTsaF_5x1NDbOF8vSCjZ4vVQTPzs4xS2Nw6F8hxPiMN754trlO1fWPn8wUlRIbbeHkR6YvUIPjQVLBeSSp4YKI7ufHK5GRkoZmOuSLzaJ_c0d8p5lpzQ866noqaUU79D_dAXxNNHZJwfnweOnmXr3adD3HWE7NegH8JGJZ7ICQphqX2z7hqjJakFuxzA-Q0n4PveUOHHyZDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : درباره جنگ ایران چی میگید؟
🔴
ترامپ : بذار اینجوری بگم شما تو ویتنام ۱۹ سال بودید،جنگ جهانی دوم ۴ سال بود
- من ۳ ماهه درگیرم، خیلیاش هم آتش‌بس بوده. تو دو جنگ،ونزوئلا و اینجا، ما ۱۳ نفر از دست دادیم
- تو جنگ‌های دیگه صدها هزار نفر کشته دادید. ما عملاً ونزوئلا رو گرفتیم تقریباً هم ایران رو گرفتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121320" target="_blank">📅 17:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121319">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: به ایران فرصت میدم فکر کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/121319" target="_blank">📅 17:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121318">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: اگر عیسی مسیح پایین می آمد و رای ها را می شمرد ، من در کالیفرنیا برنده می شدم اما این یک انتخابات تقلبی است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/121318" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121317">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ: وقتی پرونده ایران را مطالعه می‌کنم اصلا به انتخابات میان دوره‌ای فکر نمی‌کنم و برای رسیدن به توافق عجله ندارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121317" target="_blank">📅 17:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ: امروز خشم زیادی در ایران وجود دارد زیرا استاندارد زندگی بد است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121316" target="_blank">📅 17:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121315">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری/ترامپ: برا جنگ عجله ندارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121315" target="_blank">📅 17:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121314">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: نتانیاهو کاری را که از او میخواهم انجام خواهد داد‌‌
🔴
من و نتانیاهو درباره ایران توافق داریم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121314" target="_blank">📅 17:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121313">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6fdf71ef.mp4?token=Kvk5zumhzAP4QpEuxFw9cORQc46TROk6m88QLPZt34VRD4FB2fFz4RcbLilS2r_Ahz15Yt5_xm-rAMLn4sy0N7t3HSfmZL-YG1ybnikTQUzOVQJ5zLUnXFbPzneSDjAXCTUgumNG-CaarbSvuMw2XVixyc0LrWrYWUo00h_IOxvBSIBXwcpzBIZnyMZuQaSsHyJD1Yolj4ESV21b72k0w20jOXvtwdkxOTrHohN9v2oCBWDNFSNjSC--sEX14AXSakiwSubFX-y8nJ6tKxB_c2a7ORq-12NfwcuYzqboygiXz2AVwi4qJEkV8R-J7xHyue0l7WxCuwSMW-HBo03kaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6fdf71ef.mp4?token=Kvk5zumhzAP4QpEuxFw9cORQc46TROk6m88QLPZt34VRD4FB2fFz4RcbLilS2r_Ahz15Yt5_xm-rAMLn4sy0N7t3HSfmZL-YG1ybnikTQUzOVQJ5zLUnXFbPzneSDjAXCTUgumNG-CaarbSvuMw2XVixyc0LrWrYWUo00h_IOxvBSIBXwcpzBIZnyMZuQaSsHyJD1Yolj4ESV21b72k0w20jOXvtwdkxOTrHohN9v2oCBWDNFSNjSC--sEX14AXSakiwSubFX-y8nJ6tKxB_c2a7ORq-12NfwcuYzqboygiXz2AVwi4qJEkV8R-J7xHyue0l7WxCuwSMW-HBo03kaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تسنیم تصاویری از حمله پهپادی به یک نفتکش منتشر کرد که سعی داشت بدون هماهنگی با مقامات ایرانی از تنگه هرمز عبور کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121313" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121312">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
دوستان ما در پیام رسان‌های داخلی هیچ کانالی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121312" target="_blank">📅 17:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121311">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9AkjOft93HmykOY-0Gr6iK92RjxHJx4NrMXZHcyj25ASR-gF7ADWqffywIkDX53wndwIWTumgkGqWpX_lvU87IlPmNWEFeVsLqhE6edM7yk751fxpYOhtawFg-XTNUmvi9S24WxH704ThZGWwRXKvwQ_INpO_rApVPIXxZqULFQ48qxUL-o4sbFHxHBqF8o_dZWp4Pi8gZVNBmzIjeP4H4FDW7wNPMg7aT3IanmuB1KTHj-uw63Y6Pyv5_ZRlMk_uKzXXOQq-uvPz7QBcG8Dp8ZDMx6G2biqATItWB37WKPvZE43BVDYo3Amt6J3Gtdsmo24M3qH7kWAQxZnkW4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: آمریکا دوباره در جنگی بی‌پایان که در آن امکان پیروزی ندارد گیر خواهد افتاد
رئیس مجلس در حساب کاربری خود در شبکهٔ ایکس، عبارتی از فصل ۱۱ کتاب خاطرات ونس، معاون اول رئیس جمهوری آمریکا نقل کرد:
🔴
«ما احساس می‌کردیم در دو جنگ بی‌پایان و بدون امکان برد گیر افتاده‌ایم و سهم نامتناسبی از سربازان از محله خودمان (محله فقرا) آمده بود.»
🔴
این وضعیت (گیر افتادن آمریکا در جنگی که نمی‌توانند ببرند) دوباره در حال تکرار شدن است. این بار فقرا و فراموش‌شدگان آمریکایی باید هزینهٔ جنگ‌افروزی الیگارش‌های نزدیک به کاخ سفید، افراد شیطان‌صفتی همچون جیمی دیمون و لابی تاجران جنگ در واشینگتن را بپردازند.
🔴
گفتنی است جیمی دیمون مدیرعامل موسسه مالی و بانک جی‌پی مورگان در آمریکا و از مهم‌ترین چهره‌های حلقهٔ تامین‌کنندگان مالی جنگ علیه ایران است که اخیرا نیز علیه کشورمان لفاظی کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121311" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhL_cW9WSTETIPhmDVPTrUDxYPxOeP4wSWMDgoMYomXGlAzL-wABMUtEzTyzXPeYyhs83rYj27zrXlJBge6ZKYE2CJ3sL_WeSJxiPsztuu42uyit65GGf54zfqMzQIWaAZklidPIU5wO6FQb9jDzKEBMXzQ16VyddwLtEGQ6RXq15LDzK7VwNYWyF2qa6Fp5KmoRF3L1ZFmimsb0nA1XRh5fNj1MxpffCNADr8dQN8FtTWe6mZD3aN123ukq1LDtrZb10HdnysCOO2aQRqhBAc9DYEN7m0R3KGNcKli9zF4N8SBKKFpmGoMs6Cg2MfK8CdvjAc_m1biAYWY7NaBCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله
بنی گور وزیر امنیت ملی اسرائیل به گیدعون ساعر وزیر خارجه:
برخی در دولت هنوز متوجه نشده‌اند که چگونه باید با طرفداران تروریسم رفتار کنند.
انتظار می‌رود وزیر خارجه اسرائیل درک کند که اسرائیل دیگر کشوری نیست که به راحتی تحت فشار قرار گیرد.
هر کس برای حمایت از تروریسم و هم‌سویی با حماس به سرزمین ما بیاید، کتک خواهد خورد و ما دیگر لایه‌ی دیگر صورت خود را به روی او نخواهیم چرخاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121310" target="_blank">📅 16:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121309">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urCFY1X45udA7es1d8dD164R2cpO-vLKYzVCYuXfBD2a3br6q8VJT9vNvZA6E5IQhR788WjuUvnc5lgcNjTgzw40MA-O_skSpoCGp8DEkWg_FWQjChKUiO3urlD20-OlWSBl9wShTX5phaWSu9r2cL5GK0x2Ts8qfFLeaxCwS1Bzzx1DKXjd4vwMwfED8r8z6Zqwo0iv_Xj9K4xA4gAtl_p1iURq3C9G_SKYGcWR3fdvEHEIQ3EIHx6aTSPCWHKRwYsk-N4gFjYbibu-PCiFPrZPGIcfdDfqzjOMSJjGNFY3TAOU_jhlL4zVkxAH_kBEGJ9Ch_fEsRAcP-rz7bu9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
درگیری بین وزرای اسرائیلی به فضای مجازی کشیده شد
‼️
🔴
وزیر امور خارجه اسرائیل، گیدئون ساعر، به بن-گیور:
به عمد به کشورمان در این نمایش ننگین آسیب رساندید - و این اولین بار نیست.
شما تلاش‌های عظیم، حرفه‌ای و موفق بسیاری از افراد را خنثی کرده‌اید — از سربازان ارتش اسرائیل تا کارکنان وزارت امور خارجه و بسیاری دیگر.
خیر، شما چهره اسرائیل نیستید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/121309" target="_blank">📅 16:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24468a4f6c.mp4?token=QVV6Z6FVnkZmyNBznspRqmmPZ-RTahPLSbxfxwqZme8VLyMQn_ajnb7BxWIdq_8Szw8Mk0R8ORcKXgMtxxRoRE8TbziQWDo6XwSOT5qpKGIVwZic44JFghLX0gtPeq8LqeXz_cJ2sKaSmucRi0pcs0uJhRkBuEoJY8jVv6MF5DxwjQjfvSRGFSyDCLXjom8MRzLt8QhUG2FihMYq43okTSak4vsuJTf-GVvOcpjD-KU0ZEetgxsRs9RSzonHS6F1IULFqfw-73612AF4RDklZk8lwIWOuJ5wpATKKVen5xkn50I0k2gHITKsMhJp6IQCOGV3V93wdbgxdMGeuD9qSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24468a4f6c.mp4?token=QVV6Z6FVnkZmyNBznspRqmmPZ-RTahPLSbxfxwqZme8VLyMQn_ajnb7BxWIdq_8Szw8Mk0R8ORcKXgMtxxRoRE8TbziQWDo6XwSOT5qpKGIVwZic44JFghLX0gtPeq8LqeXz_cJ2sKaSmucRi0pcs0uJhRkBuEoJY8jVv6MF5DxwjQjfvSRGFSyDCLXjom8MRzLt8QhUG2FihMYq43okTSak4vsuJTf-GVvOcpjD-KU0ZEetgxsRs9RSzonHS6F1IULFqfw-73612AF4RDklZk8lwIWOuJ5wpATKKVen5xkn50I0k2gHITKsMhJp6IQCOGV3V93wdbgxdMGeuD9qSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ممدجواد ظریف:
بر دهان مستکبران خواهیم کوبید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121308" target="_blank">📅 16:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121307">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
تخفیف خفن فلش‌نت فقط به مدت ۵ ساعت!
⏰
از همین الان تا ۵ ساعت آینده،   تمام سرویس‌های ربات با قیمت ویژه هر گیگ فقط ۹۰ هزار تومان ارائه می‌شوند.
🎉
هدیه ویژه به مناسبت رسیدن خانواده فلش‌نت به ۲۲۵ هزار نفر
💎
۵ گیگابایت — ۶۵۰ هزار تومان
💎
۱۰ گیگابایت — ۹۰۰…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121307" target="_blank">📅 16:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121306">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
تخفیف خفن فلش‌نت فقط به مدت ۵ ساعت!
⏰
از همین الان تا ۵ ساعت آینده،
تمام سرویس‌های ربات با قیمت ویژه هر گیگ فقط ۹۰ هزار تومان ارائه می‌شوند.
🎉
هدیه ویژه به مناسبت رسیدن خانواده فلش‌نت به ۲۲۵ هزار نفر
💎
۵ گیگابایت — ۶۵۰ هزار تومان
💎
۱۰ گیگابایت — ۹۰۰ هزار تومان
💎
۵۰ گیگابایت — ۴ میلیون و ۵۰۰ هزار تومان
⚡️
فرصت محدود و تعداد سرویس‌ها محدود است.
🤖
همین حالا از طریق ربات فلش‌نت خرید خود را انجام دهید قبل از اینکه تخفیف به پایان برسد!
🙏
تیم فلش نت
@Flashnetofferbot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121306" target="_blank">📅 16:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121305">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا، رفت رو مخ حکومت کوبا و گفت وقتشه یه فصل جدید با مردم کوبا شروع بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/121305" target="_blank">📅 16:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121304">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b55e5d1e.mp4?token=CJ4HMJTvitUmhv6v5VLNXIlgnisXXA1lBTZEOKE3IOJ7-xn0ZBVYuOdrRKuWDir1q5pSRpzlk0xpvA5jnwBpGHGFfCA4YGOaLIhO6FWpkHqUQvNOzNXBppFpZFmDyIfx6K5hm848lZiHdheORK4t6f8Pig50Z0cGy-mqPT24AwTjr8B8MR3Jgc_KEY2bhj6yt-c0ug4M8Qr4EWSVRU0RRpd07Pb6D1FKBA7LlZ7VmK9cSRCcSlPr0Ts_f9NYsLybKv--WCQEzz14_p8rhTutuMwenwF491-UZmmZ-6cT5OSXxYeSFbgYymntcAHZEA8-h6z7ybjDZbNI1DC9zTIORQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b55e5d1e.mp4?token=CJ4HMJTvitUmhv6v5VLNXIlgnisXXA1lBTZEOKE3IOJ7-xn0ZBVYuOdrRKuWDir1q5pSRpzlk0xpvA5jnwBpGHGFfCA4YGOaLIhO6FWpkHqUQvNOzNXBppFpZFmDyIfx6K5hm848lZiHdheORK4t6f8Pig50Z0cGy-mqPT24AwTjr8B8MR3Jgc_KEY2bhj6yt-c0ug4M8Qr4EWSVRU0RRpd07Pb6D1FKBA7LlZ7VmK9cSRCcSlPr0Ts_f9NYsLybKv--WCQEzz14_p8rhTutuMwenwF491-UZmmZ-6cT5OSXxYeSFbgYymntcAHZEA8-h6z7ybjDZbNI1DC9zTIORQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: روسیه میداند استفاده از سلاح هسته‌ای واکنشی ویرانگر خواهد داشت
🔴
مارک روته، دبیرکل ناتو، در پاسخ به سوالی درباره احتمال استفاده روسیه از سلاح هسته‌ای در جنگ اوکراین گفت: «آنها میدانند اگر چنین اتفاقی بیفتد، واکنش ویرانگر خواهد بود.»
روته جزئیات بیشتری درباره نوع واکنش احتمالی ارائه نکرد، اما این اظهارات در ادامه هشدارهای مکرر ناتو و کشورهای غربی درباره پیامدهای استفاده از سلاح هسته‌ای مطرح شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/121304" target="_blank">📅 16:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121303">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612df8d7aa.mp4?token=vJfKzt_NUM-PrSMpFehYzEI_JtujhChiMwvm8jh6Go9Tm6bWZOhEC8ovNJhPgaSr2GK25qcJWCsjmhkTTM-NqcKTMr50SgUYwZVNUkVhMrUbwx9mUjwb6Ckyg6FS_QYwjmYZ5_LnAhCbs7Sf6nMOTpszBzBl8PLET34w-OVMmyA092txAMvKM3gU_Xp2iGdI-7xUhL5rv5U-VA1D1ohFUMBld5Tka3dNvVVI-6kh0majimMr718jCwWKnjiXRIKYrnb_bzK8OUuKiTxpH9d_SFp1reE4jDoUnbgCSBJrx97hZB2dKEB2kxW7l219K0eiemaI8OGhB6MFoH1p_QCaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612df8d7aa.mp4?token=vJfKzt_NUM-PrSMpFehYzEI_JtujhChiMwvm8jh6Go9Tm6bWZOhEC8ovNJhPgaSr2GK25qcJWCsjmhkTTM-NqcKTMr50SgUYwZVNUkVhMrUbwx9mUjwb6Ckyg6FS_QYwjmYZ5_LnAhCbs7Sf6nMOTpszBzBl8PLET34w-OVMmyA092txAMvKM3gU_Xp2iGdI-7xUhL5rv5U-VA1D1ohFUMBld5Tka3dNvVVI-6kh0majimMr718jCwWKnjiXRIKYrnb_bzK8OUuKiTxpH9d_SFp1reE4jDoUnbgCSBJrx97hZB2dKEB2kxW7l219K0eiemaI8OGhB6MFoH1p_QCaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: وابستگی بیش از حد اروپا به آمریکا پایدار نیست
مارک روته، دبیرکل ناتو، اعلام کرد اروپا به همراه بریتانیا، ترکیه و نروژ بیش از ۵۰۰ میلیون نفر جمعیت دارد، در حالی که روسیه حدود ۱۲۰ تا ۱۴۰ میلیون نفر جمعیت دارد.
او گفت با این حال، اروپا همچنان برای دفاع از خود در برابر روسیه بیش از حد به آمریکا وابسته است؛ کشوری با حدود ۳۵۰ میلیون نفر جمعیت که نقش اصلی در تامین امنیت ناتو را بر عهده دارد.
روته تاکید کرد: «این وضعیت در بلندمدت پایدار نیست.»
تحلیل: اظهارات دبیرکل ناتو در شرایطی مطرح میشود که جنگ اوکراین و احتمال کاهش حضور نظامی آمریکا در اروپا، بحث درباره تقویت توان دفاعی مستقل اروپا را دوباره پررنگ کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121303" target="_blank">📅 16:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121302">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-uTUsYuRoHHhtD5DHJ3n50Yoa5r9U579kM4nFTiRuZ8oXHt0Ut9sRfTxKqAGqv8Qj6Z3uwZ7-Ex1TQLzeDcpr7u0U5X3rUp0cY9CdbunBTNW8lKtR5g_4s6ZbBdqjWl7xpMT3sEmYtEca_u_H7Ep5lz8oHdk76BpNnU2Sn_FQ-Xr9sJEmtmueZhl0F8pEOODWWYUPc4QDDn56amREp2k4NJvURH8I877uRNwXhyxuSvT0zpKDY6H8GPMTDLYU6Q4CAipe4hmS42XgFfEsdC5YMco9R0B1HYo3l9xFEjKKFxszvesYn2hiH-HY6MfOy9_ThWCAyANJCCFmF_6pAQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بن‌گیور، وزیر امنیت ملی اسرائیل، از فعالان بازداشت‌شده در کاروان جهانی صمود غزه در بندر آشدود بازدید کرد.
🔴
به اسرائیل خوش آمدید، ما اینجا در کنترل هستیم. این همان چیزی است که باید باشد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121302" target="_blank">📅 16:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121301">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKj44UEYNYMlQI-1n6DEr5nNQrtEECU3dXn_fKhEGiWCuFy2eN6NsYWc65uKxlbpW0MEBFz61VSbmlit4s90lhzJkQTiXM0GedjF2gJxD6tdpBZcGK7GGGhcrVgLzDoGYHcuF5qW2a-mx0bkdnaxWESw4yxygFbki1zJ5GnySCEMj48Fm1y0PDFWHdmYOhwNGnircUSX_ssM2hv_l7eVGCZB7vJearXsvKfR1IqRjZfLryCVfqptfyL7_qe96n82HACx2yQ3opAVZme-IV3qEv9aqhNxWCqHYwx1LIGv-99d8E6aFok_L7ee9GpTHLkieeK4qzkKZ7c5zDfI6PKi3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه خانواده پاکستانی اسم 2 پسر دوقلوی تازه متولدشون رو "علی خامنه‌ای" و "علی لاریجانی" گذاشتن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/121301" target="_blank">📅 16:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121300">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2668c9eb.mp4?token=XudHcyQ4lgOPOBjz3GDBY3n-suV6oKvxxNhT-w0MXZ7l_xNt6CnYIne7-LZeM6O5KofHjshdX9zj24bG34wfa--hwPuMDcJUnLm9apApU-wnWvnlTHLypP03U2jTgOrCn_5R8zgsh8O9LkrGRzzQ9EqtrPvmS-zI2YIdPBW5dv0XRa-M7-Hjwc-oetQw-ISGE_k3mR_rDPvxirERz6lOkCMh5aacjRZRImFIeXUhO9pAWPp64-nOsXtwxM0J6cSg5w6IN11HyvyuJ59Gf5F-Nfbg4r_sW22cw6SSikffcPCtYiUXSzlJCGT_ipVppAZP6CKnqM_tF1vB9_NLH7sKBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2668c9eb.mp4?token=XudHcyQ4lgOPOBjz3GDBY3n-suV6oKvxxNhT-w0MXZ7l_xNt6CnYIne7-LZeM6O5KofHjshdX9zj24bG34wfa--hwPuMDcJUnLm9apApU-wnWvnlTHLypP03U2jTgOrCn_5R8zgsh8O9LkrGRzzQ9EqtrPvmS-zI2YIdPBW5dv0XRa-M7-Hjwc-oetQw-ISGE_k3mR_rDPvxirERz6lOkCMh5aacjRZRImFIeXUhO9pAWPp64-nOsXtwxM0J6cSg5w6IN11HyvyuJ59Gf5F-Nfbg4r_sW22cw6SSikffcPCtYiUXSzlJCGT_ipVppAZP6CKnqM_tF1vB9_NLH7sKBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به الدویر، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/121300" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121299">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016dec75b2.mp4?token=rkJCU9AGMv0snXP0xue-gWyH79lgCDqLwcQTlmN559JLF5YlOFtbWp84Eqgd98fswtN5afhozLk3FD5Ys6eK9CT5UWQhj-liUG3RaUXklUWV2ZBK04N7hvO_RDY51iwmCx_IWXBYBoT8arSJeS_RrLZQgc9Yy4tYObUWj855ESszgJEwOSjU0tY-kJgnYoMd4XNEbQ893ihrmLaV4jBlmVhPF43jaw0BUqXX2CtRqD6sJEgEmB8bRX6RcmXQPbqHutk1IpMJvyWiU94BDB9zbX625WU5wTpean0J2Pfiz59c-hu80Oy72VhkbJhf-vhxJUwYygnD2NcGYz66yTSi7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016dec75b2.mp4?token=rkJCU9AGMv0snXP0xue-gWyH79lgCDqLwcQTlmN559JLF5YlOFtbWp84Eqgd98fswtN5afhozLk3FD5Ys6eK9CT5UWQhj-liUG3RaUXklUWV2ZBK04N7hvO_RDY51iwmCx_IWXBYBoT8arSJeS_RrLZQgc9Yy4tYObUWj855ESszgJEwOSjU0tY-kJgnYoMd4XNEbQ893ihrmLaV4jBlmVhPF43jaw0BUqXX2CtRqD6sJEgEmB8bRX6RcmXQPbqHutk1IpMJvyWiU94BDB9zbX625WU5wTpean0J2Pfiz59c-hu80Oy72VhkbJhf-vhxJUwYygnD2NcGYz66yTSi7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویر دیده نشده از شب ۱۸ دی
👑
حماسه‌ای که ملت شیر و خورشید رقم زدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/121299" target="_blank">📅 16:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121298">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
حزب الله تصاوير منتشر کرد که نشان مي دهد يک fpv به يک باتري گنبد آهنين در محل اسرائيلي جلال العالم در مرز حمله کرده است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/121298" target="_blank">📅 16:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121297">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bfdabb819.mp4?token=D2IRCJ6QkB4nLUi2QX6J3SEUb1J7K8WGq8j3KQeLr08FxYa9C7Aa-UyteFyCii0XWiVxvOm-CGtKvkuN8vZzLN9pJDc53cX0fFDwClE7L2zdE03jynlTW1jXhK70FRg80yzTXoCwKvbIwVdWYoElqQhMyIjsS65TJ5WTiC6IoE_FTDttL2xvimOYkfQ3p97VjKts68lriPJ5Zg9HC8eRwFGovzGDt1piJSX5nGvCs15o62Q87pxf-xuvB_GT0lsi5-ukhKfLRKGI--4CMImT0faNtBEMYmGJsyuF1WKEv3-KBgvHk6jH834ofMujWvlXZ_EqJoO11i2WqDWVDiJu9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bfdabb819.mp4?token=D2IRCJ6QkB4nLUi2QX6J3SEUb1J7K8WGq8j3KQeLr08FxYa9C7Aa-UyteFyCii0XWiVxvOm-CGtKvkuN8vZzLN9pJDc53cX0fFDwClE7L2zdE03jynlTW1jXhK70FRg80yzTXoCwKvbIwVdWYoElqQhMyIjsS65TJ5WTiC6IoE_FTDttL2xvimOYkfQ3p97VjKts68lriPJ5Zg9HC8eRwFGovzGDt1piJSX5nGvCs15o62Q87pxf-xuvB_GT0lsi5-ukhKfLRKGI--4CMImT0faNtBEMYmGJsyuF1WKEv3-KBgvHk6jH834ofMujWvlXZ_EqJoO11i2WqDWVDiJu9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ظریف: ما نیاز به تضمین از قول‌شکنان و پیمان‌شکنان نداریم/ مردم و نیروهای مسلح ما بزرگ‌ترین تضمین برای ما هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/121297" target="_blank">📅 16:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121296">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/121296" target="_blank">📅 16:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121295">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs3_qutmuwAz0sU-bQy7iMFdqE43_aIITHQIseQWhD6i4j6GgPiij0maIqxk5DU5JM0olpOsXaZSBVI47_FEzabCgzRwSniV1feb0Soes-M1pXq3XfbbWDjj4jWzHaw5cw7ZGIawOlCabDbBkXko3tCdHTHgAzmAmY2BTmFIY5ezLdw5_CY0dylVoXZ7sjEA6OkpAPgW9u6IN5uJ6-eNP8Sbossn-3W3rKm9pw0l1KKOa2u0gxUCXGSqa_Eq4jAcnxtEblvUmw7n97OMSPDEXoMTbWRudf-wi9cb5vo88zTqL0Rhx1PjTQq3A_ZfhfCoyri8ZH8SN6fnxLBEoAwpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ۹۰ کشتی رو تغییر مسیر دادیم و ۴ کشتی رو غیرفعال کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/121295" target="_blank">📅 16:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121292">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIuNqOiFOZytWS5W6FxpNKDJo5o7mkS4HHaOmFSM3P3FwnGu93r0rp90r0bQ9QBVeBnS2inOjEtMu6SMG-9I6Rt7X6GYTzIoSr2rScAiHQlVF_NOMmYR9-j8ja_tQzM1jiRl5JlxTCODUZCK8aLCbjxbVZwqSOpZdVqIFz7imIWvRoyeL0dCC_a4bo0JPPbUm9mIhbx0gPrDfe28lTjicZ5icWqVGFuFxW8xfMIV1sTp-pMJcG9CTW2dOLvxzCpR3U1MdeVyOvSsPDsG3FAlHubtbr8fZ0npo5IAd-Aaco8jJIUFBknhI5ZoA5rjlpfu1Tue6yhB8u7E1BEpUfhIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8e6d5c062.mp4?token=fR995SI7pe4LTZG4ZkA6CInoYOlb1v8Avuf7te3XDHP_TV6lrBHiKFnTaC4-6YFvZs02-XRKzMSMLfmrQlQcqce37y8q_XYiEzBOmDwXLZSxcy8ELPNCSJi7gV_w_ZxYCDTZBch4kJ2Iwdh_SskSYBDvkl9ogbSAYYenikUSZv0HZG8BC4gKA9eNLskbcuRBPFt_xF1zg_nHmQGeeAy4avPPztCVrc3WzkJ71mhnzK8YMglGaxtnQDa9p-M2zdxHqVEyFTPitfwVY1nh4iOanchG8fp0LG-U7T0u-68fUi7ahTuEI8DOI_tXG5S0XKGoLFJvJIZJFxy0FnJguq8J_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8e6d5c062.mp4?token=fR995SI7pe4LTZG4ZkA6CInoYOlb1v8Avuf7te3XDHP_TV6lrBHiKFnTaC4-6YFvZs02-XRKzMSMLfmrQlQcqce37y8q_XYiEzBOmDwXLZSxcy8ELPNCSJi7gV_w_ZxYCDTZBch4kJ2Iwdh_SskSYBDvkl9ogbSAYYenikUSZv0HZG8BC4gKA9eNLskbcuRBPFt_xF1zg_nHmQGeeAy4avPPztCVrc3WzkJ71mhnzK8YMglGaxtnQDa9p-M2zdxHqVEyFTPitfwVY1nh4iOanchG8fp0LG-U7T0u-68fUi7ahTuEI8DOI_tXG5S0XKGoLFJvJIZJFxy0FnJguq8J_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوهای که داخل رسانه‌ها وایرال شده، یه فرد شبیه چهره علی خامنه‌ای، هست و دست راستش هم آسیب دیده
🔴
میدونم AI هست ولی دلیلش چیه که دارن اینارو رو نشر میدن؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121292" target="_blank">📅 15:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121291">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MH6VZYy0r4OQL-HfOMs98IzsdgCSPYwbcU8ZexqKWyiPI8cOWlIBMGCw4DPzkEFfRieNwy2MOSVaRu2jHOyWLZie3WnAX5as6W5UGk31wlKUS21fpUNVMMsOe6EfoHwpH-j1gEvqQual1IJtPHaxgGzt596mTV7syO7vn_k9SX089sqnqHH3zhvHlaOUyj9qEyWVXfRKddKEcr6UWvk8S7WrojSE1hrgT2F-AC3O-wWcXzG_miWe-In59ulRz8byqdiDwFIfcTaffze3tul0DY37hnf90WjSTGlRkdxOJzas_vhojTuc1X91MeZCSucB2grAPRe3zKJ_tRz4IY2TUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دریایی سپاه: ۲۶ کشتی با هماهنگی نیرودریایی سپاه عبور کردند
🔴
تردد از تنگه هرمز با کسب مجوز و  با هماهنگی نیروی دریایی سپاه درحال انجام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/121291" target="_blank">📅 15:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4ycoI3wK1hyHMbaQzKA80_N2zqwuNGezMvof14DCF-JSW4nYBiRP3BFH1HWmnSMSzOU2_TD_8ug87F3yfFip-JNiAimJXJ2KMRJXMuk0obnsoghUF5CmY73KjZPH4nlMzSqkQNvpB-Wjs7x5eYfai_C6ZDm_D9TdiFFh6XRP90JAhp0OJSvQlmyungNXH6YiOzXDpvEW-hiKX0slliq5v-voBMj2SfY_YTvCQbyyZsjlSezFeyXsl9WwH94j0XskJ-f35XlkKbSpNZYRU0j77a8Ns9UlbeZlSENJjADeJqK9yF2mBotjlq5ZHY1COO5jidhO-6vtJfRfvJ0opxq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عقاب‌های دفاعی جمهوری‌خواه در حال بحث درباره راه‌هایی برای مقابله با خروج برنامه‌ریزی‌شده نیروهای نظامی پنتاگون از آلمان هستند، طبق گزارش NOTUS.
🔴
قانون‌گذاران در حال بررسی درج مقرراتی در قوانین آینده مربوط به بودجه و سیاست‌های دفاعی هستند که می‌تواند تأمین مالی کاهش نیروها را مسدود کند یا نیاز به بازگشت تغییرات اخیر در استقرار نیروها را ایجاد نماید.
🔴
گزینه دیگری که در حال بحث است، اعمال تعلیق بر نامزدهای وزارت جنگ است که نیاز به تأیید سنا دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121290" target="_blank">📅 15:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
منابع دیپلماتیک به سی‌بی‌اس نیوز گفتند که سفر وزیر کشور پاکستان به تهران بخشی از تلاشهای فشرده اسلام‌آباد برای میانجیگری برای توافق صلح با افزایش تنش بین آمریکا و ایران است.
🔴
یک دیپلمات ارشد پاکستانی گفت پاکستان برای یافتن راه‌حل، تلاش‌های خود را دوچندان کرده است
🔴
او افزود: اسلام‌آباد کلافگی‌ها را درک می‌کند، «اما از سرگیری جنگ برای همه یک فاجعه کامل خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/121289" target="_blank">📅 15:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121288">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
منابع شبکه العربیه
:
آمریکا به پاکستان اطلاع داده است که در مسئله هسته‌ای و مسئله تنگه هرمز هیچ امتیازی نخواهد داد
🔴
منابع افزودند که ایران تضمین‌های آمریکایی برای پایان جنگ را «کافی نمی‌داند»
🔴
آمریکا به پاکستان اطلاع داده است که در مسئله هسته‌ای و مسئله تنگه هرمز هیچ امتیازی نخواهد داد
🔴
منابع افزودند که ایران تضمین‌های آمریکایی برای پایان جنگ را «کافی نمی‌داند»
🔴
پاکستان از «انعطاف‌پذیری محدود آمریکا» در برخی از نکات اقتصادی مطلع شده است.
🔴
آمریکا درخواست‌های خود را در مورد مسئله هسته‌ای و امنیت دریایی در تنگه هرمز تشدید کرده است.
🔴
ایران هنوز معتقد است که تضمین‌های آمریکا در مورد یک جنگ جدید کافی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/121288" target="_blank">📅 15:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121287">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سی‌بی‌اس به نقل از منابع دیپلماتیک:
اسلام‌آباد تلاش‌های خود را برای حل مناقشه دوچندان کرده است و معتقد است که شروع مجدد جنگ برای همه فاجعه خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121287" target="_blank">📅 15:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121286">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
الحدث درمورد مذاکرات ایران و آمریکا: پاکستان از انعطاف محدود آمریکا در برخی موارد اقتصادی مطلع شده
🔴
آمریکا خواسته‌های خود را در بخش هسته‌ای و تنگه هرمز تشدید کرده است.
🔴
ایران همچنان معتقد است که تضمین‌های آمریکا درمورد عدم ازسرگیری جنگ کافی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121286" target="_blank">📅 15:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121285">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d857cfaf.mp4?token=rhMq2_NkLt0ZbdZKbpy2GabV0NOF8GMkyaHQb9fYjPHsmPq2FBQTtk02XaOfqCdEoA1TjCSyAiQWp-BKcD7tyW9sVKBj0x_PzOAYxzEHEHiMTIH-V4381t_hv72UOI02miGyh00tCpfqMj8Fo_KfYy5TQZGWuR0CISjUPZwLugsPM4rJ-8YzcqPfjEnKzJMnr01VolUnivo1GslrYlZw0TPFYPJ_6SYO-zRs49wPmzT271gITcSvmILeN1QTaPRtcbXu10j4DFNRB2K-NCC-1LtnF-EN_xCBZ3EEI22JbUy2uget9uW7ZkmQT8lj_m88ga9H3f4XhOSW8LFH2ZLpsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d857cfaf.mp4?token=rhMq2_NkLt0ZbdZKbpy2GabV0NOF8GMkyaHQb9fYjPHsmPq2FBQTtk02XaOfqCdEoA1TjCSyAiQWp-BKcD7tyW9sVKBj0x_PzOAYxzEHEHiMTIH-V4381t_hv72UOI02miGyh00tCpfqMj8Fo_KfYy5TQZGWuR0CISjUPZwLugsPM4rJ-8YzcqPfjEnKzJMnr01VolUnivo1GslrYlZw0TPFYPJ_6SYO-zRs49wPmzT271gITcSvmILeN1QTaPRtcbXu10j4DFNRB2K-NCC-1LtnF-EN_xCBZ3EEI22JbUy2uget9uW7ZkmQT8lj_m88ga9H3f4XhOSW8LFH2ZLpsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا، کیر استارمر، اشتباه کرد و گفت که بریتانیا با کره شمالی توافق تجاری امضا کرده است به جای کره جنوبی.
🔴
او پس از دریافت یادداشتی متوجه اشتباه خود شد و سریعاً آن را اصلاح کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121285" target="_blank">📅 15:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121284">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزیر نیروهای مسلح فرانسه: ناو هواپیمابر شارل دوگل به منطقه عملیاتی شبه جزیره عربستان رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121284" target="_blank">📅 15:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121283">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YISoXma3UwJUOnvBf3zZ58qFkHoyaCUwf773dmxQ_JQNmAO5EDBKrES-D23bLuWG0VHVAg8TBAn_zKNuam98Qn5rGiXHJkPoJr2IQzFKPBR6g_V_ZsXkzy72ctP8xuvmYcxwZDbiYlQTkXUY_IT9a5Lp2cxuKaryh1Gxc5JJMfcelgvWl5zDSz83DeRF35SPF13t0dZTwjAJNm3gpYizXKJUbsyEIloNqlb4f6ik8VROO7ZyPN2Nm4Q9QsUgqfRwZi3HTqhlqeBqJsjXDwgajJ2uYOLoNKuz96sl0UgWyY-NBuUgzrWH84l44xKty_RZiaOqSfLSJ_hNiEzgFHds1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
از امروز، نیروهای ایالات متحده ۹۰ کشتی را تغییر مسیر داده و ۴ کشتی را غیرفعال کرده‌اند تا اطمینان حاصل شود که قوانین رعایت می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121283" target="_blank">📅 15:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4dbb78ffa.mp4?token=cje3LiTxQFlqH5Iwbp-MHox0RzL4slmUMs2nvC75KPKmei9fW2j9co5RVv5JG4JRp4DKNCs12NJTJEdXXlaLX2Oy3f25RLzAja9dS-SK7tjwA3pc_BmreE2eBRjw0sjzinETEgNg0vwbv0cOoeXplJATev__rmUp3mF23q4SRXcETse4A5g8GFkN_Il4p75u1m52s-PwLu2PT42_jOxCoUNRgoBZJ6apJiMYJmpvUW2o5m72F3Gi9lFAw6Ib4D1f820noZemsm3wnXSy2Qe8IbgacK1dxm7iWGebwwa6NS4NtsVHkK6T4EuckXYlXh4wMvqG9ffX810ZpBCzVx2Jmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4dbb78ffa.mp4?token=cje3LiTxQFlqH5Iwbp-MHox0RzL4slmUMs2nvC75KPKmei9fW2j9co5RVv5JG4JRp4DKNCs12NJTJEdXXlaLX2Oy3f25RLzAja9dS-SK7tjwA3pc_BmreE2eBRjw0sjzinETEgNg0vwbv0cOoeXplJATev__rmUp3mF23q4SRXcETse4A5g8GFkN_Il4p75u1m52s-PwLu2PT42_jOxCoUNRgoBZJ6apJiMYJmpvUW2o5m72F3Gi9lFAw6Ib4D1f820noZemsm3wnXSy2Qe8IbgacK1dxm7iWGebwwa6NS4NtsVHkK6T4EuckXYlXh4wMvqG9ffX810ZpBCzVx2Jmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر مجارستان، پتر ماجار:
اوکراین قربانی است و حق دارد با هر وسیله‌ای که در اختیار دارد از حاکمیت و تمامیت ارضی خود دفاع کند.
🔴
هدف همه، دستیابی به آتش‌بس پایدار و صلحی پایدار است که توسط جامعه بین‌المللی تضمین شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121282" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
صداو‌سیما: سرریز نفت در خارگ صحت ندارد و دریا سالم است
🔴
عبور شناورهای ملیت‌های مختلف به‌ویژه شرق آسیا از تنگۀ هرمز بیشتر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121281" target="_blank">📅 15:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل: پس از هشدار درباره یک حادثه امنیتی مشکوک که در منطقه نوفیم اعلام شد، نیروهای امنیتی در آن منطقه جستجو کردند و یک ساکن اسرائیلی از جامعه را در نزدیکی حصار شناسایی کردند.
🔴
نگرانی از بابت حادثه امنیتی وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121280" target="_blank">📅 15:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66d1114edb.mp4?token=Gqy4_4aOPHIg-4p0RbVMYamzV-gRXYNMvMjOxgbPVD4LfUSq7_CH_kOuJuEu7WZN_YroPNMRhzAdDLYZeoFFcCYnu9-SxEvy0YFLZxjfG86qafulf6gjb6SLB65v16lZRr4rqjch5pTpPMzTBH5Pg2-ryfCFUL-8DPzUS6JXBbNEuf_zH7vR8CLdz-hBpDA2t4otGI2sZQypwTIv3D0WpSKQvc48iBBfzxyLmIcf9QVT6AosAXHKoZQHB5kCC4cm5iMJZnUnFxMp4mNfcM9k64DKKUKKIZPFt4I0EM1ORTOcaLDtKFoKqq768byiU4btQ6FOtAjkkiTf2qXcR5KIMTIp0V-0u_hLMUi_O0wwq9dpVIBHm3lufnfrXfWkRArLItTTo3a_0K4Y1BuG1owY4azG8zICbALF64Wi74WUeuH8-qx5M4MUw3k0ucX7dbOMaGmF3t6WMM0g2hXf7Z38QR3s6EhfCIwZUKP5r67g3LDkZAnmxR_iU1CqYYol_pqMYGj8GJzHOMrlvbYFG3LjaKveF0TjpdW-RRRHZj5l4F_NN4gUGvj3LAPjPj-Xjx6ZLuEuJZkUKkY2fR9r4XtwEPd-zm_02aUzl82eVhyjQL_ll6dn4ZEp4vrgpI3lURx2bO-lqDEt4DiUhsxo87uqxoNILsaZKZQbYE5ib2vyTlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66d1114edb.mp4?token=Gqy4_4aOPHIg-4p0RbVMYamzV-gRXYNMvMjOxgbPVD4LfUSq7_CH_kOuJuEu7WZN_YroPNMRhzAdDLYZeoFFcCYnu9-SxEvy0YFLZxjfG86qafulf6gjb6SLB65v16lZRr4rqjch5pTpPMzTBH5Pg2-ryfCFUL-8DPzUS6JXBbNEuf_zH7vR8CLdz-hBpDA2t4otGI2sZQypwTIv3D0WpSKQvc48iBBfzxyLmIcf9QVT6AosAXHKoZQHB5kCC4cm5iMJZnUnFxMp4mNfcM9k64DKKUKKIZPFt4I0EM1ORTOcaLDtKFoKqq768byiU4btQ6FOtAjkkiTf2qXcR5KIMTIp0V-0u_hLMUi_O0wwq9dpVIBHm3lufnfrXfWkRArLItTTo3a_0K4Y1BuG1owY4azG8zICbALF64Wi74WUeuH8-qx5M4MUw3k0ucX7dbOMaGmF3t6WMM0g2hXf7Z38QR3s6EhfCIwZUKP5r67g3LDkZAnmxR_iU1CqYYol_pqMYGj8GJzHOMrlvbYFG3LjaKveF0TjpdW-RRRHZj5l4F_NN4gUGvj3LAPjPj-Xjx6ZLuEuJZkUKkY2fR9r4XtwEPd-zm_02aUzl82eVhyjQL_ll6dn4ZEp4vrgpI3lURx2bO-lqDEt4DiUhsxo87uqxoNILsaZKZQbYE5ib2vyTlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: می‌دانیم که چین در دور زدن تحریم‌ها و تحویل کالاهای دو منظوره فعال بوده است.
🔴
من هرگز در مورد نقش چین در جنگ روسیه علیه اوکراین ساده‌لوح نبوده‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121279" target="_blank">📅 15:06 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
