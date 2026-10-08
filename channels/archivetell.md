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
<img src="https://cdn4.telesco.pe/file/i2c8kbDI68iRiy2VU0_Hjvp9iSVmAvte8OnA4Hnlx0AyeGZ6AQndltTKsKhoLQBKxMvukdsrNUqEizx_VnFBnMGJjBYQNwqpo6VJLP25Xtd9ztS_Im8Mw7F-qXUXBV2TUX0NkF5IENYlFRHZzT5lG6WkI-_YSMvJVAIEv8IL1BIDlsY1YnA_S0aghHiAstZqiwmU_8aDwvukCs2c_P4BYdEG-oSEr3XPMQmGgLIOgoHJ0cD1pDphiInmn5FLexc6usfVnFyaS7wiHnI13QK7FgeRJwcVb6a8Cy2ai6sDBJqxo-4OOlA6FFN948X78retbsQgXSSF2RhQwDybSxgwKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLyrP23vih0QnII-Ofbppwbn0asmTg8hM8ppMhiDFK1MTrzIwpf5sP4gtI3eiBduHvvmCgc1mmq3GQDekYIZR4jwU-dfj_7LHhGyyfT0FUq2lTzGrpyLztehlIf-6ai0nYJitPa2mIw0NdzVFzuUn0SBNiWrMV0akm0nkLHVZoWYmDoOuiBIP0F09J-HV-8Hon-kS6AQojWdv9p_U5hgwzXHR5Hww5SCqrWavhiyEJL3WsO3_3XV-xLTgrAbp3v7WlQtSs3IQ3NBkyW9wzvt6h9nZrPjjvw1qMe7BMv33sDSYVMolwArkvCBMkCVJhY-pL7SkjhA6zXDSTsY2W0g6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 787 · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Es302l3gDJtbhyFFkCXedpcSzveuOJZrZYZpqWlri7kpy92dZZXrsoWWYBR1jFGjrjuI8ZeMIxomYokcNEUeJfG0dN5rfXIICdQJ3cOsR4rk_cijcPJ5zcdqx4Frq-RWePD6TGlsp3JshemfNEhB0U0Hcq6D2ldyFIWLYNpIBSBu6Av93DHSfbkOBR8NjkZBqznDYcZr6Ed2C5wom6OQHeBM3wuZho-JEQAik84PH5neoxjY7y8WKpZYWTEIeV1jdYkj_Tp3l87uiVwthOsIr8H_IMlxBa_MgAp8xNmjIrRdXd2PWJOIevIllj3xbFur4qreMhcqfWIj9d6pNoy0ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROMqXkr8freAi2vT1LAwfIaeRUjhSn7yUAfb_LPZfOWRPRcdrINTgfnok-L0q_otYMW_S0QToEJuQnDMsXvsu5NtCBKrsL46iEpsBIExlGG92FqXWx9m-nBIswV9HmNIEaShoMrkFtEPhGzA86U52_QaWb5O1QNab6X0FtJWUjQkw1Bky0RFCewyD3TawuanaEOZELUe-nFmrvhgkfsG3M3WPFdifsTNjj10LuK5yfEtvfNpeviJHyr9ApO1bEARKrPoTBuKw5N1MPt32yI9nB_FvHgCCXaaqRtq7vZuHSmG2izAif92c8FUXbKge0oIHwmYaZAcCQvd3akIQw8aeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=eA1mhuIab3vdBitxC_2b8ynnPWQIKcNMEfGTcFdNZn9pjJPp26zCuDJPSx04wOCyFE1OftBYxuYm7rzEvpej1RymUNHrsZ67DLZr-k9Mz1kMJ2l7iJLl-fa9zVob3X5ytVmNP-i09BJ_AtTyN3YmtOlvG11f_OMfvFgRnPi5Yw-MSO8uEbzEe_L74Nkiuaccufs0TX7V4v9Is4nBcMUtP9sz6iHMWGotdHJB7Y61sur_Aki4-G8GljVCxEBUhnhuD0G8Mf4H6XO4QEsiXvEa54MHVd-p2wxwEL_UztkicBFgLUwSmyYK-OBmmMV7ILRq5fe8UwEXuslMqToiKlk8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=eA1mhuIab3vdBitxC_2b8ynnPWQIKcNMEfGTcFdNZn9pjJPp26zCuDJPSx04wOCyFE1OftBYxuYm7rzEvpej1RymUNHrsZ67DLZr-k9Mz1kMJ2l7iJLl-fa9zVob3X5ytVmNP-i09BJ_AtTyN3YmtOlvG11f_OMfvFgRnPi5Yw-MSO8uEbzEe_L74Nkiuaccufs0TX7V4v9Is4nBcMUtP9sz6iHMWGotdHJB7Y61sur_Aki4-G8GljVCxEBUhnhuD0G8Mf4H6XO4QEsiXvEa54MHVd-p2wxwEL_UztkicBFgLUwSmyYK-OBmmMV7ILRq5fe8UwEXuslMqToiKlk8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpO-eAzWOPmYgZNcmd7C9ve50t9qN_VbYuGuCC3h3L9ujBmxx4cMkVkpgYmpAEPtQsdZrqYtvUdsmyWTFp1RIfkpsFzM3J2nSS0TwEiWEGYqB2pO7sPYMzbnVW_7Ts1aGFvDIbaKHN1IK7P88iLwbHL5k3ppXLvTSPrctIT8uh1epAw3XAaLzZ4M8ZV54FYWmaBEXVGogbtUW0zLQa--ZdFxIL3UltYUINGurr_F_PpX_Vna3tMycF_RwCdQghsk19h7LbKt1fKPvsHV5In145wNQ8q9Wcr66AophdCyjWToPxAQ_qekMmHUmWzqzgmnLM-wa5ElVxS77KJAMn7kdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E382gsUcGc17gX5ElB4fcTxn8R2s2KQ3ZFELPfEnQlhW5KE-g41USPi8hKaAm6J-iQ21yUnuoI5BYYcDvo9K6O48X5O8HgMVlNZqQfmfEi8jcG_EuCCPRBb2MavzEmhHbq1MiLXqv3sMbAzqQaYqyOJCQIB0MCQk0xVPRDJcAEsgOHOvYIqeOg3WikjbmvJv9DR0TBUgSwEWNflUuBnN7MGTHnRiE-GY1SvjGCBWtP6fi5kh3ZwppyidYVHA6ZNe8yuyk-PW9tQfZHrtZM_HGwZDbxNUA9U1f9yUn-IMcBIAYXtA4EV95haFOEOs2lnOBazwOz04OJhbUUe2GcI3Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8-6MVndVBpSUnWY3oixfG0lb3GG1jAnSnyVPJCWNuRstN8urcxvaTlMcr7QzyAozwr6LzUAlHCN1I9WvKWCEiNlh5OV3DuKCJyvuYrULyrJN38Zh7pXzStEaCsjYtb5f65RFrge-esb6jwy8V0oHQNkMKTwz2Zaok_qXOCTcnfKPrroIZqyIMbkQUH7DLEgdPYQDxwRLkH45RqRkP3r05BiPirdd9WLUjK8vCO6NBzYIh_N4XODEmmcpL2lGKGV0tZJ0cszdIZwshGlzYjiZDs9hi-OMq-Sj4mlthbD7j5WKjO2CM_xnJj6TWjHGGkcvWmhdvnoYF8eFWeSSGPkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CdMKcLg9u7odtfCYD0mXi-6-FCU30SMkZHMlZ-rfoz4knVWDnfa-2HuW5TL3I8_drLD7jvkr1LwctZmaZRtApDrunFrWjkLITiBdispSWH9uqZVoPRsxdkId3tZkugCPUmWNoONNFa-Skt84Kio5qOjq1mr7OqmBuaPLG8FxxT3lIyXmq2HlSMwFpnvneofM7zM-04JjNN49VNx6h9KLlEo6WIWQtDucBjVF9YKfV-YBoWHHAZJGTGaLbd0BikJw5mSOE--Tq66K3jQ8w3CHOQx2W9czEgqX6BuzmjUReqw6aWa6T297rPwEIPoJtDOaZuij7IjL9iLjkAao7nCLag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpjrrPDrFuS8kZ1w68gC0pJDglsNd04HQB9IHDXZQPWJgSMGv4fWj9Dq-u0wo_ajW1pDzaDPQkZNxomFUTF1nUXXjymp26czqyjqAhIxQ9qx0PM-Aldj6eD9_WLWpyrLjtOYRg1eQfgzzdoDI8j40xz3M1D7TceR9fmibybMxRN_BvWT3scC_MqLQ44D-ef6-soTbnvwktGf-XtwutOfQH7zEhqBmzDE1rAV1GFYUuyxv4_xvoDmvmdxRA3NfA3TBqCU-PdQUkUycd2Sm-iOE4hRJ7W5mTmsiA2qF8trwyAldJgwKzDtQyOgYn84Hs3t0VYNEz0dB1UgtEoGKQrf1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=kCGoZ0-uQACrG7DT3XATKwn5p2owiZtZf83RBlyturBPJRGQbW95LZbgtId_MizfI_iIfGVSIBzWzz7FWO3gWKlIyPwdINcZSdLVJe7rJpHHc24U5LEAjML5pEs6m7a0o-1GVHUPg-_LKXf80yrq02nRxCa_Uc208QOB_35_A9dTKyfwF__V73eoxXD2EmoQkKLq_c5PKWAyacuPXz9OyuGRukGfmj895fr1cDFdCJoT0zFEykMigTEVTPVwl72Ihg9nfdJXFiY0puDGsQhNN93CEobwUyFaEkz6fae9GFTjstCpR06hYlvCDsPBtCHS1Y4mxDHNiyoC4qtIT3t9dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=kCGoZ0-uQACrG7DT3XATKwn5p2owiZtZf83RBlyturBPJRGQbW95LZbgtId_MizfI_iIfGVSIBzWzz7FWO3gWKlIyPwdINcZSdLVJe7rJpHHc24U5LEAjML5pEs6m7a0o-1GVHUPg-_LKXf80yrq02nRxCa_Uc208QOB_35_A9dTKyfwF__V73eoxXD2EmoQkKLq_c5PKWAyacuPXz9OyuGRukGfmj895fr1cDFdCJoT0zFEykMigTEVTPVwl72Ihg9nfdJXFiY0puDGsQhNN93CEobwUyFaEkz6fae9GFTjstCpR06hYlvCDsPBtCHS1Y4mxDHNiyoC4qtIT3t9dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1I1keKvraQAqU6Xbi9s38gi0hSSQHr2b9g-dWDWf-OT1ydJbXEU2u1fjw18TobJruHMk9_E4yb7k2obh2TYWnAOIbA7fo_5Qwav0FzzEsv63rSJCqw4oM5hlBzYr6EIHtdNv7Ac2stSvlu6VqbaVkdhmrsnStlL7vtKiIfqgaalpsfgXKP3z1pKzFKqrj5E66rOBQthQ759FtxneiPN0ZU69sgJ3OneMy3G6mIQMyx2S_Fcnr0uW_YHX4xJbJSeiJ1zVdj4xiuZz2OTQHZ5vIZ3ADcZmkNI94o_8wA1EbuBQlYx94wmSG9Dep3DTpjrAIqPu2enDrWdBBM2TsNyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vS14kyciOgEBmjzCy0qps9PV1xRayKBq7XxpGAKff5EJcvtQ1guSYHB99dcpl8lxblBlmSKdYlDAke7p_zMEGJxYR08vk1luiTA35585tG03r_a-7AE9p3nY-t11bSJdoSP1H_FGgaQv4hVnoGjn0qmndONGzFeQCvPVXpHdwvMHdmjOkRkWK0GBwhaZPW3yM64I1ySR6WnOo1M5MyYzGhrNOqw-bUX03ni2k_ujj0hAzelSBnhaLfLSLLRUbRfVhDk14FKPOGs_btErUy_yRvjY6HQauIhRFZJfJcEbckoilFDUQWNKfIxBlbnpM3BMg1gfrvksSeeRzu2UbeOFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLL3hTo0kNzBoXALZ4fh7JnKe4IpHtn7hz8jB9WeH70KWPJMDl99SQKhqR8QXVi9rBCS2h5tmi8YyGUFVN0Y6id_hlujYCePUFFcANWITL8w16ee2V5UXoe5WCxVTLDU3euePt2bZKO4PpAxzJ8F1MooZDuGSPByf6CbemCoHwccWjDfCzo8_2WBpDkXjgvhXAkyeWNeqcs3803SR7o_INNKnYARTsMYU6KJ5K03c73qKZoSOZ3PUrRC_q1uPeA18k8N70watR3_qOk2Yo2B7CCxp8pAcrVMrmpHuGNu7a1AVJi0Ws-PWaaCPjPXccXoYv9HngbqUimXaPrBrzVfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sV0AKKazm_MnJ6MsKR32Kth9opBbUYlsEWpKpKUI-Z3sHNEAKbJV7ylSHSEdVdqfZdH0P7LBESzpdwwk_DAV2FPGChg6qU_yOpQ3jmBOLQgm8_Ryr7YcrieCTKWtI04VqRiGQk7fVnrFv_b_sTRpybenCslKgNC8K8uo1oZ9xT6XPq0Vix39CvLNaVEDbZyhcLmqxhrNb_eQhtzpKeBBbdMScEG_SAceP4Bi2aY1bEbszaUi5Fqd0LOMY394hGj34qME8TioMoLkJRCZNq_1rTp_ux_vTmYqnsdzEPk01McKZOJHjqqXI0c4Hs3TOXjoBEgtg5yDea79gvcNZ-TZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-aBSOxrBDhg1gZy3Yg8F-Fu4_QhFliKs2QXGEoc7uQquvkRapMn7lukgWodvLZBDRTzQHRC_FZEEeg1EMwUQuFiHc6NmpiYb5rsY03DrCTNz7Nkd2feqeOKfxHHPpG2TQxxwrHkF1y_wYTIe1aU4V7Zi-lmFk5UbGR0m_cI5h5zne6DcSNXyc1mnjonQsHBVrAcKYV0yo1owHPSBIuFM4girDJKqnwjCHt0UshoMBLLHp42OYFgHV4tHfpiYmVKC6fuCRkPISdVXQ5KfK3W03kv8JJexz_wR9GwCAxBlqeGOJw5xFDfRZnjFweedyPGq0WKLTTO4eCwQhIsKGKWuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X58De0Da4bGKs15zf2ymM9mwzvir92MFPNCvWFhxjwW7SKEfbllmzjurR8Ygz3wBGto4WbVrFPwjmObvyxXik40gwqrv2pDFnGPgVHgSrTZsh01guQ6PRwzYNyUbLakn0SI7DQuKDeTwayMtKcSRq4w2gm-odP37-rFQi8U3mSQ6PEhUZRBt9h6Z8gbcgthG-IASH2qOdqcf0zTrCpmHUxMj0COQ6gZPDbrsJeTu9uDIB_wRBlTtHFsg6t4XB4i8DsXgDkbmk7f80_blFn6iFpZM29Q4HYj81222ddZLPtU8CimnPrG6Cr4t3fMhQLAJbrX7nOYx7YhgUvSvhbbAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FTg-mG8gk6if_mwpjbiB3Xw3XhSJ-i0dCp59pOfZCHTxehHrQI7RdUTY32opZt_bvoK_ydl3vV-sIm7g3Ke8dUOwHfgnd0-65iC6bKbiN43hT41Sy89lZiPvsj-wo4gmFiBlGXKwzktGPtHA5VaKa2MoLa4DqEG_OASQEoy-NPG-VS92g2PYatjrtVyOd_0Q7C-Tg6O24RQF86T8v4C1Aaldr5aY02BL8zUIQHFDaPtPFbWKv6sdRrK58W4wmLrmsavPeLY8srUefg_3zqQXC0FOVsD988TPkX6AfHInYC2C41TXBjOOAKa5sOG4Z_0Tk4yefPrgEl6puX_wfQzzoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nWYli0bi4WGNf_jzFalwJVD6wcIrE6G1cFpqtAu-zlfwsgbD8n_tCdKa4s9aU4Vui0sOkshYPCYDTbOb566kmKP7m8Qm_ng_pfRC7UB8asykLp6P1jGxj6m61CZ12QZO5Q7RrQGAFQiJmHfK23qgtkBhqDOiLIjHde7dvbD44YiKoR_20kGZEA-7mdoMmK-JoxcC5D2kOCfm19ALxv8uvNttWeOeUEhrbS-1SGq-bmQy12-33ReGr-gCbaxCl6XOVmOvA_l4wFsNJ0Xdwq53OBKtBropZ0GbY-L4_j5UW1knaHPAwo5jPa07QQxTyVIuwf5ASrINHDJikyaHp4Rv5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P0pL9EcDevG5MdhMzNezzChQp182IH84qoGjLpChY1IIY0N8bV2ALgy45hXlrUMHICwoVAD_Z8gpBiBfI9Qice4Qas_N2pyQurDZsPhiAiZXeju1eUO7S37Gh9kJEGHUBofXH0YCYdnpfgvyNkvXfQOdHyrKe2oa8rq7oYs1FDloNDzLm2fezyDQ0V0URXkk4LuBwX1B4T-0mZNwCprYU-YTI4v0xgPUZfaJXlvvWNfxTbJqbg91V5qs8-ajmR0McPeXLoG7d9__pPUkB7DWZwA32ORgydE07SqwrII0xhtKvX6eKoSHzyi5fw-IAccx-hGQ5Qw7Fh5ZOyz7ZI8A1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0XtIuSHfrDDDSHzqHPdaJidML6BE1UN4HICK_mU55ZhRno2PtPb5gUMH3a58beX7xeJjlSMGu4bYMq-hj3NtLAO7UVVfObVFkp5dDk_qPL7pybUSs_qYiSe_vhySAdbmVE_9FTXic_LcsKzk_hS0I-Nkc4UjJQJhPMAwwF61HboeRfNbz60Y1LQONC8xSHc-T-J8238gmP1J4zV-3kPr1TFJvyCcktrcYx2SQjb9sd53MPSjwhGKDc4TD0FT0FX9aw5tfj7AmtL62g74Lj-X1i8-9EPprGvOEa05FO8fG7Y3zPkef2eYqqoEk-tR1E6wbRM8xRa_zRMVtiW_qmv1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKtbD6RCB8vOFNPKBZbYLAshmGabxsEFYN3XKW_HTv9Wmjyq9grR8F3MrlaSWBuCNuUrvKS1h9RLUXwjGCKUbffe1NS1aauuGElX8xUEPNrYCF95lXZJyAlrhTtlhLZO5p3s8bMI-D6aEmOULDiHSuv1uVrTFtUydFa2qR1iXSUVJW1Ovs1oZ-caA6nUSMskp9upzKoxVGhJrf4cLTTn3TYFlbcd69s89R5YlB8__oR2qVGE252B-a3PzIRZg0OGv6sEtA8qmlGtcmpKFfxvVwCcOTLTXlhDGzz964s53o-QxnpASYQGvy6aQNgmQz2YGcdmJACbN4gzf5BdO1UFNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY2-7lwEgcNUf5rCmKHFIX6zMBJKnow_Zo4vsg5oLssltPCZPhq1tBXotGcDcYbbhioAt6GBU3E4csCRxooBqRpVMU39d0PV3o7z3PiKcfxC8ejOVdlCofO1WFn9T_pWhFGa3wLbz4nFTdDKUsM4wH-L8i_x4huQPsiIbdGjBswFcgkPaP8o4s3A9iuXYkYuxiRhHptj6tvLlCHszRLkRLZ6JXB3yGGGc7oMx92T4np7soh_VlhNEcAwOhEcHrAbig-PNS2tkM9qFcZBFzwXSL5UNFWYrCgwmcWk7vH3PzfMy7ZaGGE89VmM1aTgGhDulvLL64uRXbHqjc0YuDkh0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTwnZF-bsAq2QVxVxY8KKhUSo5NoAzc_zQ4wU3spyQ-VfH_YUsf_MTV3b6CeIRLLg16gq_SJwjX-YC_EJ6MKI4UhIZFeZZm56-T5-Qo1QFGHHqM9GAaM6JUVAAZMt6xvF3htEcKiKubC5O7Jtndk_KskwzwcsnRSCM1XS8lwuA-10tQ1LjwnSCHkA31JhDxgfxWNaLPlpvKWLpGzzuXbaTf-jg_J2eTse3aV9b6NqBNmJFsw7HVZG_MRu9OSyakTw83rnUAdo44IiTc71YxrxdrzHgi0t73JOJBoBVQK23N-lXflMOTd2831tJ-0JBdaKIQrwS70QsBKni5pjhx-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OlKD6AmImB6jiPcJtHSgRVLsqpAQyWyPxEp5w_TSdwVqeZnH88SbYVw5PbXIOSu18c9wRF0itQUFr7E4MuOAB1K2syPYlaPudSWAa5cBz--LM3kWsExhNUGpEO2UIVJ40kyxi9TzozMeKFTEGHjvmXUjeWDM0QM-5dR7K1doDmiaFWKITIjGrSC42w8wOeZQz-AOBNGdgyPBLrSBU7ZqNHOnbxkdONm2lVrAtfapy-xI-vurBVnE1F8saMLMMSQdtsJrUuY8vruIxA1WJ2waWYfiFA_mnGMRWaXoL6BeyHUAhFL57nz7GJV1WJeJWZQjCFFq7Mh72ThJaWw0VqfXTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj8pqIKtnPcz7pGTGevvJ6ZemRIoUW5hCyd6CXAEZO5VpP2MTF5o7Sg4neVOs-XCq0KYh6AZh70ulLOEMJgKCcE64Q5eqpJUpzxqlxC0nqyQZEGgikpY5nqZPYvynj5oLcv0fhkwqNPv6buBLritG444PRWrZk8txWGQR2VMOwYzWGVA499SCsnHfvN1qifcCXBNJUesUQRVL0HuxfL28Uczk0oTA-8TYmHdG1FbN8D2GQMCnR1OaTA4zQJGAEphILG64NMfapPRloUL597UhIdIopnhhN7Ooegce1S1fWuNdYqYkw7nyg7YYzfVrWX93OGtYEC64Zoz47O2XBEUAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFCf5GSLwDxEA8fKAjz0gAVzMUW1LTD-yAUC3aTT46sB3lPhJwnTa-HOH4Egh0JgHPECeAM38Wb8tqoNGLknapR-43yyLTnlCzjgs2lRp_LH4fFCJw9kxpkV-EGa2X8A8bQFrmxJZUOu28puykK1JbyhkseM8YQHhiF-DqtunPbUCoURYlxJ-OdX_yGf7mkp3CgQY2_hQ7wYyWra53Yk_gmN7Z284JfS52aIo31fNxeM4D8l3dhlvJ6HadnMxFH1uhOYJ4Lcf61nY95zbBYYXPAnU33_arzrytpn9ZHuYEr1-HZVsYutmzJxTR5o8ZWRhOHyI1pHNhvvPIMBvJyRyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHDABU2nabWxAlHeF-N-S8hWvNbOnKRPgI62QYP0jwC8Fy1fsQR79kMLwXZugTNLteZQ7XD73MmXnI8KiFmOBp76I4JoQoEqPtP3b5zWYkAFkkH5utwkb1xJaLvcsedfnpGSJ6OocX0KGYGkFLfNQdBjkSMf4eiSQx3zw3LPhFCVzbxCu7khsPA2W03eVeHOqwDs6wzoAzX-VWYiEwONAl7HwXR4hqISF3DuDKRj9iarWZi8zC-Byq4kUGno5dcpqwOWduVw6zIt6p5BVQE8py519rmVNWpjCg3NRZa6GLaJunAurTipiOXWnDRfCn2FXaD2Kax2mB1GUaXw2u3j3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG6OQVUxTTKG43OA3etcGmHZSBrksO4WsAib7P8cEEDgAMlKvS-2Zs4SsHSG26Uf9RAlZ0mbk4nipNyRZ3sQzEvL15ug423hkgl489paIAuuz6I5m_uUtyt_ej4T9l0uVcde2UIkxCUPOEpZ5vtgqGzIhznp-En1u_p-sjhXXUqw3DqvnH_G2aZtW5R1Mfph-OrFLAVhQO6G3WKB71GNZn-rNoNUIXqgxkPkeDaAwW7kpggdltul_5x4IPjIKpt4Vz42zSE96FMS0Me-VLWRoHNmX-P46Fqr57UIKLyF3-5f4OHENX7MlnPOZipm5CYlRWfk54F92fGdKfgqJ6jGoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZActchfynluXJ_4Lq0wROZ7ufOEOqilgimlaWr0snf2gy_5M-MABwNxddG5YfyGwMeoqLH2R7NMDyZrUcd9SyTap0-jAhkQdHJ0aqwLeRIFQpU7j1o4nR6niSuzynI5vjA0V1_5_g5fjd2cMdfSzYg3-Qv1LIpb-Hqa2K8EdZthE9-X7giTrnl_OkzHiU7JSwkIiMuHAQyoj6gqWZbYNWQNEgfIxDyxXPVbRh-BQHKmwPjQQ3vs0BK6B_8sCqevBSplhFhWkiRTrtLp_YxufJu2Vt5dC8D6lyajIADWYBFkGiZsPgYTpgnzfEY_prz3zejrYrs1RA4Yi90sw-ZTqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TpkqO-cIa9WJFx8S40c7RdTP6fbbnlHe5OYwcrDV_VL0jKBOpf7U9Sjsj91L7U8zL9bkx2EQtpF1NTRfbXMz6QxS37a9qDk0hQ4Hq082UJm4COAlcA0j2grcSVdaeslqqpPxF22hwdSXheDbivNfe0MUdeP_flMLwtdk6QYzrsktHnLUStQsQlwroIz_2Tw1D6Qu1pvN8FXMDtRTBEP5hMpZZiKTr4Fc1KEQlKBPEGaXyykrIecJ-vxDVr4tDaJcjexeZwd3-FPGnclL6__kXyaW2yo5fwK66JiMM0v6AReDmQvDx3u1x4ItXmmtuP4vN4cnZPa0qSqC9s6yb_4m1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pCtFwWHcaCJ7ckD7vjfqrGHkJ8ZJLlovVxmSgjIpa-sGsJYFoqXLShMfph2NeA-O47nxkxpbNArrMVwMS7ucNndiClIrQfBs_I-PAlJcQmvV83PfDqn6GREvsRJ4k-E-8k0s2j5d2Utk5LWfGOM3EtikG0i5jPPXV7Arp1Nn1FmTVekQFDQmgbsbSzDDgxmL05_MJrZzC0P9yw6Kivl1Jraf_gTS0MvhSBu3zANd-sfJdR-aJmw7T9B6j5PMymzxYXzrD05tJ6hSojwDvwJQKIQR9Bw6YoLcrpPPfcsieghcdReK9yUIT6KCBSuPwfUg047sGiyINb69KOv2GYiLaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVV7qsqEg5AkaU1gosnQnAnX3DCBFeZp-wnDYycxrVAMkMDegSLIMXs0BqcER7QQVj1QZF_T-niFJkXjRwXoVhu_6NfT1xAV10rENaAn08LanhDZYDS8e-5vE2z-hHd_1sNMORsukBtBVCNW-dVEpDEvm4lhtXwRoxPH7Vlz8rA6utFxgZzjqR5ILXw7tc2V6FSENz7hsIVWDrYt5yK_o3JcXZytpOIe_gWJCY4TFRkirFbhln6GGhlwHdwciIs2iH5ludlngn1zuKDEOMGUnTuqj2UaxMW--Wkit7C7g6Uk81grA3co03EoFFzDjwFLqnULiJ0oz2Sn2d8N7BqZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3zmYSxRdjJeh0vApzX_TNXXLmr5BTAvZ5Dk41Vap_H1JXqIBilvAQcPNOLTBbPn_IjBnke6ldcEPVcanUu9PIzy8tuHs5d8e4b-EfiRrEoDT0sYSmDIxNc-2R8aHQWmwHfyzuCEzgMIUxcuNi5m2eh5JzqPu3V7HcX59NvMtFa_rIvwBCF6_gMzB1cJ-UxKUuNMDFJtTxKRijKxjuAL_WSxfFgs_x-pP3wq0KTcEWktYRBAh9yRGwpA-7ZQzw-UBStacVupnFF0amHoXdrY157hoZoZFIhRdHaP-GK_IS_wzBfUek785VQyTxdgAW7ggQh4Pd4dsyUHwqCy0GWU9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln_321ZilU4lNnrrXmgFJ6Xzxe4MKI_k1V4A01HAkKqHFhIJmJ1-jyE037k4nzXb4_XzwOqB9GwtMoC5yH9fiByNCiNP57-eYDeD7_S4WEmbEbAhIszPVZQLIlh6whkMGnsUJ93ShzKSPygjdk65AwwZFqfBGuRThLA-LshdXXiNauFjkZiOcH9cKn7uWcHYwLiRv-nZM7vnQ5AhLGNSLde-Vk4c6e8l7LcQSpsfljI0cSUFyGWOunGdoixzH0Mv8Bk58NVNmsf18Lc9gkvR7UpngQWbQzaegqXVNTuT6Z_jQFH9ccSxPLzmf35e0j8fZQSyjS4t9oUVX22ayUHtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qktkw8jXuRXqDHiEDFQgVEGxy3MutqeXCpcmBdm0vxnD9a5X3XtB40ZYrC_fIEO5zga-GOQZi6ZDPaYhQblU_DpTALayWuiquN9oKqc9RfmUPxlOtbySyJpIoz-GmFq8ckEbkJFoC36GTfJf_rOHCdYrds1K2F6K7XC4a3FA-QY4yLNp0fr_gqCYLTRZ1qrF-Eh-rfezXuaW6YyKzxsC1cDvqTdoWSJlBSTFIfFMbdSInWxDSHpAXSp0SVcIPkYPhiFV0Rete9TxBjrTZzBQyqwRMoePg5BgccKYfayDQk61m2ULaRGVTkqUeCoVXzyUutRBeBm12muZST9BsucFPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0djTPCh1FrtOvCmhzBZUw2T9W9tTEekbFkBZuyaHM6iQ0p5SA2esJ_eUeVJwDfX864ZVxFoey132D1NQyGTDNx-FDPOggF-BMhtwteinQRmOJuqPpAL5f8nHzVuvu-Oj5Pgd1Vqx36PkTQ1C8gd6Oj5yHiV8NrzmWYtfKnHV2jp5XyJ8gXeZioFtsfB6iOF0kwhvh4V73m9g9H0zubuVxThgPn-2TJLA996K5ud4UKWBoSkF4YzlMpwfX7YUue8KvlPabRPLbkTIafo1Hdms94grAUjDdx2gSZGKlpwixWvtbx99EqhYWkCUk0qj87D_g349fFJv8hfiglPkOX2AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVDnm-I-FlrJ6RZxawhL3kmbY-Gt5YZmoxsZHs_W3HsuARcC0cHIv19fyIYjnY_d69AS0A9_-Ez2QYfzFC6BP2DtCkdw2ZBS6cavv2iZquLVP0EWcvBKcFZCJ2NFbqAvaHChPQernb8AdpRAZqmuNAuX4cRdpUP4fNzc93fyfyNHFzHUBV-56nHvXdqqoTHFBy9tTEFZrenS0H0-wp2kflkJtaVL7VS_59QlywJhjzjgH6qOn2ehAUpDbJUAXE5wNUUtIXuxVuJ_8BxDmIWsemScbpC0wYj4RJrXHoJXJJ-HlhRcNHP2QLQ5sH1WUDjmLA6u_7iOnCD7vjjtGAMUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6N7g_riTCPHAIjmi1QrfLDknMSv4PEHI8QQVnE0PJt4hvo4jPwzZYvq7MhTjsIFJIKFnX3PYUoOysQWctZk7gaTEi_7WUU29684bXJpnFi_6Gk9xqIt2MJ37WPxH5GZLdlOrrQeSPO71zLTNH-ffvrxf2Ufnj3D6WqQk5DqUsxNABMhJc4GSSoFa3pvhbRF79VhoXguXn-Zxw50idC4X9mLMvCIoNnxoFyNclA1X3yQPQx2TWhoWyGJiy2KszxIUYW7HTZ0OrRSbetggaSC7-AGjzAAZfT_ONCAqNTx0oP2jBPkJR8N2eBonX43_NTOCulr2YELCg14wGP3Hak9Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/invTwBco8nyBKVfIfE8DRz0EI811-5pPMkWkwL__n3DyA3bv9gPhVWlQDovfzeVgCUITkjT3XSL-jHtLIHU0pBS-IZ-mV-_ladF8KyYmk6aZ-LzsywEXEnO_nPvqbMPNBHoIeBHg1_0wUjOdgBXzi2d9Y0eIOb4fFPfgtno1O4P3x0rdqfjn3s50s6eYyjh3Sg4Kpkd3uf6jYIxWdkQkfYHXIYkQjycyru7aH3qnBW1KEzrULXxvYF-KKIJk56F04S9rY9GB3ltOp6zfqwISeOWKjDNOtHmTFKKhnxv9zdlZT0RXvKGYZajOaQZC4m0Q8fSZerywCMDM02NrHMs0Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAPrlNGbUheGtJn2dMBhLNf82L16TC4BU-07Oj0hzH0TtKMX69yjnVarJ2MhwfJuMp_ppOq5bMgrEpiHwRDADQfwV78tFPb0bzKUz4axcV6PuMae2Wyx8kDwyHKHLGngcqC-3Hi6QgRObZ2vTAuxcL0cLuNsIk1I3AVBKiQ9-gsQur0eJyxeusuAyv5qsLkwLWJf2eaTGNgs-o471_7tmB5JfPTLMFonsv2im4g8oyi4iJPr4N7JywxCdcEgqXlMweI_4OCVlJtwtNIQ3JvLjBpKrkMwYIm8ZsaKUBYTsUdGIrk6miMXLC9hVCbMBHTSWP-yRhAkJbshoSIHO_bMrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZsH1hhKyT8Ab0Jx_oEyNFpPzW5Q3S78GjdoACFYEOPbaZcZkSvFvSNM72jpQLHVmV_6UmexumfopOwNFWvGIEgOEoRnqOK-Sq1DT4OCy29zwwxnYOlZ_qUcj1nZW7oPoH_t3ay_7UDb6Eo9slel2sLIQkjPzt6thA0zNpDj4bZIOQgRcNaJN8YxaC2LnWkwyoIOrQpW_HVc_mfWXxe8j41Ho9_pijgJEhSTqkdIEoOz8jKDhl5kcnXE-aqpc94tCjylUFnbOMlMbBUmjomFJ6lQAW7tcDqu9nB1JTXFn7QW28hEytFhgzMPE3SGo6ZMO7aFa3rz_g7STMt_804XuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqihT0AX8Aio-GI7M8IP2f0fhpu52WA44RIfTXIC1pAtXNQTwDjMFCeJgdoIsG71NMGZtEg_sHkJA4ao_bWWhj1Np0U3sPEITxemEKOh-jLLti6qKQdP0Kkvv-Py3SPuSj3rpR_a4gPkRLM65KgUkpSV8oH_hU-iKDZaGZpEqvnTzrcHKKYglgLtM5xwNCXJ1B0JH_zRUuwkdsdwPQiJWGlOpmxhDpCbT7l8aGZn_XVWkxAre1yI-8EF6V1iqpUlu9X1dofYSO0F8C6DzTwq3RUGhEd9Q4ojWA6_zG_89pLnAfBVeB92gn8ngzbB00HaJ16T89sVq19TSyQ-xXPsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8wZhxBsHG-YwEyjS0XfWYRfnY2YXPzoobB-rqxoK_2hyLRdhCOhFhCEZckOaQYO6PdViGrqnYrGWmKe2NTdpP73apZwLgktnS7GjdqC69oVs04tADg6zy_S07zQT07KXjgUnvD-7koL_OudDq68rAoMwwkUIaTkyOeD2CZDv0fAXss-3vmzroc3lCFrg7nq4M00GjJqOMFgSRRqM4EYASPN8XwvpT-7w_2Bp5c8Zrn9fB0SIUM9-W4ngzlcjR7UIfiz10mOm9sQ3xFb6QMCxq-NBP8wVDCpowpIYQbTfvoqplTMBam9uZCiwchD5YbNy9OFrvBHr4sa9MVzg0gN_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0gxSnB1IN-P7nHDaOFP-XHXvg9fUV0pJbrsnuZ8gtvII_Scd0Dy5ZNKVUCzsbEsyMhxttT1fe8gKwL4IwsOnITZ5iXzdp1qEL_gYoXeSb82Mya8g5xC4-HLEijyzzn-vCxeeWHBh_knQaw0ZE8zamkKxJ2MYJcdnTTwsKFXgepLmLonW11fBIybwasbfFElMRcMPdDg5-PkB9ojDbSCjfXwuVX5HWCJC6mBh9WcbosnUGrrVzb_REck_znfMfTJ7l7HtQypFAAGIaUSNM59x2ug0OYF8U0FOwXKJ_MK4FV7APtEMf43bac9mrpSa-UvoX4i8gBQvKX3vwiqcS9PLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGUuPyjap4aGyprHFKEl1TEjYFpcXjZVl9_Ajgp_Y6WBiJxld-D1kL7xZOnbnqsJjDJdQs4MDSxO_QY9zZB7v5ioYwqpPAuB71SrViDncM1HVpBckvXNmXCggtV0vtq9q7yjuGamKl9b_15uy9bLfktdVkj4Xlc74QAQ_tso1mKfUhxcq0uZktjmAr6PX2ALjFKWagR_pmNGrlASJaKBLnIW1qLMDwdhRPKurH-EA65yaX8sSSbCbEcAPBulPwFIIVnzuu2qstbWwl6YyIdg8sJOBxwfPDmQ3ELOlYKWvdrSNmPOo1NTc5V_uJ_ZfAu9BdCrg4f61P1HkEaQFoDGVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d6qxtifOFBbkdkhBvGxmlC6Lwy31jGUZ9KHoNeafGkeQIEW5SYmH_MSyf2nRoMrUNKF_5_v3Q3u0j9dpdkoZpr-LUQnQZkILyXSIF_v6Bv0MjBypzlGdML56hMs02NOEAlB1PvgVk45_QF7pDoO0bUkps7QIBec9bqvaUfF6xEA7rqrdfowMUSACwdX7_Ym07a3Yhc2IFh_Z9bvUQUMAtVVJpAamelm953_IbZ3BhuiJpqWKk3YVU-kNKgd8lPrlyLf8-qGPWLBxKFVTsdvSsDaUInd9zCIPQwHuDQQ_MxYXyG6iq34ynSxZ16RQtuy-EsBdP_TlA2F93kuglQ97Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQUyviPSsc1mcWRH9s0zxbq7t9YQ9j88mFJwETYWmI-t6D4e4JGtZtODNQQCKPtKfSN3zsByKEDG3eUersUCGe-b0KVaRxRvgEkuYF1fk3ESGL8Ckn9wyLb850DDW5KzqSbQnD5vD4EV2xZqdKNOB_9-ra-afMuZN9ddTVemc4o1SmvoYd4I08dUgY_HXwCbQJHDmBF4gWpakA4Ct9I0uIjWF9d5oAu_gAFp6cr25x1mn_X1wD8734U146SEbKWUXthio7F8fBjcEz-ujiDjXZmHkT0-waecC4dFu0_c3mZU-l3X0KirmEcL6BTWkpy8BIRg4RpZbF_fYQ_ddskZYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbjofwwWEzaf2MaGrzum0AdcE-VMZD4mLxqf6tGlK6uwfR4PIooc-By3rhpC7RqKB-AzS4oNk8W1EXv4SmhPi7s8amg91KaGmYrDv1erastuFrbOAfvNpSCMgB98IekUjHZhS-bu1bynV0K20y_SNWTuWtZkEmWnJD2Dw-8ztpVBHgveP5GE5-gxcKWd5So0z4pbF99xG8-QfBLPq2GC4OBpZdPcqJrf-OYOyyCLXgwzco0cDhefpWJ8lXlj0DArb36vfZDg88gtVjRchwzH8K_AgAH79PSVIzZL35Q4CDB8Y9YWCQqFbAORXaO5mq97q-c8WH8sq39ASGV9MzMfiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEaNEj3UL4B_Z7OcaLufJOp_hgRIdNIdDVGMqA5WZN5b95DwH_NGodmU3zRj6z8CchFS9QinG5k4Tmna2Es6q1PaD-hToFRIMxxr_v3dBX93uqosoM7OINw-m6EeGh_4KqU-mr8k6q33_j-WmMkQq-x1qhrNm8ytNj0AdJUX9fKC5rg8wqtQZ5KjBzNneuNkt8pZYzIjNOOvuP2Y-QuuavSzhcpCXM8Z3f4fTbaA8wzxNQgEFxG9VgjMMjEYVXqWiY0LpwO-ghfMdED8NeL456W8QKBZ0U-M83gc5TnyC9KKM2D-4VCcrOzm2_aJdCzEPP_sGJF62XaVX2LyxYKZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3aI5b0y_uqM6k8PZ0v3Uai0kAekU4tGrfWhKonpCidjn8edXKruM7HxhUZnCGmjjRF29vaciqfAuDjInBgjILom-O0RQ4iEgl0FCy9gWGsX7DfYg0gq7rWqCPxxn9IqorIG2reCWZ5C2g8So8OmK3RJaRln6c3No9nLOVkwiIx5rLbrbdi3csYmInJw_oxxb3Gjk-idoZV-Y6n9-UY7fD-vjFDgpV4Q-JaNjt3Zi_U_rBuontU0xFWS3qrDK66iD14k03cE94JRBYKrkVUUeQkO69Tt2h7gTzHCPWbUPIwbcktzMoK-S9uct6bqRSfy_vOxpWnHaRKYCYWEb_QjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXgSecXEqI-XIGtnVoYIKXlfn6BM0sRZOwwBm6B_zuhDOAWM0J9uGaN7innr0SUajhgcHKXQQogKZSuU0ibSqNb4cP-xJjGo34lQiz7GIJeQmqp9NQevcam-CQ_CTKFjqYssYb-23yyut_DxnDwdjS1a9HhotHSrNrJ1w0--OCfoErEzmYo2sSDkmyM9kQsl7oaWusyQIzCLRBFSbuRgaIGrg4koj4JT0Pxal7pZVXmCLaD_EAHtWEz4STR7mMTwM3EbxFFVOWDvFNKHqMGZDXOUkwLN4Ipc03K7ao5Wr3H9M7i1P_h9-GdMzD0Fzb4HZq6GcZay4TiAuLbgmKXkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-GpT6jyGx063Y-fC5uHioHCZ5f04cgx3Ok9YnlK-vATTCeqp5EIJQgHNBShW1ArEQfRwmPhGSKICAyxfQaxOnsO2jq7FSc2_onAlwpy0xh59QXOasqN5Yqa9IMeE4n9aj2OdTYJEWGi5kKCZ8hThuyGPVAdsUYBMZX-3y0d2AkLhdYW8wJ37JQdORfGcNhjFO80fNDBdxSCnjGtNCJTXMoI7jskuCnWWO2W4E9_GeuNjQIdfnfMyCiFNDu8zt3bbzig4RGuNk1h2mciqJ4ZSxUYvvHgzWG4XNyOVxoqnnQ1new3zK_arOfewE8WYGJ8P1xWWrpTZaolVwJt29TNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLZfq-0Gq0dmXbx-UGEGwtvvGshS6VQa87N1ToXyCapsYf-43_8qK-RfZWQ2IUOgpJWd9vzbYIWjyqc1of3IKbNUpX0vW042PRoZnmgTYCa6sEElUleF6akvEKOKfHm99vNALyT3hvPHj16XETDQfO5KlAOxZtodwrMsKnByIt4dABQSRTLbaPCSz6O83-jxiYo1xicfzI8AfmEa1Uu1fAy6-cW3oOArTODLWpBDrA3REOLQcDcvQATRjoEuoAt7Buyarn6yoboYptFOsWp3bVT7weG-hH5iKl2sHiwWZ-fq6KgydvAVw2Tw5MkTzUHlpvLcWCE1_w-Em0TuKmUhBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8f7KMldnVpXOOBpMVWX9Y1MPUB8MGAjvsvcZ0W3oeHkRYbByWcPHRuuRlmzpMXz6pAAWrpp5mfGSvNwzsJRdlXO3PVcmYqcl-C8U2u_KmnP4oxsDbi5Wwneq7v9Yk3AM2gKESxgqrZtiKUenM4Xh4O-uGfpBeyTOvzopRFZmbWZOsQakzjOmaA9DMeb29_hWkR6zPcoyxT_VUVsocZJ32Wn5F5JlD9N-DJHqUVjQQBhzTbtSyQ2QofAnhJP9-Rla5y1zT-Gs8m2wcWLI2X43jNYh0M_d7xo5I4HY5zuQElat6KZStSYgjC4qoWu8nu1m9vVSdmdpKcBTwZNZx3iQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTqDMyTY459n8sELAnY-wblCE9eO8mzhYVNUI395QmHNuCLRxNLINS5x4BcWzD9SPdZ4JFN2p81KSw84EPoQkWWtYQH6-RgQtXMgndabSWKznp7BjI4-nPF7sLO5NlYCa2SNFT452Ya6JMjfy3IBGQAR2_0zd0mY9ehm_Rw6SZTNsFGDQ0gGrcxVbu7kt0x4E09JAJxNYqc3_5FLDeMfTFAj1uvQUn1qTXPrJnkU9ldYRbx_RwHthrEr7wrNqz7VIkIzkl3206O6Fji5UfBFul6o1ojyOcywtx2f2RBBr4erFXy8BkYUg_GJXoEzl6BNN6t7gkafX3yOvsNc2ORJww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB9Ld_3u5OLHXzBzzC9721Bs-CFSOLRm432Zs0cakPnIYxCcskW6k7MblWOGLNcUlmKYHhy3Zx1efxmB1aqu3wSevX9GNu2U7fqSsZH33hZQc9qGV66ITGc_h05DolSba4gaHygZzvhJb0kPUrXSzqtQuv5QZZYWewuj4Wz_uPY1z6WMfVFXkyr_qorgmsp2k0GsTMjiVE1zuF41vMFP3jh_bw03w1ApgRrDphalKgpubn_E3eqJQaxiqNNisM2Gxi7QEK8uZYov8CViD430EWayuPplZ1eIPc0cBccCNM6ZotpKaARiR3wvdjhiOdf4E8JYw2CGBQYziUWfrp6vZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR9jVpv2MyXTP-nC-vwMlhit5v0MN-Th23RGuOU0K_1Qb5CEO6JFIdMqgBBIkJ2bK3fyJ6cx-ZXDuwTl42zJCrHp6ttB5pjnP_eNtOd0ZV_3QCSqBxvUk9KnPn6O8AuriTOvmyj4SwMMu2FVV64VXdnx0p16BBIOLJcH-1csxOFFbwRWp5Orn-EJBPdhBdUBS-Tr9QkjA8ErVyNQW-0H6F6EvzT7EmtMbfqce4ONTJXemUvlwQDIyPgDO0Xp7O5QXFU-Z2auUbEkj3X1OhQuU-Sp2-b5E7Dpdl8fry8ic3ntQ33DM7Qn8XQXWKYs9YPe9QICbaHTWF21vDEWQ9GRzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDyfqC2y6Wz24DzVfwCYUZ1a7RKSczE4Y3w6p7M4xoWX_ZtUsOtVIAXTBKpWxFCRddU7O_7YDSu-lNw7U9FOxwj6tZJfYob-xL6kjGK_xmRcIfq0poaBe16s0-EgXiJS0O-doTEjfE3yIqhviy0cxDyp8zJf9m-36g9BFIoHnfDl5frTr_cxFjH8hQq-MRsIA8Wiwtbx-P-9H2nUZ2EMxe2jWQT4CBpPXPbtOEtvUGpbUGToJ9D_-7kruoZQ83MiUF2vtXGWkHP0WP3qodskDKBAYR7mJK2-uq4qiMDJDOJIH4aZ7FKo0YiB8pdWYqpnuDJkElpbkwELketzmjyPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsadYOoyDfcgqgFQV00Gx0Dqo38UPx0LW9O3-Es3Ou457zNM58_BCNjuT8xYbS07v-lZKdJvnc8X_kWrvQEXn3AWX0u2QNhC9gp32JluZWsfmrheAcIIKbgFGdDwg0c7Ehr7WoZLJPXpObQobamVOdMv21M4ny_96BYSS3xlaYeWabYKb97l2cF5-BeP-6sMiJ5i67QNYJexkck-Ej0Sm-sJfaTicY6QY0N9IQ6c45lnTLX4O2oHTcOgT15CtJHqdoRb6FIQvQ-5cM7qgqhq2YjY5wHoc2I6YXsRTJMAwTPN4cmvnW4jEoZJ5CXnnZmpgpi_HtQdKyJjfP_o3nLmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNa0v9ilGob_yWmI0aDRZIQlvuonwgOtS2x3E8SCYLuST8YkyN5j0OdLR30DrD9wQWj7hcCroPUe5UGxq9yKORwYvoRxQ-dIaZ3uEiTBSb1IefaOlKJ_8AFPb5K_Byx09b2lrnQsA9in7zp-NR6vlXfg9NEto9jYxAhL-f6pAlrNSYQRIhvPNYpivNeumdwBNt-Bp9PB6tSKGhCBskQKkkv-BUts2b3SS-Sb_fvZX_xk0VbN_XAjLb9l3CEsJqktcETlXdbbzXhBDzrW1SFwx0Lr7RYI_BpxlVpGELpYtjwqCSKZPv5O46GjTapA9ofCsvh68aojmh8ab95YCd7glQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Th2ZodWSmXikHbnMAeVZuoCIsVo2fz4DvahIEKeg8HdWCh7OA3EUuqU4BxjqPSRheI301qKO0r5mYdMtZGKRPjfo_DtBL7xQRhBPQqd9Eg13vFdfWWsrqU427ef_5ja-YIL7u2I4JfoJ3R4ccxq6hoLl2e35N0YRyMPWuHl1whjKR3mA0OJMGrPIsv7RB_-JAF_cGwlZPIgYJwNXH7CezQUBIZxCcfxZygFVx04EVAKF4Gke5la7cIfA8VVQ24zCwZwWOJI0NQV1QTe-CBriynWGQ12Drqcvo7Zz9uD2ySyZ_oioXn4cV5J5cWjcCJ7Qx9yWSTUJ3HUtE6Ju_vVtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJl_GXfDDRVaY8RpyVq2MpniB_5QNoRTPx0GC-o9j-EB8p3TNC9zuFaUjV-RtDJyqdJIotBviz5xqDNExuw6kVCS-W0PsTUl4eY6TuuoiOUjoFlIcaXS12gH4dZNQXL-IZ03ekYb7I6l3FeLId_ypRVZ6IRwL0T8mXxg6FR6GDeRHiDc1Y8LA3R2LDfsjXreqFm3tuXo6p17oLpX1SZGCdr4JztB2B44mWIr6oN1sjpETmnY85BxD5KbWC0IljwPqgmWRvzO_ur2NWlxXxFY6obhKuK00LpLBbWWQmtTZDbfwfwKUCHMjjB7HN9pVhd2vmE05gcndkeMHpzfZAOfjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNbi2zkJCCnMLHDp0I5LB77biaOZaZmVZ-CqkPeVvyevtEspC7T6Uqt1nIjUwwNg9iYx_ssM1sbTXauWijrVDfE8SN3Rxeu19zaZXGDjuVYCqN5r6k-XuoqiCFiqAO9RAlpxae7kyfgjYZf6Sh8-R6NR92Tb9zDKHiH7vDjNoBoO0gOPQf94a35DoVLdr3enUKo4RX69i78UaKuc_1jf0TqWje-hgHBSrnhxFxFf1q9SQoUwNfjbknjJ6FBEcCaQcG9Ny55Semoj5Og3CJkU0NIkf_ZH_zvZruDUgqebXUzWOR47rq8m_5uR-YWPTUTK2Kb6db-rUiGLs3ZUONlYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maD42jM2vW14-aLNLuIEr77srWqeAArvyxxByRBjrLSlGHuDiliaNLx_cd-_UuxSaNEbTLnSbQhXkojNSxqSPMo3Dsgu7nvIfvrRE2YZnatChNNIrP-TF-87e7ILNsUISO7ZmVgDJ3K2m2ZCbbvlEtSQfxi0JAzljOUYOqHLGeS5oGlvU8oRyKRvzdMbSZCYjD4UFcOV_i7uY8qejchqqpY0CCMlkXiJTweUUdql5rRFlTi9tbPbxWd3cfrd4BdfyIXdXIF2f4N9LM5zWpv1SoRTFx116n9tzREpEdV_xA4KlGDQeoXpaKnsz9Y6de01NooZHCGcYWNj8hrQ0NZMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqvwQK-7d5Jv24eR0F82LW_uxT15faKU20DtTfix0huLJm7BYVELzVDqem00AcjfgLP9j-KeezmN6u2ZWRWVxVa55IfiAJqmZwPmlQA6vBYVdMfIYDG-8KFQDIGbLKr9spC9or3JqR5sQKafOa87vu_hBI_owh_9aqND0HDrjFTGO0vNOvNcFPKUq0WbldGfzRZomVKwHAw6-L9xfYXt4yqUem9gni-LgirGXlxnYJB8qDXY0EMi56FpIxM13-W2wUkNL4p7ME_Lih3KtIvjgTNjBuSTYXYTSlv--45DkZysU8YGveIZoAC2pP8StTQvKeAUmjk-59sWU-vqeuH8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNUJUaIloXyoGgpcRh_CI0CfH7fU1Y8desqg9SyQkpst2VKLZebdAfVg6MWcNOUwq4LOTX9VNUDVid9WQuhWdFspf909dZdAM24AIH0nuVgqzMYInfjcTbZpaHBuSDP7CdIs4GOEWYT2iKYFGA0Bn7gTJLKQfg9SIkeqFsSwJk8Xlv2Ke-lQLVM4dPTlUJ28kAKh029gqOUUrRiIbzpmol4-pu97Mbc8q3tPpOaUFtuC6TKUxdJt93tqozVciwV731mgYJIbQf-sPMtF01wru1HTyiYiRj-LuiqtgjQt9MDPReE0SGeGdxNHZ0BqpyrK9H2GBpvy16fCwU_HNX6NKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsp2gVG6qQROtZ7Rwt-FMqAYFEk1pyXQjhSkDanP6TyO-3Dcj17tlq1hpwNhzyVFbNGeQSSBdm2rYf3METEib8HjeJ_GGjqPHXRucvFt0TzoZ3W50jHOHWqg0VjB7raroCROUrFmBsCVmhotwd6TAdodN0j_X0_8HkNwbw_Ej8kmjzMTgKUk6kYX01hqE_lrZ9Catq4ZT6iwlLhBbzDr01uA1niZSwqoXNXiafd2SBO6HHfhNYXSFbCMm6qyBPfOVVIpBKq4w0mSXwQ3WLtDriXiNORvYbpl-ihbzgOZNvDQynP3Ul3CnyQlxaS28ISd7ExlzAnS9noxOTQ9dS1kTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax3O9YnkSQ5xFlgSq0Yz7hV13zUDkJ5CFlmvZYKV-fAOFe5gtB-T_2AU8_QBG9KQOH_1nMSX6SrAXwYhDUdYGr1HY8g7kQdULJDyV-eAsB7eYEN7kS7q0XvHszR55AVVxg0h0E4M_zvYBE_e9Y9LtP2Cxt2JqferwdhK7Fl1bDRUnbn3TGYXWs2jdw4O7oSbLSQYYN_LGD6EF6lgPFUlQ4SRtrZa9BGGeuZ2f7YuiDOl01h9pjc1rcnntQeYxTnbPuYNoKzS9upYdOLeNdWkmWKRG1RUixqD6BRkh6KQkR8Sl40DrWlv-aoOA0M0M5WtiSOaGWscAejL205ei4AE2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=QKZkBd7W2pY5C4bRr1GdI2SVC84uy1KRk2MTCNmc59p1SUKC_Lr3HhYy9o2BjQ_ovOJSRtt-kcYYHVXKNq9vqICKvY2y5-HiebH9jNHdyye87KpfraDynIdkHliCGzIwygyv_hh4ta4XthDlAQ3T6R8qAUfw3i5AAy6OEAdQQa4C-7IOmy19xSVO2X5_ApwVV9Vbqfox0vw4abjceN1yyTeNbpB3s1_wchciCuNKKrDZLyMS3R-Nggg7lW7PU_mA9LQZgNGVPrJc5Vb4qCzh_aJhUUxLFWRcUu9a1qUujwToFjUpwVgzfCqebA6aC-AF4fjFF8WXT5M6D0WnaYOemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=QKZkBd7W2pY5C4bRr1GdI2SVC84uy1KRk2MTCNmc59p1SUKC_Lr3HhYy9o2BjQ_ovOJSRtt-kcYYHVXKNq9vqICKvY2y5-HiebH9jNHdyye87KpfraDynIdkHliCGzIwygyv_hh4ta4XthDlAQ3T6R8qAUfw3i5AAy6OEAdQQa4C-7IOmy19xSVO2X5_ApwVV9Vbqfox0vw4abjceN1yyTeNbpB3s1_wchciCuNKKrDZLyMS3R-Nggg7lW7PU_mA9LQZgNGVPrJc5Vb4qCzh_aJhUUxLFWRcUu9a1qUujwToFjUpwVgzfCqebA6aC-AF4fjFF8WXT5M6D0WnaYOemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAG6FThTgXEasrg57rrJGUyMUCz-HNVycSAHORiddcNaU5tTnGm_WeAYQ3U8yIch3B9TZOZBRMO0UjEjErYW6UF-09O4LQZK9tYRWhoV6bwwsuN7WY5wXxLeEAkc3XlrMEOEb57fKfnI6AtQPFxinJF9Rs4y96Pjoywgw9cKQIuIKri0jawpbXdUWzSTbPrn5oBxiQFcdkPzbB1BXzSoouNyAdJI53WiBjjXL2XdsQQUX6Tc4pduCTkqHSuiE_9vicP2Gz6DtGBO21tWU4Chv_d4kFc9BXOebxjlE-QUU3AZJg2eEM3LV1vd1smv95u2uszMkP0g_zG6Zz66Tp1GkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0ZH62LM1iPfMdLlR8BhYc4WNqOO3Wr7Rb3XrOB9Dbg-rOcYM1wN158bMOkjAnPllPhAW2fDLMzWbipJ8tcp1ecYS9dDJ78wjzSYU3hELjXX3ib4Zv2jvupDZZ_HEaDBHm0uaWLozMiC5QxhqlR38lgu8ta78elMGT_gZqGwwpqPPntXjXU66BDsisW1XSQ4Fq4mbIMOy23QrmStdHXHxXGilClYiU9ZwUrRrKhg8T928ngQxZYjy4xBnzTQHpHVvMfHm9aNjx55zNnoZHtO3d7_ByqZ7WuM0VYJtJ3wPtCDgQZJAbqY8zTga8DrZyV64lWGLbCGWRAsAEIbMPCvuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4ePYbVL5bdQYR5ITumjY75_glLDe4YYikRFqmqOA1wR3UsugPM4WMuu2ZGLg-OTfcJkwYR84xs5lqkFS-sV1KOp7mi7Yn_gKJ9YfbGvkoyZyG23o0Jpgm1sXzDQrMjwK2xJ4Uly6-TqFG3vn2PgRi4DkmZ3jkmcZzQPb7kI4xiLFYSa-VSqMZkz4rK8RxrQ3d6PNkwys-MRfN6BnQmC8evy4OI9Ssgf921cPjVNeI9w9Ibw-2kpzMJp8IMD7mfywcl76O33faDg4zf4YgyCwxDJ3RDcsqm7fSQ2tmlAPsPrJMgE7cDYzmUjZBjZ3Zs-loqLANCv0JYpBtxnXl2pcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3oAQXmNzHjdG0jV_3Oo6LtXa9b2SpEMoy_0wIoYF60TgI-iuUFSr9Ms9RmhQKOFoicYIPiauqCaJWxXo_F-v69_V-9pwb_tEfTvXRIs4If_jm56J7HIzBUU35BPvsdWL1Bl0je1SiSi0Zgk-k8jn6IJnPXQWX1pUwuvLQEoSLcu20NOGB8-g6Ngt0UGc7LioBxUYbQG0gqTxDYOMy0b1wSi47kvmEXjjx7WhmB4WTWvmj0A7vSROpjqgdHPAxhAR5l2IS3s_tqCMBhKWz0_CBlalOiKvIHZ2sDmIRNWVzeSeFGqauSCvVRNt5IOh326pWXifD2opW2Wq814uPUNrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAb3iHNY-yMdVrCNZMIEINIveFCYJkvkThhkR-0y7wcfSM3UeJK0kviEpINQQP0jO_ubct1vwvZ-BnBXKI_KHlfCnn8GgshhKKTrnmfSNCbnuZWU-fG9ieSq6Oo5ozRmE2qX3ADstm-QVLof85bg8Sa9YDkdJ4ZfP3zuQrTvlqPoTRJk3xXmPc5kzvS9Q3ZdtgEpyYpb80Tsp2mE8YtbmOrTmbshb-nNjog7EkQDt5DE8mHkhuxLTK5LL4IgdhVxihqkHpMFRlP2wHqsKeDfwQ6zQw-ZGgacCajex_8rhkgYpuXWV7ONBH2C5PqnF6bYh9AvAJiU8bXYEbsbnLGPoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFneP55fO2yUGRDthvtxIg5NMKeYQnJCKuciF16QQ0MrhCdgZyxL35qkHKyUxQppfbVT7m8x4pUPW2_8LtyCvqd8eHK6xRdLmwcLZM8r0POKlLqE0P1i0PJIjG-fa1S54U2U1AqoHAe8QYEDIyeNtr19X2G3GNRZYVrz_twy_vbpfCmrSIGPv7TwNZnBUtsuWl_mpk6g4pMVySHTjZZJP4nWIsqUNY9DE6pjQU2Ihp6-1mphvLcKfORC65yIYRmDvMa4BNXWPPlDOwSqv0d1fjPEHfAa0Bl8vaECzu99D1p2CMzmMQwDZcvEtsa348f6Y1xg-6ZfQ5OM5pb_BQQAHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuWj1LHFa9b2vKKY9qc1zJ1aEmO3NKNQT4kJL9ciMzvShs2XeXtMN6QZe1IGF47382v-jB8YTCcSohW2N0Ffgh5BoM4BIu7AKO5v8drPzQSbsX4j9hpeZE-ZsSda2t4U6ejc3dFksLW4t3Cy9NtWghW1nswb7q01hJppDLBxrm6-Vy3AjVr-yQ9kv-rhgga20WO56-eeA_M7dU45u4vxFkrgmxtZpmrxZrpLyj2rZVSbsKYZBG7xW4kh1KAdrFpBjwLo9W_vIYiVGoCBosM6yGmcw1jqE4JyERfxzqCa1KGtmpZpXmkv_zk-oHkFNoP2VLtgTX1EHqDfTanutQCDGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5r2RqAScEbX3PWJGjnqW3YLoQz04c9JHJsSwloQBxhg3HkBRr1RhHJH2hmrDfRKAlksAa33zpzRX_AEaAh6j6VA336TWDVZbUujVNk9j5BDsY2vmcz1lNlrBaXLqEsN8SNB4YljJ4dkCkHdEHUj01xYYLzHH1dzM3C1-X6wtCR-N2Xy1lVR6OGdM2RHS7wiOtW-Wh9wmm2ufpaBZXAg4XOJxeJ2SYrE4UKvag139eEwMJSx3_yb0BB9sAdVLM_KsVCxn_PWTrysTravBThPx3FUGLz8ab4IuoqEpKfRA4GQJSZUiO3MMMjz5BYEw3BgwjVEQjoKNJM2CIlE-FaHsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVkwV-2Qs9u5P6jvTvH8r29VyyPLVcMN961K5PHCB_882auOddZaSSh4ZbnDdPqVCOOaUFGBrIUHY9vKgXnQ5MgrJvsEQuEihQR3jsN11dWlCREdSrzWDjZRzNXfBWZANgt9oAGqusIbLajyekaXxc59sMQNxjyhUPPYLKKl3ME4F2W5pdlKpvPHfncAjHu8Ya3NUCRq17qV54DnKdWIyxE-nDoFVWn-o3IjZCePxjd405b6DD1uzWL8o2SA-xHya6eex_eoNEM4Vq0a8QBOl_n8qeC6EJlyUXjEDDAqx1JxZTWXpVJskca8eoC0LPiELMzeCYjyGbfL9ObB96NzsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHbt1kE-IvKHX5Dlta2_ivv1GzmPSzXYRGfN2lAAu9N1y3CIsERoR0d2R_hUvOZCqysKHz7lJg9wGgBXtlh1Nbo7ljmMwdp_fGPgGyprwRMjXj5euRb2_mwmhvu1tiJhiAPA3SO2XaL7ENNTrpk10gpBP7bBDiNKBkeilY5tvNQhttdMu9mLasa_AK7J6dvb0wx10ndxizFCrTDXt2Qf6Fbyb9PG3zwNKqOrcjH7H1xmhCAryKoP0m-EBNxL3jMTAXsxpu_aGwzi0N7whDb2ntDYiOOFmcXNFN8NGvWEl98VVTHLVwGhZXmTvIoOSdi9cYlNPn9lXWpBinYfjuy5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBgtXkdKrqMr4vH5cI5QiBQALf63IgRLhDUnclLSZ7vWBYkAcH4IKyCEzOgx4QCCwx62DV2H7LJmDsFohCardvbTJdYapebJ2XJsG5WOSfn9A1HwDoXRs8XehFHVTYK7sYtBLGZWRLrkfDWke3f04bnssJQnDSOzTqhpjVWpadUTmbozhhvIWz2w94Y19a3UxLFx2ikjOpuDVwiRk5powXlrqo0os001RBtvR1AgFMLqQ7lYaobq8D-493I1XCURhM8KNPKzTzLplOe31TABGruiTH55VsM2in_ufqhVjJVtNmviyqqazS9ZGKpauVVuxsRq8PpSxECizoSBkOcOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWLdOJ2xi7NMgMsOkCAG9KdPNZQtwJCp-RR1O9Sx5S1YKot-cHp38BTmvBrcu6TWZydQR4hn4pRaV9AVXeHuwkd9tBHKYmOwPYG7dPkIg4j3PFElUSNgzdAPgZx8PAvhMYj_NeMPjbffungOHFQLL3ibN0oeeAH1qkhNv6mdnGwf4fWITVVSTjA0BNjg2ZopNyCupVFvnbX_VoD4kpDSo-lcIkOTF-uVJSsQXhRWAGNUOZBvgE0WcLSbYKiKS_Ts4vt0zFRGgRKpFkXU9o7fNjVw7gDoYgZB6sWbUd1EBs-OmCZsF9FEbu_EItDwoKmmHtJW_Xuei2QSC4MKpyGKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
