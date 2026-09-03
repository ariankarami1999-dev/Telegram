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
<img src="https://cdn4.telesco.pe/file/qfCx6nJAYKZruNdT-eLoGwGfPj3bJg64BJNDx4Gx9I0d5Iwhj9vCHY7YTZX187aQtcaRqthj8mwIgDUNDUyvYpKa9AEm8kp4OAO47J9ZJn3uaDMgxQ-Nxwyz64f_ueSRRA1EGaZYW82y2wPKI4jmA6XPfI-gB_HBeXjZnGftrglMYf9qeMLQsbbW3pIw3X4DDt4VaaA1TsOPoZ4JfCmtl4POZtWVnGN8w0kV7mqvhaxlyF5V01e6ycXV9V3iGvaCW3hO6OPMYxJExD5HsZEUOEo3ejt1hroIdNH6FJ2M5PB9fIQZ8MoRjSRtZD0jELFE9Ax9fbhpPf7q6rSFidr7mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 622K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 03:54:12</div>
<hr>

<div class="tg-post" id="msg-28957">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHYub4oOmsQ9Tu1uislo6IBt67rFVzqCVZ761QT5ZFb5XprbuMDd7oCM-tQS9uamIwomKMxr62gC4Z3PXhj0ifwNKkT2moOZo8CrFHP4K7dkjV-ikc3uvz258S9VykcNPl-SE8vJ2XYvn6DkgNPj9y6_zDh0q94OcdWmI_OIoIznFznNlKjBqO0G9mEh0YHN5Kbpw-yKRnmuB3zLE-VgAYjM1tINh3E4-wt8PJ22TlVreg7oj2XLofHhnoRrBA2A2vwNRlnsEc71bh6YZX6mbmr-1wmY94rH4cCZlB9sa_LdlVDtYLlWBdGKWTXGNigY3LlikdvBB18_mLm8E-YLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/28957" target="_blank">📅 01:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28956">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVggffYqmowiUhrXCGQC-DKdtOjFP16ons8gvNLDbDo6zadsJpRA_W0LnXOhk6oktKAO_1ZYB0s0jn1RuAf2lmW1TdxMELNep6bKDvUrkFfQjQ_vatec9tZkMXjeRCkqjWQEY-17W96IKJ94dG9ffQR5DUm9aDADFxq64YFq3rEJuQpsBK5m9nwA8RDW4wA_B0ff6QAttmanUcOc-D30XhkwtVM9ohv7grWr6UgP6650UFtuLMkYCRo827PDWkyrCV7It3BuLchwTq_b0sqaG85B9ELJT8D_71LUP5FzlMYTYaXOyIIqEZVGSUkGNEDNlxdHtGU1YueGoV1cbswEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/28956" target="_blank">📅 01:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28954">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy4o4NgxKy8RLSc4tX8s4erVoJfZO-4xuo7bsbR3f52xafhiaSBzc4p6GOvzMI_wbPaaFl5Xk7khCayPgyQejckn_PDKiGNP_6nML6vj8i31NrNa5FiyAE1zhpoPbxE2t4g6LXE9KfQD98OTMI-dm7aMbX2qnH9GNNljMZT_mwhPSxCgHc_ZprJBdWrxQvk3DGdScwPTi4U90uxkdZI4FOZDEvzTPqEPObLeRyxe3JAPdfx75wmYPU3-8zxIZeIrcxsjqVyvijawLMzYEmUgOLkJXQgS2lGUQFjdMgTYdRtUSUBBww-D1E-XzUanb1TJnKj6qoxzcAb_A0S2htybPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛آخرین‌دیدارهفته پنجم لیگ و شانس صدرنشینی یاران صیادمنش در لهستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/28954" target="_blank">📅 00:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28953">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwnWSdUl70tFw04STmRNvYgqLcSIs1jnpzSbXAf6oECz0rhxbOllL9Nwp3E91q6mhA3yqVlQMG5ztICYkLbFxhNGmXBGWk4mbx4NSQ6AL9kX17USzUIk8j2teehtu55iAWU94CLJtWZu3-htsodFRsI22Te3-OhJLLIJWLmSZExhi5z0YNahLz9xMFGs_hTWcTBMPyE8EFip7vFCl0CeBVwue7Jb76E3ZRrOZ8NrVGFwW4vpauzPdG4C8dsUJThzXsFfbMINXCJrwg58_x8U4gUAJVrHkp7SdQvO_4TvmXJqyLrJ3R1ujEuRGqNWmj0knxdRQk5Z3jbEFldKN2TzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌ دیروز؛
تقسیم امتیازات در دربی و صعود بی‌دردسر باواریایی‌ها درشب دبل هری کین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/28953" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28952">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b6gIeHfutL3M2ThrTUN9OfTzpzuK0YQ-8ZVbp_A2_mNKUd71KHTF4pE1FcBqQGbE6ThcdyJ7HrIm40gK3-V1CQUpaqBFnwYB4-WuvmLjvo_3fcyXR6Jpp7tsbYdHVp9wZ-v2ROUUynmwX9qh98rYPRjIl2T3NKbOsE8PL2Lz0Uh8Hc6mGa-oZXBjJPLjMvxLQ-Y8_W1quAy2CR49VeFRlMWS4YpwO4jAXdBjNoRjQEOEd7-78BJkrDftnkRZ2M7gciwcI-0KXMTxw2nrJKTYrJVBqKslEiQSQDlZ0LO5Y7LWTFXDD9SQx-0MmpFL7XLMuk-KFHPNUuRf_ibfVZu1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین‌مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/28952" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28951">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMeCeHxjUFOEBOrFTgB1J45cCdeSWo9cTa7KcKMJyL0CK0WP5APxPf9qykWTakWQateY8esMcxH4RbT3qKC_tM6EtftMp_3gq7g3nMddSI4N9N98T5zH0dQ73TEBhyk3n2PH0YjzRTgqPGXPaTP_wR8io9MGw358AFqE6-kbaKBH7H3cJDrZkS13Prn9aTbbq5N0ilm8rRvHPEO77uLknXA0ERk5W2H8NJ58fTetyi_6KZRB4pRspsD3s8lFx949uD3Agl-owFp-WRsWHX2a5ReKnspoR9o7MI6T88XQy-5n_dqP9VrE9FjrUqDwzVjVwa2o7lQQofot7M-0ZrdlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/28951" target="_blank">📅 00:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28950">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwWdvw3104k1bbTkIUYF_msaKW9c0GEd9xcy-cli9wQaWNiYuBZR_Zu07X0beWVDkAIX4ZwPBXcZimzBEqE1Tx7K5XWbqj_BqTSW4jY6THOslEmifu-q5r6053ePoP6v5pVJSMceshY_tKCdfHUHK_NNLzMuecIJxA4mwhJyXxXbNNnc9SkIwAf9tCCdxf0LM7nfc7M9hp_rxtIhtawN8cy-qje-d0Z4U4JGVNFdMQMJQTN7FvvOIOgmw05UmWbtFj81ZOhANFRo3guCHa398F78IKW0uGkii1VWFTjtDYGW9Da2Hk1axwhDV_bge6QT0sbQELRBoW2MREmvt9YuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌براینکه محمدحسین‌صادقی وینگر 21 ساله تیم پرسپولیس ازلیست‌ سرخپوشان خط خورد. دنیل گرا مدافع‌راست‌مجارستانی نیز از لیست کنار گذاشته شد. همینجوری‌پیش‌بره یه سهمیه‌خارجی سرخپوشان برای فصل آینده رقابت های لیگ خواهد سوخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/28950" target="_blank">📅 00:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28949">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=slVNa96Ym1CUAEX6FyiFTSysFmHlhrR8LlmehrLtriLnK6UqHFaOxNv4g6CDLTVaCjKZ69lmG5vPWWDcvWhEX1Y_8y5bbEhRoIaNDO_gM_gCwxgWFQizqXFqkeNlXOYGfGcZ57W_NK6OTMzo97wyQXu3j6mo_RPtJZn9dpRixmdBMuMYA3gpxHWJ4szL3D59ffWvB1yZJeq5u0Gdb6rTzgan1ua_fEGYnv-D1W-cBeOGsO1AUfUROuVERmh5wxmkjLvCmQ8dLzJvk3TYR3jQLAaf0eNNuNoT4t3RClpnnk9deo87_3QNRwEMbkCAh9b4mYSGN87KE5MPGefvL_Lnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=slVNa96Ym1CUAEX6FyiFTSysFmHlhrR8LlmehrLtriLnK6UqHFaOxNv4g6CDLTVaCjKZ69lmG5vPWWDcvWhEX1Y_8y5bbEhRoIaNDO_gM_gCwxgWFQizqXFqkeNlXOYGfGcZ57W_NK6OTMzo97wyQXu3j6mo_RPtJZn9dpRixmdBMuMYA3gpxHWJ4szL3D59ffWvB1yZJeq5u0Gdb6rTzgan1ua_fEGYnv-D1W-cBeOGsO1AUfUROuVERmh5wxmkjLvCmQ8dLzJvk3TYR3jQLAaf0eNNuNoT4t3RClpnnk9deo87_3QNRwEMbkCAh9b4mYSGN87KE5MPGefvL_Lnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری جنجالی از بازی امروز پرسپولیس و استقلال در گیرس عجیب بازیکنان دو تیم که منجر که خونریزی گردن عارف آقاسی مدافع آبی‌ها شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/28949" target="_blank">📅 00:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpJ2FWG6u3jokEI9p7VzC8QPYiM4hOs-vRbGV03D1u2Dgk6Gr6s8B4GbDkY5PNx9FS4-bZ03H6xyMgAVFWfUZvCLFklw_elmI1X0SNLhj88g1tBYJ41y2Qt2uYtBj9TJasxh2BIV2duVavkxcEU08z9h9bnUEW8UakF_lAzNJLq7Uv0lWvSwL8mqT6MrAXFGzTv8D_mumA5u479Vz63j1I_U5TJ5hxu0q0cYib9h7Lz4_agOXuFzy4iHEW1yXCYf5Yfh6umZadic3H_Py-kXAgAWK5my11ujJItO3CeGX6tY9qyVxryGwRprdo42bKStJqc3oTkv_jDuxF_i9i9Sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/28948" target="_blank">📅 23:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28947">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=EMqj6dlHzlIp5us28GJlmvoq2N7zsofkMpLdCvHJLP8bEwuGOdHL7VzB_BqCQbgsRbgMlzxDrQmBF7ZElFjuTCQa66uEFNLlLgNjYijvpS87ucroOHZOqCYXa5IemByZyWndMMveX5yGuRao215TonBCacBjMpQQuX728yBtRt8RkHN7-5iOE0Xxc-xJag1ja8YAA31H_r0k15n44avYdE_tc4tZXUjiFQFV6AIOS_WSRMI9Zfjm-8s5K47VG1Mnzx8cobIgEZu9eN_HlP3jUGD2lYdqfC-Se1pXb2VqG2W4nJTaHGp0Hg8BXvVAoTqFqlZJ6dwVI-JB8yr9juxdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=EMqj6dlHzlIp5us28GJlmvoq2N7zsofkMpLdCvHJLP8bEwuGOdHL7VzB_BqCQbgsRbgMlzxDrQmBF7ZElFjuTCQa66uEFNLlLgNjYijvpS87ucroOHZOqCYXa5IemByZyWndMMveX5yGuRao215TonBCacBjMpQQuX728yBtRt8RkHN7-5iOE0Xxc-xJag1ja8YAA31H_r0k15n44avYdE_tc4tZXUjiFQFV6AIOS_WSRMI9Zfjm-8s5K47VG1Mnzx8cobIgEZu9eN_HlP3jUGD2lYdqfC-Se1pXb2VqG2W4nJTaHGp0Hg8BXvVAoTqFqlZJ6dwVI-JB8yr9juxdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این کل‌ کل بامزه نقی و ارسطو دو بازیگر پایتخت با عادل فردوسی‌پور در برنامه نود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/28947" target="_blank">📅 23:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28946">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdGucIQDVN6utVJRSFBExqavBnZ7jFTCuiirwK_gxnVpW36Bz-qmtrM-T_UzjfxGbmzLCR4lCu3JdDONQI3MiXbLuleTCnMC3CroYm_eXxjRyqJYwwziziVqgBSAPwtb63t1Gy7HOYE9nv4U7eCRWi2bjK7JBAjpCYlHZ3I8m4PU04P7q-B4Ds366W2RN6pFMdSF-zhNdmrI-Fqm-HV_eExsvgRvXNKqvrDammCl5jHv5WY-YpHsTvNkp5yc08f1eMxvHm1zNsy231FsfHFRov9bhdB4bjxBsKqXLMDB_kKazsUAjTktHxMG4bhn6KYaaqvSxumeILjZaQ05mkGxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/28946" target="_blank">📅 22:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28944">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WY03DxhVsKaZIe7UUv3BERusBKYPKRJghGnwLs2ZiGnY-0rNt5KKKC3KWiokIbrW82DVCPABfcQ1n6p2No54OB5rn3Wfx4_GwmUdeGzZ-KX8XDFBJxlJ4P_hABHBzpgrGS51CHDzDvchk6O1bDdSBibhEbty1xNrEEcNeUOnlBWuMbqKu819oxl1Qm3TEzEgdkp92jLxF5mMjMjKz27WRlTBoXMaVs3f0aCMMUiHCmU1_YujOOoZdqqdW18BZ-NBztQfF9A58sSmlk-0Nbp58xPdOzoYHCPBxjyqUjqi3XfheFyvlMWJD58P0GkDmc0INoeymox6cSMmNcOxN3LN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKqtjncBQYablzamVCMz9vKAd6b9nvCMG5u7Zo-7PpSI-DwnMKVkxOx3L-gCPKHhnwH3fsyu4UYlSwFPpcru5emZMfwLBiTuAnFu_iGreQHHyxzd0mfXxjsY9-NiKtE7JG_bC72onrCikesuugz6TwgXUhoRgIJlJh5b_ZXIN72OtCxlDyAGtSEh8ztxF2XQJOFVWZYoPpJYrwUKPLp056SI7Ol5G5gowFTKAJsykUq9XPq9AAIHtfmYu5Dv0OUagaqLJP_8PUOTsW9gmXoSrtWQFkiEeqYG9zUntsD2tzQBfVMbSTIfiFzYL_FSRh48kWhYaXYMOdgtHg7_bHdJBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/28944" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28943">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJTNGFwXal1NqqayPoJ7N9GAt_J28wa1KGHoQTdCDyO0mp8-BS_kxJ3NopbaK37im9S8Oc7xbKkK2gAwYz2EhKMpxcHQ_BQ1oYY07ySMgsvOqGQTjqUT_PvztJ41mxUTyMXwg9WyNEjMx4c5ogbepWV_TM0zM5vpg2hKIQE1FUGr3sKQ7_WOJKU5vNFGV1bw2NyovXHthVu-XLgoTgIi-gcb_Y4gVRfKyw1CaSbeS9hD_dDzFAATvz3vOYGPLxGfLtVv4vgOZePwvFsI8cAy7Ym3tGNtYvD5roEUsljB7A2i8nzjf5Rf_h2hYRT2MxQTJIRAGscEH_gDAC78E_rVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/28943" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28942">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9SLSyv1g81TnkCR31mjEvtyVJagge75LHX_9z7BxnGBdUABYWZRnahdTjzK8sgxDnjKgNivOilKBW4TpoJxR92sw9bxhMWm_2G4wrqkU83vAVOBgaNOL2QYWldGzHjFcQLVArdFvlrKM-hl6IJeqvhbkmZ10mMCCqlF-BA5cq7xpzKyPTq3NNm9ENJEVb-0Xu0Dsw_cPzw1X71myPXEuzwdep0Eye_LvEibOi9Gp_c_dVbmznl9HoyEsrEbWN7UOKlMVh72p0luXZGt_XfySBqb00v4nKuMbOCMb6vUNU3Dojts4WPqkIaOLR7AQ7I5vZt0iGb6oQ4ZjKd_kSvBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی دوهفته پیش پرشیانا؛ اعلام رسمی کمیته انضباطی فدراسیون فوتبال در خصوص تبرئه شدن استقلال و یاسر آسانی در پرونده شکایت مس شهر بابک و سپاهان.
‼️
دادگاهCASهم از هرباشگاه 100 هزار دلار میگیره آخر سر هم بهشون پاسخ منفی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/28942" target="_blank">📅 22:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28941">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=FSFGXOkty2Bg5nx4_o8u8qvF0UqSFh2kdkP3VnPRptaxDFcRSkVLPW9CAoOWqn4GzygpUI04VMK_lgsRRDTTnL7nGCrVtIcQZqffrU049gINuwG0exKawZoguDG5E03CNVavhdFPqI2pYSSGRci_CosZocWHc2XcMmK6X7LLvLMFIJyQFG9ZyTgVUJzsDKjGt67u0xEwMvxKuyjtGgohoTiqTj_iHB2yizzAv6iwzILAHstfkJJzOyU6W5SOOiRXzWLKHqvAopfkLMGRjdTvO7LbYk2wUVfCMiSCQhXnJpD3ZwbQkLZT6EB-T4V0oXz0VsJAMgb2_dZP6MoxyQJ9iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=FSFGXOkty2Bg5nx4_o8u8qvF0UqSFh2kdkP3VnPRptaxDFcRSkVLPW9CAoOWqn4GzygpUI04VMK_lgsRRDTTnL7nGCrVtIcQZqffrU049gINuwG0exKawZoguDG5E03CNVavhdFPqI2pYSSGRci_CosZocWHc2XcMmK6X7LLvLMFIJyQFG9ZyTgVUJzsDKjGt67u0xEwMvxKuyjtGgohoTiqTj_iHB2yizzAv6iwzILAHstfkJJzOyU6W5SOOiRXzWLKHqvAopfkLMGRjdTvO7LbYk2wUVfCMiSCQhXnJpD3ZwbQkLZT6EB-T4V0oXz0VsJAMgb2_dZP6MoxyQJ9iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28941" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28940">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📹
خلاصه‌دیدار جذاب دوتیم استقلال و پرسپولیس در هفته پنجم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/28940" target="_blank">📅 21:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28939">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaKgVYXMxW3PwSKTlnqh24qn-RxFjNOT8THlDGZ6_oNGVkM-ZYGjBUpah2uwVV0PPQnvxAfTxyMbTxZpLFl585yIDFS8gw7kQvQkgeE8VJVwv3JqBSm8WvWUr3I9LhFQtTHElFBg90IFjA22jEgOR9_YcAKyB4en2nnAwmNxASA60AvZs18CV68yK-uQ7W8LhxvS2APFj17KwslK-eR0LT_H3S04vtOKkkRTke0IXM2yyyXojHCAEpxnVqjk--d5owbxVAkx0YKklJruKPuA7ZfgfqYWVzg2jqD4uz_iWeVQvx91sybSw68GJ5CjiKjqCDnErg5MWftpyIEb-_A1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28939" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28938">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCFHZK6Nw2dcoq_9de2WjY1VxVXvEhEtNA1cSiTJF7OTeXxdnqnwpHmkLy2s268iZjg4KT5tDSuUrD2-swElQCK1G3Fj9qleNu8qQ7mhCiFr3biiIU7YR9_w3o-14UZeKHKTqjmIAJAdeGSll9jSVOpqQdxLvjdb3yKUeAhHJUiTXnS0Q-XLanKmrTkHjr8vXG8LWw6_aRc78bXBQ6EHCYNx2-LGfkpelK7gFRQAGfKnpI2qqy6FbIf21xBfcRbwKCJsz8WIa79s3XG8mZrDBlcMDEIn7qzjDZNh9v1AZWkpkARNuPIIYVGoQ2aDWV4_TiWgs8Xi3RRMSoX42N-OOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ستاره آلبانیایی بازی رو مساوی کرد؛ گل اول استقلال به‌پرسپولیس‌توسط‌یاسر آسانی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28938" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28937">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sJPhtGfnKXH9lJjiyi8SKn7FC5LSasuxYGldPDCoN4rcMki9Mqim0ObWKJv-8yonO1qt1a8t2m8w3HUOV4SgaEfJJ4ISRpeqylqhZVJhj0hThd945tYGvhORhIGuisNt9B46CNVznTRoCM-E6LF4mMEk4fli2Macia6zVDMT6dtU7LlOQgFyGtmQQfzaFGnrA3sONnJYJWqi5nqkcEa9VmXGeI8Cl9lUCb6tA5GfCehKbJl0OLBSHyZRMzMB35STuXncFqIGM94PIhVUzoC0LvQJj1JmNV2UVqhyyfkKT1qM2k_R-PM7gMKK6NAwQ5L7mNSlTSwdpmsw3Lj-2eAnaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sJPhtGfnKXH9lJjiyi8SKn7FC5LSasuxYGldPDCoN4rcMki9Mqim0ObWKJv-8yonO1qt1a8t2m8w3HUOV4SgaEfJJ4ISRpeqylqhZVJhj0hThd945tYGvhORhIGuisNt9B46CNVznTRoCM-E6LF4mMEk4fli2Macia6zVDMT6dtU7LlOQgFyGtmQQfzaFGnrA3sONnJYJWqi5nqkcEa9VmXGeI8Cl9lUCb6tA5GfCehKbJl0OLBSHyZRMzMB35STuXncFqIGM94PIhVUzoC0LvQJj1JmNV2UVqhyyfkKT1qM2k_R-PM7gMKK6NAwQ5L7mNSlTSwdpmsw3Lj-2eAnaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دروازه آبی‌ها بعد چهار بازی باز شد؛ گل اول پرسپولیس به استقلال توسط محبی در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28937" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28936">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=r7VlSSUr9sgDGkvwG62RVDd8nNfTruFdSZsftRI2QJqLKbLYq86xm900e9-Wexo_IMk93WzZ9NbpO9ht3J8YR7x_CcLsbULIWiWaOeUz_TraOWegB0sBimqEtIQcY4mKAxgwWnKSuCaBTxGdouTm8MlfdY2yNUyGsZ-gbjvnMYOLT8blJ58QBJX-XipGhi9fkQdVoUzKmda_pg18V3OH5nlGuO2sisXRjzy7_QmWQddknO8D1icBdTFjJaeJwvv_m8EjCCIjP_2iUisDVj23-W6k1fVsorcSoM38UUpUUdMXPo2yt11OtuwzXXqTvQcTmO3g0OxTop5W5el045M_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=r7VlSSUr9sgDGkvwG62RVDd8nNfTruFdSZsftRI2QJqLKbLYq86xm900e9-Wexo_IMk93WzZ9NbpO9ht3J8YR7x_CcLsbULIWiWaOeUz_TraOWegB0sBimqEtIQcY4mKAxgwWnKSuCaBTxGdouTm8MlfdY2yNUyGsZ-gbjvnMYOLT8blJ58QBJX-XipGhi9fkQdVoUzKmda_pg18V3OH5nlGuO2sisXRjzy7_QmWQddknO8D1icBdTFjJaeJwvv_m8EjCCIjP_2iUisDVj23-W6k1fVsorcSoM38UUpUUdMXPo2yt11OtuwzXXqTvQcTmO3g0OxTop5W5el045M_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28936" target="_blank">📅 20:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28935">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=je0z6aQ7dPFPytVIS8TgfvDGg5bj3WnvtQf4wfKaLO_tFAbBlrQUfb4mTyUUZCWzyMXB0eM0qZ7AZ3guiLkALVpjd9fsUTdjf5d6pMi33wNddDR4A-1vS7oJrGc8iphJuptB4WmdKPVXmhId2vFw-BIXJCqdlzKjb08VMimJclaKyxMCukElttpSNXlOTt8S0r4k4PVWPlSQZQIS9BhOvYeE4GydoFA3tT2N-23WDlQMvTyL_TyioV3TdMuJvTyXr_ucNt7ixvup8MDVn5ovTcxtwYrR-aKBCG4KFeFZjTheUovURh_Hp8anUMim5jPY9IT8wRZ_g300RU2qtXap0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=je0z6aQ7dPFPytVIS8TgfvDGg5bj3WnvtQf4wfKaLO_tFAbBlrQUfb4mTyUUZCWzyMXB0eM0qZ7AZ3guiLkALVpjd9fsUTdjf5d6pMi33wNddDR4A-1vS7oJrGc8iphJuptB4WmdKPVXmhId2vFw-BIXJCqdlzKjb08VMimJclaKyxMCukElttpSNXlOTt8S0r4k4PVWPlSQZQIS9BhOvYeE4GydoFA3tT2N-23WDlQMvTyL_TyioV3TdMuJvTyXr_ucNt7ixvup8MDVn5ovTcxtwYrR-aKBCG4KFeFZjTheUovURh_Hp8anUMim5jPY9IT8wRZ_g300RU2qtXap0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشید اسماعیلی هافبک تهاجمی سابق استقلال با این‌گل دیدنی‌اش در دقیقه 90+8 سه امتیاز ارزشمند رو برای ذوب‌آهنی‌ها دربازی با پیکان به ارمغان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/28935" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28934">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igWYY_ycNGP5pM4FEmWQxTSAEOuYRMUHxX5if3ZRh-11WhUibmkZeDSI2PYE-cKqOqiqJnJd7pZ23oV8XdFlUXCrLvC9jNdzoEW_rVRMldDGfCOvTp7Gfru2ook5Rf1-pHVu2gFeT8WDRbpAwgxh-R3kA9714W_AQ0EEGmJjsG4e6NPSDdX5tverWO_BSomPpTk4QO4Htypr1uZ_T8SD7-HT0Q4tGegTLQ25wQ5Yo5my7KRMaTZ-fuLj3K67UX4-FlqYzAzVghRkDOVP3ICp2wmw7uGTbg59V1XiVL_olcgNJdKfH-eLo7DXYLD509V_cmTKh4wnQtkRu5GtlcQKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28934" target="_blank">📅 20:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28933">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ld7sRZ8yl7CsOuKNSeYfbh6vD5H2qrR4wtXAgng8T4LWoM4KHghi9RTbvhgCGZgHxO0_CrO2VdYsNiZ2Jf6QDGWgnuXDXZo3m2o0baDa7fs9xT5Z2EkuZjbyre7FL63tSi8n4YqtzVmlUgPvdKquS1oKBUUTIq6Eaq411mDueM2-4_T5d1TuyMKi6Nu08q2z-8a981fW7IfAhSCAZahVwDqHP4JyPHDXwiHVLP9Ni7bTE36dj8ClhYjekMzHXgN_K8eeYU71Pc0RCMGCHLDlhxva2Eg0F3hA210ZU4A5GnEDkG4u4FYO6ve-i3c5pA-LwW4DP7C858crk6iDW5gm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/28933" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28932">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJTRI8ltikY9Lx_i3iyWGzXye5fbRBzsfu8aBiWvxbYSSa4k5q4nV-1yJK2eNeDmfKxfhp_S9IyQxFfCVh4gKLbAnt7bEM1fkGNC4k5m_Z69B-xrxoQ4p13HaYLqF3YaBVAmfPleDJo3aKNkX1E7wFR9Pa4eb0EJMoHBpdUIyng0puKGoIM2w_h_KFWWG3k_pPJGfXBcPOyhYo1ugyqPd_2xyftwLKb1riLuZ0KfYo6AzZP2_M7FCwzVRSG9JaFZjhyB9umhY4VZO4AKV77e_bUkAJ5caCL8YUPqJF2Y34jKabdnv0GHVy_ijL6v0ULyoQtXfTger1CNkAcIY23EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/28932" target="_blank">📅 19:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28931">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=LTmTZRXzW2rYx3QLpnRkbqBD1XgcLEyxX4j8emmICO-A66oQLN7GPv3-p_aiFBofrjpVRwhIC7LpME2NO2zyRd0_uFRF3Ehm1IccPg_XvRbCavMMtdDkHlIugo1vB2GnNyGQ8Oi3dkFqo331PY_RNLR9VsCsQ46cE21mojNE59ZzGRPeUkQpsLsTID529chMBq1naCOgaKJgk7epOzAn0g94mWLgIDbaahwy1JGc6N6BMRkpkNhO8UQA6q28VOFN_5KDToWbm_upltx31lIKLs-QaaURwX3S3eeTmsMfZdy0i7b3uYuobdv6k6GgtOcMKwGrTmQxz2JzRtoq8I1uPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=LTmTZRXzW2rYx3QLpnRkbqBD1XgcLEyxX4j8emmICO-A66oQLN7GPv3-p_aiFBofrjpVRwhIC7LpME2NO2zyRd0_uFRF3Ehm1IccPg_XvRbCavMMtdDkHlIugo1vB2GnNyGQ8Oi3dkFqo331PY_RNLR9VsCsQ46cE21mojNE59ZzGRPeUkQpsLsTID529chMBq1naCOgaKJgk7epOzAn0g94mWLgIDbaahwy1JGc6N6BMRkpkNhO8UQA6q28VOFN_5KDToWbm_upltx31lIKLs-QaaURwX3S3eeTmsMfZdy0i7b3uYuobdv6k6GgtOcMKwGrTmQxz2JzRtoq8I1uPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره سیروس دین محمدی از بیخوابی در شب قبل دربی و گرفتگی عضله در دقایق ابتدایی دربی. ماساژ درمانی؛ جان هرکی دوست داری ول کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/28931" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28930">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIIvYLexWLRsq3-DrVonIcYdnNrPShYokVnbTQWtvRGt2p81BEK-APS42-CclqxPqaxVclzRZLRtrvWFdynJODPcPG_xcMZ8MM9rhww0iwmM4QeNsr5oNUxMesoUEaP7UyyRnJUlkRhaCZYjSMEC_RkWE_cfuusFv3LYypQeayDw9GDYPb_vveBAru2UQE_USaMUMoPpFZZr9Dob9nJDhGjaJ2X3VUQm5c66Jgv05ls7kZov1WmF-e0kZhXAvYOS7X8Gu3SbBx8x8W2adMZaTHpD8fAHAyYawjmo2VODfDe8fGFC_8zFgUKgnUltE9eaMop0wMyxpJo7Gv4_rFeJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست کامل بازیکنان اصلی و ذخیره دو تیم پرسپولیس
🆚
استقلال در هفته پنجم لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/28930" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28929">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeWW7ii3BOHcOqNMTI5NHWxVqyAWerL2WdXYIW9un-Auc-ld76RBohxPqf16sOXAdI_XEU8fc7gdxXXtRyvvgdpXKil5__DPsfaZS_N9UJjG8UifIRRDP2MoQyvUtRM75Kyi6swO9PvI9OlpxajKq9tNS7KXDOmpM-w-koqby8KE6s3MXtj5aWO-VAQoi8s3xViUn_-cwPqLUQet_EB_JOOFO56p9AXAQy-LCLo5lZYRfLGVhiy-1r1wdJBESHs5HTGc2Xb2KY9sXjCds9ua76h9lTFlaqDILARHCsyx3wZkWQgsr5PHY0zxfTdm5IErCOoR4cSeIUTkmpbxdG1IUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دور اول جام حذفی آلمان
💳
اسنابروک
🆚
بایرن مونیخ
🇩🇪
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۲۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/28929" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28928">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg8RQWGvS7c7LgHfkOtijqBEnV0cDau-XxYqjUT0UVT-vUtT2fraGKATYiUOj_zlAo7nWwmri3UY6hLuvVo2_awBk5SI-dAqv7MdurHWGTd55EHsmWkw9LnTC8wC9qAJhZRZgAN2Pw6wiXmqlDRf5-3W79cjz6ymZqGRkqLxZb1EkomCcJpwhpdlQ8BL1QyIeI-8IiSWdXIrQApXdjCDa1L5k3HttrtKDkflBRskhNTzwXYhbJ9AzeoM_ts9VmrqJwKt0sUVzdIa0ueETS2QKOYNNs-gONVpAkn1NohoGqQYpllXFmeYmTBUyjyIYlGdjrTvEU0ftgdLzrBPCnrgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/28928" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28926">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXCD05ycz2lT2mHJUVdA1yNrTjh54iiu66lk5Jz-rtqiDWRI-RsRRRQUVuqhlU19TADW1gZa8JcNdsFa7pm-Anyn0FQPOTi96kAwLQm7LEyWwSsEGaPzJ9A1tYbObAo3roiFI3JjLLo19QXKTu8IzjzGpi3E3loFwBlGxST7cOc6Tye7lMJeaP1SQ_FsxvYajhZLVmj5oKSAkeKQDDFqqoyXrxbriK42eLttntfwLU03FPdtOPP77oocor03vPx3pY9vjmZtaJsJLuFtQj-GC4X83J3feAYrxg-SaJtPglhTtquY_aLTt6kpnEkX6QIO6EYaSC5iNUvRyPA7Qv-veA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/carUBFQQ0x31e4Z8xHFNKvMsWlYzH5eE-gz_P0edhCLb4am9AEujVHxTicahqX8dUEvTP516MZFXcPoa_7Qzn_crEV7fuPKcpH88TGDa2plswpI0kRQkIqif7wLgs3MvI5iDGiao6FzIX-G-wkoElQnQlK1qhUtpxaTtUI8QnCwyHm82gqdn6f_zEA927_SGD1-8asmKa4zhTPVoxjWu3h0Kxv_YidQxE-wuBk6I4K-JT5pIDPF5EfHw05ZiPcPRVkf798bMSMjdZRXX8c5onQsU9IrQl4gw5MZzLbFhlcCGPMzbXUyb-E-IU2r7k63galiasHLr1mROBo57YRYz3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/28926" target="_blank">📅 18:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28925">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqEVh8SselVcL5qAC170N9xFdE3Lxjq04byOt1QMdP89Dkt11RrWWdsmLgejeEX9708MWo07h9smCPNs22KCsLi4_f543rpvULf8_vvIhqgoBgipVhWDdFIWtI6wKJ2VL5ukkE5Erw7PsO_uujiOShsfdnhU_5fGt2BUF1I9AVC7W6o0CpRpNXTT9Rj-OhzSG2eGvGs8IBp4rU2Bm0nYlTACWKN5ZXEgiv5LTXSWF2bjAlT4hin9aarrf4j1yBIBEp-O7ObAK7_1LmbRt5YztH9Iaq1DfkckIwjBaeC06wSTdnW702Q3a9HGMGMT5SE5W0aHRgPA5utuPZlxs1x20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر لائوتارو مارتینز: لائوتارو در آستانه پیوستن به بارسا قرار داشت اما اتفاقی در پشت پرده رخ داد که باعث شد این انتقال منتفی بشه و باشگاه بارسلونا با گابریل ژسوس قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/28925" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28924">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD8Hm6w0MboqcZH540oG34XASLpRQOmcSQVoKSQiULI_iQOqyYntmnGdL8jxQEIZ-VBRR44DFUYghk33E6L5i-YkUvo7iCRykvqwcPWSaTHXwjLTpsIn5buoPJ6ihSqj6m_mVFu1_ViIUY2bnAu4-f8lykyCuIHc_4q4r_l1Iqtx_639mJ6IcbOpkeZvJb_BlXCZMhICmKb75W9148_FwoCmJSOgxMjzbZWiRwvH84bMZrgs6mTC9QGrkSiofw6yJ78U5pcnilOTbe8u00HsUsPJFGqYSnjbQ5Wevxe86aS5HxIuVgbfZuqQXJxE7zExkVBNgSI95pGIB_a44cGB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/28924" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28923">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwmmE_yi7rFGRhxW5XVDsSdAOOzg7TTLzuUcKJXgQo87W7XGdbDM99N8Gb1NBsogSvUkZdMFSCVvlKFIfKqa5xVPCFy_p3Ij5oBODVFFGT7P5iX1a0EwJyfcPDKIcIwblwDa4Q-ZO7w-vGgnaCn_YEHfs-m38A3l340R_WpMsdH3bCjO9i2EUjrre8lVB_g92RAZFImR5h_pkiP89gHjTA_XPkKfeowDOMravVyAY4iusGn6gX-yT4aoCEbRnBUmVWZ9WcEr9vqXUk1gQDY8fTW9Upd_yKVDDCWboH2ZeueuPrvNzeEjhfocnKoeG3pB-u0z1k41gWEbp0xTsDgAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
شماتیکی دیگر از ترکیب احتمالی استقلال و پرسپولیس برای دیدار حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/28923" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28922">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAgf2k2NP1NHIEdZu6W24lG6kjdP44u9It2oXcu3pg0r3h_PB8BTLVT0mELQ1v-fpT8z7VkDL57oZg-ZT8s2j9jvYab7DV8YD23dboc9D0eOfLmdcUSGZprCA9eyuQpvLzSik-BHa_xWPKv7NqPJhKf3Kg2uBgreSaEm0YnVx2cKM2dDVxPQRUe0_VVXnFUeO9zL5MBwhT6lQYrQtdzqVJcK7seKdccww98Lp0eg8DNbHQra2W8jiZYnMkchrgWJQY4-AHp7t54cG9wrJkgJ8alK86-YyL6kdZXDjRM2xyYCrtamNnqhua-F9rweHT2XbPfBqil5-g0PIeYqac-YVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/28922" target="_blank">📅 18:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28921">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=pQi_Y64tlhHw7arEI-WSg17WHNNNVfRF_G4iRkgmHKWQNDru_Z3-6YKp5BgpTLjAr_V63BpFoUSSLrDnYCaajrwnofpdBhqvIhR5LJkRv_AJ-qmapZeIW1yV_-lt2ECsgjrtnoJcIUlV4TBAXbarw6u4J_MCvv5Qbu06C9QXN5cQAQEg2e2wmccdtwJMUgyxcbkJywZUmW7uo_sC_y6vfXSo7vCikG6k63f0kcy44YfI9PqIXvREaKOdvGUUEP50ihdMegStQw3GXE6IUiagrJ2v1WMg0TxU4SCfjzt7c3--082ywpJhXXV7LioH2g18AQKfejdmbsrmpEaQfxgK_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=pQi_Y64tlhHw7arEI-WSg17WHNNNVfRF_G4iRkgmHKWQNDru_Z3-6YKp5BgpTLjAr_V63BpFoUSSLrDnYCaajrwnofpdBhqvIhR5LJkRv_AJ-qmapZeIW1yV_-lt2ECsgjrtnoJcIUlV4TBAXbarw6u4J_MCvv5Qbu06C9QXN5cQAQEg2e2wmccdtwJMUgyxcbkJywZUmW7uo_sC_y6vfXSo7vCikG6k63f0kcy44YfI9PqIXvREaKOdvGUUEP50ihdMegStQw3GXE6IUiagrJ2v1WMg0TxU4SCfjzt7c3--082ywpJhXXV7LioH2g18AQKfejdmbsrmpEaQfxgK_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
کری جالب و دوستانه بانوان دو تیم استقلال و پرسپولیس در فاصله دو ساعت تا شروع مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/28921" target="_blank">📅 17:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28920">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ea0yh9g32ObihxuJ3zl_OtyhRgiMgUrHBfMojue_0RKqOpNOr_vTr-zp--QCylfW1uG5JzLwCjPQ3HY7RrlhCepOQWJ8WXXVAB98lhVTCZbhHjbqS8I6pnjcbpamwi2X4Oh1Z02PMJqvYcHloezRS2K8szLKqy0YJViUp-KSwgk1Qmn45-lI--Mt-aNVhCw2ApzT14qq3v7zQk6s1ByRtOY8W20AHCBR8acEoQPmCln7Hd5oyJv0vvGgrFItrzkSvLTACQD-X053Rjdb2lTvic7R_811pOrC_97KBIpC1Ly8PVKBF3MZw9HlsT4VgJoArK1kTRThDsBuUF6yqoPbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
چهار دربی‌جنجالی دوتیم استقلال و پرسپولیس در تاریخ این تقابل‌ها که نا تموم به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/28920" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28919">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKYHNi_-oK-G3N02ZI4vHk0wfaSdpg1Q2auLRVpWK3CpDa9hpvq9_kQP-_sx6sn4Q_7HYhjloPy9e1NCdEtL1QtKV2Xrq0hj15Ms2hdg5agnT6ErnXN51GPcLGbWLMpLhjy6liEd3sxMp7vt4bNm0o2E_YLoSRPS5xtfshBaxt_JB4mmforYh4gfXyWs8sUN0gX2O8xLQ-8ruzbKR1Mth7rXgCNn0dQeXWbrRGUV2ui5vun2jLKB7Ec-Yj3jU_-uh6gBa4U4yBKYNPfmJJDfz-K-ADIKeKmlwdotKjl1gm1NI4Y2eBOQRhoTVCRePC8Zz7yYPayANoRem3StWRsviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد پیام نیازمند و حبیب فر عباسی دو گلر سرخابی ها در تقابل‌های خود با این دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/28919" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28918">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tovri9sJ2eojfkgNsZUfCuI1ojzSMhxjUG9vPovRXk9yW81YzjB76_Y3iXNHO_pFZ_x1WJplSb8d4ZZQKDSu2LLkNCHM8lty9SVa1XPBl-2ivXBvblZ-WJQ3RsnKV_2ndF3q_ED-nmrdT2UBgfxoPJEaGGkrQKxta_8Q9azs8J0FMTCRuVP9cvSothMFrrl5AjOa7IMfch1EamsXaCSwRVKPkSyXa3cFSjrPMhZnuHyOq6QeSgeZe_W6AOoCILkcQNvqN5UG3yX2nus7G41saDWRKmB3V8ODvod-vPnOxqECZk6y1AZHGFAgt5sMLnI6ZbdD0EA61JxXgawcpv8jKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28918" target="_blank">📅 16:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28917">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT-Fc7cOyF75LYWh6RmUw4qJcdSSGeKuQ1Hq5ewBzYx2p0SBeVXlezUjEj8t9LjuCNx9bkrbMT0wvQ7lP3iZx9OgZutwtYPC5xyaEeHwCZgeUMF-Tawe_Zgq8zJOOST4ocQLcc-Lezf8XSInKEEw2PIJdT1NX0yPKJm0L2xi38AzhldaIS741SU-juNnhOiNbauJUsZTV8gFqk_I2V4BqPYgpZY1hMeVZWClJK9uQZyz1vDzPnTSF0mQCk_2LQOrQLheaXrzBt4q-6SkVSqolbqTWY8m5UXStOXTx51y5rjGHSaqXQtD04bvr7a7mAGeQ3W-BGn1r80tfOjov8ACdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی بیندازیم به عملکرد تارتار و سهراب بختیاری‌ زاده در تقابل های خود با استقلال و پرسپولیس به مناسبت بازی حساس امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/28917" target="_blank">📅 16:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28916">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOJ2MaqA0Z9ehkl4b-rp5t75V67oK1b7gbfunHKsXXixKFGhZ8Y2G4cDNSHv5U3EjTDAa3mlftmky1kKZ726zi5Sy4PtBuGfZ9aXKjBhJe5y25ZWvlC404GF9KR8y18lHOQlSH40732wBWXy4vbcY2jXFvfmSN7uhAAH4Eh1WeeCIQ46LKGZYoRd6sSYpa36oMj48LkmpCA65nMIVCnObqjKWDbIB6fwD2Dn_zUtQe7xewNbbi1bjMlaSvb82ggduC8pY5BLFXC4DJz0Drm4M9gSVMdVi4sV1ZCWwQB6QbKkXlNMCpjFcX2A50YG10Yxr2NLAWTVIr2D1Ue4WonwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
درآمد فوق العاده 200 میلیون یورویی باشگاه رئال مادرید درپنجره‌نقل‌وانتقالات تابستانی امسال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28916" target="_blank">📅 16:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28915">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl_K0J6qM8qzaSY8JO8J3EsZjjBIYlTZ64GeU86TFWgPT0hEeq9zhtRY3jxoy56wmyTSbGcp-aZmrnFisbOs6-SXjE-dF1eHmbJJfoCTqNMLiIulHk70SS3LI00F1c0hfMegYzxICa8p5zBobKC4T1qtvUFvlV9-6nYd9jccMKp80JVds8_89B-DrvOzEPvFltno2N4xUOC1StIl5YNgb1o4SlloDrsvC7deWYFR2UpLNwqPatV_sZDFN8pcIW1rJrTEnsHbwoAfLqfGV-jiOtRGQgnAqePwj3W6nkVUD-j74AzLnTa2WYoAeSmytVK2pYw4Fb6TJmkB3lwYQqXJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیتسو موسیمانه سرمربی سابق آبی‌ها رسما سرمربی تیم ملی آفریقای جنوبی شد. پاکو خمز سرمربی اسپانیایی‌سابق‌تراکتور با عقد قراردادی نیز سرمربی باشگاه مراکشی رجا کازابلانکا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28915" target="_blank">📅 15:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28913">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1oKnuRBp2Rwn6ZJmIlMgRUAdoSvAAxziHGrg2edd-tcdZofyWX5ZDdWR2MQRBQ2UX_nq0NmrXCSpltU6Ox4CrGYbHxGuzBDG-A3-70YpnPeWR5ceAjssdaqARQ0mc96hEdFy9HH5uTsgnVPtN15X4oV2bztgeyWA7kkhjRIAo1afwxZ367CEA-fOJZBBqeEtRCJgoGB6DR-Y4-1R5Ij6zAy5LbW3VIZgDXMcM8yHIEs7g0ehTrUMTvVJ5p3_N-OQiwjjjkt7KUQ1KcWiU0vlV1-ff9ec4Tza-10iCen7E0iZog81zIjzMZGfQ_OPLbcFRH1WY960spTQDEpeHV_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eicnJ4tSpbYSwcpfGZwWiOAjJ_5fP05qiX_UYgv1mvoIxnbboY0PRM2OfFDrI8En_Ukvz5BYV_vSkHWs7d6x3gACNEuNuX80_aNuX5TsU3niFOgo8KSSMZfSf48DzZVhBXalklQFxJ8C8eHjNPfQ7edinelTQEXCX6NKi4VQ1G5YaGMnOWOwgTjf7KlnCWDO4h8pmEFHvDV3Ta6fphAZwxMeR1fuzZjVpFWrrtIJhoVu4yE1mZiYUIqnr0feLBB-T_3WVXbWU03L4BIDtDU-jCnFEojwI6jPvt3xve9Ahw0_oKonD4khj9PLy__CR94oS10rhtuGJnQqJOubKgJQIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28913" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28912">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YogSCvZNMJA10UHpNLCmffeMZuP0pyfQ4WYGc_l1h_Nc5qEBrBiGy_y1oTV_iCpinRUYdl3J1O4u_JvXdorqYvYxTLdRYrh5RVucytorW33wNjaQSz9gNWYdXGZDjbswZtJm63jz8Zlk4S4U194n2RHbqqDEqQcx2AvfJJip07-HrofTeb2FHJDebb3p8gJ0M1bloaZbiUR1yCj2oVtW04YJV3WYyrslDmGScvud0RZYZ1iw1Yaym8KGHCgi5Pz2n-XZ-6iXhX2UO2T1QHOUYcgeIf6tYBXl1eOOZUD_cYJhkiP3c5nYZ3f1nsfWaPZgvGIqh5nT4gSiv7t1LEK7pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28912" target="_blank">📅 14:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28910">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaulHS6TS1KMMWWzJYtdRh6rRL0kgSVih5IZB7J6BJbfpaDroRRUoEH9kv9CoT-yaO0aO2cF4KUJndHKhkmGc9fCLx0apBBJhiBsZwg-M6mYfxg5SyMDe7ya3fjkiflzpjf0aWp_CrNlH3VzyOkyGZuOWnHumyvWHG19JycoFOJNHcMO74vxeb05UyHxJoafpyUyqdSMx__i1bh4G_F-qIhGiZ80qjd2ve_zHxKySeUKWz-uWOlph-OSjyNJvW1kgyIDN7Xw6UekoBlGrtlbYMEtCYpbeLXYrKjHZfeiSJ1xSBcHYTDbPxO2bqgh0hyW-NN6wCVquUVvItOaA_rVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28910" target="_blank">📅 14:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28909">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=iIj97xmdkYbjxHq2vQWXGXuRjkQrKEp1dhE_mVUAt7XCds8spcis7CCXkwHZ_ZdpedA6SNEvdKz_E0XTUnHZYfoAXg2zSkX_V4_z9M4jXA6FFMh6lB40xIgnu_vyivFF3K8EOttd5ezydVKM_OAWdf7_aX9twr6vfRG11gWN-5wLJ1hBSeMOa059tCF-wSbzhYTJtsWLzS9BUgd2Kb8WWJ_lEuS6sRXxYBdE1euKWWNfooeyBbhInuhRzNYdv3H1uCnABiESLEBStKjERPyY6en5fqtPwdfjEfaJ89jPtmPKg7PDfTsdtzP7TZZQt9jbisjskP0gXZ69CJMbJ3t6GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=iIj97xmdkYbjxHq2vQWXGXuRjkQrKEp1dhE_mVUAt7XCds8spcis7CCXkwHZ_ZdpedA6SNEvdKz_E0XTUnHZYfoAXg2zSkX_V4_z9M4jXA6FFMh6lB40xIgnu_vyivFF3K8EOttd5ezydVKM_OAWdf7_aX9twr6vfRG11gWN-5wLJ1hBSeMOa059tCF-wSbzhYTJtsWLzS9BUgd2Kb8WWJ_lEuS6sRXxYBdE1euKWWNfooeyBbhInuhRzNYdv3H1uCnABiESLEBStKjERPyY6en5fqtPwdfjEfaJ89jPtmPKg7PDfTsdtzP7TZZQt9jbisjskP0gXZ69CJMbJ3t6GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
به بهانه دیدار امروز استقلال
🆚
پرسپولیس یادی کنیم از این سکانس به یاد موندنی سریال نقطه چین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28909" target="_blank">📅 13:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28908">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN0evEuemmiMWqlpQM8uXJoYQBZf9mHZJvu5947RshdP4DVIG-CIR0adRvwMEOnMUAozjhj4sZFIDqfOhv1MvO8-aQMAy3Fko6S75RHELnknPLagxI5lsClb584adNXbgJ6uN7r4kP5q2yBydUq5Fd49QhnmyetSSWVTdpttGmjUAYZqCYnL75dlTsYMPdfv_LlT_mZrFrR7uOdGqqB0om1uK2POtgKCnPBoAEyGb0Lz6sH69O5RhqczWY0HyHes8lMH-PPHi47BawFNHWFIrgsEaKU0E_--UmbUBsntFUtzpiO4GWB52c9TIYJyv4kBIV5mI7f-A0Jp4PC7Fr31_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28908" target="_blank">📅 13:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYhGeGyjGnMgk9w_QB2-1L5EwoBW3mKzth6nK3e0qtCnP-ANfgk4oMhRXIVn1Q9Dnj0PEk7Q4dxnr1_1PcWRyh_I8dlffksgIqOZFoZME55PhQhf9LgrKZZQW6OcRoL_JOjRhApDdTJu0Ti8t5c0IHJdy3Hqt3lkgW28amY6kjNLK4jfAuIJ-amk_1mpl49Zzmq7n4WAAIb-9GBMfxx5g6lTf1mxwu5DqOTVa2iGkJ7sR5zGZ2Cv1zceZ2JnI2tqY15oek0RSfZ8iwnbpYnrp9GLPzny1oKH5y7eW17yl1smfgl2fjCFotZJcA3Xqlmey6ACUHZtj_zk0TmRJ9tfIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_Iilv1hkrdJEPOm7rkiXtbl2jZuvfpWbX-0N3g1pdqX6yfE3VmYeIR7uWKsg5nHs3j5TN-DKLWM2oBCQKeMP4DrECY03TV8Qs9AFUsAq_DaaZHXsMP3sB31MNgMONoZKLq4MuTYP8yS6XwS-5LVbFKqrMJYbjdH4ge99dVO-AUsOLzuWjN6aYTI5l7vy78UtYt-4ekGJ9X52-0BxqFdRIG1HQzDyWZ-Wq25Nc6Zv86wl-JtXwqgcoINpzjh7J3vvKFjG4j1YXQQC5ZMqNIX4QhLYDd6VUsE13-BZMOl58A320FOmPbUeIfKMNEaoj08xKsUq_R62L95YYJtZXdLiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/28906" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28905">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr9__Vp8XhIKU_xEq7QeGv7AGUe1tEJARjAMkDaI5bWonJ2-W-RzVYQszqHUcuehJvlBWZtCih0bsQ0_e6q_-4_ElQMAbd36aoQ9GuGO4KS9E291OdOXTjxdu4mtlfAVgfbrGbqkZJ5OJ1fjplQhDkVkDJ3Nip6ctF_I_Ai_Mkk15I4Od3RrFh44ya6sCZZGxIbBrCa0MA2cumQ8-fC8edt5UwDQMpoZB4K_Y3ICJbjVNxPSsztvXNycYslRMDAfeLGfU_5YF3eXuIXmlKLuHE92WTgLVLH6dcB9DQrSVa3NtkzwiaR3XDEtMW7IPzQPoiDCZpDDoHkuozeeMoSJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/28905" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28904">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7doSIVPpSR_58sKVvoSNGVxBhNEhYCJa-Q_cDE_8Wq9gguw9vNJFG-n7jsWAZMxbgPBM7HHBzRyR83-a_4iL8cSS9ltzdWIzCdiaI34h7UKI53UUf_NI_yBQ8gqWz70AEzlWY55oyDGDiDaRK8ElxoFH9H1xsn-rTAZsZpVmY_uTb3zqtD6uFgZPyE0z9JyPXCceff6s6FRLODUaaLH3VWfCZYrEyMHnsM1loOy4lRJkjvVOiXH9y8llGU8TIVd1KxSkOb0U4IlUaFJw7uX3q2cIt5FAZ3Yx8SxtMLgDNaJazoqAmym6rG351B4hMemlelUYAprfxyFjiYwOWp30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
نتیجه دربی رو پیش بینی کن !
استقلال
🔵
—  پرسپولیس
🔴
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
🟨
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی در ربات بتگرام :
https://t.me/betegram_bot?start=p12_r4EF37DCE</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/28904" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6Vn4iS9lygqi6bfpQuij3Enq7SgH0sZBG5TANb5MgMdRQaYTIjVMTCxpjQGbnTmj_PgQJSfE9A3jnQPpCmuh7GbpALyL4Lpzpu_Hj4FRMUUVmeyRai0GAYVImFtT6gAG3C3ft1TKDJKWcVz-V_690-12lfJurUNrBjDbXWytZvEYaqhpSqYJfn-TFT9inKSR7PqEY6CUfr-MDStIst2XXF2DzyEMy3mRdI4D7MHKcstZwmVAVIJ51a7v_OhMNmfvsvikZZ6RMFm-RZV7fJ9ZGOvINsvQ7vp1gWN92__t0od0w8yEAbOjLm4pX7Vwn-CluSkKrf5WEOz-NtxZm3B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از ۶ روز پیش که همتی گفت ارز به اندازه کافی داریم و توبازارمیریزم. ۱۷ هزارتومن رفته روی دلار.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28903" target="_blank">📅 13:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=Pl_mNfSXuhzFW5eGeGm2ONXB6XeMZ3ysedBvDLCaMlLDVu6VVv_s06RQmth7uFKgkvVxpKwfjwnvhUAT1Uim9zDoSQdabGW-xq4SYXLYdOZASTwel6PQonruJCpJwD4Cw3Nvhhkp0pw2mneduj3VkZ1ZyABuFXltFcoFYAV2DNTreVmPbNr9K5c48REsu1pNr0PJDaj9c14onG_uN8k85MJCmPuNzb3Nrdv4OO6jH6DGVFEMzO1NavsXiqJ_HWy89lmERXDu9bsTRotfuLe2LhfprvbF4kEuTK-hvM9R-HnOTxKxOL2TSzMLEFcZv2cIgIrQUq5KcloLwWp5JtSoXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=Pl_mNfSXuhzFW5eGeGm2ONXB6XeMZ3ysedBvDLCaMlLDVu6VVv_s06RQmth7uFKgkvVxpKwfjwnvhUAT1Uim9zDoSQdabGW-xq4SYXLYdOZASTwel6PQonruJCpJwD4Cw3Nvhhkp0pw2mneduj3VkZ1ZyABuFXltFcoFYAV2DNTreVmPbNr9K5c48REsu1pNr0PJDaj9c14onG_uN8k85MJCmPuNzb3Nrdv4OO6jH6DGVFEMzO1NavsXiqJ_HWy89lmERXDu9bsTRotfuLe2LhfprvbF4kEuTK-hvM9R-HnOTxKxOL2TSzMLEFcZv2cIgIrQUq5KcloLwWp5JtSoXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28902" target="_blank">📅 12:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEZUPkaz-RpPuMcewGH4YhN1eysStEcLXxVzEafGnfmpVrpZLUguSpghscfNS-w3wpYDUKxWQpcWC1y8Da8tR0iUCuOJQ8cVe3gISMRADqfEQUWhzR8IztfOXDdOBla3Qz_99BE-ajSr-zsWUcOlHrPeLiPPkxF6LsSYmGy_ny1Lq3QRRYjlHkhOIMLLNkRvJwXx2Yrguiger74b4CCwqpzrm4OjQ1j7gt1OVDeAOr_Jg0UJM9MdAHU40TiDMIN7vz5yUH7lYBObcntcMp8PqRSt0t3L_3NLKNudQqIoD4M0TVKYXENzrdRHzfNzkyfy7O-aC9aXJasBX_zuzNA_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28901" target="_blank">📅 12:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnmkOlozmdOvQ318lWejfEsUp4nMoVeVeBFX8aSb8zBMSFyq7AautaxoUiURox6wqbJ_GDiTg2kQvVU-ONFRJC096ckkAhl1hX-lV-UM1gHr3YQ4k-MmCf0yvb1Hy5kzv2DC5vNcoM5UBeFnsA4nBV7ctjtMDRTNfaCdSBetjZLr-irvIXP_LsL3XBTSok23-91NwRbCO3SmWBUleuP84XZMRlvA0st7UTMqF_qXEKwnQcg49I6gdUvG7Fy2kUUEQEkgG3QdNdTiEUTqKG41u4OJnxh3VexIHRxHcy4jpgGDaEPqFL2B3_PVYWpyDggNFaziMlOOumap6SKXAQ08zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌گرانقیمت‌ترین‌بازیکنان‌لیگ عراق اعلام شد که شرزود تمیروف مهاجم ازبکی‌سابق پرسپولیس با دریافت سالانه 1.2 میلیون یورو به گرانقیمت ترین بازیکن حال حاضر لیگ برتر عراق تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28900" target="_blank">📅 11:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28898">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7N0Q3kvEB7_EhxxOx54kS4dAcHDg8zqRT5xSIWsDRWap8RBoqvHIZM7X9vUHLrYCIwmGudseuRmH4cNHoEC4CuQjW1bgRBd8MMaP1Tbn05CRXZNuGF_0p8S5NvzqnTCNKXyXuzdN54U2X7-KJ2o8ajozAcbexANF_SjWtzlHz7zcyKFEFM_EeyqoghTD48OYtC4e6l7GBjSH1gIh0dgXjRU4SSftFVckOtaXp9VmJ5k2j-faMVXQtRWSxj5Y78ZPGKkGSk83u2Jl6eptmRGELJ6iFYCFjZvwhNnNUanAkAuJbF5moZNbe5uRUwD0Z6-Sjjw-YQgd7EUdxsz1fSfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=D3hfK-3s2OjuIX_hPOVBJi8Y08vcnkzRtViRKgq9E5SHZe0jmSySbUtGlpKAjk-Js7ObWwJvrF0c-3ITsLcHnWQhEs_tmvocAtbHz5fwerGzDMBgYeeevI6gbhbf5i42cW7yhu-OvIybJR_9xAQX9Vfl6s6uF5leJ6wKu5OHJoL38K2IAtAajegXwTbwjK5EPieLtGtew1AVgVsaequiM30ek2aIP5-iAz4ipTJa2Y1IgBFPmslYnEgQl4YgPa2MuW2SzbzVC5ZJUqF8lUgMIRGg9BF3-63oIxjsAjOrv1OyGpTcnrfS6mILP-S6BUBmHEZhNSV99BhwDCa6qPAoZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=D3hfK-3s2OjuIX_hPOVBJi8Y08vcnkzRtViRKgq9E5SHZe0jmSySbUtGlpKAjk-Js7ObWwJvrF0c-3ITsLcHnWQhEs_tmvocAtbHz5fwerGzDMBgYeeevI6gbhbf5i42cW7yhu-OvIybJR_9xAQX9Vfl6s6uF5leJ6wKu5OHJoL38K2IAtAajegXwTbwjK5EPieLtGtew1AVgVsaequiM30ek2aIP5-iAz4ipTJa2Y1IgBFPmslYnEgQl4YgPa2MuW2SzbzVC5ZJUqF8lUgMIRGg9BF3-63oIxjsAjOrv1OyGpTcnrfS6mILP-S6BUBmHEZhNSV99BhwDCa6qPAoZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نظرت راجب آلوارز چیه؟ لامین یامال: ما دیشب ثابت کردیم که نیازی به مهاجم نوک نداریم و همین ترکیب برای دست یافتن به UCL کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28898" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28897">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfbWYz_xnPSKpb_Bhpgf-RxsvCVHP9izEMmLSluQmoAGnbeldoPw6qJmNq1Asy-MZ3GNv3qEjkkZ493SICBg_E81RTGcgacHnRpqTPJnyWwoT7QwTsrUvwrsAiJ8gcZmm5UzxWlbdBFB5asG-gIAF6pIJABNt1OOvc-1VbsHiHc_A9hmV-u_VhFYyVBdS-cPoS_tVl_OVcHXN4-0Zf1i6kyVtPiW5m5nt9DEMU1CHtEzDTwlWmDFPO9TBeLIirWf2sNSrrFTXqiChjVe6k3GU3v5IFb5twuDbm6U6_UgqqObDbBv1XzxffAhGluwpUim5AbNckqgm13NPzT4a1Tp3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه‌باشگاه استقلال این هفته با عزیز گانیف ستاره خط میانی ازبکستان قرارداد امضا کنه بازگشت داکنز نازون به جمع آبی‌‌ها منتفی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28897" target="_blank">📅 11:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28896">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfSiywjI3YrsGas5zUteW3L7tBLn_HqNcqf3YmYsgGecE17JGl4vsu9aYLh7GzfM7xmDFiMbsFaZAcMa2nr_MBdnl9fAhbIlF68pUMTQNU_XKOfm-pHGObNqndkMQtX1UR152WRNHk2PyE89qwo_GA5n86P670vWgIxDGkrwLMP4XUtRCA7tJUD8Jca_kshXI7YmRorN4OMICZJWLtVV51Z4CAPV2tWCJIe8wGaBzpiu9AsjvGCZw80zuxW0dJmkS6qQjQQL5pZ9nfl7YeIriIHm6sR4yiPYuPbh3s5rKcIrPqHXzlWMS0_RfKksdYNhQHaZYgXd-NHO4srDFGMEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو شماتیک ترکیب احتمالی از استقلال و پرسپولیس که به احتمال فراوان فردا کادر فنی دو تیم با ترکیب‌ها به میدان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28896" target="_blank">📅 11:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28894">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y99qTw_njheS5N4Jg08gQhvc0eoogadDVRhFJaVtIfuOp9R0voLGnAa9iSzxR9a25xTt3MPue1tf3GBDMFTUdVHA1Ixu89ir8R3Yp6OaWRj7uHOmRiby0ezi0UNsPo5sn2IDYtLSBvghZqsC5dXzaS_yH44psG75tc-JCclDVVbJXjNzD5UNNL2w-SJZ4Xa-kVQz7juAFi0yxuvpxMH4BkiQfJWbNXn4RjIY_7bzaG5TmoN-8igtNdtDhbM7QFWSDlJ_sPROjj2o7yqFMx0SeWOJOZFEFjyGSV8byICsfJr1Nb36asn3ctju66d9kjRtrWciIbhbHQ88UOpe7S7ieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvBJvsB7kFg8JAkmv8JXeO7FEI0I-VhbFdmtWeOE05mJeRpw4_t3tnFPO469v776B1PL8dPhoPKPDH6o911jfHVqxjSaTD5XgBANLPaN5YH499c9eReHqLiwUbJuyS49aoh-ECRgCDFerS_ZQrvlDoXRMQjvjIjFSvr_MenJ8SkBvdGRxSlulUU8pkd27fHSvSoXqeKkmn0CMaWkpEvmn3AV2E3X3lHvqLnDLchHseasVuAHvJQiZe3huSITfIAR3z24-iS8tLVK2jsAPP8zvckz3DuteuOXw7crv8faXbE7EsllkBz6oM9W9rF5UVioSDQaXDwALfKV9L_5AdPuWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28894" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28892">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvK9fx3HJseH8RsHFTArQf6zFfbWuuWlXAfL05UI8IYr7jXpDsUCL12eriGwhVZY81YEqC_a9c083kUM4Whz0vvYgkgOkJ-Nr8DlPWpKgtMKoYc8DfcKZsnxrnFF8Cyc3xZ3lqSlu7aA2gwSBNHnRWpXaZt_up1YyhdPMm97v1jBtKGh13sSYuJwlNsb2Le7C0cKlcMSm6MKOXzfXZjuPPsNhrv98ur41i_Y6fr5NFvk3lvehTpmIv06Qoj_yQK9Ghkxn38PJphLgEykBOFIsxH61hw0jD8F3d7DjimI_nqdS92veDvXfHAE268DE0Y1xLLEljdPwCYZmysCAWIrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28892" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28891">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=UP4PW8TnbdhL7b63cSXL_OJpvzSQNfAg6TcvKNRNtf5D5aYV9ctDJzb-2dIPxMjupYLIofrRtrLxlQMjMLmliHLVL3L10gxXcE_M-Wc2SVJzhk6i2reuFM2N1hKI8l8FH5Kp_3iXzv9ufoC3o_0eXRfM0AbB5hmBdfOps39rNmhTNXkgZGxl09DoX-keiUBHBDFAxFG_Baea5UbPG-ckFXJq7D6jHbA8eoKTwyWhObepAHdaB6t9fnNERvd0SlWtf87GjVWp-NxpWUZT1iDNc63r9HRr1KyjlGYsbGR7jxCjjQZ4jSPT8Xe2fo7SbV4dikpJl4tf-E2osN7yUF8wZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=UP4PW8TnbdhL7b63cSXL_OJpvzSQNfAg6TcvKNRNtf5D5aYV9ctDJzb-2dIPxMjupYLIofrRtrLxlQMjMLmliHLVL3L10gxXcE_M-Wc2SVJzhk6i2reuFM2N1hKI8l8FH5Kp_3iXzv9ufoC3o_0eXRfM0AbB5hmBdfOps39rNmhTNXkgZGxl09DoX-keiUBHBDFAxFG_Baea5UbPG-ckFXJq7D6jHbA8eoKTwyWhObepAHdaB6t9fnNERvd0SlWtf87GjVWp-NxpWUZT1iDNc63r9HRr1KyjlGYsbGR7jxCjjQZ4jSPT8Xe2fo7SbV4dikpJl4tf-E2osN7yUF8wZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار!
شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28891" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28890">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLf_XVhgpeFVGPaNTONCK3LdPLjjn6yE0a747pdYie2_BoFGI5CcUI7H54izNmRj8t_eMOFeYsQ1H_0Y-bx5dA2oZdp2d43wLcDl525x0qROiH5WhMoPGDs_RHe5sG2o07HmsIvJ0pHUV4FSaq3RWhSYpr5AI26BvoN2v3yHsDSCS0-uU6YS00CrzWANuchbecViVzGKlvHK82IS9PiyhU5-29XlJbTzYc9cAa-QzDAQcQe6SR0wOCDEL0FW9fn59RIl5zHYAVwSeDAQPd3bJaY4ZyG1Sl_WWrh7wGmT_6_iL0AJfkEAgBN3Ov5ij9i_UrPfrsB04eJ1VVro8fcPHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ دربی شماره 107 با جدال حساس استقلال و پرسپولیس در شهر اصفهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28890" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28889">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg1AovS6uFNrh8HsNBEW_ut7NQYnSj5OSirJCfL9e5Xhk9EjjDUe9yEFy4nPY01EPgfBs6jZYIq17bamZvaTSsWgRCrQfDsAUV7FDigvRqTx2XcqdpqnlOCsxLuZ8h9EZ9Gw9X89RPUbRNJdoicinG31S7N0Jkw1D34zklmbEGjFQx_iFvaky5IqN8Tux2qHy_xN_LiaDvYXI8pLPJp5prRS6FlFwEwqM4AV5mueXL363S5Q2oyTqrG1RFSTkNSjNqSF5oDsM8wxEa1ACW2PyHOmEyytc8rRztSS_ZyxUGYTHi4F0LX4lD3-zAZly9i9JZ1PC4GbTD3KP_B3DrHCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
ادامه روند بسته‌ ماندن دروازه تراکتور در این فصل و برد قاطع الهلالی‌ها در شب گلزنی تازه‌واردها؛ واتکینز نیومده گلزنی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28889" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28888">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciOoJdZqp530L1QewCzxaViLv8zSXV7Y_RwK28fMMwX0TiN2jyGtbv9O2cMaheKjg0LOUzPQtpd1mWdVzCT_wgEnfSXdkDUTaP8HsYTL54DOi1WtZWPjG-N83mQKTXoN5BT4Bz2eTyaoAsV-OWmDRNB3DYX68IRIps6-zdlB6uHgx2YFzcO7Wmu-b7yNu-LYBme1BkGw2vyrD6kkKhY9SBwCpUKyclE7CB_M_-qsVWPTPaz3MHLJxzkvHM-xQ2hwh7un6dSpiBD0pu5SnVKw1YP8d25HggkEeeHg0_qK7AZ4gnjhJ8fCv8lhmQoDx7s2kwJOJLXGdXau3tPGvoW7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
بعداز دست‌دادن‌فصل توسط ترابی؛ شهریار مغانلو و امیرحسین حسین‌زاده دو ستاره پرشورها در حاشیه دیدار امروز با شمس آذر نیز مصدوم شدند و میزان دقیق دوری آن‌ها از میادین مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28888" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28887">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJcsPhgycsf1q4M8lMKWDHN1KPhps7PxAHChq8s5Hh_itylOnjBqXulmlHZlOKbdlpzJu4P44YV1zEQVpAI4lCqCQouqsA3886v_VYungMhYBi7tmZC99ITedwI2BdMV5qLxbL87GFSXehS6uajw5A0sDAhefrKcJbWoPBb1zCn749ZYDWqiB6PvTDkdqxBd48cnyiNTpRSF1L_lzBJ4rHiD3vgCFDSUxM41erkK30upn0UhgsundzJ4Me3U-kWdOa0CsmxX5ISou1y4Jc3uyyXqFeN1asStwDaKFEcL0DjOHnrO06oJG2KCBtb5BnYldqXaUjqztLYRvmwe95Rfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28887" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28886">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOsJldtoBr7QfoIwpUa7yQ-r9l5eifhjWuIKg3TUE6VZEUjkAs9G8p1YGk66vd71C7zt5xGRoyqXj0lg5AtAl7eJsStDiDo3-NDkpd2B7ZBJLJn0r2Rr4hg19HSgul0GJ86-sD-xtqSxCxt7HbQGpUsBuwXiawq2ZynAjO0UB0xo2I391ryw-FZxOLa8Put2HFF7HrDTPhtl3vURGQbJPbT7CFlCw6gOalGLMtm8XDMUj1dOxJlz8NJdMH-m10y_Pim3Z3Vmne7qCCuN9ryVbO9N7tXetY0M7sfu4pxFeZp5M2VuFhjgQFRro4p-AUE0AYtUuSpM1Aq78Y5e1D7NAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
لامین کامارا هافبک دفاعی 22 ساله موناکو با عقدقراردادی‌بلندمدت به‌چلسی پیوست. آبی‌های لندن برای این انتقال 65 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28886" target="_blank">📅 23:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28885">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THmRDGpb1MISeB0Hdu-Jze81JwCiTnvaytyoHy7lbKcxbQlRaQp2eqtSScYNNljoRwgcqNGIZvA42XSHKqstsIKwXdlLkGja5RuBD1E8sTz7U3yXzPFv2x5xPNDwGrtv1VKmJTJCcnw1sYCpDWirR1JKXI41Qpz6MOxKYiIJObaCNcT525TeWFqP74xxvo_tqUQET-B_Y_LWmRAR-68T4lyL7HM2LkPz6-X-ni9MpTJPczhXQ5J0xXiaWGgM8uj9Kei4PlyI1CdN91cz9qfNRwQg9LHLNViU3osUlhAJ3Q1yrwLFnY1slhbLdjxkiSo4R9d3OI0guSHoJIDOb3KhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره "9" های بارسلونا از فصل 2004 تا کنون؛ گابریل ژسوس صاحب جدید شماره 9 آبی اناری‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28885" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28884">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koqsxrlfggr7QN3tQSmHc9n0lVHdBae5YX4WOvLDxzvlzuH4co_U7CpZHz1kAzB_1AlKNQ8CSAQD8htiYEhs8ZNp4LIr-f0fH2NY6v30dO7hRxaQsZrgkCmby4XiBugK-MkR0VE7a7wLGDdDuoO96z6J5oKJrNODFtRDbRjhlfL_dGAfHCovqII8x4sgAHi2pRIqIRnDDI9PeUDu9EXRdwFrpZbXDzGnimjeUIm0NYpH2yvqQLGzKuONOKaqBrAZtcTIzsIlL1UrAQXrIFGgQbc44iy5Yh0Pz3ewJULVXrzYO_CQmoQjRVE4ugorRbFfUVjUa6CWGO0k_ci8EkqehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28884" target="_blank">📅 23:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28883">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of08_GyjZ7bXzYhC0tpSbUYBgjQmyQywpsf_raiyWKHDV2cEq5R0307rqeO0GC2jKzqGUdtxHbQK1A_RJHKBeTzrQH0cV8Iqk8eMkr2vbcEgdRlg9zF4V0WtasKNGbp8d_itoYF_rk7DoZbMcNOz00k-R_ESd7ZUxBEkRtuHRZysXxbIfXZiixuL579hSyKHQcJJ_oQtiBYakN8U1jpOitzvl0jRY55BYLj8g0ezapUCs-J7Q94k6gZebEL2K9dhunxucvb6ik_uJbjXS6Wz2cebjousUTJproCR6-TRj8fnrja2C4GzcGLxtGWS1NE-OXeVG5qj4yB0CprTaZCWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28883" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28882">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghoUyIJGENPBRJHWW2Xjx_MHbqMDYpYCltMYoiQemS9dCRDMCsOFiULngyKO1NbH7xVRhzc_6WKP9njbMiXj82otTYsYsNTG3pIt-0ty63PRKjFpiD47Sp0QCbNrJDrgL4jJVdQzC8HkjTaEy9fi6uQnAMBWuT9Upwg_uAK3cByYpS51EkUMtE1WcdWXJ13Fr1qyIeNLXV49d5ddxTUkRNtUVlHIJtQN7oJvAUXa3KfWc29z2tIGeFmJs_-mO2qiuUcl1ft-IFsP0nQqDiaGw3hqSsSSuGdh5p0Xz2ux8lf8SskG3JsrKPHd8Z0Kxw9x69azBYWKZVaCJj8lwKFbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
به‌مناسبت‌مسابقه فردا؛
10 گلزن برتر تاریخ دربی تهران؛ علی‌علیپور تنها بازیکنی از این لیست که همچنان شانس گلزنی مجدد در این دیدار را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28882" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28881">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdYZai-Ra94JfoehZgDZLUiOQNimJ30hLHHP5LRgFtDWV8LTDdl2hLG7uaZgSZN03V5g8yWJ1gZ4M0_uCRljPd7-3Sdg5-KQeXlqWtABkdqJlJ4UpIPQXnIQZkWt1hkZcd_quuIc-hjPQFjuxad-INMFYLzPnj9ay_DiM8-DuTo1I59EwNwlIhG9kbm-6Y5nozpvJrx9RYyoCY4nTc6cDa_c6QhVJhiqH2thwNSWLdqF9aK0EXDkw2Jv8_0Wt8W8JmxJCXxrDsJ2-RlXqWxRHHubL2mFNS5O5DW4E8u89JtO3mLMd1dVR2t51FR4LBD66dECchUaEOGac-T-15JfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28881" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28880">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=u7HNoaraXafplNAIjznW2U6EECSHIxBwWOWUSILvS78aKi0nGKrvrLwooRR7rLQ29s6E8wViYqB_dtfTkRl4NLjKBODdVd0bxWCYa8G7GE3euaA8_-zo8or78xe6oMjtjtFv2pCGKNyLc3EW50T-LuKSDW-yQslaUa93YdiOKQfUlueBEa2ypr7x6Glrm-mpQPYAiwUG1XSknNREwvDNwBcczaKmGzAQcafdszaIiRRr5SOt5mKA1CQly56r4diX8a1WNW4IgLdi7G84zoweBrtBatTl6Ls4HMxj2QNmmYRhi1PTllo6kaiYVZDkH80KSQ7R_XNj0-aAHNJ7aAMw0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=u7HNoaraXafplNAIjznW2U6EECSHIxBwWOWUSILvS78aKi0nGKrvrLwooRR7rLQ29s6E8wViYqB_dtfTkRl4NLjKBODdVd0bxWCYa8G7GE3euaA8_-zo8or78xe6oMjtjtFv2pCGKNyLc3EW50T-LuKSDW-yQslaUa93YdiOKQfUlueBEa2ypr7x6Glrm-mpQPYAiwUG1XSknNREwvDNwBcczaKmGzAQcafdszaIiRRr5SOt5mKA1CQly56r4diX8a1WNW4IgLdi7G84zoweBrtBatTl6Ls4HMxj2QNmmYRhi1PTllo6kaiYVZDkH80KSQ7R_XNj0-aAHNJ7aAMw0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
الان رونبینیدکه بازیکنانِ ایتالیایی عرضه‌ی صعود به جام جهانی هم ندارن، یه زمانی وقتی می‌خواستی مقابلِ این‌تیم‌بازی‌کنی تنهاتاکتیک و راهت دعا کردن و کمک خواستن‌ازخدابود! به معنای‌واقعی‌رقباشون برای سلامتی ورزش میکردند. این ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28880" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28879">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTLRWmBC4D1uhwQmxHPk2eVfQYIpJ02tppp8ihCHDvW8cYNZrYPn9C8rHSRSMP8pyVoSfAw15XK4fMngQjOOpFtW1AIiOQPxO8dMC9Idxd1H6iEC5imLqzAnyTJ2K9p8RSvmQ_eomO4YtDIK1E-rX43E6mBTKL0ptoQF0yvJNqnuKzo0XzF4Y6o8luHHip5TNZ5qX6q9fA4Bm-bk5vQSidQhk6otzEIdk5lQtV2i3RNSTQwsbpjCgJCja6_cFEBQS3qIbt7wt68qLSj0hdzKXTvHsKmzpYCOSr0l0jr2nz3AP4Mv5zqUvUR2TLF6GJqi6cCfuRqwqeSvNIEOsykKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
به‌ درخواست ژوزه‌ مورینیو؛ باشگاه رئال مادرید قرارداد دنی‌سبایوس رو رسما فسخ‌ کرد و این بازیکن بعد از چند فصل حضور در این تیم جدا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28879" target="_blank">📅 21:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28878">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3t9pTsFSNKTIeJisr56vHGVD8bB42F2TZtmegjHoj2-MVQPS70r18i8lwcir_pZaozGULUo_4xBgSU7slTDGoCPrntD3zukuZKvb5Qt_hfk3MqHB2n-TVXwvzXnTLEY_nBuuVA3WZsiNAwJlLeEGN5F4fLjVUz4tbrHGKZ30x3gl2VYZ80Vp7c2fT5leY2vwemCmzz7gZ-NG_tmK_evGr88Hy7CHOh3L9aT3jxQAO5FO0BnRZRzTmGWdOO9TcpLMHw2hWzM9lLPiEuSoPsAFtTTG7u7OmSdqzodft4f3tomhSgxkZ0HTf5rgrhUdKraaI8-OBB0dfNqok06PtksAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر
؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28878" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28877">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=WQBtm9-MorfbFT-qNk2F1mQBou43GnWVbxaL3Oa-cTJecSK9H-Gcjq6h0pRrYBuOId9ZgYWkf9_W283fN4G7dlzSsmN-GwS85CJf7FB0SiuywF0t1JV3XtQ0dOfTOFqEhDx23AUriBUsxha5rXrG81FcdHF98-C2xAO8rLHNDQjuoRQzMYbZeu_JwG014pDTUNbYYV66TQEdPBNPbBu8nz1qbqa_q_RS4cHm2Vp7LgEejVgrmABZKnYOVp-Lqe5Tb3V7oQNtFXmQKqaWdGAVKbNsvTrK8GcPfcL7rMEJl_i34HDVYvL0wjQLNERQ_GDtPSVczBy7c4Yaqt-xcsTlcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=WQBtm9-MorfbFT-qNk2F1mQBou43GnWVbxaL3Oa-cTJecSK9H-Gcjq6h0pRrYBuOId9ZgYWkf9_W283fN4G7dlzSsmN-GwS85CJf7FB0SiuywF0t1JV3XtQ0dOfTOFqEhDx23AUriBUsxha5rXrG81FcdHF98-C2xAO8rLHNDQjuoRQzMYbZeu_JwG014pDTUNbYYV66TQEdPBNPbBu8nz1qbqa_q_RS4cHm2Vp7LgEejVgrmABZKnYOVp-Lqe5Tb3V7oQNtFXmQKqaWdGAVKbNsvTrK8GcPfcL7rMEJl_i34HDVYvL0wjQLNERQ_GDtPSVczBy7c4Yaqt-xcsTlcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نشریه‌‌بیلد: هکتور فورت برای پیوستن به‌‌‌بورسیا دورتموند به توافق رسیده بود اما مخااالفت پارتنر فورت برای زندگی در آلمان باعث شد که ستاره جوان بارساییا قید حضور در دورتموند رو بزنه و با قراردادی سه ساله به تیم رئال سوسیداد بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28877" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28875">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uO34KKnihy-Azb7opymIbnC1CYPxWFsv9q0cvOOUTsCOd2fRtZAY6pOgWAHnWpBmKTK8oKN9pXFOgbtIDmCWVV7JeJ_iiwWe9b_FdmuFLnnQux8u0-E-HhrqWDYlLpRtYqqKvehcA-NZOKkTOOSGE2jytKR4wAe2eGcUY9pKSxGCV0GY7BJBQETl6DtWuPPThltyqtrRd_4jrprLvPY3CmNLZWn4gMFBlkn-Q60RcxQ3XqXJTCf6i-iREGsSR4ZcMu4GXOgN9GHse2PPC98iS4qPH2lq0qz3zC9bo4fx0ypAL-gtTAcWsYNcTybblh9fV1x0c5MGfDCI38oVwgneKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28875" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28874">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWyG6Q71SwOFSNz63EWokkcfuez5UKYhatllr0Jg2cQ7CCCXO0gCXQmhmROpQBkY-2rWJKHKMbrOU-V6VN0nIqwe9XCiUsjor1tTXc1U-djMWk5dCV_dHFogr0I9Kvy-yZpBBo06LdLj_tQiGDsumADX2QuaJkjPUp2Cdhnw-nZB1VYQ3CefaVVchhruvi_maClJKwAHG5hBoRn8fM53-oICcBgx2TCtZ-f9DcVnxUg_f67RuCsNHMMjCXxD76eJWGNyG5ofSJY_eJ2TxK8kCgSUzw4Wj3IJ57NWFsV9AZ-dZKolllgtXDXKOr50tdMi0Cbf6UWq7TJ1RhX0q02PQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگا رسمی باشگاه چلسی که گفته مطمئن هستم با ژابی آلونسو قهرمان لیگ برتر میشیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28874" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28873">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnmB-JB-Iqwg9FQQ24FFDUM876lfjtQiS_ncBnai9QczLYYf8Bza7ziep6ThHqtt-FOlR_5l-q45qas8hzEi7fiASRjzkiV2s37z5hZTuEBB-sV0DdEjj__tWzpy2epgxCWrMlmX65gBEu9eXOIzETMjAjDt6_eIxTEK6qCx3R9uPbtIf8CimwyRaXlZN_dWqXQeJ9S_EEllRJ5FO07fWsbcj--1gb9WaTFLyRjBvtDS6vhFS3yAsSSNr0aoJAIIp2fLZZIIqaOzP-4X2eXwRxBfVA32os6HGe4-_rRyTOYHT6T6_l-6Cr89BY04k5CGTtBnWN8fyvk5VNhPtNAnNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28873" target="_blank">📅 19:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28872">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikU7O1K2qjRNsysu4FGUKWHUek50JmlNixuBJjXUn-B-Yg6V5OUnpNke0xqcIxvELnVUCCiUWZ87UtYytvBOf4H77HyvNOPgnfxlHKCU9SSqVuOGeVfqdh_0zsH1Y2SOObdB0CBvPjtuxE26mHgR7ZAWxHXkaxzgNNV2MqwDr0HnKSOcZyjM6A0crZ-eDruDHexGfNj2VBpt9Kvg_o0zukn3e1O8wzARY13qIRGfA8lTkt2xqaHx60Sm6TLN7_Kw7le06aIlHHjL39p31Lz--QGbRqCsryWrCpg2Wx-GknMg5q5sTNeU1dkscSvHib8m8q8uSpZ9UrdnBiufQCOJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ تا ساعات آینده انزو فرناندز ستاره آرژانتینی تیم‌چلسی با عقدقراردادی تا سال 2031 به منچسترسیتی خواهد پیوست. بند فسخ قرارداد انزو در منچستر سیتی 100 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28872" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28870">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSI068wA4tGOSg3B8xqa_aqVR36LhemlGN_x0zM5ogMFzVdSSxS856vK1RgAlY-tnUON-pkpHGSytdzP2srENRKmZ1Jh3en9xO-JH8WgpIrJGHVftk567yvrPXzauIgnLn2JEu4kK54i62kycO-vk5oVquL1-grvOZQL940gxI_CxtD8VF_JYMRLDc6cvqfiDoShbBHsglzlU8F9AfHKhyk2sogM2tZbJPsi47qOoYAd2-zgSnNsKcv7LWaH1WxOIo9XJt64ErjZoBPpN0lPHqdqqleQiJAA4ljvZN4znmXycC444S8tT_I_peGCpSNRLTWqF8kmPKO_RejRjgVWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3bU9egnvBP0WXHjIoRwDgj93ezQbeL2au7D6j7xzsZ9mhtmeFWOTiA9mqUP8SNPPxkdzMJf0uy9Y5qeG8qKIuIrYgcNET04KIs6GEC2RiyPLxpMjkwWDcv_muQcyVomfoXLsbSQa-iJW99Qg5-pHVhAbJA-LHvdt8wz7I_ouf0TA4C8ew-nYKIm2PsLsF3uv1TH2xvmpw1AsX8WFTAVR9VbQeWu7-H4mBkUn9WhUqiJtt8Tpb7tmm2nq_1OWMAG9nEfJYE714A2s34UC06ndsugO95swYjToR-fmq4VATXsTqOSajX1O74L6v6WXkMqmj1r8UVgW9EDe-MQvk7f4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کاپل‌های‌ فوتبالی که رکورددار بیشترین تعداد دنبال‌کننده دراینستاگرام هستند؛ امباپه در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28870" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDyzgvLlvGMaIZLVNf4AtA76RFFpj5fBbprG-qU5yhyFPtmGOSclLjXlEdEpnaIvU4NOsdMK3u3SfrOuuHZT1gP7sHIoTYrAHeSoZCBYpPq0QPXuBFpSwyw1D9oj2hm3SWHNtq6WObY5Llf03LyB9HctHHsF7OrGoNmc7gdFPm2UICZyofSBXRfdAHErMOioueQFj83OBep6HIHsElAX5sc-RYYjMBsYtQ24htwOTzU2Z6nsT6B5_IAm2bPN3dcuBH-y3T-kf_7jIYUy9VptrUnXXcv4a7smfudUowGFoMvp9sS3bhz9-FcPdF02J9WygWN9QLjI8m5UI6DUfsOdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28869" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28868">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHDoh_WJckWIc0qkSE12248Bj4rMM3x0LQQrpu_5ezhAUIuE38u5ZHAgGH-ftaFHDTjthkm4bs6eNEiZznOaTW0nCrMol2oojd4mYq-I00zpkq6H6Vl3PUwe7cB11J1jLg0MpdZEBXiCEZBVXxcgyKIR5VqEQESsiT27VkipFVEbNWGaERLjiOjAxQejGIqOr4W3z80K2XadgWN9nKxk4jloF7p4O68gkZbrfPe_Z1fYEUMWTNtxUdTGIVf6Zza7F6PXeouVMj_WLitlajsNV5i9T5x366ad5UzQSRTSuR8WSCVo9ag4xU01PhyeIpPLwq6FkVafGDW4xJYEXDab5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تقویم
؛ سال 2017 در چنین روزی؛
کیلیان‌ امباپه باعقدقراردادی قرضی همراه بابند خرید دائمی به PSG پیوست و با به ثمر رساندن 256 گل زده با اختلاف‌بعنوان‌بهترین گلزن تاریخ PSG تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28868" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28867">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPipaRUUS4j1P35V0UJ4yVIkXMKZRsXgvTD9Wzw0T8Slvjx7vwi53nsBhgMTbBfHpLEEC_mmMxc5SUCDAj8-EhD-Xlfexe7q3u1JAMLaXpwiiP4y0Mctp_P0NhTItrxgHhraafn9f9AuTWtVOZPG-BxQfawNbj1JARlKWdarmsx-vQMFx5xkgN5z7fTnN8qy1ohMBeKkz7Z4ms1eYTP0W7RnECfQ8YIXhtqY9fRuGtWeAwhs2Oe8Vf0kKfNeDFZMRW-5SKsubVEbBVX73hYR9gZfYewNUuEUpJyrsNrENpl1tWbYFYGXHhkRg1xGNDjLM3aSqy-kTP85MuYK01-PbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدار با شمس آذر؛ ساعت 19:15 از شبکه ورزش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28867" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw3PcLMoCpkUTOTJ0PG5Ep0NNqUCCqp_Dt1g9idd-vvDPUVyI8Fhy-UiLM61TdhimE9SZ5-8gI2B7aq3g2E6D_ebdSm9hYXgd70N1feiIZtf2gw9Q5KgpvPGCSaR4L3ZqsycFQJi0MLyl_-Q0TsKBbbUEspOVdLp5PE_NtiRn2A4Lzix8EjVaAhO3L3S1EtbtIKuVw77bOfQfbPT3Y7e8oA7zfxV2T5Rc1dl3CfOC9SIgpXJ1u1P3RLILCeGMqvCuHYGDWW1GusHEa68b3jHNXHX5UTvQHUbMTKnUnGchxAoHsX_w5wU0CUfDCsh6lxAivlbXahFdnPAbswSZ3h36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28866" target="_blank">📅 18:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28865">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6OhuBK2I6XyKf9Rn_R58YJA6JhCs5-TjqfqPKtmnsu8awdgQshIRusFwv46u9B_aGPUAQuLjrpaTXLcHcX039hUNTHM2a7Zem-XqTL_OaWy7fz12hZzH-cb4DhPCq0jZ_oi-UWTsleiZojDzVIjbobAMEqEzbE2z_I1mph7adCkrpWy-agNtzkt5NWpVg7DML4sdomw4xsXF2nhFqyqQmLSeCsVMmWwRCeXFiU97Ot21SN8MGJVvbhN7MZhcuhoqep7Qte2ISCbK1Zqa5j90EpMc0YbQXMfNFwZjiW5h-Gcyu8dSKXU5dX4l-5WOh2jJ5zYkfp5qsGBidemOegvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و پرسپولیس به بی اهمیت ترین موضوع‌بین‌مردم‌تبدیل‌شده و این‌حجم از بی‌تفاوتی قابلیت ثبت در تاریخ برای نسل‌های بعدی رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28865" target="_blank">📅 17:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28864">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ae770053.mp4?token=kWbQdXcRRaUMEHAWGsO5K-uvPprBFM2XWthAuud8RwN2SDSBy3pMSJgvhy8xW2XRZGwH0vKJrh9CzOLcsL6s9QAYnujovtKImyMB1kNYgx8Ap_yXOvVTd5maTrcPli--4N8ML9QKmLl6pR-sVTcC26_iIq2qGtGi78bwIagwYqRz82dm_RRJYvXmWU5P_RYPkkgbVA4dwZFilIRqa0u2SiLPnlX4aDSXH6D9YZsto3Vjd2G8jUGiJT5wHFrjj_t756M2qhEhWWj9x8BFTMu_I6Ui1TD_zwI-ykjFsxZLxhytO_NA_q08pWF4GEJ_ndWWckeFQqJeJb5CWPokvuH8pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ae770053.mp4?token=kWbQdXcRRaUMEHAWGsO5K-uvPprBFM2XWthAuud8RwN2SDSBy3pMSJgvhy8xW2XRZGwH0vKJrh9CzOLcsL6s9QAYnujovtKImyMB1kNYgx8Ap_yXOvVTd5maTrcPli--4N8ML9QKmLl6pR-sVTcC26_iIq2qGtGi78bwIagwYqRz82dm_RRJYvXmWU5P_RYPkkgbVA4dwZFilIRqa0u2SiLPnlX4aDSXH6D9YZsto3Vjd2G8jUGiJT5wHFrjj_t756M2qhEhWWj9x8BFTMu_I6Ui1TD_zwI-ykjFsxZLxhytO_NA_q08pWF4GEJ_ndWWckeFQqJeJb5CWPokvuH8pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28864" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28863">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8jktnYxml5J-ErMZwdPgJ00TQVtUWC0wPtEbovMbg3im0TxjTtM7cdA9gnH9bpq6995kZROa5EZsgn4jMWpbeK40d0f2qmTFOiyORSTI0JHG3wP3UA7wnCL8i_sfBFjEZlQgTTugfrnJvmizVj-gT2L9n7liWcKmc2nlhxOa3rUa08tYUtre-03TDp_YKKSmlku9C3Zk-FPJW_IEv5PBvM1flk6PZK5keXYB9qHhes3J3RU1HVUxD1Jaa8mpaGqoaX2kkKl_EqaMLS0i_XVLz8nw3Iy3oy1yebyDQfhmSw3d0M_tNf9ZN4ANKMhe3JWjIuFqRKsbbpJlpPic-JzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28863" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28861">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvqDJg-CuPKQ_dNbLm-0Jpe0LlIgrDi-tN8w8xJS5AVPGlLOYkIMR91prgiL3g1o_Mz_3p8PVw1GN4SZ-NoznpWtL3sWqrGay3cYpA09Wuian_DqU4hzfJsFTVRavMG77RjMpInP9PAiIrQO65y4LVce3xVlrTXXb6Y-R_rtNmCO2kFRoG5ZCdR96BlUrbfWHP2tH0viwNiTqHWOYpqKhK6CuHsCKgRlzimVZxQlHEzaU0FIix7ZDWzBbUdtLhE3ichetoSAgGuyz4rbu1vLEj7mzuoHHSwh3o5NbzKCPQka470IS5MID3KfiJ_3_iMG0h1s8aarwtwpZMSA3bMObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnKX_SMkS2KO6vaVV_b9Gj-oh5YcKPAESBw8Q_RWiyvz7YwGhrE_FCXXjq42RLqHybB8-8kVEvCSEdAUZzOUV1GCJGYGQ7BUQuPGEVV3TROGAu_E1PljSyRHkdI4q6PFE_OVK3kjyrpL42p6xJo5MkU2C78AsLoszYpScDLXM87E4TcbIO-UvIRXI4F1cumGr8-1cOUYXuQSH4lMJXs9-1-P0jUD8SLyjm2NDiQOooL65jGIPuOFPirdg2MdyWYbYcXFch5bL4Nh_lYcp6VKf0Fx7oomMQBvRZj1JGpotkgGQcOcFuPgrFjGpVe4fipXlyg1KJUwqY1VybtipaeimA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
خبرنگار رسمی باشگاه‌شباب‌الاهلی امارات هستند که از نگاه‌او سعید عزت‌اللهی بهترین بازیکن این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28861" target="_blank">📅 16:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28860">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFmqyZ-wj68Fj131eRYpOgoPYYGg6H3WE1wai2sDeyl5iopdKsyOykAR8H2IH7oQXDKn6UfFR5E8Yp49A1su7HlAdc_Ivbh1w_aDSs9z3m256zSrbUfu-QopbiUz-PpKmD2Fbow5Ta6AE0jE3U2vWk0okfhcy7EJVnLjsIWkCy-YQaJwUtdRB_qaJkZDJEcNJvGoOSfzL6wZ-eV1NfoSLh163SOPXhLweHqQNEi-Qfxa47OAOIXVAwkY_EIrKfaTL9xaJ_gN-HIJHHh6KFwsljUGYAOCcOdeb90tsRryHxykz4Bptrjf7NVMoGQB0qYGSBoqJOdHoWV52uXkz2NVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28860" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfRNc-IfXmtNcYrmUskfEbwzL-bciSiLSUTgKbuJIGcOh8I_ryE0tj8cZNxQiB-6kSE9CkFDOsRsCskfSO120AAG_mWUgDMzuKe9LFjkt40vyspqKm3uGJ3aJHsIZg8k1iSiAvxzmI0PwNFm9LVIuP_ldaY_0xcg7yBsqwX6c9inzmyvhGZ28bIgHyij51LsK8r-CTlK3oxjDuQp5460w0Ru2-wx7wxOo8TsV7Hg092TZDrHyKPZ6lilY8d0LwqP0PeZJjSSEcRpcmrdRewfPO-kZ_3aBbaw-Q9Qiz3eq5SJyhH1887Qz74Rab3L6XVnyZy9cBpJOT2yJtLDE_vT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28859" target="_blank">📅 15:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CO7FlMvyEzYxxgBT1bQxrJl-dJD2gP_hipfZrfk0p9qwIzLxfm1-UncD7bavFhC1vJoZRUmYwUuMf_Gq2jN3PpcE5Tc2BqZ4wfVQNRhpapgrkwhlcomis-aNAAFZvT2MvKmq0JYbhweiuTwoo7On9TuQxSD911AeJqOxhuW8nkPma2McBdgJYJGAchR8XEsfaktaK9z8TxkeRDKTx0-0R-yxxfbvn6ELv1Rf0etbT4N0Hhhn6wEwKPdV5yCAf3-2UQbpxS-68-S1j2qzF6Cw7XJqETga93M5cVNtDlGWhPvcFUHUhkDKvQKz2OV0vRNy4e-qhYCeCXyeTZnQywF0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌رییکای‌کرواسی با انتشار این ویدیو خبر از عقد قرارداد با محمد محبی ستاره تیم ملی رو داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28858" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6u66cgEXTfYNJ6nNPrcjUt8EksLJqGn7dhgbGGVImnIJ62MaXZxZgiiQ63iLgfDxgtNbiAwrhcxrejvF5H8ApK_YkssF-nyeCLy_03R7jYGo3-u1svM-wOOm2rpRv_rYiCFQEcLLfafWVIUqNDG0WOLAOQ-AFSa_giC_sDbrI80Vvrk4h1Cm6hu6uSLTu3rgB7ULMA_zATgsc3fGxOlzO9NlD87byOgdy05BSvyiUn3JnadEpzHIarqy87bNBiQ7klk6owiUJpn9ZDsuCxZbw8T7-Hyw2yuRB7g6yFy2ywfOz5NVa4LyUiOLGRMpEjTYHUCmgEua5sVxTz2JaBo5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28857" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28855">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=tt8zFoqVC7C53zsCZVm6bnnxTa_rVtmuLJyHY0Z-ANOpzCKgbjZf_FTISo7IgkxQgC6T28MZgBcEAGZykrOqQv-dlWn58XEwy1B8cMM7TDe3NRU6c3ya9WODwrpEl2HkLGavX_ShikLWT1s3C5yrDtLkrkw7ne2MsHG6UDKuC03JtqkpJlXdeVWMaFm7d-ne_niupHxdXGpE5LM1W-9gxdjBxjJw9LLpwDYEfZCmfyg2tteZsZzUkxsGCTGmW7g5n4qfnXDAIZKAv37tFPSfRabzRZYRkoKgGh4dW7t3cOjwzvEWdBkVGyz4rBjxOjgbJiqh3FoRga6OYDGouQ9_lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=tt8zFoqVC7C53zsCZVm6bnnxTa_rVtmuLJyHY0Z-ANOpzCKgbjZf_FTISo7IgkxQgC6T28MZgBcEAGZykrOqQv-dlWn58XEwy1B8cMM7TDe3NRU6c3ya9WODwrpEl2HkLGavX_ShikLWT1s3C5yrDtLkrkw7ne2MsHG6UDKuC03JtqkpJlXdeVWMaFm7d-ne_niupHxdXGpE5LM1W-9gxdjBxjJw9LLpwDYEfZCmfyg2tteZsZzUkxsGCTGmW7g5n4qfnXDAIZKAv37tFPSfRabzRZYRkoKgGh4dW7t3cOjwzvEWdBkVGyz4rBjxOjgbJiqh3FoRga6OYDGouQ9_lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28855" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28854">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNc6l_M2VRHrIxtGTLUkKOdV4i3ahlPIxxLl4HbacizwLrEKo3dlGcjV2U3P_bF2K14VSV4GV6qNyjvapn31CYP79oEpW8QJkZpbSmeVBFWWe0TAMY_3pGnP6VRZsVMjnbVu7Qh1QU3_vsadzotBXdgpKC4CxDbYrpKP66h9rWt4qa7dqUlQNLg1t2ZBuPIWrkeQd6cJ_NaKYwEx0sFbk4GPn3oSRAdf9k0opVxkkQmxf-FZwg6bUPuc2O47fbOykClDHHswpVGH52l-Q6n4H61gNsNAzkkLkuCqqG5NqM4s93Xe23G6Rp4rcc2DAu60z7lX2Bf19EjySceMCtxrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28854" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28853">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔵
🔴
درفاصله کمتر از 48 ساعت تا دیدار فرداشب استقلال
🆚
پرسپولیس؛نگاهی بیندازیم به زود هنگام ترین گل های تاریخ این تقابل بزرگ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28853" target="_blank">📅 14:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28851">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWKA4jg0wJdhirnhdYD-u5cw51bFo4s92KBtM_H8IyE21Hoz5MdbRVLKOnlzfpoW6UVbrXXvLWaG3gMjHFw0tmzah5VySEZi9UnLcxLzs7ukK_zxLszaf08IfzAP_D3MrxhsualHpjHBAg-VYmDlSIeypTcwkHBLXTLJj5Du_ellXLQ0hWCB2uzrzmLT0zh1SoeltH_WLWhegzlzwjvxi1WjojxPlDbNV6WZfBYk5sYxOX3jWrgXz_Y48Aa3QZiCIadyyul34KqCzKbaJ5a9fN_UnJm2fKisTeoa9pALIk92L74c7L3PobGfuqiF4GqgTNLkQPwJYNm9fQ1qQV0H-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krqcs1VDTSQYyonQXM_giURaQFyNFChgPFliyak0vGN-prbnyvf9mcm1ydi2wdLwTO_MFY-UiwpQXcaWedWUNH8VIdzSf2QpWOfzGtcVnSK37vMkVgZsShIVUDEZTVZMcM6qfLyXrSkYtpFws3kFYJArRMzgTme7bL-v3LXMuh8fsOKbuiUk1gwWac31ylJ8gTmzy8nAFCm-zIf8Ew5XOFyZ2MR8cfqxvpSU3TppUOlDIqzUPkcwKw-r8ErQTd7qEfqcUTyV2tvtdsrgmUGxLuXDpg7Wf41PrYcxIdVcm4EHxu1bI0zh67lZ4QG_gaTeTH_g8wBgZKfbf0Ne6dd9XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28851" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28849">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFqyLG0ioBb_cFh-epaTWKITYJ2S9FWsyoxJTKU4Ox8iGgOG5fmaFyqXKrGId6p-L9-SF3CtmgZ7GRqrCFqq4MjxAb9Trmd5bk7npGUPXIajF5DAlhmI3OXYu2JFQK7byTTl-hk-vibGvN-Qh8Wjyp5dA_ka9Q7F6FYAtc6ATigwsZ7_PZAMR8IsmWMRtD-g3CPM9I1w3g7dQDMPSDhAlWAa0L1dT4XEMpM3ZobCD2mN5yPH3GgtjipuJiC9yTIJiNhoL4pwW-DbfTjiICAj9fLeLKHNvb_yq3DB4geAIEmu5i7LQwTErPzETPPhjrANSap9rNeyUJjFUJtLJtErZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JlXkPvAtSr5PnijSzUDcvVIJQrfVgrNOCpBAFMorZS16Lbge8ZyZHKemP61TfW-Ymh3SocmZRfEy4FY3NxeakalxhC70C5o4VbT_AGmJXfA8haFx6punJoSh3TXO9dK4fmBHr8HWLcmf9ktzMiqcMdk7lR7I-1A0I1mCTY4wUv740a9kZyeWMlBbBrcMBnDGlML4hVWYsEXWIYEeJ8Y4P60OSFTpwJdZQoVKXmHUuoDUqYarCUfeZxRXK8iAYBScHzllxnOfKvsFeMgQVyyBVvxxufvE7K_N4mrkAZuV6x0ZcNGPZaZ3LEIh1Vu6mGV-c8K1Q_wO04mqPYsUq0LX7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
پوستر فدراسیون فوتبال آفریقای جنوبی برای پیتسو موسیمانه سرمربی‌جدید تیم‌ملی این کشور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28849" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28848">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG7Tb2bOJPPs9Dtb4S9j8ZSSWHT4suTd3jlpDewTDZWG231rx2AVhlrgXlDsg-_BaQ_1-P55vthNabuDctPbC9wlPqBJdAawWJtA2EEwne5uLLPYUbgxqwSrd4bCV-b7EbVH2Lwwc8htqrcAYpUBHGb4BGDz8yjEbcMT0_4ogrC5hX80gr-gnBlbYCtsCBj09wOWTd4xy-MXu5LlpUThxX320OqjOohYb8yquDnymUYzJv1bfVtswhGvF_VdUESLD6cm24hpQYHV_WoBPRTVeVU5ZiKPGZx32BKs2Ub7Q72caVjxD6qRFCUA5lGAFqv0QzPJZM-G5Vb-Zb-BV0_qzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
فابریزیو رومانو: انتظار میره تا فرداشب که پنجره نقل‌وانتقالات‌تابستونی بسته میشه انتقال انزو فرناندز ستاره چلسی به منچستر سیتی نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28848" target="_blank">📅 13:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28847">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuDHA1I-GSrquUJ30_KNmUo7penv_eusG0RkotMCU9pE_kI01eLPcivy5ttNDbbTtF0ozy_u9q6oZ6Tg3K_B8IlPFEzIntkF6XWXlod2Wt8ogtdq1ZWQ9jBqHQZG1BDGHFnojJ_51eokPlfZQFugscfiYjMV-pDVnrpee1fWo7kW-IWHJZm2mwrg35gb9CidAte_eMyZ0Lcwk7hBrNJ6wM8J-6cIeO8IAnaoNCkIzE_WqnUuJqmEVu4ESWLhCBjGBKxC2sS54cIuOGX7UVksDz8huWeQACpneN71-rlCDbMwZ1hhKi0vXMLgubQm7p9DDTQIYIqHJDhsn4o1_C1euw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مورد جذاب گابریل آرتتا پسر میکل آرتتا اینه که چشماش دو رنگیه؛یکی‌ تیره‌‌تر شبیه‌ پدر، یکی روشن و شیشه‌ای شبیه مادر که توجهات بسیار زیادی رو به خود جلب‌کرده. جالبه‌بدونید در دنیا تنها چهارصد نفر چشاشون‌دو رنگیه‌که پسر آرتتا یکی‌ازاین 400 نفره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28847" target="_blank">📅 12:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28846">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APix-iSALlpuuliMZRws_ngEwKYlK4b_vAqFLUKqBBO3Bc3V6yNQeVUNpEj2g7k9BUl2iTHJoCuGIBOx7fMmukd0g8X_sRb_xyWN1_8lM5GMQmBldO-Q54X1MqtLuJF0M-FMoETD97oWW0aushT61zFCxmTroJGtiTxuHCNlRoxNsIm9XOpSlQlUuYD8JBnXHVLEQM277e5i0t2uinbfpPBzwjm00lAkOTjZ848Rc6kbxye68RVMO9vVHKIfxJXee9RWlIKws32n-lT4UuZvEavLS57uxx3XEyXmjK7HeJqJOXNoHps-Ec4Swkkgl-rOqg7sq4LnuEMhG7v0q6iR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
نشریه‌مارکا:خوزه‌مورینیو ازوضعیت ادواردو کاماوینگا هافبک‌فرانسوی رئال‌مادرید راضی نیست و به فلورنتینو پرز گفته او رو بفروشد. پرز برای فروش‌ کاماوینگا رقمی‌بین 60 الی 80 میلیون‌یورو میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28846" target="_blank">📅 12:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28845">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">▶️
ویدیوکامل ویژه برنامه شب گذشته عادل درباره اتفاقات اخیر چهار هفته ابتدایی لیگ برترو افشاگری‌ های عادل علیه فدراسیون فوتبالِ مهدی تاج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28845" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28844">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ3HsC-VPYehq94DB7YgXuA4bRokfhd0WzlLIwFrMcgfhOT3BNs6De-mLwhrsZIvGbhMUJhm3z-SmcbOdwSRkZouvMxETJSHdvRyzSrRjkNz1H013udD6Sk6XdXVz5pTjLXWQ5fu25oOicMCCBh3bRAm8KMy5Jys_2CaE461Uot52ldlmWeIUq9ehKPpTA8Jw6Lojm62sHtbSbUKf_QwI5e9hT1JVBbrugKPOzuEhXTLWjjzHZk4qjiGuPr1VSiDQdYNTEbSPYNx0wwy0FnCvOpIQEvWEYcQ03biR04HZ1BZu69FmLe5iV0ayJnq7H0-v-pf0W6TMNu-IqwX5-Wxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
دستیارسابق‌انریکه سرمربی تیم کره جنوبی شد
؛ روبرتو مورنو سرمربی۴۹ساله‌اسپانیایی‌ودستیار سابق لوئیس انریکه، به عنوان سرمربی تیم ملی فوتبال کره جنوبی منصوب شد تاجایگزین هونگ میونگ بو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28844" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28843">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABbRdsXqG8qzAnC4BekDiae1ROFWRdSiwRi1swe5iQlw5ol6VULLO271NFfAHmwguJQK_rQOHlId4M3hGOEJXI-18YI6rItKMqaVSqR6ICdfpYoJ17Oug4jiocSD6VjNyXFyKYAE6e8cCueXn5XkcwRoioBbBYNlSq-wvSc7oZgN3jv6OGJmqyf9CTRcafW30Jmeku5_tFcePk4uFVd8JzqzDpNixoptLpfjtRXmY2wNzSJDjCt71bok_8jtjSLGSiEW_6f16PAb_pXE3WdKFo89m22t_NMDaJpHZNoZldH4cQDSJrn3UfuGioXNy8UOLBaYqmuWA6uEhuYvfvI7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌کمیته‌انضباطی فدراسیون فوتبال: بعد از برسی‌های کامل مشخص‌شدکه قرارداد یاسر آسانی با استقلال قانونی‌است و او مشکلی‌برای‌همراهی آبی‌ها نخواهد داشت. بدین ترتیب پرونده شکایت باشگاه‌ها ازاین بازیکن بسته شد؛ خبر ریپلای شده هم بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28843" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
