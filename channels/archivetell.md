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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
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
<div class="tg-footer">👁️ 350 · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbD6efolv6_zFsrmzzXBVQ4kySILD0x9g1jx0WJ3bpJ36Bi7a41Uh1HvL64D_yxHpaPOkuGBVyzrOO_1j9fbZ6rDrr5jYscUrlcyGkkkwINVwzn1PSyzhbnwBQDx_BiRtXUhI5sIR3aql0gAplhNV3d42ByWlXQX3XiqacljbTmLYLzJNv8BeSU_3y-GNjSzPKrlkDxGpHTkZ-Tlb91TO1XEmooFZDLpZvxXml2BweCmGczuwTys_Ba4PISPdJOYGUUGdyAFoOFY1n1AjaHenMojb4TwPlx78PmvUJzFpa7OOQWuKFADAE618eSJLz2bgZNhSpsXs2kBr8Ci-scCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShR5cy8_V2ugrIeU0mnbbyrZtS4lEsn3Xp_pikgjFG6lTr2w5bawaj0vgBVKwIOvd2beF5-mQgBm0pQSf31QZ1I1qIhn_35MJjc0pLn418ABjwR6_jHniVboDdEvaGL2KzThKHPNb1lyyuIoKg4xk1DTBxULs1wp5csrPzNJMS2llpwDDecHHZQY0g2QahDMCPq8YSY7MYeLa6IMZnwpXCvX4KfhXiQTpLW4ZdIhSAOBdCkSNIIZScnemR7iNjQHyF0M2DYgbqJnB9_dU2Ht2dgIGLgvQLoh-NU1zB1JboLNqxHGY9o_nTVSW86GDNJIQAwW8hxFAsN7JjAD2Y-Lgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTRMXsdCGDj7aFuXUZKDOMm7hpnW2qS8tXsgryFD3PHCjdcXGZ2p3KyLf9II8Sj5xIFz_sJK_jQg5UBp301tbZsYxrgBtzz5h04jn55Rr79UHvLOZiXioSHYIlW-AxizbLy7dQpYB_gnH4WyxKdGokV_nB8KepSF1ydIQcDH1qM3axL5WxWCUncT3bRAmAXYTL8SJd71fA5l1ywFiJ3jSbnRTC2j_LjnocwAW-GkWdIYLJQkwxEUYbCUYq3PZILjLCxwHQCMGjTFcxrwBMNo2V_ET21Nq8H96jydtNydvQMamaDfBis_H_yUjp_LETygjTZrjlR2jg3nXlVDFvnfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=CzrAeILMIXngHO6xEUzoUxGy1Iiy8HbI5qeLqGhFRS6HJPi5m3FrltvsUf_M3C1Pmiguq7agC1LJFzy62NrPjFkfHssb_yRsDfKHIjyAcbeHOC3xgttg_rHE1wA_8NabgNe3H6_zGRb4DExvfCJZkixooWqJLTEXxaT73Byg4S8qntU0_nRJBPRLaUOktOMDQhwlTdAWG_q1lc-Z4OcD6pEaEqZAUyc-yG_HNWPB0B4jlGCZKqKQxYAOnqwi2dj7uq37Tpb0APPtRyMJXgkVG32ldUmz0t6tqnSnTHIjoiBWQR7_rzvzhhLpQwtanV_hY1KHhCMfKkI97uzfIMggPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=CzrAeILMIXngHO6xEUzoUxGy1Iiy8HbI5qeLqGhFRS6HJPi5m3FrltvsUf_M3C1Pmiguq7agC1LJFzy62NrPjFkfHssb_yRsDfKHIjyAcbeHOC3xgttg_rHE1wA_8NabgNe3H6_zGRb4DExvfCJZkixooWqJLTEXxaT73Byg4S8qntU0_nRJBPRLaUOktOMDQhwlTdAWG_q1lc-Z4OcD6pEaEqZAUyc-yG_HNWPB0B4jlGCZKqKQxYAOnqwi2dj7uq37Tpb0APPtRyMJXgkVG32ldUmz0t6tqnSnTHIjoiBWQR7_rzvzhhLpQwtanV_hY1KHhCMfKkI97uzfIMggPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSW9Sw6ScX8QAW1OctHDJAQe94wn1XKJlPF5Y9AjeG0hvRXw_7hkbvpdYwARLekUc4mWksv0zkUL6B5jnfH-JmYyPpEuqoJYGXRmOk6Jk2Lh4F5fFO0ctkiJW94UWiuR2_7qM80o59MWjx134v89-RBAFG5xt2DCeH1D-llNMl9OaZuY93Wmaeu_qrod-44So-F9TefgmzuNKR9zunN0QZIcZfqisy1qF3N7_oiJJjEInsu2OJHOBEcUU1GQENLkuAjNgrme0H0tMbnrGvP1Gn1ow2ufUrT5qqzYlO9YTjrRvPQp3vV9PKun-UkamKFB9MMBZMLiZ21aMIVLDfMEFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4gWTMB2-90zvr2n5J7ekXQt9qIBoavnVYEOjOd8_jKFzcMe7Df6F3dP9fXwkK2dzaO9hHALpj8UyV0Nx6MhjRKzVxh3NhI9-WaSyM7Tyx5exaciX3Fb75udGoXSrqIUa1hREb7R6I5si-aI0oL1TaQrQRUB83umNv4j_4VCTVCWscSphAQuVsneS2lC1tiJcKOJ10Gkbl1WfxHLNnrjxWwccP2l9J-nBiCdF91Gv5uMtdxABKXe58w53WYOLJjvfdDeTG0M0WYPluVe_hBSfmpD_1Cq8ClX-eqoZAPxXEfpsYdHt68ITtKWzTydzQw6kVTbrQUj75jw07tblXD2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Psvc4thzv7NWap_X9eaYqSwjrsoQtDJ12f-ADDMZL3fJTAgt7I8opUQk23lRgxEoA4ft9ZJco3X1KzuiQkU2OLwzF9zFi8Sdrr-6eeQ8Y4uidLrDvwvgsS9PZJDP_94FPmM_ohhcNgb2d0_8sKCLf2drfjgUGVZ3M6LwcDxJ22QE4PVoNFR8G9AAsr9og0WVOqPtqR8SjISnak2atbe2xA-wChSjGd0t_-RKSte_VAt_3uNcE8MYIQ4XoybEvb4oI2YomiX_E2b3BKdeyDZsB2i4DvtDRCCYB4rgXH6WBFQ8h62PqflC8ShJHzCmE_4FHbmw20ADP_3GH8qGG5U-7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUNZtCOVr9--g-TbCXOjG0BlfhCbHRb-gFTib3ZuzoxxgukEjMfV9cfzLEDRGHX3C9YfmXy0WryAwdKMvMhLfVYuv58rj2YrMvVWQGU2Y3GncNBwEVid4dqmYwyBRUQP8vosdbx8YzqlWW9rri8Ket1RhtNNGJbf7LqQVdMQ-1aPlrKynZB0DjLtuFsagR_npFa35vFqIWvrbz5ABqrdbvGBN98upwdehjP-qg7u3hR1SlUXzmAbicrpjJrtLIYLDZ7CO88UQwhIpeds74sBUD1iE4n2y6spZ0ayvWoY79k3j0Xk_K2mqJeSTJUJddeeXgn08O6sp9umdSaf8NhYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7CTGm86XuwWxmhDwqru-2RZiH3C9r2uH7CVcPs8ei_xIj5c_M-kOayJMBnKjP2PfIB-Y7S7wKKqHFAXx78_tt_jTFqpj_XaOUGtt_pr0oEqBLifliSVC9nGyqsDmUb0gHHEFY2kWG0P6OTCzT86rkUyOyZVqsDnaf03BgGBlvdSAu21jixFEcjIBIhGqe_sPWmgpycAYb9OjIKjZ4LDHlDfOkUBftEZQeDqG3jAA6PxVDwMV6egqdDeTgU6IChpNoP8XVRAHgq18N524aRuwPQrDV6cBxGShTys1JzaeeShQOZFL3A7DQqiF6h-Y1y4CJkOK_qnkNw-A_d-QV8-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFuaEsxAy4HbIeVvEWBHqrsqlLwadhkO1F2tjiCjS3MJ96PkjCjbaJEw1kbtmppIBQcPkG6nDr2XMzVS8-sojvk3ANXnn-lFAEUeEv0jyWc0Zda_kFIk2sF_apewQXhon7WClEts14bE4JEZWUUd0qUE1_nSk5_ZW-53m0Flvrtoi2rl5BUmP1xW40y0eIh8rERACxYx9I_e-jQTR4hDp_yfOH8CbwKbmuT45Cxm_Aual69HEJLTxIaUUfR3ghcUCi2y0Fqk-hLrVpzB9f_et7ZCH76Q7V3yLklkM1kWLqSm9CP2rvKcFmXwMKNPpKhAPXBaXeH8GAyxAruuGnnmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3rBlRFRA6lOp8hBM52A-4V-b2hmLID0Lr2tUC12tDJc0aV7eIt8Rrt6f5RhmP9Yt6f6DPIif2f4-MX_QzS2I6F_B_wDiFYBZTBctN6qutl-9bmA4FieOBZ21wj-vKJlBU9y36_tIIp4Dzz4fU_E2qa1c4u5e-AxL6rwlV_kN6meMLwLCPAIxXjmiygEJTu8vawOtbcPqWMgjmTexcU8qdAv9rCuMVTxZnh_Qjifu-ldTNNKqRgqHANQ8G6neeGNEMpZpL7-sLcTFu2FDT7dHif4v5_yR8ZzYbGtEFjaVT9VAFC1fkg64i-FkNAxD3inmgJ-3T110RYM1PdWw2-jJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9Hz7lMTLHTZiPhjv8brlg5ndDRfXp2hYcB_SaeMdIdZZvOOHZmBQt1hetvNVxxaPEZqXVc2y2lCulMHkGPJR4Yr8uHldP1-bCAb1Rrx5xTmV91N90XeuwRZKLRatT9TLbFX3tcBM2U2KhPGigem7vbFxYvBuVqBOYWJWO0RW-Rhs0JrNWQ44glrDMB7Vvo7zdN1R6JcO60nchFAy9NvDP5FK3gWVFZ7p6uO69mCohuTyiAmEJGzQ-PfwzZOgExRWCvJWpcXdyC5uGF5jyv1ln66rdKzB9fEOge7p6Pjb5g4K73q2-MJnipWOubXZVHV-L0FnmHByEsyxQ7hpfgP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6vmJEr7a6m4B2k_gKDl3TKZRppytiyzycgK24FWcjwmfAZqT3Y-lO7j1-bTCFGtXtB3CVkfyjSqWwqa8xxxCv119J4YoKI4MH01Bf20KliKK4VbcSYdBQQje_wdwhuB2UTupnKj3Q_jnMUroawcavzcCGuXKycZ3eVH5MGHUx4ow3f1RbAQrliZdmtGbuaWFKLLRJHdSVVTBSpTlqVfmmDK-qYPluTbOK6qmppwSHfJvVkQ43gz4gHSTfDUTkuyap2cpJ8CEikC2NllqkrTiJwyIAZ8vaM0JiiJEA-aR5caG5jQud7-4S2_JS-Y77hkrVE5uHAig-1Eq-Pt4ZmEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qq7K83nNEjQZaoEHwr0xCmB-cbGtP8dugOLZFmlymPXx_pf886nCoY-7OBiq2kIfURZpzmoN7vUIXYmw_lZTQuzu2CR5KOvZYmNeIXg7WjS6Do5_J1WaElPPZYEvzJtz_JN7QztF8e7w43pExVI4zJp1jWH1aL2mUfvnhEOm2Op1jghTlQTAjOHxZY97cS3conT6m84KcLK6pCP-VSAk5W_CIUxTVXAanO8_D6WCfDp0QuTDBNiuL_QBbID88lbCsQdOUhTNR7S9hb50KZgUHm00mvsrNuCDjQMyYy9Ixm6Zo6qViY1E9Cv9mrBaLv3CzWJtUybi83Tf47tdues3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVnc_gcwvF8HACfjoC5_kgh6J8oZcdn_XcFr71yvqzfW8U2MYX58sP6ejvlry0qxwAlRRkedH9Ztbshpn7Wp28jQJBPFqIMLhyml5fOjONk3O2ZHbFzfyeAKK__zmOyZyr2MzP87h4D97RysjDHEb3t-uc8cRYFOO64G5BnLANktQIVjNkHccc2Cio_QwaqzQC4t4jhF0SpFnuu-cA92f9wouHQneV2L-Z6js9dp35ls6VyAWR73a3qWIc_pAlPLc9Gj0pP4Hj4sGFIPrM0COS4Wkq8ZYnYQidAnMye4_IgKNpZE5HF_z3fmF025y2Tgk07-7fcjYuv-zOfzIdFjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyMLZm0-CsLRkYeZ1e1BaJhuw_Wec19K3tpJI9AVhgl8q99kn71qaCY-x8aQk8VzQU2UbgitMUoCgEA8ngROVrb9FBLeIXR0u4POHogi9G50D9XQivHxN9IK6i_pc1e7_VO7kFvLVnyqdbA2iS8dQebESULjCe_2p6nciTKUTlNO2Auv9DzrC4Hirp1Kgp0XK6I_K11MDlI-LChW3v1sO73R63siuuCoNHUPbXRVEbUfU0ElDrA8qG8-ZukADT3r8_4QwUgr4HsbnTiHXJXz_veTY6meZirly8h_uv5vxcBZprgPVSHkhSqmD44YiwvAdKAblJA0F6NmqX9RJDHeXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da5o7oKSCNrwV-gJ8iF78bxRV7kqK_q1_YWNmubUCcIy1oAP_qQgq5JCXnjgBS_gF8eigKTH032BXhy3dv6G2CAJ1p3GrioSKoOrWt5WU_6fCO-4PCOkMYzBsgwrvBCMwpfmqg8ASxXjm0kTQdCTrJJy18dPM2eWWok-UBT_lgVr1rN6XXrIOQeBc7QtHr8TOWfdFTp2oJAPrkCFAk8ZPrVfWPutHrk3NqvK-bbySB6K92kjC6Zre5UyTitP3C4deRGefHWRpsc7xXcl-ZacHioh8IgB53-ZX2zLJwxEDj55pEfw0GmseNElqRIlgpXVDepBTHeHPl2ILMxfkm29uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGWAnAXpXdOu4ZkL3gzBlIZSQVVLmqUpuyl3ldnTQ6qZxXY3SKIJsKMPvbq7EIkPwr0YjWORWBpamE27ooaWuBP3BqVVQxCxEl65igfV9cFo8YX7Hv3-yLUsq6OI74hU4-qjVTdxf8_b0dG9H8Ur1zDDBBAlQwDXTNYjni8yUniwXy9kutjqpg-Nk9UdW8N2XZMsPpyNHQIYkMDWh-9Ow0XvzYWlLCNRSRY3RTSqTrtmKbKmrPyeJiPBAlJHKxcGV4u5OBBuP53T__wFHCKdTeaxuqaddbZAHn6dlah6jVDonb3jo76LTujfSaL8qNu3hBstvnHo-m8Z92uiZ4nPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yn_UEn3o0PhfZjIReTvOwkfJkoR70kESGKIZLV-ZTMuZ9wG2yYWoKwLCrDU4qZS_5nSJN01TavqMCQRn_Vjxil-QnOpxYwyxQUCY0GFS9P9yLeQZpNYDz591CCnisMbYm-jLoOV0scZl396jdEGh58eiAenr4Z53i3UsOvJDyp-Q019tlWVj29hLYTpt3y1Elxw23iaLjVZR1O6FjoRHEP7DrVGEVySRD95lfsXA5Vf8U1QDmUvO5xGUE2ujmxa6FtqL9II_y2NuHr1di_834PnhGxESdnibAW8HjlznGxQmOxArMExbhm95ZLq8-lBit4MxwxhGrIFudJc3wYSAvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhDE7p8QIctKkzwHy03HiGKNPrj3Cb9BbfYuBshCsrWEX4I2mcAz7R6alxcJZblfZq_JJCVby3n8DfRMG1zaf-qDWJ5MKKTdj08nz8t5ZzgjrQCmDNWczavRZe31HocPEph_rUFSnBBS_OdD_N1-ulmccrzr9uFxuljCdZrswqWOASnQbamt-oQ1Z3zK_NoPYxcasjY3QJqkh4me_g8IMSaOMqWCdMTAMyoDcPZnPHaJXtn0lUtg9qUYCznn5zis6AjTn1iz__XbctFqVfWUeWokA6Ncu0o4t5opkwPYCpZ7V-dor7xBaqEDpKu8k4qfO_x4IFBGsSVvuVR7jZra5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=T3j6WIeXpRqYKwJkc7vbGAiJhS5j9gfZsagw596XEpbXSJ88_weVLYgPtzt7QgB_YmM4RqEsuflZLcyTiRRmF1EXiHJMf5-YrW4Zz1co5_L057q8mm_eJbIU6-iEBdHELCxRdE2Ip2_87COaVE0E6gfSjfQPfiWBM0e4qqF4c7qswiAEO5oBduHygNF4RKiLSeZUMC1NM7tRv_ujVpUjp07JJK2Lt0AvcfysCqyvcGZ8-zhVLNutCuMAbA-OLhbnfeHYppW6rH_IRihPPEfEnoaCoSwDb65OjyA8cq84SFhCj3w1iQr-d-DXmdPN_X1pyxplGf6J8Av6M07ZBP1YeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=T3j6WIeXpRqYKwJkc7vbGAiJhS5j9gfZsagw596XEpbXSJ88_weVLYgPtzt7QgB_YmM4RqEsuflZLcyTiRRmF1EXiHJMf5-YrW4Zz1co5_L057q8mm_eJbIU6-iEBdHELCxRdE2Ip2_87COaVE0E6gfSjfQPfiWBM0e4qqF4c7qswiAEO5oBduHygNF4RKiLSeZUMC1NM7tRv_ujVpUjp07JJK2Lt0AvcfysCqyvcGZ8-zhVLNutCuMAbA-OLhbnfeHYppW6rH_IRihPPEfEnoaCoSwDb65OjyA8cq84SFhCj3w1iQr-d-DXmdPN_X1pyxplGf6J8Av6M07ZBP1YeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4giNRsbepuT6VdgNYiYoGZg5I9GYsextdY63ZsDfcbBJM32xkcVYSW2I1bsrIOfUZk5nn9R4GoW3wVEtnS8_qIV7J5Z5qCxvaRpf-Y0eSa1e6SItXtidRSVLCY5ratVmp_UGLK8AVEZr9o34dYJPTc9cJomS64ClFY-WYWopR9e3-SJJDuQJIzJT-WZSb9HkgC-O2-iFEFYu4AH01UqaJPfVYVPMrOk72KZoNDz__79lo0vU31-dYGJjymByE9Knlo_kzIftEqnhcQW_vq9XI5F8QtFUKZ2aignp5hDhNvB-1gxRXjsoPYpQAKBPF0c4Os-nYaereleG-ElWlHK_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0rZwbOwPzgBlFoGFamTIE5A8Llmo01uxQycORO0XEM8eYk7pDZrin84c0KbMef5bNDjhNYNR-LwUenx2ePBApTpl29Qwhhvdg_LPip4iiM3WPeug0iVPy1-rfNUehzfTgNO7O2-lcb5iFk15xqJzwGIVnz3sg8OUHBxphEUtWSjMAbs9wFs7jHleO6I1swVTdfbyfwlv2ctHDVvEcKtkmDSHs5rqZjtCChoyXeM8R34KaelIFzXsSRcxSEsWoU4Lq5UJ9leEvCnVrnRvYkK4QGASmhI5Cvkfd2zLv_QcY3n1alwUZp2a9y7iYcq5iWrXXAepJ20Ia5WTni6X0GnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agXosQZG09RZf8jvm87WyJVsjHoTJ-16Ixi2u_sIqmFL1i0m5tcHDDVJSkSIo1lGJVJhGtMN_sB5LhGonMJgEMqPeq6FL3RKYVuUpv-nIvS3j1cpEP_4HhATTSea7zAUFEScEZQMhAcHFYKRQngGMs3pbBPLwHfaN_gv8uR8STp6P-_fiZp5Nxv2_5bzjViiLnxPYNZs2QdpGDJ3MDcKUwi6u3mhhWFMokX0915XItoW_CWjngwT5yiH1YBCdlaONZp4b05h_iD7epg-rtvH1CLIAQL1IJhtu71KqIRFxTpCD3K-blhPExIAXBV8ZqfYZfXvn2EtOc1N8p7YeublUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_UyW3a-Mtx7m0d-0Lb5WihmrbkTO1K2--srokVyzJkNosbcZEN6eogTzlWzui0rF4aIP37ohy1o5bZYgrfoP_Rn2vTOCXkJdcFygOXgNp57IefRs7JbofraZGwQdVXwzcfAYbRyr1MGElqTJctY5lpQP1ZMr7lCDGGLvTxNajQJwNlboX-YX1XyG0VEy4eIB_zfgoK5Ui6KSwOIbi_SUBbIhI2eu8e-siauuN660TeS5PkE89FmD2HgeAqyXmGE_HHuIzs3oro6VOg50OxqLHii0ZmVfQ0uafyt4fbUOMbViU0H3dEfS7O9TnVzbgYe5Aa2fpsVbtng4QPMq11-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBmB104Y6nhGf73gF5X7DVccuVieYp4pUNJ5QnyvuVUSpqNwoF1UlUyabo9tzIrGMa8MqBFAqXDhuU4cHLz1i3UVlQx6TD7KRLX6nUMhLP_JlARnfZYmrSEn5E-jmU7xRKnFBG6CiHfbYSqUvS3BWA23l_99wmRfnsuzJwGtpfoQp6D4ypXys39Xwesg66aOPCR8nyoaI6eQRNAsxr2CQSYLe150RXe_JIh_EZ49KrokP220b6AO7xzS9PNcKDZ_jQoMJVrJ1OMQXOfNHXpdgI3PZyKBuuzGvAI5uJkCmOzKrNEHbzQs8AaPeMJXWm52-6_yW38wsArBLGLDFWt6PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKm0SOewymTgYTD5Ho2H-ghDlk6AuwfD1KwFG5cOARuKVw5bPwO7f6VXA_oaycU_xU9AWncLFp0TSr71TUq0PqebbaHwVgrePLvtspYbtqRyn5ECQ5pottAFsg7tDaPHF01RLf2vovSXm1kACjYL531ibXWU2sAe3ek4Hc9a1pJ_P7q63BcJMHVwsqYGuRiWKtRJxjCgk3sgSht3M_PEruc_1stYBeNYK9VIeQFqUVmdHHbxsFEFi3B6Y_EI4pmcsUJbDHh_Lqaqkj-zZDZ5xcHek1nc4TJis6nS4JdWbxvyLSAHUkN1qo3xZKeV_qbVkoR9RpJpIq7C6F7mM4HTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RzIG7gp7AbP_zagfwNjRlVQSpH8Kc24L4IGHt_cAMcep2BV5u1cREWF-BHuYe59GSS5FPy8Y-wCOTQx3xkOVqVct1iuLjeV1L4Tq_Hme4yagQesEcKnTmW5FAtdigUX__Lt6x5NL09Z3o5SXcgMBYhQXwVFZzDqJ5J6ycrzSZRA_yfqlURp17XIoeKDw7mHsbYD8CeGY_V_dcWQG6lPPD9iGLKEVxsRaF_nTNJbq1GuaXfvd8TfgshTLQ_sdCW55vLD1mgp1m2ZfrxIRq2SiPXgS6_362X24SYDIIskjLgAVi5h7Tlj0xtZmoaigK4DgusWdHvD6H8snCeGoC4_8gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bNyF5XQetR11ZNAJEY9v2kQQ-UYmVFdaTl8raJRRP_xfcSku1ewdYlDvHfvTIdiADgn8geJK09z3_vxsdeopIaE2ZmEGf6ji2jZwWz8Fsn-fsY-gUeiRjkX8YAkcU3D-m7hp6-9bT9-tg43FT4GldcmbThNkzcpPRsup1CF4U_IP3zGUDD31BWKyRvlxYITgLDkg4mYcVGT42JDjF0EBorINSbr9_Hxon_OqvgRxK9_fdf_oYNqbCIBw26lkvpWBuWWFj9tTNpjUC3Ld9erLcPzqkHqUiAgAy47JhbULddWuAaF0eSNz7d2TfZNnid2PVsxQvgMWP-Pc62h5NDTcXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lXjGslJQRr5z9Tj-sqtoUTsjzMPL1mjEtV45D1PdYuoBEUCjhmkWmJ1WoXtqNBvpEbzo2vlLYhL8_NIORZIH5STHIfiA1-S_sNGP7sZfwi-MSTk9tMvFdRPszm-p026baUESwY4Uwjnl0MRiJe_eCmtgCMvKg8WPlb_GQsB2EY_uern68b0mLLeiUIaZY2JAMcV-YvfctaDUZk3hnBlzc9_uwakLoFy23umbtHn-2nefkkMfl50lsuoeI-D2MQmG5uYPH9iQYVYxNDRcSCafYHdAYUqlMbVd_UmaNPLdkbeRMOhXWs_3KTscQ3DNvJZsXy1TSTC2XAtAp9xRNt84SA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6IqIqUO7dxFZ8RYUU_XXrmXc-auUOhgPMm6d1u3xIX0sCEYvxMM21IJm2HlS4wdACTDrmkZ-4fFzrxqyCC8SGmtvncvwcrvFhMdEVozuUve9_l7epDROeJuPs8lywYz5zHzKldxvOFo6WxUjAcgKXFCRZc6rwuYltQTfmQXLzdvImmNO5wtfW2FBFhb1SQ-9X6xq6YvcbxfrXf-8yEdcpM2gLXgQTTSVNoampT-ONNoGWjhStQt8k795v3CnWCs7M5syow_Qd-7OS-QyUncpKr065XHtsAnma4Pm7zyNPAwxYvuB5YMCnuA7975fmoIgZws3YadUzo3R28Kii1LUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTvSUQJ6EUqr_sNj8MCFsBBDpwCyT-t1ny_9RggueFatTPbtYIWkhb9kkANrp7AnFTXV9AgdweuzC17uG65lbSFg_WjLw2yF6hNl70Fn_Q4ANa15CROd979GUObJLvYtdumNafZtn6ZRagkhTM6JIbhvIXg6A4d03jtHjDzUa6DWQjn9MP2me_vJGDfQ-bWO8tNOAQPaj-1KAua6KhYBe0Hxrc_BkS_0Zg2R2oMI_0rQgfN-0adcQfmsFICVZLS-1r6Qgae_dMVKT1qcky_Zhq9Ruxt78rfffmYAF1-altX4wkhLWLBQYwdaMOsCPkURQ0M1j98YtaL-sHK6biYsww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvXp_sKNUp3wfrpYd2tfrmpe2I0WAPkI2tt22b7QyKGBKGdldzDcRcDV-3hVXeXpfu641J0mXj9WxxFRO5WbZ_GR_At6LNiRjrOweHKszGoRYbq5HCeUzgX5FxtoynyQoeLPKH1ecuDWY1vsE8aqnB74ukJY_EzJFUiZFv2Sh3YwTZn5Z1WIZA7h6TXxmC7hy84bRUubwLaGYqv8S-5y_KAI2FoqMx6PdgUryAgpmTz1GTowwmc3mvlJFSw8NsOYFNl2cZd2p4pjDh5v489j0a-8CnUf-FdxH9Ix_TKaHsxhMVwVhhijcaYhNlBZnCC3gOofZ3cDeCWXWimikj67qQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bomn-HxLJl_jPhG4tRo2JwPinp7Ni9WTiFyQTN12LpA2gEF7ZtYzEQKCzElQ7xOOfgF3O_8RiXKunJ1WHYnOGDssgOng2l2LN6dXIPymh8ZyO2SNwTaGnJAjhPQF5fat8pSgfiHBHq-eG43DsYqRGLLx8wTLKgvkMt2YbtGilQgKLCforJpJ0Xo6SHzVyt4nHhYSwylXiwNI3igdwMUNhdaoNiMTdzAfIjbz12R7tXwyImP2T6BpqUcD7mHoz-co_HYHL-PkTQxp8ghU6Pq70xIB5pjAdvuJngCUGhhEYVctPsuOx-Zo6a25TuTe9TtWHe4akQXgCIYytuxFsjLvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fUCEbR68Ja4iIJmeEpviU-vKijDS_cNdsvDuWt6Km8PIKYTg_F3s2j1JEeQKpfOAlhcBLulWxytHsCJVKcvVCMvqQRYLORUKX84tY8unkGnYXYgFwSqnqYw2GpHN8sGh--4xtn3zeYDgTN-JwTI2IqTLD3NO9BfqjsvOQ5mpp_-rMfU5wbAwzExW20GSPCLD_Z2t8Y71N7sjn03SFxNxXUGn_w4wOQkYVYtd5TWs3DiugHEyYYCQG6PxKG4OqZ5MgnXvGzpZKmC9xIYd8SZRUchiXWEc-NqMqAe5OarwaE18eDMRKshG3xcU1Z6qNMYhX6ZMevYJz2xovGm4ADj6Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh_ev2N6kTQI78ne1BosariPeynvet-y5io7pfpu-WsZduwBz0isX6uVxdZnuZODfc8QBNVKlE6fle1d437aihLl8MsCL6GA0ImN4g7EedEb8YfRRjDl16B5WLiEvn8-UjvH9A7CpiW7YPP-YXhd5w1CcGPutUw53AF3x-B4XEXdzDwMzEuGhO3rDxskgGd1Ny8iVZadstfpFg5xM3cU5NmZALuQL0Zpf0DJIzWNczEIFo0FQ8Lbco2fEhdngpwTGphJ4jDxFFhs4FlCWKym-TKneujY7IqbZ109CR_4sT78aC8ObxjphvLeoETF_Q54JvvGuBJlEw8bW4ZJ6WQbCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlVyYNia0b70nS0nLltWBn1baqADhQlIq5LUIBhWdz-1P8JGpOybQitlXLqL0lqILLrZaUigNCxbquX8SIch30y-sTKGwvdzMHIjVwGWP8PQq26k8TR3nOEIzTnEi3C6wvnveNcqoZ4vgnMtpIOTOd33p4lQQHNhS_NllJ4Bg3_Ltjw-61kGyGbKhQOJ15uIF7XQ6bm9GwXtAIiRrtmNKtra-ZdGosLcf_7t6arBDEmHeUiy757BI6NHteXbXAoCkqshfwoSrmLYZMnNQoLfkZMVfUngyIGu58qdFxYMQmLwEythsNnVuxyXudPof1Ie7j1oz3MRYnizx6YyA8jnOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2SHqsWqifMSYbUd-vQ1HWzpzG5ZXWiMcQkiLb4us3U4ap0R12Iry1HaqwWqqLQU_R2yNYy2Di24TAm96q5W2RXtNuLGmD70u7p4B7QlzG1QikFG3Oftm0Q6xsmX-04stuZglYaM5_jpWZ9a2121SCXtrpnIVo9g3_lJEqFMtqElqLNiwg8JE_4lWAi7k14dDYZjCdWoP_5OosnzLZCmtyQQXJlMNhAFrikwb5FJEUxibThMAwEyHOHPlGGDsJupTbEBo7P4sCpn6-htdqcjSLWcvPmlguesVTQN4cnhN4MrZmSET5kdICfzIS7Jr0aIT5JYv1lhvFZs1p_ZrKw6hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dba6s4TPM9jbt_qfHznU1J7qJWcJvRilIFJbDuGR8Woq5knhkygiXHm4F_h-fWjG2be0hSWnxq4nKjMYIgdx_TREg9slG6dUTMh1mHllOLVnCA62eKsFMNFEO7I5UzgmYE4v_C0qXuBb2kimMAhIa5ft6XZOnlHPL4LeijaIqjukWr2Wj0rgX6w_2ZOm7Eh_4zNgEgN--5FchLmvHsvkMwJFDZI7RO_k1cynxy11tAGzGqN96L5_SSbOpEgHa-WNbaF5Wrc95SNzwflrXRM6SulNBBHa0kMCDfV_xwOgvoFld764syizo6oNhQ0EHrEI9w4WWizNNpQEMn2ZiViyRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDN6ArtcXBf3qDfkxldvhcu_FJb6ZKrEE1U8NUEliuQs0p1Tf5nXNiC24MuzjOm11ea5czXS2xoH-bEv2IX0IYCu5r13nCbQeye0GtapKciBlfLTE7Xf2ihB8yKTkPIHGBR0UA0G6Sves028bsCb5mqMYvttg0WSJsyva3L44pu3n4f9eYTp8NpxQrlyczUer8jftnnwp9lkShbKrULdGUPpAGrqr_kLcIbLFixm8nrSQg3nKsdW42reyKMv4XXbtigVsPYhKHmmJxdCHrc40QY25D3DivbFaUTV7vKm_2EspOh_LT8wzCvs-UyjQmaPJJwPI2pgHHnZpedubSardg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W3dbl43oQbe_RNGJXLlfxul_CeSyFKkS-9d9OZlKJzfNbPovYPljhxDAb42WxEpA_D_TJs_wLJKs7jmN_XI-PqE29ZAn408hZ3FPB17NWZl5ZwFqi5ruOBwFsJ58y_5iR3u2y_ypzXkYAaMKEMGPmrPlX4Wd9RKwHhed4aymqE3NtINfgoxxNZgqLW0rdCIL26Rd-GxcTqbh0g8GFngWPF5Vkyb9wJjQfklx_tero1XIwy1iqSCM-6D0iSXkPDK841OFMdaeMmJ8i3ck-8mEghhBcoYbU0MWO-KMlusVF76KuvacaO24__cldzSOW_FpI23nznBtBs-HKTZfFJLy1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pAiPlG-gqjqfPQkBB5RhnfamhIUtLKVUugjvdK5hDFg3_LJfkR_CdMriDh1X114ZTikPX6VglkCe4hv4VOl6yuySWJMVN2_8EDNSmvF6UydNFwk4r6OVoX-ZO2g9STqf_0evQf5QMCfHPaIYxphJreQ-3SfRkjZ3wXIiwogZvov333gab_PKcYFZFbjzR_7GpITAtEGyQN80634RKIVC6Muiidepr82CVPPO0XW48nUqIGKNGS2R7IwTMMnOpTMnCFWKCR96nXGmxeR0D8FxkB37yvxWza4ZXIpnHGBY6eU13MBAoZ-3aZ96ZvIdnqyk2Zs8UZDV6Ap7oeip4RuNZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkOCu7yBXV3NtLjVyaoft-zKwU21ZkvQo4GbPONU56NDfyVNqIcKnrLEuMhJacXHmhOddSzI5vkodQYuJcNj-4T7hziwnv52P92EIHE9xtg5jmzqmEmMJSdnpHncRIk4JylAddpCx0bMBMfQ_q_lyDxO1bCoOUT-d48Ve9WLixaDUfS-SkHTtL2-zCVzohZNNHVedphnqx4AtSkuSGLsJxUhwqqmdJ1oF9WDR4Kn68V9iu6emnlc6aJc6upKShDzh32kT9kSvyJ-dHGYa2dxtJ_oCPksyrwePnMA9MBE4sewGClWZH7E5tR2bqdHjFozbld2sHrJRldhM5zp03vsxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCimighDqEbK4KcWwYIUlM0zQeNqHSggpaF0Jv9V19FhIZP1-zg5mO_NoHbds7l4_mhKQG4pJr48tbuDx2hy9xOztRyFlGr51MmUULsxSE-tTFa9m8XOMNdlLzP9tHuaJUXpArhO0LhitN26k1_4I2vwEkQxNTEDkLLcgJfHEWa-6letgxWGb8xgNdaSuUS2is2QZJNNG7yznwhlk-ind27jS-fy70EX5PQU-fQj0A1mf10tmSGcQibF0lwF1ceCmT5nx9vid580mahnHGQ_GRuGz9a7OTzYBpKhuBKJOKY8GQ2U7DrvKwmTwNtWKI5YtVkPCQbIoD83ID4ACvNlVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7emg1wFliLLPVuOQYzgipCqrU0ys9u8oabCbSPg_pgXsTqApmrdC2i0FUGNCqwALapA5jZ6K_aFVOfAwbmz3oLGb4UYo1vTD5QzZd5fcrPhoFf9bH4h-xQzKXYVh4Mo2MWTmhv4-Jtci0oyIHKvMrzDzMvOMxPcHlc-dUggrj6e6Yj4srUODYFC6FEjLq7-rCVTY2f2aUNqeGrLLsbrzJVE3GzLQTREUzpWViT2TkoSb_mNTBo5aqExMdk15yh9_rzJJYTRhqMK3xvulEFSvOMyHolXY0pQjIw2LvIC09mdQ8EzB8_vrZE7_2I902NXmRdO8AMPQAkVidKVVut01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRt4xY3OqOXEXlBKndSTHARQosW1T6evWeSgwws4iwO_Eay4oJsgNDvTHhgKR7MBxy8-SPwx934OKRDFhjHp2-g7z6X14wddjfMVAOPuZjIJhNXUMghCPjp6fwNrNlO0jCDNSoq5nvjNliUYLOITbd1DVgFGaA96mEgouZRf5Yv9vPH9bQnWrEPKS2HWyNLvQuXukrda7NIk2irBw_OFMmGdm8hlDHuEHw2cIBDrt657Q9vlMdy87DAyNSmCQq5dXMGY8rmOWk_NADxE89xKMNL1vXXU4zql-i0Fr1sEfldatDXGkM8pXrpMXmHrIrb7szhcs285sMdU_7HJ86W0Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwSuIcY6C23NHlymejS5Ua-9JxsnJk8XAMs5eCpmBLdK_-Ca0rrzp3YmaQZZfUcH9JutxGfMLgwpYOpWPQiSN9qWKZwP_YIAJD0hnKMFoxOkzXID0rgKGkOnSC_rQZSER_lTJtKPieQfXrAps8tKdq3zOZ2KgpgBpOQxNkTIe3a3fJiCR5UZLqcE62PD3ZHstzPcQ9WOVgy05UMv3RE_fbny6MF_CrmzuyoMjE_E0MqD-tbniV9iqQIJbDbfgBKZSgemuSE7KlnPYg_2c0U-6nRy6qIWzQC-vvipm2q-gaZu1r2o6yiYmY8oWLKA1Chx3W5laM5b_x_i9tSFTeDm9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDzu6VlcDN8vaj-5osLwOr9L6DIddlaC-TjNbUKqC7prAzz7urbycOqNotAkELfioSBZM7dE0XK7B8Ogqy4_Kr5uXnrRVJHe9WDqpSf2pGOahv-aKk8MlD4hdL69PVKOMw7Al7KIhwZlOl_6iwKzs3XWyXo4SOSiOwvwQ7aQo1_KdYPU9om69QvxeApHiTXJF4d9hYCDCjNS78BwFP_TzdIzMevNBmy6beGVP4RvJgZY2fkptRli6Vm6_5W35vq4Y2sxukprCwVLdX5ZtSmywyCSSjjXXDAS_ln9dpxKQvDsE7mdc-Tjl0SS6EtAw1XKP7SHxMEDSHHg0mWwdvRzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXPukugT4FlZmNPCRRKy-Efyiteoi0s9QslQSsdot9SWkOBAci1avykWXso3FH2kZf1f5KSWr-f0BJVoXwQqXSaWa1lGADoWomxtqDq7OTANy6-6QS3IgHZ8GyCC2eFPZASjDXVETQbPSdK1NqAl2Q95BHhQbcoZA-PuJcvEISEZ0k_nr5DLwPtmHF4pOShXBvyfmigDxDcylAJqq0r42Pdfqhnh7LmWlbw41c9VQxN0q0SFgcR-fwYSl-5zg5XhC6VbAeMyfSi4SCeVzGwCD6JAuuvSlEAZPb3YYdipKgXKCIn5bN5BpuuPFIZC60GibUjL8jPa1X3Iq8i3WFut4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWzMrV2AT_2V7xaGkocjz9l_a4HVzlUbnXs4QNSwse2pxVB--Wmd9Yeb7KzQT2iRo1kKiinYua4TnzOLc4Zu2XYCWCahNVFyPd4bXET9sgMPrG54Q2Dkejq4sB18QK5stXyK7UN7IuJoTqXpigGSbwI9NSMybGQ8BcE53JtkH_6OX-viI5Un81F8ExP3NVq8W2EmAzjKgvH993FL4hMqw1CojKLBz_otFSxdvG9SuaeuX6cufsDUWAQLAy9GD6nph1J469a7rljGNIHY6SxaD2zsNd2pAZzBTUTQ4qayHzG1T3_6buP97PYdyEsTtmJDcc1vFnJXE7PQ6tajTiYhZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSmvmntoRx_ic6IRaJlpyuSndBS74AqeCxeRo3XSSwUM0qZXP-erh5YpNS5rWMlxG84GdZCSW3GPHpZIaYZNDrhRf0wAHAWC04ITGT-IiVe4BcbnJ64esnRccHlvd4BvdVxQn8za0D6Dn4ygkbsFpajYQfNIHpROIVViDE0z0xY7IOEm1hRZlj8TCbmlvJwX8BRGrcyr-xcl61EMWTrpwizS7XkqK_wlXlYDuPhRNv4ig_y5CBfkQ8GI8p3-xOVHAFXOWGhKvTEZT9XGh8e8ssgz8J52kSYD3jxDKTLrtUQYX-ZlASyPo40mpnQ0Uvd82Z_U2cCqv1-YDXa_2lW_6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVOJkoknxSU9DIzIAKy1hRXDo9iuoU3v9PjTbG2RC1DHhw5QLMcf-3O02O6JYGM9x__0xq487x286UaKFHWDtkUOr3ssAxXRvy3zwR0GJS6R5ZfFKsVP81ihwCYZoS961bJGZQFQ_nVF8z3Ue5HgzgUKXwwZjI2ZGoesLpbrFB7h9TxmiuYEv3zZbbCaLQZzSr2MEL0E7EU0L1_zUITREGFdipO1MvaUWiOMAfCDMiEI9CiK9NQIvd5p4zMRvRL5qtwWXLnPWWFZ8H9uyWvBGVWoYWNLflZPnYi7D8Zbq3X0gl4_-lW4TzlUKA-cmfNBYKJk4ny_uEw-7_x8Dpam0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeEdofSnauN4YHic1t6121J3UEUbZOajlsSEfp8Ys28bPI50pE5c2HEomlDWgeMh0wZYBrVQ08iqJoSY8X3SA17NNpRe-GsUtNnzmWhuc7p_QLp4ryoO5alrJu57HuXIV9SNPq1Od09t3n28Wr8pACTnokT2JfwLbELM3wRzvdPsOjbkYaHktKDxWjNfyBeJncm17UFjGVU17QzDJfi-QgDXNsHSiAqWMGILnnhChW_-JFvT0J7YZmgWMlIKjw0jqwVzqBo7uIxjRPkTz7VjZuIKRXTNz1J3DjJ0JmEHmhRc3eAsyakCHV05_QGDdvsexYFMMZON1v9i3ExsGy0njA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otAw4ZWvnPRZVC-SA_s6eHjvkGtzIY3c6Rkf5cFWe4wZhqGm7MW_HkiicjjwVoj_J3-Tq8PeQ7pBB9pGxqIk2__FH5JkGY6xhpjs29bskrC70wO2C5GWDC-0uP5spKhCFgbk8kySrI9779QBsMtbsqqxnZdbh-GAp_FeYAUSHAdboA6Qu63VU-c58i-O8zfnWMqlf62YsjXUS_qvws9Bson_qVLwf3lCtj_rH6HdYd9YPqL3VnYc97ZGmM-wcDqrawHaFiQKyhpOBI_BxaQ3XqwibWjJaWoZWCXfjenwlYHRr6NflUdSgSu5HjQ6nxsEoFqKvErXLzJd7-hOZoiF2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9iSTR79PX8RKfdUQ7lSUBq2Q6oF_CtdKibsnLxMhgEZuAiTyQCSokjTuf1kaeoaJt-8-e_o3EKgBw2C-2T3dZG4JQ3ld7zuuyEWrot3WcApl5tA4UAoTJSSrGAydPAFvU9Y-k9HQN1EEhYISd7AbAcYeWJs5za6nQOITTitTVlYEDiz3CffMUND0R60JrupG3Q2htZOQnGAj7lNKIwozQr9Kds8GHX8-F_fjRhZ4iJgfISE_x_pRzydIv7neuChCgGQy_JDKTLKy_D8rZds4p0qCkUXPdWOSZsdqcG-BnSsiiQx6zsqYeNo0D6vUO0A2-XhpQIcva4gqbER049UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPAujufZkSkL_HPsrmzetxgCBxElgZ-SWFkTf8eE97NGMz0ZNntPb5Uz_vOOrEbZe_4-gL-WpKlgeltjSFW0aNzz6Bqq1YsmwqRHcwPdirocqq86IFWIb3w1h13FIACwwp-xAr1Zb0_8julXhkP9iamCeKcC4gEjPbwZWE-FPOiQoGrabH3xEeNzxCG0W5RcxtvJa-49qLBVCBASBMJzRPpONruZlPVdmcfrmPtLVCMUjRfOptFClh2ynWXvCoQAeWf2fNSz1fZkgYaWSF-LfuZqwXl9FsqAqpJs3OaLJlpB99l1Y3Xnm31lw9bd2iLEFi5kxvxDaD2YBeY0ykc6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZT7w8JjyDg3VRi7RhAJHw1Br8Ey2Go6Fx1Y7SD6SopkyZo7a8EMr9FaPtbOFZ5aFG0IJVOPJBDAS8DUUcV35Qubre2okCIBCmEM6Tptbt1JizBc_IKt5fKOCUQnevtMCNlQR3AzyzT1YyA0tB0YGYpFI6CbX7LPPpHNOKM5DLEDUhaDrfgL8vwtIi5AX6xwBniTh0jpvuTXodpK5QMjRDzJY8IIXqtM9aeCBUhabzyMBN58datuVTY8e5BVErILBKchNpGECwfHSKjw8uJVzp5ypZxWIzUQ0vDq9p4ZGr7EtRkRe3zy04AvwjJTJwQ7K636lHn-duW1hrOG84tEJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDBLHyG_Iq6WmOeQ-w0YAfEqiIE4idVNfObG8BUJZjdaJaT4WQyiFrDLUyJvZty153JE6mcOmBJhpaIMIMKC5ytbC52FBkHRAr_n5p3ANM2O2a2a-PZ5KJfswWzrOKbMH9wzEJFEd3OgN0nWId1Z1s18kbz-Isa8BlT9AcCoAQL41XudqOo_5frXL7T5YFpd79_h_IqEJOkJwP2H0P0n1P3RB_2TK3iYSDzdUiDHWFpJPg3D9dtnWyVA7TRN_g5ZZGMHaPEmZD6tQUdqgVsinHuoTp_8jlLtCwaaIbhZ0trM48OxidPUPpOUqivbQhWA5IWiE9CbQr-BlEWuOzQfjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_NbLjv8d_6WikA_7TmlP_kkuJYnAy-NiQCK2tqA9f1-FtxSxWnu6GLWcFJ84DHlYLwlzJSg8mM8oUdsr6-qPGlgf2IYbv5yuytmR5STNXqZPoPS4Z-EQx-L_R5jZHEMVlqdWE1zmXhkFF0Q0WSu2_eP4tKFXEgfkjAfuL1zGNGFCRZpQC11BN9Fe4krz_7uzj403McDblM4dIt_NQk1sY8XicWe8q0mmzM9YEzYf3v9apfhbPGk_LY2_H5kM-Je62FCiM-hUIrAZo_n1wNEi5lqfrdm8TjRT4WHWvpZKZZY77d_DH_lvT8mngVg1L-Dowffxok4Vb8WqthA0sauJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmvTK73nZm-sVy8Msp6BrC_YsrI4YxrfiLTZxrot-4CgeC73EnsfZ-CgjTKNpXG6U3Wl81-dzYqGzuBaLila2NV1VB7l0yVVrKqbUOAUcfINTV8r7-75o1kj294AuNWZw4axae5cJ-iBcLY7wkrknaz0CTr87CPsoXAhCb_paozLHj8NhPQD3gBwGxxoMpUSjukw6Cuv1fT8_EpUC7IgtaQ_lEVYhofvsYC0xaa5P6RlCAvyLvLrThMfhyhnD_paFhcq5BB6w2-tMhdQpstCoR7Bvf1ScMExhc8mq7Uggrpf7a7PJ6XyxlyLlSyiA0K9Q-LjgqNHS4n0P-HPg77hOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXME0dpdXekU-vlnpGiaz4r8b5q08YkLhsV4ny4fx6vRQJcOiY1ppCT0zSw8mcHuOpPu1e6pECTexuzVECT4MM9hZL_hw4nYZrpHq0FyJqxr1Z-yykVLdEf0JN690f6bQCFCzIH8YYY-Zvep20sKnF2vV-7Arm1hvdmjjJsri0E81SLh_0PFY5heoxpTRBn0msXLa6I5EeKzToSVVAkNtnW4xx3EGpQxE71dMNsoZ4G5JjkuaZBLDAT2JWHa9JGjBrmht0ngPr3O_xyCJNhhqc7lUHoe8LWunBtQbLcsPmDOLO4iditfi6jCM--ZMazy0VX_S8DolwVH-5w4HuWNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9Q53vuLVvCiPtf7nwDNZoCIWzH_96rW3L1RpJLbVgFkrSpxOWOjezeOgh7MBbeo5huL0gg2PEFNXQnC6pJcAb8MiL2-aVpJTFmI1T_YnDAF0ZUZ3D1VxNNzbsZvaI-uHWwigk_ZY35NUZXw1Hx6uhhI13ddL2jmFqEbuGZeeOA1cTezDVBPN5WIZruW2GByQpxkZnnfTrVqdVVJdjZEqg1mNN_X3yaEmG99Jdq_z-BpRJaxbDtCa1PH0g2IXuX6k2km62SS0yE1orKVH7KIMy4qKPiutaOkYJmqkJhwgTOQ24tWkNv5zdYiflT6UXFHry_EahiekwsSngtgKWitsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_kdQ_av3L7kIrvYKWRJddzeyegM91ZE6RDNCmvZnCS2nUD_s9Ckl5h7H3Zpd-6gREhk_xdlsyf9rU7CnFsbJUcd3tOON9gZXDTZFkKpfVGeSkvG_WWqGHkUWyWPzg4e9zLn8rScznVXdDymJnJQ2eoJQOLzSKlriAWF7wZKDs5ULnQzbuFekwEtUVUisPJwYcSr5QtF4Cei_TpcXR_n9c20L6iFV0M_RluDLWDl5lw93SwRSU2XFrYF5EgPnz2itKjKafGLr0jJ7PRT2l8-QukTAAiJnEZc-bnEC5ydw5JhXUEhtFUx4dtaf3-Wsfhk1tFEO8pczs1R4HYlqw_kuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAwwN7ucloQTYXKIQEsObx5FAllINBFbBTdf4ugjk9iwKeuAaLZGcR4gsTowBp4Uw1KU6bSptepeMJouyoifU4RMPJAlpOmmd4komN_eU1zEHqg1WtFTWIEb9-GFDhYeSO1mQLUgMjYajLDg7_154oNFviIY-oNps81PrZ-OkXUZJeMW6uWlr7PQyE_mW2cP16qm3JhMNCEe9XwJ2a_YXSXzaDMilBmerYRHTd6B5xWjys2LjFFafID8NYzgltXoITHQn_VfL1pNYKiz_QBVsba9FwOyRgrXl03h_dBokpC3g_e_Wh0cD0jQ2gRYg4fVyrv6CjeJoYXf8yPoLQUBAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_u3sUgNqRYqfcRt_90J4FclTKpYSwTYSLtYkKyZK0OCkGEBxOB7eKfJ_HVEN9ku15gBgJJ1i_uNDGstns8q76-ZhatdGgKU1VP5u8xPSRmTQoROajTyZMBvL4fm2Wk0U7UIiA89slTEP5J47t9Y-HslhMDq_HnAd0utIkVRTFjeoh0SFgYjWIdXjE8SBeeO7fPJLxrnpSVnufqy7sDLpmdbSYYY_cqK_NfAPp18LLarOZSBSuExWuCWuKpp3MqJFFepQTJG7G24DasooJpcYJYUUJDRqmQlMCFVh71gAzczWYMhq9o4wrC4_NjRAfmavLuKP4A8ZVy3Tas69Xhevw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HygZOdgTMQC6zZcUUY-zAfdraFaKMHSNnNzhjsAYRMo6uU_7Pr8b2TAmONUX3wHD3TKSlw5xIVjmGobnn3vioinD7q1EaddGtai8LHac1_x-WcFdJ1DlhTFONqbiifbg6ZX70HKtJ5iCbAPmoJHdTyjwP9iZ8iMKiguB_9_ZNGNGiuc-1clxHZp2i1rn5ijD7VV0zR0UlucJ2Avrg6d_cIuzVfkN9kWws9PmTOu_Gt703Ljlp7Iu0sWkg2OMvlL_JhsyCViRUoK35hAPaKy89L_sWR1yu4JA0Hm5gLXF8ZMrPZwsVvH6prSm0shOrwcg21b6lBgDr23eNMN7X94qcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCT772kSsSqUfyX2X96f4fEERQ9E0tnEAY4zGZIHPiy3SfcXifpx8FYbWzvYA1jHkvBTqgo09vWJ1Nw1mVXWMsAwtKyPNkZi650RpOAu5zEC2OQuTmQxuYQt9tkp4ffikQR_Bqtvfa0_oZ3EUVfRdJlVEM-nf-JE_Vmo8x9sHuFMB7cvj8s94nLamOhg0CX7V-eIvtA4aJlzIfHO6UFRG0shMVUty4rMtp2Bl5LTorbg8czTLUQ0KyxeiNdxumwgjLLupWtNr4xzj-nSDpAHi_jfkmJk2-y1LZx4G6uM2LBHNlxddeLVl0KTT9DyrH9sJ8Tke8UXyGJH4mxESd7Gnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr5oh3U0oR79A2Tjir_cos0tqAismMa5aZ_mjzJfGyvhWIWz1ve0SME6Rvfz3yxfQZzxqgSENb_wOkiYibEa9TllZ40T1m3Hg_3Rt0an9P1ZAG-QqaFsQiq3RknhIpGtdT-YHTbMhv6JIeY7GwX21AgRnYJdJfyum-ufTWY8rYNnX_LJOQny0VIQ4-uP1gzFTfq_ihZdpBHyLSINFTQbceo3KfS6H780d8hvGE8_AXJuXNykhKxYlUh8vS7btD90TR9JTnhWEGCCQoKeX1Zcqi2Riw0od-G145CamJFIeMqmxiAaFi6eILGxvqZGGvvrkjyFugiGnZmqrfwF3OgwXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_HuofE8n0r_pV7dcygjBei83Z5DSTu5c7ue7R6sRHJYX0Jandi2nyx5oHVO2xIfHjR523oxfL5THwvlN9immjtpZhVFYTTbOlTYfIB9USDz8n8bt1jeV4VY-H31yEoQw9rG5SQjm17dgQtEuEsYLpGo-Edf8uI5LBt-pitNqoQL6DYLsqh6AaypBM9wcZhaU-X7ZqyDchMRqIyYJ2LMGiOABYg4hyAjLhiwJQbuybopX70rYEQiV1h4622VPvJnQh0dPpg4kShc9hDfVI7WDqeYfhewPu2ztDg6beEkEjcw9xscqHhP8t5_2ljA5TMTrT8cB2K5N9lrW4aaD-gW4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJ0OVniK3ZMctw_NYhvMod10gCN_QFgXY2VaM06UHTn3bWvXjlBfD3Skhd24FQuaPUUOnKTfTbQEQrhsoVk6zIGktj6Ckm4aC79WtouAbC-IOfhAVd7COBv0ZhH-Le311c85SXowCd-ptHtu1N1hWC3-NDhXP7H6euGK4_V5YOWULjgGjtt77muJu1g248WMCpYHx8A9sTUODj6gZaG0AzUEMIdA1o98qpiSNol5Ne41s2nvOt85CGlch64mx5vjj2thRUt9s5PCMPfSj1JzR9j3BBLts4bUfn5acBEQkOSW_lG4A-dM5FEMnVqc3noIJ-N83T2Fqgg9QeYuLacYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTx3w6f_Ml5D3qtvvM7-DnILaayA1WHjX6u4xGU0uKYO75rv_-0IfHbq_3f7jbDqC6IBYOcwvt6xKwZdxPftgsE7_fhDF1eZ47M2bgPpO0-6MIxwUtpnzaYAbdJM7gVuFgDY_iKf1g9TI_vTtDefifCw-N8pqFu_B0477t2mMoWVXn_04wPjx3IR__00QJ66xIJMbU3ypX54s4FXNfpkfKoZZ7JFPOI9AVzk1_GXAiFFH4xgG423OzGJmZyd3H6DbTpSDUG-qHcwEQmu-rINx7LMiYJquHWuwrzhFHQAhXZhoUbgmZ2fem_TAo2fXmg4amkZcYw8hfqKBVQmdjP-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUk_qdl7qQ3xd9aghGINFwfAlPv0Ek9VroCd07nURB82rF2zd3RGVnNpcsT3m1BxWnMiUDvxqvFEb8HoBiIL9ndV4Ggxs6DHdr24dOJv_t9RIw1_7Be-22DI2ntQUBfpDAuIv4ZwMFo2dsJo9nUuRpvf0TxsWnCbpdXneZV1ztfwymPqVNpvDbwGq72zZpL4sdvYsN_cI9R6RA5pYV6rcwHBytajypE6wwbDxwNaNsdaIyF4WUHih50tPAqVTdpgnCeS2T7PyO1krsRQfIO3cgBEKd6JgBd8iu2LbM3TH6gkP8oRHjXVUFxKgTFmDYRxzFZSUpgAfcTq7LuKUQaQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BipnACOB2NhdE6W3-S8TKMWx2nBOeECL6XLpquRtqUeOelZ6-Drc-7p0JPwshaZWJUMBEwrafu7_8nIpJvxpa4-GSiWRJhoo3lGyLIXUXff3dWLo1F5SPhCFskGQ7vvMrffQh_sraWcb0vEcy1SwSN9Gf3zHpDAtzxaXofXgQoB6P2RHzn3HuiyHKLIpRg_qHqWZ2Zi0hPMao-1mNx7PgRaKt8vGVmGQNnpGvVF7wkrFt7Q_WxG7FXlQtaphjxPKRaXMYQrE_j5EueESDb6zRi1uGrpDiE1vtcTPdhzw0fU--2YXnh_TniiD4PcOM0--eqqNqqelRNIZTuaBkX9gfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab4Pt9FFFf_oX3_2k4TpmQkqhwmoF5EO_rLnRStsi4M_5DlbBi0gWpleVyRbLJmAYwrNylPl8SxEIMwx04M6osjRgXLOWORWXtF1OHOJz7rik086NszzE8p4zD9LEYJu41KyEY1tyi8HtqivcFpTyYdxD4RFEQDl9BMvo07ypJf984NDhnqRKPGVbGCF1ZdTqHIP90fgsDnuv0cEYU9LQPMa3Z25ftPMq2RUPaPyIz9Zeddgr_AkeBCSgnBedkJ8LhwmS3mC_2htluzkBwYt38I57UsAxikLIjQB7OHzhVtBFQwXH8RsAM2tcOVUhA7KB4I4zoTI_hhtXbB-Fnfyuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9t-qPA7udbgxFYnSlPi29htPkDsIQfawk3XhED2vFaO7BxLQC-n6DXK_IGZ65daGQGcx4M7RKT6pm8uSem24Ui-gUv-JsFmcSVfi3sh4y3O41PmF3cHdyXdVyY1pljz_B4Qj2f9D4EW94E99KBxaCL2CGdCi1C5Eg3Cdbjp5Gm-ouqJlDswPG2WNrPOUCa6f6-_8Ud4VrPg2kwlSJJIVJAgIkF1KWd5HDzT3g5P4F1txoflOUhWWOJFBzpiLV9WZpo59iqIqa-QVKjnufDRArENXevmw9AvvhzrSwKyFsiLElAPjDE0RVCwZNncE8geDOXlhQvXAcc99z_3kNsOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRdhWJjvSv9U9xOsDFt8NthRonVHuqpO5kUVig_MreKaf8wrCWWr4hnYL3wp5rU3yluhvruv6EhxKw-dpqq5ESfQSJVIyUItjARZmE37OBDgX1AsiGUMudfjxPm1UG_knjhdpCAzVz2xmLowjTPELjhd4OcdvmGL3rVU_QVJYUICHUbfxA8xQYyVJ3G7yL0AsKQlSiJGypy5ifmBoJTahbxetJh-CFeV9fBzuUitkflHb6rtjt733uNjMAk1GnQxLzZwSxWbZUYTd0uN8LvtRMahvbHopbNb3oqTU2OaNHci7HVyNSv46D0EXAxVyQFGjcu6101-Jenn_EiG-PhExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu6WrVMxEeQS0BAPxX_EraszKmymXV_nA1XlSjc5vP-2d9tups9J9YOFZD4PUZ_HePOF1d8rFbPOJSdyyJJ6_nO2OLLxKRlYAiyCMvfUH8Me8Xd3tcLQwPxbTIQkFezfmC7lzAgfATy-RxfFG8Di0oxpWsAQDYMWmuDdhhyAwuDLeo2tQpfcazVMmI5kgtJrOQPnzPwcxqezDftMfv3CX7nDfHLguvGCCV9WJfJsWQwInuyGEzBE-wSLZ7nNExX9ShWGybnshc7iaj7wzxErBIe6QeiargdxjPCJBPNOLheR-5_cgs01z-C1k_xDqNCx_fIiTG28FX-oRG4BffOCJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYzHf6DT9zkcyf-Joy66LDQJmUkow3ZaZqkz9Q52ywW_XDGhPg5T5W5pswqMbmNVgvkPL_p-ZtJ01rApwlBKcTVQ8v0j2WUv1GzuSjnrzVenYqfduxhQn3gWWmkReUeTFD1eWPZ2pM3ve3x1Xhy8qe2QJ1GgS8DAQlNgP6ceo-NOPwt5m7ycChIeEbSUNR8mf8pOM2_zp0zkJnB6CV77tomIt54Di6j7d2Vpy-AB1i9daWl4gQE9S4LUHaWsIzyhTm4Hi04vlTXWZ1ru-loqjW1g0O1E_JxzxNAFysejSdpGEr5-dZlRLs-y1nEu4Pd7LzZMxAakvwyqHPF9HQMFgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKEAvnWhDtOO1bXtKJMHYj-ojhcHyGtb-pBFfItNQ3El9qr17a4jvDNAg64C5iWedF6SDFc_pHfwAoubMsf4qRyBtyE0_vWxm4jkbQDPcJ1Kf00bLkRXnHmipvT0BBR799ZWc17MpOCToKIGcpiH514WXjtb_u0XIZW9LzknnNZ1vZv1SoRofGynacUaP52zgUzQIYoa7MV0X0JZbvc_ceFLBKeQ56e5kplCLSs7aUwBaR68DaiCdshGjR5Mn4tR0S4woxQz8n--ZHkyjBd0JIpiGKupLOHYpJbE8vO08XOEia7FhUWAgvx-MD7vJ2JiXaaILgtqee1cqeUVq6vkHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=ehgM_P-5CriUAqjvie8eUIkFTfGB9fgNsHrMrmvt1iMtO0m65cOWemIZU0Aii2dyqeBE2QsPEl0ryPLsX9iBv5UaZoQqBik7Xwq4QFi2qk36ndJ5aWOQ8CIqK5dRA112XQWiPaQMDHX_2182tZm6sYZzNqpV_-iRzO97BnlgQQwm-OYjRJZhqnlli_TsRRAmaqSxVjVEeERO31SN36NmxBhWO3BgBKu5Jm1Kkf2p0qZM59DXtbe8UZOPniVsEnr2F7Y4cPasyhq6pg6Yka_w5549TbPZacxLVbql-23IdRiCRD5xeZOq7Rt4VVnsT2O9ZVb-V9PMV0rsgkM2AulU6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=ehgM_P-5CriUAqjvie8eUIkFTfGB9fgNsHrMrmvt1iMtO0m65cOWemIZU0Aii2dyqeBE2QsPEl0ryPLsX9iBv5UaZoQqBik7Xwq4QFi2qk36ndJ5aWOQ8CIqK5dRA112XQWiPaQMDHX_2182tZm6sYZzNqpV_-iRzO97BnlgQQwm-OYjRJZhqnlli_TsRRAmaqSxVjVEeERO31SN36NmxBhWO3BgBKu5Jm1Kkf2p0qZM59DXtbe8UZOPniVsEnr2F7Y4cPasyhq6pg6Yka_w5549TbPZacxLVbql-23IdRiCRD5xeZOq7Rt4VVnsT2O9ZVb-V9PMV0rsgkM2AulU6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6wHZC8HcEIkwq7RBcgwyzZTqVrqc-s9wDRLbn8cPlVM4baS7ROJhUoRvsNxVaAXDVwEB3wGt-BTYJgkst2IuEh2jC08UD4sPfACmbNmx-Zkf9ANAq-8wnjp-04raMzCxn-VaLQA0_CzHA6igsNkzqmz8WT93ekYiT2MA-2_kJ-VFvrDh3R02jU3gwO2glqkTBu32vU_lverMoIgF2z_EZDnLANtozO941npMa2N-gAh5oZgX_U2PmUXqHXDEtXbt0_7KSnB4enolzcTWirbERRNj3IoqWILJMOYf17B_rOYMT7tbqNhn7Yi0jUUe3NByRmO47IUwa4g3G2oLzoRDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPbfl9xRhRkTp3fX0UwO9W4U4w3oCd3yH5Im39y_UbjpyNZFYtYk5o7l7StFoVqPuq1wwDQwl4dJocwtrVgjLeNAK2tzl110xobbY4b-HvX_xe39BmMAzi-6b7Op2f7YpvDGNlgyKdWTg-c0CTwgmRGg5LXu8uCVcApj9LGe-t9ul_XNPoJRPMgqJCFjjwdxPsBheH1D48k-Rc8PJ1xmb3TNxOhvPA-no-5Mh1G1ZsIGiwBCBPmbK3f-3lC7H7tTMCfVo_C994bMSCaaxTp8YE2JqCAKx_1b-IoG5pApPRAUQ4y2vJpinUZlXhtnAYb09bLMJb28rHkhyglwO4PkLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM65Ktwe-Osmgw1hEcfmlX6lwhuDP0nOUPmMI06WFyuKY-JQ42w8fMt0wScPlD1fy2UoJ9bCKDRnDx3WwdWoJX1rm19DdAcNfv6kr1RqmPpXjedEsQjd_e9OmZlyVoYisr3lxqJe2ngL5NC-kPQ_VdHrbrxtLINmZJf7dvoN54_0cYLAnLvOZOJdNuy_ImUo4AUTSGgDlPxr3yx_HcE9BJgLjSTdiSAuvC8cd6uthhIHDGGjavxirsH3P-VZSX8MBEBXB1GsmeQp5k1BzzIrRgGJ_ZfQNaC3ie4rwxuBt70lR_8B3giGpMJUcQXCJYeeUCT7VgftOTEuMROlzwQLOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcGLP7vgV1IeVNTokQuGiTp5zXakiskG_FZlQuFNgCPJFWa4RwLht1X7Xz6mp7rCVetoaAvDITc5vHE95sR78vPcxTbHPcyxKKe-poqe6cVzSS6D3zMJSQdj2cqwywbZr8lcY7t5wsT5mRYDrIYAbkAnbDd5z2S5OVrDFFVnZaPuV7QR82b21YwqCB1fv26uA4fjaEmnc6YQ3cPT93s6ei1USTHkEALgBOTcpU9navz8W3X0gJhTk8aZY_z2tZlMly0q3hCd5CK0dsIJB6JZpHDS87dDma85kw7S-VJFxZB3F7Sw1l1AqCSHpMOqLDuVfCzGs8JXKfbmhLNEKasMGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na6-19JE2hj4zK35h5vY2UV7f_HuN5npV7PvEfUkc3C8W6owxAg_3ZfG5pExaPUfCOM08SlVaWcpGh7_f1Kep_7Q1OIajp7fs2qd9dV1i4tRg-k3g6X7zyJWehIx8XedhUIQ80mvc-d6UAK3WQUobopUG85CaY3jIfFaIRG4e42hbccu0qRjvtQ98TGVHMxx-OJ7kpkzZOGbwVbPyFTL-dgdBd2PzJX0-4AMG-o1inG78jmofUr6rupJc6dXoWd3FPV0JiakAAwD6sEPQdIP0zVXOFQLWgr-fcDWyGNs021WmVhJdtHEvkLqokhwXVbXCtyTz7X4aUTuOi2GPGRmmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyukdhs-mrZKYVrZtwRDjL2yXFhYcQwS4xFHIUmRfa5OHjhqhK-_AB5_ruBUvWKJHmn6k6gVyzOj83covJaIlERV_E2Gwt5NmWI-KBQYDIRazjnN8l3_fH8u4YXTgjy1GY-NahIfeoReeAg8CGl3L9Cyqj1BxgZAesb6ENn2fdBXFnXUcFz1BqrbdMhpBRgfwnn_tOOHjpTXLdl1T_WxzhdbLc4J14Ds-9SCgaaWuGpbWS6qzGpibGLUsC_Kk-w-b_5zHhIXMxEAJWgJIWVVFszI39jzLPrG5eSYzFvoI8WqP09i0bEI5xaXNK3EZaxbpic6fgXWJbASHQNPvT_PCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
