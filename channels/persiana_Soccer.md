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
<img src="https://cdn4.telesco.pe/file/gP7Gih_e1TfWC7ws5IrNMdfbarMNY8CbuOJ2deizAjVUQR_Xjf1bv-PDumnegGfyZ4VMQj20Qatd-PPyMjymY4vmltHDziOOEiW3KbcbA8KPW-WKt8Ap9Akx7pKOo6f6lB_mt2IQLg5l8Whn9ZoW8O1Ya4IPzwAyr4PVD_80QG2uKe8-JQ6OWjO3buC9-nZ3C7XV45n-8uxVnLv_Z5UzwwhjoSue5B9uhlrSZbQTDbXx-k-4f0N6mim2Hjkwlfy7BpywY9FseToecF6-KMEM9abKQaYGCcQVtj5ASh2TQVO_gNGOvA2Crj2PafftzmqAygWB-4eglPuCgBHCCe3_bA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 23:41:06</div>
<hr>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKhPC2kTVuKNFa5jO0OCEaIdjTqE02sZTArXVAT1S9ZCZRNzsYvwOYUTWxa4k7Uz4Me2Wwiy8RDqtshNROwup55Fi2YBnHz0L4lUfIx9yqFkl1X71Ci4CNtRJAEbWuetVjQcgUspOzQV9_dDb6X_mzBL_0qSHNW90MES0eMib5SaABihrzfJDzly-T4eSiHvC-IaAfg_jYS4wGLrNEwBUgyWFqJrXZNubtNAQ3FjuGSjI00h7KDvmEOGrdFZXq1qaeZ0N0TCbV_UAC3knjGRt98RNtZPNeUyEGAub-A3RJIEQiAqBpjgFpdGEgjZUUA87gUBjxnWk5WT6_jVXCdDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eniSSEHLNdYSVF-gF9hB-pN26jmHKmTRa0sGdcHyr4bnqH6y6aan1AmjeDcmGSlKheoh8XEK6SqoNNsxexePZRU0DKhgJ7eI__ZaswUoj2nnZaNHvPZ15Jj9qnEZmXlRNrWk9oq5nHEpoubYvDbNRuTw9m1nF6Gso_tmg67dBQva9j35GBlDjXlAn7O7C67nTcbGhll9b4R_3IagbUEc09YYGPkbJjarE04wVceLz-69k41VI6qTCqyp1-4S9nMHZS3NOQFLfsnhn3rDkRprAf9VKKU8CrkgwsuanzCblQS4X2zZbnjODxVrgU8ngQj9EhuieaY47G62pW6_z28Xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzI6gH2FyOllQAcazWbfOsqx0Xp-gqRycyCE62_LbLLOv0L2GWiRTVmGuvzgEswn8axgSIvuYsU4IZaFMgV5IwwjJCOLCf05e7PgRmHS-s8abKoNSLfOAoe-YpJ1K6WGZTQvr8NnMoCfU8gFHPibe4s-Vu5nD92IWmRicedaAbayQrFFC80tba5kxrIKTol07UknIohBSfIaRDnqTymZXi74PpJR3ncMAaj3TtECkjmtDRNuaeIBjhyB5zz8SyoRdjv8YXGP4dWNTaB6wERigu3AvFhlwulPdKbVis9C1awFiRdBAFOppjyVNffsESvpu1x-bh5nFPubPzItiYdeaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POPEdQE00uvwXeMSQ7Ki6XrKUZlG8qViZMyRQX3kW_wO2wmZYrdYhUVW-Q8cWv9AvMjtIDM_b3pqcrUW-g-0afTtv3qW4YNQwDx8sx2FOzjrC9oDlmK5ydtCCZ-pCqtlcdTSnuUZ7w7ftQWv06lATIcBADGUIjnjJDVuXfTolkbbvF2g-AUGb4S5u3uUnFCegjLYN0aatgTwE7ZVq5AKdI9dPkkiJFBqY1zX6KgS-DKHK52pyGio1mt8jRGzbNNnrI8TuQYdtyLzMLLzRcqLSVI61Yj8lCjrKhzYCx5yp4AK3KKZVrKDf1rfkWw_BGuc_GLeGLc7M8d9A3A-l0DLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqS8sRrVRy5vrVYFO8ANhfqpRkWS9p3x3-X4KV1BDmOGaESKaZkXr5edto7gGKY1VQrRfEoTM2sWVZlhXCVX7F75TiwPOn8fU7HDYOgLPbjmz0UmH6tzSiPD326MC2RILGFyGQUe4thglDrz-GLTsdRzsNfbbD7XiSghOHUiSj-u8uyzrYUmn4B5pCv5vaO1EQyQsQIpH6SghFVx4ZVL8179C83z-TfbfBveWFRI0QBHb11Vgx2AkZrm0zX6a3-S5JCFApSbxIdf3oxmiUDQkHXES75NbR4Si_6M1GIdCzmCI6TmoNicd8MWNWseepCky8idqt0JPxBSxCKyMbPTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4isEYp0s-xZLLlzq2Di7I2THPTywQ-Hb7i9wF45J4TGZOzoeVWSHWi2j3XW8Bc-f5llxw4nSbz5FKxW8gNryA2D4Dv4Et3c701QQ0ucVzmbGNqextyyPY_3V8MjWNu5enulXAPTSaEB1Vj08z0CvkvuveFphgGjoBEXUZPcKG9SYP8wL137q3EkbjbysWZjKKJi0gy_hG2KvVSntn88VHKVGaSWVDUpmXyTNYD0B3RDI7nCB9kjaw8ffGHPkr_7Bddn5E_E8PeJIdnZr78-FsvSaEN68ara5-Pc-jqJX0sApovSAhSmogRYDcuvWdX850MNjry4p3VqlxJuHnedhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDNLBSHn7CqbtP-LJH_IlkL51XrLIDj2vIldPRcc72f7Y6iRcr3nTcOrFRS_RSyN8TmTVvxhVGEXT1bpt-gluq1JRuU-mFD1DHfq7locnaiw7tS_xI3xajtbkfS8ZFbMLuDkryoAfggaqJGEZVPqqsNg_zlAnRZ6IwMJiegsDY3AMKIixAISi5P_hi1EF50OGOna4XFJnANmp2gHtWUBCtLPxrTReqExz4aVVmrReHwx-TI3yD9FTXUSEZ3DN9oDWr1PNuW2xDD1Vw1YCYfI9mkL0Nblq3S6txC81co3loGeHatqn2sRH5oxR4zBHXe-0zp2VVX_p4ZOCBk1i_yzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgakwr1s6-mQ5Y0r-t8g2SiHGm43u2XGxsxwnj9vRVAPP2E3TLPmb9ZwzzrK0OCBQKvFOXpy6cNIhwVDAXBVjZ-W0wrDn9-v3TYJSpuxFcFe8sUFlP0dHY-d9s4PHR2dD6na1fHRkM6nF9kNzimcGqKo-qNzF9-bYpseCeNJgIcrezh7gn-pS1cCANOEiBpYoRDVTeueQBtFwowcjqGpeGUUH6XzT4AI3OAnO4lprrsERZgT5QAG2lmfm6OuJgAp39w1la8Dme6d51aPkgvEXEdXM7YbKKGmd7QtZxhcFAiTpEZS2OwlfkjKPQ5VRh1ds5_-s5JC-eFMTH3Koo5LqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwaFqYb5pvwYCpJJqiQg4-q589168mhir3aIVBv9N6gzxOtKmRWdETp0Zt47Om18aQlHGDk_AD1JkagZq1GmLtwUNo8DA1FSzUUpwsVWNfDM4zNt5OVpbn47wZh-1oi6PhRU3h_CbuX21DOsK4hxGsSlzw3f3zASk8HgbfXb6cXCBNBmOvmZU4i8NHEQs221_ABDHrt9Mx01VEkGQMRrtcYi6y2nN2x-pX9OYEE96oISeUP22iZC9nWD6jnmWTRd5JUqvQwj-nDfzUIL5m3X21uOBRrht0ZhWwvtpMm4h7B1iNwQo3buGDuiq1_CmsudJNprfVlzxeiy3uAGQOSPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN-VoIX_PKsJKYMQnjmk-DJEJN5MjfVjxGB12oMT698r-NF2s89FUcTQ2G0n7Ygyo739Pji1h-IyYa2y0izIqgAh5nzRMoOOECyBknn8PbyQNascpF8GfBrqU6GL1CJ0ytl-20b2AwQlMNAaYsKpsO-QQuEOjFAJwHz3pEUTOGiQq1yi62p3JtwDaWBSk9O4URqBDH9sLf-p8TT7cRbOWcvZUvCw40m7-2TafufHSjRboNKGqreFGaVadnYgjifLTbDTWyx12LNPZ7G_nthtCO-K8nSHSYkt32U9NHCbyRlI8hmI2Bt3lmIuqElDOkp0ng8lxo8WiXG5Ya35VHKrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdQ5HU6xbeUIQEIYpsqQ63L7jB1yQWcNiTqqPbaCq9iQKl6O2cfqH1aLulBz-6UCaoDhTk409RoC-_nKPE66s-Xs7YrYfazYso9xaJY4hOxOWCgIzX4M9TwvGVjl8Kay4p-5nkfdsnb0_oyVs0AhqY56wj817aoc56NONMkBfk7vp9JAi4_rmRUEUxc_-fW0reZSRit_sAXKKzMsPSqXhwRyUDvtI_phrQ47_9yEbWneESvjsc8yup-H7B03F2h7zMERoUhsbiPP3-BZoD99XmWagB1J0Ykfes9agA5rIZUgSaWUq3Z7Dzu4C6qt2H9kN-WwXrpdQsXSOBs_Xc-f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRtqEdq0qkVD20Wp77paUnkfx_2rFhDb46Ev_jmQigViCpARdI7ZowrVqT0hG8z0ZqCaEm_pTs2LmbO_HeT75fhq2UVNgeLVmeoIU--d4maJf7Dkns2ZAAowJtkvmp9sRkdxYM-g2BkENbGjAEQPSXApI_Annimjqur-yh6F61sPfTF-1mq0hOZ6PTXz4UVKQQF6aqOfJE0zPrWaT_nXt7yh3laD6W8MxtemS27WLUWbwoDQTqy9eG9b1YPD_0ovRtI44i4TItwRuaavqkfQr5NtBS8LKom8UxZ4l9JTClBuaosvQShLkx3KfIszJlcMTyYek3ySBuasBKvrj3gCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26829">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPfxCx_-Ahoxj7VP5BDT8A5fwR5H87T0T6LbfV28CFobn41KOLwtoQ62V8ph9HD95IX_Hkgo8XrQrYUcBiJZYIv0lgtvC6Sz7JFwgO2QZ8qUymp4_de_m3wKimSXtLVSCx97QujTxnBlyy5GGiB-aELjcf_2uQrmAu9BrQE2Z82BWxDrVYd1LTl8766Vx6byaCcyzAGUHTrwoXCj4upIelDGiPchWJTgVD20GW4qzR_vWuA_eaY4_p5JbEpubIax3oMxihLa-mwf7HLYHaO6xVnrzwEVsc0yvCYW5U46Et5yb77GuWClpWxMYbdAqSRCzt3qTodtShCCEEA0ftmxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26829" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeqhjGsS-1tR7VVlei0Sx5M4jKZT5oZrLY9zGwwDnMdtMWR4_PDa0qKIwDEEHCQMVxZsf2NzmnIFsUO1NJtQUCkw79fCYqPyDQemHVCEZkD8U46Mj7QUZtrGI2UVxhg1wGg44p40aUqATGuSpn2CAmvYf5a0G7OdqCfxVJ9ZYeJ_wKt9rSpdPGR9_BF99GOWrVCjrRrmTs-HK-lObDXv0bYDk06VoKsfipi4c5OIPzqM9FI3eQog8FMa85OlquP57K0CdyioLMgLl-8VJN5s_sN9srgpQ-9EYOgW0lpb9bm5_SEWnk6e7AENWeRrNfYCSdKRpd0wnBuoZfiT5qiAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWuiiR5v7JNVv90V62DUm6FBfSWwJjNMNhF5Io5kA5Rg99jN_lG_nL4sAcQK_ANYyJwu5Uu48tz--A8ziOMb1we627xMBXe9gXVpF8lOovWw2Y1w8XPGxd5ovHYQZyMFt5qs8Md8aUHDg5JKszZz87VjuN_JrR_A1VB2uTZ2zP7ii2S2bkATG8hVlThgEMWTdpHffG7grpErgIA_52uQSCA86uxP_9k3Pm6DQyIMjXQ9l9JRZjgLOD3UXINTYnrjblRhr20hGqCBANumqYgooxMJsY7njINWIth4Qq3aBwiK11utfwg64x0hvIRE4JJVnzyszBhJS_tKT5AQGJviaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDz7VcMTMIivY_0ieRuoVgg6DCyAY2I2fVk0GJItEPfp5cICzcW20F0G8V0CkZDoT7G3naWMfMEe-Fd_mky6-H2dg8EsZ5qzd5sZPStGSTOvgqrJ-uuX0SyPxzfH4nAwxWJjL9MDjRd4Impy6bPY18fS8ACSAvvBBczItMmNELtqJkYMkAPYs_fSyCjPCi1Exn6jF156gYzsTC1oykYYoNp-mbBRmr0QKRUcup2i1RQUTl5k2mgbMO3KqhF7SL1QpUSF83q_J7plrYFoj81plDuzNrMA8r2VWkEtm2NmT5L8Td481C969HXbyKTzU4O72Hz45DdlAWUMlIJdYuA1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKWme0TEH_Jg-8QPA4e9JThdX-Kt6NO_BBH2JIjrpJFlIkEuIgKwDlRXdQRL5DdaeyBwsq9ymEZb3pP02atK7Z0cCEwOApi7koEo2Lh7V2zrc6c06iTZom7dE5xbUYR5xIQTY6DxDISt-Rnpa7wvUuD2538LFSwmTFV_3EZ13111QRn2681mkO8w4qPtMA-CP-h9tAIIuTBcqCq34pzKxqt0sjftlLZGeY38IAuCY3ayi5bU4cgUhI5Nl9DvY20JJuUNuJcOx7Z2P4BkDjGRdjaGdJ51tBOmGhKy3G_HE-XoYIOSV2tg-wR6img9f-UAXYr06gjIih1fcExuRfPEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1HpVsRpDDNDUP4U7KBDjC0kJwcxnZZJ-X4l_zbYg8j4nrVMMBaurdJZJhE3wF5oFptXUHscqplyxKeWvMf7u9RbM_OGH_PC3dxpaXszOjQ2W9X09xz5vMp-MLbKWlWd24BE5Hh8RhoFryUtlVlGDwJzf3LeKpQKT1ye_-HXeB8bOHTko7fCQLDiZXgxTDcKDOnpDK7b5zGn6MvaAMgT21qhaK0AVjxsiLUFC4e1u6ak9mwgI809CfFpTYHIjZ37y_kf8qtrvui4VELJh5eWxItbQvWTwbtg7xDr7HfXXYxRQsXPB1iYrnrC8fQ8mJNZgEyAPKKbTNNY6gj1Wmxyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4W2fumHRq5cUrz5IA8jIb-CGoXV5mC1xXmfMHst50SYt420xy3qIHWr7osrg31Rp9naShJRKjx1Uiso6nrGQKwAO-v7270enVKQmM4XYQudmGlH53xQso1oOrIp_hC_2PMcdKmHPaAT7Dhk8YY9p1Ov0khQZfCfG968Q6O8uy4Cp0HVbU1UOaPWP9wqMGUgM4JD5jJjVCdmmmjyLuFMzgNdLuBscWUgbFfUb5ZETg2VDP_BneD83U8y6BL3PNk8qLgElId6BA7JVlGp4gSbxLguONEdXzxSDqGQc3HeCvZr599kwYM6HdCSg0STe1_oFzG6AsYYSPQTocuEKB4HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhGF50jp9ycu7cbd56G_4H_S8-Sw5pY-b0BlSEET8jkmjI1AMx1NXP5Om02v5S8W7_oRQ9H01n4IOER-HHG-qdYh0oYhVWzW3wRBoFKXrncPKPvVMYguQ5oonlt5wqnaMRSnLrvJfHfYA8NTqcVxZ8s5ZfBAQM-yQI_3MeJkcRvi0BXeO7AzEJZKDGmx_9RIeP-wGjjx9iS6JKfhpa4JbFRTWRAZz7efRXJZ5uLBuMhDSRonbiUL6OANsJZ5axzSRjZcUTm5vMMaVCYQNuryCdZEE6wgxrGjPNZYHg1Ooll02_GEUx_1XMOAJG8IXpK9XL7uDm4q0Lk_bv6WqMSlzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax5TwQhfiBtAaurLEcFU5J7YwVToA7hygV3yuUqqyfvwBbdaxwDfEE04XKtGBatwcXndzYXnD2cd_5gAwpx9vA4f2bXpr-v2hO6LsQiqjfQ5Va-180sfNmVxwcmPuP3Q1O3m5IBqwNRrUfiQULX0hoXmgUITqrRthKQqb6nNwRotQAjJT3F64GX6EjUKPqb3kuGBJiHNuZwDn6N6jy-iJlQCJ4IgnYYFaxzpyWryd8qI56f3lp0VwtaHigrpA8gM4QneO2ejghjYvj7I4Y0raZDuvn41114hA3BW4W0twpq4xqyIL-eka0b9s3cOGyoNiBmtyKL5VHCAsuIVxVAWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvsq_PqlYWkSFU142De9mrVd19dz73UXQyLk-RHXKxtWQ_mni4VinjAUOTI_-whrEA1_ngJ_cfRpqW9mHKwSSi_lkb2TlJo0ly3QLFpxqGQmjqircElMwtTarKX1feucjAVSTSf9QVlgpjeWCXuq_-Gg3QagVQYot7CfU_UeSnb7a6rfPitScvkURXKnBEZZ9qiGxV2M9bXSl432RGOzxUZ8hI_pQfqFOI60Sp6nl7hJRMuxM7gkGnUY7T_--WcMMdSN5KMq0HyPdgLyoh-I8-p3mVhCF9d42rqEpvelp199ZdVBxx4G7hOOgZvQMiip1glueJsr2WlblXa1l_Ydmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjOM9ic8-rou644tw9MsuYLwPMYa2LgrtR29lKUxLZuQYTogdYd_R6SllmHD9ky3_TT58WHD4hlonTy7OLAzTdxZ-NizqGFgJzQWu_WCTVsAfHhKKQSyXzEYMYcV4ktIO_qZkfmW-NYxKFtXWCRnjyRE4VODXFe6Xj3_1ur3rQNIsuS7kbKX5gAb9dipjzYaJfOvKpYIvBgl1AR-iqHZdXwNLWymZTqFAGuKhQ28S8_-wJz9-81GzQ7OHfOrIj7b44NCjeN7_cMJvMxfq6BfuIXqgKclK1cTYTVMSZ4bQa87MWGK41p3DMkXMwHNzJF2wjxbsPCWzxPdgPgL0v3URQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drEpuKrEVlapZIIPU-5PUWDgWzSfKfaxKjj_Q9sLYwgRWDhxCJgZyhqmQZkA-Wn1KNDrBX60mlKHgA3yQwln-RBkdk1H3H_A_57-FpFyl6vLd5xyL0j1qz8jnXILS-kflLw2QMTtPczc1BtKDHVX6FULiU1MpuKuJWMcH_9ooqpHXWoOWQD28XIB0ZqOSEbJ6EHy3je77-GZN5LIQPypYWGGd_c0-7CdbrRkQAppqeboMCrFd-arGIWA8JQjZFMLXbFTUng6bjb_5Pi7-RV5U-79cXS-pCudB32xGB-wqib1c06SEYQnCGRB427YEp4JzfmHqVOIMk4wyVpJ_90AIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeqCHsVSmKcwfef0uuAfsyFAN89AmFOEDyXkbeieSqfhqe6Shy6iAieDcrxdALYIJiD0_y9y7hxgmHBSLsCLBdbGfw7PZEaU97bXYJa6ZZzNNz7pLXlmreXIcHiZQC98GH1ULMmWlimvanFblUsydykJbliUbo3xlvpoRoNsYPJD1DGLfFqgL1LFh9rZIXlMl08kndKozqfcy4Flju2B357xN07oF2dPbFsfRwQf5Z9yGpajf5nmaa_zAd5upWA55pNa5KtHrwL5Ky8Tzu3i2H1dBaAM_8eawMbMnlKkwGcoZBGofHcuRrMsZ00lJadZ8HKcpUnR51id61EvPpfi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zVqty7OpBMxPod8TM7LOLu6TH5agcQElx66oUHF70rQc9rinl-LNM_NwR8qKYCMX0ptzlrIkUYGhWg2YNZ7QswzWBbNw0j_NMZSMgT5zhRy9Ng_oV5X7IimxEzvU7y4W160t65lLyqVWQrplNmCnMj80GttzJr2qWBWGd9eKvH02InGYyOS9l5a64JZzcTx2RqpNaZE5WWsEdSkchMKDsxL9f25kXldK_8bpFjR7Fhj3_q99DrwHOyGMaLE0eQLHm-wlI27VW1AyGgNwAXQXo1O1AnEN7pb3SH-sHuAomsLj4suhgHQ_uLYANsqxkcsOKKGzYpu48D8pjqOHJGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEoujU2QW28HpXPT-yPVJcOzLixNW1Z10eTvA_th-lo5rc_971i9-2ZubA_Daxn39lCmmPQnBz4h1uTKER9eqHuhfZGj69REVpajqmJIPbo7AjP4A5cTaBfEVB8ogF3BUeIXadTGpy-P-VFdAJBs5bC8lRjGkepuBkPew-iEoWHGxtuea32kJG3e9fsHs_Hroi2IDHGfdagSzacfBy4q522GGCDxrLGJ4PJHezDkWJ6c-xVBdSqSeQLQDzN0FGkaPMjjize5Hqdpb47Kx43R-Swjrx-icokMQWDax1FP2aenEUNB-rtzyJq5B38aWvNnPqLHknHU8Z63xAP3HCH_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7vZombwTJZvayKQ7KQs9Jv3LwT0RbTPZrNG11zVVdBRHuKL-JfxBiCfX5MK1vDtHaXX7oJJc2KjeyR6XWPnJZtOmzYuT7yIVmyZ1riKLcE-PmWV1ZAoRJDQ7h9NBppEaKWHX_dIS6lgG2Sujo0A0n9zgqjblwqd-CQOvkNBWBvRCsonHsm8IrJImNT_m1P5Y3ECGKBBYc5_BzyYUhklfLzFSFzVkeRUHKZMbLPTUbsvI1TTbmWwYn8qxAXBorBNTa5Tol6btyv-lZy047BZp_WyLA15pjcguOtLVJXI18ltsex_c_FEWn7tm3DoDaK4dAew_20KEETabDQDIbZsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyRzXvBzn_7RwFZ6QGGtHQZGSnwDRa6uuSypUnqNHNLBc7GN2Kj7aQNydYdBMnbNO_i8GwXj85EXuf6IpjISmfNtj0DPpvs-SL3obchKCIxL0s1TXUbuZyekV2ZXiexqErrcDX9R2kskVRWIT8XSX89Cl90vauWUFU2bBLYLwqQK3y7KjFTFhkcJ5xR49t2BfHPmwxPIuSGt0YTxpYV_K_Qws7r-1GYIMSwHjXUNYo7E-ThhaJjB8OIppetDJtTaSPGCS8LnepysJngJctN3yfAvNUxVg8zi2X425isBBJQi3uBUmIUhQJIkxYJAGjC11pcP8-Dw8nCvm76RzGZl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26806">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIEBOR0qy4ny9MvDcJe2F2fJhoK02bLWjlRIt87zslVjeG37G9owh3RAnKb-aL8hNlz1S9CfmSANJoJui7Uvqnt7r7VD-GGCp1r-BKixDM0I-m06Ehr1nwlxH6UqN93HPaah2--7Qc1jnl8LyP9Vt57Vdhp6O5BbO0EztkZ7Ty-BUZlFivilPbjkQ8-EYrJK6hGhS4VpFvsz7zHgIia8w5S-umIfJXQ8lNi0T6dGCt3w-Wv3asde2hHpE7aHeU_XvXM-qP-CBicaoCle-BYqB1safCKGSLTrOQPwlMavYePCfW3SvZysCImo_b8zDErLL0Q07rCWXyhSkw7Y7BFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه‌درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26806" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0PrpqWZKu1mLPv3lxU6cAmAk9O6-LSyNpx_qKCs0V7hLogWJgR5JzUNKONW_1QnEnmYdGCWyHq4ZtXoHEDgqoVChDULTuwFKcK6HcrqMwQ5z9f89aTofE3_GYpCLNupQUJmN-8JC7e12VnSx_RNoHcmLO-GX49V3Q6wjYHu_ff4mFfH_MDNNwDB47c4Qexd5-EWixvmchKSG0FwMiNpXFrD-964EYClpnsK7D9uDkxqi-5fQ77Kdg4jIfS1M_nA-Moo0HxX63uoD4QU5l1wvyQS8wtpo6kD-YSPwqWnJpwPaw64LzhPKhVwQXLMw1UqyGkjG9h0LAMIrVBjGLkL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ple3gSemwVfU3UjSdgxS4UvTAm48R8c54wThlXKU-GM_wa5MrnKlQbyPjM8g68jKO3OLRC0x8tijFxze_sfomRnBEWG6SVM6MgiEmuB_z-sJbNnwiGZ8c99KMDJt5xjFnK2N3LisUSVLWJS8YIc53HPGBAoqwAV6NJNhn5C5qDF29IVN0f3W1whD4Ks_dWRw0JIxbjCQ0keTAFi0Y7AIBtnEdK3A23EHiO9ptk71R9Lwu7lfzLj1mYdbsSEdWqk1ELqQ1eDoNgHn6TqKsoEHHtTWRa3OZ8dhKmnRgh9UxWqz57oOnRMLD8NYFWCoMXBRsjEX-ItJhGzl-IsBCUgLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN4XLSHvtvBLsXKH8UCu2yhZvaggDImoB3mDvmvLc2TjQ52HdlK6jNHBc3NYqycm9bVS0szv4Xm8B2Fj1k-1Jw0CWoGfJyK3-2Zi5b8WmMmO5YC5VX9naIFYXI3Xg8C_aOb1RzyLMgEu51Tq98fV1ydRcgqnepcvALwuoX2XtJ5MNsFdlySi8nPROIN5XIYnxaPZZEL4Y-s7y7Kd6JBfAcMbZBwRuh0Cz9zPVgjMf4K1pzo0uDb3DL6wj1jmii-TasdRm1thkKylS2w25IaBrH3BIEc2araDnws8z7c0ra9KeFrNtwK-gh2CVCDctWhyPCAUQ_V7ogYKhyrOFD2Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmpeU4MBQRJs-hkdpqH5EhRp5HVyNNQ63Y0Xr8pRGDrMSPWqbkJT_tXu-QBxejKKLMaLldu1DdYy-kekMB9YHUB11F5rn7JKYvDDhtmJVteB5tTqZB-C0xZkmGhkJ19yOnAPEkMyzxCJXE2mgG1CybYu8sr0aCErdhw7FPATH_gT-9WTEx-Z0xyRubLZXuyVMz-x09XUqcFY5ZDOhD2vjtDnrYQwGDuNCJ5VwlD39fYUwZXzXa2loJebzhqHRFd9iHvri5FvBNJH1rTHzy4Y8t5ZLHtsPO7KnRnPl6eYLhsirat02u57qB6VwvEZwVDmp4CSgZV_hwmjKT55EKwT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsACNJ4YoHSjKfAX_iZ5HTKzCT_L3WFMnN6lcmHQFs0kZnWWoMmsEyckprrJAnnZuZ677fKzd84qWNSJ6NaeDOsT-Q8tCCVXwFxZ5CYMch7qjNODxOVJhaPyiioa_ADM9cIk6mRqI6ytACzqOxYy1wXZGhFkPFlo0V2F0A3lV4KKA9ZmfPZ8fRixMrXxZu5Drn6lnGMaZPsh-OmjAwiA1p1oRVvHjxB_dU4cMZj9BS6ldknNpOx2W3VYecAaLSdfz9otjJ9dimlKp0Bj087Fyyp_KTmKUd_9el0sXOSLql3t8XsBU_4X4_a-AjIzCXz7cgTIGuM9uyNADRLOXLvQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBcTR-r6hd5DRAGavn04h9FrXVCTqm5zE1k6pGMAz_iKtWdFQKxTtz_3VZDiNVlV4qZWBm7ZR3JHaO9C-9hHIIX6N13NmOGhnckkzd_53h6vtG0nsLzCFzFgdWoLp5mYog5lWp8zIcVFFhMHRCQTi4Z6ecUL_xkJl73SmsVMO3UyCNi94EGqnMxep8BVB140Hohu-05f3YC6MEGx5SwfMSleXfU0uIrBUPpCvWubg80Vd9brveF-y9HsE6LLLlwRjrLvw7lqI66moETnsKJIiZQz556TfUrE0NTfxsp0kgPEHxjVH8mZf_HY9emo2XIqyPqIVh8f2Ad9qVwiZNY55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=NYlMmbZtNPVMi9fi-iAUWcve6uczhaZw1BYwkAa4gSzwL3VgRcGTCX4rqBHajqhZ8ixCuuqVEw6CI7m7JZ3e8wN3HHlnKQs07FPHmaD-A4HWcXeozdVcqWLNk-qfzFpkZIdIMuPezcNQNz1PKpZdz4b4wJVHLhHnvSr51D3atNANMhbcvOg6e5UZF4WTxlVm7RhibboSUj_e262Wp5qk-tYphbv5tgn3qFQD6szAxQNoMi6pcbusfb47yR-kl28bETtUfgzZVWFi1bkH1p6Bx60q4WYyvSgoSSEja6mTGcphozVtakZ2zRTfVMFc6neYEIlesY2AJ8KoFT4ypSiDjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=NYlMmbZtNPVMi9fi-iAUWcve6uczhaZw1BYwkAa4gSzwL3VgRcGTCX4rqBHajqhZ8ixCuuqVEw6CI7m7JZ3e8wN3HHlnKQs07FPHmaD-A4HWcXeozdVcqWLNk-qfzFpkZIdIMuPezcNQNz1PKpZdz4b4wJVHLhHnvSr51D3atNANMhbcvOg6e5UZF4WTxlVm7RhibboSUj_e262Wp5qk-tYphbv5tgn3qFQD6szAxQNoMi6pcbusfb47yR-kl28bETtUfgzZVWFi1bkH1p6Bx60q4WYyvSgoSSEja6mTGcphozVtakZ2zRTfVMFc6neYEIlesY2AJ8KoFT4ypSiDjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXOfp94oinrIAP0vWzYCqqZsHW7voi6HuIFgXNDb_lSIBKxi44hKLZvMoJtAt18sTJQyd_r-_7xow1wSjzVJx8OX8zRPgAGUo7oCbz0SXMoj2okJUkiQRhSP-SyesfHzauFQzcJ38EUVtQBRgfSOjLA1PQGPPBu9mkQUWA_LjJjpEiwoC-4hk9Rp0ueUzZX9qe6Kxq4wqR6fzYqYjjQ2JsXFS8BpB8DAUSqaBNP-gj-t7V9_vqcPQwyv9Tnw7T1UzNA4WPgwFsHuj1q3NOT78JmWcOBbcPrmAuPGC93awTkCJx6lMPCsh_XbKZih_I-ZQDn5kmP97W9UBuocbw-FeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU49xYALl_zbqfSiOIbPx-Mc3leYBRCAYtXOElYiyaG3LO4tNE_YDNKjZinqvZd-KH2KE2qseMPW1UZIx-Rdn-GBE9Beai5OlEdfx8tvn1eWmorGkikCbFQSGfu2x8lQVLLmHlX7eJ2ONu_WqBEF2UIpmek3AlSP9BZEkTRsFbygZGx5gdrm3swljch7es5JIz3H2-HgC7_PMiQpEu4gKIV9EA-pL40r4q5x_M-TYwzXtj__dcCBI0lGmdiXn51Y90OwRS38EX_EA7bbhMOJX0SabaD9wtr167FDaQcADJur7DR9YyxYDceBJLLUNMlWc2AQOUSbqH_BY4VbitGtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUXQGVhLIcncGWXSJ5wNkPG0pNgqN6WEFzq4HOKsN9ZgKNa5PX5rKuMqbvAGf06_h9ZsgU_ckyVp2P_lZFjC13SSfVb6sy7XkoMLAQA_p-yNLBZtQqd4YXm6RU_ki6BJdz329umQ0nEK-wn9DYhUv6ULfiXMmXl7QW012DeHq06SFicg-Mrvpbg6wE5Yb4R2VdcRzBBoPyLEvaH6mRAUYgNZ9Kjkei1gqEM1AE1hNnQucviJ4i118ZyV8wf6Cuox6xc99hjwhgaXPg2kURe79ok4Sr7Tu8Htw8_fjDdGAdnEFQXYHXJByPJ_sxSHd-SH0JT9pfc5TlKvT8T7loQIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ct8zf3cSCHhuDeqAMF8qxmrE3fMcpXxhxxbpTTLv9m0_6zL_h9K07-ShENrxG7iJpO1modeLdL9vlAv6cVfj0EgblG5qzJJALFjMPxM0RSbgVc2GcbTWFZGGe9Ib1whF6t0Zi6embDrWNj3aNjcXC8l_5BrqoO7Z-sYtkgaX258Aa4Kvqdu0SrWQs15cAXb9OC0pdTYAhZei73PL0xLWpdGivnZoolZ-ps-0CmB3cj7kyhkwAVnLf3ZnZ7CiRS5nVT67UI5_xKzDrBVfdTzApSw5dYSc6eW-p6sEp1RfpjzLjE8tdYLR4qX2B12emWfZJffe5q7VtjIhpU7iPblNmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=CTtwwmq_HjAPsfexhGubY-GStRNmIdIU9jrhJTtVLQCVYwiA4Mi5mX6Rz2r7FGbma-hLjWPltlnMwG65gE_j2xKP1FiDKKnN6rb1VtuMj-jclBqdMSOMElJ2_KM4uf5Qwjp4jUKFSHOyRgtez7uIMui7YtW7b9jNuifBXUDSyrpwyiNKTLDqO1zztz1AsD07WKXW1yNMoo61-WNuv4poYIUSmMAL0WcZWEmWPqIxor9J6-CgaC8mAEOGUu-UMXCnLTFb3xW5wB2jj3BK_DjkXodIwQHhameOeyz2Z6aixaY3lUaLwETtClHmpLj2WDZrxJAQJZO2JBE03EzkAmOdJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=CTtwwmq_HjAPsfexhGubY-GStRNmIdIU9jrhJTtVLQCVYwiA4Mi5mX6Rz2r7FGbma-hLjWPltlnMwG65gE_j2xKP1FiDKKnN6rb1VtuMj-jclBqdMSOMElJ2_KM4uf5Qwjp4jUKFSHOyRgtez7uIMui7YtW7b9jNuifBXUDSyrpwyiNKTLDqO1zztz1AsD07WKXW1yNMoo61-WNuv4poYIUSmMAL0WcZWEmWPqIxor9J6-CgaC8mAEOGUu-UMXCnLTFb3xW5wB2jj3BK_DjkXodIwQHhameOeyz2Z6aixaY3lUaLwETtClHmpLj2WDZrxJAQJZO2JBE03EzkAmOdJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=iZMhowXJ7cYhBi9qpx-jVC2LYe1nwmZECCasM2wX3_jsB-OgH9yQKqvlz6DYQ1ALadNSB_Gmd_6mEPzQk4SuI9QhTNmfxQ00GvnquLTWB-ka5S_EfH7PQh5a8qpquIslHyH-UHyRG4JeFw2ReUwZOFdfY5HpeuW2YeRSpP7iDcvP6J5yLPqOsnYlbqh0Uv7WRYC2U05e9rAWB1GWLrEaPL8gZSlqtJV45MrOwnmpQad0oJM8JMkD6CltMoB3oBNeqJM98k7dO4QW9l2o3fXJPX6JGjqC60SvbueRqV4RK5mT_inR9vVmNfkAuwuAZE1_RodMui7p_sAwQYFsBm6sqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=iZMhowXJ7cYhBi9qpx-jVC2LYe1nwmZECCasM2wX3_jsB-OgH9yQKqvlz6DYQ1ALadNSB_Gmd_6mEPzQk4SuI9QhTNmfxQ00GvnquLTWB-ka5S_EfH7PQh5a8qpquIslHyH-UHyRG4JeFw2ReUwZOFdfY5HpeuW2YeRSpP7iDcvP6J5yLPqOsnYlbqh0Uv7WRYC2U05e9rAWB1GWLrEaPL8gZSlqtJV45MrOwnmpQad0oJM8JMkD6CltMoB3oBNeqJM98k7dO4QW9l2o3fXJPX6JGjqC60SvbueRqV4RK5mT_inR9vVmNfkAuwuAZE1_RodMui7p_sAwQYFsBm6sqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0yKQqSeQqHdHLLh3VlRJNv2Y9CHlonWJzsrak3oloe-rLNGyu0Ic6NEPWMtpaMZEzwllSBQjBR159JcgJqf221E6Ei6b7SSXn1KHKWaEeIxrju4bOq503UChkmeRCshOoyPxI3I40hMrtj8oIz8_poVoH9dosoJyFabANGM9w06zHxZMnhru1bM8wqd-g6UOGgyoM4-GWOy3pd_3KEN5y00f44E-z0WsWGwwRUwoXvRAy2GonquHwy0i4u6TJDQIvfvtSQpq5Inq_e4AJF0c2alp2K3rJg-vbg2DmXqxdaQty6NMk_YWl_3QwRrTcMOVFC16xxrk0KEKDCDKcxeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB1iEw_gQwnAr4hLECf0FPJEcR2Z9wcalLO9kPAPycfz1g7KJFUOujhwehaKxOzP8UGYakBzShi76mlfGHW7w-Y3NOcvN6jJbQcq2NGE-BJElCvsvg_XhEF82tTR7fa6eHy0EWliZH7JLSeVS32mj0PIzu5pi3MfHcGgSx1xYZbydZG0oA3qc22PbiatX6kwkbv8TOR5OjatG-7V38DF7BvPsYezTJsr_5GfNYDQpOdXFmbBqqFXPHvnJ6FY_7Wln2nGrLUjMeLtRKVpE5dhJgs_ijoUF--LWvzept1IACi7ei-qdOJkcdzu1RXKFvuW6LStzHtYdoX39zS0Y2LQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=VQ-1tUAeEeVzBIn6ugeVIi8vqU1GV-DDvkebhfpKM8xi2TQVv4muf0TOaQ46iOm6_JrUS2WT3NItNn0uDrJOa6jH3HX4cKe9V9fZDmfSLy534pJADXAw2qmhGnD6yd_8qc4Fz0fCR_botqP2w22qQZHhC9cLFVt9imCnMwt_ZAoOmAxHFu6ehl7QIMeT8laBSUHWjXyunYHY-X_B3U_jz0nf8XySzaJQcyVe1A-mrvCTRXcA3VOglbEqanr3qp5NDj_TNvZfUB44VZ7oZZbjf4nSYbf-zP4WLyAi4aIW1MmaIUZaNXuoyrpVP5sYKh6vxa6kwGzMJmZ7FePTCavqmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=VQ-1tUAeEeVzBIn6ugeVIi8vqU1GV-DDvkebhfpKM8xi2TQVv4muf0TOaQ46iOm6_JrUS2WT3NItNn0uDrJOa6jH3HX4cKe9V9fZDmfSLy534pJADXAw2qmhGnD6yd_8qc4Fz0fCR_botqP2w22qQZHhC9cLFVt9imCnMwt_ZAoOmAxHFu6ehl7QIMeT8laBSUHWjXyunYHY-X_B3U_jz0nf8XySzaJQcyVe1A-mrvCTRXcA3VOglbEqanr3qp5NDj_TNvZfUB44VZ7oZZbjf4nSYbf-zP4WLyAi4aIW1MmaIUZaNXuoyrpVP5sYKh6vxa6kwGzMJmZ7FePTCavqmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=mve7hkoDuHsh3JVY7fYW_5rxPv2Qm4_-3hfVcd0lGSqTsYPn6wQpgAbhkewJobGrJKPlX_ftzSIQTlylHA76UPZrkdpAfGpldjNq1bCxQYFQNtfDKb6UiUfiChLNh9sbG1Tre2ZJP7QHOR_q-xnMFHJkW93ihenIyd2r859Dly6NX2tCdFaPGDOulRCrVtGSodA6EGqbN4aEUEkzYKE2FxgwaxWI_70yKozmYh9CecgO56GnwKs31gEfVkTO6QNTbRo1iU3MCwQ87RVOMwoBXQ2nmaAAbi8H9eMUdIEMrSoE_H-TUHK-o-F7pRepBiGa8YsvHe1bu33q5x18l-7KTHuIed0S5lhiMORCsEnmqmsHRcHnDKxdZ3lz9xCn8rqCO9KhdTaCSLIOtbj5K3Rqb_c8pi94mlSnsaamqYLkf0YYsbPoALBQiqcu8wjUCgn85PY-RzOjivMSvySuPoOiWCE7zgYJ4vD0XfldlxhvLnS8mH1FciFGjv_MTN6rlcUPELGh6GfSPhedYqUC6WciwGX5k5Va9e39cVse7yn5P9tbP30-NM2RMSARu2MbOnvmLNYaQhScRJQERkEZhTwkHeQXTQJ3Yg9ocYlx5bGFosDQ8pW05NAxQ9lsCRFSFhOA5PlK3ikLiBpr_wtosepCLbhCvJNcQHZpXX4rZafpH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=mve7hkoDuHsh3JVY7fYW_5rxPv2Qm4_-3hfVcd0lGSqTsYPn6wQpgAbhkewJobGrJKPlX_ftzSIQTlylHA76UPZrkdpAfGpldjNq1bCxQYFQNtfDKb6UiUfiChLNh9sbG1Tre2ZJP7QHOR_q-xnMFHJkW93ihenIyd2r859Dly6NX2tCdFaPGDOulRCrVtGSodA6EGqbN4aEUEkzYKE2FxgwaxWI_70yKozmYh9CecgO56GnwKs31gEfVkTO6QNTbRo1iU3MCwQ87RVOMwoBXQ2nmaAAbi8H9eMUdIEMrSoE_H-TUHK-o-F7pRepBiGa8YsvHe1bu33q5x18l-7KTHuIed0S5lhiMORCsEnmqmsHRcHnDKxdZ3lz9xCn8rqCO9KhdTaCSLIOtbj5K3Rqb_c8pi94mlSnsaamqYLkf0YYsbPoALBQiqcu8wjUCgn85PY-RzOjivMSvySuPoOiWCE7zgYJ4vD0XfldlxhvLnS8mH1FciFGjv_MTN6rlcUPELGh6GfSPhedYqUC6WciwGX5k5Va9e39cVse7yn5P9tbP30-NM2RMSARu2MbOnvmLNYaQhScRJQERkEZhTwkHeQXTQJ3Yg9ocYlx5bGFosDQ8pW05NAxQ9lsCRFSFhOA5PlK3ikLiBpr_wtosepCLbhCvJNcQHZpXX4rZafpH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4VP22R3rEpE2qWpE5_ogJre7oKmiEyfzd6cKxn5rOP8oWZ1i7ZB14AchmtiTTEoDhw2V04S8Z1qrWpxlf5yxaMDNnQmQCeJIaAPUsrrgPZUeh9BIiR1jJ18ugXwcHB-M0Z_hmJUyTD5VHH02-53Jx1o_zBAnAhI_6DjoLJQpPe5umpbcZcWxZWSIJaPuSDpEaCLJIGzNLqwzEBrNMVywshnuw1l7l7nkwVLS5wK4uCOLOA-SsN2P6iiVfJ7xV4_7hA2-h4RVxOzQ0vX3hfSIofU970ynppxktbzhqaYHi1o5DWm8kRSieu8-SFR7I2_nWJx5zBb9vSA5-1X7-6Qxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uG8cL5r77BBezvtvvEWZZGiki_qpUUxhNJnQfP-WKwz-okFuSBaRBg2mBHIVTNLieOokZwMegdjDUmonTV9I7fgxbXkCQR-8Qw3GAD8tUtzjXhbwQsrStTkfjGNujrCe6aJ0jK2IJRRuh2QgZ4nypkHz7NSYVtfcVyqsRhd9dEv6t2bs2B7iENkUa3eLY46avanal69Tcyj5STGkQ5vzZEdJeBpxdHXH0tNj5msjjBuxJ49YfvWTKNz5MrZHpPk80HPq8cszFWWED1GwUZVU7Upm7zTUjVYpHNOuJY-qJP_NpVe12TIaCO1wQ_brcT-zqcCIyvajQqsmEWKtsdQ6dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngB6hf2V1DXR1Dh8zLTEO77029jmz4Xfx5p9Q-zPcB-VjmRc-ubMkz35ftWXDSjNlvL7Y1U9L28dvZiqN8JkHm8ypJaYphAHNQqfUXAjRjDw395EgSnoySt2I0002VVjihDQZ3x9al-hMN6L3JqKwDWJSKc7ts13W7diWc84WMOr-wmBx6jmD3tbOa__GLyZwPCQS4uO6mCxufXtnQHJYDSvkQnuTibFrv5SgWY-I-e1IzZc3WWHVZQjn0XCaUWxvOASBFG9Md8Pl1hfZmkuThjZEz3zMIY0Fsloz2JZjBT-3ZPkw8cUkaRRkYo78-K9T5IYL-m4-9J4h698HWv9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX0tSFWIRAXrti5v1YHwa-kPxnU2Hnhpjlw8P8MPCdSvYASXfyhQd5jaFAbuQGAuotoHytfD5CYk0dgy5xqkrQ42HuRRgnRxuCH7-194xpyxXiYvAb3mjD4T_lPJ0-YP5DviVV-z1dYuSEOk-C8nNEMTB10IiXZ7cCE-e0ZNIqdJhHjq018twNHlShL_jN1APajfiybKuAYn-mcaVQMEB2HSgXeq9W1x3vENzhdhdr0XRUyTQcXDi8M3grjVgfPTUpLmPIx4qah3-lBTeV4iW9_N-8_rmuqeow_RUOP_mJFP7-0VTwnauGbbZKHFgBlG-0lHfRzF4cPZJJDLRLYkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGTbSuN9ciB6euM9c36l8xYTRj2pv04vWaUnqbixtzonBgbxYpq2aa4d_G5oHBPTktz3rh-s7e_UwEWCnMyLxTsQ1oqdT_IXM-33kihKzFf7A7Gn5CTeQJayWRNtf9LVesiVg385z4FlXUlIPH7x0sGBd2jW8oCBJ8uomUQ98xKXjr9nQn0misuqkmdCiRINncYLxH8OkGgadivv1FH-IR46f4n0F533W--uSF7TlccDOJyBJ8yz-YCPJ0Uver5tCcgHZ-T4gNPunPnEZSeEvDh_6KTmvEBQa5MROzFSwvyedIUtEdY-WZqkQX2BNw6uLvfBnWJyqNMQIcOUaYkq6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-LB0HMHvvOnAmq4ZWU2xOnMAxH7QzgMXzvW72SzqbW7EWgF_AcT_DEj3_WwZVpMVqGMvo6QwEG9hxiBtcROKnsg_jsr8gGT-y6Tge8Y4qJ3SUUMT9MCw-yv2SvLFSL-BEnWc-qQvLfA_cIwhhgXRbDXZQ7KNM39MYonDYT1WJJr-4uyNjc1koFagADHSjBsNKqK7qqYK1tXzCAeVabs2YhIVw28l8ugbtMiZ5oGS3yohZedIojM_GtGKJgjwYcZlBOy79GPsUpFzGMO34vxii_rSItWhePO0Hyia3mSAmZrajYZy1hv0DOq0YiTQPIB8cVpIV0KPv2lsN3wY7WDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=Atd-HJ3eTHTDUhEaFCcyYvbvymTAzZe0hjQUQBlx_0ZBVXqF_1MGbQtYUu1acCm3wtTg8Q52ljhg8TtNtLrNDil9ymNTlfa9jKEQOKtqlghK7E1lSxFagTt0XTdAU1pj8hyRF1b1AgKGzVsPkXJ1mw1HSOAFzyFWUfYFMCGt06bIKxzcx6P6dcQ6HcbWR9QsSO3_-nvxmxzprTlxhr2N2l2nKBK1tyXuNM3UdO-XmQV4B38Y_B84ciKQJ5XZD7UQGaa8thWLE_7UkdTdl_lMilp7zuuFvSKc-0HsmfZ5jI7VH5TUBv7kgkO8jgkUWW4h45ibmXFJ1CcZhwFwx5UwDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=Atd-HJ3eTHTDUhEaFCcyYvbvymTAzZe0hjQUQBlx_0ZBVXqF_1MGbQtYUu1acCm3wtTg8Q52ljhg8TtNtLrNDil9ymNTlfa9jKEQOKtqlghK7E1lSxFagTt0XTdAU1pj8hyRF1b1AgKGzVsPkXJ1mw1HSOAFzyFWUfYFMCGt06bIKxzcx6P6dcQ6HcbWR9QsSO3_-nvxmxzprTlxhr2N2l2nKBK1tyXuNM3UdO-XmQV4B38Y_B84ciKQJ5XZD7UQGaa8thWLE_7UkdTdl_lMilp7zuuFvSKc-0HsmfZ5jI7VH5TUBv7kgkO8jgkUWW4h45ibmXFJ1CcZhwFwx5UwDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=hYHifSZ7sm4LQJk3hjpGTfPT3L989FXAkC839hOSR69nm9Gxca3mT14abNtMR1eOMIsbC4ryI_0V0TqN7gdgmdlPJTA_3rVXJYCOS6b8mciPZtpbc1lIhIkC34SUhI8MlH8UubJRMHY3WRto3fSHnYlNYrB3wsodsxOq6uY75v_BmYqSdqQ4SbZAGWl7-huZC6vYwdf-glQ9GaoULo2zAMOTKJIulxAj61Xjoqm2Z26poXSjaMNMSGTEVcq2ghdwk6QeVRr8T_mOY39ivGtHflD4R_ynU66ZEDZptTdQuHhQWEo39KTJd46UHGj9WViIqkNtwPiaUhKVFgHCKRnYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=hYHifSZ7sm4LQJk3hjpGTfPT3L989FXAkC839hOSR69nm9Gxca3mT14abNtMR1eOMIsbC4ryI_0V0TqN7gdgmdlPJTA_3rVXJYCOS6b8mciPZtpbc1lIhIkC34SUhI8MlH8UubJRMHY3WRto3fSHnYlNYrB3wsodsxOq6uY75v_BmYqSdqQ4SbZAGWl7-huZC6vYwdf-glQ9GaoULo2zAMOTKJIulxAj61Xjoqm2Z26poXSjaMNMSGTEVcq2ghdwk6QeVRr8T_mOY39ivGtHflD4R_ynU66ZEDZptTdQuHhQWEo39KTJd46UHGj9WViIqkNtwPiaUhKVFgHCKRnYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cqmj5Lr8RHncIfcDuEaTNA21dDx7HdQP9A4rtnhjx1dQ0Nsd3K0wDAF5xUGAq9eRMgd1SO1D6Nu70Ej5hPV2KrVlkN_iP4_xDAx0mp1A4oe5vhEub7DccwpHlFbY0oirkBEUHHbA4gL--EHxoburMGc8i9p_JmxBVKZTsNTM7jA4VfgXouJdC4l7dHvpTj_FIqZMfwMOezu-p3plq0Wra2sS7KahW2uakzRBuDBDI4u_5mnfL9lmrRiq6TGE7Ql639YbImopaYygCm5_2PZISPMDHippUMT-BSXynkK734elDJ6lBnprmYNROAiP278_-0lP6RbNz5A4wm5JgV-LfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRnS1HodChuRphTcaHGnRzMCsePVbght9KzU46Q6buv8DEV7p05G93j6e-oFxPGoQET9WpMIuUs_f6IkAx64iTMRwTQysQMsFHMgAr1Tu98EYhGj1nb4zRVPLOuIrDn5MUG-obq8VeBRD_UxYn4rCgt85Hacwpl7ZjcFIE5xIFkzksFWOkhvsWwVGnu0ba8_PfakQu-EZRLb3fH1OTy1fBJyl8NqpGaZFsGnSk2wTtTlnYfLwheOla-G_d8jggnv8F_yQGInF3_OhRGIX1ca14gEoI7PlEeyEycvCWC9TDPgaVf3B1pzK2GBu8rd-HMfZFRfZkvygxl01C-L3Lj6tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=jRFq3KGPi_MsAaMYIkKwjGowvgbGvkU3WlSGtUZ8yMuS8TzIo9vapTGbZ03clLhOLo_bJhhl-761VG_WxqyiWEi5Ehh4m-eB7o5uYlKYk45CJAsAKmNxlb7L9HnPcKhOTPQ7wRKcZoh84-HGG9WHrnSjB6KxDe1puV8E2c_WFp_QHRgn56e0mE6Bu0ntVNvY0iH19l02AyMz6LYDdiGY89-TzeleTDcFxQu-H9nrnAkJoXhbJFmM-YAXbOmufFi_K3Ip3LPrCNZlWT1nEhglWBB6T0Tdv7Uala8ijW3eLsS4hXQcXz6joHuDFXJW_UKQcCIIhzkKgS2_379hpzPTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=jRFq3KGPi_MsAaMYIkKwjGowvgbGvkU3WlSGtUZ8yMuS8TzIo9vapTGbZ03clLhOLo_bJhhl-761VG_WxqyiWEi5Ehh4m-eB7o5uYlKYk45CJAsAKmNxlb7L9HnPcKhOTPQ7wRKcZoh84-HGG9WHrnSjB6KxDe1puV8E2c_WFp_QHRgn56e0mE6Bu0ntVNvY0iH19l02AyMz6LYDdiGY89-TzeleTDcFxQu-H9nrnAkJoXhbJFmM-YAXbOmufFi_K3Ip3LPrCNZlWT1nEhglWBB6T0Tdv7Uala8ijW3eLsS4hXQcXz6joHuDFXJW_UKQcCIIhzkKgS2_379hpzPTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtfKMXHd0IJgyr-JQrZyK0AeqgfVMKSMEvV5Xcv0vZMyvNW8I_6b0alN0khAyrE2zmEr4Ka-9y9_gwgG6RfBVOGObyQkiu9bpIThmYbvO4p2EKjv-MLCXPt7_IKycJsBB2_-XCPCB5ueGbEU-hOEb0urue6BALtSKoUXWLouvIfjaOxFaNn93R7AWIAgdk1QpFNytNJtrG_ONF_6Ue8Joq4j3jRgvXX7A7jr8FL4ro_QyR97RrguX3sDhnq34DbN4VeDBA73Nf-4KvIWhG2wb9CGMxSOvG2Ao_UDN6fSjJgInHMGRQCDqFKyOaqiCGRY0kwxkWHahdAWXEIh8XeTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw3y6zYtyLcV04c1wVNAOhcg2ErFSBI1u99PoBzaYEPgseA79ZQYVTm1JZsj_AzWbFU-RoRhW_kyVfJElX3SAWpePyX8OkvU3BQFA0nfNiSKduz--tW6-G_Vx_e3kgCk6KenR81Jk0kOmwtI27f_yA6iEbkLGPllODqfBh1dgez-QYlssHeKTOo1_1LSBA1GDfdM0Pl4BB_4PqOvNvpRtFzeh2oJhiMgmNK9IfaFAHVBltUvfkUePxbyOjPukGe4tInK9kYevC2Z8FHLw0bGgXCU5CBX_umKdUL8_RrmvJyW1BN_WBB-jwjpFomRyjuM-mLCWIlHSX5bEKmifTKgXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=BKa2gY3pukh-X443Nr_WCnu5p363GoGP7bMJXmXyFc4925zO3kvo6hQC0TBkml0DHryaj9Bl2eUyILZQBnF1VTPSTpMx5clNNAn0QlWgEONkY20vwaw6AkKbHoZwsAZgGmFagoKO_vPqe3FM4dOd_g1Gd2RcjOWwNmXJOl9dW0wt4RsIxR5LDLfRwtS186EYJe4EeIbdcZxzHptXvVKREJL6k-zk893hmkfuwAYw7sQIR43HWOrnptEqgwH6swo_m39jmppvQkaRnRL8syN6RJcK44jL0zSc5GAhGnoo1jDfnMJp8QMO61D9Qr53QyS5M1BZ5oP3KXbQC4XrNb1YkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=BKa2gY3pukh-X443Nr_WCnu5p363GoGP7bMJXmXyFc4925zO3kvo6hQC0TBkml0DHryaj9Bl2eUyILZQBnF1VTPSTpMx5clNNAn0QlWgEONkY20vwaw6AkKbHoZwsAZgGmFagoKO_vPqe3FM4dOd_g1Gd2RcjOWwNmXJOl9dW0wt4RsIxR5LDLfRwtS186EYJe4EeIbdcZxzHptXvVKREJL6k-zk893hmkfuwAYw7sQIR43HWOrnptEqgwH6swo_m39jmppvQkaRnRL8syN6RJcK44jL0zSc5GAhGnoo1jDfnMJp8QMO61D9Qr53QyS5M1BZ5oP3KXbQC4XrNb1YkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1upFll4qUgkWOtN35HTWYQtNBiNUn3Ea8zBQ8-5gZW6SrzQ77-G_BWcLNVuUun6HgI4vFywbAsNUw281prQPJU4MpX8frhRbWnBjRDRoy-ENJfH0r70WClpFIQah1CZmc0jk8haQf6nN5SDLL5K-XjJoDTki2DJP31iCCmZyI1YO8aKKyQ2OgYQn0k2t_EjHpz0FnHHnYE1BaZFJP8exBowIQv5h2qXtpcR1Uv2NOPdFBl3dn3CCvVOWiWGL27SM5ty9xtJuufYNdNa0WcjPkLanoDg1HCHw-Icio7_nIwwEqVzLEWpKXN3w-oXK0tUrq4rqaEo2YyPHmUtPxr3CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRfxzb1PHtAsX99xP6WTz4bm0JdY3kaZ2QtT3dzu0IsByYccXjQYPKbQiSOR6L9beX7UqSAfXcEuPJXc3-gv2ZjFCdk4E-a2cIcqBGaluLX2F5FQOPWEg0WT6KERFXqXDsr3bTEy5_SAq9oUT1keV7JReTg0bWw4o8zbyimMZjDZOBq1KS7hPIffbg130QirVJRZzsm6He1phgWmwp44gy5mau-rpFGNcevugBGorvimlO5yjQSh8Fri_pSMk7QTBfF21aJQrK54DP4hI1jYV6a7aIZPsKi8M5uwdOl0aJSVutp5fDc0-IyZjJ6N9Bug_w-eMDK36h-d4HQvMR5iHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=djWjTdet-fEG3w9htiZExrsImTRmJ5D5qRJ59UQYHXddgRpMCpHevj1bU8tiCme2vRvectmNPb-9yvUfyc-rBT284bUgIVI6R2XVktxqzeloSuplaUZZDEYt2brASXp7GNY_SZwCf8vrsUgfcNnWlzXhblOnnVNvvjUHJakO8hctsPkOJRn3uey9qqr8Ijbpia1U9oLdz5uG3ooK51ZbGWQyePm-36tCMv0BFvjdTbuS70R0fLIMOPRzwMoJsv4xLcRs-CqISmg7LuXW6657-OEVhkBl1Hx2fwiZWX3eXUU3iOKfU7gY4FpC51py7Z0_bizitRQCtTc5xGXjP8Kccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=djWjTdet-fEG3w9htiZExrsImTRmJ5D5qRJ59UQYHXddgRpMCpHevj1bU8tiCme2vRvectmNPb-9yvUfyc-rBT284bUgIVI6R2XVktxqzeloSuplaUZZDEYt2brASXp7GNY_SZwCf8vrsUgfcNnWlzXhblOnnVNvvjUHJakO8hctsPkOJRn3uey9qqr8Ijbpia1U9oLdz5uG3ooK51ZbGWQyePm-36tCMv0BFvjdTbuS70R0fLIMOPRzwMoJsv4xLcRs-CqISmg7LuXW6657-OEVhkBl1Hx2fwiZWX3eXUU3iOKfU7gY4FpC51py7Z0_bizitRQCtTc5xGXjP8Kccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwOHmUVotjhCd5R2NoFoaBnLYZWPPPPPGGTk_EiaK-_AlMpOA0EhPgmv4T9SJFaLBGV_xuU6BRZsDJGkMM3ULPV_-HWEKax92JZ5JpBdrVT3Z9cQnahntKHKQN6IP6KG4pp0ZnKRW-H_hg7CyRQuICv0e6bZa32O_Kyn3K0gMFJHpU8Y7XOxJWi5ZHFqanPcgo1YH_1IePhnwt5YuwQ7V1DA31P2bmf_h-gs10YJrK_I_MqnWMb-gxZJq3sbM-tFURCx_88k9yf_JvrTk9FnW0V81fdKHQ6QtUU7dr7QhYpWinL9xfztOiTdjiBBK7tjh3WoWStlKQYiOXr2DMgY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQdxzhPfBAbpxSn3VUraQmFX8aEOsLQVsIREaE-fYyVbKtruysN3bSNeItDfrPDrUlr3nsmmlrHOlH_eVBG8cU0ttRgjKw1_Fw2Qg4zp6_q1unMjwcnh9x6ck0OI9mw5_lS21HwfpTzt02Ky4y-ri_vdjASztHQr5zbYGkvXNFLiJ0We4Pd30Y5a7F30R9bzfje4_f0ZGooqsq5KcfWwPPDZPzjx67eJJfFhc7zhSAkhpIV--Spngtfhp4-qXPSDCfm4VblAyI0XTg4swOq674nl7QLZ7R_gDDwEImwA4LdURiFscsLEr6ugeFdsZGCmghqanhYV10pu_24X1-l64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6E6s-gJgfAyddAYhopBWkTCRvtzHEwXnT1-MaGpuqf3IS_JKOQxSj1hCWgXfcYnTkLhUfUXklyRSZM2MtworkexFudJaGCq42dS_5KSdBkhgRFsVnxER3c_q8mh5UBwcsJMomgrhrj9cIainqz2z092MPJmCIRA7Je7wW7Ge_4ch0ChqrykMsv5qXliQHaPFL1rJg5uHDKKL2ekHX94Brh5ZDFCQbI0eaeQ9aU45ntlMATIAVjYBHYBw9swc-oL4Yi-Id3BP1diyJ8EggjeaDUdmiwDSkegXELkJ4cwZNTadkcyIj97rzk313QyK5oky1cW_2rZRhcfo6-HZ-WT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7q0gLUifjEPh8xsG-UhIdm07ppNSh2lbkbB6AzpQFi11HzU3NC9Z_86IRecS1FGPx_Ie8_FtSBmGeanB8Ch2vPximwwUM0A1RhRDUs_XHMDFehXpOSszfgSk0F68jjseX1Fp-F0lPLXT3GPHqx7Y2FDEfnvlQwEwGiRVVwfezMmmEha6o-MsMMaxjtuPFhmp3Yl_SSIxAs88bWuq1duw4FZxZa9XUioip4d_fQrGzqI6_TCORCBE8-Ws9tgYmhGOEysYKGCZs3Z3ZCqoee4HXOgIdxK-mXQfVqKeSVwDuBF07l7y-tamYsUMStv48ifJ215x3FRnpZH7lyO9MSSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3-RrZWYqIMOArbAP_htHi2uH-NVqnHjZbc_1CgWPk15CAYnRoVrd3jAWMlUAA07K10qe4lLlZ3vrDzy2LlvWTbgaesfZ4js42fiDgE6WD-EykJoJOysU6gp71fNEbvkpsX945RvihnWZWF8C_koIdG5WrfiNVoec__z4j-aALxiJYJSZWbLGTQu4sjg-l5B3-piLX-9mcbNKi13ax7q8a1LclB69POSCj1tSHmWKCgLd_o4LJDThnupXTDkTDsfP6xeahdDH6JpeQr-LPwn9g_O4BAGxR906Uj3p0yCfYs8QF0HqQjCFjYRbtqHmCgCOebK2tMsWJ2_WIffH5ZdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuvyuJK-Koe9OE0YgtpAwD29deACYrIuwv_YvYwPTc32OTpTwcHx2a1vxamXir00UpJSZHwx-O0Ku1Vkudp1VsX2_I2gGoX2dKltOStwqnQNgiZgt0msgQ-h8bVBwkYJs85q799o1BuMFHGvgahFQKMJ9IpJP1p7DfLoXNDzjZzYNe7lTuX-e9criUuNxkmlOO6XKF7WkjSfHY36AbCL6RzEgvGAnZJEc_ydGYk1-tmJVpCDJ15xkQq3dS-cqW-h7mxuWPztKy-xU0v3uQSe8xuoNXzDi2qsBrGulDZt-HQLcO3qu3u8eqeNwDVfLRWVplp5-PzywvwUlozifB68aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=dhM157YldxCh2xJqpH27TPtT8baqISmh_CZGZfQTy7rOw_OF7losZDhogUpRmjZz-CLRD_dGLr38kGAjf8Jd2nfo3Q-HdGtZ6y4McnoEqJRl-GiyDFvRf9sPd4UmK3uCu1JQhT7EI0hT9Pv2ebeagAElSeo74MRlKL02XAwNgs0mqDKnIa6OUPravrI3wxkP4WI-Dlb_GNIoVCxZWhgMvJsJs_bXELOABPc55hHf9dTT5YguvCCkcspgHJy2cfTc8Q6stpQxwe1f8pWv3ZkDA14NWHO2QusfDFSlhiIPKoyJ9gYxB78FhqKYyY1gr4socr8fASyBUAEm_b4K6t1KQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=dhM157YldxCh2xJqpH27TPtT8baqISmh_CZGZfQTy7rOw_OF7losZDhogUpRmjZz-CLRD_dGLr38kGAjf8Jd2nfo3Q-HdGtZ6y4McnoEqJRl-GiyDFvRf9sPd4UmK3uCu1JQhT7EI0hT9Pv2ebeagAElSeo74MRlKL02XAwNgs0mqDKnIa6OUPravrI3wxkP4WI-Dlb_GNIoVCxZWhgMvJsJs_bXELOABPc55hHf9dTT5YguvCCkcspgHJy2cfTc8Q6stpQxwe1f8pWv3ZkDA14NWHO2QusfDFSlhiIPKoyJ9gYxB78FhqKYyY1gr4socr8fASyBUAEm_b4K6t1KQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkLU7Daicxt8dwHpmT2zIG5jt0WwdRqQbYPUyO3Bz4VxI_QbZjjo4MtIyLPMxnf51JWudao1DYwx7wSYs9wVZcs5SPYqo-j6Nhdrd19Q2aoOF4RqcpbdYTml3AasTaX2HCXa5UYXhjKIB7euuiin_GLk4vFRe5uwfIDmneWCaLrdJbSIfVe0_YZFtw1ISH0OtHzfY04MVP7zL4Yxc-rP6oUcT0Dps24znQmKW2qo7PM0L1ex_2mjKksywXaxjkgzVsJew68l-amoDZ7C2IBJqsUY7u0M6sthWHKDP05dfUusj9L6zXXKR1xD238qnbg3b29q7vStzeu4tA99pYUAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTOcX8YRJknTzzpjOt8INUiUDjkVi2mSCGYexqWuhte_fvlNEvvxBS93eWhpHIrMHG_MMOie2jayWyt7Rrp1_GYDey3OqlGOPE4aprpB7lrKmat64ELEB-_gi39Z0lfL5AavDwYuA-ezoTyDPaFZLjECOmSq8SdQq869jFKcrVbeMoDdyDRZLPDYyUMSvXoSIwu4Cg36y6XFVBMbGMaRXuXIdi57ZcIeUZzJhw03maFRS4bYl-_zLkxneBJdwdtEHOSZ5lp-_D06F1T_ePCMHeAC1oHppXzw4UIrZuLIjrwKMJz3NjTQeB8oBDlhScF7-x7AZx4i_9E2LprErwgwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=LPFTfgkytfO593PQlyn8oDHQFkSzZ9Rb5K24g1Skwomsh-J2b7H4Jwoe22VqoI9m7iJ6Q1PjTKm86Ls7SssPGJVM55d0tguplBi3ibe24JDkelnfdPS9Qq8zrCCDBvGvZg0JU4bto5P_Tr2syNIElujAW_RbqCgrH-oX4pNFTuIS1fWUh9W9t9S26e1Tl4xf06lnm1gUUSMDTYiHqiAkJADS5xkDZUMBdj8r739Osg5s3vdgNjV2wwf-uqa_K1CpoiFJPlMxI80xHyLr0IKl-rLGgA5zYLYDPMFWr57-kaKdAajQ8Ht3uly1LREdir_b4CnJmKS0C44229Ct1IlrsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=LPFTfgkytfO593PQlyn8oDHQFkSzZ9Rb5K24g1Skwomsh-J2b7H4Jwoe22VqoI9m7iJ6Q1PjTKm86Ls7SssPGJVM55d0tguplBi3ibe24JDkelnfdPS9Qq8zrCCDBvGvZg0JU4bto5P_Tr2syNIElujAW_RbqCgrH-oX4pNFTuIS1fWUh9W9t9S26e1Tl4xf06lnm1gUUSMDTYiHqiAkJADS5xkDZUMBdj8r739Osg5s3vdgNjV2wwf-uqa_K1CpoiFJPlMxI80xHyLr0IKl-rLGgA5zYLYDPMFWr57-kaKdAajQ8Ht3uly1LREdir_b4CnJmKS0C44229Ct1IlrsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzrf13WP8ocAZAOQ0X0EmQvUMhihlpl1JuJlRqsRwzKeD2iycQUIk0MjclIZdBkHhvdDpKRS98hoUcrQSrkP-wMipiye4bsshpD1aHa6bmVCEmpwygiLXas5JQOZScB0HxHLMmBHlFJ-2HChUIVsz40aN9yjGEAa1KMXob1iYkU5bv4TCwhOwqwO0VdFSo9HITajE1d24ZxQ1Dma20hgRz5gMLXO2FFb32yfW7qMGCx6szjBbgKXkd9zK5o1tM2rFA-VlykzbCMKIb_om3eoIPmm32t0293NjKeGuoivkz-PY_JHt3rZ1n8Pyy6e5GrwZtk4I1LexRJ15bTv8VUCyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma2UOFA7Fh0vmMv0HDql6OFuFowDCNY9Wc2WD9iKqaBzH_vVrtOKmPu28NBb8QlHcrcSOeuDsu5fWXGCW_Ib6QyaR4qMXFdKX4srbf7OOcw3yZ90HKSD95IUhDt4qJ2kSH7jk9bQlObbVEElrgfKmV2brtxgK3mIwzW2cIUBaHi7-YeiqO-tjbdu60M4upEzQ4dX2RAJM1yyn8FNwklj7uRjKeLW28IL30QdX7cjBxjeGQCrfTyyWZqpNMyOrE9F-Dx8K0DLNzJmlkibXtYb3WXMQmbnsWbK25b5IQ5wvNyy3poUyKcXhVWRlSgDheayBRqx94kzuNWsn3LrlRwGGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/moZLLyQdqYNgeKnT5NL0ic1P0rqVk3t25cITcvC_cFnOgR0azsFngcA37ikdCigRUE3iwcF32l1kr6EXPtlcNxRLb9SmOuk3ho369hzM_Wl1y_syyAV_UniQzMKfs9UT1as7lkBNf_IZVg9wsrC6TUNbxJscwdEFrqWOhfalzCT6d6ePpyl46Xk9Y9ZSvF0LVd1W3o8AvRy4OVNH4DUffDDZnM6Rcb4o3DI-OHVc5ceFgGecii_QJ7DpeXi_zEJTUn54Q4D-CkkddtvAPLeew14ZuplpQIIa84hUPPhZsWB1AwpU067_r1qhVhPx-R3zvKlTEtadzBBmnbsQK9L88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kvn5eEuK8K8K639BcIvtAW4G05lBW6IrTp2LKwd7bl2W1WBnWk6JfPa46xtA-AaAxBv1Nw5g8EjeM9JLEq6WP77L1Vjw012sxANepm2V90mNEHH6kQeY_xUk9fjfKlTT-_iiaYizhc_ocEEzDA7f-imZ1T7h4Q06d2Q02DMtbfTzIFSsKyY6uwPM83ikJzGfVR-YhIM01Zn6U9UBSGYM3bg_55aEAkEafcG3JWWWz5skdreNER2yb1m8rOCLqxM6FeZDSdYiBtrLHdg8j7RWMPE-vzKdpIXspZH5C_XgYXDjRUNpppcF0LEDX75VDtsiPbPn-zZLX2Wb2VPh-izjoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnXdPnbUd-kHlUxJbkwwQRr0OuSxvS51SP5WWOijbDndIfAdVTcM7LhOXc-ZL0s4vISAwKi8VMjstkcUpXJ7lz9SUUM5w0QILeDr0kuXNf6X8vzHktXSFbsnEtrQahZjsoUbGlBXFG06ChusePbFB9_U87GYNMec8FRb4r5ljJI1GiZchk9ApeVKjf2C-PB0R5HoU0VZgD2afVgkFt0WwsMDKwWIH95fQK99rCs1FAW1PyHkHgfZZrnEKae6urdFxlih2AQ5ddwft7pi3HziDXSXJXXtor3uDkR2rlsza44AeYw23SANdStIOz0cm3xC3Q0yZhj_dzjXbQ2FeUG2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=VbzCLN84zWfVn49RSz__Y4eD12AxZm_4y32DSvV1soB8YeVsAHt3eBDiL1ewEVvvmzucxpfp6tdw7Ib4gLLQZBwEfw8WRQQnYrwgQX7aDFVCNEcmKT6aO8ve8IcZ7jMpCwX6lLuFa0T8nwVY2jw_2iYsG9nkm15FP33dFnr0rOfwtVNN2iMeBfZzxPTXytBI6HBh-TOsNpLJEYoW3kzYf0rt17SK4ftuDnw8JLr9OeOKNaCuO9CQsq4DTo40nJWoYGyZHSb9RV3Wq15oAUA0IgcflOOl-EZZ7JMzAyrZQA-DMFnq59kPozohp6mDChOPPyULXDEnHaKyvyANa2H3Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=VbzCLN84zWfVn49RSz__Y4eD12AxZm_4y32DSvV1soB8YeVsAHt3eBDiL1ewEVvvmzucxpfp6tdw7Ib4gLLQZBwEfw8WRQQnYrwgQX7aDFVCNEcmKT6aO8ve8IcZ7jMpCwX6lLuFa0T8nwVY2jw_2iYsG9nkm15FP33dFnr0rOfwtVNN2iMeBfZzxPTXytBI6HBh-TOsNpLJEYoW3kzYf0rt17SK4ftuDnw8JLr9OeOKNaCuO9CQsq4DTo40nJWoYGyZHSb9RV3Wq15oAUA0IgcflOOl-EZZ7JMzAyrZQA-DMFnq59kPozohp6mDChOPPyULXDEnHaKyvyANa2H3Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWtcXrUSFMIEtz0Ge1VP1warYImt1QV1VQwvS-vlV7Ts3cRRDGqGJ7piujbPoZ86ZWU9fg3aZz0sm8GuRa9sc0h6fjsi6u2Z13K7AQGpDlO_PIz1zVAsiBWpg8IhJzaS2sWzhzhZJ5r-q-ak-ObgywQSh770lbeCpL0FrLh-zvONLQwRyW4dGX13XTE5pzt40F0PBkeZQS_TowLpsZ7nt5CB46Mn2pmzdTnEnQSUHLbP_AKq4dKUxlBwgFIku6N8glUHONU7b9X_kXIU8LY9IL5lGDuCQ7S9yEB1nGA7APpAnuuWdHAd4MnPG58u4Mht-b6d_UvrGa_rNX0EJvbVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coZWqX1WAmymVIywZNVtFia0EDa0sKYNgV6k9z-P1WG1JCqTKYeZdDC1M1gVK1-nBJHkI8d7YY33ZbJLaf7IP1G4Kt-HF-8hcpNPHl5Ap1ODO_tXUObjp4i_Kof5tgt7oGDpbBa37gIwKi4UQTd1rkl41xayuLWuN6rOH50jzGXOgZTd8n_AkmPNwxGw22Ovlw1VRjwcKC2ivdFNmdrZQ73j2ebt7DvGAYoxdh2H1tccdP_qXm5nV6ZDLTFaLdIG1iCId1BXIjyNeJXEDpB61og2lBtZqKERn66lfVUOeNiyzWVqL_YeqPVdLHDONZAa9FPQDdy5wfIcnRXbSNVWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=VdyZW2ZwIpDdW42vtxXh4impkY7QvFTZUecXwsY2U4zLzJZk2xglffYKycZH6nC9bTv4m9Z4Kzcb7m0-WmLALadyBkpNM795yYd26gVn3Ba5AHFLpcUupO2RwlqU_W_yR6kKgoRjOiG_cO9BevHCdw0mft8SugPn6aYeclcLiabukbwdykAhTt0bsLzVG1Qt-mzyCoJXF35S5JpP_wQDiIXxLIMSBWANjEoGDDAXt8TKWfB-k8KnEzK-9o85O-q3poI7DFzC1n7jWQUi_c8EVNFMYHzYCssCrZj8oy6tdHh3kSlGu0XgMjDYzpxD4RbHjLI-h9DQyXdzswzbIBV0aU253zdMd1zOuLMUtOjoBzFbOI7PYWJLXpuPQSGLhC1Q47imnLtnUAIPEMNZ3Wj6EiCLa83qw7tuYyT7pUkOeotpV_g2_B-RE7GXpMyRB8uUD231nmrB383xg6R_Z7h-3VaTlx36kQHbqJz6xH_5bwk6uc_FtB8wh8Mb38brm8smB2gkf9nb8rDmmT6FnnDBxamELWS2xni2-aOSziiHmARImOT-y0rqyOFfu4yJsmxSXzLFQLQGnLuGscLIZbySJqkPKl_zjsfLPb1bTFfXzpJxVBYfBm9pwojHSGkY76UPl93-GnJhtzHJ03afAoN8Hl7Ze7g72WLkP7LVEGu3JWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=VdyZW2ZwIpDdW42vtxXh4impkY7QvFTZUecXwsY2U4zLzJZk2xglffYKycZH6nC9bTv4m9Z4Kzcb7m0-WmLALadyBkpNM795yYd26gVn3Ba5AHFLpcUupO2RwlqU_W_yR6kKgoRjOiG_cO9BevHCdw0mft8SugPn6aYeclcLiabukbwdykAhTt0bsLzVG1Qt-mzyCoJXF35S5JpP_wQDiIXxLIMSBWANjEoGDDAXt8TKWfB-k8KnEzK-9o85O-q3poI7DFzC1n7jWQUi_c8EVNFMYHzYCssCrZj8oy6tdHh3kSlGu0XgMjDYzpxD4RbHjLI-h9DQyXdzswzbIBV0aU253zdMd1zOuLMUtOjoBzFbOI7PYWJLXpuPQSGLhC1Q47imnLtnUAIPEMNZ3Wj6EiCLa83qw7tuYyT7pUkOeotpV_g2_B-RE7GXpMyRB8uUD231nmrB383xg6R_Z7h-3VaTlx36kQHbqJz6xH_5bwk6uc_FtB8wh8Mb38brm8smB2gkf9nb8rDmmT6FnnDBxamELWS2xni2-aOSziiHmARImOT-y0rqyOFfu4yJsmxSXzLFQLQGnLuGscLIZbySJqkPKl_zjsfLPb1bTFfXzpJxVBYfBm9pwojHSGkY76UPl93-GnJhtzHJ03afAoN8Hl7Ze7g72WLkP7LVEGu3JWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQcFMOdSnJ_sk6OTG0ZwDmcSNgKMgEWEjtnB9EdzIE9nTKDuyagZ-1n71xrQrFHmVYVHAjiKFCwMBTizvMpjVKtBiLLz6YVidMl2SILC-2EKhVSTqeyaT9uOiAV7ismQOBTwEqwqKMBMjo8f6OGPM70tWNfK_7G7Zd5P5SDsOdFfdqb8PJx0uRXqQIwvMkLxS3excgLRu8nJwBTnHEQ578ldjRelmX7Y5JYKacuPAwzTWOmNXYp4q5JJsbkY3MkGgQ6KJ85GD8n3wIwdkhHQ5kPWytBufZFF_ORZX2h4erht5pIaDVXz2goQFmQwDqGD8TzqWn933CRckIbhhMWvrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBA8-_rUYLQKfCtv-Y51pRN5e-uPTm34o3TdtfLwOpNhV2JGhJrzLbh5OCl3FCBORwW0Bvc4MvKNRN6gUsRpxDNudDPI9cUNT5elmKN0fTiZoOhRDirA57n27IBRhbiKif3ppv9uoBK4Edm08GE-mNBsJbJ-ZZHH7y-GOMj8jAj2T-YKqVSr-V-t5queCVyic227FHI0saHVMyVDde4iGGsH_kQsmsG7i_voBFyMuFGrj1JMEf3W8LMFIRJTMQ4QTYH6kSRmk55rhLnVUFuOG21qejH14pNlFPclb-jqRxJ8W43l_J7HGp_gVqnTtO7sL7OjOSUkYJWwK_6hbU6jwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=QtoAAUYkGeG_pCxXLaFv6WR1LwXNZhbdHXikE3loypj_glVv1UCNeHs2YDFQiv0gW4D1TLBTYjfmWavO8tocDW_oQNs9ITTJWzs_FO9Cz6LqHZmLDeY5sffKW14Xdqhvc5tj7jB1B1FEsbiHsilalce5qrE9F9BUqsxw7WJN6pmBkrMsegOi1M1kxws_--MTMo-eRg1dIVqmdHAz-8j-YqQcp42oYx2IQ2uJ68tVDsciVt3rhFHCFLcNltgFbks6pB9ytSXIt3EgiMiYYLs95HdsN-AyiOgjzvjRstW0Gdp-WhKVkaymySIWPRLkOfBcG82rdboIizXUYPzhXL_QgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=QtoAAUYkGeG_pCxXLaFv6WR1LwXNZhbdHXikE3loypj_glVv1UCNeHs2YDFQiv0gW4D1TLBTYjfmWavO8tocDW_oQNs9ITTJWzs_FO9Cz6LqHZmLDeY5sffKW14Xdqhvc5tj7jB1B1FEsbiHsilalce5qrE9F9BUqsxw7WJN6pmBkrMsegOi1M1kxws_--MTMo-eRg1dIVqmdHAz-8j-YqQcp42oYx2IQ2uJ68tVDsciVt3rhFHCFLcNltgFbks6pB9ytSXIt3EgiMiYYLs95HdsN-AyiOgjzvjRstW0Gdp-WhKVkaymySIWPRLkOfBcG82rdboIizXUYPzhXL_QgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=Cc7D2FvPwict2y03AHCPqr7KTQri97YNqmsxHww5fvtJBe6rrry_jihvHZ7_XdDiyE1VKS3ruWxB0xtTpwlqYb1IPUkEePIEMw-AS2_zRfYDokY25uYtUMDK9et9mzUMgamaWvoAJdtAWBxNRQrFtgWAPjLBRItTWw6TqtKoyd9NooMKTQEsr3HX7F5Cv--0teaIxcvE9-azJ6CQU7sESaUgPPdSsfT8J_fVk0sW3zhAW__NjnxxNRYtLljxwrK42vDgohCZCiq4TFMnME7R0CxOy2X7l8Ueq-tvPzWrjvLxAUgCppMoBr6DLILAviZ_w27Zx2zHV--bNBolVsllSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=Cc7D2FvPwict2y03AHCPqr7KTQri97YNqmsxHww5fvtJBe6rrry_jihvHZ7_XdDiyE1VKS3ruWxB0xtTpwlqYb1IPUkEePIEMw-AS2_zRfYDokY25uYtUMDK9et9mzUMgamaWvoAJdtAWBxNRQrFtgWAPjLBRItTWw6TqtKoyd9NooMKTQEsr3HX7F5Cv--0teaIxcvE9-azJ6CQU7sESaUgPPdSsfT8J_fVk0sW3zhAW__NjnxxNRYtLljxwrK42vDgohCZCiq4TFMnME7R0CxOy2X7l8Ueq-tvPzWrjvLxAUgCppMoBr6DLILAviZ_w27Zx2zHV--bNBolVsllSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5LHpHn15PXhkXh8Zpsy8mrd1BYP3ywNAF8snUi_ExTb-1eLwN6XLaF86x-FRmnWstpT0S_2AIxgnmcI4GmQt33RJkB4oGhIg4VIB9S6Syb5ZVJhDPZY259OkWHpUTMyshdSeYl9tM2ODItl94lXkyqhRlaSNO1dagOjPWX90e8UbQMYTN6OmdDwGS2LCZ3_99MX5bOjvwuHZuPiR6gknzinSkTyRUkHwhp_VyPDgLEdqS5ZiAUuX4rWDLyDLCucLPn6VF8fMcxYgCmFlKgMr7FU2HBVwtoCbmStbTuB2n4-jhPQHhxffPDSmI2jq0BMZo1rj_F5p98NtK5maU54xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CO4qNXQFfoVvKsRVnm0TmIBqHudfVbdMIYIQSu6_NGVolmvEUgwP7W1HW6WFZLyJN9ooYxlSCPwiFUYvmarZklm0A7eStoOGn-8jWrL1favJH9efGj3S-w0nw-HzCq7jwDcX188Foz4lkxOHXwTqIKy5Z3rnBh2O2ewgYYYNXv0N_DJ0oozEHpzzW2JEZzOBNAbcge_kpVK8wW7XLqKxNXvs-l7dKv3ylUwNRhNI9DOxUEqVI8d58ItV676WKi-kGD8RnTWSuCKKRDnw8RcY11oSsEMoxWjENy2p_Wepj3fC3yCm_5QuWgQsIcbJ2HByEHFcsGkcJtldPyzBMbfX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Futk5Ps1cfUG76JquPM90I87G7fwPSHOa8Ph-qgYEOi9rv3S8jMfS5SsTXg3CHIaTmwCWaKGjLqRVIGZyepMSfJFCun_msAiPR44cryoLTdqVOewf37jUylHw5lUxb2AMLsPMHqWdU7Aqd3T7DFNKXmCOuxjNrgKlQL2TXVx5p-uZshcRk3q01iExE0_ngYGjmbmBJp8nbcCuw67XU80jK8P7tF4x5Nrvq87LO7c6V9WjZrYgvLyIzknegBSOusYXYUVtXQxMRiS9IeXAY4fbTyTOrtevJ5-YlcCgotctoE5zldiQht-Dkm1H3RXSSqIme-S_imGOWp4VMoQrtNEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=RxgLbKItd1ze5P_01nzCDwZPXv4tXXqBR_eljQ6x4txtv_OGk0KID7JjDCQhdv7tMUKFwFrCIz1AUYC9sYCE6yoFoHDK9I9s3c9gCw2wwZudby6Q6zqvkOL5iwc9BNXKY45ctp1Zp1lt0zZembiKIC1ySZYNhF_LA4s-G-IcLum1CvRY4h2s1F0PnjgZAzcrWD8pR3NWbxC4-TidRFDOBUsdQnQevaGYJ2SGQmh2bTx3F4nbsyIp8Rqj1ZV4uGaXPb-f7KKkh48oTAm9ahyswUospsjFgWf-I2UgxrDyLRAQ_BjRAY_nxzl7M9bHXUWn2rSHkAKuD-fb_2T_RRHHzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=RxgLbKItd1ze5P_01nzCDwZPXv4tXXqBR_eljQ6x4txtv_OGk0KID7JjDCQhdv7tMUKFwFrCIz1AUYC9sYCE6yoFoHDK9I9s3c9gCw2wwZudby6Q6zqvkOL5iwc9BNXKY45ctp1Zp1lt0zZembiKIC1ySZYNhF_LA4s-G-IcLum1CvRY4h2s1F0PnjgZAzcrWD8pR3NWbxC4-TidRFDOBUsdQnQevaGYJ2SGQmh2bTx3F4nbsyIp8Rqj1ZV4uGaXPb-f7KKkh48oTAm9ahyswUospsjFgWf-I2UgxrDyLRAQ_BjRAY_nxzl7M9bHXUWn2rSHkAKuD-fb_2T_RRHHzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=JqiLwx62E1ORKLXH97J8Drsq1zt_ENgcCTIT4oXxP3KAiDOp_deCSpyOSPbtxMtEvNtuYUEAjlIp0WFdyM8CjXIXYyh_Xyb7gbqNvSWDTyvsmsyPGMXriD-QXOT7ZzAvRYTXozFqAJhkRYoloy_ffh5empZZQf8XF-F1UCXOSEwJkLjuFmwFu48IQm_Kzg4jADgJzn5ahiz4KiMq4spHgT29KIKU_nBeJjvUIjXl2fypQPodvj2uf7PsRE8cWfzo5GpWAAXR4-Xqf_-h6feCSCYcSpAV7OLkrWFm70USsrIqlWhx0aUjmyvP1MuVCIqv10DsjbM3N-c50X47tSrKmk3Trpb7jM-WjcrZt5ki6-4aPV-2fabhaGJ2tOnZqS8OE0qcqthP6BvSbd3GNZZsEBaBzFZS9oI0hKsMV4ujhPygAP53g-EnE5ejGhhhwCaZcGYcIF_FMlRxRWZR3Lfz9HyjUC51AFlZEm5oNGJvvi8gDNZryDtKQkE0x0pwC5ENBzOwRYj-NSd2jhft_1qjO1ZfaPZ83BNOios6BCcj1Xjn4TsJo33BtrkbwGULtMI3SP7w8-wlTY-uHv0_cFHSZWMq9CdYhTxOQHRqCneOL04UEbs0s04yI4tAgHaMvqYM4Bu5WgrBgjBdkaU8OdBAQok4EJlAleBfHy9A8Eb9y7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=JqiLwx62E1ORKLXH97J8Drsq1zt_ENgcCTIT4oXxP3KAiDOp_deCSpyOSPbtxMtEvNtuYUEAjlIp0WFdyM8CjXIXYyh_Xyb7gbqNvSWDTyvsmsyPGMXriD-QXOT7ZzAvRYTXozFqAJhkRYoloy_ffh5empZZQf8XF-F1UCXOSEwJkLjuFmwFu48IQm_Kzg4jADgJzn5ahiz4KiMq4spHgT29KIKU_nBeJjvUIjXl2fypQPodvj2uf7PsRE8cWfzo5GpWAAXR4-Xqf_-h6feCSCYcSpAV7OLkrWFm70USsrIqlWhx0aUjmyvP1MuVCIqv10DsjbM3N-c50X47tSrKmk3Trpb7jM-WjcrZt5ki6-4aPV-2fabhaGJ2tOnZqS8OE0qcqthP6BvSbd3GNZZsEBaBzFZS9oI0hKsMV4ujhPygAP53g-EnE5ejGhhhwCaZcGYcIF_FMlRxRWZR3Lfz9HyjUC51AFlZEm5oNGJvvi8gDNZryDtKQkE0x0pwC5ENBzOwRYj-NSd2jhft_1qjO1ZfaPZ83BNOios6BCcj1Xjn4TsJo33BtrkbwGULtMI3SP7w8-wlTY-uHv0_cFHSZWMq9CdYhTxOQHRqCneOL04UEbs0s04yI4tAgHaMvqYM4Bu5WgrBgjBdkaU8OdBAQok4EJlAleBfHy9A8Eb9y7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raxTOnHodf3k7i_bbAzpq7XJQUvUj4_8eRazEFk7Y4XPHjVhBhQe3EBNBb1EoEzklqFbMjErkJf0GZGH__zhXj5XTJWgELn6kVh8EelR4ltNui9S5Sg04R0OxmgsapuHTXQWTTDHWkOpnIl4OJ2oevw2V9SajAASAGxC7WAE8s6dFCaa80zglX-bpJ_JLWmH4bk_i0Q2etEDnQkmzPPl9kxAYl8vKpBG96glgudDo6PwMUnc0cEh3Re7uyYzvRuCLHR5-QO7nfg-xqhdAX5dUO1DVhbvw7oP8g1KjOTsUMZ5jAXku4o37RVTZWJMRH0Lsi8GDB1GhqaixunxrIcbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OW8KqJzSEwQP4APHVsbLvgWwo2kT0tAa1mqO2QMLT_-4-F_UrPn2Gew__3npsdzEGX2z3uquF1-VFYMditz3u4zBa8ORGVNq6QdTFBWFjffIz38IkeOFwV5xrR1QTFXIEBpX484jPMQuET03WnfB2qJxKTDtzoPoagty3c9sL0r7iiU087KV52xo_A4Nqeqr8n-LlNsBEKIP7BkeSaHCT0fbcIda1jx44Tu95Lh0cZam_td8Tsukav3-4A5eoD3OEMSQYZUCZqCejLzdRT3iqCDawWKRD4DaP09VV_Eq4XjF6_hXlsTMTDGq7gyunOXQmqUDgKx7SIS1qWd6N17gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
