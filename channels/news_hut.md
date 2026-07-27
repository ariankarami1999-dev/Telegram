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
<img src="https://cdn4.telesco.pe/file/QrvxPEjXiB2H_zBMRtR_LJlirnrMhl3U5xR96ve-ivnlP77LXSdtOBsS3DqJTdwQjTSJ6dSehNhGDdtBTLq0v_4hlvw775mlqgSackhzhMQww7rjKhLhRFNF8Kg9-01IxlLWWhcE7r23s3MeQLa3VXZGGTgkoqxpgOEmlX-THh1GSqFA35SPOO6oYSMOEgJfgYcOMRoB_a_SsRTPl7YbUxWCkmRIEaNlJVA1xDZBNrsj01VolEWxDcNsW22fOwI3F4ToC7ioNuJk67YJIQhJ8sGXhthXqMFyOKhsNM8fnipTWz5dLAr7xJ4BHUrf0-Tylk5Wd1sM2Z5VMzNe-2g36w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 147K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 23:44:36</div>
<hr>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWvvY0owfPbWxb7l8STSmAKde0mo96ElwXhdGs2av4symFPONA13GMwitdD6t3afXP4cilzOMqHUjQEhVgqE3jshEeNFSUe17q_SOV97HcWJaIJ3NyJKKszDOr7dAtr7plAGVkMnN-qhQHPF7k3Mi20NLNPcMdbgdAnPBZ57q1bca02EV7xb5azMDVXI3RkKJGsyjtUTq6mXs5BF5aV5MBw5Wk2lxwHfCHuzIJJKK2fR9pMjpgVfjAIbV7lnI9fxH6uYs0H7hKizFhRRQBnwcoUwUFzipDisTVZNIwwUGGyHxY22yNlP0Zazc-KsCdPdDcsq3GYeLV5WBqRSPQcYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=Myd03zLlAHndm4fO9c_r1Dh4GmbcKZ7KYIeRHkNxnRma0JGU67kwfT6rJVITacTj0OZlsKub5ooanTwdqqQF9BCFTNarTjVJgO-EwdKGhMgYwMVcKdBuHdaztA1mANn0uIeYlSBOOKRXHBCPc6UR8_HrMwbqeBd9PwkJSzLTK1lv9Ols9LMnDi0uf3sC0T7BMyKTo4h86WJgKAWNYgyQwjGQVadKtr19PV4sNsoNqOoa9VVPTB9JEXxS7NH_d38dccMcZbPd7vIzq1MsSmGcsHhLnWKxZ_7NXLCP8q3XK1mnnI3531EpVIIoo7uXWVVm8eeTStYXsb79qR4dMk1l8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=Myd03zLlAHndm4fO9c_r1Dh4GmbcKZ7KYIeRHkNxnRma0JGU67kwfT6rJVITacTj0OZlsKub5ooanTwdqqQF9BCFTNarTjVJgO-EwdKGhMgYwMVcKdBuHdaztA1mANn0uIeYlSBOOKRXHBCPc6UR8_HrMwbqeBd9PwkJSzLTK1lv9Ols9LMnDi0uf3sC0T7BMyKTo4h86WJgKAWNYgyQwjGQVadKtr19PV4sNsoNqOoa9VVPTB9JEXxS7NH_d38dccMcZbPd7vIzq1MsSmGcsHhLnWKxZ_7NXLCP8q3XK1mnnI3531EpVIIoo7uXWVVm8eeTStYXsb79qR4dMk1l8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUzFelpAKkjFEsaglVX1vT4Gia7qms-npYENNv7adEsoXXSQ7_GSAGvVyFMypAGysoIwSbRM1GWkXGPtudkbqKPUy4xVGitmdy-9D-L9JITREPOwMU7n8KcMXlrces0RFrZqDKCURVQzIcgGpCEO1r7lMgzRg0kLon_fhtyckAtiCNkk5nwTIqtr5GlwUpZRn-T4ja7y_2PH4gHuw_pEEI3LBRv8PtriC7lPNg0MbA9_AS7RalzNbsc6B0bT4scTI2YRlomTbXntI_l3xasCgGtRpj1s6WeE0Pk-ofGbsbmG955KxXOe8lboWt4-HluA3TMlrqx_BzrIcS9j9wpyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=ayMyS7KXwzR2XD5GPLqyIZya3XYU6MS99fjuX-QH9YW2KmeaRCa8D9roosYOzsXpHHSVuHfLlzBfCovoQ_fziqIxaNrzVwGsjReNMAK-zjmFNSxZbzgqkjXe3s1sPQ6d4v_kHXcfQHHoI_BGwjVQwiz-oo3RJsGzu193rtdVKkz_2PF1pNsnAsprILEVtIga4Cw-dsQWQdmZoFVCLrW_ncSKFZBGVGR0OM5FcY4F0ScxbwSOTaU8YfDZZ3j6LoEOIUzE1m73fZgOB5S_BVyjCLzDUadOXEXAlXqrpm3TomURebDNwb7IwyroK1GeTYF6Ird1EmJez7zrg4tB4v5z-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=ayMyS7KXwzR2XD5GPLqyIZya3XYU6MS99fjuX-QH9YW2KmeaRCa8D9roosYOzsXpHHSVuHfLlzBfCovoQ_fziqIxaNrzVwGsjReNMAK-zjmFNSxZbzgqkjXe3s1sPQ6d4v_kHXcfQHHoI_BGwjVQwiz-oo3RJsGzu193rtdVKkz_2PF1pNsnAsprILEVtIga4Cw-dsQWQdmZoFVCLrW_ncSKFZBGVGR0OM5FcY4F0ScxbwSOTaU8YfDZZ3j6LoEOIUzE1m73fZgOB5S_BVyjCLzDUadOXEXAlXqrpm3TomURebDNwb7IwyroK1GeTYF6Ird1EmJez7zrg4tB4v5z-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_TG2bAzuCO37ti2blp3hnjozEv-AEWy4huFp7CrUfzvs5QZ_QYtPrONmBNfs5ZM4EbIM4JjiOiwdfdCcu-ZPdx5Wcej9NAxH_RFXdsJ7SjExMtd6_4pv-fLLha-65MOPZnXk-5NutLL6D-ZVPQ9Cdp0EcHM81hVBdol3eZ0e7yjz2iKQsmSWfBfJpGOsnQRSg10_l-VHik9FWmM9viFlSTuW462qwae7iiEuTh2oZaD43_sHVzoYi9aAOO-_HqAYQsIQ2bDy7xWnt03frVOsifedyMAPgPy3X2cSdz4kQ9zi-8iRSBcgT-A5P46lSENFNUA6yKKwOEzLyV1AxvrFpos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_TG2bAzuCO37ti2blp3hnjozEv-AEWy4huFp7CrUfzvs5QZ_QYtPrONmBNfs5ZM4EbIM4JjiOiwdfdCcu-ZPdx5Wcej9NAxH_RFXdsJ7SjExMtd6_4pv-fLLha-65MOPZnXk-5NutLL6D-ZVPQ9Cdp0EcHM81hVBdol3eZ0e7yjz2iKQsmSWfBfJpGOsnQRSg10_l-VHik9FWmM9viFlSTuW462qwae7iiEuTh2oZaD43_sHVzoYi9aAOO-_HqAYQsIQ2bDy7xWnt03frVOsifedyMAPgPy3X2cSdz4kQ9zi-8iRSBcgT-A5P46lSENFNUA6yKKwOEzLyV1AxvrFpos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=sZOIGoyNh-WhiyOWKuj6MToOIpkyF4RtPn2ar8Mr-FfldyrwSd9Ke1gwPdl5fJiqeUa9EOqr-x7mH8SAc5i1sCzJ2E-fsYGxiB1vEeQIKXWo4YESTl_K4KLjLluL5oidi6mPH9MZKfWfOjs7R4aU8wEa5ds3sJ8WP5GxvoOGCFN0AbTaBGmAu9rC5cepVdH8brrKDHiz72zfGDEehqp766nSMwTPNRFO27TkW1Xs2TXEK5ldzI0o0ccV3O4oruR7xmY8i_WmHGX_FF44JPiiLPR1fIdY0Z_fSHR4g0tPZ7ro0Eg0njJTFmBrNnfXDBIvsz9bJiXCNyYcp9s5mkmAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=sZOIGoyNh-WhiyOWKuj6MToOIpkyF4RtPn2ar8Mr-FfldyrwSd9Ke1gwPdl5fJiqeUa9EOqr-x7mH8SAc5i1sCzJ2E-fsYGxiB1vEeQIKXWo4YESTl_K4KLjLluL5oidi6mPH9MZKfWfOjs7R4aU8wEa5ds3sJ8WP5GxvoOGCFN0AbTaBGmAu9rC5cepVdH8brrKDHiz72zfGDEehqp766nSMwTPNRFO27TkW1Xs2TXEK5ldzI0o0ccV3O4oruR7xmY8i_WmHGX_FF44JPiiLPR1fIdY0Z_fSHR4g0tPZ7ro0Eg0njJTFmBrNnfXDBIvsz9bJiXCNyYcp9s5mkmAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=Ukz55_dqPAUpK7JHY9do2uLV41K1HBVfWDIdEDlfga7zMPy4Tl4ykB0VJmY_uEGajD4LDfTzaTSNKND5kTQBFMgNW1lHqSSf_AGtQHo3IaOrQjJg7lrlBoJQVCTW6uYbByFokxU-LRKI49dsbnBanFLiPAjoYfRJbPcKo2IvOg-stvLL3oiClJod5jHHHgCNchibL-OuiWwtj7AMBXU2TfSHv4Zhw4c4vo77vPQfTDb_itq5rBWkze1FKxONvbg9h7GX_vOeii3cBhiSi_73920ZGyA8xEEgR18fPCWaoLCSegMfp5vvnUz5T7NMPZ1mgCyim_snY_VqOmYX8ysZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=Ukz55_dqPAUpK7JHY9do2uLV41K1HBVfWDIdEDlfga7zMPy4Tl4ykB0VJmY_uEGajD4LDfTzaTSNKND5kTQBFMgNW1lHqSSf_AGtQHo3IaOrQjJg7lrlBoJQVCTW6uYbByFokxU-LRKI49dsbnBanFLiPAjoYfRJbPcKo2IvOg-stvLL3oiClJod5jHHHgCNchibL-OuiWwtj7AMBXU2TfSHv4Zhw4c4vo77vPQfTDb_itq5rBWkze1FKxONvbg9h7GX_vOeii3cBhiSi_73920ZGyA8xEEgR18fPCWaoLCSegMfp5vvnUz5T7NMPZ1mgCyim_snY_VqOmYX8ysZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klTK5t0OXCI6uNkPbjlVPhblzhIy3m1BmUD-Fxmp1i0z7uJdt7iEJGg-RBRxCWlSTkbmQdN1u21mSLiqCZ-o24Nw6-7ImLPh7OgXnI9stdon3uQCaIe9ZTgkdj44vPPnED5P1Dt_jVzOASJ1mCcwLLyATXy9tPKGekxGU3PBes_gl_COVQtrRcLM6mmuXSvLWPpgXXnZsh2Ds9nNON--CoKnCyqLyjnRGbNcABqUTAaos1hNVdbB6VO01bAFMbLw3BMF5WVkLz6g_SSwj8Q3map9S8uyjFsWzM2wOl4JOMFSa5-EUfjexnchBjFdlNqIsGX4d4NQsh9KhqkFqoA0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=tyMFVzgu3OcOprLW4shxBFsSfgtlNqGfT2iTzCFBXFgAl1vIFVvoTIR1HW8u9Sq7BhD_is2gszB2F248-XJRFh2sp9NraWsDXbMSrR3q98yaMIJD_ggXADl1SlcMUAtN1cp48B6xFZum399MFQkgiWwBGt261PQfUxjEld0Cs1x2v83Yy-ENBrn_hie4DSWbxwqg1GeS-246Lm8BTuNH_8L_3uGcVW8XUEz4N1hr49LoG4Df9t-RdNRVV8jjKQs1uCcn9C01mSfmFL6bHWsuKvfDla69Zy2J9BZhUp0gUwv0lRdqKBsQ7qxdMn9A3vBweI8YAp2jPkBavKIFNC1T4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=tyMFVzgu3OcOprLW4shxBFsSfgtlNqGfT2iTzCFBXFgAl1vIFVvoTIR1HW8u9Sq7BhD_is2gszB2F248-XJRFh2sp9NraWsDXbMSrR3q98yaMIJD_ggXADl1SlcMUAtN1cp48B6xFZum399MFQkgiWwBGt261PQfUxjEld0Cs1x2v83Yy-ENBrn_hie4DSWbxwqg1GeS-246Lm8BTuNH_8L_3uGcVW8XUEz4N1hr49LoG4Df9t-RdNRVV8jjKQs1uCcn9C01mSfmFL6bHWsuKvfDla69Zy2J9BZhUp0gUwv0lRdqKBsQ7qxdMn9A3vBweI8YAp2jPkBavKIFNC1T4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=pM19W93uwqGrF7Vs1XBlyXuyw8og9LHnMO6lbUCYxnqc0NM6H-BSAd-0jo5es5_nLSZ_PcK6-RDzTWPHJYjrDk8JNnCuN0l2dg3V-OT868ydK6ggeqDPMvsqk-LPwMZL-DBAOL9mONQBJWv-b1lAEJXTvCABeiZZh8oi8d3QpZSyV_FHLDlkLOKyZGKuuBczcMlAJSyJmQFg4yHF6Grw7d-UVM6XLbbQiO45lTyETxfcHy_2-TyQjP5cvZSI1-MmkukqBfOqc6vabEdZaG0kFAEv-0-8asAxqB6E4pJpBewpFaGq22WVD2Z325hGduTxxRic_4GbSjOvDbow04GV7J8XJaTqoLHcR3pLuO_C4oj3-qpPMb_kiH9VC7PILo0dk2COvoUhUyc8flPVU0xvDXqjk9plpCU6eetMg_hdVbcJAlaLN-b1mmnMRWeTeIUHLAdjg1XIhyg_irfBMG4hL7SqrpcuwINroTxoy-TAtd2k8kjVUy5mcj5q0MIYMAxq9GLA9QZiAtb-PfFUXKsmegEP1wdsV_Mlc6l6ovSvaMsS98ATf8R2J2owuQrHxObR-XuaknlNmziGgDsZN4S1pb1C4RE_KLf0yBxbLSTZrxkeuAy4kFQtk1j2pNZcum0aO4J0HzcrRTTSvIrxvc69sdU8hJjBNWTd2F3SminZLYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=pM19W93uwqGrF7Vs1XBlyXuyw8og9LHnMO6lbUCYxnqc0NM6H-BSAd-0jo5es5_nLSZ_PcK6-RDzTWPHJYjrDk8JNnCuN0l2dg3V-OT868ydK6ggeqDPMvsqk-LPwMZL-DBAOL9mONQBJWv-b1lAEJXTvCABeiZZh8oi8d3QpZSyV_FHLDlkLOKyZGKuuBczcMlAJSyJmQFg4yHF6Grw7d-UVM6XLbbQiO45lTyETxfcHy_2-TyQjP5cvZSI1-MmkukqBfOqc6vabEdZaG0kFAEv-0-8asAxqB6E4pJpBewpFaGq22WVD2Z325hGduTxxRic_4GbSjOvDbow04GV7J8XJaTqoLHcR3pLuO_C4oj3-qpPMb_kiH9VC7PILo0dk2COvoUhUyc8flPVU0xvDXqjk9plpCU6eetMg_hdVbcJAlaLN-b1mmnMRWeTeIUHLAdjg1XIhyg_irfBMG4hL7SqrpcuwINroTxoy-TAtd2k8kjVUy5mcj5q0MIYMAxq9GLA9QZiAtb-PfFUXKsmegEP1wdsV_Mlc6l6ovSvaMsS98ATf8R2J2owuQrHxObR-XuaknlNmziGgDsZN4S1pb1C4RE_KLf0yBxbLSTZrxkeuAy4kFQtk1j2pNZcum0aO4J0HzcrRTTSvIrxvc69sdU8hJjBNWTd2F3SminZLYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=JhWm_H2tnjoPdm9rhsAsElV0kH-eO9rQEE9RBvvZtQ2GuMCPh51zBHJPowt6vgQi97aQm-MD5TtVrt2hrSCzZP8Iqzp-eFX2SpFju_u3xw0XKOVwT43haWetBGFvGv1S9aXFovMZFnSP4NSMMhamZdY1OKExc06MS930WU5xPxKFKmLZDCyWqYLMHHCi9xPBad7zarq6L4P5x-F4JnmxlsKydwpD28hivjpyUsyztOHA5ZfxQfIHPJSwmxoKe2IfoP-qHnSho4_kTXVyplxGqfAwHzbWkMnD4m4vINaZFRbd33y8GGwfkVY2Ye665iUX5_PDNq3eaJnjSPUgytLiGLHirssbeFAIWTaB2YLfCN6J_VqfXtI2__l_2YKwHEDMUweGd8HMx8utEE4b_aUfbG2PePol96ZQhjXyL-cXjNgIy4J1ZBWEBnFOl0h_rHXiAdJnehFla_BZkEFWz394b2lb8eymNA0snB2gKwNFMYbHmEQY_LIDmJzsPjvOwOYRVXSuuAyfEtLlwgY-ztqwPdxiC8JlWjnbJOXdSrZgcNcJIspUVZSqSUwJyTHbsJf81OiQ0OKIdPHAlsL5iAQ8aoc4RV1XQFH1Ic74-C27jFKO5y4tf_DqogMlnjEO4NW_UadobimmWfyyHTQABlwakZY8NaSyfzMs7ukqd3QH7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=JhWm_H2tnjoPdm9rhsAsElV0kH-eO9rQEE9RBvvZtQ2GuMCPh51zBHJPowt6vgQi97aQm-MD5TtVrt2hrSCzZP8Iqzp-eFX2SpFju_u3xw0XKOVwT43haWetBGFvGv1S9aXFovMZFnSP4NSMMhamZdY1OKExc06MS930WU5xPxKFKmLZDCyWqYLMHHCi9xPBad7zarq6L4P5x-F4JnmxlsKydwpD28hivjpyUsyztOHA5ZfxQfIHPJSwmxoKe2IfoP-qHnSho4_kTXVyplxGqfAwHzbWkMnD4m4vINaZFRbd33y8GGwfkVY2Ye665iUX5_PDNq3eaJnjSPUgytLiGLHirssbeFAIWTaB2YLfCN6J_VqfXtI2__l_2YKwHEDMUweGd8HMx8utEE4b_aUfbG2PePol96ZQhjXyL-cXjNgIy4J1ZBWEBnFOl0h_rHXiAdJnehFla_BZkEFWz394b2lb8eymNA0snB2gKwNFMYbHmEQY_LIDmJzsPjvOwOYRVXSuuAyfEtLlwgY-ztqwPdxiC8JlWjnbJOXdSrZgcNcJIspUVZSqSUwJyTHbsJf81OiQ0OKIdPHAlsL5iAQ8aoc4RV1XQFH1Ic74-C27jFKO5y4tf_DqogMlnjEO4NW_UadobimmWfyyHTQABlwakZY8NaSyfzMs7ukqd3QH7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BupSD1V0Sg2x4ZGsllBrHLS88oGyGMitiK5GQ0d4ESQPgXMOGZS9pNS7juVvvxhTWp5nDkfC-LWvY-puVmyQk1lcMUnZjpAAVehnRrZJKmIkfo4NZU8yvI4WE2-VUXmJ2TITK8Qi3_RwT14sW9bp13syHXZe9cPDrxi02lmkRSQJ1-HCU9hVji_8w-OCrhEdtReeAt3mx5yPDj7CE_8ht4AyEfQ7Els8aOxOhVG7iGWREGvZZX4Il4KSePvLU7U62Ab9TBmPVJuDawei84JTxTTVYTUt8NNRTm817n1ePHsJw4wPzMwFoRYuM7RWBhnw1rM5XwjIoqYqL3vUVecqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4svIsG0l_KaI6or_AEgGqGLx2t8H4LgBntmzDtqupgWeUFSzQH4HuP_RYuQVD_qETEi8QQ-2HcvdmG58iLeoVQJ65WnizFDQT5P8rgwcDcf4nFXyi8AtXouD23m_TUQYD8zmWFAH85cEsuq7tXLuQE0scjhNM_tL5mKCx7MWC5BcSiDuow5N2NWUDihgxnhgx7SHX8zfVoi--SPEHVea2rdoRcSJcJ3G9_RAvFSmWEl9TQUgRs-u_04boUKnbwEghFctVgxAmbhqwblJ1holDtUfccnYCgVY41UfZ5ykkHfdantEnC_eJ_VKdSZeWSUVOYjTF9n7yHCxl6cH9kacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG_3E5E6kkFsTF9Fgx77inZMi3CQawzXc_8K7KRPbdfm3tLzd7XpIdo5iQPasGnquVsPRzPjUcJYJL8KNAsoriHINFLU9xD4oISqX7FjotiFXdheuKIeXcGOkMICbbpz6BXeEaCP-egrExJZ4-Ds0PkLhojSMF0CIQj2fx920-abWaDC_XwaFZhW-UBlXaQLdvYkvrMKHa4T6doBCR29m0wGIdtWX37ExjGk6RihxeIwNxnf9mniSj0rftFewXcGKVGuKHNLTNkDFEyfSbAgj6m38HVMefQzqhB95Db597-3stbtjpso79j_VklR5QCrvucmywbodciRJdohPz9Xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=m1riKDHtRzEgexk_Hx6XRfKYuCvNJGV3vwA9DrTeJhOV4efkjP-U1G2HCrsCk2WrNfHWXWkvf6MytFExG26G7RjjdjgKVNMONSZltmtGQ2hGc097vDA4EZl80k9nKpCCy-JFoJrmSQyJcDoTnG0OvlNSmbhAX-ZuZMen0BsmXnObGQijhVjCM2ybvv5zJh7IYiRPs6KSxrxPcE3GjT1enxCkOr2L2oIqLG2nEjhC6aDhk_outcRdAPv_PkiujJWZsfKG_wDrCBSwo-OoWTjb9FX0SV-_HDmTgr7MxgZLUjYEqsqS3ha20W9TIYtdWwQANiCDqF4GmhY5FK_rMhHhkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=m1riKDHtRzEgexk_Hx6XRfKYuCvNJGV3vwA9DrTeJhOV4efkjP-U1G2HCrsCk2WrNfHWXWkvf6MytFExG26G7RjjdjgKVNMONSZltmtGQ2hGc097vDA4EZl80k9nKpCCy-JFoJrmSQyJcDoTnG0OvlNSmbhAX-ZuZMen0BsmXnObGQijhVjCM2ybvv5zJh7IYiRPs6KSxrxPcE3GjT1enxCkOr2L2oIqLG2nEjhC6aDhk_outcRdAPv_PkiujJWZsfKG_wDrCBSwo-OoWTjb9FX0SV-_HDmTgr7MxgZLUjYEqsqS3ha20W9TIYtdWwQANiCDqF4GmhY5FK_rMhHhkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Ov92E4FJRmetJQbnzxJOXdumaajhRVyJJCTbOdLvNBgRj5hBRWye7ibs9hxD28O8THKHci0hzNBd6qy3nMz2CZXvKS4-bB9K40IsM4i8O-uGJehfjI5mjsx0mdakFSLLorf3FDsco4DCbvmv3QdH8xH0_m1ysisGtW7vmLY5tynTXw2_oi5pcLqJvve58i_syPy-koAetSdzdxD9YZBq5McQSADVNvd62aggF4mojiuVfpDtlRQUPqODxyJeEc2vYaBm0ZAHeBDtAiWQfQ2vz9ut7v2w_hTUzVr-eRRjhfBj6647P0ADiZH4TT65aV_S42UDSbHpS9yV_3jDJ6VAdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Ov92E4FJRmetJQbnzxJOXdumaajhRVyJJCTbOdLvNBgRj5hBRWye7ibs9hxD28O8THKHci0hzNBd6qy3nMz2CZXvKS4-bB9K40IsM4i8O-uGJehfjI5mjsx0mdakFSLLorf3FDsco4DCbvmv3QdH8xH0_m1ysisGtW7vmLY5tynTXw2_oi5pcLqJvve58i_syPy-koAetSdzdxD9YZBq5McQSADVNvd62aggF4mojiuVfpDtlRQUPqODxyJeEc2vYaBm0ZAHeBDtAiWQfQ2vz9ut7v2w_hTUzVr-eRRjhfBj6647P0ADiZH4TT65aV_S42UDSbHpS9yV_3jDJ6VAdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhNJxy7cNeIWAeEPKA32rQVOaESp1kSWduLeXzNLHoiEDoD5CQqb1VnL-X6_e4c4FnapdIJ7xzW76U4XX0S3g_VR_zqXYqkBfShCClFnNy7VtFhWY6BNvfOt6LNpvuxtQ_DniK-ybAq_Wl0zbPvEqs6sd0gBr1PQE9oWFAHVr15atwLtQPe_7L8DXJEY5fP6xKFUxsOePSEDNjcqa1cTmhhg3NJCdWN2NS9b7fU-9HVBsBIzpRtOc2qYS4baUZ3DrL3kHJSxo3fA5ReZB56W7vVW36n0r4tequjT4mYnKgedfm7L7rNiGA1vLyYewaESXi4lC7e_e_s-Q-HfXxP_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky0ZBQZ0T5YPMfVc2fyJp4kbFRQHO_DZAw2Yb3HJLh7Ocn93TEK1oyXkHEr2DfouNaUe8x-um0ibBJgdZFzQlBHt1ocRsyPmWcOjLRTS2YCDA6J3mPwYCHRGaMzjVs-FtdQTqB0EGRKSK99_L46q1G3i5ynMpVGdLbZT3rGvcEqHZmwCf2uwNHWarNZkhhUm8pslgboBK-Vk4VIovXaVi0xCQJikkihm3YIX-WXzkL-OXtcjd6F5Hln12Y3cjmkRuxbF9n4vxjsX6_7GEvnV2J2MnF51eE_s9yxuBbn1MtBiWtA62OD-6zTjrLdpU6Kl6qHfUshoHL4JGvoZu7M0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avd69e2wBFFcmBb1oEjAIWkk9VvvWfyncVAIZQWjSs2PckiofFvH3_nicQdnWT47lNrpxnA3OVrxbOFnA0Wk9Lk2Iyk77xlJiOyByPm3hWgZ0t69br99_WEI8sav1i6I9FVJDr9xtZFEn9LnEdZu1XLetIHnVSSCjvaxof6MYP_rHk1vYkmJlau2Zdbs1Drs2ziLlRuvQraepRlgDiG4CPh_YYtdM16SpMxXqvohevC_oq9k4uUL_EyFYvLnESm9OZxWiZu31uyYBrd0OuYztfTdQzYCyGg406rclC8qoG5JUqZMZ6wvz0msPphPqITd-JbrR01-LYm7SSExKf2AXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👑
شاهزاده رضا پهلوی:
چهل و شش سال از درگذشت پدرم می‌گذرد، اما او امروز زنده‌ترین چهره سیاسی در پیشگاه تاریخ و دل ایرانیان است.
شعله عشق ملت ایران به او روز به روز بلندتر و فروزان‌تر می‌شود. همان‌طور که جاویدنام مجیدرضا رهنورد به نیابت از میلیون‌ها جوان ایرانی نوشت: «نسلی عاشقت شد، که تو را هرگز ندید».
پدرم با تمام وجود، عاشقِ ایران بود. قلب او با طبیعت این خاک می‌تپید و باریدن باران بر دشت‌های ایران، برایش بهترین و زیباترین خبر بود.
او در ۲۲ سالگی، کشور را در شرایط دشوار اشغال متفقین تحویل گرفت و با تکیه بر میهن‌پرستی، ایران را به سوی دروازه‌های تمدن بزرگ هدایت کرد. اگر فاجعه ۵۷، مسیر تاریخ ما را منحرف نمی‌کرد، ایران امروز یکی از درخشان‌ترین قطب‌های رفاه و توسعه در جهان بود.
هم‌میهنانم، اگر به راه او باور داریم، مسئولیت بزرگی بر دوش ماست. برای وفاداری به نگاه او، ما باید ایران را از این فرقه تبهکار پس بگیریم و آن را دوباره بسازیم.
پاینده ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Ae5PT8gUezxTIk5pw6H-_Npx8BT5WKK-EnKuYF0o_rqwwBaxx2UtmYvwtS5PZ8h0AMAh5GXaIOMZIipyx65TpaDA7gH_FMUpE7z7v-B684_394M5JuTDZUny9o7EkAjL6i_bH2A-nGMjjxCZ-AIdLy9P2Pfl0_8LAcxhfz8E8IR_I9_w7jyuWp6cziwbHuiq9dfedqVp1IrFhKY3pEqw3ruqayrgrGcb4L2OGSsCmgZ7T6lmtMmH2UtFcQ93W9YIOtcT_xSAgQGxeXzT3NUnOF805g05q6-10GYNDJAKopc5ZmSYZ4swNkZw23vDuVsr5DOnqyrstw7ivdJRgVs1F1jcM-umYkB1cQjeZa_YjekvmwEUUijaLEkZwEpEQfAjVO3Mz3ZW_e6G75eN0VnjoY_Z-nJs3WnkBye-f9lqyKoZb2mwSvfAbXdr4TY_iUaeiFkjUUd4yT1atTnfqsHinFjWZ_r7G8cu3MEDoqJcSBy9_FBrvGpA5_6UQWJzx9sXAf5vhHGa06-XQAa5T6XL72ZR-SoZYgL1_4ajmBwsr3iVL5KHvzMxIB1ATLSmiBy-L2tRa7RmCtvolUZYn3qZ_4IZaIX_PJWsz_m0CVnt4ldS7UtER6phJ-m58vg0Cy-3kWv5chCwUCJVLJmGIkYVsCM2qJOGjr9L5nfnNCKn5s4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Ae5PT8gUezxTIk5pw6H-_Npx8BT5WKK-EnKuYF0o_rqwwBaxx2UtmYvwtS5PZ8h0AMAh5GXaIOMZIipyx65TpaDA7gH_FMUpE7z7v-B684_394M5JuTDZUny9o7EkAjL6i_bH2A-nGMjjxCZ-AIdLy9P2Pfl0_8LAcxhfz8E8IR_I9_w7jyuWp6cziwbHuiq9dfedqVp1IrFhKY3pEqw3ruqayrgrGcb4L2OGSsCmgZ7T6lmtMmH2UtFcQ93W9YIOtcT_xSAgQGxeXzT3NUnOF805g05q6-10GYNDJAKopc5ZmSYZ4swNkZw23vDuVsr5DOnqyrstw7ivdJRgVs1F1jcM-umYkB1cQjeZa_YjekvmwEUUijaLEkZwEpEQfAjVO3Mz3ZW_e6G75eN0VnjoY_Z-nJs3WnkBye-f9lqyKoZb2mwSvfAbXdr4TY_iUaeiFkjUUd4yT1atTnfqsHinFjWZ_r7G8cu3MEDoqJcSBy9_FBrvGpA5_6UQWJzx9sXAf5vhHGa06-XQAa5T6XL72ZR-SoZYgL1_4ajmBwsr3iVL5KHvzMxIB1ATLSmiBy-L2tRa7RmCtvolUZYn3qZ_4IZaIX_PJWsz_m0CVnt4ldS7UtER6phJ-m58vg0Cy-3kWv5chCwUCJVLJmGIkYVsCM2qJOGjr9L5nfnNCKn5s4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW2Q3N56kec2IOBIner8y4HmSmILluGaNwHntKycY871xHOSeKYBAj1a4UB9le8XQ8_yyGghMSGI5msmM-mo1zYYOjg4IGac7jfc3UMqQDTrd2tqXtsT9YLmfWhUQDPuf5DH_6hUKJKgjQx_hRIsVAW-uZ1B15mlPyXGBBeRcSBCqMX9XXd0KZM6h5FzYxKaxXGcYwgCEJalraEkq0LZrnxMpVEk5LK5lGSwJTwJITdWXzP-odFvY1zri6gd7EyuI2TjxBptNNoQGADP07yWOR7LtwhpRipmdNqLfWUxGXVff0be67C3Qv1JKV0YhgzEksMLClPV2ywEuF87K_UX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Qo8wqHHlw8u9Qdl5VMeTpTbsKwQwMdhyEZGbywzXzvt7gyvrVJsshrH4lnmZbXhkfA5-7ca5IJUcoD-E65xpnkhmUxtdhs2J_2EIHHcIpbwWqIqSjDtaUiO6g-mHSoErhgsF3VtoQwo1n5W4DtmgXWDgxoG1rRnEBw1kBlkJ1zw3tl3XDFXXsWI0NuCg9IAggR-q6YT-ufCnMEoQ3HEw1fn8cqPWZ35BZ_lgCnfP9PLONhAEzEzymt_gTsGEdcxZSMER3jf-aayQTLJS2qaON09bKsc1gwGoHQmbosHZJI6jh6wjQk8KfrGPetvGOyd1EqOeVnqgfaNUQvoD_xDCwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Qo8wqHHlw8u9Qdl5VMeTpTbsKwQwMdhyEZGbywzXzvt7gyvrVJsshrH4lnmZbXhkfA5-7ca5IJUcoD-E65xpnkhmUxtdhs2J_2EIHHcIpbwWqIqSjDtaUiO6g-mHSoErhgsF3VtoQwo1n5W4DtmgXWDgxoG1rRnEBw1kBlkJ1zw3tl3XDFXXsWI0NuCg9IAggR-q6YT-ufCnMEoQ3HEw1fn8cqPWZ35BZ_lgCnfP9PLONhAEzEzymt_gTsGEdcxZSMER3jf-aayQTLJS2qaON09bKsc1gwGoHQmbosHZJI6jh6wjQk8KfrGPetvGOyd1EqOeVnqgfaNUQvoD_xDCwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFNKrBPP-FwnkbjxgYubi1zoHJ5rozCxD0KjuL923o3lCeLhkjJIBksUKbwJtlIRBAxAopvfOHFr__kdt208UT2m42-MqERjO_gaKT3nRAsGWujuMPuD-dDQ0r9VfsjoM0ByBzTNaNW6NTAHIel7zgILVm8TMVvv0zbNCUl1OLgv_p9Hrd5BH02OJvPBY6NL7mH4JS8Ucl4CiwaWpDCq2N78fgTBup34O4rgp-k5mYJkm4voijkxmK8oK1QYw0pTHXv-SBgN4mNZeoDhpnzOMkb7EH968AKp8k4bNSvO6tS7ak-RU7l-BJArhs05eMalzqWoKeoeX-vl243_zEDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h-mny9qaFlhJ7Jn8ao8wFQ9ifyQzjt7-lnHjOn7WOAG32fb_NzPxwe7t3DGZcep-QV7T2xZve0MKiuSfLo2Vt6s2N9sCbZy6EIIjHmyV5TzWTideKlMU5GaEV1P7N8LIi2Eq2bE1Uu3etq6R0ZaAb7wRyEF5AnX1XLyzKlUw581S3bxNqQzefnmCZr9tn15tZFKncjgdYABOTUx7Co87G19pfQTKwvkwb1vaOSOz_1OC0DwZSIpy4WtlgRKlPBhrWriTpFmBBmCjUiOccizTIFD8XslDKENJvohxUd3Af_QSsuNUu7FEZqTC4oE2AXcV27SUXbA97J0P8uCFKd1NIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p1sCX9o0tHaU37cU8Is6ijgJUtN6Q3PcYmGYIpFUXr0d1E_aqN0P1NE97-xSQ3pnh5txY0Sv5ifuMvm_8pZbX0xs_w1SGpWRCJHt9JxwjRmyD_TZNuboouU0VBQGj8lfbTF7GQ1U7dWdh31n9aBjNmJy1mHXbfNSqr4_buQRiQOllG8i1_HbD8tIBiGJEryIR1Jhrj3Zr8uhmRaEH4etfu01NAcuSmfwM7RtyGqOwdNQ6mV6lPm_Wgg0oqBRwuQn90DmihB4MRijc-R5SevYv1e3UV9IdVTC8Yw_4YHqAtruFrSVPp1Ew35NeeLsP93LXjFXTBMSOWbuQu6WeAtfXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sdm5MygwAxl-V8q-q9x850WIvECrnRVaCJIFTF4eVCoFSx46jg047Lm_KFQ6d-1Bus6oSZp9ae9f4ygwbqhGYo-INmbe9CQuiPMx7YWgnHyx3jZqMS627jLej4FC-QRvD2NenRwMFbm4wD5jj0GYZ306-1cjgSCcS2P7hl8n_XWVscRM12HT1gNEk8I2-WfATblP15mbQ4_hnvYM8_8dwHjSa-TA6j5HeziF1fyxcMD6Q5N9hHetYOmtdcFnY9acF_OeMXmHYKKUuvqkRM7q9Hlixzeu4yz5T5Y0xdihadve3A4vOURcBfPplTXMt7V5wqoSb1hSoyi3OhGoskCeuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sdm5MygwAxl-V8q-q9x850WIvECrnRVaCJIFTF4eVCoFSx46jg047Lm_KFQ6d-1Bus6oSZp9ae9f4ygwbqhGYo-INmbe9CQuiPMx7YWgnHyx3jZqMS627jLej4FC-QRvD2NenRwMFbm4wD5jj0GYZ306-1cjgSCcS2P7hl8n_XWVscRM12HT1gNEk8I2-WfATblP15mbQ4_hnvYM8_8dwHjSa-TA6j5HeziF1fyxcMD6Q5N9hHetYOmtdcFnY9acF_OeMXmHYKKUuvqkRM7q9Hlixzeu4yz5T5Y0xdihadve3A4vOURcBfPplTXMt7V5wqoSb1hSoyi3OhGoskCeuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqHvF-ytla3tB1HPtPNv0jdyHh5tIPGT6erYd3gSJb_HSrD9R39LPYXDiXK1Yd4sZmbqmwXfrvl8HIhnHn95qgZZe52J10QAqxbr0idYZxlKXNYCD8FQbHGeYzza9aZZDxHxx7YOtUkYCEHns58gc2nIkXreOuwdSEFaMb83hU-uFCjlo30r4Sjk49sBbfgZ4UIgBUW8BUPxU2Fk16mFt_CQalzJPqZGaGyUT4oTvg0u3wGsWdnCIN4Qssr9cjHwqtwzyRou9cB3Ao9i5EPIofgUoheTQLodia_ih8hMhmJ--OzJOPJTmw-WMliAu0C-kD9h0xytVj0gIGMr1xv9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTq7ZhpHRa0xW4U3AZyh6n9KOG6CQUxe96PZlvRbCApPS6TKKZnmOF-zjSxMbKm9jdG3ropQW5OF4OaBcn-KGG5OISC55hWR3lKZNRyAWK-8YZgcWJD3R13JU4EzIcHLfUO1uNe3LKyOFubOz4kwdIpb6bPAx0dpPHma8nEnuc7jHnQYYyRvo4OzQeg1bRLeyakE4X8qCY6_2r07WGcBylL_zPeAl89I7BOTrOTQhnfVHpRDMdsEw7FdCaE6jInGMSM-HQRx8bkoOoX6zp8rOo761bKUbR9bVYhOBbXlGcjIcbGp_6f6hT6sjBwiYHhDukPhm4f-nPXqiEL6FvSdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8bQbJk46hGnzdd_KlTKsLTddDtEQAp74UyTTqgFQB1sDlU1JkhTDmAoRzkAArOEHNy8WUEy17Mi1mM513la_R1wVOAil2IQCgCp6fL-elWRobnFgeijioRIqTuuZC_V_ZDXqI6E4llqMEQdMt_j-CKAKgXuwzpdNjSxyd6lpKWYzdCf1-DQfDHR8yHuPUGxJ17IdpUs_AZ631cwIWW-Q0DBMoh8KJkrcQmRa5shUoOkC4rhkCLQzZcS48-Mg1bT0eeTnlXknDxAS7wZB5Y-yFbe4t-eYaHlZwvS3ol5DaEuC0OHqy0HAOLwqFMH9zSWj4nwpI9Y3b0HeTQhvXTzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORquAA7EzfCozfa1p3isqkWukbUq7He_n8HyfNdT97GwzphNJKC7l6ddn_sXxPqUyYy7vv63k2OTDdVjkrIqYfL-cLKgnjjJn1-T0BK8fwEE-aOJXp_ucjmORQanP66ZgMp-eNT2mkBMI1vwJgbtBjQvtEpxbwB4f_lUCsrJq2tm8y2Tpg4ZShK6dFVbPkrnUimRDVpxRkngNKHa3Z5FWWA-8SW7mCiyo5EncageEIMAu0gIoCDjEKCpwYeaj1Dg-LWq99GnFKnDbnM1ON-kMeSc-8K3rsum2_2Ryka34MVWHDjziuXcbGSLvqzUQGQts2qRJ8SsOriOHJgtQmUAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqOlAIiuW8o_6zzZgpLQaTdSjFL5jWS3fwresLgSnCo93_4gnoeoAZomwPz0G02__UnE7A1l2y8MqosSDqGwOozDkgh8T9NxOu8P0Ll66kqoRbeVwqK42YWVseYLk3BoCoPyN0mU9F4GnslQ4_lthrYWC77sJYqhVaFV4reyGsGRgbWmBmARw4rkVjEQ3uYQt9FsXJTuHav4xK5avZrlqDRTafvXVwQ25hWt05kceGbPFZzkS_8ou98t5Z32Gc0vc9monFtE56V3a9SLgxzcgAW5D5wyQR5Rjq75u2egtHZP15HkxVfF-iUcoW1t0jJIE2wxUnJ1sfuXxl4HSlJwdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szbtJ1tjQc3JoTjJ3F2ci02dT-_HvVRGs0mVu0lZHewOVJ0t3iT_l8kVD4td8xX7Hl3uhjRna-eqVQAUobsrzC4Q-6_APyvQ14DXz2dj9VFtOTOXTYQfzo1LqQ_fg1ssf2Ufh_mKYu4jd0_hBU3joGZfrk83fZ306Zo1Wm9fydc6O65Rdu5wABsq3mN26Oyy7kqQ0ra52TCY_mkOinEIB8qQZi_lcwjdN9YEZmCSJ4HqHwzB6vEqHXthCI0V5Vp_IIip6DM_z6u1zwK11wUXF4vrOljyOpfGvjIZIh7mxfV7crgSPa_HM9SpqZyZilDBYS6Fsb_ffoHkedBfVFKWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEfjkWzaccIT_q1H5sf82LOnW7aPrNWcKg-Mp-xmqqeo9qpyP8e9Bv0hRjsNf68NAVIP5acdkAsCOIGZrynotwi-foG35iwJi8fWxj2nCe20sM3eJtXYjVgEj5exqetp1aEpQghZkXWXoEOAH6bXwW6kzwUN2N9rFlbxzkNn6I8S2kUWNcWI97sFm5E1_woNrZWAaguJihln59tkKzx2TBp1ud--w7OhWAXrhat62_kM9ixsrucy9XvMQYRx3LJAGA1Oi4sK967TD5-mM5mFxySrilWu17mdVdffeot1-SgZHDdIRhfC05laWo-vyKptcKC33i0jBQxrTnl3nJQ2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwALPY8INHEb64aZJeuqex2ygVxd0yWCiiuDuegXPwdG3Mm0hZar8GuCk-pvzzhVVDkAWJjZ8KyOz0Ykbk83kc2rdPocL2n6HlBeAsStf6oYxmsHLh9s3d62OHjLWh0biaS6pof8jGp_XXNa3tjK5sYw4Wm3icW_tB2H2xp2I-RZuWWwJuaiM24ANAaTlRNGB7ZsdFcFWeQ_V3s2v7jNluMQBjkTxk1kZl0xOF251yjZTN0Veog83ljBm-rfDz8EFvzoPMmjGrnPiJMm6CAFMjmtFMiXVrxpunb8JqEb-4oiZ5VWV2_6oKocRUkpVFRt2dASJExJpDJwDy8gO39aaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXNXRs14KgYWTl4sld-6g-J7eiZEc8uCnoOs0LfU7G40wUDAvJ3cqjE57727I4IY0dBJe_COnzD4TcUWM1ofB_Ad7gDADfYWMEwd5buwifsDf3ohNTCu2XvgQ-ap1EGJ2Ty386qp1ftErQtHTMUi-n3aOBYGLhWVz-RpXtb3zX0Dp91-Y9bVtGLs8g852NrxKzGu6hDz8AmNKBkxMrFqTPFIT0BHWvWRmNLMtab4HchDXRqPgmWGARv_1VsOWDXrfaBjKQj5iYAlLiulyrKw9CgA7Cr7xsuRzlr2NntgeIBCaGU46ikcVs-mVJ-zwBrLydGAki72o4QkOeM3WgIC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbWVzPSe37HF7cjlr89CADWW_n_BXpqH0-SiAmfUZiMPOAPq790zncnml3Ij2LGSKBbokD0E3EagWI_r6ahQT1lh4rjJOIyadb8UgVWmA5AZoUfG6rr9OaNgAmmZrbKIYazZJpMpO67O9bv-3nA8zytohzTUX5Y-F1Po8lRGONTzW3iJWAJfJl1WdB6wmznQcv7-sAOp1BsVTG-eldnanAXjBFRV0sxwtcudcdaAGkWRLhdC_NXwolX7iIOWob7WVHwQjsWw1J_M9jsp7pSDCAoKUqEtWVSuD4r_BassqzLVEhDtRlJJiRizmFI914ww9ch30hv4SfX6x3JkRoWkeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCe4XBlgTmsnWkScQzkhIqqvwsaELc9j-7j_H-ZqZRSKQzcZZ8-FPW3DH2Sw5eqnyTKJ_bjPIZfIcwLEnXD2XxMcH3d6C7ghR4osbHEZhjp4lqYLfoZIE2Dz317ndc3LhCeHO58ppAzrt-nUDBo2GdVZta3FI9szqTMgEHGDI96VCny3FgxvUMQwByhMo_lqEMX0-rZD1Ezw-l90iE0NhrQwVh1-NHUs8YIgHBXzwELkYXQwgo-Q-oQpLCZJisi52isPwF8WuTyxuaw8a2f6i0kJSXYbn6s5Y8bqRWBGt6WWn-VN015wTs670GscDJEGOzcVh5FvXbwa6FV8UiSzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzSI18n95hLS8eeFTvLO9ioMSLoD0L4JlVJ-N0wAhYilt37or7AZQj0u2Rzfy9rfSm9xzn49vJ2cpFaOtFg6qomz-A-gvqmhgznxc0iJb6ECAQucmSToU6qCy__BzbS8H1uZEYSUGT_5PmqLrt7l59iprJBShW-CXHmJWHBADHk9kCfBfkso4BuUOudxTS_-ExGajCoS2lgoU0a5ATIvKp2Ml_Dhy7a6yFW6oYSB5D21zqr4WBTX0hA5pyV7V3qHB7pKyE-JkkXPY6wLzCLOpWS28gphQM62TSUnzMfyW0d2GMZMM4mxvVxLSMdfxZijm35f87wIeDIR1V3aFmpocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQREaawW0phMxZTL6Ajw-fJSCWSmqRZ5reOa85p8hIeb__kKmQvYiGlqcBlmEIVrXCYz47yH7_ILfYswggB71McZ7K2VjKJ8l2nrI1Vhbyf368jg--oH5EiSjRZxd1_V0Kg3JVxYyHgtrhB0ruCqOxDOhKsmu1XSMohSmCjaUwRKZSoERZ6wpY-91pocef0Eoy86FkhQrb36zwBksXaXrEiRqnGPVyCvGPLJ8gWHfkRvlSRgFlSoEj1Jj6kDM7B2ZSEg72sDUhu1v8zEoez2sK0-NLLq1FfM3Mb2keXItZUlTj6gMUMlDXvlbXSE2cKELMR3IIuHor_O3YyMuB6FbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nU2Kc6sh8p9990MdahH4N0oFTDyKhnhuRhHLXWwof5QoT8S0qExbNxQBIYJv-2ZKLfjCE6XQ064BmInE8pYRRDlgCvg36MTba4Bo_JXgCdNh-m3l0hXCbtqJ-D7GOBBxcIPwR4kt7UpnUB5Fs_OAmvyaSiCxRA0NHKuHjR7CKKh2iGzlXS7UBsGMqZlCl4n7BH79ug0VqAyhRW47iqHjHNOJ-YGe3FSQoZZefrDpBm-GHkMooIRO318CjXIDiKCctprFhIKz-CQ3xRR6HLxwLpSOHHxKiwN2sszpNyNC-3ZVpmd46VAPxOQS7-CKth5IU0FC9fud92oShFgBzHgAeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=bSHqVtW9_ZtsxkjuSMCAj89q9v2fy_Za3jzRxWQMJHF-bSGxjqy97sFoqwfrx7HiAIi594wyhCsfbvEPziZujhkSjXeglPSOUSrYBlyYI0FLJ_hzN6ybXJ1M5Xz6iH_JfeGZmWUgqsQwuY2lv7KyL0pzvv8HCp5fIoN_ZxUFUH5kytCS8WQgBKPBQX1-y13oLHPDfv-Yu8RhzDL_JxfGr0qM-mbteYGgLuv1gc5zrddeiqa-XNu6u6KxV91YGLrbNwX3fhMGTaLqm0FgZe5e4B_M5qfKPSIjUW-pg8j_OgeY_ZHWyz4wEjaldGeYGuu_py7wSCXVEo53vcjpq1Uxhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=bSHqVtW9_ZtsxkjuSMCAj89q9v2fy_Za3jzRxWQMJHF-bSGxjqy97sFoqwfrx7HiAIi594wyhCsfbvEPziZujhkSjXeglPSOUSrYBlyYI0FLJ_hzN6ybXJ1M5Xz6iH_JfeGZmWUgqsQwuY2lv7KyL0pzvv8HCp5fIoN_ZxUFUH5kytCS8WQgBKPBQX1-y13oLHPDfv-Yu8RhzDL_JxfGr0qM-mbteYGgLuv1gc5zrddeiqa-XNu6u6KxV91YGLrbNwX3fhMGTaLqm0FgZe5e4B_M5qfKPSIjUW-pg8j_OgeY_ZHWyz4wEjaldGeYGuu_py7wSCXVEo53vcjpq1Uxhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTYz-YHkVRD60dcZC9SkHkJx9GEn_3Ty51inDAI8ka6LpvgK0qi2Cz-6NJr9MYqOedbbVHmhO_4uZXsrRXIS1BbDOeYjmUb4nPhYDse49V-bJ1C0pZxIOVCjSKPGyj7Rn93aNJdJsxBgmJQKMuuuGcEeSKoNB8vdD7FadflqI5DUgy-JYDshenZamFVfPDpH6qaJdLLsFpEY6Tz4o3PUhOcYIU1uDKI9flbzaScNqQg_HJufYs94XCKZd0v_AONe4p-Olg3mdk9srvUqUBQuqE3EuuA511gPM4ZxNXkXW7iu_QUhh2rCLll7rknWijAPUYsSc41s25q_3lPbBuH09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3y2SSP98WTmV9Yk-JGeODNO-Le-FF0hnKDBomsqsRlVNyBe4tnJ5haw269D7zCDlPv1kz61DqVDuMy_5p2G9fWz8yUh5CyOMy2v9esKmBVHVjTaSUQQhkQQDvmI6rwzhH8IFIt02v1r9SFkUaCZWhPrG-dTCukQngRCz2EC1IgcuulGk0M0rkmNyvEwmpFkxNkP-BE9DzU6o--eN7ZnsqMVv24Emo6HrrGGstY0E99v9pGZWA3mHCKrxhkGS02yXOo65Mko1nQRF7mzPw9ZmU9CcAgyP-p4iLUQ6wT4LMa5p_9bbMnhYeIDlY8MQnE41LRSS6tBiZ1UG1AUCFj-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nftnpZky6UIOpznLUSuy8gMaYYcJkviyE-KymD7MtQ3BrMfM8JzjwptI9JYPTM0Y_gVNFovRZ6egRZDX_XqlVlzBYC2kYA0Qbdn8eKlUF9ulCKlV_MKhp-_JiOpbF4qhsnmoHp3ZxBB2FQkGaOQdPQ1A3fmOioeCLO1lfAvY6amZZa0V6mF5yeEWvHj5tr-XWT4xjTo7GVw3qbb7ochnN9Lck9aLAvOakEl0thLGEoZoc3ds5eQEVDiP0Ht2aTqPqMUw1WXapQ04ojtP8VmjKB7i1SNdLAH-SDx0KamfljIrB0Dfr_kOHILC57m0BWm24GyQZkQ3V5hRqKrx4xW6AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl5qoGeU7ROsMbNuRcpUsk9V3ZZo1fgwjHpgzywJW7cYaDufjc1IffFKkwQQpaaOCFiEEjgs1IpU5J9JT1NTa6ksyrcmUSLV7g9SjkghhyBdPu3Z3-Z9bQOXGY03I2kvejLhvsHFaXqO0jPVBHcaDeUiX_wCAJRq_-EursrRw2gy3ozgJ3wTWzcp0XFiYAgtKABk6zgOMJBPU1Aqyc4deE-SDtMGWtRB4bKo0piiMk5EyJP055wVmzR0yaEVr_TkPfGB-JIKXk5W7ZsxKBzsIhrMNND21qrAq3JWMO-jBeswrhoQw3HxoNiUJ3IEilydEp_IWySMODTDdD5_B4l2LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=EWNS9pFnR0N7SUe9-Gs150KAJcdQ6EZ1V_ctYhLNvwk-thDewcwy1b7lbGAZ_zJqNt7ZgAwpk-JmetYxaq9i4Cn23NE9ICqQ_fNVstB1KDdpTv43T9Vx0pFjiRQzkJdiat7vewJGUK6Sg0w5Zj7-kg9d9G56Uezjx_FZVBsnTnLDkXBzHZhAgT4O8aMJioevnug5_yS0yB_JiQdhBZ18Oo2rzxBVIYPc-tDVTYMru95d1Hsxuwh0cupHoFOmgPbnBbDiNDXLQk0ahCDm5m-j3PdFnnR8wbY6ovZcwho9GSAPsu5pwhjpwxWld5LD9g66o7lnNuCJt84rB0fgCMjKiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=EWNS9pFnR0N7SUe9-Gs150KAJcdQ6EZ1V_ctYhLNvwk-thDewcwy1b7lbGAZ_zJqNt7ZgAwpk-JmetYxaq9i4Cn23NE9ICqQ_fNVstB1KDdpTv43T9Vx0pFjiRQzkJdiat7vewJGUK6Sg0w5Zj7-kg9d9G56Uezjx_FZVBsnTnLDkXBzHZhAgT4O8aMJioevnug5_yS0yB_JiQdhBZ18Oo2rzxBVIYPc-tDVTYMru95d1Hsxuwh0cupHoFOmgPbnBbDiNDXLQk0ahCDm5m-j3PdFnnR8wbY6ovZcwho9GSAPsu5pwhjpwxWld5LD9g66o7lnNuCJt84rB0fgCMjKiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=o0XFAxTd34WlXChQwLEfAIJLa_uvyCAhWIDQwdvYpjnq4GksgyKERAkxmUIChYXdFZgQCeoLYupYdEEwo4NfJtfxAGmx443GEjXNpOohMPNkmZu9jveIisZN3Uf8PehiH3LXR_wTLw0eZ5LuEtDxtTI4RBUYz_93WcRxPHBPW2H4CHimw_iqKLqwF6MkuGMwWZo9n4IAhYaUNEIRuWxWd_Ccf1UtUsP9S0IT1pi3a1aKZFf6FBjIQKNwb09qV-a5FHnzDNuQdW3izYwdW9y7nB6uTjVxCEsrCD11vk16FBbADs3SBS5etwUg7tI7cfnQzT2BRyU0M1EKznd6dddb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=o0XFAxTd34WlXChQwLEfAIJLa_uvyCAhWIDQwdvYpjnq4GksgyKERAkxmUIChYXdFZgQCeoLYupYdEEwo4NfJtfxAGmx443GEjXNpOohMPNkmZu9jveIisZN3Uf8PehiH3LXR_wTLw0eZ5LuEtDxtTI4RBUYz_93WcRxPHBPW2H4CHimw_iqKLqwF6MkuGMwWZo9n4IAhYaUNEIRuWxWd_Ccf1UtUsP9S0IT1pi3a1aKZFf6FBjIQKNwb09qV-a5FHnzDNuQdW3izYwdW9y7nB6uTjVxCEsrCD11vk16FBbADs3SBS5etwUg7tI7cfnQzT2BRyU0M1EKznd6dddb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=iTuRhC7lTro8JPFI5ki-fqQZFyGvgRBj1fA8FCQb8lCSbXn_0IlQckUCYQ4ml_OcfO51T5SfehQR5GpkFfdEQsfCVLQkof-MJdTpC--G7binqcsiOcm3yJdO6BC37-DMrSsrBF8ylNWLwXKwdlo8I4w91DoFpS90GnHy2WifTiREkWBPils5HcEIpp68EXwPyrSjmsDVvlKwuDElmmaRNVEUnpVAfUcaOIxvpWYpq07b3JAIysBUACbeaksBtxkAzrDW1KuvZHe4pLI0afBsRLmNuYaud4C3I3G63cbZjJVcBjzqF90LVZ5BXe0sskL-zG_70tARuhmIOTpz-yM0DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=iTuRhC7lTro8JPFI5ki-fqQZFyGvgRBj1fA8FCQb8lCSbXn_0IlQckUCYQ4ml_OcfO51T5SfehQR5GpkFfdEQsfCVLQkof-MJdTpC--G7binqcsiOcm3yJdO6BC37-DMrSsrBF8ylNWLwXKwdlo8I4w91DoFpS90GnHy2WifTiREkWBPils5HcEIpp68EXwPyrSjmsDVvlKwuDElmmaRNVEUnpVAfUcaOIxvpWYpq07b3JAIysBUACbeaksBtxkAzrDW1KuvZHe4pLI0afBsRLmNuYaud4C3I3G63cbZjJVcBjzqF90LVZ5BXe0sskL-zG_70tARuhmIOTpz-yM0DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtzKniOuAtLpvaHH_vGIjWN-4zMn_B2J1F6MVFAEdZ7fr68c3-Mu-_74Bve4IAg6yL6gR_tqfI_8ZHEpLSPUB5gf4hPjIUVtgpa8jeKUnGhC-_KgM7TBeb4FbiavW7kBQsT2o1R4VeGZ43ekpcpcdtisQqBA782hj-DMaxt48gn8mUkd8YvhU5yGBKuNuHm_6Sm2skSgGKyBGowjCVhfCaN26wvSqyuRpPXfIiP2MdziVYPpJpYcUJq0VdXPpK8bmtIppBx0gXg7bXavprXas2lMiz0GPF2D1UiC7C-vRkfPVjDtQmDCsdAX1fCqrzzEk5VR47yZZ_CXjaiJMp1EBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=A1ksJgHCwnSjgFJ3BAQ0RQClNnNB1T_ikqdTDPG9yLeaf5XzsFzloofiP9PRyIMs1HTSSLiVGf5UzrPldUyB2g19kzigBcW9jSx86u2R7abVflFLfrTjVsV6Fco7aqLFTFTgPot6AEd_DdS6merPhECbQGVtG_fDNF1qFWs6nlxZlHH3tvg-BQSPXsEkvuZLR2kuYuESWS9gXCyQdfEGRqcfTBGbFyvgqsJ6giH2AOv5_YVZahJxo17KHkEVL21MQW3vPz4RTto6zF1pUwrCDQqguFPrlySm9zGdQjIkKPNIQk6p1RRnDAr-LzQNhptjAykCCMgI4MWuDCIV--WHPnJR9seNS5OWHKjS6Klg9i2EF8FtJeFRXCMDnwIt5xMksbmO6g4P0oP4_OUZe9rRgS9IipG3LvTTCi1A_OEUe92JBGnnYVdGvwSl8stoMdGWxeni73fMRA3p0ZQUsFribkdLnsRlOQY2yXs_QRNQGVQ8pm3yORKtBBVRFZJpON60Hmnp2Z77_IMAqZwQdwT0XPECfBxKMJGLuMcso03xivXw4jWMi7j2kIwrmscjM_eyrblj9G139hV9qE3ss_7nraT1lo6nrjry3-xhfG5-5im6EXrJ39RIB_U4ydKmp9nfN7M50koReCRGrEhdkMijdXQTG1akMOoh7oumlXQPl68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=A1ksJgHCwnSjgFJ3BAQ0RQClNnNB1T_ikqdTDPG9yLeaf5XzsFzloofiP9PRyIMs1HTSSLiVGf5UzrPldUyB2g19kzigBcW9jSx86u2R7abVflFLfrTjVsV6Fco7aqLFTFTgPot6AEd_DdS6merPhECbQGVtG_fDNF1qFWs6nlxZlHH3tvg-BQSPXsEkvuZLR2kuYuESWS9gXCyQdfEGRqcfTBGbFyvgqsJ6giH2AOv5_YVZahJxo17KHkEVL21MQW3vPz4RTto6zF1pUwrCDQqguFPrlySm9zGdQjIkKPNIQk6p1RRnDAr-LzQNhptjAykCCMgI4MWuDCIV--WHPnJR9seNS5OWHKjS6Klg9i2EF8FtJeFRXCMDnwIt5xMksbmO6g4P0oP4_OUZe9rRgS9IipG3LvTTCi1A_OEUe92JBGnnYVdGvwSl8stoMdGWxeni73fMRA3p0ZQUsFribkdLnsRlOQY2yXs_QRNQGVQ8pm3yORKtBBVRFZJpON60Hmnp2Z77_IMAqZwQdwT0XPECfBxKMJGLuMcso03xivXw4jWMi7j2kIwrmscjM_eyrblj9G139hV9qE3ss_7nraT1lo6nrjry3-xhfG5-5im6EXrJ39RIB_U4ydKmp9nfN7M50koReCRGrEhdkMijdXQTG1akMOoh7oumlXQPl68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=G3Ep7Q0qTIt0KEZJ0uKFR8_FdwB0ls6F2yw0zKYwc9p6FwPcfB5vsKgxpBdwYcI4UrOfQ0pHqSrgfccJ4wzwW0k_03Y0aJLmw3YyUK_rYNU5mRZ3eTNZUX8xLqV2GH6SBjKTo1EdkCc9YaAZcJGKob7QqamHmCEBvPVheZTyM3BfcpudM_jFCdOHDGhFg9Pcnd85aM5OdvHbbLPKzqFTeqZpecPbDofnIsSzurjhTuQeZj2y-AqDQeSI21pZmb0HTVKylVc86iekfgXSbFmN6orc6mnawHeqY4jw1O4Uk1kUMqvVRZgcv2_gIL0xz9jIxa5-uVDchvL5ySHUUuPw7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=G3Ep7Q0qTIt0KEZJ0uKFR8_FdwB0ls6F2yw0zKYwc9p6FwPcfB5vsKgxpBdwYcI4UrOfQ0pHqSrgfccJ4wzwW0k_03Y0aJLmw3YyUK_rYNU5mRZ3eTNZUX8xLqV2GH6SBjKTo1EdkCc9YaAZcJGKob7QqamHmCEBvPVheZTyM3BfcpudM_jFCdOHDGhFg9Pcnd85aM5OdvHbbLPKzqFTeqZpecPbDofnIsSzurjhTuQeZj2y-AqDQeSI21pZmb0HTVKylVc86iekfgXSbFmN6orc6mnawHeqY4jw1O4Uk1kUMqvVRZgcv2_gIL0xz9jIxa5-uVDchvL5ySHUUuPw7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjM35lolkpYIQVWGx-6j_I9AuVXxLdon3smGDhplOQnEliUVuQWGUx7Rme5FfI_aIttrNMWsd1-0HLeIA8bk8eNjgz7SpiQ2GtHMbmBc6nEi90NL_KBox19BEH2j-k0RVl1Aq56qjG7tdIpg6rVSkoLf7TFcXzIMXmtp6qqD81IB8AiQZNHHuKSB0xiVqQ67tTz32U1gw-w0T0X44sim4_SmXKBVI_pIjwt6CvRrWYGZiA9QTEJrZkOS2cWmeke87s-lg0oYMtPBZVz6jK_vT33-Ko3XigiFoxFoSv6CODjRD6ZVdJD5QAjIhzxLKJ7DHe4baJt77Z7ffPoYwNJp0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOh5y7I5vMznoFNPmgGw-7YuHSho9WHkjfbtov8mH-Al-UOubKhrVdKrAJGgFLdDb-tisrOXxU1VDn-ZWLMI4rE_kxZerteeKmXkctKBPh6wohwgss-Of_W6Gs6A9kdGd56gn7MhhDKDZy6ouS_KVq-IUvIb2cX7utWCBh_SwPTeOuDtXQAV6XnFndH2LIq5M6XUFp4PgQbsNeXp_eAY8ubTwp75Tetgd4B_FmfmDHbo4Dd0IL-CVyMAtFDtR9W1tZFZbfvA7jz3OYp-qao0sE8qpTnVF7yFr33hsVKULs6l0pyaXROY7TQ0EBiJNYuABvoEUkdFAKU086QxZT9edw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=aaksgqBB1CKn2NNo8GBwi-eBhKOwtUYWSaArwd3fGbuRq_9eOmfTRs1x3PXBDZengNnNXc99N_oikzIAea8JY2jnzZyKyIRKw1s4MkKVUISAArO9E0r2O3EOtIjNrlGVyavu7e2Dpd0AfO-7RKOz_TM07nCDdFNroPw8gtH8fKJzgSk2sz0_dxD7tN1JVHGYT6UV7ez1J5ZRpVgtEoFKSTJObqjDtZ3H_EyuIXVJ2R4Phccyvq5AtYDAwGsq44VXQY2kC9rVfszIlv04rlZfs-Jb_TkMngD07wzIKvh3E9WQ1WGVF7diFvmXAJwWWJWIEdamFyxwi0uYR8UIxC0Tig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=aaksgqBB1CKn2NNo8GBwi-eBhKOwtUYWSaArwd3fGbuRq_9eOmfTRs1x3PXBDZengNnNXc99N_oikzIAea8JY2jnzZyKyIRKw1s4MkKVUISAArO9E0r2O3EOtIjNrlGVyavu7e2Dpd0AfO-7RKOz_TM07nCDdFNroPw8gtH8fKJzgSk2sz0_dxD7tN1JVHGYT6UV7ez1J5ZRpVgtEoFKSTJObqjDtZ3H_EyuIXVJ2R4Phccyvq5AtYDAwGsq44VXQY2kC9rVfszIlv04rlZfs-Jb_TkMngD07wzIKvh3E9WQ1WGVF7diFvmXAJwWWJWIEdamFyxwi0uYR8UIxC0Tig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EdOJXREPhfs34d9U5J5jgWFM326NE5Hs3PBWdVgZ6YHXzIXrwdyr5ohz_HaLnd1nIW7R-MCCdYksig4DBWrReh6zKM1qx_Ij9RLE4jX1TAsGJaKjrQz4JKXCTCkYnEIo0Cpub-9mxdP8B6iy9CpB8ifuyLeO79Uj5zVObJyfl_0pVx_e93DYhAgPgp6XIpqp3sjz8JcEbgUNqcFp-44jgjzP3MEUytfiMjdDs5DLT8J_IMwisM059PmV91KFqk4JuSVF5QPDznVWAnJOoP33-3mQ2bNyaKhTstf7K-nLoBAR6EsAg1YEA0kU2MduRUKZr_YcUJbJwsxc0a2f5xNCGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ahcHwa135S8plNSmeFSzwA7I7EsjPmCgXCsFAs5wHEmZtTBrBiBJbc6aqmC5GYGVQFM1mfkK13U3Yd7Tz2QeyWwR2eaCOhdClhwX4PhZ2yXnj2qnTdlmupLSJEQC0qtBsB7QyGUxoAowPU5gpzbbuA_J2RWcIxL61p3OebnQ2mZfEXe641R9akPrH6j6I0FgdWmHJVqFPwKRBIiVh4OyUt5FUKQA3qjoG2L_qFZAQnWlbuigS-QwacKUhZz3WGxlbQkoFKDYBYCpwg9nwdrZAr-9SLz0NZbtvGp0jeHxQZSZbwSa1M4docOitl3zTbo--AEkJCMQVijTYhZ_tu50vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=q-yHv5qkQfQpTZPiUrpAhshHgZ9VPVDZeVdIrYWGMux1i8zN0SsVbO8CJNpVHKueQEi6p-eMe_E-9SQMStysN_ULPcbf70Vd_9OiH28T-H2o9hiYnrl-oMgLBY4M-cbyD84OnQAiyt4SwuZeFG_JWeRs_TascnINYzC-RxACXLCceWQ2XOt7zXmlgwwqUaBtiTFypxz6JnCG-xdBVorIk5Zct9BE2oxNaOL80LaA35Hgl7aL3ZSeKoXhO8SY_GXLjwCeGVNEVIV3KJPnpKBXAZ8m7Wx2dI6wWMCW7EZcn1jxq6aQ7z2gdrDAKISGKJ_jusbV1YkjVgakF5K7142snA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=q-yHv5qkQfQpTZPiUrpAhshHgZ9VPVDZeVdIrYWGMux1i8zN0SsVbO8CJNpVHKueQEi6p-eMe_E-9SQMStysN_ULPcbf70Vd_9OiH28T-H2o9hiYnrl-oMgLBY4M-cbyD84OnQAiyt4SwuZeFG_JWeRs_TascnINYzC-RxACXLCceWQ2XOt7zXmlgwwqUaBtiTFypxz6JnCG-xdBVorIk5Zct9BE2oxNaOL80LaA35Hgl7aL3ZSeKoXhO8SY_GXLjwCeGVNEVIV3KJPnpKBXAZ8m7Wx2dI6wWMCW7EZcn1jxq6aQ7z2gdrDAKISGKJ_jusbV1YkjVgakF5K7142snA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=tFc1tNfC7OSGeFY5S0bApsbOvOH_rXPwf3uNaCFQnHvxQwRp2g6eZyJkHAb1porNvvRIbWBNVHznwrNMytCch3GD5xuWIlQiVAGn3LGSWB9AWnX9dVJ2K3zXRPRuRWsBiNilDG8JU9ZSjm-4zoN7YZBPmxQYyfn0rKvt65iX3K9lebZVBZKMVHK--hLQd9qQkpYO6a1SXXULMVtNMThn1iTHrWom-wbpW6HYeY1Y99hDdPOCrkUvw8n7DO2vCZjLd-ckYZc7ELHmGrEHiKbmh8oNV0yBL2ocqfdt-0YqVjMfjFk0eBprGyzYkjVM4dX86taDzt1Smmpsch7zt9JLXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=tFc1tNfC7OSGeFY5S0bApsbOvOH_rXPwf3uNaCFQnHvxQwRp2g6eZyJkHAb1porNvvRIbWBNVHznwrNMytCch3GD5xuWIlQiVAGn3LGSWB9AWnX9dVJ2K3zXRPRuRWsBiNilDG8JU9ZSjm-4zoN7YZBPmxQYyfn0rKvt65iX3K9lebZVBZKMVHK--hLQd9qQkpYO6a1SXXULMVtNMThn1iTHrWom-wbpW6HYeY1Y99hDdPOCrkUvw8n7DO2vCZjLd-ckYZc7ELHmGrEHiKbmh8oNV0yBL2ocqfdt-0YqVjMfjFk0eBprGyzYkjVM4dX86taDzt1Smmpsch7zt9JLXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=WP6hio5ThQ7bwpc-umCXYqfPTsamTFaaRiho6xAL_74HLSw51t2zmEB_ypY_ZUNSVY9AFdAMZ69uo5lbKKXDz9ytY9rLUQ6KsQM1WdSGa07DkD2punl-mCsiaqtImoyHIrY10XXSOuTA0lvbhj8tbexyxbITnT_26P_G8ujMLmgIaBd_Hmtdm8AG9QF9He63FlDi6U5G6Md2QaExEzAe7rjwFZtxUVcdlggOnmtnLPiddC4fPkrRbhZf0nTj90eYI1hWlB56YaBtDVmQ3GuiVyi76eX_IdqrgAkg1zjc6vb1Q7TLOuEOUy3z7j45pKGNhrMWLFislTUH4MDwl-rrhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=WP6hio5ThQ7bwpc-umCXYqfPTsamTFaaRiho6xAL_74HLSw51t2zmEB_ypY_ZUNSVY9AFdAMZ69uo5lbKKXDz9ytY9rLUQ6KsQM1WdSGa07DkD2punl-mCsiaqtImoyHIrY10XXSOuTA0lvbhj8tbexyxbITnT_26P_G8ujMLmgIaBd_Hmtdm8AG9QF9He63FlDi6U5G6Md2QaExEzAe7rjwFZtxUVcdlggOnmtnLPiddC4fPkrRbhZf0nTj90eYI1hWlB56YaBtDVmQ3GuiVyi76eX_IdqrgAkg1zjc6vb1Q7TLOuEOUy3z7j45pKGNhrMWLFislTUH4MDwl-rrhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef2gZyPgFQw6IYIzak7lK7drZ2CwoTnEcFfDL6CB4Jm3cAT2O7ljCiuTszGw3VssVRvuDt3CgFknxNZkjbmXO4WysdZTDvsyzRUZyVollh77cwbTrH_F25VKOXJbLEqmuPa3Pt0ASup3Nl_zXREtRJC55vSOQwAdihDAdcCCvLSLAk_5hNyyT_Pz1erM-wsHaNhxN_85Ud5XXJi84h1shmu1zoDWMORvWEKp7CoOF_MCBBLMezjEuE0qDJn3iyw8ekxGyFpuQulH0ySs1V3cY5jnYQLO8ROjIe7hAOUWOUxn8ZHpRb9CkE8jk_yAkhWPZwEkIQd7CiHehumMKthu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBZVDXzMiZYJRXfuvZwtwksoNSpK3A8Iws3QA0P0TluyGc_7-2DQuSzCM3b0ZmeZnFD518vwLC17FNeHKlLx48uKVKPfIqXx0Ko7d_170joCT5dSFg4YWyCVfmJJqqCJzmVroLB3W3pv-qSdT30Qf2jEk-QGCpVRSIastJ-Aqg_xkyygRfUKCHzfbQjZmgwsFMK_DOR4-QgNpHLBiuq4EI9BwXO5PMsaG09odPicqYqBg40wl3ncNy_wVn545fjY8VVuG5XGZsR8pd7u8KOXouCjbIXFoj1qjzIKB4yoVpXJxJV3cdK9tKXne3YAvxaalPejbs9e9607n1blBCcy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=ZYOdv7IYoR9MhnJtgJ_OQi2p2qPL9WfXgmXxSAhTKdmFZbnT476Bk6KSa6pKfc9jqGt_ApXwHwdtNRARXRffP9elfZM0IF50SzNHceSdKXrAYAk--4rBlCKB30edJtAjILYxRKumNtWzQ28DqAfB4OI7wUC51TmePtoDhe8v6gvGca-VLDIi-ipYzyozvr-pOiYB93u3FetrxXIrDCedm2rg8LheXQRrBH2gJwoXeWT1_zhYkrJu21RrvL7cJTufwiLb97UYyMr0gr_LNFl-frUU4idnP7oFFI0MdDVzUwhhGN8qJOr16va7h2kvmozdNgbbANcX-QFZ687MDJIVbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=ZYOdv7IYoR9MhnJtgJ_OQi2p2qPL9WfXgmXxSAhTKdmFZbnT476Bk6KSa6pKfc9jqGt_ApXwHwdtNRARXRffP9elfZM0IF50SzNHceSdKXrAYAk--4rBlCKB30edJtAjILYxRKumNtWzQ28DqAfB4OI7wUC51TmePtoDhe8v6gvGca-VLDIi-ipYzyozvr-pOiYB93u3FetrxXIrDCedm2rg8LheXQRrBH2gJwoXeWT1_zhYkrJu21RrvL7cJTufwiLb97UYyMr0gr_LNFl-frUU4idnP7oFFI0MdDVzUwhhGN8qJOr16va7h2kvmozdNgbbANcX-QFZ687MDJIVbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=N51_BskzJV8cIQLdUpVwyU4EG8pPpb0NXUpkwmZCo2mk0y_2GoSmkrjKiRvQQIh9YcKiOpJBEZwh95maagPuUkJuW8whgHtF1bmpj0UosuOP_YfD2NUHu2cgqZaTvjl5okeChhdacD1zrArtmHvl3l2FsvLlkhGbTm76QntPR8FBkoBqlcM6e9LppYyVW3smSr9OEDBnrLk7QAl6WfL3sb2AxTqu27E1ik5HcRTYkFpUK4ywbQnei3ZLQ1SBmSmiqFoDhFe3llYaJ097H6WYDb6GaJRkzpeQduzR5mehQjq_Mp6_Eroqpsb8Rb8e9piSdSMg4hofoP5r73xoMIUyFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=N51_BskzJV8cIQLdUpVwyU4EG8pPpb0NXUpkwmZCo2mk0y_2GoSmkrjKiRvQQIh9YcKiOpJBEZwh95maagPuUkJuW8whgHtF1bmpj0UosuOP_YfD2NUHu2cgqZaTvjl5okeChhdacD1zrArtmHvl3l2FsvLlkhGbTm76QntPR8FBkoBqlcM6e9LppYyVW3smSr9OEDBnrLk7QAl6WfL3sb2AxTqu27E1ik5HcRTYkFpUK4ywbQnei3ZLQ1SBmSmiqFoDhFe3llYaJ097H6WYDb6GaJRkzpeQduzR5mehQjq_Mp6_Eroqpsb8Rb8e9piSdSMg4hofoP5r73xoMIUyFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qazjvH0WRxn7OMoKWktbxqEOgW8iwXkLY-B546qyE0d5o4b2-aHyHHHEduFAXy9DJoKi0ynGZt_gkOuxZ38pzfaowvU9JXl3tsewC4TEu3OLyCrC_i1bP0f-XKQ1sVjVKcVdRvAdoZdP_bEUnKkiWwvH12mzCFAETpFB092tuTM4GqZztLXFNyjI_v2aQ5tsMLJjBfUaI5zlhvCWsVkgKdh0pc078a6QcCev93Q_06nQ67T8LIVebQ8HIzZ9oMlYdRQwPf4iHizJRaGyuR8apYcHhPL89DDOKknIExoOdGznrm75vZGan3gI7zsKgH02iDvDM4tLC76fDCjgpaWP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=CzucZvEd0aJYZoce04z0FZ2y_TJ2cQ3NCzIdvi_HxUfGYzkLlD1XS27rmgFgeg9w5WJ3RxGORAvAAv4brURBeZ6w47SdF6iOWiwescRy0QzT5xf4fCElmIGW5PveVHmiu3-XAzo2q0FrwEEE5LkRQ4zFdoQfDeinjXJhRt_yZjdD9wbHd8D4TUaJfQ4LJmmk8pd9KLB0wcoqPEhj5C731MxSxESzZhwjQ4XWb19ehediVNLcASxzYAlkWalenOWFboWNM2hYycyGy4hSl-ipe2tR9f-UQ2KWD3govHmp7OOSOYjwfsgcAEpdFx86Yv35p2yRFP497ND0xZMMChFhyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=CzucZvEd0aJYZoce04z0FZ2y_TJ2cQ3NCzIdvi_HxUfGYzkLlD1XS27rmgFgeg9w5WJ3RxGORAvAAv4brURBeZ6w47SdF6iOWiwescRy0QzT5xf4fCElmIGW5PveVHmiu3-XAzo2q0FrwEEE5LkRQ4zFdoQfDeinjXJhRt_yZjdD9wbHd8D4TUaJfQ4LJmmk8pd9KLB0wcoqPEhj5C731MxSxESzZhwjQ4XWb19ehediVNLcASxzYAlkWalenOWFboWNM2hYycyGy4hSl-ipe2tR9f-UQ2KWD3govHmp7OOSOYjwfsgcAEpdFx86Yv35p2yRFP497ND0xZMMChFhyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwMewcr5ieN8aVfT5jIaBpsyEU1r8F8y-cFz-f6CA6LoUXtYUH7UL_XkGeaC9aM27D6pdkfrtjJ8sHxRYT_DvBLxuz9OlIbQqH_hQJBEFgpYzYXJTjrLmL9R1qSXvC-NZYas42y_RZpJWQq7ErDHtsXQiNK_xhmqgZO2CcYAmi36t8h6R9JyfoMCmIsi5U2ei65LsYqSXyOGAN3I1SY7ScktohtHIK_I9-sLU9iCwwcKmj5ceMxW3uQOLxqRzlwDIX99hKHY8_bwI_GLcSTPIcIL1djNMg4LbrkQAjto-oo-AHF8IRzS6UC8pKRFFIG7eWGJGBi-42JNUqIWblBwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xqyeqpau7VxEzXw0Vb6kt9Xao9KcxfoMjKDFBRtFIIejJbFLlihPKDOIMBHCIvWjf5DdDTMpy6XqyqxByzvrKQGOkDmYlemWcUlURZqM8OK92pGyuQ_dpGDrCQ4BVbBTctmw48W03weuJEY9mPqXkgD3e93secX3y6fHauATgewJktShGXSO17dxl398IR3PDYCIVCcqd3QB3VwL7kRupNTINvDR7tA1fsnjVOF3VkypLmFVTvSS0X3eNxMHRW-cO1EE8N4pN_G85y45JlzYMZ0CwMIAja9vX7YoiFlK0eruV_zFVxYVKSJheVDxkpMOeEsNypGkOusG8GeHEwMzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlqEWpDSTxKyy2cS5Lru0-MCbk5cQwmp6YzlrY8LwGlaZQ_fvQUH-xiarHFoP_RSLJTAOX6zLvmbXGZD9dGOH-STjWB1LstqMuYCp3Psl9B-JNBaKoccvkCJtKwuGyjzkGoSNZe8vaXjF0_vOj8zlPkvLUv7oz9KHlVOJh98P0YPwsRxRvcOP_0s4QT-pIJPPc5sSMQsN9JxC_ti9x9H7nvIutgV_-vdPV9ykaLgThSGxb1TIzQRGNRpggXLowFbhE90GkXsh9UssdCDiClVS74iWMnl4U7gN4eK7nagEOxiU4leYr0Q-JDOLY_VqQgH2a2ovxIYrEi8aTvsVjnABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=o4W27QLvAwgYQdYta4Va0DlrMpB2OfrziqZNd1-KlStCQIIRmTNmp0MfLPlf4NFEcTEHLBHWPc6iSB29DG4rIN3sSR8ZlQddWpBA2VgyWmOwgtrNAnq96UGa-OTK2hI_zT4s9pVkV8LyVG1DrYeqW4QsCrWOA9tkXump-U2A_7gPz93eLkhpb5jAZR_oDghmDtpedWSdm7mFpIWxW19lQYo3RWrwp-LZ-IgADyeLJE3qymVGwIvX24MztsgxQkDcuZY6wdyrA4F7zDt3Pe0f-dSfbzx61S-FVL2nlY4XkPdGUdSW3OpT4SV66lUDWW8DNCIBquz5Pxa4HUzDYYxc1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=o4W27QLvAwgYQdYta4Va0DlrMpB2OfrziqZNd1-KlStCQIIRmTNmp0MfLPlf4NFEcTEHLBHWPc6iSB29DG4rIN3sSR8ZlQddWpBA2VgyWmOwgtrNAnq96UGa-OTK2hI_zT4s9pVkV8LyVG1DrYeqW4QsCrWOA9tkXump-U2A_7gPz93eLkhpb5jAZR_oDghmDtpedWSdm7mFpIWxW19lQYo3RWrwp-LZ-IgADyeLJE3qymVGwIvX24MztsgxQkDcuZY6wdyrA4F7zDt3Pe0f-dSfbzx61S-FVL2nlY4XkPdGUdSW3OpT4SV66lUDWW8DNCIBquz5Pxa4HUzDYYxc1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKpNrmOT8DSPZpdwGiCZOA74jMXC7HSuoZ8d_-D164vzEMRlCTYrsf-uMQLmOFnMZoGD2Z9tGBVL_YxvsW2JgYdn77X9Vy6J8ZzwTq96iZ078F3aPXYx0iSo2Hgu8cZhj6iU3maopEmuL8m7KNK5UXMeGgW1LSkenyK5MG97UlhPyVAj-mSRd5-a0F7q8gjG5upKtvWKkbrVdqqx1Urye9H92ctASh1pfMcxD7ZP5tGlAn-ylAjGQOiNxYOJyCmaeZ4mxDiy8CulvNGWPzhMbAyWYOQYsYSROTHulkGCrf6YxT_AQC0Ct43D_lvhnqXIHsxqtwm36oJO07BEnwbPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=ZRFz7BfJGSVJnEO5wSCh8h0gHBnoJ2OHG9aLoPSWEouZZDtJh_eHmqVzlyEbAU9s3VGPVDhYMrBLMgjr8cxFEEBwurVAPDMW99gzeFRWwtOEY5Jp6W6t5HPoX-mwWv3nsfBkX6Di7mAWRYqlGDxdi3fuqRI45MK_KJaleaEBGPmgUm7PeUxTQ1MOuznGCcymVquTmkNjcMulsDqQQCvuyKeAr4xKDRe7YYX_WkUetQ0HD8fNardZelkz3mXH7VwFBYwEknaNaZlbJh34jlqvnrftTGgQVzZOVL5Rqwl6HnaVcO5CkQ5tFJpEZML06I1j9F8IhGgT6En9A3UysmjLag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=ZRFz7BfJGSVJnEO5wSCh8h0gHBnoJ2OHG9aLoPSWEouZZDtJh_eHmqVzlyEbAU9s3VGPVDhYMrBLMgjr8cxFEEBwurVAPDMW99gzeFRWwtOEY5Jp6W6t5HPoX-mwWv3nsfBkX6Di7mAWRYqlGDxdi3fuqRI45MK_KJaleaEBGPmgUm7PeUxTQ1MOuznGCcymVquTmkNjcMulsDqQQCvuyKeAr4xKDRe7YYX_WkUetQ0HD8fNardZelkz3mXH7VwFBYwEknaNaZlbJh34jlqvnrftTGgQVzZOVL5Rqwl6HnaVcO5CkQ5tFJpEZML06I1j9F8IhGgT6En9A3UysmjLag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=ILizK1vBUdGsQ2OnlNkfkPfpf1msCV5N98iisaVqRMiVenLl0Oox1Jgrr06i07EfCDecDyBHJpsVKAHfZO4OjNsGq5wxxCCF9FsVbWZfWO4jExZFiyYA4rufPY8MEw2eUh39Bh-Awl3w3JJDIOqR-gkH9YjLzR2_KQtILIKODtbi0geaaoLtnb-YmIGZTpHe2dFbOiox2CbBm0P1PBZkAKd63-SAvK_ao3UPOZZEqi9rp4mng3CP-yUI62TYfncvPiBg_WSrINdwSr8QXA9lTXYu-mPPXV_ZKs52iV_ekS0aJlds5xYBd2zcFcCW5o-Scko0JIzfCZMmxdvReP545w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=ILizK1vBUdGsQ2OnlNkfkPfpf1msCV5N98iisaVqRMiVenLl0Oox1Jgrr06i07EfCDecDyBHJpsVKAHfZO4OjNsGq5wxxCCF9FsVbWZfWO4jExZFiyYA4rufPY8MEw2eUh39Bh-Awl3w3JJDIOqR-gkH9YjLzR2_KQtILIKODtbi0geaaoLtnb-YmIGZTpHe2dFbOiox2CbBm0P1PBZkAKd63-SAvK_ao3UPOZZEqi9rp4mng3CP-yUI62TYfncvPiBg_WSrINdwSr8QXA9lTXYu-mPPXV_ZKs52iV_ekS0aJlds5xYBd2zcFcCW5o-Scko0JIzfCZMmxdvReP545w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNlSse40xg_OxB6tYkHKbezPjCyLoo6m5p_RfQDP_4_cHxd6l6-rnJownwZllbHpqKgOhSugUVLAzi3iV8NGsMnT3U2yVTI0IGQvLMPk_ESz5EeizBqoMSTfwAHwl-k32rV7OgD2Pa2Dvwy8XaqxCPsrMvVlmjHnc0Rhnf63SyjsCjKu8bgTeyfGUQ_LZOo4YLVlLOm8OwnmBJxD8cMp6iMTQjrIRu5mFDWUTXPLH_yyKjZf6UhHYogw1fyTQUWfGo7RqurQ3HojahvI2-IFDHDVCUfYgeaVpZpmXRpRmmKW92NO4ltmUwbmpcXiR-sDhHqdF-FmgZqHOHPfQJdHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=lEQ4mjdd3GbHQ2QAYe0fIwiKvmerxARlArrzaLEfbkrDfJ7_1kHdSrDhvbTm_JakiGrNNQrtnTpTAPgW00-cWhG_fJO4lCSEnCaN2qbCV1DSJcHdmlr0urpDpkNxnXldtWwv-5nJeevaZ-634FoT9O9WNJ7lF1RijyG58m4sLDecZMYgpH-yhH1PhMULGjo4vKjQSc8Bqh_cqSUaFKBnjL0IrzkSbAuiE0n9vDldtTPEj7NezK0_l5an79wdjdy0E0ccERsK_HRLCZvRdEakb3yP__2CGW0dkL9SxL7pR_EPlXmNwKS0jy77gBiFXstQgo-ylx5SsV3JmabD7vLgEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=lEQ4mjdd3GbHQ2QAYe0fIwiKvmerxARlArrzaLEfbkrDfJ7_1kHdSrDhvbTm_JakiGrNNQrtnTpTAPgW00-cWhG_fJO4lCSEnCaN2qbCV1DSJcHdmlr0urpDpkNxnXldtWwv-5nJeevaZ-634FoT9O9WNJ7lF1RijyG58m4sLDecZMYgpH-yhH1PhMULGjo4vKjQSc8Bqh_cqSUaFKBnjL0IrzkSbAuiE0n9vDldtTPEj7NezK0_l5an79wdjdy0E0ccERsK_HRLCZvRdEakb3yP__2CGW0dkL9SxL7pR_EPlXmNwKS0jy77gBiFXstQgo-ylx5SsV3JmabD7vLgEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=hqHL1uoVtCjRV-FCMwi2L6LlnluWh8DN-b69gsj65TaPhkB-t1SSsYoRaMPphN_zG7bRnE9dW3onYCACFQ2GkeuOtigZSOFGn2k_3sVOqqCF5UkzmzvDeJEmHHNpEe7CNVVqLUuC4ZB4b_wuvE2Uf3G6dVnFg4e2Qz_eZkQfhw5mKOQjTuHmhcblcEgy1ZSdc6aI81Rclo0CMXmL1bS8uLU6qWXGWTiqIlq10mtPRPNOFHRboCOH6-Z7RljO6rubPDlW5j8CEb-t4IN2RpAqo9AzyyFEvX2uC7Lg4BLJ47ekcX09j67AJ1MOzU7v93bG_dAroF1gGU8yOGZo8SuUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=hqHL1uoVtCjRV-FCMwi2L6LlnluWh8DN-b69gsj65TaPhkB-t1SSsYoRaMPphN_zG7bRnE9dW3onYCACFQ2GkeuOtigZSOFGn2k_3sVOqqCF5UkzmzvDeJEmHHNpEe7CNVVqLUuC4ZB4b_wuvE2Uf3G6dVnFg4e2Qz_eZkQfhw5mKOQjTuHmhcblcEgy1ZSdc6aI81Rclo0CMXmL1bS8uLU6qWXGWTiqIlq10mtPRPNOFHRboCOH6-Z7RljO6rubPDlW5j8CEb-t4IN2RpAqo9AzyyFEvX2uC7Lg4BLJ47ekcX09j67AJ1MOzU7v93bG_dAroF1gGU8yOGZo8SuUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=VxKXy9dELcksIaz2KVokWLvy8QH6BwlN-3LYWmXzTsJEQaNA8DoG2xLn-OFkXjPtaj7IkLo-Qqp1ZoLvSGfjKBGjx0vFHRZ5drXGYSYjK-QRK0lCzngVY4PoZnnSSEFyCoGKgeHOQAYfFnrLlpFxQKXi-fXvvOH0_bcLEyqY8-JpCsQpb6h7Fd-RwTq09XP9IZ_2zpApJ1dzPO06PFeDEszvVkcP2RBiUPTV4SWoPv9qgD0FwQEn1gcoxptp8lLn8p7H-mU4ge-d-3BMg_WOVGhfOaztWFZ1jqic5eitoNhfYZgSGHgnS-iHLKpNkKIT6RUnLidflcZO1nhD_eZx9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=VxKXy9dELcksIaz2KVokWLvy8QH6BwlN-3LYWmXzTsJEQaNA8DoG2xLn-OFkXjPtaj7IkLo-Qqp1ZoLvSGfjKBGjx0vFHRZ5drXGYSYjK-QRK0lCzngVY4PoZnnSSEFyCoGKgeHOQAYfFnrLlpFxQKXi-fXvvOH0_bcLEyqY8-JpCsQpb6h7Fd-RwTq09XP9IZ_2zpApJ1dzPO06PFeDEszvVkcP2RBiUPTV4SWoPv9qgD0FwQEn1gcoxptp8lLn8p7H-mU4ge-d-3BMg_WOVGhfOaztWFZ1jqic5eitoNhfYZgSGHgnS-iHLKpNkKIT6RUnLidflcZO1nhD_eZx9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=bnTe9JhNpw4SY1ggFsBqXa001itgONAVcHYFQ1_aFSDMheCN4gHkILieClj9whfBBFV_yMRp_oW496Kk_02tikTVa7haijTIjZYMAuKZ4OIFWnhuzqDAHQ8YQzuUM-3N28wR3INheclQ8w8rHYO3GMdhsnUZsnfNnMcYpYcR71QIDfcMOtZpgt2HneNScKpFcQtU7Z6LuBvsSeu_mRMVsJC-BWYA6r9ng8x-7_yCxzT2hO47TR2x3Z-enG1HN1zrq4aX0BFzU5f5XqTb_omABDfEZXGPilmugeJY7OdoyphCUYqxaMZ31gwt7aGwM9Ck1fq4L-APVgDPVgPMvuCSsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=bnTe9JhNpw4SY1ggFsBqXa001itgONAVcHYFQ1_aFSDMheCN4gHkILieClj9whfBBFV_yMRp_oW496Kk_02tikTVa7haijTIjZYMAuKZ4OIFWnhuzqDAHQ8YQzuUM-3N28wR3INheclQ8w8rHYO3GMdhsnUZsnfNnMcYpYcR71QIDfcMOtZpgt2HneNScKpFcQtU7Z6LuBvsSeu_mRMVsJC-BWYA6r9ng8x-7_yCxzT2hO47TR2x3Z-enG1HN1zrq4aX0BFzU5f5XqTb_omABDfEZXGPilmugeJY7OdoyphCUYqxaMZ31gwt7aGwM9Ck1fq4L-APVgDPVgPMvuCSsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=NcKVPjCGUEdoKA8JfwTIal6zeT77V9CEFUjeuUWZ1ZRRqxILJWLRYQxrds32_qW2Ar1ysKSw_1xyGYyKvyV7B64y1Xlbsf6rPk3ur0Ib7SxNDmhTmwJp7LqxkMVpfdfchq1GEnPPUu13UXH39BckTwhvMvkPZGWqKy-Bn3RyGRIGPC3scx85FfvKC0Ae8r6FWyz4_QxIGBl3IW7xxVAytQdqISfqnj0KJm07IjZaz0nmVVss2p3dUIHW-82CovwKh9coxGSuSZc3xwviOJqoMfotFRAje4w3pQq2QeTcJqqa119pHjYX3waFmLZRFerhAhXYKkBkeKRu1WpfoXS7cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=NcKVPjCGUEdoKA8JfwTIal6zeT77V9CEFUjeuUWZ1ZRRqxILJWLRYQxrds32_qW2Ar1ysKSw_1xyGYyKvyV7B64y1Xlbsf6rPk3ur0Ib7SxNDmhTmwJp7LqxkMVpfdfchq1GEnPPUu13UXH39BckTwhvMvkPZGWqKy-Bn3RyGRIGPC3scx85FfvKC0Ae8r6FWyz4_QxIGBl3IW7xxVAytQdqISfqnj0KJm07IjZaz0nmVVss2p3dUIHW-82CovwKh9coxGSuSZc3xwviOJqoMfotFRAje4w3pQq2QeTcJqqa119pHjYX3waFmLZRFerhAhXYKkBkeKRu1WpfoXS7cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHIA1SjYMgcH7aosUgNfNWOhYUzajegx3zSJb3z5h4uqro41b9Oyxawrj40CfHG8CydS6IRL8S5x3KVJGgNoGFm2XKzftPjxS9MF98geJfo6jOEHFyE2Tg0Li6woqTV2_Nr36Kw7WgZaTaLPKJLjoJcwPGVI-jtwfv7nKu0pirqdKur-3KvBow0_NI2LvqFW40-hiZZAYL2wyKAJXA_KY4xWCCp_WELIJOyfqlPm0htj2_lv_BqTPvALavOSXYgBGYFCC2XbE0wz6h_DH7VKbgPowe9_oevMzB3SBNeDTKmTwzomsSLGf5Zv8PSHEwx25kgss3fAv0RVlGYDTJenJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=h044BC6AVTPgi6ZTq4Qf6-agrJgqgBfxbo0gkwUkqHFMYwG1eRQlj8dX7Y1k6YkXeZLP46sEahkH4gYMVjc_N-OURYrWYHf3mTfUobdgQ3I80VbkfHwGgJABhZSKjrM3uuK2xD2_qC2D2QPNwZdB7hROj9WsQYtPO225Nr4FD7UT5gPzHekSkBS5o-5sDztTpSdtyXhYkKA7U25DfF3XbNcEmoaYKwo51_LUt9A2LUTa--3rQZGTvtg9SYpcxsPMsVUuiw_yu_kMTQW9mg0PSdaOfqi4JVLbmuwS4mu96Vu90PKwCcVj-I14vbc68xFZ0_fM3IuqqFmgeZlJX9c5EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=h044BC6AVTPgi6ZTq4Qf6-agrJgqgBfxbo0gkwUkqHFMYwG1eRQlj8dX7Y1k6YkXeZLP46sEahkH4gYMVjc_N-OURYrWYHf3mTfUobdgQ3I80VbkfHwGgJABhZSKjrM3uuK2xD2_qC2D2QPNwZdB7hROj9WsQYtPO225Nr4FD7UT5gPzHekSkBS5o-5sDztTpSdtyXhYkKA7U25DfF3XbNcEmoaYKwo51_LUt9A2LUTa--3rQZGTvtg9SYpcxsPMsVUuiw_yu_kMTQW9mg0PSdaOfqi4JVLbmuwS4mu96Vu90PKwCcVj-I14vbc68xFZ0_fM3IuqqFmgeZlJX9c5EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MioXY0mYW3NkDZwdJ08j98nk_Ij6zAvm0BWdF2M5LQpi4w3h5pTFZLU32PVMvIP8dHO3PjanJ7asL785oYueRO6i8xqdWV9x1WRs518OK4lhJ6ZrTvdRSaPXJ35v_j8ZNAzbfVxASdSHLCiSW3mMKaYwBeVYVqJb5dOs-EKLtCrbhgB_2ZgXCsPSULNES5dW08vF95wNvx4hmFa5sUuiT27faK5IUoF1AMDeeQZdWk1FqoTvcW5BrmQIDFuHuc3TW1gSp3i8ZqjVHlJrbW3oXhmj_jtGBx4tJC0Tvubn29mUtKDqW3DsdXNjcWGK9GeUBLbm6BrSbqOK64SDwWRdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=iTz5bZ66Kxml5NDdDBgJ2zZZTVwXW3ZY4mn8y41LWYOmATK4KlxmPoNEXYuj84F8KEp7IbiNBtDyWvdw8poM6HUWF_K3WwGxyozoZKfnczngJb46RuX751KIWONFkQxzvuRnpJpeYahIML_-Ii1PZMzSC3gM3VisY8n7abJoWpbAopwmYh0qvwO7LsFP8EezD4JMYMG91NubA3-r_IX56zup-9CcFH-JAhtn3TC-JvIq47GmR6RKm44v444MfwIWw6Sg4hMosySdC3xBiCMRVB2GvElpgpwOSiUEN92lmxkZ95vZDYLMAmO3IOZZH27ynNCn4vRtkkpkxsimKG2xAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=iTz5bZ66Kxml5NDdDBgJ2zZZTVwXW3ZY4mn8y41LWYOmATK4KlxmPoNEXYuj84F8KEp7IbiNBtDyWvdw8poM6HUWF_K3WwGxyozoZKfnczngJb46RuX751KIWONFkQxzvuRnpJpeYahIML_-Ii1PZMzSC3gM3VisY8n7abJoWpbAopwmYh0qvwO7LsFP8EezD4JMYMG91NubA3-r_IX56zup-9CcFH-JAhtn3TC-JvIq47GmR6RKm44v444MfwIWw6Sg4hMosySdC3xBiCMRVB2GvElpgpwOSiUEN92lmxkZ95vZDYLMAmO3IOZZH27ynNCn4vRtkkpkxsimKG2xAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=YXJdSXl6abOJB4TqHfkf3e13hLli3vcUYI4roHqcQDlXxklKw5AWvbe_G8FXoJHvK0WHD-JiTShAVV4ymze3Rnuz2FraiaEfFLLiGpABahnKUMZuWyW-7Dl8Z0qSvptfJ6eQqp8ndwHMg0kEZ5m2muQWkLTP-zs0dE0-uoJvSoFjNRMP6KTM1YTK7ka1ASaCTLvF8L64G5gI5GjSEAb_1-m4j86BzoQhAM1fLSND3a-acd2x06X-YEOAshElr0eszYQ7b1GJ5iS2adgNkm5abvzVFtY5Gl0MhuMMgkFFACoHFdIvt6HOBFsHxjhf-ZR64HCx89jhDOwG_3lXN9yTtYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=YXJdSXl6abOJB4TqHfkf3e13hLli3vcUYI4roHqcQDlXxklKw5AWvbe_G8FXoJHvK0WHD-JiTShAVV4ymze3Rnuz2FraiaEfFLLiGpABahnKUMZuWyW-7Dl8Z0qSvptfJ6eQqp8ndwHMg0kEZ5m2muQWkLTP-zs0dE0-uoJvSoFjNRMP6KTM1YTK7ka1ASaCTLvF8L64G5gI5GjSEAb_1-m4j86BzoQhAM1fLSND3a-acd2x06X-YEOAshElr0eszYQ7b1GJ5iS2adgNkm5abvzVFtY5Gl0MhuMMgkFFACoHFdIvt6HOBFsHxjhf-ZR64HCx89jhDOwG_3lXN9yTtYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=sddDWJVXKQCv67a1vfUrnPO0VGDjZigMxU-FWPGEOEZLNltz3pmq3Oz4t-Ja2CS6R2UUSoZcuKeS62VEFwH8_ax52B5ngQ68FO3OFsFtZaDs9yrmCxguLInVKDUVQvI1lk3EkFjzNwmOPlHBaYP8frdJfXC9NOIK8ePu9CqprRz8StotwXZET46HZjBYQBkcMnYwCWCgtAUqqTIhQ1JWtosZjLMZPkJX3Ot2KVDqidS3Etmnhht0GewV5vCsSiJ95T0TLqumt13er-VodzczVvSYagO-1wuEv13rV3Xf4D6t3CrBEbH0vjCjT9gS76dg-8SUyjUnpzcJF3xILPODTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=sddDWJVXKQCv67a1vfUrnPO0VGDjZigMxU-FWPGEOEZLNltz3pmq3Oz4t-Ja2CS6R2UUSoZcuKeS62VEFwH8_ax52B5ngQ68FO3OFsFtZaDs9yrmCxguLInVKDUVQvI1lk3EkFjzNwmOPlHBaYP8frdJfXC9NOIK8ePu9CqprRz8StotwXZET46HZjBYQBkcMnYwCWCgtAUqqTIhQ1JWtosZjLMZPkJX3Ot2KVDqidS3Etmnhht0GewV5vCsSiJ95T0TLqumt13er-VodzczVvSYagO-1wuEv13rV3Xf4D6t3CrBEbH0vjCjT9gS76dg-8SUyjUnpzcJF3xILPODTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=jg4b5yokgkBkDDaJNzaikNv8tqLK69v5z4_7eaaNM038PnL1-SXeWj9Df542xyscZ9qMi3mhdVqxG4ryfH9BfKkf2PS84y2rgYn-WUKL3TLAh5Qyzs8-_RPHoMope7Rok4u98QNtEstcRN6zCVkt7wbrnqyxtGyLuufv0LVkl1Hae7gnbOmV08llRfpwj8WFO-RxvvttftC-GhdBWwdiBWDfl9VddXl69blpxVxBXWPSHjll1G8xG2s_YGkoc_zU0uXtuhg6gKUrWW7MSx-IalhJ-aYHF_qoJLS4mGofhaWrROlzMy5o7JPaxlIOwHY-PeWtdDN9MzrwHbDycghXc2wTTB-QsgW-f7NZNrG9ZsU40nDH066-unQE5o-wEmGJZMnzpTZvt0Xfg1T2KCj7hE23hXoTLY71m9HTiHITtE6CvMtfzxau3v0ISeZ17CqCgFhPDFidpBKqaBL_ntDu1sY1dOZTBUs1ZeFFGRM4r6RleT1Xm2ZrGlXVoQ2Wxl6KPFJheFM681xjWWWsjGVbYxvrPqsQLmaciTyEqK-I_MaqG9QPl5NRayu8jKfynf55vlDay5uFbVDmQoJjCiqowkGXNsv2RZVCYsNJH1JMYhKpcL9CfNDTNV9B5kbc60euDuuO5UvqajM2_NssEbo8WHNMxQtUnbEgh1y_Sm5fqnU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=jg4b5yokgkBkDDaJNzaikNv8tqLK69v5z4_7eaaNM038PnL1-SXeWj9Df542xyscZ9qMi3mhdVqxG4ryfH9BfKkf2PS84y2rgYn-WUKL3TLAh5Qyzs8-_RPHoMope7Rok4u98QNtEstcRN6zCVkt7wbrnqyxtGyLuufv0LVkl1Hae7gnbOmV08llRfpwj8WFO-RxvvttftC-GhdBWwdiBWDfl9VddXl69blpxVxBXWPSHjll1G8xG2s_YGkoc_zU0uXtuhg6gKUrWW7MSx-IalhJ-aYHF_qoJLS4mGofhaWrROlzMy5o7JPaxlIOwHY-PeWtdDN9MzrwHbDycghXc2wTTB-QsgW-f7NZNrG9ZsU40nDH066-unQE5o-wEmGJZMnzpTZvt0Xfg1T2KCj7hE23hXoTLY71m9HTiHITtE6CvMtfzxau3v0ISeZ17CqCgFhPDFidpBKqaBL_ntDu1sY1dOZTBUs1ZeFFGRM4r6RleT1Xm2ZrGlXVoQ2Wxl6KPFJheFM681xjWWWsjGVbYxvrPqsQLmaciTyEqK-I_MaqG9QPl5NRayu8jKfynf55vlDay5uFbVDmQoJjCiqowkGXNsv2RZVCYsNJH1JMYhKpcL9CfNDTNV9B5kbc60euDuuO5UvqajM2_NssEbo8WHNMxQtUnbEgh1y_Sm5fqnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK0AfXGT8JQ9TzxAc_mxP8QfbZsmXI2eZYa4Z7_HuSRo6aTRKbrSnNt7pcsp83q7NiQ2d59--Bcv_oN7_1lhoVmlDQ-HAHs8pguKUftRZzp0TZhTlBPRU5aaTCRr-6HMjPpKbnrs6dmNvl7TvEh8CeIApU4HqBMFEHvfxMxlaB2myt8yWejYaKS8fhBwLOsRoqzDiuinO9FKNfdimOAneEcqXl6wNCkVETr5ji33WC3Nm0qc7sxTDvDY1VYl8idi2H4-C--iIpN5IRI8dZKj9zRPmsAKAi6foCAOyLghSpc5d8ihWd1dQoo8yTF7Cz75sRUdpiHEIVBr4NT48QJ8pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=r5HWyHxFH5vAHsVHX6mmV52yhPLsheqG0uJjLdocohjNdG6ezgRvQrKEqmQFvIiaXhBQ50z07sP01JTEFF9vxCcBd9iI5GJkQz98DvsuMJBreie_Wuk_MSKODt2u-1TXUpP_TU-MVqy03O1iTTXpuo9wZRfNFwVQlK3uUZKEJnwfdm0q00CxK1yFROnabqNhaszhKAEt4Ylw1bZx1-7PeKTvhJJX1i0Rz7SZQziXI0BToJ-ZN9BXhp2zsdgUJ9O0N1LSGsFZtwjYmgH5lvZ4R-ZdRGy1IL55MrFIOd_v5FsHJ8fThbeEuvI7nY4qrYwZiBXbYcKVlfRus89S2u95yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=r5HWyHxFH5vAHsVHX6mmV52yhPLsheqG0uJjLdocohjNdG6ezgRvQrKEqmQFvIiaXhBQ50z07sP01JTEFF9vxCcBd9iI5GJkQz98DvsuMJBreie_Wuk_MSKODt2u-1TXUpP_TU-MVqy03O1iTTXpuo9wZRfNFwVQlK3uUZKEJnwfdm0q00CxK1yFROnabqNhaszhKAEt4Ylw1bZx1-7PeKTvhJJX1i0Rz7SZQziXI0BToJ-ZN9BXhp2zsdgUJ9O0N1LSGsFZtwjYmgH5lvZ4R-ZdRGy1IL55MrFIOd_v5FsHJ8fThbeEuvI7nY4qrYwZiBXbYcKVlfRus89S2u95yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWziRqOq-aDIj61NqRC7ydHpw1faCxNwbFjBujN2UNYa6Fjtz1qywBQ9Bu52fJ4br54QvOedk22-U2-HdJH4CW0Fs04P492MNHEBpw1bvNfF_v_2HylI-Is6r0Hv1Vab-eXhP9Bit3cMDlZ0bhsJtRWSziEcfvE8GKtR5YHF2RpbpKUDfdc0BiANCc--Hv3AscXYVB7fpU7hFIuJi_tq4AnKdc3RDBF53ujU51AxRICJdcAlJx-nUrlLtpvLYSI1wTh1LaXwGcq4WT0e2rJczQKsAhUevbRKSZRykq5p8_vY2chCJkmRrYFPMgYU_2f-swsgUGMSgY_2kyipKEDelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMMgtJCCCOhFp4yuhR_ozU3rHZeA7WUrGKYsIYIKzwT_8l6Rh7OUA6GVJ-SkQi5hiyoxzuFhcAAPkGDRej-NRQjQk0Du4wKiV5pq4P3dSnlf2xbDCREoQiEqGdMbb9uVa6bclFaM3AFtIWUJNqNmt2NMQAoWaiV5oQdr3ok08dVFssvWztGR1da8IOacpkcIYe_Tw7WfHIt-cRlEbOPsW2VjuT_FDBaxFQzsFdFZLi0bjUnMSU5Yf-QGjjC8bklmzahr1mHQU1Ey4xs4BmXuUMiCYU4W__4lXX9kdp20Z4GLkAF90d6usRRArXNzG0pps3dnjHh19ZLDJ9jjXeHRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FICBIYuOjmruqaPhCj8SofnSfp6aBZBvUmO_zloAsg9WeNzPVWZb3G0kGD7FyS44SBJtpyLJ07-NoxJaxoHXZq3UWqAEctvayEH22VdnVNlDc1l9_as_Hg-bYDeeRM8YnKmlqdPNkyD4y9At77VLStrGm0oFXGArztIHmTzC93mM1G8aIF9A-3QP-8IuAS1ssXHxX0EgVLKWlucx2I8E4k_bS-J0o-aoGZiFykvk4gJtspCz7Lg7l1HY2kx8rNC9JgiPHrWlzVAo3LvLtaMWAL6Wi0_oruT2ajWmGXBzdYa_W9SbCP_DM_ATF_rhYW4kWGlhIEyeEZZBvtWTth7KHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXlVpjH2xYfy1sLKw7f9A87vXCDrxa_7rSZwbXQlOFOKSN6Q8VHlSmewTr3PaP-ShcFHBV3jLHyp9DB8d9ReCnWnEbbRHjhNATQX-DgVA2HjWpQGsARuqGtzqXGYZgHrlguFZ4yNaEkji_0nhOqD98SM1lGKwKGqeqmzqnBSarYeMuE7TVMaQ7N-LxanN8PBkJjoWTMC_9VcNd4dNCdECegoteNh6G4Kw_mz_Kx5puvmSFl8NLhh2sEUlngtamrmix0Q1kffWJUFrscdIQ8Sr336lUucs_mlePLuL9fjKYPOYgaSr3xem8BU0LZ2YEj6R1dJ7SxQpMMls8qgn6bPVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBXTme8FVZKTL4pXsqLE9bGajkpP-XsqMjScYRuO2RilPXuVrUg34gxqwfUplLvb4Xv6Rv2Pf49kPFp6CnhwrB6G3fL1a-NzmfgvzY0_1f_N0RBKIKYhNK5tPpSKnaU84pTyi3As_kzPMFhChdsK2y0dFaHR450ihA4xb8-SmkFkYnUBPSxRCvqLT2Z16Is5ZL1rqnUZdVpKBk7PPocpdxWI4SKK4PBajDkO6LsDJQDoUUr4zTambl9-kUFSA5tMeROY-4w_qMex9CT6-KW0CQNtgqh1Dqk1a3NQ-62DluAI967c_846DvEQ8fFo8GOS935WZUxVVFbbRQgL1SeT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIfsaEDgeJ2s01nHdM6tf7a82Q3cGBiEO_tAPZB60pixIZiOYN4l9iJomzAZaCRfO6t4RbiHNLYazHYGIyHjRqO_5KhiC7UqPVY6FmwjPMFvlqGZUlC4wbUapIWiTmnFKfkKRBYlbEj43rV3H9JUzvgFnrFsVLw2G-S-8Nmxc2dTvXyeKhGNtE8ekfzwv_et9uaG9dwOdBB1peLhO7gSVJcSbOVzRjKiRUjy5i-YfZSmb0x6CJ98zOTTaVE7JWKpNasg1he4MbQZZJKn9cTDI7TyCk0ePLINYaoQZ3vheP1VbP8iMpgExWGZbMvx9ZCKnWMSanVu_Yvr9m5fKHv2kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=idrc8RGo5MiIyk1sI-grLwTdarbSDxo4e1MEx1r40ILyo5mFtQ9UFCjjvVEB5FuoXRrmtZSYXpUD8wHCrDtr8C8ASh5ezsn7-BGF5rGcEepC7szKWhcfBPGsltyIbAKYlLddhWQbdbK5-9CDm-Xmo6a4Ow1-tCMlCCpme-jmYqZdozA0jwHZPLWMxvDDB5Qfvg7Eaxx2wpCkn1CI9N6FjTTN6MYy2u33jfQiWi9_M6l5LAWDYBoSt8JEGOdQ9AnZO7XepjIVup6aWr82fc3P089uTSpyHnywS7BM8yP1OGFvf7V32fPOVi4BGhN2lMvXe9AIIy1R1AXBobsQ5B_tMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=idrc8RGo5MiIyk1sI-grLwTdarbSDxo4e1MEx1r40ILyo5mFtQ9UFCjjvVEB5FuoXRrmtZSYXpUD8wHCrDtr8C8ASh5ezsn7-BGF5rGcEepC7szKWhcfBPGsltyIbAKYlLddhWQbdbK5-9CDm-Xmo6a4Ow1-tCMlCCpme-jmYqZdozA0jwHZPLWMxvDDB5Qfvg7Eaxx2wpCkn1CI9N6FjTTN6MYy2u33jfQiWi9_M6l5LAWDYBoSt8JEGOdQ9AnZO7XepjIVup6aWr82fc3P089uTSpyHnywS7BM8yP1OGFvf7V32fPOVi4BGhN2lMvXe9AIIy1R1AXBobsQ5B_tMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=T7TgubBB_YrK81Fu1UVy2EdxFoDu0zO504s0co3jLZkssh78mxJkzBJ2iwWKOnDkGMTfI0o38JNIVj9PFTmCZfiC345UpY8MITvhZp_ZPWeJMqi12fQIjhcpslGu6-oMmPNrQFc4tju95PDzQ7QHMc1XI1HBayIEQv72Jzq0F45e2w8dSiacFsDKc9Cq4lSXtZDHD0mi20tRsQViO3YEXu_j1le6YECSu07YVbUaGNNN_5j1G7dCA58BkbpXzfQRUbZGkeYFed18Cj1iAF6LvVK0KBp2MOK-kf2qCe_FVK2yDvG5ozpFv0eT_itAiovlnF4ZWZzA_AUGD-v77NikSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=T7TgubBB_YrK81Fu1UVy2EdxFoDu0zO504s0co3jLZkssh78mxJkzBJ2iwWKOnDkGMTfI0o38JNIVj9PFTmCZfiC345UpY8MITvhZp_ZPWeJMqi12fQIjhcpslGu6-oMmPNrQFc4tju95PDzQ7QHMc1XI1HBayIEQv72Jzq0F45e2w8dSiacFsDKc9Cq4lSXtZDHD0mi20tRsQViO3YEXu_j1le6YECSu07YVbUaGNNN_5j1G7dCA58BkbpXzfQRUbZGkeYFed18Cj1iAF6LvVK0KBp2MOK-kf2qCe_FVK2yDvG5ozpFv0eT_itAiovlnF4ZWZzA_AUGD-v77NikSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=FOvSppsfStXzjM4EWzph6wHNGRjxa3Effgf-CCC2yXfWf-8jNK3GWplrCvmPm4HSwO3TNkeLalo608okdvAVn34f0t7406pO-GzVP6iIf578rL1XS8qjMTLbExrrJSIYQjxOb3Nfx5pUhE_ProVoGUY-_SGHyN6hEfpTAoOd9eRWTQnk6oaB5_mvDmfmdmjYQW1CUjdhESePnnLqgQIWrr-VG9HUnyVZi6BRXETVawzAV2ohsmubgsHdDyvl6QoTpmt-azB5pz6MkvpbUwfMTEabsJx-Ld61BeMM6a7AmBCAkNoCGcImKAisw3HCagdjbGUY4dHZ4JxsNJM1ksJhZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=FOvSppsfStXzjM4EWzph6wHNGRjxa3Effgf-CCC2yXfWf-8jNK3GWplrCvmPm4HSwO3TNkeLalo608okdvAVn34f0t7406pO-GzVP6iIf578rL1XS8qjMTLbExrrJSIYQjxOb3Nfx5pUhE_ProVoGUY-_SGHyN6hEfpTAoOd9eRWTQnk6oaB5_mvDmfmdmjYQW1CUjdhESePnnLqgQIWrr-VG9HUnyVZi6BRXETVawzAV2ohsmubgsHdDyvl6QoTpmt-azB5pz6MkvpbUwfMTEabsJx-Ld61BeMM6a7AmBCAkNoCGcImKAisw3HCagdjbGUY4dHZ4JxsNJM1ksJhZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=A6zHS38vkM1y8EN4K2LWSrwzcpLErXjvQR4w7gUq9sJXHYgp4YytcBHEArHlHCpJVw6-2DVEXsX9VUnl4lMdEQcYyfHGVosqesJfhCCrY8SAmqp8xZFFvBV_NdiQMq29SJXI5aGaJXMooGlQN-FWcouiFlLiL35UWvUR_Bom_XO65TrFYq0meV7BXsxZhxl45eULXBv1s44sWDVpD6IWjLTrWx6HkfXAvBfjFC3EmOKxgOFD0OEsjqeO4RhkOs205XEOsaeSOF5FRfYFZS_YqH7TSK-vF44_VXcvzOUIIcbAQj9a9Yi9nh5IC7GB9wdBXCrorJ8F2uV5H1g_vFv2fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=A6zHS38vkM1y8EN4K2LWSrwzcpLErXjvQR4w7gUq9sJXHYgp4YytcBHEArHlHCpJVw6-2DVEXsX9VUnl4lMdEQcYyfHGVosqesJfhCCrY8SAmqp8xZFFvBV_NdiQMq29SJXI5aGaJXMooGlQN-FWcouiFlLiL35UWvUR_Bom_XO65TrFYq0meV7BXsxZhxl45eULXBv1s44sWDVpD6IWjLTrWx6HkfXAvBfjFC3EmOKxgOFD0OEsjqeO4RhkOs205XEOsaeSOF5FRfYFZS_YqH7TSK-vF44_VXcvzOUIIcbAQj9a9Yi9nh5IC7GB9wdBXCrorJ8F2uV5H1g_vFv2fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=o3dZs1jMwPt5nhsEZ3s0axhs4eAJ3zPUTfLhtPN3A-IQQaKe8zPAP5MhXu-VnOS_Bo2wrZwvtVdH4lE1TeA8uoHBgsW-Mt25XCzrH0Z5XGKmbHI3Eg9lwAgeUPhRIJRFi650G-5kW3quVRmV8bW-y0Ny3ODIGuMVmzqU659pawN4SKorxz7jQmj6p-H5zSb6kEyVB_hM30wyc88HZ5PCgsEt5hW2c_jKSvjkDMvaJEHYkUaQJ0LrVFP1jzcUq8RU4leKHfqHKNXhWmScQWavLAcLHa5GburaoQin_xrlTfMUWUlCL6KolGK1ZBWA4x9e1hHxUORkISo2y7kk9F-Bww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=o3dZs1jMwPt5nhsEZ3s0axhs4eAJ3zPUTfLhtPN3A-IQQaKe8zPAP5MhXu-VnOS_Bo2wrZwvtVdH4lE1TeA8uoHBgsW-Mt25XCzrH0Z5XGKmbHI3Eg9lwAgeUPhRIJRFi650G-5kW3quVRmV8bW-y0Ny3ODIGuMVmzqU659pawN4SKorxz7jQmj6p-H5zSb6kEyVB_hM30wyc88HZ5PCgsEt5hW2c_jKSvjkDMvaJEHYkUaQJ0LrVFP1jzcUq8RU4leKHfqHKNXhWmScQWavLAcLHa5GburaoQin_xrlTfMUWUlCL6KolGK1ZBWA4x9e1hHxUORkISo2y7kk9F-Bww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
