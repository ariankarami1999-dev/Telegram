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
<img src="https://cdn4.telesco.pe/file/NN4HfmiDHW0sqdnzSg7OUi4qHOzjbIdiVVC_KKl3ycV5uKohRGQ9O2m4FnlHP_x8PWY6wNz1m2xFs3IiwlRVrazdN256QAxqVpP2VhLgLoBZ9YehYMVfNFp8_EYGjNmrSzO0fXN6e7pQUr4D_GMvoAtrpNQ_jNhKr3T7oBlDA3QHzGqLgoRU9zwH45RKTlopK5AlbRE_trmUvGH-zD39t1eHNTjKGBLhUTH3KyFCjCVm8yIwJNQZ0TAY6P2TLVc7qZ0ZtZvQk1lnMeaGXod6v7XfOIruruDk3REBXePd5iSLyRAzWqXSJLDwB_L0zz3XrEHbn3iK2OQK3TxYG5RIxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 23:27:51</div>
<hr>

<div class="tg-post" id="msg-138278">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdvMlKMl7BTKhIJsbhQCAgcu--6awgCnES7gHrMdTSZEHjfLauZlpTjjB5FHbmdGxTVaWAKqkA1OeF_DCNCxVo8sCo6fCaSfcuy8yK2E3Pt1J4GrG16HQSIL26_5L7qmBnAM4tbJRdCTw2MlVqhpGIMpwxFKJOwZ2Zh3dcnoZvlj9woKat2nq8ZzmPJ9_ywbyOBf5Rvf532ju8Qn_TfmsyHy4ziF9Nw4rfnRH9xfX66WzdMp16jF8UINz8Q54iIyFRjDwNX4T8psekdUrReI9Qul262Y8c-lQV3ed4WmU0CLh-KgMfE2D507aYT0VS-T0JKnBo01Q7vaQveffHjfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار کوتاه زلنسکی و نتانیاهو در حاشیه مراسم لیندزی گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/138278" target="_blank">📅 23:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138277">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRoTs8r2eY_Zo6npCPCLoauL1MVazFk-P8A8hZrEfQ1gAq5MVIehw3u7oy_QK2veXQ6cAae1KBviDWAUOe1Fu2mZCvb4AtaT-k1ixrLLpz7qvFT0Oei-O6hQDEX7TxFaqaVe3SeYnL0fDGDOiK-ka28g1WdLl_zFwHQLEMst_vXLDVPTli6jyAUE4p8pqx1yC05_L7djCuvSEfn7Jch3jiXspWq4VeCNTLLgwH7Uv-iI5sFfY3FcgtbixPVUwS1bK2K_G3E7Cs2zBMm9GWtSc3RCXzm9q4M3k8qrxZnXj7WjLqq8h74CxYAtAPSWEZwTXkHRL6T-Izi4z6lRkY_JeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان UKMTO (سازمان دریایی تجاری بریتانیا) اخطاری را صادر کرده است، در سواحل شهرجازان، عربستان سعودی. این حادثه در تاریخ ۲۷ جولای (تقریباً ۷ مرداد) رخ داد. این اخطار پس از بیانیه‌ای از سوی گروه حوثی منتشر شد که امروز ادعا کرد به تانکر سعودی به نام "NCC Ghazal" حمله کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/138277" target="_blank">📅 23:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138276">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
جروزالم پست: نتانیاهو به‌صورت محرمانه به ایالات متحده سفر کرد؛ پس از آنکه نهادهای اطلاعاتی درباره تهدیدی از سوی ایران هشدار دادند.
🔴
بر اساس گزارش N12، نهادهای امنیتی اسرائیل توصیه کرده بودند که پرواز نتانیاهو در شرایطی کاملاً محرمانه انجام شود؛ زیرا گزارش‌هایی وجود دارد که نشان می‌دهد ایران تلاش‌های خود برای هدف قرار دادن مقام‌های اسرائیلی را تشدید کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/138276" target="_blank">📅 23:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138275">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
تسنیم: طبق آماری که به دست آوردیم ۷۵ درصد مردم خواهان کشتن ترامپ و نتانیاهو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/138275" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
عربستان : چند پهپاد رهگیری و منهدم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/138274" target="_blank">📅 23:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138273">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbvGZA2z9UuTBPYzUdk2XzvLsEwWqIIayAhOGObVtgNmkU-QLWqvPz-tcCdrh59QejlMPPqZWf0IbupnRJxo-TgEscDbMX-HLxpAXVzPrRsLhp8c7x1guln95yMunbads6lquL1HIFhmMLkoNcevM4kqWMfjrc5wyNqtegw94MHKJ3284xwCrHREHqRXzCI7ragSfMEOwuAr6Qeatak2aWBWmHvF7BmbyFoQshAhqShNCXZ-8IjdSRjgGCgxsyqOc_xsHcHXVmLuwouMnItqvcDvwUWmgzOlMYBAeKclIQu7OvnVmDh6ChWsFw6kzkZVDeyWYzXwYjV9fnZ-5c0fPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">POUYAM SMART CITY
آینده از اینجا شروع می‌شود.
یک شهر هوشمند دیجیتال که در آن شبکه اجتماعی، هوش مصنوعی، سرگرمی و فرصت‌های جدید در کنار هم قرار گرفته‌اند.
به آینده متصل شوید.
🌐
https://t.me/POUYAM_APPBOT?startapp</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/138273" target="_blank">📅 23:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرنگار المیادین: صدای یک انفجار در حومه اربیل در کردستان عراق شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/138272" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138271">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خبرنگار المیادین: صدای یک انفجار در حومه اربیل در کردستان عراق شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/138271" target="_blank">📅 23:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138270">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
طبق گزارش ها حساب روابط عمومی سپاه در تلگرام، حذف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138270" target="_blank">📅 22:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138269">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4c77ecf1.mp4?token=Uy6-il7N3ySBeKwjNJeJge-G_RI2NkP5JGinX9JV9ccM6_9_Cj9K6Qp7s5luaz0fFYf-WB2C2x8wsI8PE_qtV4DgNiTHo5ETFZ-QlkEzUjX_Xuay1H-JmwiIsI6YIAu3GIMsaA3Rm2ityREysOxs4otQG_ep3Euh9bT9fky0G1THbew1dYL2o_xBryVp7gR3ib26xFpBK-lBILxNq2YFPtE0wuPFyMWxoPKqjL2vx70msIRk4OOkYUN_lRtIiDrkKYz1enQXMosZ4RYwjGPO0Cm33mtOxPPLHbL_07q1JFcfWB95M9-zHYkJ6MP65zHrhYrGGEhSWzB_LyGAw2pJeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4c77ecf1.mp4?token=Uy6-il7N3ySBeKwjNJeJge-G_RI2NkP5JGinX9JV9ccM6_9_Cj9K6Qp7s5luaz0fFYf-WB2C2x8wsI8PE_qtV4DgNiTHo5ETFZ-QlkEzUjX_Xuay1H-JmwiIsI6YIAu3GIMsaA3Rm2ityREysOxs4otQG_ep3Euh9bT9fky0G1THbew1dYL2o_xBryVp7gR3ib26xFpBK-lBILxNq2YFPtE0wuPFyMWxoPKqjL2vx70msIRk4OOkYUN_lRtIiDrkKYz1enQXMosZ4RYwjGPO0Cm33mtOxPPLHbL_07q1JFcfWB95M9-zHYkJ6MP65zHrhYrGGEhSWzB_LyGAw2pJeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شان هنیتی، مجری فاکس‌نیوز، در مراسم خاکسپاری لیندزی گراهام خطاب به نتانیاهو گفت: لیندزی اگر می‌دید که شما (نتانیاهو) این مسیر طولانی را طی کرده‌اید تا امروز اینجا حضور داشته باشید، واقعاً تحت تأثیر قرار می‌گرفت.
🔴
او شما را دوست داشت.
🔴
او اسرائیل را دوست داشت.
🔴
او مردم اسرائیل را دوست داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138269" target="_blank">📅 22:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138268">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7840f687c.mp4?token=Vcr5WuQoy15EW8jqNu3UIX8O27ivaRlvOMMQ0TUlrPo9cBsYIcYwa8VwSk7zAvgEAXCvOcECfpGnvpcqwpVVto7NkdchEGzP6bVFpSqdktviTvxBiStQ59ktSkGRghX0Hbk3Ypw5G4c8Zgyk9XmUYwbUdYNdTSFiXmkUT3lnajlQ-Li2GGN3ki9_gGzjZPoCErzh1fjlo6nGwmZRtb_yjqQuyKGrf7tQB0gS2C-3STuB67mC4Mqs5xhYj0yrK5Aa3JuqZr4K0ox4rw9W-B75v7E6mIt6x2wR_LqQRhlY-JVOgnOxUOb6zTocrdspgqb0KePG8iNZuN6jdlSj2l2Kkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7840f687c.mp4?token=Vcr5WuQoy15EW8jqNu3UIX8O27ivaRlvOMMQ0TUlrPo9cBsYIcYwa8VwSk7zAvgEAXCvOcECfpGnvpcqwpVVto7NkdchEGzP6bVFpSqdktviTvxBiStQ59ktSkGRghX0Hbk3Ypw5G4c8Zgyk9XmUYwbUdYNdTSFiXmkUT3lnajlQ-Li2GGN3ki9_gGzjZPoCErzh1fjlo6nGwmZRtb_yjqQuyKGrf7tQB0gS2C-3STuB67mC4Mqs5xhYj0yrK5Aa3JuqZr4K0ox4rw9W-B75v7E6mIt6x2wR_LqQRhlY-JVOgnOxUOb6zTocrdspgqb0KePG8iNZuN6jdlSj2l2Kkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مراسم خاکسپاری لیندزی گراهام: لیندزی، ما دوستت داریم.
خدا حفظت کند.
🔴
ما همیشه با تو خواهیم بود.
🔴
تو واقعاً فردی بسیار، بسیار ویژه بودی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/138268" target="_blank">📅 22:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138267">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3ca77852.mp4?token=nRbVQNXvxTagnl3QoiRbtPjUGSlx2EVS4lKlARHR3eoJH_dZRa62WnnVOfl3cprMgIxwvy8XtwkofbBM4pD3UWdKOwWuxx8g0wX2k-UNRN9n_A9EtY-vhUp-9vzuSsxoReQDWVVcpcsEklBT1sWrkbsmK7K5SjIGEg2iz3vYp5qt0ZPQhqh9--VW1NnGB0_Grx4sRGoLl-2zlMGg7KDgrdEvJUwkeJu-0mcgeXWB_lih721TAhxuy1TdsAtfGWiFITwTVigO99qNUdjE67vmdlAQ3lKAEgbb0UsmT99B8kA2wIBwpazz48_jlUpj0HEPbmp6ozlMbPuSLZm6eEiabg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3ca77852.mp4?token=nRbVQNXvxTagnl3QoiRbtPjUGSlx2EVS4lKlARHR3eoJH_dZRa62WnnVOfl3cprMgIxwvy8XtwkofbBM4pD3UWdKOwWuxx8g0wX2k-UNRN9n_A9EtY-vhUp-9vzuSsxoReQDWVVcpcsEklBT1sWrkbsmK7K5SjIGEg2iz3vYp5qt0ZPQhqh9--VW1NnGB0_Grx4sRGoLl-2zlMGg7KDgrdEvJUwkeJu-0mcgeXWB_lih721TAhxuy1TdsAtfGWiFITwTVigO99qNUdjE67vmdlAQ3lKAEgbb0UsmT99B8kA2wIBwpazz48_jlUpj0HEPbmp6ozlMbPuSLZm6eEiabg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره لیندزی گراهام: کشور ما به مردان و زنان بیشتری مثل آن انسان بزرگ نیاز دارد.
🔴
فکر می‌کنم می‌دانم او اکنون کجاست؛
فکر می‌کنم او آن بالاست.
🔴
و فکر می‌کنم دارد ما را تماشا می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/138267" target="_blank">📅 22:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138266">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
به گزارش وال‌استریت ژورنال، دونالد ترامپ پس از موفقیت‌های اخیر اوکراین در میدان نبرد، به ویژه توانایی‌های پهپادی و مقاومت آن در برابر روسیه، نسبت به زلنسکی، رئیس جمهور اوکراین، رویکرد مثبت‌تری پیدا کرده است.
🔴
ترامپ که زمانی معتقد بود اوکراین شکست خواهد خورد و از زلنسکی انتقاد می‌کرد، اکنون او را به عنوان یک رهبر قوی‌تر می‌بیند و نسبت به ولادیمیر پوتین بدبین‌تر شده است. ترامپ همچنین به فناوری دفاعی اوکراین، از جمله تولید پهپاد و همکاری در زمینه موشک‌های پاتریوت، علاقه نشان داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/138266" target="_blank">📅 22:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138265">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
العربیه:
یک منبع ارشد در هیئت همراه نتانیاهو گفت نخست‌وزیر اسرائیل و رئیس‌جمهور آمریکا، در واشنگتن دیداری «بسیار مثبت» داشتند که در آن متعهد شدند اطمینان حاصل کنند ایران هرگز دارای سلاح هسته‌ای نباشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/138265" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138264">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d25d76fc.mp4?token=Fx9nZyIw43SIUbIDy7DeqZzRwMBCwWlnJZoI1C3W6hFNvcBmQTgQ_SnmXO9ongsnxIKd0p-9T4xR35IznnMp2vW0GoQNNTXSqdj3ImecPh1p8XlKjeeE_0LLMFfcNH3url7kVehZpkUWm_k5ZUmftDMdA72DRvnDqtzJhE09i27hAUrcDfXdv-fYhKU46VjQTuo6IdsoXXq16qB3Y4vdgJmBU1b_pnXqcz8PeIZngW7ul9jdacSxjpbhnHMkNIN0fjQjoWBksz0KbF7D_AVqQ4GY-rqU4Lteyx-l_5GeK1XoHnjgXR01IIHc78lCEYBRDw7vzqnzoyxXLV15evMjkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d25d76fc.mp4?token=Fx9nZyIw43SIUbIDy7DeqZzRwMBCwWlnJZoI1C3W6hFNvcBmQTgQ_SnmXO9ongsnxIKd0p-9T4xR35IznnMp2vW0GoQNNTXSqdj3ImecPh1p8XlKjeeE_0LLMFfcNH3url7kVehZpkUWm_k5ZUmftDMdA72DRvnDqtzJhE09i27hAUrcDfXdv-fYhKU46VjQTuo6IdsoXXq16qB3Y4vdgJmBU1b_pnXqcz8PeIZngW7ul9jdacSxjpbhnHMkNIN0fjQjoWBksz0KbF7D_AVqQ4GY-rqU4Lteyx-l_5GeK1XoHnjgXR01IIHc78lCEYBRDw7vzqnzoyxXLV15evMjkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره لیندزی گراهام گفت
:
او به‌شدت جنگ‌طلب بود.
راستش را بگویم، هیچ جنگی نبود که از آن خوشش نیاید.
فقط دوستان نزدیکش منظورم را می‌فهمند؛
اما او فکر می‌کرد همه این‌ها به نفع کشورمان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/138264" target="_blank">📅 22:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138263">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrgi2iXBqJALtvJEDSpCvin0YkkKDOneC3IRBfsAGWlPaACFwJiW-75NUPbWbMXoqBuQ61FCBXkokABbZ37rhXNthm4WaiyHhQlBeMW2mW76Vy-921ROYpzaCnp_xRGvTETnqwA1dJfM7tAjqo6n08UVz8vSBxDz1L8Vnedl2fRJkt7mfCFQggHbnafuo7Vctdh3Mw7bUb2OClZmhY9j0s4PNuCcB6gStvop0mAmjla14vFM7EYXWkMaqJXGfwL_-xJV5-FWnEHiZg8PwCvwbAM5Wor7K7CECeO9stXubs2FK8Asx9hprXQrtEC3RzPux2WoONDQ-Jq2oZJyg8Ic1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شکلات شیری خرگوشی در آستانه یک میلیون تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138263" target="_blank">📅 22:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138262">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd212</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/138262" target="_blank">📅 22:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138261">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh27TtMEmL62XfYOO-z5DXWjx3u7I8a0gg6-evigXxEiZvhVctpNL5XorGjzw7JLmonNbV9qV90WODKAa841pfzhNDV2fLjv3UtyXJuP6dVGnLvlRenH44fCJQawKylFp1mqFoxj_Y0aLJVS4QCezgRbJLoPal0L_mQk1kdBqO0IPyu1xXgquUpIjlINmKzDOOm5zyJwIzoLRkHgAoz2DBUK4aRUng4OaPWcGYkbikCZtMdu_VK_0BIRjwZaheE6rvy5yYZQDG8DIFRlNdTxalhe9aWd8CMaM-E6xYxKu0DsMMMR2zg3OTg6UgpChhdS2Fe1wtSsPxvEVXwIjz2X-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
عراقچی: خواهان تشدید تنش با اوکراین نیستیم!
🔴
وزیرخارجه اوکراین اطمینان داد که حمله به شناور ایرانی غیرعمدی بوده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138261" target="_blank">📅 22:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138260">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
لحظاتی پیش صدای انفجار مهیبی در استان اربیل عراق شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138260" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138259">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
غریب‌آبادی، معاون حقوقی وزارت خارجه: هر کس فکر می‌کند که می‌تواند، بالای ۵۰ میلیارد دلار از تنگه هرمز درآمد داشته باشد، کنترات می‌دهیم برود کسب درآمد کند و نصفش برای خودش و نصفش برای جمهوری اسلامی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138259" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138258">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رویترز:
چین به‌طور مستقیم با انصارالله یمن گفت‌وگو کرده تا برای نفتکش‌های چینی عبور امن از دریای سرخ را تضمین کند
🔴
پکن برای هر یک از کشتی‌های خود به‌صورت جداگانه از انصارالله مجوز عبور دریافت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138258" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138257">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df79cbfe8.mp4?token=nDFXuu-0P8bmKGdLDrSYld9XBamvjo3Mz9N90-8sMyoj3zoOWr4xfYKV27szdtWKldBg2KTC4g4eoc4DP6fyj-OsT7sGqZOau2NKn_XkmnKDLDm15px1IKOOjiD0R81gKx7v_tndT6X1di6CLTMZ4jCqw8cbLDwO-7Z555k8D20HsYNfx7NdbKJsbRRRloX1EtfOD79S8JPd-VE8tjG6rGTjlIcOO6-SXmqccDex8FKD650ONdFVLTvbS6PeWsw6Ycnc7I1eNseTc-YJCKE1Tr82HXUlHnrQ4cIaLZwUCnhheb60oBPWLjOGGn99eNKceiopiGr0vscv95jVZ14iDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df79cbfe8.mp4?token=nDFXuu-0P8bmKGdLDrSYld9XBamvjo3Mz9N90-8sMyoj3zoOWr4xfYKV27szdtWKldBg2KTC4g4eoc4DP6fyj-OsT7sGqZOau2NKn_XkmnKDLDm15px1IKOOjiD0R81gKx7v_tndT6X1di6CLTMZ4jCqw8cbLDwO-7Z555k8D20HsYNfx7NdbKJsbRRRloX1EtfOD79S8JPd-VE8tjG6rGTjlIcOO6-SXmqccDex8FKD650ONdFVLTvbS6PeWsw6Ycnc7I1eNseTc-YJCKE1Tr82HXUlHnrQ4cIaLZwUCnhheb60oBPWLjOGGn99eNKceiopiGr0vscv95jVZ14iDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو و ولادیمیر زلنسکی پیش از مراسم تشییع سناتور لیندزی گراهام در حال گفتگو دیده شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/138257" target="_blank">📅 22:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138256">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
رویترز: چین به‌طور مستقیم با انصارالله یمن گفت‌وگو کرده تا برای نفتکش‌های چینی عبور امن از دریای سرخ را تضمین کند
🔴
پکن برای هر یک از کشتی‌های خود به‌صورت جداگانه از انصارالله مجوز عبور دریافت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/138256" target="_blank">📅 22:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138255">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4yw7Co4tZf4Rjdj94jtEJrCpl39To3LZIDK1MmFwW8kef-RL6cjhJNVlvoVFo0tt0WAMPay___ZccoqFc38zG9PjLS9zUpHV5iI44uy0a4It2JJJXlUpGpAZmmgxAYxpdD_vnRxrAM2RWC63WBwoEDeCB8boFPPImhb6xyftn7D4xNDu62yyvUXFUcaNkEKV21vK8stsRUbQvTeuQadYebRpQx3vwaZ_jklfPQ-vJGOjRJM_R5BxxuJyGPHfqo6-vWJ1vB7z509XKOzu9q8il2IeB5E0FedhwlUQKbftHYKO4okZKovRvQpcrceqsLQCMOppnpYTclM_S2umfdA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش های متعدد، سپاه پاسداران در حال آماده شدن برای حمله موشکی بالستیک به اوکراین است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/alonews/138255" target="_blank">📅 22:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138254">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23353f0376.mp4?token=Yk0OW3U59LJqxjUVxlwWCsdM6tq_GQtpRP8zc8abLJEIDXSU1HegaCc_ECdO3Q4wHW7puN9V9KfsM8LQFO_mAuXm-ZiPIHa2oAslw4XPvv7kV4R1f-_n97XozLlzKjaBBODnzxO06XH-EYqnEDmwhob0wPW53eAL363lEy9hZYTyPaOb2u_Ca5vJtdQj2nhrbVxWp4-U_33tXHVGKLp0ax_OKjUON7Pvs128f5M0-dMVMtDFBmfs3SbqWyc7bQ4MEW3wpvP4F07tH-93dvQt26yxEAYTfrydWHFmSSPxJEOm0lxKPifQPTJFeyE2TwHQeOCs4hYPtGDBG8HYIbh34A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23353f0376.mp4?token=Yk0OW3U59LJqxjUVxlwWCsdM6tq_GQtpRP8zc8abLJEIDXSU1HegaCc_ECdO3Q4wHW7puN9V9KfsM8LQFO_mAuXm-ZiPIHa2oAslw4XPvv7kV4R1f-_n97XozLlzKjaBBODnzxO06XH-EYqnEDmwhob0wPW53eAL363lEy9hZYTyPaOb2u_Ca5vJtdQj2nhrbVxWp4-U_33tXHVGKLp0ax_OKjUON7Pvs128f5M0-dMVMtDFBmfs3SbqWyc7bQ4MEW3wpvP4F07tH-93dvQt26yxEAYTfrydWHFmSSPxJEOm0lxKPifQPTJFeyE2TwHQeOCs4hYPtGDBG8HYIbh34A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از دیدن این کلیپ متوجه میشید الماس چقدر میتونه از طلا گرون تر باشه.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/138254" target="_blank">📅 22:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138252">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h37vWiltPLLrR4anLUejspEtAv7KLyMzYllqE__DnUu1GwdNZMhk2vL5xBeySf6Aeaq5tdkmi9udnnpQ47i2CWtVjdDfr1bAuL1sf7AHXkGUaZnZVkadi7Wa_89x9vcXEe3BmsI2yik0T-Kj9n6xX0Pgz1v798PPffmVGqiCsVLNR4MRWJ6l5QPGK3BpxCqRtokMvSPFkqACZGV3wl02ZQEKiwV6D08idTWsqr07kSo8vKzxnaJBOUcOVLJukZFyBVOZ9bDGaG_RzTBC7ER66zp2GwgmP5fr0fAEgrSILAVl4-6aQiHPeP7GpXZ2c32jaOMuvvlKoT_ISk126fBh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950c5db38a.mp4?token=FtAC0B7GQO004zEve2AcrouMsuRehNvED5rcUr-B0AXP-yDyZg6YNt7fc4dUTVR33qQrqk20YRH2-XWw9ariJILRNrSoFZYyGscgX7WjA-SiylqU6Weugpzwa5gjKgOUAQACi5PSrfv_k5raNfOG3727Cybif5jtbFX-yQ0mNadLJQY80TPO56Zm-VpC4A1eTOx0uC8dxGGMaCF3uahm71ySHWfA_sGXJcuclMkn9ba4r-D18usev1fNzCwc1fowJoD-f08Mmwj3CSM-6SOO07gaxOaQmkPHuvVGAkQyTCRSqxSAUGL7ykbIy7DrfYQceDu1ENRjq6Ee9DE6Kd3JBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950c5db38a.mp4?token=FtAC0B7GQO004zEve2AcrouMsuRehNvED5rcUr-B0AXP-yDyZg6YNt7fc4dUTVR33qQrqk20YRH2-XWw9ariJILRNrSoFZYyGscgX7WjA-SiylqU6Weugpzwa5gjKgOUAQACi5PSrfv_k5raNfOG3727Cybif5jtbFX-yQ0mNadLJQY80TPO56Zm-VpC4A1eTOx0uC8dxGGMaCF3uahm71ySHWfA_sGXJcuclMkn9ba4r-D18usev1fNzCwc1fowJoD-f08Mmwj3CSM-6SOO07gaxOaQmkPHuvVGAkQyTCRSqxSAUGL7ykbIy7DrfYQceDu1ENRjq6Ee9DE6Kd3JBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فقط حقوق ها رو در آگهی استخدامی ببینین
🔴
جمهوری اسلامی با وقاحت تمام خود را مدافع وطن میداند درحالیکه کشور را به فلاکت رسانده
🤔
لعنت خدا بر حرام زاده هایی که مردم ایران و این کشور ثروتمند رو به این روز انداختن. شیاد هایی که آخرت را به مردم فروختند ولی برای خود کاخ های دنیوی ساختن. عرعر شما هم به سر میرسه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/138252" target="_blank">📅 22:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138251">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ : لیندسی، ما دوستت داریم
خدا ازت محافظت کنه، ما همیشه کنار شما هستیم، تو واقعاً خیلی، خیلی خاص بودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138251" target="_blank">📅 22:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138250">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ درباره لیندسی گراهام : اون یه آدم خیلی تندرو بود. بهتون می‌گم، هیچ جنگی نبود که ازش خوشش نیاد
🔴
فقط دوستای واقعی‌اش می‌تونستن اینو بفهمن، اما اون این دیدگاه رو برای خیر و صلاح کشورمون داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138250" target="_blank">📅 22:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138249">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ : فرقی نمی‌کرد اوضاع توی واشنگتن چقدر پرتنش بود
🔴
تقریباً همه، چه جمهوری‌خواه چه دموکرات، لیندسی گراهام رو دوست داشتن
🔴
البته نه همه؛ ولی این حرف خوبیه, همه که نه
🔴
باید قبول کنم، اون شخصیت خیلی قوی و سرسختی داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138249" target="_blank">📅 22:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138248">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df79cbfe8.mp4?token=sAcaX5PAQ06MacQZwWdfx1Na0vx2qaYo3Mmdz7_bvFfYykZcFQnkY_2WEa4b790paFrS33_3ocHuPx7n0Msfcvm-OMYymCCVbyUprDfiK5S3g7Le4nhrrYVbxMMjQEajHHhC1Nyl3r-xpZL2sbNXISEfZxsPGwP60sCSASlAbcy3zxtHk9p-jPFjI2ZAvuddgEuzIao3LMJKVn9MIJBDIGCgQB8q7KvrhbJTQV8R87Hwu-v0HQV15lOmRC29BLlKUqm9iH-3YEgpEebmhlVEgGa_BZJxckufYuw0-Q6mV1REIwJzvNHTzPC8ao0kWVJlypxVU0e2Se80NiOFpOne_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df79cbfe8.mp4?token=sAcaX5PAQ06MacQZwWdfx1Na0vx2qaYo3Mmdz7_bvFfYykZcFQnkY_2WEa4b790paFrS33_3ocHuPx7n0Msfcvm-OMYymCCVbyUprDfiK5S3g7Le4nhrrYVbxMMjQEajHHhC1Nyl3r-xpZL2sbNXISEfZxsPGwP60sCSASlAbcy3zxtHk9p-jPFjI2ZAvuddgEuzIao3LMJKVn9MIJBDIGCgQB8q7KvrhbJTQV8R87Hwu-v0HQV15lOmRC29BLlKUqm9iH-3YEgpEebmhlVEgGa_BZJxckufYuw0-Q6mV1REIwJzvNHTzPC8ao0kWVJlypxVU0e2Se80NiOFpOne_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو و ولادیمیر زلنسکی پیش از مراسم تشییع سناتور لیندزی گراهام در حال گفتگو دیده شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138248" target="_blank">📅 22:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138247">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4a4e00d89.mp4?token=IZ4UVQ7EhpIvZ24ClOP5iT8pe2xh0ftx7tVLTzsFNvPWcSXQhXmWaCc9uGNKnZNhy50eXvO4oqBE2lEerOUinu8eNwTWEMSGBj7Q2lzgynuYoUxshPS6FNTVCkjWSWN8ds8xq73RddERBsO2msX17sZAztBG0m1D2trxMgm9spV5VjYcmBzn-ezikmVtihn2O4_sVlMtN-Nf1aom8N_RJf0ld_wNYb5v7uusCK4gDcAQziBqFr2ugD_esWX6k79IZrspdydX2uHM3xb8PMRUkFvgefQxa7liFF71uIHMbUwde2dlO3FZ1k4uTPKv_oAcD4p3vVGeamiOVNuDZYxhnZE92t_5H0TI_RBUqLgquGA8N4mT8wfiFJSBghyO4HdxiK6RYggWBSQzWE_-ox8N2wxI1mcWnNUuQMIou9ymwkskoM836KT1zvgnRmp3gyguc2XyFGnVzugWOWqwbilQLfbnqGcbnZMigBFsKcIYi15ys1K7ZpHKLt3F-QJyApz0YGU8bTXpZuPGZ_R1dwuBv9k7aPPAQ3g-7GAhuTl2fZM6mPF-nwXK_xsc_uVJ3sMYnKFS6Mi-Y-PzLu4v3cGyEqcCXnTbIX38Ro0HA21Vu-s7GhNl_L-ar0QTLDCjQpto98ZeTfcJ0R-iNTFEmBTC8fm5wIccK0KXZlTYfAn6_jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4a4e00d89.mp4?token=IZ4UVQ7EhpIvZ24ClOP5iT8pe2xh0ftx7tVLTzsFNvPWcSXQhXmWaCc9uGNKnZNhy50eXvO4oqBE2lEerOUinu8eNwTWEMSGBj7Q2lzgynuYoUxshPS6FNTVCkjWSWN8ds8xq73RddERBsO2msX17sZAztBG0m1D2trxMgm9spV5VjYcmBzn-ezikmVtihn2O4_sVlMtN-Nf1aom8N_RJf0ld_wNYb5v7uusCK4gDcAQziBqFr2ugD_esWX6k79IZrspdydX2uHM3xb8PMRUkFvgefQxa7liFF71uIHMbUwde2dlO3FZ1k4uTPKv_oAcD4p3vVGeamiOVNuDZYxhnZE92t_5H0TI_RBUqLgquGA8N4mT8wfiFJSBghyO4HdxiK6RYggWBSQzWE_-ox8N2wxI1mcWnNUuQMIou9ymwkskoM836KT1zvgnRmp3gyguc2XyFGnVzugWOWqwbilQLfbnqGcbnZMigBFsKcIYi15ys1K7ZpHKLt3F-QJyApz0YGU8bTXpZuPGZ_R1dwuBv9k7aPPAQ3g-7GAhuTl2fZM6mPF-nwXK_xsc_uVJ3sMYnKFS6Mi-Y-PzLu4v3cGyEqcCXnTbIX38Ro0HA21Vu-s7GhNl_L-ar0QTLDCjQpto98ZeTfcJ0R-iNTFEmBTC8fm5wIccK0KXZlTYfAn6_jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراسم خاکسپاری لیندیسی گراهام با حضور ترامپ درحال انجامه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138247" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138246">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59af49fe1e.mp4?token=lZa-0ZZUjODNtmyq1EtHFCFHtI4p5huWXRnoKISXeztj8FzIev3r4D4RXBi_Vn9E_wTg2S6hdY6xwaKAn2oA-XY0Pa_1Oe-Kwu_RjWZ5iQD2vokLY4SBwE-goW020ymGojnt8gBI7dpwqRHlF4UVvp-bYYz_dpzlkUPu4f9d7GTCCpkGKQjV6VHh14viZeO3ZycvUW-EUPw4zcP6Vaao0cdfpzPV7m7sjnZ8nYsrLHCE2myGYw09wWBp5x1O4nGPjhwT-Wf30chCP7vsA-SDnwXMX1XZ6M7dpRckxpxMaC-uLUFzBFGyCs0zVFAnovosp72o2d5s_7pydUYQuUgIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59af49fe1e.mp4?token=lZa-0ZZUjODNtmyq1EtHFCFHtI4p5huWXRnoKISXeztj8FzIev3r4D4RXBi_Vn9E_wTg2S6hdY6xwaKAn2oA-XY0Pa_1Oe-Kwu_RjWZ5iQD2vokLY4SBwE-goW020ymGojnt8gBI7dpwqRHlF4UVvp-bYYz_dpzlkUPu4f9d7GTCCpkGKQjV6VHh14viZeO3ZycvUW-EUPw4zcP6Vaao0cdfpzPV7m7sjnZ8nYsrLHCE2myGYw09wWBp5x1O4nGPjhwT-Wf30chCP7vsA-SDnwXMX1XZ6M7dpRckxpxMaC-uLUFzBFGyCs0zVFAnovosp72o2d5s_7pydUYQuUgIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : همین الان یه جلسه خیلی عالی با رئیس‌جمهور ترامپ داشتم؛
- وقتی می‌گم عالی، فقط یه تعریف ساده نیست
- یه گفت‌وگوی صمیمی و کامل داشتیم، با حمایت متقابل و درک مشترک درباره هدف اصلی؛
- اینکه مطمئن بشیم ایران سلاح هسته‌ای نخواهد داشت و به اهداف دیگه هم برسیم.
- این یکی از بهترین گفت‌وگوهایی بود که تا حالا با یه رئیس‌جمهور آمریکا داشتم؛ با دوست‌مون دونالد ترامپ.
- تیم‌های ارشد دو طرف هم حضور داشتن و درباره اقدامات مهم برای امنیت و آینده اسرائیل هماهنگی و تبادل نظر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138246" target="_blank">📅 21:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138245">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ادعای کانال ۱۲ اسرائیل: نتانیاهو به ترامپ تأکید کرده که حملات بیشتر علیه تأسیسات هسته‌ای بازسازی‌شده ایران اجتناب‌ناپذیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138245" target="_blank">📅 21:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138244">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر خارجۀ اوکراین: با همتای ایرانی‌ام تماس گرفتم و گفتم هدف ما دفاع از کشورمان در برابر تجاوز روسیه بود و ما قصد هدف‌قراردادن کشتی‌های غیرنظامی را نداشتیم.
‏
🔴
هدف ما، اجتناب از هرگونه تشدید تنش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138244" target="_blank">📅 21:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138243">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iuu0-1OIt7uWB7-9k-EqD-z0HQz6AMkuoRRs7ukY2SfaZj46Wv9PfRkddAbS-Z7aurvgfVMuGkP1jPqJAMJa1V6U6b240rKvaAAijGXwqrV6L3ozYiWdeS3l9lLRgpRbqw1oFNhosk-SCQzv_WwdqK8VmAIWp8Kfzt_kqCnWHVStbAcf2h2CcyRYC9qj5nZ-leEOCzuyOPX01NI6rd81_rTYyTzTclNpBPFu94hNURASlZGKYrn93m2qvMQpYWgT1eVGiZwQJbs_LT8_-G0GPfg-6R-07mzfncsF0-O2Joq9wXxLRMRL2shxn2tUA7fd2opQ0et_B4uSHZBDSG-75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
دنبال بهتر کردن زندگی مردم هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138243" target="_blank">📅 21:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138242">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138242" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138241">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daaee7b635.mp4?token=bwTHalAq1YIuBxYHzlN-lOgS55UqZ9mYpmLSNJflSsoZ0XcwDx8sFrvGjmpWBCnIR91s3ybypXYY9xsZBoPJ2FaLVd_VjUe5OUNZn304G5EIJ0Wtfg_jEJKMFNocwDTUfSLwkmUax8TgJfO4beK7uLA5tsxvoA1qRvPG8yRH7aSljY6sC3e_227KDDMWVoNUu-JubJKEnqywGVLATCE4KxZqU8S4WAM-2KwzNOS9cdX9YZB7ISd5QtdQvVhXc_TqH9z0sOvZ9Uv7NIMvCKDDmsqhhNqNFepKcM_NG73sLapstUqRI54K06rx3HqJ0c7dcK74dZooUtot97n0RHr6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daaee7b635.mp4?token=bwTHalAq1YIuBxYHzlN-lOgS55UqZ9mYpmLSNJflSsoZ0XcwDx8sFrvGjmpWBCnIR91s3ybypXYY9xsZBoPJ2FaLVd_VjUe5OUNZn304G5EIJ0Wtfg_jEJKMFNocwDTUfSLwkmUax8TgJfO4beK7uLA5tsxvoA1qRvPG8yRH7aSljY6sC3e_227KDDMWVoNUu-JubJKEnqywGVLATCE4KxZqU8S4WAM-2KwzNOS9cdX9YZB7ISd5QtdQvVhXc_TqH9z0sOvZ9Uv7NIMvCKDDmsqhhNqNFepKcM_NG73sLapstUqRI54K06rx3HqJ0c7dcK74dZooUtot97n0RHr6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
المیرا شریفی مقدم: سینگلم یکی بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138241" target="_blank">📅 21:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138240">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فاکس‌نیوز:
محور اصلی گفت‌وگوهای آمریکا و اسرائیل، تصمیم‌گیری درباره گام‌های بعدی پس از حملات اخیر به ایران بوده.
🔴
همچنین نتانیاهو احتمالا اسناد و اطلاعات تازه‌ای ارائه کرده که نشون میده جمهوری اسلامی با وجود صحبت از دیپلماسی، همچنان برنامه هسته‌ای خودش رو پیش می‌بره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138240" target="_blank">📅 21:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138239">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKfpe7bFIyidUtybEBK-0vPPZoQthZap9MAUp2351wZpqAPpTJa_RSznQJDAYrR8fqRaYNapdSXEEkZ9_vzd8hmXXa2bnWpE-qV5ZX9yzeSafFEd7pa9mThckN2mdwn6nK3rrSoLB6LFC5k3u9kUvDsgznxPK-zf5BQKh-KkjR8JZVGn65y7I5obi7G9PdMrfdouee5yu3Uttvox2qzeUhu7gz8coDLvYmSZvf1gBT7czf8Vc8wIt6O-HzvJwDdum3pAVbWY3Ft2vcqNUygXFOmFRTm4C9PAUoPQGP8sBRCTeQzRVHYyxeBnTMBJLNojbGalOHIsXtSA7m_uMV2wLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: تا ۲۸ ژوئیه ۱۸ کشتی تجاری تغییر مسیر داده شده، ۲ کشتی از کار افتاده و ۲ کشتی هم بازرسی شده‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138239" target="_blank">📅 21:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138238">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏
👈
شبکه 11 عبری:
ایران تلاش‌ های خود برای آسیب‌ رساندن فیزیکی به مقامات ارشد اسرائیلی، چه فعلی و چه سابق، در تمامی سطوح و رده‌ ها را افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138238" target="_blank">📅 21:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138237">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd1db5e6.mp4?token=uzBAxS3X88E67fUTgnktL9HzHySapMOPtZkJHaqKcdJHHber-xFutTpBSdavATsYMuwfCbbKYgj_aTl45I3kruvkGTu97sK_FJ7_-iU-3PZ9lpcMHU2nKO8nFoHQLD9CDgxiqyeAhtTkK3A7l-0oY-aDI3EOlL4cTyLvBJazTEezOQR0ulsqJY9Q0ykNWY7QW9CafMquLLEjBnQaMQswZrg4bml_6WDfCS4GIjC-1apySHT8YxPv7Yk-m9UUN0if2dZcHnP5J5vLMzUXcAzaDI9K76fk4r4AQhP3U0rcmIQ0sSiolPMmmYDGc64H-8oXnf_rARlX7NR8s3weIuaSIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd1db5e6.mp4?token=uzBAxS3X88E67fUTgnktL9HzHySapMOPtZkJHaqKcdJHHber-xFutTpBSdavATsYMuwfCbbKYgj_aTl45I3kruvkGTu97sK_FJ7_-iU-3PZ9lpcMHU2nKO8nFoHQLD9CDgxiqyeAhtTkK3A7l-0oY-aDI3EOlL4cTyLvBJazTEezOQR0ulsqJY9Q0ykNWY7QW9CafMquLLEjBnQaMQswZrg4bml_6WDfCS4GIjC-1apySHT8YxPv7Yk-m9UUN0if2dZcHnP5J5vLMzUXcAzaDI9K76fk4r4AQhP3U0rcmIQ0sSiolPMmmYDGc64H-8oXnf_rARlX7NR8s3weIuaSIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ژیلا صادقی به پژمان عشق ابدی : خیلی هوشمندانه بازی میکردیا تو عشق ابدی قشنگ مشخص بود رفته بودی اینارو بخاطر این برنامشون تخریب کنی.
🔴
پژمان : والا من رفته بودم ترکیه برای شرکت تو مسابقه ورزشی اون کنسل شد دیگه رفتم عشق ابدی ولی حیف شد الان یه برنامه مثل عشق ابدی طبق قوانین جمهوری اسلامی تو ایران نمیسازن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138237" target="_blank">📅 20:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138236">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک نفتکش عربستان هدف حمله قرار گرفت
نیروهای مسلح یمن:
🔴
یک نفتکش سعودی را به‌دلیل نقض ممنوعیت کشتیرانی با چند موشک بالستیک هدف قرار داده و آن را مجبور به عقب‌نشینی کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138236" target="_blank">📅 20:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138235">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
کاخ سفید اعلام کرد که پایگاه مشترک چارلستون در کارولینای جنوبی به افتخار سناتور متوفی لیندزی گراهام به‌نام او تغییر نام خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138235" target="_blank">📅 20:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138234">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/138234" target="_blank">📅 20:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138233">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnPIdPH6HlPApVCvjruL0nYwS0MquO63HahQ1EJijhiC9y-UWQs3_kukwR6cS2QVNQw8cK_B1lKc0brsEGBeFQawzaiPnWMteRXpVr-DwEg1kC6-grUFZQtOcfVnfsvlZfCuBIaMriNvVZWwGe3w6FUdXd_DlES_ud1a6xtizJrq7YYEpaVecR4iL9zf4grI170SWv6F9oze7Xeq9PjACouq8sn_nL0j2MTWw23E686IY6s2hJ5ELONG1Y9dc9e1Kt1V5V8Y4l-j32dKIE0k3ufngu3cWMN2IYmDi29QW0Juz11DRoFu3TzeZAFQMMnQ3L2FROUDU_cPKCFLatP3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه اوکراین در مورد ایران
:
من با عباس عراقچی، وزیر امور خارجه ایران، برای یک گفتگوی صریح تماس گرفتم. دیپلماسی به معنای گفتگوی مستقیم است، حتی زمانی که این گفتگو دشوار باشد. من تاکید کردم که هدف ما اجتناب از تشدید غیرضروری است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً برای دفاع از کشورمان در برابر تجاوز روسیه است و هرگز به منظور هدف قرار دادن کشتی‌های غیرنظامی یا مردم عادی نبوده است.
این موضوع در مورد اظهارات ایران در مورد شهروند ایرانی که فوت کرده و همچنین کشتی غیرنظامی که در یک حادثه اخیر مورد هدف قرار گرفت، نیز صادق است. هدف ما مقابله با تجاوز روسیه است، که ریشه تمام این حوادث است، و روسیه است که مسئولیت کامل تمام تحریکات و تلفات را بر عهده دارد.
من بر ضرورت اجتناب از هرگونه اقدام تحریک‌آمیز، و همچنین پایان دادن به هرگونه حمایت از جنگ روسیه علیه اوکراین، تاکید کردم. این جنگ غیرقانونی است و باید پایان یابد.
موضع ما بدون تغییر باقی مانده است: اروپا و خاورمیانه شایسته ثبات، امنیت و صلح هستند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138233" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138232">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ :
- اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، رابطه خوبی با ایران بسازه
- بعد از اون، ایران رفت سراغ توسعه موشک‌های هسته‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138232" target="_blank">📅 20:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138231">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de0ab7ddb8.mp4?token=rAZbWuNEdvWTpmYVn-I7B9tR82s8x9aCJ-LKOmKCWAKVN4R1VgFKWUAUL53B4okbgChvkD70UzcZBPKON1Sot1cAh2IaBo8RqZTDcm7kGBKPEnoHhG3Vfpecxp9nyTm_8vO_qJ4UV8bcuk5trDsvxweWu2cumlA0EZTHNTzhEel4pQxkct3zXBajOab772CoA3Hxgl0xykKJgVLah2llcbMsLqk5bIYnW0XxykTCPN3tVTrwc6vSiWVJ3WOoVM78W1WO5FdOhoAljzHA0U6V5KrAZAotSOhnX9HDIggZYQMaUk99vhUo77rRcTZ7nBK3F4QF7b4J0SMQ0Re1-9Z56IWqRE6_4R-bDqvrkTTGg16-FbbUgKe068yRnNs8twsqDO0El7eHTKjti5iYDQNZY0ws-Lhx-kDqMsspuewPuRX6DH6JJQl4T9wab8s0rYB3GckqMwXo7bu72Fbdzi6rqW-kdQekk8mhvB2CRZqtLU1ErQDjV5sznF8FHiiBzW7ASvSKOgzdcdM4I34E1FPVw7Pfx9_1JUaQAiU2CAcewH5DycFSg1A4Wln-XvxjrkHO64pftQoudnpkfJrUf5YppEsUb3NONauL6z8As8kUv7tLiwkR35OzcfUtudPtjasYB-iedNmdyOu6SM0UoJGI1Yc_FLgTnRyWKFBwo3JG5bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de0ab7ddb8.mp4?token=rAZbWuNEdvWTpmYVn-I7B9tR82s8x9aCJ-LKOmKCWAKVN4R1VgFKWUAUL53B4okbgChvkD70UzcZBPKON1Sot1cAh2IaBo8RqZTDcm7kGBKPEnoHhG3Vfpecxp9nyTm_8vO_qJ4UV8bcuk5trDsvxweWu2cumlA0EZTHNTzhEel4pQxkct3zXBajOab772CoA3Hxgl0xykKJgVLah2llcbMsLqk5bIYnW0XxykTCPN3tVTrwc6vSiWVJ3WOoVM78W1WO5FdOhoAljzHA0U6V5KrAZAotSOhnX9HDIggZYQMaUk99vhUo77rRcTZ7nBK3F4QF7b4J0SMQ0Re1-9Z56IWqRE6_4R-bDqvrkTTGg16-FbbUgKe068yRnNs8twsqDO0El7eHTKjti5iYDQNZY0ws-Lhx-kDqMsspuewPuRX6DH6JJQl4T9wab8s0rYB3GckqMwXo7bu72Fbdzi6rqW-kdQekk8mhvB2CRZqtLU1ErQDjV5sznF8FHiiBzW7ASvSKOgzdcdM4I34E1FPVw7Pfx9_1JUaQAiU2CAcewH5DycFSg1A4Wln-XvxjrkHO64pftQoudnpkfJrUf5YppEsUb3NONauL6z8As8kUv7tLiwkR35OzcfUtudPtjasYB-iedNmdyOu6SM0UoJGI1Yc_FLgTnRyWKFBwo3JG5bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اون‌ها توافق کردن که سلاح هسته‌ای نداشته باشند
- در واقع باید این موضوع رو رسماً اعلام کنیم، اما اون‌ها باهاش موافقت کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138231" target="_blank">📅 20:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138230">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ : اگه دوباره به قدرت برگردم و بخوام کار رو تموم کنم
- همون‌طور که بعضی‌ها می‌خوان، با موشک‌ها می‌تونم بیشتر پل‌های اون‌ها رو کمتر از یک ساعت نابود کنم
- اما می‌دونید، ساختن یک پل برای اون‌ها ۱۰ سال طول می‌کشه
- ساخت پل‌ها خیلی زمان می‌بره و بعد از اون، نیروگاه‌ها قرار دارن
- من می‌تونم نیروگاه‌های اون‌ها رو ظرف یک روز از بین ببرم؛ همه نیروگاه‌ها نابود می‌شن
- حدود ۹۱ میلیون نفر باید بدون برق و بدون پل زندگی کنن و این یه تعادل خیلی حساسه
- اون‌ها می‌دونن اگه به توافق نرسن، من این کار رو انجام می‌دم
- پل‌ها کاملاً نابود می‌شن؛ واقعاً. کمتر از دو ساعت، بیشتر پل‌های اصلی از بین می‌رن.
- نیروگاه‌ها هم در یک روز
- اما اگه بتونم از انجام این کار جلوگیری کنم، ترجیح می‌دم این کار رو نکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138230" target="_blank">📅 20:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138229">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ، درباره کوه کنلگ :
- لازم نیست نتانیاهو اینو به من بگه، اون این موضوع رو مطرح می‌کنه چون می‌خواد من وارد ماجرا بشم
- نیروی فضایی آمریکا بهترین دوربین‌های دنیا رو داره و ما دقیقاً می‌دونیم اونجا چه خبره
- شنیدم نتانیاهو این موضوع رو علنی کرده. بهش گفتم : «چرا مستقیم به خودم نگفتی؟ چرا باید همه دنیا باخبر بشن؟»
- من دقیقاً می‌دونم توی کوه پیک‌اکس چه اتفاقی داره می‌افته
- این موضوع مشکل بزرگی نیست. اگه به توافق نرسیم، مجبور می‌شیم کوه پیک‌اکس رو از بین ببریم و انجام دادنش برامون خیلی راحته
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138229" target="_blank">📅 20:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138228">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
غریب‌آبادی: آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود؛ دوباره برمی‌گردد و باز دوبرابر می‌خورد
🔴
مجری صداوسیما: ما در این وضعیت هستیم؟ چرا دنبالش نمیرویم؛ ۴ ضربه بزنیم که دیگر نیاید
🔴
غریب آبادی: کسی مانع نیروهای مسلح ما نیست، برویم بزنیم
🔴
نباید پاسخ‌های خودمان را ضعیف تلقی کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138228" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138227">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a223d8da6.mp4?token=hbDzqagQJtkdSt9Ec0spbeuRZgfFP7FkJEeRQdhSvzgvGat_YQKsjXRPUWIRc6TmyFXNhIjkNw1fXotNIqhAWi95xgN-aSuMh1QmjxIfCKcgwmF9Y35v8wdTkXjF_k93HxgfAbVN_1bUVaJhhwxQwrFXpKpPzV3gnLyBWedERgwVMKASNMQEYCs-eBfvMW0KTPRS4TkvokIIGJ8DbfC9dfSY5VDswOE2-MnhFYFttq-dpZE-ERnWwUqkwiJnV6JhVSbHb9xNpxTUUwOaIYsu2tbpygtd-dLpWH4_LqNAHBccxvFziFERLjPAeCuOweQzNW48MvtO0pW0HV1ym-3Xx1kFz_nGjobmLFFBipg8uBuFALq5XqHJxtxLBSMEm3gzDHkV85FMrA25wI0lLyWTyudAv6lYYLcmQxtkYL4rTBjOml-ECuW7QY_sPoHST6N2tOpkU9Z_MqFqT3lQ1dicSaSnaYN_oEEpnu-XGv4LHS7k3kKD783wuKNd6MeSYRhWAVpQLcPoBYLWu15HeLyEZQT4U3JXyqyK7Nre1eZ9SSYoOxAnBG5R0YB0Vor9DeZr06yv5OgoCnRcnDN-uyuKC8R0oVfCJZ1ByclL0er6KcuglfsBPOuRZele9OkHSN7wVDJpdKtepz3mPpj1JdyvgwMPCvMQ4VD_dBAmO1sv0WE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a223d8da6.mp4?token=hbDzqagQJtkdSt9Ec0spbeuRZgfFP7FkJEeRQdhSvzgvGat_YQKsjXRPUWIRc6TmyFXNhIjkNw1fXotNIqhAWi95xgN-aSuMh1QmjxIfCKcgwmF9Y35v8wdTkXjF_k93HxgfAbVN_1bUVaJhhwxQwrFXpKpPzV3gnLyBWedERgwVMKASNMQEYCs-eBfvMW0KTPRS4TkvokIIGJ8DbfC9dfSY5VDswOE2-MnhFYFttq-dpZE-ERnWwUqkwiJnV6JhVSbHb9xNpxTUUwOaIYsu2tbpygtd-dLpWH4_LqNAHBccxvFziFERLjPAeCuOweQzNW48MvtO0pW0HV1ym-3Xx1kFz_nGjobmLFFBipg8uBuFALq5XqHJxtxLBSMEm3gzDHkV85FMrA25wI0lLyWTyudAv6lYYLcmQxtkYL4rTBjOml-ECuW7QY_sPoHST6N2tOpkU9Z_MqFqT3lQ1dicSaSnaYN_oEEpnu-XGv4LHS7k3kKD783wuKNd6MeSYRhWAVpQLcPoBYLWu15HeLyEZQT4U3JXyqyK7Nre1eZ9SSYoOxAnBG5R0YB0Vor9DeZr06yv5OgoCnRcnDN-uyuKC8R0oVfCJZ1ByclL0er6KcuglfsBPOuRZele9OkHSN7wVDJpdKtepz3mPpj1JdyvgwMPCvMQ4VD_dBAmO1sv0WE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهبر اپوزیسیون اسرائیل، یر لاپید، درباره جمهوري اسلامي ایران:
من از آوریل ۲۰۲۴ می‌گویم که کاری که اسرائیل باید انجام دهد، یا ائتلاف باید انجام دهد، بمباران تمام تأسیسات انرژی است... تا مطمئن شویم که اقتصاد ایران ویران می‌شود.
این تنها چیزی است که رژیم را سرنگون خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138227" target="_blank">📅 20:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138226">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRYk3KLw8JnV5yS0bCOsgalG7ZGbVcy7e5UR7eY55i5Y7MNzmMSi6cKz4kGhe9__MYxg02A3lkVqmeCxbDCieRYSzUQ98g2zs5nMA1Le7yXgnnaJDD2hU6aeNayOM-EZ86KP_bmsRXb5LHuIGO0Yg_3IxcfsGiIolqi4RFP7PzRPujIs4dq6TGV9X80r521NAsoysKcrCfduWL40-jzreHH5LoDU3nucFN5gee-_Wpbt2O6CWr9UYN8jmv1LuhamN81oOjeAmBjLxeFw-5uuMaTz0tJeGzNDhdsKyp0FsR6yG3JMbinIgZpYNbvf37MzLDaP15bTPgr_SmA3lz6h7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138226" target="_blank">📅 20:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138225">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سهمیه بنزین سه هزار تومنی که ۱۰۰ لیتر بود به ۵۰ لیتر کاهش یافت
🔴
اینم بزودی کامل حذف میشه و دارن نم نم جا میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138225" target="_blank">📅 20:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138224">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کاخ سفید:
دیدار نتانیاهو و ترامپ به پایان رسید، جلسه مثبت و سازنده بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138224" target="_blank">📅 20:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138223">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نیویورک‌تایمز:حمله اوکراین به یک کشتی ایرانی می‌تواند دو جنگ را به هم نزدیک‌تر کند. این حمله در دریای خزر، یک رویارویی مستقیم غیرمعمول بین دو کشوری بود که سال‌ها در دو جبهه مخالف بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138223" target="_blank">📅 19:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138222">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57cf711cfd.mp4?token=VtjVHJgq5je3oVemam7RN6xpd7etZ2pzrwrxpNXTm7dYOMxR4LQr6Gc4FtHqLsB1w4o91PGSt3AnLn3qTFE00qZu5eeBiAaB3CbifBJTjwYRgMQ9ReWM74REt2hLFn3jflmwgBkfr0H34U6LYq9JeVAxZh8wLaKCpRrX1UQhaebpfJ01IBbDzy9_CDBhVCDcFzM3L0DIW3AvS88N9JmbF9ks8akuOQ-rXc75jvBAP4p2g4M4T_40HdKhr1Zf_bZBz2D7WXMZiQzmn5SH3yo9ZVNvIgLLgRjbU5FLw79zA932kjQPXzKHtQxfdAak7iuLCSvjHPI9-8q_e8pfEF4skA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57cf711cfd.mp4?token=VtjVHJgq5je3oVemam7RN6xpd7etZ2pzrwrxpNXTm7dYOMxR4LQr6Gc4FtHqLsB1w4o91PGSt3AnLn3qTFE00qZu5eeBiAaB3CbifBJTjwYRgMQ9ReWM74REt2hLFn3jflmwgBkfr0H34U6LYq9JeVAxZh8wLaKCpRrX1UQhaebpfJ01IBbDzy9_CDBhVCDcFzM3L0DIW3AvS88N9JmbF9ks8akuOQ-rXc75jvBAP4p2g4M4T_40HdKhr1Zf_bZBz2D7WXMZiQzmn5SH3yo9ZVNvIgLLgRjbU5FLw79zA932kjQPXzKHtQxfdAak7iuLCSvjHPI9-8q_e8pfEF4skA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون حقوقی وزارت خارجه: سیاست جمهوی اسلامی این است که تنگه هرمز هیچ‌گاه به حالت قبل از جنگ برنگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138222" target="_blank">📅 19:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138220">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jEg-Osw-Y0P6ktaDcNO9vUGc5WZQaYoVs871YfcbhqSYay5dj1cGhSzEQZDHOX0Aj1A0ftb2h-u8qJlL4mdsv3erYfhI9HYEdPri8RXzu5H1l5Nc4cVSuy4VQ262DypvQn8_NkL8_CG9jm9p4zpEWCEd1HpojG4Wg26DwqAJxoGw3_zFi8tXLeHR3W-xlPAiujIdAKQAxAjGzFexloBxXEDqhLstJPgV4J6EYzzmywBVMM9tqtDdhuFcicb4JBBIXY0MYmVqBNinZxuYlR2Vo-UY6Ec21WJ3vznEpwUS7ZXLqrjV30ufrwVY0AqIPmL1HKSneaK3rPvhZeoXBXM0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BnKWdc7ZYO5MX02sx7oyBseRaCzsgUEXsPRFTp6Y03EmNW3NSpscseGz69_yVIH34Fi43oxuoFqRHHuYxLz9TWsS-mfUOtu6661OUJMxh_PBiUytAp1Jb_66a7aLrNNB8LvtreyBGpqsb1tHChIrCHQO5_41w0AaoNL1zuW8A8VN7oqOtO20hjb6TztsQUe4kqF1VNbdEbN-SP7V49dGtYPC60V6DcPpFgu_xFlH4rqImGAa2DqJPAiAQVMAVXZ1esEc2odTuqdpUKuKjdzkVAeOfmZXoO5fxAqZCmGU9uN7ZOOagEtsbI0_Q8QspyejGHl0UPfHdVghklh3gg9o5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از فرودگاه بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138220" target="_blank">📅 19:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138219">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
زلنسکی: امروز دیدار خوبی با ترامپ داشتم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/138219" target="_blank">📅 19:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138218">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اولین تصویر از دیدار نتانیاهو و ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138218" target="_blank">📅 19:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138214">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riy9-3JPiNmq9kAdXw3CTdvKISGD3o2xAUtN3zQZ--Fpa-Hf_BIYLqfRanvFzK_CoB6Rg9JIfJEhm4h-ojpEyXW_JQJk45GP7QTwdKfvns-2Ia9fAXeRe2DJg_iWKqWIvQso-mPnYM3rwnm9yYLTKg_HxHIR1I6jsO2SrdwXg99Kcsu9l8_zmZyO-HQOJWL_Y8v_LYMZhO17Rt1USZ9-XE_YUxO8g1m_0DEf4KaSXvjqdaxBx9XMC4wNRDisBxph__aO9DMonwlnwxP0ad25iEsuKbMVJ1hmsXhnh7OS87ay3QCkRxLxC0copQwhMHcVzizjpJjvC2L9bKIMfJ2FyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKmSCttkujnfiV4GCH3taw7n-pP1cNJxC-LnJ-3TSixwKHkMtX2tDQXwt_wFGSbT9schHjCrsQt7SoPNyVo9cltWzIuqyz8a-cVDj1rJ1vHMOX4WzSXk4Mblyh54oBA6V7VvQf0hWWI1YRBo2O8EGmqIXfbch5keNWx8-BTpSLD7fcnroVBQb825uYGnD8i4WUpzQ7W3CDzpLihpcIjsa9ScKRWuZ2NGocLO0HNTKK23FstUhT0wUACxWIoG8xWwoJD2jNmhAMWbm_XnOrh_C1Ham3hdI3A4jkALG7OoWYNVdiVZN-c8dc2NsRG20zlCUpJdYcSiMKNm7OptZnIZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwLA-UeYxwaoGYXQavVr5MV4UxRnqFu-9_0wZ-3SuAzJNswnDmLRlsbtzPEXMS6Z8iuxHGC-7A-q_op81s6dXCuJp_mMA8jJv7Kk1YcJnOCpxqdt5p5sNYp8k_N4MszVp2CN7HJypkk8hE6wNAR-4AKywqj1Xte06EVLK5S7h62Lvya7fMcJugw6e0WZJxXA7Q2Wqo70rTHQCAdZqC6bXiRUS4cep65BUKcWNBQJ7xvDtGy4qMPupuCKxBpdfmAVKQxETKAf_DuzQtsnn5Hjc1yxnWEPc_kLYr5HgEQeaeqqmtPO4-C62aGmazLyEiZ7HhkqZjVFllvGQQAbckruIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTchlRurzGGEzdyAMH6rMRSwaDeOrJpRI1w6H_BNSe839CpvEAeDp3cghetLaPu-8E6tLBcWnH6dC_W_eWFDyxnaEBnEycwTFoiOdoZIjtNgh4ppPjsgrG07l5ujfzXnjnB7ztF6Zcd7U_KBNtgRGas6kMIAJXxJBNqHGCbT8T7jx0iuDeUw-DriPiIDFoam6fkaXz7YQxZWlqHCLkmxICVxVRr_AzwP7A0r_wxai7SGVJouiSyVkdJ-wOSyIs4hh0dnoog7tvgVqBdy8w2JhXbBjO3K1NLQUw3RDlFGksPf9ibmPVE0BYQJqorZELBMK1e7PtT7DPhkvUThqXzIPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون دیدار ترامپ نتانیاهو و هگست و روبیو/کاخ سفید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138214" target="_blank">📅 19:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138213">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvf2d5mCOSnRE3cZUzftB7HIOmlekZ2QkcGw1de1ZvBlsAd_zUGSbA78Aq4uF4mgHK_dsKZ6QKgG8SvRNsLrjPjulsCrgmdhP9Rm7nwW2r8a1sicDdgouBeEsbZ8pkw7bZTJjxd4FkfKRAFCUs0GY_fcY6W6iSlatvDSKT_jgQidVm3cgtQCRex2Zw6FjBlDRRHB7FCikQ7AnjdgA9_yecMM0EHAIaZ3OVNyCD5t-Uco_aI7dx73__ayR6ErvFRhA-DM_g7pl676x7ooJxxyVP005yqKIXCmgS9y-t7ozIh6dEefG31qJpsphy8Da2MRx9SDumJ3HajQ3awW_Nsb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین تصویر از دیدار نتانیاهو و ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138213" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138212">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
لایحه جدید سنای آمریکا برای تحریم ایران
🔴
به گزارش بلومبرگ، گروهی از سناتورهای آمریکایی از هر دو حزب این کشور روز سه‌شنبه از توافق بر سرِ لایحه‌ای خبر دادند که به واشنگتن اجازه می‌دهد محدودیت‌های بیشتری را بر خریداران عمدهٔ انرژی روسیه و ایران اعمال کند.
🔴
این لایحه تحریم‌ها علیه ایران را تمدید کرده و صادرات گاز و نفت روسیه را هدف قرار می‌دهد.
🔴
این قانون، قانون تحریم‌های ایران مصوب سال ۱۹۹۶ را تا سال ۲۰۳۱ تمدید می‌کند. طرح مذکور، تحریم‌های اقتصادی ثانویه را بر شرکت‌های غیرآمریکایی که با ایران تجارت می‌کنند اعمال می‌کند، تحریم‌هایی که قرار بود امسال منقضی شود.
🔴
رأی‌گیری مقدماتی لایحه برای صبح روز چهارشنبه برنامه‌ریزی شده است.
🔴
آمریکا در چارچوب یادداشت تفاهم متعهد شده بود که در طول دو ماه مذاکرات با ایران تحریم‌های جدیدی علیه تهران اعمال نکند، اما تاکنون چندین تحریم دیگر را علیه افراد و نهاد‌های مرتبط با ایران اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138212" target="_blank">📅 19:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138211">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
زلنسکی: من با رئیس جمهور ترامپ در مورد روند دیپلماتیک، احیای آن و مجوزهای تولید موشک‌های پاتریوت صحبت کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138211" target="_blank">📅 19:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138210">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lopBt_1p2I4m1oapPAAaCqQX0OBykoGUhrPzFLhdyPVF0uokj-tZ301dq92lr24Qmtb1hDj40C_XbvRwnfeTevJzPmctQaPl9cdqvRG6MtX81CuTN1VxSY_JGl-L4Bw8McBHSugDBrZ5QdsPRBtdK7ozbKRFqG3XfXOrA4oVFkApa4ZY6pIqEoeHJIPEYJVz2BaK8kp37AJU8cOoIYtr263JmXR8Mal77KWwDpYVa7_ZHAZranjHyNWYcyy0KFsMWkKus-yJT5ESRcWSwRV8nUdKupNldfsC9cBX6KmDFOLVsdIIO4eNVGafS--LThyd0WxqERLeUuIy0-Zu63XMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطر به تنهایی ۲۰ درصد LNG جهان را تامین می‌کرد و دومین صادرکننده جهان است جنگ ایران به توقف صادرات قطر منجر شده و بازار LNG را بشدت تحت فشار قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138210" target="_blank">📅 19:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138209">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N81OHPR9XuDHCkkUD0SuCiJxlBL40ybYA53QwCK4R6mO43NzKovvRUxjQ-P8qACceiQnHvNtwpuuzZFY1oLCR9tNPBVYP3uqumeta9ogRQsisJnotUq8uycnlFIz7yI6-yttZKhmk9OLX-FkcLbcV_CZjC-lMMmE3Meb3hDTu36ASopLgLKkhrB3wKzg5OORGhu_irFPVcoBVmBPkMkjwazQ6lhhBkf4alQcIgmq8UnSSoIiife-NcdoW8Yqe4blSZiBdUf7UKNqb8GRejyraD56oZqIcH1Y8kbUO1EkTlnLOp9138EHeDcDXyArSc7jEPBh_3KXijJGj8-qcTvYow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین در ماه ژوئن ۱۷۳ تن طلا وارد کرده که بیشترین میزان از مارس ۲۰۲۴ است.
🔴
در نیمه نخست سال هم در مجموع واردات طلا چین به  ۸۲۰ تن رسیده که دومین واردات بزرگ در نیمه نخست سال و پس از ۶ ماه نخست ۲۰۲۴ است.
🔴
چینی‌ها در حال خرید طلا در کف هستند و تقاضا خرد برای طلا در چین همچنان قوی است ETFهای طلا در چین هم با ورود پول معادل ۲۸ تن از شروع سال مواجه بوده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138209" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138208">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، برای گفتگو با پرزیدنت ترامپ به کاخ سفید رسید.
🔴
این هفتمین دیدار نتانیاهو با ترامپ از زمان به‌کارگیری او است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138208" target="_blank">📅 18:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138207">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
باراک راوید، خبرنگار اکسیوس: یک مقام ارشد کاخ سفید گفت «ترامپ در مصاحبه با شبکه فاکس‌نیوز قصد داشت پیش از دیدار با بنیامین نتانیاهو، پیامی قاطع و سخت‌گیرانه به او منتقل کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138207" target="_blank">📅 18:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138206">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
زلنسکی بدون برگزاری هرگونه کنفرانس خبری، کاخ سفید را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138206" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138205">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6k0j_rKL9f8v2kiRIhh-N59-dHOMojHbbDeUJixLAQbvlfG9EotmaNaNBCGWLQ95SkNym8L6MFntausIzEjLV7eaSDPziDulL2d9gof27TLbqQjOa_vdFOqxwHYEe8hpOPST3krEJ44NqBod54va0Z4i40FHANwPqjRKRFElYiW5ldMoeqjO-fh2KuD62iYLyWAaLz3M4SWknbRg2nqNTXI5liIAr7FyzvjyG-FFf0_9kd10nixRSztag1O07l7ykA71Nj-pkewa7h7UXObTL5JZ5HYo7X7avUJxqW05DycSBT83XtW6qUqtNWnC2WLtZ38RcLpgWupTQD3KPijOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندار کاشان: ادارات یک هفته وقت دارند تا نیروهای مجردشان رو شناسایی و کمک کنند تا زودتر ازدواج کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138205" target="_blank">📅 18:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138204">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV8yIQxKkIA0pn0xYogP_SsKsq4OpNfe158I_7nQXHE65_wYAJzIMnXY_YNamUloo9a6ESSg5l9X0iKeRGbyQvNdwcoqebv8pPpy070fRg0hGyyBXTBzo-iSVyXVT3HaLIgY51yp94HNboOB5yYySnOb15vR4CQ3d85A1EqG1V9iZxvwbXHFI-nhKLDPkV6w_t9yra7ZhMNQzhTl7trwy6XYT963nc7HZpFv0h4wGKg8t1eiTsdJaurX68DClqDPxU_RXI2j03uRAs9KkKx_TLXhkOpbXO_3TtpDcaR7s1lsJ677H-rn9mE0oX-cC6kM5tSRF8lQd1WFfi2tA_Qh_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده نیروی قدس سپاه: دولت عربستان از تجربه رفتارهای غیرعاقلانه و پرهزینه آمریکا عبرت بگیرد و محاصره یمن را پایان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138204" target="_blank">📅 18:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138203">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRBTkCKVLaTLQheGGngUTp0nXo829HW8xb9uvOAOskkGTYksU5CTs_BgNZOBJn8CNPgEKlvehHtw7ECAnjWXRgzfV99WRxM9lswE4HhaXYL_T0uLdsAEeK7NeVxvZhvCN84sELCIl5jdcJlzfcVUA5cygen1meOgS_AihK_MI_SZVUpsKkcF-AO3vh2FzC9hxB2DbkJDBeGXt80Ur-IYKX--dmom1f2e1HB1dtPfzPuBI87mZFBKagQT9iO73Du4JXFEtORIXq3iEVY6n7QB9U0haZCcrsCThDVL2mVZ7HPnSdO6S8kPyVDxIq6H6K_gNorO22eCdVDDIVpssku6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ورود نتانیاهو به کاخ سفید برای دیدار با ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138203" target="_blank">📅 18:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138202">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f588936643.mp4?token=EYJoMzNwejB6dI0sFNZTcnb3cBVt8Wa0cLlliDkE9UY-mbNaijZ_RB4t_tkIfCB1TS8nMakV_O81gBTQbs8xBHqnO_lFZV7sHgZ_4t6lNQ-nt3NdaDaPjEJDTQFlfFqeG8R-wc-Oe_UQg0luievitfUAm6rzLPrBW64SWLj2vIHb0ImivJ661IwXAijQcjKGh1M9tRaESHQZlf4UDIDNZuoR_Q7B3DmfTaOFJSlZWnMzt8SGoBGiSiF-6sTjwRmyZfAaEe5QOrnigqcHdwqmb3scnuSusYyFFlsLBjxWUo3aktXlfLWpRj6PFxh6Yn_yf2zz7gHFsff_D1L70VT5PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f588936643.mp4?token=EYJoMzNwejB6dI0sFNZTcnb3cBVt8Wa0cLlliDkE9UY-mbNaijZ_RB4t_tkIfCB1TS8nMakV_O81gBTQbs8xBHqnO_lFZV7sHgZ_4t6lNQ-nt3NdaDaPjEJDTQFlfFqeG8R-wc-Oe_UQg0luievitfUAm6rzLPrBW64SWLj2vIHb0ImivJ661IwXAijQcjKGh1M9tRaESHQZlf4UDIDNZuoR_Q7B3DmfTaOFJSlZWnMzt8SGoBGiSiF-6sTjwRmyZfAaEe5QOrnigqcHdwqmb3scnuSusYyFFlsLBjxWUo3aktXlfLWpRj6PFxh6Yn_yf2zz7gHFsff_D1L70VT5PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهبر اپوزیسیون اسرائیل، یاایر لاپید:
اعتماد دو حزبی اسرائیل را در ایالات متحده بازگردانید. چگونه؟ اولین قدم کاملاً واضح است.
🔴
بنجامین نتانیاهو و گروه او از افراط‌گرایانی را که ما را در داخل و خارج از کشور از هم می‌پاشند، به دوران بازنشستگی بفرستید.
🔴
به دنیا بگویید که این یک دوره دیوانه‌وار بود. یک دوره دیوانه‌وار. و اینکه این دوره به پایان رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138202" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138201">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق: مقامات ما چند فرد که متهم به همکاری با اوکراین و انجام حملاتی در داخل عراق هستند را بازداشت کرده‌اند
🔴
مظنونان اعتراف کرده‌اند که برای اوکراین کار می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138201" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138200">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نتانیاهو برای دیدار با ترامپ وارد کاخ سفید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138200" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138199">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8bef0b40e.mp4?token=gyNzqspK_-2HHPbx2eBtg8L5203h5nUR5MfNChoeahwuQkT_M5TSpwiXCPM69IKzMayXehtPqdkjrZep2z3OCJZ5PkkS6fu6nhbianjLq1i-C64Jm5AqzzRAkFPkd4iCE-p81iXaW83hpI1tzQr3AuHXpZDt0DaBbRrjK842H5mUahixvsbYRbpYevl4SWmqGIKVvOCJ963d0B_fgSQOY1195i2aJJgY0LWqyqaUw6b5fWcC4BxjN-vB-j58L-Xh09rDdJEMBr6iO1uX3Aw2CSOxMWG9QXZ9vvBzE3i9VYGCGHBQoVIMKBSBEV1NLaxrMNbBP1HINz0FX1PzR1PbNBoQDkn_IkR96yrNYZD9xc5tod9FfqvjPVP7KpTUk86oIoP6kh0icfOn_HVdftyXZgLKs6PJdqRHCUj-rm_nPqD5LZE6jgFW46vparTBierjpvmrGLhkxwAMishERJHY8_B67umct_HdnAwm2ZU07kJNxNlTWsnPoYN6Vdgl0htcHWkCVs6iWNodiNHlg5J8baOvNMBEsxFsoIJ7Wm1ZmlI4bZgqhGwmPnTlFKjmvE3dXZn5oTu1AL8mPeisPpZhPrMFjJA7F3Tz1Q0B6ODoHxI4CLnBqUixpxPhmw3t_EWq5uRVTrkD7d4yUuhSg3ReDTwF-bwk8BHRFxl5Hz_rHVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8bef0b40e.mp4?token=gyNzqspK_-2HHPbx2eBtg8L5203h5nUR5MfNChoeahwuQkT_M5TSpwiXCPM69IKzMayXehtPqdkjrZep2z3OCJZ5PkkS6fu6nhbianjLq1i-C64Jm5AqzzRAkFPkd4iCE-p81iXaW83hpI1tzQr3AuHXpZDt0DaBbRrjK842H5mUahixvsbYRbpYevl4SWmqGIKVvOCJ963d0B_fgSQOY1195i2aJJgY0LWqyqaUw6b5fWcC4BxjN-vB-j58L-Xh09rDdJEMBr6iO1uX3Aw2CSOxMWG9QXZ9vvBzE3i9VYGCGHBQoVIMKBSBEV1NLaxrMNbBP1HINz0FX1PzR1PbNBoQDkn_IkR96yrNYZD9xc5tod9FfqvjPVP7KpTUk86oIoP6kh0icfOn_HVdftyXZgLKs6PJdqRHCUj-rm_nPqD5LZE6jgFW46vparTBierjpvmrGLhkxwAMishERJHY8_B67umct_HdnAwm2ZU07kJNxNlTWsnPoYN6Vdgl0htcHWkCVs6iWNodiNHlg5J8baOvNMBEsxFsoIJ7Wm1ZmlI4bZgqhGwmPnTlFKjmvE3dXZn5oTu1AL8mPeisPpZhPrMFjJA7F3Tz1Q0B6ODoHxI4CLnBqUixpxPhmw3t_EWq5uRVTrkD7d4yUuhSg3ReDTwF-bwk8BHRFxl5Hz_rHVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور: ما تازه از یک رویداد خارج شده بودیم و در عقب ماشین سوار بودیم تا به رویداد بعدی برویم.
🔴
لیندزی گراهام داستانی درباره دوران حضورش در مجلس نمایندگان برایم تعریف کرد. و اگر دقیقاً همان چیزی را که به من گفت تکرار کنم، پایان همیشگی زندگی سیاسی من خواهد بود.
🔴
اما آنچه می‌توانم بگویم این است که آن‌قدر خندیدم که وقتی به رویداد بعدی رسیدیم، دچار گرفتگی شکمی شده بودم و به سختی می‌توانستم صحبت کنم، زیرا لیندزی گراهام می‌توانست هر کسی را بخنداند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138199" target="_blank">📅 18:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138198">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6531958cfb.mp4?token=FhgOe6JUmORSIc3gt8bW9-k12uACqtTY1JbkMliPDf2OoCiLfuWQPzAwEdEiYXn-Nt0PpmtR0yJGpCf8UMoHAAQn84BQD7ASv_o8fAjNkRl-6ZWqcD_a7vp5Vuxo3QG23y82C8sy7G-apsD_7qGKDIFnvUZ_tigNCXNx3dCowvo0Hb2nV8UOzDRZiBBYLXD2Lr2vmRrHq328rgfF1uT43AjbfLIJbTP3Bu6E-8K8WpUOKqx_aKT4c3V6PcN6jDTlWpjgUg1vdLPgfBJc5pZFkZq0X8cFCfHz6UBddWkawXOP9ajNn0Gri87R6poO4HtWFlc1LF9S7MnaqlTrZsahfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6531958cfb.mp4?token=FhgOe6JUmORSIc3gt8bW9-k12uACqtTY1JbkMliPDf2OoCiLfuWQPzAwEdEiYXn-Nt0PpmtR0yJGpCf8UMoHAAQn84BQD7ASv_o8fAjNkRl-6ZWqcD_a7vp5Vuxo3QG23y82C8sy7G-apsD_7qGKDIFnvUZ_tigNCXNx3dCowvo0Hb2nV8UOzDRZiBBYLXD2Lr2vmRrHq328rgfF1uT43AjbfLIJbTP3Bu6E-8K8WpUOKqx_aKT4c3V6PcN6jDTlWpjgUg1vdLPgfBJc5pZFkZq0X8cFCfHz6UBddWkawXOP9ajNn0Gri87R6poO4HtWFlc1LF9S7MnaqlTrZsahfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس:
لیندزی گراهام به عنوان یک انسان غیرقابل نفی بود و البته به عنوان یک سناتور ایالات متحده نیز همین‌طور.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138198" target="_blank">📅 18:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان نخست‌وزیر عراقی الزیدی را در مراسمی در مجموعه ریاست‌جمهوری آنکارا به گرمی پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138197" target="_blank">📅 18:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfQ5KNgA0lEOLGOu6Sd4jWaZPwjxBHjWWugzjsLF8a_gup2XSdcTbpxtX2GOfEdndh7vxqFPSHwrOePo4p4ROvQ9pg1YOSVk0YNQJmhWwUZSoIkyxcD9IQzuvqQtDfAGiNVft2Tgg4pzgkS8l7jjHDfaD13PIyLvkLBZDJUgqjdm4TgAImX4pv-FJ2D7M5OaGITGtZHmNNoO3809ebL-OrbxPvkmWk_gHf7CNzcYI3uoUakA5y31YCJSq5tv4eXDqWJAUc-vbTaATquIiVeHTWettCU7ZeAabkA5aiKYJL5EbQNPbtCFwF0rrxIJRSnuegzX-3XoQ5bVWrFLzrVs9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جی دی ونس با ۴۳ درصد در پلی مارکت و با اختلاف نسبت به نفر دوم یعنی مارکو روبیو، شانس اول نامزدی جمهوری خواهان در انتخابات ۲۰۲۸ آمریکاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138196" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138195">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlUtcgLNm2su4unu1qPESBsmXX9nayR2xBgWwxtXYqS5fLNfhMOpkyDlLoOhuwKxJAZiTG_w45KXqQdBHB6SJPVMXFShO1M0TqxGLE48PidMzjTuL9ihXcdzjqd6lrtY8h5SaiOqwYNTzAO6i5_dGhTSbEo9pIPAILt1kXYrA2n3qxspbj71tU-r6FGyq6HkPtL131OGfPGhGg9thR8BS1evwDo0IWwOi0fLZwePPGuEwFTTpcKumwZjvfsmFewpKvce01CK3lUswAnsLU5S-Yw2d9WToQRyfuPmEBsWBg3YxuTsR1N1JLw3lIyNNg9eduRz1kA9MMdO4ntpDdtEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پژمان بازیگر عشق ابدی رو دعوت کردن شبکه سه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138195" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138194">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
العربی الجدید» به نقل از منبع آگاه ایرانی: تحرکات دیپلماتیک برای کاهش تنش در  منطقه و دستیابی به راه‌حل دیپلماتیک در روزهای اخیر شتاب بیشتری گرفته است.
🔴
در دو هفته گذشته، پیشنهادهایی از سوی میانجی‌ها بین دو طرف مبادله شده، اما هنوز به پیشرفت چشمگیری منجر نشده است.
🔴
تبادل پیام‌ها بین تهران و واشنگتن به طور مستمر و بدون وقفه و از طریق بیش از یک کانال ادامه دارد.
🔴
تهران به واشنگتن ابلاغ کرده است که پیش از پایان محاصره دریایی آمریکا و بازگشت این کشور به اجرای تعهداتش، اقدامی برای بازگشایی تنگه هرمز انجام نخواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138194" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138193">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e2bb8d9b8.mp4?token=G3AW-ggTLxcv2ykUB8Y_-Z3JnlVH7rXmmktDfrktSBlZZtu79MZGMoHRpJ0yWOe-NiVfHSFsLnxvDv6pTx2p0bvYJoZIoXbYfVmmk4b-PhmiMkHAkFpDoSf63SvTyNGGpINZA9i5FUNTa95n6MH3qDoAPQ6O3XIRhK-NsdhLqImuwia1eq6R9OGZ6KXD7FK07BlzXlMPAVwUvGS3RZi9e-Vm7WVoSGJF5noN5P4TqSGInAOv_tFPU7T3DufbbKCO8GeeGQkq63MRSPc3JnZnDmGrPqanRVoJ32JqY1PYcWlNTvnJb64vIeujiJ4AvVyphQxXeGQGMZuhxVdRMRa9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e2bb8d9b8.mp4?token=G3AW-ggTLxcv2ykUB8Y_-Z3JnlVH7rXmmktDfrktSBlZZtu79MZGMoHRpJ0yWOe-NiVfHSFsLnxvDv6pTx2p0bvYJoZIoXbYfVmmk4b-PhmiMkHAkFpDoSf63SvTyNGGpINZA9i5FUNTa95n6MH3qDoAPQ6O3XIRhK-NsdhLqImuwia1eq6R9OGZ6KXD7FK07BlzXlMPAVwUvGS3RZi9e-Vm7WVoSGJF5noN5P4TqSGInAOv_tFPU7T3DufbbKCO8GeeGQkq63MRSPc3JnZnDmGrPqanRVoJ32JqY1PYcWlNTvnJb64vIeujiJ4AvVyphQxXeGQGMZuhxVdRMRa9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی وارد کاخ سفید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138193" target="_blank">📅 17:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138192">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
یمن: نقض حریم هوایی یمن توسط عربستان با پاسخ قانونی مواجه می‌شود
🔴
وزارت امور خارجه دولت قانونی یمن اعلام کرد که نقض حریم هوایی یمن از سوی عربستان سعودی اقدامی مردود است و با پاسخی که عرف‌ها، قوانین و پیمان‌های بین‌المللی آن را تضمین می‌کنند مواجه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138192" target="_blank">📅 17:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138191">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e13ebc21.mp4?token=KLYk41pHZJj8FVGBPdE7NZu_T5cRdNYbSu62D7U7C4cd_i-RrPHc5g_knOimeFXpQqrkJLM24PoCgn6T3Kmu2_8GdbtrqFkaguLKru6eQLTSAzqLL66IqkG2JWDbM7MMLoMNnkDo9myzHGL47G8bOGD8sOyS0D2YRP-wPFOI9v7FIzyZF76RemivmHyAn4AHh7xgI-2AvwfPAPIdZwt99CEKpLjoo0CtBI8XNYnYfiOJMZA0vFtQN9OVKxTV_1YLJviJVu0jYJ6K_aEw0u_kOLspg5_ENp9DhW70YE4lcEIRfU19BblIJrmAxU4ZBRIeUFZ4qME4CHy2iUu_7qvWog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e13ebc21.mp4?token=KLYk41pHZJj8FVGBPdE7NZu_T5cRdNYbSu62D7U7C4cd_i-RrPHc5g_knOimeFXpQqrkJLM24PoCgn6T3Kmu2_8GdbtrqFkaguLKru6eQLTSAzqLL66IqkG2JWDbM7MMLoMNnkDo9myzHGL47G8bOGD8sOyS0D2YRP-wPFOI9v7FIzyZF76RemivmHyAn4AHh7xgI-2AvwfPAPIdZwt99CEKpLjoo0CtBI8XNYnYfiOJMZA0vFtQN9OVKxTV_1YLJviJVu0jYJ6K_aEw0u_kOLspg5_ENp9DhW70YE4lcEIRfU19BblIJrmAxU4ZBRIeUFZ4qME4CHy2iUu_7qvWog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای که دیروز گرفته شده‌اند، پیامدهای حملاتی را نشان می‌دهند که زیرساخت‌های نفتی عربستان سعودی در ینبع، در امتداد دریای سرخ را هدف قرار داده‌اند. این تصاویر همچنین آثار سوختگی واضحی را در اطراف یک مخزن کروی شکل متعلق به شرکت آرامکو نشان می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138191" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138190">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: مذاکرات خوبی با ایران داشتیم
🔴
بهتر است با ایران به توافق برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138190" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138189">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کیفیت هوای تهران برای همه ناسالم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138189" target="_blank">📅 17:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: بعد اینکه ما محاصره دریایی رو برداشتیم، ایران توافق را نقض کرد. ما دوباره آن را برقرار کردیم.
🔴
ما نمی تونیم اجازه بدیم ایران توافق ها رو بشکونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138188" target="_blank">📅 17:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
آکسیوس: مقامات ارشد آمریکایی معتقدند که فشار اقتصادی ممکن است آسیب بیشتری نسبت به بمباران به تهران وارد کند.
🔴
گزارش‌ها حاکی از آن است که ایران برای پرداخت حقوق جنگجویان خود با مشکل مواجه است و با خطر ورشکستگی بانکی و کمبود بنزین روبروست. یکی از مقامات: «آنها از وزارت خزانه‌داری بیشتر از وزارت جنگ می‌ترسند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138187" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138186">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FP4wpHyhbMRdbhfjkTlKEVbW_47EPKqfGRaqBDPakZHoccRehbnxDaoFHPpeYWwTqmztZ3nakhMZ03b1fjg7aUH4HULBB9yGwmQ4Pf3SFOPoakP2nbLHSdnDiO68KW9Qvfnu2KUdaoXc6eRTKwOdHIf48ghHtmdqkNAEv6q6TmKXEvaQ3cHl3URWuAO_E-ZDm6aLbizaXvRrr4a30ajrWIrCIOVrapSwL3RulMAJeUMMLc0oU1RyjxedVjA9OMrtFDvyqLoO9-cxvM5z8Yrl5xndIChNv207sD-t5wbqsZWhf_tm2TIPyW2uAUz0jpOonkEpgp__XbfkDncvQYsSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت اپل برای اولین بار از مرز ۵ تریلیون دلار ارزش بازار فراتر رفت.
🔴
این شرکت، دومین شرکتی است که پس از انویدیا، به این دستاورد دست می‌یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138186" target="_blank">📅 17:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138185">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: لیندزی گراهام خیلی با ایران مشکل داشت، اما این اواخر یک توافق خوب را ترجیح میداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138185" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138184">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
مراسم یادبودی به مناسبت درگذشت سناتور لیندسی گراهام، دوشنبه شب در هتل فور سیزنز در واشنگتن دی.سی. برگزار شد. این مراسم توسط آنتون سهناوی، تاجر و بانکدار لبنانی، و مورگان اورتگاس، سفیر سابق آمریکا، برگزار گردید.
🔴
در این مراسم، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و همسرش، سارا نتانیاهو؛ اعضای خانواده گراهام؛ چندین سناتور جمهوری‌خواه؛ و همچنین سناتورهای دموکرات حضور داشتند.
🔴
همچنین، استیون میلر، معاون رئیس ستاد کاخ سفید، به همراه همسرش، کتی میلر؛ مارکوین مولین، وزیر امنیت داخلی؛ و یهچیئل لایتر، سفیر اسرائیل، نیز در این مراسم حضور داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138184" target="_blank">📅 17:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: ما ایران را نابود کردیم. آنها نیروی دریایی و هوایی ندارند، ارتششان تا حد زیادی نابود شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138183" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یک منبع ایرانی به رویترز گفت:
عمان ایده‌های دیگری را برای مدیریت تنگه هرمز پیشنهاد کرده است، اما ما هنوز پاسخی نداده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138182" target="_blank">📅 16:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138181">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری / یدیعوت آحرونوت: نتانیاهو پرونده کوه کلنگ‌گزلا رو روی میز ترامپ میذاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138181" target="_blank">📅 16:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138180">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV3XDBX9d2x8s1LGJo7MogxtefIJL7urXahTCTQbHrNHdEKJ8KoAO1xSk1D9pAHy7HRiFky60mGNsM8Bs4Z1w_k8ecaR5zLoxEBOTlENQtmmUuFx8EBtf_xTy5ecCwlNot1juX3GtlwiBiVfcUgLJDjJkqDCrqhNtGJNi9gCIC7T9gboVM1mkY_Iqe239bMFyoA0erNmfoMvMeSYJ1epjF5MgjA1gRfPuCV-jcXKYxJ5NJPzNn3tc4VBuX411PatvOeQ390VOOWgtfVjK21Vwx5LDralM3y-QkofmdWpebwKVhoHATTih9eeq43xyc3pVApO0_P0NHO6FTYP-obMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس:  سه ساعت قبل از دیدارشان، پرزیدنت ترامپ در فاکس نیوز پیام ترسناکی به نتانیاهو فرستاد و ادعا کرد که بی‌بی در مورد کوه کلنگ در ایران صحبت می‌کند تا او را متقاعد کند که در جنگ باقی بماند.
🔴
او تأکید کرد که بی‌بی باید در این مورد خصوصی با او صحبت می‌کرد و به دنیا نمی‌گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/138180" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138179">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مقامات ترکیه در مجامع مختلف بین المللی بارها آنچه نقض حقوق اقلیت ترک در یونان می خوانند را مطرح و برجسته می کنند. اقلیت تراکیه همچنان به عنوان یکی از موضوعات مورد اختلاف دو کشور به قوت خود باقی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138179" target="_blank">📅 16:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138178">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ : تنگه تحت کنترل ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138178" target="_blank">📅 16:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138177">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f7a42bd6.mp4?token=tflC-O8AzyGD5UBRIdMbmDFapFTHfRBDtMJEHAjCWWLbbTR73aoOqV-5Sj0QlHn2zX0_8YCete11UjR66x1WTGiIYeS2EX9vdghrWoX6rlrmfxugS18SGK2yo-xiSTzxL6Yvgn5oZrpoiR4GqwM9CxE31hLixvEb8pGUu5WH68EiKcKlAVK_2L6IPhhCBm2HBPzwqNFB-Y7iYSNNFt9saXPQ7EH3OgyxkF7wpcGcdU7PIPkI_GJ0EY0_aYmLKtPI434xti4C0k5jJNepCQbE13aDsoHafkCgHuu9AZ4PDilp5AljxCRf6qU9z5c1JOHL22rFZ6e4ub2q9MSfUKFjbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f7a42bd6.mp4?token=tflC-O8AzyGD5UBRIdMbmDFapFTHfRBDtMJEHAjCWWLbbTR73aoOqV-5Sj0QlHn2zX0_8YCete11UjR66x1WTGiIYeS2EX9vdghrWoX6rlrmfxugS18SGK2yo-xiSTzxL6Yvgn5oZrpoiR4GqwM9CxE31hLixvEb8pGUu5WH68EiKcKlAVK_2L6IPhhCBm2HBPzwqNFB-Y7iYSNNFt9saXPQ7EH3OgyxkF7wpcGcdU7PIPkI_GJ0EY0_aYmLKtPI434xti4C0k5jJNepCQbE13aDsoHafkCgHuu9AZ4PDilp5AljxCRf6qU9z5c1JOHL22rFZ6e4ub2q9MSfUKFjbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران گفت: ما محاصره را برداشتیم، اما بعد آن‌ها توافق را نقض کردند، بنابراین دوباره محاصره را برقرار کردیم.
🔴
آن‌ها توافق را می‌شکنند.
🔴
دیگر نمی‌توانیم اجازه دهیم که توافق‌ها را نقض کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138177" target="_blank">📅 16:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138176">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/741fab9a3b.mp4?token=Nd2tVG9tjqMixzG5kPSHU1Lgr7IDpTgpwTH_yHJd0dYlh7hcvqkVe8XTDyi0a3Ez4smcsSwXuwVuxLwpZhAcmRO5KUiJSPELxlhcxmDSyrXyS9Of11klm810HObID6vHwI_RqCFnZqC5oR6z3qXWX_x7i_0yACYBRVLkQ4VYaJL5m5HBCutGqBjTC3nx7-9vP8TvmXVn78rrK1z5ijIAaJzwacZ7fkHn1aeXOG6GIgPy3LFmfh5SF_eCAxqpJinK2FF_Rl9Gtg3uyWdb3OiGoYvkKZU1K2sFIgyalo3QEyXZhbQzN0arfgw78FGW_4r4De--swNLrvXl8vBdiT_hQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/741fab9a3b.mp4?token=Nd2tVG9tjqMixzG5kPSHU1Lgr7IDpTgpwTH_yHJd0dYlh7hcvqkVe8XTDyi0a3Ez4smcsSwXuwVuxLwpZhAcmRO5KUiJSPELxlhcxmDSyrXyS9Of11klm810HObID6vHwI_RqCFnZqC5oR6z3qXWX_x7i_0yACYBRVLkQ4VYaJL5m5HBCutGqBjTC3nx7-9vP8TvmXVn78rrK1z5ijIAaJzwacZ7fkHn1aeXOG6GIgPy3LFmfh5SF_eCAxqpJinK2FF_Rl9Gtg3uyWdb3OiGoYvkKZU1K2sFIgyalo3QEyXZhbQzN0arfgw78FGW_4r4De--swNLrvXl8vBdiT_hQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران گفت: اگر من قاسم سلیمانی را نکشته بودم، شاید او به سلاح هسته‌ای دست پیدا می‌کرد.
🔴
آن‌ها در آن صورت به شکل دیگری فکر می‌کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138176" target="_blank">📅 16:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138175">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده و امارات متحده عربی توافق کرده‌اند تا اولین گروه مشترک دو جانبه را برای تسریع در توسعه کاربردهای هوش مصنوعی نظامی ایجاد کنند.
🔴
این طرح، که با نام "گروه ویژه سیناپس تالون" شناخته می‌شود، انتظار می‌رود در هفته‌های آینده به طور رسمی آغاز به کار کند. این گروه ویژه که در ابوظبی مستقر خواهد بود، شامل حدود 20 نفر از متخصصان آمریکایی و اماراتی در زمینه‌های هوش مصنوعی، داده و امنیت سایبری خواهد بود.
🔴
این گروه ویژه بر ادغام هوش مصنوعی در حوزه‌های پشتیبانی اطلاعاتی، حفاظت از زیرساخت‌های حیاتی و پایش امنیت منطقه‌ای تمرکز خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138175" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138174">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e377889b.mp4?token=dfZXCyyjoaaQDqkPXkk7CcUkpcz5o32TJucEWnsC6ROp9M3bJlEyPLVOCCpx3aJv6M6eLWW79D7NPjiUjSOOKicTknxFZOiPDcntcTlU3fg1PHo7SR_8plu6zmMZc9HZx2fEipAIxmdkzpugcihWhP9HAuV4x-FH1B0m4X6P4UKk7grM7meLS-yqTvO0kQ0neovU6E-CQaIdExNxynqu9IhovLMbiPUUXisIhNuzc2RrVrvfaSEnv3WVuIZq5P22iiJGOtsRH8YFMtCEIrReQ0IKwPLtcT7nxlyelnN1ri-tTLbHPlbjKU4ClQNcw0IT4us9-Z9weDBYzgjYIhSwLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e377889b.mp4?token=dfZXCyyjoaaQDqkPXkk7CcUkpcz5o32TJucEWnsC6ROp9M3bJlEyPLVOCCpx3aJv6M6eLWW79D7NPjiUjSOOKicTknxFZOiPDcntcTlU3fg1PHo7SR_8plu6zmMZc9HZx2fEipAIxmdkzpugcihWhP9HAuV4x-FH1B0m4X6P4UKk7grM7meLS-yqTvO0kQ0neovU6E-CQaIdExNxynqu9IhovLMbiPUUXisIhNuzc2RrVrvfaSEnv3WVuIZq5P22iiJGOtsRH8YFMtCEIrReQ0IKwPLtcT7nxlyelnN1ri-tTLbHPlbjKU4ClQNcw0IT4us9-Z9weDBYzgjYIhSwLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی قرارگاه مرکزی خانم الانبیا: هر شرکت و کشوری که از محل دارایی های ایران مبلغی دریافت کند اجازه عبور از تنگه را نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138174" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
