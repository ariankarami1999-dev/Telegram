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
<img src="https://cdn4.telesco.pe/file/vTwKHL0SD_peP_Vtu02mtyH8TQVdJt4TY51i9LYQCvALDmFEe5N6iYyWVlUYK014mVuyrPbRQ5teV-6Sdt4_beW98dJhcioT8Bx_XsXMnriLiNq4_Nu3guGqldaHUHoOj5ergAH9GW5dntAqh5EVYDMxw_XcPRGfIeruc3-Hzp0LOxgLmAsKH7W93QQ1x7rNme36eVVU1-aPEPvnvbi-EKqVGwihkI4_N5ngvWvNNdM_CdXPpCHxm2XZYNBDdsPnQKcumHCS80Zr_T4lIZC9DPaVvSAK-RDNHKd39hf0aLjRrw0BHvza9VNA7KApzvfJSuIie5oLa50JSBGcOBcGdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 20:30:22</div>
<hr>

<div class="tg-post" id="msg-15677">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26cd4a0fb.mp4?token=DcW4iI8TP3FihLCOgsAtT_5xWaTrF-oC1govTT6kQQNjTWd6KNX2rL0KJnRy6clCzr22-94Q1u99O25ywF9hxQmreBd-6efQrOY4QQVpOH03XiiN0muQah0BHyYRAVCjRh2o19gaeAaMe_gueU4kDjvcy5oBYU2s1IWAgQxUigTC5h2i384jOimeJuHqfWpGx_mpsglw1QrCwtJMio8oMZgCrB7kBTA_rJkz6YvcZYc9kIPSfUu61YRb_iHO9EnW-aWRLQ4yu5-edqAVPJMP6g-vZ8OWnWGw29LKMkP7PPvVykeyzZ0gCsNGIms5aNfyPfnykBAny6Sq0m09c0HLhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26cd4a0fb.mp4?token=DcW4iI8TP3FihLCOgsAtT_5xWaTrF-oC1govTT6kQQNjTWd6KNX2rL0KJnRy6clCzr22-94Q1u99O25ywF9hxQmreBd-6efQrOY4QQVpOH03XiiN0muQah0BHyYRAVCjRh2o19gaeAaMe_gueU4kDjvcy5oBYU2s1IWAgQxUigTC5h2i384jOimeJuHqfWpGx_mpsglw1QrCwtJMio8oMZgCrB7kBTA_rJkz6YvcZYc9kIPSfUu61YRb_iHO9EnW-aWRLQ4yu5-edqAVPJMP6g-vZ8OWnWGw29LKMkP7PPvVykeyzZ0gCsNGIms5aNfyPfnykBAny6Sq0m09c0HLhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان دکترای افتخاری از پاکستان دریافت کرد
@withyashar</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/withyashar/15677" target="_blank">📅 20:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تتر 163K
@withyashar</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/withyashar/15676" target="_blank">📅 20:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/withyashar/15675" target="_blank">📅 20:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vlt-Z5aqnE_4yBKJP6AjRWnTAYtIF5r73NXk7ZlgbzAVQtxlP4UTJDew8GeK4WMA4lS9oT7B-bNfPQkWWVSbZ741RHCTJ2KwsWuczBnD_BcJtRW_kB3_M4jq61SVuoTo7q_31iIPiE7Xecm7fGr9L0PiqMp7G07hblCHxBIg9pcLdBSg-4EgEHlR-twtz5-nsPqFw4y5vUt6NgpSPMCcBZE46aq-Hf__SaZBkhpjOnX7khfAG-r73z-sb9bwtTVp4TQIjO0Yla8WM7JWCdOxkkQ8Lo8QWCCZp8-412E6plTgZlqxnVuzfQ7uzBWVIcSsSU-UPJD2WktpSDyypCgGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شواهد نشان میدهد مدیران دفتر انتشارات مجتبی خامنه‌ای دقیقاً امضای ابزار یکسان ، نسخه یکسان و سیستم عامل یکسان دفتر انتشارات قالیباف استفاده کرده اند.
در‌نتیجه هر دو نامه قالیباف و مجتبی خامنه ای با یک کامپیوتر نوشته شده در ابتدا و بعد از اوایل ماه ۶ میلادی، اوایل خرداد ماه، رایانه را از مک به رایانه ویندوزی تغییر داده‌اند.
@withyashar
پیشتر در ویدیو اتاق جنگ گفتم که ای آی دست ممباقر هست!</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/15674" target="_blank">📅 19:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ریاست جمهوری لبنان:
ونس و وزیر خارجه آمریکا خواستار تشکیل یک کار گروه آمریکایی، لبنانی و ایرانی برای تثبیت آتش‌بس شدند
آن‌ها گفته‌اند که ترتیبات مربوط به حوزه اختیارات این کمیته و نحوه تشکیل آن، در دست بررسی است
@withyashar</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/withyashar/15673" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15672">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هاآرتص به نقل از منابع آگاه: تل‌آویو علاقه‌مند است در مذاکرات واشنگتن راه‌حل‌هایی پیدا کند که مداخلهٔ ایران را از تحولات لبنان دور نگه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/withyashar/15672" target="_blank">📅 18:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15671">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4IbgHGZtAvuGFRMnUxmFMcWyyogHpUz0YcRmDo8H9QLZP9CAsXjsxkniWC6b8NRS9otMKXH4hqXncTf1NLZpkT-TUTiL4W-MzJXaK81jwJJAa1Bycc_Hj11NW62EJErCHHeGAQuBJD8_V_jH7f1CTvB5BVsHjRtqEf_zNwO3GVM2cQuVQdQLvkqXS8ewPx7p-KkXh1HqUwG2d7l4D4Hlznf-1-wOaj4zZb_POefkNdc9w0uBIST6UTYsnlXuA8YlgMR9sGMZ6jLCbeKtT3-aI0ENf9VCASyUj9SoEiY0ZXSbtqa8uzZQKmiQXoLGMivxuc_-gqnJuyEpuBWtH7T0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ما هستیم ناو ها هم هستند نگران نباشید
ناو هواپیمابر USS جورج اچ. دبلیو. بوش (CVN 77) در دریای عرب(شمال‌غرب اقیانوس هند ابتدای دریای عمان جنوب ایران ) در حال حرکت است.
دو ناو هواپیمابر به فعالیت خود در خاورمیانه ادامه می‌دهند در حالی که نیروهای آمریکایی همچنان حضور دارند و هوشیار هستند.
@withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/15671" target="_blank">📅 18:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15670">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عمان و ایران بیانیه مشترکی منتشر کرده‌اند که در آن قصد خود برای ایجاد یک مدیریت مشترک آینده برای تنگه هرمز را تأیید می‌کنند
این بیانیه همچنین به طور ضمنی تأیید کرد که مطابق با استانداردهای بین‌المللی
هزینه‌هایی برای خدمات دریایی اعمال خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/15670" target="_blank">📅 17:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15669">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فایننشال‌تایمز
:
با وجود افزایش سطح تردد کشتی‌ها در تنگه هرمز، مالکان همچنان سردرگم هستند؛ این وضعیت در حالی شکل گرفته که ایران کشتی‌ها را تهدید به عبور از مسیر نزدیک سواحل خود کرده و آمریکا مسیر عمان را پیشنهاد می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/15669" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15668">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هم اکنون حمله پهپادی هدفمند به خودرویی در جنوب لبنان،گزارش ها از ترور چندین عضو حزب الله.
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/15668" target="_blank">📅 17:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15667">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شهباز شریف نخست وزیر پاکستان: مذاکرات ایران و آمریکا شامل دارایی‌های هسته‌ای، موشک‌های بالستیک و دارایی‌های مسدود شده ایران خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/15667" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzn-TaOvCWUnOrNSy2KyFgj5q8TvYQeIOiYKJSPlZNLRs-P-J02AMaoAoDtZIuIgARSDTn8kV9SOUPRlwWGZqzvl3VhUVRxiWgoxIoZtKmS8VoO5OeEYod8xx4RSxxA5rsEhdvDXIvGH94d-Us-zMFixEWDVC1fkJymHCtfB4nYVhTa0NrzWExOC_AV0XuNJz6Jzxq9oM6mL0ULDQeejaKaedD78gqdbcgNYDF5YwwVIUjHbw0zUxHrzPLdIgDxqUkv8S-JKCYJ4nhJUGWnDdZ9GqQhZBDkxbi-DrL1V0OA5iLcQbGaByX7pon-4UHIkOx_WixMUPTVDMQGjVtbFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز دایرکتی از طرف یکی از شما دریافت کردم که گفت از‌ کارمندان رتبه دار بانک است و این قطعی نه هک است نه چیز دیگری و به طور عمد از طرف خود رژیم انجام شده وی افزورد تقریبا با یقین میگم پایین اوردن دستوری قیمت ارز و طلا،حاکمیت و دولت با سرکردگی همتی و سیف میخواهند در قیمت های پایین فقط خودشون خریدار مطلق باشن و یک نوسان جانانه از بازار بگیرن با اختلال عمدی در سیستم(چون میدونن سرمایه دارها میدونن قیمت برگشت میکنه به بالا و پولشون رو میکشن بیرون که طلا بخرن،اما با قطع عمدی و به گردن هک شدن)
در نتیجه از دوستان هکر قدیمی دوران جوانی جوییا شدم که در امنیت سایبری بانکها کار میکنند. آنها به من گفتند که بعد از عملیات اکونومیک فیوری که آمریکا انجام داد که شامل محاصره دریایی هم میشود و تمام زیرساختهای اقتصادی رژیم را هدف‌ گرفت رژیم ضربه های مهلکی در رابطه با ارز خورده و این ادعا درسته و میخوان پول رو از جیب مردم جبران کنند دوستم گفت شعبه ها هم دسترسی به هر انتقالی را دارند ولی دستور این است که بگویند قطع هست
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15666" target="_blank">📅 15:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15664">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6rYuIlzLvr0srlB5ppQ2idlT2cQfmZkFZNOopLbQl17kY01uoty0NtoQuLqfVWwnl3GNKm-Xakrd5bPqKEQsq2kALlQl_D6DgrVXUH8ZvzBs5VaB6Ggzuf--qdICQFJCayKLkg9zhit9uQoFH-_X6L_ILbmUSSgZ5cVnuMQJRv7LOslEtRvMqj944OW3Q_LKJSvXAhcW1BCJ07U-xxU3TVjhvsyTYny29MjmH_Rr9rNZTKqdyx4WIUgxbRMJ5Z8QlQiH5p-z7NiV21mNYsTagk4aS3jJCfwrhVagTHJjpECpxPqKzaidyCgWzuZtv3iUX-UqdWEpuqsyHrNQKi5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلبان آمریکایی جنگنده F-15 که در ماه آوریل بر فراز ایران سرنگون شد، به مقام‌های اطلاعاتی گفته است که پیش از اجکت کردن، چندین پهپاد ایرانی را دیده که به‌صورت هم‌زمان و هماهنگ در آرایشی شبیه «عروس دریایی» در حال حرکت بوده‌اند؛ به گزارش سی‌ان‌ان و به نقل از چهار منبع.
این روایت باعث بحث در جامعه اطلاعاتی آمریکا شده درباره این‌که آیا ایران توانسته قابلیت پیشرفته‌ای در زمینه پهپادها یعنی «شبکه‌سازی مش‌مانند یک‌به‌چند» (one-to-many meshed networking) را به نمایش بگذارد یا نه.
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/15664" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15663">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3xrOjei0vYRP3DZT9BHOc9YJYHD3rWueINWHTOcFyKU4Q4CIFhmuom1gCZ-VYOcIV2-o6rECE5YU_VZyFyvUU8ppBeD6gpbUarn2_npHKSW5LEjgTXB3lejQmjqzG10b8kbKHGJI-Pp32U1MjvLA14UNfKzASVN3rN4bXaf2qHAnMnlJ1Y0Vz_blRhjvnpJfhDFDKbxk3pLx1e68Zo6RdM9C4-CMNogbS_sqBnKHk8kY3Sg6W1SBNBPwDYtc-f_7BcE2yMQVsYriKB_PLCmBOPq42ABq3zsXd3_2ZI2mcegrJUtIHx--VrXFie9_Z-xzDb7SnVpzvBiSQCcem38dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
اگر آنها با این موضوع موافقت نمی‌کردند، مذاکرات بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات عمده‌ای که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی بیشتری اعمال نشود. با این حال، همه کشتی‌ها در محل باقی می‌مانند تا در صورت لزوم محاصره دوباره برقرار شود، که در این مرحله بسیار بعید به نظر می‌رسد.
پول و یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، در حساب امانی تحت کنترل آمریکا قرار می‌گیرد و صرف خرید غذا و تجهیزات پزشکی، به طور انحصاری از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما خواهد شد.
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود!
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/15663" target="_blank">📅 14:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15662">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZNc0K5SfnuVfSq0KJTrP6fWZjOgX1oFyD32Sd5rBzVHyoXcxhPdqUlAfk13ONWQXn_6q0dzysxVYFseVbvUM-5R4pt3vR7OKsKzO0XzHxh1j2YaFHTTLpRq6GIHWn03ErVtUBJU2VLY7AmHUsnUYUkYVLcSmjZPuBX2MIVSc4u1wLOyJIzZoQcRfgqAoZ1lIt3ycoxULpmANYUYoa5f0YercW0pNVdmCxyu7mrgNaOqdQJDV5uieaYNKbMSYZjsNbVQSmue2MvGuO26otOgHqTMz2RBknoPn7KsG8-Q2maf-0cKqlE-LJMWZP_4ixwHO3tmcSeHIYTcRQPjpKROyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان وارد اسلام‌آباد شد
وی در بدو ورود با نخست‌وزیر پاکستان دیدار کرد.
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/15662" target="_blank">📅 14:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15661">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=j05qs-QQ8f1fd_5V21DlhVQT-T0aYNwRE8bJeiu0vP-rU40P9e_CFfm6fbzSXQ7_Nk290zS7r8qYythAIovdu2FvSfiACy6N09vhXFeG2Ek857W-xOlDQqMZFVaMJ_DPnSrPT8Jq9SHBA23kXFu3TiKA1a7jAhnLZTggLeN9bZWaV0AnaKJ4xS6mszTUD512PlrL-nqfB2WEiy8gFLq_1PwPbexikQGdjUSEIUMaqfQs9Sg5c0qNGCZ8ot1fEjyukr7p6FtsSkyXHfygh1HxkY8Y4Az72cUqJkXJHtv27nXgqS-rlRF9ckqEgSqvCCKYmm00B9gNHfTIZg2lQqykAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=j05qs-QQ8f1fd_5V21DlhVQT-T0aYNwRE8bJeiu0vP-rU40P9e_CFfm6fbzSXQ7_Nk290zS7r8qYythAIovdu2FvSfiACy6N09vhXFeG2Ek857W-xOlDQqMZFVaMJ_DPnSrPT8Jq9SHBA23kXFu3TiKA1a7jAhnLZTggLeN9bZWaV0AnaKJ4xS6mszTUD512PlrL-nqfB2WEiy8gFLq_1PwPbexikQGdjUSEIUMaqfQs9Sg5c0qNGCZ8ot1fEjyukr7p6FtsSkyXHfygh1HxkY8Y4Az72cUqJkXJHtv27nXgqS-rlRF9ckqEgSqvCCKYmm00B9gNHfTIZg2lQqykAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژیم : هک شدیم ، داریم روش کار میکنیم و مشخص نیست کی‌ درست بشه ! شرکت خدمات انفورماتیک: تیم‌های فنی و متخصصان امنیت سایبری در حال رفع اختلالات ایجادشده هستند تا امکان بهره‌برداری دوباره از خدمات فراهم شود. ضمن عرض پوزش بابت وقفه پیش‌آمده در انجام امور بانکی،…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/15661" target="_blank">📅 14:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15660">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رژیم : هک شدیم ، داریم روش کار میکنیم و مشخص نیست کی‌ درست بشه !
شرکت خدمات انفورماتیک:
تیم‌های فنی و متخصصان امنیت سایبری در حال رفع اختلالات ایجادشده هستند تا امکان بهره‌برداری دوباره از خدمات فراهم شود.
ضمن عرض پوزش بابت وقفه پیش‌آمده در انجام امور بانکی، از تمام کاربران و مشتریان محترم تقاضا می‌شود ضمن حفظ صبوری و شکیبایی، اخبار و اطلاعات تکمیلی در خصوص زمان بازگشت به وضعیت عادی را صرفاً از طریق درگاه‌های اطلاع‌ رسانی رسمی و مراجع ذی‌صلاح پیگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/15660" target="_blank">📅 14:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15659">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">روزهای شنبه و یکشنبه ۱۳ و ۱۴ تیر، تهران و دوشنبه ۱۵ تیر، کل کشور تعطیل است  معاون اول رئیس جمهور اعلام کرد در روز سه شنبه ۱۵ تیرماه استان قم و پنجشنبه ۱۸تیرماه استان خراسان رضوی تعطیل است. @withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/15659" target="_blank">📅 14:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15658">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">روزهای شنبه و یکشنبه ۱۳ و ۱۴ تیر، تهران و دوشنبه ۱۵ تیر، کل کشور تعطیل است
معاون اول رئیس جمهور اعلام کرد در روز سه شنبه ۱۵ تیرماه استان قم و پنجشنبه ۱۸تیرماه استان خراسان رضوی تعطیل است.
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/15658" target="_blank">📅 14:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سفیر ایران در لبنان در واکنش به حمله به جنوب لبنان: هرگونه نقض تفاهم‌نامه در لبنان، چالش‌هایی را برای روند مذاکرات صلح ایجاد خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/15657" target="_blank">📅 13:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اختلال دوباره در بانک‌ها
@withyashar
🚨</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/15656" target="_blank">📅 13:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15655">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVgbuiICbh2uq3mu43FTsK9qo6YsCsKiXwan3KaC0_OqkPFqCerlhh3bp5OneAscFupMmk20DodUG00g_TWlOK8-J___z9NKjrkB3FaROPnWslGm1jqe7bV6Vk_GRS-9LPXGNvyLMm5XmVRIg1HCuWmSMtSl7kfVHiSNz3hsL3UDmucuJpsNzCgPmHnu7dYPZZy1RcCUKnKHqcaJReTCsY0dVVAmXU7-gn6loajlhACvbQSag0jwNHA1TO0VBlM42-d1mdVY_gsmStRCignzyapSDSTMhPThyGnw1_JaygeCxYtewT2Xf0Y59E4Ark4r9aEtnTg4Z-008fPC6gB_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقض دوباره آتش‌بس ،حمله اسرائیل به جنوب لبنان
@withyashar
🚨</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/15655" target="_blank">📅 13:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15654">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نتانیاهو: حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم @withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/15654" target="_blank">📅 13:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15653">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رادیو ارتش اسرائیل: تا زمانی که حزب‌الله کاملاً منحل نشود، از منطقه الشقیف در لبنان عقب‌نشینی نمی‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/15653" target="_blank">📅 12:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15652">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو: حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/15652" target="_blank">📅 12:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFTBjVh7eswexiOMDftCxx0nQ-kWSLbiqMpIfJZRr9mHu3jIG1guo6xHenntrlnd5a8bIqD07UbpEaFTBltmXXIoOApMyBjyGmMM6BzgDsvXtRSfNvjx0qpSSYGLuUZ6BJ6wOURNK7nVoI-XRCmVWX2MoJKZt70DOYTHXruy6qu9KRuCQW4kljXHXO3vj_UcOg8dmV0ty7UYFCOzVThO-AXkRTTSnYJfULUkUTMnTm5tZbJGGw0d-DW46lRrJlvPB3gExPy851PXiw_liUGfcxirxiGcWvWoXtBsMsC71nDTAqH3OaF-DTdN_0mCh_nkcPcfAJ2gDOPkLuoZld6wjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون ۷ سوخت رسان شامل، ۵ فروند سوخت رسان KC-135R و ۲ فروند سوخت رسان KC-46A پگاسوس نیروی هوایی آمریکا در منطقه خلیج فارس فعال هستند.
همزمان، دو فروند KC-46A با نام عملیاتی BOBBY 81/82 از پایگاه RAF Mildenhall انگلستان به پرواز درآمده و برای الحاق به یک یگان جنگنده در حال عملیات‌اند.
همچنین بر‌اساس گزارشها پرواز CUBE 31 شامل چهار فروند جنگنده F-35 تفنگداران دریایی آمریکا در حال انجام مأموریت بوده و هماهنگی‌های عملیاتی و ارتباطی لازم را در جریان پرواز برقرار کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/15651" target="_blank">📅 12:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15650">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پلتفرم دریانوردی کپلر:
۳۶ کشتی دیروز از تنگه هرمز عبور کردند که این بالاترین میزان تردد در این تنگه از نخست مارس تاکنون است.
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/15650" target="_blank">📅 12:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15649">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:
اگر آمریکایی‌ها فکر می‌کنند ایرانی‌ها برنامه هسته‌ای خود را رها خواهند کرد، آن را لغو می‌کنند و از تمام رویاهایشان برای نابودی دولت اسرائیل دست می‌کشند، بسیار ساده‌لوح هستند.
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/15649" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15648">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: خودروسازان آمریکایی تولید سلاح را آغاز خواهند کرد
رئیس جمهور آمریکا در کاخ سفید به خبرنگاران گفت: «آنها برنامه‌هایی برای تغییر کاربری کارخانه‌ها دارند. ما قصد داریم سلاح‌هایی از جمله موشک‌های پاتریوت، موشک‌های تاماهاک و موارد دیگر تولید کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/15648" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15647">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هواپیماهای سوخت‌رسان نیروی هوایی ایالات متحده پس از تخلیه از پایگاه هوایی العدید در قطر به دلیل جنگ ایران(یک روز قبل از جنگ)، به این پایگاه بازگشته‌اند. حداقل ۱۲ فروند در حال حاضر حضور دارند.
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/15647" target="_blank">📅 11:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15646">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بقایی: توانمندی دفاعی و موشکی ایران هیچگاه موضوع مذاکره با هیچ طرفی نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/15646" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15645">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الجزیره: «تغییری بزرگ» در سیاست آمریکا؛ ایران اکنون می‌تواند نفت خود را با قیمت کامل بفروشد
این اقدام صد‌ها میلیون دلار درآمد اضافی برای اقتصاد ایران به همراه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/15645" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15644">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل:
جمهوری اسلامی ایران با بازگشت بازرسان هسته‌ای به ایران موافقت کرده و این اولین گام برای توافقی گسترده‌تره.
برخلاف برجام، این بار بازرسی‌ها باید در هر زمان و هر مکان ممکن باشه.
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/15644" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15643">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عماد الدین باقی: طبق بند 2 توافق ایران و آمریکا، از این به بعد شعار مرگ بر آمریکا یا سوزاندن پرچم این کشور و لگد کردنش تو مراسم‌ها و اجتماعات رسمی (مثل نماز جمعه) ممنوعه.
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15643" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15642">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">https://t.me/boost/withyashar
یه لول اومدیم پایین ایموجی کم شد لطفا اگر کاربر پرمیوم هستید بوست کنید و اگه نیستید از دوستانتون که هستند درخواست کنید بوست کنند</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/15642" target="_blank">📅 02:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15641">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">@withyashar
FPV  آتش بس و</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15641" target="_blank">📅 01:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15640">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">@withyashar
شصت روز سنگین</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/15640" target="_blank">📅 01:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15639">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8773aac7.mp4?token=XIyXD8_Hqkb9cplHl5_bHNfjDTyyQoTPvaQnDIKZJGaZRjHP9S7o6TkTIoEmpTHzFcRCA6XAWCwtYlfgU1MCzdSten1LIqU_tLo7OXeS7mBt21gAYfwb8s_SUTNaa9UDy_QIkTcLVg5FKtGrAG8IZYtekSdFF7bdTNSTbcrtnI1TvBzFrIieEh97wgQS3ewSuUyiARAYwvMawQD0E8vjssucbaLoNaUHz3C8acYolpyZqDmLQzyRaGkQYywEB-i79Y3NGCVnXFPyT2Nlcwsx2nnx-Bv3h5g9b9X98PyH5Shx0jTcs0BJowwBkp__H883xeGV46QEC2zgOHUPgQUypw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8773aac7.mp4?token=XIyXD8_Hqkb9cplHl5_bHNfjDTyyQoTPvaQnDIKZJGaZRjHP9S7o6TkTIoEmpTHzFcRCA6XAWCwtYlfgU1MCzdSten1LIqU_tLo7OXeS7mBt21gAYfwb8s_SUTNaa9UDy_QIkTcLVg5FKtGrAG8IZYtekSdFF7bdTNSTbcrtnI1TvBzFrIieEh97wgQS3ewSuUyiARAYwvMawQD0E8vjssucbaLoNaUHz3C8acYolpyZqDmLQzyRaGkQYywEB-i79Y3NGCVnXFPyT2Nlcwsx2nnx-Bv3h5g9b9X98PyH5Shx0jTcs0BJowwBkp__H883xeGV46QEC2zgOHUPgQUypw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا می‌توانید تضمین کنید که ایرانی‌ها از سود فروش نفت برای بازسازی ارتش خود استفاده نکنند و فقط برای دولت بعدی آماده شوند؟
ترامپ:
خب، آن‌ها قرار نیست این کار را بکنند، قربان. خواهیم دید، اما قرار است پول را برای خرید غذا برای مردمشان استفاده کنند، چون در حال حاضر مردمشان خیلی گرسنه هستند و آن را فقط از ما می‌خرند — ذرت، سویا.
تباید پول زیادی باشد. امیدوارم پول زیادی باشد.
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/15639" target="_blank">📅 00:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15638">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
با یک تماس تلفنی میتوانم محاصره را برگردانم
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/15638" target="_blank">📅 00:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15637">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ: هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران شود. @withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15637" target="_blank">📅 23:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15636">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قالیباف: اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/15636" target="_blank">📅 23:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15635">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ: هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران شود.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/15635" target="_blank">📅 23:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15634">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرنگار: نتانیاهو می‌گوید نیروهایش لبنان را ترک نمی‌کنند
ترامپ: ما قرار است به این موضوع نگاهی بیندازیم. من یک حل‌کننده مشکل هستم؛ می‌توانم مشکلات را سریع حل کنم، از جمله با بیبی.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/15634" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15633">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: «تا زمانی که ایران به ما احترام بگذارد نمی‌خواهم از واژه “ترس” استفاده کنم چون مناسب نیست تا وقتی به ما احترام بگذارد، ما هیچ مشکلی نخواهیم داشت.
ما کنترل کامل تنگه را در اختیار داریم.»
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15633" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15632">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قالیباف در سفر به مسقط: در سوئیس توافق کردیم تا 12 میلیارد دلار پول مسدود شده ایران آزاد شود.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15632" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15631">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏زنده‌یاد⁧ مانوک خدابخشیان  ⁩: چه کسی می‌خوهد این رژیم را براندازی کند؟ چه کسی می‌خواهد پایه‌های این رژیم را اره کند؟
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15631" target="_blank">📅 23:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15630">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15630" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15629">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شبکه 14 اسرائیل که به نتانیاهو نزدیکه، مدعی شده ایران از یک «سلاح الکترومغناطیسی با فرکانس پایین» برای تأثیر گذاشتن روی تصمیم‌های ترامپ استفاده می‌کنه!   می‌دانم این حرف طوری به نظر می‌رسد که انگار از یک فیلم علمی‌تخیلی آمده، اما واقعاً وجود دارد و همین حالا…</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/15629" target="_blank">📅 22:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15628">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به کانال ۱۴ درباره لبنان:
امشب دوباره با ارتش اطمینان حاصل خواهیم کرد که دستورالعمل‌های کابینه برای هر مبارز روشن شده است
ارتش مجاز است هر تروریستی که در منطقه زرد شناسایی شده است و علیه هر تهدید واضح حتی فراتر از آن، ضربه بزند.
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15628" target="_blank">📅 22:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15627">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال‌استریت ژورنال:
ترامپ این هفته با رهبران پنتاگون و پیمانکاران بزرگ دفاعی دیدار خواهد کرد تا برای سرعت بیشتر تولید موشک و مهمات فشار آورد
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/15627" target="_blank">📅 22:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15626">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnYqQKSWArBgiET6C1OjWPvl-dKT8jcpAUv5R6FMkmWQHliDLJ_p5mQ5LwmHmqNLhPz4kuZfTfEaPHCE6fGfTZvPdEL5tgxc2H5bQH9m_BSLL8LWUxurNP8OZknzuUF76Tt5eW6tWLwaAKcEKxDFmjSAi_sB3mZvSJftUk1RK-LtcPZ42Hw0xTtN49JVhqKnr4iR-afuN17YgjM38yiPse__LoiypsBfYbMygn9jDnCtyie9jcCMjdNGRcgDAsRmD0Q8tMyughAjIP-wwDOnMNzDxAZ8jLq2B_Rl5BKNGTfcYp3YHBcU4TfuNfmreV877OVAwDPXwQWLdvd82kjPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای ممباقر (هیئت جمهوری اسلامی) همکنون در مسقط عمان به زمین نشست.
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15626" target="_blank">📅 22:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15625">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ونس معاون ترامپ لحظاتی پیش سوئیس را به مقصد آمریکا ترک کرد
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15625" target="_blank">📅 21:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15624">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fe556e38.mp4?token=HQSUN8Uiww7d-YgdQqHCQ-vOI_lmc2DjU0Yp86JWCM8EA52GU6vDkh4l7r7SakwnNzzlJFJ0bRxWMC7eGpITWylFwMgcxkrEMt_2qZhR1gnDXQuU-0_rOQf42MCZ2En5q7nSEswgT_B05tU5XitdiNsUcoBqr0hkxo806QjZIE97Uu8NbXtj-LYlWUuEZC4hHWzmIT8i1K7czcgnlmN-GQ3mA65JlN4iSvSNFewTkJbYhTpABDyv_y751arSnvgER1m2Y1tD5kzf-fJLa5pdzh-TTxeEuP-5-HRbo4cv6Vq6cFQ7gD8X9fnbyBnreSCu6kr3z8ST7kGid9YiPgkMEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fe556e38.mp4?token=HQSUN8Uiww7d-YgdQqHCQ-vOI_lmc2DjU0Yp86JWCM8EA52GU6vDkh4l7r7SakwnNzzlJFJ0bRxWMC7eGpITWylFwMgcxkrEMt_2qZhR1gnDXQuU-0_rOQf42MCZ2En5q7nSEswgT_B05tU5XitdiNsUcoBqr0hkxo806QjZIE97Uu8NbXtj-LYlWUuEZC4hHWzmIT8i1K7czcgnlmN-GQ3mA65JlN4iSvSNFewTkJbYhTpABDyv_y751arSnvgER1m2Y1tD5kzf-fJLa5pdzh-TTxeEuP-5-HRbo4cv6Vq6cFQ7gD8X9fnbyBnreSCu6kr3z8ST7kGid9YiPgkMEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با تقلید از ترامپ دم توالت هواپیما
: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشاله در این گفتگوها به نتیجه نهایی می‌رسد و تا به نتیجه نرسد، رهایشان نخواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/15624" target="_blank">📅 21:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15623">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDFeB7CvSSk3Kx63m7dTWpbICX9gyZQDB9QkDaPbbDD7Uac2ie-3hVKmDVIJX9f1KI1UlKi0tpEhxv8whg9oz4omR9s4LuNO1zOFodlbHGQOls-K7vcihYNFRKso4EaM8oy6DqZ82egVfjKCiVpRliDZv6deoMDMsd3I5d01hnuliDiWVjXK17E40YEpWocTrW4ZnqzhbF2h1Mlf-91zjqP-FoRicMIpdmJrz9mquGKasHxmImgBftdotQSgxka6J49PX-4he8KrazZwPD_D8uoLvOT1M1_i3cfFuRYgW91vdTC06h2Ms7f3w9VIzIs8N7kxw1X9TUSaDJcdHoaXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : همه کاملاً آگاه هستند که ایران برای تضمین «صداقت هسته‌ای» در آینده، با بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد. رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15623" target="_blank">📅 20:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15622">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شبکه 14 اسرائیل که به نتانیاهو نزدیکه، مدعی شده ایران از یک «سلاح الکترومغناطیسی با فرکانس پایین» برای تأثیر گذاشتن روی تصمیم‌های ترامپ استفاده می‌کنه!
می‌دانم این حرف طوری به نظر می‌رسد که انگار از یک فیلم علمی‌تخیلی آمده، اما واقعاً وجود دارد و همین حالا هم در حال استفاده است , این امواج رو داخل مغز ترامپ فرستادن. رفتار رئیس‌جمهور به‌وضوح تغییر کرده. چیزی شبیه تله‌پاتیه، اما از نوع الکترومغناطیسی.
روسیه این فناوری رو داره، چین هم داره و ایران هم بهش دست پیدا کرده.
باور کنید یا نه، از من خواسته‌اند این کار را انجام دهم و من هم روی آن کار می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/15622" target="_blank">📅 20:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15621">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مرندی: ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15621" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15620">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شاهزاده رضا پهلوی در اکس : در حالی که فیفا تلاش می‌کند پرچم شیر و خورشید را از ورزشگاه‌ها دور نگه دارد، هزاران ایرانی در ورزشگاه سوفای ثابت کردند که نماد واقعی ایران را نمی‌توان ممنوع کرد.
دفتر شاهزاده پهلوی افزود صدای مخالفان جمهوری اسلامی در جام جهانی بیش از هر زمان دیگری شنیده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/15620" target="_blank">📅 18:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15619">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تکذیب تعهد جدید هسته‌ای از سوی بقائی
سخنگوی وزارت امور خارجه:
تعامل ایران با آژانس بین‌المللی انرژی اتمی طبق روال جاری و منطبق با مصوبات قانونی ادامه می‌یابد.
بنا بر اعلام منابع مطلع، در مذاکرات ۱۸ ساعته دیروز در سوئیس، هیچ مذاکره‌ای درباره پرونده هسته‌ای انجام نشده و تعهد جدیدی از سوی ایران پذیرفته نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15619" target="_blank">📅 18:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15618">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">طبق اخبار درز کرده این معافیت تحریمی نفت ایران در ازای بازرسی آژانس از تأسیسات هسته‌ای ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15618" target="_blank">📅 18:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15617">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو: تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/15617" target="_blank">📅 17:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15616">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده رسماً معافیت تحریم ۶۰ روزه‌ای برای نفت، محصولات پتروشیمی و گاز ایران صادر کرده است
این معافیت اکنون تا ۲۱ اوت معتبر است و ممکن است تا زمانی که مذاکرات ادامه دارد و توافق نهایی حاصل شود، تمدید شود.
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/15616" target="_blank">📅 17:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15615">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8C2o0MtgM_8yd_498uVWzRWrx9JsDpdpBu8My53GVl418G0B4VxzD5zY3GcjQOJqRrVqphkYYV5_YjTQ8QUdTXkygH_PCb-85ywmkrr4nOL8ul5nFa26gxmW_9VQHO0SfVjP7i8TYcq_Gq2AuwyZXx17qmW5TwSTn2cfonfOUI_0gZ_hccNTULnRvpWj02kHV1WCYNeFUjnSlltZZqLJOEiZW9fdcPVqgWMVBrMuwPSlV0Y5Zsf7JqDKkexL9ElLphjy8ARiM1ZNu2Gkq9FflxjuD83baqq-_Xj0IYPEeyHErk1SW824Jn1MDt7uFXZXPKIYlK1XDrCC-NnBctpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بمباران توپخانه اسرائیل منطقه المشعع منصوری و منطقه بیوت السیاد در جنوب لبنان را هدف قرار داده است.‌‌
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/15615" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15614">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فاکس نیوز: ایران متعهد شده است که به آژانس بین المللی انرژی اتمی و بازرسانش اجازه دهد تا به ایران بازگردند تا بر روی مکان یابی و برچیدن تاسیسات هسته ای کلیدی کار کنند.
معاون رئیس جمهور ونس توانست به چارچوبی دست یابد که از بودجه مسدود شده ایران برای خرید محصولات کشاورزی آمریکا برای ایران استفاده کند و این محصولات شامل سویا، ذرت و گندم آمریکایی است.
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15614" target="_blank">📅 17:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15613">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">العربیه:وزارت خزانه‌داری آمریکا مجوز عمومی‌ای صادر کرد که اجازه می‌دهد واردات نفت خام ایران به مدت دو ماه انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15613" target="_blank">📅 16:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15612">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">طوفان در راه تهران
سازمان مدیریت بحران: مناطق نیمهٔ جنوبی، غربی، مرکزی و ارتفاعات تهران در معرض وزش بادهای شدید و گاهی بسیار شدید قرار دارند و احتمال وقوع طوفان در این مناطق از اواخر امروز تا روز پنجشنبه بسیار زیاد است.
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/15612" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15611">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72fc6efcdb.mp4?token=bK33fuERl8GjIndJTKSRTbyRTPQOa_A-cVGGd-iZ7qjFf7csYQkRwxNrMeAqrgcUzR6fl_IlN5qd1ctcS2cAZm0pNG2HAbwBzYnVznkuphxVSQ5EQVvJJWoE3JZUeINp-9mpR-eePC62nmjdDmUgDNZKnUGnDV1zcil4yAp47CmZyH4T3Pxhodhv8DZ9sc5YENoLB9p1DNuT47StbXceEDzCOnkhZZjEQSmI3LDoO6hOiCwcCucjojtEEIbo2v8lLl2-wD-zlPJS5251jsysFej1ClgeGl_bR9ePNzT3nd5xnmXiJuMDEUKXxrbLGJoCvZz-445baAi9y36Y_B6zzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72fc6efcdb.mp4?token=bK33fuERl8GjIndJTKSRTbyRTPQOa_A-cVGGd-iZ7qjFf7csYQkRwxNrMeAqrgcUzR6fl_IlN5qd1ctcS2cAZm0pNG2HAbwBzYnVznkuphxVSQ5EQVvJJWoE3JZUeINp-9mpR-eePC62nmjdDmUgDNZKnUGnDV1zcil4yAp47CmZyH4T3Pxhodhv8DZ9sc5YENoLB9p1DNuT47StbXceEDzCOnkhZZjEQSmI3LDoO6hOiCwcCucjojtEEIbo2v8lLl2-wD-zlPJS5251jsysFej1ClgeGl_bR9ePNzT3nd5xnmXiJuMDEUKXxrbLGJoCvZz-445baAi9y36Y_B6zzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک قابل مشاهده در تنگه هرمز نشان می‌دهد که حداقل ۲۴ کشتی در ۲۴ ساعت گذشته عبور کرده‌اند که همه آنها به جز یک کشتی با استفاده از طرح تفکیک ترافیک ایران قابل مشاهده بودند. به احتمال زیاد تعداد عبور و مرورها بیشتر از آنچه نشان داده شده است ، زیرا بعضی کشتی‌ها سیستم شناسایی خودکار خود را برای عبور خاموش  می کنند
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/15611" target="_blank">📅 16:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15610">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">معاون رئیس جمهور آمریکا ونس: ایران با ورود بازرسان هسته‌ای در این هفته موافقت کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15610" target="_blank">📅 16:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15609">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHdTrx3o71sfXzy3L-uzVkT9yWsdkmVzcqIrxiXJ1I6AwN96LiM_dObKRVTUWAibFDY3XuxGk5xqi_Imk3_YyLCoUB1B_bhWUnQa1b8jF-esdBNP4G1ca5GXaoj10ZxEdNkY9Tc__yE5Pnk8zpb4vtRspB8gs9rqJ4ejBd9dCfTYtfa-gDBlPncNmonA1EIKWTa3r22F6xLSvb9SWow-Yky7VdYYHl1e246oxXThX3jjv9E6mf2P04aOOV90qeUqWdYHvZ3J3YeRztAlAMC_lJa6kpND3xPK4SIPjmzShsZbdnDyjP7X3au89xj5RPvYSAm4aYfVnt0nBEO2DNE93w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : یا هر روز به جون هم میفتیم و به هم فحش میدیم و جونیمون میره یا همه باهم متحد میشیم و این وضعیت رو تموم میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/15609" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15608">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d6b1d15d.mp4?token=iprL4j1GjdJ_SHcUuqA7aCUFz1jMJXX4hJqa8ANicwXKeh76LEZkqejwbBHE-X37b_0LhWGk1sYLPAqGQT5jonjIVy1ShCyLWgnzt7I0hxRkPjLce4KCdsjj-if_IEn46KfaJlKAa55Fw5zsSRN10LWYxs3iUWFjKctY8jdgozO9Ip69q1fu9vwEw0cQVi7htLkagY3FkMJj72teeYHFN0vlJ5BtDL6bNT3U3vRNn1-O1WvxPER_Q1Dx9VFoloQtIvsQFffreCJTx75ud1hE88Opq46kdrH8B8fNC6Z4cWKGtRn2KQWK5DN25D1vqQe9FqIqu8sdwH5XHcaebMGmuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d6b1d15d.mp4?token=iprL4j1GjdJ_SHcUuqA7aCUFz1jMJXX4hJqa8ANicwXKeh76LEZkqejwbBHE-X37b_0LhWGk1sYLPAqGQT5jonjIVy1ShCyLWgnzt7I0hxRkPjLce4KCdsjj-if_IEn46KfaJlKAa55Fw5zsSRN10LWYxs3iUWFjKctY8jdgozO9Ip69q1fu9vwEw0cQVi7htLkagY3FkMJj72teeYHFN0vlJ5BtDL6bNT3U3vRNn1-O1WvxPER_Q1Dx9VFoloQtIvsQFffreCJTx75ud1hE88Opq46kdrH8B8fNC6Z4cWKGtRn2KQWK5DN25D1vqQe9FqIqu8sdwH5XHcaebMGmuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی : یا در مجلس را باز می کنند یا جلوی مجلس جلسه برگزار می کنیم مردمم ببینند
@withyashar
🤣</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15608" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15607">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوحه: دیدار وزرای خارجه قطر و فرانسه در سوئیس با محوریت مذاکرات ایران و آمریکا
هدف از این گفت‌وگوها دستیابی به راهکار‌هایی برای حل مسائل باقی مانده است
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/15607" target="_blank">📅 15:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15606">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جی دی ونس: معامله نهایی، خانه است. ما فونداسیون را بنا نهادیم. ما خانه را نساخته‌ایم، اما فونداسیون موفقی بنا نهادیم. @withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15606" target="_blank">📅 15:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15605">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ:
اگر پول‌های بلوکه شده ایران رو هم بخوایم آزاد کنیم شرایط رو جوری فراهم میکنیم که کشاورزان و تولید کننده‌های داخلی آمریکا سود کنند و مواد خریداری شده به دست مردم ایران برسه نه تروریست‌ها!
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15605" target="_blank">📅 15:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15604">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/15604" target="_blank">📅 15:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15603">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جی دی ونس: معامله نهایی، خانه است. ما فونداسیون را بنا نهادیم. ما خانه را نساخته‌ایم، اما فونداسیون موفقی بنا نهادیم.
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/15603" target="_blank">📅 15:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15602">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس جمهوری ایالات متحده: به آمریکا بازمی‌گردم، اما تیم‌های فنی به کار خود در سوئیس ادامه خواهند داد. پایه‌های لازم برای دستیابی به یک توافق نهایی با ایران را بنا کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15602" target="_blank">📅 15:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15601">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">عضو کمیسیون اقتصادی مجلس :
ملی، صادرات، تجارت و توسعه صادرات که هک شده بودن تا دو هفته دیگه وصل میشن
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/15601" target="_blank">📅 15:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15600">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ونس دوباره تهدید کرد: اگر صلح در منطقه اتفاق نیفتد رئیس جمهور ترامپ همچنان گزینه‌های زیادی در اختیار دارد
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/15600" target="_blank">📅 15:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15599">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ونس: به ایرانی‌ها گفتیم که وقتی شما حرف‌های بیخود می‌زنید نمی‌توانید انتظار داشته باشید که رئیس‌جمهور آمریکا پاسخی ندهد
👨‍💻
ایرانی‌ها تهدید کردند که مذاکره را ترک می‌کنند ولی نرفتند و تیم فنی آنها در حال حاضر در حال کار هستند
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/15599" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15598">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جولانی : در صورت دستور ترامپ، ده ها هزار نیرو رزمی متخصص جنگ شهری برای نابودی کامل حزب الله وارد لبنان خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/15598" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15597">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ونس: «باید سازوکاری وجود داشته باشد که اگر حزب‌الله شلیک کرد یا اسرائیل پاسخ داد، ما با هم صحبت کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/15597" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15596">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">معاون رئیس جمهور آمریکا ونس: ایران با ورود بازرسان هسته‌ای در این هفته موافقت کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/15596" target="_blank">📅 14:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر به الجزیره گفتند: این یادداشت تفاهم نیازمند تلاش‌های زیادی با شرکای ما در پاکستان، با حمایت منطقه‌ای، بود.
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/15595" target="_blank">📅 14:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15594">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جی دی ونس همکنون در سوئیس :  دیروز روز خیلی خیلی خوبی بود.  ما پیشرفت خیلی خوبی داشتیم.  ما دقیقاً کاری را که می‌خواستیم انجام دهیم، انجام دادیم. @withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/15594" target="_blank">📅 14:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15593">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8ab5474c.mp4?token=pKo7X9SoHPZ-Tt7-EEYQ1HwF20qwIniJRCXsptpIhrYGhW4GtKbbM_uTffYmtSU6Be1DLHrBB3KMBMII3Hm2ITk4LL3felSUut6tEQB-_GMAvA0VrZ6HkPX6-uzGDSUY_fepp0oPRHrj07c2d3KmPp-V3aNdDPrqwlEVrEyzfrdyhwf5io90YG9lXzD1jMJAK-DReXUqJS76pelzc2lBJIL-IW4F8Ilm83_t-37dwfMNs6cC7gB0qnY7fJu5QMJDCOCxVCWE_3eFQ96g8ZKXEYGXuAt0kSOpMe716n28lS-8O3UMuTdVuzc3yFBBqFtBooVHzpsOvGu_Alxe6BeN4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8ab5474c.mp4?token=pKo7X9SoHPZ-Tt7-EEYQ1HwF20qwIniJRCXsptpIhrYGhW4GtKbbM_uTffYmtSU6Be1DLHrBB3KMBMII3Hm2ITk4LL3felSUut6tEQB-_GMAvA0VrZ6HkPX6-uzGDSUY_fepp0oPRHrj07c2d3KmPp-V3aNdDPrqwlEVrEyzfrdyhwf5io90YG9lXzD1jMJAK-DReXUqJS76pelzc2lBJIL-IW4F8Ilm83_t-37dwfMNs6cC7gB0qnY7fJu5QMJDCOCxVCWE_3eFQ96g8ZKXEYGXuAt0kSOpMe716n28lS-8O3UMuTdVuzc3yFBBqFtBooVHzpsOvGu_Alxe6BeN4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس همکنون در سوئیس :
دیروز روز خیلی خیلی خوبی بود.
ما پیشرفت خیلی خوبی داشتیم.
ما دقیقاً کاری را که می‌خواستیم انجام دهیم، انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15593" target="_blank">📅 14:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15592">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ادعای سی‌ان‌ان : اجرای تفاهم‌نامه میان تهران و واشینگتن به مسیر صحیح خود بازگشته و تنگه هرمز برای دریانوردی باز است
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/15592" target="_blank">📅 14:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15591">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر امور خارجه اسرائیل: قصد عقب نشینی از جنوب لبنان را نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/15591" target="_blank">📅 14:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15590">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">المیادین:پزشکیان فردا به اسلام آباد می‌رود
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/15590" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15589">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b3269c0c.mp4?token=eLvbjqq9MLDZQHYbZ8NJ5Bxdey7Y2h_T8xcHHcKu8Ip951id0weLUFCN_cnFcYfrY2elQlM_NS8oz122iw48XbrzZvmb4CzJataw65qAksVqhl9toFkzLzFJYqiCwJepY7brKJR-uPx7ta7xp_-chNH8_wccTocWbWXJo3i4I0O51eWzQPDjdRhTji3km_femkk89LDA9vQz-Uy9cur-loebYrIl7L53r7x_NK3Xmr2jLZraGFZqZM---IxgXIkPDe76dV33JUWc41668-pTSdgTY8eYkIV_0SdCBB7-pMdC4MTztUgq7snDGSR_bXRmiAIYS8E7PH96nOMj1uxGbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b3269c0c.mp4?token=eLvbjqq9MLDZQHYbZ8NJ5Bxdey7Y2h_T8xcHHcKu8Ip951id0weLUFCN_cnFcYfrY2elQlM_NS8oz122iw48XbrzZvmb4CzJataw65qAksVqhl9toFkzLzFJYqiCwJepY7brKJR-uPx7ta7xp_-chNH8_wccTocWbWXJo3i4I0O51eWzQPDjdRhTji3km_femkk89LDA9vQz-Uy9cur-loebYrIl7L53r7x_NK3Xmr2jLZraGFZqZM---IxgXIkPDe76dV33JUWc41668-pTSdgTY8eYkIV_0SdCBB7-pMdC4MTztUgq7snDGSR_bXRmiAIYS8E7PH96nOMj1uxGbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️ بازسازی پل b-1 کرج
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15589" target="_blank">📅 13:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15588">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">همتی رئیس کل بانک مرکزی: مقرر شد اوفک معافیت تحریم‌های فروش نفت ایران را صادر کند
بر اساس بند ۱۱ تفاهمنامه ایران و امریکا معافیت (Waiver) باید صادر می‌شد که مقرر شد توسط اوفک عملیاتی شود .البته صادرات نفت ما هم اکنون درجریان است ولی از این پس بدون هزینه های جانبی تحریم خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/15588" target="_blank">📅 13:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15587">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سی‌ان‌ان، به نقل از یک منبع اسرائیلی: اسرائیل در حال بررسی اعلام عقب‌نشینی نمادین از سرزمین‌های اشغالی خود در جنوب لبنان است.
اعلام عقب‌نشینی نمادین به عنوان بخشی از مذاکرات پیش‌بینی‌شده در این هفته صورت می‌گیرد.
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15587" target="_blank">📅 13:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15586">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9abae6608.mp4?token=TqqFfmwNjnUeiT_XxF17WX-2BAiYX_4RvPUBZqjET2l6nJcBmk_XAAZ9FQOyvqJ6n64kvNewPHlnx2yAfvFlDx4LW6PAvncrdqJ8YVPsCUysSodsw0gsS43LpInDR5sdFa9yOaOpldwgsca6KN9R8TX3b45XzW1FjCjI7uOLSgCX0HAUJyQNQloLHpIBllygft06pF_Ms1EeWQ_O5Th66JEyTFMc8h0CAxOM260xjElVKIM7OxRcfLIOUbFeRWHTTq_edYEhTipkvRjCgG54LQpgdklhckWOhg8u_hNQ8kdWEFM75Tv6bpQl-CCbebOUQFsH24OS9cuSctxQiBkxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9abae6608.mp4?token=TqqFfmwNjnUeiT_XxF17WX-2BAiYX_4RvPUBZqjET2l6nJcBmk_XAAZ9FQOyvqJ6n64kvNewPHlnx2yAfvFlDx4LW6PAvncrdqJ8YVPsCUysSodsw0gsS43LpInDR5sdFa9yOaOpldwgsca6KN9R8TX3b45XzW1FjCjI7uOLSgCX0HAUJyQNQloLHpIBllygft06pF_Ms1EeWQ_O5Th66JEyTFMc8h0CAxOM260xjElVKIM7OxRcfLIOUbFeRWHTTq_edYEhTipkvRjCgG54LQpgdklhckWOhg8u_hNQ8kdWEFM75Tv6bpQl-CCbebOUQFsH24OS9cuSctxQiBkxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مجلس شورای اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15586" target="_blank">📅 13:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15585">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایتا رو زدن
پیامرسان «ایتا» دقایقی پیش از دسترس خارج شده است.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15585" target="_blank">📅 12:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15584">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFhBowZDJA2g3JNza8o7jxsCHVM9HAhFdAr-1aNzAUgjJj8_-VDh8zuIoyt6mIjnFVVdBolKjs3sO_cXXvtztGFB9eR0zuPHyTcIFN-fLS8yW46vb9Tunock4bsbHfrL_T7ETooE8QTb3BrbBK2ODC2OiITt0JyRJ959R7HFY2HHrTf1liuMQBVyNI570jnGQaIhypzFz1HO64Id6ssPtB3PcBjLlIIuz-aAjASl_zjQ2In3nxPLcyKFOQ8Ps_BegC2-_zqVb7ObTpx45pb-U-j7HvOxXbBgkTqAU9M138qPp4hkAyx1F-D0ZkyzpoFOR0p1H5_f_cI_zmau6LF1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم غریب‌آبادی دیپلمات ارشد جمهوری اسلامی و از چهره‌های شناخته‌شده پرونده هسته‌ای ایران است. او اهل علی آباد گلستان است و در سال‌های گذشته سفیر ایران در هلند، نماینده ایران در آژانس بین‌المللی انرژی اتمی در وین، معاون بین‌الملل قوه قضائیه و دبیر ستاد حقوق بشر بوده است. اکنون معاون حقوقی و بین‌الملل وزارت امور خارجه و از اعضای اصلی تیم‌های مذاکره و پیگیری پرونده‌های بین‌المللی ایران است. لقب «کاظم دستکج» را کاربران فضای مجازی پس از انتشار ویدئویی از او در یک نشست بین‌المللی رویش گذاشتند؛ در آن ویدئو گفته می‌شد خودنویسی را از روی میز برداشته است، این ماجرا به یک شوخی و کنایه سیاسی در شبکه‌های اجتماعی تبدیل شده
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15584" target="_blank">📅 12:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15583">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by6NCqjDgwEUXK_mJM7c5UTOanz5hFQ6TkVUoBGWibraYlv6a6DLUapLDWToF4WE9wsiEQL5Izg9ZwwgcHZaul1LxopQQICFII5cgEiuiSDj5NUtguMkOm23Gv8899AQg-fA6-ABSGlGi7VdYR0iILGzJ2GySJ8JvrTIsK7zj0lSPFDofQURqqkXEjEw2GMc0s5V9OFdOZIuMN3TKQhZlpySjSZRhygOlkmMa9BhvGgmrn3VFlddsiWgDoVmcptpzJZ4EdCjUskX1Xe1JhPdc5e_G24j-AxfEpDj8NFGCKMipexLu9OPaSSf5WLQP2qBi3H8nBNCvquMIv-vzsaKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هیئت جمهوری اسلامی (همه بجز کاظم دست کج) زوریخ را به مقصد تهران ترک کرد
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/15583" target="_blank">📅 12:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15582">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd0c99669.mp4?token=rncfMPSX81CBos_Wxn7HXuObsirJ6UWecD0fj1Q-fUXF7zJzmGAesUCgZvbbBsM5fptS7bnCoR18AyOBz384tf8uHqSX7v6EOOKNZobuxuvxntTgoUBygw6elYZxwfcWTKggnrczAzt5YzYT1dnIq8dKSw2n3gePi-jZ5hVwgRvWX8RoB5daO-ptLf5pu_mJegBbMwvg4BOJWqwU7K6QlsLO2UlYr25bqFBP_D2dvIG3qTwpmuUvXPqr65a5kdHtLXfJjAbRUKCMO3_7-MXUEN5E9rrHg7NSJxpqKyCIdvYoD34DdTUK52F2afSQRz3m0b8wz8rrRtJowV0RfEasOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd0c99669.mp4?token=rncfMPSX81CBos_Wxn7HXuObsirJ6UWecD0fj1Q-fUXF7zJzmGAesUCgZvbbBsM5fptS7bnCoR18AyOBz384tf8uHqSX7v6EOOKNZobuxuvxntTgoUBygw6elYZxwfcWTKggnrczAzt5YzYT1dnIq8dKSw2n3gePi-jZ5hVwgRvWX8RoB5daO-ptLf5pu_mJegBbMwvg4BOJWqwU7K6QlsLO2UlYr25bqFBP_D2dvIG3qTwpmuUvXPqr65a5kdHtLXfJjAbRUKCMO3_7-MXUEN5E9rrHg7NSJxpqKyCIdvYoD34DdTUK52F2afSQRz3m0b8wz8rrRtJowV0RfEasOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیر استارمر از سمت نخست وزیری استعفا داد
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/15582" target="_blank">📅 12:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15581">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرنگار الجزیره: یادداشت تفاهمی بین ایران و قطر در مورد اجرای آزادسازی دارایی‌های مسدود شده ایران امضا شد.
وزارت خزانه‌داری ایالات متحده (OFAC) معافیت‌هایی را برای نفت و پتروشیمی به مدت ۶۰ روز صادر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/15581" target="_blank">📅 12:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15580">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزیر اقتصاد جمهوری اسلامی : آزادسازی پول های بلوکه شده آغاز شده و بانک مرکزی اقدامات لازم رو برای دریافت پول فراهم کرده
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15580" target="_blank">📅 12:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15579">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">@withyashar
وضعیت</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/15579" target="_blank">📅 11:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15578">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA GH</strong></div>
<div class="tg-text">دارند مین‌های دریایی خنسا میکنم آمریکایی هاااا</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15578" target="_blank">📅 11:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15577">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS H A Y A N</strong></div>
<div class="tg-text">الان یکی دیگه اومد دوباره پسر
بزن بزنه فکر کنم</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15577" target="_blank">📅 11:46 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
