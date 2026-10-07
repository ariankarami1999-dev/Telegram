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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 01:37:44</div>
<hr>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 424 · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 984 · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=vTEDeV4Y_qx3OuD5OJFkf04C2nMKI0wvv5FL-uKqypew7jCrTYyVSv5HaJPjliYOaxbgvxLcBpImOf8yJky1wefuwHGcch1F9XO944A-RrrLRSw_VlW15dgX3piJSEDpz6hLR1caKXAGeDVkVEqNJCISht3Dt6ptyg3jJcb2t-lLf-FpVSVqDKYwBl1bn6y2s5D2hY63XhXKbkHQX5_W22aJud0RtZDaEQsFZCyX9XQsP5prrhrQ-FCQ6MPXmSsGzDiic5FkzIkxBTUqMXGjalUW3penAqtd01czTfYX5HfkGdH6UEMsk7iInDJiQEMjkhToX7660wPwDfSa9tTzzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=vTEDeV4Y_qx3OuD5OJFkf04C2nMKI0wvv5FL-uKqypew7jCrTYyVSv5HaJPjliYOaxbgvxLcBpImOf8yJky1wefuwHGcch1F9XO944A-RrrLRSw_VlW15dgX3piJSEDpz6hLR1caKXAGeDVkVEqNJCISht3Dt6ptyg3jJcb2t-lLf-FpVSVqDKYwBl1bn6y2s5D2hY63XhXKbkHQX5_W22aJud0RtZDaEQsFZCyX9XQsP5prrhrQ-FCQ6MPXmSsGzDiic5FkzIkxBTUqMXGjalUW3penAqtd01czTfYX5HfkGdH6UEMsk7iInDJiQEMjkhToX7660wPwDfSa9tTzzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPq_u10OhJDa0AMEpJXEwynHY7H05CnwJfl78hnFF1VNgat77CzbXs6q82A_T-Zr8R8ZU5sZa70s29HqqIqtE-rDx9kSiR_TKecRJJmyAjuhjkUbD5uDXA2d4cOYGXFFGZ5Owl3jgQGgYARj3chxo2F84FviEz3ouxTaumhdpczaZLMXgRzrENi3HS368k4UrrqIDoJHFhtlBzVvqQn1wA1UkdsUY_PVzR5OcfEwK1XlAPwlGVIHMAL_SVRnYqNGvccr2O38y_uEwMo8Gt2d718yy0-hg8h4JSZSdoPNNsrCGLMDpOi5oc2G24MaadYXkaDjeHmDZTfNY9gn3yY9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKeZy2Rf_PSn6ExFrPqhW5Q4k9FTV59xeKNKkw0ADNSj6QNexzR0-jsUHQaf-_2PpfV_ZNgX_PTpqJ2Dfd37emQ113pWGNtmZvjctNXl-bri2-jYs5QNiVg1L12-hd487JYq1vQ9-Ecnn1R39rIJCcNq1R7tjpQ3kNB4X8fLWfbJFdtT78lkJknMLs2KColz9NQQ6xSIitPCNIxy-R7fVK_jDbjqy2NoRStxpkzJ7B6Xr0Gh3lkkUPIqYCPRu5EawuEtIqZu8CapFPB-YmNspFPYDwHMRCfNK96AMH1_PyTO6DOaE7LEegOPM5tm4o0PpU9h3Dz5reYKXjQQjEK9JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr-iRmP8SeHASy6VWf2rprjz-rXW6UtaVH-C8EfVpY_dkRB8AXCX1y4gLPvet02O_x0jFe78dtviESM6S8SopTvTM75s7rw5MGTu76AEm0TLura1weNE7UvMLm5-EKblvfaGcikVWiAKZ5ZSdclRZ0kvPv3rToEUIcyKF_7H1vMqWo1ktgIgy-NIWVus00CKLWu-TEYJOwDsQWSUZtPuXt6h48q2V3qqISxldO7MekZuCK33HotCCDRayuYN8JgGwt6PdAbZ0uiNU5VoF6yTGBa02eBNNRcImUxhcJqawO8zw7CLeOvNgM9OqUVEyHN60XtBng7vBdA69Q14pmxOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mzt9sLIRUlc726-1ucc0_WoPbtLMHFzCZP9jS7JPKR0fzIbFZbs7zvbAGoqP57MFInrctfSPlf53x0vIcWUH9Exh4W06YDf76zk1JHwW_RjZdim0f-065cur_MuB0TbuBAQapT5QE9YyiHYAclXXs5H_5yvN81YM34vAeX7fcCVe3bcwn52lEJs_aYuAPJJEphK-J5uTyBnStBGAQm7HKEVdT4Q6-acCcoRqUmIND2i3Ob4WwkgoV5mD2DcUkaRBMsVVXuOi1-4orxeLgbAp3cS3n_14GKiwyFi-VVQAn0SXj13Fwu2WVg-ESyW18lFv23t2xKvqDqiIMdcTa0SrKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or2lqX2O3kIwhFj4JwyyfGYBOq6H5FUhNE8WQ3O-zZCiz4TaFrMuF4HIPHJEyiIROjOPxbJDRGceBXSutwpnIg7A4n-BFV9Jx6t630mp0ca0Vco8dJpH6LJuueQZ_2_2VUKhBUzTHps7r_LOljLI_xxacP2AWjcYSRBt8uyKEEFqAMlCX2-gm2IYeGAjyZ8ZdG6xLTuGyTJE8GzepHXLFyffdsNW30lsmU2i8HnfdD4E5MyNPQ-3lvWS2rIbZSnftBdXdLDLyP8IhTvLTZ6bllcz1x9FUqHSVlMd4cHh2ZTl3bXepGXBGVyAr1dlL0766uAhFcb5jx1kc5g-K1yh4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=bVbl4J3asbmO5AgMX1mPzFBM9gsTKA8wPFYxGGlIcHnaVk5p59UHtuZbgOCeG3P_f5HzCGyOGAbJCeYbsB7f5hQYTzy_wHhN93tG_J_gxRKrfIBLHZUVYdSqMT6vXnOfHXtVOtO8SYXsXm86UCTm6kysCIV7Zz7OnC0OPd5RmTx9iM_XDN6kUjjNeRkuou1Za4RoU-vwxHHkdRxZ5RiBFNiusM32pg5l4ljpQHzTzSmm7qEdGZZknYqcu-44rHW2HzzYXSrypcOR6NXCNPcGadWJjlETcj31h20sqJyVSkelfzE994CIj-VVHztS1d2B_ZI8aMuBfCtNJawxWwFivA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=bVbl4J3asbmO5AgMX1mPzFBM9gsTKA8wPFYxGGlIcHnaVk5p59UHtuZbgOCeG3P_f5HzCGyOGAbJCeYbsB7f5hQYTzy_wHhN93tG_J_gxRKrfIBLHZUVYdSqMT6vXnOfHXtVOtO8SYXsXm86UCTm6kysCIV7Zz7OnC0OPd5RmTx9iM_XDN6kUjjNeRkuou1Za4RoU-vwxHHkdRxZ5RiBFNiusM32pg5l4ljpQHzTzSmm7qEdGZZknYqcu-44rHW2HzzYXSrypcOR6NXCNPcGadWJjlETcj31h20sqJyVSkelfzE994CIj-VVHztS1d2B_ZI8aMuBfCtNJawxWwFivA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1I1keKvraQAqU6Xbi9s38gi0hSSQHr2b9g-dWDWf-OT1ydJbXEU2u1fjw18TobJruHMk9_E4yb7k2obh2TYWnAOIbA7fo_5Qwav0FzzEsv63rSJCqw4oM5hlBzYr6EIHtdNv7Ac2stSvlu6VqbaVkdhmrsnStlL7vtKiIfqgaalpsfgXKP3z1pKzFKqrj5E66rOBQthQ759FtxneiPN0ZU69sgJ3OneMy3G6mIQMyx2S_Fcnr0uW_YHX4xJbJSeiJ1zVdj4xiuZz2OTQHZ5vIZ3ADcZmkNI94o_8wA1EbuBQlYx94wmSG9Dep3DTpjrAIqPu2enDrWdBBM2TsNyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAU4Jx4Az3ZrGByIoIe6XfjDmzXrDvDulJWpL7Xkw9dPGfvgRZJpQIj83FC9MWmpI56GYOfqh3kz0OyBeWWTb64wr2mEGsylKTgIwQib9LAUTOoqbFdZ38NdCepCfQVMNekfz1kMmfOxbIuiVD9gtFOwfrXl9sMF19vKEMKYie_llVS6aNVVg85s5Zwnprt2wuACgqh5PA92d6myQKzcYt-es_WNYm8guHfQwT7gqj7dZPgs6uR3SXZAKyEjpdgKZZotCPtozghgRgZ4IhYrG5m6mjGXguHyjTD4bS9IhvmK_k5dpa01bxzW0XVVgraZmAunsy5_fWE6ENymhvaOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hi72pT7CNRiyeJwI10ByjLYXH0Gz2JVKA1_wwcUyyuHLzQW5YkMbSu8ul0JipvUibUyMlIyohqy_H5o57OeEYXE--zF_Tx19FaocuRN2dYuL4jnW7FIgZ647EzA7Cj2s9DB-abug_-egYIwlbCcicqn-JYmc83zymZSFhq3jI0RbqsU-u12JupLOd1YM14OWzDPWfJheE6CSzzYPT0snc1wZyu_S98R0RKwAZxy5ZhzC2GI6upe26lvhLJXu20zHeLF82gkq9XaHNWOc4SjTwvjAdlvvd3ZgABxK_8AE9olRXKNhNflsohOyFwin4rZ4rtDIWgvCany2Yfw1CV5JPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYEeZnQ2vZ6D4X-ORJrRB5j6YnLToqnKX2QmSY50dkEY0GYkYFspC4DHy0M1wWX4PU-Ssa8oyylgiqC_k3JB6XHsSEVOZHfejbueF5yApPsHSqIIqHWW9oc3nlLow4JOMSlO0J2L0aJhWrUcw5RCTGfDETcB76UXWs0jYeSNvWCvINROP--eAU1BQaGy5i5SusBWvHaJpTsAMmhT8QJPIUCm_gSJBoeVC5I34O9IhCrH14oDgp7-BdC4Lv0N0qKJZtlcsnG-uoyoLuwRYQE6Hwf93WWu_ZTz46S0T5B-CV-V_ADOPwOkMhVzTbGWqfxivVDq-OArVOZoHfsOi72e1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTsqrKjuiKasCDm_fN_ikvI5AQuFJbVTG-oAbxEMEEHATdODzYm8njmS0PhtpSLGT23gQxjSdUs8YEgYbZxQmoHyhxpOrOaQAxl9eyCgoXEs1VnbwHuJPDsEVWgVUGyBsG8LwBCUD3OJrlHb7xlp8zy8InPDH58dWOIbLEZaN06pNDOAysOlBxYM4AwkkRMM-t1gPCRxr0uc8k8O5_W4QK0P3Xo_r5A0qTdWMhO8udY6yZTrdmvFK3YfURg8X_Hn7UU07tNwEYEEaby-5dHmxpPG_MePWGZlPEePsGZapGdzvpaCXN6xd_I7ymDd8gFNoZHekUJ0Kh8fVS_KQXDJ4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR2Y_WEV-L_DazvAy9RBMtL2IhzeCiqELLkHgSNS43V_CifbJKneeSiMpfLAbz837TA_BVKuzIKhnfR_P8J27EckbvG9TsfTEttAFfhA773dUF9sRI41J9ZwAUWZmnzjJuacwJq8OmgVHURfa00YhcFVAqZTqfV6de3C29E4NaGRVR5jWcfeTQN2tIqUGvpY5VLs7m7FY8mYfTunTqlEsdBWYVGro_Zt6JK1Qso1HuqSlF3N2vxUqTcXJtfpCjScDZ4TAFbG-tiKNou2gEz0G6H4C_mellNNsN4Qomfz3SPhWyk2cOlcN63-np9sFqLPAk5mVaNez2LK7F2yUuYCqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fzEHQ0L2VonksJLjDdF1VGmVaZS6uT2LkSBVv6oD44WwhIoFZLqeXUDXxFqIZlunky32j7JH7hu4OCgGyUOswkcOW-j6d10OfcHw-x5KBlHpGAkXREYSnLZ1CiHPk34glvRJN0LBGJ1V7SYO7npTKxolXAvb2lSXn5DyDOC3hOC5nqzjpR4G0r887hii5QbsMper3SWnkj54iaK75JHecvxJuEhS9XsZvonxhDLeI90wPEQuvMc5cm-rBWCJnWOVHP2cKEXgHnrse_QcNlD7bKKZFadkmMHRM8MZSlrnVmVHyA4lhUXzU6hjRW0xZnHD2t2nPhUPZam8BKHaPiWvLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aKii6vMV-4DHSm1b4ivcga1Yh-WBRar2BTneaCUcxKs2t-xSlxxwKSWhCQvbJGsnU-RaX54M7ykhtd3hc4z5jRBnFZUPo6Jg19dpbOhcKbvDhrXErB12OWI_tF1fkjF_vPyv6mWzb2rRwwDWHLb3OmuQ3Dr-Azpa3P1yjZX0D6sXnhcUQqZxeDQvgy4j7yFJjoPQpysthDyTFBKpxPrQwnXwwvvEB3-SpWmO-7k1Kk6IgQn5_bbnF1ep6xJ-HQyfDnNtRdECZZf1PV_yGtp0JpwDMPhj3rassCP2AjgPd4Pr26aVzLq6ykl--IAIlJTUPBQ88mXBzOqpSF7G3kxYGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bNivr2vtPXHEGTLYDXPne9IfalJQ_HpVOX8AZ_UxSXy1yDvtZozS38jKZ-snstDPV2llhArr9-MvU5vHDNZ2M4SshjiVXcROrTQpuZGLyfb7d7kiEQ0fonZRFhZ1neL8WekHd_3HgbfF65Yv-hbZ0YcQx7NZfJ5HmLhK6wzimf7L7YsCdrEsI63SKBVDg2AJ-mWkaAYcPpss1QRN9C9vzoyBT9jM9adgiSJiI5B52eFg6zQPSphPVhYbansbw_RN8KlctZdwOik-eQP9FFrMJD5z17XAKdYa0ZSjprNRSaw-OqqIMvWrR0p2qauJcoGg819rRWtxnlirSBWflwopEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
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
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMzi_maf7xclDcM9CNoFo0cttCNOSqp2xomextFabIAXqBdlkV3uuXWcCMVQsIO_d0Pj8294XbdZYMIaSiIkPrvOcpsxIxjIQGt4eSr2SN0KC53mD_qMH0M-92tX6vURLrHhfyc4uzVgbDPHninm-o1HmKzty3mVLUFOX_yxE4WfMPCqeKdNp3lPWHntJ1Wz9wF_4qcsfBJftA4tt-qw718mGlKdhUy7_1L1TCupVBRj0GBxvrYrSmH5xFFhkRnlTWYd_9dbmXeNnN88KFwnl15V1z64GQ6GXzOKAbZE2pANXo3aXlcqnXopMmZYSwDWZq9O4tPruAUJB2tSpFN1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzR-rBMAV2cyUNfvCYOMwVmf8ImnhZX_I3gtBwqAnKmx5Bg5MMn4y6FQpJvuvi6SrHD_wuGg8H-NH6s4sEde_cLBo4lVEJg95s42HDo3iosrnUyEZOCaRLSo5K_fAseUVQqmtyf9FvGaYBYsl48Yaf4TeSE-fMoYJnO5WQw8TlCiqNA1ws0cWqQkoPo76_PQBGBxUZmaNnaSByJlloDLQRygI_S-7ttrYWu6xETi5ub3js5Wyn3wIU6vKL-rcCtvZHszkXD6DXSERy7S4N3gcWWYG9VIi4r_ha8TN0266d3P6yCunszaM5MplMmfWPMaauF8nM6VI5rm4xfBoZsSsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgZ6gq_TGZ0hw-BcLBCpDVOTkcIBjb6yTpY4xoOLxr_bcTHAgLCuhO77CbkOfszMXZieSV7AI1enKDdnCAhKDw6k-V6AFdBahoiDYICZfP17pLQ6lAcdmQoXF0QFq_qAzmym6QiHgMw1yGCYKKnfgPIoxjCIfxJCssaFBuZfzHSDzbm63oHfCWiiVQ8Z3Ns_JF9mSiVprGasU2JcHLLB_qjFbp6kCKxv9NHFonJD6XyUFFYWmQTN_L2sLrUak1MEYJLHF-nPVQdQf_TZkPRtI9c690n7CsCmSkvfDW-4brgqbWyS6r-YRTPK_cG_NxnPpKXphYCKGQzNIDh4RcuARQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JR8h2UN601lFBGgmtZRdYJgT0sE7KV9EJuSJL4B-3C101JjJfEjpSWetj6Vyivft2vLlR4tdvV5MH1DU9-RHNmBWo2Hd5klHKSFpL6KQTFnFpvA2vuVZesmONKfplXIsqfH9LUBnSpjX41MurVAeswR0_5wLyrQ1aM7bNHIanCP_-Gev7hmnm8TrVgZQRRy0VqXAn_splpQU5OFFXenjMRyEn19FEgnW3IlB2RvwMGgkQOVzw-0jKL5PNXRFv_5HQmAdGniBmEXIVJpA2zXvmjemn_ZpI_fmqpFGRQkkijZAu-eqGEkWspuU9oITdb1B11w-EiGSup4VEClGjBgJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVXtCqwZ5czYlp7MZuL05qtNyWgiI1lc_TNNDmiDPK3tarUC_3pc2LuU8mY0f3Ld3e31lbiLDoB6jQpmBrd7DmoH0-Ar8C-rn_msfOE-XfoaykvRw8GayCE2TF8m8uzKKSeuAXbjKb3slHSeN7DkgWXmCCaDlX8Ysvq2JAq_xhmHLp0baBYHidDRDtS74p51oGiQMr2Qw05cKKUYtv3DaeaDRjRFCA1zgo7E5brG4mqaLYP_ZXORq6FDBfK-QUzIFDHGa3G-18BmwJ0JpXqEZ2ty6qAdUdhOIoWagzYok1XZC4BbZGe7EJ6cttost-CrRpTuXtoa0veiBzWt3fSfiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQond7gKaAR-GIvQdR39_a18H-xAwLITlJFrKYk72zDqTAh_0Ehj5SjSmtb_aM_LDgUmAssu_UgLw9o7Z6RBtEAJnNWg-jTunt6YRSoO0Z0VyNVLsMhseyndoJEM_OOL6cuSTHcit4S3OQtoecQoFo_9n0g6_Wn0vEf5T9DqUJQZCRnS-FYivJ2h1lvlO3l2zQyrnd4siUekF25VEGXGzV5eh4Khyzb9LMxdbQBA5xZQUkSMr5iEud3ni5avLhY0Yy5w1CXk8hzH9T3nnMLJNB3cDibI64-EGhP0i0HZuJ3rl8R_5lhqBsuiB8-PPQwQJtZiMcQQ-dy1Y97ZlKA1qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh4sSA2Os2Y9SCWmXoo7EewCCpe2xg2cxTwopjNH9uduvZRxJ__jyXg5QfI8FlapFh_VDb97B0edIb7but5bRF30wsUK0JGl-FT5ampVVgMgV9hZXwnAdqv6gFgeo4uLOGUgxQ0NNAUZ49LvnsQ32GSPzdqGAH3rHtCgOM0UEKBopjJZTjm5UwXXg2dd8zC2P6BtDF_PVxRtZ5nIkmCKOq68sI16kFJJrMIX1f1riur6NM3XNVYQgQGcKYvIGdbZh7mG5W0mQ8fnirGcMFjof8uishZ8UpTBDaQvUvaM0WI1sB0UWcqxCLLaBMGDkthy_zJheLL-sjhY2MPWGfe1lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lo-HZe_Mx_Hwwar0NG1YZqimcDVy31gAzr4Lq8gOw7AlIstHfFAqDjDaJDhhoOECUoiGtlnRJVZSHh2R-rDbocC8222LmOKuTpMhUmDI7ymOMQ74DpEfv3IhfMczQquV5bI0a6f3NqU4VPA41v--7Zazh5I8DXsOQWC7EMEPE5dJrhpJhnbe2RG2MhmcY_7zCYAVKj_n8Osk9R9U3XmHAlpeArEAemiCI4uHspHAlWqjv02f0ubjmS066osWm6uNhCQncJrek9oHhgHvQMI1sg3COeDGVQbm0TLzaf0sFqGyfCRHLrDtxIf_SnXGFeqD5rLp9pKuu5wcOjzXCYevLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PB9U5u7gYZZctgr_ax2iGqiM6i0ASlhQXQt0jip2BwO0-jAkF-c5MpivhkCZZanAXIbfuaJppzaO7KbALCAXuImoF0q9yKx0KWMvj3NpzNeh-cx5SMLFk34VidjN9rzlqhIapmyKcENLPNDYjVQNv-Phsjk8GoUiCrPVzb0Ie-7oj7JDoChMbKHFTCPAk8vWrofq7lc8-7oqLcQxTMTqhbQz_z9fWjUA5_64uTeQvTjgvJnKs8q9M_lyndYqKramV7CdTC2O5zI9S3SfiJMwpHQ_ksXP1gWFoiXluXPQM2BqqRXBr9CcoW3QqdoPH-cmoMIfhsa2kj7cghgaBGIy6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV43qjljHi7cfg7RtWk21MM-NRzsovh5l39_EZFi9E07GCIyOJh3VE1Zk_t_oq60UxC-ZQdiO1zskx9geLXSBPJr78boQXvK4gwIWe5Gb51liaiF5Akvhmne4BfEW_VVIfyeeEFmtM262K1ceqqOwOnJXwTPyhu6AtM67c1u4izDJG0pcQAHJMVtWOGj203NjFREcjjfTpOZtIZVwf0rqHzXLxdfDo0eZyk5AkHjZ5L34ajjFx7tHCwCA3-QEmDyQAS9hv5uMD2v7WkRqd2I1GuCVP_eJ6KjFzsh5tzV_L56d4KyXhL8nb2_jyTIXmvIotRDpB3yS-pnAXaCi2MU0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MFJWIxVp25U7E9IF6RKnOUH3Po5JhKYTqUbuwZcqAgBodkstMX8OSwNXg98phdW3_x5TOlleC66gOyrm0eC00qCTwE1rPvSA9wk4G8ggVZwtfoFOCumXUfjiMw_wfVPHBNoSH9UPqINKg0YKAXwphvkZ4tRbRo33VqAWZbfYV4ga5jJJ-x_U-XZD3islSeXJAmVwLRriISMLUPLOmkwPJYJF7fgN_BQUgw88D8arpqmoVmavYsv1eoMC5JGsc6Bp-J209_wIpRn3wuxbyY-VxYuZKxX0VojJx53eQNNaIGqEYctgJOK0YwjXLabz0mhF0g4CSkdYJlcz3CCCjSc6lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pq05vHAoLjazEbG6F-S0eegI4BJTkf98jS3wAfodDp9y9Ou1U8Edin3hA9xtII3g2oTOzXPJ1TtpD6Te7hk_LNSwwn8Trr45xpUa4-v6sQkRN53X4LyFVraWmTDhTmMeCQoG2SInWCoKuqQ-HpcLIPmkTSWRcIoSgpd8o-EIA-1y-8_at1D-lhXqQPiWTnbubFOh5EZt8-L4uAsm98grSK6NmIVtA4aRE61YBBSiBxmpVMmnDHOz3e_nQnTeHR4AMzgss2AFokNvXEf-5kujgcbVJQpT7Tc0YKSRdOJTMcpQTO7-aiE7APIkp3hc8digd3MI_3yfEg8nYf8bfq-bOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS_IPwMWTq2rzkJTq4JBOK7Eq1Zg4CLUcirsndv2DqP-NWubMsEYS7tr-bvySgDpYf4hkoM4hGByo0CKztGgw_ZCGbBezek9liABnh8ppFTG9wZPclMEqJwTaIzGEGVIM5z396PR587YNQL9TdQae9jPpk8xhdL8rZPztDOLQIZXbZJ1gok-FNjjdkZs2qa0bQ2vmmQpmojwnSHUfVPP9bbpy72SuQ7AJYrMfzhixCAmEG5d-flEXRY2J-oomEEIwFsVhTlUV61SJeyy7SCiCZLdECRpDcUVe4pwERKkWdZ9czLlec1OW0JoThPWD1H4weicrcM2YS4N_zjn86HAiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVhfJaSfaBvCKJd0CqCaQsA7rRiOQYXQn6sYkfGTU5Xl3ABx3V-jjI3P6xjVWLLKi0HUJq1smEWEv2zLmvbNaMXZgh4gfPtuFsHcBhCzA8ZXU-R-EivpwT3mQjSpbBHZi06Av99YmK8_jx7GMc0kwVB5zmexoeTNVJX6TD_if3XPSppQFCPpDIwd00KJQyF6tSVVu6_FuX5ItLjvi8BcHbVF-Y3FNF0ulEncsX5CG-o3AiND4GWR90t7JzFc6SoqlIoR1Wk32J9T5qIbrBFgPlvymaQnIC3OyWXN4CDNnbl5Yst1ozsGUM0DlWswJybv97thdhADY_bftpPw3EEXDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td59r0vWDBgKZ5P5oBXBVNq2ZD4IKHd6vhO9W4iuycWb625kKF18WrhgWaQ24a8Zj0f8L-hLEwi7XvBLGq-LQlNA0ezfLh7PyDlAw1Jfs4j1bxYf0vp31xKEg6pT5fAo_4YtYDNKq2f4GmoVrEPNbbCU0yS-LfQfx50Lgw5MK13Rf4iu6fx-sAtJ-KHa9FQ9A6r0tJjuZ_rebS12FuVNVAwr5jDQZRo64mzlkDCTZ8e1UVUUFy9gHmCGr5Pr9FI9gR8GpAC81tEdVGrOnrjXPE2lNkuPoxPft3K5l8kW117hbs7DAtpj3LCJs9Z8mxvhrImUzhEisjGAXYXzdwUt0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5Ah0x6QfpizbWICBSITySkaWGETwSACQjax5YORSi13W-EL5jVabP2FrHzy8ZSmlzCh4MoSiQBboLrXPiH7aZn3-ZcYCl4L2gRqqtR4XR4cKLQufa93yEVwb4YBGjeKz9LBIb3DiEodVauFHtVlZjqNiEofZqQ97hOAmAO78NBdtLtGw59nuthkkMfK8Jlq-gKiwsV7fiYto4k56R2yLTi0IS-q7rZBrghW1lrbyREqnP-pGn_sac2h4waJHiw5hSFn0IHA8gnabPT12X4iWRN5xPKLr0Kk4lv7oEWaA8v6TmtFy6Mjjkkr-B3gPkSTHX24B6gdmOyBjCy3105Dkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO42DN7--gv3c4TX9IVXxvFCk2OaT_XGhAxE7TQqtKujto-Hrgb1fWllESv31D5LBkdHok2EibL3oHzWCgnRrkC-52k2yWI3RAVHKXtuLlclYXQEhwIU58bHCpDLKBBLVIyyKaT4PdqtBvJwRcQwO1MHo7drJ5OkVRVPRKVZpLSY4Ej07_Qyw14OP9yJ6-6E2MYXq6GnaT4xLCC-O6Yc2c-0uCY27N20Pc8TC_wJjfWSJ8KJFbIRxSduvLhwikUZMwLQi47eX79FuBq_zCLXyZgwmNFRdSJdXBdCC7RDNBqfOyi9AgZbo_aIRVmqecZB0tpKo8TdOwsLpwAD4s5m8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVZVs3zRLtfhSVOZVwhhSb40IR3wgf3UoHAD5_5owmNPcMJaKbU1hIYuDjYvPuk0pdJpqBkTHgQPi_DtgErSJNRjyG4Ba67ZxBZ-uf3r6lUmUDUBukz0Qjv1XH0CwjwVlDJJlZPeO7uYFu9uww-mZEP4eakcbIsCqeI2bFNbM_q3VPLce-L_LJi43GOCz4ug6mNSt6N6SPyObGOykTw4hwjGr8OgBPv5v6nxEZk3JpiCk-X9TAiVTMdCL9apI7W3WbTBcQHIYTt4091U4pggUtHnxLx0zjzZID1PIfmkErg-ezGTqZuK11DNXVlFTZDwMrJe66Zg-TkQ0GodFfdLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLhnKgSz_vKxuGAJcRcTc3h5OBMqdn3o14b9L5ZK3DAQnhKg_8UKynqmmQamp2zmVPqrSgrLlWstKKU_DTySSGpIrITb1qhvB-Bz3lEUETu3wTT0JqVkBrvrpzvEZLwXVYW2TF_dlyDI2IA4qNFF7dKEJDXUZvINtZ6YgGl1thWhgTTKdqGddi09XYifqLXSRjbLxJNdtSluwdyoEeEPB5c-cWvIu97TV0SJ950YP6lns_tLn4ht0a805rJ0jig61gP7zdRw56E7-ZP4PvCcZHXGomfoiqKMPF8plGYfXKb3jf1lWognv7QFsy6zuOJZphfaHu9NbK1SJV3y4dZhEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwGPQAR1_gvhODUBZX7wGSVUtm4kdYSh2VEOl0Oap5E4RNUmyxZQy8A3cI27b7dVGS0BvNhv80USZRTiyIKEGhzkJaPFFiaayGmDyEVijXa55fPDeETuadfVjWO26MMusVCk8P02PmBpje7lhpAoJbFBg1HG1LeYpTZ7vPHo2CxOtxcH6m-xj8w9NKg9Fir-5yowFCFrXHvTRUi6sk71SOJZ0p0p1ALSAo4PnGCI9GsqsAxEYeOQe_mddeRk7-qX_QBKMZi7m31bfP5idGOpW5uf_p0J97GNYqNmi5rlVGpQdmxGhQpbBK-XZz7dkNR_PKNbZp5W_v4N3_pvRk2R5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx5et3DuWpWhu_vhOLeTxWaDRr12SseJqPFkrbVDZgbNscicj2JhhUVp8OlE2tsAm88Jf5qyY-3TpZ5EhgyWFf_FuwX9qNiyB28mtlTxIACF9FbZGzYHYj5qXp05WasZsR6N4LIY2c6fchqCmt9RMb_hNT-0yBn47GSkIyAT4U8Rv8TRkmFLXuMovovgBGH9-8rGhNmc6cklXPu37_2LI67knlFlQfoGZQK1OjzdbpjidJCFD4lTUxs-CXtJQeMEeM2OdUPT6OjNu57gattPmz5IeaV-pzzvGnd1-dsWGHZnmyPEbvWlD83EjkqUqWiW0o1sMKzowRxhB6J0VCRQbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwc896zhds9DA1oKSfEv164WqGpbqBGMrqG2lCJSHEJhDdhNWUb4qyRAHwFWwsu5Fh5Iu5HuTbZRQFdsQpDkib9lZzJuULq7n2-JtUg1s7Hyg72MKPDWAvlUKHsy8bEbPsv68lLIwfzo6MrbCsJ-GCbWonWA3schdfzAwMWcvMQUtH5biuvcWUm2yMvtGYwnl-swe4RVkv35udV2-CuIiaAy5WZq5WvGKBtOMmm0DXCx5zmz47UpkRv7qXWXu1qo4knBIYcWrj7FEjbml5V3xHslNONq0OPPISQuXx0P0bpe0qke1wwG4-3ii8MtK1uBW6w6GvfL0Zvt8shhXXDQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2il_P1EVNosSeRi1w8B2fRhIc_2hVFG1OcABrmbm5-xiNG1Ciq26PQIlrYUsT7tRFMLc2Bt2DC6xSs7kvLdpJvsSN9F48fq0lGeSJrq5nidboMtXyugOjNa7r1SPC0IE38JB7I44b9Y9_oMEfZHivVx1KeU-pwAHB5Md758URjb5PJgeVA9bV51IHKKjAwDH_jSj719eGqL5YkXVrZqzFQICxI4vfRr3okYkyBLdnczVPOXjli2R6O6GeymaNYN-Q0XPXA8taWjg79ot1EXijHt80-_wjwLW-Sq4v04DBSIKNbp9mVfZkzLj00WquCN22_19g_LzKWrDSX5tGzGgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMbQIWzcPlzAuG0TZXHvLQwo6rcq8y-OKcTFiq-2d84L0O3UAEYpI66TiYIeQbn3Yj0DaLHVAzdvUqi-MthJ7PqQgpVEJ1I4pO2mGJGM9pooZNucZzmuY9RD9k3TfGl_3xTEduQKFui-R5qSxEi-B8stMGGPBRr233oEsuQSCszIDZC_UB9Ibfq-H-TfJX6r_9wKYHYVTyjpRKVBmYxLQvw7ELWFYIFWL9wiUWXHNVxAIhIxVkFc4bZo9qbDkFhU_EdxuNvRVLAEirnpUb2bDnyEHsWVs5gi6U2TjK-IPcSZV_VRCdL_OptQ27mP5DCO6SVc0LSqu1b7ZTacyDxSiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dECP-PKou_BxaowJb0fGoXbmdS7GLERMLMkGRq46pp6G4mbJ_ibVZKT4SFdGn1zNvZr6FyA1sjnlljGT8muX3viYoJJC4IaKx9Q32EywQagUM-MN3OCRbNZBhkLd8kY3aRYjfmacyhkwrIQWI6nEERD3eMrntwqVbdQGmQAK4V9nr-2E6dsyNajUJpYYbUPSJtIoZS_quY6Kuk6hFcRpFnpD0GuDYFbwhx29VcaVmCB1HyJxGQFWSAgwP4Vfdxagn6DZ7B61IgV4bal4jVYb9LZ8RKveOOOmbCeTbklj8Ndw8UeFZHJqb-LQkj_7nb6p7yPWz1QTSuGP23piDOj9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE_PZWM2MSSJvAE1O6pCgfUkjkqxy8w_-PNl-2oLCv3xNvlhVZ9nu_EaMzCY5a53E_paT0GgAFheuDE9r3IvpKEHa7AR4p7tkgRS6sm1ExKav4vja1Y54ygIZ6z4VLa1a0k0u7mhVEhVgYByg3G2nvxavEIfbjnCBelp_Qd5MW5II4jbBoP0Y4885nuVeMCnVZZFlO6e_f-RjFV2DTQ8mXhvedhRLUHqTwtfg6VRAkPb9TwjcKLiax9PYdcyBMCILgoBYuY4wK9UQhkFVK17z3mnjsbP-D-fb2007kv54aLKWIy-hf70IDBbjiPgtkiUjiO7twF9BmPUaOlRGEoGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/APD4BTOGQzeQn8G4BBziM7_U0sy3tVZOLYelf1B3rlNASO9VT9wxJ5v67CDO4cRNP5znnFDsVgI-9dMDwSSPTuTe__878L9P9BHYnsxGhAOi-FO7lna5OdbTZ7il9F3g7q_3EXDRGYfRaVic9jdYwHjs7TYj4DglxmIhrQ04qc_u3y4sGqtXrGa7ALshKOVCavcbxswd1hLChFdWHV61KCxQDmqVT9YnY_T5pvpGSn7fkvTMPkjNyRilaW9q9B0ZSzzInlMezwsVa_G7kHmZAFPg4g_Ust-Sl6TBKGh8GevDHcufY_jAybgAuaI253UHTsBrb7PDt8a2BeiQu6UVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtAKa1o2Q74gAjlJcznAtc7iCnHMZuHr9DYg_aamqUSEpl5-vyuEVAomb_QAsO9LlCfHdg6okebVO9GVWK-b3f3vwdZOpRwXGUhnsEdeBVfpcEOZfWM4oTdjVjk2ypRyAi9ODDOrobHxOtYcYHw0OIzZcQR8noCViizQA1FFyh7ig_kzB9crQhWURRQWQ6eWnpUqVHkJMmrOjVxA5r7HRyDW3VFmXHpFarMwA7VJiaD4v23xgm1FK0uawWMsBEA4DuJfXCNlGUqhyBXXCvIbdOohdrg5oN1ycqmzxG5OajhEUKIbY8ykeIPoUWTOxDyxD0YXUW3LVaZqoYhgFl8b3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZISxadssBvZUm1uRNqSX-X_ezOONfmY0gI2lGIxGyjiaT_qJdnFWSWUBG_wRKb9-jULBrdIEkFxvp5ovKazmIOd5Xu0tJx-rzkxcgyRUS_G7hSLZLQSC3sSnrqYJr3k3eza8Hrv8x8PTuT94UUUpxdnyQXvv21Mexlolu09b0lT3ks_A47L_QMHXqZJI-0pe0CvRwu9PpcvKmU8KusAn67Zso25f7oqpxBC1R-8IYZP6vjhHUZEJM95ap0v3txjP8VVfFePvCphcPKSnhIYtRH1TOmRcMbsFgVUvZmjNko5Xi4pHuSgkPGgd9jR_NlooEm6447maNbV5OsfCEXFMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRzLXyfQ_5jC-8aDnhJu_omnGkQ_juz3dOSuDM6DNhcZTs90nMK7O95ajEz1m-lqS7Hb6QDP-orADttgHJPQWGVMat1vQrRlKF_phfUriJpwN0VNGntiAYm0sH-NZccJTEfg_uXrSVgJsfd0DdvlMEVPyiovauNBab8xyAx6KwUxv7fhJGod0akbkwG_EawOr5Lsz00v-mMea7pF7SJ0b8R4ysnSrxThYsNRPI3Q--fdPWtug3D3uhVdcncTbMigdVEMCdADdAFC0o6wUo2lcQqrg8lhx5225hXBPneyfSzmqRkbn8wCisF1uPj4b64kpTzeYS-1jYTPMYxHrIOg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itJN72H1ggLH-lfbsFjQc9vVdxulEMd6E1bWcbRRCnK5LIxOqzB6HFfdGZeLWDQY0Jm6ECxrasLuURK0xvQnSCWzyWYi6T_yX59uXQUAQBmNawj0vtBY3tN5AF6XdRLMbO19o2ocuZRMXHxgSyyPlMGOD_jfl6duXbJrMG0BXgvP22rRMvi4F_pvfbnrwu0_V2oRtBsa84vqLtXz_I7KYLU63ghCTzmGR9VEQsqoJ7Zv4SlQHyV4l8GP1JlHdwSg6e4Qn1v_K_SVictD_PX5pJYbMyif36aL-OsoUvUOlDDtSYnZ9AN3nlbACR_7klyNzXXvwjBr3T1v1BLS9Ib4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_YBqg9-OkrvyKy6v-XAgluOsPO2LXfrVGhimkrQyxzYW6p75TT1h8t9Zjkh-MrLGdh3sUcZr3ioHuuzKBZAbqOitOC5Ycsd3-RLmhk1deALkJyPl8GSjFLS9fFi1xgrXz0upQQ4fTfTh2At9Q0BbjtnWORc33TeJVzUdtB0cZUynQuzNmMfcu5RitLTHvedsL_Y9OYygS2nsAeZxDy82fpoxVRgbedSCab-FPfkPSn0DnCkVlf22pWCdcwTDXVA8mxoPiFGeDKLYvoKRN456GYGzhiA7J3EJCpHjsIiTFdbCBlWnU9CEYU98UwmGpew5kjcXpIRMV8i3r0AovuxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RENUFp5k0hzEHwqwnXR3rC2Rv_0e1N3AurSoPSpUYZ5JHs3N4igXtPUctVErKKqyf9cLYG8CEBUvi-50JnjxzY1t3VfApGyiLnTM5PvXYrYn-24kKFb3NygIDWOEipUB1_M5LUO0tNCNJHma-_kBgo13dfpqi13cNsUqf9sAnzXBKWMzEeH6zCIFnKmMD_xquWh2CoauYahyWBUk2DioQErjtbDaiKF7v4oqibNQAfSP2wKOlI2Ijd5K3Y-N8zOwByuwO4-n0dZuASkBTrHpMTuq19qH-ewUozDAhApFCRDZfLJA8THL64EwKpX4h9QGwVX-UT_rRWWu9_0kj8OAEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jz5giSyPHJIWHU3UUyTrl29j3pJZ224lzuFimmbucY2AYOcwkshyd_fcTi5OPSgqEZ_AhhG6dmuI8eFErKbclZRpTrexF6KbtqccG332I0Cmw4eh2-kDDDLgE1LCsqTnzrSIo0YQdnFsR9ybkVDJUpU-MGGFvI81OQlOLK1fzKLUI_Fnr6EBqumK-QAFd_b6n5jutEnissysX6G32vzD2TohatT7IwmJtzOl-rAu4bHisYhb72u4Hr7u9tMYsZOiPj3bEkIKh-qXcDUcgSwEML9xwYeHsllGsSmB993OGI-2Z3QAYwjKUjrkS1rEsxHWp_2RwirL4jMV46GgxhmW0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6H-3MFLR40f9JzdJQSOJK5nsbC-wAZSYhCzGzOJRaOXf8vNL8jk2JmFr_NhVOI-rBfHInd7d1W-DnLsnnDjkutNPtRyI-kKssoSKnWkdGu40FRh_d7mTEOaJuNJETtZm2b0tqkXXmqtjL4Gva0w5AutMEG9j0anneUC4ZbgISlB9NdO3YB_0K5mR5VG60pbYfFvsbaMzW11GEJNdwGe1tCucSyObHrP8fT7DI2WKpaot9JLXj5u-0jTQn8mSHrMc0t0iPoLB3PPJ1JCKoz6MiqcJ5JmgQ2Ch5MM6UXdYAGqXfMf2uDFM0Aiuo5gzXtahSLHvQJv6bgUue3UNesPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGw0UnZZ2swcG8vya_0HUUQGFr1o7nEQHWKB64AsscRQu8500Kubk6bOEDcoraVNqnQ58Vr9w7I76AUNMA0nZ_dLLp7gvEcasyQv4UJIYrIAsksm1LEpZ9k99zhC7X2DBCPV2G2NxogPd6GfOQ_aYhT8YyONmHBqSletvnkKXClyMD8L_piI_R4qXS_UEBLo2el7kxxgza_aSIryks3BKacg_m8yJJKYaIquZHeK2uc8_5juHElrhFEFhFCqqWXsIQzRXzLnQrMNMaUogILM_DqaI69Dg-o2CsXpQcwCvOK7C18SkPZP7Um_4Ipwl6zam4ex7LMovyPXrgJM_l9HzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il7tdazm2QIYfP76cMQwPekJvHGW7QUW7D_FbZdsHwD8kIXerqWjWp4FJIzVPIbvw39KSKZcOU_KxfUL4I-yV8An9-sPk8nQsY02bxk1Z7wjsjfCCYZQzbXJBPjAQVlQbfM36ZpodlEt0geH8VahzOQTZgZyejkE0H-eJyNuKull0W-OAPY57Axm69jjHX4ieHwbhdEAg8uX8R4w3d-CrQby-Dh-dxpz3BV9-p_NsIsumdC4FQRBm2CBKeeL_xMatDMrT2A-TaDaBT2iaUhv6qME3CTX1O3m9RlmZFdOvFvA6ap19iS6X-s8gVnYoXbbn33xX9jFOIRqNp-VkCxDRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHCVS3YUb8t8H81IlrCI0QGgtSovUV3YwuaucyKqNOH0L3UQlOrug-2XzCtgjKK_1D8zo6LW3wGJ3I2yyd05YSOpEneLQkBLseEmnUK1SFgZDztcixyP1WEecVYf9ud0FF0nvLDw8vC4LWv7VjNyFnBL6IhuCPJuOaF_H-xdUVGX_dOAVuoJLO6X2iLoQKglVE015FLv88Mz7aE1soxwquXllltCkvr6KEWYvzzvdXhPeWKwBcWQ335qWlbn-c8M00s7Va5mpoRkohRb_J22Y5n-vI0odozWk9qpUkXEkZevYHtTJiiGrvSBpxMqBsJglBV56a6oaJAkMis4whD8jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmqJRA6Rfg_Ty8bmP3FTTqycck7XfWP_XQIbHrxv5EotaC-iXjgJA9tyA3SbDNXAykTEv-3NlKu26z_vTtVMaVnoFOvNqFIALJtYWHv7EN6Kk2TXgIHw9VXrbto7pDGGwH0FtXJAt77m5-h72iTmACMCJ9L2ItRMmBUAeUUD0zeaUQH9P6fydL9NZLfkYqV7G0ptdys6TlDITfSzcUSLiR8NYljqK8swO-vVjDux31pKZv5bszK0lyhn41T15ciqXYmW5ZC4OL4LbkDndzYFrzfe40L9SB1GZ_QGu3tJOm_gEu_An-275vJ_O0pD8eEjknw7qwoDYigCLUN6srmOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWXKIbSViQAua3IuUWBW8GlY7YTUOuU2ZiLpidIXxXja48baOLaAaEUyYgq05gAjryCfMDfK9FOCj6MelOOq3nJ9HW7UbsIvgFOwl31bm-oRsnxNTXesBv9d2qZyWB9qQL3sB1YQ40E-vw9gRzcLgQx24C9-LULdatawCB_k47sHkoMTcIWAty3RydTV6g5ma6wg1x5yyBmgCFWM8PHxFVW9q6bfjdjIGqcB4k61YT5CGD9LkRXaLsjme2fJnzRvCDCnR36uOj6gwmaWZ3In-spb8Tf-uVG5SsxoCK2bBKdA3jPvEe9bSFnxiMscNDKsuouWhiQ91ZaYaZczEcUhsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEPfoIGKFRgh-lFrxhRKg5n9elnNhPs1wnupX6mlevRBldfQuhfQBDMMWgt9jh39L1lsuBuM4abCx2LQjJw-bPYEi-zp0hcj-l7wN1OAOhB9NP59OY7w6a-BCFUyMGxD-DwrNDRNCgflp4sl_GHoVR-VOaGv8VCU00T5eb_KmMdJTJM8FnikkvHKZIh1NlQgO1Fmd_FSnrddPe2-GzK7ESHopDQL89WKzZJDxi4HCezFAqTaMoZfZKE3Qdb52AYgMYsO8zo1Buh2-obT4aaAA21ilozX0yyUcg2MdZf7fp_59neTogTTiZ_klC3-5uUe1rx-kdcsHqPQBebuYeh_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m19Noi_zH-ac-91ILAeebmqPHdcxAs4en5RBn2P0lTD616VnQ2xDIiDyNVqRK-aXGBiFMig0LMYcmyzC0l0X76KpL6pFyN7CCjQR0kHckZKcQchKZ6urTIdBaI40S0BFdMosqMaKFchzYyIk6rdfF73i4R_C6dLU1YF9MnDOv4SDvbV6i-2ylP-4QLZCbMQLO6svUzxqw-7uVMkPuX_DPtJRkZGvFlZu1SLUGHxY8L8Uu-5V-ps8FKj1d2i_jmGYwHgFXrrBIWlDbqJe1rLb3xVoHDZFuxCnSksiG9ZCEG2b9cHNVN7n2XgCU9gL8qhivQk5rK4lRCcgtTa4bq9kPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXo5bxfzpzFCX6xTmKcKhODNTp4s2BH2US18sIKDgV_uNnxQxslW4oYyTkofNMfjRhl6hmcrKDSrb8aqr3nJrQk-yXs9betj1RpsIJKrKGGBsdgaBuMV-m5XRgg1u7BIuK1Jys1FUWIv7r5ao9Y234Q55Oder8kwhS8AWwI4thnsJtEnxWSp8pniUE8TkfT4SgIpP-rYNV8xDgNSiIERfW3rqXjwVoXDjxuFIj_Q652S481dfuGg_hw_OdA68E4gJztNeDKzcyxOgVyISwBqhHWKDhlDwOrR4vThBsHV9RNnmcRWh5YTdPcNat43dCt2Gj7FCCh3DZR4WwywmD_Srw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEhQxO41L2_PifzwjmceFHlidyGudPw5V_-HgU0fkcom6SLEShZo0UJOON2Wqg-S_Ml-60yU8OnkVvWEBEiDPhh1qgiAkDEjzf2q4_62kpoVc-Sfh3yuanEnZkU8c5jMN8z3vicRSiGsta0lUafYO6TIR4FfT9Zxyf66NMGgjq-klHX8f7WuvySvKB7d3lcX7HWu-nnQ-XsE6jGaVrABpkO0ploTYe1DPHNmx4tCUctBYQECdZ5Pe30GDtxHvbuJKauqB8TN2yy8S8Ta8DXWwZBcnVBuCjuB6ecfZrheNM58HPAValDua5wXsxAE6W-RnsFRHNNuOaej31POViFpJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ4fx_zHHlCSIs9v6G7vGt01eZ9GdQvJGKpA1374FQZ4HqP1_2euq7pQsNAyxbyFqFx9GLNMRbCL9SAsgPhwgnSRM80a0sRnB0IOzdqM-fiDYOfP7An63HPnTTTSHmH45ebj7JxC0o4f4eorhx-7VCbC_ZHIf31rcvaM3A4UGwF66jlh5ov0-WXZ6iJXD1AuBCDeq5Mr4Gc5773P9awyDIyGnqW05O9D8JOUmXnL4_Ff2kQPS3LboPxJPY3HC2Xr02lXIFyJEr3VIYdiZDVUvAHbQkmkvZQtxSrkglFjSoquoNPMN5rICxrWGXKmL7a84K4zgrxwpcjf-XG0wgdriA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcIucjymjJv-Tyu_WU1aBTvJPFW4lquf2ZFXVArw04UuNwqV_Kul230PKja5dAwAOWJWIjuCFO8fiRZiRNyeqrh9yCGhp-mhp52GtfQagpVZrDxbmlDjkHdfW2_UpdIN6H37krplCKx7VHwyH9BLJu9T5cGRc7DACaXQjAs0eX2cG4u4jWeal9ZqCk3-2ikJGWzTyRYWkn-OrA46VtqRIi4Ju9iCPsBCqD4O5LOU4x_r-neNsr8ldRGKEl299uFPERUDqZS3QrEKHOFk2f3RdgAEbLuF9VYHb4qth_i51VoEuqsbHtO_t6ALdBZIiKPNU7WNGd46YNnwxwPbphbmiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiZkqxc6e8IqoHBv1NFfDmw34Wffm3mxFvno1_upiCUXbA0TkOqqFNqc6A-VxGKFZW1M23ijOjHPhMhvtUfGLDUGHsEwvRRrkX6Qr8IdczgWdYMIjf9YqmHp5sSU1VfSLAssZmpYuS9ZX660DnF7iO5KmgBhnGxFPjc96t1RASrzINrVyeP2RlB03YzRMEJbdodkFvMUTVF6HC8mFDi2oYyKZhsj2sL5PO4ZBUtOxEsrT2cGorSMqiA9V2_MUdrURHLrLp71zKaWtjiV54z4uoTjnl2YT4L8zelUD1nKBWs7e_9CYMKMbVHkfjAG2CpWGMQDsm82gV0JAyv8mIXYYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dImo1oC11OKvHJyKwfElnpXM9Hhf6Uxb6VRR5HKaZSOr2TPNa52wucTpdukYmvTigR4mvfXsf8qN7c9LmpBIFAKLxGw7be6LCB-GW6v5lzlcTVpgzRcPHJ4IXl5m4EN0cWSOKbqenZNXtzana-YzTuXyrvZsgtNxKqMJH9M6if1owvUJhYiYRSjAD2iz00fUH9VcC5hysGRDOsk2UrGqQLxB_3d6jE2stnN_WJjx1ZP1QcN544yyJOEiYBYCyIpS_DYFFWGbfDq0BjhqrHoR6f_FFarHiWSCEErNwlTI64l8eDQhgvIzw_KidHUwMVu_rbJ6GaUsjZcYyGgkrg-1cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj5cKoJbCV_trYSqG3wGwilppPlnvwjBqZVTueQSnPaXr56jYBJzBsqPVJfLz0L41Qbny2FYAUv6JO5WSlZ1fpVGTWD9QEulMr-hA2tKE3n2pe-7z1PLZIeReGXcYGU4zp7o0unsl0-OmDtcXv7uZ8LU2covkkdy60FR1lJRIKFeekqRZItCWeIGeDQBzd_GvKilIMp5F48chu-amoumhNQyyfNPIpUfXTkeVmnNK8m46NXw1E-fO1H-TLeHsO0u6hmqxt1lUgewS5AOQ2Zt2Y1pjiy1snyrLXrwVUIDlocyJnGo3usI_k_P_xMsZu3KUsSFsPjeu97PNE3gVA6OOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=N_gM1xVN77syeowDn6ksW12Anm4E5cz2azuOxf3PDP8eHzuYM56bP_yTa5iRAJXOoqXh56St_Ef6U3nT7Uoo4noRds2Jb420EgDxGKKAsZj1MSGHvoeXDztsMnXEoR7apRnC4GvyM7zQdXNmvtWtl7y5DfFX-3Keg5a2Z11gfNiHlRsLiUkrWgumiGo7Ya7mrlkMzybzbGgPEaawyZlZ7-4KqBjJ5U_m3dDm6LOx2yKIT1YWnwHcK6fLUlwp5XsX9--wgCQzc2ea-dtNDiW8KuOM7JsqVkXv_cVPruXB9LvT91KvoqtBbkt2FVnkwDiAJa0AmwgO8g9yLTgNlu-Tsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=N_gM1xVN77syeowDn6ksW12Anm4E5cz2azuOxf3PDP8eHzuYM56bP_yTa5iRAJXOoqXh56St_Ef6U3nT7Uoo4noRds2Jb420EgDxGKKAsZj1MSGHvoeXDztsMnXEoR7apRnC4GvyM7zQdXNmvtWtl7y5DfFX-3Keg5a2Z11gfNiHlRsLiUkrWgumiGo7Ya7mrlkMzybzbGgPEaawyZlZ7-4KqBjJ5U_m3dDm6LOx2yKIT1YWnwHcK6fLUlwp5XsX9--wgCQzc2ea-dtNDiW8KuOM7JsqVkXv_cVPruXB9LvT91KvoqtBbkt2FVnkwDiAJa0AmwgO8g9yLTgNlu-Tsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvFB9YGNjc743pYPgxh6NmWNRfKtJevHMNsLbMK3cGpgsurHNQoscHFFFPOuQh02YCcXB_fEB0BgbabhGj4APxA8vIclsZewDm0YBBvfExXsLWHgAYrBX5WefU1k-xsq71fa1ZrjF23qaYGSv4DCYklhrKWrugsIph9OytezRY7uJ6tyBcWEnA5Fi1S7G5rdEPzINo9I2U5l3QhOj-Bodb-My4h6jIGPjLuAcCrdAZGnHYiV2y722MmC0V95zDnlWEDERcZXnmQzUaaXQOV_i_xhpn7h7ALHCbdQ246wd4MwDDi5PpOgruP3yU-AM8DATwkXKlRBNEEbHUmPFBQsrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_RI_WpGx-ni_89Dx3aOwxBxsL_wpzSxrgIfEOpvTY4axtTrOYR68HuA5wY8Kp73Z0_y6kC8PU7YvexRGlvcuQrlM_vtmDWlTDdheCBm1YkpLRGxp8rlm3DkWdmpye_F-wwFKYlXEsNYh3X5sPqk3IKVkkfCe8f5yefMKCRekedFsylYkTmdlFmKLjX3Czzv1yUXl67ch2Io7hKWUIeIngYOWfcmzTKeuQVz-Dsf8wX91tTIgyMIqYbGgvgZeH8lhXp1R5bq8iejpUnsB2gqE92XJ8LHXXVAlAMPfOzIqVnmuwfrOZp_pps1mzDxIYMJS_xMT2pMu6937IsDSlan9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ox2Xf2la6RPJO0Lece8dM3Xhd44J3R6k5P0Bh5MCO-81TAOYLjzS2NpvgAcFU_ejk1XIupwJBDfXsTVLG-bmIli--b0RiARl4HImOUFxBZKdEbZ6EcVXTt1ImRLETMC4lBPn87lcWQ2QzcwRzYb5A-_RW6wqtrq7z_geqaIN0a-TuNxSk7WqvbVqXgl0xLf9naQkTzztlD4cdxWQCWd6A0QMCsfMAqkVh5C-PkCYCzYuifCx4bgXjuNtJPAlBsS4gPAG190wW3ct_M3CozOBVQ37HptP7_V0sob1uZaoLQ9Ji-_xUzzdE74fZbBx2X1IrjINLowP9nsfItk42czdKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heUHwH_65auJsaIWabIpYbT1lXzerevuSwbB_CrS6NL8a5A_6XleIQwYCVuEiuTNuirHlf-tMUzFKfQEcbikzJmXbdWH7SlUVAgLQuZ9LYqM-WCH8fgoQK_TLU6UkEhz7GHwCN2LrOsHbG2Ajj_Q7ZQnJIKtA5jXpsZ11Y9EMjLNA-woQEKU2PizB56-xxnbUBjdAxeuf6tbwLA0-1WYVQcO-kxJUpVflvP6woiuw4UWUsqyM9kH03N3LmEi2QSXJDeOfPNmINcvtp38gMaFnORNyd-o6RsN6kg0If0b1Hsdc0Af8hPzmTVsxIQ-iHw36_K-EBew7EAw3k3b5uboeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQMGR1sA6Sll2jVIP2L3-E-a74PzrU0NxUqmiHSbLtfmKHYSP2MmjDDK5yWTn_gtA9QbLrknWypMaRiAph94JtopIYAVxEqQ71ildidcW8aF367ZMOXRCgwCUzNynTrmI1SZHc__NdM7742Yf18UNbe9yjoH2eD-vnNo4rB47v0sR3HeJS0gy4u4VFtihouwQg9VZnRzTHSLkGOrcg8BUSF2mJmq-uAYYOBQRwAzqEZQs5RvPz4eqJLcgLTh_qnqUWwV-Q9TTdIUBJD6ceZxZAhWoAia0BaoUptn3iXsBxSRXD-_ptTgGVq4dfRV1HeDbmZVzUkNDGhNhUd4AXxT4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4H2LNSMkqCgRaEfJTfebpq3yqwXbVbsFVYt-gxSTHWW8xOY14OAkqI3zm2Tw8FqdTki2STUD_sPsZT-Pzl-p9b_0_PORjFof38kCM_i5oOY9_WbEDVs3BkuAinzBuv_Wezb2oqW7i9ZiDV7yTRPntjfI73FVUmDb7Y_MwMKty6DGNHwY2dPhUOb44ADswMzrK5svg6RnO5-Tvyfdss0dD9a9V6a9cOOB_wx68-bvUYR6t5XOR4EpSbTqJmAyLJfgAtHiJ8x3dPv5kEhWF0VqPdZ3bQgF7BeiV5in876GzxzJY4YjQ9c7zijjQThSUDKB1Y6SkPxVxqYauA5in4n9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0AUpwo42WN6dUpau8ZEyWlORhE4DiYJRHBFeygQuUaS4jM77GFG2lQsCMNTrpJPzY65v6wdAU26XeT62r4NF59030gxS84WwT_uKlTvKrT1XzUnLD7IPqBjQY4au-70HYGIhOenyOR_x01F4rzW-49f9Lu9Xc78NVLakpsRhRqlHZ_mepzVzVvoxK-FoTaBj9fbVr1_ICZVhTjKHW9341IOr2JWcvD4wdBHgdG5WOJaHJH2kw1zrbJyNfyC4ZS_iaCb9DePegNXqBWPREB03gFmJqVXFUOYeEtEMBuRrHQQ7I-Frr6d-4-bsBDySfW3OWSz2o57Fd-6gL8Snf01AQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRXezq0apK1e-nKbG_1NEV0ltM5efFx-huVBiQTjoNzSd9gXtrhXFtNURnrCRz0uszdo1QSbIwwcl8R9VrfT8qH8fJWKaW7lvvYdKNeQgE1lCRgJ_KCQYoc0DJTPAsCzKkLmJ1WJf3DCtU4gJpCgB6eeL7_L3ZN9SFF5TWshvX3iV1wu41aWtYQBHQDSu15mHeW5I5WqTcml9P-G_AP87SYYolI8dZzkLbG-rfzqdajIIvJCKrS7FnX1GcMc89ur8fllQuCB5SdQEwParB70vrBDqII2Qoarf1uQdX4nFAEP3MRQhQcNZORmT5SuLrg19AkZMO9k7ZaiVWVDgpyWew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyHq-Td_xbsTW7Y387WgdCnNya4-iwWw0vYHbXWk1_OwIdXXFqAOjSiYOeNicBh-SWdX8PBb6m6vd0oRDmzmPPZ3_SPKCLLd4xCYRWQg-KXllGUQpz4-owigu05Shp7MsZum_gYbXJQU-aiLRg-Tjl2UIG4ScXZrLsOO3KuOqRQGcHAUINs_KQYi0MlP7gVgomyvd6SK2i6gV2Ux6RPGpU6F-t2faPm2JuWc9zqbh8O6bEnH8n4ufCeIcDvHoveBNvDaWHKf_SRQQcHNN30DPelXaVkf2ScdJ-xnqEFMz3gBJ1cuBs_zvm_BFnvyujI6NIegUqf9vmEorqmOceTvIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLEbteM0VzKrPOcPj5qDqk0DQA_kM-oPv30dUMFySKb5_pRlZjKldC5m8OuEKS5OylDB1iwD3OkOhNh-Up22MG3oFJKKa2hwR4lLB-Dj6wxnaGkUnPiHwNDymJYw-9HDFmIMmiGWjkKWlIUElvdI-v_e8lrgn87lLdIyIBLtsd8nKBrcAxJMgw4G95ZWXw5Jq1uqwGA_J7s30U1ESu8EsKyOJQ_QPALXruwQsyWu4lsTzt-JoMm3YGPZksd2e8XyyrGxCbLgXkB9w1XUwSO-zYHai9iyijNdQXgutYhpEC2M9bye2jAeZIa3b_P2d_DVKr66Kpq2lnhDoHVKOLkOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2kmSUcqBDHOR93rgy8hPKbyw8j8Ubc4nWOmE2O1BmgkTzghFkO_Vse_sAuTX81A4CzYaZaemApsfgkuT-S5c1l-TKXa_urp4T8Uq9IZgkgDUAoDzUyKsUdRioUTOnSOm-oB3NNq7TMF-nTDNCFrRYpPYYMOrtgCMSREfJvV33Iql8V1gBZgTJo7Pr7aNivUiW4jAXF7qwgzCl4b7iZ2pYYQe0JoZhEZz_ZNPT7Vv5-IGxjXprMHFYwY2cY0tHUwJW5plqWG4WTGFFsT9dPvgdntHuSLtmpE9xLE6jfMQ_zmJFispJObRUfQCNL08QB-gs3-F_ujr_T8zJdqK6im7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyR4u5RX2tUi2PxcijZ7kfmCDD4y3qUIRmcOkshQC2oiMfN3GOrFuN4FKNoY86SmLEa2owNPnRAttN9E1SaZCi9qZs5xOXUke9GZPBgGAF2rBLl4iMeCwjKowwYKnZuiaekYXeSwxjrNYsrjt7-bvHiP1GkHIoIuD6yS-bfrjcBxuf9oliQKQ5VhPq-Qjb_8tGKCPwlkj-qfGod76cOS3kEaByXXw8Uh0dMS4xS-kv_IDxzcoX_wKw-iZwoQ-kmcySM_Thc4zy6oobaME8BlO6b2gpz-nkIQNioctPWgDfEVMaluMDiZ5h1tK5Uj8u8KONZV3nq7ZymyHHYMt8f9Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHxbvjtVrZfuszdsvr_Y1sfTS71LHvJ2uIBblcR8S6vdMWVk77HajIxE_fLyhNVXnm3cJpbu03KZPcVKhdVj8QQPhlw-U1PStiuN43n68pmiDHWL0S9-kSicTU1Kej8Rr5BISud2rVBIID369Aea1c_k94hYsx1efhqTFxLwDkL9uCSRT9qtScMyid5I7gf0SNcYOas5YAccA6AC9es9fj13_Ubv3APQkmGSE60CDI8jdBlFQKGw2cXsXzBm-2htgv23QDsaiiG6edUR1-gwQB-WeXxHwKFPPnfpAW9_aIT2FDaCo9thmwFSh0S9lQS4wm_r0witdiF8VId_I6pL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
