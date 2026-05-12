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
<img src="https://cdn4.telesco.pe/file/OolP85dvrP0V82WwvwWajpgo6zS7lzuXFzRX2Gp-FB7LRlFVRn7mkbvylYrPclyKFLKyNshPs_gaiiPJbVsCX74SbRTpoubo9dMLe-EnMbQSzs0syv-LdX4gwyl1osVMafF352Dml_Yka6Fc1-bpil77d-qIfTgGM3EdOgLOPlz7CZgZBPgYfJc-1PLkHZjG8SQdWFax18JBYsV3nrBp8KRH0sGzUFy22j0n7Er11miKG1yis1jeKEcJfp9qtttK2T1OmzShyuxkqXxHJ0-PE1xbo8qYOk4oAGjmIj_3PyxWg3F1ICTl2c6iMs_5JE-Im4U3ZKm7MGhxHqYwLDJPBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 58.4K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 16:50:58</div>
<hr>

<div class="tg-post" id="msg-579">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به دلیل تعویض زیاد سرور ها توسط کاربران، تلگرام ممکنه بخاطر امنیت اکانت شما دستگاه شما رو از روی اکانت logout کنه و دیگه نتونید وارد اکانتتون بشید!
راه‌حل:
1. اکانت تلگرام خود را روی یک گوشی دیگر login کنید تا در صورت logout شدن شما بتونید دوباره به اکانت بازگردید.
2. رمز دو مرحله‌ای اکانت و ایمیل بازیابی را فعال کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/whitedns/579" target="_blank">📅 14:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-578">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg7SCZQl7mkJlcvO9HCFSHfP_898C9n95FytvkjuznJVMApZWPhCGfpaX99Zr_Q92haMHUjGbwxBvTWu72pxfXLIZRqOXtgY8z9UI4V5E2EzZ4mR1UPd049xc5xJGZOeB_3TsrKGQq0xqXKir8LyZHsQaqwSsovGL2l0_pBGYyWkyWGKdsH6r-A3E4K9-mFcPfebM3ZnRqMKjlHhdypIg6lmnkksGIJpaDBTcLwtgEKIj35PNb-xwOQK6jhiAzCuauXlXzWG38h2jyqZXhFJOukVz3NZGQZqsX-sf2SCbRDeUy4Lc4XCFBpcruXsFy_HNbnPP-sDSt-Elz7GLo_70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
‏فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
‏ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام ⁧
#اینترنت_پرو
⁩ را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
‏ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
منبع
https://x.com/ircfspace/status/2054094958353678824?s=46</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/578" target="_blank">📅 12:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-577">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-poll">
<h4>📊 آیا به اپ WhiteDNS تونستید وصل بشید؟</h4>
<ul>
<li>✓ آره</li>
<li>✓ نه</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/577" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-575">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTY5txbhzw1TfZmIcCmwnjJZ30kR7ejrsJ0Q6qDusCVAaHy03j_c-LYezvliMbLzwVm850GF9H6bYs9wowdgQcBay-WMi7bMc4TA9qi002RROpMOlvXd7ghXkXY9ebtiG26zfRsP2REh5uNhaHguHHlyEszCqUf5TGH_grc4ebBcoopx_GP8MDMxCgW4XKV2lOlegc_bUImwRg2IVysa27sYt5WpTICmzVaroAwShMp5X-wAun4SF1GK8m880q6MDcLOdTF9M7hpsd7RebAlwIyAMzjiv9g3L8EBCp2LMm269OoNL_rWvx5-_eOs5MV70TfLLAg-nrzK-ZdalWrWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای دریافت ریزالورهای MasterDNS / StormDNS در WhiteDNS
ربات WhiteDNS حالا امکان جدیدی برای دریافت ریزالورهای MasterDNS / StormDNS دارد.
برای دریافت لیست ریزالورها مراحل زیر را انجام دهید:
1️⃣
وارد ربات زیر شوید:
@dns_resolvers_bot
2️⃣
دستور زیر را برای ربات ارسال کنید:
/dns_master
3️⃣
بعد از نمایش لیست ریزالورها، برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید.
4️⃣
لیست کپی‌شده را داخل اپلیکیشن WhiteDNS وارد کنید و از آن برای اتصال استفاده کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/575" target="_blank">📅 10:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
سرور اهدایی از چنل
@Masir_Sefid
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigxKSIsInNlcnZlciI6eyJkb21haW4iOiJzLm80cy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigyKSIsInNlcnZlciI6eyJkb21haW4iOiJzMi5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigzKSIsInNlcnZlciI6eyJkb21haW4iOiJzMy5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig0KSIsInNlcnZlciI6eyJkb21haW4iOiJzNC5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig1KSIsInNlcnZlciI6eyJkb21haW4iOiJzNS5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
@WhiteDNS</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/574" target="_blank">📅 09:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">White DNS
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/whitedns/573" target="_blank">📅 09:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9ad3f5766c.mp4?token=HWfAq7DEtuXPosJnJtQlzIR608B5EIUgT9P7B70ztt7GLbW9z03DU5d1tsz08pYqFQYsEl-3XYVC10twyb0oysglQVRnmReaSrDIHj8YWAaUfg4EZzbRfg5FiR17nVNi-wAB6PMDGmLnajpZXvnW0Nvhy630I_TXW3Wx42MVpuofQ63-IPI7nZZuunm5hAX-b-HSTf3YZq359KBhaFQRe1ncKoTdqCHI1DJ_oOODMOrJedsxZ4wUxKeLeecMItwJWDGFgquWgzEpjum5XpqPX2tEjzjQ3Tn55D1fRFFhzwv9npQeudqA41Ry9z_r9Ik_F2E0yjDYbJyyeFUtVpswyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9ad3f5766c.mp4?token=HWfAq7DEtuXPosJnJtQlzIR608B5EIUgT9P7B70ztt7GLbW9z03DU5d1tsz08pYqFQYsEl-3XYVC10twyb0oysglQVRnmReaSrDIHj8YWAaUfg4EZzbRfg5FiR17nVNi-wAB6PMDGmLnajpZXvnW0Nvhy630I_TXW3Wx42MVpuofQ63-IPI7nZZuunm5hAX-b-HSTf3YZq359KBhaFQRe1ncKoTdqCHI1DJ_oOODMOrJedsxZ4wUxKeLeecMItwJWDGFgquWgzEpjum5XpqPX2tEjzjQ3Tn55D1fRFFhzwv9npQeudqA41Ry9z_r9Ik_F2E0yjDYbJyyeFUtVpswyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموژش نسخه جدید Whitedns
📲
✨
یکی از اعضای کانال آقا محسن زحمت کشیدند
👨‍💻
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
🚀
✅
حالت Full VPN کامل‌تر و پایدارتر شده
🔒
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
🌐
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
🚫
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
⚡️
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
🎯
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
⚠️
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
💾
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
📂
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
🔄
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
↩️
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
📋
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
📄
@whitedns</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/572" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/whitedns/567" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی بهبودهای داخلی VPN در خود WhiteDNS بوده است. هدف این بود که اتصال کامل‌تر، پایدارتر و مستقل‌تر شود تا کاربران برای باز شدن سایت‌ها و اپ‌ها دیگر نیازی به NekoBox، NVPN یا راه‌حل‌های مشابه نداشته باشند.
در این نسخه مسیر DNS و ترافیک داخل خود WhiteDNS بهتر مدیریت می‌شود، بنابراین تجربه اتصال ساده‌تر شده و کاربر می‌تواند مستقیماً از داخل اپ وصل شود.
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
✅
حالت Full VPN کامل‌تر و پایدارتر شده
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
✅
ظاهر صفحه اتصال و دکمه Connect/Stop مرتب‌تر و جمع‌وجورتر شده
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.2.0
از همراهی و حمایت شما ممنونیم
❤️
1⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/whitedns/567" target="_blank">📅 06:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-565">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همگی دوستان
🔴
11 سرور اختصاصی جدید و بهینه برای اپلیکیشن WhiteDNS
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidi53aGl0ZWRucy5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InYud2hpdGVkbnMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiYjA3ZGMzNTczNjBkNmU2ODk2NTA5MTM2ZDcwOTc4OTciLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEyLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEyLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjAwOWM1MTRiMmE2NDNlZDQwY2JkN2NjNjE5Mzg5YjBmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEwLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjFlY2Q1ZmRmZTM1MWE5MzEzY2VhMzlmZTFiOWM1OWRkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjkud2hpdGVkbnMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJ2OS53aGl0ZWRucy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJhMmYzMzQ4YmZhMDIxNzA2Mzk5NzBmMmQ2M2YxMDNkYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjExLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjExLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjRjMTY2OTMyNmNkYmU4OThjYWIwOTY1YWNlMzAxMGMwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEzLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEzLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImUyOTE4ODcwY2U4OGYwNTU0N2ZiZmJhOTlhZWU0ZWM1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE0LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE0LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjliODY3MmEzNTJkMDQwNDg5ZDk2YmU5ZGY5N2VkOTY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE1LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE1LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjlhYTY4ZTdlOWE3YzIyZDkxZDhmNDY2ZDY0YTM1ZGZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE2LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE2LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU5Mjg0NWNhMzhmMTk0NjEzODNkMDU3MzNjMzMyMTRjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE3LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE3LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU3NjU1MDM1NGE3MzA5NTMwYjdmYTI1MTUyZGM2NzJmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE4LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE4LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImQwNTM4YTNkNTQ1YTc4MzBiOGJiMmViMGMzNzQ4ZTk1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
#Servers
@WhiteDNS</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/whitedns/565" target="_blank">📅 14:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-564">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👇
👇
👇
👇
👇
👇
👇
👇
👇
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/whitedns/564" target="_blank">📅 12:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-562">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">امروز یک هفته از انتشار نسخه بتا۱ اپلیکیشن WhiteDNS می‌گذره
🎉
فکر می‌کنم برای شروع، اپلیکیشن مسیر خوبی رو طی کرده و این فقط با همراهی شما ممکن شده.
خواستم از همه دوستانی که در این مدت با دقت تست کردند، مشکل‌ها رو گزارش دادند و فیدبک درست و کاربردی به تیم ما دادند تشکر کنم. همین بازخوردها باعث شده هر روز بتونیم WhiteDNS رو بهتر، پایدارتر و کاربردی‌تر کنیم.
از اینجا به بعد، سرعت آپدیت‌های نسخه اندروید کمی کمتر میشه تا بتونیم تمرکز بیشتری روی توسعه نسخه ویندوز داشته باشیم.
از دوستان عزیزی که خارج از کشور هستند، همچنان درخواست داریم اگر امکانش رو دارند با دونیت سرور به پروژه کمک کنند. این کمک‌ها مستقیماً به بهتر شدن کیفیت سرویس برای همه کاربران کمک می‌کنه.
از دوستانی که داخل ایران هستند هم یک درخواست مهم داریم:
لطفاً فقط مصرف‌کننده ریزالورها نباشید. برای زنده نگه داشتن شبکه، باید مداوم اسکن انجام بدیم و ریزالورهای جدید پیدا کنیم.
WhiteDNS با کمک جامعه کاربری خودش قوی‌تر میشه؛ نه فقط با استفاده، بلکه با مشارکت همه ما.
ممنون از همراهی شما
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/whitedns/562" target="_blank">📅 10:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-561">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-cDCP2sMH4vFdG9hKB02mDBKrKXhxyoXMHKMm6CuVDBz_VGshsPo1RP2l7bImQkCHXDOJLoMlkXaTWTOdFmRKfmQnk0ZyrCXxj-bBcPB1XTnuEcquo1IVVUzPscCnrw9tA9aFz2x_9XK3a-HcbNqecxhcvt9CovtUqwZ3VFZZKgILw3PThn97vRqh0a02FP-Ygi69Gq2TvE6aLVFdMo39zTDU7qp8Dp8oq75N9kh_WBow8NfZqN8oIG74zhJcO95BNt65xGobsq7VvRL8lDnorlF3d9EjrGd9IxfZXXPKTwpNkCIKv0ei7jiNoINMHZMxf6kIvsQ7hGzitwulncXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/whitedns/561" target="_blank">📅 09:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.1.0-arm64-v8a-1778467437126.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/whitedns/556" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
هدف اصلی از انتشار نسخه ۱.۱.۰، رفع مشکل «وصل می‌شود و دیتا مصرف می‌کند، اما چیزی باز نمی‌شود» است.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
در این نسخه، اپلیکیشن بعد از اتصال وضعیت واقعی مسیر ارتباط را بررسی می‌کند و دیگر تلاش برای استفاده از Resolver یا تونل ضعیف و بدون پاسخ را بی‌پایان ادامه نمی‌دهد. اگر مسیر اتصال بعد از چند تلاش قابل استفاده نباشد، ارتباط‌های جدید رد می‌شوند و اتصال معیوب بسته می‌شود تا حجم بسته شما بی‌دلیل مصرف نشود.
همچنین هسته StormDNS در این نسخه تغییرات مهمی داشته و به همین دلیل اتصال بسیار سریع‌تر برقرار می‌شود. VPN/Proxy بعد از پیدا کردن حداقل Resolverهای سالم با MTU امن سریع‌تر فعال می‌شود و اسکن کامل Resolverها و MTU در پس‌زمینه ادامه پیدا می‌کند. علاوه بر این، اتصال‌های ناسالم زودتر تشخیص داده می‌شوند، مدیریت ارتباط‌های جدید پایدارتر شده و کتابخانه‌های native برای همه معماری‌های اندروید دوباره ساخته شده‌اند.
در این نسخه تمرکز اصلی روی پایداری بهتر اتصال، شروع سریع‌تر VPN/Proxy، مدیریت راحت‌تر پروفایل‌ها، اشتراک‌گذاری تنظیمات اتصال و عیب‌یابی امن‌تر بوده:
✅
نسخه اپلیکیشن به 1.1.0 ارتقا پیدا کرده
✅
مشکل گزارش‌شده‌ای که بعضی کاربران وصل می‌شدند و مصرف دیتا دیده می‌شد، اما سایت‌ها و اپ‌ها باز نمی‌شدند، برطرف شده
✅
حالا بعد از اتصال، مسیر ارتباط بررسی می‌شود و اگر تونل، Resolver یا مسیر خروجی پاسخ‌گو نباشد، اتصال‌های جدید به جای گیر کردن و مصرف بی‌فایده دیتا رد می‌شوند
✅
وضعیت سلامت اتصال داخل اپ نمایش داده می‌شود تا مشخص باشد اتصال واقعاً قابل استفاده است یا نیاز به بررسی دارد
✅
سرعت شروع اتصال بهتر شده؛ اپ بعد از پیدا کردن حداقل Resolverهای سالم با MTU امن، VPN/Proxy را سریع‌تر فعال می‌کند
✅
اسکن کامل Resolverها و MTU حالا در پس‌زمینه ادامه پیدا می‌کند و Resolverهای سالم بعداً به اتصال اضافه می‌شوند
✅
امکان روشن و خاموش کردن WhiteDNS از Quick Settings اندروید اضافه شده
✅
دکمه Disconnect به نوتیفیکیشن VPN و Proxy اضافه شده
✅
امکان Import پروفایل از لینک‌های stormdns:// اضافه شده
✅
هنگام Export پروفایل، QR Code نمایش داده می‌شود تا اشتراک‌گذاری راحت‌تر باشد
✅
ورود Resolverها ساده‌تر شده و حالا می‌توانید چند Resolver را با کاما، سمی‌کالن یا خط جدا وارد کنید
✅
پورت پیش‌فرض :53 به صورت خودکار مرتب و ساده‌سازی می‌شود
✅
اگر Resolver واردشده اشتباه باشد، اپ قبل از اتصال خطا را نشان می‌دهد
✅
تنظیمات پیش‌فرض MTU و پایداری اتصال بهینه‌تر شده‌اند
✅
مدیریت پروفایل‌ها هنگام اتصال بهتر شده و فقط در زمان Connecting محدود می‌شود
✅
بخش Split Tunnel و تنظیمات پیشرفته مرتب‌تر و جمع‌وجورتر شده‌اند
✅
بخش Logs به جای خروجی فایل، Diagnostics آماده و امن تولید می‌کند که اطلاعات حساس داخل آن مخفی می‌شود
✅
هسته StormDNS برای همه معماری‌های اندروید دوباره ساخته شده و پایداری اتصال بهتر شده است
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.1.0
از همراهی و حمایت شما ممنونیم
❤️
1️⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/556" target="_blank">📅 06:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-553">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKvCsR6GqAfvBY-bXZih3_u8elY0XVkXxYwS5iAMZvCvH6VPLbQIl2Ctvfntbi6jvMG5AW0fEQYGQjerpVxEWt7mYXmxFoMkTsCdjc_IL8f1WotHn-tMZIzuOTrn5flakMJBuD9oExLRVLKkL1gpKUuzHrmVfOo4bqd2-r54drOxNgd_oJv_Nawo41d4PHZn2VaRQ3nuGwjfcm2bOhZuX0Yp6F6kavRGlUIKXMChDI4ZGKVQDM-VP85eoNKMDmXtOpY1fjii-2OCJlnYXeF8xMLG6uluro1oJSJrE5Swt8O-VuEOzAl8juM46ErUtsG3kIfv4r8ZOEokLCOV7qQ7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام سرور هایی که داخل اپ بودن داخل تاپیک سرور این گروه هستند. لطفا عضو بشید و گفت و گو ها اصلی رو اونجا ادامه بدید.
1⃣
t.me/whitedns_group</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/whitedns/553" target="_blank">📅 15:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-552">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Es5BjrhiFxD4AUBBNgeofKpWWTPQZidroCubht5ols5v5rKVi1HB8SIYspQPgVfYhoNaL1DkF1aq-onPKvatD3vN6ALdaBxBJbzcwHRM9M0cxA6MX-CxqM1lyo6-HDcO8QxUXlZwuStxq20jCjP9zAfeUZ49IVjSdBw5zsOrEwBID88C6iDtHzC1fS7NoRrkvGiLR-A1F9d7WTwrUbIR5dlA_faR8uf5li-twsohAqlxTUli5Lz8pQ3Vhckrnyv8Q9LPoS94Of0bG3QRLuTKPAyaCAU11neqiYEyTbeNpJdkoklLv3ZozBiSd1THN6TjSzDolWGr_a9MShE2mfnkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/whitedns/552" target="_blank">📅 15:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-551">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/551" target="_blank">📅 14:01 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-x86_64-1778404214016.apk</div>
  <div class="tg-doc-extra">5.3 MB</div>
