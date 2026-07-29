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
<img src="https://cdn4.telesco.pe/file/dabobywK6JZYNhfYNRlQ1cviccLjfC2NQVQQOaI0Z4NZWE7DuWQ4Lq4_oFXEvycRg02-3T2k1yxuqI0UprOLScTa-W6MHS5mcpVmGP9yZW8H3zv2LmV4ChmbPGUeBY47vDwVJfEEmeAKAOjRAq1dOQR-ZQlhdZWQ6jz3rCdZrGAauob5MIcdz6u59dOBfNsGCUNZRSPoHKbrJ3iZToo1nAfISH4ESIttcPyNXh5A8XSFlwFpfUAN5tz4JcdZSs54-jh4AAnuhWpglwVzlqDX5uKMO-lQcsWALvwwMlIWvpPuvxksyJ4hd_7cjL-KZbd4yUizdS-NoBstsTmvmWczpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.17M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 21:31:29</div>
<hr>

<div class="tg-post" id="msg-676459">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
منابع عربی: نیروهای رژیم صهیونیستی درحال پیش‌روی به سمت دره الرقاد در خاک سوریه هستند؛ همزمان توپخانه این رژیم حملاتی به حومه غربی درعا دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/676459" target="_blank">📅 21:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676458">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
خروج ۲.۲ همتی پول حقیقی از بورس؛ مقصد پول‌ها کجاست؟
🔹
بازار سهام امروز شاهد خروج ۲.۲ همت سرمایه حقیقی بود؛ در حالی که ارزش معاملات خرد به ۲۷ همت رسید. همزمان ۱۹۲ میلیارد تومان سرمایه از صندوق‌های طلا خارج شد و صندوق‌های درآمد ثابت با ورود ۱.۱ همت پول، مقصد اصلی نقدینگی بودند. در پایان معاملات نیز ۵۳ درصد نمادها سبزپوش و ۴۷ درصد منفی بسته شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/676458" target="_blank">📅 21:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676457">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYxR4sbb8pqG1rAH7NCk-IlXJLXYJ5ZI2YBVhNEpZDr6KxEAKx7Ofxu-YKEFn9dPbNRaXJuQ8UMuSzFcnbneTvOjpwtXDD-z5NIkPY8HCthux-3WhrLnb50YEZD6bh78fbrifgC5rDXSjSLjAAY60Ftl9NhwuUyGu_r05o-Naco3cY-ZxPvaRyK7SlFZ-5Esc13AoXT8eQVE0fOYbKTUr_UkSPIUmmP-HXLXhGn9NvXGd6vEfQ9cP_ma8WbuFELpXZ16pXcBcHwqTQRH4B1mYS2_9GOidHKgpBLrpa2-bsnozh9cltyNDu20mNG7Cwe_sKmQg6OOdbCTT5DVzXjo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش تند سفارت ایران در غنا به توییت ترامپ: شجاعت جان می‌بخشد، ریاست‌جمهوری آمریکا جان می‌گیرد!
🔹
سگ زرد در توییت خود از قصدش برای اهدای «نشان عالی افتخار غیرنظامی» به جوانی که جان یک کودک را در دریا نجات داده بود، خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/676457" target="_blank">📅 21:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676456">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
معاون امنیتی وزیر کشور: امنیت کامل در مرزهای شلمچه و چذابه برقرار است
🔹
خوشبختانه امسال تغییرات محسوس و قابل توجهی را در توسعه مسیرهای مرزی، خصوصاً در سمت کشور عراق شاهد هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/676456" target="_blank">📅 21:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676454">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/676454" target="_blank">📅 21:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676453">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6baeacb7c.mp4?token=X_5f0qQVvxWcVklMPpBmxSlP167K3BMtJJDuXo17J8F-HhfURNDtOjktEZNv-G2eDKWimcX30nsSxRJ22Gc6qjI2Hx4NJnFF-_0yL4dq2jnG1dX9Z1uAYkt5OJKV2j8OQhkPLUyCfe5IX3zKEzJQL04SDK55_zFUKY2TMkwgYgTBJR2cXg2rYYPDkRA02phDbR0g4fZLGvRTapTRLqyF30dzGLGZtJ7ySf5iFCPMBGkKzGOemmC9IweSflPLmqBlA-or-J34TnDGt9to_32BKmPNofbg85l8zGhMaW-3r0OalvLuK6Bwa4yv1Zf-ifQfyr-lYDgONqaw49cChuZZSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6baeacb7c.mp4?token=X_5f0qQVvxWcVklMPpBmxSlP167K3BMtJJDuXo17J8F-HhfURNDtOjktEZNv-G2eDKWimcX30nsSxRJ22Gc6qjI2Hx4NJnFF-_0yL4dq2jnG1dX9Z1uAYkt5OJKV2j8OQhkPLUyCfe5IX3zKEzJQL04SDK55_zFUKY2TMkwgYgTBJR2cXg2rYYPDkRA02phDbR0g4fZLGvRTapTRLqyF30dzGLGZtJ7ySf5iFCPMBGkKzGOemmC9IweSflPLmqBlA-or-J34TnDGt9to_32BKmPNofbg85l8zGhMaW-3r0OalvLuK6Bwa4yv1Zf-ifQfyr-lYDgONqaw49cChuZZSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
پیام‌های صوتی شما در پویش «همه باهم برای ایران» جلوه‌ای از همدلی، مسئولیت‌پذیری و عشق به میهن است؛ روایت‌هایی کوتاه اما پرمعنا از شهرها و لهجه‌های گوناگون ایران که یک پیام مشترک را فریاد می‌زنند: ایران، خانه مشترک همه ماست.
🔹
این صداهای صمیمی نشان می‌دهد که مردم ایران، فارغ از تفاوت‌های قومی و زبانی، در روزهای سخت کنار یکدیگر می‌ایستند
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
#همه_باهم_برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/676453" target="_blank">📅 21:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676452">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud-0QSac3H5BFTBG2ddG8jkVSaZsmQzQghJ3-l4ZziMVnPr6agvIHn2uDfbJtlWwXCZK-phxj7pr9Vi08D1mpjRH-q5iDb926sOm4DlfXvCOIMjlymBSO54rQipmRTM05a74g5S78FM4rtpolXtneYEDAlnt3gn33R5gJWZsYOlsVNq8lDr8MqQw85dzi9iS_Bf_SWxSM23AJQt4I7URYdtAd0xY9Nfxo-ogC3C61YkiJkSSqA4UI1sVK59TGpViWlFe_HhQdiXeFRWyPwiqYppq2kwAd5f2Nuc2OwMpVPMUGUTQiFMMRpRQkIVRSNSIaG86_ItTNuDVLdvgK0VENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع پیکرهای مطهر پنج شهید ایرانی که در حمله شب گذشته آمریکا و عربستان به شهادت رسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/676452" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676451">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe57d58a3.mp4?token=vAa9s1uKpBYzHcwu4sI9xXs5Y0jOXzmoCXlzB_jaTd-RJRql3SWnnMes-QDtpd-YxOFCW-NHb8v3G87UjO1n3n6uSTlVnOYxXUHd9zvJb37T0UgEIlJcBrZVaDAmyt8TcUN_A4t6iaD_XvJ8OwSFS-99fPUkexsX_ZuuQdcuifUw90himxWa6DooVA0rOe-nGKtNJ1GJm2dAdZJgGn6g9xj5DoXHdHovqiPyiEZtVGFUHMQe7g5k9pjApfIdeRXUirfGP_JTOl8dLbR_HrcmQ_HAjAjGwrMvHgGUJrDB2VBF7mLqfahBp01s0ZHeOcjSipe-xKwvVZfNLMcs1aLOAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe57d58a3.mp4?token=vAa9s1uKpBYzHcwu4sI9xXs5Y0jOXzmoCXlzB_jaTd-RJRql3SWnnMes-QDtpd-YxOFCW-NHb8v3G87UjO1n3n6uSTlVnOYxXUHd9zvJb37T0UgEIlJcBrZVaDAmyt8TcUN_A4t6iaD_XvJ8OwSFS-99fPUkexsX_ZuuQdcuifUw90himxWa6DooVA0rOe-nGKtNJ1GJm2dAdZJgGn6g9xj5DoXHdHovqiPyiEZtVGFUHMQe7g5k9pjApfIdeRXUirfGP_JTOl8dLbR_HrcmQ_HAjAjGwrMvHgGUJrDB2VBF7mLqfahBp01s0ZHeOcjSipe-xKwvVZfNLMcs1aLOAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم یورش وحشیانه اشغالگران صهیونیستی به جنوب نابلس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/676451" target="_blank">📅 21:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676450">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112ce0f51e.mp4?token=FBUp-nsdyWosGpa5uI035l8k2o7d-GCpl2t3s3C_HPDxHT2f1aNyLdvBXd0_-VCIOSGrqWHP2fzRJrF67pHUE4oAZsvv7TR1xa8TEr6m61IUKtogqpnd07SUYGl1wkW9ZUeRPHOTso76QHJAWYPJ-bWbJJkzMWkmpjdr7F9T4uXRDtB3l6bmF8ikSRQPGsin8JY4MYRJtl6939pVbKEhxqWfdIvKC8URTqLbSDEQ8fOrekoq_wy9uvzEyMECoIHdQIlGq-nZsx9UiHzaXQx6b7_Kue4fwNObTGIIyK9yqNPdvrfPLZUq4VuTqNVqS3kc3htLJJkdwMeSrZwpdT784CG-xgo1z_bUMy4K4Zdxt1j6tM8-1YyIyIvPXrU2iPb-ukGSeQrgWysMlsYryVppL6KwXkA6R4suctJf8aimttlVTiKD89M0QTvjgaApxsV6x8p4ToGXVn8LWgn53enjNXSLVxtOOSZrBYAslwPWjav-92nS28Kt3KZarVwoofI1u7wbdhEOYZm_4iqaYh_sITMMY-Fz-9ObEDb5DWEaBXtn4euF1PEhNAiuZXDDjbhEQwsA04GY6YawRYfPsdwYuENElzwF_ogwYmwZ-RS68senuNslV-e7hkvO5NRqJ4_DOmZm7B2NMRanlRM9tsdq56NyNG9q-Qj-3kjqtmI-Fok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112ce0f51e.mp4?token=FBUp-nsdyWosGpa5uI035l8k2o7d-GCpl2t3s3C_HPDxHT2f1aNyLdvBXd0_-VCIOSGrqWHP2fzRJrF67pHUE4oAZsvv7TR1xa8TEr6m61IUKtogqpnd07SUYGl1wkW9ZUeRPHOTso76QHJAWYPJ-bWbJJkzMWkmpjdr7F9T4uXRDtB3l6bmF8ikSRQPGsin8JY4MYRJtl6939pVbKEhxqWfdIvKC8URTqLbSDEQ8fOrekoq_wy9uvzEyMECoIHdQIlGq-nZsx9UiHzaXQx6b7_Kue4fwNObTGIIyK9yqNPdvrfPLZUq4VuTqNVqS3kc3htLJJkdwMeSrZwpdT784CG-xgo1z_bUMy4K4Zdxt1j6tM8-1YyIyIvPXrU2iPb-ukGSeQrgWysMlsYryVppL6KwXkA6R4suctJf8aimttlVTiKD89M0QTvjgaApxsV6x8p4ToGXVn8LWgn53enjNXSLVxtOOSZrBYAslwPWjav-92nS28Kt3KZarVwoofI1u7wbdhEOYZm_4iqaYh_sITMMY-Fz-9ObEDb5DWEaBXtn4euF1PEhNAiuZXDDjbhEQwsA04GY6YawRYfPsdwYuENElzwF_ogwYmwZ-RS68senuNslV-e7hkvO5NRqJ4_DOmZm7B2NMRanlRM9tsdq56NyNG9q-Qj-3kjqtmI-Fok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات ضرباتِ ویرانگر ایران بر پایگاه دشمن آمریکایی در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/676450" target="_blank">📅 21:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676449">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
آلمان: ما مسئولیت ویژه‌ای نسبت به اسرائیل داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/676449" target="_blank">📅 21:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676448">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e12a6efbc.mp4?token=dVHc0paLSfeW2Vti_M-BJFZt_jGAq8A2vyMKVAzveH5DWSkWVZHTpf16cKbKcvxgMYPM7l8zqDpj84_OSKozfvtM9Hag8oK3UawvXO2wKqyEdrmps6asB0EFIAcKz1Pz8lDs3rWPLhbWJQm6qmLarW3ZLC4FQxr70S_I4yVNa3ZxlLkOhLrG9evgbTBDJJsl7aJ34wJdQ8-hP_3N-xF_acXM18xfHLIvILJjMEvhJln7yxQ5Mdb-ltg1zitazOg24RezvLdM_bazaeRLukNEl41Cy341hUNM5ole65qpykiim1pqu4p8OV8BlvhTiNNweUOz4GDlBOLpbRXoAWCr5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e12a6efbc.mp4?token=dVHc0paLSfeW2Vti_M-BJFZt_jGAq8A2vyMKVAzveH5DWSkWVZHTpf16cKbKcvxgMYPM7l8zqDpj84_OSKozfvtM9Hag8oK3UawvXO2wKqyEdrmps6asB0EFIAcKz1Pz8lDs3rWPLhbWJQm6qmLarW3ZLC4FQxr70S_I4yVNa3ZxlLkOhLrG9evgbTBDJJsl7aJ34wJdQ8-hP_3N-xF_acXM18xfHLIvILJjMEvhJln7yxQ5Mdb-ltg1zitazOg24RezvLdM_bazaeRLukNEl41Cy341hUNM5ole65qpykiim1pqu4p8OV8BlvhTiNNweUOz4GDlBOLpbRXoAWCr5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک
سنجاب مسابقه بیسبال را به هم ریخت
🔹
این سنجاب از اواخر اینینگ ششم وارد زمین شد و با فرارهای پیاپی، بیش از ۱۰ نفر از عوامل اجرایی ورزشگاه را برای دقایقی سرگردان کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/676448" target="_blank">📅 21:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676447">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02937f3d0b.mp4?token=N1Ps4DAAnFwoipMUc2SQ6M8-EUUjy3eCpCGw8DPmKthScKEg-hHaSBIdTW3UC1TPdmymB1NipHdveQvy_agW58UXOkSKqiHzvHVjzdVBLlE0JPUUABYgnCwmZweK_dpzO71iOms2_8i--raeUwwMduK_MDRMS9RCsNGVmsRgGMK_POSsL1L7MLrLf7Qz6tOjo993mj9yJACgl_4RLlyerYn5r4Q90mk8DFxzNjYApA9aqQs6KSe9XgeFR6wSPXeG7tOOMP7fkI9YNVmKXgQ9ZbPuomdRCSacMaJkiBiKsDl6VKooYjMup1oF1cT5oxOA32y3GjDLTBdMJgb8_6zD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02937f3d0b.mp4?token=N1Ps4DAAnFwoipMUc2SQ6M8-EUUjy3eCpCGw8DPmKthScKEg-hHaSBIdTW3UC1TPdmymB1NipHdveQvy_agW58UXOkSKqiHzvHVjzdVBLlE0JPUUABYgnCwmZweK_dpzO71iOms2_8i--raeUwwMduK_MDRMS9RCsNGVmsRgGMK_POSsL1L7MLrLf7Qz6tOjo993mj9yJACgl_4RLlyerYn5r4Q90mk8DFxzNjYApA9aqQs6KSe9XgeFR6wSPXeG7tOOMP7fkI9YNVmKXgQ9ZbPuomdRCSacMaJkiBiKsDl6VKooYjMup1oF1cT5oxOA32y3GjDLTBdMJgb8_6zD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مازیار لرستانی در مراسم بزرگداشت اکبر عبدی: اکبر عبدی نه‌فقط نابغه کمدی، اسطوره‌ای بود سرشار از صفا و مردمی‌بودن، تکرارشدنی نیست/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/676447" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676446">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
باراک راوید، خبرنگار آکسیوس: جی‌دی‌ونس روز سه‌شنبه و وزیر جنگ آمریکا امروز با نتانیاهو دیدار کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/676446" target="_blank">📅 21:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676445">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جنگ خودروسازان با توسعه مناطق آزاد یک اشتباه استراتژیک است/ اصلاح تعرفه و رفع موانع تولید باید همزمان انجام شود
مهدی دادفر، دبیر انجمن واردکنندگان خودرو در
#گفتگو
با خبرفوری:
🔹
تعرفه‌گذاری فعلی، غیرمنطقی و غیرعلمی است و باید به نفع مردم اصلاح شود؛ چه جایی بهتر از منطقه آزاد؟
🔹
سیاست‌های گذشته شاید زمانی با هدف حمایت از صنعت خودروسازی توجیه‌پذیر بود، اما امروز دیگر پاسخگوی رضایت مردم نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/676445" target="_blank">📅 20:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676444">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9NbBg71IKP2lNulGprtS3jeUBnJ5aCBPY2tDX6AVxycPTbsFUwhDcrSnGVXv3XppHHtdu5ZOEfzdNTyjR2pD3Bi9h3CfoTdwsQJr9Chkz2M_U7ud6NIOEQ7zo2uZ-NAWbTp_8FDD5d_h3fLR2O3ue-KJiwKtNS6tJ_BTXQBX8mJUH8q1ImfegUHq2dNyPbvnHSbNKk_VwwDQEf4N148msfQroOI0pxAtWDq3hf1NUvzH1GXSzC-WB61NoNFIAGlt4q4PLICVlUUs3soWZyg4E1gWmWBSrpvv9uyGFC2WUboKejPHkURfazGgEiSEq-3tckrwsXY2TFBF_jjPco_ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«
نقش پنهان رژیم صهیونیستی» در حملات آمریکایی سعودی به عراق در اثر جدید کمال شرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/676444" target="_blank">📅 20:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676443">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
قطر ضمن اظهار نگرانی، حملات ایران به اردن را محکوم کرد./الجزیره
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/676443" target="_blank">📅 20:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676442">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6fbe63ae.mp4?token=fOmAWtIy4ZAqBjFcFXpStLXYhbM7Ob8vTdHdhlFpF4dvyFLR03xqRy2kPA5851WB2R2umtTdhA9bnfPsQPLcQMZs2DeIBr1OcyuKSZORSkVG00oOjeXO85iV_QIr6JSMY_FgdEBju1do_4IQpMo8qtcs5Mrl-llaTt2CrtB757OSmXYAg8NZVidAGikcxFFShetxoH5EVW2mj2EPUTMHXJFDQGI0Q_XPjSy2LDSF2XcGdi-BmIBaShbtzQvGvSRLHcVwr0bbGa0_25Gid4G3mjqiafN7DEt80k8YtEmPQ64NaUHcDh6q6A73x8zl5O4cEQHhNXePiF_dLkQptMou8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6fbe63ae.mp4?token=fOmAWtIy4ZAqBjFcFXpStLXYhbM7Ob8vTdHdhlFpF4dvyFLR03xqRy2kPA5851WB2R2umtTdhA9bnfPsQPLcQMZs2DeIBr1OcyuKSZORSkVG00oOjeXO85iV_QIr6JSMY_FgdEBju1do_4IQpMo8qtcs5Mrl-llaTt2CrtB757OSmXYAg8NZVidAGikcxFFShetxoH5EVW2mj2EPUTMHXJFDQGI0Q_XPjSy2LDSF2XcGdi-BmIBaShbtzQvGvSRLHcVwr0bbGa0_25Gid4G3mjqiafN7DEt80k8YtEmPQ64NaUHcDh6q6A73x8zl5O4cEQHhNXePiF_dLkQptMou8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم منتشر شده از دفتر لیندسی گراهام در روز حمله به ایران #Trash
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/676442" target="_blank">📅 20:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676441">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9TFNrJkhkOBWM-kuy_Yn9IlhBWpowItiAHOJwUJIhZShgImVTVVcM3I7W0wtQ8SaxOwr3e0cSECd8gR9xkyyAFeH8e6SB5wSqOC0lE8hm1os9AkAMf8-HkmxcrEz_H_BYXd8Eb3s9iLa_wablcYb5Yh0dM-joz-f9imXpQFr8bLs9inQrq6XmLrN96pJgCij1G64ZihBsWFK5eHuK-tIKqnZq7PsNBm_NTmtAaFV18KGdvhQQnxn3iEOdhWh61mdkMT6nuRP-J5lkNuokSMuGPPx0eKypFVcxryIbMAjPHOHNpugztn8L3BWQqEniQeTYvDuervQBEzZJadJ7F5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفند خطرناک زلنسکی برای ادغام جنگ‌های ایران و اوکراین
پایگاه خبری Responsible Statecraft:
🔹
شواهد زیادی نشان می‌دهد که زلنسکی به‌ دنبال پیوند دادن جنگ اوکراین با درگیری آمریکا و ایران در یک صحنه استراتژیک واحد است.
🔹
در صورت تحقق این سناریو، اوکراین از دریافت‌کننده کمک نظامی آمریکا به مشارکت‌کننده مستقیم در تقابل واشینگتن با تهران تبدیل می‌شود و آمریکا نیز از تأمین‌کننده تسلیحات اوکراین، به طرفی فعال در جنگ با روسیه بدل خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/676441" target="_blank">📅 20:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676440">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f4bfa8755.mp4?token=sEUqHvMDD5EgF2Zzg_rTt4hNHaWwRxVGO_NMzfOhBfQgDh8MgbwDt8L75LrsV8RfH6vJANsmcrWhckNzLFVQXfLkqLgcwDXnIjcgoNhy2tykmtaN5vEvdQEE9tBVnyjvIPtadVnS1tWZQzL4ypp31V90OUCqYlwsQPoH2_8_HSpLLkuFNP6LvbgssH3qq3SFS8JcZye3YDSe5C4TY2OvihTO4ToK4Ygu3UPzIskEgzRASJIvdAP8ayUVi3znnnWUSMtLX8LRSwOG9VVIKyMzZsYe6gD-UqKYrJ6ICXNCinHKv8q3Zei-0ClHaJw87t4nsuwUyABPmiXaXju-a0n_jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f4bfa8755.mp4?token=sEUqHvMDD5EgF2Zzg_rTt4hNHaWwRxVGO_NMzfOhBfQgDh8MgbwDt8L75LrsV8RfH6vJANsmcrWhckNzLFVQXfLkqLgcwDXnIjcgoNhy2tykmtaN5vEvdQEE9tBVnyjvIPtadVnS1tWZQzL4ypp31V90OUCqYlwsQPoH2_8_HSpLLkuFNP6LvbgssH3qq3SFS8JcZye3YDSe5C4TY2OvihTO4ToK4Ygu3UPzIskEgzRASJIvdAP8ayUVi3znnnWUSMtLX8LRSwOG9VVIKyMzZsYe6gD-UqKYrJ6ICXNCinHKv8q3Zei-0ClHaJw87t4nsuwUyABPmiXaXju-a0n_jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله توپخانه‌ای اسرائیل به خاک سوریه
🔹
منابع سوری از حمله توپخانه‌ای ارتش رژیم صهیونیستی به اطراف شهرک عابدین در منطقه حوض الیرموک در حومه استان درعا خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/676440" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676439">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
اعتراف شیطان زرد به نامحبوب بودن جنگش علیه ایران
🔹
برایان کیلمید، مجری شبکه فاکس‌نیوز که با دونالد ترامپ گفت‌وگو کرده گفته که رئیس‌جمهور آمریکا به او گفته می‌داند که جنگ علیه ایران در کشورش «چندان محبوب» نیست.
🔹
کیلمید می‌گوید در جریان مسابقات جام جهانی فوتبال با دونالد ترامپ تلفنی صحبت کرده و جنگ علیه ایران از جمله موضوعات گفت‌وگوی میان دو طرف بوده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/676439" target="_blank">📅 20:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676438">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
روایتی تکان‌دهنده از برزخ؛ از راز رزق تا شفاعت حضرت زهرا(س)
🔹
00:02:00 اهمیت و جایگاه والای "محبت" به هر جاندار و بی‌جانی
🔹
00:06:10 حمایت بانوی دوعالم از هرکسی که محبت ایشان در دلش باشد
🔹
00:10:00 بازیگری در فیلم نامه‌ای که خودمان نوشته‌ایم
🔹
00:18:10 سبک شمردن نماز ، روزی دنیایی و مسیرهای برزخی را محدود می‌کند
🔹
00:22:30 وظیفه اصلی هر انسان چیست؟
🔹
00:30:10 سیاهی قلب‌های ناامید، حتی در هنگام خواندن نماز و دعا
🔹
00:39:30 به حرمت کار خیر مادر همسرم؛ مرا شفا دادن
🔹
00:58:50 معجزه‌ای که برای من اتفاق افتاد
🔹
قسمت پانزدهم (مهر و امید)، فصل پنجم
🔹
#تجربه‌گر
: حسین صاحبی بزاز
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/676438" target="_blank">📅 20:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676437">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
فرمانده کل ارتش: تا آخرین قطره خون از خاک پاک ایران دفاع می‌کنیم
سرلشکر حاتمی در پیامی به‌مناسبت شهادت امیر سرتیپ دوم خلبان کاظمی:
🔹
شهید کاظمی و همرزمانش قهرمانان حقیقی ملت ایران هستند.
🔹
آسمان ایران، میدان رشادت مردانی است که جان خویش را سپر ملت کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/676437" target="_blank">📅 20:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676436">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c101f5d684.mp4?token=onzlnTFGcfHVXRvwRhiva7FAiu41XhfoYarwQPNWdt_KyuPwFWLTqxb76U_TiSw4WWDPwu9x3UxvudoiLSA9L-nOp_zeVXlgZirrN0VYIlLcAaMWqzWBLd7NX0VHgNWfCM-QLz6jMEZD18WuTa52614rIsGQN81YMiMcveN1zrkTytC_NHhir7FnIB2NTZQqmOm3WkIE9hvfaKy3hlZ46CIt_nXdsuOh5nMqdXtMldqtC1M6UZhlGmnR4oK3d5dZV88XpCC_tgrWycF8sUvE-G4tlYpj_UfKH8gVkkjOGa8rEGukAUQwAJZW7XDtccAOsQ3R554FgjfijPTJAo5m0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c101f5d684.mp4?token=onzlnTFGcfHVXRvwRhiva7FAiu41XhfoYarwQPNWdt_KyuPwFWLTqxb76U_TiSw4WWDPwu9x3UxvudoiLSA9L-nOp_zeVXlgZirrN0VYIlLcAaMWqzWBLd7NX0VHgNWfCM-QLz6jMEZD18WuTa52614rIsGQN81YMiMcveN1zrkTytC_NHhir7FnIB2NTZQqmOm3WkIE9hvfaKy3hlZ46CIt_nXdsuOh5nMqdXtMldqtC1M6UZhlGmnR4oK3d5dZV88XpCC_tgrWycF8sUvE-G4tlYpj_UfKH8gVkkjOGa8rEGukAUQwAJZW7XDtccAOsQ3R554FgjfijPTJAo5m0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیگر از تشییع با‌شکوه زائران و رزمندگان شهید حشد شعبی در عراق
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/676436" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676435">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
یمن درحال بررسی دریافت عوارض از کشتی‌های عبوری باب‌المندب
🔹
رویترز به‌نقل از منابع آگاه مدعی شد یمن درحال بررسی طرحی برای دریافت عوارض از کشتی‌های تجاری عبوری از تنگه باب‌المندب و جنوب دریای سرخ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/676435" target="_blank">📅 20:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676434">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3CY3f1VwH6km3UsO1vnrL91G9wsJNDBNB2koARCpVZc0Ooh6ioGeCKtqtp2mmYa6GZmqAvBjipsuDBvjcqqkcT9BeitFdcyVa6V-p3B-CQFIpn8ByWNJo15a1jRn9SpgK7azQsn0CBVoYWZfNFCdCMOgeZ2hWbGjNhER70VUehLJF7Ex1gCcEhtF21Xw4682V6_nBUiNwb7xCfSJaJtljNHeJerdZONIplj5E1MhsRZF5MPHau_lCuAy807rK-06_NXaq3EM0GV_tDjQxlHmJN3W6ijJpafaD5aVBHgsExePpwd4BGUh94HeGXI43kojmDRfYOgDTd-iRJsoDXZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیدگاه افکار عمومی، آینده جهان با چه مخاطراتی روبه‌رو است؟
🔸
در این نظرسنجی بیش از ۲۷ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۵ درصد، بله ۲۷ درصد و تلگرام ۱۸ درصد بوده است.
🔸
بیش از نیمی از شرکت‌کنندگان، بزرگ‌ترین خطر آینده جهان را جنگ‌های فراگیر و گسترده و حدود ۲۰ درصد نیز نابرابری‌های اجتماعی دانسته‌اند.
🔸
روندهای جهانی نشان می‌دهد ریسک‌های ژئوپلیتیکی و اجتماعی به مهم‌ترین چالش‌های پیش‌روی جهان تبدیل شده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/676434" target="_blank">📅 20:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676433">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
جدید‌ترین تصاویر از حمله به بندر دمیاط در مصر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/676433" target="_blank">📅 20:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676432">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWi9elQeh8mG45onVhALFqX7YHNoG-QokEQhYPHNfx_Hr3xLdMM1H9Kw4Lkh230-ihh4cBVeAF6P3Z1EZcaGyEA4sudkKBJce9l66VH7cK6qQCgqk-ls7mqZk7tcbNoyzTjmIxxlkCcucj_RJHkODWy6YTsSWcT41--TxJuFxFodh--toHATC6i1TWhsRa3FWB9-I1RockaBFSBKmQZaTiIDFt7qIobwcpn9VJGLfHVsWO5Ed04lUjPR-fdDdeofJPZszgZDJAiDfaH72UFvBRjzKwYI4dZ5dnkvqH4dHrovxeJGS3Ui8BTfeyR60c2K5qHiShxBzVsZT681iyVIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: تجاوز به تمامیت ارضی عراق مصداق آشکار ماهیت شرارت و برهم زدن نظم منطقه ای است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/676432" target="_blank">📅 20:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676431">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3a1eecbda.mp4?token=Wg5NzptfZzTOU6r-RHt94HV5jQNJSU-BEde5WAkNf8f0AZg94JXA3OVCy_pB953cw66KaFJEJ14sQWplq8yolwV5S8cv7fZpvZtU3SDrq3vrRcWpAwx6Q_SrrU_VFzfwCNmwP4j-tz9gMTrQs_gKO9LZtw5T5UaGJJPv_O7VY2JSD-Egjux4MNCGszVX9I_Kqwl7m-xt6_56rdQlnMyyPp4_bYzkSihUMXh3HGMv7JyZ9YcAlQOW1-fMEaRnuVaVANPgb3EralOGfHALuBhozZrdxYlfRxHC8YTlZXRPfmAp55aDbDxJrYq-LoA65zj-qzTJ2GL96IaX9qRilYyvrKd1bqSQhRZeAR1WbI03V2es7GoICV-RsroctfwKn6hm7_K_JSUWjjNoF_fEGnT0NLmoQy2vrHZ8bf4PRBzMman7hRxWLYiDQPicteMD8ts_hQ-ZiyIxkO1kbkeSCdQRM4MxW2vmw90TvOjlkJvO-zxzKFsiu5Z7l82-WBEKE6lWvfp67qsGzTXC48TJNnZBiydEoeraJ3nul9Q7mYgLroeTrAvnoBtm3AtjS-wpT-qKqb2iyDEmfFOuFeElMg_wIICuvKmk0JFGCgNGb35Hs7guhybHgy0SneViJ2dMktwWlv9uFhe6kemHFu6B0siv5seIUmcXSQPowkMrOtW6SOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3a1eecbda.mp4?token=Wg5NzptfZzTOU6r-RHt94HV5jQNJSU-BEde5WAkNf8f0AZg94JXA3OVCy_pB953cw66KaFJEJ14sQWplq8yolwV5S8cv7fZpvZtU3SDrq3vrRcWpAwx6Q_SrrU_VFzfwCNmwP4j-tz9gMTrQs_gKO9LZtw5T5UaGJJPv_O7VY2JSD-Egjux4MNCGszVX9I_Kqwl7m-xt6_56rdQlnMyyPp4_bYzkSihUMXh3HGMv7JyZ9YcAlQOW1-fMEaRnuVaVANPgb3EralOGfHALuBhozZrdxYlfRxHC8YTlZXRPfmAp55aDbDxJrYq-LoA65zj-qzTJ2GL96IaX9qRilYyvrKd1bqSQhRZeAR1WbI03V2es7GoICV-RsroctfwKn6hm7_K_JSUWjjNoF_fEGnT0NLmoQy2vrHZ8bf4PRBzMman7hRxWLYiDQPicteMD8ts_hQ-ZiyIxkO1kbkeSCdQRM4MxW2vmw90TvOjlkJvO-zxzKFsiu5Z7l82-WBEKE6lWvfp67qsGzTXC48TJNnZBiydEoeraJ3nul9Q7mYgLroeTrAvnoBtm3AtjS-wpT-qKqb2iyDEmfFOuFeElMg_wIICuvKmk0JFGCgNGb35Hs7guhybHgy0SneViJ2dMktwWlv9uFhe6kemHFu6B0siv5seIUmcXSQPowkMrOtW6SOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندر احوالات اختلالات بانکی؛ کی بود؟ چی بود؟ چی شد؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/676431" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676430">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
تجربه واقعی تزریق زیکورپا؛ از زبان یکی از مصرف‌کنندگان
شنیدن تجربه واقعی درمان چاقی با
آمپول لاغری زیکورپا(داروسازی دکتر عبیدی)
، دید بهتری نسبت به روند درمان به شما می‌دهد.
یکی از مراجعه‌کنندگان
کلینیک آئورا
در این ویدیو از تجربه خود، میزان کاهش وزن و رضایتش از روند درمان می‌گوید.
🎬
ویدیو را ببینید و تجربه او را از زبان خودش بشنوید.
☝️
برای شروع درمان چاقی با زیکورپا، از مشاوره رایگان پزشکان کلینیک آئورا استفاده کنید.
👨‍⚕️
رزرو مشاوره رایگان
کلینیک آئورا (جردن|سعادت‌آباد)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/676430" target="_blank">📅 20:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676429">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6730bf1abc.mp4?token=DTGVR8AtA15TyNy5rvSG3VVx3DDAqkyxd2WYfm8lkksMjbwTMJfGtkL3vuRH2oPk3RCBuoh1PC2aKoGBkV_t4A6biCLSmtHqZ4hrsPGj7vjjJguAZTiG9h3dFx3rEmx1c5-xhMYkeOcBAVl3eIh1zwS1Cpvt9rfd-RLETRBMhmTzoRlHSuMXsaCfyEBk0bC_g1vaErQzHQCshxuyvu9sMdjKat-71eSo5kxSjpvWpcxMI8KtVpeCb2dYoSIHA3ydlroZi3_WwZqZezRgoTQCoyFOc14La9ir1KLIMVfhzjaIfK0D7On7UztdYQMsRAdxbgFU3MWikT3FqciJaF0c2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6730bf1abc.mp4?token=DTGVR8AtA15TyNy5rvSG3VVx3DDAqkyxd2WYfm8lkksMjbwTMJfGtkL3vuRH2oPk3RCBuoh1PC2aKoGBkV_t4A6biCLSmtHqZ4hrsPGj7vjjJguAZTiG9h3dFx3rEmx1c5-xhMYkeOcBAVl3eIh1zwS1Cpvt9rfd-RLETRBMhmTzoRlHSuMXsaCfyEBk0bC_g1vaErQzHQCshxuyvu9sMdjKat-71eSo5kxSjpvWpcxMI8KtVpeCb2dYoSIHA3ydlroZi3_WwZqZezRgoTQCoyFOc14La9ir1KLIMVfhzjaIfK0D7On7UztdYQMsRAdxbgFU3MWikT3FqciJaF0c2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احتمال اصابت پهپاد به تأسیسات ذخیره‌سازی گاز در بندر دمیاط  سی‌جی‌تی‌ان:
🔹
یک تأسیسات شناور ذخیره‌سازی گاز مایع با مالکیت و بهره‌برداری آمریکا و با پرچم جزایر مارشال، دست‌کم هدف یک پهپاد قرار گرفته است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/676429" target="_blank">📅 19:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676428">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57d7228a9.mp4?token=HFiiPNZUhf81MFAethJRgC7A9tdPUpDzxNpMhrimmcaz2FO0XShPlAPj_VFAql2nPmzyHgVxtBzzGfVQ5WLqP1FLj5w0LKCeTG3UNQCBwN6D-jN4QwN8w0jU7dL2AlnMTo0V8Ke1AMc7wOMWdYH9VcDMTmTqMGjtLGCWYQc__7zUHOUysmU9h_x7cgTxqt1V6CDoUq8gSv6aXuSQZw9eYlM9asEMbMnjzHgQe6UT5ndnW9zIeSzwbLNP893g7VIwrV_2QdbREvvlBhCIDYdjbNtOsU-gpdgmXDIFvieZ7h4Ut3h2yzC9O4fDgwQQD9DAHwIhs2c1oBV55bNju3FE8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57d7228a9.mp4?token=HFiiPNZUhf81MFAethJRgC7A9tdPUpDzxNpMhrimmcaz2FO0XShPlAPj_VFAql2nPmzyHgVxtBzzGfVQ5WLqP1FLj5w0LKCeTG3UNQCBwN6D-jN4QwN8w0jU7dL2AlnMTo0V8Ke1AMc7wOMWdYH9VcDMTmTqMGjtLGCWYQc__7zUHOUysmU9h_x7cgTxqt1V6CDoUq8gSv6aXuSQZw9eYlM9asEMbMnjzHgQe6UT5ndnW9zIeSzwbLNP893g7VIwrV_2QdbREvvlBhCIDYdjbNtOsU-gpdgmXDIFvieZ7h4Ut3h2yzC9O4fDgwQQD9DAHwIhs2c1oBV55bNju3FE8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد مشترک آزادگان ایرانی و عراقی در طریق نجف-کربلا: ترامپ را بکشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/676428" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676427">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-B8voRgvqBD8wEZK8P7xR-tYCPmydocW4ov1RAmf5uD04M2Vjn9llX9uTBVal4HNF7I9_Nk6J3_3YpuHn4DfOMGKyu-kuBDl-y9-YLdfUKFmBmZDAJ5fPDGdUfOP2hMq4eO5zuxeey2JuxLeWwrlSFmUzeNlLvMZWL-uWNhRj607qMU3FAAXnN2rIT6dNewzWEyKHM8M06wvh5EBI_Xp2-MStbRZCHQ358N1_shEAw1yl_pk68dmQDnXl5knE4IOau_mLTwxhd7xkxmUKZvm6U0kGm4-eYwMlNnhBbNpqmqTckoVMvrRAigMNG0T4xzQQw7X7bYyXJAkETKhNtrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
مسیر عاشقی پر از فرصت‌های ناب است.
▫️
فرصتی برای اینکه برای چند دقیقه هم که شده، بار خستگی را از روی دوش یک خانواده برداریم. با همین توان کم، میزبانی کنیم.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/676427" target="_blank">📅 19:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676426">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ورود ربات‌های چینی به آمریکا ممنوع شد
🔹
کمیسیون ارتباطات فدرال آمریکا (FCC) اعلام کرد ربات‌های پیشرفته تولید شده در کشورهای خارجی می‌توانند برای آمریکا آسیب‌پذیری‌هایی در زنجیره تامین و همچنین خطرات سایبری و امنیت ملی ایجاد کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/676426" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37de8e66d6.mp4?token=EapXWZE3ymSwjvO1QqsQ76-PoP33CnqwXcN4d-LupKMyTjljUYelhFtUd22D0aFE3IzGrjpLuJUnrBivvuds5l9j4lisAoVWvVOCFTexCj31BXhc11V3CyIcpySxr_ZXgMjBogdFQizN3Dv4SQaadceO_64dudvidctlAawdI0GU2WuyrvtOF5MVlehToRFLD_NFX_kO9fm4CY8crKbMmyQqxuYUUJ6Gxs8UncKRjuSaRMd050bDtoOLk1z1Dd19Hy-6mTFKtlqzSsMVNvFWZwL1AMs4_BZ_Gs1ypVnL-ZINIAPAWKe767ZrAKSZs1ZkQEZOF-5yHQqLWAyatHqeFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37de8e66d6.mp4?token=EapXWZE3ymSwjvO1QqsQ76-PoP33CnqwXcN4d-LupKMyTjljUYelhFtUd22D0aFE3IzGrjpLuJUnrBivvuds5l9j4lisAoVWvVOCFTexCj31BXhc11V3CyIcpySxr_ZXgMjBogdFQizN3Dv4SQaadceO_64dudvidctlAawdI0GU2WuyrvtOF5MVlehToRFLD_NFX_kO9fm4CY8crKbMmyQqxuYUUJ6Gxs8UncKRjuSaRMd050bDtoOLk1z1Dd19Hy-6mTFKtlqzSsMVNvFWZwL1AMs4_BZ_Gs1ypVnL-ZINIAPAWKe767ZrAKSZs1ZkQEZOF-5yHQqLWAyatHqeFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مازیار لرستانی در مراسم بزرگداشت اکبر عبدی: اکبر عبدی نه‌فقط نابغه کمدی، اسطوره‌ای بود سرشار از صفا و مردمی‌بودن، تکرارشدنی نیست
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/676425" target="_blank">📅 19:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676424">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7033b797.mp4?token=ewfTyHTsLDPCABDD313K08xleG-OWkb0My7-DHvVVZvtPiSNLh8acLDs7K3cF6Ryv-J2G4ImI5yCzYWe70-G2IyxrK7hHltfYhEtOi5EQmYsflzqAhkOdmia8s8nnGula_DyA0IDTAB1lL7ZlQU5ttx8UG1b4pY7cnX30LlLgh8yGgEOjnHQ-1fKq-reA1srNSFUwHTM1wLNsvzyY-8YZcsV6RIMukK7Ns_lZeLzR5rtnliwIAMmE8w7gqkj7Vf3YblK8AW1wrDVnG6ZvZZQsg9NK2cQagDyWJKgKFkmh42SzMRZdjJOXvmz6MevpGj7qGKsgejrj2e4VbOUSNEdp5GpgAFNlhayFj29W8WSXcG0pXE9xNw2Y9lbVT-R5UMMWMyHC-tandEIrwTX0HF17HDKa81GKAeBbc7a656YbaRjj19_sKZP9BHJERxCO_hMUaS0UjFRBWMZMh_5xuinAa8hK_9ncBDjKW8cMvuQdJKv2YTjI1ETENb9bzVdtZionsl0dsDMFQGZPQHjN_UtfLVUEYRFuzHkLnsNfXOk2Eg0YuJj7fgny_z5kI-9r7HjmRutetJX2BRnqxd-rQWWC6NIiavIZBQtkVZoiQfd5Bp4or8_krV5VYtxl1vKnUP6WvA16AdMniS0pnCZWJdF0DLXguEPFKR4Ab3XQkgJ3t4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7033b797.mp4?token=ewfTyHTsLDPCABDD313K08xleG-OWkb0My7-DHvVVZvtPiSNLh8acLDs7K3cF6Ryv-J2G4ImI5yCzYWe70-G2IyxrK7hHltfYhEtOi5EQmYsflzqAhkOdmia8s8nnGula_DyA0IDTAB1lL7ZlQU5ttx8UG1b4pY7cnX30LlLgh8yGgEOjnHQ-1fKq-reA1srNSFUwHTM1wLNsvzyY-8YZcsV6RIMukK7Ns_lZeLzR5rtnliwIAMmE8w7gqkj7Vf3YblK8AW1wrDVnG6ZvZZQsg9NK2cQagDyWJKgKFkmh42SzMRZdjJOXvmz6MevpGj7qGKsgejrj2e4VbOUSNEdp5GpgAFNlhayFj29W8WSXcG0pXE9xNw2Y9lbVT-R5UMMWMyHC-tandEIrwTX0HF17HDKa81GKAeBbc7a656YbaRjj19_sKZP9BHJERxCO_hMUaS0UjFRBWMZMh_5xuinAa8hK_9ncBDjKW8cMvuQdJKv2YTjI1ETENb9bzVdtZionsl0dsDMFQGZPQHjN_UtfLVUEYRFuzHkLnsNfXOk2Eg0YuJj7fgny_z5kI-9r7HjmRutetJX2BRnqxd-rQWWC6NIiavIZBQtkVZoiQfd5Bp4or8_krV5VYtxl1vKnUP6WvA16AdMniS0pnCZWJdF0DLXguEPFKR4Ab3XQkgJ3t4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج پر دردسر علی دایی در بزرگداشت اکبر عبدی با هجوم مردم
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/676424" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnLM5UNjIr77rbweJtd8fb8vYQgFiVo0Yt6bw89v0ga3E2zYVs_OCB2jyMLqQRT3CfTse-DlIbPPqKQE2s_SheixnS1rzJPMb083ypL8QOBiV92eNMiTN9MWdxPe4S2aIdifWKLDakfdPSV7vL8jUEc9Z4LR7iZtYLFja1lYyHz1O6MnD648WQ3fo1qBCXbbCPNksHxClEKc2zwpj8o2F-j_YoQVo8XeERYM3mkpjvxX-2YmlneTmDho8CBuLwTm5Ah9KXIZO4aEBT23hWwtr_Bvb3MCDYPCz2jNDhfRciBlydW-HkPaLWftbHyBFbZaFuTiPMBn21TTatYK7G4rtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلاکت عامل تروریستی در بوکان
نیروی زمینی سپاه:
🔹
عامل تروریستی وابسته به گروهک‌های تجزیه‌طلب که به منظور اقدامات ضدامنیتی در شهرستان بوکان حضور یافته بود پس از درگیری مسلّحانه با رزمندگان قرارگاه حمزه سیدالشهدا(ع) به هلاکت رسید.
🔹
از این عامل تروریستی ۲ اسلحه کلاشینکف، ۶ خشاب و یک  موتورسیکلت کشف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/676423" target="_blank">📅 19:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
احتمال اصابت پهپاد به تأسیسات ذخیره‌سازی گاز در بندر دمیاط  سی‌جی‌تی‌ان:
🔹
یک تأسیسات شناور ذخیره‌سازی گاز مایع با مالکیت و بهره‌برداری آمریکا و با پرچم جزایر مارشال، دست‌کم هدف یک پهپاد قرار گرفته است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/676422" target="_blank">📅 19:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
بازداشت سرباز ارتش اسرائیل به اتهام جاسوسی برای ایران
🔹
یک شهروند اسرائیلی که پیش‌تر در یک یگان محرمانه ارتش اسرائیل خدمت کرده بود، به اتهام جاسوسی برای ایران بازداشت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/676421" target="_blank">📅 19:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676420">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c29d6742.mp4?token=sqX07ZHky0bfhJbBzUjvw7jHGW6tUxpd_-qkV7Rv8OX32mrqIYuSQ-vmZbamjPFvm3zlN4Jo9JbXD88pyHhtldwSD38yfjfMm_j8oF6BMqjmJoLWfVGgSp92q-JJAyv6kKmBKBk1gBane_tDrHO9-1bhB8uCdY7M0L6nDpID5HeWQKZ7gYWyvhimV3Jfgi02Kql9xDoaqCd0MVL70e5ICq0zNCmjiwPZmYJir4UnFuSf3IdZxrliTqzTwFmaQsWC0BQfdBjeNBeTWXq2foxjFx_NQ7wj8Uffuj1BZrDuTXmDiwxuS-2aU2pjR_5JspzAyn9RLPcKnHAKef2cmwhB1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c29d6742.mp4?token=sqX07ZHky0bfhJbBzUjvw7jHGW6tUxpd_-qkV7Rv8OX32mrqIYuSQ-vmZbamjPFvm3zlN4Jo9JbXD88pyHhtldwSD38yfjfMm_j8oF6BMqjmJoLWfVGgSp92q-JJAyv6kKmBKBk1gBane_tDrHO9-1bhB8uCdY7M0L6nDpID5HeWQKZ7gYWyvhimV3Jfgi02Kql9xDoaqCd0MVL70e5ICq0zNCmjiwPZmYJir4UnFuSf3IdZxrliTqzTwFmaQsWC0BQfdBjeNBeTWXq2foxjFx_NQ7wj8Uffuj1BZrDuTXmDiwxuS-2aU2pjR_5JspzAyn9RLPcKnHAKef2cmwhB1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در مصر
🔹
منابع خبری از وقوع انفجار هنگام تخلیه محموله گاز مایع در بندر دمیاط مصر خبر دادند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/676420" target="_blank">📅 19:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676419">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی عجیب؛ پزشکان ایرانی در حال مهاجرت به عراق هستند
رامین پولادرگ، رئیس اتاق بازرگانی ایران و عراق در
#گفتگو
با خبرفوری:
🔹
تجارت ما با عراق متوقف نشده است اما شرکت‌های عربی از ترس تحریم‌های آمریکا و اروپا نسبت به تجارت با ایران بی‌میل شده‌اند و هزینه تجارت ما با عراق به همین سبب پر هزینه‌تر شده است.
🔹
عراق در زمینه‌های ساختمانی و برق به ایران وابستگی دارد و ما نباید این بازار را به چین و ترکیه ببازیم. در زمینه توریسم سلامت هم ما هیچ اقدامی نکردیم و این بازار سلامت در دست دلال‌ها اداره می‌شد. اکنون پزشکان ایرانی در حال مهاجرت به عراق به خصوص اربیل هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/676419" target="_blank">📅 19:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676418">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
انفجار در مصر
🔹
منابع خبری از وقوع انفجار هنگام تخلیه محموله گاز مایع در بندر دمیاط مصر خبر دادند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/676418" target="_blank">📅 19:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676417">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f525e84e.mp4?token=JS2W6suz73glw7uKxyzvTHlFNDMzZ88jto5Rv6GfzJfbKGZDkx3ahXByow_YyWYYzsKmkJVlLOw7305mFgDR9CieuLr_OuX-tFTCXK0WNDuJQgKDff4Rv9BDVzEJS6a3r55Jin4DLW_1chhwfKZzXvIr0AxDVfemcjRE6Oj6V7arFuiOtFggBunmVo6JTiJyw8iiKn9WXtYTGeXfCbWUb6acIXZsxh2871N99pCQ4XmJY-SKZi9Ie5a05tsgByQBxW-ZQv9xaWEXXCI2Mj91ZsM8_EARFrv18HbGHc30_k1HfWMB-BLsSeiyzCF5oQZvHUzOZ6jeQx2upt0oHzi9NYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f525e84e.mp4?token=JS2W6suz73glw7uKxyzvTHlFNDMzZ88jto5Rv6GfzJfbKGZDkx3ahXByow_YyWYYzsKmkJVlLOw7305mFgDR9CieuLr_OuX-tFTCXK0WNDuJQgKDff4Rv9BDVzEJS6a3r55Jin4DLW_1chhwfKZzXvIr0AxDVfemcjRE6Oj6V7arFuiOtFggBunmVo6JTiJyw8iiKn9WXtYTGeXfCbWUb6acIXZsxh2871N99pCQ4XmJY-SKZi9Ie5a05tsgByQBxW-ZQv9xaWEXXCI2Mj91ZsM8_EARFrv18HbGHc30_k1HfWMB-BLsSeiyzCF5oQZvHUzOZ6jeQx2upt0oHzi9NYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره پرویز پرستویی از فیلم آدم برفی در مراسم بزرگداشت اکبر عبدی
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/676417" target="_blank">📅 19:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676416">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای انتقال سانتریفیوژ توسط ایران به کوه کلنگ
یک مقام صهیونیست:
🔹
ایران سانتریفیوژ به کوه کلنگ منتقل کرده اما ما از اینکه آنجا غنی‌سازی انجام می‌دهند یا نه آگاه نیستیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/676416" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676415">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c8063071.mp4?token=dqzNgkAZN9o2ICy3SsRxyzpQHiBLvbDo9dOayWv43rjBFjTafrR_ubWW6BBUbxNKbWploxuuZy9eOiiDfk0ZIKOV7n0xyW6Gvypl6WgL66WVzL4XPL5384iOF7-efY7NBsZI94tYIp-Jq67fqKN82wA0O2KCmHCONrQY7EEYOQ8-LoOxZhFZqPl2bxR0D4zEdp4bjDw0FNiMaq4vXd45m5Swg4JTyXxdanr_rM3ZoWs9dlKjixaLMaNnHB19LI5Cs1kl4i_7StzJ2BxLFixDx-YLyz7HDC5kCrqRkeGlHUG8gH0y8FQuQbkEjjw71Mcwy2pDrOh92VXqW-DUyrcfEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c8063071.mp4?token=dqzNgkAZN9o2ICy3SsRxyzpQHiBLvbDo9dOayWv43rjBFjTafrR_ubWW6BBUbxNKbWploxuuZy9eOiiDfk0ZIKOV7n0xyW6Gvypl6WgL66WVzL4XPL5384iOF7-efY7NBsZI94tYIp-Jq67fqKN82wA0O2KCmHCONrQY7EEYOQ8-LoOxZhFZqPl2bxR0D4zEdp4bjDw0FNiMaq4vXd45m5Swg4JTyXxdanr_rM3ZoWs9dlKjixaLMaNnHB19LI5Cs1kl4i_7StzJ2BxLFixDx-YLyz7HDC5kCrqRkeGlHUG8gH0y8FQuQbkEjjw71Mcwy2pDrOh92VXqW-DUyrcfEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود معترضان به هتل نتانیاهو در واشنگتن
🔹
گروهی از معترضان به نسل‌کشی اسرائیل در غزه وارد هتل محل اقامت نتانیاهو شدند و علیه او شعار دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/676415" target="_blank">📅 19:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676414">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33ccefbfe.mp4?token=mMf3odjeHUY_YuMrFJMkmj7uhxGXlBK_82QuhBmdlY-q724zhwx_WQ-s38MkpByvI4q_fAA6GlQWUBC7QXzonWfPtrW2qClMxkhmI97c-HDNrPYQj9uD3i92vzw70yueq2nMz4ErG-9EixmHJhQUmdhmKxrB3oLaMG66VKHSwsqMDJG6Y1bn6NCY95PV96x2KD48Mg3T2yd67eXnQbXBBNDwgEWeDMp4-vxwFd95iFCrvNFQf-uZ6GB3FZVO39B5BJtIQz4T9u6HezzL6MSprJmEqavH_9rOeICvtjiwF0mugKsH8IKWkKMZvx2FAFCd3KDM-u1YBwgKRNrG8deVeAzvWbPmMZPqiMJvtLAB_VuHKlL7iZIOXshoi5LibdR0eJJC1p9KQTO-7IJGb24em6rlS57PwOmTFUFJEkVI33bE8Jv6P6FEu5duRcHdIlWVEtsZ3WS1uZeseLDVm1W9jt8JntlrVb0PPl-wJMIVH4jmIE2f7es0QPMLdUFjDwx7u9Df5pP8UudCx45VHbJC0OJwOGrL712r7GJoQJh07Gc5Yr_0BRYoOZVLvPItTNgpecZWHiIFvvOc2lDCgc4vvcN4ujrgQsPOpiFdROKmaXcT58XkFllkmQRwJwG_dUUNaqyi2UjSWzXWjmtI4795RjtoI3hL9EoCo-rt4TacAt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33ccefbfe.mp4?token=mMf3odjeHUY_YuMrFJMkmj7uhxGXlBK_82QuhBmdlY-q724zhwx_WQ-s38MkpByvI4q_fAA6GlQWUBC7QXzonWfPtrW2qClMxkhmI97c-HDNrPYQj9uD3i92vzw70yueq2nMz4ErG-9EixmHJhQUmdhmKxrB3oLaMG66VKHSwsqMDJG6Y1bn6NCY95PV96x2KD48Mg3T2yd67eXnQbXBBNDwgEWeDMp4-vxwFd95iFCrvNFQf-uZ6GB3FZVO39B5BJtIQz4T9u6HezzL6MSprJmEqavH_9rOeICvtjiwF0mugKsH8IKWkKMZvx2FAFCd3KDM-u1YBwgKRNrG8deVeAzvWbPmMZPqiMJvtLAB_VuHKlL7iZIOXshoi5LibdR0eJJC1p9KQTO-7IJGb24em6rlS57PwOmTFUFJEkVI33bE8Jv6P6FEu5duRcHdIlWVEtsZ3WS1uZeseLDVm1W9jt8JntlrVb0PPl-wJMIVH4jmIE2f7es0QPMLdUFjDwx7u9Df5pP8UudCx45VHbJC0OJwOGrL712r7GJoQJh07Gc5Yr_0BRYoOZVLvPItTNgpecZWHiIFvvOc2lDCgc4vvcN4ujrgQsPOpiFdROKmaXcT58XkFllkmQRwJwG_dUUNaqyi2UjSWzXWjmtI4795RjtoI3hL9EoCo-rt4TacAt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین تصویر از پیکرهای مطهر شهدای ایرانی جنایت سعودی_آمریکایی در حملات به شهرهای عراق/ جماران
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/676414" target="_blank">📅 19:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676413">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbSePobNdh6aoaJrRE8tlft45o3AzAhKyS-ena7pXD8iaOPQ2lCH7QUU_4SXc5hDuPeV_jiCU-6xaaeCUmVLHi1IHJVHIlfpZQFjHETBr-kisLB6XsaSsc7n3RguIbEFs-tJJH22oXduGdFrO5DrKb50LiNElIs8sx36pLseCvt9keqsVXNu_3rq94rglNQUI32JZ68DT1fc6PsIgCB1uvttGHdMU7WXus-oOIat7jTh4jlI2sJNjnUix9y3Y9iRNv4BYuK-7T3GgyY6pCxPogLU2um_iqBd4Zc4c0IORS1n6BhAZGAoojcEDNVVfDtlVUAzFYoU6cIKlp0LgnzddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بختک؛ موجودی از جنس تاریکی که روی سینه‌ها سنگینی می‌کند
🔹
در فرهنگ عامه و باورهای کهن ایرانی، «بختک» موجودی نامرئی یا به شکل یک عجوزه‌ی زشت‌رو و کوتاه قد است که شب‌هنگام، زمانی که فرد در خواب عمیق است، ناگهان بر روی سینه او می‌نشیند. کسانی که بختک را تجربه…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/676413" target="_blank">📅 18:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676408">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVEwrE2QzCS6TmgArB8eLGySZCUjXUBPMfKrOyktlbltmGDU8NCuql0PzF9qs4nifRJR2YW4re_mwZRdgrUZeGBK1LKEh0UbCFJ7Xa66MgLZls9OxYosWldqEa7J2P0bHjtgNVn9XI6n5mG9uqlRr_V4iTsGSexcJPp4S2ZYl-TvMfsducU4oHQaOBZyaE6FvuDO-J-8t6FczbrKqAjiJe8BO46m-yw9vgATAd8G4kwmwg6_bwBQHdqDoW0yQ3qbYSE2w9jkLbrNj2R2tW90JKdpUkjFm3_m549uRYbnXOFz-sHix9lQtV5y_Ezi98-05KGLwXPpWJS5vrJaWK7AeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaIWXPzxyYTk26sangQT3yYSyqmxU0uhUHeUqkg-WGQMhrGaOfQbCww0NVnbJOu-E5CBAkxs5IRkdrgaGEwXeaRBFfEAjMuE4M_bivp8JZnjjHXi0od7WaM5anl4TeeEcGxtYdemG-sZ7VYB0au5VYGqttTXMbxrGHiwUIaEwwKdzFWL1ibIOG87zg3omQBcNlu5UTtbFzfoF4Gf7MYLX9MYGIO2WURGqKaZHnqvq6nx2l5NLVqgrrEYNfkYNDpDhIoNP5LkLhvPl3T-1ieCjDDUO9gUeegCGSnCmVFhWqSQWJZt29WlSkfxTvIvcks0I-n3nvR6LG9Z1-ssTD-8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSmeX_AGiO4vxxVg-oyu0OtilSL6T9U6Z3lnrCXbCaDsJDhcbmMgLCOG1vpnJnl46Jc6J1VRuAjr7eDjXmiCc4S5yeGvef8pj-ULezN7vjBiP9KpUpFzJdRXwEVE3_vi_fpz5G5Z81XajggpyIwENKadcWP8LNX6WG73kqqIOgu6LIrmkryBANtNZQws0Qw24v0TPIq9-tnEFhdFDIKA_QAbNTguW8q7HhhFzgj3fZIuAtF5PVSH6_15AdRqsk76x0TdVo77uZwSW1dFApbjkNQ-3f2R-pUz-_2CB9RlMdEy5WPmRq7RsUerAeRPmLi4KiCa5J3riTIvJPey6OwqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsoxOPZvvDXJBbK5emnLhH-nXf1N7qcHo_89DQSYin9pHbCj4oZXH7AkxmEhV-K0u90GBHeiI5auSCZRbu1LN9-D1wSZe3vvAZvcUW916UUIHa13JiOb7IDul7yWcGK4kjUpBcsOPm60iy05II_i-3j4K4n4WRY7xyHJKyR7VGGA2G0tEyOOVxSJ1btxJgr62t5vI-wZlab6rjAz2-H-k9UHoiI3fwJV5miPj6-gObjigidaWtsHz4WObVKGW0YDdDUF7PvSgzV1J0aYppezxErtIRKbGVpsgJtOXGmIEqrf2egyRtgEXTerHJ3_-RarY2bhCsCl1u64paOP151cyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jC62Ff72lthQQ696ZnAXK9AmGDL2UpWCEpclbfzRn5QwFiIobpsEb-mdN9iUcqHoF9gqtaClGhu7e6GujyvEtRyzOSeExKIt-JokOSnzxEI3VhwRh5z-QktzqgzKbZjhRyepJ4E_KPrFyZK5g7vz4OU4Y-k6a-hSeCwjayjynJUKvu-xJqDfGYz-XUzZPDZI2LGz-MnO1WIXmKxBtG3Y478ATe8aV5rIioiIgJwEc9zb2ofZwzEpQ6pQPjXdVKRJ0so_G619-68v5zp0-QuA2iPHBimGZkdIIBwgFRqlm-cWHwkl9MI61zk5A-NYpR39FPRE-qGbg2Oe896qfzWD6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اوکراین در تیررس موشک‌های ایران
🔹
اگر ایران بخواهد از خاک خود اوکراین را هدف بگیرد، کدام موشک‌ها به مقصد می‌رسند؟
🔹
در این اسلایدها با موشک‌های بالستیک ایران آشنا شوید که از نظر برد، توان رسیدن به اوکراین را دارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/676408" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676407">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
کاهش شتاب تورم در تیرماه
🔹
دکتر مهدی زاده مدیرکل سیاست های اقتصادی بانک مرکزی:تورم ۳.۶ درصدی در تیرماه در مقایسه با رقم ۷.۴ درصدی خرداد و ۸.۵ درصدی اردیبهشت حاکی از کاهش شتاب تورم است و به معنای کاهش سطح قیمت نیست.در واقع روند رشد شتابان قیمت ها نصف شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/676407" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676406">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
پول بازار دارو به جیب چه کسانی می‌رود؟
🔹
بر اساس داده‌های رسمی، برای ایجاد بازار ۴۰۰ هزار میلیارد تومانی (۴۰۰ همتی) دارو در سال ۱۴۰۴، حدود ۲۲۲ همت نهاده مصرف شده است.
🔹
بررسی‌ها نشان می‌دهد پس از کسر حاشیه سود ناخالص ۷۰ همتی داروخانه‌ها و ۳۰ همتی شرکت‌های پخش، تأمین‌کنندگان دارو در مجموع به ۷۶ همت سود عملیاتی دست یافته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/676406" target="_blank">📅 18:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676405">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQhrVfvZfqP_RZ9XCGU4MJRIbbYk5jJyShGkpNl4bFejei2i8yhoYHjiVTFROR--AVQ6B4iIh7-j4iWJ8_kqCpgzSbuLA6mw4hh1HWy3m4zX9sTHDZifdVCzCMNgk2hto3TaNglAdnXQvzMAHJniKqTxtzQo473FRlNDGKK_o0S5v1m0SKaaSoRsbjqaQ1qQOBJqehGilxOUKYNFcPpj_cndJ6QfRW0_RV0VzbNijFKiM4tgIedXC_BefE__KOV3c3Ln8O4VYCAoFIEM7bdLV1B5QmTow07xFeZTYK-P9-cscL-qYbzbHOl2YYg0kJaM10tar6YIQ4IhDfrvOW1TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
متقی‌نیا تشریح کرد:
تأمین مالی ۱۳۳ همتی در چهار ماهه نخست سال؛ رویکرد هدفمند بانک کشاورزی برای تضمین امنیت غذایی
🔻
مدیرعامل بانک کشاورزی با تشریح عملکرد این بانک در چهار ماهه نخست سال جاری، از اختصاص بیش از ۱۳۳ هزار میلیارد تومان حمایت مالی به زنجیره‌های تولید و صنایع غذایی خبر داد و این اقدام را گامی راهبردی برای پایداری امنیت غذایی و تقویت تولید ملی دانست.
🔻
وهب متقی‌نیا تأکید کرد: این حجم از منابع با رویکردی هدفمند و از طریق تلفیق تسهیلات نقدی با ابزارهای نوین تعهدی، جهت تأمین سرمایه در گردش و تکمیل طرح‌های فعال به تولیدکنندگان و بهره‌برداران اختصاص یافته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/676405" target="_blank">📅 18:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676402">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jv8KdtEaDXIRwVnhKb8m9pW84ZqM6HVMtvT-p6JrwChxY3WjcckOx-jGen3rAwKI5DvKETRQo7HSyWzbnQ5C7a11oKB8iR1UBaio-w0JyBORtY5jZbdmHMitEFRVSFBng2UOV4aC0Sg7H5sdATOQ6FyZ0vA4rdoXwlU0PLNFzo41kj4zpvvZ0rYNB-nufSkCXRNuH1oi51wlI6sCEMUOOw7_WaZGC__JU7N4ZAVzRw6R-wbIFIX6TRRfk5BM9N9UCLmemSCJzUfRLmHyZqc-UFXMBINI8-MJn7vJa2PKNSkV6ugknDA5LkPjpjQoRdw2LSrdzHSchFQz3YRuSs1d3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرب‌الاجل مقاومت عراق به دولت و تهدید به پاسخ نظامی علیه آمریکا و عربستان
🔹
مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.
🔹
برای حفظ امنیت زائران اربعین، پاسخ به آمریکا را به پس از مراسم موکول کرده اما تأکید می‌کند که این پاسخ قطعی خواهد بود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/676402" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676400">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3_xL6PGqP-GfildBOpBNnuZowYEnbWJKL4vBEITaTJqxTIURApZksz9OB93eM39039P_d907IL_t-45Jck4d69Sq1DZ4mKjVNeyliVEailcgoMwS-iCaRglEIK8u53CTLY38caE3KvpnMwk_mkJhfot7_lgaDZQnfOqv2CP_Vg6xO3ReW9PajYu7PURQUSNhy14FSm77WrzWYCFndbgUTsrMgCshoB95mVBwxR3yvqEFLRFc9z78CXgh-hhbcx2QM-yZCYtUZqLQzQG28BJQ90PNKR7TflLSGPKrpUFe-Oi1CXXFD-PG8_JzjyHQdRtTPq3x9AY54TV31hWzIkeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
مهمان حسینیم؛ میزبان مسیر...
▫️
خاطره آن ۱۵ دقیقه‌ای که برای زائران قدم برداشتید، برای ما بنویسید.
▫️
منتظر شنیدن روایت‌های شما از دل مسیر هستیم
👇🏻
@Ertebat_gharar</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/676400" target="_blank">📅 18:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676398">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQkbBHx7Ay_EkIiBlwxrnuZnZSLUJtCgI8eJfZzgtlBhKSVxw5KbysCzno2q9E_pvPF1kjsu1pve2Io603E8igPlajcUWd2sD_w879vf6yDXowZjRSqj0sbF_AM5yvN-xK62hK1pWBh5s1WVE3VyQmXWns_EC2UA41qbNkD6gg7Mj2vFURlJJclJ98GSIY8DOcqAVSzs_4jWzkCuYXJiSz4es-CqmydDfFa6peJEGosKhUp4C9n02SLAFxm9UfaDwJNk7uV3-25pSAa7Bn--WPxno72JsDoWiMmvVtLkuI-okjNBWKNOwEYO46_mblPhLVXLVuaAINj-sEEey31zlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت ۴ ایرانی در حمله مشترک عربستان سعودی و آمریکا به کربلای معلی
🔹
پاسدار شهید علی اصغر آستانه
🔹
پاسدار شهید ابوالفضل متقی
🔹
پاسدار شهید مرتضی اکبری
🔹
پاسدار شهید امیر عباس درهم فروش
🔹
هر چهار شهید اهل کاشان بودند. / صابرین نیوز
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/676398" target="_blank">📅 18:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676396">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پشت پرده تخریب پلیس امنیت اقتصادی توسط فیک‌نیوزها
🔹
در روزهای اخیر برخی رسانه‌ها و صفحات فیک که به دروغ پردازی معروف هستند، اقدام به انتشار مطالب کذب علیه برخی چهره‌های خدمت‌رسان در پلیس امنیت اقتصادی کرده‌اند.
🔹
اما اصل ماجرا این است که از چندماه قبل پلیس امنیت اقتصادی اقدام به برخورد و مواجهه با رسانه‌های فیک و باجگیر کرده‌اند و پرونده این افراد نیز در قوه قضائیه به صورت جدی در حال بررسی است.
🔹
همین مبارزه با فساد توسط عوامل پلیس امنیت اقتصادی موجب شده عوامل این رسانه‌ها که خطر بازداشت خود را لمس کرده‌اند، دست به تخریب برداشته و با دروغ اینگونه القا کنند که پلیس امنیت اقتصادی از آنها باجگیری کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/676396" target="_blank">📅 18:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676395">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Paz-yZqVXVSJpukYH7pOUgcEWXQcsAnPlLjDGMxwNFkNEhfnLXcAORrsQ0FMq_BmXTr7CjKNaPAJB_bMcOOEClgUgcYKLIvrkOfOccMkNuzQrHbvzT4nbMEwZEwo6axQXt3PyqITiR_G1_7UZvq4veZxDt2bNmQEMZ8KD4VW8wcZADxN-caUrgdqiEmeJqPrJ6qJ_DUNGHDwTYeCOKN1x9p4rmdpZ8H5Bqb45QDGs__SsjwUqYgB6cLmNyBg59gjM3QvkVlAjTrXZ5C7P60xlgdOo-eydG5_e8NGRWKjjvo-dliSfxFTj60APWiIt4VzVyzTotjLdeY40YpEAS5pQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیخ صفی‌الدین اردبیلی؛ نقطه اتصال عرفان و سیاست
🔹
شیخ صفی‌الدین اردبیلی عارفی بود که بی‌آنکه شمشیری به دست بگیرد، بنیان یکی از قدرتمندترین سلسله‌های ایران را گذاشت. کمتر کسی می‌داند دولت صفوی که ایران را دوباره یکپارچه کرد، ریشه در خانقاه آرام و مکتب معنوی…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/676395" target="_blank">📅 18:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676394">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7e19da75.mp4?token=nawyS4qno0iJaIRE8CAe8hnY4XXq_WRwnMNls0knWJkDllORolM6ULVeRaybzDhIGnF6ZcZPwLTpL43ZvLXY4h2vLhU7NllErOzv8hDhRNdXLtr-2MZOHUsK1cwlHjHMUr6Di79FrMHbKv64-UGj6KPpMupE6cZdhJ_Bkm0MsFD2pskS6CiqIHPfEq2VYTzQm6Dw9HPYDO8EsceoRMQQJ-1LvbJjIFE2jUyIukmKwk-Z1CuaGsjiTfcatAtuxc7mWVD54-Xcqk9BOWqph4Ap2JWlIoJ6UlGNDzMJ0ZvYqoBG5KQFCMLevOPQdRcIGwWqk8msGdNpm1luaW4P0LR-7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7e19da75.mp4?token=nawyS4qno0iJaIRE8CAe8hnY4XXq_WRwnMNls0knWJkDllORolM6ULVeRaybzDhIGnF6ZcZPwLTpL43ZvLXY4h2vLhU7NllErOzv8hDhRNdXLtr-2MZOHUsK1cwlHjHMUr6Di79FrMHbKv64-UGj6KPpMupE6cZdhJ_Bkm0MsFD2pskS6CiqIHPfEq2VYTzQm6Dw9HPYDO8EsceoRMQQJ-1LvbJjIFE2jUyIukmKwk-Z1CuaGsjiTfcatAtuxc7mWVD54-Xcqk9BOWqph4Ap2JWlIoJ6UlGNDzMJ0ZvYqoBG5KQFCMLevOPQdRcIGwWqk8msGdNpm1luaW4P0LR-7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهمانان شفاف ساحل قشم
🔹
ساحل دوطرفه قشم این روزها پر از عروس‌های دریایی شده؛ موجودات زیبایی که با جریان آب و باد به ساحل می‌رسند. تماشایشان لذت‌بخش است، اما لمسشان می‌تواند هم به شما آسیب بزند و هم به خودشان.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/676394" target="_blank">📅 18:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676391">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc1bd6606.mp4?token=U_Pv832wrvU5xd_I6eQAzv94xA7naJwD3N_1DGU22fzrjqbmsIY-e6p_IwyTLbSnFxngXsAvtH6CINVVk4BVmOQDe5IfFSM3rIYoZbCbGjedE1f5G-0RYCzp3wT68sxatw84HGO4oS76hTLbI8Q2yk1ib0lx7PuiqfXzcMTT5ASTOiZpxiFj6d_EzzUKf7qgYc2SGRVIpXkN_ca_3BxSNcuFm7tq23LddNBLoaS615NaOCKTJh-gxN85tUz3FTyXTqslkGGe4qJtYLkO7JJBUc5S0x1878CeCQ7vj-nyCm2InTq1Cw8HzpdsCaifhgL0U5O7zIcYxC8N8wUd4yd_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc1bd6606.mp4?token=U_Pv832wrvU5xd_I6eQAzv94xA7naJwD3N_1DGU22fzrjqbmsIY-e6p_IwyTLbSnFxngXsAvtH6CINVVk4BVmOQDe5IfFSM3rIYoZbCbGjedE1f5G-0RYCzp3wT68sxatw84HGO4oS76hTLbI8Q2yk1ib0lx7PuiqfXzcMTT5ASTOiZpxiFj6d_EzzUKf7qgYc2SGRVIpXkN_ca_3BxSNcuFm7tq23LddNBLoaS615NaOCKTJh-gxN85tUz3FTyXTqslkGGe4qJtYLkO7JJBUc5S0x1878CeCQ7vj-nyCm2InTq1Cw8HzpdsCaifhgL0U5O7zIcYxC8N8wUd4yd_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی چین از موشک بالستیک هایپرسونیک YJ-20
🔹
ارتش چین برای نخستین‌بار تصاویر شلیک موشک بالستیک هایپرسونیک ضدکشتی YJ-20 را از روی ناوشکن مجهز به موشک‌های هدایت‌شونده تیپ 052D منتشر کرد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان چینی دنبال کنید
👇
@AkhbareFori_CN</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/676391" target="_blank">📅 17:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e147683f.mp4?token=SPC25EncP-CkAs_eaElN9XFyugQOzT8qFLb6Sc3fYAtE9Zo05FgLeVp8gCNZnKTd1r4fJtp5ktWmnY2f2b5o95HeXVUBWPJHMCkss-soBiIXmtZoJZqBfJgYEfnCzQaCl2KvzQK8QTfyReiZIK7fGfvu4-gulWZl-Xoin9Cqpl90WChPRtrt8aFK7REuIcO0d-17iuePmctrqRlYrn7-F__ikrHmCTGTnMz_9Pfxbb8RZh4uapINOB0gBgtwWSMbPc4q4xMBJwRvUCdKHtv1H6iCWkw0Lz9JwQqrsqYtZmqR8SOGI3KI8kcaPeLksqKUuDDevFmBUnefc5hmD0MUMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e147683f.mp4?token=SPC25EncP-CkAs_eaElN9XFyugQOzT8qFLb6Sc3fYAtE9Zo05FgLeVp8gCNZnKTd1r4fJtp5ktWmnY2f2b5o95HeXVUBWPJHMCkss-soBiIXmtZoJZqBfJgYEfnCzQaCl2KvzQK8QTfyReiZIK7fGfvu4-gulWZl-Xoin9Cqpl90WChPRtrt8aFK7REuIcO0d-17iuePmctrqRlYrn7-F__ikrHmCTGTnMz_9Pfxbb8RZh4uapINOB0gBgtwWSMbPc4q4xMBJwRvUCdKHtv1H6iCWkw0Lz9JwQqrsqYtZmqR8SOGI3KI8kcaPeLksqKUuDDevFmBUnefc5hmD0MUMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرزوی شهید تنگسیری برای حضور نوه‌اش در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/676389" target="_blank">📅 17:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676388">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69947047f1.mp4?token=d4790vh8AL5wgDhbOBIM6LGO62WKljUUUR_1LCyVITW40neD3rJKGhY_hfh7ZFCkUTp_8w4QuB6BQT5qNeRcdB-b4b3pQriPxIzBgsWDIWiBE7pZYh7kjsDCIuRJ24MTrdcZY27cnc9qB7Qo9NFtTZbr4-yGuHke0lM-ybCgg66uyOQb1ay6zGV0cuNyQDn9C3G644uZXKupJL-mZc8VEbEgVkSaE7WcZorNXvYLMMkqkayA49cH3hrCD7Grja9lIe-JbucPycaCQHfPWXFZ6KjUWN-56Ry-grRKVBXeTa2U-0Uy09NtiwOHUwzRMo2csc3YKjWyrrZvPfvaA7WlIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69947047f1.mp4?token=d4790vh8AL5wgDhbOBIM6LGO62WKljUUUR_1LCyVITW40neD3rJKGhY_hfh7ZFCkUTp_8w4QuB6BQT5qNeRcdB-b4b3pQriPxIzBgsWDIWiBE7pZYh7kjsDCIuRJ24MTrdcZY27cnc9qB7Qo9NFtTZbr4-yGuHke0lM-ybCgg66uyOQb1ay6zGV0cuNyQDn9C3G644uZXKupJL-mZc8VEbEgVkSaE7WcZorNXvYLMMkqkayA49cH3hrCD7Grja9lIe-JbucPycaCQHfPWXFZ6KjUWN-56Ry-grRKVBXeTa2U-0Uy09NtiwOHUwzRMo2csc3YKjWyrrZvPfvaA7WlIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراسم بزرگداشت اکبر عبدی با حضور خیل عظیم هوادارن و هنرمندان و سایر اقشار در حال برگزاری است
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/676388" target="_blank">📅 17:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676387">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31ca1a5ce.mp4?token=dSsPagXcAJmZuU8sM6wt3ohH9TleLkbTB4M6busnM2x2clwt9hHQbY5uIBNYTHmT9JDkVkbv-xi42IKxAZV_xBd3mCchqnXUKHbg0j2csRUGKSeX_dGbLnhV4uTEw9eOk7tCqX_wY0vMtvpHyKQw-ZLI99eK1B_IjWzR6yyFMZjzLszomUuhcaa-98NnzZYghqZONOjt03ebMZaYbu-MAHFJqXfZ9aV6WLSRLSS9db7eJZIa9_OB-NJyRz32mjLchLoEme_sTJyYX9gf0kIiiBv_O4unco3SbHRcU6BBIsHnlg0gbqTsI7qJyXHHd0zklYcj6ZOkwGnZOR_EJv2-MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31ca1a5ce.mp4?token=dSsPagXcAJmZuU8sM6wt3ohH9TleLkbTB4M6busnM2x2clwt9hHQbY5uIBNYTHmT9JDkVkbv-xi42IKxAZV_xBd3mCchqnXUKHbg0j2csRUGKSeX_dGbLnhV4uTEw9eOk7tCqX_wY0vMtvpHyKQw-ZLI99eK1B_IjWzR6yyFMZjzLszomUuhcaa-98NnzZYghqZONOjt03ebMZaYbu-MAHFJqXfZ9aV6WLSRLSS9db7eJZIa9_OB-NJyRz32mjLchLoEme_sTJyYX9gf0kIiiBv_O4unco3SbHRcU6BBIsHnlg0gbqTsI7qJyXHHd0zklYcj6ZOkwGnZOR_EJv2-MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبور برق‌آسای تسلا از میان آب، همه را شگفت‌‌زده کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/676387" target="_blank">📅 17:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676385">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYsz76kV1pFWpENqgIZfNTw8NHXBt2X18SmpzTQxVjd5vXq-1IAOinonsGxCL4hiyEIBPkxfHR9QeEmOrphUYhULVE0-6ygJecNXtIx7doeM5sh55NAwW4IETlm5LYfNOuV4gS86xeqlH0MSXk6OnHsaNdy3bk1KWWTZ7ofjNAkfA19hdDgDLILc59RnzJjxdNzTuvbDBep5G3YfbDJZVUMYgIlYzwUd46fEuE2nBrKtoDyR0gPYPF1y3V8wd5lLXpF6cRCG-131XgSCQ7cYJWys-7JFJSWzBjSiyfdZhQzah7In_LUWMNPK25qtS47VXhrpeChLR31UILIRGSbrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🏸
ورزشی |
#ورزش_صبحگاهی
| ساعت ۸
🍱
آشپزی |
#آشپزی
| ساعت ۱۰
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۲
✂️
فوری استایل |
#فوری_استایل
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
👾
داستان‌هایی از سرتاسر جهان
|
#روایت_جهان
| ساعت ۱۹
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/676385" target="_blank">📅 17:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676384">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVpxyssYoTzCc4OsU-aeUvTyKZJsAxSueyNf-fcmTMkl47Cvpjg9h78nXYrDaBwsrUw-yPJnxKa9rkcngr_FwOiY4LUcdSQr2a229GM3X2sHX5_oXQQwVj6jfkrsR4YOwG2Bm3BMUV-ZExjZnPfojxTRLFMn4e45bzo_zr0D8eQyZGEScELY8xKNFivTkW-kotmjxHRuDxfF_pPXRGEn4j_Ob-by2_1rltXniK6QxyrBAxyEgYECRjKKwIJhNyx1355U1OLeKYReGIwyRBPW6O17t_G2rLZ2hvII-OQ3MISZ7UVY8-UeIm77FhLfAp3elocgBmUeRAykP0lyxwrX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن بیگلربیگی، کارشناس حوزه اقتصاد انرژی : بنزین مدیریت لازم دارد نه گرانی؛ کاهش مصرف و بهبود رفاه معیار سیاست بنزینی دولت باشد
🔹
موفقیت سیاست بنزینی با میزان افزایش درآمد دولت سنجیده می‌شود در حالی که معیار واقعی باید کاهش مصرف و بهبود رفاه عمومی باشد، اگر قیمت بنزین افزایش یابد اما مصرف کاهش معناداری نداشته باشد، حمل‌ونقل عمومی توسعه پیدا نکند، خودروهای پرمصرف همچنان تولید شوند و فشار بیشتری بر مردم وارد شود، نمی‌توان از اصلاح موفق سخن گفت.
ادامه متن:
https://eghtesademoaser.ir/fa/news/56135/
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/676384" target="_blank">📅 17:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676383">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg3TZwbf9C465Wm1yOhpWFu1eJ2kWuwn1wwy-FHPKz8PF0q0ldZF_s4J52PuyY-CSbJ2AZete0mhFArQbG9gXls10mRSthMCJTmLJV4F-aGcpuicz0y3d1P5wx6g315a3LsNK6Tgiwgd1s_Zn3JNxXIMKTyBfjApZV9MjktjGxf0wDy88bRbwbCzHe1dE2dqyA1eVTlTEyNutAqVtyb0Kn-2OQ_Ni9QGYabvrcTMyLG_Wv6N78HORGHLVrsWPjArGqeS28dRIcaJjsEKH4aj4-UkE0gFj2cVWsFIgp8QTC8O8KvgvxZACmyT3H6EbsATTMUnnstQ5F4GUdiV0Tazwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پل ورسک؛ شاهکار مهندسی در قلب کوه‌های مازندران
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/676383" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676382">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
از سوی رئیس صندوق نوآوری و شکوفایی ریاست جمهوری عنوان شد: موسسه ملل با گام‌های جدید فناورانه، وارد فصل تازه‌ای شده است؛ بانکداری آینده بدون فناوری معنا ندارد
رئیس صندوق نوآوری و شکوفایی ریاست جمهوری با تقدیر از رویکرد نوآورانه مؤسسه اعتباری ملل در توسعه فناوری‌های مالی گفت:
🔹
راه‌اندازی مرکز نوآوری و سرمایه‌گذاری فناوری‌های مالی ملل، اقدامی ارزشمند در مسیر توسعه زیست‌بوم فناوری‌های مالی کشور است.
🔹
به گزارش روابط عمومی مؤسسه اعتباری ملل، همزمان با افتتاح مرکز نوآوری و سرمایه‌گذاری فناوری‌های مالی ملل و رونمایی از چهار محصول راهبردی شرکت تجارت الکترونیک فناوری اطلاعات ملل (فام)، دکتر اصغر نورالله‌زاده، رئیس صندوق نوآوری و شکوفایی ریاست جمهوری، از اقدامات نوآورانه این مؤسسه در مسیر توسعه بانکداری هوشمند و فناوری‌های مالی تقدیر کرد.
🔹
دکتر نورالله‌زاده در این مراسم اظهار داشت: بسیار خوشحالیم که مؤسسه اعتباری ملل به عنوان نخستین مجموعه مالی کشور، مرکز نوآوری و سرمایه‌گذاری فناوری‌های مالی را ایجاد کرده است تا برنامه‌های هدفمند خود را در حوزه فناوری و کسب‌وکارهای نوین دنبال کند.
🔹
وی افزود: راه‌اندازی چنین مرکزی، اقدامی ارزشمند در مسیر توسعه زیست‌بوم فناوری‌های مالی کشور است و صندوق نوآوری و شکوفایی آمادگی دارد در کنار مؤسسه اعتباری ملل، حمایت‌های مالی و تخصصی لازم را از کسب‌وکارهای نوآور و دانش‌بنیان به عمل آورد.
🔹
رئیس صندوق نوآوری و شکوفایی ریاست جمهوری با اشاره به ظرفیت‌های ایجادشده در این مرکز تصریح کرد: بدون شک مجموعه‌های دیگری نیز به این زنجیره اضافه خواهند شد و مؤسسه اعتباری ملل می‌تواند همانند یک قطار قدرتمند، واگن‌های متعددی از شرکت‌های فناور، استارتاپ‌ها و کسب‌وکارهای نوآور را همراه خود کرده و مسیر توسعه و پیشرفت را با قدرت ادامه دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/676382" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676381">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4rbMyIojA9yMcwK1l7wS5ZTZAAxrfidIW74Xt258QzP4ADoUQpRemqCw7H8ts2A6tXwyiAZAMGh1oq3l2I9NmLT2hhdGDv_nhdWv-EPryMedXQoYnGizGg-X7oNK_2k31VEPCtN_mZl4QIP8px3osgsy8fMuYUM1pvnp9ix4ri_tybOvTMxnJpWU3eC_OeI5mHebx9HTzCOYOWsPoDd6lqxo01MIO-Wq0lW6dbz-ZGE9styWFBlTu-jY9P5MnrnsGUkjhz8wln-r2A4YiNmypWFdPi6M6VVtOGNj7okflJXbYcnuiO6GKYcM-6QxauZz_D-qrwUDYBtHHSZCGn0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با این ۱۰ نوع گیاه و ادویه، سیستم ایمنی خود را تقویت کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/676381" target="_blank">📅 16:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676380">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
شهادت ۴ ایرانی در حمله مشترک عربستان سعودی و آمریکا به کربلای معلی
🔹
پاسدار شهید علی اصغر آستانه
🔹
پاسدار شهید ابوالفضل متقی
🔹
پاسدار شهید مرتضی اکبری
🔹
پاسدار شهید امیر عباس درهم فروش
🔹
هر چهار شهید اهل کاشان بودند. / صابرین نیوز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/676380" target="_blank">📅 16:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676379">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38ba69f36.mp4?token=fZbRvbyoNYMEiCowAzulXaYerhxsK3_39n3_4TlXOie5XdS6hWlP5XmV7niP35YK7PtHcXL3gJO0x0N9-Eb4nZeUFIK3xXot5YjwjW-2cbWCTbM36KLSzJhNLpA9L3-JhPp8vfzJl1DPSdl6dCqAcVuBNrCRmPLah_O09xoQ-3-0FxvLJNwIeTdHav5BrZYUirV9yDK5rqV192Tt34W1lWNXt8i94zPAXGzW7DMjtvlx1I6moJdMlKMGfAdbDCNL1JZlJMWVgU6K3gu5fnGqm1fhm_NO0aqP8y-zE06aHtku9yWbl6-et8PC4kypCyY6D27aEoVNRLceYDn_KZ4B34eW4P1Nbr0Qw5nCevi55fnr-1eWcsfwLADc_vZD2ABDSamobA5zRfMROLEUjU_W0sY4b1cdZrPUgrMBAtBopP8TGujuGpZb7tRplRvddlyf-nSBJeGa6UDz2UcbRTYUsaO6EwpqNuGXAHW0wm4OQo8j4G0Cwu6fOiOFCR_SBgGgN0LWQ7do_NB9HGzyikRtopgZVvTnnsJ4BL_PPj0J17YYd9jG8MEgyOEaN0Jr6jiiU_0-wXjToEtWAX6I4buKEoLRLDY9RdhAwMAbKLb0PSCddrV5Rgwl1BEd9d7C2yhxEVT77Ga29NHSTmvRWA6eUMIIo4-GPlk7fPZr2At6VRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38ba69f36.mp4?token=fZbRvbyoNYMEiCowAzulXaYerhxsK3_39n3_4TlXOie5XdS6hWlP5XmV7niP35YK7PtHcXL3gJO0x0N9-Eb4nZeUFIK3xXot5YjwjW-2cbWCTbM36KLSzJhNLpA9L3-JhPp8vfzJl1DPSdl6dCqAcVuBNrCRmPLah_O09xoQ-3-0FxvLJNwIeTdHav5BrZYUirV9yDK5rqV192Tt34W1lWNXt8i94zPAXGzW7DMjtvlx1I6moJdMlKMGfAdbDCNL1JZlJMWVgU6K3gu5fnGqm1fhm_NO0aqP8y-zE06aHtku9yWbl6-et8PC4kypCyY6D27aEoVNRLceYDn_KZ4B34eW4P1Nbr0Qw5nCevi55fnr-1eWcsfwLADc_vZD2ABDSamobA5zRfMROLEUjU_W0sY4b1cdZrPUgrMBAtBopP8TGujuGpZb7tRplRvddlyf-nSBJeGa6UDz2UcbRTYUsaO6EwpqNuGXAHW0wm4OQo8j4G0Cwu6fOiOFCR_SBgGgN0LWQ7do_NB9HGzyikRtopgZVvTnnsJ4BL_PPj0J17YYd9jG8MEgyOEaN0Jr6jiiU_0-wXjToEtWAX6I4buKEoLRLDY9RdhAwMAbKLb0PSCddrV5Rgwl1BEd9d7C2yhxEVT77Ga29NHSTmvRWA6eUMIIo4-GPlk7fPZr2At6VRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محیا اسناوندی، مجری صداوسیما در کربلای معلی: با وجود همه مشکلاتی که وجود داشت، مردم خیلی بهتر از سال‌های قبل در اربعین حضور یافته‌اند و این مراسم باشکوه‌تر از همه سال‌های گذشته در حال برگزاری هست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/676379" target="_blank">📅 16:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676377">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGBTydyEiqz_o83FtW52hq7xxChcqEjheCRgiAnrUd5j_LUNBEpkI6kCyf3JW1COOXkl7q3psxsMZ8zGhIHvNHhiKvggd7aFiIqi9bu1oaBJjbsL1UU6EpCpz5babSTko-m_et1V-anOW_5mBQQg-qXdyNNEOadTpJl0XCy51K3DvCq4x0DuubkdwFK5qSe6L5oFeAMQ5Ymp7nAb_LbusKv9yjK7Lj6XprqP366MhXP8BfIJRQVE9gLQXWYOvjFaiQA5NFkojOzllXvRGXmxPQhNDpZ2H7wdzbUZKosV2iraihbXmYaoU9FhEBWrMsmf-4zR51qt24N-NhBO57g8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
امسال هم زائریم و هم خادم تا هیچ جرعه‌ای از جام عشق را از دست ندهیم
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/676377" target="_blank">📅 16:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676376">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420d680fb4.mp4?token=dDmmWVtI-Ifs5ffVj75fUNuliKnz58R7-zg78vLwDQ3FJ-eUASeR43z6zsqispalsPIry5CVA74xifRmeDYaeqkRPQ4pH9tvZtPpPqRJY7Cw3ElybgeSBs_PttktlVNnS5EfIEqVnwZP1UPuHG-ze6sTxlTrEyeRmTxwnPrO7jHCq7Ou3KBOkKBaLfJOO7fWaOfNZiV4BBhcrn1JlmqkHdv79nfE48Hg8nJI6vFLTMZnYUlvIZTLHeS2SH6nRyAEJLTrgMCqHeLM1zciZJYaFVnTTccceu356IK_7W1u8hQJ26pDTcC9t0Swnn_ugpL0WfqaL0XDHrO84sjDmog6PYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420d680fb4.mp4?token=dDmmWVtI-Ifs5ffVj75fUNuliKnz58R7-zg78vLwDQ3FJ-eUASeR43z6zsqispalsPIry5CVA74xifRmeDYaeqkRPQ4pH9tvZtPpPqRJY7Cw3ElybgeSBs_PttktlVNnS5EfIEqVnwZP1UPuHG-ze6sTxlTrEyeRmTxwnPrO7jHCq7Ou3KBOkKBaLfJOO7fWaOfNZiV4BBhcrn1JlmqkHdv79nfE48Hg8nJI6vFLTMZnYUlvIZTLHeS2SH6nRyAEJLTrgMCqHeLM1zciZJYaFVnTTccceu356IK_7W1u8hQJ26pDTcC9t0Swnn_ugpL0WfqaL0XDHrO84sjDmog6PYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجارت مرگ زیر پوست شهر/ دارو هست اما در بازار پنهان
🔹
یک داروی حیاتی در مسیر رسمی نایاب می‌شود، اما رد آن بیرون از این مسیر دیده می‌شود.
🔹
همین تناقض، سؤال‌های بزرگ‌تری را درباره پشت‌پرده بازار دارو ایجاد می‌کند.
🔹
ماجرا فقط کمبود نیست؛ نشانه‌هایی از یک چرخه پنهان و نگران‌کننده دیده می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/676376" target="_blank">📅 16:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676375">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f22a9d150.mp4?token=Wq3srqHJmLA7qNjjIdIQ4mLxDaaF82-l561Ss9UNQ1IvKc0iYaBFOddbNpQBZuaSw1dZq78HUxd59en0v2cc4bBLngA-qUFRrXPT4SxnRrqizp-2BaTsGZIfRG3SaFGhb-jwjjAYRdYdR9NGUlAVOuybEB9Fwae-X-DoLGf0ZUWOpoixea6p5NvkvQqkPl7-1c3Y1sec_sk9WfJYJNyzDIhtL2OVOOKgpAcX6PeCRMhvDQTUYKGq3gFSFJimu-PRY-UtJVja35pCZLtbDRr2UfVC3SxVaHEoMRSvjw0wFWKz0s6Tzsa75pc9XgMHfEKCsGL7EVNRNZWttiZ1M9Zh0kqZemE_WSIYSYctDzofbI20PEer_Go_zDJj_xaLEUW0GqMhFXCDojuVb7TgHIFeoGefXTQfLHGH1ewromv2z3G_FeKZUglKldhys2xyrls8gnhsDUfR52_uuF7l0wIMwIF_s8uYAvW6VAChiAjfR8Sdp6u63qjQdQcUeMDmTzmwuzUyZUqwzidXaT5O4Rdlxk4I2qMfGMqGAln4NyMUgSg3ppQji6_tBGaUV1bj-__3mQGcitMK1eheQ93AlRFkcxaEBU04Iz07FJsQjG2pop77mPr6gkUinbz7PRhyYuovweAoksUpmfkoHBYvfTMci-043OeQczUfExi3LFi2gxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f22a9d150.mp4?token=Wq3srqHJmLA7qNjjIdIQ4mLxDaaF82-l561Ss9UNQ1IvKc0iYaBFOddbNpQBZuaSw1dZq78HUxd59en0v2cc4bBLngA-qUFRrXPT4SxnRrqizp-2BaTsGZIfRG3SaFGhb-jwjjAYRdYdR9NGUlAVOuybEB9Fwae-X-DoLGf0ZUWOpoixea6p5NvkvQqkPl7-1c3Y1sec_sk9WfJYJNyzDIhtL2OVOOKgpAcX6PeCRMhvDQTUYKGq3gFSFJimu-PRY-UtJVja35pCZLtbDRr2UfVC3SxVaHEoMRSvjw0wFWKz0s6Tzsa75pc9XgMHfEKCsGL7EVNRNZWttiZ1M9Zh0kqZemE_WSIYSYctDzofbI20PEer_Go_zDJj_xaLEUW0GqMhFXCDojuVb7TgHIFeoGefXTQfLHGH1ewromv2z3G_FeKZUglKldhys2xyrls8gnhsDUfR52_uuF7l0wIMwIF_s8uYAvW6VAChiAjfR8Sdp6u63qjQdQcUeMDmTzmwuzUyZUqwzidXaT5O4Rdlxk4I2qMfGMqGAln4NyMUgSg3ppQji6_tBGaUV1bj-__3mQGcitMK1eheQ93AlRFkcxaEBU04Iz07FJsQjG2pop77mPr6gkUinbz7PRhyYuovweAoksUpmfkoHBYvfTMci-043OeQczUfExi3LFi2gxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی صدری‌نیا ، مستندساز و فعال رسانه‌ای: شهید لاریجانی روایت می‌کرد که برخی حکام عرب متوجه شده‌اند که آمریکا و اسرائیل خیر آن‌ها را نمی‌خواهند اما چون در مدلی از رفاه زندگی می‌کنند نمی‌توانند پای حق بمانند و مقاومت کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/676375" target="_blank">📅 16:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc53bc3b80.mp4?token=m99VLmYAWHmxKEV-IYvg2hghodiVniNkhTmYUN7j2NaucIW56K34CF-86JjPkSuUwk0y81oNu5WMgTJ435tpWZhBZ8aAl-HIK-3QpyHMboPqlEptzCV74OstNUJtAcPF4S4JjLvuKqDts8gmNZrHf2_0R1BS0LWZ4exNtKS_JmB7gnQb6A7L_F685uUywLp01iZttfKUVVqv5FqVPDHALMmlBu4_b9RCZ7KGcLSuxzOKAhoBcLt2HmibkH77FgY_NWMNztFKzXGvvBbfPokJtVTXZo8R3b19L_jK4Uh1p1Vy0QPdi-T0vAZGyQ2eHOQM2BQ6NoBuoCzrVCihH5U9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc53bc3b80.mp4?token=m99VLmYAWHmxKEV-IYvg2hghodiVniNkhTmYUN7j2NaucIW56K34CF-86JjPkSuUwk0y81oNu5WMgTJ435tpWZhBZ8aAl-HIK-3QpyHMboPqlEptzCV74OstNUJtAcPF4S4JjLvuKqDts8gmNZrHf2_0R1BS0LWZ4exNtKS_JmB7gnQb6A7L_F685uUywLp01iZttfKUVVqv5FqVPDHALMmlBu4_b9RCZ7KGcLSuxzOKAhoBcLt2HmibkH77FgY_NWMNztFKzXGvvBbfPokJtVTXZo8R3b19L_jK4Uh1p1Vy0QPdi-T0vAZGyQ2eHOQM2BQ6NoBuoCzrVCihH5U9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معلم ایرانی که ضربه آزادش از روبرتو کارلوس هم عبور کرد؛ حالا پیج ۴۳۳ دنبالش کرده
🇮🇷
🔹
پیج ۴۳۳ یکی از بزرگترین و پر‌مخاطب‌ترین صفحات فوتبالی جهان در اینستاگرام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/676373" target="_blank">📅 16:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ترامپ اعتراف کرد که جنگ با ایران محبوب نیست
ادعای هاف‌پست:
🔹
کیلمید مجری مشهور فاکس‌نیوز در یک پادکست اعتراف کرد که دونالد ترامپ، کاملاً از عدم محبوبیت جنگ  علیه ایران آگاه است.
♦️
رئیس جمهور گفته است که سایر کشورهای خلیج فارس «در حال حاضر از یک حمله بزرگ هیجان‌زده نیستند.»/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/676372" target="_blank">📅 16:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای خوک هار: حمله ایران به اردن غافلگیرکننده بود، نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را ساقط کنند
🔹
در پاسخ به حمله غافلگیرکننده شب گذشته در اردن، حملات آمریکا علیه ایران انجام خواهد شد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/676371" target="_blank">📅 16:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676370">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای سگ زرد در مورد تجاوز به عراق: حملات آمریکا و عربستان سعودی با هماهنگی دولت عراق انجام شد
🔹
من در نظر دارم اخطارهای جدی‌تری را علیه نیروهای نیابتی ایرانی مطرح کنم  #DEVIL
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/676370" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676369">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c7a42a18.mp4?token=IaTbDU1Fo0sR4Dqq4mgdDCGeP7oV7mmBElQ4QDCKrwbNxj1qLkH5xe_olY1ND_i5aVMVY_RwYejcEnMfcb8TKKsdJrvx3Yb2juCyLlENMUTwLAqYpeJmFDm-6UfkNIfUYJmeaxUX8K2dLJWnXdZZ7s8qL76LzF0AlnkRxqhw6JKFWmV66eOcNSVAfu34Dr24wlpDnzKMmu7I3Kcr6BAiwM5ryxFTiICCEIpdvxv1TN8cZbOZKxsXv7g1Qv-RfINXO0Al9vzhDpu0jLwP4FR3yipkd5lQ2SWdoik4uwE1PgdB8hyxEkREiaFgVFLDeWa-1rBMdASLXltiKm67X-IPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c7a42a18.mp4?token=IaTbDU1Fo0sR4Dqq4mgdDCGeP7oV7mmBElQ4QDCKrwbNxj1qLkH5xe_olY1ND_i5aVMVY_RwYejcEnMfcb8TKKsdJrvx3Yb2juCyLlENMUTwLAqYpeJmFDm-6UfkNIfUYJmeaxUX8K2dLJWnXdZZ7s8qL76LzF0AlnkRxqhw6JKFWmV66eOcNSVAfu34Dr24wlpDnzKMmu7I3Kcr6BAiwM5ryxFTiICCEIpdvxv1TN8cZbOZKxsXv7g1Qv-RfINXO0Al9vzhDpu0jLwP4FR3yipkd5lQ2SWdoik4uwE1PgdB8hyxEkREiaFgVFLDeWa-1rBMdASLXltiKm67X-IPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا وام گرفتن برای یه نفر باعث ثروتمند شدنه‌، ولی همون وام برای یه نفر دیگه شروع بدبختیه؟
🤔
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/676369" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676368">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای خوک نجس: حملاتی به ایران انجام خواهد شد و ضربه محکمی به آن خواهیم زد #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/676368" target="_blank">📅 15:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676367">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای خوک نجس: حملاتی به ایران انجام خواهد شد و ضربه محکمی به آن خواهیم زد
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/676367" target="_blank">📅 15:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676366">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4de24473e3.mp4?token=V6vVKWETm75T6KnA-MaTW5UhZHC1-6lfKaZ1sXdGKUoh1Zm938w3OGJGUcKdaFHXyywgB9iy5GVBGexNzajuZvyeBoqXhBsOYNlXN8s--d7m2IwOimv5bbw_ocVk0isIH2hdc0uq7EwwjrUhijK-EnPobHuFhztPaDgfULybiix-p-UcNZXtwyQu-6gPtIWRk1lgs7Wdys9YHI1DRqDeZcp-TZCChe0iXOQoVX5ia5SIgn6gYmOjNDjOqdLlHLqdGT5RosRKL753aXiY_YDqzOBSgA7G59HoyoMVdHqf11QYBdBuzfk9csxQSlIuAR1umHWFbqmWcFHFs7AoYp9clw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4de24473e3.mp4?token=V6vVKWETm75T6KnA-MaTW5UhZHC1-6lfKaZ1sXdGKUoh1Zm938w3OGJGUcKdaFHXyywgB9iy5GVBGexNzajuZvyeBoqXhBsOYNlXN8s--d7m2IwOimv5bbw_ocVk0isIH2hdc0uq7EwwjrUhijK-EnPobHuFhztPaDgfULybiix-p-UcNZXtwyQu-6gPtIWRk1lgs7Wdys9YHI1DRqDeZcp-TZCChe0iXOQoVX5ia5SIgn6gYmOjNDjOqdLlHLqdGT5RosRKL753aXiY_YDqzOBSgA7G59HoyoMVdHqf11QYBdBuzfk9csxQSlIuAR1umHWFbqmWcFHFs7AoYp9clw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«قصه‌های جزیره» تا امروز؛ گذر ۳۰ سال بر چهره بازیگران این سریال محبوب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/676366" target="_blank">📅 15:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw2G2Riu-bEzS17yWXqY7hXWRGWGUGONrqE_1swLneO-4wYyB3dppNufUg9I9gym-BjCwTmNZR2F9gQCWqTijUZ40ydqKh02GZ_H-cFUBxrtX34mwT70TVTgD_QimkxndcsLQh9J0RkiUP0SE-WxmdsxMCYHSOR3jdzfTjbCCyvszpZtvfKGMOw7IL0V_L3wz0xBD2pbKfbYMRZQ2fOUQIi123u39U4s9L9jGr34F42jH7w4Hw-iXBVxp3idml-RenS1uii3uTp7nxgREhTIzHcgQ10aUJ2kcTFyJltzy8xcxekHoitHfI5C4H-5yZPtN6WLQg4BGx5ENRxZ3p46pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین واکنش پژمان (شرکت‌کننده برنامه عشق ابدی) بعد پخش برنامه‌اش در خط قرمز: من حرفم را از روی احساس لحظه‌ای نزدم؛ از روی باوری گفتم که سال‌ها به آن رسیده‌ام/ من به ایستادگی احترام می‌گذارم؛ به کسی که تا آخرین لحظه کشورش را ترک نکرد، مسئولیتش را رها نکرد و در همان مسیری که انتخاب کرده بود جانش را از دست داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/676364" target="_blank">📅 15:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676363">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4bf76e75.mp4?token=qRjBIL90Kl3rTZI6cu5S8q3RyvBpFDXe8-EM1uw16HbTrPHGaFCHEMRhmVeT5V6Z12OpVdeYKoi1sEUkr3s7q9ZltLbTMKQvG3GKZW_CgaS-I71qUUlmjL1mzjLfFSb9-uVQLeSPJwUDwkhtgYV51l8BGqvLPv7YkOIgwRzmvHgmyxkaTGITooZNDnQZHvUEvSefh5t90kdNxrNxAFdWUq_hy3yBo255-tjRW-uQSt2yf2fGkbsmt-6-8MG162lBr59Q7GRV3vHj49xwJkSe0zvtqzjZfaprB-1vHremE-Bo3zmLBkLZuX0rFPG6ZtWpo1wxC-mFP3HIzhoEOPuzWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4bf76e75.mp4?token=qRjBIL90Kl3rTZI6cu5S8q3RyvBpFDXe8-EM1uw16HbTrPHGaFCHEMRhmVeT5V6Z12OpVdeYKoi1sEUkr3s7q9ZltLbTMKQvG3GKZW_CgaS-I71qUUlmjL1mzjLfFSb9-uVQLeSPJwUDwkhtgYV51l8BGqvLPv7YkOIgwRzmvHgmyxkaTGITooZNDnQZHvUEvSefh5t90kdNxrNxAFdWUq_hy3yBo255-tjRW-uQSt2yf2fGkbsmt-6-8MG162lBr59Q7GRV3vHj49xwJkSe0zvtqzjZfaprB-1vHremE-Bo3zmLBkLZuX0rFPG6ZtWpo1wxC-mFP3HIzhoEOPuzWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنگ‌تمام گواردیولا برای کودکان فلسطینی
🔹
پپ گواردیولا، سرمربی اسپانیایی و حامی مردم غزه، ۲۸ کودک فلسطینی را به کمپ تابستانی خود در شهر ریالپ اسپانیا دعوت کرد تا چند روزی را در فضایی امن سپری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/676363" target="_blank">📅 15:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676362">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlQHDUo2necFHrR0_nFYtvKwFOvfwmwk0dvd7yaPreP1KKbEvJuWqnUT1T2igYIVoUzUV7yfPv1Lcgf6kr5v6CY5culZsudGxgmP1UEyxyq3VTvvq4SaeiZ9VBZ5WK_KbGKg0JcJxkd4kI1ozGXYudLFZIRE0jZvaQtMkfVopWdHlxdu7kbyYyPt-guS9m_QchtLCjxaWSqhfMiCJxDj1GRXV9WPcY73i2Iqsy_n6JlJMr-sbgNrKE462hFjq1O81NAahN2SXUWOOcyKbK2nDOzw-JJkHbUb8bsKoDAh-YbdyAWyeacqgZMfc_Sd4jhXP-dWDcrjF8xtSEM3LJZOYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
گاها یک همراهی کوچک می‌تواند نام ما را در سیاحه خادمین اربعین حسینی قرار دهد
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/676362" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676360">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afda39a823.mp4?token=Vd8bKVtoo5T3glz8oMElOdH6BaI9-S21TE4GOr0pcT_QhrVrrF8KfV2e9ZXxNc80eSlfhCBoEcnSuZ96tTI7rqIRaJhW_bCZpjE3_BbOW5Lutn5AKa_zjqVhEZtGL942Ce2ereNFrVbgMwemdv4sTjb77--eSY60uho1khnrNEyf0MxAKPhS_U4TgyfUCCucHnAh8v0SqZpkxi5VghrgTCrZAm_96xOwqRhRTQEnn5Ctpfx4zjwpJUgGFgG0eLtDuXwkuRWFV9tyWi4aXBm3RlLFSS3oXp43titl5CFAw0s-9bv31rZDbjXc7IK4YJiNlqYOuYUiatos8tznz1-VOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afda39a823.mp4?token=Vd8bKVtoo5T3glz8oMElOdH6BaI9-S21TE4GOr0pcT_QhrVrrF8KfV2e9ZXxNc80eSlfhCBoEcnSuZ96tTI7rqIRaJhW_bCZpjE3_BbOW5Lutn5AKa_zjqVhEZtGL942Ce2ereNFrVbgMwemdv4sTjb77--eSY60uho1khnrNEyf0MxAKPhS_U4TgyfUCCucHnAh8v0SqZpkxi5VghrgTCrZAm_96xOwqRhRTQEnn5Ctpfx4zjwpJUgGFgG0eLtDuXwkuRWFV9tyWi4aXBm3RlLFSS3oXp43titl5CFAw0s-9bv31rZDbjXc7IK4YJiNlqYOuYUiatos8tznz1-VOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چشمان بسته ترامپ در مراسم خاکسپاری گراهام خبرساز شد
🔹
تصاویر ترامپ با چشمان بسته در مراسم خاکسپاری سناتور «گراهام»، واکنش‌هایی را در شبکه‌های اجتماعی به دنبال داشت.
🔹
برخی کاربران با اشاره به سابقه انتقادهای ترامپ از جو بایدن به دلیل چرت‌زدن در مراسم عمومی، این تصاویر را دستمایه شوخی و مقایسه قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/676360" target="_blank">📅 15:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676359">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdbfc3d69.mp4?token=No46L8FJhmyIZ16GBHI0Bmee5FARo_etBuxeo0ft3ikKAxTInEUfPDo2EBl7-riJrHT7taFu6qDQiBvyGQiE-9_Q0n92NSaZ8eisPkhf7Qs1QjODh5fneqNZeNuVu5RDWBonFaydjiCwm6a8BJq7N8EQa9aLhJtwYPUO2XeUMniytq5ekm3VPKEO1NYPDhxrvs0LUtB4NbxuqcOlIZKn7kKYSCPsAzZKjELNvftgyN9DA4Ipo58AFMjJz-VdwD9geRxwVIj-bR4PpHXRVjxEI1Stm9vk4UE3vumNGhWGWZJAkryjHYiBo3Hg-WXWJvEEKr0ALtpc5lAFRg3Hl-6PXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdbfc3d69.mp4?token=No46L8FJhmyIZ16GBHI0Bmee5FARo_etBuxeo0ft3ikKAxTInEUfPDo2EBl7-riJrHT7taFu6qDQiBvyGQiE-9_Q0n92NSaZ8eisPkhf7Qs1QjODh5fneqNZeNuVu5RDWBonFaydjiCwm6a8BJq7N8EQa9aLhJtwYPUO2XeUMniytq5ekm3VPKEO1NYPDhxrvs0LUtB4NbxuqcOlIZKn7kKYSCPsAzZKjELNvftgyN9DA4Ipo58AFMjJz-VdwD9geRxwVIj-bR4PpHXRVjxEI1Stm9vk4UE3vumNGhWGWZJAkryjHYiBo3Hg-WXWJvEEKr0ALtpc5lAFRg3Hl-6PXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت علی صدری‌نیا، مستندساز و فعال رسانه‌ای از آخرین حضور شهید لاریجانی در مراسم اربعین در کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/676359" target="_blank">📅 15:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676358">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bdd9158f.mp4?token=QorPa-qReztJ0r3dn-EiMb4jRoFbPBnrHDp-UkuNCT7aLGxxrJTalAuXpfqq_SVcx5letTfv5T8A-MvTNry4gM-mfGjvxrCnvGrNxDmaSr7hMJ37sDJr2JTalCyMv5UdC1UIBTpm9vihIeuTCLrSuX-v9JgBwearUM2A0AqbV7JVOwHjWdCoGwyxSt87v0mYnWLtrIrI_6QR0vQf51Kqj7h_aneXpWoerffp39aDCeTT9umPd2tx0cKlgf8be3gQ_6c6Ib_fWbfyVIUHJFvK8n95ccijVeX-lTigHqZLvxrg8veTYlURjm2nKhruINiOJHLVIMOO1f1Z_RmM-QwkWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bdd9158f.mp4?token=QorPa-qReztJ0r3dn-EiMb4jRoFbPBnrHDp-UkuNCT7aLGxxrJTalAuXpfqq_SVcx5letTfv5T8A-MvTNry4gM-mfGjvxrCnvGrNxDmaSr7hMJ37sDJr2JTalCyMv5UdC1UIBTpm9vihIeuTCLrSuX-v9JgBwearUM2A0AqbV7JVOwHjWdCoGwyxSt87v0mYnWLtrIrI_6QR0vQf51Kqj7h_aneXpWoerffp39aDCeTT9umPd2tx0cKlgf8be3gQ_6c6Ib_fWbfyVIUHJFvK8n95ccijVeX-lTigHqZLvxrg8veTYlURjm2nKhruINiOJHLVIMOO1f1Z_RmM-QwkWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احسان علیخانی با انتشار این ویدیو: ما یکی از ستون‌های خاطرات‌مان را از دست دادیم. ممنون برای تمام خنده‌ها…
🔹
خداحافظ عمو اکبر، خداحافظ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/676358" target="_blank">📅 15:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676357">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95677ca598.mp4?token=TwiohbXo2Gzhm_NvLsaM_RukrXbJQNQj8TwVpxzhEwb0cczBO4vwQA_Tf6f3MEwyGAipDPRj_qm7lIUbKWESBlPb9m6XRj5Vlbms-slLoOlcXKsvTcl3ebbsfRhswTEFYaJpDAk0e_uoeiycLjpnXXLVl9fbJwcXHRu346QmzvvHYtCKOzM0E02I25ZMLbZJrqa9c1VxWYGwKpcYUTs_DcfXERuFKWZm-dYuIYjQlONhf1lzGDl7dVPqT14aAO6tqXZEVOVyt-FEKgfhwMO-zSPU0fNZJ7FmiOzm1kcg46pINtS99DeYj71odz6VjzirntmoW0Gah7bXhgzZB1y7Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95677ca598.mp4?token=TwiohbXo2Gzhm_NvLsaM_RukrXbJQNQj8TwVpxzhEwb0cczBO4vwQA_Tf6f3MEwyGAipDPRj_qm7lIUbKWESBlPb9m6XRj5Vlbms-slLoOlcXKsvTcl3ebbsfRhswTEFYaJpDAk0e_uoeiycLjpnXXLVl9fbJwcXHRu346QmzvvHYtCKOzM0E02I25ZMLbZJrqa9c1VxWYGwKpcYUTs_DcfXERuFKWZm-dYuIYjQlONhf1lzGDl7dVPqT14aAO6tqXZEVOVyt-FEKgfhwMO-zSPU0fNZJ7FmiOzm1kcg46pINtS99DeYj71odz6VjzirntmoW0Gah7bXhgzZB1y7Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
📍
تهران
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
یا عدد 4 را به سامانه پیامکی
3000909030
ارسال کنید.
📲</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/676357" target="_blank">📅 15:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676354">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
رجیستری گوشی در مرزها همچنان ممنوع است
🔹
گمرک ایران با ابلاغ بخشنامه‌ای اعلام کرد شیوه‌نامه خدمات گمرکی اربعین، از جمله ممنوعیت رجیستری گوشی در مرزها، همچنان تا اطلاع ثانوی معتبر و لازم‌الاجراست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/676354" target="_blank">📅 14:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676353">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgD6IuQlW2KDVbcTozMpJpuLSmGdfHWhTByvQd9J_r0OAamIsEJ8sliEYSjGOiTEKDFc3PaItK9T40VkHg-sGvqx9OvYPUMVgUMSwt8GVtBqyJzDkSi0iT38hDPCIheEd6bB6mYYaeJggjPzbDfTl3EfLltgmWQtJbu2CkknyRnYVPLhC9Z9L-riujFPjOZsl_sp28i924RhhhB723kcOK1IoiGqc0qm02PY9ifQzd5VG8dCJ8RZ-fwuL7R4KRg07QYMJDpxyIC7LENFTHn9qEnthXuVLMKpmZ9476X6gF5RYIOV0z-eGgktdvVQg8aUgbN8zABr2oYr_FuRyW5HpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
شما هم زائر یکی از ۱۰۰۱ سفر کربلا باشید!
✨
همین حالا با شرکت در پویش «زیارت به نیابت»، عدد ۲ را به شماره ۳۰۰۰۱۱۵۲ ارسال کنید و شانس خود را برای برنده شدن یکی از ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/676353" target="_blank">📅 14:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676351">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sojvlaPCVqEgZ7lYVJprXDOqtZrH3NtT0gLeKsIGyfYADPyGkJpCxTtgtoskTGDm0xdLrUQ1jivt0VC_-QMoMRz3071Q0TmAiDnBQAYItfGA8_fkvxGxIGhRyYNcYyxcbuSLWkJl6b7wcZAn1M9nGzGoIMfi2UDlYC3ySNjLmMMt84ais_vYn8_QiITn9Eez5Y8aEfZoZ8CVNBpd6P9tr2OrfpfpAUNrDUxddftJFXdolxO7Mi8DkLkmEavWn2nED9NvjUNhR8rye3ctCuhsGRhr0NvLTxkEPP60z6K108Qb3sYxrF2tPTkWrRVOArGthyYFAjYSGg-j07biZhu-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e6dbca08.mp4?token=ukTMEcLtO7yhP8ueNpbBf6pXtoB40Tpve4qRqGxztCRTLs4PaXfqgTBhmnY26U3DsSLpQOuwn_OUpO9GoyQzV7Zyz-h6E-Ml11weaoYwJ5_tCyL9pyqW-NkOPJYycKs8mHspbLz0YsvuETtTDmnmAU_TjiHyaQRqn2_rK_kizTgV4a-K_0X7ZwVRnFFiweL9gB0QaGR90vRU1aLZwjSmmqCUdwAnvCBqyLQT_vyQmoZzHbmQENesXyLvUCW-l-wX61bvXJp20KI2WXP_InplpiDrd1eaIakxAG6pxQeaxDzv_-T-frSdtPXxTTBueah5-ZlaNmYEEk4vdWSibfXZKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e6dbca08.mp4?token=ukTMEcLtO7yhP8ueNpbBf6pXtoB40Tpve4qRqGxztCRTLs4PaXfqgTBhmnY26U3DsSLpQOuwn_OUpO9GoyQzV7Zyz-h6E-Ml11weaoYwJ5_tCyL9pyqW-NkOPJYycKs8mHspbLz0YsvuETtTDmnmAU_TjiHyaQRqn2_rK_kizTgV4a-K_0X7ZwVRnFFiweL9gB0QaGR90vRU1aLZwjSmmqCUdwAnvCBqyLQT_vyQmoZzHbmQENesXyLvUCW-l-wX61bvXJp20KI2WXP_InplpiDrd1eaIakxAG6pxQeaxDzv_-T-frSdtPXxTTBueah5-ZlaNmYEEk4vdWSibfXZKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غول ۱۸ ساله دنیای بسکتبال؛ ۲۲۹ سانتی‌متر قد و هنوز در حال رشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/676351" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676350">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEXfvja-n5RMbw0A8xrr2yPvGvVt_XJe8ajx87OUtHe9dp6WLL4eyL6AnqHz-MYpOiLh8WmNAtEJXGaP1kHKD33iJfwcwIWVX700482EaBPy3NzH7PekCefDMha8K-x4fRs8iYNQhV57f0znoi3EmDDvMw6SUiCwjw0TCU4UWwYE7U5krl2lxzEDRH5VJnJgFNqmp7E8gZk8WK3B_End_6qpNoD8LpJnUHx7w6nrvafe0tSfGB-m3lFo1S9-qt9b57rLmX10fjOCuUm8a6kk-CBiEBDqp4DfOIRDgfPKR8X4HelxG2lwYstCUXAXdm6F7J1Rho1NKv_Uj_ZldQXyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در شاخص جهانی نوآوری چه جایگاهی دارد؟
🔹
در شاخص جهانی نوآوری ۲۰۲۵، سوئیس با امتیاز ۶۶ از ۱۰۰ برای پانزدهمین سال متوالی در رتبه نخست جهان قرار گرفته است.
🔹
ایران با امتیاز ۲۸.۵ در رتبه ۷۰ جهان قرار دارد و بالاتر از کشورهایی مانند کویت، آرژانتین، مصر، لبنان، آذربایجان، پاکستان، تاجیکستان و الجزایر ایستاده است.
🔹
با این حال، ایران همچنان فاصله قابل‌توجهی با کشورهای پیشرویی مانند سوئیس، آمریکا، کره جنوبی، بریتانیا و چین دارد که بخش مهمی از اقتصاد خود را بر پایه نوآوری و فناوری بنا کرده‌اند.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/676350" target="_blank">📅 14:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676349">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdce95a76b.mp4?token=DiKEzY3A29XeMch1MtaibW1DYik0PeUEM--MhnVYlrn71nj9PTqfO0sumweSAYChxKzKozPYvJTnvkeaDUqqhLAKPxm5mCls-f4pr8K0Cy387ZEpqcFAJBYKrG-j7Y59uydpQ3NhzxekqXruPVZAFC9Pjuu10XEMVybpBK0ANDsecxoFogwliBlRixF9LyjU4vZyn1sEHa59KGFhg3jIr2nn3IYEgHM6CqFdfynCkSq3w3Qe-JjhMlkj1yR_rcn3KBE9PIwndeYG-DSqzlcM2KuXhf91eiA_wQ3Ow0r8aY_MTkz2ORWOp_zS15XdX56F7Iwvq9SNpAOQRSSnH6jV6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdce95a76b.mp4?token=DiKEzY3A29XeMch1MtaibW1DYik0PeUEM--MhnVYlrn71nj9PTqfO0sumweSAYChxKzKozPYvJTnvkeaDUqqhLAKPxm5mCls-f4pr8K0Cy387ZEpqcFAJBYKrG-j7Y59uydpQ3NhzxekqXruPVZAFC9Pjuu10XEMVybpBK0ANDsecxoFogwliBlRixF9LyjU4vZyn1sEHa59KGFhg3jIr2nn3IYEgHM6CqFdfynCkSq3w3Qe-JjhMlkj1yR_rcn3KBE9PIwndeYG-DSqzlcM2KuXhf91eiA_wQ3Ow0r8aY_MTkz2ORWOp_zS15XdX56F7Iwvq9SNpAOQRSSnH6jV6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، سرزمین قهرمانانی که شجاعت را نه در حرف، بلکه در نجات جان انسان‌ها معنا می‌کنند
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/676349" target="_blank">📅 14:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxPxkB10eQFl7UgfpmffgpQDE7BpqBHwhaJaBas_0zWCSM1LLE6gi6gzO6kGC9y9Pebb3zVYCrG50JlC4MWq3RrhQ63-E37MZiDkZS7i-OBcVc8u1RC5xCtU9F7HJYkypDDnW_yzHTQPWMpyVqdGIwB1XQFPE51LW69IKPjVp9QxO9ESTzA5u6vfaBODYQF58vVOrhCxotZkTNVAqAQNhw93TPHgVrYPus_NxWITyhFbj-N8RYkQ3DitWl0x9b58nAl3F44xdG0DvbY7Dg4DvsBPw5060Qa1a929U9zIRWXtEQXRVe9weAKcxcraLYDJXYZVudEZRjcXDmcm5j0vMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مبلغ وثیقۀ مورد نیاز برای خروج از کشور با هدف ادامۀ تحصیل از ۸۰ میلیون به ۲۰۰ میلیون تومان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/676347" target="_blank">📅 14:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coP6RSNWe_GLQT0GWKHDOoq-lwgcjtWywBDaqfM_cB7ZQKZmL_PnXlecJbJyLtSdIBtelSFZns9kC2CU-ZU8Y1bd_4cH_S2GQOoy1k0MSoy4sXBCs9WwF1ynMIWOAQ6T4I81xEWq-z7XFvGP9siM39CVEc63hS89ROZrtkFg7KGQFKoxmFu1_a05c5x0Fvcdo_l1Ybs6ohHjE406WwpguZDP6WWdRj9cOquPA9GfdQcLSNmsbkWwISTcXr3TnTTMOFVBUz_adYSSTo1esJy9HsLKvOOAr-3q4SMJWscUL_B1ZUUewKiBpAh_hJ2bwT-7h95oaeUk_LRHhF8MEjdeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صندوق طلا چیست و چگونه کار می‌کند؟
🟢
صندوق‌های طلا در گواهی سپرده شمش و سکه سرمایه‌گذاری می‌کنند. پشتوانه این گواهی‌ها طلای فیزیکی اصالت‌سنجی‌شده‌ای است که در انبارهای بورس کالا نگهداری می‌شود؛ بنابراین دغدغه اصالت، نگهداری و سرقت وجود ندارد.
🟢
این صندوق‌ها علاوه بر کاهش هزینه‌های خرید فیزیکی، با مدیریت فعال و ابزارهای مشتقه می‌توانند برای کسب بازدهی بالاتر از طلا تلاش کنند. در روزهای جنگ نیز صندوق‌های طلا پس از چند روز بازگشایی شدند، درحالی‌که بازار فیزیکی و پلتفرم‌های طلا همچنان امکان معامله نداشتند.
🟢
صندوق طلای رز ترنج از ۱۰۰ هزار تومان و با جست‌وجوی نماد «رز ترنج» در تمام کارگزاری‌ها قابل خرید است.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/676346" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676345">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd680441ef.mp4?token=e68lUvzogQXd8uwArPvIqo8AeseroWhbgAgq1i7zc5qUMQcIheukzKeJqjUCstEiW2scUUaqnPMSlVKlrhNweXMi4neCwhGnS7I17JKMkzSJ59ozSI2x-Ny8sOFHhdEe_I-B_yXg5WPT1DPj3H9PePqYXN9FclWSeYzwX3KUiOgW0KAkFpPab9WF0V9X4zfVgZJDkn_Jbcs6ylda0eAJ8ZtCD_xziJl46oxKFZWoY2YzqXjcZ8iQDu5McYL0_qwHx3btTPYKZasdz0FWlQ71PV1Ccsxyek62zchGTKuNHs6c2FpHmxKTUCGLZa0tAv2fqaMBPNgPAWEdLsYWZDDvJZ9xHCRmapP5OExFoknQXohBxxtKSaMyd4DzrlQsg3B0mizkN4aGtMX9tbK12erv6QdWqRYsYQWFyhaIglXMT60fa8aMIINmjzYFs3MtAoRkGXpRNk7iJdHWNuAWdw2-zc5OJ2bSnG3MsK2k563x7NO1t9Jfu5xET05dZX4rwHJO7BE-d4OxkYwHcG7wq3aCkwN5iPerZx8hjSbzXDT4sJM-RA29SeiZAAteaQL5FMJkNUHTZsw6OkQVJulvBHWi0JYCsa3O_qsz4kERAnjzG8RuF8a69dItdEivNWeUgUxvlQ8jVT7ScDOtEhjyrnIEHHZCJyRleEWUZIpJWxdozS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd680441ef.mp4?token=e68lUvzogQXd8uwArPvIqo8AeseroWhbgAgq1i7zc5qUMQcIheukzKeJqjUCstEiW2scUUaqnPMSlVKlrhNweXMi4neCwhGnS7I17JKMkzSJ59ozSI2x-Ny8sOFHhdEe_I-B_yXg5WPT1DPj3H9PePqYXN9FclWSeYzwX3KUiOgW0KAkFpPab9WF0V9X4zfVgZJDkn_Jbcs6ylda0eAJ8ZtCD_xziJl46oxKFZWoY2YzqXjcZ8iQDu5McYL0_qwHx3btTPYKZasdz0FWlQ71PV1Ccsxyek62zchGTKuNHs6c2FpHmxKTUCGLZa0tAv2fqaMBPNgPAWEdLsYWZDDvJZ9xHCRmapP5OExFoknQXohBxxtKSaMyd4DzrlQsg3B0mizkN4aGtMX9tbK12erv6QdWqRYsYQWFyhaIglXMT60fa8aMIINmjzYFs3MtAoRkGXpRNk7iJdHWNuAWdw2-zc5OJ2bSnG3MsK2k563x7NO1t9Jfu5xET05dZX4rwHJO7BE-d4OxkYwHcG7wq3aCkwN5iPerZx8hjSbzXDT4sJM-RA29SeiZAAteaQL5FMJkNUHTZsw6OkQVJulvBHWi0JYCsa3O_qsz4kERAnjzG8RuF8a69dItdEivNWeUgUxvlQ8jVT7ScDOtEhjyrnIEHHZCJyRleEWUZIpJWxdozS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریق نجات نوجوان، جان یک پسربچه را از دل امواج خروشان نجات داد؛ شجاعتی که حالا قرار است با اهدای مدال از آن تقدیر شود
🤯
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/676345" target="_blank">📅 14:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aefb607a1.mp4?token=lVrUCJhKXLR4gBB226nsUvNthGfOZYxaW7-wyE_UWIfMQH6TtxpjvVpxxJRZ_MJKitQz5dNwuS48W-4TtvWLf-Z-RhUS6HSdJiM_dtOI7fYw6NvS06pwU2o0VGTbKXqK7IPbAjaZWW76dHVy8fv8y7Iq460eFACKXXrFpc0nm1UJyXptea1hoywSnTj-r3eunj0iIkyCP3XML8C6qchZ5CQ8ToIjSkpEwcNYirunDwlSNbeBEnR6J2Gozta1ifiioxfs91Fazdeik8AEQKmi-ExV-1ObyitSTF_KJcImXa2O57yu7DMtvcQMkIbaC8JiCjxYfH9uCYJL2WQPnxGz2V7KIwZPrTQkbWPPghY04Lb3kePo3wdEUHFm-PNSya-Jm8rz2N9XX-qM6SRXzv3ZYgWniYkN4LC0zz55BSwqSRMn54FE4A0j_iRUqjt8rCPo8EE4GKB9nWnf5dBH9qQy29I-Y5By-a5qGaHZx1GtiHTKmGw2xlcD8fA0YII1jPc_x8ocqP-XVpOm8OXefrT3_Cpi7JN7Bo_OSKOboIh0UmxRh0FKbJ8Q36SQjbyCM9dqO1XslbMuuixAaYdaXwEAbNmpLRx1Zr9j8B4YX_GIHxGTHoCmxdVO6k7Dgl2fD7vID_h2fixMrX3SwhrCAKmZfufCA1ADiMtiuTso38jcQYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aefb607a1.mp4?token=lVrUCJhKXLR4gBB226nsUvNthGfOZYxaW7-wyE_UWIfMQH6TtxpjvVpxxJRZ_MJKitQz5dNwuS48W-4TtvWLf-Z-RhUS6HSdJiM_dtOI7fYw6NvS06pwU2o0VGTbKXqK7IPbAjaZWW76dHVy8fv8y7Iq460eFACKXXrFpc0nm1UJyXptea1hoywSnTj-r3eunj0iIkyCP3XML8C6qchZ5CQ8ToIjSkpEwcNYirunDwlSNbeBEnR6J2Gozta1ifiioxfs91Fazdeik8AEQKmi-ExV-1ObyitSTF_KJcImXa2O57yu7DMtvcQMkIbaC8JiCjxYfH9uCYJL2WQPnxGz2V7KIwZPrTQkbWPPghY04Lb3kePo3wdEUHFm-PNSya-Jm8rz2N9XX-qM6SRXzv3ZYgWniYkN4LC0zz55BSwqSRMn54FE4A0j_iRUqjt8rCPo8EE4GKB9nWnf5dBH9qQy29I-Y5By-a5qGaHZx1GtiHTKmGw2xlcD8fA0YII1jPc_x8ocqP-XVpOm8OXefrT3_Cpi7JN7Bo_OSKOboIh0UmxRh0FKbJ8Q36SQjbyCM9dqO1XslbMuuixAaYdaXwEAbNmpLRx1Zr9j8B4YX_GIHxGTHoCmxdVO6k7Dgl2fD7vID_h2fixMrX3SwhrCAKmZfufCA1ADiMtiuTso38jcQYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵۰۰ سال بعد، همان دشمنی؛ پل‌های ایران زیر آتش متجاوز
🔹
دونالد ترامپ در حالی به پل‌های جنوب ایران حمله کرد که این اتفاق برای بسیاری یادآور حملات تاریخی استعمارگران پرتغالی به سواحل و جزایر ایران و تخریب پل‌های این سرزمین بود.
🔹
رخدادی که یادآور تکرار یک الگوی قدیمی است؛ اینکه دشمن، هر نام و پرچمی داشته باشد، در نهایت هدفش آسیب زدن به ایران و منافع مردم ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/676344" target="_blank">📅 14:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676343">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
گام بلند موسسه ملل برای تبدیل شدن به بانک با واگذاری املاک مازاد
🔹
موسسه اعتباری ملل با دهه‌ها فعالیت در ارایه انواع خدمات مالی، از جمله خدمات بیمه‌ای و واسپاری در حال تکمیل فرایند بانک شدن است که در این مسیر اقدام‌های مهمی را انجام می‌دهد.
🔹
در تازه‌ترین این اقدام‌‎ها ۲۴ مرداد در محل این موسسه از طریق مزایده عمومی تعدادی از املاک، مستغلات و قسمتی از سرمایه‌گذاری‌های مازادش را به متقاضیان شرایط واگذار می‌کند.
🔹
این مزایده که فرصتی ویژه برای سرمایه‌گذاران، فعالان اقتصادی و تمامی کسانی است که به دنبال خرید دارایی‌ها ارزشمند هستند.
🔹
این اقدام با هدف مدیریت هوشمند دارایی‌ها، تقویت ساختار مالی و پرداخت تسهیلات به هموطنان عزیز صورت گرفته است.
🔹
همچنین این موسسه که از بانکداری شرکتی رونمایی کرده در تلاش است تا مجموعه‌ای کامل از خدمات مالی، اعتباری و مدیریتی برای شرکت‌ها، سازمان‌ها، کسب‌وکارهای متوسط و بزرگ و مجموعه‌های پروژه‌محور را طراحی کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/676343" target="_blank">📅 14:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676342">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlC1orAtNIBlZe24R8vjHGFnLk6Qu9KIM4QUrTmhGt-NHvhmI2DqnHbKkLDEtHW70CSIo0s0Mbji8t0DkxdR9FYDumB2ULoA5jFiVAnS54L29SOf7qMS-gZQLx9ZHJ05P7aCKVt-MkiZIGGCvkIqmRVx9TNr4ZSDqDjUYPXmyXPFAkfGRMFwsSSCx5t_28Cau3wDccD8S-PIapdxqUpkIYapyvBrHXtf2AJJ1nRkT7T3dIJRTyp4w-lQgCJUbH2IT_oYpv40wAthKGGDx63a2I2ws7cz6QSF81_diySTl55H_lp7ntBROmV-sW6jP6SsX3vRd3msz0c4ja_Vsc6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای تلفات پنهان آمریکا؛ ۷۰ تلفات در ۱۸ مارس، ۲۹ تلفات در ۳ مارس و زخمی شدن دو ژنرال در بندر شعیبه کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/676342" target="_blank">📅 14:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676341">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تیزر قسمت پانزدهم از فصل پنجم
🔹
در این قسمت ادامه روایت تجربه‌ نزدیک به مرگ آقای حسین صاحبی بزاز که در این تجربه متوجه اهمیت بسیار زیاد محبت نسبت به هر موجود یا شی شده‌اند و اینکه هر انسانی مسبب تمامی اتفاقات خوب و بد زندگی خودش است و همچنین کسانی که از رزق مادی در دنیا گله‌مند هستند بخاطر سبک شمردن نماز صبح‌شان است و همه کسانی که مهر و محبت اهل بیت در دلشان جوانه زده باشد توسط بانوی دوعالم در آخرت مورد شفاعت قرار میگیرند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حسین صاحبی بزاز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/676341" target="_blank">📅 14:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8aaabca7.mp4?token=LaOj-s9H2-ZNaCMzdqMnTFVSVApAME0IvvNRZvgvbSuWm86OBFNLIZyNQ5wGmwbwjH1gxnqm7ChHhlILCXyp3E5ZetqFKW1SRp97zciccXNMUoJM2xVYOuXB7JrVbHgzxBV4iG84TMTaoZ0Q-U0FC7Vh4sIAFO346BV_N62NnRZkhBU3ijwWRyC46thc651i9bUzp-cL7zW33gl9iXLePuWgZ277u7jGxpa2-um579LzQs0oRncHGd0tATDjIUov0OTVR7G7XRqbulMNrvLCiLH6qwLQKSw-oIin0vKDeyimzZnADYcLXTQge1WcFQgGHI71odwKXfLLolPY_MpoGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8aaabca7.mp4?token=LaOj-s9H2-ZNaCMzdqMnTFVSVApAME0IvvNRZvgvbSuWm86OBFNLIZyNQ5wGmwbwjH1gxnqm7ChHhlILCXyp3E5ZetqFKW1SRp97zciccXNMUoJM2xVYOuXB7JrVbHgzxBV4iG84TMTaoZ0Q-U0FC7Vh4sIAFO346BV_N62NnRZkhBU3ijwWRyC46thc651i9bUzp-cL7zW33gl9iXLePuWgZ277u7jGxpa2-um579LzQs0oRncHGd0tATDjIUov0OTVR7G7XRqbulMNrvLCiLH6qwLQKSw-oIin0vKDeyimzZnADYcLXTQge1WcFQgGHI71odwKXfLLolPY_MpoGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این آموزش بفرست برای کسی که عاشق شال کشی و استایل کردنه
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/676339" target="_blank">📅 14:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676337">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2-TWfZtt86UJnoDiFEWwy2ZFm1R5PewJ_eLmMI528qrvpupCGj9eqsUZRcbb0J6h-f-EXtk3vmjaEBPKGYznZJj_gyGLhtCVV4TdM2xzqvWgYKExZfgbol1sCyCzfjPfvRW8vxJCzoy7onOxOZPzg8rd14ShXiZzdpHWtt33-miXcWEPhDeFOTVJzUEP5M-L0mQ9IbqGug7FYgZOQV7Nlns7KnVcdmKu3F4AlCpJFJ9n0EjlANhwPtAPOHhuKP5CDiUBc181EUujB9joRj62uUdj52iT-LGVdKk4iZWUZgzn32qg07W4AJ8jKDeuKfCWrdL73b3tg_roKcwizRQgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: حوثی‌ها در نظر دارند برای کشتی‌هایی که از دریای سرخ از طریق تنگه باب المندب عبور می‌کنند، هزینه‌هایی وضع کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/676337" target="_blank">📅 13:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676335">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ممنوعیت واردات لوازم خانگی شکست خورد/ نماینده بندرعباس: وقت بازنگری جدی رسیده است
احمد مرادی، نماینده مردم بندرعباس در مجلس، در گفت‌وگو با ایسنا، سیاست ممنوعیت واردات ۴ قلم لوازم خانگی را عملاً بی‌نتیجه دانست و هشدار داد ادامه این روند به ضرر مردم، تولیدکننده و دولت تمام می‌شود.
🔹
شکست در عمل: «قرار بود ممنوعیت به تنظیم بازار کمک کند، اما نتیجهاش افزایش قیمت، کاهش تنوع و رونق قاچاق شد.»
🔹
نیاز بازار حذف نمی‌شود: «وقتی واردات رسمی بسته می‌شود، تقاضا به سمت کالای قاچاق و فاقد گارانتی می‌رود؛ مردم پول سنگین می‌دهند، اما امنیت خرید ندارند.»
🔹
معیشت ساحل‌نشینان در خطر: «در هرمزگان، زندگی مردم با ته‌لنجی و تجارت خرد دریایی گره خورده؛ نمی‌توان هم از اقتصاد دریامحور گفت و هم راه معیشت آنان را بست.»
🔹
تفاوت قاچاق سازمان‌یافته با تجارت مرزی: «یکسان دیدن این دو، خطای سیاستی است؛ باید برای تجارت خرد مرزی چارچوب قانونی مشخص کرد.»
🔹
تضعیف رقابت و تولید: «هیچ تولیدکننده‌ای در فضای بسته به کیفیت مطلوب نمی‌رسد؛ حمایت واقعی یعنی کاهش هزینه تولید، نه حذف رقابت.»
🔹
ضرر مالی دولت: «با توقف واردات رسمی، دولت هم درآمد گمرکی»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/676335" target="_blank">📅 13:45 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
