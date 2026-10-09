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
<img src="https://cdn4.telesco.pe/file/UEq15s_h3q4jg2ZcFQiPxbi6aHGp9ZBxgo-KHnb8lO594LMOKdRJkvzIVjqWrlQxJdD6tM-hvT1TBgmIUV3ygmxag1I7RCMs9adT9YAbvV-FTd5WjqTP6YGYdY9VbtNZX4ZWAKBEkqlVJGjIEqD6O9FzUdRtuageomeiG_KNIh0yQtH50vK5fOV8OwTyBKEsfW0x_K_V0gCoA02_ekeLXDvctVMYg2qbI_nTrafUC4IzTEsDMpZGivQeo5Q7ldW6B-6O9WA1zJn80u2tZ5hTBKwh4sRPiqSiZ1l-ZMvXOCnVyClZKwbAj9viUm85aP7mHWCUZzXRhZ5yWm7BjyHQaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 11:42:18</div>
<hr>

<div class="tg-post" id="msg-8048">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
✨
ویجت‌های وب داخل پیام‌های تلگرام ⠀ ‏طبق گزارش‌هایی که از نسخه بتای تلگرام منتشر شده، یه قابلیت به اسم HTMLBubbles پیدا شده؛ پیام معمولی می‌تونه به یه مینی‌سایت تعاملی تبدیل بشه. ‏پخش‌کننده موزیک، محیط اجرای کد و کارت محصول، ‏کارت پرواز تعاملی، نمودار زنده،…</div>
<div class="tg-footer">👁️ 408 · <a href="https://t.me/ArchiveTell/8048" target="_blank">📅 11:10 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 472 · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 601 · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShR5cy8_V2ugrIeU0mnbbyrZtS4lEsn3Xp_pikgjFG6lTr2w5bawaj0vgBVKwIOvd2beF5-mQgBm0pQSf31QZ1I1qIhn_35MJjc0pLn418ABjwR6_jHniVboDdEvaGL2KzThKHPNb1lyyuIoKg4xk1DTBxULs1wp5csrPzNJMS2llpwDDecHHZQY0g2QahDMCPq8YSY7MYeLa6IMZnwpXCvX4KfhXiQTpLW4ZdIhSAOBdCkSNIIZScnemR7iNjQHyF0M2DYgbqJnB9_dU2Ht2dgIGLgvQLoh-NU1zB1JboLNqxHGY9o_nTVSW86GDNJIQAwW8hxFAsN7JjAD2Y-Lgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foe5daYhN2C9MWNTMNDGpQ-3LZeoM05x5v9oXu_xll_Wf0vCVUh-VBPaXQWBIOvTp3wbvqWEmSYMjBN7ZXV3J3YRDJnAbe_VdPkkyW6W9By8HNDMaNTrY_1gzOMp9FUa64cmYS9J6Ae2uG7oEBvDcNkpuvfgF-OuN91Rl4vLcYId__TV2dTamn0lTl4l3aHDiXrD3Uektm4IEojo3k7sOb6vqJQp3gGuwERYkd1865dK2mr9SiVUmJfxZa4eMGBcQ_WCgsOmLzkQu-1XI4_FqaYuDRzuwG5qL1sqI2d8BX8NmUv7cUF0ZymYisXqhctnZM6chAL4kEZKtEZZKzdh-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTRMXsdCGDj7aFuXUZKDOMm7hpnW2qS8tXsgryFD3PHCjdcXGZ2p3KyLf9II8Sj5xIFz_sJK_jQg5UBp301tbZsYxrgBtzz5h04jn55Rr79UHvLOZiXioSHYIlW-AxizbLy7dQpYB_gnH4WyxKdGokV_nB8KepSF1ydIQcDH1qM3axL5WxWCUncT3bRAmAXYTL8SJd71fA5l1ywFiJ3jSbnRTC2j_LjnocwAW-GkWdIYLJQkwxEUYbCUYq3PZILjLCxwHQCMGjTFcxrwBMNo2V_ET21Nq8H96jydtNydvQMamaDfBis_H_yUjp_LETygjTZrjlR2jg3nXlVDFvnfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=eA1mhuIab3vdBitxC_2b8ynnPWQIKcNMEfGTcFdNZn9pjJPp26zCuDJPSx04wOCyFE1OftBYxuYm7rzEvpej1RymUNHrsZ67DLZr-k9Mz1kMJ2l7iJLl-fa9zVob3X5ytVmNP-i09BJ_AtTyN3YmtOlvG11f_OMfvFgRnPi5Yw-MSO8uEbzEe_L74Nkiuaccufs0TX7V4v9Is4nBcMUtP9sz6iHMWGotdHJB7Y61sur_Aki4-G8GljVCxEBUhnhuD0G8Mf4H6XO4QEsiXvEa54MHVd-p2wxwEL_UztkicBFgLUwSmyYK-OBmmMV7ILRq5fe8UwEXuslMqToiKlk8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=eA1mhuIab3vdBitxC_2b8ynnPWQIKcNMEfGTcFdNZn9pjJPp26zCuDJPSx04wOCyFE1OftBYxuYm7rzEvpej1RymUNHrsZ67DLZr-k9Mz1kMJ2l7iJLl-fa9zVob3X5ytVmNP-i09BJ_AtTyN3YmtOlvG11f_OMfvFgRnPi5Yw-MSO8uEbzEe_L74Nkiuaccufs0TX7V4v9Is4nBcMUtP9sz6iHMWGotdHJB7Y61sur_Aki4-G8GljVCxEBUhnhuD0G8Mf4H6XO4QEsiXvEa54MHVd-p2wxwEL_UztkicBFgLUwSmyYK-OBmmMV7ILRq5fe8UwEXuslMqToiKlk8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpO-eAzWOPmYgZNcmd7C9ve50t9qN_VbYuGuCC3h3L9ujBmxx4cMkVkpgYmpAEPtQsdZrqYtvUdsmyWTFp1RIfkpsFzM3J2nSS0TwEiWEGYqB2pO7sPYMzbnVW_7Ts1aGFvDIbaKHN1IK7P88iLwbHL5k3ppXLvTSPrctIT8uh1epAw3XAaLzZ4M8ZV54FYWmaBEXVGogbtUW0zLQa--ZdFxIL3UltYUINGurr_F_PpX_Vna3tMycF_RwCdQghsk19h7LbKt1fKPvsHV5In145wNQ8q9Wcr66AophdCyjWToPxAQ_qekMmHUmWzqzgmnLM-wa5ElVxS77KJAMn7kdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6h2FkHmP3CcjsLpND-nRiyQECWVPnLoX6EIuQpiA0IFhHUkcEbzd3uZ5xf4ABWCxsvwPZ3bhU0xUCmZMae4087rRh8Noh3GILQQlAtJ6BKy681Q4wYZ9hcVJ3fAvKI8Zyz98VxO-vGlOANJbtu2_Y5uRtbkTKa_13LSvmUPiLaF3KThvoT7-7Q_TPSR7fixbhFsMl3yh3vlLQv6K22DZN2NnTVxnbHjoH5Ih_PhUXuN0Yl_3SiMIi3QesTw4kRJUUdQRYIu_-2fzprQ0XEAXxXBgpRVSctk8df-bswu-RlemIuU3F_dMtrg0O4a4DGpyxx7Oyq3JU9cwuUEaR0YEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rtp8Lvfw1eW2sbneY2kIr-X2dD9oPP_kZyu56-uvfE-tT4TyCBKfVriKX0sQlt8hDxLDewd7nmq1Ow3MkEDhteV7kYiPCOJxbL-J2MDbduvlqBGOho3L00VDTlpwIS6QsDzYJB02zrOdLRcNpEeg4sn3vJHalEtPH0HUidzUdvjmmYT-v_2eRw0qeQN5EzT7EE9GchOa0-MDECTXeP7zJ2jX5stYbIgH2GLENZcqGPoatZ75I54U89Mh9_uQpgm610g1gfAqlfNbSKX_JMgn14vkvdfllkNnyDPuSORXUbLK05mK1ALbDSZ1CBUp37ELOnM8tVs5yRrMQhAsNZ02FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTfPN90p0kYWgkKSeaZDcxwhWH1UUoJGtEFishjXnOupj7gjmv5wNdsqBjnVJHllxwW-FbaPsBQ8CLgwz1Jdm9KrqgR22vsUjlK3f_GccbgKl7DCyusFkzUJCU7EA6_Mm6BOZ5CpuArKYLxbQq1bW9kWdGKzk5jZFbG7hUaQ4Csa76O8oSXT_BNiLXoaSEUw43UZI4LlM-Q7Hvcn7JrXsQrlCjAxD-XwymiGmvtrsw3aqCQ6yzYQaLr1fOw_Ab2ljHBr1PEAk6EliILkW3w_ExT_xPKe1EkF37UtpB_ssVAeqZW-lHyqUbYisRg4w7QabyO40-TUG1mxzM51lj1tQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwe84arZRjThdnYOGZIHsV3kc5j_qpxFeSoA2Ze4WD-5YpD7nWx0-Ka0biL56RWlZz2zBWExiWX2-LIluCIwa3F_IwNH3iQSbJBluyls4dVQ6im9R7CdDw-NxyxXSzrYrqpYnzNhaLmEqCpjq1yS6DeuSsd1qZJCxOyj8NpiWdozxKZ_NG0Dwer40DxzQ76Thn1h_857kFHuHWooneGjV5LaWRRgHNkwDFBt8NaYRfOm9NfNUnHpFPzEiHLQRJMnqpIj_3k2V1hTNqPArFBX6BjY6tYIXA44eu6guF1wIlVzEVkctm49AmXiCqh5dyEp9ca4TwTss1dDZRiIhsB8Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNM905VsLLwA4TJqUg8YvsFSXZViLaZHSNX0fbEpxgpDAjxKylEsetUwVpKL1V-dxd2gvhks559F8nO2hJNVvsbtvidqzxhfFJxtq6tzDgA0kiH7JAzmDMLmaYWUgR1NqllotUdGpz01wjtNP0P4s9P7e23-pn4JvO2E6vQLlOkurQLLjS43tCbQ7642KcSubqqMiaRILkkkuciEPzYw-qoBsxsjbHuIJaFP9s5oyfra5o5lhessTrd53dy6fePelatqJmTVxVR6pId93EvqwBHMepXh0EM59COId4_4stNJPz7yfmuMwmkWM3AW6vApA9Ei5al6I3kRLV6KMWfymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI-YCaCEW5S3bBr4UU6JLVvmawmJ6XOYWrbOcQAMbUO_yRrDCdXvpo8QUaNnQVlDEiDpDtHvzs1jOAIfMZr0CN6tAhTu90uqaK1uKUm3DHz4KVpO5MsxZl46979o1YbDgZjwgEgCNoheXiwQaj_R7vdZ4YOz925bihVu5dR0BFJss2h3n3le5EJK2oJ0E7RxZMaJ4rWuZzUMM9eZMYIEGmAfrdD-Zv29IOCSpBCaUcqIjkvI31Z2PwPqwvMX-dd89SjR8rLOo5Rk0eepV3_g6VYrhMP5_EJSbjDLOBZWhWaVBjh9vXF_Qnmk1aI9oIdZ8Tsuz4-M1W9n5y9M27JOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSC7JidbASO18l3yGrXaic_n7FJ0UiMp1wJyFdrd-9oUoK7yXymuTLf4-BPhBPlW__t4PF9bINBorYjy7Pdmogdb8o6zAyOJIn4g_1hknnGluRgVAXa1EoxWsrHxYYKvK83leHUVXCE77zmmf_e0q3kNtFekC0El0j3NgOoIriPIjFnPv-xCvqhArL-OO8QGly0rBfmwzo0sSdCXHG7VDeQfrNxw-I3MNNJomLeSMskHsdIK-Mv4pz4R0P0r17GzWeIqcH7pA2XSo_zOwZsLbth3sNuE6ty1OhA3TKpYV2B6gGKs3bWjfK3bb4Fjg6AX2jYRpDMweQ1EqTsyPHS3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jir-rVrbzsV0YMzlFHmePqsyBEnta20GveAoNVZH0yViMptcvGFaMXppqnuNq9xznLd1xpldmLamkH2XIjCiMv1kPKwAwM8Qr3ot8---jsuoFpjrnK8wATuSAvRRzGhHDqEPvnDnDhxQDEnweImaMWNcBjwXj-VeWQWP3-vG8BzSrM5TRg2dd_yQCkJyN4S9Xye5mJd5zbknn2S4fj9XwWvXJ1rVtfmZfgGqtUgVYx7w6jV5-JgvUl_DD18A0GTq-_zvp78B-CzD-pzpqD0AApZABeNn2IYJkuyvNJqQY5m9Y37y1VKzEzNez1nMIXHnAfDKvfY27JJ6w8kkhcol8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/koc9rgZSe_PUFerYQQE39U25Z-t8vSDE6gLiOC5zvWrYfKYheSIeH18IudAMGRMEEy5pzsPboqGek9MrlYDp4jbw6cCvZMMfW-xyHAub8MdeSjWcLe6Tj6i5AjEsT33RjoyNFGSUMITk3HfKSdLdnfDGJB9s-j24kT4OnUwM7VEjhn3fMAgipTYkizg6D92Jtr89S8Efnj3Jkwt7v9iqwo91G1kw9Gz-hxMjwFcOlMeBknXTJVNP4O_GR7Fx02FT9Wri5ihxt7uzmPv9cXqJdVBNpIpt_PvRORLkg3DlZjjESQma8NdI_6NRG6sWhytFPG6s8HsaOfhCcWP66U0QIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4S6RcbnW3rarlVhxNUbBXm1keJSENxnHVQ5YmAKGU4jbPqerlSdojIlPmZQx7HACPDMhMcIv7MDra4T6Ii64RZV6j2b8Ba79IzV5RWNtAKT3ieHZX3a93fL0KQ1fxfgr-U4_KqMhufsS2WyFIz7TjU0qEeNRKlCT-wQlwgEpBpSYWW6ZemlAdCOVvP2KsO29HVDwvTi8PKuSF6aOJFQSrONwmt58SJPUjDHNLTlAfF6GzXuQvRqkgaEkDgcYoU3qX0bUzxvd1xX7s59vJbCk3PSnYa1GErd6z5tntpD1lNE09SyQWJy8nEg3Ixbewwh6Z_MA_r7hUERNLXPbnYGBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4d3VqvZ99c9nQVqlip8QyFXEJsK5SzidFtPkS7Hd_jytsgGJ-Th69CBbos5VKGIyegb9nDUV9yuEo8LVhMzXZg5ZPzAFxXLIqqdTbcCXwTSqbggunplmXcSlt9c--jAled0EnW4aPriqMJbEA0Pn-YMb8uLJa1JKE07C-0NmF-D0CJkw62ZpafF9MICFfDZskxZbxEF1UOkmPxVnGqlxNMMTkpg8mhqAG2hAOo-ICt7-dSSDVUD80E8M-SdoxUGm0TocOKXX88v0zwWmylwYhs375zF55DDa4Wzp9n90zfPPtZg4LqA19eu211JwvPWwelFVwSIZ64xAfRrjOfArA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qh_aqRMcQZfbhJGJNYiuimU2CiLDWME1-8KukVrh6bDO5DvtwpIYlMHQSIF6zSitLFB8X3Clz5dgsTfG8zLhauMz0JbDPIxrv1VeKu3CaVm6tP6S6WbckHOKUXPFtnVCPjdj9_cKmaNNIh6jcZkx5B0066mPL3uEFsbwZMTL4Tf8wwYLdFKgwEzcw-N4BiJzBlMCrd1PIKyGnmDIHqXL-Yc7oZlnpYP9t6BEVtUp6ocuSFbM-wroZsIeytQlNQYMavA5jss4I0lTQafJXI20qKDcxSRmhiS1cyyYKsz9rFHOESh02rpY9_edvgOuB3i3UJfj7gbWz5TJFfwXOEhaXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiUZvTGhM7eky3UuukbBLomhEzrFXcuufDBhsipY8H4C7ROouDLmKC-28s23VZWQNlXGZjAu6CldUptEhbEiZ3V26F0t7E-y3wA_Y6wIWL4sXeY3ufrpMwlN9qVV1rI6WX4kWS1bf6Cb00UvTkOilSTJ5vDNax8h8Fw2gadyLEi7JQJ5ST198g_N94J4XzCrRH22WziPlMc5H2B2b0xJf3H7cMDqXa7worErBpEE1dVybCxSwpR283R8y-NryNu4V96XN3uaZqcjVJrZUwezzAVEaKcD45QvvndmKKZUs3kUChmHUJ-t43n6g7FBwHSHTr8J0gFwUyBYmMXcISL-MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=jUqq7fgann-N7pM0W6Jd-Ez5zzXsDoWBcafXoYRfDSzd8v8byWfuHVAWQhVZin1JVnOqGZ_9D3FLP-leBdDhZeMkAES715L_DUnt0Dl4Sb5TWW9NWAu_TgNZkcUBxZ5OKt98sSTtp6Rh8jNr5fs6W_bANwbskLcqsI6-hK_wMiqg5I3x9mgRle5DSu2dYm9hWr9OOvaK2TneQXa8gKOdCmLscw1uvJEuoZIYJbwuHLtH2qabjMeY_c8NgJfrOVjdS4XU68i5TeD2EzN3YCbIIon9B_2MXFIxUAc6EQadaBUH3MfBkQEQ368QzF9BhY0iEDqrw_bVtJNnQPiRVUKNDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=jUqq7fgann-N7pM0W6Jd-Ez5zzXsDoWBcafXoYRfDSzd8v8byWfuHVAWQhVZin1JVnOqGZ_9D3FLP-leBdDhZeMkAES715L_DUnt0Dl4Sb5TWW9NWAu_TgNZkcUBxZ5OKt98sSTtp6Rh8jNr5fs6W_bANwbskLcqsI6-hK_wMiqg5I3x9mgRle5DSu2dYm9hWr9OOvaK2TneQXa8gKOdCmLscw1uvJEuoZIYJbwuHLtH2qabjMeY_c8NgJfrOVjdS4XU68i5TeD2EzN3YCbIIon9B_2MXFIxUAc6EQadaBUH3MfBkQEQ368QzF9BhY0iEDqrw_bVtJNnQPiRVUKNDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUKxadj51m4lfI_v3EfcfS4T_u8dTmBwyr3DEKBZAU3QSwDuz3kQ1aAHR6dzYJJvCUYYDfXs1FGZCCNjPnfR60p1NeeaA4u1gi0vPiL_LAsPY58qtX7mXE3yDm9Pd9VtaQ94qvyBMmra0O7kpH63CzPV_TgvNhVKqvHWSbFSPzC4UjBedQ6uXOzXxUFJ2ej48cb6CJOTCvL0MMMt2JCBKQtjRG_Q_5tT6C2knpNi1WcqVlkIbShkJ81dowuy38CBPq1P-Q3A5aGufI7HA28NQVCBfpF5JT54Y9wl8kL1Hngophd7Fuau_NSbAwKtBIKsPxswdDdIv76LzZn4oHZrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEsBGewcQeltAKQBhWv0fsJPGSM2s-a51uZldCwTVR16s5uiFDrd3QkV60Ic7rJ4HFcw1bXuYFfHyZMeV_u4eNLveyDGVMVZl4M6r8Hz-Emve032bCNnX0KMX8ejex4yxeqm0G3sbDCsoSeyEJ6I-sPEbKPGm50Hq_eQG4DowWnMa3bkDa5IJtbxSPP07yI-AscMntG_eGc8AHQ4GCORynvkmAksCpVaagmmb5f9skMRooeifFMEZh86WzxQRWjU7kmZrIm_gJKqXqfpf8-MIncUJfYLcuISG38GvMjtklPiIDaarA3y9fMSOW8jaHmVBocKy2zuQenN8sxyJRa4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kuoh0anXgEc79PviZX_uUIOIwrz06aGmXLsJ91fym36Eu-KsRWcB-RtBvCpFfG7OreI5DiykSs88HWw6c2vvPqpoDY5qzS0xaun01xZV887ZuBVcJKiE0x9vyYEC5JczTSYGBHHtmLgn1KZgYE4atfxC8IQo2ukUKXTrDDwh5YM7GHKR5HafDT9EbV7vtgje9d0ig6_UYLgJSvb6d_CsQkyqxjaa-Hah9M1dy_AEqE_wg1GMt3-fo-FE4K3n569vlp-2tqA9HOF5JLLZuX_jTrgfxSbBcFNz-QLFPyQ4vQzOgGiM8qaCy61rGunUvtCxBHxYZJ8rf19naLw_gHkAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzRuIW8g_SiVl3KcmRgYhs4IRjpm-OrQb7FJXcVq5PCAvBZl5-vGRgIRDz0FU_IcRpVIb0EdEw7_-m9fIXCoH3-h5Xc_8yzwJd8X59a1ztvGmq5Zw0A3Y46Lfnyv3iqs9_JMtPE0TQZ5TCf3IXu-9jitgGBb5pOI90a0FUuPkhciGt_2l3ymcX49Z6YDtXF0rS2fkMkIo_L2PRQt2Fo52B2WyrLv9CkHpvV5GcTf0C-Tg-uC2Tih1_778IajH7jkwdBO12kh6OhCJOvrZOlxhzfVgOPe3QOPNGIRUzv7zw8JmSKNRlCvnzmX41AEVhHSPdLxmgEs1wD-Ze2r2h2mVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFE6TbvoXhVYKFpIYYqAn0NISR3VXu0bqbtMWgctkTzA67YqDem_qUJ0LLBGVe1ZKkYut18RvOaEUHDhlcHJcukC8dv1jgGtQlXiPxoCcobBfIkMuUbIwEO4zHqybCCI0y5F8K_SvPQdFCjXFO-KzJIsw_ycIeU7RhrevCVZ4NogCm2c4jcH1MwDep1e_T9L6NRVDYyRcRXhd5J4LhQ_4W9HXAcLAgLg1x_uV7a141puosa96XjilV-xZGqU02nv5JDq7SUwYMsAsoXRaG5KqqRu8fxsYz4_iJDn8Ta3Hm5kba0Z7GU8vnOUwxHSPAOAMJVWckclK0gXIFhn6Yad8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gie4iVD6_56pBW1AarXrFPqD03P8fbwcscyOUc9R70aUp-rdVzpHxjecDryqmfNu6NIVsAH6yaZzU-L7QGHe-qclZ1wD1PLNbfP5eSmtT-gPB33YkzIXrTgtF7Bctax8_3q-g-cKYjg9z97xnHwEPQodsaMm7N-0idMfL_iSbHkslFsKp1pB0aPeSKVoERCIdyW0iBP6ymgG8Beigl-yLHB8YsnrVtpt0FFOlQUkMGN_0JXqXVfa225UySb6uCMs8qEMLQKFaVdFWzdYl7h2k-IMm-oWq6zZW1jkttMqhZiCfYn01DBK-Tv0imEodYqXpkkZ7ujlt1R3la4YR20hfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UBzovzI5hwi8njgCeK06Z8wCq7DTgsWIhpVW7R_BosBTAHovkvXs4BznDa55tlvtplmI8Cr8DX7OBFzosignwRYNkiXwThNCcnWTUzvgr3JcuUfO1mnfR9Y8oJOTGCqRbFPJ_B9_3heOYmJpwDZnAU2SwacPaaKVKs_3-heCDAT0J3pMibJikk67E4c3-e4m_KDBaG5igk6rZFCyXBrVxdZscKCDMxeT-ue8DFsfLShm4dfKn_NtTXRVqLT94jhh3Qf9Wf1wpxUtobhMa0um2vkuyexZofLDh_ZKEeEXSdV_XMGTeXqI98td4rI-F8Nx3EkvowEmTJQRUFLN-N_hKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5kDEspXr-ZwqAoKSbyirT17ZugWAcfPR54obZcL3gSjSIaiVBpYzyophaNG3-vlJugThovMzdHs3HzI2wGpg2VrQ7KTnWND-QH2mRQJAcllKvktmFmXK6HwWUY7JpU3SXfWqtOhLKIvbBu8Z2tDDasn8A9zrro3pbDRNi7yYouP4sTr4XbCWOVn5pVRE_5WnhuG_AbEFfqbfAVg9oU8GtDeXKjUBfVaOXo_GHbcAYmTLMuViKUTffs9cej5DGZ5wwfiFDNz6eRW6-zCwTHXFcpYH9bcxSSo6FHclA10Xof4QoG2sY0skcMjMIgNBe-TN51uAejBErGthp9X2tYFEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNQ72hedi9_LWr6R_JaMfH4mkPWQpjVxgzP8F6LgNBzi4iVtKXQoqxnsgAYidtIORBYWPux9EC5CvhzkGhtpibW2ULs48fDXflWApKBgodk_L39Ce48BR7gSPdgsxERcJkHAHuyTRvJ2VBktUmsEN5vY1IGvCpe6L8_kQQ5WqNjn5oufxsvnc3OYDzsHtTfpNHeNj4HiezAOOXvBGbA2MZjogbwfbYhwCcjLMgx0GPOq8CSPYX5VYpyool2ZzQ1n1pqcXUL1r-v-uq9S0wXg2IRrasPh-dxZGLI4xc27gnxYLLihTp1S5iKJygsNgrC5o65zQr5pOMfLhV-xvYuPAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH63j3XQ6HPk8BTiglqctcwpXU6hX0p-Y3EChnfp_DHCAiJv2L-UtiNmThB8VQiKVEFWLp32R2Ctyorya8TK9UJRr6WanHP1olXf5rKZyHnXeJaFUaoQ3SIA-bAD2LizUYNbKKrvkniFFpT9cEZl7RHXhEEKEKm0gqp-EyJwsx73TYr14xQU9jQGsUMgPX2luMSQhSHJN48ktqmJvG1G1J0o6EBn_l8i5GwpdoxAlU3qOFaE7sQZkTZKMCEomUdAj0GXRYeGOaE426UZvXPIS2liKA2SFBfljMD965WJlfxm3Dx9JNi8Ofy6BLi6Cz7fqHBbbnfPOntrMLyfkWhIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYsjhTJSDj7-yUHl0D6nmrG_BkTWfRybSBG6oB5UP8dtt8LYQ78NbUE_dUouu68-xFdyXzbIzVsYfY7CUwcoFiovRKKv-QmbsKbNhMCBVenJpC4Y_lBlWho84BwdQ4alHC51-choKcARGCty36_rLkM04um4X1q39cap4OVo1EYNogScFust3UCKhCRE2nSQtS22muWNzrcPP_aQHOAIBbNp332JQUvuRmRufAOmb8w63NC-BNWVH58rX1umHgjgTXYR9GVh8c_LTeGQjRZjW9wttDh8Gktj0v-UQ7yZe0BNKm-9u4gL5cSCB1LQij6cDEIup6_KAEBseG5y-IKxrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwP54EWImZUDN6LJaMv367DPgTV9BWAIOq55qVfEBFql7SdHh4PHLZzPdX6KFO-_4eST5jnse1SOyqQ0vw0CViuNGVBjc2WWE5k8sguKBG96YABQihIl0N6WKp6Ra16tS3qu01OW-F2kLaFSYJQ8IjjZrPR3t8Z9pY98oegfGKHVzjzdbcXBtaHfGWB2If5ZffUFaZj2xsOa0XFVGrzWmD_Xymj3AlFf_21m_lFeK_W_j84Vnx1HTsasm84vMeiNY5v0_y7LnbomK2M6MNu95R2zqcXlX4-17z0XOfuPFBBINMX8JVCuIVCyjETKrMdCtkECUI3sGHaEopoqg1lkIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meG4dYRqlLPIMQeGnr6v5xa32MooRzQsXdZqGLyWXIqJd7jiFCXGb8HBHgbrgSP9wCzD0gRZgJB32SuvebSn_VqXpfI9uO69bO37cHJuiSsmOd0GD81E4N98vP5b94vuBGQbU6iKl2Z29dRpO49yLyC3K1Z_CcI0CyB-GkdnTAIs2svn2NywZ8zGGX0bdbyfeCBrPr2JbZeZlfjsf14JJcMlQd6zFMT65NZ3wXmJqT-G7cWQ35wERpiVKtahIPp8028WTJuXGbbbsXCbaahoMVrxD2y4lCTKB3YJaH-e6ga3tBtWCWYL0lQxrxqJlmOo7dEhEfGOD3ORlk-sae9PpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vEILsqNjygsd1F9mqueJHRMg3AQWI-h0wPJuLFF-WC5Bt2GIFaDHG8mUNxSCeKIyiU0dtXQnKaZcFq7GH_OekbEff1JMswq44oUwosLIw7fFMRiHREozJCgHY1kTMOkyqqVd-fGZ6HmF_ESpB0BpRKypllsxgV76Nk-JolUiXjOEPCqZA4FJ_0JVl9I3d6x8ermKZq_aAYl-jLJaHSO8o29szmvC4o3T_K0ns1xCTiUkxfzPCM73MsXHrheMVM4u-1kveREK0lmQOa1_jRQ74Tak_G4Qrsy0y1EauE5KIVGu2mDU4mPMRogei6AgzwBhyJLpmt1MPWTUvKNn1-41JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROo6NNFRUijO8WZ1f8CdOFUDdfP7J8-9EVMKfLAQQq5yF6iWFGyv-2wDsGMrmD3E7rodbgBSO8eqwLkMiO2wVkXSXi17TaQZCLMmnVw6c3YliYf27sq6uRQFPrh-rre2uoex040yRu1JmuEK1t3HwBjS6xsPQg0bQC7yCY_mf9Wkd9CL7cz5ocTeBZn8nu-_B5ik_ohdvwrLhhmte2YFtVgPpB_iDqPvQOyIERM7v87WvEtgriDiZ3Xrdtctsvxh5-MhuTX1JihJofEUy5dDC6MvpfEdW9cYApRed5RiNFQKTHajDBrEJh2fPoGOAqGHGIwvSgqUW8FI8S7RIfNK1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osLspOAvtMCVXGxAqhE7JMJK2K8ea_0lj6SPMx526Mc_vZ5Pg8TAKtwgwklhTntG9Vm-LQU7BoBXKxS2xcGYVXG9ye9WxlfqONC9CkBdjAULd7Q31LbG3eo3hmeCF1NBLXyyCLpZ0_cWQn4cRz5xDHXRYJhp6mG6_M3JRd7iEmes-ogcln6I4-FqCyQQRuRWHoQQdjqc0xyD2dVhJwwGskt8juclblYPn8Lqks4WI73_ejncSCkRPzbxGz8gFtXvpEFJLBmmmnR3g73ykqhrbPf1DF9RJqhaOdwgrF9nydWAyh7HzeuFin79P_AYeeZtI39fKBzqrNvAN9hZ5ZjUFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaZ-6LvUdpNESLKB6lfoX1AbQ0Q51tyy_jFwV3bzN3Ko1RWmmRHkiPeUeg08ip8q_Z0QtSiPJXF4XC2JBsC8x3Ds3_u8evpSJ6CFCZA5kiwtqq_8oOD178O079QErY-Fd0xw2fkGNJdsFGWWm1RAnYV86koTBKN6Oxt3Mlsg9hk7Lm-HxZNxEF5FY3iIEtZfTRDIjz4ypcdc537sy6Iw65VK1dryH5cfVrN2wWUyUvlzSKaAvyO11X1rjhUVl6AAsfnupTut58sjaFfB2cDmN8am-mOMwB2_kO9oYQHS3-qKEKtVH1IEuXoUza6wJcroQ06wjtBMEKYQ9mr9p9b3lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNDLLkq4h_qQr11ArKPQTuyEEUGemyNQg1shSq4PgMbHL_pFgdBzcDZsOBt4r8y3dZ1udzS6vQJXwZ-v7HqQxiLz0RKktBLCvopo1Z88HYMGmlbfLLmfjXlN3jzhElbFC6gxeEvPk_7owkafkyeVP-nNMjfApHEJ-rET5UX0sv23cgOCUTWX8i1xoKU0tGN51c293hY5ZM83tPr5a54bqvQDVOfjXoSfgtsR-ah7SzYCdmmutJqukd0wvgl7m0ECl92B-CyuueqBMuKaK75-ZFI_AhJ82MiX7_swHC3lh3OcHsO4TL2RgQI6e7SjAv8fCnnn5dEmLWjRgxF4uwHHLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADnd1yuC1PFMFD0dtdMimY-Vbtyl8xJgsGiTF31Hf23TRKaj2jLqIGj1Jg_23ZFX7Ouf55P9yLiE9JLiyAF37zINL5KVoN_BF0Fo6uzyiD99jitFZGZ3zJc91CVbB6Z1WkRRiV-KlKiMQWfiI1iXlWdwhMhGN33rJRkYA3f0IzeNbcSu8pe4mxguEADoS3Wak6Kv6A6Hmy7jBYAv9T8yHuO8ONiJNpv4AiosCii7dU0U_GVTmTphmYEJcSi8WtvSywLtI8o3oZcAXlVSRjjIZRQ1Kg29G2TfCmJRcSjoZS1g0ZuHv7Vd-8AbCyg4e9cITOlFA1BODEJl_VYLX_iDrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NBo99Jn0g31wrMHqvTIiyFWMUmMlXfUwo0V4r7nIvlxlshv_UYsq7uSG6uT8SlDlflO1shgDQ60yshQzYldEN_whEA2V8jenVtzYWyxMJwEEPfd4kxiovLvqAQNNmMgK2ZjxbfkvLrRe3Fianw93kbRZbmLauOj9K4NcJzcpbEPRv5e3NklOrc0E8qUqMzptBVq6sV9eWD5FsD7xnFEc940LlydCE6rlVhOaoIKhUW1qxUGq0X4IOSJTRbANpIR6QmUm7oBqAKDweZ6hO2CnXzLuHEKu44Qf1JngQnCPhWgmdclqbi9xDQ4hd0K6rhpJpaAxZQ4a7TaRf9lGxBc6pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lx7SbyXucHhF4qx3KjOrbL8BcJu5_7MasADyGj6luoo3KpWqNgveL3z3vFeXthGNew6p8XGdzYtLIzuNqaMbq2fjgmdKXVWP0WOkgMXumvvT3Kw2kSR3lynpZXRNTRJC0iVYypzP-YbPu8i8eq5SNwyFv-PqIZmNj39V7F-jFJdvRRp-WpL10o2WvKz4HKqBDLCp15D22f4plpCVBNMsuedIs3zdcS937zlOhu6oyOMRapZOAHrNnwsqK6s3W9GSvbRVzvY3a6H3VICZzpv15OBY1-NZTkwykDxawiJ8dJ-BLaOngWfcKAA7GdE8GvcVsHuUVJHobL5BnYy6sqPiZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI0YiGUX4WEdx0S27vuj03eAu_EvmtJWbJuJjblav5otH0-XsiUhgYWlKzP14-AE82QZCjszTVCBZLY2y0K0vwLzuAojKZa6K58R2-Il2wNslokDfGOxHqOMOzZT1CPuTGbBUDr87psIsaC3IdZIzD1HKBumx_GGgyiXn8WOnWwwlzlW4Fw29gND_S0cWIo7Vlu8EK71TvgQACDu_ZHNB1rAk0m1FJPdWp9kDGEHqte8VUGGOETlqKGpAH5yj-svVSTJvGb987OpE_MvRCdqzeAprXe4jqvMBm_nps_EmS_2c9yNoKeVz61YEFJ6A_B9jz6zzKVudE5utfjw168leg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE6-KbHbunBzwcwhThjGVNWLC6B0IOl5nn3BfH8TsC5ofwJHKINxSFdMyvoj4_3EToq7D84j6mNqTHcyXqHIInt4EAK_vhyHlGER-0aAOyhoLDDNdmI5nvI0KtpK18GIkjhHcAlCx1glVcd7GyJKnyHqFwUQwsCXGXbO3ZJBdKTNNjzNpPznNUNflAZHpqKHtKh3hJ5nb_uOLWDsS-93twts1boiLMm67Wz1RihvZIjataVWYaYIzPpSU9p0kXKhhGGL-Eph53juDPfXkPsSdi7d-JpsV4o_bjS1BadKhfrwyjhssX916-ljBv8NvnqtMZPxuY11zr9IKymRK4ZCqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwPcdlf-O--fz0IOT2s0VlOOkcKNJfLb363NxKiHfMUIkdo2U74QnJZvycNkkcT0f8PhQN_p-JGRSEXT4nIxBn3X2WLicgTEFi9fVe_44xSodVKnwO2hLXjpE6ai2KQPvh9qp7Y3qOn_996Sm12DLHtolOJTysZy9UvThXmT_kgUXWgegZl3WsWoBIpdleTy64lQgFUBIv7_DF2DQuHw_PzkxMbWQ_Fdsih26o_h6EXbjQ7wAGA41FfR9C_5y9XpLw5GodM8FAxwRKB8r6I2XlGzjTM13EeBSKsMPSlcY4OKXG4fK5veQZUacwMHNXk_JyrJU4_N4aW69dBBr_p7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2iF21esgAbmnXOJ5O0U3aqVkAji_yOBb3EJW4ygXrmtgk4esH1Nlg-3BQQpmKHCacsdh4y0KcT62ey1u54b9huV_YpBpiLq6E3WQFMNIH-3fOkdCqO4W5Sn34mPJpf3wQc0Bqhgg2Ga6ciBORruSBew2gKc5U7MaJfShTcnG7vGJ9bgaT13NeSaJNm1xbBkcNjnWI2h7p5fASuyV5JpBA24TwlP_GMbzREjEDzCri1YHh7Z8QihBobutFl0sAhfJ7BHuHKONAef_3DJ8a0h_gDEQBa6tXCtb1LwPD2SVAM0pTbDP22Z1xAiuTUkqZBvAW4uZZFVGBr-MvJDeVzfiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJgicdETDXLkyncOtOjTkRTP4VmEQbdh0jnRR9p2HSAG6FXD68gImZH9exIa-1HZsg4jPLUlGsTUZA7Te2aIqPPIKMV290761eU3UDogrttcC4OoP85O5Oe_Ph1VoXWhF9PJcs4bgn--WaM0703AhEsWBI4rzy71cB8IxoSxT15twm8VQNR0cYEpJts_ERmHPDEAUvz2BQgMfmpImPbVgHBg_IOpUoPwkY2oGDpf4l1yAQlFW3F-oZpUl17inf0pac20rA1RAsdz83jQD5DBd8CdXjxVvL3t9l76HY_r5KaGRuBOOHRs7Mz1mT2eck-nRorOGbkC7VFszq040bfJjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSVxdhgIe95GYpr2EsX1stAn27oGEY6jt4znEZA8hmUOuXxVVHwg0FWVXOTPpQpZ6k4nWxRNHx188R57WE5h5fsz0OPMF57m1f3i8YP0ldv4ryD1o1gmB2Cuz6zjhqnc-D1Mrcch4PvQgpOZFD4238sqOiZomHpQ27o-K_S9BzrUdHcDUAOWR2mch-B7R3ZpjbNGj9n8ehPp8ONeiFNS1FTsyD7nkQAJFRPeX2I-78rzC03Vvod29JWZ-tFSwpvSsyZsO3jl4OX1p-eD4l_VzZW7jk7x0WSAlqW6iqzeQDTLHFssHHxrF-CTQ8sinPLxNB6L5ZyXx4VfMMUec3adMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvE5x4Nkc7KQT4G6swnFXDyZfb8Ve6TziODDW2n3_MJTihbDUCpzN6bFasvFvnK8ciA7N93cEWmQos_gmp6GHH0dtmperOwvvATIRB_2y1WP97dV-MA2fhvGwRxGuSqsBxS7Rbu0NpP1VFtFRBCk1hIaZE3dUb-_dkK1mp1Prb05HeQzvI-hfakPjjnVw7bKAvOECNV8nHteIYwmu52ggozau4oF6bywBRr2YmbHWsL9Mozgqb9o9V5NF2ytGJsH8_tTH4m4ggmcFNRZnyPWM44xks5-XqRXKNR0HLliPJpEFSDLFPEcQ9SAB-QICl20mVil63N4yzfwCNrRYkhomg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqxK88vi-8PZuhwyZURQq8Xl1khTsMhgHXaRSQVYZ2jlwvn46yAl3vYSSVR6Bh5NRlZJQFHpz6YiS225muQrmj8KH711ukmkKqjgNgimSe-KSXFypos23ESz3l3j6XpEsc-Y0_mlzWOhKJ5dJpSqXn1Tm3Zzc01ExK_E1gKUPb7P0JxMvdCWDm8iOK5ya0H8ysFqLg_70JvjybMGwAcM_cVZrdgINCB99UxCD1Y5QIMwlOTIfOZ7Kb2No09RiA8BptkrtKCBr_pQS2R2frtAqc9fxVrOvSgeEMWInv8uXIA0VYIAyn5idBRcAJla4TptXXncMiBENWJQKLbqoXVG7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEsjKHlyznU1iLxs9MrF11MB6ncR3wMOZs0LAVwo8Wvq-TYCM3FRKyDg2j9voAunVgIQDOozf9LEK4uj-7Ww8c2Bu2ARUuS63n-09AGBwiKeEO1JiX0Ky5P5z746oXkxco2FbjaIVCyNLcEarMjFPlqKHf1v1RZDeQUGwvL-SKxKJZAGlLYRsG8w5LI7nJ0iq5tC0MNH9mJlreC9lWMOt2pREezeZ5ygOdIyvdAUnHgX7tCCmAovR4GQ4XwxrEg9Ct7cCcQLzLXYh49ovNvDAa79yx-edPoiDHS45taArtcajEyD665VVP4Ap1EQVF3CgIBILkN6pqcu4tawnocUNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWGDlH4kh78jctLK6vy_ZKdPPM_G4FEjqOunNSD-7l7MS7a1oBcwYQrg8W09--Hllsa7tmla2anxoBiHI29qSkQVmByMy8LDJot5qwWtdSdwBFX6Qvq--8mwkY9O29xQ1VRfqDUyQuUW7d_DQj55mqMYCjuzXbuoU_wdSHHNHV52L8d9osD0tAv9p87_AWt9Ix1Y4ywQIbbrRYmY_R69FY0wdJlvBjMRX4uH_mCngROq1o_l6MqhRZQ0X45bo7PkymuSOOjM2yn-QaNQdPtXwePcHuCo7TVmi-8FAk1vzHqEbVSSIHhoJnVU80AhP2X-I-wR1AySqHDXD1aJhy0r8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKd7pqpTKlVr6TcsNMVlRi_kIo0rlNlywtVhOBowsCcniXsu29ynpjyQJuBSmPhaHvs4NYFZB5Nl8jnq9ZJY66gtXMoVsS_sA05B49hOsOx0uetLA_ummVB8eht__0FjPj-oTYYez-N0wpCl9mVqzq-sGHiOAE-DllQGkZVyOzkX-ZIOO0MxydHT9v36TK_U_HkvO7uVSvm6_x8Y_HjZ58AFY5i5bzGtdBzDnYvP9c_xUTb4IZOmGcaoudmSEtc-jAgwmcZ5EgNssxtBtl4Y3KNX_9PSnvYR2QWSffQAQHC3F0AgTCnn8obqtqplDxsR1EiW_NAClaI6DzWzmXlPUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7V0-ZP5h3wAggLZ18R-7-vbSHKNmKqY_H4OA_kDkyxMoWAvTrhlk5uFDIOnnxO4BdxZef37EGjpLKIZ7kqAWhZ1lvhwJMB_gHX77qAUqoAGPlJcSwcBI60K-n9OXBNFxgcW8l8stwtuzBCeyCxsgsqibH7VBCZRz7jau4Of3YKRYz89_M9y3GP501Z3bSligxi6SweW9q34BcFelPKITUZ423IQVS3qC63tRlDtfmace0SJsnq-I1HU4PHYgBkDHnB50mD6Tjw9i4bKgqR_tLhps_8u7AMbZlZIUO3jGT2amBmTzMOp56gg5fnJMUSw4n6fagJJBV8SyXTHjRuDwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HifklIKS9RtDNU77DfxynMnFFx20TJ2BfmJ6K6mSHSptst2T14IlTa7hKtcyzor-0BZYyBfwm3JXwaxd1e_qh8CXgMM5kfAyUC5cKGgjWbFnAYqaJyjPYlPRuHXEF01O6b2QI09R5DxVmQb9U3liyG5gTiTV-aOwapC7rX4sdpgaJqPGxU5EkKFC-j3W7p5YMVxq3NJE-NhB7nlBysvDWYyWFAckWHkp7zj9hIR89u-PngZ-IFSAvzFf5eRAgrjKvboFtNw008zczxO5apIPaXF7QskS3LN0Wfa01hblqU3v4U4-2urxXc-_iqnqRMN-bx6P6P_Ur9dCs5YEXMJuEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuOCweeYGlOFu4yfJguCPH7BeuTog315GNahEkWwvFMoBqV_H49V4mEDEQi1CdhUoy8rRZcb3xuyQD0fBFOUcWtd7x4-m_h6lWrXaB9NZuM-QkauFV7tqOPYDRBzV8gS7zo6N4j14FvOq6txV7aawUCUY9616BD3EqlCiyQ_ACsbd8U-bAAvaLugxirF4H9JXfuO41bI48QejUTW20hrnM65BD-GHX6ypngZ3QRARoSWG1cWWPl_9SXQkrXv4miP_xngS6wyokDTkurz3DRgIBL4esumDGNbJ9_3neLSUHFeDvvxhub2Pr4hU676Co483ER6pc0192Tuta2cxTEWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f8Uf4gjQ1hb2oFtiofnjOPBvkCdDTZqX7XVe13_A-PST4ekSw4bes7CFFip_0ai0wPEA-elrW4oAwWRIQ53YLXI2-qOVZ6xaMVSEo_PJ3CMRY9bmOe5zmdoEL-D3xGbJRzu_sYAgYJjkd2Md_IAIqX44hcCeM5Qm-1LQWoAw6wHncUZGH_rPf7imbhyyxAbpqTmWt6YfcTntE4MzexeORnuPzWC79KNtXS0g_geoWFC2BZP4PMI1QMy00_RJkSt8X_7JHmDfKJOaNsqNzB-HFnuNwjDeHbXMoRRK0rvvpYFnkCUSB1Xfe7vZ42qY281h8kfsHcPq6_GFphfJZX7zcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9kon9bG4k8Qh4yNit8iyMR-fG_XIkXlCO4sb-IZ0ANCxAr4b0kBGXcExlVrpCSy8CPcbQ_YKLPlJaHULxGHnJgHr7FK-2yox8ReuVwX3-SD_GE4SQaVQdBg1YiFyHM06CqbEe_hdlseFEpeRyUDDdlNJ2hiTivoVdwJfv1Cz-9dNmVjpSpLlPGIZh7y4mtd5Q9WeouMRm36KkVYpjDm8_lY2dKKOQ3D399MYqomRgf8e-olwkFaYg0edWP5aooXwxBJ07n3nlgmEACjM6PyzAw66fkt8Qk2kDhrcKf_TkWY7K4l0UYJCRgHUNx2nDxxTOV8L7lm0FfcvlpCU-rupg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdKmXM4CC24pjsODcP7ut4-qBplII7sTDyAlmLIUftuUftUIMfJZJgMrP5c-osNG35_k4i1tdmduXKnVtlyiMlK6WsFyOy9ae593L9xLW8nu9bLWRWr033hxr5FdYzsWHQaxyt-o-8ki7iI6vjS7nMJbmDkF8vt_CrWGKgHWvFR1dMGGwogVaOhsLqJqU1atzFQdOQ2OeH_dz1aZBnvQXoSfxppdQr0XLqfGKnNqWXgUR1GMucd6wWTNBHJG99h26YkzHOpuOlmI5qSc_GdqyypHgXbA8Hk7lopwIhia84-oai2-dj4QxOY1U84x7Wf2WQx7YqP2AmLwlplRE4FKoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpT-5H9T7QAilCBJ9_Ay3GkKX4ztR9ma_4ahk7SXiAggwTuI5fCkSMicIAN877UuNhf_uge24UMiBPTJX3YTldJAe8fPTHER9Oq4dap54Q2AtyO0pqJvjKJYIWDS_A5ntPHydZsrkuS3aP7vI4P8xyRTabewXyOYlQ6Gh7v-l7UHjcE8nMWDq48-hXT0nJUCH7gnh5KzV64fRLsWIVqx3D8pHrc5Yi3IJGT7uTqoVH8G1JvolQPd-bE8fQBSkXgW2g4yxJg8MPsEYE-Tv2VD6WtwIoNUfyCvPdhnMrIyh8neklulDRfjjOBACfa7gq8ayJ-jL15jW9pv-Bz82v-a5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6UjXYhaGV-tRo277KOdNQUAFUFVq1b9ksMmFJvaCtTBh5erSUtB_jzsl-fWKQTO59whhrPxpPwWhGADW8GO3YY5AU9x7DDJayChwj1D-SlhZ9sJg4feDdM4KP9ZeXy7hBpD4D9apVHaZqul7YOAU1QZ_6HvnPTdz_2d9m29W88Fdlgb9AGS2uRkGXiQXiHvSHjgp368Iid-gQKWybVyKMuHgX6ejqnuCFAIhpcD3104vVIq-JYU7-lcjDkqvYVJBuDJNd3iuzmCtyzsxPdU2PKZs8f2HGKTazYXcCuqdlCPsARHRSSrJbF-dzKQwjZTni8Y8-pdcOOoLhwzCz63Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TF7MdXJgUhL86Mdp33BEELKiRldLafnN-mXY0mlFBUABocVRQybA3DH9TXD83aynm4_mbmEJGE6ppfCI04Kykv9HZumb5AJewjQ4euYn-e34nxanXWTtNpLFoyunUELaTCyT-heiNioBdMRW29dOUI7RRN-PH2HALDCZZCxodWtjbk8HliGVrggXuhQoSBO59XQ_ckjmmTC7duZ9PRe2PtCJGZQxeOwtFHXhP75Ke3DfUc3e2TvE3wi63OL8N2JdfQDnyEu5pGKvVfpyBxpt_SGYZ-8b9F9gTeKhyGONaFYTcMKp72UNvMrnCDh7BUjElwZPINUkUrMuMwHchTQfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaVuodSlM70GH0Sh0I-NxBZUqc5tXucv1bxTPY5p4L66dWwGUkSogQ8WhhvwHS78s7l7ynBcYGAy253B-T1C42231C81Ue3yaLdYbmH664GkohgzkbLumr9RysxtbIH6ru-AgrcrC4TVjYQAAV8l_H_QopxzKuCODBqsD2q8oLgo8LlfhSyNILLvsFXJgBIlZRDjA82UDYuElZ6WcNJp2XjQv0Va7TT50XSa6JP24VhWRcTvqmKB_L_yfSDKPmGt8qaFjFdeFqELEaESB1bXBWL_gwFa6M7WjJKcR6CxpL2NS1YJ9P0pDKPjsAeFC48hxz5E5CqytULSbLrHurkmNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhOKUClNCDBTzgaAIQ76j_E3wPCC2Xqqmmvp-P1Y8PSN0TE2-MziPiZsiHon_ezmqUURzDxtZ8eB_7LF1HYFvNnYIzeyDDi4BOx8CZn9XmIpwSSOfo98GHMyd5lcOq66zyxXysPYmdopVbPMW8yHq47piq2aPk4Jb_Mygc8nAabLL8NyB57J-ELCh_N-c5UxdSBNEAvmjKRUsju0DfYnZVQNzmPnzvbCHZ4QxiRfB8LcOaXYe3clrsNs3fw_7yEf7LnVQro7PRXlS47jdG5Ctr_qo2NIG5E_vJ3iwcbBtY0b_cb5FH9DAwOcsZYw_ImFiVOR1PhtnlYhu8_dmR9CCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZbAC4iJM75ckHjrSDMRJTF8C22SjtgYt9IDdSMvlrUnGsutq9P-4NTN7GUkmgfN_cCseBe2b01AhCw8JeG3jqRNgtiHm5LfkiMuMHZ4cuE7Oegi4heOwZwPghGsDjyv7qAZoOBittigWSI-_JZCbkYnR16QkxMDVxChHJlf9rC8QxuH-IqcNInk78wMUYIyDlg6mVAvzrWavzPmR0VId4mQ1GGa2cgzsbGzxuVNTPHCkTaw-UH5_hNCLe1vpqZfXua6ctDjVVQu8QfwfVMn41vpofR4HDbfX-cZ11JUy3w7CJ77yuGejPCQySrg5fTJpFdi3fl90pB1vqgbntfWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5Y8vsiwq1eFXh9gJjX6yGlMlRnJR8uIQoy5UWUK-XQozjaLygFPZKCiRg2re8IUXo3D1At0cGAHTZMcDQAjfeirDPphEl-3wMsw4zGLXZGkNbNRjgvaQArCEVlotKZr72_7-tEJxsJS6ORY79rbUSguVTVrko-SBSa9eQoDmP-aW5SqDHogGVNQpG--xT9pU7KC_spQFvgVZraRZzCPxZ2lcdEBDq1PoHPH6VyoisEzlG9wDM0w9h78icZd6v2KwwtChWYLrDas_OuoAZrAk9mMQfy4zZnQgaSuLgrpoh_3oX6mAwnmxDD19PpyzWQiJ0S_YXZ4CrMXHBuQzMvpRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3PvJs_i8cnAbQxNYFk-R9eS1JcdtKHcJAFtzaz49RMZccMKNcOiC3gtVAAVwbJ6JmBD1pSrDYaH1dC6SSJN5zFsVj8C8MADw3R23KuhEopwkytr39AqSlRtxp1cVQ4HrXh_CM0wvrPMrHkWYuy04l7YTymdVYzfS7u5tUHbvhd5e9y428wDZf2uDstjLc-ti4QQRSO8VOq20SfcQKx8DMzkvZONO8eJKDsRUcANL5qBUGEUTTApYvChHtA063E2zcRuiYlo-f9k2DIRQMdy4bHg_8prk89_yuvIErU1zOfm2FBM29RbdS7ZdxEIFoPOHF605xeoS61qETFe3DR0IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Apk_ZEv631erBokgpjPcivpYwzLeWahI6v2N73ItTiEDHeKBRacn40c5KicqR8Y1UMXBQCXFT_8gE2yBxUYAcoIlzHvOcJDLG2qxAkwnEnc6k0iJeUWjMN6cSeKews8D4PBRKtUmvsgQSNoRdcxla9aeHNc0oQ-dmxLMKz4KRFhbFm4tW0VwHm3ng9b5KMlXxtluYKIG-G_Hhl8CQFwR0cLsZhE2083jb9EuifJsQ2mOPGaspAfpYk27q1PRWPgkX9jWeWVSNitIqcfXxtcCZAC6kQ7i1kJ8dKOpabEnY31fO2epG3mA3R6oam-0WYt3kRfBstDJukqcxnS5364HRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oDYcQJKhcFXvniW7bvI6cojG4wSSpWXs3X5Iaa2YGECuRFfmCW3UNlLR8Kguzxt_KxrwMt59GE6df9yvd8VERwwJlpsKGmB_zQnUJGwUFomO491-fm3wn6O4XN6UziDKN3zKgwsb_LkFTPajDcklqGu4xM2I3EG6jj7YPPcVECEO7Ki1ElwTAr_HsjG5ozMe1jesKtq5Shq7oTu9un2LYhMAoqRtuAk3RIsMLwmpf9skN1wdcHriq9cwRPg2LdCxnTdbazW2pP6NkuijIEFCmY7EpeZWW1ytD9Vcfh1y4NXA36BtcV6UMHsHcjjXPdwcwBJczsSPy72zyz57GbkRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzKqmvVJKc2aHg-9DG3HKTaG76ZRL4GFKQCoe3iV9GgZqZMDGIqGYLezR1lm-3Wy0XNHiF-3kVTAL0ohC6U7ZoYnUyQaqpGm5ZXsqfhejyglMW9chylWXtxF11oQooIUawwMPQZ035KHMuhYB5V9btzUpBRMpOoZlZpyj-L_tmKU-GyJeS-5_Yt7VCduUbzE0AY5nPE4GwSu-gOfxLfOkJLGDJEpeIROe8SH5SuoivDc5Nz0n1w59si9TpuH6ITQp_bhitAJwxgpl2tykkVwjfKsvx5ChkPaMIvvpHuVuL3nOSxiB01Qf1ZvAvvGmHl3FaiiLDIm2ih0oTmFD1VGmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYS0KJUv7uJoL66NDWU6usMvMSJQ_llXRqIHOSu-Bw3DP7AiI0KG8eJ1xAokIJivKaujmbEQY8goilemWD1n1kmTV2jOe0ki5w6vcj3OcgsOGpzdjWKbckjj1Vw_YPVSiO31-aGZKHPY-PYsgpInFC0zCCc-E57t7hCdyu1fXzTwUsZ5vtjF6_Z0Fhx5RNHi5fsPvKXGJuud_scebWgGlfm8GXUEOE5S8kT5ZesCZZ9MsWcBIre5vMLE-XBw_XW4yC4zh2RB2Rbq8p0WCo7xxOensdmq-opl2tJ0fiJ88vIfmmwxlFqXhGtRw0oIU-ctXYO2HVz_ufC8qQAGM3wYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGFgGwL-eDz33aByzCo4EOh-MOnz7QvXsPEMoXmFVOZmwhvGnCT8Q36GMrRQ_4vy8gC7iiFJuviRBaNzh3xk0pRNrES4vmBDhKJ6o_9xRukuB8Ve1WfXW5XEk3oPDiBM1h1vXJyVGaMxOLrJASmVakjocRVVJ7zym8JJlHbi49bhI4iTs9gROXQuqWWsztKjNsY4akAVnGKBat-0Xmn5DB3VwxnD1GqZRWcp5uaygAeDhnWOe53Vi9P6brhxExBbokaFdmhdjcekCVaCqspP4EXeV-3TKGT3KIEw7btoNUa3FVC85cjkLeDS1ssFc_myM4CGNZK5QNsK0_4U0YzxjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfpRnyOhBFa0fytazJRTVnpn7tmEqOjsOLSTLxfP1lt70gvAWxY1kCtY7q278gMHpOZKR6HMVhuxUbVwcbxQTcTjRi8AEpAZ8S0M6Mjy4e8YeouHLhECmw7RU9TwK6v2V-BSorDT8WiABSERVnI2GfCgB9NGovYJrsnOTXUBiLId_HL4xjzcKMOFTNNYWEO0bO4o0PgtG4Ad1-8b3gTlmG9y-Q3SDaEWcFKGIZc9J9QaegD58BZwETVTI_1amqJPFCOle9-ZB77Twghm5ZgMG3Mz5sBRnilYftWSR3xfKCnHr0eg59LlGU15ugwEel1X82UHWPYpKMvylZ5axxrcyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMB8ejakID5V3FbZRKWh0StBLKI-XGRuYAvyLjargFypAKr9br9mx6JeidCnfDwd1jks6RkXClPkHGNS8VJ9jtI0f-XUmv570W4iM_ELaT7yHGLoMaNMRT3yc-DMNHCX93hg7CIKD5UfmTQ71aeapwrRuqHjT3kucOn7S3Uju_53pOwpGYykkHOlDKojhr7skpsYGw3cgxNBzAgaQS9Y4GKnd9yTtkmiUQxOyiScg_ft1dY6uy4X7Vjvh-R6A0-F-rtwAlwt7nMIy-2foBZ_rKhQELjmmZrMktA_Ml9LOYHWipYWFpz1D0jpInCrePTUgSxNMAhsxzMAdEvs8KegHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra_K7uowMpgAp47xTiZbnuxzJ235JMnA4kv5vAsMsLz8UC9OYNBFuUuNhwMKFmwTV__w4BthYTIprZVhLLK1J1lMpJWpbwySd1NwnYG-MjC64QJzB1j3MlGbwgRi43loCUdypDy0dz9a6uYDBh5dJ3s38dq24q2PKJQ-7Rm8512qpcgQ129U1T2oqDiJXjiL5PKO_JLsE5brmsxWITbgCviq89kCpQRtQ7WJQquz4uO3Oi_TVNz5c3gbGs-bkU5SveW9gt03vI_AJVqKqaUd_of8hJanJ90kbG_yMwnqIxtCESkDML0tIBbWIqQ0vhnrTFXX4lDbYKlnCtE2oTkJsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZ-yYl0at_D84X53GxVGRg_AbCI45Fk7ean0PsnX_cB7bvytcBZfHl-N9yjFnHPuUyur8ZJRJj9pwoOAkCDK2MLzqtYySiBqIfkTecQnXEaWcU59EfKF0FKmZWgXIjb1gennQVgkawLiQLR78NhK14_aGZyW_4IzjQ8Fp9eld6-IXtKZo0vUx03Fd9VHxcvL0p7wUn-7OAf2GT0f8Qx_GielCgdyxlYf5IziyRccvmFaCmi1gQ3Uq4SD2re69BSxFVqLmJ0NarDwzsxEIwYNZ7_W9ExjvSfC_vV8SQZm3d5Q4KpI9bm4UGVUksCnVETsSmFG-co2tDrHW37eVrmmrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSx_VaDwX5y5QOnmyFIlcalTu9rZZeH9TmCTmWor8L1DYwv5ACTTZ09yF4xLjushDkT2LIvUWeTIinVMoPUpXNafcOmMWw-p3KK4ur2HrsnEm5FSOQ8yhesoadSRA6zg612ajPpprfYDKXxCKUvZyrUocIFC0Cu2y4E2IjLTorgXGnDRSiwqxNIOm8zvlCxbch22W-1p4oUr6KVP5t7CeXe2f6QvpTBX65EHEaHfMsy99JATsNTiXTqX4kn-jRfwDZnqMPWyO-BIrkJN-IBDSUVNCtwwAfKTLCaUBgAJKEU7_Aks7FpGdynF1OxzZha3CKZV_QJkJwB_wuK5exhZKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMWkg8-9JstJcNL3unuEND_AvAIqfhqUsiZnoVHdHfonLNqjNPch87EXfbyBWW3B9iF4bDqkbkGprsc6CAUFzb8w9-Z23Xztzv6fytUkd49mAPai3xzwSTOk9wsf_3roezBLuLLLqyX2kFlI2b9gBGDaVp-tbdH1I66rNOSQAI_Kp0HyFJwTleZnW0jJlvRNEzN6ZjWjsNZPtRfs_SGAkJb8OPy39x-PzmP7cpeHGtbOBZeS2xMh0tLklHxfQWf5H13GydAupAYkrS1j1wW41TZtRoG8B58s16XVqy1rEQsFcKXfXh-NeptOZyNS9WY3pHjpRBRBmepcImkHO6YEWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrqxOuBBDCLdRH8OJ2Be6Tgl6QcVuZOFPjRPgh42unbrcjsoVOxdsXkY4hNLhz-b24x-6JO_D7AUsRe1nfJD2KZRHu4xTrtOGY0IgtEaAgWJ2Nrek7oer5j3J6JCUlhN-gw9adkySuJiWUHIWuH0y96bdIEFILMmXuBf_NCUQ6eLbxTVAxic8C_cG_1mb08gS2lXNYq5OAciDba2UxOaduPWEZqZzOz92JATd2dbnWRAgBUqCtd47wUlrDW9J9LmlUdyMGZTkX7zXwvmqfI-W4pU8nyg2znrzzxJkwjirfMinbAHAw3aoO4vn9nuP5ch_UF6AHsh4Gx_4NvA0pGfBw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=v28-pOlCSEHtNkhM0tgYxP2-9HKOxj-OwwjFAsIxIV6gtH4-Fv2NTsR64dEq3ibseL8qFFTim3402t-GUo8AfFi4SosMBm7uJTAuT_7bBQvBlkFnFasd-faCXcJcW70gxFxVr2HK3IK4S_JgQBPi42hpCxKpqNeC9Anwyw16ZeRC91LrKn2PPL9lr4OSdzbbCWbdCXRg2riN3G_pSQ2L-OGzyOuWCO94-LPksb6emxx3QKAmVlzvXswiTJ2tBvAg6blgp4Nz-Wo2ic_ZwdmErRk_sgA1qz9rFJxaGA8UqX2LEcCpWznmTeHBOxiCYlm8KE-AW7ChoJM_ji4-KwyFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=v28-pOlCSEHtNkhM0tgYxP2-9HKOxj-OwwjFAsIxIV6gtH4-Fv2NTsR64dEq3ibseL8qFFTim3402t-GUo8AfFi4SosMBm7uJTAuT_7bBQvBlkFnFasd-faCXcJcW70gxFxVr2HK3IK4S_JgQBPi42hpCxKpqNeC9Anwyw16ZeRC91LrKn2PPL9lr4OSdzbbCWbdCXRg2riN3G_pSQ2L-OGzyOuWCO94-LPksb6emxx3QKAmVlzvXswiTJ2tBvAg6blgp4Nz-Wo2ic_ZwdmErRk_sgA1qz9rFJxaGA8UqX2LEcCpWznmTeHBOxiCYlm8KE-AW7ChoJM_ji4-KwyFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OShXc_neZbIs7rRtvNC_MZnzJcT92d6nyzK8y28-JyKgwyqSYcukODsLB8dEvoKe4SMZn8ie-OzIlagyB2lsSS3_-RigoPY-UbdIKZKkP92XJPzRMb0W5p3ebQd-oCeypBoc6Zhnp_9I8IZq9KqvZrIgUSgI_3q9-34kp_mnLq81YVi_3oKeDkMx_szdC2beO4yOBI4yMmALmIe94Q4SvG-ua_ubaK7MoIyTqyyiS2AH5Qv4IVll12QL8UB76U6Min-WdEab_CEf0iuqeF1L1txGG3suZowhCiVMh1KK8zxNisJJedT5q3G-g7yYAb3xaXWeuiC51PIYH-a5SIHy-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceBIfZ16gi9lM3DUsvJBNEplBUm9ytxi_lvoNpUnaStsK-PvEmHmQQ1k_hbF7D9ANMyYQmLFnkIrPw-dZBqgNdh_h55Sn02cAvqrz6UhfS-Rs3Up-FbL1Z2uMuCM8owLzHm-MXKFMGi6_UDHi_5emWxHeBHRGkfhpKFJYMNkOod5H0JP0SYmcCKIqE6Kj5Ro_rR0xwpM6e5sbBBe4X0ofqCLGJWNyT7UyPKEyi40nx1wwZ0fmD7Xx9XJydALSr9J2iVAHJ4IXRMK9CzeUb3z3jwRxIfNNqpqXlYGIU5pg599jWBRW51FAdnb0jBFk4hosmsgGrhJR1Ec3F58G8JfXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVFoW8UKAi_9Y54DA-TJ-1etiHmbhIy42Q6xdkPlWTkSZvGYX5SqGpcTAjKCpXK4IXSY6eWMxQuCn5xAMg4V_gfs8ceItWyRqepQJoPp8-pOaD-T_0TLZxJ4fvS0KWKn_FDROeblj5T-S9aEYrpKb1ifEleI_ZDvAUSRFwKvomiqLDe4uJ97s-OuAfemanUJiZK-lko1o7S_GCphyrjolqeEvrrymo1hSQ9Uv29pRgT__CeRmLXRpIwI32jT9kB2EpnvcrBQA53mXep6fzLaiSzZvAxVMgj3-qSaxKjf3_5FWTI4efXfIuwgI6AjhS0cZM9MDH-TSUS-E5YNYl1hsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgDnpAsJrW6ShpUO6UjqePElC14ueNtyhHYutkiLzm8QNnKde0EnWJIyKK87JtwNzpdxCSRZWwNxuBfHzh8jhcMrHMxyYBD7taNm4QxNnlzuKB7OhDJA-e7G7Y-S_ih9SEhEq-3-wbTLYkvQZDMKzWFykJ99ixUzgMbGGQ-xkDiMIIvUDxuk4yiGwP3qbOq0ozT2cWekqco3eLIJyrIdHf-fKtviH2ent8Kn7r46UJQ3MSuKO3rr2XncHcs_6wB-XCTnZN6gxdquDBlZ8FQOto7nisQL1X0GEdL_vYKKQ4IGBs57GDGfrFfNQPnYMD8MY0KpJD6alXTIP2O0VIKIkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfmkLl7IWtkVC7X9u25EzBlo5NQnmimiFsirSOg6y-d2a-7HTp8uXEEqDJdlCb7MB23ZFt36ticLFda5ON8xKkcEDMoK02XVSaXShiAOz5VG67pO13qdgNmU7ZqR4T0RnjfmSVDprj_AqA7JnrqcFLl-sKyiHP5KXLEQMU4w1U9S4GbzNiChvk8XF5sC7Ktmz74AAf91LkKcaGDFMZdYR4A02ts5-7SF-UXEA9ELRZnToRr7jKlZzehNdIYbkHd-bQAmbBHlpwAPHiorBudyvcezYQj2YnQjTrn6vw9zNKr_zZOMpL4Q0UZOhKlexgUslD4hNI3TPHQnsz5wCc4qpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hpx16vw4zb-JvP1s0zaGqYx2fcKGpLmwb74oMXMvs8KmqTkgCl7huu7YoUB3AkThYGfX3fpxy2NPPrac5EoWO2jwoSkCpTKAHnoCKjsK40Rt-sOq5I79gtEMT-Ak5oavgugN5-zRHlxuBru6ELAiAiHyUToen_Y2M7XKsR7kvgFloEqI_GSl7HewEa_9YYyU26WVKUczVEgTbhQQZIxdJP546C7J9y0evG512YK6ywrZykZUzs4pC7XSZm41udVMpOEa2g2bjtJ7cc7v4LedJlSEo-Ov0gp8bfq_-t7NRz9YTMsJ_fUzbCDaq4p4NR70LlzkHx_ioc9OzCYi4mQC3w.jpg" alt="photo" loading="lazy"/></div>
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
