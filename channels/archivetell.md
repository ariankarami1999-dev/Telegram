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
<img src="https://cdn4.telesco.pe/file/fUR5F7yZvvYg4b2FHmt2h5qV3Wkgez0E9ND7lLaEDgNd0V62WQgSftJbHr_dAeiYOJEM6SbGRPpTItYhv_u3dTaz8_h7HIDHzl__F756E86xmbkY6W7QO56LRiRwNpZM7myU0WmdyDUor6T78s5kwlZLMfYvdcJ_eUI0RNyWC2cgjBd_mTBKK19cZmdBtWPsqILTjnx7FQpYS1lfgfePCV_XUkn4mNAynnG676XUipX0CufrX996-kSeCnac0YgX59WZEPMuCxjwlji6S3ZqaRPLRCZsQPlaIVV8-4iibQpTG7-VH9ea1ecSJ7wKIRa8gqVmlnT9M8fHppBUKb5z2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌بازآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 03:38:05</div>
<hr>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iaj5gpyPT5sBBmdPWWfHPk_-aeGuZuAXdm0l4tAKvnvLjmg9suZqS52fmfrbJct_XsiqpBw_PH78EPg6Lkm67lHBQlyWb5umEf3x2yAbBA5Ks4NOhYgGMSdYMEvkQ1F45WlmVd4git8fipJHdLt1BVZARfeFiVNDAIHyG2yHZLIvk0DCmM4TnvfzFiF5zEJRvGsjcw_hr6Z9wT16zYxy5hiUdcZDpIUHDdphGb9eCxi7eT5wK8UJUSFg-0xvcXOC0_cFfndi-M3GgqGgYmLMxbFKHGG0WUVnT7ruNKeGjG2a6HhaqK_0TReFS52nF8hSiwHTK5Eu5d69jyG-IoxXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📰
آماده‌سازی مدیران هوش مصنوعی برای سناریوی فاجعه
‏به گفتهٔ Axios، مدیران ارشد OpenAI و Anthropic در جلسات خصوصی سناریوهای یک حادثهٔ بزرگ هوش مصنوعی را شبیه‌سازی می‌کنند.⠀
‏مدیران ارشد این شرکت‌ها از جمله داریو آمودی و سم آلتمن روی سناریوهایی مثل حملهٔ سایبری به بانک‌ها، اینترنت و زیرساخت‌های حیاتی کار می‌کنند. نگرانی اصلی‌شون موج خشم عمومی و فشار سیاسیه که بعد از اولین حادثهٔ جدی هوش مصنوعی سراغ‌شون میاد.
‏سخنگوی OpenAI گفته این مانورها «ابزار آمادگی برای نتایج محتمل» هستن، نه پیش‌بینی قطعی یک فاجعه.
⠀
‏
📌
گزارش کامل Axios
‏
🌐
خلاصهٔ فلش خبری
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=Q1cPvTg6EB3EzxHpHA25hMS7H0KxSoCdJ1sC29geezBlgwV-GApRim2Y2X2iQKnl7pDgv9r50zhJvPBSb7ysiLnnCJyOXfzghec1IQHntKap3sKnN6B1oXlXtt9DTjws1ZcPvSKuDMqkXthhVTVFD_gLuKGxaNWoV0O3JGewwylJpaL6YujyVVHyDpjnL_fIFAjfibUcgVhlDSjoQCYs5wVG9iT02_SNovJGFg9xPjbgBfWyA7QfI9UnJrWVatAZ_GMIQtYkyCBqqxW3QBsOkYaFBFo2SY9g2q1XrGFuRFGT_gRawev-P56owaMn5_P9ya5oXzhO-yXbdtpE02oDsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=Q1cPvTg6EB3EzxHpHA25hMS7H0KxSoCdJ1sC29geezBlgwV-GApRim2Y2X2iQKnl7pDgv9r50zhJvPBSb7ysiLnnCJyOXfzghec1IQHntKap3sKnN6B1oXlXtt9DTjws1ZcPvSKuDMqkXthhVTVFD_gLuKGxaNWoV0O3JGewwylJpaL6YujyVVHyDpjnL_fIFAjfibUcgVhlDSjoQCYs5wVG9iT02_SNovJGFg9xPjbgBfWyA7QfI9UnJrWVatAZ_GMIQtYkyCBqqxW3QBsOkYaFBFo2SY9g2q1XrGFuRFGT_gRawev-P56owaMn5_P9ya5oXzhO-yXbdtpE02oDsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
✨
ویجت‌های وب داخل پیام‌های تلگرام
⠀
‏طبق گزارش‌هایی که از نسخه بتای تلگرام منتشر شده، یه قابلیت به اسم HTMLBubbles پیدا شده؛ پیام معمولی می‌تونه به یه مینی‌سایت تعاملی تبدیل بشه.
‏پخش‌کننده موزیک، محیط اجرای کد و کارت محصول، ‏کارت پرواز تعاملی، نمودار زنده، دکمه و فرم ‏همه‌اش با HTML و CSS و جاوااسکریپت داخل خود پیام رندر می‌شه و دیگه نیازی به باز کردن پنجره جداگانه Mini App نیست.
💡
هنوز رسماً معرفی نشده و معلوم نیست کی به نسخه اصلی برسه.
⏳
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZP7-cwOSQS1sH_3jWZ2STuf-QdGhYDT3tNnIUevTZxJtgdNgs5VP3vPbb72jLAg3GuMKPqwvMrroPCWPT1m5uw_-difPfzn2VY9-TBocVQ4xBXtDipsUHTkzCK5XSgfGYDf-jEn7YzfVtrlDLBpqITOfMNCtjiouRPHD7E76HJ5kbAfRMSTL9RTVe9pqyuAbNYRsAuoZAUX70e20az4S5l9GPyPiGAkCQVtjctN9P_6M1qzca71GX3wdAuh8pc9CNGBn4LVY_g9GRQQXshCuIbqsaimzmFj9DaWE98s9qcO3UbMCVzxRPS3LgMkNAEDN-PQZZ3KD7E_WubrsV_fp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎹
آهنگ‌ساز رایگان و متن‌باز Tonefold برای همه
⠀
‏بهش بگو چه آهنگی می‌خواهی، آکورد و ملودی و درام را به‌صورت میدی قابل ویرایش تحویل می‌دهد.
⠀
‏
🎼
آکورد، ملودی، بیس و درام در پیانو رول؛ نت‌به‌نت قابل ویرایش
‏
💾
خروجی MIDI و WAV و استم‌های جدا؛ افزونه‌ی VST3 و CLAP برای DAW
‏
🤖
موتور آهنگ‌سازی با Claude Agent SDK کار می‌کند؛ می‌توانی از مدل محلی Ollama هم استفاده کنی
‏خود اپ با Rust نوشته شده و برای مک و ویندوز عرضه می‌شود. قبل از هر تغییری ازت تأیید می‌گیرد؛ یعنی چیزی بدون اجازه‌ات نوشته نمی‌شود.
‏نکته‌ی حریم خصوصی: برای آهنگ‌سازی از لاگین Claude خودت استفاده می‌کند، پس متن و ایده‌ات به سرویس مدل می‌رسد.
شاهکار هاتون رو حتما برامون بفرستید ...
❤️
🤝
‏
📌
سایت رسمی Tonefold
‏
🌐
صفحه‌ی Tonefold در Product Hunt
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=oS6L-_dwOIoldISRO_SFgYi7pa54EG7qwn5DDnkDvuoUw6RGsmo28Y3u8hH0QEoY9yNkCs0SlwoOR6-YvHluXG3zkgw0KvfM5GORS3ARWvLrwFgKYa-rr73L998ZAo_rw7nsvO1h6l0MVwG9qp5jWULT1aqpUpljx8ac-QQ-s2j9PHgSWtmvA1RtQAeSz8A2Eo44hNUawC7P_-tcBWpENuZIiXVpXHiFKhzEv9ZxRpmPLeO9LtEOcVt-iy6yIZvsSGGxJ5XOYaB9qlGZ8TF30xfpFzvJjaXFcDsE9N2ldJQIYdr3zXNMtEUSpX7DxNkpMKR1wkiIyr6RBFzEYSI7PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=oS6L-_dwOIoldISRO_SFgYi7pa54EG7qwn5DDnkDvuoUw6RGsmo28Y3u8hH0QEoY9yNkCs0SlwoOR6-YvHluXG3zkgw0KvfM5GORS3ARWvLrwFgKYa-rr73L998ZAo_rw7nsvO1h6l0MVwG9qp5jWULT1aqpUpljx8ac-QQ-s2j9PHgSWtmvA1RtQAeSz8A2Eo44hNUawC7P_-tcBWpENuZIiXVpXHiFKhzEv9ZxRpmPLeO9LtEOcVt-iy6yIZvsSGGxJ5XOYaB9qlGZ8TF30xfpFzvJjaXFcDsE9N2ldJQIYdr3zXNMtEUSpX7DxNkpMKR1wkiIyr6RBFzEYSI7PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪐
سیارهٔ تازه‌ای که با کمک کلاد پیدا شد
⠀
‏یک برنامه‌نویس با کمک کلاد کد و کدکس، سیگنال یک سیارهٔ احتمالی را در داده‌های تلسکوپ ناسا پیدا کرد.
⠀
‏شعاع حدود ۱.۴ برابر زمین و سالی کمی بیشتر از سه روز،
‏دو هفته کار بی‌وقفه و بیش از هزار اسکریپت تحلیل داده،
‏و هنوز تأیید نشده؛ قرار است تلسکوپ تس دنبالش را بگیرد.
⠀
‏اولش خیلی‌ها فکر کردند توهم هوش مصنوعی است، ولی چند پژوهشگر سیاره‌های فراخورشیدی هم گفته‌اند می‌تواند واقعی باشد و داده‌ها برای بررسی بیشتر رسیده دست ناسا.
⠀
‏
📌
پست اصلی نویسنده در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjIFBr24L2kplmJLijQbKjYeGj6NWvnoEC9QguSL5yMjue_5YAdx5fEFI2eqqhZKOwjiHWOk3HAN1UAFXAnGZ_b5-T0Vn0DIOdxYAEh8yCYrLL2SXoP-a1jUAQeNDXcH1FfAmprTApWdEVLWdBl0763b5FmqYFQjppCym5qiLMqJQetD7WBs_w4jHEY9e1R6IEzUGpgBw_V_VUIiY31G0V_9Qfgrlhn_oo8P3R7GXkc8oqnR3KI5R4Qc5PRJg4pBrpCljEAI03ulzQqtuKRKAuDc3MJf3tXsyBlAFJvVz51MXyjp2QWzBlDoJRm00dvtvlazGWLp20qlU8Leh-XL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmBPewWrYwX3kWHeLb70QdfIazXE5JhLdk-6cUaAH2hdB0Q-ktpbTdE-W7BFyQKxXXIcRqoQNkz8-x_Po1RqVc2AhRPtyWt4lqZv0-6iz3UGODd7r8aGNXCBVBIvs06TRujW-FOh8zsiAmkQSF7lDnjQ7duu_bsdGPeKQc6zqN1xwLGonr2xiynMDfD_GdI85rwrkUDBfrsnSj4QtAiOrNkGT8uuEK9Ww2WxOTN3xJAGwjZXph2ZpENl0-rOv-pGlN8m5nht6trje83HE4pQmQoQ69mlT2fqJZW9La54RUYveY0aEVI8PdfQ9_RU9BlxXvwHgjOHHIBXfHl0-L22qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUQ6XHFIaU53E1f8iKpxNm7i4jtRajEBRPtceLYZUC32adAN7bIOyduZIAx0ncI9fg-StTI4ruzBXF2oGaAyJXSqTjaNrEHBY_zrI1WYWjB0xaVIT4-lTNWttBnghGD2yi5xdIFaho9B3icLrkgfnsIp9vocwe53GSluyxmFX-Nwz_Jkf342MWmn4yE0xc5Sx3nqHmH971hz898q1iVE88QlanOa08bD98hliu2ifbh1LvC59KLhSRHi20kZODUB5W8p_I5v_duN_ZMIAwlSL318L4DqAhseQ6lm6zd81vHj-v8YRYGeSG-6QNftwCtjhDolbef8vFH9nWTf_XjkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
متد حرفه‌ای تبدیل PDFهای طولانی به Word با Antigravity
اگه تا حالا سعی کردید یه جزوه یا کتاب رو با SI به ورد تبدیل کنید، حتماً دیدید که بعد از چند صفحه کم میارن، فرمول‌ها خراب می‌شه یا پرانتزهای فارسی به هم می‌ریزه.
ما یه ابزار
متن‌باز
و کاملاً خودکار توسعه دادیم که این مشکل رو ریشه‌ای حل کرده:
✅
فایل‌های طولانی رو بدون خطای حافظه پردازش می‌کنه.
✅
فرمول‌های ریاضی (LaTeX)، جداول و متون فارسی رو کاملاً سالم و دقیق درمیاره.
✅
خروجی نهایی، یه فایل Word مرتب با فونت‌های استاندارد دانشگاهی (مثل B Nazanin) بهتون تحویل می‌ده.
🚀
نحوه استفاده:
فقط کافیه فایل PDF رو بهش بدید تا صفر تا صد کار رو خودش انجام بده. (پرامپت‌های آماده برای مدل‌های دیگه هم داخلش هست).
🔗
لینک سورس کد، ابزارها و راهنمای کامل در گیت‌هاب:
🥹
https://github.com/faithsaly5-stack/Antigravity-PDF-to-Docx
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTRMXsdCGDj7aFuXUZKDOMm7hpnW2qS8tXsgryFD3PHCjdcXGZ2p3KyLf9II8Sj5xIFz_sJK_jQg5UBp301tbZsYxrgBtzz5h04jn55Rr79UHvLOZiXioSHYIlW-AxizbLy7dQpYB_gnH4WyxKdGokV_nB8KepSF1ydIQcDH1qM3axL5WxWCUncT3bRAmAXYTL8SJd71fA5l1ywFiJ3jSbnRTC2j_LjnocwAW-GkWdIYLJQkwxEUYbCUYq3PZILjLCxwHQCMGjTFcxrwBMNo2V_ET21Nq8H96jydtNydvQMamaDfBis_H_yUjp_LETygjTZrjlR2jg3nXlVDFvnfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inHMD0VAJI-qcSRO3DWI8HLbKNoc3KJmemdmnbkUKgjpxB1FV0-J22WfMkJoyOCez26qjnPXjBaoKKfYor5WkDq7GKuOGffo5KCKCQ7pfJa_6jLOG6sZgDfdwBHUyQJy0NDEku_eYCxIEe695HQhnOskUMHRqkICt4MGLFHi9OnySn1g88lQeZWg73BE-ouysMTpb4BUrCYjmSsQUqNap5SCcJUPWTCr6_0cuPdvc59Ies7-6g9hjThnLnxQFizGI8t49JWlXt58ahv0oYB1J5-TGFluAZZ37CzdGNiQyBIm9YZviUiwbLmPxFGMm4GpTR6qcu7IWHztYlaR0BBgtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">#حمایتی
‏
🔐
برنامهٔ غیررسمی FoxyVPN برای ویندوز
‏به گفتهٔ سازنده، فیلترشکن فایرفاکس رو بدون اشتراک روی ویندوز بهت می‌ده.
‏
⚠️
غیررسمیه و ربطی به Mozilla نداره.
‏
📥
نسخهٔ 1.0.0+1 از بخش Releases قابل دانلوده.
‏
🔐
کل ترافیکت از این برنامه رد می‌شه؛ اول کدش رو چک کن.
دولوپر از بچه های خوب چنل
🚀
‏
📌
مخزن پروژه در گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=RV3R6YkrszUZY4o1_kH3cpmj54vdtYDLthZUMu69sZwkeXUBH7C4pCV1G6zAnbNqa3DqYmD6ElP9Lz-S64CJfals4hi98_S9-tAFiJLKHcmn7nQnHCKiqZBGXyB9xJ6Q-icTnJckhlZnb_scTtBbkdtVfkyJNgOdptKuOVH-1VydJFE9RxJJkYKz3rl08FI5VwVkmiu8saAjKqtLCsemMtBYX-fLjeMgGAZ6Ah7MgCPpOvEuzGZYhkppOx1C11kXcDannBM-HMK73rtxPPqrFBTc4UNXJooQILCUSavDYTAqfMC2S7GSKfILU2DGTNKVg3MO5fzachAtHFXJF8kXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=RV3R6YkrszUZY4o1_kH3cpmj54vdtYDLthZUMu69sZwkeXUBH7C4pCV1G6zAnbNqa3DqYmD6ElP9Lz-S64CJfals4hi98_S9-tAFiJLKHcmn7nQnHCKiqZBGXyB9xJ6Q-icTnJckhlZnb_scTtBbkdtVfkyJNgOdptKuOVH-1VydJFE9RxJJkYKz3rl08FI5VwVkmiu8saAjKqtLCsemMtBYX-fLjeMgGAZ6Ah7MgCPpOvEuzGZYhkppOx1C11kXcDannBM-HMK73rtxPPqrFBTc4UNXJooQILCUSavDYTAqfMC2S7GSKfILU2DGTNKVg3MO5fzachAtHFXJF8kXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-8ZxxgiNjrmW6JeO9gGfhBElqgjgB-Pu6XZ6oRybrplqIRy_gXUs1HIILIP4oh2ixiiaktTBYy6dXBQg2bvnHN1CcVl81dAZmBrOJH8R7eSFypuOtiUo68SJqDtULVqxiMKTfpKZiJ-9BzJU_ENoEIKRjp2sl8zZsDlNioGx6qua2s2PEbS37e4Ll3cNtlPBAAYce0AcPdrrhFlvNsnkTBk35Xofol2pgzEFgbwXz6dg-cfz-y2bdThI6ZyuiHFXvM8wcl4ZHP_Gwr5A1yXC1VS1jc5nzCF6199n2IK-NjuPRDnnMGeqLkeW86ghElDXGWy5Uf61ceHPvgo3mSWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪙
ای پی ای Tooken Club برای مدل‌های معروف هوش مصنوعی
نحوه ثبت نام توش خیلی راحته فقط کافیه ایمیلتون رو بزنید و از کپچا عبور کنید ( یا باید تصاویر مشابه انتخاب کنید یا یه شی ای که خلاف جهت بقیه حرکت میکنه رو تشخیص بدید )
‏
🤖
کلی مدل داره که میتونین استفاده کنین چند تاشو مینویسم :
claude-fable-5-1
claude-opus-5-5
gpt-6.1-sol
gpt-6-astra
glm-5.3-flash
grok-4.7
🎁
10 میلیون هم توکن میده برای استفاده اولیه که بنظر کافی هست ولی برخی مدل ها ضریب دار هستند که میتونین از بخش  instructions بررسی کنید.
Base URL :
OpenAI:
https://tooken.club/v1
Anthropic:
https://tooken.club
‏
📌
سایت اصلی سرویس
‏
🌐
کاتالوگ مدل‌ها
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1AGgCZK3xaUgJ_bAu9jlheZaR85h6Vq0gZMpZ0NDh-_pBYp5h0VTwpPEEYGo0ZTqrTl73FvOY5EERINQzrGs3Lqbdh5ezt2x773G8nFNsBtrsBOU_rEKmUZ3wJ4oqJr2pLGtGm57MMDtAd-UjCG_WBbvlY-uP0C2Usv1cHWcQGd2tIuZ7ZkwfRT0qfBhhqNYX-6Wll02yXNCQWUfu85jCiJbwj-fivAX_74Vn27zyblJqyJWtMWuD4RQYsdu3ogKxaptVtaMZBgJ8o2Z27gchoJCMBpsyRSKSwPxlpqN0aJ3JtAxtUhMiZGPedqqKryCdrBZTpNGc6nPhMmba9QzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6i5O-Jpc8O7exkoUwMWwYu8hDFW-B0bJo9FIzD1mATIcmrMbr4CQYdviYjhU9lqXj9purmk_R60omIwh8PharIS8yaGbAFzE3dvzGZc3wjNY3gtWjNQN0DF8n9enMr5hp9TrnYKa06iyXcL3vZVyAh0O-aBipWc8FEmNvB8j4b5wozvCTxi3CBdG0aorR2_BWzoOstI4adGyTNCH8uHNchfEynVZD2HO5V6APJvSxSyeOJcx_IfF5jV66tO5my25trxmKu9YsGOkaWrPD7JiKzsELrZGr3dLbn3oiheEBhHZdl5QBmSSnLjCdBHc7X-_D18xDnYfTVS-fnj8gbrhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها
⠀
‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده.
⠀
‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه
‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه
‏
⏳
اعتبار ۶ ماه بعد از تاریخ اعطا منقضی می‌شه
‏
🏷
روی اشتراک‌ها اعمال نمی‌شه
⠀
‏این اعتبار فقط روی API خود Anthropic کار می‌کنه
⠀
‏
📌
فرم دریافت اعتبار
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=ba8ORSmM2eEh5ENHHdGfJDCv9wmtZWzdYlBwEr7x1ZMDksJukr3jmphwOQLRXN01E1VioEb0JrVmGLwp4Gby9ffpkVwUsMJt6oaeB_IPQxA20oSIVJg5eWDbjLp9cXolrZ-4jXH4_m7cSx3xBsm_wkhgxIdP6wZA2ZgWvAc-K4rNlD18wvFNTKma3wnR3lW8C0W6AYdpPzcZOjdII3DDn2xHarjXKRrn6DOXiYzkJIArT69vtizzSWPgW9Os0KbthyNE4AMHD72ueCYd3AJwA0QIQaWJkqAIPYK3QmyvShXrtO9_BP7qaXHZ-6rNERV5RPScqOOilOZKDajv5QTxyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=ba8ORSmM2eEh5ENHHdGfJDCv9wmtZWzdYlBwEr7x1ZMDksJukr3jmphwOQLRXN01E1VioEb0JrVmGLwp4Gby9ffpkVwUsMJt6oaeB_IPQxA20oSIVJg5eWDbjLp9cXolrZ-4jXH4_m7cSx3xBsm_wkhgxIdP6wZA2ZgWvAc-K4rNlD18wvFNTKma3wnR3lW8C0W6AYdpPzcZOjdII3DDn2xHarjXKRrn6DOXiYzkJIArT69vtizzSWPgW9Os0KbthyNE4AMHD72ueCYd3AJwA0QIQaWJkqAIPYK3QmyvShXrtO9_BP7qaXHZ-6rNERV5RPScqOOilOZKDajv5QTxyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-J8zrWFChQVlJu-srlng0bCIQS0GQiHu-TWTHtzGg8xfLNbhofLqF6U6iKVjgj_QxRiq17sGxsz32Lmjr10NAIiSOasr3YUcQ_FElvqstZh-jMv4u1xxVoEiR7-f7wpYKFpQctCD-Kb12rWpvpVLCssRLyZl-0KQz-COawHcns-lp_e3XammkaFY3IO67L0MPoVmXs5qboYymkGJfyKqGN5Sxg5AARHU8vlpuYW-GmCCxZXg9LuEZexYVnm9tm_sqSE9fZBe3P_c_MyxFSTB4RLAbxjiNJ4HiAbckPc4rtTDNs63uDYn7BlE-hDfOcoFBQjXgKY--irlB1b07Qaww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نه آقا ببین ai که حس نداره، نمیتونه عین انسان حرف بزنه بخونه
❗️
🤣
همزمان ai
⭐️
مدل جدید تولید صدای Elevenlabs V4
⠀⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMRUM28U2cyFJpkzp8Fpr0IVHlJCIvH2CuGaF4SVCh5kKT_acOU9Y3COlsxdePQhiq1IsHbQtSITnU9Z7xdsp5HX8GFQdlOOiPy--2ewOkqnRsuq8G3TkjYV7sZdsBpb9HpemuSI8D4c3Cg8ScS9y168FEJ_lDy9Yx3urvDbrM8Etlu41RpxlTxiLD-s10Fnf6lFnNnfJn2-zw7s6TLOPNnas9uyJr3joQ91hFrX_9gUnHiXpL5KktWvNfcyWaJ9VdySIECR0gwMViEKbgVgZiLNmijGUjncaq0MYne9wAYfimjiZWMVjzBaYK040kT4Mm-Id29KE2jE7qeLwDPCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfYV4q694bW8USWUdrRrt3SWb1xFK7sIQkrFcvjRCGpkWksNEjCkX-t8dJ37ceTGYmJmK3rjtE9eBdcvZOu9IDU6XNRp2lY_M6tmODUFuExdW5NF3DwCp8N8VBakgQNgZF474XC95jHVxmvTRXPi2l8PYeR30yiHIshMaq0jbnZAneEnSosYCbx4kwccHhgwJNKoAUOnOozvDhEciXnvThgHORB--8CSiJYrX046QvLiQh0PNcJ8gRNp7PdNA2az3PUgQhCh3l6avMtQqw1-o6Xu8RX7_X1RsLEitMLSJHwYT1KQE1DAp_tZnyBRtmcFlCA5zcKYsf5APRQG_DAmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riWTFDhI1v-qZG750NgfQBkAOUIuLt-uTWikCsGunZkV6psMElNwFzNqlLGcIbyxK3bn0SE0-iBRdwVhhET7lJRj6pzAXFr8h8nacbDlZ1HP7U2G_mhMZTF1rDPqgj3fARbVAjZtaAbOEMlHkJQT4f9xGBfHdNIiReJDDXJSseE1yuNS8LTumtwkCc84caSgbs2jRj5uoHCLzwQYq2FBXcmFHdGy2s4Y-y3W_KtfLAfSbWOGtcVLlyHByM_ymrv6QRnudnRUxhqKHBfrvMLvKfDHnbeswpVAfQry6cY0EXb2o3DjoiShd61yLUSOSFpzkFwEKLRWnFhXkTASkiregQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaVOv4jCAY-2vBt4pNM_RM9eHXhEMOH6DH-RkHwtGztjBEqDrz1yFA6TA3CaEMlnY5HrkxjLxilHsJGKD-Xf3-jjm0ckpu3YreeqptfNwqhn3v9FmonjlZuGbfRm8prqZbZ8x-e3KaKfCFkEbx1hww7aw2neV5bTRPdI53A5vI59cUEtGOrw0TwmzkjaRoQP_gaEHjPCi2xJPeuhGdiBGKR70-jPkafVxN060ph7TVyislXZaHaeZswS2_bnkLMGrLA2vjpV_3mRvP8a1vpVE_ByQGYr4visPL-Nr-WAMaRR-V8zbbUUeKfIrj36W7kJPXsg5XoenhmrMom_E1L9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nB8RuKe6wnfl7wOdpvQ-ERzn4W6RjirnMvfiNy6tEhytX75jYnKILoMBaY55fLvWRjEbPoJN4puhwJV7dX0cFbq2cn5GrfkVTkk8_GyGhjbX5ZfcOlxwHv4pFONU-kDtojT5IiO216joMYQlb5pJmjMaKp-QNR3_N49RUbALqDo6yimXLikV73fMpynycXGPhTtGDj8NBh9RNtQT6Y62SgYzx20U2KzvCmOCRes_K2ybOIgPaGIqw_D7eRS_CFMIeWANCvvxMwu4Gu7-jT0l-qlo2JAFrzWBQhTA-g8VHYGKHj7jrK0gBnChkGjdnnG-0gXEPqt6F2eGptEUc40A7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-oYf1iMjBp9eC38dhCzBam8MgFheRxc767KKoYSyAGS6g8a8HqvYstbHoAkOg_DOQWuChpXgvLSGCzE-qpieM2VDJpcgIATIly4n4zDn50a3iCTnsWnycpumEPqauuOMMYyjbFLIGTaJMCbT6jGjiAfePReKYR7qmoZLbdQdeq5NbWL6UNKq18aD7MjaVN1vAsT2bTxL_HsGnsUo2EeFGr7yhNA00CLYJ3mDQWfClwCufcyw9OXLFYd0cfHDVzGlFojnKWTJnbneK3xLRoa9sXKukLTXTvgiOgUjciebZCuCwLQOgoUYkxFCTgGZlmv0nh_Zw6BftLtf3s8AjzFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTIuvu7OsNpCci3xmeECLvSj91gGYoUKLZYa1iEWcA5rIANiAw2T8e36kN8dHAJUwPSvA20Y-4Z_SVqbqy_mIa24cPMKVs1O-aQC-_K4KIoswQxletOai0pbJihs_nGQyI3D9tDXaknm4X5BT2oIU9IoSfns9u3rfwdR26N21Mwlmn01I127Is_rAYctyjmjVigG9I3GS1ZwSlfIBxGGRAdoA8cg_yOCX4uWERJ295fjENRS2NN7elYL-sqed_3xPc0yvOEjr5OuC6JS7vL4OaMmgL9Baei9ARZtS6QbZWEFpms_jm2P-Ax0I2GEZmKv9gPYmoFJBOr-wUqkA_N03A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNchniZQJWUbIk07wvU0CUDYCgamn67uMfNLuUcqn6SiUOxBX5H3TgajRqehgSfnW1JDh_Z-4zjCrkMWoMcB7J9ngz7zR2wTfIZg5o3fjcTLrgxiRM9P1fRfPOngMhFapM5_Bw-uDyki30YB0_ni9MIC3XO5uEvFCHzNwTR7FfYn5KuRSmJifBpIykth_BroCRKTBDjHuG33RnWw4oiZ_JlldqSTCdzQ8-BE5j03D_Ea1tnm6EToh-JSa_334pdy1JlUj-eCxRsjyM2o-eDrBgjiT90il6ST5YQdCtuhgoNWFAt2BsjQKa3FJup2wIqTmrY2PHW_MstjgK4_iZYcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Itnf8xrDUeQpLEA4KkbcqjdO52pnSOB8-W4Gga45H0haOJqhiqbS_0Enkt2-OYLRQz7v4ErCX0zzYH4-z0bwQV_XxxyP8d2dUmWttwxToS6q-66RD3aw8dLtedW5c7bvDO_5O69aQLdrmjqdEy-93jqspBo5CLV_ZjxAGDWuitW8DYMCXKSFJO_jhIPeD9VoAzfqDC4hMvYoPlt-JOg4W1f-pEx4FDiRmYdmS1KZ7zfgPCUT2uBPIatJZ887H7PLvoFpUkRcw30GwC1I8IhX-8epG0aRSGa-4CrAO8l7QuT8F8uIELjl8qmXDMKSzPitzpvUfsEK4figCl5_M6jtkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyyjW1Yb8-kbBNQvJRviMWVc1qVFlGXxC1E4NXVJYIw87G5mgHbfoMQ5Ppo_ZuJpC6rvhNnm5YVGbvCHD6bFiQmK1MxDMpnWqW5JE9K69qnTXiwext9sENPgU8XyGdwTmTGeAyGrK8XjFwObxnksyZaM_PHasAybLYQnEUb7SvdwnRJi8Ue01MxOHqX_z21WaFKnrVgKiLNIvCmJViTxyi0Pnu6Ah-rRFLOxSr0KuwKFKtPJ9NbF5q6Wd2XCE0b-yHr88DTXgcTy4lxDvAUT5D0vUdS-kkuAgICvw0Rp7gTv5us8A0DqMiEXuKDx5m9G4Fla-K-lXzUINU-CMI03Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✨
بنچمارک مدل Nano Banana 2.1 برای ساخت تصویر اومد
‏به گفتهٔ منابع خبری، گوگل نسخهٔ جدید مدل ساخت تصویرش رو بی‌سروصدا منتشر کرده.
💡
به ادعای گوگل، حالت Thinking توی اینفوگرافیک دقیق و حفظ چهرهٔ چند شخصیت از Nano Banana Pro بهتره
‏
⚠️
هنوز ممکنه چپ و راست رو قاطی کنه
‏
🐞
موقع ویرایش گاهی روی ژست تصویر اصلی گیر می‌کنه
‏
🔤
متن ریز یا خیلی طولانی تار درمیاد
‏این مدل روی Gemini 3.6 Flash ساخته شده. به گفتهٔ کاربران، توی اپ Gemini‏، گوگل AI Studio و API در دسترسه و به جستجوی گوگل، Ads‏، Flow و Stitch هم اضافه شده. به گفتهٔ گوگل دانشش تا مارس ۲۰۲۶ـه، ولی منبع می‌گه عملاً از ۲۰۲۶ چیز زیادی نمی‌دونه. گوگل هنوز پست رسمی براش منتشر نکرده، پس این جزئیات رو با احتیاط بخون.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpD_Fm7gIvx1gsJA7TFve7xAjp0NZBzstmC5XH-pLdKwrGuIEHOFmKxusrx7Uz4sNojKKEw9FuqIWmSaXgucrrT_1juZWeaQ2rKl2f3CiDy3aWbAv2eBFQVpOlm071XipoeShQpQl1LiNzbxqnEuiJAEiKVvTDs5NTulc1SiP6S3v_0mPbXyWvJpr7V4HCwr7Ub6nrKi1c2oDXLuDY63pFvJ2dig1iPFIiY_6Sh1FQdrkXuG_eGBKbyDSoy_835rV04nGr-1ELB_PhM6ZZbJTrAy8BpCeYFCug3KJJUiQWebBTAFx_TLZj8gh5F9ou9f5XYjKThvUXxBXXgFQtEsbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MZslRrfF7hfpx-o6OwJb_VCq-q-Yu4zzj5L8S2xY7nR7-Yuv7GVPoN9USNbEHbGQqWG04V-WFxueOZagnmEH5185kTNuV8bmwQzh0u1107w1vNW-aM8nZq6qSg-LXLq5lMe-dcBEi97wuyfQg6oEK9qDlQqibj4oz4QsgImR1FXebffE2Ngl6x4SsYuvNav4kTTMm4_wRE5vqSmkw2PjWCb4BRMRYM-ywlvyrWUcDV3MNJZvVGn9pb4sbrOp_OtFr517QsrLzIcxj6iyXNX1gqd6EtrGNI-x_XQ345X53f8mZw1mLYeeg3JShIKkEYms305vekJin9kOvfQj_PDbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚖️
وقتی هوش مصنوعی خاطراتت را لو می‌دهد
‏
یه زن تو فلوریدا به Claude می‌گه می‌خواد به دفتر کلانتر حمله کنه؛ فرداش پلیس در خونه‌شه.
⠀
‏کارلی میشل هلر، ۳۰ ساله از فلوریدا، ۲۶ سپتامبر توی چت با Claude نوشته بود می‌خواد به دفتر کلانتر «حمله» کنه؛ فرداش هم نوشته یه اسلحه‌ی جدید خریده. خودش به پلیس گفته از Claude «مثل دفترچه‌ی خاطرات» استفاده می‌کرده.
‏فیلترهای امنیتی Anthropic چت رو پرچم‌دار کردن و بازبین‌های انسانی خودشون به پلیس زنگ زدن؛ زن بدون مقاومت دستگیر و به اتهام «تهدید کتبی خشونت‌آمیز» متهم شد (تو فلوریدا تا ۱۵ سال زندان داره). نکته‌ی مهم: چت‌های پرچم‌دار ممکنه توسط انسان خونده بشن و سیاست Anthropic اجازه‌ی اشتراک اطلاعات با پلیس رو توی شرایط اضطراری می‌ده.
⠀
‏
📌
گزارش Cybernews
‏
🌐
گزارش TechSpot
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv-7RhCpnxhKRzpihwZ5OYwolZxtCPgKY6KlewohE64GdMQwFPixQuL6d2IpgoVWJHQ1hIOcIVfmyPt63HdYE9GpFaoq9xboEIo7yscRT1ZWp4wMcrHxUmN2j2e0fuVJ897uKirgDKEgGnck6MRUIh8gWYg-coVPD-znoyiN1NNSl0xF4_ec3e6NQC3w3WtX5mHm9EXDuA3Grc7sW04M8WDQNUDMQsE7_3ppBPp9tkssVQvxYQJH9KAWkDSN7uCLNEw4xXUGY6Je2zR3MlIWyKe3B-jukqY7L-5I0IcGWBuJFsotitflY2e4a4tCNXQkcJbFq26uRZlowE_3-1KrRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
هوش مصنوعی رمزنامه‌ی ۲۱۷ ساله‌ی ناپلئون را شکست
⠀
‏یه نامه‌ی رمزی به ژنرال مارمون که ۲۱۷ سال هیچ‌کس نتونسته بود بخونه‌ش، تو ۶ ساعت باز شد.
⠀
‏این نامه مربوط به مارس ۱۸۰۹ئه؛ دستورهای ناپلئون به ژنرال مارمون، درست قبل از جنگ با اتریش. خط اولش فرانسه‌ی ساده‌ست و بعدش ۲۴ ردیف رمز: ۱۳۰۰ واحد رمز با ۱۵۵ علامت متفاوت. کلیدش هیچ‌وقت پیدا نشد.
کارتر چرچ با GPT-6 Astra اول اسکن صفحه‌ی یه مجله‌ی فرانسوی ۱۹۶۹ رو رونویسی کرد، بعد رمز هوموفونیک رو با آنیلینگ شبیه‌سازی‌شده شکست؛ کل کار حدود ۶ ساعت زمان مدل برد. حتی وقتی متن‌های تاریخی ناپلئونی رو از حافظه‌ی مدل حذف کرد، به همون جواب رسید؛ یعنی رمز واقعاً حل شده، نه حدس.
⠀
‏
📌
گزارش کامل رمزگشایی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=sNvHWHtLXBpV4uTd5pxzXILbIi2DVs-2rbq5jwEkmW3v4EpT9O-UY3EzmMJV--nyZcFgzWdyl_11qrFWCXSQFTVBqxgUnP7STm4bGWD0QpSwHGDpp24Xkc1jPuaMpCIH93QEgsYsm2vaCxJoH-mWF7XrDhE0HtzAWjR6K2LZFY2UnJlaSToIPXCKu5a5cmletrYsWYou-iZt_bZY0_Ta3bfd3TJQ5LnjXiIGVKTf9PWqH_awYIlwOcd6IT_kcxjZQ-HUW-SOJBx0kIQKleeIFw4BNqx0qLppYSmkwomUXAdGNOHOtDpHY6DUC2bRQI84cSBirTXDFMkeI4IK3MsHlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=sNvHWHtLXBpV4uTd5pxzXILbIi2DVs-2rbq5jwEkmW3v4EpT9O-UY3EzmMJV--nyZcFgzWdyl_11qrFWCXSQFTVBqxgUnP7STm4bGWD0QpSwHGDpp24Xkc1jPuaMpCIH93QEgsYsm2vaCxJoH-mWF7XrDhE0HtzAWjR6K2LZFY2UnJlaSToIPXCKu5a5cmletrYsWYou-iZt_bZY0_Ta3bfd3TJQ5LnjXiIGVKTf9PWqH_awYIlwOcd6IT_kcxjZQ-HUW-SOJBx0kIQKleeIFw4BNqx0qLppYSmkwomUXAdGNOHOtDpHY6DUC2bRQI84cSBirTXDFMkeI4IK3MsHlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4giNRsbepuT6VdgNYiYoGZg5I9GYsextdY63ZsDfcbBJM32xkcVYSW2I1bsrIOfUZk5nn9R4GoW3wVEtnS8_qIV7J5Z5qCxvaRpf-Y0eSa1e6SItXtidRSVLCY5ratVmp_UGLK8AVEZr9o34dYJPTc9cJomS64ClFY-WYWopR9e3-SJJDuQJIzJT-WZSb9HkgC-O2-iFEFYu4AH01UqaJPfVYVPMrOk72KZoNDz__79lo0vU31-dYGJjymByE9Knlo_kzIftEqnhcQW_vq9XI5F8QtFUKZ2aignp5hDhNvB-1gxRXjsoPYpQAKBPF0c4Os-nYaereleG-ElWlHK_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_Pk9R0dFPXoQO_gp4wHlfXOHiKBjWXdqVk0iqbBfrFwWBQI4-YqYrHQudqRXqacpOKb4cLAlzUz_zGz3TgY32MJMYBtt5c7HIR5k-lVLWiCe11R6nBq9fRAfcR8kdB7ke-qVUketBwAhHtkpcWyGNAfzYoeEeasci_EdXw-WTml3E_T1hzftPGyLbM55ronLixgN1MppDudT_IPpkBaa8efIFfNtxzDJCBXBNAbstAcsfnS4_jy8QJk6meJ8ZogndefeQzyeGgGVezmIKXzMMmvtyqeLe5lE66cAV6_B_UqNxrS49p8TOHhszDjr9GJi11xbAuRgM6pGem88AMikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txsf5Wrefq57KIWrLz_riSi4uvDvUNuCL46QFsh-Zvas6g_KBj6Q9BPTT9CS6BqXofdU3qbHrCVHQoaTSV8js9R20Ggbv6uTpXwuTuSz4IUwwtEoVmogPxr2q4pRc1wNFgNrHPR93wLcu-7AVwWJROOu2gB5Jk5Uucxv1YCRR31_LmogZ0-CgROFbE_XfSNVcNznawpwR8PM07mGEvE-dLzBtEEEiT9vy5p2Cn1q_OfrYgbkFije2Rw_u_qLT1yDrFU4jRvTOWGoLQsY5Yo5faPdURfOpvWXQq5apPy7brfj6q1EjsTlpwwMtMh_uJimEuttpOPZdFC76D82l1HjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VcEjlwJkL-0_u2esmzIv6c72kzzNoPe66hZUv6J8Vi9R_KIhomDctbCCn0TxafI6YwvVBV2QJ6wuxLje2QjRnVOnCL3R83oCsXY5DXgBE8FBb7VW6EacugW84QZ2FS9GqUwMjsY6hW55FSde-xlIqQwOduU4jnnIBbnCsODlEPAF6HPJpgWcD2t0k-WqpjSrmgrGSWb76cTGhLx9Gaa9D5ZymjBLvWFIV3ofi5eQNLNkXY3H2Pw5Y6YAsLKccKKodPid9mA-j8_2Ade_kEZyjtXAGemkJBavAhrd6HazdPXlwFUMgCU9nCccnloGmpSl4O3bwKf1NetQuyZKcjSEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rn7HD0VfK-D96kWwghKJQ3v1QfB2H7DtLp6Z1p3YST-IgeGRWN_Uu0Vl5zuoOYESX8OWHP7KC0Rs2QuZBVzPbOFnSMN6VMdTS1WsMQmmmLFAOSfqAiREuwYyjrgpxeTErruvhY8rz8lDmMw1r4jfyJxXqpd46cmMlbbkEPexfAqYw_kiXZMurSplT_LaxX9m4w6nEzsSP9CrUlmJ3TjiufhPeyzT7rrqDSRzLZgYAsESkpFdl1L8mLAsu_1602zHHICZQtGYs4Pnlrylif_GeVGGdv19swn6B2m4am9hVFOlpVfxiO3mjmElWGN0U5W2ViVtA1xoI8b6AersowsHFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🎁
فهرست اعتبارهای رایگان هوش مصنوعی در یک سایت
‏این سایت پیشنهادهای رایگان، دوره‌های آزمایشی و جایگزین‌های مجانی ابزارهای هوش مصنوعی رو یه‌جا جمع کرده.
‏
🪙
اعتبار رایگان، دورهٔ آزمایشی و تخفیف دانشجویی سرویس‌ها
‏
🆚
جایگزین‌های رایگان و متن‌باز برای ابزارهای پولی
‏
⏳
مقایسهٔ سقف استفادهٔ پلن‌های رایگان
‏
🔍
مثلاً دورهٔ آزمایشی ۳۰ روزهٔ GitLab Duo که مدل‌هایی مثل Opus 5.5 و GPT-6 Astra رو داره
‏خود سایت مدل رایگان نمیده و فقط پیشنهادهای بقیهٔ سرویس‌ها رو فهرست می‌کنه. بیشترشون سقف مصرف، زمان محدود یا شرط ثبت‌نام دارن. به گفتهٔ خود سایت هم این شرایط ممکنه عوض بشه. پس قبل از ثبت‌نام، شرایط رو توی سایت اصلی هر سرویس چک کن.
‏
📌
سایت nopaywall
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDZuoSL_eCM-ugy96V-Otg_Ht1Kjo7IctAdhOPIijC4mFdTaY1U1VHZUCtYovrtFepQS--JfMnDUnwbLg8J_8SDCcDAYT00HXFQz9yqXQ5ZqM-6hiBTWDZsETQY6lOFF5v7rW9iBNWKn3EzMCBuaHxuqAydgRo3-e81o4mngHiYY-S_7CilIukQ01gtOCK99t-IHGpOQKcmWM8hS0XMS1cUnvMKBrRpq4wk4X-0x_ojSh1EBxJQvA5MaI0b34MpTAdlZ2-1R2JSZI8urpo2658Vxub-E0vETjC1e6lJd8DH63IfXjZWTvC6eWhiBuCKTn7PCqIAQTlNxV2IFtB1MrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚀
تبدیل هر چیزی به PDF فقط در چند ثانیه!
دیگه برای ساخت فایل‌های PDF نیازی به نصب برنامه‌های سنگین و مختلف نداری!
🤩
ربات همه‌کاره ما اینجاست تا هر محتوایی رو که براش می‌‌فرستی، به یک فایل PDF تر و تمیز تبدیل کنه.
✨
این ربات با چی کار می‌کنه؟
📝
اسناد و متن‌ها: فایل‌های ورد (.docx)، اکسل (.csv)، مارک‌داون (.md)، متن (.txt) و حتی فایل‌های کدنویسی.
⚡️
عکس‌ها: یه عکس تکی بفرست یا یه آلبوم کامل؛ ربات همه رو توی یک PDF مرتب بهت تحویل میده!
🗂
فایل‌های فشرده (ZIP/RAR): آرشیو رو بفرست، ربات خودش بازش می‌کنه و محتویاتش رو توی یک PDF برات ادغام می‌کنه.
🌐
صفحات وب: لینک سایت یا مقاله رو بفرست، نسخه PDF اون صفحه رو تحویل بگیر!
👇
همین الان وارد ربات شو و رایگان تستش کن:
🤖
@Everythingtopdf_bbot
━━━━━━━━━━━━━━━━━━━━━
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eNqYFhrq4c6kAGivI9TXBxLI8K7cgTKZqkZbrtoeaThZuWjH4gWWlwHG-_yurxOtzx406uWYO2gavzz1nYQtdxsiXP_7cmnTMjM3aXWte8lRQUI7nb61SPdeZpeaoSCi63TlCmQpS-tZDjW5uiT0_Ly9YGAiQJIwtd-9ffSCYqINHMXV8epGKpL1MTxkpno_IK2Fwlka7XTDV4dRP8K0AXL2GSONOg_CE1J4vP4Ot4D3tKtEgduab_KZ2aLDde6Fn3fGM6Hc00G95kbK31JCPfdu6VKBmaUgWCUd5UipnW26P9KP3gD2YuJi_RzN65TKsV9n3yob4jJpg6_xa2884A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
کلون متن‌باز فتوشاپ با Rust منتشر شد
⠀
‏استارتاپ ArtCraft نسخهٔ متن‌باز فتوشاپ رو با Rust منتشر کرد و ۶ ابزار دیگهٔ جایگزین Adobe رو هم وعده داده.
‏اسمش PhotoCraftـه و روی گیت‌هاب با لایسنس MIT منتشر شده؛ حدود ۱۸۰۰ ستاره گرفته و همین امروز نسخهٔ ۰.۲.۰ اون اومده. با Rust نوشته شده و از شتاب GPU استفاده می‌کنه. البته هنوز نسخهٔ اولیه‌ست و نباید انتظار پایداری کامل داشت.
‏نکتهٔ مهم: چند کانال نوشتن «هر ۷ ابزار منتشر شده»، ولی طبق سایت رسمی ArtCraft بقیه — VectorCraft، FilmCraft، LightCraft، PrintCraft، EffectCraft و DesignCraft — فعلاً فقط «به‌زودی» هستن و نسخه‌ای ندارن. پس فعلاً فقط PhotoCraft واقعیه و بقیه وعده‌ست.
⠀
‏
📌
ریپوی PhotoCraft در گیت‌هاب
‏
🌐
سایت رسمی ArtCraft
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z9XWg9wA_PeJhlLozzVXEbQ7_akH5UHeA3BN_P4FYE36lPRMZMDcwEKLF66WEGvGa4T2NS0UbAObp79RDV5gpDDC27ANBwpd2QDhSfQ_OyW0R41rkm6STj-sWaFJl2MA--SKgrV9yMVx4OpGqz-Zq6GJNksYImAlwPzTfVfNXpPuXAl3oyM-_81aZ9d4xOmtPt6uubyizDGf0KA30NthZQEX4riR3SqSqWlcH6YmG-EEJVr8H3fmNEnAKmyJjE4w6kORo6DG-1EN-tvOMvUvpLc_6wtHQkbsJgNEtYFvv0sp3rgsT528VfHViIZ_GMRLVIExwYJsLeo8VflIa7fehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚔️
هوش مصنوعی بدون دیدن صفحه وارکرفت بازی کرد
‏⠀
‏مدل GPT-6 Astra بدون دیدن تصویر بازی، در چهل دقیقه منطقهٔ شروع وارکرفت را تمام کرد.
‏⠀
‏به‌جای تصویر، بسته‌های شبکهٔ بازی را می‌خواند
‏خودش ابزار ساخت، مسیر پیدا کرد و استراتژی چید
‏از یک باگ نقشه هم بدون اینکه بداند استفاده کرد
‏⠀
‏این کار با فریمورک متن‌باز agent-wow انجام شده که هیچ منطق بازی به مدل نمی‌دهد؛ مدل خودش سیستم ادراک ساخت، اطلاعات مرحله‌ها را از دیتابیس بازی درآورد و با برنامه‌ای که خودش به زبان C++ نوشت مسیرها را حساب کرد.
‏⠀
‏به گفتهٔ گزارش cnBeta، کل این فرایند فقط با یک پرامپت Codex شروع شد و سازنده می‌خواهد بعداً ببیند یک ایجنت می‌تواند به‌تنهایی تا لول هشتاد برود یا نه.
‏
‏
📌
گزارش کامل cnBeta
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fotvg_qdWffXsIWLq6gMEH9rtRx9ZeriFye5ofNhMvb9KHe6Hm5thzm8kgO0SGjGPg_BYLgb0SaBYDDf-kI9r0EacU3otioctYEV4G_r-UFg_HffPSzM1YP3bzOgp554x-GIFqixsGzPLkWWEF2AJU-OLAqkKoCucMEewnOrlmwrS6E7Y1X55vsZ9pi7MwPA5guKCIOyAXV7dbjUBPLRqhEFxJzWegKd7A7X4uLRazoj6X2tcTLZ09f5GMig9TzPiKvw3bO_mdMD_7PakFBOv06Q3-gFc8M-vfLJy0v47HTDF1jr27iQkggH7-AHjLVsFqTt4DcbNQFkA06Li4PRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔍
اسکنر امنیتی هوشمند و رایگان برای دولوپرها
‏یه ابزار امنیتی مبتنی بر هوش مصنوعی اومده که بدون نصب ایجنت، آسیب‌پذیری‌ها رو پیدا می‌کنه و جایگزین ارزون تست‌های نفوذ گرونه.
‏⠀
‏•اسکن آسیب‌پذیری بدون نیاز به نصب ایجنت
‏• تحلیل و اولویت‌بندی یافته‌ها با هوش مصنوعی
‏• کد اصلی پروژه متن‌بازه
‏⠀
‏سازنده‌ش می‌گه چون هزینهٔ پنتست حرفه‌ای رو نداشته، خودش این ابزار رو ساخته.
‏برای دولوپرها و تیم‌های کوچیکی که بودجهٔ ابزارهای انترپرایزی رو ندارن ولی امنیت رو جدی می‌گیرن، شروع خوبیه.
‏⠀
‏
📌
ریپوی گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel | BOT</strong></div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده:
⁮⁮ ⁮⁮
🆔
آیدی عددی برنده:
2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل:
@ArchiveTell
🆔
آیدی چنل:
-1003718102196
🎊
تبریک به برنده!
🎊</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00  قرعه کشی انجام میشه و شماره مجازی تلگرام به…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR8ZJ_Y0TWdpJkeAZJLFBR6EMyvedA8M0dMYaXR_i2v42AvlxjLaJ5NZaD2wAYYEq6PNgJRv63JCoXByYzrhCEJ7sTzR2fmpfho0sUooiNtpAhQ9inDYmbfWpxnn0_PVL2F8noL9wLHUR_4k0ivlt1VBHasP7Eis9d6_WXIfb5AfNV2h0fLqrQ2XdvqT50ZyAWcBsce9H0lVA37F70KWkgZqu2rZYEAzp9jrAm089FhaCf8kU8QegUJM06wHn_M2nLlF2wX88F-h9usF8GN7zx7L72KuN-VUhCWGGxA_yJM-fnV71ONTg2vDG8DpewS_-2YrZzLqfmVG7MTr434IlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxDxcpCQALDSRT45hf43XwkHHT8Cdl1U_lYtANfPg-n8ppPzzjBSe3o-QVyE4ZFC6WLTnifjVJuW8QxuB3BHlqth8IQiqj3yFWyFLNqU49HwwxyzjoKz8K8hQ2rwFx0zVeVWjzhZ7PPUrd1gMVVFqvN6Loah8ZvnELh1UyI1S6eZm0azavYPg0gIf-J7btSxZZdMmUUR5-zUXUplKiDPkMgEKi03X_2PosDBsdm4uKjmM5-WZOLnIdBfYhx67ogsUsXlLAWYcLFe0CWS7KeGBtdATS8xfFST9K8CD_FkLnh87kU8ZrTo7x6aPJLr4fpldWOdetIaNqqP0eFCfpgCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📥
دانلود راحت ویدیو با Yoinks از شبکه‌های اجتماعی
⠀
‏این ابزار متن‌باز به شما اجازه می‌ده ویدیوها رو بدون تبلیغات اضافه و مستقیم از آدرس صفحه دانلود کنید.
⠀
‏
🎬
کافیه آدرس صفحه رو از یوتیوب، اینستاگرام، تیک‌تاک یا شبکه ایکس بهش بدید تا فایل اصلی بدون معطلی روی سیستمتون ذخیره بشه.
⠀
‏
✅
چون اجرای برنامه داخل ترمینال انجام می‌شه، فایل‌ها به سرور شخص ثالث نمی‌رن و خبری از تبلیغات آزاردهنده، پاپ‌آپ و تغییر مسیرهای مشکوک نیست. به گفتهٔ سازنده، بیش از ۱٬۸۰۰ وب‌سایت مختلف هم پشتیبانی می‌شن.
⠀
‏
📌
مخزن گیت‌هاب پروژه Yoinks
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-oCbwGC_5GJqwFLFre4MxdnQVRegVzxs1NUz0qbASfhylyJuq35GgarUyQwHdtkXmNwcVqlJ1iJiWJPcmvGokd1E5e_hlI_7sZDGrdmE7G-Ary48dJ8VjW4p4H_wSvfVB3ecZ8rmFLqeNwTrOfOGCzN6-mWNs5ltIYoQTmCHzzdNK5FmFRu5txpezheMDgbMdYJg-PQe7c4hnRtoexpJhDUcMJFdrVBDHDQDAooAJbr_1PCupsmYDECvMZSw1PVwW7ryv4P9PbJKBpPXgYJm8tLtba9a4-5_jlIWWfKYP2dXoyitZGmIH54Z5iBS--t0phNa1Aq0ySjhQV38M2-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ترفند فعال‌سازی Opus 5.5 روی Gemini Pro (آفر Jio)
🔥
اگه اکانت جیمینای پرو رو با طرح Jio فعال کردی ولی هنوز مدل‌های Opus 5.5 و Sonnet 5.5 توی antigravity برات باز نشده، اینو انجام بده تا بیاد:
💎
اول یه اکانت جدید رو به عنوان عضو خانواده (فمیلی) اد کن.
(دقت کن Sharing رو اکانت اصلی فعال باشه، و ریجن هر دو اکانت یکی باشه)
برای تغییر ریجن این پست رو انجام بدین
😱
بعد با همون اکانت جدیده لاگین شو.
تست کنید ببینید براتون فعال شد یا نه؛ تو کامنتا بگید
💀
👇
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eqa6yXfgpKrXUZ51_ay-AtTWl4hTC7rpES5weV-t8GCCCNYNHfREpx-MBfhDhE_pKmi5QRqqMKqV2w5iv1m8NiPRki3Jq-9eiVx_-Sv1uuyBzUx6ehotblvW-BNYd2YplGwU7Cst5M7P7NrAHafyv8aYvevcUO628zVp2UoeyUx_OwH08tmLTF2vEmBcaJxWVo8TlICe1ofF3TI3qzDD_Y76Btgxxr7NjeOh8qHrc-icrj8Qab1kOIhVXdfoxeEyDis9S_P7N2xTk8Th8-KQgzKoLt0mDphhjrW3qk6BMIHz-KdnIPBziS1N9_uzRboqsipE4O7rUdS2tJY9gCaixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nYWLHOWdwzmLQ3Mi9IjpPCbQSIxJ9pUHq4-j5AFtsDzc8wDAXYXfhCGtuh3o0-zKIkBRiDmp6ADsmQJA-u9kIVnZ3a3OD7BxZUBify1i7MyfL4am-OZmw7WCsBGr5wfLbj1EXNgZBjDdsqqZtLQ84o0qPx8-TvFdmXVrMV0PwaS9GGfoWR9iNDvpLNIgES6RBAfNFADaGOO3DLrP7sDuWFZRXXt3LUpvxCpHZmw3KfsauK5qY5Jl19WzDj0EKxXsf4X4cotCWH4X6u2VXKATaIut7C-IByxY9HmQZ3xLgnuLoxiXMNdRikPQf0ymRyPwk_pB69dwmo0YRSKnC6bLIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
☁️
اکانت تلگرامت رو تبدیل به فضای ابری کن
⠀
‏یه اپ دسکتاپ که تلگرام رو به یه فضای ذخیره‌سازی تمیز و منظم تبدیل می‌کنه.
⠀
‏• مدیریت فایل‌ها داخل Saved Messages و کانال‌ها به شکل پوشه
‏• پیش‌نمایش، پخش ویدیو، همگام‌سازی پوشه، WebDAV و REST API
‏• ویندوز، مک، لینوکس و اندروید؛ همهٔ قابلیت‌ها رایگان
⠀
‏برنامه اوپن‌سورسه و مستقیم به تلگرام وصل می‌شه، بدون سرور واسط. ولی دو نکته: برای ورود به api_id و api_hash از
my.telegram.org
نیاز داری، و فایل‌ها تابع محدودیت‌های خود تلگرام‌ان — پس «نامحدود واقعی» نیست. نسخهٔ ۵ دلاری فقط تبلیغات رو حذف می‌کنه.
⠀
نکتهٔ امنیتی: اطلاعات ورود تلگرامت رو فقط توی نسخهٔ رسمی از صفحهٔ ریلیز گیت‌هاب وارد کن.
⠀
‏تو تلگرام رو بیشتر برای فایل استفاده می‌کنی یا چت؟
👇
⠀
‏
📌
مخزن گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcPNs7Er9Di4YmQVRHDiHSaJd2gXRcZsbQD0nD_gDbVRiCLN_Z3wWVo3QiAqezjrapofYTfCf7x7FxOIpC6bzclq_WlJHmkhBLdpHmiakWFi9uy2XEagWetYOl5AwY-7xNrw9Uf-V6zOInzXIIeeM6fb0ho-CMz1weCfDv_6B5t3fs7sasBD56Qx5ND2DqAaEveyHgAyx3oHmNekZnnN2Me4FY-C0fsmmpbsQ86e8TnnxSoyGT-sZQd7IU1xeez0f1qbkcO3UGaROL6XFmcR9k3uiPFdwluIsxw9tm4AP-qkPxPknwbJhDJAl8x338-wattuaf0-3vjposk-b0yOYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش
‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.
‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری
‏
💸
کم کردن هزینه با prompt caching و compaction‏؛ به گفتهٔ اوپن‌ای‌آی ورودی کش‌شده تا ۹۵٪ ارزون‌تره
‏
✍️
پرامپت: هدف، مخاطب، محدودیت‌ها و معیار تموم شدن کار رو روشن بگو
‏
⏳
کارهای چندساعته: عوض کردن دستور وسط کار و سپردن بخش‌هایی از کار به agentهای فرعی
‏تمرکز راهنما بیشتر روی API و Codex هست و برای کسایی که با این مدل‌ها ابزار می‌سازن مفیدتره. قابلیت multi-agent هم فعلاً آزمایشیه.
‏
📌
راهنمای رسمی اوپن‌ای‌آی
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgBap259yOTZSpgWBmNdB6SO-MU7ZOWJKqhCQTX4OZFpSH8XnT0S49OfEveEsYHh5uKcTxg2it76_jhQ01Fki4GteSuOBHKZUvZexLwMkJdzCdCGgW9Ev_cuGdBsYxumOLeZtJpdqsLK04dnTdP9m-nGxMfR4cDUYqWuL19TySoV9gZZ3YIWYky7rYFHFromrhFsbGKbHNwKFigTXLyfmEYV0pOJ-oHByRv5dH2NwVaVKeAx07mNzMZp4rGdvGronvIr2GKahUTQ43mfVKOQxAz2RqaFd1_XEq1ihjN8acFnasM4rJ0eGOHl8raGSK-tys8Poux0qGXd_V2zs_1Qwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚫
انتشار Grok 4.7 در اپ‌های گروک
⠀
‏مدل جدید گروک حالا توی اپ وب و موبایل هم در دسترسه و مدل پایهٔ همهٔ حالت‌ها شده
✅
⠀
‏به گفتهٔ xAI، نسخهٔ ۴.۷ روی یه مدل پایهٔ بزرگ‌تر ساخته شده و با یادگیری تقویتی طولانی‌تر، توی کارهای کدنویسی چندساعته و خود-بازبینی بهتر عمل می‌کنه. پنجرهٔ کانتکست ۵۰۰ هزار توکنه و قیمت API مثل نسخهٔ قبل مونده: ۲ دلار ورودی و ۶ دلار خروجی به‌ازای هر میلیون توکن.
⠀
‏
📌
یادداشت‌های انتشار xAI
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYCGaNLTK-csC11TD007OkDs2zR544mMSqN1_ZqFNRS3SqXRFjK6_1Ml1lKkKkv9xQNhgjcH99ViXH07qNfD9rjpI4mhQswxCrot_GCQaGvOYubV80FSWSKoDMa8auxDdQDJVktzJo_WcKQW1mSRDMo0Yl6afm1W1BDMTwb-fw7Mr179ewcSwDDlM7ScAdxJliRwktWmilTHVKo5l5g-64BGH7oiizb5p-miIa03hOU5mZZ2gGj854EFYSmoshq08nmIQTLY6x5u_C2RUsU_Y6TY6Nud5cBnzzapAzjloWP6BciweDvLY7B-ihWMwA8TiPpiwH_Ckdq1sL4oRKdpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان و ممبرهای عزیز آرشیوتل،
😍
ممنون که تا امروز با حمایت‌ها و کامنت‌های قشنگتون سرپا نگهمون داشتین. سعی کردیم به قول نیچه «با خون بنویسیم». راه سختی بود، ولی به لطف شما هنوز زنده‌ایم.
ممنون از ادمین‌ها و کانال‌هایی که با فوروارد و تبادل منصفانه حمایتمون کردن، مخصوصاً تیرکس نت. دمِ توسعه‌دهنده‌ها و همه‌ی کسایی هم گرم که تو روزهای قطعی، اینترنت رو زنده نگه داشتن.
تیم خفنمون هم که جای خودش رو داره:
احمد، که داره به مو می‌رسه ولی آفتاب شکوهش کانال رو نورانی کرده.
وگاس، که تو روزهای قهقرای من پشت کانال رو داشت.
«اس»، که با اینکه گوگل‌فنه
😁
یه متخصص واقعیه.
محمدجواد، معین، ایلیا و همه‌ی کسایی که سهمی داشتن.
خیلی‌هاتون دیگه دوستای نزدیکم شدین. امیدوارم سایه‌تون بالای سرمون بمونه و مثل همیشه با لایک و شیر پست‌ها همراهمون باشین، تا روزبه‌روز قوی‌تر ادامه بدیم
❤️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyt2yyY3l3FCIgtWwAcjW429EfeUfIn0bMxreApn3HYr-PFhf2BjJstxQ1HD2G-CwHOXjRD00UBoX-zHhWYiVPvtDAiazoEy4O3aCqZQMKunSjMSCURPqdU47NINt3-XgC62EKHmnngwt08c7ET2XnF0dqrxE9F70ZABtGufyZZXQdsHBxlU8qWcnaZohV5d14iJgVg0GZekCbfsDe0j6PF23aA-lw2DNaphJyf6ZVsjHdVmdEagDQvjXq3LJ9z_oHzfyc34DFsYQA59GkKWUWCiSxulWmNF5t2zVKkKPj5ECx5iiEtxi0R-li8GLT2Ps2aLLgBDMpwmCkGX_as7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDt2JmvvfgpEJ5JsW4Djmdzdnhu0Klj9sP-eSRlL1wbC2Fr_8T-HLmC9p1xCH-5epXR_OnHBulP2kvzflDDj1F3I78tXutv22Ws0M3IWw77CNLX_2Ndck6r7TmnPjWb_0B8hKfR4XVQcTgrQOVOXHodgIo-xd-VQysXp5K9YsqPeMjRzXj8U9KgA6QuuIj0gGpc7l8QuePH-9tcxgyCypZIcx5jeYCv8_QRcyMvtuOaIzbmH5zVZ2l7NAQsQxtPrSIEsa3WCOtxWFW6_S-p6ZwJE8Mzp0Ofquc4SvV9XFqIsw0em1hHCfoU-N9q7z7wmnugUIzupDjGfZ-SeFa-KVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A7Pp6j0R8CZoIsvna8qzQBsR7fqMMH02SVokKCneL_LdTsRo_aIvOCD3e1wpU6_tIvZoEJYHANl8taKJz-tAqofuYn-OSJl9gf6Yox8WLXIhDE3THDHq0nba2vJ11Ev9CDS8-k75J_pQEhhEVUl38GSCjrVNosajZTJr21RHdMPsi42dlnLoHCo1lMmVa1BjcVgYDcDUlSOgIVTVpDWnHpwURU2Er3C-aB02oJBYQDLuR51x28g1Q_HDkSEmQE1AN7XHp6uo9y-3__oSPFGbnqABTVfak0qCj9AvpNSLQOC-rt00mlQsmBOB6Gf00ic7KKoCODhPFLV09_VK_ncMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hRISoetCBBE8jIyF2iNAIExB_YyrOTIZAjkNEdszmnGBE4srQzEo4d0QJUJXitwkxLbbnVAAeZ0ZR681RwJnMkUWdoL9UiJYkXP-MRHM-yeJEffzAudfr0I8o63MKyZfKhp3_2PgMxZtRzg4tR0QBg981ud1FJgnfSXoV_OZaZLLakArwXf90fD1KeXJurd4MmrvjIMuKlhaJSqa_QySKQGjLdQBP0bp2YG6kQ6LH6TXnURopu-2k3Y5xmRVFVomNe1IDEIkgByRzbM5bRsZhnezpC8r9J2zjrUXIBPeC3Ss6ZiJQvc-Ir5dfUmZ-jDvZ1DSIJBciz4i8rhTATBcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7QiTg4gW2pOiSMsGuvXK5tCEMoKDQnpttc4b2Dsqeah527YIoRt9sGF8pfgAXOFrginIW98rE2YCUdx183LYdAbuTUAIunyY1rqNKT4onvQ_Eh5rGK-pIQEV0if8Y6nXgqwb4FF8Qjd1wVO0bGGFzdYfTlfw6Zkq_3KXGTmF3D-7F-B4s0CVPCYKXub14_cZ0h_50rH7rH-QGWJtAJR3eWZn9Jg2J_qmZgu4Kwfc6_EedQreLtBB1OnEaLux2PswfqNtTkelqV63OXzd1JYZaV1FO5BPdYSympPc4UPMkdZYGVPpXs7HDUlsZ6Ul5VWlux9yOz2isX22q_L2fXrsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jotaQi5zkCg6swYMhhut7HhZu8gRSOgaEkI7bsaH08YJ-9MFOSkyufp0Mt7CfW36P82D9K0WDMeBo4bNIett-abzgJ5BNkDzcCw63aApXBxCpzHCNdikXGP6FdxaO26KK7E_W6VcdZp44Ohv8U8V7vIKpbBhDQM8I7g899upyJuxTt9-vFxVU02CwaUgB4l5cfGZo7wS1nxvcaeblvuxwQdYKNzoPD9qDg821BYGGG1sCnYYCoLNGe_DH7E9h0kwYMj4mkTr5_BILFGg-y371YS-AlKlWHYQEvcVjlXz3t8rxjvisfEm17CgeT0QTZY1Bi15pRHPhiGNNe4hKyslKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSCH7ONQb1SdLT4q-Sa32Eif6agmtQQJ1dFf65nrob6LfoNTVUoRl3adJjYWrun4cCXcxI_5SptMfHqeNFLr39w7p2PxWqPROWzByHU_mohQMr-yRnQf3u6pp9ZsMSaIu2C_XaL3WSU2l4ODYzSBoHvp-zPGlK8O2dJ2yq4pO3LHUp6R2rxIFQewMWpmZQTR9ixmHdsMXlFtB2hjVQXhrG9arL4Z8MyVl4ObPAKpqBcKjWxknGTD6Nt8tmb9Dods5OSNponIbqzXIGadSfEyfkMO5qM5wgGKrREDbKQP0Ea9uYzobFTbSvns4vWj3eOZAANv_fIrrBbT1pPV030QsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPakj3b-Tg87xe7yC42HhsvKF_ND3v0o3e2ccz2Ph2oXTlOhMSv6xtyczHT2NNEf1J_rGxWA_hVmxU8fWucGBypDLmL-is08-aCsOochFiYVVLU_w57dI4OgquJ2fLOLboRctrk34mj5suJm3urTLPTcnQasJih0ABmUfcb8w3wIZh3fxRKiqxNEqYXNpFy6iVLY05cJmZ3KYDhuvMOenXn6kRI4lEiSTlv1Ek8LC1-isrne8W-JI4oqZuJ8FmK_c8DhB9uWTNqM7khMMLyPCto0lp6RDQYyhRJkg6Mh286H6Ny0rw55aDA51j-3-XotooaDetBpw3GZvTdkeqn3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV1wKqAVqO2Drd_dPIHR3N5Gw64aqxrwYpy1e5FzG-G-aTdhnJl6WRC7v6q7XwLX8pX40ZdU068HP_3iXDMPe0PU4xCbLIHeNDiHJLZlB2hDvPixMp90frf77wLsP9pSYJKaq1WRwGberIu7eIwzhBlIqg5rfTsarpwMAKXptz5GRPQjPVIk_nbsedp9QZCghKSrwvD48jNV9j7YOVZ_tO52SynKzaBGDTu-vtIzxaPDKukpZwvW3FKChYNBUdVbdKtb5d08RjLAUUWCPnM07GT_ktrTmmp9MeUsAZaWdPWMdCFlQr2w_sh1FKfTQRDtmqYf5hPicl0JxyvPmyg-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2_M7SHNUcKobLfokoXNVlOXaXzcT6MJeqvXoBu-ZAcs0MhfEczBBZSA8qeFl30nhCdx--O7R_k1CGhd0KZJKZ801YdOJXTWNWIw3vw4toSC9nJe3nVkghoN5zfF5WoJP7R4f6FIfg8W2ooXOQtwPp_La9krCPMqRluKxwpsZzeJElYUSPXXTo-SxZIET54lfX-hvKtdoWymAPPsDP5ulYmCBOaYYn3uu_VvMH-CSzdM5cIjUNbh8MbefRL2Q3t0CJIpGMb08GZZY522LEoOXDcnfPkzzJBIBwfsogMNj3yUL5DqLStJ0mf8oiZhjazMT_b2rIFMc8XSYMFofQVCnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwvvZgBIOHvNf3rx2EOdmpnM3EW6BVIPtvy_1OTBRKizqdoHeNc-CGyWK4qLVGOd0y0QQCvSzweuJXA3aC1mg5q0KHwUVBUxhOMb_oV5J5YHgos9iyVFZT_Yj5SQu_HvrXj_kGJn_svaUwE4HlrxMlZerj7C2PSP4MHpmcnAtQHDcHIlPJR-o0_Z9essrSHdbdj4FlkyeXtPU5HH6XhmJtEzPHvV-t8pszddjVX-7RQ1ILW6nF6b5WJ_E6KxzbnYYuGOulAtFsgNUGW-5aQsln12j3R3vYZlBb2AhZJxhcgJxK_tvsBh1b4gZTj5uAYXlndz9UajIoMmPd93EmHjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXtem_foeknWNBfsjabTZmTn1CUBH6gndW2bwoJb9RyH6B6FJSbFbah6XHpDi6qB2a95H4oV0DxJFcbiwm8vuVIDed-a2Tcqbco1O4uDMtBnyP8emwu8zB17EPZSaq13cInckmYma6GU4_4NtiIKkJflNfZRqi4QfSInfNgLHKQU9seR_IHW_Bf6FtKMXvz_z7-yvWKLA4581FueVV36UMlr3EdxxuHRmHQW5kITvj59KPx4POiG5FVNcx6ioKk5k5UdTD7Rfcw26BHVIe7V_Jr1pZD04gK-LMkkwR-3JbsyifHYNebA6DvIl4X9eZ05kiDth-hU-utz40zVCcx8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqjv-7woCha_IS7n7BYZR6ivXgchFfTACvEsiegWUKI0s1w6bHY9pN2AC0D6YVBFUBxnScUCDIp1HF_rP-wbw4bX6pRoTtAfAUSRDh9zWruaO9f5S9OLPSIVcFgCOo29wq9-lZsUFkubhzW0AEcor2y5epRJc2Au88mY_CLCct9Ns7jf9_UtqDTrCxx2w0dx1qxKV32ZAV-6TDzeS8d1UgzlxwtAiDTLSUtIi15ts5fBTYx1y5f7YW0Q3Vb0fqGkPfKs5E9rkc7r72dSt4i_UvNvtFlLW0YIkkkyrEiLSK8FMfHoTKjdnPhUjfqtw3zseRpyBIcAkQ4IuOgekwq-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzYK7FjuQsr_YMGci4y-kkOmw2Tis19tdklrk_73TKaH1PAUC_bhSJnGaOqaV2ZMyshTSVwm2eDPztQUKRJPdL5wrmDO3xzf-yk2ZoYByTnyW1bhkEjDFaTEhsFYRCYAhOFxPcQ29t8yezLQiNwkR92bqxVr-nkD1V5nPb3jUpfYBgXpMKicoHhgJAqwESrp4xL9M4ajgVpmUCCWrhdChPqW2fskct70fX5tIytK_DF1E6qbT8gUc15Y08PwsUoJ6yaHv3uXnHgG1855-Q4MBn5cLzy5Kmx187GIMUwnReQJx5vS21JLP1jEhTo6cgcby58e6ZIMLRokfFZfj4a2Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpZxeSh04sQVXKQpHKNDe_wDSaggIqZz8Cmzh1gxDcWvZnqf8oGNlgtWUEwkV1qk6JGtJKdShjTliWZlkLOkzO0JXGompHBWhKyD-Loez0vTCMnLgbxneWeE9hkBHhXUG_LMZzIPMnyWQreddeeCCns4oU5Dal5B3642NZj5H1YnTMdoBU21Yo4Tlr0_PZuAwkipHItmj-peOAZ9rSanTm9scHPzrk7WPwnlPSGxtpjbLCWk9NT4OlU7BRMefcpYCgAREMf7uk7tlRCi_z1c6QE2xiRd_beJUt9XivvvjtPd_EOBIFpG84J-e5exKvg2FHT9eFAowzo6B1qR9khW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geh5EqvZilv8qF8S_LcEiZhfIsh8CvBQKR5WGpE5gxoxVcFMAJXawibZOm8gfEE9t0CM9uW2UDIV1yA1ctskoU8z1pvAdL79aY_4cm4p-QKUxKU9NHjBptU66zFFl3AatNqfYSR28DEvaxUmrP-hOgtDwx2a_MLYRMerYJJ54srTM4fe1OwWa5A97_L-YH6jeeDJ7IaOOkTu_OfznN2VshZz2RZl8dd8X9H9PktINx6bhLVklDBjcgH8ZIMPy4QJQp5P0ngZsXF3EK_k8zHCWthA39A4keLLEvCXiV3ezKXONegwbsfy-I_2WY7kHXQlt_qE9fXHGoP997RostGgDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3ViiDajNhEpWos4jwASKO_HgwTS7s0HSlnlD0zOgZ5uMwFSMBRksftRjofUrnxY9tS88inLQ1SylJgJGwrnAs26zwa1Iz1FyAGj-abbGioSZKkKQhTaAeJZAgl-mJhj3jggDaF73Xf0Jrasd6iaJerISJIDbBUCd1DwfbZgBo9cR0C99i2kW0nnWIvZh71D3xB9Lvi4Q1ZLTEUMDbXbP9vo-F9o7LpeV6DivKL6V3X_0rMmtr6CL4p8O60NjWgnpBOKct6tD4d52CbU9kBvX0BVq3X0izBp8pfAN8NacT34PhEYC5eHosNljk8awiZ91Hgy3xOj3rPTIActkymJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQkqtTopG1wNZdCo87FPg2U6pHt4T02JSXVA5eWdkc-kdhsMTqQBcuei6jbXOEP6dX0nGFnAsWyS3ZhN3edeGPYT5bgrIjIHMzzcmw4H0eVNVD1fOrvJxQajFFJw-rWzoF13Id4LIM2aw9451dnNm-fhc7s5FFBxmIhwHlSYvLqKFbB6Or1AcPKPZpDAkS62R9gsF1oaViAtgjQUCc9Dm4inBvKKsMaM7PleB3U9YKhtpd7M5oos4MMpXi45PABq_raeA8rmEJN3iM0_bQMpB1ko9DIosCCJdCC9f5_lrOosgMQRgck_oOF4PJdnt3p1gYIYyjvz0e4heUEV9KYM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nPCm2vHOV__xCaZD_5FUAyjMFQKwJn6_2IVHH_liVO_uXWZgOYHcqXNd2-oNO7BJceHZtccXKmrV1DhA6HeAGn5jqWhqz6Sh9NdZw-GNKtAhS5njQbuvtSJWF9t_GHKYshv3joLPExraZ4YFxUstdMoytzLAg2tMWjbrbXlqInHMgDgrS5PviYs95nbb5ZuUcvnoAISS4kM6-dJN_0K6CeydnDqhcLM992ruMYL6mVH3sTU4OsBOlZXetwjOQeUqlouNFZo2d-6KGl8B6uePPt_irE-8fKQCfOw67rX_mgAcxiitf1DIxP4GTfuRdJcDyHxlkQoUkQvGQcjir0TP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9KOa1Qkk-srLBw9-6R0dVqeS5PqMCcty9SqYzaDlXOedGlyilg_UhWNP40uQew0OSbqO0T3Gd0wmiCuJ8qYuYG37YfOXfYAsawweIlUUIFdPJBP20r_5Gsa3Od7pYOV3cDM22mIoVQKS-mcQJ5CEtyNVahmzc0rm63kisftA5TW1tvWIODhpQWxbLKsPVIFtm577ZhVQczth8y4A83FUohngnhXuQQ0Pxy-91E9IXQV2c30Ll6WJ2W-k8ULuiMaQPHxfG5IPXbmKYHEvBlka8Vgl8fketpGwo351XrFVXjU3JuliTJ2w9fT87P5w8ON9QBQ1999XRdLGwgCkvvDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fsyk8Qvp9Q5s4GOGf05TmOFoSCjoksg-O5DmSNfQJdHHN5IOqZodDUAFHhrRa0_C4uqKOQ7ygcd_UB-SrzV_erp-wi_hYodKwoj50TcMDInm0Bt-r1OsX2105DHQXbXBTAiWDxZHKsOLDQOOV5ic3C5ERaG0up-Un1X92g1pVq_m0FRN4Yl1lp2Lj1C4c70I1DV5HapOPaxBvAp9kjZ0CNrumu4TD3ur5mmVhNInfK7Hl4inLhKm-FCGJRYFJayIp9heJRgnrrZIvPJmlqzQQ07jjN3JZdM_7AG1q53aFDO3TOMaOHdksT_rMPBu4CPMjBJvw49-f5VsYooQPuhRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdjbuM3S8X6IcRBYzFoMDtAvFXjvuo-kmSnxjfm0_uPZjSiuDLRrhKHT1VpbTebMjnv55dt6hDuzouHeRr12VlczRXnw1Ck9XPMZ8O2DG0dzFUtYYoXEmlCTKpcfkcB0dtMIsvMgAo41zGy72Bg-s4ctYFvCt84lSZZRaw6hadOG1PvVGsduILNP9bU5S5c7HOEIst3-PTgaoEYaV18z_UfQDU_ZqSil6x5TI6XLxlpfbMs0Fj3naY5rW6rRpVk-HiXUtIpFZ5xEkdVUdPHIGtWNiGVVgCjhGV-yIXB2rK1pZSzze5EawmQVHBrLUAUPYskUwjTTumymXYsKm4X40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAqsjjHkCe_ieMAIxvPqiFTUzPXdEoisCvIUs4QAEwweiqX3fOIPNQsSD9YElMWeZaiXC4Ftla3eFH_-mYrpkmiYHtbCa8bIjkRPGFcB2Q9XeSJxJV-sJlxw9aVPWv29-Ot3avCw6pLPSs-1h7NA-NORezwFrXer20cq3DnZkvEexLq4J-rpwfVXYN923Ell46d45-BQbUmbDKyQuBM1hmoLQivcBjFUXHOLuQY0rqCwr9rqP8mQcCJusNzW4SO5Ggy9RZ23RM0s2Ef1r9ny8TGttEutx0hwmFPWGOTeTS5lbI6mSAJtdD03h9JwDRr5O7Xi6fjfPVtbJZac_eDEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LyWvWr5kFXZmUykrP3X568gYtLL-2ovWL8kckMXyacgyJ9PtqfjxlU0uQJEVhii2VxggiEgFReqBrp1674-5wBXEiA7MZymMkcDYQKXnJLfdJAmvmpodIBBeU7umO1VwCqz3dwrpLYQ6ZZxC9ekX8wrxKvSlJYg5yQ9BPesYR0UnT4M-sWAQ0cvl7rsPt63Xqqsd41tpr7G7vj1sfq4jx9VvMc6F2xa9X_M74hU6KV-hTJsXcnmt1A-iYVVHKnw-ywdScH_MQCI8II5NkcXnhxgstF4Iw-U5_ukUlsOINu-5nrYPCbirjEPVGdAp2HzSkC6OU7EgAXwZ8Zs4DShQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOXGRrNxUBkfhKv_4Rud1SoAlLpGcg3Xrtu6avvUbQyZZUGkaukIRQEEoeUHJh40SqBIvFdLM3CKsUU6-IzbObyIpbYPgeY9nRyFdi2bh8opRRWFvc8V8b-SRV8swrvFwdA0WCzgjGPubJP3gpuseu6uqulapTGFsKTvUz4haosNSaTz5j_gsulGvv3X7Q70E6PGer0rssp4N4UW1KuJwAeJoJYVlqMo5yJpIklSvRvadvCaG3LWsnUFWJ1GppjZDNxK6AgQazTtlUoHyOL4fLWusKT3keeufObBTJbyqVc4Rb3O1bkI9_ZD7tFEZ7-rm4K5shlTCQvXT8A3T5W7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlI-Zs34zRsgJDWbcbiF6dXgQKx5faCzO5MpN0XMaHlx3TVi2EDZQd9M25fhM4aLQ9hziN6ey5L7Kf2FVdT8E2u4ctuZt91AAzQm9nb0mLBJ1xnh13E3fDW0BcAr91YNIwkwlSGqV0lc_wOU48dN9a9EuHw6N_EL12GQN0XJ7zTLtprUM3GKnUGBNUxVgTCQK65vPHz1r4OFKV2ebS5Z4ak9SvnePgLW-62xwS_b6ZUNYxwpggJP3R5R4lshNUmhD5vznJnprlHGC-e5n7T2j5tWCfDn0f5WDYFBKNcLsNfS7pf7wAxDnLPGf2fpSBRvJUmr6gSZTqAMDqnBxRxLoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQZ41MGsRzN38NgkbttUgRPL6S8xX6-IvOTzLfUq_6OyMXg2J04ixHbmAABdVdot3O22fXt3dz7NDZGrpAjEhkdJHtKPUn4fJ4l1FrebU5VTaUwAkIDBUb9I75bYT_Ss-e1-WZYk2GHZvalTtccqhg1mHAGEKto4uIktCr7lWPawY7HCe5c-HayparECSqmC08xRZyblpzIwIM6pWHN0kSx5-MvI0iRGAxPv7cSMCdbkmpyjZKl2onhVD3Qs5GlPT3K7yIV-sxpykwKK3tA3JZPSV37MkcgNQuNWZrSZTRX0t6n89SpZtDB9DW9CwURkt5BkxMByAl8DNpM998STpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uetJHaWk6lyqsXjc3_X2C5Av6iax8tqAkIyihzjb88zR5tLJ_LOJ79MZ13ME5TQL66L42a9hQFfo1C4qD9jd-9K94dqgix7XRRJ4mGTxPi_GfeUeIa1P05d26W3thTJEGWjULrfOPjFZp9s9hpaQ3z83BzJTmv_tOddnHuAIE22wAjBOjxg9s6_ianjGiQmJP4jl-hhRGW3dr1v8k67lFSTNQy_R0mpVbFdX8fla2WnhpjWDTccbdUQbFi2kfBgvbyJSv4QIbMrnAllYvITSGCK4kOctzrPGQLNhCg-Y1Dg_dWoQAlfoC6xjp5nnO6xlZTWGDVQn_8sspuc4Cd3vHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rytkJ9g1oT9OBEzs1fW-w_XYuu7m_cihs8aRveH_8y42t7o5SHKXjRnrdvkqdjTD_QIL6mxFX0bkN1hkInognOzqS-G9yogDxWDY4Pv_l5BYqGwzmsZeyZf-Z74BD7gGOk545WPPcQ3wvfVmSW6GXkRXvUfmglYasqExjj_S0xHRyUIO7dI2KMilEeRmAPzNcsF74hPqbrSPoePOgUq8_J5X-ZKYOvxuRfi0D1KyM7uHPr6cWvpXpIY_piJEMw96G72nySLsk6g0gDi3um2pWg4RlxzrlY3LqN73hZBs1Yg7VuD_EdSJSts5GZXCb0yQCm9rDlZrOdYG8MGMgSCvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG7bkPQ_KhQcGFD17GNWpWlUV4njK9q1xc-OejoMc5pC9s27clRrtL1pruW0biEdCnG9_Cqj749eOzZaAulXQ8YVQOySA9jy3c9C7bFgdXvG56kq-h710deoAVUfKWTdaWbEVKh20Fdk1QV-_Z8F2HhVLFaEKd56utE51cuyhlJ3zPrquAfMfNMyiyRECsgeVcX5iCI_6MX8-LnryANHGxaNuoxGJv1z3dDcogWGCMwV-WB1gYchU7pn0VdNpqnnavx41MQh_sl-W1rngl614tRNXrCRs9-r05EzydbQaZPr9jBdur7A1WtyjI33C51RyCWqXw1i3TDG4QzLhnDROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKFHyWfSafe1nPUS1LdwMcukm2dSG67dnL4uQh9qWOnFvo0FBBjygbVyba0dhrYYDbGaHqtKzPSLxSLP6sj97T4WFehp4fr-HfMJ2rMg3tkAHPptFuw-SzGHHLDhUv4whPhXBovcsNq1HNven-5bCiEykZUmsoEbIqX3wclk0HgNz1LtkeDqowCNRDxklGIhgP08zbiZqzsh5vclxHwYTcJIXfAxO1WoqpigQZlpAU5nZSedIz0CHo-7O6sSrbByGheVh7uachdnHEZfa1BM4HD7w25scANH7JgcGx4fA42JD8ApKgWhMxm0ZemhlgE9Eetc5QTWzU-sJyu5BFMQ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvBsOLlcSh6KWkrHHZL1cqCNVsF_nvftJkl0J5sjH9cp4zYr9HaZesSAPp04KipDRVwxGXopRSrvBlD7-M4opGInXSAAvfCDC_TZBV5hAYQZreh9zJLrSOD8rnS1-4R2JwMdemSYrJAwZdUWclXPOHr11AmNYzaELOC_Df_3EhoxvwR3Lxf_jmBsQpW5ocdMInLzNQCEtbVBAkA7ZjQODkSjeSStYiU11SEr1dqz2i7TBYcnJivAbiOucrQocuFuJYoGDBDysYV0XxLJCCs0JdwO6udQuUELPK0OOcNxaN7Hwqn8tHGrSul2M5yNowgMvBZwq0_Uu6Sox4JYVLJ_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLUXvdOyaY8J5zVf_EIbGGlpyulf9BOtjH4uKPr-TtavUYVsaZdQSIfCRKnXuBMTzcKLHqDL7bkCVTw4zH-dKcRZ-X1N3A37rbSkcnDT7Z-XA3skXJy_y4cAijFxgNV-CNAcU7pgS4aEN1oVtT7UTJ6zeAJBAornx89D6w7vGn-5zsFlTYIH5OJO1behxErEsJZ_wzo8iIw3B4vroImrAxDgRJI2Iuol4lvPIc0hGsFUGm2GMHDVLWhjqJw3nG9Em8VeWOvYtQ7VmO1CQrM_S8noBpD3n7gyczlNfJW7yA7LrUBFEI9io0l4Q33GbCxrcVVLIrHEoYV6VUqOzf2AjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfFtkDxv4lhYCrYiPs4xa9vpD4WrL4ezl6MciCkW4A11oAYMiJpimQ66cDClN7olNTWjTiF2o4Gjp6SKktGcbYRJW5o916kwq8koLoxRDTzE7ei2DLjuFWmxKXNICpNWe6mfDKD3TIICHKNA_1sBTz8hT311EQ6fY5AOkNww8PQop7tkFcvkRARKT6CT4vUm3PxmoF5hB5HGmzVNTZxvrDaDY72Z8OvtpVW0-uhbvo3bXWsWWCLgQLYyY5pcdYikbnzTFrXkjpAKcW5c8NHl__LmXANOH6ApBOxX-_mSXIVlRZvgLlQNsdbtEaasiOsoG-6_3GvKwI8jIrfMy5ScfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFdfcHrLs6mj5RgnhwV0nPVTr0uquvJVQdXFVqd3Y8FYS32_UiY-s-1uVh9SuOO1SxC28GuikdDjNx0Qxev2_bkzsZBkL7hrzq9EbwCNNvTsgt_C8Nwrhvo6zxH8jyfdJF3fRw0_yZ_bAb5Y1h_b0DvfI4-3FrTXEBqZrs2gr95GwR8AbPzKycjlrKlo0TiIvrwsPB3fNRahaz96nMNJG8kh4z3V4ZOMSyA9fLftMW3SPkGSqEpKYEN3FzcQ2NZoB3Y4NQuIw3CknU8LjNp-ghmW9Oj74oUNv2KikkOxyWpJibKHSSoVSAjmKfMCeS4RD5tIeBkjCGV-JnrxDVLiuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFbmZVSg9M6mRcTqmfxoeF__7axNmEs9T4sIADl1UDyWmB8kCrCjzQPw17_7VbJa6kDZNxTwENd7t7LrygPh-bYbLvQyO_Dc3zcNCDEwUWsmYkEbK4G0iTC93oTlmbzs_NyCSr3K9QUyRIEnfZbgdsrOSZqhZKb-78kNuZK2-oVZVTKOioNT_WrteWIpdr3wxXiNcSk98nQUi0XbvcXJ0i3OT_6TUMUPkxaAwtXppPau9Okp8RQ924KDoR6rx6FgG5YDNgRM44-uXyjcxZPzWR2aDBuxR44apiTqTCwzgpw4pl_QgqIw0hwdYoVaFiLsUc0ZBUQku3P2dVKuWnA1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGShc5jW7PBQoKwInvzfNaU7whnBkWGEo5qw9Co90ycUQxZj_RQJOkCk5_ve7wTOX-RQWom3BYkBO-lBbzjnnemrhi_G1lW1iNXXV6LgaeQJDtOr_r55RVzjHhisVfURdkXigioA8LPtzExq1NsybmW1onSx37yPiINPl7n7O-JzupmX2f3bPh_xwToLZOnIaM9VPQTfSi34Xsb-gGOV2bU_I2kiLZZ2WmpqKsgH785GUl0l5x-5SN_ez_mF1TgqxcWjI9S4eAAOhiswWJCPMESbkFupErGQ4mxW8LE4pl5qTUasr1jBeLdsNQdjI9CoqHMUlXYc_2VJTM7lnRr2FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGYsbrW6OywQNcYiBU_1efuzHBVfFUo4BZZNOt9VxaTh0KupBReRcCLlgman4KBHW6JXvmBbKDnCM2lnjTkS5CiBa81yGT2gdtLzAILNPx3s9VBd0JB9SAvzQGa0mxhJW0BEQ95T_7cES7GmLtb1gQJhSozRNTudBlDOVYx8hup9V4tiCrgwJ7K64I7bIaccmLsqqJ9VZBjGsgAucIQIm36SAV1ER2a-VJrfYlFla4KslA-LbSEhhtB_MYvZpzk9bESRlR0Fv-nYEaK_Q1DnMK4JPcKgChPEzh3fI7SyD4dvWroiYRdNG85_rqw2tz2vaGbaazgCmN104txXg9xtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRuIWLpow54S776fQs5451uK82Ycsp1lMHgSciJ549euWI7_VBF54jc1rQ7FNICA25P5ofQZQxS88afMWiiPuteNkPXKMsFVhnVe3Hb-pFcqAzVAOa9JsAoolIz9Kaq1hsLZroiymQIQD-X0wqAOFSWS1liMSCtXK22AErv8t9djJSxBJxYInRF_HX3wABpj3lUG94QwSXSWUzpnAOntwmG4c7jG6v1L0s1kLrKYutZlYoEhDZhldlFREpNRASBh6ORShUoIHovBn7-8GO6RLKME7NCjsuIesg4cMTS-iZDLiWK8haFDdU7k75q0s855BuU-6lnfLpIdvAbeooFIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36o9wMSL2tBsFFCukXk5ZoZlpTtCY5gTRkIj8uQ5lLIuglYj9o0bS-SITZsyVYBshWmy6m38dLx983u7vHqAipvws6816Vv7dyS8SK2jMASEiJkkrudKWt76ba6MzGAY8GG9VNMz5lhEDYpDfvmvNeQUQ2tQNXiWBPMuZoQ4sIJ9OKJQBAqqRcI2AU8qJelFhJghnzQMPsLguyEWSnm9jC-NySoIU5mlvyamdCpnVt8niPOswACi0ntgZkJ2QPQNSSiiNcQ7zDgfR3CQhMt20upxkQa62Ak2V9pqe_xIOy8pvS2QT1Jp-q2QP827wNBvmSfbmF0p_F5ais4CnvmRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lo5BYe5rhce57tUakW5XLHVCIQOgvqMo8p0-q6ArY9dLvp1vomXwE3QPHTOrRCo4lH0DkAIViZCWsKq_MM0Q7VwE2FfAiTWLaT1pLCzp7xDB5jhOp3i72pxBCIq-iNcxAlNzWyq_5e6B8Ai589fla0d7TswhZdKdYDq-74tSnUgNiEvb0dgDnuul3RUnXNuC-g3SW2SmQisNS5RD4boS1UDp8VVj3WqHFvWvR_uP9-XwRPZeAIVrA-7lNTLWUrbzCSK0KpZScQ_bI4g2sMzuE9OqSWmRVFXv8LR1IrXMASDgj072TaS9dS1N7j4Zhi-oPCk08x96golYxoO2GiiD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=hTn5Sa0KSl40XEy_rnEnreWGEAZEtIahIDspXWUUxltiZl5hMmAhQxva7_9Har-AG-LpiDnT7AyRyMc7pWf2lxV60VNm0TdiNWko30sYbGehr_J3_6BAN72hG0a2tf7DZ0IEyqxPKMlEQCu2F2MrIJgRo63nu2zjptjuDXJ91fnldI112YDx-fwzXzzp2rwJ2ymo5E6uI2qrvJ22-QseExALcNwEDCjtuyhtDHEn_29ccEcH6MmYanrjFtFee5JH9sKHxx3_gqAI5DicsDyERi4BlCG9qE0jIZXY_vVjW7aPyDZIAhM-TcC2djE6ODG1nHnBl4RUBaxyti-TMt5z0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=hTn5Sa0KSl40XEy_rnEnreWGEAZEtIahIDspXWUUxltiZl5hMmAhQxva7_9Har-AG-LpiDnT7AyRyMc7pWf2lxV60VNm0TdiNWko30sYbGehr_J3_6BAN72hG0a2tf7DZ0IEyqxPKMlEQCu2F2MrIJgRo63nu2zjptjuDXJ91fnldI112YDx-fwzXzzp2rwJ2ymo5E6uI2qrvJ22-QseExALcNwEDCjtuyhtDHEn_29ccEcH6MmYanrjFtFee5JH9sKHxx3_gqAI5DicsDyERi4BlCG9qE0jIZXY_vVjW7aPyDZIAhM-TcC2djE6ODG1nHnBl4RUBaxyti-TMt5z0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHelnzW4WcUf1QbTro_xQIMm11SJ5myBT6JtDp1K5qpVfSvidAXPnIYdUYorS1FsfVdv2XUjleNpVzhPsbe3KkYieHzYt5bnoaP1p89od2mb6kcWFfwEFzLtlxurMJt42iYw9ZefZPEUjTX2qy9qmLV4mLLcfBY9MFccBb9YPdLWCZtcpPUBO1sLF-J7YRZ82cMCoXSvIC13Pzsmtb2oIB8GlEUnSLWIgIU8lpyMnrcxwz4MiWl9kOjdsXIEcKSILJZN2uYWDDNC1yF6aB3PVYwV4Na_HKF9xfPM1dvOQulTuxugz-ctVvcFlDA9PT5mKCU0pbVRVQuxSa7bKuleaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBhTv0sboaFOgl8c9KtcSL_a7VUlHm9jBlaEPzKeyWILw0bAoX3IqYrtU3v-ysa2lIJqdisyMlEMWNWoAidnqVH1IiQymUWvy1SEEz4SkbQxsdZyKNLv7gFhTXDXfWPYI20uDPPYU6rMY2sxcNbFU_7LnLkDxFsPuyjUA5MFYzjtY4lX6OD3K540E19-JOgkngQnVyVXSL63PCNasTub_3qf4HEQANw-FlzA17Nv_dqI0224RgvXDLPOICqLrvvHFaFb-sKh2rp6TA_M-OlM8XeR0EFEPHr587MCT59CEA08dYE3PvfAXAnP6daawAo3k5VtWP-WJx3yRP20FEKbsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU-VSWsF_OuqPqX0rFuzKs48iKT5RSRrp3KdRVfpx4Qy1V0Qcu7xzsUznLRmP2hpPYFe1oNqmP96S-vYxTFGIdXhrYRPma_fsdsFaYeGkq8-SJi84JXtkI1Ek88FkG4M36_YsInsGkrMWxRP9aBXj-HuHilwY-gWhFLsfM0_prgk57gyTBQ0pqX22fxBNVxRTmgY7Rseq-DTKeo22u2ySPHz7-vi5ni4LmLHpBvirWRnfSP_bwVdks3xzL3Be5Xf2SJg9uWfVbsMwUTXLZJ_CUISfS0t2ay1-vg-X7RxqwSCnx-Pb5D9nvoRLhl-SVfT40v-QPSZqb8fz0gR-8_HSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVPV11BXKOjMY0DI43rSRztoK25ECGTH0i5x_C8QfMgbr_o5UPsuGoVC_kpJku4I5vcTqNvhK1Jz6ToqOaTL_KbD_SQDYbXOP-xKoHHj_IntWS-zU94nYT7eKACE3l5Q6d9XkLzfmA5F2t7vQUMBRYBnuIc90uEYGTU1LBublYjwyIynxFkezyCydHNIcRV1FC-OotNWdJ8QrtMTa9_0yidlSEOso5_Vo788d9grImd1GMR_pj3Xk0dIZwA3Nvl5Y-Ehtox7tf5BOrp6YU4nFST8TUYKetvXg_o0F3cQyeYkwVln7_6VE-I6KhEYtQuUVwom3zRXhzd1do5wMMHvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUpVZNNOU_j1hfwnvsfk9jTYCSrryAReEk5sUfHDo_5bK-ytnIHqOG3UJ7k41Ft4ec92twbDOjmeCkbbXx8ONxlrNWDg4W9VMKGve0JTcV2GG7B2qXBtl-j7Jw6SuliFMabQRYSbPjUwFOeo14rSwLzX6NLM5aFq6OblR-79AtlOo6_OnH4EJDlErlTNgOBvTntpMHodVarhlNW6r-bZuVtWLJjnSNhgQoQzBBn8UrcJAJaf5_zmQjlVRH80vbBND0s5Mz5KY_v5SMnGa7xn7MYioeSTat7aH69W46LSU003OHhZeVJBbIFYJf7KQhVTWEJdzYZkonPyr2uE_OvwRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH9uOGtXnFBLRxf4o1ZbSrbpwFhr2vW1-cBClERMCXWYFr-lg28wqToTfr0v6YgVdeW5gACqBB5asM8PROwZQhuUWRZfEPt1RpOv9BA5hu2OdUYnoi0mVv0zjHiwSGNe69qK8PMMMhJYN7dymsf_BYnNZ-j83ZScHUOtW8Mt47g3vFmUs29skgpWT77RpE2c5VdHwOyXARIX6plxWBJdnaOYKPhYXOmeufL7RXNYQ2khegrBv_QAIoYNQhVHIHflT4gAiBLEcGu-YV6xBXgPMqNxF8sm56KvBSO6NbdVremoY_rFU-Tqph8Izu2tkBrBb7oXKlBN6_rKeumh6eUfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
