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
<img src="https://cdn4.telesco.pe/file/t-ntRuMLm1TDik2h166rImzeEhnqVseHb8kNpeQG2Tqsf22YWyOZhmSBGMzBoTRtTDMAE3nJY0uxRP2XctEDIO5MCrCiZEwK5vFLh4isulif_Hh_bh-tynZirV-RFhe8rKljUNi7yJgmTyrsCG0ruO4ImiSgB-zVUWrfCYu_5jmcdfHrZqPwKeU2OSVJ1_DVHR-ICDt9ROO56XVQr27h9haOAIhlt_5rU3v44OEXtSn7r5iLqgwfo58uJQiB9ywpEWFyjQQc_VFVRGqg472E6qnWMwVurAXsv_SeQiCK4g1nF_TOXs32gDpKS7eod2vsIj03qKJ1aiXs9JMTBAjcjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 923K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 18:56:49</div>
<hr>

<div class="tg-post" id="msg-133088">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نماینده پاکستان در شورای امنیت: ما به دنبال دستیابی به توافقی جامع بین آمریکا و ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20 · <a href="https://t.me/alonews/133088" target="_blank">📅 18:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133087">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سی‌بی‌اس: ونس، ویتکاف و کوشنر در تماس با مقامات قطری در چارچوب تلاش‌ها برای تقویت دیپلماسی با ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/133087" target="_blank">📅 18:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133086">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: من دستور دادم که در صورت موفقیت در ترور من، ایران را در سطح بی‌سابقه‌ای بمباران کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/133086" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133085">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdB0ePw6FjYSVF2PV9-dNM7VffqhDEXs3DCZl7ugq5plhtIongHtwgm5P3hP3v0Z5Gg84Q2iLsOJ-5fpYt0WH79Gdx7ysBDg_74fgs6z3Ul7XMDZWuVmx_o0x_f7c5dYh629xYyLesc9usTdHNmEjtnYoLL9-s0OBG-3Oskur8rEEcUizCLPMLpZ6BF7HVLDhxC6M_ofgnHUdx3QeJIp1SuQG4yG84Gpxin5vzgfaNqMhIT5-znHIPGSZTa4WrMiGTtd2tNoicyWxVQY_7QRSDXGVsJcwbtXPr5g4vmnciich-q6fZG3ImLeFEzub2OjTMnU-BazU92tYF20U4ZiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری منتسب به کنارک
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/133085" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133084">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری / ترامپ به نیویورک پست: در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/133084" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133083">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش‌ها از انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/133083" target="_blank">📅 18:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/391b205ef7.mp4?token=kgw7vk0rMR1EBdos3ch0hpdA9JLk4AAdi0vW7eY2TQO9Qw3v_5F_GirqLCwIn0IJSKFc4m64i13w-r1qRyrt1uKUvX5NV2VllJvQjtDLd6kWfK4GmDt_ReiivAXCidpyRxDHgA4ZKNOoAPSK1aTfcOrp_2Fa6vZI4yjkRzACBcwJlPjvQ0UaCYQx-d-fpUzqlmxsZsOhjrlmjnJSevpS5R13lCn5WvoaAhNcHn0ILcliGe_8u3xdkipxe_50hgGS_5z1mfvvl8XGGZ5Y73uVj_yjq9g8oChY1Uu3Zl1j6L3Iq2gSsGpM8am-IYrRGbvdRTfqm0VbtkeBswqQz89kkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/391b205ef7.mp4?token=kgw7vk0rMR1EBdos3ch0hpdA9JLk4AAdi0vW7eY2TQO9Qw3v_5F_GirqLCwIn0IJSKFc4m64i13w-r1qRyrt1uKUvX5NV2VllJvQjtDLd6kWfK4GmDt_ReiivAXCidpyRxDHgA4ZKNOoAPSK1aTfcOrp_2Fa6vZI4yjkRzACBcwJlPjvQ0UaCYQx-d-fpUzqlmxsZsOhjrlmjnJSevpS5R13lCn5WvoaAhNcHn0ILcliGe_8u3xdkipxe_50hgGS_5z1mfvvl8XGGZ5Y73uVj_yjq9g8oChY1Uu3Zl1j6L3Iq2gSsGpM8am-IYrRGbvdRTfqm0VbtkeBswqQz89kkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از بین ۱۲ فروند جنگنده رادارگریز F-22A Raptor نیروی هوایی ایالات متحده که در پایگاه هوایی اوودا در جنوب اسرائیل حضور داشتند، ۱۰ فروند در حال انتقال به ایالات متحده هستند. تصاویر نشان می‌دهند که هواپیماهای F-22A در پایگاه هوایی RAF فیرفیلد در بریتانیا فرود آمده‌اند، که احتمالاً یک توقف موقت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/133082" target="_blank">📅 18:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / ۳ انفجار سنگین در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/133081" target="_blank">📅 18:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133080">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری / ترامپ به نیویورک پست: در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/133080" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133079">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
براساس آخرین آمار پایگاه بین‌المللی هواشناسی «Ogimet» که وضعیت دمای ایستگاه‌های هواشناسی جهان را رصد می‌کند، بندر دَیّر در شبانه‌روز گذشته در صدر فهرست داغ‌ترین نقاط زمین قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/133079" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133078">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c4e411a5.mp4?token=G1r2rS_AKXckRlBILt85yXm4eT2EWv-kIh__PwDkolEkLq_E7ArIjN2laBETuSeDZJrWgdpPNA1gvtNUsFnLPZGylR-ZDLIyXnw8-TZmBhyvT0NX1RdEAK9QnHl-GF_l2a3hb3WFJTIFlmv0R0r-Xw4rec9vUyrJ54UnDojWxAfD27cyOGNI6SMn22y37WviA0PLirdbX0eUII47_sgbFz1iET630-CMnmvb7_wRAxtFFz8OLuv5-mrxKZ_dtmMekuQmrmxxSOGI0UIaUmuw6eUFANGs7kHW5V0PgKTuUwE0u1GvqeaADBTzCosQ2VqZXqy7YpZPn9pzLlKv68TeSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c4e411a5.mp4?token=G1r2rS_AKXckRlBILt85yXm4eT2EWv-kIh__PwDkolEkLq_E7ArIjN2laBETuSeDZJrWgdpPNA1gvtNUsFnLPZGylR-ZDLIyXnw8-TZmBhyvT0NX1RdEAK9QnHl-GF_l2a3hb3WFJTIFlmv0R0r-Xw4rec9vUyrJ54UnDojWxAfD27cyOGNI6SMn22y37WviA0PLirdbX0eUII47_sgbFz1iET630-CMnmvb7_wRAxtFFz8OLuv5-mrxKZ_dtmMekuQmrmxxSOGI0UIaUmuw6eUFANGs7kHW5V0PgKTuUwE0u1GvqeaADBTzCosQ2VqZXqy7YpZPn9pzLlKv68TeSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده چین در شورای امنیت: قطعنامه ۲۲۳۱ منقضی شده و بررسی پرونده هسته‌ای ایران پایان یافته است
🔴
قطعنامه ۲۲۳۱ در ۱۸ اکتبر ۲۰۲۵ منقضی شده و رسیدگی شورای امنیت به پرونده هسته‌ای ایران پایان یافته است.
🔴
اصرار برخی کشورها برای برگزاری نشست درباره موضوعی که از دستور کار شورای امنیت خارج شده، فضای مذاکرات را تضعیف می‌کند.
🔴
سیاسی‌کاری در شورای امنیت، اختلافات درون شورا را تشدید کرده و روند دستیابی به راه‌حل سیاسی را با مانع روبه‌رو می‌کند.
🔴
چین از کشورهای ذی‌ربط خواست با حسن نیت، مفاد قطعنامه ۲۲۳۱ را اجرا و از اعتبار شورای امنیت و دیپلماسی چندجانبه صیانت کنند.
🔴
نماینده چین با حمایت از موضع روسیه تأکید کرد که شورای امنیت دیگر مأموریتی برای بررسی موضوع هسته‌ای ایران ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/133078" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133077">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نماینده فرانسه در سازمان ملل: ایران باید به طور کامل غنی‌سازی را کنار بگذارد و به آژانس اجازه بازدید از تاسیسات هسته‌ای را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/133077" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133076">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نماینده فرانسه در سازمان ملل: ایران باید به طور کامل غنی‌سازی را کنار بگذارد و به آژانس اجازه بازدید از تاسیسات هسته‌ای را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/133076" target="_blank">📅 18:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133075">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/ترامپ:  با ادامه مذاکرات با ایران موافقم اما آمریکا به ایران اعلام کرد بدون تردید آتش‌بس پایان یافته!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/133075" target="_blank">📅 18:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133074">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXTVjzhv2olwccUxQyA9LPrYk6IMJOPbT4pRFjmfgot4buWCaPDdZ2rFNy40ecmOQJg-HLUmEjgmeBG_ZmhTOKuZTlI9XEgANgw4YZSvgjmGt3qLF5ZMKlBA352G9_Izcd6OuWPy9uWp_tD4naVwtnAJuVG50vlDtWWhzEGmD6A6zAp6FQEPoKlgvLJzHIoGwwukHbyAn9j-7b8aqlNGb97I6WX_OZW1qQCRA6sc8zWCU_03501Wr1qXei56oKjlSeUMXKbAw24MAlxMFeKxZSbwg675YmNCC-Mo9oFjyLcNF1Hk8Kiikc6zYu85zmbbugiDHpOxN2C5Kbgr3ngRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای به تاریخ امروز از ناوهواپیمابر ابراهام لینکلن در حوالی دریای عمان و ۵۰۰ کیلومتری تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/133074" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133073">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSCKxP5oDHeQqE3AqPtpCHM0Pa42manTE3hp6WtkSA2j55mjCd3m85yByXoac-ogx94Zv1fMrnZYRGVqBjysu4ZGIcB0G8EcJN_Q_UqciqRaNBLqPZmNoze9OiMUB-f-J434iw6pKM_2Nm9IubL0qaKgGeSK7IWsxEwmALJDRasZX1XaVqhD2ggqiluuUiSEZpot0Cc1uylfYrZJo7Xdl7MZEE9WpR6hSuqRbCPMBHb16lhlOwc1ksz4rDCIrhbOZqmngSluoF79kJau7BADJBo2BnBlSrNbs95Qx7L1iB5dVu7jZ3sdaOcYIhAyuVEzCPzhSt5oK1gSFooy_wN0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور مجتبی خامنه‌ای در مراسم
‼️
🔴
امشب، موقع برگزاری نماز میت برای علی خامنه‌ای تو مشهد، یه فرد با صورت پوشیده و ماسک، سمت راست تصویر و بین جمعیت دیده شد
🔴
اطراف این شخص هم چندین محافظ ایستاده بودن و همین موضوع باعث شد توجه خیلی از کاربران فضای مجازی بهش جلب…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/133073" target="_blank">📅 18:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133072">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlHAf15YX-dez7DIbqUKVpoQqScihuRvOZWbxYlWuzpavwJLq5OsfVC-RK8dUlHcIEOXZfmA5Gdi-s1Wc3n7m_nmttSQXT8fC3Vc3xI9-LJ5VbDm3W3iCi1F7-bieqTPMUD2qFGBRQedCvKpLhMT81_zHpx7uus1TR39ID3qhM3xZnJzwON-Tyji4-ObetMnS94tnMTFMWhyt7iqqXUFcZgjGX_3EGIKEZE-QJ_1d9HKmDuYXRO7fWUi_q3sGLep2Dxu6Dykpes1QnDreISQlqL81_WFux35I8rP_agH0znZN8bNNjMIWeQ6V_48zTVIE9-vYNbQFNtkVgSgHp9Qjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره ای از پالایشگاه ساراتوف روسیه که واحد اصلی تولید بنزین آن تقریبا نابود شده است
🔴
این پالایشگاه تا اطلاع ثانوی فعالیت خود را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/133072" target="_blank">📅 18:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133071">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
روس‌اتم: ۶ نفر از کارکنان ما بازگشت به نیروگاه بوشهر را آغاز کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/133071" target="_blank">📅 17:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133070">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmvI3xjcoT6m-DVirIO1PnySV3MYck8Q2Q4ZSrxwbBvMz6oqON43L_Fw-ILjoInNTPY5gChSu8bE1gC-oKWHjyfnWGFoXq12zELBaS0Zl0wGcmJxNP1RLq2DEsqJS85MlCQ9YrFahIzhwrSYlWa6zKhKH3lcgycTqp7Zd8uxmrt5a3db2uml9NiBiea0uhV3EDgZtBunf82-axLwNVbExyG8dL4Jg2oJkQUrWEEMylOXxH2BfBPMJHE8iw4UFRI2pzcsC1MM_EFFtM5EaMi30hbxKRXuKXPOJZLVM2YxqhufUt3Pcx5Tw7IWzb-nDrjt3rhXxPDhnYlJA1XzC5x_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد هواپیماهای نیروی هوایی ایالات متحده که امروز در پایگاه هوایی شاهزاده سلطان در عربستان سعودی مستقر هستند، به کمترین میزان خود از زمان آغاز این استقرار در اوایل ماه فوریه رسیده است.
🔴
آخرین هواپیمای نظارتی E-3 در اوایل این هفته از آنجا خارج شد. در حال حاضر، یک فروند E-11 و ۹ فروند تانکر در آنجا باقی مانده‌اند.
🔴
به نظر می‌رسد که ارتش ایالات متحده بار دیگر فشار خود را بر ایران افزایش داده است، و به همین دلیل، بسیاری از تجهیزات حیاتی مورد نیاز برای انجام عملیات‌های بزرگ، از این منطقه خارج شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/133070" target="_blank">📅 17:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133069">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
طبق تصاویر ماهواره‌ای یک ناو هواپیمابر آمریکایی به همراه حداقل 3 ناو جنگی در اقدامی عجیب به فاصله کمتر از 300 کیلومتر از سواحل ایران رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/133069" target="_blank">📅 17:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133068">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رویترز به نقل از سه منبع نزدیک به کرملین : حملات اخیر پهپادی اوکراین به پالایشگاه‌ها و بنادر روسیه، عزم پوتین را برای ادامه جنگ بیشتر کرده
🔴
پوتین در زمینه تصرف باقیمانده منطقه دونباس اوکراین پایش را محکم کرده و مشاورانی را که پیشنهاد آتش‌بس در امتداد خطوط مقدم فعلی را داده بودند، توبیخ کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/133068" target="_blank">📅 17:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133067">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjxBry6Gf9YZ2dzVFli4WJhPbiW0ziiD-mi89i3rc_YyYCFGCi0a-mpPYjNbaSBDvcWnWhVKnZuXHBmhvkUviAQWl614ombuNSBg3FfjVPbAJNfIs1c1rLCbxRFXwEF_w-U1IExRB6xiOooFLErBq_1HsetjOXzj9s4SRMCdRBPGfYmkqiOTbJcqISHdcxehyZYiEyXJKZ8eseXzgnkfJonJewYU8Bhqq1YjMZXYaZ1wNqlRcNa8bilmHMkcbVy2wYVMD3vPuZhXwePzw3O49q2jwI3uiJTHlAAEv4yrgWtJTnLWKYmqrYydo3BNmjkRBBINjgSVxWvgsJdseY3YrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق تصاویر ماهواره ای منتشر شده؛ ایران مسیر های منتهی به سایت هسته ای فردو با تپه های خاک مسدود کرده تا مانع حرکت سریع با خودرو به سمت این تاسیسات شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/133067" target="_blank">📅 17:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133066">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شرکت ردیابی دریایی کپلر: فعالیت کشتیرانی در تنگه هرمز به شدت کاهش یافته و تنها ۲۲ تردد تأییدشده در روز پنج‌شنبه ثبت شده
🔴
تنها یک شناور از کانال متعلق به عمان استفاده کرده و مابقی از مسیر دریایی تعیین‌شده توسط ایران تردد کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/133066" target="_blank">📅 17:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133065">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti3Q_g-3auUfqmsOtBRWcb7b3n47FmocPMdhWYli0xloXKfCdZamL9b2JKFhqa7aQcHeRGGXY3k_IQeEyyP6JkYQwh7G05q_mZkl-ZwfFXdIGVclS1AioJo1xLSqLViwl0hI541x05m4BADSZxJAKnLLHIguP2J4S6-FcvMXJgrCXAtmDb7KBHAzGkwdvWra7wChfk3C27XTorQsx_NHrwNhSWOZwrM4rji12d_nrLGr6hzwJwO965t5nnEuWOqgqam0QPpyOr8Tx9-PYgcedAT7qtSmleR3JDkI8PLx4_ol4tCmvGQrREL1yfrcsXNNEgKByVEEwmDvOGOAsdlQZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیویت، سخنگوی کاخ سفید:
جوون‌های نسل Z که از وضعیت اقتصادی و زندگی تو آمریکا گلایه دارن رو بفرستید ایران؛ خیلی زود قدر آمریکا رو می‌دونن و دلشون می‌خواد برگردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133065" target="_blank">📅 17:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133064">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-DABUYM_vyW80kqCWsRK4IcYOhGyvx4YNJK90pOvy7m_PLRInmiW3O2PARoWwIv2NwB7ZrdmWNFjkuE0YqV94gicDvxaeen4Os2UTqTqLj4iS-QV2x9emIEsschY-48Ulw3NslrfKuTePX0dciZqSIm1cb_OY8YtvPS0FQkefXpH51G_qQQ-Dx0cYiqnw_GAOSR7qys4_gLog3k_0MWEN7v2zPplOnVSleXqolJChEjA_xAs9Qx84jtBj9opDa0VcwywR9RsSinMIZrCw1AraxjviH2-gkLucPF50K9rsFzddCjtrQT9e4Ozq2A3hbYrGqiV1Jbn13vujnXD8FhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اهواز(مگامن): هر کی موشک و پهپاد داره، ترامپ رو بکُشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/133064" target="_blank">📅 17:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133063">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پشمام
😐
بعد از برد دراماتیک آرژانتین گروهی از طرفداران زن این تیم در استادیوم لخت شدن
😐
⚠️
⚠️
مشاهده بدون سانسور فیلم</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/133063" target="_blank">📅 17:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133062">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری/ خبرگزاری CNN:
دولت ترامپ در حال بررسی آغاز مجدد محاصره دریایی علیه ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/133062" target="_blank">📅 17:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133061">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnKaTNErB2Vo2PVPoh0w1RXCAPcr7O9fYHK1yeUr8c9Kb8PlkV9Vo1p7nh1abtxOAW55Z9PfO1k7Z8B5LYMbV2OKcC0b3PPEQXbaSwjKwJxokiqQvUsnJsXPZvc44K7SK0kiaOOyhbzt-Up3q3mxY_B7X102S-hnnlzNa3ZbKOqokozC2KMZBc-FpgYqgftpqd-35eO_aIQhGk7Q2SEvor3w0uRAkLnS-Qa9l6UX1HXo9lcWV5PsMhdW2NV7q8P9q5qntvvvyWGB9CtDkcrVctM6rC3aKvEYFuPDrh-CIv2EsavATDncrmX5RQR9mrdbHN76r6UxzrDlXZcV8Bmldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله آشنا به جلیلی:
انتقام اول شد؛ نان و زندگی مردم چندم است؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133061" target="_blank">📅 17:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133060">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwbLQBVjfpptnIg7URbz7gHUdvQrIfklYzdzbKpfGuTRS4o4SZuDVNuegmVtWNkxt83q1eHXcWDOirygho-20hGIVe7igYmvx1afCx3f7x664jSn9YnqBaDOLccRi7xNdl4Nhc2AqhFNjwr9zoeRKZo71H4hsz32hqY6wVx1NX1vgCRxgglPrar9yF6aTA3XVq-D5S1QKWY9opCOAWr6zsl9TqQe9Gs-dA23mx-iloifHYUvHwzhoIu0ksHLVijSHL5iHWRdBlj4GoVlgE5QJzRrAle8OQLoE47L00Bu0azSAjmzPylYbMgiXxEaSxXIUw8ci4IzAd3_G5gQBloa0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین تصویر از محل دفن علی خامنه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/133060" target="_blank">📅 17:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133059">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc5b51f6d.mp4?token=luO0F9EIquuD6rCpJepeWyRNS8FwFP3un1RdbAVm_EA56fk-cLM49OPdCd8CuQXrSkfJJpZMwSBH63uFHh2fFVtNdp3BL7AIQFA0jLo46OqOZbfOeoEaLX98Euf1nO5FGjWaZ4DuhiApLepjvN5aHOXVzOS93CKnQSoMChYwUisRtSSJGUWP3S48CKlxHL80aFIQjw4YW1a4bHu9u9sUZoKuJR66E0VtovAoWsykAJ7DYj301Jr26yHXN4OhNjwHzJ6aa1AamkUcjQydzEnts6TJ0orRKGUlIDKNdZDSCpDiwkPEuuVt0RocnHtzOfq_q5KnbjRRD2OaBSRU9BgKTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc5b51f6d.mp4?token=luO0F9EIquuD6rCpJepeWyRNS8FwFP3un1RdbAVm_EA56fk-cLM49OPdCd8CuQXrSkfJJpZMwSBH63uFHh2fFVtNdp3BL7AIQFA0jLo46OqOZbfOeoEaLX98Euf1nO5FGjWaZ4DuhiApLepjvN5aHOXVzOS93CKnQSoMChYwUisRtSSJGUWP3S48CKlxHL80aFIQjw4YW1a4bHu9u9sUZoKuJR66E0VtovAoWsykAJ7DYj301Jr26yHXN4OhNjwHzJ6aa1AamkUcjQydzEnts6TJ0orRKGUlIDKNdZDSCpDiwkPEuuVt0RocnHtzOfq_q5KnbjRRD2OaBSRU9BgKTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افشاگری رضا جاودانی از علت کناره گیری خودش از مردان آهنین :
🔴
درگیری بسیار شدیدی میان همراهان شرکت‌کنندگان رخ میداد، به طوری که یه روز نیروهای ویژه دور تا دور محل مسابقه مستقر شده بودن و تعداد زیادی سلاح سرد و شمشیر ، قمه و چاقو از همراهان شرکت کنندگان مردان آهنین کشف شد، منم ترسیدم از اینکه این فضای خشن و خطرناک تو مسابقه وجود داره و دیگه کناره‌گیری کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133059" target="_blank">📅 16:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133058">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4zo1Qy_GrPXM4FQvusYOH1Z9gw2LLAGLitWrY4icnA4srG7zKLH8caUkSzvzDEKpCYGZRMvyjjpy1oI8sUZNc5GCVUsHgzkrze-h3Nifvto27uQEzn_wd_rSvoIbBdzak6MV6Czaz8LTrEKid8r7aYf-meUaFC8nFjz_od6gdA3AHrZbFwqdDd-Lstss-I1cemuyi44yJ86OANJeTIi0UVHa7pUIEX1UDwXvO05CGwDTWU8Y4itGBLYZzFZKS0GcNfJZuCuiofIZLTau0nVVd8zUKUfDgtbGdgQYgfAmoX5gyp6w-X_kMKSdXeZJ3Vhpv-4ravCFvREODFMRFN64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی ان ان: ترامپ نمی‌خواد اسرائیل تو حمله‌ها به ایران مشارکت کُنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133058" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133057">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
تهدید آمریکا به انجام حملات احتمالی بیشتر علیه ایران
🔴
یک مقام آمریکایی امروز به سی‌ان‌ان گفت که واشنگتن فهرستی از اهداف در ایران را به عنوان اهرم فشار علیه تهران حفظ می‌کند.
🔴
وی در این‌باره مدعی شد: «وضعیت [با ایران] متغیر است و در صورت لزوم، حملات ممکن است از سر گرفته شوند».
🔴
این مقام آمریکایی ادعا کرد: «واشنگتن عمداً حملات را متناوب انجام می‌دهد و سپس برای جلوگیری از تشدید تنش و دادن فرصت به دیپلماسی، آنها را متوقف می‌کند»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133057" target="_blank">📅 16:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133056">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpX7vECth7cbGwS_pcgLE6MAids0ECTOlmt5vhobiYEnL-FmZ_tIXlZkZgIzVsn4KlkPyFML_fI6u8vL0K6Iwb_hgSiP98beecdkxEO2S0HPbn5iOgENaCLqS1tfOq02skEip11R1moKGiQt7VPBCZiXfSNCHYEQiPbvZwrZSiGFiJW2VCeoEaAMQ4p04r4U0IEL3QJaPSYOywEMyuXR2hTHCn8qHxavgRYRKVv0FJ9qSEXufMil1z5Gqpw2RcJKhIUvqpeK9lPjJITaUTOB1T8L6Und3Yb77NZONs2jH0PyJkMSeNkNqWL1NVOMHx4Of0SNtVtfjHRRHH-oy3VFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
فهم امثال ما از زمان فعلی بیشتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133056" target="_blank">📅 16:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133055">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رویترز:
مذاکره‌کنندگان قطری برای کاهش تنش و تلاش برای ازسرگیری مذاکرات در ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133055" target="_blank">📅 15:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133054">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
هواشناسی: تو روزای آینده دمای جنوب به ۵۰درجه و تهران به ۴۰درجه میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133054" target="_blank">📅 15:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133053">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
زیدآبادی: قلاده تندروها رو باید مهار کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133053" target="_blank">📅 15:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133052">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
معاون وزیر آموزش و پرورش: دانش آموزها بجای کافه گردی برن درس بخونن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133052" target="_blank">📅 15:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133051">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX7xuAT0qkOwUNEUxtc13xLUEn-k2MW8tQcqIkZArDVqwsYUWclp3gvFhiTcqSU1RF9yddyjmqtzhvD4soU4jj4Fuyjsww3HwcB6tfLLWRHiBqjTZF7HCvB0R-Y_KbcOdwnXVGAqlo-F2yPgMqjQYIf83QF_jurm6q03ISuQjv-8Vshbw43xliwtZQM-rFx_yzerEV_LtBlFVginO89jQMAz7gVBXurgNZCrMbE3_PdncS6Qgo9pUyW7UOaup41csOmfwNVdJjdcB8SQnmEe7AzOS0B4ES-OoF6gr2dSmTg_B3Hi6WbjE_vcGmIKf46KUYfoLtdC5sprplNdHjWfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی:
برخی می‌گویند ما باید اموال ایران را آزاد کنیم؛ بزرگ‌ترین دارایی ملت ما رهبری عزیزش بود و باید انتقامش را بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/133051" target="_blank">📅 15:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133050">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5c47f340.mp4?token=CpMRJsubCdXnjMijKwiaMz242i0r4gUToRjf7fLUH9LbQvfaOIU4c29gNWRZqpcgGMMem-zuNpnPJZv4HN7Ma9ah-P9-qmeliSQ2Z_QKsjjLdL7WAmkLxUJkb0tu3LWAjy0xik_Qa82gfcdQn_6YFWHDERLrTygPzixdjYpobQO_hWzpUZpAB_MERrk5SD-VqtBpHSK9LJTioYDObB7zcDZN7iFj1BkeX2xC0FwfmepdpMdUL334brQOBsQQkOpQ_BSuOsBOxsM9rUANylyhvrqDXJPJIEEqxwAECpFF4VFqzI0IIYQfcONSYdnc6745Lu8LG3gk_bTgLOe0GC-Jcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5c47f340.mp4?token=CpMRJsubCdXnjMijKwiaMz242i0r4gUToRjf7fLUH9LbQvfaOIU4c29gNWRZqpcgGMMem-zuNpnPJZv4HN7Ma9ah-P9-qmeliSQ2Z_QKsjjLdL7WAmkLxUJkb0tu3LWAjy0xik_Qa82gfcdQn_6YFWHDERLrTygPzixdjYpobQO_hWzpUZpAB_MERrk5SD-VqtBpHSK9LJTioYDObB7zcDZN7iFj1BkeX2xC0FwfmepdpMdUL334brQOBsQQkOpQ_BSuOsBOxsM9rUANylyhvrqDXJPJIEEqxwAECpFF4VFqzI0IIYQfcONSYdnc6745Lu8LG3gk_bTgLOe0GC-Jcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مراسم تشییع آقای خامنه‌ای، یکی از حامیان حکومت سعی داشت مثل اسپایدرمن، جلوی ماشینی که تابوب خامنه‌ای رو حمل میکرد، بگیره اما موفق نشد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133050" target="_blank">📅 15:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133049">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d349e1e2a.mp4?token=vTfeEfBO1S-_UHW_Iq6gO_5S200EFhdHZUrkCxsoaL21RQu2F98Jp9uPKOBra5LA8Ecemv5d-jNnDAwolMNiCprTCXl_tB9JA0jksZ-IIlCqdWwRdT1n9RsARLVGik_jgSHISIVsx4rwtL_cp4YpUu-oAdRXejg2ctOsO-_cT-ewpRKRuCrX43VU5ywJbOMG8su-bVCfNM0t2fdkwHGQseEnNJnQVIw39ku3F8KcTOOFsbP2ZjXlIWg6vcg6eBSvoQZWCWBUdSSLrupkKIJCWUYcUPLPBfDlMYBzGUKt-LYvqilM_QeMwitL1jaNRcfHNmGPbLXBTqY60vvja6nfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d349e1e2a.mp4?token=vTfeEfBO1S-_UHW_Iq6gO_5S200EFhdHZUrkCxsoaL21RQu2F98Jp9uPKOBra5LA8Ecemv5d-jNnDAwolMNiCprTCXl_tB9JA0jksZ-IIlCqdWwRdT1n9RsARLVGik_jgSHISIVsx4rwtL_cp4YpUu-oAdRXejg2ctOsO-_cT-ewpRKRuCrX43VU5ywJbOMG8su-bVCfNM0t2fdkwHGQseEnNJnQVIw39ku3F8KcTOOFsbP2ZjXlIWg6vcg6eBSvoQZWCWBUdSSLrupkKIJCWUYcUPLPBfDlMYBzGUKt-LYvqilM_QeMwitL1jaNRcfHNmGPbLXBTqY60vvja6nfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سید علی خامنه‌ای، ۲۲ مرداد ۱۳۹۷ :
به طور خلاصه در دو کلمه به ملت ایران بگم : جنگ نخواهد شد و مذاکره نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/133049" target="_blank">📅 15:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133048">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJjqXrqA4wxS16kwzsmL9v5019FEQ3VKE7VSlQ1FXRWzDTKice7Og0a6E24P0ZnHh7uZQRKmltNQz1WkHEvs_l6xCQ2WH1PXEplrVPZ7U8HtXWWIaJxxqThnGurHNx4E7xhVxWertxEymi1jEEcEAmtGgQ-hcnPB4uWgJrol_36jc88oMb5I4tIRWnBMmWCFS4oSeyMCv7Djtux_yD0AA-EWYbmxzsavBq5iaoQIEQAFomMHrxkDRA-rXCEkligfol74tPsXYZECzY351-0BRkKrTOqsiC-rgObYM7nf8pSJtXRNLNofhpRsF0YC1quzl_DCGhNyIOZbO2zzCsHjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر شورای‌عالی امنیت ملی: با حمله به زیرساخت‌ها مقابله‌به‌مثل خواهد شد و رژیم تبهکار صهیونی هم از پاسخ رزمندگان در امان نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133048" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133047">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
به گزارش بلومبرگ، اتحادیه اروپا در آستانه توافقی است که به اوکراین اجازه می‌دهد از بخشی از وام ۶۰ میلیارد یورویی اتحادیه اروپا در زمینه دفاع، برای خرید سلاح از شرکت‌های بریتانیایی استفاده کند.
🔴
احتمالاً این خبر طی چند روز آینده، و احتمالاً از روز دوشنبه، در جریان جلسه ائتلاف کشورهای داوطلب به رهبری بریتانیا و فرانسه در پاریس اعلام خواهد شد.
🔴
بر اساس این طرح پیشنهادی، بریتانیا هیچ هزینه ثابتی را به عنوان حق دسترسی پرداخت نخواهد کرد. در عوض، لندن کمک‌های مالی را بر اساس ارزش قراردادهایی که به شرکت‌های دفاعی بریتانیایی از طریق این برنامه وام اعطا می‌شود، ارائه خواهد داد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/133047" target="_blank">📅 14:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133046">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c5dfe512.mp4?token=eCKs1qTM0z14jmxdZPZjeOOeOJwL_Y7YcmezXADHLV5xVDV_o7AO906qjDeIQVbwBFgl3Egf71YGtN_aVVuiYqDFpCUGtrQDBBIeaH9VGwaEmwu3_NbD-eXBgrW6fSicnyjON0fFc1UHK-wm7tP7zq6igPzAHJrH8vPRqLX-bMQKzWaAlePtlzdXVINL0EkxpEIxlCAhIk_C3_RIoNlqwJXXcDW4BQTOYZ5sZ4s5YkxnbDOIjQPJNEynW93Gzcl_EcWc5KW_nbpm16MqEsky1WpZtmZAiMifB_lUx6rTmJu6F7KkWmPLW9z4a6aCsO61qnKHVR70DoSAlwsKLeWT2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c5dfe512.mp4?token=eCKs1qTM0z14jmxdZPZjeOOeOJwL_Y7YcmezXADHLV5xVDV_o7AO906qjDeIQVbwBFgl3Egf71YGtN_aVVuiYqDFpCUGtrQDBBIeaH9VGwaEmwu3_NbD-eXBgrW6fSicnyjON0fFc1UHK-wm7tP7zq6igPzAHJrH8vPRqLX-bMQKzWaAlePtlzdXVINL0EkxpEIxlCAhIk_C3_RIoNlqwJXXcDW4BQTOYZ5sZ4s5YkxnbDOIjQPJNEynW93Gzcl_EcWc5KW_nbpm16MqEsky1WpZtmZAiMifB_lUx6rTmJu6F7KkWmPLW9z4a6aCsO61qnKHVR70DoSAlwsKLeWT2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز تو پرواز یونان به آلمان، یکی از پنجره های هواپیما کنده شده و یکی از مسافرا تا ناحیه شانه از پنجره به بیرون کشیده شده!
🔴
همسرش حدود پنج دقیقه با گرفتن پاهای او مانع از بیرون افتادن کامل وی شد تا بالاخره نجاتش دادن و هواپیما هم فرود اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/133046" target="_blank">📅 14:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133045">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
به‌گزارش یسرائیل هیوم، دونالد ترامپ به‌دلیل نگرانی از کاهش شدید محبوبیت خود در آستانه انتخابات میان‌دوره‌ای، قصد ندارد جنگ با ایران را ازسر بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/133045" target="_blank">📅 14:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133044">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
به گزارش نشریه "بِیلد"، سرمایه‌گذاران قطری، مانع از مشارکت پیشنهادی شرکت فولکس‌واگن با شرکت "رافائل" اسرائیل برای تولید قطعات سیستم دفاع موشکی "گنبد آهنین" در کارخانه "اُسنابروِک" این شرکت شده‌اند.
🔴
شرکت فولکس‌واگن در اواخر ماه آوریل، یک توافقنامه اولیه با این شرکت دفاعی دولتی اسرائیلی امضا کرد، به عنوان بخشی از برنامه‌هایی برای بازسازی این کارخانه که با مشکلات مواجه بود. با این حال، "صندوق سرمایه‌گذاری قطر" (QIA) که ۱۰.۴ درصد از سهام فولکس‌واگن را در اختیار دارد و ۱۷ درصد از حق رای شرکت را کنترل می‌کند، با این توافق مخالفت کرده است و دلیل آن، روابط پرتنش بین قطر و اسرائیل است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/133044" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133043">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6WW7rESMVZ6T17GXlFwLG-10NCEKRgxcn7qWPrcEDicpekm6qLi6fXfrRyb5-xLX3P5JqxVe7GeaEZhfeTEtkQIlso9Z7a7CrECH6euQ0YYT0Jt2yq17rvsuvoBx_XjyduKN8UhEAzpKMGHCmBZ-7V7p_Ybw89-6iJwBMlDFZ8XqqEFCS3u_w5_imXYx7vB1J_bG40OWU_eZepqz8gVi2zsR9h2D438DgWD29q9zVU9Wsh75jkwPdDP8uQea8mTVykAuMEk5fghWERSCNOH3wMzwIyQ7H7sp57_fbXwJivZjtaliiuAN24rgo4p6PwaOe6_LhbmMlWxe4efqi_Rww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: تصویری شیطانی از من ساخته‌اند که سزاوارش نیستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133043" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133042">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / سی‌ان‌ان به نقل از مقامات آمریکایی: گزارش اسرائیل درباره طرح ایرانی برای ترور ترامپ ممکن است تلاشی برای وادار کردن او به تشدید تنش‌ها باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133042" target="_blank">📅 14:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133041">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۴.۳ ریشتر کهنوج در استان کرمان را لرزاند.
🔴
در ساعت ۱۰ و ۵۹ دقیقه امروز جمعه ۱۹ تیرماه زمین‌لرزه‌ای به بزرگی ۴.۳ ریشتر کهنوج در جنوب استان را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133041" target="_blank">📅 14:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133040">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
طبق داده‌های انجمن اتومبیل آمریکا (AAA)، میانگین قیمت هر گالن (۳.۷۹ لیتر) بنزین در آمریکا در بحبوحه تشدید جدید تنش ها در خاورمیانه، پنج سنت افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/133040" target="_blank">📅 14:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133039">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شورای عالی قضایی عراق: روند پیگرد مفسدان مالی و اداری و بازگرداندن اموال دولت را دنبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/133039" target="_blank">📅 14:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133038">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرنگار الجزیره گزارش داده است که یک پهپاد اسرائیلی به خودرویی در شهر کفررمان در منطقه نبطیه در جنوب لبنان حمله کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/133038" target="_blank">📅 14:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133037">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رئیس کمیسیون امورداخلی کشور: تنگه هرمز به شرایط قبل جنگ رمضان باز نخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133037" target="_blank">📅 14:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133036">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نخست‌وزیر کره شمالی به چین سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/133036" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133035">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d1fc7f0e.mp4?token=pzrpk1JI77YpeugdUAYifNL39LbdMcqmNGiA-ZDtDdk8xaPcoBEwSU-_LYe5J57QdUTLmvavfiI9XLwHuwL1LuBZXvq_We3nE82xEKsD644lARJAiHNgYIUkw-LiTgP3opYhwuN_G92saIRAFVUiT_EUeNWL76epnC3rGWWjXiwpfxuogBk-GBrBN3ZZOFSQgxii9rIcDuVrP18Vzw1Chdvebz_niI0IfLX06LF54efwND_jWef6CVpOMJTMucIyYpB-coG13g7zOeMkrMJCm4mgLZKFOLfN3X2tyGrtDpzp65IRLigrOsudMNcjBfHrpuDqaWlwQB2-nQw4A9BCCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d1fc7f0e.mp4?token=pzrpk1JI77YpeugdUAYifNL39LbdMcqmNGiA-ZDtDdk8xaPcoBEwSU-_LYe5J57QdUTLmvavfiI9XLwHuwL1LuBZXvq_We3nE82xEKsD644lARJAiHNgYIUkw-LiTgP3opYhwuN_G92saIRAFVUiT_EUeNWL76epnC3rGWWjXiwpfxuogBk-GBrBN3ZZOFSQgxii9rIcDuVrP18Vzw1Chdvebz_niI0IfLX06LF54efwND_jWef6CVpOMJTMucIyYpB-coG13g7zOeMkrMJCm4mgLZKFOLfN3X2tyGrtDpzp65IRLigrOsudMNcjBfHrpuDqaWlwQB2-nQw4A9BCCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یک مداح به قالیباف:
بی غیرت، بی شرف، عمرسعد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/133035" target="_blank">📅 14:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133034">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔔
تبلیغات قفل ربات الونیوز
هفتگی 250$
میزان جذب: 30kالی40k باکیفیت
سفارش دایرکت</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/133034" target="_blank">📅 14:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133032">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بلومبرگ: مذاکرات فنی بین آمریکا و ایران در مورد توافق صلح دائمی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/133032" target="_blank">📅 14:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133031">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ob6nsJFsbLzQBMEoM8P_39NGq4av5lkbs3hCLyGJHjzkamtLAjbBeFWubPmvp9uXRjkm4YynyV-cnCx1xYqthOuB_eKnwI-5VS3FFA_otj1HKcaiYw1BvfZOP8unnmQ2nm-dPUCWdhWZKKSZIMi74jSsfjnYuZrlVjr1q6eKtzSFjTnhrn1sCX1qUREEnimfuctDNAW9cEfIXlrFPscewP1No9cdJp8BfccgyDCcW_VmYm1GvK2suI_sbQ5nMZaCn1EaGwh7AI4V38EeDRLp7JPMZN-ng6_a-0t6iliLEhDAst8jUkNYxmU9mzdTwTrM1fMV788GLk1jpWhRBP4LiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزش یک میلیون تومن در طول سال های مختلف
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/133031" target="_blank">📅 14:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133030">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترکیه اس-۴۰۰های روسیه را به کشورهای خلیج فارس فروخت
🔴
یک روزنامه نزدیک به دولت ترکیه گزارش داده که آنکارا سامانه‌های پدافند هوایی اس-۴۰۰ خریداری‌شده از روسیه را به یکی از کشورهای حاشیه خلیج فارس واگذار کرده تا راه را برای دریافت جنگنده‌های اف-۳۵ از آمریکا…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133030" target="_blank">📅 14:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133029">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رویترز: پوتین آتش جنگ علیه اوکراین را شعله‌ورتر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/133029" target="_blank">📅 14:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133028">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
روز گذشته نیز ارتش اوکراین دست‌کم 10 کشتی تجاری روسیه از جمله 7 نفتکش را مورد اصابت موفقیت‌آمیز قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/133028" target="_blank">📅 14:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133027">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
عملیات دریایی بریتانیا: سطح تهدید امنیتی دریایی در تنگه هرمز همچنان در بالاترین سطح خود قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133027" target="_blank">📅 13:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133026">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کاخ کرملین اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور روسیه، تا کنون با دونالد ترامپ، رئیس‌جمهور ایالات متحده، تماس نگرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133026" target="_blank">📅 13:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133025">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga3QA03utp3wEzBuKJJz35U5zU8XepPKXy2s9hpA4TbisVDnbY7IKoXF_xlRndO9PpxomwlugSIm8xbtYZsocYy2Qtdq8xwL8dvB_1riidJ3heIHjVmDYqaoYgAYsLdatGKOejcLF8k4PsTs7YRe7szkp5QyvWpM77MJhF_xH0jKDItLRpRAxpNhQWdUBVQe12QcEl03STUp1KXUb5HGvKs5Y9FOis3R0tKqqe4E37VPQtIqYZmrri-YpDJ8cb9FKgrNfgG3PUkxgmKDdL85KKqMd8V2x55MLuV30fyl95IRJtJp8hHcXh2QCxJKjXX621ln_9AA680CNV3G7R5ugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم پناه، معاون پزشکیان: بعضی مداح‌ها یه میکروفون بهشون رسیده هرچی دلشون میخواد میگن
🔴
اونا هیچی نیستن اما جو گرفتشون و فکر میکنن تئوریسین دین و سیاستن
#مداح_بیسواد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/133025" target="_blank">📅 13:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133024">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
گویا فرمانده نیروی دریایی سپاه به دلیل حملات به کشتی‌ها، توسط شورای عالی امنیت ملی توبیخ شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133024" target="_blank">📅 13:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133022">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری/اکسیوس:  ایران و آمریکا از طریق میانجی‌ها توافق کردن فعلاً به همدیگه حمله نکنن و برای حل اختلاف‌هاشون، به‌خصوص درباره تنگه هرمز، دوباره پای میز مذاکره برن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/133022" target="_blank">📅 13:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133021">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJLgv2v4kK2LHl-ysYZANQXKQfb-83YgkKCu9LerQtBbd_Ny_lKcdf3q5CQ6GrLqYGTTI5gBHrJM6ytajk1mQNRi3SC6NgpK2cyB1R16ztfDv7AdinXklJsA8JMTiw9o4b3f0SNAKIIiJgD0W3YpC9XU_hyJFhyciLCpoG_HcaY77_pDfspzkx3nNkkpO9nQ0_NuKq3JoNl81C_zTvB4UCa6j1-Ow_zmDRAGW4GuRGkWinU6N_vtMsZhTQHnv51QmGbXG1qE5uQ_L1u0JwfpEct4XlRuqDn7PJ9fU9vSIGQGH4IgjEpKqhYhKFKHDM2pt_wGIfeN7JR-0WAoAdxuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: یه انتقام مشتی از ترامپ تو راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/133021" target="_blank">📅 13:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
مدیرکل هواشناسی خوزستان گفت: تا پایان هفته آینده روند افزایش دما در استان پیش‌بینی می‌شود به‌طوری که از روز دوشنبه وقوع دماهای ۴۹ درجه و بالاتر در اغلب نقاط استان مورد انتظار است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/133020" target="_blank">📅 13:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133019">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
فرمانده ناو هواپیمابر «لینکلن» در دریای عرب به خدمه خود دستور داده است که آمادگی خود را حفظ کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133019" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133018">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eULMZy23s3cp71tk6MUBuXF6kZCuneMH-Sez22iNj-kLCez97bW7KBnlp5oZycqrgWE3byjKWm2Hx_sspaJyIln4lYLrzGbqI5xYy31G_CXVhhTFqTxTNA0H7kKcph1kytWeGACZh-S1ctcRLbtF6B60Liapt5X_IjgQiyy3CVXwMN9g2wUD9zws4_M2m8aIsrQuIewKqP3Yjjc1iYf12GEKm13YuBp9ZG2Hewiq5v9zg9r2aPPOpg7klvenkiLuaHjpArzQTZ4g2dalCC1Bn2J4SgIlkGW8xGiUCy733zTvhQmNJBJPgDsWX_82Fi33muclxIku8A7LGIU-Y-aBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: در خصوص (راه آهن) آق قلا حرف و حدیث‌هایی از خرابکاری به جای حمله دشمن البته وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133018" target="_blank">📅 13:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133016">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5ace0db3.mp4?token=c3cM215dLMDCOs8Sh4wzCt3P1H-4fSJwmGnq7uhvq3M5AsCmNIUuv_FtPW2qmK1OErv68GqrMdrUpbtIYX7LHamPdKlgn8oEuBZnkk1mqvA4boAyhlSFJt3HlYvUGkpYBfefnp38jRFMWXN-VEu6fXJShdf2zgUAvOwbF11DaIKc5lkS_h8M6yGwuxIJzEbRUDQ3raGPa9Pu4Az8H5jHLd31OgYdU3D3C1cyJ-t97DgTG-D3BrbITTNctYjRKD0zaqHgfphAn694Y9eKusj3VxxdNTNwJbeWPgCmfc2MUSDBSIPqfwhBAs_9pi_rG1ykWpc5tLYxJ0URgY3H-sD8rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5ace0db3.mp4?token=c3cM215dLMDCOs8Sh4wzCt3P1H-4fSJwmGnq7uhvq3M5AsCmNIUuv_FtPW2qmK1OErv68GqrMdrUpbtIYX7LHamPdKlgn8oEuBZnkk1mqvA4boAyhlSFJt3HlYvUGkpYBfefnp38jRFMWXN-VEu6fXJShdf2zgUAvOwbF11DaIKc5lkS_h8M6yGwuxIJzEbRUDQ3raGPa9Pu4Az8H5jHLd31OgYdU3D3C1cyJ-t97DgTG-D3BrbITTNctYjRKD0zaqHgfphAn694Y9eKusj3VxxdNTNwJbeWPgCmfc2MUSDBSIPqfwhBAs_9pi_rG1ykWpc5tLYxJ0URgY3H-sD8rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در کارخانه کفش چین دست‌کم ۲۸ کشته بر جای گذاشت
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/133016" target="_blank">📅 13:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133015">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aa971ff94.mp4?token=k6-powcpr1ao2HvCO6LzKDhlHZCKuWmq4TRNfscxQv_p338j-j7AemqGjOkLk1sXwxjVsT5q8Xvi95fPErS9o6jVe0SvZBOcp_XwyQHcz2H50JT0nX_D4CSgQCWfOFh6OEBKdIdb7yLOgS2EdW3OTPswHGr8hM-_4N0z6Gfu9lZihfMx-bQGtaDgSdKpqCOUFROivY66EkmSo75b8Q_5j9yXNpTVe_76Y7NfyYCXht2q95Wq0-DkyM3eV3q1DItaZlXsplUwaBKz8D_Pigr5LvLRkMX0kGW4_r4dIbMltj0rY5b7JS0qq29pT6Q8HJMNc_X3HWuA9j1fiFS0RdKfCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aa971ff94.mp4?token=k6-powcpr1ao2HvCO6LzKDhlHZCKuWmq4TRNfscxQv_p338j-j7AemqGjOkLk1sXwxjVsT5q8Xvi95fPErS9o6jVe0SvZBOcp_XwyQHcz2H50JT0nX_D4CSgQCWfOFh6OEBKdIdb7yLOgS2EdW3OTPswHGr8hM-_4N0z6Gfu9lZihfMx-bQGtaDgSdKpqCOUFROivY66EkmSo75b8Q_5j9yXNpTVe_76Y7NfyYCXht2q95Wq0-DkyM3eV3q1DItaZlXsplUwaBKz8D_Pigr5LvLRkMX0kGW4_r4dIbMltj0rY5b7JS0qq29pT6Q8HJMNc_X3HWuA9j1fiFS0RdKfCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: نگاه کلیشه‌ای به زن در جامعه خیلی زنان را اذیت میکند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/133015" target="_blank">📅 13:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133014">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
الجزیره: تنگه هرمز اکنون «کارت اصلی درگیری» میان آمریکا و ایران است
🔴
تهران به دنبال افزایش حاکمیت خود بر تنگه بیش از آنچه پیش از جنگ از آن برخوردار بود، است
🔴
آمریکا نیز می‌خواهد اطمینان حاصل کند که هرگونه رقابت با حضور آمریکا در تنگه هرمز، به تهدیدی امنیتی مستقیم علیه ایران تبدیل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/133014" target="_blank">📅 13:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133013">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f442a510.mp4?token=jzXojyv1qsx3EEdqmIxxbvie4Zt9zar4fhKhPmYiCrzgQSZ_rdvakOpsARxf0ND0AMTWSXGiHbPgFUwnNNF0qM1S3JvRPGpNoW6sitw_Ah9_9LHuNIujZAAEKbg5IF6xdghPLakWzNUiyKS3i4HVETX-e4k7hsoCEVHu8-4kUcSQZxn6sVmt54mRGkIy49yKJB3pvL98Mz4N_se3r6ynRIQE2Nbayug_frPqwhhQlUnmcLFkN6-ENDhOfScBpBzy9pxUPK_tp_9E-9bubZzXuQB_MMAIyup48d8wObm24BDv6phYMYq1yxeB06R8eDuwm7LHlVV2ZNqV0qX_aI6TcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f442a510.mp4?token=jzXojyv1qsx3EEdqmIxxbvie4Zt9zar4fhKhPmYiCrzgQSZ_rdvakOpsARxf0ND0AMTWSXGiHbPgFUwnNNF0qM1S3JvRPGpNoW6sitw_Ah9_9LHuNIujZAAEKbg5IF6xdghPLakWzNUiyKS3i4HVETX-e4k7hsoCEVHu8-4kUcSQZxn6sVmt54mRGkIy49yKJB3pvL98Mz4N_se3r6ynRIQE2Nbayug_frPqwhhQlUnmcLFkN6-ENDhOfScBpBzy9pxUPK_tp_9E-9bubZzXuQB_MMAIyup48d8wObm24BDv6phYMYq1yxeB06R8eDuwm7LHlVV2ZNqV0qX_aI6TcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پالایشگاه نفت مسکو تو روسیه از صبحِ تو آتیش می‌سوزه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/133013" target="_blank">📅 13:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133011">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpO25LrVN-H4BXZ0-C_ja9-w6-u9nFyCOsiiK6KtDhbVoxeaXz55ojrwxuNG0OjTODl2_aB1B2onFQAE4X8oqW4hdsqZKcHi53G3SEh2_rGZusj9XyLtB8tiGNtXoJmH5kGy4QHIZKGGN8GycpQH7eUC5JeF1oyZvgoMP-5KA8h4IOmSZB5tilPj24NGpgx7KdM8ZaGaiYqR_a2t08Pv_v02lwyxyZuMHf_10H6sp8By-kkD2d4omkv5cPKZ5Lyvc9_iYvdaBpwwNqKDH_igSDH0LRZS309UUTwIcGUiskxqaffcXq2TAA0oPdOUdC_yghhIO_FrJsIwBmprfK2L9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae26a6683.mp4?token=EthmZS1zOIMh6ldbgTcClf0NGMRcjJhQ0NsvrwfwUkYwpEnCHKhmFW0Lw3Tktb_PXsbQSect2YvCuwG5npjzHYDs8VrhxHmk2FCkpD_fqOmQSjFvHdk0Mohx6_cyAfaDuAQ8NJeqn16U0FcB34XJO9Qe8hcqb0dv_qNQWyp0xMZw-9bCWBIWm7lhzkzrzUMXiE177id5JLZDOasUM6bv-XyaSC8AjOoJH61EKkX-v801zRfZSalAcFxsBbvSw4h17H5kfzSap80kz0TEK8YEhArtC3DNjhhh4a2iSAG22FqPrHhYQwLUtQMPs2TWTMVjzNFTW-drd9iwotYv85OAwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae26a6683.mp4?token=EthmZS1zOIMh6ldbgTcClf0NGMRcjJhQ0NsvrwfwUkYwpEnCHKhmFW0Lw3Tktb_PXsbQSect2YvCuwG5npjzHYDs8VrhxHmk2FCkpD_fqOmQSjFvHdk0Mohx6_cyAfaDuAQ8NJeqn16U0FcB34XJO9Qe8hcqb0dv_qNQWyp0xMZw-9bCWBIWm7lhzkzrzUMXiE177id5JLZDOasUM6bv-XyaSC8AjOoJH61EKkX-v801zRfZSalAcFxsBbvSw4h17H5kfzSap80kz0TEK8YEhArtC3DNjhhh4a2iSAG22FqPrHhYQwLUtQMPs2TWTMVjzNFTW-drd9iwotYv85OAwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب عده‌ای داشتن شعار علیه قالیباف میدادن که مهدی رسولی مداح خیلی سوسکی این شعارها رو تبدیل کرد به حیدر حیدر
🔴
الانم تندروها دارن بهش حمله میکنن و میگن خایمال
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133011" target="_blank">📅 13:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133010">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46be7e5d32.mp4?token=hJHLEFMmxQhKK42mQdBfuX-Jt_YqIYNqY2vqy2xHL2LqdJ9LXHs3EKbMDanSsXoI545QKe_vs3gspyJ0CIoplBY93t6U3UN4K6E6j0mNYqhFsCo95VTK-OtNR6OkCcR9sEFj34WPiGBluXW4b8OqPkxIFtIcCiTZ5WjnlLF06JZtk2xwgMujUVgTFBQh2cd5pEOhv5BJGErqSq8muGstIgzLvopNH6OKggJzA1-Ym3UXQ_wVC_FWw-8tPDS6vN6lUxfsuVfnZ0dTCqITmpfT6wkg7rDKDGilZwv1XDLVvlCB_nRFNUTocoqSpN9_x0oANFZjHwbFuDJ6xRoZVr9Vk72Rdx22ywdkQHtI1lc9E5OFArvi38XXDBqP1Gpj2EezvRrf_wGupvCZ40CCKo_Uz-ZnP4TFIY3dvdIOtiV_0Tr8DC8GL_O5VxPSzIOoLY-E83v9qIgXX9deZ2VRMVVvyeFuWg7O7do-WYxaSTGdc_9pO1HFFqXY4EgnEXtnlq6wmuxvgoYC4bDa4v7Iwx5jYttDPO5y8tM60TaYkRBKk5obMcLwf1w-B9mLwgNHYdDhrdzkNu0-9ZbVEEvdFeJ95IZu9zaG_gNuwym7kFCFHmyBGXUiUJlUp32wYyJC6Kj-1kzLijUl1Cwx5hKx-tAPhiGNuXDXp1yB6_YJAXi6bco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46be7e5d32.mp4?token=hJHLEFMmxQhKK42mQdBfuX-Jt_YqIYNqY2vqy2xHL2LqdJ9LXHs3EKbMDanSsXoI545QKe_vs3gspyJ0CIoplBY93t6U3UN4K6E6j0mNYqhFsCo95VTK-OtNR6OkCcR9sEFj34WPiGBluXW4b8OqPkxIFtIcCiTZ5WjnlLF06JZtk2xwgMujUVgTFBQh2cd5pEOhv5BJGErqSq8muGstIgzLvopNH6OKggJzA1-Ym3UXQ_wVC_FWw-8tPDS6vN6lUxfsuVfnZ0dTCqITmpfT6wkg7rDKDGilZwv1XDLVvlCB_nRFNUTocoqSpN9_x0oANFZjHwbFuDJ6xRoZVr9Vk72Rdx22ywdkQHtI1lc9E5OFArvi38XXDBqP1Gpj2EezvRrf_wGupvCZ40CCKo_Uz-ZnP4TFIY3dvdIOtiV_0Tr8DC8GL_O5VxPSzIOoLY-E83v9qIgXX9deZ2VRMVVvyeFuWg7O7do-WYxaSTGdc_9pO1HFFqXY4EgnEXtnlq6wmuxvgoYC4bDa4v7Iwx5jYttDPO5y8tM60TaYkRBKk5obMcLwf1w-B9mLwgNHYdDhrdzkNu0-9ZbVEEvdFeJ95IZu9zaG_gNuwym7kFCFHmyBGXUiUJlUp32wYyJC6Kj-1kzLijUl1Cwx5hKx-tAPhiGNuXDXp1yB6_YJAXi6bco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندین تُن از کمک‌های بشردوستانه ایران به زلزله زدگان ونزوئلا اهدا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133010" target="_blank">📅 13:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133009">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19f47e808.mp4?token=EVuSf3j9KyEYSW5EBHTKuyL5hmRMRlysPf1i43KldOZg5_MghW6fRBuDpuuSz3tyX5xwjVz3Iw6TlaUoovsoatkxwUtk2S4dYcmnh2W8zvDwTPD6jE2HsyPydnt6nFKN72ixie7MKmd-JyaDh_alrLicJfQV5r_GIULyWdDbfRFYXGroBWNd-NdtJRDuuPYMspU0Dh97qCv271lR-WW1EaO4oQSjxJE_ckJvVlbrJgwAxMsvk8zlksbTRfIBVsAnFUzu8IoY4RpCLkkpxn1cGANahkvWHSx5Mbzf3NyJ8IGCyp6eRpnvq3-Dyy5erZsS1UIcC4P4hW_65KlYwO-fVVg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19f47e808.mp4?token=EVuSf3j9KyEYSW5EBHTKuyL5hmRMRlysPf1i43KldOZg5_MghW6fRBuDpuuSz3tyX5xwjVz3Iw6TlaUoovsoatkxwUtk2S4dYcmnh2W8zvDwTPD6jE2HsyPydnt6nFKN72ixie7MKmd-JyaDh_alrLicJfQV5r_GIULyWdDbfRFYXGroBWNd-NdtJRDuuPYMspU0Dh97qCv271lR-WW1EaO4oQSjxJE_ckJvVlbrJgwAxMsvk8zlksbTRfIBVsAnFUzu8IoY4RpCLkkpxn1cGANahkvWHSx5Mbzf3NyJ8IGCyp6eRpnvq3-Dyy5erZsS1UIcC4P4hW_65KlYwO-fVVg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زرشناس کارشناس مسائل سیاسی در صدا سیما: آنقدر تنگه هرمز را باز و بسته کردیم که اثرگذاری آن سست شد
🔴
باید مواضع اقتصادی منطقه را بزنیم؛ یکی زدند ۵ تا باید جواب دهیم تا بازدارنده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/133009" target="_blank">📅 13:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133008">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فووووری/نخستین تصویر از فرد تیرانداز
◀️
مشاهده عکس بدون سانسور</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/133008" target="_blank">📅 12:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133007">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
جوزف عون، رئیس‌جمهوری لبنان و ژنرال رودولف هیکل، فرمانده ارتش، آمادگی‌ برای استقرار نیرو در مناطق جنوبی را بررسی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/133007" target="_blank">📅 12:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133006">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: تشدید تنش‌ها بین واشنگتن و تهران ممکن است به عرضه مازاد مورد انتظار در بازار نفت در سال ۲۰۲۷ آسیب برساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133006" target="_blank">📅 12:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133005">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پاکستان: حملات تروریستی از افغانستان سازماندهی می‌شود
🔴
نخست‌وزیر پاکستان مدعی شد حملات اخیر در بلوچستان و خیبرپختونخوا از خاک افغانستان هدایت می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133005" target="_blank">📅 12:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133003">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پاکستان: حملات تروریستی از افغانستان سازماندهی می‌شود
🔴
نخست‌وزیر پاکستان مدعی شد حملات اخیر در بلوچستان و خیبرپختونخوا از خاک افغانستان هدایت می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133003" target="_blank">📅 12:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133002">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_adI2mKgxsLbX9aKlGouHSVlHsTELADBgI6yYCAOKjQw8O6QLs7V8cuPyBcVbvcxJbJRtHoweR_DoGv2pSHy-EC8yXfGn5BO7zIVIUrgYufFsgIo9Rh-Q3l5aWyZ5u_s4qtMdgdkjEW1eY01hLFoJjIGyX7AsWaQvOSUUfS52krdFb9UpKJbMr-TekRKgvuj6rBpoS2AB2q7LeJ1HBnOOnVIc92uv-MbrU48Z4yiR8scnGl8UbudSrWUu8L_gbhkHFYTDNh3S1vaDWVmQTsb7ziPw1tw2kCSpj1drM_o1yu92e4Ep1wbkZKweUJxPPV50XX1Q0URanSHxn-NY6G5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت عضو تیم مذاکره‌کننده: تفاهم خوب بود و شیوه اجرای آن هم تا الان خوب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/133002" target="_blank">📅 12:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133001">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQAdBiJPHfoWU-DR-d9RANRoCKd4hf2mGMs-01iZExwSXtSM4_Luq-DelmrbDSycw9RNGW4yh7uJCnV16TbHHNtR3xUtao9v4Gv_En78R7I4CCYjuZcYHWo9X_gYMHSyzx_ezchXWGN26MnfuEwfdMPZaQenFhPGT4qscTDOX3EbHN4Vd6jDCKhtuV6e2n7CQe1ZfefQ5WAiE-7TfFcpYZ6PapWsKjsVEoDErrFyr-4wf3SmvMZ23aJxxW2yIlg7UmcqQEWdIBQTeIoYi0kOND17FZq1YupD7HvWncDKU3893rkmFzrCGaNH6FRbdCF2ZV_AovvvB03U3I9qcNtOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش ۴ درصدی قیمت نفت پس کاهش تنش‌ها در خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133001" target="_blank">📅 12:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133000">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سیتی ژورنال: وزارت خارجه آمریکا جلوی دیدار مقام ارشد تیم زهران ممدانی با سفیر ایران در سازمان ملل را گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/133000" target="_blank">📅 12:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132999">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/177af0ba50.mp4?token=Mun65Who-8Or9XCggGJCp0vm_XfFDLv9Lbfeqt_jA-G79qn97nRU1A3_Xo_MkINKOv_yJ7OlyCx2D1cYQAGmy0-Cda-yGyhfJ85rllwDMvUtYGu5tpGPt975U0wz9A5RkI-EOTZFDMsv17LQ4mFNJT377US9wBSc5QslE3Q0_lh_E_jdrDzk3mXQQhfbJoyM58SWTFAAIYPBgLryyXHj3sRyaRqIVswXf-zGv95-TL_EfFTtBNYl-hx4hdvGkPsh-f_3zHxNJye-lzdtv-V1yUd0dOdm-oIPlKXMUod-UIZRMgMX-WEHm3PmN78iKRocxF4ER_u5VUkYAQdsBij2Jybpt4v-X1PmbwkmUpNpJzQCPWwbin5t9pCTzycnBl7oAdElwwODURxwFv_hgda6kr0oVlj3PRa6KvCn_YNNtpJl-bC-K241hq5FwSgjk1ucGwqIbz-wgpgFVjwCHmK6PMIxx3CpGBy17WJz-ZjPC8PUCSQTo2jrew2P7E3TIoBz14ekoiTUwVnpNIh8dF5Cv1t4VbgAwVl9waFfkZcjHz0V-GXaPNj9et2iT1a9SIjcaFLcFJ5dWoZrypMHAXwDic8Z7myS0cIqreCHlA3RVP1-Y8W1cuEboLWakSGb2L1e3t9f7heuBWmTD_n9WXHoVy3rpSkej_IB-u0akb3CKPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/177af0ba50.mp4?token=Mun65Who-8Or9XCggGJCp0vm_XfFDLv9Lbfeqt_jA-G79qn97nRU1A3_Xo_MkINKOv_yJ7OlyCx2D1cYQAGmy0-Cda-yGyhfJ85rllwDMvUtYGu5tpGPt975U0wz9A5RkI-EOTZFDMsv17LQ4mFNJT377US9wBSc5QslE3Q0_lh_E_jdrDzk3mXQQhfbJoyM58SWTFAAIYPBgLryyXHj3sRyaRqIVswXf-zGv95-TL_EfFTtBNYl-hx4hdvGkPsh-f_3zHxNJye-lzdtv-V1yUd0dOdm-oIPlKXMUod-UIZRMgMX-WEHm3PmN78iKRocxF4ER_u5VUkYAQdsBij2Jybpt4v-X1PmbwkmUpNpJzQCPWwbin5t9pCTzycnBl7oAdElwwODURxwFv_hgda6kr0oVlj3PRa6KvCn_YNNtpJl-bC-K241hq5FwSgjk1ucGwqIbz-wgpgFVjwCHmK6PMIxx3CpGBy17WJz-ZjPC8PUCSQTo2jrew2P7E3TIoBz14ekoiTUwVnpNIh8dF5Cv1t4VbgAwVl9waFfkZcjHz0V-GXaPNj9et2iT1a9SIjcaFLcFJ5dWoZrypMHAXwDic8Z7myS0cIqreCHlA3RVP1-Y8W1cuEboLWakSGb2L1e3t9f7heuBWmTD_n9WXHoVy3rpSkej_IB-u0akb3CKPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی:
قالیباف شاشیدم وسط اتحادی که درست کردی
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/132999" target="_blank">📅 12:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132998">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پرواز‌های فرودگاه مشهد از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/132998" target="_blank">📅 12:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132997">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPU0zKS1znyzE1FznM5JQVj4-YQJ2lmpLEEjILiLCIe1hsqoNrxI1f6sWrseQoywAvYLMhTF3cUYaf8wroCjhXdRAvhkQH3QeLIYtuGo9O-2JQKs5uKHVLOGW8-4FR1vFxyz8eIoH3lKFkIr5OYINZKOJu22pIkJfz7WcVOsi5Vq7For0srx7C0QcUh_DIK8XysjY1CBVcYsIY-z8GYPzfb8je_e6DvjpJXtRZLLyafZIwRACsmT4L8YQDlMv1YTctbRZ_ImowUO0NMIP7Dh3giIZ4E2ndN3b-3AtW5KRTH_c-dOSKc6BqwxBwPvkdGHRTIANR-IGhiBGaqfyrg_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیرنویس شبکه خبر : آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/132997" target="_blank">📅 12:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132996">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
شرکت آسلسان قراردادی به ارزش ۱.۴۷ میلیارد یورو با شرکت SSB ترکیه برای تولید انبوه سامانه‌های پدافند هوایی امضا کرد
🔴
این قرارداد تحت برنامه گنبد فولادی، طرح چندلایه پدافند هوایی/موشکی ترکیه  قرار می‌گیرد که اردوغان اخیراً با ۲۴ میلیارد دلار بودجه اضافی از آن حمایت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/132996" target="_blank">📅 12:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132995">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b00498f39.mp4?token=SCgn0wvimO9hQuXyR3oHEBQCBuoEk5ICA6_VsEbW3-8qsWEiMjP_IyFwybMud8xljhpRL56lc7Zp3a0-qNILVhRvhlpVKJvl3NpvVVU_XswKG5QaqfWYB3OAgck9HMR_K0_nZuL-3I-rXaT8nZFbgbiwaqYjlN2W-6O84nxjSVmbWk-N08_1gKjSDZXsR7pH4dleefXLxzKzwdzri_RlPJqSfL1TFlPurFNgbHeoxdXQhPa5x6UyktST160czzH9riRZyIGwJJIbwaL_chyrdPMQgfjU1huIrJcQkmAz29xhTTuUKxn6OucqHawc3UbZf9i6g4bKlNB8VA61JNkE9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b00498f39.mp4?token=SCgn0wvimO9hQuXyR3oHEBQCBuoEk5ICA6_VsEbW3-8qsWEiMjP_IyFwybMud8xljhpRL56lc7Zp3a0-qNILVhRvhlpVKJvl3NpvVVU_XswKG5QaqfWYB3OAgck9HMR_K0_nZuL-3I-rXaT8nZFbgbiwaqYjlN2W-6O84nxjSVmbWk-N08_1gKjSDZXsR7pH4dleefXLxzKzwdzri_RlPJqSfL1TFlPurFNgbHeoxdXQhPa5x6UyktST160czzH9riRZyIGwJJIbwaL_chyrdPMQgfjU1huIrJcQkmAz29xhTTuUKxn6OucqHawc3UbZf9i6g4bKlNB8VA61JNkE9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقاد نماینده مردم تهران از تعطیلی دنباله‌دار مجلس: قانون‌گذاری تعطیل است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/132995" target="_blank">📅 11:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132994">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: انتظار می‌رود تقاضای جهانی نفت در سال ۲۰۲۶ حدود یک میلیون بشکه در روز کاهش یابد.
🔴
عرضه جهانی نفت در سال ۲۰۲۶، ۳.۷ میلیون بشکه در روز کاهش خواهد یافت.
🔴
عرضه نفت در ماه ژوئن ۴.۱ میلیون بشکه افزایش یافت اما همچنان پایین‌تر از سطح قبل از جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/132994" target="_blank">📅 11:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132993">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
آمریکا اعلام کرد همچنان به تفاهم‌نامه با ایران متعهد است و به دنبال مسیر دیپلماتیک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/132993" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132992">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترکیه اس-۴۰۰های روسیه را به کشورهای خلیج فارس فروخت
🔴
یک روزنامه نزدیک به دولت ترکیه گزارش داده که آنکارا سامانه‌های پدافند هوایی اس-۴۰۰ خریداری‌شده از روسیه را به یکی از کشورهای حاشیه خلیج فارس واگذار کرده تا راه را برای دریافت جنگنده‌های اف-۳۵ از آمریکا هموار کند.
🔴
عبدالقادر سلوی، نویسنده روزنامه حریت ترکیه، افزود که امارات متحده عربی و قطر از جمله گزینه‌های مطرح به‌عنوان خریدار این سامانه‌ها هستند، اما تأکید کرد که باید منتظر اعلام رسمی ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/132992" target="_blank">📅 11:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132991">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
شرکت بین‌المللی انرژی: پیش‌بینی می‌شود در سال 2026 عرضه جهانی نفت با کمبود 860 هزار بشکه در روز مواجه شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/132991" target="_blank">📅 11:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132990">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
عضو هیئت‌مدیره تعاونی صیادان گفت: در جریان حملات روز‌های ۱۷ و ۱۸ تیرماه به نوار ساحلی استان هرمزگان و در پی اصابت دو پرتابه ارتش آمریکا به اسکله صیادی پنج‌پله بندرعباس، دست‌کم ۳۰ فروند قایق صیادی به‌طور کامل از بین رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/132990" target="_blank">📅 11:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132989">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
بیت‌کوین ، بزرگ‌ترین رمزارز جهان ۳.۵ درصد در روز جمعه رشد کرد و به نزدیک ۶۴۰۰۰ دلار رسید و ۴.۲ درصد طی یک هفته رشد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/132989" target="_blank">📅 11:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132988">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996091c351.mp4?token=J1zftGxeJqpr_9OUmwY0jpp2OrcyrmA05pprJ1zu5T-xZxSmWpo3OXCusdUpSOhCgIMA-6W3DvaD0a2XSMYYyQ6kbGOmRhYuf4fZRfR211_39WbgStnsGyLQeMmAkFguI0TtNB_oZqUM_FdZImAoGJi2j1kn9IQjVwOwMU9hJK2L4BHJFR9JLAPF4lJdA2fNgmajkI-JjRMOxaXo_-5WbE6HPq2SYgWs74AO6yXSOXaB0M3vbNXeIDURF0KRmt-ssLetobwZtYhmdJInjNZyUIIQupTeGqWIKFZr2z_CbSfpCI6D2h_QAXAoj3KqinCXe1x3BphlnnJUshNCWRItEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996091c351.mp4?token=J1zftGxeJqpr_9OUmwY0jpp2OrcyrmA05pprJ1zu5T-xZxSmWpo3OXCusdUpSOhCgIMA-6W3DvaD0a2XSMYYyQ6kbGOmRhYuf4fZRfR211_39WbgStnsGyLQeMmAkFguI0TtNB_oZqUM_FdZImAoGJi2j1kn9IQjVwOwMU9hJK2L4BHJFR9JLAPF4lJdA2fNgmajkI-JjRMOxaXo_-5WbE6HPq2SYgWs74AO6yXSOXaB0M3vbNXeIDURF0KRmt-ssLetobwZtYhmdJInjNZyUIIQupTeGqWIKFZr2z_CbSfpCI6D2h_QAXAoj3KqinCXe1x3BphlnnJUshNCWRItEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتیش سوزی سنگین تو منطقه آلمریا، اسپانیا
🔴
دست‌کم ۱۱ نفر بخاطر آتیش‌سوزی‌ جون خودشون رو از دست دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/132988" target="_blank">📅 11:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132987">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کره شمالی از تقویت کمی و کیفی توان هسته‌ای خود خبر داد
🔴
رسانه دولتی کره شمالی اعلام کرد این کشور در نشست کمیسیون مرکزی نظامی به ریاست «کیم جونگ اون» تصمیم به تقویت کمی و کیفی نیروهای هسته‌ای خود گرفته است.
🔴
بر اساس این گزارش، پیونگ‌یانگ در نظر دارد زیرساخت‌های فنی سامانه‌های رزمی را ارتقا دهد، پایگاه‌های نظامی را نوسازی کند و فرآیندهای تولید نظامی را استانداردسازی کند.
🔴
کیم جونگ اون نیز بر افزایش توان واقعی رزمی ارتش خلق کره و تسریع «انقلاب در آموزش نظامی» تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/132987" target="_blank">📅 11:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132986">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsOkZbjjOMuZ14Uo43lQdllN88GHdti0JnicuxiY2A76axpH0KkDNBV1KTA9zzSjaNB6Jtqc224hWUNxWG0bK8Il0XJTFd6AQA2Xnumr8Ow0AA_brdGRaX2-13jSUe5oBfQb7R4m4XlF4UVIAUCegGhcIT7-FqL7r8XdjvM7U1ZNhkAS865eyA_6KjbvwYl3T2ZesDAfiB-ZokvjC7VxMnelFeU-otU6-Pb5cEMMk-CmOEr00CfVTiyR0EiU5ajtjWpkZpmUM5ljPgzhGUDdRrwYj5JjkU1_CTLY4qyPemdTxBx0dN_jsIyB6c1U8_fmmqSitXv6wb4X0Acp02Dkgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مردم ایران نسبت به همسایگان چقدر بنزین مصرف می‌کنند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/132986" target="_blank">📅 10:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132985">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ارتش اسرائیل: ما به عملیات خود برای از بین بردن هرگونه تهدید ادامه خواهیم داد و اجازه نخواهیم داد حزب الله به ما آسیبی برساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/132985" target="_blank">📅 10:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132984">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / فاکس نیوز: یک مقام آمریکایی به من گفت مذاکرات با ایران در هفته پیش رو ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/132984" target="_blank">📅 10:39 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
