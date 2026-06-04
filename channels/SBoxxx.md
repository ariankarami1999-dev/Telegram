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
<img src="https://cdn4.telesco.pe/file/CaVIoWIDuELKdW8y3p5Mj_ho3lysgNgzUPhLkJP_6b_5wcQd3g1pp-FjI8lhC3LdSah7KOyDWxc3-BY-Wl1aPwO0wZ1DdIN4URwQXGcSeZTYvY-OuCiYCt8PlqQPTmSIg2Q-505bpt_NSpzfqWupIUT2j4zGAzCOGVikpnRCGeeGus1YEg7MvQJlIZ-XExGCLorHnYWl5nYX3T6rQbM7kJIIL3mh3uZ6iGukVttdYVNAeybLyy6bJgfSROY5MRqQ1IICiO6raQmt6eCZq3AhFkCHbuJUH9aAJ8HCHfrkVWoeKAfLqaMX5wNRffIB3vHvTtne3jzidOsqa_6-HLtRbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.95K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 05:13:01</div>
<hr>

<div class="tg-post" id="msg-16934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhkesMQ_1RaHjR-AmsKO_LgUUAhnTdoSO4XcfPCeKi4zPtRCYtQ2D9d-lEaaVV3InvN5Q4SGuVLozcslYPWZg0zFT6PEQXdiILtxTsuOZrr1m-DGwRBp6nS-gGO5t2yA1tFRxLlP7kPFkusjPG0RU4zATLKjodsPjr7i-8Zol-QVT_kA9mEZ8yOZX4xUBWhDOOx80QsSmjCMjWM99Yqavzra5-l7ZjtMPqj7aSrsheHrh7Q8IA8F3SEtbWPVHj7A0QTOLsLzlpzMkFD-3DsC9yo8vNa1FD3u6jZc0XU-YzSwSLHH0IPYuOPS7SkW28Gaup_ej2DDLQeYoO7keIdbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی ایران برای رساندن نفت به بازارهای جهانی به شدت کاهش یافته است.
پیش از این تحولات، ایران روزانه حدود ۲ میلیون بشکه نفت خام، میعانات و فرآورده‌های نفتی صادر می‌کرد. اما اکنون نشانه‌های روشنی از افت صادرات و تولید مشاهده می‌شود. بر اساس آمار اوپک، تولید نفت خام ایران در آوریل ۲۰۲۶ به حدود ۲.۸۵ میلیون بشکه در روز رسیده که نسبت به سطح پیش از بحران حدود ۳۵۰ هزار بشکه در روز کاهش نشان می‌دهد. برخی برآوردها حتی افتی نزدیک به ۴۰۰ هزار بشکه در روز را گزارش کرده‌اند.
در بخش صادرات، کاهش شدیدتر است. Kpler برآورد می‌کند که بارگیری نفت در پایانه‌های صادراتی ایران به حدود ۶۴۰ هزار بشکه در روز سقوط کرده است. نشریه تخصصی MEES نیز گزارش می‌دهد که این رقم از ۱.۶۴ میلیون بشکه در روز در ماه مارس به کمتر از ۵۰۰ هزار بشکه در روز در ماه مه کاهش یافته است. همچنین از ۶ مه به بعد برای مدتی هیچ محموله‌ای از پایانه اصلی صادرات نفت ایران در جزیره خارک ثبت نشد.
با این حال، صادرات نفت ایران هنوز به طور کامل متوقف نشده است. چین همچنان روزانه بیش از یک میلیون بشکه نفت ایران دریافت می‌کند، اما بخش عمده این نفت از ذخایر شناور انباشته‌شده در آب‌های آسیا تأمین می‌شود، نه از محموله‌های تازه صادرشده از ایران. این ذخایر نیز به سرعت در حال کاهش هستند. برآورد Kpler نشان می‌دهد که حجم ذخایر شناور ایران از آغاز بحران ۳۳ میلیون بشکه کاهش یافته و به حدود ۸۹ میلیون بشکه رسیده است.
در نتیجه، مسئله اصلی دیگر صرفاً کاهش صادرات روزانه نیست، بلکه سرعت تخلیه ذخایر شناور ایران است. اگر روند فعلی ادامه یابد، تحلیلگران Kpler هشدار می‌دهند که طی ۶۰ تا ۷۰ روز آینده بخش عمده نفت در دسترس برای تحویل به چین مصرف خواهد شد و ایران ممکن است ناچار شود تولید خود را تا حدود ۱.۷ میلیون بشکه در روز، نزدیک به سطح مصرف داخلی، کاهش دهد.
چنین سناریویی می‌تواند درآمدهای نفتی کشور را به پایین‌ترین سطوح سال‌های اخیر برساند و فشار اقتصادی قابل توجهی بر ایران وارد کند.</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SBoxxx/16934" target="_blank">📅 01:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:
در توافق پیش‌رو، به ایران اجازه دستیابی به سلاح هسته‌ای داده نخواهد شد و پس از امضای این توافق، تنگه هرمز به سرعت بازگشایی می‌شود.</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SBoxxx/16933" target="_blank">📅 00:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
دونالد ترامپ
:
در اون منطقه از دنیا ( خاورمیانه ) ،  آتش‌بس یعنی وقتی طرفین دارند با شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنند
﻿</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/16932" target="_blank">📅 00:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیروی دریایی ارتش، "مرکز فرماندهی و کنترل" شرارت های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
در پی شرارت ها علیه شناورهای تجاری ایرانی در دریای عمان و نقض مقررات تنگه هرمز از سوی ارتش متجاوز آمریکا، نیروی دریایی ارتش، مرکز "فرماندهی و کنترل " این شرارت…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16931" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبر کوتاه بود و دلخراش: محمدرضا شهبازی مورد تجاوز قرار گرفت
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16930" target="_blank">📅 22:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صدای انفجار در بحرین</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16929" target="_blank">📅 22:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16928">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به نظرم دسته خوبه را داده اند به سپاه که هر وقت میزند واقعاً بازارها به هم میریزند و دسته خرابه هم به ارتش داده اند برای وقتی که نفت را Short می کنند.
(باز بپرسید شورت چیست)</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/16928" target="_blank">📅 22:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نمیدانم این حمله های ما چطوری است که تا خبرش بیرون می آید نفت میریزد و طلا بالا می رود!
سبحان الله!</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/16927" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیروی دریایی ارتش، "مرکز فرماندهی و کنترل" شرارت های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
در پی شرارت ها علیه شناورهای تجاری ایرانی در دریای عمان و نقض مقررات تنگه هرمز از سوی ارتش متجاوز آمریکا، نیروی دریایی ارتش، مرکز "فرماندهی و کنترل " این شرارت…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/16926" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اطلاعیه نیروی دریایی ارتش: ساعاتی قبل مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا در یک ناوشکن آمریکایی در دریای عمان هدف قرار گرفت</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/16925" target="_blank">📅 22:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اطلاعیه نیروی دریایی ارتش:
ساعاتی قبل مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا در یک ناوشکن آمریکایی در دریای عمان هدف قرار گرفت</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16924" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16923">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقچی:   آنچه در ۲ روز گذشته حمله به بیروت را متوقف کرد، در درجه اول قدرت مقاومت لبنان و توان نیروهای مسلح ایران بود  وقتی کار به جایی رسید که نیروهای رژیم صهیونیستی می‌خواستند به ضاحیه جنوبی بیروت حمله کنند، موضع قاطعی گرفتیم و نیروهای مسلح ما آماده پاسخ…</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/16923" target="_blank">📅 22:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16922">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عراقچی: من مطمئنم که مسئله سفیر ما در بیروت حل خواهد شد، ما به حکمت دوستان و مسئولان دولت لبنان اعتماد داریم</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/16922" target="_blank">📅 22:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16921">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزیر خارجه ایران: تماس‌های ما با آمریکا قطع نشده است، اما در مذاکرات پیشرفتی حاصل نشده است - المیادین.</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/16921" target="_blank">📅 22:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزیر خارجه ایران: تماس‌های ما با آمریکا قطع نشده است، اما در مذاکرات پیشرفتی حاصل نشده است - المیادین.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/16920" target="_blank">📅 22:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16919">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL-CKbfo2n1EyZv9PR6ZhYYi-PlnpiaT8kQifCsHmRNVXkXDwtV0wy_6Wldhw2iypLR57YAitoLa2LRrAlHweMvNFFFibKkMVE65Iwp_uYyOUqRn8iVUUMIRTkUjglGTjF-OflctVgtHTL6lHJJj9MGwSjjw8nxjVSeBof_tAkoDFITDRSHgUOrYo43724qHTTFnpwK5h3nTlNkBJSRWHcRVjHu0oK6kP6fxKy8H6tPhMtJ1GsTx54sWR_iuTRIl2pxgqOtojjO11kbLQALWacGSbesMYcKbmcuktJkWizAdYM9Y0hKelY4aB2EIBxVOviMx5N68R1kEp5BW8XT34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم تخریب پایگاه «علی السالم» آمریکایی ها در کویت
تصویر سمت راست مربوط به آشیانه ها و تصویر سمت چپ مربوط به انبارهای سوخت</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/16919" target="_blank">📅 19:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16918">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">روبیو:
به عنوان بخشی از سیاست خارجی ما و به دلایل متعدد، ما به صورت علنی درباره اینکه آیا اسرائیل سلاح‌های هسته‌ای در اختیار دارد یا خیر، بحث نمی‌کنیم.
ما پاسخ بهتری به کنگره درباره اینکه آیا اسرائیل سلاح‌های هسته‌ای در اختیار دارد یا خیر، ارائه خواهیم داد، مشروط بر اینکه آن‌ها درخواست پاسخ به صورت محرمانه را مطرح کنند.</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/16918" target="_blank">📅 18:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16917">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شرایط جوری شده که اسرائیل عرب های لبنان را می زند و ما هم در پاسخ عرب های کویت را می زنیم که در حین آن هندی ها کشته می شوند</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16917" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16916">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2b300c77.mp4?token=hzqqiKFvMQTT-5hwX1AXqZWlAK2vzGkcFYOBCoYLj-nGQShCs-Xr6xNDThiG8PQ1tYCxEuHiAqRHPfg4Ic9nnsaYBsXA8_DJg6pCShvqDfsBuS17Jmb-q2vegJTLk9bDDxuHVrygMA0R8yekWf2Vxmw04XkcL5muQ8UX0kb2rlnwQHnDJWKA9OHfDX9-137KenOJn2Vta8XHzSMKJCpM9dJ7aZxwedRSGK1uBk7lnOLFdK3z9N3B7HCSip4lBhe7cznHGAzDqyCbeUq0_vCNljMFqTwdjmRpJ5VE3zsyKLiQieMtiMs8JiecvgLT1_HJQQIP_yCQ7xWIWEk-LprhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2b300c77.mp4?token=hzqqiKFvMQTT-5hwX1AXqZWlAK2vzGkcFYOBCoYLj-nGQShCs-Xr6xNDThiG8PQ1tYCxEuHiAqRHPfg4Ic9nnsaYBsXA8_DJg6pCShvqDfsBuS17Jmb-q2vegJTLk9bDDxuHVrygMA0R8yekWf2Vxmw04XkcL5muQ8UX0kb2rlnwQHnDJWKA9OHfDX9-137KenOJn2Vta8XHzSMKJCpM9dJ7aZxwedRSGK1uBk7lnOLFdK3z9N3B7HCSip4lBhe7cznHGAzDqyCbeUq0_vCNljMFqTwdjmRpJ5VE3zsyKLiQieMtiMs8JiecvgLT1_HJQQIP_yCQ7xWIWEk-LprhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رومن گافمن: از زخمی ۷ اکتبر تا رئیس موساد  سرلشکر رومن گافمن، مدیر تازه منصوب شده موساد اسرائیل (که در ژوئن ۲۰۲۶ سوگند یاد کرد)، به عنوان یکی از ارشدترین افسرانی ظاهر شد که به طور فعال با نیرو‌های حماس در حملات ۷ اکتبر ۲۰۲۳ درگیر شد.   گافمن که در آن زمان…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/16916" target="_blank">📅 17:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16915">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رییس جدید موساد!  رومن گوفمن، سرلشکر متولد بلاروس و از نزدیک‌ترین چهره‌های مورد اعتماد بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از ۲ ژوئن ۲۰۲۶ ریاست موساد را بر عهده گرفته است.   گوفمن که پیش از این به‌عنوان منشی نظامی نتانیاهو فعالیت می‌کرد، اکنون در رأس مهم‌ترین…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/16915" target="_blank">📅 17:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16914">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بلومبرگ :
مقامات غربی می‌گویند خطر تداوم  مخفیانه ساخت سلاح‌های هسته‌ای توسط ایران اکنون بالاتر از آن چیزی است که قبل از حملات نظامی ایالات متحده و اسرائیل در ژوئن ۲۰۲۵ بود.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/16914" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16913">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شاید باورتان نشود ولی حمله دیشب ما به کویت یک کشته داشته که آن هم ….   …یک کارگر هندی بوده!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/16913" target="_blank">📅 16:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شاید ما برخی کشتی ها را با پهپاد زده باشیم، برخی ها را با موشک بالستیک، برخی ها را هم با موشک کروز.  خب اینها می‌شود تفاوت‌های حملات ما.  اما یک شباهت بزرگ هم میان همه حملات ما وجود دارد و آن اینکه کشتی مورد تهاجم مال هر کشوری که باشد، دستکم ۲ ملوان هندی در…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/16912" target="_blank">📅 16:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رئیس‌جمهور لبنان حملات ایران به کویت و بحرین را محکوم کرد</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/16911" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رئیس‌جمهور لبنان حملات ایران به کویت و بحرین را محکوم کرد</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/16910" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKF2jqFZ6y4dP9s9FVqCup1LydbJPuECQ42l7DFwxPaec6nsrrMshKcOhhKsEahROoa2dpO_FDG1Swmm-luCm6nnv1Bu01HG79NDcx_FTPFC7PLhUWbxXKsb9WKmmli0wfd9eyvesTTsBmr1Qvydcv8Fv0ULxG_Tan2sioi-hGtnxcXBCpV7-_4F7fBczmrQnrJ_ER0xF1-dInv_VU_yrKgb4njUdVKP7vCbQKb2frsi3EAj_Wz1G6-IrBuh6ZaZZ1XVMx7JD5OfHjFRYrCVzgXzcSg22Lm1QdEpFPMLtArkUgGpTMejmH4fdwKKoFNvGruxBil5Yei-a4uNZ5v1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه «مختار-007» ولی گفت که به شرط آتش بس در لبنان حاضر است سلاح های خود را تحویل دهد.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/16909" target="_blank">📅 15:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/16908" target="_blank">📅 14:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایران ۶ موشک بالستیک به پایگاه آمریکایی در کویت شلیک کرد  سپاه پاسداران انقلاب اسلامی حداقل ۶ موشک به پایگاه هوایی علی السالم، محل استقرار نیروهای آمریکایی، شلیک کرد. تصاویر، صداهای انفجار و تلاش‌های رهگیری بر فراز کویت را نشان می‌دهد.  رسانه‌های ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/16907" target="_blank">📅 14:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">در این پست و پستهای ریپلای شده اش گفته شد که هدف اصلی ترامپ «تحقیر» شدید جمهوری اسلامی است و این مسخره بازی امروزش هم که میخواهم رهبر ایران را ببینم و اینها هم در همان راستا است.  عجیب است که ولی عده ای مونگول کماکان تصور می‌کنند هدف ترامپ سرنگونی نیست و مثلا…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/16906" target="_blank">📅 14:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OIwF6S4pTjA6HlpenJZy1HOHSxmpYAQ3iObUSkhibe50zrgDJZdvxpmjl3D9z1QkR-6gEuzTW7HhxMdpFAHVdaDsOcyEQHtbPUGUIvPrLpOadtbIaWeT-tknC84uSsEZtNjvr-kx4JbBNJ5VpVHoKCDtgyRT1dlS7aHI_tf0dxDnkE80MMRJGYaBALBSkFosRX3WmoHIeXGIAA5KILdotR_qR7RTyNTez69gZF_-YzRMt_eoMNd-E2KCahpGYUS8nxyKtecbK-DDMstoBGTfMFmJCYzJ1o95dJza_t7GNWq9ijs0gynqYxyPa6MaxEGa-ff7D5BjW0qfSauloFj_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر کوتاه بود و دلخراش:
محمدرضا شهبازی
مورد تجاوز قرار گرفت
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/16905" target="_blank">📅 14:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اینجا گفته بودم که هدف ترامپ تنها شکست ‌‌و تسلیم ایران نیست بلکه تحقیر جمهوری اسلامی نیز هست  به عنوان حکومتی که ۴۷ سال نمادهای قدرت و غرور آمریکایی را هدف قرار داده، جمهوری اسلامی از دید ترامپ بایستی پیش از شکست، شدیدا تحقیر بشود.  — تسخیر سفارت آمریکا و…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/16904" target="_blank">📅 14:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ:
رهبر جمهوری اسلامی با مذاکرات موافقت کرده است.
اوضاع با ایران به سرعت در حال پیشرفت است و بسیار خوب خواهد شد.
ممکن است در مقطعی با او دیدار کنم.
ممکن است محاصره ایران تا روز کارگر برداشته شود</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/16903" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16902">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-VZSMKFWaVTfQ6N88lHnWJw54YnFKm0GD6Vw_ifM77xasuwp2nSFa-M6mwNCJHGpZDhNb2bqqOKVhCcFTrBOCsH9Buc6QpjZItz3-dIisIqOOEkN55Pk_Z-rWWmefvO0ujqzccKGOvGeiuwOvA2EygFhFZ4WswceuiY-SXoJBldeuq37rQGKtBj1XNyzRuwb6T0gznD7tAMd8ggd7AJW7sS9Eu22IRActcMgZ3kxdKb97HVOSpiS0rdTLNbUaazvjRm4rIMM5qeZ_Ib1MMEzlMFRSzEfGJk3yTCBoDCBa4S1BYZrXBlTjX3lW-m2yr5TQ24pa3f7SD1jPZQoidCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تخریب ۱۱۰۰ مترمربع از آیینه کاری و گچ کاری کاخ گلستان در طی جنگ ۴۰ روزه</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/16902" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16901">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اصحاب کهف با خلع سلاح گروه‌های مقاومت مخالفت کرد  گروه «اصحاب کهف» که از گروه‌های مقاومت عراقی وابسته به «مقاومت اسلامی» است، روز سه‌شنبه ۲ ژوئن با درخواست‌های سیاسی برای تحویل سلاح گروه‌های مسلح مخالفت کرد و تأکید نمود که استناد به حمایت مرجعیت از این روند،…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/16901" target="_blank">📅 12:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16900">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇨🇳
پروژه نظارتی چین با هوش مصنوعی: شناسایی منتقدان دولت پیش از اقدام سیاسی
🔸
شرکت چینی Geedge Networks که در زمینه ساختن نرم‌افزارهای امنیتی فعالیت دارد، اکنون تمرکز خود را روی تحلیل رفتار شهروندان گذاشته است
🔺
طبق اسناد فاش‌شده‌، این شرکت درحال استفاده از مدل‌های هوش مصنوعی برای تحلیل داده‌های موقعیت مکانی، الگوهای استفاده از اینترنت، تماس‌های تلفنی و حتی تاریخچه تماشای فیلم و مطالعه کتاب شهروندان است
🔸
هدف نهایی این پردازش‌ها، ساخت پروفایل‌های رفتاری دقیق برای شناسایی «نیت» افراد است تا سیستم بتواند کسانی را که ممکن است در آینده به منتقدان دولت تبدیل شوند، شناسایی کند. براساس صورت‌جلسه یکی از نشست‌های این شرکت، تمرکز محققان روی «کشف اطلاعات مضر» است؛ حزب کمونیست چین معمولاً از این عبارت برای توصیف نارضایتی‌های سیاسی یا محتوای مخالف دولت استفاده می‌کند</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/16900" target="_blank">📅 12:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قطعی برق خانه‌ها از اواخر حرداد شروع خواهد شد
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی، صنایع، معادن و کشاورزی ایران: پیش‌بینی می‌شود که این روند از اواخر خرداد یا اوایل تیرماه آغاز شود و مردم ایران احتمالاً به مدت سه ماه با این شرایط درگیر خواهند بود که در این مدت همراهی و همدلی همگانی ضروری است.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/16899" target="_blank">📅 12:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آمریکا چهار صرافی ایرانی (نوبیتکس، بیت‌پین، رمزینکس و والکس) را تحریم کرد.
مراقب باشید که در این شرایط، ولت هایی هم که با این صرافی ها در تعامل بوده اند ممکن است بلاک شده و موجودی شان فریز بشود.
در این وضعیت، دپو کردن دلارها به صورت اسکناس و|یا در بروکرهای معتمد منطقی تر است. (یا خرید سکه|شمش و نگهداری اش به صورت فیزیکی)</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/16898" target="_blank">📅 11:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKJqskvPWZLXHbFElZSLS8P6MrioC87lEqdUWE69yX3B3zkztsW0KsBQXgu0-fHStfeo2Q5NuTMKp4e5CWVcl-SjksMQyH7W71bKkPkbKfZkEgjggPLTeSPI3Q2hS6DhroRayrM_0R5sCKvdb3DUykklIWUrsqv6mhOH-4-vDtEspjw4YF-7-JO444YfTTmi2ODM5xL9bYIBvZ0z1Shc-fhLOjaTvBTNwTtGJM4ZmSCvnZWJhn8y_NjAN4SC9N4QGlD2jtbVcsOIOnPtnNeD4Y7DrFcD64USfUT5ZuXEdPwDq4ksa0O9N9lGGVFd3FqrpdCiv0GlTNsdfmM9Yze-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه به قول آقای رسایی، روبیکا حتی خودش اینستا هم داشت  (منظور مبارک امکان گذاشتن استوری بوده)</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/16897" target="_blank">📅 07:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLFip1apv1rRBCug8Pq8E7ISZmGoozkpef1DNekESMEIkWlGOHjtZa_dGqOh3J-q7P7WZR5-9isRhV6Qd7XxgeNQnEamjQObFTHcl7zkiFhsio5sLq6iMzQky6yCNgfQ8kb8SOFfbWkfxcu-RD2YWEdmpNP6-UwsO8JavtYo_Oy_NnuiQxm0lctSYn3NVeQMcsEt7Zslw-3pFq_Eju5wcy1FhQZugcXBw2xGLDHXdR3TXWoPGg_WYM81XdMwXKxm3TxTsErkJxJG9pgvdPAEhrTrncXFKoLW-Fi2MNZ_hjPzZjPv0cFx89LpOZ4w3L_asNhAc2yTwwhHJSbN6Iuqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد ایرانی فاش کرده است که تهران فناوری پیشرفته چینی را برای قطع دائمی دسترسی به اینترنت جهانی وارد کرده است.
این افشاگری در بحبوحه خاموشی بی‌سابقه اینترنت در ایران صورت گرفت، جایی که مقامات پس از شروع جنگ با ایالات متحده و اسرائیل در ۲۸ فوریه، اینترنت را قطع کردند.
محمد سرافراز، عضو شورای عالی فضای مجازی ایران و رئیس سابق صدا و سیمای جمهوری اسلامی ایران، در ۲۳ مه به روزنامه آنلاین فراز گفت که سخت‌افزار چینی از قبل در کشور وجود دارد.
به گفته وی، هدف از این فناوری، زمینه‌سازی برای محدود کردن دائمی اینترنت در حالی است که فقط دسترسی تحت نظارت شدید برای کاربران منتخب در کشوری با حدود ۹۰ میلیون نفر جمعیت فراهم می‌شود.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16896" target="_blank">📅 07:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اطلاعیه سپاه درباره وقایع شب گذشته  و بامداد امروز   روابط عمومی سپاه پاسداران انقلاب اسلامی:  بسم الله القاصم الجبارین  فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ  در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/16895" target="_blank">📅 07:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اطلاعیه سپاه درباره وقایع شب گذشته  و بامداد امروز   روابط عمومی سپاه پاسداران انقلاب اسلامی:  بسم الله القاصم الجبارین  فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ  در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/16894" target="_blank">📅 06:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16893">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ایران ۶ موشک بالستیک به پایگاه آمریکایی در کویت شلیک کرد  سپاه پاسداران انقلاب اسلامی حداقل ۶ موشک به پایگاه هوایی علی السالم، محل استقرار نیروهای آمریکایی، شلیک کرد. تصاویر، صداهای انفجار و تلاش‌های رهگیری بر فراز کویت را نشان می‌دهد.  رسانه‌های ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16893" target="_blank">📅 06:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16892">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حمله موشکی سپاه به کویت!</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/16892" target="_blank">📅 06:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16891">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رییس جدید موساد!  رومن گوفمن، سرلشکر متولد بلاروس و از نزدیک‌ترین چهره‌های مورد اعتماد بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از ۲ ژوئن ۲۰۲۶ ریاست موساد را بر عهده گرفته است.   گوفمن که پیش از این به‌عنوان منشی نظامی نتانیاهو فعالیت می‌کرد، اکنون در رأس مهم‌ترین…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/16891" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16890">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-LL7xQSoO8r1J_Fo-tP_OvaF_OKKjh1Fx0d7rTCYtY9aEh9eWMUZJwB4DoKVufRVkXtBnQiHJ0Mcntg4INgMo5MWVKRSnqyr7nNBLqnIshXII957LTB9edw5LWV7hE6-jKm_BTFAEQa9aROI521_Y3X0n_luRswj8Y89cEbog0Df1RgZVmB3Raf0bFrqMnBC4zKneLdM-lH6zELlRV1WyvOWkCdMAlfKFcFDUHHdwHyrA-GjrT1iBVbWpDbnkHbCsxosXgT688h_Imo3L319RVOWTAzWWtPsWLuHpZUmHYkoeYRmnoGeRkZpNwlLhwoETcuqbdf_uF5YOZOkiOUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا رفت برای این سناریو که عصر گفتیم…؟!</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/16890" target="_blank">📅 01:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16889">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حمله موشکی آمریکا به ابرنفتکش ایرانی!</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/16889" target="_blank">📅 01:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16888">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIY7cSYm88aoy055yoaVnKTZUwHAqxAOodHEwohm-5HvSfWVdTttJId9OiQ8stMaplqhOYEUy1dYwwOZ17xFnLe1t9koYXR28FPPMEnRzkcyKMgNFB-kAb27_UvTg4QM9bCqrKYx3NLwi9TdjLXbt8udtXpZbAskHtRTtycffRm8a39RCiQiqMZnjAeU9L38t_zS9zonIO4uTQQryqP0M_iLqfByy8eUFeuhDjRKzoYitvT4JYYtFv3DJomSSMztD_ytTgNSjN7W6fKY_8_XvweiHJsBghu1RYq1M0mDKVUz4xwqgE4BHdzmasPHySIXLYvK_HYAjVCnvh3y_c2b1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس جدید موساد!
رومن گوفمن، سرلشکر متولد بلاروس و از نزدیک‌ترین چهره‌های مورد اعتماد بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از ۲ ژوئن ۲۰۲۶ ریاست موساد را بر عهده گرفته است.
گوفمن که پیش از این به‌عنوان منشی نظامی نتانیاهو فعالیت می‌کرد، اکنون در رأس مهم‌ترین سازمان اطلاعاتی اسرائیل قرار گرفته؛ انتصابی که از سوی حامیان دولت با استقبال مواجه شده، اما هم‌زمان نگرانی‌هایی را در میان برخی کارشناسان و ناظران امنیتی برانگیخته است.
منتقدان این انتصاب معتقدند که پیشینه حرفه‌ای گوفمن عمدتاً در یگان‌های زرهی و مسئولیت‌های ستادی ارتش متمرکز بوده و او برخلاف بسیاری از رؤسای پیشین موساد، سابقه قابل توجهی در حوزه عملیات مخفی، اطلاعات انسانی یا مأموریت‌های برون‌مرزی نداشته است. از این منظر، برخی تحلیلگران انتصاب وی را بیش از آنکه ناشی از تجربه تخصصی اطلاعاتی بدانند، نتیجه نزدیکی سیاسی و شخصی او به نتانیاهو ارزیابی می‌کنند.
گوفمن در جریان مباحثات داخلی پیرامون جنگ غزه و ساختار حکمرانی این منطقه پس از پایان درگیری‌ها، به‌طور مستمر از مواضع سخت‌گیرانه و قاطع نخست‌وزیر حمایت کرده است. این همراهی موجب شد که او به یکی از اعضای اصلی حلقه تصمیم‌گیری نزدیک به نتانیاهو تبدیل شود و نفوذ قابل توجهی در روند تدوین سیاست‌های امنیتی پیدا کند.
از جمله موضوعاتی که نام گوفمن را در کانون توجه قرار داد، تدوین یک سند داخلی درباره آینده غزه بود که در آن از برقراری حکومت نظامی مستقیم اسرائیل بر این منطقه حمایت شده بود. این پیشنهاد با انتقادهایی در داخل نهادهای امنیتی اسرائیل مواجه شد و برخی محافل بین‌المللی نیز آن را گامی در جهت اشغال بلندمدت غزه تلقی کردند. بنا بر گزارش‌ها، حتی شماری از مقامات ارشد اسرائیلی این طرح را  «از نظر راهبردی خطرناک» و «بیش از حد سیاسی» توصیف کرده‌اند.
گوفمن همچنین در جریان عملیات نظامی اسرائیل در غزه طی سال‌های ۲۰۲۳ و ۲۰۲۴، به‌عنوان نزدیک‌ترین مشاور نظامی نتانیاهو در تمامی تصمیمات راهبردی مهم حضور داشت. منتقدان بر این باورند که این جایگاه، او را با جنجالی‌ترین و بحث‌برانگیزترین مراحل جنگ پیوند می‌دهد. برخی منابع آگاه نیز وی را شخصیتی توصیف می‌کنند که بیش از ارائه ارزیابی‌های مستقل راهبردی، تمایل دارد دیدگاه‌ها و ترجیحات نخست‌وزیر را تأیید و تقویت کند.
در نتیجه، برخی ناظران معتقدند که اهمیت انتصاب گوفمن نه در ایجاد تحول ساختاری در موساد، بلکه در تغییر جهت‌گیری و فضای حاکم بر این سازمان نهفته است. از نگاه آنان، حضور یک چهره کاملاً وفادار به نخست‌وزیر در رأس دستگاه اطلاعاتی اسرائیل می‌تواند به کاهش موانع و فیلترهای داخلی، افزایش نفوذ ملاحظات سیاسی در تصمیم‌گیری‌های اطلاعاتی و همسوتر شدن عملیات پنهان با اهداف و اولویت‌های سیاسی دولت منجر شود. بر اساس این ارزیابی، مأموریت اصلی گوفمن نه اصلاح موساد، بلکه هماهنگ‌سازی هرچه بیشتر فعالیت‌های اطلاعاتی و مخفی اسرائیل با راهبردها و جاه‌طلبی‌های سیاسی دولت نتانیاهو خواهد بود.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16888" target="_blank">📅 01:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16887">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCDJ1731YVCix1IuCIrdm-pt6ZF5e2h98ko0XYG27hg26IRjNQPtwzqLhijv1DBk7ZmxJDyeeaKFlorohHT1tRDtRXj710yXgI---h8osUVqJV0jjYNjEc2MrSd9V9vjbO-AJ6leyBhM6now8oBa3s2ozz1eBchZG9mC6i9Q_5fusR9MonQlPpxsOmlpaN4FrZWE_UkXICStxHxRQugUB8En2BEhjAcLOjrwwD8PLxCyoEIIYFNeZqFZc8Tk5YkrwPu6wAeQOk16qU1FY8QWOU9_BfNcr-AaDpDHwY87_WZwabuuUhwJ5d-Rr5GTvKzgzWge20FxEe-tK_cWc24Y7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلمش را هم به این سرعت بیرون دادند حرامزاده ها!  اینها ثروت ملت ایران است که دود می شود.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/16887" target="_blank">📅 00:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16886">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/864d5386d4.mp4?token=HcqCcBAS1jPLjCJuKDcooy9S4_UGSkC9l9FpbzxcPyvE0K7bq8R2zs5TER0_IGAhpbxUtsSkS26OiBZ-zjvTW4LktE7HqKyTt8gJzGq9-m6oQrGZbNYFQddYOvP67w0E1Y6sc9PndcbZbXSzJuCzQ79BEBocXHtNFcAULTym7s412ztf8nLgPTUnNF4n7g9crXSkEC3zBbg5KDSYuBgaiIoAS4JDKin3b42NzAWN0cjW-wwYvqduAbJKk5b3ppyDT31uAuX0pA_z8lSi-pPxkPVGw0zQR1zhKL-79ol2JJ5yysMgeVpY8S1x_R1fAz8K136iNYdRYmRBCiXtbX4_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/864d5386d4.mp4?token=HcqCcBAS1jPLjCJuKDcooy9S4_UGSkC9l9FpbzxcPyvE0K7bq8R2zs5TER0_IGAhpbxUtsSkS26OiBZ-zjvTW4LktE7HqKyTt8gJzGq9-m6oQrGZbNYFQddYOvP67w0E1Y6sc9PndcbZbXSzJuCzQ79BEBocXHtNFcAULTym7s412ztf8nLgPTUnNF4n7g9crXSkEC3zBbg5KDSYuBgaiIoAS4JDKin3b42NzAWN0cjW-wwYvqduAbJKk5b3ppyDT31uAuX0pA_z8lSi-pPxkPVGw0zQR1zhKL-79ol2JJ5yysMgeVpY8S1x_R1fAz8K136iNYdRYmRBCiXtbX4_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/16886" target="_blank">📅 00:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16885">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkwFcAP2t_-Dt_mzrgD45fHEvd6qxiiigyCn9rF-Y99XbtduJJgxGCD1U2vesGlHPOkFS-RkM2CFZdQZzhmNOlb6Oq199IK6aaLATcvijV3OLmUNe-yvSLc-ckaXSS03vLx7ryTiLpge9tiFSlS_sAsUWVwrmGuPkF8NwbMExur4Z9jxYAEo17HPOBYRkJ8pST0enuKa9yGyN0vS8ugvYzM1j-4gLZkNp8RI9zHBfY7ANy_3DdtYfh-7JdahO99JdvkFjP-KvTTYL5k3VgQ1vvVQjmFrAEkMWW_on5FjjO3dCXu9hSBLfil-Hsod1IKkm5jLmFv-Gdr7U9-fnwBFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/16885" target="_blank">📅 00:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16884">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حمله موشکی آمریکا به ابرنفتکش ایرانی!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16884" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16883">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حمله موشکی آمریکا به ابرنفتکش ایرانی!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/16883" target="_blank">📅 00:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16882">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گروه «مریم مقدس» هم با خلع سلاح مخالفت کرد.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16882" target="_blank">📅 00:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16881">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گروه «مریم مقدس» هم با خلع سلاح مخالفت کرد.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16881" target="_blank">📅 00:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16880">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اصحاب کهف با خلع سلاح گروه‌های مقاومت مخالفت کرد  گروه «اصحاب کهف» که از گروه‌های مقاومت عراقی وابسته به «مقاومت اسلامی» است، روز سه‌شنبه ۲ ژوئن با درخواست‌های سیاسی برای تحویل سلاح گروه‌های مسلح مخالفت کرد و تأکید نمود که استناد به حمایت مرجعیت از این روند،…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16880" target="_blank">📅 00:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16879">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">همینطور کتائب امام علی.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/16879" target="_blank">📅 22:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16878">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16878" target="_blank">📅 22:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16877">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خب گویا اینها هم لازم شده یک گوشمالی اساسی بشوند...  بعد از پیروزی شان در سیندور یکم، خیلی سیس عقاب برداشته بودند و این نمایشهایشان سازندگان سلاح های غربی مورد استفاده هند (خصوصاً جنگنده رافائل) را آزار داده و بیش از حد سلاح سازان چینی را نوازش می داد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/16877" target="_blank">📅 22:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16876">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♨️
سقوط چشمگیر کاربران پیامرسانهای داخلی در طی هفته اخیر با بازگشایی نسبی دسترسی به اینترنت بین المللی
🩵
منبع : مجله فناوری گجت نیوز</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16876" target="_blank">📅 20:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16875">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♨️
سقوط چشمگیر کاربران پیامرسانهای داخلی در طی هفته اخیر با بازگشایی نسبی دسترسی به اینترنت بین المللی
🩵
منبع : مجله فناوری گجت نیوز</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/16875" target="_blank">📅 20:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16874">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فناوری_هوشمند،_جنگ_را_به_انتخابی_احمقانه‌تر_تبدیل_می‌کند.pdf</div>
  <div class="tg-doc-extra">476.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/16874" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">توهم خطرناک جنگ مدرن.pdf</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16874" target="_blank">📅 19:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16873">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حشد الشعبی نیز به پایان خود نزدیک می شود...  بعد از گروه صدر (سرایا سلام)، امروز گروه عصائب اهل حق نیز اعلام انحلال کرد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/16873" target="_blank">📅 19:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16872">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/16872" target="_blank">📅 19:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16871">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزیر امور خارجه آمریکا، روبیو: ایران فقط به خاطر بازگشایی تنگه هرمز از تحریم‌ها معاف نخواهد شد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16871" target="_blank">📅 18:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇰🇵
