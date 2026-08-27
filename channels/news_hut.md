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
<img src="https://cdn4.telesco.pe/file/nAoUaUe18-iE727LGw5cdH1szNaQMb_wdMfAr5th-guQLtdz9XfypOWqg6fGZCVKOQETjNe9nxRz5OR4kvcuWFUfTp4JALy1mwvWGnDgpZwJtSwdPrBSN1M5BYK5plIZq5EIYlCHGf4n3YedQmgbIw071kK8HafGmsUS784jmWbIRjHzaTGPdkoublatgI1CWSis5P9qlRQRESK4gntu8HScfYqnVEPmApVTn4ddXLQA_P6o-YChFA3BLvRb7feauTUce85tdXYWOCxgOaHQLo5s6iRzyQRCMv3Yg86YnSdl06cWNWgOCe0ShG6i5vGndO5NH0Xks178_NRg3YNTuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 117K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-70677">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtpRWO_NBZCLfFjB7vn-zxMlT-ccwSfIdkA5ajKvcZBJCDM-6y2xGxxb3KqUUQBuSA8anEjjwOC9FOqxYlm6Zs-UzoazCGOTjY6DrzprfVZoc_sS827T9lw6gUtxylsfscr4SqlnMVLcYdEa4AOjEn2NEW5Z3Qw0CHyqhYkJBOvUEW6UPGF9ID_fML6I2I-d8gmDoWDqXN1nko3IsG5oiP8bqr0FJKp9CZltRLof4AZp8L-1zVt5mvLAn0IbIiB0_3i048H0gtiLBk_5h4g_evWNLp18J4E1heQLZiNYwnjFQVehefbEA1zmd43QDGZjlap349BabOIlN_bFfQAtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
قالیبافِ در جواب بسنت:
این امپراتوریِ رو به زوال، به‌جای سرازیر کردن میلیاردها دلار به سوی اسرائیل — آن عامل نیابتیِ تروریستش — و صرفِ هزینه برای ۷۵۰ پایگاه نظامی، می‌توانست آن پول را خرجِ مردمِ خودش کند؛ اما نه، چنین کاری برای این رژیم بیش از حد منطقی به نظر می‌رسد.
اسکاتی، رفیق، اعتبار تو در خطر است. کاری بکن.
@News_Hut</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/news_hut/70677" target="_blank">📅 20:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=RN9jvkpuoXyrUbxXIVuslWnochhlcNE926QPN8KYYv9csCIvZWtcO-I9ZQMv5Ua2XuyaZPgCFfl6pDwYMFesV1ae9m-YD-4h1alAs9_5U0mxz5C8IvXRkIfeNXVD0dPGlsPqBegvvsHIHhK0B5Z_MmHA8nLHeSoNLBQaz5K4-lkqnmmrhsQeKRYiPZMP-6l8ZSthNgWlJTPOWPuPn2XODYiX-o99LOVPheJaJOogLhfHGcT2a18X5dPgp9sbqG21r9sY-q5s2SmulS_tWAFHQOWlwWjHZ_a_jgtx093o_QZ_vqbXi8-fC8rKOYBpoL8cshvXcGXnj7ZBsl8gcayfUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=RN9jvkpuoXyrUbxXIVuslWnochhlcNE926QPN8KYYv9csCIvZWtcO-I9ZQMv5Ua2XuyaZPgCFfl6pDwYMFesV1ae9m-YD-4h1alAs9_5U0mxz5C8IvXRkIfeNXVD0dPGlsPqBegvvsHIHhK0B5Z_MmHA8nLHeSoNLBQaz5K4-lkqnmmrhsQeKRYiPZMP-6l8ZSthNgWlJTPOWPuPn2XODYiX-o99LOVPheJaJOogLhfHGcT2a18X5dPgp9sbqG21r9sY-q5s2SmulS_tWAFHQOWlwWjHZ_a_jgtx093o_QZ_vqbXi8-fC8rKOYBpoL8cshvXcGXnj7ZBsl8gcayfUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف عجیب پمپ بنزین در کرج دیشب
.
@News_Hut</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/news_hut/70676" target="_blank">📅 20:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxmaCiPU3Ry-PRD9IvZWLi_Q0UU2lSed_x5CZhFmPKcbUrkefa3ITzr6-R4ghRxQa2bEURWrO2FihRZIthOmw_xtDtK-JdjuPptd_QWdevve4UnBR8cVsr1-JKQ-a8cxMgnGYoxUEVICMB6LArRoox8f7r94CLOOhEPKBvhrFtno-fncHV5I1f7mNJ5FRUqLHp9baoKldCSbEir5g7IPb9sS4v5agyQbvnq2p280YArjXjcu_R5UE7a3MnMH2EDai45VfUtrzOrsayUQfQ-s2458IdzM9leiE11lR04TGZx8kgfnNuMD6JcnSfde8_XhKTQNRr92_Fd4cXALUVb0NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
هم‌زمان با تداوم اجرای محاصره علیه ایران توسط ایالات متحده، هواپیماهای جنگ الکترونیک E/A-18G نیروی دریایی آمریکا بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند.
تا تاریخ ۲۷ اوت، نیروهای «سنتکام» (فرماندهی مرکزی ایالات متحده) برای اطمینان از رعایت مقررات، مسیر ۷۵ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای بازرسی وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/news_hut/70675" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833865a38.mp4?token=Y8KD_rg59JsOpmxNSMlegEeXeUkQ4MUNVqnGh4s65s8R1n3Wr049S3WE_WBQi4ox4kIB3N8yS6POenJfUDWekEBqc4KK7VFTUmPhad-bqlNIfFMmXK9LA7M1knjckElRAFIVC3GRHerl_LpCBjzziv6zlokEmrq2ekaJSbHhtwD1olavRZiubguplFxkdHJ3BApaOxtQvuZPHHMQF0PWg5FG_Apb_18syjtNwAO6xFcTQo-l8S_f_2GvWpRLR4VmHyayikVs-vD_LwfCw56dpLhCS3dfncPSb0-WgWADVRCBFg_SLXhNiOnV199zqA7JCE5Y71o8ZWAHe4CBfjkysQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833865a38.mp4?token=Y8KD_rg59JsOpmxNSMlegEeXeUkQ4MUNVqnGh4s65s8R1n3Wr049S3WE_WBQi4ox4kIB3N8yS6POenJfUDWekEBqc4KK7VFTUmPhad-bqlNIfFMmXK9LA7M1knjckElRAFIVC3GRHerl_LpCBjzziv6zlokEmrq2ekaJSbHhtwD1olavRZiubguplFxkdHJ3BApaOxtQvuZPHHMQF0PWg5FG_Apb_18syjtNwAO6xFcTQo-l8S_f_2GvWpRLR4VmHyayikVs-vD_LwfCw56dpLhCS3dfncPSb0-WgWADVRCBFg_SLXhNiOnV199zqA7JCE5Y71o8ZWAHe4CBfjkysQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس نیوز:
🇶🇦
نخست‌وزیر قطر در حالی وارد تهران می‌شود که تلاش‌ها برای کاهش تنش‌ها در این مناقشه، با هشداری صریح از سوی رئیس‌جمهور ترامپ روبرو شده است:
ایالات متحده تا هر زمان که لازم باشد، به مبارزه ادامه خواهد داد.
تنش‌ها در تنگه هرمز همچنان بالاست؛ جایی که ایران اعلام کرده این آبراه حیاتی تا زمانی که واشنگتن خواسته‌هایش را نپذیرد، بسته خواهد ماند.
در همین حال، ایالات متحده با اعمال تحریم‌های بیشتر، فشار اقتصادی را تشدید می‌کند.
در داخل ایران، فشارها رو به افزایش است. صف‌های طولانی بنزین، تورم فزاینده و تضعیف ارزش پول ملی، مشکلات اقتصادی را تشدید کرده و نگرانی‌هایی را درباره احتمال شعله‌ور شدن دوباره اعتراضات برانگیخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/news_hut/70674" target="_blank">📅 19:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=A8RMRv5eMNIyg66aGPa8LGGZYmPUc2ZFiN11dtB5yWlr5WwMjUdCsiIqCRzQOFwVs1XuaLo0puvKjkHGhfEJpGmNsDJsAFAztjIsW8xChksSep4TFY0aQEj_H3xweHhkSRdCrQb3GQ99xkbGMm32UGkoQtgcDLlWYt7iaoGMhq6V8ycmQgl4SDxcDQLOelnKvYmwdVLp0T9CNV4MLtSHTykNGxpY4EyMAzRYDDYA40UpSyiRSW4qkTUhKBouRfwKB4uDuoUB3Qg1vNrdJ0cIE_HUKvO0uDxs5ynv3IiQBi36ekCzJE1fl13J2qoOUi9xBqTnei0gLHD5T9f4RCXIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=A8RMRv5eMNIyg66aGPa8LGGZYmPUc2ZFiN11dtB5yWlr5WwMjUdCsiIqCRzQOFwVs1XuaLo0puvKjkHGhfEJpGmNsDJsAFAztjIsW8xChksSep4TFY0aQEj_H3xweHhkSRdCrQb3GQ99xkbGMm32UGkoQtgcDLlWYt7iaoGMhq6V8ycmQgl4SDxcDQLOelnKvYmwdVLp0T9CNV4MLtSHTykNGxpY4EyMAzRYDDYA40UpSyiRSW4qkTUhKBouRfwKB4uDuoUB3Qg1vNrdJ0cIE_HUKvO0uDxs5ynv3IiQBi36ekCzJE1fl13J2qoOUi9xBqTnei0gLHD5T9f4RCXIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
فیلم از منطقه صنعتی بین کفر رمان و نبطیه الفوقا در جنوب لبنان پس از یک بمباران هوایی اسرائیلی.
@News_Hut</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/news_hut/70673" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70672">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHUf-UGTYythln1xXRRsJm2jhny-NqK_wkDxyUKUuik6-h_RiPWYfcoDVz2rv6qWbO-6VgYWtV97AF6PlAdjnSLYRJuGOj8i7go7Xjw9c8XPp_yCSb0dIsqeIAjr51DsQDbe1LAZCuAJt86aB9zdehFFH23sjwLlDURJAxzeP37l-FtTlyeBVhn8bYSeOo-Nuv6fg6ouAdhfi1l4-Tf03eX1X74tYQm7cRAAA6mVhBYw9-qAFAeHF_0-WUDtP10fTnoN6QnbHV4tC3YcxPYgwrvz499fh4vGWfuqda9aTe6JzUPStVXL-fwcsgj8pCNx7x7Aodi2oL9uVXp5RTZHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
〰️
بِسِنت وزیر خزانه‌داری آمریکا:
در حالی که مردم ایران برای تأمین نیازهای اولیه خود با دشواری دست‌به‌گریبان‌اند، رژیم فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.
این رژیم باید به‌جای سرازیر کردن میلیاردها دلار به سوی نیروهای نیابتی تروریست خود، آن پول را صرف مردم خویش کند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/news_hut/70672" target="_blank">📅 18:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70671">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=QCVaG3MI-tlGwL3sEbhhFtsOSP2NL7kYlAzrMs05o0ImQZYE1p9O7XrU3X6FFP40x2qANVghQqwvCoST6W8jv1--9Rc0pD2WaaP247YY0MV-RaWVVvMDKsPEBjZngK6kfpuyZ5_q-5KcM5V3Ar4B1quqQBMZcJTIu-TztrXCxjHVgxjpmyKqIi_Zne95UW02CTEhAJxQRtOPYRY7_WreWrxP1zi_RmVONND_z-he-qMWU_PC7FMZZ_x0mR-hESVZHr4Kmv6TYzvGWSoW-Ic8TSjj-fSnp_BuAGXKzCHikRkYGB8Mcxi2_ffWkzzKgrvGht8tioawIoFeZYVyOD8dBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=QCVaG3MI-tlGwL3sEbhhFtsOSP2NL7kYlAzrMs05o0ImQZYE1p9O7XrU3X6FFP40x2qANVghQqwvCoST6W8jv1--9Rc0pD2WaaP247YY0MV-RaWVVvMDKsPEBjZngK6kfpuyZ5_q-5KcM5V3Ar4B1quqQBMZcJTIu-TztrXCxjHVgxjpmyKqIi_Zne95UW02CTEhAJxQRtOPYRY7_WreWrxP1zi_RmVONND_z-he-qMWU_PC7FMZZ_x0mR-hESVZHr4Kmv6TYzvGWSoW-Ic8TSjj-fSnp_BuAGXKzCHikRkYGB8Mcxi2_ffWkzzKgrvGht8tioawIoFeZYVyOD8dBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
کارولین لیویت سخنگوی کاخ سفید:
در حال حاضر هیچ‌گونه مذاکره‌ای با ایران در جریان نیست.
این وضعیت تا زمانی ادامه خواهد یافت که ترامپ احساس کند آن‌ها ممکن است به شیوه‌ای معنادار پای میز مذاکره بیایند.
ما هنوز چنین چیزی را مشاهده نکرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/news_hut/70671" target="_blank">📅 17:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70670">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=UEfHslhE6AH9nTrx3BmCVyHU5A-pXLLeiRS1tlm1w7YszdeUR6LCfk9hzS7s6sfF0wY5R3MgodvKlq58tSKFTFjx47koNwD60UxtrkcheHRQCefUyO2-Wl1QOTd7--Hrm4CpSZXSHCj1jZq3ZLWcCitbkqJeLVf18BNPt--wlwNhmuUNzq18C75fdKLKm63Ukf8hVJIVjWbmu34MqqO-8C40Dm9yngv4If7t4zXKuXVCcWZnK5s2q1uCSN40HhRXeIMt6ZIy3GdLSY6prumBBr01OLg92eP4Eu-0syBYhcvNSSZhLWUU7hG7knydufDQvuSSpWUfg28bCIN4yX69EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=UEfHslhE6AH9nTrx3BmCVyHU5A-pXLLeiRS1tlm1w7YszdeUR6LCfk9hzS7s6sfF0wY5R3MgodvKlq58tSKFTFjx47koNwD60UxtrkcheHRQCefUyO2-Wl1QOTd7--Hrm4CpSZXSHCj1jZq3ZLWcCitbkqJeLVf18BNPt--wlwNhmuUNzq18C75fdKLKm63Ukf8hVJIVjWbmu34MqqO-8C40Dm9yngv4If7t4zXKuXVCcWZnK5s2q1uCSN40HhRXeIMt6ZIy3GdLSY6prumBBr01OLg92eP4Eu-0syBYhcvNSSZhLWUU7hG7knydufDQvuSSpWUfg28bCIN4yX69EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت!
می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/news_hut/70670" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70669">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9LfVuWY_3QUK3yiDYs5f7Iav06s8K72pVr8Fz4GOdev72YveJmnNaiesImpVO4_BKVJxCPMnu1VEj7243eUEdezt4YLdN6nuONJcCfSQlH1tnyeFxNNeEduDXx5yG5Y8rLIeEPj7E_zUbRCfa8oygQ7GfEyBt1PRWJOjvVK69DWTY78jKDinjD9nX1B6fx2frclgVjR5rYpQuaWzB5QGDCZI-uoI0vgQZeTATNE1tTmBG8q6o2ymIQbQxVxqRFyreRzsOfnLHO7s3ysr5mf8xhFXS7sIRUXeEvNq8X01bo3Bh9oF-rSQXjRQ7zPU6LP4OvCNhrWYgjqZWQNjAQTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/news_hut/70669" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70668">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=UOidhZPUaBQ9tZVdMUUHgVWZKaB03o2SYnznC_b-sh60Mt5Eyx4zkqCTYEuYVyHYUfSquHRetgs5yugAFs65gZzK6DCk2S3kS528_1VbxWaQDzXU1__ahEI4TGoHm6jPYcUunI6G38F3RFt-YrGrk0T4KKo80CPqOZ2ZTk-uQpDFHpimVCc9PIlYk2F0MOXyPtjEGGyF0q9C3jzYYjxqNTltZpavPhvDlWH8WfPGw6K6b1hS6vbcz1rXtr8Ii5Y9QzU0mwbj9jU1XATiPr5Y4TI2T6Ly9gDLgqiRxzSHiIMgeTEgYMXxu3lIaC6m5A5aAyfOs4kXoELycCAE1Srosw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=UOidhZPUaBQ9tZVdMUUHgVWZKaB03o2SYnznC_b-sh60Mt5Eyx4zkqCTYEuYVyHYUfSquHRetgs5yugAFs65gZzK6DCk2S3kS528_1VbxWaQDzXU1__ahEI4TGoHm6jPYcUunI6G38F3RFt-YrGrk0T4KKo80CPqOZ2ZTk-uQpDFHpimVCc9PIlYk2F0MOXyPtjEGGyF0q9C3jzYYjxqNTltZpavPhvDlWH8WfPGw6K6b1hS6vbcz1rXtr8Ii5Y9QzU0mwbj9jU1XATiPr5Y4TI2T6Ly9gDLgqiRxzSHiIMgeTEgYMXxu3lIaC6m5A5aAyfOs4kXoELycCAE1Srosw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بازرسی امنیتی در مراسمی که تحت کنترل حوثی‌ها در یمن برگزار می‌شود.
آن‌ها به دنبال کمربندهای انتحاری و مواد منفجره هستند.
همراه داشتن سلاح‌های شخصی مانند تفنگ‌های تهاجمی و خنجر برای مردان یمنی امری عادی‌ست
😳
@News_Hut</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/news_hut/70668" target="_blank">📅 17:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70667">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe281d624.mp4?token=A1BE8ee72Gx69Gx9lXQhMm8KYayg77NyehL0iVrM4tiNTR4HZKXf4vXfoEsVqr2Nkwxir0nOwPRVx_DJVQ34BN4DvwMZLyGKszO0cam0y1knko0aELv55AXAqjHGEuxI98uOSpIrwirWU8q4wTn7e3P4NW00tXFkLXX983iO8-VXtIA2yHIPZg0uoXXNsdta7LNgT7h68HE_5cwffH5DzpUwIUrHBb6m7iwYomh1K2nfsFTlFXV9r7QSldiJvSegz1Rt8drsieSAF2EUj1YA3hUcWmG9Hqw-SZWb1NXTl5R9favXVUXTv_oqlDo-3ENNldX8I_VvQHZdswZZvx_UtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe281d624.mp4?token=A1BE8ee72Gx69Gx9lXQhMm8KYayg77NyehL0iVrM4tiNTR4HZKXf4vXfoEsVqr2Nkwxir0nOwPRVx_DJVQ34BN4DvwMZLyGKszO0cam0y1knko0aELv55AXAqjHGEuxI98uOSpIrwirWU8q4wTn7e3P4NW00tXFkLXX983iO8-VXtIA2yHIPZg0uoXXNsdta7LNgT7h68HE_5cwffH5DzpUwIUrHBb6m7iwYomh1K2nfsFTlFXV9r7QSldiJvSegz1Rt8drsieSAF2EUj1YA3hUcWmG9Hqw-SZWb1NXTl5R9favXVUXTv_oqlDo-3ENNldX8I_VvQHZdswZZvx_UtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خنده‌‌های علی مدنی‌زاده، وزیر اقتصاد در واکنش به فشار گرانی‌ها بر مردم
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/70667" target="_blank">📅 16:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=ETCwnZX7HiCePNaYkwYgT12OMg_hbNVW2wI2zp8_1gUHQZ4eyOoRpedq-QhOmKs30vvDnZKg0JHE38wbYJtbHLfwvbeKX_Oe5yfNn0rQip_bipJ06rRKonz7ZRu9Cbpk4BHBKjFDacQfzHLneWKyYnoSbri8z-PB1jrWIeDakchp4w9B_0jZ1_RE57S19LTjHuuGx_7AJg3E2KctJpr04KzYTShGNQyL5QbObRAcplrNBCfmNF89t_bRy-kADSWGX9DPuLxww97fZ3C130IUk-hXoBH3_E7qORkhTNB8nwZ6_aOlCJRes7gc04RZnDxHBG5KOuaUzZh6cqrpccwXBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=ETCwnZX7HiCePNaYkwYgT12OMg_hbNVW2wI2zp8_1gUHQZ4eyOoRpedq-QhOmKs30vvDnZKg0JHE38wbYJtbHLfwvbeKX_Oe5yfNn0rQip_bipJ06rRKonz7ZRu9Cbpk4BHBKjFDacQfzHLneWKyYnoSbri8z-PB1jrWIeDakchp4w9B_0jZ1_RE57S19LTjHuuGx_7AJg3E2KctJpr04KzYTShGNQyL5QbObRAcplrNBCfmNF89t_bRy-kADSWGX9DPuLxww97fZ3C130IUk-hXoBH3_E7qORkhTNB8nwZ6_aOlCJRes7gc04RZnDxHBG5KOuaUzZh6cqrpccwXBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یک طرفدار حکومت :
قیمت دلار همینطوری میره بالا و ارزش پول ما همینطوری میاد پایین
ولی این میتونه به نفع ما باشه چون برای اون خارجی محصولات ما میتونه ارزون تر حساب بشه و بیشتر تحریک بشه تا کالای ایرانی خرید کنه
این یعنی فروش بیشتر بیکاری کمتر و چه بسا درنهایت مهار تورم و توسعه اقتصادی!!
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/70666" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/timgv4R8Y6d6xYeYa_AUwugmhi43k3pjkeBKotfqtrHS5cYubEkkxzFXTfYC4P6bKXLRCQf1TnvuIYZNX60HhhA80P6afTEy-QGIfq2y1YFiGPKSQG9_bN3770K4OeoLPWb880-I6gr7P68ahsQrCj8W2m1v7Pm5M6NR42FObXiT2UpH9oyy_OrwS9xg0WP_KusIGrZ4D5xjV3fIsfaykvgMbpfOli_oeTqp16ya9L9Ymy_6YfTGk1EWSAtR9g4WLcjgCWqMSwn13tkdooqy9AmganFZN-x6vSDXIwFpodrGfhi7YrHTPKt__vcDc9gvXvnlALkIYC0Ngq81IQjYiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
📰
سی‌ان‌ان:ناو هواپیمابر USS Theodore Roosevelt همراه با حدود ۵۰۰۰ نفر قرار است در هفته‌های آینده به خاورمیانه اعزام شود.
این استقرار حداقل ۷ ماه پیش‌بینی شده است.
جان پریمن، Master Chief Petty Officer نیروی دریایی آمریکا، گفته خدمه می‌دانند مأموریت بیشتر از هفت ماه خواهد بود و فرماندهی به آنها گفته برای ۸ ماه برنامه‌ریزی کنند.
این اعزام را در ارتباط با فشار عملیاتی ناشی از استقرار طولانی USS Abraham Lincoln قرار داده؛
لینکلن بیش از ۲۵۰ روز در دریا بوده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/70665" target="_blank">📅 15:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70664">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=K8w_PK1dODZY2rDT4-IiUug-GeaySMtw8TcIjm5jA1cfKqlH7-MpaAJL7DNrmvpW3og36yn21n4FeHzkNDpwNp912DXUfi-G-UWFGhqC-3UaAhyXBIF8bXi2sblnPl40Oll3XXz9G_1_iH1eZlaxv7OtHGxFgVD8cIcF8p7hdovGGfRuOB1K7PsqOlIIV9PJVIpSef0HADWnFyg27wSEiJ3LHNf9I25Z_Oj1FbTI3C-fegTi5UebpiO7BFzraLqsVNEKg2PS2X9inY8kvAP83SZgVuQ3T3TCxMFdM79LGlwfcp4wsPLk2KT_joO3xom7MHJnKz93Wo1Fr3DFGAvR_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=K8w_PK1dODZY2rDT4-IiUug-GeaySMtw8TcIjm5jA1cfKqlH7-MpaAJL7DNrmvpW3og36yn21n4FeHzkNDpwNp912DXUfi-G-UWFGhqC-3UaAhyXBIF8bXi2sblnPl40Oll3XXz9G_1_iH1eZlaxv7OtHGxFgVD8cIcF8p7hdovGGfRuOB1K7PsqOlIIV9PJVIpSef0HADWnFyg27wSEiJ3LHNf9I25Z_Oj1FbTI3C-fegTi5UebpiO7BFzraLqsVNEKg2PS2X9inY8kvAP83SZgVuQ3T3TCxMFdM79LGlwfcp4wsPLk2KT_joO3xom7MHJnKz93Wo1Fr3DFGAvR_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیزدهمین فرزند مادر ۳۳ ساله بدنیا اومد
؛
از مرده میپرسن چرا این همه بچه حالا جوابش:
اساسا بچه ها رو دوس دارم من ، هزینه هاش؟؟ هزینه هاش با خدا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/70664" target="_blank">📅 15:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=jlbg68jatG5XawU-A7JuGc5LEWh0M5W934j9NM3pMO_S9MV9QD6TwxKHgSrlgJxVXkV4ELyHYXBDFd4_9teXLdz8YMyZf0_7MFGdXTKRsrEMzfM99YUHUnZhasOS-yn7orQLDLhGHtnx9Yo0lHCI1Jxv_b8WLllFgdIDuuYJRHGbZVaDj3DvfglMwMq_0TlW5tqx8eGIVmFkP9kVzkq15kM1cjUPo9F6r9BNwbqQcu91U8YBX-KUhDZaBR_VqPDyRjCDtsZ4ZvAKzHe-QarcbtsgBmBWCa45BYYz9zAvtEoeoNKc98bcSU7zQAVoII81vqPFKv2G2thQt6Z0QvaLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=jlbg68jatG5XawU-A7JuGc5LEWh0M5W934j9NM3pMO_S9MV9QD6TwxKHgSrlgJxVXkV4ELyHYXBDFd4_9teXLdz8YMyZf0_7MFGdXTKRsrEMzfM99YUHUnZhasOS-yn7orQLDLhGHtnx9Yo0lHCI1Jxv_b8WLllFgdIDuuYJRHGbZVaDj3DvfglMwMq_0TlW5tqx8eGIVmFkP9kVzkq15kM1cjUPo9F6r9BNwbqQcu91U8YBX-KUhDZaBR_VqPDyRjCDtsZ4ZvAKzHe-QarcbtsgBmBWCa45BYYz9zAvtEoeoNKc98bcSU7zQAVoII81vqPFKv2G2thQt6Z0QvaLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش یه دختره اومد از خودش ویدیو تولد بگیره تنهایی که یهو یه 207 اومد کنارش و سه تا پسر اومدن وسط رقصیدن و تولدش براش جشن گرفتن
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/70663" target="_blank">📅 14:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70659">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2FOxbVQPjDuVmFNueyQWRFNrdMP09q9LLDAY7h6DWqs1OI4n67Erjo5u9FGToYo58pT054zpLDjbnKest7h9cmpaH_frLHOMGJafeE_m5LKwc1XQWB5tNNkdSrUfKG7xHRS8dQxEuyT4Fc5ZD6ZMmn5nWJbh_YyVJ46bsXilhSYGQsSzVhOht5pt6cElXJK_gj7wGaOwsYBv72VaI1pr6gMvkP6PFfDJoW6AI3HFdsPOP1yVM_kJo-SG0cFSk5YSpsgAxyGymuOTvvwnPmumOaoeI3cIoPDUvrcTYQrzPXnyDxeTENhHosXEcsV0FQNI1LYFrNY5sDE7ZkhcZgEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItmtEm0BrYAW6L2UZcl6vclh1Iuhm4v0B2ehTvst1U4so7z3mp6SFb1a1sctmFKfA54g_fM7LjoNhPJpNCwmYxEuMqr5iTMSERfFTmsbjLTDEd0krrOCYuAj92CVJeWofuVKOhw5D2EDyIVDa0_pazFzOp8BI3SY7v8JsH0KSJxhGMj1g5iLoSet59OpC3J8LObXuc84d53v-aSmLmYkoSKQN8RZaLExB2G_8zS251LKKkrLwuX80PXxJCmLf7qWeSLTDvL3fz_wHGvIRNG6Vo_Zu04Q3-nOSxMtdqNGTu3EtJ8_Timx7SM4anPuRIvD8yJ5E5ZfM5nISLU2FvLUFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=cETFojY6oR28x6Hk1VW0YI1LvLofMDb4Yz5aTb-qlzO8BhXAz_bEW96YXJ3fjypMLFfNKlfnwAWPyLAeu_nRL0cmbqQ3bjHlmNZburQLV1UF14fp4etYWGNt-mLriLTQZLsnAq12sHRrbWCEPj9ADQGGicUOI5jvZoTHGdf7PEay8i-gBRUFpPSJX4fxVEDdNSycAiW4sZhWCrFsh-ANxxh4OaYok4OFAlDWQIiG4jNfEaUujczI1VQFLg8dGf1upc9DWRa9u60YSiW--D6bZrBMxFMGNwN7LL4NQWpZ6f86MBP_xuvOyaj4kfbqh4tX9NTEaXsVKqvcRHLNfyHqbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=cETFojY6oR28x6Hk1VW0YI1LvLofMDb4Yz5aTb-qlzO8BhXAz_bEW96YXJ3fjypMLFfNKlfnwAWPyLAeu_nRL0cmbqQ3bjHlmNZburQLV1UF14fp4etYWGNt-mLriLTQZLsnAq12sHRrbWCEPj9ADQGGicUOI5jvZoTHGdf7PEay8i-gBRUFpPSJX4fxVEDdNSycAiW4sZhWCrFsh-ANxxh4OaYok4OFAlDWQIiG4jNfEaUujczI1VQFLg8dGf1upc9DWRa9u60YSiW--D6bZrBMxFMGNwN7LL4NQWpZ6f86MBP_xuvOyaj4kfbqh4tX9NTEaXsVKqvcRHLNfyHqbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ایرج مصداقی از نزدیکان شاهزاده رضا پهلوی در یک مصاحبه درباره علی کریمی صحبت کرد؛
صفحه اینستاگرام کریمی در اختیار شخصی به نام امید دانا است.
بعد از انتشار این صحبت‌ها، کریمی در چند استوری به‌شدت واکنش نشان داد، از مصداقی خواست ادعایش را ثابت کند و شاهزاده رضا پهلوی رو مخاطب قرار داد و برای اظهارنظر درباره این موضوع ۲۴ ساعت مهلت تعیین کرد.
⏺
مجدد مصداقی در ویدئویی جداگانه به واکنش‌های کریمی پاسخ داد و اونو مخاطب قرار داد؛
علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره
حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی مثلا؟! داریوش که میبینی که بلایی سرش اومده تو انگشت کوچیکه اونم نیستی.
بهش گفتن جهان پهلوان باورش شده. اخه مردک کسی که دوتا لگد به توپ زده پهلوونه؟! همین مونده بود تو برای ما شاخ بشی. فکر میکنه چون فوتبالش خوب بوده سیاستم میفهمه. ما اصلا تو رو حساب نمیکنیم ابله.
اینا رو ارزش دادنی فکر میکنن خیلی بالا هستن آقای کریمی با تو یا بی تو فرقی نمیکنه زیاد حرف بزنی صداتو میبرن
⏺
علی کریمی هم در ادامه اومده گفته؛
از اين لحظه به بعد؛
از هيچ شخص يا حزب سياسى حمايت نميكنم.
در حد توانم به مبارزه‌ام عليه رژيم اشغالگر شيعه ادامه خواهم داد.
این تصمیم من به منزله سنگ اندازی در راه مبارزه دیگر افراد با رژیم اشغالگر آخوندی نیست.
به اميد آزادى ايران و مردم نازنينش
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/70659" target="_blank">📅 13:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70658">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXtAXNGWHJf7Ndax_LmEFPWOq3NH5n5L4qg5WqoRWM8Xjw-f9mGMFFrOx15F8n_5gEDtNpslFi_qPLkdqO5xEgKqGMe0haEgAmGiwaeBFVCvDp2wklPO0LliEJpH0XHrpJM_4cR_reb5GkcFJA2tNhuCSFRNlz9sYtpLseOnOEkUlaqXEBbsh2JH_oHRBctI9aPwd0PqXJYT5EooIScjkIgsQdwY12wkntzSiCjj4hdb4qbKXBKAdGwjVwZQEW3NXikJhA5A7SsMgxzowIvmojMJGDKobirtOSe-INlL5mc9NvhjXYowMiu9cVPdPDSzsJuFk2HLSSfKarISeA3AUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
📰
وال استریت ژورنال:جان رتکلیف، رئیس سیا، این هفته در سفری غیرمنتظره به مسکو رفت تا به روسیه هشدار دهد که به کشورهای عضو ناتو حمله نکند.
این سفر در پی ارزیابی‌های اطلاعاتی جدید آمریکا انجام شد؛ ارزیابی‌هایی که حاکی از آن است که پوتین ممکن است در سال‌های پیش‌رو، با انجام حمله‌ای محدود به یکی از کشورهای متحد، عزم و اراده ناتو را محک بزند.
مقامات آمریکایی نگران سناریوهای مختلفی هستند؛ از حملات سایبری گرفته تا تهاجم زمینی در مقیاس کوچک که به احتمال زیاد یکی از کشورهای حوزه بالتیک را هدف قرار خواهد داد.
آن‌ها همچنین نگران آن هستند که کاهش ذخایر تسلیحاتی غرب — که ناشی از سال‌ها حمایت از اوکراین و درگیری‌های اخیر مرتبط با ایران است — بتواند بر محاسبات مسکو تأثیر بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/70658" target="_blank">📅 13:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70657">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=q_p-2ty9qcfKqDKPLkNAEOVr41NWFb3ALXOLbEi4sfy_98rQMio-DYpoNhJhaGVgnf59Bb1PqDmWl2in3J5XdiJY2JrvcYfVDCBoZFyOKbkh-rlFPk6YgQSJQb8WorhOZaeqY6kP60k37cxr_-wLD_7PWRHv9QnkR5bXTS62HGTNseBOJPuIDGY9zc3PvVxaCgIaICdS1BSvI7hDQip0j9TkBU40kYwx1PEyubM5HwiezEB2Vc6t1hI6VoVosAlPn7RXjQLnA9IHDsIPBDALc6E_O8m87HXeptsAnFihjpISbyLRkCKFtXrwZANZmn5-Q4owSSGdVqPI2yh-cvLiPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=q_p-2ty9qcfKqDKPLkNAEOVr41NWFb3ALXOLbEi4sfy_98rQMio-DYpoNhJhaGVgnf59Bb1PqDmWl2in3J5XdiJY2JrvcYfVDCBoZFyOKbkh-rlFPk6YgQSJQb8WorhOZaeqY6kP60k37cxr_-wLD_7PWRHv9QnkR5bXTS62HGTNseBOJPuIDGY9zc3PvVxaCgIaICdS1BSvI7hDQip0j9TkBU40kYwx1PEyubM5HwiezEB2Vc6t1hI6VoVosAlPn7RXjQLnA9IHDsIPBDALc6E_O8m87HXeptsAnFihjpISbyLRkCKFtXrwZANZmn5-Q4owSSGdVqPI2yh-cvLiPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از خونواده‌ها میپرسن چقدر خرج کنکور کردین برای بچه‌تون؟ رقما به شدت عجیب غریبه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70657" target="_blank">📅 12:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70656">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBGcGhgK9gl7EqbfvkMcxx78R_4nPWHrGNnhpsEaTleT3ptbTd-lnda2255vPMoOTHFea67PYoG-5Ny3tF3kcngOLYH5erDwgWgRbMthQMBVzhPDEfnnhmMrBmZFiqwmVnXxJwN6Vu2jjP7OUqxj0Df3G-iTCOqD2gA7iebTk2eVeVXTGDeQOiQ7PLJV2EFZVAd45O9HDzacusOwwjFCSRbGstlfBGH-1yvQzpg0eknIK09ddXoa_U_jni57-VJuoJDlHNL8PGCdBdVeJVxAy7DLJZevGSwCaGIZ0uaziokyH4Fgd-wgohCwzXg2kN5SJp7OsbvDhNbeN4Kx0aoHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی دریافت کردیم مبنی بر اینکه یک نفتکش در تنگه هرمز هدف اصابت یک پرتابه قرار گرفته و در پی آن دچار آتش‌سوزی شده است.
آتش‌سوزی در نفتکش در تنگه هرمز مهار شده و تمامی اعضای خدمه در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70656" target="_blank">📅 11:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70655">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=VKFFNYfEEVbfH5GVq6iVe0bp_ZA4wMRY_UG5KdqOefRMoCVQl-_B-VYxMGo5FX6JaxpbPE3a0U9SQ1TsTu6s7Z_BsY-ViixhvCR3vJrsVRwwVe1Bap2pCbJPkapE8lNoaSmoltAVGn19fZFMEqi0PgN5Bk51wS9MEulIeFbzh0LXSEnjfC7kMOFOUvZHmUdElO7dCcLpYfywoITIGeSrJhkPDD1x1hGLHUS0A61VK7V1DBTBVV83kHUF8ShCK7a2qS-FLvuyEqWIxD_a9WfMujYuyFT1ZbYiZOvyRG23e7Lx084qgDxgyxusJYQqAwI5b23_XWNS8yG7ZbNgWGQI0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=VKFFNYfEEVbfH5GVq6iVe0bp_ZA4wMRY_UG5KdqOefRMoCVQl-_B-VYxMGo5FX6JaxpbPE3a0U9SQ1TsTu6s7Z_BsY-ViixhvCR3vJrsVRwwVe1Bap2pCbJPkapE8lNoaSmoltAVGn19fZFMEqi0PgN5Bk51wS9MEulIeFbzh0LXSEnjfC7kMOFOUvZHmUdElO7dCcLpYfywoITIGeSrJhkPDD1x1hGLHUS0A61VK7V1DBTBVV83kHUF8ShCK7a2qS-FLvuyEqWIxD_a9WfMujYuyFT1ZbYiZOvyRG23e7Lx084qgDxgyxusJYQqAwI5b23_XWNS8yG7ZbNgWGQI0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇴🇲
🇺🇸
کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، درباره دلیل و نتیجه نهایی مذاکرات عمانی-ایرانی:
ما گفت‌وگوها را با عمانی‌ها آغاز کردیم تا بتوانیم به آن‌ها بگوییم که حداقل در روحیه همسایگی، این اقدام برای باز کردن مسیر جنوبی می‌تواند یک‌بار دیگر تنش‌ها را ایجاد کند، فرآیند اجرای توافقنامه‌های اسلام‌آباد را مختل کند و حتی منجر به شعله‌ور شدن درگیری‌های نظامی در منطقه شود.
​
انتظار ما این بود که با کمک دوستان عمانی‌مان، شاید بتوانیم این مسیر را ببندیم. با این حال، فشار آمریکایی آنقدر شدید بود که متأسفانه این مسیر جنوبی بسته نشد.
​
سپس آنچه رخ داد را دیدیم: جمهوری اسلامی ایران تصمیم به بستن تنگه هرمز گرفت و در ادامه، شاهد درگیری‌های نظامی بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70655" target="_blank">📅 11:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70654">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=RIfv-INdXqXI_iKAiYAici_wAu-NUw20zFz64Sh_Ic3D6okCRgIBsNg9MSLDdpGZooLROWlZFQ2m2m7hVGgAVNduDqxPynY28F_NeLuGcHDYWvcOz_7nzn_B-rPgEA4DPlN9a0N2lTojwk1ZhkwOVuevHd96-JFjIqzYeEx5ybbc7YRlwdqHm8_90h6W_8MfJR1vf6MGLEbgkTFHW41cQ2og2E9Ej9N1kroDErnqOE9lv23pXwTcfnaNcWonSJEOt3Z0ddYDooBXH5VX66Gp6mnwsVwkXKhY78SkFNIVuhlpGCLpYqBPr5dJxI6VbrzDdRoeqrz9Cagw5cK32cTdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=RIfv-INdXqXI_iKAiYAici_wAu-NUw20zFz64Sh_Ic3D6okCRgIBsNg9MSLDdpGZooLROWlZFQ2m2m7hVGgAVNduDqxPynY28F_NeLuGcHDYWvcOz_7nzn_B-rPgEA4DPlN9a0N2lTojwk1ZhkwOVuevHd96-JFjIqzYeEx5ybbc7YRlwdqHm8_90h6W_8MfJR1vf6MGLEbgkTFHW41cQ2og2E9Ej9N1kroDErnqOE9lv23pXwTcfnaNcWonSJEOt3Z0ddYDooBXH5VX66Gp6mnwsVwkXKhY78SkFNIVuhlpGCLpYqBPr5dJxI6VbrzDdRoeqrz9Cagw5cK32cTdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعارهای عجیب حامیان حکومت در تجمعات شبانه:
دلار شده 200 تومن همتی
یه کاری کن میگن تو بیغیرتی
حیف که نمیشه بکنیم به تو بی احترامی
ریاست محترم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70654" target="_blank">📅 11:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70653">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45450621ea.mp4?token=E1FCC5RvGr7r5xUfZr3dFqgwQNlpBDLzlhTLiBfir2_OaJo8T3_rAzpLCOdhXCldwjnUHd7gcdC0Ep9QCuq5mPf4xEynekyf6gzGMBciGFw1WJAG6kJ-rEPfUXRxKnz1UT8pSwehJEc-OiJAFp1uX6DcHBlEOONf5V-LPrtFdbErtFxKfhEAAApahMqCsSo4pqxMYBscGdex-W1LRT0Pdc8it3Kcfi9gMxIUtWUNSFpkMRHEPzwUwf-7RekHLR7KTYEHnQM_iXPR7xzSyTrFB8LMRkVzaaaFl6Gf_rqxhqEEIecaDMlvuCQjYVa8zgngJxTNCMbO8_Or7mr2J2QLdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45450621ea.mp4?token=E1FCC5RvGr7r5xUfZr3dFqgwQNlpBDLzlhTLiBfir2_OaJo8T3_rAzpLCOdhXCldwjnUHd7gcdC0Ep9QCuq5mPf4xEynekyf6gzGMBciGFw1WJAG6kJ-rEPfUXRxKnz1UT8pSwehJEc-OiJAFp1uX6DcHBlEOONf5V-LPrtFdbErtFxKfhEAAApahMqCsSo4pqxMYBscGdex-W1LRT0Pdc8it3Kcfi9gMxIUtWUNSFpkMRHEPzwUwf-7RekHLR7KTYEHnQM_iXPR7xzSyTrFB8LMRkVzaaaFl6Gf_rqxhqEEIecaDMlvuCQjYVa8zgngJxTNCMbO8_Or7mr2J2QLdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
سخنان جالب امیرعباس هویدا و آمار ارائه شده توسط وی درباره وضعیت ایران در آن زمان .
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70653" target="_blank">📅 10:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70652">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
اعترافات اندرو تیت (بوگاتیت چه رنگیه) و داداشش تریسان تیت :
اون زندگی فوق‌لاکچری که از ما تو فضای مجازی می‌دیدید، قرار نبوده واقعیت کامل زندگی‌مون باشه؛
ما داشتیم یه نقش بازی می‌کردیم، مدل کارمون اینه که هرچی محتوامون عجیب‌تر و اغراق‌آمیزتر باشه، بازدید و لایک بیشتری می‌گیره و در نهایت پول بیشتری درمیاریم.
اون بوگاتی‌ها و استون‌مارتین‌های چند میلیون دلاری که تو ویدیوها می‌دیدید اجاره‌ای بودن و اون سوپرقایق تفریحی 50 میلیون دلاری هم مال ما نبود؛ برای تبلیغش پول گرفته بودیم.
حتی خیلی از حرف‌هایی که درباره ثروت عجیب‌وغریب یا داشتن چندین پاسپورت می‌زدیم، بخشی از همون شو و شخصیت اینترنتی‌مون بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70652" target="_blank">📅 10:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=l1GWv3m6m1VfNPm9YFBXuLvT7Z3NUj82TgvW6MkstY37CMgSD4fMOAyEkddzQHV_DFgThpSKdFxKn9W0HaHIUtFiiNtgTjCWOXp3wLZGGaqdsdZL489jwms-ycM0diNas9VkNjqLyleFnnlyJnF_QJFKzSeWxBr3P-WSPXqYOIu61YoeCoPffN6qIcV4Ub3j4fmWGrhRYcOZi6bG200_M8t3Ew6qII7dfvuiXhJCdW7B5eZTqWwO6AUMb_i8s5W-lTxV2E_hfFPO4iKjGEgOi4_x0h592YqjKcP8edg6G92beL6EcApG8dBw3UMmfXPg6VdljF7AxPzVVHSwdLYrDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=l1GWv3m6m1VfNPm9YFBXuLvT7Z3NUj82TgvW6MkstY37CMgSD4fMOAyEkddzQHV_DFgThpSKdFxKn9W0HaHIUtFiiNtgTjCWOXp3wLZGGaqdsdZL489jwms-ycM0diNas9VkNjqLyleFnnlyJnF_QJFKzSeWxBr3P-WSPXqYOIu61YoeCoPffN6qIcV4Ub3j4fmWGrhRYcOZi6bG200_M8t3Ew6qII7dfvuiXhJCdW7B5eZTqWwO6AUMb_i8s5W-lTxV2E_hfFPO4iKjGEgOi4_x0h592YqjKcP8edg6G92beL6EcApG8dBw3UMmfXPg6VdljF7AxPzVVHSwdLYrDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکنا گزارش داده یک فرد که بلاگر اینستاگرام هم بوده، عاشق ماشین‌های مدل بالا بوده و توی دیوار دنبال آگهی ماشین‌های گرون می‌گشته.
با صاحب ماشین قرار می‌ذاشته، می‌گفته یه دور تستش کنم و بعد با ماشین می‌رفته!
نکته عجیب ماجرا اینه که بعدش زنگ می‌زده و می‌گفته من دزد نیستم؛ چند روز با ماشینت دور دور می‌کنم و بعد سالم پسش میارم!
ظاهراً هدفش فقط لذت بردن از ماشین‌های مدل بالا بوده و بعد از چند روز هم ماشین رو سالم برمی‌گردونده!
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70651" target="_blank">📅 09:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70650">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=cX9kNmPVYGBdCkqFzT6A4k3kPsftIj9J-P2QoqOPWkqueEk6quc3D7pHASngP0fYCSPsEGw7my2z1AJkntTVRaVT4A-q-k5_eyIny2bxkcusfIq5zdcQ1WmhQf2U7_3ggXZtpp2ZiVzaRjKB9aZLkv7Oc01VMZIGIpsa_9iWFaxHc6Wlge19FZ_hIBvQfU6KrTvRx0oiRGHxb1ZZiUPZJGiwvv0RxPhaL68eAJkNVDytLbf_8gMyn4zLhRZJknwVZg3XXTIQ7enHxwu2JZyWl6uPIKaMUz35t4SVFlV72u8Uk9XB8TdSj8ulUmSyc4YlQorlZWjFtY-cEEB-AGEqgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=cX9kNmPVYGBdCkqFzT6A4k3kPsftIj9J-P2QoqOPWkqueEk6quc3D7pHASngP0fYCSPsEGw7my2z1AJkntTVRaVT4A-q-k5_eyIny2bxkcusfIq5zdcQ1WmhQf2U7_3ggXZtpp2ZiVzaRjKB9aZLkv7Oc01VMZIGIpsa_9iWFaxHc6Wlge19FZ_hIBvQfU6KrTvRx0oiRGHxb1ZZiUPZJGiwvv0RxPhaL68eAJkNVDytLbf_8gMyn4zLhRZJknwVZg3XXTIQ7enHxwu2JZyWl6uPIKaMUz35t4SVFlV72u8Uk9XB8TdSj8ulUmSyc4YlQorlZWjFtY-cEEB-AGEqgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
یکی از زیباترین سخنرانی‌های محمدرضا شاه:
هیچوقت به زندگی فعلی خود قانع نباشیم و دنبال بهتر کردنش باشیم.
برای بهتر کردن شرایط زندگی، اولین شرط خونه و سقف بالاسر هست و بعدش قدرت خرید مردم.
محیطی که در آن زندگی میکنید باید شاد باشه، غذایی که میخورید لذیذ باشه و لباسی که می‌پوشید تمیز و لطیف باشه‌.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/70650" target="_blank">📅 09:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70649">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70649" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=PJxtQwm_wlpd91ln3soqX93z8J-YhNzzAuEObg_KB_GGskvv69s7FEFY4ICdguaS1RZ-BEjzqjb5A18yOF0fErJ8mVbJWnwXsc9w383ctALnv0sHFddA6lIV3T7tPfn_JLi6Tk6Vnt2vhpa1mI73U5KNEdjtYK7weUZBoyA94eYm2oZUm74V_HIjP5tGAp4KH_hXNqx8eXBfsSfBdZKve8lHPhgmrMKsGwY8ajTMnrlCKXldIO1SrqewRIl8wP4EoIBxC8CQ70rWk9-CpJeQjjBkgKaI5Q8WIMlRSu-Izsa9tMZu7Xzh_q4rW3iCsTOf1uAEmMZcLvaSKLkAgAJFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=PJxtQwm_wlpd91ln3soqX93z8J-YhNzzAuEObg_KB_GGskvv69s7FEFY4ICdguaS1RZ-BEjzqjb5A18yOF0fErJ8mVbJWnwXsc9w383ctALnv0sHFddA6lIV3T7tPfn_JLi6Tk6Vnt2vhpa1mI73U5KNEdjtYK7weUZBoyA94eYm2oZUm74V_HIjP5tGAp4KH_hXNqx8eXBfsSfBdZKve8lHPhgmrMKsGwY8ajTMnrlCKXldIO1SrqewRIl8wP4EoIBxC8CQ70rWk9-CpJeQjjBkgKaI5Q8WIMlRSu-Izsa9tMZu7Xzh_q4rW3iCsTOf1uAEmMZcLvaSKLkAgAJFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a4
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70648" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff574e553.mp4?token=DqUtLoOTdAJMPqGFYOlqDCogYmAMAxMHPMlwlg-FNfEHQ5q4DPR4xsHTc3kZAVMMXhKZWDIRB_49pPAg0IMtdEZUYrexjNhiphcV5BK7UGMVPkdln2tF3PQpiVj60OoZXn4nkV3bgYPisRpLjQ6kxb3RkmF6EvDx0cKAFw82Fw18ai1NxKlP3Lxgxpg-8OdT57ikclKfEyNx2PKHGW_zBQqvm9nQJblnXytO75jNCBL-BcnRjoXHbxW5Ns98KnY0qLtZU4s1_8oRCCtFQqcKKm0bKuZTgIW0wDBvPk6b3UdHVoKLc6m0zVuBegEUbP_TjzzxtdfZLONsXVz4MliAjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff574e553.mp4?token=DqUtLoOTdAJMPqGFYOlqDCogYmAMAxMHPMlwlg-FNfEHQ5q4DPR4xsHTc3kZAVMMXhKZWDIRB_49pPAg0IMtdEZUYrexjNhiphcV5BK7UGMVPkdln2tF3PQpiVj60OoZXn4nkV3bgYPisRpLjQ6kxb3RkmF6EvDx0cKAFw82Fw18ai1NxKlP3Lxgxpg-8OdT57ikclKfEyNx2PKHGW_zBQqvm9nQJblnXytO75jNCBL-BcnRjoXHbxW5Ns98KnY0qLtZU4s1_8oRCCtFQqcKKm0bKuZTgIW0wDBvPk6b3UdHVoKLc6m0zVuBegEUbP_TjzzxtdfZLONsXVz4MliAjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهروندان اسپانیایی ساکن منطقه "سئوتا" به ساحل "ترامپولین" حمله کردند تا مهاجران را بیرون کنند و اقامتگاه‌های موقت آن‌ها را تخریب کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70645" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr1uNfFrjx7PXK2ssdlDsVPh5O20TaYIeXR_q2D4jE8ljXZVjP8-kue3nmrutTn32fZ9-f1I8iTVEaZ7nQrL51cPaf0zuPBquvz55m6Lw-qct89aVI5GxBL8eOvhZTlMhVJeHn1kRLycUkqxGq8N9cInR4c6UUPxgv8Oc_lyxE9DaQZty9rzEDzyUY6iVk23_PEocHfn0cuT9tGHQUb37ISqo-KotDqkjvODzrseur0AyMxd6welZOgt5apc1Fq-gsRTx8cTXZ6ZKtppBpGQm09OZ9j_bZitn-5y9Ip0QauHtTH6hiw2iHP1DUzBTujAYfe5FAhZ2IKss6tzvjMVDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا ناو «یو‌اس‌اس آبراهام لینکلن» را برای نمایش قدرت به منطقه اعزام کرد.
پس از ماه‌ها جنگ — و بیش از ۲۰۰ روز بدون حتی یک بار پهلو گرفتن در بندر — این ناو اکنون برای استراحت و تجدید قوای خدمه، راهی تایلند است.
مأموریت: نمایش قدرت.
مأموریت فعلی: نمایش تعطیلات.
«خسته‌ام، رئیس.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70644" target="_blank">📅 01:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3143921715.mp4?token=ZrnE0kxRC_F_CJvVmo7kmaOaK5HROUhRLD1f50pzrH-blYdGMUOu837Jz44UYBeqhwcVKeYWA_OTq8ZmhRqPTDOSHjdYv75SYJ4ogJ87zY1qLz8zf4k_Ua6QqJTZjlMNWwxpRHLC2vYxnmv_ljsMyz45pwsdtm4iP5bxWKcIZ7udHY6MDNyetGMEj0MeiJWGa7nJgz0b9t-9o92NuqoMtUXeHi6YV2bsHvJLpvoUDer9DkTv1TAaQEWlHsuUqkLd68Xdy8qPGkhABgXl4zCgsG2Vqr9i74BADJTpClFBRul-CGzxmt4GO2Lcuj_vrXllJ-y46ipVEiUdCE8ciaT1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3143921715.mp4?token=ZrnE0kxRC_F_CJvVmo7kmaOaK5HROUhRLD1f50pzrH-blYdGMUOu837Jz44UYBeqhwcVKeYWA_OTq8ZmhRqPTDOSHjdYv75SYJ4ogJ87zY1qLz8zf4k_Ua6QqJTZjlMNWwxpRHLC2vYxnmv_ljsMyz45pwsdtm4iP5bxWKcIZ7udHY6MDNyetGMEj0MeiJWGa7nJgz0b9t-9o92NuqoMtUXeHi6YV2bsHvJLpvoUDer9DkTv1TAaQEWlHsuUqkLd68Xdy8qPGkhABgXl4zCgsG2Vqr9i74BADJTpClFBRul-CGzxmt4GO2Lcuj_vrXllJ-y46ipVEiUdCE8ciaT1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شکار شکارچی
اپراتور پهپادی روسیه توسط یک پهپاد FPV اوکراینی کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70643" target="_blank">📅 00:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiEGxgRBV1-mMC9FeeK8t88QQbHUT8SB9DcWKol1Ne_omZZNTXxJlPIFXkIfF2-V1zLNGaGasos3sQn8tuOGWf5wzlxwu7xpSWclFT3SiAeVoaUi6gyvPbHpdkIb-yyHejtUTkEWfhQXZ9D3Jyu2REQa69B-6V9CSZe9fGD_VugI076YpCwb1kfaw_qC6Rg6kNrjD8IHe_Dr2cyz5e8ZiwNm-j1D0ZbWYY3PlpUAbd6Nr93EHpaLwL2uXW9TJ3dmVXNerT1L7ux_89ej0f_qpgD1SlvL1UbjWmkKMT0el70rUQDAZ323YHysDs6l8maqq4m3F04N1Xu_HDeW8hWsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=sBQARAegDceZMrKEPwr7IOON972ojT2xTSYgN6TZ413JnEyQXJItFWYxcg1xnzWP5PHxZDFY-e3ZYc4LtKqTjWFXIQeYNTFJPiXd_4Xn_21TESwq6Pq_tBr0e38lknfAk96AzsItKHlwZX5NQD-uGPriuRZjyABfpox4JFCuxuYUMB8ZYDYo5osDFGuMG5BLBpdE1Mp65gGD1OkAaupHc0_GTzh25WIXduNU0tscOZYyIIAhnU4ubmW-xIqELjy7bAG8Yl93qUk_ZYB0Eo3jcK-PxOrHhuFJC8ljATgl6nBDcWYMLzJO9tUs5IcPowbijljq1MCY0avKSmRUSwV6AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=sBQARAegDceZMrKEPwr7IOON972ojT2xTSYgN6TZ413JnEyQXJItFWYxcg1xnzWP5PHxZDFY-e3ZYc4LtKqTjWFXIQeYNTFJPiXd_4Xn_21TESwq6Pq_tBr0e38lknfAk96AzsItKHlwZX5NQD-uGPriuRZjyABfpox4JFCuxuYUMB8ZYDYo5osDFGuMG5BLBpdE1Mp65gGD1OkAaupHc0_GTzh25WIXduNU0tscOZYyIIAhnU4ubmW-xIqELjy7bAG8Yl93qUk_ZYB0Eo3jcK-PxOrHhuFJC8ljATgl6nBDcWYMLzJO9tUs5IcPowbijljq1MCY0avKSmRUSwV6AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇳🇵
ویدیو هایی از سیل آخرالزمانی و وحشتناک امروز نپال که باعث شد صدها نفر کشته و ناپدید بشن!
ویدیوها عمق فاجعه رو به خوبی نشون میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70640" target="_blank">📅 23:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=pzHC8awCvuuNlAms9dIh5NW-GG3sfliSJ6l5bcAGd_0EyI7DQm0AOmP-MrXAKjPwqC4LYyi4Ie5W10wwM5IBHBJOmYxZYUxwK7K28_Kdnau8a7bE7M8u1PIW7W3kRmneskHDbctKP7srCadpXIbxNxvf2bzAn9-J4Avfx3aXLPzNho4WhbOGYA8K4ypGK2KrE3OhRe1rFT1XxMtd9-jqrNOavvfLCpYTePCnMhTHLZ8E-WH_ADrSeR5zH7B0_xzB0TUYcJtXLIHEZIKIgS_RpmAJdD8eMurGcOQ2O_Bb8lfV7l808HANPGn1VPmhXdIUYGKTh6xQqfZ7sRIOxRTyPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=pzHC8awCvuuNlAms9dIh5NW-GG3sfliSJ6l5bcAGd_0EyI7DQm0AOmP-MrXAKjPwqC4LYyi4Ie5W10wwM5IBHBJOmYxZYUxwK7K28_Kdnau8a7bE7M8u1PIW7W3kRmneskHDbctKP7srCadpXIbxNxvf2bzAn9-J4Avfx3aXLPzNho4WhbOGYA8K4ypGK2KrE3OhRe1rFT1XxMtd9-jqrNOavvfLCpYTePCnMhTHLZ8E-WH_ADrSeR5zH7B0_xzB0TUYcJtXLIHEZIKIgS_RpmAJdD8eMurGcOQ2O_Bb8lfV7l808HANPGn1VPmhXdIUYGKTh6xQqfZ7sRIOxRTyPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالملکی، وزیر سابق کار:
دولت دروغ می‌گوید که پول ندارد و نتوانسته نفت بفروشد. در طول جنگ ۴۰روزه، فروش نفت ایران افزایش قابل‌توجهی داشت و درآمدهای نفتی کشور حدود سه برابر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70639" target="_blank">📅 23:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70636">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07429c6dd.mp4?token=hDxaqN-h7sb0uHA5hFfRNKotEw0U4pVRmPkH-SUEA5btzKqk5Dbdt_zdpnd5MEyam4we2ly1QQgKzRSIaBapg-iHfl1OflCtvobb38rZVbOwOC-Njvj3LxG3dEqVceWndagnMOhV43U_aZ9Wiacl1OupusA52Z37YLsTTkV9vkFklC4Hg_SdH3Rs6cgJRYWvdD2j2S7B2L1ct4KjrAbo47-SZTYnmDedY6-KDU0kt9RYRUqpHXLqCobzNM0JxhpQE5IpFucwkPYw4cHuPMBP8MI7Mu_pcpeI2J0Th6Jan4SG42Aj9Kp5CZRY1TRQMNsUgDgHmRpbb9Czh7a7eAYRVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07429c6dd.mp4?token=hDxaqN-h7sb0uHA5hFfRNKotEw0U4pVRmPkH-SUEA5btzKqk5Dbdt_zdpnd5MEyam4we2ly1QQgKzRSIaBapg-iHfl1OflCtvobb38rZVbOwOC-Njvj3LxG3dEqVceWndagnMOhV43U_aZ9Wiacl1OupusA52Z37YLsTTkV9vkFklC4Hg_SdH3Rs6cgJRYWvdD2j2S7B2L1ct4KjrAbo47-SZTYnmDedY6-KDU0kt9RYRUqpHXLqCobzNM0JxhpQE5IpFucwkPYw4cHuPMBP8MI7Mu_pcpeI2J0Th6Jan4SG42Aj9Kp5CZRY1TRQMNsUgDgHmRpbb9Czh7a7eAYRVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دادگاه محاکمه اندروتیت اعلام کرد ماشین های بوگاتی و استون مارتین اندروتیت اجاره ای هستن(یعنی مال خودش نبودن)
اندروتیت یه مدت بخاطر ویدیوهای انگیزشی و سیگما طور که میداد بیرون؛ حسابی معروف شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70636" target="_blank">📅 22:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70635">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaLySuBUDutNl2bNXPindr2-eRIGwLCbqj2ogksnPcDjnIS1AppnUg4SIjbKTrUsuTEvYhAO6NG50prhx8WPxzzZ7vA_SepN7zlBlyQB8OnNTmZaZ32ZmmQ305UudCWh_EUIRPnvhWf7Kfnye_s1-eDUV0L25-Lzjz1ruyx4NLqekN2_Jqiy_TKliSsQ7qEf5UrebvC50RbMTJL_CXhuL26V2Zjlxs0E-igYDhSKpTTYi3Sl63NIXi1fXN5D-EjH8eFTxMNTl1nF9Gyzy1fh0pJJ5ewViHfB1kZhJ6sSEUVaLCLzpip3LgUeMXPD4DcsOpOfiDoFO1p5nhUgFvbAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
ما از بیانیه اولیه چین حمایت می‌کنیم که تحریم های غیرقانونی علیه ما رو رد کردن
مشارکت استراتژیک ایران و چین بر پایه احترامه و سازندگی و یک دیدگاه چند قطبی استوار وجود داره
این رابطه نیاز به تایید هیچکس نداره
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70635" target="_blank">📅 22:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70634">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66110614c2.mp4?token=DFOxmUO6l2srh20HGeeLL1gHNpHmw8T_6W09yTu8ku1Uzc6CWDBA5GVASGIDAWqi-XxR0to28037V9XwttWKrNzR3hxcMUU3nAi6Ff1xYiUj0zeM4gIsStH0LLJIA2zcr7efkcU9mJndPMcYH6stvatNk-H0b_cSRTml1DWlfsWZNWQupTauw0ump0LS6Lt7qn-7qRQLY7IrnHKYZGVirHZsXiNvoT1v726hNnrVxVU7ooiPuSD5eKnpgCPc1-tnzuVm3h3eULOalDbW3PLDpzxsUCjeMq7qz9tCuL3TDwRYMA9DYuGcqi4PzWkaKtcAxfOn4slY4eTO2hTUmHBMBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66110614c2.mp4?token=DFOxmUO6l2srh20HGeeLL1gHNpHmw8T_6W09yTu8ku1Uzc6CWDBA5GVASGIDAWqi-XxR0to28037V9XwttWKrNzR3hxcMUU3nAi6Ff1xYiUj0zeM4gIsStH0LLJIA2zcr7efkcU9mJndPMcYH6stvatNk-H0b_cSRTml1DWlfsWZNWQupTauw0ump0LS6Lt7qn-7qRQLY7IrnHKYZGVirHZsXiNvoT1v726hNnrVxVU7ooiPuSD5eKnpgCPc1-tnzuVm3h3eULOalDbW3PLDpzxsUCjeMq7qz9tCuL3TDwRYMA9DYuGcqi4PzWkaKtcAxfOn4slY4eTO2hTUmHBMBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو‌ ارومیه یه پسره واسه دوست دخترش یه لندکوروز سری 300 که قیمتش بیش از 70 میلیارد تومن هست رو خرید تا سوپرایزش کنه.
تازه، زیرش میدونین چی نوشت؟
ایشون نوشتن، تقدیم به زیباترین دختر ارومیه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70634" target="_blank">📅 21:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70633">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlMcIvvOSgotyogzajVMIDaa-qPJxCm4hb3dcxHWIHBu1S2jquJiLSSxWmCEY5dEuSbgNgk70ZtEADaen2XegWgL8g7L5_j1hUh9CCKpnfWGAfmCg5d7HpOZFRVp_XjUvlKXHHNzq9dKrKyxH9kYesx9OY09dY5jpJO8qEyh9Nge8bb2tVb3ZNxSDoPlMOXgWm9QcFqeilYCTwVi_CleFoMFMl3vRH8lxuUOE32q9v8fOwDG_higCpq4TVs3ZlyI4QkgcxBuPaGFhoMmqoyca1f-e9ZYYMBhvHwoHUdn4s1uBEJhY2qXkInOmlFOA69_G87MzWFsvtJ1VRXB1HLR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فارس:ایست بزرگ مقابل کشتی هندی در تنگهٔ هرمز
یک نفتکش هندی به نام «HAANA» لحظاتی پیش قصد داشت تا از مسیر جنوبی تنگهٔ هرمز موسوم به کریدور عمان عبور کند اما با هشدار داده شده از این کار منصرف شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70633" target="_blank">📅 20:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70632">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0J0pfLw3f1lGXyCD79hnXdUT1n9wQ1qLLOA8Cx0-FEyP5OJYrlKi6l1U7SNjetwfBPQgXvbMrb6XfRXLmXEp_GSXmB2qzcePAgdwjPfhF3rR9FN3Pahb9bqNCMgi_s7iej8Zhu-lnEeZpFcfOPBoW2O1Q1cFcE8W9ymO7B_FExqsAmk_ynHIAyron8gvfsyqHmR5sAaw3qrwBl-r4xBWWftojdkdYdzioOdOIg9B7VChz9jLGZXxTJZW2uWn4vS_efgsLQtb3zgZ6zkYE6TbhQhZz9BurZUqcbxNrJbAHpaC6SrMPm5C28XSHuLQipCzssSfoW8v5k2208Ufw5cyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70632" target="_blank">📅 20:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70631">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ℹ️
صحبتای امیرمحمدزند بازیگر صداوسیما:
حرفم با مسئولین اون وره چون این ور اگه حرف بزنیم احضار میکنن و تعهد میگیرن اخرشم‌ممنوع الکار میشی
قبلا حدقل زنگ میزدن میگفتن ممنوع الکار شدی ولی الان زنگ هم نمیزنن خودت باید بفهمی جلوی نون تورو گرفتن
ما ایرانیا با دلار ۲۰۰ تومنی و طلای بیست چند میلیونی و مرغ و گوشت و .... خیلی مردم شاکری بودیم
هرچقدر هم اقتصاد بد باشه گرونی باشه جنگ باشه میگن باز شکر کن سالمی حدقل
بعد که مریض میشی میری بیمارستان با هزینه هنگفت میگن شکر کن حداقل زنده ای
طرف میمیره بهش میگیم خدارو شکر بابا مرد و راحت شد
ما ملت ایران انقدر شاکریم خدایا یه امتیاز ویژه برامون قائل شو
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70631" target="_blank">📅 19:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70630">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
مهاجرانی سخنگوی دولت: در میدان ولی‌عصر یک خانمی به من گفت الهی بمیری!
رسایی سرباز نظام نیست؛ ظریف سرباز نظام است
رسایی منافع ملی کشور را نمی‌فهمد!
جریان پایداری خلاف منافع ملی حرکت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70630" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70629">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=i3pqjHwFo5UKQ0N_j0rnRPQQ8g9sQBofg47RFjt9dmgYeG3AVYm6sIh4HpuPKAXqVs8Ap1R45TmXffmo-_iOlLfgN7ek7sSSj86n58pt9-aYriLNfXUfhlVI8pzvkhAmsJyRWvgLEnKaAXLXUyK5-eH4P4-bfmWXVkcV0fsVf1mwl8RuUEHsPHake8STt-mpqUK5V-bal6xH0IL223vdnqz07nS4TqFGVT9rR6Nwg9UkJYB-Kr1GbV-GeFiQlXxVPNJyaN8jvGv6SVi8oWqYqRpqtZc5_LRa3txVWU4IiCqNeknwsTwZQp3GvvjSClHB-UImTyBtF6z0zeaA235wVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=i3pqjHwFo5UKQ0N_j0rnRPQQ8g9sQBofg47RFjt9dmgYeG3AVYm6sIh4HpuPKAXqVs8Ap1R45TmXffmo-_iOlLfgN7ek7sSSj86n58pt9-aYriLNfXUfhlVI8pzvkhAmsJyRWvgLEnKaAXLXUyK5-eH4P4-bfmWXVkcV0fsVf1mwl8RuUEHsPHake8STt-mpqUK5V-bal6xH0IL223vdnqz07nS4TqFGVT9rR6Nwg9UkJYB-Kr1GbV-GeFiQlXxVPNJyaN8jvGv6SVi8oWqYqRpqtZc5_LRa3txVWU4IiCqNeknwsTwZQp3GvvjSClHB-UImTyBtF6z0zeaA235wVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای این دختر در مورد اینکه تو این جامعه، سخت‌ترین کار پسر بودنه، به سرعت در حال وایرال شدنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70629" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70628">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70628" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70627">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAnyAvym9g3uvgEhyjwflf_YTk9M4fc51wkkwPmI6oI6OnTSgGitGOQwCZ46LPYW9ZxS5vbJcay6MER3wf2CSR5LVIp5Jl1OzOI4zuNOPqvrjU2_h7SdcSSI1VcNeMNwLLOck76bJkIO5OPPU06CNM_5zKq5PQdUis1ZpeXXcyR0g7aNPdgTSLdYVFb0_DIao1_knyTw5Mzc2JKDb6Eq-abdDn8RS5noxJctapvYj7mNfpJkwKjbK2Ga6Nt1pikN1xrOeIr4mds200yWQsWmScsGstaOXfmTb7fwlgOfbyKFyTBFgIH8pKuxGfYA0QHc0BDCanvDI2bzwWwM3fZHrbSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAnyAvym9g3uvgEhyjwflf_YTk9M4fc51wkkwPmI6oI6OnTSgGitGOQwCZ46LPYW9ZxS5vbJcay6MER3wf2CSR5LVIp5Jl1OzOI4zuNOPqvrjU2_h7SdcSSI1VcNeMNwLLOck76bJkIO5OPPU06CNM_5zKq5PQdUis1ZpeXXcyR0g7aNPdgTSLdYVFb0_DIao1_knyTw5Mzc2JKDb6Eq-abdDn8RS5noxJctapvYj7mNfpJkwKjbK2Ga6Nt1pikN1xrOeIr4mds200yWQsWmScsGstaOXfmTb7fwlgOfbyKFyTBFgIH8pKuxGfYA0QHc0BDCanvDI2bzwWwM3fZHrbSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g4
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70627" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70622">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=JcHvirtvScC-9QKfB4oBG-XWzg8QJBNeD1tci0R_BftMUt-K0z8zzpXWJEHGLmZGAsrOertP_XkQM17bUGawsnpMYJW3kYqrazzWkA3113exqmU1_vI8GSEAOmzCAT1hwaw4Z4a3VbZySf0abtmYEgGiPyWuB65VrQ-7rj8JLjNyrlLb7AhnqyJPP2HyehCOe85dptBYnQzVctQ1RBOSRaMhzNjMfxyGI_QQGeuJlm6J013_BDdoWykDbdX19jFAMPDj4DslqRnVkdgltNmOqxC959cQNC20FO7lGD9SyKRTepyiqwwoifwyJJyuvY8VQUebDYDJggWXqy7mvHjJolftl928cP3sUe8vX1S4q8R0JzcY0WyK4-dYXMFRV4s3qicqr6FoAP1rVRgj6I9p0V4C-u45vKTu5xBWzDUdi0CS6urUMWfiw0INeMAfwZipFB6zuW_cN3EO11pss9Bk13oxs60VNXItHVjzWLGgQPXYY3Z7IEKTK_SIFQ_KChzApexpYp5YSo19ScjCvea4Rmoyas_ub3W77qOdN7hoDeIoy2VtkRI8z0X1uSRN1_PX6ehBwFpv66se-ZSxqjTZc700R35YvDexJZi9rLxoiazHoAdwSySF75MAp60y1865LhWeCGjXnW-Uh2iH_XZ7UL8ZkPKbLle8Re6pIL98uSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=JcHvirtvScC-9QKfB4oBG-XWzg8QJBNeD1tci0R_BftMUt-K0z8zzpXWJEHGLmZGAsrOertP_XkQM17bUGawsnpMYJW3kYqrazzWkA3113exqmU1_vI8GSEAOmzCAT1hwaw4Z4a3VbZySf0abtmYEgGiPyWuB65VrQ-7rj8JLjNyrlLb7AhnqyJPP2HyehCOe85dptBYnQzVctQ1RBOSRaMhzNjMfxyGI_QQGeuJlm6J013_BDdoWykDbdX19jFAMPDj4DslqRnVkdgltNmOqxC959cQNC20FO7lGD9SyKRTepyiqwwoifwyJJyuvY8VQUebDYDJggWXqy7mvHjJolftl928cP3sUe8vX1S4q8R0JzcY0WyK4-dYXMFRV4s3qicqr6FoAP1rVRgj6I9p0V4C-u45vKTu5xBWzDUdi0CS6urUMWfiw0INeMAfwZipFB6zuW_cN3EO11pss9Bk13oxs60VNXItHVjzWLGgQPXYY3Z7IEKTK_SIFQ_KChzApexpYp5YSo19ScjCvea4Rmoyas_ub3W77qOdN7hoDeIoy2VtkRI8z0X1uSRN1_PX6ehBwFpv66se-ZSxqjTZc700R35YvDexJZi9rLxoiazHoAdwSySF75MAp60y1865LhWeCGjXnW-Uh2iH_XZ7UL8ZkPKbLle8Re6pIL98uSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
وقوع یک سیل ناگهانی و شدید در منطقه مرزی میان نپال و منطقه تبتِ چین، خسارات سنگینی به بار آورد.
گزارش‌ها حاکی از آن است که در پی این فاجعه، تاکنون صدها نفر از غیرنظامیان و نیروهای نظامی و پلیس مفقود شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70622" target="_blank">📅 18:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70621">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
فکر می‌کنم ۳۰۰ [درصد] باشد. شنیده بودم ۹۰ درصد؛ اما به نظرم تورم ۳۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70621" target="_blank">📅 17:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70620">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=Zw1VJhwHwZblECmy5oKeMPskCZ3DFSu44NeJF0lJZ_82rC3yccBJbhGyF2ApujGV_7MJAZzL7Ut20dfU69ZOLWeCjc28Ee66IRVqdCRxh04g7i8ZUB3S4xbHPTMRK5rOZUxOv_4pCRkXhMWteqrfJV53vKSP46Mg2-UUyGKLYUgwIpCun0k0QLzU5DWYmiVnIJShPEwUqMpAK9OUs-lnq9idBYxnHMmO4AtfFxUWSphYv1jaBrKZ1YvlUMyOXDL_IwUyTfnFDzVFWXV-XmTfngLTFpN-aEIAwJDHNVVmGmV9GUvX9Hhl0Fe6aLvP7e3JHW1LURnl4tq2Y9Jo7L-CSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=Zw1VJhwHwZblECmy5oKeMPskCZ3DFSu44NeJF0lJZ_82rC3yccBJbhGyF2ApujGV_7MJAZzL7Ut20dfU69ZOLWeCjc28Ee66IRVqdCRxh04g7i8ZUB3S4xbHPTMRK5rOZUxOv_4pCRkXhMWteqrfJV53vKSP46Mg2-UUyGKLYUgwIpCun0k0QLzU5DWYmiVnIJShPEwUqMpAK9OUs-lnq9idBYxnHMmO4AtfFxUWSphYv1jaBrKZ1YvlUMyOXDL_IwUyTfnFDzVFWXV-XmTfngLTFpN-aEIAwJDHNVVmGmV9GUvX9Hhl0Fe6aLvP7e3JHW1LURnl4tq2Y9Jo7L-CSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
وقتی کسانی هستند که حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است؛ به همین دلیل است که آن‌ها اعتراض نمی‌کنند.
و البته احتمالی هم وجود دارد، چرا که آن‌ها بسیار تضعیف شده‌اند... به بسیاری از سربازانشان حقوق پرداخت نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70620" target="_blank">📅 17:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70619">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7effdb513d.mp4?token=kWmNQ4z79GRIIT9Tg89Nar0TvLjuCTIB7H4fPPyqREM73zfStZ6QKFSEWq14SW0pbP5bfihakIU0Oa_3a1HGV_UOlrPI9UnKK441dgqk_4GettCKrTf1zYyx9vCmbF8sk6kR9YcV7hskKmHBILcXuV57TsgJVKa24dKwtc7HUg05azE6IUwPG-8xsvN7b138pPJP3lWtkRZ0Y0PcG6pj1Km_EOAvWBVIBks5NzDW0a7-JuTKZZVrV_hzQg2ZFqN3VnYGl3EcBfwpjCD8qwcS3LI9q4duJhTuofXaZU43OStS31NSWBYBlGvSOJ01ukUwkMal-3XvIW1X8d_Fk_UEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7effdb513d.mp4?token=kWmNQ4z79GRIIT9Tg89Nar0TvLjuCTIB7H4fPPyqREM73zfStZ6QKFSEWq14SW0pbP5bfihakIU0Oa_3a1HGV_UOlrPI9UnKK441dgqk_4GettCKrTf1zYyx9vCmbF8sk6kR9YcV7hskKmHBILcXuV57TsgJVKa24dKwtc7HUg05azE6IUwPG-8xsvN7b138pPJP3lWtkRZ0Y0PcG6pj1Km_EOAvWBVIBks5NzDW0a7-JuTKZZVrV_hzQg2ZFqN3VnYGl3EcBfwpjCD8qwcS3LI9q4duJhTuofXaZU43OStS31NSWBYBlGvSOJ01ukUwkMal-3XvIW1X8d_Fk_UEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما از شر مین‌ها خلاص شدیم. اما تنگه هرمز... تنگه فعال است؛ یک تنگه فعال.
بله، هر از گاهی پهپاد یا راکتی یا چیزی شلیک می‌شود، اما این تنگه کاملاً فعال است.
مقدار زیادی نفت از آنجا جریان دارد.
دیروز ۱۰ میلیون بشکه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70619" target="_blank">📅 17:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70618">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ce2d5dc6.mp4?token=OdrJnVkc42W824iOH1ssr3nRzdANMiTHjbh0dRqdGskvMEhv6ux_9U-ovhUVPO2uLg4yXCNDBWbhtuvE7OTOexGe3jLGcvRCBoJJUj6TfUs-RvMuoQP4Hw_5eaxlBw5X3LhsY0d7NkU2SBf8A8WzEU7a0qThbDZWuV9x_xbKkDSH9P6yIGX9SWv4BkRjWzpsRfqx1fnujMoIJzhmciQF4XwV2n1X6lEG89-2clAq7S3KoINdM7hQBM-aI_D7iQdzTGXIOJ3V48ZZH-_W_SvVG38iCB3n037fELNhqukymHWfHyBXENos3ze-O5lgjaSh-kGX_7bXyEADQiALOpV3eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ce2d5dc6.mp4?token=OdrJnVkc42W824iOH1ssr3nRzdANMiTHjbh0dRqdGskvMEhv6ux_9U-ovhUVPO2uLg4yXCNDBWbhtuvE7OTOexGe3jLGcvRCBoJJUj6TfUs-RvMuoQP4Hw_5eaxlBw5X3LhsY0d7NkU2SBf8A8WzEU7a0qThbDZWuV9x_xbKkDSH9P6yIGX9SWv4BkRjWzpsRfqx1fnujMoIJzhmciQF4XwV2n1X6lEG89-2clAq7S3KoINdM7hQBM-aI_D7iQdzTGXIOJ3V48ZZH-_W_SvVG38iCB3n037fELNhqukymHWfHyBXENos3ze-O5lgjaSh-kGX_7bXyEADQiALOpV3eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«باید بگویم که آن‌ها اصلاً گروه شرافتمندی نیستند. و می‌دانید، ما کاملاً قاطع عمل می‌کنیم؛
دیشب ۲۲ فروند از قایق‌هایشان را نابود کردیم.
آن‌ها سعی دارند محاصره را بشکنند و وارد شوند.
نیروی دریایی و ارتش ما عملکردی فوق‌العاده داشته‌اند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70618" target="_blank">📅 17:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70617">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecc2b192.mp4?token=fzFsQnAb7_ZfCOMxKa4acYpuy8TNmH0yhaCD4WLVbztyJ3aKqkaO-XT6uTw80wq4fJScMJPXfjB28dF76nM1BV5rv8mozGWICnv-nFCD0Hn-zI9dR_BPjxaTyQrvJ8VkJiaZCjvrWZYduCzj4biUk_DkOwxi0Oddiw5DqOPpfnqB46Bhr3kyNX41BcUyfWJeHYIQzjD8ehX9S-cLf90oKP6jeJvKnOviI1HQm34-eKnhKBIwEOLHLmZpr4XThZtvnwX3Idi-CY6sLIk4R7O3Xu8QWOq9u9Z8_iWeuNB5XW-eo4Mqqhj7EauvurFV2l89oZRdK0Kj0dPd9EP1neeLSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecc2b192.mp4?token=fzFsQnAb7_ZfCOMxKa4acYpuy8TNmH0yhaCD4WLVbztyJ3aKqkaO-XT6uTw80wq4fJScMJPXfjB28dF76nM1BV5rv8mozGWICnv-nFCD0Hn-zI9dR_BPjxaTyQrvJ8VkJiaZCjvrWZYduCzj4biUk_DkOwxi0Oddiw5DqOPpfnqB46Bhr3kyNX41BcUyfWJeHYIQzjD8ehX9S-cLf90oKP6jeJvKnOviI1HQm34-eKnhKBIwEOLHLmZpr4XThZtvnwX3Idi-CY6sLIk4R7O3Xu8QWOq9u9Z8_iWeuNB5XW-eo4Mqqhj7EauvurFV2l89oZRdK0Kj0dPd9EP1neeLSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره مجتبی خامنه‌ای:
فکر نمی‌کنم مجتبی خامنه‌ای مرده باشد.
او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دست و پایش، و تمام آن ناحیه آسیب جدی دیده بود.
اما گمان نمی‌کنم که مرده باشد.
اگر هم مرده باشد، دارند نمایش خیلی خوبی اجرا می‌کنند؛ چون مدام صحبت از این است که باید برای گرفتن تأیید نهایی‌اش با او گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70617" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70616">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/852e6e635a.mp4?token=srln2fUPsqWNoubVVem0GQQoIqm8Ig8LYkpInSIlqfkGg7RmPYQZ7LHajcMr861F4R4V6muLNNARp5QjVe4Gl4dUyGLtRjCDc0aPsBCZ6vJ_eC4ltySGkfcjEPZzPPhIxVWq319q3f3YTKWsywo8UdUfwoJpx1E6e0_TAg_VTU2B6eUHj5mC1yXH1OIiZqmPwRGwmkPoKRdofdqe3WcMXJGfQH2bpjIMJ-XKIKDPahZxolw6TslOmDdp-D0nU-I4og_otdtJDIXoeX6yes3YuWEDTfR16cPY2h8897AFc6hPiT48nWJYzHKw1kmK96SP8N_BVm8InhL9g7vAxqMLaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/852e6e635a.mp4?token=srln2fUPsqWNoubVVem0GQQoIqm8Ig8LYkpInSIlqfkGg7RmPYQZ7LHajcMr861F4R4V6muLNNARp5QjVe4Gl4dUyGLtRjCDc0aPsBCZ6vJ_eC4ltySGkfcjEPZzPPhIxVWq319q3f3YTKWsywo8UdUfwoJpx1E6e0_TAg_VTU2B6eUHj5mC1yXH1OIiZqmPwRGwmkPoKRdofdqe3WcMXJGfQH2bpjIMJ-XKIKDPahZxolw6TslOmDdp-D0nU-I4og_otdtJDIXoeX6yes3YuWEDTfR16cPY2h8897AFc6hPiT48nWJYzHKw1kmK96SP8N_BVm8InhL9g7vAxqMLaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز 4 شهریور ماه، زادروز شاهِ شاهان؛ کوروش بزرگه
.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70616" target="_blank">📅 16:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70615">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b4425472.mp4?token=WXK4DQiuMk0BkZeu3gN9AvLqb8njGC5EW5t_Vd6MBmDHGE10NwYjNHrS4VW9dbZFzGyG6O-EHp54TziY1YaQWYBQxWRNMLVTFawFdgp_Wp-wLrUPrYd_UtkQGtkDXcbidcwRQXm8-h9ZI-doHPWjxzNH-kiB16txV7fr8uyMWT4SflZt-DAKJocJJ2G_-KHib5b8A0e2w0N8IUKe9j_swHUMIvXlv58elLgrWHpwcppnJ6IsZH_mXdKtqSuF7KQsZEyAXfBoks6oA-X5401NScl1vOEX_pmnU3TiBFOlD42m2CgkUnF0aMuT2Gb0dbk8UmWz9XWalXbglwI8snrS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b4425472.mp4?token=WXK4DQiuMk0BkZeu3gN9AvLqb8njGC5EW5t_Vd6MBmDHGE10NwYjNHrS4VW9dbZFzGyG6O-EHp54TziY1YaQWYBQxWRNMLVTFawFdgp_Wp-wLrUPrYd_UtkQGtkDXcbidcwRQXm8-h9ZI-doHPWjxzNH-kiB16txV7fr8uyMWT4SflZt-DAKJocJJ2G_-KHib5b8A0e2w0N8IUKe9j_swHUMIvXlv58elLgrWHpwcppnJ6IsZH_mXdKtqSuF7KQsZEyAXfBoks6oA-X5401NScl1vOEX_pmnU3TiBFOlD42m2CgkUnF0aMuT2Gb0dbk8UmWz9XWalXbglwI8snrS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کوهنوردای ایرانی موقع صعود تو کوه های آرارات، آیفون17 این دختر آرژانتینی رو پیدا کردن و بهش تحویل دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70615" target="_blank">📅 16:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70614">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662dd7f509.mp4?token=BbkSmG-PMUZL9en1JfCUtikQPnGFIlDrwoUdVLfBP2WQkBFKy6Lemgop8NpUDeIyHSm9cl-loMuUCWMxWnG22u9-NZwsx3nFvt2m50D_yjMuPk8hZZS0EAT1VRNB9MtPmgkcKTxKshwPWdNZ3rnOzj1oacRAo2wZ_tOrdavagySR-xJs1vaxAMJPhF7JJl9A7GvpbG_ooU2JPJqcccCGh_J8-UchYwEO_9ZOCYatUmFduZYNKyZEh_GwWiZE4fiaPj2n3RxnFvh0Rnx4X6fpKbiM5BChHePlXSWS_3AsNe__1ctA764-AXC9qUO2PPLV5Zy4P25MdA3MFXae4xnrWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662dd7f509.mp4?token=BbkSmG-PMUZL9en1JfCUtikQPnGFIlDrwoUdVLfBP2WQkBFKy6Lemgop8NpUDeIyHSm9cl-loMuUCWMxWnG22u9-NZwsx3nFvt2m50D_yjMuPk8hZZS0EAT1VRNB9MtPmgkcKTxKshwPWdNZ3rnOzj1oacRAo2wZ_tOrdavagySR-xJs1vaxAMJPhF7JJl9A7GvpbG_ooU2JPJqcccCGh_J8-UchYwEO_9ZOCYatUmFduZYNKyZEh_GwWiZE4fiaPj2n3RxnFvh0Rnx4X6fpKbiM5BChHePlXSWS_3AsNe__1ctA764-AXC9qUO2PPLV5Zy4P25MdA3MFXae4xnrWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی وایرال شده از نوجوونِ 18 ساله‌ای که با موتور کار می‌کنه:
من روزانه 8 الی 10 ساعت کار میکنم!
امروز یکی ازم پرسید چِتی میزنی یا نعشه بازی؟ گفتم هیچکدوم.
با خودم گفتم من باشگاه‌ام رو میرم، خرجی خونه رو کمک میکنم، اهل دود و دَم و دختربازی هم نيستم.
به خودم اومدم دیدم از خیلی از هم‌سن‌هام جلوترم واقعا
تویی که از این روتین خوشت میاد و سالم زندگی میکنی، به خودت افتخار کن، چون مثل تو خیلی کم شده..
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70614" target="_blank">📅 16:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70613">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/91fcce4d61.mp4?token=rhVOOl-OMqvCeBvHPLTWSMMJ0ojCEUhW82JtLeSYOwAkhCFMqIdDjsKnHcWHWvZqugT9yAM5--2ZhXjkXcrOLaWUQMGfvm73BFwHONbDtkoieWw6tB2JUeWjLXU-9lHl16Pqxau0FtPHakVcNC3COvxrmcu-Kj3Lc7yZjCU04x0AfZxhYeEqxBIEN50YN02X26Z0lFOY3gH8UzENM9EIrdnc6A89xVALhMKO5Q9zQJPFQQDKzNl5QEKYmvNoGk4Z_faOpdg846hr92gn03NUJ03cozYNXmwdVhaTtQKFRyB4F4RtEIexbGzjgGLXtci7nT-It7tZE5DzkiJMQPymhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/91fcce4d61.mp4?token=rhVOOl-OMqvCeBvHPLTWSMMJ0ojCEUhW82JtLeSYOwAkhCFMqIdDjsKnHcWHWvZqugT9yAM5--2ZhXjkXcrOLaWUQMGfvm73BFwHONbDtkoieWw6tB2JUeWjLXU-9lHl16Pqxau0FtPHakVcNC3COvxrmcu-Kj3Lc7yZjCU04x0AfZxhYeEqxBIEN50YN02X26Z0lFOY3gH8UzENM9EIrdnc6A89xVALhMKO5Q9zQJPFQQDKzNl5QEKYmvNoGk4Z_faOpdg846hr92gn03NUJ03cozYNXmwdVhaTtQKFRyB4F4RtEIexbGzjgGLXtci7nT-It7tZE5DzkiJMQPymhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ هر ثانیه بیشتر سورپرایزت میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70613" target="_blank">📅 15:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70612">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee1652504.mp4?token=hc2NZU7ln2V7nDHjzQGwjZQ7RAJx2rLTRHZ0MKr5wmDOKKFxvNhw2dJ8Iwf_IttCpLDoUXSYacZUqJ7mFr2YmNLgQlKhGxU5qX8e7Umn79rXGa_RSI8NBDDHp-ntBOkOupHxW3q0JVntHQ_CQhprvasmiqz1CGJwnBGxaF_0WLDeS8nTihrDXxZ50o27pcQ_qKPkpzZN8e1ni0PMb6oqpPq-_JzDwIcXXujXhr7N2i5tTTMTEB0fdJNYTVm362faF8CK78un6JfUzqB6HBNQsH7dmZDHh9WYPOywajNy7_eyTWHxgcode9nZixFQT_3tBem52cmgIqgDQJ0EuGpd_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee1652504.mp4?token=hc2NZU7ln2V7nDHjzQGwjZQ7RAJx2rLTRHZ0MKr5wmDOKKFxvNhw2dJ8Iwf_IttCpLDoUXSYacZUqJ7mFr2YmNLgQlKhGxU5qX8e7Umn79rXGa_RSI8NBDDHp-ntBOkOupHxW3q0JVntHQ_CQhprvasmiqz1CGJwnBGxaF_0WLDeS8nTihrDXxZ50o27pcQ_qKPkpzZN8e1ni0PMb6oqpPq-_JzDwIcXXujXhr7N2i5tTTMTEB0fdJNYTVm362faF8CK78un6JfUzqB6HBNQsH7dmZDHh9WYPOywajNy7_eyTWHxgcode9nZixFQT_3tBem52cmgIqgDQJ0EuGpd_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
لحظه شلیک RPG توسط سرباز روسی که جلوی پاش میزنه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70612" target="_blank">📅 15:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70610">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/378122b9f3.mp4?token=dxGSKT7eZFzY8N5AUIIjYtBzRS1oxJJj_0zNxA_CDFp4k6N5BBYlsHwSOtXEgDiIjvBHiBwFoOT__9sXT8ZyEdioGklgOYvC13wGQK8D4iBsih7TGE_UzshYv14Q4aMLbfN0OisAigZ86TzgEyxL6pXb_QTqBofsk6TQt9PV47165WegPfIwWEtQ7JT8D6VwH4he7EPR1WSPQSmaUZt7Km5_RefOp9YGxWq_d3HkWv0SFF1WqSHtO9tsR9JmGO7FErC6tkNLuGOLRGJXzlNpZJxpYszLNUsNbDApXOgAr-pqWl7sGdcoBc5dn5Insk2Zxg8EeXIUOepfwfCUkfAcaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/378122b9f3.mp4?token=dxGSKT7eZFzY8N5AUIIjYtBzRS1oxJJj_0zNxA_CDFp4k6N5BBYlsHwSOtXEgDiIjvBHiBwFoOT__9sXT8ZyEdioGklgOYvC13wGQK8D4iBsih7TGE_UzshYv14Q4aMLbfN0OisAigZ86TzgEyxL6pXb_QTqBofsk6TQt9PV47165WegPfIwWEtQ7JT8D6VwH4he7EPR1WSPQSmaUZt7Km5_RefOp9YGxWq_d3HkWv0SFF1WqSHtO9tsR9JmGO7FErC6tkNLuGOLRGJXzlNpZJxpYszLNUsNbDApXOgAr-pqWl7sGdcoBc5dn5Insk2Zxg8EeXIUOepfwfCUkfAcaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این زوج به اسم مینا و رضا بعد از پنجاه سال هنوزم عاشقانه همدیگرو دوست دارن و پنجاهمین سالگرد ازدواجشون رو به زیباترین شکل جشن گرفتن و رقصیدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70610" target="_blank">📅 14:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70609">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qb-8OJVKej46pP9c0gw6fNG67AQ08xz0vNVPdFTRxbYHk6bCRI-xE1mMbomwXd93aA841HI-T0FlO29sVO3WHbTcv6ScTiDcz4NARUfwIHvL0xOsr6nxosKCXV4ljfpkFOfIIXKi8O1cpgT5XnPYQRnjgHujzHcKjxJytD9EuWQG8sZ9nUucDlc7p_yW8KcxGr89UoDe6t5jYVpcncTsQ0ETNkIaCR22S3wm7fLpu-JJzWUdeUwNpVrjirOanvzIfUpE5eso83mo798eb-URbbV0fcESzHtnXVkOV3PABYfwkc1VZIsIjoD3m-MdMFjJvaoy_DGz5nkAM0JfCw8nYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زمان شاه هر اسکناس هزار تومنی، معادل ۱۴۲ دلار بود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70609" target="_blank">📅 13:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70608">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=Dr7q8srQAceZsHWNhZk5EdEmaGzJMSsIZLAxXCR7jxBKGiBvywKSUy7sNDnHTf0Vf_ykpZEm3kr1Ybt17VFIBBm8Bslx422TXgCcCB_05WPOOrkh3HpLJBYkB16mfy_CcQ9g5yP6wHuPB0gE0Ga0qeYUO6wCpCoAcsH_qNTswAQRGvKhdbgVk2pOEYSmOPvXlZpt-CTmrZYSTVZUF8gykJQDP1U_3mNJMASPIdkQmdPzJ5YbgnHOLZDNrZGv3rDoYdpKxdOnMGZtf5YJ7OA-PP6VZgpmC0g9e_cDF2vrM7a0N2yWDOKEdzbRvrJstJ8vcctXWH3YRaJvas5Pb2rr2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=Dr7q8srQAceZsHWNhZk5EdEmaGzJMSsIZLAxXCR7jxBKGiBvywKSUy7sNDnHTf0Vf_ykpZEm3kr1Ybt17VFIBBm8Bslx422TXgCcCB_05WPOOrkh3HpLJBYkB16mfy_CcQ9g5yP6wHuPB0gE0Ga0qeYUO6wCpCoAcsH_qNTswAQRGvKhdbgVk2pOEYSmOPvXlZpt-CTmrZYSTVZUF8gykJQDP1U_3mNJMASPIdkQmdPzJ5YbgnHOLZDNrZGv3rDoYdpKxdOnMGZtf5YJ7OA-PP6VZgpmC0g9e_cDF2vrM7a0N2yWDOKEdzbRvrJstJ8vcctXWH3YRaJvas5Pb2rr2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تا آخر شهریور هیچگونه تغییری در بنزین 1500 و 3000 تومانی نخواهیم داشت
‏مهاجرانی: تولید داخل و ذخائر استراتژیک بنزین مناسبی داریم و جای نگرانی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70608" target="_blank">📅 13:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70607">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=QJdgMH6A7Jf3KP7d55ESTURB_uEz6nyBVhgPjGEdN-40dNoRSjnGR_tfOJe7w5kI46hjcJqvNcjBaaByqWF3SA5gSVqKXDxGe4y56QgzU4aqKvnssTv_QbjuP3CPRxfyhutxMFlYmX4mjrZZXG4YhOrpT8WfUTMweTe-kIWjCTnp0F0UQfv1IoFizWDHb79kKPwIcIGwvJ7rVKpFuLN1g57qSP4yhHqmtdQSDSsy4OGJimrcayCLAiiRwKC0hFct5RYcCzREPYfrUvurCC3fRNLi5w4PxJ8ooXSrCrYuvqsI2Ae4D47dgSgWlHC5z3HXoaj_8zjx3Ph5yVk6NQiBSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=QJdgMH6A7Jf3KP7d55ESTURB_uEz6nyBVhgPjGEdN-40dNoRSjnGR_tfOJe7w5kI46hjcJqvNcjBaaByqWF3SA5gSVqKXDxGe4y56QgzU4aqKvnssTv_QbjuP3CPRxfyhutxMFlYmX4mjrZZXG4YhOrpT8WfUTMweTe-kIWjCTnp0F0UQfv1IoFizWDHb79kKPwIcIGwvJ7rVKpFuLN1g57qSP4yhHqmtdQSDSsy4OGJimrcayCLAiiRwKC0hFct5RYcCzREPYfrUvurCC3fRNLi5w4PxJ8ooXSrCrYuvqsI2Ae4D47dgSgWlHC5z3HXoaj_8zjx3Ph5yVk6NQiBSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
می‌خواهم به شما بگویم: ما همچنان با چالش‌هایی روبرو هستیم.
چالش ایران پایان نیافته است.
ما همچنین باید کار را در غزه، لبنان و سایر عرصه‌ها به سرانجام برسانیم و برای انجام آن مصمم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70607" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70606">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=kZaxMT6PNPEI1JAlRmFPEJposkEV451aOoWW9WNf6CxUxOCWX4FoRfiPUZHhbhp0Zsa_WwTlSrTBrTQnwrtEPzxkXwhjaeLsLPEV7YQn0D321n2v6q-aglUm37NWW5SSVP9Gqt3s-DkCzQdDWiw8wgdWYkPSzgc2cNf5WeAwYtUt9_pAOCeTPXPflBfstuHX84SquIU8De-3ONxBa4kTGu7eFTH7_13meZkgCdN5n05JNI332dA3ELISxT7oI2OKqSsL3lbGEdWeWwbVs6WJmAGc0vDgQlf0IqazbnlL3e4L6T-kvRZw1mYHTS6_aczA9ZSDuAOPdOk3MbwqnQWO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=kZaxMT6PNPEI1JAlRmFPEJposkEV451aOoWW9WNf6CxUxOCWX4FoRfiPUZHhbhp0Zsa_WwTlSrTBrTQnwrtEPzxkXwhjaeLsLPEV7YQn0D321n2v6q-aglUm37NWW5SSVP9Gqt3s-DkCzQdDWiw8wgdWYkPSzgc2cNf5WeAwYtUt9_pAOCeTPXPflBfstuHX84SquIU8De-3ONxBa4kTGu7eFTH7_13meZkgCdN5n05JNI332dA3ELISxT7oI2OKqSsL3lbGEdWeWwbVs6WJmAGc0vDgQlf0IqazbnlL3e4L6T-kvRZw1mYHTS6_aczA9ZSDuAOPdOk3MbwqnQWO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
⏺
و من به ترامپ گفتم که احتمال سومی هم وجود دارد: تشدید محاصره.
او دیروز آن تصمیم را به شیوه‌ای بسیار بسیار قاطع تأیید کرد.
اقدام دیروز رئیس‌جمهور ترامپ، تشدید محاصره ایران بود؛ نه از طریق تنگ‌تر کردن حلقه محاصره خودِ ایران، بلکه با تشدید فشار و محاصره بر کسانی که به این رژیم — این دیکتاتوری هولناک — کمک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70606" target="_blank">📅 12:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70605">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c258982c.mp4?token=rC8K9Lx4oZwS6TNTfhHJRdmaq_WwKpUYmpO0HpnArmZEsvsw_BhP6l8lsxlvRrW2Wx-6EAUPd7qpP2wbJf0sYoGO0ZkRyXmYGIDEoXOwWaPDwU_rMCTeh-ZCnCZBPLQ79kL6tlD_nChYsfPG7bb43sQ8rZVfkgdJKRDyImOKPL5fOSDhHBpMuGmXkYhuAJ_bGCjdoPa7VYjdlU5a8_sTkv2z2Nf8azQF7NtP-iBNhAuS1sGlv7OjRbbCKI5-Fpg173JjspQFfbUPFsyzic4Ggwbu_4WtR5808ooaStBBhNPkpiKwaKFivNyxSXwMc464-cEsR4nWxRfsGo3UbfUxwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c258982c.mp4?token=rC8K9Lx4oZwS6TNTfhHJRdmaq_WwKpUYmpO0HpnArmZEsvsw_BhP6l8lsxlvRrW2Wx-6EAUPd7qpP2wbJf0sYoGO0ZkRyXmYGIDEoXOwWaPDwU_rMCTeh-ZCnCZBPLQ79kL6tlD_nChYsfPG7bb43sQ8rZVfkgdJKRDyImOKPL5fOSDhHBpMuGmXkYhuAJ_bGCjdoPa7VYjdlU5a8_sTkv2z2Nf8azQF7NtP-iBNhAuS1sGlv7OjRbbCKI5-Fpg173JjspQFfbUPFsyzic4Ggwbu_4WtR5808ooaStBBhNPkpiKwaKFivNyxSXwMc464-cEsR4nWxRfsGo3UbfUxwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
⏺
به ترامپ گفتم:
البته یک احتمال این است که شما با ایران به توافق برسید؛ یک توافق خوب. ما هیچ مخالفتی با آن نداریم.
اما تردید دارم که بتوانید با آن گروهی که آنجا هستند — با آن وحشی‌ها — به توافق برسید.
🔴
به شما می‌گویم: نمی‌توانید با آن‌ها توافق کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70605" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70604">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=e0x0lG7W5yZzPcERXHia2aL6-jv5O6Bnf_DpEP4HXECfI0OoxAXn138YW9weSYgROrp35epVQFXa2ZCDVp5ZLajcrnNUGPakPQyt1SLOSor9OzsJ6dJxnsZPZ8w3kAyapz3uelvJcYhYWUo11292qrnLstfOlK7zx7E8BN6hX4ZCsSAVlrx-HV0jPiYn5wT_z5BNSjklh6fy_KGn-WrS_ci0eHFJrR7d6FHMgC87ROB2TuoS5QtXTog4wM-1NLr5hDZPSRop8JT7ilrEd7tE4idrKncBkfuHhci3J94_rK4xh0cyx5qmTW9YGBptDil33ZD9fffS15428MQFZAnmJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=e0x0lG7W5yZzPcERXHia2aL6-jv5O6Bnf_DpEP4HXECfI0OoxAXn138YW9weSYgROrp35epVQFXa2ZCDVp5ZLajcrnNUGPakPQyt1SLOSor9OzsJ6dJxnsZPZ8w3kAyapz3uelvJcYhYWUo11292qrnLstfOlK7zx7E8BN6hX4ZCsSAVlrx-HV0jPiYn5wT_z5BNSjklh6fy_KGn-WrS_ci0eHFJrR7d6FHMgC87ROB2TuoS5QtXTog4wM-1NLr5hDZPSRop8JT7ilrEd7tE4idrKncBkfuHhci3J94_rK4xh0cyx5qmTW9YGBptDil33ZD9fffS15428MQFZAnmJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رفسنجانی سال ۱۳۶۰:
پهلوی همه همت و دغدغه ش این بود که مردم خونه و ماشین خوب داشته باشن؛ زندگی خوبی داشته باشن و ارتباط ایران با کشورهای جهان خوب باشه ولی الان دیگه اینا ارزش نیست و برای کسی مهم نیست .
الان دیگه مردم دنبال معنویاتن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70604" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70602">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=SC9pPTl7a6P14DJ0W3t5bUCTVohczmFo1qKlhJY9YCCiMQ3UEXEsFdu0zWkYhBTkReoqfqsv3MXi_3ly0UusJ73cUxwCsjqKO3XYnUvASxo0Fb0fASyF2DCeGtbXs5OPDWc6AKiOUhG-SeyW7WZWkAq-Ou-7O8aZmwdboFQEQLZBw7f-n2sx7rRQHtjzlaBkX3JoYYqP2TDRJRd3rzSm3d2ezyieOXf5947QY7uQiBgkOaFyqEUF0IkPU5yY3ivwF-ZiFg9gjKyKA9zkfOK-SMy6lgafkxzc1wxqLLpqwid9oYvDadUkSYmr8VBSGpwCAS2crvB2ZD8gdl-scm9nhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=SC9pPTl7a6P14DJ0W3t5bUCTVohczmFo1qKlhJY9YCCiMQ3UEXEsFdu0zWkYhBTkReoqfqsv3MXi_3ly0UusJ73cUxwCsjqKO3XYnUvASxo0Fb0fASyF2DCeGtbXs5OPDWc6AKiOUhG-SeyW7WZWkAq-Ou-7O8aZmwdboFQEQLZBw7f-n2sx7rRQHtjzlaBkX3JoYYqP2TDRJRd3rzSm3d2ezyieOXf5947QY7uQiBgkOaFyqEUF0IkPU5yY3ivwF-ZiFg9gjKyKA9zkfOK-SMy6lgafkxzc1wxqLLpqwid9oYvDadUkSYmr8VBSGpwCAS2crvB2ZD8gdl-scm9nhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مدیر شرکت «فردا موتور» داشت واسه ثبت نام کنندگان خودرو توضیح میداد که ماشین نداریم. دو سال و نیم صبر کردید؛ باید چند ماه دیگه‌ هم صبر کنید که مردم گفتن «سیشتیر بابا همتون همینو میگید» و ریختن سرش.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70602" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70601">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70601" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70601" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70600">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWKHwr4QZNY-wzngvUU8UIhle9ux2OWsnjkngSEZfH3ENtZ8tzDZ7HWF9pdj_17ziOjl6Uh3f0tQTWRhscPZ9uEeLcPceCxMEE4o2dUKhnVPjLSZUCmJ9lL8Mqxqagc9znB7nDTZD7kXLqJzPHhAlkMmsbxlOgq3HSVE5NsUjrOxzXIZHmgljv-8MyMdMArD2yQXnVnQxe5OaeCmLkfY3jTEtigrDQ_AnPZS32zK9K0tWiKI7fl58J2AwoiOteK4jlPSKscltXHtmdS6yTIcwwZcdc6a5lGCW_CrWiZcCtHV6hXpRsxO9_Cvox_Z33KzSsiKVQ1Jbl95LzKgzA6dEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r4
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70600" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70599">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=CVIosU9NUVASzOF0CV5VBT0QpL9-9rxZbupNSY3N0d2D7MtnSajqwprU_VFcU0Txt8A9_7QikfgDziwNQAEjMDWBURhpTUZ3CoxE4P08_xC42t2HJrFST_vF46yiasUFpjp5VATKddIGKTD4zFVFcP63hoWPCQsSlKD-yhz0mWqh5xKowv9xSDyZyXaVOIGBWfMalwP9_P1v1ivZDG3WSpPJ21dfyMI7ndQm80Mfu-wIy3ZxD_9-LxTii_58lF9SBwIY04Fu1mqu0bc8kscxtNpZGFr7yVXNOLfCV-qdjocUxc_A0UQhQ9u1XJHB9ES2NwLQM1frJhFqxZpeax4hcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=CVIosU9NUVASzOF0CV5VBT0QpL9-9rxZbupNSY3N0d2D7MtnSajqwprU_VFcU0Txt8A9_7QikfgDziwNQAEjMDWBURhpTUZ3CoxE4P08_xC42t2HJrFST_vF46yiasUFpjp5VATKddIGKTD4zFVFcP63hoWPCQsSlKD-yhz0mWqh5xKowv9xSDyZyXaVOIGBWfMalwP9_P1v1ivZDG3WSpPJ21dfyMI7ndQm80Mfu-wIy3ZxD_9-LxTii_58lF9SBwIY04Fu1mqu0bc8kscxtNpZGFr7yVXNOLfCV-qdjocUxc_A0UQhQ9u1XJHB9ES2NwLQM1frJhFqxZpeax4hcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای یه آخوند طرفدار حکومت راجب حجاب
:
اگه شما آزادی پوشش داری، ما هم آزادی تجاوز به شما رو داریم
چرا اون کسی که میخواد به زن ها تجاوز کنه آزادی بهش نمیدید؟ آزادی باید بهش بدیم دیگه خودش انتخاب کرده که مزاحم همه بشه
اگه مردم آزاد باشن که هرجور دلشون خواست بیان بیرون پس باید متجاوز ها هم آزاد باشن
چطور میگی قانون باید جلوی متجاوز رو بگیره اما قانونی که باعث بشه لخت و پتی نیای بیرون نباید جلوتو بگیره؟
چطور تو آزاد باشی اون آزاد نباشه
هرکی لخت بیاد بیرون حقش اینه که سرش بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70599" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70598">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=BgdtCDgJUjaTH13qHnwvlFL5J-DPp3RQuF8vM_hcXI4sjiIfxNv8zUYFZ_ARz9Bs9AOcMvVzsKBw-PHroyjCPHnD1OJwZOk9EDkSimAUa1YOZouiliDGc_nhOT6eXpKhL34bDwfCE8ICIBhJAGdc37D7SqM1hjH6F9p1k8gPsN_7UL19Is9zOscGPeKM1yXggBVsB6P-q9a3F7qTuD8Y9-XVTtev9_pQldSSU2fllmBupDjpKmP0PZ0cUMKKf2TQltJkc_H1xRaR_9mxLWTYjLnaTW0Pu4dy9_nfmt2JwA0xCVe_7EmacwABTzOy7a_skxH5k2V6AkTmXHXL4nhhKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=BgdtCDgJUjaTH13qHnwvlFL5J-DPp3RQuF8vM_hcXI4sjiIfxNv8zUYFZ_ARz9Bs9AOcMvVzsKBw-PHroyjCPHnD1OJwZOk9EDkSimAUa1YOZouiliDGc_nhOT6eXpKhL34bDwfCE8ICIBhJAGdc37D7SqM1hjH6F9p1k8gPsN_7UL19Is9zOscGPeKM1yXggBVsB6P-q9a3F7qTuD8Y9-XVTtev9_pQldSSU2fllmBupDjpKmP0PZ0cUMKKf2TQltJkc_H1xRaR_9mxLWTYjLnaTW0Pu4dy9_nfmt2JwA0xCVe_7EmacwABTzOy7a_skxH5k2V6AkTmXHXL4nhhKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این خانمه داره مشاوره میده یک فرد چطوری با رابطه تریسام کنار بیاد
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70598" target="_blank">📅 10:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70597">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=UxHGDo_qYSzo2_QnXzsjdrgwOKb432MDWO0tsKs-wO9f96N3l36dkNwvyoDLHgD-CcRDmR28knhYaGuD0IlSz6a4l5UqujIxYagHWRLvVdkQIyW-z8yDI_8CUmQ8watIEyJj2-ObOgWPUEmTH0tB447Z94yk1W0aiG7wfpnYSNLvPBH1EWXPtElsZaMA2YAk4LRiuK8hfi3JrS4zpFZD-YyDFwJJ0mOXCQV1VFx-X8_vYiz_6iZk6rmW_FQJaKSmGsFfFRiyd3IbS1dmaiiXeGXEdHUVYQRP8w7LJQvfzM8W5ndopknLc2GyjFjImSWdZ5jqzQShmit8rOW0hmj4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=UxHGDo_qYSzo2_QnXzsjdrgwOKb432MDWO0tsKs-wO9f96N3l36dkNwvyoDLHgD-CcRDmR28knhYaGuD0IlSz6a4l5UqujIxYagHWRLvVdkQIyW-z8yDI_8CUmQ8watIEyJj2-ObOgWPUEmTH0tB447Z94yk1W0aiG7wfpnYSNLvPBH1EWXPtElsZaMA2YAk4LRiuK8hfi3JrS4zpFZD-YyDFwJJ0mOXCQV1VFx-X8_vYiz_6iZk6rmW_FQJaKSmGsFfFRiyd3IbS1dmaiiXeGXEdHUVYQRP8w7LJQvfzM8W5ndopknLc2GyjFjImSWdZ5jqzQShmit8rOW0hmj4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
همتی رئیس بانک مرکزی :
علت بالا رفتن قیمت دلار طبیعیه و نوسان های خاص خودشه
ما نمیتونیم بخاطر یک نوسان بیایم مسیرمون عوض کنیم
مسیر ما درسته و خوب جلو میره
اگه این مسیر ما طوری باشه که میان مدت دیدیم درست نشد اصلاحش میکنیم
ولی من معتقدم که این شوک هایی که ایجاد شده جوسازی امریکا هست و شرایط مطمئنن درست میشه و رفع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70597" target="_blank">📅 10:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70596">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
ویدیو وایرال شده از یه جوون ایرانی خطاب به مسئولین جمهوری اسلامی
تراپی خالص :
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70596" target="_blank">📅 09:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70595">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0e780a212.mp4?token=jhgQTYfrtF4YwSCccahcQuU2HyBpuGAtsOlveIK-o_8Lj8p5sAVKKcAvBkSSuDFj_uq2grYFcNUziqywDWEoNzJsDDdA3PITeSDDfXt8oSYJ-doZqAthHRfHv1x2luPRxsTNIu5uRXy7frVe3v4TpOvlEYA3JvilCtvfztOvuE8l_nKXabwd3NihQ7brRWRCJaBn6qGrOHhX2AKPYhb_9BKrGFTsR0qYpUUfP_VbDDeKN6BxY1SdBYgaj7kLg4xtt7c4PlZgdFiVQIqILZrqwq4f0z5_sU4j1QEAXRXickuk5q49fVarviJPiniT6TkUSexCRNcRCdP62M1wvoim-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0e780a212.mp4?token=jhgQTYfrtF4YwSCccahcQuU2HyBpuGAtsOlveIK-o_8Lj8p5sAVKKcAvBkSSuDFj_uq2grYFcNUziqywDWEoNzJsDDdA3PITeSDDfXt8oSYJ-doZqAthHRfHv1x2luPRxsTNIu5uRXy7frVe3v4TpOvlEYA3JvilCtvfztOvuE8l_nKXabwd3NihQ7brRWRCJaBn6qGrOHhX2AKPYhb_9BKrGFTsR0qYpUUfP_VbDDeKN6BxY1SdBYgaj7kLg4xtt7c4PlZgdFiVQIqILZrqwq4f0z5_sU4j1QEAXRXickuk5q49fVarviJPiniT6TkUSexCRNcRCdP62M1wvoim-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
غریب‌آبادی، معاون وزیر خارجه جمهوری اسلامی:
چرا باید همیشه منتظر حمله آمریکا باشیم؟ ما میتونیم پیش‌دستانه اقدام کنیم
بازگشایی تنگه هرمز فقط در صورتی انجام میشه که جنگ در همه جبهه‌ها تموم بشه، محاصره برداشته بشه و وضعیت یمن حل‌وفصل بشه
به فرمانده ارتش پاکستان گفتیم ما توافق رو نقض نکردیم
اگه آمریکا میخواد تنگه هرمز دوباره باز بشه، باید همه شرط‌هایی که ایران توی توافق گذاشته رو قبول و اجرا کنه
ما هنوز در وضعیت جنگی هستیم و تا وقتی این شرایط ادامه داشته باشه، تنگه هرمز هم بسته می‌مونه.
اگه آمریکا به اقداماتش ادامه بده، ممکنه قابلیت‌های نظامی جدیدمون رو هم رو کنیم.
تنگه هرمز تنها ابزاری نیست که ما در برابر آمریکا داریم. آمریکا نباید فکر کنه فقط خودش می‌تونه به اقتصاد طرف مقابل ضربه بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70595" target="_blank">📅 09:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70594">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70594" target="_blank">📅 02:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70593">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=vgJH5XyG_dtQ0e97xvKoj7hphLN9ca2H6pFRuWAoZqp7ZzOT1CqXODZhjPPXJx9rlcfjj6tVNV6fzAyU4Wpw9u4vsRiMCQelEBWUXkkV7OAKIvYE25n8W-1PVtGS1KNU21iCqIWzPD70me98tAvNKidHJcnXgyce7baAk-LdGKV21Itwp0T1-dAVSkhY4lmh5MLk62OUjHxwq4P-DwN_kclPbNoQT02RbcB0VErOXKF0YWQEt_KW245TZjsmAeZ-fqbpgUnvFpYBrqxb-Zljlpi-ycCcUhBSeWPxucPuf-CPl9UgYBi3rknzvsUeFwldUR0-t4JHe8FGZnqv0V5qEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=vgJH5XyG_dtQ0e97xvKoj7hphLN9ca2H6pFRuWAoZqp7ZzOT1CqXODZhjPPXJx9rlcfjj6tVNV6fzAyU4Wpw9u4vsRiMCQelEBWUXkkV7OAKIvYE25n8W-1PVtGS1KNU21iCqIWzPD70me98tAvNKidHJcnXgyce7baAk-LdGKV21Itwp0T1-dAVSkhY4lmh5MLk62OUjHxwq4P-DwN_kclPbNoQT02RbcB0VErOXKF0YWQEt_KW245TZjsmAeZ-fqbpgUnvFpYBrqxb-Zljlpi-ycCcUhBSeWPxucPuf-CPl9UgYBi3rknzvsUeFwldUR0-t4JHe8FGZnqv0V5qEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a3
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70593" target="_blank">📅 02:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70592">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRbKYls93JaUTsj5ybnpd4PMKf_RVhpCbVA-wljDpx6KJ8HYZPhhA3KaDtj1REX_IyKmmHMOQNkYDIQzzPMpbquY8fMSll5-RwBKMwqPTd_zvjZcJf2W-JL0FNBKREGkq0qEr8ucfMvle17-_dThkR6cjudoAC_SZ_Tyeu6uLZGpwfSOcF9Woz66pRfBSWCDSyX6ZA0V-0ggUvso-_4uP9H5Zy7ojQirq0aXDWFu_B_Di8BJillsY5NCw8rkQMDRRwZtCzIHlZcts3Owv3sHOhfSDBXoBwyDiq0XVlf_XXgRD6lUimKK0zFKP8KtiVwbs3r9KKgPLaqv8q1CO5ZxBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وام ازدواج برای یک زوج ۶۰۰میلیون
⏺
یخچال ساید ۵۰۰میلیون
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70592" target="_blank">📅 01:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70591">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nawgS5g5knXmGsmtgvzLBIkrploIG9MWxuRGbDV8gxfHYwPZTEyLymgLkq9RxJD0Vl_6uby24-V5UtiTxC_T-C3NlMVnjwgW3WPZA5fzJqJ_lbQGN4EzYNJC0NnGTeN13MNq4BWQBcx27YI7qIN3M3FiFHadi_OMPdyfhnupAp36cSiveY_Yz04iS0hfmORIU1spm9j8rOiCeNpayCbYiS4_I7ASgTQVe9Twzt1keATwannxenWDd4Xk8ZGNDdntWXIKgM4mQt_Cf5T60RqHpYVbS0FbGEdiDTXcqRVIV-hwsP4_Ci167ne_Cc-RdI7osN10DOfn4jdQbATlP2HaWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
اکسیوس:مارکو روبیو، وزیر امور خارجه، به چندین تن از همتایان خارجی خود گفته است که ایالات متحده «در حال حاضر» برنامه‌ای برای انجام حملات جدید علیه ایران ندارد.
در عوض، دولت ترامپ بر اشکال دیگر فشار، از جمله محاصره دریایی و کارزار تحریم‌های تازه اعلام‌شده، تمرکز کرده است.
روبیو اظهار داشت که اگرچه واشنگتن برای بازگشت به عملیات‌های رزمی گسترده آماده نمی‌شود، اما در صورت حمله نخستِ ایران، همچنان امکان انجام حملات متقابل وجود دارد.
انتظار می‌رود این سیاست دست‌کم تا پس از انتخابات میان‌دوره‌ای حفظ شود؛ زمانی که ممکن است انجام یک عملیات نظامی دیگر مورد بررسی قرار گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70591" target="_blank">📅 01:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70590">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBZaPkqf21fEYHbTzYEcKvs3Up05rq4TXPRgQQ0M-aRPZac0vzZtnzq2EFnTWCJDPJ2EoJzGBhqKvYixTwBVA7gGUGrNex2UtW5jNJBsz0Selv_qhqdGYdffyfjzDgWNwS7W2DiCeTz5AdnmvAakA26c7YkGumZMHbOkukNl1BPUdbVIi6Qh5vcCIzAe5MiTHui8L1KX_XBWR4X65zhvR7hpGPvYWMfFuYLLWLlCzW2xCQzfb9xHKbzhh2LpPXgO2uoA0nqWNvxf9YiiQV5pFV262jXS0qKv6l1SDqHKvoxRhxxswxYMu0AXKstklPLPNEjSBvGYp786U715SzhDrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خروج یک هواپیما از باند فرودگاه مشهد
روابط عمومی فرودگاه مشهد: پرواز تهران به مشهد هواپیمایی سپهران هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70590" target="_blank">📅 00:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70589">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⏺
🎙
وزیر نیرو :
تا دو هفته دیگه شرایط آب هوایی به حالت عادی برمیگرده و خاموشی ها تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70589" target="_blank">📅 23:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70588">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixY1M5wywFymHO-qQs2ZnqCsmXLMut1E6dPsG04VqdwNZzaDnp63uRekqWmyKKyK9sU1iVZwJIKatGzBuaZqOmjiPOZuRSpd7-IC01Zd8na5bUG31JKvkBmwewO041OmZeKqY5WWzOO8_RqT_kZnPE3dXtfhQ8NAgDYnNboUPeAEz8AXLw7P7qATNA0dMK0UBN-1qCJxhRWIi6Cyvz_QXET5gmokIxF1PPl9bA2Ilx-ISeyX1SkBYEwLfU7LFmsBV9qS_M0BwndvOxhXYAWBQgtSJVB4xSIJQ2mhs8AyevaV0aJMzP3qQQUVKGZfR61e8HUAIP3zE7LJy8NhSE5-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇴🇲
بیانیه مشترک ایران و عمان: دربارۀ چهارچوب ادارۀ تنگه هرمز گفت‌وگو کردیم
رایزنی وزرای امورخارجۀ ۲ کشور بر ازسرگیری دریانوردی ایمن در تنگۀ هرمز با حفظ حاکمیت خود متمرکز بود.
🗣️
چهارچوب پیشنهادی شامل این موارد بود:
ایجاد یک کریدور مشترک از طریق تنگۀ هرمز
اجرای پروژۀ مشترک برای مین‌زدایی از تنگه
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70588" target="_blank">📅 23:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=Pd-zsFjef3m2vI1ScYvsw7mjEsRh3Voll1HLMqfzHr9NwQ5JKUbGf93tQOIwPi0tEA6L7S-hjW7Lem9TrxCtf0j94qkEEsUbWN5DddJNYOFJspiY5yiZ3kQdpQAqTHLBnBSzbH-6n8aRADVroZcJq0jseemHiKrr6-xmyC_SnlKCvpCwGJrAsOutD2VgEf1SW604aqWC7iBcitGfvZh_fpYuchHko8GTomZc1H5dMwsekQY42on2SYiS5eHHAztl27DUI7TLx9EjuOEmnE79cpQSdq3S-6YmNGLut7FGlh9vRg1__av-y7Kj1ttE4jbveiLBozJlF7geUsKajSC04A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=Pd-zsFjef3m2vI1ScYvsw7mjEsRh3Voll1HLMqfzHr9NwQ5JKUbGf93tQOIwPi0tEA6L7S-hjW7Lem9TrxCtf0j94qkEEsUbWN5DddJNYOFJspiY5yiZ3kQdpQAqTHLBnBSzbH-6n8aRADVroZcJq0jseemHiKrr6-xmyC_SnlKCvpCwGJrAsOutD2VgEf1SW604aqWC7iBcitGfvZh_fpYuchHko8GTomZc1H5dMwsekQY42on2SYiS5eHHAztl27DUI7TLx9EjuOEmnE79cpQSdq3S-6YmNGLut7FGlh9vRg1__av-y7Kj1ttE4jbveiLBozJlF7geUsKajSC04A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به پالایشگاه نفت آفپسکی در منطقه کراسنودار روسیه حمله کردند.
در پی این حمله، آتش‌سوزی در پالایشگاه مشاهده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70585" target="_blank">📅 22:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=Ix3lWXuknhf5aRmIe7v5F5Jq5Q21pETuHHbKUVaz9J14_u6cCQ3tQlczsUpVMwNcaqTGWmxgQv-AgOalxSgXSgcJpQOFs3PGVK1HOKCjkYGctSkwjIKyXHEDBXt-zluiar962hljNq0lbroT5kiQp5vM2A3Nvm_O5jaRZ80g5puUEGQ4SFaOWbYqIvyPdZ7hIGFrjENENzhVCAgoUFzPcZID7CECYXw9I8CUMyhwbk2M83XGa6tfAKcV8ivuN5OJXrHuUwueGn279rLGs-WW4KTNu8AnCytpbU8hcHNtoGgexeVyehUdLjstq89A93XD0pRD_BfoNj6LKGa_lWePxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=Ix3lWXuknhf5aRmIe7v5F5Jq5Q21pETuHHbKUVaz9J14_u6cCQ3tQlczsUpVMwNcaqTGWmxgQv-AgOalxSgXSgcJpQOFs3PGVK1HOKCjkYGctSkwjIKyXHEDBXt-zluiar962hljNq0lbroT5kiQp5vM2A3Nvm_O5jaRZ80g5puUEGQ4SFaOWbYqIvyPdZ7hIGFrjENENzhVCAgoUFzPcZID7CECYXw9I8CUMyhwbk2M83XGa6tfAKcV8ivuN5OJXrHuUwueGn279rLGs-WW4KTNu8AnCytpbU8hcHNtoGgexeVyehUdLjstq89A93XD0pRD_BfoNj6LKGa_lWePxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مستر‌بیست(یوتیوبر معروف) یه چالش خفن اجرا کرده که باید خودش و دوستاش از دست 100 تا نیروی پلیس به مدت 12 ساعت فرار میکردن؛
برای اجرای این چالش ماه‌ها زمان صرف آماده‌سازی تله‌ها، دوربینا و مسیرهای مخفی شد و حتی یک شهر رو به‌صورت کامل اجاره کردن.
خود جیمی (مستر بیست) و دوستاش به مدت چندماه تو یه شهرک نظامی، آموزش‌های نظامی و امدادی دیدن و جالبی این موضوع اینه که مستر بیست برای خودش 50 تا بدل درست کرده بود تا پلیس‌هارو کصخل کنه.
این ویدیو یکی از پرهزینه‌ترین و پرچالش‌ترین ویدئوهای یوتیوب مستر بیست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70584" target="_blank">📅 21:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70583">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=T6QN-JuXtiU2O-cCWaPLr61VCf7x3wpfHA9-bVsYkbEuxGiNxsnfSOoASZ6oYGVU5_NVPLgJTmqmO1D3vFWadUv1CXi14SJoH9XExs-pVrI5gNuBUnSKbmsiL0mkEMVZ0ql0wQ9dIj1aK7CO_IYRswCH_tAZyWFyadlJWbYHjWFjYs9IEjWkem3e6DhctNwuCXMwehwXno5W-cUURgpKnLqJ0YiEQsAs0KtrINh15SCx78HR4UhieALZism3goSShezbYmbhDWCv525Rb8wWK4qt0ABTi6JTBrCnLgpmVvPkwzQes2JRhj9ZCfeS7Yh5JfFeM5G7Ox32MxhBKR4NPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=T6QN-JuXtiU2O-cCWaPLr61VCf7x3wpfHA9-bVsYkbEuxGiNxsnfSOoASZ6oYGVU5_NVPLgJTmqmO1D3vFWadUv1CXi14SJoH9XExs-pVrI5gNuBUnSKbmsiL0mkEMVZ0ql0wQ9dIj1aK7CO_IYRswCH_tAZyWFyadlJWbYHjWFjYs9IEjWkem3e6DhctNwuCXMwehwXno5W-cUURgpKnLqJ0YiEQsAs0KtrINh15SCx78HR4UhieALZism3goSShezbYmbhDWCv525Rb8wWK4qt0ABTi6JTBrCnLgpmVvPkwzQes2JRhj9ZCfeS7Yh5JfFeM5G7Ox32MxhBKR4NPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
سوال خبرنگار از شاهنشاه آریامهر:
فکر می‌کنید در کشور شما کدام‌یک تاثیر بیشتری روی زندگی مردم داره؟مذهب یا پادشاهی؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70583" target="_blank">📅 21:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppXk4RvJpyx5Zb7SwQEI-eZ-LK9UJn7Ii8VjkxU87x9SyYjhHYUqIM-GfTynt25sDBVQSLAKJOKbFDqKiNW49B5U948YaMKm-VoXyZYFcy-A0cJccuZhV6bo7sTD0diPG8DxCuF9QRsf_uN_GGfdzelHNB-ZgEbYtfqaQLnw124uUB3PI98ctzArazkCd29HdtZicXdJwel1RgbFiyNZvRtfzr4i3-Ps9MdAZUbj1h8CrQDc0ds9ppWgPSCEJUXSBM-_ZLktAWVrikSvodYGHntv1sd0O3Q8KaExvG1LUkVdsoBCswnyVi9usfAg8b3lrZITWagy5fFye7aKybjTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxIZSh1Caj-4E7EMTylaU1XMqsXLZuJD7ZlipVr02Qg-jXgp2kbI7BQKFd9XGa_Gw6F_hvtMv5V-O7rB1RddSPRoLtt65WuzsL50hrhzR4Z_Kqch6EZtNtrS3HxAvJNyrg9R_TUygLvh2kBot-RGcbNcQsAEQ2ntZf0bjNw6XuOGTUkaud6S-zEw6XBfswTvEGps34_RmLL3L640D_vY-sMT8zQKHULbMB3Qr7qEIZPi6p6azmd8o4jr73nIH_Loq64PKbYkpJEA4uu1E3BnnpIQF57C92gEhKU1-vOCnVFXIrcKaIs6pPQQrWSzs_nyNXI7GyX8LtTnB0hPyFq_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ob_deVphfEs5WM29ziRxcNJimGACn7Kvgzs0pyKtUVgJ1TWM91BMwnCR38kktOJ2v0_jXZYMxy2a8sBcrkViw0tqGFHuSulDvzuR3jfQn67MfUx83-LPPpasv-slo5XRv44YaYXW9NjEciiztfrH0mOX4c7CDEhceuX8pX-1xTXD0Hjt3uTEo1OOiIwr42CoDrhpCPndqEL6e3gLbb60Y023lyQsIYNpOBFaAHpSFsrHjhjed3K3XsBqVmb306R8JKe9-GYR0iWnlXpvdslRBwHtCig7XRSBathXoa-fnUsIrYAw3p3pfvDjSxLRczWIMO04N1iQQZiz-apKowzq4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
〰️
🇺🇸
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
🔴
رهبری ایران به واقعیتی اذعان می‌کند که اکنون برای جهانیان آشکار است:
فشارها کارساز واقع شده‌اند.
🇮🇷
مسعود پزشکیان، رئیس‌جمهور ایران، ضمن اذعان به کمبودهای اقتصادی کشور، اظهار داشت: «جنگ باید بالاخره روزی به پایان برسد.»
🇮🇷
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر سخن گفت: «هر چقدر هم که قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و خبری از گردش مالی، رشد اقتصادی و تولید داخلی نباشد، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری همچنان به قطع تمامی شریان‌های حیاتی اقتصادی که این رژیم را سرپا نگه داشته‌اند، ادامه خواهد داد تا زمانی که تهران کاملاً منزوی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70580" target="_blank">📅 20:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70579">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m2LWwAPUTnQqjZfTGUCw1mESYT8dYreSgWPo7NB7f__ljch4DpRhP4fq92cqZccPjrV0zpSy1DNNpnK2ryYPF37ZmHVZBWne1lslZeMRGwsHE8pje_rOLjbQhhJ33ThqijCcWhOGRWsv3qpGc0VT6dnDjuSyMthcY31MtS6jElNKVShrKE6BB_f1DyUK1ryMoLvfT-Raua340toZgOkwQZ0hxZOurovrFQQYhiwDAPCbgtdTUCd1X5rByuumS2NJeQWM-ckksfWBSnR83ivhOOaEHTHnFDY1_THx8RG-ucRnGqqpV27gPJ8yTTdeNWUTkEVZN63xsmfHkp1JiD2_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
اکانت رسمی تلگرام در پلتفرم ایکس :
امروز به کراشت پیام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70579" target="_blank">📅 20:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70577">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=gzv2mZvwDdtkw5vYTi9Y4WwRQ2BkBudcZchwf33QFqWe9nBMjFVKhSrG5ifQ1kZNhgRNKKbcHVhMp7vLarLLBmfwJdi0gQcKF01c_MV-Feod05RAxdkEtkhyN03khl5feEP06GKwAQQkezKhgAyDVUETZmt9RyPiiZzLodjDh8yfpYo0cztxkXxCteIRcdmRAX5OCb2b_SeMzrRyyMcp4PqDdxQ3jRxasiY9lw_TauZlviw3UB5HQdDJTJNsWSASGrmyXs6lql_BG0dAiAy5EO4sBejs8NidclZCCciu9zdHjnsBThxEkKvPxp3QJsK2WLVHvBojWZgZv_Dqt7hQXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=gzv2mZvwDdtkw5vYTi9Y4WwRQ2BkBudcZchwf33QFqWe9nBMjFVKhSrG5ifQ1kZNhgRNKKbcHVhMp7vLarLLBmfwJdi0gQcKF01c_MV-Feod05RAxdkEtkhyN03khl5feEP06GKwAQQkezKhgAyDVUETZmt9RyPiiZzLodjDh8yfpYo0cztxkXxCteIRcdmRAX5OCb2b_SeMzrRyyMcp4PqDdxQ3jRxasiY9lw_TauZlviw3UB5HQdDJTJNsWSASGrmyXs6lql_BG0dAiAy5EO4sBejs8NidclZCCciu9zdHjnsBThxEkKvPxp3QJsK2WLVHvBojWZgZv_Dqt7hQXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر ۱۶ ساله رونالدو و دوست دختر خوشگلش:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70577" target="_blank">📅 19:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=OTxiwrh_nRV5jZo7RVz-xMz4kN75gEjeeXin8gmUjiLUu09O60pRWYAq843hHEwX1xsR-sKUQPa6aJKiHLao65pDfjNt2pKTUc8XZmfRWDo489qToWCuva_kIRKpAGCRGWjoR3r31BwnjF3WhI6f_uSgj3Lq7z1EH4i4_FaVa1JEQKGhlRJc2DfeJqa5cCGAPcOm3lyC22mssTYoUC6pDPyGKf5KDHaxUWikVO0aQb5nRXqnpmbyZ-rM06j_1wmVyTJH_taSc9nHCH5I6U6WTpjzPobrLeFmYc0thxV6pYO3YBs7rwperWBwBllW3RvbFGLiwC57KAn-AXCNbcLVu2gnFCQNwDz_rZA2v9XMCIdiYbjusC5k8VUnI3cM48tEu4TywZglZ4_xF2YmjNLfwVE955boBS9Sc00Tp-UJhZXk2orYxabg-QXH0zq35OvFDN9GSX_FUlVCFULR7jM8vT7-CXjpWKEDdAsV7I_V3ShZAMoe9L0VddukSj6UDeioHVT5R95wH90BbQ0UpP2CydoB6al-GYTxoRVzShUrB5CiPyE-TMeHnOW5uDFpKVpBvMBpjqWiJicI7y2EkF-c3AtXoitUsapuiATZlM6hJwVn8xFzPA-rgryuh-U4KywTZn-CJG5KBknHcmSxCFY-NrR4Xwb4xJHlRKBogf0nr1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=OTxiwrh_nRV5jZo7RVz-xMz4kN75gEjeeXin8gmUjiLUu09O60pRWYAq843hHEwX1xsR-sKUQPa6aJKiHLao65pDfjNt2pKTUc8XZmfRWDo489qToWCuva_kIRKpAGCRGWjoR3r31BwnjF3WhI6f_uSgj3Lq7z1EH4i4_FaVa1JEQKGhlRJc2DfeJqa5cCGAPcOm3lyC22mssTYoUC6pDPyGKf5KDHaxUWikVO0aQb5nRXqnpmbyZ-rM06j_1wmVyTJH_taSc9nHCH5I6U6WTpjzPobrLeFmYc0thxV6pYO3YBs7rwperWBwBllW3RvbFGLiwC57KAn-AXCNbcLVu2gnFCQNwDz_rZA2v9XMCIdiYbjusC5k8VUnI3cM48tEu4TywZglZ4_xF2YmjNLfwVE955boBS9Sc00Tp-UJhZXk2orYxabg-QXH0zq35OvFDN9GSX_FUlVCFULR7jM8vT7-CXjpWKEDdAsV7I_V3ShZAMoe9L0VddukSj6UDeioHVT5R95wH90BbQ0UpP2CydoB6al-GYTxoRVzShUrB5CiPyE-TMeHnOW5uDFpKVpBvMBpjqWiJicI7y2EkF-c3AtXoitUsapuiATZlM6hJwVn8xFzPA-rgryuh-U4KywTZn-CJG5KBknHcmSxCFY-NrR4Xwb4xJHlRKBogf0nr1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صادق خرازی:
به آمریکا در افغانستان کمک کردم و حتی فرودگاه در اختیارشان گذاشتیم اما جرج بوش ایران را محور شرارت نامید!
بیشترین خدمات را به آمریکایی ها دادیم و حتی خون دادیم
این نشان میدهد یک جایی در پشت پرده محاسبات دو کشور نمیخواهد رابطه ایران و آمریکا به جایی برسد
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70576" target="_blank">📅 18:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70575">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=Hi_Wh3reoY0g4br-UDGm4cuYTWVYg6QT1JO_71wOa-caEY3jcmOeXi8pb2U4N8QM4LV6BgoGs9EiTbqpArjfH4Ucij7Xg1q2gKrg0PvPIfZxmKuzQEW0gy3DmloXUjUiLz1cpZrUJS4csnOmaj2xOIVj2DUIKEzXNXqSsp1cE7e6laeVhSS4OQ28iatbZ2i9V51xAsKHl5zbs2QU1GMDdjIaM_eFuAkHXanNsVP9J2ZqJUpteh6HsylE15-xzZemRovEO3tkj2KeR9ADGYVYdMjCfyPworoxMoCiRSgstPOIg0iDkz0iiQxX8AGS5iKm2KA4JQnzViLKxt-e8jA0vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=Hi_Wh3reoY0g4br-UDGm4cuYTWVYg6QT1JO_71wOa-caEY3jcmOeXi8pb2U4N8QM4LV6BgoGs9EiTbqpArjfH4Ucij7Xg1q2gKrg0PvPIfZxmKuzQEW0gy3DmloXUjUiLz1cpZrUJS4csnOmaj2xOIVj2DUIKEzXNXqSsp1cE7e6laeVhSS4OQ28iatbZ2i9V51xAsKHl5zbs2QU1GMDdjIaM_eFuAkHXanNsVP9J2ZqJUpteh6HsylE15-xzZemRovEO3tkj2KeR9ADGYVYdMjCfyPworoxMoCiRSgstPOIg0iDkz0iiQxX8AGS5iKm2KA4JQnzViLKxt-e8jA0vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
نگاه هویدا به یکی از بی‌شعورترین و بی‌سوادترین مخلوقات زمین
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70575" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70574">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70574" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70573">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAjCFU9GhqhJ90xrHvTNLdOHNW4ekCrm5DgSL1jFeaUK_-yBC4umu_H5O09ug9UUZ85QYGWxXlu5nl-_vKdbvJFrVkz0khSV4mPXd6phS9NbeFZ6ZLKaAtBIGTD974u_DG0G1xphgp75oqGAJ5gSMz8v7oJPQIVGVXgDC5CEArXsGFP5vxLljU05JLeq8OJBnxduMfl-ALB6ko_8rcyRCqV_zVNIkZXJw7TiggDh9ILQkrki7K3gk9O8dtjJ61Msi3_8EWetT9hq1hJfldaLKQJLq2d8XyculCZ122HPulEWIl9ATMnFydQxScgXpUsK3LiIRoZg7f4zJyeBHn4ItLiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAjCFU9GhqhJ90xrHvTNLdOHNW4ekCrm5DgSL1jFeaUK_-yBC4umu_H5O09ug9UUZ85QYGWxXlu5nl-_vKdbvJFrVkz0khSV4mPXd6phS9NbeFZ6ZLKaAtBIGTD974u_DG0G1xphgp75oqGAJ5gSMz8v7oJPQIVGVXgDC5CEArXsGFP5vxLljU05JLeq8OJBnxduMfl-ALB6ko_8rcyRCqV_zVNIkZXJw7TiggDh9ILQkrki7K3gk9O8dtjJ61Msi3_8EWetT9hq1hJfldaLKQJLq2d8XyculCZ122HPulEWIl9ATMnFydQxScgXpUsK3LiIRoZg7f4zJyeBHn4ItLiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g3
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70573" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70572">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHPy5ZKjuB-ztWvD5r1u8BfCAPaZcoiQ_fNWSQ5wUOxVWmDxqtfRmWDtjUrkU-1j1y3DIpv11E1p9bVOY36XixDiNnT15GZZSVb3RSyKFFzyEmWsZBCAMrB4aPdOVA-DlD3DgLE-JnowAWDbPYTGbLqYm6qpc8voZArkl6Wfp13oc7muPbT3ttwY_ZYjaNmH2RuDvNIcyXw-8PzzwIXLjXx_5de4-5M19geuXfCD2oIQHUirVFZutkMbpagnhqZp0Z-hUC8olU7e-3zmRSKuPHkK9v1_sT1lq62Ub3DShG_3-KFU3CWqKZoGwr4DwRFqJAJywCapSbQ9VY9OtlWxgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
نیروی دریایی ایالات متحده به من اطلاع داده است که تمام مین‌ها از داخل آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدیدی را در آن کار بگذارد، فوراً و به طور سیستماتیک منهدم خواهد شد.
ما از طریق نیروی فضایی، هر اینچ مربع از تنگه را زیر نظر داریم، همانطور که در مورد کوه پیکاکس و سه سایت هسته‌ای دیگر که قبلاً نابود شده‌اند نیز همین کار را می‌کنیم.
سیاست عدم تحمل در مورد مین‌گذاری با تمام قوا و به طور مؤثر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70572" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=d6qscwA1J9sN_G7yhDWqJYrNNQo9uAEMu2OM81y6YHr87ltDbQW9fv037Fv8e6FDv5sWNWt3PudA_Oz0fA1Mry92X3RtxexS9y4NIH-GAIk9u86rnfj8Sye4uTqNKngyxEgsa-CddbF8jUsUrPKfWKhmHWAo_tNSD5jXIGWxrHiKvr1Ba-O2ms_G_kTvDpLiS-DQpcurd8T7YEtVbrTnCXaZiEodaIp1lHp1HpXttI5aGVnuIACXBx79EpGdABlFBVPri2cSnmzYMO8SgfdcMABs9jg5bHaX1PRk-BhJ2W4zytp-BH1hPOygS_6XngtfECTDP5jpn_OsQbKpBV3lBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=d6qscwA1J9sN_G7yhDWqJYrNNQo9uAEMu2OM81y6YHr87ltDbQW9fv037Fv8e6FDv5sWNWt3PudA_Oz0fA1Mry92X3RtxexS9y4NIH-GAIk9u86rnfj8Sye4uTqNKngyxEgsa-CddbF8jUsUrPKfWKhmHWAo_tNSD5jXIGWxrHiKvr1Ba-O2ms_G_kTvDpLiS-DQpcurd8T7YEtVbrTnCXaZiEodaIp1lHp1HpXttI5aGVnuIACXBx79EpGdABlFBVPri2cSnmzYMO8SgfdcMABs9jg5bHaX1PRk-BhJ2W4zytp-BH1hPOygS_6XngtfECTDP5jpn_OsQbKpBV3lBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید باورتون نشه ولی ایشون بخاطر اینکه آلت تناسلی بزرگی که داره، گریه میکنه! میگه تا میخوام با دخترا رابطه برقرار کنم، جیغ میزنن وای هیولا، چه مار بزرگی و فرار میکنن
😢
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70571" target="_blank">📅 17:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb0dbc493.mp4?token=kdneqxLZDO8JiKs4hAIaM7k9vsWuZc3xJuiiTb6_fqqOl5Y7omFApbDg7OENC4tc_PkGCK2JoTkE88Fy4cmOmbNbzuzEeu_w8vYKzKwWDv_t0U-oa6dhfHPmUu3FKFYTsGWA7S2mXHfAjw4J99ZXc0XgoiY4WkUwpPN-fnT8nr1reGahVjpdIHm6Kfz1O1bhqXM2g9RcwNgYjdZkauKkX2vSt00yz_aBbgA3yZ2-WMjfS16g_PDYSUc7ntxGDSus02ExZVL9myD_NqsWmdAdxGXi56jNFIA7W1fKurZEUx1zC_ksNxgCnIFNe1rS_7CmyBEhacR7V9inpYCg0Jx5cKmm4su1SIWxGY-cRPp6oUMngMrhRzRV-i9hD7k30-5RCiSAOE5oCsPQzmvXRUhEFYgfyh3OLJd2DCojrF9KsWrBr5bEDHZH-ddMVA_i-fSaMD5xASohPjCH_7_qRQOT3xyDo6dsUpiAdgsj9OviVSOJnhT79H35y4t9jH5PhHK4EJewdkxD-rNXsw7giRQfMpW37-J3WWDVwP7UjjBMI5MfkxWFJqFEEQgb4enciYllIWcXh_C0bVWwuKCE1fPDHuJARuUSx7WMtBX8Cb7cq3eEdiu6BDxr04-13E19MvzkM5ZsMMx5xDGx-yFLCCaihQ-ka8OZiAX6oCQYqPj7j7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb0dbc493.mp4?token=kdneqxLZDO8JiKs4hAIaM7k9vsWuZc3xJuiiTb6_fqqOl5Y7omFApbDg7OENC4tc_PkGCK2JoTkE88Fy4cmOmbNbzuzEeu_w8vYKzKwWDv_t0U-oa6dhfHPmUu3FKFYTsGWA7S2mXHfAjw4J99ZXc0XgoiY4WkUwpPN-fnT8nr1reGahVjpdIHm6Kfz1O1bhqXM2g9RcwNgYjdZkauKkX2vSt00yz_aBbgA3yZ2-WMjfS16g_PDYSUc7ntxGDSus02ExZVL9myD_NqsWmdAdxGXi56jNFIA7W1fKurZEUx1zC_ksNxgCnIFNe1rS_7CmyBEhacR7V9inpYCg0Jx5cKmm4su1SIWxGY-cRPp6oUMngMrhRzRV-i9hD7k30-5RCiSAOE5oCsPQzmvXRUhEFYgfyh3OLJd2DCojrF9KsWrBr5bEDHZH-ddMVA_i-fSaMD5xASohPjCH_7_qRQOT3xyDo6dsUpiAdgsj9OviVSOJnhT79H35y4t9jH5PhHK4EJewdkxD-rNXsw7giRQfMpW37-J3WWDVwP7UjjBMI5MfkxWFJqFEEQgb4enciYllIWcXh_C0bVWwuKCE1fPDHuJARuUSx7WMtBX8Cb7cq3eEdiu6BDxr04-13E19MvzkM5ZsMMx5xDGx-yFLCCaihQ-ka8OZiAX6oCQYqPj7j7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ارزش پول مملکت رقابت شدیدی با گوه داره؛
یه مادربزرگی گوشی نوه‌ش خراب میشه و میاد این پولارو میده به طرف که گوشی جدید واسه نوه خودش بخره.
به گفته‌ی خودش این پولا حاصل 6,7 سال پس‌اندازه. از دو هزاری بگیر تا ده هزاری جمع کرده که تا موقع نیاز ازشون استفاده کنه.
حالا طرف اومده پولا شمرده و مبلغی که به دست اومده خیلی جالبه‌:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70570" target="_blank">📅 17:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439a914edd.mp4?token=PZOeW-SVdDr_vIFu5CqP8TRI_lGgSJmEfoMAZt4mSE61pznlKKETZi8XohDNrZ_lE0SIsXCpt4yWqqNN-yvieOju7Av2hrHpDwIA6dyku8yAOZDaOlC1OBifkEbG7zsx35H2jSRBGD71QGwR-V9wd2LoAcORhlfZk0fwyZda1q6WmzD0k8_RXAgpw-zhQoPjX8IvpfRsMJ8Uikmw05bAGQ3dRpj5tsgpA0O2KSdBpGoEYCy95NT-ths6Ya_GxrqGX0cZBadBbBELefi0tQm-gt63yjo597hEdm93guKJrGHAyIEsP67ffdVo89w3tA3ec4dWiqnLzLbbEtATqokiGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439a914edd.mp4?token=PZOeW-SVdDr_vIFu5CqP8TRI_lGgSJmEfoMAZt4mSE61pznlKKETZi8XohDNrZ_lE0SIsXCpt4yWqqNN-yvieOju7Av2hrHpDwIA6dyku8yAOZDaOlC1OBifkEbG7zsx35H2jSRBGD71QGwR-V9wd2LoAcORhlfZk0fwyZda1q6WmzD0k8_RXAgpw-zhQoPjX8IvpfRsMJ8Uikmw05bAGQ3dRpj5tsgpA0O2KSdBpGoEYCy95NT-ths6Ya_GxrqGX0cZBadBbBELefi0tQm-gt63yjo597hEdm93guKJrGHAyIEsP67ffdVo89w3tA3ec4dWiqnLzLbbEtATqokiGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70569" target="_blank">📅 16:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70566">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AgicJ3639uzyGRkAbHmW7cY8jSM4WLyjKHgdRaLWb08nfIYfG2DqVpvVnwEDCcQeze8v1sMRBCkGlXpGXTuCJ9uTzNUVna85eg-LQ_r7C7HRTHyLhARgQfztAdo_D6wwtIKvbsnR8yjZcI40ZbaI2K0VSZIhPoyjmJYwcEuHb5kAXf63_yp7TwFzdgUojTsumMMhe5eVvkxaJdKzWhS3vsOlS84SPvA09JXTBBU7bnVcAeiWC8MJHyNq6Wpeo5ZEU-N05FUSMXUvUPDisov-4vBfe7shiGAIFKSBlvI6zNv_yLybaYthNklJNpHVxwDTdUO3dTloGts4xIl5VZgEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmgNtTmNTntdXbnvk1oeDKpMUok1D4-qeVUuok463Wcdjkeld8ANQdGILGa0ZGlUTzh8Di5YpdefYKSyq3CYKJtARvq2ErZc6CMNPxGPuHkXrTsS0ufNv0M69MI4Y1ffBFUDpeWuDqyKDRxYv8xk1fxob-2peqi3AhJwQNaMUL5-pQxe4QCKS2vzilt6iOqBgWZwbXr4fzgC0I4J4GmRDew_3I3NALIaTR9x6kNTft6V1v7VBsZGAmz-J1I_i6KNfGN381n1Uh4SxBynibI33VSxunN2frH1Jcirqpxouogj4_45RQbFUKg5fYq3vZBK4c2MI72h2ujcSW3jKS-ngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRvEXT2f6q1hoNUu-AOpfqiJgOmOcRWeoyNlYyEtsx5PPQUJqxNNSHXcW72YzWv_WLhOawgxyLEc8CTXKY30RXiGAAIWb1EN1x8MAVtkugnoB2QoSrz-5PQ6i4YglV5UfKxTWmUaJCpWCqWxpYOxYIjAB_jty7Z53hbkyfHnuKXa8hMKQmVQcoKH1QKdHj5wFq-Gt44l0IwGrJmzBnGTkXDTvhR_4BYKjFiFSvoJtdUl8h-Y9leW4KOO4J4ljYW4C9OHWfQexwX-6REsxX_TJm81oD4pV5eNGfRtxgddgIyMl1RXQqi-gG5va3SNzuA3YriARnunue75jaA0IOIc1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇴🇲
🇮🇷
وزیر امور خارجه عمان، بدر البوسعیدی، با عباس عراقچی در تهران دیدار و گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70566" target="_blank">📅 15:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70565">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVjvUXUa4IYdLjVkMlB_ff7S3O9EIFoVQgEaJ4L_GjiGLXRa7F0RsEpsaYwTaF5LL8xjB0Y4k_m1O4tdLOuS_ZlqrWbqzVDHmc4iTT1IWpP35x3T82sBJF_Z5Hj6zIzjDTU6VY9XhBfKbldDnLL5xpS6Q_Y9GQL360hPUZrMmmxFWx1Z4ciBJCKDKOuC26DstjUGpOOBk--wl70xEs05P_qIu9Q4nGSscf9qDIq0UnW1fvkEFZE56CpBZzyKvDOvfrUnn_VjY555rBe0i3qgaFX70s71Ck2z0VR8C3QP7a03_t44G1OvxcJHW8UVr4sIGJrfpPM9U3ERsbGYCbJkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
بانک ملی ایران در سال ۲۰۱۸ به دلیل حمایت از تروریسم توسط وزارت خزانه‌داری آمریکا تحریم شد، با این حال همچنان در سراسر جهان شعبه دارد. اسکات بسنت (SecScottBessent) وزیر خزانه‌داری آمریکا به‌تازگی اعلام کرد که تمامی این شعب باید تعطیل شوند.
🚫
مکان شعب بانک ملی به شرح زیر است:
۱. امارات متحده عربی — ۷ شعبه (دبی [۲ شعبه]، شارجه، رأس‌الخیمه، فجیره، ابوظبی، العین)
۲. عراق — ۳ شعبه (بغداد، نجف، بصره)
۳. عمان — ۱ شعبه (مسقط)
۴. آذربایجان — ۱ شعبه (باکو)
۵. آلمان — ۱ شعبه (هامبورگ)
۶. فرانسه — ۱ شعبه (پاریس)
🚫
بانک‌های تابعه / سرمایه‌گذاری مشترک (در ۴ حوزه قضایی)
۷. بریتانیا — بانک ملی پی‌ال‌سی (لندن)
۸. هنگ‌کنگ — شعبه بانک ملی پی‌ال‌سی
۹. روسیه — بانک میر بیزینس (مسکو، کازان، آستراخان)
۱۰. افغانستان — بانک آرین (کابل؛ سرمایه‌گذاری مشترک با بانک صادرات؛ وضعیت تأییدنشده)
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70565" target="_blank">📅 15:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70564">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjltNpJYgmzTo0F3dFDsOZ1Dlj5XtpyldjoWAtTrIBT6nGYEyw7Lu326p9mwfr0OquYAMOENIl-nFcRe-YIwobcd4HZ06KwkAY6IXYkMonw7cYyzjYP8Ursr8FCaUcQ8Kyq_YGKk876WP7PTWVOrqXWYqxGEwNOqHGLZVLEF2jaHxKXnxeCzSMHhy2bf4zZCdQBIkxQrg8ieuSsQKxcBtMDIFNy0PaI0up15Psq6CKJ6mhiWTSd0wfWb5MS9-Jb_vqsDrVpqq7H8WZPt4cOGzjNt_tOydYyOta8gW--7Bil3_GUBZNEKQmDlBH6iH9j_cUkZAUbXHD2Aj1F-00tc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی ایران که در حال فروپاشی است، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را — حتی زمانی که مشغول اعتراض نیستند — با شدتی بی‌سابقه به قتل می‌رساند. این یک بحران انسانی با ابعادی عظیم است و باید همین حالا متوقف شود. رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70564" target="_blank">📅 14:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70563">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=scXAovUXcVAkGhcUFv95ZkmHbbks42gy1Z8qctNn_mr-K__KEAopYAV_FUDRhiZUS1UkJ_obbH3lR8uQYamPekJXe2v-mV_2y0eXBbc5Z8PMsj2R4yqoeiKOTdkUf-fF2AO5ZumnxpPLjgyEQn-FszyhsH0DiNd4UTIdVq6JTRWlWBrB6GkI15pzmG6_3QaNr5c5n8_YkuFl3lY5Tk1CwOK9C5q_N5qoJ4_c4SkY2ycswz40K7Twr_BJpO62UveGT5y-TNFrw2MN_6QZ7FGFGj4hM9o5LhLbRTz7rqchJg-d1gam1nE4anr8jJjoLTT92ebzVEYOb1PGne5lTeYjWTLfXCZR1h7BHQ_7NzcSaJPk805KtU4LWaPT6x2r5Uv239-EOMX_6uib-hV20oe61NacCwt2vTm8nH-l-i2vFFpTRlbU8YlQoKDgakmQoyokjzXdVN-R0KJ5c40zyHiKFtLmBgK_bRSYtnWMj65_CA04VBFktRTpmKZ-XvhUsFhHJRTAt7lz_cSIvAY2-1aWuuZTSJjT1i1PMXcCwsoVANGQrRLFOETBk81_31NIS713JMdRiTenOoPFKCbjgCDnqiHd0ORCTO3wb0BJehS9bvbnSJaTV47CfXL9F6hHPzn1xYCDRkcOymUTZ8tVqh3PnNsb1onjZbBFoYp7P-77-tk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=scXAovUXcVAkGhcUFv95ZkmHbbks42gy1Z8qctNn_mr-K__KEAopYAV_FUDRhiZUS1UkJ_obbH3lR8uQYamPekJXe2v-mV_2y0eXBbc5Z8PMsj2R4yqoeiKOTdkUf-fF2AO5ZumnxpPLjgyEQn-FszyhsH0DiNd4UTIdVq6JTRWlWBrB6GkI15pzmG6_3QaNr5c5n8_YkuFl3lY5Tk1CwOK9C5q_N5qoJ4_c4SkY2ycswz40K7Twr_BJpO62UveGT5y-TNFrw2MN_6QZ7FGFGj4hM9o5LhLbRTz7rqchJg-d1gam1nE4anr8jJjoLTT92ebzVEYOb1PGne5lTeYjWTLfXCZR1h7BHQ_7NzcSaJPk805KtU4LWaPT6x2r5Uv239-EOMX_6uib-hV20oe61NacCwt2vTm8nH-l-i2vFFpTRlbU8YlQoKDgakmQoyokjzXdVN-R0KJ5c40zyHiKFtLmBgK_bRSYtnWMj65_CA04VBFktRTpmKZ-XvhUsFhHJRTAt7lz_cSIvAY2-1aWuuZTSJjT1i1PMXcCwsoVANGQrRLFOETBk81_31NIS713JMdRiTenOoPFKCbjgCDnqiHd0ORCTO3wb0BJehS9bvbnSJaTV47CfXL9F6hHPzn1xYCDRkcOymUTZ8tVqh3PnNsb1onjZbBFoYp7P-77-tk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر اقتصاد:
تفاهم‌نامۀ اسلام‌آباد روی کاغذ نکات مثبتی برای ما داشت اما اسرائیل و تندروهای آمریکا نتوانستند آن را تحمل کنند
امید داریم همان تفاهم‌نامه یا بهتر از آن احیا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70563" target="_blank">📅 14:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70562">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XugW19eJMUMqYEnyEQ7vzHPYHyYOtuz5pilykqY6wwhz8vS4hdnn4ZLgsVYqFXiRUqN82yTN-2pBEzSttQYRzo-FmO-N8JgvUSqcQfxhLtgA6L1Xf1FkVtRbBce1HZQtV7hTRdneFEEPB3FJYf_BdSxXNLObD8Lbkvqrc2U4sIzXFfjEDj1gjMQ4AD22H0tZKv1Sh5xBd85m8bN7Ch0-HkAjIsr36dvJv3Bmn0ix209vaEAyQy5Ehb_44aSOKZ28MQGkdlONbkxzNnK8axFHTFnnyk-mnmQcukdyfb42qAHfLdFOkECwB1G6a9931WzawkhWx25bJNb6KBIeDqQcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
حساب اسرائیل به فارسی:
درباره ماجرای دایناسور خراسان، احتمالا فردا امام جمعه مشهد می‌گوید: «این دایناسور از برکات نظام و نشانه پایداری ما از عصر تیرانوزاروس تا کنون است!»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70562" target="_blank">📅 13:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70561">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
📰
اکسیوس:۵ نشونه فروپاشی اقتصاد ایران زیر فشارهای ترامپ:
⚪️
سقوط ریال؛ دلار به حدود ۲۰۲ هزار تومن رسیده
⚪️
تورم شدید؛ پیش‌بینی تورم ۲۰۲۶ به حدود ۶۹٪ رسیده.
⚪️
فشار معیشتی؛ گرونی و افت ارزش پول، خرید مایحتاج روزمره رو برای مردم سخت‌تر کرده.
⚪️
سقوط صادرات نفت؛ محاصره و فشار آمریکا درآمد نفتی ایران رو به‌شدت کاهش داده.
⚪️
رکود و بیکاری؛ فعالیت اقتصادی و اشتغال افت کرده و پیش‌بینی میشه اقتصاد ایران امسال حدود ۵.۴٪ کوچک‌تر بشه.
با این حال تهران قصد تسلیم شدن نداره و ممکنه دست به اقدام نظامی بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70561" target="_blank">📅 13:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70560">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a518ac30e.mp4?token=JTBaCHkEvDAjdRm5ZSDP_nWBp4APPM6UL4qYbG5iuV8lqHCRLmq8CQhcArebxm6PwooUG1JAo1F5fKsjGu3rQ_5PyatoXN5tjhfCMpI-s_3eXM7dzLNP_saDHALtauZOQmEfBuaWjfVW9vqPIZc9v81BZG-5EF3qkAUWquHvk1iRRvpVibC9wrSEqYr94l7lCyYuilKmjAoWg25gnKFJMZ5sGqq66VTyuV5x5L3BqNOVXm0Iq4_tsWD7DieaJJUFNSSXRRK31iaPnrbcoK5gTubFgxnrUCRre4cfz6OH2NqlMhQpP1pE7xmk_jXcyZBn2UsMxFbFKkuxW-dDj956Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a518ac30e.mp4?token=JTBaCHkEvDAjdRm5ZSDP_nWBp4APPM6UL4qYbG5iuV8lqHCRLmq8CQhcArebxm6PwooUG1JAo1F5fKsjGu3rQ_5PyatoXN5tjhfCMpI-s_3eXM7dzLNP_saDHALtauZOQmEfBuaWjfVW9vqPIZc9v81BZG-5EF3qkAUWquHvk1iRRvpVibC9wrSEqYr94l7lCyYuilKmjAoWg25gnKFJMZ5sGqq66VTyuV5x5L3BqNOVXm0Iq4_tsWD7DieaJJUFNSSXRRK31iaPnrbcoK5gTubFgxnrUCRre4cfz6OH2NqlMhQpP1pE7xmk_jXcyZBn2UsMxFbFKkuxW-dDj956Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما یه ویدیوی جدید با هوش مصنوعی درباره پسر ترامپ ساخته و اونو تهدید به ترور کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70560" target="_blank">📅 12:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70559">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/377055b126.mp4?token=EEr2kUQrTua8tAqJd_vioNnggZzP1bKPXG_foJ4vJhM3leSp2UXTx4DzavRkKiPVl8TtXpqrDLpfeEhkKBsYnM0yKZ8z63lg5KVkFu59ACNNfjVE9fUYFmRwsCC4k632sXXJKtfkXVnRhvwNuRAKHLj305xiftz-__bXOq9nZspQ2wYPhsFonUmux9kjOgtZvGkaav0l3LpGjB1mgvXWJ39Gx4Za3GG0NsF0ghFNILCASA-vjQLFQ1gCzUuHaRQGYUjdnksXZeTx6L_3EzJ9jEhtBsJsX7ugEi1yVEukuCHZn1LDVrf7X47VUPLb2PBp0ULql72MdbeKAgItSnGkSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/377055b126.mp4?token=EEr2kUQrTua8tAqJd_vioNnggZzP1bKPXG_foJ4vJhM3leSp2UXTx4DzavRkKiPVl8TtXpqrDLpfeEhkKBsYnM0yKZ8z63lg5KVkFu59ACNNfjVE9fUYFmRwsCC4k632sXXJKtfkXVnRhvwNuRAKHLj305xiftz-__bXOq9nZspQ2wYPhsFonUmux9kjOgtZvGkaav0l3LpGjB1mgvXWJ39Gx4Za3GG0NsF0ghFNILCASA-vjQLFQ1gCzUuHaRQGYUjdnksXZeTx6L_3EzJ9jEhtBsJsX7ugEi1yVEukuCHZn1LDVrf7X47VUPLb2PBp0ULql72MdbeKAgItSnGkSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این شما و این برج زنبق واقع در منطقه ۱ تهران:
۲۸۰۰ متر پارک و فضای سبز اختصاصی.
هلیپد برای هلیکوپترِ اختصاصی شما.
بیلیارد، سینما، سالن اسکواش، باشگاه، مجموعه آبی، کنسول PS5 و سالن ماساژ.
اتاق بازی کودکان، فضای اختصاصی برای جلسات کاری، غذاخوری و...
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70559" target="_blank">📅 12:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70558">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e23f896bb9.mp4?token=IEA-DGmTLp9lTe7a28Kmxo3ryWS4eCCdO1j-cTxTQoINU-M7PWTxEnDOi1npvsF2pmbKIjhr9ohK0OOgAvRBV14YjDkOPiZItjGoGyWPKhE9O6s0uNXYrlTN6WuODuhYwfHahcmvUBE7koOhO7ZyP2xxIx0CgPz7UYm2Jn0fVPetFBp-1ky3e-BFg2p2JwzRz0bQAmFQAjliC7A-fGqALUr1IDYc0Mu8NsKSwfPxZpt0zaulOHoZqyV2utIkiZoAAJ_oa8tcHsff5Ni3i4t-h5H8Jy1nQg6jV8rCZ7sQ0p2k_TqlOJcV9AMnEgOhhGZyZk99580VRadPcNbnFs4mVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e23f896bb9.mp4?token=IEA-DGmTLp9lTe7a28Kmxo3ryWS4eCCdO1j-cTxTQoINU-M7PWTxEnDOi1npvsF2pmbKIjhr9ohK0OOgAvRBV14YjDkOPiZItjGoGyWPKhE9O6s0uNXYrlTN6WuODuhYwfHahcmvUBE7koOhO7ZyP2xxIx0CgPz7UYm2Jn0fVPetFBp-1ky3e-BFg2p2JwzRz0bQAmFQAjliC7A-fGqALUr1IDYc0Mu8NsKSwfPxZpt0zaulOHoZqyV2utIkiZoAAJ_oa8tcHsff5Ni3i4t-h5H8Jy1nQg6jV8rCZ7sQ0p2k_TqlOJcV9AMnEgOhhGZyZk99580VRadPcNbnFs4mVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه دختر برای پارتنرش شرط گذاشته که هر بار دعوا کردیم، برای اینکه باهات آشتی کنم، باید برام طلا و سکه بخری و پول بدی.
بعد از یه مدت رابطه، این صحنه خلق شده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70558" target="_blank">📅 11:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70557">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So-cWdIin5sf_0F7gHLvjQbzvd0Hcoj5G3hig0DaYyRCY4PjH4aa_OZeY5uEWONt9yywdpvfIF8hwBbI_hddXA5_5n1BQPJKM28a4yJoUmxGBZjtDBEieGzZLgb0KbHSJChn-quAZiJh0xvNkSSckFYm7JGKL-VZKI91sykxrVkEaC1CSSJkNoyytO3109XSjuJ0eqKF7A-LOtgckfsg-oce_9BYgNuzqflR7UFW3jecCgjIexgOoM2k4_hPy95xx84Hc9I1JAgy44s4o9P2Av9uFzEm2sHcZU3a1kUKnFg7VbPCFh5TX8dPcxWxoxCsj7ZWRurBeq69B7oC0KJY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی از زمان دلار ۳٠ تومن تا امروز که هر دلار بیش از ۲٠٠ تومن رد کرده به آینده اقتصاد خوشیبینه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70557" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70554">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=GyvZo_tV5av0UK6vQlXNJWMtmXMcXC23SbsCwbSYafadjq0V6kCLlhvGo8IFfx3iYsh9lKRqel_3rwDkUZWPZTw_niwauk_EKIFGM8nDDJWutiMRdlRWZBTWOsm8y9judInE5qGvol8eprw4K8_tY4DYAN8Nut-Z9Vsk5EOJrEzqUn_XU-Gk081iQkz4q93_mJs3l-X6_2aeTuIEqBsh_SrxFzdn_uNAz-IFd4zTLuO94Im9UCgNvKo7vG_dP8N6U_Mp_4H4sR5MecyJJaZhi59Q6YvD2A1CVi4Waz7bdwg3x_yJFHObazMJb0PThxvj66ilMpvU0QR2B9CIVlDZJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=GyvZo_tV5av0UK6vQlXNJWMtmXMcXC23SbsCwbSYafadjq0V6kCLlhvGo8IFfx3iYsh9lKRqel_3rwDkUZWPZTw_niwauk_EKIFGM8nDDJWutiMRdlRWZBTWOsm8y9judInE5qGvol8eprw4K8_tY4DYAN8Nut-Z9Vsk5EOJrEzqUn_XU-Gk081iQkz4q93_mJs3l-X6_2aeTuIEqBsh_SrxFzdn_uNAz-IFd4zTLuO94Im9UCgNvKo7vG_dP8N6U_Mp_4H4sR5MecyJJaZhi59Q6YvD2A1CVi4Waz7bdwg3x_yJFHObazMJb0PThxvj66ilMpvU0QR2B9CIVlDZJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی در طول شب سه مرکز لجستیکی اوزون را در سراسر روسیه هدف قرار دادند و تأسیساتی در آدیجیا، استان استاوروپل و داغستان تحت تأثیر قرار گرفتند.
این حملات در میان مجموعه‌ای گسترده‌تر از حملات به مراکز توزیع بزرگ روسیه، از جمله سایت‌هایی که توسط اوزون و رقیب آن، ویلدربری‌ز، اداره می‌شوند، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70554" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
