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
<img src="https://cdn5.telesco.pe/file/c1-UUzRPDMFrpp37Aitenah-07p7dfFkpTx1A6kUPIDn7JMtW6-bjggYRcZZXi85beImwQcNEQ1e8q76v7bf-662xcH5Q_IH2fEDp781lsSLpw6F9EUrPTj8H7xVj9fHtCE1v1S5LZCQD8Im712MoA2JZyjhRWq88mpcxG5qRY8Qf1zoQxUy1bsfbMzNkWRQG0Y-TzN4rDYsp8d0eZJS2ZBSfLY32FudILw2B4VqOrEVnHvH4J5AI7w46ENNiP63GhiN8VLUKCQ-x2xg1LUsWAL7zo4au_PF2GVaeh3sV4taxUZpFpJRrHQWC7U1Dk496tLjxxhSJUQMNPOM_EJ8sA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 547K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 19:46:29</div>
<hr>

<div class="tg-post" id="msg-101475">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=mn0FRZ6PmHsDv82ul5AP0tJ8NTXCPFkXrc9oZvVtgrpYnCbroM1iRe1MxHL67d02I-EJtBrxIYAIhcuYycqKfrSJLW_fLjmQeObsxYBOonXSCX-ZI4tbuYy8xb2egD3JOMAk0tVtpMaawZqcM1copcOVXUS-GIc_dgGSHOlfi7-IMP0BkzmbvsEqFtYqCMMRIbmAOFLk1XFyvZpShFkXgnkF096WVYKO534AWGIa6WPYaI7Calzh6cXSmws7xZIYQG4r02jmSMYp5dxVZyQCK4IkJK8nA2q_M3rS49Ec_uCHFjkm4P2GhvT7nwAeKuUwly9mPZ8zZwpPVegf2b9AmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=mn0FRZ6PmHsDv82ul5AP0tJ8NTXCPFkXrc9oZvVtgrpYnCbroM1iRe1MxHL67d02I-EJtBrxIYAIhcuYycqKfrSJLW_fLjmQeObsxYBOonXSCX-ZI4tbuYy8xb2egD3JOMAk0tVtpMaawZqcM1copcOVXUS-GIc_dgGSHOlfi7-IMP0BkzmbvsEqFtYqCMMRIbmAOFLk1XFyvZpShFkXgnkF096WVYKO534AWGIa6WPYaI7Calzh6cXSmws7xZIYQG4r02jmSMYp5dxVZyQCK4IkJK8nA2q_M3rS49Ec_uCHFjkm4P2GhvT7nwAeKuUwly9mPZ8zZwpPVegf2b9AmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفتم قبلا یه جایی دیده بودمش‌ها!
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/Futball180TV/101475" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101474">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/101474" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101473">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_1XW61mLLOUWRSWfRaR-SlOmAhMu7Eado_h8paXapd7vcEz537gG9Ir84Q9ujxnrjd0UEOwqfhf21mJx71QXXP1dAXPaGW1m1pTuJopW44AYZuXPhgl-tbzhjvlZg99GG6xwvmJegSb2tCCReDE4WocdCpTPGOc2O7d4y4PCHw9SGmTYhxwC7eM9nMlztl9AD4KlEIGiLYjFgUqRuAe0eQ1y5UqjpDpPYBgt5xBeeAop2W4cnd12GDUK7mjxTjDs4Al1rH7c28hAF8ktxf7vMI6hTAGC3eZckLjgouj1l0RNhcC4aEfk3Xiqyeo6Q-b-9rqM0Z5NvyHwTf6bOatew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/101473" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101472">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=i90N-d2zlHotlEG5IBb621GKVL4-ScLHmaqIp4M2a56PA-Na_Fy_NTpIX7FlMRxy4NrDcnlWKriIzl-LM8GJzTnR4N-dhzkcZor4JTZzdhK6fF2dgs04gSae0aw2rvYOXjYWyaqBCFTzcC3W8bU0awLX6ecQonkt6IUxPXQY4Ck5NVQ4oYZll41K6H0Df5hrp4YslwTTSQXtfa3FuNs-yBmhFOEJRF45M27eQplqwczEyaAXU-7DMPYnlnmhMKHIiuOR9QTLkbGef-KH6oWQqZCbb3Q5ChxplRpRO36XLKJUmVBHnSZ4SSCxYrew4mDkI7lCnU4iRk2x6Lg6-sFb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=i90N-d2zlHotlEG5IBb621GKVL4-ScLHmaqIp4M2a56PA-Na_Fy_NTpIX7FlMRxy4NrDcnlWKriIzl-LM8GJzTnR4N-dhzkcZor4JTZzdhK6fF2dgs04gSae0aw2rvYOXjYWyaqBCFTzcC3W8bU0awLX6ecQonkt6IUxPXQY4Ck5NVQ4oYZll41K6H0Df5hrp4YslwTTSQXtfa3FuNs-yBmhFOEJRF45M27eQplqwczEyaAXU-7DMPYnlnmhMKHIiuOR9QTLkbGef-KH6oWQqZCbb3Q5ChxplRpRO36XLKJUmVBHnSZ4SSCxYrew4mDkI7lCnU4iRk2x6Lg6-sFb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
حمایت رودری از فران تورس در جشن قهرمانی تیم ملی اسپانیا: "شاید بازیکنی که بارها و بارها، ناعادلانه ازش انتقاد شد، ولی امروز... امروز بخشی از تاریخ فوتبال اسپانیاست!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/101472" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101471">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=IH9bXX4uz-pcJRhNbVMplZCg4VMcrGf_qpxvOs6saOMuU1eTjWb14sXdb__aJNGcaDu7cZxIWkVBvi26WWgIsuJTkEHvHKtOgqEKXyJxg2mT-8H2ZQW_HWeEUBxELM3m_W2Hi-Q_gv20sN0gDC7UIeBsPXcE3CN6r7GZGisshErsS3Cs7PNu4TDy5uQe_b1CRcwMiQLTWnbfwdAyFrzSHMx4D_xTMzO6_epNTYfs6-FT0MXmxFhzUNE3JxP5qpuWBAk3TP6XowaH3ehEe5Eez7UaTS4LXgPjlSALDJ2hbmmehT0TpZJqyCWelmC34SX1NlkWFgGnoQuxjUgAXCaNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=IH9bXX4uz-pcJRhNbVMplZCg4VMcrGf_qpxvOs6saOMuU1eTjWb14sXdb__aJNGcaDu7cZxIWkVBvi26WWgIsuJTkEHvHKtOgqEKXyJxg2mT-8H2ZQW_HWeEUBxELM3m_W2Hi-Q_gv20sN0gDC7UIeBsPXcE3CN6r7GZGisshErsS3Cs7PNu4TDy5uQe_b1CRcwMiQLTWnbfwdAyFrzSHMx4D_xTMzO6_epNTYfs6-FT0MXmxFhzUNE3JxP5qpuWBAk3TP6XowaH3ehEe5Eez7UaTS4LXgPjlSALDJ2hbmmehT0TpZJqyCWelmC34SX1NlkWFgGnoQuxjUgAXCaNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
امباپه و اکسپوزیتو در میامی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/101471" target="_blank">📅 19:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101470">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1SJEK-AL9M5e3moAli5pPv9aCb8ceVu3LAmOCRP4_iUmlnOU3LODgZ0EeQpoWNtdSuVCJG4siuTuQ7HBTnoIn-Hzwp5_xpxqnxIhw8CasVSr4uo4QoFm96jvBqSWPbfY3650dbKQYnTS8nu3Bn4wSaYl0Ru-MJUyvozEKMfleBEnhrzZ5elgc0tL6UuDCJXXb16W92vSJSE1SF8WaMwPtQ3vthAKZPeakyUhFssgzF-lzuXQADE_MIgXoxiZqKVEVC57Os5Y1_6prN2AXSAHNpwayki25e93QGB1aZ3dmEeERRme_3EwQ3Qlq1pFPPbvYoOZuVeN8lS6nyUdMBq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه حدود دو سال پیش با دختری به اسم فاطمه وارد رابطه شد، اما بعد از جدایی، فاطمه باردار شد. اولیسه اول پدر بودنش رو رد کرد، اما بعد از تست DNA مشخص شد بچه متعلق به اونه. با این حال، گفته میشه هنوز مسئولیت پدری رو نپذیرفته و فقط از طریق وکیلش پرداخت نفقه رو قبول کرده. فاطمه هم پیگیر حق و حقوق خودشه و این ماجرا باعث موجی از انتقادها علیه اولیسه شده؛ تا جایی که کامنت‌های صفحش رو بسته.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/101470" target="_blank">📅 18:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101469">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=Zp15kol6Asidzxm6N5-w2zbS2POil1FnT2fZyebRGEvgIFRSU_kdafvOwrl5xbqkEdtVxZdWryR_-1N0JIRaqiioFZqWKmJOdqKu2t43CPWiubsUC2nuf6MHZahgEzziPAOodj5If1IpB7RUQOaiX6sXhtYuubQJnVbZ72HhS1XxgbTVprtAROdwTCRaOIJsiEsrmPN3afICyiXklpuojKeYz6KQVCv6dLrcg8Z0SHMQOy14Dag9gzEjDkyVJEkbSvZLbZxANkK9q9QwCyZP2NtgVHTlMGvPgrO8_QgcV75gO6FkpUlWIVvdA3yaIgI0on8RNmnTtPOtYnFmJbbYlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=Zp15kol6Asidzxm6N5-w2zbS2POil1FnT2fZyebRGEvgIFRSU_kdafvOwrl5xbqkEdtVxZdWryR_-1N0JIRaqiioFZqWKmJOdqKu2t43CPWiubsUC2nuf6MHZahgEzziPAOodj5If1IpB7RUQOaiX6sXhtYuubQJnVbZ72HhS1XxgbTVprtAROdwTCRaOIJsiEsrmPN3afICyiXklpuojKeYz6KQVCv6dLrcg8Z0SHMQOy14Dag9gzEjDkyVJEkbSvZLbZxANkK9q9QwCyZP2NtgVHTlMGvPgrO8_QgcV75gO6FkpUlWIVvdA3yaIgI0on8RNmnTtPOtYnFmJbbYlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه‌ریز دیشب رضا جاودانی و عادل فردوسی‌پور به محمدحسین میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/101469" target="_blank">📅 18:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101468">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3BeFVtf-s7bfqxMNtE0CtVx2sZ0-b5I4Uvk2Ikd8zznP4N2zbdxoAzxI3gEr0hlDaXecc2M8HN8Q5HvOf6B3c3uceWU7gpROKtUfePWqVZGUBuTZVY4jP9YK8V7lh_FDc9mtJLgTb9xkf5Hzd6QehXEVyx_ai8YsfLMiod3kPrKKt4G1EShENSAnKs9nJ7XyuQNAnWVfoUhZxmA9EAXwSLAXNU_B9SN4hzZlILe3Tbiw923ongD877o74xwKzWZSlQs97BPbdKElRUrTlWgWb4ipOuWAnutjvBWmVGTaCKAfuuwyoHfGtU_yiDQh8HfKTGxDmisjR4YPPVgXcDumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه روی جلد FIFA 2027
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/101468" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101467">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk0L2h2lbKy9HVFpv4hLP0GD3I_upzTfFoHr0x6AFmQlwL31m6TVIKjY7LHuSj-2jJqkXxP1CXedOpnTHIj-Puasnz5AN6sMIDbiROCndtKYJCvRw7JGpkGB3nO5F0rb2zXjnGiqFD_19EKBup-uXwfSQ6TxRH5BINIyPbakyCLHOiXe1J5GIygxFELWJbpH7bPgBf5hjUlWbqlN4eEE19Vcc3W5sgh8e2Z_R3x-y7p1ynk6avpTZdrL7fa1CHlM9E9Gs7Or2nfZKzvV_vPSAn7hLx5rVe5H2U9s-89_X-JnzvPbbh7Hy5vpTWDIk4JGDyzOgnruFUufDWZfFGBkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتونی تیلور، داور انگلیسی بازنشستگی خود را از داوری اعلام کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/101467" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101466">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhpWQxbCdqsUPqed0prjxvaGc8jNZoDPLpCDC1BMuHq1UNkOb5eeDvxP9RnckeWQhE7UOdIiY6eWPaPPi1sv45fOXO7g57xRoFHW-uarkQzEQLnBq5-RCqg6IP7gA-KwbLg0BIR089qbClux1IDOXsL7zV2EFoIUs3odytac0XnGOJvKOobzGCShwezxnTYscMI1zWdCYg4Mbg9A7pouHUbU9dV2PEpXCRVsfs_0YcKSq-QRF-0f2lEDs8N-DMUgk8jrXD13snj4Zvv2K_GBim4as-Gp1ZbHkM4GzRwxelQiDPTujuO-i6mD6r5gTl_wAY3BFEePlK8dWlu1WXB1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ماتئو مورتو:
الهلال در شرف تکمیل قرارداد سامرویل است.
الهلال معتقد است که پیشنهاد بی نظیری ارائه کرده است و امیدوار است در ساعات آینده همه چیز را به پایان برساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/101466" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101465">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw6d0w71nAk9EwNt9MAFkRjHGoUvD0j4aWdCW7zU3NTC4gNh-Ed8GBe_BsYPNRUgRPd0RnUCz_TV9C3nEK6Y1T9o2NTpiINAZWP5iHCACAKpxHP-naVLpm4Y_xlggb35CupEHIuKxBtmQmvWWieN_Y--GfQXGqKVzAqjON5nRJDlyvxs8M9J1JzMjrHkJvjwkiW6m7uKXX8_wbRtNskF_fPa-nHK_n2RV2A5_N3j9c6RQ8rt2WQxWKdBiNF4HPzzF2cKzd0jIsdX5KJMD1qB1PBoRmtH3D454tL6PVwm6A48MWAPKIDLdygeIixcuVE9aTIE4nxbqVVhzzT0tRgSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
تیم‌قلعه‌نویی پس از درخشش در جام‌جهانی با دو رتبه سقوط در جایگاه ۲۲ جهان و دوم آسیا قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/101465" target="_blank">📅 18:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101464">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21557090e.mp4?token=BAAc91it5rXzN1vYTc8NkcfPgF8I332CbhKiSpjyU1cC3hTh2-YYRZRZAbpxzlC6F7GgTHU8cbp8njG6M7TuZBiMT5wbCjSlg8KCW1jDvQDoDd6PDfm2Uvb7lnEPBU37EJU_4B10-gmFeOBuq6plmk-HcRxtoB68l3Tub6g2LrrsX6txvXiWMYwIyTQuDJlJUiLqH5Zh-i4Mced8fcITfiZZzRIKQvpJug_elQIlzzzsEB3MHxdLKsCdZXGSlo-2dYuKKt1sS-1Im_fFTpIocjebaRY0JGY6_FJzKNDzlLu4ZX10z0bkDtRV3GkcK7y3f_74uj5EVbMCZw1zmbBRXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21557090e.mp4?token=BAAc91it5rXzN1vYTc8NkcfPgF8I332CbhKiSpjyU1cC3hTh2-YYRZRZAbpxzlC6F7GgTHU8cbp8njG6M7TuZBiMT5wbCjSlg8KCW1jDvQDoDd6PDfm2Uvb7lnEPBU37EJU_4B10-gmFeOBuq6plmk-HcRxtoB68l3Tub6g2LrrsX6txvXiWMYwIyTQuDJlJUiLqH5Zh-i4Mced8fcITfiZZzRIKQvpJug_elQIlzzzsEB3MHxdLKsCdZXGSlo-2dYuKKt1sS-1Im_fFTpIocjebaRY0JGY6_FJzKNDzlLu4ZX10z0bkDtRV3GkcK7y3f_74uj5EVbMCZw1zmbBRXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم چه حرفایی علیه مسی و آرژانتین میگن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/101464" target="_blank">📅 18:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101463">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">😢
تمامی سفرهای استاد اینفانتینو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/101463" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101462">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4ba1VhD2iGzdlO0CD2YXypc_nsdiiCJkbqjPBecIb8SqS7tOpEuJPTnp3wgX65BSqQ27s6tfe5i6GOlNniG0pCuVgegRWvWV3pfzXTqiEgU66ULRTSSCh9j6uowFPlbmGJj0c3f0KyVDcvhqzQP2VQjmmfLoEK-ZOjbBPHQYK-790a745viBQXxwiqjol6PiL6pGtGfPVRx4pODBUd8O-fQjJPdBae-Q07nfe60mxdJLF5Cbn4yHs5dAIxZVHngWSL9c14UTsYw6GFOcJEanoekqeD06oy4iQXs1IfQ2ButBirZhuJX8T3zFPB9Orheo9_ch0wf2Me4bd1OsPDhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: استون‌ویلا با ارائه پیشنهادی به چلسی خواستار جذب قرضی گارناچو با گزینه خرید در آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/101462" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101460">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-KWVnA2YIXGLDdul_ADCdunqTzLBt9jB3D0TxtkkTMD_UPRLSPSWkhwCRY_yhOhMLlnnntw_qG-IZJQBzUFFucZzVSzaFDqVk65P3v4RX9rwZxzBm0PK3RnPgO74nZRRY7l8cGCG0N4r2p-Nm7fOq0d3jLn-Tl9bijbJsqx7vHsu0B-0v_wRQSkTvxH3b2Jw3eFJvtQy03jR7rH35W4F0JLERajZsyni65AWSFR9X8-54ju3xzX-utwGHZUIAgEL9a1yJnWKxoTWDxqvENlAwEjf5tPYonsgZjDwp8k7wpDHrNgrRtcQCjM9UBanlX9k3PoYgWJfV83TiBsWXCq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJXjEuvfUFYWQIHhVj8Ev5JHBDfNBboq88zrHouifXYhGtT-qvZMVUtzmLPIgBMcVx0Off45NJGfsUQ3bKgK0KT40E5UmT_UfqKquOoWSBp2zTw-gplGoeCb1KlF8-W6lNd-wdCeK9UxbOgrUVG3wkCZTvXiQeIk0BUV1HJCyt284yd8DY4NErdz3R7k3dkIjmQIwwcf7xsMOeu88XrPEIpasN6GRmBumblO7R3GZRCV-Iv8R5EUWcChgl9R7kiAdxclbHYf68yOxSW-0Zcvqe4OaPHYkm0ZlP9bmpWE2Lv8LMlkhkpWcDdN7uIU4hp5H9HZj0RqhyMzOFXJ2nrgeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصور کن ۵ سال کنار یه نفر زندگی کردی و خاطره ساختی، برای آینده‌تون نقشه کشیدی. بعد یه فوتبالیست با ۵۰ میلیون فالوئر، شهرت جهانی و حساب بانکی چندصد میلیون دلاری وارد زندگیتون میشه. فقط دو هفته طول میکشه تا اسمت از روی صفحه چتش حذف بشه و جای تو رو یه نفر دیگه بگیره. چند ماه بعد، تو از پشت تلویزیون داری جام جهانی رو میبینی و اون، کنار همون ستاره، تو جام جهانی از کنار زمین لبخند میزنه. اونجاست که میفهمی پول واقعا همه چیزه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101460" target="_blank">📅 17:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101459">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=Dhy_QojMM-bbyXnz4qVLA3ZNPFKBPmX3k4YigPBLXG6lhlq6FB9rYSWyB6uOP-sbnS4HDtxj24LUgyTnx3LIEXhz9TNBGFikDXQeEeCdANyL9oi_NfxGWM-y_6XoFLeZfkXYG2Sm5S2CF3c1RXcmiDt2kT4KS2JHag0lg27jeSQWijLYJXb9XBhEZLnuxWTJBXOodf4dgq7XCPF8rLOwwfYzlYYXYq3ltxaTdNADEH_NWchyrBBvbbAaPAZTT0hlCZHGqovK9k98UrZA0nEd0zczvuKus7jt9zSV47h-EhUgj9bk1yNU2oMeR6e39_jGB0IwnEpJHAC91mfhIk28BwaTGbv4DhUK-Hf6PkNIeYUON3fYdU-flYl4Ebfdz1zJvSG3K5kSon4fRwY4JaOCA1bGcKBSMXWqXhXecA1uA2CFjwGerh-xOkKpW8KdCsh2m96-XMBF1Gs7N8uSy8MomRarynvFdj7Te2ZTecDW32Epb0mTAiU6kRgWeyQawjsDeQB7ycov_tbbCeIPFUkIZXZ9L3CMSpRX2wjKZReaFHsVmUPyCiONYJIb3X1odGRQ_S51Tr6VJD7qYMXz3ch65sg6Jv06R4hSLUN-rfWM7CXh3a_D12isgc1-DIDLXE9rGJt_3xpkAgMPtsYNqewibF35NBmQXvYnILLyusw_3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=Dhy_QojMM-bbyXnz4qVLA3ZNPFKBPmX3k4YigPBLXG6lhlq6FB9rYSWyB6uOP-sbnS4HDtxj24LUgyTnx3LIEXhz9TNBGFikDXQeEeCdANyL9oi_NfxGWM-y_6XoFLeZfkXYG2Sm5S2CF3c1RXcmiDt2kT4KS2JHag0lg27jeSQWijLYJXb9XBhEZLnuxWTJBXOodf4dgq7XCPF8rLOwwfYzlYYXYq3ltxaTdNADEH_NWchyrBBvbbAaPAZTT0hlCZHGqovK9k98UrZA0nEd0zczvuKus7jt9zSV47h-EhUgj9bk1yNU2oMeR6e39_jGB0IwnEpJHAC91mfhIk28BwaTGbv4DhUK-Hf6PkNIeYUON3fYdU-flYl4Ebfdz1zJvSG3K5kSon4fRwY4JaOCA1bGcKBSMXWqXhXecA1uA2CFjwGerh-xOkKpW8KdCsh2m96-XMBF1Gs7N8uSy8MomRarynvFdj7Te2ZTecDW32Epb0mTAiU6kRgWeyQawjsDeQB7ycov_tbbCeIPFUkIZXZ9L3CMSpRX2wjKZReaFHsVmUPyCiONYJIb3X1odGRQ_S51Tr6VJD7qYMXz3ch65sg6Jv06R4hSLUN-rfWM7CXh3a_D12isgc1-DIDLXE9rGJt_3xpkAgMPtsYNqewibF35NBmQXvYnILLyusw_3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
نیکبخت‌واحدی: ۵ ساله پارتی نرفتم و الان دیگه با وجود هزینه ها نمیصرفه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101459" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101458">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHa0-ytl43CERasALwFNTAu6l6omzO4n187rfEC1vd5UDkheI31FC8VFWqk_rPfcfjuZrOBZyx9CCpo0i8QohN9Gs-pvNyQjLiDiUp_urBNJnOKZNkUwmzUtZjYL8bGSkuemrY0UU5V2bTomZptcRJebEkMNy-VBOu5lTZIq32UiUY-BwwBnooP2hyLWyxNdHhP3gbJ-uou1H3k4fSrRvQU_QAcBSfKhGdRgcKJtUP58YUYOzw_vIUz6WoSUsOGxvTtNNm0SwI5lQezIEV_l6ezkf2UVJIYTuwFz1Bx9wWLhRohiToYxzl2L_S0vopUB1ZT9ZzrDoVz_43t5kH3djIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHa0-ytl43CERasALwFNTAu6l6omzO4n187rfEC1vd5UDkheI31FC8VFWqk_rPfcfjuZrOBZyx9CCpo0i8QohN9Gs-pvNyQjLiDiUp_urBNJnOKZNkUwmzUtZjYL8bGSkuemrY0UU5V2bTomZptcRJebEkMNy-VBOu5lTZIq32UiUY-BwwBnooP2hyLWyxNdHhP3gbJ-uou1H3k4fSrRvQU_QAcBSfKhGdRgcKJtUP58YUYOzw_vIUz6WoSUsOGxvTtNNm0SwI5lQezIEV_l6ezkf2UVJIYTuwFz1Bx9wWLhRohiToYxzl2L_S0vopUB1ZT9ZzrDoVz_43t5kH3djIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🔵
محمد خلیفه سنگربان جوان تیم‌ملی با عقد قراردادی به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101458" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101457">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=U7BYIXwL8-mrF0ClEwTNC_0TAxhf74-GR7XovpHtl1bHBHOoiacdS3zc8PKntpmoIYaBIEfQCka5P49RNi3flv9-t02_ZuwVluea70g0MhfeXlUmmbd6bg_7aKft23Yf9c6Hs0LWT9Wanq9ay3ZQKfQVg4NX15wnZPQuTqyzQF9Xgn0HpqNonzpY2C1_4P0GIcioRAYw_7b3wwVrSj43jS2IhJo42Gp9D3WLT2_nSJkBl7MKZIkJJJsDua5y_CpliU-OiE-34eoYMWAnFIb0LW5-ubvJUY27fHz58vrEkxZ4-GaBlCY7MGz8x1D4tlbA_E2AqCKzSk058bMDUhf-tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=U7BYIXwL8-mrF0ClEwTNC_0TAxhf74-GR7XovpHtl1bHBHOoiacdS3zc8PKntpmoIYaBIEfQCka5P49RNi3flv9-t02_ZuwVluea70g0MhfeXlUmmbd6bg_7aKft23Yf9c6Hs0LWT9Wanq9ay3ZQKfQVg4NX15wnZPQuTqyzQF9Xgn0HpqNonzpY2C1_4P0GIcioRAYw_7b3wwVrSj43jS2IhJo42Gp9D3WLT2_nSJkBl7MKZIkJJJsDua5y_CpliU-OiE-34eoYMWAnFIb0LW5-ubvJUY27fHz58vrEkxZ4-GaBlCY7MGz8x1D4tlbA_E2AqCKzSk058bMDUhf-tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/101457" target="_blank">📅 17:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=i5OebZxyyO0q7df_tkXi6mKn5YqSODP7kiry4jUR3aR_yw7Ax0hcrhzmnRjv2heQMY4XoNk59Guf6mC9EGPbfwdzMyCLDOcQk8MtdsdV5HV5dlQ4PyD0ZxnMFq8mf9oC1iwVk3FiKtbQ-16jd_zdcWM0_32eyNpZBiPFvmhtwBNNA0WeDSMVhyFAGP5edg3Q1iaRhAmpE49pHbZ4Xp1iQLbz-Mulv4zgILQS8iMR7i3wZxglYdko8MhzC0RGdYRpjTsH_AWmxm0d64TRyNDUq8f_aPUIN1-aEEzIbG5XpzMnzVQL4UPdiS-fb7NpQfXrER3qaU5Ng9L5TDbWnealKiNQ2vppX1JDhquMAAT4SQzuzVuqHyS00R39aTqBGlZyhPwck18F2Xm0X1imHZ5k4EtgxHTHCLOO9u1eHrAZtE6GoLZOAggSNyStrWWYNim6ZkIoWEpyCLk9TcC8ZyD7sa08uTxhg26STXMFeivxUhPLn5R2fzG5ao80RRVGq2XswUknrOfgJNsr0fHR_U53xrD5WTddUIpvPu7V3pck8l1s1NA-VQXEmTF0CQcE9GZUEftdCoWM6vQrwAfU-Z5KYK1-r-GOPx9fyib2c7APOu07CNs0hs9gCs9lc45fj5SgeoVsYQSuXeU_ao3HVx96rWHivDBBMiUw6I_s--dOZqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=i5OebZxyyO0q7df_tkXi6mKn5YqSODP7kiry4jUR3aR_yw7Ax0hcrhzmnRjv2heQMY4XoNk59Guf6mC9EGPbfwdzMyCLDOcQk8MtdsdV5HV5dlQ4PyD0ZxnMFq8mf9oC1iwVk3FiKtbQ-16jd_zdcWM0_32eyNpZBiPFvmhtwBNNA0WeDSMVhyFAGP5edg3Q1iaRhAmpE49pHbZ4Xp1iQLbz-Mulv4zgILQS8iMR7i3wZxglYdko8MhzC0RGdYRpjTsH_AWmxm0d64TRyNDUq8f_aPUIN1-aEEzIbG5XpzMnzVQL4UPdiS-fb7NpQfXrER3qaU5Ng9L5TDbWnealKiNQ2vppX1JDhquMAAT4SQzuzVuqHyS00R39aTqBGlZyhPwck18F2Xm0X1imHZ5k4EtgxHTHCLOO9u1eHrAZtE6GoLZOAggSNyStrWWYNim6ZkIoWEpyCLk9TcC8ZyD7sa08uTxhg26STXMFeivxUhPLn5R2fzG5ao80RRVGq2XswUknrOfgJNsr0fHR_U53xrD5WTddUIpvPu7V3pck8l1s1NA-VQXEmTF0CQcE9GZUEftdCoWM6vQrwAfU-Z5KYK1-r-GOPx9fyib2c7APOu07CNs0hs9gCs9lc45fj5SgeoVsYQSuXeU_ao3HVx96rWHivDBBMiUw6I_s--dOZqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
زد و خورد شدید مردم بنگلادش پس از پایان فینال جام‌جهانی
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101456" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=pABTumjlXpsFqnvM1gJ9kr2JFxo6mrQkEgQJGflvqZ1Z09xsIN0ZU6O7r497VEwMETkg5dUVIbDW823pNxqbB1fnRSY4csSG8JvbIh731JL4czxID-1CsA_sw-Nrzlx7GUFugRrGs1rkDLq9VwREpEksO2TvjnUQw7ibntfxFGs167_w6JjoE7ZFKf72n3byehjUnvs2DiOgM_XslnRu3uRGML-3mxtvN65abI3em8gz6T3VVYgr5G5RTidtDFw46izm2_xS3UpUCr_ogT2j6qsKPnz65RSdUTA2KbQZbjetqZosvwJQ241nSVhRNkfrZAKr8nsaJSE931_536U8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=pABTumjlXpsFqnvM1gJ9kr2JFxo6mrQkEgQJGflvqZ1Z09xsIN0ZU6O7r497VEwMETkg5dUVIbDW823pNxqbB1fnRSY4csSG8JvbIh731JL4czxID-1CsA_sw-Nrzlx7GUFugRrGs1rkDLq9VwREpEksO2TvjnUQw7ibntfxFGs167_w6JjoE7ZFKf72n3byehjUnvs2DiOgM_XslnRu3uRGML-3mxtvN65abI3em8gz6T3VVYgr5G5RTidtDFw46izm2_xS3UpUCr_ogT2j6qsKPnz65RSdUTA2KbQZbjetqZosvwJQ241nSVhRNkfrZAKr8nsaJSE931_536U8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
سرگرمی برادر لامین‌یامال با نیکو ویلیامز در جشن قهرمانی اسپانیا بعد فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101455" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101454">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=cg4x7QiQsbU5ZNP1o6UzNyC-3OeIrTYZR4D0z_w9pLsQqcvXsMt3wJENNSR_2Onjy4VjipUGM2zT9xQTprp93bQHZ4rKxdMjLBFR2dIM2dzfX4yJlbd90BLkxfcTNbQHHc4khBPwghn5minTzotPM4X9WlaKJkjyaunjeMU-RMKuUo1EsGsqltcPf70hVp7TdOkgsmbdGaJB5lEVLOhZfYzCmROrpQysAB-qqprKpWOsAaN7NKcMrojAMVpenbG46X9jj5cgIjwIipigX5usCQ3kMX4GAJuULKE7cqWfZWSIbxquE36hnr5vIWVDyfewQZPKCLt3RqTuhxtSQmUHTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=cg4x7QiQsbU5ZNP1o6UzNyC-3OeIrTYZR4D0z_w9pLsQqcvXsMt3wJENNSR_2Onjy4VjipUGM2zT9xQTprp93bQHZ4rKxdMjLBFR2dIM2dzfX4yJlbd90BLkxfcTNbQHHc4khBPwghn5minTzotPM4X9WlaKJkjyaunjeMU-RMKuUo1EsGsqltcPf70hVp7TdOkgsmbdGaJB5lEVLOhZfYzCmROrpQysAB-qqprKpWOsAaN7NKcMrojAMVpenbG46X9jj5cgIjwIipigX5usCQ3kMX4GAJuULKE7cqWfZWSIbxquE36hnr5vIWVDyfewQZPKCLt3RqTuhxtSQmUHTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی‌کریمی بازیکن سابق استقلال: استراماچونی در حق ما استقلالی‌ها ظلم کرد. نباید تیم را ول می‌کرد و ناگهانی از تیم جدا می‌شد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101454" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFCG6Rq6nSAuPypwT7GBC8ye_4xeWvPSlyhQGOhtrqf0SzzxlIphZeT0xaos3vjcH-sIw5Q3-b2M7d9rJyT2PSsg7zkLszv_WviL43HiBUVmb7RDiDNWeD-xKJAzHW5IvlIX3oFYokb12TkHxuZRvufcOt9UMPPJvLTTDcXi9y_yfMIIVY_a7iCImKVTSVdoL9Px925UNj4NsfpzmgSZ4Iv0DdyD0-FsJk8q9B69bUPxEmEVwzhGjmtEJIYli0aA6gNgqft5WedysFCLer7sBvn-QAYKXpRSQD3j2bphbT5whBURxXbi0O06SgI-u1AbbGahXwRa8M6w2ac8eivGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بند فسخ قرارداد آیمریک‌لاپورت با بیلبائو ۱۵ میلیون یورو است و اگر بارسا برای جذب وی اقدام کند، به راحتی موفق به امضای قرارداد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101453" target="_blank">📅 16:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Wg_XBjcSnlhSwLB0b4rDOQZ2AO8SLDSjWxSPV9pVG4kUstdwBTJwxT5bJUETmFL7YJtJMCC8z4KJ1dq98qFJlmzonUMCmA0j2Qv1-HMykNrxPszA5OdMRzfeQK-Se8SpYKenj9lLzFCqnqCKP3hjWfNCa5EzUmpgwzakUkjp8faHWaWrAhkn-MfoTGirqLiWZVedd0SSc6rXJejuNxB-Av9DvOMr0mZXtN6yDbO43jBacnD4Qj4kmj_8lAkA9-lrPKYQJs-fmMKPbrsjAQwzVR9rdZItH4lxorSj0JA0mQG3lJP2WgJTJe8ZtTPOXAuk16g1Qtkec7N7dmSpE2k1uDI1Uudgsc9Ocf5KY5XyGywTV4hIMcqecjyzXtSVnSHpO0IOMMPGutRRJvHjxH53fn6P-KOROSu4kE9r819gjNG7_NEUFDJQVLka2IGQ6mzXj2h9iO_2H-bCp6v10UhzXfr8SREzwsFMSuhENLJMiCn0N2keSvupQHZ6S_BS-vpajcwE_V35sgTdJHwe21MWTAIf2jksGL8-YVoZZ9SrsWSxcYWJ_XS183a89Gn2OEoWBWww-BclRQ2XI7VgcTbyXizVe3owzfO9ljQzA8RTkrlDbjImvIEyy41dkUDL16zLELwBpUwfIt66EySJoh34wjEtxYjYvgfjkZ_I3iWVWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Wg_XBjcSnlhSwLB0b4rDOQZ2AO8SLDSjWxSPV9pVG4kUstdwBTJwxT5bJUETmFL7YJtJMCC8z4KJ1dq98qFJlmzonUMCmA0j2Qv1-HMykNrxPszA5OdMRzfeQK-Se8SpYKenj9lLzFCqnqCKP3hjWfNCa5EzUmpgwzakUkjp8faHWaWrAhkn-MfoTGirqLiWZVedd0SSc6rXJejuNxB-Av9DvOMr0mZXtN6yDbO43jBacnD4Qj4kmj_8lAkA9-lrPKYQJs-fmMKPbrsjAQwzVR9rdZItH4lxorSj0JA0mQG3lJP2WgJTJe8ZtTPOXAuk16g1Qtkec7N7dmSpE2k1uDI1Uudgsc9Ocf5KY5XyGywTV4hIMcqecjyzXtSVnSHpO0IOMMPGutRRJvHjxH53fn6P-KOROSu4kE9r819gjNG7_NEUFDJQVLka2IGQ6mzXj2h9iO_2H-bCp6v10UhzXfr8SREzwsFMSuhENLJMiCn0N2keSvupQHZ6S_BS-vpajcwE_V35sgTdJHwe21MWTAIf2jksGL8-YVoZZ9SrsWSxcYWJ_XS183a89Gn2OEoWBWww-BclRQ2XI7VgcTbyXizVe3owzfO9ljQzA8RTkrlDbjImvIEyy41dkUDL16zLELwBpUwfIt66EySJoh34wjEtxYjYvgfjkZ_I3iWVWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ایمان صفا بازیگر سینما: با کری خوانی‌ام دل خیلی از استقلالی‌ها رو شکوندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101452" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101451">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101451" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101450">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIL7gNGbDwzmImp7suZtqYlRlko1REKrZ2qexoMTVQZf_jtgegF3H9_WeawGXeOA4zd5QZ7BtosYxbygHVjWQIWjwYcsJTNr6a8M_3-Bdr2_wWEdVZTWkIjqNgXkMaAluCEJtNQIJN91S9c4N2-qCHtCR6v8NEPPfgo7y7Pv_1SaPsib7_8_iGS7T3pf4BMUl73NOMoEiTQUzF5PvVciI_jKxNS-omFtmk9N_o1k8cS7iVXwbA1gicipYaIX6UEXj-x0scf01cC1TFsskzlSz8bjhpPmv91YZ-f3XZcg2mIWKs4yx7UNPBoBlIdi6cMfr3dYS7nXGj852n57h894rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101450" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101448">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=BwrFby8CsjapsrwkAuY2nrVFRjutI1tgw5yzjMGjn5EsrhAm3T9FqKEo8kbUAZdF2gRSkKjZJRxHSWmEEUNMHhR7EhfBHTDEyvj_ujjdFKQA0S3yL-6di4BaHutC1Sui-yckc6-6AAnGW9Ujm8Bc_Se6-0OWVdqFZ04iRl3pPUH3UQ5QaPLT5cgBFCirOUeOBYCiiZkXmyOubrsfetnd-cQeo43aEVZKJFquWLOaVUvC8f-TXDSycgCsXQRXayLP0Luhl1SN3KnBkOlOYwMoM5xMHtbtkOxlbyoWTE7_MAM2YL-YrjCc7VXg3ekFRzxpoGpP2p3PzfZZ9mRbh-Tzjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=BwrFby8CsjapsrwkAuY2nrVFRjutI1tgw5yzjMGjn5EsrhAm3T9FqKEo8kbUAZdF2gRSkKjZJRxHSWmEEUNMHhR7EhfBHTDEyvj_ujjdFKQA0S3yL-6di4BaHutC1Sui-yckc6-6AAnGW9Ujm8Bc_Se6-0OWVdqFZ04iRl3pPUH3UQ5QaPLT5cgBFCirOUeOBYCiiZkXmyOubrsfetnd-cQeo43aEVZKJFquWLOaVUvC8f-TXDSycgCsXQRXayLP0Luhl1SN3KnBkOlOYwMoM5xMHtbtkOxlbyoWTE7_MAM2YL-YrjCc7VXg3ekFRzxpoGpP2p3PzfZZ9mRbh-Tzjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
خاطره علی کریمی بازیکن سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101448" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53a9000335.mp4?token=Gd1KFX4R-pBIKVvzS3NgPWQOGzKiVdFHT23_6Enxir_WjbEXkTyG1s4W45ocB68pHvclchc_1f5Z4misLPtU8-9dEGj6-SaFOJwyZcb166CDtSHsZtKQfUF7E02PfR3NxAfURVDa3m1tjdFbUMs2yQv_oA2tOVGTr0C50K94DXwbDFwUDd-ZAdglmjSZKCEj6woiuFjCG19as6yumr6jnch3biJfZJuFXv7mg_JxuHdva5o4jFB1ThXCKPJmYRU-jaAs24DnYkjAY0qPupT9GH8tZuYTcqxoI2MzVAJ9uKkFDDNcJh_Tmby4o_kwmu2UnVLOgqwH6x830MJAmqSi6I6QxeFowWluH3BDPB4bQQImpy_EEeMZt8Iey0FHM537pmK5rwASxuPTJg-rv_fOzyCxfxDSwlttNWkJbhDeSNmJs9xQVR5az69W2d4PjT5crMiPcWUJ8ba3PSZ0FAr0kL4xkKArJePgBr-cObrenETI_I5c4nSwHMEi0Q2_SXHHvfr6aJ-qKZwhpDyjHxW3jrSERT_A3olqO_sFb3UgG95j5Kd2XUhodPuxrxemltIIYofuFeoV7_Q7EdxyB5Bd6s1qesx0WDsrpZ-1k1yAex_wtwo-G824pKoGFL8aoTyw6D9u_Avxvujzh6bakLWzUU8fQg3-PXYodeMGDgt9vzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53a9000335.mp4?token=Gd1KFX4R-pBIKVvzS3NgPWQOGzKiVdFHT23_6Enxir_WjbEXkTyG1s4W45ocB68pHvclchc_1f5Z4misLPtU8-9dEGj6-SaFOJwyZcb166CDtSHsZtKQfUF7E02PfR3NxAfURVDa3m1tjdFbUMs2yQv_oA2tOVGTr0C50K94DXwbDFwUDd-ZAdglmjSZKCEj6woiuFjCG19as6yumr6jnch3biJfZJuFXv7mg_JxuHdva5o4jFB1ThXCKPJmYRU-jaAs24DnYkjAY0qPupT9GH8tZuYTcqxoI2MzVAJ9uKkFDDNcJh_Tmby4o_kwmu2UnVLOgqwH6x830MJAmqSi6I6QxeFowWluH3BDPB4bQQImpy_EEeMZt8Iey0FHM537pmK5rwASxuPTJg-rv_fOzyCxfxDSwlttNWkJbhDeSNmJs9xQVR5az69W2d4PjT5crMiPcWUJ8ba3PSZ0FAr0kL4xkKArJePgBr-cObrenETI_I5c4nSwHMEi0Q2_SXHHvfr6aJ-qKZwhpDyjHxW3jrSERT_A3olqO_sFb3UgG95j5Kd2XUhodPuxrxemltIIYofuFeoV7_Q7EdxyB5Bd6s1qesx0WDsrpZ-1k1yAex_wtwo-G824pKoGFL8aoTyw6D9u_Avxvujzh6bakLWzUU8fQg3-PXYodeMGDgt9vzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا جهانبخش: در مکزیک زیاد بهمون بد نگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101447" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
محبوبیت خریدنی نیست...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101446" target="_blank">📅 15:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101445">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_YeiiLTyWmaH4X-4Pp40TK58SvpC1FwYmasRiL5vky26KBl1VHSRAZgoWJc4Iqn76iFh0Malplc4jxOSJE7V7kWgpZNAhCbRKn0-HnGPa2g_Au64Jo4f4AuyXtUDVggmOyCDLuJgYTu5athBfloyKWLwPxhpVHAsx_GhsdULAqgsQyfZzftQS_gnULgNJ4c8_ZBzW6LmHR1NJCRhJdlVhtN1Wk1kxnatV5QDpG4QTIVffGwkdege6sQluIvcR7gDFoMc_oNZn6MhEUqZEy5os-4lOHqzIWx0fsR2WssppZDWiEpSuTupAxtCioYLrKSN6qP0P_Kak3Y1R6ZcB8xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
تعطیلات تابستانی رافینیا و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101445" target="_blank">📅 14:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101444">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hag7ki8B7t2PcGfpUqBZEPw0VwcwqlTlF-5lZUEqtoJGyqVAYAe9JgnLhDUZ5n4OkL0REOS0aa4_qgptFdEyI30e4sZTdSIKLwGs98vRnAv9_ykjKjqp1e9pMqRQUrhziZV_XxdkZbCUuD3a48pEIBm6_Hq4x5htGQvjbXuMqwZBqTUW0dTtOcVFfSDZMvpYaNRpXA48EY5H7UADXYBrlcrVNSFS3Cu-5a4h8oWN_ua_O8CW_gV6aTw8jM7AW5IjFde_7v-EoE6KXqD7Z4fjczRNt-NOTLzI_huNpRG20HGNeMGba5KjzJhL5hfunxfr0Y2qXbBfQ9q50jte8rH8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
علیرضا کوشکی دقایقی‌پیش قرارداد خود را با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101444" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101443">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=B8M6Bf6QyO22vL3GZpiScB0GU_S-i2y5C3J4hD1oigH0xAYWtoYHLURYNymH1nPGuKYRBjHBAt0mlPMTHGiulYcw3vdrI_ndWWv2IZg0l6uD3-_FYsErqv7xb5PSD6CPJHX7ruNJZ9JXu3ABc93zrjVU5N_pOVFBnlRUIn1756hTctmoxMGlPfsnWMe9QCkMlO7NSpc8HRglLaS4huNmf4Yf0SaRqk_D1ASX6rKFIwcJH0gx7H1HpYCdFbRjukq9fselPeuTagfS3scjvuBqQ4ie7pdNWvg8ufXoagQtLepaneFiO7PeZlouIz0WtI90eY8QowXJNgKrACagWuU85g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=B8M6Bf6QyO22vL3GZpiScB0GU_S-i2y5C3J4hD1oigH0xAYWtoYHLURYNymH1nPGuKYRBjHBAt0mlPMTHGiulYcw3vdrI_ndWWv2IZg0l6uD3-_FYsErqv7xb5PSD6CPJHX7ruNJZ9JXu3ABc93zrjVU5N_pOVFBnlRUIn1756hTctmoxMGlPfsnWMe9QCkMlO7NSpc8HRglLaS4huNmf4Yf0SaRqk_D1ASX6rKFIwcJH0gx7H1HpYCdFbRjukq9fselPeuTagfS3scjvuBqQ4ie7pdNWvg8ufXoagQtLepaneFiO7PeZlouIz0WtI90eY8QowXJNgKrACagWuU85g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عکس یامال روی پهپاد انتحاری شاهد قبل از شلیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101443" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101442">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD6oYlT3Nm_lBiTb6btSHhjodKvsPH81tp089KsqiccI9hDIPn5GlgGqYcHWmlZnSB4fxhqrNIV-CVmH90GdWq4zJMOL0r5YmG4P22J9n3R0VZgcpHOfM4entr2hHY98sNplSxitIjE7ukpErU9dsY3gGx9USPlE7kM2zhR0TmPse4S4vSPm7kXCpMcueaRdOxsHXd6XDqvZRopp1Rb_Dyg-H50EchSvIGuY9EvMO4yq3VHe3b9B768yRlWXvPqePzlBC_E7rD1Su8qnGmfdb9kjnviokLDHe2F45A6cN8An9t43BmM-FIiSNtwxW0NCkgbLr9c-VKrypIwaqLquUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رامین‌رضاییان با انتشار این استوری تقریبا جدایی خودش از استقلال رو اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101442" target="_blank">📅 14:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101441">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eouL5Z5Ji27Gig83aBAXLqQlDbOp6aX9g_GBsmtoHx7x5cWxj46B35nC043M9pSANAHb5CAsRYoqzPdY32MfyfafYAgJyk1BycTw1IW1V5Pdm3-77MLHf3oQzhEVEfz_Zl9h_AmjPUp4RoEhyhkvh0vTfd3OW4zJV0Ku1ieoImgpc-VNIOMQWRFY3lnAw3gpWYg2BHj_AfaVLfRCvpwhHTJJDPLl8cUCcs4dRv9Fkk1N7Crih4dDzdTRbHxfbu4Ql9s27vplSH9-G5CZVe00fvLa13UAUdP5nkP54NLtmNyvX3e_KdoHpP7cLYyXXZ2wFbKOaQf6QW2PS2GBszq0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🔥
لیگ‌های بزرگ اروپایی چه زمانی آغاز می‌شوند؟
🏴󠁧󠁢󠁥󠁮󠁧󠁿
[31] روز تا بازگشت لیگ برتر انگلیس باقی مانده است.
🇪🇸
[25] روز تا بازگشت لیگ اسپانیا باقی مانده است.
🇫🇷
[33] روز تا بازگشت لیگ فرانسه باقی مانده است.
🇩🇪
[38] روز تا بازگشت بوندسلیگا آلمان باقی مانده است.
🇮🇹
[33] روز تا بازگشت سری آ ایتالیا باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101441" target="_blank">📅 14:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=CAMNrIBEL9bVxfqy7D8a4X4fd-9N7bQcu9cxOF61VvBV3fjhATgYL4ZNpud_RA3DMAc8CEzaaRjHMh98KWYOtmC66M-Y6U0LeOwjlkFoaHQ8hhKn6zcqqIev3g_bwQnqoc1xBdo7XqaOAqc409-t_kLzXtW35DL5R42R98WWaV90dYRJdy3T-ThmVPYTulWovUdwgflT3N8AALqhgiGj7AQQ1NTufJX8pBY-wHyYESCPEoAqOxrtfQq72djk6VMQuUzvQZBO3TsHROcCN25UG_OHJS3Hep1pBiHrRxM0eFeutTbBCBw-gAu5SwyM8Wvs3rvB3djQBXJuHbyC6YImnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=CAMNrIBEL9bVxfqy7D8a4X4fd-9N7bQcu9cxOF61VvBV3fjhATgYL4ZNpud_RA3DMAc8CEzaaRjHMh98KWYOtmC66M-Y6U0LeOwjlkFoaHQ8hhKn6zcqqIev3g_bwQnqoc1xBdo7XqaOAqc409-t_kLzXtW35DL5R42R98WWaV90dYRJdy3T-ThmVPYTulWovUdwgflT3N8AALqhgiGj7AQQ1NTufJX8pBY-wHyYESCPEoAqOxrtfQq72djk6VMQuUzvQZBO3TsHROcCN25UG_OHJS3Hep1pBiHrRxM0eFeutTbBCBw-gAu5SwyM8Wvs3rvB3djQBXJuHbyC6YImnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا در مراسم استقبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101440" target="_blank">📅 14:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101439" target="_blank">📅 13:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101438">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e455125710.mp4?token=srurpYpFxij1ZDcAdXRD2QFW8i9HDVVMJanSUKfC9iumg8sMiXzzEnZd4TG4-PMt3e96YOYpwavzUUExrvewHFXsNSQDsFGSvZzEPknjNGeTpjNLGXftREOMTqeUx3EYv8y8gmfYwE0j8Gip6VQUcg5_93szuQly_zZMsl02-3KyWlfz0eW8BTQY1bB3hUOaJ8Uemaz8EvOVglphnsaV_296FM95uq-2UAlW5uSjC5t0VCbj2FhaOu3Ei8mJw9RSg01MUjgTld_D9Si1MS-p4HHfLfmWA9AhbgDrLEmZ6PNKG-FiNr1Yk9q22JCAQp3HnaeDk3AEZV-A4H2rJYEnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e455125710.mp4?token=srurpYpFxij1ZDcAdXRD2QFW8i9HDVVMJanSUKfC9iumg8sMiXzzEnZd4TG4-PMt3e96YOYpwavzUUExrvewHFXsNSQDsFGSvZzEPknjNGeTpjNLGXftREOMTqeUx3EYv8y8gmfYwE0j8Gip6VQUcg5_93szuQly_zZMsl02-3KyWlfz0eW8BTQY1bB3hUOaJ8Uemaz8EvOVglphnsaV_296FM95uq-2UAlW5uSjC5t0VCbj2FhaOu3Ei8mJw9RSg01MUjgTld_D9Si1MS-p4HHfLfmWA9AhbgDrLEmZ6PNKG-FiNr1Yk9q22JCAQp3HnaeDk3AEZV-A4H2rJYEnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
دیس فوق سنگین ابوطالب به قلعه نویی: ما تو غار کنار عادل فردوسی‌پور هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101438" target="_blank">📅 13:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7wpS2OZL6i2F0a0rfSOnjmHDXz6ZRHxYIkxEkVKOxMhGtngEm9eumt6RN91AAD4ikPB_Q_KNczWE1am24UjrfN4a1iW4DPV8dMUaBTP9zbEGeWp0ey8m0MqokPVBgpI-jkkxngRR3bPOi1GwNjtRbT0yHxrOrDvNN-V9Kwasfjwxy6OKrOFkRBasTbZqH3sm6EO0j9DGUl3RpFfapWpqSMuc770YpO6tUqt3oejTOwlyPF5xX9Fxw-PdU3jl2D_h_KCaNhWWhEYyGGc-OZux9yttV12jpFDqe1hCg2EwDcJHVIBfB3oza6wldwpOf9NNPjcy0mus-kyrimlqI8TfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101437" target="_blank">📅 13:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b01qnqpWiSJtGe76zuSFxho60ebc_nIlXhWIjxd_nJbgBMCSQRZAIgUik5NBuN98xkbMr8IEd-28p6ZiLYzd43Oys7zItVN4wfNgLxuLEvdIT4cT-C75fImpDeRv_6gDRIsKV5H-dl7_JZbpMWXz2la_kkH_aZy93vHUOJ1cj09KVneQbThACrmOSiNpqwVcbUCFW3xhwnvZnM4KZvV5SZawC-MZHgw6EQnESuzbXD40Bn7tKTmEgUYSQgy8n0r5tXwK-QEuvD5Xl9VuoZ5shbYaqnQPcm9cxKUpQ_FDYf__yZMsmxQnhvgeaQLRs7pVQIJ4_i6sdPU8oFmYkwyMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
جسی‌بسو بازیکن جوان تیم کلوب‌ بروژ بلژیک به باشگاه بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101436" target="_blank">📅 13:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101435">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101435" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101434">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2juIKFHLZTtwZwKT9ha_U8bgEXvAXnTf6GhElcSnwLyCDqACOsxLtn1MLa7uqZ14Ph9IP9_jOPVWkVQ_-jsOZV80yWJGVMC8MiHMq81Kd39IqbmzCg7ti6Ov0jqmIjdqFR4C3JJ3ydCdLAN_RSav_5O3WSdRBS3fCpQs10vqPyz5KQdRHo8ndT63ahcufiD_e1P9k4Ejf2DNRDWTtin-6AsaiheVWBHaRStloZoGOVI5Sp71qs7Q2R-BQ47iC1uLVevV3hQPssNdCgTjwDAL-olqzF0gQtlPV7fCPdDs5ZSzX-f7_SuqGhOi83vw7aq-KvT3OxELK_t6MorlRt4IGhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2juIKFHLZTtwZwKT9ha_U8bgEXvAXnTf6GhElcSnwLyCDqACOsxLtn1MLa7uqZ14Ph9IP9_jOPVWkVQ_-jsOZV80yWJGVMC8MiHMq81Kd39IqbmzCg7ti6Ov0jqmIjdqFR4C3JJ3ydCdLAN_RSav_5O3WSdRBS3fCpQs10vqPyz5KQdRHo8ndT63ahcufiD_e1P9k4Ejf2DNRDWTtin-6AsaiheVWBHaRStloZoGOVI5Sp71qs7Q2R-BQ47iC1uLVevV3hQPssNdCgTjwDAL-olqzF0gQtlPV7fCPdDs5ZSzX-f7_SuqGhOi83vw7aq-KvT3OxELK_t6MorlRt4IGhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🔵
باشگاه استقلال با انتشار این ویدیو نوشت: برای بعدی آماده‌اید؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101434" target="_blank">📅 13:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101433">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8rJE5AzDhndZeZsdo3Zcps67huw-S_idOX0pknW8fO5qgHFkWKpA7JDaPbUq3bIQn7cLlG9V-2QA21zoJMJYR7D62ZodnRvvJOQRn0VWRR3nDzqRwFrLwE--8yKnfIXyJgXtB7QLr6g8IA1WFVnRL1hFnXZ6v8ukdt5N4l2afmcRTJbLLr__jsC2bu48lgnqlvbSQhnSjhNUTEScaCTaFB8KchhMdgPm8g32VGVce1YNTQuRrhn_YATGDEgeAWJLs_1C5rTUT69RqZ-slTV6W_AWBWuG_SxoZ8f7t53V4I1sk7YB_PZ5um_0O1bSe7LPrjXZimX4gAdaLqR4b5NQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🚨
نشریه(L’Équipe): رئال‌مادرید بدنبال عقد قرارداد با فران‌تورس ستاره بارسا رفته
کاملا جدی این خبر رو زده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101433" target="_blank">📅 13:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101432">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=LfC_jrK7efy3tOx1p9JZLm_NTJL-jCOZKlznUOlrhx91KZmR2ekkvq25yWEEqtL0E2D4VypRvpKbxtyQfw4J6gm7XUuQuuZw2j4l6yxHvbItsMQfzKzlLGeSJFwKQ1rznvA4eRtwolHEo0-QRDB_Nf600ZZNOjA4tvKM74F6-H4WvlEHmUuEq1ZC-1oxohjiCm53L5qoFZ8qMvt-TD-0vwsdShYk6zBQg81Kaf-sKQNubVrXSiyishF8u4e6vSm9V65AN0KOODaBv1ZhUy8dKvk08FslqoOvteoZN7fVS0Z-FFRKmxSeWSMFkg6BDJ6GMS46E3Qpqy_URlKIDPXjKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=LfC_jrK7efy3tOx1p9JZLm_NTJL-jCOZKlznUOlrhx91KZmR2ekkvq25yWEEqtL0E2D4VypRvpKbxtyQfw4J6gm7XUuQuuZw2j4l6yxHvbItsMQfzKzlLGeSJFwKQ1rznvA4eRtwolHEo0-QRDB_Nf600ZZNOjA4tvKM74F6-H4WvlEHmUuEq1ZC-1oxohjiCm53L5qoFZ8qMvt-TD-0vwsdShYk6zBQg81Kaf-sKQNubVrXSiyishF8u4e6vSm9V65AN0KOODaBv1ZhUy8dKvk08FslqoOvteoZN7fVS0Z-FFRKmxSeWSMFkg6BDJ6GMS46E3Qpqy_URlKIDPXjKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه نیکبخت‌واحدی به ممدحسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101432" target="_blank">📅 13:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101431">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=ESHoVIKt3QWZj8XLEL4fXzGsTSwxwH7blDTQfDwqSK-v3tGOxJjijz-FPXO4y544kI2qp8HXYEv4Tb7WhsC2AhOrAGsFwBG9QCV9sSsSqQwziOrsLB7gvb-vJC40PDzgAgWUCH62kbsCKoYcEYyTpF3ahmxhK2xvBa-y31KkxSx0o3VwgnlWmk4Y7MJ5x0RmEje1fBSy2zZOBhZPKHj_B_WQ55xepCwflXRh0HOmTbwuNQjtEKzadlrU7VDHX_1YPGA-VqE200RPILkfkvlmqRIf9inoA19iH1X1A-pYhplUVDnljq8nnchnlmecbgMyawwT2xQWmtImsfsZ1zSPAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=ESHoVIKt3QWZj8XLEL4fXzGsTSwxwH7blDTQfDwqSK-v3tGOxJjijz-FPXO4y544kI2qp8HXYEv4Tb7WhsC2AhOrAGsFwBG9QCV9sSsSqQwziOrsLB7gvb-vJC40PDzgAgWUCH62kbsCKoYcEYyTpF3ahmxhK2xvBa-y31KkxSx0o3VwgnlWmk4Y7MJ5x0RmEje1fBSy2zZOBhZPKHj_B_WQ55xepCwflXRh0HOmTbwuNQjtEKzadlrU7VDHX_1YPGA-VqE200RPILkfkvlmqRIf9inoA19iH1X1A-pYhplUVDnljq8nnchnlmecbgMyawwT2xQWmtImsfsZ1zSPAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
داغ‌عشق پرنسس لئونور به گاوی دیروز تازه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101431" target="_blank">📅 12:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101430">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=uC9mfc1wkSnTpEu90ZSAo-4Si046-kpYnpRsuw04Mjtd1weA3AD3omRN4cB8Dn4buT9rGse66j6yt1FaK0EiUUwZMVcSR0stDIvcsK1TT_SnJS3-04oIZlJJFutKwys4twMS9wvaY34ATeJlOmbkt_4AYJ8eOmgb6K3Id8TbisAFJX9tULS1taNFkarpXEIOVMO-DNbgmnh7bXQ9WOcvZGLaM9wbu-bJrJ2DJvO_S39kGFGUtcuZUNHnnKhkUVODpS0TQGcwEMxmki5J1L0o1P6io_ZTqmEf9Jt0rci94rASw0xtdt4LI77GHQcZbMsUwiDO0HCJ_oAYcVK_YgMIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=uC9mfc1wkSnTpEu90ZSAo-4Si046-kpYnpRsuw04Mjtd1weA3AD3omRN4cB8Dn4buT9rGse66j6yt1FaK0EiUUwZMVcSR0stDIvcsK1TT_SnJS3-04oIZlJJFutKwys4twMS9wvaY34ATeJlOmbkt_4AYJ8eOmgb6K3Id8TbisAFJX9tULS1taNFkarpXEIOVMO-DNbgmnh7bXQ9WOcvZGLaM9wbu-bJrJ2DJvO_S39kGFGUtcuZUNHnnKhkUVODpS0TQGcwEMxmki5J1L0o1P6io_ZTqmEf9Jt0rci94rASw0xtdt4LI77GHQcZbMsUwiDO0HCJ_oAYcVK_YgMIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇦🇷
استقبال مردم آرژانتین از اعضای تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101430" target="_blank">📅 12:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101429">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=NFL2bOO4kKRXRWGmNIE9QvZYVQtTmt8f8VsFcO7uSuEol4tBuOEFXoNxAQCs6EnUxvsVqk-5UyZhrArc-JQ7kblmsXd6hUnBvyFbMboWJp0ZmaOBwkpezaVvDWBSNbnA6-y1H1t4yK8xZ9CedTpz6uTPE4TsXFkMl1ewALnvqpUObe0c0Smfc-Uuthd1mUqXSJRhRxVOeKSH9rdgg2FNTKoxo6o20VW6MqNEbXN4PxhpcLy9jQG6GqIpy5TwUZqQyk4cH9-p3pz0HHOCE8vFtW7B928y6pgGcOt7vfQSSRNmgnU3mqyGmU-XGGC3yGV9GgZnKprzm6q3ADWUgexAwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=NFL2bOO4kKRXRWGmNIE9QvZYVQtTmt8f8VsFcO7uSuEol4tBuOEFXoNxAQCs6EnUxvsVqk-5UyZhrArc-JQ7kblmsXd6hUnBvyFbMboWJp0ZmaOBwkpezaVvDWBSNbnA6-y1H1t4yK8xZ9CedTpz6uTPE4TsXFkMl1ewALnvqpUObe0c0Smfc-Uuthd1mUqXSJRhRxVOeKSH9rdgg2FNTKoxo6o20VW6MqNEbXN4PxhpcLy9jQG6GqIpy5TwUZqQyk4cH9-p3pz0HHOCE8vFtW7B928y6pgGcOt7vfQSSRNmgnU3mqyGmU-XGGC3yGV9GgZnKprzm6q3ADWUgexAwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور ترامپ در فینال جام جهانی، ورزشگاه را به یکی از امن‌ترین نقاط تبدیل کرد! از بالگردهای امنیتی و نیروهای ویژه تا تدابیر حفاظتی چندلایه؛ همه‌چیز برای حفاظت از ترامپ در بالاترین سطح آماده شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101429" target="_blank">📅 12:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101425">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/co-DkvzbSi9KWK-ZQknG6a5UHIQI0HNYlFbZlEFBYuzBNJ0HxNED3AUfO6-QjEmrpXuRL0yJDHyksx26D2AkSRLN_PhWoGzrMoUjYP5ZTR0ADuPSNrKS3mh2urJGUAlsQxuObpZlRQjObZeZtUgsAs0tHw-vKfsGb5qBci30CDsBC0VhoBX6QnZlAelWL0IxK3blcTtdg9t6BEQFIAMu52MWYWa7LbYSJmR_u7LjPyqEkFgJWA7Amq-f4ggESJkYB1xa538FHezwC-0aLLzvl7HGDP2Nl0x3__Y4_D0zOlHo9I2soc60xzT-2Mnzo5c9asR1EQZh9gncJbWmUPvI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfTeh8xssZa_5JIwUYX8sfGCVkn95cn-wQKEI1TH0sIfLUPBK0Qh-YFIybDFbOYNxmZv2ZfMy21JxONU7LyQscziPilL3h1wfp2vpDYYg32ftq1jXDFfOgUqw74hHtjH9lQKYndOnjFe1hGsdpeLWU_RzwvsyMb3XIbbL2-VO9-mEVi_cpy8avdrlh2Tp-GHWznvIQZtcoBpv3PPrYYMR1eNv-nVH1TTYn_xspSK0Hk6GQmPgasx7YcCLH0oGgfOfRG6eWRzLtNZq0fLZVT0suWSZxP3D_HOdp-3P0Np-HuJrHMOwVObcpDM4S6UkOsFB1ZBXvhQ9fgYx-y-KyEjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpYu8YF4UTIcDaMqTcvI7jJjS_VchmoFb2LqmMmRYQYIlh3WrZdJ5K-PPkTfxJEf2QIKte-P-B08ufIjBn5gjjlBWsfTnh7si0Sk6EMmKqKKOkYULm8MbQlG3AMu-xv_GdfxsAmecJ_DLKFTFcU7sslaT0rvz-CrKrVwernlD795U7ceTAe72_71Lc5iLve5uxbAfBm8e8iF_l0ujaHuVPddjXxt0tvHGp9BjT2C5wFcXfSgjEvsgJP4Sqfgd1qafssxY3-ystmP5qRrZYBNp-wSA-4wGcZOFOxvKjx3Om_OzA4oT0CLh8EfgViN0My6yW7D_J_u5po-WO1bUwp76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcKw5U-jYvB2IuHlxWq1WDNBdOzWi0NVY_tT4gQiK1f0u9aIe7lW6K1s3fQgSZqHsGoFyQjky8aRyrfKuzlqnD52T_pR68doYMglrerkZpgE9EZIQn9TWt-GIbDry0sT0rfca0rse006lQmR4vQI1NtFL-N9trP9p-YrCS9ODO7BIgDo_Yl9OQg4JcssJNeTT56nVbLLT2fixk8YrmDnOuZgHW7nukZJkkII5ESV0qd4sXCTxEKNHYqGckwTrXf9-tmsEZzBjuRY1tZ2htxT8c2ltXlrjRnXj4sZbwvqdcaK3yJbvYXgBcT1F-VOUFswHcPz2bmY6i2hxxGWhsmHRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رونمایی باشگاه‌میلان از کیت‌دومش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101425" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101424">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfPbzucTC6EWk_j21DEQMrrG2FmQ4irsRRTqDFBJ9HJCxVCx-m-ij442a1_s5q87juU3XJqi6oK8MA8gdO48TTQ5fSwbeJ4n2Gqgs_rDPWtCnDs5pT0Ja25L5yXiomUR661wi6z-1awR7oydY-nXVqAD6eO2AQTA2kaLlwzLM4nnordTDfaFeCdq_SocdL5fZo3L4QK0yg7zHkOIpekeSmz3UCtJ8jKcgNVPzL8FohELk6c9FwUJaSvqbUaVeOfDGsLaMGpEYQpxTPNHOl3svudyKFviAMNLqJXtm1yrvyszty2PzPw9XlH_aH8Nii1xWvgNf7s_yEReqpOAiyWBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
بهرام‌گودرزی مدافع چپ جوان آلومینیوم اراک با عقد قراردادی ۵ ساله به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101424" target="_blank">📅 11:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101420">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ddx1A0JIsAP5LtJmhAS3rGF-aEEoC0Vwbg_wiiHTQHh2Eb1AVCO9kVmylHJ5530H9F14yXK4CVgKIJq58UTK1drLfGiV2ZHlhfvOUdHkVH1-IEYX5lvGxAATyX8J9qFD-9PxSJmuUv5lS_MFN9P5tY0hntFdNnKdVcsQWKyr0v3_wtZEQK1Q8dowX0WkZb46qSLVaj33x2ICAYKgf0g6ugRr-Pn6LBusLXOHuD7IrWSrrfnslDU1j61bw3nCxrP434TVlz6efm6BPmbGjmrPOhas4FJwi2LfrLxJT5a9CSjohHY0Dng5ruELZv3NNxqQrtuqGMxyuaK0Oqa88sxyoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gG2FARAES4YQJCUeBlAfcscc5vkuEJP4fsqjjmb1rNR0DDAMR0NHtNU5p-tuKvgXcCgLxRpVKQTZ163UOKn2dFqgL7NoJRXbYXUnxSyAPtgxrGoQcnx663E_pKANshmff1zHK1B4F9FwSF1mZxYEMRAHI_JX8XGxQVBnnC87shECR24OQnyL_unWQ6T2A8A9jaJ2tb3Got823YbGmZZ2ud5NTrZv5tXNiW1rmznDaLM53kxGYwv4RpDYAhqafyvEzfO0LByt0C9rI2AHORUgWd_sEzY4cYyXvOn0EgcWb8PZHD8dQlBRU1feN5HimBuvzxqFO5i1dtxAzGK9jNXrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGsLTsol-q77C0kbafmi2yUnvqkxgfLKiwEw0WzdBf33kM2lJJLPR0L9zLK0z0aZ7IMcMxuGsz4JD6F8j5khLJZAv8HzChjjsA_b04yT2onpnIOExXF3FPZLiLrm90cXQCbZEYXbTysVHLXMkzdJyZx2dmeXL-DwcGacQhfs9EbN4NByfwGOM7MpONTOui-T5mwvL39FlICeY61sbu5G2ia-4HiZ76QkFtV58ZFnFaSiWwpgW6aIbUFtXlRLA2KwBK-EaFTe_YkmsWDT0pmfFxsLcLxRC5AMQChUbiZhEY2rVXzxnOGxe_sVlJUAPQW4mxBGulQoSuAfDKZEGrZmzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8fYHrtYVviBeGjJopBai7LbxG0f7FU9jZZxiSqmqRj3-0yBogThxVuY9oVHUS0gaFOXTqK9RRNxOh_1xti0jGbs22bQqAfGjwyauIwbKOu9HQElUpV4j6zdo9RiLqvPNmYZretvBfJgptli1a75NwyJ9oChNKwQii6haquDhKt6qLvYEm_JMlT_F1VbTBdO4tY_bJCJeCH-RlIACOGtqCL9QeeiFo1PuPWv9Uo1YdgUFNsiXuGoKuSfmqXoV8HQBmiGp8EfpjA5PD-hENvHpH_Gyi-k7x9_mOkmqlJIozyldUuWejITtSaNnNjXdULtvBwgvb3efflCUapjKB156A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
رونمایی باشگاه یوونتوس از کیت‌صورتی رنگ دوم خود در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101420" target="_blank">📅 11:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101419">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGstd0rXIiq5GDwMuHnrwWNlssqOAnCriiksb7q6zwLnKtrnj7K8-syMWMzwFf57p91ZGLz_S8DF-BVtJwFNwmSrsqns3HhAYPj8HxnDWaZDwT4EZnqiJuKwN2M9xCdKDFSyxitrHdE22Tw80Q7l_Ab2UiH8mjiHFcc76eOeJm71UakjfYJ5xyO2-FCE3v3s_I6tKtY255HuEi6xVpuMduXTJHJz06sig-CF3omAMRS7nHmYbXLwigtpJoyr81X3DiK3yHKHfC1qEmnowJNNoQcB4L9xlh6dHdKrgbzz91EdkA4BwOjsJLPqgbHtnKIrzB3F4pZk2icPEUb9LOqyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101419" target="_blank">📅 11:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101418">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1b98bea2.mp4?token=GL4E7V8GCJ8t-F25cJbIV_wO8mHFI3bR20ZbI2oGmFWMY_lDFTuMeQew9AOr2tJMl3YqWp6u6ujb6mAEEHqtbli60yi_MzF2t88INQF8ZYI9PXhop8OngofKbKLbiI1ieJGJJAlzRWkQT_NslyBuurTn3SFA9zZEdtU7V728prHrMoUAr0cX2G6n98NJDBxB3-WCOS1EP4qrDS_239ORl9ktCE2mrjJ6gg48IuhHENcpEYNuTIeqHAgp7XkMmJy5gQMqRADnD5v5YWHsY1rZdfJCK8RzconSVxIynfzypemiaNibmfjpjFDuDG_hybQtuw9VRTi8GDqltp8iP32RiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1b98bea2.mp4?token=GL4E7V8GCJ8t-F25cJbIV_wO8mHFI3bR20ZbI2oGmFWMY_lDFTuMeQew9AOr2tJMl3YqWp6u6ujb6mAEEHqtbli60yi_MzF2t88INQF8ZYI9PXhop8OngofKbKLbiI1ieJGJJAlzRWkQT_NslyBuurTn3SFA9zZEdtU7V728prHrMoUAr0cX2G6n98NJDBxB3-WCOS1EP4qrDS_239ORl9ktCE2mrjJ6gg48IuhHENcpEYNuTIeqHAgp7XkMmJy5gQMqRADnD5v5YWHsY1rZdfJCK8RzconSVxIynfzypemiaNibmfjpjFDuDG_hybQtuw9VRTi8GDqltp8iP32RiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پایان‌یک‌عصر طلایی از سه‌اسطوره تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101418" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101417">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c9a3d75e.mp4?token=HWkqN_knp1usw_HbXN_fdKbVbA4OgjVtdxBWQsgiX22YqyilGF9NA0rmZaeCGuM6FqKI7fUnbz5wxigLaslbGv3_6idNsR0DuvUhcrheeDf09RHXXUXMDO-C8pqeEQ8gFBR3xQCbyJgQaqUHMFKHiSrdSZeduMQJ5zgeZRus-h8QWdARNb6lAyUxJC_RWRqSZ0SeSsj36j8SQT7bYSR68Ba-io-pb4-tAOB8bso-8BYJgiedCaqOT1JYOGMqA-dlsAePy4poif23nr-jleDypyNK4q8poXha36bWiPzRGrGTS67KAcQ0VKnrAQ1X53iV2PAUc_tDkDXbupIDEFK2UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c9a3d75e.mp4?token=HWkqN_knp1usw_HbXN_fdKbVbA4OgjVtdxBWQsgiX22YqyilGF9NA0rmZaeCGuM6FqKI7fUnbz5wxigLaslbGv3_6idNsR0DuvUhcrheeDf09RHXXUXMDO-C8pqeEQ8gFBR3xQCbyJgQaqUHMFKHiSrdSZeduMQJ5zgeZRus-h8QWdARNb6lAyUxJC_RWRqSZ0SeSsj36j8SQT7bYSR68Ba-io-pb4-tAOB8bso-8BYJgiedCaqOT1JYOGMqA-dlsAePy4poif23nr-jleDypyNK4q8poXha36bWiPzRGrGTS67KAcQ0VKnrAQ1X53iV2PAUc_tDkDXbupIDEFK2UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تک‌تیرانداز‌های مت‌لایف برای تامین امنیت ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101417" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101416">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=mEfhQQy4Ocv-VO9ldXMD9DxOG3JQl2-OPCru-JI8eknmPyuE27n7_OUynpfhKJ5VFm8l_uC1RDb2EqOIcg2OkcEVPqkDBNf2EoeR4CNgjHJ77Yc-Mx4-0ufwfuN-B1Q9xVxOt6hviS0hymkLRoIW9GLMJO0eZJg79SmJ7dzxNTgH61ZSw3eErV19MctcAl_uEcMA9DFzY24k2iGR94aBK302yw7DjxuOLpi7RCDCEzT4ZJwJPf8OkRcEzrjZjTyoglzhzqUlaoBuv6Ulg1ilg_GmIMwnrUv3SG8RjLNoND_X6qZshSeF18jH4qkDSEP1Z8T_2ITAL5xmIg9QnIA8k4gu1gGfYK8LhppmehnEts2pm_JuhPSuwvCEToKI2XXn3UPbBCsViVWBiT7xJkQb1QwaZzbFSp5P7q3DpDKfpUF94FOV1F0F016sVvVb_UX91fDN5ptKMUyrdYY0Mn11SdeS3G_fjobMBQsXZcSuryHnI3ArRl_MkruWEfRqWXydU0n72VmHexCVqTVymgDguzMNkvUDOVUjEvqbWzzl1dtQ5Djc-6veBWF6FrB1CGQp5PlFyUQ5zYzVghrnpA0DgXRl3cYJusrLxQomxu5SHBCYP6evY_Q8pDDBn6Yg1VP20ZImosG0GBvq59zyYWyxEgmTZJ-9pKxZ98bnFufZVpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=mEfhQQy4Ocv-VO9ldXMD9DxOG3JQl2-OPCru-JI8eknmPyuE27n7_OUynpfhKJ5VFm8l_uC1RDb2EqOIcg2OkcEVPqkDBNf2EoeR4CNgjHJ77Yc-Mx4-0ufwfuN-B1Q9xVxOt6hviS0hymkLRoIW9GLMJO0eZJg79SmJ7dzxNTgH61ZSw3eErV19MctcAl_uEcMA9DFzY24k2iGR94aBK302yw7DjxuOLpi7RCDCEzT4ZJwJPf8OkRcEzrjZjTyoglzhzqUlaoBuv6Ulg1ilg_GmIMwnrUv3SG8RjLNoND_X6qZshSeF18jH4qkDSEP1Z8T_2ITAL5xmIg9QnIA8k4gu1gGfYK8LhppmehnEts2pm_JuhPSuwvCEToKI2XXn3UPbBCsViVWBiT7xJkQb1QwaZzbFSp5P7q3DpDKfpUF94FOV1F0F016sVvVb_UX91fDN5ptKMUyrdYY0Mn11SdeS3G_fjobMBQsXZcSuryHnI3ArRl_MkruWEfRqWXydU0n72VmHexCVqTVymgDguzMNkvUDOVUjEvqbWzzl1dtQ5Djc-6veBWF6FrB1CGQp5PlFyUQ5zYzVghrnpA0DgXRl3cYJusrLxQomxu5SHBCYP6evY_Q8pDDBn6Yg1VP20ZImosG0GBvq59zyYWyxEgmTZJ-9pKxZ98bnFufZVpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
پشمام بنگلادشی‌ها بعد باخت لیونل‌مسی اینجوری حالشون کیری شده و غش کردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101416" target="_blank">📅 11:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101415">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRMSkUF8ZyIzBOD7MhGqTv3aCsPL4kJ0Eb8qnHmcBU98a0zHHAIXi3BoUiaTLresBbFjdXJe7rGJxrF7rk7_2vo3TJnehXf4JujZI_4-YX_pdn6qU1GHSHwUqagzYbr8KbueQ6oRrGn8sMcRAGP5jEzSxjHqhQU-XIUlJwL5Dqu_jHq3U1QcROJhlIPV7ZD-RhUluua47yZ7iC0K2PrIRQTrHelcsrMi-09KujNIIVk-t9uoO8TU98kL1ze_hcvtrTkuyItap1HlUmXgPYK9yVY57mUwR3Y24rJMZSexgWCG-G5Efut5ZjkDbg9OgCLVz3xTxBtag5en3RjP2jYtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استقلال در فصل‌آینده لیگ‌نخبگان آسیا در سید اول و تراکتور در سید سوم قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101415" target="_blank">📅 10:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101414">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=u4OqcC96JBRvIwV32tbt1pzhJtlZuMwGBfL21Ul_4ekpjeMmfkz901_Fy0psmsdJidj8b9Pe-773t0C4KZSBLp57MOvN1H4W6or7XqnatzF5Bd50zbcESVAFdYPYWLsu7WZvct-02hhHOsEjAFgYpE--lN2OkXgQubRdaJZoDYev4TPHsBaClhbGjiCEZGizlXjSqecxCxJPRP4scWJ2G6AFO7rdx9_NK83GjhyuyuJa60OlpVVZ7hCBpUuGWYz7-iQqwZ0DVhZIWC0941MIuu08XkcmUC6WGKkrrcBtTzs-vQVF9M0nnNavK5Ez1_GE_x9jb9semd2aXFcrrsR0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=u4OqcC96JBRvIwV32tbt1pzhJtlZuMwGBfL21Ul_4ekpjeMmfkz901_Fy0psmsdJidj8b9Pe-773t0C4KZSBLp57MOvN1H4W6or7XqnatzF5Bd50zbcESVAFdYPYWLsu7WZvct-02hhHOsEjAFgYpE--lN2OkXgQubRdaJZoDYev4TPHsBaClhbGjiCEZGizlXjSqecxCxJPRP4scWJ2G6AFO7rdx9_NK83GjhyuyuJa60OlpVVZ7hCBpUuGWYz7-iQqwZ0DVhZIWC0941MIuu08XkcmUC6WGKkrrcBtTzs-vQVF9M0nnNavK5Ez1_GE_x9jb9semd2aXFcrrsR0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مراسم ختم مردم ایران برای لیونل‌مسی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101414" target="_blank">📅 10:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101413">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWbHOLMRAwi8CRkbLieaKySExNPqgWPFFY461VMjpa6Dal4_Pwk6_ez_QmCYXfY_x69QNsUO1LFx6ld9eeqofLm6dGfXyCFnJAGutcCuOjLFNaCuhUr4C0Ah2VwB7DhW07EvU3UOhaNSL_Ce0Dvju7e8vBbrFlbeV30LwuObhYh6W9K3xlFOgWLnIMPIExjh1LSarnlRJJipL0px3tBpDJcVmaEfJqtJP6UeCrB6qMCim8pQC7DQ6gMwt41c4QkCKW_lCXw23CQGnMIyJzgyw7bjPWz2wk6KDY3HAPBKploSeNGJ6B5ZJEQnMLeEWKXk_hwTGReT98EHHWbXKmg3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لوکا مودریچ در ماه اکتبر از فوتبال ملی خداحافظی خواهد کرد
بازی اسپانیا مقابل کرواسی آخرین بازی او خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101413" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101412">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=n7Kp-hYuc2cGyq75VCmDC-2tTw6-EiG29HTd4Xa9-O--LvKBY6b2aGau-1_U807XO9lPWkK4QLxma1vaMx1IimKQPWDR8JugQu9eCyucW_rt0ka4WX09KcGUCBKLt74_rAxkHkXXhfRfkQfMLSn5cLdjdLkW95uF7RwOH2hT2ja_0vzAiP1spkDHkzvUTaWjDsaemvbkPZiTGoF969l39OO_-eN1XaS5FOMDWwAkw4zdkpHfmKGhG4lgD1wduHCDiTrfuIBcf20fSiTDYA_hj1lHupTs4HeWFjTlTOZqB3VmYfbFCEAdCvS42kTO2jzY1WAiltwXkgO9x5ws4WRs9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=n7Kp-hYuc2cGyq75VCmDC-2tTw6-EiG29HTd4Xa9-O--LvKBY6b2aGau-1_U807XO9lPWkK4QLxma1vaMx1IimKQPWDR8JugQu9eCyucW_rt0ka4WX09KcGUCBKLt74_rAxkHkXXhfRfkQfMLSn5cLdjdLkW95uF7RwOH2hT2ja_0vzAiP1spkDHkzvUTaWjDsaemvbkPZiTGoF969l39OO_-eN1XaS5FOMDWwAkw4zdkpHfmKGhG4lgD1wduHCDiTrfuIBcf20fSiTDYA_hj1lHupTs4HeWFjTlTOZqB3VmYfbFCEAdCvS42kTO2jzY1WAiltwXkgO9x5ws4WRs9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
همزمانی شگفت‌انگیز عصر مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101412" target="_blank">📅 10:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101411">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=BzBiQoX0o6T2jogK6hQkD7JoLAzhLXdzJo9es4Rix-QYY0Pb7VM45y0u--9gQqZ4WY4ImiJ-rhv7929v1gE6UMxKakSRcARtHEDSu0O2VKqf8msnIH__pKUfR8ZR18WdizRWj7OiA4XtornNaU67eoByooN0O8_4IjkteKMWVtao4-ZF2CQJIu1NiwhPIg81ABPCxklVg_pQWY_lq5YK6J3DovRXLoVcbtI_XSPbTO0gSY8G7kQ7j8-Tc7V07apYvkwbdozP_WJ4i8NTJzW8218J-wh-qMtgw4vW0AL_1BHYP06AJrPMqkjqgww8_hauBdFWPUEu3rVmTE-8av5tqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=BzBiQoX0o6T2jogK6hQkD7JoLAzhLXdzJo9es4Rix-QYY0Pb7VM45y0u--9gQqZ4WY4ImiJ-rhv7929v1gE6UMxKakSRcARtHEDSu0O2VKqf8msnIH__pKUfR8ZR18WdizRWj7OiA4XtornNaU67eoByooN0O8_4IjkteKMWVtao4-ZF2CQJIu1NiwhPIg81ABPCxklVg_pQWY_lq5YK6J3DovRXLoVcbtI_XSPbTO0gSY8G7kQ7j8-Tc7V07apYvkwbdozP_WJ4i8NTJzW8218J-wh-qMtgw4vW0AL_1BHYP06AJrPMqkjqgww8_hauBdFWPUEu3rVmTE-8av5tqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
استقبال مقامات دولتی آرژانتین از تیم فوتبال این کشور در بدو ورود به بوئنس‌آیرس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101411" target="_blank">📅 10:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101410">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔥
▶️
اجرای زیبای شکیرا از این نمای دیدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101410" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101409">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
❌
⭕️
سروش‌رفیعی با انتشار ویدیویی رسما از تیم‌پرسپولیس جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101409" target="_blank">📅 09:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101408">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfpbb3tLd8Du1L6vdmFZiFqaBfK4rmBlm39hgmKN4NplWT5KEcdmOgEjd08h7rZyAdAf59x0D-FhctQpcmrqGuqQhx6KARSH3W0SbvWi5coSZk1O5bGIh07rAHLakNaiC0VLh-bBBmxqSUyvsDRIpg7__Fst6bteAHF_KC2qxf4fT9GruEzBHJmh981rxSfGviDEbO16yNnlvdrXDLHKlq48kxhXpS1_xoDWtgOOPxgaZfzDoyjaXSOTdFY_m_8Smptne6hM5V6XE-7oiJGRV9GQ9F8Fk22vNSQaCRnuvh3B44HwH81CwDHZakPw1-6ytSFevh6vVOAkjsZM0KvJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برندگان جایزه توپ‌طلا جام‌جهانی از سال ۲۰۰۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101408" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101407">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=fAHad0-HUOVOwegMn6YCKg9jPeTQ-uojQaCggqlxqZ6Fjok1JRKn1VfPdN_rIIuK-HCvcbTUsRxuMHPfS8ehtBxpc1_vUbrJ4V5BGrqJVIjmiyOK8EM6gl3giBPdJknkn1n6tZVIKfwgfAI2TpMWcfUpNxAj_JyTj3pMvYWDF2W9VYkTGkcTaS5pDgEVGHok_vsRgFhskwqH_6W2QfprNcuo4i1dNI3fPNsxrleN5DYw4mKz8FKrahRJnVcK5LKSqkSye-5xn7DJgqx4fbrA2RB4Q6JkDv7RuU2XthP88NWDKUDEx_1ttqLMBH8jpoCnKNqQ9Zar9_8y00I7_EQjCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=fAHad0-HUOVOwegMn6YCKg9jPeTQ-uojQaCggqlxqZ6Fjok1JRKn1VfPdN_rIIuK-HCvcbTUsRxuMHPfS8ehtBxpc1_vUbrJ4V5BGrqJVIjmiyOK8EM6gl3giBPdJknkn1n6tZVIKfwgfAI2TpMWcfUpNxAj_JyTj3pMvYWDF2W9VYkTGkcTaS5pDgEVGHok_vsRgFhskwqH_6W2QfprNcuo4i1dNI3fPNsxrleN5DYw4mKz8FKrahRJnVcK5LKSqkSye-5xn7DJgqx4fbrA2RB4Q6JkDv7RuU2XthP88NWDKUDEx_1ttqLMBH8jpoCnKNqQ9Zar9_8y00I7_EQjCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
بسیجی‌ها گله‌ای ضد مسی شدن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101407" target="_blank">📅 09:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101406">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33df2c440b.mp4?token=qbvt3OwsnGNWKk6wFPKO7T_y3Al96kVQNxSiTdAsk7N2ZR-BJkJexphQyomR4IXSHrO3kj0H3TlJueomxdD-T-2FAL9V7wYzRaJrb8uPBI7G-8d9XhHbf6nduFyjGoTKcmJnUy8q5jIq1AbegAZRj5So4xYjB1wXm1slWzxwzjdKKJUjooNClzqUsnrbaFEtfs7O6gTnAgJWqa4GM1kMmRY_PwsxKFRac6PCBxnFZ_gi_hBhGhYk_s_rPVe9iifRRIN7ZxtnT7OVmpiih4GSoG_-JxYjCfnCIyUoS9jt04-6G9U3jWsPqOLiSnhh-WYAkFCc5xfhNevxlhoI4QhQjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33df2c440b.mp4?token=qbvt3OwsnGNWKk6wFPKO7T_y3Al96kVQNxSiTdAsk7N2ZR-BJkJexphQyomR4IXSHrO3kj0H3TlJueomxdD-T-2FAL9V7wYzRaJrb8uPBI7G-8d9XhHbf6nduFyjGoTKcmJnUy8q5jIq1AbegAZRj5So4xYjB1wXm1slWzxwzjdKKJUjooNClzqUsnrbaFEtfs7O6gTnAgJWqa4GM1kMmRY_PwsxKFRac6PCBxnFZ_gi_hBhGhYk_s_rPVe9iifRRIN7ZxtnT7OVmpiih4GSoG_-JxYjCfnCIyUoS9jt04-6G9U3jWsPqOLiSnhh-WYAkFCc5xfhNevxlhoI4QhQjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال وسط این همه آدم تو جشن قهرمانی اسپانیا شرتشو کشیده پایین و میرقصه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101406" target="_blank">📅 07:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101405">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30588621a9.mp4?token=S-MsrCfpzPqlYH-G_LmEO1PcMo8uEUaNbXWcEkARY3hPugfKmWWdVbbHHqYAIeLBewiPF28HZzGxj7vsjFnRO4mitCliU9itTIHo40cxdP-NWeSwcLkHBvxoASuWENUPgmbu7NjpUdGwizKS5cS5DZFkqPyUrNFulgZsXAtx1ohYYAekZsH1IkH-6mwVYnkPVbOr9w7nvVJFiWe-Lzo_PctCI7SjGMusSJQfUSQyzXGHenxhRDH_M6scH8IqEgyXjvCdHjvQbW_xRQhCl0diWos0pJWYdjOgvZvzMI9VKj25yYi9CE_qSQUieHajCL1Ye5mPT4lnjsf8nzKKpQgVKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30588621a9.mp4?token=S-MsrCfpzPqlYH-G_LmEO1PcMo8uEUaNbXWcEkARY3hPugfKmWWdVbbHHqYAIeLBewiPF28HZzGxj7vsjFnRO4mitCliU9itTIHo40cxdP-NWeSwcLkHBvxoASuWENUPgmbu7NjpUdGwizKS5cS5DZFkqPyUrNFulgZsXAtx1ohYYAekZsH1IkH-6mwVYnkPVbOr9w7nvVJFiWe-Lzo_PctCI7SjGMusSJQfUSQyzXGHenxhRDH_M6scH8IqEgyXjvCdHjvQbW_xRQhCl0diWos0pJWYdjOgvZvzMI9VKj25yYi9CE_qSQUieHajCL1Ye5mPT4lnjsf8nzKKpQgVKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤣
ناراحتی امیر قلعه‌نویی؛ برای اسکالونی کلیپ ساختید اما برای من نه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/101405" target="_blank">📅 07:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101404">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLnyhvVsZ3QxzlMRswcd5Fdxy8RP4Z9vs4qw7f_4URQzYZf5G2yI-AlaYcRyCvFl2wgKhdmjzNPcQl5siJGLH-8GyGf42fc3vFxcoTI_iGtCf3SuI-q8tk5EJ0tnu5u78DALOvPHFASfeo3K4Dh15aCiiVnYX3dgLOpGHPw2TBf_mI6IfRUxyL9ndNcZySwWOWQcjiu7q9E_PnanK2oXu6R5oOK5jthtQBsobs-xaPJHWbdMz5SN-2_0fHihg-5CUY22vSbey60_09QOmMIzPcj3WaD9AM0Mn2IiSC6gVtk35B8QhdiQUS3wVqzU1f2XSyPWJWYWX3xOUEUUY4auXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
فوری از هرنان کاستیو، خبرنگار آرژانتینی:
لیونل مسی به هم‌تیمی‌هایش گفته که فینال جام جهانی، آخرین بازی او با پیراهن تیم ملی آرژانتین بوده.
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/101404" target="_blank">📅 03:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101403">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRREIQgm7_-G2O-EedhILh2NRmpa1_I5XdAE28dUNt8PfdgNtCU7yWPa6m1onVVvJxySLX6By-992Sq7zSpciqwbsupAvMeoyYwXHMBRr0mn9iYXJWBIQFxdgOwpefXziNpxaHsxgRroi7V4twkC7PBIB9WxXcEtAoiQSevlbMcPTHXajBEE3ctIz6xZuTu02SKPK4bPFJVbMuQXOtJiKUB9tlqhYCgemSQrTmuuAlTdiuxGY8RUZJRgy7lRXik90BaBbHLMQjk6Hrpk-wayg6YD_wQn2i767y2Xd-___YRPA52EZvhqmu8a0ESQfzYIKiZLZfaIX7V_XDxT6XMgDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
||
آمار و دستاوردهای ارلینگ هالند در دوران فوتبالش به مناسبت تولد 26 سالگی‌ غول نروژی:
🏟️
[419] بازی
⚽️
[359] گل
🔴
[66] پاس گل
🏆
لیگ برتر انگلیس [2 بار]
🏆
لیگ قهرمانان اروپا [1 بار]
🏆
جام باشگاه‌های جهان [1 بار]
🏆
جام حذفی انگلیس [2 بار]
🎖
کارابائو کاپ [1 بار]
🏆
سوپر کاپ اروپا [1 بار]
🏆
جام حذفی آلمان [1 بار]
🎖
جام خیریه [1 بار]
🏆
لیگ اتریش [1 بار]
🏆
جام اتریش [1 بار]
🏆
جام اطلس [1 بار]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/101403" target="_blank">📅 02:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101402">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA1jWgn4FrEbyRy1uxmYc-JS3sEa2pd3w0Cbij3cBByRy1H5j9NgIQcZUwNJbmp76iD9Q-8-lDq1daGL1ejVQfFY-doEspRmKoPFesaVv3Sv1-Ctkv3-nlry_DliGeNUwuzPFhWrVagK7mNaUW9qtjFvMOmYFsRME0xnaVgCcai6Bq1BvD8ILJDMoSMN_KFbC5D3jyGYhN2R2GPOHTT6jjEkVu6Vf-XmeagPYiG5HlSJTzCSojS1eKOpdW87pUsVxw66bFvvwgAVkArjpNeBq86GkZkFx4xjD30s3_Kbshl1ZhFLVxj1gSh5QnzjRVzOeeGARZwlj-6DRXTR-xGyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
گلوبو برزیل: ترکیب بدترین بازیکنای مطرح جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/101402" target="_blank">📅 02:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101401">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور:
افتخار می‌کنم دایی و باقری با یک تماس آمدند؛ یک ریال به هیچ میهمانی پول ندادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/101401" target="_blank">📅 02:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101400">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brj899KBPlASO2pxRxjemPlr-4LTGP-WNEfqGSAKroiVoicSx9HpPczl4hYRV0f5HqgkOM2ir3HjtOYxxBxjhv74fZzvPMvUnE-u5-uhz9FXHd6S_uRzuklOcVPmYxGQKTKwp7tgQ5V-wMT2j_pRnW6ojMbuxdrxLAulDSbZ5yhot8c83-vSOa4lnt0okxCRbkNTyg5b-A7znB2zbUoLWof8zdW_G3PI3TcdaNf35FiIIYI0lxlqTrGBgCMkq31c6RWggKJDhKP8UF7wYpJ0xahJGeqryv-DkTVVMvGMtgLU6-EO94XWs_mEmYgfEaTGGRAXUdO3Sc31j36xE6it5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/101400" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101399">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101399" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101398">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZlxzLZ7lIn19xR3GLNw2YlzW-2mHFwjydWNiMMyBdL2DNgNxpZ4dNWnmrwjg1aspaDVggVYP_nlAlsVkjmtA7UqXZWVeS5ET3RvG36OeidYbls4KvU9Dctu4JV9pNWaJl6C_JFp20K8y-z7-VaS4PG_ST4PtrK2VMQ6jGQr5htxsHx3JDWVPaT_mNItxeT6ubrVW5Kb0eEC-UuQGayGakVMN-cOh5yA0MP26RMqjyJU6mNGAcsfvOQj1kIEw0Chol70Y_JJjdyDoeECJh1N57MbwP8-Udyg9F2gNS4yGwFfVAKRzsF5WJcKCtVO7MXQg5cr3A3AFrVLvY2iAPoU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/101398" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101397">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e202619a75.mp4?token=i9ehdXVTNo4KVDkl20KvJsjkAfoiQ2qvBnw7-cdhEv3MC92qU2zHgT3PEGqBfoTEbsqCJhBb60IV6RaTqP9quGKp_U5w68HcKwogNMz73wKord6P4gOOMhGPcf10Gi4CnhsCHiZnQK9507cSBQ8K89IwZVRF177RQiTT5PEyNO084JLhWR9a8lZXUGxismRZPzzHCuB7YZ5RbCnk4JpFhTgOe_AJdYDGfB3zTp5IlfxXCisUtOrUJuhtDF3jdg466cOdm0IZgoBPV8Br29vl0gyEzv42v9NKKg9J43sAzdkQ00k3lzuszQquloAPK92uPpyI2UIjIzEyaYGAgIpw_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e202619a75.mp4?token=i9ehdXVTNo4KVDkl20KvJsjkAfoiQ2qvBnw7-cdhEv3MC92qU2zHgT3PEGqBfoTEbsqCJhBb60IV6RaTqP9quGKp_U5w68HcKwogNMz73wKord6P4gOOMhGPcf10Gi4CnhsCHiZnQK9507cSBQ8K89IwZVRF177RQiTT5PEyNO084JLhWR9a8lZXUGxismRZPzzHCuB7YZ5RbCnk4JpFhTgOe_AJdYDGfB3zTp5IlfxXCisUtOrUJuhtDF3jdg466cOdm0IZgoBPV8Br29vl0gyEzv42v9NKKg9J43sAzdkQ00k3lzuszQquloAPK92uPpyI2UIjIzEyaYGAgIpw_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور در ادامه: من بله قربان گو نبودم، نخواهم بود و نخواهم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/101397" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101396">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWP1LYrYAs7jTLBnSX9iFOwmgqRRZ6-w0g3Ql1u0aPfxrpQ9NP5vW6HA8k-ClvxSePcFRiXuBTnN3IlfIu_ZWznEdovUwYQOvERo4OWzeGTOBZjSRX85iMRnxqWBhKlNCL6xKKYXaXskf9pNCMc48jH-ecj4mmgtVU1O9mw_7o0nP-a1bRtCGx39QHJd4NeQ6tECf6MLn_JL-Q6Q9wHvgc3uEbvmfF-2pvHdnbjIa41AV2Kd8uySSdi3ICUKuZYIuBxSPQ1BpWr-V3vFHyLL8LD1k-MsjBBsDTVWiOShqHuyk5RKZ1y-HwuKXFvgvUuag5Zu9-bjC8ATT4_oSSYKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر قهرمانی اسپانیا
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101396" target="_blank">📅 01:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101395">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=ccQm5CI08Hr7F09yTjCEoqwluRucYOHfmWy6so_Ict9wf_9EbJ_Zm3zCFa9Ge1_roSQcQWTFQgPOTouo5aPT-_neG3JO95QJIvgviR0ep6LQACdhCUHg6PnlVXw46_dpaVVLuWeOaw6SlLSwwojvLKqooFVqobVqcuXGY8SW2olx14iuWA4HoX1-bDnA9PHCpgx0RRDSPa_4WRyHn81VTEn3hFx_TiYi87092SL6O4aFskPmKLS5wTrx6sVc6_JAveQxbJzYJJppGqqA0ny9JdtKVlEs9pwCNN0GEHVilXL-El7wcG9vQt6mL-5iUwEJFvbEgb3SylZxv5DTVyA_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=ccQm5CI08Hr7F09yTjCEoqwluRucYOHfmWy6so_Ict9wf_9EbJ_Zm3zCFa9Ge1_roSQcQWTFQgPOTouo5aPT-_neG3JO95QJIvgviR0ep6LQACdhCUHg6PnlVXw46_dpaVVLuWeOaw6SlLSwwojvLKqooFVqobVqcuXGY8SW2olx14iuWA4HoX1-bDnA9PHCpgx0RRDSPa_4WRyHn81VTEn3hFx_TiYi87092SL6O4aFskPmKLS5wTrx6sVc6_JAveQxbJzYJJppGqqA0ny9JdtKVlEs9pwCNN0GEHVilXL-El7wcG9vQt6mL-5iUwEJFvbEgb3SylZxv5DTVyA_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101395" target="_blank">📅 01:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101394">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
👍
بغض عادل از صحبت‌های حاج‌رضایی: جایگاه اجتماعی با پول خریدنی نیست. در آخر، تن شریف باقی می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/101394" target="_blank">📅 01:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101393">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz4jvAvMWUIWlk4yilA8CmcZUGBPgaTe16hn_JJJF8bZPMGmLlMJ26x3Q2hWMFZC1AOqaOr6fWWmW0aHSej4JFxC_TYgEp9iE8JxEf91efEhPKitFjiVhE83LlAcR6_SgtDUc6fLNFaTm6fMK2FslNoXfxO5pmGnX8YA7jNzkkTs3kChKW3YbQIJWbaSLkRogeu2g_5D8_oIi_yiUl3r9h4R5U2AMWbAj39t08UPL8OJGZTju0-bwra508PZI-z0b-0OL4p6Q0dwOJE281pxYpR1IJP9zw8e8V_WdF56HEVLbwx9Ha94frOSoC2PwQbIvJIaHZ648zDnV7D39oZ9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/101393" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101392">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlE7P1aGsZDzZlvCJ1Pf8m5TyZNY3uPQuK-pWPxJDf28xkAkqxDtYnQMOR2myF-Dhj2Tlt0gI-qOjGG5SeVNzp43_8vIbdbbsAe0E-1QuZZYXC0Bguj-6nLuGs-qFbaldWzwgnOL42_ZVfF8K-jOltfNt1OO-SUYC3cmVSVXpRiwZK_2dTc0ccw7KDHq5vHdUrr14MYu160pPJxuKCMxpoWY7WFhdZ2NPQZJoIRLsNyRrwZ7syqGZRavhh7cTbNm6a42r3ndDVY8s0otJwCIHVakw2Mnc6k_ecRmXZYe2WZpnDYURoMI82wQmLaqXwH4nXywQQkfi1rYdi8sByCJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
دی مارتزیو: لوکا مودریچ و میلان در مراحل پایانی تمدید قرارداد هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101392" target="_blank">📅 01:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101391">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eV8xXh_iNd83k04TN2YZ7TOdk7eazMZp_LAHe2hHWkxGNjHwYIF5xeoMG6elDyukgJ6N579OoeH8zBDXuCz-qNljhWWlxLzQlo_WK2kcgfNAbggAhN1NyJcCTZOpWHI6TCN9_o-XF7nWYn97pR0VyB_J1w7Bmsf0RBbxuSJlbvtfFSJHwzkRKIndjN78L7iDIRd5KN3VmmLfDx_Kc45uj--5A5Is2BBQeXAR3PaoWsDC8P6J9Ripiz4u4HnioEDWt_W2iorXX6J3Lob3Xu0Cl0JjnAq-fWVDPZKuHeIp8Gl73lwkPvUqmFReFOH8zHfL-RSmY-qiSLnaKXPjzxndEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کیت جدید اسپانیا با دو ستاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/101391" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101390">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=DKY-UeCWwIN3spUpVCEaT2dWyU2nO3-Q-kH4q_Fpth_DspDrCq0pfMae7GHGo0NWo1hCIPvbb6zY6LvcchCt-w8wHRqUVRmqRzqqPhCPJhkhutIhrWYWBe0p3PY4T3wiii9Cxw8qDqPZ2LxNJb0-QLSnHMoi6gXu6JMfEm5oKqlz-SZ15O4tm5PzKTWMHw3fG_McDA-_bPD2_iN9pjFbRhzkOCjoGHFHiO9n1trE9sJPhRe8Mn0-yqW0ng_UeoXUkvkF_wyX5qXFYcaLAutH2Q_wQ5uxTtbTcYSLo1E7JrY3eRUMNrpWnWvf5WbMcEr9xlOibAUkofP3tEaHyGSPtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=DKY-UeCWwIN3spUpVCEaT2dWyU2nO3-Q-kH4q_Fpth_DspDrCq0pfMae7GHGo0NWo1hCIPvbb6zY6LvcchCt-w8wHRqUVRmqRzqqPhCPJhkhutIhrWYWBe0p3PY4T3wiii9Cxw8qDqPZ2LxNJb0-QLSnHMoi6gXu6JMfEm5oKqlz-SZ15O4tm5PzKTWMHw3fG_McDA-_bPD2_iN9pjFbRhzkOCjoGHFHiO9n1trE9sJPhRe8Mn0-yqW0ng_UeoXUkvkF_wyX5qXFYcaLAutH2Q_wQ5uxTtbTcYSLo1E7JrY3eRUMNrpWnWvf5WbMcEr9xlOibAUkofP3tEaHyGSPtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با صدای معروفش در جشن قهرمانی
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/101390" target="_blank">📅 01:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101389">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار در شیراز و اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/101389" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101388">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/101388" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101387">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1UhgVqt1j9wjrAovIZB5s6JDukn0OagjaBTSoWT_fghsTSSx9_vSACfxdS4vS03POr-DOhEJ-Mkv8nqsgom1m7lhqjuSE0UQNsIMXJpzPlPXOVUSMI-uskp2CZnzf66P4CPyV6USsLruNlUuWQm6ZtR6fpLfjrhh2pcMLQZ10Z5lkv-GpTllOXCP4kpThQKpkDQPI66BpwNk-LZoJqQ1j3BW2B8DgBp1aq2DVH3hjCPgo13sI2Ev12nDNtCzFqoe5BW3g2dxfyu2h2crSjwqJORrppT3O2XfCRFYD4EgirDUmDCKg6_QSldjInjBqwUOXn8hQF78E0UZDxoASSoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تی‌ان‌تی اسپورت: فینالیسیما بین اسپانیا و آرژانتین در ماه نوامبر برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/101387" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101386">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofvbAujZav_kSYehBSp78VpDxQzSRqkUgbyHA4BAMr770h0kqH5Uiu0s5Tzy-5GldI__ElMRM2srB5XwfhHe1G3GmUseXeE7Mo4KSITSW0eT2VEF_WVGYjkLvVSd1pyYEePlOT7YaqEiUCGDxeowoaFMf_65M-YkN0lhkmXVhhpapdREij2BdmkF_zQWNXOtlWcX0u1-CaFiWAH-KGGqcW-c5Oh5hznFHS-hKNFsETATtuig7WtcDEML7UDwv44cGQfqJKym8ZDN-lCa-oUvf1BhkWbpeQ6O2i-t9aJZbBtAqz2aYkj6sJgBB88_Apa-kpImKwVb3CYl7MOr2kWuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
#فکت
؛ پشماتون از معجزه خط دفاعی اسپانیا بریزه که اونای سیمون در کل جام‌جهانی 10 تا سیو داشته و کلا هم یه گل خورده درحالیکه مارتینز فقط در فینال مقابل اسپانیا 11 تا سیو داشته
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/101386" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101385">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c9-bHUOBHKWFkpZSONK-0VfK8bspRhHtNGRaRR9SV741-3d0GiCjB-9_lOw57t3SC62CQn58mop1YVLKTMwvmeNWwMC88Dx4rBffQZvFn50JOTnidqk7qxR3Zp_dVvpOoyCBI1lVQg2ZPy94SM0XVZZmcsIudB51rQdBcvwNQEdcFochRqlgSqe702WJphELyrxJZxzMkRJXfN-z-OldFXSZf49bYlGmrEOGARUgd3pTd4DGzbrDVB8l5vdpaJYYjstauv8PkROm9IM-nowMB7WT0r1gjDN2DxkwxZ67J8yKLWznUfrI569w2jXoxhSZlUDvoiEUZhs313FI7_ryIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تو جشن قهرمانی اسپانیا
😂
😂
😂
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/101385" target="_blank">📅 00:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101384">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qdQFtliaz_1Vj9wQN6rhcrL7w67eVgPl-8eRXrHVEdSbI-mScRTyNNkEmMBeGfafxEdwHsmZXzrf_aodwEDCgz2D0yzAIE3znR5UfeF1VfTC7htpPaRZXaE4dhZNd6m3YjQKxzX85_MAXFTVC942BJlD8iLKTj564w3YTU_6EmHqK10xL9_qrYbRBWSEZTskX9IehHJmDJiTMvsfsPyuo_iPFocCkJppyRXL82dEMpL7T3fxhoKGf_0iXvsvNl-iEiaODrvVIIGYZB0JNRhXmlpkhiWH8iqeSzlZxeg7nmjseAIyKIs-Y-JPLyrgTX7stoKvdS7gp8kNvDUn3mtbBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا با کیت اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/101384" target="_blank">📅 00:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101383">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2968949297.mp4?token=UGfr5kfb1EYXMmtHDv6BmvLgaDyohRa53thiLqoAJ5nTdhKMT7mESKU0wpFsuXFgjwhywxJGPaQbv_BJQ0P_rs6pNg_H9pTiTYnTMzOWFtvWi_LVcG1J7F4mvyIQSzBCcUGP_qpTa8oaZ71nrGkArxGGw-keQVjq24THxNQXRfisepC2eo0s-rJ3e5cfytzz9PYgOxagup4TjaV5O1cngIltScT8CAyJvuCk3vbm5Tyr3ypJ2iXR3G1VwYNWEcP-790Jb0fPIs4D2goVHuDj3BbsG87w-2UN_AdCynKI6APPLZ-gLy-WM5vMheTTlHzrPmxAEmuCllZHSjoU-hZDyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2968949297.mp4?token=UGfr5kfb1EYXMmtHDv6BmvLgaDyohRa53thiLqoAJ5nTdhKMT7mESKU0wpFsuXFgjwhywxJGPaQbv_BJQ0P_rs6pNg_H9pTiTYnTMzOWFtvWi_LVcG1J7F4mvyIQSzBCcUGP_qpTa8oaZ71nrGkArxGGw-keQVjq24THxNQXRfisepC2eo0s-rJ3e5cfytzz9PYgOxagup4TjaV5O1cngIltScT8CAyJvuCk3vbm5Tyr3ypJ2iXR3G1VwYNWEcP-790Jb0fPIs4D2goVHuDj3BbsG87w-2UN_AdCynKI6APPLZ-gLy-WM5vMheTTlHzrPmxAEmuCllZHSjoU-hZDyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/101383" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101382">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=lMGN7Fe2LwGj2Qtn82rN98aPR0QzQqPFm57oIlCuVz_QnZ0yy_weDP5LgwCK1ZmMJJKXI8bqj3BZmM6HADoz8ZI8DIaKwMpN-IWvTH9aLN0hQ14q6_CkEL9D8K2-Q7YZKE6oWnEJRbzUR3EDU1VcbE2aa-svAUYrngcXCmgTFiEI19ZtE4ZDQ6oLs1kY2brJ-9QXCw0kb6XThI-KMUBjCFJ8S9XdvtZlKV6iaDF93K3uGJlW9B9HasjpRJJpSPLsILQ6wyj_THuqTY7Th--cj99OvjJ7fg0nyTgyBArj3iWh25GYkNXeJf-ysCYn9dexZOJHcYI6efWQG2LRqfiSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=lMGN7Fe2LwGj2Qtn82rN98aPR0QzQqPFm57oIlCuVz_QnZ0yy_weDP5LgwCK1ZmMJJKXI8bqj3BZmM6HADoz8ZI8DIaKwMpN-IWvTH9aLN0hQ14q6_CkEL9D8K2-Q7YZKE6oWnEJRbzUR3EDU1VcbE2aa-svAUYrngcXCmgTFiEI19ZtE4ZDQ6oLs1kY2brJ-9QXCw0kb6XThI-KMUBjCFJ8S9XdvtZlKV6iaDF93K3uGJlW9B9HasjpRJJpSPLsILQ6wyj_THuqTY7Th--cj99OvjJ7fg0nyTgyBArj3iWh25GYkNXeJf-ysCYn9dexZOJHcYI6efWQG2LRqfiSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال با آهنگ معروفش رفت بالای استیج
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/101382" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101381">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/101381" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101380">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=F-_BGQTCzkic2eP4RsRfdveCnTeZ-TDFpcnVMZv__tgP82ObDCX4ZHMUAnuZzm9xJifK1xN461uiBN-JPLEsWWY1IJAKYw4oARKWb1tHWCJkFHUJ5DNygzkBNHJ3M20yDB3kFdwqimEGMwidwXD_I8tXXkCv8gVucd6WYRDgpZ9vGvFRfBdkg3rqCyTEeCWEpuVi6TnoCcV43Jfsi5U2jzu8ZVRmccnt2tx5VI7vB09A3Ui0tyNR6FXvEzl6uyULbZeooscdvXsf5ClpBSGnZbK-UcI1hkrXYbxJpKYM_kmkHjtfZI3o8p8sIaPo8RNXdRrOSZhY6ikbbJYeyIqy4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=F-_BGQTCzkic2eP4RsRfdveCnTeZ-TDFpcnVMZv__tgP82ObDCX4ZHMUAnuZzm9xJifK1xN461uiBN-JPLEsWWY1IJAKYw4oARKWb1tHWCJkFHUJ5DNygzkBNHJ3M20yDB3kFdwqimEGMwidwXD_I8tXXkCv8gVucd6WYRDgpZ9vGvFRfBdkg3rqCyTEeCWEpuVi6TnoCcV43Jfsi5U2jzu8ZVRmccnt2tx5VI7vB09A3Ui0tyNR6FXvEzl6uyULbZeooscdvXsf5ClpBSGnZbK-UcI1hkrXYbxJpKYM_kmkHjtfZI3o8p8sIaPo8RNXdRrOSZhY6ikbbJYeyIqy4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
قلعه نویی: آمده ام بگویم شرمنده مردم ایران هستم می توانستیم مردم را بیشتر خوشحال کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/101380" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101379">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDYaI0l7wLOBRqjBl25MZPqyzQ5fJmZWzU8CuoSSyMDtAd26Cbbi8Z6Sa4MbKcL3OkEIQjHuFkobWgJ6GV0tgysSVK_FonU9FWLhTeHTSyn5Orkw0UdzSojG6P3oQWiaQz0R6pLk_iquKIu_ce6Ma3QoGboMXl0lqa4f7TVkWrb2s43lHwSrEj7ak_vH-EAtKHp1urk83ksHwhzBpgXiO2xFpGH-7rBDvz0o3e1gv9B-y7T8JkcTvhZXPI2GDa093O_VDDwkUBOCnI2QPPIIdXwjbO-64guDNYJrekZ_AHFKEbKeW2ruru3iUoEH2uK7XalgWaNfcL8adZDfBstOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به گفته آاس نزدیک به 1.8 میلیون نفر در جشن قهرمانی اسپانیا حاضر بودن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/101379" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101378">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=Bm85Uh9rlf4ZjrMu3Se8lXI6G9dANC1mt125hC0Q23uMW7PHaVcSTOKBlqSNnqN-HJPx4he6uoIQnrA1sUYMEgwNMH87ZY0rEWk6Z4UPWE-hfbI5WYVAF_UPSw9cZvOHFteylqe4M0_e-XVaGdBLcJw3MBB36hIT-qsVdo_vgjHhN1A0fTu4UcJBOnT8f9k7pje9zdJBI6xHlGYIvzP3qXoCQrrWmIVu3mpNZ8aThB70h6lofOgJYtgIRVT2J9mCuJpFmHRJ_M6P5YBBVaZc-ZVaBwAge2JLioD972KOqyIn3VgrfiIJUK8YUiBAjaWZ3C2bL9sG7cGKKaUTItdvDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=Bm85Uh9rlf4ZjrMu3Se8lXI6G9dANC1mt125hC0Q23uMW7PHaVcSTOKBlqSNnqN-HJPx4he6uoIQnrA1sUYMEgwNMH87ZY0rEWk6Z4UPWE-hfbI5WYVAF_UPSw9cZvOHFteylqe4M0_e-XVaGdBLcJw3MBB36hIT-qsVdo_vgjHhN1A0fTu4UcJBOnT8f9k7pje9zdJBI6xHlGYIvzP3qXoCQrrWmIVu3mpNZ8aThB70h6lofOgJYtgIRVT2J9mCuJpFmHRJ_M6P5YBBVaZc-ZVaBwAge2JLioD972KOqyIn3VgrfiIJUK8YUiBAjaWZ3C2bL9sG7cGKKaUTItdvDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قلعه نویی: در همه جای دنیا انتقاد از سرمربی تیم ملی وجود دارد اما آنجا حسادت و عقده گشایی ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/101378" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101377">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaU4mGwz3mgdC12L9iE5MJmYGscALYTXzqITc6BegiMCN_0xVCxqYiQTAiYbRy4nWQMf3KR03q_QIf_HZFWuYYIsewgsyWt6EkyJ8wAAm3WjuY_zgvWKVodmSvOKlJu0HnBd6S5eWlkQzFROZlgEDWO5HHBPDYc5fy9xZ794oh2V-i3cvj3QnGaLbJYg5Lf3h1gYWjUEJcFBoTqyBJbU8r6vBmtb_Y7bmH-TUVZIBfm-UqnyppZL-uVWumsxI0gA-IeU-fp1LeaeLNWtDdLEoAWIxtBxUpIDkrbAmjsIFMaHFjkAdtyGEBObQ76WR885twBS8aWuDyMS06624dX-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان دوران به صورت قرضی از النصر راهی بنفیکا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/101377" target="_blank">📅 23:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101373">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-NJB_x8RjQWHHGItX1OfbfKU-EaRiAXf1BrzwEqcftYtGFAcYxBdNH5GO1dHTxPxg8DXYn466abLjQch87GsCkNuqaAKKrm5VKFrW4VDbjy4T7p4nlgANGJTjqrFCHOwinOPBrhODvvI94MbxyvLKRBgEjrgziYKtvyGb5A8EpOTHKAH8_zwzIqKtGw5k-o-wwJg0yoGS8peYJ2Z75L9snOm-h0qpwWvrqo-4Fo-DKbqKaokuBYxwdKEWwAs64qEPxEDnP-Jcsv1oAYl12EgJrHOMph9lFJhV_qYHxL2VIEypz_7XbPATV_YU_85I08Nd8TJfRSgSUQR3tcd0IV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXhccCrnEFFMCp2y4rVk4ouv7M2MoVmysnjZZ7-sIVsOFQz3vOgqMJ3Wv76bAWc_sPue-LuIIwncm7f9JV1TW8jVp0w1xA2IRPNTCtYiOZVMhiCvcbaFkJo69jPzgteD5tbzABKhnLH-WR07pkXVV5QEblyc9_5GZrxd3jZ6Uf2F4NZ9zUFkcZnJu_7lrRHcNJxBokP9ba8O7juGoUNvCHDBYBRV2lYtuhyztNlZNHmSDJ6VZ_web3KYTA883IYwM8k99FK4QS3Xz8TIZ1n1i-dRvR6Lny24apicDixVwr2jMYYm3_Mdj1dgk7tei-LcE_Uf_Y0ZVdST2G9HuztL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NurzYWDqjgj4AhI8ZtklCRxOPz9FEX2fGQQ52BcYYZwvgv85g5RZbZDwNjAgobKEoKuu3khWW7qJ_J_U7zZ87FPWbBZIX8wGnGMYv-dlFiPLRmKC5nEgOAEkv8RMmBcMog0MeKYrLVvQKCAvv1-4f8vEgo0mxaQpn6-zSE-zTUWZ1iV-aX0101a5_UBr5gErqBM6bNZXw38mKJudDepXAlJYqBQXUnVOtc2xEm3DOGXM4Rd9U_jMOvAtTza52114SuH129jxukqtpGmFVZPXX7fEExHASa9vaFkStm1N_PiG8Kr19mlRwKNOT-ltdEXgJWVtOMFHlHQdJksbhAvrxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjXhXMaliV-KgRIquS9Q2IIxHZOkKGLZAJSP7oE614GPJBktZvdVV9tlFZRAj8GIf7k-ggtmnuEv_1r2n985-8hMdAFHTVVm3yVBYm6FSO7TBCJLEbRKff73OTo6PU_sT6BW7e7GOg8xrcoXS1Puk2vljJibjWeIehMUAILFyNEcpEyeyP5F87IQvwYouawNTJiSvQmyGrOYJOVj1ahQQSvmqJZXpyxg0A5fUnzCfo0uQqzdF_k0gY5DzLHsi0UDfAGMhvcsBo7wBMmcg0cC-vyAi9qNkNAWrM1fjnSiIV8cbpqXwuv87NBD7EUZZf1aWv8i9QvifpuMDN2MeAvxUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
| اولین تمرین منچستر سیتی تحت هدایت انزو مارسکای ایتالیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/101373" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101372">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK3jIKsBwhBvL5tFFoyyWqbQoGIx5RVFjaRFa10EmIMqY87yxwbZR4obSYs8LGzvQ7AANjJqXnMvPAwPeQ14BYPSxSJzYVv5KCPHWHiItR_Uz8sfkf_yvRKlKEJpHs7Dai7HExNF-D1uWztEof2Nvi1rJEbdiazFwEnDjXd3YKNiYy1xTTXOpXpGVqCS-2-dJPpboMs-UVymST3gTfQ1fh26uk0nNTAtH2FOT9chBwojKcqtqsDxmzXOM5qPrqBppdU2g9GrZf-Mkn_NcXE4YQ7vKlCKYR1Uk5k5rZ62tHnUfenMkeTGiZ3VayQBYlUPujTPGR3c7NnGnbjKMDiefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:  رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101372" target="_blank">📅 23:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101371">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9632195436.mp4?token=BxGsJzWNHp-RuSYnF9HcJso_z6ohX5HIcrJ0iObubTVp8Gu_yKi0Z2TIsOTsCoYolfSqHRU7RQN74FwOeEjiyd0LvKY5r3Ix1a8V8TS4xTUFbYfUsXd_EofE8t2kRyE-40sqkAEciPJlsZkPjJ7boKhO4QJygbymQ4603T1VUcJ_KgY6Dkh8lAhgc6n7G5aQiOm0v6V7HLyVLuGk6NMblvPc1_9m25QH5atrmqAjyDGMPlGxb1tf51lXfDGJWfipqhb4gry22wmJszEPE-pUL3X-l_VCkCeEf9anu3lGEf-P3wLCp5CCWXblr16dAtFswY7VOhVWJqzRVihq8Vl_1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9632195436.mp4?token=BxGsJzWNHp-RuSYnF9HcJso_z6ohX5HIcrJ0iObubTVp8Gu_yKi0Z2TIsOTsCoYolfSqHRU7RQN74FwOeEjiyd0LvKY5r3Ix1a8V8TS4xTUFbYfUsXd_EofE8t2kRyE-40sqkAEciPJlsZkPjJ7boKhO4QJygbymQ4603T1VUcJ_KgY6Dkh8lAhgc6n7G5aQiOm0v6V7HLyVLuGk6NMblvPc1_9m25QH5atrmqAjyDGMPlGxb1tf51lXfDGJWfipqhb4gry22wmJszEPE-pUL3X-l_VCkCeEf9anu3lGEf-P3wLCp5CCWXblr16dAtFswY7VOhVWJqzRVihq8Vl_1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
تاجگذاری لامین‌یامال در شهر مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101371" target="_blank">📅 22:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101370">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGB02SMSaXNZvZkcuF-sfcEPi7IQsmzOk6HiHyAXyf41moyLzeKjkNSowkPPHyS6DcGzXIhklF5hM8oN85igwMwJy1-7_etzEE9txY8B2YbNEEMZG-aDD5S66FhV58nmfeLzvd51xN1fLeKqlRNlB8JMDcAynAHkevtzz4Q9Qyt7geJjvmaVRGy5eTf9QXtUXn84N-noNzKDZgCraX3-KEZq-8dLkeKbFd0ygHVlYrO8gX04tPnZitV0rqXHygw60j0Mv8UnF4XhaFmtiSiI1kfnj3jVY6Q8p-n4OUUx5M05jEs2_9MUZMQzHKJeuvRSqORjow9qwHCtmnzdDQCJsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال این بنرو از یه هوادار تو جشن قهرمانی امروز اسپانیا گرفته که روش نوشته شده:«هفتمین دورهٔ مسابقات ولادا دل آنیو (یه تورنومنت بوکس بین آدمای معروف)، بین پاردس و گاوی.»
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/101370" target="_blank">📅 22:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101369">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇹
🔴
فابریزیو رومانو:
🔻
منچستر یونایتد این تابستان به مارکوس رشفورد فرصت جدیدی خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101369" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101368">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bufyjGMUTZj22sah_0xBkn8XUmQcBHIXCandbadR83WUNWXpJz4e4gQwRgSlYNatfAhR3B_RaclaMlKgVd47f_XxPZ4SKkYMYW83DB9oTCmUil3QHtaUggyOMwTu-KqiybhcFH-IfLuxNy3jagM22x3m_BZxGBe5ovN21IO5Qd31voT_Ai9TZX2J__9EBR56v0h-6DodTL2pExgjfzpcP3xg5CLoO-lK0ese3oIEbtnN9BOyHKbV7dZuQ2QCXOxwxcnpgXBlfrg-yuP6WcJhIFSzhiBFUw8N-4zS2eVi_LdwuXUaPvRaFwJwEZXeurO_TZaUmaUU3Rk2nlD0Ab3uDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:
رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101368" target="_blank">📅 22:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101367">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmBa_SHJFTwt7cn6iZtgek--cOJVir48e7UzBKUK2b5PxBNxXXZBOzB9UhobwpF9gZX4KeYc5a3RneLneXyUGUpChzMDpn4Oc2zCT2T3_cqHhOR9KKZrXmWaHixNO3WPwa2RRaLmmHcnoIAmC5p7ecSGfq7JqfwNd83i_1Iva6lTjQoogTr5x9leJt8GHvCt4C82RWUAG9SqsyW7DYYACJS82nZ7w1dZqMr8tFbyv7k2Mpor2jvZqQ6VeiiLENCE6gOptcLJ__XYogqm07mx6zIBH-Q_crSOPgQiTgIsGDCRKCNC81pOL3MZzs7KXcdiJYm2MvOm3ifsn-zZWXE_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دزدی قهرمانانه لامین‌یامال از اسطوره مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101367" target="_blank">📅 22:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101366">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=WXUXxUty0Xdp-tNdAwmxm7OSs0WUo-zrhLtH4btZTxipgoywQ2ttPEU8YliHSLHHzaDdLV1azF5KkpwPkhF3Vt-PoFjaCBQla8PSojQyUlooRX1KpYGwePjU2ljaFYSLq5nszOVqEVVJKiZg5jVAIcxEgz1J2OuEPI8IyT0bkiGN4MyigUW2T3k_qY_09l13lEo5N5J-xGh9D0QAHxxM_xV06givEbJghMvcvb0w6xYK0i3CssIf6GqsRKfU19Q_qYS1pUAL74NoEcWgIvldJnigE-wdlnPDIHnBSSFBI8l_-NnQ54yOLJ2xSUaC7Go151pMt76ODSJ6ByzjE1zmeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=WXUXxUty0Xdp-tNdAwmxm7OSs0WUo-zrhLtH4btZTxipgoywQ2ttPEU8YliHSLHHzaDdLV1azF5KkpwPkhF3Vt-PoFjaCBQla8PSojQyUlooRX1KpYGwePjU2ljaFYSLq5nszOVqEVVJKiZg5jVAIcxEgz1J2OuEPI8IyT0bkiGN4MyigUW2T3k_qY_09l13lEo5N5J-xGh9D0QAHxxM_xV06givEbJghMvcvb0w6xYK0i3CssIf6GqsRKfU19Q_qYS1pUAL74NoEcWgIvldJnigE-wdlnPDIHnBSSFBI8l_-NnQ54yOLJ2xSUaC7Go151pMt76ODSJ6ByzjE1zmeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
کارلس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101366" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101365">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=AsQerfhFf3Smpg0_pd1ci3r9d5gdA4oNUk1i9EuuAyYP7LgCOyP5N_G9v8TvGfv7D2la_Xp8gsPpXlx4GaUWYM_YUtcasU1L1qG3JjpAjL0vCeK8ftfcVBPNyN4rrHah2kU1uEDu759uiiVLMRXKJuXxcXR54_PHqZtBuEgAqg8mstD3Rosfr0xoGFL46nwM0ga0SMcr-QU0DT77JWO7ps_dEnKTEbBpCKn0wr9d_KWzUa5V8R-1wj_8kiUPN16JYPK2DKoSyOyQYPMREexHN1BcLAsjc_yuKAN3Loz28xeYoFfSf0pQ4N2xSP3FmlPl6eH02xHJ1RcPfMYOIMOSDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=AsQerfhFf3Smpg0_pd1ci3r9d5gdA4oNUk1i9EuuAyYP7LgCOyP5N_G9v8TvGfv7D2la_Xp8gsPpXlx4GaUWYM_YUtcasU1L1qG3JjpAjL0vCeK8ftfcVBPNyN4rrHah2kU1uEDu759uiiVLMRXKJuXxcXR54_PHqZtBuEgAqg8mstD3Rosfr0xoGFL46nwM0ga0SMcr-QU0DT77JWO7ps_dEnKTEbBpCKn0wr9d_KWzUa5V8R-1wj_8kiUPN16JYPK2DKoSyOyQYPMREexHN1BcLAsjc_yuKAN3Loz28xeYoFfSf0pQ4N2xSP3FmlPl6eH02xHJ1RcPfMYOIMOSDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏆
پرنسس‌های اسپانیا بیشتر از اسطوره رونالدو دستشون به جام‌‌قهرمانی‌جهان خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101365" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
