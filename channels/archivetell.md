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
<img src="https://cdn4.telesco.pe/file/MB_gRT3YEcNfINadnfmOTlxDwhOil5duu0zJf4TTpBAwOmdmzNIi-ro5euCx5oLwDKo1u124OVTV0kTemeiRI8XF8YOrao6W78TthycPJOLLSys0g5gItM_eVjefeglEXuE1RItlZ2P4eo0gQFf40cOYnG0BS7tYbUTFxulsZ3M1uomTcIWg7haq0ANxcWHb3S3VxE84dBp1-KRV_B6L4bWDru2qFuDwVzTdqrTc6Hm1-vUzIjyS45m2RI5HXl_0uJ4xWYrkLqyv6PHloMWG1Gp2ht1a0pfZAvRVUXRUpW2hh-0NTCAV5ItQuNoH5li6Z4xt_AEy-k3dYuh9WN8ciA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 12:14:42</div>
<hr>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtL5bvKN5w2BlfV--VFl3QndWJJ66hfzdyoLXiXpjSMzn-LOdJol6-V5RsyZV-i0XSNmfiLdn2R5wCt_4TTwmzQw10HyHpXkN8-6zKWdKHOF9ZKpuHlQUFSAWjm2c1LhUHyAPx02oIyWVSA8VvzNIx939bav8FCcO4czr_uFM8vJAI_a2-3UX0DeOir1Cxdf446OyQp85vQi59LN3p8rWAe7grN9lUi4CHfo2-rc1SZtEnRPNGBcmV7pHRCV5KhqBlmwEqtINy1G1_-ftT5a4GSW6wmlPCp8hIH1NHTgFy52DUOKiuhNVHQCZChdG5IFYUrQhHZmFqMBKsJAohFhBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 534 · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIb2j-xkRK61dy-eBl9BYIgGrj6R-CilMuTBPNDJQEQv-4y3QSChFuRjCHxeWyOTdNeiK0Q_5GQ3i8Iaop5IcY6mk-13qWBLETCNcPfg1DnJTRRdw9-9zWFDuUb8qm-mAabLtD50DGvhonmJZ1egT8HDm04T0__DxB_L__LfatDQaKcgHgzVIOh_jW9_6sn5mqwq3xIge5jYGcrNnyi7qQ6hsEuvUeAj9IMi5uIXm3WPH6pyI3q2OXXqwIL2mHso4vpSaOkZvL8NDQ-hZtsGtROtVJPy1Wcbtl6-BHC-sbv5KddNv5oRUTN2tl9_xWu32lFEbmRFuKy6x6LAnQqptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMeBN5DKQvx28Ge949AF8AMRDUBSifChGdSfw5UhI3veLCz5bsdv_huaHmHhvNMNVqwtNqbeisZbWIvTzjPw9TS_xowy0DYtr_EGZ1I3LQXQs6X4ZFc1ZTvf1FKq3qD0U3qiX-qU4Vralk0ob0wNk_O_49GXRU6pyzk6V9OjxA1BZZE47__1PLrS-W8KY8CI1SDm6Pvs0OwfFhElKUD9-pXg8PFFxwAs5qPXN6AhISSNR2eLQTTQigQ0D7DC8PkOxIQjoo1XCsKK_YFEqAsCocmBLtrvK96VIVoGlcZM-2rCyUrLz3Ym9SeLsJuMR7i8vxCZwLr4h-m0SYvWYj8-kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y49uIQjllDva5cpQ1ZeQn3BGm-S3KKEpX1TpTiuP5Yp92XO8jlB8Pj4M0iqvdlGYdIqIGXAos8v1n06RBBX8WGlEwurs2x2SAAp5O39Ka57gW8sNapW_4XO2YD9A3efv6VzBXOxa24UljPu-TWQbPaOmchZYqMI9CvJOH0xwd8Gw9aVOJek2OeMrRHYhBdNpREBvCdW_N0tHqLpveeD_8At_B6WfdSZwcHT2WIcN1LWDWaRauy4vgjDvrkUJLg7wqe8igLYcT3RZ6IFVkkqG78zLJpFeEPprjLDFEPZYVCjdgZsmdM_vkQMe5gctMRvF1KTg8idREc4GZOFpY2RIPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6mPQZacLhdR8mRTCiQsiQpC5qrzTmQcpzSWeFGmwDl2K8MrroCTvXXnQTKgPJYXXDHjwvq8X9nG0N_tzFg4PLtV8_oNH2KX5k7ILNPgl4Wn3E8PkSjCSuQijMI2agO1wUOTaScd0W1tLEhb6GdjJUwBVRWOvzXIEPeRLGVf8p1mcOTu_cQrkks4D3UwJ-HTfz1FkY1Zu7hoFpRjPVwajJT55Lcp-73LOwt8P1Bo8UmqTOgxu8rfsCJ0gAmBwuOGbJIn-ic-yKFFWLXgUwyhIRlmV1vmyMlf0RwR4W_zoxdIjITOBFGap3Cc26ITBS9bZg5waZpZ8nbNTzqldiiePw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKgs3fwLHnKcVoT7wszhdqQhJnsMHeGyCabVtDVnRE-h_wcG_Sl6LPlg2uquu23a7-GxeHqQnmBj-FJs6h1hUQmgwq1vHEdoPGqGA7Zp-h2ftCvS5d9ZF8zNBYW_0U1P9zt2vjECPIeAOyFD0w-tevQ9DDWNgCDld7QuHAHGENdxnsSdMNOiPg0aZ-WnfGfQJhxG_fqzU3o4TuV57OoeLepvQxODl9m3KwMaUx4dy-cNp7qE7DqrK64zwePtEvBwzj2zKsnZmTJN3oTUfedzIpX17Cka7KN9KJMRiC72rwB0yreNngZrQ0xhXK64DfFzNuE8YTEAGJeYphyNY6VYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7o_I_NToE66jFLsZdaUKkEL2_I5cARe6WGWab3X6J9ssLH7d1Wax8tvjJzjFtQYdgOzafr2P96_idSYZbe80iawaBl5RmvHsTWaq4JVMbyylBAPn7nDNHDQOjsCQ_-MqDrkmPWVdsZNuN2xxLigQsQzzj3LEuEV1sSpO2Fc6lFeDnzbGmQsxQSlMhmz1sq8KWGSjU8y8w7RtUYkfDo01f-5PsZrGfiOhLTIrw5_uNQESR3U1yiCUoWFGvE-5nPYT-S1TxsSO1j2NXShHxTWBsnpDehgm3km4P4iLfWfj_ywfBi0O_YpvmfLrzKMr6WhpyOiULPIgkZ5zV6QcH5x8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYhJDZzm4dIkOAYQXhW8fSKKOdC-YIT86JDE_WtbGju8GOa2z-mA-Le1Sf4xxXGVWRTo0pISicZFb3ux9bjSvtP9lp_fnzA7dHK9Y6ovY3C7esgaSJDRov-Zh3NchE1Io6T9UkcC3rLbXm4CMFfPaeqTD4qqKGT3kAZO7pyiWcmRup7G469BrjpsPiXRsYUOd6GL6njFRzDo9BJAnI7BZaFtyn-LyfifRYC7W4N5XRCVZ375ROnElBQY0p2631i7SVqNXfBtZ2scU7g2_g12SivVtX_O0jSLqYUzMAHUUjEC8XViJYhKr5Gpfx_4tNP0dwPwaFnIW3Vgj_MBRdDRRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwCgJBV0Oy8w0cfZBE-ltxJI5UekttWhcumAIb4QHEZ6pxGGZUgmYmIoDToSkUICBi2Brt10lxaWSfRUSNkid2EHHAT1SSVzzZB1rgUdNl_b2sWsVs9AXttCDogJU6L2guD8ReKH4IBlhG0KKXeXSUYuZ3qnING8Ab8aBrrxvcvKa873ObUidrFT-eU84MqV0cyuMJkf_TOoxxT2Y2P4Z9pLkPAPxPRwWc67BAlIkxGSvwVLMRZentLPh74x_IW6r0ie8kJS3Y4Dmhqtx20k7-OXUgslowX3vq7QvMjmAM-XIFhpCa2asoZt9D_YFET5PkTg9xJJiO_Ah43Y260QGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQojFrGNmPpdaSRF_bV9gZ2e7MZHIz_9IcW8VUVcOzSuhKGMNmVXSa0-VDYeA0wtoGhfXLXZa4azfBZZ65wCkqvBurCAZzcWQMf3hlrSg2NOXRpXYgsqb6OqRhB9oqCPOy1k3QXh-hed98B5kUx5uXL0F8j5LOHmJU5xreJ0JBnRR0JY6RyJrFVf_VC7IHF8Ih_CJ10UwYU-nGnRNV29ECFNBNkoW-jxNzgNX8-Hr1fhLGAHmUxWJvJkSsU8JNTmkCzndQoY_S6PSRJqScWd9w1lYcXCnRJiccVCU6xpjXendz2bXg-ZU905wcGAdVwp32Dz3ZuQQnOBH-Vlkqsw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXjcdHG-rzEZFJRSUgp7nBxXZtHheq7ZoCN9GZ-ICQosUcqIXhum98QUGavHp6nTO9sVE_o4SzE6FZhx5zloFIcN2KEhRHGTDru4WAyy7mP2OVOXOfGzQY4xdAmkYeNg08ipmJkYqJxc0z04kEmKZOMMEh3KLP_u7qBP_s5kNAAtdA_z5tNArgRBM2DupBSn5BCKVk34wvDJWjCUfebAjXbYjY5ry-jKokZGrOKMfcOeLLgn259XmTTlN3Hu2V1HwXYfTvxyQIxgQxuT585LUyH-xzAKDFF08pi6w3saeEkKC-WQa-qfSurPWiwqNzklzhK_CDdd26GvNjcOHDAxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhxgQs9HOsCGh3SYgkUgyl9S-o_2WhHG7G9uDetdCn7sPwRdOONKrjzMe4sf9DcdAuWLU97qILYpiwkZ-eL2mDyc61ur6oQqS6lporEeqvKj6pUHam6AGFqWpJ6qoExoyELDlzssThMS5ZeBSxq5ulNmiHAdJuDTcPqOQMtsOV0ORmP4nFxKCbHhBtYbfx7mEfzuJMHlrxjgiOxEwsNuErQUK5VLChpiiLeGbnXAEBjLr6E_BHQHh2LwwfzQDuXiKqxrXZGvFhvrYKxJps79LN3j0q3FFxLCAc-vcgSsvO74VyAmIWrL6Du1VTNFleXYiLNn0vDvgv8oId3vvZEunw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrCq52IQg4_2KJFkoT35Bqh7t4i_aFlNBPIv0S-lglyBWr8cQ8DENdrZVdj4_Pa-jIanGECXWCS5Dcmaqf2xdnMV8WPFLfufq5fvHu4wr13yXOqQN02T7xkKJR8mCvoGVoV3QGAVnN95eo1ZGYfddK6WaXN1nVE_tGYQho938eub3QsSqNLKZmWKSY490adltBdamnlP-Ntm2r23EA5JKXZhnaGiIxDhUbdTRUH3nEywLNNTi_BxBLSFlNQXeuUmPSEQUjE8jdlZBAIKy9gy4S61k1fIP7E_v0J1ZlYU6Dp9J_4tM5hLo7HeA_079cAtjkI30Epwd-Wb6vJeXoOyHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-3Rp9qr1ggwRtSwoXlDLD6PFd4TXXICxaDSvsgQTmXZeEBymxlvldOp6wARspx0Lla0r69ZfmJ86qyLp5Vq-3EGgFpV35Kyl2JW3WiQiXAh7D-3n3XgWzKOqvhXDv7bZZcxYR9N5qTPHxMKiami9soVcNgImNxAkjYVkdLNJ2YQVrfJMIgeZbr7Njr7V5sJI2f1P6kCqQ3R60rwCeRbHKay6pwjxXyyZYG0DMJnlkG29VdrzlPwCRdVH2GEZ44AQ9ZWD5kD0QF6BYv1sopP0QOEVFWdnRm-TXGo0Bp7iebuvk7S3ltNcxzuDrt0_q-wG5vS8ToSMAc9BOnEBRRytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqwfld8DddmdBk9o7aXdJeDUDRLFXs7T8bgLYSCz1oSItlxWcvZicccj4s4cXbJQviz2XKa6epHjM59u14mqG4Fyc7VD4EXonSeywkw51z5kn9CugNEIA46Te4ln3vIzmgIkemJVVIBOihjM6rXsUxxOcObMCqeuXEUGHr_3wbWibjfHfremH7DgTJdZrWrvngv7XQhjkvq1tsZoUVAwVpNkdxkFuAOAI_lkCu28adsEsqWDZipKTBs5o1ha2-K2Ayi0uOuN8EZy4ESsjZyMbuE-UiLBgqsH0sQbuVpYc8tgV9D5YdUYMcm9dvN7dPp7byKVUjBES_G9IuBdst2aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yxwjy4Cce0L214uSqtcDLa0nZ1KFUQYHNxh7_4GweVAanE-9a3zvoNS2ZaHcaJbSwUrJBtaMYmhFy5zcyCK6fPBFnsg-Ka_ShFLk_6gZFH4O_uLkyMuBzAf4j3M65ugiZgTvxo-4EGjVwjmN-564GARR5m-rKHhX06JJx-bgzmcTv6TjGOO6XHbBLNRTO8k7VVng4vmCeCWF5ilhmbMsG3rago0vS68bRRm8GAzBWPYFIlCB5Qkaj6vn08dWiyKgw-ashHXcIJw88seQVgoYjgdRLdeedlDW6RhRMMf3GZAkc4Tq_yh36qn00TGmgeGcpq2jNEKRb7Ekdyo4X-lJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUJPlP3P42-3r8kFfI0x1goB4yYXlNxFWvRjYgpxkOmBwlGIQUXXnxB0lC-pT_QXK9kK1ax0NhCY_41Tt8RgJRqGUzOvSegp2EM7QLCpPW5MftofCu3Yt3xrsV9qTnOHtJ0kCsIu7DtGxD1JFwOtmlk5f4d7N4_Dw0UVjF39CX5fZszeYiy4oUO6Z-Ydiflm5l_0s1_x8WjPAjNm6IlkKKbPQg3EeH4pU4GiMjcVlcfcsyiXjSPJnh0O9xuFX8CwqhTkpH9RCnXaiUw15Hr3oPdXdleAEvjgOlzXFaGfLZgHeb-1ZpfMDCTIPwjEftrbgaOkTDIUdUrsud5W-wG9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYzZt9OQSiwK2vkZOKnu4lvjtmY53-T4beIOcGMkKBbAXDItEnUSZKNLNsMyirFBtMYXzKf6Lp8rIkmyOezf96EuQFBAyiY7_j4T2i43ZiuyxL3RkNqjPyIzWw-hrgCrHTDC8cTkqCUKcf8Gs_c6QYkN2gN0-OXdO9Waf9Nn0zm5Rm_WJIBz_Z5pPp93f5byScanFicsPs3AQJtssuoslilMIf_T3xEWHTw2QhvFMEBYJZK_K6PEGgOClHKe_H0R8mc5E4BX_dr7vcclprE7EJouiY-99EAIBJo-hV1nZccDD93-rv3h-xEBCBXpQ5ivWRtogfBMG3pFSK1QRAKvgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nz4CPLR7csrsv32WBH4HZfVbKl3IOhypqfOaoM1_pgsSYJRLYGwnnz_w_z7iV0KoOHUKW_zmUVTlopkbZfBsaE8RFgzndWuilR_ZHxTl5SiBSTSluIH7wC-tQwT8O4kVlJgoHLiKAMnhn7ZZ0CXUV_h9oDhbuXhhnvHrG7QS5MRrSql6f5f5x3kHTIDLltsh8cXcl7Y64wC2BdhNLmEBPeX2g1mgqzQw6-o8y0k3SKkqVj0cQyPlidVHu05LLbXwPZHXnnluPiUebviD2Kx39eWmvXOt9A2uN1aobMhnAKJYBTTHyE7XPfNN3JJp7lnq5SikqBFLwKz718jN8np87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx1ErF25JyFs8ubc20d7NyWnMui_Tw3EoSaFS8ikS1I7gcEaJOrgRN5638X7ZVHSvuEwu68D0jJWEEKng81PmyU-zA4PWpVTbG1WLyzkdOZmXzk5cUQS7OEPSK4PfLgP8GqX7mQWaO-HfLN1mgPwMVj21JDL8qztU849Byh8cTte_nNN1fmhx4XDNWhKPsG-4K-p1xU_lRc22rxS3AMjTelJI3QZhoBIKE_faoijfPVdDbXXbOwRuXokf-b7U_A7sS5TkD-nDkbP6GJw1T5DH17lCL0LCJDHR04rzZHMCY0fk3tjOp6KB1SMwkAbUTo2gaYODA0z726I4Fdwz5d9Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHkp01xFqF7qrdHop0egf3SQFdtxcfWfdpWMV68JqeMouiOm8k1UVWHW01LEP44mWc2F-UIfSG-y-AOTmsnbUI9ExlSOInLmL0hwxTIV3t1qDFAnVKZ78JVNVhner8S00NTeVc1HQiqJm_7pODT8lsi6QYX-RIeNWFXQr1eiWVFtbpJnr_1aeErBzATrM7Ygz_Qju-6kxlMnDPLfCBAoR5QPEcWLugXMVa3hRmUARMs7qlpWmwEvgYVQeC3BZ_5Oam1wswmGC0RVWleiuIFa4VylaiqT-j2YPKo7o3hcBTZYzZ4vF4UsZMTH8__QHSDKuj2LfPwzWI9ChQuyzINAew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNaOb2CBgvOnvTemsMhTwIAL_bVJf7B3TiQHjRishVnSTndoUsByphYjUy97O9L0_eADn_MhdiRRaSStt8FPH4fan9G4fcW81LMJ4jpB5KbOuNtrju8ufnJzcjNDaaG4vP1s2Fu9PCQnv7qlcs7MTp6PjiiaNkaaHUmq2PmFi-sQ63keBhAZVo49d5evWj7uyzGsHK9kNMVJgOEdYiu__L5lioilbCyw8uygU_sjicp90fM1F8aWUgwENCRaK8m7uFrjzc7sI65RkqF8yRMwjsYmyqXsbstpEvl6JO5mMNqfkhLBuuNLHJzd4w1hGKWKElONFrrKKJZ_Z4GJC78-zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_s13e_y8wH4RYUjQyokPCmx6uWzXkyKTgkO3w3IoDnggQM2IrbNigCraNb4uGMDvzq2ZWd51m6hRG8p6ZowSbfom2o0LZ_GL5vreZkeM-xVmvocm_o6vcGwPvuAdDyRqa26a-pAozveMMSJJn3WAwnyzKjcuhmPMgG9Zvs40lmFe07lss7xzn_qSoIgE2jDaYEkH_JvFeUVc7aZ4B0gx9g9BFwdJyLCcEu1J8lT1DJCZ1W8G2T0h3XjTPM5-Z6LPVOyuCNGBnnl3DRKDr41Y3_W9EtWT8dPoA7IuPt32WBe8dyFTKRgNiNDkZjsE2vs1WNRs8h-m9XBp6QD65tjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acqBg3vkKyBEQsD5E1BvUcnSK_3jj_8JPLgEKy1TsllLn5ej7oq237MaOe_TKJVAkVnb6C5mq6Idg6kl2aQval0vbORNH5UuP2efFc1EyTSIztEIDWFQkoX-kT0_99No6eBOJNIhluzv32jmo45LEtOW3arbEHK7n7BzMdAXya_0iG8R4EdIn1OZdy5V6IjdFQtqAAHUbgSGSqbU8cKxxX-RW5JSvW3mDHzDwxVfpTPsunsKQMYMR-vQy_OjKsR1BEtU-AEutpIa6AW7rXniCpAPZXIjVvTwXasJQ0kw0ZqD0pFNlDpMDiP_uXBRNRMFVhOWiPHySsCXho97ncZRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEJuB340kyEbD2sm7dusaqXlHHyir7pH9x61Th54OetUmpbDzt5nA-5KzjFoG1JTASqTQlCzMPVvgWT5eTku-N4b9-6dShGisx0ZzUeKGyXQYn9QjPZPVvTut-aGOxdM5hV6nT496Sfwqfh82_uT7yHzYeQqyraT2ykj4NJbruspaMiayYpZD44Xkcd9BGrwh8SK3865Jle8HRRuOwjHUTYUMySg836uXdpj8SJiFwx3TbYNX6zyut6kAFNxzgmLlzhuPAXqkVAeTDb1SMr4CZ9oqPla_am7depWRMvScv7D7lgrMPXOmExnEnZYvMXJPPqdVdeI_eK1BpbX8rN23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqxRK9LkxFLL8RnHPQwJTSCq0CegR3U4vkjiuni69KU3_fMgcGEBDh7VD-LC2LxXPzSp07D_XWfwwE9ZyPTxepyi7Sx_dQ1jpEDeoI4Z2BRBu6rl_jIJWeruM0hwmNFupu_kxbVYRxiArhLh0LQSASgySsbzpIvlMKN1F9aw8FiE3ueAFSuhqsS2Xjcizckh__QCiMuVQEOHz18oFktaou6TUQ9GtzzcXtKjTI5N--HwGtrpE-KmLmNC-vPGOmblJdwSrWTkFrxi9L12bYuPOnfvz3NUbwpqkYdi2RyMZRpC78ik4BSLoMm7cpPp6lpCCQIrjnHWIISb62xYKWkDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbbUPC1czgkyKvVBpDHpfI6L4uR-9PI7SLm_O1OMEQVWcwW0i9p7KdtB6M2-PmO0HLZbCKtEdQstvfAP7i88KDq_efqj9ihxV0pBLC3vbbywA4y5W5PkNCelSpsikPaDkcGN9NSyDSF6B6J6mtMKAVSSRHDUngWwtadLTyz_cpItysgMUk_ybmno_qGTGAiZJ-dHCWsroqBiaiUjK5U_COwv7AP3-mjYQkxZCTAzdhj5s-oVIh6qQVhZ8XHk_LBKMSD0mOWLZZGydm_CB5Ep8tmyk00vJn_mnO2lEt43e7GZ_jKdd0wrvUhu6k9oYWf1p3UzzFeWspRqc6ubpXxTpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X83h_cTdY_v37JTjiCPMMFPyoR06kcZ_fXgYKTOMzw3Fmd9XjSdyPVmIY_V4uM4Omr3DsEcdHjAh5qB9RMnPo2J3qP4EgQ3JDUDtp9Y0iZnEpuQpRHA0sLMY4L9-zQV-t__FRre3OT7jFYq1gGxGQ5vtqq2iRWNU1qGxxShNLeOeli0VhXldvOY7QpUAc8M9BGLJJpqCU0VAuAS0ceByUJJe0-9_qsQ8n9dK0-nwfmmM8NUZ0yWq4MOsP7eEdYMVOQotfSSv5e0C1gM8alVdGPQqXxPbcOHCMucV3fX6NlqALLF_7t8giHGLewPqc-sCZficq1DkCcokE7WlqgHFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_IiD5Aoea9hKmE0sjNW453UNwr7Iu52FdgrL3-10pMMp7U9G4LLRUL4KrLvxLnI1iAXEpm2kyFN4Gtj6k90NxjdfHTyEPb9kM1h2cyq0EK-H211Q-nxjsfhI2tiwO_Ih5cEA2mvetIHy8ma68hjmr0kAwhSZLw_mDKVtojpujzrzVPnksAH0Qg_m3VU5oNdQObnV04K180OSrVVSL6lKiM3rrNcnhp0FGsNgL8ohJJnpKolP3FZKqT1nAjfQsWnfKFSjWXpDEyECU9FpGBwp1AJW-SQ0iC1ZFi1iFV7FaSdaII9n_lfkjIt-ZuEVc7F_HCPo7mmuZ4gc1qo4Bh_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3U2qsSz1wPm_nJuPX5BC2azv1LWrIiOqeBnLdgamvQef6agr7nIPPENBP4mdg7sgWE90ln0xHXe8ucO-T6Wb_zsXZEmcMsEl-tVRRWnqhq6L6NusBMv9fY8kwz1k6T4PmpyRE6DRtdLpxsECLyvkIGWBrbPPmMfYTgQUEs3loFgJ2UGctFrcuxMvqZWBhZ_fZtCo4MnheaUDt7HDEkk97Rk9YcF0TWUXqMEh7dHfJ5YwFLtGDJAW3yJ4HqofAmULUO-94GPBSwtTc0Izu3KhqgopOvB-vrKyUQQYwVDlMwboYN8phDlcArodQuX40tQ3sVNGneh_8ALxXOpo-A9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwD3RDToFkX3H22-E7CGVcYpsSnndJ9KMNSJZDLPeGtyciYer7DTpm6dWSP70Pmvc1ut3J-sOkFEnnlWwAy7fX_Vr1Rm6AFnDTmitpvLgczX4nYOf7zcUlPGEZe-4Ozbuc9DPDzRwIOaEmP-7HtBurW7YpmNjByfvRVsRPC8fdo7-bxu-yofiWhMgB-kMgEvaRy1pMqp0QtGINsAY0gXADKXnuhhjbmmQU7VGHanyg3U_vDLMqTBT4W30PX2ZKUB82z1PGmm4gk5W9LX3dUhk7k4ljQLVe5jrCFWt93q_lCiGjXYfIACq09EceFVquOeDy5HIYHGg6f4hDgi0ax9Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cooBjTuZbLJ4E1_1mlI3bShPM-i77MTcD_eFe0R-yWGtlFoFcd4ypGlnM0_UDvlIBmeCuH28U8yH22bHFeknBZ6PaR9mC_8HY6CH5jrlFrs8YjwZjRY03mnVVbqcQUBWZjPvh5m2aqY6AG5ccm51VgrGZ9nQOdmCcO3gp5jRC1v2Qba7sQk9W7iAVZ3-W22GIsCIUYgw4ycguX3BzRwzcCYisfaASRXK3G0lra2CzSkFcmTJfsrFNWmyIanGLSUFBVJPiMcna0SZ9QpVekQpD3vdh44dY0AJ8nm5-PAY9TClK4DEgKnWh2tk4X3xXEIupuvDH-TTUhepPt3NiL04qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6zw648ze6PPylBsCUGnlGb39Q91NTVwYJWeUmP9ZZH1jyvGDK-98aWN1WJDzGucPqIFuneNmauw-sglr3T2g52zwAt9qIZmosLtblUu7tWh6bmXrqCXL9dykHGNr7xf_fwSdDRkRYMhx5Kt0kzklZFfD4s3haT0HLMNmG1Dl_my4S7CK_-ViGznXUrOsbBcc6MPKZIKE717onjRmADcq6i26E3Le3YTL0hwtpji1gzkU7anNZzYsshWM9To6_jvpwcbnphCqAWCl19E3f-3VoM----6GFrMc25BqkuwUjzNBCZrzBI9bPbSg-shc_tYGcXcx0aQ-cte5IMbSQUgpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=jz3s5uqKT38sAy_FfQl2JQyPatbtYH-6SpcYZmaAbMskHyWeSL6QcizxYDoVFL7V8vWSwL0IMn74Ewcx0UfNnBVIlij_ykbWqiffYScVyiYAc5PHzyfbwcpe6WWkclVwpBzuW8rtKra2qwHwm6rEe9eF93ZxqCy9xHva_ZDUKTwfX7gq43WRfJPaQzfcdBe67UD_M8iBdwUXCqjq8NxA3GqjLKhUgGd7FH4_lQ9HWnI4DEZht_-DJinpZXIqUtQm_eLNs7mJY0XI_ti6JJIxdDNdpMJvW_0fE08pFtLRcCkZhKMsIpdthfeLdtZJbsKAUnZfqUC2gZZEdehtKER2Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=jz3s5uqKT38sAy_FfQl2JQyPatbtYH-6SpcYZmaAbMskHyWeSL6QcizxYDoVFL7V8vWSwL0IMn74Ewcx0UfNnBVIlij_ykbWqiffYScVyiYAc5PHzyfbwcpe6WWkclVwpBzuW8rtKra2qwHwm6rEe9eF93ZxqCy9xHva_ZDUKTwfX7gq43WRfJPaQzfcdBe67UD_M8iBdwUXCqjq8NxA3GqjLKhUgGd7FH4_lQ9HWnI4DEZht_-DJinpZXIqUtQm_eLNs7mJY0XI_ti6JJIxdDNdpMJvW_0fE08pFtLRcCkZhKMsIpdthfeLdtZJbsKAUnZfqUC2gZZEdehtKER2Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdUxjnW8EK0AWJvz-KHgxT7qldpirYznPZZ-fgDPT-n8f-6Q_NIm4KP7TwQPNaQ7cWkxDakmkWBvR4GmZ7pp_m103XYmp_zMkI-hbnfll1ZPEABJKnpk5z02XoBFCWKstyD_8l3W2PfwX5gosACNb07kMqj_LY906qpAGkUC-0RKzjXI8njknWicyxKF6qYFPwOd5qHnho7aRV9YOv25A0nWBb_ZBrT1JslZ98crE8TP1ZZKKzX8NXbnX71H5dP-h1voDfEgfwmXaedPw4uaDxPDcbmLSf0AeVYah_J6jq_mthHU4LgUzNy032v_VlthklmSfDMuZWZYEG0TRpL4Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6fPRi4GFbZw4kkkFsZ7EQ6pgj5_uisBaHTZkPiw4GPaY-wD3BG5q_4MtdcxgS0l0hdZHjEyRjP_fBqltAG9G14FGqan3zyKGzHZIFzY43bIzU-MbIpYa11WoDc3ndt0qQISVr66yqquDvUdtKnkpik1ZkgOw3T-kOGgHxxrzywdQZjBedkPwMEGTqNvHvz6yjxXgHJ_Vjhf4SwSdNuG-gxVYOgC37slDVir6PW-WUABEIdmyU6NAYXXxkrUcWsLc0bIOWmdgCyZPJQqQoCpsv2RfiNUllkVnIsShBU5jRVK5Jp208BqHtVRpEkuSVzPe76wnzQoif-38WgiG4HARQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzmmDVljbzZe0Fx0G4USHepEfz9Hu6D53vs29fotgjDr9GeT7SiXV23_PlLQaSup813Da__nPCPSwIviDquikratW5FoIx5SGgrm1Q529eEY0ycNTR8lLGrBk9MtimL7OZCRpwa5XPlPW4cRwaOnu6VzdA3QhXaCpi6GSMIrmuGPOl1ITVXyMhS6apePxvX7w1X4tBVwvDb_6LeMIRKNUuV9dsv8GvXB9r2Huq0fV9zNZ2BTPvpnOhRM8cA7h7UOExduJJrQ7p_NKklmjOQF3g2Z10oT2xZ3HWqMPYHoHvttquqWhf4zB1EiqDoEQEyyzGurrUfgyzI6NquKqZe7lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvgJdmVESempQQ7gRJofmZjzf8lMr7BT-VdDDaCxARr4_ldonsSAcAZH9BeWxNBGAseM1b_C8lrbUgFOOVA7s-aZrcxp5M2PXKsihrhNveEjti6HMDofJS23g9W63O6VD728Ma0BUGYaataStyjZM8IjLrI8mBCyLyoeWxjZWUSVrxieZTzd3-MUyoJoRs1nCaUpC3YVnE1mvTwx6VHsMLlsDkuwf2jiV-skpBwSLe98jnUuUxiiMh-PCWX9M0IKaFUuYnGMqgcpr20AUWXft81SJwMFERXSBZurSaDpA77nTLeN9QjidhQuvE5ryC24yxmDj5m1B0FweLuSn4S4yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9WPamrW8rLmItfum2FsvphMy_wcZZYVu4uO3K95INu2ClfjtAj7rnN9XogiITpc1Qgh81Qx952_4m6cz0UsVJc_5t1CPMuRUbQ4l48Z_56U6F9xYY9xq5W9EAjL-cqJMY1fyzrSw-RDTwmCgTN3XBfKkJbx4wjjnMv1LIb4HpgPHX5hvGBHfUpUs0CrkAcZ8AD-nWdBEeV4qSlHFJiKCA25ESzjxPrGsHauEa2IbLO-jHCRf61rrvSqcELYFhYtw7iTXvXIc2Jt-Fe0nslCkvSQNsn5bIx0CilZfp3FR1IkoqR1mWkAChDyien_SiWBD7Bh0_sulxZEiyfxh4fSMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoDXAPZ7LMQBeabqvyhLGU0I-0COKpuPBY5_0Vu88uOJLl4dUSGA67pg6a-40sCMGbYLLXD5QAwMlEotZ5cmC-DkEs2can2YURTzQlhhLTEJuT-z2Ud1UTUm0mR4wX9tWjmGpEd3M6AkP84tZ7F2W1K9JvfJMHSGlTsTyO5Ex-KjTlo9rMJkx-AKh-YoeIQSoh1wz47OCjXrga35j23SlPtNH5DqGuToDqSVW-YMfb4RVkvRt3Paml6lxnzj2YR2ZW8QPbSA7xPTpVvzhLuEKwUuB6JIqRQq1jXnybKmck3ofdkEtc3HwsSKUJg8Dg6jU3JWmtNUpd-PiuDwDp0whg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5v2uwRVPJME3ptFoOc-2949IKiKr8gHQV_9F_Vu4JKKDo2FrEV78b6i18hcMHPDQRAjiun-lMnLq3VEmLc_2Lp5B_hG_oc0krVJ3BrPJW2dyc_FdyEHHmeqP6e8TKPQgvc6WLGrkohLUQWA5b6H3yakwYaizq0wV7CNXl59lVzhUZWbAGqFSjmq87g3OG9CgS8qbIgcBHqA2zqCJTFItuLrT6UKX3XgCr00nZWvf3QL7_mDh3Mfd1RrzZ_BddPrPUkzqVtFk2oHlRa_0fD86Yi0nHuISRZVMJ1knf66LlAnRntRacvtqu4-xu4oayEcaAZQWkzOH6DhJr8nP4lT8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t892PVZOZJqVKamlzMQVnKLrRUyYgwi5OA_YobD1NyrDwxQbLTa92XhWE--gcrZ1jRjdfIqD7QIlXWqsdsvpFf1xQNqVu5_4dTZ14-kLc39oOsY4_DtJGYR9VFpsnKWqniOneL5qhxwC2MaqrnByOsP6atnSe4CJYDwio0O7eL_scWudcoZ77ykD5qsB2snDldE8MaPtEcEcumYLBkMTi5a-MqUVsB-JWQQAyalxEyPYrHLhl6IPV7hDsNJwZc5EPW_ya4cEodcTv4SEIk5gWOF7rbN4qkZNeWiw3m0qXf3Bd-o6rSnlEszIb1Tk5kUJnKoZKj4CjfQmDCvkifvHzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCCHFRU7sCHognCnIZNFj3Xxz_3VjwN2v9naydTfB4QzCb4IoNRbyuBzwrhIrepP7ysylSY6yj5Ea4ZJUOf34g82Rop_K2Bi3vg_lQNJo2wO0-JU3Cn6Kxew9VsV228KQQy9je_hF4oCCJpLl7-SRY8iMRQXemno7-JNPMD4n-UcdlZrKLSfzhUBdRUekSse-qNshql4TMt_B21QUko0MT0OHQCz-fXsdWk2XlHABLoHkmvfWuruVS4uCdUiH3yb9g0tgUYVaRvH2WdLV8H_0q9wipapoMPdNHemWwADHgjECWfWKy2HobvuSdGJwGzb31h1pzHDSsVzZkmNeMXf_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4r5HbC9slwpNkolyPqbrovWM_nXWY8aPN9O8BusZRNPRK8we0EJkYxajJxK1KPmVfn8_4-t7I_NZsZekaIR8hvIyRu1opp7KyGQ1PqZYw74eqHzC4BHhNuDpp4eAe9TZsh1Kl_vMMUA-929BeJrJfDPaXb-eUl1EeIOTBmKEJMHVGjU6MM1Xq73sB4gHJn5mLr8tijMjJm1wAxVN7KYL0Y52746N64urMnKpIRMSzz8_R7TMUepVQyZ29d1pU4h7RnCII8DWN8akysCztOyuv-cRKdQmByZc2uUMeWHv2kcBTkPerksueOVfFUNFrxhh1V_pCu3dK0Mmwqa_Ja-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8sxQga6kwXOLz-vMd4I55VK4qqkuzVdanpp_d8MqDNgqo-Wrwv1y57xzlLICwyN9WaoX2M0UF9lwUDvqjaBNK89sJepmgx_GfuF8EqI2RW29lmW3CZsrW5OZn1PS_PqtKs77Ddv3LgzM34cVtGVKQFEiBpcco1yWpFSQm9OP1YzcEDArFHFgppVXLSmr5p79Zbme2ku1l2JQovdWfAaFFLw9BMEXe2wFfL4UnYEOa3LNWuLD9vqXvuTlyWRN1Fs7wbV1tcYtmTC42su--yrOnMEpIIKYLcDxXS0C2LRUFIDoDY_GS_mcCC--nQZxyPMp9RcFqP6x2Sn3xOHQbwoTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjQneKTQrQ6VOWu7GdkudBuveNr1ePbHZKJvHHphH1pfdZfjKG5b-2rD8DaPn1SmuQGYh5YFvI__-MDPq2ABQ_eqxh6s9Vms8bawaa6R-zbZMiR2mehFom72dnS5t5iOmIapiMNan_ea9DuqNNxMhmm2rZpC5V5OEyGwUj2R5SObVggYBvpMpUxEnKXhtGFiu2puVTuTAruRMvyP_Nz_MhJktpZcvesWWqMcJhq3PRoyM2g3w6U9oBCKO49BCJdsOAtLatEShc44HjP1noBCz0GoF_9XFtxm46ctX3yevjccYyexAOwe1gwMDp5TTZCu194-_VtrfZNjcpEpNyRwWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPchVEb14glAfDYn1XIG48xGkT-LPJLir49vIV1WXUikKgNr8EebGYvA-93DtVLLK5sff6GM_s-6RwF9Rqb4IBK-9sFjnQ2CRS_ImHjQbM2B8cuZ2txPn22rDNoKBuSWDP03qSWCbhgCRRnLYfx2HhYE9GDh-ktHIglkIniyKjynqTKkSoWPakfKTt7yrEvvAZ2jIRbGnq2dhihXIZDb0bx5rifwJHZIhZ3e_rlUsr7S07ASvRleGY8gWh86-S1lDIjKqD3Wielz567qJNdWWdOlIKhfZrmvXiJdb1_t6vOEH6JhTcvTGFoXF1ekb8qhDvkn6jaV7pM8qERRX-2Exg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkY6y-EWn0izPdO9vtMdZnVZuNBEmoXLCHtPEPZg_huLKW-T0yRBAkn4xwEimBDqKH4ENY1Y4LSTleaapAG7lwVz1qTofv-qLCXdp5-pFI4fSBx3-PXSR4Ap_hVl60qyXJjhf6XUVxiYbaUDmTNBqokZjq_ApHVGW_KCy-2fe0JSQzHXJLPrpKHnvP0cTE72pWvVj2MvPrt7ZlHrRgY10uodhpgkRex6yFOE-xHGWYEJN6HIyj0uLFpXHyPJaDCmpecgg_zCKM019Y7ZfCO3o33fK6JtiqXfPYNEjLERmqOjweyaTo20goe0i8iK8V4cD6aANkcx-Im3vv25po4M7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnwH0CvStOsdwpQVQQjTwpObKPscKRb3_t3hRNlH9mN0f9M11Nwx6jlJW5W7DuuwMQzyN93PzAHHoN3xDCb6YG2QRPP0B2gtBBCF8i_d4BnzVqylAzZWVYZ9lHoaLs6scUEHkTXS_YHIfYlSFIbfxs-z4G9s5dJkHu2XlEZfq0DO2zVFYcV1dIBezovsM-UJpD7lcpbb11BzfpLHOqRZ7Fo2CQCUSmgVcUvuDRjP5afXS1ZFnPJ47kizboExG0ohRMNbjJnP2uxiQddrbqQOJY-pD8jwykTpEoHVxLfLtva2WQaH59Hi2rS4yzARlwnXN8pRFb-bWv3fefbS-7K5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6eOACu0H3GlP7kvHYlx3-NtjFByQcR147F4aWoXrqRt8L2e_f9s4neX4uO9LgcL1KAvJvUvbA9ForA55XZ5H9DYDSryGDrBUtGPeHLDzziMGX_FokL-yJwWsBp_vQ_8qo-fNiguH_VO2Luss21nFTEyb_rd_DXS6ctfLbeP23kNGo1-_7iRSBEOxwe2e_UapJtjGepptD1Klo7DG4ii6jf1k3YY01O8_IGv4FPumKtbrm_C1tzUfFHjkG_fjayys6i4D5IWq42dXEqprQaa22Qf2rmcdbIvlUorUBtWZESIT907WoC0KQTyVPvx4NJ3ToGsh5gU9EGBGCd2pZ74Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHyQ-cQ-0Van_uv1XzSGGtDRpyWZuRr83nwmyUlN4fYh36NrpIlIdOgwm9x_7H6SiDc9h1byZCkika5op16MfjI7kYVThfcdTk-GcBz5xx0qOcCTaHtQglK9zFp1sPDPnKc61Ojs_v6S69cEqbHxmaKaES5WP4T8jEbBucMGdUQQgO5rGjFOjqL05Zafe6j4TKtIvWPbwZgfAbGGcUs5aXx8vsfJHT4UlLdmDaUWBxRwyzDjCAL0UPpAnUrIDs59MI-nV_FDVpB9CHXx8dAGsqqgAoYkIFadhtTNuhLmEgLgoOrGZbDDzmXL5k_J9pdg9xODQmwr2UG6FRgRdQ26PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6Nd6FfshmTaq4mkzEdUSXyqtHSrAZ6zcShAP9oBBAEae3-YAqIn40BLqtnyAHHjt8QAbaklyABopfgnlvWiJdm-C-dFDQWUoqZW3Mqi_xeu8tzXrAso5D1_dZZm_AzLZ3tX63UHPmQd9cmAJM8aKbhvSGxiBlOphDNCVzzaUG8aabjQ2kBuAIzqnhKtjKy9hSFV7SrgFNqDzM7wEMrvdQFj1sxiH1dICe0MGTuudcUYBS61P6ntfNJBsG2WHq99Gn3l232ZKOzQmUdkqu2C_tcctEtUuVVGIUFV8iSjOMyHXcoeEjXkRAVYXHtwb6rMl4TIqn5GSftyMBseCxy3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mByWC54AdbL0i87p01hV9Q3fVGzGLXmm9gsYZRtUAx0ZGsLiiAtsbvitgAXAIgedfQcVsFtTN6ut3QLhGhkMACRnXSc_NOrJkbO1rnls1rV9vUzWL8gdiqFTNoiHn6IDCEv90S0biQZz88OhyJ1ohRzD7Sg0iscluRgsIowBOrgCHIC8cG1Gi9oACxjX8RS512rn2zGN0jT3Bu63fM2iL05gQoFHJyOgobFjbNhvMJIkfgsz5y6iLag5VBrYBoUf6_v32y8gA8t5lPUcECm8nw_5pMAcCXSpeEJzidr95UdnmsNOYAVDusL1vw2-awX6-Cxn8yfZ-nIMyM7tC9DIug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuQP2aOPyUSLpH840ru23IWBvKjYzrFBaeKJif8gVcMWiwPiKFxls-YRD2akzLhmiavleCuPMRnJVaZtwqi1WLLhgru2xWkmRagBxY4NpOtseWXDTXJTplJSKoYnJlBaAGynZ9HgSTteATaFSPNfFq1IdOOTh8nl-EugWiZ_oYJyTarA0kYSda-tnxJwD_61wSAw50hRfTCm2JK_QcKlSdBEhNnvtAbNNxdjGH8sLyDAeuHt88yf8uhKHJNdHMfLWK8-63yDIpGbpEcTW5KJMCwqgkVMkt9wGkqrG1KLCmuf3EnznvH13f1m1HLS2QwZM3iAYIfyiLn8LwOdWjSlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMuls7rARwJQLXVJYCzU3mBEcKpBK6SZhyQuWzl78aGjAHv2jvgnnH7qNUJovuX5WgAzC6pCoiKbkAgoq9HquFx0wLw_w0GeXvvIaofx9BXVzG8YpuO3a9Xxqal46j3X4hENm_9SF1ohWKi6liiGbjwOPLXDzUD6MsHmY8shZUZRuP2egcwW2_j0zIzhUfXhjWH9uwuFWXSx7DhGlQLgBmUyL68jvkiOPmyiCsjpknUrt0bwiqJfft---VWLCS56uxb2kZ5h6BkL8yT7ZPSIGSBcrTyYJle6mG1GAFj421--olcRIImQOAuZS7y5Z6wzzhRlJp6e8yVcdWVWYHWzUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=LhrELCb8LfH6TxVQLFILhx9U7jOGS6YVGZmE3LdYEL84bxppzEEhy2d_Le9-qDkIloDV2HkodKn1lmfD4CGZDcgcSlru4vkV318bv1_LTmOx1H5PnrFk9Ujjp1dAL4ZnjJ19NqtyWw0dwuf0hXKRWEeC5NmUeTeIoGAaQS_K50tK73hNJYYbFZfaVNpR7bYZpc8uBpfxsk8XGuViCpJFSrL3NCrxIy57DAy2TcnkLKpLxRkF874Yo-wFH2QeTiuRbbBz8bW272dH3TjnVgBNhzwwxjvM45faZvW4ukdfaQ6wr98n52fqer77StxUGdiUn9vjmyUjxXtNRvCM7oO99Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=LhrELCb8LfH6TxVQLFILhx9U7jOGS6YVGZmE3LdYEL84bxppzEEhy2d_Le9-qDkIloDV2HkodKn1lmfD4CGZDcgcSlru4vkV318bv1_LTmOx1H5PnrFk9Ujjp1dAL4ZnjJ19NqtyWw0dwuf0hXKRWEeC5NmUeTeIoGAaQS_K50tK73hNJYYbFZfaVNpR7bYZpc8uBpfxsk8XGuViCpJFSrL3NCrxIy57DAy2TcnkLKpLxRkF874Yo-wFH2QeTiuRbbBz8bW272dH3TjnVgBNhzwwxjvM45faZvW4ukdfaQ6wr98n52fqer77StxUGdiUn9vjmyUjxXtNRvCM7oO99Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTZgXpwU55Dvt4bH-UDLTEtD_462_1ur-EW_K6oGXq5zsGkFYEOdkAO3O7NiLhrmBNtXfO-QXAyDfXO98CbU0Qgta8qT_PNGNnK8_nLx39T2UW7ERAy-HdXCCHvE8WDSuzbX8O7Uah0RGRbQGJTHJW_WEYa2wHwqoZd2m2H1NE_KDUu0YM8-ETybzCKjal7MhypFpggdYwtuTbr69ICjQS9uZD9fbbImmzmTAj64SuYqAHw2Gpawke8_nE7SCQs4xbcYlf8WEbAURvrIT1am-IVlRJwu1KLJOfLV6yVqP4ZPzXqf9-z7t5-YiETAt33YMbgjOGP9kuXwPNZTqblepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejpdxuL5IN3ekA04dCZE_Ex2bWG5d_FwNnO0uzCY-21BdEjoTKTNM4ThNZUKgCzbT5KlLhenRmTRpMtBJmvK_tCpVSqZUF4s-Q1GKLv--LExhFYhde8WvZDsb5QMFuxQvln4huQ9fzf5nvzwsYsmaWqlb0MZB63ooaL116DckzNp3O4X0_zmdrPH2TfXdEfWiXL-ZwGosJ9vDgP9gevM1ffIHovWZy0X_1aI2qTizerrywADuQ4Lv8JxsXu-gT1DTdW9WTtCoVJ0Sbak8mqoC9zGvEr9T5CsUgDUucyaM_-keGSkOHuxxndnIXrx5-myPX-UN-IUgKmLRxKyFLNOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نرم‌افزار TeleDrive برای تبدیل تلگرام به فضای ابری شخصی
فایل‌های شما را در یک کانال خصوصی ذخیره می‌کند و ویدیوهای ۲۰ گیگابایتی را یکپارچه نشان می‌دهد.
🔺
پخش مستقیم رسانه
: ویدیو و صدا را بدون نیاز به دانلود کامل پخش می‌کند
🔺
رمزنگاری انتخابی
: نام فایل‌ها، محتوا و پوشه‌ها را با استاندارد AES-256 قفل می‌کند
🔺
همگام‌سازی آفلاین
: فهرست فایل‌ها روی دستگاه می‌ماند تا جست‌وجو بدون اینترنت کار کند
🔺
نیاز به کلید API
: برای اجرا باید شناسه و هش شخصی تلگرامتان را بدهید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با حفظ متن مجوز و اعلان‌ها مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYu-Ost_Jg3f8j4_mJ1Neie47brYeydS7B23kZGrKOqp5TNgBP1m0viBXZ8f3dIjyuaJSVVcRmNmLiWM-3cG6VBzMT9JkqOm-2NZCnc20jm6g-4jEqgIbC7JP7TaQkww22TcE_6h9s0WFQ-TKURimyYNQVjIgxuLW60HrSwwfSz3SAApHt5wsmHLZYH6542D07LWVAfo6rfOnURnG8gwKpFsYw3lp49uaWySWi7OMEfsfQ0mo_USvpCyz8n32Uva8VT32mN5tjq5mT41Br4RsioGdD5pYw6DtmaQn98hfg_dtnXnbiPm1rE6tjOUSv7OQSu2DlF0o8SJPpfkJrQQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=gK1jFC4A2xxL9FvZ_tWkhMAFKvIXPGh3_hl0nZrXgG8UOVkfXFJTBfMWHQ7q5dV5T-vYDzQQDhDXPnWqpgdCrYCh5ANDVConFHiqIHNTkVBfJe4J5vcnJdOyvRu3xq1o78LR_gU8qDHIyitghWiyn0nnjS9M__ucnClZ98r3r2WALXo-wIz_JYtkEZ5ocN0I7Ot5wirp9tcV0G4nQuEReEJBGY8HR9wGSg0pyH211JholJLR58ozTBVsiFTvYbc9Bn4v8W1Lg35qLQj8KfYCHJKK2umkf0rppIC9fs6xH20tK_YWXnqZhGgG3k53KSxckm0g9raGvOmtMomB5_BcyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=gK1jFC4A2xxL9FvZ_tWkhMAFKvIXPGh3_hl0nZrXgG8UOVkfXFJTBfMWHQ7q5dV5T-vYDzQQDhDXPnWqpgdCrYCh5ANDVConFHiqIHNTkVBfJe4J5vcnJdOyvRu3xq1o78LR_gU8qDHIyitghWiyn0nnjS9M__ucnClZ98r3r2WALXo-wIz_JYtkEZ5ocN0I7Ot5wirp9tcV0G4nQuEReEJBGY8HR9wGSg0pyH211JholJLR58ozTBVsiFTvYbc9Bn4v8W1Lg35qLQj8KfYCHJKK2umkf0rppIC9fs6xH20tK_YWXnqZhGgG3k53KSxckm0g9raGvOmtMomB5_BcyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چند API رایگان LLM که شاید کمتر شنیده باشید
🆓
💥
اگر به دنبال API رایگان برای مدل‌های زبانی هستید، چند گزینه کمترشناخته‌شده وجود دارد که در حال حاضر دسترسی جالبی ارائه می‌دهند.
🚀
🔺
Atria
بعد از ثبت‌نام، 100 میلیون توکن رایگان در اختیار حساب قرار می‌گیرد. مدل Atria-Dawn-Preview با کانتکست 256K و حدود 50 درخواست در دقیقه در دسترس است.
🔺
Routeway
چند مدل رایگان بدون نیاز به شارژ حساب ارائه می‌شود. سهمیه فعلی شامل 5 درخواست در دقیقه و 200 درخواست در روز است.
🔺
Selora
یک پلن رایگان 14 روزه با مدل‌هایی مثل Claude، GPT و Kimi دارد. سقف استفاده 30 درخواست در دقیقه و حداکثر 5 دلار اعتبار در هر 4 ساعت است.
🔺
ShareLLM
120 درخواست در 5 ساعت و 600 درخواست در هفته ارائه می‌کند و مجموعه متنوعی از مدل‌های GPT، Gemini، Kimi، Qwen و... در دسترس است.
🔺
Vireonix
بدون ثبت‌نام و API Key قابل استفاده است. یک route به نام "auto" دارد و طبق محدودیت اعلام‌شده، تا 20 میلیون توکن ورودی در ساعت ارائه می‌کند.
🔺
OdiRouter
مجموعه‌ای از route های "free-*" برای مدل‌هایی مثل Claude، Gemini، Qwen و MiniMax دارد. البته پایداری مدل‌ها یکسان نیست و بعضی مسیرها ممکن است با خطا مواجه شوند.
📌
جمع‌بندی:
برای تست API، پروژه‌های شخصی و ساخت نمونه‌های اولیه، این سرویس‌ها می‌توانند گزینه‌های جالبی باشند. Atria از نظر حجم توکن، ShareLLM از نظر تنوع مدل‌ها و Vireonix از نظر عدم نیاز به ثبت‌نام، ویژگی‌های قابل‌توجهی دارند.
✅
⚠️
سهمیه، مدل‌ها و محدودیت سرویس‌های رایگان ممکن است تغییر کنند؛ بنابراین قبل از استفاده جدی، اطلاعات به‌روز هر سرویس را بررسی کنید.
﻿
✈️
@ArchiveTell
|
#API
#AI</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSI8WsSrBTgAv7UDSl1-FN8T7vDiQTJhYwHPeYEpqBlekAet3WqaDaGAIldqwfHsJMlRf3kzVWSGRDdon0Ic6ZlVsqfvDGNDYq5ig0og-5L9W0keO1E0kKl0Qf0Jb6wWxhk3It3FugfjcaWQ1ZWK1NueEA7Tm2GFrBO45gWxxQZZSqcIF7ACxuRk75njd2IY7CL3Ki-LE07oQS3R_O0nA2fbA1Ao7GNd25PIMAs6AyRM3HU641QAR_qVejBViWAwi6T5OdRl5u9bToeikFpMRdTKNZtXB6ToRHlhznq7Ob6i0OCgrvxFvbzodMli79LPg4Iu56xuXx4OXTSmQuSMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk_Lxfqua5yDsLNnA1f2Z3dDE-X6yXhc89ugKXebOqhEm8aki92Ybx1tp6Awk-nbPA7k5hKIW5HgHwx5-OYWIT8R0aqMoePimNsERXFBkMYjepsttq3S4aV-VSBoErewz1W9rygL44fun6OWT0iEiSJkMXk1A8U5kNeSFtAxx_KLkTM4eQ6h76rLNjv5f43Ch7jS39ECPru0wrrYxSWDXFL8HyXf5NlngNfCI0n-wkGLXVPg3eLUxAOxmqhaihAGqxcA896OaCg5WpCPi6AHNgZ2OhwvdiXFl7_UDmwL2-5NvJOEuoWbwoQBIAMCzSpMn3neXojqPcWTRgqBJ4LU4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWk15WOnOceSfnIOuLHVvsU6Di9sKP2HVtEe1tiF75J75IC5cBpXpH58CtTujfdG5IcYLLGplq3T4TuDmOyaFUeSggUHU4TA2XxqA3nFfqNRpHLBAzyA9JyUu4c5DAEEuSfOUQ4Apf-OFqK3EvJo8uYSAvWrnywEJCBRNzd3ltfoQjWWTkS0lJ2PfJWI6dezT_dEE6xPjQ_YbUZY_yPKkMcnhuvjDuHkyJ-Lx4jJpoXShkfUsI3LKSMktjpvG2tHk_uuVI6nUvP7csEINPNzbM4REK3OlPNppuJHLOdp6iIocEchhwtZTAMdbc7DUU_2cSO0Rza8Tyn2DBf1qINNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEYbUy8KRQquGOwP3YEWPcxiMkGXSkjoB-SzpYE13kXKgxlwGHShEZSV-ATqyO9VcKxi8gT3k7L70uoiJK5Ej84J4AD_2O3M-oD-OP3pe2AaC9i4PMFqsCag-Jl4m3-eSV7Jh8vMi-rexhtiVMR-G_X_LXtSZLlqdrc6B0SZ7Q5NksYI_ll37kncu_fJmhsh4bBM6HunT99HELuXkdtC6lVPBhQO6KJA12l3kiv6mzl-C35mF6EckNDvlmzK0iHfPHqqiiI6l6F7WOaCywLpfCby2Wf3KUq30kGgiInwjCZapVSI4uNrBHbD98as4wLcolHTXB08I3xES3VFTcR3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anvQp7hHKvHGH-wURc06JJfwB0UPUwkIrM4zoPsWxM7-_FNzdqziG9UxiOUcEbInomvqAa7PAp0wruqOJWtGNYcVTRbbfgq2XtjR2EU5OxDrh0VzeSdxNBg8CpKCs5oAMntvSJd3NoxtO2eC_UVTN2ehff7qFn9cXSBNOHt_n-Q1KuCWNBNQl34t7nVAxBGGV36cteo7ZlauSzSLZNeCRpqmaKFuR3gT3MZxMGRfprs8dfoNEXnloELhIKd14iwtGXpMuuhcetuCvbJAw3JfFZ9_Jc5qymeRfdYvy7fdSy0AR9Hn2-bUY3UztQ8jqYdkZy3f8A5aXmMuUT_h-LBsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szd79znRdRTfC2ICRSiYmdzgEmpfaa3aDM3cHnHq5sJjQYVjH2IsMjRg7jiEPNpsT5NwhluR7E-ClcuhqGwuFQsWk4KYcdcYkrKTMQbOH8iuhgdyJZFdyJGSdLeEz3UdbhWydxPAiQxfMT07la-5kx-41tDCozC5X3uNDlV47y0nbK_DRNASMTwEUwR8VrX_-L8G-t7LjFf8OgEnKuexjGmjvEnooAtxPFxbJs_EYZp3Ued97P6tt1-AHi5fwZ2bWbvQFICXpBnNRfkg6lVUn2FZGmEh8Lo9w-vAhsr4RxdtsnKtyns5dHZ1Xj8t8LcnrzJpv9CaDcvDUQkrHWlfLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj_dtMgm-Eo61Js97iMNjDeKTLwtbNFSPOr86yTh1_DbquPoOxne-dQKBILN6QEhj1G3-6K5SuWVL-JD_DdcSdHr3VGWPJbo0sNQ7i1XHUFt7eROc3w0N4xFFODFF1Czfvh8T4TngAhPuLmCnRwK5HmJIzD6ZEenLMbHeHk5Al68nUNOHL2IhKOe8lBTiuAp1MqqR7V48ayTU81UjoSLoqXt_gl4tA53aVaBRWJw-LVmQXG6ZNF1h-JbHM3SeRh9bsqTc3GrVKUVH6CZvaLP7-hs-EiH1kLSbkNuIn6g5EhbSJb30zvtXzowxM2h_1xVLkIo8LPV2KueO2m0gsfwtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=NCnuMfsG9T3VXVdvhmxz1t-6vWqmxYNgVNRfnKxV41FySgLuJ69IkfRbhKBL8LKkh1Idm3ZC3kEPh0JtLDuWv_VVgiLUmdAinm3dx0mMRL0SROBxrKXMrRcTwkbI5woAgrjjykdJZS5AQDmlsG0JVCR4mv1Ypx9gxBojSwfI1jCVsXCYmS0m6zqGlLG5s3UkGfHH0uipSEekNvWMaObnSPRp9aqP3bE0fwlzleQruDQrmTpzjfaGmbrnqipEklUay87rWrpFwHm-PEAjyXmMC8mZu-HiSBsLIV__TaMdqGfwmdy_SJo0erxlfu1RQLVs360syAK2ulfMRFvnjjhr_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=NCnuMfsG9T3VXVdvhmxz1t-6vWqmxYNgVNRfnKxV41FySgLuJ69IkfRbhKBL8LKkh1Idm3ZC3kEPh0JtLDuWv_VVgiLUmdAinm3dx0mMRL0SROBxrKXMrRcTwkbI5woAgrjjykdJZS5AQDmlsG0JVCR4mv1Ypx9gxBojSwfI1jCVsXCYmS0m6zqGlLG5s3UkGfHH0uipSEekNvWMaObnSPRp9aqP3bE0fwlzleQruDQrmTpzjfaGmbrnqipEklUay87rWrpFwHm-PEAjyXmMC8mZu-HiSBsLIV__TaMdqGfwmdy_SJo0erxlfu1RQLVs360syAK2ulfMRFvnjjhr_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dnc9Dn_wVGOsA8nSIfKhfMZ-xCBuhm59yqXUHEr_t2mR-lglkKeWWmYCSNHPRBwWYFe0U-piJVpT7D0Kv5_L-uEWDBOV58-_3nSVOyW6lUH_tTUOKcS-pWohXu2B-qlwkpXhb9dFVIQm5S0QOmrBcEJn3i-N-7XkHrs2kGWNWmmIdb49xUS9agSCAXVCo7aC6eGTwVY7IKg824od1Py-QBtYD6suoUyIEX1qXeASRaXL5J1TvKs3WBJuINJ5Mf2_jC2qSdR93MmVC0FQPKQ9-YoUbNYBouTK7m0k0kmlcZ0RPz6l79-2L2thbBXZ0VqHC1BdbreBCCxcsAJ7uxcVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7GfX1SH5vs9e_0Kz3oU7lrE5DY1nIdyosuOu8f-1gziOjKPi1sH7xFXtNvOJUXHzWSV_TRAG3pJEy8pNNyGnH1IPIfvJwc5cVbaOnvdXj18kR8S2YoxUdontlLXwCoYQNXNnLF1rrbPijhcaM6ECZC8N3ewdZpNTUi4WxG66wNE4BgO6Y4WKWuR0UJWYc_BSARuRy2V0MuDF4yXPjL169yQgelfuLNcok9kqREOZ-OcQE9E9d5LMv88K__CWpb3NPGI6o31LJhynjLLkKa5oAymwGZkozCKyzSY9KZRSZS09_wyQgro7HCjgIfX1joP_bTQQaPve4SpHsd29gmBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
10 میلیارد کلید API رایگان MiniMax M3
👾
📌
مدل‌های موجود:
🤔
MiniMax-M3
🤔
MiniMax-M2.7-highspeed
🤔
MiniMax-M2.5 و مدل‌های پایین‌تر
💎
کلید API:
🆓
sk-cp-jqkYZKrokpSo6XdjlPb7cHA2kZfLdhdZwgtX15DsiwBAbFjb221rKvZtuZvPk0xEy7AaEZnD94ugiuDisZ8U1sLs5qfzCAHog6ti5fjjUsqZprpRqiNzdBg
⭐️
Base URL:
https://api.minimax.io/v1
(سازگار با OpenAI)
🍀
✍️
همچنین با موارد زیر کار می‌کند:
👀
🤔
MiniMax-H3 / H3-Max (ویدیو تا کیفیت 2K)
🤔
speech-2.8-hd / speech-2.8-turbo
🤔
image-01 (تولید و ویرایش تصویر)
⚠️
نکات مهم:
🚩
سهمیه هر 5 ساعت یکبار ریست می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJgU7pS3cancy8FnIDvaSxFq9jWPCrQomHUgf1E6W6juyC2E94cIQb1kUpbRdNVf7YXbobWsjgoTVUgIC9DykKpqsE9tehaKylKEi0Vbwzq7ccXkzqZFcAIRUsnKQ4t6ogiEC15n4ifQbDmFqRA1fE3kqlLL631cFrB0l1dvlLhOU1TpQvqf_lxLQsmxXrTauB51KSvj-CX7JeZY2X9OVKz0pZ4OliayfMNvg23vZANG7OU2DEQksQVNQZBZcxfGcdE1J_jivKKKleQKGp-w_gd9YK2jZXP0wTArmhMzSVuWlho9lFUgGO8CluQWVHt-v_7Fflm_EQMpQwUvUjShJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
موتور Agent Executor گوگل برای اجرای انبوه عامل‌های هوشمند
هر عامل مثل یک فرآیند سبک اجرا می‌شود، پس یک مجموعه سرور میلیاردها نشست هم‌زمان را می‌برد.
🔺
خواب و بیداری زیر ۱ ثانیه
: عامل منتظر تأیید انسان، هیچ منبعی مصرف نمی‌کند
🔺
چیدن خودکار محیط
: مخزن کد، سرورهای ابزار MCP و مهارت‌ها را خودش نصب می‌کند
🔺
جعبهٔ ایزوله
: کد ناامن با سقف پردازنده و حافظه و شبکهٔ فهرست‌سفید اجرا می‌شود
🔺
هنوز نسخهٔ آلفا
: روی سرور خودتان با فایل پیکربندی
ax.io/v1alpha1
بالا می‌آید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری مجاز است و اعلان‌ها باید بمانند
📌
سورس و راهنمای شروع در گیت‌هاب
🌐
صفحهٔ رسمی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao51fCW63WW79YIKcJvCXhibx0yuUD7U_cd2U4RuRkIrLYLNEneiWJSnI4DRdeLFdeJdza6tu8-3Q3ao2SxjCe2m90V7k8w6pDxiRQ45zmR6YFb0DyhMTQrxkWNL57Em5t3iLlNYxOVUGaqb4eY-c4ki3HL1fVsfvrm-IHTfABBuGsXNI4ZfOFWJtoV_nYgxzx8fVB7XYe1VP0TU384Q3DRSBYip-7M-Gj37a8YJ2QJ03kJXjaZqoJaRk7M21_lzWD8C-x23bqSo4fLcL3Ni8ytv6idxkmgUIFvnuKLaDbAUyNaVZgquTDQPzDMX7F1_Xf0FiF3t4O2Fw8CsEVuvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🥹
2 روش برای استفاده رایگان از Grok 4.7
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
Grok Build (رسمی)
نصب Grok Build
ترمینال را باز کنید.
دستور زیر را اجرا کنید:
curl -fsSL x.ai/cli/install.sh | bash
به پوشه پروژه بروید.
دستور grok را تایپ کنید.
وارد شوید و از آن استفاده کنید.
💬
نسخه 4.7 از Grok در Grok Build پشتیبانی می‌شود.
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
2️⃣
XPLabs
به
platform.xplabs.ai
مراجعه کنید.
لیست مدل‌ها را باز کنید.
؛Grok 4.7 Free را پیدا کنید.
آن را انتخاب کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzjd9YVcXxGqH0J1D8hdgxgxnVx7nfeFdm4qhIgWQ6PuIqJiNL4AXIEoQ6VzEEU1tOOFZ_Az05dWXDWW3b834mLNAm59H1IaHgTbkJAUs5V5Ko5WgaZg-lFX-TVVaY4Kewc1xST5K-ufCU996Jj88-jkkQ61WD44Euvi0ezeX5zf52QZEgRaMEBLk3TtuMYjj5nNyGlVHRpbnxg69BwR_CcuqlfRTwjmD4o5BXJubAIPhztO1ZbO7nB3xDuMa2mUwpxYtG7JhkZBOkvnR3BQuLv8Wn9CvgK5Za56ZPD8Jn88ski6nnPEya0g-4rCapQTOPNwOkDsTlfR7xt839TXJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBjLTUgyIeYAD6JvE3RTgTJNlETKP0AdUa15pd2kK8jWxTedgM-thAax06OkV0Y9YbLz2Kzp7B9hKCqxFtI8cF1n1ukZFAQPg_7r8LAy8Q2RSQRZSCdlJF7YCQfM3IxL-U1G3Rm5UdanrPYqQ9-9nuNeSCDNTl2AVsGlYRbUewo5kiM6OFd3mvTIj9W1gIkgxX58R29yL0iVYjeGkuyLqU7Matg8y-rn5kNhM6uuF4YXP3gUmI57jj16-UOdJpcxqrpk1TZIVz3KfsCJ65nLqgfQDrhsr6bhMHH8HTRMJd3yNHdHGu7U07s6FiWS4-NCdP0LN5idJClcInCHAPVkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faK0J2uNTCi4pDkmnPT43yGikkX-Je3NfuKIboQnUgmyL8Z20E77vPA0L5I69FwMAOpXZebaff2xdb5FvqfG-n1o7ZBuPc47Lu4bjvnHT6SKK95MtL3LGR-fNWQXA5C9hImXNX9yfkfaKgUkdVA6ukrenSBdj62-VaXiriaYgurlNgOsl-LYrn-xsnr_84TIFNvM0x7hdyeXO10B-oAnhI8TMMX8D2QnorjWeYVBRI1vvnvdbk1ZZr829LmGXvEaXhzDQHqSfZ6Z9BE1xhclLFOzj05yQu2-tYOkIAnfPFziyUu3B5ukifZqVo_CyAxNunfImslfNhZYKKG6jOqfkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
دسترسی رایگان به mimo-v2.6-flash-free
🤔
نام مدل: mimo-v2.6-flash-free
🤔
ارائه دهنده: Xiaomi MiMo از طریق OpenCode Zen
🤔
رایگان برای مدت محدود
🤔
صفحه مدل:
https://mimo.xiaomi.com/mimo-v2-6
🤔
OpenCode Zen:
https://opencode.ai/console
🤔
مستندات:
https://opencode.ai/docs/zen
🤔
برای استفاده از OpenCode CLI:
curl -fsSL https://opencode.ai/install | bash
🔥
تنظیم مدل: mimo-v2.6-flash-free
⚡️
میتونید این مدل رو در
MiMo Studio
تست کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3pOuuVD5Y-_hPPleQWZmg0ctqlf4R_4SQ7wK1SL42HzrLc_WENl_Cd1HoppTp62aDKHaoHaP5DQ58iqlcScprusHzbs9Gj5VC_0Fir7yQrsmWNKM5uCxkv3jXRsNTweIzsgGXKAM4qgIA611nG8tUVzR0Ydudu1ak9zdYjxx7di1yPYZ9LJZwh5-lMD0NwPwRGHV0qxMNmrDZM5hNfdNprGyHYKMvqF31hzit_5mDWLWp_x0yuBAQdw7B6B7TOoF7h5Wp1wnDrCO8_QDn-t1bpoIuF9Zir12kTEmF6nv-ZvYjJtd2D6mDiaB2sIr040GdnCNf1fC4LXpHuRgQsEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj0rOXJMFzKQwbzCb8ewqLH61aBlFrdDg-f0lELchFcEuA7mS7w8ZgUPhWYYEA_IBGM5oNKohTwcLAc4xLBO8NUr_QObv438HugJVL45p-Zkd7njoockp-umf5VUcE6zX5bcd_wZJT4aRhNIb2AoGb9NN18AQlh_vsumrldpq0j4FSs3p2BEmQTWBxQ8GlL-BCvD8Xoe6NnRlAe2FALn7FsuN7trxZazBNfKVJ6bSnslKzhkFToyF1o1WVILTn7c3KE7AetbzrC9pmjyRglRjsv2Lnr2eYEdQXEbroryBweCP_d3ieoayr1tZZXaPUpbkJdeoCKj6r0rK51qsvRPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=pOm28C087xcca7CxodDtPtctRBAsSrOMDFH41zgJW0Au7Fkd8LnCTXV1uv7x2bg77ehTvdqJg-moZTSfrO3UXy8j19j0LJWyORn7q8c-jeyp5d5Q9XeIFiy63ib70GypNuMcSGZUphkO-s6UKStnVIjeSs0OKYT-5QpMY10DkVPUcloA86KrNudcEf_SltmSWt_WrW87r_fPE_8gDJzg7jke9Mxg-oxgS8ECiWEHpvLV4-vnpIgw5xB5wQubmAsRwQK-w89Fvyl6RKH8Wso98NrdLtOnh3xpOXGMyPFZFvLXoUbXAUFvwjrG2hiENPy2g1tptounlCSPytnuM4V3XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=pOm28C087xcca7CxodDtPtctRBAsSrOMDFH41zgJW0Au7Fkd8LnCTXV1uv7x2bg77ehTvdqJg-moZTSfrO3UXy8j19j0LJWyORn7q8c-jeyp5d5Q9XeIFiy63ib70GypNuMcSGZUphkO-s6UKStnVIjeSs0OKYT-5QpMY10DkVPUcloA86KrNudcEf_SltmSWt_WrW87r_fPE_8gDJzg7jke9Mxg-oxgS8ECiWEHpvLV4-vnpIgw5xB5wQubmAsRwQK-w89Fvyl6RKH8Wso98NrdLtOnh3xpOXGMyPFZFvLXoUbXAUFvwjrG2hiENPy2g1tptounlCSPytnuM4V3XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚡️
یک خبر خوب برای طرفداران VS Code و GitHub Copilot!
اکستنشن
🔀
Router Models منتشر شد!
با این اکستنشن می‌تونید مدل‌های مختلف AI و Providerهای
OpenAI-compatible
رو مستقیماً داخل
Copilot Chat
استفاده کنید؛ از OpenRouter و Ollama گرفته تا APIهای شخصی و مدل‌های Local.
🤯
🔥
قابلیت‌هایی مثل:
🤔
مدیریت چند API Key و Failover
🤔
تشخیص و فیلتر مدل‌های رایگان
🤔
پشتیبانی از VS Code Settings Sync
🤔
؛Import تنظیمات 9router / OmniRouter
🤔
ذخیره امن API Keyها در Secure Storage
با دادن
🌟
دلگرمی بدید.
🔗
GitHub:
https://github.com/web-elite/router-models
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Th3EYb7iwuHwB3PyUzznBVBxLg9klkUZGzyyAIzeA6mWA4ugtmeSKoGJwkrykW_fseUIfvPis0yzAPhnKaEwZQ7ec2d5gP5j-x5FrGDZsXQznQhBSPTJTPiO0_b4k4KeKPFBhMVnLGtTM4QvTb9hakoGKW3J8cIgi3hLk85NqYP1NVV-Q2ZrcFNYB2z1yXeN3KxssUEBA82A0gTal5u8fq1bwxreJDQTeAOWcDBMJ8lvrBtffvqzShVpUhrkqlKLNzRkSqAulqLFLcQX300UcqtlbAmt_PLrGZm9ONBLib8D6rMc8E0FxWKcpqryoAegX3xsTAT6C3t-ziA2FThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥹
نسخه 4.7 از Grok منتشر شد — قدرتمندترین نسخه Grok
🤔
پیشرفت چشمگیری نسبت به نسخه 4.6 در تمام جنبه‌ها
🤔
عملکرد عالی در حفظ متن‌های طولانی، کار با کد و اسناد
🤔
مهم‌ترین نکته: قیمت بسیار مناسب — قیمت همان نسخه 4.6 است.
🤔
با توجه به پیشرفت‌های چشمگیر، نسخه 4.8 از Grok به زودی منتشر خواهد شد.
🤔
برای
تست
اینجا کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7810" target="_blank">📅 20:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7809">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaq6nRaQQkrSXCvp_AEq83ktJmyN6TQcjaSdi0HyTHIYW3wOoxoMExO7dsmicEhk1wXQv59imQcHVJgR7dboPmaVsA6plO31E7JgkZGeqGtBacuvDcULgjwt8rEasrkzGoyL9mZThwBVzG_nx7Kcd3V6FCFhn8I6PZWSZ_rk8YBrobgSmZ6_EDBbmfEE3CMa8UsHX6dY38lBZR7iwi1nxto6uM665tSuLAyOJikykcvh3XOKndY4ST5a51tiEWdvgcDUDVc-FZma7DMkwsIMreHFTAPTltWf2x_R6RD4GgVbBwJDC8oLwaRnRELgt0aDjIBMU2tcAvX8haxvSTm03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
500 میلیون توکن GLM 5.3 Flash
؛AutoClaw دوباره توکن توزیع می‌کند، این بار به طور همزمان 500 میلیون توکن در دو روز
21 سپتامبر: 200 میلیون
22 سپتامبر: 300 میلیون دیگر
درون آن، GLM 5.3 Flash، Deepseek V4.1-Flash و V4-Pro وجود دارد.
🤔
دانلود
AutoClaw
و ورود به سیستم را انجام دهید.
🤔
بخش Credits را باز کنید و روی Redeem کلیک کنید.
🤔
روی Claim کلیک کنید.
⌨️
انجام شد! حالا ما نیم میلیارد توکن داریم! مهم این است که آن‌ها را در طول روز خرج کنید، زیرا در پایان کمپین (23 سپتامبر) از بین می‌روند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7809" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7808">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhLu47rgQX3RP2tZ3961N8ZDbse8MlEVQnm_UezyAh-IMy47myHoczD2_LoxK7cpaFYR30pN_5JnrIpm_NCRhZdYFEwRh0XBlDBNzvnV2gBurQFZEkSSDpyDpVXcbVLLR-VEFPTt36v2Wp9h-alqwDkoUK9ystdvQbfocCIGh_5kSRV3jG5BHZChYRJyq_X98HKmlSmMTK_ElO51sXBCNfrmwYReCkETqktAoTPoZC-UCgdYc-UxPF3U_j0d1_WF-D5ZVjrYct6I-GDp23lUXGs4i2ANBb4I-j9-icuVOus3sW_LzzbwgRYYgeMxl-KU5wgjL0rzLRps4CN5zJHOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مرورگر Sigma؛ ایجنت هوش مصنوعی داخل خود مرورگر
مرورگر Sigma روی Chromium ساخته شده و ایجنتی داره که به‌جای شما توی صفحه کلیک می‌کنه، فرم پر می‌کنه و کار رو تا آخر می‌بره. هدف رو توصیف می‌کنی، خودش مرحله‌ها رو جلو می‌بره.
🔒
مدل محلی Eclipse داخل مرورگر اجرا می‌شه؛ طبق ادعای سایت، پرامپت‌ها روی همون دستگاه پردازش می‌شن و آفلاین هم کار می‌کنه
🧪
حالت Deep Research برای جمع‌کردن منابع و خروجی ساختاریافته، به‌علاوهٔ چت با هر صفحه و ترجمهٔ سریع متن انتخابی
🗂
ادبلاک داخلی، تشخیص فیشینگ، رمزنگاری سرتاسری و پشتیبانی از افزونه‌های معمول
⚡
در بنچمارک Speedometer 3.0 روی مک‌بوک پرو M4، سازنده مدعیه ۱٫۱۳ برابر سریع‌تر از کروم و ۱٫۳۰ برابر سریع‌تر از سافاری بوده
💡
نکته:
نسخهٔ فعلی برای مک و ویندوز (149.0.7827.117) و همچنین iOS و اندروید موجوده؛ نسخهٔ لینوکس هنوز منتشر نشده. بنچمارک‌ها هم تست خود شرکته، نه مستقل.
📌
دانلود
🌐
سایت رسمی
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7808" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7807">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIHzuFkgIyvIuvtgoNGeIbWjoGH7Oy68AtYpJQsqVnyFC6yCKVPRF8JoMVx25OABfSgCpOHG7XmLPlehuOdsJHVS1hwmlj5SuYJZEJzB6r_u9JV26_PiEn372JH1wjGJqWM3HdIXC7LeTrHGYX26OVqSd0KfD0r_2q-aqTXakN3TCH67ffAMy94j1o2ZrDq15IEEzJbY1uyoWiVmHTcunUJ-jymitV_-s5GE1r1LyXd0JkNoetuLL6iY5dHpzbnmyT7CDtvyxP-W2gVtAgUL6yK3HCa4ArcB0lHdui_qsBiPluilppzC8hGpYEvjo1YEeq2xD2ApgYGX9WROQUd_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Jev رو رایگان کردن
🤣
console.typesafe.ai
120 میلیون توکن رایگان میده تا هس برین بگیرین، درباره کاربردش بعدا صحبت میکنیم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7807" target="_blank">📅 13:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7806">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiWnilglm_wQPXpIFXGEIFion574OusfZ4-IEkJl52fNwn4IcMqU9Fho_We170H0htHkHNCZZ6fnN-MTOgVU_m3W7rC6FUWXxVshIwl9BX3DN9hTU7eicjTEaBVx-yaDu90lPhbiQlT-X8jzKD7kx2192t58XXJ0Gx4YdbfqD6UkYpM0OCvnxQinN-aEnCxurpW5livbmJM5MylVyd1bYc36tn0heIQ0ExCT-P1kHBQjk_0MHEuBdITR_5rbo66jVyGNeGBPZMyh9Jpt0xji7-F-BcmQcuU-vf7_5hRsfg_b42qLL-Wz76TmNgZUO8C8ySP1jKu7Pd1qSdTRR0QGoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود iso ویندوز و آفیس + فعالسازی رسمی رایگان!
همش در وبسایت زیر:
✅
https://massgrave.dev/
سایت قدیمی و معروفیه، سافت ۹۸ و اینا همشون از اینجا اسکی میرن
😱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7806" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7805">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QblHlDqHLCX1sz3drvna3FLEkwgxXG2yFyQUZG3uTSz9CfQqFPbWEw6QnKTfQS6qCmq7LayPRwOJNVzdiv4j2XdWI9etaFWVgJV1euggIVPn9nxO2mIXuhMx4u_ujFVcbEONTYH98L-9IECjNFv2pnbpTALuZwWQgY2rRopex2cFtcBzef0Gkxs_Fql8vQdOtJ0ei5wmP-CxCAirL9ei6PUckynsxwLopjZRWdC0_bwdMTxEgbDIktiR7gaqnYJC30jD8HZ46g2-vdCxRwG0hF-bJqrboBE8dyh7GciCANrl75PkxnOEjEH2MwZ9c8EOTOA3x65ovzgXHGdLh-cSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cloudflare Quick Tunnel
☁️
یک قابلیت کاربردی از
Cloudflare
برای ایجاد یک تونل موقت بین سرویس لوکال و اینترنت، بدون نیاز به باز کردن پورت یا تنظیم
DNS
✅
با استفاده از
cloudflared
می‌تونی سرویس لوکالت رو با یک آدرس
trycloudflare
در اینترنت در دسترس قرار بدی
🌐
🔺
بدون نیاز به دامنه
🔺
بدون Port Forwarding
🔺
مناسب برای تست API، Webhook و سرویس‌های لوکال
🔺
راه‌اندازی سریع و ساده
📌
این قابلیت بیشتر برای تست و توسعه طراحی شده و برای سرویس‌های دائمی مناسب نیست
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7805" target="_blank">📅 21:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7803">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cz6rVmwwYPNoe2ZfrscbqJ8OslTFmjOIAa0n-kociE2xQRH3XsNJD4uM74HinwOUr61HP0RUEs0LpbIQ62vA7l5tR-q4bQfI8MQaEqokgEbX9PwCwQ4tIfer56Up8oVnS9DU_jV2Kf9BHkysYaf7qJtvCud5VnrXiA-NFXCx4CAeFodMXxjZToXXYMJu-SbKxKFiy4I9ZzU7MD8WbgP1nxGYi-GjL16PhqNfAvw2dZbBshczTF_haLB8GDPdZIJqJbPs_SJKRW1S7XbV9je6iqxUwgcZ8rXwEANpXbcs2WSIvKA3dzadjL2oye_AsNkDhh2SBhGtEPnPlD8TlVFYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج طلایی API هوش مصنوعی | قسمت اول
🤖
سایت‌هایی که برای ثبت‌نام اعتبار هدیه می‌دن!
بچه‌ها یه لیست پر و پیمون از سرویس‌های ارائه‌دهنده API آماده کردم که بهتون اعتبار تستی می‌دن؛ خوراک استفاده توی کلاینت‌های مختلف برای دسترسی بی‌دردسر به مدل‌های پولی!
🔥
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
سایت Modeloc
👑
└ خفن‌ترین گزینه لیست؛ همون اول
۱۰ دلار
اعتبار تستی می‌ده!
2️⃣
سایت AAAwinn
└
۱ دلار
اعتبار هدیه ثبت‌نام
🤒
اکانت گیت‌هابتون باید بالای ۹۰ روز عمر داشته باشه.
3️⃣
سایت Jucodex
└
۱ دلار
اعتبار هدیه ثبت‌نام
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
👀
قسمت دوم به‌زودی...
سایت‌هایی که مدل‌های
کاملاً رایگان
دارن و
هر روز
بهتون اعتبار می‌دن
🔜
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7803" target="_blank">📅 13:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7802">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔥
دانلود فایل های پولی، کاملا رایگان
- بخش دوم
خوب سری قبل گفتم تورنت چطوری کنیم لینکاشم گذاشتم، حالا یکی میگه من حال نمیکنم تورنت کنم چی کنم؟
یه سایتایی هستن که سرور های قوی دارن مخصوص تورنت، شما لینک تورنت رو میدی به اونا، اونا خودشون  فایل رو دان میکنن، بهت لینک مستقیم میدن!! و شما به راحتی با لینک مستقیم دانلود میکنین!
سایت سیدر یکی از از این سایت هاس برید توش ثبت نام کنین:
✅
www.seedr.cc
✅
با این لینک برید ۲.۵ گیگ بهتون فضا میده، ولی برین تو بخش Get space میتونین تا ۷ گیگ افزایشش بدین با انجام کار هایی که میگه
🏃‍♂️
خب حالا من لینک تورنت رو پیست میکنم تو این وبسایت و فایل ها رو بم نمایش میده، روش میزنم copy link و لینکش رو کپی میکنم، و میام تو تلگرام وارد هر ربات url to file بشین جوابه مثل ربات زیر:
@uploadbot
لینک رو بش میدم! و به همین راحتی فایل تورنت اومد تلگرام.
برای تست فیلم سریع و خشن رو از تورنت میارم تل که ببینین تو کامنتا شمام تورنتاتونو بفرستین
❤️
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-60DrYlrZhCHbFWF3GtvDxv5OswTlhHaBEto1uZGXh9PYByWtQzCyOWpUlIt4cGlaSmKPnCGiagi8DCawJq115C7nrzF9eclXj9r73eMeu6iGdnOcw6qGZzs9a4SkmlwE2-iZBElBvNwT59X8xvzV2a552Uk9bCPYtV4mmoe5obifL0oApbua3PhBIHKRFgyeANHTsnr1PG946Yv-Bgs1BnWscW3dwj15bHWFygKsgpDyXnYqIMdWu0Y1wq1zIk8AGo0j-gpAJUdd1xUmWsagRSL2mXeekOaC5dLwSDTQsW9r15wrjhp8l4ezW3BF6gzvZgiPCaiTMFuVACbwPiYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دانلود هر فایل پولی، کاملاً رایگان!
🔥
اصلن به این فک کردین چنلا و سایتای ایرانی(فیلیمو، فارسروید، سافت ۹۸و ...) اینهمه فیلم خارجی و برنامه های کرک شده و کتاب و اینها رو از کجا پیدا میکنن؟
بعله منبع ۹۰ درصد این فایل ها چیزی هس که قراره بگم و کاملا رایگانه!
از جدیدترین فیلم‌های روی پرده با کیفیت اصلی و دوره‌های آموزشی چند صد دلاری کورسرا گرفته، تا برنامه‌های کرک‌شده ویندوز، اندروید و هر محتوای پریمیوم، نایاب و بدون سانسوری که فکرش رو بکنی
🔞
💎
( آره حتی اونام اینجا کاملش هس
🤣
🙈
)
اصلاً داستان از چه قراره؟
اینترنت یه شبکه بی‌نظیر داره به اسم
تورنت (Torrent)
. اینجا خبری از سرورهای مرکزی و محدودیت نیست! همه کاربران دنیا سیستم‌هاشون رو به هم وصل کردن. وقتی تو فایلی رو دانلود می‌کنی، در واقع داری تکه‌های اون رو از هزاران سیستم دیگه در سراسر جهان می‌گیری و همزمان بخش‌های دانلود شده رو به بقیه هم میدی. نتیجه؟ سرعت بالا، بدون قطعی و کاملاً آزاد و غیر قابل فیلتر شدن
🌎
🔗
🛠
قدم اول:
نصب کلاینت
برای وصل شدن به این شبکه، به یک برنامه نیاز داری که کار جمع کردن فایل‌ها رو برات انجام بده. کار باهاش به شدت سادس؛ لینک رو بهش میدی، خودش بقیه کارها رو میکنه.
📱
دانلود نسخه اندروید
💻
دانلود نسخه ویندوز
🌐
قدم دوم: لینکای دانلودش کجاس؟
لینکا اینجاس
🤣
آقا یکی میگف من با تورنت حال نمیکنم. میشه مستقیم تو تلگرام دانلودش کرد؟ بعله اینم تو پست بعدی میگم. نحوه انتقال فایل تورنت به تلگرام
😜
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7800">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🤖
JIJI AI
مدل‌های موجود:
⚡️
GPT-6-astra
⚡️
GPT-5.6-sol
🧠
Claude Fable 5
✨
gemini-3.8-flash
🚀
glm-5.3
🔥
deepseek-v4-pro
روش دریافت API :
1️⃣
وارد سایت بشید و با گوگل لاگین کنید
2️⃣
وارد بخش API بشید و کلید جدید بسازید
3️⃣
شناسه (ID) مدل‌ها داخل پنل سایت مشخص شده
Base URL :
برای GPT:
https://api-slb.jiji.cc/v1
برای سایر مدل‌ها:
https://www.jiji.cc
🔗
www.jiji.cc
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7800" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7799">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffr-fwSaOiTKAJnOdI0nTIdCO2kHYQUXqir_7_1XSv9x7cTCyXazeFywx9zxWGEmfX7t35U101tZOpPvVTEPSs1HedDZaGkV5gK-81q44AMiHtBVYItzUBaiA1zdnKgmT8zTbMwl_4Jenl6ZS5oft2D_clbp-Ctp9rfnCGgETPspdpwXETDe8zX8wBTsS6epl0OZ6ttp2lXnjcIGFgOi_hiu_fNg2fDXzIzX-N-kRBSpwByXXWLkZfJHtGjmqa-1cc1NvEpTy7aYNu6YlbOUMMHSto4SPeTVQRn7PL28_ggnhtXorpMFih0-JhVrP-5QNzszpxy4zfUIdHDkPXf9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVNcOUAFfuTBltj8wDLIUP-xhi1AHyUKlKyrxIAI-6c3sOpCejQcVmlnuVFRBX85lIvoBa3uYjBVe2jSzUQ_jQSESsS2_LmWQuw69oF5gJDLWJpSNFuCY00OaL9RROcFHPWAkWzeSe4bLzeBCioL2aZkRlpXgjwr71Pm75ySPDt1owBI127i2Yq4UNnCE6Cq0U_iWB3t7I5UK6_oUY97xpETy35JKKiglz_fz5ZBlpI57k2vpKFmpaxlSN_2QJUlkJM419m1BWsuEZwG4GIHlo5xtN5k5fTQ6W2CUHce_S-zPJ-lSpf0v42eD0Tvm17WBX_QM24xiShYlCW2Nbt6YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX1YqDj45tY-JaYivMoC51HwZWlhLNVox_LjQVoOzGnPmH194TQfXNSyqSIFZda7errcvKkS-CuxUQJmg1Ga2buFNZYMjMrfcy0ZXjsZN-pwsjoHBPkkDJQPwdMf6QAkzlz8qh0jVSiF23-fc0dizzJLG4doa5s46BQIUjRgZNuLXRZ1U9lc6KGopJMfvcgydOZdCeiEW9PHYuC4whvQE5K5VwVnPHaBB0tx1PnJM0S7TC_i8RkGSvgX9cuP12719zekWJd7Ot_DjznEAyJzQOKMF8Mondi24WHH1uzP5lHdkiBUqipC3HPEW0RmO-gYpVxchZFMc15rDfZ8IucwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل GPT-6 ASTRA به صورت رایگان در MiniApps در دسترس است!
قدرتمندترین مدل شرکت OpenAI، بدون هیچ هزینه‌ای.
آنچه دریافت خواهید کرد:
✦ مدل GPT-6 Astra به صورت رایگان
✦ قابلیت‌های استدلال، کدنویسی و انجام وظایف پیچیده
✦ اجرا در مرورگر، بدون نیاز به نصب
نحوه شروع:
1. این
لینک
را باز کنید.
2. ثبت‌نام کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7796" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7795">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMdqZ0a5ZsJvNj3cx3CQFw1wTsOhII_2T_3ktnyUFbxbCd7gRWyTI0rZ8OBt-gU4_0lmweTuNT6hMXQFVaGTXuAJ-vEsb3XH-8FVjLwpLWlO171pikpap4SvpHe7-atMUn0P4SiIH4XX_pBGdAIh7hFX1M714uu6buy9-Vync4dNnJLBTZ_D8_LydVYtm0zpbUWNHdLFnE7nxnpvyNIOaR8VFbl4HWkujE6ajY-zJsmLW2Nx93d-EBAyL-mWf8kORCM_5fKouWrZQSysdHs5Zo8yI5gyrQHQ2xAA9OffyZLsi4_TnIo_rqyRxjFWQsAIltz1Qv6UtsFMdssEyqp7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
مقایسه‌ی تصویری GPT-6 Astra Max در برابر Claude Fable 5.1 Max در تست کدنویسی Code Arena
به طور خلاصه: Astra در انجام وظایف تحلیلی، محصولی و محتوایی عملکرد بهتری دارد. Fable 5.1 در جنبه‌های بصری و تعاملی عملکرد خوبی دارد.
در حال حاضر، GPT-6 Astra Max در مجموع، رتبه اول را دارد. می‌توانید جدول رتبه‌بندی کامل را از طریق
این لینک
مشاهده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7795" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
