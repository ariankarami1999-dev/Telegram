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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 948 · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIb2j-xkRK61dy-eBl9BYIgGrj6R-CilMuTBPNDJQEQv-4y3QSChFuRjCHxeWyOTdNeiK0Q_5GQ3i8Iaop5IcY6mk-13qWBLETCNcPfg1DnJTRRdw9-9zWFDuUb8qm-mAabLtD50DGvhonmJZ1egT8HDm04T0__DxB_L__LfatDQaKcgHgzVIOh_jW9_6sn5mqwq3xIge5jYGcrNnyi7qQ6hsEuvUeAj9IMi5uIXm3WPH6pyI3q2OXXqwIL2mHso4vpSaOkZvL8NDQ-hZtsGtROtVJPy1Wcbtl6-BHC-sbv5KddNv5oRUTN2tl9_xWu32lFEbmRFuKy6x6LAnQqptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5Awo-LbeGECrh22HUKfKx3YwVJ9esMnkAD0l5QSPm3pwBlHs9GNeesMwkjipmChUWubVATIEmkpCMeD7DVmxtaoxJzJI8qDmnZHPcMHXmAS0z3_Sfk15TBVO_sXxhAqpcwlbO8gybkW9q4e6QrwF6wBx940UTLq16sNhfkv2aMm93v_fBAC0TNrq7LMgOjMi9LhfPw9famo1H5j94rChAea-1rysN7L5e9cdhXGqvST5Fe4wk9DuHWMQxKPNUcwMA1IGiLnruW7bgTQszfHE6pXjau3YZaaxHqy7Hn7N-Tl-pLJsgUwfK9sNA4dYTyLc3bAxERKE_ReIxnJYq7djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2hlcrEhqBqdsAV5AyGcNx8BAseq1ubiMvWYBE80pyZGdJk5Ebxe-q9hfn5NRfrJJ14AdSpYxDL-czFptvpAUKxSy8JoeLcH6b01voL-5OO5GkN27NJhRPfYRuY5MP0c30jE_SVpeAMKa-KDxV6PfCtnnP11h_HKJoPN2rAE3Asua6n2GFWtKDED0xzsELGQ2dHIZHayXXaGjc1u_cFj2gWmU__XVM-MsRb_wMJ3_wMZ2cfaQMrCphvuWHeChIILM3u6Tng9shsJ29ClFBGJHdmtZFyPqvCaJoUN3IVn4mm2tA6AO-sLdOZHDJo55b0_bhf67wpNnoekPVDV3TG7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8YTFGduc5tR7Ek5MMGGa-JfGtWVi4lbokyerz_9mp2xaJsrG14NOHOM9Fs9D8EogNeqs95-j-jhsdz8xZmJVvpCrjZuSWJDrgsftS65PiZYFMYNmbj-a5zytz5HqGZ1We4OH0oObaLzofCVPUgiwsHI3Crq3edqB4YWHxPoDVDKmTYiNtV02eSORSKfwQY5ayeAKLM0Sro4uXU5ieYnG-vmxpIcdiG77suQh3LRp5ZdIeCs1FhJdTeej3we-3H1jOlraijGcqxp9mpneB2qV0QTaZi9Rmk41v86vvBMJoko0cf0rHnH075CKfMSM0nIPxetZQu1Dh3073DttwKAaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brSy9xsrRDgqV5g6hlneHtWPO7lGSNCHvkuHJMbBBJKkh5AFm6GGtNklfVjg8Bh0sFm9UEm8JFywjC1_AYBdg89xleW3jzbsFKUdRK_24TfWMFNlyLBtDcNeARQSsPB7K9VUc_5furum6kRnZEmNuI4o-iRv_Iq98imGNbJ9lzHKaeqsVDINaTZRksUqD7_iOwti6DhfJEpLKL9FmIVtMW6qMAp8HEUnsrNeYUxpOPyYSzVagpB4Cfd2n6tS_Sn4XWQTF8y5C0viVPGYBl-WR0TBiWVPRkwqM7omU9m3V7L5Au8JFp2nsFRwYca_Ycs8CLUw8T0fQQFA9eMxh23N2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUMaQipE0KrjJ6KEPhMnfY_QXxcYnHrts42NXKmtoWv7Faa7nPhmYBX6QBtTvKQseWrF-RotcFng1rEHH5Ps5WfTzUQc46EUsI5s0gRGdYQe-qxd7NlbivMlSMZmCFyzoCcd_kPdIyO6sPRYXeoPREpGl2PqLReZGE7vSp7gKjMKKc1D7RcvrTh357zHqtXiKgVs8o5mxUhFX16E449dMMTFyQTcg5STQ8FISwbF9l9bQeq0yple-7STXaHPt9FFtOfhm-1eCNHRgQTY93x-bDG_eO9t281SZbUoFUFZzrZ6rd29Y71-t7c-7vqgnbHQV3jHRf8Iv5-C5F6QrinNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXjcdHG-rzEZFJRSUgp7nBxXZtHheq7ZoCN9GZ-ICQosUcqIXhum98QUGavHp6nTO9sVE_o4SzE6FZhx5zloFIcN2KEhRHGTDru4WAyy7mP2OVOXOfGzQY4xdAmkYeNg08ipmJkYqJxc0z04kEmKZOMMEh3KLP_u7qBP_s5kNAAtdA_z5tNArgRBM2DupBSn5BCKVk34wvDJWjCUfebAjXbYjY5ry-jKokZGrOKMfcOeLLgn259XmTTlN3Hu2V1HwXYfTvxyQIxgQxuT585LUyH-xzAKDFF08pi6w3saeEkKC-WQa-qfSurPWiwqNzklzhK_CDdd26GvNjcOHDAxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPhqjY2To_gByvHnSOb0OI6lsCOpUHV6NCZXmPNwsOqwaOpw_WTgHyxgGBATYaqk5QHXGj962b3R6CEEQWLY55kxSRAQivqXQI_WbZ8-e_Xj6MU3Ftek0_5Mh75uGGk5AEQBVfUsgbyUIXGlbS6RG8uYtBlUvIDWrLUqGL9EJexdkmFHhA-uLUw4C7kzARGePAQJXESa2GITxSQhmVEWuIVwGttKu1QLMXll4xOQUmUklt5kRbGkPqTrhmhkI9S-_0QovZKphz4u6aAg3aa918_HUcCObt1DFr9E5TyIcQ2Wt72IpwEqM9Ix0NepbBpeNDLN0IQzcUxHXXrUVOA5Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCL7s9olVDpIKwKbfTM4cxK3vmIRPt85x7JqdkWvlkg5TLVcanRmZPK_jvIx6xxu4-e6hR-3kDgQ0HZyvNxKTBeI3XyqWALS7WZhpLNpsoGGNr_a7yRT-hxMEWixFidXt59uTEIP56sO3NkvZM94s4y5KKBb3nd6uTRfP4W7T6q4zmYu7G8jiYjG3IR1qIL63a-l-zfzmeg0EWLx-z-TjloMosw8kWpcXE5h7g9rc3vesMpNHRCIEnbtUHcdlkOCHCEjD0jgrA2eB7LJ0tD6hqksryw6Mqvw0t7Va7gIKL4W9ew7NvGeyfoghsK_5CGBzMDg-D8fdCqrL9F0niSatQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZYJUSEbyiUDDgkZGaHDlfcg08HDjn69QuB-hp-Rwj_t4HS6L7i9h8NPhtNVJmUuGzpqb6Vpl8-rvjMoa3wWLWYf3jQL2PIXokfjqErZozMbvZZ_6DJigU1zwgyeR1JldAPzBjLRd0HIGkybuUQd1RErgRXu-7vspqXhntERs5Odc5w5oKJFHvCh4QSujTU-UhVxMXfTZ8rlgjjKAj5EDbjYeDLOtBAA6NwEIN2x4OOocCvJj3fu9vPuy9-i15OSTvRwi0mJ113YILun0esvfCr7pAk2LH-_K3-rSsPnWWgRfUwZrpeytpySduktby7-TZh-HiQ-C00bgyyzG5NreQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlcTCjTxKCuaI9GN0aSNxV6Q8ESFl2l0KxJNt3RswzhN1DflPSLY68EUCGOnO_b5ATn1CDS1P_hnwWpWWoBfCZE0uGOuz6OcILKEBxdDetiYyq6cPM8ZnHeVGthaajLVrA2PePdb1Fm6YIwarwdbq16FG3LT978OPD-yC7UJvsRu9S7uR9sAEQ7NGXZ74Ba0Fic5IzLUg_7QdRvkO794UV5sxlS8BffbNIHiUlC5grDOIjxmFvbG9e2URjD2W1B1YAnrMqqYCwy1KlHLQB8N_Kz3sG91sc14KzMlev8opsYRJ8MgPeU3_Zjymva_69izQT20laX-MObSMyGWcS50Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0jsjzy5RWATc6fPiWcjf2vH8FsUj50VeCK2kq_wdvhJ8OZ96fTLYYERzdZPc4EjfIlqLPijYgXP749KBN-wjJwBk-X1-86FDVfu19kZ8-SzX1fMjhv0uFKjlxWncMv_8M38NEr0vkk0UsE8P_3_AyWSG5wd5XpqyTx72Cheonz3CvvW_fzBZYpsiRlMesmaFzsDulQQbk-FJmEln6gmUV3q75zdgHG7oo_lKSV_5bVQHgM99GuAMjJ1593riVGW7pJ1NfDvqmpXAHZsw8p05UxOtO8fr-sJTSicYjdb7fWhdw3cLBJ8wkEomR-JQfKPMV-TxOCYtuA8TV1JTGnE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3JuRCgkp4-KvahPIe6YOx-3TY0ZO5LfrD8Tdq8ZvzPwI41kBTvUZzMZrL3BRt5i6cecXIal8_OtYCBiKzO3u2A5gJzY5yJX4WgNoH2mIGelQocJRBLaf9sr1IDedNwf1m7ampqT1UoA8lcs6hgcm-6SwycYAdYuKscqeBBOcvoYwr8jiZWsB70YWc2KLpD8kDAF93IlH398Kc8kV6_ZWmjhhR___gUaHRzvnVUhEf2Xc6F02tF-8qSUlDCS6ikfuXcijQJYSchnBXn8lLjqDw9XwwxYejvGx_Fg9SoreCYp4ZziaaLhrN-l4utltwLI0BR_trKhwr9iFvxxoW2glw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGrIT9Rd0FrPf-P3yNgVvJ6tHsLtEUnVemMNco1IoF_PF-IUDAc8WSq3gGf7zVKU7qt_9247MouS6A017ayvB__JrEAsZRFj3Axe4SjGaN_szpvUQrPEwJWEwAz05-Kjg24umpqNaP9shR311MI7lXfNZB7s8UyrgvVsDHRAtZ0N2V6Da-d998r9h_JO3_VI_mmXcQs8RC1kEArsZGKXEzToIhEqwEb1l_7WRfWwvSW62qLQmbaP5EjRXnDK-hF9A0Lj7Ra1KmyZIOey3ttz933mqg9UMQa7ohRVZG6vBhFN6Rs6QLBTNIswR7gsLcoHSlVBo-E9vEuPhM4vZhwcOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVloPcHqdWGHuDPJG1T2SBcPt3qTPTksBmC5nfrYIJrapJHFWsT1Ht1BJAIsgiIcEZsiVZre8STxRLqa5PlGEVWiepydswF8nl-pCAzkeo6R6ongUybyzCjGzC_Ldlj07C4_6bEWQ9yqLzEeH27QdBTdeH5qlTKdkvRyeqE18_oZ3nwgBDM6JCFAs1lxLlqqmJ51y_e2mISnhnMTevstr7iTKI38XuvRHUwr_xDZmvKBn5gpY-YGPzy2iL2gMheEMTcw1NrGKt8md4hb0NW3okN0vBshvY0I2a78cvmV7mlNVfdbYZqCmDJlrVlxFkoZNWpNZs-oT-ag886U3E0tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTfDUisI3vDAdzLQSxdR645p_o8qjWJKz4s6yqr5dN0hv4I3uMdaesuqbnPiIbRWE2vqZiCDxL4FkwefJC8B7ecGORp6rPVU2NBrTbNU-FY0cWGqQ716gvT8dpErm8juueXc1W1YWeNg2VAwgzt2IdQ3vv6hJ6RIP7o8sUGjLMn1dgq9ADH_GAGdLUjwz8WVW14c71bAuZ3bEI1x57Drwnk2GUzElAs5pKyoZNGI3CWQUkinc92-XsFFCXp23QHINiUe_E53DZ7j2tRzKJa5iH438JcvT0TQNH7C_Yp7tZtHfCcN3dPDLL3LQT6R1RUMl7LFEHLJu6dDlAQbD8fP1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhfpPxYXSQstzb3wkN-wALcBy4w3xAMILgehsAR4Bt-_OOhFroWm23ZnYhfUKbj2lXv4H2DekU2f3YBJzNXSimu61hvRvNLsZiRIQqFwvQz19mHxp6L15aTpauNOG4pzXYuyKk5DQiWsv2xw5-opJFzFvvQ7vQ0IGOOyq4wAw4dcH03BRQ62LMPuOIne3zhQWNKTRmmoOHjX8_Mr1Z3348R5mzS4Qr0Jd2FxmaNumWZlaKbIYTIWAKCpgufhkVAGxqYDuk3Wmzrj0lrlU3i9BghtjAUqGW9F_WxDN7QpAB0hUnC6b8G76y-ZLJxtYouzi32_yCZSw3U5wYNBH9A6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESCWgH-xBEKSR6d_-7L6TySxDSIE5i69zWETL8yK6ZV3ZFoehsvopxlIsPb0xVdntQE41-T-AOoXjA7E1G4QFHwN7hKF5GkQC1j4SIasgkrYeiaN2CkmWJkN3ooqcKY2iXrKm6nEZxFJkdBv87GZS0EcSFwcBL3wIwk9xICLs7JEmOzrLsbM1afvldL3WLDugcciTCxttIzuo9HkomvpPijHfrjQDhKYnjejq2DmT8NvaRodK3rGE3Pl1ti-obJkP974sgQ76aLlSCjvZHd0jzWSCT1WzI5Dai6trXHDdTcMKhp4Qrpf5Q-mMEU_JV2hsn1Y87xwRml-KcKPXkUeog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFEpnRBCmNikqZitFENkh5Ag5o9AW-sa3T0cYxemmcwg9oxeey9_C-JyYX3YpyGRU6eLWR8zL4nrsGhTAm04fkjcJx_btxbVV38d5g-54WBbJSzuHpyJjAcjpMgeh1imwRHkOgTL0jC8bR67k_vUuRv_bGOp5AAQpx1DRRiWM2rqviiygzUSMKhy2WEXzUEUQF1CgiMs8LV19iyjmX9kGK9KllQUJtj65rHj2UbjtvYfJRLlUSAuJE-F4myCMAPSz3-34x2qvx-LsnKkfJdS_H6EyeMMDikXgbBVt0ds0Us-HW85HZ2dWUw1pYZFqFWksxjiGfCi-K5ueNr8YRUdSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNsbK8ey5A6F2lgbrY1JqlnQSRg9qKT2pGC15CrE7-xgDCa283kpKUOxwmv8swTx6mNKs7diOpnzRaqFzJxg4kXP9JaRUGjlghfQnaUCew0J8o6khMRGO_zidgNKAOkGtpqaS6pTPD8dcLpOqsdmQZkoiP35VbhVYVyJyZuwsmJlY9A5_FjQ8wq7xO_ybB2nxpmrJaaCO66nI-af8dffVG0-lGWNW6ScqAuXgn5jrEwOnxobhuK8SFbX6OYqqwKvNHDckiiZdDHt9PKUd-9lpjq3UcRQbbMg--BrNowOMbulWdgPDnGmkh1NiyWWa-gikIG8XuWqJltK_y7fv15fgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJoF6i9xRiUPietGNDaeInOKQ7AcFYy82D_-P8FnpaRu65k8rGcKtHNRF2bhZs5T4T86EcwVKbY-0qBBuKwllvJm5WkmS1lL-wwNONJRzUkgmvN1E5KWyXL_75pL9zcEaOBoN9WE1rurde-BUMsZ3cDqHBgwYMQMXY2_rnAhTUQGmDprmvih3BxJ9SfvZFyDpICTiN0QGKL5LdQkew_zBPvia1EbtJGG4rZ3iALIGo2bMDmIBOcgx2I7u2YrWzfIDOUVhSvINahT0T4nMGhJ_fclgNaqudUUc_52GKEHEO0VZ9iyc8DTzg3h4gQbyYzkwJU2uIBUFunRgU5zs_2B_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff4eUIvb_dhySPd17P12fOl38k7PYmVxX8lJqnnBsPCrgxni4vbpYVzjk7PedikG7ibdjoIfAqwPoTRyCpzdjjQbe-7AaFLuKFyj8GMASznpMuV6R-GwjER6lZ_C3ta0IhBKeRvtMKnHiyax87Mw9R-lITggtTITCHG4zpUVWeugZJ6c-gCQ6qQoWylmYzwPC8ocPIaW6o4WCUXMe1UpaiKBvKhxKJvuPreAXGzk4gSrB7DOHlFWUlhYcsjNYTAeYaj7-m24XUEbx48oxLvnVx0K4UUabUvk_18DR-PKUoRBFFeULcLSHk11mAEL93H04L5W7aIQC1-8oL-rBirUpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=Qq8nUBt38ntohI5umhnfGcxakhgVIx_pJfQ-7ZMRTOqCu90UFNjVOixIi6swg8XsF7d5ywdgWz9SelvZMWTGbBh-ziU4Heyb0y4odHJGJOkGH6BqGFB_ZnwKakIuRfjXRuGTNxd74VQ4FWhIf5EMUe_dbkPh-lhDSaP4s3PhRSOQlZ2n-lBQS3TksoWqlrXNgTJaFl0VRoqw5FTcsiSEpHLiy8a62O1nsLSJL0mVTcvezJUq3ULROOIifgHcEcS8nKJbU-V3XGfWCi0Tn1773YCVUvGKYRwYDDKF-SgJN70TY2lTs4JurFY1oZg1VSYta5LFRA81Nd8b-7yhhLrDRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=Qq8nUBt38ntohI5umhnfGcxakhgVIx_pJfQ-7ZMRTOqCu90UFNjVOixIi6swg8XsF7d5ywdgWz9SelvZMWTGbBh-ziU4Heyb0y4odHJGJOkGH6BqGFB_ZnwKakIuRfjXRuGTNxd74VQ4FWhIf5EMUe_dbkPh-lhDSaP4s3PhRSOQlZ2n-lBQS3TksoWqlrXNgTJaFl0VRoqw5FTcsiSEpHLiy8a62O1nsLSJL0mVTcvezJUq3ULROOIifgHcEcS8nKJbU-V3XGfWCi0Tn1773YCVUvGKYRwYDDKF-SgJN70TY2lTs4JurFY1oZg1VSYta5LFRA81Nd8b-7yhhLrDRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3PrbSbXkfXaCmtFrOsae5ymClAUzfHvlx8WW5DV_4AsxbnJUeuXFwsJSXXameYUbtFDdH_QKaWCycUB4RliMhCe2HgPAz4Mor3mTxEor3n19X140LX8DmSxHYVnBFKhY8jrbfwerXk4PDsoD0EhVhqRZGbBXe55pE64WjD1XpD-rcbQShJVpfI-Z6NNxGibB35XTdOSh9HRU162iMxJ-_R8PUZ0iQTHg65uNIeRU5XZrHFgjwul5jO-GLAySqZxGYnwjQs_6dnaZwJpBB2s54OOtd7eHLEq__KoZ0ShzvEYwyltTyU5sSRt5xiNrSwYGIaZtjx6VLHt-idcf6gmyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7vDnM2-ha0lrLY4RMtIMMlBgrXJ5W4DOnKxbLOZE0zLw0BNBB8vWD91Xmd_d40WVATwtpd1Rifmc8L-VG4Ql4JbxhJCX00I8q1gSGDF_ldhu0K0Qe-VjI0O4pec8fspA-juQwrv8eAtvqmoq2oQgwTXu90gEgT55p1CYg1nNpN-9Pixmg3izwDWDcAlLiZAc8kVGVV59vCqTr9MLEDHshJomLZqmCikH6-kRkS-J9CaWuVIhxBYqyo1nrcaIuaLfsrEN87UTSLDRQEY6mOzNw_d0G4AgFbx8DNUk9RQcTrOcqikddDkmvCa3vrps6YIq4Ga_xNXpKmuJ-c5b1YQnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkmg3Vvek56L6pMZh2wLYcDB3st_acB4GKO3o0F_7fXWChrpgPtFIvnr6OVXoeYQyFRWgtmrJDcWSGElIk3QfAK38vUtAyW0ehfoqCSj2lUNG19wl1V2E7LdKeuO4Xf9jFrYgpH6hN9s91am4JGlIZ8vRnuj5IrN6FoRTDbXg513s87nZ3OLDVLTzR7vrMe99G5-noHLLA6Xbi7fvjC8ez9CJLBtVke7RDX-tievfnQnKTiAv2pdi3KykMjW9npt9IKfqZ_g-AJoxrf1goRMgzmMtQZnk86sZeUSpvdiVuULvtbtJVbr5MPioXPX25YbOXA4G41nbam_zP6ceA29rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ7cZL4yinA4EQefCeBxnH5DpY6TolH6QnP4NPvnYUyTXMTUY3dYqqnriMw9ZJYwXVLoEzr6vcvkxyqHg4NKFLh71yKF494Gz9o2ABXSX1KoAGAF8nxzZVUFf7_FgWOvF7d1aeKtJsn_-EfmMRoDr1YcwWkOSbZTEXYNcDnSWG7Xc5-KiUyHPqV8aU_XaQZvdR3wkCkBopPrPBir688cxMbsqUZwGjI-M_43BJU5dyZ1HyFJ6U80W6otYp-vJDiOy8D-p13ss411TsUsWdwFyM7VPDAzjiTjpRKZbcJU99BHSg1pdNmksTPp1KTJvuP8yKCRDBzBbCtwiY07CthcBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JACH27GfgJR1qT_IRdk0GHe5CivlWMcaN1R_56-Pgas3Xxe09dxNbSJgXJvrcG31CqW3k370JrtCPjOXboYZOor9AGK9kjjLz_1L8MX5Cw19db_oIryOwLoUkwEurem0ithvwjTgFLRomjKQ0M0sxQR9EmojRa0wvgQjqbCur1ybBq4qSR-N4CRCu4NBG55w768BbSKAtXZOmjAii7lM3pfknRRsFIW4yMKkisVyBZKIq11TBwBHAExR5vWoTelwEzBLXRMo8ykvpMaNO6hnYR1idTGQUYt88B-Z1PfwGI2hhKY1q7HLeL59oaqa2XIk5JOo21Vh6Vupj79TLv2k2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6Y1dr-bsNISGLpwVrWLk1PZV2qyYqDvqvzGZCtasH9dPL3hsZex0dyLLshcoQMjlu5vTW6JxTkvCQ7WtRLaeSZvk9L8BZludSA6d-ag0us8HZi6oeMAUOVum-KPWSPltXx_VDgI8mgS5I2g5X7mxi2Ls1BsUQD9OEn4iBjsQWiIcyHS6Kv3TQhbcPyUAUQXj3AaTgN4jiH96YGHUthL47EAFyDdQAOj6Q6JqOciqXNd0sjzQoGSAM3dL4rRjDA9sCNlX8fqVuY_64RzqXvsyB17TRf-eS7wo-ptQQ5-_fjwTfxbNr_fXRCkrkaw_5B8e1SYFzjc-v6IBZh2-wp4ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqpR7u_1wFaOzIZPLKsgd5rmSRikwt_YKw1dA7Mc4gBAeSDZDgJN8DdSac32B2j2-ub_sA0MmzwZcWMeNoL1OGhlACLcqBSqr7yiZJv1B2fdAThzMHw_6qt8FVq0PMrwdh6EHThKO1IA6k3hyu3ssqddE42K43PgJ6xkMBHsgtQZ6X8e7qHb6iJOnu9hL54OiGzwdHKD92_fpuBO51RFkW5qm0XdoCYs1OaNkiUAJ9ZmFIh_PrmwOcdOALv0xucMebddo-ALXSFUbQUnjJyC2aQH_qC4Vd8Qc9mU2NJ4Gh55ubQUqbOJHOyhqBN6Gfao4I47OcGFIs3EITAnljXxxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0ybbFLXJj1VD5j3_mEy4WJShmTns0dp8b4Tlf95yBzrb9wh1pMVbdcdhQmtzBQH7Ruar9q3DUTbu_lko1qzZbzV9AKeHwcvxhSebU34vfsY1XI7pHORFFK69TlkblZT_UshOpowtMIVbARfwP66tti2yR-MSxRcInxRK5zweAuh5gD1QqYhAf6rt72kO46IBf9CPDRq03XR3EJMdPkgRmmkVZLOL9-fZnF_TvSs2e-L1YLF-sOZpuhYeGcygVOfMB3gxldg0gkLWhsOQXSzJaW0yu1ubVI6oqroGY49YAXbrVA_ksktb-ZXGQ_K6qadhHaCsNUAy-EQ_7aFyU47rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBPqs-56JkM2aPWgfKsvRRvySbynzTChTUHJI0bwYmRTsOMuQ5umobGca04F0ouAq34vUfl63UjUpKqJW3jtRSB9e_TBVh-c5IehzETpobtPxH6TStnpPqUZatgw5s7RyWiLF5kR6MkzL814kBqsbtQ9PAbJFZzIatGW7SQfgYlijJPWqi-ejhNpK4fP94Xmifd1wghxEA2mtaOqRzvKAK6yjkreAjMvcgzvGXGSz_UnMeR3Jhfy1kPnEH850u0vexEWqezQE_tDxs60mGV142caiSxoXk9A8YWiTdOLGXtSpTqT3VOVP17IYiiiCc0dcU4Na6WWkyOMki19fmDQVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx5BZiojmKqMIeNYMNU2cDrxUnqxkxPvYl5iRUg2z-DSwCU5SgipBAlwiZffUhdeS8f9k-zgYKSSPeeICJ8o9yJHjDpZtEEYeZF5kQsLOYkc-HDEhAbG84F9WMdNVjq_4TQJlDiTK7zDfpaxlxAVo7YNxqLDPtYTpWFEyBOhyI49WvyYHK8ZtcoD9Jtin6AsoNaViJge5hOGq3X9UDwBlQrgqsVoDFrdPbQorvnLiyJRB1abDGA5A041wtGzb4sXA7uZ6bbHEVOh0NSOvbeKAbIOhFmEdc7akKv_Wv_1UeyB3SQIGG2KVVnodj7agJICP-_BsKhPw0FavVoI2hWGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAzp8Jil3moYKQCQtgZ5IhivHl5NbALp4-i4FZrfdV1pvpuf0RFzeTFHQVz1htLXhJV7E-GIgFX3pavRyulHij-8FJtRH7n3vnTtY-x_kOn_LzoJuiXfcPf9I5fv4Zp-2KYkaAKJizCvmDMUiJwI-QC1VAEVwNtXF_R6vJ1ySvc68RWTYrylotODRX-BrhwS5iXOerNyS8-0GQjVlJa5e5QYO2-eVo4sJjtMo6Wi_FdlVh7Szfkv5c-TdhhV6TPIKzo0W76v4vuIBf68glWeG223UixI8uuVdsrrvLEY322YM7Ok0MHgJbjJK0BQY8QvPaSnol9YxhdBK6DvvkM79A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhccr1W9Ef1-NqqrbQnGpcTUq-Fxey9BucZKHpLmEgXLA0IZ3-XAGhaEm6GE3huZGafZmQw5296jD2IwBHMge50GfNzMx_LwPfNAEiYS2Pg8g2D1xWENSu9iWdvlHlSvCj0qpPAgOHt-t1OJq-tInS7cwO2-h-ooZMLDqItYhhH-C3RA3VnI626psRdIncMIpF3PedIOtUAgDoKBVA5hwOTdHMSGAukIEvhfVr-klaapwzvZgNhDqfS7FvyHqN330OD9Fdl3JnKdVygUH198UCv5ZOt-2rAnYp5vaQPbOsAiq6zdSfMKSIzlJjpxpfBJKLoWo7GsJx4onvlq8deGEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhdse0O4aLjPJGWuaBnW4XtcxmG06Uttmh_O6UKbi8mjk0VRnxhr8lirhM5_IGYkUhzF7dO_dcYwNLx_BjUOIQqlcZzXrRszSIjyzL3Sbi8wmoaLpC2NNbTXLNPpyak7EgqJATquyVYIbxNBAZapp59Um3da0tBuZNqMS3gVILuLtTlTcppzjvidwIwTmFrdYZ2QH4b2lR93UlBKC5tw0EpluJEr2osaz44cgBBFgQsnJB3YSQan73PFJR-gq7Msz2fxxdb08qujV7u-yT5asZTU4aUVnBb9rEMISXlO8I6FfZ9uFQx9lUiL6WJk3mTcaqhqbixU-HyVY27lpsrxRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDhGVVy_ZiNjwBRmUdQcL2nVfWz0b1AJ1Eh1GaNQQ2RnW7TUMhsqNyM9R0wmQW4PGXhBVq1GimKw2eO65OcvLWogM1-kLGuwiNvebMM4G61tBclWnKeSyTbB3a89YMbuo8B2_PGD_Y4EdyxHoTHs_V2HDNBD1WwBD7E5l_k8OJMyYKYcKg2TxIDCn2aUB5yt1iiGPRgN6aEREHI4fLfw4P3Mnm_CBTGXri9ORFUBhI6U4ZEgsa3_ZZJ5cgqnvLAvoW7eOcwjqVxCLvU8MeHVITjFgV6RlXcUbhMCNdnueEFiOIamuDEeZm10ennekuWb4iKFsiPrM4xFKQp33EhJ4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp_n5Lnb9pn0DvSRiFUl6SnrA7MGvYOEVMTPCvhn1J_A6OQ5o3uDYAUqnxMfneNsWn8FH21t-6WV4EQ3AlzRv_Ri8vGUMNU8OGB3URqEju2AbUXBVqmIURj0UTcXWH_E-rLNrFqfm6mqGvCUZYddIS-a4WFk2RWuKSDWTuCykjoQYQP4vBUsjUE4VnpV3z2GWtCx74lVr_AQiV6H-ybbWBq6J4NBJcStFTXhsQMQl1HofJW8RtYe64f2xgcC4K7ENJYPoLhp51fB5clttXguXhbIY9NK92YQv-rIesXsOMDkZiAo7YpNKQ7tW-JhhEF1LRyUhZd_6jfKLLOGMN1dKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sV2Ng26JyoH8vMsUDS-CgmJAW7cqUm9G76NEXvMHz4LnkMcTH9CnOEWUPBgAo0UBZX-7CVWZADH1Zib1pnXk6BSbNobA1S-4fOYjlE9ob4GxVLhW64SRXBHJB46GbxSXK8Blda5Ln8j2XkNM6D5O3PVUao8nctsVBaTwQ-CV9m18B78IL1yd9xC97IY_31qy0Hg-O9hdcXaG094Zk0IfMLzm4bd_NbC17NmLgogVD1emZzeQOiE5BCY9l7H-laTBj701YMFSABd91JUIKAX-U-0OMzcXUU7fs7f2MnoLT_tBr2frMyP3_FeDSUB44zlowFjE8V9brxNv0hzm7gzXZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WumKLyKXcJdz_6YylxCaLDd0lnTNwPupbRMdyVYe8m1Qg3ypZ95Cgq8nmaq2T5ETznjJtNvWlTP7mN3ckVsop_t8Gj4BCQmarLcQ-I5cdKaGUSSkCLpg0rp9-QZzffGoUNnUXgUAK3Le9GOKk5sjFDduK7O3lWRw5XtHGGDMH2WliNdcs9g2HPxf_h9mgxsMo4caFLegHoEExJgLLiCg3GL8WfvQrD4nKACoA_qWPfx9fhNjbgTctbEBJYAwy7swN9O0ygW3jXjobsYbmGmALb4E2X1S4tRasKuKeBy9fPr3qh_Mh7WogvaBJpSNQB-b70YHI1RgwUfQdPMqaiPxpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfGENgG9zLZ8-3iqxzH6_biZ2qbMysh7aCis0Y-PeZdW8H_ZAIXx7LgkOMwXK4__k2ErtxRZb7RTlOdFti5w7IkVKT_Ht7xbs_mqMUsMx4MPLhN4T3RWM4B3__O1UHg53igslti55vuT-rFCqWySaaaHUq-fSQdLhQ6qRNVGQlVk4aMqk5Bj_563xsCJ0vvto0tgS6bXwjUvYi8W8gOI5c2b8LEhvzjm89WEwcYqOeu2_k3Ls93dF2FlBV0vMSyTcoZWMve5tDdpFSk6Dvanp9mOys_sLKjpd1dmZJe1oGUEo9wb2rEG8wou3oOhe18dynIEYwDhjKXtFvu_t3L3jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pItZj3VDbT-zKCaTzWWep3VS0SaMiQyGPtD3g1Pg2tDaiNOI55o5gxdMO_ujg2XlusdCauvxJX684RMtYzoWzF3ZHn2uOJSmEBdsvN1FUPqdFv68KG-hvx67nv9kat5G4u6aH6d-P2spxE4Hk4br3GhxrXrPkbMl8pklTeSwz-_zB5rxamvOSAc-Y-nSjeNWKIMXyer3bV4irWlAZCOXWkEHJykf0z77i3I35ojaxhKaug_LBja4TIK2Weu-ObyF9tSrshXjVp4992btdnpsxCpQLJZVSad06mXapNV2O8Kb8CW7CqQka2xYTThlYDibx4Xc1tR_0i4ovvPauay-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnCxj29aSZvd0sV6nkP0cwVbkKSrgX7rl638NfZHX6QSTRYGliJkUKsz617AuUJebcmOxiZSl4Fc15n4SMTbJObaaUgdyoz2xtM6bHG6mFYJFQ1hulil_UgfhwuBVQoe2ufx0i6rIYrnEPPTxveW16aF9-5Djw4luQO39Z5t5nxzqMIdtaVgrva4IEpZZ0PLaCFbH6T-Mx6DyR7mZJlIXW4v81wcHVZqLnFIHt2Is7ZILx8XfChWFIu-FW20P_BfAdIgj2u3OuQ_hv7j080zA1v0N_G2djmlU3p6rX4gKNdkI1Rz0BdIyUZSW3-5cl3UZKIUY1JkfXgm4DyVbHsylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9u5kRcDoH3oIfMdiC_9ye98eL0nhBM04CSLeMsVTd_F4HNFeKCmC-zLvZtT92f6hko1_fOwxrPucuvlPZwZztFYp29-OM9mQaE8GI57tRr5AG3TD-HJevdu8E59Oh-6P9aO2COIT7DOTT2btPcAFMFBoQYltyKoevm6dxUdvfx53L05VIm8ME8etuIRnpqIO4HNW8r83GCY1NHrRIl6-yuvWkjlTHDHbqAUCeLDjNXz4osAV1UY7nOIk8jnSyMgetA22PUHKO0PH2kLiDpFgM5OQAy9eRXq_lGu_H6AXZG3SPflhyqkhHjufp_uH7hDkNrTITvWzHxfytrqn66gQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=k-hmEeluuXmofOIn_LujXx7P-OyJW2e_Au7JSppyj3HQ6MWAfTYqsaHhFgXnI-97TRJUVOymJkRYIA8p2SCX2-L4IjHPer3ASeCmgQJHNVw3HuETzsyQbce6YY4oMZgmnZq3ng-7dMOttwDR2H5CMYFda7FzHq9QOT9kphKHrXIjiUIRdy-1KKnkFIZhwx1dZfp9gO2iKaDFAD7aoLeQr0PgF3BmZLuTxvIVhbrlTXmaUIDe2FEMC_Z0hYevfsSE7t_qmNzHGNcBGGG9c-nh5O41TJY5DvLsXq2umfap38tL-5ABT4u4anOXSfODYO9p1g99lxRODjYSz2VETi0Ubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=k-hmEeluuXmofOIn_LujXx7P-OyJW2e_Au7JSppyj3HQ6MWAfTYqsaHhFgXnI-97TRJUVOymJkRYIA8p2SCX2-L4IjHPer3ASeCmgQJHNVw3HuETzsyQbce6YY4oMZgmnZq3ng-7dMOttwDR2H5CMYFda7FzHq9QOT9kphKHrXIjiUIRdy-1KKnkFIZhwx1dZfp9gO2iKaDFAD7aoLeQr0PgF3BmZLuTxvIVhbrlTXmaUIDe2FEMC_Z0hYevfsSE7t_qmNzHGNcBGGG9c-nh5O41TJY5DvLsXq2umfap38tL-5ABT4u4anOXSfODYO9p1g99lxRODjYSz2VETi0Ubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q29maLbzgKUbPwwS8QzaHYA4n7kmn3kAW-6fw8oRjzT6xjrQ8P8nJ66DvqR7S2m5AyjafoJ3Ljp55cuJYFD5AXAyVPm4hUa2_lF4nIvp8R2UM13jGZdLpxwKYap3H6nNDLGwVgqIOM5QRr269GCHmdZBSTHUw4UvsbgdQJarxf_bJZ3zejN2BZT9TBwTCZWnV3V20uWSahpBVp2fmQknzfAa4dWWW5wKXtMs6jjpyN4I93yB0PyBNCGpnL2zGg385paiKCMw19-7DJi9HLgRhK36qRwrMLxLvo0bqzy_RUsmRH-ubfUvUjeCXtOiisD4OqAklz5kEw3HWuhfE-Ig7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CekYLhqGF87p-IEfMaLD4K1nssKiNAwhLAPrP8rrq724s8Dr30u7JOEXlVAe08zaV205VR5KJYgIgEWWHfzVuLQdm_2Q_VPBO7A6n5LMUe2aYwDWovax4YV07hpmBEcAObHcd9_GK1YcGtkx_aCwgD2kO8n-elkkGsCDyN65eQ6HyGIfy36zPzPw9IdSmC7hdX7koY78tf3ldGoHUFB_kjpxGHg1GMqStG6boF7e7fmjsi6H9hA3IbKFOPiX6zDak0iVvQcYd5JnUAVhlgfGhBIUVBvmagFq9MafJ_7E2jHLsi-PV7E5ks-QOgp64jDlVAHeirYUkreJsfO4fhlPOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRcSrBY8LLVkP4pivzk9cwMZakAwJCE2xP7WG5Eop262GCCt0yOT-9Cmn2_U4kwSIXGCGD53MD5dAjdGe8cxn1dbCx2-AWjpGMTgSc9cn2sG3sXD5hZKPDH9j5biZVWXvsH6KSt4K0wJC_HBYhsNIf9PE9rjz6XNEAzXr277p_vsJ_o_OD-vrTPFRSwwFUIx6nWC8VVcvszys1ZryXDIn46rA6RDdPSL-6F5YbLHrDDX5zYRsXwtSeDA1RgAVvfnMOQpMVDvrjpky7g5sPgfufbpHXb3FClLLhOkRpzObjlrpytxYn850G_aLnuDN4qbcQwp_BMbowIz2__bx_kktA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=ssjCZkckbvADsN7qFvDpoYpxas1yssTCgcCM1f2U4Af_v7okqWEpcPjz6osiECAOaoI-dMi11okBa2zz_mi37k1W9Za6dQMq-znjRaB5hlKTP4-BhiUsxoN3sxCdlAdRwMczlpNExmec_9lLz7UzBOTEk3aaJpkyRDfFT6xBt-E_BxdGktVbMNIYn5nGgx7sEKHDUiDLgpOk7hsNoyU2ZV7vxWTodR1kt3t4fR6YQrEelU1LZVwc6ydY75rvn-NjP1rUdOwZOy55DHFphwYd9ROeTw5nvV1ZM-aq8vy-_dZNgbx5GadIoKzStc4UZfnP3Hy0MAD4oryMZ1Hf8OeMRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=ssjCZkckbvADsN7qFvDpoYpxas1yssTCgcCM1f2U4Af_v7okqWEpcPjz6osiECAOaoI-dMi11okBa2zz_mi37k1W9Za6dQMq-znjRaB5hlKTP4-BhiUsxoN3sxCdlAdRwMczlpNExmec_9lLz7UzBOTEk3aaJpkyRDfFT6xBt-E_BxdGktVbMNIYn5nGgx7sEKHDUiDLgpOk7hsNoyU2ZV7vxWTodR1kt3t4fR6YQrEelU1LZVwc6ydY75rvn-NjP1rUdOwZOy55DHFphwYd9ROeTw5nvV1ZM-aq8vy-_dZNgbx5GadIoKzStc4UZfnP3Hy0MAD4oryMZ1Hf8OeMRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS00KqAb0vdO3AqrKygVeTu5ugHHh2VZiSGdtvFCcco2UrLRy-DYj6qj-QANPGc-pGzvrS2KOxL2U_FWglVkmNHki7dsL0McQEnrIS-6j6M0drQiwxKhL-A0oUK7V8RX-NsumTzFa5To4yjlpmwFx8ypgOqmfw6xXSb8NOsS6lfyTALsr4U9fG8t8XJigH_AG-5Byq4moi9xAxHyeHgttFGAd_ypraOuvlWqbrW5mcBNDOjpwYeEYmHSxHL_2xaaoqQziwIqkoWFVs53xHe11QfcgRlUKh-zYIXaZi4bCoobBjBFw4pyIpK9-YOXD2uS_NXTbCTVM2JyIFozFwztBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FE2H7EdoyWNWnVVeCK-5b9IjxoyQjzSuwAh6u8NKr2-2WfTnBBaSyg-WZvjkSRo1h1eZuE80jont6TXK-3oCbbHuTK3xk4jl3WSkx3wKnZgoz1If_wRqyQGeoLwo-X8kJ8l1xWslpqG9Rjuhsr9Ep4_0c5qJmZwcGCG6dxGquWYBFx_RejVrc0wYqtN3GGJp8ceWxUwdDa5zCEVH-tFSksptzuDCynOSk0xJ4jnv-Cs4MY9F3HxqqdCueMIVE1AZWNQBMIAjWwT_1SDxYVono_l4AXHahRZuAo7qG7H-p_mbesFDuke1BUuUy96YMlMOMXSu-BS2cgycawK3mi4OPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aR1qnpPfwO5XiTNoCViCf7Uc2QEvbpxb6A0yIndKP3UqgysWL0XDBK9a3A1BYGwKO3WQakCGFWiXDkRMGSdxPh_ioXA54SaDLrIBJFL6Zy6g5HACJU5PiK8ZxaZsxo9nCeR60BdAwON_KBVLbcqxAh5C8FKwHJZtzalTW6cbO5-Lht5vhyl1SY4IxYxtAZ3L_8dztt_Cw-XaYpNLLgGXGjnXdVDYqs7jaV6LYGTciN5nyuV1FOPkNxfpCwW8M2EQ_ko_NSVQEX0TUovfECWmfJMSzhv6t-vIpVM7AEQ00MKnrtHsy2xsE665pBLnaSefUArdzedbKKKe7qj3VLebbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SklSe3IcQuiL8ZDWUHC4S6sq9e490Xs15OQWvMK43G3dMSbXjK2IwIGMTMCdayXil43tCmpTiqVhN0mil_Wv6a0G002lplDyAEOuAXGR5_TZ_cXV7LeqZ6hj8Umu2RBwoaKZlb2RRTferMIXEcrJpQ1rT1hiffDzNKJSFBewETrIze-_S2VCjAA3WOPMpNmFW5HZ0v1iu_9jKAHmKkSKMNmDwvjl-A1p3Hn8jfeQ0OfQJLUiOOkuV45cgOVE302m2iuEO7zouLz5VXFLECIPt7ykZM_niehMfc_86vgQqEzxY7Ueywzeg2NNu0V5GVoFcargEo28rRpyfNW4ndV6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sj2oBvMZe6o_4qHdA_6s57ETtlnPXt2gJnjYSIvbzVLWiPW3uHmhgl74COiaNZxhvpgrBsbKiblc6YDqDcgyglLGtMLcEFiAkf1oUiHIQA9BM5KTQqJSObTI-ROL1cS1vqEw58ovmaQZtKqPOo96JxuJm-d4Q6-tIQ7MXfx-KU6O76ksLTIdYT9VmYfY3Hje5DkF0xyo98RBlKptNrRAvAOezurjmEQTru-kArusLp3rVi-vEKhloBDUU__2WnfOEHJpHYUAC03-MTgepHUqAoqrsdYP6TXbH8GE9OYb_tCATqD5jNWlgsGjmAo3CgT-Be2L1XOTSW-yCzD0K5qt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEqBkTpiecXFFzwsa4nPsMrLXsxm6gp_iuRDLV6SeKy4jg6iQFJFp2Vumxy-l4k0e0NBySfLSUA6iBjrTmPE-vFoh1gwF-ghEMPmX4K3ok2C-iEvEJe9u9gJboHTS_On8FTGBAPRBclVD2JEwINCWlgS41iKWUYFZ5ZKOhanLS7xfFNfVA3FLxUwWwdAXPxCAfS0zCthJH-gXQeiXbKut0hu0LILq50egT1irRmGOaZGELJ2vMk-igKO1REhcV3x-L8XIga4a0aZBVF2DaTWtEpLAqBgvCmbHsdVb72w6MOrcjHi2d4DYF3VmXguLviM-Qd8faPLNC4ncCHTyBkqJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvJgxflh-A36l2r-nSPmmMsy5OHKaZ8RI1qQWXj0Rs9jp5aKFesRGXPoFiwF0v9DtWsP8yTUhQcgL17Oc_EAsaf8j4Jt-Fkj9_5hIEEIVP1On1i_yzp9T9Rb0MUCd2y5qDm7NvxMq93G4LTUtUDZP3aS8AusXA3Pi3hr6rz1dEakHp7PjHPYUP1sxe_22ZdEqFm-yFZe9ZpTr5OZXotA-7L3BaT_XGDM1u-aKZZRyDuv32E2xZMhGmw8fS1oDCsN8E1lfu5FvD-f_ixnOIzV-Rp--TXyf-SfFmRaLvUo0Qe7sCExt7M_NvuHqtmy1XHPhnx-JET0BzMmtL4bWGBUSg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=uelGVi1eFA_uk4jXmqolcLgV4z5SXh-jHL0BSCrovBY3kaohd4W9_3-O1X0n3Q4FXFcujDJK_Lzm-2L1Yy_Z0ITfCdUC7rEJpDBYyYGvtIeL6LQ_XPM7Ll2KrW-DsJGBF-fFBGYB8MeUpUlLnIhOjkzyWOtRwBqRvlTnhdJLsrdOV9cFh8a0DYS3DZ9g4piVgZiA44JaiolmpI7zespY_KmrKQcji5zqXhgbNTrQg7n4R-Nc3dCqIvPlalakDUoe5yLVmkxYMK3XLS7dEHRRJslDAg754DA5Gaycp4zb_NWiMyS63KC0UuIR4IxdJUoj9nycRFDAuSV84kLarPkh_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=uelGVi1eFA_uk4jXmqolcLgV4z5SXh-jHL0BSCrovBY3kaohd4W9_3-O1X0n3Q4FXFcujDJK_Lzm-2L1Yy_Z0ITfCdUC7rEJpDBYyYGvtIeL6LQ_XPM7Ll2KrW-DsJGBF-fFBGYB8MeUpUlLnIhOjkzyWOtRwBqRvlTnhdJLsrdOV9cFh8a0DYS3DZ9g4piVgZiA44JaiolmpI7zespY_KmrKQcji5zqXhgbNTrQg7n4R-Nc3dCqIvPlalakDUoe5yLVmkxYMK3XLS7dEHRRJslDAg754DA5Gaycp4zb_NWiMyS63KC0UuIR4IxdJUoj9nycRFDAuSV84kLarPkh_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHKo-8Xc3unYPzpnHjlsjLFepUcT3d_KYzxiLllwdUzG_eeAEYxJHO4sVqAeixYQYZ56jyGIQ_aoVmBsEsZkxM7LbW_WdkPe2p7evZYCdmdr1vZgNBX5nKu5A9fIHSD5P9PPWTB6s60oCpVQ0gL0XQN-7kAdS8slf1NsTmZLy0SJCpc6M2ekb-LGzmOrJFGfUQh5V-f4mM9ovgw-HelwVWUqvcxoUT4zFAC0cf5delkP-BPoFGvNyM_T3DBP4MFWmHt4uUPmMeBP238gT-U4qec3ehcizqYH9nG75tICuAi5SNQGz59L51Y3cDu_RQSMz8svtPbyYem-eUe4vz8FnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhM_-0DXYHMZKv9iezgSR03m9tqczIQet9CnThLDchh91nNJfq-OOJMak7Pnrg-ecwuIfy4gWHZrPHMl-CIiy-q583va5sQNS21S3oDalfaTG0QEJktDDjd4ee_FBVkgr_FgBYVg_B5NLijsSTsbNYKS7cQLj1Oqp2z7Vzk3De3NZU1NoFivZuKQc_IxwpU242dAVnaL4DdoIjje4c2GTQXvTvvnth6A4CE6NKcLcIuuhtw4TO-DblA0ZvgPE-3g3QSp_pbIsiCwP6MdCV5z8BeFOAgxF952d6_XnvAquLhoYbcf09Z2EXLp1gawmic8lsJY8kTggTPqwjj_cTyPYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyjSgOHERIkxm-hiNff6Sn4hnIxOXDqmDGt-FFlnvmTvVnglcrOYvSnaJnfLyCzcEP9jOgc_FYS_sHowP48kvxo4_wbpLKeg5K6SJuy1Teqx29fUmOmYnX_c5Lqe1Uv7ZL1qxRrsX3pWP8l04L7juezF2oYr4hP8lbgSp_nRTWnw4xLqPLwCaGQVECgk8WyaHjZk0hfhjqZsQ2m9wxR0EHUzTmEz1ba1xKnil_91pYkd68r1gh_ij3iXIoy4l2uoWaEPDsSHl5LcOeqV-0zcrzLLOu7u0PXacam7UTBLy-RuphgpchhUJZ_8N1Gb4INMMXMFS5MbfwyZZm3zJfTUiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDjkDX171EVl1bhWSTvag0ng1lfFeXsJ8TfJwicuDwVN2Tvj58OdDiNU9cdDQcADOCfdDJdW8H-Pv5orFM8i4GpzxEj59ELqmSKfbAiWm4KvBG88Hr5sddXxzTKWfWqehIFMRigtLj8h-ATQZ1XuSvy29UYwKn3myqirANErdkjTQg56GjjuLPkhBbpmYP20IW7oQgOR_9xYH8YN-zNObmyP3jN_50HrUJPtC6OrWgEpYveybcTGliWUCFSk1nFlIOQyrBhSIxI0SDQFt6y91yD3eblXYbD970vtz8iWofenMwucVobu10JoItLwUGlKcuW-98ymw5FVPZTrajJhKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fISeG9WQy48jWVOFBfrxmz_gBtLPLchyYkQbgtw39p8O27bmN2zN6aFQIDouxpunX0atBmgCSy4jQJcmFxtOzL9tigQ8rHbesg0d_WQDQ_iraujwHUzLD4T5daUVBHq1DQwwarJDUcCcBahpsChn7RQu-XdilUtbOe26-sshctSStp32tkbAJ6szkJNf6r7tCDuFAxXp6ZNOsnWrHZONRYh4SIZF7WHt29oqSgGtsOWWl2J-PA9VKz2D_4Pi4FSDoJFOqZVD92DjOqPQ0Oi7RToLNA7ulywtt-2dtlHKOEEzgtu6FCeE7Jd_o5J3FysCBXpu5hQPrYwSwTVc8Pw25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fx0dPLlMAwajfa2xmr2ArqWfeVDxG9I0nI2Y4OlNfGdg3qpZtoZHKtNHciMqeXbwcB3ShJN3SsfFpiFhx7roZp-VJ7muaeHYSmspNBXqLcgZIinoosw8Gb5GwsUscIUK7S_sluZGYL1gCWVC8sjDEl0JAQsDTIFdca_i_DEk2EYNUhzq3zmsoYm_IM3V5C_RH0lTqdE4SQ8lavCeFuTK94Ws-WXzSh_0Ay9DF6DzzGEFBKBM9K0ATIonqEtURDSCZ3fc9Znl42MQ0OU7O8pXdRAh3YpRQbmmzgJ7zSvPK4tykvlxPXnK57bC4Y2wuLoTfa872VSsNAAnGNCctcsuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tR30OLRqb7argUtdhu0wXJ1CdidQhUxmQEBvXoLbfWtE-kOpVsc3Yxif-tmEfRDYWlYD4tI0OXa3Aq-40PK2gYH0ACMl2nsjB1xgAkcUhcIwHrUtlqDwal4dmGNGp5u4Ldvrf-C6BLUaomlw0ARVRME-j46Gx5F_2-Y67azCJFtSD2GvYyJ1UDjKV4jxFs_mzR-0v_CPhFyk5xeW5oG_rOJ7hbSTv5S_8uX8YCsBERRW68j6gRcDuFTTngKcp4B1k3TnVATxqI-C_MR2aVyb2mr5azMOgpmVHHIln93xwjGYhaM5NTxH0pk4SHcEqpb5J4acAhTbEYS1fgIWyEgLbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rd1QUHrcWqEhNDjtxrGUL9479ltXY2OjpiSqN-HrRuS0fibVw1UV23sL-HJqdrKzRS-Gpf0L-dtin_t0R5Ih4GQo7pyPYFUl81cAaYmNYQsh2AWACi6y45iV01TWqPji9QTgKVKveXNHhO0NKb4fyKgaOpGdw85W1wUj2pODwTLW3Vj2PR_FrtNSXdBV-A25yHcNOgM5u0pUuNdQOjICwEPHM3HBN0DiE1I2hRoajBqWuc5DxI43DQNBav3srh8ZHeyi_hGEAz2bAvvB9OBasABdeWMX3DUVQhG8yVgoT4RTVZ-Pjfb09f3jtHAJlM8nn_RAe9er8087kNrJYznlug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-EyOpRggP0vrpw_9_hMqf6K5xpcqjwvKiJ3srV_j5nq4Li80Ji9LRNZLkdmanZEi7Bq1RXidmzL5OXjwJBS-2_SyNj8Rqqu3szhrR1XDo2uJXhN_ItgbYtFG3ouaNvFX_Qa-ElS--Adx--dxpg7zfBaeW5jcAY8A_fGVY52-aPfl0wn2H85kIDocZw1ZRQV-E7AOqg3AWACXyeGINRC7TlU9qJhTdKUiMZmLTbxsnlscc0SvWA-buUDuhsurh80dZZPXQKS5txYGBmmaTOXmf-z4ekD4kN1O0T4wvw2kiFJt6-rsiFduUH0nEcVVl5xaoQMMqaMvvgYR93pDhhbRg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=vyfdibFQ5fNEr1OdHXzQHBZinuvy5fcbJRi5GcT8lBk4os28mqOWuuT9drWE4ye9-M9qX5vte7nz0xGSPI2AXR326Sxmh4YhaxYOYJ0HMlwqJlFCcLrHmF7TIfbgRUyMXnSNpshWI3EX5VNX_WGRXZF_fR0Av_X8j-wtXK0uFYCtMXmWnE0Dx9b0GS4uNw41XY_JIs92xG6NT4-Wb0WRr8lk5vnpNEKl-JP2SRye5aUwQMrnR9NMIU6w7UztnH22tX92Umn9yYvRxJTGCizdL3dx_bHpm6TNMEDy6EZVx1KxS7dDLPbUUGe2PzSPFoBlyuVWkGBWV6nDMrv-7l1QPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=vyfdibFQ5fNEr1OdHXzQHBZinuvy5fcbJRi5GcT8lBk4os28mqOWuuT9drWE4ye9-M9qX5vte7nz0xGSPI2AXR326Sxmh4YhaxYOYJ0HMlwqJlFCcLrHmF7TIfbgRUyMXnSNpshWI3EX5VNX_WGRXZF_fR0Av_X8j-wtXK0uFYCtMXmWnE0Dx9b0GS4uNw41XY_JIs92xG6NT4-Wb0WRr8lk5vnpNEKl-JP2SRye5aUwQMrnR9NMIU6w7UztnH22tX92Umn9yYvRxJTGCizdL3dx_bHpm6TNMEDy6EZVx1KxS7dDLPbUUGe2PzSPFoBlyuVWkGBWV6nDMrv-7l1QPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZHuGuWVq2-TWAcd2hgT7fx28rkASjXNqNVDttmkFuJiZu7Py3HX2cLne33LASlBOF7XQzO12k2X0TGzVm06c-nBFbztVheVChFYxmd2d_qMrSfGjJK1-JXDjq08jcHPKGqkfwCKUefzQs0uU0keRCGv-yyX0yqB939ILFcg0BSJfoPAJlznOmsx3-Sh540J2V0ACls2IhjTYaMS8UxXkhuC-fVhdg444dD-ECzH94BNFCtyDh9XA60iBAe2bvTO0dgiIXx5a3GDtL5J-A79k6CUc8aNu7zm3cgVsT3o3tVZNSVOMjqTPV-vK0wsSkuUppoc7O0Y0jNP5aQgLvJWOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHq8b8lDCk1zLZQHHTpwq84Mt9YcSFRkVEWizNp6G9d5YOAy5fM_AP1FpDgqeD5rF6tHARO5lNYyGz3cdJCGatWeRZvnEKJ4XF6QYFIGrAKLwxCrbsP-AW56K10Zn9QW2fXgVrdsmKA_E67JY8brpErO9o-3lBcsfKypYD_6CSBMMT47CsOdLokuaaDcsPYdK8k_D813IsQwl13VhnSXU-TLbrv1n3p5lj0arVDVldG6zjj0b-l_7jq_ORmfA87z4qXSVRAFNJsyVygvL_WTdleVxvzi-lgOBvOGe7jQGrSxDlCNXuqVfap7E6vCcwi_RG_50p9mPgY5vcjX01ti4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiQy4XH9RlnEW--AehTJCnt8GVRy7_jpYXvfTFudHTOUpJMDFEsJLMOoORo2WivAyJvJTjDolZq3faWVtRieQJV9_o3vZjkTV6NiDz29EFCgIFHBaHOHUdjMhLiKpFeOv_ZTIN2ttXe1YqfvsRKkFG6w1Kl420K0Uga5rZtuNxDs1UKt2xWRgTfr88Bv2j-t7lCUA3bUZfFlpDPpPm_zSo4T3VozV1l0qAYGFjAAyETwwRU-Gtihvnrsr0KxdbB2yQWID4tmDTCBRYpy8n2xl9jZOlI6P1SWyeceOZtBlMysddJUDjq8KNnfSkC0j16F49w70Hqrg8-cLci4twuDDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkElPg5EWClqgL4E0lcuNyBBTJnu1MDFVMEzoNWgfAI4z-2A0m4wJJUQ2wTOGSPv-o9vXnrF8HKV0PZHMHpOXKXgALT3YWk5Wgn1KyrBvhS1YROZVkrj0tztaNxCwC_zzXMSbI3ezz10R5N9dNceqO7AEqMrN3n9RsXNQRTEEqIFA4eJhUohcRdsP6NorEO9Pk-41r5fS7f5qtr9OFYWi0P98mYnwYNx6V5NSBpNR0k0oBMynkL08OSJm-ZmzlquhKOA1oNbjVe_buLyXyNVZFR4efo2dU6k4OiOvPU8UdygpTnL_F-n5YNw4t_fygyVCcYIvxCBzN0UkVVQqDAfnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxubhbC1jVsNLirb5TBpHqzEmAqL2-fzFH6h9Nh329dwFM4vVI1M2QVVSL3xtoWmE14U5_ckwgiJyv0AWdC95GxSCcahmz0SCBj_RxxhmsYIf7UHe68ABCarqJF-m9TcInYrfHw3sQaUvxl8Z5UT1ONlMWfxplgH50zqBj7rLyn6E4-D20FWqtuH7JIy6Nhasq64LSY4IZYdjLKzTyNIwDaE-Eolwzy95vT_IL-8ajr6JnGhIDMyGFctulqXQSE-zqp9D7a4nFMAg7tGIU5nXj_LwOrGx3KvLIwFYEWYQI1svtxVaUO4DMYqskj4PL6yGTvHTgWEx-vV9-QAT8G7eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0_12zcdwRRGY68Q-AgtWutnLDzYL0Tk_5Bs6mzVc8XbnnXHjFCunkiQZaIZ7-ysfQw1R86-i_bj5e4GzUqeZXo8NOiyjmccTa3TKf8avtnKUNrnlN_5WOFSvPiZtvni6RdIk8VdKuS8-0K1wjzf1cfboTZ_fcnci_r66LajF-veBgkoCRa6dkweHi6fyZn8sqArFkV_MEsu2ygE8y190ASjjmRBuDOtqDlJG0yxVWxWNpTkUEJvOnoFHRyJgfg9UE1MAVcBkMwy0oN30Qjw7A6IImdg-fbltc4h0mfm2AZpE_ci9m3Rp1fygLc_D8qP-UqpAutTnrjj3l_KlWVjCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfFh67kLoelzYhXR_mf-cs-W52pYR4sNEYg8kzeXSrzGYcT4jktu40UO84b6lIeax2irlUyXO1OqjMcEY7ZhjU6PvBYnXZwHLvIY3-g5uvNifaLtJOdQhDRMy7M6AJdTJKVh-WS7QO3fuJHjw_yKntif0Eya0TynbMwIXVyATBdr68hlEpAbQO0zusX11sUgUug6TP82wLocJjkd4gml35g8tmq24Z_EQTaPGcaC8W0PzbATHE6vPfr9vC3aexSaZPRTIRkauZNRstX9gjb8Sgz4IKN_D0-qYXL6-LND0Yen8jCLKxWOa3ICCk1ORz87lJC7tJ0WbZbsEmDNAl1bzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dldra2sIFVSsDiPXJOQmZHvA6J6foOx5YdPPRddP37xb_X0EEfQylXLhs9a639C_ydxLmE_-81_Al8YP1LxI0AZDrbP0W7SrGbVsFAzpM_KCr7dkHSsS94UYBtBct1RQdSf98AIMCm7Yge7HiZ5A1k1KY9Mm-lI17G2Jx9S-64g0cHoCg4VL8TuEVVF8t0rKAsV26zW2XfPLkUYdY5rbtxm_vH5SK4KGULpEpHrCrlPQGA2fAxKYU_bY-HI9FQXur6CF0RSZzTpSKVinDNdYKm99xabPRGfSFWZcb_AcQPoLDuv7RPbfnS69SCKEZPbajWVFevedDKxm6DD9F4Xl1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFcCeQPOFqr17IjeRUb_N8UnfErarnWBJWoDodApyM055dpE8-qQayjRgs03c0gNymkC4b2lzbKUZq8FJiW2w44ztqs83f0lzPzOm4BsETaHjw-US-le8lEy81qmMJAM9tgDa11Zjzc-OP6TwF2RQsBAGgVV-xS-5giwPJ_NdtCmm9xpt-FfqoW3faME2yoXS5AZGNmb9FqyYoHbjheWpWLL4bMGzINuLqRTzr6qK1KSv84uDkTvKLEMI61hFLFb3hrkFK5hzx_tYgDWkclhCBFvAGnaSU5YzHoSHcL4ebCW45da8FGiHRIUQDGDdCxKUnLcLkrHMOKbCLVexu5GCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-e5uJ6AogVA1m_5vohVBmCNelvPBJZc1R89wD9KrzM9JZ_KoXditczxgnk_R_U0kJ5b4dPdz4uqTEMoFJ6I3KzuNvZaSlHYNt8uRVXVicC9doJWNVQ6X-nqT8oiNNCgrccI233NsRRsTZLr_AD_yPp37iJ9ntyqdtFIX42ca-TIj32ZIft4sD4XjIGf6KWypzd4-wU6KUj5NkLj00PRw-cRLjiEElsVtTDDVdHFzK3YHWqfniklZmVM4NsbUmDrDfKsdEhlNaLBHivJLxSFxndqWr5EYU4e5Wx2fHuYoUPPLoIRUzF7-sxqYDjRljeJiJJz9TNuoX3hyVtOP31iQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7-mxd7ga-PwiD6-r-85-lixTYGl-RAOBqBon1WOBIsXHrxq5z6tCowmbS0FT_GGsFg3qmmJdtPQop_W2ijVA7xQV7xPQTTu4QT2Jj5klIaR7Msu8OkYJRKk23Tlv2xzd4WJDf1IMdDHulDZh3smADTIbFSw7G39P2Awnb50CEgrjRu2gMqxlkQ5PYuki-nf-AJDW8RV-oe4BggeI1u4-VL4wi__br0hU3w7UpglDHf1qvZEMkIzrJQtODrqCt7Kp7EJ13pzbWEadUJF6PI_OnOGvDkYtHF-Oj4RWohV-O7lHDKWANMmZk-ZyRVG2ERHiLTzECmhPB6VcftilgMVNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUU-cufd0AJgaNyUn_3JRCr0-ek0d7jgz3O8bld2XFozMkIHaZYxIHZYOn3rNQrssT3v0Hxg6BO0buDxZo8u1kcnEhwhO1AR7VkA66pUTZqm8JhE22V63HCKSkgDLel1aS5rp9vEiiqo_qKRHjzd2rHbJQSmKPHue7154HOVf3XJK11Fbg0TatWJMzLWSUEmnuGnVdWYl5z_ifXHO6akyq4nGZCY1jHgOODfCfbDHbotWnkKfZUkGYLhnUE9MekuFxf0reNfPg_oZ9dlNcSiM_WSYtmhlLY8zk2Pfd4R1-nRGSQFZ7Yg-k2iylHEf0eAiS3-5KTHJePBfGW5KxG9ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAFNosMCyk8p765zJtSIYyf7wQGBNh2TCOjvFW64ksp0MMJT40WfvKpLL0fqEkPs8sENVdxLp3-V650DHw5ELbueq1oOS8p42x4dtwEvl6GsAnpISQo2gqbq7OHKzHI04LHeUA0oqkoKcOFOv_4vJGKB-iP1WW4GCpX12k1Ftmja0z1E2XL0Zr4Ca_7K_CyT5sr5BBYT3T1A3foLw8AjKwySC-wAH1LvDnligiQRW-fs5tFTozu45deCKpT2K2V_X7CYVrvRgHwbxA-w2PQgEY76nKi-LNJb-1faO-muhZOPjG-iY-_fTGe96mKW6dGjbxtnfGzj8GHCWRJzIeg-2Q.jpg" alt="photo" loading="lazy"/></div>
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
