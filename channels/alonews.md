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
<img src="https://cdn4.telesco.pe/file/jhWrHEXaDTewVdE73FgELzETTSfQ3LI-ETZeGK3gNg4Pi0uP9yal59u1pPDFG9oX_lpbn0ofCgfaFVyHfgUZ-r3K_x7XPF1FXToEJcWtHpvL_GIS7jLwFi82wz_uQ_n2PoHKb80ZP83-wdFm6Ba_jXYAs6XhOGrOEB2xssd4ulb1O2Ek3J4co0O53SMaScyRpwa7XDKEmGOdF7qAu4qwR7w5eI-T35odgi9RrOnAlVuPX1jqbLFp5cxDSriBQQocha2NZ3YMvDz8Z5PzeK5npMO70OyrE5wJASwCQPY--laJRE2eeAm3Ku0prJeqP6InbzFlwRI91l-oQ6XIs0Mr3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 992K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 21:23:56</div>
<hr>

<div class="tg-post" id="msg-139197">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGwIJ90XUWPfhTsnqkqPxKLcAmm5Emco3lkrKIDa72FOsJlYaPKfuWB7MUbrqS-4tt0uMpzhphtfZUkQ9GO8xMbnsAh5xSuM0ZASKRtyrArW_GXcmhqkoOnVATk5yQhchRZPk7E_AvnckQ48AFSMUp2JvMPe4pc7jy6jG56OsCzG5F-ocNEvxISFBJlN8PSTAFhlbUW9ojeK1HofqTbllUu6E2_DtB-oBbmQ4hnfwXRGfGm27ug0-vs53wJ3WSnD5RPjKF66nXDV3yFSz88rVspdnIlLYh1HEnmiuWEc6N0jM6nt9074zfTbD2aKK4MgunSj4E1CxttYKT7XR1tdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲ عبری :  ارزیابی اینه که ترامپ از هر زمان دیگری به انجام یک حمله بزرگ علیه ایران نزدیک‌تر شده، اما هنوز قطعی نیست
🔴
تنش‌ها به بالاترین حد خودش رسیده و اوضاع در آستانه انفجار قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/139197" target="_blank">📅 21:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139196">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT43CeOsFghMiRslyAnyP4GTrsUZ6Rcf-EpMc3TFVAdXrgfIwxZDdPR9X44S9sFuOlxmn2zJr8WWw_HFsbBb-9gucT4HsxPeN6GXMLu6JzMZv8dPLWbNxDuDl08qnkFTf1s4zLLboxN60aOOXVZYPN-detanRS8sS4XkpCeOAnfy5XoWrvpGaXFmxuqJ8FI6dFySweRIFp2_78p97NfF1dTv_NZX184Rl0zXf2ZcfwFQ68rksdCbhcyShE2XucXNNyqhc5gh5erTxsiJmEKiWin4YqMxbuHdeatZRWJXK6L2no2TV-MDcMbDtiUu9wSzaW8SuT1fpgWSnoFDy47KqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای ناشناس آمریکایی که احتمالا جنگنده است از پایگاه هوایی الظفره به پرواز در آمد تا بر فراز خلیج فارس عملیات کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/139196" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139195">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شیوع ویروس ابولا در جمهوری دموکراتیک کنگو به بزرگ‌ترین همه‌گیری ثبت‌شده در تاریخ این کشور تبدیل شده است.
🔴
این گزارش می‌افزاید روند ابتلا همچنان شتاب گرفته و ویروس تاکنون به پنج استان گسترش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/139195" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139192">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9E2yvzkLhiy246hZNtffyid-ARyEsRy5166n0qZ0F3SIfEcmLjKKcmJSD-LwUSZcxfjDFpiXemXcbL2dQ-7I5_UQW9b0s7jy3gb0O9cxfCI8yzuBqt3g69lPHNfLqCK3AP8767jUGxezLDX_jCPX1HT5H3YOySwKxgfZGMt1j33jXJnQnciHioKTjlEby_7b8TSyBPwxjqZ-3_VVfNqR3qTYWTIfIbswOzlvMc6BorbNULlz1XwXa_S4BftGqlZkKKY8NQxyn3gawgC4DWNBh6sDXGu5kiVRfQX3oVIKxH41y0ou_qQGlqTnd1mKBr1voARG9UKaQdOA1ZFM8R0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDAl5rQs1DDHADU01kL11odX9hiy-DyYqd2Y_FS9P5QCcONqfG0ZgWLXzzJ9ZH766lTNJvxhgYwWIc58IjCBaRbbSy9_KSnLrXCwIMaU_kY01HbevL_rGM-FsB6g3gHkEIuYU9WKb38UPrW2eDuEQJ2qSA5OnWylDGQbJixgi1hsuSQxbOOvGcw2GgTzcxwRMTm1TvZWUKGS65NJvvys5_KmFvlZjC2nsDDiYGtu_mOvwqptTg3yexc6nHR5KHwzOlF2YoOHW0sRqhhpWf1y1e5nNItlk28OSvchRe8eeyMJjXE4waTUXzvwYHoo_Tw5yA0J_YFgkgSqGXwkfx37ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlHJ6eYsKnC70lg5ozP468Q87aMaP9F9HGlZ97PZGXQpDNXsQPdSMcUbjf7_Yf0HD6f7hkPRc8-c2aYLqKs0NAU_6KrqsboktmIlQ6u7XdwyUQ2_qPWJEpX4rb8Lo1tafD7HcPfSCTz1TSnDtR0TTAYutv5vKdb8dndE5WlmPlxVmmVUuDhdxBDMCCMUSruafairuO40qeM11BE94fD6EA8xpQ59J_Nr5gqMSUMo_ldwWVpVuPgXuL-Pz0hUOd2BsJcoqbejXSXigLWraiNWQ7u13846Kw_d2WU1Aj7nYBWI6xBeYkXKDZIfsm40ZhjNRUtyqglj4MG1otwCC6yL0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پست‌های جدید ترامپ بدون هیچ کپشنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/139192" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139191">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd220</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/139191" target="_blank">📅 21:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139190">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTAm3EKYiOGqC9LY9S9sgAusZrg8DOGailxlvADLawagOLBPWHtPq9XMpR0mhxicmNdiF0z7yrDIOKZrnHF2G7Gwh6pvWtOmfuj6td1QdhlvjhzzHLZs-MOFulWBVS8TH2x9n0hVGmqiaO_mrwOGRsMc-EWdA2DBQTTa46dCwn8pv-ebFsqkbBQXbsX6NrP1fRVYTxAa_5TMS28sk0M1oR7mB6GfNCkex0tp6Hvlt8yQQk0C2OiRHOUGOPhA8S_gQaUAACqzu9Z6jw2wU3KD1uBhJxiy8P7YE91qw9VopsoXiq7_Id7WgKaNarXuLmQgoCknNC4zZMamqqJCwQvMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظاتی قبل، وضعیت پروازی آسمان منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/139190" target="_blank">📅 21:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139189">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
یک مقام نظامی اسرائیلی به نشریه "The War Reporter":
اسرائیل از سوی ایالات متحده مطلع شده است که واشنگتن عملیات نظامی علیه ایران را از سر خواهد گرفت، و افزود که "این منطقه در آستانه یک تشدید جدی قرار دارد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/139189" target="_blank">📅 20:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139188">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مشاور تیم مذاکره‌کننده، محمد مرندی:
«شاید امشب آخرین شب از دوران عادی بودن در خاورمیانه باشد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/139188" target="_blank">📅 20:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139187">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کانال ۱۳ عبری به نقل از مقام‌های ارشد:
انتظار می‌رود ترامپ دستور ازسرگیری درگیری‌ها را صادر کند و آن‌ها ساعات آینده را “بسیار سخت و بحرانی” توصیف می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/139187" target="_blank">📅 20:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139186">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
یک منبع رسمی اردنی به العربیه: ما به عراق پیامی ارسال کردیم مبنی بر اینکه در صورت حمله به اردن، گروه‌های شبه‌نظامی مورد حمایت ایران مورد هدف قرار خواهند گرفت.
🔴
اردن همچنین اطلاعاتی را به عراق درباره برنامه‌های این گروه‌ها برای حمله به خاک خود ارائه داده است.
🔴
انتظار می‌رود عراق اقداماتی را برای مهار این گروه‌ها انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/139186" target="_blank">📅 20:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139185">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: تخمین‌ها حاکی است که آمریکا یک حمله قوی علیه ایران انجام خواهد داد، بدون مشارکت اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/139185" target="_blank">📅 20:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139184">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فعالیت ادارات ایلام فردا و پس فردا ۲ ساعت کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/139184" target="_blank">📅 20:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139183">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVTJkOVfyigflP762KyOj6ypIj87y3pV7GEWSTxtnbIl4Q6_GIFSt0LDRItKg1bWmOD8IQKU88KE5yPOKGNth7-bil3PXmTReQDN7h-k5RFrHEbeBGYl23riN5y9CuW1IaOasl5xNW_papTx-obFZiJmF--5xMYorf7xtWC_2wLCg2f62XpCbHI3Py_jpYkK8xtafYe9igHtzNbge_ASlfNpqlyZsbh0GjOiTw7FLJtkXSwErU3Z2HK0sW0x3RYsKTfkj7_Ar9PG8IYrCYFACGZ6YcJmLla_mv8AdD-EgcXHP2Xh7uiFLtMyfiteiP9Fi8_wM9GvoA07AvyVkUVktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: ایران ممکن است منافع آمریکا در سراسر جهان را هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/139183" target="_blank">📅 20:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139182">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
واشنگتن‌پست:
کشورهای خلیج فارس، به رهبری قطر، در حال مخالفت با تجدید جنگ با ایران هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/139182" target="_blank">📅 20:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139181">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjqwERJfmqzZgFKQYE2gT808cpbNP7oSj0OZL1sCKeugtp8sUwXF2P9AVTTvQfsW-Ba88GaQhSR1jM9sV3ZI7fN57RB8TyfIimzJzG38ndKzUALsWPdDqiCwN-qinEnfOhzDdORAZeieB5Ai2v3D9DrpitYSCtwfvJGb1K6O-MTyVgfDE0UmGM7i_nTBHW1szUCWpsILvuoliAJQBiA2LMcJIYkqpGJ-CBakvHeVIMbR-VnT_MJy-8syRimFwSOT_qrT7v_YFeH_PkUziCsCX5FIlW4TCQ9pbgQq-QNs5gAIga-6nb_p0SsUvMZy1FBzlaO-TLpQh0C0M1J5RoVSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : از طریق شبکه اجتماعی Truth Social: من به طور کامل با جینین پیرو، دادستان ایالات متحده برای منطقه کلمبیا، در مورد حوضچه بازتاب (Reflecting Pool) مخالفم. نمی‌دانم او به چه فکر می‌کرد؟
🔴
به نظر من، این یک مورد آشکار از تخریب بود که شامل چمن نیز می‌شد، که روی آن با حروف بزرگ عدد 86 47 نوشته شده بود، و همچنین سایر قسمت‌های اطراف.
🔴
ممکن است مشکلاتی با پیمانکاران وجود داشته باشد، اما خسارت اصلی توسط افراد خرابکار وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/139181" target="_blank">📅 20:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139180">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری/اکسیوس:
ترامپ در حال بررسی امکان صدور دستور فوری برای حمله به "تاسیسات انرژی" در ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/139180" target="_blank">📅 20:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139179">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تخلیه پایگاه‌های هوایی آمریکا در بحرین، پیش از حملات احتمالی و تشدید تنش‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/139179" target="_blank">📅 20:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139178">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
گفته میشه در بنادر حاشیه خلیج فارس برای کشتی‌ها دستور تخلیه صادر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/139178" target="_blank">📅 20:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139177">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
استرالیا با طرح شکایت قضایی علیه تلگرام، این پیام‌رسان را به کوتاهی در حذف محتوای تروریستی مرتبط با حملات «کرایست‌چرچ» و «بافلو» متهم کرده و مدعی است با وجود گزارش کاربران، بخشی از این محتوا همچنان در دسترس بوده است.
🔴
بر اساس اسناد دادگاه، تلگرام ۱۰ مورد از ۱۲ پست گزارش‌شده را حذف نکرده و در صورت اثبات تخلف، ممکن است تا ۵۴.۶ میلیون دلار استرالیا جریمه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139177" target="_blank">📅 20:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139176">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC7Sz_CpM7KFjHuMgm5CEF5udWfrCqsl79K8SOryc8etVpIQj0ljo_WjIHMFPFGeQc4AkujUJFtd4bjw02a3ZSMOL4_30b0dHRejlmARmQIFeG_HPyHz_B_hr657vg3Ho2xy5hFfvITPeHTPk-vAmtCIBQ-0vwcWJOYntiP8dgqMRO4Q1utYP6qqwPre8_mIiPVe7ELMdjEISbc_8MU1aorLoXJlzd9CwlErNT1LWG7FPTdh9ZmGzrxI7q9mjoB72RDVPv2Jv40OlqfymVVVfcGGcNpnpylVwHbZy3lqVrd8neZSJkNpORWtE4wuEVHqXeWBfW_ORy5qe_jRilW7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت ساعت پیش سنتکام:
یک هلیکوپتر CH-47 چینوک ارتش ایالات متحده در حال آماده‌سازی برای فرود در خاورمیانه است. چینوک یک هواپیمای دو ملخه است که برای حمل پرسنل، تجهیزات و تأمینیه در محیط‌های مختلف طراحی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139176" target="_blank">📅 20:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139175">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وای‌نت: پدافندهای اسرائیل به علت بالا رفتن تنش‌ها با ایران در آماده‌باش هست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/139175" target="_blank">📅 20:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139174">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16152d790d.mp4?token=kegcHYqFCfL4N8yhZFNvgmDHJIXEWm1C9f5vl27mPJl_gGp-IS0qrusAtg-JmpE6Nc2OVvKftldj3VxrvITbBC8_X1bRrYFo0lKsJZIwl8omFQQgkW-w4MBus8Y5oDjYpAY8BNkzOt2hI7vBmGdhIo1cmia2zyqmRVmsS3LiWb1P6KnQoPvazd4qvwUiS18i-OEJ8pkK3-Gcs9qhOHVXbYIALTh1aY8vV0nN6u-O1FAklGFzoZAUy_h7XHgN_NEIH9RM1w0BpyHzJbB1-N5EJbhZvHsFeEt9Yvralqb4ayVhcUX-2y6b00FC8anYDaOXI7HqPWPCqwrSYvnU9onjJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16152d790d.mp4?token=kegcHYqFCfL4N8yhZFNvgmDHJIXEWm1C9f5vl27mPJl_gGp-IS0qrusAtg-JmpE6Nc2OVvKftldj3VxrvITbBC8_X1bRrYFo0lKsJZIwl8omFQQgkW-w4MBus8Y5oDjYpAY8BNkzOt2hI7vBmGdhIo1cmia2zyqmRVmsS3LiWb1P6KnQoPvazd4qvwUiS18i-OEJ8pkK3-Gcs9qhOHVXbYIALTh1aY8vV0nN6u-O1FAklGFzoZAUy_h7XHgN_NEIH9RM1w0BpyHzJbB1-N5EJbhZvHsFeEt9Yvralqb4ayVhcUX-2y6b00FC8anYDaOXI7HqPWPCqwrSYvnU9onjJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
امروز تو بازی والیبال ژاپن و آمریکا  تو ست پنجم یکی از خفن ترین رالی‌های تاریخ والیبال رقم خورد. پشمای حضار و گزارشگر ریخته بود
🔥
آمریکا این بازی رو 3-2 برد تا اولین باخت ژاپن رو رقم بزنه و به فینال بره
@AloSport</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139174" target="_blank">📅 20:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139173">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ارسال کنوانسیون «خزر» به مجلس برای تصویب
🔴
سخنگوی وزارت امور خارجه: تصویب این سند، زمینه ایجاد یک چارچوب حقوقی روشن میان کشورهای ساحلی خزر را فراهم می‌کند و مانع از سوءاستفاده‌هایی خواهد شد که ممکن است در نبود چنین چارچوبی، به‌ویژه از سوی بازیگران خارج از منطقه، شکل گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/139173" target="_blank">📅 20:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139172">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
الی کوهن در مورد دیدار ترامپ و نتانیاهو:
🔴
اهداف هر دو کشور علیه ایران مشخص است ما یک فرصت رویایی برای سرنگونی رژیم داریم و آن را استفاده خواهیم کرد
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139172" target="_blank">📅 20:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139171">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقام‌های آمریکایی: دامنه حملات سایبری به سامانه‌های آب در ایالات متحده دست‌کم به هفت ایالت گسترش یافته
🔴
هنوز مسئولیت ایران در این حمله به‌طور قطعی تأیید نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139171" target="_blank">📅 20:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139170">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34401b5b0.mp4?token=V6cm1fs8Fs6dogziIax0VnPW9b4eINqyeRWG7-P5HWLFEPHcemwlJDlwwbE2Mw20axUBX9KgubH4OIr5wRQeODr0XmQpRJ24dgbBoTngQvCkfGW4HJhKcpo_HPx5oUYXgEHFetdPvPJ4pBDcqUcjGPb_R0e9cY2wL72KFf7nCH1kfGV0O3kaWDvrfIbEXfWrGpp-mQ-VX9KtCrJu4VpnP2ZFKghWZAqo8z5Kf1N80QV7PfOJalsMw92kqtBLB-hsFxQYCHjz3Zjb0XeXQqzKU8URSNuL8EctfRWst0-pKteF-DEn6nBioGaNGcmy6hM0eXt5wqBY0ijuiSbSDW9YlXRUD0xcv_11D0oAXUs9L8rbyLndy1cWEXm8RZpsxmwWEcpRvONoAE5vtavs87T6eGfGUiwVc9LzigeOaC-PKacLEoc7hL-CUE8K6s2JDjFxx8hUXzXA99jBmZlKVaQKE-sux7Z7Ngbc-p5o-Oj1rFT8lprjiVxH2Uj4iF6VoPC7Y8uBpC9X5KQv3C8UEnPVAmJPOyic1eVKeFYxYDqoK9_ujkCaenD7yoTO1-w0fGB5hcDVMoLnRoONJfBIoM6gzhzeRD7iJ-JuWUDZwEK8kKFLhRhiXuueCzLyMp4HojYeIwJamM2hPOT4D2u5wqQ6HDP2hsKvukUvTxnH7B9umgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34401b5b0.mp4?token=V6cm1fs8Fs6dogziIax0VnPW9b4eINqyeRWG7-P5HWLFEPHcemwlJDlwwbE2Mw20axUBX9KgubH4OIr5wRQeODr0XmQpRJ24dgbBoTngQvCkfGW4HJhKcpo_HPx5oUYXgEHFetdPvPJ4pBDcqUcjGPb_R0e9cY2wL72KFf7nCH1kfGV0O3kaWDvrfIbEXfWrGpp-mQ-VX9KtCrJu4VpnP2ZFKghWZAqo8z5Kf1N80QV7PfOJalsMw92kqtBLB-hsFxQYCHjz3Zjb0XeXQqzKU8URSNuL8EctfRWst0-pKteF-DEn6nBioGaNGcmy6hM0eXt5wqBY0ijuiSbSDW9YlXRUD0xcv_11D0oAXUs9L8rbyLndy1cWEXm8RZpsxmwWEcpRvONoAE5vtavs87T6eGfGUiwVc9LzigeOaC-PKacLEoc7hL-CUE8K6s2JDjFxx8hUXzXA99jBmZlKVaQKE-sux7Z7Ngbc-p5o-Oj1rFT8lprjiVxH2Uj4iF6VoPC7Y8uBpC9X5KQv3C8UEnPVAmJPOyic1eVKeFYxYDqoK9_ujkCaenD7yoTO1-w0fGB5hcDVMoLnRoONJfBIoM6gzhzeRD7iJ-JuWUDZwEK8kKFLhRhiXuueCzLyMp4HojYeIwJamM2hPOT4D2u5wqQ6HDP2hsKvukUvTxnH7B9umgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها: این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139170" target="_blank">📅 20:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139169">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VszP8knlkjk7yfwrIrvk2dsAy9OQoLF7ahkvtlIguu-X3-OLnNrnu_RWSWcGmHsxT5DVBeWL9899DhjVXQD3r-EcmJweLP6RPWE8Ogy0HbHgerSElU2PUbfZuaNArgdg_tbdGSkva0OMz_E7o6jknNJSbtbvr1NCLc72CXzXTW_dIEoiKjbX8Q_q5GA48St5NK_7FWvYTBYDF9eafuEYJX_ToERyqoDctznSEvGq4jYeyClOT-XnxbOh7y9z3WvctetmkdyQjOGaqYTgF43pfY-2x5ksYFnFjqYuJyADEh53Y_8KNPGBwhJ9hSb7bZ25KKoEs7I8Kg07S4kjnan16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موبایل سامسونگ A26؛
پنجشنبه 52 میلیون بود و امروز شده 87 میلیون!
فقط در عرض 2 روز، 35 میلیون گرون شده!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139169" target="_blank">📅 20:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139168">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8e8dae83.mp4?token=sa9JvhvRyZn289LlF691Xs2xUj9YpAETXlFO4y-pTVVgfjwMPWJulB1Vs2bKXB29JiRPttOXYYGsWvmtzytuC1esH0_XrgsDFg0LJ2sTVRscIV3FqXOFQoQceXOjabD1_fQmcoDX8NwNjjc9Kiq9p4Jg3ogi37a0VwO5yFjucxVacytFHw70P6SqMVcB-4CEyjoHd9DvdLMqDT0EA-LSFCPZbOOBuhjsLcA7U2uOgl-3nadyOXPdu0INPTFwx5s80XdXMrCkJeWxnOC7B1prjLGAIHe7rn1H-myXjGZJAN8k_lwtM9pEkdDqp1YzAIeJQ-lDJamvzMl-O_5xuUror3Ds-aAkehNlm0ppsryo5XqMSHJqpj9plAgR2t_6S0vHdXHtl0KJRsirr6m9ydqK9zfS6l7-eyFXoq-ykoBOkgGZDIRqqniJLXtj0Yyq0w4PjK55NScblm2wbpQxXdp4CsxKbzx8Uc8_vZZbX31YG_OtOqLRgLhS3Bz3iH77YM15O8bnj-BXqonEBxDGyjO8Rb46V2f1vtiLunWXMHQBphWV_56uYsIeg0tmCSDto6w_e199SThMOZJ-Dlh8GgyGyNzLi7hQruOxJCcbdrr64jLQjrOxIOsUpESVJZPEO9ONVb_FUN2Bk_2RCutFy297asNCNTK6U3RhJPnIqO7iW1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8e8dae83.mp4?token=sa9JvhvRyZn289LlF691Xs2xUj9YpAETXlFO4y-pTVVgfjwMPWJulB1Vs2bKXB29JiRPttOXYYGsWvmtzytuC1esH0_XrgsDFg0LJ2sTVRscIV3FqXOFQoQceXOjabD1_fQmcoDX8NwNjjc9Kiq9p4Jg3ogi37a0VwO5yFjucxVacytFHw70P6SqMVcB-4CEyjoHd9DvdLMqDT0EA-LSFCPZbOOBuhjsLcA7U2uOgl-3nadyOXPdu0INPTFwx5s80XdXMrCkJeWxnOC7B1prjLGAIHe7rn1H-myXjGZJAN8k_lwtM9pEkdDqp1YzAIeJQ-lDJamvzMl-O_5xuUror3Ds-aAkehNlm0ppsryo5XqMSHJqpj9plAgR2t_6S0vHdXHtl0KJRsirr6m9ydqK9zfS6l7-eyFXoq-ykoBOkgGZDIRqqniJLXtj0Yyq0w4PjK55NScblm2wbpQxXdp4CsxKbzx8Uc8_vZZbX31YG_OtOqLRgLhS3Bz3iH77YM15O8bnj-BXqonEBxDGyjO8Rb46V2f1vtiLunWXMHQBphWV_56uYsIeg0tmCSDto6w_e199SThMOZJ-Dlh8GgyGyNzLi7hQruOxJCcbdrr64jLQjrOxIOsUpESVJZPEO9ONVb_FUN2Bk_2RCutFy297asNCNTK6U3RhJPnIqO7iW1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هر وعده غذایی که تو مراسم اربعین میخورن ، یک نفر در اثر نبود غذا و دارو داخل ایران فوت میکنه.
🔴
آهوهایی که در مراسم اربعین سلاخی میشوند برای جزیره قشم هستند. همان آهوهایی که رژیم میگفت با صدای موشک آمریکایی میترسند.
🤔
لعنت به شما حرام زاده های حکومتی که با نام دین هر جنایتی میکنین ولی کورین مشکلات مردم رو نمیبینین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139168" target="_blank">📅 20:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139167">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121b4f43ef.mp4?token=YNLer4av89x5XMEMRVOHwiQpT2tfWCaSEHbSvK-NTPbVUc4751d1Nq1A7vg6uitid1Or3-FOWqkojRYwZllTSinn8QP6Pv2ImKtPGO4F9Wd6Vj-Qtte0kxlHJgirsbJ5OufxI5HErsVo1FuI6F2lfggCfwKHXHRauX4J3aXmCx2SAt7twIYe4rynbVzoZvRDhKdMVnQ9-pngTiY3C4JtyGXRefhYg2bN7a7M3xlBd7txOllFrVvihoVRF2WCU5fz8ImcQoCe8Kh3HSt_IbEDrkIOmWdY3w2vsPI-K-6JvbwruIHTh0ZI7AS9ljndGjI2F5sdg6EBalv5SriQ54NJgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121b4f43ef.mp4?token=YNLer4av89x5XMEMRVOHwiQpT2tfWCaSEHbSvK-NTPbVUc4751d1Nq1A7vg6uitid1Or3-FOWqkojRYwZllTSinn8QP6Pv2ImKtPGO4F9Wd6Vj-Qtte0kxlHJgirsbJ5OufxI5HErsVo1FuI6F2lfggCfwKHXHRauX4J3aXmCx2SAt7twIYe4rynbVzoZvRDhKdMVnQ9-pngTiY3C4JtyGXRefhYg2bN7a7M3xlBd7txOllFrVvihoVRF2WCU5fz8ImcQoCe8Kh3HSt_IbEDrkIOmWdY3w2vsPI-K-6JvbwruIHTh0ZI7AS9ljndGjI2F5sdg6EBalv5SriQ54NJgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ماشینا دارن خاک میخورن تا ما پراید سوار بشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/139167" target="_blank">📅 20:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139166">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
به گزارش بلومبرگ، ترکیه و عراق به توافقی برای تمدید یک‌ساله قرارداد منقضی‌شده خط لوله نفت دست یافته‌اند.
🔴
این توافق مسیر صادراتی را حفظ می‌کند که امکان انتقال نفت بدون عبور از تنگه هرمز را فراهم می‌سازد..
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/139166" target="_blank">📅 19:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139165">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ارتش اسرائیل: تعدادی از عناصر حزب الله را در ارتفاعات علی‌الطاهر هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/139165" target="_blank">📅 19:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139164">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ccfb85d5.mp4?token=Kd4OsRb2aMOLjmwWP2_rr7p1k7zntCAqy9AKwxOjPjYJYN_FCykJ3SwvWqIBfdfT7KhD915LdqzAMe2ToLtHLBKZMimzv6RrLV8_jV4Iqwrw_8b_PM1mwswl9FMtUleJ87zi5i8KMF5DRB6MAxkmR02o3KNNCzDm-HxgDS2PZ94F2mOJcqJXD66ROpZYVRIXEjR0PSguQ_48cMn28Q9RflSvdXzByse8wTRezJE4ZRJb_Vul62kaNm3HmzIwnCS2HhS_vx45HP7YqCULYuKRsDL6xAw76E3d8n9QkX_CHDms9YKMHyrqE6vXu7Cz_z8n8YtCcQwU9ud5jfr8Q5cuNl11VvEQ9FaMkOk9j-Tb_uHJ6boVkCeGO4dB9rFSxbQBc3ekIH1uFxEgP82wDbIFObwRzwStRKBLcS5Y3nDFdC71HgDe6pVm0j2opakHHjq3mB8x56WBVZMmBKSIgE1G18jdFR6IUP_5upQVr6qtVEGV7DCQjLoMs-_nyZOiG_Ebu2oUPncETJMMWUZ5m-fwZDc0xURuQlC7gijohQsjTm0uMLm3CF1Uh7dC8dQjZnRHGVd9i7LtNLVtFckxycmU2funE1aADnh5afEZIW7cTTENdvB0D-cMrPhLKubKBfr7m8s6_MRA3U-HKh_gr-JkjeE_5STyrtfOU1y6GyUAfHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ccfb85d5.mp4?token=Kd4OsRb2aMOLjmwWP2_rr7p1k7zntCAqy9AKwxOjPjYJYN_FCykJ3SwvWqIBfdfT7KhD915LdqzAMe2ToLtHLBKZMimzv6RrLV8_jV4Iqwrw_8b_PM1mwswl9FMtUleJ87zi5i8KMF5DRB6MAxkmR02o3KNNCzDm-HxgDS2PZ94F2mOJcqJXD66ROpZYVRIXEjR0PSguQ_48cMn28Q9RflSvdXzByse8wTRezJE4ZRJb_Vul62kaNm3HmzIwnCS2HhS_vx45HP7YqCULYuKRsDL6xAw76E3d8n9QkX_CHDms9YKMHyrqE6vXu7Cz_z8n8YtCcQwU9ud5jfr8Q5cuNl11VvEQ9FaMkOk9j-Tb_uHJ6boVkCeGO4dB9rFSxbQBc3ekIH1uFxEgP82wDbIFObwRzwStRKBLcS5Y3nDFdC71HgDe6pVm0j2opakHHjq3mB8x56WBVZMmBKSIgE1G18jdFR6IUP_5upQVr6qtVEGV7DCQjLoMs-_nyZOiG_Ebu2oUPncETJMMWUZ5m-fwZDc0xURuQlC7gijohQsjTm0uMLm3CF1Uh7dC8dQjZnRHGVd9i7LtNLVtFckxycmU2funE1aADnh5afEZIW7cTTENdvB0D-cMrPhLKubKBfr7m8s6_MRA3U-HKh_gr-JkjeE_5STyrtfOU1y6GyUAfHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با سربازان آمریکایی در نیوجرسی دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139164" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139163">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjfD09u_qNtVYfQjN0kSRiR_xX58cDe7x2tbmqID5c4pw9tOAPE4iUBEIMvYOs9it_g31PRVm4Sin82OnOtFlxq-jG7gTBkY9wprp8V6H4SBtcqqzJhd_WqjZ6wERKnoERaw1956CkoybdqNYRfrB9cnpNWrXDPmn3w_XAKZUKaZY11l9BOHyOOmIk7NzEJmXoElPgvIBZ6bhZrFT_yKrOscJHgVE2N3hEUGs9pF4imzZ6FCpvfi32LiHFz1z1h0B3kjtBNfSngX3Ug9O59K1GAiNeFi73362VE4ajRSfayDubl8iYQfdEaXRnwcTekLY5nBO7C_Ms53e0IFgihRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / کاخ سفید: خداوند سربازان ما را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139163" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139162">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رویترز: انصارالله گزارش‌ها درباره دریافت عوارض از کشتی‌های عبوری از باب‌المندب را رد کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139162" target="_blank">📅 19:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139161">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
گزارش های تایید نشده از تخلیه پایگاه‌های هوایی و دریایی آمریکا در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139161" target="_blank">📅 19:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139160">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شبکه CBS به نقل از یک منبع اسرائیلی گزارش داد که تاکنون هیچ اطلاعی درباره تجدید جنگ علیه ایران به طرف اسرائیلی داده نشده است.
‏
🔴
این منبع اسرائیلی تأکید کرد تل‌آویو تا این لحظه در جریان تصمیمی برای ازسرگیری جنگ علیه ایران قرار نگرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139160" target="_blank">📅 19:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139158">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbfLSIXJtIeyCC5l93eW-3tDXa9EC9x_3FbiQXfWIiRXNo1pv_6eZv9YESHQh02RQyKuQDuU_0q1BmoZ3aMYAIbrUmGXOMOitf2iLUcxNKuBLi3nG2-VwhsmjltplwuHiWtZOWhR6rP5j8znT2cWR0NRw2f4NE7FmOlX5GnNPgdc2edj2LlCUyu0WpR7NwBbYWw-JOh4uclJg3kY_XdRAqLrjLkI3dgRwGznGs9tXWuRrTNqur-OdllSMyVVuDOJWeVIkV9x2UAMbHO2fNPax89CruWJR_PTjWFaB3NVjmNna5-Tz9gewVktJBwhWPtFiTiSQnH_R9Ns5vK-0qKwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHUxGvJKCTK8OvpKfDQN-q9vG7oYkhPpBz7unifGnY2WGUsPUeLCkVLJce4Hh7GzlsUjcPEIhC3OkFfHZIUCOz5ZaMUYJBdVzWXDzpxMyDPgmWD3Gpu_flKK-F2LEZD2ie1AAOlELp46NSlfMMVDSUapj1b5y7f-bBaZ1wXSe1W4LX2kqI-pzZ4yNsAuH40BgpZZQrDmw7K1pduu3ffm8dk3njgvq-aJ_2HHL5HXejS4J3zT_H9snJml1VZP45S74KLyjbyAOpLBp_zySwzIdu1cihWzWur3Tka94BtODxkU8vIPJ7f29EgADPuEycYrNx4BeeMcg2uG4F7reLZXGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پایین آوردن بالون در فرودگاه بین‌المللی اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139158" target="_blank">📅 19:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139157">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hop42-po7pvoY2Ock_6A5cVgvdIp6QgEV_feyiucZIqvcS8iliccsILRH8_EF4oxiWn12WZthuz0HPbdOrwUIe3nbO1ntJUp8Hoa99MKKRJZI-mS2GcK4tGezd20p61i0Jn8KqOLQXyZ0IVzDss2FIhYXWWNA9Xp1xeW7E9tpgkfL8nIIsuKxTsSIjEwRtC2JJan597b5UWSIkflHExDamuteH1O2JM6hf3-ao6PvTfQCQAcUFCb2tMxEVRpNT8Ma5YfUJGcMd4117rb1FC5BSoFzC_oWYn4SRxUx2porPtOlLTcASfAvEpaYKfcs1Gol3FPJeezHer098Pb0f1qhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تصاویر ماهواره‌ای جدید از خسارات وارده به پالایشگاه جازان عربستان
‏
🔴
تخریب کامل ۳ مخزن نفت و آسیب جدی ۲ مخزن دیگر در اثر حملۀ یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139157" target="_blank">📅 19:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139156">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrCeKRcuuowSp1Xd8CPAqAZ_2HnCabbp0fqy3NKdJzjWlfls-imQfBFqHyGZgYFhDm_MepKu909lgUqEkaRa66DfAJDbypOX85EF8vxYu_FLSp_KA7OArSrT2hhBrqN36kU8diCtyl3egHFOnS2zxtimpPv2Kh49EePf1hPDq0o_xOzmtXH0hKSt3dGxQECEDElVJlAIBN5KlMb3fmKdScDX7AHpBu3sk9wgbuxTUfHr_1A_hS63WPiZ20mTE3X9BxGIlAyMWsFtMAgNTlazIFv4a7kfDjv0z-Pcr5L0RaNoOmhS40g_fqWNz8YlEvWT2g-XDtOW3MDSMVxVGVaLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست به ادعای ژنرال الکسوس گرنکوویچ، فرمانده ارشد ایالات متحده در اروپا، به پنتاگون هشدار داده است که دیگر ناوهای موشک‌زن کافی برای محافظت از اسرائیل در برابر حملات موشک‌های بالستیک ایران و هم‌زمان برآورده کردن نیازهای دفاعی ایالات متحده ندارد.
🔴
این ناوهای موشک‌زن که موشک‌های هدف‌گذاری شده بر اسرائیل را رهگیری کرده‌اند، تحت فشار عملیات‌ها در مدیترانه، دریای سرخ و اطراف ایران هستند، در حالی که مشکلات نگهداری نیز در دسترس بودن آن‌ها را بیشتر کاهش داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139156" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139155">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
آمریکا: ایران ممکن است منافع ایالات متحده را در نقاط مختلف جهان هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139155" target="_blank">📅 19:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139154">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_yMnHI0dLKcGotudxWrcOSZSYrVTRUXkweWF3CAH76CF8_nmW5vaCS2KwRhsyMImmXz_RUAEBfW2CsBrEDGSukvSYaqMlpl0jHh7dQxYaGmq5mUT3QI9JsvS1mh18gUN0MwARCwBKAlGkmoqeITRLPfFHpqxaOIvvkFXBJ9zxtYbP-Uvp3fdQUVLUXIpWyhdVpyE02nIqNYNDmykb9yJlxdvtB6gSlnxnfYSLtpuwwWOvoROtsTJURf87AZG9-Qvizyz_vtWaDqRTvHBWziz6UwK7qkEmrgwqsoFPbo5vwOgIAWdxyDKjcyY_QhxvRuKVwcGxSIn6qH8aPOv6iGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخبر: شما با معادلات نظامی محاسبه می‌کنید، اما ما با منطق تاریخ پاسخ می‌دهیم.
🔴
تعرض به زیرساخت‌های ایران، مستقیماً گسل‌هایی را بیدار می‌کند که ۲۵۰ سال معماری هژمونی شما روی آن‌ها بنا شده است.
🔴
وقتی ستون‌های این سیستم فروبریزد، دیگر نه مرکزی برای فرماندهی می‌ماند و نه بازاری برای غارت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/139154" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139153">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_RiPq1SsTgcmahTb2Wip-txas12gGuk33awmhp5vVAY4wr5Ty4Ecqzo2ddNygU2Qw00ZHnq4kq_1mQKQ7MF5fd9JCbmzenFKB4bmdPsxT069jXkfat55enu1rAyTqrkE9rOtxogt3eogXrJFauCm5mij-11pb6VgeymDZOyqQRLiXBAjWLBjJQ3NMn_9ejc6nr1X_urY-DLYmMzCnl1C5WZ2QFyueDn-4WojDr42gWe_RhoYaL7dE4Fl-je9Yn6i0YGJtPRSeUtDIW_Ja7BcNvfvg7nHdzWsQVoDwiNaTIpAGHajmPUtm1Mkab5pqq6duxvfutHZfj8KtM42TJa1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تغییرات سهمیه بنزین
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/139153" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139151">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f8511251.mp4?token=pduDALY232gW17KKT6-s73CbdufUb62U7HcW0HhOpnCuQfnDMdLo1doMDkbgWysmrODYhcPRWKe4cX9BWIALO3Cb2wJZMRJF-81xa9eqXIc4wpREKL_NCk8qcRLt-6bz_HqZ_f8IJd-19R8Au-Dj5HfDgCf4zBPE8MFjfgE0OIr6jZdpyh9dSHGtPVD7DoiKmjabq8-9ifymUdCiWpXBunQ-JhQfKwLL1ShfoLlPsBxMHfVo9_zI6S3dJTvakCyxNJ472dqMN0QasJaEHgF4CF4nDLzC95lbhUBNlA6GY9t86_6jl4PyyMurLI0Za6OOx_vnAlz7Eruq5kupMS74qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f8511251.mp4?token=pduDALY232gW17KKT6-s73CbdufUb62U7HcW0HhOpnCuQfnDMdLo1doMDkbgWysmrODYhcPRWKe4cX9BWIALO3Cb2wJZMRJF-81xa9eqXIc4wpREKL_NCk8qcRLt-6bz_HqZ_f8IJd-19R8Au-Dj5HfDgCf4zBPE8MFjfgE0OIr6jZdpyh9dSHGtPVD7DoiKmjabq8-9ifymUdCiWpXBunQ-JhQfKwLL1ShfoLlPsBxMHfVo9_zI6S3dJTvakCyxNJ472dqMN0QasJaEHgF4CF4nDLzC95lbhUBNlA6GY9t86_6jl4PyyMurLI0Za6OOx_vnAlz7Eruq5kupMS74qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله سپاه به پایگاه‌های گروه‌های مخالف کرد در استان سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139151" target="_blank">📅 18:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139150">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
در پی انفجار در یک معدن در دلیجان، ۲ کارگر جان خود را از دست دادند
🔴
‏یکی از کارگران در محل حادثه فوت کرد.
🔴
‏کارگر دوم با وجود داشتن علائم حیاتی به بیمارستان امام صادق دلیجان منتقل شد، اما به‌دلیل شدت جراحات جان باخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139150" target="_blank">📅 18:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139149">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uf4E3SWrSl4EhJYVPEcB8P7su1cuTVPDGI2PJxuyWszFheAVyHPFmtEucpmfQq1Sxl6-heEpxerM12Escnejy05iJg-ZHbYg6xYQFIMly4fRh7dwJydXAQOn96Eu0NttllriZr7qtqGZIdwo2YoEhpvZGQu4FQlm8A8-H89gl-s0EtTjNPCHvj9rHN1naRCjlw97vrr5Wec0mpdLSiUiW7t0Foy3j7R72FA3YmbzLHIECBOdxDh9FhqnSCBeQtEQVnyta9oCEjGK2cqi8ezpsn8C4zSjN9dO3oDVdnDAdeC54EudjJyM0qa_mpsOr_VQttmRKzyNTURFEvwQteLnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139149" target="_blank">📅 18:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139148">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سیتنا : اخبار منتشرشده درباره صدور آماده‌باش به دیتاسنترها برای قطع اینترنت صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139148" target="_blank">📅 18:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139147">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139147" target="_blank">📅 18:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139146">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
به گزارش تایم، بسته شدن تنگه هرمز تنها جریان صادرات نفت خام و گاز طبیعی را متوقف نکرده، بلکه عرضه فرآورده‌های پالایش‌شده از جمله سوخت جت و سوخت مصرفی را نیز با دشواری روبه‌رو کرده است.
🔴
این نشریه نوشت اگرچه افزایش قیمت‌ها و نوسانات بازار در ظاهر می‌تواند انگیزه‌ای برای سرمایه‌گذاری در سوخت‌های جایگزین باشد، اما واقعیت این موضوع به‌مراتب پیچیده‌تر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139146" target="_blank">📅 18:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139145">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گزارش ها از وقوع چندین انفجار در سلیمانیه واقع در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139145" target="_blank">📅 18:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139144">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrAk3IALVhnXvhtKDBeOuA1K9-loPbNgHaVDZrC_DIB-wSa4T_paG5NMVHui1q9-zRcvXp7EnxlcA5ydAfCRAvd74210AqQdVtBKmW55hr8OewtkXzJPofKi-iDP2YWXWH8TbkbL6a1iJxcbLPwFI8B7ZIUS7pGlAphuv8AFNH2RvF-CnNCskaTasdUVyCSrl_xZ-viZEGMZjb5FkTQxJzbas7qBYtxPxu1IWf7C6MSZniAT5oaOig8TTh0FV22z1N_sG3Gk9MFxBTzRuNsZcwiTWrt1N4u-sDj08ec4Yv8Y8wh4lCwc1Zx6DR6wT8JV4lUpMldOnquSKsu2L6Thig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام اسرائیلی به واشنگتن پست: تا وقتی حماس خلع سلاح نشه و غزه کاملاً غیر نظامی نشه، از خط زرد عقب‌نشینی نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139144" target="_blank">📅 18:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139143">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4xLOsORufRWI_dmgJtNc15OfMaeSEL2qxomOOTQgXRghwj1ZhdOMegAVthdEx6LsdNKXHuBY7CeUn4cApAuwkq2sqjGhKHVuwpAAqtkgNwkjFiI7w7ZQyuBx9bYg30OI7Cp4tqoMqDm9D2ttgrqrU9u9_fZcMprBthqgYi0YKCZWNLNn5X0KDdSsGXzjmXOIZam8K_kz8Z3fNSiik0GQ1oSXPvv9YLpPH3p0jbjwI8GiaXQMvtkBampSaytbhAD11EYOk93FJcI0iDR34exQKLPCyPxVVdlRbvYal_3r0T51v6hH8Ajmmz4nMcspe9IOQ5OCR71QODVAUNiGeI_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید:
امروز هیچ اطلاعیه‌ای برای رسانه‌ها منتشر نخواهد شد و ترامپ هیچ رویداد عمومی و مصاحبه‌ای با رسانه‌ها نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139143" target="_blank">📅 18:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139142">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myv12aE6JFxTv9VK9upj-w1pFTNOgchSqrwd_cu8XcyNZrgGYT6HYs3tr98umZlhrQe57IbyFCodl6BXzMNEZdPfCgDSJ_0ukxcPtr_km8_V2iEpF_YaipwLsj97TB5vVIK3Jmm-5BrxRRPeM17B1Vco948S3bwxr_7nTYeQ3XzseuwiCHTiOitvqF7x-TNEw_epZatyAa4kyjht711NlGNN6et91vcwRHh99L8EGhWHLDAtPAGT6N2MwzNG-xBJEAX7rMvTcXiZqA4twQEnzZ89eIOmm2S9PUp5d3SqorEzdfh98CglAzh-wuiYvJfUE2VkLNoWK1WHzsu8V91ZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سوخت‌رسان‌های آمریکا تو منطقه درحال افزایشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139142" target="_blank">📅 18:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139141">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
اولیانوف، نماینده دائم روسیه در سازمان ملل از آمریکا خواست تا به میز مذاکره با ایران بازگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139141" target="_blank">📅 18:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139140">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49864c315c.mp4?token=Dby-gNPKudGlE5N708wHJ2a2pDAffeSYvAfyza_H5OOFy3jLrbjt20_KHNa9XZ_BKfxTA6vw68oMGMBnXKxWzMeVEwFFZlm_pm0gxzmJMFgXo_R1uR_Zg-IEUvnL7l7W-jtrTWCHmesmC3To4L8z70CZ4YLzyC4sPELuQwHtxtwSP3tFN6zzY4vSTHkTyeBRIu_k95twPljDn092bxjE0gMp_EGYeIEx4Uwt-KBLFMdj_AMnt773rKaKyaZtcP2l1e4pbph3sXM9IObRYA3SpnrWMn6zNjAqFABCFSllRKGeUHrpvn59FdTww0Yp8xuU7kGgma48LWtm8DOCzOLSsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49864c315c.mp4?token=Dby-gNPKudGlE5N708wHJ2a2pDAffeSYvAfyza_H5OOFy3jLrbjt20_KHNa9XZ_BKfxTA6vw68oMGMBnXKxWzMeVEwFFZlm_pm0gxzmJMFgXo_R1uR_Zg-IEUvnL7l7W-jtrTWCHmesmC3To4L8z70CZ4YLzyC4sPELuQwHtxtwSP3tFN6zzY4vSTHkTyeBRIu_k95twPljDn092bxjE0gMp_EGYeIEx4Uwt-KBLFMdj_AMnt773rKaKyaZtcP2l1e4pbph3sXM9IObRYA3SpnrWMn6zNjAqFABCFSllRKGeUHrpvn59FdTww0Yp8xuU7kGgma48LWtm8DOCzOLSsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آزمون ساعت ۷:۴۰ شروع می‌شود، ساعت ۷ در مدرسه را می‌بندند؛ چند دانش‌آموز ساعت ۷:۰۳ دقیقه پشت در مدرسه مانده‌اند و به آنها اجازه ورود نمی‌دهند
🔴
این اتفاق والدین دانش‌آموزان را به مدرسه کشاند و باعث بدحال شدن چند دانش‌آموز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139140" target="_blank">📅 17:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139139">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
فارس: یک کشتی حامل گاز طبیعی در تنگه هرمز هدف قرار گرفته شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139139" target="_blank">📅 17:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139138">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
فارس: یک کشتی حامل گاز طبیعی در تنگه هرمز هدف قرار گرفته شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139138" target="_blank">📅 17:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139137">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_9GNFhH7bIZhFGkoiwYWmZxPgBzkUQ50DTSpJ_K_86p5YjPOfzjNNQmj0q2oFRPdl9Vwx5oekI6gvC33lBpqsfFjYc1ZjNsAWrgKTws7u_e2_nu8iSslYvpig47_e1f7EwpRY1r7fWccEKMdFeNAdu0n-CoTDB4GvHqmHVWNGeI0iH3-WIap0UnmiHURpkR_I5otLTHygQsuTXatodBBUTEvNPvTNOc8NseqYCQHoE7g32cCOfpa5RNWLX_AA_4qJ3p59J1BpqfgpPTlhOz-GFr7O0WokTbLSThFxB2EMWZVnmOokHukNxgyYs0w8587t3NHhENxQdzvZT7E0lH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تحقیقاتی از سوی خبرگزاری رویترز نشان داد که شلبیت، یک صرافی ارز دیجیتال بدون مجوز مستقر در دبی، از ماه مه ۲۰۲۴ تاکنون دست‌کم ۴ میلیارد دلار تراکنش را به عنوان بخشی از یک شبکه مشکوک به دور زدن تحریم‌های ایران انجام داده است.
شلبیت دست‌کم ۱۲۵ میلیون دلار مرتبط با بانک مرکزی ایران، ۲۰ میلیون دلار از عملیات‌های مشکوک به استخراج بیت‌کوین در ایران و ۶۷۶ میلیون دلار که به بایننس منتقل شده بود (شامل حدود ۵۴۰ میلیون دلار پس از اقدامات اجرایی مقامات نظارتی دبی) را مدیریت کرده است.
این صرافی به بیش از ۲۰۰۰ وب‌سایت قمار فارسی‌زبان، بانک مرکزی ایران، نهادهای تحریم‌شده ایرانی، عملیات‌های مشکوک به استخراج بیت‌کوین و کیف‌پول‌هایی که اسرائیل آن‌ها را به سپاه پاسداران انقلاب اسلامی (IRGC) مرتبط می‌داند، پیوند خورده بود.
سازمان نظارت بر دارایی‌های مجازی دبی دستور توقف فوری فعالیت‌های شلبیت را صادر کرده و در حال بررسی ادعاهای مربوط به پولشویی و تأمین مالی تروریسم است. وزارت خزانه‌داری ایالات متحده اعلام کرد که از این ادعاها آگاه است و آن‌ها را «جدی» می‌گیرد. رویترز نتوانست مشخص کند که چه کسی در نهایت این شبکه را کنترل می‌کرد یا بخش بزرگی از پول‌ها به کجا رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139137" target="_blank">📅 17:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139136">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کشورهایی که توسط سفارت آمریکا به شهروندان آمریکایی برای خروج از آنها هشدار داده شده است
بحرین
مصر (بی‌سابقه و برای اولین بار)
عراق
اسرائیل
اردن
کویت
لبنان
عمان
قطر
عربستان سعودی
امارات متحده عربی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139136" target="_blank">📅 17:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139135">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: آمریکا جلوی رسانه حرف الکی میزنه، اونا دنبال مذاکره با ما هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139135" target="_blank">📅 17:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139134">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-eTIJfUU4NSG7mCj0jvEjeXEOj6r2O1s14mTbuSDYF6HBBUfv6RqbKImL4P74RGt8m3sLOitt-FQbWCfnIow5fgKMqDp6d6yRYiR435LWs_oz8Eawuq3RrTizX10VdQaZbDchqsvS6WGJTSO-FiM67g3fEh5nvcpbPOFsqI0V6bz0StQE0mYmbXBec6tyCBWulYZymZAfOXdrasnbffkrtta9asqoh2YWG3hK6hEXibAIfauJfEsTt_lr59YK1yNO5LNj8d3EfcL85PhnbfW2ccvsmAl2G8gEkUca7c0GDJwwExOIitKlHvYVBMDxD-mUQ9tPRoHB5lsL89j_UJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعزام تانک‌های ارتش به جنوب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139134" target="_blank">📅 17:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139133">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52322b2b53.mp4?token=ew2e7kA8hbzhFDpZmg6p5TTKflSahHANcUvw5v9dh0VO6W10SGPOLYMDcQvamISh7reH-OAOYKlwwy44b-4QuqQghVsZYhcPCJ0S1f66rdlLSgz9pNTZfR1iMK2C-ynlHlWWR6wgIYzmqUpHF2y-IbtQ6wLWw4-mcuvQFP_EhIyK6vQu2KAj_PRXeiHiFOSkVEgAcQBviTSvK-GMU6zNWx07Seo1ccVqYoNxiqfPWZ1NcSt73iLQHelQOrd_EjvVsaiVFc9pqSV265Qk9yoob4b6CL8MHqbTFYWueefkyXEPtqmiOg7kFVl3izBO3A8FT3OC_xVQ-i0pNWwycHLcc6tA5IIPC2fjLo23FinRpO0_WWwGF76d5noCQawpdiiyDBvHQ6I3c0G94orddmurXKeHt5lnu8CfMmBoKY2f3o5MCg5eNBe7kk6QD4iaEW7u4tEd1IL_He1Q8_X_JuJS0PV4tDEQGuGldFAW3vrnUvGZXlDPQ9Pf8VB7um65cdEUlUEmC8NSlQOg2hvD9xMNZJC1Vhba2IuH6wjdZ3MxoGT9SK7JEP2WYK8aaehg4_2HSa8AiWxQvbt-kX5_T8HRhI_IM49R8SDJ-cponQgioLpYMUs6UEgp3VgaW4Bl7DicpnGrmgkfvuKBHZQ021Ulx8Q2arS1-Ht6VfcIbyRLTVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52322b2b53.mp4?token=ew2e7kA8hbzhFDpZmg6p5TTKflSahHANcUvw5v9dh0VO6W10SGPOLYMDcQvamISh7reH-OAOYKlwwy44b-4QuqQghVsZYhcPCJ0S1f66rdlLSgz9pNTZfR1iMK2C-ynlHlWWR6wgIYzmqUpHF2y-IbtQ6wLWw4-mcuvQFP_EhIyK6vQu2KAj_PRXeiHiFOSkVEgAcQBviTSvK-GMU6zNWx07Seo1ccVqYoNxiqfPWZ1NcSt73iLQHelQOrd_EjvVsaiVFc9pqSV265Qk9yoob4b6CL8MHqbTFYWueefkyXEPtqmiOg7kFVl3izBO3A8FT3OC_xVQ-i0pNWwycHLcc6tA5IIPC2fjLo23FinRpO0_WWwGF76d5noCQawpdiiyDBvHQ6I3c0G94orddmurXKeHt5lnu8CfMmBoKY2f3o5MCg5eNBe7kk6QD4iaEW7u4tEd1IL_He1Q8_X_JuJS0PV4tDEQGuGldFAW3vrnUvGZXlDPQ9Pf8VB7um65cdEUlUEmC8NSlQOg2hvD9xMNZJC1Vhba2IuH6wjdZ3MxoGT9SK7JEP2WYK8aaehg4_2HSa8AiWxQvbt-kX5_T8HRhI_IM49R8SDJ-cponQgioLpYMUs6UEgp3VgaW4Bl7DicpnGrmgkfvuKBHZQ021Ulx8Q2arS1-Ht6VfcIbyRLTVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل : ۵ انبار سلاح حماس تو غزه رو منهدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139133" target="_blank">📅 16:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139132">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTUJzNHf2fcuUmR2xQ-hxZstz6bDc7MQY8WmopbeZudP-aEURU4dydmHOKSRXhzqgc3LlEsKKVJvxS_NMmYLlg7iy_d9OppTMii2MTBvc194lixZ0xujVbCOee6pcwaSYnsmHnC7uLhqaWSO6vDHmpPQyKJpq8WktvT9MasbaSlugl4e40ltY0WisGCzK9QhhbKeL10V9BTGZyuG1AMcTukwiGP9JSPwfAmunMONvDH-F-mHyB0qyfRhLPWI2dFT9lXOAy9p_MvP9FWT9ksW26zzKHCnSmcVotZrZQjGEAZ7gEDEbi21z31xEedEKz8mcMQkpYdndpo81K0HUVnfsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نورنیوز: حمله امریکا به زیرساخت‌های انرژی ایران، فقط جنگ با تهران نیست؛ قمار با امنیت انرژی جهان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139132" target="_blank">📅 16:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139131">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f255af304a.mp4?token=b_gehumb4Fi-HaI_mNrjQqeTEzKM1W6dMxnMN5I3l_0NgZtb5cF2Wq3zBhQdCjmoj57DViayhU8A6yWccvEXWxarey0ciMQ1OeSL667TLO8nSUh9dyBeuIBjGUwwSw_rxQ0Bfgh4YX1_t5AJB0E0G1-uY88iPgnPtSMkIEKMwZPI-RbHR5F2KYYrAoBSKZbHAK3jOuuwvWYu-yGk_V16SWnZUPqMO5FyF1uJPIYleCS2mNctJZ0OvpxrJ814VJu0AyP-o_oZYQgag3R6wP5IS0p97Y5ZXaAnx1HgeqLQ6CvHTpe6fh1Gy05u4qBb8KgGp7R9PcAWZ1lZvW1rduH_wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f255af304a.mp4?token=b_gehumb4Fi-HaI_mNrjQqeTEzKM1W6dMxnMN5I3l_0NgZtb5cF2Wq3zBhQdCjmoj57DViayhU8A6yWccvEXWxarey0ciMQ1OeSL667TLO8nSUh9dyBeuIBjGUwwSw_rxQ0Bfgh4YX1_t5AJB0E0G1-uY88iPgnPtSMkIEKMwZPI-RbHR5F2KYYrAoBSKZbHAK3jOuuwvWYu-yGk_V16SWnZUPqMO5FyF1uJPIYleCS2mNctJZ0OvpxrJ814VJu0AyP-o_oZYQgag3R6wP5IS0p97Y5ZXaAnx1HgeqLQ6CvHTpe6fh1Gy05u4qBb8KgGp7R9PcAWZ1lZvW1rduH_wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
یک هواپیمای جنگی آمریکایی در حال پرواز در آسمان شرق اردن دیده شده است.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139131" target="_blank">📅 16:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139130">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
مدیرعامل روس‌اتم: حمله اوکراین به کشتی روسی در دریای سیاه راهزنی دریایی است
🔴
همه ۱۷ خدمه کشتی که محموله‌هایی مانند مواد غذایی منجمد و مصالح ساختمانی را حمل می‌کرد از این حمله جان سالم به در بردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139130" target="_blank">📅 16:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139129">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پرواز (گشتِ) جنگنده‌های آمریکا تو شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139129" target="_blank">📅 16:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139128">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا، جورجیا ملونی، و رهبران 21 کشور عضو دیگر اتحادیه اروپا، از جمله نخست‌وزیر دانمارک، مت فردریکسن، نامه‌ای مشترک امضا کرده‌اند که خواستار اقدام فوری اتحادیه اروپا در پی ورود گسترده مهاجران به سبوتا است.
🔴
این نامه از ریاست جمهوری اتحادیه اروپا (ایرلند) می‌خواهد که یک جلسه اضطراری وزرای کشور اتحادیه اروپا برگزار کند تا اقداماتی را برای تقویت مرزهای خارجی اتحادیه اروپا، مبارزه با مهاجرت غیرقانونی و قاچاق انسان، بهبود بازگرداندن مهاجران و حذف انگیزه‌های عبور غیرقانونی، اتخاذ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139128" target="_blank">📅 16:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139127">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بر اساس گزارش‌ها، یک رزمایش محدود و در مقیاس کوچک با مشارکت نیروهای مسلح قبرس و نیروی هوایی سلطنتی اردن در حال برگزاری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139127" target="_blank">📅 16:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139126">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
واشنگتن پست: ژنرال الکسوس گرینکویچ، فرمانده ارشد نیروهای آمریکایی در اروپا، به پنتاگون هشدار داده است که تعداد ناوهای جنگی دریایی کافی برای محافظت از اسرائیل در برابر حملات موشکی بالیستیک ایران وجود ندارد، در حالی که در عین حال نیازهای دفاعی آمریکا نیز باید برآورده شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139126" target="_blank">📅 16:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139125">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsfXSk4eRAXcURkkuIKBce4pr7c3BU39aUtdkQ5Cq9gh9fnuU-oX7qwqG2P9RL-HDVn9Ebk8DeyZNKM2SbUJH-UrEvPgsvDOgMj6lwVLRQK5XVK2GeSqeHv_IAUtZ907TDUSSI5TlEfR1YZbQ0sBmOHb7dT4hjjrcH2MZ6GonmLmhSYtxN_QMwCrFxf-KOsvRoKra_gGPrytTGJmDSnIc2tCbjwSZqKm755xrHxG0HwQyTa6W_CEFu2zl_l7Fc6Pup11zVmCu-Os75uh8Xl8BDxARAf-zRke5xrDuxjmXoypixn1BnkrNNOiVyFptEj96CmFJqtDZPisp-dprR6lcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌بی‌اس به نقل از یک مقام دولتی:
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/139125" target="_blank">📅 16:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139124">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb82625a1.mp4?token=fgtHd43gnh7WoCCxzy05wFsy5iipP5XK_hflwrrzikWPKXnoFpnDjkvhASrUIB12MCju1IJmlblKCcKpx9fai5VaisV_AkW4TT09r_Wxw8yNSsVYuvJxJ26G7wntb38rpBNPjXfL-SqcnaPZnsOM7zLEACrxACvdQafN6R4VrlvYqvXmA91C4HZBLIwBJeAn6o7JSM6jCiMYCFawTN31BBn7VGYvc9MWBDvCRmhSZwzyiO43EaouQGvf10PPBPVT0DxpJm8RDaxdFTEQ8Gi4hAG2dPoemoG_a_h_I8At-ly33qct7COWlstCF2pI03WlZ0lrwjhBUt9xqzAb_3FASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb82625a1.mp4?token=fgtHd43gnh7WoCCxzy05wFsy5iipP5XK_hflwrrzikWPKXnoFpnDjkvhASrUIB12MCju1IJmlblKCcKpx9fai5VaisV_AkW4TT09r_Wxw8yNSsVYuvJxJ26G7wntb38rpBNPjXfL-SqcnaPZnsOM7zLEACrxACvdQafN6R4VrlvYqvXmA91C4HZBLIwBJeAn6o7JSM6jCiMYCFawTN31BBn7VGYvc9MWBDvCRmhSZwzyiO43EaouQGvf10PPBPVT0DxpJm8RDaxdFTEQ8Gi4hAG2dPoemoG_a_h_I8At-ly33qct7COWlstCF2pI03WlZ0lrwjhBUt9xqzAb_3FASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار مهیب یک کامیون سنگین در روسیه
🔴
یک کامیون باربری بزرگ در بزرگراهی نزدیکی روستای «مارچوگی» در منطقه پرم روسیه منفجر شد و شعله‌های عظیم آتش تا دقایقی به هوا برخاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139124" target="_blank">📅 16:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139123">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Zh3pZ2Shu9VAlz6MJXdQzamggG7MTfxzihi6VwopDoXirwbLnkHSslb27sW_WqeMii4g4ZU3C1ZjC4cu4S8yebu3btoE-OS6_VDVmPpuED9qkOw7hXWFTo0mzXPNKOxE0qjF5UYm7Y7HlS6oAUQZJ-yPG_jPmGlBm0dlcuqJu3MVHWesk-NOB6zRYFlLaca3Vna_8AujizVJ6Gz6PjExvZlEF5CIkSq66Ab347PT5jbSMfB_0GMAAp0DnJaRmYTwYdQq5Vi12cacEy8XivudmsI5E4_4mN3nbI6yK-fHSDpGcoo83XZFomNKhfai70pKftfjX7F8Xx9U5qAXMwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز صبح "آروین خیرخواه" جوون 20 ساله‌ای که تو اعتراضات دی‌ماه دستگیر شده بود، به اتهام محاربه و افساد في الارض، تو زندانِ شاهرود اعدام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139123" target="_blank">📅 16:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139122">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxop0oZji2h9BKE72o09YlrMiPDxShPnTss3nte_xtjdPf-dODd6BhsLXIxmfoIQXt6SkTtcU5XHBfgZ2Ie2_y32jCALVWtN_NPPWGbEd07weY5u7MWBNsYoML7V6wjp9hrm3O4ACdb9pJWP8xKaWGk1vAnAPIRvJf4SSk_DzPTLFJZ6994q35afPWyfgF-TXwdegsFBOBqWLLtANkc6L3blBxf72QNnc9f1Kobn04wwljYHktoA8o2EUweiDIuQt2yfyttoI6XEuyM651TSQV-jbLhcVShy-Mqo7o6PtSzS6NZ-QMIjKc9qQPAuuI6dCsvUswfHysAcA6XHpc55Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از رذل بودن نماینده‌های جبهه پایداری همین بس که صبح تا شب میگن جنگ جنگ اما پشت پرده دنبال پناهگاه مستحکم هستن و مردم بدبخت هم زیر بمبارون
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/139122" target="_blank">📅 16:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139121">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
طبق اخبار رسانه های داخلی و عراقی ، بودجه مراسم اربعین سال 1405 مبلغ 137 هزار میلیارد تومن یا 730 میلیون دلاره !
🔴
این مبلغ از ردیف بودجه عمومی برداشت شده ( دارو ، غذا ، آموزش و پرورش ، صندوق بازنشستگی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139121" target="_blank">📅 16:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پدرو ساچز، نخست وزیر اسپانیا، کشور هایی که مرز های خود را بستن و قرارداد شنگن را با اسپانیا به حالت تعلیق دراوردند، خود خواه خواند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139120" target="_blank">📅 16:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139119">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اندی برنهام، نخست‌وزیر بریتانیا، درباره فلسطین: به نظر من، حزب کارگر خیلی دیر اقدام کرد تا خواستار آتش‌بس در غزه شود.
🔴
اقدامات بالقوه‌ای وجود دارد که من در مورد سکونتگاه‌ها در کرانه باختری بررسی می‌کنم، و این موارد مورد بررسی قرار خواهند گرفت و در زمان مناسب اعلام خواهند شد.
🔴
یک فاجعه انسانی غیرقابل توجیه در حال وقوع است. ما باید هر روز به آن فکر کنیم، بررسی کنیم که چه کارهای بیشتری می‌توان انجام داد و حقیقت را درباره آن بیان کنیم.
🔴
شدت این فاجعه انسانی غیرقابل قبول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139119" target="_blank">📅 16:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZe3VcqvG-vPvQZh_twWIx-aBf9bwfB7cJcchj8IQp8iULpQZA0B_1riBgMko2OZ-H6vdRiXNB-LjqTO15vj4Ky2uj6lUVDTml-douZnuOZfItzjaEKFBLWBmwMjhavMjFOZefGQHPYmdCPhoa74MLUYFOlB6i4eFsHayMEbp45ACY6cppSbrxoO-dItUVDvo2klYJ_tIpKZqn1c1BJiCyHAtNfdnaynKt1jBzyhx6QljkOYPY0wyAsR6r_WCo1ve5zwGvOPkPnaLkKp2hTN4Dqhu72X3aKhpdHw1lxxbA3XndlpvgJip_NCPGZgJ6VoAqJCPNlVAQW_4bblO9LF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPiBw4CVwofGAy7QBCfGlIZ0nhu5lIOEXikbxhGLO4lF9gvpUDlIVtu-zZRAnONhLnGonSptUohZuym5u5eH5VnWIEnOTBW7Ra8upcaqvLkjAUOJ8fc0QhGOnl-p7dBZRq6lOaFdkc7VyA8SoHE2YwcJbFy6GmlY_OWSfELXkXo6K6z77R8K3sAwrtynOtmyaxIL3PmjzS1UuQt9QLIK3l8w5asGveKGwfoFw1nF3dGaHdJm7sPhVPNJ3VJ1zwCKkWHwhK3gDDitAZ_bSlRV67KyPmw78Kbuo8NT8NYlvOMYeBUKD_wsH3JbeFy922mme8GN4mf7ExtZlHghiUhsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3jf2KHLHDcZTvt29qPwGfe2UWT30KzJ55GqXg1ecOPS3ZXywskBCoW1rYQj6nU5G37JC6APPlvUCAo1z4sVMMGDbHVaoYJbziy5EPBISr8dPG3uf87miNf1ZazqG8f9K4nbv2cqeQ-jKpg6bVnjhFWGMrpfPzKCHfzPaVM-ZqES8_Xr6umkHLolKon-yzLPS_Ovy2rk0hfMXGPX1jLKsfT8Kiah1i12_aN6AAh33WW-g_P0ub3GLagt4wWezSokoZS-b6MKdSon4nIGLoWnNGnsAa1UC1LdRdL5mp8bQ05RYMJ5Lw5GSEs-cAk3K1DRhvxKu0OmAIg30cv2cD0HkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید از کیف حین حملات موشکی روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139116" target="_blank">📅 15:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e99e305a.mp4?token=vvKIycj0CHe52HjQjc9JKhLVEjdGcC5MaMcERYVEIV9KobPb79yYmeYmNskpEsHcgeBx1SgHoBo00D0Lm6WCaid67hlWBCrZvYhXz4DwwiLkrNmtkwtqpnEB8CNVoFy-f5-kr87Gm54JyVzbPZ-BGuUll1bODBpLM3IsRWoqmOE7wO_vmF9zS4pZ4JXChp0XrxuzXeemCGBq9WwMNNBWTL50Oj5a0DkfKQOE6e-kljMlVT0Ql_LZbuHZ5kzlcQoVXH66bXJ_69kNjcQfX-eMV_1dC4_KZGMWwUEyuaNJnQ76cCaZkMpH_PFqIO8LLOquZ2DpQC4nnMJfJ5T4gAj9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e99e305a.mp4?token=vvKIycj0CHe52HjQjc9JKhLVEjdGcC5MaMcERYVEIV9KobPb79yYmeYmNskpEsHcgeBx1SgHoBo00D0Lm6WCaid67hlWBCrZvYhXz4DwwiLkrNmtkwtqpnEB8CNVoFy-f5-kr87Gm54JyVzbPZ-BGuUll1bODBpLM3IsRWoqmOE7wO_vmF9zS4pZ4JXChp0XrxuzXeemCGBq9WwMNNBWTL50Oj5a0DkfKQOE6e-kljMlVT0Ql_LZbuHZ5kzlcQoVXH66bXJ_69kNjcQfX-eMV_1dC4_KZGMWwUEyuaNJnQ76cCaZkMpH_PFqIO8LLOquZ2DpQC4nnMJfJ5T4gAj9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز به نقل از مقامات آمریکایی
:
احتمالاً این حملات می‌تواند هر لحظه، حتی در پایان این هفته، انجام شود. در حالی که ایران اعلام کرده است که در صورت حمله آمریکا یا اسرائیل به زیرساخت‌های حیاتی، آماده پاسخگویی خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139115" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a63b8ad888.mp4?token=cSJojMCZAKOc58dZlbU13I3pw54dwkJABg-72_X-wNXk4GO64cEahDmSQSANAGFmnB80ikokA-ldgn4eTr9L7d1On7i_8Vw5OjcApAeCi4YDdAJv4nukWlsLHWRTl-gpnisl6HwSKPEJSOTDk8iAtYUu-cvoqII0LBToj7xTjgBE5oClcfEhtyFKtiBwKZVbB-O58FgKo92I678-VJ_0XKqnzDAK7yuOFpVQWMmQMSd7M77kiCA0CyVTTB65IT6eDt5ZLh2nHIkEPJVIvSbrwjhlV5iUjFpOPOAyoIQekIPm3_UyCos3_AQuYqm2R4HMW7I20SoqzBe104ihvrEbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a63b8ad888.mp4?token=cSJojMCZAKOc58dZlbU13I3pw54dwkJABg-72_X-wNXk4GO64cEahDmSQSANAGFmnB80ikokA-ldgn4eTr9L7d1On7i_8Vw5OjcApAeCi4YDdAJv4nukWlsLHWRTl-gpnisl6HwSKPEJSOTDk8iAtYUu-cvoqII0LBToj7xTjgBE5oClcfEhtyFKtiBwKZVbB-O58FgKo92I678-VJ_0XKqnzDAK7yuOFpVQWMmQMSd7M77kiCA0CyVTTB65IT6eDt5ZLh2nHIkEPJVIvSbrwjhlV5iUjFpOPOAyoIQekIPm3_UyCos3_AQuYqm2R4HMW7I20SoqzBe104ihvrEbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش یک هواپیما امبرائر ۱۴۵ از باند فرودگاه شیراز خارج
شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139114" target="_blank">📅 15:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به خان یونس در نوار غزه باعث زخمی شدن چندین نفر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139113" target="_blank">📅 15:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری / گزارش بلومبرگ، یک نفتکش قطری حامل گاز طبیعی مایع (LNG) به نام گاسلوگ شانگهای، هنگام عبور از تنگه هرمز، شب گذشته در سواحل عمان مورد اصابت یک موشک قرار گرفت.
🔴
این نفتکش در ۲۷ جولای گاز طبیعی مایع را در قطر بارگیری کرده بود و در ۳۱ جولای در نزدیکی ورودی غربی تنگه هرمز، ارسال سیگنال AIS خود را متوقف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139112" target="_blank">📅 15:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139111">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
برای اولین بار، سفارت آمریکا در قاهره هشدار امنیتی صادر کرد و از آمریکایی‌ها خواست منطقه را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139111" target="_blank">📅 15:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139108">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JY4S6HnFkB4njGjkncl1r2McbEUkxIzY62bBGiamTTU6CqpPErz9r274PuGUR1v-JRc6n5GyCo4SrLAllf-kMCXhXzD5oLtv877nTr6Pa55iLyUKRZDt78w3JeJ3X1l-0GXDnRHRnW9WmZhR88Jpk9BzxTgtkEdpL64XpjEMYqvo60mR_Mzo7PWexrZhMOagqN4qvqRachQve0JQmv86syWEGqcZEzTvFvS6d6SafAstgpt9gqdYBl8flXWwcLF5gZPTMofgRFRvhOcqFQ0JLEQRW6tCBh7LbFAnjaeaWxM57iZeS-xG8e4zxS268rd4ejXZtYweLOGov6fS1V_5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIJblLgb8AyDtVcvXezpplLgNkiVzxwkjD-XYpmAXWXK_nhv8Xlv82tF5CDXXamAtKCoiIEzhWvRawIzPtnXa63k_-cULL2xgg9ZNecGPvYufEe3-z9AFq5VBNmxsLlxGqk0IQJS14FVOVTiw9som9ojmkr1YTSkCL-1iz-8Ee7OzAfDlLuc5e7KnMqogGDwczftk6zIhKk-1cbdeDSJXkwZyPlxphTuYdrtcX23C_7UloTbQuZG0ndofoxADmBYPKJCdkd1jlEhzPt9vhzQSNyfMTqgMWz77So4mbKUGK4yu-YjagdbyjePk7EYNESKplGapiDIqHwqSNv6cCUR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uh5mGvPDmt6yDJYItJddLMW1mPf1d5opPfHcgexdBD4fpiUfSNL4-s7OLnIo8SHDMLbc1laNn86VwWOx5wb65FAWE9DvSRDqDlRkQecJFFcDJksg_Azkr-DRiZJfu_O2bIO8cSx9SATY7kiiJKVdSouj9Mua8Q_K3IplDyGr6BHYaR7Jj_icCDcfuYbVpCyqvt6AnDl9aT_L9E9NkxYMODpjR8fY65R50OFvtdIvh8gPdAgXVdgytV1SkdBCUS4Yxo4kiFmrAmP9LO424PfSpH0NLhMbo0Rq9jFhBjPO6JwTyYZ3ZxdN4G2M2e06uiSjoAQy3315-JItsrJg-NtXsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سفارتخانه‌های ایالات متحده آمریکا در قطر، بحرین و عربستان سعودی، همچنین به شهروندان آمریکایی هشدار دادند که منطقه خاورمیانه را تخلیه نمایند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/139108" target="_blank">📅 15:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139107">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOsDcwL08p3wX9wKYq4-YMdsEO5Ry3R4A6IgTkUmxh5JC7_yjzDX3ORMrJy11Vyh_k1KLdnLR74Ykibf7Q8OVtDGNYPM-XlwTePlcZ60zm29cNBb4L_LplhG3Ze3B2SqWSe9sqldI3i-Pu0tfEmHyvml__Hkd9kruwMUoAQgQ4pz39_eNCApDLuqYnOXBHpFtKF1ynvqfUVKPM21SN3hYPH5yxK0jjCIZX3SA2GkJZJbq_RujmhNOQ0dHQ-1s57e9PIcaudmlftKygLuX4ijTn6AslYX3TMrX7SB-kceOE5ZzbJU6AOi4vGW7EHpJWI4t3O3HdbjZxt939H_ndczjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: اگر سناتورهای جان کورنین و تام تیلیس، که هر دو از من ناراحت هستند چون از آن‌ها حمایت انتخاباتی نکردم (یکی شکست خورد و دیگری کنار کشید!)، حاضر نباشند تاد بلانش را که به گفته همه یکی از محترم‌ترین حقوقدانان کشور است، به عنوان دادستان کل آمریکا تأیید کنند، من او را به عنوان دادستان کل موقت نگه می‌دارم.
🔴
هم‌زمان با قدرت برای تصویب لایحه مقابله با سیاسی‌سازی دستگاه قضایی تلاش خواهم کرد؛ لایحه‌ای که به کسانی می‌پردازد که در دولت جو بایدن و اوباما به‌بدترین شکل با آن‌ها رفتار شده است (در حالی که با من هم بسیار بد رفتار شد، اما من چیزی نمی‌خواهم)
🔴
تاد بلانش صدای عقلانیت بود. این موضوع فوراً دوباره روی میز قرار خواهد گرفت و من آن را به سرانجام می‌رسانم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139107" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139106">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
تعداد هواپیماهای سوخت‌رسان آمریکایی مستقر در خاورمیانه به 113 فروند رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139106" target="_blank">📅 15:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139105">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عارف: دولت برای دو سال آینده حتی برای بدترین شرایط برنامه‌ریزی کرده، اما حفظ آرامش مردم همچنان اولویت اصلی خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139105" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139104">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
بلومبرگ: کاهش ذخایر، بحران سوخت در ایالات متحده را تشدید می‌کند؛ آمریکایی‌ها با موج جدیدی از افزایش قیمت‌ها مواجه هستند، بدون اینکه از بازپرداخت مالیات فدرال که در دوره افزایش قبلی بار را کاهش داده بود، بهره‌مند شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139104" target="_blank">📅 15:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139103">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287ba1985f.mp4?token=YtrY7aRP1NPgUp99zUzdM1yYRQzRF0-z3yRRKyUnbyY3IUqmxjZw6jPT2qsnM5hKFytmqQgXEAX8udmf8HGXu-cu4Z-fTgIU9FyzxVp1EZJb-h8ruZYbWE4lKkaE4hHUE0FttMN5Bl6zIl7s4sMPyVfcwyG2JVkXe3LYe5abtKPcO4lv7xqhn9eGTfwnXRIySXQXrgo5323PcoYdVc_oRwpXxmqTlOgJv2AORoVRWU8WxTJl04VtItTWOOHg494F7IJJTuwTujqaq8WQLGMl1107qqcTT3w6NnXsRZBLy6_Vmx0h2KDBhw1I8XooDecDU_-699ieR6BW6_YYptTYGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287ba1985f.mp4?token=YtrY7aRP1NPgUp99zUzdM1yYRQzRF0-z3yRRKyUnbyY3IUqmxjZw6jPT2qsnM5hKFytmqQgXEAX8udmf8HGXu-cu4Z-fTgIU9FyzxVp1EZJb-h8ruZYbWE4lKkaE4hHUE0FttMN5Bl6zIl7s4sMPyVfcwyG2JVkXe3LYe5abtKPcO4lv7xqhn9eGTfwnXRIySXQXrgo5323PcoYdVc_oRwpXxmqTlOgJv2AORoVRWU8WxTJl04VtItTWOOHg494F7IJJTuwTujqaq8WQLGMl1107qqcTT3w6NnXsRZBLy6_Vmx0h2KDBhw1I8XooDecDU_-699ieR6BW6_YYptTYGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل و قبرس عملیات گسترده‌ای را برای مختل کردن سیستم موقعیت‌یابی جهانی (GPS) در سراسر هر دو کشور آغاز کرده‌اند که دامنه این عملیات‌ها به لبنان و سوریه نیز کشیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/139103" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139102">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری/وال استریت ژورنال: ترامپ، در ساعات پایانی حضورش در باشگاه گلف خود در نیوجرسی، طرح‌های جدید حمله را که به او ارائه شده بود، تأیید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/139102" target="_blank">📅 14:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139101">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری / سفارت آمریکا در اسرائیل: آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/139101" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139100">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سفارت آمریکا در عراق: به شهروندان خود در عراق توصیه می‌کنیم هوشیار باشند و از دستورالعمل‌های مقامات محلی پیروی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/139100" target="_blank">📅 14:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/139099" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
گفت‌وگوی وزرای خارجه امارات و انگلیس درباره کاهش تنش‌ها در خاورمیانه و تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/139098" target="_blank">📅 14:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
اداره کل هواشناسی استان تهران نسبت به بارش باران، وزش باد شدید موقتی و گاهی رگبار و رعد و برق در مناطق شمالی استان تهران هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/139097" target="_blank">📅 14:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
قیمت دلار به ۱۹۴.۲۰۰ تومن رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/139096" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری / شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/139095" target="_blank">📅 13:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1VQzmnKm63z0sHI0ZeZXWv151duACtLxQo6dFbs8lamFQUyngCZVUBd0jsDpfFt5SSKCzCq_bKMnCMf4T6BP0H8d3uFYlke55Qws5_mamDkrwsC6UBb8s4Yp7FMPqvaW0ZJL4jlTBheY8wW3N_jKz56fHF5FkiSei_itTXs2bhGB8fQ9TL_HTGMsDvVmndSCteMZD0i6TyOmH7CGhT-SVDnTQ12m7PyWNRzlLiIO8n2zh-lF2D5Ldnrbox9tZXQ1_w0yQuwOnB6V-_DL4HdM2cndKy3zyB0MQHKQEHkS_nrDTqO16UJQcfYDCX83lLbH0B2LTtuG_LlAMdq2fnnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس: اگر به ایران ضربه‌ای زده شود، کل منطقه و تاسیسات آن را به عصر حجر برمی‌گردانیم؛ به نفعتان هست که حماقت نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/139094" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/139093" target="_blank">📅 13:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=fAw0uks55jvVsm9c8SjH6ic-UPz2RuIy7GzFp3pDZgzlEu-m_YVw-38d4GzuPxMdSjzfqCeg3bPP8Vyx6CY7_UYddPMn-m_MK_ei0zKcYM-VJ7fjP2_m_vZd71ksQsgUjYreApq6Yl9aGT8OOGh6VcL6Ag2HwrPvNfrBmjwRVUqcTmtnlb4uWfNE8JGGMoIh0dH9rRzA1OQVNQ8LCi7jfBmHYN_Mm0ECWi6o81PJwtZPHq7vyhJHSygIrsQmHCYrbpIYQj5s3NY5cl0rE8PRRfNof4PKS0qJdGxj1JERhX_wxCqg7GhURzU0M3VE-7BOtzTGZ8plzARfMduk8FEpeaN-l0oawhE0WOQaOtPO4X-6D4d9rP4vVHD5DltxvB1nqnB7vt6ction8DN1i4SYT24Snq-dXrzKHLeAWYgXv8uMH-fQ8gi25BVT6-l5eyCcj2vL99nu4WB9Jwrnyi0WQdBvnnPhHDmm_uibJ92uhDSR47jrBQIJs8eYgxYcaZAsQDZcofJRWYqrNXtybENEXHPEcvD-zWCPhtYcEypdq5VlIRf1-A_O7kPCkWKHW7OoQuoSjIZfaajftVVHI-BglnFApzfRV1ffXbPK5sYeeWKEdlp9SsrrzAT5kZMhQm7jMMtX9nTAftUFUwpnZAN6pORZ-CRQ-hY9PUmPj5SGCC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=fAw0uks55jvVsm9c8SjH6ic-UPz2RuIy7GzFp3pDZgzlEu-m_YVw-38d4GzuPxMdSjzfqCeg3bPP8Vyx6CY7_UYddPMn-m_MK_ei0zKcYM-VJ7fjP2_m_vZd71ksQsgUjYreApq6Yl9aGT8OOGh6VcL6Ag2HwrPvNfrBmjwRVUqcTmtnlb4uWfNE8JGGMoIh0dH9rRzA1OQVNQ8LCi7jfBmHYN_Mm0ECWi6o81PJwtZPHq7vyhJHSygIrsQmHCYrbpIYQj5s3NY5cl0rE8PRRfNof4PKS0qJdGxj1JERhX_wxCqg7GhURzU0M3VE-7BOtzTGZ8plzARfMduk8FEpeaN-l0oawhE0WOQaOtPO4X-6D4d9rP4vVHD5DltxvB1nqnB7vt6ction8DN1i4SYT24Snq-dXrzKHLeAWYgXv8uMH-fQ8gi25BVT6-l5eyCcj2vL99nu4WB9Jwrnyi0WQdBvnnPhHDmm_uibJ92uhDSR47jrBQIJs8eYgxYcaZAsQDZcofJRWYqrNXtybENEXHPEcvD-zWCPhtYcEypdq5VlIRf1-A_O7kPCkWKHW7OoQuoSjIZfaajftVVHI-BglnFApzfRV1ffXbPK5sYeeWKEdlp9SsrrzAT5kZMhQm7jMMtX9nTAftUFUwpnZAN6pORZ-CRQ-hY9PUmPj5SGCC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/139092" target="_blank">📅 13:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر کشور اسپانیا: شمار پناهجویان [مراکشی] کشته شده در حوادث منطقه سئوتا، به ۶۷ نفر افزایش یافته
🔴
کسانی که به صورت غیر مجاز وارد سئوتا شده‌اند، هرگز اقامت قانونی نخواهند گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/139091" target="_blank">📅 13:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / پاکستان به ائتلاف دریایی عربستان پیوست/مقر این ائتلاف در عربستان سعودی خواهد بود و کشورهای عضو اولیه آن شامل عربستان، پاکستان، کویت، بحرین، قطر، ترکیه، مصر، اردن، یمن، بنگلادش، نیجریه، سودان، جیبوتی و سومالی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/139090" target="_blank">📅 13:20 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