رهبر کره شمالی برای خودکشی ( درصورت زنده ماندن فرد ) مجازات اعدام را قرار داد</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/16870" target="_blank">📅 17:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16869">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc85d6917.mp4?token=Q1-9YNljnHf21ndtSH88HYsELaaBopEqE93qZAVzLR3ni6TndFj1E1SDqAfdVTHLnL6_3AdeYm1SA59sI1T0ny3YdUvmLD2x74YOlYVSp0p5xua-01Cqx2SAcHwGiwbQpPdcV5qq1-QpLRCaC0LNE11NBzHiUUt8xSSzxXPf2yUQ4QH1jDpb-FnC2kZsdx0oLzhIgjGHILVxReutyt1Y3YOJwitT41fRGiUqGfoXYhw1OiPrAAS0tT74ufqUjFicL5-ZYI0uVAeiMvTUcSCxpigmntWyhbcWhS1zXFf0aY45_p9NjQ_mhPEWMU448cCZ065K2GxrJDRlNHjOWc7SMoMV0bJZLrOFGvC5M4YJb9qkSUtsB6leEFHjjeneTgR5AYOZI-AUYyLVtfTeZEJJfN2lj6SaY2o051CogRf3nVQbPAwldbNzEBjJe0kHbACn-cqYXTEYHLwfBTtuAfXZd4yYYj1ifmKA7Cb_pypxxp2PFRpnwqFNcvOV6rtSTnU5hUOYPcO_tnQ457djg5RZKduMdZrBBFMfARsBplB-gFjx3SOW5KAjOxjn4ER799y8_TYUJ5Wf9H_h-VgvI7w0HJ1mBY_zfqvYnusPYvFeHtMuExoNRHP-yI_ossWILuQaQBtUTZZdkjBYLCWSLDWDI2JwwBXSOdWlPFo0fIl0JNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc85d6917.mp4?token=Q1-9YNljnHf21ndtSH88HYsELaaBopEqE93qZAVzLR3ni6TndFj1E1SDqAfdVTHLnL6_3AdeYm1SA59sI1T0ny3YdUvmLD2x74YOlYVSp0p5xua-01Cqx2SAcHwGiwbQpPdcV5qq1-QpLRCaC0LNE11NBzHiUUt8xSSzxXPf2yUQ4QH1jDpb-FnC2kZsdx0oLzhIgjGHILVxReutyt1Y3YOJwitT41fRGiUqGfoXYhw1OiPrAAS0tT74ufqUjFicL5-ZYI0uVAeiMvTUcSCxpigmntWyhbcWhS1zXFf0aY45_p9NjQ_mhPEWMU448cCZ065K2GxrJDRlNHjOWc7SMoMV0bJZLrOFGvC5M4YJb9qkSUtsB6leEFHjjeneTgR5AYOZI-AUYyLVtfTeZEJJfN2lj6SaY2o051CogRf3nVQbPAwldbNzEBjJe0kHbACn-cqYXTEYHLwfBTtuAfXZd4yYYj1ifmKA7Cb_pypxxp2PFRpnwqFNcvOV6rtSTnU5hUOYPcO_tnQ457djg5RZKduMdZrBBFMfARsBplB-gFjx3SOW5KAjOxjn4ER799y8_TYUJ5Wf9H_h-VgvI7w0HJ1mBY_zfqvYnusPYvFeHtMuExoNRHP-yI_ossWILuQaQBtUTZZdkjBYLCWSLDWDI2JwwBXSOdWlPFo0fIl0JNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۵ درصد از کل گاز تولیدی کشور در حملات آمریکا و اسرائیل از بین رفت
در صدا و سیما می‌گویند بعضی حقایق را نگویید
سردبیر خط انرژی
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16869" target="_blank">📅 15:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16868">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کرملین:  اگر زلنسکی دستور عقب‌نشینی نیروهای اوکراینی از مناطق روسیه را بدهد,جنگ «تا پایان روز» به پایان می‌رسد</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16868" target="_blank">📅 14:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16867">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کرملین:
اگر زلنسکی دستور عقب‌نشینی نیروهای اوکراینی از مناطق روسیه را بدهد,جنگ «تا پایان روز» به پایان می‌رسد</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16867" target="_blank">📅 14:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16866">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Faprl8yeV36ecObK9J5qC5cywnVxnvOD5RkM7KzORYToTlDFMrZgNiyN_WonWEy2v5ot_t9NOOsTq-8K32-yyijth4Q-FTftodGFRrFWK6c_2q0B96aRshJaX_t4MsOJqOrT9pQpjAHJKA8lgMtgxVJvFNnIICF1MjLUSrvQR7m-z_kjk5O0PpZCLqy69cCi6XaH9dt7uP3_2hlg7Cw29bYwqdrIuXjXjYPcB9l4BYGUxpmstMd72kT-MdiWQK2kR60eTjL68t0SMJnnrVcHQIENNeD6RFPKkCTyENHzAj5m_8oDTffG7zUHxrKUDuZL6rWqakyknNWfZNobvosWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16866" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16865">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بر اساس ارزیابی مؤسسه CTP-ISW، تعلیق مذاکرات ایران و آمریکا در ۱ ژوئن را می‌توان نشانه‌ای از ترجیح بخشی از حاکمیت ایران به تداوم وضعیت فعلی دانست؛ وضعیتی که نه به توافقی محدودکننده منجر شده و نه به رویارویی مستقیم و گسترده با آمریکا. اعلام این تصمیم از سوی…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/16865" target="_blank">📅 13:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16864">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خلاصه دیدگاه موسسه مطالعات جنگ درباره اهمیت راهبردی کنترل تنگه هرمز در دکترین جدید بازدارندگی جمهوری اسلامی:  مقامات ارشد ایرانی در ماه‌های اخیر بار دیگر بر اهمیت راهبردی تنگه هرمز به‌عنوان یکی از اصلی‌ترین ابزارهای قدرت و بازدارندگی جمهوری اسلامی تأکید کرده‌اند.…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/16864" target="_blank">📅 13:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16863">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فرستاده آمریکا باراک:   این بخش از جهان تنها زور را میپذیرد</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16863" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16862">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این تصویر را ترامپ دیروز پست کرده بود.  کلمه discombobulator را پیشتر ترامپ در توصیف سلاح مخفی سری که آمریکا در جریان ربودن مادورو استفاده کرد به کار برده بود و دیروز دوباره گویا به این سلاح اشاره کرده است.  گویا این سلاح به نوعی در مختل کردن کلیه دستگاه های…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16862" target="_blank">📅 11:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16861">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آکسیوس: مشاجره شدید ترامپ و نتانیاهو بر سر تشدید تنش‌ها در لبنان  اکسیوس گزارش داد که دونالد ترامپ در تماس تلفنی با بنیامین نتانیاهو به‌شدت از تشدید عملیات اسرائیل در لبنان انتقاد کرده است.  بر اساس این گزارش، ترامپ با لحنی تند به نتانیاهو گفته است:
▪️
«تو…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16861" target="_blank">📅 07:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16860">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آکسیوس: مشاجره شدید ترامپ و نتانیاهو بر سر تشدید تنش‌ها در لبنان
اکسیوس گزارش داد که
دونالد ترامپ
در تماس تلفنی با
بنیامین نتانیاهو
به‌شدت از تشدید عملیات اسرائیل در لبنان انتقاد کرده است.
بر اساس این گزارش، ترامپ با لحنی تند به نتانیاهو گفته است:
▪️
«تو دیوانه شده‌ای. داری چه کار می‌کنی؟»
▪️
«اگر من نبودم الان در زندان بودی.»
▪️
«دارم تو را نجات می‌دهم.»
▪️
«الان همه از تو متنفرند.»
▪️
«به خاطر این اتفاقات، همه از اسرائیل متنفر شده‌اند.»
یک مقام آمریکایی به آکسیوس گفته این تماس یکی از
پرتنش‌ترین و تندترین گفت‌وگوها
میان دو رهبر بوده است.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/16860" target="_blank">📅 07:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16859">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from📣خبر فوری ایران💯</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11be99e5c8.mp4?token=FQGaO45pUmHdAFl1u42GkYiTiS8vauDQVQd8qMaN20OafQn2ZUP04UKc7FTM-J6Yh51Nfipi9GT3E2vz5JuFNdMV83vxZ2tWNlxlEog2g-lwZJA6r45FpB7D_5GW2-uqn6K0I5Es79VzmYO9DG3Na6jYKZYrMs0mgBCjW9PM2cXwGUOsYWX1gpNpFBcOTXTUIdBhp9BSMH5697iebQwGvs6tfOa0-fDBhB8Mc4GWK8JvOgUN4iyyDbjWKVI7d4i_j6glWn4JyEZpBXU3UgwmjtyTUTy8IaW0_DtnfyK-Wa4wNxjpyZ-0bNU90IgJf-09k5OlhvyRaIMTvvWkVylDujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11be99e5c8.mp4?token=FQGaO45pUmHdAFl1u42GkYiTiS8vauDQVQd8qMaN20OafQn2ZUP04UKc7FTM-J6Yh51Nfipi9GT3E2vz5JuFNdMV83vxZ2tWNlxlEog2g-lwZJA6r45FpB7D_5GW2-uqn6K0I5Es79VzmYO9DG3Na6jYKZYrMs0mgBCjW9PM2cXwGUOsYWX1gpNpFBcOTXTUIdBhp9BSMH5697iebQwGvs6tfOa0-fDBhB8Mc4GWK8JvOgUN4iyyDbjWKVI7d4i_j6glWn4JyEZpBXU3UgwmjtyTUTy8IaW0_DtnfyK-Wa4wNxjpyZ-0bNU90IgJf-09k5OlhvyRaIMTvvWkVylDujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با یک خانم فرانسوی در میدان انقلاب تهران که در تجمعات انقلابی این شبها شرکت می کند
🆑
@kh_fouri
🇮🇷</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16859" target="_blank">📅 00:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16858">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYcdv8wX4YLB6bZxl3jnCva55L-CsHzzMj37008rYRfDK4W2UCeJnQJUPde1RAetHt-wsIrMf0mRiMV-thHG__rEI-iogYLuLDqCNd1yH0vR-arpbcmou_Lfze1ERdPlRzt6Mmxx0T3_KYpNN-7rTxQJymTwBSx3ERCfu_rZLyZpoxID76hddYT0Mqp_TnV08hawe-j9HThiReCmaN15jPaR_K59p9oXrZ5K8y63BQW7JWj3h1LuV0pkFWoWYEx1bUGRxEUwQE5jGwkvONXFXYBjKhaF5rpe4_21IcGdWEwNojF9PURSIB1SIGfIRrqDNH-sEKn4bdp8dzf-TdNLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قالیباف در گفت‌وگو با رئیس مجلس لبنان: جان ما و شما یکی، و پیوند ایران و لبنان ناگسستنی است
💬
رئیس مجلس و رئیس هیات مذاکره کنندۀ ایران در گفت‌وگو با نبیه بری، رئیس مجلس لبنان:
🔻
حزب‌الله و امل امروز هم از سرزمین مادری‌شان و هم از امت اسلامی دفاع می‌کنند. از این جهت پیوند ایران و لبنان ناگسستنی است و جان ما و شما یکی است.
🔻
در ۲ روز گذشته با جدیت توقف حملات اسرائیل را دنبال کرده‌ایم و اگر جنایت‌ها ادامه پیدا کند نه‌تنها روند گفت‌وگوها را متوقف می‌کنیم بلکه جلوی رژیم‌صهیونیستی خواهیم ایستاد.
🔻
ما مصمم هستیم که آتش‌بس در همه‌جای لبنان و به‌ویژه در جنوب این کشور برقرار شود.
🔻
چنانچه توافقی برای پایان جنگ بین ایران و آمریکا شکل بگیرد شامل توقف حملات در همه جبهه‌ها به‌ویژه لبنان خواهد بود.
🔸
رئیس مجلس لبنان ضمن تقدیر از تلاش‌های جمهوری اسلامی ایران برای توقف جنایت‌های رژیم صهیونیستی گفت: لبنان هرگز مواضع مثبت ایران در این مرحلۀ حساس را فراموش نمی‌کند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/16858" target="_blank">📅 00:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16857">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شما خونه تون مورچه داره؟!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16857" target="_blank">📅 00:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16856">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حزب الله پیشنهاد آتش بس را رد کرده و به سمت شمال اسرائیل حمله راکتی کرد!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/16856" target="_blank">📅 00:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16855">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ادعای رسانه اسراییلی: تعویق حمله به ضاحیه بیروت در پی مداخله آمریکا  سازمان رادیو و تلویزیون اسراییل  گزارش داد که طرح حمله نظامی به ضاحیه جنوبی بیروت به دلیل دخالت‌های طرف آمریکایی به تعویق افتاده است.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16855" target="_blank">📅 23:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16854">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نمیدانم منظور جناب ولایتی از اشاره به «ذات السلاسل» کدام جنگ است اما بد نیست بدانید که هر دو جنگ موسوم به این نام توسط سگ هایی رهبری شد که هم ضدایرانی بودند و هم ضدشیعی.   یکی توسط عمروعاص (دوست صمیمی رفیق بهزاد ف) ضد وحوش دیگر عرب و دیگری توسط خالد بن ولید…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/16854" target="_blank">📅 22:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16853">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نمیدانم منظور جناب ولایتی از اشاره به «ذات السلاسل» کدام جنگ است اما بد نیست بدانید که هر دو جنگ موسوم به این نام توسط سگ هایی رهبری شد که هم ضدایرانی بودند و هم ضدشیعی.
یکی توسط عمروعاص (دوست صمیمی رفیق بهزاد ف) ضد وحوش دیگر عرب و دیگری توسط
خالد بن ولید
حرامزاده ضد ایرانیان.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16853" target="_blank">📅 22:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16852">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ولایتی:
بمباران ضاحیه ونقض آتش‌بس عجلۀ رژیم جعلی برای پایان دادن به تاریخ نحس خویش است.
🔹
شما آغاز کردید، اما برخلاف انفعال تماشاچیان منطقه، ایران و جبهه مقاومت تا آخر کنار مردم عزیز لبنان، از مسلمان تا مارونی ایستاده است.
🔹
تاریخ تکرار میشود و پاسخی از جنس «ذات‌السلاسل» در راه است تا زنجیرهای اسارت را بگسلد. «نقطه‌ی پایان این کتاب باماست».</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16852" target="_blank">📅 22:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انتشار اخباری دال بر پرتاب موشک از کرج!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16851" target="_blank">📅 21:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16850">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انتشار اخباری دال بر پرتاب موشک از کرج!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16850" target="_blank">📅 21:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16849">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yct6M9TBI780mOr1qGiOKjtg_TIsOUr0lLfPp9N2THwaE9mVgCb5N9waiEVDjoj4Y550ttLoA-RaT7BMqo1g8xz3gxh-suuUX4ABW1jqYWFRfycZMId2R8bdIYMYXeQX5-cu3q1u5mRtnzrPvglELewju6Gv6c3KXROF7oibn47eoePplyPZSuHjoRhUfLG_1JMTX0W8A9NhzyJAtXJYXs29AWiYrDyxeaRrQaOZug8iBXH3YJ9Bv7dHQhU4wSvVOhZGXs-0eS9nTxaiw8A90-jKtCUI9YAkvHN9lEmGNgaUL5kcj7qMKT-4lLRMsYFZaKPon9e5l5TE75OQ6Xb9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/16849" target="_blank">📅 21:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16848">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حزب الله از طریق ناهیب بري، رئیس پارلمان لبنان، به ایالات متحده اطلاع داده است که آماده پذیرش آتش‌بس کامل و فوری با اسرائیل است.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/16848" target="_blank">📅 20:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16847">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16847" target="_blank">📅 20:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16846">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ادعای رسانه اسراییلی: تعویق حمله به ضاحیه بیروت در پی مداخله آمریکا  سازمان رادیو و تلویزیون اسراییل  گزارش داد که طرح حمله نظامی به ضاحیه جنوبی بیروت به دلیل دخالت‌های طرف آمریکایی به تعویق افتاده است.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16846" target="_blank">📅 20:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16845">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ و نخست‌وزیر اسرائیل نتانیاهو در حال حاضر در حال صحبت تلفنی هستند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/16845" target="_blank">📅 20:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16844">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چرا میخند؟</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16844" target="_blank">📅 20:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16843">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">با دوستان مروت؛ با دشمنان مدارا</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16843" target="_blank">📅 20:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16842">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محسن رضایی: صبر ایران حدی دارد  تنگه هرمز تحت مدیریت ایران است. اجازه تداوم محاصره دریایی را نخواهیم داد و تشدید تنش در لبنان هم تحمل نخواهد شد. صبر نیروهای مسلح جمهوری اسلامی ایران حدی دارد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16842" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16841">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16841" target="_blank">📅 20:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16840">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ به ان‌بی‌سی: ما محاصره تنگه هرمز را حفظ خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16840" target="_blank">📅 19:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16839">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ به ان‌بی‌سی: ما محاصره تنگه هرمز را حفظ خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16839" target="_blank">📅 19:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16838">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حالا توجه کنید که در همین مدت که آمریکایی ها دهها کشتی تجاری را از تنگه هرمز عبور داده اند، محاصره دریایی شان را کماکان اعمال میکنند و این یعنی کارتی که ایران دارد (تنگه هرمز) در حال کم اثر شدن است اما کارتی که آنها دارند (محاصره دریایی) کماکان در دستشان باقی…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16838" target="_blank">📅 19:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16837">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">محسن رضایی: صبر ایران حدی دارد
تنگه هرمز تحت مدیریت ایران است. اجازه تداوم محاصره دریایی را نخواهیم داد و تشدید تنش در لبنان هم تحمل نخواهد شد. صبر نیروهای مسلح جمهوری اسلامی ایران حدی دارد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16837" target="_blank">📅 19:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roCT18dEu_eziWmoFi_p0OP8PCX_gJyMxcV2fxPvfRm-rGE9GQErV7Glfnt97jHG7Oyn7-hHO6iNEEPZSSL82LjPf3GC1q9NVt2V7_EXjllgvyMoFemHndAFxr0E_ewglAvv5DNLbOrmyKoL-csAh2Q461Qo1nJLsTbuEI112qeJQU5LGcp_33MXXj-g96ledqY38EesFcSjXRoFF337q6mxTTUx8mrUgIUe6lVbRt8O06K4EYhKLHb3c2BSTwvejOYhbkJ57fRQMMD348OgSOiK8m1CBW4YGLqqg2eyBRkcSIdUFlUWNuIXvK5TYYwI3omWx6vSlQDYRO2Dk21iPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایده خوبی است بسم الله!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16836" target="_blank">📅 18:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16835">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست  آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.  نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.  آمریکا و اسرائیل مسئول…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/16835" target="_blank">📅 18:10 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
