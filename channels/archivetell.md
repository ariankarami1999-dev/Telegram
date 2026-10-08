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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShR5cy8_V2ugrIeU0mnbbyrZtS4lEsn3Xp_pikgjFG6lTr2w5bawaj0vgBVKwIOvd2beF5-mQgBm0pQSf31QZ1I1qIhn_35MJjc0pLn418ABjwR6_jHniVboDdEvaGL2KzThKHPNb1lyyuIoKg4xk1DTBxULs1wp5csrPzNJMS2llpwDDecHHZQY0g2QahDMCPq8YSY7MYeLa6IMZnwpXCvX4KfhXiQTpLW4ZdIhSAOBdCkSNIIZScnemR7iNjQHyF0M2DYgbqJnB9_dU2Ht2dgIGLgvQLoh-NU1zB1JboLNqxHGY9o_nTVSW86GDNJIQAwW8hxFAsN7JjAD2Y-Lgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 174 · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 696 · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8040">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سلام به همه عزیزان
❤️
ما یک پروژه بزرگی رو داریم آماده میکنیم اگر از عزیزان کسی تمایل داره برای تست پروژه لطفا به
@Bachedev
پیام بده
🤝</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/8040" target="_blank">📅 14:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLyrP23vih0QnII-Ofbppwbn0asmTg8hM8ppMhiDFK1MTrzIwpf5sP4gtI3eiBduHvvmCgc1mmq3GQDekYIZR4jwU-dfj_7LHhGyyfT0FUq2lTzGrpyLztehlIf-6ai0nYJitPa2mIw0NdzVFzuUn0SBNiWrMV0akm0nkLHVZoWYmDoOuiBIP0F09J-HV-8Hon-kS6AQojWdv9p_U5hgwzXHR5Hww5SCqrWavhiyEJL3WsO3_3XV-xLTgrAbp3v7WlQtSs3IQ3NBkyW9wzvt6h9nZrPjjvw1qMe7BMv33sDSYVMolwArkvCBMkCVJhY-pL7SkjhA6zXDSTsY2W0g6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gadaYP8Hurszz03zCUtMG2tW7iPZamEIa2bu-0gnM3eTgytzpEub5P8L9lPuEjPC2uV2zXhMUr8v9AQYTPFgtixGWT9cYfduBbQYSOEFZszWD03n2I7nqd9M0-q1d82GrroOR9QLLci1SaNWF4rsdt3o6yIFSyzm7HPjQ-VaBIpb13kfUVpyE4xLky74ykdtRkpCTKW9T8n9F5IC2pcffH01D4RsXpoA6HB1I1Gyl7WOAUpIdc2S5zQ3ad2VtuQN6rhWE4Cczs5sT_8eMnn0lfLPhH_mdYzG0z4GvawtzzCbUWxoxziCpe8wFuwGSDKowMr7IQv-km4eg7sqxGhghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=JbfmiHMsl2sy4tFOYEsvDEtYXTnXb0xP3melCwP64Q-FZssofd3ABJFGfxK0qDaJNh8Beugw12EBLoeh1BsZ83d7OcB4qiLHNBtR1Q5_oot4ZvAI_lJzmKOwHOpK6-vb3ynD2bxOCfTV48Vz8lGYTqIsLuYRS7mzM0iNkHru8hKaK3Pg5yFdx8UQiDbEl1SqMeRtcj1Y-8333Zbr7u1yJIn1hzbhGLvxMvz8AFvWKKSBfoTytg_gzFEjlsJf15lT0yhWdbf9D2v--79O5oGZflkgNZqASuLfmakVKek6c2Z_6BEyNeBJNvVZV7yBHqlOHgrkWpKyl8NJWhmD2FCO1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=JbfmiHMsl2sy4tFOYEsvDEtYXTnXb0xP3melCwP64Q-FZssofd3ABJFGfxK0qDaJNh8Beugw12EBLoeh1BsZ83d7OcB4qiLHNBtR1Q5_oot4ZvAI_lJzmKOwHOpK6-vb3ynD2bxOCfTV48Vz8lGYTqIsLuYRS7mzM0iNkHru8hKaK3Pg5yFdx8UQiDbEl1SqMeRtcj1Y-8333Zbr7u1yJIn1hzbhGLvxMvz8AFvWKKSBfoTytg_gzFEjlsJf15lT0yhWdbf9D2v--79O5oGZflkgNZqASuLfmakVKek6c2Z_6BEyNeBJNvVZV7yBHqlOHgrkWpKyl8NJWhmD2FCO1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyM0GbwGGb9bgGX3X8N7zGo-JXmnOsWm_wGd0VxNXEIzyQTwTPQ6IJKD0yuvJsfp3AEsVMeiyIbr2XSeFQhXtRQknjHkJif_ttEuvvn--KPPAevq1J6TV2R4ZMxHAsErZoNgZfIMfeIn3AnmrvSO_QtiEQI0uMLSdIVN2De1eqGKwWauWhsGw_1_3__myKWs_YgOGaI07pDReqGo6kx_dB-MEibVXVesaxPQ9Q73igo2uweVEwXfcKqkYUvZNfKO9W5vP9gZSX0ReCpuZpohfXolAzXGM_kLE-FlAsc9Upk0vBn_XxM9IIjkpPHsjv5W2TxMjiBOSFNfnnsWPmHLyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=eA1mhuIab3vdBitxC_2b8ynnPWQIKcNMEfGTcFdNZn9pjJPp26zCuDJPSx04wOCyFE1OftBYxuYm7rzEvpej1RymUNHrsZ67DLZr-k9Mz1kMJ2l7iJLl-fa9zVob3X5ytVmNP-i09BJ_AtTyN3YmtOlvG11f_OMfvFgRnPi5Yw-MSO8uEbzEe_L74Nkiuaccufs0TX7V4v9Is4nBcMUtP9sz6iHMWGotdHJB7Y61sur_Aki4-G8GljVCxEBUhnhuD0G8Mf4H6XO4QEsiXvEa54MHVd-p2wxwEL_UztkicBFgLUwSmyYK-OBmmMV7ILRq5fe8UwEXuslMqToiKlk8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=eA1mhuIab3vdBitxC_2b8ynnPWQIKcNMEfGTcFdNZn9pjJPp26zCuDJPSx04wOCyFE1OftBYxuYm7rzEvpej1RymUNHrsZ67DLZr-k9Mz1kMJ2l7iJLl-fa9zVob3X5ytVmNP-i09BJ_AtTyN3YmtOlvG11f_OMfvFgRnPi5Yw-MSO8uEbzEe_L74Nkiuaccufs0TX7V4v9Is4nBcMUtP9sz6iHMWGotdHJB7Y61sur_Aki4-G8GljVCxEBUhnhuD0G8Mf4H6XO4QEsiXvEa54MHVd-p2wxwEL_UztkicBFgLUwSmyYK-OBmmMV7ILRq5fe8UwEXuslMqToiKlk8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpO-eAzWOPmYgZNcmd7C9ve50t9qN_VbYuGuCC3h3L9ujBmxx4cMkVkpgYmpAEPtQsdZrqYtvUdsmyWTFp1RIfkpsFzM3J2nSS0TwEiWEGYqB2pO7sPYMzbnVW_7Ts1aGFvDIbaKHN1IK7P88iLwbHL5k3ppXLvTSPrctIT8uh1epAw3XAaLzZ4M8ZV54FYWmaBEXVGogbtUW0zLQa--ZdFxIL3UltYUINGurr_F_PpX_Vna3tMycF_RwCdQghsk19h7LbKt1fKPvsHV5In145wNQ8q9Wcr66AophdCyjWToPxAQ_qekMmHUmWzqzgmnLM-wa5ElVxS77KJAMn7kdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICSpDevtAO9AEE22KN7Ry4r4Zs6YcSTyKpNGLyWomqF2LyEcFryFNMcV9oyhFg4Kw4FJLU6uEiAj6EpduL5odOD0WSf7TljJ0SE_MRqEjJzinYu9cxXP_MZtSKy-num0wNXgqq5vt2Is2EULzMPGqsW5o2JZRMMvQE94nhV0LFl6P3dmAm6gyTheV5jwFRtUsxEBt88qfodc1YevHxOOCmqarcso8y75wW3RjcnJdhM5utXc3WW86c_H12YyUMvuH0Lrwson41xZvjOwqNx7znG3WsMq2Q52j7ksfsvCQ6GnKrrvx00xutSFK2VPkn69_iPGwkIBT12p6cHICokSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFWIDiRjW07pJLZQZhb5IVL2cBTnp-0Gngm8L5dAWNOUzVjzTl1aafjIhgrL0eolmdB6yY3sVS_dcjMWeeIYXxjvXIwWZqroVlnQlSFHcdNzrbFUf2Um09_2T2K240WFMBxQQ7fniGdHwdmylo-xAoa46PtUwYCiiuoBlmKy8CGAaBvkAjx9WIr6YSHuKMOBb1SQ7JBZwBf-0F0Na75XERPnvV0DxG4nwv_XZhaVT0uY6JnsQ-FwM848tlTi3izNIsZhn-uCId-L2MvDZZbLbsTpYB8-M4E9wd_sBSd6873cUlZLc5KjkVD0lHZkp_SHqmZUYGmmiPo7LTqsRRKbHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8jhwSRZBPh1AuaHUQEobzQXQhMQu-cO-JY8g16GLLDsFb4TJN7QEkZcMzxRhXuAfenp6gprwdkXVycIngMmnCySvB9cfz6ahA_-sN6dNTrFZZMHn4JESQIRK7XqWn50pEO4vr2H0gks7GoWzThts5bnyscYopPO3BQ1lPOx4EDznY_8ds2z2iHpH3Ae4lzuV1407HeJ5k7u-C-Mzr9VFUCsM3w6P26p8J41SBb2tBzPCh1ZVSDliiRg76z6bTFKwVQjGOwA_U7TfcuzdcDMSj0q5n0HpavIPBdj6COArAb9f45PS-ATl5qdTGH5Lxx2jV4B_Z27TGyFYLBogErXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Unb7S8D0fRhdWB8Eg1zJG9BZaNW95kpmglQY-0-QUPriYSUq-9P_i64TMp32Fr56IqiJSTGFmDQzJnnXdtzVM2XZ35YRwRxNJ90lmhVs5i4MoIhnqHzvukLpPcxCTD8vTOJ0ib_F7kG65grJl36iRuLMiTZCh9id-ztKLewtHnkDbuasAotTYl8MrBMO76918y11KnemvofFmPJooRXHZtElI6MMvV0ErxKLJCId2pUbFFzSwdH0m36sDENTw03JVBm5STUYAbukigiohd6kBs5eXl8NCMeY04ZubOihyHWyPqjl4hpEKLsOF75UQMJ6I6IJJWXGMXLa53Mmwu-0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eh-2kWdTphvTplwb3fAH5nsOdNwU3FyjIySvMKW1ndqFVquh3JmSk7X8SXrjos9hbA7Y9iFhbWQi4WwZIavwKAtOhye-IwbqQ0D3csAE_higjDg1mDeDt9dElY-hOML1K6L_EToSc47wZ2bjYrQyZUI_9QkR97IXnFZkFeqaV3fqB-DSUy6K4WEl5GIbhI78eEQ6YWqHUXGtfgMzv-i2IrA3E08mgGGnf6PIx57iflJls8vOLgl5vKfBVfwd5_7sk2eqMYCsLGUSpLUtkL385q6WtzOKahTKY1YKaZ0lbBpv6wGjdh9GudZSWhcQ1qd2wloezfOATgAXLERAaoFSdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq-37R8SuGMbYoDx_zqkUKL-BZ6HQSl-7l9ZY2Ep5Wc4oAoWXARM7FOIr-V-i8xhpzKr4xBNkXi6I4vYZ2Wh1nH1ozp_tx5bvScUhdKNjgHlfQD1lCjTepHUXM4CNQD2falPF9KgPB_hWn8rRkcJ-tSTmAyxxeobnA3CAa4DF6t2aGXcYICB1xCXV0kgVnaRlu5xx8GUJiCa3dtXnwHeiJS99Tlc6XUM1aYwdP-OQqPph9eqiZrsqtKsaG_NfO7YSydMfUbnU-YeOLHb-7-30DDw0qMsvS2iPO406HwaDlfbOtSF6SeDbsM-a-e3jXREGK1NbqQrPcHIysaon_yAIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pj5kkNpbqw6wPD51cYuXnZ1BCHGvFUHChRepEVt5VDbkMQlWgtpEreZDz4B7DGmdRMVRPUy2K2fvsRVHcOxkOQNXNyxdd-L7GTVUU963H8SvB6zk3aUjjklpFQTmQD3grmynx7HR8Tpo6RscB4oMmYGp3w-um1S48a90URzROy1IUz8OrsWPDX_t8_YmSuqP0ACD7BPvvKAuENzsuFoZg4qZ6XZrc0hc7Xws1tBQ9IBRA_DtT4kLbLtAoJsWEaa-1aOEIUT_paXVPI5mkHPgBqtKGmGgmAmNLDHDNq7hSCiV2vKK3ZDGEg85hyZ7J1w6mqUnxdDXu6_XPW5F7PqY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6j9UAB8crYfij9WdX-EQWkBGtxhJmWUFNA9xFWSt-Y_cncTyzMa4GNfEQd_X74y5quf7435j_uMHAuM9pr6mbxQAaVaXD-AdSW4Z1Z8dp8a_HT80IqfzmymBPIVD9eQXkOfR3tUrUHap0gk3Y9X-TIaba_aEk8rsm7CY42GoJNAUiIlgfgqON_6hPXmAECjZ_Jmyy2HjaZ9m7CVeByPYcVgzY5lMvduNWEcpRWw06mDmL48S_tl-MfoYNDDbmZEIwAoa4BPDq8cEDspvMCPXGC1y1WLazMSBvaItHV1p95aTOUM0ScqQ65XyesvxBGzS0Z7BcP-k2NlFI2vieF3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJsThXrp4qa6j9XC8CBs1j35SuTCH7gdM7bBH-FvOqniwiyj1ka2yPpA7aCVERbD1LsgCkVyfFCpUyG-5ugepFgTIDzGxj2D_4a-iG5REDEKhd3PVuZzJeGUeBvjgzFpHp9tEAmTKgBpiPGNo99E6jhxfJ7vxspKpo9d1w8oo89LqJiPV1elBlgSb8XrNpzsBa0C-Lu4jlv0YihpAcRkJ0WVbxw1W6XFu0bE7Zx_UcykDm4Va5LW1oe_YVElrAiVOk3brwglEKkcHsDKT4foc-ztpxZNN4cc_8t7M4kID4MvmRAU5gUXoObLklNvY98j5kIvannjB2fYOrsspA3zyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohobZ7iSJnaM4jQbdJstaQhlCdlOjH94E99aJ_XN2u_NXRBE5hWJgC6HBfRHhZQCV5lG-7xTsXe7F9N7jBOY63BDbmVil0OEDZpwO6Gq2FmNyCjJfDBM0jt_cPlK0Nb76ii7CTq9MIQAa6G6iYSQWfWdkgQ__wCPUS5VMPq2OOzknb6BCo3mc-oiqfMKhewn1M6Lf2N_jrPUoEvtV9-W6Da4sjN3OnwonksMq3XSkBrOALhmt89M4qBs9pycr7jSNaxQTAMDgts_F9AS8NAQnUgx0tVg5mTlwN-9C4kt1j96t_GI9lOCtcxjacH4LNvpiOorsP0bPzCQBbHinf56RA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCObs3CO1T9HzUREYrZ5ObCaIoKMv12Vm1iQSMUmGCkFPeCZSE3jmohfivxeFU9TS6gppzA0dJBFQjkTdukwKxFQJ2FTX_DzRf93AB9-4MLxUny9jQbbuvPERs4KuFRYpjR5RUCdOVpCZ5dxV5qqvMJwpwSXbfat_qie9VRee38bTdts2hgZX0fORUQm7_h9vk5HVSwYb45L8OR7Zdq-pWGVvdanyqFQfdx0njn4NF9AdaN2DvyRpexgYIHfOc26fejI6KSkqYAiAZKf8fnrt8rWYjlTT6uCsBbLV_hGB-pvIzOp__3ggJuN8XOoP1KPQg2M0FBJYc6cibiLqYVWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IoIHOI2h2J4c8K-yvRHo5bY79Ox-f328qHGFlYWtimRXb0SuN5t1wy2FCVjeWpyedekA-G7YtrBQhaFgH3PwYfo9sm3ui1lkIB5fT-g4WEKzqjDoWcy6NbORsJertmS7Xkc0fm2yFKq_sU2qtylZABzbsemlGy8mBEm5nj_eZyRYmh4VIQ5aAAhqlBny40v-80EOrzJG-LKbhb0iSg6cB9OXatIp4HMm8BOgujsYloQEriRO-MQBQpkFHYseYENLUvKKOky3fiNn6NjMe26hCPHnV3E1L-7EpnWkQvuiSkEiPw4uVJpr1t43qTbk2yBN0y50JCld9YHCeL4jozEsFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TknkKVyt1x1-5DLcT4M03lqcbj5CppyFOzg1N-Lv8uB4IDHIK7tKzxtct07PiWN5MnvM2kWb9GMeZp1WMopu6mdyxBz5nZYIhB3HIBukkBXtDWFZ1jvEQ5WiP3d0IdsIGEUCV8vG9-95XsG1LNxmIPB5sP-XXzHTiBJXURuvntoXmBoN-9-9y4XFmQzXLuwbDZ4uD4AqKXE2ITe3023B9zAIIMgit6dJ0bMHGl5Mo-hBHvoGACMzRQ_21_FqNH0eiHzYc2CdPlbztFdueRG2TE-ptFJ9y_QZ0LUXennDrcLvtg2hDTRjlbrofVtIMRiQb34cffsJI9LbiwwBKMRTog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=UR1Cw8zhru_P-wsf1ee5Ge5gFbCryobSKTAJhEj733wPK2hvYvUNsrARYXPIzSAY8t6SWwSe39fj_KnBkBgG0mXU-oTRbuqx5eN6AsAuHQRNUW8IvWiob7QoeKHifiZjK4H09YPGzH8mDRcdLIT5W7GEMmakCtkO6EVNxFs1HL2JagfZQe1qlvjgEjifOxRCm8XoI10BoR7C8x91I6K28Fdi6MfD_Y6j45cUS0rSMUnJzqfuQwtVPmYFG3dH0OMa4fV_ieNKDoON53xizAInO20VEaL0PmLquV85D3CJEgYFlbBuNBPf4uoq6PaJvEBps2JBndq3DfCCXgZ4_7y0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=UR1Cw8zhru_P-wsf1ee5Ge5gFbCryobSKTAJhEj733wPK2hvYvUNsrARYXPIzSAY8t6SWwSe39fj_KnBkBgG0mXU-oTRbuqx5eN6AsAuHQRNUW8IvWiob7QoeKHifiZjK4H09YPGzH8mDRcdLIT5W7GEMmakCtkO6EVNxFs1HL2JagfZQe1qlvjgEjifOxRCm8XoI10BoR7C8x91I6K28Fdi6MfD_Y6j45cUS0rSMUnJzqfuQwtVPmYFG3dH0OMa4fV_ieNKDoON53xizAInO20VEaL0PmLquV85D3CJEgYFlbBuNBPf4uoq6PaJvEBps2JBndq3DfCCXgZ4_7y0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWeMs1ZViJcItuJD1Db7zypNRvvA1zUo-3qgMiPVBndPe1BIE5saQ2zZAz7PiAiyoxjmLyi2aLBkdDWbS26oHU0_AoUERXrNtjki7OTZROubFFS2Fde7g184rTVmFdydq4c7EaMUJJxird5q7H9L7Pf0JTVnuzVSNQTYWjkeSafBdE-INtkQpfLWxYLKCfR662y0lIYRYU6xKZ-2UgFLqGuPsjsh_ZhsxUUkgGVLoFanmhRT76AtzReWihHZEAJ_iNOVan5l2Bw-YjaRCjE2X6vZGILPiBdVS4eCUa3OG5irkN_ELwQMD4TKcn0cEwoG5QzK1W6MZVFW6tHDB3T9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oon1nikpOonM2Snv5rWgluPJq0fZv576g227uWOiDozDYccoQm-k9OZ99EswB7yhWbSqggNLsfmdUoKTXIdYYppsCGaH9G7YxZXcFZJ6WMns0hY2dmWkRHAZ_Vj2SgsJFcwdVcoZFoPVNF94fxI1xJWCIIXFc7iZZrJj5rR-QcqqXlLBvMJQ41qa45iNTDik4L288W2g-sOs8B9zTTLJr0RvSGHzyZ2akoTGIyAwLmfmnYh4ozTd7WyMuzhof0RnAP7OazE75YZ--bko9DID1VNNP7i-wB5-sruy8qy8zRGIhn0s7v-CfNgRpmCu-hjSroOOPljncVxm8C5U2lUouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pj7Vb_825S055VPEZLGmgiwaOkxU9kT8Aa_hb44o9feWXulijgjZOE0dBPBEkOa3cNsaLCO0lYIKlYCLjYjNH9c2rwhBI2_T1VAl6zNKfn_soj7UpJdahxf60719fRC_m0qkD6_Gk12SNwMeBxPBld_EsTQzvpn2r-T1MIoVfr1BXEtCp7UN6OLLWsCRoRQWW_vLO8GsK37KBSAKJj0F3T2jpo9AQ8d2uVfPqKkIJkJ-__CRdTEmnlGGM2KfUcGojGBRiKEuQ77krt8nLIThFx9KznjkPXKAI1ueQMd64Le47tA-EM3myOF6zQ0rqW5v88eGePMOHzOg1dnDQP6rSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyCZqfq6_nmoW9EGZPV52SU_Wq6K8UzGUGeeA-aPePQFs6WIzHX3ngiIPpE-xmhpsW8sM_1SwOj-h8TFFd0SCLD46hRnepFJlJqtEURrcpXa_TBEG3CK_vN6kN-l2nWteL9goYSXWYZYY8O3HQQNRidPVD_EW9c8pENxH7QsVYlFfT5ZIPKgevpUu5WkILOaD_o8PgERqE-gPyD9y-fmS6CNRmwfbwU98kzIRUo_GiWupx_R2h1hg4O72l6pyjzJ76CF9qE64pcJ5gcSJSTWU3rRyYGScqHNeBrLmRn3dLP1rPIk9UeVcSRy-SgEAa29o1isWRqCk78UEOa8hthPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWFRokSPYrDR-mnpdlK30iQIRkwrbI3n2VOemjh0otBqfMjX4LklcGL7Owa0MlToERxpf3FqeQz7pDzF14Q23BSNUoOwUSi_Feo8ErHRrpQvop1SNKnse7QFlPT4YH2O_m5hBozfg6mfSJ-C2eJgnut2YcQHBkDZ738OZhN24JPTM4sD6dkg9WlOLQYnydtbBCWPPtwB4LnoUGCjD73u7uiIhFWMzj4stWTiOJWdnle3sgLQfkNJeqt0p8sn_zF2RAKjDkNYEyo7eCrQoi222Nz7RSzO1DuIsSgUhR5zbL6PLBQlqwxg0nRXUbQTAxWXbviXIhpzKDvKZgQdyhpTIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs1ThGSp_Mux2_eWNhjAki6xDnin3SbC6-DlMlOK4DPR_-RvKk8ffED_8l7Hs5-I-oARoXOuJYy8IKoL3EcATuYxjHgm89Pm64p_WHZLg8gvmNNB4HeArXO_dAQW1eDIqxCedJ0KSX7G29Cm0k2yAp9U4CQATfvGv6GZ6fZxw-DCwZEcbvkpxsBsEQ8RBpINb5vHwc6vAm8YsvAOziHJuQEzqkNZZmwU6xexJfEUlKP_JJy1fuHVb-cceMUrzfTF_V0dJh7K_h0TbodGnJ-g9bVUIlNoJ4n_wUzcfXrtdkk7Pk10hVuvHHFWgO-Am5CATv7Dd1K8EWkqoCBLWXDtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eSbQt65c4kvPWhJJmNG15pGB1-QTyuHZzw2POnPvPjryOvM5bR4pRoUIXC8D8ooIM0rkHbLWQhTHWPTTtkRmG7tgk7tOWsA7qFzGy6EWeGRBG6Xg92u-urwpKorGf-QGgSzDeNfucHxnQxIQ4kYAxZDVkl8cEgdgfNB0Tz-ppEUTXlMQUClqdmHFTlSF4u8kxRS_Mj8ofg7Y19pDLMMPie2MzvXL1Hl_fTD2hM4eWM4EoVi4dwy0_8kXvpyZPGtOYEDMe7OzickvaCbWzNeN0dPzF8QXlPm_o4ueAUg3hU8iJEfVDqw6P-uaHJanMb4XMJ74Tsz262wj7kQKfcmTew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MQHwJZdyBndWuqbeE-qyJIG1C3Hqi5l_n5c-i81OY1cP9clCtrgbjFN3lnWeROh97bzbH2mACBpmuAD2mnI1BLo0P_dje0uLlJTpPZlS_RUR89yWO6k_OAc5GC1FBz9k2_gJgWt2MOg_3Zv_mgb-ks6oD4Q-nxihi6agowHazkNET1Z9Xd_yAIAATmIO3n-YoPaC1nTydP4Nd-oPHvtFPaAe7Qpuq5dww4Hr8-TOfWFbiP4jTA3v39nhi9mO1ZLK1hln-odD1ovCqitd72PD7RGVPbDBM0P5qtDxjq7TNyIlAkk1RiVLs-Goh5Pq0mZpBmy2NqofF7_P646D-Zp8kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7ys5f25qyjPxO-p07p6OVyIjhR-oU00Mv4gLTsKbzQbKML_Q5Z1VQel58dqlQ2r9GJw8bo_5GNACPB6Ny7Lvo55M3zqP5_kCxowJfU4gmuBzV19CmNENQVOeHXS-jiVr2bzzM7Qg2izvadWTR7J-dNFx4yV3iuAbt-IyOiYm5nvPuQsuHwPEn3HzvyLIT3uPKd3nSN3OwW-MlgGOChPLVBbud8AaDZ039gaeoDhTLy1jGBKB8lZitgFeYik24X20I0VrZjI_KFuPDT694tpc-QdkvshdgDURWAb2lSTMOyVN7p5aTTdPjCwVeJ9HIOYomyCWdkIQ00yU0XMBhqVbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amLJf5DtKvzhFVZfMt45XX4MJnCWNU7ISaTGb4aC7FQc--wN_dVhiXGq2GspdcWk4FJSZGTbBHBJ0RWZ73NYS8JfhmCaB8rL3NikYw45bGwZtGg3Z8stl1P8w55LdzpHuuYViwJgaqgac6lksw5FUg3zNQ5p1SpTjesFxeNcXYjXTjfUuR6reBew7s9nG2zNyinJbnKgs6joiuAiElXp-318iT0VudBE3kYKGCgInM4tpla671E4Ugi4EmWdvev8l652ANQfZbOWBoZyYRszCQrkW6-bUYAQLfdxGIGITUJ-qWe7dAAwdmctJvk2KF257WQHtSkH3GoX0BDk_ocFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmAoiEeWj7up6ZAcen3OMX89csFHhFwEsMUMkPULsnA3lECVMh7jj8YAPqhxL9C3SukO0newCBweRZeIdQCKXQvNAn0geypG3B-KGoavfBwoDQjuAmbHBUTwOoUcgyeDdQ1uarnzvVy759saB-f-p8Xzhj0J9I1gh1fJBpKCSwKLvQz_SwxZrkGGtverIz0FYMytICVGVeXvfavWD_mjIwqX2q2ysX2Dk4ql_h_HKApkEKnzBR6ivmGQg75_x56vZhZygKaCqDFkZxYIjaZal8gnrqJqtDkReAc0ytKWGJJAG7Fn3BM5I8OYIMsxAHIOZeUeux2Bcylgcd_eHnrrQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC5cyAjj-i5x752tvfq2mixpDoaSlNdThrb4rMD0HOPOzuXx6s9l8Tx2Xz3XLJerv2TUKWjsgCWFv3qijQDUEOFDFcUCuxvV5omU2u9hlzCmH0iUZJxECLyOFeVocRYoKwnG5dQ_caitmc4rbiJwbJsnUcKR_It2Nz_M5EpFI9UJs-Ji4uwJblr3k-h8EhgLHfM1PcYVlkWhcqqe_T6WQgMsJDA7SkNZK-3TntgnhqoQ9EsPb4wRbrIQpiFCU0llma1gg92wgU-K39CZWNkpzEBTDiF5wS2BlOIf-skFhrhjh1PhYcCfiHh9XZSHc-23lZnG7Fi_8qw2HljPmUmhmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6pro6DsVjBrDkfvQ71sfzTY_KNzUC1e-yq91tCjFIAqTQAOEPVPd_e0L4ZlPJA2NfpkMzjLdkS_1GVkb6B8TBjQnv0wpfh8_fK-giLSsihhrlPX5B55opQSRhF5hhKvlfEPO3KvB6FfGZIQ-OObLQnLCjo696A5E0eJCupsQPgG9-HYIYKQJpl1ePAzsLZd1dMYGI8iAi_b4AOTlyy-_A4fgQs4gI3oYQ02ZrbO8Z0pq8NEBVD8x4Bbhbu7Dch4JXStvw9FYLinZcIoN0uMkg8AC8b2lWat7ykgVmhEAGrESkCyFEI2ySXfO5-OYHe8gd_5PFE-tnH-LfyG-Z7rFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MV4zUnBoH-JrVMwlALN7hnk5zyOj55Gz3PS8hfiHaw5flK1pkyorImoMrArCCZSi_2w4oEnJMos0Vaoze9DievK2C_eBFQXpZbQEdVsdEMX2rNqrw4twZmQ1OKdNWpIBDfsuCTDDoXV_HbQlUZqrHniyZ0ruW7aVkFQcCLC4IC59CMFZz-U6U53fIO02CIviPYJHt2CGqKFjhlI66TMvRB3AlJdEox7LtYyeaKGUfGI-9egPa_2s6xA_NgMjuVcdb_UU951rnUekF5cOrkvl58tum0Ir6ucfbg_7EQ7GJlNARZzpXc0ShvHew600VXeHq8h74TNmZ03oQ3jklom3yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vcp-t7EWLlRdOFXaUVmxQCjN5UFf5FAB_0uW5xzIIzMNA_15vtlS99oOyMKFewBmRdt0Oo6GWskT3SY-Q7_yn5gdeeYpzcgdacPcN8yitLw0vrqpdBjWLHgF_PrZLa99LpZErcs6nEkuR4IVmb44OsDdoYrZDxDHCGUfcXxcsJSy5_vwtiJ3IjDTu6_Gh4I1b-Ugoy-XVEumJWD9FXIkoQWtNY-AGG7OCssQiHa9a8OnaRefr8_UsvJGFCCY6Vmc68azqoyiLEJv1cDQw05r6AfDdaL6zh0PzzGQbtdnqf9HAjq4qijKWo2GhJ9u6dbvfrbItnfR2Wg_MWSVEakGfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj2L_Ydo-_OdsKxzO1JKplnXM13UOj8ynRgSbTlCmSJucgnNBSOggT6F8tarw6MiMkh_KMI9v3R2OvQAN0dO573TtbJ0AEcNDYSZMeKSj6kLgc6cKf8nnhXZIMG-jTc3XHqEeI8iiSoLTm7oI0Kfr8PC_SSOU2Lq-BrJB7AkNGwjUOJ5u5rX2avxV4icnzf3yN298A_ezBUSZWNIEaJqqIKptD83M4SP68GeldCIfsg2KO5nK6TMtiD-wBp-2KsS04pCfWPoa9kjvkwyMJvjqxnkAB8SLqUzS84UWjaL5T9_f_qczDVGjBHVMFViqr58IzvTdZv9uD0-4Hv6T88trw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2tnARQj8sFdt7iAMunbdbG9wvHfiefEkvmQ9XaJIJavzbzZyiSopIsAkyW1L9Ylnbc09uNkm4wa7Z02eWL6J5cvps2Fa7XyQGjq-toIzQP9i5hNil-9iGWm6Qcfk-2N3DWvODBL9EVWYbYLCxyxolAQhAvFQ2GAKzR2bw5p8OLwXLHRYRFca69tORzj2f3RPRofip7JUAaXgmwfj_9X-vFSEYT1ogAB7AmTjavu_hr10B0fZditALH9swSDO2YkhuojdGXLeJjipOGDS2h7wbD5IjvqPN1n1opLfbGHf2M6Vbh6wcpjZ5dyZ28R66LI1q-MGcoqTyIKEtWd8M1p4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsOcudg6fi813oCouqwGezDX442XOmiy0xWe2anA-u2pVMtTWnrmMLyVt7FkXjbliT6uaOC5FHDJgtUHy53YqPhh4qq3s53fKnidnPkhv0DPnL5tN8u5FW6BXL_63RZ_yeISqYcoVABa0cy81gjzjR3P-8RpHxWvZafy5I08uyFh0cC2mpbMtMxTU2F1KyJRWUUoF2Q1aY2f2JJ6ypy2kUbbHx6nHTulsUw42JUP2YkkKmQBb6sQNFnjXsF86e5zR8X6fCSH3LMYuuROLmJhnZXilTh1eH677_d7aB5Ix26KlwUqVe4w4JOYy92TkPTA4Xr10ITwGLJM7Cii6a5bRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1CN1YtQN0eG9AmEFRddmo-f5XTbz4A0byfmr1WU4U70Wy3MST6QS79COnkC3ZT1HDfVWiAK445O3f9EZazd3gt9nPC83aL8HgIM2lJNYwFYncK5b7XF-lrS1u1LapCV2pLg2OwO5m6GUBTopa16rvd8a7gEsbQQAL2636woi-ea5FjKanSbJcrTXNM54j39uj4deRJBmOkTu2d_XmbMBpehYxr1sG5ODRGvxhnu4_seAxp6pbzj4J552ktZqKIv782uMhWo8Zl2Z42ReaKldDeXZJ1CEXardp-9PIhLPUr_NscjiRtrHrqJZPv7pCj1ZLrUpnn1RGhlnnxoMdMe2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MpWZT65w9ZTbDmVJGT78BgHG_JCZibVvHkWcXllx_rBfDhozgnRvgZsSvctAxdzLKhUEyaTy-d9go3DZCk9jjY7aqdRX9252HL-lG3mHdlWBSQzrvLrz1wF2OcQpWebhPLXTS_djhyDQLYHmHnNcTkCNzF4zvRDZtiPa5TETQFvhDnBfAkFsSS2is1BGtuUXB598yNaMXkbxm_paRHxksddl7YKB7GRgZgpYsvGtc97UkVEVq2e9d4Q70Rhaxdn40hh3V0cRHSdttg2hRRVMczRkev6foGwz-SxdxhlBBb-JFVfigHWspIl-JK6Sp1azoSwiOWEHmT3XL787l_WuVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K-26NO1ukN02yLnYV9Qn7fG6cPE4uHjePsSU1WdVqu-FjWD1TYYTYDrS2RAE3nDmVfDug4cNH-c5N9mGYh4ydTZEPKR2xhGWUxjO1Ur0FdNZWmIs5ztglSwetFOxw6tp16tPtRjm1lb8rHTW-Plzo5eOKiU7QrKkTJbA-GSS3eY2XNALd2OKHRrrAWeeOjCCSxKUutRsE-StUXpucd1oOggPYapNC7Mc_BnGyqZjEhdNAlTOjYsoU22pqzlJzKUT2jUiHfyao6Joh3sCb4ItdTYeeg6vvmZMIFMhWURb581xEqVjZNQwtRbERfiG5a_eC7_5ireuuRL3GcQLL6RSjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMMbXQRH23ZB06fBb_T5nJhshXLzndjbQ1l7ByEjtOmrTtxL6uJO7LHH2SPHnlPo8DujnzIL0yY6-JD6W1QpAR727Z1ZUxqnbIASrBe5cBgisv8e7Yn6FvEkJJ2MQdniYK2epUGNGxrvXYmRgcfVqTBnBxVYl7We-YBvw7fWHKk5IhHgrOYWXeGNqKVmI9JM9qblLQBN32YPNcfqgz_iNzIPBOjokyoIqJty57uvjTYtqEliSwV3_5jcpdSDXmyc3d8m-asm4wx4N9n0ZKIQXPpDHKJ0ESUgIxD3jTm0GR_NaV_HArG8RRCupaoxiOacFPZOotvk_Gnk5lsBeDMpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUaMOXnZ7hkjjX_Ebp0MG17qXzx5kN7lKJ_h21lOVxn6eZFje1JZgnhnDyByXmRHXasMaEc5y4fR8ZkDAz26TF_pmumJqGp6Fr7io_ZH4d4x-oGR02UW53tMJ6_EBsukoMEZn68e2B3nMv0pbNx64msKkbjfXgJmVu9rkGFb5pK8og03M3ZBxLutYxR_H169xb1dAUzBI-EDLbIbWYO32YCbbrENMkznGTebPz3kw5_OQdlcwMDvD2-omoOHlzzhyt6XuYlRUW7kPXWSoJD3oCGuEVdKrukyxeD_zz3VUBQOfY6l7UCxAchPL4e59sFDRetu7Ku6Gjdo9_h-bmtxrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYT_nVtNjC4y3Po4oM0LAR1wok1DAXv13vlJ6D2BDtJY8Pnc8DmscKgba3yaFkEtWMDh2X3UMq3Q_EQ3gFYWCShiJFqq30m1Tykh9v1N7TGgDDfPyZ-pyFsvNr-t8QCp5wECutAQQk-gKlWRmR64_H9vFlRItU1ChrGw_Zd_31z49oqyj4z1t9FeH4MtpoWp8qR_KzDwP0w0C_Pz_8p9o_epqrj0Oe5tk-mSR_5zKnmFQdr69g53EoSSMwH69gmkS0IQr8dkOtqYmUOobv_gcnb90AzpOV08tv2aRWmfMbFyCM-FhLfrgNTOKN2t4kO2axkvoMOst0cq4ljK1u5t0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cnn5yPOB_jzTOLRCcJ3VFCw2FvP3CN0P0B3Xpd4KUpBqu32hwi-jFwgIpHwOrVsz_l27DNmbdlrMm_ho4nsFbOHvNztMcFPko5KdTHS20MMz75-Iv3Xqk8Ytm5Skh-gLT17F02FD4voghdwWMY_12-PM8nT7V7O6DufGOaiv_epuaIS_nshfSVGOfOzpt1n0aGWll-C7J_pfcDRRVAmdmImSIg9TNmHjdQt6tSofpzaTV6Ynt9v6epk7o6TFdTraO8LPnYYWPUdoyAeOSuAq7hmA2N8OZoEfn-E0o70rzDysrdelaPv7XT8-iXkZdap0C92Jvj2DGShWWF39pWcJOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX9UDi-HPgJdNf08sD-9V8sXBRefh-kmJOneNJIv-zM2CJFoTiFs1Ez07b6vxNNVaWJ92MGAuxzXtitfJTKF0O9KfVf74WrA0OkQKzBTlxpuu519lu3JzdQ29Q3hzcGyqJxMpqrJBbVYuTAp-muOdHjPkFPzzxJcI0ARwutRY70oOd3To5oJKbf0lE5jqa5qGijTcrF7u3RV3pP_0TmEXNbWM9uGb_kvPRwx5FduKJu4i7ZkPSYqe9M-ePPBB3F1nWDFxhcP71mNkRXcT4XHQhh5Vqdv577vyadR4wsobRm3vVHv6v5qEk3W74tBR3bihxtF82fdJ0d6rFel4Wlujg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2_ei3_pBDlKe31bqwLmEAcq_66nT785y_jJv79wyzJCA_HQhXmeJaJHdhRRs33Ix1cMIWk3zrm1abl4xgfX1V-zKa-QYfFGcT6wRZUxaTeSLpTWkm0suNbPf2zIBTiek5Eg67sdSKByxnsHf2p4tLvbrd12QmbTEK4KtK4somNMxhMU_g0h8dRj3O_1DszbN3iOIJc7fQ56-WBHEs0xhOAW0LEgQ2L6NJwU9YtrVjjcTmiZkyUXn-jzmbyNIOEdrEiNVFWFf9h3SAZ5PeH6671sl7p5k2G2-1YJGt9qarPJcBoZGvNcg3q9oRTXqXdCGTnakOyULzBTaP-m7kmxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG20Ynww6vMW26bijSE1k3OFjHzBXun1cPIPLDgUv9PRrx8p3a_Nm9dCm10bvnibWbrCsL8_LiAhKZL2lBHlewxzJ7kDrCdCk54yZ3Xp5Yc7JyszH2df1laM1Nfla8wscqClEdp-q46HoKT3LSOYfZn0fBFk6cRAyTf3c8wZWj-XUCDyE80Z_I8a9l74Fawdq7kZfDFB_RfuJvVlnYvaQmsf_GA11EuALUnCz7WurQearlIhbFppv4rMgaZDWQXbT1Llo2AENtp5rm8429wPo71LIYToOq0ITpY1PhjIgLhdSvreNFxEe0KkdI-dUMknAupmiKW5Z_Wy9N4PRsEokA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjxNy3SxXClxBE8opfAvnwBKY_qF0m3gNnXwvZ0FFVtguBeFC5tfmUC3anly3T6VZwSc1GDfU6IDdqQ14y7mdMyJmizLg-raZFMzUWXrsIgpwmosqwTZsUuYVKbv0VvUu22Fn6E_jgxSkTwc87CapBcEECYzT5sLOIkfiZki30X7VFKzKtFTlOjP1TgWhYMI5MozdXKpDA2058F_P8IMI2gcaM-rA9hIxYYErmed3ku584c_mAcNwPUM-3xvn90KB8rdYKbAJ85ibqDIN9u5l2435WXDaltmd8K1hEV19CNSVT-EWxVyO7E7PmqWdHRShy5AW3PE9GbKpQUZx4YKEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCcmlhRJAN8YZGHBkQ7N6_ndYfKH49JB3hXatoByPhPDiH1JcEqn9D2_LnK5E_1oZJgClgJ9vbqzTcfJ5ohDtW8GecO1rxXZtsZHrBizTHoKbpgyhmCDd1kIbvSzNdfU-8GZBQyFzkYDWVq8j3yGmV6AIkirQ6L7dCV8BTKGNVDcbL9kuII5HNh58W9dTUJKebecV3zh92jI_s_1c17QrYKFyIrx0WMYRwEXYKPaQHZQ3nWm0IwKbU_QDiOLF-ovu5U04F2-1C0MynMKraiXSXZ5e2dvoOBvqcuZITBN1lCCWzbRvsbInE5tpciVOUSvVqn0sp1JrFs5lmdGqquM7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oai2BANmDczQ99ebHCkDIErzAnP8v-DET3Bw_3SaMppI9gZmFghorMX1dvBvPhqjW-Btnfw31_4EVcptooVRh6CVR91w9A5pAynCfy9QYL-h6lgr4fYyiInhlYAOW3R9uR38INzR1yL45KK_w54LtxKMLtiBmFg3tTgTwzzALPdYUk_2F-76MRf1mtQIFDOCZCPjLdGzY4ceLjshB5Aa0tdsg9Y838KHYiXK34S3zfff7Yd5o2ekAE9g1wgm3GjYsKtAS5yJVO-IohFofA09DSxI7rOM5VG4rVdSFKgkSMthPaaX4Vx0PpKm6hiQYGZz0R-r5cSwEXwCtoxXWLWeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4C26bVT0-HLZK1-MhxcQwLehZeC6DD-catqGmyO_xOU7i1nhx1R0ykAKE8ZnedPIWi1ztAcwJbAGxG8MiZhQ2upQ_Ll6s_PfGnTZhwclZQC7Fj-vxuULzhO92NosAk7__ikHLfRQtpDR7JP4n_HjkYp2Zjt0jkDeOiA6iPbZaoWLgIzlEC3IIvSdFD4LONzvem4Esr4LeyQ3m2V1yoIeykU1T8eGQEQBm_zEkD37zQkzQxhCyRK9gDRqSO5-2tIFU4_oqdpxn9BSZ6XgKp-t9k86ddwk3qJ3s2Cl8uKo6NLthfO4lYREmlBCpZ95BxOLjUvxdFxxQqiQzHB49ljIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3lNYizGLgTvFR_5IK0Xjq6-ZZo_1hv4XzaLmezTazpy0SwupnKMbS7L9Wuk3nDdQZoMele6UTtWZySTe3tIPTHrGKpUuAI411XWwDgrvViCO6J75hvoTkI-vjmMvMmzb2E0RVllrUiF93rws8RVayiOrMyB8p3mziQWHrZogXM6s5q1nn38QDb3YiQKKoOaMaI59JAyH_Yl4fELE5nuNgiJ_P-v7Y3t1VzGO0CDS8yXTif2FzocvySibL-e9NdCFeSgxpkNwvVALQ0oEnjCzlkSO7J2MBU4dsBFWMmBDAC-t5F8J9mk8HThHdWba2IjOMXESIdJ8HbF3zUffXMIcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP1w_myG8x7sVAkz6wrKxXteOLZi8bUfED_vD-vGWr4oHklAPIwwdwEI9ViulKEUOwQrU7J4xS2mf0_1jA9tOLtZqFTgfnOLsSt_lS6tJhAP5ye3LRwTkXMs7GwpNcotvqmc0EkPi46srKR7t4jzKWFwDKYYUuanw8kSNwjLv7zF8pal1vYTFvd7K_vm5QLwPB8hqSuJal4QcaROdMV8V0tWb0ngw2TXYCgdTGJzWnKJ0-n47V7_VQYsRUyI_xim3wPAORx6p_aYQhRtZNKJIvTgS-x-MsIidoRuaPYFxvsfEwc6xGeXiecA11qr29VmH_GOCNlAdqm6rkSK3DQ4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKhV_oJ6TNro2QvtRD8DJ_XYAKOnAUjPt3SMOQDhKk57SNgvVmE8nNrNOi4V_5h3G-o9Azl2wdn7cEKdzTQpJbX7nU7lWPlxjAu2z3HO417ZMX5i5qCCpOt_52dVVerpu_QZPs-vHjnLeKjL0ukoarEV-iyH_BZSK8mmhtCdjMzlXU8J4SqQzdsWTNpZNa8f_EijV-MdDCfwNGh85muKG2JJ9DJVvRgUHdvZ731Eaeb6UmLF65ZM6eSlK2j0tfeDosqYKaiEzBTeKr-S9og4szDd7dB_8hZHsQLa2sUjJdPI-Mjku10Hw2yvsx8WoLLtQTEY10Io9ZSngkfGqeBnpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qu8q2PH0ZVmiRA1htLNsHZhrve-bpsErmoS340xcmtN8jVGuIMDSI9lJkRBgAd7KIPQwjw4aiIHKTPPpmAoilwBinoJUGeqp8zOsQ8QOTTVkrF7MlE-eKnNSeUL-kn4yJIxDsvYK7hB67xQ9xwEcXvLVM8L3jIE_IjUMA4zIWHSU-5wl_wmotim_IGV53Hy-dOA3T6njUIFhKjhfSrzUUe28hhG_HDrPTcKMbvq5JBvKkuyQ22Y6TkSyv9Y71UBljZA3GrCAM3BOKgJk6Iz5sVQTw69zjt1e6rCGufw9xSTZR4M2w6KM4mmCEIp9f6a6I7lyXubRhJ8S0DsVSqgyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnB2aeLJfb6_hOlze_op5elRzwK4-KbZVoydPg6KrhqHBKLARcNX4gNa_oXCvdxspMzBBK3ij0Un1e-A39GAf1UyH1xjhlI0SIVzVWUI-EYFEdmEpl4uZdMt643FTp3ZwYupsu2zVIvWm47qW7E0GXlR-ztYXFBUnMX-7-Vb-J_7ue7AV8l5llmLBf8-YniWPuvTkc0XyZ4Y1cH4luzRfVaTv_QILtUAtv6CaloA2bU0JcBjkvaUGEFFYDGVpiwTaJ62P2xkoqZECifkGIyxSBj8V34-vPAeHtgYDG71P90UPojTVPqtYqBMFEasK9HepmstxuJgw6KCHghMyxk0tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPESL6f295sZlrYbJJGogv0-sa8Wzr-p-G3JYDJJrLg-WWn_yPbf0BrqQ7WQJikxX8FqKWKPXMJUeK6hLwXJaNadGWgIGJ4kplNHOK2yjA4xzvoRRP5Ywea5ZgSVWFq6loclUOqTkKA5l93Wo1JnYV8N-q8ZxZ5PjNwKgqBq-twd9BuxNev5kyXBoSOShufmTy4lC0V9sLbHgp1SFYMefMnDFfIbspuIg5FD7mJM9a1Rys6-RDCXABZ_Op3gVJFPS-T_qtAYiSM40oJMdCKktD6MYQqgH_amYiptqRNmvYG6vxXa_Mhxdwz-T-OC9JgLyGR0VF7Ht7yLUxytR61Mog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJUG4nLdzieUlSI4VnkovfDfde5m-Igy2UsMoVBQMwZE58ZdpEX_j9eCOXuB348w4-Lw696wdEjs4rhh0vORkWCykMzKwNn8WeTFYgYlnLqtx_rvAAuJoEaDuDi-aX-WRzmI0star7ZQ1b6REPbOHjK0XTPJvzsvXELXstcWH4Fnwq1ju_oUioRVXMOKSfc_TP9S_mbH9qK2DVbiKuwXqOBGnTBf1QaeLyhZSKAIhDXAJVUL28bADz_zQOXPTigFAHQSkt4RoSFdcW219zSTJafPA09vs4UzZl-JYnf2RY735R4POvdYJObJBIMdXbn_yLykvNV5mUQjRPGb0ne37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j78_OuZWP5uBcaLpLe3_b8JSs1nmmXoLscPtz3OFr7VZzNKUpZYGQZOqHsrmlPYYII2SQMIDsl3mjKE32DHovx4zpPX8dBAmPC7-qE9D_3jY5XSawY8Du8QQk0R7ixCm8zpIBPk_UT1-iH9JoBWTTonZaHo4m_rWnpKoFo70_8jAVvLJf1rHeSWcawPMRryizglp38GzmUSRhroJRWjfBStqLdP9ohZAoYmDLzbB9V0i-INHS_xjz6OcoZ0dTYGy0MFMfmAkPAz4PhW0B-sS8GDQHv7qw6rhumCJDOWxVeuXcZrVEyS4sz7wcMiFPy0vDRDHdeTqMW_cmlcV2TOsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kc3BCF_2ZDfP-h7k8DFBcunBoU5FO88lQ3vWmBE6joW75AuLA2pAc1WdoRsZLal97eAf3AaAAR86yiGmv75CZlbt-1OWUS89q5tji_IbWZMTrcD_mbTX_as0s1umBKe3NEB-ZvGMgqm3SwtfN6ri8F8CsFrxqyEqM27p27Qkq_KhGG0j0U4VmPe6a-btU5GMgl7TIw5F1xa0rRWis8DqxSDoNc1ZQApI4WB_mlb_ndd4BMADvIfWobK5gHrByOXSFrosigJMKfVJuAiP2mhZpRw_ImdwP0DGUoGyl3FSFsIbyK37muun3GwAuzqWR7NkHJMtK0vLprRn_w2ipNnz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4MVZ4d3Tru-9CFyiA9aw8HPCIT7RSKflU_5WSfGuUpvl0wGnU8kMZjqaLURJAhje4biImtjR9FwuDfNFoED9OQOy3c4ov65JbVB0Mg_2-VkueY6bsC3rThc2-TxzI9U45MN6b_REwoUytBNrnfnUdr0WJf4cPcrnpHD2hBEtn3gNk5-KWGhk2MsizKVhkU2h9wxnYJtIYwXPFQe2hf_xnahemi1nYZlFWYWJQ2TKKPESeY5GbPTEKOHBCV9EwPRi7Dugh-d8vyb1xp0xLAlGwkNeNcbU0-1etLYRdhETbmQ5jIJqsfQlGSbn1JD0iTwpS5FrlPkH1LYeDUcLStkHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qz1fQ-tj4NCZ0JRR56XWPkiMy6knz7iJJXVkK3mfR7E_-cPgdgUt3GphDUKwMCTSzgYnagyQCVDoAGylOwkVuOhxOvZVFYsl1L4mVUr6qCH2uMGTsvxGQuxJfCyS09DOFpYgGXIZo1E2rzh6p_849DvAgAxCTk0p4kvwa1jdEY9NA-aGluOG1YOhLzY_XNz1ZAA2vwMQspR1zGceDUjV54JtJCR6KaU1TodD8O4-pFggorS-B4DB5iSfiTXWeDndNz98slBtTSqOmcW-5OL6q4Uj0PwnZmC8u8IV-UED5hl1rKg2MPsa9qzJeb16XHcKHY-7q9WbxGVUdFiYmlTwpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcOiGsIfDqlCjmY2-AurueiOWtoVacYPhKZQJCVrHTp8vXn8bS6lKtAHK-JrCov22dV8mjulqex0JZcDz0kHUS4oXqnLqY11KXnxLhZb4-RF0IqWVGZYCg2atQO51TuBRcnAnmQ4UdV5WSquYdD51pn6CiWs2muYelcawZlGazKkmzsTU9HoA6G51052tr04NUwgY3rjUcTUbAHpIBijik4LvOHVEijfqCj9bB82Nxsz2zpl083Qs09_APZY9BOSKneeZ0qve8Q5kWGmRTJxn_HS1Es3ocy51ISK0PGNAAfGV6cRRIP1PAbJoLf-25BZpSjdwFDeNFddHe-Q3f3IdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-KbCJcxGEbAa1hD3x0XhE88ZZPstntJzf9rlO3TsznNdz_OS6rXVq4EP8w__qDo5I1kHQPcOyD8EwkRFynte2AmDBcGy_WzXm24tu8ZCXnQUDklnreajQW6R4bxrahpTLZl_EV9YpCpLZeESxmrfWyhLEeja2dHh_4gSvU0ZE_rSAOHbAwoaKDQ4EVcfdSLZ8Cq2sOqxwlQhGa9_f92gAPsACwZVaTYw5JEXBdYJBgjeQ0p3_AxukTJDHS1zbW1AYwVFT9viUZM1P-I1c-4fcmebmSOA12ubwyEMH9uOq0ybgQJVoXos5-CWyEQgGHqAEdJZVyTiArzUok6dIRdQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sw47jDvhm1dy0IhbvhC-3VBVewJSTRfhZS7XmgtsCvlLRTc5e8cPgP4kYPp_FfWqwxMj-38BHOJ0jRBy3saFLo7VYlF9lfzLlRqtTovFMxSDFUfGtE1pD3Et1lMb-TGW4wiwpegfFvu459pO2GEGB-SMakqf3Av3DXjX3SummDG76kxKFBpAA4oFfQaRAcp3mAHuL4XDNYIjy8RBJ4akJD_kr7iz6g9idY6JYHSpPd637V6--y2kpcIMIq7UOg7YkkAk2-ecV3SN4falsbkHKZXsABQjnrsseaMcLILInfI5-xx0aeLAdjeyHXkZLwTjqjC9g-ILklxacM0oUUC-EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6D5K7C4MtLRNYv7AuAUOyDcEuEe-STSnwzqSpWH1QsJB4QT3oMsQ2sj1I-T-bknu2NuVtQiD_CEZqYOd6Hku18nmclq_XuS8HbLWa-YrrWWxZqnZRjocLLKSrbiC9dKEzNxxAGRmWIlQq4DkRXxqrMmbdRN5gpCoxyl-SEEMAQFGGyQiUj3k7H8jTi-jZXbtb2cwJfauZE7eqCvG4h2S5T9jSyAL2b3wlXGbmTlZ0dn9Q5oAaKWQU9W1B3MWWmAmUvpbksE2THVNyY72cDgzHLRB03Vk9O31arNL9qfh_xGs9-AeAAFM9FolKF_zRhOZGxEfTZv_7lcFU8jtacuPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KnxgGCraiflj8XSwFLAkTu2wknbYcKMN31adHM-9gYpbVs0CHcFRO3YEa1ltvSw9qhkiI6i784HTL5YboiTz-bsFxRuCvL7c3Dq-3oPgxZ3YGxIMBQyRZOb1olKTjAl4kiNPkHEmwBpDawLYUvWuQBK1OwRyuZ88zwARCUAer3CbL7KuDi9Z9bs8lOIpYJ8TqvVYKX1WZ7xCFneqN5kOAYKSMYp0U8quYNKDUq3vTnweXDZmG-M4-xy_xGgebUSKdL6fgASjX9a90SWDHedVhyV1isZAx5ADPxy0meP1cJpk3_s4MMTzKKxes2ygiC1hF-3ciDB8J-ziTXbzNa9qCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/co-_Bv76Lnnj0paRVvmu2HDwYk6oEv70P_So6GtMjs_YDb9_Q5vZAVuI_qKJcbKD0hnzZPHUDemiPuFw_LozDbRgpJH9GQH8yOGpo1zv2mwvvEFZoZZDEBaUHiNaOcw-PXhqeSbJeXKOFSh34T08ds1aBpLvjMaibsfZhkLz5_IfI3KSEM3l-CUmWOuOfKI0-nAEqHe8BmaA1BdxEBgjoqsqR_ztXyU3ISJnk5yY_74FIm5nF5mP_hh2c05gdSrzWjOcSccSQgx9eWCRWQuiPsox3N8gvqyiLW5SBEuGbBPYYO98nmT3N9zBZPS0OPX6pgABqXCimtAY8T-LOKLbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xp1AEdnaTgZ2_BHTgEznWKz6ni3_7ymmUzGFUy8GIA7KlPzGaXq7O0nutRCc-gmIMkCyPdTT7qaoILfOmIk8pVa4lWrtT0A_yhI4otPodxuUA54SETxZtR7gJ6sAHosYcwIJ0uugrju5XnsZU4cc6KVpERHJYqHAOp9MbcTvwv5YKbM8OgDFn_yR-1Xk-bg7T1HSYajnbLg2S7N4eBNRgxFCIBAiu73yti2xRGhzdsINtvxPUfGUQWh5lbptTYss84JuxokD-ERk2LdWSEYco99v0ZiF7SD3aKmz4V2Ij8_5vRuBDBdKneKD43HUpvI31mr-rDdY9vcGipns9LB4sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnH22Nhul1DVmrDoYrp2imUHevAa0enWCvzdgRLrH2KzTCK9o05vi1i3hUsYuPx5X1wKB6eUQRY-g0Ql09LwU-jDynY4GFmuwhhu8a08iTEpNAXe88ev8AelchfeiDEqhMzf2wWy5xqIFx1aQvrW-vP1eGplykc2GVBODDwOJe4e_AoOTyRhkyQ3r9XwoSGQi50LH6tMg8g-n52FDKwEN36jtRFWbmwFNEFctKATXgG5yL0D4ves06TGWLR0a3otLSq_0LADVpyXIdFnTMFSC7uJFi7NV0d-Ap5C80X-onBbDVPBGezkM8cMbd7FbC0ivQ49EMC0-jUzfSo11IBmPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4jHElHSnXACtcGM5huJi6hnplCTZqGEtgmtrGlGavyIqMAvM00xCo7hqfHX5-LbAXQJh66hPNqV-sJSSxMeMGTpoiuy7JVVksFm8SjBWrityTYXKWQzOynr2wUxBbMH5TmetoPblB3SNye6R_RCSGWZYCx4xmxa-Slr0kCVVQXyRa4OgcKXrIl_Lqt9GkQ9oJL0AdPO0n2C8S4jeaWMroQpwufnuzyS0_sW99KI5CFzwWLIBE2r_VZQQRxqt6JFNs71ycv-M-iZnfAZEMdDFFKGRIkL1hV4Rm51NVLz_4fz2yvpsahQSo5oIVJypl2UM5OiDV0UzdvWri5Rv3SVCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN7BWVQ3DdYaiYFL7-2b_JwJUB_3AuPAiWkt3v7EeZXmvGs1kglSVkOoBv9_PhTh11r2xBBQpVCH4Hev-ep7ukfCKC3IpIhWnchH_Fig1ZVHnUN56bsmG6vBXP0mtesqXLCagmr9hGdss5lLxgOgIwk3xJJosU2rV1VQP_onAVALRfqBkOZ4E9coG6K8NdYbP2M3sSp1kgBLe8Jtn5rFZoKCBOFz2WnAsbtOA7oN6Zt4oZ1778Ing91z7IbsGSdqWNM2uX50KuDud37QeyOGm-gatIPuYDY32AlzAwnhyoLpiVMqKJV44pHzilu08pgTkTbc2DFTW7eqphZU-naZLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVZOnhu2qBplr55QPml-IVtNhDC-LFiOM9mYt611eEbLlgXjhdlcyJSIZyaEi-8BJgZ68oJV5_yBWGFx0IoLbMJpgl2VRuofBp2VQiBwKI-CsXaebMUqErH1GZuMoegBLkD6qJ15lX5bTPKQFCqelMR59cvLCf4ZQSRpK0sIgGeygjr14dRzEdm0WXUprqgw_1BQBHU0HOC4RdtNNJPgNxvtaDCQfnHvZZDHux8Uc4pZN48qMQR1Ie76U9vGq9KgurP3YVJ5EXxAgtgnOji6qYTp4scmYouTyBEyRFrMoCw6nEgv2tCJFZUT-0NFIxvlhVgp8RHWer8LgdNn0Q0__w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTXEQz4tTPS2xJJBQAKATC84OiSZnXYEsSR30FgtL9FYts0PEMJCDyxq3YBReW4A2S9B_ojFC3Tm6mWjQ7dT6fQj0mnRs876V5h7kzKGiiGJPN8Vy14ql0wmde1LUNxZhexI55qtLRKBjFyAXyrHy4VqA6r-eQoqWrrYnPG_jexIoutxxf12tsKNT6qfyM5gE61oe2kB_JdFdGWu2fYraL3vzSeap46EA7qCd8f-uTgCWwUAZO0gCR9uXtDMFeEMqYJqrMvRF3GcjjizOkfXvpuO_TG-yX0Z45rYJKeVpT3nZffjqH5WJx_4B__Y3bIzz-eINTuYpEUSYPTILpmZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BL1Bbw46cG4_ipJEtfRp9AzkTTD5nXfCYz9LfJrlgs6fmDw6C-8tv1-nhuYRDPn0qyJFptoYEVU5goqmOU-pLYMT574qyeM0ru7LUmIKuyYyNwiTIyX3B4kiVe9cRHkLz2b8LDe8yTRV4qbwc5kRqm5YoBKgCrkkQT6xMfKt1ZFrD9tGWUgYuodsv3_ZYEh-cEAwIXkSXS4AqWN6NKVe97XTIgRpdU5fyijlDqr9XMi28sWq2vCqqtOczlw7H84su0sSm5uUViMAuUKZ03CtFl6muGbOCk8JYZm8E5MhL7sQC_2l64W5rqen9EQqjLf8vJgQu4Bozpre01tN5581cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0bO8M-sGmRcDlFBt-w0-Z4zGCa-4EYKv5S4kXJQ4aR-s023DPT-FMqxA4Ta5RZLCdVKDf2CpKNSQyu4G49lUU7Qth2yG9oNx_DgO4w8soWM0E1QVuOl7SdCbHU-qOqemAM-IRfrTjRjZX1EvQs2RIi2Pr3wIz5JHXQ701etDGWQuub5HUS2nmHHQNddWemVR2C2k7hvO1pjyHIBkKhkp7rBz2qahe8mbDklNN17f4mBuj8poiPNxPIeoqxa904x5F-pClBl3gI8vFY3FLv3GD_PkUYuzrZbsfzQfTBUJ6zOVAovp3M6l1rPgqdwejwoJSTa9y9snZIJmGtvV9sMng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WozlEsZmpe8D7zRn5SkM9NY7UiuNDzQvX21FkTT_uvwUT6kCylnLLuSS6prSEfLrZwVJNzpviP5gfbngXvQjAo8urgvP79Fd6uHTVIiCIgkOWt0gvsVB8XYCLo1Gi5pjclg3065VNewr3OiBfNLLI8wCGOKR-lWT_euu4UeHn0WW-kugw8IshFoYNnW5WC2yVgh_ybD3BhrU4GkIirJeqzKGEUdcd2r9HX_Zee5MHcviXWU2RqJYeM-BMYMvBsQyn_y4Mp-CQx1wr7fkCv9CjqUTbWBs37B1P_I_8M9Y6KLm7mYLNZP1aFWVSA0MDWWIdJYs6a1B7aQqJxPZBN381A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=e8GUH_8V0PvN6MB96SP4pska06Ks4xhBRql0H01K1PECYmtFDf-AgeqnY7Uw89LhEmP_SUzfe5JLySb6YO_RQdKw1s7RfCCRTOj6zBAjyq50gufvScgyDQXHOSJfVlB5BgL4dZsFXvSOKZJq7Xnt81wOxTIkJVqlmeonKR3oHCs63qktuyH0ro1OrdesPiQBMImsLvZHe_aP8Sg60R8Qz6LTURAgUyCQj59Ff1t96ANWkL0IGHkxXrwz60FOzC3VMnIfFxuucMxXsIGpjSXCoFRjo42piuKoxjyxD5WPKf18eIANlYI66LA2wh-TRKSg6sXI8kGAzXbgXEzPiTVnsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=e8GUH_8V0PvN6MB96SP4pska06Ks4xhBRql0H01K1PECYmtFDf-AgeqnY7Uw89LhEmP_SUzfe5JLySb6YO_RQdKw1s7RfCCRTOj6zBAjyq50gufvScgyDQXHOSJfVlB5BgL4dZsFXvSOKZJq7Xnt81wOxTIkJVqlmeonKR3oHCs63qktuyH0ro1OrdesPiQBMImsLvZHe_aP8Sg60R8Qz6LTURAgUyCQj59Ff1t96ANWkL0IGHkxXrwz60FOzC3VMnIfFxuucMxXsIGpjSXCoFRjo42piuKoxjyxD5WPKf18eIANlYI66LA2wh-TRKSg6sXI8kGAzXbgXEzPiTVnsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEuJpjs6q_mFvfUQlkZ5fwIMPwtJvneDofiGg5AzA0a4FKZ_nMFPB6Ne3Rkn8N2RHnnyE_NtooC_QMf_iN4wDgE7XtCG09IkWpZFugIFgITGWBUlAttv87O6kzmlHV43v2ZiRxESfa7zCs8re6quo6mdXl0Z4GaT6A164FO8-mM9tVcT3VrHEgA2IeA4TQC-nCroC0DMQ2D-vAcjd0YCWaBvPD7R21adTsaqR7k7EjkscwyHCyYnFCx8glVM8K8ZNP0lJZQpFmj1UZkvpAfT84PqnL-1Wju8dUYPC2xu_AYIQdPFDNChC0ME0KJlDwAr6GSA_grjswPfjNiFqqmeeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqoEAcvjeCe3_QgABQhxRVBjmu3krzq3IFk-AQ7ePNIJWG7GtLH0256Zur16BDSXEiMRWjQ9A8waLDGPReot1PDphBTJynXm1DWjpD4hpMsHz4I_NKSftq-kg_cMxKV5wL8XKVpSe5sRcHrZdlG-SrhJlzIMQP5sW3lKguxXZuDVIopehU1Tu64YNFqZM0Ty-L0K1xxHq0i6YE7t-tjhSr7p2e8LdKfLv2BUloaJYuSp2MKnNbVpnUPV6cla8A8yGhNDXllWCP7WijdkIJ5h3I4j9jUP-xpIviZFrK49aFheR6SUwPD1mO1Xm53HYrLj6dxR-Sw6hs9azsQR2p_o8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPQMntFgQ5SF81Ns94LApmXVFgOH3ZyX4chB70G7SnD0nSS-3i_-HdNf6t2YpgHrE2OSiEFpwyQSgZ3XmuhKI2Ut_snJbDzAEgU9WI60DNWLbhzKt2NUrHD8M4DdQujUBZY-UsdZD5dmTFKnA7WyfbX7kTpqVCpcv45AQQxR43sV4QASwIskJdBiI_-TgSFivPEnuwCF00xHYIgx8ZUWAZd0b3H53KXLOjR51Ybmv8JipcWzmEVTIRDKvhWmn_KgSqIM-9Tm-wEbaYRK4SXzy6DxCIIy9AhKKR8Qzw72NQIillVhIJJTn4OYjby1E5lmVS-ZlXhfoapNhR6RuNyY3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0d7il8csQjMlWDEMJTnWCRPMqlLNFKgIB1rLqK_SkMyVUuI4DqIIcJlhbq-e7SQvB8yMCqY7M0wSrUNZ1xhWvOJjw0tzFWsUbGKt4ZxJtP-UoaA_MWqZ0rfeG78MqhxzM5GnEpUWVXrr_BtjqkxNYDsevYaPVMveGQKMjEOPvVU1sM7hkhG1nkZbmVsFl23g4drK9xa1RWNYmN0F5whrnQHSC_PfApf8RqDsp4uluvDaN-b4EYng-0gToZc5XF3MNHwu8UqI_EeDnf_BSIING8nATdBVAm0qblpx9p_sf2Bqpua-lBFCqUQsovh_t7PA5EOCvsTly3NUJd12g0W-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey0mgsIIAwGMiFv8CQ1LU-DUoo-WvnlGS2X_GyBRRIVNrpXVQOERwC5B778ewHoezrRVrv2epcm68u5HY_PezjRrf7kHriFhI3uqTHSUHAp1obxuXf0lRAev54iG3N2nv1_E1VEq0tDZMMhIbZiS6hVJn6PCqxQSiZb43tHDigIpWkih3tNDM1g4x6UfC10LC3d0zZ3IqWyESOswglRR1-hDs41Im1uS7ekUfbOw6QSope3nfsmmGMPIa8GHtVyJF3Z9aCfRqgSY9EcXZQm-6Zx3A43UXL5mFNOlK0KAxVHDrFUNz_UTPgnLw1aDKQ3Bhbz2E5f_OS17BPuNYfXA5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDA8t5WbsMV_oPQbMkvjpXL6akeF_gq3BEJwBqwRpL0NNSJdQadKAYS1FQz2WUm_w8i7rB1BG7ydZPa03DA7ln7qyIt2BfshVnxvKpxZ6vlGPlRAzRUExy8fWhAfdrKLPMXYroHHNQEsinW3hFT4UlFPryNBPAS2kDfSDSDIWq-t3qdoldeoRzTTOLPPVn0-FwzFIRJLNhr-qvIffnzl11e8AP4ZuWX4riZm5HFpnW8aZUsXzbyvXOorkaMVmUqU4RdhtE92H-GfKubwJA4R030aZz_CckqqOnfskJLQtev0gyDtK0mfqYaRxRUet4ZNzMg5kxGs8IGvq342Vn1Ygg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO9raFEVEmC5c1Z5vzAMYz5-j0AhppPjzF9D0XO0FcOjKdiPmSaX_j6GXlcrUU0VXYeXHtk0z1qn1qrJjWeHhsu2An7yWoTLos4NT8NDIhuOiq4bn5HqAKARGY-_yWAsl5FqZ34RTv3XiObtGChM1Roij5yTZdgp_W-p2kMvwOag7giTb_Jl1j1gA7TSrmmWdke5ITKdQ5LD5I6JIds0N0l6TpzbPypPg5E7v41mkwsL7tI1mkyIiqsZB0yK3IOKewbV9NtFmqJAF48z6xGvDUSaod1_cWnJF_6PKsGVhYgy3TbGqDY-OJiekyxHd4PpYFo2YAiCAIOEJOXL4isn3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsxwASubwPD5zvt-dbnQMxuFdt_We0_JHbWGm6A99XlY-mNZum7AK5SZA3TbZtFtjBiA-nCYAKU3p9pOU9QG8xy7KUucRE5W7bOTn59zTBoYvZ095ojBSOjCRLD-wUM3rx-aF1WwynZ4oYG2CkjZ8otH9xEdBz4iS5Jcq_VHOgF4zpwC33anEifWKW5XTWUjt8A2gPyClKPSyp8smHOeZQ3m00Lx4riIdIeWrilGoh6KDvWsYeM9X2Ncvcru-WNqsaTjqWGfnxzhX0vX_kS41U7BcddCp_iy72dcoR5oFN6HgXsr5SvbuQ3kfqX1gky9Ush9vLRiYTJeJRYBM9elLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQfrVSLqGZ8a6B5RGLc_oF-mxfFdK4cV8sbh7bZhwUiH_1aDO7dMInoDIYGAQz1MTPfIAhY-5TgUIsT0Zvfk93PSaUvv7Hp5iMkEL4vquNe2V7UR4tKyM1cw0whe8-eWdFTdIqNLhuXX-Jp_YwB8YQ001sOEzBX-8SjS6caWI6F5LEOXlxBsQSlq3JBMlnCl7bXNRsQhIMLQoURjYyY_VKO4BdB4PbQkU0ge1SxTFbuuOEeGj5OE52pAj6eQAVoGMIz9VI44lQo2lwIvKmEgBW0bOGmDB2HYBdfc8KuSWvDjSQTux8A0SgznRegKLQqk1WUkgVv7BpEhxAnSLfIImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs4X1JLjQefQdMnyjGUOlcwboPdgYeFzotFtDfgEutlW8pz66d27hfjtGWR0pxfy6TNADFpZsk-bYPyLc27wBTL-J6WY6vErlKYp-fyR0vUId4HbrRoGq6jELIV5t1xjcCjVSEHUi6P5Q_2FBq5Q2lpcA3YNv8tGIDsQc0-2lE71mB0I-CsKEKnuMmOhUpiEKVWfDYlw_gByrsPdOqk57zghyfAjpaVEGEWavTT2EYtDaPPfSahZDS3VdMKc8mgrhgS7L3tD9qvXrtJ7CvoL_XWM4GlcosK-NN2Wm_59ISlCid3MD4aQaa7ZbsNqCjAtC5HIWBtEYtU4UrNibamIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
