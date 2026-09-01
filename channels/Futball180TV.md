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
<img src="https://cdn5.telesco.pe/file/kVPcs8LmLfkXZhz0w2Rhq5r88gGNGhPVrfCaghVghIPdy4_ff_xCDpmWDmMC0ok7cHb5E6nA9kIE3kjSmwko865LzX-QcVtKzZ37yNp12sF_pU_noeJBh-rKqVf-kNyh3dPA5T5gL2A5vG372j9iQ8T35m2u2hGWybXHDimd-Bh1SHequrgRqmrcwVXhIG1yEy4I7rRpfXUHBq3JB-pW8da0ktfsABrlmn8y1R1LLfzkM2qdOr9OT7CLRg5bs8R409YmMao7Ur0ppIF09PYpcah353HadHwE5B4OttV2PJhw0svhDGn3jgdKammbAajyW1rX8aguS-yi4myA38prnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 432K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 01:22:27</div>
<hr>

<div class="tg-post" id="msg-105314">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگه استقلالی هستی، به هیچ وجه این کانال رو از دست نده!
⭐️
💙
📸
پوشش کامل بازی‌ها با عکس و فیلم‌های اختصاصی توسط خبرنگاران و عکاسان ما
📰
اخبار و حواشی داغ آبی‌ها
🎁
🎁
و قسمت جذاب کار: هر هفته قرعه‌کشی به همراه کلی جایزه
🔥
🔥
اینجا فقط یک عضو ساده نباش، محتواتو بفرست…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/Futball180TV/105314" target="_blank">📅 01:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105313">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwzC9XFp4k2mSfu9-w8192ZG2T-B830MTFrmX541-eYzVQFsnp1YVgyPDtHTbbgJ2rp5NsjuFRuhHIEi0_fA3aEkLAK4vpqF2qN9Hun6WUq1b2UpGMTx_gdes0vNYhzV8-LDoBQaGMvNY1b8_HEenENewFWFLBlDbiHsdKUjOtR3cAtcijNoH4L89VR32GoB9hh_riP7P8RjbRqKEz23V1gyOXBwpUGXvjwpdOMAmC5FCzjjKW5BZ7CcP7g4SWPVv_IgpbEBq-AbRvtjtPYhQnmaGTG20pMi7o3U5GNyQiz8BvRET21XLz07SCJ3Q8yeZ16a-RGSbJNNT6ZjHAc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگه استقلالی هستی، به هیچ وجه این کانال رو از دست نده!
⭐️
💙
📸
پوشش کامل بازی‌ها با عکس و فیلم‌های اختصاصی توسط خبرنگاران و عکاسان ما
📰
اخبار و حواشی داغ آبی‌ها
🎁
🎁
و قسمت جذاب کار: هر هفته قرعه‌کشی به همراه کلی جایزه
🔥
🔥
اینجا فقط یک عضو ساده نباش، محتواتو بفرست و منتشرش کن
🔥
با استقلال... برای استقلال
👇
💙
@Esteghlaal_twitter
@Esteghlaal_twitter</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/Futball180TV/105313" target="_blank">📅 01:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/Futball180TV/105312" target="_blank">📅 01:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105311">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
⭕️
با توجه به نزدیکی به دربی پایتخت و بازدهی فوق‌العاده تبلیغات تا پایان هفته، اگر تمایل به همکاری و انجام تبلیغات مدنظر خود داشته باشید، با ×تخفیف ویژه× در مجموعه تبلیغاتی تیوا با بیش از ۱۵ کانال مختلف ورزشی و غیر ورزشی در خدمت شما عزیزان هستیم   برای هماهنگی…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/105311" target="_blank">📅 01:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105310">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/105310" target="_blank">📅 01:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105309">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=czWeYcGuHu_CPc3U8Z2hf7AS6tUl4coJlKUvq20UF_hCEIVeLjUwyBZXFjv-XpER2HLm6GV1Lx-IuW80hs08VI9DBNJ8KZF_EEZGBSmIbA230Swx_Gg8_niybH8LmPV9fCgvYgKWOR7Z2om4nz2n3gztq43dWCMUSzPoZheJ2SSM8mIi28H1RTBPYec2H3rMo8cFZAAX45BgrGaiCYdMDmt-BcTL5LQzBLM48iEJXeJeQiEFukV3JdcwONpPSicV44i-llbx8CNhjTvC3qn4eobSdedOuEG1XMlu12SCnH9bDMfGkt-c2D_GUDYJ1wVlqET1_NnpHvCb0EWmvQiRjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=czWeYcGuHu_CPc3U8Z2hf7AS6tUl4coJlKUvq20UF_hCEIVeLjUwyBZXFjv-XpER2HLm6GV1Lx-IuW80hs08VI9DBNJ8KZF_EEZGBSmIbA230Swx_Gg8_niybH8LmPV9fCgvYgKWOR7Z2om4nz2n3gztq43dWCMUSzPoZheJ2SSM8mIi28H1RTBPYec2H3rMo8cFZAAX45BgrGaiCYdMDmt-BcTL5LQzBLM48iEJXeJeQiEFukV3JdcwONpPSicV44i-llbx8CNhjTvC3qn4eobSdedOuEG1XMlu12SCnH9bDMfGkt-c2D_GUDYJ1wVlqET1_NnpHvCb0EWmvQiRjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
تصاویر دوربین مداربسته از حملات پیاپی به نزدیکی یک مراسم عروسی سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/105309" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105308">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAMjrewbGufGPB0qyWzC6k4uBblf56I8Csk3nVMXofGVx0aX_O58jby84L16o4yVLZAdooo4R_N1u8xbp5J4xq0GWqejV37uIyzChxA7Tyg8KoU-xPFxXTve5rvAfgGyJaWz8fEoDh-IkbRYBSjLVUHcA61gx3j7Iw-HawW4b0LybL0JMWEieCSqpguL4PY8NErcJTWkSWDMEwu9Pra_Nmcmn6mw4c2bUhfdIb7hvC6nQfZSS8hZoKT8mqzUDuBabM9JVgmo3EaSSdHbh76Ld4kNz6A4HRAM-oulQIBJYmmQbD2V7C5V0XfU_iTQ9oCKLpUmYQlT0yMtAMCcoGNquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/105308" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105307" target="_blank">📅 00:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105306">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180
#فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی اطراف استان اصفهان نرسیده و این اتفاق تقریبا بعید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105306" target="_blank">📅 00:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105305">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=bXOnqYBsbgI6LIJEQ4ruK_YP4NHvhC5Vv-KExsrFfbmgEKyulWonUrN89Q8kuKeetLkKfLT2_KdmSlXui2JFNdRVFSMmASmf07FUBqYMFdkNOV_2lVQBg-1zZBcvUlBGXn9KWjzuL-GLUWul8_CdobfaXhFEccfEFWJksPrHCmwj7pZFmGYb7pTFqmAH3gpugUMEzzmSclnZvX9jaoOPl7VA3hZhvRQwbZ1RFKsH0gylRloBRMLwWlX356eKKCrqxDGLjJkNFrtK2SqkUKmfEYaycE8C49Phdoqv2fQySRZWQ2ElvQq9Z88W6oX-Qtq7r6_eqfdB7rtZP0vw1RrE7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=bXOnqYBsbgI6LIJEQ4ruK_YP4NHvhC5Vv-KExsrFfbmgEKyulWonUrN89Q8kuKeetLkKfLT2_KdmSlXui2JFNdRVFSMmASmf07FUBqYMFdkNOV_2lVQBg-1zZBcvUlBGXn9KWjzuL-GLUWul8_CdobfaXhFEccfEFWJksPrHCmwj7pZFmGYb7pTFqmAH3gpugUMEzzmSclnZvX9jaoOPl7VA3hZhvRQwbZ1RFKsH0gylRloBRMLwWlX356eKKCrqxDGLjJkNFrtK2SqkUKmfEYaycE8C49Phdoqv2fQySRZWQ2ElvQq9Z88W6oX-Qtq7r6_eqfdB7rtZP0vw1RrE7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105305" target="_blank">📅 00:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105304">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=fG7zsvtibOTJ6Xgf7J-cZTtlXPcxgBmI7vZfpk1ll3HbyU4eGck1FxBt3yjgsZ6kfah8Ikd639Nxx5iOIlY7ZFj1_OZpzID6_uUPs2hhVNl1KpDSffA9iZnOEVoOUMgBjuxzkMfUKIVE1IbscdZ2fAnzUi3JSEX21FK5fQ-7vITsqigYoPdE_THtpq0bnP17LSZ_jNfbvx7YVWg6QSIQASCEGMVgzuSe2VeK7OWPLxzYtdJoemTp26IOqdUm5t6dEv8mz6m5eWFFKX3ntEVB-LhY6PO4kjj4lqLTwBPsgMTmhmyPZalCfQonuMf7Ryj4XgEnSsrvfzLVDz5tqTVdbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=fG7zsvtibOTJ6Xgf7J-cZTtlXPcxgBmI7vZfpk1ll3HbyU4eGck1FxBt3yjgsZ6kfah8Ikd639Nxx5iOIlY7ZFj1_OZpzID6_uUPs2hhVNl1KpDSffA9iZnOEVoOUMgBjuxzkMfUKIVE1IbscdZ2fAnzUi3JSEX21FK5fQ-7vITsqigYoPdE_THtpq0bnP17LSZ_jNfbvx7YVWg6QSIQASCEGMVgzuSe2VeK7OWPLxzYtdJoemTp26IOqdUm5t6dEv8mz6m5eWFFKX3ntEVB-LhY6PO4kjj4lqLTwBPsgMTmhmyPZalCfQonuMf7Ryj4XgEnSsrvfzLVDz5tqTVdbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جملات قصار و واکنش منصوریان به حکم انضباطی علیه الطلبه؛ از جیب خودم خرج می‌کنم رای برگردد! مستقیم می‌ریم CAS؛ یونس محمود ١۵ سالش بود من بوندسلیگا بازی می‌کردم
❌
⚠️
در شرایطی که دیدار الطلبه و نوروز در هفته سوم لیگ عراق با برتری ۱-۰ شاگردان علیرضا منصوریان به پایان رسیده بود، کمیته انضباطی فدراسیون فوتبال عراق حکم به شکست ۳-۰ الطلبه داده است.
😀
دلیل این تصمیم حضور همزمان ۲ بازیکن الطلبه با پیراهن شماره ۷۷ اعلام شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105304" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6jNj0153gp1TpkvWA4GqpI1Wz6cLmk7p8o6cczuwMUUzWKvt3Yg9j9cnKyNxKvJulFzXEnL1vAktJ4j3JhIMsV9jUA-SrZILZAH0epoMs5Yq2S_Eq8Uwo-BePXn25-DmQRNVa-jqdIIpFK2cc4Ut8XgKALfq44Fuw7GNYuAxDKcTNiTisVPd9SItpt00gqTm0hjdjjEi7NlEBIzZVnVTnoN06hiZn6lBluqis7DCdi2svnSpAb4dfw94zax5tBwdr2R3Oe56sBbMiRKAl-RrZDVbBazMLG3MtSOo_CwozkXvWUvjUyoF_Hh1zQxl9SgtVVjMKsWUiNoi_JIkA-RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسمی؛ اندیایه با قراردادی پنج ساله به ارزش 65 میلیون پوند از اورتون به سیتی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105303" target="_blank">📅 23:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
گزارشات فعالیت شدید پدافندی در شرق تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105302" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👍
🇮🇷
بانوان جذاب ملوانی در بازی با پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105301" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f706e532c0.mp4?token=h236NRUo6NE9asCMoWNXjv6GrxnY-yg5_RRd6Ml9W95xMk98jjQWRo5h9P2j0PRCkExQapjcW18OKKAZY336Ren0I9Fk07UjKkjWjDnjaj9re2KV8idvMl4Gn31xfnmUf7v2ZwSYSgs3UUqopY10x6tZU9JgBsZn9ULy6fRV7iYpWGUygP0HoqkIuKllTgoIe4it118DlTbbWv1ZxMEt-waQEsC-1OaDaBIXkwNSbZmZl_HMqgz3JX4md2dqNJ3bgjxQLphu2hm00PVMGNmzwk8kpw_bvvsde9mwhwfsczfaYdM69Prhsh9tPd84c2nz_WNEHcIR5eRTjPB2-YMT9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f706e532c0.mp4?token=h236NRUo6NE9asCMoWNXjv6GrxnY-yg5_RRd6Ml9W95xMk98jjQWRo5h9P2j0PRCkExQapjcW18OKKAZY336Ren0I9Fk07UjKkjWjDnjaj9re2KV8idvMl4Gn31xfnmUf7v2ZwSYSgs3UUqopY10x6tZU9JgBsZn9ULy6fRV7iYpWGUygP0HoqkIuKllTgoIe4it118DlTbbWv1ZxMEt-waQEsC-1OaDaBIXkwNSbZmZl_HMqgz3JX4md2dqNJ3bgjxQLphu2hm00PVMGNmzwk8kpw_bvvsde9mwhwfsczfaYdM69Prhsh9tPd84c2nz_WNEHcIR5eRTjPB2-YMT9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🔴
خداداد عزیزی: داور عجله داشت بازی تمام شود
. چجوری 2 دقیقه اعلام کردید؟ وقت اضافه را کی می‌گیره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105300" target="_blank">📅 22:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f17ff9c0b.mp4?token=aymtm9CrGXUHizv2_OTEfwLKhOU4pEDZacdsT5K7o8dMiqMW1AdM1yq_s1VuIuyH4hfWXlr--O20wRvVcMq0a67C4ugpIq8mz4Qx2K-LOhn0Ddef8tfO_R3W047BE-UP3GCZjWXvu-yth6jwNau4gYJXgEb5QhtJCO3uJZimet2yhIhhWGso0Km9wowbk7iodMAoAiNMTI94uOvi_ZBa4wiy00RTtZPaL6L0zPxzVlE6j_eOUqk_35VCeMKsh2vHUcXn33Bz_JYXMV337s7rVi4Q9aEf21VtCZ6n9w6Iww56QNZ3Nt32Z7sKw_F2_8n5ixypEfGCjgapHTIlBf1aKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f17ff9c0b.mp4?token=aymtm9CrGXUHizv2_OTEfwLKhOU4pEDZacdsT5K7o8dMiqMW1AdM1yq_s1VuIuyH4hfWXlr--O20wRvVcMq0a67C4ugpIq8mz4Qx2K-LOhn0Ddef8tfO_R3W047BE-UP3GCZjWXvu-yth6jwNau4gYJXgEb5QhtJCO3uJZimet2yhIhhWGso0Km9wowbk7iodMAoAiNMTI94uOvi_ZBa4wiy00RTtZPaL6L0zPxzVlE6j_eOUqk_35VCeMKsh2vHUcXn33Bz_JYXMV337s7rVi4Q9aEf21VtCZ6n9w6Iww56QNZ3Nt32Z7sKw_F2_8n5ixypEfGCjgapHTIlBf1aKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
🇮🇷
همچنان از بانوان پرشور اهوازی در حاشیه بازی استقلال و فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105299" target="_blank">📅 22:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=frZ5gOD8rFSi2J5YMgrh7zoxPDjwyHvtWqICIVH0lAHoEqnSbtvJHll9S_4wIA-8dcfkoEq6oaArSpnTXq-TNgGD61H_FUo4A-u2hPKn7yLgkKwdRlrah5z5AdKjrfIFpsKJ9QHAsZOnh-rMby1bLbsRyzXjTm5k84u5ATSV6x0Wcc3gIH0Cj2a9VmqTd-vFESKEmU72XJyuCJSWUmVNju7eToCQNTi42YCgGYeDk8nteRFYrOOz-AhJWZTkfDTKgxEcMNKEaCEs57Nb-b9D34B7D4kYygLFKLL6pnjZ0xbRy-ycpzNcncB1-_pwy21K9oAiFlHVh1jFc2M-HFtU6izFRmKNztIolc52bXUFxDoyxZ7kMECvZAJl5341UPWlK9YMkCgl63VX61kyslSqB433fXz2KrOO08UJ4Ux6EqDUhHlk0MsI_kyhP_jvMTSp7FbZjvleQ_DLSZDXxXANa6uzZpgGxag3GqftSKTf0z8eKW-xWCEXnyAerfwoGn11AC1eS_hOw4RmfnDYtiMeM9-tPmjJX3NP57QlGpZwo9tF_2fV23pEb9FRjF-9f-1-gWJQ_UrqcvIM6hFQibpLdyXqo3t7TtG7Fk2OXL6UMwAlouL9smwP-EOnw1Cz-5lthjhkduB1BgnsQnPxxsi03st6I8n4J4WRYnwwO9Y8A0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=frZ5gOD8rFSi2J5YMgrh7zoxPDjwyHvtWqICIVH0lAHoEqnSbtvJHll9S_4wIA-8dcfkoEq6oaArSpnTXq-TNgGD61H_FUo4A-u2hPKn7yLgkKwdRlrah5z5AdKjrfIFpsKJ9QHAsZOnh-rMby1bLbsRyzXjTm5k84u5ATSV6x0Wcc3gIH0Cj2a9VmqTd-vFESKEmU72XJyuCJSWUmVNju7eToCQNTi42YCgGYeDk8nteRFYrOOz-AhJWZTkfDTKgxEcMNKEaCEs57Nb-b9D34B7D4kYygLFKLL6pnjZ0xbRy-ycpzNcncB1-_pwy21K9oAiFlHVh1jFc2M-HFtU6izFRmKNztIolc52bXUFxDoyxZ7kMECvZAJl5341UPWlK9YMkCgl63VX61kyslSqB433fXz2KrOO08UJ4Ux6EqDUhHlk0MsI_kyhP_jvMTSp7FbZjvleQ_DLSZDXxXANa6uzZpgGxag3GqftSKTf0z8eKW-xWCEXnyAerfwoGn11AC1eS_hOw4RmfnDYtiMeM9-tPmjJX3NP57QlGpZwo9tF_2fV23pEb9FRjF-9f-1-gWJQ_UrqcvIM6hFQibpLdyXqo3t7TtG7Fk2OXL6UMwAlouL9smwP-EOnw1Cz-5lthjhkduB1BgnsQnPxxsi03st6I8n4J4WRYnwwO9Y8A0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
حمله شدید اللحن شجاع خلیل زاده به عادل فردوسی پور: همه می دانند فردوسی پور با تراکتور مشکل دارد!
💬
شجاع خلیل زاده: من دو سال است که فحش می‌خورم اما خم به ابرو نیاوردم/ فشارهای زیادی روی من است و خدا را شاهد می‌گیرم که در مقطعی می‌خواستم از فوتبال خداحافظی کنم اما این کار را انجام ندادم/ دو سال فحاشی به من شد. تمامی این فحش‌ها تقدیم به عادل فردوسی‌پور/ همه مردم تبریز می‌دانند عادل فردوسی‌پور با تراکتور مشکل دارد/ از زمان برنامه 90 همین بود، الان هم همین است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105298" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1acbc66f12.mp4?token=nVr9qQPitRX_pH1LS1d3_7t8e6oxRP36GGNMyZLoqlVyedIxkhVK5QNRp1LqOVJ-mJ4Lj0WDdCclBskZ-uxn4EksoGmowSr9ObubZ6YeOSVImoSgB_1O5e9suOU68t2pYkQC0leqwfyuA9zobT70OfvpSkethFmMh9uID-2kO69IPRdS0gPjw7xuOTMSqtFvvqSTxGuS2-lSfjl-vh0-LEcodlpgxEdHmdtbnITB4V4X7S2dOFglESRL-2nLm6VgAYX1N26w_hiPq-OsHvtB--7sW9wkPXJBuzpbj2ZKbz61QX4cLJOcvNnR9LAlc11LCq91hFNjqoiw8nubKqCrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1acbc66f12.mp4?token=nVr9qQPitRX_pH1LS1d3_7t8e6oxRP36GGNMyZLoqlVyedIxkhVK5QNRp1LqOVJ-mJ4Lj0WDdCclBskZ-uxn4EksoGmowSr9ObubZ6YeOSVImoSgB_1O5e9suOU68t2pYkQC0leqwfyuA9zobT70OfvpSkethFmMh9uID-2kO69IPRdS0gPjw7xuOTMSqtFvvqSTxGuS2-lSfjl-vh0-LEcodlpgxEdHmdtbnITB4V4X7S2dOFglESRL-2nLm6VgAYX1N26w_hiPq-OsHvtB--7sW9wkPXJBuzpbj2ZKbz61QX4cLJOcvNnR9LAlc11LCq91hFNjqoiw8nubKqCrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
تناقض عجیب در صحبت‌های پیام‌صادقیان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105297" target="_blank">📅 22:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105296">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
آغاز حملات موشکی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105296" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2a82a31c.mp4?token=dgxLNUANp-z0UHo4KHxGPlKK92U_C1B11fqj3alCXrcHqI4GbJPI1w4_USwuEdShGrQKHlXBv3bXfL9G5oKyV26yQ20SsZI3w6nskuqgaad28hnulUC0ovBFl1mJFHEw2gK1gXXnMwCcXb2dBkvPPtj5MXvevUp2SoOLll1EuVWK8d0k7PH2uLFOANN3JxokdGEU2yV9tG4khY4fmwpdNmbIZnhIM3I69feyHSWNbtm7Wk5aN_rgt8NL3rOGaCIbyB1WvvbUnQLOnEc006ushDQwC3XAQq1jiiMYfvIZ-LQJTrMKTGu8O_JFLLaCmPTOzlxbpXGnb_BIPMN-E3c7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2a82a31c.mp4?token=dgxLNUANp-z0UHo4KHxGPlKK92U_C1B11fqj3alCXrcHqI4GbJPI1w4_USwuEdShGrQKHlXBv3bXfL9G5oKyV26yQ20SsZI3w6nskuqgaad28hnulUC0ovBFl1mJFHEw2gK1gXXnMwCcXb2dBkvPPtj5MXvevUp2SoOLll1EuVWK8d0k7PH2uLFOANN3JxokdGEU2yV9tG4khY4fmwpdNmbIZnhIM3I69feyHSWNbtm7Wk5aN_rgt8NL3rOGaCIbyB1WvvbUnQLOnEc006ushDQwC3XAQq1jiiMYfvIZ-LQJTrMKTGu8O_JFLLaCmPTOzlxbpXGnb_BIPMN-E3c7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری فرشید باقری بازیکن اسبق استقلال: پاتوسی سر پنالتی چیپ دربی با فرشید اسماعیلی درگیر شد و ما جداشون کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105295" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8d66f699.mp4?token=AR72EBba5VRLdhMsy015AcZhjDFTUd_Pl2f_6MBR2-OJPWm7ktRPZEfPkcUhVqcfnB5nbk224FEXqNIibabyzf0F3bJtdI7F09rLE0i00DgkReEnyuSBAEt9JnlY4DF3gVY2D9EMgZqP-ma-bGAR5Fk9ExWefF1oBgU46a-2DuuU1FU70rSqsx3KU55NXnxDgNDE7SgfoVhF_f09jzhHAltGk5HEyAH1bpko9u6kPZWwas-wkSPnNnEV9LvENr-CQJbtKK-Q0nfUCifLSbTGY6BDV4SBgrhPOdnSa4k8DPOlT7wRKcaM3Wj-Tri2_NNFgMpM7OpziXP_cO9CGiDDQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8d66f699.mp4?token=AR72EBba5VRLdhMsy015AcZhjDFTUd_Pl2f_6MBR2-OJPWm7ktRPZEfPkcUhVqcfnB5nbk224FEXqNIibabyzf0F3bJtdI7F09rLE0i00DgkReEnyuSBAEt9JnlY4DF3gVY2D9EMgZqP-ma-bGAR5Fk9ExWefF1oBgU46a-2DuuU1FU70rSqsx3KU55NXnxDgNDE7SgfoVhF_f09jzhHAltGk5HEyAH1bpko9u6kPZWwas-wkSPnNnEV9LvENr-CQJbtKK-Q0nfUCifLSbTGY6BDV4SBgrhPOdnSa4k8DPOlT7wRKcaM3Wj-Tri2_NNFgMpM7OpziXP_cO9CGiDDQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
💥
خانم‌مریم‌یکتایی هستن مجری تلویزیون جم‌اسپورت و گلر جدید تیم‌بانوان باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105294" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105293">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFdSsDuEIWUGDFAE7bwjbAqvtiGACCNCiJQP2aZ7sK62VwGnFm9mQEQBFUEaTFG4vdZ8fnhvvNyyT1lz3sQmKPY_pL2rN3HH0X2FkSfxRVHCPLLIi9V1_SXWCDo1Wkq-8MzjloisE5DZOHCettJU1r2lJ7RlAC8YuKnonE9eXC6OsP-Tc7i8z6P8fM1c4TH_cV0vJsOrFiRNCFC3rGA0TFvP7MecPAdSab81feb4qJETO78Kq34eDcShWfUi_LMyQDzGI-mJCubiedDrOjaqcIT7guG7Doku_NTmsbTWTgY8t634BU9Efn67se8BdVeO3YITobEm0z9VxTmMjLLT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
#فوووووری
از ترامپ:
🔻
‏"در حال حاضر، ایالات متحده حملات هوایی را علیه اهداف ایرانی در نزدیکی تنگه هرمز انجام می‌دهد. این حملات گسترده و قدرتمند هستند و در پاسخ به تلاش ناموفق ایران برای کارگذاری مین‌های دریایی در این تنگه (که در حال حاضر عاری از مین است، زیرا مین‌ها یا به طور کامل جمع‌آوری شده‌اند یا منفجر شده‌اند) و همچنین شلیک هشت موشک توسط ایران به پایگاه نظامی ما در اردن انجام شده است.
🔻
اگر ایران به این حمله توجیه‌پذیر پاسخ دهد، مجدداً و با قدرت بیشتری و در سطحی بالاتر مورد حمله قرار خواهد گرفت، اما این بزرگترین حمله نخواهد بود. بزرگترین حمله هنوز در انتظار ایران است و وقتی به پایان برسد، از جمهوری اسلامی ایران تقریباً هیچ چیز باقی نخواهد ماند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105293" target="_blank">📅 21:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105292">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649b5fb52a.mp4?token=H4D2xUKcD4B7Aq0DAKMGE0wB9-C0VZd_dVYEOfkESQU8nYUZDpI3p4jn1PVnIuSzKrHPxt2KrKeeRbg-QCXIjPH2XlL36o3XCerY5o3y0_Upxxaac6uzLRh-akfmOkWpZ0Ge4RVELdhtLm0rKJoHrcEz0xpWMI5JTGDFWTkWe0JqwJyQi5n0EFZ_qeeAngFdX-8sZWPvSJ2_v2j2bOCaE2ZcEcoxXhZbsKdd9S0yIP4G80L1xMJgPshIel2moyQZUcUzH1DyTsp9lkQCdMzDriIO_CDjvIq6MuwOCd602THj9F_aMXAWza1BL-CDi5OnkthRXtLybmzhu23ypvwOBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649b5fb52a.mp4?token=H4D2xUKcD4B7Aq0DAKMGE0wB9-C0VZd_dVYEOfkESQU8nYUZDpI3p4jn1PVnIuSzKrHPxt2KrKeeRbg-QCXIjPH2XlL36o3XCerY5o3y0_Upxxaac6uzLRh-akfmOkWpZ0Ge4RVELdhtLm0rKJoHrcEz0xpWMI5JTGDFWTkWe0JqwJyQi5n0EFZ_qeeAngFdX-8sZWPvSJ2_v2j2bOCaE2ZcEcoxXhZbsKdd9S0yIP4G80L1xMJgPshIel2moyQZUcUzH1DyTsp9lkQCdMzDriIO_CDjvIq6MuwOCd602THj9F_aMXAWza1BL-CDi5OnkthRXtLybmzhu23ypvwOBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🍷
تلاش خداداد عزیزی‌ برای یاد دادن اصطلاحات پیک زدن در زبان فارسی به اشترکالی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105292" target="_blank">📅 20:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0375b01ecb.mp4?token=XhwvXTfGUNpXhb_xNHGsVMdxzyXebdDtay7sgZNlzgZIS-q2ja_k0x212g7fWUYftgyrw1CVYHLK0yczczlskQeeHBywrBq1O4u_3B-dJkaHa8H21THNDc-5cNHXurl_9IBcKj6ZEa8uJxf9PI_Jn-OkrXrpDZtOAgZfcnbHeGkDCn3WDA-6wMUV2zoHAVpwc89QlxxEHdyLd5Adhs4G1IzOgK9Kd8ESzdnOigAJuM61a5osmYpmL5SySQjbbpH8nra0itVfRI80dR7tlFRAdcHfrEQLkx0EqKLs0Az7tbxordwJokG5CujjVSacGgRA5SKDnV7MVKCC-zAp1gzv-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0375b01ecb.mp4?token=XhwvXTfGUNpXhb_xNHGsVMdxzyXebdDtay7sgZNlzgZIS-q2ja_k0x212g7fWUYftgyrw1CVYHLK0yczczlskQeeHBywrBq1O4u_3B-dJkaHa8H21THNDc-5cNHXurl_9IBcKj6ZEa8uJxf9PI_Jn-OkrXrpDZtOAgZfcnbHeGkDCn3WDA-6wMUV2zoHAVpwc89QlxxEHdyLd5Adhs4G1IzOgK9Kd8ESzdnOigAJuM61a5osmYpmL5SySQjbbpH8nra0itVfRI80dR7tlFRAdcHfrEQLkx0EqKLs0Az7tbxordwJokG5CujjVSacGgRA5SKDnV7MVKCC-zAp1gzv-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به جمع بزرگان تاریخ منچستریونایتد خوش اومدی، برونو فرناندز
👏🏻
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105291" target="_blank">📅 20:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105290">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdSEgtueWn2EwJddYIU16zOUf-49iHem1o45ybygg36RB5bvp9JnC25FArqeBsMWEIVrxYmKWQMQH4-db3aQKtbzFxd-2LcZLp2KDUHATEp8A8i29cTAL4BP0d7vN_0TVpS92JvJSuvEP3dVsRtuibnPIlrPR2uyp6gWJQ5l1oax_7zvJwTCx_RVa9B8rZnKAKl4QERBsCI6SZ7_2UlOqGbfska1zVn3kA-fRpf2OFh9Cghzcgqb6gHsM-DOJ6jYN6AQHzwRHq-c-gr7MLBmanGt5yZ1m89F7duCuL4OYIl5-Kar029ztNSK7wPRD1ckBpyhnNy8lrHUJNUIM7dVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
ترکیب الهلال برای دیدار با الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105290" target="_blank">📅 20:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105289">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
موج جدید حملات ارتش آمریکا به مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105289" target="_blank">📅 20:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUsgIgh-CY9Z2Mnctrs4uVnj0ZED_4Wr2SN_Ux0IimWONRED6cn1vSMt5jlhU3LK4h6zit3lGGR7Yd8wzUZCn4dKh6Cg0Tq5S2f3dRL4gYTDbeKOOzQbAWuR8Qi813PJLJfYJBjNtn_I4jEv8qLko-Z_B7dHk5K8g0HcaH-CySV1ZRN80w43U7Z0PyKjnal1aEeXygxH62SWRx9E4MOLXnoIT8BaZlygrryc8nU4u4l3a3fZxKSoRkmbWooEtvUMRgHLVmjMoDLqx2cYmJ8knKCl2gpVo3WkbrPP631qv066k6X-XSPtmAkQUX5jx-pXq26n4WxGOgkhicaGfGTPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
ترکیب
الهلال برای دیدار با الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105288" target="_blank">📅 19:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
موج جدید حملات ارتش آمریکا به مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105287" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
آغاز حملات آمریکا به نواحی جنوبی ایران از جمله میناب، کنارک، چابهار، قشم و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105286" target="_blank">📅 19:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
متئو مورتو: مارک کاسادو با قراردادی قرضی به لاکرونیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105285" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo05yuHkrGNbR1wB66QGWcYzNssWbLI-M3NDw0OC3VftNhljH2yaPn8OWVJNf7GYpzkNm7cyqImpxWW8oiDhgIcxJwpguBGucEdFSFZiX2eQq_Q6x32cW23rIqE35I1KkoJNfgjk9Xzy5XbDQ3I1boOBsYLFErbBqA9kIpZcxRMAGqFpFQrs3hW5GXIsriEeUgJuZHQudkgo0FPNduwE1eVo-ckZpitlqzSCVNdh-FqAS79npfnxDA8gF0bSt0KKPn3_64jP_8Yd_r7CyThT336ypDd413fCF3UsT_AKsXlhyrXEjBiW-IoT4ww2Y2RoWf_kfnlu3iIdw0PYnWoA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
متئو مورتو: مارک کاسادو با قراردادی قرضی به لاکرونیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105284" target="_blank">📅 19:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105283">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
آغاز حملات آمریکا به نواحی جنوبی ایران از جمله میناب، کنارک، چابهار، قشم و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105283" target="_blank">📅 19:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105282">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🎙
🇮🇷
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری پیش از دربی:
🔵
دربی همیشه خاطره‌انگیز است و بازی‌ای است که در تاریخ برای بازیکنان ثبت می‌شود. ما شاید موقعیت‌های بیشتر و بهتری نسبت به فولاد داشتیم ولی استفاده نکردیم ولی از بازیکنانم با توجه به شرایط هوایی اهواز راضی هستم. امیدوارم بی دقتی هفته قبل را فردا جبران کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105282" target="_blank">📅 19:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105281">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep68WtputvOLQKNgMleraEHooJ0GVEL7DBD6VHhGv1zD0ympnnadbmcvQRoVhRPCV0rfwvVl2c8gCds-zzyTIBKHMQMoee74nVC3ftQUBxMeRaSWHmkF4okbE9jNLAHjrtMzol0MqpfE4ZMUfKi_7cfpoNTqglEmmSHE3JS-lQtpCG7xCQ5OCXrLy0ZTm6lG70Z_0CCM3279WGHxLL1XMMtyvrAp1Qyh9VObJLpWgOw2aDGpG3baqxpSkdHiBnfKjSAkRirvAZPE7voW6UCGgCQuM3xLMOJnZximrpyLNlCbenTO6yWo5hhTFvhheiDGj-ku-x8p9wY215XqbgoFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105281" target="_blank">📅 19:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=X37mq8Ca1eBy9KCqZ2U_vnnsKb2Wes4L0kCD8znEN8DTBEmR01WE4BpDF1jMQlGHvJB1h1J7VvNeWOSdgJzftJCb2kWU5JYU6b-Tru2hMXovDJA7t7qMwZ3XZZHCqFoL3KzbpyjorYtSjE29lsOpwYhaWdSiID3Bnfmcrgkw1NBnQ48-e7HTrSALoQ7-6Z98015uQibB30cNBgwBmYrZ5jRnxG17VmeRJJ6veh9QmCM62-mKzCjO4I1FU6D-vU2s5UVEZOBsQzwGJUTzgC6bS6hJYs6pHegH9NKTkLazbN6kDS_jOT6Wq-DejLK5b0VuApQiapH_v7MElPtydFIKaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=X37mq8Ca1eBy9KCqZ2U_vnnsKb2Wes4L0kCD8znEN8DTBEmR01WE4BpDF1jMQlGHvJB1h1J7VvNeWOSdgJzftJCb2kWU5JYU6b-Tru2hMXovDJA7t7qMwZ3XZZHCqFoL3KzbpyjorYtSjE29lsOpwYhaWdSiID3Bnfmcrgkw1NBnQ48-e7HTrSALoQ7-6Z98015uQibB30cNBgwBmYrZ5jRnxG17VmeRJJ6veh9QmCM62-mKzCjO4I1FU6D-vU2s5UVEZOBsQzwGJUTzgC6bS6hJYs6pHegH9NKTkLazbN6kDS_jOT6Wq-DejLK5b0VuApQiapH_v7MElPtydFIKaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
🇮🇷
هوادار پرسپولیس در آستانه دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105280" target="_blank">📅 19:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105279">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei-co9DRurwACPPZLvz5I4JIdJdmp-Aoc2TlSt69tB_YIu45aojRjplEkiVkRT3S8_UcUcCKb1M13EID286qWUhdiNERKlCwpE0Ex65ExDKjgdOPJLe2dbgxr_XY8j8Cvac8C053gMmkfMK6kCWHA2t32heE3tc1pNXB5PkjRIWUgLFs_ZrNh4WC4kB6COi65rBNJ19AcxHJS4zyv2q0mXPWoZNn-OFy0rKOriM0gSDtGwJLyKT8kzAuVUnS9PL58S-jN2Zuy4425gl0THkbjwqUDwyykviVq8drS3mbVKMbFyEyWY6m7twTWgao2-kfTBaaz4CWFfkCJdieRAW61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105279" target="_blank">📅 18:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105278">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cf132574.mp4?token=G3bpoDAPE7nbUJYmWfsqPjvrrZsnGRY0z1jTbelG3AWmPzShmxkDBWkG28FBmhxr6ghjbEc-Iqwm7P0d5u0oH1kfL04BMZwh7A2nlzddeZGLV5qBavmIvuMIzvM9WlpJ8Z-m9lwxcaCw2Y0MmzMmi__qtY9ibR0x3QNJ6XI5djkeGq84dxPIVt0_dVeNcHyeL9p88-FR6asJaByN0dfCiv8dkssPfrbN9mlGxO_rr6kC0W3qAmHYb8fwJ3Nh0QPapOiHLc7RGsBIi9jMkpo3EMlwfxO69yZEcWp7oXfywtD6FgULdBYoWKu9_6eHRtJx89S3UB_V-HX6sYJDCsBo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cf132574.mp4?token=G3bpoDAPE7nbUJYmWfsqPjvrrZsnGRY0z1jTbelG3AWmPzShmxkDBWkG28FBmhxr6ghjbEc-Iqwm7P0d5u0oH1kfL04BMZwh7A2nlzddeZGLV5qBavmIvuMIzvM9WlpJ8Z-m9lwxcaCw2Y0MmzMmi__qtY9ibR0x3QNJ6XI5djkeGq84dxPIVt0_dVeNcHyeL9p88-FR6asJaByN0dfCiv8dkssPfrbN9mlGxO_rr6kC0W3qAmHYb8fwJ3Nh0QPapOiHLc7RGsBIi9jMkpo3EMlwfxO69yZEcWp7oXfywtD6FgULdBYoWKu9_6eHRtJx89S3UB_V-HX6sYJDCsBo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
⚽️
تحلیل‌گر شبکه‌‌ورزش کشور عراق: یحیی‌گل‌محمدی تمرکزی روی تیمش دهوک نداره و معتقدم میخواد به لیگ‌ایران و سپاهان اصفهان بره!
📊
یحیی در چهار بازی ابتدایی فصل لیگ‌عراق موفق به کسب برد نشده و هر ۴ بازی رو مساوی گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105278" target="_blank">📅 18:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105277">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guPZup19PF0Zwh8ryaUIQ9984gYgjsWIorWCFtunM335sUmAR5CbGJ3Hjf7_apsGGIg7xvtVbi-iQjZT7Zcaf_40a6vGxG6MlyvTuxnpv-rHZ911DpiuGmKJo0oO0xXmpj5zk5ss-lMEnQEy4jz_RgNKNB2ywZnc2bXuVdHuBVWcSHjQTHXDzfPK3B3OimO3wFLph6lthuaPOeo3yXgcGo2Ptq9syXl4jQaxOgSh6ZrOTpmI6_JHjIBJCsOR7wNwSs2OkILIzuApvgT65pvTiFDQPfN-R1Orbp9F-YosFLP2gJxuvLRMLTPhU3fqRNw0oH2VMVMC8ugRFp01cmLAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور تبریز مقابل شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105277" target="_blank">📅 18:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105276">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=XHk3_408Imdbun2KdhuF68dShHRoG5bZs7TRBVdwy0AIuBU-Kz9zBxyxHfyr2A9QLrPrQ-IxX6QkpQVsdIfbBS3r-AvMCOLKVv_8_9XcCc3IjudWp9YLfHt-7BM2EBlqYSlKalKreLbkizLtvzI9o6-XI8udRG49rs89SqsA1mW9bqbi3njoQDwkcT00UMssR_wApI7COnRRqI4bTY8NlgILIP8Ss4hom-L6FmZrrL2OXMM9SonvxpQo2skdUw-GfrwjypRrMXuHCK_5ipSMwkfAavuuAOy8cKGSPzS1zaDRV3Kd92P8_ExHb3m7cvIuKEAiTL9Ay1W8_VpvNqxKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=XHk3_408Imdbun2KdhuF68dShHRoG5bZs7TRBVdwy0AIuBU-Kz9zBxyxHfyr2A9QLrPrQ-IxX6QkpQVsdIfbBS3r-AvMCOLKVv_8_9XcCc3IjudWp9YLfHt-7BM2EBlqYSlKalKreLbkizLtvzI9o6-XI8udRG49rs89SqsA1mW9bqbi3njoQDwkcT00UMssR_wApI7COnRRqI4bTY8NlgILIP8Ss4hom-L6FmZrrL2OXMM9SonvxpQo2skdUw-GfrwjypRrMXuHCK_5ipSMwkfAavuuAOy8cKGSPzS1zaDRV3Kd92P8_ExHb3m7cvIuKEAiTL9Ay1W8_VpvNqxKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان‌چالش ترند این‌روزهای فضای‌مجازی
😂
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105276" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105275">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105275" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105274">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRp58W9o8CtofwGTSMvAnhu1boa8YoNKl06f3hWODBw-l6k_96JQY2hAyzSD2U2o3apSaReKTy0vlFk2FcUpBxbn9PAMeSeiYrQFpm512X_GwPp3qnDX5xPfGvpRGApl2TcI3KoYDB-aFYSBy4qu789T6E3wF7jJc8nwKd11vq3tLZBMjDAVMllNkOnpCXJyvswDHgVAeCfWxiOCUTo3xFUCJNQqJlJCvZv96tkNOiJluj_ay7pP8ivI7t50SwHzHJGBFHbMRUIArr8gWNbOr1u00JPuwMOmuHo93v6EV-9E0M7GVVQIHtMiPL12o8c51fiGPZQejOc6k7Wl-wfCtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105274" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105273">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=oaf4q2WeIRRf96mvCabdZKyE5bAcAdh3ydrzIU_RciNxYFp0rBgYlEseGVy4YLVC9jrrTxcOOQnkuT5pKntbYgRhhfp3IqSC4yPfLYg7wyucJQTd_zxR1CPyotvUxPAwZ8h4SCpO726QOcyNw3zJ6eChhmVfGo8CEP39KXO-jF4e76_9effm3KMBXz2o_q9zOJ1furEMQ569vDOUp1-ogSYE8ikntkCxMl7aG4-KcgG8jEECIZhyAWipq7kiYknddEU_VmX49ASNRYBwX_V5KOAH9zWDf546JWtBQdI6M4942H5oFRT_qYYdqDgpxhbfbb8o1npMF3BJPPSMX8Xp9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=oaf4q2WeIRRf96mvCabdZKyE5bAcAdh3ydrzIU_RciNxYFp0rBgYlEseGVy4YLVC9jrrTxcOOQnkuT5pKntbYgRhhfp3IqSC4yPfLYg7wyucJQTd_zxR1CPyotvUxPAwZ8h4SCpO726QOcyNw3zJ6eChhmVfGo8CEP39KXO-jF4e76_9effm3KMBXz2o_q9zOJ1furEMQ569vDOUp1-ogSYE8ikntkCxMl7aG4-KcgG8jEECIZhyAWipq7kiYknddEU_VmX49ASNRYBwX_V5KOAH9zWDf546JWtBQdI6M4942H5oFRT_qYYdqDgpxhbfbb8o1npMF3BJPPSMX8Xp9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پلیس‌فتا در واکنش به صحبت‌های دیشب: به پرونده پیام صادقیان قطعا رسیدگی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105273" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105272">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=AodSf0Qg2No0hoiHL5bxtZJa08Vk-gynLeCJDRJIfBEB2YdeSQrNqkXmMkyR4KLymitnlwwiUaDOhFt7acj9iBTijumIQJMnAaIJqOHhD6uxkJTxAwFZuh79An1Oeyt9jish-q4eA-hTASMT_qEBVhjGO3kJVJ-MbjOoGEX_DoDipyJGi_UWrsMA8gONFdpw8ul4nLr0PCCC68DKnDdfuezTAAyQ9UfOwiBuVDvV4jL0DVtkg9WmqgJXNNs2yBA5rj4KCdVeScU4P7o9NT_215yQbe8w85nCCjc9cNOVGoyn1IJZND-wxUM0baHO-mNP-X-jKdBWVoBMOc3LtxSFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=AodSf0Qg2No0hoiHL5bxtZJa08Vk-gynLeCJDRJIfBEB2YdeSQrNqkXmMkyR4KLymitnlwwiUaDOhFt7acj9iBTijumIQJMnAaIJqOHhD6uxkJTxAwFZuh79An1Oeyt9jish-q4eA-hTASMT_qEBVhjGO3kJVJ-MbjOoGEX_DoDipyJGi_UWrsMA8gONFdpw8ul4nLr0PCCC68DKnDdfuezTAAyQ9UfOwiBuVDvV4jL0DVtkg9WmqgJXNNs2yBA5rj4KCdVeScU4P7o9NT_215yQbe8w85nCCjc9cNOVGoyn1IJZND-wxUM0baHO-mNP-X-jKdBWVoBMOc3LtxSFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
تیم‌نروژ با قرار گرفتن در رده ۱۲ فیفا، بهترین رتبه سالیان اخیر خودشو کسب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105272" target="_blank">📅 17:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105271">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=ub1swnPO_F-Q0xXIOBVYoaW6KfpIxtm9ZGnI1ElK7FZ_0_t-kXYZ8H51Z7l7gD6-VCQuh6u6k-Lb0kCJ_CBYhBS3mbaK0N52zQUamdGSWms89K8rq2g6uV_kLA7l88u62Fe_0FJK74zKNzdtA8wp33RCiySU_ESscyL0c-RXebF5HvRBtPuKx0Qlwu_dOcLVMx9h08mnc1KdT3x3uI4aQ0eGJ3pztRzELg_kwQ1dp3YBKeawDKQ6BSeQz6jT0zUmpxib_t_I8uG_D1xvatLK2rwcU5kodT3_dLgLHW0cmfZ-S4LynnRShNRYSLDUI5s70JROdopWogXSe1n_k5cZzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=ub1swnPO_F-Q0xXIOBVYoaW6KfpIxtm9ZGnI1ElK7FZ_0_t-kXYZ8H51Z7l7gD6-VCQuh6u6k-Lb0kCJ_CBYhBS3mbaK0N52zQUamdGSWms89K8rq2g6uV_kLA7l88u62Fe_0FJK74zKNzdtA8wp33RCiySU_ESscyL0c-RXebF5HvRBtPuKx0Qlwu_dOcLVMx9h08mnc1KdT3x3uI4aQ0eGJ3pztRzELg_kwQ1dp3YBKeawDKQ6BSeQz6jT0zUmpxib_t_I8uG_D1xvatLK2rwcU5kodT3_dLgLHW0cmfZ-S4LynnRShNRYSLDUI5s70JROdopWogXSe1n_k5cZzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های هوادار تراکتور پیش از بازی با شمس‌آذر: ممنون از نیازمند و ایری برای گل و پاس‌گل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105271" target="_blank">📅 17:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105270">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOV8ROzXCdoV9w6reBmLFv_BHyE8T51Wd44GN8RPtsf1IwisMSN5JXpy8uocECHPSOihP_QpoJ1d_Tm6c1qjOEbwBgjOKs5voTSOGdlxP_JvJQJQLTidCfB3ogKIMOyZ60qcMbkMJbzJXxQ5GBF_XtqFrU9qY9s4ZetyNh24zSJCXt9LbbamHNh7qWwfRQxv-Dc2vXsVCD91fP378oO4VUEhcjRyIMnp9eiCjraWtoyCAGuPGFgd1oxSfys7niV9f9A6Ru_Xkn4q2Nr3kW4cCoPWioY9dnQGeabohuwfG0J1qUiH6V0ssxGvcOt-TvLr4XuY9QELEgkpLFQkwuCnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تاریخ اولین ال‌کلاسیکو فصل مشخص شد:
‏
📆
• یکشنبه 3 آبان‌ماه
‏
⏰
• ساعت 23:30 به وقت تهران.
‏
⚽️
• ورزشگاه اسپاتیفای نیوکمپ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105270" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105269">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6DTASKio92OEZ6Txd4w6o_7Gtxjg3rgVwvnkog01f36F1LBktBn84BuTrcy9Ruxm5U5V9EeIJS3BKyCCPUHuqQXIiViE_KfAt7RHtQJsTRPlB_eocUE7dR7368Xi5t5WNsGERdUqy0az5U6SbeNI2J6SMhGgTKF5Z828jf66XgqYNiDiZ4t2keKF6cK3Zwumc0E8kQyBe2ursF71IzFuqaY03CDZHozO5X1re_J6NFCzGL-MU0v1cWRAIjr_pHxi8-EZRNM4dP6evNreBeHWNyNhcPsB3S_AG8woRNE5PP78oZDlgWhIVQn3dHZRX1Bzr5swG2DPw0EU2Dsk1v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
🇪🇸
مقایسه عملکرد هانسی‌فلیک و مورینیو در تاریخ الکلاسیکو فوتبال اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105269" target="_blank">📅 16:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105268">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjAqfzhW6-JGNcMVUCf3VEYWnKhkkRpCQLzzrMJnVi3xcIHJTtFYg-bIbBh-T7sSBdiKU9KuOrKTXzJltqdbhBptWOPbu_QdkboihoO8-BpOTKEekCnPPjDHLDUq-TdX_odY3UK09I02Ma1S1t_ChFyFAKjvmCwN8TCtwNPMkyjBPnoFnXuzz6zfB9qTNeq7HAxnuTKRVnjk8nO74lvxH5ML2ORc3YiK4yeiHXG72aRjDH_0ES1VxlGW-9zTQiubdJNxmuOUZE6Wuhs_epYdOgULFkIVyecGq45C35NtF_7EnGkn--lLnSW8QoEY4NXutO0DQGuq6CleHGnlmUVa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
💥
در آخرین ماه از تابستون یه نگاهی بندازیم به بهترین فیلم‌ها از سال 2000 تا به الان که اگر فرصت دارید در این اوضاع شخمی مملکت نگاه کنید. سیو کنید بدردتون میخوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105268" target="_blank">📅 16:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105267">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=n1eKTd0KqE47ZGFHhKm-trM7N0j8BqPJNqdR6qnmBs8hcppojdGO8wDgAjtmN_lm7RHOqZ0ZA5Gi0cyg2uyVtUalpBvMgccRwAyWbhrBYjknIokYqpMd0ECsbzMAcKhpXLN0S1YPJehxKRSGEm8vfOZ9DsvYdIeyNTZmERQr7oRZ8eiaaGYhwWvWJidVDO8ikqdJP5eivLOQ4JgQp_bxKD2S-xVSgTmNExVQ6Vn5vj8GgGtT2XvNGBRuy0Utd-gK8pWkEyPtJrjobA2vtkwl0AkTlfPTCjCPlDYmeXPCHKOpShP12AeT40z2Fq8ANhNQOxJ38PaWjYiH1JJ4lRK6cRtdDNkCiaHP2UcPdnRLCv5rNBq9VKNuawFsLwndXD7-ZRy9d97nsRALwxpUrqmn6eYbCrbrp-D3w87caqJ22xOnlziMxSRqSklGkoeYDXXa2kRlzJH6wbsJtiZqEmHxwWTMPmn7ltLQANSQv_OZAG1NPLMHn0f1nPON83IGEG7rNkDSiYNvTXC5N_j1Z6opiZGYpz6NzNWoQAE_rspnxpQp0gxMOc7uinK6U_dMWfHkpURBsLGws8_vC2tcrH_xY-heqEAk-Q1TaTlKBxtoljyUmviZmCxWPz2E5bbXrjnhV7PDinBEDUP8_eglli7DVZYz0sLyjW1ly4SJ9EhlXb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=n1eKTd0KqE47ZGFHhKm-trM7N0j8BqPJNqdR6qnmBs8hcppojdGO8wDgAjtmN_lm7RHOqZ0ZA5Gi0cyg2uyVtUalpBvMgccRwAyWbhrBYjknIokYqpMd0ECsbzMAcKhpXLN0S1YPJehxKRSGEm8vfOZ9DsvYdIeyNTZmERQr7oRZ8eiaaGYhwWvWJidVDO8ikqdJP5eivLOQ4JgQp_bxKD2S-xVSgTmNExVQ6Vn5vj8GgGtT2XvNGBRuy0Utd-gK8pWkEyPtJrjobA2vtkwl0AkTlfPTCjCPlDYmeXPCHKOpShP12AeT40z2Fq8ANhNQOxJ38PaWjYiH1JJ4lRK6cRtdDNkCiaHP2UcPdnRLCv5rNBq9VKNuawFsLwndXD7-ZRy9d97nsRALwxpUrqmn6eYbCrbrp-D3w87caqJ22xOnlziMxSRqSklGkoeYDXXa2kRlzJH6wbsJtiZqEmHxwWTMPmn7ltLQANSQv_OZAG1NPLMHn0f1nPON83IGEG7rNkDSiYNvTXC5N_j1Z6opiZGYpz6NzNWoQAE_rspnxpQp0gxMOc7uinK6U_dMWfHkpURBsLGws8_vC2tcrH_xY-heqEAk-Q1TaTlKBxtoljyUmviZmCxWPz2E5bbXrjnhV7PDinBEDUP8_eglli7DVZYz0sLyjW1ly4SJ9EhlXb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ربات وزنه‌بردار چینی وسط مسابقات جهانی وزنه‌ خودشو رو میز داور ول داد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105267" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105266">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=fBS8SMeBWcDCE6THSpMUeBpJkDRqlTkiKoOvBKyTY0cQ-kTy490n6mpHk8vBSCj1kGXRQMwD6PCTFB8gUJM32IyWttMh5H18XiwOJurydO3DzjvUsR83hRmpcf3LvsNxd-LkR_TlIj-51TV5y1czHKDhKSGBLIbI6hAqHa0x2ANw5rP4JCl-5vQSbDVoiBt_K3cPoWaOm4FXJeWVmSqmwcwDW2zWs2iCYAQ1oGybBvQvJih_V-9ggxtpgotQHWh63MTJJjJx3XKd08w7I2tx30LBPzYysFv8zLHkFGfDFt4oFrUwoWTxgdGrv2vQEhsS5MLK4ZnUguAcK7pt98EG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=fBS8SMeBWcDCE6THSpMUeBpJkDRqlTkiKoOvBKyTY0cQ-kTy490n6mpHk8vBSCj1kGXRQMwD6PCTFB8gUJM32IyWttMh5H18XiwOJurydO3DzjvUsR83hRmpcf3LvsNxd-LkR_TlIj-51TV5y1czHKDhKSGBLIbI6hAqHa0x2ANw5rP4JCl-5vQSbDVoiBt_K3cPoWaOm4FXJeWVmSqmwcwDW2zWs2iCYAQ1oGybBvQvJih_V-9ggxtpgotQHWh63MTJJjJx3XKd08w7I2tx30LBPzYysFv8zLHkFGfDFt4oFrUwoWTxgdGrv2vQEhsS5MLK4ZnUguAcK7pt98EG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
پیتر کراوچ در سال ۲۰۰۵ فکر می‌کرد بالاخره مخ یک دختر اسپانیایی زیبا در هتل را زده؛ اما جیمی کاراگر خیلی زود فهمید این «دختر اسپانیایی» کیست!
🗣️
کاراگر همه‌چیز را جلوی هم‌تیمی‌ها تعریف کرد و کراوچ تازه فهمید دختری که به او علاقه‌مند شده، همسر ژابی آلونسو بوده!
🙂
کراوچ سال‌ها بعد در پادکست گری نویل این ماجرا را تأیید کرد: «فکر می‌کردم به خاطر جذابیتم از من خوشش اومده!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105266" target="_blank">📅 15:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105264">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=H2MKV1fuMm259VCvQjMxmkvwjIJrCuuXqWvK9ujaAZfEyjgCP0CTRu-0_Ifo8eoTTsFdW0QydzJUTtv-oL884DRmu--BNOgsiTj_mQ9ZvOBjBmLL_aral9VHDInv4fs_RmiN9Q3HME34_qCvkin5RkbZ9v-5H6hKnnmlUuD1QabGWsEPWnAionaHi9FRvB3ig6rA7SE6dWvv70Hl1_hL_r9VH9rlQPDFAs7XbQoS95olrVtcVIcZ9OqKX5mL6htz_6j1DxtfAFCcd0dgJvkCqwhexGaVm-bdJWTQv0LU7Fp-9ee_SVAIau7H-F0-F1aYI1DxmPPprDkfh5uSrzNlyzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=H2MKV1fuMm259VCvQjMxmkvwjIJrCuuXqWvK9ujaAZfEyjgCP0CTRu-0_Ifo8eoTTsFdW0QydzJUTtv-oL884DRmu--BNOgsiTj_mQ9ZvOBjBmLL_aral9VHDInv4fs_RmiN9Q3HME34_qCvkin5RkbZ9v-5H6hKnnmlUuD1QabGWsEPWnAionaHi9FRvB3ig6rA7SE6dWvv70Hl1_hL_r9VH9rlQPDFAs7XbQoS95olrVtcVIcZ9OqKX5mL6htz_6j1DxtfAFCcd0dgJvkCqwhexGaVm-bdJWTQv0LU7Fp-9ee_SVAIau7H-F0-F1aYI1DxmPPprDkfh5uSrzNlyzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
⚠️
واکنش عادل‌فردوسی‌پور به حرکات منشوری شجاع خلیل‌زاده و عارف حاجی‌عیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105264" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105263">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=r2wHOo0C1V7-HQku-42Z3E_gdLOwmsVQ4zusXtnJHC4euCC1TyuwJZ2xaEShIql4hr66QcXu4Unf_ryGuEqGd1moXR0umnXLKTZne4nD9KeG8UhunsDWKHdkHoZMQGnCl-1J9GC1BXF0YjMMDox_PGfnLy0NTQqBDpm1Vfn1GnI6o-UgrYfsWuTxZzYy4sEcFUbli5mqeAA9WbmVMnjzxhgWoz_92T6nSlKqU6D6sb91-pg9CnZ603tm6jS13EM6FfkFXYdZNvbMJ7FHbwGyKclOfdLPxL0Aj99fFQDA29MOm9eZcScL9LB4RgaD1P_LxjNZRjB7YobCwl9PAHqXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=r2wHOo0C1V7-HQku-42Z3E_gdLOwmsVQ4zusXtnJHC4euCC1TyuwJZ2xaEShIql4hr66QcXu4Unf_ryGuEqGd1moXR0umnXLKTZne4nD9KeG8UhunsDWKHdkHoZMQGnCl-1J9GC1BXF0YjMMDox_PGfnLy0NTQqBDpm1Vfn1GnI6o-UgrYfsWuTxZzYy4sEcFUbli5mqeAA9WbmVMnjzxhgWoz_92T6nSlKqU6D6sb91-pg9CnZ603tm6jS13EM6FfkFXYdZNvbMJ7FHbwGyKclOfdLPxL0Aj99fFQDA29MOm9eZcScL9LB4RgaD1P_LxjNZRjB7YobCwl9PAHqXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دخترای جنوبِ ایران
🫶🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105263" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105262">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILjz67sSIShUMaZgWiCUr0bHan6SHKZx465he8io9mWnUjV3ixqrV97VhZwnD6hFC7YbK3gqgSclfa2DAqqi4BHsUgzEd6oveU-tJGwm39PXi8htFjklWnG7pEGoemsA6owU2_tzeWQMUMcUrtitIigHfLlc8N2nTIcWY7HPI_c3CkbCorS3LC27qJuN7yeIeBZWcJ8XKOq8np7OG0ThzQEJDWRZTvauV5qOPkvMIAq6Cjg6ws-9IGDUgjecBVfrMeWcwTJJkFbZKoLq0i8Cr63UGNRfc09G887LdKrppol1jNZzZPET1miDhMconGMBzojigFdik9KNTMHzDHBj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
هوادار بانوی تیم‌فوتبال تراکتور تبریز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105262" target="_blank">📅 14:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105261">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93b254714.mp4?token=J0pUdprou3uHj-zUCv76cxbzDpFqy8aUykDhjOOo8cnnwnmrwaKxYND0ieXHt7vJ3Jm6BH3Ww86dXbJhZHoEwZ5CZwMqUUKGE9ytLTtPcLbauTOr9-ROMjL-mGKzEjqzIToT3gItuypanKw0TnTqo2ZeIWBhO50Uwpopnvugw7j7hjnoKjzKT4ZL4Xu-Pzc437yS3VdK7_f7TBOOwAy3NPf-WjTNfE_QBCPQVZiZZKYlqAruDsenKfL8rsMt-18FTwxseHSz5xPzjx2dPZd3o9994lDB4Ga_8tXKxUCt4zWjUKckYsLt-khYqQzI2vIqdVIU1M8nNEihi7BB3ZtNgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93b254714.mp4?token=J0pUdprou3uHj-zUCv76cxbzDpFqy8aUykDhjOOo8cnnwnmrwaKxYND0ieXHt7vJ3Jm6BH3Ww86dXbJhZHoEwZ5CZwMqUUKGE9ytLTtPcLbauTOr9-ROMjL-mGKzEjqzIToT3gItuypanKw0TnTqo2ZeIWBhO50Uwpopnvugw7j7hjnoKjzKT4ZL4Xu-Pzc437yS3VdK7_f7TBOOwAy3NPf-WjTNfE_QBCPQVZiZZKYlqAruDsenKfL8rsMt-18FTwxseHSz5xPzjx2dPZd3o9994lDB4Ga_8tXKxUCt4zWjUKckYsLt-khYqQzI2vIqdVIU1M8nNEihi7BB3ZtNgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
بدون‌شرح‌ترین‌ویدیو امروز...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105261" target="_blank">📅 14:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105260">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=QqegKNDC4LahwtaOTqDkt6CuB9rEKaw8DzXWpSZaoTr-hPKx7fMFAupVS7eMcNXn0fempq-3BYjy3Kwvkk1vXDjLL2-GxUeM-By-k0B2YEaRdlJE2q44aZvsctFyd3nRtKIh4Eu6atIsMswN7ri7RJfcD1Is-qfqadqVC4AB4w7yAjKrIgHBa0F-IheBWbukeHdi-l9yUHrCWtz9Y1W2FYEZOxbMOjEF_1wZ1kP6g4NM0c2KKCfdqODQvv3nP8hdJYgXOjgyYqmb3YrXX7l4NAdjzRocg_zS4Gq7S37r4-CYlKwUZA5A3Yo3PFC5zaKlPoRsYPZmPZ-nrEelZrQIhAJYiAVtGgrobKnFHAsGx2Zc4b4FhtY5CY7Z1emdHVdH-s9sqACX0adLq9nPTNjmAW1Y9-Kj3g18r39RCx9cVYJhbx_q27qhW7ib4w-SKBEXKN_ieVg-FFcoihK-XseiRIQdP6w-l4KDytX32zmRND-Oubn0yyI4-B1voZ4d2yIcvephO2p54-bCW3J0xxAdUhJkYrU38gqyaBarbrMhnff5bej661cHLBsTtRUqvOz1CYjbV5iMCtp2ByAKWfRPM5GANFIv1aNeHLai94mVNQe2qa6sJxqQWh25vgNp5Y7YUb8I01oUVdpDpRjTcC0C8lY1ZZJnIT3ANVdMujW54cY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=QqegKNDC4LahwtaOTqDkt6CuB9rEKaw8DzXWpSZaoTr-hPKx7fMFAupVS7eMcNXn0fempq-3BYjy3Kwvkk1vXDjLL2-GxUeM-By-k0B2YEaRdlJE2q44aZvsctFyd3nRtKIh4Eu6atIsMswN7ri7RJfcD1Is-qfqadqVC4AB4w7yAjKrIgHBa0F-IheBWbukeHdi-l9yUHrCWtz9Y1W2FYEZOxbMOjEF_1wZ1kP6g4NM0c2KKCfdqODQvv3nP8hdJYgXOjgyYqmb3YrXX7l4NAdjzRocg_zS4Gq7S37r4-CYlKwUZA5A3Yo3PFC5zaKlPoRsYPZmPZ-nrEelZrQIhAJYiAVtGgrobKnFHAsGx2Zc4b4FhtY5CY7Z1emdHVdH-s9sqACX0adLq9nPTNjmAW1Y9-Kj3g18r39RCx9cVYJhbx_q27qhW7ib4w-SKBEXKN_ieVg-FFcoihK-XseiRIQdP6w-l4KDytX32zmRND-Oubn0yyI4-B1voZ4d2yIcvephO2p54-bCW3J0xxAdUhJkYrU38gqyaBarbrMhnff5bej661cHLBsTtRUqvOz1CYjbV5iMCtp2ByAKWfRPM5GANFIv1aNeHLai94mVNQe2qa6sJxqQWh25vgNp5Y7YUb8I01oUVdpDpRjTcC0C8lY1ZZJnIT3ANVdMujW54cY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
دیشب‌کریم‌آدیمی بنده‌خدا فکر کرد چون ۱۰ دقیقه تو زمین بازی کرده دیگه بعد بازی نباید تمرین کنه که دستیار فلیک این‌شکلی کاسه‌کوزشو میشکنه و دور تا دور نیوکمپ کنار نفرات ذخیره تمرینش میده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105260" target="_blank">📅 14:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105259">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=pc4909X5bQL0elLCc92_Jj5bQFW4qNg291u-ydRpPeZCxN6GgfQHEVrgtm6stRW9T18NY1-mjGpGPkQvBGrHCrWEoK6Ua_Oa8O6rHMvi3hGNhZqhLpNfZ1Qsd_0I4AO2aDMDhNiCQIPgF1tWeMdtkYvu3MzUuJZRLjnR_AFMC6WItMKqdOWeh7boOCLuJO9rmlv6-iPXfr5VA5d3Wl3MCRS84b0TPgzJpN2eY0xXzKG8pbHvhQZFHYEhMpGJU-qMgndsID-RA8tRNz2_aqq6XXxC_GFXFp_e9pDMURRLrB7sTH3jYkuvRm2JcOwjFbJMlkec8C3_fEX16hlyjbyA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=pc4909X5bQL0elLCc92_Jj5bQFW4qNg291u-ydRpPeZCxN6GgfQHEVrgtm6stRW9T18NY1-mjGpGPkQvBGrHCrWEoK6Ua_Oa8O6rHMvi3hGNhZqhLpNfZ1Qsd_0I4AO2aDMDhNiCQIPgF1tWeMdtkYvu3MzUuJZRLjnR_AFMC6WItMKqdOWeh7boOCLuJO9rmlv6-iPXfr5VA5d3Wl3MCRS84b0TPgzJpN2eY0xXzKG8pbHvhQZFHYEhMpGJU-qMgndsID-RA8tRNz2_aqq6XXxC_GFXFp_e9pDMURRLrB7sTH3jYkuvRm2JcOwjFbJMlkec8C3_fEX16hlyjbyA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
عملکرد پشم‌ریزون دیشب لامین‌یامال برای بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105259" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105258">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=sDHzmRvDyfGJvnmIwjlDPyWq8rNWtHJ4axHsw3yjomkZUw4eE-ZTJ0kAidwOctN2UI7z16fF_LZ8E84ze53S__mdNzC2RRFTE-RtGkaQea7T22DmIWMZbXdM_M4W0ic6RJvvGJvKLxIZeAzTx2nhJNZ2YcAvyNx97O6PiKum0eTTiLe6GUsHrrxPTEyNbx8N4qu8HrpSSkepmoYSw2_0owgfI2bynAjmn6j9-UIHWDwYP36q5hgNmHr3K95-4RqOu_pVZgNSnK8Z283JGVZLnDaJut4SPzPdbncPwh6wWfKBdFFPIzu-esSJqQvy-I9yy2NZBBJqKlAiCVogeXUPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=sDHzmRvDyfGJvnmIwjlDPyWq8rNWtHJ4axHsw3yjomkZUw4eE-ZTJ0kAidwOctN2UI7z16fF_LZ8E84ze53S__mdNzC2RRFTE-RtGkaQea7T22DmIWMZbXdM_M4W0ic6RJvvGJvKLxIZeAzTx2nhJNZ2YcAvyNx97O6PiKum0eTTiLe6GUsHrrxPTEyNbx8N4qu8HrpSSkepmoYSw2_0owgfI2bynAjmn6j9-UIHWDwYP36q5hgNmHr3K95-4RqOu_pVZgNSnK8Z283JGVZLnDaJut4SPzPdbncPwh6wWfKBdFFPIzu-esSJqQvy-I9yy2NZBBJqKlAiCVogeXUPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
محسن نامجو مرتیکه دلقک در کنسرت نیویورک، شانزده شهریور سال ۱۳۹۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105258" target="_blank">📅 12:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105257">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105257" target="_blank">📅 12:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105256">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=Ud7fBZuPkbwvfiqQ3Cfw4XbHiV4icC9GsKua8_lH1CY8M_BjcSqQP7in2JFdhwaRQYmukYHmYnBm-U0mDT0rE7hrSKIl9lO0NZyZ1b_xNVIvlnEbjTdnMjHGu6eABTW0NjN18Xw6EJj4ppOL7vrTCR5yyz356l8UY5ra4VGv2_R0Z9TLlrr1ZPHD9pJSK5HjzanbHraUTqBLc-ZYZ-VE215lkAnzMHNbgYYnVHDqge49b_P_6NVG-rUymWgazIxTTYcMDZSNtTWFUwgKog_3L2wEP7MfmUwBnHESPrCt9ZA4iswcFXUyybb2fWLbxhmuVYpfqGqJTpFNq3v6AJm1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=Ud7fBZuPkbwvfiqQ3Cfw4XbHiV4icC9GsKua8_lH1CY8M_BjcSqQP7in2JFdhwaRQYmukYHmYnBm-U0mDT0rE7hrSKIl9lO0NZyZ1b_xNVIvlnEbjTdnMjHGu6eABTW0NjN18Xw6EJj4ppOL7vrTCR5yyz356l8UY5ra4VGv2_R0Z9TLlrr1ZPHD9pJSK5HjzanbHraUTqBLc-ZYZ-VE215lkAnzMHNbgYYnVHDqge49b_P_6NVG-rUymWgazIxTTYcMDZSNtTWFUwgKog_3L2wEP7MfmUwBnHESPrCt9ZA4iswcFXUyybb2fWLbxhmuVYpfqGqJTpFNq3v6AJm1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مجتبی‌پوربخش: تا جایی که اطلاع دارم، وضعیت جسمی علی‌کریمی خوب است، فشاری بر او وجود ندارد و صفحه شخصی‌اش نیز در اختیار خودش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105256" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105255">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kL1TyQTtwH3OgBANnVtNsuZG3-VwxwA0oioCzZCXSH1JJt0K0LS_keRpGdVJlpubFHYJQXpffF5XTJA4x5KEN747Kd5oj1FEMfGXoX9EFO_LfCJnW2Avox20-h1Z_Cvue6TbP-vO7iKnqiqQKeKN5vbLQ_85-NFZLI4BjCrU7Zv_18Z0ZEypiwixqoOfhcZb6tRDlAG25zwFheTzZCfl38_N-8SaO5_saHzGQ62O-ku3gfVHrkn-aqjrHN0jSgZxQ7SXACLE6aZ4QqyLbDo4OoB5iOlCouH-6xg5iPPa7tohD1v4ZVi9ThukWxaCSf4RJS7QB1eofxxHkdPGrqnO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
نتایج سه‌بازی ابتدایی بارسا و رئال در لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105255" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105254">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=L5RfZLvmpwGq2QTUsM8SXcTAP32Psg6De5-h3W7MUFOKUwFX0trW_qJfdDLv3WuO_RtrZGhdGHUERQh-RFH9DYFz0xBx-hIyysujCexYvNhInJLwgGdfl-0Dd323n0Lg7zyahSCW4-0TOkWQkQ9ZKhtKMWy2tGimDfnTxilELmAiP-49qdtNJryMPUHXK1q4M7HUmtqivxHx_8O69USeBODVQ6lRfGDpoCwSF2rBcfksGdwlS1-eQNuFFFAtSZKSd-zMeprBe_2PFdjQOw1bXvA1iosQys1HA8YHkASsm3V5Nvc6CAdk0xkypvTf4Y9QLrPGzOmjCppDzJAJTSuHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=L5RfZLvmpwGq2QTUsM8SXcTAP32Psg6De5-h3W7MUFOKUwFX0trW_qJfdDLv3WuO_RtrZGhdGHUERQh-RFH9DYFz0xBx-hIyysujCexYvNhInJLwgGdfl-0Dd323n0Lg7zyahSCW4-0TOkWQkQ9ZKhtKMWy2tGimDfnTxilELmAiP-49qdtNJryMPUHXK1q4M7HUmtqivxHx_8O69USeBODVQ6lRfGDpoCwSF2rBcfksGdwlS1-eQNuFFFAtSZKSd-zMeprBe_2PFdjQOw1bXvA1iosQys1HA8YHkASsm3V5Nvc6CAdk0xkypvTf4Y9QLrPGzOmjCppDzJAJTSuHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
ویدیو زیبای و دیدنی حمید سحری پس از اعلام خبر خداحافظی اسطوره لیونل‌مسی از تیم‌ آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105254" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105253">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105253" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105253" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105252">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv5LhDVrOxSu-aSP3lvnWH3wMaXkVSJ6JnFdFLpVgmAphWZ1adVKK4NBcwVw1o8u9gr5VrFJNQ_1qXngjfsX8No4R0E7K3rMd_2MZot75oUldZJbkQ5130r87sjiBXk7phdZ93dM_cImFv4dOZBcVNVfj9GlQIPIv6kky9DvTsZRwYyUX1WEzfc9LmakcHDoNadYasYgBU8e5YWNTGhl_n7HQKqhgDVSIttxKKmq1Wc_Sbn1J1BJ1bvrkJbW-b4d2X-akLKCXIv_5UVeIZbDQt2yGmJvE1xjmvK_qWkiyu0Xoto4XS-WTDVraIl4D2Z9MjqxaJ5wL8w8K8_KtOINMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105252" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105251">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=jBfX0W_8yinl9ilBNVUuLScdEVHXSPfM8f4ZUtZuVrAcALCTgsWr5P0k6m4a58tCF2L5LpVi1oI5avGPQqChAF9lNqoOjiC4Iuis9gVGhVCn6mYRj6DtBLV3L4oGbRPFQhYnqyoslw14w3fn2O6lO26zkm4DabhtXCpXTOT2d1glz5kkntwEQaIdkFnUX8XCXYvODCTlZTae5U_Z7mfB2gcXpkOqYmhK2jHF_e78RzhZ2Bw-qN4rsshTSh2qBNHChY5FkPtE1IdaAT5PxpOYDDCNFQRHCRutMlt66CfSyaBDkCjFXhBPqbZZdGpyowz_EfEPF7R1Vd7R3JfDaVsnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=jBfX0W_8yinl9ilBNVUuLScdEVHXSPfM8f4ZUtZuVrAcALCTgsWr5P0k6m4a58tCF2L5LpVi1oI5avGPQqChAF9lNqoOjiC4Iuis9gVGhVCn6mYRj6DtBLV3L4oGbRPFQhYnqyoslw14w3fn2O6lO26zkm4DabhtXCpXTOT2d1glz5kkntwEQaIdkFnUX8XCXYvODCTlZTae5U_Z7mfB2gcXpkOqYmhK2jHF_e78RzhZ2Bw-qN4rsshTSh2qBNHChY5FkPtE1IdaAT5PxpOYDDCNFQRHCRutMlt66CfSyaBDkCjFXhBPqbZZdGpyowz_EfEPF7R1Vd7R3JfDaVsnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
🇮🇷
فرشید باقری: خداروشکر به پرسپولیس نرفتم؛ آبم با آنها تو یک جوی نمی‌رود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105251" target="_blank">📅 11:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105250">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=mgLRGk_xhbsGl9E1j_zGQWImd-Sw9aPhSIRjug2fzgV8D5YSg9yWK7rBPyPCX94gihJ9H7dZfNnR3baL-fYYX_I-DI4IdfNXELKhX9RT2k6ZEqgijsRCuXf0qbObl6xOfc962IciD8vr4wdx6mLAAo3zbm-hzQeg1JwzKZxHxssRnHsTC3uwC2vrtzTnYLjlpfAcjvZLNWDWhPnrnv2C9iskYmlnTJ9L1ojWqRb-5zjmgV67uXfOZV-PrBCXS3otW2cbf3ojXGUGvpjXlohrD6i-t_jx6DmBwRY9jWtQK0vAs7YFQvJ_OIqwHLFCDVm_sS96pFDm3vv6BDGlGhUMgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=mgLRGk_xhbsGl9E1j_zGQWImd-Sw9aPhSIRjug2fzgV8D5YSg9yWK7rBPyPCX94gihJ9H7dZfNnR3baL-fYYX_I-DI4IdfNXELKhX9RT2k6ZEqgijsRCuXf0qbObl6xOfc962IciD8vr4wdx6mLAAo3zbm-hzQeg1JwzKZxHxssRnHsTC3uwC2vrtzTnYLjlpfAcjvZLNWDWhPnrnv2C9iskYmlnTJ9L1ojWqRb-5zjmgV67uXfOZV-PrBCXS3otW2cbf3ojXGUGvpjXlohrD6i-t_jx6DmBwRY9jWtQK0vAs7YFQvJ_OIqwHLFCDVm_sS96pFDm3vv6BDGlGhUMgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وضعیت سخت‌افزاری ورزشگاه اولدترافورد که وسط بازی از سقف ورزشگاه آب میچکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105250" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105249">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWHRo9C4GOjpqsl-bpAQTfOogo1E_CNMgASi1ryOzATFfgnzbCLwamZQKOV8dAN25aiXx57k42EL46oxtXwhJTJ4DhUpGpQYLjDvI4tdGgxJVcVpSgNC_xLBLTr1AC7llxI-KSBMdj_qYpQwmRzs5kiT2uCnsvEKqEzhyTX57iRg3CmVWvgNcHOIwyYZ5ORtBSzHdZGLUWi6AooKOUSHBOmlYFcYvPQFwlf2xU6X_wB6NKbHP1E-DhG1wEazMn7qwh8YmgDp72bsUnGuqELvodLAe02Qq3ocriMCQoq5zppcJFTx_38040uV_htMcjUU4AqeR3WAwsXJhMkx8oRAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105249" target="_blank">📅 10:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105248">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=BTfUcl4kRi89cBtHXQ_JXBEXBPVuQ1N4JWiFjCZBg6RPfaYOeQTa-QBYlvAv6aC8Wi5TQ7WPEvrP16q7cka0OSVkyMuAATw2NofNA-Dc0UoAEYN_A6TQBY6bEmjfXJZ3Tq2Vb_d3KO0XXXbgIwuk7IUIL28DIqEqF-w9keAKcX4-kKTAjdSE8YAJ7lpni8gUfyeptlFoBEXPMTrI4ic4E1BfJF3E-kx5-v9tkUjTgBxSeqiEOud6g2oX8Ui3X2I7jZH8wJv68u9we5TwncePuzTQx73ffV1rjHAKLKXmeyrRytACbJARoKVZfPPe_R8GR0c-4DWrLBIGruVgluRZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=BTfUcl4kRi89cBtHXQ_JXBEXBPVuQ1N4JWiFjCZBg6RPfaYOeQTa-QBYlvAv6aC8Wi5TQ7WPEvrP16q7cka0OSVkyMuAATw2NofNA-Dc0UoAEYN_A6TQBY6bEmjfXJZ3Tq2Vb_d3KO0XXXbgIwuk7IUIL28DIqEqF-w9keAKcX4-kKTAjdSE8YAJ7lpni8gUfyeptlFoBEXPMTrI4ic4E1BfJF3E-kx5-v9tkUjTgBxSeqiEOud6g2oX8Ui3X2I7jZH8wJv68u9we5TwncePuzTQx73ffV1rjHAKLKXmeyrRytACbJARoKVZfPPe_R8GR0c-4DWrLBIGruVgluRZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری شب‌گذشته داشعلی‌منصوریان از فساد شدید در ساختار فوتبال عراق
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105248" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105247">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPwWc27qiO7U7X0qDfGzRa9GiMzR3mMvKHSYR0TQGtFU4gHTmdOH4QF9NCW98i5F2MPhb-F1CmwG3u7cUinMPmtbyi5QWegEJH1lYUwWlJzcTH6aFj5riuTdYSafq8JQjCoVorZow5eXcsYEDOyFpEN0yILD2XPG5O016-xkTU_PbFB8WXKNuiRohRKqFt6U3gnY4gT6J3n-oigzCyqLvkD5FGYy7qh7lSsuuPqMI8lsCVIzQBiGuYI37suPBDci1rnOxbm5M-VkLEnOsMNw2eTCs-4qFDSigRTv5wu8LUtNI4Ma1T4Hy40CQ8w6vaqNSVmojU8s_V_XNFyaDnAyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
با حکم کمیته انضباطی، شکایت دو تیم سپاهان و مس‌شهربابک از استقلال بابت بازی غیرقانونی یاسر‌آسانی مردود شد و این بازیکن مشکلی برای همراهی استقلال ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105247" target="_blank">📅 10:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105246">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=l7hzNxkmVKrAfDUqbYH2FMSjK2WU-JqTCKOYG7N9x_8viLgTBM0j03vtrN67RY7ckIKYIT5ciVrCmb384qS0UczUlwtBLydnMrpFjtBUEl-tF0EUsD8Nz7iTKmjfH4SE8wLtP3v1j7JVtxqIlOiUt8xjP5ejgLiM5YKTEGaX3YGdxyvHD5igR3MRndJGecY5fRCGfatu5LP3JbEJGZu6ygCVUYFrXgX0QJrun5ML9Z9MsyF_eYYx_tbl7rhCN527UEYNVdpw1hXCDIyqn3SeA-Leb9vaaZxD5HuGDe-bu6P9YLHjvLqgv_vXwJbPK0aqlimz9PeSea9DnZIhNyw6Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=l7hzNxkmVKrAfDUqbYH2FMSjK2WU-JqTCKOYG7N9x_8viLgTBM0j03vtrN67RY7ckIKYIT5ciVrCmb384qS0UczUlwtBLydnMrpFjtBUEl-tF0EUsD8Nz7iTKmjfH4SE8wLtP3v1j7JVtxqIlOiUt8xjP5ejgLiM5YKTEGaX3YGdxyvHD5igR3MRndJGecY5fRCGfatu5LP3JbEJGZu6ygCVUYFrXgX0QJrun5ML9Z9MsyF_eYYx_tbl7rhCN527UEYNVdpw1hXCDIyqn3SeA-Leb9vaaZxD5HuGDe-bu6P9YLHjvLqgv_vXwJbPK0aqlimz9PeSea9DnZIhNyw6Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
‼️
عمو رشید دهن سرویس درکی از دیدن برنامه با خانواده نداره
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105246" target="_blank">📅 09:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105245">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=WKKmopdeG7UrQGsMXzi2l9Sc8RsauwQzQ0aj4M2BxVlN_JnaTdP8IgjdkzViEaOZeir5Wb8SKm069vv7mWbsnc_NihMtnoNJSqtlrKtNLR4hvjjhkAV_KaluasKeqDKqsj3NAtMocPGezQbYtCWBDfCeNDDlJiOq9UzW4_8Mno3Bk7rkSNPU-PcKgkmGlEHQO607H2XChHYfKNxwcPIIfzuhe4h04uwhsrAarmQAItl8bLNiRHejhsl-NFPb1dNQQwqWCpG3gVglppFVykRgBugzT7NK-J6wy3ckVIXY_o1YTTMlwvGGgDY3q9X75Y0djgDElz3MSKehlLSXZbEUt4tEgsLK_zoEoQMG2SkZFlKOf3nSxdyAC1m-Y0Etf58xDzdj8HCNFMelYzirZFEe5QBOMLcpnexGQx-idoyw6cjyxNPVERCo1qvdTj8qGGXKRaMXP2JwMgu_9mVQZ8_-Q2-TVvb18P7TTloeND813HRKknVgdE5471v60jp43ggHtBicHiAEeCdG6ojWwDWXZ0xU8blal6C1U1Rjb7CfH2LDQp40Ey8lQAAETc-2I8bWEHn19LYQPSxAca2XlmkkILlux8YSYHCrvs4DBvXDlcCz9ZGPY17ZfwEKhNhHSZbGYWVcKaPcRoBY01D1z8e6DnyibCScnFsnf4Tv5_5wnOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=WKKmopdeG7UrQGsMXzi2l9Sc8RsauwQzQ0aj4M2BxVlN_JnaTdP8IgjdkzViEaOZeir5Wb8SKm069vv7mWbsnc_NihMtnoNJSqtlrKtNLR4hvjjhkAV_KaluasKeqDKqsj3NAtMocPGezQbYtCWBDfCeNDDlJiOq9UzW4_8Mno3Bk7rkSNPU-PcKgkmGlEHQO607H2XChHYfKNxwcPIIfzuhe4h04uwhsrAarmQAItl8bLNiRHejhsl-NFPb1dNQQwqWCpG3gVglppFVykRgBugzT7NK-J6wy3ckVIXY_o1YTTMlwvGGgDY3q9X75Y0djgDElz3MSKehlLSXZbEUt4tEgsLK_zoEoQMG2SkZFlKOf3nSxdyAC1m-Y0Etf58xDzdj8HCNFMelYzirZFEe5QBOMLcpnexGQx-idoyw6cjyxNPVERCo1qvdTj8qGGXKRaMXP2JwMgu_9mVQZ8_-Q2-TVvb18P7TTloeND813HRKknVgdE5471v60jp43ggHtBicHiAEeCdG6ojWwDWXZ0xU8blal6C1U1Rjb7CfH2LDQp40Ey8lQAAETc-2I8bWEHn19LYQPSxAca2XlmkkILlux8YSYHCrvs4DBvXDlcCz9ZGPY17ZfwEKhNhHSZbGYWVcKaPcRoBY01D1z8e6DnyibCScnFsnf4Tv5_5wnOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
افشاگری پشم‌ریزون عادل فردوسی‌پور از ریخت و پاش چند صد هزار یورویی مسئولان تیم‌ملی جوانان و امید در اردوی ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105245" target="_blank">📅 09:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105244">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=Au449o3krOmtP1O3DKI7xdpBlM_xdD-FFT8q4ZFrJmwk_b4prNtugJ9tjKDg-ERPEz5O7eSwq44l-qZt5Ww6wqAozZwkzEeLozSnoVGgWMwr_0BqTO4yG1_rOvwD3ZAqFqyWG4TgPwGraJAkEKKAozym-KOsK5wth9TvzcC2YNlzw3Vv5P39gvhgBWzG5uLpI5oC7oXL7aYdrq1p6sHpV_QE51gR5v1rZ3CcABTiYYXJKrtsop13-3FtX4DwYtleOOLVkHFFF5sRFxHlqNcJsyISnwocY3duk4-B4m78Rv79Whp98wJapQeQk6pH8kH7wZEKeaMnbsFkEV8TU5YFQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=Au449o3krOmtP1O3DKI7xdpBlM_xdD-FFT8q4ZFrJmwk_b4prNtugJ9tjKDg-ERPEz5O7eSwq44l-qZt5Ww6wqAozZwkzEeLozSnoVGgWMwr_0BqTO4yG1_rOvwD3ZAqFqyWG4TgPwGraJAkEKKAozym-KOsK5wth9TvzcC2YNlzw3Vv5P39gvhgBWzG5uLpI5oC7oXL7aYdrq1p6sHpV_QE51gR5v1rZ3CcABTiYYXJKrtsop13-3FtX4DwYtleOOLVkHFFF5sRFxHlqNcJsyISnwocY3duk4-B4m78Rv79Whp98wJapQeQk6pH8kH7wZEKeaMnbsFkEV8TU5YFQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو خواهر پژمان‌جمشیدی از برادرش در بدو ورود به کشور کانادا پس از رفع مشکل ممنوع‌الخروج بودنش بابت پرونده اتهام به تجاوز !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105244" target="_blank">📅 09:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105242">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=rCIeuv7HSlqkiFwaiFasSXZTGJCu4idrUbbCQOkYq-c7Dg5ZU24AKx461Iwv6KhYjIlSlR7-H76v03hQj4joeqfpGLyLmZQt6wiZNeTiIjGOrG-AV-gjF5O3q8rFLzr212y-0_o-oYTUnjnGgE20MJuAvdz44mU_DFz2Rz1UZZPV4Zt4EmElk98uHKPiU90beSYCzOdH7Uzke39_BrBDc9lKTPXQw_W286bVkg1rEvE8p4e1Qof_4hh7JQjHiCyin1DxSDLqYadZGBQbm2bxX70Nld1aCnBOvQq8iUY4qpu_84v0XSHuXhf5J2amBVbrprc-rLAS_e0uLxAj2BKS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=rCIeuv7HSlqkiFwaiFasSXZTGJCu4idrUbbCQOkYq-c7Dg5ZU24AKx461Iwv6KhYjIlSlR7-H76v03hQj4joeqfpGLyLmZQt6wiZNeTiIjGOrG-AV-gjF5O3q8rFLzr212y-0_o-oYTUnjnGgE20MJuAvdz44mU_DFz2Rz1UZZPV4Zt4EmElk98uHKPiU90beSYCzOdH7Uzke39_BrBDc9lKTPXQw_W286bVkg1rEvE8p4e1Qof_4hh7JQjHiCyin1DxSDLqYadZGBQbm2bxX70Nld1aCnBOvQq8iUY4qpu_84v0XSHuXhf5J2amBVbrprc-rLAS_e0uLxAj2BKS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های عادل فردوسی‌پور در اولین برنامه فصل‌جدیدش پس از حواشی فیلتر شدن سایتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105242" target="_blank">📅 08:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105238">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PD6Id20dD9okMT-WadJM06yYkWVLHbVZZnalR7VpZjzrPNTHVakE_VVe3bRESxcujpLrh4n3GDxcRyk5p-r_sZE7HZQdND03W7ZZS_X4BsrLhgx15J0iKb8oeupEZ1FkHsOrbrLZ4g9keN-Bg40Ru4StGE12P5d1Zxo4aeBTK4OXKwDzDRQf9BBWb1zGV3OXkw7wc0V7vptPzdM9BLgpNFuzyfyySbH7Rt4pR4GCRCMlntm5sJnQ6tE53Rq3q6_skGsE0kkPgGdsmnpJQzvi1dSQGB6PjKhnfCctt5RvkISNO6d55QMSXoa-QQwdu1-ipWVh_csBSdgte0se_9JN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیك: 91 پیروزی در 120 مسابقه با بارسا.
🥶
ژاوی: 91 پیروزی در 143 مسابقه
با بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105238" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105237">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YA1vZhx6tPIPKZDuVwC9u6JtH6tAfZJYJW4PtkZz4-F6GAP2mqDP7yiR3SXJnAYTsJckxXQK5kEvtCoo42S2MBQI-a9wK-Ua2dX6HB94_HPXj9Xl85bxtaDNd0DC8D7sg4tnlZ9nM2uUfJjjhkauwUh7XAE0SNq876Iq_VLI53YDnrEdAF6hYJxB63_WGW8CMVi_pubT5yoQOb0tK2OPj1X3nXAaTT0CQVC2vnsREJnV9DIlhThQzZiTi9lwKpn9J16g5w7W7iCv4XePj3kRvkO3cgUjpe1UOxQKLcUxzSmRRk5vs3gEPedp3JItSrqsaGAxtaaHFML4dmPsi71JeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: مودریک از چلسی به تاتنهام با قراردادی قرضی HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105237" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105236">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QesEytxYuNCdVF-g3jSuF5kxN5pru0iJ9geHvS6rpIynzWMIz6yxrWDegYQWjRvEaFgNasjISAzJRNXaBuESbt0uEWnbNmkati1aSiIs655kz9McB_PoFO-aeOUYh49fuyNBZGY0AW7QNGeFxGH-VHXE5qA_H0S-bVIWP0ztNF6642HbAZJKKDVjqX1nI2Skkw200jQUWK3Civb7jJ4jAesWmV92YYq0yQ9rKyCbrxzQ9jOlnRk79R7g0AM-kJGgCHY8MabIarmSN9To8rOalo72mMweVk6rcySsnxw1AsCZioLqFQMXtTSYMmOMYgwrSp2q6K935jX6j-S61uF8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌سوم لالیگا؛ بلوگرانا روی نوار برد؛ پیروزی پرگل در شب بریس رافینیا و‌ یامال
🇪🇸
بارسلونا
😄
-
😀
رایووایکانو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105236" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105235">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">لامین‌یامال دبل کرددددد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105235" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105234">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بارسا پنجمییییی</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105234" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105233">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گگگگگگگگگل</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105233" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105232">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105232" target="_blank">📅 00:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105231">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی استون ویلا 0-1 آرسنال با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105231" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105229">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلگگلگلگل چهارم بارسلونا با دبل رافینیا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105229" target="_blank">📅 00:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105228">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🎙
توضیحات پیام صادقیان درباره جنجال سایت شرطبندی؛ من اصلا نمی دانستم این سایت چیست و فقط تبلیغ می کردم، تا الان یک بار هم وارد این سایت‌ها نشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105228" target="_blank">📅 00:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105225">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلگلگلگلگلگل دوم رایووایکانو</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105225" target="_blank">📅 00:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105224">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105224" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105223">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105223" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105222">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=Q6ZB9XoNwBHTzaeUanaez_6Sfqn7UzSBBh2GYo9vZOifW_DaPVhJz4r4dLY4a-NmQmCl2xpL9qrFNi6bkkC6MItpdZ1PcJy4WgkZpX1AI5ifu9A6mzrcsaV7Lm9kNLlqkUYHNDO4g9maZ-rbnriMTwzylELGfCRJyk5xIlnjD5MJd5MZVrxXP8GHSDg3bXuDHPbJnxjqGMHMGnnu6yDJMGJivqtUb-10H7DzEIubmLXmyl93jPmqAdyTrnb5lruZ1z7lQq5t2rdzQcSS7S8r9yk3krXe2IKabYTZXqFHhfzrHaJl_40q1SQB1uGzH_qvNm2MNFnIkdX7ltYiaoCvqrZ3eWLPFcuxaUf-I12sXHMI8QbenGeeJOM6DbVnYwgsR3xUP3eahPSjuILwvyVEM4R4WdZXH-J1HYS6Pc-OWLJiWQSSwomeJOZCEInTxPg59_4eXHh_N1vdcgdj-pKxwEB847modfszxi8M6VA6EPU_vbqSyK8mhkhz67AYyebtI393Nf7lHD2KEJPtgzktPqgCJcjqd4rG6sjsFjTfm09Ru2deV_MkUsZB_NjVPZc6Jr45sL47tWtu9VyW-SrcxvFMRnWQG4I7V00txfnI-OzU7_DkmL4e0jaJtqVEo5XE3IHM820qj1Vk53vvUNUqg0XK7M2CvxsjhkTe1LMUdSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=Q6ZB9XoNwBHTzaeUanaez_6Sfqn7UzSBBh2GYo9vZOifW_DaPVhJz4r4dLY4a-NmQmCl2xpL9qrFNi6bkkC6MItpdZ1PcJy4WgkZpX1AI5ifu9A6mzrcsaV7Lm9kNLlqkUYHNDO4g9maZ-rbnriMTwzylELGfCRJyk5xIlnjD5MJd5MZVrxXP8GHSDg3bXuDHPbJnxjqGMHMGnnu6yDJMGJivqtUb-10H7DzEIubmLXmyl93jPmqAdyTrnb5lruZ1z7lQq5t2rdzQcSS7S8r9yk3krXe2IKabYTZXqFHhfzrHaJl_40q1SQB1uGzH_qvNm2MNFnIkdX7ltYiaoCvqrZ3eWLPFcuxaUf-I12sXHMI8QbenGeeJOM6DbVnYwgsR3xUP3eahPSjuILwvyVEM4R4WdZXH-J1HYS6Pc-OWLJiWQSSwomeJOZCEInTxPg59_4eXHh_N1vdcgdj-pKxwEB847modfszxi8M6VA6EPU_vbqSyK8mhkhz67AYyebtI393Nf7lHD2KEJPtgzktPqgCJcjqd4rG6sjsFjTfm09Ru2deV_MkUsZB_NjVPZc6Jr45sL47tWtu9VyW-SrcxvFMRnWQG4I7V00txfnI-OzU7_DkmL4e0jaJtqVEo5XE3IHM820qj1Vk53vvUNUqg0XK7M2CvxsjhkTe1LMUdSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
ادعای بابایی مدیرعامل چادرملو: سه‌جانبه را برگزار کردند تا پرسپولیس آسیایی شود
❌
صحبت‌های علیرضا بابایی، مدیرعامل چادرملو، درباره پرونده جنجالی معرفی نماینده به آسیا/ رانت اطلاعاتی، دلیل گله از گل‌گهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105222" target="_blank">📅 00:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105221">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfRby6LmTbKTs2svfC1WFRzLVo6DmzbEyfWgaYHsho6EmIVWF9f3MonDbi2WRchwlXY1PaCw8-UWz991zBwWx9dBqvTiuJUUJjwHP26nWIM0HpeHPyDFUxlzm-gKD3CD8eH3svfV4iN8opmk52DvxZ0GJAa4AXiE3quKC5nCsajE3BtreE00WgTWRDUD6aG2TQv4PPPN0gNCOC2y-kdQOObQ2RvfRFwh2OGy5jXq38PTrcRx-Xgk-yRpzjkdjItMFvPLhNfAegbBhlYMo8SIt0UdMT5dY2NOv60Av5L87Xo8ojzcLtyEMAdsKCsAE4TdZMaKefRJ1s0gxcSLRS4vIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105221" target="_blank">📅 23:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105218">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گلگگلگلگل دوم بارسلونا لامین‌یامال</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105218" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105217">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گلگلگگلگلگلگلگ تساوی بارسلونا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105217" target="_blank">📅 23:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105215">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل اول رایووایکانو
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105215" target="_blank">📅 23:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105214">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=TzPlgB6jbVJhWbH0z0ZmquaKJZnbYwu00GydZdWkpiUC6otrDHPxMFYrGzbhutD3HlCHMDjVNbGZN4eqWHqtCXywFxPkOPw8u9KeQjguQMqjmI1wSAmE1brVtYLrLHldNTkig94hQ7on1MQrLnKvNHf4ILbgq-xwZg_q7EnBOY2F1lkWpV8KSXjVHSwYEuthJVAVwaFA5hYjoU2gXsQer8TPlxgq6GRfJ4-5zJO_8gflNBiBBWMWXfODyoa9cJm-rXNDYJFpe5GmRtDM_hmZSodD3FK6WtR929fpNUpuxe4xzzNkDLoJs0DprlbRxj8GDbI_PV9rjBRro_b0lMzeOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=TzPlgB6jbVJhWbH0z0ZmquaKJZnbYwu00GydZdWkpiUC6otrDHPxMFYrGzbhutD3HlCHMDjVNbGZN4eqWHqtCXywFxPkOPw8u9KeQjguQMqjmI1wSAmE1brVtYLrLHldNTkig94hQ7on1MQrLnKvNHf4ILbgq-xwZg_q7EnBOY2F1lkWpV8KSXjVHSwYEuthJVAVwaFA5hYjoU2gXsQer8TPlxgq6GRfJ4-5zJO_8gflNBiBBWMWXfODyoa9cJm-rXNDYJFpe5GmRtDM_hmZSodD3FK6WtR929fpNUpuxe4xzzNkDLoJs0DprlbRxj8GDbI_PV9rjBRro_b0lMzeOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
در اولین معاینات پزشکی از مهدی ترابی مشخص شده که این بازیکن دچار پارگی رباط صلیبی شده است! معاینات تکمیلی قرار است امروز انجام شود و نتایج آن اعلام‌خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105214" target="_blank">📅 22:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
مصاحبه‌های منتخب هفته چهارم لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105213" target="_blank">📅 22:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=PpsdLgFjX0YPlCZAKQXcaWWhH1nlf_B8FUpJGXJnSx1feOoyPLgIJfbG6GED7TyQRfDtnsiT1ABWVdxdsLyaZvTSfOQifbuMdBtAoke9yiE8T0omBU5ofLFfkvz8xn5uHdGW1WSZNy6efOvtbZAB5nhSUM-vnCz4Ujgv6oFQ1_w3c_734g2qJnV7rcaDk1xQyLLZESl6zOk64RMdfIalPVKwT81PvllMBzeCumuZtb_TfSDtmSrZ5T7I626ox4wjFsJrE2ZFNdDapWxdkUauUugXyi-_IN8Bdj48vvHzvzv-GSuEm6XZajqxDR8ioaV9nVhHRHOOvQAqocf_hfoJaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=PpsdLgFjX0YPlCZAKQXcaWWhH1nlf_B8FUpJGXJnSx1feOoyPLgIJfbG6GED7TyQRfDtnsiT1ABWVdxdsLyaZvTSfOQifbuMdBtAoke9yiE8T0omBU5ofLFfkvz8xn5uHdGW1WSZNy6efOvtbZAB5nhSUM-vnCz4Ujgv6oFQ1_w3c_734g2qJnV7rcaDk1xQyLLZESl6zOk64RMdfIalPVKwT81PvllMBzeCumuZtb_TfSDtmSrZ5T7I626ox4wjFsJrE2ZFNdDapWxdkUauUugXyi-_IN8Bdj48vvHzvzv-GSuEm6XZajqxDR8ioaV9nVhHRHOOvQAqocf_hfoJaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی با گابریل‌ژسوس خرید جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105212" target="_blank">📅 22:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC3ovKL_nkYw9hskYjyX_ph2OEBeNxp_zo2JqS9t_9ZgJnfhi7I7UhuFLPsfbtIq7Vm6tCH4qbm44GUZxnUZPDrvXwKNW6csi0E7XEgV1ahu8wvTPKDe-7mAF0yWODnxtu9k4yPUW4g4AzfGWFUjUKTDsuIUVKgUKq403h6zyFepEiTyNPd_COS6202_cRe1DQFR3E_tvTDkgTzHvNUcQiz673eXnGbOjlP0lnCjD7E9ZKukC8bnLpfTvWA2AjFohPtm0u1VolTUAVIuScLxSu8tQ_XPuyJM28CuZf5eUK5-ZCgCVc6Xx4C4iMQEgFC7FwZoR1rFC-gA4n49PB5CoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ایلمان اندیایه از اورتون به منچسترسیتی؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105211" target="_blank">📅 21:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_DueLXPYIU2lpcO4zdqn6RxO0kn_c6fKGcDImrXxQmVTBegIPXQ58Z8hkJKwjUERuGKIilcTIx9w-sR4Vw5r9fAKxcm-QnNGWhchqfUxM66P8uyuCeYSQFtJXXmi2gSQfqZV_SWNfsn4AnicazktbklefrP7zEcfzWzhl_2Rk7VfDa6yp28PhhnhPDbU2QASTTaA1C6qZ1vGswe3hzaJgwbcgtr38lMF-9ytsZUThVl_ZjO3ndbzhCGzlBIaOWE2lB6WQxL43dbb2zYItG2WdK_r0JZ6db1eKIPMe6w44FOCDCurmwobirhUePvJrF1uTn4oIvmg_Zo_GvcY9nkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌سوم لالیگا؛ شماتیک ترکیب بارسلونا مقابل رایووایکانو؛ ساعت 23
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105210" target="_blank">📅 21:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105209">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jejw3vCMFpL-UEpQdRkCyZk9_X98Rz1rTuB4Lmhsh8atNIWcBgZxMcgkdPFuNt_eVVeWHMBVXE3H3_cHrXaimGjL38lxPBgvvoCDFSLzEa5dIV94Cb1BVsgxAnXurPuFEmPbAuL68DGPxq5cecmjBl6_LnOB-fqaUrgbh77fFwNg0LRf3UaQDK2ryEOXsBudIe5UQT7cY4PXSQk0bd_lxUmkK0ZXYwgKUDlkYrHnWQ7TFdfDYaqx8FHsPbwUnKwFJpTx3U3MCotoOyFEqyNE1gkNtOSVcbbi4qro0UxNPe82KvSf0-zt05zjg6EnIBG6Q0hj7NbubNo0I0p3R7EqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105209" target="_blank">📅 21:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105208">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzfxrm_dVcpZRRGSOJ_tmzrYbOrBUJZ0J7vGrVpJspPhF1MTeKwlYqIR6zxdbpReQdJ58ElCxj2BYJzEhH_s-k53QRnYXpa0tTVNCA3UWNTdaH0NECpehg7Aus53RNh0r9r37hT8r0VTqivDDpm-qfBCOb-3YY1FtFkHhM320edlHvQpIeMAfDMdUPi2oq8YztB9K214fBGe2Iutzqvy4wbpZaflUYpH6K1-HUR6DBctJx4Hnx-qRWrStKUjFESgZxs9tSn9gINn4_eTErjyc69sg1ADrQ426uto3YKd06E-CulQfDMn5fRcRiOOUeKtzKFrC_pj0DW26g5p2lea-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: اولین پیشنهاد تیم منچسترسیتی برای جذب انزو فرناندز به دست‌ چلسی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105208" target="_blank">📅 21:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105207">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMpmJAZqWEG8jSKh6uubAd3fGn14MHYlXbiodbxJYwWGmAIdDefjaKazUWbnQJBo2WxNL1fk277hyrdgcwz9q2X-bLHvUMqRmZQuMO8B4vKR4ow5j_seetAUWw2Nz4laky8NmBHViLlMi9QupdmCLJkS1SeWFW6BXwGC4xIAu3zJhoF-lbcIBTeP1Dv8DXCymxy7plC2ya2IpwiJjiriFJSDp6UAKO5Z-UfhglTXBSLcWVSV65s1o3h7-0bcFmVn2RPmw9R_STPda1yye3wnO5tVxLyg583OA8cUjni2FjjC0ZjmF-VA-h_KMdkYwwFPNAyP0ByC2LZZvLtt2MxY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب آرسنال برای بازی امشب مقابل استون‌ویلا؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105207" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105206">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWRdh1zOM5sSsW8ZaNTWfAJCOfbjhydCAUC6OwBalaXMWVSU1R2ZiUwm5YFd8Wtz-d66xTUqjnNm_iuWQkNc5eU_Bx3d8SGbPaoTQoFnFmIUXddZpnQ4hzReC712122ZOBC4myXvLP9rOhpMkjRIR4Pwc6fi5vSoHtkLZG5PVC7EUsmIJi9v6oRR2WQa_QE4NJrJ78qtGttE57bFSY61UDOLl2NrcVRIXaI8imt-mj16V63nDUUAQQg4iOEevauLU8l0AKz1zYDeWZsj64tE-k_UpoRBIfF5ZG-UvA3oBY1Y3tBzMx6n7mo615jZTp-b-jdDRv-q6AmuqUllVf_dpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: آینتراخت فرانکفورت درحال بررسی جذب خوسلو در ساعات آینده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105206" target="_blank">📅 21:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbsIAYRgg1cyd2zsmR9PQSWvX0kATExR3hW5ZiZxyGE8r8dsh9YwXNhHT-A0kQIwjf5Se3oRihpb4xvCoFP_SLHb5Gx6hrkLlVuuf0ebJCaJzXFTaaZXoJFCIfP1_PtAYVUlkc1_gW1tkDJ7LtYC8HN69GsY2WggtXySDqqNa4_51aXLd7p46PTMUhKdnN9PhYYt5lZsDRYOct2zBR_msqs3YYbdajeoURdw2XmSClg9lj7XnhXzkCRd8nKzNE2HCDPu9rj3PkXLhbPO_8BfuiFMtXVQ0obfuVKfPjVGaHIzRIEFyXTA07CpKLd51dxYd6kAVzTraK4jUdZC8JPE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105205" target="_blank">📅 20:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk3bud_sX_RChL3hwHjQZ-gThaTGkAjqcQW5V5QkUy0BSkQIiocvjjhLUGoy5e77VhApGVAMYNL2lmw32V607tT2jDMX2TMxSSSh07uoc8POdPRGc7i0q0eilwU4TsVsRcuFIeglhCAcj8t95D48vNttH8tdLejbcorao3ygHNt_JQ7aHwIbbC75BI4v3hGUEvMVjCzQ_CIQmpXLFPDgSt3E7rxdwTz69CDT5FQHcqNjn3FNrFiKNA7F9V47_YsrYvtWkIlWJurWL9mlNW89MWMSWPv5Xi4AF2BiVcxwXWVxHSpaVcy6p1BZB5joHL2rBR9HkJOhZbgMIS63kwMDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت بلیت‌فروشی دربی طبق معمول ریده به خودش  زیر ساخت در ایران 0 گنده‌گوزی 1000</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105204" target="_blank">📅 20:57 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
