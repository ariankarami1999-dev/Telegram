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
<img src="https://cdn4.telesco.pe/file/b1MYv6YLwpoFWyMIZLBnPD24CLM0L6ugBUnV5nML0E86Oj-FgEFl9ymInWdlKKR_-Ycew9KbdKaPahTliDaGpJIe6LLmmefVconyty7BS-0pH7yPzcanNNue2J0Q3J0TV26bho4OdromKBv4oOyT37Wub6YqrwuQ2p3YngvXGKzr6MmZJAyTzKvpXL7oA8d2Yc858W67ZA5slhWZyAADBLbz0zQPapc9RQgdiFmsFTHgT_J99AVYN9XIGk2-SQdtXEzfcpoijZ25y2pE4OqQyH48kPg9hHorqA6YjJnpQHHg7zS2KlVK4tsxMYNVXYoNC28JVXyCUk7YirZzJF5wnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.56M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 13:31:37</div>
<hr>

<div class="tg-post" id="msg-659243">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
خروج ناو هواپیمابر شارل دوگل از منطقه
🔹
ناو هواپیمابر فرانسوی «شارل دوگل» پس از پایان دوره مأموریت ادعایی خود در مدیترانه شرقی و دریای عمان، در حال بازگشت به پایگاه نظامی «تولون» در فرانسه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/659243" target="_blank">📅 13:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659242">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdO656ujeZGWWKAh7gP4ZTaAYVksjgeCH92MK66HjILv15CWxTQKEJZmGky7E6vSvOXsxsGbDCyqoZ9VIzyf2W_UyERBlow2szSKH5HM5SwKZ1KW3wP920ugHp79BaB_mQdJXyzDPkBgPxUoYng7vd8CrwMI4WkLFE81ImNFuIacc3tBJREyb_09QlKOgMsnxhM5u4y_9SdmuMxVOue9BdBxG_wq0YOhaTonaooQ_0x2m8cjzZgeo6XhfFXvySouqXNqQaH7LElSmGwadiAB0WlYxb1lSrCKztwcs6lM8ouPGd3tI1Iv544lO51cjV4cbGyuWzNPuf2aryL4COF1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضاییه: دشمن به مخدوش کردن وحدت و انسجام ملی چشم دوخته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/659242" target="_blank">📅 13:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659241">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حاجی‌بابایی: دولت وضعیت استخدامی معلمان را تعیین تکلیف کند.
🔹
آموزش و پرورش: امتحانات نهایی از ۲۱ تیر برگزار می‌شود.
🔹
شنیده شدن صدای انفجار ناشی از مهمات عمل‌نکرده در تبریز/جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/659241" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659240">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2583a92d5f.mp4?token=vEHOlmoQr3FYU1hgpiy0yyTKBmwJ2MkygIVkYQVAOoHg3bLwYgsp2wYzUvEEUHokTb9dACVZm56hBcfTYYt_ua6FxsDF_3d12i6kZY-lxC1g3K9VJjgs-_ASMVaud2-fHXQSK5_2GQulL3KZ6_2GBSx_m7zo22F7KrSfEwqHTPr9Q2QJiuJYegZmX64rLCq1_UzXe7kvYNhrCPh_7iLxB6v2a8dukCghgYuphbosag0TrTPZuUhowiannsG7dcLicaV6BCD39leizwjZFRhcQzemgX7l-Og4rgYfpRAm1aZ5mTO1Wjug-5zQXMoYXpMJivBqHa8GwUBdVO8Fzp2JYRM5UvZVfPZs-nLD3db-4SpPoT9wsp5TV-KHWQPsWATy3iaGSsbC0orAA1Q5ze5021eH6BhRCRdbBfut3XByg2XRu_p2wZRtkylN5uoEzJaAnz0iv5-UyYMBK81jsKxlMYhRonpt56uCY9GvXbBH6kQdP_3w5YZKe7oM2-djBf_OHVDmPw-KgW9BM7VScDPS5_h7-YrN1JUjMpDlNGL8VP5oJkXOPW3mHAkjP2vl6sXN2jO3TrOXsvjnQbWI1FUfEwlIt0_R2y2Rgw0j-i7w5UClB7XDKEMYTdPw75MsCsnsjQTs3PTwKfVUIKgJ8QDR1pNIlDglfpXRJ-gPQAvhI18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2583a92d5f.mp4?token=vEHOlmoQr3FYU1hgpiy0yyTKBmwJ2MkygIVkYQVAOoHg3bLwYgsp2wYzUvEEUHokTb9dACVZm56hBcfTYYt_ua6FxsDF_3d12i6kZY-lxC1g3K9VJjgs-_ASMVaud2-fHXQSK5_2GQulL3KZ6_2GBSx_m7zo22F7KrSfEwqHTPr9Q2QJiuJYegZmX64rLCq1_UzXe7kvYNhrCPh_7iLxB6v2a8dukCghgYuphbosag0TrTPZuUhowiannsG7dcLicaV6BCD39leizwjZFRhcQzemgX7l-Og4rgYfpRAm1aZ5mTO1Wjug-5zQXMoYXpMJivBqHa8GwUBdVO8Fzp2JYRM5UvZVfPZs-nLD3db-4SpPoT9wsp5TV-KHWQPsWATy3iaGSsbC0orAA1Q5ze5021eH6BhRCRdbBfut3XByg2XRu_p2wZRtkylN5uoEzJaAnz0iv5-UyYMBK81jsKxlMYhRonpt56uCY9GvXbBH6kQdP_3w5YZKe7oM2-djBf_OHVDmPw-KgW9BM7VScDPS5_h7-YrN1JUjMpDlNGL8VP5oJkXOPW3mHAkjP2vl6sXN2jO3TrOXsvjnQbWI1FUfEwlIt0_R2y2Rgw0j-i7w5UClB7XDKEMYTdPw75MsCsnsjQTs3PTwKfVUIKgJ8QDR1pNIlDglfpXRJ-gPQAvhI18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاصه بازی جذاب برزیل و مراکش
🔹
🇲🇦
1️⃣
🏆
1️⃣
🇧🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
▪️
آینده‌ای طلایی با سود طلایی
▪️
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/659240" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659239">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
کنکور سراسری ۲۹ و ۳۰ مرداد برگزار می‌شود
وزیر علوم:
🔹
کنکور سراسری سال ۱۴۰۵ به صورت قطعی در روزهای ۲۹ و ۳۰ مردادماه برگزار خواهد شد و با توجه به زمان‌بندی جدید، به احتمال زیاد دانشجویان جدیدالورود از نیمسال دوم تحصیلی وارد دانشگاه‌ها خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/659239" target="_blank">📅 13:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659238">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
منبع آگاه: تصمیم نهایی تهران دربارۀ تفاهم‌نامه در دست بررسی است  یک منبع آگاه:
🔹
ایران هنوز تصمیم نهایی خود دربارۀ تفاهم‌نامه پیشنهادی را اعلام نکرده است.
🔹
بررسی ابعاد سیاسی، حقوقی و فنی پیشنهادهای مطرح‌شده همچنان ادامه دارد./فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659238" target="_blank">📅 13:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659237">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
هشدار سازمان بازرسی به بانک‌های دارای عملکرد نامطلوب در پرداخت وام ازدواج و فرزندآوری
؛
اخطار قانونی صادر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659237" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659236">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei8PXk53ubTNRVcCB7WARMxxUsmM5HLA2frhtU0Ke7jLRXPzJe0UUdt2tXrKSs6bZDQ8dAx829j-z_QMdYwxHBnlwqtiKh8OSye9QuLzol3b_1ZSoayvzEM0zmo7QN84_OROOH8wUcvcNXLz5_gpBlCfgmNEU-xBE32J2_ao1ui-0Xgg19HwoqoP5P7UYWUShBCv6txcORv83XEmdOYUDxhwjWzOHayjkEDpM_x7jO8VS23nz-5TkD-UrfNmBFM5GQADnIpNE1mNnfzH5raXgXCA4mLbBO0xOnB0j7eZf-EqkKHIuIvpnIXNlKefxTnHoTiJ3VW8bARAuqf27yp8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ دقیقه‌ای که آب ۳.۵ میلیون نفر را تأمین می‌کند
🔹
با کاهش ۴ دقیقه‌ای استحمام یک میلیون نفر، ۱۱.۸ میلیارد لیتر آب ذخیره می‌شود؛ معادل نیاز اصفهان و شیراز. در جنگی که منابع ما با فشارهای اقتصادی هدف قرار گرفته، اقدامات خردِ جمعی را در خنثی کردن نقشه‌های دشمن دست‌کم نگیریم.
#سنگر_آب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659236" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659235">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM5JaZDX1f64SjxgYNlfaP0qCXHEtOE0plGwXI1smrkvWONbHu2sdE6HhssHQxVrmTWzrPQGHMM4uTJCdngoxBkrYP6a_Nb7rxJxZPEIIzZnZYttNjH0fUZKe5PxHpvr9EDPbxKIi4HEEgrFJyePJVnEEdVOQ2HAPOWl3RpcILKRz6VhuRKRhg3z1tc0sd50yDt4nC0Lay3EOdmPOKTlpEJk8c4WW9eErXEJLQgCt9qIs9YR0cal_0QqkWKyOjAGzvcTB1Cu6wS-zPYkyFP4kNhorXSRF-jM1yyXbsecH5jWfE6KPhDqHnNnjVpUWWLzcEs-aVhENgNh2OwI_XFEUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر با تساوی مقابل سوئیس، اولین امتیاز خود را در ادوار حضور در جام‌های جهانی کسب کرد @AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/659235" target="_blank">📅 12:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659233">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bfd5ffba2.mp4?token=a0Tp5tVozcOF_HfftgQx6X-I25Y-xoGnBP7ixDFs4h064hneuN5Y92TFzFnQ1akk-6qmOBlnb3OaSo55NBB8QBE83JQXF8ujLj_zQvH7cUjouUJZ4xsGbZLhADD0phl9ASlYU8MDI-tUMu1Rt_ej60M3fOscZfTkaHu3HoWpCO00EZZZNlEp8IiHsk7gBRCcM_wy0Q1qs-cALYM-T_P5OUeCaJXiZmgGvG4R4c_4wL3eRDwTfuHRwxk9FKYYx9HEHSMNUMEaDMOpTWcdoq1VZURPBG-Y3S46_zsx_Qh70p1n1a3_j2Og1UuTd_UQiW4DoSu5HyexUJp9wWRSaNQ_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bfd5ffba2.mp4?token=a0Tp5tVozcOF_HfftgQx6X-I25Y-xoGnBP7ixDFs4h064hneuN5Y92TFzFnQ1akk-6qmOBlnb3OaSo55NBB8QBE83JQXF8ujLj_zQvH7cUjouUJZ4xsGbZLhADD0phl9ASlYU8MDI-tUMu1Rt_ej60M3fOscZfTkaHu3HoWpCO00EZZZNlEp8IiHsk7gBRCcM_wy0Q1qs-cALYM-T_P5OUeCaJXiZmgGvG4R4c_4wL3eRDwTfuHRwxk9FKYYx9HEHSMNUMEaDMOpTWcdoq1VZURPBG-Y3S46_zsx_Qh70p1n1a3_j2Og1UuTd_UQiW4DoSu5HyexUJp9wWRSaNQ_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمدین آمریکایی: تنها کاری که آمریکا می‌تواند در مورد ایران انجام دهد این است که دمش را روی کولش گذاشته و فرار کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/659233" target="_blank">📅 12:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659232">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3ceaef5a.mp4?token=jOoh34hPU16Rxdw_ePKClTSZfn1VaUkiBYVgoLcICc4vqckSvx8mvcX011okDZq_79_9mh6tVIWoHruj2bEu26fOJPR2Q_HfXm6Y4siuntpJ4pRjFhTl9NtkHXOHrvzwQnJnNKRhonmm6IiPA5uUp5FIaKT3oikeg_tT_V-I6-SCAT5pZnZfnZ9ILJqaHw14QjW_z6xezCMGZuLtMWYW-nKPRlv25m4UuJF6Uixb05oxtUCQnIj8BZouP_apBCBotd829n4RXld3oFqoxHOs_41HFQKi6iykEa7an40LHi5bKl1r4VAL5i71o6j_elPdp25KaIM59rwP-x3Ijf6CyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3ceaef5a.mp4?token=jOoh34hPU16Rxdw_ePKClTSZfn1VaUkiBYVgoLcICc4vqckSvx8mvcX011okDZq_79_9mh6tVIWoHruj2bEu26fOJPR2Q_HfXm6Y4siuntpJ4pRjFhTl9NtkHXOHrvzwQnJnNKRhonmm6IiPA5uUp5FIaKT3oikeg_tT_V-I6-SCAT5pZnZfnZ9ILJqaHw14QjW_z6xezCMGZuLtMWYW-nKPRlv25m4UuJF6Uixb05oxtUCQnIj8BZouP_apBCBotd829n4RXld3oFqoxHOs_41HFQKi6iykEa7an40LHi5bKl1r4VAL5i71o6j_elPdp25KaIM59rwP-x3Ijf6CyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمیشن با نقاشی دیواری بر پلی در کالیفرنیا!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/659232" target="_blank">📅 12:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659231">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
مشکل خدمات بانک‌های تجارت و صادرات رفع شد  شرکت ملی انفورماتیک:
🔹
طبق آخرین گزارش‌ها درپی اختلالات به‌وجود آمده در ۴ بانک ملی، صادرات، تجارت و توسعه صادرات، مشکل خدمات کارت های بانکی بانک تجارت و صادرات رفع شده و تراکنش‌ها با موفقیت درحال انجام است.
🔹
موضوع…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659231" target="_blank">📅 12:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659230">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO-VDV_JbByoNHlMlgc38K-FREOQRagFFC_CuitUClzCj0vBj6jm2lmQohjuKIvw_RSu4GfD33OsWlA1YBORDN_eQNrR9YFfJo5ioRhzmfvv4tiS-7mKceAV1mL-WVxPTPRUvFujYibgWLtruWtpYSz6c6iDbCnIjY4eHg7bUl03MUBUjRbzKxSXNoiKDQaKlBiL5WYw_V4iij8HrQgIyTg8QWpzH9w5qqHl0Yy5CDvo4YHZ_qsUo7zk8J3BOSfZ1CfsK-aaoNJW0V3lCdIFWhaIhRcAl33tGOQgQt-i9AnkZw33HeZaNcjQcJkSH4XyYPb0pUFkEi5Y6PJHRnJxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس از ۴.۸ میلیون هم عبور کرد
🔹
شاخص کل بورس امروز با رشد ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید و یک رکورد تاریخی جدید ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659230" target="_blank">📅 12:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659226">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae92df0369.mp4?token=MRr47eVQBuCLuAklazw9aRud7NeprxU8YzQzH_ov7AL-Ih1i4fWsWluuCCoemzKQrHBN3Bt0sTxBzZellxRmzv79gVwOv1OTXDw5r6FQ4aEZxRs8OnyY0FvpvdsMgxD4GYHGXivF7gxZanbhYoiX9EiSZgkAAJo6nnoUbD_5713CcuAKtq1Sm6u9Q1J1z89J3QBFxhBVJXj5lVoj6Qz3UACULkyGruzdzWKnpkIBgSW28nM6aIa2Jf-8MIQWtrCdelKeqadjnCDT88sYAI01wmU1ceHD7YoHFJQp8IewHd-yfxjdNmqjjtrsnMOSlmz6OfFg7WPGBeJQbyXXSTr4Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae92df0369.mp4?token=MRr47eVQBuCLuAklazw9aRud7NeprxU8YzQzH_ov7AL-Ih1i4fWsWluuCCoemzKQrHBN3Bt0sTxBzZellxRmzv79gVwOv1OTXDw5r6FQ4aEZxRs8OnyY0FvpvdsMgxD4GYHGXivF7gxZanbhYoiX9EiSZgkAAJo6nnoUbD_5713CcuAKtq1Sm6u9Q1J1z89J3QBFxhBVJXj5lVoj6Qz3UACULkyGruzdzWKnpkIBgSW28nM6aIa2Jf-8MIQWtrCdelKeqadjnCDT88sYAI01wmU1ceHD7YoHFJQp8IewHd-yfxjdNmqjjtrsnMOSlmz6OfFg7WPGBeJQbyXXSTr4Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق‌ کردن زلنسکی از حملات پهپادی به روسیه
🔹
رئیس جمهور اوکراین با انتشار یک فیلم اعلام کرد که پهپادهای این کشور در عمق خاک روسیه به یک تأسیسات نفتی در یاروسلاول حمله کرده‌اند و این عملیات باعث اختلال در ۶ فرودگاه و اعلام هشدار حمله هوایی در ۲۸ منطقه روسیه…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659226" target="_blank">📅 12:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659225">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4dd5e434.mp4?token=DtVhXG7jXkEFez0P87llOaXgIeifl3c7pqOqqr-dsupr40MHSwBggVx26vnZ329WPDPOgXDCvTTqcocCMUAimxJvKUif0BYIycWme86xvnuRK1dOIRBzIjILdurvVhTzvoPfA1LbcLaiNKn9DGsrAIrsZOxLziwDzm8C3eXPuJdUm8SwiYklyLyOw6lHoBokZm2ln_GSvy1_mWghQE2X96vMEm3vQUPcYl0Nkk_hzGmYHNu9o2IlnltVyeKNCHdk9-N_cdkEnYfF7-RhyC-NBnmRur-BkDBamPWXL4Dp3zJVliYBJrR4Q18blF7-AICQ6C9szLRCdoLhm5Ku2u3CwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4dd5e434.mp4?token=DtVhXG7jXkEFez0P87llOaXgIeifl3c7pqOqqr-dsupr40MHSwBggVx26vnZ329WPDPOgXDCvTTqcocCMUAimxJvKUif0BYIycWme86xvnuRK1dOIRBzIjILdurvVhTzvoPfA1LbcLaiNKn9DGsrAIrsZOxLziwDzm8C3eXPuJdUm8SwiYklyLyOw6lHoBokZm2ln_GSvy1_mWghQE2X96vMEm3vQUPcYl0Nkk_hzGmYHNu9o2IlnltVyeKNCHdk9-N_cdkEnYfF7-RhyC-NBnmRur-BkDBamPWXL4Dp3zJVliYBJrR4Q18blF7-AICQ6C9szLRCdoLhm5Ku2u3CwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حزب‌الله از حمله به سایت نظامی «بلاط» متعلق به ارتش رژیم صهیونیستی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659225" target="_blank">📅 12:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659224">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuHEtakyfiNDvVUbhuJ_nyyBSfkxkk6L5UMeRpJ1SNdEHDExfPqJt_x81k0TLr6c1GNPUBHLb6i2q7oFdh9wBsyApD87Qqr1s3EKV3Bz00WJw1PgEvaOaP6KBHm8TMVRMZto6OmudTB58hzvAS5WDz1ibvJKcsSEFBlpvHb-ceyx1ZFTSqUVSJ_3R8vCpX_zjGhI5sPrxkvMqLugsn34iddHvdQezwHNsQoLt9334ylBrkOlCK7avM8Ov9GFAyohnD1Ui9XS8ecdZNEthiiGyXdJmku9Fl9-SZfbLmQltrVR6c9Y_n-MX_OH2Q5eOLDCa_33oIvsJvpJfHsM7NXJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای تشخیص طنز، تبلیغات و خبر جعلی #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659224" target="_blank">📅 12:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659223">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
انگلیس صبح امروز در کانال (احتمالاً کانال مانش) به یک نفتکش متعلق به «ناوگان سایه» حمله کرده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659223" target="_blank">📅 12:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659222">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر راه از تخصیص سهمیه سوخت و لاستیک به کامیون‌‌های فعال در حمل کالای اساسی خبر داد.
🔹
ثبت‌نام آزمون کاردانی به کارشناسی ناپیوسته از امروز آغاز و تا ۳٠ خرداد ادامه می‌یابد.
🔹
انهدام مهمات باقی‌مانده از جنگ رمضان امروز در سردرود آذربایجان شرقی/جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659222" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659221">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb865ba92.mp4?token=UBpJl9DjbEuDbMDvKwSYP3WBKu8PoOjvvIt28aALCCTgXlf2J1T2bv1xNeZS4PdCb5p-i3J9Mfyp89fKo34kEl8vaEhVvGeLaykwMzHZSirWibvxru3290wpS920MH8mgMRu7q2XbunNYwk6HHIBAb3ybNLQVSFz8tTQXBIBZGHGRz78NH2q_wWS-ts6MMSRkczBIzM9v8sTiiBzYFzBbfWv-rxNV-TVaHdLeD91TIMeNBJUenkEjEuGHlnicIsAQ0aRum9a3-H0N8tnI7-EWEufGFCFyES_8Fmteh9qvbVbCUMfitX_gbSEqs6xnArd7sntBe0WzJUtKgSInx_tGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb865ba92.mp4?token=UBpJl9DjbEuDbMDvKwSYP3WBKu8PoOjvvIt28aALCCTgXlf2J1T2bv1xNeZS4PdCb5p-i3J9Mfyp89fKo34kEl8vaEhVvGeLaykwMzHZSirWibvxru3290wpS920MH8mgMRu7q2XbunNYwk6HHIBAb3ybNLQVSFz8tTQXBIBZGHGRz78NH2q_wWS-ts6MMSRkczBIzM9v8sTiiBzYFzBbfWv-rxNV-TVaHdLeD91TIMeNBJUenkEjEuGHlnicIsAQ0aRum9a3-H0N8tnI7-EWEufGFCFyES_8Fmteh9qvbVbCUMfitX_gbSEqs6xnArd7sntBe0WzJUtKgSInx_tGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان تلخ مرد عنکبوتی یمنی
🔹
«قعقاع بن عنتر»، کوهنورد و ماجراجوی سرشناس یمنی، در جریان انجام یک نمایش خطرناک، تعادل خود را از دست داد و به داخل یک دهانه آتشفشانی سقوط کرد و جان باخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659221" target="_blank">📅 12:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659220">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808b08b6f4.mp4?token=tHWyG8DJO7QQkcVn_4Ltk4mlmqiKSnCmJpgwyzPnUo-RYb6ahPthn0sSn6dNYIOY1Y9aZ7el1aA6syGwfwfj8sP6ZcFPLTt4-1meC9iVc4khGzJWl6xTSaJDZNPghB1S9ls24FTmA3ONVM2Qeld--oRWEV_tMAK7nqVb3q5VAblLevK8z1Z-bQBJvKecBSoeJZfZjuA2gYPl4ncdmfS9oDmESvinMVV3MlX02yJbpp5gqVDG5VO3Qyq5qrYcweE3VdKDQruU0sfmMbmyLs6opt2iB-5SlOPyxsJtaI70pfzPeNt2fnb0ZAEhmtipq-PerN162l89E7e0sKTwmbjnRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808b08b6f4.mp4?token=tHWyG8DJO7QQkcVn_4Ltk4mlmqiKSnCmJpgwyzPnUo-RYb6ahPthn0sSn6dNYIOY1Y9aZ7el1aA6syGwfwfj8sP6ZcFPLTt4-1meC9iVc4khGzJWl6xTSaJDZNPghB1S9ls24FTmA3ONVM2Qeld--oRWEV_tMAK7nqVb3q5VAblLevK8z1Z-bQBJvKecBSoeJZfZjuA2gYPl4ncdmfS9oDmESvinMVV3MlX02yJbpp5gqVDG5VO3Qyq5qrYcweE3VdKDQruU0sfmMbmyLs6opt2iB-5SlOPyxsJtaI70pfzPeNt2fnb0ZAEhmtipq-PerN162l89E7e0sKTwmbjnRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق‌ کردن زلنسکی از حملات پهپادی به روسیه
🔹
رئیس جمهور اوکراین با انتشار یک فیلم اعلام کرد که پهپادهای این کشور در عمق خاک روسیه به یک تأسیسات نفتی در یاروسلاول حمله کرده‌اند و این عملیات باعث اختلال در ۶ فرودگاه و اعلام هشدار حمله هوایی در ۲۸ منطقه روسیه شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659220" target="_blank">📅 12:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659219">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
قطع دو ساعته برق در راه است
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی:
🔹
توانیر امسال اعلام کرد ۱۲ هزار مگاوات کسری برق دارد در حالی که سنوات گذشته بین ۱۸ تا ۲۰ هزار مگاوات کسری اعلام شده بود.
🔹
برآورد ما این است در ایام گرم سال، حداقل دو ساعت قطعی برق خواهیم داشت./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659219" target="_blank">📅 12:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659218">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
زمان برگزاری آزمون ارشد ۱۴۰۵ تغییر کرد
سازمان سنجش:
🔹
به‌منظور فراهم کردن زمینۀ حضور متقاضیان در آیین وداع و تشییع رهبر شهید انقلاب، آزمون کارشناسی ارشد در روزهای پنجشنبه و جمعه ۲۵ و ۲۶ تیر برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659218" target="_blank">📅 12:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659217">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksBElsag9c4AptEMksjIdDEXq5D0cP72_Rr_hFpXbstFsL7e7-SZaCDGYZyvxhWMM8W6awuF-Gb2salpPfQbtp8SmsONN3nEwqP-viL_ROyBmZOKFFlZTd9YcHf_eeg_Xo-lWyqJzM9vJy-QKTVlRcyGEG08lF3x_o40NNslwiX5WweAYB2cqb1T17wRpf9pEJ_rsoi7aobOMzFKSFc-s47gOSPbslb2Blf0Oh0AdB571SMLqCMrrXjp_3QX3-S9Jd0ggyOIiTiBUd4qkCeSx2RR2SAsGIaBgKbaExhiW7F6CpW1irIrulrV4doVOT4P74lNw8FyfGHXteMlxHmhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارزش دلاری بورس از مرز ۹۲ میلیارد دلار عبور کرد
🔹
ارزش دلاری بازار از مرز ۹۲ میلیارد دلار عبور کرد و در تایم فریم هفتگی همه چشم‌ها به هدف ۱۰۵ تا ۱۱۰ میلیارد دلار دوخته شده است.
🔹
امروز سفارش خرید ۵۰ همتی در پیش‌گشایش بازار تب و تاب بورس را بالا برد و در حال حاضر ۸۳۰ نماد بورسی معادل ۹۹ درصد از کل بازار سبزپوش و مثبت هستند.
🔹
به نظر می‌رسد موتور بازار برای صعود دوباره روشن شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659217" target="_blank">📅 12:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659216">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWMjUDJV3MEvb8mEcT4d9Z1yFX02LJkFgfqR7gIxaKSF2juva36tZ_QBAW5mRLlj_PPp1JJcjzGL1CVWeKZrpoRYsIf4d5h6B7zKTHfnR3peX_j2pAiIgsFvu6QnnQB0GgDcqN-l3ecPz4XGiWppfBQW_uZRjF2iBb46hnKtEdT6mRvoSST2RdhOw_sq1EBB5-8I3fSKfkkVhmiiCIDgJzCZZKjIpt7m2zoA0epQrs8KqcL4EFVjn41qs6gaPvbkub3Z8HBSUkn1RtYW0C5DSyaUcBvPA_tnxKfi19hEJCh7yhEioUUnYjIofAzYxKtZVmwyQV_nrFRFv6p6P0NISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیدحسن خمینی: تخریب مسئولان عالی‌رتبه کمکی به حل مسائل نمی‌کند
🔹
کشور با دعوا، اختلاف و سخنان تند به نتیجه نمی‌رسد و باید به خرد جمعی و تصمیمات کلان نظام اعتماد کرد؛ همان‌گونه که در دوران جنگ با اعتماد پیروز شدیم، در دوران صلح نیز باید با همین رویکرد پیش برویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659216" target="_blank">📅 12:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659214">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa16d263ca.mp4?token=eBx38funACo3kaPTb5P8dmfAIkC6a_tm5ZIfi06PYQasKvNSUqQwM6UbbNqFhh5BOmenrcmtjtqz_V_tS_H3xBKsHM9Q6ljapUmWzWtT4umf8wX8G7DllqbsvICcn02Q4B0pHq1sRPq4wcQd7J7wCkWUn-QuuZfi-5dTiOKzC2rg570X0qAp5_XMsaQEBINoP9_ujZjLQgE2TVUsq-N5UMMVCnsp5sO0-fBjvnw7Ho-s2LT86pmGvVcGIe4V9hzpTfJ11vdqUKcOlrwJ1w5upw0Z8aEKuWisH6wC4VhEwV-UJKKzEUyibLI3XkjXmOkBdIwcgZDY2MmwXPZKl-Euyq2ypL8Sp3bHnGI6wp500PSTcVst4bwgpcmLf_4nEONGs659kQ3YLpbQxc6tjSd5I81b7BjjNVCfelvB0IVdWpdXaGYONuIKuslKZKgVIBQW9cCpJfRNFCmox8DBDwp_Eox0Swurnv6Ly1vQ6wWVNPeJu5xT4U7OlcfVg3bcOfp6IjvqJnllx5J0Bx4ZWcc0HwhdChz5Sw7r5fkMLS_whV1wY3CvAg-mjIZ__Z38A9EJAzhPQIeBgeo8sFKtCpA0YFr3S-zqzt3j-TdhcoWwGnEo5_1JjEse9CpQaFVbVVkWkYIRGlMK93feHZc0Ru0Zoxddqm7P5u0Ro2SVy2gBmoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa16d263ca.mp4?token=eBx38funACo3kaPTb5P8dmfAIkC6a_tm5ZIfi06PYQasKvNSUqQwM6UbbNqFhh5BOmenrcmtjtqz_V_tS_H3xBKsHM9Q6ljapUmWzWtT4umf8wX8G7DllqbsvICcn02Q4B0pHq1sRPq4wcQd7J7wCkWUn-QuuZfi-5dTiOKzC2rg570X0qAp5_XMsaQEBINoP9_ujZjLQgE2TVUsq-N5UMMVCnsp5sO0-fBjvnw7Ho-s2LT86pmGvVcGIe4V9hzpTfJ11vdqUKcOlrwJ1w5upw0Z8aEKuWisH6wC4VhEwV-UJKKzEUyibLI3XkjXmOkBdIwcgZDY2MmwXPZKl-Euyq2ypL8Sp3bHnGI6wp500PSTcVst4bwgpcmLf_4nEONGs659kQ3YLpbQxc6tjSd5I81b7BjjNVCfelvB0IVdWpdXaGYONuIKuslKZKgVIBQW9cCpJfRNFCmox8DBDwp_Eox0Swurnv6Ly1vQ6wWVNPeJu5xT4U7OlcfVg3bcOfp6IjvqJnllx5J0Bx4ZWcc0HwhdChz5Sw7r5fkMLS_whV1wY3CvAg-mjIZ__Z38A9EJAzhPQIeBgeo8sFKtCpA0YFr3S-zqzt3j-TdhcoWwGnEo5_1JjEse9CpQaFVbVVkWkYIRGlMK93feHZc0Ru0Zoxddqm7P5u0Ro2SVy2gBmoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب گسترده در جنین توسط نیروهای اشغالگر صهیونیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659214" target="_blank">📅 12:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659213">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
اعلام جریمه مخدوشی پلاک در پایتخت
معاون پلیس راهور تهران:
🔹
جریمه پوشش پلاک ۷۰۰ هزار تومان و جریمه نداشتن پلاک جلو یا عقب و همچنین ناخوانا بودن پلاک ۴۰۰ هزار تومان اعلام شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659213" target="_blank">📅 11:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659212">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس انجمن تجارت الکترونیک: نگرانی درباره دارایی‌های دیجیتال بی‌مورد است؛ تحریم صرافی‌ها شامل کاربران نمی‌شود.
🔹
ستوان سوم حسین رسولی در درگیری با پ.ک.ک در چالدران به شهادت رسید.
🔹
وام بازنشستگان تأمین اجتماعی افزایش یافت و از تیرماه پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659212" target="_blank">📅 11:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659211">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98197c2078.mp4?token=h6c1BhZiBvTL2oyV5-PFw9qx-LbVR2lGMFQ8ms4Ll_Bzz_TbTPtCHwnnWqQ0TbXKuRvqkSxZ8VX2BeRPDlVge4kGavvae9KGNMXyrnTxAjF15eMMHgfd_YiwV8X-TQGbWC3-6pJOvLev-tZkt6AAxgI4brVki0ss4yrEzcBySaLDe8REzmUHUlHDzkwDdq8R5GpvMRyYT6bImHir-KY4o6E34Ubw9ZMABqkv4dE7CSxsmyZEJYmI-zXu1PZYfRLG07RhFoO3fTeIybm88QXEJu2AlwH6oq6LZ_0m95l7abMbmtDlRDi3C_mW6G_eFAG0DAdQxtS_ki52iC_kbm1BQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98197c2078.mp4?token=h6c1BhZiBvTL2oyV5-PFw9qx-LbVR2lGMFQ8ms4Ll_Bzz_TbTPtCHwnnWqQ0TbXKuRvqkSxZ8VX2BeRPDlVge4kGavvae9KGNMXyrnTxAjF15eMMHgfd_YiwV8X-TQGbWC3-6pJOvLev-tZkt6AAxgI4brVki0ss4yrEzcBySaLDe8REzmUHUlHDzkwDdq8R5GpvMRyYT6bImHir-KY4o6E34Ubw9ZMABqkv4dE7CSxsmyZEJYmI-zXu1PZYfRLG07RhFoO3fTeIybm88QXEJu2AlwH6oq6LZ_0m95l7abMbmtDlRDi3C_mW6G_eFAG0DAdQxtS_ki52iC_kbm1BQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلاتان حوصله یوتیوبر معروف را نداشت
🔹
واکنش جالب ابراهیموویچ وقتی اسپید(هوادار معروف رونالدو) اعلام کرد پرتغال قهرمان جام جهانی ۲۰۲۶ می‌شود
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659211" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659210">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arGpOfInir8dh9IGlHPkhcqjjsRJ2ly7_vHhkNCiVSPURWk2buH2PZ6ZsDbpmJ4i2BxsgyG_2Csvtqgr1FpUMQASW_AY-aaNFO7XMR4D8A9ND1JVX5OAkzUJqm0mbE-053wPKIqwQyMp2QsosrNqAWcmA0Ew0ct64T-JQKaa6uMikZoixjjsQhQGjPGEL0uNlzFnlodPa1No3cPo00X0IxQnBdwS2cKgf8fi-h0oPMIpwYq7F6CnBFV6b_g4ZXbdqnS5LFi_W-_-9EL_rKv12mAXWlhz53ZHhavKBVWrhPryZ5SPfH3L16LYem6GjW23ceCrxmNyoDUwToDYwDRPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ کشوری که بیشترین مصرف نفت را دارند
🔸
آمریکا با مصرف روزانه ۱۹ میلیون بشکه نفت در صدر جدول قرار دارد و به تنهایی بیش از ۲۰٪ مصرف جهانی نفت را به خود اختصاص داده است.
🔸
چین با ۱۶٫۴ میلیون بشکه در رتبه دوم ایستاده و با سرعت بالای رشد اقتصادی، فاصله‌اش با آمریکا روزبه‌روز کمتر می‌شود.
🔸
مجموع ۱۰ کشور برتر جهان روزانه بیش از ۶۱ میلیون بشکه نفت مصرف می‌کنند؛ رقابتی که قلب تپنده اقتصاد جهانی را نشان می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659210" target="_blank">📅 11:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659206">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3J-OQF-R8adso2phOzbSi6tNveauro6xSw3omWcNaeMXEBIOJCZtS0UFTRXTdGxCMoer9Hj_GdQSqy7W1aau81rfB64m-QeSozp2hSDe3vNoK5E2M5Y3RP1Bz4oY-7BNz8fdzYI1Y-KEe2mOXhloBJroMX84SytWeV-Tng35O0OWx2rxnXkkNnM0CW5fa0NCiHwK4b8pE0teS9Tgki5UvpXq--ZQCKJeYy4b2A9lLqP3Z3SCkv-eqO4XFq4EujgLhOlUC_ro0iGw-srTt6A5e0BjpdyF_9n7jt_93lgHkFQtc7dFnmhe6sL1y05zWlPXjFHGBdhM8iIwoRUXUrNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2V9PGWgGNyEOArPxb9lN4mxovDDjiMJBaHL7h5dwLbVx1RE2WKaerulpTwwcDvY0Sdg4LI1CXj6QTa1nEaaD0GPPGFxY9A91UFYCTgGvtQI_Q8bKVGlRFEuGOJAXFpSzveCJvy4i7SihosL5MgBKuZs6Ltq3BBHfB29DyEh7QpI36ENuj8w0U9Qlp9_tyBGnvAcfE5XC3x_RpUOyCQ-qFLyhJq6gjoQ0zC4KBrxyJU7l1ijVLtA1GPWnvEnvhxhHvltfV8fgiYip_TY6U9H2O_ZyCdLhGPskEaPkBzGJBnTJeu_fWBRcI0NPlT1hH_9Tpa5v90CVU_FFX-UrLmcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHvBUzOTkuI2CbyjWfsMbNiud28EiwfdJw5FKzUZD57Q21azQ-1eEoCUXRY33Fe4lyahTrZxCeFjuB3t7zXTNW7W21BprZ64_WM67Z29p81QwEs3YWrZJn65XwFxlEo37lW-4SoxQ276vTFJUaT8bgQNO3i4kpYL_xB7tT2ZaxEqEs_9TQdSyKe6y54wh9QFDjmNKHplFDS5ii6vO2JoiB1KWVh2mNIIBQvwnXGEUoTrlvxfTsq3SMrB7eE_h_9TSg1CNL1vG9Ay9VIftT_Qx9jZWjT_BfWtkKIUwJbmnIsV717sq903v1AC__1JJVTM4cqQgQxQKB9VyE7UB_kb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJcntOSt5wjmu90lJKzZDpZrZYpsNT6_gb5hhFZvq8TVFGVKRzFD-x8m6dhjYmy2OAtviYzeC9hems2DWXiuXRv_AclqL5OHfA4kqIIllVqAm2Wuh9WG_eZluwAPIEd2pPbbEnFeShvWUw4KJvnc85c0kJ83Dp6IXGpMy7yX8CBoz4BWrUUJPb-WRE6ATGXlNBzLByrWrINapq968BpJnMJjhRk_6UryrZ4STbuKIv4GGGaRrpkwCn92DY1m-pms4aaejWs5Ff6n9Bd37SGtR73T_zKHs43joi_K4sM3v3pmDlTcdWz_AUEsGi_7CCyUZUTWxh4FlHtn247-9KO2bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر جدیدی از ماکت اولین آیفون تاشو اپل فاش شد
🔹
تصاویر جدیدی از ماکت آیفون تاشوی اپل منتشر شده که طراحی آن را در حالت جمع‌وجور و تبدیل‌شونده به تبلت کوچک نشان می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659206" target="_blank">📅 11:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659205">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
بورس از ۴.۸ میلیون واحد گذشت
🔹
شاخص بورس تهران در نیمه نخست معاملات امروز (یکشنبه) با رشد بیش از ۱۰۶ هزار واحدی از مرز چهار میلیون و ۸۰۰ هزار واحد عبور کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659205" target="_blank">📅 11:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659204">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وکالت‌نامه‌های تعویض پلاک تا پایان خرداد اعتبار دارند
🔹
رئیس پلیس راهور فراجا، از تمدید خودکار تمامی وکالت‌نامه‌های تعویض پلاک تا پایان خرداد ۱۴۰۵ خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659204" target="_blank">📅 11:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659203">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
مشکل خدمات بانک‌های تجارت و صادرات رفع شد
شرکت ملی انفورماتیک:
🔹
طبق آخرین گزارش‌ها درپی اختلالات به‌وجود آمده در ۴ بانک ملی، صادرات، تجارت و توسعه صادرات، مشکل خدمات کارت های بانکی بانک تجارت و صادرات رفع شده و تراکنش‌ها با موفقیت درحال انجام است.
🔹
موضوع در بانک ملی ایران درحال پیگیری است و آخرین اخبار اعلام می‌شود؛ در بانک توسعهٔ صادرات هم شعب آمادهٔ ارائه سرویس‌های ضروری به‌صورت حضوری هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659203" target="_blank">📅 11:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659202">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
مبلغ کالابرگ و یارانه برای اقشار کم‌درآمد اصلاح می‌شود
معاون وزیر امور اقتصادی و دارایی:
🔹
دستگاه‌های اقتصادی مکلف به برنامه‌ریزی برای اصلاح عدد کالابرگ و یارانه به‌ویژه برای اقشار هدف هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659202" target="_blank">📅 11:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659201">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b2e17333.mp4?token=WvMvKwGC8MHQTX-EZC2uNI8YBcWK5Fm-BVUmyeomVHC182QBckYPVg1GBlEmVBBqRX5oY4GyKWKMcRycP5dG76p8Bzsq_8009aGdrdb_kKCc87CUYJhUaDadjpj2hW15mkQdr2Z5Dp8AqER3pwnLZrGymqeCreer5ayOGSxuYE9c2HeK23LSR7OnccnEiM0OHoiRc2doPuPCcJarElcXbTsubnIp7ZEi3zCzBTQQYRCUbTzs3rRGgguy3HL3Ux3IrRS36RRZaGNl2fJCXYIPzwGM3edoosDtCOLj-H1xFjLZaiCxrLDNpc3WAsNaVh2yBxKmm5V-Rx4rUmU4KzXfDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b2e17333.mp4?token=WvMvKwGC8MHQTX-EZC2uNI8YBcWK5Fm-BVUmyeomVHC182QBckYPVg1GBlEmVBBqRX5oY4GyKWKMcRycP5dG76p8Bzsq_8009aGdrdb_kKCc87CUYJhUaDadjpj2hW15mkQdr2Z5Dp8AqER3pwnLZrGymqeCreer5ayOGSxuYE9c2HeK23LSR7OnccnEiM0OHoiRc2doPuPCcJarElcXbTsubnIp7ZEi3zCzBTQQYRCUbTzs3rRGgguy3HL3Ux3IrRS36RRZaGNl2fJCXYIPzwGM3edoosDtCOLj-H1xFjLZaiCxrLDNpc3WAsNaVh2yBxKmm5V-Rx4rUmU4KzXfDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۴۴ سال انتظار برای یک شاهکار...
🔹
یکی از بخش‌های اصلی کلیسای Sagrada Família در بارسلونا، شاهکار معمار آنتونی گائودی، پس از ۱۴۴ سال به مرحله افتتاح رسیده است؛ بنایی که امروز به‌عنوان نماد صبر، ایمان و نبوغ معماری شناخته می‌شود.
🔹
ساخت این بنا از سال ۱۸۸۲ آغاز شد اما گائودی در سال ۱۹۲۶ درگذشت و پروژه ناتمام مانده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/659201" target="_blank">📅 11:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4O2noF8uZ57_c07ryl4usgeTz7XgJ37D7u-dedjUmhlrbLUwEntYl6YE-vDAnhZS8DRyDckgjAQAM8kiG9mEar2mog11X_qcqFkWIgIp5OF2pg42F8NR6QGOV6JoMedel1yi7cCL0G7H_0gPp2L8e7zUIA3Mx8SdV_RylE5xDHwvXR90GfZlak3COuQwsF3wq-f6BQXMbpW49QIZUXhT9V9JJkwFuFtkwubuvo9Lb59xHxhYXfFH-RQwsJ_XiDCWXlXpwO-vzGo9e9uxjPOn9bc_XiEWME4LDUOQQkRUIZKavyd_etNDj-doQEN0u4KjsM5E_40_KkGbn_LK0dOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جام جهانی در حیرت قدرت‌نمایی تیم‌های آسیایی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/659200" target="_blank">📅 11:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
منبع آگاه: تصمیم نهایی تهران دربارۀ تفاهم‌نامه در دست بررسی است
یک منبع آگاه:
🔹
ایران هنوز تصمیم نهایی خود دربارۀ تفاهم‌نامه پیشنهادی را اعلام نکرده است.
🔹
بررسی ابعاد سیاسی، حقوقی و فنی پیشنهادهای مطرح‌شده همچنان ادامه دارد./فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659199" target="_blank">📅 11:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
حمله تمام عیار لاپید به نتانیاهو: برنامه موشکی ایران پابرجاست، تو بازنده‌ای!
🔹
یائیر لاپید، رهبر مخالفان، از توافق نوظهور آمریکا و ایران انتقاد کرد و در توییتی نوشت که «هیچ یک از اهداف جنگی اسرائیل را محقق نمی‌کند، حکمت پابرجا می‌ماند، برنامه موشکی پابرجاست و ایران می‌تواند برنامه هسته‌ای خود را بازسازی کند.»
🔹
لاپید ادعا می‌کند که این یک «شکست کامل» از سوی بنیامین نتانیاهو، نخست‌وزیر، است که اسرائیل را به «کشوری تحت‌الحمایه که در مورد امنیت ملی خود دستورالعمل دریافت می‌کند» تبدیل می‌کند./خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659198" target="_blank">📅 11:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5a5fc9c9e.mp4?token=odhGsg_OOklQV9fkf946KOvAeEZU7bPMLOibbFPZGmaRS_1ZW3ytPMwrMXc2ZvviTQHZaGjSNkL217dBgJSUP3H7wkyMKE5u1GZY32kboeP2xjM4V0TutrQtvN-V0KepdO5OYC7mRzapsNHVzVPqeZUi-gqnVl8WfUzbgK3c1ihENcHuroXE4IFwAnuL8N9SZl7-XvblYhVDg-WmnAxl5awP1kRGLDgc99y86k1DsoI1MoHDJ0tIdHyOyI6mpDt_eHDMy80H4yP9ygFbbwmUI8fjOhX4mZklHZxsLS7kXODYNSvKXkfMGMLZjwMFRt4IwNsaKoSlYzCGS2q7KxML95YFmpYG_4vAwbzxMhEZKiKJwNAyoD6Hf8I2fUxxC2fiVy7oOFU1YuKUOoUhquK5eSE0gKkZKXHzyWBGgsXhiqDFIeMb4W7UBitNborzNrDUlRnH0rDK7P2jRgx3HtiK2ywFtnBxhTFL41Yu9z__s1cP_bv67Sq-JR5dmMICcY0gOLnwm1nkB6-cgiev47X0MO59uoH-aqkVvPraYwjVLPFfdN_iLOLzkyExjSxBBiejhX3OOqWmcWYlQxCrui322hQ086FbG9r-DaXU5O3ayIoqAMQGtuXhPKpB72vI_5WUxRq7qeMTphSEyGNhT-zW4BaGPjjyB0Hi-smmktTNpK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5a5fc9c9e.mp4?token=odhGsg_OOklQV9fkf946KOvAeEZU7bPMLOibbFPZGmaRS_1ZW3ytPMwrMXc2ZvviTQHZaGjSNkL217dBgJSUP3H7wkyMKE5u1GZY32kboeP2xjM4V0TutrQtvN-V0KepdO5OYC7mRzapsNHVzVPqeZUi-gqnVl8WfUzbgK3c1ihENcHuroXE4IFwAnuL8N9SZl7-XvblYhVDg-WmnAxl5awP1kRGLDgc99y86k1DsoI1MoHDJ0tIdHyOyI6mpDt_eHDMy80H4yP9ygFbbwmUI8fjOhX4mZklHZxsLS7kXODYNSvKXkfMGMLZjwMFRt4IwNsaKoSlYzCGS2q7KxML95YFmpYG_4vAwbzxMhEZKiKJwNAyoD6Hf8I2fUxxC2fiVy7oOFU1YuKUOoUhquK5eSE0gKkZKXHzyWBGgsXhiqDFIeMb4W7UBitNborzNrDUlRnH0rDK7P2jRgx3HtiK2ywFtnBxhTFL41Yu9z__s1cP_bv67Sq-JR5dmMICcY0gOLnwm1nkB6-cgiev47X0MO59uoH-aqkVvPraYwjVLPFfdN_iLOLzkyExjSxBBiejhX3OOqWmcWYlQxCrui322hQ086FbG9r-DaXU5O3ayIoqAMQGtuXhPKpB72vI_5WUxRq7qeMTphSEyGNhT-zW4BaGPjjyB0Hi-smmktTNpK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شو اسپید متوجه نبود که تمام مدت کنار زهران ممدانی، شهردار نیویورک، در بازی جام جهانی نشسته است!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/659197" target="_blank">📅 10:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd17cd5474.mp4?token=u7V93XYjoe0n_Pe-iGlzO62YxrbIdX7iTsNNIs0D5OQZ8jrP_nvQ--KSQuyrZofZ9sjES7iL91zjRh_bDdkBaEfkPTQGuLU_TyyX8H1G_EvAnn0ifPauktSaO9Vl8YXyxzgB3rMpbBIQW-5uPMD8RlGGDAYty0okr0aiwS6umCaPEmuZP1umV_5DzPxUSUQrCXI3AIHas6gG5gMeZCI5tArc0l9VkCoSZxiw8vM3WSDlOZhsd_HRfSEQRp_EVc5zxRK6PA5LReX3xvMnOdYRAU3Sf-1ekNx-cuss7cGWEf37tWD_8QHN70YlyuZj_-LZc7LwI_gye7gfMe1Ktu-r6rHSLCF-uS1k1LjahhSrDTlwepjBHTQ5ZK_9nAvnx1-myLxz1qI3Ab7ikynqAL7OP32TpWA1V_N5X847LIk2NjLxzyPxXIlH9WHXW11wkMwrd3kEfBEryiqfgbHakFUEivpprJNmmZEnNDPATpjkbcRZRLDf46jLddWZdDjdeAtX0_zGEZT6o1UEh7uX_V04ZwJxOneWspsFVadaC6L7aKQiRBVDTTpPnN8KmAhbT1jz0rlIgzzFkmi-b3kOeAqnhXURJLkBj907YLdCUs4kzP9TeNLWOLSGKMwejbnSzsrFYGM0Ua4PE7aun3IVbu7JAUDe83kfMVYhGDT7bcvhY6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd17cd5474.mp4?token=u7V93XYjoe0n_Pe-iGlzO62YxrbIdX7iTsNNIs0D5OQZ8jrP_nvQ--KSQuyrZofZ9sjES7iL91zjRh_bDdkBaEfkPTQGuLU_TyyX8H1G_EvAnn0ifPauktSaO9Vl8YXyxzgB3rMpbBIQW-5uPMD8RlGGDAYty0okr0aiwS6umCaPEmuZP1umV_5DzPxUSUQrCXI3AIHas6gG5gMeZCI5tArc0l9VkCoSZxiw8vM3WSDlOZhsd_HRfSEQRp_EVc5zxRK6PA5LReX3xvMnOdYRAU3Sf-1ekNx-cuss7cGWEf37tWD_8QHN70YlyuZj_-LZc7LwI_gye7gfMe1Ktu-r6rHSLCF-uS1k1LjahhSrDTlwepjBHTQ5ZK_9nAvnx1-myLxz1qI3Ab7ikynqAL7OP32TpWA1V_N5X847LIk2NjLxzyPxXIlH9WHXW11wkMwrd3kEfBEryiqfgbHakFUEivpprJNmmZEnNDPATpjkbcRZRLDf46jLddWZdDjdeAtX0_zGEZT6o1UEh7uX_V04ZwJxOneWspsFVadaC6L7aKQiRBVDTTpPnN8KmAhbT1jz0rlIgzzFkmi-b3kOeAqnhXURJLkBj907YLdCUs4kzP9TeNLWOLSGKMwejbnSzsrFYGM0Ua4PE7aun3IVbu7JAUDe83kfMVYhGDT7bcvhY6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوت دیدنی؛ گل اول برزیل توسط وینیسیوس در بازی دیشب بین این دو تیم
🔹
برزیل ۱ - مراکش
۱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/659196" target="_blank">📅 10:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea5ec3ad9.mp4?token=Pp0y2Vs2J7aDltYywM6ZwFldhgRfPJwceo0mo7nc0EevF7HQgAtpna17d89hoiD3iJmtH5kIbxk3gyqYegKOsONRrA4rafrYcSQvT2wJMmHJccxwDzy4-I695RGzoyl2nZEpx1szyEP78P8xAdVaSy6ja6sDV6p7dZkPyuBc11TYEN_AakKccbQ8dXJZEr45zBSzuj6ah_5c-N38Wv-toMSbIc4ZIfLEBXNizmAgwICitxlkch0lrcd6dx70DE1ukCTad9ZLB17U44LrTLGQockiYu50410WeG8daOeYItPCdlRxtqu8dNFRO-PKHcSqcgZSwOI3L1elHY7J1Xj5YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea5ec3ad9.mp4?token=Pp0y2Vs2J7aDltYywM6ZwFldhgRfPJwceo0mo7nc0EevF7HQgAtpna17d89hoiD3iJmtH5kIbxk3gyqYegKOsONRrA4rafrYcSQvT2wJMmHJccxwDzy4-I695RGzoyl2nZEpx1szyEP78P8xAdVaSy6ja6sDV6p7dZkPyuBc11TYEN_AakKccbQ8dXJZEr45zBSzuj6ah_5c-N38Wv-toMSbIc4ZIfLEBXNizmAgwICitxlkch0lrcd6dx70DE1ukCTad9ZLB17U44LrTLGQockiYu50410WeG8daOeYItPCdlRxtqu8dNFRO-PKHcSqcgZSwOI3L1elHY7J1Xj5YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول مراکش به برزیل توسط اسماعیل سایباری در
بازی دیشب بین این دو تیم
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/659195" target="_blank">📅 10:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659194">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a411a8ae.mp4?token=v3HcfkDkYChmTm8psL0Mgu0le_cMvZgWjj71bV1VgFfLNXNmhWBO6uVTIOXEOOrnHvNhOORvL0HLp51SIjXt8L03WetziKye4RjQfCcvSDAXw1bmPwFCSbMbZx1Kpv_Z_8JZOUFjrVEhWjwMkiGcOmNn0Ot-kU6tEY_Jr_2IWhC2UOcTeOWVJQpYqrhqg5ubtZqztwOgV87LEbymekPIUAio6ZQ2vxymbHYgucP-1eOUbU48vQmKd5L5bXjPX0eaCDGKILyFg0Tb9X3ZbpjyFbjRlTqALpbRAyORRdYZ4kvfMBkod1e2TYzPox_SGsiMZgRC8E_rZHxgmvl0k8Mw8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a411a8ae.mp4?token=v3HcfkDkYChmTm8psL0Mgu0le_cMvZgWjj71bV1VgFfLNXNmhWBO6uVTIOXEOOrnHvNhOORvL0HLp51SIjXt8L03WetziKye4RjQfCcvSDAXw1bmPwFCSbMbZx1Kpv_Z_8JZOUFjrVEhWjwMkiGcOmNn0Ot-kU6tEY_Jr_2IWhC2UOcTeOWVJQpYqrhqg5ubtZqztwOgV87LEbymekPIUAio6ZQ2vxymbHYgucP-1eOUbU48vQmKd5L5bXjPX0eaCDGKILyFg0Tb9X3ZbpjyFbjRlTqALpbRAyORRdYZ4kvfMBkod1e2TYzPox_SGsiMZgRC8E_rZHxgmvl0k8Mw8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسابقۀ کشتی در آمریکا به میدان جنگ تبدیل شد
🔹
آمریکا از سال ۲۰۲۵ اقدام به برگزاری مسابقات کشتی آزاد تحت عنوان RAF کرده که در آن خیلی از ستاره‌های مطرح جهان هم شرکت می‌کنند.
🔹
در یکی از این دیدارها چیمایف از روسیه به دنیس از آمریکا لگد زد که منجر به درگیری نمایندگان دو تیم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659194" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: مذاکره‌کنندگان قطری برای نهایی کردن تفاهم راهی تهران شده‌اند
🔹
شبکه آمریکایی به نقل از یک منبع مدعی شد که مذاکره‌کنندگان قطری صبح امروز در هماهنگی با ایالات متحده به سوی تهران پرواز کرده‌اند تا به تسهیل روند نهایی‌سازی توافق (یادداشت‌تفاهم) بین ایران و آمریکا کمک کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/659193" target="_blank">📅 10:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659191">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
انتقاد البرادعی از تقلای ترامپ برای بهتر جلوه دادن توافق احتمالی با ایران نسبت به برجام
مدیرکل پیشین آژانس بین‌المللی انرژی اتمی:
🔹
ترامپ به‌شدت تلاش می‌کند نشان دهد که توافق جدید او از برجامِ "باراک اوباما" بهتر است.
🔹
در حالی که به نظر می‌رسد این توافق چیزی جز بازگشت به وضعیت پیش از بحران نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659191" target="_blank">📅 10:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659190">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای الحدث: یک نشست مجازی میان هیئت‌های آمریکا و ایران با حضور میانجی‌گران پاکستانی و قطری برگزار خواهد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659190" target="_blank">📅 10:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659189">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
الجزیره: ایران هنوز تصمیم نهایی خود درباره تفاهم‌نامه را اعلام نکرده/ می‌توان انتظار داشت که توافق امروز نهایی شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659189" target="_blank">📅 10:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659188">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
معاریو: ایران پیروز بلامنازع است/ نتانیاهو شکست خود را با سرافکندگی اعلام کند
روزنامه معاریو:
🔹
نتانیاهو باید در مقابل افکار عمومی بایستد و سرافکنده بگوید که من شکست خورده‌ام و حتی بهترین دوستم (دونالد ترامپ رئیس جمهور آمریکا) هم برایم ارزشی قائل نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/659188" target="_blank">📅 10:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659187">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887fd432f8.mp4?token=HSs3Gt0Z8Ig1daA7nU9Im4DVQRNjBuurGyL1X_4f9L1QoCsnkWnu9CslAELWTg8uF2y0YeIvQJD7IKKFSIITc0OXoq-9D6GsPtR-HVYYWYyphP74mARf3-uPeS9zIptJCppEpmxNfdmht4Q4TfbNatZM03nRlcqIEbxISF9cn6G4s9iGuWhc2k3PVRlYDZi7LK8W3uOuDcDH1NkWj5qEEjruHDse2eM30ClO68x_ZHZTeBmbmiLMcfl7FFZuoB_M-2P9MQVoW91b3ipLCmYcMyvMLrmnKQ_h2ju0mkErcC_B09nH6hMd_zTXE6wU3u6jvhqTBaHCu-inJPCL7N-Lbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887fd432f8.mp4?token=HSs3Gt0Z8Ig1daA7nU9Im4DVQRNjBuurGyL1X_4f9L1QoCsnkWnu9CslAELWTg8uF2y0YeIvQJD7IKKFSIITc0OXoq-9D6GsPtR-HVYYWYyphP74mARf3-uPeS9zIptJCppEpmxNfdmht4Q4TfbNatZM03nRlcqIEbxISF9cn6G4s9iGuWhc2k3PVRlYDZi7LK8W3uOuDcDH1NkWj5qEEjruHDse2eM30ClO68x_ZHZTeBmbmiLMcfl7FFZuoB_M-2P9MQVoW91b3ipLCmYcMyvMLrmnKQ_h2ju0mkErcC_B09nH6hMd_zTXE6wU3u6jvhqTBaHCu-inJPCL7N-Lbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر میخوای واقعا خودت رو شفا بدی، باید اول چهار نفر رو ببخشی #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/659187" target="_blank">📅 10:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659186">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
نیویورک تایمز: ایران اکنون با نسلی جوان‌تر و جسورتر اداره می‌شود؛ نسلی که به حفظ مواضع خود حتی در شرایط پرهزینه باور دارد و احتمال جنگ تمام‌عیار آمریکا را پایین می‌داند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/659186" target="_blank">📅 10:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659185">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb9660cf0.mp4?token=Ne0Awj0xFdvd3wzhYX0Sp8B0m_FpQ7UfAu-QepkKXKQNe0u4O5p4I3Z6ZORve_wNfHFRyA6ojb6gMmBegYrW75Xq9ryVBRkD9KD3ERwehubdFunA8mcYAJ9ZrQTTwMeBDtl6iJ00iSobZegn7TvIgAHbC5I7ajW0l_c1KmeY4GVvWqaBPt2Crt-wHcu4kYgaXXDYJrvmLMVIe7VZbHfX0ELneTW8hfqTNFQqCYAx21HHYUpUmeNbycEypNXXNGtEwAnhoKGKcxS2yM3QmIwo9LaRTMeMx6jBR2x-usFgMW-lSOduKlVe6t7xLcwLOwEFaBRpXKMrGhy_a3nhwDirAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb9660cf0.mp4?token=Ne0Awj0xFdvd3wzhYX0Sp8B0m_FpQ7UfAu-QepkKXKQNe0u4O5p4I3Z6ZORve_wNfHFRyA6ojb6gMmBegYrW75Xq9ryVBRkD9KD3ERwehubdFunA8mcYAJ9ZrQTTwMeBDtl6iJ00iSobZegn7TvIgAHbC5I7ajW0l_c1KmeY4GVvWqaBPt2Crt-wHcu4kYgaXXDYJrvmLMVIe7VZbHfX0ELneTW8hfqTNFQqCYAx21HHYUpUmeNbycEypNXXNGtEwAnhoKGKcxS2yM3QmIwo9LaRTMeMx6jBR2x-usFgMW-lSOduKlVe6t7xLcwLOwEFaBRpXKMrGhy_a3nhwDirAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی بزرگ در شهر تریسی ایالت کالیفرنیا
🔹
آتش‌سوزی گسترده در یک انبار عظیم تجهیزات پزشکی در ایالت کالیفرنیا آمریکا برای سومین روز متوالی ادامه یافت و مقام‌های محلی نسبت به کاهش کیفیت هوا و خطرات ناشی از دود برای ساکنان منطقه هشدار دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/659185" target="_blank">📅 10:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
انگلیس صبح امروز در کانال (احتمالاً کانال مانش) به یک نفتکش متعلق به «ناوگان سایه» حمله کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/659184" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nt-ybEE25Pi7_BCqSbLXhHEMETLAsTCwM_UlUe3zLA7jJzwAsH6ig-VFfMWkDVimcDDgvnIrVO0D5Emfe4lVE-GP3AIx5vgvlgANMQ3LARiHmRPFsOqoZOY7zLstoDjcfDteBDmNfMBR3AtfiSeUqD1KaqC2g5dg2YtswBTKkH8_6NmAXb4ib69hLFA7ZmDmG5NrU59EqKsiBilCVtszZb6TdafSla2mewjMZq5_mmRcQliWQur8wX-jevHv_3tlQA8IVREKfNoiEtZk1K14-sHXfQIKDPl0Hmo-qws-PKy4ltuaCtZCyPj5LmR0bEHc6Hfg_R9g0NHmXMmim9LUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت برنت با کاهش ۳.۳۷ درصدی به قیمت ۸۷.۳۳ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/659183" target="_blank">📅 09:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6fb66b31.mp4?token=SFifk4t_xzE_wT7jfQxEsuYwIvxS90pTdZu-Fg-Wn-3JtMnKi9fpkVcifseIh0fMEb8s4jVkX4_HKH4q4gFVAQXAHMwTbx2V7KVzKrZ2Okcr-5sQfThpbTeLTBfKFbpq72yQgL8BN66XcJrWL8qq9Hr_jvPfbkrjH4vxsW4QMkV9TDtElSQBCdEu44GOFQOLgZTsOFes4strZcov-Spmlg7PyASNGBn6OFixhSpGaQjpPuNXXaABMoPPRUtkXYsbBiKdjCVfGTKFViYGAYtyKQ_mbHTSRpXAS30asLNG-hoeGJgZCRCrdVn8Mgi68uy1_mUwItCM-9_0XFD4Uub3gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6fb66b31.mp4?token=SFifk4t_xzE_wT7jfQxEsuYwIvxS90pTdZu-Fg-Wn-3JtMnKi9fpkVcifseIh0fMEb8s4jVkX4_HKH4q4gFVAQXAHMwTbx2V7KVzKrZ2Okcr-5sQfThpbTeLTBfKFbpq72yQgL8BN66XcJrWL8qq9Hr_jvPfbkrjH4vxsW4QMkV9TDtElSQBCdEu44GOFQOLgZTsOFes4strZcov-Spmlg7PyASNGBn6OFixhSpGaQjpPuNXXaABMoPPRUtkXYsbBiKdjCVfGTKFViYGAYtyKQ_mbHTSRpXAS30asLNG-hoeGJgZCRCrdVn8Mgi68uy1_mUwItCM-9_0XFD4Uub3gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ملی‌پوشان فوتبال به اسم ایران هم‌قسم شدند
🔹
ملی‌پوشان فوتبال کشورمان در آخرین تمرین خود در تیخوانا پیش از سفر به لس‌انجلس با تشکیل حلقه اتحاد، برای موفقیت تیم ملی هم‌قسم شدند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/659182" target="_blank">📅 09:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659179">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: مقامات ارشد اسرائیلی می‌گویند ایرانی‌ها بی‌دلیل با این توافق موافقت نکرده‌اند، طرف آمریکایی شرایط اصلی آن‌ها را پذیرفته است
🔹
به گفته آنان، این توافق بلافاصله منجر به رفع محاصره دریایی و نجات ایران خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/659179" target="_blank">📅 09:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659178">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
آموزش‌‌وپرورش: ۱۳ تا ۱۵ تیرماه احتمالا امتحانی برگزار نخواهد شد
🔹
همچنین تمامی امتحانات دانشگاه‌ها و مؤسسات آموزش عالی کشور که زمان برگزاری آن‌ها با مراسم وداع و تشییع رهبر شهید انقلاب تداخل داشته باشد، به زمان دیگری موکول خواهد شد.
🔹
اطلاعیۀ قطعی و نهایی…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/659178" target="_blank">📅 09:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659177">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0wAL--7rX6DOgoqBy5oK2FDvETplTrJYp2eyoUGE4QLjZ8fvDI349TOdF81JIkl0zU6yQVUQBr2CmnAzGvdOP_NgG8fI6srXD93YZNGPImiFtaq6ru2yL9FWuUgfFEzExGJT8ZFOq6B7HFH5nTCVkNaLek-TmnDiJW_goAwHYmbrSzvEVFRIoFBwwE0kXeNBiA-AvQP04LFXnC0tXpRXpSwc5GywC-vkcAv2fXp8iFICU0_FJTcJqu4hDp62o4n4MucsEvd8C6QLQ03Zpn-f9hv0SMAclRP_jigESkKZm2-sAPP-fV3oZsyDpieI0wYn6djqu8omwXjI6QgKw0WnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال نیوزیلند برای دیدار با ایران در جام جهانی ۲۰۲۶
🔹
این بازی صبح روز سه شنبه ۲۶ خرداد و از ساعت ۰۴:۳۰ به وقت تهران در ورزشگاه لس آنجلس برگزار می شود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659177" target="_blank">📅 09:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659176">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-ACQAkBO5scK_McIN6CTef0awuWeF-sIDckBXCuSq-601GpLYaras-5qhv1D9WqHs5v4RJ-YS8mpB7Ynun0wOm1sgtzG8X0OOC-rYaYQo1K_3U7QsAof67cbPBXl-15Um5-gzM-uzikKqkaIjAYzdReO2aexzBU3MSluwBEzRkctfAykgIuVdiKrm4DXlIkUL_IphAz_OIzOtl6LudSFNWgExE8RWNjFUrP8KCc2E1uOfbZdvSfkGGzkRXiF5aYGZSacQO8fDaRRXD0gDSRH4JM-C7aTSTbauMw3Ltlj50zWYXxtqRNw4hTFoF1pvRvoQfQU5SWDMu3-FbFt3z3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۱۰۳ هزار واحدی شاخص بورس/ یک واحد تا کانال ۴.۸ میلیون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659176" target="_blank">📅 09:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659175">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
با اعلام فدراسیون فوتبال، اعضای تیم ملی ایران امروز برای دیدار با نیوزیلند به لس‌آنجلس خواهند رفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/659175" target="_blank">📅 09:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659174">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqUSx1C7ZCwXqeUJaUskUOHK1waG3kQrxoEDF-eJc3mIASrB8ZU-YBeWiBRYHskJLZcIeJavEpzWtw-NyWBiG060MyzmDf1JU77_OgidkyhKC2D2S4aI_toOzu6HnQoLpd-FB1Pus_lJl-tLpTpk87gM59TX9ZGLpexZUWNE9CPAfGrgWpyVkL8GZwrpdBA4Ya4C8gKXgYyy2FGD-68w96RO0gr7cPS3Ts7MPbHqrmTAxTXlkubtJUldtGexEJo7Zem30lgwnSmNCM3bwsUNlAXf1IOSYk36Aib4mc4F2FRplhDWCpDE1D__PXSiDSZAW33zkyUfnSP0R_FWzfoSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر از رهبر انقلاب در کنار برادرانش
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/659174" target="_blank">📅 09:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659172">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFVhsvPShLTsT47MkY8GuseEUgkK5Yp4iTiasH0sbRnzJfb8Z5Tcm8XJe6f0GuCb18EMeaz9ZgRbnZD0mGp9rNLHCcU-eYdqwnxmRed-kCJ0-FDK6AGBj5wXK4aGy7UHRU0-bTTeAx-at-fBe1mIDZxXYKCLr_fN_edz1HZ-yVsb-zvOZokwmDVEfULv4uOwheZvRZRWbJHtGAY3Oq0olww5eLTN9FC6omsqoaIbDh4epg150zaOuLFeIcEr-w98eHkjolVocU2A6QMnAd_7up1Bj7Lb7HByZ1LMkG7ld5nMF2UUCMY_ht2VbNa8HSPlEcOO--90UwXT0kOxP0wwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmwmlRJVnNdD3nbmQogmbN4JBsPp2KYZtgDbmNF1K-40EUgmR4EW9g0JxEsagSNQjps0HTRTNv8_942ZWgvfFFKI07dZ56HrnbynLuLUCZWk2PEBiVUBZRduWRFp9bWyWWtGaeeL42RhTOCghwcxl4eobT4aFO_oAcTSvAFKAlXuA5Yys7VHazMWJW1BMsjKJB6aXsjd1q0WqXSI0CyfpZoiXu0tadlnwELYT1XC69nplHY22THsU5hHy8SjhR4QhpfspLZDcPJgVhyKzaclyCsYAe2p5zSxCAyjCya_ACnFD4UzrySkVPFdd2g14T_D_rt3ED6jcFyWglCss-ao6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دو تصویر جالب از دیدار ترکیه و استرالیا در جام‌جهانی ۲۰۲۶؛هوادار عجیب ترکیه و تقابل عجیب‌تر مهاجم ترکیه با دو مدافع استرالیا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/659172" target="_blank">📅 09:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659171">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/503b930548.mp4?token=LKK-FRe3SJyHLDmj_TI5Q15_aK9hRqu8HhiSit1QHpBBJDNr_-H_CcbXbtyMHnI6RAa4AFsVhXLhyeSs0zxIJrdhm39f02nbGaiWPU885GWmZUgger8oN_0JrU1NuSa73qTyEPBFCgnaPYAOLoFltGYNJqwfW6MYJXeVj5ufgzk0_2ZrWN7-FCdEzXMVZsC7rqKWGuZgq6k3mibcfUVGk8JJ0Pe1FQO5IjKpRgVx8hyDk3SABXjayHYUwzrZxYJxEuHPJBH5Fv9jHUKqtL4MzvzbTmY1Pi1Q5VsrN1yRUPEgsYJNQUKweZS_bB-XM_8jsPcptc2Z6ozPdlPrdhCjvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/503b930548.mp4?token=LKK-FRe3SJyHLDmj_TI5Q15_aK9hRqu8HhiSit1QHpBBJDNr_-H_CcbXbtyMHnI6RAa4AFsVhXLhyeSs0zxIJrdhm39f02nbGaiWPU885GWmZUgger8oN_0JrU1NuSa73qTyEPBFCgnaPYAOLoFltGYNJqwfW6MYJXeVj5ufgzk0_2ZrWN7-FCdEzXMVZsC7rqKWGuZgq6k3mibcfUVGk8JJ0Pe1FQO5IjKpRgVx8hyDk3SABXjayHYUwzrZxYJxEuHPJBH5Fv9jHUKqtL4MzvzbTmY1Pi1Q5VsrN1yRUPEgsYJNQUKweZS_bB-XM_8jsPcptc2Z6ozPdlPrdhCjvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت پهپاد به داخل سایت نظامی ارتش متجاوز اسرائیل
🔹
رادیو ارتش رژیم صهیونیستی تصاویری از اصابت یک فروند پهپاد به سایت نظامی ارتش این رژیم در منطقه الجلیل غربی در شمال فلسطین اشغالی منتشر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/659171" target="_blank">📅 09:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
خودکشی پس ‌از صحبت با ChatGPT؛ مادر کانادایی به‌دلیل مرگ دخترش از OpenAI شکایت کرد
🔹
مادر یک زن کانادایی از OpenAI و  سم آلتمن شکایت کرده و مدعی است ChatGPT پیش از مرگ دخترش، به‌جای هدایت او به کمک تخصصی، در تشدید مشکلات روحی‌اش نقش داشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659169" target="_blank">📅 09:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659167">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ec9e5630.mp4?token=Yz3Rs-t6I56lQwq5GugW_F7XJcICtZISGL3WNHrFz3SncF61luC01YcEP8enmW4PKYgcdLlPXkV-BwSzCERvBAFgr6rRUziO_jcDoHoQJEbmHt3Z2cZ97CP0lIKanlhKiCwzf4JaKCXXF68lk2dqh9QghpsQAsR3Ynp9SjJlRZZWDJFvlHUCEa_U1ufPUZWFrTVqh9QXgK-zqiupbLIqrPm2upE0EA4rD1YcXj5X9G4zXYbX3eU3iO71RpkopuZunZV1tJRueERaF8tYZCcySrecmuJIk9JFqDYCSjeevUM7_WtdEtH9zQ6KTYwh873VlqMc0Rlcx1_TKDD_l4kNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ec9e5630.mp4?token=Yz3Rs-t6I56lQwq5GugW_F7XJcICtZISGL3WNHrFz3SncF61luC01YcEP8enmW4PKYgcdLlPXkV-BwSzCERvBAFgr6rRUziO_jcDoHoQJEbmHt3Z2cZ97CP0lIKanlhKiCwzf4JaKCXXF68lk2dqh9QghpsQAsR3Ynp9SjJlRZZWDJFvlHUCEa_U1ufPUZWFrTVqh9QXgK-zqiupbLIqrPm2upE0EA4rD1YcXj5X9G4zXYbX3eU3iO71RpkopuZunZV1tJRueERaF8tYZCcySrecmuJIk9JFqDYCSjeevUM7_WtdEtH9zQ6KTYwh873VlqMc0Rlcx1_TKDD_l4kNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهرزاد جواهری بازیگر تئاتر و تلویزیون درگذشت
🔹
شهرزاد جواهری بازیگر تئاتر و تلویزیون و همسر مهرداد ضیایی بازیگر و کارگردان تئاتر، سینما و تلویزیون روز گذشته شنبه ۲۳ خرداد بر اثر ایست قلبی فوت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/659167" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659166">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5664fafbfc.mp4?token=XGcGNWhxPDzP07Km_R6XSQlZJ64DF2Mm7qqS-qDeNVUhY8yrPw8-HItk5VxF2HepWRFQjoFeYrJDH__iHArdJP4GPRGmeOMNmFFZEaR2KH3idyWpPZ2M_pdU5JfzE3mSG7gIE--kgqer8bl_bR3E8kLc8SMtsibX5Fu-CZvNt12Zkft9VAu8DuBvgXp6vKbxNFCDw-HUJZkoXzRPI7Tkkr3OdXy067bqh176IljWdpkQmLgZFQR2VGlzF6i2G4yZjpeyzfrVD0aQp-5dJoOh9YhhPnLjjXHfop8jRH5cU1KSKdj3_nllpaEfjrg_QbVWWpY4TRKoglUb9qo9aP-OIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5664fafbfc.mp4?token=XGcGNWhxPDzP07Km_R6XSQlZJ64DF2Mm7qqS-qDeNVUhY8yrPw8-HItk5VxF2HepWRFQjoFeYrJDH__iHArdJP4GPRGmeOMNmFFZEaR2KH3idyWpPZ2M_pdU5JfzE3mSG7gIE--kgqer8bl_bR3E8kLc8SMtsibX5Fu-CZvNt12Zkft9VAu8DuBvgXp6vKbxNFCDw-HUJZkoXzRPI7Tkkr3OdXy067bqh176IljWdpkQmLgZFQR2VGlzF6i2G4yZjpeyzfrVD0aQp-5dJoOh9YhhPnLjjXHfop8jRH5cU1KSKdj3_nllpaEfjrg_QbVWWpY4TRKoglUb9qo9aP-OIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باشگاه رو به خونه بیار #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/659166" target="_blank">📅 08:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659163">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9757a712f0.mp4?token=IjB9OyOMpvfuzzGsRvHkw11hKIyPwb8nWnuv7KKqXJ0WbUjJ_H3DVh0tG4C1_p-AIMwFYaBRYWkSICozx0eDyh4Sj3uwlyDsfYp8wh-fPRb-H2MlazV55PptCZDeX_ACSB7k4x4bXZRtDUXwDphxZRQ6ns9ZCMuAef0xz59K0uX53DlD5WRSGDjl6rIhZkt8sBXzDJ2mmJLxZbhbOCben3i_vzFZpmlDxl1AebWWjsxgO_KP_YY4cALBXkeOJ95GFgA5LpkUHGXPge4GQb-NPx8nxydjQXC_Mx2rAycolmx8QYsjtxBMvB9fvFU3ocaX9oWswcY0cuDmIl8yyC1-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9757a712f0.mp4?token=IjB9OyOMpvfuzzGsRvHkw11hKIyPwb8nWnuv7KKqXJ0WbUjJ_H3DVh0tG4C1_p-AIMwFYaBRYWkSICozx0eDyh4Sj3uwlyDsfYp8wh-fPRb-H2MlazV55PptCZDeX_ACSB7k4x4bXZRtDUXwDphxZRQ6ns9ZCMuAef0xz59K0uX53DlD5WRSGDjl6rIhZkt8sBXzDJ2mmJLxZbhbOCben3i_vzFZpmlDxl1AebWWjsxgO_KP_YY4cALBXkeOJ95GFgA5LpkUHGXPge4GQb-NPx8nxydjQXC_Mx2rAycolmx8QYsjtxBMvB9fvFU3ocaX9oWswcY0cuDmIl8yyC1-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندی برای مبارزه با گرما؛ تیم ملی اسپانیا با جلیقه‌های یخی با گرما مقابله می‌کند
🔹
تیم ملی اسپانیا در تمرینات خود از فناوری خنک‌کننده CLIMACOOL آدیداس استفاده می‌کند؛ سیستمی که با افزایش جریان هوا و تسریع تبخیر عرق، به کاهش دمای بدن و حفظ عملکرد بازیکنان در شرایط گرم کمک می‌کند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/659163" target="_blank">📅 08:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659162">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0afde03d4.mp4?token=WnWZTbN2q8Z3GlIbQ894HjVYlFOzWSeWJfUUg08JOu2hXyPg08WZyccBYcj5KgkdGuQO_o6RS7iIuZebTFLetmT3EQjlGTIT8vkFS7oEoEx40qdMs4mOIlCmHBcqQwB_0JqUM9zTzMsEIxCtha29AmsbX09gUx3KrQQ61NJ7hCWvU7178e7Kd2rY6l02W33uFfqT86hpMHNmH8IlHpf1KMOmX9w5TLqFs4LIkp4aS1D9YIWr44wgsZCetbISgSR5-eCFXV-IdutRAxVPX7euKVpHjxNnPxkAsj4xaAm9SNwdq8Y8JV9XSQXXeAErIlEm56uU6kaoc6vMXi6X6NBd8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0afde03d4.mp4?token=WnWZTbN2q8Z3GlIbQ894HjVYlFOzWSeWJfUUg08JOu2hXyPg08WZyccBYcj5KgkdGuQO_o6RS7iIuZebTFLetmT3EQjlGTIT8vkFS7oEoEx40qdMs4mOIlCmHBcqQwB_0JqUM9zTzMsEIxCtha29AmsbX09gUx3KrQQ61NJ7hCWvU7178e7Kd2rY6l02W33uFfqT86hpMHNmH8IlHpf1KMOmX9w5TLqFs4LIkp4aS1D9YIWr44wgsZCetbISgSR5-eCFXV-IdutRAxVPX7euKVpHjxNnPxkAsj4xaAm9SNwdq8Y8JV9XSQXXeAErIlEm56uU6kaoc6vMXi6X6NBd8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای آهنگ قیصر، خواننده سابق لس‌آنجلسی برای تهران در فینال رقابت‌های فیجیتال جام خلیج فارس، یادبود شهدای میناب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/659162" target="_blank">📅 08:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659160">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
حسین شریعتمداری: چرا بر سر باز کردن تنگه هرمز تفاهم کردید؟ چرا غرامت نگرفتید؟ زمینه را برای جنایت بعدی آماده کردید
حسین شریعتمداری، مدیرمسئول روزنامه کیهان:
🔹
با چه توجیهی قرار است از این اهرم سرنوشت‌ساز دست برداشته شود؟ او تأکید کرد دریافت هزینه خدمات از کشتی‌های عبوری کافی نیست و تنگه هرمز یکی از اصلی‌ترین اهرم‌ها برای دریافت غرامت از آمریکا و شرکایش است.
🔹
به گفته وی، رها کردن این اهرم می‌تواند زمینه را برای حملات و جنایات بعدی فراهم کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/659160" target="_blank">📅 08:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659159">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g66SmdrP6yLIjnne0VwEGHMflvp0dWj5l8Ey1e2lRSZNjx_o4hnncMNUAEyHXM2LQ95Dww40lFMYeP_hCmIC0iV9xrUOkxJswiE_8Kzz5kzr5hP_F4ki20KuXL6-1LumzoIrVzsjJHqg8O3nsC9ehyU__yKcK3ojVAbMTqzBDNSL9iu7iZxxMTJSVcqpkReCZMn3HKdSKnAQmC67f8WffCV9S69rmV4xZ-cd_599b2I8NZyC0K9NP233go3vKksYcY08AvqsT1bs6yZngayyk3EU9pDHbUTAXf9taGYnyUHQRNjIMmAMtqz7-NJNQIhWDjfybuovbjTKYKjpvHuP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افتضاح‌تر از شکست «خلیج خوک‌ها»!
اقتصاددان سوئدی-آمریکایی:
🔹
هیچ جنگی از سوی آمریکا پس از حمله خلیج خوک‌ها در سال ۱۹۶۱، احمقانه‌تر از جنگ ترامپ علیه ایران نبوده؛ نه تنها هیچ دستاوردی نداشته، بلکه هزینه‌ای سرسام‌آور هم به دنبال داشته.»
🔹
عملیات خلیج خوک‌ها، یکی از مشهورترین شکست‌های نظامی تاریخ آمریکا است که در سال ۱۹۶۱ میلادی علیه کوبا انجام و به شکست شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/659159" target="_blank">📅 08:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659158">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd5cdaafc.mp4?token=puC28tf9-P5YfRyfK8w89edCKK0RwKzo-4QdIRzroJ8eQ9hAM6pda64mx2nGYY38gF6a8fDrpdfjSzZUimSucfVvwc6kQnSVFPPXuhkTqcN-DaGB5WfCtJKshU9bNX5dpSzV-YGnWljFhugkiJMCjbCWp9NiRDXmKVCIgJ-y5Ja4NC5oy2yq0pLIwh5fAAkC-Yyx_mAbNDPEBoFR_0UgU03S4UW4G5R7xGxIW2GlgZHF9T2hoF7MV3DLfhRn9zAp0J2o79VK5BFKmhQXcSeoed9-moAkEUSRQ8RI4pPysA9IUu5RTziOq7FXYDhof8-vmaNiJMjCbhumgYssfN7vDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd5cdaafc.mp4?token=puC28tf9-P5YfRyfK8w89edCKK0RwKzo-4QdIRzroJ8eQ9hAM6pda64mx2nGYY38gF6a8fDrpdfjSzZUimSucfVvwc6kQnSVFPPXuhkTqcN-DaGB5WfCtJKshU9bNX5dpSzV-YGnWljFhugkiJMCjbCWp9NiRDXmKVCIgJ-y5Ja4NC5oy2yq0pLIwh5fAAkC-Yyx_mAbNDPEBoFR_0UgU03S4UW4G5R7xGxIW2GlgZHF9T2hoF7MV3DLfhRn9zAp0J2o79VK5BFKmhQXcSeoed9-moAkEUSRQ8RI4pPysA9IUu5RTziOq7FXYDhof8-vmaNiJMjCbhumgYssfN7vDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهروندان مکزیکی بعد از کره جنوبی سراغ ایران آمدند؛ برادر ایرانی، تو مکزیکی هستی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/659158" target="_blank">📅 07:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659157">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
کالابرگ کد ملی‌های ۷، ۸ و ۹ فردا شارژ می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/659157" target="_blank">📅 07:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659156">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwh980kYteKadBMfj2NAZDF3hU-rysAnB8bbhcQjn02-O-IvarFSlCXHTw3uSfekS5DpN8vun5Ci3xBjo_dv77hXkUoaXMjAZysBIWA_ptu1ksMAKiC4-nRlhvaks7hstJtwS1eSN1RSmrhq9tUtHIq9pmmydyZxGRiwCJDUw5mu4ufPAbf1PfKsziXSdTBQAIMXJSVM76TjW1VyF2G1FcLizyvcybbyJoRY2anbdyQDw4BEkcb-6JJYWjYmYKi2kovfv3OKV_6pSdIm8rfJk5MN9TxLW3JPya7cWM_SBixBJNQuZootVgRkZtB9erCaKceYOTGT7CGxxqa8gX0iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از حمله به یکی از مهم‌ترین سایت‌های راداری آمریکا
🔹
تصاویر ماهواره‌ای جدید، تخریب سایت رادار هشدار زودهنگام آمریکا در جبل دخان بحرین را پس از حمله پهپادی ۱۱ ژوئن نشان می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/659156" target="_blank">📅 07:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659154">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee745d52b.mp4?token=BFz3SmM3bbqUxkMtWp4fkX3Mnc4B2alJrvD1sRT8_y6wkqYq2RZdO5muTzaTHmtP0GO--smG3XTakxLKUuD6Z3MLQMTDdYLdlD6bbo0Da2al8N_AZVX0acMZffsTZ0VrjXJrUHfL4nI8IcLT4JAMT-6Up-VaQib6NS3WnKkloIYZHdN6duuDkI_2teFobznWpVZ-TF4X-zPn7h3VVhizQTIF2ox62_V7sP4d9y0qOx5zA1SQB6Va9RhAol2SZI8QLigfua7f_-5l0eQLcW2n-QpJIjS6GOgZrmKZkqD87Vp1n5gl7HCP-VL2aS2njOgwpniVnl4k_8SqxrGLv06wkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee745d52b.mp4?token=BFz3SmM3bbqUxkMtWp4fkX3Mnc4B2alJrvD1sRT8_y6wkqYq2RZdO5muTzaTHmtP0GO--smG3XTakxLKUuD6Z3MLQMTDdYLdlD6bbo0Da2al8N_AZVX0acMZffsTZ0VrjXJrUHfL4nI8IcLT4JAMT-6Up-VaQib6NS3WnKkloIYZHdN6duuDkI_2teFobznWpVZ-TF4X-zPn7h3VVhizQTIF2ox62_V7sP4d9y0qOx5zA1SQB6Va9RhAol2SZI8QLigfua7f_-5l0eQLcW2n-QpJIjS6GOgZrmKZkqD87Vp1n5gl7HCP-VL2aS2njOgwpniVnl4k_8SqxrGLv06wkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط یک فروند جنگنده آمریکایی
🔹
منابع خبری از سقوط یک فروند جنگنده اف-۱۸ در ایالت واشنگتن آمریکا خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/659154" target="_blank">📅 07:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659153">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWrCggYsCSHOHR0x6LOqzHE8JkPo-CecEd_JntYNJw145bZMnel7_ktv67XwItZ67c2hTbwf5JWNBSahL0xv5kmkON64gL3yrcNuhxjgsAoFzPKM28WfJQYBs9eXkp2h7-DcJIbuXPkLPZR_EIh4cWyZBrLELIVN3zzwlMPCI2xtPfUcpvJ3vDZETTyPGPAmk3NMsve0pE4HQeLlV1xAE5qIU_yBcMnza05ZXA3X4rtTmCSRsuckCJCe4lIHTgTVymHkXeFlJJIyotTx0Azj_c_Z0WQNWvNlnFnxFY2ZZheU9o4dtsrj2sD1DUPwEOT6O39QOURwfDQ3TdVvUMiynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیگر هیچ لحظه ای آرامشی نخواهید داشت. هر ثانیه از زندگیتان را به دلهره تبدیل می‌کنیم
You will never have a single moment of peace again. We will turn every second of your life into terror.
#WillPayThePrice
#تقاص_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/659153" target="_blank">📅 07:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659151">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9FALzmd5B3vpMw8TwOSCdkijy3dlJa395nKuQg8qbYC1YHBiskJBW1qGt1gprTjplJnbq_1dvp-hnM3Hl2d8SkIpA7EPrBXpql-giptDvN2z9FFVsLvUlPfclhx4X1pmBnL2tzyCxazutEP4ZVeIWXX03I6E2tKIYj55_tPD9Do0ZsdVZGso30wt0gyVRXlqaF8TE26VcTbynD7m53YqERrKS_9Xr5ujULD87QUu1mSMwCSRovDOiGZAd3RCOI3tTq5aWXLIce7dfB9LPjU_sBIOF-HzHnzWNy59uDTTIycp1JteMCGmkS6xjs9oBqqo379GFOwZ2wlVMb0ThJixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زور برزیل به مراکش نرسید؛ تساوی در دو نیمۀ متفاوت
🔹
🇲🇦
1️⃣
🏆
1️⃣
🇧🇷
⬛️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/659151" target="_blank">📅 07:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659150">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آموزش‌‌وپرورش: ۱۳ تا ۱۵ تیرماه احتمالا امتحانی برگزار نخواهد شد
🔹
همچنین تمامی امتحانات دانشگاه‌ها و مؤسسات آموزش عالی کشور که زمان برگزاری آن‌ها با مراسم وداع و تشییع رهبر شهید انقلاب تداخل داشته باشد، به زمان دیگری موکول خواهد شد.
🔹
اطلاعیۀ قطعی و نهایی به‌زودی اعلام می‌گردد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/659150" target="_blank">📅 07:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659149">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epwFigMeczB_7G8vFXKvH8NcoOsJOQZXwKazofOy9YoU-_bzk1iv9xuBSPn5YTiH69Gi98yaOIYoitXSlfwK-I13qrekkfZkk7KLwh_BYqvI3DNG9QxmgdONbtaC7uLxW5LC9jcPgYyFit0sgB-iuKC-mqq0yNoSMnJR096nT0FhRQSazF0U86dQVcTDmMEw4l7-tgE4gDBZkfBRPyZKXIbW4Sy3_JsZDHs5JWVZtsd6rdkVzYZN0dklErJWlPNzMu3zGwSA3loLMo17QoYYh7nGaqkvlWG7gkcnxq8VNPSm51wwU4J7SbSsgTqkP-Z10qEqGtXS6MVVZHqu2kCteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۴ خرداد ماه
۲۸ ذی‌الحجه ۱۴۴۷
۱۴ ژوئن ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/659149" target="_blank">📅 07:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659146">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
قطر با تساوی مقابل سوئیس، اولین امتیاز خود را در ادوار حضور در جام‌های جهانی کسب کرد
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/659146" target="_blank">📅 01:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659145">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsJ2fNPim-fvTXPrhGc-N_fhpCOvD29bSIFAnSeGN2znBk3rU42t3vTEZ5sriSTxyECw_UL7o7dnf-hV8cgL6Bgj2aph22XMt_4-wbk01IBOqGBCF61hz37eUkV-YH6aH3WWmFyRRk0IVaHd9LoYrsYl6FO8Zeuwtyx8k1vLrDU383QF5kDgobYK0s2HKZMNWL-QB1M-HBNEBSztMThm3VEUdJ9GyPl3UTPylnpj4-EhoAIb20XIP4vcQvPsTj7J0HJYi9efBrBF85o78D6P9iGoOOPk2J7WfGfIsJmi5qYe_cW4v9ejK0-ok5iR4F-_-FifEA6ZR4IBUEL01vrplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله میرباقری: ‏
🔹
مطمئن باشید مذاکرات جاری، ضعیف پیش نخواهد رفت / رهبری صحنه را کنترل می‌کنند
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/659145" target="_blank">📅 01:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659144">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
آخرین اخبار از توافق و جنگ ایران و آمریکا؛ احتمال امضای توافق طی ۲۴ ساعت آینده
👇
khabarfoori.com/fa/tiny/news-3222545
🔹
ادعای ترامپ درباره نابودی تاسیسات هسته‌ای در اعماق زمین با بمب‌افکن‌های B-2 پس از توافق با ایران
👇
khabarfoori.com/fa/tiny/news-3222777
🔹
شوکه کننده: کشف جسد کنار کمپ تیم ملی!/عکس
👇
khabarfoori.com/fa/tiny/news-3222565
🔹
فراخوان برادر داماد رئیسی برای لشکرکشی خیابانی علیه توافق ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3222722
🔹
زمان و مکان برگزاری مراسم وداع، تشییع و تدفین رهبر شهید انقلاب اسلامی اعلام شد
👇
khabarfoori.com/fa/tiny/news-3222672
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/659144" target="_blank">📅 00:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659142">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/No-8wHHKFSoV5dBXJ1FpYpMprB2_7zUxUcbloeOUj60vbXxyhK3oNgOgny_YCpkj2BbgasHuJwGifxVN2QUzRGM1vs0BLIf1BRBDl5JNtDHXu3iG2__p4qwDwXU0FrcLVXpB1NZOQxWlMd9V9WqowrlhgJrVcwiX7GFGl7V7MpMB-6MwrcymFqKw_rInOk3PPg1VcU7HnMCqsDy4NJs_QwRg34sQPm1jmlUxy_bFPwAMRh8eEtj_C4JzH1hRdNOe-aDAExQkYPD0iF4e6jgCvbBSlm598_YuVWDYU9-E_VUUJ0u0ll2Sh5Rszw96JP4zZt2wd2ehXVr4j5yOZeLnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSXnc_i5LxjCnzBq5M_yvCnEVJDY30-cCXFop4gvGdXER6bC6UR_Xzf42yC0RV0maQr-Q8D6CrxD1uBVqPTf1nWTto0HypX2_BIPOf_DQCU8ZrKdLyMtl_fTjEoYR-jNRzNrzlGkq3cdC7h_GuN1lwjYHnk_3x2XaxAOmb95jZ-kXevtTOkk0zy2uR7khbhiystm1C0EviFrt0c3aemTqjjcTwqFuiog9V5mNYWoz7HPw3chtTT1oWlzVXUb5ExWx1NlB6Ru0SKDtMXq-Ru76jw044--ePnaheiP5iJuljVSI5OazYQx7qiJQd0lpJo4cNJaGBdur5ZBvB8Z9WR2ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صرفا جهت حال خوب، ماه - جزیره قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/659142" target="_blank">📅 00:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659139">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP8hdHkYoflJZ_Mgb_4zeDHKzjsSBRSEwe2OURlrqnB_7FCC2tYzsZ--Maq2PMCElNj7-flFjiZ_mzJtLJRrA1_duzO0JC8skkhuAGtKtBGIDQKLdjmZ3ovdGJhOEjTHh-u-kpVo7zR4_3XOx-tRKw1wD9cVlhnUzfarhcqGqtpWyA9v81grrawuVKhaTF7fp78b2nGlVsucHvChRotWujOo3s0lgWTQZfdh6Hd8wlhks-b_ZsLLrrVyPUn1WdqciynZI1_JmrcGASm7jCFaVKz5EMthKe18hJ3q361YCSb_aAgUehW3NUVHA-Q-sEv-65E4Njc5SvWzuqpq9sWTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659139" target="_blank">📅 00:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659138">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roizOAh9xoSayTclEA5C6i4a88bBbYEMEPPvjQhU5B6yoD29SR8MzKDfH0Ift83PMcv8ASaQ1fDXm9DRI_kR2YFVsuzxUkGgBxchdTkyk2QHpMTptZvI3rPsJy62xKLQM1Ifn5jHcXAH34_bwyFbAOlTzP7qM1F4PMq5cK-LxNHY-ps_B2zaqtQ9lGoYQwcsykKDdL4rIFnmvtJ4mPBCGfEIc-yUWT6dxRlMMPm4iBlyfq9zc4TNdDIrM2tLv16LGLdUm4Zk-USCrYDbd0F7MY-7dFwzAlVoaYOM3D_qRSAtGTg0gfGJyfNbv1W9GtqX4tUIzwthJr31DMFHQZpqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ متوهم: فقط ترامپ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/659138" target="_blank">📅 23:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659137">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/659137" target="_blank">📅 23:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659136">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
خروج تعدادی از هواپیماهای سوخت‌رسان آمریکایی از فرودگاه بن‌گوریون
🔹
بنا به گفته شاهدان عینی، تنها تعداد اندکی از هواپیماهای سوخت‌رسان آمریکایی در محوطه فرودگاه باقی مانده‌اند هواپیماهایی که پیش‌تر نیمی از فضای محل پارک هواپیماها در فرودگاه را اشغال کرده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/659136" target="_blank">📅 23:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659135">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
مطالبه ملی از نهاد مرجعیت: صدور فتوای مهدورالدمی برای عاملان و آمران ترور رهبر شهید انقلاب
🔹
امروز مطالبه خیابان‌ها نسبت به ترور رهبر شهید انقلاب در ۱۰ اسفند سال گذشته، فارغ از جایگاه ایشان به عنوان یک رهبر سیاسی به جایگاه ایشان به عنوان یک مرجع دینی اثرگذار در حوزه بین المللی نیز معطوف است و این ترور تعرضی آشکار به مقام مرجعیت در جهان اسلام تلقی می‌شود.
علاوه بر این، تداوم مطالبه‌ی خونخواهی مردم در بیش از ۱۰۰ شب گذشته در خیابان‌های کشور، به وضوح نشان می‌دهد که جامعه، این ترور را مصداق بارز هتک حریمی می‌داند که امنیت ملی و دینی ایران و جهان اسلام را خدشه‌دار ساخته است.
در این میان، نقش مراجع محترم تقلید در هدایت این مطالبه‌گری، نقشی کلیدی و راهبردی دارد.
🔹
امروز خیابان فریاد می‌زند و از نهاد مرجعیت انتظار دارد تا با بررسی دقیق این ترور ددمنشانه، فتوای «مهدورالدم» برای عوامل و آمران این جنایت و در راس آنها ترامپ و نتانیاهو صادر شود.
🔹
صیانت از حریم مرجعیت و اقتدار نظام سیاسی، ایجاب می‌کند که این مطالبه‌ی ملی، در قالب احکام قاطع دینی بازتاب پیدا کند تا راه را بر روی هرگونه تعدی به ارکان دینی و سیاسی کشور برای همیشه بسته بماند.
#WillPayThePrice
#تقاص_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/659135" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659134">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcDM7fV0WLO6Ig850Ab4KZhRGjUvwQV8HDV3AqtaU0AxQMbHJuvVtRno8EryKQ8bQnDrD271AxfuROhkiUy6xyLWyL7H1KH2_rg645Tp0u1ctriulOIWoakhJHpKhF-1Fzu8BmlCAFj_UnpbXvDi8ESswl3TgJxMoGp5mWfvc0r33N_OJt37ali0f5jhYdBPwHELNInXpBpnAqF2kcNJHSXUOgot7-yaw1mJqaZZm0A88lALy9UASH_nE1C1wdYPjepahlt28If7f5ru-2CydBW2uDKDB2xYoLgRWv1xBtOXezkoMnVAN_-6smC_QSkxffoTMMHkpGbsowr6HFqFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
تجربه یک جام جهانی مهیج در نئوبانک فرارفاه
🔹️
اگر در "فرارفاه" (
https://www.refah-bank.ir/fararefah
) دارای حساب هستید و یا با افتتاح حساب در این نئوبانک، ضمن شرکت در طرح "فرالیگ" بانک رفاه کارگران همزمان با برگزاری مسابقات فوتبال جام جهانی ٢٠٢٦، از جوایز ارزنده بهره‌مند شوید.
🔹️
مشتریان با مراجعه به نئوبانک فرا رفاه و انتخاب بخش فرا لیگ با اعلام نتیجه بازی پیش از شروع آن مشمول امتیاز می‌گردند.
🔹️
در پایان هر روز از برگزاری مسابقات به مناسبت شصت‌وششمین سال تاسیس بانک رفاه کارگران، ۶۶ نفر براساس فرایند قرعه‌کشی و با لحاظ مجموع امتیازات کسب شده، مشمول جوایزی تا سقف ۲۰۰ میلیون ریال می‌شوند.
🔹️
پس از اتمام تمامی مسابقات جام جهانی، ۳ نفر دارای بالاترین امتیاز مشمول جوایز به ترتیب ۲۰۰، ۱۰۰ و ۵۰ میلیون تومانی می‌شوند.
🔹️
مجموع کل امتیازات هر فرد و همچنین میزان امتیاز سه نفر اول در جدول امتیازات بخش فرالیگ از نئوبانک فرارفاه قابل مشاهده است.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/659134" target="_blank">📅 23:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659133">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f92a2a9d.mp4?token=rdRgFeseOLQcXGhS_UUC-01p4MHsU8CRkEVQeraHRwUeWH-e5-KHu2THm-aSS2NcaQC2uQ4XFLvAggqCkyqXdWlCPL2PkRwHSvLZv9v-gP1w-ZR2BoUKoCzduTlfHlmU7mb4v_pu1ERyJnoFne1Uut9aTwQq1OGFfWfsEQaPMfirJZHmW-FWTtc_BIv2UX0rvIeci_1fbfAGY-TDSwJmIN3GmSMgcz47jAzsvlUF3Fj9-VstuLUM8lB3_RiYT944YXtiZhz1d01WZTKBw9JWvASTeiQRjsUox68nw0MkOxVe8i5b1AIykjy8Ljw83n7FMZFN3W38ES1Y8Rg0-1VQPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f92a2a9d.mp4?token=rdRgFeseOLQcXGhS_UUC-01p4MHsU8CRkEVQeraHRwUeWH-e5-KHu2THm-aSS2NcaQC2uQ4XFLvAggqCkyqXdWlCPL2PkRwHSvLZv9v-gP1w-ZR2BoUKoCzduTlfHlmU7mb4v_pu1ERyJnoFne1Uut9aTwQq1OGFfWfsEQaPMfirJZHmW-FWTtc_BIv2UX0rvIeci_1fbfAGY-TDSwJmIN3GmSMgcz47jAzsvlUF3Fj9-VstuLUM8lB3_RiYT944YXtiZhz1d01WZTKBw9JWvASTeiQRjsUox68nw0MkOxVe8i5b1AIykjy8Ljw83n7FMZFN3W38ES1Y8Rg0-1VQPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای آهنگ قیصر، خواننده سابق لس‌آنجلسی برای تهران در فینال رقابت‌های فیجیتال جام خلیج فارس، یادبود شهدای میناب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/659133" target="_blank">📅 23:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659132">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEX8gqIs8zj1AR1qSYDBDiHrbcxAOs1ljdqnshnt_wTWvqVOfT2gki5uLr1oPGMfZyHSpCq8HcZd1lxUyDXdETILqQ2cHHdq5cftUlM4u4KOW2FFOdEtvzzrmLPfvuyLrzg7KaDd4IIOfgaHbh7XF1hAsXTuVjcf5bS7KHXYPxDrl8hQ9HmG04hrUgzB8dp3SaKOQSoDrN23U0-eP6q9gfj0wfg84cTB5o8axrCPVnA4Gth3rasDJCvjXDqVnZTtDWCBy6UkBWYBePuEz3qwjd9oG9u6iNTd3XU-_KFqhV1TTCxkhJKhrVJhgdjpRz2uY-nwk_7lbuacMgROQRJHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حکم آنچه تو فرمایی
🔹
گمانه‌زنی‌های رسانه‌ای و برخی نشانه‌های دیپلماتیک از نزدیک شدن ایران و آمریکا به یک تفاهم مشترک حکایت دارد؛ تفاهمی که گفته می‌شود در صورت نهایی شدن، به‌زودی به صورت رسمی اعلام خواهد شد. طبیعی است که چنین موضوع مهمی موافقان و مخالفان خود را داشته باشد و دیدگاه‌های متفاوتی درباره ابعاد و پیامدهای آن مطرح شود. با این حال، آنچه در نهایت اهمیت دارد، حرکت در چارچوب منافع ملی و سیاست‌های کلان نظام است. هرگونه توافق یا تفاهمی، اگر محقق شود، باید در مسیر و چارچوب مورد تأیید مقام معظم رهبری باشد و همه جریان‌های سیاسی و رسانه‌ای نیز به این چارچوب احترام بگذارند. در چنین شرایطی، وحدت نظر و پرهیز از دوقطبی‌سازی بیش از هر زمان دیگری ضرورت دارد.
🔹
هفتصدوهفتادوسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/659132" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659131">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959dce732b.mp4?token=CRKZ3BbInN_wOp3ugX4XB2B-alPJog8ll10HpxVp3Tdr-2lEg3T8QahMYKsqARXHM2NjpltcI1NwYs2I0HhGnMBJ4h1fkab8rJ-RiNhOdmrBlffPZn1ecXk3O8uAPKeod3cnPtMAw6bVRPU0uBdEF-5CCweje_yipojyfC3p51xXA3VLs1Fq__Gv6qJlolCPcCR8Qc2RIMxaYSYnCZya-V614vtJ2STLvQ_1AaWYpGOgZT927rvgdcFxyMlCdYgBVyzU-unMnL5McqvFQGYHDs7Z-8oQUC9CyyGXgJRqB7fKuAxlBc11U5trDD6A5lhWC-CqbN6zf5W4qffKGKYI2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959dce732b.mp4?token=CRKZ3BbInN_wOp3ugX4XB2B-alPJog8ll10HpxVp3Tdr-2lEg3T8QahMYKsqARXHM2NjpltcI1NwYs2I0HhGnMBJ4h1fkab8rJ-RiNhOdmrBlffPZn1ecXk3O8uAPKeod3cnPtMAw6bVRPU0uBdEF-5CCweje_yipojyfC3p51xXA3VLs1Fq__Gv6qJlolCPcCR8Qc2RIMxaYSYnCZya-V614vtJ2STLvQ_1AaWYpGOgZT927rvgdcFxyMlCdYgBVyzU-unMnL5McqvFQGYHDs7Z-8oQUC9CyyGXgJRqB7fKuAxlBc11U5trDD6A5lhWC-CqbN6zf5W4qffKGKYI2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم فلسطین در بزرگ‌ترین میدان نیویورک
‌
🔹
هواداران مراکشی جام جهانی پرچم فلسطین را در میدان تایمز نیویورک به اهتزاز درآوردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/659131" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659130">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859711ac57.mp4?token=UezXZnKoPonc78Zxjd4xaHXZi2X7ylgSWjYTjkLvpFwRczhlVyTFGDRDIPKxluMx0MccB-dn9bQ8gMDgQ8sjj0UYsTiEDDeWevXAE97qMIJLxEfrN020vf6bTPNSNL_8BhFI9rjbnhvbEMrYXA-5EKiPnNF4gc2KZoWOG8uurKc8CMeS3kR7nJrFNxLGfy9r9WQIJFMm0CJ7eN3Bk6QBryoKzWuYuiZI3b7htcf1mhTDs6teC6n3JjMr4rUyisdZJdkziTo7O0VACwvOG8xeQuTS4yawdRx-hBv8g8d_duDnTwTOznFxYSyFV2IvxcClSInmY1FTwuZmQ9eUBXjqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859711ac57.mp4?token=UezXZnKoPonc78Zxjd4xaHXZi2X7ylgSWjYTjkLvpFwRczhlVyTFGDRDIPKxluMx0MccB-dn9bQ8gMDgQ8sjj0UYsTiEDDeWevXAE97qMIJLxEfrN020vf6bTPNSNL_8BhFI9rjbnhvbEMrYXA-5EKiPnNF4gc2KZoWOG8uurKc8CMeS3kR7nJrFNxLGfy9r9WQIJFMm0CJ7eN3Bk6QBryoKzWuYuiZI3b7htcf1mhTDs6teC6n3JjMr4rUyisdZJdkziTo7O0VACwvOG8xeQuTS4yawdRx-hBv8g8d_duDnTwTOznFxYSyFV2IvxcClSInmY1FTwuZmQ9eUBXjqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویداد تخصصی «نقطه تصمیم»
آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند.
جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود درباره بحران، بقا، رشد و آینده کسب‌وکارها سخن خواهند گفت.
یکشنبه ۲۴ خرداد ۱۴۰۵
ساعت ۱۶:۰۰
مشهد | هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774
#نقطه_تصمیم
#DecisionPoint</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/659130" target="_blank">📅 23:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659129">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCri3s1SJ5qbTd9dXPXqm-BYEU0OMpoR_Zc4XK4HP00MMRu-4yKLWjiYoqApAfN7P0fSGZY2z6OOnmCqcxIeWUQEGof0zZTpi1GKM9KzO5GIYGVar-nIUW0dV0i5g2tYs41baX5UiZk42jb6NmFLVJikYjxyp7axjUAa-avG0KpT7EOGDRe6h1SIT6ic388PvWGQt1jH0FEixdB4qnyBp_hZCf2RIcrJCP_clQciiUvq9x5hreIdbJO1QfMyvGsd9F4E_mBbZuvWBVHxXg0dP5E7FNxy8LuihWOAeZRbD6QuEYTCsjtUNkZcHBs_RCf3zKZsT040kqvS1aul8rrgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
The cries and sorrow of Minab’s children will never leave you.
آه و افسوس کودکان میناب رهایت نخواهد کرد
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/659129" target="_blank">📅 23:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659128">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5WuJBCNqzYRR14l5EfcIwHRiHU-6J7PiwfTVMGA5rwSXb-niYDNa4gfAfPezDKdywTk2SRrkRftDN0iVEldBHong1sJqUukxgerawXm8hN3EQm_Z31fzOByeeXYsX6Bi9PZn4zh4uDh6fLJR7wjHOvkx7dc568r9_g6uQH84HD5ilhr-5tvG-Azrsp4w93XsitQ9102x_FSForgmDbBYmiAG_Z1z6Vd6KSDBmi8iOlgLRHDI9LnrdT0xqgHUAFW4ni-ayEHm2OUIVMmW0EebTt4-tVuIIVU9AzLyytn9U2GO2uWTl2__jBkTZZJbtqHV3_I1aYzp4Cx9N5wu0V5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار وال استریت ژورنال: ترامپ گفت فردا امضا می‌کنیم. ایران می‌گوید که این توافق نشده است
🔹
اصلاً تعجب نمی‌کنم اگر دوشنبه صبح به وقت تهران/یکشنبه عصر به وقت آمریکا باشد. ۸ ساعت و نیم اختلاف زمانی.
🔹
فقط برای اینکه ایران بتواند بگوید ما در روز تولد ترامپ امضا نکردیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/659128" target="_blank">📅 23:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659127">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
رهبر انقلاب: وحدت ملی از مهم‌ترین عوامل پیروزی در برابر شیطان بزرگ است
‌
🔹
از جمله مصادیق تقوا، رعایت نعمت عظیم وحدت ملّی و انسجام بی‌بدیلی است که حول پرچم ایران اسلامی به ملّت بعثت یافته ارزانی شده و در زمره‌ی مهمترین عوامل ظفر در مقابل شیطان بزرگ می‌باشد.
🔹
شکر این موهبت، اهتمام آحاد ملّت خصوصاً نخبگان فکری و سیاسی از جمله نمایندگان مجلس به صیانت از این وحدت و پرهیز از اختلافات پوچ سیاسی و برجسته کردن تفاوت‌های اجتماعی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/659127" target="_blank">📅 23:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659126">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPGRGuz9PiebSL4Q4To-wHdWhAJf2e3wmKyoKbDp35cwUGbQwE91izto3WUIXfDhgTMgh1sclHtRFx9c8doVcVhMwuLZBLvMsVfJC1t-MYtkfiWb6Ka3tegUnQ0ktTBF31sufdcazoTDGIGUJI1TbGEUanpZCY8px28QrnsAaM5r3WU_jvK5rrx2rcehx6CGCIPPkHq-VxlE0k0LsFCmqTxDzGYCiJElFVoDeWfrgBV6os1Qyea-brK2lsxBhogZkvxlm7QGeHhPIDbX99YYoNdgjlz8xCYrcJieIoCKg9GDQ6uYXsK0dInJac7efHqP-JgSXb9_Dq639ggbaHH_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایه‌ات را به کابوس همیشگی‌ات تبدیل می‌کنیم
We will turn your shadow into your eternal nightmare.
#WillPayThePrice
#تقاص_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/659126" target="_blank">📅 23:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659125">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: مقامات ارشد اسرائیلی می‌گویند ایرانی‌ها بی‌دلیل با این توافق موافقت نکرده‌اند، طرف آمریکایی شرایط اصلی آن‌ها را پذیرفته است
🔹
به گفته آنان، این توافق بلافاصله منجر به رفع محاصره دریایی و نجات ایران خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/659125" target="_blank">📅 23:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659124">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رهگیری جت‌های سوخوی روسیه از سوی جنگنده‌های گریپن سوئد
🔹
وزارت دفاع سوئد اعلام کرد جنگنده‌های جی‌ای‌اس ۳۹ گریپن سوئد روز شنبه، ۲ بار هواپیماهای روسی سوخو۲۴ و سوخو۳۴ را رهگیری کردند.
🔹
وزارت دفاع سوئد اعلام کرد حریم هوایی این کشور نقض نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/659124" target="_blank">📅 23:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659123">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO7_H1prvA2rXUKODv85Ux8MHVGCzFJmyU85ioogU7Xs6UHGEUK375io9DLUDFom-TA_4tSs6SsOhi1SNhsSH3AL_C-eZ9wUWEA1JRsfP0nigemGcvF_xVb1Ps_uH5R3F26l0c2Rj-U0_SFDHraxuzkUbJgiWpvoedzE9PTGEaj7et7ohDfnPUd6pwjMYhXGTuL-waazyM68r7Wr2E5W1PnwKnpi3DpSbutZvqmV87U6f_xTGAFQqgzl1f6VTMTryIhsqKyd6bf-P_Qw3mLFuHn1x_7czvuN71rZqGla1SfYNFiGaSqj0wojD7u5KTopE7QfRLB-3m30gRLtr4F2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت بیمه مرکزی با تمدید یک‌ساله مجوز قبولی اتکایی
#بیمه_البرز
بیمه مرکزی جمهوری اسلامی ایران با تمدید یک‌ساله مجوز قبولی اتکایی از داخل شرکت بیمه البرز موافقت کرد. این تمدید بر اساس ضوابط و آیین‌نامه‌های مصوب نهاد ناظر صنعت بیمه صورت گرفته است.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5046</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/659123" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659122">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اختلال گسترده در سرویس‌های متا؛ اینستاگرام و فیس‌بوک از دسترس هزاران کاربر خارج شد
‌
🔹
هزاران کاربر در نقاط مختلف جهان از اختلال در سرویس‌های شرکت متا از جمله اینستاگرام، فیس‌بوک و مسنجر خبر دادند؛ مشکلی که باعث خروج ناگهانی برخی کاربران از حساب‌هایشان و اختلال در ورود مجدد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/659122" target="_blank">📅 23:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659121">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H55yZ201K7S7iYFAo2o5oc9KFCHYLrLWPefrmqmbDnEuMU6hopYVcVClRmJd_vBPmvQJlCI_9NxIMIfY7jxuopN_yfm09i2iGoU2b4GHaZMz0DVXq3hT15sTUmUI2v2FmeJSgz9iETFgKDcT85NOx844sbyRIH_65PpvlgH9Bd8L3oEnw9Ol-o7XUf4vZ8eo1gS7lcmbxXjix-yjLMIcqJ6jpZi2EgW_uHhJv1RoXg3XMe5TUIWLh4rVn_V3mzGOkIQ7cGkIWgm18--rlnF2mUHsVhth6KFp1mT6jraglVElGwOq5P_lS2-f38afCOb8TMlF7AaM1Q1sZupOiucyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا تولد ترامپه!
زیر این پست یه تبریک ویژه بنویسید!
برای هدیه تولدش، هرچی فحش پاستوریزه، کنایه آبدار و طعنه خلاقانه بلدین، زیر این پست براش بنویسید
پیام‌های شما در رسانه‌های خبرفوری منتشر می‌شود
در ویراستی خبرفوری را دنبال کنید
👇🏻
https://virasty.com/r/BWcv</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/659121" target="_blank">📅 23:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659120">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715e5146f.mp4?token=H-5caifMr6R4s8JKCcFBjRYg3VCILPeezZ8mAXYcqnVDPXrcDl5dy3it8bfSp18u0FTOl5y8yT2UBC2tka5lc6mBWXC14qoloO7xoEITFAOhZpLrIiPc4tfO0Iq3plhOtwq982YzpIObI9VsnIeVTvqN5uoxHCLqgcuhQfx1BFWGpkNMDC6Ny0MlNXH_cVxgoAcdGqZIcl4ywUIrLm7wgEc2Gf6F2B9ylXHaO9LHXPfMfhuPoaeyGkLL2D3qlQ7vL58-eOiXBCaOM14DheWxP4l5MD5roVaJtgOYHBI1NPkphCmt0siaf_jVGj6d2brufcinNqO_qAsX2vafxstElA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715e5146f.mp4?token=H-5caifMr6R4s8JKCcFBjRYg3VCILPeezZ8mAXYcqnVDPXrcDl5dy3it8bfSp18u0FTOl5y8yT2UBC2tka5lc6mBWXC14qoloO7xoEITFAOhZpLrIiPc4tfO0Iq3plhOtwq982YzpIObI9VsnIeVTvqN5uoxHCLqgcuhQfx1BFWGpkNMDC6Ny0MlNXH_cVxgoAcdGqZIcl4ywUIrLm7wgEc2Gf6F2B9ylXHaO9LHXPfMfhuPoaeyGkLL2D3qlQ7vL58-eOiXBCaOM14DheWxP4l5MD5roVaJtgOYHBI1NPkphCmt0siaf_jVGj6d2brufcinNqO_qAsX2vafxstElA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم هند تصاویر ترامپ را پاره کردند
🔹
در پی کشته شدن سه ملوان هندی در حمله نیروهای تروریستی سنتکام، مردم خشمگین هند با پاره کردن پوسترهای تبلیغاتی دونالد ترامپ از روی موتورهای سه‌چرخ خود، اعتراض خود را به سیاست‌های آمریکا نشان دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/659120" target="_blank">📅 22:52 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
