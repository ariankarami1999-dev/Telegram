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
<img src="https://cdn4.telesco.pe/file/PkmP68KdnmaAU9ui13KRvbPDQoDFM0aD0XtqFXj3i64roOfD25hlbu1CcZGSqU8Mixrq2L9cdPYZvZjT4YqA0zLsUEXsvAVBt1rt4XRaoCGew3nrrbhoo_1NsznAUxFQ7DC8sbZ1JzNErlDIucui04Z_pOtDeOfCXfKW1ebt2_pDa9F8G6fWS_VHkiMQ00p2sh3TugDg5wbXmKUuSbnpHUfcSz_osA_kjWf6uofe0bvkfdlPqmGmncUAYCi1HiiJZZiENJUiWrC3WLXJ4d9NzL3pHxRXvL3-K_qwSrqt0U4QC7qoZrwR4ZZaifhJJL_D8COgNy5C_hzPkQBtDniBaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 02:35:17</div>
<hr>

<div class="tg-post" id="msg-121911">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meRttmvweNsqGrZh9Dl8qYiZLlqGDQkJBYPFB96WyguMvJ-n_clbmdLALmfldrgOvfvi-kuzdjR5zlH5mUmF36qmc9cOJDpEU2aWFT2E5QWx8MmlOKQWlyI8uZ2-pBKgmsEn6DHTu8R1j7wjMmc0gGsyqt36I2HIoVuV3OwzisODbfK0olm1xAsz-_K07kaRLsmwhq_sZtOyPYTbJ6koRJqfU6T0YvtwIv2IW1rAS6C7Kn8nNquv51Yq6OUhxq_1Uh9I0mukCayVMXaV0Z9if1_iyN2oileQH31jsdri4RqCSuXm-1njp7AyAexIJ96OwQdgc_uUiVDRxAnqZrHDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به ساختمانی در صور در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/alonews/121911" target="_blank">📅 01:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121910">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
عراقچی هم اکنون:
زیاده‌خواهی آمریکا مانع اصلی در روند گفتگوها است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/alonews/121910" target="_blank">📅 01:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121909">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5302f20640.mp4?token=qcp9gFDhj0qtYWyN05ul19LzZ0Ijeg7HvxHxmwtWe_dGLKv46yIKEo6wN_q0WaRhpg65-RzejhDij_H1VsN2Y7-y22lVrXxunBdKJOJSkUd54oxBbBg7MQXt66SdBD9E5_E9aIADA9aDsvgR0UJvUZn-48VSlgHa6sop3amXFlRrdsVgdOWJm4-GZWH6amzjnqRmsyO6M9D5w8cQVn-r-QYPIhornGYPr9-5VfPKfGAsMMXccWSUP4bEmTlG7b1rp8MJY_u7XIlHd08rRxYLf9A_d6QrBT3D5UAv1Jk98GKUGw14zsHJDlg4QLiYTM28Lc0Y9LrqZGU-9JnXv4j-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5302f20640.mp4?token=qcp9gFDhj0qtYWyN05ul19LzZ0Ijeg7HvxHxmwtWe_dGLKv46yIKEo6wN_q0WaRhpg65-RzejhDij_H1VsN2Y7-y22lVrXxunBdKJOJSkUd54oxBbBg7MQXt66SdBD9E5_E9aIADA9aDsvgR0UJvUZn-48VSlgHa6sop3amXFlRrdsVgdOWJm4-GZWH6amzjnqRmsyO6M9D5w8cQVn-r-QYPIhornGYPr9-5VfPKfGAsMMXccWSUP4bEmTlG7b1rp8MJY_u7XIlHd08rRxYLf9A_d6QrBT3D5UAv1Jk98GKUGw14zsHJDlg4QLiYTM28Lc0Y9LrqZGU-9JnXv4j-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به سمت کاخ سفید رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/121909" target="_blank">📅 01:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121908">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgRgN_Facv400vjkapgWmDj52Tb3wzECcTwf2qK8XCjl7wMJudyz9C4YmVR-KUyO2SkuUz-gpZ2z41dCy9ePvKfTwoLeS_xsqx0Yy36cDNS9Qutn3-kj-NufCFZ3ZCq-Vdh85-DSEdV5zqeXxe6euMDwr-LZJliorrWaqZnXoLI0Y9TPRbf9iRG6TzusFUMzuij-vL183bEf-Nfdxx0hQNdHzZhEIFqua5wwlWs9VW-wOAyP6Tou2iBMViX7GnD4Yhf8o1cKUKpTsha5SFriNkURjk17y6HFrS_oZXrnIZBeRhAvuReUU0oO2I64PfrLHph0uXVZX_w8kuUdxhYMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فضای هوایی غرب ایران طبق یک NOTAM جدید تا صبح روز دوشنبه بسته شده است، به‌جز پروازهای روزانه (در ساعات روشنایی روز).
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121908" target="_blank">📅 01:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121907">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دقایقی پیش بازار بورس آمریکا برای حدود ۹۰ ساعت آینده بسته شد.
اگر قرار است ترامپ فرمانی صادر کند امشب یا فرداشب صادر میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/121907" target="_blank">📅 01:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121906">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
منبعی عالی‌رتبه به العربیه: فضای مذاکرات مثبت است، اما تاکنون به توافق نهایی نرسیده‌اند.
🔴
«پیش‌نویس توافق آماده است که نیاز به موافقت تهران و واشنگتن دارد.»
🔴
«تهران خواستار تضمین‌های روشن در مورد آزادی دارایی‌های مسدودشده و تحریم‌های نفتی است.»
🔴
کار برای کاهش فاصله بین خواسته‌های مشروع ما و خواسته‌های واشنگتن در جریان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121906" target="_blank">📅 00:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121905">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76666c05ca.mp4?token=eux0agEN-JUwOQE9W4FAn8wQK2Z8YnMorAe3yEOX9MYSzCw_IRrlekAPUOsfmaqfvPQlWv75qxiNJCuzDrOSZedhN7FPtJUd-o1e8nVLfhOO8BD8_A026zsq_8YMCEKUvhhfirT1HInix1yuBpJ6T8UUO_T1RHvXVl8eZ77aHhxGGrf3pIPHAQ7fXCKYmHVvmmIlvPnqnfn_yyPJY7aXpd7HYd-uogEwKCaILPfYnIJvRaJBESs1w-qpn53t-cGV241H4Pkm2QMTsW9bUQcVUNnxSVoTUMDSnKZfgH_4b9wH-Zt_uZFOctLZmOEXuB5SyIuq7Rq_FxUyxLdyRSuaFojlhy3NfLM7v2tzk3-Vun6rSR_NsGtIgifTIIFtNERCBGtcx6XFMRoTWAD1a2M9gcBDBrgFG0VD8kYL_YhQ3UkCISgNAMpTsRdwGoM7hX8kAWn8rA4u_8kYlGL3lnXpRiILKbMr6nMIwdmFMNCaznTSvhOCmxur8Q6qCZ-85qXYs6kt1wAe1Vfl3xT6sSK93ZvMsFRegA3nMVWRgBwth4TDVV6jTLt7AUliWioJ-Uq_V1KyHb3t3eH8l-HNj9-V12zNIuyf1XUcU5fY18EwjkeJ9D0YAbYLnf2tyALlwsMJwdVxH7wQSut7ZbTylEX6NfJ5dHhESq4n4ndtzB1Ryhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76666c05ca.mp4?token=eux0agEN-JUwOQE9W4FAn8wQK2Z8YnMorAe3yEOX9MYSzCw_IRrlekAPUOsfmaqfvPQlWv75qxiNJCuzDrOSZedhN7FPtJUd-o1e8nVLfhOO8BD8_A026zsq_8YMCEKUvhhfirT1HInix1yuBpJ6T8UUO_T1RHvXVl8eZ77aHhxGGrf3pIPHAQ7fXCKYmHVvmmIlvPnqnfn_yyPJY7aXpd7HYd-uogEwKCaILPfYnIJvRaJBESs1w-qpn53t-cGV241H4Pkm2QMTsW9bUQcVUNnxSVoTUMDSnKZfgH_4b9wH-Zt_uZFOctLZmOEXuB5SyIuq7Rq_FxUyxLdyRSuaFojlhy3NfLM7v2tzk3-Vun6rSR_NsGtIgifTIIFtNERCBGtcx6XFMRoTWAD1a2M9gcBDBrgFG0VD8kYL_YhQ3UkCISgNAMpTsRdwGoM7hX8kAWn8rA4u_8kYlGL3lnXpRiILKbMr6nMIwdmFMNCaznTSvhOCmxur8Q6qCZ-85qXYs6kt1wAe1Vfl3xT6sSK93ZvMsFRegA3nMVWRgBwth4TDVV6jTLt7AUliWioJ-Uq_V1KyHb3t3eH8l-HNj9-V12zNIuyf1XUcU5fY18EwjkeJ9D0YAbYLnf2tyALlwsMJwdVxH7wQSut7ZbTylEX6NfJ5dHhESq4n4ndtzB1Ryhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کسشرهای ترامپ تموم؛ آخرش هم یه رقص معروفشو زد قمار باز
‎
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121905" target="_blank">📅 00:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121904">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: «مسئله‌ی ایران خیلی زود تمام می‌شود و همه‌چیز به‌‌ سرعت به حالت عادی بازمی‌گردد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121904" target="_blank">📅 00:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121903">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
یک مقام ایرانی به المانیتور گفت که «برخی ایده‌ها و متون جدید بین دو طرف مبادله شده است.»
🔴
این مقام افزود: «این فقط می‌تواند مبنایی برای گفتگو بین ایران و ایالات متحده باشد. به معنای توافقی نیست که بتوان آن را اعلام کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121903" target="_blank">📅 00:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121902">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / اکسیوس: ترامپ امروز با افسران ارشد جلسه داشت به شدت درحال بررسی بازگشت به جنگه!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121902" target="_blank">📅 00:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121901">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
اکسیوس:برخی منابع نزدیک به مذاکرات همچنان بر این باورند که طی ۲۴ ساعت آینده فرصتی برای نوعی پیشرفت وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121901" target="_blank">📅 00:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121900">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / اکسیوس: ترامپ امروز با افسران ارشد جلسه داشت به شدت درحال بررسی بازگشت به جنگه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121900" target="_blank">📅 00:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121899">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0a0b67a23.mp4?token=FV1XvE-7Z_1QVm4LUVYhTqgnSVYp-WsSdbC34CctaXurpf6XWctecAjQ6j6MC2FdS6AicULnzc0EwLgPX2iD4yhF0NlA0fCqCCEJ0tsRzcAtcaDr2EE-G_6eGLFGVg1qw6wPzA-G4BHeqeDu9wPF0XvUlcDHYL-i-93w4NabW0UiPZ12xov9yU_gBJRUfKCa694h8rU9RxeuWFzqeSAbmvr2pUSr9iiJMegs3KLjtaSqFgsciT7OLvEInVnz1wTK3Cuwo4wZdZB4eyNPRabY8qxEYsGnHnr8FxNBmiFTR3rOC0X0WsySA99mW4Cr1KEgNNfGg_zjYbX5ILLyD8ijtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0a0b67a23.mp4?token=FV1XvE-7Z_1QVm4LUVYhTqgnSVYp-WsSdbC34CctaXurpf6XWctecAjQ6j6MC2FdS6AicULnzc0EwLgPX2iD4yhF0NlA0fCqCCEJ0tsRzcAtcaDr2EE-G_6eGLFGVg1qw6wPzA-G4BHeqeDu9wPF0XvUlcDHYL-i-93w4NabW0UiPZ12xov9yU_gBJRUfKCa694h8rU9RxeuWFzqeSAbmvr2pUSr9iiJMegs3KLjtaSqFgsciT7OLvEInVnz1wTK3Cuwo4wZdZB4eyNPRabY8qxEYsGnHnr8FxNBmiFTR3rOC0X0WsySA99mW4Cr1KEgNNfGg_zjYbX5ILLyD8ijtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما جلوی ایران رو گرفتیم اونها هرگز نباید سلاح هسته ای داشته باشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121899" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121898">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11fa26796b.mp4?token=Rfn3eRu39faRB2Xb8XAPOZpMDXLCDZMaXfRlA1ghnSTmTaEft-pv82OkeV0tCRKu4o-Xe6fe0iC7Wya5JgMORaKlMIFrpr4bVu7x6KX_dOHRz6e7td84VOSQIZvtqHNlWW-YfIYq01ca7symNrDJWHlTcAmT2F99SZyI75OlO0POJwU-y03U58dmbG0U_mkSvxYomNkM8I9HEFZDf2WkJKSHf-RMl5FA968N6lGxhdeTffllgW6Ey9UlN9viRYYqMNEUgWPuainOyyylP6JuDWpeNqFPXoia5Yv9OqRCKbe1octPANKKZoPFW7L5rPkAsFjl7_UInXGNFb91do3gtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11fa26796b.mp4?token=Rfn3eRu39faRB2Xb8XAPOZpMDXLCDZMaXfRlA1ghnSTmTaEft-pv82OkeV0tCRKu4o-Xe6fe0iC7Wya5JgMORaKlMIFrpr4bVu7x6KX_dOHRz6e7td84VOSQIZvtqHNlWW-YfIYq01ca7symNrDJWHlTcAmT2F99SZyI75OlO0POJwU-y03U58dmbG0U_mkSvxYomNkM8I9HEFZDf2WkJKSHf-RMl5FA968N6lGxhdeTffllgW6Ey9UlN9viRYYqMNEUgWPuainOyyylP6JuDWpeNqFPXoia5Yv9OqRCKbe1octPANKKZoPFW7L5rPkAsFjl7_UInXGNFb91do3gtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ می‌گوید این محاسبه را درست انجام داده است:(203 × 9 ÷ 2 + 1324 − 1292) × 19
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121898" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121897">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af1fc50695.mp4?token=PEETLUd8xUk78YqrpbpvfmpkwhGX37LTyWmAauWt46wNVx_etnG1edV2wB_RYz0AQn5513hSGzZ-raI9skhFnpqBZjgtBIxp2f56BpiCIiy2RDPMtlDwTmi3Jbmk5IjI57sZoDl_REwqWPAyCqfPXxyUX-O8bd4-kndIAqRtkjl-fn56CzqxkdwI4dLp3SiwLQerLnoasm_oRMqmCcpERWSKnGaYWtGX8hqXCwrIYIY_aURUPIVP2_E96ReaJLmQEmMPBP7sHLxTjq867Ya-L8c1MloWqIRNKgSlWy4OlrmpOmDQZ6DnQiz7rgRtqSuhslgnYEGRvDI7g2V2J4FcrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af1fc50695.mp4?token=PEETLUd8xUk78YqrpbpvfmpkwhGX37LTyWmAauWt46wNVx_etnG1edV2wB_RYz0AQn5513hSGzZ-raI9skhFnpqBZjgtBIxp2f56BpiCIiy2RDPMtlDwTmi3Jbmk5IjI57sZoDl_REwqWPAyCqfPXxyUX-O8bd4-kndIAqRtkjl-fn56CzqxkdwI4dLp3SiwLQerLnoasm_oRMqmCcpERWSKnGaYWtGX8hqXCwrIYIY_aURUPIVP2_E96ReaJLmQEmMPBP7sHLxTjq867Ya-L8c1MloWqIRNKgSlWy4OlrmpOmDQZ6DnQiz7rgRtqSuhslgnYEGRvDI7g2V2J4FcrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تست شناختی : بایدن حتی سوال اول رو هم نمی‌تونست جواب بده
🔴
فکر نمی‌کنم بتونه بگیره اینا رو کدوم خرسه کدوم اسبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121897" target="_blank">📅 00:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121896">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ: «از ناهار خوردن با کسی که واقعاً، واقعاً موفق است متنفرم، چون او مدام درباره‌ی عالی بودن خودش لاف میزند و این مانع از این می‌شود که من درباره‌ی این حرف بزنم که رئیس‌جمهور شدم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121896" target="_blank">📅 00:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121895">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42665bf8db.mp4?token=aLLQsZmnWMu0HDtzjTxZ99oioI0YwRWeM7G5ukqBiONxPQ1xZllSB4oTYZubyHu5wiRbho4y-omzfeqotq1U-GH6iRq4ITjfissWgwr0_09FNT2lVhStmx2od_F3NBGsKGKHNqTw_2wIuOhymz0dybQbG9kTSSPPdDBZhDLLBQzvusbJjHmsRRpdiogVg2CMD5BPNPGBqjk_RjM91QU-G1V0Z8xIlvtf-9dJYmccXgMQY9y0g9vuxtYaP9gWZi1paAAoYXPQ-j8vBVnBpx1aFFyKszQv-75vKOd7FHsNUqVulUNJ1lWow401XOG1GVOhe-hYWGiTojs21SKGM8UkeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42665bf8db.mp4?token=aLLQsZmnWMu0HDtzjTxZ99oioI0YwRWeM7G5ukqBiONxPQ1xZllSB4oTYZubyHu5wiRbho4y-omzfeqotq1U-GH6iRq4ITjfissWgwr0_09FNT2lVhStmx2od_F3NBGsKGKHNqTw_2wIuOhymz0dybQbG9kTSSPPdDBZhDLLBQzvusbJjHmsRRpdiogVg2CMD5BPNPGBqjk_RjM91QU-G1V0Z8xIlvtf-9dJYmccXgMQY9y0g9vuxtYaP9gWZi1paAAoYXPQ-j8vBVnBpx1aFFyKszQv-75vKOd7FHsNUqVulUNJ1lWow401XOG1GVOhe-hYWGiTojs21SKGM8UkeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من مشکلی ندارم که به من بگویند یک دیکتاتور درخشان و تمام عیار، اما نمی‌خواهم احمق خطاب شوم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121895" target="_blank">📅 00:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121894">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45636768b7.mp4?token=HB5HqnZIF7WUVPvIX0TwDPZuJI0g3XSLDrgeWwB2gEAo5M2SBTvnZENeWFNGRFVXVi2M5klnVh67Z7Crvod3w1HztoLpwzserl99RF5haBXJwMEq_pGT9NE9G0jpr47XgkGwF1DHHD9thbQWyZQZMqpBp2Oyt5MVbyPPjyggQH2UR8kKjUsX_OngGVWL89VNSx5UUSLbDkUsF9IIZb3TN4bhdl1NRBlUj1hN98bP9aYLgGT12ImfOv56v96TiBuMN31-5l-tLibkMsU5TJXIdnazFmOeaezid5nC05loJAp6GURxxQeO9lgb5tzctiGdQIvtzH4oGX4YMXCuBf_k-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45636768b7.mp4?token=HB5HqnZIF7WUVPvIX0TwDPZuJI0g3XSLDrgeWwB2gEAo5M2SBTvnZENeWFNGRFVXVi2M5klnVh67Z7Crvod3w1HztoLpwzserl99RF5haBXJwMEq_pGT9NE9G0jpr47XgkGwF1DHHD9thbQWyZQZMqpBp2Oyt5MVbyPPjyggQH2UR8kKjUsX_OngGVWL89VNSx5UUSLbDkUsF9IIZb3TN4bhdl1NRBlUj1hN98bP9aYLgGT12ImfOv56v96TiBuMN31-5l-tLibkMsU5TJXIdnazFmOeaezid5nC05loJAp6GURxxQeO9lgb5tzctiGdQIvtzH4oGX4YMXCuBf_k-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما عاشق ماشین‌های برقی هستیم باید اینو بگم به خاطر "ایلان ماسکه"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121894" target="_blank">📅 00:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121893">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB9b45F0hVdlsyhkHnsZkQ7Q8-ls1MbXK-9dL6biLNod10Tkah4E4lPsShsyufXIU-I_IVpuQ6MBZY7WgeipEHtrrkuKdNjrzy8sUc_5xtEIWhuTA37xFtvS-jP-b6FggYuIBA-JHCCeJXir3QzgN0Y1Q4cQgIPgJCoyfJkqhOnxtqW3q97KxTuxkIOzUuE4Dnxmddrqdi2GgEEt2FcPTuXcLYptcDu4V4i3GmFCMZ0TdYogxWYh1dVUwNVj4TGsz8emfo935kOntELhA_curpL4uDeOaQUbAkYNUVkjxnSSHBfNyluzgrjCFOMoG-SQAHVpfwWV3BgDt32J3pF1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121893" target="_blank">📅 23:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121892">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb4da2ef4.mp4?token=DMgmc-sDEz7FDuU7whhGl3vXHqsHxEG2tPvb-q7_gFe9wokLZpgPc7iFmABjAQ0j07ukSsHRPp2c8UYQoEc_cjnq1bll3vkTwpV4gbqi3XW9EIugkIgN47PtvHf5RcPf4f-YkLKihpuMgMGz50Q3FhVbJqXdTcZQDINLKGkos1PQhjRp94hcHMs3DAL_H8S7xr6BEaSxXuxHMbysNUhxiiwotbGGBXKonJ3pv-tGrVbMLci4PYiGm1bmAoPhGX3jw91LoeprMSLsbI4nad6DW-6P5hYzUQk0Hx4E4qKhZL7qK51xbbHs9U-ELb8LT1yNwl38D9ccu8SDGfSol6Bsxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb4da2ef4.mp4?token=DMgmc-sDEz7FDuU7whhGl3vXHqsHxEG2tPvb-q7_gFe9wokLZpgPc7iFmABjAQ0j07ukSsHRPp2c8UYQoEc_cjnq1bll3vkTwpV4gbqi3XW9EIugkIgN47PtvHf5RcPf4f-YkLKihpuMgMGz50Q3FhVbJqXdTcZQDINLKGkos1PQhjRp94hcHMs3DAL_H8S7xr6BEaSxXuxHMbysNUhxiiwotbGGBXKonJ3pv-tGrVbMLci4PYiGm1bmAoPhGX3jw91LoeprMSLsbI4nad6DW-6P5hYzUQk0Hx4E4qKhZL7qK51xbbHs9U-ELb8LT1yNwl38D9ccu8SDGfSol6Bsxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما اینقدر نفت از ونزوئلا استخراج کرده‌ایم که هزینه جنگ را حدود ۲۵ برابر پرداخت کرده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121892" target="_blank">📅 23:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121891">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48e736075.mp4?token=YbI6vSJi154VtcWw-mZBwQyFSGoB4uiC0jG8d1trwEZ1HTXoXzwjlZQRgqJphqixaoDWfYgjdPKWgVSIOr9F9vwDgHHhkCVE1bssjwSeK-oI4mvCctKmr0OrSqw9KY-l4SM_4KaK4bJHD5sbc4EilC-r1VhT19TwVHEV44TLdCl9neu1cJhF571k9f6F5pkdy0lwoOjjpmaem3C48CvyMXJLkdIQwyqtu-_dmOBHDeSFkJ2YMF3DO5Y7HmJzU9ZooFYR-R1E_JRGZe3LvRnKDz2OZCDuruTY-ZVlhu3hQ8PQW1b_wjsOWGqLunU7DBD2_a8uAYtot2z4PAh-3zVVwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48e736075.mp4?token=YbI6vSJi154VtcWw-mZBwQyFSGoB4uiC0jG8d1trwEZ1HTXoXzwjlZQRgqJphqixaoDWfYgjdPKWgVSIOr9F9vwDgHHhkCVE1bssjwSeK-oI4mvCctKmr0OrSqw9KY-l4SM_4KaK4bJHD5sbc4EilC-r1VhT19TwVHEV44TLdCl9neu1cJhF571k9f6F5pkdy0lwoOjjpmaem3C48CvyMXJLkdIQwyqtu-_dmOBHDeSFkJ2YMF3DO5Y7HmJzU9ZooFYR-R1E_JRGZe3LvRnKDz2OZCDuruTY-ZVlhu3hQ8PQW1b_wjsOWGqLunU7DBD2_a8uAYtot2z4PAh-3zVVwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: من باهوش‌ترین فردی هستم که تا به حال ملاقات کردید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/121891" target="_blank">📅 23:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121889">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_jrC9voq8Z3AXGcQcbPIWA1dI3ueNrVqB-dvhdzld5LfSONV7oD6Fj7P5BX3IDFPGRNAcr68lZRN3yJXIVuyOnZ7olPcrc0awn1HykCWh8OLmP_XZDyb3hyN--c4hL_TDqIDzFkOWlR91MoA0NhTdw0aHdMWwZAKV_7jrIwZa7XSKGfhyL6ERX7l-uMQ10_KY9gaqWPGCCexxwa3NKqAuid1n7GpPaR8oksJyJIYOf5MB6nzsQtRNbQNevP16W6MGc38nBeE3UGet0v5gLcK6rq-4fmqdYxBgxTjhSVTZnskH5r99PTQqZmNehZf8-7EBL_P73r6ppMelLpKTcP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور گراهام: من معتقدم که آزادی مردم شگفت‌انگیز کوبا از چنگال کمونیسم نزدیک است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121889" target="_blank">📅 23:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121888">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
منبع نزدیک به تیم مذاکره کننده به تسنیم گفت: گفتگوها و رایزنی‌ها بر سر موارد اختلافی همچنان ادامه دارد و هنوز نتیجه نهایی حاصل نشده است.
🔴
وی تاکید کرد: پیشرفتهایی نسبت به قبل در برخی موضوعات حاصل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121888" target="_blank">📅 23:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121887">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=rByy1wuabqQHCpX72M_Vx2iUVE_VZnbxIhhXnSj8jaij3PZIUTXkvyrlBJTpAVQt_yX3aPdcq2JXZ_ymDT08UcwpiNFjgqg-brdeiaO1Z7pUgPRWEIWEEEwTBa_QNLKC0CBLO2KnHiZFf303p3_dBGbJzemPiwaqD7WMPNURdLgIPKzCO5LyBiD_pO4X86tKCx8F8wMVSxjGPrahcyGr_zvsnNJnE4fsG717Kwp6Srqp9vfpBRqNuaAdh9GBSJyE--LaeGAy9eNb0-FvO3P4PrsgYKYKg9Oe-MKsAJUpCYFCow22l-DaGVnrke1VTYqL97oZSw3Fq4bfiuJFgy_8RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=rByy1wuabqQHCpX72M_Vx2iUVE_VZnbxIhhXnSj8jaij3PZIUTXkvyrlBJTpAVQt_yX3aPdcq2JXZ_ymDT08UcwpiNFjgqg-brdeiaO1Z7pUgPRWEIWEEEwTBa_QNLKC0CBLO2KnHiZFf303p3_dBGbJzemPiwaqD7WMPNURdLgIPKzCO5LyBiD_pO4X86tKCx8F8wMVSxjGPrahcyGr_zvsnNJnE4fsG717Kwp6Srqp9vfpBRqNuaAdh9GBSJyE--LaeGAy9eNb0-FvO3P4PrsgYKYKg9Oe-MKsAJUpCYFCow22l-DaGVnrke1VTYqL97oZSw3Fq4bfiuJFgy_8RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکات عجیب ترامپ در سخنرانی امشب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121887" target="_blank">📅 23:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121886">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de2dcea48.mp4?token=ibjeOFA-mKrTW1akmAZ54Bku3soUTMl-z98Sxv3zrwAOmcyyNp8j8LuPX3arTEV_7jCZz5Vk8RWf4Il0zwEOP1xFRkNs9kBsDnfeCJnafqS7-gCeJaimqa2vgskhxW5t8VIEPpZgEl5Pc3_0SQk2eOH7gZMzQkxB3Fp0iJkTmrbhs_9k3IyAVEzkbn4w3E_xwVf-jYTEvfsZCv-CfHUvIZabkhq1B0A-fQCS1IHMjHFjJ6gt25TgulCjkLncRsjcQ8iP0bumhQ_yA8rDx1p9eRBEQHJhW3QWeTkIaKA0jMvM38mdVRQhjgN4wZoJYDBppVsMCWOIVL0eQUE4CDKx1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de2dcea48.mp4?token=ibjeOFA-mKrTW1akmAZ54Bku3soUTMl-z98Sxv3zrwAOmcyyNp8j8LuPX3arTEV_7jCZz5Vk8RWf4Il0zwEOP1xFRkNs9kBsDnfeCJnafqS7-gCeJaimqa2vgskhxW5t8VIEPpZgEl5Pc3_0SQk2eOH7gZMzQkxB3Fp0iJkTmrbhs_9k3IyAVEzkbn4w3E_xwVf-jYTEvfsZCv-CfHUvIZabkhq1B0A-fQCS1IHMjHFjJ6gt25TgulCjkLncRsjcQ8iP0bumhQ_yA8rDx1p9eRBEQHJhW3QWeTkIaKA0jMvM38mdVRQhjgN4wZoJYDBppVsMCWOIVL0eQUE4CDKx1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اعتراض کردن تو تجمع‌های من خطرناکه من چیزای خطرناک دوست ندارم دوست ندارم ببینم کسی کتک می‌خوره پس این کارو نکنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121886" target="_blank">📅 23:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121885">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e3d4db7.mp4?token=MtYEXEGKL-TdKsKG_CXLEZrPAmXN06uVC52xkgBubYXDA43IJRJAp6-cdPinZIsuEdDx7aWEOf2K9CGOqBdkWxhRK0q9fekolqnlPopPZ9hOA4uGBIlD8E6Q1piAIFwj_hUI8dg2C04Tc_kfW1IQosBGgbQumcOUGVLjLIZFlb9YuxmfNSOPCsbfbrz12md3oTxuFj638BGErOFV3KNsOgq1HAb0dl7_FBn9QTJvhns01swG7IjPJQ3GXjaCJZT2umZrKZ9kAwlYFGdGHpICEJqsJxF4qd2ykCfpZPfxIVmKjRoolIORDsVaD96zmFMCxKbscGIhPCy5hIZgHDwBIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e3d4db7.mp4?token=MtYEXEGKL-TdKsKG_CXLEZrPAmXN06uVC52xkgBubYXDA43IJRJAp6-cdPinZIsuEdDx7aWEOf2K9CGOqBdkWxhRK0q9fekolqnlPopPZ9hOA4uGBIlD8E6Q1piAIFwj_hUI8dg2C04Tc_kfW1IQosBGgbQumcOUGVLjLIZFlb9YuxmfNSOPCsbfbrz12md3oTxuFj638BGErOFV3KNsOgq1HAb0dl7_FBn9QTJvhns01swG7IjPJQ3GXjaCJZT2umZrKZ9kAwlYFGdGHpICEJqsJxF4qd2ykCfpZPfxIVmKjRoolIORDsVaD96zmFMCxKbscGIhPCy5hIZgHDwBIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه معترض که علیه ترامپ شعار داد، تو تجمع انداختنش بیرون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121885" target="_blank">📅 23:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121884">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef3e74afc.mp4?token=YY8QdTas4PeC1dagxqKLCskLxjas70UOe7_AArUhDnHXdUOpIMQL9U8VdBk2D55X_uAZvwXyclv5wNVnPsjehQhrXvgVtfVHJvka9d-rzsuLxatrLCeMvZlizD3haGvHCN7lIt9-dCGhxBfzXW6H9TxFrVOuadxqZbiuMjcCaxiLhG-2VbNNlsWakWl50Fv7uElReuapb66sS_IrCiXeSC4khPbdhqw6J0Rd_mh7zhF4CQG6VjE8VuBYKv7nwpWSL4VCakALVK2lfyHC6lxfSBRADHI1J9KE0vRM23AUS8fGqegs4Gd5Unk-ubt9kAO3ecTYEmk4p7atuiaQZO2v8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef3e74afc.mp4?token=YY8QdTas4PeC1dagxqKLCskLxjas70UOe7_AArUhDnHXdUOpIMQL9U8VdBk2D55X_uAZvwXyclv5wNVnPsjehQhrXvgVtfVHJvka9d-rzsuLxatrLCeMvZlizD3haGvHCN7lIt9-dCGhxBfzXW6H9TxFrVOuadxqZbiuMjcCaxiLhG-2VbNNlsWakWl50Fv7uElReuapb66sS_IrCiXeSC4khPbdhqw6J0Rd_mh7zhF4CQG6VjE8VuBYKv7nwpWSL4VCakALVK2lfyHC6lxfSBRADHI1J9KE0vRM23AUS8fGqegs4Gd5Unk-ubt9kAO3ecTYEmk4p7atuiaQZO2v8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  ۲۵ تا از بدترین شهرها دست دموکرات‌هاست آبی یعنی داموکرات احمق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121884" target="_blank">📅 23:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121883">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3439e4ce92.mp4?token=YgOENuFAd4Ww9MDdFuxkjTkigZlYKkwD6ZtwAbFYITReISmsd_dOJcbBNnkE-dOKiqpPHiYexvAFWlYstGSS6okGY2HGXFIdudx9akaKr_qTpEXJ3N_l9AIZ_wBoq94J1rmdUTLHgOvY26ASig6kg-kJQlOx3bTFdrIWpAYz7dGwFxlXbTj7gZD2XS78llLaP4DvuLUa_XsYH4rJAmVtc9VU14UR1WHkH-OqzMC1uHKYsBkpI7I1UnVCe_-o871x7myhnjhH_PYSjfUWozov1LI9XUJi4u6_kvUhhNdyNdEYWOwn7GsBfbxtf3qp9S-t_SAHPyyy9Q-LpWUM6GAiRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3439e4ce92.mp4?token=YgOENuFAd4Ww9MDdFuxkjTkigZlYKkwD6ZtwAbFYITReISmsd_dOJcbBNnkE-dOKiqpPHiYexvAFWlYstGSS6okGY2HGXFIdudx9akaKr_qTpEXJ3N_l9AIZ_wBoq94J1rmdUTLHgOvY26ASig6kg-kJQlOx3bTFdrIWpAYz7dGwFxlXbTj7gZD2XS78llLaP4DvuLUa_XsYH4rJAmVtc9VU14UR1WHkH-OqzMC1uHKYsBkpI7I1UnVCe_-o871x7myhnjhH_PYSjfUWozov1LI9XUJi4u6_kvUhhNdyNdEYWOwn7GsBfbxtf3qp9S-t_SAHPyyy9Q-LpWUM6GAiRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : دارم به جکسون نگاه میکنم به اون پاهاش نگاه کن این پسر خوشتیپه پاهاش مثل تنه درخته این اصلا برای زنا چیز خوبی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/121883" target="_blank">📅 23:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121882">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a94e327a.mp4?token=KrtLyalUt4bfY_Rddb0bBmFR7k-At1XSwwyZHaya1E_9myPuw5R8qUMRMt2N2WStVGK3EDt6lrwC_ICKembNawcQ60jdwyhkY7QpKRTMMuveGjVslh0ESGWgoOJHVKFcKkNy8MrfWwqiOyZY2mNssOc8RPj_GqKQPKUqQKBgfd-phIZhBpbmgaxGg6Ix6amxWN-Vxh5KwfF9EuFZaM9acnzz-6BtMu1q2xvg2N5bpTBUgkoSp-1u76wClVCja5x_lLWMiQW2lLZXRgs5dn1L4PP6hlIna3jKAIwbUt59LiPoWQLxrGOvHWTlo5uFpyO3oqMRagg75n0GV3D7depFXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a94e327a.mp4?token=KrtLyalUt4bfY_Rddb0bBmFR7k-At1XSwwyZHaya1E_9myPuw5R8qUMRMt2N2WStVGK3EDt6lrwC_ICKembNawcQ60jdwyhkY7QpKRTMMuveGjVslh0ESGWgoOJHVKFcKkNy8MrfWwqiOyZY2mNssOc8RPj_GqKQPKUqQKBgfd-phIZhBpbmgaxGg6Ix6amxWN-Vxh5KwfF9EuFZaM9acnzz-6BtMu1q2xvg2N5bpTBUgkoSp-1u76wClVCja5x_lLWMiQW2lLZXRgs5dn1L4PP6hlIna3jKAIwbUt59LiPoWQLxrGOvHWTlo5uFpyO3oqMRagg75n0GV3D7depFXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «من رای ۹۹ درصد نیروهای پلیس را به دست آوردم. باورتان می‌شود؟ هنوز داریم تلاش کنیم بفهمیم آن یک درصد چه کسانی هستند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121882" target="_blank">📅 23:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121881">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a94e327a.mp4?token=WmAXA5OMYZF-mlUqbB4U7j5RxTeU_ymnn8VhyKvLaD53NTKpB-rG9dThtBhocEsiSuCWBoun7pNSX4alFDlNabuzw49UxOZ8GsnpcbZ_4HN8NNbx_mBDZiMssYL0n94TaNjAUanjnREkECmEYN-AtzD-eNrPeIVIMVKmyDt2bR4nfaQZexm_YS5zBo3KeXMM-J23TDsdUscU8EKj3VgMHurxXQTe9UCG5NXS9C5i4Jogl7PN5cxDaQJCMevCZKRhpMvCLKmKAvi394O1MjhoSy-VR_AoXdywqptRR4yQg53wJq1mv9RNWEX9mdQygOm8O6rrqK00KAzhkLuPuQGHqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a94e327a.mp4?token=WmAXA5OMYZF-mlUqbB4U7j5RxTeU_ymnn8VhyKvLaD53NTKpB-rG9dThtBhocEsiSuCWBoun7pNSX4alFDlNabuzw49UxOZ8GsnpcbZ_4HN8NNbx_mBDZiMssYL0n94TaNjAUanjnREkECmEYN-AtzD-eNrPeIVIMVKmyDt2bR4nfaQZexm_YS5zBo3KeXMM-J23TDsdUscU8EKj3VgMHurxXQTe9UCG5NXS9C5i4Jogl7PN5cxDaQJCMevCZKRhpMvCLKmKAvi394O1MjhoSy-VR_AoXdywqptRR4yQg53wJq1mv9RNWEX9mdQygOm8O6rrqK00KAzhkLuPuQGHqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «من رای ۹۹ درصد نیروهای پلیس را به دست آوردم. باورتان می‌شود؟ هنوز داریم تلاش کنیم بفهمیم آن یک درصد چه کسانی هستند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/121881" target="_blank">📅 23:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121880">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزیر امور خارجه با دبیر کل سازمان ملل متحد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121880" target="_blank">📅 23:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121879">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
انور قرقاش، مشاور دیپلماتیک رئیس امارات به رادیو اروپای آزاد گفت: ما با ایران همسایه هستیم و پیوندهای بسیاری داریم.
🔴
موضع ما این است که راه‌حل خاتمه جنگ بین ایران و آمریکا یک راه‌حل سیاسی است. راه‌حل‌های نظامی عوارض زیادی ایجاد خواهند کرد.
🔴
فکر نمی‌کنم آمریکا یا ایران خواهان از سرگیری خصومت‌ها باشند. منطقه و امارات نیز خواهان از سرگیری خصومت‌ها نیستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121879" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121878">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وال‌استریت ژورنال:واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121878" target="_blank">📅 23:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121877">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
انفجارهای کنترل‌شده، صبح فردا در کهریزک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121877" target="_blank">📅 23:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121876">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کانال ۱۳ اسراییل: پیش‌بینی می‌شود پیش‌نویس توافق با ایران شامل حذف اورانیوم غنی‌شده و همچنین توقف پروژه هسته‌ای یا موشک‌های بالستیک نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/121876" target="_blank">📅 23:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121875">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0sY1i-wLNikUkCydBcK2q0oP292LB0qzktx3aW-yvuIF6FjDujPcUsXDWuL6V2qqK-CtUxIYLOYSNlXajWpVctJiDa3gd9UoQTQjqQYrL3-Mh9bw236Q4fJxh57YIcZpvzTDJK-cVGsTQbyisLyh_LyZzh9bNOL7ipGM42n48gVkGcK2B09j18fIN4pbi7I6zqyCE3UQz7fligQEFcGP4Ozj39qpLfT6wGHeGeHNzOstG9K3ahE4w0eFs1gTPAR3iONF54SNAEINpKKTfxsRO6joZc4bgb-0LvHrDUoa25hkuLWZvP-Gh0F9la1sOQBH8V_ImdxfY79jGkBDdIXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پهپادی اوکراین به سمت روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121875" target="_blank">📅 23:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121874">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
الجزیره: یک مقام مسئول ایرانی امروز به ما گفته که هنوز هیچ توافق نهایی بین ایران و آمریکا وجود ندارد و تلاش‌ها برای کاهش اختلافات بین تهران و واشنگتن ادامه دارد.
🔴
این مقام به الجزیره گفت تحرکات دیپلماتیک ادامه دارد اما فضا  برای یک توافق واقعی کافی نیست.
🔴
این مقام ایرانی هشدار داد که نیروهای مسلح ایران با نیت‌ها سروکار ندارند و اقدامات خود را بر اساس بدترین سناریو برنامه‌ریزی می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121874" target="_blank">📅 23:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
امکان دسترسی دانشجویان ساکن در تهران به اینترنت
!
🔴
معاون آموزشی دانشگاه علامه طباطبائی با اشاره به مشکلات دسترسی دانشجویان به اینترنت گفت: در حال حاضر دانشجویانی که در تهران حضور دارند، می‌توانند از اینترنت این دانشگاه استفاده کنند؛ حتی دانشجویان سایر دانشگاه‌ها نیز در صورت حضور در تهران امکان استفاده از خدمات اینترنتی دانشگاه علامه را دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121873" target="_blank">📅 23:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی وزارت صمت: بسته‌ی حمایتی ۷۰۰ هزار میلیارد تومانی برای ۱۲ هزار واحد تولیدی تصویب شده که پیگیر ارائه کامل آن هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121872" target="_blank">📅 23:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121871">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر نفت: در طول جنگ ۴۰ روزه بخشی از تاسیسات گاز، مخازن ذخیره‌سازی و تامین سوخت را در استان تهران مورد هدف قرار گرفت و اگرچه همکارانمان با استفاده از دیگر ظرفیت‌های موجود، بخش عمده‌ای از آنچه را که از دست داده بودیم، بسیار سریع به مدار برگرداندند، با این حال در ادامه بی‌شک نیازمند همراهی مردم در مصرف بهینه سوخت هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121871" target="_blank">📅 22:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121870">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
منابع عربی: تماس تلفنی وزیرخارجه قطر با همتای سعودی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121870" target="_blank">📅 22:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121869">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⭕️
⭕️
اپلیکیشن‌ها را فقط از Google Play یا App Store نصب کنید.
🔴
فایل‌هایی که در تلگرام، کانال‌ها، گروه‌ها یا از طریق لینک مستقیم دانلود منتشر می‌شوند، اگر از منبع معتبر نباشند می‌توانند خطرناک باشند.
🔴
نصب این فایل‌ها ممکن است باعث شود اطلاعات شخصی شما، رمزها،…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121869" target="_blank">📅 22:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121868">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خضریان، نماینده مجلس: ترامپ لات کوچه خلوته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121868" target="_blank">📅 22:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121867">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5G6n4XfMicnEXxTQqVjBzuL4GsoUOKB5RYyuKvQxj8EojaGdA4KuQgMwrPqrys1wvrhsmZbPIvMM-M79PWW2kysKwTQgLT3z_ohxguZ_CqMQkM9KeEUGlQ7Ooret0WZAz5jebirzSEpCU73wFCQPpUbl0YK-Vt1uMG8yv0bfO-T8x1lmf7L73F9FFNGL1D2jrTum4vfxpkVXfo_ByYRwQCvtCWDHrIcPoSJriXRRZ0Z-bHiTBo46PpoOtyYpLHRN7lcxaUhI9UPFKxqt0dwvZvnZtGfc9g5hTgKGZO9MWkJ8U7oQpPTXYgAJ111q9y5pVLHEEQOnOOmvIGqxzMrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منبع نزدیک به کاخ سفید :  با داغ‌تر شدن درگیری‌های نظامی تو ایران، ترامپ برنامه‌هاشو عوض کرده و قراره آخر هفته رو تو کاخ سفید بمونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121867" target="_blank">📅 22:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121866">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
‏پنتاگون با انتشار این ویدیو گفته : یوفو
🛸
تو آب‌های ایران
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/121866" target="_blank">📅 22:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121865">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc69f28eb7.mp4?token=c_WXDjoV832HLYDpsIV4DS3D5zruotSeSdzTwo3Fy4m-2LIixaEbE0C4IsQsKl0VdRaSRxFVjgAmjTteTEQOn6kN2ldnZPL2x3raDaLneer-ax5zIZhwMejwBeQ220BWOCBVh2qrOPmwP1PlyK0Ta1BvjL6TLhTId03yxLb3yPzWElqoAFOezJnbQzYtut36QgqpZ9n770ZJSzLo90o48qCzxhfS4S33CEGKlcTgugtPD0FewRx8sgk3F8n4UusIkZ0E0EL2U8XJNZMzgTBCNLRGaPDRZFU4YyA4F_kGd8kXsROrkz2kdyST0a2ujQe0h_6ZzeY2AdQnxc7-wFWpVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc69f28eb7.mp4?token=c_WXDjoV832HLYDpsIV4DS3D5zruotSeSdzTwo3Fy4m-2LIixaEbE0C4IsQsKl0VdRaSRxFVjgAmjTteTEQOn6kN2ldnZPL2x3raDaLneer-ax5zIZhwMejwBeQ220BWOCBVh2qrOPmwP1PlyK0Ta1BvjL6TLhTId03yxLb3yPzWElqoAFOezJnbQzYtut36QgqpZ9n770ZJSzLo90o48qCzxhfS4S33CEGKlcTgugtPD0FewRx8sgk3F8n4UusIkZ0E0EL2U8XJNZMzgTBCNLRGaPDRZFU4YyA4F_kGd8kXsROrkz2kdyST0a2ujQe0h_6ZzeY2AdQnxc7-wFWpVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏پنتاگون با انتشار این ویدیو گفته : یوفو
🛸
تو آب‌های ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121865" target="_blank">📅 22:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121864">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دو منبع ناشناس به رویترز گفتند که ایران این محموله را برای کمک به ایجاد اعتماد بین قطر و پاکستان که میانجیگری در مذاکرات صلح را بر عهده دارد، تأیید کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121864" target="_blank">📅 22:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121863">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرگزاری رویترز گزارش داد که دو نفتکش قبلی قطر که از زمان آغاز حملات هوایی آمریکا و اسرائیل در ۲۸ فوریه، موفق به عبور از تنگه هرمز شده بودند، توسط قطر به پاکستان فروخته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121863" target="_blank">📅 22:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121862">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سومین نفتکش گاز طبیعی مایع قطر از طریق هرمز به سمت چین حرکت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121862" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121861">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
پرفورمنس هنرمند ایرانی در خیابان
🔴
پیاز می‌فروشد و رنده می‌کند…
🔴
تا مردم، بر وضعیتی که در آن زندگی می‌کنیم، اشک بریزند.
🤔
امید به زندگی با جمهوری اسلامی برابر با 0 مطلق
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121861" target="_blank">📅 22:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121860">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
یک منبع رسمی ایرانی به الجزیره: توقف جنگ در تمام جبهه‌ها، پیش‌شرط اساسی برای هرگونه مذاکره آتی است.
🔴
هنوز توافق نهایی حاصل نشده و تلاش‌ها برای کاهش فاصله بین تهران و واشنگتن ادامه دارد.
🔴
فضای مثبت همراه با تلاش‌های دیپلماتیک مهم است، اما برای یک توافق واقعی کافی نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121860" target="_blank">📅 22:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121859">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: به نظر می‌رسد فضای مذاکرات ایران و آمریکا تا این لحظه مثبت است و پیشرفت ملموسی در حل برخی اختلافات از طریق میانجیگر پاکستانی حاصل شده است.
🔴
آمدن فرمانده ارتش پاکستان به تهران ممکن است دو هدف داشته باشد:
🔴
۱. حل اختلافات باقی‌مانده
🔴
۲. احتمال اعلام چیزی پس از نهایی شدن آن وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/121859" target="_blank">📅 22:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121858">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری /
آکسیوس به نقل از یک منبع نزدیک به ترامپ
:
رئیس جمهور آمریکا طی چند روز گذشته به طور فزاینده‌ای احساس ناامیدی کرده است.
🔴
رئیس جمهور احتمال آغاز یک عملیات نظامی بزرگ دیگر، اعلام پیروزی و پایان دادن به جنگ را مطرح کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121858" target="_blank">📅 22:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121857">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ایسنا: تلاش میانجی‌ها برای نزدیک‌ کردن متون دو طرف کماکان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121857" target="_blank">📅 22:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121856">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
اکسیوس: یک مقام آمریکایی، مذاکرات را «طاقت‌فرسا» توصیف کرد.
🔴
این مقام آمریکایی گفت که پیش‌نویس‌ها «هر روز در حال رفت و برگشت هستند» بدون آنکه پیشرفت چشمگیری حاصل شود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121856" target="_blank">📅 22:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121855">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yxnpe2yXKtagRsOumnEIRsGRxhTuTgXeeTVLQoMHudbpe1NA6UyE4RrkwOZm_IrWz3J9GYZ4di6pj34TsbceO3xWbmPXShdfFdKwZpQz80tPq0bglUakeGNXUr-Ula2HXIwL3QKRy1r31v2s43sEix-xjrun7HNBaXyrAn3Vx6ZaseMwlNLwkoeyV8VDrL5giJbvMCbcLkPsMPYVIh5IBJ5Wsfbcy7pN5O8qoTnB0gzrNWuv5xxfheGKSYrU_XpHOPz18-xdB3VbfpaH20fee7d0CJpNeePJqNlx2AALNwqXfsqKy0BtF9DdEglUANOdFyIAYukzIfPTNEMucnddfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هاآرتص: یک واحد مخفی در وزارت آموزش اسرائیل وجود داشته که معلمان منتقد دولت را زیر نظر می‌گرفته است.
🔴
این واحد: پست‌های شبکه‌های اجتماعی معلمان را بررسی می‌کرده
🔴
فعالیتشان در اعتراضات را ثبت می‌کرده
🔴
برایشان پرونده محرمانه می‌ساخته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121855" target="_blank">📅 22:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اکسیوس: یک مقام آمریکایی، مذاکرات را «طاقت‌فرسا» توصیف کرد.
🔴
این مقام آمریکایی گفت که پیش‌نویس‌ها «هر روز در حال رفت و برگشت هستند» بدون آنکه پیشرفت چشمگیری حاصل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121854" target="_blank">📅 22:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
دونالد ترامپ» اعلام کرد «آرون لوکاس» به عنوان مدیر موقت اطلاعات ملی منصوب خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121853" target="_blank">📅 21:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121852">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
یک حادثه امنیتی در پایگاه نیروی هوایی پنساکولا در ایالت فلوریدای آمریکا رخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121852" target="_blank">📅 21:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121851">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz1gPbAuaVbV2AfmuHukVSBYscTnpqpD-8MbJP76DN5Tg-9oYvh15jhJ4V0NDAnc4pNZAht5mQuUljj3ClQ8lsj2iB0F23mDblwuz2e53Lv2P5GSLsA-IxN4G89C2qV6hajC6a_i9TFJ3ymkilrLVve6Q5Ox5L1Cbuiz5t1MuWWMwFWSFQOUfUG8Z87BbNjEgEduP8rLwZvjE7BgJu7ecSUGcrtufWlZ69zFmgmjyEmhPPcVWpMJr5mywsclknOtHdf6DnoaWHbV-OZGggUqkKj9GpxqwDUroYyxEKxVZ6gYnfxrDWGc8BDw_nWCcit2zkFFbqHYehGALOWm5ZjTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۲.۳۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121851" target="_blank">📅 21:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121850">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKBW93FDVYQBBJEYR23G7diMYahhbDD1dWgoCY_cj8lfgaFJdYBs4-nK0EoP5KGBYX4b7iuH9BsBjgV4kFh2_LLJJ2_-QErBy1UbzHJmUee5OlbAJl0V4rIcZpeBNtq3Fw9UEU8wGrdE92jMOnYl7Ono-yP9esIYrHNO1QfpFlmcJWmCGmdvtNKIr6BBc8t5zPrtEUw9x1D2cmEFdNBzM_thoPAYHh_f2Clr8WQdhnFKzC_9mXUaT9CheGO8x3oVAGVXD59VgVWvkMFSLXp5i3Vs_nkWsb2rzjMPlT__TBN1uhnsZAwbazaTsbVQflM1xQEB01WZmxSKV5CW5kgutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گفته رویترز، تولسی گابارد توسط کاخ سفید مجبور به کناره‌گیری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/121850" target="_blank">📅 21:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121849">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ سفر خود به باشگاه گلف ملی ترامپ بدمینستر را لغو کرده و در عوض در طول آخر هفته در کاخ سفید خواهد ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/121849" target="_blank">📅 21:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121848">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh2sjIO9bk4NWJm3d9kLJCtqiTLe5GrLGqOvX2zGYbRpZ7nargPfiHgNK963JHRe2ezjNhYTyv21XLJB6rH7TfwYVHWntCYK6bgaqwzHUlgAaIwzVcBD_XHZbQn_WplZKKTllZ9VqRiDSwShow-IQRShyu3N6Ys6oO7PX0kU2Mp9UgeQnOZV4RDi2b5jBagkADsnHqxGYqu1htr8y0rGhJv5MNyd6F2i6gyoMlj5J3aC2uXp9NBo6RacJiN70vyMwXcUo0SfNFsS8XASgTHQueU3WBr_FKpmSpA50-11inq8GTLcJkHmPTu1AC5Tp5qNDgrY0Tr3_uD5WAsHWwDjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: متأسفانه، تولسی گبرد پس از انجام کاری عالی، در تاریخ ۳۰ ژوئن دولت را ترک خواهد کرد.
🔴
همسر فوق‌العاده او، ابراهام گبرد، اخیراً به نوع نادری از سرطان استخوان مبتلا شده و او به‌درستی می‌خواهد کنار همسرش باشد و به بازگشت او به سلامتی کمک کند؛ زیرا اکنون هر دو در حال گذر از یک نبرد سخت هستند.
🔴
من هیچ شکی ندارم که او به‌زودی بهتر از همیشه خواهد شد. تولسی کار فوق‌العاده‌ای انجام داده و دلمان برایش تنگ خواهد شد.
🔴
معاون اصلی و مورد احترام او در سمت معاون مدیر اطلاعات ملی، آرون لوکاس، به‌عنوان سرپرست مدیر اطلاعات ملی فعالیت خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121848" target="_blank">📅 21:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کانال ۱۲ رژیم اسرائیل به نقل از مقامات اسرائیل : تفاهمات بین اسرائیل و آمریکا بر این اساس است که اورانیوم غنی‌شده یا امکان غنی‌سازی در اختیار ایران باقی نماند.
🔴
طی روز گذشته، پیشرفت‌هایی در مذاکرات بین آمریکا و ایران حاصل شد. در اسرائیل نگرانی‌هایی در مورد به تعویق افتادن مذاکرات در مورد برنامه هسته‌ای ایران و خروج اورانیوم غنی‌شده از ایران وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/121847" target="_blank">📅 21:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121846">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایرانی:
یک هیئتی از قطر درحال مذاکره وزیر خارجه کشورمان هستند اما میانجی مذاکرات همچنان طرف پاکستانی است
🔴
سخنگوی وزارت خارجه: ‌اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/121846" target="_blank">📅 21:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121845">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a75475343.mp4?token=qji4xseagKt_SnEWwOoKs5hobRBsFySxPaE58v6pkHbsecXqZNli30KIyk8Nn8e4evV0If-zKfYwg1q8Kqo523sB5EEH6UVJfcDbDdfivZlU_aKGy7d65b7AVNtUuSBACz4AW8BivAziUZ9vzH61SWAXWk6JHVRBQcnSPs8BFuIPgZUUXyNykx3kEU4dsQSvfP6WDvJoxQL5-nmcy1wgLK1FhyiD0sJRtOnOYFv-vSl1zba0m3cG79EXzSc7mMThbnvep45fUnfY8sf4LjUOXdDoOwohnGt3s0_ydw97PM1l7MLcDsIqp36FZYABzeZJMc_zbV11t6KkNRlSr_cBs5qpW3Ecrlb_eEfHZjQVvYOxTjxTi1PWYYv5uzQkX9wf0ubB3f3AGbRU-2djkle7RsJ4JErMB_rTKX6SUsYrziEIxoV4gQqzV1zTfUdiaJOLcNr_YElcX1ZaoYsM8AqGKCRh1zZ2fj26a79UeZrSsffF9T_G6M__cpkCoK9DsDkHkPxitXuHpRAO9VBxWHDR8HBCnzUeiDbo7FsuoIHqk8kUx1bVUXtPjPQi_4rA-XCrbr1UFekzlm75Dhp8do77_l__5MUeUfg_vrgHC8-H6LIXU8M4MDP05W2sd3H50ua_a4eIZWLe2LCcYd7_E3BudV0Ik935ESD39qLQ4irGwKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a75475343.mp4?token=qji4xseagKt_SnEWwOoKs5hobRBsFySxPaE58v6pkHbsecXqZNli30KIyk8Nn8e4evV0If-zKfYwg1q8Kqo523sB5EEH6UVJfcDbDdfivZlU_aKGy7d65b7AVNtUuSBACz4AW8BivAziUZ9vzH61SWAXWk6JHVRBQcnSPs8BFuIPgZUUXyNykx3kEU4dsQSvfP6WDvJoxQL5-nmcy1wgLK1FhyiD0sJRtOnOYFv-vSl1zba0m3cG79EXzSc7mMThbnvep45fUnfY8sf4LjUOXdDoOwohnGt3s0_ydw97PM1l7MLcDsIqp36FZYABzeZJMc_zbV11t6KkNRlSr_cBs5qpW3Ecrlb_eEfHZjQVvYOxTjxTi1PWYYv5uzQkX9wf0ubB3f3AGbRU-2djkle7RsJ4JErMB_rTKX6SUsYrziEIxoV4gQqzV1zTfUdiaJOLcNr_YElcX1ZaoYsM8AqGKCRh1zZ2fj26a79UeZrSsffF9T_G6M__cpkCoK9DsDkHkPxitXuHpRAO9VBxWHDR8HBCnzUeiDbo7FsuoIHqk8kUx1bVUXtPjPQi_4rA-XCrbr1UFekzlm75Dhp8do77_l__5MUeUfg_vrgHC8-H6LIXU8M4MDP05W2sd3H50ua_a4eIZWLe2LCcYd7_E3BudV0Ik935ESD39qLQ4irGwKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم دوربین مدار بسته لحظه‌ای را ثبت کرد که حملات هوایی اسرائیل امروز زودتر جویّا در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/121845" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121844">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مباحث هسته‌ای در این مرحله قرار نیست صحبت شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121844" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121843">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: نمی‌توانیم بگوییم ضرورتا به جایی رسیده‌ایم که توافق نزدیک است.
🔴
تمرکز مذاکرات بر خاتمه جنگ است.
🔴
یک هیئتی از قطر درحال مذاکره وزیر خارجه کشورمان هستند اما میانجی مذاکرات همچنان طرف پاکستانی است
🔴
رفت و آمدها به تهران تداوم همان روند دیپلماتیک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121843" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121842">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nlvw0QS3XX9EQaC6GcK_4NZpeme5AA96nv06VMHDCewxe1QzoumxPmiRYh9JFZSmd9wq1TP4F4GfK7Cte86_yyYPnkN4mznbEy1aXX7Uwy2BWs7D9srhYK73M4beI2AHqCHC5OJjfDTXLM2d1tGnlfgB7B3OU-KzvrCkf2QxqM3XIAkJ5g0IdG2DHvZ6TaYEiuQchbQhnONfJNUVfc1-Mq6pjhzNgyMjaeVpct9oiqz9zGT5016dVAwUXUjUBv_dll99iMi2RvoBdRV7luX5x-ZjS0E-tmAMAlsnPLSI6JT6t5IejNNqqPeLiUz9OUwQrhtYDSAkhsZ15pRyw-278A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: با اینکه خیلی میخواهم در کنار پسرم برای مراسم عروسی باشم اما حس میکنم که مهم است در واشنگتن و کاخ سفید در طی زمان مهم پیش رو در روز شنبه و یکشنبه بمانم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121842" target="_blank">📅 20:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121841">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه : هنوز به توافق نزدیک نشدیم و اختلاف‌ها باقیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121841" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121840">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فاکس نیوز: تولسی گبرد، مدیر اطلاعات ملی ایالات متحده آمریکا، استعفا داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121840" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121839">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
آسوشیتدپرس: اسرائیل از تلاش‌های ترامپ برای امضای توافق با ایران خشمگین است
🔴
یک مقام که نخواست نامش فاش شود، به خبرگزاری آسوشیتدپرس گفت که دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه گذشته درباره وضعیت مذاکرات با ایران، یک تماس تلفنی «دراماتیک» داشته‌اند و اسرائیل از تلاش‌های ترامپ برای امضای توافق با ایران خشمگین است.
🔴
به گفته این خبرگزاری، کاخ سفید از اظهار نظر درباره محتوا یا لحن این تماس خودداری کرده است. ترامپ پس از این مکالمه به خبرنگاران گفت که نتانیاهو «هر کاری را که من از او بخواهم، انجام خواهد داد».
🔴
این اظهارات یکی از اولین نشانه‌های علنیِ وجود فاصله میان مواضع ترامپ و نتانیاهو از زمانی است که آنها تصمیم به جنگ با ایران گرفتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121839" target="_blank">📅 20:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121838">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رئیس کمیته نیروهای مسلح سنای آمریکا: ترامپ باید به ارتش اجازه دهد تا انهدام توانمندی‌های نظامی ایران را تکمیل کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121838" target="_blank">📅 20:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121837">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فرانسه هرگونه مداخله ناتو در تنگه هرمز را رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121837" target="_blank">📅 20:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121836">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/890d2d4def.mp4?token=vferExctGyDUYUcS-JEavhY0NDN3urKm0ocqy4twt3wcaS-sYLEmMTUMEwS-RNeP6oT9RXBV_8F3AcZrNpW4Ba-8WAN5bN-PeX-AmVJn71mA7zTbItkOclOQfT7DpAJ89TT_TUaUll8wctk65HGZWBJQ5C0IATS56eU6HUCol3_RsnyVza1Kdm2-GpLjslxG7dTIz-44Wfn_vUxGwF9lcIgkaUiw3zO4iiH32rsAiGnPumLX_TFQ4MnbTorKMmOnA47JjKXUBpaaXq7j_6MYRAAYhmoxHcCB8tK82Mdcw1drvfQWAF05FQAcCmH5M_BPU3UUqiY4gWJJkX9sYuXucCr31EP7Jd0zK5KgBb9h67zrjhwiwQehjj2BTRy9BVyk8OpWE9L06KbtfhjyZfRhUdKrEV_oj-csjfnAWmgKSPW1jazyXsxQbqGN96O60W84Pk9Q64nAVCkTzr3_gLcjy6rvftyWTewEZb02cahznoJmRonQewmtqEu1slbnI8SO7TmRoN4OQr8ITPOkcMvhH9lW0KWZVMa4FX_C-X05F07eXFp5_Wq5t-MAk7acFg_Vc9EuDL91o1NO-IWLGyhTf_8Zr3V6ZBx5fVelnK7RlJD72RbP9I1WBafyWEevCyjlL8rrM107ybgeV1p5jjn-2yBNUMtpiFxv_NXljePQHYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/890d2d4def.mp4?token=vferExctGyDUYUcS-JEavhY0NDN3urKm0ocqy4twt3wcaS-sYLEmMTUMEwS-RNeP6oT9RXBV_8F3AcZrNpW4Ba-8WAN5bN-PeX-AmVJn71mA7zTbItkOclOQfT7DpAJ89TT_TUaUll8wctk65HGZWBJQ5C0IATS56eU6HUCol3_RsnyVza1Kdm2-GpLjslxG7dTIz-44Wfn_vUxGwF9lcIgkaUiw3zO4iiH32rsAiGnPumLX_TFQ4MnbTorKMmOnA47JjKXUBpaaXq7j_6MYRAAYhmoxHcCB8tK82Mdcw1drvfQWAF05FQAcCmH5M_BPU3UUqiY4gWJJkX9sYuXucCr31EP7Jd0zK5KgBb9h67zrjhwiwQehjj2BTRy9BVyk8OpWE9L06KbtfhjyZfRhUdKrEV_oj-csjfnAWmgKSPW1jazyXsxQbqGN96O60W84Pk9Q64nAVCkTzr3_gLcjy6rvftyWTewEZb02cahznoJmRonQewmtqEu1slbnI8SO7TmRoN4OQr8ITPOkcMvhH9lW0KWZVMa4FX_C-X05F07eXFp5_Wq5t-MAk7acFg_Vc9EuDL91o1NO-IWLGyhTf_8Zr3V6ZBx5fVelnK7RlJD72RbP9I1WBafyWEevCyjlL8rrM107ybgeV1p5jjn-2yBNUMtpiFxv_NXljePQHYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121836" target="_blank">📅 20:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121834">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6abc6e496a.mp4?token=ICkRglUxj2DBDTyijfIOaJKPH0s4Wlpr2nLiJaKZu8x3C16kkfMUOuG-paPsWkiaj01VW9MgbuJgeaJYgacdGxATYn2H7Kgk8pCZg_DtMHq7XnozpKovEbCoFfeg_tXPvitIv3tOnh8nhKkxoAKJa3uNdoEmWAlWj2D2qXEhI6nw3BAfjDxZDspeK3ULtwZgQWxGwCNZm4yR1jBOIqD3zSjd2cDdfjWeOAjLzsE12IDC7QD_pMm7nlGG-AcwTsHYXOkBK1_I6ne88gd9aJt6UVOY4DrqvZ6vhkUgJThrXd2sTXeqZh9G0SPpkXgnRUxDbl62k8elyWqlbip6iXGrQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6abc6e496a.mp4?token=ICkRglUxj2DBDTyijfIOaJKPH0s4Wlpr2nLiJaKZu8x3C16kkfMUOuG-paPsWkiaj01VW9MgbuJgeaJYgacdGxATYn2H7Kgk8pCZg_DtMHq7XnozpKovEbCoFfeg_tXPvitIv3tOnh8nhKkxoAKJa3uNdoEmWAlWj2D2qXEhI6nw3BAfjDxZDspeK3ULtwZgQWxGwCNZm4yR1jBOIqD3zSjd2cDdfjWeOAjLzsE12IDC7QD_pMm7nlGG-AcwTsHYXOkBK1_I6ne88gd9aJt6UVOY4DrqvZ6vhkUgJThrXd2sTXeqZh9G0SPpkXgnRUxDbl62k8elyWqlbip6iXGrQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لهستان اعلام کرد که سه فروند نخست هواپیماهای جنگنده لاکهید مارتین F-35 لایتنینگ II ساخت آمریکا در پایگاه هوایی لاسک وارد شده‌اند و تحویل‌های بعدی تا سال ۲۰۲۹ برنامه‌ریزی شده است.
🔴
ورشو در سال ۲۰۲۰ و در دوره اول ریاست جمهوری ترامپ، ۳۲ فروند جنگنده F-35A را از لاکهید مارتین سفارش داد که ارزش این قرارداد ۴.۶ میلیارد دلار بود و خلبانان لهستانی هم‌اکنون در آمریکا در حال آموزش هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121834" target="_blank">📅 20:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121833">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وزیرکشور پاکستان که هم اکنون در تهران بسر می برد با همتای عربستانی خود گفت وگوی تلفنی انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121833" target="_blank">📅 20:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121832">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXQMyO9DoZ3ira4LnOWE9iao6bsdUQmzSua8DcWoKhJujq0K4mT6ETy5mb3mA27DLeuUkCSiS-t67IVs040z_WLmLmAnsJtzbioUzizzl6h2mFNZyLoI_P6jylBxJxhtIex9xWdQ0SBs696rlW-COu-I2hI98ryQpO9tsHXOfZ5nZeJ4VGo0G9KD9HIxWsDDAU4LnoWseSrR1a1Gi4WIv5lGjmNiXS0fdLI07pz6MG6nqnCFkc_5pKBkufcZCzSmeZLOqXlNLaSLBcgTT9lm4bEuytMZDLYwcUFbX6NS_1ytuxXUdN0GZA_7RxY_HnJeUOczYy9My1F4bR1jtjw7qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121832" target="_blank">📅 20:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121831">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
هشدار آژانس بین‌المللی انرژی: بازارهای نفت به «منطقه قرمز» نزدیک می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121831" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر کشور ایران، اسکندر مومنی، هنگام ورود رئیس ارتش پاکستان، عاصم منیر، در تهران از او استقبال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/121830" target="_blank">📅 20:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121829" target="_blank">📅 19:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121828">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ایسنا: عاصم منیر وارد تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/121828" target="_blank">📅 19:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121827">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac7a56144.mp4?token=qDiFSuBAW-F-ZFsJTxtMOovvySOFn8LspuHpBEowM3gfgQATu03lC6iCaOYLU6-hKN-UVHqVe1AODQALH2zOobaGu6zb8NT5pe1VGWtPLLNyyNyWmb8cMeHB-sfxSYTJnwzgqyJkJ_b27owJDr8jfyoBpnVsYdL-3aZLx38ziJN-YGjzs7gZgV-oaZ9BgkKAKY62LZKelYcEoELHgNlClozeC12UA0EGJDhPIf5puggVaaRK2JpThy-SiNLNpU0cEeOTgB9KbuEgsDiEKg2q2e1lb2NlT5SrKRU6Eq6Wrw1qlUo5BXO3zdjopdEhjBgu7u-sjL06eSSxDZur7xFcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac7a56144.mp4?token=qDiFSuBAW-F-ZFsJTxtMOovvySOFn8LspuHpBEowM3gfgQATu03lC6iCaOYLU6-hKN-UVHqVe1AODQALH2zOobaGu6zb8NT5pe1VGWtPLLNyyNyWmb8cMeHB-sfxSYTJnwzgqyJkJ_b27owJDr8jfyoBpnVsYdL-3aZLx38ziJN-YGjzs7gZgV-oaZ9BgkKAKY62LZKelYcEoELHgNlClozeC12UA0EGJDhPIf5puggVaaRK2JpThy-SiNLNpU0cEeOTgB9KbuEgsDiEKg2q2e1lb2NlT5SrKRU6Eq6Wrw1qlUo5BXO3zdjopdEhjBgu7u-sjL06eSSxDZur7xFcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوین وارش رسماً به عنوان هفدهمین رئیس فدرال رزرو سوگند یاد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/121827" target="_blank">📅 19:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121826">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند.
🔴
سفر فرمانده ارتش (پاکستان) به تهران ممکن است آخرین تلاش برای جلوگیری از بازگشت منطقه به جنگ باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/121826" target="_blank">📅 19:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f142d5eab5.mp4?token=Nn70c9LDgXnuslvGa1tzvrUW8nRby9IiNtSxgj31TXuk8ZiAW2PrCF0sns9bgVaovzqKZUK8MYZi2NXmL_v2BjMJR5TuMkSLqvZJZ7hoKeE3Z-hz3JyTC2irjUSDBRkIo8oZJofvBhT_VOoXWK8XOECh4zmj2PAktBDQog4sFnqx80NTRo3EcT9Gto78JuBP0rkQmlblit4T18NVUsp4bakFJnDLXo2Q2B7joUaplkUWY67XlxL3bDjwrlVyG2rmUfO0H6mx60BFE90UsxLyuUmQ1kiZY-w_MO_0Bsr06ZuF54KTctC9cBoKqkWWhnN7nVX7_oKuElgL94e3eY2Zzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f142d5eab5.mp4?token=Nn70c9LDgXnuslvGa1tzvrUW8nRby9IiNtSxgj31TXuk8ZiAW2PrCF0sns9bgVaovzqKZUK8MYZi2NXmL_v2BjMJR5TuMkSLqvZJZ7hoKeE3Z-hz3JyTC2irjUSDBRkIo8oZJofvBhT_VOoXWK8XOECh4zmj2PAktBDQog4sFnqx80NTRo3EcT9Gto78JuBP0rkQmlblit4T18NVUsp4bakFJnDLXo2Q2B7joUaplkUWY67XlxL3bDjwrlVyG2rmUfO0H6mx60BFE90UsxLyuUmQ1kiZY-w_MO_0Bsr06ZuF54KTctC9cBoKqkWWhnN7nVX7_oKuElgL94e3eY2Zzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من اینو زیاد میگم پادشاه عربستان به من گفت ما داغ ترین کشور دنیا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/121825" target="_blank">📅 19:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: ما بزرگترین ارتش جهان را داریم و بودجه دفاعی ۱.۵ تریلیون دلاری می‌خواهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121824" target="_blank">📅 19:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ : خواهیم دید که اوضاع چگونه پیش خواهد رفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121823" target="_blank">📅 19:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ: ضربات سختی به ایران زدیم و چاره دیگری نداشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/121822" target="_blank">📅 19:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: ایران به شدت خواهان توافق است!
🔴
همان کاری را که در ونزوئلا انجام دادیم، در ایران انجام می دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/121821" target="_blank">📅 19:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcbeb920f7.mp4?token=PVsGtRn3kAyGY9wbSUQjvEGmGG0S3eeWa09shKMSRdYVw-G0AGdOwp5Vug6SW8DmXJSySJ25dwhLgf31Uy4O493fc9pdz3A9u1yXTnUG2W5sAJS9A6PencfJM7QMFeZbOyz658wLubOO8svypH2PPhAoO9LTo_L0sIRrXXI603MRJMZ2X_ONS54o5JBatEvw9cdueV7FDjndXavHwZ1AQGZdxgxolfxsabXn6IZ42QROfx5GgPSYZT7zG8azT-_w9GHCto4UFYGadDjuvYJM4MBLhEaDHceU9ZRLZ11p6_kJ2Uk7kPls9u6KQ3UAi67bV2DcCu7mxVrlJ4DCBI--IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcbeb920f7.mp4?token=PVsGtRn3kAyGY9wbSUQjvEGmGG0S3eeWa09shKMSRdYVw-G0AGdOwp5Vug6SW8DmXJSySJ25dwhLgf31Uy4O493fc9pdz3A9u1yXTnUG2W5sAJS9A6PencfJM7QMFeZbOyz658wLubOO8svypH2PPhAoO9LTo_L0sIRrXXI603MRJMZ2X_ONS54o5JBatEvw9cdueV7FDjndXavHwZ1AQGZdxgxolfxsabXn6IZ42QROfx5GgPSYZT7zG8azT-_w9GHCto4UFYGadDjuvYJM4MBLhEaDHceU9ZRLZ11p6_kJ2Uk7kPls9u6KQ3UAi67bV2DcCu7mxVrlJ4DCBI--IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من با رئیس جمهور شی بودم و بهش گفتم ما بهترین ارتش دنیا رو داریم اون واقعاً مخالفت نکرد جلسه خوبی داشتیم در واقع با من مخالفت هم نکرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121820" target="_blank">📅 19:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee075f90bd.mp4?token=IqHJJ0ghYnghPQDXjaqcTBGnQrlMLOoGUlQvtFm_ECtOWLWQbPgd7qYXDBZqapDrjo6xUE5NpboXQuiAu9L9K_Ogl7F8qqE7l5h_W-DazM_sysXL0y5O4hKlen-TNB5kqcI-MaWnJGz73dlRMPvcf-m4Z4nAEfaqkToXg__yF6QGtcN3EiW71jnbt_pIwJP__v0RRp72-5CL6LKrYaW57Fv3kjdt54dz_Y1wUd8hnXNewNhXGGJt83ACYoEEAOVQS01CIdtqGjM6vaIHnYizL7FOVAAkE9zdNCe74r6Px5Grwgu1N1LELs53qm6hpJHwnqWualmtssqT3THE887Kjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee075f90bd.mp4?token=IqHJJ0ghYnghPQDXjaqcTBGnQrlMLOoGUlQvtFm_ECtOWLWQbPgd7qYXDBZqapDrjo6xUE5NpboXQuiAu9L9K_Ogl7F8qqE7l5h_W-DazM_sysXL0y5O4hKlen-TNB5kqcI-MaWnJGz73dlRMPvcf-m4Z4nAEfaqkToXg__yF6QGtcN3EiW71jnbt_pIwJP__v0RRp72-5CL6LKrYaW57Fv3kjdt54dz_Y1wUd8hnXNewNhXGGJt83ACYoEEAOVQS01CIdtqGjM6vaIHnYizL7FOVAAkE9zdNCe74r6Px5Grwgu1N1LELs53qm6hpJHwnqWualmtssqT3THE887Kjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما یه مقدار بدهی داریم که باید حلش کنیم و راهش رشد اقتصادیه قراره با رشد خیلی سریع از این بدهی خارج بشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121819" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645e2d127d.mp4?token=b5BXh8TvuheacEb3ZhElt2t89mwdG8CzeiS8pYQWWeQ7nCSqsLmDqV49ljU5f1Est-VEl2MbuOK6QanzlydkBOGxqc0jDhrSC6bWtRVIxfZZ_b0vm4NlMyZATc6mDiOsRDD9VETDsi3VkRpJqDiPiZlhi1nQMF10Io5MDSWNBy7n4zt91n5Qn08KMsCMc67pwFk00tQ9KZOXTkccS6vSfHu9PPL4a3Hb-_1wpyiJHac4cHAR6lZ8h_dPHsfcIrtkGQLsowB1rcwBW-cRyJkhByVMOeywvsZyjy38wFFi-2hRVA9hgcw2tUWhZQC-nAu9Omi78TJ89TiXjcxSd8jofA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645e2d127d.mp4?token=b5BXh8TvuheacEb3ZhElt2t89mwdG8CzeiS8pYQWWeQ7nCSqsLmDqV49ljU5f1Est-VEl2MbuOK6QanzlydkBOGxqc0jDhrSC6bWtRVIxfZZ_b0vm4NlMyZATc6mDiOsRDD9VETDsi3VkRpJqDiPiZlhi1nQMF10Io5MDSWNBy7n4zt91n5Qn08KMsCMc67pwFk00tQ9KZOXTkccS6vSfHu9PPL4a3Hb-_1wpyiJHac4cHAR6lZ8h_dPHsfcIrtkGQLsowB1rcwBW-cRyJkhByVMOeywvsZyjy38wFFi-2hRVA9hgcw2tUWhZQC-nAu9Omi78TJ89TiXjcxSd8jofA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جمعیت:
*تشویق برای کوین وارش*
🔴
ترامپ
:
فکر کردم این تشویق برای من است. خیلی ناراحت شدم. به اطراف نگاه کردم و دیدم که همه به شما نگاه می‌کنند. من از این موضوع خوشحال نبودم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121818" target="_blank">📅 19:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رایزنی اولیانوف و گروسی درباره وضعیت خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121817" target="_blank">📅 19:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
منابع خبری از سفر مارکو روبیو، وزیر خارجه  آمریکا به دهلی نو، پایتخت هند خبر دادند.
🔴
موضوع انرژی در بحبوحه جنگ علیه  ایران و فروش تسلیحات به هند از محورهای گفتگوی روبیو با مقام‌های هند خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121816" target="_blank">📅 19:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وال استریت ژورنال با استناد به داده‌های کپلر: ۹۰ درصد مخازن ذخیره‌سازی نفت ایران در خشکی پر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121815" target="_blank">📅 19:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رئیس شورای عالی سیاسی یمن: هرگونه تجاوز جدید آمریکا یا اسرائیل با پاسخ قاطع مواجه خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121814" target="_blank">📅 19:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1-KS2mgTx0QYhHJMIZY-gg-YPZS5e1NxTf3y4nyITrNeOwRZlN2bMKalKlyVopDu9ie0m_tMC9LqwI8dPy1vyrs0CgMuMoNDPqsznQEB1Xblsac1qdbtCK82_swvMIqp_T61JeEvTrUTWbiG4_e_nmEzX5R_39j3-6CKVlO8p5XwnhKYph3ci5NK1PaeyrBcj-9Ui3513IzgZHUFhh0t5b0T9GhpBm_Ktj93C7eoxPgpnDMrnujE5kIp40LEE5Anw0ieMAJ5Sg1lInvLkaz91L1H-CNA898iOHa52NzM04RtpDma_wq7LSG93-f5eVRAvrvYcmqmpZ3kTh51fhHTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الحدث: ژنرال عاصم منیر، فرمانده ارتش پاکستان، به تهران وارد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121813" target="_blank">📅 19:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وال استریت ژورنال: صادرات نفت ایران از طریق دریا به دلیل محاصره به سطح صفر کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121812" target="_blank">📅 19:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مقامات اتحادیه اروپا اعلام کردند که اروپایی‌ها می‌توانند انتظار داشته باشند که قیمت نفت و گاز حداقل تا پایان سال ۲۰۲۷ بالاتر از قیمت قبل از جنگ باقی بماند و قیمت سایر کالاها نیز روند صعودی را دنبال می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121811" target="_blank">📅 19:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121810">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
العربیه: اگر تفاهمی بین آمریکا و ایران حاصل شود، توافق تک صفحه‌ای به نام «بیانیه اسلام‌آباد» خواهد بود
🔴
پس از دستیابی به توافق احتمالی، مذاکرات جامعی در یک بازه زمانی مشخص انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121810" target="_blank">📅 18:53 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