</div>
<a href="https://t.me/whitedns/544" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
انتشار رسمی WhiteDNS به صورت متن‌باز
دوستان عزیز،
پروژه WhiteDNS رسماً به صورت Open Source روی GitHub منتشر شد.
این نسخه، اولین ریلیز رسمی
1.0.0
بعد از ۷ نسخه بتا است و از این به بعد مسیر توسعه پروژه شفاف‌تر، عمومی‌تر و با مشارکت جامعه ادامه پیدا می‌کند.
در این نسخه، پروفایل‌های پیش‌فرض WhiteDNS از داخل اپ حذف شده‌اند
تا برنامه به شکل مستقل‌تر و عمومی‌تر قابل استفاده باشد.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
قبل از آپدیت به این ورژن ، تمام پروفایل های خودتون رو Export بگیرید. ورژن جدید دیگه سرور های WhiteDNS را در اپ ندارد.
ورژن جدید اپ Sign شده هستش و از لحاظ امنیتی بهبود یافته.
برای نصب، ورژن قبلی اپ باید به صورت کلی از روی دستگاه شما حذف شود.
از این ورژن به بعد، نیازی برای پاک کردن اپ در هر آپدیت نیست.
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
از این مرحله به بعد، توسعه‌دهندگان و کاربران می‌توانند پروژه را بررسی کنند، مشکل‌ها را گزارش دهند و در بهبود آن مشارکت داشته باشند.
🔗
GitHub:
https://github.com/iampedii/WhiteDNS
از همراهی و حمایت شما ممنونیم
❤️</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/whitedns/544" target="_blank">📅 12:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های مخصوص وایت دی ان اس ورژن جدید( 7 WhiteDNS)
👾
کلاینت :
WhiteDNS
1️⃣
|
WhiteDNS
2️⃣
⬅️
نحوه ی اضافه ی کردن پروفایل ها
⭕️
پست تنظیمات کلاینت
⭕️
پست تنظیمات بهینه تر
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoicy5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMikiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczIubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMykiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczMubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oNCkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczQubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oNSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczUubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
✉️
Channel |
@link_dakheli_app
| کانال
✉️</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/whitedns/538" target="_blank">📅 09:40 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/whitedns/537" target="_blank">📅 09:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-536">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سلام خدمت همگی دوستان
🔴
11 سرور اختصاصی جدید و بهینه برای اپلیکیشن WhiteDNS
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidi53aGl0ZWRucy5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InYud2hpdGVkbnMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiYjA3ZGMzNTczNjBkNmU2ODk2NTA5MTM2ZDcwOTc4OTciLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEyLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEyLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjAwOWM1MTRiMmE2NDNlZDQwY2JkN2NjNjE5Mzg5YjBmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEwLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjFlY2Q1ZmRmZTM1MWE5MzEzY2VhMzlmZTFiOWM1OWRkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjkud2hpdGVkbnMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJ2OS53aGl0ZWRucy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJhMmYzMzQ4YmZhMDIxNzA2Mzk5NzBmMmQ2M2YxMDNkYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjExLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjExLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjRjMTY2OTMyNmNkYmU4OThjYWIwOTY1YWNlMzAxMGMwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEzLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEzLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImUyOTE4ODcwY2U4OGYwNTU0N2ZiZmJhOTlhZWU0ZWM1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE0LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE0LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjliODY3MmEzNTJkMDQwNDg5ZDk2YmU5ZGY5N2VkOTY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE1LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE1LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjlhYTY4ZTdlOWE3YzIyZDkxZDhmNDY2ZDY0YTM1ZGZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE2LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE2LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU5Mjg0NWNhMzhmMTk0NjEzODNkMDU3MzNjMzMyMTRjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE3LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE3LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU3NjU1MDM1NGE3MzA5NTMwYjdmYTI1MTUyZGM2NzJmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE4LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE4LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImQwNTM4YTNkNTQ1YTc4MzBiOGJiMmViMGMzNzQ4ZTk1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
#Servers
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/whitedns/536" target="_blank">📅 07:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-535">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbVcQ3FSGKwJZOVbDARj5nDH9HLgEZdBFcmvKQxebiXFG0Ij1PHTDeJgHCkkKnlQTEPsevKsy5Y5TwSYYAo26nOD4EqlOSerCqDTo8zDJG8-jtjBkRXCV1cyCsNAzeW-pdKvy56fgNx3B1_6ZzCtR--LJ6TF6EKqUgUqZGqYOLkOvazLrgLaTUbxxu7FBLsRNzq6Xa3bZm-qc0mySGw0c-JiwOhZ5hc1N3eCg2XjWawoj9LnIZNKpn2t_TfIgPXCi0j6gz9fenSAEx9iCnZ_7nfcg67id5tw11IFSfSJT4zGVOTM1e0z9wUEiVRd9I26BBw0a9gTekdV5b1tqeGuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه بعد از اسکن، DNS های سالم رو برای بعدا ذخیره کنیم؟
بعد از اتصال، زیر دکمه
Connect
یک عدد نمایش داده می‌شود.
اگر روی عدد بخش
Valid
بزنید، فقط لیست ریزالورهایی که با موفقیت تست شده‌اند نمایش داده می‌شود.
می‌توانید همان لیست را کپی کنید و با آن یک پروفایل ریزالور جدید بسازید. بعد از آن، هنگام اتصال، پروفایل جدید را انتخاب کنید.
با این کار هم اتصال سریع‌تر برقرار می‌شود و هم اپلیکیشن سبک‌تر اجرا می‌شود
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/535" target="_blank">📅 05:18 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-533">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">White DNS
pinned «
سلام خدمت همه دوستان عزیز
🌿
برای اینکه مطالب، آموزش‌ها، فایل‌ها و بحث‌های مرتبط با WhiteDNS بهتر دسته‌بندی بشن و دسترسی بهشون راحت‌تر باشه، یک گروه جدید برای کانال ساختیم.   متأسفانه تلگرام این امکان رو به ما نمی‌ده که گروه فعلی رو به گروه دارای Topic تبدیل…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/533" target="_blank">📅 20:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-532">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
🌿
برای اینکه مطالب، آموزش‌ها، فایل‌ها و بحث‌های مرتبط با WhiteDNS بهتر دسته‌بندی بشن و دسترسی بهشون راحت‌تر باشه،
یک گروه جدید برای کانال ساختیم
.
متأسفانه تلگرام این امکان رو به ما نمی‌ده که گروه فعلی رو به گروه دارای Topic تبدیل کنیم. برای همین، جهت حفظ بهتر مطالب و جلوگیری از گم شدن آموزش‌ها و اطلاعات مهم، لطفاً عضو گروه جدید ما بشید.
از این به بعد گفت و گو های اصلی تیم، آموزش‌ها، مطالب فنی و اطلاع‌رسانی‌های مهم داخل گروه جدید انجام می‌شه.
گروه فعلی فقط برای کامنت‌های مربوط به پست‌های کانال استفاده خواهد شد و فعالیت اصلی تیم در اون محدود می‌شه.
ممنون از همراهی همیشگی‌تون
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/whitedns/532" target="_blank">📅 20:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-531">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بازی ساده اس !ً مدت ها ذهن شما با قیمت vpn های هر گیگ 1 میلیون و یا 500 هزار و یا 200 هزار تومن عادت کرده بود
حالا وقتی vpn بشه هر گیگ 80 تا 100 کلی حس پیروزی و خوشحالی داری و مدتی لذت میبری ازش .
بعدش پیش خودت میگی خب میرم سیمکارت پرو میگیرم بشه هر گیگ 40 هزار تومن و اون لحظه اس که دیگه حسابی خوشحال خواهی بود چون با نصف قیمت VPN دیگه اینترنت داری  !
حالا اینکه روزی سه چهار گیگ میتونی در روز مصرف کنی و 11 برابر گرون تر از 3 ماه پیشه که اینترنت وصل بود دیگه اصلا به ذهنت نمیرسه چون مدت ها درگیر بازی قیمت توسط حکومت بودی
اینجوری چرخه بردگی تا ابد ادامه پیدا می‌کنه
حالا فهمیدید چرا ما با هر رانت دولتی مخالفیم ؟
@whitedns</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/whitedns/531" target="_blank">📅 19:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-530">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سوالات پرتکرار مربوط به برنامه‌ی WhiteDNS
این تلگراف به مرور تکمیل تر شده و سوال های بیشتری نیز داخل آن قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/whitedns/530" target="_blank">📅 16:17 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-529">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/529" target="_blank">📅 16:15 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-527">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTdB9bym3MtWwrJBdfPHBPFzs2zzYRd9zqOWOVRzy-IZRzFDmmpdE-K2ZOAuSmEOQSW_7NGEQC1CU0qg8Whu3YiWdg7bnQrLgQ9cbw7aaHtuklvv54R8CsMIFnzsWHy8uHeCcsW1I290J4x-etj-L54tzMOHUHoYAkXys7gLPiUZX-lzDmmGPrOr2RGTz5GARQmIXkDkm48mL_dcvEe2akukaMXXAVS_46AXNSzFiNPJvkmlanPDnTXaNC8wCpMBLLTWYGF3vBvbgAP3OIvyc_6C5DXX6LvSAydiJeAm23NFRmP4WbsL_mqIfc5C0mUGUiEreN1oZbYzAEVkFa0g6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/whitedns/527" target="_blank">📅 13:36 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-525">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEKIlxIXESfMzoMhOLm5Nq3KsbZhrMgLfgPYgdXzIAZ38pwL7tkvA9ipL6ZscDATFqQUIwt8Ct-6MpXQlwVlw7SiG_qzDPkvn31StEkMV_Ib-lSlKI0uErJfwlbFdVsU4esuWW3QXU_15VJw2c7CbQrqOz0i7lCJkpUZtptAd8YSMXF_mQCQSxVjUUq88VQcjhQ2t38e43LcPJMR1YoNwkOcoAtUDTBvAeFY30ZK-3GuBS8-E8c4abYBFZHdeofgQvTi98kspYcT_KJKSl8RICGOZKUuV9jhIoQxmDgT1qWwNmlJAUr5wLQUxDkb5VapS45eYrYeuTktTQOZIRRImw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربات WhiteDNS حالا امکان جدید دارد برای دریافت ریزالور های MasterDNS / StormDNS
۱) وارد بات زیر شوید
@dns_resolvers_bot
۲) متن زیر را برای ربات ارسال کنید
/dns_master
۳) برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/525" target="_blank">📅 10:43 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-523">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/523" target="_blank">📅 10:15 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-521">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSFebt3P3A06AQ9w_-mrrIcyBOM2JH1fvas_ggWYVb_dtjfjmbKu32bW61REohisSFGIEc0pWYXRo4jS-Nn_IdP8WgrxRSl7I2oOH4BJ1Xfg6X_YQXnK4QTHpOY5uZMHKaaIz0neWPpVFHK7migF09zv7BdYmCOz9IpLFD1WM01BgLN6FNZthUuLFrkb9xBeaV75K3rwcOCrrwKYdhoYNPBQ6s_u5zNb4JQKyGW0VQ5Fu3i89YMr_F1TFochHN__fhc04NWVtm8x_0ChKHib7LG75SI5qlMaXkiToHGrXdOij5vnr1_ASCYC58Xa85tEWz-g-G4enkMI_x_klccaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ سرور اهدایی از چنل همکار
@link_dakheli_app
برای ایمپورت ابتدا ورژن اپ رو به بتا۷ آپدیت کنید، سپس وارد بخش پروفایل بشید و بعد دکمه ایپمورت رو بزنید.
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidGUubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InRlLmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZXUubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6ImV1LmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoic3IubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InNyLmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoicy5vNHMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJzLm80cy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbUNoYW5uZWxAbGlua19kYWtoZWxpX2FwcCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiczIubzVzLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczIubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
👾
لینک دانلود نسخه بتا ۷ از سرور داخلی
WhiteDNS
1⃣
|
WhiteDNS
2⃣
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/whitedns/521" target="_blank">📅 10:03 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-516">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta7-x86.apk</div>
  <div class="tg-doc-extra">22.8 MB</div>
