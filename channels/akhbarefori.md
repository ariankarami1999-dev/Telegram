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
<img src="https://cdn4.telesco.pe/file/a2l-I55Ldkag-wHHYKEQHBH0oWbmialpkOhQxDpMyvgobnGOQihjm7ziFRgChQWESm6OCrvljtDrzTgtnWWWsrj4NG54Dz4Jkcc64JIUpAyhuqxo3_Uem_qfgjzlb6_zRHC4L4EqaHq7xLa8lMjBKHA07RtJYYa5hARBpv475b9nNXqF7kJfCUi5-Vcl7HD92saZIAZUtXZ1zhkg-_xShS1UwKarI-iGAjuhOmTAoimML2FAYLaMtbZnMJ1CldfIQsC_8CXypo3PrA8RAFTsaz2_DJEOBX77-xg7Yw1Vr9JUOxsWP7odACHJzRn4yyfDll9nIA_Te85u_bJGNnB3AQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.22M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 17:50:05</div>
<hr>

<div class="tg-post" id="msg-664317">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de251a27f9.mp4?token=rc9Qf8R15y10LQqEYpFRl9Dgqm_h418Kz1o-kttSgpRQIDG4BUSDu498cWAtIipt8_JneYbP6sS5Xw3WtpGE0mEqetTTWdcnJpPSSgR5Q8WN2TA2IvNtjJi9X4bPvnHNQ1JSsOeKdP8ttEielQfLyp6chtXz5gMUUEyP6RYK73GBlXUF35lAyGh2EZYtEa9FtDq0Xyvx_-qTDvnFSvCCjNTDmyyy51QwH1Hv31NkS1UtQvwv2OsTkN9s3_wgCoCv2jBZCO5bwx6tNL77i0_fH2LfGcTQwweqrWtTGtXpapjNkyPTJfASwJ5EjLoj0hLQ_4Ipk4iGLfMroI9xXybpe41wWrhG_95cqg4t-FiHb2HNVxIe5SBTPonzz_ZOhh4ixqmyyi1B_T6NGd6IfFApKYN9_1m_5s5jd9BY3cBsjysedEhFq8SI1SJ7DqlHjYH6S9Rv9qqD9NoJhFh9SwOHxRdBwp4ZG6OeH2ueraWNytcrmD5NDLfhBpw8ScIdWJGWHPrw6E03ppqJxFqMbIzGe2iGwM_aTUFRi3vmDMbPyGs8-Jw6iiGkdB7OD_NrdJSJcRfVubLDnC8Xmm5g4q56seRj04VmTPqZKnU687AmV_LoINvKEuyDyt9NUAjkjhD4yEdj3wfZXd3jvWUbMUBHSGySPLhZUFhAv-xkRnDNtso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de251a27f9.mp4?token=rc9Qf8R15y10LQqEYpFRl9Dgqm_h418Kz1o-kttSgpRQIDG4BUSDu498cWAtIipt8_JneYbP6sS5Xw3WtpGE0mEqetTTWdcnJpPSSgR5Q8WN2TA2IvNtjJi9X4bPvnHNQ1JSsOeKdP8ttEielQfLyp6chtXz5gMUUEyP6RYK73GBlXUF35lAyGh2EZYtEa9FtDq0Xyvx_-qTDvnFSvCCjNTDmyyy51QwH1Hv31NkS1UtQvwv2OsTkN9s3_wgCoCv2jBZCO5bwx6tNL77i0_fH2LfGcTQwweqrWtTGtXpapjNkyPTJfASwJ5EjLoj0hLQ_4Ipk4iGLfMroI9xXybpe41wWrhG_95cqg4t-FiHb2HNVxIe5SBTPonzz_ZOhh4ixqmyyi1B_T6NGd6IfFApKYN9_1m_5s5jd9BY3cBsjysedEhFq8SI1SJ7DqlHjYH6S9Rv9qqD9NoJhFh9SwOHxRdBwp4ZG6OeH2ueraWNytcrmD5NDLfhBpw8ScIdWJGWHPrw6E03ppqJxFqMbIzGe2iGwM_aTUFRi3vmDMbPyGs8-Jw6iiGkdB7OD_NrdJSJcRfVubLDnC8Xmm5g4q56seRj04VmTPqZKnU687AmV_LoINvKEuyDyt9NUAjkjhD4yEdj3wfZXd3jvWUbMUBHSGySPLhZUFhAv-xkRnDNtso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سانحه برخورد قطار با خودرو در جنوب عراق
🔹
در پی توقف یک خودرو روی ریل، قطاری در یکی از خطوط ریلی جنوب عراق با آن برخورد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/664317" target="_blank">📅 17:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664316">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
بیانیه جمعی از اعضای مجلس خبرگان رهبری پیرو پیام راهگشای رهبر انقلاب   بسم الله الرحمن الرحیم مردم بصیر و انقلابی ایران اسلامی با عرض تسلیت ایام عزای سالار شهیدان و اصحاب باوفای آن حضرت و آرزوی سلامت و طول عمر با عزت رهبر معظم انقلاب اسلامی(مدظله‌العالی)…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/664316" target="_blank">📅 17:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664315">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
گرما در فرانسه نزدیک به یک سوم جنگ ایران و آمریکا کشته گرفت
🔹
مقامات بهداشتی فرانسه اعلام کردند که حدود ۱۰۰۰ نفر در پی گرما در هفته گذشته جان خود را از دست داده‌اند. این درحالی است که بیشینه دما در فرانسه هنوز به دمای خوزستان و سیستان و بلوچستان نرسیده است!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/664315" target="_blank">📅 17:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664313">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2EGZqYSchc7sSGPXjS27Xu7IYVWmheHx_X4BEzW5x3nXNGApP4ZEegMt660AvBh-P9lTZwXpEZ8ALIUMcjtU3f1wGC3FI92iqQSmN-iqK9vkHKaBU1ddW1iv4b27zZizsLWEWAKZuk69Vj0x355UARzjiBJaxl9VWXCq8C5uUJzqQAwhFdjcWQQBi0nZhWPTlicRIgAOFVI3oSYeoACdYEJrBx2I_8oHkOaANx_11P6P-zpSuZ3JjDRAPXMXLPW6IfbRW1XGdDQm-515U5mIgoRek3aiVsBmmD4wckvmhSDUeO6woNcVKFx1P2W6L79ygh4VSeltPlNDOmgOk_s-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uac6isuWphyOWlqc89FMnksSTCx2PRyqyPNftkWjLmalNEHXmojvgwx9s1MMEMipbbl7SauU_mFdtaiaWRpsr69R0l4VIlN4Y_QTPhe63qz658w-O0XPHcYY4dRRvz8nekSBtOG9HwUJLn51BcwrADahUTAgtmNtxiI7qfr6Sqsz-kVXF3XD9q_tL5meXo-Y_vTD1op2zDyr34z6UUYLd9VDFCj8YSJkOBKDTcqq3LDcJIOKRilCXhf2ZhTw5TD0QeqbHqJM7wpcpQ6ADhdzUhO-Qcdn5x9l5o3zhMqK8okI7GDJ4M7mDi_ZMOP6unRv8SjsYV5o6V52zaBtEOHzdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قایم‌باشک زیر شقایق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/664313" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664312">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iooNyZVB-3YV3SGFI_EH1cGurDVxioVj07j1IOOc8uzDbo4KBgbYK4Nv3Dq9ruMqvwwViyA4XgYNClsLTsz_NyLCTCOFgo7ZKhHouQKs-hte1VdlT-a5rXwMW75e5NJR6b_DGCbEfDExYVaCVaVe9nhXLkfuGMDPkmy2avzbXcOPNmghwWRv8L7lYAuyw2NaOJwvgEyz66n5DQIAhCniIKkg7yw0Ha_t-8bSjBLLNpHND0wDcNzHkS2Drdwgtql_3ukup8S7ECT-tVVsPfFneMDBkI7rv9ewWqp67n2Qgy93fw3_OlNyOZ1sTwkkPZysv_tScp0D7OGmwowOBBx7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفاوت بالکن، ایوان و تراس در آپارتمان
در یک نگاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/664312" target="_blank">📅 17:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664311">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال/ پایان ست سوم
🔹
ایران ۲ - ۱ کوبا
🇮🇷
۲۵ | ۲۵ | ۲۰
🇨🇺
۲۲ | ۲۱ | ۲۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/664311" target="_blank">📅 17:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664310">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce8a9944a.mp4?token=RKrtuVNWNM0VQXkBgYDL5ImW4XtcO4Axwzqga5KN9OOyS88ESPidlzUfXIZg7_HvWYqDc6aSK94RLfKo-QvzMSQHkMIOFQ4Yv44osYdsjd8fZ5Kc9-9WByoNFD2_ecyYFw3wtF1gZ4aw2ng6WVC3EgckPeZk50TA11PXzuhickz_m-jXYcYJJw5U6Eut3I8oa4BGeLBlg05CGBpD6QxIV0ltL41aBDFM6N2IzTqyhXHJmggqg77AIteza9Wah1hD2TW38COFXk_ImWa5gcHvK332-J2V98lQyA9Tv9Z6AVxWOn0S8-NGZ8J9tiMG7hflx9riAvNUmNE1wQudNlg7Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce8a9944a.mp4?token=RKrtuVNWNM0VQXkBgYDL5ImW4XtcO4Axwzqga5KN9OOyS88ESPidlzUfXIZg7_HvWYqDc6aSK94RLfKo-QvzMSQHkMIOFQ4Yv44osYdsjd8fZ5Kc9-9WByoNFD2_ecyYFw3wtF1gZ4aw2ng6WVC3EgckPeZk50TA11PXzuhickz_m-jXYcYJJw5U6Eut3I8oa4BGeLBlg05CGBpD6QxIV0ltL41aBDFM6N2IzTqyhXHJmggqg77AIteza9Wah1hD2TW38COFXk_ImWa5gcHvK332-J2V98lQyA9Tv9Z6AVxWOn0S8-NGZ8J9tiMG7hflx9riAvNUmNE1wQudNlg7Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب اجسام مشکوک از هواگرد اسرائیلی در جنوب لبنان
🔹
منابع محلی در جنوب لبنان از فعالیت یک هواگرد اسرائیلی و پرتاب اجسام مشکوک در آسمان منطقه خبر دادند. جزئیات بیشتری درباره ماهیت این اجسام یا پیامدهای احتمالی آن منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/664310" target="_blank">📅 17:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664309">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
تکنیک جدید وزارت نیرو برای کاهش اعتراض‌ها به قطعی برق؟
🔹
گزارش‌های متعددی از قطعی پراکنده و بدون اطلاع قبلی برق در شهرهای مختلف منتشر شده است.
🔹
بسیاری از مغازه‌داران می‌گویند این خاموشی‌های ناگهانی باعث از کار افتادن یخچال‌ها و اختلال در زنجیره سرد فروشگاه‌ها شده و خسارت‌هایی به کسب‌وکارشان وارد کرده است.
🔹
پیش‌تر معاون وزیر نیرو گفته بود که نگرانی جدی درباره خاموشی‌های گسترده وجود ندارد
#برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/664309" target="_blank">📅 17:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
قالیباف: با جدیت پیگیر خاتمۀ جنگ در لبنان هستیم
رئیس‌مجلس در تماس تلفنی با همتای لبنانی:
🔹
در گفت‌وگوهای هفتۀ گذشته در سوئیس یکی از مهم‌ترین موضوعات بحث پایان جنگ در لبنان و حاکمیت و تمامیت ارضی این کشور بود.  هدف ما خاتمۀ جنگ در لبنان، بازگشت آوارگان به خانه و کاشانۀ خود و رفع اشغالگری و خروج رژیم صهیونیستی از سرزمین لبنان است و با جدیت پیگیر این موضوع هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/664308" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664307">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تردد خودروهای پلاک مناطق آزاد کیش و قشم در هرمزگان به‌ صورت رسمی آغاز شد
🔹
ثبت ۳۷۶ زمین‌لرزه در کشور طی خردادماه؛ سهم استان تهران ۹ مورد بود
🔹
روزنامه آبزرور از تلاش نخست‌وزیر مستعفی انگلیس، برای تصدی پست دبیرکلی ناتو در سال ۲۰۲۸ خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/664307" target="_blank">📅 17:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e2f8e78d.mp4?token=UMkO7USLefmrET5teKQUWb9D4udVTwZo7F2VOvwmD05jNLnwcvDeozJrottn9jmbB8jQOFfFuVQSvps68isss9bk5s7j78_0MFItP1D5c6lwYKlZXfSElWr7XiFdZKOCYufMqlO00tjU4mMKyObT9_EKqzq6PWi3D-Hq8u9n6tuqoiuSInviSMosTyjG_EUzhy5pLQ9ch3gJLGjOBDZtF2Lvp6h0Eax3aH5UDOBJen0Glw1Xpuq0uSUC9lu1CEXMX0m-mGfvGnCruFJsjFdl44UPjnPxjRgwlJUItJG4u8bn6SqI0RuujYq5OYXhiVDSHgKfzBo9_0bZCKhJwRYmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e2f8e78d.mp4?token=UMkO7USLefmrET5teKQUWb9D4udVTwZo7F2VOvwmD05jNLnwcvDeozJrottn9jmbB8jQOFfFuVQSvps68isss9bk5s7j78_0MFItP1D5c6lwYKlZXfSElWr7XiFdZKOCYufMqlO00tjU4mMKyObT9_EKqzq6PWi3D-Hq8u9n6tuqoiuSInviSMosTyjG_EUzhy5pLQ9ch3gJLGjOBDZtF2Lvp6h0Eax3aH5UDOBJen0Glw1Xpuq0uSUC9lu1CEXMX0m-mGfvGnCruFJsjFdl44UPjnPxjRgwlJUItJG4u8bn6SqI0RuujYq5OYXhiVDSHgKfzBo9_0bZCKhJwRYmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعتِ صفر؛ تقاصی که گریزی از آن نیست
🔹
ما نه فراموش می‌کنیم و نه می‌بخشیم؛ تنها منتظر لحظه‌ای هستیم که عدالت حکم کند. هر ثانیه‌ای که می‌گذرد، یک قدم به حساب نهایی نزدیک‌تر می‌شویم.  #WillPayThePrice  #تقاص_خواهید_داد #خونخواهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/664306" target="_blank">📅 17:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7Lf6wYF3hWWRaowJpyhnofAHkjombsUmpdXLtl6r0ZvhLMovc-k3DnKtQLv1xP7b-RKo9cnIuc8W47vqHXVwd51eAhzwjwQR1jsX__kC9rODcfYGn5UUHWDVok6HeJi9OGi3qBZfg0eNFmKaqpI0inxil_nunBLxo5nhvSiKSBqRw7urRfmzGrPDVfhHUNMLjTU9goN9G9tlinJJ4Ugz7hOQYGrB2cjzBfjZHhJkEqOl19Mlu1-kvwPQs9_v5W6_wcKXRGIsmd6aLREuHPToU3uAteUUQHS3KAq_lwmJ-8pTund-qU41tMszHJh-Eq6lKY8LPNZaTpnSUnR9wbnVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکاوی مبانی فقهی، قرآنی و کلامی
#خون‌خواهی
در اسلام
با ارائه؛
▫️
آیت‌الله محمدباقر تحریری
▫️
آیت‌الله علی‌اکبر رشاد
▫️
حجت‌الاسلام والمسلمین دکتر عبدالحسین‌خسروپناه
دوشنبه ٨ تیرماه ١۴۰۵
ساعت ٨:٣٠ الی ١٢:٣٠
تهران، میدان فلسطین؛
سالن اجتماعات سازمان تبلیغات اسلامی
جهت ثبت‌نام، مشخصات و میزان تحصیلات خود را تا ساعت ٢٢ روز یکشنبه ٧ تیرماه ١۴۰۵ به شماره ۰٩٢٢۶٢۰١٨١۵ پیامک کنید.
#ظرفیت_محدود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/664305" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664303">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سفیر آمریکا هم ایران را تهدید کرد
ادعای والتز، سفیر آمریکا در سازمان ملل:
🔹
اقدامات ما در صورت نیاز برای نابودی زیرساخت‌های مورد استفاده ایران برای کنترل هرمز ادامه خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/664303" target="_blank">📅 16:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664302">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
لیگ ملت های والیبال| پایان ست دوم  ایران ۲ -  کوبا صفر
🇮🇷
۲۵ | ۲۵
🇨🇺
۲۲ | ۲۱
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/664302" target="_blank">📅 16:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664301">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b9209944.mp4?token=aKFJ6DWtcDl5JDdrMNaNPM9Elbx4aMK7IPxeninnecATZ3_1Qn8YH2N4y3qViOqqVsN33fA1g6lNNthPtjGLdpYy6xRojLZyFgBhjOp7pGAok_Y7xeL6_zuqmAU8poXMMBohdKhKkgMq7J7pBNkqnJAXuq0Eg6zn7ylL-yvW_2vkPH0x4PIyH_jdh9dNWNoQn5fQp0UnSBKbMp4nOTEwfPmYPuq2WysyLyZ8IrySY_WSZjWWm5PQs4kAmYSaerCysOHXLA-6ysblhc_0i8L6YB_NdDeydQif7wG4z5tBv2frsnoS_ezsjuuKtQYNGdObsjB4OUS6tjWOJdmjIqGRjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b9209944.mp4?token=aKFJ6DWtcDl5JDdrMNaNPM9Elbx4aMK7IPxeninnecATZ3_1Qn8YH2N4y3qViOqqVsN33fA1g6lNNthPtjGLdpYy6xRojLZyFgBhjOp7pGAok_Y7xeL6_zuqmAU8poXMMBohdKhKkgMq7J7pBNkqnJAXuq0Eg6zn7ylL-yvW_2vkPH0x4PIyH_jdh9dNWNoQn5fQp0UnSBKbMp4nOTEwfPmYPuq2WysyLyZ8IrySY_WSZjWWm5PQs4kAmYSaerCysOHXLA-6ysblhc_0i8L6YB_NdDeydQif7wG4z5tBv2frsnoS_ezsjuuKtQYNGdObsjB4OUS6tjWOJdmjIqGRjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رواق کشوردوست تعطیل
شد
🔹
رواق کشوردوست به دلیل حضور ساختارشکنانه‌ جمعی از کفن‌پوشان تعطیل شد. این گروه که روز عاشورا از مشهد به تهران رسیدند، تحت عنوان «خون خواهی از رهبر شهید»، ضمن جلوگیری از برگزاری مراسم روزانه رواق و حضور عموم مردم عزادار رهبر شهید و با سردادن شعارهای تند علیه مسئولان، باعث بر هم خوردن فضای حضور عموم مردم شدند.
🔹
به همین دلیل، برگزارکنندگان این مراسم تصمیم به تعطیلی رواق گرفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/664301" target="_blank">📅 16:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664300">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-9GoGFrCpf-i7Wz--GhcGKc3HI59ecRiWhu6JRaLlEy83GN0MwQSS7kM3fpMf7m9FIqvLBQewSG_nraeOOegSnBvIcR8UhvRN9Fo5IszWssfxwncmm0GOrpirrzKSWp2Xo9Wt0X4E3RePnz3jx9VXK9zykMECEpES7mWK6QMN75D8kp2D6o2AyxmJxl2R0p3M2a94GYyOAWXi-3-T-SWzdaa4PsKAwurINj1Cqs8hjZEffN5UE-QVaqvBTFos1vgDkyLTubsfRwY-KDFTDRrOLesbYRHOQd2np-04IEdAGRqSAvDWMi6iI2TtEk5ONvv6NpBSQ3_YYwGDA4vf65Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌زدن تابلوهای تبلیغاتی توافق با رژیم صهیونیستی در لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/664300" target="_blank">📅 16:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664299">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پزشکیان: باید برای مواجهه با سناریوهای احتمالی آماده باشیم
رئیس‌جمهور:
🔹
سرمایهٔ اجتماعی و انسجام ملی مهم‌ترین عامل ناکامی دشمن در تحقق اهداف راهبردی خود بود. دولت نیز همگام با نیروهای مسلح و مردم، با بسیج کامل ظرفیت‌های اجرایی، مدیریتی و خدماتی کشور، تلاش کرد آثار و تبعات جنگ برای مردم به حداقل برسد.
🔹
در سایهٔ رهنمودهای رهبری و مسئولیت‌هایی که به دولت واگذار شد، دستاوردهایی در حوز‌ه‌های مختلف از جمله ثبات نسبی در لبنان و برخی گشایش‌های اقتصادی حاصل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/664299" target="_blank">📅 16:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664298">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/929b4f703a.mp4?token=PTxZL6sR2osG5Ob-M-ApCZVd_T2YnjI6EJStVBhbgXPCdEegBZ6d-DzJsoDMkXgDg4crxwFLz5tt_utrv8duAWhcYubF6M-VvTXAvJrXTBVC81P6m0aVugx815JLWXJcAhdbjsAVFpYQf_XrHPLIkw0gvd2p4DqnCbE1jLBC5GcTdKoozEQV2E92w43etJw1aSDuiMMFN2p_pv_LBHlRKH0__aVo861hKuzBJuyckGU6rljpbXWyLi9ccSwopyB6ZBcbAE_SEiqNxAnGOf40tF3wV7LH8cg97FqEK7hc58Ho8vAcCbUfp_Xr5x3ovJQoEoSDI0GWi6ngAuR0dA6nPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/929b4f703a.mp4?token=PTxZL6sR2osG5Ob-M-ApCZVd_T2YnjI6EJStVBhbgXPCdEegBZ6d-DzJsoDMkXgDg4crxwFLz5tt_utrv8duAWhcYubF6M-VvTXAvJrXTBVC81P6m0aVugx815JLWXJcAhdbjsAVFpYQf_XrHPLIkw0gvd2p4DqnCbE1jLBC5GcTdKoozEQV2E92w43etJw1aSDuiMMFN2p_pv_LBHlRKH0__aVo861hKuzBJuyckGU6rljpbXWyLi9ccSwopyB6ZBcbAE_SEiqNxAnGOf40tF3wV7LH8cg97FqEK7hc58Ho8vAcCbUfp_Xr5x3ovJQoEoSDI0GWi6ngAuR0dA6nPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۲ راز پول جمع‌کردن چیه؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/664298" target="_blank">📅 16:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664297">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه بین المللی نجم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebee81128.mp4?token=Sr5C2hJvO0OerHWUiOzCIHqMkCfXNLFoovOmufEoHN09X1rFsuMVMAknMKagL7iNHhKIGx5XiFZilTmiAZKdnZXUU5d7LLIaLOxZU0bSng7tcmwjIb1qWk3BZcSqV8ccF6pC-FG6yQIh_M63TicDrEufUKPBxB6Mpu9a1Uh9mO3HK-QfkIUuWikyEb4d21AKG1mgOM51fSFjRTztdzhMRCcP2uYhnFzie-ifQyVPECqE-Bmyz-cvlDLYV1a0qZq5l-w9N_WmDa2vJo9gbjUUUjWZF9UithszahAesuhjvL8bYIt4_jhHt2TgC3qNe6pHPDzoQfkj1ciGPdbSbpyKrLCZvSz6FvngUPyAa3Jz39EapoNHNLfxrMK3iElnhrDSFWJ5JLhRSAoJ_lxwxLBcTEAK-JpEA3eutT2Pt5xZ30XTCRytyqMCBuen0WHNqsmNfvI45WvAMxXPufHvr2EffP7Z8QDlAph4UMXNSaYFeqWMeytj6NpvKPxoxwbEmURC6dtHIzN_jGcC4x3dJE7eAkRuABOQoIFOLsKavGkkawqdjTVDo7z7suo7kwVkr1SaC08zUJevLiM2NOmQkFkhozqqh1iz_GdZwFbj3yEFFH9jMEPQlSZrFmdNCOKHvz1kvclrPKbAYdTxz9a-dauF0pIP0VnKmhZeqLzm0tyIKQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebee81128.mp4?token=Sr5C2hJvO0OerHWUiOzCIHqMkCfXNLFoovOmufEoHN09X1rFsuMVMAknMKagL7iNHhKIGx5XiFZilTmiAZKdnZXUU5d7LLIaLOxZU0bSng7tcmwjIb1qWk3BZcSqV8ccF6pC-FG6yQIh_M63TicDrEufUKPBxB6Mpu9a1Uh9mO3HK-QfkIUuWikyEb4d21AKG1mgOM51fSFjRTztdzhMRCcP2uYhnFzie-ifQyVPECqE-Bmyz-cvlDLYV1a0qZq5l-w9N_WmDa2vJo9gbjUUUjWZF9UithszahAesuhjvL8bYIt4_jhHt2TgC3qNe6pHPDzoQfkj1ciGPdbSbpyKrLCZvSz6FvngUPyAa3Jz39EapoNHNLfxrMK3iElnhrDSFWJ5JLhRSAoJ_lxwxLBcTEAK-JpEA3eutT2Pt5xZ30XTCRytyqMCBuen0WHNqsmNfvI45WvAMxXPufHvr2EffP7Z8QDlAph4UMXNSaYFeqWMeytj6NpvKPxoxwbEmURC6dtHIzN_jGcC4x3dJE7eAkRuABOQoIFOLsKavGkkawqdjTVDo7z7suo7kwVkr1SaC08zUJevLiM2NOmQkFkhozqqh1iz_GdZwFbj3yEFFH9jMEPQlSZrFmdNCOKHvz1kvclrPKbAYdTxz9a-dauF0pIP0VnKmhZeqLzm0tyIKQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اختصاصی| نظر مردم کابل پیرامون امنیت افغانستان در زمان طالبان
🔸
گزارش اختصاصی خبرنگار نجم از خیابان‌های شهر کابل
🔸
مردم افغانستان: قبلا در افغانستان انتحاری بود، راهزن بود، شبها نمی توانستیم بیرون بیاییم، جاده‌های بین شهرهای مختلف ناامن بود اما امروز امنیت کاملا برقرار است و به همراه خانواده‌مان می‌توانیم در ساعات و نقاط مختلف تردد کنیم و بازار بهتر شده است.
محرمانه‌های حوزه بین‌الملل را در نجم بخوانید
👇
👇
@naajm_ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/664297" target="_blank">📅 16:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664296">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
زمان شروع و پایان امتحانات دانشجویان تغییر کرد
🔹
زمان شروع امتحانات پایان ترم دانشجویان دانشگاه تهران از روز پنجشنبه ۱۱ تیرماه به روز شنبه، ۲۰ این ماه موکول شد.
🔹
پایان امتحانات پایان ترم دانشجویان دانشگاه تهران نیز از روز یکشنبه ۲۹ تیرماه به روز شنبه سوم مردادماه به تعویق افتاد و همچنین روز دوشنبه پنجم مردادماه پایان امتحانات دروس عمومی می‌باشد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/664296" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664295">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9fb97667.mp4?token=IKophT1VnXS3LfZa2KV-5m7GKR9q4G_mCdEz1RIzj4RLWrTxkz3EYOlHKhsiTY4OqlNei1WpZYavIn5XmAf24NKsXZeRH-4rM-SLtym7qGZ7-6mkmYdLMZAIk3g98G4ELlZxsKap5hXSCW-5bS-1KnwMP3V5EXyKZfhKHVigNm43qEx2fTvGfX_9to8A6UouE550rbi1toNJe4yz4CY_B8fZOOZF2WIN5Y4i7qgbK0wIYAe4AE8ZGeg6SlwWlsOxGaIZszL9ktP8DDPuITUCUd5ZW_zBq7fpGpbGLKcc2Cp6ieEiho6FqijOA8iolYs0MxY-CqvV91s06CiBb52ngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9fb97667.mp4?token=IKophT1VnXS3LfZa2KV-5m7GKR9q4G_mCdEz1RIzj4RLWrTxkz3EYOlHKhsiTY4OqlNei1WpZYavIn5XmAf24NKsXZeRH-4rM-SLtym7qGZ7-6mkmYdLMZAIk3g98G4ELlZxsKap5hXSCW-5bS-1KnwMP3V5EXyKZfhKHVigNm43qEx2fTvGfX_9to8A6UouE550rbi1toNJe4yz4CY_B8fZOOZF2WIN5Y4i7qgbK0wIYAe4AE8ZGeg6SlwWlsOxGaIZszL9ktP8DDPuITUCUd5ZW_zBq7fpGpbGLKcc2Cp6ieEiho6FqijOA8iolYs0MxY-CqvV91s06CiBb52ngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جنجالی درباره یک عروسی؛ حضور ۱۱ دوست پسر عروس، مراسم را به درگیری کشاند!
🔹
بر اساس این ادعا، داماد ابتدا تصور می‌کرد این افراد از بستگان عروس هستند، اما پس از مشاهده رفتارهای صمیمانه برخی از آن‌ها، میان دو خانواده تنش ایجاد شده و مراسم به درگیری ختم می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/664295" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664294">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3cc34ee6.mp4?token=jiZfR_LEf4WEF9wkwguXS1rksHXYnU3OC8RzXPSFDMaBq6xR36AJ7KMi5BYvBcbi244JBs2Iwb7BIYRkJVnPR_75mFFROVLnT_hrgEAuuvqEB3wjvo8DjB7snlP954XGfpdwyr5rvyZ879cmB_YWrrP-i7XZ1hz2XnlCxLS92AdEcy-wX_vJSR6G8nLge1-DaUhJQbtvKT9izYjcETlkIuyER4EcZzGQHLkyPU6TMwcJeVZ780om_0-dxxRmGj_A7Ukns-nQJf2rYzPrHW3euOoA58LN2zrK6727tNHtipnxS9SOngnv2U62TTZ4H2s5jMeOJ_0Z3z_OAnEaIzpwHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3cc34ee6.mp4?token=jiZfR_LEf4WEF9wkwguXS1rksHXYnU3OC8RzXPSFDMaBq6xR36AJ7KMi5BYvBcbi244JBs2Iwb7BIYRkJVnPR_75mFFROVLnT_hrgEAuuvqEB3wjvo8DjB7snlP954XGfpdwyr5rvyZ879cmB_YWrrP-i7XZ1hz2XnlCxLS92AdEcy-wX_vJSR6G8nLge1-DaUhJQbtvKT9izYjcETlkIuyER4EcZzGQHLkyPU6TMwcJeVZ780om_0-dxxRmGj_A7Ukns-nQJf2rYzPrHW3euOoA58LN2zrK6727tNHtipnxS9SOngnv2U62TTZ4H2s5jMeOJ_0Z3z_OAnEaIzpwHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌های تل‌آویو از ترس بمب‌گذاری بسته شد
🔹
پس از انفجار خودروی بمب‌گذاری‌شده در حولون، نیروهای امنیتی رژیم صهیونیستی خیابان‌هایی در تل‌آویو را به‌دلیل احتمال وجود خودروی بمب‌گذاری‌شده دیگر مسدود کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/664294" target="_blank">📅 16:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664293">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
لیگ ملت های والیبال| پایان ست اول  ایران ۱ -  کوبا صفر
🇮🇷
۲۵ |
🇨🇺
۲۲ |
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/664293" target="_blank">📅 16:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2a9f660e.mp4?token=BYdowkFpiogERbomzvf80si_uR_LZPuWVBaQg2RIeeGmFhhN74O6QssrNT5ehNqqhBRqhc-q_f2XCPzW1fU6krwIlYcZbOb_h_asvDpwAka-OXZsa3ahdI9q7a40pHOeclHybbHPkAOteKBZ8vtvlPUUtfJf1vmYg1lBbybQKv7TOBHDQMnBNQPtZLn-VBfvYqjqhPEJ7jvXoaT3siAx7m8cS4U98u6TvRtN_Qc97qAoslClIW5UOVWtBAgC-zXJwzkTXh8OXzM0yZTuClA3vItY7bxbaZL7MAyDu96XHo4SBY385WecIYAnnH7F5r_HT3q4pi3vjfvEZ01Zv9hEUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2a9f660e.mp4?token=BYdowkFpiogERbomzvf80si_uR_LZPuWVBaQg2RIeeGmFhhN74O6QssrNT5ehNqqhBRqhc-q_f2XCPzW1fU6krwIlYcZbOb_h_asvDpwAka-OXZsa3ahdI9q7a40pHOeclHybbHPkAOteKBZ8vtvlPUUtfJf1vmYg1lBbybQKv7TOBHDQMnBNQPtZLn-VBfvYqjqhPEJ7jvXoaT3siAx7m8cS4U98u6TvRtN_Qc97qAoslClIW5UOVWtBAgC-zXJwzkTXh8OXzM0yZTuClA3vItY7bxbaZL7MAyDu96XHo4SBY385WecIYAnnH7F5r_HT3q4pi3vjfvEZ01Zv9hEUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاق عجیب در مشگین شهر؛ ورود سیل به داخل یک پاساژ
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/664291" target="_blank">📅 16:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664290">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
مردم نگران پیامدهای اختلال‌ اخیر بانکی نباشند   بانک مرکزی:
🔹
در پی اختلال‌ ایجادشده در بخشی از خدمات بانکی، بانک مرکزی از نخستین ساعات وقوع این شرایط، موضوع آثار ناشی از این اختلال‌ در امور جاری مردم و فعالان اقتصادی را در دست بررسی قرار داده است و حمایت…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/664290" target="_blank">📅 16:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664288">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a65fff145.mp4?token=SiK4323shFjbIzxlUMiXV2HSHmbJS7u-9apq456Q3doLWCccxluJdsV66IfTxr_UuOePhTfOQMLGc3eIoAqb5kpSe0pu7XrBopm7JC3S7JRXUv0vrRBAKwh09PNsluK8inrSgNzbozuCbTaqeTuGMxojjz0f9ZbE0bzXfer09Gu0FGbxg9kk1yd4NhJ_o6PdZCUOrClffcjbCKl05h-d-BQYuMqpMq2GgriRMDiMpV0PDSv6Dhl87cwtKeemzNpsI2e7eUIg4Bz3YWIvuuy4mFv_6ekRqz_rJDnHKwP_rKfkxfiAUp5V_KtN_emtrdZgD2nJZkc7ZPKXSLJfjYSpgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a65fff145.mp4?token=SiK4323shFjbIzxlUMiXV2HSHmbJS7u-9apq456Q3doLWCccxluJdsV66IfTxr_UuOePhTfOQMLGc3eIoAqb5kpSe0pu7XrBopm7JC3S7JRXUv0vrRBAKwh09PNsluK8inrSgNzbozuCbTaqeTuGMxojjz0f9ZbE0bzXfer09Gu0FGbxg9kk1yd4NhJ_o6PdZCUOrClffcjbCKl05h-d-BQYuMqpMq2GgriRMDiMpV0PDSv6Dhl87cwtKeemzNpsI2e7eUIg4Bz3YWIvuuy4mFv_6ekRqz_rJDnHKwP_rKfkxfiAUp5V_KtN_emtrdZgD2nJZkc7ZPKXSLJfjYSpgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌های تل‌آویو از ترس بمب‌گذاری بسته شد
🔹
پس از انفجار خودروی بمب‌گذاری‌شده در حولون، نیروهای امنیتی رژیم صهیونیستی خیابان‌هایی در تل‌آویو را به‌دلیل احتمال وجود خودروی بمب‌گذاری‌شده دیگر مسدود کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/664288" target="_blank">📅 15:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664287">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سید صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفت!
🔹
شهید سید کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/664287" target="_blank">📅 15:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664286">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037836dcf2.mp4?token=XkXv5iD0a91aVOrYJWlOZsx0_kH0haSPOuh7myBxw91Aw9zn9U18mHuVjopeghSkwDKJNYsTCJYEjZLezKrSyUDHP76RX5On9GYIZgZ6TNvLzQJDfEcPMZnteX4vVq_bR5iXBd4JHhFrwYn8fSVa5f4cTrW84FL_-nHCXCHsrcmrUfu-r-bkY8tPHb7z9drPezRtYzP9LusBzHcG7hycn7xYbkbr5jN5eamPUvyIBbIXORoJu2H_BJB4B0crr9O_A-bhyAOYSsi9oO1cL4uVkmRlutXTt_PWWRs9B8k1ZEtMa4_VUFIaHQaYCF7caohtDo6E_YzPQDCY4sWwJ_ADqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037836dcf2.mp4?token=XkXv5iD0a91aVOrYJWlOZsx0_kH0haSPOuh7myBxw91Aw9zn9U18mHuVjopeghSkwDKJNYsTCJYEjZLezKrSyUDHP76RX5On9GYIZgZ6TNvLzQJDfEcPMZnteX4vVq_bR5iXBd4JHhFrwYn8fSVa5f4cTrW84FL_-nHCXCHsrcmrUfu-r-bkY8tPHb7z9drPezRtYzP9LusBzHcG7hycn7xYbkbr5jN5eamPUvyIBbIXORoJu2H_BJB4B0crr9O_A-bhyAOYSsi9oO1cL4uVkmRlutXTt_PWWRs9B8k1ZEtMa4_VUFIaHQaYCF7caohtDo6E_YzPQDCY4sWwJ_ADqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوب‌شدن چراغ‌های راهنمایی در اروپا
🥵
🔹
موج گرمای ۴۰ تا ۴۵ درجه در آلمان و ایتالیا باعث تغییر شکل و ذوب‌شدن چراغ‌های راهنمایی و آسیب به زیرساخت‌های شهری شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/664286" target="_blank">📅 15:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664285">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh2uiY2wK0DjEnmgEsfSTI5A9fb3cqz7F1U0fZs1W6IU1bI7gEaU1qqIOt5QbJqQoW_uChLEKQ-tNCaViUqeZrV-kfwwCO1ZT8XIgK4n1uHiQ6XMaQT2LCC80NHSKdmgRWGOcDBTz8fuvBY6PaE0oG2hGwE0JxdSkvA2yaPCzYgKpY2p0-NWLCbbAWdBI_uzPjF_E_1yzax914PQZBThqFc_Lk_tH9v0CowQuGCFi0oqZdXK4Dq2Fd3mAAf5jt59nEY5tjPJfssGrYhoA-OGaeM3QZ2nbcEqCnsmkj2did3gOt68w9ztvldMAml2cjNTfL3uiK8TlbPw0x0IgCFKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرگ خانواده فوتبالیست آرژانتینی در زلزله ونزوئلا
🔹
لوکاس ترخو، فوتبالیست آرژانتینی، در پی وقوع دو زمین‌لرزه در ونزوئلا همسر و دو فرزند خود را از دست داد؛ پیکر قربانیان این حادثه پس از ۷۴ ساعت جست‌وجو از زیر آوار بیرون کشیده شد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/664285" target="_blank">📅 15:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664284">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
لیگ ملت های والیبال| پایان ست اول
ایران
۱
-  کوبا
صفر
🇮🇷
۲۵ |
🇨🇺
۲۲
|
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/664284" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664280">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGK1-o1D7r3At_-MIVDgu3Bz7kvRdPvvCLNuDDXs73WPox12iC6FyhJkTa7eoTkMUZcqEnbIsjDUwISpqrOgpKAxQAXjnNxNk65o9pBG8uEQF0gVR8zhVo6nGIejr2G7YcZnWiPZk_5L8nai-uT3uK_WXkl8XIubFzvPUlhTGNVQeTC6Hzj1NeuMukMPo8vuKHGoDMRUCRHh0dgITKQCt4LPqrOzdBzn20p2YDEjprxww4flr9lZOF2XPgMeWBk5xK5SEeACGnYNVLI5NsLgisTOPPc0MoRqgyZ4pzyAP24YF1IvY4I9el23qKKYun010_L-M9Vde_Y47NuTcd76JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cb9bDO2ZsjQ-uXgQW0Wo29v7-zD1l4XnlTyFNavT8k_ytgU0vg2aiy0qK4IrU5yvLeKER1T2DeawCT95tRnrwfQH2B11tfPAtoTKmpB0BuBw9mLJLBufJIXnoraLce1pOFKhFhW-wMxDXHSQxDdVPxGycHGe8dTtmey0MMPFAXOuCghZfRJ4Po9l6ESeedVJuFwwbYcuUp0oQtv3eWkr3Gsqyq7d1zaCQmjiRrwhFZ3zs7RrMMoadmdjmO5AVuF5lNmP21lChHvAtrePA46jxKV9grS5qa1AIqdtrK8-45DzCuHSURoSpiNWJlgKitLW5AjQlvwKCteQj0HTwdvkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kfz7Hldz1-9BBk-fIts0oK_VKrDRTiTGE5Uhaayg89mdYvyQvH7zWhgl8i3IlCpBAcbjewJ_3idC_uFe5FLj5IDQ_02k3-YfouJL3qggMhuD3TpzBwNcYhSKLgT7Eb-c3E6fTbuMeJvPJvz8pizXKDH_BJef9VI98FQDCo_a1_WH8_1LRCuf__732yLSeWB0y8QNQidAT9apakiBeed7ajCjRpP2BbDRzva-3GBBzxYXj62jilqeQTWnhJWjcOS3iE9Es-yXUsB5Q0Z7HtHyQQONT2pEBbAVaYi38FQsSO_-QjSbX9VcxaxLFK-AQyxMEPGkUWH89B_T8v0LkuwVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4C7S4Gy94qy5MWHYsCvLQQTt6CYHNGPWeRhu6aqn5Htl10sE6Zo748Oxx4RT8nuFgYujMhSjiRX4hdcuK1VF1AiRsSHFTD64a8B8RLAAzd7VfVDJBnHvcaOgtvekNr45x7jQ6g6j_D0VDdrRhu68B_9KB7o-0pbGalmk4_Y-_gsBN3sSgdupDMYspKN14qPQuU69xsJ35wwhmNzsOyecnlHF-oKOy1_ElKtBEzhuaqqhkPwKzZFvBT9MuEN2qkr0ZU_gSuXK7zab1aAYvV7G1gp7uh0IzwoBqeffQ_yx5FMvLHCCwmAFsmGzlzUDCclG0owYVELPDXkTARK4xsxIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وعده‌های بی‌جای مسئولین، برق خانه مردم را قطع می‌کند #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/664280" target="_blank">📅 15:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664278">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635706bbe7.mp4?token=Aa65AqjvfF7nmsCpko2Nn_D5oKl80ZgngDsrHOmW9M_Sk35mCa3gYk90rPeTHTvFbm2HW0uottrGcEWNhodzFE-qGrfVqPSp5U5o4hOsrx2i7iy1T2AfvykjB4o4JHRn1NSlUmnzVz12tlQvFYBxthaULVbObQaWpToh8w_ayjfoK6Q7n3SZvf-EvzuKracz-KIKuAIEWlw830K7TrUT8FKGkberGtoWUdyjGtienrDWWlz5TfMNEkPQFFTnN05UVHmOXZqexlRg_MgM1v_Z71aTPBAmmy4vKsLZfTJtjMSYP2rl26OTh0WBFq2Pa_YLME3zp_nY9y1egRnOZgJskpCWLOL63kRxyeACB_ToPnHhrh_CAe5r9IY_7M3Io7ILz1deTkfyG1rsTu_AQ5eIhkl_5wHHca3xQAsW6LzJKmD2diQlfpjYuXSw8U3qwsZomxJ35ZJ7-OrfFqum3Rlx3vwSwY95TE-N8FlzBCVhck3rPvi0PO9TEH7s8BPYpw08UXyqDXdRQ58JXZb08s9w85E0Gth42lftvfIBTlpdm22xVVNPepuBt_nK1mhdo6fXjvIcqBccLT7BhDJZSi2odyAWwNposNjrsuC8edO5x_sPiygKaNA0P3UkcMID3L7EbfSyRsdoDXs-oZkUgbUFqdvbWRBiExJvj06714X9Ips" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635706bbe7.mp4?token=Aa65AqjvfF7nmsCpko2Nn_D5oKl80ZgngDsrHOmW9M_Sk35mCa3gYk90rPeTHTvFbm2HW0uottrGcEWNhodzFE-qGrfVqPSp5U5o4hOsrx2i7iy1T2AfvykjB4o4JHRn1NSlUmnzVz12tlQvFYBxthaULVbObQaWpToh8w_ayjfoK6Q7n3SZvf-EvzuKracz-KIKuAIEWlw830K7TrUT8FKGkberGtoWUdyjGtienrDWWlz5TfMNEkPQFFTnN05UVHmOXZqexlRg_MgM1v_Z71aTPBAmmy4vKsLZfTJtjMSYP2rl26OTh0WBFq2Pa_YLME3zp_nY9y1egRnOZgJskpCWLOL63kRxyeACB_ToPnHhrh_CAe5r9IY_7M3Io7ILz1deTkfyG1rsTu_AQ5eIhkl_5wHHca3xQAsW6LzJKmD2diQlfpjYuXSw8U3qwsZomxJ35ZJ7-OrfFqum3Rlx3vwSwY95TE-N8FlzBCVhck3rPvi0PO9TEH7s8BPYpw08UXyqDXdRQ58JXZb08s9w85E0Gth42lftvfIBTlpdm22xVVNPepuBt_nK1mhdo6fXjvIcqBccLT7BhDJZSi2odyAWwNposNjrsuC8edO5x_sPiygKaNA0P3UkcMID3L7EbfSyRsdoDXs-oZkUgbUFqdvbWRBiExJvj06714X9Ips" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت ونزوئلا بعد از زلزله های مهیب چندروز پیش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/664278" target="_blank">📅 15:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664276">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0lSW-c-FCMBGx2CbaFV-dNfXXJpzPi__pNVpRZRjLN8Fs3LR4mdtja6IdnPEJZQwBgHD-A-xreI28fdK8G7eKPT-0GbJa-Y5aW-a4gWlCiPXcnftatydrP7jXcljAWHAzqPDlTo69-LKQLpkJvF63TDZwaCT87hmD3bmYsbH-Lx-WCqq2-pf1IaDSOglXtdE-zzHn1hbiS7U_MPMfx9Yv9MlkJMrMDVWZrfAwzSsNUWUCv_T6TpN_N8Nk-n3QnGsqLzvUvxt6iqY9yorqUXXP7R1YhvekBuXY_2tjRE4duN1bSD72LYqng0s26cXXfTkEFJpC94cSO3iyzaBw_DSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جکسون هینکل، فعال سیاسی و رسانه‌ای آمریکایی: فیفا از هر ترفندی برای متوقف کردن تیم ایران استفاده کرد؛ فیفا یک سازمان صهیونیستی همجنسگراست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/664276" target="_blank">📅 15:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664275">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICWiszix4imzQj-kVWBWKwxTReG9ey4RdZHCCbwSXOUx7QCP-_42PpgDL7EhSVzegN7UBUvJFbI4GrRWKCpX5YivyubZT8kJFnSOjvicbyESVWkNhYGs_g6l5nLBvXcrAe4n15DVHoD2p6b8SaAsPjlg3VKYvXQSttNlSWntQJr7bmlbMFQIQyXYIPbtBRCGUCehOrIGZdDgDE5To2dBOyw2EPgfaubIzpmhB-4DuxO046G7ZKgeNFppiZq7RHNPQmKlozZmoc9mO-ybDy-oPX1SCA0FvtbJt91Py_RqQeJd3BThDuUpmvyWlo2CvbXTtKU1OaSdO64ZXCyv3iyDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ دقیقه استفاده، ۵۰۰ سال آلودگی
🔹
یک بطری پلاستیکی را فقط چند دقیقه استفاده می‌کنیم، اما همان بطری می‌تواند صدها سال در طبیعت باقی بماند، به میکروپلاستیک تبدیل شود و در نهایت دوباره به سفره غذای ما برگردد  شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/664275" target="_blank">📅 15:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664274">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6zClQ8JD_wpZv1bROvxYQ00MffYn4RW9-NtTKTS5NxbA_SRH5zP039p9JoZPGzjMai3Fi8tkZsLwfgcsFTcht6CFWVdGQIgffJC356C6soH4l4xbHQV2bMoFSICKVQWY2aOmmE-8tR_dNozmjbECm7eBjjjGaZGsm-a8wysQDkiLezKi_0OK-_HYskk5mOIqzIdcj17UHcUnOrz_pJZh-tGyvPXBXao7eVNEDeu2VPvSYJEeMaQd9bX3Yok64SL73myW6Ka2XFDO9GZdfkLbDqkcdf-6DhXx73lFjceigLm8gysiLOPzxI4XLe8gSdJGDY03K3eUhIF2IoI4ydkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کمجا‌چوب مرجع تخصصی مبلمان تخت خوابشو و تخت های تاشو
✅
فروش ویژه تخفیف نقد و اقساط
مبلمان ال و تخت خوابشو
سرویس های خواب تاشو
کابینت و سرویس خواب
جهت رزرو و ثبت سفارش و بازدید حضوری
☎️
02122141020
☎️
02143000098
جهت بررسی محصولات با ما در ارتباط باشید
🧨
❗️
https://t.me/kamja_ir
https://t.me/kamja_ir</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/664274" target="_blank">📅 15:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664273">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
دادگستری استان تهران: تعاونی اعتباری منحل شده و در حال تصفیه مولی‌الموحدین هیچ گونه ارتباطی با موسسه خیریه با همین نام ندارد
🔹
روابط عمومی دادگستری کل استان تهران در پی برخی برداشت‌های نادرست از اظهارات رئیس‌کل دادگستری استان تهران درباره پرونده «مولی‌الموحدین»، توضیحاتی را منتشر کرد.
در این اطلاعیه آمده است:
خبر اعلام شده از سوی علی القاصی، رئیس‌کل دادگستری استان تهران، درباره صدور حکم ضبط اموالی به ارزش بیش از ۲۰۰ هزار میلیارد تومان، مربوط به پرونده «تعاونی اعتباری مولی‌الموحدین» است که پیش‌تر با این عنوان ثبت شده و در حال حاضر منحل شده و در فرآیند تصفیه قرار دارد و اموال آن نیز به بانک ایران‌زمین منتقل شده است.
🔹
تعاونی اعتباری مولی‌الموحدین هیچ‌گونه ارتباطی با «مؤسسه خیریه مولی‌الموحدین علی بن ابیطالب (ع)» که در استان کرمان در حوزه امور خیریه فعالیت دارد، نداشته و خبر مذکور ناظر به آن مجموعه نیست.
🔹
توضیح حاضر به منظور تنویر افکار عمومی و جلوگیری از هرگونه برداشت نادرست منتشر می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/664273" target="_blank">📅 15:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e7054476.mp4?token=rsWunR_yb5Ifye5VX38zXutHchnFLRqSDIK0gRBVT63sLyp-V64SFOgVaMKknMD1v49xXifAxEHiNR8ToKYjrnOYq7t23QrnnbQ4HHxrD4Y5aUkCyCkYM2gp6Jdacm3IQAPXCpEwE5JMD7WnpHJmUzfmrmdr87HBPkw8syvRprvDBwzooR-GIcrGwNxkfaCbjmSb-Gv6bWvPtu6LAezeqoCf9gDPO-AAAsxumhXgnZTrQJwxykWpMpSdZNYDqGMp-8xuC9zyrO_sqI2w3M1ClsyKigTTJ3mOGoiIkDBKNIoYFdrRHOa-YIQj2aumUEC3V1C6C5SJBohTUYIqNjy-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e7054476.mp4?token=rsWunR_yb5Ifye5VX38zXutHchnFLRqSDIK0gRBVT63sLyp-V64SFOgVaMKknMD1v49xXifAxEHiNR8ToKYjrnOYq7t23QrnnbQ4HHxrD4Y5aUkCyCkYM2gp6Jdacm3IQAPXCpEwE5JMD7WnpHJmUzfmrmdr87HBPkw8syvRprvDBwzooR-GIcrGwNxkfaCbjmSb-Gv6bWvPtu6LAezeqoCf9gDPO-AAAsxumhXgnZTrQJwxykWpMpSdZNYDqGMp-8xuC9zyrO_sqI2w3M1ClsyKigTTJ3mOGoiIkDBKNIoYFdrRHOa-YIQj2aumUEC3V1C6C5SJBohTUYIqNjy-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهرام جیزه، مصر
🇪🇬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/664272" target="_blank">📅 14:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiLRzelanxYlQDg7WH06SdiV_zvuoD0knvWOZcVzTFmXulUJT9-9J2rczpSnsx829KFNOzzsT7h88HuGHcQauXD4fLHtEGlVR0VLRPuQPwKJjfIfcCMIPiCkFuohZpie4YfvnsQfd11Rg6SgQz2wjDNRfeGvHGatGrv1G3SJV6Kl372yd-DUY0tTiYKt1M2psNkgF0lwI5QBTqoP0aWQy8V4C2GYbXuzZhRoQheVAFuEVola_DrQ2VdMNRhg-4YUjefiMx8P2gjNwrvJ1ZUvl9tFuxnmRkMe3-nQG0m1r--OxlcX5QB5fKvPOhR-wiviU11O9Izb0bKr24YOQOFg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان دسترسی به خدمات سلامت در کشورهای مختلف چقدر است؟
🔹
کانادا با کسب امتیاز ۹۲ از ۱۰۰، بالاترین میزان دسترسی به خدمات سلامت را در میان کشورهای منتخب دارد.
🔹
ایران با نمره ۸۱، وضعیت مطلوبی در شاخص پوشش همگانی سلامت دارد و بالاتر از کشورهایی مثل ترکیه و عمان ایستاده است.
🔹
افغانستان با امتیاز پایین، یکی از  کشورهایی است که کمترین میزان دسترسی به پوشش همگانی سلامت را دارد.
🔹
اگرچه برخی کشورهای آفریقایی پایینترین میزان را به خود اختصاص داده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/664271" target="_blank">📅 14:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KbFepfWTiTJNigWkKEjP1d_3NBnO6EL-zDrnK4z_K4qBtd9pAlCXi8ByejVaEVXYkc-6LyF5SetYHNECTQF1QSfwIfeyH5swDq5QXLElgef_AWWqQ53jtA38uzC5St0STgJ91EyR68XyjlYaYZu8dT-9wp_sBvGZs8dKAsHMx6HqNbq_-NagLgD8S-Xf1krlP6y2JfTTyCjTynsWGbl-Kz8H83Sw5Kucohz8OhMzXT7-Xx0_in-QYGfWdkqRAPDG5OvRzdsFgTILfkvEgvtnTw-EqpuRjkGDAja7BC7rs0VjtdMnLf5BLd-s-rDGX0VjoYagTJIVkmZkziu9K-FpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSy0awH4jZpD2joUPIXkEo9w2Isk13StW6RgB4RSydH09HfH4zVkHF3baxjkxugF_wiaHVXtyDOLI4rb-oeDtfV-inrgEvEyvlrzLQPr8gOdnqUfcTa1Hgs434aVnc5BI2vT7KdkMRGP23B2I63MPPCTIUo1Q_KuU5C75d4jgaT9kOPQkvLH1CNq8u0pzlgKL1Ahgtr2T_plbBk1H_Ik3hrYOgrjlNS2n2OGVEzgteMLpgeShA1RARVt2lVfXsXHH1Mp47C3-MMkV1ICaEJAVjMH_xdEXDlH-t_UtXXjCZXNNap69bVRlJV4DRwkaY-AGUkwj20-TkPeTqr5G1dq9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سید عباس عراقچی وزیر خارجه ایران در بغداد با علی فالح الزیدی نخست وزیر عراق دیدار و رایزنی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/664268" target="_blank">📅 14:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
توقیف تمام اموال ساعدی‌نیا در نوشهر
دادگستری نوشهر:
🔹
اموال ساعدی‌نیا در نوشهر به‌دلیل اتهام حمایت از اغتشاشات و ارتباط با جریان‌های معاند، با حکم قضایی توقیف و برخی دارایی‌های او از جمله یک کافه در شهر پلمب شد.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/664263" target="_blank">📅 14:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh423HnbMt6Y1oe4n-j-IL9N5a5XsZaG49jkv0I6swj61GdD7a0ExnzOiOP6SLuX3tf-lQmcgqNnNpWBxk75t6YTz2CcNBIiT7siciPirUKadg3fZhaTyiw2i2IuXZEeEwXLQ1-O6laIomEu_UAiGc_yuOuZszk5P7odO4dKQmX-lJ8vimcdw6PvyRelBykpl14LDUdQ1V94Kf_T_7HlaqCk3W6f7dykH_TmSBDqLRqYV_5lxArxIZdKIBZ0CPjSf7dNv9o0Y21odp_XTWr5X3582Nkl_GJdELXQs-dNztp6p3fwPgAkgufbD1n9nlQih0pCqMIQjHhU-V2DmpdLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور علیرضا بیرانوند در میان بهترین دروازه‌بان‌های مرحله گروهی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/664261" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkmgGWaGX4ethjbguG8lnpHkQIb5XwArH9kL2e-BZ4JZQ02fU37mK_31p-G0gYAae0fssODLcPoefBstBm2DWCrs4n1I014mDyYMod1ZVx0XMEL6OxSUFKOzK3JmHxuhvPfiAGJvu3UFxBuMP4tV3GxJVyVm6uLnso5VKLe4uKqr-XH4TrQ-Anu4bCNI7npCmVgDjkyeG_AiIamWRAqAofkOdtRH8YtKK1eeVsKiByMyw_LYpeYLEfIAWhuMFi45QIjl0RkT8OqJ0C-C5fvvK9uUPYgaXOfIIwEmCIBQhFfboOLPoo--7kgE2n4CtSf-A3uZJcSHgQDuY8m7iOJAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امتحان نیست، ولی بد نیست معنی کلمه «مالیات» رو بلد باشی
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/664260" target="_blank">📅 14:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tle12Z-jqC3gXczH1yWNIhxJvYF40GvpB9jUf1GWBwySm9YxKCL7cFb5HqHtpbnzoAlKa0A98DSZMYMVabZOKaOJRW4VIZLeW8bRl_sS37_S3Hcq_6_uJGOGGfbS6z037WzqUuO7sKjuVHSDbM-Rc8daRJeWezwlrne03cqdtHVUs9uJ8_E311Cq5H701O4YhkTp4FWIbfkkcEZR-QrP4POYoYjOinLWWcQpYAxVKi4OUW3gkui3PWCyJl3VnR-Z6EzG71WqPNIZB50qQpvgFIEuLth84hBN0ECQ8umNGHgYmnGzHPgJYhvd5yP4ZfzLY4RHxs11R8Q5G-1aOWzrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سید عباس عراقچی وزیر خارجه ایران در بغداد با علی فالح الزیدی نخست وزیر عراق دیدار و رایزنی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/664259" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664257">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3oWHTyotPuLiJTpGS6l9SjSbfZgW_-a1CDjsuIthUCtIB9of2jbwfsImjRLqymMiMPIZ7ey109dE4nuL5SoPqCOvIJ3_GGo9zP3c7gyTM6zo_34Ge7A8A4jPA14O6EEr7bMIouACxKaDH3IlSaCuKkGGuZF57lNo_xNMFl2_hh2OY1_6dApjRuBELM6kllJaIIz2c_NKfizMnb7vtsWMcp0OPpzvrOCBMe8QAr2k4bkcUqTTamzdxA_dDdF5fls5XMz4E6MKzZt9Top9dHba7XeowlE6cBOqBrFxIEMXMs2qXipDvHgI11K4w1fNVPnkVQnxFMRaFSkz0hn6V7riA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
حضور مهدی طارمی در میان بازیکنانی که در مرحله گروهی جام جهانی ۲۰۲۶ بیشترین تعداد تقابل‌های مستقیم با حریفان را با موفقیت پشت سر گذاشته‌اند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/664257" target="_blank">📅 14:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEGZVcGsJ7wCfXvzfcwYyiip6U08hHm1kicTkQW0XsB-bwpQvdITK4FuYQasJzWqPlpRPpCUOAPHpXUEyQc1Bik1bJrYNrf3kzPKJ4ZZYwgnhMTH7Sxh5_QA7H2380VD9WkTwGgv84yg10KmDp6PQgwtiDpV8TpmisEH445GCeb03ONSC6Mn3DUP55TzAb0-n7ILxNxBrhkonswFC7yMrrrbhDbvGKhh9dGRtJojKy7kcPHdcje0ALbV5vJCbHFK4MagHf9aJyBrRk8-cuNn7AgMYwZTvRjPdGacklvYToYDRmXSSDsFT01-qgTRS9-BXkhfkaZCR2Y5a10z5SLnlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده‌ها کنتور می‌اندازند!
🔹
با وجود وعده وزیر نیرو مبنی بر نبود خاموشی در سال جاری، قطعی‌های مکرر در نقاط مختلف کشور خلاف این ادعا را نشان می‌دهد.
🔹
مردم انتظار دارند مسئولان به جای انکار این واقعیت پاسخگو باشند و راهکار ارائه دهند. #برق_مردم_کجاست
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/664256" target="_blank">📅 14:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPEsCBo8zhBkX7R-ufzR0qJkd0DTi_HKC4_ZFF8PwbA39OeYrDiJqL80zu3NKa-uOoa8zwZdiryoNi1emXr0mpu3YgkurL8dbepJe3bCkYYgZR4932NcGt0iH71zuaCRF-d8J0XgPB8rUg_oaX_knimOMK9NOsqT6PdgfvrZbIi1_AOVgQRQtxQ9h6hPjGkq3Hox_1quHW1JdLEbkGOLspvPXiaz1X_upbE0WFjf9Bg7KS6o0RaDa2FpD_l72DLhxXokLKKaDzyhAr03oNBpz6u2TwCcXgQmqNhzPOhOV0j6v4AvoTBhqpK0YaVc-5_3HTE0vH7sOuGK61651oU27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای
پیشگیری از گرمازدگی چه کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/664255" target="_blank">📅 14:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔹
ثانیاً لازمه‌ی توجّه و اهتمام به اجرای دستور رهبر شهید انقلاب در آخرین دیدار مسئولان قضائی با ایشان در تیرماه سال گذشته نسبت به رسیدگی به جنایات صورت گرفته در جنگ تحمیلی دوم، تسرّی دادن آن به جنگ تحمیلی سوم و پیگیری مستمر آن تا وصول به حکم و واگذاری اجرای…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664254" target="_blank">📅 14:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664253">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وچهارم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای محسن اسکندری که در سانحه آتش‌سوزی روح از بدنش جدا شده و توسط موجود عجیب و حیله‌گری در بیابان برزخی هدایت می‌شود تا اینکه به ناگاه متوجه اشتباه بودن راه و حقه آن موجود شده و از خداوند طلب نجات می کند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: محسن اسکندری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/664253" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
متن کامل پیام رهبر انقلاب اسلامی به مناسبت هفته قوّه قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش
📝
بسم‌الله الرّحمن الرّحیم
🔹
ایّام مصیبت آلُ‌الله و شهادت حضرت ثارالله صلوات‌الله‌وسلامه‌علیه‌وعلیهم‌اجمعین و یاران باوفایشان را به همه‌‌ی ملّت ایران و امّت…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/664248" target="_blank">📅 14:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
متن کامل پیام رهبر انقلاب اسلامی به مناسبت هفته قوّه قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش
📝
بسم‌الله الرّحمن الرّحیم
🔹
ایّام مصیبت آلُ‌الله و شهادت حضرت ثارالله صلوات‌الله‌وسلامه‌علیه‌وعلیهم‌اجمعین و یاران باوفایشان را به همه‌‌ی ملّت ایران و امّت اسلامی تسلیت میگویم.
🔹
نهضت و قیام حسینی برای اقامه‌ی حق و اصلاح امّت و مقابله با ظلم و ستم، قلّه‌‌ی بلند تاریخ در تقابل حق و باطل، و عدل و ظلم است و درسهایی بس ارزشمند و فراموش نشدنی برای همه‌ی آزادگان جهان دارد. خون سیّدالشّهداء علیه‌السّلام را خون خدا می‌نامند که در رگهای عالم جاری شده و حماسه‌های حیات‌بخش می‌سازد. نهضت و انقلاب اسلامی ایران، از آن‌رو که شعبه‌ای برگرفته از همین سرچشمه‌ی نورانی است، باید همواره در پی دستیابی به اهداف قیام حسینی باشد. هفتم تیر هر سال یادآور شخصیت برجسته‌ی انقلاب و آن کسی است که با قرار گرفتن در رأس قوّه‌ی قضائیه در این جهت تلاش بی‌وقفه‌ای را در پیش گرفت تا آنگاه که با جمعی از یاران مخلص انقلاب شهد شهادت را نوشیدند و مظلومیت او و عدد هفتاد و دو شهید همراهش تأییدی بر حسینی بودن این نظام و معمارانش گردید.
🔹
شأن قوّه‌ی قضائیه در نظام جمهوری اسلامی ایران، پاسداری از حقوق مردم و احیاء حقوق عامّه و آزادیهای مشروع، مبارزه با مفاسد، اجرای عدالت، و اقامه‌‌ی حدود الهی و نظارت بر اِعمال قانون است. ثمره‌ی موفقیت در این مسیر، علاوه بر کسب رضایت الهی، تقویت اعتماد مردم به این رکن نظام خواهد بود. انتظار بحق از همه‌ی قوا، دستگاه‌ها و نهادهای مسئول آن است که همواره عملکرد خود را با تراز مطلوب نظام مقدّس جمهوری اسلامی و شأن والای ملّت، تنظیم و بازآرایی کنند. در این زمینه قوّه‌ی قضائیه جایگاهی کم‌نظیر و بلکه بی‌بدیل برای اصلاح روند امور و به حرکت درآوردن سایر بخشهای نظام دارد که این مستلزم پیگیری روند اصلاح و بازسازی در داخل خود این قوّه نیز می‌باشد. اکنون انتظار عمومی جامعه آن است که شاهد تأکید عملی بر این امر در عملکرد قوّه‌ی قضائیه باشند. به‌ گونه‌ای که تحوّل قضائی، از کلمات درج شده در سند تحوّل و طرح‌ها و نقشه‌های راه، به فعلیّت رسیده و جلوه‌های آن در همه‌ی عرصه‌های مربوطه، از اتاقهای مجتمع‌های قضائی و جلسات دادگاه‌ها تا محیط‌های عمومی و فضای اجتماعی نمایان گردد؛ آنچنان که مردم آثار مثبت آن را در زندگی روزمره‌ی خود در قاطعیت مقابله با انواع مفاسد، کاهش تضییع حقوق، سرعت رسیدگی، ارتقاء سلامت و اِتقان آراء قضات، و دسترسی آسان‌تر به شاخص‌های عدالت مشاهده نمایند. در این تصویر از قوّه‌ی قضائیه باید اجرای عدالت به پایه‌ای برسد که هر مظلومی آن را مأمن خود بداند و بخصوص کسانی که به‌نوعی از قدرتی برخوردارند، جرأت تعدّی به حقوق دیگران را نداشته باشند و باب سفارش و توصیه در آن به طور کلّی مسدود شده و داشتن آشنا در بخشهایی از آن هیچ مزیّتی بشمار نیاید.
🔹
البته احقاق حقوق ملّت، تنها در مسائل فردی خلاصه نمیشود و انواع حقوق عامّه و اجتماعی آنان، از حقّ امنیت اقتصادی و دسترسی عادلانه به فرصت‌ها تا حقّ برخورداری عادلانه از مواهب طبیعی، محیط زیست سالم، آزادیهای مشروع، و حکمرانی کارآمد نیز از زمره‌ی مسائل مهم در جهت گسترش عدالت قلمداد می‌گردد.
از جمله یکی از مهمترین مسائل حقوقی و قضائی مربوط به همه‌‌ی ملّت ایران در این برهه‌ی زمانی، پیگیری و احقاق حقوق تضییع شده‌ی آنان در اثر جنایات مجرمان بین‌المللی و مستکبران و تجاوزکاران جهانی بخصوص در سالهای ۱۴۰۴ و ۱۴۰۵ می‌باشد.
🔹
از خون شهدای مظلوم جنگ تحمیلی دوم و سوم تا صدمات و لطمات جسمی و روحی و مادّی و معنوی وارد شده به کشور عزیزمان و هر یک از آحاد ملّت مظلوم ایران در داخل و حتّی خارج از کشور؛ از کودک‌کشی‌ها و جنایات جنگی بی‌سابقه در میناب و لامِرد تا حمله به مراکز درمانی و خدماتی؛ از کشتار نوزادان چند روزه تا کهنسالان عزیز؛ و در رأس همه‌ی‌ آنها شهادت شخصیت بی‌بدیل، گوهر بی‌همتا و یگانه دوران، پیشوای مجاهد عظیم‌الشّأن اعلی‌الله‌مقامه‌الشریف، هر کدام پرونده‌ای از صدها و بلکه هزاران پرونده حقوقی مهم را تشکیل میدهد که در محاکم قضائی داخلی و بین‌المللی باید با جدّیت دنبال شود. آنچه مسلّم است گریبان جنایتکاران را بایستی گرفت و آنان را به سزای اَعمال مجرمانه‌شان رساند.
🔹
نکته‌ی مهم در این مقوله، اوّلاً اعترافات و حتی افتخار وقیحانه‌ی بعضی از سران دشمن امریکایی، صهیونی به این جنایتها است که قطعاً اقرار به جنایت محسوب گشته و مقدّمات احقاق حقوق تضییع شده‌ی ملّت را به شکل مناسبی فراهم ساخته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/664247" target="_blank">📅 14:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlXDlKl1_YWHnuYVTbyXJfAsbUyLZg-IVdXVX1fl5Z73bGPAw_ld3jsGsoKEfsi3Mm_kdJNNBTTalBTHme2V7M8bpH7H0C--1cz_6iWYBKsyeta2-nZ89gJERED3bkTWcsQsjAc1zqQqkiBtL_ZV5jmjUaJNi_lzu1EiDQKXL1QOxaXzKIgyqLnFPYgGhgYkIgD-ITRbL2YjrQUjJqzbz-kf82az8UBixbYUXOXkIu7E0EuhL0sjWcvZxJozIoDUh1DbXMlwRYRmqcK1cc_jVm7iOINy7dWUOpdLVVB26l9qegl1uup-5pMGkyQCYIDOutcOjuIrR-qlcDyzP9Dl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ظریف: بازی‌های سیاسی را کنار بگذاریم
محمدجواد ظریف با یادآوری آخرین دیدارش با شهید سیدکمال خرازی:
🔹
دو هفته مانده به جنگ، دکتر خرازی به من گفت «کمی آرام باش».
🔹
خون شهدا برای ایران خودباوری به ارمغان آورده و باید از این فرصت برای ساختن آینده کشور استفاده کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/664246" target="_blank">📅 13:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOjlgiJmzTjUDbG-_WE-N997cYO16PlqSKvDPoaFWlU4MXpDHj_OFFQwjrMzcA2Z0eRnqrYoVnkcHMVYTY01egWONobdfgtoxe7UASRsQvMkncR5p9_R0GZZzdNlrVsHuMMFAKWO20bVGhDZF-houRukM5IiuPchyXqCxjMo2BUGAHtQIG6ijBmAE-NKGepG5-WC49PlMW0Wao2dOb_6yeh7YzUPTu_TCl2F1PidIwckJ5WVQyNwlz7btdL-rZNOwIV8R5AEtRtqglGuCCAt5R3amoeKlSLTeHJzL3js3Ct-KOLF0uQhaWbE-nCW5smaUpKyToMHvijjyhaEWz3vxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعتِ صفر؛ تقاصی که گریزی از آن نیست
🔹
ما نه فراموش می‌کنیم و نه می‌بخشیم؛ تنها منتظر لحظه‌ای هستیم که عدالت حکم کند. هر ثانیه‌ای که می‌گذرد، یک قدم به حساب نهایی نزدیک‌تر می‌شویم.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/664245" target="_blank">📅 13:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664241">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsC3AgrRcXb98qUBU45ri267gRJSMMKHnR__8gZz-yzNXGKiAX2OG17utAm8NxcDmaA5gGsudg5PuAYLVPokIyXmcp7xDo28nuVBK1IMNrkmMXbHJcHnNkq-hXNyiajjzMDbHkzCiJNPx_Wt1Laef-GdYP1INVSDx29Wre_ibM43ttWSJwpkJdlE5UNsCwHm8cqXKE00KIikIechgEn-RjZVuC_a67IJaI69R8hvsM0DzzKtFZd7XJMCiVVKJkzrYqzVBIj9zi4QRT2u2n_QA46dyPd5mP_kjp7YEXxlWM3fkLvg3r6VrqQ1-sIHOJuBeB8Iucz8mpwquUhTH_uhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4bgVU6sRtOTfR8XyxEvFahDNoLmpFXR6n-JmMfDw-CSPvEqOqS4nvmMPeI0_A-UNmrW1I6DrxuAyWaN5bIoHtwVlg8mrd-PS373hSniufM1KqdvMGbKL0Xfga3fk6BX2JlQwdkd1UJSbNlCDsMBw-NeEayfs2BP8SxROCfiPyAkMaORMrIgL6S2ORbXjGjw6u_GIXZmtdqENF1wAommFYVv-WF3onSnWVZY7Sj4_gZug1u9cBRE2-SznjrrA1RtG6fIiEYVMKAPq1cdn5ecAsLvJaprO-lW1RK6gkL5Qpc80wf-Nj0_I9ElaEJ8hdceiZz_jRSUqSgr_dAbW6Qpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b32ALrWdAFOt6qDYbhUEdwYl7uaI77QAMRY-yTjbp97Pon1yBYvuqM9eDnPDsRYl2pn4dhRBeEU7Bj5FKEQDNP-4Lh0it8Rz_39RQJKI1PL_X0QQCTy6cbOoXuyxVPV1pNSzmO3kvfF1DjGRTx3bPLt3f714po3Av7ErspfP6R0bedZF9bz1tULiGkGb6EbnRNW6248T0kJ4oHw7DxR5qO67ldOpRx2FbWwsKDrDP5luJllt-7iizsG-4wX_yzs7JmZbld5EuPHh4jp1vBzSNqz9E8igPKuyy1AeaaUNsBiDsO21QmBBMLiB4VNP0tPvQVSqChVTQm1a0YWD2qbKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyJX01TEnoIj83RCxYknwm07sVgRXDhPmUyOXVnVsQ-ygu-VoV7g-FlSqDQZJhIg8qKw4bEfJDWKUJNtpEY5oNPXd4_9jFCpR3siig202JRK8vDDN5yKVWoBOt3Yyl1o-70MP1g2AhBPwDOFJOfD75B5XkBBcCmQKVUPHn7s2D_RKzxjMEJcZu8xr9p7P6p0VjNJ6IkQ8QbV8rK8kGCj9Crd-pQp6n5b8vyPatFqKgBc57fHDUPP2DTuGeMYX15CZfedktouxwT9-e1trT4e2gmNbHnuAqi9mTvRx-r8ovlhUsrZkHT2edWpj8FF4UWFDZvCvEcXG7Jr3OLnL2FSBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عراقچی: هدف سوم من انجام هماهنگی‌های لازم برای تشییع پیکر رهبر شهید انقلاب در بغداد، کاظمین، کربلا و نجف است
🔹
با تدبیر و همکاری دولت عراق مقرر شد که تشییع پیکر رهبر شهید انقلاب در این کشور صورت بگیرد و نخست‌وزیر عراق ستادی را برای همین هدف تشکیل داد که…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/664241" target="_blank">📅 13:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664239">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ccs4YOF8XKn2hvD6f482VjbVX-cbp1XnOUjO3RaNu13UB1p7Oxy4r6HLS4D6iuDvGvdJzU9vYQ7EGEnB5kQRx3VowhcH3KAve6aKlyxGMFyzzR7QEqjgWKlDa_3duXVcKOmgVgw2p-ceIjcDRaiYyd1UkR7zgWxgd2a7BoIzzDsZd5xGljGm6qqPUYCjGu_cMYhAmsu40JoWbwQ6h79QvZaFElAn1wd6Z7ZqWoxCHtXCYpH8eCO-saISoLUU9UCfLbyKrB4lrm-k70t-l_nRuuvDtMRTd1FsZLQr1wWFqH3dfJBhc6DxYhsC7g2pTUoAxY9wnkW03GkhN5YRQGJBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oDBawTGRcfUKn8zMYvEic1ltpqqdsTKCclRLzANv_qSLInzEVuJ6R8u_GNTT0eOVXb6DJtRCndx-X3xe99H986cZiFq6O3u1Qg-xfJvV7orsAzVO-csSoSh93IQjmY0IaplFkhCAMJRaS_PYKGwKqPQ_x5r31ZpCMRJTFYvSDU9p-f32j-VsE64BPZwcyNw_QECOIdubVQq8h-ixXrlAKrKeiJ-oNQV_bmyPrsPLb_YOOxboZaQHpUSqOZIXOSnJulmw5GRCwmMCBxy7Nu1rF3OB-11KLy1McmI2RgmjEw28DAvCXJEXRA46zF8LTrJeMqPMKGO0xNawbugmhCFYXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
آپدیت رنکینگ فیفا در پایان دور گروهی جام جهانی؛ ایران در جایگاه ۲۱ جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/664239" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664238">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
رئیس سازمان امور دانشجویان: یارانه غذای دانشجویان از ترم آینده مستقیم به کیف پول آنها واریز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/664238" target="_blank">📅 13:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664236">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85468abdb.mp4?token=cZAgs4JZfYnFXFH_deFbbzV0JK3vzOhNxog6N_pTWKI0jQ5qip_vfTUc1CAw5vpfGEzB8wuBtcCE7F2SgZSJwhJwhxfPqTS1dlegVMB80j3wK-ptBE2NUtXU0R-KLI6OLqnVkcMgYS5Y8LiPZ1pLVdJeK890Pk3lqmx5cX_hlzZMd7PsNR005k4Jzz_vvODNcDANNx9MqtGMFdViCDGPoIbs3-aoLEDNyQ1tNOjfgYJmttmHd32PpXgrKNLNQ5V3iOclPNHh0aUomKjc5rwphpQTulh6KOnmY-eHxaSDlBJl0HPbW3mlW0mB8Knl-ulOXJbAth907Xv4Hy22yCJoFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85468abdb.mp4?token=cZAgs4JZfYnFXFH_deFbbzV0JK3vzOhNxog6N_pTWKI0jQ5qip_vfTUc1CAw5vpfGEzB8wuBtcCE7F2SgZSJwhJwhxfPqTS1dlegVMB80j3wK-ptBE2NUtXU0R-KLI6OLqnVkcMgYS5Y8LiPZ1pLVdJeK890Pk3lqmx5cX_hlzZMd7PsNR005k4Jzz_vvODNcDANNx9MqtGMFdViCDGPoIbs3-aoLEDNyQ1tNOjfgYJmttmHd32PpXgrKNLNQ5V3iOclPNHh0aUomKjc5rwphpQTulh6KOnmY-eHxaSDlBJl0HPbW3mlW0mB8Knl-ulOXJbAth907Xv4Hy22yCJoFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله سنگین اوکراین به پالایشگاه اسلاویانسک روسیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/664236" target="_blank">📅 13:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664235">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d73ee40e.mp4?token=G5QG4tfadgKGv_59aoudBwgkv86ZsR3uInu-_4Z-SZ1jeCqSPiLc_CheNF-R28833mQtAgTdfW0RR_1sS9OzpV80AJSXGREY-8nkdOj_gnCbuQr_0Bvv49J0b8rr6UTWjymVFQMMNbXBWb22680Rz1RZH7suZkkqptQmbb2_ETLpAwxkbbOgN39Yg355SViL6Pag-4d7amDjF9XbTUolZC-Galbq9Dnll7dcG8qNHDvJ5Qd3vLX5IZV98le3pQzHSePmnfjtgr49OVZBy8wNWy8Q9IIiaJrg29je9B0zgSeI2Ra2icqPln3GkbnV9qlGRCdJyqSAnfSgHvKhbutMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d73ee40e.mp4?token=G5QG4tfadgKGv_59aoudBwgkv86ZsR3uInu-_4Z-SZ1jeCqSPiLc_CheNF-R28833mQtAgTdfW0RR_1sS9OzpV80AJSXGREY-8nkdOj_gnCbuQr_0Bvv49J0b8rr6UTWjymVFQMMNbXBWb22680Rz1RZH7suZkkqptQmbb2_ETLpAwxkbbOgN39Yg355SViL6Pag-4d7amDjF9XbTUolZC-Galbq9Dnll7dcG8qNHDvJ5Qd3vLX5IZV98le3pQzHSePmnfjtgr49OVZBy8wNWy8Q9IIiaJrg29je9B0zgSeI2Ra2icqPln3GkbnV9qlGRCdJyqSAnfSgHvKhbutMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
دریاسالار بازنشسته نیروی دریایی: تنش در تنگه هرمز بالا می‌گیرد؛ آمریکا در حال آماده‌سازی برای نمایش قدرت نظامی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/664235" target="_blank">📅 13:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664234">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
تا دقایقی دیگر؛ پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به مناسبت هفته قوّه قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش منتشر خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664234" target="_blank">📅 13:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664233">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
عشق اینستاگرامی، زن جوان را عضو باند زورگیری کرد
🔹
زن جوانی که برای بازدید از یک آپارتمان اجاره‌ای رفته بود، با همدستی چند مرد نقابدار، صاحبخانه را کتک زدند و طلا و اموالش را سرقت کردند.
🔹
متهم پس از دستگیری اعتراف کرد از طریق اینستاگرام با سرکرده باند آشنا شده و در این سرقت فقط نقش «مستأجر» را بازی کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/664233" target="_blank">📅 13:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K36ksvH6KPxTRyWriALOR3nxXLj8qQyGWdOXfYHop5cQhCK4p4nuqMeAM8yU3qbXIe9UyzuWpsGyl62_JZtEOFz6oIfQdeSKQONAf_rd18FUtBEeY6DonefqeahOBMyggBYoUAkizjlG_c2mkYzu0qBg3r4q5wVoniR5rsCn0HciH0p-KMKgZp9drUKpPI7QA5Q23sBWtuFtpB6hS5SUJz4OTUOCC8yRdCG1hTKntXsMSm2fPEMYv8OTcVH7GZjuxsWfTAnmlNxXQBNfBvkMz_TONbUxZqUTwYA3pQ0ewT1KTYxkFgvsZhj2MCqLfhqufx8TIfeUqmbqSEavnOcNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badragheyar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
@Badraghe_yar</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664232" target="_blank">📅 13:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664227">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQjZMS_agWUeqBRCRRqu25GGHzhmGYZrwNZgfLmEhDnpsBg16jcVT-1TRYkLOAZSVd6KhWdbPn29Nz2XXp793fYrs4CM2nYKrLGQyyIxOwbOEtZ7mTscAjQT9KdfW9vCtE2s-kjc_BERhCNx5jVCsyXwq3DPXg3IG3dV47rcuxsxoDQmnpPEG7bmZfy9RlRbdQglCxgSRF0ToihKBQ5TrlicO0fOHPGz1vcDomurfpy3EsxwHG0CYHzzdZZg12YWKZjR1KPbg6Fur2izOVCOnHZUGca0qFwryoZmpK-hse4QCpvHHjbeetZ0ES1O1pen14RkHQ-FHnsR0__dGash8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBYkICgbaoNqTifSxsnJW5RCoxf_OmnUcqEahPhUIMiO-A0WeDAqnnV0r18mTqbgiRsVYS0ZQ1PbY_Q-u9s2dGlmznKhksShouV2Tru34ZlTJz_iQRqObHFeHp3BWMT8uR8fqU459zAu8BBFQqUWQwUTxbpyEkeOIOjbKT7cXGkmCGFKxMQ0W2rrVGU0rTWNiJzPOve4REMk1Scg9zh18SJR3_BgxeRH4N7AA-gutKQ-jd1koLfDO85oFggukZICwaS4fAfs0Dq68AgTLBu7krxyE_R663GCJiwVMqJ93TzP02wtz4Wm4BYoD_zt-mx0hUtr7R7_4ckelZ7gi4OsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yf3shsOaTmJbpz3TteEvFY5EiE8tnHfptMxXjI96Hc5TyuK4Pkrv2IivRAV5WjQeYQkePOaYjA_Z5XaTJ-HQ8QX9RZVgJKiEQxCpqCfb3O41VavxmXgIM7Cs0mb972FhP7SLtKK-qlOw5zy3870EWa1KLnnx6oaSLb2eSt5gX6DyvxbjR4DTPJdP1UQP-YIJb-r1k5VJHX53aYu4hSid53sbzV-uFsMOrnc0AN8t1cwiD1TXcljSeQSBCvGANzhjp6SmiT1eEgY9kJBx3dbGQ3vZbxFqsW3Luk5XNPXbishLiNrmQGHSe5ZuTaaYtxVYEigWuI1vUx6DdSJT57f2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_234DKO04RoGVsdOrD0FOJSC5q5R37hzOj2UcFAfsOoBw1JlTSP9knpeEaoRK2S4osS3dR-sWGWw4FoymP6YVtIklFpWZGIMfIuPybCzjXejqfzmelDwXb4kHxZ5HovlYSsmfwA7tA6y_qV1OMavJ52mvKCwb5__VuJrGRq65uTuQwdVXLai7raZCTCFvai8z_ocYhQmBX9naEAyNGR1Y1MjgowL7QVXO3aLjL_qID2ps4uBSC1YBiBeAi1FAFdeJy0-aAEUsM3mr8thQ-B6h8LjKDX0FUJz5G9oyXBS5Q9sU2uXpMGWwQGSLpvEz-zNEWc-4tj8zB4HhI1WbRIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u81YD50z2C1r3OkwSJw3CV2LRxHGMNBo6E3J17dy5TdGy1dcgFscsuoNWRM1uT-BUb1a0umLQlA-qsJsdGN9XIX5K4z89F5bKFPYk4RJSqDJU28XxUUh8YfBt3x3i6-DMY7-qUbfUc8ncD0skWIQdBj_nu01edA0C6hMwWuad4mAB850Cu1a2RlU6GXNd14l2YoGNKc4kFeNuk5Aiv9MoDeAzRUZFD1GuaGCJeNx7HIkN8YWstXuBjQajXBHhZ8sStCCs10NfzfRdXQJXTTH17nRP2fx2MCMKDtBpaJnRDPk58_lWNyKtvMlOaG4KPbQjqxmLtPgypViQsW2WlDvPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ظهور «بتمن واقعی» در مکزیک؛ مردی نقاب‌دار دزدها را می‌گیرد و به تیر برق می‌بندد!
🔹
«بتمن مکزیک» این روزها حسابی خبرساز شده؛ مردی نقاب‌دار که به گفته رسانه‌های محلی، شب‌ها به شکار سارقان موتورسیکلت می‌رود. برخی از مردم از او به عنوان یک قهرمان واقعی یاد می‌کنند، اما پلیس به دنبال شناسایی و بازداشت اوست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/664227" target="_blank">📅 13:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664224">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db9afcfbb.mp4?token=fCQrH4T9Bdsye9jb4L3x_KQRg5jq1_eZGN0z_65ztUNPo8Z-NgbCkLPNG2PT1Cepi_5Z1Ze4ZvfZkr2_damBVCFp6zeAHyGlSA9XxEgmZO2F__mCOJu5463FSwj4iO_3Usrwl2H3jVvvt5nbqZ579s4qc9KT-PF1EL5xt9bB1sIANVxB1wWvtMiV_0rOroEFeGhn27UAslf3cKbqfzP4NPsRu8ExDcnMmvsaN0AvaMnqz2R9mtx0r1CZzUXrCl2FFfacffI0YHguxyPagBlZPpbeoaSkHyl-J_VOpoqt3wl7zn6l6-ZZTxW2va_xosuApt6g8-JkenqzQHMDw0lSEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db9afcfbb.mp4?token=fCQrH4T9Bdsye9jb4L3x_KQRg5jq1_eZGN0z_65ztUNPo8Z-NgbCkLPNG2PT1Cepi_5Z1Ze4ZvfZkr2_damBVCFp6zeAHyGlSA9XxEgmZO2F__mCOJu5463FSwj4iO_3Usrwl2H3jVvvt5nbqZ579s4qc9KT-PF1EL5xt9bB1sIANVxB1wWvtMiV_0rOroEFeGhn27UAslf3cKbqfzP4NPsRu8ExDcnMmvsaN0AvaMnqz2R9mtx0r1CZzUXrCl2FFfacffI0YHguxyPagBlZPpbeoaSkHyl-J_VOpoqt3wl7zn6l6-ZZTxW2va_xosuApt6g8-JkenqzQHMDw0lSEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی دما به ۴۱.۳ درجه رسید؛ پلیس برلین با خودروهای آب‌پاش به کمک شهروندان آمد
!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/664224" target="_blank">📅 13:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcoSB6eD5KXmk9DDRMmhasd6HU8gS7bn5uS-KxGWhuOzgbotqeWLwGukov8usPAS_dJxO7OexARoGkKETHPXHXVnRvAt6M_EeAwEjJY3AEaMeMQaiNJq72xWa1JoXzg-OwokzdlllraZcFm6dunJa57LwIg1KUw8XBOhzB0uY9uo7uOoev56DMnppZ-kj360-MhgsvhNuzlSFM-GE-Ij3aNqaQ02KM8_StNqlgUDNe2IxhvE712DzhaiM4g-dw8V8Qt92Jo_bEker9hanz8gBZSOKehD3Sdo0ucPFX0mWxX18BHYYWfOvmypYlOjxenPuo4tHfI_Z0rDKOtYaUpfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امروز در دنیای تکنولوژی چه گذشت؟ #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/664222" target="_blank">📅 13:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سخنگوی قوه قضائیه: هر شخصی اقدام به تهدید رئیس‌جمهور کرده باشد، اقدامش مجرمانه است
🔹
رسانه ملی در زمینه تبیین اقدامات دولت در زمان جنگ خوب عمل نکرد.
🔹
ممکن است جنگ به پایان رسیده باشد، اما «شرایط اضطرار» تمام نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/664221" target="_blank">📅 13:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664218">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktCyBj4de8jEYzQd4Kfhx01PRZxklqLZx1DKaeDaQyL6Gya0xgLbhRKXc_xUq2w3iWCtbY2BLA_8u2Iueb_DP77z2gLrW5EnAQTXG20e06s1O6w_m9bErqcxv4AwuPnlC2lFfk_lWm8lX-nrfB-6aI4JBzVVqr7KKE8B8QAsgbEseTEBPWKIdZDgKuds1A5JVnJh3LOMLoqMhhwZ_iwltUmEWDvWmoR2YCyz_Gk5x-nsSCdAHWpL1BuIfP994PICDM62b73JEbFByI0MW12z0rsPMqSf5m7ur9TCu1TAtjHcuA_chc49RvB7Kh5vyO3qq1ybN10_krb5JgDX3YpDVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده بی‌خاموشی، واقعیتِ خاموشی؛ مردم کدام را باور کنند؟
🔹
وزیر نیرو وعده داده بود امسال خاموشی نخواهیم داشت، اما قطع برق در نقاط مختلف کشور روایت دیگری را نشان می‌دهد.
🔹
خاموشی را نمی‌توان انکار کرد؛ مردم هر روز آن را در خانه، محل کار و زندگی خود تجربه می‌کنند.…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/664218" target="_blank">📅 13:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664214">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
عراقچی: هدف اول سفر من تشکر از حمایت‌های دولت و مردم عراق در جنگ تحمیلی علیه ایران است
🔹
دولت عراق مواضع بسیار خوبی در محکومیت تجاوز و حمایت از مردم ایران گرفت. همچنین ما از مردم عراق حمایت‌ها و پشتیبانی‌های بسیار زیاد و دلگرم‌کننده‌ای را دیدیم.
🔹
هدف دوم…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/664214" target="_blank">📅 12:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664213">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fjx9t7XNr5fFCPCiqiuEH_wnCS2Unz72cN-wYk9ix3xAWlpWboJZM3bX1OhyHaia3ei8Krb_LegTqQrTvevPeaV1kEkr1qxH3RPIHi72PCNsxf8d9SyWwjckTbuKenYmhXsO4h4xV_vYoG5AnznIRE4MkgPEmM2goP3suDHJX3hWJeUZCYnQy-BTcbeaWjP_SUeupq8EBJSewBPNYT6Ghs0xvclSYYhKh8-ur7iTmmcs2SbRVcsBeNbrhhohsrxK6LBFOmnM6Zwi1lYqv8kEsRv6f3a-ysFl5NSM2wHz5T_LeDjWcqvVBmXYexmk4XHQFpolKjRzdAVA542hWwd6oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریزش ۲ درصدی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۰۱ هزار واحدی به ۵ میلیون و ۷۶ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/664213" target="_blank">📅 12:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664212">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp2MZ8NI0vsqJC-Za37rCQ0Zl8KycYiedb57WG_gLkUoQgpXFstpwXLMzxVoeNi9T2H2DoEuJ_w9usB3ioUAQa52C6n8DtkcmvXIrtKT19YPaBpxXk5w4Swzx2QEWNBd6txXa_DCnzrde4UAYbRQW8EN84v9rVEuwW54neUNmFPWffepWTx68OiRiLOBkIZ4cPYnZJfNCa737SY7J_ehhW6LkVpkckJFRmpYL135r4imrRG58f39NckoseA2OsjtWtMrXOsERwMrzxV40zcPHmEmc6rPW1wMQPzKQAECkm1JEVJt3JdRrMGfnpSxAFV8ek9Nos9lr7GAsnDOSa4ARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدهای مخفی کاربردی گوشی سامسونگ
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/664212" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664211">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu2gr57LySxucN_wvSXQorAAzh9FSMDd8726bzNZYxSh_VHatggLgUsqRwjnFiqrEl8ob3bJ2obvDzcf5s0BqlVV9wGQFSQFbEQ-bQbf-XqIkL_5gC_IC1WoQenqellIysKnccMNU2zKTuIAmdeAdB3nQ6JwE4VgxIf2smNHry8J-cty25gFcHKnFm9v0FoSxejGUSi-GKCkE8tpPqaEfmAbDhqMSV085BKLXC0wDW_3Cobcy55OHr35h5KKPw9r4Ob4nA3tRwl8BtNXihJgxmE0VBvvpg2Q0TqWuv38qf9siw7j6Zolfb_mOMFTO7x3UtqyyNfFiYdnLUA698Zu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شاهکار نمایندگان آفریقا در جام جهانی ۲۰۲۶؛ از ۱۰ تیم ۹ تیم به دور حذفی رسیدند #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/664211" target="_blank">📅 12:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664210">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuU3ATeXIMiNMJHvezSWXf0bH2VIWz3zw34_y6GyZtl1zgn5sVDcPrA1GwAeBUbAK2cHtk8ktbKeAj2iiDu828DnUyqpod0KjBepmOWQuVC85AR44Kp3D9W_zxsaW8Z16a8dMJhuHevxaXhhoAqpmdufbCXvY0EJwLGr4moXnwfBsObNzgqU9AqbrJqzxJWi7lv3dRFmVTBboC_KlqJLXwN4pROBNW3Hd-DrUlz-fFTH8xQUIbiVOMqMK0YybyAJCqQNWSzvxd6J1iGNzFplzl-QaqQVPPdWE7kG1BFYfvHuhr7FDM3Cg2Lh3CjUPfHZdQXxYiG_j6PqUAgB8Jb6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمول ساخت ترند؛ الگوریتم‌ها، اینفلوئنسرها و رفتار کاربران #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/664210" target="_blank">📅 12:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664208">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
عراقچی: هدف اول سفر من تشکر از حمایت‌های دولت و مردم عراق در جنگ تحمیلی علیه ایران است
🔹
دولت عراق مواضع بسیار خوبی در محکومیت تجاوز و حمایت از مردم ایران گرفت. همچنین ما از مردم عراق حمایت‌ها و پشتیبانی‌های بسیار زیاد و دلگرم‌کننده‌ای را دیدیم.
🔹
هدف دوم…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664208" target="_blank">📅 12:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664207">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e4dd528d.mp4?token=v24bWEcGtgXHxTWHpwsxMhZArys_xcGE3_Q6Zs1z0qpgEekTAx4GuBwzlpB_kEJ6XgzCuGoBwzvYFPznNlWYv-RjkZiwIQqVRxSjNjh-A2DEczk6NFWj70IbKcRc9PU8pMFy-Ghn0I8_ByKueX4_Xm6qkdWfwRjD32MaaPeIjiedoIT1Lbnr37SmY3MSLaiQNehyP7F0KQYltGda7ChkOOkvmMpqGmGU3DWqzOCchO9cDBFCLhlHkDCO4EC9KnKf-_FsbKIRA5cGdjdpr57q2W_gqm4nGcIm3jPUkt5p5Xvt8OUtVGNek8U8YwGfpdLa-FIdXdtjHDriD6EeHXMHDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e4dd528d.mp4?token=v24bWEcGtgXHxTWHpwsxMhZArys_xcGE3_Q6Zs1z0qpgEekTAx4GuBwzlpB_kEJ6XgzCuGoBwzvYFPznNlWYv-RjkZiwIQqVRxSjNjh-A2DEczk6NFWj70IbKcRc9PU8pMFy-Ghn0I8_ByKueX4_Xm6qkdWfwRjD32MaaPeIjiedoIT1Lbnr37SmY3MSLaiQNehyP7F0KQYltGda7ChkOOkvmMpqGmGU3DWqzOCchO9cDBFCLhlHkDCO4EC9KnKf-_FsbKIRA5cGdjdpr57q2W_gqm4nGcIm3jPUkt5p5Xvt8OUtVGNek8U8YwGfpdLa-FIdXdtjHDriD6EeHXMHDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: هدف اول سفر من تشکر از حمایت‌های دولت و مردم عراق در جنگ تحمیلی علیه ایران است
🔹
دولت عراق مواضع بسیار خوبی در محکومیت تجاوز و حمایت از مردم ایران گرفت. همچنین ما از مردم عراق حمایت‌ها و پشتیبانی‌های بسیار زیاد و دلگرم‌کننده‌ای را دیدیم.
🔹
هدف دوم سفر من تبریک به دولت جدید عراق است و امروز پیام تبریک رئیس‌جمهور و رهبر انقلاب را به نخست‌وزیر جدید عراق می‌رسانم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664207" target="_blank">📅 12:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664206">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران؛ پشتیبان حقوقی کسب‌وکارها در شرایط بحران
🔺
شرایط جنگی اجرای تعهدات قراردادی برخی بنگاه‌ها را با مشکل مواجه می‌کند. اتاق تهران با ارائه مشاوره حقوقی، فعالان اقتصادی را برای استفاده از ظرفیت‌های قانونی مانند معافیت از خسارت، فسخ یا تعدیل قرارداد و... همراهی می‌کند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲ (۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664206" target="_blank">📅 12:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664205">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
وعده بی‌خاموشی، واقعیتِ خاموشی؛ مردم کدام را باور کنند؟
🔹
وزیر نیرو وعده داده بود امسال خاموشی نخواهیم داشت، اما قطع برق در نقاط مختلف کشور روایت دیگری را نشان می‌دهد.
🔹
خاموشی را نمی‌توان انکار کرد؛ مردم هر روز آن را در خانه، محل کار و زندگی خود تجربه می‌کنند.
🔹
اگر شرایط تغییر کرده، انتظار مردم شفافیت، پاسخگویی و ارائه راهکار است؛ نه انکار واقعیتی که همه با آن روبه‌رو هستند.
#برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/664205" target="_blank">📅 12:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664203">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdTfExp62WapmMVyAyX0dHnjtN_EJxRoZR_Ofm4uWDnWb_DzR03u75mwk0PrMnsSaSz8QNWS_6XynPfvSQvL-CbR1ww42dqAi739347YbsBTEqmY-5pvpyKTCmigplnOO6k3LwmODWuRTxSi1u0cNNYaG7P3OodAICHqIb9xMEkUAWjqCe9qhn7Ir7BoNjTWFUnEYVfjgs0FfgOwl33I2_uXr6z_8XgCbXVlTNnonlnA9B3mwQFn0xvH2nMapH7S6n2TTyleon7wCAS1XJ79zSB1VkTDe-ssLd7oMLVrC_wS4GcjGiZtI_P37NXGi4NIr85LvSQ0-k9o3PgvhrbzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSGuZhnzV1VuONUHAXxuNH39h84lOmgTIXUeTz6vwqNqMLnoPHr4LSZkZsqLEB6ImkdzcYy19ndGF44pzrcnJSTuXrP5cKxVc0T0G75h7AxYdgYYUy9xSdwfr6bYSxXSYauCyfuMd_T6hd4UI7YMYgP0rN7LCRmYUcpm2gPElQSHbwngz5MBZccAfipDLuAG77I5OzvVALrpAKJSqcN-vmNQU0Zie_-EcSKBApYAeMsw4Mf2if5uOKzpfdIw4EdCGWwHbdJtZPlE79J28rJA0gb1z5YS8vfG14DN42uSB8VfAKWO7S872mRKJAzq7IgnEJp2zgS7Z2qNSjOiJeZPbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پست اینستاگرام اکانت رسمی تیم ملی مصر با کنایه به شجاع خلیل‌زاده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/664203" target="_blank">📅 12:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664202">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRVMnPhrhdCJHmk9dC-PzxM8YJI52Mdw_CoOIDCtli0J6uO434wtCzDT1FSNOFvyzFiEgWgvw3hNEmy-xICDcdGfEJ2lZPy06zOOJAkJIQN7nJPqRdkLT8JNl9SQL9anaDYzjI64I_VvFDkYn94cbQKOS5Pzn9iyRfontYib8vaN9OzeZRu7qJ-MgLbB2t9shWEF1ytI8pHBIzOW8ZpvLuXndHQcFLh4Q4T3Vx_K5G-kX7xRb0KjJtArCLjU3QXAfz_wRRgO-fzdaQ8tOQyTXO9_qyOwODzD5OgLhE_tRvCfwX5sDychOgKoZGhW_Xpqe7v-pmqebzqWLMX84gGoEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت میوه و تره‌بار ۷ تیر ۱۴۰۵
🔹
قیمت انواع میوه و تره‌بار در میادین شهرداری تهران امروز نسبت به روز گذشته با تغییرات کمی همراه شد./ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/664202" target="_blank">📅 12:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664201">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca37845d3.mp4?token=lZTQWk02MgmkywD5P9Jd-upYaoDO0GTQIdAtOqBhzXcBh14FYNR5YYhgyAeEDTrk-8_d59Q1XVciLQZ3F7fL-i6grkBKy-_j-Auq033XKeK3KdfNwWaso5tWx5TEw5siN_ldUcaTcGmrLdNl-G_FiHiYNvb-P-rSkguumG-WhO8bEM4sfBKigSrppJPCPQpipTxhWbgrpbuu3HdrzPr8yrT2mMhZ0oQ8A6LoPCUOszQLxvPxk1itin1LQk2sZU7IEIXlrAeHjfcu-Ix7znxx6dK5qkJO11qM01gwx6gxjzKm4UKFXTLZjLD0UxjTNluic9zViLr42k1uzyl1E6nYgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca37845d3.mp4?token=lZTQWk02MgmkywD5P9Jd-upYaoDO0GTQIdAtOqBhzXcBh14FYNR5YYhgyAeEDTrk-8_d59Q1XVciLQZ3F7fL-i6grkBKy-_j-Auq033XKeK3KdfNwWaso5tWx5TEw5siN_ldUcaTcGmrLdNl-G_FiHiYNvb-P-rSkguumG-WhO8bEM4sfBKigSrppJPCPQpipTxhWbgrpbuu3HdrzPr8yrT2mMhZ0oQ8A6LoPCUOszQLxvPxk1itin1LQk2sZU7IEIXlrAeHjfcu-Ix7znxx6dK5qkJO11qM01gwx6gxjzKm4UKFXTLZjLD0UxjTNluic9zViLr42k1uzyl1E6nYgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الجزایر دقیقه ۹۴ گل زد و مجری‌های صداوسیما پریدن بغل هم و گفتن صعود ایران قطعی شد، شنبه باید با سوئیس بازی کنیم، ۲ دقیقه بعد اتریش گل مساوی رو زد و باعث شد با این نتیجه، تیم ملی حذف بشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664201" target="_blank">📅 12:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664200">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حذف بدون شکست؛ افتخار یا زنگ خطر؟
🔹
بعضی حذف‌ها، از هر شکستی تلخ‌ترند...
ایران بدون حتی یک باخت از جام جهانی کنار رفت؛ انگار فوتبال این بار بی‌رحمانه‌ترین روی خودش را نشان داد. نبازی... اما چمدانت را ببندی و به خانه برگردی.
🔹
این یعنی حسرت؛ یعنی همان «کاش»هایی که تا سال‌ها دست از سر فوتبال ایران برنمی‌دارند.
همین ابتدا بگوییم، لطفاً نقد را با بی‌وطنی اشتباه نگیریم!
🔹
ایرانی وطن‌پرست بیشتر از هر کسی دوست دارد نام ایران بدرخشد. بیشتر از هر کسی آرزو داشتیم پرچم سه‌رنگ کشورمان در ورزشگاه‌های آمریکا تا روزهای آخر جام جهانی به اهتزاز دربیاید.
بله؛ از جام جهانی حدف شدیم اما بزرگ‌ترین خطر حذف از جام جهانی نیست... بزرگ‌ترین خطر این است که حذف را موفقیت جلوه بدهیم.
🔹
اینکه ضعف‌ها را پشت واژه‌هایی مثل «بدشانسی»، «بی‌عدالتی» یا «اگر و اما»و «سرناسازگاری خدا»  پنهان کنیم.
درست است، مقابل بلژیک نمایش خوبی داشتیم. برابر مصر، لحظاتی فوتبال چشم‌نواز بازی کردیم. بدون بازی‌های تدارکاتی مناسب به جام جهانی رسیدیم و در آمریکا، دور از خانه و زیر فشارهایی فراتر از فوتبال جنگیدیم.
همه این‌ها درست... اما حقیقت‌های دیگری هم وجود دارد.
🔹
فراموش نکنیم از همان روز قرعه‌کشی، بسیاری از ما لبخند زدیم. گروهی که روی کاغذ از چیزی که خود امیر قلعه‌نویی پیش‌بینی می‌کرد، آسان‌تر بود. بلژیک، دیگر آن قدرت ترسناک سال‌های گذشته نبود؛ تیمی پا به سن گذاشته و دور از دوران طلایی‌اش. مصر هم آن ابهت همیشگی را نداشت و محمد صلاح، بدترین فصل سال‌های اخیرش را پشت سر گذاشته بود.
می‌گوییم بازی تدارکاتی نداشتیم؛ درست. اما چند تیم حاضر در جام، به اندازه ایران سال‌ها با همین ترکیب کنار هم بازی کرده بودند؟ بیش از هفتاد درصد این تیم، سال‌هاست ‌هم‌بازی بوده‌اند، یعنی دومین تیم جام از این حیث.
سرمایه‌ای که خیلی از تیم‌های بزرگ دنیا هم از آن محروم بودند.
🔹
اگر درخشش در برخی دقایق بازی‌های جام‌جهانی را در بوق و کرنا کنیم یعنی پذیرفته‌ایم که دیگر نیازی به تغییر نداریم.
حقیقت این است که تیم ملی ایران فقط در شناسنامه پیر نشده است؛ در تفکر، در تصمیم‌گیری و در برنامه‌ریزی هم به یک پوست‌اندازی بزرگ نیاز دارد.
🔹
این تغییر از تعویض یکی دو بازیکن آغاز نمی‌شود؛ از فدراسیون شروع می‌شود، به نیمکت می‌رسد و در نهایت به زمین مسابقه ختم می‌شود.
فوتبال، بی‌رحم‌تر از آن است که با خاطرات زندگی کند.
اگر امروز شجاعت روبه‌رو شدن با حقیقت را نداشته باشیم، فردا دوباره همین داستان تکرار می‌شود.
شاید باز هم بدون شکست، اما باز هم بدون افتخارِ ماندن./خبرفوری
#سرمقاله
@TV_Fori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/664200" target="_blank">📅 12:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664199">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f6df3668.mp4?token=DMo-ArFWTEZkcuPr9WTOnbB7RZ05Ob0Byh0DwUTAXLMTQZMYRkj1ERQFJP8y6HRy37tQBXSJCVy_qIyVDJfJs-F4iMm0cltNj093-eVCt80HluYqZjm4hexrdRuG3y7lAqARQCZrgsg11yjWkk8u-wSsPxsRhtZxBv3lsP_upo-KLB4pDkA5jmh0lnbI_VJtpmfq4dTsxvoVNKO3xKi0J2mE0meJ3wwOZhGCWRzc9sl6h-piVRdWmeVnklVvZMMRJlQGcMe41FP9laOMtUjND6c_BOZqjZkD7wffMl_V1ZHtS40KhR8CgKZu7ECn2c0hAwnMSUnZVjoYpqcT5AXFUW6GYJo0rMjmZDGYQD9pHCy-fkbYsbEyDRgPeRrPN8JeMVNPtIDbP6cpe_xxlslJZJS-lX-pgJZiyp7hYgYLfNtSjiLItRzbaZQPM4B3vBVGZ6N_V0jWgfrd7FP48v35pQ_Ny8SmM7NdYRmq91zhKFUg8ymmFD_xBAYMjqClfcmAYZ_cti4xflrH5S0Yx0peD7AeuRcu_fiU1azQnbS-O9Y5sdNHO-nxVJ11-bWQMy8SgSfAtZw2SagBHrsxZuMUS4cQn7HGK_h4e2ShOczfSq3B0SNNajnylWTiXXX-ILEspPibsktpe-5SZ8kKS7gIPPuCteikFuzpBis___ck5Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f6df3668.mp4?token=DMo-ArFWTEZkcuPr9WTOnbB7RZ05Ob0Byh0DwUTAXLMTQZMYRkj1ERQFJP8y6HRy37tQBXSJCVy_qIyVDJfJs-F4iMm0cltNj093-eVCt80HluYqZjm4hexrdRuG3y7lAqARQCZrgsg11yjWkk8u-wSsPxsRhtZxBv3lsP_upo-KLB4pDkA5jmh0lnbI_VJtpmfq4dTsxvoVNKO3xKi0J2mE0meJ3wwOZhGCWRzc9sl6h-piVRdWmeVnklVvZMMRJlQGcMe41FP9laOMtUjND6c_BOZqjZkD7wffMl_V1ZHtS40KhR8CgKZu7ECn2c0hAwnMSUnZVjoYpqcT5AXFUW6GYJo0rMjmZDGYQD9pHCy-fkbYsbEyDRgPeRrPN8JeMVNPtIDbP6cpe_xxlslJZJS-lX-pgJZiyp7hYgYLfNtSjiLItRzbaZQPM4B3vBVGZ6N_V0jWgfrd7FP48v35pQ_Ny8SmM7NdYRmq91zhKFUg8ymmFD_xBAYMjqClfcmAYZ_cti4xflrH5S0Yx0peD7AeuRcu_fiU1azQnbS-O9Y5sdNHO-nxVJ11-bWQMy8SgSfAtZw2SagBHrsxZuMUS4cQn7HGK_h4e2ShOczfSq3B0SNNajnylWTiXXX-ILEspPibsktpe-5SZ8kKS7gIPPuCteikFuzpBis___ck5Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مداحی جنجالی که این روزها در فضای مجازی پربازدید شده است:
تاریخ دوباره هشدار می‌دهد؛ «مالک»ها کنار «علی» بمانند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664199" target="_blank">📅 12:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664198">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bded40b15.mp4?token=LgU-F1WbUuPlc-N3_K18BqBuExZc7u9VIJD9At4ORLDJUbRFZm_UPSJ1oN7n0iqlO2zWBDTFeaGjAsG4qecm02KMKihRE2MWe5PguErRPNnEjff69klYvWCNl9iG8sB4hRfIRPdJZLaXIk_iWtyd1XXajpmiu9xQrXTx6CHf-ACG24vQRgY79AViSwdrIbjvd1fvD6qXuMOevTT1jQfRTCnlRKzjavW2B5s9H5KzyQsXp-huUqMBvtgpM17lDCizC_3OSLY86Z1hqZ50o0_wIcq4mEokvn74gNPy98X9cBYSQ24fYgjPSnoq5M21WNY3pOvzUiYJHvcnbgEqandYAmdNTJ6heZp7TdnZZkwPZLsX_Nk3NCWOaC1P109qRTztOwQz27QxBJuyKH_Nq2wFaJY3I8ungkPTl-IwVjj__jQbDxrrqSVgZSuiVbWNNFJJeUOiLukECDoue_GLe9wvi-hoenTifFZeOHxRQDND14Vg0tkD9ttHjxQRxJ_rj-unRrjjXODn7bDf6VeQL_T6qipu4hB_T7T2GYKb2AvUzOyrf1VGy8I6UDo4uJ4rSqVfqGsCzVmV6zaZMs2uFeOU7D-17Co9-YQJP5N5LuQxopOsrVXOKGIENAlzOH5zbWzPWK-2S9AsfhXlI-Ql_XMm-FlroxVyeCr54Y6_q7SC45c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bded40b15.mp4?token=LgU-F1WbUuPlc-N3_K18BqBuExZc7u9VIJD9At4ORLDJUbRFZm_UPSJ1oN7n0iqlO2zWBDTFeaGjAsG4qecm02KMKihRE2MWe5PguErRPNnEjff69klYvWCNl9iG8sB4hRfIRPdJZLaXIk_iWtyd1XXajpmiu9xQrXTx6CHf-ACG24vQRgY79AViSwdrIbjvd1fvD6qXuMOevTT1jQfRTCnlRKzjavW2B5s9H5KzyQsXp-huUqMBvtgpM17lDCizC_3OSLY86Z1hqZ50o0_wIcq4mEokvn74gNPy98X9cBYSQ24fYgjPSnoq5M21WNY3pOvzUiYJHvcnbgEqandYAmdNTJ6heZp7TdnZZkwPZLsX_Nk3NCWOaC1P109qRTztOwQz27QxBJuyKH_Nq2wFaJY3I8ungkPTl-IwVjj__jQbDxrrqSVgZSuiVbWNNFJJeUOiLukECDoue_GLe9wvi-hoenTifFZeOHxRQDND14Vg0tkD9ttHjxQRxJ_rj-unRrjjXODn7bDf6VeQL_T6qipu4hB_T7T2GYKb2AvUzOyrf1VGy8I6UDo4uJ4rSqVfqGsCzVmV6zaZMs2uFeOU7D-17Co9-YQJP5N5LuQxopOsrVXOKGIENAlzOH5zbWzPWK-2S9AsfhXlI-Ql_XMm-FlroxVyeCr54Y6_q7SC45c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سالروز بمباران شیمیایی سردشت؛ زخمی‌که جهان ندید
🔹
۳۹ سال پیش در چنین روزی، رژیم بعث عراق با استفاده از انواع سلاح‌های شیمیایی، مناطقی از سردشت در آذربایجان‌غربی را بمباران کرد و یکی از غم‌بارترین و تاریک‌ترین صفحات تاریخ معاصر را رقم زد.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/664198" target="_blank">📅 11:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664196">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f3b4d6dbc.mp4?token=s6Kyjln-KLGUJmoQS1jyqI-pBkFRGxbDCTaOnoMR8oqiLMovur3cdRxCiPOyxeJgneFnm4RriZ8upmbyd0ypYX1WG_6zmFzNHvKZNvm6p9qdINTtfitdzIF3RotXkIDrrHTyV4SwQotg7QegZOE2DCXeKfFO-AKuO-1893zduuwaQ4MuRizHza5zyBe01JdeQFrRpA7gu-1n8MmILr52a9jX1ZNjMLcUPafOZd1cZNzNTxEJjYMvGc0al-iJgiu0bYi070tsWUoYPkjuL1EKXARpXI-SSWjXyX0KUyVVpm1hDofz1tJrEYwgW8xZF2AbqUCubLHiQ3tAfjz1sm3rpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f3b4d6dbc.mp4?token=s6Kyjln-KLGUJmoQS1jyqI-pBkFRGxbDCTaOnoMR8oqiLMovur3cdRxCiPOyxeJgneFnm4RriZ8upmbyd0ypYX1WG_6zmFzNHvKZNvm6p9qdINTtfitdzIF3RotXkIDrrHTyV4SwQotg7QegZOE2DCXeKfFO-AKuO-1893zduuwaQ4MuRizHza5zyBe01JdeQFrRpA7gu-1n8MmILr52a9jX1ZNjMLcUPafOZd1cZNzNTxEJjYMvGc0al-iJgiu0bYi070tsWUoYPkjuL1EKXARpXI-SSWjXyX0KUyVVpm1hDofz1tJrEYwgW8xZF2AbqUCubLHiQ3tAfjz1sm3rpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظهٔ شلیک موشک‌های سپاه در پاسخ به تجاوزهای آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/664196" target="_blank">📅 11:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664195">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksBKGR6gIErl-MmXrw2KN7lLsdX1nJ73UtfA_kvVf82vGm6z0OAN3mfGcZxQfqxO5n3GcEzdQNRRidOKmdlRDTvElfvRAxoqV3nsyveANdsf2XgEhqNDWC31iSKjLeJxBjkHtVTnF7PYIfme1k0keCXfDcqGZYpypGm0fb1AgoqmIx8PfCPehjF78vYvy_i7sgvXBcKuRk1y-m6qzHWn8XYpUxTSF0oNO58MS9qPTE8eXM-9wFDardjERPleeYv28b3p_CpocH68ZwKW2iF0c1ufc98Yh-HxA5f3i7KtCsl5_9XuGnkpNywM2HL9exL-CDAgd0AXMjnTHAWLZjivgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژاپن در عملکردی خیره کننده، از ۷ بازی لیگ ملت‌ها ۷ برد به دست آورده
🔹
ایران هم بین ۱۸ تیم ۱۶امه و امروز ساعت ۱۵ با کوبای رده ۱۸امی بازی داره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/664195" target="_blank">📅 11:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664194">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWcM1YdkNNxkR9Rq9xDWnstq_WdpYmoXHoTJ5QLjSVx1_Bjn8Iq6668_cjtbw7Bf9PJBP6WztKBEt2BemIH5oZ8rMY0xZSdAkDht2bIqjTXhqfT7hZxDsbI9-8rh4K_tGTI8JnonE5X3zcuKqppF_6D0rfxtcJry8CzDcrVRSZvZI6fXwr70nAbrCtqNBcxBuv-urAIcizxxXFl1HEdLg9ji2PX0yYVKomMCyQ4WTgeSg9ZIRI8somR3rU833k2yzWBIn8n7oxuJrj7J05uhJtiZnUHYXGyBMyTqo2glxUBc6d7OcMu_cTByJGCHQFq2N5T4sEpCzep5inNVm_Q25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جام جهانی امسال جام‌ جهانی بچه‌هاست
عالین
😍
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/664194" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664193">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ایران در عین بدشانسی حذف شد @AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/664193" target="_blank">📅 11:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664192">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df43f4a96.mp4?token=GmMIqKVsqrbEGi660yHPcP_-b85exfBOVYS25VQQV6g4GAcv0n9pTGAk-1nRO9kw62SlAn24U87o81p-ptWzK05ZhoMa-_2Avi38aCpdOfxl1OeLzTh6dsJcF3IUkrAo8N3IusF0FSZvs5uR66hVNyTWoxOg3H_9HtWUisaf8vUWAKV3kaWgsDABXyHN0UjqqSRxuwqjrNT-3-H9Dzj_JfLXjuWm6tZJhWHxkcHUyZamD33uwweElRFomBovh89bvfGytW1hQmqlLccTGczyWueB7bkr56KtNXcKjacU941TwSSv4nYWr0TVBH8cEh05WhmRDK5_uH1DCJ4UxB03R2cIfnBACW0rnCmlNoYrklvdxH6OId-eP2rD6SdKbtG8cvOHr5jtcjygLWXuNi3AZtbhaF_t5rvnvPBxRyotLRGcOu-7K8pdE88H7OouvI1M550DcEJ8I_-1os-DxQOU6Ec4Bh8qVtDv4i2jbryuFPMDbrrtJmRKeMibOFgWJRm-UcV6hx22q8L8CX0ILERvuyjuNJTo4ddWPgpbdVymARlrM3PFsXXB4mLZ4pFSxVGgHUYAgqsfp-b6WMXTUDi-U8xxV-BhljPT_jGH1UhLdXfKLi7TfnYvd_iFXXIYJZlTXDfYhpZM5Fx3kT5NVgEjw4yfr5tidA9pm2lAqc7Jg2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df43f4a96.mp4?token=GmMIqKVsqrbEGi660yHPcP_-b85exfBOVYS25VQQV6g4GAcv0n9pTGAk-1nRO9kw62SlAn24U87o81p-ptWzK05ZhoMa-_2Avi38aCpdOfxl1OeLzTh6dsJcF3IUkrAo8N3IusF0FSZvs5uR66hVNyTWoxOg3H_9HtWUisaf8vUWAKV3kaWgsDABXyHN0UjqqSRxuwqjrNT-3-H9Dzj_JfLXjuWm6tZJhWHxkcHUyZamD33uwweElRFomBovh89bvfGytW1hQmqlLccTGczyWueB7bkr56KtNXcKjacU941TwSSv4nYWr0TVBH8cEh05WhmRDK5_uH1DCJ4UxB03R2cIfnBACW0rnCmlNoYrklvdxH6OId-eP2rD6SdKbtG8cvOHr5jtcjygLWXuNi3AZtbhaF_t5rvnvPBxRyotLRGcOu-7K8pdE88H7OouvI1M550DcEJ8I_-1os-DxQOU6Ec4Bh8qVtDv4i2jbryuFPMDbrrtJmRKeMibOFgWJRm-UcV6hx22q8L8CX0ILERvuyjuNJTo4ddWPgpbdVymARlrM3PFsXXB4mLZ4pFSxVGgHUYAgqsfp-b6WMXTUDi-U8xxV-BhljPT_jGH1UhLdXfKLi7TfnYvd_iFXXIYJZlTXDfYhpZM5Fx3kT5NVgEjw4yfr5tidA9pm2lAqc7Jg2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ویدیو را نمی‌توانید تا آخر ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664192" target="_blank">📅 11:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664191">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb6ba14bc.mp4?token=PTWmtBuTfY3nkD3OEHlBUUQYqrhmzKjixWeXFf0DqvMYRs6wE-Q8CJtyceVePOgzmtc8hLK4_mLAnFCCyjWyR2-edKkcitYuhrQCQ9K6al4gJb2C0qdPkIOSivq_ljwYQkA-xrk4sYjGzo9RXQzJyoK04MbXqHTLz6OYyi7CWUje23w_y9Jo7F7SiGExb0j0bfKsxLPTdqAcAWuFiOk9AN3iDjHz6umCrGIk5DM5zrRFby7m_SNlVew-uBi2UdgAgrA1qmmeQCV3Yk3ipAHhEPb9lRNi8z2dGaj91HPZ0VU-Lllxgm3uPyAH9ZdYFiN89-TivnAtBa2VWo07uAD6D0wx1rSKGS2kx-oZUB6Lw_k5ERWmZT6MkXziuGTWDsasF_ImCelTHgpWw4RYEKnN4wJf-JKLOam7PsfePauHvAo37vi7mwDZS2xVFfdQ3QYWBLJoYru_SWhHHDtc_nYJvS0YeOLuvpgje3eatGa2nV-8jiYs9YqYzFfyLulccHsBX6aeW9mCVANryA61Nh4VufUVEuTWGPPlLFWthdWNAzgeRTAILtYofm0RKUKOTW5Y1BvDgEnBxOAzvJAGbdfIWqKtIWehpzOJtTj9vl2UEprW4cCnZ5SHTcs80g8IgPQyAJFTClmYz7d7w_PxW81vno6xQZ7UinJ6GyfecM_29a0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb6ba14bc.mp4?token=PTWmtBuTfY3nkD3OEHlBUUQYqrhmzKjixWeXFf0DqvMYRs6wE-Q8CJtyceVePOgzmtc8hLK4_mLAnFCCyjWyR2-edKkcitYuhrQCQ9K6al4gJb2C0qdPkIOSivq_ljwYQkA-xrk4sYjGzo9RXQzJyoK04MbXqHTLz6OYyi7CWUje23w_y9Jo7F7SiGExb0j0bfKsxLPTdqAcAWuFiOk9AN3iDjHz6umCrGIk5DM5zrRFby7m_SNlVew-uBi2UdgAgrA1qmmeQCV3Yk3ipAHhEPb9lRNi8z2dGaj91HPZ0VU-Lllxgm3uPyAH9ZdYFiN89-TivnAtBa2VWo07uAD6D0wx1rSKGS2kx-oZUB6Lw_k5ERWmZT6MkXziuGTWDsasF_ImCelTHgpWw4RYEKnN4wJf-JKLOam7PsfePauHvAo37vi7mwDZS2xVFfdQ3QYWBLJoYru_SWhHHDtc_nYJvS0YeOLuvpgje3eatGa2nV-8jiYs9YqYzFfyLulccHsBX6aeW9mCVANryA61Nh4VufUVEuTWGPPlLFWthdWNAzgeRTAILtYofm0RKUKOTW5Y1BvDgEnBxOAzvJAGbdfIWqKtIWehpzOJtTj9vl2UEprW4cCnZ5SHTcs80g8IgPQyAJFTClmYz7d7w_PxW81vno6xQZ7UinJ6GyfecM_29a0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاشته دیدنی؛ گل سوم آرژانتین توسط مسی
🇯🇴
1️⃣
🏆
3️⃣
🇦🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/664191" target="_blank">📅 11:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664190">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8aff6ae05.mp4?token=FcwXs5D0MpOl-mYlE5vpMmwBUq_9jK_5vPWEXofZqPS1nafNrvF8xajkiO6R61q1rptlWtRftOI8phoxe3wRRebP1RhsbnksdR45C3EcjmFzqbYRCOvGaMGCCpuD02nfZfl7DbLoB3sPoL7JbWrHeIeVMCrBFj48t6by0Vsxn25sApuQrVRjNh3PZ53vcv1cKl19eWaLCAuy-UI5rJ8iWA0Pnrs3e3wMlnS_ozRz8E57J3oOdZJn0HHqgrRxFGM_3zjz6Hz5_hnjF1t8gMaLa4Jzo08qJQXeWT-xbpFohdmRSrd8vE3dI7Y1-zaBfgVm7c4EdpaegCWZK78oJsaduj1HcaP2ivgvYMr1byrzz-XU2k2xJbGpP4n5zDLpoZxagAq5xJS5Q_qx9mIMcdKATHUkkEGbO7hxQyH99UHeFD45iStHew1J5KmX_2UdC0_s7vZ-WyBAUpEQEoUoVfNywedlicaRT3GaddSoDuZrG5-acINv12eP8s-uDhY10sX1fVizm8Nd2MAQVxsZv9UijCMqNO9DeuFNv9IFJv4yAAsHMZmGSlkGvRKSuuVm4oCHGuILSVR5wO59yHYeriUNTic7n589_8JAKvNG1LKZxTwTo-dbCeWsi9chZtNuDxdIDF7mv511YwpJVo_Cdz3hyR3ZZ83vFWFLbaiNIJkksCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8aff6ae05.mp4?token=FcwXs5D0MpOl-mYlE5vpMmwBUq_9jK_5vPWEXofZqPS1nafNrvF8xajkiO6R61q1rptlWtRftOI8phoxe3wRRebP1RhsbnksdR45C3EcjmFzqbYRCOvGaMGCCpuD02nfZfl7DbLoB3sPoL7JbWrHeIeVMCrBFj48t6by0Vsxn25sApuQrVRjNh3PZ53vcv1cKl19eWaLCAuy-UI5rJ8iWA0Pnrs3e3wMlnS_ozRz8E57J3oOdZJn0HHqgrRxFGM_3zjz6Hz5_hnjF1t8gMaLa4Jzo08qJQXeWT-xbpFohdmRSrd8vE3dI7Y1-zaBfgVm7c4EdpaegCWZK78oJsaduj1HcaP2ivgvYMr1byrzz-XU2k2xJbGpP4n5zDLpoZxagAq5xJS5Q_qx9mIMcdKATHUkkEGbO7hxQyH99UHeFD45iStHew1J5KmX_2UdC0_s7vZ-WyBAUpEQEoUoVfNywedlicaRT3GaddSoDuZrG5-acINv12eP8s-uDhY10sX1fVizm8Nd2MAQVxsZv9UijCMqNO9DeuFNv9IFJv4yAAsHMZmGSlkGvRKSuuVm4oCHGuILSVR5wO59yHYeriUNTic7n589_8JAKvNG1LKZxTwTo-dbCeWsi9chZtNuDxdIDF7mv511YwpJVo_Cdz3hyR3ZZ83vFWFLbaiNIJkksCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرمای شدید در فرانسه باعث بیهوشی راننده اتوبوس و تصادف شد
😳
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/664190" target="_blank">📅 11:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664189">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678ead5773.mp4?token=S1E833sq3MsagKZFgMEEb7Lh4W-2VBDPMucxF4UPLfoSP7W25XYzxM_rwQEWJtAT9M7QxOU-PMkFXmBTaqV30tvWw6S-kCEE2TpF4BCedPQfMJ9HjbXr0iqI2YB-aVQGJ8Mx-4NYVpQIO0L5Znnoi_4s4Z2p3bxGhIEkPfIAjuO24GTevRGiP3JuBrK9hE3S5oh39K1wl7CvQhWkCLxoCoDzQ37DfzArvYAp5Qm3SvmX3diThlOhyY6G7hP5Z8tFFI7A1k68kmxE2PblYML8ielfQtWxASC8dPAnl9E2SoFjRFSoSNV5TVFxazzdWgJ6XBtDMsFuiurhjOSmmOXVJAwUkjALn5nW-VW-xJDCGbhdrPlr5v-sAPd8VPXROtZrSCbm2kM9WlSuptoBWrSuIFJne3Wm-CwyrLPgoVC7OSGNc3c5uazOPkwUworBuzj_hmCU-rRVx6j603pKwVIjGFKNwRFUrnOIyr6e9UDXe1hdsy4tLmPNZ6LIMbr967PhUOyUeuprNb5U2DF9JCf1p0hIhCauPlq4L1JdCpPsz2VSUfOSuch0KdUPrhKytJzS0lilwQ1M8MQvizEMA2eoD62_XNUPQreplBMJ-6M9QUojchU0sggOCtpOqCvaCrUb-FrTHiuKK4FYrMi87psL2GXaIWRNo_iitml03tGYVM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678ead5773.mp4?token=S1E833sq3MsagKZFgMEEb7Lh4W-2VBDPMucxF4UPLfoSP7W25XYzxM_rwQEWJtAT9M7QxOU-PMkFXmBTaqV30tvWw6S-kCEE2TpF4BCedPQfMJ9HjbXr0iqI2YB-aVQGJ8Mx-4NYVpQIO0L5Znnoi_4s4Z2p3bxGhIEkPfIAjuO24GTevRGiP3JuBrK9hE3S5oh39K1wl7CvQhWkCLxoCoDzQ37DfzArvYAp5Qm3SvmX3diThlOhyY6G7hP5Z8tFFI7A1k68kmxE2PblYML8ielfQtWxASC8dPAnl9E2SoFjRFSoSNV5TVFxazzdWgJ6XBtDMsFuiurhjOSmmOXVJAwUkjALn5nW-VW-xJDCGbhdrPlr5v-sAPd8VPXROtZrSCbm2kM9WlSuptoBWrSuIFJne3Wm-CwyrLPgoVC7OSGNc3c5uazOPkwUworBuzj_hmCU-rRVx6j603pKwVIjGFKNwRFUrnOIyr6e9UDXe1hdsy4tLmPNZ6LIMbr967PhUOyUeuprNb5U2DF9JCf1p0hIhCauPlq4L1JdCpPsz2VSUfOSuch0KdUPrhKytJzS0lilwQ1M8MQvizEMA2eoD62_XNUPQreplBMJ-6M9QUojchU0sggOCtpOqCvaCrUb-FrTHiuKK4FYrMi87psL2GXaIWRNo_iitml03tGYVM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اردن به آرژانتین توسط التعمری
🇯🇴
1️⃣
🏆
2️⃣
🇦🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/664189" target="_blank">📅 11:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664188">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06088a319d.mp4?token=qcE0xJG3gCUiJmfUqMzwdy8wOvxdqDl2W7p1mzLGGGAkJEy3yj9A7UVd2N70EXq2D8qL2pP-qzIxs-SNvFrTVXMY0oKhC39JuLeUPyGIM2-EpZExVU7aEJ084KEJPyDD90qhov3rymmkmpjH2zrnedu5it9HNGq7dS64H6WnNknw9_cdCsvzkZ2u5SJQHG3tE269BJS_PVSWJThgkSb8-Rr5yksn4g1uNNa7SEV__5fmOZ40f16wV0z0_7hifPWuTquM9PfiRPhXUADpDemBgGcRW15bKGns_3wMIOQscConwvTfVQFrvrZd5ODAvuzuYqyeyuu95BMGto9f1HDO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06088a319d.mp4?token=qcE0xJG3gCUiJmfUqMzwdy8wOvxdqDl2W7p1mzLGGGAkJEy3yj9A7UVd2N70EXq2D8qL2pP-qzIxs-SNvFrTVXMY0oKhC39JuLeUPyGIM2-EpZExVU7aEJ084KEJPyDD90qhov3rymmkmpjH2zrnedu5it9HNGq7dS64H6WnNknw9_cdCsvzkZ2u5SJQHG3tE269BJS_PVSWJThgkSb8-Rr5yksn4g1uNNa7SEV__5fmOZ40f16wV0z0_7hifPWuTquM9PfiRPhXUADpDemBgGcRW15bKGns_3wMIOQscConwvTfVQFrvrZd5ODAvuzuYqyeyuu95BMGto9f1HDO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از لابی هتل تیم ملی در تیخوانا؛ واکنش هواداران به همراه بازیکنان ایران به گل دقیقه ۹۵ الجزایر
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664188" target="_blank">📅 11:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664186">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip6fP7OJnFah-JpjWplqga6mkXobN6zkX3UR7d_o6kCrBuf7eAa4_NzZFNc0-q2xNUg5ZEgPqo-BHTGWGunTh3sq4v_Z8ZMm63zEjSzqYDs-c6xkIQ3jf97J2Hfi_LD3L_vOHzF_Q61-7FMydVGmHauM_aO6PL6CkqLaOdsqr04jbdPnIHWG5ThlHGV5rVMVQ0vqG_S1NpuZ-uGox0_ntT9qZcUEiJWw3YIaGXCKL8P9KvCx4fnH8XWUT-WTx5zMSuQQRgHciZ_CSZEVjV49BJXnFwBUzxsZsRgzsjJWQRi2r_XoCdbD3Zz2Cb8xGO8qnlbDJ7ynHix2QSHxzvjztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ ترفند کمتر شنیده‌شده برای داشتن موهای سالم
🔹
اگه این موارد رو رعایت کنید دیرتر کچل میشید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/664186" target="_blank">📅 11:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaAuqDapOmWsQrajbLEW5lR_koe_LvumnT8fhRSp6Pfi5EcoKW3khpKIwLontBmsFQyNzueIVoc30H8nzQeUM1fqJah-CnZEcGaSajiGiCFQRQNZSVWWgYY1cWPFfXwI51X8JDo0zmrx7z04KmeRy0jMYMrB3RnqO_NC4WWJUqJFUmCcYoIVHJL6qZa5VBtdFeNhTL6--B4O_Z7BlVips5oRgLuToGxx9AaHUBl1AV5k_k60Wr56YP9LI9a8nHWB0sbOPj0xqsy8VZcCaoaP8tWMBx7IYLv7Q1xa-PXr9MpFRKl0JsvDnfe2wM3IkVDjFb2z1SL2dgARbHGusTJUKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت‌های جدید اینستاگرام برای شخصی‌سازی بیشتر الگوریتم در راه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/664183" target="_blank">📅 11:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73bba0667.mp4?token=hH1dMiywhGABgdMiRtwbUAcu1PXbnPjpn_ReaYSfBRglYI967WnpYfypwDi6oOhwfkVLJruI-3Lpysl4cUqTLxyZ68WzNVpmV_aagJxZJPxuoYXUkr9gkM_-_w4JWWtiu7oIvBDiIywHg479QDw81GX01KJKOlYfHNZby2ewVQghgfUYs9_xqrk6E5V5UdCdk4-i11FfOGoLe9Jh6v70YVpFKWwV-k2clGTeDcaoTrYN9cihEV8_Q9TsLXJC5E-gLunhMnmRQPIMVxe8b7-HuHNXkLpHLBsvOaYcTOvINP0MG_uQGfYM2Cxq54mFRX1LiheEkxdM7w0L6g6fdH8uSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73bba0667.mp4?token=hH1dMiywhGABgdMiRtwbUAcu1PXbnPjpn_ReaYSfBRglYI967WnpYfypwDi6oOhwfkVLJruI-3Lpysl4cUqTLxyZ68WzNVpmV_aagJxZJPxuoYXUkr9gkM_-_w4JWWtiu7oIvBDiIywHg479QDw81GX01KJKOlYfHNZby2ewVQghgfUYs9_xqrk6E5V5UdCdk4-i11FfOGoLe9Jh6v70YVpFKWwV-k2clGTeDcaoTrYN9cihEV8_Q9TsLXJC5E-gLunhMnmRQPIMVxe8b7-HuHNXkLpHLBsvOaYcTOvINP0MG_uQGfYM2Cxq54mFRX1LiheEkxdM7w0L6g6fdH8uSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانتین به اردن توسط لائوتارو
🇯🇴
0️⃣
🏆
2️⃣
🇦🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/664182" target="_blank">📅 11:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664181">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdGEJzNBuonVJgywBjWEu1AG7w014Ewv9_2Q-8wpMzB_Ei4DoCRANZ5SXOjRyMhh0aWl9XJX-Lfo5_3baCKOEYkXHwg2nakGacCUwn-DEVrk18il5JB9KaOu1DDOVQM7IRMpobDRvFoHAsTv7WniDWzLfcWHi2MTrHYocaw8mDja4a1jGm2Gj8llFNnbJcMyo0HviqEh36aCc51HTWUFOIJ4CVYXFZtGDSuP-AGKUqWhvflqJxLqZEJ2F8sDOGOe05BUUbAxUtJE58TjQT9up9mN_7iJeNj64_gOtooKi21mVhzf0wNyVARdPLz7KeISKJcwNWmriQc2cSEyo6PBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
این روزها اگر سری به آگهی‌های خودرو بزنید، احتمالاً افزایش خودروهای پلاک مناطق آزاد را هم دیده‌اید
🔹
تمدید مجوز تردد این خودروها که قرار بود یک تصمیم موقت باشد، حالا باعث شده بازار خرید و فروششان هم جان بگیرد. فروشنده‌ها از «سند به نام»، «تمدید مجوز» و «قانونی بودن معامله» می‌گویند، اما در مقابل پلیس همچنان تأکید دارد که تردد و نقل‌وانتقال این خودروها فقط در چارچوب ضوابط قانونی اعتبار دارد.
🔹
به نظر می‌رسد آرام‌آرام یک بازار جدید در حال شکل‌گیری است؛ بازاری که نه می‌توان آن را واردات رسمی دانست و نه کاملاً خارج از قوانین.
🔹
به نظر شما این اتفاق فقط یک گذر موقت است یا می‌تواند مقدمه‌ای برای تغییر سیاست واردات خودرو و افزایش عرضه خودروهای خارجی در کشور باشد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/664181" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664180">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322e5f683d.mp4?token=WsQU4JoE-An-ll9KZgN5WnuyqbERHcZSEHf308aHujK9gf4s28qWqSAOvfh2LC9AGdOch8vX3RfEht6JP7j6kIFBhYbi3O_pUVrYon8j01hi_Io7CjV3YY5uxluDhQ2QbTaWnsyVncz8ARORIUWD-rbQdDDmJZyAw7IV_2n44NgohhxEuAW1rezaCu4OWNPoncOyi6z49PNkhSjjTmX3EA0DQVM7RYaGh8oe_p0H2zXiYM4VZA6ttXb1TsaQprELEis4ipsKSLBaKck6Nzl3mp8nhN6doKRuRsDD5ERlCv1_omJxGcE3OzxlsH-LW1pbzJTdFWk006C4Et3wmwtTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322e5f683d.mp4?token=WsQU4JoE-An-ll9KZgN5WnuyqbERHcZSEHf308aHujK9gf4s28qWqSAOvfh2LC9AGdOch8vX3RfEht6JP7j6kIFBhYbi3O_pUVrYon8j01hi_Io7CjV3YY5uxluDhQ2QbTaWnsyVncz8ARORIUWD-rbQdDDmJZyAw7IV_2n44NgohhxEuAW1rezaCu4OWNPoncOyi6z49PNkhSjjTmX3EA0DQVM7RYaGh8oe_p0H2zXiYM4VZA6ttXb1TsaQprELEis4ipsKSLBaKck6Nzl3mp8nhN6doKRuRsDD5ERlCv1_omJxGcE3OzxlsH-LW1pbzJTdFWk006C4Et3wmwtTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیشتر رفتارهای ما در بزرگسالی، از طرحواره‌های شکل‌گرفته در کودکی میاد، الگوهایی که اگر درمان نشن، بارها در روابط، شغل و عزت‌نفس تکرار می‌شن. #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/664180" target="_blank">📅 10:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664179">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf7ddf7fe.mp4?token=CaS31_MvPWsYS6HP1Q_yjxgXHiP76qiNW10_UryBeWpl03iLnxifW3GG6ws_pSGdeUhfdocJ5Ark5GeywV0oePIZKMyjrY_K-YgM4kbgriAg601Tjvw2-5mpS_Mw6Tk7o7Maku9xR9wx611r83if1CAU0IaCp2pd8DHl8lrnlRUiDVJ9lxF91yG_bgUq6LchC8Yqy_RZPTvFfLTvbSxyXWsoxoYf-tqjaPJXvWpyJe5lAmgUAsU58y4WLMDFlP0CJbKhg7wJ6WHgKjzNSeIOrbOQEddIIWa0AmLAyD_X-oesW1kLL8_Wr9qcwWoo5ho_x6EPz81yEyApYVFUhuAz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf7ddf7fe.mp4?token=CaS31_MvPWsYS6HP1Q_yjxgXHiP76qiNW10_UryBeWpl03iLnxifW3GG6ws_pSGdeUhfdocJ5Ark5GeywV0oePIZKMyjrY_K-YgM4kbgriAg601Tjvw2-5mpS_Mw6Tk7o7Maku9xR9wx611r83if1CAU0IaCp2pd8DHl8lrnlRUiDVJ9lxF91yG_bgUq6LchC8Yqy_RZPTvFfLTvbSxyXWsoxoYf-tqjaPJXvWpyJe5lAmgUAsU58y4WLMDFlP0CJbKhg7wJ6WHgKjzNSeIOrbOQEddIIWa0AmLAyD_X-oesW1kLL8_Wr9qcwWoo5ho_x6EPz81yEyApYVFUhuAz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به اردن توسط لو سلسو
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/664179" target="_blank">📅 10:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664178">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538600ab0d.mp4?token=muZY8nNjELvFN3rHuuISLqNx7elB_cyLyUEbtFuhL2sosk3g2VJQaEUEvKjeYARWR6fVU4XayOJ5d1dt7AOMZtKlHdBVoKam7pAOUIm5eeBFze66zZ-f7aey5L-agbexMWMcg5STl1mcZADwsmHxi0LXo-YoVkSutXUgqKg_bH7Wq4WXtUzqFuq14c-_nh9Cv5tPVc7hwVEkJx_jSEdgDNLnw5sy5UlC0Lt1g92gLU2Y5qGXPE_E2YTz8jvpBayDmrhaBCiInPh8gtu19cD3y60SyMyQazSXFqK2KMlQTYGr2jHxxGAS5VVP0d0h71RQquHsFkqza3uK0gcOU-Gq-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538600ab0d.mp4?token=muZY8nNjELvFN3rHuuISLqNx7elB_cyLyUEbtFuhL2sosk3g2VJQaEUEvKjeYARWR6fVU4XayOJ5d1dt7AOMZtKlHdBVoKam7pAOUIm5eeBFze66zZ-f7aey5L-agbexMWMcg5STl1mcZADwsmHxi0LXo-YoVkSutXUgqKg_bH7Wq4WXtUzqFuq14c-_nh9Cv5tPVc7hwVEkJx_jSEdgDNLnw5sy5UlC0Lt1g92gLU2Y5qGXPE_E2YTz8jvpBayDmrhaBCiInPh8gtu19cD3y60SyMyQazSXFqK2KMlQTYGr2jHxxGAS5VVP0d0h71RQquHsFkqza3uK0gcOU-Gq-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از رهبر شهید در ارتش که برای اولین‌بار می‌بینید
/ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/664178" target="_blank">📅 10:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664177">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9rNPn6GbOxPFK5QLGwLnkLDFfTsIrfSqOZgoWJ3AXd4bKHhpW431O4HrwmLNjO6GVTcdJaiMhjxtGrGKKyd8lPWuLLfODb9jfJN7CxhJr43NVbyH-o9Gz9ufAYmutLKIjtl02Vho9fJXwahk40Yry2kXg8aNgVk3sa3wnguaSdstacv-Bcou7C43hsTeA95RpEV6nPcBuDKiWqNu5jMDc8MlZXWfM4Pbu-ZRIeHkKy5I6O51XDvKW5JHjkK_ji6eyXnRbCNiOyjjtwvopq6rxyJ4YsvRRv04dVwJpq_dcgUZrlttjdta7m1Dewd2JPdu0eqxXPvqG8e_5KvVWCR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آثار حمله امروز صبح ایران به بحرین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/664177" target="_blank">📅 10:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664176">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7ccb3cb9.mp4?token=F1xYFwVKF2_DbOMgZtu5TyaMJr8HVmVel08Tu7a57Qa3BUBiQkFTo8hTiS4b7ssOcy0Z9cWEFz9RSkpA-Rs-aKyYS-Dhq8PR_1ntkIWL5yIx7U6ABIWRwu1zwq4WLkLsNZRLDmvPOy1mq-AjYWvJnhJj5PoNz1aVOlOTXu7VvD_wE5skUZmGXesfEvcKMDLjKc76zpPCaWL987dVYyKPfOgKrdk9haMmLpeoUxbWAhbj4AurjuAqA2lElByc8sfobA1hFER-luGr3TzMheCWmAIoAfSnNZ5UVWxWIj7QbxCLxmB-KHX-K82rr6FSdPV3NH_gm-3wrhsAVsdl1mb7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7ccb3cb9.mp4?token=F1xYFwVKF2_DbOMgZtu5TyaMJr8HVmVel08Tu7a57Qa3BUBiQkFTo8hTiS4b7ssOcy0Z9cWEFz9RSkpA-Rs-aKyYS-Dhq8PR_1ntkIWL5yIx7U6ABIWRwu1zwq4WLkLsNZRLDmvPOy1mq-AjYWvJnhJj5PoNz1aVOlOTXu7VvD_wE5skUZmGXesfEvcKMDLjKc76zpPCaWL987dVYyKPfOgKrdk9haMmLpeoUxbWAhbj4AurjuAqA2lElByc8sfobA1hFER-luGr3TzMheCWmAIoAfSnNZ5UVWxWIj7QbxCLxmB-KHX-K82rr6FSdPV3NH_gm-3wrhsAVsdl1mb7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه زلاتان به دیدار اتریش و الجزایر
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/664176" target="_blank">📅 10:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664174">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
اژه‌ای: اگر به اموال آمریکایی‌ها دسترسی پیدا کنیم، آنها را توقیف و ضبط می‌کنیم
رئیس قوه قضائیه:
🔹
دادگاه‌های ذی‌صلاح داخلی، علیه برخی از مقامات آمریکایی که علیه مردم ما مرتکب جنایت شده‌اند، احکامی را صادر کرده‌اند؛ ما از این به بعد چنانچه به اموال آمریکایی‌های جنایتکار دسترسی پیدا کنیم، به موجب حکم قانونی دادگاه‌ها، آنها را توقیف و ضبط می‌کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/664174" target="_blank">📅 10:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664172">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f59f6c5fa.mp4?token=mE6buOUmGzro83JFa9KI7hnChKiqp0UJ1Fd1tIrO1tm20O96Fr-DTP_uNIPiq_LfFgEZkKDHBUBTypyAZcrKKaXwLj5_aMbSdRRMPjWj3AGhL5OqpSd5Dz9RIlZuLXl6R8CPKY608ID8SSZ9V42tsmXGjzXbsSMV00I9LaOBUHCVwkhrpyzHfjslJW08rFLzkfgi1HmEaQe6LSD4LoCJAcqDdEm7zQ3sWc0Wm_BsTb029NKwrZ4KWY4KOKQRh5RM8n11LNvtpcz_Zz7BLTYRiAtYN0-7gfYyq68R1A1llgPgvLO7dN9-aQlMdtkmYORnL-a7napkqbn4mcaUhn7FXwRsdMGzOvFoSqX7MoJbI-wFQht-eEuc8TZWSoRMAUKRuTEd8UFaw6HUz09ezjqb0lCm_nLZaYjbytQ5_PXEiBQRk3u8aYzdrd0He0sftKF2-50_qWI8aEvMW0cqOHFNML9UGK0cxK4lggNXmKnJvbHDdd9DDnXF2SLl9PrabzK16gdVtakZssGAiOvh_ruZCUaO0qk_Vq4ePlM1JiuABFpOLrf8VWS3n1kGLgrCySFVwixcCggtL5jmG3XVikbjYGN035CKyiStqaeovhLYJF34-5wTUHIi1-26yewmu15zRBur-TrW1JFjAg2OZ3B5WtwZxAVlW_i4uW1B--lxqVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f59f6c5fa.mp4?token=mE6buOUmGzro83JFa9KI7hnChKiqp0UJ1Fd1tIrO1tm20O96Fr-DTP_uNIPiq_LfFgEZkKDHBUBTypyAZcrKKaXwLj5_aMbSdRRMPjWj3AGhL5OqpSd5Dz9RIlZuLXl6R8CPKY608ID8SSZ9V42tsmXGjzXbsSMV00I9LaOBUHCVwkhrpyzHfjslJW08rFLzkfgi1HmEaQe6LSD4LoCJAcqDdEm7zQ3sWc0Wm_BsTb029NKwrZ4KWY4KOKQRh5RM8n11LNvtpcz_Zz7BLTYRiAtYN0-7gfYyq68R1A1llgPgvLO7dN9-aQlMdtkmYORnL-a7napkqbn4mcaUhn7FXwRsdMGzOvFoSqX7MoJbI-wFQht-eEuc8TZWSoRMAUKRuTEd8UFaw6HUz09ezjqb0lCm_nLZaYjbytQ5_PXEiBQRk3u8aYzdrd0He0sftKF2-50_qWI8aEvMW0cqOHFNML9UGK0cxK4lggNXmKnJvbHDdd9DDnXF2SLl9PrabzK16gdVtakZssGAiOvh_ruZCUaO0qk_Vq4ePlM1JiuABFpOLrf8VWS3n1kGLgrCySFVwixcCggtL5jmG3XVikbjYGN035CKyiStqaeovhLYJF34-5wTUHIi1-26yewmu15zRBur-TrW1JFjAg2OZ3B5WtwZxAVlW_i4uW1B--lxqVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور عراقچی در محل شهادت سردار شهید سلیمانی و ابومهدی المهندس در نزدیکی فرودگاه بغداد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/664172" target="_blank">📅 10:16 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
