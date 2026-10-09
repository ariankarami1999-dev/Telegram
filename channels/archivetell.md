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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 05:04:34</div>
<hr>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 825 · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbD6efolv6_zFsrmzzXBVQ4kySILD0x9g1jx0WJ3bpJ36Bi7a41Uh1HvL64D_yxHpaPOkuGBVyzrOO_1j9fbZ6rDrr5jYscUrlcyGkkkwINVwzn1PSyzhbnwBQDx_BiRtXUhI5sIR3aql0gAplhNV3d42ByWlXQX3XiqacljbTmLYLzJNv8BeSU_3y-GNjSzPKrlkDxGpHTkZ-Tlb91TO1XEmooFZDLpZvxXml2BweCmGczuwTys_Ba4PISPdJOYGUUGdyAFoOFY1n1AjaHenMojb4TwPlx78PmvUJzFpa7OOQWuKFADAE618eSJLz2bgZNhSpsXs2kBr8Ci-scCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShR5cy8_V2ugrIeU0mnbbyrZtS4lEsn3Xp_pikgjFG6lTr2w5bawaj0vgBVKwIOvd2beF5-mQgBm0pQSf31QZ1I1qIhn_35MJjc0pLn418ABjwR6_jHniVboDdEvaGL2KzThKHPNb1lyyuIoKg4xk1DTBxULs1wp5csrPzNJMS2llpwDDecHHZQY0g2QahDMCPq8YSY7MYeLa6IMZnwpXCvX4KfhXiQTpLW4ZdIhSAOBdCkSNIIZScnemR7iNjQHyF0M2DYgbqJnB9_dU2Ht2dgIGLgvQLoh-NU1zB1JboLNqxHGY9o_nTVSW86GDNJIQAwW8hxFAsN7JjAD2Y-Lgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLyrP23vih0QnII-Ofbppwbn0asmTg8hM8ppMhiDFK1MTrzIwpf5sP4gtI3eiBduHvvmCgc1mmq3GQDekYIZR4jwU-dfj_7LHhGyyfT0FUq2lTzGrpyLztehlIf-6ai0nYJitPa2mIw0NdzVFzuUn0SBNiWrMV0akm0nkLHVZoWYmDoOuiBIP0F09J-HV-8Hon-kS6AQojWdv9p_U5hgwzXHR5Hww5SCqrWavhiyEJL3WsO3_3XV-xLTgrAbp3v7WlQtSs3IQ3NBkyW9wzvt6h9nZrPjjvw1qMe7BMv33sDSYVMolwArkvCBMkCVJhY-pL7SkjhA6zXDSTsY2W0g6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=eA1mhuIab3vdBitxC_2b8ynnPWQIKcNMEfGTcFdNZn9pjJPp26zCuDJPSx04wOCyFE1OftBYxuYm7rzEvpej1RymUNHrsZ67DLZr-k9Mz1kMJ2l7iJLl-fa9zVob3X5ytVmNP-i09BJ_AtTyN3YmtOlvG11f_OMfvFgRnPi5Yw-MSO8uEbzEe_L74Nkiuaccufs0TX7V4v9Is4nBcMUtP9sz6iHMWGotdHJB7Y61sur_Aki4-G8GljVCxEBUhnhuD0G8Mf4H6XO4QEsiXvEa54MHVd-p2wxwEL_UztkicBFgLUwSmyYK-OBmmMV7ILRq5fe8UwEXuslMqToiKlk8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=eA1mhuIab3vdBitxC_2b8ynnPWQIKcNMEfGTcFdNZn9pjJPp26zCuDJPSx04wOCyFE1OftBYxuYm7rzEvpej1RymUNHrsZ67DLZr-k9Mz1kMJ2l7iJLl-fa9zVob3X5ytVmNP-i09BJ_AtTyN3YmtOlvG11f_OMfvFgRnPi5Yw-MSO8uEbzEe_L74Nkiuaccufs0TX7V4v9Is4nBcMUtP9sz6iHMWGotdHJB7Y61sur_Aki4-G8GljVCxEBUhnhuD0G8Mf4H6XO4QEsiXvEa54MHVd-p2wxwEL_UztkicBFgLUwSmyYK-OBmmMV7ILRq5fe8UwEXuslMqToiKlk8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpO-eAzWOPmYgZNcmd7C9ve50t9qN_VbYuGuCC3h3L9ujBmxx4cMkVkpgYmpAEPtQsdZrqYtvUdsmyWTFp1RIfkpsFzM3J2nSS0TwEiWEGYqB2pO7sPYMzbnVW_7Ts1aGFvDIbaKHN1IK7P88iLwbHL5k3ppXLvTSPrctIT8uh1epAw3XAaLzZ4M8ZV54FYWmaBEXVGogbtUW0zLQa--ZdFxIL3UltYUINGurr_F_PpX_Vna3tMycF_RwCdQghsk19h7LbKt1fKPvsHV5In145wNQ8q9Wcr66AophdCyjWToPxAQ_qekMmHUmWzqzgmnLM-wa5ElVxS77KJAMn7kdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBsEf8fSEFJ9QNdNhYwHy2lmCgwUdwCcpAmRONmy8ZkZlo7VBEvfoxEuCEEpYa2YiKZsg7C23sLuk-Xkm-x6mXGMIZua2Hu1fPcQmrQgJJXprdcVsWTYxTEnC7EDxj3gMEAjrDLPALggAsay53VTkeJUK0EFTvoHdedFQJ_UQ8BLinSUjFTNoOny5H5VTqJfKCHD9dL4CJ3WRFY7MgIDS6OQ9pIjmm4p5AGwb_6byL0J9RQFgjXbMnttvA3reKXORtqUTVYxTChzfbRkV7R2F-WgngH9qC-a5p0dc0FVAqxJ8Hth2722nRYEUe6vvq-9mLVpNGRH5hDHXSQFX3B08g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTT2IdZ3zP07eA5HdG18uokKOjQxYliD8635qvSk40OviOnNVNb6kr-aR5zogBd_f2Lb68icnmZrp60382IMBdE1zvi5sznr9E9iuJ10q-OX0NI9lAKBnIZT3b4thk1ZPIImi4croL7ieIH05A14P4AKLNtRAQOh-DCaj8CND5KYdfD2ryThaRiOLxIFCVQSReRjlQ1wY7hVYp9y9KerwKsIQFqEp4aNXfrjCcEmGjUp7NjlxGMxk_e8dsDBY1IOTt5ngIc7fDCMJEx7k0cmka3165kfLtwG22d0KRUBP9dJox7XxTSRuKWOiISeeD4rv5vziP43YtT-jd6G44M4kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZXalZwF5XemhPtc5MHo2gwfu9HbF36SaoUZDAUzqJbx8Y0Nt0lP_xPZlfaqjItH0Hcf0uvBnMEvTBm9wyJxb_epKnP-Zl-Gt8SGff2sHcZiFnA91s96HnamkjTMAbjHVs31be_mDZi2B2qBYW7coU7zb7WvBtivp8wSDZWmTBbXJbJKZuGDaqFOgnwwY2dcx4tJakf2P2_c7siqeZVS_dJGjVydJk5mWLHTdZd3hrOBv1SNPOQUB0f0uthpuR3DnjwPHWJ6sg0rfWjdffyUXV6ffMs2YjH3q1Lgpi4YJiw0O9Fw4JZWleSefzhpa00MNIBcKGDKbyzd1ttczPmKUPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxkITVZyaZKOnIZblfFtWou-Beup28_-WO8jEJjf4sBlZ85x3WeSp2XAc00K_MuRDx9aRZgp8C2EasRkwozcwwy2Cl2W0WRyJ5ezZxPWtoViBiLS2u-zb7WL4wdYLBNRc4tA1YpfqempoPbA6QtFctwox02n771qJaLe4KnXjebtTmlN8UjoebJe0MxUcQ4Lyb031lXGcyoksIdD1ErGZWKppz3yG5khx-idur5AGPJRJxljxn7vLbmGnEX_aSrHA-tJ1waHYEyc7UrrwB53sZ4x9ZZcqMug6oP9veGJZuByUGOS6p6H2Yn6Oi6sy66YNRnHcsz7PL43bm7ai_HJoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Uf8OSoc3MQzlK5_lPduq0ZAHqNJDNjG7T-wQhP4zX8XZLX_kGW_nT9y0z0c2knfA18QmMBd_ytScS4za3SZmAlK2VnwSwxfwyH9DodnuiXrjV-qVFyfdcADPzQzBeLD1esI1FIP6lcXSu8x6y7rARJbxMslFq5kQuPSHMablFJGNn01gFrwSy9X-7YOpOlBOkh4JtNXtp_UDO2YaLb2O4IuAOE1DHtN3pXOvXm2_1IMFOclCiGjLVmR5CNhwshB1s2pxk3o8Zu6YBeFHaggQdEKlgoITH7ultaLOU_z_aaZS2z1THKy-2dH4oiJ4uciGDyqMGo89V-4K3DTnfB5fsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Uf8OSoc3MQzlK5_lPduq0ZAHqNJDNjG7T-wQhP4zX8XZLX_kGW_nT9y0z0c2knfA18QmMBd_ytScS4za3SZmAlK2VnwSwxfwyH9DodnuiXrjV-qVFyfdcADPzQzBeLD1esI1FIP6lcXSu8x6y7rARJbxMslFq5kQuPSHMablFJGNn01gFrwSy9X-7YOpOlBOkh4JtNXtp_UDO2YaLb2O4IuAOE1DHtN3pXOvXm2_1IMFOclCiGjLVmR5CNhwshB1s2pxk3o8Zu6YBeFHaggQdEKlgoITH7ultaLOU_z_aaZS2z1THKy-2dH4oiJ4uciGDyqMGo89V-4K3DTnfB5fsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUKxadj51m4lfI_v3EfcfS4T_u8dTmBwyr3DEKBZAU3QSwDuz3kQ1aAHR6dzYJJvCUYYDfXs1FGZCCNjPnfR60p1NeeaA4u1gi0vPiL_LAsPY58qtX7mXE3yDm9Pd9VtaQ94qvyBMmra0O7kpH63CzPV_TgvNhVKqvHWSbFSPzC4UjBedQ6uXOzXxUFJ2ej48cb6CJOTCvL0MMMt2JCBKQtjRG_Q_5tT6C2knpNi1WcqVlkIbShkJ81dowuy38CBPq1P-Q3A5aGufI7HA28NQVCBfpF5JT54Y9wl8kL1Hngophd7Fuau_NSbAwKtBIKsPxswdDdIv76LzZn4oHZrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noOcx-asgE0xTsyvr8oVJTzWhR_gaCp3HlBDYQOjUX2o4N3wiR37lP4Abmz7iiskROtDzl1O4Z_HxSDC1-K2ead8_ap2tNupgVc9BCgRaheev1y06CzwOqo-yBVV5oj-YqnfHqA1ohfCPMGT0GezAFKIh0tpsaS6rYn7t8Lp_PE_CAiS9o9UmiD9Mya_TWMjW8_RqW4gAQqIWrJeXx4df6OUQpBkhCtGxa52Lan2KXwSdXHt0klQIczKhF034twzoOmOQ_uAYeGJtbUq4DH2epAHDRP_7I8tWjTsK43ffeUmvxYqvVZe9YmpQOZJF5SXSTCKHaBMWFCgZqtu9a61-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8Zes907-v8vIM1stmKCkzVouzW9ZzEwaqRWxFxOG2wSL0GhxR0G6wype6QfCPBAkXdMrUDLX3dTxQAv7sHexheMok2TvlDTy9C_wgsXyJ2ODkCbqRVrj9TtmRXcDHa9zr-U1-LFtA05-VbsER6-AKzfKj35g38STNmAJAGFPTuUbkfCHGrWcqNMzWJpnJVQn6F23hwrDxf8o0MbGft73FUfterAVSyFRjkpUyhoU0BeReZZJWSFQZ4CeTOt5mWru2Qw2hdI7iC3XRnPmL6ULBQBTCzn57-LXgPx4mhAUNS0ypU6FhFeQRrljrdVeYHHZj-V2xhf7l9-_relWzv0pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehrT5Sn9eOj3rTZnST1jiSH-iDU9zpp65i3jn59S2EN8HmHbUybziQKWeyYEDiExMMGiHF3IM8r7dB43ws4dMP-tUDfEOKJ4uMoz9f8oO5KoUjVjz-Y3jTrSjT7t97IACpfOQdbttCv7kcD0K7nWu1Y1sSU4Q3E1M3plxQPcAel7oE5_NeRJLjUl_Ffu1rs8kQfxHmGtf0TxioJCaYHdq9gVgvFoEBpU7rzqrUutbz9Ln8qV40TDe7RXqMlvCZrcdy8FMPJX0DBuZo2vM89aUAQ3B9mTBll1uFIJABpihq9r_owTt7BS4-hf3MJoknlsjTX1Mo012DPrZ-R3Rl3K-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyK9N3SxWCF1RietUvQb3HjzeGxc04a1XkDUFH097HoWq9wMcqC2fParbjJUfQOzyReSMmS1Dy23HPftJtA4uszeptjtZ0J8llpv_koqozGPu9oaLs8-RuRGFd80XvFfQK58GiKPPS3bz2dzIcQ3e3aYb_YwNs4Z9iJ6WzY_yQqWxWmBqeAWyjrrq4ALyDXYyiB2VNd7cgCCwawjlKLsOOIWVtUt24vfqYotm68vwye39A-Qv351IpYU-nF2Wsa9OPGn7syhIhJWe3dqZ7wg8j6FlRqUtrdFz_2XS7_kJ6I_XJ9R2kV7jk7m4yxHR1nbHEjocteRXizi4qO91BEpQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-_EGkCW_UAkCce8_09wXPWkoByWCBu-39D4nBuKkHCXCg7QoPUEOgTJZBc_8Xlw2JX5-uccEvyJkbh9gs0o-2Qzg2sqww5AQlBJvOZTxlMQBigYJH6Vp8TBQ1vK2YpezQ_9hXuWtSp4_q6xDqdCHUurE-iSL7DMMzdUEL66FI5m484gLRY6GDCvm7cqYNg5E921XvXuQNWHOKgs1t4QoYj_LaKSW4zWIAqFui3MFq05BFg98Pw7zNE36gobIKD-m5z_hdHGwCZ1QJ-5ya2B9NSFCrxkgxyKxs9tFPLr8WzkQkvtHPMh4tp77S7_MtGgtpjOl982P42EntWdyQzZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rb2aj3YG0bOvs1BcdAaSRAkgj7eJk0noxpey8OISBH807JTXD4htdGgptbVzBxNcn5Grvp4nAHoZ9Jr84Kd69y1G5HQHSEcake95rohPRORq-N6EopolK1TJaBr6bD6aOo08KH1FaO7_UypwKfFVUPy46Ktu4SXuQZYg3WqGH72p5FV4vCBP_uF-fKKjkTgiKYUColHCRD_7whXr6WvtWxVZne5jxAisqxVZG0UkWDumlS6f5RDDDkuxh4IruxLs60XMrZdGeG93elOW-aCIe_3ix9jwaSxMuRbmM9t9_wfZKQQieoTlqdDmPm2Ujz4ZEqkb43923wZoAGhB8SmJcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lhfs4o9a5LL931QoREGPx0gJUjnN5pELVzA27wJJ8c3HZKIJf4-IaTFS63r3SUKjXGyqIcuddOqOXLHFUKdI_UlXPFrtN4uM043mabOUtjKjlvyYreIUOcQBnz5QdU82PBmHuMuDKB6hs4W2YC2dEsLrklWIJO2L7BI92nz11FvL-acFTcn6S2d3wE0gFed1T0O0lT0Y4ZSoXuNKpONPRkb-WJKgMHrotppSVA2u9-WkYe_xN12RpB5SEVAuPoAVx-xN0TWa9_b0HXO1wbBzPdQx7amqTEjhSWBsXzim5ibWdmLrgITydHWnfRKlRzJA-jmfpsT_LqmexmOnA9lpdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ciXaygU4Y2zJHoarPN5vtok2two-HPdOJu0ozv8Qc2J6oz3XJErUi6wNeU3t0f-gUAYLClWhspFw7sLLAsGOlXJ8sIweohyNTWxSpUVNSxrDbEl9pkc-hLXFQJoUEY6hgosqksrKZoQk10NutkRY4JxXyu4_1GSLLvqhvzafU8vzGtisRXKWu2CSWfbbMF50q1e1Imwb_OQroSqgbzqSNVPM5WGf_C6HkOCth9pck8GY5lWjbqWUrbcJZZ4lpN3cHpj4wTG3yO-kSY8Wki-IxpT8-tQLSAD-dnt0uXvcq9rvkLc-805bjcomMwK-EjGZx8PB65tHnuP3ltKie4_yGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cswnj8xOSUCAwG1bS5uctPLTulPHS0tugJV2fAGZPBKYlyJZ1iZ7tj8KzhWdL-A_ULw2E2m2LK_Rs90nPScyCioM4cxCJqTCEF1mXiQ4QdgBab4phLsXYWoBNUwDF_X0ukdE9DBWMKSgv5P_0mR58ku7I1Dnl1HPbfED5Qm2ueNzVJd9Sp9xzYg4Cg9XplmOGT17wrgQiA2zsKPm8aJ-h9Uxh2q_OUygNWHQLKe3afRFzMOFgjGJbu5th0waXwQhbEB7vDlceaQeiKpssTqqHrcx-U90okVOpLGhUCGdbARfwPzmL3bKLU4k72lC7fK5rP7cSsXIl1iQYUkCu6vY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvntTMGe-rUEzzBR9dnlYx0V_mDM90zOSpRUmP6LhMtb2Q-LckbKjQkxTOM0Hl38eHWjEEElFGTD8MKjGlYxgiWAKZPWG_yEhbNA5tLv_inj7lNNqHIDcHPdMLzqSI-z0pWKHbSB_R0hqWbKb2VNm_nX6JEjahSn2U4SO0zLveU4Z6hRSWNoLfOfwHx0kGj9HTN8JcfQ_J1X2oerFx7-SUbAfCkdlv8EPzraag1yaP9sjZXMcdOnXwxAO68daSHViJObBE7LzLZyONjbnyF1DRxn9VS_yxI7A9L21851--ixdem3KDMP94PnBxpgPuNcxZwzoqVOb0pkekvYizFIkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOnyqv07OochJwBcUHzajeiwL1quyfRaowqBUpEFXllMKqFr7w84HCC1QF38pF2fa_Jg4KESjRy-8TlUjHIghpSAfedSqGTLZC7ElschGZH4etBlW7Rli3SFSeeoLpsw1j5ghZtU6aF8MfTnMtHb7hZwyM8urwyfEcyfI1x815hv7VVzPCb59_wcUgHFQkuvYEe30yezWQ9WQ0F9pnONjuzWXaaNTUd6pCBF-zIe8f0vbCT8dbVIcLAlesMhXg60Wd4xi1DFA2t8cj_opFfmNMj6Bv-Vv0HyOENTJPMyhASNo1rMJ5GFi9sPbKX-yjra19EGpHkXcSkCjgXYT4WpHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoAtIPKyhEFNQlkREjNf4qIUjR5bIdtOSuKhJlQPHZb9I2iPkyaZCg5xiuyDnpXTJY6u7-yTL4rn-jr6jN0_i5oQVqUcHgamV4DpwdZVf_qCdur_Kdx8vA-I8XHcVTowRBKZ01ickOyLPu0pJvIvsHErDPyBiVjeSDMf6jTlm-hnkzMHLYYAkWDTc2CGKyp6np8AHO0EmtGNfxalM7SnEIaQYyyRHjjQfyY5a0uQ9krFxRsTQpNhXlAizB7ApECRHdSQKt9Azkf5q3wK-eqIMUoaIUSrrfVswt36xM4a6hRTc84uQNHbdfLiIJxyDTg9mjyfDYPJjb5_terlp8SNJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PAltyJLlpRwBFT7KiQdDqTZaIEyUyqPtjwM5U3xb_Gx3lUrLGn3b0qBV0dg3M7ElBZpKMo5_gz3zOQBTDrF2xit0hX6ieleo2AKNh3u_5xVCHKRJ3OrUSdd1sQAHsk09SWS5Oet7BrTc12n5fzlx8XHi0znaKuqKSC3pNQ8RBplY0Oqq3UBSV7JcNJBpVmvNgJlmEHx6szfOKxJgM07l3pm8TMR2sF3nTtNlkH5z8u-xY00OZVPKPr4fFCrrtUrZ6EZl1XGOLh5lVrIzqpmfvozfKIk-scQaipbMAsEzAULb_GT-R99eGCHAtpERCfwIm-kLxQlafk6e6sBHCWDFBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrMirb1skzBTgm0ifW_eqnthtI09NPP8yh_yG3CBglgt0GrrqfY1bVBOYe1Ck8dZt3O0y_-DwzD-_SjCAGlibBsoqQy8jG4w9eII8Q_ovsJlhT-Etuy8hBa2NHzf0alPIrUaXapR3lPA-qBjVvSKVGJFRknRPqXfOp_2nDk9kp2pdO0XMUmta7SYweWZKjDIXZgNyd7pFexIEFFF8Gi6R6A5_x1MEYG_Hb8eWTpiJDDlEi_bt96_l5himCoAywH_qCx_VGr0sHZxBZSQ2Ltb2nTXjxvQnlrLsUw4JRqeJ6_Q5RmtLqiDPyKgi4aZrVhHCMposrkQ5VxW_IpsAAYppQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX7_tj1q6CHox4S_sAu8dRYLdU9ZlJwCdk7cq30KR1H8R8pUZejhOr7UtF2LunaUBqk3ptGdFcE5gcZQgL0WNSFaRdFyuqMnpNnIudOKlsEmvTrYu_qvJ7aRLD32mzo5CIbxB5_nvoeeYiE-8jy0pYpwptD-2waumM6QixVn7aR66EXH0u2bF-PSYdGS53T4zK7rx8H1axy-tCKbPr7P_ZupFYfjoG5juF9n9hrsuXJsydUT-fFikJovmE2-2P57jQbZRwjqr4fCoOGbWKrJnM8evXISkdb3sXlrXv_i4xpWVZKX3TbUpV_jpVM9TqVd8X_Rm2xMEQ5VTOtdnvTwag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY77W7zyRCcCy9MSw-yzpqtQC7Fkg95aOdV9a6Q1KEwbnTikHXXeHP5zshb0RGV-irjx2krcpgrLuqMVB0dxPw026tnhEvwuQ0CCX4AbIfq1JWxR-WuEyW1OrL2w-UtWW4Z9HndSsMYsjZwpk7JI5b5KMfnV3A4ljNnt1rE0gcM02ZCwSxhkw3-ZWm4oAhExNczfcCW8wTQJmKeAFOvWns-ITrRialV_CaSgwteFYyddbe2tKuJfRhooLHi-s0EioPZvwF11zku3z_gVvewcV1EonG0kl6hTopXEgF2KG2Ag7BnHW-FlRf6wCd_v9KU1dcHL4JEWc-6fjayhu1jG2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kzw0jnkcvkejGiIlsFHyQW0hbS7TaqDqHeeI3MjBSSwW3yszWpazEvRXGyteSSsU0O_VmUU_zpuSHFm74EIylYSIm2d5AMJZ4DWmfbdFld0B5jzhNatjLndJvKY41q6jHHftmur7p6NTnbqugTuksKoPgDsdCcLmKY3DojhjFfPzlmbPyWLBeLV3yWIUGecSotSi6NS5ZO365DapNpj1UXeut_S3wkxCEcheGVjC4KmLpOxyS7sHfKealRz8PPCOMYQRqzvXcnZ7gvNwOy8kxOILk5jfVfKIoVPsJABmAPakqmoBHQtKLD7zuIXxWHXq_B3aXxtVUEAj5KhwQ8Z37w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPUMbuQh5JHJEzliEkuWq5jLpfLhp0bGsoh1sLoDYmltcxgh8tnH2_E-K2O1aBmv3ajJ6_HmnP62HHZg0IvM5WjjIubQVq9nWsithWrn32dE1Cc3l7selec-XvwM63-3k0kAdA6n2_1YuXQCsc8OtUxMiT2xG3muzb5AQRh0U4O6jpwybDmIowH3fcoJg89dsI4-AuwRzuIjOd8T-QFfC0mth-TF9DsNJIa_C_fikCRg1HSWFnfDnQmRIkffGa2zTZNIlp1c31rX2jgyN_calzJj8zoV_ANiV0uPXUHTiaAw6PVAV5_qSiz6hdD9xmfvXyPnOm3XKfLdgXWO_38Z_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJ2mbgUAdFanCgmAOHB9BZbq0zscDpwe-HU1h_yJ7baqEudI1lmWK_lQT-MzEOZV9Vzx91CZ1kJK77XutfFxxfOiiL84YcH_vxD9-YKMOkunYPCov32JrQSR94rG4EahdA7gJLxnqlZJprOADG8KsBz5Hv835wYIH8C39CngLXtOWFLoAlHNuzbyY3JPGGv-g4WdoCP_6MxckWv7mYHI_IR3kv5CY6-BSRwls7Pu5egzHS9td6kP_5Fzv3rYLVWYow2ysH3ilD95Dt5uxqzXDPfymSPzLrLbr8CrcgEM9018pQfIX-fYqaiPjXm60oWxyG9FagRTdF_QzmP1uinokQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S0g8hdbkv2HF2YN_O_qHKI50r5kddrZAB5lrTH2sxC47TBMcEqz3Lm7SnjK-gi7DqqBWWI2KyfhNy6QeaHR3V9iQCaBi2VDwOnfn5y1KgvkN9HHMx6YZZ4UjwJ1R1qK5NfE7nP3PNVVoNXXd6qH7Ntkhim3T8jpvsr5AFrVOjgZcWdiUsO_yL5gNUVJOKm3qKIe1UKw4Bgu6CPsLEDpBkO9Fx6s5kNc9PlSvhe40C9g5cwUXic2NdJzPYwujnYUE83P_uXXinLI7sUvoRt3a1m7SZyE3vZR014MEJj68Q3a4GHWoaOlvznSlx9lT6RHPwJXrBIeSIacnVZJlGVdgxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRaOnZFCDVBZemz9tI1cuNnMjjh186R2FUl4QDoO1pLBcn37UAg19LHlBPowRHzYVEkstSIkUGZpzPZqM9kffzQ0dQCCpRSkuG-cGkJVzva27cIak7FuA8dmn0-RgQMY0R7TEOptim0bbzgus6pckbOl6DG5ISWfNYUJVYAQ8ewLR7juMH6opJ_aLUnvp7NTR7DyUiLD2QZot7ePIZ7yuFEslPmvo1tjoXgR2XX9f_WnqljQ4aGkFU2hZ6w7UJP6pLBVvq3sdBZneg1Uie2FU5nazDCJgSZdHFxFaoGgslcl2reskqTJeWk5QiTgxUSIatWjZWYQp2V95YraNDQU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2K83iFMmVKFfVg9xu6wj6ZxY5ZMcVLJGob5I1YIov98JgSrhtD6xidCZfYaNJnifeDAXOUcO3i2kkvN0hFO1SKSEkij96yBahKP_gOINq5HVJT9D-riiny687aF8f-O1pVIRcr2oajVCQqo6EwPEAXq3XYIipMjRQbxN4HTSkzBoMbPmfcEBt0zaO5ZiQ7uuKG9XX-C_EEbDcSY5k3ngD3z6kjqo87LNKICa91nv9swik5m0xjeK1JHUmAsV3PDcPMOIVpWXGOHrebHsgyosozmKp_SRw4lrvXc3TJT1fnSXhhGAc-m0W9C4yHuHprOlvGEEqzkhwkrYmkm8H9fnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwPcdlf-O--fz0IOT2s0VlOOkcKNJfLb363NxKiHfMUIkdo2U74QnJZvycNkkcT0f8PhQN_p-JGRSEXT4nIxBn3X2WLicgTEFi9fVe_44xSodVKnwO2hLXjpE6ai2KQPvh9qp7Y3qOn_996Sm12DLHtolOJTysZy9UvThXmT_kgUXWgegZl3WsWoBIpdleTy64lQgFUBIv7_DF2DQuHw_PzkxMbWQ_Fdsih26o_h6EXbjQ7wAGA41FfR9C_5y9XpLw5GodM8FAxwRKB8r6I2XlGzjTM13EeBSKsMPSlcY4OKXG4fK5veQZUacwMHNXk_JyrJU4_N4aW69dBBr_p7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS1A-HlJfjbWfKX0Md-sVStOZjRmNiE5g7_9ZUI-Yvc3Q_hY3QuJhbsKKRRkGoaha3NwgyEWbRUqQN37ylUVL44Vf9Tz8EhPBB4TkwHtpGYjqaeQqyfI_NiFawpGiQe9pLwhXCkELZbNuKkrLWV01xV117SNlxF-tFMAdRxS1EZq3gjFas_6jIlFhkxHJ_QmAqJfqT01ZHeayyXCsiQTDDx3k6njLocZLJiZMc_SlXzRBBwoaFA7vKXl6pmqTlvqZ32O5SyqfTNU85Nw_l5pFRKFd8SeJzcV61kCE1lXE-9bNM2KL2Y4W45KJ1-9nn9rlDuSqYKKafkWntKamtlRSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIkOgnhAnlH7bDQ8ARLrxuHWiZtPJlCBuZl31-fk20WLc9IGFEu_p97dcJuvzcWdLFHQj3oXFPwraRSyvmAbo0YNQHKqrNoph9tg5wNqo8XBwUQqGE0Of3t-0TXKFuBZaIDSSPHzO4lx54MmylvUOXwL5KzMb4YC23xYPm1hCw1WJwQetkPii_vdYcI_GF-oEOwioEUTi6r5yCq8EFIRjXPp5GaXSMVYN6IFv0cucLl0xNj_arJIKk1PHH5HEeYiADdpawaACodcw4aYRsbygF69PXb_S7IhoA3up7835F5g668uLbfV2AIFjJ5nx8AOjRNiaaKe7Qe0Bcu4N1Lyvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie0nPqBR7lxylA36ltSKUt_qAbNeT3XaZ8RSfWY8gTVQSjParzffTmMBUVVTX5fa8Z5191S1pt2xAzZ1xOkYrKIB6zEd4XNzlnkC_3cEdeFbBbK4OLyX4Tzee_PrR89ILFSMIi9ePyJn2_VnTcQkwSrmdupHGMNMhd-ZkfFK5YwUX-dO_PZeWhgjBLM5nl-wg9TcKDsfC_3gWuitdW42v9pTKI0KiEi0T0tlnIWphg-bCJKowvglfAksZsVn16U75gbLugoD5hICW0Oy5fCjM7wNajV4MQ4SjdI4vjGckVdL31V_6KxpSVoMfjf34LFnhqExui1T8UDF7vRrpLg4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgjRHBuOOqUAD-BJvvk9rTpL0JzguryEEWLOHi7q21S33jf-Oml5CBmQ4jZ0Kt-bgYFO2HXpLBMefawvWT-Mr3qrZkV6JdntBUYO4GLGFQPhCI8gYVpEkSmuzy1EX7bchrR3oOXBsbHIwLAe4vK3PCjS8GzRj1THJ7eaUN0kn1wHZkS7N9z-LDaJUyBvbMKMWo92pN7_wmELkLc8NnLLCovbXzwXA5mKyEOo2GGhx8ttl-ohK7MsYOau1CJlPrrrBG_1VAil3yOmgOBU5G-KWCjuFcYEBM_2fbY6gla5D4gxurXiWKK9hdtp5HGdbtF6-IpvjV2ZbR8ivmSbG35Isg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJwAHyqdtxUOl96SJPIS4eY2RtjHeXftw3hNt7GvIv1sle-Y7yhoAXtWgtp92zpNVgoqw-N1tpxEyGVU6aUiMoe5EREulyIjMEy0iuUuS-1zDVzw1tQNVJ-XTnGzX4J6vq-fpLS2s0D6IE8VRbqk5gfIYPWEe3zzkUKK3X-tvVniQA6GI8eW3x_o5dz9to50mInQECDQiHYGRjv5uMRN_yXPEusbnXHjL1xprZOxZ_CZMyEjXHdJ85kgFGUfMnMqIEsnjPPbW48JGYQtjURytCWAhxc8hmxMDxwD3Y_95zOjW_crMtljY4LOyA4bhINi3azcje5ISTsKaJmC5G688w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb_cPrOFIBu_g8KdEjoyjumTxtqWgttVIWKBNRuBUyYHunHWvKey916gpngOOhsD7UteLFfVyfcfgSc5B0XbucGWlV5hZNHJQ9iDRMORCLHKWmAIOyjiVRSLJLi_5KmrXrK3sob3HxhnkpWR33r0T79y4FFS5SK9bW6qDu2i07SWrgWSaD7UOySb7CPTdRSl7JjTmsHFmA3nwVgonCbHLpMZ4eDB9yi665HsayE_CA2RUL1yDzmFHWYBLb6gkAmokYXeS51hgJHaWsXjnluV8pHWlGDMoPPMmWdzh9LsMQaH9Czk4maj-SIC5-W-_VfNlsuFdb2R2AjyQqHejVeySw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrlXJDjUQIb85zz2duqG6HuVUsB536jkMDTu7adlNSMtYcYksaToTx_NK0GmU8Q_dhiGfZZ-aJhhDZt9ZNdtG9jd5JUTFLx6iH_MSXJ1sc9BhoUivX5Yf5Sd6RE6ozzyULrPPDVtWG6-wD7m_0EqnuedoYlccBAOH3-voSWinIdd5R0wJKet3FbzkSvo6BkWZu7s1InZQZGqsjerHi8IvU2nEZgbrksTRirpLDlkbEKhyzKpzv5Qnt1g490URY1DB5waopc1jgVT1Yqp4p1aKNEThF7MHVUsOfG7ioABQIfnt6F_14jVVQyowgkQMtLYCwiMT2sbE_Q9ulbOKeSqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GoVwjhY8SVd5PFCt4mZ3UOsrFI-0eK1Cd3wsLbc4X5_Rg_LXLwKd7Sq5RcRLpixv8u7E4MAegK68nvySSJuXNGYuZ1lp6WV0rMrvvcTlHCi9xmbSCmWTa8XGnudfypoKQNGNw08Sldp_d3EPQDH0LpEG00kvrUdSME7OfYdMvgidNhMgsjCeXRsPo3WcPmxAW0kgfxbpnvc7mtzVnpxvXPojNFiu7hpYUikLUX9OZxEaT-eCfchEHJJgrTonIKCsBTiW5RLrx_J3lcGDJJt5DAvj5H3BhiL3LLK9hR1xLsJD_zOniteRDkhFNY9g-Hp7CC_q02kFxy8dcn6DO8qBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FlKE2WWMtM2ZT4xsrronGrQlsn0Q0vjRa5YmXSYPyyQfChz3Rm3FyJyqq4fnLlNrY8bWwO6P6xmSWc54WONo3bShtdej4ixSXU_JLGfGRYyh4Ys2IXIpVbEiW0Lvet1ZpvQZipG1IWlXp_2Lrih_Gm1sm5TR33ueD_8uUpw7amGez2frMFjhXvvp3PU4Kg-hh9rCciVryXwXbh3cl6yIAOoIv6mqhGVrlccw4RZoltfOkk4FW5X_cEl7QxG94Ytyq1IegmYMN8i6P--80VRUzuXHf7HHzXbXjPO4IcOHJscByNPsb_4epp58k8UrA_l7hQHhGgeUkQimjixc2_njHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrav1Ysk2sL-vZk7uYpy0rtRQcxmaBrcbvTVU0IURoruLLyKzEbmd39lc77siylKfvdVwZW2cQ6ILgkKQdVosgpemDHMT2lvObmNL9eF-0cFywRWOhstBxAywkIWLwsfqiFS3ZQI4RHxN57j0P_JtVPXI_SwTNMS2pMUtxliojvfcdWChxMG60-AUPdobGND4zJPnEEfQWRmSJM7P0a5MjYJlZZP4qITpV-zl5V1LrG5tsToNSPRCsmwgGlu-GTmdlVPXoGrGPi6uuGdj4eEgPJqJWdHsH4ylsIresNdG2sckYZEmxByuvdivJ-UBWQy5MGFVJAR1GnS15FfP9nZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuOCweeYGlOFu4yfJguCPH7BeuTog315GNahEkWwvFMoBqV_H49V4mEDEQi1CdhUoy8rRZcb3xuyQD0fBFOUcWtd7x4-m_h6lWrXaB9NZuM-QkauFV7tqOPYDRBzV8gS7zo6N4j14FvOq6txV7aawUCUY9616BD3EqlCiyQ_ACsbd8U-bAAvaLugxirF4H9JXfuO41bI48QejUTW20hrnM65BD-GHX6ypngZ3QRARoSWG1cWWPl_9SXQkrXv4miP_xngS6wyokDTkurz3DRgIBL4esumDGNbJ9_3neLSUHFeDvvxhub2Pr4hU676Co483ER6pc0192Tuta2cxTEWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f8Uf4gjQ1hb2oFtiofnjOPBvkCdDTZqX7XVe13_A-PST4ekSw4bes7CFFip_0ai0wPEA-elrW4oAwWRIQ53YLXI2-qOVZ6xaMVSEo_PJ3CMRY9bmOe5zmdoEL-D3xGbJRzu_sYAgYJjkd2Md_IAIqX44hcCeM5Qm-1LQWoAw6wHncUZGH_rPf7imbhyyxAbpqTmWt6YfcTntE4MzexeORnuPzWC79KNtXS0g_geoWFC2BZP4PMI1QMy00_RJkSt8X_7JHmDfKJOaNsqNzB-HFnuNwjDeHbXMoRRK0rvvpYFnkCUSB1Xfe7vZ42qY281h8kfsHcPq6_GFphfJZX7zcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZT6G0Fben1qp4GB_TMgcBF00kY8QKCYzHTkrK5HXhNaXgMb2FIp-u_qpNZ2uMxMjSUaA_dL3AcDZf_y2erMlkEh5l3j9M4NEKOxP22vcgk10Qgzam1ZCcY8lx6a4JmG6qRy_D5QHJVAx8c-Wg4BhtkJ8EFGkpSlrdiUZ6_9xslU9oHxTgQB_EHqIDbm3ttegCmAqYvSpCkw9W3apY2HFsiQFnMaWNc5byV3SYjKg19_8SBS2PM5ft_mIL7Jc9oeDs8ao-ogz27iPfV4KzbguHp5tTPV8GBq312QOomdTnkOXMzw2gGBQslLkavXMaQBxJ4XPIV7PUWw6Fx90YGz9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKqHCEw8_bAXwAku-250eiy30-JwQA9qwq0J-V-5Mt6fiMCs-wUaX1s3lEcGZLAzkRBT0ow7Nto-EY5IWNU0SaNW9fnIOra04eyiXuc_fL2uV38RrPdXfqpMIfSLXbgD7uw8ozpVdLbB_6UGlnn_S_pvqjqDiLNtXwKy4AQWl0bn5rUDJ-AwTS2w7VmC-qhJi-ja8ayA7vYFSPBe4Ok_9Q3hUIJxeLy9g0NUBhhW91cfnkl1rPeTAxEn1v-1X9SKR7EwacuV5lO-NOiLo9y5S0uRo494-LUVbVD4gvwrwm-83FxvEyGw3kkmfc1bfonmIZoTEtRCwqC2S3nStTJF9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gff9tl5iOnjL7Aet684sSWR91ADSx_CrZxyse4D1gLdySYqO1-FnAd5HBqy68uuYhHivXadSfX2e84OhHe-cViSEWPNqApDbv8x_PUaFgitgAH0Igh47GJWXTmvNxeZZ0KYEWu81sH13vbH89anAiHgCXJZO_oK3tCy-O7tIgj4M_cLaCWtl6PM3_HCHYLqs-ZCR4W1qb0_u7Owdd2ymhRd905KvEf91iyO-F8jeZaz-L72z-wM-EoJm4Ay-WkXtcmfL-TfJKR4Oqfuvo9JO18gqqCZR4nMPXceDo-hVVO6W-lQlXs4v3AZGyL1FI76Rl0dFifVC1e5vgWRtwFHW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rsDCWPbHSox_u_ewvY_Gu3q4YbAzVSWJqIlJTJv1vetOALI_cwyQzt88g_mFBWf174t9gae6M0_EtbhLdyx50kilyKJtOLSIQ0mlSWtx2rTkfRegDS0dIb8mDdMKjAPmKgmcHBOSwtJVYLKuNzrHzKH-VEtjtRJ5YY4Am0W_RDUL7WLX--w6Ufbif--x0A48jZ8T0ryefTwGM26BJPstruNR2EDt8ffHPQas2TLte2prRkoBaeQySjnQ3HuI35dBn2Hb7B6-SPG64QsWALCrZpscPK6nWv4Su1cneF-tnFPGkpTRl762krcLa9-MTuaC-kkFGtMMMroOqDIMNSevHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKIrmzWJe5iM7iXRtlM3de_ZuLa7xxLNebORzRj1W0aLJ7_nQBoNFa3zrudcXvB_VPeCI4EBVHJMvvr2byylOhNfp7hCwl4KuNO27pVkmsdKF_KWQUnjf5BAFxy8LnHFlEZOO6QqD_YhS3qoujIK1Q7fMuUovNLiEO7rFqILbRP_s4Vw16j8nevUPGoPpNOYkVzCKuRM1FOskyZnlkXw3aQismpbH5Qa8E_21XjDPTES0AFHFdZqjrSv-5D0vk1NMfZ64SMLBZxjLvce3BzjIMBuFXMNgVvaMMPFKKR-E8X8swEzoj5XOVp4OzxwmGEvjRfjBoVE4JXaQvQpzMg9Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDpxO3p4gtCtXZ_RLjBZpnV5SYnhPBQGAlApzj1MEs_v2L1wb3TDnlD3Ke1qKgXC42sRl_yznS5bt57uikaWTos_ogo3YAJCAJ2CWTBbR9b-wOXhTKSqM2GzoHDvJbQT8e9uTcwAcsf0dno0J_VySbGBhr3ozT0HeHjqpX_67O9YZoOEAcXrgHOtzdMiNizPIMvFUICVT-vqq3HRMdMnd_7dELmsDJ29_EfZui0TROczGd5GACj7aTd3BFuFd4ci_jPBvBzDCxXtN9duadSTEp7Wv6IdVOuz2sT988KXSu3X0sWymTuT2ul04u_hMrGuOlHKd1ttIyzkW8NSKT5h9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZvegeJixuRzHWn_JjWkpZqbilrp6CcXWQajHaYFOfXh-rytmxGVn_Rh0SrCxNOtbs8SLfk5qXexJE6C6nrXtgqM-02daccShuJJtNlxTfB4BEEVykX5hCyaNbmX04AodSFKBXlOPesHpdziGQUQrfRjCYN9DdiQRKb5UkomRkKSxuavE-kdR2e37odb8sUWOSDCFvqxiXzjNs2ZpvOTJrykqqcI3tA7NoQiphwcAzj0owOB3apXHNhaGhKqH9IsvuEy2vnJ2prTggkN8j1Qv0EBFWwGNpNPOSJihUjDNvhwI_BPdFSshKQpldOkN83BXqM4iN6IcwhBIcEUcFx23A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvuJmxWyhfPN7GqCY-sysBSAaogMEgiHsXwLuL7lcVsUziJc-NQ_NTgCM5uAxbfRaA9AJJV2wwsvhKf5rUleLDKnEHMauZZFgpxyXW6BYHDZYlm25DonxZTQPfMHZFVYctTke1zLntxJNh3se4y2RP1PhZJAXBQ9emwb_FgjD6boOsF-3FgMEvU2PX7D_kvMONqodu4yF3okQHKV2ecPM_2C5P6FP_tcTH4B0kFps0IQJRoj_mvhNzP1qS-ZP2VIff4ivDJrbexXNY-0KAVeA_1qv7krkAB-h1mPlimEcAxwCu-HsnAntLuDIYy9MqJ6f-ntXnh1zfxJK-tBn4ca9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqjgSSfO1O7xcBwAUrAcNztYQLIIrFQIFFB3088KwT4eZ8cFng8fUOyaFDFMY9JA6b-Szhmzb74v0EWyBIsg1IRms3UqJbUk8v5_EME1q2sZFPKRJmqiCFA7p2qSN5xWlXLgqI-0D0lNJ25jfmneFw2-hV-nsQvM0rtwijHNtnKl7eyWv_sGsa99Ezm-V5S39oeenff3alaiAAx1jjPZxQ4vOkUCJuEECj3wM0Z2B8V4QvpBcQhe6JlflCq12_Nn9vwHt7iCQCupN2lL2dZZFHa71EQNIdYeb7F79cbicJ5DdtlN6rFtlkxfOltiYCDHLA-txUBLp4FVS8VcYWV-8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkjWSJYmeAXzQr0q6pX6sng5beNpDu2mxxEUosTeirvOgOVqdGTf3qDk2FR6v6aTMgM8O5i7uvLPc9ifwaxZWwwZgPhjMPuOf0ewwNb7aJka0NZYuC7Se533U-eXMPmCvAIvVTClsn7WR5bFIFII9i47P6D2kDlrwkLHkoln-CREvqp2ePY_tdjULDP0uLXpdMXbVZ9PvGbK7m6N5Lwn-mpOIARff5iD-jwoiL7XVQa8pCxHchNLbsnVpe7E8hbpjmx2k1H4Iiew2vqlUnoncEFFyybPzzThtEyDoS6YlN0l59H8iIfi7l3AVXkYWe2f_3h1b4zXMYAgpHxVwk7Q7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE995LFBLiqAo66Vp9wpDA19VAbml5kLCnJja-BLI-1Okl3Ivpte3sSPCsG-D7oea66yhWRVmxWL6G4FGX49JSGfO7UDX-hYdppk7KkMXHm-IsulzRJBxH2Oq0ax6hb3SNhLR7MkOXNUNHUNETC2WeCKiVjqKDMDjTfDEVr5T14EeZOD5PpWFF3vaqT6yxCWIHdU03b4b97YTRNBXjd4EVVzhG-rN-SQHgj9F9_0vLBzH5afZq4NQcWo0HDQ03uo8sZMg6B0vJBQ2xyhje8zqeTddA-O6dRFjAItwfxejTY5L5VIZlBIuTe0accGvbEEDeu12HxUdTKS5iJTu_KaMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5l2MF_r1WlV4GR3QCzWUD4l9sMmvbpvz9mUgNc8IBmkhxFhKonbjDLDByIYnHbPc2Hp7EFOq1ujVOgwM9hkqYZUiqYUqVtImMz0Q4n3e3WX6dVHu_m_Tvb7KyFIWbLxpwr7p84KJ7U5WBq6A3LKzFfw7aVf8vFJSlbJyGHu-zC8LOdgfzAkNdjiQSIvGpA-eJwHIuuQ82hcQXvJzqyix9IlOyDWSNIWKLfv3IJ0nRGX4KiaPjdY39LXozmKxKTJRaVtkzAzHf2Oc-nCFJfnuiAgOatI1lcVYa8Dw7OQQsTwr5PyWRO0NAhCmfBetDufXWIyLh4baNvYNZbbycU0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uO3o2WQvXJA45z1Kal-0h3m3c-T3D2Lbw2ZgkjyJ9GVAS_x9Ly86xZTfHr-XpHTtdxPQFbay6YkiVy8abUWxVWE-ZLJ4KYnZY8PdHVzp1pMwYN7dvrlwPevsr8TFlyZFmG6D-81TlLEFz-tUztMs23HhimKLj2JXPfYHkhRzp04ocCzkvviRfo2ocWudnec9QHJG_82wodCaKwYA4MrHEAV5QI6ozr3GLjXvf_bAmGoPgpPA7W5hqFsiHTAZzYnq55diJMVy6XoaifLFy_OIrC9I5Ns8BQrxzKoMviLMZopoakrBOJTunX56QLDElcz7c5t7hEcfLaW4bLFQHz9DKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbx6kRexjz_aeBL16HvCR3OIrJ7V-cc_0UK37JN5lp3DTLQ54Ofkz5CGPHOOU_C0bbgI_W1pu-8OtqNHq7ait0zABWCYtVN8A6olF2ynB55TaP3R8307pOze1MI_SrR5YwHPyBR_1mDOtORRrZ9_UWEIZWg2Ml_M6VZNyQop1Lngz_26NKodFjQadxlOPEv7aCANB3IuGfsi6mFGUclBPxp6qttkX_A3XLu_p61sM14JKThdHPMbLxGEBSMaG3qZoXWm4e4j1IuALghQC9iWXh55UUxRuMNAWTFQ-lNJm8a5qTRXXlMObCTyLCcoz2KuxzMDryxq2lEJaFwoA0ovsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AHMt4QkN8VsG8WUn7ne4bzeo-PN2QErOBLI9m44Bxew3NvBhvP20XUD-XlATtyyeXhd4Bczv8Jq-2UaHqXc_oTZSBHkNsUIoyxIif4cJ7UQpB7DwWIz8U7K3JMJk1dt67bQBMGW2KvHppbtHhctpObNVso3BsuupRWli4_JH564LfFgfA0GMCvuiftvBUbYouH6lB7wFyJgljUM8uPxOug4Twt7VBBpFpJN3JI_Si0YyFnnqAFZsOdBGSYVLUG0m7TIwP0gAO8-NQIzynXOaQ9DpeqZEGdASjHpPUmorLL6I-aCzNzGfFNIJDqddvleOaGP2v2lR8zJ_cYF65P39Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9BwoAIyBIjBv2n5IQDk-wQYZV5LwJ9rk4BJoK9t3LrNCGmCulwa9aI81U96Vh1UnsoY95-1wdOq1Y77xmipFTFU6QIDrmHilnH3sI-1G5pCUE_rnvn4oR6YSbjlGO9emnafQSDTKOvMQNMJhZd0kY8MvZNTPvafFOyjYF3SBoJO5u6IOt5UrvLSQeZGG5LUvo6MFIdxi9GxXsE4uErDQOFmgf1obv6ROvrR83MCDc9_bHtWHNRwlefWdsdFfxJoxR4TgjOhEGYbk5BZG_2l39qsHDUsqYUL-7tDW9LHYFWfU-TVAjJBSrkgRu-pxJZD3DUUUnrAklcehKwRiq71Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN6Sat-ChblRbP-AgjisLeIuxfR56--4EjE_3JlIY7I-4k7DYAyJoRjHVW9XZz-lNTo7CC5vWR9ZZ9PIR51r0XTzb-Zw3SsXK5ZpLr2kLtCWzPMFsj3cSsT3o_YTz-CIzeJ4Mh-Ziayw39JRpgZVX97HqF-NmIlYaHKqCiY5Cv_uA747SZchgpFVyfhvs9wyJeaijbT3bmy0dCS2bv-1RB7mKj2Q11lSk3sgNXs5s_xPjPmJNLibPfURXWQo3XcXIEEBxmxFQN9E-OP8jdMpr6sDd4yMcpfLvHfn6p3Z8d1jMTtoKdi-Rl8vbv16GN20R_N6wch-styLgMLipJ0zdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUOv2SjQixpo2T1eQ5hmlj0TRq3MNWsOj33havHcbGz4VGpVgJjOM3cd5_ogKpfV9odEYAy63RNhDG1cupoUoxfsvhNyqv2xBkonJxIsMd7CPncl2utcW8Luz8dhrfYh01il3He2-aeLGVOgl4tc7z6Je-BEEupPyOZ47xNAd9vBxmKMeZOcDaGJOC0SieyXhWBCHT9WvXNMyjZ1hWLuY9Iu8F0k6BBcTeqD4RrWcE-xfSHnEVH3VCjf2jHpzSwZ_0qC1tgZsDOt92-gj-ppQ8Q_DxrVUDSbV85Ap02Qnzob_F0JMKyJRi3hY-5BM7bQ4TyYAmY6o1mRoTrfyMkYow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNvyHDiKuilu73OKru52TWutht7sfWchqEtRgSJBOdZVhmN3j_v744RzGkpIXQCR_b2h-7LR2GfmsWXX4cgCHpxkYizzrcqSBW_q1DRdvx1XzxUBwS0q1FEGEJ2ySl_1eXp85oJxYUwd7Er5rTddZf7dJS2Yhm_lySfVunazqabsh5XcdnGHD7L9mezGIXuLY5KH7-CdKHN3-4T0seUweZrjevnYPy5nr6xE4w1hPtZcXHdypVQSymQ563WQP36PZdnA16j-hraV_7T2-qMKNG_p6ojTB4G8TJaGjc8HhAEIj9aLvXdNS1skgkNRBPjqtnVHNtUMf47FUvYekeuB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCx00BHzB05YQlEyAsUjGn20Mqz_R9Lb0Ph78WKjCXfxF4aB33wozcOAWH_fvNp6sSEJLypLZbtbuFjrZmI-V8t9ozwcZNHZ1P9HznpSWJwSZ8NgEoZjLm8-OLzwSDoUtHC6lS5my47zzq2okc1Ka8qAtb4u7QkXIlINcCJcqi1YrYDKzx9n769g6vpGSibLlxEtPGPtBMpOFR97cHYt859FVTdSd-ojduemdsvf57pBGXfqoOuA8vPs8A8Tq7Ba2op5w4ElHyrNpWcTyMIcTRPcQRtOMpycwYtzYzorFKoSp1JHPQVLDERuXa6UP-a4tvjdq6CXRC3YcCapFHa-Qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djX9bUaJaTbKS60BkQVIBz8krs8H29-fQ1K8yPNkXsAqPzxyx4ZLynRF77Znj3itKIhaOkRaZov4NV7Vad1ntyv9xX3mGyGv2z6-zBrfNX2d32SalFyxv-mmTuaDc669YIH86R91-GZsODCCQNsAhDnL56P7TTTyl1cuKNXPdHOCjHmzpAd02ar2rIZSDbBQFrcOKVxK1S9GPToGRBJqIQwohGo3V_1IJ4v9ePs6DJmHFPY-N9Q_NaY7cOKO__4oSNJe5fUvTFiXpUVjcb68B8RH_IELJMwsTqCRUqmlAaeu74P0yZwAzDCWWixJ6ZwrkW_6ZDIgOfF5ugNpyT7Ghg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2kOAjxWwIjdqkYuk70HrNKVLjLb6yzKLTcvbcPdh_5w8zbbeFC60kknhaSg5J9BnoPaAb85RsoQEd6UCb-G5G2K0rR0rP5hxR5hJnIuxv2ghHCooR8t8LrcNYmqyXizloZzrdDfhTn3AzoJbVrlLYcBX6yK2ABe-9-BLJ3LCNT2IDWxlLNAxcm5fpiCseqNRJ-HJlKtXT95fGYLq2KH7KVxUR8V4B8RxV_MTB9qNjQr5rPqG13KriSrdqE--DaK28r3JyxP7KN-bmMvcTvRC2Mxn2wnr2WoxcGLo-Rd4hKo2Skfr2kw_MONLJg2SSSr7P70VW4aR4EluwIpa5cb2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=fMHhDmFDfxiugnpq7ymCKSWeVWMg0AKGCGHvlDbJ__lnXg86NJyiHTQcaf7L2qJaN-raQgozTrfeYKnDa9kyTNK6w4wisN8N9gNyLF3R9xKa-TDvLjFB1lGeKeN1ckC9WBb1la9O47Tm2UKGtk02SMV29tY-cVNUIxzVhSwSIno3OgD7qE58Xgx55Vw4SKOtwNV3x8iABwE3b0RJgEngiYJqwQAvGYNPRh2Yt80FnfjQpc01vPX8zyQY2JutxxhgqhwZSihum0XeLTD5RMvMusin-EW1qNuMeJpfje4Od5pjYPZcVdvJAMPLN7cYUkUHXAPwqkgtqK8O3sT_461IXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=fMHhDmFDfxiugnpq7ymCKSWeVWMg0AKGCGHvlDbJ__lnXg86NJyiHTQcaf7L2qJaN-raQgozTrfeYKnDa9kyTNK6w4wisN8N9gNyLF3R9xKa-TDvLjFB1lGeKeN1ckC9WBb1la9O47Tm2UKGtk02SMV29tY-cVNUIxzVhSwSIno3OgD7qE58Xgx55Vw4SKOtwNV3x8iABwE3b0RJgEngiYJqwQAvGYNPRh2Yt80FnfjQpc01vPX8zyQY2JutxxhgqhwZSihum0XeLTD5RMvMusin-EW1qNuMeJpfje4Od5pjYPZcVdvJAMPLN7cYUkUHXAPwqkgtqK8O3sT_461IXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4-pDR3ntIAQYfFh64e64rOiBw_k2Rj3-2E5YJP8QptUQsyln-iMMcl7wOxccIQJ5oF-yspqtrD5imTPaftzEz1JmFkiBs4ecvauADojMyShJEmLDP8UsJNDWycy-ytbLCB5yblAIlamg1C_G8r_0IWB1sNwuoTbg6MdeqFYgkn2yoa2j6626SMZtS0d1oP-0hh69hqHSjLuA4b-llsiCyxfuv5Nw5qdt71OnropOWOom_B-WFUqwQ5mEJN8ObFEOmnOrISR2tTNzejVB69ut7P-4B6CFQ6_K-JbXwujdgxMmomkl9-sA2RYpmt3doD3_UTYol46dyU_AMRv4NUAWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBAkUFZqH-0ws0K9hAkEyMjfCwPhHxHYR5-lcuA2LLGlCoP87HOZi3CYisOh9-bLuqlz7FuMKpni2rQywSYdmPqQogz2FCi_XBBexW2Vsxdnw52bXT5u1mzxUmVMS2JA_d-MGkiYw38IDoQzKIh7jd4fbn-76IFjoprxpK5fYIfy6A35E7Htg5picgLrdU-WfYmZr6O8ybeWxhRWPj-J8UyMatCCDLur48dc87Owz8o81RbL4Pqys-FDkC3_kxKCw_4QSr77lMoA_B7bWMLt4uPJ7IbBeGfjOUgzjSjOBKKX2OWkCCIk1f86RUThYXCclSBylabB1-P3L8SKZgOuPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI8urLmnTBmbgqvbFWCJZ5_7u9pvm3k7hJXiESQdJyN64aQdJVkHD-U3GohsvZAwWsGY0f8u5-banvglH_DsMou14Ba1gC_HDh1LzztM1vEBSR2uHwUNVM99bFZrlyd3fUFsWf7oPBRJfbuTmmSPIv3m69-lkcsZp_r5EyRKfEifwHWnymFGNYe0FXO_RQbbGY_z2ELh-g1PQOi__qkqzyN2_v-6iXA3_7IVGtRZMwjP7iNksZyb7peNySlRQkjhPWbNRhAqR02lM6kKOmceMIWr0n_X5mGrt4HJhXTMqWnZQb1BXgKbBjI_gjUeQgwK3TPdZxsdbkh7_AkPxMYYTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obw_GgEGbdgxAG6Np9YIB6zddDKD6ihAw2p8ttnLnU1_WM3GyLZb16Lbm8Hqy4_hKLlYZvqb6i_OKKH4KufEF5Zxd58StogqZOXpI5UcbVCAAbHIMFYrjust__jByvgodZAgFG4l1ROb0L5p4-2MiNmZ05-ozOfT3sU8zX3HO3tNn7md-3SLcrrim8_6nOkV2TdGCda5ZKSil1t1-VdiG51SkOPghk8IZ3lWEZwTfdO7NZnBdZGCQkyZ-9ynIvgXa2oxq4IDmhuytPv9-QB7RP_jaZ0LaDx5Zd2Jd-TOWDTv0hHdc17b1m3QIoOJDwC5eU08EsR9vb-3ZetM-FDAvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibbO4GmiUI6qsoBlbL4e4pnCmJ62O2Kcd1wNTUo2X-rNWjBVtEoR2ulVMlCK7weNLqYOQVL2PncnJ5Tt8OSU6se6a1E2hyKGupbGwTXHyF2wf4HyrDAz3N_0ic4wpJiOY67-xzPN-_Q1r6TN9B-ksGowkwHjkMvJQaWgo015Bhxy8_yUp9B02kSH3pNyAT8mMJu4UwotlHQokA172jgyiOu1RTGBtRYexEFZLSJ3AHYdQCpp2zMhYLlR-Mns8lzwamsz-dGszttuyQbYFJ15j6V9IocKK11IpppRBpetipqkzf9V5lgULiBGmydE0e-0OaAVGTGGIq7Pm0VIH7mTeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAQGWCfTf_Dq26Dveu2fmkCuxaQQRYlkZxR6UlutXKE4e-cz6Tjc32d5tAAyNVoIpPucfwEmagXuvpbuJTAWV_d3VHtVfua0Ois7u1grTGeh9Va6yakpeHejUDAyqZb5Nn5z5dfAADuv7rkzZUpc4eEEDHxOkJC7lu-jcHmPzHBVgik2ERdj8GAk4JrTQSdiyNQRwA6D_YAvkBMSHtELz8IuwlOTeGTrH2hIqIyRuy1TqUQ5jZY-fG1xlso5z07PgDMIyJgXChAwgYj1vCohcK1HcdyS1ur-9Zfv7plRT3aH69XESv7xbGVSIfIgVuOshoS7ORbUwhy5ND3MGBKiZA.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHpdO7u9lzyXxrxaWTNb1Mg_SzYpYic9PPXeBgcvOg-jh_6bmh7mC6_E35K7A0yCgsNr8735drHHXrnVXJGSSjwIXnnKPFXndYIqlZQjfuiPWfwrcPCoFnqOKmzRoxBI0Eha-Xntmiz5GQxUMUfzBXUMywnRSeTaPyMmLNWqEHWe1AGMRVeeGEcS1P4YeAmmH5iu4RvV7JXsVhSHCexo9kaLyPx4pUicuxd9lGv0l-pRWCEeyWS-NX7FyBIR8gc0eGhiZLjslCsQfFpWm5vWicvksIsBh-sVDDS5jlSwbjDrjux2XDBx0u8WCWP1_gcqU3ZMF-iv7pNzdwfAecbnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh8hZZ3VLIqTBkYr0luPfsfbee93ljP7XYdmVcQmgTmuSGDrCTg8jBxEgoAN1qI6Pt7vcxW3tbz1ApSS_MY4LZaUIKA72AHYf0RKlx6RAAG3TmGYo_LsWe6d5L4m_irWM507uJy3KLAehgo5TLD5ONDdptwIaym_6OeiPvkgVenPyHL0pXBCk-zLqD863tuAttKkeW8JlkNY5Kd506tblys_ESdYVFpltoW4t5NwtlRdQ9BfEOTTbv4CFCho0atr-oegSMrpBKLbCb7X80mMJwUmVkqXfHRIHG1ZenidC4neYHBovKqcKVwncMi2Dixhn5hvUAV90iy2bV48kvwHaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
