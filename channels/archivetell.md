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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-7949">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 172 · <a href="https://t.me/ArchiveTell/7949" target="_blank">📅 17:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIb2j-xkRK61dy-eBl9BYIgGrj6R-CilMuTBPNDJQEQv-4y3QSChFuRjCHxeWyOTdNeiK0Q_5GQ3i8Iaop5IcY6mk-13qWBLETCNcPfg1DnJTRRdw9-9zWFDuUb8qm-mAabLtD50DGvhonmJZ1egT8HDm04T0__DxB_L__LfatDQaKcgHgzVIOh_jW9_6sn5mqwq3xIge5jYGcrNnyi7qQ6hsEuvUeAj9IMi5uIXm3WPH6pyI3q2OXXqwIL2mHso4vpSaOkZvL8NDQ-hZtsGtROtVJPy1Wcbtl6-BHC-sbv5KddNv5oRUTN2tl9_xWu32lFEbmRFuKy6x6LAnQqptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 327 · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5Awo-LbeGECrh22HUKfKx3YwVJ9esMnkAD0l5QSPm3pwBlHs9GNeesMwkjipmChUWubVATIEmkpCMeD7DVmxtaoxJzJI8qDmnZHPcMHXmAS0z3_Sfk15TBVO_sXxhAqpcwlbO8gybkW9q4e6QrwF6wBx940UTLq16sNhfkv2aMm93v_fBAC0TNrq7LMgOjMi9LhfPw9famo1H5j94rChAea-1rysN7L5e9cdhXGqvST5Fe4wk9DuHWMQxKPNUcwMA1IGiLnruW7bgTQszfHE6pXjau3YZaaxHqy7Hn7N-Tl-pLJsgUwfK9sNA4dYTyLc3bAxERKE_ReIxnJYq7djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2hlcrEhqBqdsAV5AyGcNx8BAseq1ubiMvWYBE80pyZGdJk5Ebxe-q9hfn5NRfrJJ14AdSpYxDL-czFptvpAUKxSy8JoeLcH6b01voL-5OO5GkN27NJhRPfYRuY5MP0c30jE_SVpeAMKa-KDxV6PfCtnnP11h_HKJoPN2rAE3Asua6n2GFWtKDED0xzsELGQ2dHIZHayXXaGjc1u_cFj2gWmU__XVM-MsRb_wMJ3_wMZ2cfaQMrCphvuWHeChIILM3u6Tng9shsJ29ClFBGJHdmtZFyPqvCaJoUN3IVn4mm2tA6AO-sLdOZHDJo55b0_bhf67wpNnoekPVDV3TG7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8YTFGduc5tR7Ek5MMGGa-JfGtWVi4lbokyerz_9mp2xaJsrG14NOHOM9Fs9D8EogNeqs95-j-jhsdz8xZmJVvpCrjZuSWJDrgsftS65PiZYFMYNmbj-a5zytz5HqGZ1We4OH0oObaLzofCVPUgiwsHI3Crq3edqB4YWHxPoDVDKmTYiNtV02eSORSKfwQY5ayeAKLM0Sro4uXU5ieYnG-vmxpIcdiG77suQh3LRp5ZdIeCs1FhJdTeej3we-3H1jOlraijGcqxp9mpneB2qV0QTaZi9Rmk41v86vvBMJoko0cf0rHnH075CKfMSM0nIPxetZQu1Dh3073DttwKAaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brSy9xsrRDgqV5g6hlneHtWPO7lGSNCHvkuHJMbBBJKkh5AFm6GGtNklfVjg8Bh0sFm9UEm8JFywjC1_AYBdg89xleW3jzbsFKUdRK_24TfWMFNlyLBtDcNeARQSsPB7K9VUc_5furum6kRnZEmNuI4o-iRv_Iq98imGNbJ9lzHKaeqsVDINaTZRksUqD7_iOwti6DhfJEpLKL9FmIVtMW6qMAp8HEUnsrNeYUxpOPyYSzVagpB4Cfd2n6tS_Sn4XWQTF8y5C0viVPGYBl-WR0TBiWVPRkwqM7omU9m3V7L5Au8JFp2nsFRwYca_Ycs8CLUw8T0fQQFA9eMxh23N2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUMaQipE0KrjJ6KEPhMnfY_QXxcYnHrts42NXKmtoWv7Faa7nPhmYBX6QBtTvKQseWrF-RotcFng1rEHH5Ps5WfTzUQc46EUsI5s0gRGdYQe-qxd7NlbivMlSMZmCFyzoCcd_kPdIyO6sPRYXeoPREpGl2PqLReZGE7vSp7gKjMKKc1D7RcvrTh357zHqtXiKgVs8o5mxUhFX16E449dMMTFyQTcg5STQ8FISwbF9l9bQeq0yple-7STXaHPt9FFtOfhm-1eCNHRgQTY93x-bDG_eO9t281SZbUoFUFZzrZ6rd29Y71-t7c-7vqgnbHQV3jHRf8Iv5-C5F6QrinNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I38Evbc-loTYSSl82oyb4jl4F2xy-I5J5WxgETXm4izp0ByQO7VB6rmJ4khUGWc8nh3r7Ll6mjRh5Pcjh-1uDLCK6XL0KRCWna2XGMzZyFOkKKfMt3eTpa6JVI1D7oYJLX91FHmtx9OXn4-y--XaU8pjUq0iCspOwnAfLYhy1hVBKoVqLAZoxnGXi6sjzul67vNnCky6jEn-tHh53c_-YXSl43k06PyIRoqVn_-aKTQF6b6rjsti3UyQ5_G2eTAjMWPNXQ-8bEFgl0gVYWfBTas6zwEMhB8s3YmU9ZbIw_u3hcMc6KQ8FMy5op5hkD8KMUuDxxg9G6A_QNYHD2LjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5O3LejaFxxh5HZoS_DJWds6-Q7-2sSuqMq63pZYP4hyHajASvjRcEK-KSwW3qJECNSs_RqfpjV_zX77-eXIRZr72OlUfZVocUAzKu4ix-CmQDVD73-pzFu3yFLv8IS-gsvcgi1zrdggmFJ_nAc429IZ0cSGmM02yLh5X15Kg0PmXDemGdtotMgAWSaZjsYb-zvOGUrc5-HvsBAws_fC1NBNCfa71X0tec-Za-rtMHgQG3bdlRDsYMJPoo5zN_aiNed2t7xrK6aZrMkV8TRcpJ-whzeEudB-kCcl_yNfwbz3I7_qwTVmyK0zbG-JyP6bgeYXI5WIQhtaW2lxijxbnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vATKNX2oOYFcu37BsbV-v_zQB_qVgpjF2oR9K-mEY5jHJYsd8y7InFydGpQmVEZ4jAqE06Yhs5dcs-S7wY1pcnW9rmRsbs9JoiIlsHF8_Kex5cA4jvXrQkWwooUEfMjv4BaPZkFkKQi3LRodigrIiU4XCSm3m4_-G4iRI6Mi1BjCxPT7Gze7c3DrjRGgyhczI6JiXt8ykKXCVjonp5SvSqy0-VWYupcM-djy2FQ4AfQ_BTjYDoWcQX54INSQH-6zXx68Ej9v7cO7BYIIKbW4mO8gv0nSguidwdHVcy_98nlCVRG5E1chYd8xzKCB0746jL0DG_8SHrEVYzyFsKl23A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNw6nWIr7V5_P9r8D0UzqRwbMhZ2VBN8lSGKaTZG7j1qD1R-73NRoHGxFTyu2ekvfujz0ZILzDN-W5W33HNCP5XQ7pSQyx33M5zYMQEA9azD8fiHF3Hz4M4UgGRnoeTevEGjRFp0I4xr5gz9tomhCQEKQvOkutKYL1ERznrYVd9QO_ol_obFgaEj87pa8_2ZEVD-i9uHk9PfX9FLh0st8ZDqSiNItIq6lCjgPe-9NjmhFkc9MEFYTUVp7LbIN1i0mgV6D-t1BT9W6LlYHwRIqOdF1j9A45q5VCiGTaVCPFWKD8hvQKTn8vSt9EK7ObARcRB_cdcnfNIrD6jsdmPlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgdpsjMpfPz2pS-QZOWdp2QctP8wKOQQh4K1r3eAUJypDRBCNCD-vwC4pytlq_hO2P96CcHHk-OWNNYOBYx70YcFKZJ3MJvB_qSHJq5orMJkL2upxXZxlxYz0y1rJWSQ1BRrM5pGSFH6T0XdcBPiITgsD7VR8AIvARcabwmEVUI4qqKldlvxPO6U4wxmo3zRBCk_Hf0vp2klgIXyh6aTvbEeCT5D_k7jQWnV8HiUfJOi6wnvD5OqcjmYgao5B4FpXVdXhlorRAf-E0WRfQz1AOEogztz5q3N1H4bZ5KXW2cXbPdcSN-E2S8visiVuIe2S-vC7E-R9q6Uy6REvC1z6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjTxGW6t7Pw3gcCaYTo2sANtTSVQJkzRFNRy8iFA8L3QzX057Qux2nQtswfhoy8KIn6culoQEasrTTYeVIAuwyTZZNfB5cZRj3QlGScTXFceLmqKkTwxzV5Oi0K25b8-VNysB0hoCORhre_LFg6JcVYhW_B1qK8D0ST9V0WaTEj62jG3jqIc75NBGSTg_d1MnxarrsV_5UyIYpWx9o-RMhAy9e650z4dXn3Iiaj1xmqaGmNn0VoMhmsyW0j5xixHfVXnPHm5dGFsadUGXbPpoYEhZTULiHj7PuJGB2QPq36kN1RPEnDELyK4UB8qtL7Nk4vJ1ZaN3yRFwAi3dO5Omw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1wlUqTnYisEcJloY2CPrGGDruEreiVbVDxjW7LGyYsdeJVOPmNYnpmcIjKX6wHHhUBRmZO_6FEEuBM8GOlBHjfhRZ9L_9-sj50Ibhq7XqTbWFw0RVlvc5bmEb0uIwU9QiRSiUksfQjOHBPYX_XMy6SoGFBLFa8hM1eGiv79pP-kwWU0tb3CNxNgV_zy0fWeFubJpPfiYnv8GnP-NTesjWx-LEcnElsHUF9G4D5Y7H5qd3QHlqzf4j1GpVNwF_-WNPzg2HPV6n5T9jmdvkQ8w3pBAmNaeZxqS2UytGvD4zTaXRTuP-8MkOrRHz78rzob3U5c6IGS1r_DroYhzaFQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rReJD72wX7fEOEcLL-mlRNIZPCTvMffR907G3VezfhSy1cDuMo2vsHJ6Y38IvuVQSOXGnt2yYtevovpWgOGeNLxm7Wai524q1Whk2cVow7cBraaa_OLzHBT3g5mu-BC85xv4Ypn5UTo_n8v-jXPVk0kvniMMjkVv5PI7U0ap1mbQgdKpk8MDgRumj47jPEGdPxtrtdt0b1hJqiSPJiEZqThW9sPe-KvmonPqEU8RsTQzkYoYs0tvd8Ka6kRNt5dSdr2k2_Js1LYyMUjV6_U0fK8Weg2S4g9Vzwd8aemtpwaRLGVDL2OjIRNQ_VVXBqh6_SBOOyLjFdZouHFra48Lyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6dvejKpLqwbZN_sNHt2IJb_H2_Sc94vVQRT4ktfsPmNMjIyc67Oa7L9QML6xJvUYdmjVx6DnRJDi-w8iPqrpA-krA8pEW6jSfHNprZZeKtI86t0Kfv2OOrEJD2RI1uRO0QD40hHoyCoPTlE758HhxMtK5DXZY4uiSHTPq7rlwWRJ8sGLdm69UKA7YoYP1910QXKqCCOtJCjnAVbFD-di3zQySRg6hPP59_lqMnPMxkL3Zgiqe6WXKK2VfDAZfSmpB-3e9fcQ3LSUs2ZkMwvSHuL7WWBFlX9HMXoqqbwDuPj5L2x33xkMQlvXONUET_jNwDXirybiTvbIyiI0YmfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU146CeQ-AFgdk2zYx8Q_KATvb7jttl2tf1DYi5e9QL9P5Xj4SZcG82R3w6o49djQa0Z7bEv24Wg4Nwv1Yjs3HRok2w7vV3en53rBSW1v-Z0lW10NHkmOzDe5ka6_uSehfNj0rP8DFrK4est-FkiI4CYYhKK3mDlrfL34XApzjmgLirS697szETY3ZyzgFQrVvEtcdSdTDngEA9_cJefEf_Ahe63FRZDi2gxMCj3nARXTZCgaK6x_uwvMTNyB_pBSV5AYdYK_W48ijcqgE5QROuvZkpQWUgMawwxJd8zsbsUIipsAq-NhGcUrxHz7-3x9ouNqg_CGAII3DdkLbg6lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUMrb8oC4ei6XJGowsqTQlHY6ofZ-QJwu_IrY0ntP_jj1UpGmAL-Du8S1VxiyE4JCDB5twYptAo8Tm_vd7iZZ8FHT6Joj1BVJTvr37i48pkgl7UswWHgsiZ5pfy8LcvjcVgNd9MzKKFW1eHXpWhO7nFea0NrgW2YebeJ-gIHljrHIhSIKuyPTE69ST9ZdCrvrFJDLL6_UseqCiBKDeV3QGN9pjrAkQevdvDcSavzER0jFdUJLh8k5QWH3QCNwWO9lYothaKMghmapDBcyAVnDzTU7ivKoxIFqbJ6HdADx7tm5huCU4uOfx_iBO8fA15psK9lCUNynQFP0lWIiaVcfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVNUbTKVm1P3z80xCrIqGqxoidam4vGHOrTCuZia_cAnTNSl-1wgrOgDYMXmDacSIpKC4fHtc7OUvLJdSS3QILhfRTUy1y4el7xc20ZLg6eX-u_KfqaKSaYh3zcQwLET05bI7g8T2XvD2P1DxUc5WcuBpSjguyszP6xcrydunx9zuRBU62g0ZFCc_CD58oeBuTV5sso-h-FMls5Tlq6kg-CfTfS0PGcP6dmI0Ofv_yOrjPsE2XtAXyoAQ7f-RZp_nLhokAwYCDGTWiJbFJOQOw2IOOuaNfDYG1B3yPQFUctANBielCuvKRXXgPAyPX4DT7-xnd2hxp4bgi4GWyciXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJfFbGW9rwaIo2IqU1jQXgcx5UFoKUZMk6yvsTM1MRDVPIgATpk68VtoIWKBlIF8QyHcCFw2QBNKMY7ZSo24C3qbuLvWu6R4mJlrBIUeZXiyb6aIqyVDoFRw38e2Dwr62Ke_0zljVaDQDc3-oJxCvUdAy78h_QAdYYRgcFmWiRyeLuWMmvuszrbYrbD0XSNIph9-RjjNC_GGs0jZ0iiYB_w8zEV-ckhGvkYZNEGezc1dp5miRHdCEwvPpTguL0nN2NSsHsgEdO3F6krg_NRAypgvIFX_gPxf-H4ZZgPV4ReCvuTUqMeRb7RNs-JASSI3vC_q1EqAvLLz28LBL3-aPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dOIuJVTBtdZ6saPjqOtOu_C6QVzEtTgXQicW3DFHaLCbzqCDuEUJR-WXrsJ-PQWwtwBzAGDd09T01hO5v5wCITCynNZlOFItA77wTShiGoR3QiBeThM6ZL0WUiXGJclsoJJdlR6N4xEXJsK_mCzqCOwCzs5FwRqxy4LBx72Cn6VcukQ-EU-LWt51lb5DBG102yqahl7-TYoqEcQSe0BkN1QaAWexBJDUSmSdN8II4P6Rw7vhjnJG9XqxnEnthebvSdyMsK098j7EoZGnYk64M1wRIfj90cXkHWEydcCksglBWghcghD7POMZxgUoVFtIYy9xn_4BmqbJfVVOVRev_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-73q6Ho49hTCM-6DwXqcC9HyGvx7nI49QIftcLzFLXXKyE7TR8az8S0ceEbJXXwxlrS3jYwXZA_O3LpOZIiwOo1AVRdRlC3lgNUL17AYPkeUW6_5HEuePWAlmuzzPnO74TPLpLy_5I3e4yte2RTlb5rQ6jftPxhT1jhFvOxRwyqHLTrJR3yQFJyKMC4HDP1Na_npriOTH3SBmG-OMsYEtUAf4UuJH1IW3KiLm353EmBPOsyMRT68ct1RUB-wwUv6Jg0mBF383kt0B1GMcbtQV0-yHo986Y6YyyZHka41Wb_EhspIvUV18E415xwDPu2wqY_akV3oARY4j3HnEbFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOukdah6d2jVNLA6bn7W7BNH7c0OiB0kd_rWsf8OAqhZAXN2YEstkN_d2I-DqgWxD0-t91VyDuYip2LJf_FQZ6jjQ_VcAuZYUZvcLq9DvaFUDGtrWQDhr4pFBqiAa4-jTOXIO6RrRsc9bXHC6aEga4y-2AUfOEPqBhKD5V0MZ2TuLokcbqI2WrSVn6_quaw37eg5nXne7Y_3DBM8NYmsIsSpq2Ze76nvTbkRyWKW3VJu6ezWwqBy_g7HD1ZzI2Sx1ylKUyzmYq_KStbKMYKyxeRwPzJ_80KtUOt283lC5if0cXsBPqsoEzr_6gDWxPRnYlhcA5maxc2MPVS5jBZuvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyJ3G4KbADc7dhrSFWgjL4p-DsY-uShijpgT8S25aPDDlYeVEvVaz_VPpeofY6rrKrf8ZOq9B5Tc6pYK7HlHJiSGnXNL0GOXcGSybNDyF4BcO3mmVWy8C7Mm-lswsFb-GdhYZoxze2VIf56Pv854jTP8RAOaEmJeYpJzyaAV_TsBda6vnkX_mVjxdiccP-wG_rkIv0TsgR6InCNiAN3ukD6ekyZ-Ne1ND6iMOdgYply6YPKGP2rJP73ePh5Ks69iXuTfiO632QtjEA0T0rMR35g2pPaV0VS9ocVXn3U6MK1GVme6WVCNdxb6T69DiLyxdxvOoGz53Se2vcCSZvHiRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkV1qrtF2Wo3lQMP6rOz784KGXUtFhlrqjzKc5q-bART4hnUn8D4bb6bOuY4CpSI7mJcP9_65NeTxK8RkFNZ5DENEHhTR-lL2zNFktV8bTx3a7ZrGNIdAAJrsALn1QZlhEoz3_RGeLdkUAcBiORnvl2mSs7gWnBL34eMI-GexF9sYoZtXFr96T5iG0SftHzfiG7Y7_n47B-PRI2KKXOE2KjISUJ3MUiwCpc2vfv5AVUCGJ1u4o569198bL97jBHUC6iTtqQkgG6b4EXOfW7gA8OnrkeVaeD2-dMlkV6CweAjAYIsy3DDzUb-B3PAvggK6wG-mLoiQmbzJTwh_NT7AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhrMx5BM2-6idh820GE2LfbecisqACQMbWVSx5WPq2g0t53h7aJ0dj5mGbC0UhNjsGQ-vjRISgtF0MyHYBL2SowYH_YoklJJySL_jQwiUA71vpdXItR-jclxq77PeM4nQOYASh5gUgaYU7imYx7Inwb-ko1CA95SqHvjioaBdgze2g1bENydwQhWPc3_Btbh3z5Pu0pgXyvQoAsh1dFKI9ujsbBvXGqbiFUw3gHR7PSo6eD9VHIIhdY_HnSu6HbPoTLDq8hiGR3O0S2mCG4-9KKbf8TZL0mgWlpm_v4nNyNAE4r3uZKz7fJk6Fz1V3DuNvKaNbggcO3qbD1dzMJluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT0wbdfAPh3qHQTmcNJ2u_HNYSp7SDhIBGHPnva9WpS3jc0hllWVelgcJf67zpbUoVnjN8S2nwRnx_8ZVS0x8X2ElmOhFx57nYnDqhf4cWlpW3tvnsehLG-Zl6fvCtim2EuK7UqPtHNxuLzNf-Ekct95UUhnoaOYHDSRHakt9pcF6CW7PnFzkfJvxMH9FfzMOUxDGRXjxyPNkZ9QJd42l41MpwuRaZBWHiJTrgT9QAhqa9K3S3pN6DeeoAdcHmvPs1uHjESgvNqMEA-coHfKPvoTSrm03oTkMl5jdzxCesFxkCXNnzkm14Ct38Z1gZXOYKUjEOgk7BT34CuTSE6XMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zsp8bY-zbjWh22GacLh9NJRcbGwIov-Qfi6J1Cx7lqS5TmtmdbC-jk6KKGrGok_n-inYGWJ61Wo5RtnOURQmh8opXCxnuRHYAJL8Rd3-Wd6t8Vi4v3hw17U4ye4mw8CD_wXcOZg0vIyu_bg1xFbdTxNaD3Xug5P79WLrPWoj03u6INl_1AYP3mI8Ib8fy6v76sZnAdHZVe4PUTX0BSbdkTCYW3S2YVcrQYuW4fYbuI7Xy-BL0QxOSA-bPlAgcYiM-N9XcChp134_ivYz0w19sFRsP0H1MFXkRoZG82q79aGXVaWuYU1tqTnRtFaQlLRb9_GlJ6ozC3PPSbppbM6J5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfJJitjVm93ovU0NszxSE1HHhPlzs8isjn9azAWLFDUuYXLnWMwYDZswnWZ-9COF886_N9-iShYy_pAI_VxoZS9-eTQCrDmjdsxC0Rq8fJp33NiJ7bis_spgpVplPLRClGvHMpbsvJ8D4A_OvrOPK7ixhPgpZBgH4ZEDONAhZQZOB915--tmeWBJ8PAE27w22RfdzPkzcjbSq4X7_2NgTgCMhksRojAhcycZ6R9ANYa4bva0gYB6FKMEyWi3vlE2_oZl8CeAslaA294p_pjWn6VQn1ea3G79rCncvIoZfbGU5uyQr6AaXJpPxY_3DvquJGAOd9_9Ii1nhxlyJiSMiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUBXRpAR814zRizSRpnWMKwwBbFTWdWQ0a1dFMOOgfhqkWMe2AbEzYNS_eZ_GYMOcyZfjhMLz8FyR3_RZDlv4hh4PXNzQ4qVD9X6S4_JjK4K_aMaJIznZOjQ4FFP3rEVutQ7yRBR30lUNH5PgqhozX8Eope_Qw4XINzX5bmM4drzPpjmiJwlX0r68dq-SqPUy5s7vFd7UtBh2S8nuxd7RgYq-rRbLJou86HnTuiL5D6CYur350RND55qLR06wkq7jG7Cwy4wfeFfzEzZfdXtvNYXW1U_It-mnTLVKB8uUtOpQYVgeV119PiwMOk8xROWLdsxO5gWdQscwRq4LAgIpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=pYTkgylX49qslLIMQLmkCCGfCcJC-D8-N2O5wqXy3dHfL6OwZ_MCqG6WWrk3gcW4t6Agxgb2q2w-e8dohvf0c5dVkoSeK2n1t2_0dV-lRtikTvQB-BBWOk2T9yX9_m-girQNOcchyCNf9IxsyUtNBWd9f6zV33s2FDV8_VnfTBOL1byTqMpVOUJTh7synB4unI8X3cT2248fbz26YxyhvkSgwrnJtJyfhSMqbDTVFjcbfQg-sQCPuO9rYQ1__jj2hiV_Om44yau6pVgfC1QTRZrEtmU3wxO6WAY-yIVRlQLlHQv9mKltTE1vVMVy9EdemNTs7K3wRG9RGC40jz08pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=pYTkgylX49qslLIMQLmkCCGfCcJC-D8-N2O5wqXy3dHfL6OwZ_MCqG6WWrk3gcW4t6Agxgb2q2w-e8dohvf0c5dVkoSeK2n1t2_0dV-lRtikTvQB-BBWOk2T9yX9_m-girQNOcchyCNf9IxsyUtNBWd9f6zV33s2FDV8_VnfTBOL1byTqMpVOUJTh7synB4unI8X3cT2248fbz26YxyhvkSgwrnJtJyfhSMqbDTVFjcbfQg-sQCPuO9rYQ1__jj2hiV_Om44yau6pVgfC1QTRZrEtmU3wxO6WAY-yIVRlQLlHQv9mKltTE1vVMVy9EdemNTs7K3wRG9RGC40jz08pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m45jPm2gkhMXgFbHVJyUloj8fPS4RW2UCRf6c5Gd7xH7svdpDHO0QlXIQrykKhIDxVKVWujCrHr2OLguz6nlFKT_UT0oNVDU0Lhg5z4aKcKTC_y53B7dbcS853Ccznt59Eh9mRfrnj3Ls_sLMZq9jAQynDHp3-YAXUyEvVcDQ8DyzmuIxJQAmRusT1icmw5iZx54qLVkdJ9PNVHcRhYFh4q5MQNDcrEaHMqaY0jxZ8Ga5TIILOH46ZLFgbISM-LpQyYXSKgf1byhnz57Gk5vnEs0PM4MdSTMUKZTN1fYsPOktgJ7qwMhC57JIVdg15zqpeQ6xeyMplRD9iIGJM7e9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UszJ2P440ir6JNtE9tzIjgv9A_pUHzBcCgH7_E57CUp9DGBrwhtrF92Sn55UzNh6WpCfAayPRJ3wWFKgD27w1Tqz7m6cpSVJMd5sLsCvtR4lCGxzKZ9bx3MMcdE7vR-1OJfi3lks_Hveh3p123BLuj_s4ZEmioH-Zok3Le1XbaTdWpqn4wGBlTcecoPEkAdSGNjqF2CbCYUX6AisuLkGYu9P9V3xYaYCraKHmjA6LBcq9DG7S2Jmh3Bl2BxHl1lKsh4LryXDtFuOaTtzuMN1fOBh8KtIRvxzeeKAtzt8lt6wEA6PEZPCT5up2fAH8B1_-UdnFT0cwjSS5859cAGR3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbnPj5fqNTfKv2xNHesXulm_oRcpozvlUE_zjPpnNOmELvRM0PDb-GhZ9-sl06ZVh74OesK8ko4x0wGKRVyDrwxVjTdpHDpKrQO_g1h6r9gUX4mSbCp_AognkK1IPfa4Cc-Cc826NpUhQgxu1qi6b6GZlOE-59BrhSNKKHWOFL5vD3AHYl-UG4BAo9mXhAJ5dYAozmHS6P8Pa9h8xg4DE7B8V36HBgycS-QTPJBHcAfZ7KgT7zsRV63Wk-fdNsam8rb1flTi0fGEjGs62rWy36zxkH-HQqQc_beh0hMe7Dfj-ELd1rQrFvXIEegYslCt0wlrhB7YyL8FhWfiULrb7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK7i6oOK9mBIE4rQsycPOmNXgWsVB8WWLgHJst9_SsLr0Tqo5Nj8ddKn-_oI4ga58AvexxWd35qfDbWB_49HfXXfSPW10ixXm1S6i6IEF930RO1qquT1C-l-lnqxAThk1a0xf349qdHvRLPeJNTUth-J938PrzW-duEujE50-22cH9KY9dpDYztpzXD7Xk4YoYvw47Yq91b4K2I680hUP10KKgopbgGLBZNsUhZE5gfEFRy2njHiSjWXblVssdfmk2g97HVL7x8A8H2chcLsZpl9xz69AV0M2my59SI9wHCbJBzDDM_JTEE70kU3M9WkH4QleAcQauftXf2bnirkqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaOge1rx9I6y4vJ5Jkp8M3RMVsxtG8LhNPQhCESOt7xWbKaFV0Y5bizoehr9ZnqfOnQXtH1-t2GW3lsr23wEhJNj_Fz3dxWtC0D3FCfecT9Jc2J7jRqGTXs7uB19xI0PJVK3Jn2g17mu_uBan-UXjnTSXdAs-zbUD2OPgfYll3STsqoiEiW38Ls_qyh_rKyPgMK5QSvwMprkRwawOsxsmIhDPrMgB-RHauq8Gpglg2aoSfBn3sIZVLKpyXo_27LnS2PZ52Fzx4vX61QYBM2I3AaIgLPAb8H8U9p_WvxQueVIrZc54sFAFMeNbC2Hn9HqbzmHDewWDVG75I2aF92VdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyARaNrlqG4BxHCMxQLCEnyln766AyTgz05nf8trA6Jkz0zzfANWWY2dRkSKa7yNaK99FZeg-XGuJ0ZWYGs2HJ6MmxxAaF-I7HDy7bEXXg_z31oHv6tqZoSvGKaE6y2o_NnXTbVAVEjaADSBcztFL2hfbdjZOXQiudIABG0N6fKKS4BJ-hi9ulr4NxKPk0cVWkQLS5pXI8LQJvYxv7Rj98t2pj_FPl8hBB30iTUZM2OdsczPhoVndgpEYspCB2sOcJ6u_6UBVSe109Yj0FazERA0YBi3_wVrLuBHB2ulBr2VtSwALL3ps0Ocy0Xb0n1iLyaCJISdy25y79BhzEdTow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGWNfCBtBpaDty3JD100lqJDInOHtX1y8x4qrMaz0OEFgPB82XQPWhqOhmO29qCccUP87svTQh4B1Xs-7B35ki1YJMZT2KI8kRbmBoJTC4Y5Xvhl7_fiAWlCIaB_tUmUFo-wFw6eVHMM5sTONEmlDvhzIcj3F1OwFPvOGTRJzu2koDQCzomxpuRjdGvvps2sitsJli86jeN_Es_0TqoHAg5lgZ2F_lVTjUs0hiGK-UsZ-GI2UjzZXp0xfI83EJdFhmVRFrDO9GzgYAOgt0UjFXb8YcIdKH-MrXPCMvyzQJWvtEkPWS8EEV6FTil_-c4vl55trR9R0JMmpCl5IIsKhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecPRJZA1XxLbKFDCcKlg8XgEjXFKcr6pNbb_hwXrQ4BFso23pUqj738qjbGEIZy9IkiqEDet5t5mzTGjeJPBYAIsNziYCReuFUhm3y0UarIqc2livyucoPuPTSMxTnttT-CpEcge4opo6DjkG4YWX9545SH-xbQhrGuwL1dAXjwxOh7uwHfZkT_Eg733G1rfD2S9OZEu08sKZ0y8CPqjtCvCKNMYoKS_nYsF3Z_ZuphHDjsGVCGd03AyyTKwHAerpyQSKWfwBQQr-z4t5C3UubPFrBUagv9oOj77inQlDOOIwDhTYMEuT1t66x6EqzTx7de3UFdX1VwQFi7jeGJpAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_XxdeeClCtSoTnNK0ESy3__P8s5xCWToHC7BnvtzMBPGZRBwA8ftyg0Eon5HfW3DdDlfEpRvxbuWjskSwRUiB3o_6e-zH4tM5JuVFJQxKJIsdzd8RD_esYYpsT_aHTMhZchLvBhuX168m6rA4vnRN8GEL2ys6QzxVMq1JYCi86DDOPay79HGoWRtE_oBCElIYoPluwJez9Z7xS9Tm_IOleV9rb_jmHdtg-HxOES1U1SWgsRkXH3OoaSFI1L3bvC71fwLMTwgUu5eOnt8X887LF7Y0Y8O-dMvS9iJowLzI84eyTWPGcZ2fQqck5NVg-UJjX0gP4OjPNuapMGpNRQqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PacV6JotDTFF3c_X0umKrv-bb0e9aZWon29JV2NIdd4acwxsgsw00x_hKi-agf9p-ULcMugXTEwM-sOR-7FeC3--gR6JHK0VYqv776uWyw1JP0bgz6ZiRgVvJpUpHxLs3DGuvZpe8Alk8U7LDVAX52w-uqHgSIG7HMy2HU57GJZt6Uqyyac4PvyiCJGOd0gjvVgNWcaOC3uSOtZoDLUA160NT1SL5n-OccJpoElweB_xe4rGo-AoVfxVnj_7PVxngRxVEM-WeO-TzUMzRvtYf2Auc2qJwqMKSRhMpdzeyFoQBAMD9HrzwO0iZi548hz7oAFm7gwzeRHF5OLf10ZRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhtjTwdhZt9Yv-Ygdmn_DCdffeU60BXKxWnvnfX33BkrnA_Ne4wMJQUWY5LWbx4IOg5YkxVwWIyZhzJT0nkC-1ddxQQ4Roj6jEYsOYFr1B9vW0H3G3P-38KotQGm5Wx1qRvh1-AGBd7pk4Na33xyTFXLUi_UunZXExUbhzY5xaDbpoC69ZWiFIKtk9vb2hiuTb3FYm-aPS8eDg58KykB7HKwTWOMBFN1ceJBim6BlsyBIt07s3UF5FIOb84jRR-XfwHaDVxF3Bw8up_x-D5xXAn6aj16MgfZQ5Sx8WdJ2x4GFa9o5B-hKERb5jOt6uJQFkv0JNvpy6UILf6FQF5SnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSBhtGV_Kp0ok8zUV_t4Nb3tDTLjIE1DQ6MSdzxsJCcIRGK5YV8oiLU9-gZpMHZNW9d5mB40vKONaDpN_ph81EeUP0Had7Ke0A6Ra698XJl-fRjBNhILcH_s5oa2q1HephYWIw-c1VxjJ8CFNMa2lLi5SIkUjeQmoi0tf15lp9y33Ce-wFUECe4AwgvMMh33yv5p1ZsTUXh_sawfoFJQEkEUxgaGq15L6oHIhDs96Bo8ZR7tQ5hQX1iHmOO6a0gBPKigF5Y6fY5n_7EQKwCdjiUwEWpnD4Fujda2cf066KPilOJl2z7DCpwJ9dUQcs95yxIAv9XqSCi1p7pFi-O90Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM1Z8fXnYbs4rGK4nkyYu4qH4Y4D43wDdESwqV0YXzAMIOXwziziDpwRFd8cDoRTEm7Aovf4WZVJYQwSx7pOvbN16UQU13vegCYxRbqaOHXPa-kLSfOC44fnrR3u4Nio4N7Nq8FKTH50Ka3RdKIEjT8xLLp21EnI4PgqJSnfhqDvvx04DRUJN78jjSFIHYl5v9Azz5P1_wOKbp7vG9JXi-LqkqcSKusiC1qGz9_jWs-n3X_RvsX6doYairasitLvWNMBJK2q4-48-fL86kUP2ZSDGyY3qlXjvVBH-NFju8Woyi-z9S52iBGmZhdbihCRny3n8qhHrUEj3FECkx5zNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdkIY3O04dMhnlECgCeB3qfvoU8XAnflpTmCaq5NrppDUj9ShvBZDe0WI0ewIX0oWckUL4YxsODIA_poBPmPbM241QjdrwFV1SErCaxsHwy8Fsh77p0Mvko6_REnEyoBFir47z-FyQLdMfg4HBtO0lKj36oH8444o_-8lamHNH8Fh4pP0BgrXnejAN2dLc19HRUZ3FK1Cd64v_RawS7a64SxljPXBqrPztIICiw936fUJlZRhx0e-W4r8N03v1Of2k3EpD798P2TuTXwJ-nK7-rD_CG2vDTei8jJLovZYqHsv6Fpg7J1p2h-WiFst5UYr9WuFinTfVIzHqxM09QPFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snsJWpZGA1OfsPt78GaIwroXm9no2B_68z0H0YgAAegN16QDg_tOiMUq6eCLKF80OhHE-AFYK8v54iqOx8BSy7XwbSskehPO_bKNdl05dInUNXv7iDixOwehDxDADbiQnwA8FJUvQlyjwQdS9IweSAK6mhKjW5BydNwnhioRQqKxWQEgkJE7dBHS1iZf8zhajbM3E8dVnNRY3Gxu_ewWXbuCKd6hh4STr11P6q8AcjoMsNfX0eExQ6TZgAmQwGp2u2O7EWQHX2Bnwhpy_sZSJtZHRqPjAY_5sgACq4neA0QFJwIdOGCFzJE1OVsxfYr81B6HBxp8ZsUUeTz80011cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx5-3Q79w6LMtUpqSMTfp_oF-PTQnOZ_E9k5nQOJQ18sBNZm43CSAdI0xZZgZl2HNfs-85ZxK-Zn1TxSWgdHsQCzZK6C_WKqqtGZpEFxdhQu-xgI0lqpG4iis7fUGk3n6j6er6K4FFplVp3gt5P5-NOXwScroGDPw8KlusBzftTIM8RhFzDN788mZ3QZ5SB-NiOl8RDQTDc4XxzIkgBc-Nw702ISd1Mptr_PcIqQ-ykQIh5MkcQHQ6OMm5g7ZmBZy0M1k1V--kt7QI3DKAjobB2cYVaq3p1VyvQHK6lXdueYQtMr9pK7SIUtvywZPNuBYMonu-ng3QF1YuUyTv-elA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1E4nm_7PeqV4tqhWYQcbTs6Ewx3C8cdruwIpQyqQ-kNKXqZqH0IJZD-_fnRwex8qSnAaHDi7V8SezE3qjhQIZ3I4F9WnQNNUZAYQ9U2Ox_833jdeU15-R4hIHGx1e58B5Tww20jEuqLefKG8VAQdpJ5qYdepBCmBaf8ObdFu32yrybps7C6_klWoKo1NCIdRISk-5DGF36MSeVG7Sn2gq1QSfI65J9UsACSRys7KBIx8UZ_k47jNOFnLjuFZafDRLj4n3C_JlSYPTDmygSNF8AdiSPi702F0RrJ8vaLq0A5PCnB1YkeN2t8EZ0NSPU4mf7yOh3y2njgFElnvQuiWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6xE2tcoQNgXU_0JUjuzEPOXqKnKAy-_6A2rX0AOAw8gDb9avQxo53Ns8ERoXVaiu-z8-j1cmIa4QcfHoAG_nC16IOvdqIs-ccR5MGFatsaxzhoE6tVy4Rb52SXPDrhLT6sHfQ9xsytv2l8Wi6kKE9NLNjWeXmgQvSjwysZxFJpP9vkWTOUoABFN7aDUK-gNt5TbTvm39rQgk2Oc-UdSwLT2N-N1QHZG-OVbtmw1DdXAI_Mfa6_pJMgMEH5fYdpKP4XxSfCqpvTjROxg0kresDa4rNvix5z77s5GF2YsOkoPfEokwskmvIQpa4Me5rH1-5ocK7vRcsYAHtk8X-Pahw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jot1m7ijev6SZaojHO4FBtHwQVHF8WBvPRruAka8km7oieovjcnooNr-RQwXxu6ixfc2GwHUvn8iBYvQd7wniRps8KPO6tpCYvLzzc3hUKg9YD2ft21CH8l5nV9hBOGIEV0OMZ5aY995kYg_XS97kzYil6lC95NUrncIsaLrOC4yMqO7fztjqdkWGJ1u3v6Dsma4sM3TFmEniAQasyBPrhaOB9w61n309VlTlTVhcbHaRMQvPysDPydwwIVE0Mw0PZDgbH9cGhQdcwT9ZcQi8bqESoI-ZtC8HduFSGzQF8T0a-42QvcL1Pm5ggr3NI526MvB6-qb4MX0fTepa5ykjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrKBZC4uoXrUYIydFjMzGJds2DtUiMP25led3ZxOQYaHFl0f5gmyMzAdBUQnN622HCXELX4tINJ40MipG_USAq1vQI68rnx4CiTpMaUwgkhSuZbpuNTwTvCQ5MIgazANASh-QEROmfOtxVoeJPlkGbORCVE00FPAB9LVQuV0KIe2n8Y-ChxFD5QqssZ6Q7IlDVdNAcwUARM7adzQV337rTHR8bzffgOOGh50KydW-4IgOWSl8pzGNz9RNCl1HwWvAyRC-pEhRmTd5ROxiJWudC1frWNFkznyrs7EumlYiXfJF7Tcd09jy7wBD3HzFbYBUcP_VkJ92XtCzck_DBWSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AU4dcsxYAXbq-FbUL3q3al-EepJSpG0pF49S5K3OLxJ4jhz3eeVQo6CwdYLdl4ryUrsosH8wdvfZxOhiv_8iLFi5Fezv-7Dnu9T3bJdqbkVxatFu0ptKmSs5-BLMm-lodAw5WAw2nFEIl5h0FfdI-I9Uj6sESQk25K3I97WVOhD3Qite33PD83VEPd5XB-D1IlLYNZ4GcJ_pZAh4TXS2s9Eq7G51R53MLkH1ee_vwrjkQQe62ridnKbgHSkEV8Nf870IzsU8SKaXAYYaMVQfzbGX5Z3n5z-G-MrnuqcRpN3cCSuGudfX6FVvogQAYAtYFBhsmQhChhw_maeqrQaUAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=BKFvAjCLlyrzkNh99m70D5UoVou9GkNWJI_Ubj9e0jSZtx-LFCqdPyDJT6PJkxETME-lFYvPbHh3fxdaucXKv0Ly9QZTErWtIaZvbVcpEtsQqPTHZ1xTAppUiDec8ZFJMMx_Z0rguedI-LNkyEZx_m865sgmj2a3XUrvnW3ZHONrZ_9MewcGBZaDUqSSUxcFNI0Ugu1gCJ_H-X3Qt9dUiaiENbwsnxzizqDPbETbZYFbLLhwxCv_q0q_7lQvQwRnh_DKzFD9c5AKxDGuS6viLNc6yOM9JZdquMvqRDSLtvU5110v6-768D1d-EH_tH3S2FMAZ1MJmH2p9MBoq-w47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=BKFvAjCLlyrzkNh99m70D5UoVou9GkNWJI_Ubj9e0jSZtx-LFCqdPyDJT6PJkxETME-lFYvPbHh3fxdaucXKv0Ly9QZTErWtIaZvbVcpEtsQqPTHZ1xTAppUiDec8ZFJMMx_Z0rguedI-LNkyEZx_m865sgmj2a3XUrvnW3ZHONrZ_9MewcGBZaDUqSSUxcFNI0Ugu1gCJ_H-X3Qt9dUiaiENbwsnxzizqDPbETbZYFbLLhwxCv_q0q_7lQvQwRnh_DKzFD9c5AKxDGuS6viLNc6yOM9JZdquMvqRDSLtvU5110v6-768D1d-EH_tH3S2FMAZ1MJmH2p9MBoq-w47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0eHvHslePuLV9wmtrN6vpXb2PgQMfmlWm0FqNY7a9pSsrmI4F-RnOa4L7eBQSjQxTEhiiK6A_glvlgmrmdUxX9a_YFlMrP93eM53GCrNU1bTo1epI_xDidhBwBW9h7wKfCDRxHsAVxeB6IQwsMK3-YQ-5nw0yzkokGQmWXsUpv7Z4aaFWXF1E-jXt3YuF3uqfnc3x7P9H4yIjjsNHrwHkvMK8DbzwraQdc4Qmb1GuMv_mqBhsls1xWnQ82DyATo-DnmY0HLiA0Lblxz27FunRkpGDBoj2VaV5MknoYThgnwrl14RofezNVjGAn37CZ0aqjf7gQAHTyk36R9J7Cp3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPwMZJrSfJPk_awF2aM3xNHO86atU6xQkbDQBOXLxSCj_jvN5_bItW0uxp_96Yd6t0LxEYVDt2mSGDg-O_evB5Kl298CHbc5cKXxKKTzUDtLGFCwEXRdT8Xvo5lftEn8A2ncxWs7JsoGu2NNmosROGhfEXPfZ9C317UOd5LvVHFkH1f2z85DJv90r8nign9FIeg4tDE2xNo--SYuS6xQsMwG1kSCL7UyeR18HMXUxX8p1YazTmSzWh5BUdxKfesgTAor_lwRo52k8_N0ynkVCsTSSEEHU4AXvyr1XVZDZ-NABnB2XSnzohHYMJodIYohGPrwHfR0wpsOfr7Zr5tFRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqbbDb3AMjb8RjwEdZz9Q_r0Taw66z1Eip1BZ9cG-5i1zOIKM0aCSfMQSC-QxCG63ZSkFn76SP5OydRs6NSSF3YR8NlG0eilmPhCJ7tCvEqVaGtvRk1L5fPqdK4p_whKQ6bNMqddPyl1YfcfqXGny28IIyN5DFwNqyKSxD_SwC5Bd2mJeChjGvxGJbGfxUeP5j-OF8ZyFa1Vfo3R6OgkQ9mH8Z8zFumtUTADbUwGUFLd1_FMOiFjCeJSpz45jq3Nc3gwhjZuKh3wyG1Qzy3CvTov3S5GcKWLZ5wFPAircvc7xcUJuCTromF9iZXGVKzkyGfLTYaJdcUhsqqAxjXekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=kBow5vcZyl2SUkyl3bsgsKHJKSPJjlUkZG2gCuS-SjL8CmD43CWRmWFHh1S74o3HhOF0FHkLudzbHvkfsqCdSPAV5rw6Exd2Rca00pqlLdFzVWNhMHUsfWnF8bd0RuA-jaj9L0SkndiORZb0OWT9WxW1BNQPOnnCGuz7Wa-kjCfTexwdO88PeWaqiRdWStH2U9zy-IOiZ93TjgA3nbPyeH4fbKNuEl--sFkMpD9d4kr6ntYN7eBWoKcCpAtUfuDOtOnRpuGWozuPM5UX0K5VnJdZQhfedVppJtLVD8HGsb7cimfXHkjgtllwg5p5ITxqzvIXZVe5JJQjscQzJ2NWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=kBow5vcZyl2SUkyl3bsgsKHJKSPJjlUkZG2gCuS-SjL8CmD43CWRmWFHh1S74o3HhOF0FHkLudzbHvkfsqCdSPAV5rw6Exd2Rca00pqlLdFzVWNhMHUsfWnF8bd0RuA-jaj9L0SkndiORZb0OWT9WxW1BNQPOnnCGuz7Wa-kjCfTexwdO88PeWaqiRdWStH2U9zy-IOiZ93TjgA3nbPyeH4fbKNuEl--sFkMpD9d4kr6ntYN7eBWoKcCpAtUfuDOtOnRpuGWozuPM5UX0K5VnJdZQhfedVppJtLVD8HGsb7cimfXHkjgtllwg5p5ITxqzvIXZVe5JJQjscQzJ2NWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DP1IGpgFan9SODKvW6VKGrUD5IFl_jPDv--_ipJUJTGSYBhDfn7wahaBAhbJJP9p_7h2mTTdeWtovnxQiHXXLgQjAemiTPUL0Iw26FvMzoNCcCeQmX7VN3XEiaGuc8jld9qfNhr5z4meJ9xb5zdNf5YzNa6MrIwbgsGtrtoFDGEP9N_x82l6Ham9CGnLiYFAWLS1h_5Uj0fs3kzlNEi11t_KCkzp4f2aNQxCJvz8BZnMQEM1UUlbUuO938pFDZF_V8pSDgaHYft_1VHBp84XcamfV_x3JYajpLZxC-pR_km76G93R5KRmcSYxcSKMvmLwyGkaybH8EpgO89IxuOB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fz2SqLU0XB4eSNzVAoRJABxfry-53WDXTEpFNWFp8q6GDW2bwLYCHbflp7Bj9CrhlxTyHgZyqaqACbhMZz7fKk-muKqUQMUQ50DWq-S9XbeT_QWdu1cb_fdL7IlAKsqZueM36hZMw0_sjnxqjX226D3QGHUrERMHcDZa14Ikx8CDLcu_HhcZHskswtslg5Oq8PIPKpbV83cWPEOVCLXEEcvgKcnkcjbOdBi-a-4ztKaQR-oPYYnI4HmaTFfeP_6IP3awogkQ5MmtgsQuw4ZZuCuCaRYMrf9UWafT4xpbt_uQxGT6ZWIKxnsAfFt98JlB7l8uVMNmumkEw_Q2U4iEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KA6NVUjh_PsQGxTg5CjqUPxjGxFSidLzcsitHmpVmCUJ5VjGKkJw2Vdh9PKMnZTvAGHQmlXqjN7-Z9XMQJYGa5gv1Z9S9MH6wcOqSBP5hKz7TORHt_HYcaDOD5EoRW45g7NXGKXP1cQn41oQdVAGK93Ju8BbLwL4qtueeAFl1k6uCTFPFshwUErZ6mSu1_xysxoDRP8pOMy95zWqtVXT97jwRrYKrrNOzXKHAgW8fikiNR8ZHhvQ6vag-3G6b2YSeQvIAzwVahLR8jGmHV9awY6pYXllrHQOf4L7MhrDzlr8FkJuWlAKF3b4YMnujowuDtWhpfj0YmPnkHV21Nn8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stNSJETFod6q9vyG4Mu_4-PcvtEz9h0PirOqfxCBaPVrtfJ16Pu4sC7hOcNKLXp0gMMMFipz7VVrgw9CCwggLzwBNjkytUvaObEcQ4i6uXoIdNPt6uMQ6SQPL6cHt94kjP6YVT4HrVFAspaG2qgUSO4xQqmRUxjJgdB_icGkDpJNYRW1rGf4YBFDZsWrilIv5Ia_C89wiUN6pkvGGW1kq2ZI4q237VcEvTyXvx67gRxhGYZOrP6vGs0kTIyckB0vgTh4kFUQazfwwckkX7jaC0Oq7iM5aCXGxUeCWSQbEBkfJX3lSeCPpYqhQUzCutIXob67zKm0BOJrP-syGb3HBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKIIiwh8TozYUsftFPJjdPAJJlqzoyWEqkvHro3La9ARexKd-5pUW35H9q0qM1taUsXmrKyWbDFnTew9A88IRRz0_C7pP2sqxM_McWQwN_9_21vxXjCO0KrO-AoKZA2DrmYVOvSsrL1r0MJnrvaXMcgcnCHFlgewrBreEu7Ny1_CR5vqsxdmSnuPznL12Vy-vXm0qafXzp-uWiO3doiCm6bhI9P10dMdV3neWkpBKIkUOWCXNbE7GvOCByMISowXG05V_JiB8_q5u-nQilWpdwFNpvpMLjQt1RVkhSgVuLqhofJVz0Lhbchr95SU2XimaXSL_KMuESoZgZVe4ROkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baLoI0pJFvkpL-haEPWU_AMF5KFvnWUPIb6dccCQsspPWmjJ0Yc4RvCz0Vir96dd60KGjt5YLY5mH7wmzkGnZ0Dhv-xJLU13VTfAL_0pWiSIAEcyNeTZsR0UY9q8dORNFOovifryWEpGwC5CfoGUPIvR6fzaF1PcbMMgwpRH9suxw8buiVxjw1LR3WJwDOBXQ0sPP-IlApIGhFc8n5qecB3JcagFTjqFzUNCBDLg4qPAAkDY4sb_XJAaWD5aAxWJeEdJDPZdmmyBXPKMj1RorTuk6EZ5zp_WQDLwV1hqNJljJZpg6REM_blgorMCVWzJIB_l42ALNfZLdsb5NTZZLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uexx1vGNeIreFmtNSG4dMPEen69glVcRzTGqewg7qB17UyUkOZcEtf7L273L46RPLnv7MAbQc1ELEiS89OfZy_S5xnOek2yx3kIBJukKr0ym8qB9VB_JckSWJ631rUkxnxwj7gyOKWOg8UuTqXsVJLn6eGorslArMlpT50hvc-TWnJVlz1FcFL6j1dn70-9xCgUkqOfnbcD__w7IhzXf6tE8TZ5i0L4cvZli8F0_Zu6RZ21ttRk53vFXwHFNjJYPLtH0nRH9UKQyVWQ1X1q90A7EHSFd2qVoaeP-Gtup2Z6BIyQ7QfbDbP65nCWedAL6xbLVCtINZZNC1OwrdgPNlg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=Uc4cxk1l5K-7iETR3X2hV1LSSVcFg0ZTm7XZRTQaG-2X-lSBRowIjfoc743QGbXWSW2YY-_rPA2UCHi2FJ6oGFOKe-Z1gXDyXtbZYSqO6zJLnZsd3Bh82nMJfEGCJ4MbeaWN4B0DGec0w82YEMxRpylrIp6uwjdyahlvyi-DMIag1iScxUY1X7cbeDisuUnVwaREuUE41iB1UpIXfWD4QcPBjcN70xcCzKqhVQIAJwlibjmnZaWwLgpRpPR39zHrtsvy7cRplq-vX5xNCHveQFje7EP48MpFP7JtawngyFu4_G5rB-uvOoSCq0coFA5YuomB5ZipLizjPXGlP5s1sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=Uc4cxk1l5K-7iETR3X2hV1LSSVcFg0ZTm7XZRTQaG-2X-lSBRowIjfoc743QGbXWSW2YY-_rPA2UCHi2FJ6oGFOKe-Z1gXDyXtbZYSqO6zJLnZsd3Bh82nMJfEGCJ4MbeaWN4B0DGec0w82YEMxRpylrIp6uwjdyahlvyi-DMIag1iScxUY1X7cbeDisuUnVwaREuUE41iB1UpIXfWD4QcPBjcN70xcCzKqhVQIAJwlibjmnZaWwLgpRpPR39zHrtsvy7cRplq-vX5xNCHveQFje7EP48MpFP7JtawngyFu4_G5rB-uvOoSCq0coFA5YuomB5ZipLizjPXGlP5s1sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FonViT_LeCdpXkImAuLPuX01jo-mby1L6iC2CoZe_q2Fym_jM9fT2cLE1EfCRH1pv-YqrrQlGihHd6M0N2NgY2feQaD6Kl7lKv322THZYuU-yR3PyIpODUp6J7OL-XBerIa-dZgZpGnSSdysaYEv9teCsipKslu1wUT3OlWLNh1qAmDrg2880Sxf2kmeIjMDLVw_wmbnM0gHqZe-IHE1EpjlDRE83uL-OCUZh0lsXRik61kP2DEd6Uk9nCUG5SP505J_4Nny0OnSQdkHhlLZ2chCOzcQGrXB4icHFPi6glnAoKU9rQpYVAxgjwfWXaoZmUeksvpuqYwaHcy-YNrO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxIPhzC01mtYGASc9dsZVUMznKQaIQx_d7fpX4y_UEpG_olW3-wAWn9hJlToR4jlSUwbtole9cRWJO71Y-IQfo-1zDBPLbiVVabxBM-TOJPakVpeeZwHuGv1CAalWEyp8Q40P46dMY8c6yJju3d3xC0hNV5oeM_lgfGtbjuYPOWMZKNkeh5Na0KB21N2OkvpV883o5kUtoURuf7PfnpRMlpv9yXCNQIrjtdb00c_QThAowoVcxMGlAl3kYjMt4FCTkVWL9nxRNDkh33Q9xr0wBt9WBkNq0ypoW--LODMFh66o2bTyJ8cWLJSyOo1Yc-OZAhwrddrJEZoGI57S9R9Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK4VB--DctqMaf93RiYt8w5N8So2kMes0RyytCC7yVugWBZt0dJ-uTegKEclC7196-D-qm7CtJSlEaBf8XyH-tYU5uVQQj4AJncr5hWVsbnoL4v_yJIn4bo3WXYwaZMvUQ00WrOzTQ506NpxpSgmi-sxfFrWgugcWKAtYnFZ2FJsLbFvRMl2bE4pT8sbh2CVbA79hL07sdOVAYvorlFE-20Z8oLsEQQ5DWl0lOdh6LTJJ1fboSbXTaJLXC28_-kB2OiE0TTqrVboaEWkjSAJeUzjOF6UDsYDrm1vl4QVRcM4604keDC9XblcaWKBPsI-xf0-4UifAqNE1dAcbA-6Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odfBkoyjTBWaMT0S4o0NBafsNrN3hiYZuxA-dQA347LQOkTliss2BO2okrVLE80oPjhunL_ZQqB91xu9n6AtfutRcZLzwqxIYHm4WtM4DCtTaXclCgcAMeLSNvFi36Z_Cs3GgfV54Ettp-JX4gXDSYTrtveAOPD1Y--oRDkykxJ8j1Ya7GBY4Lf7MLDAEMAZvWybf-BmHpr9fDls8rj0bjin78-5fsFMtdjiwmiHocOM7FzH6o8bwM4TXFdTB6KCTAaUEUVGi5Fp6GO1QmFovLr9aoIKVzoGC0Rt1ylbLu2nK6vdyD6X7ZQl_OFXarSKEbrZIvKUPh9edNRhgDLUjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqvPcEVyLSo_djajkI2cV84yerK0H7RiQvunlaRE3VR3CDZJVy9OAdDttM-dR6GR6cClPUlwEjf4aguGT-bJR0pASDNNoyvwpRK8eHdC963nAn7knUPAqmCfrK6jCRrj_ziN_aM_sa9OGZvbYy7REw8rgp4KlZqamkVtYCdWxKj-Me2ERC_gUd2dm3tV5vK0jJ7NM97bfj1XgzkKhJjz7ArClfIqbjn2yr00SMv8qMWhDRBfxJuudYDuaPUmjAIOKVYgVLktKNNkj2CQA0gYtOg2oNndZ26hoViuY9o5c3omEYtEg-FQDXz-GRuomVaTC_e0oqcggdDcRuqGrxfTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKLI39RAQJ6jZBVD9gJCMtrRyqIE5iYQBlJWnPGoOYh5WzAzdAHEKqVQ-GZ70vWj2Qec1l0wVEMTq9tKik-656wBi1VpKS9rJ67cwHp3tpCpSK3877yHp8UZCr1TZv2fZywtfsYw8UE_qCwU2Cgr3jGBn_PltmxzixzrwwURtXIwg7elCurAIuLQrnDYEd2hocdp1kL8Fm2cEcWhz2nqiT-NonhiBzaLlUD0mi808HHJiHJf4qDNbfWfZfSqMhWZRWdQ1BtglIQrRXyX7uhs7geo4ESipfZ7CP-Pe5SVR97I5I7gbh26C444nicufaZ16zdCweq96J117tOt7wDdJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRBBwynvy16Mn08IIk9apoOLfhGdTZpg26WxAHBqwG21VKWe7t1CHOW8gdUB5Z_-_RKGa8PA3YuERZq4Zkt_SMC1JRNwQNd4TJ9bhP1tegTtM2Uv3c6Nhc45eaVFPPOodnCAUYXzavz875bltl7V_JUZ8wqUM63DF97koWvYibLORVXuULjp1ExzQA4YTvkIDPVUn6i5pTAe6qZ7kYcI6x4NWiGZSVPe26mygyhL3v6u18SMhOTlCPmfsmaKxtJLps2eNqQYda8RCHt0Nh-Npwwjl-VIgLrOp-t88kvHLa_EePGDQAEFhLtWvhH4_pzHBkoB5o2j5BezeobSyEMZKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_-AnDFNJ5gUUoZ3U58Ebjt30K3DyI8FaT3GojrENDsCcQW4Mp1MePaouH2nEhB0rO7EfSlBjbmiosmCq7nUo8sucfAhkgYwyJGXNfnIUvUHb9kmWouYiik24T3QvzVGhRNd6_PaTpR6Wf3vzOwmkgKKcvJWkzAXvBwHu_ZOHoIWUeGGK9TsffZW4AoyM2z4xB7xQhEwdnbUH7SAGIPDz9Ryjnw3JnMnBvpWVdNeZ1SfQGmR-8qPkPUmOc4n-8I6BmOdqJ0BqwLbzV9RC5RJ8CfB0hW259R1EAIJOHQsYbz-pAzs2_8g6DsGaeoxDiE24i86ggoXMQYj208Khh1fhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhJtIhAYc4DwdvO_vy_WnGOtOsIjMymi5AmUMniXbaf_zEFiaNZ2-AYmjTe--yISRFog1Y_mdHUnwvmCvpwJIleijENP2S-afxtnQ5VM1KlAWphwfTClyvTUwMqTCm9jp9sh5ftHwyprG_dqrswCoQJBnOFS7Y3xZ0zvy11uMiv-LhXtG4jTTM8e2F6Gwznbo6pXUiKWI8DulAT61Y1TdQxzPiUQfxHpqUkH4-i3BuIvoSW19VrQbfRkLRD3JSOrph2DXr1u7MhKoLmdoMeWp9tjS5_Je47Z3SwMgMXsdpj-Pq2dqDx8EZx_6gxXy2Vkzo0kIhu92B6wcv1uG_gCUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=K1-vurdpvB_ZBTpXrzN-1OV02tJ0DvKx7qvkU_4gThXUkAHTgkZxHA45yVNXLnracTVVyV1Oppn8IaxW0a0NWsrhcdv_RSTcghkfWK5o_mqwQU7NCO7lyTeGgfNVX4wdWbrcBMmt3y57pdb6SmsAmG2F34JS-B_vx4jVs2knjJbz9teU80RVNfDBmJKxVPKCbvXjeZIF1WPRbED3S9d5ikFn5O0UnTM3BjdMWTVHS6ElW3RbZXrGvzeIRaSVkLtidrlQdyVX2n_l8dd6beGe0tzPvAakoZE-M3uJF98yS7X34J7K5iPNw7Ek3wsSMHiYd8d_FJykUxmv8FZ_n_JeVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=K1-vurdpvB_ZBTpXrzN-1OV02tJ0DvKx7qvkU_4gThXUkAHTgkZxHA45yVNXLnracTVVyV1Oppn8IaxW0a0NWsrhcdv_RSTcghkfWK5o_mqwQU7NCO7lyTeGgfNVX4wdWbrcBMmt3y57pdb6SmsAmG2F34JS-B_vx4jVs2knjJbz9teU80RVNfDBmJKxVPKCbvXjeZIF1WPRbED3S9d5ikFn5O0UnTM3BjdMWTVHS6ElW3RbZXrGvzeIRaSVkLtidrlQdyVX2n_l8dd6beGe0tzPvAakoZE-M3uJF98yS7X34J7K5iPNw7Ek3wsSMHiYd8d_FJykUxmv8FZ_n_JeVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNaGiwuIJAvwh_IuXYVBjs4a3rLOdYs3s9mFtmJHuNeVonSJynbXTTdqIQlWYYZF2JHIWYUKui3mSVDyap2zbdG2QM_CwXpJltJMR-px_MVi-eW3CrlQQlbo3ShC9fX3h1keqp4AxTB1HZZRkAl6F3n-zoBR2UiWCXAI5A3eWfPVlaMHougGoQVECOcmCA0iuXUqT8NIJ8s445yWEEHorO0cQHtKbAncRaecrOzGEYTz1_WemAd-KIit9BIlnrXIYSA0DMCkSxz95bF08HXBQWssQ2CBRvF43Fp2hRiuKW0G7Ga4Fbui48EtcNwejfyKcWft-A2UK5aZUy8lDzCHRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb8XcMTVj0Mhm0qtRXkVgjE-tkMt_atGLr7HopgBeh4PCl4_SiiJbNQCF9rIKawg9hoigr1UY1nHx6r997Nd1PWVPFvX9fnI2dmXuXMRELhr3eu32nbL36PWTbqmZ0cPoesfncZbxMcQLhd4myNkAgN2sYJ1mJBJUPIaEQV29Ksdo3xS7ocDgjwkZ2XtgORT0YBi-UB26B2aYFotUiNr7L8imXhTs9J3kPE117bcMOfSIAnBaHfYsagCjuSJuVyX0zA1CS7hoRftR3r09pf3QRyvdsSNHgU089ZLLao6sTgGEFjNRj9QfYT6P4m5eJ8tsQcTt6APv7pLXyje7wa_rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWtlR4NtJNb4iFSKvN8rFyHMKkZ61QBksaFFFSElP3Qg-tn8ZQnRErL0JB4ZSH8LkHSUWN1XAFFWvhQroP57Q84YZBDIC6tHAy6l4_hUyvVy0iMXiAkWscH1JTI6HbHw3XPOdQc7h4hJG29upNl_9JPVAQB6sBZeQ-9_ZEcnhK1h-1KEwGlKq1TVwPILtEhqQiPAhO5-JZ8hiXjCSGjKNotcYyx8Sv_oqYbwutCJPsrPqSSRspBSa-96MxBwnE4Fj1lbbB5t5s-Qc-MRUD_Xa0ihCA8y8RrE4969xtKuFSW9gLuYzJ-7TQW3DPVCg364jEAh6XGGWHpKFspn-AVMcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7808" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7807">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeIngX32WKjjlFBA1FKXwg0thtS13Rel3wSapNz3lSYamqjaKY5W6rRl_x69_CISgigSs9UkpiGZ8x5iUUJqMujFfHFqgPYp9alSabzJyy54b3CEITwr-HVV3DvLolRUconTfQ1hLGQ4-XUsNLMgcdZj9hurhBs-U7BjZEU5LtvLXpIM3rKtKDvr6AA6O9yNN8RT9SV2KLg4bqV1vtmzxoC1jUTFOEH2YER65gTtoCAJvWVU-3PJ0aBRPDjKwGS2LlxzVqg3c_pxLQ2Qh9DkkHw1XTNLdYVsmPVtJjh2XtQivWo5zuZ5seSFcMF3r-ibapq-trKTZVCNVkhqvufjuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8REAMFSQ2Qo-1WUzNYBMBfex25GAel3YeS9wkfsjf34etRBvKrdl7eSDWACf_mj-h6Jdtt-dAhJb_oRWTaMKFAEds3GvCW6Za51sh9qBV2xIk-0mjDW7bjFkmD1j3oETExmRIXsyAUzUPe7F0tLC28xnyfJguYqMq4mnTG9l-KOottIF49-ftTo1ffupopdQFTWyTaKBYKc-oLscsfhUfhszebSYGqtK00Cv5mq4IhqxnaqFrMwnZ5h0qD6RHxjfF37DeIfbNZhvWWgEaAir_2_vaWoSSceEKpn2J3ZD4l69ZfxtFhnwPIt2OcfOTTvgb_4F1ojzkmYr98lO10qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود iso ویندوز و آفیس + فعالسازی رسمی رایگان!
همش در وبسایت زیر:
✅
https://massgrave.dev/
سایت قدیمی و معروفیه، سافت ۹۸ و اینا همشون از اینجا اسکی میرن
😱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7806" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7805">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_KM7DIFdclGUd7N7DhqufwTduIuayCbOg2VDIU0ytbJPCBWeVwUTTllQ9rfSFrek6TOXWhLRK1whvhHgpVWvUC_DuhOx8_SYZPUKNS_4sL0FUO4b2-tKq45tBgCUslYHZ89FKLc45fmZMVrq_JXDzlcitk0FaG6n6I7zRoJa_50Tp10St-l0AeJV3bxlwTtSByUzXBpOLdsx03t9VSzMfAe7aQJ-2_jzNwcLe1BYgDgaBkADzB1ialYPXShIfcm9jTMx4Z7DP6zehz8SwbBb9CYhlRBTlI0AMAjBv_IA-lzhWisiiICVX6RL6dzFq3k4aYToK9DS2zby29DGBiOBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7805" target="_blank">📅 21:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7803">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIJLB30cjdPfdy_2WFekTRLplR8huwFubETzWUTAyWV8tg5y1mCa8xW_RAOMXfnDHqHhRYNnHoygyPRj22kSG3LrB5PpFelgLODiHiEPscKcDLl-y1ER61aYecEBr_eXxjMsKJ4lOBNzz9qa2bklTFdq3WpvG50IAqSZzJwL4WQBDoYL7hqUeV4JwoZA6u6kauRSz5S2H8jvisAJjLmN2o4_f8ElXBmbpvV3fo-0J-lSzBWbUg5gLkORAXeaw2pxNoi6_6SAl52AC3FjO8Am93UYhWTpw476rJ-vaBbUmyHLgJN6saKPZmSF82l0xqeiJLWsnhWct-8s_02a1qkxAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7803" target="_blank">📅 13:59 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5a_du37JYdAi1I6k35CVezt16oRpkmoVErg10KH959si8siwlXJkgL2ibSCdliURyzKR9gcv4kDdr6qePFFod7vvfso7GG9qGPE11SxYvmQAP1bTOjbrWepJPmxKJlpus_g0nf8ia61PoixW1NPzHYtIkP8vlM5zEZQAw04pPYdxg7VBOUfZe3bmHLol5NSZ1VKSOX0qA-1vi0qJTHphC120ZEYuRjK7y5EZb6Tu3bbFyUGCAeM-kEpPdnONxvcQcsmNmlUOL0ht4595Vdrk7SZMoK6y1ow5RP93TI3wc18crG8V9ffdLyErsVv56WT2_FGI_BFeBJHTUVNi0Ir5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irRAJ3Ye2t7mRB1QLiM31t7hv5JTFk3ybybJx_fKOQIMR0Rm1f9cNdYrM-o34mqGel_qlzNOy24x6dtRuMuGSDDJeFfU0GfY_4TpXWS3mwtJYmw4k2Xac_3wee3IAxMS-5UuDhe9PjfEWuxTGys-ncPWfefQShsu0iddpyp5GXN-r61PDuXq8DuAq_oCkCwPtpkadklLps6h4wupIQxvcqf4TW1LfGdofFFLboLT1kGXGGPN2l1dOFfNpnr6tFqzi7FIVj_Vi7Kl79vavvIVxfD8xLOJbdqGPFmq54L4uLariVs-JyKsa02OYHdLChybaz788pYsHat7mY2i5k2VDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiJMTSGU6aqqE9mG4g7YzIxIi08p-EjOF_mv99xMwsTLvCuj2GcWxQkH_L_Wtv39TIsePv1fqlNlZnvGrJHDbLeTKP5Ln-58PtsV9AiCNvG_u4VIoFeb2P362NHrKfQ1NhcGtPsKsnYy9iarbJXAfq87rNNHxVOzQehFH5vrQv4jLiDZXO7rn4rYwgIgMoJ-OTxB-ORuLIMlsWgQGjc2NvlZZuUKqFnCVLz-y5fNDB8CgovRVGO6pw0B6tniqNZms_Vm9snkAqIM2tmGVlEtTjQPBCchkBin2KNy0OHHRAhkVx0uM6HWjq9Gyh-t0z6VGxi4dXMuGSIACRx4zozFkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KISZXvKgXn8zMNCmzWs8BUCE3JcVLV4ZPwV6ezgbR1o5y5GOFFNjlZsHsMhd9MuHNYYfZn8GsD0h7s6zy7Eg3Y3IYpA9QyyEREnNgjlQCOoJjME-8FTubKWMAY-GDrnd08jDUz90mYhz9ga0OwCrg8r3gLo_zKrjdsLutkmxP59IeiS1K5EMXhrh59IgSdcY82Tf-2oCPXmcva_uT6LXaHv_67ftYMzNJqbDrb_E9pdmGMb09y3VmyIaBFie0IrqFfWdb4ANMXahMDxv4Vj-ErRVN3B45qvPFcsK4ea_EqI6jy-aG9K3O5Sd-tAOfj0z_0dVIEaR3grvr9BKd-Knyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfOPLaoT2C1d4y6SX04jVscmL02KJefa1fCte6FvE19xDpaUJn3KA58h5nzthvX9J0SJRWObhXvrN4EATXAtHCu3mp_5XXudEDCMn7_7mJjjRTV3r6umg_LRZXU8Bl5L_lfLnQMD2DHQP3k2fAcC9hhlwTjiWb3LgdZKBCLIzV1daUaBM0EatTXc8qDQUdkW97-oOzFCnXSd97fq7yABfruB1WrhFRiTILMBfWXcFAJTD1Ynw-X_oG4CH6-02T93eXhOoSUDEcKVNUomXyEBfVtC9mF1vtcC1jRuVII9aCNuwienSf2jFlIHoFeWzEZKNcXL_n-Y6iavzv5TbkOQ-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acLQaxM9amq_7umB7JEfOaXO9TJQqevp6o6oPW-MlQ_3pzH48hnpIEYB9-LjD4OBtNIp6CimhjdeLOmGv_yg3YSFyx23G8pb9mbbA3eEpOhYjEjl2aNq0466fB11D-HHlN_0YLzzPflAO8VK2_ca-Z3wPNDpCTuuOny-YgovSiv7N0b2LVI0ydNt1wDl2BKKWUhtdYd4F8KC3nNimYa-6mtgg4XJtajuSJn-coW7_azXhravQjODWfjx4Gltaqul7v9RDIMIfZK4wU5WnzYRFLeXrDrYUNo-uCruCX88beIXkSfIDyWH50BwKOzC4VdKQRUntsJY4gKLslTXk6DHug.jpg" alt="photo" loading="lazy"/></div>
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