</div>
<a href="https://t.me/whitedns/516" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
در این نسخه تمرکز اصلی روی مدیریت راحت‌تر پروفایل‌ها، اشتراک‌گذاری تنظیمات اتصال و پایداری بهتر بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta7 ارتقا پیدا کرده
✅
امکان Import و Export پروفایل‌های اتصال StormDNS اضافه شده
✅
حالا می‌توانید تنظیمات سرور شخصی را به شکل لینک stormdns:// خروجی بگیرید و برای دیگران بفرستید
✅
امکان وارد کردن چند لینک پروفایل به صورت هم‌زمان اضافه شده
✅
دکمه‌های Copy و Share برای لینک پروفایل اضافه شده‌اند
✅
امکان Export All اضافه شده تا بتوانید همه اتصال‌های سفارشی را یکجا خروجی بگیرید
✅
پروفایل‌های اتصال حالا با کشیدن و رها کردن قابل مرتب‌سازی هستند
✅
Resolver Profileها هم حالا قابل مرتب‌سازی شده‌اند
✅
ظاهر بخش Profiles مرتب‌تر شده و دکمه‌های ویرایش، حذف و خروجی گرفتن واضح‌تر شده‌اند
✅
وضعیت پروفایل انتخاب‌شده و پروفایل فعال واضح‌تر نمایش داده می‌شود
✅
قابلیت Traffic Warmup اضافه شده تا بعد از اتصال، مسیر ارتباط سریع‌تر آماده شود
✅
قابلیت Keepalive اضافه شده تا با ارسال ترافیک سبک دوره‌ای، اتصال پایدارتر بماند
✅
Traffic Warmup و Keepalive هم در Proxy Mode و هم در Full VPN فعال هستند
✅
از تنظیمات پیشرفته می‌توانید Traffic Warmup را روشن یا خاموش کنید و مقدار آن را تغییر دهید
✅
نمایش لاگ‌ها و وضعیت اتصال سبک‌تر و مرتب‌تر شده تا صفحه هنگام دریافت پیام‌های زیاد روان‌تر بماند
✅
دکمه Donate اضافه شده و امکان کپی کردن آدرس‌های حمایت مالی داخل اپ وجود دارد
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN برای تست وجود دارد و بهتر شده، اما چون کل ترافیک دستگاه را از تونل عبور می‌دهد ممکن است روی بعضی دستگاه‌ها یا شبکه‌ها سرعت و پایداری متفاوتی داشته باشد.
اگر سرور StormDNS شخصی دارید، حالا می‌توانید پروفایل اتصال خود را راحت‌تر با لینک stormdns:// ذخیره یا برای دیگران ارسال کنید. همچنین استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند فشار روی سرورهای عمومی WhiteDNS کمتر شود.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/whitedns/516" target="_blank">📅 09:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-515">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Y_kBqwScvsaBgktiAlbo0I1L5kePkYMCgraEmRmW3fH35m4bOZ4VZVFsSgoHT3g-HQunEXTVfqVxHmXa2xTunAKzbQDHx4RluSeBcTrVd3Fu3mFFk4b5csxK5DiAN6mkaWh2VsokU2B01_y7njYaWsI5saK6Vkp9ZHjtzWZfscbjjaPrAU1k2gQ0CrkOc6EDqxs_uHgdY4AQf9NCpTvmiExs-BD3lOjRqCJromGqzHnukhJxNxezYepcSFHIkRg51-gQ-n43rMB6tsfJn98-VdMGPf1F_6bIW1USzc_EcD27Mh72LFm0Tp4VLtJz2KNWMI7bBwo1r8SR3g96PIrArA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/515" target="_blank">📅 06:59 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-513">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❤️
سرور اختصاصی whitedns برای Slipnet
❤️
آموزش کامل :
https://t.me/whitedns/294
دانلود کلاینت :
https://github.com/anonvector/SlipNet/releases/tag/v2.5.3
User:
whitedns
Password:
whitedns
[dnstt-socks] Public Key: 1b23cc151ab07274a4f2623a94b7172d61803956fa068f5074e38ec5eb800516
[dnstt-socks]
slipnet://MjJ8ZG5zdHR8ZG5zdHQtc29ja3N8dC5pcmFubW90b3IuYml6fDguOC44Ljg6NTM6MHwwfDUwMDB8YmJyfDEwODB8MTI3LjAuMC4xfDB8MWIyM2NjMTUxYWIwNzI3NGE0ZjI2MjNhOTRiNzE3MmQ2MTgwMzk1NmZhMDY4ZjUwNzRlMzhlYzVlYjgwMDUxNnx3aGl0ZWRuc3x3aGl0ZWRuc3wwfHx8MjJ8MHwxODUuMjMwLjIxOS4xNjd8MHx8dWRwfHBhc3N3b3JkfHx8fDB8NDQzfHx8MHx8MHwwfHwwfHwwfDB8MTA4MHwwfHR4dHwxMDF8MHwwfDB8MHwwfDB8MHx8fDgwODB8fDB8L3wxfHw=
[noizdns-socks]
slipnet://MjJ8c2F5ZWRuc3xub2l6ZG5zLXNvY2tzfHQuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfDFiMjNjYzE1MWFiMDcyNzRhNGYyNjIzYTk0YjcxNzJkNjE4MDM5NTZmYTA2OGY1MDc0ZTM4ZWM1ZWI4MDA1MTZ8d2hpdGVkbnN8d2hpdGVkbnN8MHx8fDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[dnstt-ssh] Public Key: 1b23cc151ab07274a4f2623a94b7172d61803956fa068f5074e38ec5eb800516
[dnstt-ssh]
slipnet://MjJ8ZG5zdHRfc3NofGRuc3R0LXNzaHx0cy5pcmFubW90b3IuYml6fDguOC44Ljg6NTM6MHwwfDUwMDB8YmJyfDEwODB8MTI3LjAuMC4xfDB8MWIyM2NjMTUxYWIwNzI3NGE0ZjI2MjNhOTRiNzE3MmQ2MTgwMzk1NmZhMDY4ZjUwNzRlMzhlYzVlYjgwMDUxNnx3aGl0ZWRuc3x3aGl0ZWRuc3wxfHdoaXRlZG5zfHdoaXRlZG5zfDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[noizdns-ssh]
slipnet://MjJ8c2F5ZWRuc19zc2h8bm9pemRucy1zc2h8dHMuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfDFiMjNjYzE1MWFiMDcyNzRhNGYyNjIzYTk0YjcxNzJkNjE4MDM5NTZmYTA2OGY1MDc0ZTM4ZWM1ZWI4MDA1MTZ8d2hpdGVkbnN8d2hpdGVkbnN8MXx3aGl0ZWRuc3x3aGl0ZWRuc3wyMnwwfDE4NS4yMzAuMjE5LjE2N3wwfHx1ZHB8cGFzc3dvcmR8fHx8MHw0NDN8fHwwfHwwfDB8fDB8fDB8MHwxMDgwfDB8dHh0fDEwMXwwfDB8MHwwfDB8MHwwfHx8ODA4MHx8MHwvfDF8fA==
[slipstream-socks]
slipnet://MjJ8c3N8c2xpcHN0cmVhbS1zb2Nrc3xzLmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHx8d2hpdGVkbnN8d2hpdGVkbnN8MHx8fDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[slipstream-ssh]
slipnet://MjJ8c2xpcHN0cmVhbV9zc2h8c2xpcHN0cmVhbS1zc2h8c3MuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfHx3aGl0ZWRuc3x3aGl0ZWRuc3wxfHdoaXRlZG5zfHdoaXRlZG5zfDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[vaydns-socks] Public Key: ecef7073cd119405e62f1347daa949794193ccd618f0f879fa7c10da37a7f53e
[vaydns-socks]
slipnet://MjJ8dmF5ZG5zfHZheWRucy1zb2Nrc3x2LmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHxlY2VmNzA3M2NkMTE5NDA1ZTYyZjEzNDdkYWE5NDk3OTQxOTNjY2Q2MThmMGY4NzlmYTdjMTBkYTM3YTdmNTNlfHdoaXRlZG5zfHdoaXRlZG5zfDB8fHwyMnwwfDE4NS4yMzAuMjE5LjE2N3wwfHx1ZHB8cGFzc3dvcmR8fHx8MHw0NDN8fHwwfHwwfDB8fDB8fDB8MHwxMDgwfDB8dHh0fDEwMXwwfDB8MHwwfDB8MnwwfHx8ODA4MHx8MHwvfDF8fA==
[vaydns-ssh] Public Key: ecef7073cd119405e62f1347daa949794193ccd618f0f879fa7c10da37a7f53e
[vaydns-ssh]
slipnet://MjJ8dmF5ZG5zX3NzaHx2YXlkbnMtc3NofHZzLmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHxlY2VmNzA3M2NkMTE5NDA1ZTYyZjEzNDdkYWE5NDk3OTQxOTNjY2Q2MThmMGY4NzlmYTdjMTBkYTM3YTdmNTNlfHdoaXRlZG5zfHdoaXRlZG5zfDF8d2hpdGVkbnN8d2hpdGVkbnN8MjJ8MHwxODUuMjMwLjIxOS4xNjd8MHx8dWRwfHBhc3N3b3JkfHx8fDB8NDQzfHx8MHx8MHwwfHwwfHwwfDB8MTA4MHwwfHR4dHwxMDF8MHwwfDB8MHwwfDJ8MHx8fDgwODB8fDB8L3wxfHw=
@whitedns</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/whitedns/513" target="_blank">📅 05:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-510">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎁
۷ سرور اهدایی
با تشکر از رسول عزیز، یکی از اعضای خوب WhiteDNS
❤️
#Servers
🌐
Domain:
g1.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g2.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g3.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g4.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g5.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g6.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g7.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
@WhiteDNS</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/510" target="_blank">📅 05:14 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-507">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانفیگ تمام سرور های WhiteDNS و اهدایی آپدیت شد
🚀</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/whitedns/507" target="_blank">📅 03:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-506">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دانلود WhiteDNS Beta6 از سرور های داخلی
📶
WhiteDNS Beta 6
1⃣
📶
WhiteDNS Beta 6
2⃣
منبع
@link_dakheli_app</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/whitedns/506" target="_blank">📅 18:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-505">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">White DNS
pinned «
سلام خدمت همه دوستان  ما تا امروز حدود ۳۰ سرور مختلف داخل کانال منتشر کردیم. بعضی از این سرورها داخل اپلیکیشن اضافه شده‌اند و بعضی دیگر از پست‌های فوروارد شده یا منابع مختلف بوده‌اند.  برای اینکه همه چیز یکجا و مرتب باشد، لیست کامل سرورها را اینجا قرار می‌دهیم.…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/505" target="_blank">📅 18:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-504">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سلام خدمت همه دوستان
ما تا امروز حدود ۳۰ سرور مختلف داخل کانال منتشر کردیم. بعضی از این سرورها داخل اپلیکیشن اضافه شده‌اند و بعضی دیگر از پست‌های فوروارد شده یا منابع مختلف بوده‌اند.
برای اینکه همه چیز یکجا و مرتب باشد، لیست کامل سرورها را اینجا قرار می‌دهیم. ممکن است کیفیت و پایداری بعضی سرورها در زمان‌های مختلف تغییر کند، پس اگر یک سرور کار نکرد، سرورهای دیگر را هم تست کنید.
ادامه داشتن این پروژه و وصل ماندن کاربران، مستقیم به حمایت شما بستگی دارد. اگر دانش فنی دارید و می‌توانید ماهانه حدود ۵۰ دلار هزینه کنید، با دونیت کردن ۵ سرور می‌توانید به وصل شدن تعداد زیادی از کاربران کمک کنید.
domain:
t1.prs612.us
Encryption Key:
3e80a0eb3e1fba2bf17e0e0eb5783dc5
domain:
t2.prs612.us
Encryption Key:
afc1bd5e98cd98cde7515adb7295122b
domain:
t3.prs612.us
Encryption Key:
8786a860148e2d4d55403ae3c80ba854
domain:
t4.prs612.us
Encryption Key:
943664f15fd1763e242ce12ba993d9c9
domain:
t5.prs612.us
Encryption Key:
6a9ab24a8bd3937378efbfb3c23e1358
domain:
t6.prs612.us
Encryption Key:
71201fedadfbc0b62189c08961bce651
domain:
t7.prs612.us
Encryption Key:
c4ff91174a79e9e03a4d6727878ada17
domain:
t8.prs612.us
Encryption Key:
ae5db6f03e485214e1fcc9d26a4c0a2f
domain:
t9.prs612.us
Encryption Key:
a01c03a340a3e684a2815961e086eb27
domain:
t10.prs612.us
Encryption Key:
f3a3c5d02bb7ce04f6a4f144fc35e9cb
domain:
t11.prs612.us
Encryption Key:
e7f2db07e778563d31ed1fc80d5fe612
domain:
te.link-dakheli-app.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
s.o4s.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
s2.o5s.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
v.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v3.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v4.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v5.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v6.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v.whitedns1.shop
Encryption Key:
c8328f9d541860df1637b9b3ed7b990e
domain:
v.whitedns2.shop
Encryption Key:
7ecd7b6271c47e348f6ab177517ee8fa
domain:
v.whitedns3.shop
Encryption Key:
9d7aedcaf1f94e784a24fdfc1348a337
domain:
v.whitedns4.shop
Encryption Key:
0ce14ab71acebbd46b8129e25593155a
domain:
v.whitedns5.shop
Encryption Key:
2dffd162cb02b278c1ab57ee17fe07ae
domain:
v.whitedns6.shop
Encryption Key:
e32afdaa30ca36ead696cd90d84ced15
domain:
v.whitedns7.shop
Encryption Key:
6394eec942238533798ec7524eb7ea66
domain:
v.whitedns8.shop
Encryption Key:
1c167e9850936655c480e4938b2c5c35
domain:
ob.networks.icu
Encryption Key:
3947d5ac68015a09a53a0b361bd82999
domain:
ts.networks.icu
Encryption Key:
e0e71e667e5dcfe3b18e3bce659773d2
domain:
zw.networks.icu
Encryption Key:
0798c0e8aa05080125e6c65282fd792b
domain:
v.0x0.guru
Encryption Key:
33815e1bcb88873f2199c735828ea745
domain:
v.iranmn.best
Encryption Key:
aaed913b8367fce3e20910472d9e3e2d
domain:
v.kmjhfilterchi.shop
Encryption Key:
4f3d0262ba2bd7cc20b596bdbc77f761
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/whitedns/504" target="_blank">📅 18:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-503">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1n17Sb5NeDZoR2NfitjCOPn7vgD4-BNHfLdkc524GErin57qszIj2nDsJPQ8RBea_vylV6Hd9m7KUx-E2So17qyaAvMzS6_7xNLD4PqxHs-sdkQdyqxQhVTuBoUiw10q7NO_UGwcFB4lU2gwjmzJHvtluUFvaWjzQKPm7IgAxBbUdBgJSnYDXLzGVLaCRRbmoj6lmDT5U9upESuzs1y0Fm6P2FLY45w9fK9LT0zAeumbUFezLfgIckJVu0toU0X5ILDbPOl9G2cmAxKHTEenZBIf6qOZZ_IURyE94eOdHdNkwqepVYdbYcyopzF1apAd69K9DJa4znAVLaNWAfDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد
Advanced Settings
شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup: 1
🔸
Download Dup: 4
🔸
Upload Compress: OFF
🔸
Download Compress: LZ4
📊
این کانفیگ به‌صورت حدسی انتخاب نشده.
ما لاگ‌های سرور در ۷۲ ساعت گذشته را پردازش و بررسی کردیم و بر اساس پروفایل‌های موفق‌تر، MTUهای پایدارتر و مسیرهایی که سرعت بهتری داده‌اند، این تنظیمات را پیشنهاد دادیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/503" target="_blank">📅 16:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-502">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CHfp-X2xGQ0xUp-CdvMMVmU6tWWM01taN1C0yCT0E9z79OEc4zLe3sqJtxoWV0SstbUboUbNUbV7_CTkG_jYTo2tHN88PztPgZh-CCWdMG1-VtMZS4ugZGsNYrd3SgTm5eGQjOhnfZQMqUmpmyopi1EM1O8fH2GHzPB3Yv3PG4NPikoMMPIQyKQH7kRDxzsMrMZmnvhYR8NbSMTiQLOKvo4JYUs_HXNt9szC4MCr117NURwUSDPFiTc53KLQWtgjYNrldr0gsA4-P0q_G_SuYyk4BEX4rrfCQ_-lhdAJwc5gGDA4e_BTzO9jJn9NBDtvx4qgnF7_i37wOaxd8J8QUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به هر دلیلی میخواهید از حالت پراکسی در whitedns استفاده کنید بهترین کار استفاده از اپ نکوباکس هست   https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/tag/1.4.2  #Nekobox #Proxy #WhiteDNS  @whitedns</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/whitedns/502" target="_blank">📅 12:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-501">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ArEeWHpzG1VGpvthqxcsmRmKMn8sFD9JNr4plWMv28U-3s4fJIxm8ESJUto4OYaENdpgfQSovuVikEvLL2sMl4KANCOrjUCdP9-dmANpf22NrgWBgxZrPDF3kF5iAZv6c24lxqma0gHIEPEHZw425OE6i4kRhFuUgCmnz-a5Q50dlknpoJLWVnNBuZdFf5NP67NwjXWAEAWgVBOt9YjS-ySEpwSUrVEmUNMvTjYoZd9d3uWKmZjquE9kyjFdjicT4FIlK-lWQAfCCZO6T-iACTBLGKFiMKXCUlPV0w75En-edbXjUawo_UlnrDb0A4JPAWyEptZuW60O9wF3_j6sug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/501" target="_blank">📅 11:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromConfig plus</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiGpdDhepLqZaul2kBdKifspu6gde7Ec9I7iQQXKgGQ7RJhCV2Kaw3t37lincj3fs_y9DX_ng5TC8Zi09y3lJjBnp-fhlDImdh_bdE8aW9rxWsFpsWu-f0r5pwjJXWyOjEU8qJENPOSbvEhA3_Yxv1h_e-sJoPwSCiAwQNO8eu_7HQ4rh5xwBWDRF92UMa-Oir0PBc24FGp-8pGDo2lfDW-X69xVHv4d49IZxc9NhdYxhTgQ0V01I6lwFubwR87oBWp96qRdYPim7CdTq2Z4V1B7S3Jq2tgjUeej2tCzCzke0KrEUgWGVK1IePHELL22Wo733QfxAp_2kYq8KIq_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xv5ntiazWiHoc1JP5dxgaV1lYnMn2bRCavLyy-Wr0dAUCA-YLIDbzmhOluADF1mWQGBg537G1XUfrKgmhG3aOcgV9xhb4fAZHi3iwaIFrl4Lyi3thNVUSsATzjfO7kwydifFYydayF5YZx_VsV0VscKTqQzsu68_g6zy5zh9J3Hudq4yGSlfM5t5Fq6eRwB_fmsch9vfKdzdi0yn_VPDPjAb4npSj09RPBQDhnint5LpoEenylJvllV0R_BL0a1EETmvoO9QBCoHk2rvdYLmcfQChB4tWlB_pQwXU6bC10XWn6cgkxDEo4M3RqBsL5blPtqqGoE2cs103p7a8BEeyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWL-wJxSAIp-HZ2VnK6F8_ZU_3od1KeACvh2ShYtqmeiRSn8IH-5eIyRKzsbOyeodZXyZTLtywCcENBLHwNCL2w0JkASaLa3nAGGooJXH0BBfkh8fVTHn8_3J9YQ6D7tIG38hAXg-QQURVhqqm6WxCkbVKaqZE7qgr8P687dEf5_zJGpGyE_gDKIsqNs8G_9PCS5PQOmyb3CBKHDUKvSAaVd1sE1HnI4RWYf08Q9qPHkW1ZtwlA7wKNeqjWIisLYqDWTOiJxR1KgaLh40Rzn0xCOgDUD8bPxi_bEZzcpRhIxQJzujIwrEgZz7A1gQlqxGWM7BBDIctk-4Yg8ORhk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBDUp-aRXKbypwtHh8EAOb-SlhROEET0Ke3EYklnGJ0tXj5wv6ikTzAfbNsZCYK9gv8Nch6f8MZ7_yxYRcsUsWOg1Aun-OLCnl-ep36Dwogk6hPKNDjsB1YfMsrgERjJwEueGAm1wV54albvVNFGtQj_pihWc4lTwffgXnXmX1fo6ZaA6uyGPsAs1W4zQg-LHZlMeckWIvo_Jpv79PTndbDqlEG-cKMXvJGuRLJ2P6_ppZ4ZShULxaGOyxfE9oULQGjIYYgFMOdSpJicH-ysHIve3iVDNA0FlavJ7jxb_TbZ8pjJKq8j5tnNlQkrRisqxPh0APjv1LIkAlDeYrV35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uytWBCi-mALlwiI_BLAvDTMD2aMo8GCY4nUCFv2A4lVXJENxvJ8hLc5ziPY4_YnX1ZkFW_lZ0VNmEY_M2hdclMvNQTCGKMi_i-rS0IoRWO0AIMyKOFqwspJNeueBCFLn4Ufj484RgxUAmupr_5zvcqPweTSMuq4fm0_TBPqZ3vgD8NCEvl0xsR-Dpvlul3q-0IawUuygH9cq5noFyo63RkYEqakQ1woLCOzdssVcASpKW2omT7ILV-nNj467uvKCrtVj185Qhh3SOw3v1ooUQKDiJSi9y7WCvISg1qFcJHGMATluLvy8zzw1bMh3cfloesdJY8QaKR5CEXsNRupAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_XD7QCI1NBqj4I_ZneOosJKeh_nef526_-l_7SKjgV3T7ewYVchdUgyQUEcYCpykF3nkgIkHqQfhRXkHZjWlUIbZcARZ2T4GWuoGICsM1iIvY1rcMpA7IqCJ_1yGG1Hea3lANJkfr6vukai9JuwsbNjTq0WD2YWfaQB5wNDkojOtWZ37lMdeRUd5cYilYL-gw7P0_2JDke-Q6yE0ln75e2t41AKF40d_qCkcEQcMXVlL8A7pavh8eFSCdbutb_CmIjHn6Fbvy3ne3VV1tSafr9ZuF2nXZoT4ZGgjWlNSjTJ4DR1L7bAnNdhYFSX40VyUwpguWjAbKaiYRId_JOkLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔺
آموزش اتصال به برنامه whiteDNS در اندروید
1.ابتدا اول برنامه رو دانلود کنید از طریق لینک داخلی :
https://guardnet.ir/f/8f0ef50b3049
رمز فایل موقع استخراج:
3666
مطابق تصاویر بالا کانفیگ ها و ریزالوز ها را وارد نرم افزار کرده و تست کنید.
کانفیگ ها :
1- دامنه :
ob.networks.icu
🔐
کلید رمزنگاری :
3947d5ac68015a09a53a0b361bd82999
2- دامنه :
ts.networks.icu
🔐
کلید رمزنگاری :
e0e71e667e5dcfe3b18e3bce659773d2
3- دامنه :
zw.networks.icu
🔐
کلید رمزنگاری :
0798c0e8aa05080125e6c65282fd792b
اتصال برای تلگرام با پروکسی از طریق پورت 10886 و لوکال‌ هاست
127.0.0.1
به پروکسی زیر متصل شده و وارد تلگرام شوید و حدود 3 الی 5 دقیقه منتظر بمانید تا تلگرام آپدیت بخوره
https://t.me/socks?server=127.0.0.1&port=10886
این روش و برنامه برای تلگرام تست شده ولی خیلی خوبه ، برای اینکه سرعت بهتری داشته باشد در تایم شب بهتر عملکرد دارد و سرعت بالاتری دارد. اما در طی روز هم برای تلگرام برنامه جواب میده.
هر گونه سوال بود داخل دایرکت هستم :
t.me/Config0plus?direct
🟢
Join:
https://t.me/Config0plus
جهت حمایت از ما ری اکشن فراموش نشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/495" target="_blank">📅 09:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-494">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سرورهای WhiteDNS تا امروز نزدیک به ۶ ترابایت دیتا جابه‌جا کرده‌اند.
این آمار فقط مربوط به سرورهای اصلی WhiteDNS است و دیتای سرورهای اهدایی داخل این عدد حساب نشده.
حالا بیایید خیلی ساده حساب کنیم:
اگر هر گیگ کانفیگ فیلترشکن را حدود ۲۰۰ هزار تومان در نظر بگیریم:
۶ ترابایت = ۶۱۴۴ گیگابایت
۶۱۴۴ × ۲۰۰,۰۰۰ تومان = ۱,۲۲۸,۸۰۰,۰۰۰ تومان
یعنی با کمک هم، تا امروز چیزی حدود ۱.۲ میلیارد تومان هزینه خرید کانفیگ را کمتر کرده‌ایم.
برای مقایسه، هزینه سرورهای ما نهایتا حدود ۳۰۰ دلار بوده.
اما اگر همین حجم دیتا را می‌خواستیم از فروشنده‌های فیلترشکن بخریم، با دلار حدود \`۱۸۰ هزار تومان\`، هزینه‌اش تقریبا می‌شد:
\`۶,۸۰۰ دلار\`
این یعنی با یک هزینه خیلی کمتر، چندین برابر ارزش واقعی سرویس به کاربران رسیده.
دم همه کسانی که تست کردند، گزارش دادند، سرور اهدا کردند و کمک کردند این مسیر ادامه پیدا کند گرم.
WhiteDNS رایگان ساخته شده، رایگان می‌ماند، و هدفش این است که دسترسی آزادتر برای همه راحت‌تر شود.
ممنون از سازنده های اصلی پروژه هایی مثل MasterDNS و فورک StormDNS
🙏
این اعداد فقط برای سرور های ما هست و نه سرور های اهدایی. اعداد واقعی خیلی بیشتر از این چیزا هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/whitedns/494" target="_blank">📅 09:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-493">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6eltJYgxmBXk_WiOXx7cvT4Khf9Zyw8p7Rjh48JWQlH0fIpBaNwZgOvJq__Kg0oNiAXtRk27TFs6g6ZW9IC2t20DFVCQKqvlFgw2F1F_KS8bthAq7SnRf8hQC6DIVLv2-NmYaRzaslr1EbT3p_Oa4a8EfCJPbfy4NgNoOVujdVfELY07ig3eU6IHjLjPJf8NdTf0xVTC5uw5hFN1gvCZPyahlwG7y-7lNHuumkt2pC0sKHlkgUHj5IiSYX4HigXyap5Y-GnqiPRTeekpP3E_HJByXW7g8h0be_Hp6fmu0X6E8SaZF7-7W_iZZ22B1ZRX3E8-JhT7816_kMzuk526g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربات WhiteDNS حالا امکان جدید دارد برای دریافت ریزالور های MasterDNS / StormDNS
۱) وارد بات زیر شوید
@dns_resolvers_bot
۲) متن زیر را برای ربات ارسال کنید
/dns_master
۳) برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/whitedns/493" target="_blank">📅 09:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-491">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">server_config.toml</div>
  <div class="tg-doc-extra">11.1 KB</div>
</div>
<a href="https://t.me/whitedns/491" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
StormDNS Server Tuning برای لود بالا
پست مخصوص دوستانی که سرور شخصی دارند
!
ما برای سرورهای StormDNS یک اسکریپت تیونینگ آماده کردیم که هدفش پایداری بهتر زیر
فشار و کاهش قطعی کاربران است.
این اسکریپت چه کار می‌کند؟
👇
✅
قبل از هر تغییر، از فایل‌های مهم بکاپ می‌گیرد
✅
تنظیمات server_config.toml را برای لود بالا بهینه می‌کند
✅
تعداد UDP reader و DNS worker را بیشتر می‌کند
✅
صف پردازش درخواست‌ها را بزرگ‌تر می‌کند
✅
بافر UDP/socket را افزایش می‌دهد
✅
محدودیت فایل‌ها و پردازش‌ها را در systemd بالا می‌برد
✅
تنظیمات kernel/sysctl مخصوص UDP و شبکه را اعمال می‌کند
✅
پورت‌های DNS یعنی 53/udp و 53/tcp را در فایروال باز می‌کند
✅
لاگ را روی WARN می‌گذارد تا زیر لود، سرور با لاگ زیاد کند نشود
✅
تایم‌اوت اتصال SOCKS را روی 5s می‌گذارد تا مقصدهای خراب یا unreachable کاربرها را
مدت طولانی معطل نکنند
✅
در پایان سرویس stormdns را ری‌استارت می‌کند تا تنظیمات اعمال شوند
⚠️
نکته مهم: ری‌استارت باعث قطع شدن sessionهای فعلی می‌شود، پس بهتر است روی هر سرور در زمان مناسب اجرا شود
اگر نمی‌خواهید همان لحظه ری‌استارت کند:
sudo bash /root/stormdns_tune_all_servers.sh --no-restart
اجرای عادی:
sudo bash /root/stormdns_tune_all_servers.sh
📌
این تیونینگ جادو نمی‌کند؛ اگر مشکل از resolver، DNS delegation، مسیر اینترنت
کاربر، یا destinationهای خارجی باشد، فقط با افزایش منابع حل نمی‌شود.
ولی برای سرورهای پرلود، باعث بهتر شدن queue، socket buffer، limitها و رفتار اتصال
می‌شود.
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/491" target="_blank">📅 08:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروح جنگلی👻</strong></div>
<div class="tg-text">اخرین اپدیت سرور های روح جنگلی از ۵ سرور ۳ عدد به استورم اپدیت شدن
سرور فنلاند
v.0x0.guru
Key:
33815e1bcb88873f2199c735828ea745
سرور فنلاند
v.iranmn.best
Key:
aaed913b8367fce3e20910472d9e3e2d
سرور آلمان
v.kmjhfilterchi.shop
Key:
4f3d0262ba2bd7cc20b596bdbc77f761
روح جنگلی
WhiteDNS</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/490" target="_blank">📅 08:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPy9P8HsjZF_uN3qtVN0noZ4x5BS0rWawJzo2N2PBc_QsGpIfn3b3qF3vg5CjP87baecVQzDSBZOOPznAg3lXfFuL_2Kc8T05gjYK2g8DJzOG1Wi2D-whgyLJjQe1J7XUwIyjYS9t758rAUGEO0zft4jVnXkelqnIoYmLDY3_b9OymSOrHLC4eu7YWJuEHSasGFozVzdnoT1Fq3XvGYrDB40tMkuU50jd0ImuAB-RbwLcJjOyUIL_0o7ApmxBKg6T1wnYqEJXqyn2gHufmfjBFgogXWPi9GO6bHPrtq-M9nt_1yr0rw2Lr0Jeqz26Jk3IbaiJIlXDS7ZT299-xFh4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همه دوستان
🌐
برای دریافت آخرین آپدیت‌ها، آموزش‌ها و اطلاعیه‌های مهم خارج از تلگرام، حتماً اکانت جدید ما در X رو دنبال کنید:
🔗
https://x.com/WhiteDNS_Team
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/whitedns/489" target="_blank">📅 07:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد Advanced Settings شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup:…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/whitedns/488" target="_blank">📅 05:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/487" target="_blank">📅 05:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djhI3padCqRIsRFS--7bqdJIFCN8Bx64zvqIiIiPpgvdb3fwHEUHHJylLEVYo2NqfrSCHyzPHTRXS6OEcND4PcKcGKWhnl5IA2Fk_25_4FWB7GJw3Je96UE-xukT1kdKWKGvXE2uKFLDw_Vl_l66UE9xYrKzPp4KCvkJzykyZ5uOU_Nw7Khk-31Naf9ttQg7T_X32qo7jQ1mTwSxK_BktrfWVT87HBQezHM0PGcOBA_pabNWJrN0MbfuVv8tdk6DQVBJmBJR_FnQSnk_3u_6KcrI6YdrtR0xO_sGahw8YlRdGp_IaexoHc_OuqkxemfeNJJ9pXPM9mIO7M-suMDxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد
Advanced Settings
شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup: 1
🔸
Download Dup: 4
🔸
Upload Compress: OFF
🔸
Download Compress: LZ4
📊
این کانفیگ به‌صورت حدسی انتخاب نشده.
ما لاگ‌های سرور در ۷۲ ساعت گذشته را پردازش و بررسی کردیم و بر اساس پروفایل‌های موفق‌تر، MTUهای پایدارتر و مسیرهایی که سرعت بهتری داده‌اند، این تنظیمات را پیشنهاد دادیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/whitedns/486" target="_blank">📅 04:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS_Resolvers.txt</div>
  <div class="tg-doc-extra">8.5 KB</div>
</div>
<a href="https://t.me/whitedns/485" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">۵۱۲ ریزالور جدید تست شده تیم  WhiteDNS
مخصوص اتصال StormDNS/MasterDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/whitedns/485" target="_blank">📅 02:44 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-478">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخدماتی حامد📱📶</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOPrGVgKKyHihtgOUVa6yKffupt_tFFF649Iv0f35GHxZCAGJsORi8zPtdyZDov7RXEAubAd4vzYJko-0IDE38AW07hWkkaqiwx8G54LA89k3Wt03si49kU6NaSFqgCimS9xfWqNR9h2lEppJ1P7ivqI2cnem5vrWKNNVw0S0KqKmB2IEX1Egza1DT0vA5-AnOjYqVp9QEvHXcUM8wzLIfX3i9m7peqRD7Gi6_DWP6kp0EuK83HJuEhE1f82E99a-xeRucVQPo9QfeGZxmVQaVHnvBlT5iB-qOcFolrziyCNwpdwRKCQ-zAgl2NtytwIQjZDzAh7U-z0x_85fsDxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTIfoTJ3FZa9wgCrNIhfr14kKlAmVp96kH1nR3DWRLCY6I-f7bh4dvLaUe5yvOyfX1zaGmbhlLfzn7NEJR0ispeyQTFUfhdZ9tBAIYJ-z2Od8bBClGn12NoalqWjGYzSxTaZrfN8cmepdEVxHL-L3YmDHOMjHiU_NGtmbHr-TIPahShMYgWKx9xWRmTh2Ry6R4ja-ntxMdQV7awWZOmN8WNfUQ3WCOOQuQHJ1qZoFF4UHc-yLtuO_xxMk3R-lMQK-pVQ2PLNka5_Bs3wef4Zp0b9St9C3eajK1usQKp4UjtUrtFU4f7l9Ad5y47bWOKimMJ32Si85BDAk7IcRAclog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpElb004NXfz-nXHAS10p6FQTxxN4AOV-W4BNd5JWJPXG60xJDYFq9Byt3Bd6ZWEztRaHWMsXtmmDUW0O9K-6VX4u2I6YehL7IjXs9DxD7vCmoRWZjE5E8mI7g2Qn0t-T671bTJAoFVNZh0p5ysLOt4QJW_tVKsL7ix0Of-myhpW9sdZ6OpukJ-QIgFR8mj06spjA0cmGhceJDkZcMGwhfbR92uHEmppRGIBBs09N1y7b70rA7394Ppme0KAlvYHgn8JjhcxAL9m1RDaoP5RkeLBEeXpA6Wt-BfN-zoXc6pkCiGpuNY4LdkTeBimDEliiJMJK5Uos5cIN5_6Atvryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kx2wsNnrAEop6uv_FWNBH65-q4ay60Vlq6QvG-gKh_4ifTOOfDPOXa3BSk4uoraXz7Lvxoa0zdiqlCwuzYDylQ1JRiELIq904ueBdnfDupJIGUPmMl6HnbWMm2sMdmcHjGdfDeVnemDsTcQrCprZKtUA4yWPYFvpkIuW_yGK_wNPxR3kIvxYOQEvuHhWzPww_6Rp31O9qK1PiRWVL1KWD3N4ejbpYgdwvW-8zvmLcyRwrZm6E_LhOp7IAk9bxwlvVLYewbfwhtZE4Nbs_CFJpMaSwwyyrXOW-HOE7nDZotVgEgwYfA3LpQ4INlCcwrrHKA5DwRTnE2rG_cJua6fOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F863B_QkzCKg6ddpXKPr0IgjkCrJk25tmJriqZtNGJacMb--4eE6VswaGqXLR8SROpPODcM1QAWPIi7k4X1vvJNFlHIfGVw7flcrGhrLi-mv346zmjMYwI1OJ-0-cBAg9QRoAAoc5SAzofyXdp9R_Xb61v-rWWxA5VtdniQUc7R5wPMI1uWpRXjqztvi5fNhpzhr7sQeFz78uJKzysx4HGcJdgFd-ybMFq8sytleoSh_g8zPdG-RRJrWbSto9ciL6P9xVB9hljcpR3z0nZsK9sMpkvzwgEn_N_FDI0bJWcX_iERu6b4_cs9JFQOtofSaBAWorDl_zlkJPMyh3mJqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3der-WOgH6DmA-hPbiYOGjhY2Klu1m_GCT6CZTqzN-_o5HLXHt88Xey8RBBY-Tt12TrqqbC_XnSHlMr1-u20AglEke0mzBBlAtKIpl0FdOTJpCxA6GLw3LKFfZpL2rcpomFBtLZiznM8TjyNylxD0KIGnJeYPvOMA-LblYDNrL_oK5c_vpFiC7zrVAQYhCsHaCuDD8NbC1mPaSigf-zC4G-8IXPKyilE5eBI2FEElfcmbAGLkBz4jOk9DaZHgiKGjDioRsm6AXl9ZFbice-2vrdcNGCbvZBSi53B1UTmNCcWkIJh0m5v2B4yWCtnLnvIqkB5iYrZ6b-oQfBSr6U-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش اتصال وایت dns در اندروید
1- نرم افزار را از آدرس های زیر یا پیام بعدی دانلود و نصب کنید. (White DNS)
لینک شبکه داخلی (بدون نیاز به فیلتر شکن)
https://dl.toolschi.com/view.php?f=48c485b41de6bf08.zip
https://guardnet.ir/f/Universal
رمز فایل : 3666
2- مطابق تصاویر بالا کانفیگ ها و ریزالوز ها را وارد نرم افزار کرده و تست کنید.
کانفیگ ها :
1-
🌐
دامنه :
ob.networks.icu
🔑
کلید رمزنگاری :
3947d5ac68015a09a53a0b361bd82999
2-
🌐
دامنه :
ts.networks.icu
🔑
کلید رمزنگاری :
e0e71e667e5dcfe3b18e3bce659773d2
3-
🌐
دامنه :
zw.networks.icu
🔑
کلید رمزنگاری :
0798c0e8aa05080125e6c65282fd792b
برای دریافت ریزالوزها از ربات زیر استفاده کنید :
@dns_resolvers_bot
اتصال این نرم افزار در اندروید روی پورت 10886 و لوکال هاست (
127.0.0.1
) است.
پروکسی تلگرام :
tg://socks?server=127.0.0.1&port=10886
‌‌
@hamedvpns
☑️
لایک   |   Like
👍
❤️
اشتراک بزارین   |   Share
⭐</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/whitedns/478" target="_blank">📅 02:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/whitedns/477" target="_blank">📅 13:21 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fzBpfeQLOBBR8jbiPRYCDicS72gt-Jb_utXC-smQuwB6Z7FjC2wVdzk_jV4I_yeIkduGqc2fNDPeXB2QuNqIcGPRCjy5JGkUeWAucRBpv1cR9vLFOLb9UCp39wPEwRr1rfOOD7PjPjCj7_g1GR5MhN8Zy1Yecy3FTqSl-WgY9WCk4lenWQyjj1NFJ1V_ptGZXObCR9mZBX8E9zfDKUDG_B9vdy0T-dsAD9Y3q1az8qWxh04I5OAMc-kLw5IuDSwAF7tTkaylSb0xq8_63hKelZXR54PVGbrb7MSF1Ek46uefi22Y0Kb4X16mkV-sstY_Rlt_1s6mIOIzA1WCkzqVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/whitedns/476" target="_blank">📅 13:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-474">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkBjFf1CW8enJtXYJ6o9ZL75LeUH7sLmwVFkxjmltbzNRCSPnF7bug71yrOzMR5iooZ01g61jPt_mUV_9Plwn7leArWWwU7sFOo_UXzqsUQeV1A9WjH4XqiWXMe9OWdC-SNpm5FPVhtjpa9P6x2sU41RvTcG3gL2GEGjln2TRfMba-HzqKgPHAn1exz00lQiLelI_I-bRAQ_4J9g8hVKYEZkfBLTtx9wJdpumE2oY937fDb0E6d6nx81zSBCO-MiAWPRSrdS55GKpTDsAlwDOGL2RwM5S3Se7E9sl0wfP7ehkCuj_WdWLVwV5l7kWLSo1_QTOaYw1N3Cwmzi5hCRLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWzYOORvNz__Vppul6j8rJbTi7VKlN67l4D5o6H0qMPWkQsSxSy3vjcKc6pwdy30Ec3hBfKebn-Hlk6K50kAcOENe4yfyfgYKNMcbWUigc1pwVRKn7vxcl2FEjeQrAdj2tVeoEeta-WVBZ9MaCABlJD3ELlMZ7uat0Chj5zcIQcRwegfWPBdRPWYfJ3_b__5PO_94FoP6mI8e7feN_7pVKRmiYV_mlhrBn0cauIUMzPBwALonicNjBEbmPRPbHLXnZphidVgg4Vmv7lyrFFHWy2X5GO9SDMJs7Cu46p-j_W0QqkHjFJCIsxYoT6lEetzCQqto2T0pgzvDM5B95dFXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">╭────────────────────────────╮
⚡️
WhiteDNS Configs For StormDNS
⚡️
🔐
۱۰ کانفیگ‌های اختصاصی و پرسرعت ╰────────────────────────────╯  01.
🌐
Domain: t1.prs612.us
🔑
Encryption Key: 3e80a0eb3e1fba2bf17e0e0eb5783dc5 ━━━━━━━━━━━━━━━━━━ 02.
🌐
Domain: t2.prs612.us…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/whitedns/474" target="_blank">📅 12:31 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">╭────────────────────────────╮
⚡️
WhiteDNS Configs For StormDNS
⚡️
🔐
۱۰ کانفیگ‌های اختصاصی و پرسرعت
╰────────────────────────────╯
01.
🌐
Domain:
t1.prs612.us
🔑
Encryption Key:
3e80a0eb3e1fba2bf17e0e0eb5783dc5
━━━━━━━━━━━━━━━━━━
02.
🌐
Domain:
t2.prs612.us
🔑
Encryption Key:
afc1bd5e98cd98cde7515adb7295122b
━━━━━━━━━━━━━━━━━━
03.
🌐
Domain:
t3.prs612.us
🔑
Encryption Key:
8786a860148e2d4d55403ae3c80ba854
━━━━━━━━━━━━━━━━━━
04.
🌐
Domain:
t4.prs612.us
🔑
Encryption Key:
943664f15fd1763e242ce12ba993d9c9
━━━━━━━━━━━━━━━━━━
05.
🌐
Domain:
t5.prs612.us
🔑
Encryption Key:
6a9ab24a8bd3937378efbfb3c23e1358
━━━━━━━━━━━━━━━━━━
06.
🌐
Domain:
t6.prs612.us
🔑
Encryption Key:
71201fedadfbc0b62189c08961bce651
━━━━━━━━━━━━━━━━━━
07.
🌐
Domain:
t7.prs612.us
🔑
Encryption Key:
c4ff91174a79e9e03a4d6727878ada17
━━━━━━━━━━━━━━━━━━
08.
🌐
Domain:
t8.prs612.us
🔑
Encryption Key:
ae5db6f03e485214e1fcc9d26a4c0a2f
━━━━━━━━━━━━━━━━━━
09.
🌐
Domain:
t9.prs612.us
🔑
Encryption Key:
a01c03a340a3e684a2815961e086eb27
━━━━━━━━━━━━━━━━━━
10.
🌐
Domain:
t10.prs612.us
🔑
Encryption Key:
f3a3c5d02bb7ce04f6a4f144fc35e9cb
━━━━━━━━━━━━━━━━━━
11.
🌐
Domain:
t11.prs612.us
🔑
Encryption Key:
e7f2db07e778563d31ed1fc80d5fe612
╭────────────────────────────╮
🚀
Powered By StormDNS + WhiteDNS
📡
Stable • Fast • Secure
Configs by
@PersiaTMChannel
@WhiteDNS
#Servers
╰────────────────────────────╯</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/whitedns/473" target="_blank">📅 12:20 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRt4ObzW0_8OxuJqefuyd4aqaAoKkxjBfpmMPLiHKVRKv9KswNSqBhEGmU7ulHb88D-IzzdVfMF876SmZgxmQJZSZn3FUbKLZ5-eFvOFQc_qcTcZ3RONAYyMTWMVL_mw1tRwjjDLifeLPUBOAb-PMEcnqsHtZQWNaYo3-QiPMouSF-XhFehU5ZGsFtSXWLAsbqn0-UuMBluIlYTeSoOLBrQfjhlCwBDG204hdfJeRiT6Mq3rcuX28zN765tucJHx1OzweipVCLt9MZGM8h5zKsHq6Xh1Nw5Vu_4qTO0YBfJCggLHqTO2FtA1L-t20oMXx1a71h6xiKfeiYijy1AUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteDNS روی گوشی مثل «کلاینت» کار می‌کند و به سرور StormDNS/MasterDNS وصل می‌شود. چون این روش ترافیک را داخل درخواست‌های DNS می‌فرستد، برای اینکه روی اینترنت ضعیف یا پر از قطعی پایدارتر باشد، بعضی پیام‌ها را چند بار می‌فرستد.
Upload Dup = 3 یعنی وقتی گوشی می‌خواهد داده‌ای به سمت اینترنت بفرستد، همان داده در مسیر DNS تقریباً ۳ بار ارسال می‌شود. سرور معمولاً نسخه‌های تکراری را تشخیص می‌دهد و فقط یک بار به مقصد واقعی می‌فرستد، اما حجم اینترنت گوشی قبلاً مصرف شده است.
Download Dup = 7 کمی اسم گمراه‌کننده‌ای دارد. یعنی خود فایل دانلودی لزوماً ۷ بار دانلود نمی‌شود، بلکه پیام‌های کوچک تأیید دریافت دانلود چند بار فرستاده می‌شوند. ولی چون هر پیام DNS جواب هم می‌گیرد، این هم می‌تواند مصرف اضافه ایجاد کند.
نتیجه: این تنظیمات می‌تواند مصرف اینترنت را خیلی بالا نشان بدهد. مخصوصاً با مقدارهای فعلی مثل Upload Dup = 3 و Download Dup = 7 و اندازه بسته‌های خیلی کوچک، داده به قطعات زیاد تقسیم می‌شود و روی هر قطعه هم هزینه اضافی DNS، رمزنگاری و تکرار اضافه حساب می‌آید.
برای مصرف کمتر، معمولاً بهتر است تست کنید با:
Upload Dup = 1
Download Dup = 2 یا 3
اگر پایداری هنوز خوب بود، همین مقادیر مصرف اینترنت را خیلی منطقی‌تر می‌کنند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/whitedns/472" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-467">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">22.2 MB</div>
</div>
<a href="https://t.me/whitedns/467" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه WhiteDNS Beta6 آماده دانلود است.
ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
لینک دانلود (Universal) :
https://guardnet.ir/f/8f0ef50b3049
رمز فایل:
3666
در این نسخه تمرکز اصلی روی پایداری اتصال و رفع چند مشکل گزارش‌شده بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta6 ارتقا پیدا کرده
✅
قابلیت HTTP Proxy اضافه شده
✅
حالا علاوه بر SOCKS Proxy، می‌توانید از HTTP Proxy هم استفاده کنید
✅
صفحه اتصال حالا درصد پیشرفت را هنگام وصل شدن نشان می‌دهد
✅
هنگام اتصال، وضعیت بررسی Resolverها واضح‌تر نمایش داده می‌شود
✅
بعد از وصل شدن، تعداد Resolverهای فعال و سالم نمایش داده می‌شود
✅
امکان دیدن و کپی کردن Resolverهای فعال اضافه شده
✅
وارد کردن Resolverها بهتر و دقیق‌تر شده
✅
حالا اگر Resolver اشتباه وارد شود، اپلیکیشن بهتر آن را تشخیص می‌دهد
✅
امکان Import کردن لیست Resolver از فایل اضافه شده
✅
5 سرور عمومی جدید به مسیرهای داخلی اضافه شده‌اند
✅
پایداری جابه‌جایی بین Proxy Mode و Full VPN بهتر شده
✅
اگر اپ را ببندید و دوباره باز کنید، وضعیت اتصال فعال بهتر تشخیص داده می‌شود
✅
نوتیفیکیشن اتصال بهتر شده و وضعیت مصرف دیتا را واضح‌تر نشان می‌دهد
✅
هشدار Full VPN حالا قابل بستن است
✅
آیکون اپلیکیشن به‌روزرسانی شده
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN بهتر شده، اما ممکن است روی بعضی دستگاه‌ها یا بعضی شبکه‌ها رفتار متفاوتی داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/whitedns/467" target="_blank">📅 11:22 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-466">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(سال گودمن)</strong></div>
<div class="tg-text">📣
تمام پروژه های به درد بخور برای دسترسی به
#اینترنت
همراه با یه سری ابزار های دیگه:
💎
پروژه آموزش تانل گوگل به vps
💎
آموزش کامل slip net برای سرور
💎
آموزش متد MHr
💎
آموزش نصب تانل به گوگل(خارج)
💎
آموزش متد Flowdrive
💎
پروژه آپلود داخلی بدون محدودیت
💎
آموزش قابلیت های Mahsang
💎
رادار چک کردن وضعیت اینترنت
💎
پروژه پیام رسان داخلی(شخصی)
💎
اپلیکیشن فیلم و سریال رایگان
💎
پروژه انتقال فایل به اپ داخلی
💎
متود گوگل درایو برای اندروید
💎
متود MHR و بردن پشت کلودفلر
💎
پروژه گوز مشابه MHR پرسرعت تر
💎
جلسه آنلاین با نت داخلی
💎
بالا آوردن کانال های تلگرامی داخلی
💎
آموزش متین برای Mhrv
💎
نسخه جدید اپ vay dns
💎
سایت رایگان فیلم و سریال
💎
پروژه vps شخصی با mhr
💎
اخطار کلودفلر
💎
پروژه تلگرام داخلی
💎
پروژه وایت dns
💎
پروژه های عزیزی
💎
پروژه Mhr روی اندروید
لیست بروز میشود
🍿
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/466" target="_blank">📅 10:49 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-465">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش ساخت متد MHR با گوشی + کاهش مصرف ریکوئست های گوگل
⚡️
لینک‌های داخلی جهت دانلود:
https://t.me/MatinSenPaii/2969
لینک پروژه اصلی:
https://github.com/therealaleph/MasterHttpRelayVPN-RUST
⭐️
توی این ویدئو بهتون یاد میدم که چطوری متد MHR رو صفر تا صد با گوشی بسازین، به علاوه‌ی آموزش یه کوچولو کاهش مصرف ریکوئست‌ها(به نظرم دیپلویمنت بیشتر بسازید راحتتره)
🚀
لینک‌های دانلود با نت داخلی:
https://t.me/MatinSenPaii/2969
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/whitedns/465" target="_blank">📅 10:41 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-464">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(مایلز گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izx_1AcNV0YuqZBUHtDn8DwNd6ORlyIMTZTjcgbSujsXbI5z3IVvD_NGSVVUIyEHW5eW8qMyKrdmr5f4T1ODZEXileVSrpsqZo5OcT7Nv1Lv6BrX7F4UyLMjEQsiTox0sUFbDL15WKVTLQ51qeaHzQLUvQx4zbdr9sQxyFvsx7RT0w4pf3rDnvjIma_rgkEJ8W0AhH9u-5U6QkTXLm4BCLKSCr5AyjQpatydsg8CubmIvkAv2xH0y3XunCtcO_z8tzIjeFEt30iXZRuX0WFKvC-KuPPIspARlsc-WDBBgwIRUn5ZcgpF4cMiI7sJ0YVQEFfb02xdCq6HwAO21G5YsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پروژه AzuDL - GC2GD
پروژه AzuDL - GC2GD یک ابزار کاربردی برای دانلود فایل‌ها از طریق Google Colab و ذخیره مستقیم آن‌ها روی Google Drive است.
💡
با این ابزار می‌تونید لینک‌های مختلف رو داخل گوگل کلب اجرا کنید و فایل نهایی رو مستقیم داخل گوگل درایو تحویل بگیرید؛ سپس با متود MHR فایل نهایی رو دریافت کنید.
قابلیت‌های اصلی پروژه:
⚡️
✔️
دانلود لینک مستقیم روی Google Drive
✔️
دانلود ویدیو و پلی‌لیست YouTube
✔️
انتخاب کیفیت ویدیو
✔️
استخراج فایل صوتی MP3
✔️
دانلود Magnet / Torrent
✔️
دانلود چندتایی یا Batch Download
✔️
تشخیص خودکار نوع لینک
✔️
نمایش نوار پیشرفت دانلود
✔️
ذخیره تاریخچه دانلودها
✔️
مدیریت فایل‌های دانلودشده
﻿
🚀
ویدیوی آموزشی پروژه در تلگرام:
https://t.me/luluch_code/22941
🔗
لینک‌های مهم:
🐱
سورس پروژه در GitHub:
https://github.com/TheGreatAzizi/AzuDL-GC2GD
👩‍💻
سورس پروژه در Git سلف‌هاست:
https://git.theazizi.ir/TheAzizi/AzuDL-GC2GD
📌
وبسایت Google Colab:
https://colab.research.google.com
📌
وبسایت Google Drive:
https://drive.google.com
🗣️
اینترنت برای همه، یا هیچ‌کس!
👑
@xsfilterrnet
🗣
@luluch_code
🏠
theazizi.ir</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/464" target="_blank">📅 08:59 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-463">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
سرور استورم دی ان اس (StormDNS)
Domin 1:
te.link-dakheli-app.shop
Domin 2:
s.o4s.shop
Domin 3:
s2.o5s.shop
Key :
TelegramChannel@link_dakheli_app
👾
کلاینت ها :
1️⃣
MasterDNS
|
WhiteDNS
2️⃣
MasterDNS
|
WhiteDNS
اگه وصل شدین ری اکشن برید بدونم
❤️
✉️
Channel |
@link_dakheli_app
| کانال
✉️</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/463" target="_blank">📅 08:27 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-455">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">tele-mirror-win-x64.zip</div>
  <div class="tg-doc-extra">141.6 MB</div>
</div>
<a href="https://t.me/whitedns/455" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📡
معرفی TeleMirror  در شرایطی که دسترسی مستقیم به تلگرام سخت، کند یا حتی مسدود می‌شود، TeleMirror یک راه ساده و قابل‌اعتماد برای مشاهده محتوای کانال‌های تلگرامی فراهم می‌کند.  این ابزار با استفاده از چند روش مختلف برای دور زدن محدودیت‌ها و همچنین منابع جایگزین،…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/455" target="_blank">📅 08:00 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-454">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhVJH01tqTnwql5CaTAgNRhhKuWg37SkpNHeeOARUN9ZlyN-B6W2JyxWbfg_ilYhQUmruwI-B28RTYFs8-Wrt611kb1AAY-SidNajeWClmgSo-Nrg32CczIaHqjbCeossXVY-ch3k59LT2MiJ-6P0U9PlRGlrzt0e9leWN68vFHgiAmxZXDM6W3OSp2bQSgGhQFxQhQZyhJl5pV3D7ja9GDsY5tTidTA6mb-X7-qUVzW4Aq--0ZPR24FdpuHk59JW4uw4agkZebhQ5l16yOT8H0rlNfn792JCqb1I9pb1J5QC_DBBKGhAuwHoGwmLpyFT_RHHCLRtA_oaV7FP3_bdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
معرفی TeleMirror
در شرایطی که دسترسی مستقیم به تلگرام سخت، کند یا حتی مسدود می‌شود، TeleMirror یک راه ساده و قابل‌اعتماد برای مشاهده محتوای کانال‌های تلگرامی فراهم می‌کند.
این ابزار با استفاده از چند روش مختلف برای دور زدن محدودیت‌ها و همچنین منابع جایگزین، کمک می‌کند محتوای کانال‌ها حتی زمانی که اتصال مستقیم به تلگرام ممکن نیست، همچنان در دسترس بماند.
☁
https://github.com/ircfspace/teleMirror
🤩
🤩
🤩
🤩
✨
ویژگی‌ها
👀
بدون نیاز به تلگرام
برای دیدن محتوای کانال‌ها نیازی به نصب اپ رسمی تلگرام نیست.
🔄
دسترسی چندمنبعی
ترکیب دسترسی مستقیم به تلگرام + نسخه پشتیبان JSON روی GitHub برای پایداری بیشتر.
🛡
روش‌های پیشرفته برای عبور از فیلترینگ
استفاده از چند روش Proxy مختلف، حتی روش‌هایی مثل Google Translate برای افزایش شانس دسترسی.
🎨
رابط کاربری تمیز و ساده
طراحی مدرن و مناسب برای خواندن راحت محتوا، بدون شلوغ‌کاری‌های بی‌خود، چون ظاهراً همین اینترنت هم به اندازه کافی اعصاب‌خردکن هست.
💾
کش هوشمند
کاهش تعداد درخواست‌ها، افزایش سرعت لود و تجربه بهتر برای کاربر.
📊
نمایش محتوای کامل‌تر
نمایش پست‌ها همراه با View، پیش‌نمایش Media و اطلاعات کاربردی‌تر.
🌐
پشتیبانی چندزبانه
امکان جابه‌جایی بین فارسی و انگلیسی فقط با یک کلیک.
---
TeleMirror برای زمانی ساخته شده که دسترسی آزاد به اطلاعات تبدیل به یک جنگ روزمره شده؛ ابزاری ساده، سبک و کاربردی برای اینکه محتوای کانال‌ها از دسترس خارج نشود.
☁️
https://github.com/ircfspace/teleMirror
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/454" target="_blank">📅 07:54 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-453">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/453" target="_blank">📅 04:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-452">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">۵ سرور اهدایی از رسول عزیز به کانال WhiteDNS  StormDNS Server Configs
🇩🇪
Germany Domain: v.eshkaftak.vip Key: 8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇷🇸
Serbia Domain: v3.eshkaftak.vip Key: 8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇹🇷
Turkey Domain:…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/whitedns/452" target="_blank">📅 23:46 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-451">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/whitedns/451" target="_blank">📅 12:48 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-447">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU-hkDRQiRYUdSpk9Findz5yRggMk_8A-shDLjwxSWjVyn6ZaaE32NX7Az0k8HaDL0Poff491r8BRXRrLZ6L7NZMBD5e3uiQUv2X1ZQ40SvOJIiTrxr7wDWO6gjDttx9uaah5oGbDVuXKI95BS1OwgwFJRPfwcQXCUwADEaTX5yndgWZdh_To5GW0_AVw_sxkbo97Kl28w8TTyl6N2qmUlz7OnFwP1scroUX0-iIcasVkoppvD04e2Q3sYa20o4-hdjyK2-w_7swGL9qZTyR0OT5vJo1w7jeuA81QTlLuGU_FN9g9WCaD7lLzWOp41nYlg_BHgyNPjfAg_JMZZq4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد ۱۲۵ ریزالور جدید به لیست بات چنل WhiteDNS اضافه شد
برای دسترسی داخل ربات ما بشید و دستور /dns رو اجرا کنید
@dns_resolvers_bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/whitedns/447" target="_blank">📅 02:33 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-446">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b225116bd.mp4?token=igo6N-XeA7SvS0cyFE5P6eqKw3h74dfEziiJ0keLIEJU4ywoRPnbR4KKbCBLCql5zuDvY6ifRFW9cEPhB8sAnonboIHdqHXLjKDc5pKbAFrkfHBOiRCVgWnbzwGl5dBYxqwPp7-RdCmHILZqlYWqY68cnzfb_c6IGJzD9i7LTprKWIiXUYxQtj3iqDBP12BOU_6DkV--yxcL-Q2pCeWxq4qXb3zfURMzgfdrPz3pAMKhccPyumCedMgVQewOHxGmU764aXUHdax1BcxFynYsLI6hEVynBDqpgkc9hJ3r0wK8cWKG06jjxZ2-rubiEqqH6wKZfyHK8iZAyjeVWHjPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b225116bd.mp4?token=igo6N-XeA7SvS0cyFE5P6eqKw3h74dfEziiJ0keLIEJU4ywoRPnbR4KKbCBLCql5zuDvY6ifRFW9cEPhB8sAnonboIHdqHXLjKDc5pKbAFrkfHBOiRCVgWnbzwGl5dBYxqwPp7-RdCmHILZqlYWqY68cnzfb_c6IGJzD9i7LTprKWIiXUYxQtj3iqDBP12BOU_6DkV--yxcL-Q2pCeWxq4qXb3zfURMzgfdrPz3pAMKhccPyumCedMgVQewOHxGmU764aXUHdax1BcxFynYsLI6hEVynBDqpgkc9hJ3r0wK8cWKG06jjxZ2-rubiEqqH6wKZfyHK8iZAyjeVWHjPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش قدم به قدم و نحوه استفاده از اپلیکیشن WhiteDNS
دوستان این سرویس صرفا یک کلاینت برای StormDNS هستش. میتونید از هر کانفیگ استورم دیگه ای استفاده کنید تا وصل بشید.
بعد از اتصال، برای پراکسی کردن روی لینک زیر کلیک کنید
https://t.me/socks?server=127.0.0.1&port=10886&user=&pass=
#WhiteDNS
#Tutorial</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/446" target="_blank">📅 15:40 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-445">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سرور اهدایی از علی عزیز به کانال WhiteDNS
StormDNS Server Configs
Domin :
te.link-dakheli-app.shop
Key :
TelegramChannel@link_dakheli_app
لینک کانال منبع
@link_dakheli_app
#Server
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/445" target="_blank">📅 14:56 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-444">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ux2Ohb22wSVpJvfvMAw63d-xqFD2AH7xUBrpfQ8MTyi2kkNPrbyZsiFgS4v9ytv1XGoaXITFQDxoX8_ezEdzlemP0DRqHOIVhagsSf1Al6p6y546dyWBjIytORb5x32F47pQ1hUnFGEruhckrmdSqkdi5azbFOR7x0CB4XV_4iYcxmq8vludheyEcWBshAqTNgFdRWWwt2gO6wpJfWNsuaANfxskdKTwT6aTW-3zqUzo_pSV8At4pdneAcATIZZlldh5NzCem-BMNOX3G0RgYSO6_OkiqSWQaJQnTY6dtw4KAzlG3jgJI03wLIDz__kO87G-G49VAvLCd--UAFFvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که نگران مصرف بالا هستند، میتونید مقدار های Download Dup  و Upload Dup رو کمتر بکنن.
تغییر این مقادیر امکان داره اتصال شما رو ناپایدار بکنه. بهتره خودتون مقدار هارو تغییر بدید تا جایی که براتون پایدار
متصل بمونه.
توضیحات تکمیلی
👇
👇
👇
👇
"Upload dup" و "Download dup" در زبان غیررسمی شبکه‌های کامپیوتری و نرم‌افزار رایج هستند و معمولاً به وضعیتی اشاره دارند که در آن یک فایل یا بسته داده، به صورت تکراری و غیرمنتظره بارگذاری (Upload) یا بارگیری (Download) می‌شود.
· معنای کلی "dup": مخفف کلمه Duplicate به معنای کپی تکراری یا اضافی است.
· منظور از "Upload Dup": فرآیندی که در آن یک فایل یکسان که قبلاً در سیستم یا سرور وجود دارد، دوباره بارگذاری می‌شود.
· منظور از "Download Dup": فرآیندی که با شروع دانلود، یک کپی اضافی و تکراری از آن فایل به صورت خودکار در جای دیگری از سیستم ایجاد می‌شود.
💡
مفهوم "Upload Dup" (بارگذاری تکراری)
این اصطلاح معمولاً در سیستم‌های مدیریت محتوا یا ذخیره‌سازی ابری دیده می‌شود:
· تشخیص فایل تکراری: زمانی که فایلی را آپلود می‌کنید، سیستم بررسی می‌کند که آیا فایلی با محتوای دقیقاً یکسان (معمولاً با بررسی HASH فایل) قبلاً در سرور وجود دارد یا خیر.
· اطلاع‌رسانی و تصمیم‌گیری: در صورت یافتن فایل مشابه، پیغام "Upload Duplicate" نمایش داده شده و معمولاً گزینه‌هایی مانند ادامه برای آپلود مجدد (Continue) یا رد شدن از آپلود (Skip) به شما داده می‌شود.
· مدیریت سیستم‌های ذخیره‌سازی: برخی سیستم‌ها هم از "Duplicate on Upload" استفاده می‌کنند که به صورت خودکار و پشت‌صحنه یک کپی از محتوای در حال آپلود در یک مقصد ذخیره‌سازی دوم ایجاد می‌کند تا از اطلاعات نسخه پشتیبان تهیه شود.
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/whitedns/444" target="_blank">📅 14:34 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta5-x86.apk</div>
  <div class="tg-doc-extra">22.6 MB</div>
</div>
<a href="https://t.me/whitedns/439" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
https://dl.toolschi.com/view.php?f=48c485b41de6bf08.zip
https://guardnet.ir/f/Universal
password : 3666
در این نسخه تمرکز اصلی روی پایداری اتصال و رفع چند مشکل گزارش‌شده بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta5 ارتقا پیدا کرده
✅
مشکل کار نکردن بعضی اپ‌ها یا مرورگرها در حالت Full VPN تا حدی بهبود داده شده . در این ورژن باید بتونید به
x.com
متصل بشید.
✅
مشکل وصل شدن زودهنگام VPN قبل از آماده شدن کامل اتصال برطرف شده
✅
وضعیت اتصال حالا دقیق‌تر نمایش داده می‌شود
✅
مشکل Resolverهای دستی برطرف شده
✅
اگر چند Resolver مثل 1.1.1.1،
8.8.8.8
و
9.9.9.9
وارد کنید، اپلیکیشن باید درست آن‌ها را تشخیص دهد
✅
مشکل پیام اشتباه Resolvers are required to connect در بعضی شرایط برطرف شده
✅
پایداری حالت Full VPN بهتر شده
✅
پایداری Split Tunnel بهتر شده
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN بهتر شده، اما ممکن است روی بعضی دستگاه‌ها یا بعضی شبکه‌ها رفتار متفاوتی داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/whitedns/439" target="_blank">📅 14:11 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/whitedns/435" target="_blank">📅 13:27 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-432">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۵ سرور اهدایی از رسول عزیز به کانال WhiteDNS
StormDNS Server Configs
🇩🇪
Germany
Domain:
v.eshkaftak.vip
Key:
8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇷🇸
Serbia
Domain:
v3.eshkaftak.vip
Key:
8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇹🇷
Turkey
Domain:
v4.eshkaftak.vip
Key:
8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇺🇸
USA
Domain:
v5.eshkaftak.vip
Key:
8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇨🇭
Switzerland
Domain:
v6.eshkaftak.vip
Key:
8705eb75abeedcd99001ef8d01cf9fad
#Server
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/whitedns/432" target="_blank">📅 09:33 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-431">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/431" target="_blank">📅 07:16 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBox-1.4.2-x86_64.apk</div>
  <div class="tg-doc-extra">15.2 MB</div>
</div>
<a href="https://t.me/whitedns/427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">https://c224731.parspack.net/c224731/ex/NekoBox_armv8_v1.4.2.apk
Nekobox
#Android
@whitedns</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/whitedns/427" target="_blank">📅 06:25 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-422">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ofunb4JB5kBGK_Q0sIadEaFOUl7Sv4A0_uEq0dtsUypZU-_mK4J7A0_urp3Z_55Ng4_dLA7FJyWxD6XYJ2LJmNfH43t4ZfwZg58VWi94pKY_oJmBLl-sOpJC0ZxgUoQGQPl9mf0lwLQPuGrXFrz-pB-I2rq0koqcGTUkz6LhRrQT5vUeYFyGSrjmu_blfZV40PSYCfu3-uDJ1koBhmWnqPH1MG4GjINVyz0LR_9I0jwdmkg0uH7LUKWb-iPQFJUyvpXqzkwjiWo1WjxCA5_NNlAxIrGaltuNR5coqY3om_q8SI7RRf-Mkp8X-koyjaH6HvIUkQiBjbESt3Lp99xk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/cuowWWBVPkt6csnHtLEHsWxe6LFMn6B7dtWj2d0g671XhEmWwPRVW3XSIhMmqzQgcLOX_wqI0Fbk-RBiIpStIUxXUO8GQhO2k90MBp2M1wW-UTkAzH0_wGVsvTYpG2jrRkKx6v-QaNd-xNDrEt_p15rQJGXSU_2Xk3kt4J9Me4VAIbom48zZJuJO3RVTFbH_gnNv7pEwBetS1v31OCBW_UO_1CcBXqtSfWo0WXpe4qu3Os23f41WmfWH-tWWuyQ4knXedvdT00KsK4fiXjLb6HSpgcjIuRbhb9zsIZ9d4GU70TQ2jsLu_zPM2ipLe-9byEqkbk3Icofq5wFV6vKU3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/fdzA3OGGp5mI0-qgu_0UGRBGRGnsBkQbuA5k3RMdnF9S5JUbeDbId3xK_cqaqkWEvYivX1jJfIRzniijkQ2eDoD7FwCJ3LOsuJPBP95-deq9ptHHTQBtIvuo7V3mMNbBslnQFiaLG4QG-oRwiyLBijIIZETmhYBmFxvm6XPVJqz05T8I80fgqY7Yj_qen_BNOZpq68zP9Uqz4cnwpfoInZBcGBDwBb38CZvEWheNU4y9G_Z-naif0PMDrxdmFD7yXhnvpPu3ABTuR3-bkGDoi7m_n4kzsfN-ipAIkzsOIib1za2GeEPLnj7WR3hj3wNSkyRF8ku47pAL7ZcWH0HrtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/u2skqwoRQQbdLiroODoGnYqYAudYSdYRHA_uE-_Novp9CLzP5RmDubUy5ttUMkuMgpnJjzeM2ra8PE_DnCbFZfw8gJzGshmHJhL-Rxb_YorScSoCpi1QKeYt__g1GiJr0Kfum2JLcH2QNKXh3lLGBHjG2a05rd25vBjqv60TDj-_moZJBjSk87LfwB4Re6EWkwNkc4fE_UAsAynYgGsgMK1lfNnkNqd3TP4rnjP5vQiW3U5U6otYHMoQO2hC_FjYQCOEkVMSS4R1CWFbi5zjoSzSINweFpaL6sAiC0sNTgZ-_EROnTFAQepQluEKNUhuCxI1rb1dFjIppzl19xwksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/JvTzg9mEVbSFxwua9Vy2u3i8i2L2cbaO4x89VTq8n0BcS5BL0UELVEsKtuj4CHtcpaKTaeXTJjqfBq3kaAW2yH8I5ShNu5CGMKCGPkdmfX8pXdOUwq7mpWXwnazAm9-vqCTK-AsmmQOU1p_U2CRD2XXIA6dMnHa9FgY7ntOUjlZirBCDCbjr7OzzW7_TIcbjHJTccU6UEsXGosanL7UcuXvNb6xyvTIXlujbbt57uRZr1e9axCc8gcJtXjRJpIt3GkRFZlewXtILVulOJjYWRnCrJ6KGnWwfK8D78NMOK9Hg7gkVSdHxDDkadft144LU3ozhZcxw_Kro0ap_Vf4Szg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر به هر دلیلی میخواهید از حالت پراکسی در whitedns استفاده کنید بهترین کار استفاده از اپ نکوباکس هست
https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/tag/1.4.2
#Nekobox
#Proxy
#WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/whitedns/422" target="_blank">📅 06:17 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-421">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">لیست کامل از ۱۳۳ ریزالور که به سرور های WhiteDNS در ۲۴ ساعت گذشته وصل شدن
91.92.214.110
185.88.178.196
2.189.44.68
217.219.162.200
185.53.142.174
2.188.21.58
2.189.44.82
2.189.44.83
2.189.44.86
2.189.44.84
2.189.44.85
2.188.21.70
185.128.82.2
94.182.154.105
2.188.21.46
2.189.44.91
2.188.21.138
2.189.44.90
2.189.44.93
2.189.44.92
2.189.44.94
31.214.169.244
108.162.192.0
172.64.32.0
2.188.21.62
2.189.44.98
173.245.58.0
5.56.132.97
74.63.24.205
5.160.140.16
178.252.143.130
62.60.197.83
2.188.21.130
185.109.61.27
162.159.38.0
74.80.77.245
188.122.68.218
79.175.172.101
217.219.29.66
2.188.21.146
79.127.170.15
79.127.170.12
149.102.250.14
45.135.241.33
44.244.148.52
2.189.44.66
207.211.215.145
2.188.21.78
78.38.77.2
193.178.200.3
194.61.120.143
80.191.163.249
151.232.36.4
185.236.90.12
172.253.228.147
172.253.12.157
31.7.78.205
79.175.172.98
74.80.77.247
172.253.12.216
172.253.13.148
83.212.7.243
172.253.13.153
172.253.12.222
172.253.13.149
172.253.13.156
172.253.12.221
172.253.228.145
172.253.13.146
172.253.228.154
172.253.12.209
172.253.12.153
172.253.13.158
172.253.13.157
74.80.77.246
172.253.13.150
172.253.228.150
172.253.13.155
172.253.12.210
172.253.13.152
172.253.228.148
172.253.228.155
172.253.12.146
172.253.228.152
172.253.12.155
172.253.228.157
172.253.13.145
172.253.228.158
93.118.109.213
172.253.13.151
185.53.141.230
74.63.24.206
216.147.121.35
77.238.123.179
46.164.99.102
185.10.71.13
172.253.12.151
172.253.228.146
172.253.12.215
172.253.228.144
172.253.228.153
172.253.12.145
172.253.12.217
172.253.13.144
46.245.76.162
217.66.203.211
172.253.12.147
172.253.12.212
156.146.33.97
172.253.228.149
172.253.12.149
172.253.13.147
172.253.12.211
172.253.12.150
79.127.211.213
172.253.12.154
172.253.228.156
172.253.12.144
5.160.137.130
172.253.12.158
172.253.12.148
172.253.228.151
172.253.12.220
74.120.14.49
74.63.24.211
74.80.77.244
74.63.24.208
188.122.68.216
216.147.121.181
5.160.227.78
85.185.1.10
172.253.13.154
172.253.12.213
#Resolvers
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/whitedns/421" target="_blank">📅 05:35 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-420">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/420" target="_blank">📅 04:54 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta4-arm64-v8a-debug.apk</div>
  <div class="tg-doc-extra">22.2 MB</div>
</div>
<a href="https://t.me/whitedns/415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
https://guardnet.ir/f/universalb4
https://guardnet.ir/f/arm64-v8a-D4
https://guardnet.ir/f/armeabi-v7a-D4
https://guardnet.ir/f/X86-X64-D4
pass 3666
در این نسخه تمرکز اصلی روی پایداری اتصال، اجرای پس‌زمینه و کنترل بهتر Full VPN بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta4 ارتقا پیدا کرده
✅
قابلیت Split Tunnel برای حالت Full VPN اضافه شده
✅
حالا می‌توانید مشخص کنید VPN برای همه اپ‌ها فعال باشد، فقط برای اپ‌های انتخابی فعال شود، یا بعضی اپ‌ها را از VPN عبور ندهد
✅
بخش انتخاب اپ‌ها برای Split Tunnel اضافه شده و امکان جستجو بین اپ‌های نصب‌شده وجود دارد
✅
سرویس VPN حالا به شکل Foreground Service اجرا می‌شود تا در پس‌زمینه پایدارتر بماند
✅
حالت Proxy Mode هم به سرویس جداگانه منتقل شده و حالا مدیریت بهتری در پس‌زمینه دارد
✅
نوتیفیکیشن دائمی برای VPN و Proxy اضافه شده تا اندروید اتصال را پایدارتر نگه دارد
✅
اگر دسترسی Notification غیرفعال باشد، اپلیکیشن هشدار می‌دهد و کاربر را به تنظیمات مربوطه هدایت می‌کند
✅
در حالت Proxy اگر StormDNS بعد از اجرا متوقف شود، سرویس تلاش می‌کند آن را دوباره راه‌اندازی کند
✅
راه‌اندازی Full VPN پایدارتر شده و StormDNS حالا داخل سرویس VPN مدیریت می‌شود
✅
لاگ‌های خطا و وضعیت اتصال واضح‌تر شده‌اند تا پیدا کردن مشکل راحت‌تر باشد
✅
آمار مصرف دیتا و سرعت اتصال مخصوصا در حالت VPN دقیق‌تر شده
✅
تغییرات Split Tunnel در حالت VPN بهتر مدیریت می‌شود
✅
ظاهر برخی بخش‌ها مثل هشدارها، وضعیت‌ها، رنگ‌بندی انتخاب‌ها و اطلاعات اتصال مرتب‌تر شده
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN برای تست وجود دارد و در این نسخه بهتر شده، اما چون کل ترافیک دستگاه را از تونل عبور می‌دهد ممکن است روی بعضی دستگاه‌ها یا شبکه‌ها سرعت و پایداری متفاوتی داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/whitedns/415" target="_blank">📅 04:11 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-414">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Gl_knhOjRL0FLaxOwh_axeMTnO4PCh17ClelEo2pOI-OlD1nHGXMsrHDfhHubBN9MpexdWlNJWw5IOQaM0GTrfDKcZI2ZM3MojJLR_6X1RsfDSmsXIrBJwvREHpt5kgobYc9VO8TEfeQG382t0HVhKW093LTxgoJDPXlPHcm_mW9GQIZQnSwG0uHTa29DthC8muoa7yoAA_8ChodoffXvgDiM717vF7sIm2gkI_y5YYxFI0xKg9oTynutzqLeuaGZlX5RMvG1xqGS7KueOVqOiPtFBdbn66YmbWQ9LHcgSDcTJoDIEi1DDv1fLZqYT8rDqIYct5F-eqmIIII_CGdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید Shade قرار گرفت
🙂
- قابلیت exit node از طریق
http://val.town
اضافه شد. الان chatgpt و claude هم باز میشن
- حتما طبق دستورالعمل داخل برنامه، اسکریپت جدید دیپلوی کنید
- تغییرات و بهبود رابط کاربری
این کلاینت برای MacOs است
https://github.com/g3ntrix/Shade/releases/tag/v1.4.0
#WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/414" target="_blank">📅 19:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-407">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHP5cGQqaqqTXl-S-i16QimQE4OEJLHcVfCP1iH4_s2QBXTfbHwqqSHRvSkZr7kwezd3KDMvuhnAUUXgqPbQCxXXA5Q_M61j3TAueYxnIRjIEehyQeEc0KCx8-HAA8f_j3OodcjnIbSoNRzs6eXQk-qZ1rRVXaPQUhTjeXhImaQJ6WAme6p3uUED_k6ljIi-cIp00kGa6_9bp4EheRZYXgtT5UNRCCiD05sFtBv2olxvzNlSigRVQu0MG-IfvbGoIF1uv7i7TDTsKardoXZGGKCrk5j0D7uvRDKCVpgVVJFop4pr-3oVcHpy1bu2fc7KbuCKBfW0i5uTDaWsL8wjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCKk5aNfJZn1aqCFgM2uL1mVNafXskqzXCLXGZR4IFXA9kvsjmKFtADPB9pQmzq2pAkBTR9VGxtDO5UnBI1nzoqmuAC1aCdis0t8JKtMKUqAxvUOJN68OYrWc1v9_MubRImeKS93S_pyjHxq4HRPS3KCBy-qTPmrAeQUGSOYev-iyFTN_9V96RUUCq38vgrEC7BLPzWFtOgY94T-4AmbUEckyi7eN5FiZaXSfjatztj83sh1pbBpu6zdr3VngtiEGbP6miNX4MlHdxE8ajsUS4Jk8NNT_lznKMYcaHw3cJLeRm8YtUQVNFI3kEuWGVLnxuLvtKmnn4boZZqbDZBrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgB1Hh27qaEfRZBn2hWbFcdVWJh3ZU-6OaRVx4fJARzEXwsfjpS8ERunTR9bfAy4qZmwhHGi2Zbaacn2d0dgKdbv9B-uqfamgEivwhG_Q0RXskTbKrIAE2Eq_btULXnjHmbDJiOhBrv8Y6vc4KKk1cJjpZ_6VLsnBmir6RFCBadGMKjkpZVThrphU5l_ofk_7o-WlgIOv3X7t3LpaSrp91TjT_vwuh2_Hog7trGuYeaBSaM0A_kFjikbHlkMFFPikB2sP-OCjsVk8Kn8-Dn2oKb_wUUHrA8dMjRzee00OUy-DzlwjceAlsgb4LLHSlMN1vR-0hPGyYkPoqAq-Y8cdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LmKHrZaO5bXuCrGl7U11Y1vSKHLwanHDYPyUN5qp9wn_8FulCLjcDe6X2kSbnWFPP3bvYraNhW0GukNZ5qI9rPz5EI4fh1yblPNLVj-Ygvl-xeKGcBlWKVLMvU6fkrK1igofxKNpBYgsNZVtBlLv8Ec4AUDQK4KEmA0owJrClbfIR14sFYG3dgnedLJ5tZbQ2lly1gl7xM_i8poX3qrn7oDEzA9vCPL2cAYGpalybFDYfNAnnsUU66mgW-y3CtNx7YAdUTlZ_fi8_L10EH-96B0Ezv998K6QWJUTOWWRBTFFLR-NNWLw5cS7CIqxKSrw15glx4TyPmHS2ORioEMD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLrccZmlwYQfyAyFVUEGZGdF3qZz26kRVk03SjNDXtlhAd_3yLPWHWpZDU3ebaUHawNLc9UT0dT6M64XfTInW0u-fSBQUC-i-SV8GcHzNR9UkRaHl3u_F3o2Vs8OndfHtu0JcRCUhllRgnYY7l1aWPtZcwn-b4j5R7EsbWo55IzP7u8JsVpB6kpYh_dCIuEXLuXaQP530iUAMlUZtlx8n1d-EoDL5_Jxm8ivWPOFfOUY2fupF1FFpEF0AiZQz0G_CBet6dWWV42IRalzVrzLddLv8lCQNs7JhQm2oMDGnGMAMfw9o15xjjl4ZM8qrwLRSHmWnCRA49nHg-Je8a92qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bsnHajzZuwpkBi5ms7yVUc_1C0TLfr-cnh-FfH9avDsruLaPNRxD9kKz9Y6BMzb4dsdwlETFc0BXaAwtXbZ3kkrL4e3KasacM5k3UGYhLZK-FXmsRRSlRFLcuyhZFj_vmiAj3b705rl7UqvHpkjAr9rn9oCn-70NGG8iBXgfcdkYwDhdLDL70KKtEgkWGIe5Oy3Jo09UrvZoyNmYVQz9CtE8geH0fr_a4muCaO1MGHkhnEc5csLuoQ3ZpdsTIUT7U26-0djzugvtKw-0etqSuXuJrNruTw39EtCBXccTGS7fTS0izNI3S7HVCYK0pV1Qy5AMVeL3OzFQmcsFaLDYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K58NWDQY1TmbgygUGljLaLVdSzfczI1_LBWm2LUDWaYKiDY-dhNdITEJupUjJSQKiLW-qr7jfm5td-4o1sA5nPmUQL-PfbuHxba-_Z4AQ29iM8NbrkHyOgk7_31NPIdwleZh2-8PdQZwjAhhbuVjwXxVCYu8iSh5NYEaKgCeeZIEsdBfCZi-TqHFW9S7nYL_85MVIN-JC2OhweQO8FO4SBfwNvPsrnqdtthSd_3xF5apcEPPm9ID8G8mGhD822S42z7nAnLB8V59zHVXdFEg1cGAr5Myq8XPUA18cYg5SPA8h8xKX9jdrSmRcR032j9k5QW726B-5kn_hb4EG3ZaDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه دوستان
Network Activity روی سرورهای WhiteDNS به‌طور قابل‌توجهی در چند ساعت گذشته بیشتر شده. به نظر می‌رسه تغییراتی که روی سرورها انجام دادیم کمک کرده و تعداد بیشتری از کاربران تونستن کانکت بشن.
در حال حاضر سرورها پایدار هستند، اما اگر امکانش رو دارید، پیشنهاد می‌کنیم سرور شخصی خودتون رو هم کانفیگ کنید. این کار هم فشار روی سرورهای عمومی رو کمتر می‌کنه، هم اتصال پایدارتری برای خودتون می‌سازه.
در روزهای آینده آپدیت جدید اپلیکیشن رو منتشر می‌کنیم تا چند مورد از باگ‌هایی که گزارش شده هم فیکس بشه.
ممنون از همراهی و گزارش‌های خوبتون.
مثل همیشه، لطفاً اگر مشکلی دیدید با جزئیات گزارش کنید تا سریع‌تر بررسی کنیم.
لطفا چنل StormDNS هم دنبال کنید و ازشون حمایت کنید.
https://t.me/nulllroute1970
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/whitedns/407" target="_blank">📅 17:10 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-406">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b225116bd.mp4?token=CSH7DCVFBMrjUCU2rSg9vO-BLAqmPFp-BwAYVfbfrzWkwBU01rKb2wAXG8tB0TL0j_htBBfk06u_wZ8rKmtjcakQOgNzSRe1NCcLnzfONvqXmOqYis_5TUkTuBLU5oNmI6F62nMerafI-lJUQkuzE6cC-H75wVlkWxyPTGaIBYajmdTvpFbCkfMllWqX5gENeBO-Vz6cuwL1akspVlrf2VnSF_IYZdUuWA6F-qPrDgyWylPNlTpXNZGeBEDcDHjBTRhMZGLuOd_KyAK_HSgsUtrtdm-wz0nN7359dcBhI_tvhRtfp1-a6alD2BVvbUFOjIDWplAZLL2ZEyQdb5BsJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b225116bd.mp4?token=CSH7DCVFBMrjUCU2rSg9vO-BLAqmPFp-BwAYVfbfrzWkwBU01rKb2wAXG8tB0TL0j_htBBfk06u_wZ8rKmtjcakQOgNzSRe1NCcLnzfONvqXmOqYis_5TUkTuBLU5oNmI6F62nMerafI-lJUQkuzE6cC-H75wVlkWxyPTGaIBYajmdTvpFbCkfMllWqX5gENeBO-Vz6cuwL1akspVlrf2VnSF_IYZdUuWA6F-qPrDgyWylPNlTpXNZGeBEDcDHjBTRhMZGLuOd_KyAK_HSgsUtrtdm-wz0nN7359dcBhI_tvhRtfp1-a6alD2BVvbUFOjIDWplAZLL2ZEyQdb5BsJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش قدم به قدم و نحوه استفاده از اپلیکیشن WhiteDNS
دوستان این سرویس صرفا یک کلاینت برای StormDNS هستش. میتونید از هر کانفیگ استورم دیگه ای استفاده کنید تا وصل بشید.
بعد از اتصال، برای پراکسی کردن روی لینک زیر کلیک کنید
https://t.me/socks?server=127.0.0.1&port=10886&user=&pass=
#WhiteDNS
#Tutorial</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/whitedns/406" target="_blank">📅 12:50 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-405">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">من با این لیست وصل هستم خودم روی همراه اول و سیمکارت شاتل
185.161.112.38
194.225.152.10
217.218.155.155
185.20.163.4
78.157.42.101
31.24.234.37
31.7.78.205
80.75.14.102
185.255.89.57
2.188.21.138
2.188.21.58
2.189.44.68
185.110.244.150
2.189.44.98
2.188.21.62
2.188.21.70
80.210.40.55
85.185.163.4
2.189.44.66
2.188.21.46
2.189.44.84
2.189.44.82
2.189.44.86
2.189.44.85
2.189.44.83
80.210.40.53
2.188.21.146
172.64.32.0
108.162.192.0
78.39.234.230
173.245.58.0
2.188.21.78
2.189.44.44
185.20.163.2
194.60.210.66
217.218.127.127
2.188.21.130
31.24.200.4
2.185.239.138
5.145.112.39
85.185.85.6
217.219.132.88
178.22.122.100
194.36.174.1
185.53.143.3
80.191.209.105
78.157.42.100
213.176.123.5
185.55.226.26</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/405" target="_blank">📅 11:46 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-404">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستانی که امکان ساخت سرور دارن لطفا StormDNS رو دریابن
کانفیگ این سرور ها برای بچه های ایران امکان پذیر نیست هم از نظر هزینه هم دسترسی
اما کانفیگ کردن این ها برای شما فقط ماهی ۵دلار هزینه داره
با یک سرور شما شاید ۱۰۰ ها نفر به راحتی میتونن وصل بشن
اگر از نظر فنی اطلاعات کافی ندارید میتونید از پروژه گیتاب StormDNS آموزش رو دنبال کنید
https://github.com/nullroute1970/StormDNS
لینک چنل StormDNS
https://t.me/nulllroute1970</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/whitedns/404" target="_blank">📅 10:30 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-403">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzUqIIb8tt9QbdRfr2MzKx5n75LEn0b54rLodZo_EWg_gh1TjJmEfpnDbBgh16xQh8gKhB1AMpu2DzSzTh5bIhdz6MCJktyf56dzq2MUIrTVOJHmky3r2FyyY40bs8WZywmaB7ia_Mlhb2jUM-YEIdq-CekQYgB-m6HJIJ9CIPn2tYYxeqNH8ckHXPEkK38In4Bph1cpJJz_hndWtFNPveeMgklE2xfv2KgLLCTXWXWCOsvM74EYwdpmUl5lDLwFX62DkKt5ltw_UAf6l4gXpcApW_k5DFwecX_O_S_hbyoywuAhCkDGC5SYy1Fkzyc2e-iNMf7GZI7RkFPcuA4X9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیکس برتای پنهان شدن منو زیر نوار سفید اندروید هستش</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/403" target="_blank">📅 10:26 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-398">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a.apk</div>
  <div class="tg-doc-extra">22.1 MB</div>
</div>
<a href="https://t.me/whitedns/398" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
دوستانی که مشکل کاور شدن منو زیر منوی اصلی اندروید رو داشتن، میتونید از این ورژن استفاده کنید.
همچنین نسخه منسب برای cpu های مختلف اضافه کردیم.
⚠️
اگر مشکلی با منو نداشتید، نیازی به دانلود و آپدیت به این نسخه ها ندارید.
اپلود شد ورژن یونیورسال
https://uploadb.com/rtfjbrhh1dml/Beta.zip.html
پسورد زیپ : iran
لینک کمکی
https://punkpaste.ir/f/app-universal-a55ax7
لینک کمکی
https://guardnet.ir/f/arm64-v8a
https://guardnet.ir/f/universal
https://guardnet.ir/f/armeabi-v7a
https://guardnet.ir/f/x86-x64
https://guardnet.ir/f/beta3-debug
password : 3666
@WhiteDNS
#WhiteDNS</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/398" target="_blank">📅 10:25 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-395">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ou7l1hYnNaRDLyePX_AI5YW5dg_mwvgLELCHsm5POfX0YnT-7ZTNinq5B906EpLMSfhYGvfb26WcgOkAkkOvW393d3JZZyZskdo79q2VobbhN0fyLIxLEYKAE03vxj58aT_NJstxsi4zUeaYre7Z-sYQ4g8ikdzB68dUeFqaIMlycfgvHmcZG5fJv4cHXyMqltLe6VM7EQrvfESzU8aU6K4ZCOq5UmWIyzMGjhWsts0FoX5hzd5UpOqMVB49dmb1XrXuqVGfUzKoO6_7J_ao5bPOWwJ2v45OfH5-6qEPWF0iMHg1GVDzl9Q5fjoUzEZkiCye-6aX2jf37b1YlF9mgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUuDrQMfUSaQqN4d24vBgc5jRuD_qSrumYSJOIeEyAeiM1bGt1yELfnGcwNcld75nFhmiZwBd1eby3xDBK-FU63BoQdongMyQA3hJDYI38y7vNc09rjUDKb2LerB_v_odPn3HNL-WVH5_ZFAl8p0cy7A83SULsM2OvTN3BZgI5YyAEXfACdYg6LqJJS5DTHZL1weQ4w6IL8E1E9eLr1Lwhmg9epB_nPDBfTZieqHydY1GQbDMXKEqAs9wNC0o9OZeWDiy6a5QH9gxnp9FzmsdvsmALB6oUrfS0Lbw1IQfUMVv5cTln1GTqS0YLfRHO3Krh41Z5yHr-0bsA1ViCIZvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
دانلود سرور داخلی
https://uplod.ir/9iei532m163a/WHD-B3.zip.htm
https://dl.toolschi.com/view.php?f=5bc735f5b4753205.zip
رمز فایل 3666
در این نسخه تغییرات زیادی روی ظاهر، پایداری و مدیریت کانفیگ انجام شده:
✅
طراحی اپلیکیشن کامل بازطراحی شده و حالا ظاهر جدید، ساده‌تر، مرتب‌تر و دارک دارد
✅
دارک مود و رنگ‌بندی جدید برای خوانایی بهتر اضافه شده
✅
امکان ساخت چند پروفایل کانکشن اضافه شده
✅
امکان ساخت چند پروفایل ریزالور اضافه شده
✅
انتخاب پروفایل کانکشن و پروفایل ریزالور ساده‌تر شده
✅
لاگ‌ها جدا شدند و حالا خواناتر نمایش داده می‌شوند
✅
امکان کپی و خروجی گرفتن از لاگ‌ها اضافه شده تا اگر مشکلی داشتید راحت‌تر برای ما ارسال کنید
✅
دکمه Reset to Default برای برگرداندن تنظیمات پیشرفته به حالت پیش‌فرض اضافه شده
✅
تنظیمات اضافه و گیج‌کننده تا حد ممکن مرتب و حذف شدند
✅
دسترسی Battery Optimization اضافه شده تا اتصال در پس‌زمینه پایدارتر بماند
✅
باگ کرش کردن اپلیکیشن بعد از Disconnect مخصوصا در حالت Full VPN برطرف شده
✅
نسخه جدید بهینه‌تر شده و لاگ‌ها فقط آخرین موارد مهم را نگه می‌دارند تا روی عملکرد اپلیکیشن فشار نیاورد
✅
حالت Proxy Mode به عنوان گزینه پیش‌فرض قرار داده شده چون عملکرد بهتر و پایدارتری دارد
پیشنهاد ما این است که اگر امکانش را دارید از Proxy Mode استفاده کنید. حالت Full VPN هنوز برای تست وجود دارد، اما چون کل ترافیک دستگاه را از تونل عبور می‌دهد ممکن است سرعت و پایداری پایین‌تری داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
لینک کانال:
https://t.me/whitedns
#WhiteDNS</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/whitedns/395" target="_blank">📅 09:31 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-394">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0PCa8_CRwmCM-AJFuZKkMFJFxGG7j4P8ZQD_fLLVWd5yA1vjF_0Ot03ADN29l6oYPZLObeND9gccbUmHns7IC7Uplo8J31fdXBWFI_URYZ7TytHNtZgDS2ObHf7GMC_kemsUMCPfCKP5xLZ0PbrnBeEoNCScXyX9Vu0bqj8oA5Qmp0i-vUBQYSLMw5ClWAyKKn8dAMM8QIgGGwJ8HiqWZGFnJaens5_v0YhXWw0Pz4yVM5RQ6KhNK28Gp7282tNFBUnV6-AtRzIdZN0wLbXo3_Oks4WZZZwVxd7y1khG3iw_8vaBKEeVu5_5UFzLIn3oLXpMOzZweEet0oAcfe-Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ سرور اختصاصی وایت دی‌ان‌اس برای StormDNS
domain:
v.whitedns1.shop
EncryptionKey:
c8328f9d541860df1637b9b3ed7b990e
domain:
v.whitedns2.shop
EncryptionKey:
7ecd7b6271c47e348f6ab177517ee8fa
domain:
v.whitedns3.shop
EncryptionKey:
9d7aedcaf1f94e784a24fdfc1348a337
domain:
v.whitedns4.shop
EncryptionKey:
0ce14ab71acebbd46b8129e25593155a
domain:
v.whitedns5.shop
EncryptionKey:
2dffd162cb02b278c1ab57ee17fe07ae
domain:
v.whitedns6.shop
EncryptionKey:
e32afdaa30ca36ead696cd90d84ced15
domain:
v.whitedns7.shop
EncryptionKey:
6394eec942238533798ec7524eb7ea66
domain:
v.whitedns8.shop
EncryptionKey:
1c167e9850936655c480e4938b2c5c35
آموزش اتصال با پی‌سی
https://t.me/whitedns/383
همچنین میتونید از اپلیکیشن WhiteDNS استفاده کنید تا وصل بشید.
@whiteDNS</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/whitedns/394" target="_blank">📅 16:50 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-393">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">WhiteDNS-Beta2.apk</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/whitedns/393" target="_blank">📅 16:21 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta2.apk</div>
  <div class="tg-doc-extra">22 MB</div>
</div>
<a href="https://t.me/whitedns/392" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
ممنون از همه کسانی که نسخه تست WhiteDNS رو نصب کردند، تست گرفتند و با فیدبک‌هاشون کمک کردند باگ‌ها رو سریع‌تر پیدا و رفع کنیم.
دانلود سرور داخلی
https://kalbodteam.ir/free/file/Z0YF19
https://dl.toolschi.com/view.php?f=21c0a01f957ec510.zip
در نسخه جدید
1.0.0-beta2
چند تغییر مهم اعمال شده:
✅
تست کانکشن بعد از اتصال حذف شد.
توجه کنید ممکنه اتصال برقرار بشه، اما به‌خاطر MTU نامناسب یا Resolver ضعیف، سرعت خیلی پایین باشه یا بعضی سایت‌ها لود نشن.
✅
گزینه Load Default Resolver حذف شد.
این روش بیشتر از اینکه کمک‌کننده باشه، باعث فشار اضافی روی سرور و اختلال در تست‌ها می‌شد.
✅
امکان استفاده از سرور شخصی StormDNS اضافه شد.
از بخش Advanced Settings می‌تونید دامنه، کلید و تنظیمات سرور StormDNS خودتون رو وارد کنید و از کلاینت برای سرورهای شخصی هم استفاده کنید.
✅
مشکل قطع نشدن VPN سیستم برطرف شد.
وقتی داخل اپلیکیشن Disconnect می‌زنید، VPN اندروید هم به‌درستی قطع میشه.
⚠️
این نسخه همچنان نسخه تست اولیه است. هیچ اصراری برای استفاده از این روش وجود نداره؛ فقط اگر تمایل دارید، می‌تونید با تست کردن و ارسال فیدبک به بهتر شدن پروژه کمک کنید.
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/whitedns/392" target="_blank">📅 16:00 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-391">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هرکسی وصل شد لطفا خبر بده. نتیجه این تست خیلی برای ما مهم هستن.
اگر هم نشد، پایین اپلیکیشن ثسمت لاگ هستش. میتونید کپی کنید و برای ما بفرستید.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/391" target="_blank">📅 14:05 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-390">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS.apk</div>
  <div class="tg-doc-extra">22.1 MB</div>
</div>
<a href="https://t.me/whitedns/390" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخه تست همگانی کلاینت VPN وایت‌دی‌ان‌اس منتشر شد
🔽
لینک دانلود سرور داخلی  https://uplod.ir/i7zea22zumur/WhiteDNS.zip.htm https://uploadb.com/pykmzh0af81s/File.zip.html   در این نسخه از WhiteDNS، هسته ارتباطی روی StormDNS ساخته شده و ما تا جای ممکن آن را…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/whitedns/390" target="_blank">📅 13:55 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-389">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovXDeDnOq-_Uk1RXbmAKRakUq4V8sm0-D9R80YFzCZTLwJZyqJfKr0gB5ZksJcTC7m4jJqJZ9ld-sWYaPSa-dr2B7VUY9CO-Yq5ps1hJ0yIa1HGeHhhV9wjfAaqLNR10pca5In9Aqs_1zmbr7E6fC7XRyfLdgItDE5AymHuS3973fP-0bML6rVc5XabaTYut69A3IRAZ-XKbzkpQi-I0k7dPXkjuM1j8h3x_iRHZSkjsE8VxIJqEwh1RLVOflnUUEmltIpGSbAcNJJuMZNu8h_Pat0SvldLBzEEBTNafD22rEKff5ywW29ryagg0V_ztFdEDx7VHgtKCSwcAIEaegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه تست همگانی کلاینت VPN وایت‌دی‌ان‌اس منتشر شد
🔽
لینک دانلود سرور داخلی
https://uplod.ir/i7zea22zumur/WhiteDNS.zip.htm
https://uploadb.com/pykmzh0af81s/File.zip.html
در این نسخه از WhiteDNS، هسته ارتباطی روی StormDNS ساخته شده و ما تا جای ممکن آن را برای شبکه‌های محدود، ناپایدار و پر اختلال بهینه کرده‌ایم.
برای اتصال، نیازی به وارد کردن سرور، کلید یا تنظیمات پیچیده ندارید. فقط کافی است Resolverهای خودتان را وارد کنید یا از لیست آماده داخل برنامه استفاده کنید. اپلیکیشن Resolverها را تست می‌کند، مسیرهای سالم را پیدا می‌کند و سپس به صورت خودکار اتصال را برقرار می‌کند.
قابلیت‌های فعلی:
✅
اتصال Full System VPN برای کل گوشی
✅
حالت Proxy Only برای استفاده دستی
✅
استفاده از چندین سرور داخلی WhiteDNS
✅
تست خودکار Resolverها قبل از اتصال
✅
امکان استفاده از لیست آماده Resolverها
✅
تنظیمات پیشرفته MTU برای شبکه‌های سخت‌تر
✅
نمایش سرعت دانلود، آپلود و مصرف کل دیتا
✅
لاگ اتصال برای بررسی خطاها و وضعیت کانکشن
✅
بدون نیاز به وارد کردن کلید یا دامنه توسط کاربر
اگر روی اینترنت شما اتصال سخت برقرار می‌شود، می‌توانید مقادیر MTU را تغییر دهید تا مسیرهای بیشتری شناسایی شوند و اتصال پایدارتر شود.
⚠️
این اپلیکیشن هنوز نسخه تست اولیه است.
ممکن است روی بعضی دستگاه‌ها یا بعضی اپراتورها نیاز به تنظیمات بیشتر داشته باشد.
لطفاً تست کنید و نتیجه، خطاها و پیشنهادهای خودتان را برای ما بفرستید تا نسخه‌های بعدی سریع‌تر و پایدارتر شوند.
Powered by WhiteDNS
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/whitedns/389" target="_blank">📅 13:53 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🍷
وب‌سایت فیلم و سریال Azfilm رایگان و بدون سانسور:
13,755 عنوان فیلم و سریال
⚡️
🌎
https://azfilm.theazizi.ir
💡
دریافت نرم‌افزار ها و ابزار های پیشنهادی برای دانلود و پخش:
🌎
https://azfcdn.theazizi.ir
@xsfilterrnet
👑
@luluch_code</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/whitedns/388" target="_blank">📅 03:50 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-387">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آموزش راه اندازی Storm DNS روی ترموکس
لینک مستقیم دانلود ترموکس:
«‏Termux» در مایکت:
https://myket.ir/app/com.termux
لینک مستقیم دانلود Stormrdns termux:
https://kalbodteam.ir/free/file/fN6tLa
https://uplod.ir/ihpkp15d5att/StormDNS_Client_Termux_ARM64.zip.htm
لینک فقط ۳روز اعتبار داره وقتی تموم بشه تمدیدش میکنم
(توجه داشته باشید که فایل استورم با پوشه  از زیپ خارج کنید و در پوشه دانلود قرار بدید)
بعد از وارد کردن هر دستور دبر ترموکس نیاز هست اینتر بزنید و اگر بعد اینتر زدن Y ,N دیدید حتما y بزنید
حالا میریم برای دستورات ترموکس:
1 :
termux-setup-storage
y  بعد enter
2 :
cp /storage/emulated/0/Download/StormDNS_Client_Termux_ARM64.zip $HOME
3.2 :
cp /storage/emulated/0/Download/StormDNS_Client_Termux_ARM64/StormDNS_Client_Termux_ARM64_v2026.04.26.153956-15aedd9 $HOME
3.3 :
cp /storage/emulated/0/Download/StormDNS_Client_Termux_ARM64/client_config.toml $HOME
3.4 :
cp /storage/emulated/0/Download/StormDNS_Client_Termux_ARM64/client_resolvers.txt $HOME
4 :
cp StormDNS_Client_Termux_ARM64_v2026.04.26.153956-15aedd9 Storm
5 :
chmod +x Storm
6 :
./Storm
و تمام منتظر بشید اسکن تموم بشه و رو پروکسی
127.0.0.1
با پورت 18000 وصل شید
نکته :
۱ - برای جایگزینی Domains  و Key دستور
nano client_config.toml
رو اجرا کنید بعد از جایگذاری کلید کنترل x را بزنید سپس y و اینتر
۲ - برای جایگزاری resolvers اگر خواستید اضافه کنید اون هم از nano استفاده میشه مثل فایل قبلی ولی اگر خواستید کامل عوض کنید و resolver های قبلی رو پاک کنید از این دستور استفاده کنید
rm client_resolvers.txt
برای کپی فایل جدید تو تلگرام فایلی ک دانلود کردید رو بزنید با ترموکس باز بشه ، حالا اون فایل تو پوشه دانلودتون رفته
1 - cd downloads
2 - cp client_resolvers.txt $HOME
یه cd بزنید میاین صفحه home و اجرای دستور ک Stormdns اجرا بشه با دستور :
./Storm
یا میتونید فایل تلگرامی رو ذخیره کنید بره دانلودتون و با این دستور مستقیم کپی بشه تو home
cp "/storage/emulated/0/Download/client_config.toml" ~/</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/387" target="_blank">📅 23:31 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-386">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/386" target="_blank">📅 23:01 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-385">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua56tZ3jV2PXpVaBGXh13_KJpC9jajhV7z7tBeVC2otjjF75a9LA-sc32cZpn-kLSVeAuRtKOHl28-G0VZnqLKjGDOsiuUgQ9zwNHswFWq-EUui-3TQuaBevFoT0PUOZiFzSqcJ8YogLsCeSWNmsZao3XfRQGLN0ZX-BHJAKtg0ampYsY3n0QHAro2m_7PphD6V5sQzaqnnCRZnOm6f1o8jsied9tnrf4RdjZYmvHtQMmqO7b-bjUUDOFDWW_g0Vs1kucvN0mFMAZR3bwxq_WJDG05p0Sutl8d5TBZnWCfEn1ylubWSbC5wzEvkZUfe-SVCIc53I7RDY0FEwbnmemQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اتصال راحت به Storm DNS میتونید از اپلیکیشن MDV-HN روی گوشی اندروید
🌿
خودتون استفاده کنید
🔗
دانلود از سرور داخلی
https://uplod.ir/remiindapsge/masterdnsvpn-HN-1.2.2-universal-release.zip.htm
😀
https://github.com/Hidden-Node/MasterDnsVPN-AndroidClient
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/385" target="_blank">📅 22:52 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-383">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
#آموزش
اتصال
#StormDNS
🤩
🪟
ویندوز
1️⃣
فایل کانفیگ را باز کنید:
client_config.toml
2️⃣
این موارد را تنظیم کنید:
ENCRYPTION_KEY = "YOUR_KEY"
DOMAINS = ["v.example.com"]
3️⃣
فایل resolver را تنظیم کنید:
client_resolvers.txt
8.8.8.8
1.1.1.1:53
4️⃣
برنامه را اجرا کنید:
StormDNS_Client_Windows_AMD64.exe
5️⃣
پراکسی برنامه‌ها را روی این مقدار بگذارید:
127.0.0.1:18000
🤩
🐧
لینوکس
1️⃣
فایل را استخراج کنید:
unzip StormDNS_Client_Linux_AMD64.zip
cd StormDNS_Client_Linux_AMD64
chmod +x StormDNS_Client_Linux_AMD64
2️⃣
کانفیگ را باز کنید:
nano client_config.toml
3️⃣
این موارد را تنظیم کنید:
ENCRYPTION_KEY = "YOUR_KEY"
DOMAINS = ["v.example.com"]
4️⃣
resolverها را وارد کنید:
nano client_resolvers.txt
5️⃣
اجرا کنید:
./StormDNS_Client_Linux_AMD64
6️⃣
پراکسی برنامه‌ها را روی این مقدار بگذارید:
127.0.0.1:18000
🤩
🍎
مک
1️⃣
نسخه مناسب را دانلود کنید:
•
ARM64
برای مک‌های جدید M1 / M2 / M3 / M4
•
AMD64
برای مک‌های Intel
2️⃣
کانفیگ را باز کنید:
nano client_config.toml
3️⃣
این موارد را تنظیم کنید:
ENCRYPTION_KEY = "YOUR_KEY"
DOMAINS = ["v.example.com"]
4️⃣
فایل را قابل اجرا کنید و اجرا بگیرید:
chmod +x StormDNS_Client_MacOS_ARM64
./StormDNS_Client_MacOS_ARM64
5️⃣
پراکسی برنامه‌ها را روی این مقدار بگذارید:
127.0.0.1:1080
🤩
⚠️
نکات مهم
• دامنه باید دقیقاً با رکورد
NS
یکی باشد
• مقدار
ENCRYPTION_KEY
باید دقیقاً با سرور یکی باشد
• بدون
resolver
سالم اتصال برقرار نمی‌شود
• دامنه کوتاه‌تر معمولاً سرعت و MTU بهتری می‌دهد
🤩
🔥
اگر وصل نشد، این موارد را چک کنید:
• resolverها خراب یا ناسازگار هستند
• DNS هنوز کامل propagate نشده
• کلید اشتباه وارد شده
• مقدار MTU بیش از حد بالاست
@WhiteDNS</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/383" target="_blank">📅 22:43 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">StormDNS_Client_Termux_ARM64.zip</div>
  <div class="tg-doc-extra">3.4 MB</div>
</div>
<a href="https://t.me/whitedns/376" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
سرور اختصاصی StormDNS چنل WhiteDNS
Public Key
9cfaa88a49698c09b1a37f756dbbf1a7
Domain
v.whitedns.shop
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/376" target="_blank">📅 22:33 · 12 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
