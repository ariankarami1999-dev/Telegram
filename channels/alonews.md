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
<img src="https://cdn4.telesco.pe/file/TsHtSeINuSNnBx8tegBWfWK5_PwlLgkeap7aLRPX0k8-f8LTVDZuiCFHffd_kK2reAGRcsRHyU-FxJ9hFyBltcin3p6gwmU3BiKRXtZ8mPFjvslGkk6T8xmDU-grweQNlHc1bJBimdntzBzMkoARG0qOCe6coBuktnPGhEQ0eyV7bR0_nAsaYlecMOCvf0tqJ0m17h4kQ31aj8vn_Zp_LJiQfxxXOWiRTmhcwhE2yIHgRpzYX9_peQ6lvJzUPz8JHY_3f06D73_OS-S3fUVdJVA_okdz6xebKEugyi-AXbl-T4c-Jv8bbdRFktpuNzPTzwodfGE6KqE3XcY1zQ2sww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 12:02:17</div>
<hr>

<div class="tg-post" id="msg-135008">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری / ترامپ: هفته آینده خاورمیانه تغییر خواهد کرد و همه باید برای آن آماده باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/135008" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135006">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrXh3jGkv5134nK0Q4WgS8tmbdXBeWAwXM-3xncZ5URNWU0cambLck6CWzWIdqbJFIBDQ67tAGvq8YVcFU_al1SQiormV-E6gUYqqIjpyEWX544S8mvS3mMyvf2K0cHX9EJGYyTODuEExXEfZ4MgpepMs92-dnVDFOGVX2CS11TgXxsYgolU_HW-yd14bZAzeMKRbEzdK5EOBpFXZIkaEcDzoSei72JoTl4dL-2EURN6jKgDSk4IU8PfoSZ0FmYoMbSeCgF1qlpT_XRDDosQrSJ0EVT2Dagrjw8U-Zn5EeS4zyvLxqztbEM8_yR8Ww_x_54Nhgj0F5ERBYOAOxgYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3xxi48ol-ARpLMPlpx8opcZn91qRPJHQ2NpieQ_2PjINoNjSaqjjhdmOQgGiRSrFBAfFsvTnYp_1onoaEmXlr1Tpyhnmh6ECQ4bpWoVpYgbDG4A_U_zLzmSHmtZ8IjILCxA8_8fyeW2IxmAZutp01laf91lOxuJmdZ9oeNeaIzSpF00oLNOhZ984NzFbrTysiqsfjpbYTVcMSE_4jMczLsB0xsyX4SYn7d3yccnX0XdlyqGXbQ__z_-CDUecdrFFWLuRo69W5Z4sAFakBG-630F3fXZooyi5Vqr4YxQVBAsTolVaA5LZWhfeG4PJw7KLQOkXi72AcLY9h-YaHsFrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پلی که مورد هدف حملات آمریکا قرار گرفت جاده اصلی متصل کننده بندر عباس به لار و از آنجا به شیراز را در بر می‌گیرد
🔴
این بخش از مسیر، یک جزء حیاتی از زیرساخت‌های حمل و نقل کالا به بندرعباس و از آنجا به سایر نقاط است و همچنین به تردد مسافران بین استان‌های هرمزگان، فارس و مرکز ایران خدمت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/135006" target="_blank">📅 11:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135005">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N11mXOvQQGXXOgvoqqmybRqUKOr6G1_0aeCgPM7Bxwdw7ufgOicUkYOiz24gQaVZjCHYlod7WtUBF1Pq0rlfS7S-9kXRND57eFIWRvNNen8boZFrQgsfQXRa5Q0Q9OQB4tTeh7io-Jr88nH5fzGqtXK8ueyPFreSjAyLZ0twQXumoLB9WFSJdJqOOUSWGnDkmy4ASSzRQrWaE_Lt4B414lD7ub1aNk1Jh-OvaFPQ5oMoKbZspFokECBC1EXEXi1-tdsyR49MAyFbdlQa2BklMhQtYp8oQGJCBWoO9z4zM7_n3oKEvjj2NafLpu0Yu6ZfDTE4wstNx737QhW5rtm02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دست کم ده ترابری از پایگاه‌های آمریکا در آلمان، یک پرواز اطلاعاتی از خاک ایتالیا و یک سوخت‌رسان و یک ترابری از آمریکا به سمت خاورمیانه در حال حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135005" target="_blank">📅 11:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135004">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/135004" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qGnWRZFkVSM2mRNt91KXXFTbK082ZI_O3jLwG5D7Hna4aYamfp5OVn12QiETjbygT_HxBwJUwaa2BOkJNsSJe5Poa88wTky5BCBwNfpDWIWv2Nlc-NYFG3xgA0JYv3Rmj4Lcg-3VoALcvv_r5-n0fz_c5Po9Iv_hdOjFk37dpWbLy6c81-HBa4YCjuqNsrpPleosne25AwaynMcgsxGXXtaeJB4hHaAJH2pbg0ggFnIGHaXXxv82cpmnRcCEQaxNHdn-hH9dZ7tIi78mYvHfQY5Iyfa2PyCRAOX3Agv2ccZd7PnpMUnwZtW7zv004NN7ysX7wIQQs5N_qtHZkQ91Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOIAVWzfw1jHZi6MTgl0tmm53L9zgjp9djdi4Tun0l8G4eHVJ_R9rLBVUkeL0qqITcXVg1b_6DEh6c0aY0tVaqrOrUyXRly7dhXAmQ_oibFC_ytSw4QlyjGNV7BIucx81G0UWfGvFRULDLRnlwgs8mEDY-sRWopuXCmV4fdf_bAIYjqjHO2GOBqv5NNXknqdwEqb1zeWAzbrb8uvxfgJKVrbNWxApHy-gFx1LHrp4HLxmI_c6DWVJuEBnjDDhb-GdKCMqgJ-OoY5d89uZshkx8TteRrl0U5g1FEspSpx1nBvSpUdQueWQyQT1C_EmdZTmRvFI_B4GVBv0wXVwVqLgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رسمی : نه رده بندی و نه فینال؛ سوت به علیرضا فغانی نرسید!!
🔴
با اعلام رسمی فیفا، خسوس والنزوئلا (از ونزوئلا) دیدار رده‌بندی بین فرانسه و انگلیس را سوت می‌زند.
🔴
دیدار فینال بین اسپانیا و آرژانتین را نیز اسلاوکو وینچیچ (از اسلوونی) قضاوت خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/135002" target="_blank">📅 11:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135001">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۲ درصد کاهش، به ۳۹۸۸ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/135001" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135000">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFTsyCF-4RjihZFp5G5ox4iJvq6lCZpGjtclfuEdHP2SjFZ1012QsofxjxRjEMajeBehXTGFygnOc8mnUGdUsWIcQogWdUSg_U03mbDIVeKB0fKlykQphWyf4U1ax6GsGf_QQCjaBQDu9F6KYr5_8o7KxBixIawvBIdmAyj0iucauFSuDimgnCB089BGoOVdqpf0vinYMbQdbOlfe9zSTH8OTmHIDJG5jCk0pgZVsUDXO6blaNEghnivf6KPS9AZI12xWwUsTSxtDn83Ub9I0iM1A5DVZwDqWEmKecQ6WKdVI3fQgwd2wKu1-wNCcCebrXZO-3s29pLEne5zLAlLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا صدور گواهی امنیتی SSL را برای خبرگزاری فارس مسدود کرد که این موضوع باعث میشه اخبار این خبرگزاری به مرور از گوگل پاک شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/135000" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134999">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سپاه: چندین جنگنده و سوخت‌رسان آمریکا را با حملات خود منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/134999" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134997">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ec9980c.mp4?token=CgCbj37yBSYhsgzGvatqWGRU9UDXNDC6GUHgqCGTNan61PGp9Bn40m1F0NcTHPRBuqVPNuXVj9MUNOph-9r8MNimECQ-271zWh0UKtSmRyFVovLo41HJULzt1R-HRyDdDiMw3WimZtXLhROyXJaK_slP8WO93LZMFcG7838fG1A3r1uuyU-YqLKGDe1jV3Y7ccH9tdC0T0utJrSjNsuDvrmKNBpiBS4BCbkNepdFSipe6RLshflkhOBq2m4aZQ1oXrdku6UMhCvVUxrnPkw0fOrXS9YETv8TCntcgjDjmz9G7zTnwk_IrhUFlnGYDTjpfBSLUxJv1QSSjZ5q4TtR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ec9980c.mp4?token=CgCbj37yBSYhsgzGvatqWGRU9UDXNDC6GUHgqCGTNan61PGp9Bn40m1F0NcTHPRBuqVPNuXVj9MUNOph-9r8MNimECQ-271zWh0UKtSmRyFVovLo41HJULzt1R-HRyDdDiMw3WimZtXLhROyXJaK_slP8WO93LZMFcG7838fG1A3r1uuyU-YqLKGDe1jV3Y7ccH9tdC0T0utJrSjNsuDvrmKNBpiBS4BCbkNepdFSipe6RLshflkhOBq2m4aZQ1oXrdku6UMhCvVUxrnPkw0fOrXS9YETv8TCntcgjDjmz9G7zTnwk_IrhUFlnGYDTjpfBSLUxJv1QSSjZ5q4TtR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : شبکه‌های تلویزیونی که این سخنرانی من را پخش نمی‌کنند، باید مجوزهایشان باطل شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/134997" target="_blank">📅 11:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134996">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رئیس پلیس راه مازندران: جاده هراز به صورت موقت برای اجرای چند عملیات عمرانی ‌۲۹ و ۳۰ تیرماه جاری مسدود می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/134996" target="_blank">📅 11:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134995">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وال استریت ژورنال: اختلاف میان محافل تصمیم‌گیرنده در ایران گسترش یافت
🔴
‏ گروهی به دنبال تشدید تقابل با آمریکا و کنترل تنگه هرمز هستند و گروهی با در نظر گرفتن محاصره دریایی و تشدید جنگ نگران وخامت اقتصادی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/134995" target="_blank">📅 11:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134994">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
اسرائیل در مورد نقشه ترور به ترامپ چه گفته بود؟
🔴
اکسیوس نوشت: در جریان سفر ترامپ به آنکارا، تل‌آویو به واشنگتن هشدار داد که یک مقام ایرانی درباره تلاش برای ترور رئیس‌جمهور آمریکا در زمانی که او در ترکیه حضور داشت، صحبت کرده است.
🔴
این اطلاعات باعث افزایش تدابیر امنیتی شد. از جمله این اقدامات، جابه‌جایی ترامپ را یک هواپیمای قدیمی‌تر «ایرفورس وان» (هواپیمای ریاست‌جمهوری آمریکا) بود.
🔴
با این حال، مقام‌های آمریکایی گفتند این اطلاعات بر اساس یک منبع واحد و تاییدنشده بوده و جنبه برنامه عملیاتی واقعی نداشته است.
🔴
بر اساس اطلاعات اسرائیل یک مقام ایرانی در گفت‌وگو با همکارانش گفته‌بود که ایران باید تلاش کند رئیس‌جمهور آمریکا را زمانی که در آنکارا حضور دارد، ترور کند.
🔴
نیروهای امنیتی ترکیه نیز این ادعا را بررسی و اعلام کردند هیچ طرح مشخصی برای ترور ترامپ در آنکارا پیدا نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134994" target="_blank">📅 11:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134993">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نظامیان اسرائیلی با ورود به روستاهای «معریه» و «عابدین» در درعا، مسیرهای مسدود را بازگشایی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/134993" target="_blank">📅 10:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134992">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: چین به اطلاعات ۲۲۰ میلیون پرونده رأی‌دهندگان آمریکایی دست پیدا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134992" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134991">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن جانشان را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134991" target="_blank">📅 10:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134990">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
جنگنده‌های آمریکایی صبح امروز، برای سومین بار برج مراقبت دریایی چابهار را با سه موشک هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134990" target="_blank">📅 10:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134989">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134989" target="_blank">📅 10:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134988">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
آکسیوس: مقامات کاخ سفید از گزارش‌های اسرائیل مبنی بر اینکه ترامپ قرار است روز دوشنبه با نتانیاهو دیدار کند، متعجب شدند، زیرا در واقع هیچ جلسه‌ای برنامه‌ریزی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134988" target="_blank">📅 10:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134987">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75dbcaec2b.mp4?token=Przbx_mG6VkZlWvEzCp9XCgMXme7XzWFYwaTjhcWwHkevJycxwLlXG3iP2kLR_tsWwD8_10LJkroa-r1Z-MzMN-iq0FsWFnL7Z_34m_FGQs5-XyS9xa4vnE10q_PpCLZlsaD5Ap56oKzJ6Xl1rbAKbZfUcXCL8aj9z9T6ORC5dkyH_AK5XMn0xMxyoNGrnKsdetOd5eLJY2FE-R14UpQzrZ9eb9aPwN1E0fcrziNiPY1rADEE-KOHA8yUkwdnIEcTT_JblC0kRWE7k3XIhzaSIH-3j_X5Gaf4EyLMRzZzDCwvV4Ui1QPgFqjxN6R9u7_uhIVrGv_ja4-jPzZ_eQdCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75dbcaec2b.mp4?token=Przbx_mG6VkZlWvEzCp9XCgMXme7XzWFYwaTjhcWwHkevJycxwLlXG3iP2kLR_tsWwD8_10LJkroa-r1Z-MzMN-iq0FsWFnL7Z_34m_FGQs5-XyS9xa4vnE10q_PpCLZlsaD5Ap56oKzJ6Xl1rbAKbZfUcXCL8aj9z9T6ORC5dkyH_AK5XMn0xMxyoNGrnKsdetOd5eLJY2FE-R14UpQzrZ9eb9aPwN1E0fcrziNiPY1rADEE-KOHA8yUkwdnIEcTT_JblC0kRWE7k3XIhzaSIH-3j_X5Gaf4EyLMRzZzDCwvV4Ui1QPgFqjxN6R9u7_uhIVrGv_ja4-jPzZ_eQdCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهگیری یک موشک بالستیک توسط پدافند قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134987" target="_blank">📅 10:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134986">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAMpExEY4Kg7hG3PMwOI1LXOC4aXuo7D3DcpsqhAxkh419O1vDujqUDtt-DShIcM91DPw_w3WJAbMbGCzf9PFJT9nra6g2zACohj93gdlfXsmorTG3u2P9nu-AsSK6sGxI1Y8uukEFwWhZ7UZnriKqB2SNFkkSIY8LGV7_zUfavIVoMY12Qx79oAQVHHgLYglieGrQ4sJu4S4DZ_f8J8ghKewkb6_SmWuiN-y75DjuD48chtrlLmmmS2-JzvkS2LoXHx-qc1uS2VFblsZxgeyatKKxQF61d3HtuKn9g5g1EqxHTrLA68OpmXJWxmPJtCNwimxRgFKcNE_a0BkFnDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش رئیس کمیسیون امنیت ملی مجلس به حملات به جنوب کشور:روزگارتان را سیاه می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134986" target="_blank">📅 10:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134985">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY12AjdKxrqXbpWM-qKC_tJooi0Glepan7Gje6JvDk5bL6PC5SuVxdPo65Oe2Z59Jfxqg0_RO-anq-4UH9aRbLwSVgJq2GWQmmwmzfB6w0J_nOzAfsoiN2BwusVJ3xtXzGJKS8e8NoF34jeRTIcV4dHqH9MNTFGxbLlispZKEKlFPNu3KJen6ni4RtHIEqmMIR1sgcy-1-o-XhGr2znO4CoJnpL9oaMFQx_q1pHdeg_TvREOeUHq_eR0J7yYsvteUEkPY189v-Ch4o6GlprnMsH0P9631c3H0-GRF6RpWHVS6ret55KIOchlaRe1tdnadCM1X2T6B7nrPg78SiBSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134985" target="_blank">📅 10:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134984">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / برخی منابع عربی: پالایشگاه‌های نفت در بحرین مورد حملۀ پهپادی قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134984" target="_blank">📅 10:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134983">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57fad8a70.mp4?token=Ypf8bKuvsM1mkhrtPpfb8BM82A7Pw4ka124yfhUv-Nq3U3dKaNEoBWwcT6AMlqc2OUuUFzDxwU02s1hb6eggzA_atanTrCBwNaYCb_7NQuJDbe02B7m5B8yCzf6L5yCnCDhQH9KWygAZuasgbMSFpfFOijYWKB87rhaVLpDbyqlFnyiGWdAGpyDxYQBaq-61X6Jn-piRPEvAfdfLqaJLPjgnWNfPCVC2Qw_YJidNnl5p0qTu9IQmtrc1Aa2haIp-sYp9tm8Xhq_J7mMaJPg5VxJkXKImroizDfzodPH3kJfnTaIspEEdT_Fli8Pi15W_u5Bt8BTfBLhVF7Z64VH44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57fad8a70.mp4?token=Ypf8bKuvsM1mkhrtPpfb8BM82A7Pw4ka124yfhUv-Nq3U3dKaNEoBWwcT6AMlqc2OUuUFzDxwU02s1hb6eggzA_atanTrCBwNaYCb_7NQuJDbe02B7m5B8yCzf6L5yCnCDhQH9KWygAZuasgbMSFpfFOijYWKB87rhaVLpDbyqlFnyiGWdAGpyDxYQBaq-61X6Jn-piRPEvAfdfLqaJLPjgnWNfPCVC2Qw_YJidNnl5p0qTu9IQmtrc1Aa2haIp-sYp9tm8Xhq_J7mMaJPg5VxJkXKImroizDfzodPH3kJfnTaIspEEdT_Fli8Pi15W_u5Bt8BTfBLhVF7Z64VH44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه انفجار سهمگین در بندر بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134983" target="_blank">📅 10:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSiO6Tmwb4BIbmcTdMwsBhNflnK9dZiFSz1_8mOUWy6pvRUFm2fQQlJ-3h3NZnINNTqav5e_TT7WfOCfP5__qzQHax9ntJAhb4OSe8nUb8f52K4il0JqBll182ef7xTzQaZX6sQLPKk5d_Hd69TQKTfn6uy1UhK8GFEB8SMF8UX7Y9GIfFpwdl4TbBgHX1BxtjlTqM8t65lfITyjOa32-c6ts2uPCiCeX0ECXsAgwhUKzDjNnGjX30zfvcZJ-SxTf6DSMK8QXb82Xa1-jdTqnsYBwmVJL8Md6k2xwDgwgG0DU--VvrBDEVKXL63tThFkKj-SIulqgXS2yrOnrozNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a4635a48.mp4?token=oO8-fDu5_d8v-3l53QOeI0ozm4_AGHak-UllQiVNCoN_rxLR0-M0y0dGQKPNoov3qhHD1kFphAK2ZFYOLAzEcbGFVJdrRZY5_TTiAtefxUKEzwVKitLE7MVDmeGIM-uBfpI4Yv3vdXS_Rlmb-N53RpNxqGUQ8uuvsXBQm86ytWaLQYmJGmV509aPulG0kD6faEAEehaemZS8PQ7f_qFOlCcrQffui-gIbhYQdYm1zdKk8LNhwtJtvNDCTIrDTdFS3eHxYLyih1YD7S-XZSNU6-jw6vn_FFlqPijcrZDsA-i0mrSZI_snG2-pTUnLt57ngBDOA_eS49qWocgRj4RzIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a4635a48.mp4?token=oO8-fDu5_d8v-3l53QOeI0ozm4_AGHak-UllQiVNCoN_rxLR0-M0y0dGQKPNoov3qhHD1kFphAK2ZFYOLAzEcbGFVJdrRZY5_TTiAtefxUKEzwVKitLE7MVDmeGIM-uBfpI4Yv3vdXS_Rlmb-N53RpNxqGUQ8uuvsXBQm86ytWaLQYmJGmV509aPulG0kD6faEAEehaemZS8PQ7f_qFOlCcrQffui-gIbhYQdYm1zdKk8LNhwtJtvNDCTIrDTdFS3eHxYLyih1YD7S-XZSNU6-jw6vn_FFlqPijcrZDsA-i0mrSZI_snG2-pTUnLt57ngBDOA_eS49qWocgRj4RzIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام: «تفنگداران دریایی ایالات متحده از واحد یازدهم اعزامی دریایی، در ۱۶ ژوئیه، در خلیج عمان، عملیات بازرسی و تأیید ورود به کشتی M/T Wen Yao را انجام می‌دهند.
🔴
تا به امروز، نیروهای آمریکایی ۳ کشتی تجاری را که سعی در عبور از محاصره داشتند، تغییر مسیر داده‌اند، ۱ کشتی را که رعایت نکرده بود، غیرفعال کرده‌اند و ۱ کشتی را نیز برای اطمینان از رعایت کامل محاصره دریایی مداوم ایالات متحده علیه ایران، سوار کشتی کرده‌اند.
🔴
تنگه هرمز و آب‌های اطراف آن، به جز کشتی‌هایی که سعی در نقض محاصره دیوار فولادی آمریکا دارند، همچنان آزاد و باز هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134980" target="_blank">📅 10:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کنست رأی به انحلال خود داد؛ اسرائیل به سمت انتخابات زودهنگام می‌رود
🔴
پارلمان اسرائیل با تصویب نهایی طرح انحلال خود، به فعالیت دوره کنونی پایان داد و مسیر برگزاری انتخابات زودهنگام را هموار کرد. انتظار می‌رود زمان انتخابات جدید در روزهای آینده مشخص شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134979" target="_blank">📅 09:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سنتکام: مسیر سه کشتی تجاری را که قصد حرکت به سوی ایران را داشتند، تغییر دادیم. یکی از کشتی‌ها که از دستورات نیروهای آمریکایی تبعیت نکرد از کار انداخته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134978" target="_blank">📅 09:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XFD5yRMkvkAUcUaP9irlE8RcN6YwLv7cpfk9fgeyiGry0UiEttwig-OMBdbxiC_8mczLxeLlX8_ghUY1a4oXcU_9zavmRQ5RX6yT8yg7yEA-f1E02PKYJUGoQopywkhzV57UHLBlSUN-hKUiO4BtgFvsxHU-8MXtdFCsNXeclU6UPhT1ZLO-1-F_HjBK1d2_FFufof0DeTdBBFScfV_UaxYEIVS9OvBDlwlY70JXM1pxZk3WB5yVlSxrBt1Q7NzE6_HRmQspjdxPXI23vfW9UaB28zPOh7TA30z2LHeQbpZa9wN9ikR4Q78aB3frLzUePoGI9jT6Z9U3IRUwL9U5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که سه انبار در منطقه نظامی زاید در نزدیک ابوظبی امارات، در نتیجه حملات موشکی-پهپادی سپاه پاسداران در تاریخ 13 جولای (22 تیرماه)، نابود شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134977" target="_blank">📅 09:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ1KQv98nzB2WwxRwFP67tDiYVmLfqOcJK18XJG1qdEqTw29DIdC86bUBaJYmhC8EHor5_SzPAGplJlRrSO7Q8eluZnRUnf63BJyT36AoPy6-I0htBb3k46dkWtHz-1Xi10AN4EWlY3gd9hW6ZRV1ojiNH4BzOnZgfYAxPrttBNeJXgLbi_ZR434SeJ2JEdzXwPz3dwJtyMcuetfFEOayIFwCBjw3E-pxa2p5rD8qZLFBI2N4QaLe442s2f5ts9hQx4mHtQgau4-1KoEZAtpnFUIBA0szLpoDKmfEboMpXxxejrSvc8xa8J2JJFPkuKlUmS--ffsyeulWwI9Bg3W4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردن اعلام کرد سه موشک ایرانی شلیک‌شده به سوی این کشور را رهگیری و سرنگون کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134976" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134975">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
الجزیره: قیمت نفت با تشدید حملات آمریکا و ایران افزایش یافت
🔴
قیمت معاملات آتی نفت برنت به میزان ۱٫۰۵ دلار یا حدود ۱٫۲۵ درصد افزایش یافت و به ۸۵٫۲۸ دلار در هر بشکه رسید و قیمت معاملات آتی نفت خام وست تگزاس اینترمیدیت (WTI) آمریکا نیز ۱٫۰۳ دلار یا ۱٫۳ درصد افزایش یافت و به ۷۹٫۹۸ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134975" target="_blank">📅 09:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134974">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551b40e9d2.mp4?token=i7aYBHjh6GzmIxfyhfK0Dj9qQ_2mgzQIClW378xvpritgYLLVXwW_XdzRoQAWkbtAfsgYbr24gz103IItw0VJMndzJjb92S2g3XJbn3KLRpMJYbUf-kcANGDgoUHGjgjOUqva6Aw1dN-0hPKifEL5les1uA9FDjU-iOnAbeb_QDVHlX8ePOr2JY5gKdPUv_HhjmwOX8aEcy4bJgPpqlzSRC4XhyIp5nsjNySUjnM4nl13oAjcxSWJSB6ljrUtZnosEkBU-3o-XsbxF7_HGPbXRMX8J_9lECYU0SPY6W7yj636u5_MIbLnRdeG9vBxSHhGsWZSvN-GDBSxm_Ltg9kmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551b40e9d2.mp4?token=i7aYBHjh6GzmIxfyhfK0Dj9qQ_2mgzQIClW378xvpritgYLLVXwW_XdzRoQAWkbtAfsgYbr24gz103IItw0VJMndzJjb92S2g3XJbn3KLRpMJYbUf-kcANGDgoUHGjgjOUqva6Aw1dN-0hPKifEL5les1uA9FDjU-iOnAbeb_QDVHlX8ePOr2JY5gKdPUv_HhjmwOX8aEcy4bJgPpqlzSRC4XhyIp5nsjNySUjnM4nl13oAjcxSWJSB6ljrUtZnosEkBU-3o-XsbxF7_HGPbXRMX8J_9lECYU0SPY6W7yj636u5_MIbLnRdeG9vBxSHhGsWZSvN-GDBSxm_Ltg9kmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات موشکی ایران به پایگاه‌های آمریکایی در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134974" target="_blank">📅 09:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134973">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPsRbdD5toprI5GrBP3uXL7ak4BAJkv3ZhyaGUMMo_Yd7ZXPCatvdC2f6dlrQRpW5tbLvNJHeBDbjPUg77w7WTAsfFPaJkf9GYw5a3NSyAglPMXDcJBBBCWGf513W5PqtisvFb9Y08Xmv1bpPAwuPidzzuOHd2mqBh_ePVoU5-OtHBGQU9X4NQNSVnA3vCiBDembTYQrOBJmfPN33u5_CVpfoqaZ38bIn4fF4PRLN3xmh1W21XIkw99gkVZvafQpUYvEGVHAs0ZBLNIAjNdXnSaJJlaSURa6_E--ogV7XoIMcDQ7J1NOB2od241mA95DMrkh0i1lsbJGYEdZgBbRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134973" target="_blank">📅 09:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سپاه: رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134972" target="_blank">📅 09:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134971">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام بار دیگر افزایش یافت و قیمت نفت خام برنت به ۸۵ دلار به ازای هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134971" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134970">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
پکن: چین و پاکستان خواستار آتش‌بس و از سرگیری مذاکرات بین آمریکا و ایران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134970" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134969">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
مقام آمریکایی به وال استریت ژورنال:
حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134969" target="_blank">📅 09:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134968">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=YXmtg1oAVQj4uLJeeoAgP8CJqfdDEJU6q04zUYsHGYQ0DXy9T-FhfC5ZuMWITW1wgZtfFM6UDcF30vmA-ce-JbCuFZpWb3isP_onmtxW1Mv5Qw4mMCZwXWqzvthWqpqTcYI-ClRRBCXS-3HbZ-Hl3Hx-i-vSXWBKgBRrQcbn5wRlRMmVMYdC3xyReTzU-FRYovRj15cjyKLgq3P1jBwbmiFx7wjmh9SNRYPwYTsdDBL6lRlKBkNCpYrRcodLz2AdaisQXF28D7_F3vG1hZySmfJtxTwsp2EwTgWsSD0w_4M2daTqLR4fQxsB-Txgk9T7OHbqLxrxJ2mxnIhcGAU4lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=YXmtg1oAVQj4uLJeeoAgP8CJqfdDEJU6q04zUYsHGYQ0DXy9T-FhfC5ZuMWITW1wgZtfFM6UDcF30vmA-ce-JbCuFZpWb3isP_onmtxW1Mv5Qw4mMCZwXWqzvthWqpqTcYI-ClRRBCXS-3HbZ-Hl3Hx-i-vSXWBKgBRrQcbn5wRlRMmVMYdC3xyReTzU-FRYovRj15cjyKLgq3P1jBwbmiFx7wjmh9SNRYPwYTsdDBL6lRlKBkNCpYrRcodLz2AdaisQXF28D7_F3vG1hZySmfJtxTwsp2EwTgWsSD0w_4M2daTqLR4fQxsB-Txgk9T7OHbqLxrxJ2mxnIhcGAU4lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت پل کهورستان در محور بندرعباس شیراز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134968" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134967">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSE3YJIv-JRJq7nmv0WaF6R4mSlXUH0wVKaJe-DlCmGCSUpX-u_tPvpKvYa0lgB1tsxy6zXScyjlds4i7J_8zRDxDKvlRQtgbik2M0w6dXZlE7ybeR6aYrxaFrR2g0JIx7QFFfTnBqQbhar6SfR9SCtx8sqC1Z8UBA-WVzLYJ-518tWrcj7XhkUb9Po2H1iRTYP1CwfnB-cdleatyh1s0f_2uEd5xH4IDtuFgcilUa-SCVKteGDJu5bp84EMDMAH7-ONLjZx0Mirfm2ZAkkyEYwqDck5YWfjA3RFo7CzCELdTS1tiG6hWdEPakzYZXFUPE1Yn8_ZaUBWhokssiPcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون دود در
نزدیکی فرودگاه اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134967" target="_blank">📅 09:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134966">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913d736794.mp4?token=AUvDdYaOk1Ca2e9OrosCVVmmcOtQDlHkosleb8brwrmpuSvOoQC1wKSVS9NCu9SljGdtnZmFlI1ppVOH_U43RiW6BuGWqdp7pYDkRaewNR5AJi-h_GDdf4E2c0GJ-z-KmI60vLr4pFQmH9_JxqKa7POQXo1PPnN-2eIYtLjuVqLasAlvomQLoeCQpTprxCfIw1v_xz2BMN_TkQkwOsdtUIMZpehPfBINy696_5v2GUxkU4DGhMASo_1RQTyno8fOVoZQyAE-lrwj2BhT-oWXZtIw9rntRvyJsfLUJTjumZnIix3jV3VL7UdrYQq1XnbOFTphQZG3OxCMMIDLtfJVbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913d736794.mp4?token=AUvDdYaOk1Ca2e9OrosCVVmmcOtQDlHkosleb8brwrmpuSvOoQC1wKSVS9NCu9SljGdtnZmFlI1ppVOH_U43RiW6BuGWqdp7pYDkRaewNR5AJi-h_GDdf4E2c0GJ-z-KmI60vLr4pFQmH9_JxqKa7POQXo1PPnN-2eIYtLjuVqLasAlvomQLoeCQpTprxCfIw1v_xz2BMN_TkQkwOsdtUIMZpehPfBINy696_5v2GUxkU4DGhMASo_1RQTyno8fOVoZQyAE-lrwj2BhT-oWXZtIw9rntRvyJsfLUJTjumZnIix3jV3VL7UdrYQq1XnbOFTphQZG3OxCMMIDLtfJVbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ستون دود برخاسته از مقر گروه‌های تجزیه‌طلب در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134966" target="_blank">📅 09:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134965">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
فارس: آمریکا دیشب ۵ پل را هدف قرار داد!
🔴
پلگریوه؛  مسیر بندرعباس، خمیر، لار
🔴
پل بعد از روستای لاتیدان (کلمتلی)؛  مسیر برگشت بندرعباس، خمیر، لار
🔴
دو پل مسیر کهورستان، لار
🔴
پل نیمه‌کاره؛  مرکز بندر خمیر، کشار، بندرعباس
🔴
پل روستای مارو شهرستان خمیر
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134965" target="_blank">📅 09:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134964">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVMpGnvJwxiTbecz2_jEFBsgzR3V6W9Q2q-d8SEwUEb6kCc5C9f44p6e8Iej4aE_VPDwQXSJq8Txq_jYc5IO8aySyvms7wbG3Wt_PqZqyqjYmbvteoFUl0BCC0m77mjbOXIDUVx4Xk4n486syWFI6jUsYckMLryQ6XIo4LkeMLD4XE4X6jR1r1PSTG1hv3FxvMFv9uHjQMBjJ2s0H0p69VIgaNM5_Ji2A1dRkAb5kvpakckZwwnUXAgbCyDl453-uDNPEe0ALfmP3o_UvWPwKPTvjcQCuGFdcrLrKlpAnrqpwJ2cRp0H2Bdyiww65clCQ09Iek35-1RSKZ5qh-XgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهباد آمریکایی روی آسمان چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/134964" target="_blank">📅 05:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ در پایان سخنرانیش: ما قویترین ارتش جهان رو داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/134963" target="_blank">📅 04:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/134962" target="_blank">📅 04:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134961">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c26581b61.mp4?token=FFuOKrhPhRvuBOHRurjPegCoeNAdo1TOISyiD5nbu_TTdcu9LFnbow91HU_H-3_JYC6aN8tDZMgohXKvnF7o2eT-Fw2LP8EASPWpHyZGr3jUUoTEoy3fBb7_JaX3p8NPuoR-pLTFaNDRmse7R_n0RL0XvF_joG-pZwf1zTelTzUYKgW7M-6Mda7k2NftECRlNkp9MhnsL6ihcBb3Nlogi8bqXIMBQLczjogGSZjtbsxA2do0bX9Nd6_y_444ibD13vnTnSbHatedmhx3X4qniDYLO1RdXHA3w4lgFh7NGUDoPUpdOzAnhLBaWAzSOzT37igMpVbT3fX-3TQ1mx4OeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c26581b61.mp4?token=FFuOKrhPhRvuBOHRurjPegCoeNAdo1TOISyiD5nbu_TTdcu9LFnbow91HU_H-3_JYC6aN8tDZMgohXKvnF7o2eT-Fw2LP8EASPWpHyZGr3jUUoTEoy3fBb7_JaX3p8NPuoR-pLTFaNDRmse7R_n0RL0XvF_joG-pZwf1zTelTzUYKgW7M-6Mda7k2NftECRlNkp9MhnsL6ihcBb3Nlogi8bqXIMBQLczjogGSZjtbsxA2do0bX9Nd6_y_444ibD13vnTnSbHatedmhx3X4qniDYLO1RdXHA3w4lgFh7NGUDoPUpdOzAnhLBaWAzSOzT37igMpVbT3fX-3TQ1mx4OeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور آمریکا، دونالد ترامپ
: ما در ونزوئلا پیروز شدیم، کشوری که اکنون با ما همکاری می‌کند تا میلیون‌ها بشکه نفت تولید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/134961" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134960">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4ce05c84.mp4?token=lyc9L5YSwIrVdHyCvE-b5Win-xjdZEMgSwHGrlI4fQzOz8Sb_wGTYImDHkD31SsfB9LNmE3x8dwCUHHTWobtKTQ0-INM6BlTQsmWWIQ2XH_TG9CzXL4igSNIqV35CLISYBGa_J38H-q4bSrx7twWtOq3W6NNFy1pKVYwqHypCG5okWmOzz2w9teQ_tyjW7guYCSos6yzaEbspXloF36v0nkaGbOpMa4hEJmfcy3ho7JTp_uz9N6wIzv4MzE9lmnXdWJx8lPE2NIaU9TJaL8jCw9jbhsFUQvTbZsMsEqXzQhiw2y6RER6VWvrt-3hUNWXz2xus0eR5gKQIOpl4dZeIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4ce05c84.mp4?token=lyc9L5YSwIrVdHyCvE-b5Win-xjdZEMgSwHGrlI4fQzOz8Sb_wGTYImDHkD31SsfB9LNmE3x8dwCUHHTWobtKTQ0-INM6BlTQsmWWIQ2XH_TG9CzXL4igSNIqV35CLISYBGa_J38H-q4bSrx7twWtOq3W6NNFy1pKVYwqHypCG5okWmOzz2w9teQ_tyjW7guYCSos6yzaEbspXloF36v0nkaGbOpMa4hEJmfcy3ho7JTp_uz9N6wIzv4MzE9lmnXdWJx8lPE2NIaU9TJaL8jCw9jbhsFUQvTbZsMsEqXzQhiw2y6RER6VWvrt-3hUNWXz2xus0eR5gKQIOpl4dZeIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: چین به اطلاعات ۲۲۰ میلیون پرونده رأی‌دهندگان آمریکایی دست پیدا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/134960" target="_blank">📅 04:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134959">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ:
اگه من تو انتخابات رای نیارم یعنی تقلبی در سیستم شکل گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/134959" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134958">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37596bf02.mp4?token=NX1H1lP3phMxIbJP6TolqILOSiTLqZBUEEtzna9v7RX3Hjf9EkuU9ksr6zpY9P9D4tAAzKklZ-JbOTd20n0vjrp8nbEl6kUSqUO2sp6T11fia7IjoePwJY_aQJEtPyE03euDcovqut7SyILcAv5lB5Xa3kj78N9EYSfmyTYKoe1589brqk9K79ELHVBIl4rVkh7mzbrvocH3YB-GjYzZd3gveNGyxwFNDJEFxgWxn5LGDCd1lzlvM0zqo81DCXIaCWJKeX0c1Hmlb4T2La4zliHGdK20x0XXy4WPs9zzbVgWK4CFc7JLh7aJ139ZBYVk-hAjA5po1C29iLJA_9XOxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37596bf02.mp4?token=NX1H1lP3phMxIbJP6TolqILOSiTLqZBUEEtzna9v7RX3Hjf9EkuU9ksr6zpY9P9D4tAAzKklZ-JbOTd20n0vjrp8nbEl6kUSqUO2sp6T11fia7IjoePwJY_aQJEtPyE03euDcovqut7SyILcAv5lB5Xa3kj78N9EYSfmyTYKoe1589brqk9K79ELHVBIl4rVkh7mzbrvocH3YB-GjYzZd3gveNGyxwFNDJEFxgWxn5LGDCd1lzlvM0zqo81DCXIaCWJKeX0c1Hmlb4T2La4zliHGdK20x0XXy4WPs9zzbVgWK4CFc7JLh7aJ139ZBYVk-hAjA5po1C29iLJA_9XOxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ
: اعلام می‌کنم که از همین لحظه، اسناد اطلاعاتی مهمی که آسیب‌پذیری‌های تکان‌دهنده‌ای در زیرساخت‌های انتخاباتی آمریکا را نشان می‌دهند، از حالت محرمانه خارج شده و منتشر خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/134958" target="_blank">📅 04:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134957">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38775e5358.mp4?token=X0cdoucBzsYLKSrlKRrXjvfb9Kbvb7ue_etI1GioTTQLLAUvbgmL7wV5La7LK59CGTsLPnqYrY3IiRlsBi85-1xIykOwedXM64TRlUN-zbhetLTGvjHau9O9QpNt-W_73qq64Md6ilZu_Nw-j73zrMmeZtxmpLiNf5XWzYHbo3HZhUr6Lzt7kr4SiLMO_KVOIuk60T8Ztz5HVLGfmF0GtlXTubIAjzL8Mv_ZlmHmXwaNNZGqEi_8uPv5XAUrBpTVCKLgCN732PJwgNkIZp2ECu-UiqfxNEfJ8FAmSyNZS8-wmPKC07Ldn3bGuGMFvsQmcf9qwHN-6TDHIJdNuHZgAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38775e5358.mp4?token=X0cdoucBzsYLKSrlKRrXjvfb9Kbvb7ue_etI1GioTTQLLAUvbgmL7wV5La7LK59CGTsLPnqYrY3IiRlsBi85-1xIykOwedXM64TRlUN-zbhetLTGvjHau9O9QpNt-W_73qq64Md6ilZu_Nw-j73zrMmeZtxmpLiNf5XWzYHbo3HZhUr6Lzt7kr4SiLMO_KVOIuk60T8Ztz5HVLGfmF0GtlXTubIAjzL8Mv_ZlmHmXwaNNZGqEi_8uPv5XAUrBpTVCKLgCN732PJwgNkIZp2ECu-UiqfxNEfJ8FAmSyNZS8-wmPKC07Ldn3bGuGMFvsQmcf9qwHN-6TDHIJdNuHZgAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/134957" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134956">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857d55ae03.mp4?token=SEo3o0gyZxVTd9OFB3FBMIa4aUpUKc9g8dcUqWNPMJzbdb5oo4UGPsLParjG2hBwIwcKvS16dGy3_AbqzzUjN9KzRa2SYjVuwaiYMKkyJewiwdsuk9lgMzHkvx62cLZjZnsxygd456A1OF0sL0-OLTSCLfc8cImAp5OiFzXpdaok1HdIV8LV37pcYY8jTNcV8QjlpUW8ArslKwsKu1v2abkcujy6CHohVmTe7mDC52w-E2iAR7wfUPRdX_CZuwh7F8Q1o282tqzpXVPgSqitqTNHCsLpjKeu_nf1xHyRWwzMNWxhcVlBrTcuEv7f5FRbkDijQJJ-rPd8eipS51CU3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857d55ae03.mp4?token=SEo3o0gyZxVTd9OFB3FBMIa4aUpUKc9g8dcUqWNPMJzbdb5oo4UGPsLParjG2hBwIwcKvS16dGy3_AbqzzUjN9KzRa2SYjVuwaiYMKkyJewiwdsuk9lgMzHkvx62cLZjZnsxygd456A1OF0sL0-OLTSCLfc8cImAp5OiFzXpdaok1HdIV8LV37pcYY8jTNcV8QjlpUW8ArslKwsKu1v2abkcujy6CHohVmTe7mDC52w-E2iAR7wfUPRdX_CZuwh7F8Q1o282tqzpXVPgSqitqTNHCsLpjKeu_nf1xHyRWwzMNWxhcVlBrTcuEv7f5FRbkDijQJJ-rPd8eipS51CU3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: قیمت داروها بین 70 تا 80 تا 90 درصد کاهش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/134956" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134955">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ :قبلاً همه دنیا به آمریکا می‌خندیدن، اما دیگه اون دوران تموم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/134955" target="_blank">📅 04:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134954">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گویا دالامان که نزدیک آنتالیا هست پرواز معراج داره، این پرواز رو یه آژانس هواپیمایی ایرانی چارتر می کنه هر هفته که مسافرش رو از آنتالیا برگردونه ربطی به مذاکره و ... نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/134954" target="_blank">📅 04:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134953">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
برگردید عراقچی نیست توش</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134953" target="_blank">📅 04:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134952">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
هواپیمای عراقچی رو آسمون ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134952" target="_blank">📅 04:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134951">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
انفجار ها در پایگاه آمریکایی العدیده قطر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134951" target="_blank">📅 04:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134950">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCaxd8_6wPqDzPLg2QSU2kaSnpoUMsEV61FEQIBvLhrY1HkX03wwJYwzRiCXR4JhVSdzNCiOTBfmk7Z991dzemi6ulnUdIVYWcIcQOei5uIRH9q25a-ZM4lss7ObXFOMAHhSfA_SbGDfuPOBq9BK8rSookRFHmVamb6_26DCutS30mo8WBzvdAlAS7bHgQj1eVq8S2yM7D1_auWzo4phitseSMF0DmOfwsCzsBMD_z4bfAiCio4Sv6JOQFdGQeRzzOo6TEf0ftXWsH4UTSZ8nAl0duB5TsGbX7oTErZlKCKujQIeRrJKfZe3YMF0Mqb2I_UHkHYO7EaH0zGiN21rZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت شدید پدافند در بحرین هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134950" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134949">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9NM8hd9cbL-dFjZNO3p2Kpg5TB9Bx9OdvMwUyikaStTlpfG4Wr9I--mwsvx_lb94vmNUUNM8-h-e7XZFpQTW4ZRqKHv-8RDedrGD--Edryk-p4fSFWUnCai0pjmhmOcmmrt1QeL-T4wug74lOvJXjU4t5xdSQcIvMz4oDxsNRG0ec0TQmHzS0liHpHdhlD4qtQTRh1pgl2fT8zV6MdQiDsSZwx02l6eyiPaOd-xkuB4fWhPqhke2frBPbFgUVdCW8WVof2TlnpZgsOTUmfmy6lZpaQZm5Ru4wu8ihUZ2SWnYitKRmXYNW4kppjbNODr_2mZqmnmLZT-xBZC4qVwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان قطر بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134949" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134948">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
حمله موشکی به العدید قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134948" target="_blank">📅 04:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134947">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ویدیو تخریب پل ملک فهد که درحال پخشه متعلق به یک پل در روسیه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134947" target="_blank">📅 04:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134945">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99c3c0b64.mp4?token=cuqzTYMdRb8cZ8YFM9Cfn_xS3xyNENRJrhTvEzrlm3UHdog3XuH9voWE2EoEPmYHuUMPGaMf97Exg--NzyEi_9jIA-9nxYdH5f2TJjEzQaj-qYK4DmfJJ1iZFfhNYO1S_0HnM7c9neiUi5RYygFIn850cgBX4DnAp0YPLwc1iQ2WvQU3L004JCtL6q2f6zLtlRc3mtROPNLzfJ-apea407HVm4PUa_Z-5FP-quF4ExVo3FQXpyZQW41g6ngGb2CrWiJEY6AGddRU_gH9Wp6ynobWvXcfL0EjUQVZZ__hzkGTdXE5dysdHgEiXiCQIcAt1QikvKPoZ52JgDVsEy6Y9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99c3c0b64.mp4?token=cuqzTYMdRb8cZ8YFM9Cfn_xS3xyNENRJrhTvEzrlm3UHdog3XuH9voWE2EoEPmYHuUMPGaMf97Exg--NzyEi_9jIA-9nxYdH5f2TJjEzQaj-qYK4DmfJJ1iZFfhNYO1S_0HnM7c9neiUi5RYygFIn850cgBX4DnAp0YPLwc1iQ2WvQU3L004JCtL6q2f6zLtlRc3mtROPNLzfJ-apea407HVm4PUa_Z-5FP-quF4ExVo3FQXpyZQW41g6ngGb2CrWiJEY6AGddRU_gH9Wp6ynobWvXcfL0EjUQVZZ__hzkGTdXE5dysdHgEiXiCQIcAt1QikvKPoZ52JgDVsEy6Y9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک های ایرانی در آسمان قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134945" target="_blank">📅 04:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134944">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزارت کشور قطر:
سطح تهدیدات امنیتی بالاست و از همه شهروندان تقاضا می‌شود که در خانه‌ها و مکان‌های امن بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/134944" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
انفجار در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/134943" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134942">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
برخی منابع: اعزام گسترده نیروهای امنیتی عربستان به مسیر پل ارتباطی عربستان و بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134942" target="_blank">📅 03:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
چندین انفجار جدید در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134940" target="_blank">📅 03:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18319f2842.mp4?token=VaqvcqP5iupYPzKX1wexRiF-hbE6sq68YFtGPDje0FKsXCTarIKrO7Z4AplVx_yTTaeIn-qSOqT-5rn2OdywSOfZn90qcAoHy4AN6XTh18RZTmPooElCRzPfPw325-EJMqMDK26_3_OIIN3kCrKggoQt-TcXK2Oopi04eqh-jESjH3TlDg6nyD4u5z_qkuO6JJNWE3lr1DHT8jbd1lR9fxsA512BI53pwPZyeYe05J9Cc8p66MkkdVF66vk18vM2Z3xQd9B-syFw-C7ZVeU-QQlmkzKYDEwJ3XhdcVnatylEqRkCB9goA2H1Mzqad2SzRKzZqL9Qxw3SgukjtkZjWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18319f2842.mp4?token=VaqvcqP5iupYPzKX1wexRiF-hbE6sq68YFtGPDje0FKsXCTarIKrO7Z4AplVx_yTTaeIn-qSOqT-5rn2OdywSOfZn90qcAoHy4AN6XTh18RZTmPooElCRzPfPw325-EJMqMDK26_3_OIIN3kCrKggoQt-TcXK2Oopi04eqh-jESjH3TlDg6nyD4u5z_qkuO6JJNWE3lr1DHT8jbd1lR9fxsA512BI53pwPZyeYe05J9Cc8p66MkkdVF66vk18vM2Z3xQd9B-syFw-C7ZVeU-QQlmkzKYDEwJ3XhdcVnatylEqRkCB9goA2H1Mzqad2SzRKzZqL9Qxw3SgukjtkZjWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش خبرنگار تسنیم از پل بندرعباس به لار
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134939" target="_blank">📅 03:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPdYNCY3LiW_44khmyUbjXfSGGiEOVCq0S_sDZA30mTxL5ShjlwxxK6aM8kLvmlIpsDJLBhjCC7aCx0TMfx6L94C3wovWRCJJ3mTNxgtxD_CFyidIWOUbhe-XQEqvQoF-ChBO2x5zTAVZ_4oyJcqomsb-7JdJz85ZIn7GL1ToKBW1F6h73u8qlkbq5ZOtlaQWyOcRuZjoHWQ8fZmuCZU_PNi5qP1CxlqBTlAdQpt2qq3ixXBottF-pUMpgEX3KnW4BkuCiJQL7LfEYT1-84ZBCyPcm0KDqbi-IYAqgGiBPYrAwisStMHVxw7JsTS3g6WtSLPbj5je1v3SSjLb1jMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
شاید به تهران حمله اتمی بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134938" target="_blank">📅 03:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مقام آمریکایی به وال استریت ژورنال:
حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134937" target="_blank">📅 03:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9soW4T5P2gisou9jgY3IOvPT3ESKG3PFOhMWqoBh2YKy5wHsB9KIVcSYBZ514jFQUaKaG6EtaKJN-WTG5ySJaD4arXYjR9jDhYZXpf5q30VxcLK3dzFUBQFA7q5X9g5vduPmg92ZVacwoQMOozNUart7hQjmbMcdpKO9Czv4BgQLUXt3kR16CNKlzDySzW5TTivroagtRyEBlLbhP9N99AnEf0TY6KBbrRsj6Fbur19bJTwM6ej6wnyDSa6LMJeI3nBIe164xAJBQSSFZcsHOnWQkTQQ6YNrfuMMhZdsbSeQmBnWZ4bvaSfv1M-3ArzoyRsxJuomd-bPY5AqemJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: فیفا اعلام کرد که سلاوکو وینچیچ داورِ اسلوونیایی، برای داوری فینال جام جهانی 2026 بین آرژانتین و اسپانیا انتخاب شده، داورِ بازی انگلیس و فرانسه هم یه مشت ونزوئلایی انتخاب شدن و خبری از علیرضا فغانی نبود
@AloSport</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134936" target="_blank">📅 03:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
دقایقی پیش اسامی داوران فینال و رده بندی از سوی فیفا اعلام شد
🔴
علیرضا فغانی داور هیچکدوم از بازی ها نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/134935" target="_blank">📅 03:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی:
در صورت تداوم اختلال در عبور نفت و گاز از تنگه هرمز طی هفته‌های آینده، نگرانی‌ها درباره امنیت عرضه جهانی انرژی به‌طور جدی افزایش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/134934" target="_blank">📅 03:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
برخی منابع از وقوع انفجار در پایگاه‌های آمریکایی اردن خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/134933" target="_blank">📅 03:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزارت دفاع کویت اعلام کرد تمامی حملات ایرانو رهگیری کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/134932" target="_blank">📅 03:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw7S3lbtmvgEWORIdNUQc2HhCse31D0A0Q57rJ-MNSRCvFRMBC90P1_Zw3kzgwcRJqd4js0olaZV6k1A6QwJ5dAXKP7oFvm22WkrplbRmzu-yugDmWcekTeX5ZkDqxmt3KWo49S1rn2MW89nRmk_Wd7EocKsrHg7JvsRxIBNfW4ZehdEZzYcUF-UrVRSI7NMm8Yhc4nxIUWh_o4yACU8c73H9irn_2HSzVARH3VHMh9Rz8GdD92sQj3P9qsF84E6i209m81qZQ8nlXAaND1J5M5YTxmT7ZTHJpyvwX5pzg7XHwRNxoqzy_x6zNbXT4XTAtSjqMUJPg5822tj5EwNGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای عراقچی رو آسمون ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/134931" target="_blank">📅 03:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
به ما میگین وطن فروش جنگ طلب چون نهایتا ۶ ماهه داریم میگیم ترامپ بزنشون!
🔴
شما که ۴۷ ساله هر جمعه دارین شعار مرگ میدین بهشون میشین وطن پرست جنگ نَطلب؟
🤔
این است شعور و منطق عرزشی‌ها!</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/134930" target="_blank">📅 03:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز:
اگر جمهوری اسلامی نتونه پاسخ قاطع به پل‌های تخریب شده بده٫ حملات بعدی امریکا به زیرساخت حیاتی‌تر ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/134929" target="_blank">📅 03:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqcuCwJf7Rsdq3OGrUlBriPSFk9BS0xyC7uTEqIALwUYBIjMMzHX5-_BjOwC40Jz3Kzop0_1SiYk8Lr-n91nOUhlx0QdCBqq6FFeMbU1D7cDD2Ky0S_ClGMUh2qzJD30BmWgWlKooBJ3PO0lZyBIElNPozqJm-EumpJhilJTr3LY8iT2W2ityJXqtchzhI2qI1xqRKr5A06IUxYy9TcpwApn-F19GT0tkfRO-k0WuZGMqr-dO4NO6QWXZ5kKNLHZGIjklVQLILMZ5EDZVyedZxBx63ZbAK60sFAJnRuqc_ZUtKTLhYo7kQqUJ5XK7cgnlGdBQl8PLHNGp8vV6O-kcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آسمان بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/134928" target="_blank">📅 03:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afvjIyf_6n-EqshjvQ5eXWRj3Kk5cMHH4l3cCKDaQeJ7km06-Giox2VuvWOU63ROrwXTlCp5yXYq51y3uPkKpzyt2nKsx5V4emjTm_MPxr2zcpZXSpv9h8xq-Ymm8UKeLj_22N7iIC3N-Re9IiVQ7UbyhUjgtE3HCSWoUGaJwPHUi9gcNwyRu2jtbxx88RwpPNGrEwQIxuhlOxqNYp6NbYpprO_zFe-vsK-oooM_Cq3c1OVs0M_xc8eS-P7Jp-81e4LQhuogHvuZHlTcDPazGpafUNw-glMLerYU9M_kgKjh2HU_FeDK7FenQDT_2lp7R6MHQk6r6O0Zg8LFBuwckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق آمار گوگل  تو همین چند ساعت، سرچ کردن جمله[لغو عضویت  جانفدا‌] افزایش چشمگیری یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134927" target="_blank">📅 03:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
انفجارهای مهیب در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134926" target="_blank">📅 03:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c312ce96.mp4?token=O96H3-WmGCjumqmsjK47iY_a3XSUIJF-GjjH6F860zXdocs0CcEwSOmXxdVtAnvvXdv4IE_hX2u7b0TiUL3U5S7vy-EOb-foaT68O5lCwZkNbZA41alPY2c4kR1hJntZ66y4uuY9GnBR5-yuhentgtdQ21g_aArJC-8iFQ44QBoOaozH0n4Elsl6Phf-aVDMMzK2QzYHImy7xoWuqDogQI8ot3LGGEiXg7tfDWIR6Vv7PLZH4COZHoUSTy95H6jw3u1-tiIcvaVWKZOGItHlDdHtZHQwopOg0aAnDxYBIuSezZp1_rYhueJo-syAKjOhcFYPd12dVafInS6iuyptyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c312ce96.mp4?token=O96H3-WmGCjumqmsjK47iY_a3XSUIJF-GjjH6F860zXdocs0CcEwSOmXxdVtAnvvXdv4IE_hX2u7b0TiUL3U5S7vy-EOb-foaT68O5lCwZkNbZA41alPY2c4kR1hJntZ66y4uuY9GnBR5-yuhentgtdQ21g_aArJC-8iFQ44QBoOaozH0n4Elsl6Phf-aVDMMzK2QzYHImy7xoWuqDogQI8ot3LGGEiXg7tfDWIR6Vv7PLZH4COZHoUSTy95H6jw3u1-tiIcvaVWKZOGItHlDdHtZHQwopOg0aAnDxYBIuSezZp1_rYhueJo-syAKjOhcFYPd12dVafInS6iuyptyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی میبینم اونی که به ترامپ میگفت عمو الان داره واسه جنوب استوری میزاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134925" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08de537c4.mp4?token=WmYZ0GBJaCPGd44eWEKYZrgXGfr0_DP4HKPQxP1bdqL2c1nEVXgoYUPY78MsoYlxb3PFhbHdJown4pPkoZWVTgV5CNBI-Qo4CkaTij1-mTOzaCDDj0fFMWdBIYx4vZ2C3T5ixz4Wkgw0vBWDbGZKDRpFsRuvbCrfPVXD-dYTLiRKcVx5v6MzdGTdiX29BDBy0t86Lhl2F_JPSi9weli1z0D209y5YNVJ4NBnF4PCngEH4vgtAmMpGHIfFNn4SKBEvHmTkChmiaJl-cXKDiG0gkY0auC4CJSwSdZwM8hOeBX1qiZdl3eQgD5c3rRPaJ8P2UKRQpIAFc2bbZR8XJ7bZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08de537c4.mp4?token=WmYZ0GBJaCPGd44eWEKYZrgXGfr0_DP4HKPQxP1bdqL2c1nEVXgoYUPY78MsoYlxb3PFhbHdJown4pPkoZWVTgV5CNBI-Qo4CkaTij1-mTOzaCDDj0fFMWdBIYx4vZ2C3T5ixz4Wkgw0vBWDbGZKDRpFsRuvbCrfPVXD-dYTLiRKcVx5v6MzdGTdiX29BDBy0t86Lhl2F_JPSi9weli1z0D209y5YNVJ4NBnF4PCngEH4vgtAmMpGHIfFNn4SKBEvHmTkChmiaJl-cXKDiG0gkY0auC4CJSwSdZwM8hOeBX1qiZdl3eQgD5c3rRPaJ8P2UKRQpIAFc2bbZR8XJ7bZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله به توپ ضد هوایی سپاه در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134924" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtvhRBg7_odCzGcHb3o9Ll0vZwXv-LVyU8cr_FU7G67zmsxYmaw7VVz8NMwkLfNoDO5XeJiVtonQr_vRf8cTi516HSbDEHOet7utzXu7CPKHHhmG8lx3yykjAPaW6yZJO_vEztg_tkKtrcw3895W93eFCSPH-U84HLonwPJ8-vevEHZiEMKy1kypPh4y4nNum_vSUpKmv8C5oSjzZSmV94a1f4-NH-CDjJYHuGb_UaBQFhucYX8qIZpFZdBYn_NRd-fsVN_C954GvfAEuzba1k9JLwIXv9CxLPIdb7IUBgKZk6KVfhhB6EDwHPWkAgqwmQyBiVkXlwJUtZAHSIrKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش
کویت :
در حال رهگیری حملات موشکی و پهپادی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134923" target="_blank">📅 03:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
آژیر حمله موشکی در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134922" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upJqyvYv_cHxZFdvMjcIcJK1eYPNSoUXyyLwGcJ1X5ogdlH6S2STfIdjM2XwPr5uKgQAExjrh-3lbVl1e4H_P17g6v2HdpDPI0bBj9m6Pp4jEztDSOAN-TSqHN68JXlx622QlLBErd4VPBpmMgVRPfkgEXi2EMPBQFd0uNyquRakEj50YSzossiUVXRKTQOYVpfB0el9x5KVz32mksysWR0qTcXKWKutcxByDCcZFGkCxOjiWhV4ADo7lGqaBP5Vqkd3UYt8x5PD6CcVVc7naoAj6IUZ5ZR7dPceTNrTfSBBTT__HglRxQI986hkYJnifWgjzhs93syUPaAqy4-wDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه خبر نام دور جدید درگیری ها و جنگ رو "نبرد هرمز" اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134921" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH11KWik8ACsniQskC57HCkeOl_pJhKpbmSXsi2OTDNGKiaCRUjq9OAXzk8OpNLXvmYf82pyk3SYnP_FYd2VQtnCSlw_chGktEcTw3rpOXgbn_U-KP4s2rpprGD_qCqCWQBrisZfhn6W31nFg-d1eZET3WOb5v-La3Py8E_M3Gs00xVtSOTU70PASH8rhdjFKJr3KJn6wKKrOsuBIZQW1s5_ffY8Uy-no-ccxMClZGMAM-H4tUateYNLvl7vpIgje0AK0WlCfUze7hIB8ygcKVy_MdyeLgrQuN0inGmvHdTDMPb37IW-OBV504WlAZ4eJbDjwlbtPPomfor9a_Yiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حمله موشکی سپاه به بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134920" target="_blank">📅 02:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JniQAOebjnVQ33vpQ0FwgLdC_wtCEqpycWkUvnluqT7E5-Bb-_YHL5M8CstxEHSDGGL45awiBQLPKbXK8YAuH4lDF1lxFihwES7P5S-ryS0jxRMP4jHR_dNFERuQKPqCmRjNhSjfKX8IvYXHT80KMtL5rGwRFz6kBaKbtw5jY6su_pOv4QwuxvmKvoyvR3ET0JSKON0BmOsToUU6oQeER6jVGTyCmHdXnKjC977muanuIP-rxjt8_JQiw5nA2AC512neivoFJiEeAoYeY6UXcceBw2_rkd9JLt2KDseS2knJ2D-D2f8gcXqcEZRlYe8Jo1dN2i9Xm6OzgUNY-gFNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای عراقچی در حال خروج از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134919" target="_blank">📅 02:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhFSth0sTNguWWJv0Cp-WIY6ag7bl1g62pMtNEz0zATPm5cwkfZFUMDz1q6mljLRA_dfEG2Ut52KEzwDoSHtpJ8SsP-qwgHvtz8FWzXTHTYiE2hgqUVe1cyQCMxPEiGmh0yRdF9eOlp1EzQsI3CRwQFKZJ18IV6QjIFoEsaesgTG8WFLI8lkeVpxYGD3kJYSAvGE_ZUFXEhsNOAoLQR8iYFRCz64D2s8P-qHkzu8ILakWuMEAAZj14raGdV3hN7ZhnpPqtZ136-ozNagE2hvuzp-X64YPTYB10qryW9ELMwG3DTBj95c42aOP37LHXadMa4yqsX-eokJ2iuLsVlR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون دود در پایگاه دریایی بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134918" target="_blank">📅 02:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=pD9X261JSqsukBsjoRs5ky33ascdDi5KyaGQK_oBIJBZhJZYZtXLLnl5QsfXbbohLPo4fgGJrdwpOIKcMb1sqQHnxV6ZcYUKkwJGwJaqRm7VP__OhCt1GppCK8REcn78IBpU9-87k5lcZ8pEZMGifMmofnXrIFLXFA2B86ZJbDitzLawSmCzLFF4HVS0Ka60C3quD8hYJhq58gDSQ4LB_puILrbatkq7drREGO5zVjNSJEVjPaj1_k-iBeW-pdKZXz95ti0zzpMS3GRbF5oMBL5gawpFwKiCHy-GvnVHEQ179iEBOTc7FJADO9UONeAXpdFD8U19lw8AcR6Nv538IF5N5W9GnEYuJKcwFB0LiUKc9zlfa-E--DiSKDIIjfqiLAJDuf9rX6r9pv-gQVQZhB_dJDKOtyUFqy_YgSmdHoWW5g5LA83RYeeJSllmGOhnguH--4hBkXr2l9OiypBCUTQgpcuY7grd-6ytxsXE2Ab97pbgN_wMtwYdLyHGir7wQRsxe3D6MK_hlwyIW4K2V71lZv-bO6msF0Fix26T2JbBcsB9ThoBuA3Pf6OovzGGCUjYRO0cgSvsUyzvw4RgtXq7r1T5-DbsxWB7An2QEibiidI1g7Ei9x3H6Ed6hWfrm8kSX6Z_yXqH8iKyKGDl7N_fZ_V2QAn13bcQ367YIqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=pD9X261JSqsukBsjoRs5ky33ascdDi5KyaGQK_oBIJBZhJZYZtXLLnl5QsfXbbohLPo4fgGJrdwpOIKcMb1sqQHnxV6ZcYUKkwJGwJaqRm7VP__OhCt1GppCK8REcn78IBpU9-87k5lcZ8pEZMGifMmofnXrIFLXFA2B86ZJbDitzLawSmCzLFF4HVS0Ka60C3quD8hYJhq58gDSQ4LB_puILrbatkq7drREGO5zVjNSJEVjPaj1_k-iBeW-pdKZXz95ti0zzpMS3GRbF5oMBL5gawpFwKiCHy-GvnVHEQ179iEBOTc7FJADO9UONeAXpdFD8U19lw8AcR6Nv538IF5N5W9GnEYuJKcwFB0LiUKc9zlfa-E--DiSKDIIjfqiLAJDuf9rX6r9pv-gQVQZhB_dJDKOtyUFqy_YgSmdHoWW5g5LA83RYeeJSllmGOhnguH--4hBkXr2l9OiypBCUTQgpcuY7grd-6ytxsXE2Ab97pbgN_wMtwYdLyHGir7wQRsxe3D6MK_hlwyIW4K2V71lZv-bO6msF0Fix26T2JbBcsB9ThoBuA3Pf6OovzGGCUjYRO0cgSvsUyzvw4RgtXq7r1T5-DbsxWB7An2QEibiidI1g7Ei9x3H6Ed6hWfrm8kSX6Z_yXqH8iKyKGDl7N_fZ_V2QAn13bcQ367YIqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین وضعیت شبکۀ برق شهرهای مورد حمله، از زبان روابط‌عمومی وزارت نیرو
🔴
مردم با مدیریت مصرف برق، به برق‌رسانی پایدار به جنوب کشور کمک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134917" target="_blank">📅 02:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82adfa6fe.mp4?token=F8IS48cZxMLTVVr752_oREpjR7fLBnWRTN6um6o7ka4U8J-ZYkNk10D7ZB3Ub05_4QUcohsG1VJXwJ7OQxbwJ32DcZxEh8v5pu4NQ_c6RvAKrYHmRto3F4ccbjd8pTQLQtOyYAd1QxQ3RhFIP79Uyz_lIrfMF8ptTMKqabpKABJyhpoOaNn-e6tZCqoUr0RkYKCTNjwWYYBPdtpBQ9M8bFkrdxGzX82XDcKZ6WGYLJ2Y8qNTG9QO2Gkf8TPC_KoLGK1TXSk00gQa5qJc6yAM2tPK_Mt7bMAl34xkejEcmAXD4pVR8BCN2T3UPaLX5TG1mkUYGDlCX91Y7Mx0k5IUcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82adfa6fe.mp4?token=F8IS48cZxMLTVVr752_oREpjR7fLBnWRTN6um6o7ka4U8J-ZYkNk10D7ZB3Ub05_4QUcohsG1VJXwJ7OQxbwJ32DcZxEh8v5pu4NQ_c6RvAKrYHmRto3F4ccbjd8pTQLQtOyYAd1QxQ3RhFIP79Uyz_lIrfMF8ptTMKqabpKABJyhpoOaNn-e6tZCqoUr0RkYKCTNjwWYYBPdtpBQ9M8bFkrdxGzX82XDcKZ6WGYLJ2Y8qNTG9QO2Gkf8TPC_KoLGK1TXSk00gQa5qJc6yAM2tPK_Mt7bMAl34xkejEcmAXD4pVR8BCN2T3UPaLX5TG1mkUYGDlCX91Y7Mx0k5IUcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی وحشتناک از حمله به اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/134916" target="_blank">📅 02:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fti9tqdW5TLkmzSM3pwVP382PpG7mk7C0IEzlG4ubPEpO7I6ZwHw-6pAsgUcI8LU1Bfeor91ZwHUwynal3mtFmRwZa7lDf3HjJjcmf1u499ndIfz6joPZP8m6oNKDHAyd6qmkGvNWknlhVKEXX6Kfda9whhdiwJZLK3lV1w19hxr6ptjIK61aKW947lF8k7FESDWwPWvz0ilIqS_ebgvh_GcshvAwxitdmZ-BV_9CgQcDDSEjNqkHyA7bc04Icp0C15GvPBC_YvyIfx_JTvX9F_qfSr7n15NaeB87kLB6pQNyCffLmOjjLBBDmZZhBGFzdEM1gMrO3I95Kjb9DWDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه حملات امشب آمریکا به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/134915" target="_blank">📅 02:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134914">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گزارشات اولیه از کاهش پهنای باند اینترنت در سراسر کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/134914" target="_blank">📅 02:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
چند دقیقه پیش امریکا به فرودگاه بندرعباس حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134913" target="_blank">📅 02:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134912" target="_blank">📅 02:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7aa57774a.mp4?token=aCsG91lqxpevv8sZ_5PiTDQT8k7rw7dd2yTA-HPobUQ4XaRgRb3Bf1fe-pYETzfWp0Lmp4bU8nTsiANxh8HhnjEHkpok1-fgbPqXyLhmCjTJQu94-4zj3PvnQMelsCZOnFH5BfEMvykoIJJjFigVemFvLePdTgieopW1VAXVWOllT9tjLPuMSt5eVLP735MFO45MFeRl7ReaAQOkbgJFSs6vyfoocdKFC8hqg6IbmOtJHjxZP1HMe6puONV6BzYKSG-hX0-det8kHe9ngIDX859QNplEX8MqL3ckTVl7jass2EQUSN2SphQjvTKZhexS246InkcBbk7jn90anpZpUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7aa57774a.mp4?token=aCsG91lqxpevv8sZ_5PiTDQT8k7rw7dd2yTA-HPobUQ4XaRgRb3Bf1fe-pYETzfWp0Lmp4bU8nTsiANxh8HhnjEHkpok1-fgbPqXyLhmCjTJQu94-4zj3PvnQMelsCZOnFH5BfEMvykoIJJjFigVemFvLePdTgieopW1VAXVWOllT9tjLPuMSt5eVLP735MFO45MFeRl7ReaAQOkbgJFSs6vyfoocdKFC8hqg6IbmOtJHjxZP1HMe6puONV6BzYKSG-hX0-det8kHe9ngIDX859QNplEX8MqL3ckTVl7jass2EQUSN2SphQjvTKZhexS246InkcBbk7jn90anpZpUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی انهدام رادار ارتش آمریکا در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/134911" target="_blank">📅 02:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZByEMbWGw6hyH0yVn8YQQdbZYbKQD_TR4m5swhyMhEmn1d2UrfuCq7d8LJZs8_2I28Zk_pfbIwVm68BH2ZOytUUUoKR3_z_KV3yRq-cprY3otFTGU3Nr9bbnoRJoidknMBySE7PhY0gJa9puO4Gbbjl6teoQvI_rDs8ERcJLbBC9m4HElzyeHSb3fiIpkQ8fYIXWRpeTWGTg_f2N6zNLi6OS8pctGT5c5XgP5VqydulPziUgJ-sYlgU3pK4-Hq0T1qfnWJbkNrG18-h60dCPakfUDL6uzdsXxBm_IAXeFLviuHpuys_LX6s0CmcGunMEFmGnjbBcAOeZPpv4gdD8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایپا از محصول جدیدش برای جنگ زمینی با آمریکا رونمایی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/134910" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">💢
پشماااااااااااااااااااااااااااام
😐
برای اولین بار همزمان 25تا سوخت رسان تو خلیج فارس درحال مروازن
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134909" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBDLrEtkRwkaAohZ_TRoMN9kRYLKzYYuz4e08Od2en_56gsZaLsI8iw9NGfukkLbBhfgGEji4uFNCPguW87-b7PGkpUU_bOJZQUvImVOsLqnMf6GTJYNeJgAoKhR0QZxRc6KdJiuvm2BbyKQlkS3mWohLaK9JT5YN57JqYNMVjx4dIhgIDVcqtfuf1ELiwAvVuQOzLLHxom0LCVt43hoXyDSWFEtZpIf114C_tdDyKM3eaEfgjwJRegC6l9Ui3InEWI5626_YSFidaAd28dqWtaD90c0aChRlmqqj0VncNQyzQJ9u1DCfQwpluNKP3OftZAeyWG0yZ52yCmHJXujXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست، وزیر
جنگ آمریکا :
ایران کنترل تنگه رو در اختیار نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/134908" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
قطعی برق تو کیش برطرف شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134907" target="_blank">📅 02:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=OvDT9XJgvdDJTXqLZHrwHP1cqMvXTFVVmVSlaA-_r2XE1vDtLgSC89KH7yISG2u-ygkJL2rJgp5rmu6xvp9TGqOpovPfcW1Gp-41KDfS-u4n6euUb1yWTFuglOEnsLq1M1jajzMnsPh7bUNfejMMxBrJKSVJ36-vi5rZ08C7pV4vk6Grwt595qspX4BFejGDvvimTr7oxWPGd7cz_cdGTloVWj250oyZqsBKDuw3xXbQ2DITez2OC2fQzRMg2wQVR2R-EqDC2nxwBA0HEibeHST1eXp63SATCtjMyTpzLWYpri2vipIPEMzD-MwPZmkdbiQVmMlrBqJ-0CJJoG2JUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=OvDT9XJgvdDJTXqLZHrwHP1cqMvXTFVVmVSlaA-_r2XE1vDtLgSC89KH7yISG2u-ygkJL2rJgp5rmu6xvp9TGqOpovPfcW1Gp-41KDfS-u4n6euUb1yWTFuglOEnsLq1M1jajzMnsPh7bUNfejMMxBrJKSVJ36-vi5rZ08C7pV4vk6Grwt595qspX4BFejGDvvimTr7oxWPGd7cz_cdGTloVWj250oyZqsBKDuw3xXbQ2DITez2OC2fQzRMg2wQVR2R-EqDC2nxwBA0HEibeHST1eXp63SATCtjMyTpzLWYpri2vipIPEMzD-MwPZmkdbiQVmMlrBqJ-0CJJoG2JUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134906" target="_blank">📅 02:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tX2NQ3k442wHkCWCWBNDTeNDLj1i_0ZQ1srr2TaKvkdl-rdqA7V-zTAKdtSbSjRQ_NIN9KLqZLxa3E6CEUKvK6sMgbilD6L1G54_rfKX9CcMXW4zGOSi9EdaQw5jOxwFWEAciOdfUVMhO8BNOh9vsNzXO5OdvBUJnq5p-GDk9vPBYMBfrGQxx4gJ_G9vzmpo0gjxy0Rqyzb1KTKAUfFGVxXqwavxu9H5Mnr1AIa7icMpfumxC1Ee7DMcrG_XfKqnDLmHfzvhg1IqOUvpf30RRSs-qv8ye21fC1h28ZUiRF8V-2s__u-X-hCOEjm67Emz7IETxidFlwYuDNRIVZDB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل
المنصوری
لبنان رو، مورد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134905" target="_blank">📅 02:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f0d99f1e.mp4?token=EPeuml65HdU4DeSB5k60X8xiUdwleVMgaHpr7NiWUqStXewdiao7Pvq89VHihWAMxIwOXgiu3f306f5G2vDXLj5-_vTvBqA7k3rN-C8_yDvaXft4f0x80G3gJerrKqhS8mhmivKCu8331x1hBqrRtpTcZ_izM6l19yxlK2zoluHl-p6Icf59TsbfuWp7CBoOSPALDO-nKsvJKs7WDAU-QW8UEhhaUJu-uHPU6R7Wz2dmYfucwIBwKnDNucYZ938KDmAEe7AFhTtGhIbdNM3yZf8pc0MfRNAQ5RoZwWVLzYlkRjXCPP0Ih-EUyp5AlhIhrSieeGJhEj0BGfXnOb8YXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f0d99f1e.mp4?token=EPeuml65HdU4DeSB5k60X8xiUdwleVMgaHpr7NiWUqStXewdiao7Pvq89VHihWAMxIwOXgiu3f306f5G2vDXLj5-_vTvBqA7k3rN-C8_yDvaXft4f0x80G3gJerrKqhS8mhmivKCu8331x1hBqrRtpTcZ_izM6l19yxlK2zoluHl-p6Icf59TsbfuWp7CBoOSPALDO-nKsvJKs7WDAU-QW8UEhhaUJu-uHPU6R7Wz2dmYfucwIBwKnDNucYZ938KDmAEe7AFhTtGhIbdNM3yZf8pc0MfRNAQ5RoZwWVLzYlkRjXCPP0Ih-EUyp5AlhIhrSieeGJhEj0BGfXnOb8YXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوی فغانی عزیز به حقیقت پیوست
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام جهانی/
علیرضا فغانی بارها ثابت کرده که موفقیت، حاصل سال‌ها تلاش و باور به رویاهاست. او می‌گوید در دوران نوجوانی هدفش قضاوت فینال جام جهانی بود، اما بسیاری این آرزو را غیرممکن می‌دانستند و به آن خندیدند.
#نخبه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134904" target="_blank">📅 02:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134903">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
دیدن این ویدئو برای همه لازمه
🤔
مخصوصا طرفدارهای حرام زاده حکومت</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/134903" target="_blank">📅 02:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134901">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I54Sy_8pQ2-XGhV7S_zHKVcDSGykggk7KFreseTkBeKA-BbAHI-v_Z5XHOfuNCt7jFVRyQgUWQbDvhb5AMi5G2NVdGLDn7TKt-fiepQaUJ6DQiSI6rA4S78TzmGahbwKPgajmyh3yGqUAaklHecuz6xiTmQvtsOUNbOWNHazyEaSWDBBG0nTKnQ0-tO8VBpSiBviKQaanlhQDnThaye1kSCqU-GVfZzVZKbwUl4B1b5iDZZbTCyXuhJzhXf6nY-2ELYc0YPgPSTBFV51vvfPH0r9ILJooIZkUlhkH-ElS_mSiCFbSwHCoa8liR9n4KUvWtki0-n30YmHS_Wa6kpvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح در صدا و سیما
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134901" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
