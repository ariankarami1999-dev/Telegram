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
<img src="https://cdn4.telesco.pe/file/NaDwbfPmI2EfXR5CuA6pz9kb3wddb3RksZ7gpIj7a4dYGBm3Ma9tBqYcm_OrtAavKcwfAww8OqdhPlccBb7xxL6P4ygm5fS2F7PAgJIQBnodV9WFxudUBO4yXTFNU1ElUaQzt0kbPsOI2hSRyxhkqKOmfJja9TBCbJnUY_mRu2PBdyYHNPY0X34yNIkSBP8Z2L5drA4nk2IuSSkFw-zzINcdYVLAXMuWp4pC1ikMSklWMfM34tI_8_NlR1dESRd2sDFD2_7Tsx3QUyC4d2bCIkg8kogrgc22QGLc7UXA95Kt9-3i92UMKullQjKqdSiam3M9PC6b0hCCW6OJiWM1QQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 13:48:30</div>
<hr>

<div class="tg-post" id="msg-121742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
اسلام‌آباد به شدت روی چین حساب باز کرده است تا به پیشبرد توافق احتمالی آمریکا و ایران کمک کند، و انتظار می‌رود نخست‌وزیر پاکستان، شہباز شریف، در مرحله‌ای بعدی به چین سفر کند، طبق گزارش العربیه که به منبعی پاکستانی استناد می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/alonews/121742" target="_blank">📅 13:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121741">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر نیرو: با وجود بارش‌های خوب امسال، استان مرکزی و استان تهران در وضعیت ضعیف آب قرار دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/alonews/121741" target="_blank">📅 13:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع پاکستانی:
هیچ جایگزینی برای توافق موقت بین واشنگتن و تهران وجود ندارد
🔴
کاهش فاصله‌ها آسان نیست زیرا هر طرف سقف بالایی از خواسته‌ها دارد
🔴
مسائل بزرگ در توافق به بازه زمانی طولانی در مذاکره نیاز دارند
🔴
آمریکا و ایران بر مواضع خود درباره اورانیوم پایبند هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/alonews/121740" target="_blank">📅 13:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121739">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbeee07e55.mp4?token=ISDDhwiWZWm-S95QNd0N076ODS3iMxm-9uFcftBssMV2lpTMKJ-aCeBbGjUr0_K9_E_UeECUKB77hxsN_saSMh_A5MiLC9JkqmSJLgEGsFoJAhVn2L2evQqvay7H6ZOCeceTIyAigsAZHxV4TiTWr550_FmyCuxPMeriiZEWMwKIAVL9k_sK9MsjlYRG1CcZybHmzFs7bGIe569U2fpECiAswA1CSGjMY3wvkZ1_WvyklQ_Me3r1L7nyR9MZHydnXufUxlwN8FqDWYrGS388FtOhjX0BYn1R7HQvhXtGNLyNva5iu_piZRqKfyHwgeoABCp2QQAcdRFRah9Go7JvoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbeee07e55.mp4?token=ISDDhwiWZWm-S95QNd0N076ODS3iMxm-9uFcftBssMV2lpTMKJ-aCeBbGjUr0_K9_E_UeECUKB77hxsN_saSMh_A5MiLC9JkqmSJLgEGsFoJAhVn2L2evQqvay7H6ZOCeceTIyAigsAZHxV4TiTWr550_FmyCuxPMeriiZEWMwKIAVL9k_sK9MsjlYRG1CcZybHmzFs7bGIe569U2fpECiAswA1CSGjMY3wvkZ1_WvyklQ_Me3r1L7nyR9MZHydnXufUxlwN8FqDWYrGS388FtOhjX0BYn1R7HQvhXtGNLyNva5iu_piZRqKfyHwgeoABCp2QQAcdRFRah9Go7JvoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: "درحال حاضر، در سازمان ملل متحد، قطعنامه‌ای داریم که توسط بحرین ارائه شده است. ما بسیار درگیر آن بوده‌ایم. این قطعنامه بالاترین تعداد همکاران ارائه‌دهنده را در تاریخ هر قطعنامه‌ای در شورای امنیت داشته است. متأسفانه، چند کشور در شورای امنیت به وتوی آن فکر می‌کنند که این امر تأسف‌بار خواهد بود."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/alonews/121739" target="_blank">📅 13:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121738">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نیروی دریایی سپاه: طی شبانه روز گذشته ۳۵ فروند کشتی اعم از نفتکش، کانتینربر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/alonews/121738" target="_blank">📅 13:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عربستان: با هرگونه تلاش برای سیاسی‌کردن حج با قاطعیت برخورد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/alonews/121737" target="_blank">📅 13:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c641e7ef.mp4?token=bQBTpiE3OrQo57UzipZ5SK_NKZHa25hDIhWUKQAP_CKU3fU9ft-o12Gkm1DZF7AjhWpxBpGaHoj9-Bzmfvy-3szcgqwCk_MYYh-Td5SLVFNiH4tG6DqRJScxEdi3zTS_F5sj2EREVQud_pKnPNHl9iGJ3hM_Z3OPbVqzXKtbdKy8bUiJ_jg_kXPP-R-iLXNDpMnh1HVS7b0rcLRBO0ft7rVlAysIDqFVamCrNzVnE__fic8StLaxRy2AFtpLJuRZYMz6t1rXgOxCkEy7ESPCHurqz4qmgLhx5_fVJWb-aKel__JqrklTkjvIMF6GxMBd1z3gpDTnFFeuap14jQr47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c641e7ef.mp4?token=bQBTpiE3OrQo57UzipZ5SK_NKZHa25hDIhWUKQAP_CKU3fU9ft-o12Gkm1DZF7AjhWpxBpGaHoj9-Bzmfvy-3szcgqwCk_MYYh-Td5SLVFNiH4tG6DqRJScxEdi3zTS_F5sj2EREVQud_pKnPNHl9iGJ3hM_Z3OPbVqzXKtbdKy8bUiJ_jg_kXPP-R-iLXNDpMnh1HVS7b0rcLRBO0ft7rVlAysIDqFVamCrNzVnE__fic8StLaxRy2AFtpLJuRZYMz6t1rXgOxCkEy7ESPCHurqz4qmgLhx5_fVJWb-aKel__JqrklTkjvIMF6GxMBd1z3gpDTnFFeuap14jQr47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو :  اینکه آمریکا داره توان هسته‌ای و موشک‌های دوربرد ایران رو تضعیف می‌کنه
🔴
برای خاورمیانه، اروپا و کل دنیا خیلی مهمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/alonews/121736" target="_blank">📅 13:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121735">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
انور قرقاش، مشاور رئیس امارات: دور دیگری از درگیری میان آمریکا و ایران فقط مسائل را پیچیده‌تر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/alonews/121735" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121734">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
زلنسکی : یه پالایشگاه نفت روسیه تو یاروسلاول رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/121734" target="_blank">📅 12:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121733">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CShAIR_hgOfAssz3ywOuayPFyCuvE5Ig9--1U-m8rDiQwkAY80zpOzizGMXVrtWlT3au_pjptggs6M6qiCfuKHIclZOoUlTU3JZ9EQ17kZoyAynG9aUjpKyjs9hVMMkxsqva4EupJZAwAajBNF1ikp48S-KaTEiXIyJQN0MsV5sIJHd61nHdi2PSE_byim7oxbEetsUU4e9DYcZ8RF3I19RtJVuI4FV4DtzLy3OztVGL33R5WOBIbtLhjl9_3s3Za_OC3AwJ7QDT8_WVnLzqp0_Gdgbie1gJwFiE7Emj8HZf4leRH2bIj4RZvOHvNGsZD2MtlIbgDu-gIzr1paQw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای فارن افرز:
«رهبران خلیج فارس از قبل، شروع به تنوع بخشیدن به تأمین‌کنندگان سلاح و مشارکت‌های امنیتی خود کرده‌اند.
🔴
برای اینکه بتوانند در مورد آنچه برایشان اتفاق می‌افتد، حرف بیشتری برای گفتن داشته باشند، باید هماهنگی بهتری بین خود، چه از نظر نظامی و چه از نظر دیپلماتیک، برقرار کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121733" target="_blank">📅 12:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121731">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQlio8AMeR_zeG0Oa3IWFmL4MiQF4c3Vq85c1aZm47gHY1_CFr91MgWEXJO9VWvK1D_Mpy46cs7Mej2g_yRVNq6cOaOym2hEkm7JkjTbIDN79IjnoK-N0SfKObc1K8D87wORoNxhJnl1pB_6whCRlY75FD9PdF0CtA6rvyjNnDxTydlsWhQjWkShAUcbtghJiuBaJctFPPYDGdguLCGEUbazVi_5Fk5d5mFDL05PRb7RkOjRqNv3yePOP6oxoPWnb8vxhxl5aWsnDAyWVtJDwXEGlWyUgqvpxE9UhtLSN8C5TXReju-qvQY2Sd-zLL5FdTJSQ3A2aiBuOsEcmac7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ox6IHJQ23zDG18BqkgavFxXKVxziS4eBxfdyoJr665vBsGxgLpfTYpMncXy6UAMueOlP7xOOEueNikvXGBZkgdN7DuiYShqI8D5OIS-d5E2yjh5s76mcZJ1IzgPj3bHC1X6ANz81qlqrE49GhPje9HdTQZ0wXoBZ-P9f-dgNS1YUAkM94JMYf6g2yUuglcvAvB-tt1bjBOXNGaeBcpmNOUF2cuyEyv2i8TIoS1QqHk3JQyR_AUIyzm5z_ctXdAVrhAWS6ctOgDRIw0QUTV3nqgOoHMMau1JZ-_Rwtrvx0Z445kFXxELSEvL273touOxJyOTRihHDv74XNzkbYS4wsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل به "میفدون" لبنان حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/121731" target="_blank">📅 12:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121730">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
تلگراف: قرار بود ترامپ با اتخاذ موضعی سختگیرانه‌ تر در قبال چین به پیشرفت هند کمک کند.
🔴
در عوض، جنگ‌ها و غیرقابل‌پیش‌بینی بودن او به جاه‌طلبی‌های نارندرا مودی برای تبدیل هند به یک ابرقدرت جهانی آسیب می‌رساند.
🔴
درگیری در ایران به هند ضربه سختی وارد کرده است. این کشور به نفت وارداتی متکی است که بخش عمده آن از طریق تنگه هرمز وارد می‌شود، بنابراین افزایش قیمت انرژی باعث تضعیف رشد، افزایش تورم و ترساندن سرمایه‌گذاران می‌شود.
🔴
مودیز در حال حاضر پیش‌بینی رشد هند را به ۶ درصد کاهش داده است - بسیار کمتر از ۸ درصدی که مودی می‌گوید برای تبدیل هند به یک کشور توسعه‌یافته تا سال ۲۰۴۷ لازم است.
🔴
در عین حال، ترامپ به چین و پاکستان، دو رقیب اصلی هند، نزدیک‌تر شده است و سال‌ها تلاش مودی برای ایجاد روابط قوی‌تر با واشنگتن را تضعیف می‌کند.
🔴
مودی اکنون در تلاش است تا با جستجوی قراردادهای جدید انرژی در خارج از کشور، کاهش فشارهای هزینه‌ای در داخل و حتی منصرف کردن هندی‌ها از خرید طلا و سفر به خارج از کشور، آسیب‌ها را محدود کند.
🔴
این بحران مشکل عمیق‌تری را آشکار کرده است: با وجود رشد سریع، هند هنوز فاقد قدرت تولید، زیرساخت‌ها و نفوذ اقتصادی لازم برای رقابت با چین است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/121730" target="_blank">📅 12:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121729">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا مدعی شد که فکر نمی‌کنم هیچ کشوری موافقت کند که برای عبور از تنگه هرمز هزینه پرداخت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/121729" target="_blank">📅 12:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121728">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ادعای وزیر امور خارجه بریتانیا: ما با عزم ایالات متحده برای بازگشایی تنگه هرمز به روی کشتیرانی موافقیم
🔴
شرم‌آور است که ایران با مسدود کردن کشتیرانی بین‌المللی سعی در ربودن کل اقتصاد جهانی دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/121728" target="_blank">📅 12:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121727">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b97475f3.mp4?token=HXXzPLnuA7D3yhJEfNHD2o6RQS7QEPuz281Ohkp9JUaPstM8I0hK5AdW6dcUpePLSM1SRqIVpnQ329okPR8UskoYgDbqPQy3WcgGoeoZxnFOUDta1Y30zfsBY5OG7L6yk5EjdXa-QQVsYlRGdsTd5OULOf-REGXyAhLT5TC__jBa6oILqhPoYnBL43uzxgfFj0wICRkaWJOdpYcD8FhlNeFJtjFVTu93TgIGgSVbaBzbSBpzbVNRSsMEfmZjj0AJ5cF1N143B-Dy94Mkunrq3cZdaA15-TmzQZs6O20XRmCdo4Z5cLmKO4LjQ62V8bK5iNJWONBUcKhZKmp3nIu-UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b97475f3.mp4?token=HXXzPLnuA7D3yhJEfNHD2o6RQS7QEPuz281Ohkp9JUaPstM8I0hK5AdW6dcUpePLSM1SRqIVpnQ329okPR8UskoYgDbqPQy3WcgGoeoZxnFOUDta1Y30zfsBY5OG7L6yk5EjdXa-QQVsYlRGdsTd5OULOf-REGXyAhLT5TC__jBa6oILqhPoYnBL43uzxgfFj0wICRkaWJOdpYcD8FhlNeFJtjFVTu93TgIGgSVbaBzbSBpzbVNRSsMEfmZjj0AJ5cF1N143B-Dy94Mkunrq3cZdaA15-TmzQZs6O20XRmCdo4Z5cLmKO4LjQ62V8bK5iNJWONBUcKhZKmp3nIu-UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو می‌گوید تصمیمات در مورد نیروهای نظامی ایالات متحده در اروپا «تنبیهی» نیستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121727" target="_blank">📅 12:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121726">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ادعای منبع پاکستانی به الجزیره: اصرار آمریکا و ایران بر بالا بردن سقف خواسته‌هایشان درباره اورانیوم و تنگه هرمز، به بن‌بست در مذاکرات انجامیده
🔴
اسلام‌آباد همچنان نسبت به امکان دستیابی به یک توافق موقت بین واشنگتن و تهران خوش‌بین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121726" target="_blank">📅 12:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121725">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: نخست‌وزیر پاکستان در سفر فردای خود به چین درباره ابتکاری مشترک برای پایان دادن به جنگ گفت‌وگو خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/121725" target="_blank">📅 12:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121724">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر امور خارجه آلمان: ما در حال آماده شدن برای مشارکت در تأمین امنیت تنگه هرمز تحت رهبری بریتانیا هستیم، اما انتظار ماموریتی مشابه ناتو را ندارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/121724" target="_blank">📅 12:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121723">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری / وزیر امور خارجه آمریکا: در مذاکرات با ایران پیشرفت‌هایی حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/121723" target="_blank">📅 11:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121722">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رویترز: وقتی که ترامپ گفت «تمدن ایران امشب خواهد مرد» مقامات آسیایی و اروپایی نگران بمباران اتمی ایران شدند که می‌توانست منجر به تشدید تنش هسته‌ای در اوکراین نیز بشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/121722" target="_blank">📅 11:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121721">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0874c8216.mp4?token=SKhbo05ucEzgif-PB2sftCXRRKHd9Umb7MMmsjjub9AQ2RDTwgVeIuP5aSaQ-y51DBAYSLMqdcQMSfToElHJAj_8_1chqi1-IP1PC11JN1P-dckf8FTgANMxEIQ4UExv07vEtVe8BI1AS8nLDhxou-rU0UYbZ5G03qpJgA8tiYsuo7Y9J3MTwu2EHy4641ylXmiDeNIP3aEdCDnnDclypGagUZX1ZIE7nCxlm2zNu5KAR7rfgBz4weFo6-tTgmw6Gg1qeY9sLOB2uoIaxV91mQjxfMT26jnqLkLbucdNMGIUPn6EszZIHbRb_UasAZKKT0Sg1gWmCC_JZlj--fhc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0874c8216.mp4?token=SKhbo05ucEzgif-PB2sftCXRRKHd9Umb7MMmsjjub9AQ2RDTwgVeIuP5aSaQ-y51DBAYSLMqdcQMSfToElHJAj_8_1chqi1-IP1PC11JN1P-dckf8FTgANMxEIQ4UExv07vEtVe8BI1AS8nLDhxou-rU0UYbZ5G03qpJgA8tiYsuo7Y9J3MTwu2EHy4641ylXmiDeNIP3aEdCDnnDclypGagUZX1ZIE7nCxlm2zNu5KAR7rfgBz4weFo6-tTgmw6Gg1qeY9sLOB2uoIaxV91mQjxfMT26jnqLkLbucdNMGIUPn6EszZIHbRb_UasAZKKT0Sg1gWmCC_JZlj--fhc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله با پهپاد انتحاری، یکی از باتری‌های گنبد آهنین اسرائیل رو زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/121721" target="_blank">📅 11:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121720">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
گزارش در وال استریت ژورنال: ایران از غول تجارت رمزارز بایننس برای فرار از تحریم‌ها و انتقال میلیاردها دلار برای تامین مالی ارتش خود در طول سال‌ها استفاده کرده است - از جمله انتقال رمزارز که این ماه انجام شده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/121720" target="_blank">📅 11:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121719">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال: وزارت دادگستری آمریکا تحقیقات خود را درباره استفاده ایران از صرافی بایننس برای  دور زدن تحریم‌ها آغاز کرده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/121719" target="_blank">📅 11:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121718">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بلومبرگ: پوتین می‌خواهد جنگ اوکراین را تا پایان امسال به پایان برساند، اما فقط با شرایطی که روسیه بتواند آن‌ها را به عنوان پیروزی معرفی کند.
🔴
این شرایط شامل کنترل کامل منطقه دونباس و تضمین‌های امنیتی گسترده‌تر از اروپا است که به طور موثر کسب‌های ارضی روسیه در اوکراین را به رسمیت می‌شناسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/121718" target="_blank">📅 11:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121717">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a8a3dcb3.mp4?token=q2jZeAQjS1oVhX9O4eCMwVCb_9gPgP_iYiEj3lR1c4YA47VKDhFwAuSGG7mE43YQ87WNckYOBaoYD4aBkQ2tY44FdgXmuxke-pRLsA0GzeG-7TCLjY6ZrkMbBwlm9i8bftRbEJ3Yt-bbvEBKcds6ajKJjqCEC_rHY_4oDma0_TfFhzvTZve8T8PKjT5KRwHzCjZ7PPL5EmyQHBFC_uIu5JF1sSNVVx_Nl83OR55pbrSG6DLYCkzC5IHJNEnSJvVU3eHeYHvm-CmuY5_eF0r8lTo6jDZYhKhz7w36sw8OG5xzh0TKmJ-TzgZktd4W2RIpMTlWu5SdkIVcbv9-l87InA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a8a3dcb3.mp4?token=q2jZeAQjS1oVhX9O4eCMwVCb_9gPgP_iYiEj3lR1c4YA47VKDhFwAuSGG7mE43YQ87WNckYOBaoYD4aBkQ2tY44FdgXmuxke-pRLsA0GzeG-7TCLjY6ZrkMbBwlm9i8bftRbEJ3Yt-bbvEBKcds6ajKJjqCEC_rHY_4oDma0_TfFhzvTZve8T8PKjT5KRwHzCjZ7PPL5EmyQHBFC_uIu5JF1sSNVVx_Nl83OR55pbrSG6DLYCkzC5IHJNEnSJvVU3eHeYHvm-CmuY5_eF0r8lTo6jDZYhKhz7w36sw8OG5xzh0TKmJ-TzgZktd4W2RIpMTlWu5SdkIVcbv9-l87InA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: تفاوت ما با چین و روسیه این است که یک نفر همه تصمیم‌ها را نمیگیرد
🔴
مارک روته، دبیرکل ناتو، اعلام کرد: «ناتو یک ائتلاف سیاسی و نظامی است. تفاوت بزرگ ما با چین یا روسیه این است که در آن کشورها در نهایت یک نفر همه تصمیم‌ها را میگیرد.»
🔴
او افزود: «ما یک ائتلاف دموکراتیک و نظامی هستیم و به همین دلیل تصمیم‌ها همیشه بر اساس ملاحظات سیاسی و نظامی گرفته میشوند. ساختار ناتو این‌گونه عمل میکند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121717" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121716">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9d60253b.mp4?token=dzfvwL7EoYAeITMvZUG_jY-EXi_2TFd5w_hgca2oIE4VsVFCYiXmA92a45vdd-2RYHcPL0kPw6Lb5jIAXETAYtuAY6OEu5PkCilVch-8xZB0r8ztQv1BRLxzNlPd0uxa4RB1X1gWCOE_QJfGYlGGNmKurcckDYEmqmG-C189UBiM6fqF_tKZQhLy2Hm4PTkKkXoICHMP2XBLODAOfIHBZG7NzLC4_mwGc1vwDvMyTUOYZY3jTWXxW0lhTrCh1XzFlIsTEHnlLnQvx2g6LJ-rKx079ZGXaVmSa96HnKe6J8-5KapSX6LfD0nSK_Imz_oSQd9KKlGDSf5oTHqgorfDxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9d60253b.mp4?token=dzfvwL7EoYAeITMvZUG_jY-EXi_2TFd5w_hgca2oIE4VsVFCYiXmA92a45vdd-2RYHcPL0kPw6Lb5jIAXETAYtuAY6OEu5PkCilVch-8xZB0r8ztQv1BRLxzNlPd0uxa4RB1X1gWCOE_QJfGYlGGNmKurcckDYEmqmG-C189UBiM6fqF_tKZQhLy2Hm4PTkKkXoICHMP2XBLODAOfIHBZG7NzLC4_mwGc1vwDvMyTUOYZY3jTWXxW0lhTrCh1XzFlIsTEHnlLnQvx2g6LJ-rKx079ZGXaVmSa96HnKe6J8-5KapSX6LfD0nSK_Imz_oSQd9KKlGDSf5oTHqgorfDxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دولت ترامپ فروش ۱۴ میلیارد دلاری سلاح به تایوان رو متوقف کرد
🔴
تا مهمات آمریکا برای جنگ ایران رو حفظ کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/121716" target="_blank">📅 11:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121715">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmE7UQrr5Ic6J9j_SI5ryrD_YBTdf0PYbUHWupZRbsqzV8ZSsUWJL1Vo1uCmOnXWQyVJHPlk8EoLSDak5MQPYNEAGiF7dU4xDBf8LJz-Y_8lXH1iU71NeWA3RPK6_UWHLqkiaVa1WqaRC1_mETiihFooefw2s34QnMSzOsdDRlJR35WftsCFO5TD73_Sy0kyZEzxujlGDWGTOWu5QErvt7WlvGMPzOdAzelHTFWF0lD1S1QOVD3KT-77csPn6VSkELj6LPC7J3LWJI10Q7-I9HbJOJblRHa7smVl5NekyVNdIo-VLtNl_2BuU6iJe_UZ1DwSaf11Jpm0pIOLOAyhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ناو هواپیمابر آبراهام لینکلن در بالاترین سطح آمادگی عملیاتی قرار دارد
🔴
ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام، با انتشار تصاویری از پرواز جنگنده‌های نیروی دریایی آمریکا از ناو هواپیمابر «یواس‌اس آبراهام لینکلن» در دریای عرب اعلام کرد گروه رزمی این ناو در «بالاترین سطح آمادگی عملیاتی» قرار دارد.
طبق بیانیه سنتکام، این ناو همزمان در اجرای محاصره دریایی آمریکا علیه بنادر ایران مشارکت دارد. فرماندهی مرکزی ایالات متحده همچنین اعلام کرده در جریان این محاصره دریایی، ۹۴ کشتی تجاری تغییر مسیر داده‌اند و چهار کشتی دیگر نیز «زمین‌گیر و مجبور به توقف» شده‌اند.
🔴
سنتکام پیشتر ویدیویی از ورود نیروهای آمریکایی به یکی از کشتی‌هایی که قصد عبور از خط محاصره را داشت منتشر کرده بود. واشنگتن میگوید هدف از این فشارها، وادار کردن تهران به توافق برای پایان دادن به جنگ و کاهش تنش است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121715" target="_blank">📅 11:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121714">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سپاه : خنثی‌سازی مهمات عمل‌نکرده در خرم‌آباد(فردا)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/121714" target="_blank">📅 11:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121713">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دبیرکل ناتو: تعدادی از کشورهای اروپایی تمایل خود را برای مشارکت در تلاش‌ها جهت بازگشایی تنگه هرمز ابراز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/121713" target="_blank">📅 11:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121712">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
الجزیره: مقامات دریایی بریتانیا مدعی گزارشی از وقوع حادثه‌ای در ۹۸ مایل دریایی شمال سقطری، یمن شدند
🔴
عملیات تجارت دریایی بریتانیا: کشتی نزدیک شدن یک قایق کوچک با ۵ سرنشین را تأیید کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/121712" target="_blank">📅 11:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121711">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
الجزیره: مقامات دریایی بریتانیا مدعی گزارشی از وقوع حادثه‌ای در ۹۸ مایل دریایی شمال سقطری، یمن شدند
🔴
عملیات تجارت دریایی بریتانیا: کشتی نزدیک شدن یک قایق کوچک با ۵ سرنشین را تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121711" target="_blank">📅 11:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121710">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر امور خارجه کانادا: ما به محض دستیابی به آتش‌بس دائمی، در مین‌زدایی و حمایت از آزادی دریانوردی در تنگه هرمز مشارکت خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/121710" target="_blank">📅 11:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121709">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2joucx_niQLkKox2QlOKn8J4-YrtDn3kRI6XcaPXkDYFKtG8SADT0JSPaZCnxGjNKJbcd1D3utJHQ9PZcebx3NUs--NHY0GrdR1h4lxztk848MYFrLBllGwkF0vMKQA2bETSYFkVAmL7aKiMCFERXXzRVeZVDXxCNHcIRfxn1CYR2L_59mh3AEhpcg0UCiAc1mMVGGn01tnr6myA8q1H-T94sTd91Cq1KLdJf-XGBtkJRb6ISzMTGPTC604Ht2VJPEnuCr2y9awOrF1Um9tMWG1145NYM6Zxc-KQKn7eZyJ50w-HsBd-6TA4_sCq0J6uTWQ74StLVh-3vMLWCnmDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: موشک‌ها را برای مذاکره با شیطان بفرستید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121709" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121708">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
میدل ایست نیوز نوشت: کشور سوریه در یک جلسه پشت درهای بسته با حضور وزرای دارایی و رؤسای بانک‌های مرکزی کشورهای عضو گروه هفت در پاریس شرکت خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/121708" target="_blank">📅 10:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121707">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال: وزارت دادگستری آمریکا تحقیقات خود را درباره استفاده ایران از صرافی بایننس برای  دور زدن تحریم‌ها آغاز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121707" target="_blank">📅 10:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121706">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN7jgY6W8vvW2rxB52Wa-GKjeVKdcuwRw7unSJwtswci0FxlngB5H8nj0uN0_JNokHuLrDSP88w6Qjsi5mG9vi_UqAgNYW6VlnC-FC3XsIesnrAYZLFZyphlnq-GHifasRWDwmukRMmRopaOPu0mUrPkji79Fb3JIKVxkzlUxwEUUgh9_QoOBXZqoxFd3J2xvSLGaFojPoFiPBsKpVK7Ya3S0x1CK6elR-A71YluzXwXDTGjU0KsDiPbsw8k4dLDj5XqbKM_SfE1105qvzddCcgHAdHn_u449m5zJI0NB45ROK0PJ0yRmZh4auTXJ8j8T2lBLtopkIkiUDYn71215Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه CNN: ترامپ پس از اینکه در ایران برای تغییر نظام شکست خورد، به دنبال جبران در کوبا است
🔴
ترامپ در کوبا به دنبال چیزی است که در ایران از دستش رفته است. اما هرگونه اقدام ارتش آمریکا تحت فشار کاخ سفید، با خطرات سیاسی و نظامی بالایی همراه خواهد بود.
🔴
اعلام جرم دولت آمریکا علیه رائول کاسترو (رئیس‌جمهور سابق ۹۴ ساله کوبا) یک چرخش قابل‌توجه در رویارویی نزدیک به ۷۰ ساله آمریکا با این جزیره است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121706" target="_blank">📅 10:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121705">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
چین از تلاش‌های میانجی‌گرانه ما حمایت می‌کند و در همکاری با ما ابتکاری ۵ ماده‌ای ارائه داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121705" target="_blank">📅 10:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121704">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ادعای رویترز به نقل از یک منبع پاکستانی: نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121704" target="_blank">📅 10:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121703">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
جروزالم پست: مقامات اطلاعاتی اسرائیل هشدار دادند که ایران ممکن است در حال برنامه‌ریزی برای حمله موشکی و پهپادی غافلگیرکننده علیه اسرائیل و کشورهای خلیج فارس باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121703" target="_blank">📅 10:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121702">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtX7uQfqv-Sfa0bJWznK9rUSsorTgEgx5-KePSoONSULYAmo94Y6GdQO-LWGKTkcob7bi5NYEQTFI72Aqzglv6B4ICnC9g89TEcyg6oXYROPJML1gqiuldkZz3qExC9sganMR1-kF1WwGj9p5xLxgXT3fvfGJ7vBouf9j2YdodajFZmTllKiqS48hFFd_Kwtdk-spzybx11RBKa8FkaPAkYPSBbIiOB7q_TFbssBhOS9TKErrvs0NZI5HtlbJOIkMyCYtwniqH9x1gRRJUM4AtLd36dgQ37I5xsUlfzKzk9ZJp2_ibzytr8AYKK4KSy38lVm9uVPPnJwFRvHF76AYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوجه‌کباب میلیونی شد ....
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121702" target="_blank">📅 10:24 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121701">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کانال ۱۳ عبری به نقل از مقام آمریکایی: ایرانی‌ها در سرعت بهبودی از حملات، از تمام جدول‌های زمانی پیشی گرفته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121701" target="_blank">📅 10:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121700">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر خارجه سوئد: ما متعهد به افزایش هزینه‌های دفاعی در ناتو و همچنین حمایت از اوکراین هستیم.
🔴
ما آماده ایم در تضمین آزادی کشتیرانی در تنگه هرمز مشارکت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121700" target="_blank">📅 10:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121699">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
منابع عربی: انفجار در ابوظبی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121699" target="_blank">📅 10:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121698">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntUpWUGQLQrumVr4vR65uNIL9PnBl0VzGbQNbV1uUcHlb6adyBr3lMMDT7qEk4TStfN0nxNDCubckA63vKYJGyRJvI5nrplCW5kQnbKCTDGpApbPT_qXogHEdwT74cXAyzSQbONRwUih-sg9zXHIm7nJn33B1IDpDeCPThWLqpjkoum6RhFKHB_zNhbg5qwUfEUjpS7HYi2BWejgezk5DXwj81p2g6cKEbf9BztoNEMjW8HX_P635a0TMBchDVhLwxbnqJKVbMXuxAK1hlwZ_DIGU5iHADITdC_QLgnZjcxI4HP0FJeGtxfQ9DIcmIKy917qNDdJ1l7zCoHRfctTAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز نوشت: ایران با ایجاد ایست‌های بازرسی جزیره‌ای، توافق‌های دیپلماتیک و گاهی دریافت «هزینه عبور»، در حال تثبیت کنترل خود بر تنگه هرمز است
🔴
در حالی که کشورها تلاش می‌کنند ذخایر انرژی رو به کاهش خود را که در پی جنگ مختل شده، دوباره تأمین کنند، ایران یک سازوکار چندلایه برای عبور کشتی‌ها از تنگه هرمز اجرا می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121698" target="_blank">📅 09:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121697">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ثبات انس جهانی طلا در محدوده ۴۵۰۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121697" target="_blank">📅 09:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121696">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxKu96SVDZjdnUyIK4xkLDgFq8_aOV8W_pPgwWt_fGkWjcJ1xs3BEtph3eilwLk-ZMf-aV7DfwT4BTLKhun-fQInIjRViVxRIfCX8KmWv3VMUdTVIIerfQQsrbDVDmw82aQjkSehd3-AV61SQCOnP-J62hAt8kdUZjQEnxl05a96OmTAOTnXR68YVYnkaEHCe_z0zU03fx4vEKuhPSQWozA5jMy9_LJ7dsFCq8zjlhRVitRQanrhg-lzs2gUoowrYazTDZAVRDnDVdxI58ztFk_TsJ-P8y37jdQhi2fS-OJHrIxgg-i_-Nz44uqiSXo8CnKXNYPT13-pTEoVLFYUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعلام وضعیت اضطراری بین‌المللی در پی شیوع ابولای بوندیبوگیو
🔴
سازمان جهانی بهداشت شیوع ابولای بوندیبوگیو در کنگو و اوگاندا را وضعیت اضطراری بین‌المللی اعلام کرد. این سویه که واکسنی برای آن وجود ندارد، از طریق تماس مستقیم با خون یا مایعات آلوده منتقل می‌شود و نرخ مرگ‌ومیر آن ۳۰ تا ۵۰ درصد گزارش شده است.
🔴
دوره نهفتگی این بیماری ۲ تا ۲۱ روز است که با علائم اولیه تب، سردرد و گلودرد آغاز شده و در مراحل پیشرفته به استفراغ، اسهال، اختلال عملکرد کلیه و کبد و خونریزی‌های داخلی و خارجی منجر می‌شود. در حال حاضر درمان این بیماری تنها محدود به آبرسانی حمایتی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121696" target="_blank">📅 09:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121695">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نظرسنجی نیویورک تایمز: ۹۵ درصد رأی‌دهندگان دموکرات با جنگ آمریکا و اسرائیل علیه ایران مخالف هستند
🔴
سه‌چهارم آنها نیز مخالف کمک به اسرائیل هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121695" target="_blank">📅 09:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121694">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
استولتنبرگ، وزیر دارایی نروژ و دبیرکل پیشین ناتو:   ناتو بدون آمریکا دوام نخواهد آورد، اتحادیه اروپا باید در مسائل امنیت جمعی و تضمین‌های دفاعی جایگزین ناتو شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121694" target="_blank">📅 09:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121693">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نخست‌وزیر عراق: دستور بررسی ابعاد حملات به عربستان و امارات صادر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121693" target="_blank">📅 09:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121692">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بزرگ‌ترین شرکت انرژی آمریکا، اکسون موبیل، در حال مذاکره با دولت ونزوئلا برای بازپس‌گیری حقوق تولید نفت در ونزوئلا است، پس از اینکه تقریباً ۲۰ سال پیش زمانی که هوگو چاوز، رئیس‌جمهور وقت، صنعت نفت ونزوئلا را ملی کرد، از این کشور اخراج شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/121692" target="_blank">📅 09:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121691">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کمیسیون اروپا پیش‌بینی قیمت نفت در سال ۲۰۲۶ را نسبت به تخمین‌های پیشین، ۴۶ درصد افزایش داد.
🔴
کمیسیون اروپا در گزارش «چشم‌انداز اقتصادی بهار ۲۰۲۶» خود تأکید کرده است که شوک انرژی ناشی از جنگ در خاورمیانه و بسته شدن عملی تنگهٔ هرمز، مهم‌ترین عامل این بازنگری صعودی در قیمت‌های نفت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121691" target="_blank">📅 09:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121690">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
عربستان سعودی قراردادهای جدید با شرکت‌های مشاوره غربی را متوقف کرده و برخی پرداخت‌ها را به تعویق انداخته است، زیرا این پادشاهی با کسری بودجه فزاینده و تأثیرات اقتصادی جنگ با ایران مواجه است، گزارش فایننشال تایمز.
🔴
این پادشاهی در چارچوب طرح چشم‌انداز ۲۰۳۰ خود، هزینه‌ها را محدود می‌کند و به وزارتخانه‌های سعودی دستور داده شده است که بدون مجوز ویژه از وزارت دارایی، قراردادهای مشاوره جدید را تأیید نکنند، در حالی که برخی پرداخت‌های فاکتور حداقل تا ژوئیه به تعویق افتاده‌اند.
🔴
عربستان سعودی قبلاً پروژه‌های عظیم و پرهزینه‌ای مانند نئوم را کاهش داده یا به تعویق انداخته است، در حالی که نگرانی‌ها درباره هزینه‌های بیش از حد افزایش یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121690" target="_blank">📅 09:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121689">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
دیدار مجدد وزیر کشور پاکستان با عراقچی برای بررسی پیشنهادات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121689" target="_blank">📅 09:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فایننشال‌تایمز به نقل از وزیر دارایی فرانسه:  ما نمی‌توانیم ذخایر نفت بیشتری را بدون دانستن اینکه این درگیری چقدر طول خواهد کشید، آزاد کنیم.
🔴
حتی پس از بازگشایی تنگه هرمز، چندین هفته طول خواهد کشید تا منابع نفتی به اروپا و آسیا برسند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121688" target="_blank">📅 09:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بلومبرگ: ادامه بسته ماندن تنگه هرمز تا ماه اوت، خطر رکود اقتصادی نزدیک به رکود سال ۲۰۰۸ را افزایش می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121687" target="_blank">📅 09:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
فاکس نیوز اعلام کرد که جمهوری خواهان در مجلس نمایندگان آمریکا رأی‌گیری درباره قطعنامه اختیارات جنگی رئیس‌جمهور این کشور را به تعویق انداختند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121686" target="_blank">📅 08:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU2CjU6jnI5WUt_OErBp3aAblK1Go9AtbxLBKYPf1JX_lqqg7QZGQL5m_9zfuLAQXRCywjvJEdlUv8CD4aZ4XsH31R62K1Exb2opqBIPbBKuZrJnPC5_9IUKOFPLq8OS9D6HcRNHz1XldRSGyP-c6XdpMitw9buhomTXudJNUS52WMxzxQOMJ0BtfvmHMFziAi9xHj6V8ieUpBIx69y9KlmMLxzOMWwKyyewt8v0YHw6oLMet-OO82ypKCGETB1hUihVcQ9bW1vwxvte4XsMgrz47cdG96QxBZ9Lv4OKWUI27rWTm9OzuNNKz3lTtDNGoYg1jMQVziXfdL-KE6_REQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کپلر: احتمالا هزینه واردات LNG ژاپن از حدود ۱۰.۷۴ دلار به ازای ۲۸ مترمکعب گاز طبیعی در مارس به حدود ۱۷.۵ دلار در ژوئیه برسد.
🔴
این افزایش تحت تاثیر تاخیر در انتقال و رشد قیمت گاز در آسیا رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121685" target="_blank">📅 08:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121684">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
قیمت نفت برنت با افزایش ۲.۳۸ دلاری (۲.۳ درصد) به ۱۰۴.۹۶ دلار در هر بشکه رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121684" target="_blank">📅 08:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121683">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بلومبرگ: ایران حدود یک میلیارد دلار به توان پهپادی واشنگتن خسارت‌ وارد کرده
🔴
ایران از آغاز جنگ بیش از ۲۰ فروند پهپاد MQ-9 Reaper متعلق به نیروهای آمریکایی را منهدم کرده که حدود ۲۰ درصد از موجودی پیش از جنگ پنتاگون را شامل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/121683" target="_blank">📅 08:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سرپرست وزارت نیروی دریایی آمریکا میگوید ایالات متحده ارسال محموله‌های تسلیحاتی به تایوان را به منظور حفظ مهمات مورد نیاز برای جنگ با ایران متوقف کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/121682" target="_blank">📅 08:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
عمان، متحد ایالات متحده، پیش از این علناً همکاری با ایران در مورد تنگه هرمز را رد کرده بود، اما اکنون در حال مذاکره در مورد دریافت بخشی از درآمد است. دیروز، ترامپ ایده پرداخت هزینه عبور از تنگه را رد کرد: "ما می‌خواهیم رایگان باشد، عوارض نمی‌خواهیم. این یک آبراه بین‌المللی است."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121681" target="_blank">📅 08:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
لبنیات از امروز 20% گرون شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/121680" target="_blank">📅 01:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121679">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AO2mn9U1ZURPSRU6fEyUBJreOOf7jQtwKhg9IsStcVNj_0U2jI9KToeHk_ok1QOb-OAiDivQ0xkV2ZnZqF1DakRz6RaNc7L7AXiQEfdgXcvb-AZK62ueiD1uLl31ohaGN98ZG8lOFrPYjOnHGokRM1HCzHijaSnJO562robnh_lSsGm7YaHEpmsyTd_yB6iqoO-XH1GWgTi_HhJlo6AQ-PXqPNRAFCGqRaBwP5bOgzC3V9qt6y3yvnNBhZyj-2s4__mWXCwVZ5HzhwJCs_Mw368Ajm-QqtEjVOxxonaTsO0zgmmd5M20qUQ4iMB0q1jj-sx6S4_z0vwao4JGDOzx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بسته چیپس ساده شده 525 هزار تومن!!!
هر دونه چیپسی که میخورین 3 هزار تومن ناقابل.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/alonews/121679" target="_blank">📅 01:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121678">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/288e58579d.mp4?token=XJG_C-uks9JwV6XHCHuQ0UFg0VpURnbhenKy9vFz6UbZoBuFwGqS7SRHxfyodrlk3DgumP1fnGmNsiJtvH5YLAXxVNZva_xX4DncWeU9nmRkXzSdx3q5iQzC5BbhM7w-oBZ_SvOxikFNegRoW7ulswOTVjZqmpl6SCa5fpefTv8H1DVdQDR2vCdOji3QGvYXXNYjqwSOG8QcVd702VOX-umctHK_XbB5D0QposbXAmMhsT2AlYCFt9z7Nak_RjOhg78wqP16zINPctZXyozOJfu6Q41iT0YYVjrOF-9INeGFUJJ4wbT28WQU84z2IhxBGB1CCDVdqJ09yklDpUZSkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/288e58579d.mp4?token=XJG_C-uks9JwV6XHCHuQ0UFg0VpURnbhenKy9vFz6UbZoBuFwGqS7SRHxfyodrlk3DgumP1fnGmNsiJtvH5YLAXxVNZva_xX4DncWeU9nmRkXzSdx3q5iQzC5BbhM7w-oBZ_SvOxikFNegRoW7ulswOTVjZqmpl6SCa5fpefTv8H1DVdQDR2vCdOji3QGvYXXNYjqwSOG8QcVd702VOX-umctHK_XbB5D0QposbXAmMhsT2AlYCFt9z7Nak_RjOhg78wqP16zINPctZXyozOJfu6Q41iT0YYVjrOF-9INeGFUJJ4wbT28WQU84z2IhxBGB1CCDVdqJ09yklDpUZSkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرمله در صدا و سیما: دلم واستون میسوزه ولی دوستون دارم، اما این‌بار بزارین فراخوان بدن ببینیم کت تن کیه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/alonews/121678" target="_blank">📅 01:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121677">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGkotWEIlxR-vy-c5zTOZtDzyp8OdKyRZEADGcIbunsT_FHefXEc9VdJA8SS-OhXDyTHyFQZdoSceg1sziujvgtqrCMPlDLQ4UZbsegeOqxQhh4TCFMUwGd3YQouz_xzjZkmY_n06_VInoIW9b-9kXwierkA7-iKwEkmzregU2VJ3Hb4PBE7HUSkx-3we_mqloGCAcUnQd67o5BswJKIEphoqjYft4EqDJoIe_gPS5946NfoPYQW3wuU6WGpqZDwBGFBo0oQCy2-YSiQ2MG2HkdBBIsqA7ZJOxZqcy8j8tH7_ucG3jFBxbKcA3hyKX9erJoSF6zONrqKAc0olk-AxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱ خرداد تولد ترامپ هست
🔴
بفرست برا خردادی‌های مودی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/alonews/121677" target="_blank">📅 01:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121676">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
منابع خبری از شنیده‌شدن صدای انفجارهای مهیب در دیرالزور سوریه خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/121676" target="_blank">📅 01:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121675">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ایسنا: منابع پاکستانی به برخی رسانه های مستقر در اسلام آباد اعلام کردند در صورت به نتیجه رسیدن گفت وگوهای وزیر کشور در تهران، فیلد مارشال عاصم منیر فرمانده ارتش این کشور به تهران سفر خواهد کرد اما
آخرین خبرها تا پنجشنبه شب حاکی از آن است که رایزنی ها بر سر معدود اختلافات هنوز نهایی نشده است.
🔴
منابع پاکستانی اعلام کردند
سفر فرمانده ارتش پاکستان در صورت نهایی شدن چارچوب مورد نظر میان دو طرف انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/121675" target="_blank">📅 00:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121674">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e48e83426.mp4?token=UNFw2Vt7zcgKRYglyYRFSjGZdk2nHenhDtOwW3Z8F_yO3nQpTeMmV2PhbZlfcvGRXOw-KViFGMnrITn_b_kKiew5kg4QMWXXBlOMrJftDRVa69OdNOY4AQWoN0Vg44Vf3t2SKwMuREybV28wSh9_wb2dUuydM7Z8SFeloC7u6mVxlAd3amL6-0tQ69547BkIa6ZEok8nvJP5ht7T8G2byz6qguauEfw6K0sbjlKKRPAMGlBThZS7bIlte5B1Iq0nbMVxoYjheC-aUDMcDqNab1DCKr0pjYTcIJJp1IDsHKj246uu4HmvLkEBiNGi2usEfnI_6SbLlvs9cGjoaVM9Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e48e83426.mp4?token=UNFw2Vt7zcgKRYglyYRFSjGZdk2nHenhDtOwW3Z8F_yO3nQpTeMmV2PhbZlfcvGRXOw-KViFGMnrITn_b_kKiew5kg4QMWXXBlOMrJftDRVa69OdNOY4AQWoN0Vg44Vf3t2SKwMuREybV28wSh9_wb2dUuydM7Z8SFeloC7u6mVxlAd3amL6-0tQ69547BkIa6ZEok8nvJP5ht7T8G2byz6qguauEfw6K0sbjlKKRPAMGlBThZS7bIlte5B1Iq0nbMVxoYjheC-aUDMcDqNab1DCKr0pjYTcIJJp1IDsHKj246uu4HmvLkEBiNGi2usEfnI_6SbLlvs9cGjoaVM9Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوتی بزرگ در صدا و سیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/121674" target="_blank">📅 00:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf33652fc9.mp4?token=QbIYR2znkqKn9sfcJ0DgUsY30qd9Af-kjNHcLTgEj7_cYYHdbx0N9ARKvxsIq8ra0_tBY3UjQnhXoU_8WP39XgWuFaCiE3hQr7sOVuAMLHQh8_1mu4LWAUCr_Wa6X1qYJHsFaV_TTvjShnUZper4ABs7Z3toawz6bJ-OSnD9PJUwPAU2OEk6XB3V7cvHPVZgd_iTLpsB69k7RTf-xuJ6aAztEC7KK2-sZxydViOw_BSgDzXV3CP9PJKdb28ju7VZ2Wods3U-P-08vOMBRil2we2I8qvp_-BktkWNgsOwFzxeZu4hMfD_qoYrPmCWS8JEZJnyVxfTWrkQA3i00AQ1aTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf33652fc9.mp4?token=QbIYR2znkqKn9sfcJ0DgUsY30qd9Af-kjNHcLTgEj7_cYYHdbx0N9ARKvxsIq8ra0_tBY3UjQnhXoU_8WP39XgWuFaCiE3hQr7sOVuAMLHQh8_1mu4LWAUCr_Wa6X1qYJHsFaV_TTvjShnUZper4ABs7Z3toawz6bJ-OSnD9PJUwPAU2OEk6XB3V7cvHPVZgd_iTLpsB69k7RTf-xuJ6aAztEC7KK2-sZxydViOw_BSgDzXV3CP9PJKdb28ju7VZ2Wods3U-P-08vOMBRil2we2I8qvp_-BktkWNgsOwFzxeZu4hMfD_qoYrPmCWS8JEZJnyVxfTWrkQA3i00AQ1aTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه روسیه ماریا زاخاروا: زلنسکی به احتمال اقدام اجباری علیه ترانس‌نیستریا اشاره کرده است.
🔴
او به کل جهان تهدید می‌کند، نه تنها ساکنان ترانس‌نیستریا بلکه فضای اوراسیا را نیز. او فکر می‌کند که شیطان را از شاخ‌ها گرفته و محکم نگه داشته است.
🔴
او قصد دارد با ترانس‌نیستریا برخورد کند — هرگونه تجاوز به هموطنان ما در ترانس‌نیستریا بلافاصله و به طور مناسب پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/121673" target="_blank">📅 00:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121672">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/964a3a806a.mp4?token=FNG6n1YsElJhQdpF89OxMO2EGXgn44aU_Vjaer59lSoo5SKzsd0H5m6gV7YG-_PL8g6y-qk-VzeBgLUD_Ta2_d-tN23xYfNjE3fWToXwNcKBW_-j0N9-prCIg8pSsQmo6c1TC-g_Pwuoz45u1w7O799vA6estleBlwa4qhdgeRae8xWvn0XFBMoTt4Je3BgXWlZBXWapKkWbi6IS8TcSm37ou6stKBPVR15Fz-ZKc4KDQQKs_M5nDdGLUWtbx0-PKssjL8zZKEXhy9GG-iozu-TX7i6ThuBWSV-HuxjnsunDcN5K311DR-6rUaGwv2f50xFVP6nxzy0Ibfi7ycjq5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/964a3a806a.mp4?token=FNG6n1YsElJhQdpF89OxMO2EGXgn44aU_Vjaer59lSoo5SKzsd0H5m6gV7YG-_PL8g6y-qk-VzeBgLUD_Ta2_d-tN23xYfNjE3fWToXwNcKBW_-j0N9-prCIg8pSsQmo6c1TC-g_Pwuoz45u1w7O799vA6estleBlwa4qhdgeRae8xWvn0XFBMoTt4Je3BgXWlZBXWapKkWbi6IS8TcSm37ou6stKBPVR15Fz-ZKc4KDQQKs_M5nDdGLUWtbx0-PKssjL8zZKEXhy9GG-iozu-TX7i6ThuBWSV-HuxjnsunDcN5K311DR-6rUaGwv2f50xFVP6nxzy0Ibfi7ycjq5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس دفتر کاخ سفید در امور سیاست، استیون میلر: تقسیم سیاسی اصلی در آمریکا امروز بین دیدگاهی از آمریکا به عنوان یک کشور جهان اول و دیدگاهی از آمریکا به عنوان یک کشور جهان سوم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/121672" target="_blank">📅 00:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121671">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d5f964b2.mp4?token=YmYbkPLBj5pQMLe_AhdZmKvsHjOkGL-9UdpN0GKVcGBTxOUU5W63de6T4Z9oa0o-jakGi2j1v2qiqsB7jpa-_asG62SZyLjF3TU190sBJVJSgaqHj4TGVBjB8LfIr6DHubUp1huYG7o5s1gU-BfyHul2sP7pTXz6v6aY1tqs37qFG9v1oNCkFWmfGU89y953U5ObAIhOxmcb3mEMxN4CdaW9L8RmoMAVSjW4b98Vu3WEeV29c0UiTXUiH7aMeZmW3aj1Yjmt9hTQkWbot9NgibRKu8uDm4bGWf8XTySUwKGOooSDKrA3hvPdpVq4LnBpoGk1ORbdG1cg_u068lmMeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d5f964b2.mp4?token=YmYbkPLBj5pQMLe_AhdZmKvsHjOkGL-9UdpN0GKVcGBTxOUU5W63de6T4Z9oa0o-jakGi2j1v2qiqsB7jpa-_asG62SZyLjF3TU190sBJVJSgaqHj4TGVBjB8LfIr6DHubUp1huYG7o5s1gU-BfyHul2sP7pTXz6v6aY1tqs37qFG9v1oNCkFWmfGU89y953U5ObAIhOxmcb3mEMxN4CdaW9L8RmoMAVSjW4b98Vu3WEeV29c0UiTXUiH7aMeZmW3aj1Yjmt9hTQkWbot9NgibRKu8uDm4bGWf8XTySUwKGOooSDKrA3hvPdpVq4LnBpoGk1ORbdG1cg_u068lmMeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مخبر : اروپایی‌ها چپو راست برای عبور از تنگه هرمز به ما پیام میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/121671" target="_blank">📅 00:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121670">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
آسوشیتدپرس: احمد وحیدی، فرمانده سپاه پاسداران، به یکی از چهره‌های اصلی در مذاکرات تبدیل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/121670" target="_blank">📅 00:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121669">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نیروهای پشتیبانی سریع تحت حمایت امارات متحده عربی فیلمی منتشر کردند که حمله پهپادی به یک سامانه هیسار-آ ساخت ترکیه که توسط نیروهای مسلح سودان در نزدیکی منطقه راهید النوبا در شمال کردفان عملیاتی شده بود را نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/121669" target="_blank">📅 00:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121668">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku1ReLucV4JNsVNwk_XXqinRHI2QpaUYJfhaXEgfvMVakoY5me9R_9Wgb1C8NHYOAi9xHbumOV84fz-7QW1d5TKXazCjIVRTwvTqfYJXilZM5X8trdnoZfiGxaKg_bhcVbSdMFWs6FEDJkmQD3EzPSfKV_sQQrwLUFhDh1j1NgjZsa68fVZJzN0PVCWZgqbQzdTrAYeClnuC0x9OzxriVntkOWbh_V8BEcRTCMDg8WOjb1DedmQbBYvqaUr2VU9Mz3yf8i6yMDzXFdLJMJlSqwUd8fd5v-0ROazM0BBbSg9c1UXNVUPN9_8b1nzL3k-C4XD4zV2CvPguHsENEbCPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیواری به افتخار رئیس‌جمهور ترامپ، معاون رئیس‌جمهور جی‌دی ونس، و وزیر امور خارجه مارکو روبیو در کنسولگری جدید آمریکا در نوک، گرینلند نصب شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/121668" target="_blank">📅 00:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121667">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
یک مقام ارشد کاخ سفید به پولیتیکو گفت دو هدف اصلی مذاکرات با ایران، جلوگیری از دستیابی ایران به سلاح هسته‌ای و باز بودن تنگه هرمز برای تردد آزاد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/alonews/121667" target="_blank">📅 00:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121666">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1oT_VvKQGTaEq0dbcH1bXaKPuItW2DfVHrdt-Y-OwrsPdKjis0rq4FIGeUmFwXYZEwGDHap22gJ_ieHR8lXPF0EdScw8gMXCOKddKFD25oQJJi7_QBdjyD7oNGrYpJYlVSf_wuqGzVNSSSFq8OKGzol-orahCBJv5ck_arqiXaZbTUcBJ30tBcAlNXhY5buI-ZDH30xcvtWQltXkDWJ48vRv2oGUInjwZqMWNkB1ZppW_CUUAZJ1e5Mie0AaZ1qeUnIigocO498jcOvRxH1Y9zz_Filqa6nr3wsFDrT5Iyg9pjvn9i3ncFcgz26U6keD8ubuacb5rKrLd5NyGdrfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : بعد از اینکه کارول ناوروتسکی تو انتخابات لهستان برد و رئیس‌جمهور شد
🔴
و با توجه به رابطه خوبی که باهاش داریم، آمریکا قراره ۵ هزار نیروی اضافه بفرسته لهستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/121666" target="_blank">📅 00:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121665">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlwMA_5hOVksezcqBlW0IGIBNlp36ReSNNiHWtvI0NXiKShRzjsrXBF9mdD2te3KceRJz-rt-J9tKT1RxtrACwyjIfesAwxdtpdFPzqmxC2dsDLZ44qQ4k5iLrQk6ozTCRngtmCquVrW88R65cnrZ73rY2t53NKMwmz1zpqzTuxP9w4QL-jWclXygI9qMBDq5MN_iuS4cMgXGKwpObuA8iRgV6ScozSs4gwY43o6uTcQdlBo-xL79b5sHvkgcOb4KvXrbqOorBfL1LYzjNFd7c0sbCnn0O843uUE2lV2e1WUYCh42bcw20zHKuNANtdVgU3dwMJeexhqez4YsZ0KFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گرینلندی‌ها در نوک با پلاکاردهایی که روی آن نوشته شده بود «بله به ناتو، نه به پدوفیلیا» دیده شدند.
🔴
یکی از این پلاکاردها توسط یک معترض در بیرون کنسولگری جدید آمریکا رها شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/121665" target="_blank">📅 00:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9214fdfc48.mp4?token=NKmzKUHW6bmephLuaf1OagQAKoNuIADqK-9gPEA9afhE92RHuV_wrSjfOZZFeVgg0_X7Y-1f7IUc996UJ94ycGxA50d5ZhlCfIavujWLyHvkwlXJRJiE1th5E4BxAM01LLn9MsaoYHGGha3G7KrkD4EYiawL2yFp-sxC5QXx3jbst0pTiPSTGqNvNRLJS91SEeQ0cT8u_eKHf7zXfS623erert1gRYAR4aaqBaQZwmvWXgMVqaEIcFwW510ieF_P-KhSNKGHKv5JeGvz6TChGo8zM-56-CwlanwN41VsCwIRZkdnFAWRbiZ9AKm17D2E-sPI0mvuBe512EVnHGT1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9214fdfc48.mp4?token=NKmzKUHW6bmephLuaf1OagQAKoNuIADqK-9gPEA9afhE92RHuV_wrSjfOZZFeVgg0_X7Y-1f7IUc996UJ94ycGxA50d5ZhlCfIavujWLyHvkwlXJRJiE1th5E4BxAM01LLn9MsaoYHGGha3G7KrkD4EYiawL2yFp-sxC5QXx3jbst0pTiPSTGqNvNRLJS91SEeQ0cT8u_eKHf7zXfS623erert1gRYAR4aaqBaQZwmvWXgMVqaEIcFwW510ieF_P-KhSNKGHKv5JeGvz6TChGo8zM-56-CwlanwN41VsCwIRZkdnFAWRbiZ9AKm17D2E-sPI0mvuBe512EVnHGT1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گرینلندی‌ها امروز در مراسم افتتاحیه کنسولگری جدید آمریکا در نوک تجمع کردند.
🔴
صدای مردم گرینلند شنیده می‌شود که شعار می‌دهند: «برو خانه، آمریکا.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/121662" target="_blank">📅 00:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS9dZMfJbe6UdeqKbqKF0Y98PD537Dj9BG3lXJEhTCbvdMc7PtPPfFB-TU_Cqs9i-6tBmK9Zm_fpBwjdWVMFgMWZzGD5Sp82mvpiGpJ5c10-7eTFBMWxRn26rlYPsESUQ7xxVsRXJSpjW2_zy70j3n2rVrBKHFtaFaVlRwXzSZsderf4NSZl3IQ53YtUTUc5Yce0_VS17CsGYK2FHNXEJkpHk0EgNwF2N1jSsl-cYy4eNa8MSh2EGUKu-VE3Aza7g81lPHGBsLX9s208Aezs1q0e7kQYsRT1LD6TLU1Dna7SPguyG-57w0NQSWrVxSuY56rqVmx9KL7FH44zei7E4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش اکسیوس، تنش اصلی بر سر صلح میان آمریکا و ایران، مخالفت نتانیاهو با هرگونه توافق است. او خواستار ادامه جنگ و شکست کامل ایران است، در حالی که ترامپ از مذاکره و آتش‌بس ۳۰ روزه حمایت می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/121661" target="_blank">📅 23:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsG5PkoWGFJt5mKpjJ4cJPj5rFxtWI59ROLA8hNk53LEBQwYL2Tdqp6Mp63XJPmaN8Zux2pVEwm_f8Oxh4dEB7Bm4MbKV-MwBMOdDEI8Vc7Xu43bl_a9EcLXiaNcTNMDxMUWapz3QFVMaIXnMMQzgAOQWI2yiN8yWKmCixDc3TaVL2YVweS20hvh3qt-TToUy0bF8r_tpEBgszE-xoa_ny62doInVJSK-yI7fCUemBZ5WcFpjDaZBEZ6JOcR-ebHCu1a3Hr3My2LfojjYMast44UtC6aHzg0A9LZI8I9dAZvkGkD7MHv7LwpdZ19RAoFAog64YUebOfoTPbhRAK5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسمییییییی؛ النصر قهرمان لیگ عربستان شد
کریستیانو رونالدو بعد از 3 سال ، اولین جام خودش رو با النصر به دست آورد
😍
@AloSport</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/121660" target="_blank">📅 23:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
شبکه CNN: ترامپ در کوبا به دنبال چیزی است که در ایران از دستش رفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/121659" target="_blank">📅 23:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
اشتراک v2ray
🗯
گیگی 150,000 تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید : @v2safeBot</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/121658" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzBT-_SHkI9BWqSYoKGvmUKjRXBLhsHEX7v7B2arCi9usaTln6NL9oXoDr8j7vJJJBh8zcrAwe1q863HNVcibjjzKA3ki5tpgR3B3B9_tOvS1nABbrdXdQ5mY9ldhH4gpeaUDMSzQLROaQ_t5-M1I156BOpFkC79qJxJx3YbhGsuJ0xg1TdnJxI79gUhF9COxe1Crv-M3SF5tecYjJjNk2oCg-44EJgUc7h2pStEM48Ps9NrT_rtiIkFwLPBRURbiRQ93QXsbyEjvkTUSk3z6EkrRZZkePHB3Jx6XRu6LGsSw-1cQrg2sOpgq3bO9vQ8192bnVRgvmNriN7KXPWVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray
🗯
گیگی
150,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید :
@v2safeBot</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/121657" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121656">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
یک منبع ارشد ایرانی به رویترز: شکاف‌ها کاهش یافته اما هنوز به توافق نرسیده‌ایم
🔴
غنی‌سازی اورانیوم و تنگه هرمز از جمله نقاط اختلافی درباره توافق هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/121656" target="_blank">📅 23:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyEshKfwoe1d7aJGrjgKGv8WguDWzjW6ruRYsLuwAs4JNYLEYT57xMyEtSAUVxxisIYLaCWZjECUKaPZWphlupg7Pvn58oDKxJTGPd1RReXRxr0fnj_jDFQXcwgn4eCejosYLF5lieEH1R2slir5NdGpOiNaNtkrv0REaARGfv0Fx-nK5dGWbHlZGqjhs4dRW0RgbacnYHIjjk4YFP1x5z7Inq4MV174iFoPI07vxvpuuLc4-OsDKzKb9y2uT8SXh9hSDeHRzBYg0EpoawnBzSgVZY31wK4qth7cyqcLpHUVUecV_P7rc-UnB5UUsHxsphKUvJr8Wr0Or-wfBitjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: تعویقِ سفرِ «عاصم منیر»، فرمانده ارتش پاکستان به تهران _پس از انتظارِ ۲۴ ساعته_ نشانه‌ی مهمی‌ست!
🔴
«آمریکا» اصرار دارد «بحث هسته‌ای در شرایطِ فعلی، مذاکره و پرونده آن بسته شود» آنهم با «سختگیری هسته‌ای بر ایران!»
🔴
ولی «ایران» مذاکره در بابِ پرونده هسته‌ای را منوطِ به پروسه‌ی اعتمادسازِ ۳۰ روزه‌ی «پایانِ جنگ» و «رفعِ محاصره دریایی» می‌داند!
🔴
در موضوع «تنگه» هم آمریکای‌ها علی‌رغمِ «پذیرشِ مدیریت ایران بر تنگه»، حاضر به پذیرش موضوعِ «اخذ عوارض از تنگه توسط ایران» نیستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/121655" target="_blank">📅 23:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121654">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رئیس ارتش پاکستان، عاصم منیر، سفر خود به تهران را لغو کرده است. انتظار می‌رفت که او پیام‌هایی بین ایالات متحده و ایران رد و بدل کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/121654" target="_blank">📅 23:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
یک مقام ارشد ایرانی به الجزیره گفت که مذاکره‌کنندگان بسیار به حصول توافق نزدیک شده‌اند و در حال حاضر روی پیش‌نویس متن کار می‌کنند.
🔴
همزمان، منبع دیگری به الجزیره گفت که برای قضاوت درباره دستیابی به یک توافق جدی و نهایی، هنوز خیلی زود است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/121653" target="_blank">📅 23:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121652">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پزشکیان: سر خم نخواهیم کرد، وزرا و کارشناسان ما شبانه روز سرکارند، بدون حتی یک روز تعطیلی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/121652" target="_blank">📅 23:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مارکو روبیو: کوبا قادر نخواهد بود که ما را منتظر بگذارد یا زمان بخرد.
🔴
همانطور که در مورد ایران گفتم، ترجیح رئیس‌جمهور ترامپ همیشه توافقی مذاکره‌شده و مسالمت‌آمیز است... با کوبا، احتمال وقوع چنین چیزی زیاد نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/121651" target="_blank">📅 23:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121650">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
مارکو روبیو: شما درباره ابولا از من سوال می‌کنید. مهم است، اما ابولا در آفریقا است.
🔴
کوبا ۹۰ مایل از سواحل ما فاصله دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/121650" target="_blank">📅 23:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پیت هگستث:با بودجه نظامی ۱.۵ تریلیون دلاری رئیس‌جمهور ترامپ، ما غول خفته را بیدار می‌کنیم و زرادخانه آزادی آمریکا را می‌سازیم — و این کار را به‌طور مسئولانه انجام می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/121649" target="_blank">📅 23:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ناتور پاکستانی: مذاکرات ایران و آمریکا در مسیر درستی پیش می‌رود
🔴
«افنان الله خان» در اظهاراتی با اشاره به اینکه اسلام‌آباد به تلاش خود برای دستیابی تهران و واشنگتن به یک توافق ادامه می‌دهد، تاکید کرد: مذاکرات ایران و آمریکا در مسیر درستی پیش می‌رود.
🔴
به گفته این سناتور پاکستانی در جمع خبرنگاران، مذاکرات میان تهران و اسلام‌آباد و همچنین میان پاکستان و آمریکا ادامه دارد و ما هر کاری که بتوانیم انجام می‌دهیم تا طرف‌ها را پشت میز مذاکره بنشانیم، اختلافات را کاهش دهیم، به توافق برسیم و جنگ را متوقف کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/121648" target="_blank">📅 22:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121647">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع دیپلماتیک بلندپایه پاکستانی: فرمانده ارتش پاکستان امشب به تهران سفر نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/121647" target="_blank">📅 22:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121646">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭕️
⭕️
اپلیکیشن‌ها را فقط از Google Play یا App Store نصب کنید.
🔴
فایل‌هایی که در تلگرام، کانال‌ها، گروه‌ها یا از طریق لینک مستقیم دانلود منتشر می‌شوند، اگر از منبع معتبر نباشند می‌توانند خطرناک باشند.
🔴
نصب این فایل‌ها ممکن است باعث شود اطلاعات شخصی شما، رمزها،…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/121646" target="_blank">📅 22:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121645">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnK4tkSuQd4v5saERds8h6eTpSh2Qkc8EmnWePTtNycPAtONASe9Ftj_sErHmGjb9lVjys2IPSKDe9PHrNnCHrSXJcWn3ynqWPr2jIDR-MLMMBKutL3z1UWTFQL5voFUO4Yliv_AAxxTZtE2Xg7pZ5cGhHksWj8dMg39bqVQpQJmivPRf56oCU2UIcrNBcaAdIn67cyXseOwGuLt7cQIYjh7Mz8ayynovGDYj29-nDyuQDZZCQMP5hV6DfR-Q25oiHUtFT14n5wYNOejgyqImo2pliWs6OUYCcXJPrKa-FzgAADE7lhKVdKt4gn7e4jw9DO2x2QKZrge22Xd9RFxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌ی تعداد بالای پهپاد اوکراین به روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/121645" target="_blank">📅 22:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121644">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بهاروند، معاون حقوقی پیشین وزارت خارجه: چین محتاط است و تا از نتیجه کاری مطمئن نباشد قدم برنمی‌دارد؛ فعلاً چنین وضعیتی را نمی‌بینم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/121644" target="_blank">📅 22:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121643">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وال‌استریت ژورنال: کویت بر اثر جنگ ایران منزوی شده؛ با بسته شدن تنگه هرمز، صادرات ۲ میلیون بشکه نفتی روزانه این کشور متوقف شده و واردات مایحتاج از مسیر زمینی عربستان، ۶ برابر هزینه حمل دریایی تمام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/121643" target="_blank">📅 22:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121642">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
یدیعوت آحارونوت: تصاویر ماهواره‌ای نشان می‌دهند که پایگاه رامات دیوید اسرائیل آسیب دیده و احتمالاً به پایگاه نواتیم و پایگاه دیگری متعلق به واحد ۸۲۰۰ و پایگاه‌های دیگر بر اثر حملات موشکی ایران خسارت وارد شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/121642" target="_blank">📅 22:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121641">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رایزنی وزرای خارجه قطر و مصر درباره ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/121641" target="_blank">📅 22:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121640">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رئیس سابق میز ایران در سازمان اطلاعات نظامی اسرائیل: اینکه ترامپ به رغم مخالفت صریح نتانیاهو، با ایران مذاکره می‌کند، نکته‌ای قطعی است
🔴
تا زمانی که رئیس‌جمهور آمریکا باور دارد که توافق قابل دستیابی است، اصلا با نخست‌وزیر اسرائیل همسو نیست
🔴
از دیدگاه نتانیاهو، تقریباً هر توافقی با ایران خطرناک تلقی می‌شود، زیرا آزادی عمل تل‌آویو را محدود خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/121640" target="_blank">📅 22:21 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
