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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 02:47:57</div>
<hr>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIb2j-xkRK61dy-eBl9BYIgGrj6R-CilMuTBPNDJQEQv-4y3QSChFuRjCHxeWyOTdNeiK0Q_5GQ3i8Iaop5IcY6mk-13qWBLETCNcPfg1DnJTRRdw9-9zWFDuUb8qm-mAabLtD50DGvhonmJZ1egT8HDm04T0__DxB_L__LfatDQaKcgHgzVIOh_jW9_6sn5mqwq3xIge5jYGcrNnyi7qQ6hsEuvUeAj9IMi5uIXm3WPH6pyI3q2OXXqwIL2mHso4vpSaOkZvL8NDQ-hZtsGtROtVJPy1Wcbtl6-BHC-sbv5KddNv5oRUTN2tl9_xWu32lFEbmRFuKy6x6LAnQqptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-CBf-kTeT6EbQpbyZc0LMZ-ZrfBPaYUDWGfhbDRg42CxJRFS5NdEc4peefKbTiEk6Jb0g01EXd8-rJNqdSoVfAd3J7q0Gai0xBsgRpjynWI8V-2p7_ha5G-oYfdcbcbyCgpDuDXpQkUJJeDS0cUgmKtRp1R78sLo4WNft72TjvGT0m057FKCsCwz0RXcn68ptB_g_ZMu2JUqGuMdWWTcUaEs2oPTgkItlqD0v8hvkpap5Sxl5dxE2GCGJBlzz7SsKzzR2lDJelnCO1Fd7rvma4Dx4mT3Mkk2Mri3yHE2PxpDJ0He2sS5N46b-BAXYXlyonj2N8cmSCOnMupuXqBFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKgs3fwLHnKcVoT7wszhdqQhJnsMHeGyCabVtDVnRE-h_wcG_Sl6LPlg2uquu23a7-GxeHqQnmBj-FJs6h1hUQmgwq1vHEdoPGqGA7Zp-h2ftCvS5d9ZF8zNBYW_0U1P9zt2vjECPIeAOyFD0w-tevQ9DDWNgCDld7QuHAHGENdxnsSdMNOiPg0aZ-WnfGfQJhxG_fqzU3o4TuV57OoeLepvQxODl9m3KwMaUx4dy-cNp7qE7DqrK64zwePtEvBwzj2zKsnZmTJN3oTUfedzIpX17Cka7KN9KJMRiC72rwB0yreNngZrQ0xhXK64DfFzNuE8YTEAGJeYphyNY6VYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7o_I_NToE66jFLsZdaUKkEL2_I5cARe6WGWab3X6J9ssLH7d1Wax8tvjJzjFtQYdgOzafr2P96_idSYZbe80iawaBl5RmvHsTWaq4JVMbyylBAPn7nDNHDQOjsCQ_-MqDrkmPWVdsZNuN2xxLigQsQzzj3LEuEV1sSpO2Fc6lFeDnzbGmQsxQSlMhmz1sq8KWGSjU8y8w7RtUYkfDo01f-5PsZrGfiOhLTIrw5_uNQESR3U1yiCUoWFGvE-5nPYT-S1TxsSO1j2NXShHxTWBsnpDehgm3km4P4iLfWfj_ywfBi0O_YpvmfLrzKMr6WhpyOiULPIgkZ5zV6QcH5x8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYhJDZzm4dIkOAYQXhW8fSKKOdC-YIT86JDE_WtbGju8GOa2z-mA-Le1Sf4xxXGVWRTo0pISicZFb3ux9bjSvtP9lp_fnzA7dHK9Y6ovY3C7esgaSJDRov-Zh3NchE1Io6T9UkcC3rLbXm4CMFfPaeqTD4qqKGT3kAZO7pyiWcmRup7G469BrjpsPiXRsYUOd6GL6njFRzDo9BJAnI7BZaFtyn-LyfifRYC7W4N5XRCVZ375ROnElBQY0p2631i7SVqNXfBtZ2scU7g2_g12SivVtX_O0jSLqYUzMAHUUjEC8XViJYhKr5Gpfx_4tNP0dwPwaFnIW3Vgj_MBRdDRRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwCgJBV0Oy8w0cfZBE-ltxJI5UekttWhcumAIb4QHEZ6pxGGZUgmYmIoDToSkUICBi2Brt10lxaWSfRUSNkid2EHHAT1SSVzzZB1rgUdNl_b2sWsVs9AXttCDogJU6L2guD8ReKH4IBlhG0KKXeXSUYuZ3qnING8Ab8aBrrxvcvKa873ObUidrFT-eU84MqV0cyuMJkf_TOoxxT2Y2P4Z9pLkPAPxPRwWc67BAlIkxGSvwVLMRZentLPh74x_IW6r0ie8kJS3Y4Dmhqtx20k7-OXUgslowX3vq7QvMjmAM-XIFhpCa2asoZt9D_YFET5PkTg9xJJiO_Ah43Y260QGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQojFrGNmPpdaSRF_bV9gZ2e7MZHIz_9IcW8VUVcOzSuhKGMNmVXSa0-VDYeA0wtoGhfXLXZa4azfBZZ65wCkqvBurCAZzcWQMf3hlrSg2NOXRpXYgsqb6OqRhB9oqCPOy1k3QXh-hed98B5kUx5uXL0F8j5LOHmJU5xreJ0JBnRR0JY6RyJrFVf_VC7IHF8Ih_CJ10UwYU-nGnRNV29ECFNBNkoW-jxNzgNX8-Hr1fhLGAHmUxWJvJkSsU8JNTmkCzndQoY_S6PSRJqScWd9w1lYcXCnRJiccVCU6xpjXendz2bXg-ZU905wcGAdVwp32Dz3ZuQQnOBH-Vlkqsw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXjcdHG-rzEZFJRSUgp7nBxXZtHheq7ZoCN9GZ-ICQosUcqIXhum98QUGavHp6nTO9sVE_o4SzE6FZhx5zloFIcN2KEhRHGTDru4WAyy7mP2OVOXOfGzQY4xdAmkYeNg08ipmJkYqJxc0z04kEmKZOMMEh3KLP_u7qBP_s5kNAAtdA_z5tNArgRBM2DupBSn5BCKVk34wvDJWjCUfebAjXbYjY5ry-jKokZGrOKMfcOeLLgn259XmTTlN3Hu2V1HwXYfTvxyQIxgQxuT585LUyH-xzAKDFF08pi6w3saeEkKC-WQa-qfSurPWiwqNzklzhK_CDdd26GvNjcOHDAxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG3HQQv17_K_kdeuE6adN8FlMQJoq56FdhPMOk0JlJEkEP-rBYg6Q7wvNKKDSJ1p-D1cXmQPThTXf3jX3mQBtCCBX6eahgI1ShGCucHoQqBlYVYJY0HPWDEjSszD6YJoh0yr4HAhSjZ13MlFvhct8Ujvt4z-ZQDdjYRoWg0MazIYdmcv6uI2sNxp1wgxqxp78Lgrv9EPtdvYUF9DdfK3stFjhHkwUSXWeKU3_f8cTACwNP4gEPKjoFrEJkNfBKvg-pK-hdCFGqnz0eiTYARNzWutmzoF2_G1ogM1ZSiI3jO5kLb0L8tQ3wdc4V9zbS5uwWgVNVJmsDepFtZqpqLgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggekU4TF-b5gveGes4H5ylFQd-w0aV1b1Hcdkk8f506Nm6OlECIQYc9A2Pazl87g1RDSVd6wMDxbbslXz8PUa28fHKML-bNaRJtYBo_ywzVsxlYz3yb5Xa2ebQfwD9q4l_GdJwkayCF_vcUTnNMA66nF0GsN6MMtRP_dNUq19iEy2uA6UkuReIp6ZFfbDPnGwNQ0ENCwNFJRnZnspOqj-49haanJBo4sNY1E5G_Ha8x4RKuslibY5N0MgLO2c5Dh8gjRBTMpY7nh9jpGkSQOF6oInrM13Gm02W7GnvysPlQVdr63hvceFX5d6ibK6RBSJYfTn46W3aujsd7flowcbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7qE2aj_kgVqSVtXKbIc2_B0TU1OmvMJcZSMtinOVSTItbRylxLc1YiDlLd99hGyw7wg7XFkoiMk1FQ_W91DiYwjoabCAemBbbk7_tzlDaTDTRGLIyWon8Xn2EA-lt1CRZLgd6ih4vB-AzqBsSKXlSf0OsLg6LBtOngtQf8Z1dvkAr0TOgqSXQPr9ABCEkjNjDCgNjvAimjPQh2sRGMt7-UXCvQfyRcZdvcJtfBPKJKOIVxD3YZoy2eeP-cu5A4Zgj3HwFeMu1nFZ_LEbHJjdE3yaeTEL-CkhK5cIs5AXMkVHzIMnNchxFCDpAiyschXaMPGeDW3uuECUq-BvFzLMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqGNoBcxzY9LHOqoLryGE-BWxsospLpTkwyW16FN0kXSmQWJ1M_FEagwMSjvNiEWAYWa9WeWWFflSYvYHBuDE7Xv0Uik59U60Zc0pXvRlq2-Zic7so2EGx0vLNp-M97B-RxC-o990BiCOF4nT_1zaZzMaIVTUJ2C7XE-qlTseTNhk48DY9GHj3FuGgA7eFw6XmUNj4GGRFjHyshEFEWJDcszDmpkEtwxzmgoVwCXssSwRT2LOevzOuNqOTJKztEt-NdrluINd0iuoR1ODAswnXBQj48WW6fsmdJuMh2IAMFBO3z7FB84diEZuhxgZNtJ-V8iBCzuD7rgjZmLefXNZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kL9x9z_jOYndkDPDXzDeWbJzErjt67bx7TCqVEQs_udLkbbQ3idodasijJiQX_UoHXS3lxuvri4LeWxunUxEXqNy9WYa9UpO0EFX_T1NFHw3NPWQ4Uq3GcMQFRW_F-laxVIoUztY_M9L0Vm93V3xA9OfAhW15j4Jz4Ih_fV6ksOcYMLXbiFIiGjfnhMKJY7THsCM1dYn4WRaW2vriu0SmJRYubqr3bsjt3S8l11TC20OtVF-gEHgZfjK3L25BdlsTr-EYIfjVfW3QkPZiDlZ2x6V9Y-79czLRkEHqfzzSGp5fof8yLxe_7pKLNa0koAV1sM7i6XtooantDay4Ku8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfO1UT8CCyp90O8HkmlEBgt3FC3MUUwFMNhRc2yH-eVozn72bGGcckUU51-UOZuTKySXVuXn1drLJXgoKyNvPHGG1t-dXBTDIcjea1lveRlIMwpT3gq48d1c-6bJPJDopMXuOK8d_lJk6qcpfD2ZcLC1Xt731qbIc7ZPV5EDhIp4lgOXr2BnNAnjo6ACfOegXPkjLSClJ6XA2rxQSm78fmlgLw_TMhDnwcaQuA6ernEhOPBkzxr8OTnU_ADp2YDvbjRIaMaOdbeAla9qdWQWqbwUb4hvn2hUVeiUWgJQseSgLMWJC6M7EOH_F3BBPx-Slsu-0BxiXDPXQ1nUPGyGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gALZLlCc869KPwMuff0kDKGEr434EhwbeG9Mq3rOzwaVnHGLdcpbzOwUnUJ6ybuTq-HzrgUhbaz397MRoy9462IT9zUmN1otqn9nUNshSRA-N6AYGHM__P7Nq9fwm19YL6AL3UBMBY1JrbbmQjfsc5iU6D0w-iUmhzVA4bwbATGToqMeQJO37CyNthuhRs36-k5k4hE4roUMzomc2mzEzOjyXbzylFB_LLcQRFzzcmyVkljq_TT5rTSeSVAmy5-zDaf8PktBUrqhhvZlf8HpDriK5s3arEAFiKxketJRrKw2L5O4IufMMqAEtuTYKLpv4XR1Hk01BuLDWKpe79M4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_uTJ4gEQTVsnerKFPzWYsMYVpVJX_jyy0v9tbkAFU3l23HgK7bSFJJIQdfgK1BF7QRpDPB3T44b8WlHtE3mmQW_NdtUdV0G0DD9XMwLWuTzShl13FXiXKbC1Fm8kgiLla9vGQFqt8343Z6ypuudbiG7JHJw5k2XPL-hEzJBfrrhuQxkUeP2jUSuCOSkUhgOhZf1aGSmVj8C3hgdtWpPh83mYumucq27UvoIpSE7do318IYxngjjUiaXj6lhMs7uHHGiHtKDE6j3rkP7B7NgG0AlZRq8oGGn1tM0sMPfl0NJ7Y4N2XNOf3e4KM5BqRKf2x4jGsLFcOOZxl96E1Mepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzlUKNOFRcAuv4UCBcxcqEnsfHjXagbUaSzQr9tFRG_dx4BqfiHIc5Oh2jUv2FvfDuOPTwO5JY7K4xsDpKHkABMuREfwKAK_OHhNRYQImVlq0CcWsh9utT3TGSGNWeABFf8PJokZIXuuIpKbaHs-_Nmm5aFYWQIxuJB7PH90I_OOFyXARuCdlY9c_Xqa1weKoIgh9UqgrQtLlIH_5A8JVZAJoQafTzQdacqfCBz8SwdV9Uo2A8xpnMvMvYozU9RXrNkHqyrXa5y1gCWW3DQoDderAZgMuZVjaOtEneSKM23WleV9dxf8lm0IAj5I3enMcL_kkLBbT_8u0oxmSfo6Sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZG02m_JzjETtvYtjARALqxFADv7E5qxtBlY_QKnddNCwOkh9tHo6QfZ0fPsH3tVwStKdCe_MuvK-JoQv5j3p-DMpRYKhw9oRLoC2892wA3u5R4xtw90cltCJo0J12p6ubBy4jYYdsALJde0_HQqj_XFWLR1Czl-wbcjecaEDMMzz4_MhM2SivqTV1BKRBTGKfm7MDB0Y356uYLA0mFK0ErzvRa0gNLX9EzXMjcfNO3c5UKStqrxDsPyggKWT9uSMayr8TaWF8UmyQaTIpdBTMT7mICJq_9sP-6GEbU0MmlU3s4_FPPYtNbMqLGrArK5aWBI-Z_GYlb_pEYECnKzCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leozlVhcWW7pnKQ9yZyRXKIZcq3V71t0QY-lpZPf591wLk-6WdO0tiouWZiMPDr9GM4U-3clMJqDvn_Si38ILmxCVDUfYOCQ9tqkhOwLJvVzbVD2HPrlqsUIxyKM7_rNv5nZs2HVlZFarugnrATf4TCp6CqwaKDfw730UWQkS_KUpdDK06fUte4ROgGs8Cg7OEonAbtP9v4VZrqiec26YzojkKqdiWRIfX2g0LjupG6gJzCjmQCnfmSm15GrvmmuRDJaTu3hwpuH2HpDk-YwSCBdS66_e-y00edGJZecjnlqkjH3VuKR7JZS5CYbPFHwQ5nxi7bF-4Kf-ij4z1F_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njuY_fVxe-OHVsGB_9Y7UCvG6S3L2ZAEISArhDQRnUAe-4cI0nOaHHLnhLArkmiVIm0Hhm6XEItm9yo0OH4i6awBwuZG1gVDufNAhENSCX2TioXA58fApoUk-h2XkxGkxrUY1uKaZarPqDE8JtLAUsoICiBHRaznvhc5X44Ii71UCcs8d41OUk4-UTqJoIa_erBW2MLJAkyjExBngwPs2FNDn0PQl1RFhpG5JibMmjOeRc-DCgRx7tgSMNh9GwM77-kh7-HmKurRJxMvEz9VDr9lzvTY-1x4pfoanPX32y09WyKl4kmKTTV9HvMRdgSrkCinn9fxfGCsNMnlxWoGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_pY0WVhEXGwqICFL_BM88cR3M-sXQ1vcsoNFbZsdzzqp-wZQJ4bPW5wYAqkGHt2cqV71ogj126-hacqHURs2asuPAawTR9htkZ_tOPI7DqnD0615Iu9QPM3r0jO4nJHq0dm8KHGAG8_FpeyY6HKIixc8QuUbP1f44rgQyB06tDOJ5XNXuXPojZwD--cq69MhFj9xOlJ-Na3ckyRo8LIniH8frl5noN1DKhKJjc5R59BR3tYQxxrYeNAk9NCnN_MuCvyXCNzhNYWaKv8qCtZCvXXaBwXyTYOBCZa1ui1IFWiZwh0cO1XX4Ft89VTzU6jzfpzt3O4ZMaN2lvis4w6Pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fge6vCqM5q-X0aYXj12uc9dE2RXci9ZTupYaj1n71JLBM2aikcCTDa4OXY0KDYBtcgeqbyi2odSaVOiZa9pxRlFoStmSsjZSTRM8PCI1-ClwPWdpbNn_Bx7QNC-Fdkbp163RtKuTl5pQaftBf7cWH8bEskDGxdxjqcfg14jJOmvYlh9w3JTp4r2I52edBgo3_tzPHdaovbHLdklZBGWCEHxvduqFnU0W7iU0JCsUhBDm6ORJo3tPXndoiBtmjLNEY9mtIiHODMLU0oWLauFJl2QttHqEo5ByczWSi4MEm0MALUTwDQiFgJmk-C1J3xnzbMcDuPJR16Hcq9EDQXTALw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAPBr_DpVbDXUB4iJJ6d0Ikp2UNTV2kLK1UN2XutZcb-Ta3s5Dz5e-Dc9NO7y7uKXPgScGyCoCSRqGvh_r3K50Uv-7lpMPfvnBnzQyEwgCkw3kAlXpNR3hRkpuW-O0510u6M19QxAYjIDvC3PyGZwam-i215nhhtcV-5jBgLOv1U75AaMI1uon-EZipbU19xP7cUJtKCE6DcZym72C3sUY0_IkRwyD9dZw-rgmzykwOkVOrFY_W7Ad1ZvXxCM1l79HX24chvaDo4p53QAwewrCudyOIrn5PhKcr9vsvd-aCMy29-7eDqusFq55wv_ErcrOSQSAOGxC9j170CdE8qcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=MNAlmCcsmOrvLXweWFtKie_3QF8gOm41dNGQ0m2xRj3hTfKmNCIiyYR7hpJYxzcIvewUs5buMgdiJ7ygMDoz0d0iC3_CLyuzRemZkuSQLv4q-l5hfnDjElky1NGLYTJVfv3DRU7lnDz49wIGK4jZheXD8EOiNEQ-zqDLEp6x6vC8OOalJhwEGfVesGaHZgOMvpMyhA1u_an9_pM2wRmsL7ga__lAp_iq6Z0o9XHLDMHqRW6SZ7hLe0cq7s92Zps27F_gNSsrmqYkUN_g6_dOFKcg-JyJBarkt1YwOoSNA0DE5RU8NzgZ1OS89T8J3gKsSZloSZkTnW3duFRG0Ai0hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=MNAlmCcsmOrvLXweWFtKie_3QF8gOm41dNGQ0m2xRj3hTfKmNCIiyYR7hpJYxzcIvewUs5buMgdiJ7ygMDoz0d0iC3_CLyuzRemZkuSQLv4q-l5hfnDjElky1NGLYTJVfv3DRU7lnDz49wIGK4jZheXD8EOiNEQ-zqDLEp6x6vC8OOalJhwEGfVesGaHZgOMvpMyhA1u_an9_pM2wRmsL7ga__lAp_iq6Z0o9XHLDMHqRW6SZ7hLe0cq7s92Zps27F_gNSsrmqYkUN_g6_dOFKcg-JyJBarkt1YwOoSNA0DE5RU8NzgZ1OS89T8J3gKsSZloSZkTnW3duFRG0Ai0hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOslOnTNEQpBioyn4e0DGFfGdfNbPjYO5jVkgw6U9ysg5tUCJU91j0SuvQKf7yKnjnaXwO0yQjS29R6afP_IEVdOzxNtCd4jQ5lKNcNEzB0K3TcFKbuH3tp9yl8ociUlmhOTmCF91aRb2Yt2-WSfPJAtA0mnm0WGAPJNvOan0JG3P5dXf_lcmDOUjX8eZYWuFR_D6BxqDYMKotAPIhQ6sSF7W0bTYDfDu3SAKTHRE_yvzYvvUGjDy0WFVpruiTVpSN2Zqs_JXGiang4wgm6I1jFKAfHw7Yl2BUDApZPgFFIQBE_155ymcA39GVbcOiarNcvldDVsUFBqVQ2XOUdb6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU2OzCZiaN-U0sj96yPmqdcRKmXRisXd7ibZJAGoc-ZLxtlObGFSlDTeSgZW-3gjXpuU2wpHDUvW_Ug4W42f_sy8saJfO7V-CcxpfsfdCVO_a67PRc7OXLBxxa0lkO8l4qxCJ8zmIFm8oPGfqJwAFOrN5PNBcT13ehE6MRGTjHFkNkR6aNgnDgv-l7goCt6wKju0QjWPJ3BA7ti3yM6JRuxy-9aoyMh532I_7DRrr2IljwpqNsRIRxA-0VONU3_W9kTGy-QL4Nhdgvx60kQAYopsOt2hL0vayKIJZsKqvJ8UNnYPCaOyqd0QbsK-PwmyYYEGjAOk50IKtpJsP9fxCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX0qNGY9n7KokYJZ6_ZBIFj7OljVftNLjhIs3SCiZfT_JoTolOHAxOa92LonLjq5_4bKPBx1h1NTsmiCkrplAV77BX_w3I5aTpzdQ7GdZisf8uuKtIG7BeCvrrx-koXz3NuRUTc4LVci8fnESyvPYP-t3oO6KryTEsYmgq6b72hdWqSQburYA1aui3nnR2OQ0jHqaJyyASssSkY30LTA31YBoMfnaufhWaiJO8_QbZYN108L6Ep8NcWY2A3y3IZZHUOSpYUKv4DsTl0gcjofAcqJKFgx6FiLy8dJIIVxl_Z5SqdlZAt_YIsbnuwh1o2vYty2AQPX9IFHkmtpjUEpeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2P_Sd1veEE5D46v0yO1-gWjB0jjWYZfRTFUZAQkoojPfCeAdpsbF8h4w6Bw9w2q5e1ALr6WFVkxezQq0qkiCFh3DaS9asVbALBpbBd3U6QCmCGNMVz_YVNV3-1jto0L381-LaYmV1EZRiHpa65VofzFhyWr-Vyibk7Puq3aRFNNZPMxh_CKmp15QStOMN73D-4hWLQKfn5IJAYw9JBV_7zVcyUQcR3nDEaTPOooo4mkM3evp657aXweDMSpgV9NiJ03IUEIAWLYBrtz30QMWnDZjjLqNYil3mobqzsOE7QymVQqfz0IKQrtTmobIaOSoFvzUw4hxhzYaXe6uZkqJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4fbLS7dzz2D1qA_axsXmLRcGACgVY-tC-wFyu0XsdlQtsSdutmzbeUnjvdySGJEAYMr5RzMy8tx6HO_3Lr9jqjJb1eJ3_eTiVZtvPkEpexu5u_MFA1-8JApD4Ns-6rv6Vl3CXNzJZmOnbv2BkMC2Hy9ZMQKVFAdK3PFq__Zh85ICEZXKpK6xaOhW8BDo9B9SUKwlpTJfhYBOTG5sQQR6iy7W0Tmla-Hj5OjPc_-a_tOsiWlw5WVKV11WjL_gKE0feQPQH-uX2H5o3K95iMNrFieol_ftV3vm1-JYa40_EYzvJxOsXrGBRW4ai7yK_OaPABgkQRKxqFfmHcLyZ-R2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL7cMjKFR84rogREyz7UWw2WWox3-XD-ts4wThJV_AMagv3I4APupUiYQl3_Z-bRx9HD3mmvMbVDV9W1dbDyqaNckWXuXmhbgFWriKNw7UxmDewXN6LubiBUbPirxOxRBC0aEBf7gOa_jnDr2vAwlyhPRfc8jWp08uUCAoe0MfSALcTrn9klhPy89H1bkQQUHm8OPx8BH7YMHegiNyC-EFRa7MQ72prQuJitH7HphBI8FT_86TbrQZMjzvBDEDEwNOFBnKquUpgUlzlLOnYr1F35xgPf9lLM8vlR4CvCvz-Jzse_EG1nb0zMs-OdZfcRTWut1cvEWxUPqkgfKuOrsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsbqP3xAd3TB5Y1cxruMuocontSiNNPkcnDIaPyv1hU4duov_twoHY36unx-b7JUfyHxOQ710xdIQLI14ptKqI2jnWm0CQnl_FyNBcRLAFT53BS2pHpvJjHHWNIOFAnY6lpOkgDbZICeTcx4BWKV_V8zi88OTHN_EMaESRyrcUqAx9D4jbdMPqgCOWCJUBxdsu3AxLgvWklplKWV6rCQZCY-rX_PMlrxviAWwkG-honZKxELwGnfkOmfASTahcbYOlRymbaZyHkNsvRVaO8_-udoPWAAJlBIvoyl86mOhEr8_MxY985qAyWDPWq9ArrHxLI4iuZQb7bilYJVAM0NXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kaxp9ueyb7e7Xnv_grRkWw7Eu9aSKHC5BgmdL3vgCWNAFrzOClyWBniLxnYlqWD13Zgt24NFoSx8DFvI4dSmTcwsSKkPrqsDp-tq0JmNVGc6myDjN8LpkVLi_PQtYkhYahq8YBu3M11AJKNQuIUCrkwNN8xO1snlafuDW3iq8iX16OBl489UqhoRM3smD8yKsKFFJdZ-ruCz5ZaFp_LtSSV2LmXtCyVng64VICM3c9FSyi7-1ygNW8s417lj265udhXzL23Qy9q7TN-N9NaaVQjNj4K-OVPB55OROBDRWpWVQztiGymBbs0trSEfpFlmn7v4t73KTPFEMM9SbCdujw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGZMvCovN2OetTIwXg6Law7ye9leS53KL5dJO-afTxDK49uEag6DLLpha5a0E75uA2NAkLELMg5PL51hxWkNEpYJV4mdHtNrg9S_b1Q3CNRbEbnYpm4UVr4q_SuAslZO0rnlcK0g1IkjDYdUTnysIoapb_7xYBe82rW6rmC6nCtrIFoX392Tr_xwagbccnkm98xLE7JkDKwqUOjNzpMeJ7-8gWhHY-Tn7pL-h29sWuJXThYFWFlRhV-fw0pGy4eN7XES8OHTrKsjPONFuk0rSVWqI8ZPr41ruB6_MLQTSAyH67zRikYo4PhcwdxHHS-S0iB0SNghVUbaH7eFRGhAJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h57bsLfQ4tbKT03uOzZpQjY8zcFee0N0dtszYERR3R6V-jllxSDM9glxkQ-otkdx0rEudvlBRB4inliiLIbxz2FdHoVPaaU5UWPXEUvrwl1KBaE1PfsqsDdxuIc8JCEuXrYavyGwEq_2uctjEBE7KpbKz7z8_2LqeNLW9WQfBL7XQ9VzXA5kApC42mAexRewtc9QTOC2Uzs_YK5LP2KaimWHGyXFnjWSdwlaFj15LFgtW0GL2qktw1vmmiemaZgzPA-TtVmGAEogPg-OllAp0BnLTRpv2zDPq1YhWqEksGYzwMPu9CRYYnD61CFSJ2mjnCn5IccesN2uwhWkLenCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQUYah8Qi_okXHbfo-hrSHquuHNyP3_AZhc7Wt6EFFMEIQ_uZcvMmgHrfYAMkJwbHZUdpg5K-dKH09aAQVigLoSudOhbtbtPQ_h9PEx1Ex9xUA_9uDDFsGuGkqNWcdS49O-JBXHQtRbglljw1kf05J1UMg9cR_OFgt6FSStoMveUHxDO63FUiCzpt1l2_HDrjvxLh3tbf0hY89mhX4deaQ6RE4GnLhWRH4qZVHjR1qaB1ydjxaFYBZFC---CERU-ZnE3foxQKLmZLGDazmEItbU_-hXHfCLlQtQhyjAWLlOqNYUBlwbfbLuPowhmkODmA4M9pY81sdS972g5y9lEtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/su7JVgjKv8j8x3gymxc-LcqS-fT1MQEDUf6FlNIf40tfzvZCczHD96Xr_KC7qgFW8Op8ynIDH9Ti5GZg-sn8L14VpiXYb-GCfLGf21ozA0CPSVt6HwnQVOqY9GHLT-bjCPVUxk6Uh-woh3sPj1QgzhSHZLhwZAwCa68bHM5AYceaL-0VAqPl6P4OefiJXe4LvuZjNVtd4KmXiySa60tRtaDbCsNMjY1JFi1-0QJcaCOpJFsYQLR2KnTL-hRDSm66PnBevWRRxjKoXhWGAYpgs5SQ_o-6YPWBN8dKUIMFH3TJocfALJcdyRVi_xFLXCJFCrve_5ojH5sZtDQ4kYiPWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNHJVJnMRHj803bYOSAIiOec-Yb2AvKdXIRleZm_X9jdeiijoz_GRVwhPu4Pu6TI-S_tZWS8_qupO7il6w5ddATD3nOGmQ57eVgcrtfnyx330C6sp2a374A6fCVX2BYfLkbRyHSdC_OCJbBoIA2ymT5DUR3WDPxVoGNDvkO5zSsMFMk56t5HhJvVYVab4dCJnsypAey4nJU_9GP9oJjW0U77C81ly9gSFPtwc6IoyQ7kMBIl1nE3fB59BeNeKkN8dXUyAZaTKh6FRrNQbHGtDQbo6fyRje84iNZp1JHhf_6v-XhG0Wbic5IUO2Em097m0ouaM6xoLUedgGvoaZccFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1HFoElRU3udv2vgDexw2Em7GIHo3AdW0r4e1Gx7o__8_iTZ7vDwOpe5PPrJxydqP4-npSTpK8dSi5OHUcRMSGaNNatStCv-BjYX-BiakVRdIBYCxtRgTozTM2ekEkOxwWyauE7FsGcRSzsm4eFHK7_MBdIPnkF19Fa1OrNPfrFLTeeg8lD9mnMKN8J2GHIuIAK8arQq2kcvhLqoBHs4pOf7qRoFZpmsb7ehODIPgOKU9lAUJ1SKs8QsoFThcuR-wGHPuxUgfUg5Tb6nPlIcD7Q3Fw4LbZKIl1BkDwxFc2WWqjwzyj1PKlM9nxnC2wuf4PlUKbECaT2CA9xjZOpFUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXBxRnoga5OEnkQxazRYsrf-b3FU9Ztto7HOkAfq7t7sAesmj5lrI1FZgW_IIUNCTsBAapRt6JZRdraLo6D0sD7yQ2AmQcwi1ZtJ-jjCE8it6fDfWNO6khP6Cc_WtHa4vMH3hFmWg3bxnuu8SqpewGSXkwUDTsO9yVoImqv500G3Dt38pkcMc1JRfnkvCA5F6d3ZAOQxpRI7_h27iYXTgxiTm1NWYhSo16yt7T7Ylj6R4JsrZLB-DmSXMklIhxw-mu0RtzCuskRX5Jeh9-Wb2fA8zkeTfKGpTHSjts_cZ5_6Vi7g4D1T4_s5a9t0INFxfH3IVJ3Drpn_7u7h1vZq0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0djKryb0eTiW3PjQ1o_jwTm56UpcQSW-j4F26daUHEsWwOQOAYA_btsCPMJaM_Y-uF5ZJzpGVo5GN_PLs_qSsgxefO_236CnwYz8cn9kzRlqtZ-YmREM02QcBBEoWVUx-IGqrRsb-QmuJUOqtBwo_VJZPAs2r5zJR4KSN-rjZS5Z8qo7lzv6BkBJWt8__qyBMWuHgk9Ktqp8LWu5AI8TZ2it4HQE_FK-fWtl6B5gXO9Kt-5YXcPsoPYMvhcOs6IbAYBRH3QXJnytQ6ORbDRBCd2mNtY2aCt-qqgGLiJgKn0w9kApOn3oa_6pY__37B5ce4RMjyptai9r5ZTBLpY0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBs9Xt21hv86nEM1URghA0zAMQCcIJs2L1oITeVQR_WdWfT-7hTOfmXMVNv7xFW5KMNWCfNy4505L39uBe7r3M7FnN9vOyafKTLqIG-_JLLwKQYzHi7vFtMtXKsjhEY-YlA4VKadEY4_DxTTM7RfwsRwHcIUGlYr2CG1F20bLeB2y3RmBbG2tc8DTpXsi2yapjfyBLe0dUEXpCNeKUOMYeRQ-HPTrUw-feGogSh1dpWiny3Sr17qTepuMEk8vD0-q3ccBPcETu6Jw78SURMJAnsxlLgab1V_MRX0mbzF4p1OO_pWZVUUZEkSoRj5mP9Y2R7Ibtk9G0lQs-P_ACPZPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT33VDBuo9if1mO7J0uQeRMXnXbK-7HOup72iHSthnsjbmmt2HmZF0SU86VT3ry9X4bc2245k2og04EYvrq4iRng3PSZ8AHaBdil8hq2pCov07CiRawTTRkLFb2Q6wRIkSQeX2p6cxs33g56ksp_JDTIrag0km81jOmzQfCo41p4Of406TS4SOkOpGiU6gSM8XRjqYVDK5oUoGcWg7xFOV5jboileyVHWSM5wmZlI6oFgc1ncyXvsj1AHnUrVqCoJJhEQuXufIl-QgkeYHHQzFTP7YiNlLp39dp2pKChyBNo5idnTjXzvkgeuRYX655S5D_XMIY90g_ajfzeayngpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dtyus_RoTSJ65b6-tzimaytf0FTfsavlN4mS8FhfyWC7QZnWxUwLuGZl-WeSiUr9gvKC4sooObwu8AiJ2jG7eFmyDnmJVdPl69TlcCxKY3E230AojvkljezcfwKKA0r46gS5GhzEritxU34tNdKZaTExO8FmJ65wI1roaJVoxU-0mnAZYqcUEzmYmilaJ1pHcTm6fsiFSQtM9oTMSRCk8rFk7LV0leG4_fEr_ysDfOOUjwmNTJJNmm9onZvJF-FySe4Qum17_jzgcO8zPXxMoToNTGunGQB7GH0y65NBgMSgPUVSyBaEaSkEQExlC4z-OE8W_1yYv5pf9AnkQeoOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKIQNwrJlpkX4CTRdJAJ8iHaD5OXraWzJMeU5uIycUhtSeEVebMrfhoeT2Pysvv9F2c9AgrnDH2u9kW3TDv-BtDF-kkw9vJn6rr8CPM1bJUAdxi4bNmW1s_f3pfQrQz8zEw28YVStUl3kDvToW15NVe6Pgy1aTzlCl5kU6m1oV4rreD-o1cEGnvkmGvh9z8TH59Y53xnv1FT56JqaIMI7VQlSsb_wHCilH6KaECXZZ_43vpdeRgWhzCFRUhVZ4WwksMa00_SozmNoBlvZccYVZy_DvnOdJkNkkqMzLDIJu2_PrHMOEtevNhVG6KXgS78MGnem5f1FmDxvhzae6fgGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3ojUIFnaX93RGQBOImdpsuRjnuNs7wT_UkR5BHS3kmx3Hghn7MxQcg2bz50kZMKw33Ai8zOhiWLB5n7W-ehC9S8yS2HnVvEg2bQQUfwvRlOnaKbyQ4XSazXCupxNRwz6e3M_NqyYS8qxgTYUitSlKN19ELPoaBYQZlF01AdgAzYL5x76pAmHQ348L4NsubDW5C0euzdN4HO0FeBo_89Z48KZLHgy43e-E5lXKq94S2JEXcysHx1K515YKT_D7Us8d07N3o1z-kvqgMzM98wWwBA2ioJFTV0pd9f5TYXN-8iT4aB8ssdigBOmcNC6-kEWghArkcWIoQjRIruBl8S_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=NqdCJjIPz1zuhOGdEzLt9AsHIctdyUWTIQd7a8rnUG485NWSKXdflfwoe-SVhAm3tPwIxai6yPaDZJMzzj4O23RRDHLrztjzWy-Vq7xPRRSqO2sy1wT6yzfxevzBWCpXrsclNdOYREau1nS4fKVgOjttnxUiciWPOFVvzAANVCZkqawSs82C_TDaiR_fOpBoVNaa6RYngzQDjZoG3AkAWgfpniNkSB1GxX74Y2Q7-1-1dy-K8PE2k7xMOYKbDBuXVkYaMzuXgXCrZkcZDb-xsisi-P-pDGkV2rhH-mV7Nv36gQR0M2UsUnefS6WQ6cLInH-q2MMadFqj49emhnqOiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=NqdCJjIPz1zuhOGdEzLt9AsHIctdyUWTIQd7a8rnUG485NWSKXdflfwoe-SVhAm3tPwIxai6yPaDZJMzzj4O23RRDHLrztjzWy-Vq7xPRRSqO2sy1wT6yzfxevzBWCpXrsclNdOYREau1nS4fKVgOjttnxUiciWPOFVvzAANVCZkqawSs82C_TDaiR_fOpBoVNaa6RYngzQDjZoG3AkAWgfpniNkSB1GxX74Y2Q7-1-1dy-K8PE2k7xMOYKbDBuXVkYaMzuXgXCrZkcZDb-xsisi-P-pDGkV2rhH-mV7Nv36gQR0M2UsUnefS6WQ6cLInH-q2MMadFqj49emhnqOiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5C2SNuuDpUpj7T3MpWT9hwBH2x0PaZUPx4vzi8GvJ7mQKkvzh1InFGdItBC1S1GvJ9rGuHSciQTX2Z94UUOOPJ7QhftxVn7In1efOcRicDxZq6M3C_45uQ9TXayZKvBfTqgJiSnUbWmiwQIfXNOZijECLws1CsSxXvMYAgtMT7woqQsU07ubYegGmlqtIrR255CazChXS8SxBlmLj00PogwIIZIRrqp5jvU7emis-V6lUVpj7XgVnypaAjYg70qst6joB_pkYR3_COT7NoMpAJUnRyZnIiKvnQweTpkXwSo1NNbyWzsv1ahQLWtYeupVA4PipR34014GTXIp5Gn4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2quIUYWOlxc4gJC63HKHWp52veBEknagyvj6bZePb38jkhzmnDSDpCUjp6fvCAiv3wOaU6zswh45TerqvEwOjlKwKmriWx-MqFPNfziSsRdoVfVrMEuo0KU-5VAQcfgObXaWxOTQWd9Fb-72O8GoDg28I2tlSjQh7Ml8B4ClUsHYebXOaWNhJBiEE715ovJ4cHEYLKB7sKPG8v8-V2VNDnWs6rruT9WEZbirjGC4y0d_Klp6LtuMx4qXQEcyrlxVH36GQrRWggHa0ejGWGdelMwH-c36LU8XyvarC0VHa7YsZkBcz0L8VNGu41FqzNtWSmAIhFkSMyC_DPLCBtBOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUQSaJGKhGM8mTHrEyJLGop5HojVtJ2etSeubk3hJeaUFuyR1tIKeOIJavZkNWIYuZQvx8zPAP40uYl97esmFfhzoSqfpzHGja9gDyEKZGKy9EB2h5SHlsw1Dg1Oy-Vy-u6EAP_0u7vijm6fZj1hrEkmICWSpKFpiGzyQjvu3aOH8GYO-N45ldfVJPaSh765dbkp5fd2eIoRCzG0oa8-jCJ_yT6DNmTHBatMQRbcsf1c0ltKuz3bTYfshyXTXJ8X4vlIz8HSXOAfjsuu7IquMBnmisIcJ_cvWrj6pUksWZl3TNZfoClYfIney9S5hMlaEwhyB8KokTO11z6jEVQLJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=p6B35exYWEP3cK9zJgNY-BqHFvmcjb7hZkq7qKifVCCoQ7YODShtW2od90PbvPT75O_A1ryDT69RdIyiZ7Ek1sMx2XzQf1kisM2FHtZC6rzArIsmvzCM64B62S-U3_rZMB810c_JhfVXjKSOntLq7YW92LFKrrFyKARGnWVGknqWPnRXM0f-3KIjMk7bmXUpKSXbSCiifihP5Fqtp8NcTKeTuaRfM-IP3WXkm7yu_giRBCpqW07c8LadLYJ-7kQzcQM5lnIy76bZYR2eBZsRusnbTR8EwZqLwElWtsL7zkeWGr_opcV4Yo6kouww9fk_VIwws2xbWlaEzP483FwqAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=p6B35exYWEP3cK9zJgNY-BqHFvmcjb7hZkq7qKifVCCoQ7YODShtW2od90PbvPT75O_A1ryDT69RdIyiZ7Ek1sMx2XzQf1kisM2FHtZC6rzArIsmvzCM64B62S-U3_rZMB810c_JhfVXjKSOntLq7YW92LFKrrFyKARGnWVGknqWPnRXM0f-3KIjMk7bmXUpKSXbSCiifihP5Fqtp8NcTKeTuaRfM-IP3WXkm7yu_giRBCpqW07c8LadLYJ-7kQzcQM5lnIy76bZYR2eBZsRusnbTR8EwZqLwElWtsL7zkeWGr_opcV4Yo6kouww9fk_VIwws2xbWlaEzP483FwqAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD_lsM8UnPVHkLRum0iPl2UehgsRNPMqa9WJ8vCup9ITh5PFYukr9EYtYbMw5omDQEE77AqOevsQFYz79yRpKT62pGgy55beY78uWhFsLGoZKwRiMbK_Y2lgLnXOL2TOOjwsnKLi0rbvtqAfVIzC2bArZTshT6v8i2ibQDxclVf16oAPe0O_QceZHsbtRT9sroIAtJL5WiomrnZaskxuF-JCGkejy2zN-Kt-ugqtzkA1-DNOFLanpI1xxhSewTRs2B086hTocafwWhUK_1AHnNWjJtxdErG0ZeNhNnUl8WU0ClyQuaj0q27V47ptbRu4NQ76f1fQupvvpcRarT1pVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cea0sifTt_vWNVUwSkNSY3MSiL7j6c61XXCWEN8TCyIbZv45L5KpULa7g-oNbehyMaObynxIlk00oRc3WYoJbTmCgx3RkihBMjwVNr1lI0cuSsD9PksS76tt7k5R62hbZpaDxzuV9chi34Gy2SbrHhLCTBeFoueZ1TTeUIqQWod0VZBU6XXL09oe5UhTCoAqSrOGTerF3IHTndCDyXEgpqX7tHNWdQ3w6r5puYYR00Wa4euElkjxuR2HRAmOkwmBxEe9sw4ZeymfrvEak0cAdfjZPrw_I2iuTDII-W3pQm51aYF6_d-12t3lC1iQ-BZSwzBsL_C_kDTJHQiboLe-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FU9Hvhr4Xf3no7QbmmuEF1uTnV7nAr-ULqGntTM_admpGwaWZJP5XpnbFiUFIHmQcjWuVk-GaO-0SxRJ2rYYEFB0IdhK8xXpAEde227J0fBrh0hOblnpOI7LrhmtwBzsjLfCqi9gZACloA2CWdXr1c4KY4srJVxhndENY907n0C25X8laYGwfReGBzDWK94_eA2KM276wcZ45Uw43dKRuU_0PX7uAPM3RZ6XuSqtulesf0yYDtfcqg8L2_suWDVimDscknzayZslfXrrhh8juBFcJCbuo9grll7EMRdSSS02QbS2DuMWY9imn4mLFceuiZXjZI1r1pftn6Rpwxb6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJrsbe05bshpJ-pw84vuBonO2hMPO6M0u3FwzhyCTplg6LY-ihWjSYQFaiYm1_sTNnqvy3rzUZrCR2i0uJiYKjYWUWcdDn11CP56rTMORsOS-Pcj4YvRxL1pd_3xU1cLzrbr94OyyTO4jSCcaWUGxQpTncWX0s2RQv1gDuQ1Q3BWv0FYWaJ7co0glnjsdatiV-e8hyv9w60aZ7M--fh7cQz_WlGvFfMG55SKftrGhDrOTNX6Yoc0F-YvvdVvmpbzg9jRuQgz7AYD4eANuUdOwZ1nUMv9K71ByAwC8QJN5FshuJw8_sicBWHsmvqV1-c6aw1xB63n-CQQB1lA9-cJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OohwC4cr3yAxBLIWCS2s_mEF4LUHWTMl2YR0NmbLZTju8RuVc0ywpeGGssI45RLEpsdtUijsugxtSwCOLdGuonXVH4kOn6l2y2lrOpkPJJRgkupbcpsEutuiHI76r-flzv7sm87xHwc0iRAIW7fLz2uc7eIbkAZs7AP_HC9Xpwn6ehXWNN0a7SQn6kmMt_rT0JSjE6P4b4ePnoXAO9oGoXSU448armt7Vog3N3B5sup0VG1GB-U2uoVrzwfBelOLi8uNJ58XKH0xj9qJZboSbzUyO9nY34Eyd30rrwb9X8sE8SmVRlUrdU_tbGcAm-hqggCjpYpmPKdNr1y3_3-XqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4gMFIe-HFyPCHaCrGulPMf_IT9ogSKpNbZx5k7dZm_xhUtrk-mNTUEgIEPMwpqbHBe1RY_Fh_6KoV5K6txULDbL3AESK6_KW5pVjzLla14TKn0EjrGThdshH5Ej4bTX1_tMMnP6Yog-45dV6rfCgYl3MoYtKUEhZcTjP91xjgzMBQXaFR45Uw85M2253alZ_ywiRLIwltk1wV0rkabL8FlOPFpiR9R_9P3r9QMbS7sGQD88h1HRpBQKJuTh_tTRVt5INXD3L0ccKGdVuvajnbv-Wqel6fF2ihmtwkEqdHgUY3vmlSS_pffprCuhIV6PJAXyJk6TVkAzgUaAWS86ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDf4zZORD9hQNdYHJzonNov3tm2jCMH55LW05-_HGTQX5muZgztMz5HoIY6Tgxp7baoFA3axYFZMVZvb3l1DRWbbg7vtgIFBxJpe-YM4Eo0GTPIrf-FeSL8QXqCHj_aOGzZF8lx1bqhiLT-hc933SA5cetBpbYskMSIAqZdIitUabz_NlV8Gl9oFMgC9zRErYrbwirAFLab8kxjw7sI82pPowIrKyHhg9JNmeMEOobGOw4BTOHLh9QWr4oL_cIk0ulMVU0gZTBd4_xeiHf80TfwDaSAyap-jE5TPZ1caV_7uCB2ln_Lq5aoPrD1OKEE6S-ffMyMrpekg753M38j2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=cCAcpmdgXqkfqMM6XfAihUHYnobeRMJJr_v7t5YsUjoVdcWKvLb5lAn1cAlJqnXty1SZngltQzYf4omQhB--_Cb5frPKfTlxjHuL22pkRGN4Oix_pzujHaT4qX4QvRFoLHm_ftZ2ziwFjWidq5Isc8OML3JuryMtjsyAmts73EFM05UPJdrIftf-_1erT83GZ7V4BsIsIdgB5q4WsaqchK5qs-XihTHiapQ6r23_0uWtvTGVmt_A8ndP3zKQqyLvYMAOnTEjlAZKqf7xucH3LBtOhPpsB3XFdKiuHHMUe6DEyeBOHFo7rUIqyawZhMj8D782ubk0yE38HkgE9-TbZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=cCAcpmdgXqkfqMM6XfAihUHYnobeRMJJr_v7t5YsUjoVdcWKvLb5lAn1cAlJqnXty1SZngltQzYf4omQhB--_Cb5frPKfTlxjHuL22pkRGN4Oix_pzujHaT4qX4QvRFoLHm_ftZ2ziwFjWidq5Isc8OML3JuryMtjsyAmts73EFM05UPJdrIftf-_1erT83GZ7V4BsIsIdgB5q4WsaqchK5qs-XihTHiapQ6r23_0uWtvTGVmt_A8ndP3zKQqyLvYMAOnTEjlAZKqf7xucH3LBtOhPpsB3XFdKiuHHMUe6DEyeBOHFo7rUIqyawZhMj8D782ubk0yE38HkgE9-TbZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJLnc43QFpGpnV3HIXakij9Tc-UJnH6brdskXM0FYKNOBBCvK6GRTRVXv9xGuTZNdqB-Et4L-2Vgk6PLYEtJhBcZh6LeeSHLCQYeArtayTRz3cyYNESVBfQG_RTWL9eoPA-uIBww9QRtlCKqhzG2Lh8bf8xo_HkGEcxKtTbnRfF85nKpESAJKhvrer3b8EWuikYJgEWZm8ZbwoZBBX5Eh2AvgKvEZvhno9HwPUBHeunpxM1nEXcPQ2j2ta3ZbbZq3jROMrCrxySwRe3ZPW4-crITSHXmFK63Uo1uOEkcG7pG5yKbIBw3UyQNfmrxoggwpit7cPWklgGQTTb7w8QE9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4mL7xXHNFfeDpYrCIJIY6CZ4pSZ5evQ2UxR4E42L9WUf0i7mgSLYU5ciarsnPQVaRWg6sfHzlwXedgoMYhvOIz0_j9ebvRu663hy-X2HN3JY9MXTCLPKK-RB6NLLs1rAi0HfFB9YYyE2o_xCLAGAj0N8g3oiwD_NjcRj2Q_sW9AnxE4Xnv6UWJ5LgBf2B__wXekC804Wr1eV8xxxvP8LH7-MRalVGfDnoJoR_Ld48lXERvgE9kc2X-I8zuKaIFg01RKZZueqlImiTgMBpX-pi7WKDI-xgJz6tyhondYcQd2A75PpKf616Pe2BEZwmrQmL0KuVXpepW_Ls2di7Jlug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIURT0G1g7yku34POd_fc27LdmaOnGJxTpT-eRYCBEUZDb4WQDlThH6ac3t_z25fDboO5yD9tV-IDJnRe2LCZuFK7Nfr3y4Z0fEYJUj1l8iWBL8r0WFtT-tHG4Arhuht9gJFKbneGMnKetkLmryE76chdNvN4Mo6vK4ktJunPi1aI7Kb1w0wMp7pOWbKHWDJ_V0WsE9xHuvVRPaws22pnrcFhIVBmxzwIkUHPKnRdZRVrVA2R-4-idHlv4t2OiyaeAqF94CwCrLn3n0OUR44AHDQQSjK3XYAW5uMEQMEgmJ-Tz7uc04UK0NDqSq0IXObmwWxaPik9iGCrA0nyaV5aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbWBl7OJgvpsUSXQ93onXwheN1tRDdOdb3QlhClciEFHa4vZD7G7AkmDeDSBiukZFfN9nlIMMa-BfC-ED0-XPURF8DfAtc0yLT7WeOTEUP4HWb6HYYGz_itFUp1nnttE-Y99RTYXvxXsykNGrMdOK0U8ajJFODN7jLS2gZ4N3Z-wd3DM67gLSS1H4APLwJztX1kI083D-41-HZGvyiul1yxDJHkirbq76nFtmbMNk88tUC0NKfvbXQltxAKDO9OnUJvny9PEFaGbkcIphyDv49XAfgGk7EUhrSLnHEfDuGGL1wiDnrQnIzzgxSU1gQ_7thinYaDlYFhqDsB_R9fg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXIUvGVL2LpP2NYFo_lgZtr5re41fOGh8UbBLIi1ESZAg0GIWzJdSd6kJ7aI7oJkCY0zaII_gu4Xsnna71sIz2p_chjoj_3Zazyd-TjWDNSDRuZbv89U8b7TiY5siO0tk-OySU_JB7-FqMX2evO1cJk2adHT9VVnAnIiZNconP1yVUYKvWYbrEaTP76Xom2HE5nAO_VPpijE6n9Fyq-ZphyqUJ18Mo81t_Sx7sERO1ydxA3EnxXh5Kf5WjHi4lHEUK1dPX_VS8z1jmMW-6a-v59RAl_E5SPFu6UPIuiKEA5n7rfWvVq0ajim1rQck4I1gChAY-QL8eRZOH-qbxO0SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CixPx8k49B4neBUrZUU9qJt0WZsUl0MAqyhqvqamMGNaqns-x8kW3SpbQE_AtxUX36ii_I-YDMXF_fDltvPYls2a-sGx1ElWFgo0cPrDs9998oIQbbRbWcQa9Bu-D6ZWYvKHyRBpY34Ye-ADgJsHc2dwXswbumHDxn3_Qcw9A4TJLv2OJPc2WMmHSb5mbkJDvv_7QwFOdhEimKeGAhCf-3NrjXnCnYBcbQvvGGmxMS3Hkl55tIa0VUIMoBjnzh_2HrihBi5Z_NX4pbfF4ezxYAMHvNt_WXRrkJ7tvN-3CDKQwauCRIC-aLEfFvVz00xgMiZXCPZ5JN6ap-YDk7XOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6AMeNRyWEpyGYsD76cQH5kS_X7OLSXJ2E0tDYP0c8Rvbcro_TWUPm6nhLA2p4_-W7SJll2PKIUS15EU3L8o2nk5CfPjAUmURvxoP7PNf-3LnCC7th6q3bdBWhUK93-8TiT7tUEsylNazBBdLbOqV_Ms4ZoqTkPDKvJC_NFYNQTHs4bVNwM55om_hYeirvYh6kTIwSXorujK_IHln8vx_YJY6O3h8LIWfYeYYpLfQt2MXCHWtEbYhT9Hq2liipj8YnmD6Pqf4gwDTB5jTZxylaQyJsqq40Gna_l3jvSWySz5u0o-zZEFk0rLo0URKGi56imvbj5IJ1KTddPWzIWwsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cedZST6WydnQAZfiEscbXzf2P2USeD8oCfQ5gmWrpsA-dmVaU3a_6uaE8_jNieOZkDb-k0shEe_NImI3FMExMQh7JyCRr3bkX3C4L3QeWaD_Ks3HPPiFslin7I2dpzPitYh2-k302hV1YedIevOdTNX5kd1nc55aR57ZqOwo36KhMGwcgq2q8c3YckzSqLlfecfaLzQtNkCzCQDaZxa8eeSX0W6ShSv6rhZIg35WJMrI1wEuLJg41SZTXUSWosYwRzP9RUUn8y-iHfQjNSpYZfm95GOLYKC5PdXDQDM1vAM2LHsfMSBGg0r10PGtZugppijhrAdfXt8uyMNjDZTv7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9WY576ym-_Y8GbgJQssi_Yi15QNRxf1nVA9mDFtGiI-_K4-Q9z_5EfkIjVDbrxnU3sLOs1o-0h9P5vikTyAEFzQeqThIwWTb6t94dRXcaSK25EYVlOIxoBRv3uVXxs-35CACT48cT41wc5-OiLZD0F_R-ocP0VvStwetow2wHlTO2mRVyK3vKpJGGg87BIqbUO3nXEDLsG6Ur53uE4VuHIs4jTPEX8TouW_JWEQDLsQt9ApOhgTl-SYc9FruRMJuK45LeCiTgsCO0dKXYpDuH-qp3erNd2vrdFdVEBvuhXAGUwz3DCLE_pW_arCjoSqeR-DEoQRM9lTYjyJp7c95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=Ge9PHqoysJhK5aFgchQnr5eSrAulLZNues-BRdCBh8-iG-uM2ZpSWQwG9_C3ZnGKrYGrg26oEain4pmDwPh7HDbD6-ZOaN4V02ie9FNhS1Xq358ZPWxdSxFNQC54wsNkTeMkKyl2hpeB3WD4qM25KAiXD4q-5UmQDYV1aPlHZqih1P3AQjsXLzjTCdnVZkR2UyH7Fm8taMXIDwjwHPvHbuTo6ECTiVvK4WbBKr8zzKZcLjH4YaqzeCxMcT3YqiwfqSIdSfir0E766c4GCUhf7bEMELmXmLOzV6uJXkwMGIgeBemX_qrPaKvB9aqYuYcS798jm-0PzcH604oUCCr9Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=Ge9PHqoysJhK5aFgchQnr5eSrAulLZNues-BRdCBh8-iG-uM2ZpSWQwG9_C3ZnGKrYGrg26oEain4pmDwPh7HDbD6-ZOaN4V02ie9FNhS1Xq358ZPWxdSxFNQC54wsNkTeMkKyl2hpeB3WD4qM25KAiXD4q-5UmQDYV1aPlHZqih1P3AQjsXLzjTCdnVZkR2UyH7Fm8taMXIDwjwHPvHbuTo6ECTiVvK4WbBKr8zzKZcLjH4YaqzeCxMcT3YqiwfqSIdSfir0E766c4GCUhf7bEMELmXmLOzV6uJXkwMGIgeBemX_qrPaKvB9aqYuYcS798jm-0PzcH604oUCCr9Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbTs53l8kqjRnwHykUS7K9mJKPcROLPFh8g7eFkk0vlNV5mG_q4LSdIXCzXDBHwJLaDaQYgUONWWXKZaTwkcu6jCaVQi0n1Qxpf48I0i47hjybAbbwVGMPC7WtYvFrzWySzMFecoCivga7kwYN2nYBhmB_mWZ5h9dcZ9en39C7NOUfwGCQbvzJeoZlzDavYLxlnTPzU7WxcCDmA5tofGkR3TfHZyuJzNTIWs6ShZn2QaxuQvkKgJ9fmLJINKE8XhswUg7Vc2fjAfovfYmE-I4RgdYAF9pnbRMIXD6caDY9vKTusB7-jDQG_9f_LbByFGWScbyNayXy4Wss2sQ7Mq0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7810" target="_blank">📅 20:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7809">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qx5nC-9bpXlsjU8BJ0rf8myhTCy5CI5ELhksOTTdMml1KbVStPWA0hy8vs9cCoVSNah7IrHwB_4TWYM5QOmcfgYdVXXjpHv0S11PtQ9c-wNwThfek2b_F3xTMfrB7XZTJUWgjxU4oMlWqvneC0ClF7ZML4ahiZP-8Ceoy_BYjriZT4iwG4xVY_-fFBiMOF1G92pF7EEGyIMGhgNQt3MHXF9YX_tIrgTHOEQ7t7eyZN9NKFAXbGWJJjjCqWOgnLVYdk3bIRszl4UNzqKVMgP9HPlg7mMpRO6vTQoK5m5JCn_53AKjoW5DEzNglSElX7eP3CndlFqNKEk8FcmuY1yK2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ09eVRkMjJtCZkL9yXb4pKQUgoTe5gRg7KRXbb_uypIDaqlc0DSqXroB_FBbIOTBcceAH_q0UN4siPv0NIzbeSDVtPOuqoGmMnoQVqUnhFRTn-H3AZoZPiZyRy7tXQOERrwWZKLPJ7F4eRn0H1ah5TRqfo49r8WRcQd75O2G2ytPcgf3U2GYlTSukjqJRZGG2Jzx9xs4odYqZg_knFZpthRGSRVgu4IOB9rJhL6oN2m6kWtz8fCZTxcRwfwZ0hVjdjpGlFCt0xCU_YXHAU-M4ZH6oWFemG2-_d6nQA_zgmvGXDA-kPIQ9LOVG3YnPCr6bO2R8iIpqdhMXfOkvyXAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPQ9uMWZHF5_pUqol0vaetHU0191u_nUzLC8-hsYBvoUDGK0ioJ2wyb_zE7zJsVpgAXbwCVktAwLULYIqtgCXIh8RTsmXPFLyWzLBO7bda65ClVhvc2nEjV7qDpWwCTi42DyexwUQ5EKpwvrgCI8mB6wwGpOrIZODGohWGNXuVIHwJUUZhkdfB6ZrVTM0LEFlUheyB1Angxbe7omO6IHDIzYyY6HyLGNDrrKJQKlN-39C4u3R9EoBDcI4pzitNulEdwVtOJZpIxOSeDcjdKqGQ6wSxtErk-aN3nDIJ5lLxwxeEK9aMHOGxhakU1RLB18ZoI8MTmTmj3mdC0UcuLlhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzvey8hSuaqUEG5BBGHnDVV6vIaPQ8dM_mmLoUEb7F8xAO4hK97V6KygzBFmT3NdDvBjC0jBiymE4GTRMtrzOQBewd4uIJV4Ttg9zD1Cwx_Y2mr00t1Fl1R9_fpvGTLWukcGoGuHdL3g9MroXjAKwZBBVrr86WST9loISNLUrzLuiCLxmFwZJTEWqGZpy442M_fAiuYD3X_ys0rTFwXVy5U2_raUyeAKO2uw3C5YLELclPiO9GDBkw8qhKStUYuU2fbHc0SaSVBaBkNW7y5QHX0tnzPCkmDoEP6J4kDQAJjwytvhP-qXCJJm4a1lzyAUD9Xqh0garFCRsASio31XOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tF29mgVBE4VXuQTIuXzXbV1W-ZzzCmy8CtQHLokBGZOFu-LasNDVvSylZzinYwzxwtyWQOEuVkI--WJeGTKTISEOpJS-XUoCG9ORc8kKzjMXyekViSyidQzjDroFhUFsHuTu6s6P9cV_qoqPW4RS9lFdOxFOsXRTzJ6hAxvaYquc88Ryz9VYdCC3i8JX0CMJo_PV7meiWmwZFAl04__gNYjnifB_Y9GDRTPVhiVraRYxZu-j8Sy5bYQZdny8xTpX04QQupsmbPPgfGgdZIpHZpElwF-vTcF7fC-2MwioWKpkRBi35R8ASf9MvVMiux-NxCit7CXMnzzPJ_bk1YLQzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmWJixyUM5o7dATahku2McaSl47O7HUd2x6_mqIRkO65RexElpbNhc6JGKpssaarGr61znfgE80S22Xe62ACrJnoj5bvS1XLL30DPdNK0VVlfGTtNOyyY0ur7pPJP51hPzlyaVyUsGUlZaHv8cCDkKtD6O6zCnXLwo7GK3c0uOcROk5fEVg5y79-P7Q4YTQY47iNBviUv8i_hWG635lK0syaLkXuIr28Jjbjh2MKKBAYUHNcLHMWmem5cY7nhlJAB6SE0Al92Gu4gjp6KlsnSh8eQ3sB_N08g7OhBebmh8NkytwmbjhTn8MeoAIUVGjpHbuiMAZCXWY-CBWwgDUqPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQPqpFzpo3gofyJuVVFrNc-qhDxtFr9sVyr4wWdKcgV2_MOpeut_KApR0nyIQLwKoaXeUcT6LbOPIwkamnWFgW7L2itSMyLpa9wCNIl9U5kJ5jPYubG7fivH7_VhP0_KN8mIGYi_WVgF0nBKWZgtkka788qN8W2_tS1BF2ncRVrzPYUnejySMZjud0NMTIuTw-lZDJ4VlTWkTcvgfMl8z5ucVrHI3i-LXkcId3rvCaAZEaWqzWfFq0PFgOAULKYIFbWUBb0P1233-hS2p9VVZGbgpBKvQ8ozPNdFoFjrdFPPd1Dz_zSPnVqfVE4vb-7rryOKw_ejJ02MjpoEb3Ys7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7800">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7800" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7799">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khVFA6hE4rg6bMc3zwHuGKRBfYzmHD6m6gebOdN44aw9RMk2hWBrnN--wAhhSllHwiUTeoPHsSOG-BIbFatX4oei7jalbbF86Vdv43I9PhVo4yGyZJBiyhyPnYnLOZCCzJX0Xu3qWrZ5-2Jv2Bldh7AuI6qi9Nxh7-ZflRYZ5HkUuBhTNtCGBzxofi4pZNUQEtNRhoErBdowL4OOIFN1Rb6pvn24o8eOdoKAqEvqZhPrP_Tw_-zti0S4DPCiN7-XWzn0Axgpx2V9-HWW-5kCgy9CYg-3oqo89lotooLM9eq0GX1IdDQ0Q9O1FNppsRrnO0uTzsUmC3kx163YHjBhhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gD8aIOWgstN5-km1sC60OTnEuWX3oHIolEMto-ImOCH0nEtG_5oDPFV05Jte29mhosHmKb3RWwvK_OfOth5b_qWyRIkeKVo1I2jR9XnF9jOQz3zZ-MbqYUXw0Fj8RAPxGzbRtkHCDUbPzYpfFQ3yw167wESGejxjfdHnLmuctJ47pU3FtIGtxUJRlYNPwr1khYYIn-BTKdw4jXnJg6TIV_LiCs-so1BlRHC3U5Sm6QVrWj-Vkj5RrZK4JgnPjbcUvvzp4U6cm5joD5b9iq6OTZ9Vqx0pVtkAFSuETM385GCPrMDldZuO7cFJlh3uqaiAchsmIG48OEXJPjUQ-TRU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IT6L_tjn-LuF1gpRxKBSKnexvpJ2kW-uNlQXbidpqwv3bXpnKEA3kKjGKdFagvjFLSO2b01bAmQKq6Oh1G_nwPmU2K3SRQ5U8jXQeVTeJnJYsiRvITnVx0RX2jXrWkSLbLz4I0aP8HtobeciATOqkaoY9dlvR6YOg4QRQAYefIdmb07lGDe1Gn-0JHPhgonKx0gdd3R17QDJs7XqLT8rnKezgtQS-D_6TssPXI5vMkq-Ba9sjKNhkK3RZScObm47qWqGehmBIyEFquJv8kpk3yHI_X-y_q9z0MHE0GCp00-IX3jspzH3v1YcwDOA5IPV95XrAMasrlmkBLYl3Lpgjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7796" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS6glUc8-My4_uH31ii9sjGkYrkzLD2Z2rJMVQI_78kKoMA3GO0PeqzgE5ECapO2G2Z8i_kekhAIvqxC3G9Nx-Cp1BaxPRAOV4YlCy94YR2NqJ9syG7KFVTLLAdEXj317CmqWGXvC-OYErj96F8a3d4JikYx8Hs8d-HoaQ_aj1MBq5Bbvyp1ubpEf2q5i_2S0adIoJhl4Gk-78_9F0tPc7VUcW4BmJbKOpB7Nf4EELauYFo5rleNGUGcCU_DqZXBW3SCEXCogD0T5KfnPmOJ7FBH_v7y03WxxqcH0wFpvVTUtlft8U4IOmR0WvOsefKKKaDL3mqVdiUItwQUKkyQ9Q.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-7794">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRpKsjkj-0UfmPq6IM2mj7ZYFcOwlwrjE74IPZwb0dBH0r5pwJr-D6LjPKFhRNU0SEgh-cpXe8uijHa46P8gflihCrBFBIC65CM8tvFXg0iklky9V8hI47HaKowspoVf7lJKkME-h8wH90c0KmMQUPi-WIKD95_ajOforZ4H42Hp8YqzVnSTKn2y00BgPhuwB137IkIu030eXdyp4yRieoaVjaHVaU3MA5vVjJmW_IhhnWsf5HdfuqJ7ClGSF1ZIm0pJ8P4ANkOHmggecNY3orDmEt_2E1KTi7amslPFNILErnIfvVt4X9UdCYN9n4n-QqQdd2fizOgT3VIDJ4tsRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
؛Qwen3.8-Flash رایگان تا 30 سپتامبر با 0.0× اعتبار
مراحل:
یک حساب کاربری شخصی در
Qoder
ایجاد کنید یا وارد حساب خود شوید.
یک محصول واجد شرایط از Qoder را باز کنید و Qwen3.8-Flash را به عنوان مدل انتخاب کنید. برای اطلاع از قوانین این طرح، به
صفحه رسمی تبلیغاتی
مراجعه کنید.
از Qwen3.8-Flash استفاده کنید. نرخ 0.0× به طور خودکار در طول این طرح اعمال می‌شود، بنابراین استفاده از آن هیچ اعتباری مصرف نمی‌کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7794" target="_blank">📅 15:16 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
