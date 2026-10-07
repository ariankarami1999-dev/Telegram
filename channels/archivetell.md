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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 483 · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 519 · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 600 · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=vTEDeV4Y_qx3OuD5OJFkf04C2nMKI0wvv5FL-uKqypew7jCrTYyVSv5HaJPjliYOaxbgvxLcBpImOf8yJky1wefuwHGcch1F9XO944A-RrrLRSw_VlW15dgX3piJSEDpz6hLR1caKXAGeDVkVEqNJCISht3Dt6ptyg3jJcb2t-lLf-FpVSVqDKYwBl1bn6y2s5D2hY63XhXKbkHQX5_W22aJud0RtZDaEQsFZCyX9XQsP5prrhrQ-FCQ6MPXmSsGzDiic5FkzIkxBTUqMXGjalUW3penAqtd01czTfYX5HfkGdH6UEMsk7iInDJiQEMjkhToX7660wPwDfSa9tTzzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=vTEDeV4Y_qx3OuD5OJFkf04C2nMKI0wvv5FL-uKqypew7jCrTYyVSv5HaJPjliYOaxbgvxLcBpImOf8yJky1wefuwHGcch1F9XO944A-RrrLRSw_VlW15dgX3piJSEDpz6hLR1caKXAGeDVkVEqNJCISht3Dt6ptyg3jJcb2t-lLf-FpVSVqDKYwBl1bn6y2s5D2hY63XhXKbkHQX5_W22aJud0RtZDaEQsFZCyX9XQsP5prrhrQ-FCQ6MPXmSsGzDiic5FkzIkxBTUqMXGjalUW3penAqtd01czTfYX5HfkGdH6UEMsk7iInDJiQEMjkhToX7660wPwDfSa9tTzzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPq_u10OhJDa0AMEpJXEwynHY7H05CnwJfl78hnFF1VNgat77CzbXs6q82A_T-Zr8R8ZU5sZa70s29HqqIqtE-rDx9kSiR_TKecRJJmyAjuhjkUbD5uDXA2d4cOYGXFFGZ5Owl3jgQGgYARj3chxo2F84FviEz3ouxTaumhdpczaZLMXgRzrENi3HS368k4UrrqIDoJHFhtlBzVvqQn1wA1UkdsUY_PVzR5OcfEwK1XlAPwlGVIHMAL_SVRnYqNGvccr2O38y_uEwMo8Gt2d718yy0-hg8h4JSZSdoPNNsrCGLMDpOi5oc2G24MaadYXkaDjeHmDZTfNY9gn3yY9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FeO1dsjswYfB7Nmm01tFhPttjXzu6d-keSuZweiaFhM5uEdzJlVL8hvq5811nXGOC1b3EJiujBEHBbEZACaeOsYmQOKaQ5LANEIoiEuyixusCFoAZmlxqsD64rmbnTWanvmRVqQl2fqBWmEZ5QLL-JQRgoq_LXZUBe24CazOUbyBgW366jVhigsG4JuoePWevn5EqLwyb6RvgqxURMN1iKwWFN42Gu__tZGYPSSJrwhyunWvm6BHcLcZW7_w1coxlvNTkw5vydU6gLDd-4yfzgWzzxnp5Vl5jCtaGnYW1CPBlhhvpbUNafE6UiigmmLbmWpPSSo5IYgHw0G8mqvaTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scpubDov3SvdXlIDAGKCuIEajnI3kFuqZ0SnDthU1-DuYWzBPDvmTIOY2vPD4CSq7dP-S5keluoREmslghxIJqUQQJeJ7LjAdaSZNSgCMNFVFsf3BeRyUIY7i18abQmVLwnbZ-JdR59-SNfYdOeOV_Uv0FoAeFV2m0_7mn1wMTZlGemkVytpF858f12wvRu0aASe-ypxReihpFG-5epcG8wtfQkuU-UtM4dP61CfGRHL3v8NL-2865PFPG5Kv0PWM-kKRQ_DXLUQujEYnPX8pXZCVb-u_dbU9cNM2zEp67HwTHsfNC6kIBoUPL4P0scaKbxAvzBYsu7RDkcx5_ZzAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZkg4BkdZT_aj0CjjJNy0mQRaR1q78fbhNAUbgTF_O-K_peXo_Xrctlj1NK-gFQdLqjW_aRdvIZJmqZ6raNqO5JReHXNUOtq1syyF79qNVCp3PoVDp0p9i2sr2NJUEM-HnLeZML8kbLFWbVTQyFtH_elqEffx9qT2cX3-CjO9aHRavewibxpM10EVUZH0APv0yuodVymXCOeULdqRJdoc7QXJJa-J-JVCWy845hv4a_JjLarq53mImylptolOHU_6uSjBsrhVyswolX0ZxO8ZO39sh7DJcDnmJO6UtBl13FSpOvCfoaTv2LGHsDmA53T68tlpzqIIzgvn0Aqpz7rsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0m9nE-R63POwXYnhnwwRN-eva2KJhzZBSZ15MPrAjgMVlVTpmcfm9ItTPN1yVDAjKXwSz_T-GZidjSxunk2Pf2Gk6jhf-YlqehJD4X0N9Cp5el2s_uo_mmkBbVSbb-2Znrnb_sOSks0fNcYG3h1vtV30kxi9HLf0uU2UAkRuZH-cQBLIc8KzCWr_kBEwXd_-5B_-xrnEiuon-atckPwUVoqEzUCEIP0AzgoI-5aGDM-Q0NLES54V9RG9Sj92kE8FxnvJFwRdme20rMEHY7wn7xTfC_oOnKCyeC0TVPqZx2H_AQrEmIpIH1SuWe1MSpmLB3n5gVcg_w8APFpKdP1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UB6-89DKUAYEDOOA_p5ROhXRGp0DR4aT07I4LFvxqdXN-X9GYGMD-0imeVbQYL3S94vQtDOG2hswpYnF_WpxpOk9pWbwXJfAEm5sTTcQ0_MxZjCJZz3BhlthPwnZEmlxpJ7O9_SX0Lji0d_lYgslGKftTLZvylEjNiumjyvthouC6XwXY6YHpX-kQlBpPemvcurRuR_HjrZejyiaGhCCmc9o7EIB4E_eQUlHLkWB9SyWWlWtvZ2XEGp8lYOYoB-qd8EKbRYgzeSfMOqddC8TqTzoRglK06sr_mcEzYLUxEgXSAwTg5nN_pr1I3ihDQS6xwCP2bgyXLHEzml9GvQ1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQyP67oGi0jB1krn84buOfC4R49pJMReM0ryJYfLMyeaHDHAevwq3Vc1Wnb1qabOscSlNkc_pPTLWyIPbLJ65DDv5AifVHiWGRzXd4qgNQVO_5prkcaOMwWT-mDRiM2uiuVGojzmeIsGnr5SWSDgqRpgNpoAnRWT27JhKBKoalf-iL8ZCGXRIdynCtuC_IV44N_OUqemdiEQ6caGEGdO5kBxxl41ps2BjgeWczxwUh5k8kgl7IUStLiNR_iHrfSeKeAFW1LEFhymIYAMWtb6W0aGol4k4arcD8wNJk7HnRxsJ0QlD49tFefaKNjldRuZBN_Fjk9VCQ_Km6rZNGBJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbB0cLYc5ecBLMJr_ujX8IJTRTHam9GlMAkZex0qDqj9E9WJMClMAAJQGj4u8_6Z69pvFSMhm8pJexQ1fBFPUoPEiyIflUegonDUw-O_F-0ifhBJx0xDNWQ8L9RQ1VOdHUDyA72Z0Y7Pygud7uiIxwYbPRcCzabhVf0I5JwoYFFkHdU8-O8V09M1DAkP-QknlQqtC6RzvZpJgWb9gO7eBUnGBnWLhrhSgnDi8DbIiVviDeMi5TPLpwV3xpkeOUD-AEU22Wa3_TBJR8oeI-t9hZRtmtaWG5Y1u1N-O6DTRrfoiVdpU589ylpk8MBz0FwsDQaR8r-EFI_BDWie4CxgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_tul3zJnAvI-vmgIQWvNn2keSTlu_1UYtZoGEdtn2pMGEJUmHde4WCsX075gDX4El_1kq7Ds8zcMqcnIZBceAy32tAjEsIWufHJTUZdJcZqdk34T-njzZ6S3l62bGRo8recWZmmKskA0KXTy8LP0S3i_B83gTGEw9Yi0_BSl3_jbMAkYZDTGPFzPJmmACNaMeyoKjQVP_xDneepB8OpE-ySaPGkB97ao95h7gxpvbF9bYoJMcp4nhVMudUyLRibh-MwgBSUjNxWfjbKFqxA36v_O-wsgmDVIstJRm57qK4zHI1pwA2oLc90lFWR26h5othk7gpGlKP8og583lrWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khG1QPRVnOg56EOjyaXFyjuIAsymPXgqRriFNQtHr4yD8bxoj8r21_5zYk3cFfcCbjz29AYSx9hMbTeCz2wcEs9jsO_i1Oq1M2YXk4UYwsJWq38_wv9G9OL4qTgsKbgc8DDTEnMdzRJ8YWpHEmagso4cR_gquS6YLQBl8zlMCi7lKWeYJcDj6hjL1o446waunLyJs45kz1rGyeZAX_YzrRkVGCru0PlpDvxRR8-wKaIlyEoXAxO_xAPVsWSykHuNenmnA4El87fmSoevNEMEcXxgcZZDgH9j0RhRH-y2ANLEUfl6HkGPxRmm9YCMuJOPKG0ayYgoDA0C9IPlAhahFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arKjXEmwFpcttd3t-gDVmd4P2DYeZ4cKsZzA0B5jMHGzzKjOJgGKQDqW_eFXzEEHSg8MHn4rZs1p8xa1TG9Y88i1td6CzbE4aDdzA-RfV83i-jXwXouYKdA5D9FZ4cL6_R4CP9_njqf18xMDYKZMQmRNucaX3i-T6N-H3BW4r7zPm0nuEQwi0jOdNIv5bKvFMlCb40LijvMFVR-0uQnCB8aJrEImNBE3QZ8edfXCMixYZjQGur3Zassin7UjzNypwH2kwrLvd3NstKlaKobbJReU_mBYzurGYccIUGurQCipXxzG_1JEWWJu-uQiTyHmC5EfokBPVSjANaP_gxz0uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8VXI7XpAgyiExtY0oj7VlaSLJ1m00B8oaobNDEpeNkPmITbKpUN_Ajv6eNxiOrGZdQ-hBRsX_f_7pP4Vf5pYs17sG7hGzbmjOJ3pnVBn7n-dNNCs6M3rxrw7UIrNDivNII3l91x-Idv-xzoQW5pKXtngNkilbknxjc-EWOUga5cIR71nRYA6YEsxy9IXhJETMbATa_Xlpy833nNVuwk61SOUdWHgSt_kzOfo8sJ3AfERi6PSm46pfZZsDCjn2oe90rd6HgNtqsj-Fhb0D6eP_ppw7t4zgG086JZ5ba2wimdOR6ol4GEokI4pMhDXz8pPHpMnNbIggv_dzIUKTlxBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a3SkKNR1YDeh_wnIoX7066pUB62DPWjV2QPR4vU8JtDZGWnsHqI_vg8mUBOlvGyrZ3avaWnsUnZ1pHUoqsVjxj_MfaA57fvOLDmUoGAnV3xu58sg9o1NFT9wqHdGDlpjWAZMRzSuGDRqVgdadeFdjc6944AugJndHSwrUT4DLElSSPgJYsjDFJER4OExKhGLROhsOYXzW5_wNasgKqPqc702f0OtjG0DlShfdkWxXpb_45lOZ0IYqcrMRDmdVkAwZqOKWh_2zYmne1oBAuiLIoFMshWqyRTddTwpnal4VDQajlgeitXxVbe75YxewHVqrJjDpG8aVxcqDW2tNAHyHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVEuVioIeOJfIxtSk9seCaQZkYx2DURDHEn_jA_eG2RxbTXjtx6Y5pGie9lXPcgBkCzfyhsoSfuysPeGuKvj1zNN973OuIk7yCcMHhmE_ZnOBbEJaJ6rfBeni3m56NBdz0r97_5stoktdICsjo90vb34m1Xq9qHQflBmg7t3MObhIhQKAFSNB-EPdeNpccbSu_HrHm0M-FRlqqlIc3uHv8jHLv_XeZQs16T1oHMyVbvvMMItetLwlt2TvTriaGdiVZU4OgLFKbCO6gVJ0MsEwAsQsHVNIBbQEyosPBUQMc2QfImjDvTxCX5gsh0T2Dkm1vIqKRpwP5Y-VuPggaamjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Kgr4dGgkPLWkxidcFeWvx8FLiIHiLBdf_dWJijIPgg0DgyAoGPnAmF4-3M1KrKXHL7VWWFUOLXluhEdEDLBpqaiBOVcDnr86Wd-nDayvkupagCDA5JWC7zLmf5ixQuxV862TL3jeBGQ4rHGV1qRF6VdN7u4b0CcGXc89AWaAYqdHNNq0DAV67_Wg-h6aeBSUzD_BY006UAxapRvLrQlAshFgq38tqCAR141BENFDQVWuakVLuBFR8shLWm9elDTy4DuMY9_AxM3B58cqW1dTGyAtpSlhhxB6SSl5saakcm_EfnVk2DoRmcFlpW1pxiEHqiPVGqaQXW_hVwvKDBFgQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Kgr4dGgkPLWkxidcFeWvx8FLiIHiLBdf_dWJijIPgg0DgyAoGPnAmF4-3M1KrKXHL7VWWFUOLXluhEdEDLBpqaiBOVcDnr86Wd-nDayvkupagCDA5JWC7zLmf5ixQuxV862TL3jeBGQ4rHGV1qRF6VdN7u4b0CcGXc89AWaAYqdHNNq0DAV67_Wg-h6aeBSUzD_BY006UAxapRvLrQlAshFgq38tqCAR141BENFDQVWuakVLuBFR8shLWm9elDTy4DuMY9_AxM3B58cqW1dTGyAtpSlhhxB6SSl5saakcm_EfnVk2DoRmcFlpW1pxiEHqiPVGqaQXW_hVwvKDBFgQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk-Jd-Xb9-6ixhUHpIJMKwAvHK-5kvWMHNo7-Ji_72ggKhtaoeLjBcnjrC18Mx0sa5L4HWzEwJQx7aY2laq1H0yWfZDgRD-wGgi0JQ1StuXHmKY3CSrC1_kHG-uyfbyLfJrqLcxyxznfT3YO4zBuktP4iAtxz4fXVr_90k0gg0NzwGmcIyxlQrZcsBxoWVc_OBmhm5WHkpBPU9sqED3eMqjtFQbgdwjkna3nVd9gMave97soonlzFVyC69pjGnbYqPNv5G0TBpGui8aRER3K8wyx3gu4X2mzeOV6ZREu4urL2sqYIHHKoP1UpfZ-XPBogsha81Hf2fzY3Ujs2fS-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQRIUAa7xAg1j5P-W-3whKoq63ObpOHil7HlFmRMIQ-xMaZ6o2WAyW2CvBafe1MGDHb95hi5mwTr_YJD7awdRq1HYpjUoaY9XTZWZTP4M9U-DCGXh5XzcfF4uC4-sr3b3oMGvVhWeBf8NVA1j9pauuwsecBlkiNen5XHy9kw6F_MSPzGyBZ00ir4uyxFHqZcpKN1D3bFgaudRatVuS7UO6owLB2-l0Wm8EwY4ykWioe8-t3oFjsLe7348vWDas_PPZIzpJDEjgp42W_6rbHlLfaL7GB82NcOaaHC_5E1p9qKQI8oj1_RO2LjAu6mwHn6YRpENO_pIJUviZbMCuHxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0zQiTsaEC021OjpVpE4Qs-b8kHCx38gw68g3PsiigObtHRDeNmLNsyP7r-HOLY4cv4lKJj5wprH-d0HnDCS-Mc7RMvp6ruLMBKNV7HodjYfMppbchL52U0Mk3wzrL4E_b07M7U4KmSt7qZAymvyzeg_3T8SuYW1FX6qcwOKEb-Gz4HpDxklDsbhYWBBNMarmL63Tknevh8lHSegStcxP7tGYgMh6knrxnUJc-M743i4T8SdozP-YrekzpoRVtbwVXU64XQ8pgOiYf9xuABtuy-bnJDDQW_UWjGHg4Q79bgN5j5HteIqLnpF4TAJZWKG_5CKqJjBBUWk7YCQlr-k_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTdP5zK6Ct2GlUudrSqpfZvdHPtoPvx-bj2fbjhgcaJ9O3bI8JqfzfU0-5x2rUJDBuOZo1yQXQD6TdtsYbAa5e2GeRGc2XtQZxtidc0PrXfJbCU1qumKM-H0uNu8sSDtOHjzlCHIj_X10qnxwl8jiKZNMYjl7k9MF7Fa7cdBkFR8z2NWetm7LXWq0J7n2Mn0rwQH3SfCcglWDu5WNMe7e7GJFm3hxF2zzGliuFWVGa4_Hqm_DgnzNHkAmoxMebugWG09XKGE5LsMbDwgxs8MHflg0Luu63ZRcmuVS_-iTFEawKHZ1y-I45Mgr5GAYNSSEDmTRTuXolBKuUImLXelcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWJ7qMQznaasLzMvTTHZzf-W1QjNMUZq7L_ZKmutC53tR4ZHW9TqezjG9Fau3EV00t0_y-L90s191LirU8ogRj6ET68RBS1ttukqrq6aSb9OiQpZsgkaE_XYELxK2wAuPHGMQ2F9A3J-s_0oCly6AhLOPQUrR4zCVHSryK0f2e8Q0x9U-4sdsOiY_E5ezE_S9tCm8-SIzSAMSrUwq6ZP8i2Af1RELGddI_EG6bVsRtB6o_pov7nynM1c9ukFUetBUN9CX_b8En3IlLaQnIrobXwbc7o8fzicYxWxoVPzZcV5h1jqiCOpvX8nKnW35Cq27INT_Hqr72Gl3hgfFy5nvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtaT-28XYqr8D3RctfqEEyDQQXAxEa1LSzEf7DEu70EIJUEBk8KBESgxqhm7FUFNKV68gIV1uy8_eGEos6FewGafXHzSirNaORFm6Lwi7pSdt4U31kk9y3p13EXtCwXMyVnmaRDvB40UIPn-AfKuKRF0ovJU9KatJUbflG2jKzWh-gGFPxS3Cw38Y3EPlbYnkAh-wSGnDwatWWAAMNHf1tmdKW2Pgq42_WhAsRsxNj3_DBisTVLhsvkqNO_OK5zHuCkdWULsftgv16w7Eux1rm6hLoqvKt5D2tHitgz2XxV_4l4A-EV69h3-f6AeaaRwQwpYYCCG6orY949erEYI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DFsX2_lGlSNTTGnjB7kJnhgajj0o09idLjiFbNjjf7vk0-_yzwY7k_kzeE-O7n25_g3d6G4RB3msLsM2bG6n37Ng48WyG9QWTX0YF2AuD7DHc8O9qQvjX5yVOJ1ngfDhZltDZ4iVoRMiG4O3iglkMz429yznd8FAzKcUlnYrOUjsOFYbTThVnbGQP7dzE7iADrRvQeOzLowKYUc5wOxC263BRQ_1l87x0sGnVptB_ppEltwSfQE9GWtS7ShIJRiG_X3_TebFNDyvucJWl9lBj0t6fJxbM_YLTtTXB-uB1OZO8EzL-fC-AhXH3g3siXB4Kgr5DheHlvHWqi9Y9UYo8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ff6tu_qOw25fDY6pKWp8md0BVBynsmXhll6pUxNllUyq4wJcM-y15EjuL4L7unXWc2O0UPHjqUplOx5_cl7qbkgkRxo4SDYW2n4LdaQXQrqzdQEWMKTkuYswTXay0tYnAGY_Ye4Rdt1Khqz1GHyrdCl1dmcprD6WwtInwAeWbTWY90hturmmxkzbrsozQdGtlq5tq4MhgTZFFqDxVnRGxYnnUucNKyQYIO04-GSoWZ4x6xrw4Pxct34qY_m_QKisfcNOghYat_EN4C6Xjk4zVV6QfisL7jPVtueDeOr1Ha5ksHl_VdpglC1B7F4AiSM7TLfBeZPitd_fkwuYjHJj6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m4q1AXv4sdDSzj3jas4fPKw2LYO2nkNxbu754o5MxNT6LqjN6Z9e9-H-eORVC9ghtdGE8Q9_L-uaEUA134d1VkPZe2hYqIMfnsUnVMxQH4aLs7cRHvLguw2qb2vdPOlBNkNvqpe2TWZmizcd4dWW0FmIpYOFzzWm-5ab42DiSkx2I7raSaUdt7WYnpBURUAViU_2dXlbl5nWJhgbL70U3ChinOIBf-NZD5PFaa8HDYd_GkEz1gVLe8NAdq1KMdet_zqDsoGDlhSvzdtnyguEY9hsfGyqXFqRhBr4dNI1V71_QNJycza3-YgIjJnhxjhr2ZOt-RhVVRsA1P04IuJ-0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fag8QTWP6qkKcAhhSO9LuEdBgtNBxOdfAQe7r6WybJuCgMdMAfgStawbu74yeoo9U3banzpkRx420cS2TGj-bZdGh5QtD9rc_0Wyv49KNmBr78_smJ92KM-8uW2WZxKIxKHwLQVlz5YCzq1d10hXHRVfPq2EcLxmLYDjgEkWFwbF3eXNteneUWpEEgSb59yzX9esEAODgdw6XE_NH00pIAUYYfgr7ZDhdMqxoaCJ-ocZL497l2FVmWE9ZZDcd8n4DzK2V4ONDqSr-azLTi4Lp8AOLua9_SQ876-55V-PNlkALzkSBSncuQqmR0Wg4ln6VtPq50xWvVfHJ6PYlWnZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu3z5IXx2HFF7uBNIBhHInjHshNSzKu0uiAi7eyQE0allsJyu6iGq7A6gRKHv0nlW1q5Bp5mPWRM6qpbNwvrf-giVlqhwhWgeq84sTQPM4e7KFzMqYdIlba856e2GNdDD5wU74lQWgCgF0qN2_n56c9Yo5zMtWpAkcYu-gGQXDlwBR7FjaGmosqClTMKc4jhvqHwhwqpMHnMDVgHQOCxFOKA3LyVQ-RMJeBMTSgZHbHHHrF-V2SHXD2IdFira4SDpF1bxXfODHIZwh5PAsBciuXygCyiXaRcsq1g0CvL3KthXrqGE1vlE1xaupnF1VXcapnowhaLzRDKe4uA4CyzhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6tpMmDzif2qteTa_iPL-Dbay6groUyeQWaXwY3oiaE5Fa3sUeDeYreqGjvrOn9YW1sfRZo0FROZF3kCYBM3T1_9rurD9fhaBfY-eaFpKLGoBvbTdN4miVAghJYCeSfY8fGjd_innMf8iSOd1c32K6giLmtJS5JJa0Q44AROpoPTr1A-knf4BVDh_OdKa7UwYPZ5ByWblgAtOjZcGftG4dpdE8UZd8uzZ43a-lY_7U6Mn_7VdrUx39iApuvFWfbC83xAwDSE37h5eVI1czfQ6Gep_tlWWofuAKOKzbnoAWq6czc8eiI6G4vM-09-jf6WKYXgARc_x4pf19L7ShHJiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL_pCxgFTXF_GHbWDzRNnr-bDH3spYBb0ozISd49_FECTcq9OaOrJUcYRLcawDuOrY6Y0t8RaPMYk-vmpfKvwi3gUyzYjBRsGkahjAnmiQ97MQIz6YOJZX65SplKxrwA1eKPnDTCUOrEu3stklpMEQ55beUaQvvFMWu7d_yedcaoxB5nM_MAQk64WGNDq3prp7QdwIdBA3ub6c1CjwLUvPqowvpp70pze6CMIF801KVxHK5dK0KY97YRxnP8RWN991C8-TI48R52242SHCdL25--UOVXzdkCCY_noWQiGSSJ5AfXfldo79IVLhn7vWw-2VdU-cDdoJSxz30QDRd9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VNMRwQZ_VqKiXv8a61hZvEcWetzvSI45ITAvZA7D1RVtqkJ6pJFvZAqEVC9RKQFW9Fr7VHD5LbJitrogOLKKdUIxX8mNBDvDR8-lvY6sbQfcmqWglbIMPKaJtWbITBcqX46rdJ-izXuhdLG2bHKUmq434iRGaUa1_syLz-M-Bzch6PnAi4brFOZc7_K_mmLw0_8pM56sGwHRv5ZCaDBKVgbIGFxj_8TKRZBSPNL6AWQBskqSOBPAHgQUEI-YM-F1xoBff-RfyJf-10xr91z-XVtV6WLTPeEFMZX3GAiMKppDMmkpb-c-W5vamiBQFqH8XLpRiPhB2djS_xDOKKOZhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns_pGRs53ueHNqUDTVptuhwV20xQRQLJE4aMETfP3wkSMmaSbE-heVg8pLlIOyVmRg4Z1p7inmX_lyN_fsP_i0jYlWOf-FpyJeQhvF-AHgMBJbjUAWmNSPK3S5MTlne8NsfwAScKUnYypitw5J6OCfNf3iYuMG8peLWFMZIGXQaXRwpJLLu7i9j9oHMbENlHhARvkcwH7a0o7-qmLhwOJ1ronY5y45Aqgql9jaMeVTyoa1avnwBojpIKKsGyhRBKIOPejh3MLDJVni6BQ15DB4iaBooccKt8jeO67qNL4kjTAjXdbN1QViKTyf00s2Cz5F2UdIEBhjbp5plDGjTKgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a40-V07Urse9CkcXBw7m1bZXDqvIZ9KLE7kFj3u9cOVVLWS5F8R3lQaSgk0QXIvOpZgPFlv_M2R5McXBT359Lw00wxjL3XNut8AYcHJB_ysa0LpJGw7parIVjyRVFem2rIXFAiyLUbJvXyw05560gt1D8zciFeIfLzoLS8I1m7OS7KpV9XiyQthfoFxMzuM1-jyDyPF-x8cCepYZwxsQBgoM71U-aS3BHjmRbh0dXsvBsfHxhha3mWG5SPUKdePD0o61bP9Pwr_4NEvxEUK10aT2jHUWh-ilbrlPO2M3yH2RlfpmK5iKeUxQtmn1x2ghDM8dgIJMdwFwijNHoHI0zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXWrUPQ67z0UMS0vxSGu_IYiGAUn8ZynnxSbUSyKWapemX92insxLtIKeEagF6NEVnNHtH0wBoMsnXFn_EREPCkCj2aVjd6iG217SfJtkEoicP7pp99PY6VWm9Axf-JIVi_vkpm250Ym9r1kdHeVJZsxGNBOO2VVKVodvDrQcgURW1vxlbQ1LfQn0H9vYMbHGdL9sq9zJReevZ1z_z1OjqUySlmfIKpWwXEoW3d1v6gs81IqCWAE-LYMUsxO-fmEnnvl7Rhp6DH37oS7-zIviHd3DOMjVdPMz8S5I8B0kEjiCL7Az4N8-XvXH6ucb48kgFcvdUkAKVUJtJrNbSF9sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXuO-r-uqSYHhnQHsL5noPhxmYrGpdlXsB8S_XREyDMxPf2pdJu7pDKcR2GQYFQyHNGi7nIRvjt5IHGKmnN42-kcyOdFbIQTXNdFi-BwDaqJaBon1vKlmA3jfnJDtSIYmpfVlSNXKLsfXUbSBhkwdsB6W1q0vCRa_rZ27AcK61zx03PWBa0ULFkUgKSouarCTFEOvlGX-ALj9OWddd1m9iaPT60cxlUy9WpqdbNVGVKKW42M5_E6VYvQ1efGeGqCvl8H6D4LOJmZ8hJGX0jaCDFJ730ehmH8tQuikjrC6Drt3taBRQ1x8Mzvm9VPaeNrr16nOB3syqu2p4ivlhrkSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkFGfdEHlLKb7V0Hs7oQT8jcUxg5iipO_G6fpjcHMpmgu-zm-86S_CZwCLNT7Mdo8DsaAhgPeYmHGJDMO1BRCVBX-UmOW6CuW8Rzl1lhJWsO3DR3PCMQHCU2d1lPReURdYY06AaC0LlKdSsPTsuq_ssAih_ozDS_1U_BSp9SRZJPz9-QhjyRggv_nV2xpfBAaTtEMetN0sgDravMEgLgBY-NzOLjShmqcW9nrKH9MTW4Qi7hCzhYOAvZ44b3sEnTs1DSa-nLSoev7BL61A5umEU0yS0fRSPTLiQt9WcngBpP3nbL1o5a03zgEsQ2bs-2jLeel3t7N62ZqpRn1PLfIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QXzZo5Bj2tgtCvILZko8oXIboKr109NzpXM1y2U9ubV3UUgf5VKOpgZDQ2FB1HKBVvdtkYzas5jljS5GYYBSUs3kUZUEpmviziqgemsxfnN6lagyG2PBGhRvGDquGOWZERs81GWoX5x7TAPZldMfR6IwlnRi9_zKX4L_ot2YKo69-93_uzqYSTssRzpH2ZFUyDa2CNXj0l5VsAQ23F0TeFKVVeyaR8epDMhRhcatRQPohr1OKqUItN457JNUIn9q6CUmx_qUCTURDaQmoYyGh2NiZQolDw4AytNYBrE6jcR2LV5qs95fGBtLz835eaP7KHOwXXS7kp09futQVbLBOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cpI9m3VizGO-UMl_qSJSW8dth8lE-GkFzKuoBbfvpNyxpWJD6uL77ka5tumPnmrXHGMoS_EDYVWx943p0xfTR5jFHBKjxRPm0pYUhL84PDKk4hh2qJy3VrDjpgM2joqYBz4Hg-U5Vw8Tg8t9kz7YwjXHikvI4R6mYgM0Omr7OJN12pXn0OhK3zM1qNRs17LIDw1dElm0qCAmt0qBE4oRNC7UsYml-VY2tt8SXRRA7UB5JNAIj-FTmaRPtzBHMZU1piO-49x_XPVlLCLG210u8iSpghtfamLsYuMNvc49hGdBN9yhBlnDUW57C8izO5_ho-2WK93GofkyylASXahDuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAGwoEx7DEKqdL4ZvQg6DBJyOQ75MRy0GH12spB7QjG_4EsESZ69nSea_enx4gi6gpdRcsHt19g152TKvPR0lFTJfNzr8db6Vgl7jxOK-tr8rNj3mbPBrSQXHTCIA4KDOfIDi5An_nMiQjfkh97lMcd_pZuB3Rm2ew5Q-oKV5cv5yq5EUIGYFYXuZe3MAdIoy7ENfs6jIbOHG6uBzfKo092LywHArBtdRiytOABzgetW9LcyVZTnz_e428xqeVdCRRdQ95P9PQeXx32mRXBM8vah9IYeGVWpMmi4fXASdioisWJSedNuZnGtmUMD4ROLhlIRH5dc-_qKNSNbo_d2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqn0g5Vg4uBXhUwlCqmM99fWuUSbsXPsGK_OqEDTRroSyB0bh0wc2iF-1Z2AhKX5neVXEh9bXNI39Z7CJDAB2zSx9aGeT9VUkydQAlEmeaAFOzfoqNDg1MxgfIGqj7IXeXV3JScvx7nsbBuIVG6C36m12NrcYdj_YXGCzL2dBbP9kO13XK5VNH_jBofOMOQFVELTU6x4hOW7sOKicoCOvqUu_hPtvSgDc27cUgew6_J3re9UAzAHbZPDIm-U3YY1Hr8G1z2obQEoQrMPxtOPJKUsXtOytSo7RQBhg4upsVpbuBFXyU-7dBzKUO2oqZGhaNdQXHd5hSSUePxXAe6-qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6Uosr80FZE2CNvOP-jgzSVlzrXXZd92_tpYenwu-kY5gH9hQJzrWxEseGX7au_440pUdhJiCeBy5_lXopMh0dOX2XPK5oktqwDCTlzPBhs92YIs-s9GH2pPTM2fQFzirnaTLwXFa-2kGDaNuI-AUGpT8RpNuBciuicF_Jq6eAE3Hh5mJXccHxtJ4h5zQzerjq9iPmy_P5kf4aVgphtwU4jLj525lMfDNaS8sDNfOJGaJFgIQnyYDNVp_BLpc5GPCg4xXoZ9CrYRmgkZBVh-LWFf0RMxgECdMZ_gQg7pYcdamu7AkXKG9NvE2azMUNTQxm3ARvrzRW7QtNpIKScrUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIfPS-b1cy2OKQex-saGkCDVWxNLvYcoQJnhE-83kxObIWutf0vRposcqkH1dbl1JViOZQLgN16xq8hT-PSTeR3pOIdygEK67X58ZsVKixEZKAKBV9Lj3gKeRNX1oWJD3GNkEWZA4z1zuFEYVpgs7GJzX-_rhlxKFVRdCPzdQ3j1xLpdqNshpeZAArAi2NQathVU-NsUu7a-26iyVvwt61fji3C3BTXA9F65TzbtQ54Ec7z5uBLFQCOhp5HbhH1Vc7XdB4P26fbInF5Lj9QPe6hl2dQEUecObmf9Ew6nO3DP6_B8Uaq831Vu-NFIMpn4a0bgwCdX503-Ckc74CnQtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2F9P_xqOWFS-DSizPs92Av3pyQhwGVAQdC0S3aNtd3qVyTKAS-QOFRQcZbHhI9HXC9PNJdchGJ_swbmv7K_RJd8g1rJoJ4keSPC-LlCIssohH-yvYJOCh-arIsD3anitIx3AQD0p8hiXjsq2lFnTVnlRgPDZAH5YOgodw2DVejg8PQIW2-HcaN-EVGLHo9mDEpc9nZJmeah5UoQ6peDutlFacvdLOjY8LLhcU6F4az0bhyhiOXqeIq_DPekvCOjsCF9Ya3dZwzzhpNbKl8YikNRpfhXNzufEKSlW7cgws44Zi0W1wMtUgbDNNHtl66nN7xlU7D-wqwBthHD1593Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfYM2q5Kja4_W-Wt_aZ2A8xjb0lvRLy1MiTc4lZTm5gGMCGozojnpmj-pJ_RqrQQJ_5ytCgVrcDJZNth72PtPbXxuT0sA4LMQUoPVwp4iIu1P-F78VQ56IuTtAJ0jpcXjAZhWSIEdzGqsGz7TJFbU70-uNq5hnpB6DXHDSNKhjvfqbzfHHF5NLMBzFH-IqluiPjdt4V_sQvp5wx3YCe47wo-KqFOvspgrztQkkJhi2LbFWjIggunFNbo8QaFi_rxB13F4Qy4Lu3NgmT7EKplbktUXgxeBXEGflBn9fIJLbuDh_p3abNnFMjK0rPvoN4rFaYjLo7TycWx6fH_LNGfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bO0vM-JRmpF_X24v8xu-ScCodUYruOWsoh7PEE_JiWDWqvJLf7tMl1h2gniUYO_0neU7j5vtNQ3rRRqbfjruNZDMLSE27Xinxx-k83CuxAwE8JqLVVXP999LV5X9ow2xp_Q7J1BeSPnuUniBnw8_4nOkI9sS69AJgJA80505IN3WHy_K3rqVaSz0QhvF2sdAlaLanlBaYuYIiBaq6xSk-2HcALz4vWsGRUaZulj5l8VOURvZM-xfweHVP0HD9kAaarrwUdIXM9hMBzR_qRgBA6rPZrjDx9a4KewsUJ91CrHcI6RP2MvfoBLwWZzD27bSJ8vkulWgai6QN_yoOgaVWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq75hMSQGSSSijaHrjCWRsHuda7CZzXAAuDADBAoIFQXJu14tAeRKE0nisNRXevH603HCPfzwSFrWYpCQxByb5l-ScjgRn3rlQz7vP4iURZkGXg3aGuyPZaSpDyBzeNfykiYeKrQfj1I_mh5DN1DOxtyN-8HBgoCQGOcbGhkuKhUqhj_MaHFFUo2iSmi5dPP6MvmqUyJpTZXFX4R3cS4r5LW7N-unC-VZsPgxKZZfzBpKPMWyT9Fnqjgnbjv4cewFFX4Y8b6Z7IwP8S5gjtNi8gR2wNlbFGcZm00GKnX3zptcr45KB4euwOcoxf7y8CythUgpGq0yG7N92x19cKmPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvxMN7B1xFGUX_fATEWzhhWgLceYoJ1vF-1BujU1bvfnQxSYvq-JBHn6dF6lyfHV1q9Z3j29vcAEMTis5jF4Pr3MbJGoyh3jcJTdLBaZfZSFcRqg9UZyf1yR_qtPlv2YUTbHhoiVLQP4hzVxpjhbnBb928TY4QW2W7TrVYNWOK6SI-KeCCMWEfB6PUnK4W9twQHqSUxm-zLGkfm3XhBefOMT5n54T2hvK8w2wFT7StdhYUsLnEc6vEjIHvZoYu21H1O1jRddXeY59Aoabp1olnPjiWFQfUQSfza4WGvFXPpW4-N99Den7VXE2OZ4nhKrE-e-M2MW581nuj0qwFJDeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyqMYK21Q9XTwvPKp6CwVHQ-lyFKOZnwzBBlr37dqUGLQqPHXoVg5lMSE9QtOBI0iLt44qrEWtnE32exovrjJUGVInCR23YTeaSKTch5NJBsldlcxWxSS4z8Kha0padCiHYAiyyWf4yVHeb69wD4ONe3yrsiWG4iYOEfDp_qd-L-s43WOqfJP8RU38BG756O3J4u2iz3iIi1mfZvUF4kt6aX0tY8sQn1a3GsC1noNDcnSFI27m7uI2uwPDILLwWPUfk3-KRTFdkW07l2qw8V-PwvTi9LJ71B3tZgVQvk-4qDgIiRrRNxH_wQvKrVwpHjNqghlhV-Jld9TKkM9yah-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ho6rMgYt0doxagcxf1bosARiYg_LyugvHdoWG0OD54XbuQOHW2is8dLt9eAFUabPMZTir6tVGNfBDc5cXEHl8OR13-_EAL8zmB5cE7GxnjFMbNna9jRCF9iKO8IHCVXvVssyfR5Tf8dBGNiUmzmQV9mYxKoTLpycQBsTHv-VTg-fUMhYqH_Q7oAdHjtdTYLA1blJauAfT92vd-JlsivQUUZuF7hbuT4gS6WRU5nHpFeheQNVKGpvU5comrMf8xfrRH2QbbjqjeDBCC5iuZ-6-Jp9gejP2YW5CHVhcWR-afEMADVEZoJQoaisgNNEfL9u5xLjpeGfcYzJvcpcLmURqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqxa3P4Sh6xwAXpeOZZUS66ydxxTVGx64n0GmXMKkrnPmdXobXD1UriJmBlgQ4XRf35eG6lzyrd4R6QJhmNLVBvHh_pFXs9g9BlN5sXzRRx2uOAkEocKomLCGMwf2cdsy5Ye_-fak5V17KoEv1h3f6ZC-j5SS3YqeQNOOC6Pb0fmJjkDa3XzgT6qeqLgG6AU-VatNiCoDm5Wamgxa_hBHzhmMbfTZz5SqwHQWundqElJij0rsf9PeZs8qlxjwNDLHFoPtA0NEB-Fuggu37-hU9LEZqeKIeWUyjTt3wU8oLkrjveCtSSUklEU2662MeOEygHOy2fSWSjUBcQ3RTKLKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHjNjCNnBy95HsstAyXad2Q7Plv7VnWGDsroZ4sOF8wxU806FrPA4sisozhkAsAMFA4FEZeNEA3K5UaQBeiQsi6vmc4gVswsS1dAN_k4TBAgO-xgbYSW1m5MUWyvCnO1yABwnJsfPYXoDtJL49F-2JPsHNMiaDHRvROwTfv5g6vnc1MSA6bvF325BJKMo8IWgt2go59hEVQqwwlQ_k0r9NjUYuhUd8E_RnLjxSXG2dyRV3fQfI2QqR8gdQ8impeEe8w_fBbcO2DZxNPygnF0ojEJF3ckBL5db2FkXiBnPIyaUKpCvsAflRYGqAaEPrRWevfbq3erUg5erfYkB-nQ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egsvpvWCQQGFYfPN3p1sg_OzBiJDB20GHTWNqmPOcqc7xDcwDbGUp4NNPKhFO8lg5HupN-dBPi4qfF_QNG8qhgvMldR2CVCR0pmGB6Ndnubi1WpDPnVRb3qANP5LVwcYAtC4gOFRv_5NuzL9OtcZ2TFdz0H0NPHXylV7Ox3c7tL7sZhEOxKnFsBv2tazjvKSkaOCRojKQVBl3P-hf-XvpixCbTbN3p5OMsiGqK3t8564-mq0LqDMQqPeyGxAPJqc5GySyDNT18gnrAgBLT0922CGL6FyzY17NEhOkKfn1w8MJauZbDxsgUDzfslHHhlxSnpHWARHgFkO05Xxz81hPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HVLoiEvWyT91ViYzV-hWgnhzghleBCp2NF5HbTADeJDFQtQn0Kfa2xl5MVBFpIkJDyNjpubIDNKxz6EXTb6tXDN-Ye-odaRY8AnD0XJoTPFuFp9iNLcoE4JA1AZru6iqnR_bLHLCXSfBn2n0DDYjgvg3SnswvgxpNSCpANrLkIUeeMdkW8ALJPJAOnJFiNkDGOgoFNABrlu8-aWOSdPcDhsFm7oBt4XIrSCUL6vbSx2GuTMsqpIfYafLmdGzwTLzZxQv4tmFypIGGOTcq75I1-L62RUWChuWPdxMn6r7XyV8Y7-aV2ztyjEjW_5Zc0GBWD_Ai51KCEc3QScHQrJpDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLevQ_CRfKBJnx6k2DKVkIC8JwjW7i4c_nuXZCmQjbVCsZCB86o1-HP0aER5lrk_lxpMjiKDP-fIq6o_ngkATROQzisknXmTvxCObBKP36XZ8So4eqErMISPXGftz9kAOebxgTd-yVrTp0_Q9zGCPxzA7tVGiAWcalhm2pCy6bYhXsUKRnYCwa3p3LdiJqZTYpbGOKHbSa8Ym_Lx8Tu3_9-x-rEc6G4m1aVYQEOjPK4Fvygsm6mkBFODo6za1hgQCA7gPJ4D5JHJudJMgN8c-1zafxe0PNPNjkghbabbsIzEoPc8O7iyIfM_QD1lhtR-PvDQfwZSTXokVGHdTUtMIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWut5OBr0Xtvxh_WnsYHDPzo6I7DV0E-v0-hsExiceDXI1z8JS1w68QW8jGJy-MygfZC3Wb2UjbehKyVFmRDi_7jXv5i0Z2ewCU7oL2BdE2N32ekLp-1KnbxFTHymRNsqf2pppQ3UX2dQ9JUMZ-5Bn5KprJ9AUUTGcQZ9BVVbj9noxhyJE-fkOEh2wAQgqOg7U3o_fUnDL1dqIHQ7Ar2G30NSSoJ0EJYSRbibLnuvQuvxTnNoZwiJojwIiQV5iaHYunQu_SDyjH2-si6NLImU8H8i6OMrKFer8zJOTBeiSSJJW1kQLuv1CwKPIhbPCxxy0fvpKjYKaq4c5An36ofvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daM02CAcfQmzzCs_chwMB1gorRz2IsH3eH96_AS_w1erlcz3LBl--YtTq6k7cnhAaYap-v6tSCutTYBvLgrEUVhTeWSk7Cbs2k_BIFe319StgPYZQ3i3qSoX0cFQa7cqJ7PigBsNmZv-IFA8FOSAZNGEKeaF8PtUEIZw_2A_IUlswSW6LYxAEyBHBRb5btTF7frJxNPaE7TMoPoTiI45WUM3T2lIW3vJDmmgaxS0g7wga_DxwAIFOsdfg7jiAuqo5ZBV-x7G-wRGh_Xw3bn-b_Iq4P4NFFhY1FcYL4goKDkB0Hp-fY7l6DHT3aqEqz93Dcw4Dh2nSQ3ab9QXTVC7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iX_-09d2CPUKcyOFEtW8zTd-9DVp5QhODf98E6HyCLb1WJDqT5gvyb_hUR2Qt5ONDy1u9voDOJrUmRyha1l3_2LI_v5rXZ_3j9AWxIDLv-12nYXDsukeehsIHm_Sn1gzcl9RulUbin0H9yneb0EFQA4iwpMcZNh8-D3U1gqYkmpuWOwtk7DoKNIp60ziQqcviXdAW7Ll-eyoDKjzDAku5-3uK8tAIS-uiUrHdNAhf0LqQAJnBnejC3luLQJacVux38JCgmjBsmHld1CW4x40XsLNhm01W3IW-GSYAfbJWo0NhZr_YtFIUbsq3bzj8wAf4_WqMEuazwOA16wVGgjYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrAE5IyMLabOL9IBeVsAXBtmOKJGk9E6tToTSFUreVMxowJolz_i9_sG6-_hfcXhuM72k8FtS6sbw9a7mDjdKB4kLk43BIxnpemeQ68o2xrFrhQ_03deUjMKGOl7WUpKFHWaa3irdKc5VgueklRZhCNq47_RQSXIjbih32FC11su3pgEt0guvFWlPq7aMIxk75LW1_eEAxq4wa5pSnsUN3cs4I5ds9fPG5D6x2Va6HdTD4e6u1CDuFp11NmgeqGAVEgRBnBQ419Q4Tk0MCtqcOpWN7qx3Fb-Ol9hfQKYQ5x7sa85656lXK8QQZ6ubQDjMNiL6JiuqOLWaUfi0UKEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mswGJCncd35yJLY5MByOnT7Y1-Z2qCquHKeO5tr2YU7uDIQpxo4WdJLKoBoEhKhLTKQWE_qTY_WnrriYyg0Omdb2PCI2oPpnUc8sFx-ktesXEvjVfe5qw0jl5qje_3ACN8ebgmPYT4UMp8kslYivKKKmkNnLreWcGvUM_dwatffyANHq3lP3R0DkyJEizCAgn9kw4tfzPYarVqsP1JqETaHSoSKYbnLy16pwR3ned32tGtbm5HOMT84SIB2GYsvszmFfx4rmUCSP4pmiur3wflOsbJ3unr83CWstHpieOTLFPfSnFdTAlcMLitGygjBmJjjO_xb0SIQul_7pudietg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKWqyCH1Iw7aFbk0Y-6zV5x_Vx0dlhfc0ER_OR4tPOPaPgQ09qNbYPpSU1P7epLIfAXkzmDZ0gpzudZwtYbqQpRIEEbFMvalC39gzsDt8oUSdt6XO-B5lrLKGIFkrcO4hHFWMG7qZ8euki4N_7dcbWrxe5GKciboubvkvBS7RmDN1CMR8UhhALDBPjXupaRQJoSuPNgPDMoL5v_jPWoskfqIqqr9Wl6c8V4-PL5ic3W4Sr_G7WwJdHhJf3y3TuigV5d1Si4kM3rNoqeS2UDgPCUbuA9pUaZUvfv2fSUIH5UVxuntt4OegBmIXuF2Um6bC4RIaL1pNIP6VYoEDwll5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8BYQkAnN81frP7HnnMvF6d4SzRdLSYKWLw2NrsoM0pZeKvEHUzEI1_hz6qzgAYiyoZM-cc_MWwkKywHuJkZUKAZ29oidUW5SuaCzC_BkD-_WuyFcSV6LS6lzN8vg6g4ejTWcD7ks7sBz2DRxZbZ_96cvMEljnnIBQwgiJN81nyJpcO7fIY1LBd2gpRPA64Z2U7lepHtt87V6vI50n2ImDSRRL5M5L6bBJ_zGPwdSqIP7dy6nv_nvL8tDuqi7QmshDzAxFKTv4QXwa_nb1oulANJblh9Aa1OP5b_B6vsPZf7N2nl5OFMBEU8sbd9bWteuC6NIlEOLkJCo3lwPU5YUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO-x2h2iLdg079kZOSb98lbJq7Wd3IzT-cAObikg9QhojL2-4pXqoCSj8O3a3MeJnYmNUE4OO5mwmMlCac8WB32foeYDjmVLL7G7quFd_vDV3UJtoG77p36bWwU96cHt1W-TVuUDQS_Ylvi7vrajOW3UJvbZD2tZ6bfE2q_nN9gAvKRdXBUl9UkuNVkK1NFCqLHJm8vBKgwerVMel5UBiinDErDA9ZjfNlwNGosMLK4Vinw7G7Yh7Ud2Mw4DJyLHCtqx3Ur-bXRGl8VQZtZR3LVucjuEFxzUiYTiW_GWdAmFgxxGXhVKQ6je_rA6J_4DFw3KBGYGPyb-S63DrD3SkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SotTajZ1adsQcICxcXkbuNRs1MG0iPTQq8KcbofLsluqiuSoIBLS-tt9zSq63JheXO-t9olUN8kVWLrZS_lcHmI0rNhhHNwR7DQ90zVVvFsT8Hn5x3RR8Fghe_2T7jdKazv2PHPmPRUv4iApHQSFNEqFdvGUPhQff96xlH-BSo56sHUX4v38e0-8qffdAZRdKv0HH8x0Yrt2iKhmb_lM6fvGP4jOZneCDnO7E0Lt7DinSi2plpBRlhrSqfAEHPwDMkdTAn64dkKzC-h9uKizKCF-tcX1i3_OPTsPZwsyo-7KEeXUbCewD1qcNWut0Tc128l8hv505VdZ-NP6MIE-_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKVZ7VlpkMP-UaYlP07aX1GWc_pJwLMdtTF6TwVG90TQG8d_kZZKJJp3HqTV1CgPgxethDRMcNk1jTrPsxj-rEduP4TfKiTrF2Ft_oDwulH87TVrINpD3KoWmHSyGljb7ALSa7tqVQgtQi6EhbrkRqp0vhrRpSqnLyn_l3QvYFiZlXxv3Ue7Dv2VlfDRGlX5C0EAYDXf79Sgxi5yJbnX2FM9bTbwHDZaxBxPPwwHQ0ZphFRo9UaYviQJAuqpoVyaP3XtGT658qI-OrtQeeDZinaUlbpspf_8ZJ8d604jwBQypxFyxhlmKT6JiUZtwmCFEn9kEHNaJf3UjDnPi98WZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YpLa8VPA4WJTa2-Y7e5sGpJSiVz8YaugsUow2nqGRm1b9KSSqendyH0ZuYAdC-_Do5dgWO0QTJRoIFMmHxIR6FbCxdTH1S8HCpa3ozOHVDWsqRMq4-Sjux__B0olfwexxb_43oajD7FukRlYCLaNcs-Y2DtksG8Xag4lqrjgVX0xfr9HeSDLLkGCpW_PsAoj7ywxHBzV-P22szL98dM27nWwKOLBehNQ4FBT-bg1w4CdxukppHd5ZaDaZMGCoYcFU7M_QBXz9TK_HMURk5LfznreqSAKbLMnCEZDLrcrmDeO-NbFDKD1xy4kwO-sT5X_SozQe2Xj3C4kvCyn1mqoQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0ww8Kuvtf94sDIs31RKpPDRfX1y3e6KpVcdCWgBaKOgXt4SF1yr_s3csytaEOIFUl-WqJ-NOqpcSyA0HwVX9MhcGqGLlxdMGiJTF5_VDzHbfEXm8a2vWrlph0FOaSmXOg4eihwCL-looA4ZkOMwnqp4Dlr8r44lSRNeUW8gPfxI4NwpGXypMUKOHsCSsPbPLYMDpOClzMtb1X6frdzPdW5UYg9Xhs7JAbfcQ3GuHEa9AzfDt-9SwYGN-Bd1n4CA_MI3EPP_yQZIR7zwSaMR5dVYU6QMGLj3mtPmlm5hFx2pTjRW3oQfedUelnOC4DCS6unTiLOeAL5YldcDOagkLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYJ87Et6X3jzrPSLBXXgLugCLmu7b2rqjm0b155AgmVuknDP9tLy8WSgueFyAk_WgXrkQGq63BE_Bric_IgFBapnM6FtmGKM96QPnYpwM88qHL6zkNBzZ7wwKn08bwLU1OZdZ55O1-6NpnEiLEA24UQQuLuKGeXpXztVjriqbsfJBYgbZC1QjleNfuu0tb-WxfSTqjRZk9buw_Zw_htyNep4mNvnIRsPNDawaIM6cGxZit8Z3skeBSWglPjcCxI4dp0mAhopMKVF66Xbpw9L4BJWAbO111UApuW6B0X34iRqko0CJh0SmpfZX6jipIDgcZldC-39n4z1t7amtpBIhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5kr7dn_NCLATWDLyW3CYz1sYkancs9n1rYxYEIUNdkI-2YFEHfvKdGERZVv0xolKXqEYWUitvpe0EPeBftfHnqw5lh9Xmo7B0qT4ataAKAG_9vSuZ6YqgzKNyescHLF30hqtml8hx87x2WdbMZI-3Fs95NK4z2Nn7WSbTmLGGcQsjLqPMSL-O6unXtX4HOy4qX8J2_DjE1SDU2UvS_WNKMkA4pdB2Ml5QnM5rVVcM9oeGtxb9coVfudRfHYp40oXCdevk4qC2Gnai8jFRGwGy0ew26RZHnGHAclB358YAdyrLGVwECZEQ6hzpnDiNWpNYCvoTy_rAfSDwXpRxFlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qo2BhQFDMppHRfoqa_2VpCCeoBENxtSPzNTvQ5NkgUEVkmElinmDoLWLW_C_lLIsp7N6O58Qs8ZiXJME4b-wOxE1chAjZejfkjbnm75H-7GjpCdmasp42txBfB2bo8j7R9i4TxbClDk1jDsEPut1PiHG8JMWCVjpBdvClxVECOdoSWNNcZINgwQaEeNJ81LuJDd7jrwUmNrSbU5Y14rq3_RLERpsQAefXwbMfqDW5Rjbf2P8uKZn3Idy4I7AwZnbBMrdaKAfvoz9nCSe2Hud491l7n7z26IPUsY3TNAv8TU8CCTIkm38k5aGmORY6Ld49qd1O14EiSjgUsJdCxi_Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHvHsotxEsviN6oBTv8b8vHIq6DXzmCrxkrMcejeYaSqTzblarkJxchFJqlOMPJJ3LX0_4HuwFwcAKcL3VUuH4MaVc-0dUGjHmbV1ScABlXJSfmqga27MoGkVcq0BzuihyD6TCk7ngLZKnOExXciO0QXlCOHHFDwdKRrMFMXdz-qNqmEuyJ9ZpQSxOvBzihD__QwyH2jofwyR_s5TMXT7lgSKN_awpO2EI7WaWPDOo_7ESoGO9YgaPsOa-wR5_e9Or-kD5KDzaKgafwb8LpGpD5iMFLEW60h10sJ6BRvwAKWuUtjMGI7qI3azFO9FaIAi8BnKYvYXeeETFNk_3TdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjDdG1RivQ7GMV2hbKh5vxcTJS4_6ca_BHSLu_1E2-lSR-6EAslX0L8uPuSTomNVwaCrwoSNQwWCsBK9m4mQyVBlHAa9sxx04MgthOjBCWlo85qETBs2zm3fJCfBDX5AP9JjigsiI9lcSlCZLILQLss7PS9b2V8UcHgboMD-FZOtk2bzTG9J1PIXv-CuYscwr-UKrdvJ7PgrZrB6yTjF-255laXEsKNLg1RQtWbF2w1SUXKULbDFTlVnvvYE7AEe7yWuJaWFctFL9DkuqGXYJzcsvhGMx4sg7whk0lZBBZp5GOmA1KyJLDQaForgoIaDBpREJSZQsZyaxjLvk206-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndtkqXsoottMa8TzpHPekTHOO7Bn_hQvp8pI1DcLp2EzFPnTiwSKwHS8ZkxASb9X5aBw4oUpK-nObC_k1NeELdS_Q3FwdRiaaAfsb7D_9je8CuOaOhVr0BXrJKyyuJgVBseSAmKf6N48gqO94N3GnJd34CmrG-KNkgzmavHyeDwgKMG2aizT7bInIRBqv6h6YlIAHKzOaVZBFf8eLR9q2mBpOG5cKv3jCSZyQxp11_9wHVn6ioefeTGaLl5M9iyH5vMakKy6pbmjqMf_17UCmJ8IheowKvAf1Iefe7QAO3VIQLoogM1vGBAk1u1cZgr6NHXZVi8dFoCgsFTjWpCpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vty93607gztzhSgBqo0yb03VSdX1oS7tJQi6mEQ3WWY9IaadTp-QDmuW2c9ILOdK0NmTzGUrYi2D5pKICOShGwEXS2sETmBlWRAxXH3Ea-utBQG6yL3q3KtvACJYcpTuFEV5wS1l-r9sZsKbXzqsnoRp_CMVxR4mM5EAyg1qN8CbQzQf6Wp0up8rjt5SQR_z6wUi0VCjdRbpl3I-Z9QBJ_vCjmQ5Iy14XIhDcVl5hopq0I03C-GVFFIebjgOd6SXhMCzbGBDhv62FmtWC-GI47Fi-4KjA__i4yt06ldUOqnKZGxg7AaGOLBUQGEBUySLzft8zRvAwsi2FedgCEk6Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWDjxY_HKm72jhjWo-t3e4-4G51GyI36cndOhGi9DzZ7Z_IuevcO4lAg9MaJnTvp4hpbBahAbnZ-TaXcnHrEGH-u02Wb2JBX-9xxzPvk8jRpCYRZ-6JPVv2WQ73bhGmK-Z-GzlbGWXWiwxZMtCIs2JKRyuhzDyP_kGp1f9DT7tmkZmL9LoWG0UC3w7e0uCOmV-NvIGjipn-v0S-BjlEflSRHiZHh1Y9ze2OMNqMkRHN8cgRJFmqmT3km7R2moMtaBqUR6Habnzbks24IXgaIkez4MRF5mWt1IQY0M3mgEEDOUJqOa-ydV6MuKe0nwK7F1IBqVv9r2d3nkiIBDNQoDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlbtfpCYEjl3wAv0MUGW7TEZqFaF3FTXYcmc3hP3VgFL6z6a5YipwlvInWBks6Rs3z3gDiD8b242L6exHizvMhp7txZjJpeLRDgTXvKFOcZLdSGN7-kP6kR2CeDDImtK9vlM5HwXfVlcMCt-aPTVOB-Kp1KmSKBcdHqJdAByBCmVnerRmU0CCkIxArBIIOOB-ilS9YdK9cnIAftuVg93kjXkTGomG95vKRPgjsqXBLR5FFPb6KRDSTpWfyDvJbPy-fLHb4yL8bpYyN3XddQVXxx39HowQGD2iqrxBfhpsHWpYSvmjP3ms-_I5lMbTcaRepDPyN0Ivjfw1O8N14nT8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=UVbHSODZ32pjBW3DLLV0Bke1FC16zuWnfaSrbUdPYh_roGVcbnKbCH4kqYwuexQEFmJ0wyUtR-zaJ16G5tqOm1hgvCTFwtVqzUZyuV5ketzxEZN9A8S9tFiWIEYTEy3aPt4HERpn14R4ADY0RwwQQixTIgNvPE677gV6GHqLQ3SvC0UhaqatwcWpkmk-4IwWDpSAuVDa5DRvpR8z_Zj1_AGJh4UwLDxF6d2FBTHZjNJu-Pmu8j0A80uJILymSuZg59aZHoOq-LCMc6YcDIUGn0qR7NLDmLyIpoWEmPuoNq7nL-NMI6U3en9Vw5DHiUhZFRp367woMayvU_8cYAuKJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=UVbHSODZ32pjBW3DLLV0Bke1FC16zuWnfaSrbUdPYh_roGVcbnKbCH4kqYwuexQEFmJ0wyUtR-zaJ16G5tqOm1hgvCTFwtVqzUZyuV5ketzxEZN9A8S9tFiWIEYTEy3aPt4HERpn14R4ADY0RwwQQixTIgNvPE677gV6GHqLQ3SvC0UhaqatwcWpkmk-4IwWDpSAuVDa5DRvpR8z_Zj1_AGJh4UwLDxF6d2FBTHZjNJu-Pmu8j0A80uJILymSuZg59aZHoOq-LCMc6YcDIUGn0qR7NLDmLyIpoWEmPuoNq7nL-NMI6U3en9Vw5DHiUhZFRp367woMayvU_8cYAuKJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBDckYT6uV7MkaY0ePJKMk7c__WQM5HjsmGBLSPmt5hxoC4gucmmq51M3oHTA-U49dOEb_vRIEZDNJEQ5LBFJv7OsDBk9xp-uAyv7KslXkQtA5YzyOuLnobzPNLxI3-JyVSP95_i6a562h7JujN0SOs9lt-fqr4dGyOwd60bt1lCGU-pJYB8t0XF4Vyxjkbg6fyHeXE1nEWwj3GX81IvVltgfaBjjADTiTv7zaIqH6CjMdv5yv6AguKfR8U3Q49qrNpyw9yjjM8It08zacVHwbb2TunYP6ZgOvF3KBmCJiuhslduxtsydA1n3tzI1SP6sleiISg9v4WccUHwbYK82g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFGEmQTEwlI-kRfysfnST7Ld0dDTCF6SvfBQ8k02AdTLLQXd4fEcViaIwP3yBtytnV-lG_Y-V-0ZKxCbuuZmiaheWMZQI0OAG4RvnwNgvI8hbT7103dJoh-1L0IrPyQuF67BaJoDnfw8LpCT9V8_CCO4dl7X8Ibx6ur0yQVXoqhZ8dcE7x-JILtY0oia0hpaq6R-C8gthAft-a-pWPf1LtNq3g7VT2z7fua4O_nWbOwywXt38RcDqDYt-OPiJ6UAf2MGrSbam12KT28tDQCEEZzS6UBzwJ9slHpbXLRKE6Xh7gPTxM4Kckl_PTtuFcgPueGYBieO4ufeS3fZF6QxWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6hXyDQ1An2Gr7P58CmNt78IzLGr6kewxJrnd-1LNHGducMYS6-vlohQg_J-Cz_6Pk8NXfXyEA9vHGJZnyJJzhEqLpslBQsjVFeZKxv77vxRNDNqriiqU-z6HP7_PMe5RvdSqGYoFaLN805EfqL5cKcdfWmkhI_ECnjaqli0ao28tUYqB3WUAmmMJ7DBWk97LQ1FTf2elpPIF1IkBZ1dGCF_LxIK67hXe8g-iNSoPChHoHhV9WMV5g6xBVx7JgmCazFLuFHSg1Z1Xko2Qjkyh8Gnbz5mMaJQ5qs3qfR6cammlsXirVE3hK1C4Iqf-IsO_gZMd0Pw4BrAJyN3L0zxLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbTxF1kcENEqIz6qKDBehqpw9XEggHvpKiUTqV7GR9Ab6B1omio6IxJTJbV2dnrbUV4YgEOfIsFQHmuLiJUAIdznxIXUEG_w32sWmbIjy6xkm5OqJTQDqR___Bot7RcUOcljFr-0-e-x2Zp7g8FN9IqdIUekqqWctv-ERtcJp1G8hUiAq6i2Smw_FYDwjHYwxVLg0pDXueH34xFwjQTC2lWLdplCTrEu-18nkw8xk15bNhDQ29RNzW6ygkSIfxB0bb-EiNxHAoDASxj1u6SjrVxJMQCVo1bIU7wIhDk51KwRwvjZr_P2Rwb_8V_fqBg2BPtLr8Rgs83C41wkiDLv6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro7A55w6nKK5up97EBZqQGmROJ_p7pVwB12VNXFQRFHoH50CBDfPj3uyM7-qKyauwRJX46iX21QrhyMk5JG3hKoO35eIeB4Oaf3CVi-kOxhq25x1fgWxz4hiIHcyoGa3BFt3kv9dRfOgsIkmT-16fJ9AVyo9MaaJzCxMZCAB3fK0zOPtYIC59IwZOEH_Uk1EaoTrcVVawC_r2BQBy8GA-S3R1eXv2Z8u6Yn-6ElZt3lSzGpLXjPhHYYiHjz5bu0D3gGr6mMQo_5reyjya-iPmjxLslfhFIxitwf2azecMLdzSrbTeozCtytO13oEzjiJUhYBMkCRc6jqi9FLLUyBiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-Lhx6Fpc1-Slz6lwS3UR-vv_waShrb3C-yW-QUnj_jjKT4TwvllL7QC0B0QhFctmlyBQCJGCWO2PjBAKWiqric0WGsQR8gjd2FhsEyzhpIW56fXUBPgLY6mmu5DBL2_c3YX0UiB6OZJR5Wu-X1rcg1TIag89306TWeZfHLcpQq7zXMSC6Vt46pAxC3jsCWteyn0LRQh0XPuAPAsYSnOW4OKQHojWcOihb0aL1TlRfdKPay9rRXFPZRAhdb52s1UcbYe3auHcDEaOUZnP7sXBBqZ77o3aI1LHe-5Z6-CzliGG_Z54Moz5axeYtXXhWC0OZfH8i1QIjC3HLh2om6QLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsqqBh7aLo-HPvw62KaAkpRFaTH244MW5RGNaNV6pFFvXZinFwmuzo4i-0KCdT37P-D4DsXIVstqvKKok0h6zjCEVNb8pe9iOLvXC8l6mvTRb8rycCtptCq5eCHXyji0TZCkEqkNvwQrXZCli0R0_-ocvbTS2OLhWJ86rpmDw34ie7w_zGV8SxWDXgqHKjdc1Jg9TXDt57gDcBiiRlohpClNSnfVsJ2oV3Lxoizq8q5G_B4fQmoaxdiqZvj8P-aGkCkqPG3UIwmBcjQOUe22V1RMaJ8f_p2jzjgaSgAYNuupz5gKn0ljksthKb6AYoaEuBqL8k8AgxNh1PH8zh5qUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9xBXGcMJYGBtciwfeXfnvV0B4hOwRun7kSk-zqkF-O34jXZiSRpSKYiJID5lX6zERXnQeXuE4huhbKE9OAI1yFkVXCEm6ey3AfwhxkaTTpppCuFab8ON6mL6E_uQPeH-lDzUetF639cjGUc_DZXXvnJadkWmVfq25R6zxCCcwWlZslzO2VTS73C1Br_ViVzGh79VoqIKbr8MQp22YOBHD-THaEd0SMqn8M_Y7ZCLbxnHsegXQ-kFX9uKB-P9b041g7GOXj8WiYJMW0qTGBgEGWw8Iarlf9O2N27i2EGgzphLQemh5uua-km-fYUfVHSsexZTS8rRX_FvBN079tfQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlyu1gYigvBptpIcWcRcCWa2p_2zIJ0IgHuwfa97Ofnh-m-NZLSfjCotPmP3bi-XpRf-RsjTnlKGXhNXEBhqCEeglniGG-QnWyi8PzjoUlYmslovgcErqabiQBK_qoM3ehKPdIZ4w2jscukcEAXo37iFEILfl-8Aqc4YB6xNIf5qkM3VdqLbTUy8k0-K23YL4pFsPqJoCFfP1JbIVuVn5Xu1YaoqOjgs_4gLLxD4jYPTaximDlvdPz2MtLLUdL8C4mQixzOGyfOy0LEJ_jptw249-eKR6P8YvHPGY9K2DXQNAyfFxliQnfaolcNl8l1yNNuqj7cfZAl2bvHZt-R7aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKT-BojDE3mOLj0bNpbOWciaA6d_Euj07fC0k6S8cTJHYucBQt1x9sf5hG9jUBBZebN-qmQY3OCIiUyr9KbYimOS4LkqXKqs4qDonnoJCus9XnTGShAfs5A_tkST3y-w1Rl7O8RnVfcwJYt6BZ-mMR4FZxTGaF44VmzR1Flp7TcEc_C-MSFjH-K9XYTqiThY7EaItEwM6YFgyAfCsPL25oTl6CGlIX5Hd56yj4PxqvPfmdBGoD5zYQm_dvkh7teigOsBgc12X5pwDgwqfa_rqTdr44ccs_v_kLKOjImKTsrLA1keIjZShW0dFk6HMFO-BcLrbUyrM3h2GjXCvoOIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diHXjgdjjK5-Q4Bv9uiKHHlPLE0vM-pK2bx6N9_qITAYM5CZ6YA6UcFUFKuzzLFSli3KwEqHFF_KEre-L55xSyGQK2aqzsFfjPn6hnAv3mrH723x8l9zZkge45qyLAnf3G0MoQ9vh_gELx-JakA8kjaBbHWDDiWQjVY4iHxa9wJtYEye2A_BKiJvUx7j-y5633x6I_hSfbE5X-q-j07rRKvz3FQEf_tyTCgvBASlRNeuj5eWDzwG9E3ACk5tOx-TvkRAm-LuNE_i8yGt6gewIpQtC99IJ97R0CBUy7pF8mZITxR8fiMi4IBorgesPaN8DsvDCBLTsV48aNIViwnE0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITxZ0lSOqMHsxy9wLizPJDnVJXzOzzJyEr7-zS_X3AcTYiCtSXngnUIUVZ4PtDtVqST3HfGnbSJJFsSZPxxXF87n1P004tSswVe90eC8ZgL9CWyIrd4LzTpSQ4Jr5_Buo-rvNSqI40Vp_lWqoZRwbAGsSXiBAlf1CRWhP4CbwCDBZfY5SJCPNfE7AxQ-3TP1g2XAvNbOGg7ZiKK7Qi8SrK93yuNHj4htdPJ5vPpeyY0_OZ9d-DtWzld8iREJeMsP5MUgNikxPOUWa9yoy6KBU1ZDj9zre4G2MHHeOhxFP5kwR64o96KgYqFunGph3Epgv5nSyu6jQ0SW9KVEGjS2QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXXu6QoajVC3e1aicG9MRiE6Aqr2QfVsLTEMz0gcXNiUXqNeb5v-SeDDGTjzkwx9eH2LEIjZsnVeXpEDVBHvpz90DXSbsH_wq1ieDAFmjvpeAPNw7HMFAZdgzJTm5s__2qVQIYmpzTnZ_5tRcq27JR8WfJ8lyQEi0wrmDZnDnz2HgbR_jSEHnUKPsFQRA7zkoPxgyZFUl4-MqZ0drkb8rW1HEnCwxjdo9tusHP2yx2t5jxoPzNbqGzMBXrLz2m4U2-uqPeO1ay6JuSdrjdvv64iFj8R1A5EY5bRmyiIEFarFUE9873Xgy5SdwceKnEmBAGhc5YN7oXmlFXKTZB2rnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkQ2wDoafB4sBEcFjqGOMtf0NmsFnjFG9TQ7VOxbyr1UXFQHM1x6RQoA71UObfG4s0GE-fThuYwFnaJKM2HsyIuO-emE4-hWxN6aSMMkjqPMazg4-ZTZt0zx3mg4YOufAuRQ--5FQTcn6-Yutbt-DjSy1P-pmRTMMPX_ccvussPwfeYmT1ibQYqHGIyc9JmZFdqKJLXyH7WbJg7UuNIeBH-5y3eGHZmsw0v8-5yAaNdcpZkRbRihFYgpPoIm3Hp7WmmYSpJegxkEIDPXxckYv6z2VmP2To9gRDN75MTUcACJ9NxtSV4my5R2eFwal5cz0PZy0suqAxoILu5KKtwdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
