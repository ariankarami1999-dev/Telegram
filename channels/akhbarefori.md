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
<img src="https://cdn4.telesco.pe/file/FHadioX0GrbajPg9EV7dJdGyH5-KIOqcUbiMhmHC9gRh-FTSQVeZpppE9G0ADWLYXehZKjpSzvcPxbKfmc3XtOCnSlFXsXfymYTJ9dE8Vw2B-x133CPALaBhHEZbuWXHUY4QMsAqDXPZ7EZrAgZMnmPotxeutskqHbQGtfORB7JQznGB9ny1NP2raqffJBLquzvqgFjt0WSN95jqPZm02TeGSQFvKv3vxPaPYHRoVxV26OT72x2qVakmigMh5tQHvbH2hLIvH_4-hGT2Cot9xAczd7v6_jJMi6tWyJ1jyvb-0dvXH8BNOo76MtUsNwEf4pj855Vg--OTEpVaqAn0gw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 11:01:25</div>
<hr>

<div class="tg-post" id="msg-675060">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
بغداد: جنگ ایران ۴۵ میلیارد دلار برای عراق هزینه داشته است
الحره:
🔹
مشاور مالی نخست‌وزیر عراق، مظهر محمد صالح، تخمین زد که جنگ ایران بین ۴۰ تا ۴۵ میلیارد دلار برای عراق هزینه داشته است که ناشی از کاهش شدید صادرات نفت است.
🔹
پیش از جنگ،  عراق روزانه حدود ۳.۳ میلیون بشکه نفت خام صادر می‌کرد که حالا به کمتر از ۱۰ درصد سطح عادی خود کاهش یافته است.
🔹
نفت برای عراق سالانه حدود ۸۸ میلیارد دلار درآمد ایجاد می‌کرد./خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/675060" target="_blank">📅 10:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675059">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2mTBCIL2amIc5X02Yecj3N_-cZMte2fct-bUV83oBRt6aDERD8wCGkB-Ehxtb2d3tqlh7V27Z9GMdEvNM0b9j0QsxEK6T8J-KR8ZhLjtNgHDfzekPZtlrUxh9CEOqa9998yun_vYSulUL26M0uqNfI5S-C3dVyC9YjhoQ11lMVlY0We8smKIa70oxW9PNzhVUfxuS3zy2ukxTeQyoqbFjuU4c4jcZeeC2SyljPFGEZa6IUpgZoVSwkc8fkNVy61cpYhO5WLbyOHYeiNJ-gaDslZcK4nLe0ZDPdJ5kymUtJztgGZTPfejxxrqcq7WuXw3jVd5BCIR3kbe7AaKNhkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جامونده‌های اربعین، این فراخوان مخصوص شماست!
🚩
می‌خوای توی حال و هوای پیاده‌روی اربعین شریک باشی؟ با شرکت در پویش «زیارت به نیابت از رهبر شهید»، هم نایب‌الزیاره می‌شی و هم می‌تونی مسافر کربلا بشی!
🔸
۱۰۰۱ جایزه سفر به کربلای معلی
🔸
برای ثبت‌نام در قرعه‌کشی، عدد ۲ را به سامانه ۳۰۰۰۱۱۵۲ ارسال کنید.
این فرصت رو از دست نده
@Heyate_gharar</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/675059" target="_blank">📅 10:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675058">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0ffd72ba.mp4?token=ZfJCeqZ28ai2nk1AdlmodXYanG0B8nHmW8LwBPvJblu1Sn-mhULzHlx1OLvghlDi5TIpsswLZCophGDaZ3R6H2jZa8Ivvo8nov5bbXqCfVkPNA_mMq-ZE43cuob4Q7TIivfDmekH6Kq7ZFMvZZWCbwrwLN1K6c5bBnNL9t6CaLhbj6U1DeMRYAdq1-cWhH8uSyHgXGBxXmxt5fUKpcSng1JuZ5tD6p2f8mhozZW2SK_hvoGQPWGXfFJhVxzLDg_oSgVmOMU8MG1Bfi3IU_4bq1xOXmSprAuIQ4fER6ZPBAy1JZPYhTu6BPM6xh29fnGHyoFkEpS66Aw6Cr_HCO3d8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0ffd72ba.mp4?token=ZfJCeqZ28ai2nk1AdlmodXYanG0B8nHmW8LwBPvJblu1Sn-mhULzHlx1OLvghlDi5TIpsswLZCophGDaZ3R6H2jZa8Ivvo8nov5bbXqCfVkPNA_mMq-ZE43cuob4Q7TIivfDmekH6Kq7ZFMvZZWCbwrwLN1K6c5bBnNL9t6CaLhbj6U1DeMRYAdq1-cWhH8uSyHgXGBxXmxt5fUKpcSng1JuZ5tD6p2f8mhozZW2SK_hvoGQPWGXfFJhVxzLDg_oSgVmOMU8MG1Bfi3IU_4bq1xOXmSprAuIQ4fER6ZPBAy1JZPYhTu6BPM6xh29fnGHyoFkEpS66Aw6Cr_HCO3d8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/675058" target="_blank">📅 10:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675057">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TivZAcFfc5u-gcSULSNUeEVe1dOAzXRLaCQUaVGZmSzRxtolmidFHY7AwB0egKRdpOv9obSiNFjyZvjnVXsc9RkrVSVAGU6XyQoAg0ELdgM068_SNRW7itVQj1VoEuqhztaSrll9l59-Y2MYrtdcJVZzsV-efrlTzV2dLryaP7sYySlPIi259aGHVj_MKI0erEQFy3VpTEtESCM1muP5-CJ7GcEy1xqXOedC5urrUTAZrCvIC-g-6Q3Y10DrFm4_whrKvy1yOuIm0qX8ac7ue1hcNhzU422fa144d95m-pTpGfl2Qq0KT1EMCnvv8kO1gtThVOzoxuWBp_xk4lsohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودمان را خلع سلاح نکنیم!  مهتا قره‌داشی سردبیر خبرفوری:
🔹
دکترین رسمی دفاعی آمریکا می‌گوید «رسانه، بخشی از توان رزمی نیروهای مسلح است.» این را پنتاگون سال‌ها پیش در اسناد راهبردی خود ثبت کرده.
🔹
رسانه برای آنها فقط ویترین اخبار نیست؛ یک سامانه موشکی در «محیط…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/675057" target="_blank">📅 10:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675056">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در اصفهان
استانداری اصفهان:
🔹
احتمال شنیده‌شدن صدای انفجار کنترل‌شده در جنوب و غرب اصفهان، بهارستان و صفه و ابریشم تا بعدازظهر امروز وجود دارد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/675056" target="_blank">📅 10:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675055">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d6e30712.mp4?token=lFn6e8IiuHEGnfMLUtDHo_Jk77VAkJwWzQ9IweX-IMy8YbyzO586r58eZHVIyqCW-wDtfuncD6-lB7A6LppOR_g_cBJTliKyOgRd1y-1AOXciykH4Q67akPASpnnHeSubzA7HqQA3N-lLmHged6DYHnueCB7Raz4jzi6W76dQ_BL3fBhviHcSSR3va7lUNOZ2PN1vW_RUgVWBHSVWFErUtZgMQjRE_RPDkY6J3yFogaFmTMeHeJ6JB0Mf5A1se_fNbWY_n4RO2CrTOXAtHnR8Zz_u4SCWPAHQ2D63lBT6VvsmHiF_vPJYzWA4xTX2uAnywol7bjc4Tt9Kq_J-OSK9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d6e30712.mp4?token=lFn6e8IiuHEGnfMLUtDHo_Jk77VAkJwWzQ9IweX-IMy8YbyzO586r58eZHVIyqCW-wDtfuncD6-lB7A6LppOR_g_cBJTliKyOgRd1y-1AOXciykH4Q67akPASpnnHeSubzA7HqQA3N-lLmHged6DYHnueCB7Raz4jzi6W76dQ_BL3fBhviHcSSR3va7lUNOZ2PN1vW_RUgVWBHSVWFErUtZgMQjRE_RPDkY6J3yFogaFmTMeHeJ6JB0Mf5A1se_fNbWY_n4RO2CrTOXAtHnR8Zz_u4SCWPAHQ2D63lBT6VvsmHiF_vPJYzWA4xTX2uAnywol7bjc4Tt9Kq_J-OSK9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعال شدن آبفشان چابهار در فصل مونسون
🔹
آبفشان چابهار با وزش بادهای موسمی اقیانوس هند و بالا آمدن سطح آب دریا، حدود سه ماه فعال می‌شود و از نیمه شهریور دیگر این جاذبه طبیعی قابل مشاهده نیست.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/675055" target="_blank">📅 10:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675054">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74dddcfba.mp4?token=G8LK-Ny_aQXkuAaD1MDthGBAc3GfHLsyRsn-YFRdmp29dHww3kwDICukZwZFZqA6xZeIZTXnZeADMq8kpGRADhl3Ws8x0kmxGWMjduGwyBHhZVyTOPZCuk2SJkPrVdF6sKw3CWO_sWTPG9kBU3O8LsiPC3z76lCLekt7qvJa3qX3AhnbR0TLfzrov4dgxInZlnGBzntw5S4EQ9ZShkDHhxqpX1wc5T2_0pFsuWrknRfZud2GyiEJ34cYSLafE3GF5fCR8mPpQUfdLFFmy5nNGbPggDpXbyz5mLHe9hdocMCxXocEQ9ubG2xb_NXFKkHP4YB_6orGHKEZgXwEOcOqGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74dddcfba.mp4?token=G8LK-Ny_aQXkuAaD1MDthGBAc3GfHLsyRsn-YFRdmp29dHww3kwDICukZwZFZqA6xZeIZTXnZeADMq8kpGRADhl3Ws8x0kmxGWMjduGwyBHhZVyTOPZCuk2SJkPrVdF6sKw3CWO_sWTPG9kBU3O8LsiPC3z76lCLekt7qvJa3qX3AhnbR0TLfzrov4dgxInZlnGBzntw5S4EQ9ZShkDHhxqpX1wc5T2_0pFsuWrknRfZud2GyiEJ34cYSLafE3GF5fCR8mPpQUfdLFFmy5nNGbPggDpXbyz5mLHe9hdocMCxXocEQ9ubG2xb_NXFKkHP4YB_6orGHKEZgXwEOcOqGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سالاد سیب زمینی خودش یک شام مقوی و خوشمزست
😋
🥗
مواد لازم:
🔹
کلم قرمز
🔹
کاهو پیچ
🔹
خیارشور
🔹
نخود سبز
🔹
سیب زمینی
🔹
سس مایونز
🔹
ذرت و جعفری
🔹
نمک و فلفل سیاه
🔹
پودر سیر و آویشن #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/675054" target="_blank">📅 10:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675053">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiIjR0c-AabZ8ggrD1tKTbUeoKpPtBwuwchP_BImqEC_iBCyh2Aspe8wFQBBHRQui3uPHlZow-45NL-op4A4S2vroxXov_Qs6xf_PdvBBpaRsYtf_74muqK8rg-sntoxPT_wb0m3HbuOEyUk-Q-K4i8sQqcOsc6124xu2Tg47d6TFmM193eILRMf1p5Gzfeplj4zZv-jN1KeeEqRnBjmthhgDN3USD62mg5yif0AmgFcSKjTMqLYdjhkvx5hHyAYOaPmWJBEl7zXbeMaH9udhW4bnMw4pY62x_bvIiKBopgN7gUAI5DOjyJJweaxPzwKfLcLoBUpxYWaqYbGutwqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پنتاگون تعداد کشته‌شده‌های آمریکایی را کم کرد
ای‌بی‌سی نیوز:
🔹
پنتاگون تعداد کشته‌شدگان و مجروحان جنگی ایران را کاهش داد و این امر پرسش‌ها و خشم زیادی را برانگیخت. این پایگاه داده به عنوان سند عمومی و معتبر دولت از کشته‌شدگان جنگی عمل می‌کند.
🔹
مقامات وزارت دفاع این اختلافات را به یک اشتباه فنی نسبت می‌دهند. قانون‌گذاران می‌گویند دولت در حال مبهم کردن تعداد تلفات است و سعی دارد با تغییر نام جنگ، محدودیت ۶۰ روزه اقدام نظامی بدون مجوز کنگره را دور بزند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/675053" target="_blank">📅 10:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675052">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تا ساعتی دیگر بیانیه مهم نیروهای مسلح یمن منتشر می‌شود
نیروهای مسلح یمن:
🔹
ساعت سه بعدازظهر به وقت محلی (۱۵:۳٠ به وقت تهران) بیانیه مهمی درباره انجام یک عملیات «مهم و گسترده» صادر خواهدکرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/675052" target="_blank">📅 10:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675051">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
پایان دوران مسی در آرژانتین
🔹
لیاندرو پاردس هم‌بازی لیونل مسی در مصاحبه اخیر خود در واکنش به خداحافظی مسی از تیم ملی آرژانتین: فکر می‌کنم مسی تصمیمش را گرفته که فینال جام جهانی، آخرین بازی‌اش او با تیم ملی باشد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/675051" target="_blank">📅 10:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675050">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEgzrOf8QfC2QZ7NzoSIMSHzUHUFhppaA9mPdF4OIVAqwJjahb8NPPCDEJvIAQ3y_pf9NAEzh5Imv1_f-AHRVWt8uoLSaYah-Le5yFX_BvkVMHDqJlNLzrHVTqdfbisRbJd2YQwyvyoBWO0h4rvzpjiw_I8bB552tpx2ohMxqdUOfPuOV-lqtWysDKjzkac0wPEKpzISiDx7Asp8vHviFhmPIpfd6qzfDcPjRl6U5zqkD6JE9eAKqu1D-blEkUPbdg6t5l0IJczD6EwCLfiWDrVLRaRbVe_wShJjjAbwJuO9QmdWLv8_zs55KCSRMfO2Jsp25AZ1L-r8iilbY5_etw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/675050" target="_blank">📅 10:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675049">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBxSUh0LzkBpVkvnyF9VaFiHmOf3J5oqemoDyf_mDehILOIgKbak9rCEsB6zK-sOaMjveBF1Ot4VKqHv59QArfZ2rAk086nh6m9bYxAC9lKOUUX8vcJK1Fp9WoIdlDXiepFIomGviMoM9pVvPWxn0Y0T9GGH_2GASrSJeI3OMhozKNrx9jXWb8GxKp1V9m_lDrEz7trXiGd99_9b2AlJSOSqmSnKcv0P9sw5sYY3t3XD4Qtgh-KLGPqt1y2CpTItN6o9pYHnrL7l6YumdjGYzjKQQk8s23gCauLbKaK_i5o7NT1HMe5krjfLmv19r_ec5NPc1hRmE75b-K4s4Dh91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلمان از جنگ با ایران عقب کشید؛ کشتی‌ها برگشتند
رسانه نظامی Defense News:
🔹
با توجه به اینکه پایانی برای جنگ ایران متصور نیست، آلمان دو فروند از کشتی‌های نیروی دریایی خود را که برای مأموریت هرمز در نظر گرفته شده بودند، از این مأموریت خارج کرد.
🔹
مین‌یاب «فولدا» و کشتی پشتیبانی «موزل» راهی شرق مدیترانه شده‌اند و تا مشخص شدن اینکه آیا اساساً مأموریتی در کار خواهد بود یا نه، در همان منطقه باقی می‌مانند.
🔹
وزارت دفاع آلمان صراحتاً گفت: «با شروع دوباره درگیری‌ها بین ایران و آمریکا، دیگر شرایط برای مأموریت فراهم نیست.» /خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/675049" target="_blank">📅 10:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675048">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3R5LsQR8yPy2eqjtpFpENLOW43HDGqfhOER4jfk_NDEbo8-xAen-R_dbwfENQzXMlUE6jvElkydIPyAxrF-1idTSnFafENYuCbwQOBJfOlzIcZg-yPAgWL6-MhV5wFcBCKa86QQKqUmemm70yV76jcHt-2TDowypoY_LSw8UPUzL4RmENZt0LSgse5R1Team83vKSzdllbnZ6emla2rnDaQKVVFHUyowkwsiMDtiRGYPrRqqGDfgZRI-Y3QscGg6_YtuiuXl2Gi4POIL90KnoCycCVlFNKz58EyKtKLSWA4kz5O8MpkjAiZlQ4i6ny8EkkZMu_uJicu_4NjDZX3fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👠
UPGRADE YOUR STYLE!
‼️
تا ۷۰٪ تخفیف بر روی کیف، صندل، کفش، اکسسوری و البسه زنانه و مردانه چرم
💳
پرداخت اقساطی با اسنپ پی در خرید آنلاین
💳
پرداخت اقساطی با اسنپ پی، دیجی پی و زرین پلاس در خرید حضوری(مشهد، اصفهان، شیراز، اردبیل، بابل، بابلسر، کلارآباد، زاهدان)
🆔
@monofashion_co
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/675048" target="_blank">📅 10:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675047">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
توقف فعالیت ۲ فرودگاه عربستان پس از حملات یمن
🔹
فرودگاه‌های «امیر عبدالمحسن بن عبدالعزیز» و «عبدالله بن عبدالعزیز» در جیزان و ینبع، در پی حملات یمن، به طور موقت فعالیت خود را متوقف کردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/675047" target="_blank">📅 10:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675046">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm4DDfNd3CuSu2SYtX9T4hYwLppDIrH3nvCzYEheksAKrc921cJJb8Sl_WGnSaxyjqWYeUNa7LO0jZXXsxsVUqDe0K3PZ9YhBrkvjyi9r5WjlT0yGPDHpDQ1kuuYMsC_U33qyEl3Zor1uG9cBHnkxPmRxtzJLRgdHueCM4itZbz25k45n6KAnBvDtecISNYyDP_tQlCmbfbGFChO-8hiwMBW9kqzAu8NSLZDx1fkQtarojHE9qdt_ttIuMEznT2jxwBefT37NIC1rFgHPauE7qRpgXRN_TBgQ3XbK1l5lTGqFcZtipkGxE00lydRGOyZB3KVBTaB5voGNT0GNadVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری اینفانتینو برای تولد مهدی مهدوی‌کیا
🔹
«صمیمانه‌ترین تبریک تولد را به یکی از بزرگان فوتبال آسیا و جهان، مهدی مهدوی‌کیا، تقدیم می‌کنم. دوران درخشان بازی تو در سطح باشگاهی و ملی، به‌ویژه نمایش فراموش‌نشدنی‌ات در جام جهانی ۱۹۹۸، هرگز از یادها نخواهد رفت.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/675046" target="_blank">📅 09:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675045">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
هشدار انصارالله به ریاض: محاصره اقتصادی یمن واقعیت دارد
🔹
محمد عبدالسلام با انتقاد از قطعنامه‌های سازمان ملل که تحت نفوذ نفتی عربستان تصویب شده‌اند، هشدار داد ریاض شکست هشت‌ساله نظامی خود را نمی‌تواند با محاصره اقتصادی جبران کند و مرتکب اشتباه محاسباتی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/675045" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675044">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
نیویورک‌تایمز: نیروهای وابسته به ایران می‌خواستند در ترکیه هواپیمای ترامپ را بزنند
ادعای نیویورک‌تایمز:
🔹
ترامپ با جت اهدایی قطر، بدون سیستم دفاعی پیشرفته، به آنکارا پرواز کرد و با ایر فورس وان قدیمی به خانه برگشت. سرویس مخفی امریکا پس از دریافت اطلاعاتی مبنی بر طرح شلیک موشک به هواپیمای رئیس‌جمهور، تصمیم به تعویض هواپیما گرفت.
🔹
به گفته منابع ناشناس پس از آنکه مقامات آمریکایی این تهدید را شناسایی کردند، سرویس مخفی به ترامپ توصیه کرد که قبل از ترک کشور هواپیما را عوض کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/675044" target="_blank">📅 09:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675043">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
راز آخرین‌جلسه شمخانی فاش شد
👇
khabarfoori.com/fa/tiny/news-3232741
🔹
امروز کدام شهرهای ایران هدف حمله قرار گرفت؟ + جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3232597
🔹
جنجال بازیگر فیلم‌های مستهجن پس از فینال جام جهانی
👇
khabarfoori.com/fa/tiny/news-3232778
🔹
رایزنی‌های فشرده برای آتش‌بس ۱۰ روزه | ایران چراغ سبز نشان داد؟
👇
khabarfoori.com/fa/tiny/news-3232805
🔹
اختلاف پزشکیان و جبلی بالا گرفت | ماجرای توبیخ رییس صداوسیما چه بود؟
👇
khabarfoori.com/fa/tiny/news-3232771
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/675043" target="_blank">📅 09:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675042">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
صنعا: تأسیسات نفتی عربستان در فهرست اهداف ماست
معاون وزیر خارجه دولت صنعا:
🔹
تأسیسات نفتی عربستان در فهرست اهداف نیروهای یمنی قرار دارد و در صورت تشدید تنش، پاسخ سختی داده خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/675042" target="_blank">📅 09:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675041">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c3f4524d.mp4?token=igPVUkQAF9F-jYY-XV8NsdSnhvYXjIWH1myyHB4qGbFLYrpUqE7PzbPHW1FKljfWkD7lUJusGN_njBw8tcuI1lqOiWSM6qXT_EWRkZlv4uQ6rFd2qlyex0k7MV5mQVn7Nowl17O8r5LxoII1H_BfQV4skkr8K-zcCb_eTat0qoYI4x082yBF0exKYlazfH_JR86LJDPJ_VnXZbBEtpNg7T60Zxzvy4Q3t7oB_g_LApWhEBvOE0b4SRz5sKnEayaql5jgNTMAMFCetTWLEN1BGNc9pqQF7mcsdM8Ia_wQVmVkdsgeKHMLw3wogBb7CmBPjB_TwXGiqb7MfmTrAX0Wvz2U_UeIqLzExUzn8vivIiVVfsiGJOAxqoVd3sn7wlI2lyk-eNPWowx1mu0XfcawCM1NTlYi0E-GCYE2xmWUftK1AjYW02OGKdLgtAUnOBW8gev9f9jC9oxIzDd5mKlSiXuJo6cwv0Ho0SUWMlA34nhfeKgzE1EpLu7whIyDW0NWIxwVQwpa02t_P7G2-jckVy64YqIwWhZnYjhyZQAtldLqGbuBIVUUP0REbBTfWszyDDSXfjtWMp0Yxq5UA4YNMnkbx1RYZD4E6HPnk8KmKJUzC8V6NIinaGV1KW-8_ikreru2VeOHTXghj0pTLHDxH1zm1IxFQn6ESWMjmfOqOco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c3f4524d.mp4?token=igPVUkQAF9F-jYY-XV8NsdSnhvYXjIWH1myyHB4qGbFLYrpUqE7PzbPHW1FKljfWkD7lUJusGN_njBw8tcuI1lqOiWSM6qXT_EWRkZlv4uQ6rFd2qlyex0k7MV5mQVn7Nowl17O8r5LxoII1H_BfQV4skkr8K-zcCb_eTat0qoYI4x082yBF0exKYlazfH_JR86LJDPJ_VnXZbBEtpNg7T60Zxzvy4Q3t7oB_g_LApWhEBvOE0b4SRz5sKnEayaql5jgNTMAMFCetTWLEN1BGNc9pqQF7mcsdM8Ia_wQVmVkdsgeKHMLw3wogBb7CmBPjB_TwXGiqb7MfmTrAX0Wvz2U_UeIqLzExUzn8vivIiVVfsiGJOAxqoVd3sn7wlI2lyk-eNPWowx1mu0XfcawCM1NTlYi0E-GCYE2xmWUftK1AjYW02OGKdLgtAUnOBW8gev9f9jC9oxIzDd5mKlSiXuJo6cwv0Ho0SUWMlA34nhfeKgzE1EpLu7whIyDW0NWIxwVQwpa02t_P7G2-jckVy64YqIwWhZnYjhyZQAtldLqGbuBIVUUP0REbBTfWszyDDSXfjtWMp0Yxq5UA4YNMnkbx1RYZD4E6HPnk8KmKJUzC8V6NIinaGV1KW-8_ikreru2VeOHTXghj0pTLHDxH1zm1IxFQn6ESWMjmfOqOco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر پرتاب استارشیپ از خاک مکزیک
🔹
پرتاب دوم استارشیپ، بزرگ‌ترین موشک شرکت اسپیس‌ایکس (۱۲۱ متری) متعلق به ایلان ماسک، از زاویه دید ناظران در خاک مکزیک به ثبت رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/675041" target="_blank">📅 09:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675040">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سی‌ان‌ان: توقف ۱۳ شب حمله پیاپی سنتکام به ایران
شبکه سی‌ان‌ان:
🔹
پس از ۱۳ شب حملات متوالی آمریکا علیه ایران، فرماندهی مرکزی ایالات متحده (سنتکام) روز جمعه هیچ اطلاعیه‌ای مبنی بر انجام حمله جدید منتشر نکرده است.
🔹
هنوز مشخص نیست این موضوع به معنای توقف عملیات نظامی است یا خیر./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/675040" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675039">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عراقچی در گفتگو با همتای روسی: مصمم به دفاع از منافع و امنیت ملی ایران هستیم.
🔹
۲۷ نفر در حمله مرگبار تروریستی به یک مقر امنیتی در پاکستان کشته شدند.
🔹
گوترش، اولین دبیرکل سازمان ملل پس از جنگ، وارد دمشق شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/675039" target="_blank">📅 09:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675038">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNgIuvnJpHi-ovH_6B1peko3NP3VhWZSIodZy2sEwEyuYutwIu71kSM8rqMJ1OhlCTQVan4fEgeIXIJYXfIR1Ete4X9yW7FhyqjBJPUdqVKwM77JatWaug-CTGHOgO6FJGx2FsqNGKCSIZg71PR1UDKb-XDbyi1OYbSKkiGDVXmU-XL-b1NhWTPOzlwwBbOQs3DcE8eNqtsAAIu_qiLJ6bW5HcBxPxTxam8zWRtYH0izRRh4YmhK8Cp1uNhUKGJ64xvIn1m8tdXEYkO_yfRV3edCM8zcBhx3EzYj_WnffWOStPJTwOewAbJHFrzY_kJTN_8It0v5jePfnf7nU3_Bgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ نشانه پیش‌دیابت که باید مراقب باشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/675038" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675037">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suWdaYEZBUQjI7MJ8UZyqP7F82IE_whJAdtR3GqgKYl5siwBujIjkO7KbUqH0QKQCyzuMycmOnADu9gcoTpgnvP49YQzi8-wCphZJ6tKcoV1APccsqrhUGRMlsBv6oXM5vW8mPSXqpqZpj3I_qJzcRptX6LEzZhwH2x5FcrznM-7kwgI-rsJG5UgisdyMG91eOjL8Pm6BXArNZL44AJgVgYHt3-0tdj5c_7Fc2YSs2Vey8gMuu5236yzXuaFdqhlsiuzbiC-nrga9rZ605AOepoUfHa98-78z0wnBxZv63tx0mBge9lDMRs9sIyJaRB2Jgq83HBSSmkfkVkXVIsiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس کانال ۴.۹ میلیون واحد پس گرفت
🔹
شاخص کل بورس تهران ۳۵ هزار واحد مثبت و بار دیگر وارد کانال ۴.۹ میلیون واحد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/675037" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675036">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8878ba219a.mp4?token=paXoxQZVCzKncdZ7C8nKveetkPFkObt7h49uUnSFckS-SBigjcYeCWbFMhvrhrE-K2zfe-aiwddmhw-hlHoAOhrWvTPx5HX-5kFXpcD9pVUNghPiK_OjEM5ovZ28Pobqjyp5bbuGwcyxeVAsrNNe2ekWf_OILaEUMRYigB4CKcfpsZBJljWVdc7LOgYsnALEUYMuSYc_lnUP6SXg28mseROv8tKWCHS3KLKn8tKOmYIu0TFzl30KTpJzCCywhvVM_-bf6cu-Q_M_3mfs_b05PZo_72TOPrpKpAVJBdm8oxQ891vG75J3rbwgC1JJ4tjre0xQ8Dpoqbp5ouDv2AF9AYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8878ba219a.mp4?token=paXoxQZVCzKncdZ7C8nKveetkPFkObt7h49uUnSFckS-SBigjcYeCWbFMhvrhrE-K2zfe-aiwddmhw-hlHoAOhrWvTPx5HX-5kFXpcD9pVUNghPiK_OjEM5ovZ28Pobqjyp5bbuGwcyxeVAsrNNe2ekWf_OILaEUMRYigB4CKcfpsZBJljWVdc7LOgYsnALEUYMuSYc_lnUP6SXg28mseROv8tKWCHS3KLKn8tKOmYIu0TFzl30KTpJzCCywhvVM_-bf6cu-Q_M_3mfs_b05PZo_72TOPrpKpAVJBdm8oxQ891vG75J3rbwgC1JJ4tjre0xQ8Dpoqbp5ouDv2AF9AYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران برای رهبر آزادگان جهان فقط خاک نبود؛ عهدی بود که با خونش تمام کرد، ما نیز بر آن عهد که بستیم هستيم  #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/675036" target="_blank">📅 09:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675035">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS16oApbpQ-6r6J0YMQr87-_o-UNigVMZS-xpL9sM6NHEEIAdbUrMR-CrpH50qgLDflsyGWbUHuY4Jsipvfos0wfL531-LDE_8Mz7oJAFSEPuoZ5xR_M0ehep5Y-93zvpQ4a4esd9uwB2SBdIgEsnfj1nNgsNqY2Y9TwG1kjVToFnyn04NCuBqAFHPCrOWJxuGprwO-LmiR1RWClKjBC1lP14hCMM8KbqatRNSigIb08BAQ8_m-2L6lGPZ2RK6lb8nrpKu38SYjyArDczrej6BD50WvTXEzixCpNZbwpnMeM7_Rm6oEqq18Jf-zaSI9X61FxrME2mi6ULJtdKjl8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ازدحام در پمپ‌بنزین‌های عربستان در پی حملات موشکی یمن
🔹
پس از حملات موشکی و پهپادی یمن به تأسیسات نفتی عربستان، صف‌های طولانی خودروها در پمپ‌بنزین‌های شهرهایی چون ریاض و جده تشکیل شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/675035" target="_blank">📅 09:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675034">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
بقائی: اروپا از حقوق بشر می‌گوید، اما جنایات علیه ایران را محکوم نمی‌کند
سخنگوی وزارت خارجه:
🔹
کایا کالاس(مسئول سیاست خارجی اتحادیه اروپا) از نگرانی‌های حقوق بشری حرف می‌زند، اما در برابر جنایات و حملات علیه ایران سکوت می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/675034" target="_blank">📅 09:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675033">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
توهمات سگ‌زرد پایان ندارد؛ می‌خواهم دوبار نامزد انتخابات شوم!
دونالد ترامپ:
🔹
دوباره این کار را انجام خواهم داد. باید آسان باشد. من واقعاً در نامزد شدن برای ریاست‌جمهوری خیلی خوب شده‌ام. سه بار پیروز شدم. بار دوم انتخابات دستکاری شده بود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/675033" target="_blank">📅 08:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675032">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a505e50789.mp4?token=pGf51ZlNiEAYq2GTYkGC9X98cT1ZS84o6xmnT4Q0UVhnKgG42SJURtm1f2ofRupkYsE4Spc_cRm9mqBh85esAjsGoy4zn43z4nghkhhThTcZS1sxlwfGjh7uQoEuBtbnp51LnXsj2ayOTMBsTF7w0ILEwAQv86j-mx3yhZC88YnIyiZVrqikAPQj-9362iQip4Mn4xU_kWV1BpZm-oQ5o4F2s7Gbeo9X4QVkQ5-AZiTyP-0bYPqmfsRku8RckwGJUgHz6eF9ZeTkDm3GjV59AW7t3czpGu2GEBoNxGt_G3It5RRtr-md29gEEJcYbM8YcCI_oJg4K2cXuyFALgrrIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a505e50789.mp4?token=pGf51ZlNiEAYq2GTYkGC9X98cT1ZS84o6xmnT4Q0UVhnKgG42SJURtm1f2ofRupkYsE4Spc_cRm9mqBh85esAjsGoy4zn43z4nghkhhThTcZS1sxlwfGjh7uQoEuBtbnp51LnXsj2ayOTMBsTF7w0ILEwAQv86j-mx3yhZC88YnIyiZVrqikAPQj-9362iQip4Mn4xU_kWV1BpZm-oQ5o4F2s7Gbeo9X4QVkQ5-AZiTyP-0bYPqmfsRku8RckwGJUgHz6eF9ZeTkDm3GjV59AW7t3czpGu2GEBoNxGt_G3It5RRtr-md29gEEJcYbM8YcCI_oJg4K2cXuyFALgrrIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت در جیزان عربستان بعد از حملات تلافی‌جویانه موشکی یمن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/675032" target="_blank">📅 08:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675031">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRboSPnQWHDJdO-mNX6g4WeoVekr07ys6iTGigNsmEpcvWy2w2T9VPXRBdzG0WOZfuSFmimzoN99WlwwtkZ2QmlU8MykE_X9vibuAtdxTdlKKQ942gPjpCC-tmeWKhFLeSbIqyFBRuhT_LHGx__b8_2DnhraIwi1otiuV4rXNhzqjfxmP3sYsLfcEb9iPV2kjI7KO8kjPomjs4PB2cszuJk0nE7dS-T04R_sYR6fYjRxZU521z02yhL8TKJqn5acHiQLteRPDyAgTvDq3ASvUOEyRGp8nVAAqqbKpyD3GxQ-wqF9Id4njzjt56mCzCS1qoJdOmiahbScHVHT07M_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رده‌بندی لیگ‌های باشگاهی فوتبال دنیا از نگاه Opta؛ لیگ برتر ایران در جایگاه ۶١
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/675031" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675029">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3920d4655.mp4?token=jcegKoSmeD2TYN5qnkWHWyEDQhqkKuS9l5USqU1gVHIUK1uazpIk3BzAVWLIrK9CZPl6ZdzCoLFyDryLaMQIa3C_N_2MozpKxRo-j5ZDZC6OXaacx1TCYRJTKYW9HZHhaTDSRaAl7M2BcG3ZR-4i4TBqpCNgGe7iblHhfns4DPukiUZA83xwHSyI5_Hpkd9ZfHgvZXIas1hIjLIdx8wnNtTuX_9MkBdT19edRftVJwnuTDLLhT7TtuZSwXR6tzKtxijf7HZJBfkzCaD5Jyyva1xYHGATzRWtVcYvwgy-Pmjzm3NIJ1J5KRxcVvqpcOMtLEKji8_c7DtXOtOdugvRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3920d4655.mp4?token=jcegKoSmeD2TYN5qnkWHWyEDQhqkKuS9l5USqU1gVHIUK1uazpIk3BzAVWLIrK9CZPl6ZdzCoLFyDryLaMQIa3C_N_2MozpKxRo-j5ZDZC6OXaacx1TCYRJTKYW9HZHhaTDSRaAl7M2BcG3ZR-4i4TBqpCNgGe7iblHhfns4DPukiUZA83xwHSyI5_Hpkd9ZfHgvZXIas1hIjLIdx8wnNtTuX_9MkBdT19edRftVJwnuTDLLhT7TtuZSwXR6tzKtxijf7HZJBfkzCaD5Jyyva1xYHGATzRWtVcYvwgy-Pmjzm3NIJ1J5KRxcVvqpcOMtLEKji8_c7DtXOtOdugvRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفع قوز کمر با کش پیلاتس #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/675029" target="_blank">📅 08:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675027">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiSN454sJfpq4k5yOJjBIETc0K3I4ZPw38JIBfnNI3k3DVR8-msn54vq1Zwc4dQjXNI5MBpD9QI9pD7Jsmh93TxR2thzzUFejL0qUtYYxk7E0LHJsos6H7cdo9UhxxhP9plEp7j0ZBLbtDeqv4uhR0ihUB1zT8lchC_GVxgeXkO8MVuP7PmVP-hPb3pPNzufRmIeOXhhUyU_oV7gzFmcXrJtBvG4x6oNECuIFmxu__ymLwgqshYADbLuh_1_5csT2ErgTl1BluSY3pvZ1ovy1753FFa_rex7f8GhN9ToTyWi1IYsdGQhgIGELES6NEcnE9Sbm1GcV4nWP1aoniM7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4OVip7mXFtBCp33165YgpzqEqfEVDet6bPE2gbBR2tIpb3-niAR8MHMNZqaXy1Jyvtr5Xau8rm_lLfv2jbLHtVAaKFJUEswojpv0hxuWR3VCAnhjtZyL3HG3J7ZcAIlII2ggam0hbqWARJW2S2fgV4W11wLvH-HExXVQA0FxbcFDI8XhDNAqzzZ0gCn6AU7K1Kb_InF3q6IiPKbB7Qp0dvOMOYWK8QwPWpddM1BAD2efPaIataHud1uLeoy17yHI5OO_6cO-Dx-lRVCrTTOHv_qyTc5KBauD_08CAjA4ybbVeqzjs7lK0dF3q-iD0cIN4Nv1uwc6Tr6h57QUKyk3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شادی خیابانی پس از بازی ایران و استرالیا و صعود ایران به جام جهانی فوتبال، آذر۱۳۷۶
🔹
آرشیو آژانس عکس ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/675027" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675026">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
توقف فعالیت ۲ فرودگاه عربستان پس از حملات یمن
🔹
فرودگاه‌های «امیر عبدالمحسن بن عبدالعزیز» و «عبدالله بن عبدالعزیز» در جیزان و ینبع، در پی حملات یمن، به طور موقت فعالیت خود را متوقف کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/675026" target="_blank">📅 08:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675025">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
راز قتلی ۲۷ ساله با افشاگری همسر سابق فاش شد
🔹
پرونده قتلی در داراب که سال ۱۳۷۸ رخ داده بود، ۱۷ سال بعد با افشاگری همسر سابق یکی از متهمان دوباره به جریان افتاد؛ چهار نفر بازداشت و به قتل اعتراف کردند، اما در نهایت با گذشت اولیای دم و پرداخت دیه، محکوم اصلی پس از ۱۰ سال زندان آزاد می‌شود./ همشهری
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/675025" target="_blank">📅 08:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675024">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99a19aa4.mp4?token=UcWFHORsugRNeT9-xYopQ6oU8lu_9GpJ_JEuPsVc7hZ0rdH9Xn8Ii_5LkP5dp4Hv4Klcd0T3Zlq6FusoKjFJt7d5POqNqO2Tkx7uWNPoD_9-LeF6aHes5H0tskuP6GvuiHUTgMlZOrXg32idPL1pAc0Cs4nH_qbGxcbKckgOqB9xBn-D70ZQxyUy-pIg76i-z3TnwUTL3z-F2WBEotGnRBdj-FFL7wV3gsM35DHKhXGrn5LkyKGgKEs1KFEzhfRMB22gaKwpmD5NI_qQlDHOqXB3s_BW1SiWWZr8CflWNQgF8bbHDtw0p3MHtOkBV1m0tPT7hOV1KPUgG9cOicua5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99a19aa4.mp4?token=UcWFHORsugRNeT9-xYopQ6oU8lu_9GpJ_JEuPsVc7hZ0rdH9Xn8Ii_5LkP5dp4Hv4Klcd0T3Zlq6FusoKjFJt7d5POqNqO2Tkx7uWNPoD_9-LeF6aHes5H0tskuP6GvuiHUTgMlZOrXg32idPL1pAc0Cs4nH_qbGxcbKckgOqB9xBn-D70ZQxyUy-pIg76i-z3TnwUTL3z-F2WBEotGnRBdj-FFL7wV3gsM35DHKhXGrn5LkyKGgKEs1KFEzhfRMB22gaKwpmD5NI_qQlDHOqXB3s_BW1SiWWZr8CflWNQgF8bbHDtw0p3MHtOkBV1m0tPT7hOV1KPUgG9cOicua5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای ناسا از وقوع آتش‌سوزی در پالایشگاه‌های شهر جیزان عربستان پس از حملات انصارالله یمن خبر می‌دهد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/675024" target="_blank">📅 07:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675023">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBjFTXmu-wpBzH_1axtQQUUbjpwOkBvHoArUjgFWfI7xlc6NsbOfk9_3p9HmJ7s8WoMNUzqoV7_sMI-jHMqq_VzrYxEGacO0pTzeoGZ0b38e4VgBQRxu-FchHCve8tEJ79ZzeQc1dViWZ5SaKEg7sdN4WRRbMXTkmWCbRjpcxGGowzP8pTdsuOptJajofMGXys9tG-q0tzej_OFbDiJu9i4JhMgX8Xot61mEZaiP4JjoMhd3okGc5XxIr5gr3_9owKLPFghrcM0fRbDb9O8nNwwnq50mLZnP30RT_UPSj1WOf5uCen24mQGLdmaRZ0YzfHfVz6DytyC71FTFjcJurw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از بلند شدن ستون‌های آتش از تأسیسات حیاتی در جیزان عربستان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/675023" target="_blank">📅 07:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675022">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
منابع عربی: شهر ینبع عربستان دوباره مورد هدف موشک‌های یمنی قرار گرفت
/
فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/675022" target="_blank">📅 07:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675021">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRzHD9woSXItmPTzIeSIp_CYPD657v02wDPl870f9aoRevcjfgVLwN_4v-SEchfPdqK70ozZXa2yFBoL02XPuZVWZS7zkZF1_4gBJR8BLg1rNWj4TiIVd6SSU-eAFSMRtf5vSThuowixvE5Sd5xMCOLaNg8oR6SIukTtPyhOSZaruaAx08FH4vKRy8BqeepQFcqGkBDdHay9RhDFCt9mhJ_Vhwz-Y6jtO_QJu4K7QQ2FPw0GNDzwJlQGekq22KIXf1YIaSjky2kQbqZ8WK07MmbpvnFmjg6dyreCaNEKisb-DMIAXG5brDmtf0VMkUfgFx6Bvs3Rj0ERxFq9FFByZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیکر اکبر عبدی ساعت ۹:۳۰ صبح روز یکشنبه، چهارم مرداد از مقابل تالار وحدت تشییع و در قطعه هنرمندان به خاک سپرده خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/675021" target="_blank">📅 07:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675020">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2bdf4584e.mp4?token=YGEcUhsTfb71TAwv8dEbEe68SK8iKJsKalHAvo8a8lQ7RdLiwxySBxxlVpurT5-gx05kYVwE1I13Lml4YIrR0b6QrhdxJG362id0B5jd9qThtYV_Cj_DxDgTQ-7WPGkCXSbOTqO5FPcPOJh5uZqb97zd-JxxZA2YNup1o0d1HqEXC-DRXErVC-p6m-FsqU2AmlOzUTqzfFeBuYns7B3rh8k6T9mdIrLlxTAiWySj7aExP9HUXTgMIB0qabFK6F25-V8roAVbACcVscH31dWAtp1JY4SYkVilMKzU2-2WbVXJL85ck_L9_LFsTfjTUjByGdmcJhHC04aDo2-TTsJzBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2bdf4584e.mp4?token=YGEcUhsTfb71TAwv8dEbEe68SK8iKJsKalHAvo8a8lQ7RdLiwxySBxxlVpurT5-gx05kYVwE1I13Lml4YIrR0b6QrhdxJG362id0B5jd9qThtYV_Cj_DxDgTQ-7WPGkCXSbOTqO5FPcPOJh5uZqb97zd-JxxZA2YNup1o0d1HqEXC-DRXErVC-p6m-FsqU2AmlOzUTqzfFeBuYns7B3rh8k6T9mdIrLlxTAiWySj7aExP9HUXTgMIB0qabFK6F25-V8roAVbACcVscH31dWAtp1JY4SYkVilMKzU2-2WbVXJL85ck_L9_LFsTfjTUjByGdmcJhHC04aDo2-TTsJzBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های اروپایی:  بیش از ۲۰۰ هزار نفر در پی آتش‌سوزی‌های بی‌سابقه در فرانسه و اسپانیا خانه‌های خود را ترک کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/675020" target="_blank">📅 07:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675019">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
احتمال جایگزینی بسته‌های مغذی به جای شیر مدارس/ هدف رساندن کالری به کودکان است
رئیس دبیرخانه شورای عالی سلامت:
🔹
هدف ما رساندن کالری به دانش‌آموزان است بنابراین شاید با توزیع بسته‌های مغذی که مشکلات برنامه شیر مدارس را نداشته باشد و به راحتی قابل توزیع باشد، کالری را به کودکان برسانیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/675019" target="_blank">📅 07:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675018">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98391a474c.mp4?token=oOvR5zXYslDfiw4hGIhZNt9160hzsK9CbHg4xQ9E9xGs_bQJEyd2xMMTlEj2Kn1pNJvfW99n65XJ12IKlgF8HUrJR5oAw4HuVHxGmrBcnQDNv2vWPBARwlnyho2RUef_DUsD7yI0omH_ALq__6jeKJFB1bioNI4R7Of_RNJtxUGPp9FczVap8myICGSzNsV0XduChxD7laO1Ov0YJkAdLLwGeQPBQTrMW7RptacHfeCAYI2849B5J2IpEOkjj73CiHqXwlumw6jde8tggBouzwUwpmeVw6eWEIojNwMGfl_021tHeYVTC60m0f6VZOjxbzc3sI9PaQhjX0ekVKTwUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98391a474c.mp4?token=oOvR5zXYslDfiw4hGIhZNt9160hzsK9CbHg4xQ9E9xGs_bQJEyd2xMMTlEj2Kn1pNJvfW99n65XJ12IKlgF8HUrJR5oAw4HuVHxGmrBcnQDNv2vWPBARwlnyho2RUef_DUsD7yI0omH_ALq__6jeKJFB1bioNI4R7Of_RNJtxUGPp9FczVap8myICGSzNsV0XduChxD7laO1Ov0YJkAdLLwGeQPBQTrMW7RptacHfeCAYI2849B5J2IpEOkjj73CiHqXwlumw6jde8tggBouzwUwpmeVw6eWEIojNwMGfl_021tHeYVTC60m0f6VZOjxbzc3sI9PaQhjX0ekVKTwUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از بلند شدن ستون‌های آتش از تأسیسات حیاتی در جیزان عربستان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/675018" target="_blank">📅 07:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675017">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEqcLr5hKEl_waG2bohRFMK-q8mnj0SK8WBr6z-evreYcR4TudUZP-MEUgP7TmbuDrgTMzdjl1DFHXI-IQ8A3gv51ULpV82j1yEgiWwqdg68-OultaXCunBllG0YpQ3LHPXWZBRVajD-KGbpuNYZwwczo5V2COi7CsLiRM8QDq65rVPojXBxZnK4qj65lKEnAN8OAFVmN35Z0eNxHwkPdEOaI4ExeA3L2lmTFArrCs3Z8G5YbWVZrsALMM0ruVOkVauSL-KBTlVbxe9rjNczsqrC7EPmXCfLK8umEw2qYLWI-Fv3nF325mn9SX5ZEiex2gmwLsXWSUanjuAf6yuFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معادله «تشدید تنش در برابر تشدید تنش» یمنی‌ها در اثر جدید کمال شرف
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/675017" target="_blank">📅 07:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675016">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5zV4wBvf0rXqi2yiKz8FGocU1lOylQjVTc4Ba-6pYGDa-O3PLHH5Myg0glMImaR27dxexCl50iveXqz6qPIbUz9yDvU8U-WVnCJ7L5Tw_QdXrlBDm4YOjfRpjdwneDKAUgltxui8tzOTsIzXILcdymJnMu66k-8njADf2GsDSbL7j1860SzEqOee3BaAY12uspDrx5lrTxmP847EHs1z5o8cYs8Js4qIj9-ZzIN8xqO5Ju7xDlipoS6208aKCdGYYWSXaNoKMLVBUqjFk4edXYgSyd-g_b48kvLJH6rrb4tTooaoeBu7p-W7kzzZEe89ZXxO1yzYxa40HZFMv_jQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۳ مرداد ماه
۱۰ صفر ‌۱۴۴۸
۲۵ جولای ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/675016" target="_blank">📅 07:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675015">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299ed3562c.mp4?token=Ssn4j4atDPWKhHSA2xO3eP_h4Ztap1esmQkFTJTdWuFNx4OHvR93bIfnzYWMo-VCG-E7_9eqB6rwPIEEWCnyA1PhvCRaqq1geHkJ2e--wRsS2KGiIb9moJVjo0tXdF2_KLSXHsDqrox7pE_AoYfccfcZxVhqrMkam1vzDx4VqEtXU-uEsJOb206OUliLnhu20ZiKUQ7ncOjlU6cIePNRmIop7Adl6y75kXmu-j_YyyDMXtwq9SbVm4HEe_p0yLkafKz1W_OhaLycMOgi3L0qEd-5u7nvilAbg1bnouWQBm5XeDUVcGA3gUhGohWNGtsaSqFbHZrKt05TWddaeMFHAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299ed3562c.mp4?token=Ssn4j4atDPWKhHSA2xO3eP_h4Ztap1esmQkFTJTdWuFNx4OHvR93bIfnzYWMo-VCG-E7_9eqB6rwPIEEWCnyA1PhvCRaqq1geHkJ2e--wRsS2KGiIb9moJVjo0tXdF2_KLSXHsDqrox7pE_AoYfccfcZxVhqrMkam1vzDx4VqEtXU-uEsJOb206OUliLnhu20ZiKUQ7ncOjlU6cIePNRmIop7Adl6y75kXmu-j_YyyDMXtwq9SbVm4HEe_p0yLkafKz1W_OhaLycMOgi3L0qEd-5u7nvilAbg1bnouWQBm5XeDUVcGA3gUhGohWNGtsaSqFbHZrKt05TWddaeMFHAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از بلند شدن ستون‌های آتش از تأسیسات حیاتی در جیزان عربستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/675015" target="_blank">📅 07:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675014">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
حمله موشکی جدید یمن به عربستان
🔹
در پی حمله موشکی جدید یمنی‌ها انفجارها در عربستان دوباره شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/675014" target="_blank">📅 07:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675013">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
اختلال و به‌هم‌ریختگی در پروازهای عربستان
🔹
پایگاه‌های ردیابی پرواز از به هم ریختگی در جریان پروازها و عدم امکان فرود تعدادی از هواپیماها در فرودگاه‌های جنوب عربستان خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/675013" target="_blank">📅 06:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675012">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
منابع عربی از تعلیق پروازهای فرودگاه جده، در پی حملات یمن به عربستان خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/675012" target="_blank">📅 06:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675011">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
حمله موشکی جدید یمن به عربستان
🔹
در پی حمله موشکی جدید یمنی‌ها انفجارها در عربستان دوباره شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/675011" target="_blank">📅 06:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675010">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رسانه‌های منطقه از حمله موشکی و پهپادی یمن به عربستان گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/675010" target="_blank">📅 04:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675009">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
عراقچی در دیدار با همتای چینی: ناامنی موجود در تنگه هرمز ناشی از پیمان‌شکنی آمریکا و اخلال در روند اجرای تعهدات ایران وفق مفاد بند ۵ تفاهم اسلام‌آباد است
🔹
وزیر امور خارجه چین: اعاده صلح و آرامش در غرب آسیا مستلزم تقویت اعتماد و همکاری بین کشورهای منطقه‌ است. چین برای هرگونه مساعدت در این زمینه اعلام آمادگی می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/675009" target="_blank">📅 04:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675008">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/akhbarefori/675008" target="_blank">📅 03:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675007">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ترامپ از جنگ با ایران کلافه و خشمگین است
وال‌استریت ژورنال:
🔹
دونالد ترامپ با ورود جنگ ایران به پنجمین ماه خود، از طولانی شدن نبردی فرسایشی که می‌پنداشت ظرف چند هفته پایان می‌یابد، کلافه و خشمگین شده است.
🔹
ترامپ که پنج ماه پیش با اطمینان از «پیروزی سریع» سخن می‌گفت، اکنون در باتلاقی گرفتار شده که نه راه خروج روشنی دارد و نه افقی برای پایان.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/akhbarefori/675007" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675006">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a95efd45d9.mov?token=pl9hn9S-HjWChifo2Kx-oMrwwvHQHvDnTKV5mHBsKG4HeF4yqWENYB7qBjwAZq80aUspOrzTHHWI6ufpfQsDrdZMUNhWDOsTk2O43F83VVKPEKKraL5gri6Qv9GDW3W27_rzPU9eYKJmyVGHW2due2EbMzX_8_8HqTY7fGL3iLO8GmQlhS6EZyHzYv_uPwLuV22Dwmeqp4d_Iu5Y8p_h7JRq5gqCWw16SUMs3Ha-6hYHhilAL2t5o-ZH3x4UxJfF4TT2Gx7sD8GmjWSPwIARSBtXAVZeiA2ijZQVstctMgKV4eZ92zg9X-AobkMW35jXNHh0jarBek2xbtYF_F2tfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a95efd45d9.mov?token=pl9hn9S-HjWChifo2Kx-oMrwwvHQHvDnTKV5mHBsKG4HeF4yqWENYB7qBjwAZq80aUspOrzTHHWI6ufpfQsDrdZMUNhWDOsTk2O43F83VVKPEKKraL5gri6Qv9GDW3W27_rzPU9eYKJmyVGHW2due2EbMzX_8_8HqTY7fGL3iLO8GmQlhS6EZyHzYv_uPwLuV22Dwmeqp4d_Iu5Y8p_h7JRq5gqCWw16SUMs3Ha-6hYHhilAL2t5o-ZH3x4UxJfF4TT2Gx7sD8GmjWSPwIARSBtXAVZeiA2ijZQVstctMgKV4eZ92zg9X-AobkMW35jXNHh0jarBek2xbtYF_F2tfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبور روان زائران اربعین حسینی از مرز شلمچه دقایقی قبل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/akhbarefori/675006" target="_blank">📅 01:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675005">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
نامه‌ ایران به دبیرکل سازمان ملل و شورای امنیت:  هدف قراردادن عامدانه دو شناور ایرانی از سوی آمریکا جنایت جنگی است
🔹
«غلامحسین درزی» سفیر و معاون نمایندگی ایران در سازمان ملل در نامه‌ای به شورای امنیت، درباره حمله آمریکا به شناورهای «ناجی-۱۵» و «ناجی-۱۶» گفت که هدف قراردادن عمدی این دو شناور که در زمان حمله در هیچ گونه فعالیت نظامی مشارکت نداشتند، «نقض جدی و آشکار حقوق بین‌الملل بشردوستانه و مصداق جنایت جنگی است.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/akhbarefori/675005" target="_blank">📅 01:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675004">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
حملۀ ارتش تروریست آمریکا به یک کشتی
🔹
ارتش تروریستی ایالات متحده اعلام کرد یک کشتی تجاری دیگر را که مکرراً برای شکستن محاصرهٔ بنادر ایران تلاش می‌کرد، زمین‌گیر و از کار انداخته است.
🔹
طبق اعلام سازمان تروریستی سنتکام این دومین شناور تجاری است که از زمان برقراری مجدد این محاصره متوقف می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/akhbarefori/675004" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675003">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15c04c185.mp4?token=YI0hwVeTCHI4uX_4OM5zkNSxwUvySUgI5rB7KHfQle7ML7evPEI6lwamWbmeSfCqvecn2pBCHLBmktOikIeIzcgtblCYfQM5q0dAhlZiv1Vo625X4kbbEztvMQHhbmGX8ehvDTWtorIrLW3LGIIIIMGrjNuYqQ45oEPvWUS9OF_Muzd3UAdd7eO6y4WpRpQJ6JRQ0cOSv8HMPUJmNTH68e5oH7ZBntROhvWIbIWbCg795ZwBxrTSaLCutYBhoRF7xCTcwYx016fJtLn4FtYCljssYms3OpyjnLZH7JA9v1Fq3qxQ8KZxilrLvvst6PglOtj4WrIEWl5UblZ5790z9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15c04c185.mp4?token=YI0hwVeTCHI4uX_4OM5zkNSxwUvySUgI5rB7KHfQle7ML7evPEI6lwamWbmeSfCqvecn2pBCHLBmktOikIeIzcgtblCYfQM5q0dAhlZiv1Vo625X4kbbEztvMQHhbmGX8ehvDTWtorIrLW3LGIIIIMGrjNuYqQ45oEPvWUS9OF_Muzd3UAdd7eO6y4WpRpQJ6JRQ0cOSv8HMPUJmNTH68e5oH7ZBntROhvWIbIWbCg795ZwBxrTSaLCutYBhoRF7xCTcwYx016fJtLn4FtYCljssYms3OpyjnLZH7JA9v1Fq3qxQ8KZxilrLvvst6PglOtj4WrIEWl5UblZ5790z9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی: در پی اصابت مستقیم موشک به پایگاهی در بحرین، ستون‌های دود به آسمان برخاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/akhbarefori/675003" target="_blank">📅 01:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675002">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
منابع عربی: در پی اصابت مستقیم موشک به پایگاهی در بحرین، ستون‌های دود به آسمان برخاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/akhbarefori/675002" target="_blank">📅 01:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675001">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
المسیره: تاسیسات بندر الحدیده هدف تجاوز سعودی قرار گرفت
خبرنگار المسیره در الحدیده:
🔹
عربستان سعودی در تعدادی از حملات تجاوزکارانه خود، یکی از تأسیسات بندر الحدیده را هدف قرار داده است.
🔹
رژيم سعودی مدعی شد که مراکز نظامی انصارالله یمن در استان  الحدیده را هدف قرار داده اما بندر حدیده هدف قرار نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/675001" target="_blank">📅 01:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674999">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9ROAezXp5m2G8qAuZVi_Gsw5YjMgeYDcTKdgdqHEGjSOvVa1VfONFe2seW7WS7cn9gv-e4korA9sNjXYa_nofuJweFbCShZ2u2iSNfE44at6lVn-iuYQQCA4kw1hGJjwky56FCBcNs_Wahp1MObcBCRDkoYgxtjRXQfVV0VwRfKCAnNtZCzU0eULLG9takpyB8bHuyRIXkQ5M4n3i5jnBaCBzI3fewMtbN0Nq6tyEaj68ceqGv44cCZAlO9dAz07fVTX_Al6LKZTwNNfPFLfpaKhTNL56Zwu0flie_alY1PDeQ6mo_RMw_bgpHV0dmJPjpB-Lo9hq59rTpvYNinVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اثر جدید کمال شرف، کاریکاتوریست یمنی در کنایه به عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/akhbarefori/674999" target="_blank">📅 01:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674998">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBNVbBq3-hhbYBik2_PbWSRWabi-IlLrAxwScSRsoGi02tNmH8ACr2THR1suriT4LNjdUVigktLTMh-eV7YD6F4n8WvE22DURJ_ZAgpctmY_CrUCqfcpNwy6te1WjsEq6s1enonS2DpY_kMrr2JlZE9RvcaIgsHV5BNx7VqU-j3yBG2JOUto_EbEXP6bVU8aGqpwyN4I7F3pdf1wlxJH2KYOl9uVjp6hoYQiGbpDS9U5nGUzjJoLVwMRfYJStVpUqRqTV-nHR_gBKY5lFmEhXfKePkUp6m5XYMo6Pe0mnrQ_8Uv2aj_-Jlo8Ha7Aoqe2monsaUUlnkNWuR_sERcbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکذیب پیام منتسب به فرمانده نیروی هوافضای سپاه
🔹
در روزهای اخیر پیام هایی به نقل از سردار سید مجید موسوی، فرمانده نیروی هوافضای سپاه پاسداران انقلاب اسلامی در فضای مجازی انتشار می‌یابند که منابع و منتشر کنندگان این پیام‌ها فاقد اعتبار و جعلی می‌باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/akhbarefori/674998" target="_blank">📅 01:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674996">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD5IUOOClO4OsRI-AdVwOHjrXKaD0GbncaFA8BJiT6ZfgCLTklIw1DAX8bF5nNHEckLKO_3rNIE20eKa-lRhjII5zGFc5yMSCVykLb1qsJ1MLw1lQggYqb80hyTA0SdeoL_mQtE8zFTNrbJcGxdlxb418oHFIrODQKlvVPnLAe4iilu99QiKRmir8V_wBDNQAUlDftBOINIYmTa7zAq6LxSNzwbSEcIMJpOF0_cKvj99lZsJmSU6qQLwcXBsOtgUJeqrl8UPvqHDYlyfQPoceo5lQJ6ePR2jbKSbvRuX6AY-5nvD-2XMlbLw_P2qdJjybq9mQeCBKMdIFjKKrCLxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلند شدن دود از مقر ناوگان پنجم آمریکا در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/674996" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674995">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
عملیات شکارِ شیطان خونخوار و نتانیاهو کودک‌کش
🔹
انیمهٔ جدید از عملیات انتقام علیه وزیر جنگ آمریکا، نتانیاهو و ترامپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/674995" target="_blank">📅 01:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674993">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e200a8d21.mp4?token=q_igR1YDCP2y6KyUD5WKYL6LA8iGoSQR9Wpmh9LioXveNl_0UzYt3QlzzK1j_dn44uoMT3PumZPMOgyvVDBZHRMKbyqa34r13z_KzwcStkC-eiGiY84C4DLsprQR7D3yq7Z0W1KXYtWJ0HjHthkyoBQMUJa8C1TP285Ko2RjIu4cNeBjwUF7w2ff1NvjSNY7FqU2zieO_Jfk9ApmckpvmnmZuyOfIfaRKQyq6NRXycF9LPRgy6FfeSPP3pZvmFaH9nwIV6JZAYraDR7wmGFsgFXRljVLsEk39s7yGfqwEli_S5KEyfz2e1dslAEe0xqFqG2XzV6Rho1mfe0cAa-OBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e200a8d21.mp4?token=q_igR1YDCP2y6KyUD5WKYL6LA8iGoSQR9Wpmh9LioXveNl_0UzYt3QlzzK1j_dn44uoMT3PumZPMOgyvVDBZHRMKbyqa34r13z_KzwcStkC-eiGiY84C4DLsprQR7D3yq7Z0W1KXYtWJ0HjHthkyoBQMUJa8C1TP285Ko2RjIu4cNeBjwUF7w2ff1NvjSNY7FqU2zieO_Jfk9ApmckpvmnmZuyOfIfaRKQyq6NRXycF9LPRgy6FfeSPP3pZvmFaH9nwIV6JZAYraDR7wmGFsgFXRljVLsEk39s7yGfqwEli_S5KEyfz2e1dslAEe0xqFqG2XzV6Rho1mfe0cAa-OBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سامانه پدافند هوایی بحرین در رهگیری موشک‌ها و پهپادهای ایرانی ناکام ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/akhbarefori/674993" target="_blank">📅 01:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674992">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7eda22c1.mp4?token=qrYrcf61BS44nyJcTMKjA6yfQ6dGF1GoKFKHWE1XHSsZ7A4JS7F83bG_tPBPOYXfgAO5mohF9T-Ti8byo552uVrDjw5NnBc92ZauOGonJrZw8FlLgxEilfTkWjch9zz0xTYRBH56d0lU_k8pAunJnGElVmCtqj-0HaFxsUOkUE_DnwK9D05Leom8l_0kL1ccujngALiRznmpuBj4QC366wAMPJXxiPzJPKIBhQrqIevKDLZL9SzCdpe8JsIatToXow6arGtqCY3Y4lryJFfHmiXBsrqtSJ6qR87vXtUWnrI4LvzqD10GgtO1xb88Q69i6wVr-01v0unm5ONXXZayWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7eda22c1.mp4?token=qrYrcf61BS44nyJcTMKjA6yfQ6dGF1GoKFKHWE1XHSsZ7A4JS7F83bG_tPBPOYXfgAO5mohF9T-Ti8byo552uVrDjw5NnBc92ZauOGonJrZw8FlLgxEilfTkWjch9zz0xTYRBH56d0lU_k8pAunJnGElVmCtqj-0HaFxsUOkUE_DnwK9D05Leom8l_0kL1ccujngALiRznmpuBj4QC366wAMPJXxiPzJPKIBhQrqIevKDLZL9SzCdpe8JsIatToXow6arGtqCY3Y4lryJFfHmiXBsrqtSJ6qR87vXtUWnrI4LvzqD10GgtO1xb88Q69i6wVr-01v0unm5ONXXZayWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه انصارالله یمن خطاب به دشمن سعودی ویدیویی به نمایش گذاشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/674992" target="_blank">📅 01:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674980">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t03o8JrbEhQ3uryOFlmlI_RQLWI0rD-6PePEplDtIGo3NybLoQs8vQr5-FLVdmgbqNuRkZqKQvEEhyrJgOT4EWT8nlJgmnyppG8mSJWRlPgh3gwQCDwEtoMhPzP5n0IETJNNSbKMV8gweKTDXTFrV8LmItDGcuzzgl8Aoj375wisyQpXt5g36UtKYkH9yN1ePf8BVdFRa9JozYUb6Rpf2JIBRzwQOG7c3xmx3KvW5sm137d89f2JHEW3eJ5t8KlGv5KW8Um_6Cy4W4AZdO-lVMoefexBSEcqg6xN5tV63NNxXL9Bjnj9xGHa8z-Rfrl2EdvsneqXtVFe2HCJVQHlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXDrn1CttrsfpldFpcGAZbEaljulnwm6S5AoovXrcIedH2uAcdbIvYYfQSo3HZgmyfCubaDcBGdltYDJqjVrULzy_zynZ1_6MEWta1xfIC4AfhY8FPG4EeN5NBPJuOKsul3gTtYUKwz6DbxOvhda98SvIqnrqbOnJz6YWB1lc26e_qc81I_hEcQ5S1qNqsy27j-Hfx_tU1lfTy8KxYX4qVm9ZcUL6ELof5B9fs4d_sOjleR_t3Ey1AcNgaZB-VqayEHQSayBnFI1VUOHdzjrOFqowTF-pePVEOBgVoBHgGMc_Rjyv33sev2Dke-e_yGI1YSCY9muK2MeGBXuKCRcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjxU9o_DddLDiuIk5E8fgjBiUWcxkkjF6IOFLFdcAiVEdPNTl1FCiZ4hTeLgUrE7fvCGhB9l20eofdmRPGJBf_3V1u_cY6w1OjaSEoIiK4yg3SU3IKZBQB14gZBUJoWHSiZWqY11qic0UMs1trjqeny5HaCPFzQe493FWWo8I0pJm974WDPLW4vtsZ4m5mqP6bjvwHKknsQCBwc7SkmVTvGwt9_InVdGH-yNAMsATy-WWnlvHfOJhpmK4ful_bxstvvw3bllHriZn5SfDKe0qNx4Uc1WlVTwoDy3pXHnQ3AifOZAR5Pf9kUjqiKUHJ2sukQEwl1DJrULsQbcHw9WFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTw2Bm7-8d1fFVuVzzdHeq4OWrtx5rnmE4UUwjweBelS3Hl3f8sufMZ7jP8WmwIzLbKLqSjVrDwGLUpRjdsgg1ixNv-YElIDbPc8JOpgNhCvBgUvbWdAohSZF5d8Lip1NPCpSg9cSeS-W-L4HW8hAkrfGrBZrquYUYD8hDkTvoHHx2TlXpEqX9BjUyk7hSJWtaiSqeXzM2EJMsYW0w3ilxBE3-VjVm9YhTvgtmnLjJAxZb-uRlv3-dnufpg8257YEw5DawFdGkJPfD5Rii-okwElPsxXNTZDVYCQpso9EeNmupALx1AWvQrgUAgGxX9K4sS4Rc3onYXo365bSb4mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEEx56NYmDGxHvxdmy1ru9JJXtieY7QQD5n-rDBFe_-kZNqy8rP6IyOnJBpClsKFsN2AwFYU1L2yGunj0YJXNk394Ipm5lOlLOedQjyARX9wUL0vzvS-bpq_aXaLOrFe3eCdDxd-7psIROA1P6C0rpfddM8YfE9zG6VpiS10C83OEpwj_WMNS9MNL1eu6jsbnM0cKQD4M7-AodiZr0c6wzsCZITqVWocYoMbOK5jOfOqvW_va3clGOzVGtbW1HIEHRivyBrbEy-wWA7Ze-AYOQldSJ2iOBlLn9phquPZHafMVfAWa9-eGQ3W3CtAHRFSVWa-n0l9LH2NyNEJ-LUiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lONhsDHbCq_RtkYho00NVb7AMS3Y_oVC4yjjvjUaAbn0s2XeNMZPonHz6FQFsX_-X2hNr6TvYjRakXM0_UbgGZOtWHkWCmiBuacTW4z_xKHLoJZLH9MzToNK7EUTzdhrfYpPDtQ-I8ExZlUwfAPWSO1xU0jJXQC_ltFdUFjjAwEV4rA6X3aM_kx-NWqFbewXjU5RNtnYIOF-chXYBwNvWR-57SAWBjw0FX8vhVykeRZC04XnV7oS28rEmhlMMJ-bslqilYQ4EZvTtFdc4v1MhwCEPwDbm6kavMFb7-CN9vdl4CgNKbEiVN9SqK6s7wp9MYp3VUS1gZMGHAc0duCh_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3UK59O4fwg_YRdf6Hns1RQeCtHo_lirsgkg6AorNnsgCkkpxTFtZitCwgIFj_qcStClEfXroW7j4W0nIXco0ILOi12GzcBUwi3wjHHcKhp012S4OKaODsWz8M4CqxIgYiJqX2-bRImKcCU0cNre8j7bCIWoZzIXTQXW3OyejXve5v9OGx1KPnmrMkitg7tYA6O1VP5pytb_5uzqbUlrAh1SRl5v841GJZFEyIc6nrl8GmU7CMeSUopp5HL-NOdK8jFXk_YslL8qrHSvwsCCk1xKrkJgCsPQQFcOIAMNxgLUbbPlpJjLsF-UaE9En53ZfTUbqvzFjv8UqQvNhvdIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtR-q3e_UPQG_zB7GL7yj3GqPbxbwtA5CJ0ZjlxR-O6JJIQHeTXC6f8n7byGhkX5Iu5DkjTks8ihagpa0ROUxXrchsjdJhMH3ucvAxZGtUS8hBPzU_zeoXeOvkzB1FAgBb1l3hsm51usQAMz4TyRA7XiLLYuK9QzemuuNGT_rYbDFaGoFUPu8n2i9Ue1DaUgwhTcY-XfoD1TgihLI32WiHIWR_5tLW8Mphm6mRxIBxwIEzsIcRiqAq00udSIUOXJ4uXKgs9fesuCANqKfIihc38PNn1dk4DOtKw-8zYcpMSISfs6Pwvzhq6OACCW-xvcwUfm57Y4yT1Lo4B2dvvmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ep68DufjcHXdN0AoOH7QZncQVzPD2VhnSiymvtvmiJq3BxZpns5H6OgJeVMmy83xvJgWBzHvzgafyzxHRujnpIndmsugvqwob5q5jHNTNdhjhD63Aobzo04UySOscQbrTvce-2h_z5DREy6SUkBKdehzTOiR77AoFX5QOudkEMb4CYBNPPO_rghTbKFYWtDELnNYMMhKIqFdZOxC1a8rUCQnaUBw54EgZVKyY57dYKiCH-ZwCktk6IGFJb43nlHO8vf61ctl3RfzuhkDB-kMCj-dnxTRqAB5OOx3qNPcexXS58X9h91tDhHsGglNOgOiFfcNGuNeqsecvj3eFzPS2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nni0DTEUWAfgEmazToZgNLoFBs73aZ16z3Z9dPLVypciDYbFRbo5eGT6279kqziMkLSS6L6KF2KMhTYe-zMuDvhzJHVukF4JXbL9b_ohGsvixYI8t2Dj3u_wYee72ttSMcr8GldLg6XexZhp8oId9zHFxY2nkQGfRlRZqDnATlvYE88QZ2AjOT5i7pg-Uwxc2KyX_43MQTQMqnDpes-OCDcxOkjKKmsJZa7ZZpjsx6Tojz3sf7s36CBnQ70tmCaCllXiDHt2-Qi-fqlbC7C5Y_J8D2sLe-seep5zHCeJDnsXFzj9bIbCQHNToTi5S3bQi2-EKhZu90y6CoEE1jnTuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لامرد؛ شهری که قربانی یک حمله شد اما روایتش جهانی نشد
🔹
پشت آمارها، انسان‌هایی هستند که زندگی‌شان برای همیشه تغییر کرد؛ کودکانی که دیگر به خانه برنگشتند و خانواده‌هایی که داغدار شدند. لامرد یکی از روایت‌های تلخ از آسیب دیدن غیرنظامیان در جنگ است.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/674980" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1bf73fab.mp4?token=ezWZMHQI9PENIht5rkp85WDamQWiswymvUCPZroBkezpSBnGpg7QV3lrk0jRGuh5v3uXvmCeWPyPKPdjnFwmE2Guxi_Ma69Eq3f9BLl0_iSUSab74b2mvYcY5hwXcB08qSkY2wCy1ovPgzjoWY60HxRWR5v6HjHOWXHsdTclSgJZPAncUeYMc7tT3-yhK6J6TzilNQsmZoYt2qiBw4kLzUqYjW768rFhZt-Q8qh2qypuV-uTCLPXsWq9ltCYwRFSKcJERt90DYpW1TckVOWluuGZUXX94fG4GooUgawNSKbm1Suw4MoI-sOTszwm6X1a4S1CaNrYFmeOQ_H7EKqwMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1bf73fab.mp4?token=ezWZMHQI9PENIht5rkp85WDamQWiswymvUCPZroBkezpSBnGpg7QV3lrk0jRGuh5v3uXvmCeWPyPKPdjnFwmE2Guxi_Ma69Eq3f9BLl0_iSUSab74b2mvYcY5hwXcB08qSkY2wCy1ovPgzjoWY60HxRWR5v6HjHOWXHsdTclSgJZPAncUeYMc7tT3-yhK6J6TzilNQsmZoYt2qiBw4kLzUqYjW768rFhZt-Q8qh2qypuV-uTCLPXsWq9ltCYwRFSKcJERt90DYpW1TckVOWluuGZUXX94fG4GooUgawNSKbm1Suw4MoI-sOTszwm6X1a4S1CaNrYFmeOQ_H7EKqwMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک: روزی می‌رسد که پول دیگر ارزشی ندارد!
🔹
با رشد هوش مصنوعی و ربات‌ها، زمانی می‌رسد که تولید کالا و خدمات از نیاز انسان‌ها بیشتر خواهد شد؛ در چنین شرایطی، به باور او نقش پول کم‌رنگ یا حتی بی‌معنا می‌شود، چون هدف اصلی پول یعنی دسترسی به غذا، مسکن، حمل‌ونقل و خدمات، توسط ماشین‌ها تأمین خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/674978" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674974">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3245f5ecd8.mp4?token=aXOUMNlZvPEtAoXLa_PDm0wPOADJQobGF89MPef28-nWJzSbOV748IAsOdMVNlhAS_MTzqKbJUc0pYKoj7EC242IdPXcVAcTe3x7R2x12nk9Dw2ntS3xrHmJmr3l1hEzPwtjMoGJ705ZIgUqQKr_SJ60sqaOtIMZ4Ez6C_0I9B61k45HqlVatGFOFPtrm34Rncaj3XfxEDUsOdAlSRM9RcLYMVKYLmp3pYjxt_aicWIo88ze0-tAuA83xEzDG2He8i3USGYBI5KxPlaTJG9-gfEfCSKO6XwrqWPzPqT6FsoiPoDLQDpZD928DXimpfWHY5HQNd5p9cl_y8TO2ccyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3245f5ecd8.mp4?token=aXOUMNlZvPEtAoXLa_PDm0wPOADJQobGF89MPef28-nWJzSbOV748IAsOdMVNlhAS_MTzqKbJUc0pYKoj7EC242IdPXcVAcTe3x7R2x12nk9Dw2ntS3xrHmJmr3l1hEzPwtjMoGJ705ZIgUqQKr_SJ60sqaOtIMZ4Ez6C_0I9B61k45HqlVatGFOFPtrm34Rncaj3XfxEDUsOdAlSRM9RcLYMVKYLmp3pYjxt_aicWIo88ze0-tAuA83xEzDG2He8i3USGYBI5KxPlaTJG9-gfEfCSKO6XwrqWPzPqT6FsoiPoDLQDpZD928DXimpfWHY5HQNd5p9cl_y8TO2ccyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خوک زرد: ایران برای بازسازی خود به ۲۵ سال زمان نیاز دارد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/akhbarefori/674974" target="_blank">📅 00:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674973">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da21f30e2.mp4?token=QRz3PZO70lkDfnnw7BkQ34-H8ZxePho_bjhugQOK9w-EJDFr7nP4Uh6OVedxFfhFGkzZdPdrxh7PPNDOLqSZlQCH1Z8w5VVi4FTBw9vqGhwfF9Z_hTDkYWLL84d_rsgx0nGbVqr_AfOBAQIwOlKAer4fpNLb2OataJlJOE63eNeCC9Dcirqul-I47ys-W70fVaNq0Und4rkFm4WK-yfiDgrpZNCBQUCeLK_yzGuvyRiTT9Ir-4FFr9gi5OfIdGxYnj7wZOfz2X9QXxWBaB1nvGIgU0OXuuk8GiOFgcr9LFB2J7Fo6aDlRUwzyxemc_wxnq-gFIoLxLwYyqpO1FKPZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da21f30e2.mp4?token=QRz3PZO70lkDfnnw7BkQ34-H8ZxePho_bjhugQOK9w-EJDFr7nP4Uh6OVedxFfhFGkzZdPdrxh7PPNDOLqSZlQCH1Z8w5VVi4FTBw9vqGhwfF9Z_hTDkYWLL84d_rsgx0nGbVqr_AfOBAQIwOlKAer4fpNLb2OataJlJOE63eNeCC9Dcirqul-I47ys-W70fVaNq0Und4rkFm4WK-yfiDgrpZNCBQUCeLK_yzGuvyRiTT9Ir-4FFr9gi5OfIdGxYnj7wZOfz2X9QXxWBaB1nvGIgU0OXuuk8GiOFgcr9LFB2J7Fo6aDlRUwzyxemc_wxnq-gFIoLxLwYyqpO1FKPZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت کادر درمان هلال احمر از دق کردنِ کودک سه‌ساله‌ای که با چشمان خود شهادت مادر و برادرانش را در جنگ رمضان دیده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/674973" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674972">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c795d247e.mp4?token=bVBHXjQpLoZgxSEBsIO9U7qOnHEqxNm6qKs04C0gVMXDUo5nry3n_jkGgyDANsHVZrAkGII8gIr3ehprNINi94fKVLThjsJF5oZlgjX9WGOtXt47Xd1StVZwTOYNpJmWq2bd95-xMhFEIwjEL6_y2TGRAMmOB6ERmRnFhE4YoGAQDKHsvMjLTo0A-8956IvzrK3UTbhCGATmpH3YuT-UnnZE2q5vBwiHQKlKi65eocfJ48fQ6mnTH0-9j2DBZeMDrHCwMtuHxblgdYybQKGD04gnC6_LyENaF81mznjhEFFvkuUsC1g2ry-Wxd2btWAkDScSG7bT1e-R3U4NcgaK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c795d247e.mp4?token=bVBHXjQpLoZgxSEBsIO9U7qOnHEqxNm6qKs04C0gVMXDUo5nry3n_jkGgyDANsHVZrAkGII8gIr3ehprNINi94fKVLThjsJF5oZlgjX9WGOtXt47Xd1StVZwTOYNpJmWq2bd95-xMhFEIwjEL6_y2TGRAMmOB6ERmRnFhE4YoGAQDKHsvMjLTo0A-8956IvzrK3UTbhCGATmpH3YuT-UnnZE2q5vBwiHQKlKi65eocfJ48fQ6mnTH0-9j2DBZeMDrHCwMtuHxblgdYybQKGD04gnC6_LyENaF81mznjhEFFvkuUsC1g2ry-Wxd2btWAkDScSG7bT1e-R3U4NcgaK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/akhbarefori/674972" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674971">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
فشار آمریکا به کردستان عراق برای ورود به جنگ با ایران
🔹
رسانه‌ها از فشار واشنگتن بر مقام‌های اقلیم کردستان برای تقابل با ایران خبر داده‌اند.
🔹
بر اساس این گزارش، آمریکا تهدید کرده در صورت همکاری نکردن، وضعیت خودمختاری اقلیم را تغییر می‌دهد؛ همزمان برخی گروهک‌های تجزیه‌طلب خواستار حمایت تسلیحاتی شده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/akhbarefori/674971" target="_blank">📅 00:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674969">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
اولین واکنش انصارالله به تجاوز سعودی به بندر الحدیده یمن  حزام الاسد، عضو جنبش  انصارالله در واکنش به تجاوزات عربستان به بندر الحدیده یمن تاکید کرد:
🔹
بندر در برابر بندر، فرودگاه در برابر فرودگاه، هر تشدید تنش با تشدید تنش بیشتر روبرو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/akhbarefori/674969" target="_blank">📅 00:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1oGL_K4j_M9RDUopAJ1BJNbR0RiPtZQRAQ05g8MMtPuWA4_hsQlK65QzFVIJEWUCU2ZrNwSOK0q25jAYvOm8xBDPrxOadNtwasOYEc33F20FyWcOtWa1wURn23uWKmLoVOYQ7ZXD3RHErTHJWs0as_0zgxR2xxr7rWIBsBOzFfcZClKV6AYnoE0kX5qjfGx8XOeJis1kCDVrLO9r8UOcWJ6axGjH7m3ubq0ssOerg_YZ_qy_sAVyQV2FcDaExlY5RYVYAVYOWOQ_o2mijoGDFxIkgG6r2-fQ2Y3U9c7QN2j4Fqlbt0WjIp6z14VG4V07lE2WYxVMTdNc-cGNNV9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین واکنش انصارالله به تجاوز سعودی به بندر الحدیده یمن
حزام الاسد، عضو جنبش  انصارالله در واکنش به تجاوزات عربستان به بندر الحدیده یمن تاکید کرد:
🔹
بندر در برابر بندر، فرودگاه در برابر فرودگاه، هر تشدید تنش با تشدید تنش بیشتر روبرو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/akhbarefori/674967" target="_blank">📅 00:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShbaacsekBTJSn7OgrCWfZO1wfOmyyz55_1txvhFw3HzWWm4uma0zMHT9bSKF_V9I18NAkGsLWEx_ITfLTMD927OuvrkKbshz3EjDId1eQjrABP9rD1IBhNXk6lAjAy4pVKDF3F9b-_d59NOGY1XCvCxUXmzb0vpNvSyX8xeiQU3ywc2GfMQ-Gs2XMp97tOT7oiDnKpY1mcIdUxqnrqTvyKecAXkWjBBdYdyyw1UYXL2v41JwNMc5bU1o7oFEHBoNbloX6zCI_6I-FBYyAzQJwMMVjdcU5nFPcLwLk_J8OYpbPJEMJL4V7vkIsUP7cEVy7UJm6YD3Q_Cr2LVtkoKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اثرگذاری در کمپین های سازمان ها  معمولا مهمترین عامل برای موفق بودن کمپین حساب میشود
ایا هر تبلیغاتی و  یا اطلاع رسانی ، تاثیر گذار خواهد بود ؟
استفاده هدفمند و هوشمندانه از ابزار هایی که در اختیار دارید و یا میتوانید استفاده کنید مهم ترین عامل اثر گذاری خواهد بود
مشاوره تخصصی و طراحی کمپین های تبلیغاتی و خبری با ما در ارتباط باشید
👇
@marketing_mn
برای رسید به اثر گذاری ، ما در کنارتون هستیم در اژانس دیجیتال کست:
https://t.me/+fZbPfI0dd-41ZWNk</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/akhbarefori/674965" target="_blank">📅 00:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674964">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKV_BEI2CKY73ZEnU_kVQjrRiRgJn0XA06bMBTzbIqYQXwRH6VocbTldvRpjXiZE0YaNnOGjSfXkT8Xuq5rKokkgvd0dpoW5Jx-KAA3zgF5mHDhP4J1YTcahzlaOg2qdsfcmu_6xQNAEo0qy2LG_-xwEC7xzbPMasjZf-L0ykRtTr-6MM-0iVCqIahal8ROd1wvBKULpPG_d6JrVVI-780E1vZMehSloLxOnlTCQVRgO1P3QmP4OX8zr4frh_mMlckwxJItmRyQ3EtedyFyTLyW2AapwVlPEAIGf-658PU3_qYY4t60Qid4GYBq5QBcNj2onNKBPBlMbhGXyVXwLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/674964" target="_blank">📅 00:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674962">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
راز آخرین‌جلسه شمخانی فاش شد
👇
khabarfoori.com/fa/tiny/news-3232741
🔹
امروز کدام شهرهای ایران هدف حمله قرار گرفت؟ + جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3232597
🔹
جنجال بازیگر فیلم‌های مستهجن پس از فینال جام جهانی
👇
khabarfoori.com/fa/tiny/news-3232778
🔹
رایزنی‌های فشرده برای آتش‌بس ۱۰ روزه | ایران چراغ سبز نشان داد؟
👇
khabarfoori.com/fa/tiny/news-3232805
🔹
اختلاف پزشکیان و جبلی بالا گرفت | ماجرای توبیخ رییس صداوسیما چه بود؟
👇
khabarfoori.com/fa/tiny/news-3232771
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/674962" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674960">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0tRzTHH_ZdTOnvqPcIz-UkzNUqaK82POG-uD9pbZu7xKKshUay-KOUTBiMavA42h5kWQY4ahzwhD3M95AIK4keojjq_Vkf2ONiMHdTfPZ9wx4xYUbiPhXq-4vsnMW7pWS5K4s7apxITgrDs0aodVrUDdvYEAjIlCl4Qn4nFMaWQAyISeEOuAHMyhB4nheS8PgvE40CPZ_JtlTZCoh321As2BkV9RT81iS9fDa1pT_DvqSoCOcVN2dp8gmFkbWYExsDMlvJnBE7Ipx1oab3ALjx7rX4N4Kt13vUf0f9EtPFGlhwA8SRnBC_mpr65uxveqhsaYrvuQgLC6qjA32-0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: کارشناسان هشدار می‌دهند که فشار اقتصادی واقعی ناشی از جنگ ایران در شرف وقوع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/674960" target="_blank">📅 23:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674958">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f63abf7f.mp4?token=WV3ANhLnbcZ9YOrsdnBCbifsEjKjVEn4ZD8ZaoJB4nnP0SIU1oRmw2Lk0Ivah3xJ0RJDmLIYJbrLO1xbjePYM3XrpSWJL0UtkAAKFJRWQubbx3um6xsaEs08qrw3UgNHfxzwwEYkzYpWjNpThn_giqVCx79foMiIzy44Y7a-A4O_ENuosJOdbpxUk8vxkcJPa6YmknLfXtxtaLGqar1e7OD84B_vUACLCwXz5EnhDGIpZ61Nl29QUzzNqglvXAJALMQzao6djwscPBkQ_tZCK5g-fMbrpY6idJb05QqTw9zqllqsKZx0fbaHA5V6DWccjSqeYxJM7Pu1jGBkc3Kb9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f63abf7f.mp4?token=WV3ANhLnbcZ9YOrsdnBCbifsEjKjVEn4ZD8ZaoJB4nnP0SIU1oRmw2Lk0Ivah3xJ0RJDmLIYJbrLO1xbjePYM3XrpSWJL0UtkAAKFJRWQubbx3um6xsaEs08qrw3UgNHfxzwwEYkzYpWjNpThn_giqVCx79foMiIzy44Y7a-A4O_ENuosJOdbpxUk8vxkcJPa6YmknLfXtxtaLGqar1e7OD84B_vUACLCwXz5EnhDGIpZ61Nl29QUzzNqglvXAJALMQzao6djwscPBkQ_tZCK5g-fMbrpY6idJb05QqTw9zqllqsKZx0fbaHA5V6DWccjSqeYxJM7Pu1jGBkc3Kb9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هـــــــر جا کـه هســــتی</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/674958" target="_blank">📅 23:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674956">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a642cea0.mp4?token=R9CSuqUUhOUdofK_jXO1RaA49F4o9Y9Ly8weUKg_Q15FZQoUpqK4Nxm73N3byfV6P8oO5N2DbQHnjiH-vfKzQGJ0cqOL4bElkEEDDT81my1dia8hlqUmIr4wk5JcbKHba37nBoOhGYmR4nnF5daQQrh37SJFmvGcijoWEgzm5RSqwpw6fW5LBhPfVm5_ESBR8mXFBMApO_ZZqOsXvLcZ66JEOHPV2I2SpduBqyV_jPpTFuBe3SM9RGcINoKzCg35SYRwmMSrOcCargjzzyNg-t3BRDNWhEWB-nnMic2K2UY-8oqIZ4fL79LAYsQ9kGZql9bEHTGZHeH5SauMKTzPIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a642cea0.mp4?token=R9CSuqUUhOUdofK_jXO1RaA49F4o9Y9Ly8weUKg_Q15FZQoUpqK4Nxm73N3byfV6P8oO5N2DbQHnjiH-vfKzQGJ0cqOL4bElkEEDDT81my1dia8hlqUmIr4wk5JcbKHba37nBoOhGYmR4nnF5daQQrh37SJFmvGcijoWEgzm5RSqwpw6fW5LBhPfVm5_ESBR8mXFBMApO_ZZqOsXvLcZ66JEOHPV2I2SpduBqyV_jPpTFuBe3SM9RGcINoKzCg35SYRwmMSrOcCargjzzyNg-t3BRDNWhEWB-nnMic2K2UY-8oqIZ4fL79LAYsQ9kGZql9bEHTGZHeH5SauMKTzPIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تقابل ایران و آمریکا در روزهای آخر عمر آیت الله حائری شیرازی رحمة الله..</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/674956" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674954">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URmsXRXN2cmFGO-5QX44q6BsjhjE-2XsDJyxVP_bqac_3IiZiyGWNFKCIAO9FaucQYn46lsfS-d37iOSqDd5vc-1fVLXQM_AqIGvcP_cKfdKwWSwdX0SU3U34G53dFRyca8Vk57PjgOkEugG2E_J7Wzr84ioEYLoQbVJ_tATs21ilNaJ7qEIYZ1-8TVcT1Xcrk82r8D727h3hsiPD1V6tZCieValrk9y5NhhdjqR63igKtMwpVrvmPZeR8Y3Hpuh6tNKA1iR0Lm0OTfsecu4YS9L42sBj_QNgomD82_Bog6TWFfFDWp96L_90UDwRu7EaxqVLPztNQQ2gG6_OEtxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4d128eee.mp4?token=h2Tv0N_jx3mDE-XFEvCPSBRLZF5cA5veSNKUiruCrqf8E9nK0DV4xNvhRhGISae2NzEfkuViPipb4xF4-iVGUFoVk2noiwEFPnRnnFoexAQNd_NSLmPHEqQLEtc8yhS88CjuYoVo_968ZxqQlpz3yea7hmVGn2DfWPlYD9syVJR84xAkeF-odOZhf0nI3SKcYAamO72okQyQUsMwD5SkNrqcRA6WccKfNTppE_uDh2-RIa6BaEzTAFSABF23z_l649NDimpRDSxcvXRTimE8oeP7A73l8Tyw7xVkdpj4DD-4pra36JJQdPvMeMu7-hrXy2XBY_bJQMFf2mtZU_IUtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4d128eee.mp4?token=h2Tv0N_jx3mDE-XFEvCPSBRLZF5cA5veSNKUiruCrqf8E9nK0DV4xNvhRhGISae2NzEfkuViPipb4xF4-iVGUFoVk2noiwEFPnRnnFoexAQNd_NSLmPHEqQLEtc8yhS88CjuYoVo_968ZxqQlpz3yea7hmVGn2DfWPlYD9syVJR84xAkeF-odOZhf0nI3SKcYAamO72okQyQUsMwD5SkNrqcRA6WccKfNTppE_uDh2-RIa6BaEzTAFSABF23z_l649NDimpRDSxcvXRTimE8oeP7A73l8Tyw7xVkdpj4DD-4pra36JJQdPvMeMu7-hrXy2XBY_bJQMFf2mtZU_IUtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشرشده از بندر حدیده در غرب یمن، زبانه کشیدن شعله‌های آتش را در این بندر پس از حمله عربستان نشان می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/674954" target="_blank">📅 23:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSoMgPU6CStF_axzhbcmhiN80hRFMG4ctnSj9vqGaEj58mFYrIgM2T3MCMvVyJu1gQT4uJYiYuAJX4sw1Y3XMMc28Ql2vpDW4WVm_pF97cOrxaTjPQWyohBuHYaMpMGwhXpYQyImRZieaKb4rF6kxb_pZ67bUMQAx2zPEEvDrM5fmwEgRMpqPUvxN2lxsiY7kT4UO2HdlMHMhecB7KCmsQhWW9uj7_8SdSoE4sIstIgoGPjb6Sv0VPzeYEErEwdDRIoPbytrSb2tV5hBDvYniXgqJo-DBSlthLZE6dWsHDUhNeP4ffGNfMpw14vX1Q_Yo_mHW6YSoQWiBpeV0HcNoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خنده یتیم شد
🔹
هشتصدوهجدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/674953" target="_blank">📅 23:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2oozt6LJvSXI0MearO5HKB_HzG4PT-fPStXxoKsvIDzfIXJWLX9yQ38mspy9qAlZENjPnT1INOtyJEkY1JTuQwTsBfESfuQvKwqyQi2rSkNfORorZtSK8Qv-XiB8wkjnzWuMG4o1yEiOwLP_KeqbVMrDCx05s7wjPekqAknh5jOssaBjlqWSqb-Yg7pc6AYFf4CqdfI3Sx4Tbzuz6mzDrjlIXOZCAI2XAhGvG3rLYsq-gJx8tSi0k9bj8Ow_60Fuo3iWk7rdXkDAZE3jChL4hGcrEMrjh4K5cPi8korbENgQZweyhImMmU5TCcIcqcvDGWMbRs7jagr262V8svCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/674952" target="_blank">📅 23:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674950">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7460a8d557.mp4?token=AlCKGT_cteERrE52SrOhg8TEUK6B5wx4ortAGPiyNe2H9pyvGIZOl0tZEN6reS5IscL1nlm8V6HiSpv7s2agN3YNl82IcAN2EnFau2frquwbnG7EmgZTcDjhdc4-UkQkjVkvl01q1C2fTx1kB_WmSKE3jU3utIOsfFTogyI6O3kulc4m6uUB-F-J-kPbIlJEoT5SSlthJ2GKitovZeB_g2WhaeCScEruosFAhGUIoVSH6IAp9wvYRvnhw_s2ad2u8TkeVU0Jv-_eEBl_4TpC_x_1C9in94waDaIyN-ppsmZVqysiMuJLLseY_HkVMUjyiQn34FS6jNuyTOsljFoWrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7460a8d557.mp4?token=AlCKGT_cteERrE52SrOhg8TEUK6B5wx4ortAGPiyNe2H9pyvGIZOl0tZEN6reS5IscL1nlm8V6HiSpv7s2agN3YNl82IcAN2EnFau2frquwbnG7EmgZTcDjhdc4-UkQkjVkvl01q1C2fTx1kB_WmSKE3jU3utIOsfFTogyI6O3kulc4m6uUB-F-J-kPbIlJEoT5SSlthJ2GKitovZeB_g2WhaeCScEruosFAhGUIoVSH6IAp9wvYRvnhw_s2ad2u8TkeVU0Jv-_eEBl_4TpC_x_1C9in94waDaIyN-ppsmZVqysiMuJLLseY_HkVMUjyiQn34FS6jNuyTOsljFoWrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد مدعی شد: ما در حال حاضر در حال مذاکره با ایران هستیم و ممکن است به نقطه‌ای نرسیم که حمله‌ای بزرگ ضروری باشد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/674950" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674948">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNfzxx8Eksfp3REUTJoADiAPYoRXTuTLRsw_sM8trfm9sMD9MJaAgl3emmlqeHHfJQ_MAiqcnfMStskF4pCYOYE8dHpPfu9aDxeqiidzNMRS2mPHkvH6afD0me8NcOJRbgk5C3uagv08gJn4EQ6cXEcSsJU6LlqqKWVyWxPBGkP83x9dBQ0lOniCzOcJjDeDmypfHbeLz1ohd9H4DoOxg64H6J_qPpxE986XyioOasiFHIBp6_431SE2s7AZiYD90h8yRgz2JBJutA6B4qVxsI4UlKZnOa-fwxeCxsO483YEcD4ykewdqK5G8NI7RfwwkMQ-oUjCnMgQ-mAgJCCyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/akhbarefori/674948" target="_blank">📅 23:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674947">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند
/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/674947" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRhYXR1pM1Qbh-qJGG5MKe2A_gFOIikXlqdnyY2MNGqCPtJnqoI2E7q2gDyjWccRDEvkvaxOlV2SPZmOUcly4V_lNi_HcPONJVP3BNG1TdO3WWmCf_LxxnL3x3z6tSK4dsUK6hH5ZmAjKio2mgP22RykLokd3ap-oJTEigvE9h1nVZYaFnb8bKTzNgIo9mffsaIFWS1dqaUsMzQJUB5syo9Y8MXkc6Teh_2L1G_bN2LnLYhAFlegAG860x_85xXQheslUzXFyYfSeHPUMR_0GwZnJXkstrfweJ8LTYRlvAVl4WkI349s-tKhPJ3ThNAbUcrxpnnGGjP3lh_GbZFGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشریه تایم: پایگاه‌های نظامی آمریکا در نتیجه جنگ ایران بین ۴ تا ۹ میلیارد دلار خسارت دیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/akhbarefori/674946" target="_blank">📅 23:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
خوک زرد: هنوز درباره حمله به ایران تصمیم نهایی نگرفته‌ام؛ مذاکره در جریان است
🔹
شی و پوتین به من گفتند مشارکت نمی‌کنند و به آنها اعتماد دارم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/674945" target="_blank">📅 23:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674942">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4507e042.mp4?token=EabzO5CrYp7T2sv10T9fqvMNWMTgQgIDTetvzOZprJkOSBf-T3C8dpnTPVjDN081U5S791_bl1PWUszl1HDNP8RuMKwJz0rkKJNQxIpwz1IGSJc3U8rECTgTu-uJ8VVaBJ3wJW-2cYsC_rXcJOnJHX9lThIjJfsd9XoJhI6nGIR-Km1kV_T56H4azYQOjWL6rUIRmqMNDfqHF4FdX09x0WLgOGQYtuaCh4S0D06YmlyhMsw4QOvoDJM-MjysrkjNRZORf7jNH_21WCSgPsyU08fEc9tS7153fRRHnhabD3pVUc4c17UHMX2GBol0J3ZBhgCPZBFigFPWjl-NAYd1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4507e042.mp4?token=EabzO5CrYp7T2sv10T9fqvMNWMTgQgIDTetvzOZprJkOSBf-T3C8dpnTPVjDN081U5S791_bl1PWUszl1HDNP8RuMKwJz0rkKJNQxIpwz1IGSJc3U8rECTgTu-uJ8VVaBJ3wJW-2cYsC_rXcJOnJHX9lThIjJfsd9XoJhI6nGIR-Km1kV_T56H4azYQOjWL6rUIRmqMNDfqHF4FdX09x0WLgOGQYtuaCh4S0D06YmlyhMsw4QOvoDJM-MjysrkjNRZORf7jNH_21WCSgPsyU08fEc9tS7153fRRHnhabD3pVUc4c17UHMX2GBol0J3ZBhgCPZBFigFPWjl-NAYd1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طفره خوک زرد از پاسخ دادن به پرسش خبرنگار نیویورک تایمز درباره ایران
خبرنگار به ترامپ:
🔹
شما از بمباران نیروگاه‌های غیرنظامی و پل‌ها صحبت می‌کنید. بسیاری در جهان متمدن آن را جنایت جنگی محسوب می‌کنند. شما هم همین نظر را دارید؟
🔹
ترامپ: به آن سؤال پاسخ نمی‌دهم. شما از کدام رسانه هستید؟
🔹
خبرنگار پاسخ داد: نیویورک تایمز.
🔹
ترامپ: حدس زدم. نیویورک تایمز شکست‌خورده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/674942" target="_blank">📅 23:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674941">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3427ceff0.mp4?token=ohtsKInPhrHhGXcQLwjd9vcgmky-vP3hl-2A0ySfbql9ScBNn7bn-LB5liCxtq9fmd5RtA5x98_w8GxrSHW67eB1gAsM3i2ricQgjyktr2EoEkRSYPPThFrfk1C-JpF9ogIdSkkaGlRnSr081YlQCF8jJUwk-siy1hfKy_QaodFLFw8j5hAwj5l3ZbK8pK58TJRU6T5SZV200TlYELHcmkaRlWgSUo9Ur8BIeoNLtGGdPNCyoLWnUerw8IhdPSkzNaqmuwhw_OuX06VK_ZSBzJeey4JaBGZh4xvT_Z5RphhSW0yRPLl4XOXZhY8Ix0VRS5GKbYf_8DD0VfoOYnyypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3427ceff0.mp4?token=ohtsKInPhrHhGXcQLwjd9vcgmky-vP3hl-2A0ySfbql9ScBNn7bn-LB5liCxtq9fmd5RtA5x98_w8GxrSHW67eB1gAsM3i2ricQgjyktr2EoEkRSYPPThFrfk1C-JpF9ogIdSkkaGlRnSr081YlQCF8jJUwk-siy1hfKy_QaodFLFw8j5hAwj5l3ZbK8pK58TJRU6T5SZV200TlYELHcmkaRlWgSUo9Ur8BIeoNLtGGdPNCyoLWnUerw8IhdPSkzNaqmuwhw_OuX06VK_ZSBzJeey4JaBGZh4xvT_Z5RphhSW0yRPLl4XOXZhY8Ix0VRS5GKbYf_8DD0VfoOYnyypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سی‌ان‌ان: کمتر از ۲۴ ساعت پس از امضای توافق همکاری هسته‌ای غیرنظامی میان آمریکا و عربستان سعودی، دونالد ترامپ،  عملاً این توافق را با اعلام این شرط به حالت تعلیق درآورد که تنها در صورتی پیش خواهد رفت که عربستان به پیمان ابراهیم بپیوندد و با اسرائیل روابط…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/674941" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674940">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghreR_N5pXJl9dmw_bN4YBKWnrwImIuOuJldAV3CXkL_m0Kwp5xce2O5IBlW-dsNxjzCKc7t3FPQvwo0B19_3pGzk81mzaUrlfim7I2Kl6wPzuBJhO6Z2vm8aqouI-Ykd5O7K6NP3XxkaYk_mRMFNqt9XIGE3fhhj39bDFQVWuKcEvBfqVOAxTgxgRIuMaZukxZUJCnUUCY75WzAmZGXzPhZ9xxhqOL2BXU867LKtJhL6g6KcgQp_csizUxDuRdmZRaOExxkFulZ0sc6uPCt7B5LSFp_dH22aS8KfuZ270OVtWNGN0ZjvSWw_6WbQErB8JyMAa8HX_9dwqqsX1rxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برسد به دست زائران اربعین
🏴
🔹
امسال هم با بسته‌های ویژه رومینگ اربعین همراه شماییم؛ از بسته ۱ گیگی ۳۰۰ هزار تومانی تا بسته ۵ گیگابایتی ۱۴ روزه و بسته‌های ترکیبی شامل اینترنت، مکالمه و پیامک، تا در طول سفر با خیال راحت متصل بمانید.
🔹
همچنین می‌توانید در آخرین نسخه اپلیکیشن «همراه من» به خدمات جامع دیجیتال اربعین دسترسی داشته باشید؛ از خرید ارز سفر و استعلام گذرنامه گرفته تا مشاوره آنلاین پزشکی، چک‌لیست وسایل و راهنمای سفر.
📲
روش خرید بسته‌های رومینگ ویژه اربعین:
🔹
کد دستوری: ستاره ۱ ستاره ۴۰ مربع
🔹
اپلیکیشن همراه من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/akhbarefori/674940" target="_blank">📅 23:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674938">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cd13bbff.mp4?token=SufpvLLdYU0WhyrwOXU1Cu6p0Ng5ZPUhZwUdpuC1gqSsfUAV7JC0FIvaeufUd7LL2RfqZPK333GGdKRqT3SUSG_XAyUJs5QWVXB2ONDbjRBgSizCfuvnH-a4cJODNdXeIVyLcPta7PUuU54vznHrnjHlIeSgFCGfI72UpMOsqTQ8yKAV0KeXa0sYN_AvoB3Z3WVdprNLrptnefNQVS4gXgGSP4RlPzuZa0ZhrTLI54iWXZEkImiBaW6wT1XT4z2mYjdzD8FipyIuFJVFhXL7ARnsB3jA8rF8SdNcsgAjrEeH1w-rD0wYrR1ikgZcT8j_pqQSyXLD4reO3kwVIQ1xZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cd13bbff.mp4?token=SufpvLLdYU0WhyrwOXU1Cu6p0Ng5ZPUhZwUdpuC1gqSsfUAV7JC0FIvaeufUd7LL2RfqZPK333GGdKRqT3SUSG_XAyUJs5QWVXB2ONDbjRBgSizCfuvnH-a4cJODNdXeIVyLcPta7PUuU54vznHrnjHlIeSgFCGfI72UpMOsqTQ8yKAV0KeXa0sYN_AvoB3Z3WVdprNLrptnefNQVS4gXgGSP4RlPzuZa0ZhrTLI54iWXZEkImiBaW6wT1XT4z2mYjdzD8FipyIuFJVFhXL7ARnsB3jA8rF8SdNcsgAjrEeH1w-rD0wYrR1ikgZcT8j_pqQSyXLD4reO3kwVIQ1xZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاج قاسم سلیمانی: اگر آمریکا جنگی علیه ما شروع کنه نه تنها تنگه هرمز ارث پدری ماست بلکه حتی ما در راستای دفاع از ملت و کشورمون به دریای سرخ و مدیترانه و آتلانتیک و... هم فکر کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/674938" target="_blank">📅 22:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674937">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
جهش تاریخی صندوق ذخیره فرهنگیان در ۲۰ ماه گذشته
🔹
تسنیم: حد فاصل آبان ۱۴۰۳ تا تیرماه ۱۴۰۵ اقدامات ویژه‌ای در مدیریت «علی صادقی» در صندوق ذخیره فرهنگیان رخ داد.
🔹
تشکیل و فعال‌سازی کمیته‌های تخصصی مانند کمیته سرمایه‌گذاری، کمیته ریسک، کمیته حسابرسی، کمیته انتصابات و جبران خدمات، کمیته عالی ارزش مالکانه، کمیته رفاه و منزلت فرهنگیان، کمیته مسئولیت اجتماعی، کمیته بحران و سلامت کار و راه‌اندازی یا توسعه سامانه‌هایی چون، سامانه جامع اعضا، سامانه برنامه و بودجه، سامانه ارزیابی عملکرد، سامانه قراردادها، سامانه دعاوی، سامانه املاک، سامانه حسابداری، سامانه معاملات.
🔹
بر اساس صورت‌های مالی منتهی به ۳۱ شهریور ۱۴۰۴ دارایی تلفیقی صندوق ذخیره فرهنگیان به ۱۴۴ هزار میلیارد تومان رسیده و درآمد تلفیقی به ۵۵,۴۶۰ میلیارد تومان رسیده است؛ پیش بینی می‌شود دارایی درآمد تلفیقی صندوق در صورت‌های مالی شهریور ۱۴۰۵، رشدی بیش از ۷۰٪ را تجربه کند.
🔹
سود ایجاد شده برای اعضا معادل ۱۹۵ درصد آورده گزارش شده که رکوردی بی نظیر در تاریخ صندوق است.
🔹
حدود ۶۰ درصد درآمد صندوق ذخیره، ارزی اعلام شده که با توجه به نوسانات ارز در کشور، کاملا به نفع فرهنگیان است. میزان تعیین تکلیف و پیشرفت پروژه‌های نیمه‌تمام در ۲۰ ماه گذشته خیره کننده بوده به عنوان مثال پروژه سبلان۲ (بزرگترین مجموعه متانول‌سازی کشور) ۵۰٪ در یکسال اخیر پیشرفت داشته است.
🔹
هتل جنت اصفهان در این مدت افتتاح شده، پروژه هتل قطب مجددا به راه افتاده، پروژه پل سد گلورد افتتاح گردید و همچنین نیروگاه ۱۰ مگاواتی نیز به اتمام رسید.
🔹
یکی از نقاط مثبت ۲۰ ماه گذشته، بازگشت ۱۵ هزار میلیارد تومان به صندوق ذخیره فرهنگیان بابت پیگیری پرونده‌های حقوقی بوده است که در سابقه صندوق و همچنین بنگاه‌های بزرگ کشور، بی‌نظیر است‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/akhbarefori/674937" target="_blank">📅 22:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674933">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4498bf9a7a.mp4?token=mXfIunJPiYLkvSgtOW3N5mhfrsF7JdcUBrH9ktUFc42aDlx-AwwFOfjZgrZyw7fvm-EXlcsLQAM-iWu18_GahW1ikqBhn05tClUL2w9THvkLsL0rU6hdSGiKIown20EzjAmgeqKkEhNCfNgxymLeoi3jIrqxmMj7TzAVeID4Aqelh2b1cOMlD9pF4Nw9gBPDe8P8VLkqy7XhKr-v3NcmzUnUChnV9gI1Rlf_7rwKZHDSC-zRHgt74vR4gmZNde5vpN2q0AnCE6SePBBmZrZfxZoT2ACgzqdwBFNfYNskCwwK_Qp1BkOxPGKMzIhQXE7a88KB0dQIm68WmfMTTkMieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4498bf9a7a.mp4?token=mXfIunJPiYLkvSgtOW3N5mhfrsF7JdcUBrH9ktUFc42aDlx-AwwFOfjZgrZyw7fvm-EXlcsLQAM-iWu18_GahW1ikqBhn05tClUL2w9THvkLsL0rU6hdSGiKIown20EzjAmgeqKkEhNCfNgxymLeoi3jIrqxmMj7TzAVeID4Aqelh2b1cOMlD9pF4Nw9gBPDe8P8VLkqy7XhKr-v3NcmzUnUChnV9gI1Rlf_7rwKZHDSC-zRHgt74vR4gmZNde5vpN2q0AnCE6SePBBmZrZfxZoT2ACgzqdwBFNfYNskCwwK_Qp1BkOxPGKMzIhQXE7a88KB0dQIm68WmfMTTkMieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار عظیم در یک واحد صنعتی بزرگ در رتندون در انگلیس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/akhbarefori/674933" target="_blank">📅 22:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2SAUr_59v9VDoxUeOZ80g2i4nR8_fa-lxv1nvxWdKNmlRbW3aHXK1_4ANY51B6iWh5QsyCMnivOnCIB2sAw7y3xGFUdJtjvEkAXA6gP9UEYKEkv5t0ufzA9yWsgF7TJbgkuSeAUDw0uUvKtie2DfTmc-q53MP6eBy4a1wDHPztDsUbFqrQ1qF0-3fdzZcy3Sv0oZsAW5S8aghmQOeqazG6OsL3FRPBUYoGpOD_5NMv-vwj20wu6FZ6dTPnMiRkHcWR4fAjAPx4asdDZyA4mzgTLIvD21fs9SmTdMm3iE9qyRreOrvHAcQPwK5lCGPskYtaoxj6e6DM9HVXk1ampzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZw7qgXkl3Occhh2hvnBsUGx8V1B0o3Th96wMsJo878a8CUqz3ZPvHrsG9ssjb3kjFeqiU5p7lA6gQnItIN_n_QxjLYbV03urnFoX9OZ2D3w9ExX8X3jmv1PT1kqwxjijUXWUJorksCs4kCTmCU-tFfc2wwsBQUZiFQWpdD1kqu6gXTfcNHmCjZywaZgiUbosfHgPwr849eLGCKEQezVisL6saxhx-7UUkJBKqrOhTPXL5poYwBM326OWwcl8Mr3gIC5eAdO6H1DMacjO2JV4zvGmu3YQI_-Jj59ebLjNPTT8Wx4A1JZ4WouKERXcnq8Uvo5VaaGTDkKAM9Y_Wa_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEcvTgCb6fY-GZ5Ab1lRnXjKXtR4bg19Hwn9Lp9bY6XC-rSbI7JhZR_3obfaCZuqMsFPzZQqjslCO_M2DVQEfNeAbxAyTLJZOCuiKYBTWLV1h5zdIj5eDovicIniVVwnj0blxYOHgSqJE-3z7-f-mMed_DpKcZySqrk6bw6Lm7vJULG4505agQNXmOXqDbHV1a7e8GAhxFs6tuE-QnFckWEZpPjHQaUMHqS1GqjntW7fKIdLX6GLnqGrmwpTvQyOgDH4_2OibNXS1P0JLfvji3B9dfhuupEHF1qOFQu20K8-mxqpf9f56Zib0EYmrQYNcsRFW2-N7nE16x5q9X1NdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/akhbarefori/674929" target="_blank">📅 22:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674928">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
صداوسیما: ارتش آمریکا با شلیک دو موشک به یک تانکر LPG در دریای عمان، آن را هدف قرار داده و دو نفر از خدمه کشته شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/akhbarefori/674928" target="_blank">📅 22:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674926">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370fbc2f00.mp4?token=AzpM6FSSTaPDpvPTk1PpByMcsrVETFwmRBVuyEL5FocINsIljcqUPNXS9YzV6JZ3JonBZuOqyxJrAkD8jUuf3WSYqB_2sJ6YCJflzCQjfitCVwmrKaDhCazzoa3qOtLXbHzFpp93LS32Cr6HpfkYzoS1HwuySbyg2SUHqh3zmvHiKKTKz2fyn-trIFZb6RUMTZljpYQRhKNNLKdrOABlFBiMo7NEmqptNHPxhpzjnZMg_is02QCi8attrH9p9dcw6AocBOQaf5cjnv-g6as95EJz03L1g2ajEujkQSBKAHGLCa3aQhH2ZP4M6B274KVUb7V2G3Fm20Ym0dqIpeB_CEiBBLIcCmGrD_s0zNKjdwEZcuj9c_ZmM7u34VJlX6N1zpD6dL_3RXXzLJFt5MgRWcYtg3MpTrTE1KOEIE74p5c4CfBzpjcmH_6Bide6Rt3GIRL2ErTBWL569OOvJSS9RrC_CQ2FigaF7pvEyrHDPzv4LTx47owvfsTxBWuhBFOz3fw4KAyOPoxdbMyh_K7q8_gmiQ8JvLTNnzOV2-6pdoSuamJmGiPJXPDS6Kns2l9Fx6bLMVfjP1Z8rETvQU74TNshpgEKAyV_l_ohvzbhdDWr2d48xmk7KV_DRzs18FTfc196ds3Nn9nJsJ7IuVwINarp68U08dL9Flmp2Y4nBR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370fbc2f00.mp4?token=AzpM6FSSTaPDpvPTk1PpByMcsrVETFwmRBVuyEL5FocINsIljcqUPNXS9YzV6JZ3JonBZuOqyxJrAkD8jUuf3WSYqB_2sJ6YCJflzCQjfitCVwmrKaDhCazzoa3qOtLXbHzFpp93LS32Cr6HpfkYzoS1HwuySbyg2SUHqh3zmvHiKKTKz2fyn-trIFZb6RUMTZljpYQRhKNNLKdrOABlFBiMo7NEmqptNHPxhpzjnZMg_is02QCi8attrH9p9dcw6AocBOQaf5cjnv-g6as95EJz03L1g2ajEujkQSBKAHGLCa3aQhH2ZP4M6B274KVUb7V2G3Fm20Ym0dqIpeB_CEiBBLIcCmGrD_s0zNKjdwEZcuj9c_ZmM7u34VJlX6N1zpD6dL_3RXXzLJFt5MgRWcYtg3MpTrTE1KOEIE74p5c4CfBzpjcmH_6Bide6Rt3GIRL2ErTBWL569OOvJSS9RrC_CQ2FigaF7pvEyrHDPzv4LTx47owvfsTxBWuhBFOz3fw4KAyOPoxdbMyh_K7q8_gmiQ8JvLTNnzOV2-6pdoSuamJmGiPJXPDS6Kns2l9Fx6bLMVfjP1Z8rETvQU74TNshpgEKAyV_l_ohvzbhdDWr2d48xmk7KV_DRzs18FTfc196ds3Nn9nJsJ7IuVwINarp68U08dL9Flmp2Y4nBR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صلاح یکتا به دلیل دخالت در امور پزشکی بازداشت شد
🔹
صلاح یکتا با کلیپ‌های شکستن قولنج در ایران و امارات در اینستاگرام مشهور شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/akhbarefori/674926" target="_blank">📅 22:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674925">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd09164e.mp4?token=rjOVuQajLlNV2VkCLUlEYlDFLhC8cHgOerpeGHrdfV4_6odyY_bSev0-em5UV2R7hNMILWq5zsuarD8kA3oP_huNuWs48dXUF3bF0KV8XOdk5Zr-R2p0eTrcDPgC_RDbAf1xg1-jdYBw9Y0zcXghdq-2yx4_pHn7DpD4Invy5LOahYm8J24SzJUNN3G9hGUKdKyaPK7rlqMD-1uMSxyRQzmgoYr67WUQsRQtlTk8MUKI1nGJsXQ-S9pUqnlYPXw9BUzj6mYJtpouFOLR7ZaWI0kZRz7UcgmDQm9jZo7rCKkW_belubOzF7aJmxD_g0PLqaJGfXXInDtC4KAqJWdNZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd09164e.mp4?token=rjOVuQajLlNV2VkCLUlEYlDFLhC8cHgOerpeGHrdfV4_6odyY_bSev0-em5UV2R7hNMILWq5zsuarD8kA3oP_huNuWs48dXUF3bF0KV8XOdk5Zr-R2p0eTrcDPgC_RDbAf1xg1-jdYBw9Y0zcXghdq-2yx4_pHn7DpD4Invy5LOahYm8J24SzJUNN3G9hGUKdKyaPK7rlqMD-1uMSxyRQzmgoYr67WUQsRQtlTk8MUKI1nGJsXQ-S9pUqnlYPXw9BUzj6mYJtpouFOLR7ZaWI0kZRz7UcgmDQm9jZo7rCKkW_belubOzF7aJmxD_g0PLqaJGfXXInDtC4KAqJWdNZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش ده‌نمکی به درگذشت اکبر عبدی: خداحافظ رفیق
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/akhbarefori/674925" target="_blank">📅 21:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674923">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
المیادین: فشار آمریکا بر کردستان عراق برای ورود به جنگ با ایران
🔹
واشنگتن از رهبران کردستان عراق خواسته در جنگ علیه ایران وارد شوند و ایران هم به اربیل درباره پیامدهای هرگونه همراهی با این جنگ هشدار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/akhbarefori/674923" target="_blank">📅 21:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674922">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYhW0opZnRm72uAKUWaXILAkQ2VccDaXpgDjl3xQ6qwpwCTN0UXMu5DpSWyuL3IRR_RyWVAh-fuV4j1zdjjIU95qvBYlhUBTW6oydEoo5dCrSZLxKWA38h6NGWNiPo8eatYv4B0Kjm5hPRu3C7MvwwRo_28MSKrurb9lDe2GR3aqFf_aM5PcEv6LA_fWdF8ohn0lcqvNzqYsSdA4Y1FvCshcXb1XZSmDJTFH3Dpl-GkoxO-mS9f9DIA31xEsVFLJ4inl1H0BMegNd1HjTpORugwiAdRiO9EWD5mOetcp25KzFZwtsusia-Ei3Lvh_NpBK8rWO-YC6x8Z9U2PRgzsYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/akhbarefori/674922" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674920">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c96e0588.mp4?token=uWrOYyoyExoAVf2gXE8pJImHtlTIku8kiqOItnBhGDDaS9e654pXvmy4iVCa4SqKG77nWQenlrHAP9RFr4PTwe4iO85KKEauekT3fpv3GZ-AQ44ocTHP4u1rbmHeo11TniRpHmdHGseNW-NDzEYilLy6EkeplP0ykw4EziuvivNT3ahaZzWgVsR192DoMKC3_rjLp7LIbGmbpOMpkQHskhzf1M_q0wQpyMeV0gISiKCzuXTIz-ABmQn9FfNlYES2AmwW0hSBG1q_ojueK8AevCTNK0K0zu5FE736IfgHLsIIm-lOw82MLbOw9CGxthzpY7C6D_OpPFN5eOulBxKRgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c96e0588.mp4?token=uWrOYyoyExoAVf2gXE8pJImHtlTIku8kiqOItnBhGDDaS9e654pXvmy4iVCa4SqKG77nWQenlrHAP9RFr4PTwe4iO85KKEauekT3fpv3GZ-AQ44ocTHP4u1rbmHeo11TniRpHmdHGseNW-NDzEYilLy6EkeplP0ykw4EziuvivNT3ahaZzWgVsR192DoMKC3_rjLp7LIbGmbpOMpkQHskhzf1M_q0wQpyMeV0gISiKCzuXTIz-ABmQn9FfNlYES2AmwW0hSBG1q_ojueK8AevCTNK0K0zu5FE736IfgHLsIIm-lOw82MLbOw9CGxthzpY7C6D_OpPFN5eOulBxKRgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/akhbarefori/674920" target="_blank">📅 21:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82bdf2a764.mp4?token=quCySdjQfbrADX1-xUKU0N2ACGnVAvKbs4GfVNPjdoPf3wJ9lp-84_-DZ8EZgx7eYanWrpfEUVFB8Aiconu2NDvQuaicFKxhW2qbUA1YfUEQQNVKkatf1zTsHGYjrc-McQ-ouC0vUe1GzynuMLotFyI8IUK1fjEEo6ScuVZHIt-UJLqT2j2KMvFf24gP5vZY_tZO21oOr8Edll8quBfI4DbsTHIdMg_A-h0GvLLpiOBGghAj3lWC25gssVK0B_GTuA6jk9599pDhyux0LswzjmmHxgfYt2_OAt89F09uKd96fSLI5e3HdpAF9nxL4HRdt7p5l5_kxFCeZwVyrYVFaHPgSKSHhkUrTDT6fH02LsR78k68B9GQBzA2u8P5G6Pz5Yvwunx_xwh4m3C93fNsrVyHlbwAk-Hl2v19bT2KjNyDNbD1CjAvsuC8B8LBLJZRoteaMVtpzeGURppPI-5i5bnkKE7anCM9v9Qlnd1GVKZnwlLSzLJO74U56MxWzhdnFw_zsaKg0vGrewWGgDM2i00Wqj5NBvsz9hVbWuw9JReH_6x_TeQ7DTL6Y65pT38tX_w7clgS4Fqs5uMwpnCKmrgyR4-Qci_6zZ0byIipNCeoVKm6TvUS6ut_8FTvE-TDosN0CNxKd4jKODUg5OELSL9BWDOuYLwY_3QhBCwyEOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82bdf2a764.mp4?token=quCySdjQfbrADX1-xUKU0N2ACGnVAvKbs4GfVNPjdoPf3wJ9lp-84_-DZ8EZgx7eYanWrpfEUVFB8Aiconu2NDvQuaicFKxhW2qbUA1YfUEQQNVKkatf1zTsHGYjrc-McQ-ouC0vUe1GzynuMLotFyI8IUK1fjEEo6ScuVZHIt-UJLqT2j2KMvFf24gP5vZY_tZO21oOr8Edll8quBfI4DbsTHIdMg_A-h0GvLLpiOBGghAj3lWC25gssVK0B_GTuA6jk9599pDhyux0LswzjmmHxgfYt2_OAt89F09uKd96fSLI5e3HdpAF9nxL4HRdt7p5l5_kxFCeZwVyrYVFaHPgSKSHhkUrTDT6fH02LsR78k68B9GQBzA2u8P5G6Pz5Yvwunx_xwh4m3C93fNsrVyHlbwAk-Hl2v19bT2KjNyDNbD1CjAvsuC8B8LBLJZRoteaMVtpzeGURppPI-5i5bnkKE7anCM9v9Qlnd1GVKZnwlLSzLJO74U56MxWzhdnFw_zsaKg0vGrewWGgDM2i00Wqj5NBvsz9hVbWuw9JReH_6x_TeQ7DTL6Y65pT38tX_w7clgS4Fqs5uMwpnCKmrgyR4-Qci_6zZ0byIipNCeoVKm6TvUS6ut_8FTvE-TDosN0CNxKd4jKODUg5OELSL9BWDOuYLwY_3QhBCwyEOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از نماد رواق دارالذکر در «محرم شهر»/ درد و دل های مردم با رهبر شهید انقلاب در حاشیه رویداد آیینی محرم شهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/akhbarefori/674919" target="_blank">📅 21:33 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
