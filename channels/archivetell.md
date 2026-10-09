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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
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
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=P5ia0sIhzbe9Lwd-AMzKXxPD9IXLeglkacKa0t05agEinzyTyLlYk9FUplvtwyT27nGsTXT5-9gIe-DjkRHebot2saxt3skkf1kZHQG-3d_aARStN6hdtpIKzBJlUvhE9g-NSyqL1vEOrPK9Ml1LnjqZ06m06YCLA_Aq8ymQAa1RVPny-UurQ2Y9Adt0XoQaNut2TX0mDjDYC-OFfG84D6lVk91AUOgPF-r8xhUiomR3Azw3dnrs1VAAE0DhLkdWzEK3QlTolbRbj9VuhMU4JvXEYtw-yVQSuytWhkYJnFkyr9ICYaQK99rzAdyWj2FVGgL4qmmZju_cU0ppfJjG-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=P5ia0sIhzbe9Lwd-AMzKXxPD9IXLeglkacKa0t05agEinzyTyLlYk9FUplvtwyT27nGsTXT5-9gIe-DjkRHebot2saxt3skkf1kZHQG-3d_aARStN6hdtpIKzBJlUvhE9g-NSyqL1vEOrPK9Ml1LnjqZ06m06YCLA_Aq8ymQAa1RVPny-UurQ2Y9Adt0XoQaNut2TX0mDjDYC-OFfG84D6lVk91AUOgPF-r8xhUiomR3Azw3dnrs1VAAE0DhLkdWzEK3QlTolbRbj9VuhMU4JvXEYtw-yVQSuytWhkYJnFkyr9ICYaQK99rzAdyWj2FVGgL4qmmZju_cU0ppfJjG-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmBPewWrYwX3kWHeLb70QdfIazXE5JhLdk-6cUaAH2hdB0Q-ktpbTdE-W7BFyQKxXXIcRqoQNkz8-x_Po1RqVc2AhRPtyWt4lqZv0-6iz3UGODd7r8aGNXCBVBIvs06TRujW-FOh8zsiAmkQSF7lDnjQ7duu_bsdGPeKQc6zqN1xwLGonr2xiynMDfD_GdI85rwrkUDBfrsnSj4QtAiOrNkGT8uuEK9Ww2WxOTN3xJAGwjZXph2ZpENl0-rOv-pGlN8m5nht6trje83HE4pQmQoQ69mlT2fqJZW9La54RUYveY0aEVI8PdfQ9_RU9BlxXvwHgjOHHIBXfHl0-L22qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTRMXsdCGDj7aFuXUZKDOMm7hpnW2qS8tXsgryFD3PHCjdcXGZ2p3KyLf9II8Sj5xIFz_sJK_jQg5UBp301tbZsYxrgBtzz5h04jn55Rr79UHvLOZiXioSHYIlW-AxizbLy7dQpYB_gnH4WyxKdGokV_nB8KepSF1ydIQcDH1qM3axL5WxWCUncT3bRAmAXYTL8SJd71fA5l1ywFiJ3jSbnRTC2j_LjnocwAW-GkWdIYLJQkwxEUYbCUYq3PZILjLCxwHQCMGjTFcxrwBMNo2V_ET21Nq8H96jydtNydvQMamaDfBis_H_yUjp_LETygjTZrjlR2jg3nXlVDFvnfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIaS9kB4VkBpOieEEihBeV0puGlvyejS0qkds4YSNLQDJSAd-kjOsAKc9sk1c87IayGCex3JIGCR5papxr6Yr-hPExNahzAmlw7Yr1ZYGvDYaeikjTkSokoc0MHLd8qDsvk_kQd6ABzL55xqEQLflh-C-tKsCc1w_-BxFI7zQhM3VPdFDRTaCkn64nzMeWtCPW-sg4RiVjqe1I3gNVftppebYXWZ-agf-ystdeZeNucOhATnmD5Bqi_5032qTMJO5IhB8-gtsfUwb7oY_xPozZCxWSjbu1MIPt3cOjn7Y07HQvN0iERDhu1Wa2bqIjpIF16ky-oJ1lyvbqhtOQmwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwfLR_HYb7JMV7JpfmoVC7xJo1qfwgU_f02Tq_5hVxwsUzuwBHMyTx613djCNrBXfKUvfToC_PQ5fBOlQaGTCxxgPcHzCISJjS_rwLDTzgKRYwzdHFTQHgytO1uKzudbsQ6YTXsf5kSHVNo6s4TpuJz3wPOITa2lFswJuMZBwAjiJCgZ9QGI-6Vt50wpmsJg2_-GkeEJZk3MySujZ7ubQDI0Ft3KEhxxh3Cf8zMTtr2Vs6sW20Ck6P2XM0lMmN1EjCfV5JjapQtF8I1Hh9pW8vPNNniBMqqnSBegZN_FMZcXej_K6fJnupYVROonn5pCCceJi7Nj3-BGCj3T0rirpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYbmXSuIeRVCiS-qry_4mgKGtGIqkPiXo6QpBFghJmEYpZj_Yy_wTGO-8uxxWW-1G1mBkQXSYandVwanMZARN2fiPvkxqy7uxRJsywPFPJQZLagJ6--ZJGyaa5VZa5-Td_27AX0D2zovjnEadP9aHPxwKLiUVCrVNBRcyT1Bak38jYI-hyrBVvwQT6XE8Bl4awMGOe9dC7_UHp_s_FFdrNusYrGLSfP1T5aHFrZs-gJ0G4Ioi52rirujZq9RmqFeOlq5CilVLouB3tiP4pmUB98XtKPU5G8mIddYpqBeePOIowj-1FU-GYwT5YrGmr4MEjap7Z7ABnu9m5dbjQ0RQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFryrocf3Eg-IOW4BImFiJk0wrXiD9FZjA8r41g9stL5ZUNvunOLAo0H0d0L6VL7m6flslD68pQmnEuCg-w_joDtYLbaVQID6VuKBqXBjl_onekDpzj8_FalTddR4VQtYsaqVPBCGJfDW8dJv0oEviOnfPa4MVtfdo0h-3qJTMYckJtJJ05DoJg7BGYMgPybGYksR6tO-RwlCmPG04qa_qWjLdaxRTbIWQSZvR5rcbNysfBibxNPWF8hzUvh7MZkNzKcXog9PTJnyoeuVHz5hEl_-wUS0CtyeIbg-4PDWglITdSjwGijQ_MvKXkFNmOI4dLzX77Si0GEBjsgo0E5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-leYB9iGT7318w1Pjl5HgWElNbPSX7a53IFMUeSPp8aYzVFoSoJtHPNl5oP68B7Ba5suNjqvneKdMyBf4bsA3ioM1f3E7CGbmoR6RLzVCd0DlFBbcHkgK7fxhF4t5SeipYij8Cu6sov-3-sgEsnpWGna3-W6CkmK-N70ez_QCB_IGy_1jh-jfzL1FNyay1z_H7RsRu_OvMBcCpPbq96mRmB_PYHB6mnltzS3wXOjCj6JH6Uj_7xzFmeicB3X2pOd9hyvSltf4IKOXd29fD0e7ybzSDq_e_zXOlW8fCSqAcO5Wd3GTfTJA7bW7T_d7Rh9Ne8wcasCnoJ34FS1e4N2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeYm7e61HeyQNMSDPQd_k0qCRBCHSkdRpcnqecbC0ATWgKgLRGjymTzmjFQIsCa8OMUUX2HoBiRSlxh5oCL-G32FQS_6WRZI4WHTL_9NAUNhv_Sn6fwhbplWD7o-PKbM-P_x__QFw6iBfrFzNUnjd1bPS1t3ns2ZkqOVce-PwA2Hz29cvZpzHKogd6zHz6aq_CNiOLuD3B6JTIoCSlVEySLfjtKfSSjrsLFK_hhVzUoz9YzXxGDoImSCVZBX9yoB74VwQyN5hEADJR9jxyfgujnATDpdxMrNIZbdL9y7Pl8XAfNubp4JLM2syBn6cGm6cj98Q-q9itC1X3SDXqLKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smtHEdfKb2oh41R3qfZLWFlr0yBVHXD_r2It45pIpfa93tsdtsR_vPvxlhf1sBnlV6D4kKAIJrCdDzzzsXtJGMUWl7nzBZ_vRqwIRKyWPN6_NINUhw3vP7PPx6_BLXNraBiWkIpYXtiAALEar40OCeI9CdNC14cREZZp8dzMZ1NLRT44RflN9sQ9QClhMNECfy8WfG8wrZjzkt38HVuleya6XZQM61KkBqiBYluy3djOqbILTSCjOQoEusC3VPMnGSJ3hBewcpfiljDivm79gJCUDFS7qKyqW7-Vu9LkD2Fb_EzuV87YnmPjFokw_rpoOhHvcLc4-neuNLz0dv_5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsgIBGrrlfHWs9ZbBOm--Watu1jeO-NqNHuqeVb607k2QGfiA1ts-SnNJ1XLSFWQg6qUoLGPnLhKMv907HS2P-QvupShtFRAmRhUP8KZXbs46kIkdSernvAnTberhLz9-XQGmXUmPWz65lZ6YE9FUSI722pw602yKOPCX2F-2nBHw1RPq50F0vkWUKeTICxTHvOu-Nr35LKocaXKd1_FddADqVpgfYeQK_DLy66VbxyjABpb6xH63PoywKAT7jDX1LUyh5Ifr-AAIuZ_zyve8-NvpbGcZ7zyk0yumoAvvT5guseVh9e0tdmmrd-aiX-6uEv4ZrPyzTnupKFFP2-Ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7njPq2usrlnD_t57hJkRP7dwTHfU6qo_jdsQEOpOoAGDPlqzGGdkDYcE5WJOMdHeymHyeZFym_qXDvjWAUoS7g2wDJCFtC36kZi2a0mc1rjehzxdpmpz1XHzO3Dq7cGXWDDUcdxczbyvhw8NZeCvx9t7F87spALI1Fht9xByiZxksbLSa1XaMliqW_nMiX-Luxx01KNIsu6UxoayQGxowSvMoePTkWFJXemIwgnqJd55ogoUnlaB8H_GEOUhC8q8LOL8QAjZF10CB0h4felwGAS7Gt-Ko7BXfNf0i0PVFYXDNgK19DMsT6TxTti9SZ0Y-3bw01PUEd5m2CLiBDxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyMLZm0-CsLRkYeZ1e1BaJhuw_Wec19K3tpJI9AVhgl8q99kn71qaCY-x8aQk8VzQU2UbgitMUoCgEA8ngROVrb9FBLeIXR0u4POHogi9G50D9XQivHxN9IK6i_pc1e7_VO7kFvLVnyqdbA2iS8dQebESULjCe_2p6nciTKUTlNO2Auv9DzrC4Hirp1Kgp0XK6I_K11MDlI-LChW3v1sO73R63siuuCoNHUPbXRVEbUfU0ElDrA8qG8-ZukADT3r8_4QwUgr4HsbnTiHXJXz_veTY6meZirly8h_uv5vxcBZprgPVSHkhSqmD44YiwvAdKAblJA0F6NmqX9RJDHeXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuMNlW_lFwhkIjGlm6XKMHe2aTxMDBtTHPpebbsMEtcdWmKXdyNa3rJcEbZeXB07CLkciocugdphl3vC-rq1fAAqzY0r20weKE_Prr-XzA9j-zPw5KTurGbSbyNRTZ-HMvbj5tnWtnJ-d_5Y-uvd4Owhf82iRBMxAn4-8vIuQ8LcNvEzV1UQWqClV4rbfpBl1odXx0swTJt61BF6ZSYGuT23jiBLQ6XrHlYoabVDK2M0PYvttaHyAbBUumlS6kUyGQxwnhezf9Yh4VWEfTTj3MZySxofzknHfMlT6FOJVex0hQAk1T4m8b7rIkeWf9hUnmIDUBNCd1Jss-LG9Oig8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp997eWgEgi7OdYaxI3P5YCP30k8fAHMUHkZo47gGbkM8Und2tZwgOJH_xVxFSQVX4QoCIjk_geIGPsJFqYztNoL7s6zZZLHLsMVGJtOf_rCAJd89ka-m2fHtJ1_QVu_i82lqNSAnCvfMTVCdnj1C3CWoeleyb7SMeyTLlKuoF4KnWUrCg3E7DQGXoiIAX91xCTBtofe06PD64ISMcUHSzUlgET3pBdV96QSl5INUfLwmI70qkgTlQWq_z0ZgB2rG4j1CRkpy3p1omCzhpdEzVdWtGjFxKJKf74d1j8QfUPtaJbo5qjv4LIwsTO2_0aIKQv9Revy_3F-2vUD8aTxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a06dg644XVX13ZWWMRkDjd6LqDMyUWV1yWCRA_GSw4qMoO8CNW_lDZZRnxzTQc6G_ZfnH0_Ffk-h2bdbbBhP0rf-bP3mAvqf3sKo1he8TrAx98h65XIE94EamPuGGUe8euJ7XndfqNHJ0WGYyzz1njHqv0yhIr89Bw-04pjChmHmyCoQW-BTlpbCTgoyRBKmw8wMtz5D5QNjGqKOpbbctr86dtNBvd75FLOGNwgKDYXmwZFjb9vLO4Yeiwg7_6rklPPmx47INMwfz-OhY5mhs9YfAv-4DzoYpYInfRwDInqkOf_4___KqckUAoEfscUAVnpK54lmYLpm5X_8WKcK0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1ePdDC2rdWvKmg0sI6-Ojqypja9a65s4U_rBjhZMo-rEEC4dGR5QuM3oI2VeSs0JmkNeL0azrvDMCFmxqvebtvCQ0BIS5eJtWTonDocbLqNlLRQOTVT4Dzl7DiH2hAX2_dSqn5OJXyQPRE1bYUtl63d3x0Q4Sd5KRZmeVvaIcdpJ6F_EjcE0a-KRBiKOAz9nPUUFPxDhEArJuMW6i3gUx54ZNLX2eZl4pL2bI1plEUzj5YWATAl9uIB7xx9_fcYwQadJa8bknrF6ujOPvpiBYkGYBGS6OD7NCaVxyJd8DjwB1qJ6v__1pNmMk31UKq9EyaxpmT4cqGNsfhlkvYDfQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=s432-6EUNqHCD4c7R8xeaeuUyteS6Fi3wGodfjbffBM0u6XSxQ5M61GY8cYEP9VUJkv4YdOLHRj0uYBr-0fh1POjIVo4iFgksU-tKGfPXzAaje4eGwX3sa2ghZgiogJSleoFAs-lRX5AcrTQZT08s8-Cu0g-2wmxr3imGREhOwq3eNkb6wDOVUoOdpxn9xpwG7Gqapx5Vv8uy6e9pWqGeE1D6G-hObdoOYMAkcWHQ2kAl6YEdlQ3aD0nTx8q6XNxmVy_olz4y7178egQsZtmMs7-UcvLCuped7GeY_Cwqi6DqkRdb6h6UA_ecjaTIzmEpNXnxEXx2d3SVCyLFK2BxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=s432-6EUNqHCD4c7R8xeaeuUyteS6Fi3wGodfjbffBM0u6XSxQ5M61GY8cYEP9VUJkv4YdOLHRj0uYBr-0fh1POjIVo4iFgksU-tKGfPXzAaje4eGwX3sa2ghZgiogJSleoFAs-lRX5AcrTQZT08s8-Cu0g-2wmxr3imGREhOwq3eNkb6wDOVUoOdpxn9xpwG7Gqapx5Vv8uy6e9pWqGeE1D6G-hObdoOYMAkcWHQ2kAl6YEdlQ3aD0nTx8q6XNxmVy_olz4y7178egQsZtmMs7-UcvLCuped7GeY_Cwqi6DqkRdb6h6UA_ecjaTIzmEpNXnxEXx2d3SVCyLFK2BxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4giNRsbepuT6VdgNYiYoGZg5I9GYsextdY63ZsDfcbBJM32xkcVYSW2I1bsrIOfUZk5nn9R4GoW3wVEtnS8_qIV7J5Z5qCxvaRpf-Y0eSa1e6SItXtidRSVLCY5ratVmp_UGLK8AVEZr9o34dYJPTc9cJomS64ClFY-WYWopR9e3-SJJDuQJIzJT-WZSb9HkgC-O2-iFEFYu4AH01UqaJPfVYVPMrOk72KZoNDz__79lo0vU31-dYGJjymByE9Knlo_kzIftEqnhcQW_vq9XI5F8QtFUKZ2aignp5hDhNvB-1gxRXjsoPYpQAKBPF0c4Os-nYaereleG-ElWlHK_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/moEEWfzetQ9VGKB2_bET-1_KDsiwp03NfRsTbdAfVldbI2ZqSbd0SU73_jKz2J3WtDEARhbkiHkeEtH89eHLNWxygEevws085h42GdLdPGvJlO569Q9rf95QirfuEV40QMxGAYDVRBAfalxbN1p20jsimJA5HQ1mVBQpy0JsRCdtY1L12DyiYW1RJBDMTKIZDUb2jtlBkGCqnsyNmIecCZWF9xxQmHETIAcUSdxTm_Al8yYFHRIb-pr3MooI4krYjoLfu9wDeXd4nA4r_n2V6gvn19CECh7-Oc-zsU6yIIImopjJIKLd8QjPYc2rhf6kUU0aV8-xV261BtIB70qbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cfo5SVkxV1J8AG6pvOTEMoraEjuPbcqaaRr6Wd1GofLm_dKUzz9RR37JSVVhtaZ--rCF0JK8-GqqtPPoIJ8Oi6aQLFqZ5C76KuCNWmvfj89A-K1ewnqZq0YQzimnAt9PYLXxYNHWvKm5xcVX52qKvrJQL3ANPzHOdhMbg76i2DBfVzoZENSbDnqPN7WH0Qz5CJsjl8PrM7VuK61ZcLkB7Xsav6kfqUQ_qLjRVvDbyxmpqi_nD-kQ8vSMQVK1t2Y7SISPvfQMJIflmxvZ5sAYrxyQnAvhpDZ9fYd2EscIpFzjl-3Zh76GHSQ3KepxgjYWMIoovHCDOhh47qtqhjpuUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnJgpkYHgnyQxNpNU4dHs-W5sHtYoCwhd763CDlfu0lsldoayg2HoVV-GNVahg81xVwE8z68YXv6qb9SNgvhWoPUaSlYWiaAYcfaorZz8ygEqGySdM-o__YQZrvpRaNZWsMB4A-fy7KkZr2Tw6AQybgqy-h5SFRZCSgtjyfMqpJD0J9_UKlQhRIRhZg4XaYjUwTyENBLswUrkmAASLCfbc66qxLk8CAH5xFEnkVY8fR0ye97-ibaVloqIUN7113AM9sKerBGzj-pNqSebbE3n8_khaSVhVF2Hwo5eoWmQb9zXz4-nrecLrJCTaKp8HUEirPw8oc3pmo1eU4DryAJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6Id1vNaWe5jI5R0nOM5pPXX2lhqAbnx5YU3Vk-nINz32W1NEK5BlNjB3XAcuc9hsbBIg9oVnElQLvSv8nbJsAudbBZyMTEOSKiUszSYytOr9v3Ku5tjVh-NZlxrdhm-Vs1PLBGaw-JyQg-iLENeH56ig_K3xeui-wz5dR6JhH80UgtiLN8mA2nry278ewbn5NzdYB9fhWp4vzXh4QYRcOn4rG7Ux8zZzWTM8qWtVhbkXcB00I6VZ2_GAc0qw9EVOMAa-JafiA-Gb__JKadNuZBL_urj4TZ4Z89COKpdrh2m-QMRmZDQlv9U6TgkJC5WKcYwZ9KLe9dN_lBcKE5Xkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9q8WlIUrYyiKOldYhzRObyNNUBzYp6pFP2zgbRofTqh_vc0izceOEtYatESp_hGk7CuO2GRdSGbkp2YBSncK3ZI2hYuDEo4SKDWwcDuhTW_-64yWc9SDnb8zHfy25Vvw-ygTZUwWvLao_0L0ng29adzccz_mbvp4EWKVAiboiuA-yLlcf78uyfCG2_IbgpOdm3qIrflnMMZjnMLZgDhMWiI75_IgZfs9vR4f0yKKhf-nzrioC7Gsv8qe252KmevdoI9TdUo6U4cq4EJxClAMQ_EV5EmfDYLIZAyF9N0Ijfs2RO9U-FX6JS70RuAdo1BrmmFfoK9u9rvkSErVl2P-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DeVBIPVffTlPdWFjY7LlbKzRjXeOX-rtmbI1DNQJv0A_AeTwN4j3gVAhsVJkzl8Eghj9sk9euipH7ob6OjOhoaAwbCXP1BRM-8bQoNrgix1OfYnag1INaPcWTNJXqIpvplaCiQztmDQ_jojlpuXZ1kkWhHYxfpwSksCzJrguXfJQkv4gzXw96tmb9J2_MIhCyToMnbB-fJjMUY2tZrMg-NYBXT6gwRhdBLO3OBUAGNIPF4owRQu2u_y-gPK69dW8PJtqPkgFMgScY-VC3R9w2eZj_Gu0Qn7IsYXW8vcumsCU4glzu0VYcJpuCU0KeoYLsRmhZOqgSqOM2sc9OzjQ-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jd85NrU8xlijWtW6zX990vOj7DQGh1Xny5dB66eQB0qn84UbcCa9zYdF0VGykDSuwGHwHBkHKgLfgTJ2tQPKIkHEXChhzl7KYTvJ6DWDse6K23Q_hvPnRAlN4ZHaDxT5y_9Ly_3As_4AEICLjvXEiyHjHeM5cAMYTtBpVSlXuKCf6X4ftAAOUBZh2ne9NOdWc5ppzs3n6sSLbLqDXRNseEhV1H9Nn_Nr2PTp5f6SjYehkZaBB5y7GpZx56SxM4dAzQ3yC9ByKh3ttNlwoi9Y5lTpEBdlNNf_YJsm7v_UjikGY7ORQw-RyOxhkDc97p_JVcPhKphkDBJ3LRN8AFLGnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GA7IyuxufklAroihMxTV8ObUXbcBq2p6QxNOUYYE0K7PVQ4-LT0mTzOK130GoJVK_NnZp3KaVi7uhpLzZsf-mA20ebC3Hz0xolokJdd8W3SlGhal5tzM0G9t4ZKmRlbvnArzfLByp5lFsCvP7-a1ObkkeAZ4RJdpeIqIzr-EOvOZW0FEI5CHMRObzKBXFn1eocGuHYRaQTSViJEdkUD6LoKVI8Y4PL-LLrY59vgzUz4oUID1UoC9N_2TKsI0EureChfuX65O-6S209hdE9nnIK3-Vtmw8aP18g-P37RktTHZcii2JqZUm4fZ0Q0pzuvAlNFELNtxbcupeqEr7lEO6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJHoBfoRB7WICpWExTxXNJCZYJrpFXR1f6E_KnHyE1ZgK0vj34vHgw2Rm0bEFhhrFA_N1kVGQc-YXG5Lrwncwy_OFCkZFtSbtJsesavd8z7xIlGIzBeKEj3s-duOyytVE9VTGoH1WGIYsB9oIDm1XAVnDloqlGipe68c-5cenOTvjQ9nxCRwx2_MyTTaBVXPTYuFxLXlkTGmOWAx0KHGfh2mqJJnIR2ZptFpU5YfLcOInPwTQQ3XiwfiIigY2h82DcPqIFkgjLnsFayd41gRQYkwJlZi6qR6fsSBwBVubmgrOR9lqrOWKP-ky9EdGLTi7u18UirAXVQ-Y_Y9mHYSEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtZgtiIMq2CPGVFngEa46RIbRhzD5A4wAJGTvHENWt6a4hidd51FTwoqIvayOxN1P9mIdTPHv1P-gyON2vzeChhpdaEGcdKZ9S6APIIHdS5eIc9kOm1Ry-j8wtqrwgDDLJiiICdxo7crewYuDkuHWa7c1aV26vpFxQNN3KNaLCyKRhufcvkqZxzssZ5O6jNAhQCAW1y5sYlRvrNjD3uqTGG9a0x5fp7Z58m8sERXx_Q8RLh6J9b3ZcttWMfWv_ATZuz3GJZZ634rxmmvegiwmy3tDOjH1zNsbzXVppNTy1jIe78incCD5jtFsHkYS-15AGwLUSf7GbXWVqt3OV6LOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhOpHDBATGo93DiLr3Pd3khjKBoWZJtN1Cu9JYWAwcC6uNdZmm85EiS8_LNUoUwjxFl1O0Sc9hFuSEDmyZ3_xtB55M2Uv621lLLGe_Q42uLnj_TJygCFdQTei_H0GQRQI9DfEype2udbZlFAasFgn7Llf-NkY6tXm2_nLbNkeHWEuujePY5-YVz7JI3Hezy0ycR44N35k_cHQZNZUEeueg8U03KC884eN-xvWqjzJSpYymt5HtrqNeIRaV5txrhZCz79f4PR5fXw1_H1w6iBkVsCyfzzbZbPYWKJ4sAw9acnldkqxBC5F1Xvf4LH7xY-73rwg3qCBjUGGzLgvjTgJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDSaK038Oh9gYRXZNasR8d4Fn7OyO0XgrUJkbjJbajKhlup2FSebNa57H9zl7BuWaN4tU10h09noOqyKkuCIbqAtHRtrx90S7fx2cRCfhqcH9n5Q_QcwY8SYe1eA5EFtV_xpfjFqe-Y3ufCvHFrUa_30aBOZk7Qqo9QPftwZLYk0IA6tOMdiwTOjrYmHe4AfP2yyNupLjUizQaMqPG2wqZTgQzE2fdCd71oCxKDRP1OJmAksS_0gjng4w3Vdys0rTNCLYA_pbYuPgv98k2GM_k3Vp5aG3PJB7ReQf7McaE3ER5w73760V4hRn3m5mTOuGmziNN-dF53MH-FLWcoiQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DfkO3k_FeshYf77mevIaTtvJUAmeVCi52nEIW5fH4LjyNMh44Ml43Pu6hZRAb_Lk1IW9i_w0aOIU9HD6tvNVDxXbLR0d98lEk8zJuLQ7kdCBckYLRM-J2oG_x9EOW2s8Y5E7bb47BCsk9G1z0VW8JcTyMySkTxD0zTd-UA-txeCn7JLsAai_ehJvI2PB0lgiwaa71A0mt5XyoAxJqfibCbsAsuAyU244z0lXzvnooAtdHutN-xsFYQlmiOsd9YSP7Az6hnPFVottimDOBJGh7xrE5JhvrXGmM6hJjb-FT1i0Q2Wm36WkgNqEo6TDIIABPydVKyPPbqlfNw6pdVD4Nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3vBMJMs9qWkM5yCYUkDg83H-YkWqyNWM9xgmQElVEHxBsl7HnOKprPwYQyXjib4-ZC7ZHBFUdEU5WBHmIdQc_yUlH_4HJXW7SnxcI6sC3xUyp59jxICC7lbnArrHahNv_d6u5fUWOzTMw5b4yyy_tHkfPtiWsOo_smnkRfsBIKldhizmveYACwH_5MLQPMEKb8BWMDcQppMpXVM6GH8VKNTOd3GPag_77fytga7dDQ3uuybwotgxVn9YIMX7ujByjEVQgARr5iHC78CqJYfCfprqnvstXS-_Pgg0LI9xch_yHpUrdOGUXVpOAwuNr1lSZ-3eZ6p33px1NfF__R_DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrI0ZFH4fUyllLKFglrT7PsPxU0dhqoPv5ywbLVoaHeSW5qjD1cviKXMcGV5Q9k0JKNVE3PPxRE-BIpoy8GXRruRfSK7spBeRZN9pT0JFErTtF3AZ16tdpoVdPtnSwlzm2emU1OQsXR2o7v8yyFOjtU53i4YJsyu4WdvnVNP-ESU6cXjwsxl2DqjAazA6M2oPi_h6uJEj7ai3iGY1BkihH1KoJ2CGqFUixWXHcgaFxzqK0qSQ7BqvUNlvtw4TKEmIT0kZ2Dm0aH5z4zQL9x7pJxfKIo_4EO6KrrVNwYlDyJnatMoetxtuMWxJ28li0RYTJ3BQ0qg48e_qdae1of-ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaJYQV1HOPwj-1QqNhmY-DI_0eNv_z63Wc2ZgpJDiFQJ5cTXWPoKwgirkVnknEB5FdI-wbgt4nB1jnpuBrTtxaSS0__GKkgppUv5lIpUkQ9W34oDIY9slEhRUwciWcjOfibhnx7IYw31uvf8SnB0VkgjuqWQlljK1t2jVmZssREtnVdMWcXj0it0isUiKu00Q6zeCUjT4mLkGOhGDygrATO55dgoU59yaO98io4uLv9MCoahV1CIz5H1URAQDxwy7hmwe6y49vOCi6PGQcWYIgKxVdEQ99B8SoPD20rI-f84nKpHQNaE9emmsE6h-xnja8kfFySzLxgboGFny6dPtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvlwRQVQ-Yvb-7a5dZ2nAF6MLRf_forONzmRE-4SjXZa1AjYOU4A9zFZiyn-wUfdplO6p_N2uqB3E7bfLsEP9GTFCpql9Z1kXb099LQQXzlGDlb0oP2_WT2Mp1Kexb5cFrLyrd98dw8Bz5wok1GBiDSzK7S7VUa1FWJx8Et5QlkarSxbtPxdJEqrxEOgAYySN7NpvO1QNfENMqUrED3y4FGZkD3yFZDjSp1g_KhEIocyITHX6RcbRLek92RH0wiOPf1U46guZW1VMHRBgdKGKplgXgCSEaAkCNLiw7U3sSSnohFHVx5-XrU-EwWbeYPoxv_EkcuuJDKmTaGARkFb4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU-D4NZ5xRbPal9a0nlBSCg0i4tjTfsc3B1X11PVRGMPLUdwOH-ppipvpfuamDCNrVVtiqcwurwm2VCwceOAY-1o_sMicJNQxQoS5tJQzwSwmAphOBLqrWbyimdRKfk0fjZBxWyFLHWkdn4pGgsskmFx26aYNlSBSiIA8Bm4JSQIsCy3se6Qr_y6zNWEhg9KbbdsL-lJ7pD98toqCuu9szQGk0s4rkOXOsHOMjDkODeAg95l6-HTTOOH83opgzPV7Jq67176C5AmW6g5Wm_z0MR-JTP-ym3K8qYD54VVsQuPanbG-YmLleZEdovDK_O03_wA-B8MmKGZkW_qG14jxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vtkpxDqOojvDqAnkuqMQvsbU62eXksSKss8PcM1qf6DyvTmdDbxIvI7-wvG3L6xnCcJys9N7Yw2xP0Hhc5kxu53NdtlPtKuMcB6FEXLwmnUjE6HgJ8eh36yKXgL96eh2ORjePFSCn0cKKtfx50I6GhipVgjErznPn78kpYyyrOOXuYdq846ePyvp78JbLVM0CLrgeqM9Kyh5D9wJ32WJPnIKeaftfHC3A-OF7HoEqJn7oBWNki5afEbQAu-n-ZbDRW-y2yUrvFF7Y0ME3XniMscz6F9iETJVSNXrNmHu-AtpMfMVv8zsrKI_dBsW0_fz-hp8T1yEDV08vqrpbUeKQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qhcqGNyfjoIy4yjacPTMCl8oux1mkaFUYQXIVnGssgk9ZkOx9zP-lNSVW84L5xv0pD_ZsoqDh3GNw-kwB0lLtM9QDY8CUZIe-EMdOZ80Tng-5yUsZT2C79ZAppBN7OfOPQGEPNbpvVNTGEYRBccmCOkagOFZupdJ0N6Mx81Cb94CeMBdg_CzucH76UbomzAWZ4eH7knIXlhJkkT1DlfynpmZGv92CmL9OVrA3seoUK7OHSJNj11SIGxC9ueXuJHh-icIcDd8M0i023RMaib8c50nkjUxKPH3pfzUtTGUNqJQKCXiTHkdlDN8QcWl4eRe_urPlKvsovapC4zmfN0ouQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWFKCy3HbB17fru_ApXPOEUdY1k3X4az51BOlF1EqnwchSMZiGG37TrdVPSL4PkyP654E_oSWyWmPu_i6x_b2X1mya9EjUWmpGVyClyU6DNZtwQbD8qfxFqv--mG_DWW5dnxtjXzaPqeQHrTW-Hx6m_e43Fz8wQOp0JB9OQHjHnhlfgLfj5L5sQUuEgHv9wyySwoj9Qb0wsG4g8do-Rx0oZWUy-2zQk-IgMD2Giyn08y9WQEfh1rPOQe2FQD8smpaIIR7JFzK5x-66j7_lhXWEKDmG0MGToEA3XlP0_NynwR2jza8n1LQMHUFt6_CX9no93Jjoa5KwBkWvtnCzuWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAhpJArJpLeOGFN3FCNSxyI76xgTUDaTiPSqL0lv1YLv6n6Ozbi5v3BfxsnnWiU4WVNa0AneLve6bsS0X-xuk7mQsuml8yLXSwnx2kDB7bouHRkuaK7C_yL0Pv7hvbNTCaY9v5ICCrzHwQcqbcEuTvDeoIbkww1aw0B70jt68XC2dTlpFA8EDB3sGII1DE1njE71wXCHwu9aoNC0wCgs57Kx_gUH-wWVWZo757Av2-v5D4BSHiHSr8HTe-Yf-JGSZD4J2poFbf2sdtbbJlEKUMTXPE-BR55lDcnVdOe3NTAM0cBanhKRTzpG_folT1D_Xvd5vfeTD32eGH0s6NKW2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYSl1hjmIrWRme8FUKu01jbOqme0E9Jvtqh6mySgiLq_YMhImrRAYIG8O8WsWh51s3eLGNBKDxrfqWXXE_MdM-9tFXVY9pOmSO7Q3Li-SMZvq2s2roge7owb4r_nSdg_QLokYWVzEqvcZ-_5b9ASR0c9l2QoQO5HTdrZYRa0InqZ9crgBxCUUIRlyVIsFkKyDaqZaVqXb3qhfpAgl-gBx5tyqQz4MaL1DbEaJvOF7E3J-uD9AI9J9NtLmblSMASgS3TF8VKoARuOhaxrfyXW2pOwgbcisNv-28dXiapDiHgqYYiiAYrVe6qyJeKMoIPQAwu5GuDZjESv2Qu9u-eyvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX7eisu1trOQ0vPoW0whkhHE8Benassa7v2TBT8X4gc9rYiVd7wtsJGf3-djBlCjhtV-JyyBCUUJ9npqOOPGTLsKCzjipR9K1VsLHMzADr9AcI2uvY06_aY_ZXr6ZOT6peZNd8jPUM6wHBtqibq7i5nKNlhCwlOIxoDq_HzPh9e-qdSlv_KNFCCmCpC1aqpE2hRXcq83BJ4Tk4F9tVUv_YIxK6Am-NZjKOepGSUWOvEK21YFN2bZGU9YDu2RvSS9LgTmc7Df-GSDSde0SUnxAoUj4aveFe02V3tPFNTPBuEL8uDYf9EFslUtN8CZu2W7unrCB40vT9hi7JPc7brLhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuVQGxFkW-rU8KdF-mv6U1YO66GL-oWLqpv6UdIipQcU43YtSD8FxdhydFCzAy09GwsrEyRxPHWdBt4Qk3ZiBiYJEpGE0qesqQ-cQSjdWlUJVnBgM5k_Kz4cgTajnFH5lGWPbMUKCEAwJycNLlrkjNcaPpVLHrmMkI4Nj2e4B6VewTbb1doveo7jjI-A_b1fbcY5Mgw1JhkDpLhYLG0OSe97hSHtxPv3tibISq8af0OOZb0vtQO-9-FMJOWiqmWJKiw6qA6aq0cJpyMhGPO0SE1i1nvwjEF5mPPfNdVFOD4YTmVwRO0CjlnOCcnkydHu1B-DdHSZp-TWv1r1QH1WhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRnorCRFBNQMIOy4TiUQBFZUlGy1f9T0T44NsUzFjq98vnzR_k32EHakibXs6n1wAPT2Y63pKK9LqocKsHk0xbg_PP14VNRye0T0zjrRlnEsMM82EIybPa61_TKytoZfiJaLouIk2BOTksD8Y25UEzkUKjthxWn8cr0ywsMrtRWadHEuguIecmNriQLBcR5X_mu8KLiWu8V2OIzxgqyWCdMJjWuJ8L1pinB0u6v-K9M727c1Or3WUR6bQIS-DWum_gfBwLnNGtsMQxsKsQkqmGhp3lvscT2JIaX01W-dx6iiqdheyzh-mklfzdWNPpSkrTdfAN6bt4arleYXIQXbyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEhkC-wbRtxitNLhiI81FWMWf29TaJEAhAwX35ddeQZv74uMIQS-fH0JlGseYrrJNhGJQzQ7VYkNsB-igdpOuybciXmdZmoETJq08WSUxpoAP2vkU7D79u6QW2oipi7nQWwgykl4ETNq_hSBJhaQEW6mD_pj3vDvwZhfKVNcsZC1CS3TbGuy1WzuIILkAhON4OXd8iw28JAbAE87s7_b8NcFZY8tEMej_lvklI-27QLU4a-XyNoYjr4WzA-pyQFCJmi5MnoeXxvJ-dgXMB6W3fhl7rVp8fVtdUWjRfDQKstHcg3Qr_XxMOhWbrH0YJgR5A6yL0cMtUszpblklblb8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikUdaQq_XgxW-U2J-1EiCJtXwPI02NZ9xddlwvFgFlLFACWzd9VOMJha5IQj1BnKFLB9oMC6MRWI4hxek3bkR-NyyB6M3TQMBzxLSq9-20hSCAuBESCMUuvuUqF8zw4QtKv4bscEJ4YlEltXUdIe41alkTG03QSRD4R4kZ_ja0z8zN3Mc4geA5XodWSKphZN65uhTrpu9Qa254PExMjY7xkZuF_6OdHxGa8-ciG2i92eAJS9t9_vfWvFJXWb7gonGmgMvXGcQ42BiStb875BqeJLOvLh-6B4FOJ39Yun9yFtYh5xbQfbT3eeJadMlOyTPzWB8PXi7lhRcseCDzhQZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de34XisKJCpIi-xftfWhuHvH6yub1ULyLPfOE3ILl70e0_hP3UnQdrYDyUTxtgi5MxT6_o2SVTulUH7OuNDgxUig5J8DVueXeB54vkz8araqkAbJ_OBMw8fzmg9KDzQck2eyBRIAM7L1zJoDCjqcwbAdYt5oaylPfqrsez2XjeUvmw1JLQYZ6yK8gbaqBPrgXOrh1TQK7KgsfAeJpUjSmk1MjFEUXVtY6JXDJ25VxK2pzmAQUMdLlGtFUyNYHJElzEiumAe7Gr2IIUCwqhNaWzMn6jdDnSbXjl1KT_BzlWERK2aZHtDnEeDBYOwHeUK9X3OginDrTeaJMSxcgekaBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIYjGWNnHwbLlBn8mEtNtoquPOR9GkWvPJoAWIqrm6lVcqTZ5k4fWJ4FdNbuUr0qqha3-f4u-bhXWBM9S9ii5ZZWHMjyuJ2eiX4KL1KelgxPIO1LfUEnvQHHsw9foiZKKSghJeuK1hgm3Led2LvUtbgs4JpQHMbfx8spYsAWg08OANe-jMinlPjyCXF1UR6XQoTiJKCNhuNw1ALOFS_aX6sj1Xup79Mkwmbi-mCKzSCBfeuuFW8wDxEh-0Fo2Hf9tneD_X4E-li42Pr3E_SdkdN1EGEvEdeeRd_pPup_gHJRau57jVj11jr6DaKRrcVllksEufpfsZsm9XapHR1jIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pL-yNEGVJZQJeLGBJcrHtxPXnfFngUFf4rTchaHTk9pKnsIpkGYJ0VPxhm4VULZQ3RjOo4xJpycelTAdyyMgU8isGuAbtbDCCBtkoICkLwOA8Rq0oktQ-hWmggrzerTzAPqSd_yKHH9W0aMJJIFQcubsqS1T2Oyhnciwuy9s2yXJVBQxAs3Ug6aWeVW9kdNuQF0g5Qe2jRer0t2idlYqWV9jHifoXgFmrH-9w-KhupTw744C1Tg0P6bTWQyhRCM-MfYSFvYVR2Tbh_l4Bqvm7R8i0cL6rqd_b6zKz1RaoLg5u63FJK7PprlrZPS0kV-p9wy9vhpRofKh4p89Q742kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ngM17XF1HerIhGiYFrTypcZ-1X4XvyUJxtt6XL1VRUcjTbf7jTC3iKGQUQCVAMXGF2hO8z12MyLTJioaQv-Dux_ogl8adoWYQ66Bt7Z9jTozHrhyM9UapPDYahhPRYkw5IUS6NW_V9zfN2xMf1X4KxbXxjsWEXdfMe4907QBeUsGwM_zh502ddMKz2oxbuBxmi0gsdxGqW3KxmfhXrAPbZIVF8HOJ0vhbhc_AHQo2V-lrySgB83GUwAgYEzJVx8z9pCu2l8b_5vL4WZKry9jWQWdX_4Dy_-p497Sx4y-b6PQSdPm_8CbNTgGBXS1jh4L4Yd1hZQxfVjZdMQbJCgz0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0o97MxIS6eGDN51C9xviURxSpn8jjxsxLH2Mzzc5Ok4HBr8Fycycm8YElj_cOJd2Y5-qHGz9Pi9RiYvxw7JyHr-sQqMHyLN7N8xf6txgX3FcievWKi06329TnwSWNRy7LFI9rUGMdcV3hfzroisvj8mzqcH7IRyOGN4SoD1c_fhOPhAX_sTUO_b00awlNqZ8OCJrBl57w7so3EIdp5DfBWyQ3pvZfepCK1-i6U6E0lHTGxvtc0SrJccw6IjJvWBLfGfBjGfQFL4BTDTCe3AmZg-xvAyE24gU25W6uSZp1ojAB1TW3U8198f7LODbkZnWGHrhan3mfnkjXZVuUoKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utcBwL1xL-qXA-HXIOKX5qDmRZ7EDoU81md5aj6xyGtXNZsha5TGXng6K9N5W7zIW_PmVIUacqubJASWVPa87xZyKEk1pqDkWh9P4gW1lxgCi2NiT6M93ug6YPPK5NPWRt89FzwhiHgihMvvUzl7OYhL9jV75HfvjAIUFIDpUkH6vSKg39h5InLFjiEFyufOLbxlUlFLX1wNGz8zjohpNHaMlQ2yKXwDzWTf_oqoRLfACONYIKTVQlVJPXrGFKGwmOG8FiF08nNjGXquhuPMHgsD1BL3Hi84HY5-UsilCyAL4hGOnXksCJNwVUEO9IxMzffOQHvkJ5k6CG3cHV7KSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qy1zzFve20Y5hiPIcxJPcaf6BgSrOh19WcG34gjZCxySM_uJ6du3hzWgq6vtPHuq0yY1AenYk2Eg1E7cK_OUCb1mg19ZASzKD0Gpov342TIG2mO6Pd5zNg8ShHuGBozmIk3UxR5JeAFezNu-5A8pZv12_0bVSB6lbWKTbS94zWSnMMSHmcLThIReFq8gyrLvqLPq6AITrD6nRZAKCQ-KwAI2AMk4oPJkKcUAhR3DXiQCFhBffv9ERlIpJhpowgKUD0Ti40o0k6QtCEi79RXr-ubkvS2JPxK_Z2qhh4p8w48iGx1M5_o9rHAzuAvpOK-vYnYpG15yBPOH1oWSxTPcAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxKG_sEhtNpw9wU1roVejyWhTeXw8iHhGugPD39ri8z4axqQl24nWJxPzBk-lQY1xyF38br-LyMgW-1g7K5vgBKa5j1dMOTweR41PGV02_6lZTRxQue69y6TyI6o-P9J-kZmEDPAcjNfDlImP2ZGhuVRlC5P4PXrFOGJKK03xWEO64BGilFWUX7P_fzPx4K4KcHdBu916L9I1qeBhZsI2d9jWmcwKcNiNzclxqvAW9hYcrLD6ja8XUVBMp14ykyq8c71Y6db39FKxXBxk4_JHu3dtHMkBa6IXCCt7Xu4fmjRWZvvEVMcpEPPO95wGrSPaxrHmV133qwUZvc3FjNj7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxWcogomQmjxpzz6_rAgw6h07WJS-t7vnuR25lHCxt8uYrp73TMpvxhdIlE4YRiabIxWZRY0kQqGFzaAmPjMqP2JMkHN69FgIoI_leYrC8jUghXqlqRzuoB3gIggZ9pHr3fVdRvsr1Ol6mP7JiTp0DEOtkcM1dOiSAe-hzCNrpvdXmJOdkJ37ekYnSxzSmkTuQf0Qvyp9hNJ6-WNo8fZHsuTmbtk8Edg8VCbLVCnZUWRQBTF3UOoTeYCCrQbeGHT57sAwk9F4rZhlN2J-PrqlMv0udgTtqsi2RDKk7DMNkDg5Qru68tLS4rFsFbW-Xk2Z8Nk8dLPIUZCqu7zRIcR-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtR9JH6UfElYo1wpoth3d6HwxNIE7jUc7eBC2dlTxw7vMaPi9o9dodfitTrh7l4AXZF6Btwff-Y6EvCe3wC0L7i4ec-0Vvffhw1h1xEVzaRuL6v2qzai3BNLtJQXq_QJw76p7rivPKJCJKFa5dRVx-wqXkbFLnPXQc9myxihW0i6IkQvDRWxoxlvwniRdB5i_q1gUpFxen_1THaMMKAQVwUMt732oUG5cc9VbYssZvXpD4mYUkj3kBBZ-B20o_4SiiyAMXWJvEcJ7LNtEOrJFm1aYmHbXvJbq1wBkWbwC3VchTXUlGB2PiCig8DdeNkOUxgpdyo_0gSeBEVn89kzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gv8ctBvtNkloBXqOTdGmew2xinU27UONMvq5y6M2gwl1ijH_0gVXk1_qRlelYDQNwt6knup-Gr8y33H8t9rbWOoI47Fg8-LKpIiaz5RqyFWo1cPaBnAhH6ICJS9NfiLYu9FyBxknUdz7fZ3wqhaXJisImWSH9Zev2sn5bx2iw0DXrUetSQWfj6Y8mmDq6bXBd7n6VXN-iXrxGt0bFPT7jMCQezJc-8BIqWmC-7Tak37s_ULzNGA9vqzqlF_wpiJnhdNTNewEJIzpvIfQkHEPUWRfvXp7eIZleivme07FBohIBelijO85u5pHuqEecjwroBsdAZXDVmgjp0zjjETX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FohfNoxNKntHa9R2hjQqHzryZ1cGrvS5PfIRm3nv3wkqQBini77N4-q8a_gTHAZtIwtNpNWn7JPoT31qCT0u_jOU5zrKoLiaNgbtp7ra8ZX_whygEo56Hl55LJbjhSf-6DIQTVi0DdTYhRraHrJGa3Yqm6gA3iPO_CMVeoncwnt3zNtpj1P1LM5lTaUclnr1QNIhGQT4yubdY-nKluLTrUdWw_VigM31ubgRMSRBitXcEZe2wRGok7vxvOmxURSef4cJUbvEVnxnx4Zd_b3OYuKCz6yJRTd-QRkaWDrfs1NT50sKV_GZiAjvTXrs_UNHwGPMe8Ms_OlJM1d8bFifOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tue2WDnLr9AuJVL0fF_LdgSNPC7TVH6sALsXCiCkgP1VRTw-1VZD8beQkBH0oZutQIZv5xa5sPYELEdPrmnHBIqsUuYl85v8tnm39VNZQv07ZgI6TgvqtQpZDcwxliER9GEUWdE--ZdQdEKq3CY8oO8pwkAFM7M0-G973Ld8Mtz7wifIOg0KXaBkYFzYKiU-eVltfFPRLzi6cdcIhAN4fn7nB9_QJBVa8Yt7zx7QJEgDybwxIvhEKoqbPEzq_c7Wjro5Y3alS-sSMnvshrNSuii3oflI8hlyi9OvQBp0zno26uhxKIYz71FaByTP5yhR9BD6o51CP-BDlKxduXHISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwGcHzUnVNw_xKHBP1RdR8sEwDFIyR2Zw6YeryLeOI0bV1wmLHzLcZNbXrylwFGDfwCk_2OIyDB0exOEHlENsQXLwP1_VS2FC2mBXiJszm0MyAHRVBNMh55dMvBG8gm45QVG87Otm2sYXBCRWsLlCVVtWMAzrfB0DU5qdFqz9VycBs7cYfeZesaWisPP9mUa8Q8y_YcBx19kWL5BWxTFqjKwZz6j0GMXSRlhHLI4-gRGNJZt4FQU5zIHGCSbDMObibgJYSdaksq331Ts5Bxcjv0j-TRHOOwdDQVUaajYJo5TU2IbC2397Fq_VPLihHkNfCEpkOadmr-7CA3OxS25rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2GmYGSS7tci-XajNHr_yYEA8rvKqQBq5orrZHT66Es2Wm7sGkkAz3cvMgWMpS4AAQm12vhvKar0cyV1wb907hjNmrxZBUJwvhCiJiJ4uWn0v1kksXiANzDiosOkwBiGKaj8bRjuqmHPLcI1XTfWNL9XlSTU_awL05SWyO2HmbXZ9tlRIoJ0SzozRDv-0pr4v6E79NRKcz9iHzyrpPs6_0Zb10dKJvhvTj7kjLHam6GT7e3bFPKrzpRf9lwzfV2N7nHfifV9HCLYvzZ48JUMUZAKpPUgtAGGmOsuCh-b9Sko7N0vXNmECvYy-6xsarZVqx5I0sXqy8lbsgXOiynF_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NihM5uc9LKe3E-oGDtkkRrxBjmMiDATcTnqTXfhpre0HFsFAwSQHwSBhPzUEq-0J-JDR7qmnkYP4Gvf5-XP-gB6kC-odcMOU6_iLBVl8bx2ScsQE_5WM021B90RN1PPHkBtHh1WEAWN7WiYCQ3rH-QL6M0ncC2r6RlA5UPbNxiK2zpiaRfI0RGRycy2LR_bgHPJllLdFRnCN7RoWzbBzcwSqGWi5iMZTviTQB3QhA05Kh0-VrII7kiBuEShX_jWkZfIai05kH0Gyfoq6rxY7B8swahJxotWHm2OEz0n2f0Qg46Qgpp0uYds9M-Tn67jnojPodyr4gflQm4NFAyfkoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yx5x912XhKszyHZYa4YIGDumKzY4HF-3CXcMjU5dUKc-a_SsW-QfZb-IaVP2favo0Gk90Ocrdn5rLKThAM9hqMxoOQhDPAJzLZWG4tTaImq4V20YkOuzbTOCY1udeLvYU0vuxKcjOtwsVlfphnOs1xG_kyLBTUc2sWfUcHkKibtZTBDsBGvth4fndREFCuk7lpve-uKIlk8AtuwGhPtj04cYs-nCvNM9KUVJ76_GwqDy-HlKff_V1DOLv6Lo-RiprckJMHKe9Q2fnU13PB-oJDw95FgV0X0RXVP5uDm4edF9w3qtPbl0966m4sNsUzkTkNVP04FhPCq_xicfU-KQGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ektDMWA-vSIUagckQoXFVAH6dC3AQHCvEFY0GYjth5V7DDlX-teod7ZDn2cSYWOxbQz1SC6aEpPgTqlrglxrGhd4s3q8l_RgxwQ3kayXOJX21fR_8aQ10isKRQORCebogZ6y1Esspun9K9FDjJDlSGKB68TROByeb8NIo4hcFfAEm4BkWjsS4uaM7dD1jhZghHImCSDNTqTKsvwRZ4V-yTYJxpHHPGxT8UbaabpAjPDcfL2D6tk9MKrF9k8YNBFWrRq1nxBrf-SiHEFAa1iV7tFixYDCiioy4BCkVKU006OWE6wBY82y-krRjowbDvqsDz_kzD93cKyJoliucb7h1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNEHucf9uhqPAUZqdFZMB7_FSmv8j8N4q-fzJfC0myA6hyhcxRYGqUtUtNvoZ7LQHUpniNCp-lv7M5-5hpE4W-VW6o_NFg_1EM_6wG-dnXBvwNcOcLEvfbd2bWjgG7P5YT2srjvxeuy3EJogCmCadqXIrRYzUqe-APl5ZjbXVOVJVx-GX7Qvpioi42AKewR2nFOz4vPPWoUM7-KiaI7rJs15eMACIop_pq4y6BRtcL_fGrGOz1ixgROmgMMeSERPZ_RSSlmcvqmdLvbl_kGTVwPjykZw5ogREEqCqlWS5oGjIpTZKdEVVBVcfKIyN-LZndDDKwuupPE0fMGz80aSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSSh-zXcMajc2kJqSZBWCEP1IOaRIYZMWXy1Wn2jwisze2RK9KQXJ8pJOd690DQbE6oKmpaqG45pg5lvY1xabCXsS3PNtWWOc0j99SEAMcXuKI6UTDXZJwJ_tzphgY4lz-S6TOB3MnqIEEVt5TaD30sOkXeqlTPukkUCEXNZ4F1ZYUnqsuTYnc04GA47KvI39NyXVA93mWExWDFcpTxlgY6ofQo1lsXySVAaO1xv3mafoptuE7QySz-W-9y6GCk6FeFtlX0_BzqV_HcJf-TO5gcTJumQJWm6r0yCeudLa6B3jnKgJUt8ytIExm-QMvKNx1M1x0ne9qIIHEiVLC3R3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lE1nu4pqbVY8FDzyWuE9_myIDggx7TBRo4xOzjoKWoy8wRdit6fRef3cyF65B0i_UrSOutJtaEtITU1MMyqoMZkb8l_VDcwtkMnEHkso57Y1G_7-3K9So1pxxxTssJ6PujfAI8nepSW9SkabLNjNmLk8k-7YBK1i0MkDE9IYRIROAln6DaaD2sawxfFj0tIU_bYhEc-oNIlZphDjHZF8FZ-vMlIfXpWNVONo9zIVb6fwUT3pIQUr25qDwwUiMbYGnwi4RDEkcN5S5ITJ1V8cPGKp4OHHe7bNLwfSDGyiPihz_OdRrrT7WDFxoNhysVFqN4kgxw2YWWE-NaTnTpCUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uxOfBjS8-jdAo4SGQJw5OsWm_ZewYpUtFakYJseqLMTfmtG7ytGurGTPQHch-Txf2-40fLtvMHvakhU1Xrh5UQcdIDOckxUlKdFBgDcRR-wR9NmhCUm0rnuCsJJtJCgdq_4YEVqahi743U1U-tejJPLo2aWllyob91to2_43OBk_GjwHbLK4_gkjPx7JJ5oX764qB1wok_d01ZM-ArOVOgaMSEzpgqz0fj4q31_K3VEzAALPzAsb-6A1ICMzZm6i4dsgOuCccjO0MgLvEKYGqops7ee1qtACJQ6lWQjwA4a_mpplorjJZ5s7aky72DHEGBHSkovvd4HCfGC4gtd9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXe3yXgZzPHlb9NRnPiR94rsRcJbV_zFkdW7fV6Q1zEvJH3gYFuyhz44OQyU2aHrUKlpt2mfVlCUM0N26HMd7ZikVqiL3QqB63sSxE-0rWH1G14XmR0YwTfNsNSfcR4uGYne28K6Qd3apZuabfNnyFmEStr6Z_KPabwQ2RLnJi6ZQ5iPnFEtIXpH2zJ0Bmaf8EPpQV2EGJ_36hS5vGolzMEEb6FUAfaTMmHRuckOO54YqYR_GKMVV8atSRzSfXZsuzp7WPRkwCKEgngjnLzLEBVL9B9FLg88yoy_rl1f9pnn3IKF3Tgxnzg_-Q-C0YiRNdlrIGmUIB4nvgSGViW4iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0MvrEDw_aN7AQYoEavgDrprSErR1HvBclI3uMYgdqTaVu5H0IoRvMZ_va1Net3uWL3rQoz8ygU4G6RvG2EBfsa-J3tVbKJGmk3K26Bir6KH-zvppwPQKpGSpCTvRCEnIF4tz61oeMqmImnevEYf_Bh0VWdRRK8eghgMjYb6drBDuBKlTZwtbHDa-GwlUiUmwyujWrgxsl6ZTGI9lkD03xBVea4ijnD1ZGWsU9Q5K2m7Af_UZMgqID65gXCKRUHn86JJKM_DyVLY9jwTWf4-jyDOGXjdk9_pxAUbW3KnprBl4xUPNckn-YLUoScZNSIRGcwfB3JuXBpwOhugl9fxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT_EWNBkHCFVF-VMd_RN0U6ZFzy_sNzagACrWZgvZJ8DHzgnoVr3ZScEkMkQf9qMaYiqYUsYNc03rwbUJCK3jD30ziE4OOM9Pq8zwibUYT4EYtI_-d7EWPnJylCxtaMO_HBgOy_cIG5gBr4hTpgKtnGVTAdL9WnCwh_If_pHf_-6k4NLIfH5pyqp89EO_skdECufwROm737xr9G7X4Q6xIBDGD0plawmCGvvma73ub9DX0EQ9T90NZKeOqIDqultF08K-Pi7PSRQMRXF2c4GojjORhqRMPlf6m8PS6NPrX-xgKnJhFpPBwUWk8oq3XZcf0778aPfjCHDS2o8WcpzaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCV7remRmcXvsdQjzkkTCxErNl7-nd_pfk_3Zc7smoYPSyY4yiy7WliclFQocammXaxRghiWCxxPPs3CnQ99CYOeIHOvVCSkON72pL65w242bSClj-hqVDhrYYvplBn1UlGOBP7pGM22Wr2UOtVetObcqveZjLP3hdLync_-2-xRTKJbDav9bMk_b4recFYBtjupGv7gTjGH6RA1nHJiNKBmdv4AcPq0xdj1sS83kZQJXzwjEkYizIP5Q4V5-Rb5YkYUM70OKW2pIGLSVmYl_iLJ3xrSdbnyGu25rfOooy3M9aoBEzhHsVdfZlUlm1x7LeJkEpsiFW1ieFW1-r3YvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-EChqIsidXHslSK5-SxtonSeihaQmkhNM579lBAvPbZqA5a6aQYVPsoW_SzN80WJ0n5HBCmqe1AznbHMX5gHVM9l3yCtocKTNRIABFmz_LOXUgXO5IvkaKAcHGluYolP3TfdsAFK3Qur9hEUrT8jOu55fPhQJqX4DGDg24xNVFrSD_0YF-W13TSSQ6P3QAD7UA_EfCwwx0RuHiv768Nu8x82FWSzpdjB1BMPjnftN5i2u_AqO5u5afUltNo6oTAoAI_16enl4gWt5474LDh2k3c-wSvcsBjMY2C3TNBZvCrORx2Wc92s5kZRhsU3N-UAiQFZyVUlpc6-a45nusnBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpFILa4zEb7gKHtG82KwEUXU6CKiaOjtoTjiLo07vtrD1yRwH0jEvxabnyRMU4CXjbRoUVheN2OHQ30qdVN92ODbuHCHNgKccSCw3_OVw-IJWWybBVHyAgxyZDA505GDBWTz4ihFspRgz9KKcN9tMU7PAlZJF9pJAoJYsiVIYO0L7B_Fbl59LiaGQgOPh6N0Yi5cK7h4l0do2KiJxOmYXIeYFwGc7tAw5GlF-y2Dx-Y-SM1yaWsOpO9aYtWCLNDkShTkP-sK13FpbVkvf_0ZgynuedpXv-XxYqpi50Zewlz5C9Ump41fJi3ee8BzUW3ZejTzx4yr15wifRcqpPu5eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVFb0Dtm2qCkNmPBkgO6B_JyuWx8Ml-74JsehtMo6hnsku8x5dd0KDrhfESDjpbnCoGHA9blOFmCxRf2TwS1hTI9EO_MV1o4V686SxKuQ8Iuekd7eCMx-QEauni6yrDOKptoANTGWMtsPfc0IarytUKuhYoJFCMz89TuNKYuPnO7Ou5GnqBe66848iLIQxvv4QZupc_EKVWuQGYuiIFNu_FHAaFp-vkqqLOJjIpfvzMb6klYdOARklynFkjZvetazZBer1_Y4ZLeRde-bWyr4MZpm1EY7A3mL_sSc8AcCvoO1alugdngVOI8C43a221bat2KhbsJzyxsHe8-cOajsw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=N1tFa6UeK0TnZ5NHwknT-2u3rvtjSjRFpU7CrXvWCOxMMnMbXvs_c4S1np1AAh7l99NGMZujorqfI-wRJUEjlSTWueQkw9xfR_IMwpE8jrI1kLOCclB3b5RxdKC1J0E7zJNvPKbPBJ33H-9aShAehQih8JGkZFLEOVfqs7Tp6FNuDEO9s2WXu7XihclcHK5uS2i8aY0hCWtY-9cK7ftPSzDBrlOcK5OHFgCKpZKrb-WH_ZUqWG0-NyQ7gq46Xs3Y3IxoLXKhKo1XPXAjwVqShB_p5tlCczmwsozyAUKHyegRg7__pThSHoLkUWb4G0g1qHnF5xWOLmnGSleYjZEbeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=N1tFa6UeK0TnZ5NHwknT-2u3rvtjSjRFpU7CrXvWCOxMMnMbXvs_c4S1np1AAh7l99NGMZujorqfI-wRJUEjlSTWueQkw9xfR_IMwpE8jrI1kLOCclB3b5RxdKC1J0E7zJNvPKbPBJ33H-9aShAehQih8JGkZFLEOVfqs7Tp6FNuDEO9s2WXu7XihclcHK5uS2i8aY0hCWtY-9cK7ftPSzDBrlOcK5OHFgCKpZKrb-WH_ZUqWG0-NyQ7gq46Xs3Y3IxoLXKhKo1XPXAjwVqShB_p5tlCczmwsozyAUKHyegRg7__pThSHoLkUWb4G0g1qHnF5xWOLmnGSleYjZEbeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWqY63eTd9Kdx72vEkNjXYSeLPb9G_kltBvUe3GAGGJRfN7pRjvJ1eynqQJmRbtvvJkVh6PyjLy4ZiFUuKi_YS6DlobWYAHXsZILOa5Ev7rsNr4KohacNuL9xHW42Hvr3U3woUNJMoKbsSsGz1A_jX87RHH5DK2S5COghcTSEzFdsDTFy3dGu7tHdGoLFcS7jaSN_KGxXAKmYnbbf8U8hxx-s5ZA79HOLKdPTUOatrzLy9Y-Iq1f9-bc-apXSLRBTvscvlQOdpQwRbxoKuEPLVDCDPOeuV1_7_5v91U2-Zio1eTVByBnu27W5BuwlokG9SK0uWf_i1MSa0ppgJKZTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mssreU44QURUUkJNuUWX1U4-ci6yr2N9fazGHZNTXnH5MQbzJK61XWMCgNMgt7hBLRX8hZb9GbMCKcGoxbZ6vEMlhYvkK8I5JRiZOA-VJvxam16xQMkQ_fZO_Dr1yHcL5e5hxzHECLAyR9lcijm7qQ2VOe-VU5OcbRjJtE1-D4T_T00rX0RgMPAZRzB2fhsZlXxZORVWUzjdJD428rxyNIVe4Vy9D74PF2zuYE64D_rPibLj43S7vPQt5ggftnTXfw-MEvLrmChV1ckV_wU-IbW4OyQ6acfSHYNQzEhWgcWWoUoJS_y8daOCRzky3pTNHRP1sE3A4yBUx5Uug3RQvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICNThPIRFv2uWjizhKE09FubJAIhLYmKwS7zVl8Q95U5tiwXx4AkENtE9xJvB8DJXJpztW3PwqNEZGGLMQDnE8ySm1MpAJqoe0VlecELskI1_TVCwXsh45APDx8Lj2vgmLR3nOCVm4QQWa07Mn5ADTqorTfhhx0qPvFgMvjdfUDIGZp5nJLRlMvCMKOBenSA1Z7VPEa8DV6Cakc-s3zCtsXp0Ijo4kjbMnqqyChRBelK0Z8kmOOK6m3ihiOFHyANiAnVh6DtJQv1_QaW1VPA6FbhyE3QzQm4SWGmKmb2AYO3eHc3woMiSgk_95osre_fpaYdAh7lniYCyOhxPyrLpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj_NGp4wThSsKrboYfoaEwe4M7ifM0hormuF7LevGd1KrVk0g8fjSlRkWq4d9kgEu468gE9q5EdhlTlVdHE8ui2EzTs4W6Gwvgc6i_VRNaagY0FBYra6zfJVJ52ahiU17uBgGDC6PTHGzWa_k8DS80ih6HZ1YEiKpHPZPQ4fz7fXrwMKjdcJbh8fy5pVSw41AsVC2K9Q-CUyE550E4n3aGmR0tbL-9_LZ1Bcu3b5QEKnRhYq67RoFvurV64ofgDXIVhx6n73gKNdY8XYVhRtupZG7dpu_tJ6EZvPY1JUI9RBKCI6BW8AYq7Fxqk9LgFR64lRCuLOe9aWvzhXsUnY9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueyuxM8In09bcJLfajYtUDkwJqQQjMdawCIMuangLZvK7e5XEql7TXJB_XvLb2PVO-3plCRedLbHKyb1ktggLTkmhhLRG8wOLGenpdtr8W8BCZVhDQBGCTobOCInch39WS8pnQXX4c820El3uDeNvS0G1GLceXK4osYkDMdm4tZ3326B-_oEEMJYgsUy1NlII5a5mCTbgGaeTJTGwBC49bNKi0BmNeAdMOyBeTyyw9JM3ilotVZrP1L_KW5baQPxO9xym1RL6GAY0G65T4Zeu_JDp70zC19Nu9lVRdkiT-lMTW4TYaC1p-DaCqFVbSqNXk2bcCG8J2bmmOQ1EsG9GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI0RiBCmdOf76HZELVeUwH9H4ri0eVoQ_2CIgJU9SmSTl2bhmjBL8Y0rzMP3x9dXw2qCV0-9lK24gAHp5Jv4IsU5mACQhiRKjY-rmrPxNTVdEyGDVHy3_jndpguAqeq07w5YVs0HxbyFLLjnREYwg7qLtWKYSV6bB-P389NK8p61VEmt-OgERzwEwIu1mliZkhriqq2-czwBWzLFY5jnWPyS4RnvRkIV1kfxBpZU9oQVCAWb966hkr23OzGXkz73OI1ddhKofmPwoe2KzZyCewuWZDWhTxLzeaRe0z_udP5hUErbm_BmiR1_Z25I4qb8DChj2ScnpRj14td-c3isWQ.jpg" alt="photo" loading="lazy"/></div>
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
