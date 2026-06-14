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
<img src="https://cdn4.telesco.pe/file/ByJo-9dl89Khdp4gk2KH5hMFuiT452PcrZi90zHfIs75IwHbZB6rYJgkT6DzNhuVUQoDv832gkclwpTzaX_cysIlIBR8AIPACTNcGXlJybR-IsGuR3Xe3ti0whTYux6uUjSzM_lIfb5wacgCk1lC7CbfBBSBG1aIXU4iPCbFZg9mwI3QifZAYkNM20cAViU1OOjuFS_VXvdHPPtJ0leyyzOWpPPBNcDr3DCxXfqRpYqcgJPFWZBhRBgnVBgF3RyNVTuOt9jCPuheSRZJeM3isMkzZeklhwwGCjVg5NVQfu2iuTiS-3XFjc08PfKdr-V7Cpv8labVVcMU1yaJz1p-Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 245K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 18:06:42</div>
<hr>

<div class="tg-post" id="msg-23445">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOpuwLucMeGfM7UnAebsBeWSs5w-fDOxkC0e8hVGCCXvfQCrshlLiuUWTXwoqCnJm2Kx5dL_DjjmbEp85Pxs_qKDtAcd3IyxWfjqf0m3QzBS6OJ9COZ3ESPFDFkv4HNXVKoZZYfCSICKcMOh5RgEf-Y6h_6J2LGSyqKU2b2X5s8Ag0S325CbenrbkJA7IsfQK9b7WbqMKxh3ZfQVKkoxjNWSPK353kGUu4jYzhJvHKSetBOCqXYTaU6F4Eu06ViVU0XGXXX9Btq1uRbwy1SONJYOh2ZfiHTDWtZyLzKy6Qb8W2qnwDqphS53paPlE9or16vKgwWMJ__hymbTuvmySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ ایران میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/persiana_Soccer/23445" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFTV14vMzcjpl2tfzV54lzj8oNLV-KxGWGJvErTdorhdGssfxraDZifcPmlonJ24vzYcGqSXN671YqcjQUCpzU-6E53HVd-U9VN6RPY4mMgDLpwUpMOzfP13vL_JsXIiSrLz6icqUZfehUAZHkE91KwLB_wHjnZ7SYiOznkBPuQWM3VdgAR8Ydzhavfm-G1mGqDnoja9AQ7NBl_lvbkHZUxjmqzYB4ODkqrFeGnJPWblrmZ78fvEtlt_bLAejAAIvZ_8csl9wHBlvIEHHgDaIVJe6jvRpzPDm-ruMjQ4vpHYFjvOYwlfp6hqC3vTktsCYNP7tZHIkT2w5S0zQsrEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت اوپتا پیش‌از دیدار ایران و نیوزیلند، شانس پیروزی‌شاگردان‌قلعه‌نویی را ۵۳.۸ درصد اعلام‌کرد. در این آنالیز احتمال برد نیوزیلند ۲۰.۴ درصد اعلام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/persiana_Soccer/23444" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=CHC-jvhmpGfhImjviKe9LSgh7jX8aYORPLFwzEpf_88OZD5w9Rg6bKoapQi0KE1jXXXqja_vP-3jKH8-rXAsUxkOxd1sLqv5IM7XJZROMwwQusB-Y2cHBZVexMMbqweSZtz85qoG1zdjwnivDobPpr-VTUEZuNVZmqURHYZ-bRxNQSP-HMXJlQ7FLupDQN4Jr993Jz6F_aaBhd4Y-IxjyZtCzQFS3KB2YcFsMbsVy30sheRN-y4z2skQ3s3fc27np7D8LgtbgN-zfzNSiz7QL3deHfFcTv1bRL3PTy7FG7lXHRid7VvdwXuaXkjFJvYfpvSqbjciFoHdJoDqqkJMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=CHC-jvhmpGfhImjviKe9LSgh7jX8aYORPLFwzEpf_88OZD5w9Rg6bKoapQi0KE1jXXXqja_vP-3jKH8-rXAsUxkOxd1sLqv5IM7XJZROMwwQusB-Y2cHBZVexMMbqweSZtz85qoG1zdjwnivDobPpr-VTUEZuNVZmqURHYZ-bRxNQSP-HMXJlQ7FLupDQN4Jr993Jz6F_aaBhd4Y-IxjyZtCzQFS3KB2YcFsMbsVy30sheRN-y4z2skQ3s3fc27np7D8LgtbgN-zfzNSiz7QL3deHfFcTv1bRL3PTy7FG7lXHRid7VvdwXuaXkjFJvYfpvSqbjciFoHdJoDqqkJMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برخی از حواشی مثبت هیجده و جنجالی رقابت های جام جهانی 2026 آمریکا از زبان ابوطالب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/23443" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1q5_tkr583yZlcmGNxW5hMW-71q1vvHhWsMjZf6RHv6Co9Hv8RSO0NlUUjUJ3_cogtu5vl-hhK6wCuJJEMV5JCOlTOUw3omxFEgZCCssiq8Y9S8VdW83S0cXfoxndHc9snljmeC_kjwCj4mWv0OSxVPi_FG80CS2BffoyBHH6DIN6pTltFlGmZi2LIIKKLsy8TA37bM463_R9juhASGriqAPepzWqNbV57As0H1KIKKftgqzyGoxwrU7TiLGxbSBOoBjC__irxFPv0XNDRottOZrWfErnvXLOJ-BoFEC_YfNvH-vP54E8A0JLKLRIMmVnhn2OLkk7KvIcIklEQjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
صندوق‌سرمایه‌گذاری قطر اعلام‌کرده که بوعلام خوخی پس‌از گلزنی‌مقابل سوئیس در جام جهانی 3 میلیون‌دلار و جدیدترین‌رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/23442" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHcHKWeys1V4YFOenaLFIOe5PFhKWBJMXlbAJN34TlzQvbgmUQiWjBGcq7A1zYvD6iePEV1hpyvq9bQ4d66o3yfpbHT6C6Hy82bWIjIdGV7cZ6MKtQhnbgAqHfD7elEETE1fxj1i-WrobG8jzInr-_uE1UNiPE2apP4UqTsXHkLtCxVGYnbWjTJ7HInXfqR-_5Be7zof8kTocceOWkzqr9cwXneliOgfce8TMq30wQy5_m4K0csYaYZXN85WFxQ801YYlzAWqRO9UWlpyhQ8xK5hk1mRjh5oWlPn05g4nLfWr8W5gbP5pEMCReDW95v0Wrhdw7_iRxwiTU_xVUuDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی قطر
🆚
سوئیس در هفته نخست رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/23441" target="_blank">📅 16:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ6VTCl2qm61B9Pt6lkcg7Xjq85KGLOAArL6hVwicLhdI90jgJT03f88h8CuHqazQLWXY-7qWH_ZdW98zifQbyDFqVSZzevFehErfCXfMp36TDCnDKsdJTF4rFDEdYvObkSYiLhyTTx6QO23s6hqhpiw2cpigj1pVDfRTHk3xt-hbtDp6MtEIig1os28HB2ftpRY7SFaE8C7PAfRK-CtzqWR4wbgdUAqFgZJiGdKB-vqPuuVjCnjcN9IjmWRaG7Mp9lGfFIJ_QG4h_gmx0HldI6-w-RtPk7Iyu7BeIv2tJeCjtV9OV5gTJTgZn6xcXRMZrTH72lSDmsTX7Z_0epqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شبکه‌های‌رایگان‌که‌مسابقات لیگ ملت‌های والیبال رو باکیفیت‌بسیار بالا پخش میکنند. امروز حدود یک ساعت دیگ تیم ایران مقابل بلژیک بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/23440" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOBrNbH-sTkwz6UDrgr7cBaJWiAs1gF-o20xt_Y9I9ha9uo0KFC03iDQFwmiUwgPGjwzpu7eE-qnGQOl8rrflw8ONYm55oRl9QrEFoees-xVA0QMh76NlMBmVr8aCZnHm397Ht8QypZiusfwXwVbuEVA26o76HPOHgrKDqgqMVGSmCgCxAtIuG1CCCFyeiB1-d6qsDXgO3O4IaF2OGrpLkSUwMhMev6TRZsiYrZvNCgTvqIXp4JOyHM3lK0y7Cxk6LSPFJvv4HthBayv6SWvLfAuxqD3up_C_99ocjr0jtNkyF-ld0zLRFohnKJDEGqqoeTM44XWnk1CPYpZ2iiloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/23439" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuxwslTgB-n7HFkFnf90Gf-Isc4LPl45EppHHcMlYO5H80l0XDve0kysmem_pw0eubyXUT3CWuEScx9H0_s3SgzRCWIl3G-NdPZ4sy2NrtwPtbaHZDIpdZDyShaOPhTqG8C_su61MbxsPXXVPHQRsXT9z90fkSwQbpWg04ILF0burALy6z9f8BM7yGLKRAnqY080cxvREV5xzWVqIsrEAcALaT3plvmzwiejqPH6gibrUaHkYIC3iyC5EL_LYGNxDOtycaDXnk4wRQlJbyN_rk1gum_3_PWXcNQAo9SNHpUZ4-sW01qlp31UKg5v-P73FqUCYLthPiCxxx2aXjJ4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/23438" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">▶️
قسمت‌‌‌سوم‌ویژه‌برنامه‌‌فان‌ جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید. شیت و محمد نصرتی مهمونای این قسمت بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/23437" target="_blank">📅 14:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=c20C6Jxr-RSf0TLnzEI0rN3nX2vTHfbdnaYM47gHo4xLq-D5ERUdj_Z5ftLjNUnnfctSStzklYAAccaLjOvJiOK0Ck_BYDOmloYmv-mvyImMwJwmusEdyEzTNLgzQP4xjFpWvpHTEJtI3UDiVgfDbBzCjtQJRxMWngnlaBD62M7UEHhAOrWyCIP6MwYxc8eh95riKCKDp9GqOj8fgRy5MZsAt1RS8X6PCKIX1nzISAnPZbHhm9VpgNIuICEPBYy8quYXIuJQI4VUgNzUsWSKq22SHO7XJaNqzglpuo88wAGCTNj9v6Ekn1W_Yh1KyTyX8Whu0yMSEDs6Pd2U7VRwmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=c20C6Jxr-RSf0TLnzEI0rN3nX2vTHfbdnaYM47gHo4xLq-D5ERUdj_Z5ftLjNUnnfctSStzklYAAccaLjOvJiOK0Ck_BYDOmloYmv-mvyImMwJwmusEdyEzTNLgzQP4xjFpWvpHTEJtI3UDiVgfDbBzCjtQJRxMWngnlaBD62M7UEHhAOrWyCIP6MwYxc8eh95riKCKDp9GqOj8fgRy5MZsAt1RS8X6PCKIX1nzISAnPZbHhm9VpgNIuICEPBYy8quYXIuJQI4VUgNzUsWSKq22SHO7XJaNqzglpuo88wAGCTNj9v6Ekn1W_Yh1KyTyX8Whu0yMSEDs6Pd2U7VRwmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وکیل تتلو گفته‌تتلو واسه‌ماه‌محرم درخواست مرخصی کرده که بیاد داخل هیئت‌ها نوحه بخونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23436" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=Gde4QN2ciQhgqruk2pDDu6xCIV3QjiIqzjaU52qb-wgdvea0vutjaTYzBkPX4V9TZoaKcaIEUC91ZwfBtycQEHuCew1ziNUA2gIgOy-3zRsCWu0Fy8VT8YkUBZlzZV5QpVIN5wD-a0qiIEFhIOh-GqRL1EK92bbeyW-UrnsaYAWYceAsqlTsSSkHJlFnjxeG5BPOChCn7bpmZWfaFHbq9aFCnWm8gfMIRng6zdAnb1QpKmrsIC8w01yC0rY34VClsR3blkxYK2xaSUJ1z9cULQs-RForVxJRuPZByo-LMAn2OpoL6rwDA_psWTZ_Y_3Up9NMrps76y6MHg6rCqalqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=Gde4QN2ciQhgqruk2pDDu6xCIV3QjiIqzjaU52qb-wgdvea0vutjaTYzBkPX4V9TZoaKcaIEUC91ZwfBtycQEHuCew1ziNUA2gIgOy-3zRsCWu0Fy8VT8YkUBZlzZV5QpVIN5wD-a0qiIEFhIOh-GqRL1EK92bbeyW-UrnsaYAWYceAsqlTsSSkHJlFnjxeG5BPOChCn7bpmZWfaFHbq9aFCnWm8gfMIRng6zdAnb1QpKmrsIC8w01yC0rY34VClsR3blkxYK2xaSUJ1z9cULQs-RForVxJRuPZByo-LMAn2OpoL6rwDA_psWTZ_Y_3Up9NMrps76y6MHg6rCqalqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23435" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNS7skMYVSCUtIDYjhvBMVHJoKESltv0XKr-gP42OzUNNlSeJg1y-1z1_S1nreCGJDrv4-D0VxarCpqAPFY5tiawI4amVhvep0XXAvx17xWkTGFRq_3aipbHDaV_aKlXi2Bey64I6fW9xcUZqGcmt5b12jyJ_3vn2OPcNrSv134LT5Y5B2x5AGH9VjX-Kh3z3lR7M1WFCHKin9Vh5mjzkPNLKAGYeZwehSnKKCmxwMLoCPp5DFqBZCTS0kcBGM1ZoScH9VPWvEW83ZiYVxBVaWHh8zVhZq14jYCWoswqg87cd_KWx_Ym0rwmBLRDUUX6AgMkZs_Y9FTclIH3r_LH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
با اعلام فابریزیو رومانو؛ سران باشگاه آث میلان مذاکرات‌رسمی‌خود را با روبن‌آموریم سرمربی پرتغالی سابق منچستریونایتد آغاز کرده تا درصورت توافق نهایی بااین‌سرمربی جوان قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23434" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=IcbMK3ogAUvHkVPV8SMrk6h8CQC9F2CLOe0FVRLgEiY6Yb8MGJ5qp10qUQ_fDOnP5yapOASKMjJGdAIPRXZL0U0grF5kCVpqoMdHyiLDMwlT8O071vsLTXoAhiF3DEe4paiLcXfvhRbKqXHKEO230WHRO9chlDChjTZaBkIikuBvR2fVx5B69FtMq1tZ_cpuNcipnEu34ajH6TRGbADQFmjw__oaUqCz9y2YDkcq0_GemjY2OgsZDfxgzZUdIlnLzFNYsxnOqZZ-Fj24qOIRHnm_X6b-wCwwNPEG_8Ox5G4JcM-UTGUW5lqVB2hj3A5cMCLRsdRQFKMBzwNObitbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=IcbMK3ogAUvHkVPV8SMrk6h8CQC9F2CLOe0FVRLgEiY6Yb8MGJ5qp10qUQ_fDOnP5yapOASKMjJGdAIPRXZL0U0grF5kCVpqoMdHyiLDMwlT8O071vsLTXoAhiF3DEe4paiLcXfvhRbKqXHKEO230WHRO9chlDChjTZaBkIikuBvR2fVx5B69FtMq1tZ_cpuNcipnEu34ajH6TRGbADQFmjw__oaUqCz9y2YDkcq0_GemjY2OgsZDfxgzZUdIlnLzFNYsxnOqZZ-Fj24qOIRHnm_X6b-wCwwNPEG_8Ox5G4JcM-UTGUW5lqVB2hj3A5cMCLRsdRQFKMBzwNObitbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=iMz2r2UbAJymHHwCo7i2h-rCGPFNYbPPpL6Lb3plPAE21WfLIStXJmDpburF4nEP6E2VmLewWulXgrQrvFPyhTcSFAAweOcFSvsAat-QMlksItU7mRQl6xeppl09bCRlOXzqcaxpcNdpZbYSBcBgDec_R_OXWmE7E6yVE3lhVOQ6UBdd8p_tLt7awtMN3kB2fbvjRuh3hwRl07VWJrFhvlhfyKs7cg2gnrvtKBGiDgrp8iqXiJVU4owGkbS1f5zxt84h97RclknZU3TO5RXFJAjpGZnff-MLSWsPLezxoi01EbFFTiFDqGYefvQ41xWFdM0F-F-Hbrz3DgpfR9CNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=iMz2r2UbAJymHHwCo7i2h-rCGPFNYbPPpL6Lb3plPAE21WfLIStXJmDpburF4nEP6E2VmLewWulXgrQrvFPyhTcSFAAweOcFSvsAat-QMlksItU7mRQl6xeppl09bCRlOXzqcaxpcNdpZbYSBcBgDec_R_OXWmE7E6yVE3lhVOQ6UBdd8p_tLt7awtMN3kB2fbvjRuh3hwRl07VWJrFhvlhfyKs7cg2gnrvtKBGiDgrp8iqXiJVU4owGkbS1f5zxt84h97RclknZU3TO5RXFJAjpGZnff-MLSWsPLezxoi01EbFFTiFDqGYefvQ41xWFdM0F-F-Hbrz3DgpfR9CNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شهردار شهر سیاتل اعلام کرد که ورود پرچم‌های شیر و خورشید ایران برای بازی تیم ملی برابر مصر مجاز است و از ممنوعیت‌فیفا پیروی نخواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXyzXSFLLh9SfcpT6OnEsKWLoMf4KNaZgs8EWmNFfyXSD5xlcQ1I3RMliTyBD_AWGmDO-a6hyERp-aT7i4_KErBqhKiC1FqrA45iji_SGI7Mnu8EMV_IjJWl_Deb7vxRR4r9QVj_yUjJY5xCjKfpnKchNaTqfHJu4Odn7tR5Nx_V2A-GJTAA91J2ZakGG4ukT-bePyHBhgep5RpjbCf-wzxBHGUDN2Hom2LMvqXOfBColtUBPfb4LTR6HhwP4m8ulap9xR5zT4chLsmdWkvNlM44FrddReGMvbzF246vEwYwAO4yMDnftrT2jwjeROg97pEuCURYIZI7_Ut1lfDpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKWcPK6UeeUUeAWm6WIVzVArEJsJMI6pbEfrYIjj02fv5s1qyWaiEftTF_0sGjckB0xAWvTcIjetk_GC2l7kJkk6JmM9gN1WSdyY_3Bx1rhZw-Lrdo73NBIOsHWbopLo6Vo9ca5XPWUTUoKb-8jPgLNbOP-v8ZGfzTuhqgYy7ekdXPGXpzt2bYAOOdXdBbiobHt0vd0S5YWFonQi4YWCS_mPNk7dvs70eCsmMxI9qieIRrLNe71bsOpVD-BaUi8Z2rrt6Q2lnSmnXE1sQh7q-xPVNUxK2Y3NIEt3nbLlOBg0s9Ru2tTrGyLFQvWkIYwQEsMPvLmNR4yfA72zhIDd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=Spyl_BaHjAvsf8bpPeSQxBFS9JWL0Sx9OFzwDFMJnW3RfBFfCMqsK46tiwtexnT4EALhSwDVI8u9gg3DeMup6jOMO925Ipt4wxmNLPqMxKfKBBlN1WC-kQVSMFRDKVyFjnbkducDQpk1Ks3DpLWW6mmjBEjRghXM6iYBjR5T9oLUOPBl6tpB0g8YEkr5RWpoNeNKce_kLtXTqpk5NIgYh-iMu1gR_QoBCPLySQ2o6O6_h6q5Up184xyEM4rFJ__05IFphb_vaNkP0JljzQuaYoZinb6da8FbT3fEhzF7zOHUEveL7CoS_Rxxd3zixCcJcExtxCq7a4wb-XyXViKTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=Spyl_BaHjAvsf8bpPeSQxBFS9JWL0Sx9OFzwDFMJnW3RfBFfCMqsK46tiwtexnT4EALhSwDVI8u9gg3DeMup6jOMO925Ipt4wxmNLPqMxKfKBBlN1WC-kQVSMFRDKVyFjnbkducDQpk1Ks3DpLWW6mmjBEjRghXM6iYBjR5T9oLUOPBl6tpB0g8YEkr5RWpoNeNKce_kLtXTqpk5NIgYh-iMu1gR_QoBCPLySQ2o6O6_h6q5Up184xyEM4rFJ__05IFphb_vaNkP0JljzQuaYoZinb6da8FbT3fEhzF7zOHUEveL7CoS_Rxxd3zixCcJcExtxCq7a4wb-XyXViKTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT3peM-1W2hi5-1aSCF9h11YHou68S3b3KS-DoguSwS3HPaMIyEfw7D10Kh8PJ3jZZJxCaF6KHgC0D8hCvTEP8JHhXPBERxj4j5r_qHWGFkX4JmjD9YVSJLb1LOzHLAGyuxzvACy_hb6dFswBdjvftpYjDhO4ZkcUELkcg5u2xdXL1CFX9RkfxpDsS6aFm5Qxrmo4okMhMdyBITEERvcAnlvLJvMEjF1jzQvbN-YdmLSrYmwzsjyWJSLkH1zh7XgFnbYJlO_gtvL9QvXlWONZYxyMGGRhYUmf2XN2XO8TVse2T97GKYlivD2IpV7u-zUgG4BAzh1EEWCEW4D7JX3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOlLB_FdfY_0biRmEOkhJ6BCoJwwExxARYfbFaQoxh0CrmXbDT8LUlH5a3RLtuiZGXVmzBe3wgZzGJWZHu1mg5AzaoO9YbLvaBxglA-xEkjNPfqo866-DwI9vQqXJH5CsOn5-BzQ3UXhLfN8ALypPln2RVJHgW7ARJEBtasW8IHVWgR6Yl4wrKPSgdDjqvyFME8yqh57pldnpVbdG411Xk2FUeDtGk0fazusAZFXuTNstW-jpS_3EZZDg0nvi1FXhlL5So9HxZu8JfidjzoK2PWw8ULVD7hsnlxuSXqI3QYJwa3Wkq-IiQP0801eMevz4zkEtF9mDYbwcTb0mSZW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxhj2zFewoguUOKO8M84xkUs9dbGerF6ITkEWS7nJtE_CLLSV8_PMSZOXM39eOJQuL2OG9rTc1uzkmUUL_FHaWVyaW--_HwWPBatfZQhCSMgUyfgpD5mjx5qEs9S5GBgvy0TO05kPvgFuieQryiY3Iyu53U1DqOduiklTKlNVV5CUGirzxQr5zhdpl2QiqIyC2ZqeEYc9IBU4gByXj4hDnk1Kc4bwICbrw5QTbWIGpVNHoLnJ6f6pCR57tMVwZqbvtyx_AXSjlEo_1izpF7NmYZbYcUE3lj6kJhgh8bM0ViSTNRP3fH-iA5bY7PPMxpsaw4xOpoRbGndGl3fRiL0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQG5aD6ByznKVPbRULvJVm0De31aazr7jn-mpOqi5kdIDpt0shR05Jxz6txf40kGxMTQxsbouU7xS9c8wKsCUMYOP97QGT1ZIT67R7HnoHpxqQgCO9MkapYZRern51WRf6u07Eao6mvRamNdY7ixH4Y0BYKuGhROuDfKBQd45c9ET1A6A46yZQaOG-O-c6LlfiZssqrMRJqBIOmoUgCSft4CN-UjCEdS0igODQiSkLbxWbCIlPmYIWcoiFXTeotuW_eFTwEBsnNihOOO-c-D9nhTRyLds1L0dYMk624GaFBYDZ5gWKYue_PdEXdNtlwc4aq5R7DByvuhV3KnBSRhHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QidJ5Ts0KNnMDIca2CkVUSLehtQ1RhiobW3km-8cJ8CItQ4X7n-Gt3wn5OGOgRlYHPNg6V0OHmXi8QXwYvAbtfSU5jq_zMaK2BgsdyBPeSI6rovNsQFgP471-UOKgIEqIGWFvBXxLwOcWSiBMFh29CNR3cO2zkrdpPiEbZSEJZQ2BkQovRFm4bqs7KMdij7JN-nH96gursUZVcFOk191_apRM_9QFU-UVvFWakho5Sq_fjeQPI-ZFm9CX80J-xrlemu91M87Yn1OtluVyvRfAub1jSygHQ0FGdbaHun_DLKC3_6prG6WyJ4YIZZ7CO8KXzj-_TuIgmU5LClSzbxnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lgKJqTdNC4tyrdyhv-qahCM44pXIi3jpGuvqJCbxhAsSGeGagDkQL28qHkDLndoqDDnWW8fpsXweET3PaNqRbe_YkCCBx8VzFvyDvKLRN6_gb97ky-KANkOZKNFtIpDvLUcx2E3fgoSFugJT-WU6MBMrtAUMTOgZW_loKMX1jQaS6r9n1mriw8b2RiShJk4cWmdZboLmZdfzJETqY-46N-7-xcHrfopull3aNuDW_MR9fJT-4NeYrfYKsFs6BcUNRhflXNWr9Bjd1ZsWuMnLZ9wVwNAL1HMZOimddHOTeldA6-65wYdl2cDeDJ2nTsv8QJfezw9Oq8He0-iaxjIHuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MelBet | جایی برای پیش‌بینی‌های هوشمندانه
درجام‌جهانی 2026 هوشمندانه قدم بردارید و روی پلتفرمی با اعتبار جهانی پیش‌بینی کنید!
🔥
امکان شارژ کارت به کارت و هات ووچر
اسپانسر رسمی جام جهانی
پشتیبانی از زبان فارسی و کامل‌ترین برنامه موبایل
قرعه‌کشی و آفرهای ویژه جام جهانی
✅
حرفه‌ای،مطمئن و درکلاس جهانی پیشبینی کنید!
📌
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌ Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23423" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWW-JB09P-7yAESSHmL0vID6Pc_On4Lfywlju6z8yboScAAn_LxdHvr9yD-8lRpYuSAtgnIBb_kq1C-qOINgXKs_Q4OjV5SH40wn2jgH2BOiGowq9MKMfGEPLIjayJ631RkJAyXXvHviMGulYlpADIE5UCUDBKhqcxTZc12_boTEbNA9blqrf0h5OdUBLQT7G0YRp6imki5OGOTJAkl4cl_rYz3uu-fQs_3IR9o6gBGsr3Txnt3v6_N57EI75gXTpWR-cWtlishwWtAxlavqKU6QUT9-eQFvAbonIWKPOx1deR43TxdvSaTYAFys8EMNzBhrIBRtQi861ZE8FkLRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJo_F4ZvivJCBfoVYPHhq9SC3ks0nd5GEtQKj5UT7JN_5uGhh8YZypHjV4BMMPyP_nIkZgSi7Y9mR2GSyssOqjycr8Xq2SXUrrgvDLQnRaMnFYqZihaz0HhpHnmcl9029GSIm2yRkNM18AZRkMywQEkWzhUp5GxdsaHZtHVq2jN1ljwfxCpUwQh-GkRZopOoAx4YYLLc1IMH4bY4nySDu1P8Sr0mOURbvK1SrMoACVwTjIin4ROJjYo649KDthlzp9I6zmZYgT4IllpmddNpGtx089tigiaHe4oLW0xnZhr0plSrSseglune8xpgEysLISy8_5Ncl0Fqi8InxsetCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDc5k4RLeTAtktVZysWlWRzB97S-09LwwRQChNzTMuMdi40z-LGue44vVCmFamp2uuHEm539llExn50F_2vM9J54DoGeF9BukFyPfAdHwq9GnCXKSDMLtjm-HJf0OO30680NJQ0HMX-7UxSVXgXNYBBgAi9O6B06M7auLoYipjDeeCKrKig0As0FHU_7HstBcK3GA1UbLgZt5HmYPPg49qx2y4hOqsJL8X1I1L9-VwpbJiCrNQqG1g93e66Vzt0OVy1T5xmV07dioIMI-dz90DndGPmd2-AVju3CvOepI1TeSoAXFA7GiB_poMoC5qvihI-nQXtt8f4RkvxWjlbU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Np_g05i5rO05ZUSnIW9_CBQdPhkmsQhkxOaO-th8Yums3TyJNYscw3bk3EESg6Fu9npa9339TAonpo8v26BDRHsDZOL5Ccy6w14wpM_XzmGMfSNDu0QcKKcxW56kavsUj34jGq9UHunBf-8rDxPVzdFyHlZmywF_PDfDUT4DiV8j0BFUQbot-GzePCBAE91ofxQzZL3ig4lLFJvDEDs1hDk1JKUwUSNazXmDmD9wPmsENtwAJspIm1kgOhPj405ZEehMrEMFszFFlkpautbSf56_hjv2QxoAUICfsJyPFhJhlCZP668QvMZilk_QeY1yv9_zaTnvlFnh2hW1ocmaNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNPhXGHK2t2CwU4gcWv6-7D4uCMFJ5GqRc0w36f1Z-ri1wak-NwkIWOGsn8vtNp6cmqlAWZikKsAQejolFlml-zwUSq_SEKfV5P-W-2ZYBA9yVfPVbJZbkfWvmnyNi_ZtrvHxw2moieib6QHx4M_1eNcVc6O7GYDxM4wipXoZDO4wYw30ilmlFC6mk8D6w7i4agMNR6gqNCEFGbGVgvj1H1hiaI9-D7myP3hF8_PKhAk5dsE7TF4trcUs38z-C_jPFz_4w18DeAtbJ9u3WO_b29XyM-x2rwHhOq6g-RvtiJ2aWCRvseUifEafxShKaBd0kLqyV7zhV38aVCRMaCG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=AzzjSC-PcHJEt_hRyxcY45YB5Mog0SwahDFePmpu2mdCWTeHhfFDXbi2ypEwJQ7_h8hXSJmiMYX5BoaJRF-gFTgtyI5ZzHmxd021231EFq1IZvGFxliGDgd22_sy9KoVUYoF3hfREOUGVMiM95C1dWmUUVVITv71oaJ00_K_7rT2bhlMMmbwzWdLNhRZJkdIM-GIooB9dY82sawA5Jn3UrgP5CIv66A6y3j1l9GohKV9zxow2Gaf9iiT18T5wQOmdZUbIAGuiuPrRhECYV9yzNefX7bPmISRLIOhDUI8L1YO06vkB_qjZCW88vYY7Hst7fj5gcS4p-g5p3xkdaSDlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=AzzjSC-PcHJEt_hRyxcY45YB5Mog0SwahDFePmpu2mdCWTeHhfFDXbi2ypEwJQ7_h8hXSJmiMYX5BoaJRF-gFTgtyI5ZzHmxd021231EFq1IZvGFxliGDgd22_sy9KoVUYoF3hfREOUGVMiM95C1dWmUUVVITv71oaJ00_K_7rT2bhlMMmbwzWdLNhRZJkdIM-GIooB9dY82sawA5Jn3UrgP5CIv66A6y3j1l9GohKV9zxow2Gaf9iiT18T5wQOmdZUbIAGuiuPrRhECYV9yzNefX7bPmISRLIOhDUI8L1YO06vkB_qjZCW88vYY7Hst7fj5gcS4p-g5p3xkdaSDlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برونا بیانکاردی پارتنر فعلی نیمار جونیور و کارولین لیما اکس میلیتائو در ورزشگاه بازی دیشب برزیل
🆚
مراکش درهفته‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym6-4L5bV_rCBUPm2149pxhCDToyXpcmRJt9d3BPyL19yplG5fGgMcLQUWhOdhmqTJkkGyNCjrB1tZCdI_a7XYF_21PKIC-y8Fiqx68ezlFob6j5aLnoF6GSA8sRXGcHovTS6R_tIrQqDcKVEvMYIJrWdoV4a7SKfupXVeloENAzGLCllFLmwWyNbMOeX6aAluPdw_4Apg0vMgHKefCpxMUcvPno4eZcvy3Mbgp0HVkWkKGFar9g5Ojhhp-01Fsqqiz_1k8SR6j6oAkajCQYriiOF0sUb4DkaDkX2mCqWQO4G2tPzTY8QcLdq0tAOiFTOyV9DIz_yXpOE5awvComMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=XnyxkeC-MoW6tEwT-9fMywf4rg2bN7Q3U2OVhvSqtm3lwWoBiACn4fmyK9TrlVH1_vIll3OjmJMKZ3ynRyAWqSuWCOcz45Jwg1tdeQ_Rr3SOixDOnTc9Y2CW9NnapbUWRuMxGJppv7eyJqQBcia0dtnd_LHn2WUXkLlYyzWEg5ioG-WY-uM1ynSBSU3F9I5SqJ03RppqTK1l8y0ahK2dlLI0WwENZ6CaeuLM-cYELu86nsyrnexCGwCZRgPwkWrwOlyje4U6aS9f0RjcXfoNZEU7PEenuU3z2Di1McOUrb_zoGXw8mBMi3Zx0k5MIjAHN-y4-6igujYOcecEQy_yVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=XnyxkeC-MoW6tEwT-9fMywf4rg2bN7Q3U2OVhvSqtm3lwWoBiACn4fmyK9TrlVH1_vIll3OjmJMKZ3ynRyAWqSuWCOcz45Jwg1tdeQ_Rr3SOixDOnTc9Y2CW9NnapbUWRuMxGJppv7eyJqQBcia0dtnd_LHn2WUXkLlYyzWEg5ioG-WY-uM1ynSBSU3F9I5SqJ03RppqTK1l8y0ahK2dlLI0WwENZ6CaeuLM-cYELu86nsyrnexCGwCZRgPwkWrwOlyje4U6aS9f0RjcXfoNZEU7PEenuU3z2Di1McOUrb_zoGXw8mBMi3Zx0k5MIjAHN-y4-6igujYOcecEQy_yVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxyyPlQhTTpB7p1iMeDoZN1IO3N-kUU67Kbdbnzp88DxDW8Km6iS4nqDkOaYJL5dw6rsXPRL0qN5UZTk2x_sLpxX2nbO55-fz7OzHy320OoyQgXaLJVG1wTuQDOjqc1WwXj5r-tva0idFAwi6uLNBPgjF0MOK2IbC2p12x3-vad_0okGSbPDl_J2IK7ZrI2jdxTuazyR5MhAubMtd7aeNmHmETsoO0T_gokw_CZHFRUL8_Hewj8pM9hjRWKgTfEX9rzESZkN058KLnhrNWkxmvjcC572kIChABgbZgkGwkG8yrdtwZSmDUZzUpxJiX1f6koQrvLdMmjlG6F02urk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=phd5Rwr2lEJZW6WUh0_bIyz-PAUM1UdJkb7O1JTFIb9NCOS-G8vf5jy4XMDZTRFhkpHQOgK2HKQJOnLu4JmUSPS_4ehjJ8CW5nPYF1fqB6J-rfBBi6v_lCJJYEQ9SGBCd4aufQWWriCBuKqa81HQsxZj0a5i5Ds-W0jbfPlXv7nxMYasCqT7rm1ydCnXaq3x5GkwMvtXKbeofKBRVN65MllTWOwrsb6Cv9f8vL_ohXkq5etuOQhBDIfYQE_EP7RtfwlDLX57djSl_-8ztI3_Z229tH1J4sWT6ioEGID44wiAHG--4fsmwIl2Fm2mFgrmyniuvFRQvfiaOtdsTShnMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=phd5Rwr2lEJZW6WUh0_bIyz-PAUM1UdJkb7O1JTFIb9NCOS-G8vf5jy4XMDZTRFhkpHQOgK2HKQJOnLu4JmUSPS_4ehjJ8CW5nPYF1fqB6J-rfBBi6v_lCJJYEQ9SGBCd4aufQWWriCBuKqa81HQsxZj0a5i5Ds-W0jbfPlXv7nxMYasCqT7rm1ydCnXaq3x5GkwMvtXKbeofKBRVN65MllTWOwrsb6Cv9f8vL_ohXkq5etuOQhBDIfYQE_EP7RtfwlDLX57djSl_-8ztI3_Z229tH1J4sWT6ioEGID44wiAHG--4fsmwIl2Fm2mFgrmyniuvFRQvfiaOtdsTShnMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCS7yh9mGJu26UlEa8XBTzFOZuyRMBuX18-tF4hT1DYtF3haCUqcJWaaKaWzq9yxCVkPq3Z_PwNHyAXr88VaB0ZMIiinzpK2hWDojUyP0UtQGJJHPX_M6hEpQGytNgdI-pChgrCG6sYmaYyit0qzIFaRJpqn0XYhNTcfCWaeCl_8C9_uebJ9KOL8cSy1Hqgd2dKtr28HymbZE1G7T0uCsRw55TO6G6Q7QN-CdGprtyZgsYUvklU3fSZ2PFp1d0u5blaBnV75n8KvYgjuAo_8VxJPn6RgNfsLqvoMgQ7cmekiHRHsnlj8FPLPwIvwFbaqJvRSm-KQkfR5LQEIeG1nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlEJExQPY8SEEAkLVeCZg1xHU0VfVw5DiyP4UO7CLY88izxMmi9n4s4gF3e1tB_gDQyF90Ho-sugYgUD_IM76cnM5xd8P203PdtslasP1xX-OX9hTB1p_qd3Zgu-LbIFly07BoHFryCvJeZ7ru1IwMUvAZIYRS-m7tNYK5Sv0jlxWwFcQ2_biiZbpFjqpgpIBjR_LiqKMdsCsRGt_o7SMhupcBbJIDbFn5KrJPezONZGwGxCdyW9tewOYY-2WGCmqT7v2FIFLQ1wovOreTZQWDusfyWKzS2yZveilJ4dCfWARpeotzUwv05wCkIV7EVEJsdKCE7cFuOyGg3j4i5ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=ll_jBPAMLiQYB2OSxGULe3MzechVh4HLVyR4BWse7qm1EUA6lWEey3XB99NQqesLtNDCHdkQvULnL5nTtZoKZZP6z0hVNr8PUiFa-LeojQC8UANizcXP0BGiFiPnSfWfkbiJd1UJHJ4M_dyIPVT97AEQnilmDPhKMadRMVTRKXJ_jcspzHR214A7zFU2WUQ7vVlz_NgojyyJNa6Vb7QEcMmsiN575ilgzspHIyIbvncgvT6H9fc2x821NoVtVmHkq7b81n2mQi5zK_uDfXSIv_72G-LrmTxU35j_8bEtCw2p0uQTzu_NsNHh5B9auBnxAYRReq7DLgggcL1cMlfB4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=ll_jBPAMLiQYB2OSxGULe3MzechVh4HLVyR4BWse7qm1EUA6lWEey3XB99NQqesLtNDCHdkQvULnL5nTtZoKZZP6z0hVNr8PUiFa-LeojQC8UANizcXP0BGiFiPnSfWfkbiJd1UJHJ4M_dyIPVT97AEQnilmDPhKMadRMVTRKXJ_jcspzHR214A7zFU2WUQ7vVlz_NgojyyJNa6Vb7QEcMmsiN575ilgzspHIyIbvncgvT6H9fc2x821NoVtVmHkq7b81n2mQi5zK_uDfXSIv_72G-LrmTxU35j_8bEtCw2p0uQTzu_NsNHh5B9auBnxAYRReq7DLgggcL1cMlfB4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAN7-mz-ZHNUhWPvizZBEJeYf1ieLq-atVzOfX4RHp2rPwTmIDSPPmbxSxDF3xlR9T68IcX79LEBXd2bOIOal8dYBLebitYUbEJHdxz_Vas89tgpd0Ck38OJTA6kjL2O51BrI6X6RSOnn-fe5G3IWRF10cRh3CmQKyDCRxKQFAaZMBBzcsVgcXlyeEAsUu7XzN1_ALojBTwNYQz73LCmNdVkYuFQ0wPQJxz1iKJmu-aH3LulgCYWxr3yPJPfpDAzhyjIi-YHkDYXUjmXwygSmRc0ZIsrzkiXtJ9_BMvXp__Z9I-gtfqt9n4rKH-lcXrTLmJeeDy-MPPG4qWcv58hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLfWNDOYzWu7ijCi6TyT2MIuNoGt5CkRMUVEfX_N0BfmOf4UiGnMk1WGwQ7vXy8uhmGtuVUD4aZQ3-OaA1OwcacrRaoIdwwy8VpGD2dXFue4mb4s_6QPgEZbFFvAqJ8AhgSagtWZORZz2Zr53hkfXZmcVX8PO_RJS_ye2-KSvp5jtNCgZsz86UaJgR-1GGA-Ub6IQ7yQ1qoHIqJQ1jsfd6YSrS5eIWuTP-pXfKysRuUC9vl12keVRGXL0OBOLrVBZvsMTrznW3PLw-MMznWZjvgARATnbLZoguQKfjpzcisTxdFprctISDQdir7JKyWdOcbKpivnn220jqY9XzaB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-IDtR9uvLoeKJmJl8ME1k22-uatKM_kI5aNHCnzR9OexYkDwgUIAbr5eNdhNP84faB2AkSHaitwm46J6IalWN9z8ajaISNYChPqjGdbJenNUY5h7QW5wqlp__VTyuBlUKWVaj6WBT10KDBP4toxLzSNUgw4UD_zj3WL9IYRCTqt0JiLfPVtY24UNv9HW4vGVwiUp8U-ph5NgECicYhTT01RZqWq8TdEUOACXd-LQJvOQ5yxoRzg51fLGfGr60aRSu7cHipkBLqDpBmZNwi6bosZ0qRqBfVH6mwCFS04Bes-6-YcOi4LIIClRXol8KOmjkmkoS8WovfkdGeXjtd9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=IiIPhDHuMIe1ih0ZBFEnYZOGX84ZAVMQ7fDlfiiduAVGnAyN9ERotuVrBmkUYQWIYmkrprzfFnz-sO79UnfAtaNJ0KynPAW4OF3zUNLXPO9T0sxO7vsSv5fdM3XiD2POkapOs8JoKss3Hzzr2M0Idvfp26rMvoOL9GAZ4C3Ejjs-iZqJ2arXkQFQiPpX9cYhPBsm2wi3nobbSc3zhYUUXwBzop_if6WW__HDKWJTG2fi-8ExvCSh0M8oeQwuHFGsablxWmGVm5vqcOtdBxvHqzZn_T2od6glRtQdrrVReNTHw02457NWubv4cNPgvL09iQ2Or0YUGEXbcrUXtFS_Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=IiIPhDHuMIe1ih0ZBFEnYZOGX84ZAVMQ7fDlfiiduAVGnAyN9ERotuVrBmkUYQWIYmkrprzfFnz-sO79UnfAtaNJ0KynPAW4OF3zUNLXPO9T0sxO7vsSv5fdM3XiD2POkapOs8JoKss3Hzzr2M0Idvfp26rMvoOL9GAZ4C3Ejjs-iZqJ2arXkQFQiPpX9cYhPBsm2wi3nobbSc3zhYUUXwBzop_if6WW__HDKWJTG2fi-8ExvCSh0M8oeQwuHFGsablxWmGVm5vqcOtdBxvHqzZn_T2od6glRtQdrrVReNTHw02457NWubv4cNPgvL09iQ2Or0YUGEXbcrUXtFS_Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhRbzqdlwEH7BL0UlFKRvzVta5x58ArqwY0KYLwKjY6G1u2WLEJGlLUPl896xDvnlbYfErs_whzhocpafYxNZYIXzOfG9EUOEHBuhqe9Aenvu08YKl3_z3jvWUF7Faovx7YLtDmh3Nte4jeBJ1ShdxkX_IWK33ljOvcRaQjS2ClMri8N7CUhzdIA4RLkvsAmkiCcuxSUj5-Z6NlUYt9mgiCx_DIMe2JL2XSul61xdmwm8c1f3JNLbpk2eqt_CCQLk1ieLRo6MkVLGAfAgAai4GXqgDuG_S3H-X3S5UxS1aif-fE-l-nhGiO_07hhMG4GIGc5Va6oNaAqrq0n3ErOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=K7VwNrsYJlcqvs3O21Vbnur4G4TSiMWuaSSi7RjjmzpYOd1v9vWqZjYSI8lMmpI9ro0f-hJXlHJUe6A80R51SAscOuPa7xtYaDvZ99j6kqVjUQnDGeKRQNIWBj2Q_L-iwOEiCuZILae4fmuL6wHTNeCKm29hKe9Ytm78qJ8FMuYe4sizB391NvFArPz7BdysZ5BnJ3QKwmLWhDohGl5dBQa2K5IMYaBfb-vMpMlgaXRmUGaDquX_3wxu_xbTreWz4bCFSTiCyo1ih7zbY3-caF7CgZxJOukd6Jab-ROlWgvM16sx6yTMfaL2rCQRcsuSIrD0RrAOmwOFDSkRxL6iVg-Ypw4KIRDH3iJ4XMt4DgUOniP78DDHK4nRZhjGKErL3jAaAR6yUByKdLkd7BwB0bjPYQpopX61JUzn9KpxkzC9yG-nyXIjzVEBSdcoY8xa9Kp_6QALhZv4eGY-_sIi3xbU49xiSFjLEX89FCod37_B6sPHi9PLY7R1yICVQOk7tKikHaD1uwShGv_kpVb8GohZwShnPNnNEmV5DWkw7hpS441jRydo8hgPIZwe4WjlCyhQUggonfFTJ8pOAWkioNVmEPRLU3V2Nv7Pq5TWfsdWqu-n56SMh_Jj6TUbm7Q52zooVkTk2USs9QEtD-gj6b1BfEIsR4Xzg-UMVOeAVgk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=K7VwNrsYJlcqvs3O21Vbnur4G4TSiMWuaSSi7RjjmzpYOd1v9vWqZjYSI8lMmpI9ro0f-hJXlHJUe6A80R51SAscOuPa7xtYaDvZ99j6kqVjUQnDGeKRQNIWBj2Q_L-iwOEiCuZILae4fmuL6wHTNeCKm29hKe9Ytm78qJ8FMuYe4sizB391NvFArPz7BdysZ5BnJ3QKwmLWhDohGl5dBQa2K5IMYaBfb-vMpMlgaXRmUGaDquX_3wxu_xbTreWz4bCFSTiCyo1ih7zbY3-caF7CgZxJOukd6Jab-ROlWgvM16sx6yTMfaL2rCQRcsuSIrD0RrAOmwOFDSkRxL6iVg-Ypw4KIRDH3iJ4XMt4DgUOniP78DDHK4nRZhjGKErL3jAaAR6yUByKdLkd7BwB0bjPYQpopX61JUzn9KpxkzC9yG-nyXIjzVEBSdcoY8xa9Kp_6QALhZv4eGY-_sIi3xbU49xiSFjLEX89FCod37_B6sPHi9PLY7R1yICVQOk7tKikHaD1uwShGv_kpVb8GohZwShnPNnNEmV5DWkw7hpS441jRydo8hgPIZwe4WjlCyhQUggonfFTJ8pOAWkioNVmEPRLU3V2Nv7Pq5TWfsdWqu-n56SMh_Jj6TUbm7Q52zooVkTk2USs9QEtD-gj6b1BfEIsR4Xzg-UMVOeAVgk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=Lpx6k4T6JvOKyazJWc_RMI0c-l-9muaIh7NC7EygVF4e37yZh4_fE3YP5KeoCpnuLvi-4KbPH1uM3aqg_mD4a2chTu1UZR2rqpL7DVz6DqMD_czg69672qdfaei1ASdVDc4LLuYxGrHThYUPLXCuxAoDkOdjU8orxG5fxtUbQFulVUxo8ysrVhYIr4zHafzkXtz3KBFfY6gieFzjafoEl5PApGxPzadD1TbE6ycEtOCYVsd4KeLuDvXKcbaFEVvRgfdUer_EGAhhyaeFkyqzmfSCuxusy4Q8_OJ_thMowRvpoYGpDt5R_02bXZurJFHc3eTC0o1qa5bhgRmn-DpyRjbBj_HOb20SrIxTtyqB4iTdxfe0NgZmvcFv7gMyPcV_bpt22D2Ffh8wqFvND0hXtuppez_L7MgrtNR1AynsM4e1Vllr_3MGTl_H_3hfTFu5hu2W10g1jYcNua8s2lw5Q8Xb00BFE27Me5uon-Kcvke-VVBroIfEVSKC9sVlOmPyYVqQEinR2yXw1d6Wmoeg6rcH03AGmaA4yMCN2pcakqrGA9cm5OyLqNlwlF2bz99Jt6zH6rteQUsL7sppQZh3bvtnh1Mu6nv1c6yapli4L5ly-zFARt2KYIPMx0XZ49yAq3YSDOg_JY4m8HiUOWnsx7VoTqeEuqOelk1JmSolaa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=Lpx6k4T6JvOKyazJWc_RMI0c-l-9muaIh7NC7EygVF4e37yZh4_fE3YP5KeoCpnuLvi-4KbPH1uM3aqg_mD4a2chTu1UZR2rqpL7DVz6DqMD_czg69672qdfaei1ASdVDc4LLuYxGrHThYUPLXCuxAoDkOdjU8orxG5fxtUbQFulVUxo8ysrVhYIr4zHafzkXtz3KBFfY6gieFzjafoEl5PApGxPzadD1TbE6ycEtOCYVsd4KeLuDvXKcbaFEVvRgfdUer_EGAhhyaeFkyqzmfSCuxusy4Q8_OJ_thMowRvpoYGpDt5R_02bXZurJFHc3eTC0o1qa5bhgRmn-DpyRjbBj_HOb20SrIxTtyqB4iTdxfe0NgZmvcFv7gMyPcV_bpt22D2Ffh8wqFvND0hXtuppez_L7MgrtNR1AynsM4e1Vllr_3MGTl_H_3hfTFu5hu2W10g1jYcNua8s2lw5Q8Xb00BFE27Me5uon-Kcvke-VVBroIfEVSKC9sVlOmPyYVqQEinR2yXw1d6Wmoeg6rcH03AGmaA4yMCN2pcakqrGA9cm5OyLqNlwlF2bz99Jt6zH6rteQUsL7sppQZh3bvtnh1Mu6nv1c6yapli4L5ly-zFARt2KYIPMx0XZ49yAq3YSDOg_JY4m8HiUOWnsx7VoTqeEuqOelk1JmSolaa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKI8pNQ20-5UtPYRMCQeuZOeWbbWY54uKnaMTh_ZtKpu4QieA5pwfUUqJsF1jtuVBSeuIPH3ROQTqtUkPUjfRM__H1hQnxAxD5Sr_F7jDnWsN2DoB0H5VUqfrjXgku0M341raPudVecY8nkPjEd0F8e0yd-23EEUjVbthVrDnx_HqOG7e5dSA1I6D0T_dskOMbzK7uCHyeENWDcWjDx5LTpmZm95u1hkHEFqh5ghfWH9A-sMR4rirvr9c2xY3QsqHfHcu8uIwd8xEOcdYvDDWDBv55YPVaIji6rUEZbWRCj2qXdI8EuLDrvpv4PmBenKkTWUMwcXsYqEFmlpZA1B_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP6W8x0E--5ihj07sPsHQ2v0Fk5z42rEeBMuDeoOzknjk3yP2QkWcobfHQsJI1rsTCrtnc5GkWoKh55dgDaVUDNQfyonufuUsLiE-yfXrmmw5qfT1eSk1cuwUkT7MHrpXpRRNUKpnkguz14fA_PStSPrgnY-5MxB-kUUy1Tu-XWIDz09XSCJbmx7NNFfizwZkIs_DalqHcMhvvURSEp0Rz7MvbJMINwiUfvuoL53A4I3WqPBHHdXFG6VDY8AEFCO2XL0qalRMg87f3cVXhm40Buc16jF_dRtrirbrbq_nXHPahRiiJDy0AxClLdDBdbhVeZTOSFXo-OFyNxANXvMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNRknz3P4OHHOICnA4vYJOjMFY9o4uPvz--H6LUBX-62dISRqZ1pjLI8B6epDsli52FpKiDGM8lE4MXSSdhnPJcGy0xZGh56q5DLJlACrndcu2_U4IGVb7M9oNAV2_TIlcsn89qLQaUnr_jtlR5jlbAKdP7nxBZTscR8k16JG2woyH1H-Fl1fbCOWXBgGMieDkoiAQwCE6BpT2hRu9ccc_NxHRj7HoMPctzCfHnnKdRxeCK9LYSsBa6bJDtmFo5wKrS0OM3dj6Xl7ARMXxfo4Tx2-ptr2W2aF5GM9a9fRTtzEhirJWv80X5iuBhKu1QfE7nq8TcJqzB52uoqASG7Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVWq_JiVzqO7voi2UJm87SNI-flTHvLw-TAqu4Uk3CeOVroAxOgq4fcwC3mxR5chPdg9fVgLLp2-SuKO_UEW8cpa1NeJpbs2Hf2JBgkA4wPLWfHoDxjTa9sjYnYT7KOtTfsAOVQrDZgC85NR0Ryr71XwaV5NKCf00Itltv5PAcZUnBte8d4kR7lWGCghF9u8cExen2MpxrjP9fsyuferh-J6Af8P8TWF3Cr6MhRIjSRJ8pGRta72A5ZzBK6rTNpboGMmfV4OhkcSefabCPDhp-020DA9LGd8lPm3inHdy0mv_MtV2HtkoyldOgCJ1JHSChGJ4LWEVM0TefQCNpSfeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=Qa0Fn3PTFpcQkAyNHaIptlo9XQpcbbtfm9V4Smb9pzvI5wUTxwe2-frqnXTErMCg7TqbPYxYYUPzAvMo9f_nSVkZ6qD9ZI3RbhYD9oRbMfGqma6RYHoCzRKVZ5Z011tDMGETA13hz_VIPQfaDbwgQMxb2pwe4w07_lmRRJdgosBOSkftEfSMnIbmZnX_ahdv6NRqAAJttIYSVcyTF2zUVAk7xajqV9aXXB_UnmIiNmPDNZQQGtCsrZXAa5HM2632_6Kjxt38-ugnNBp0mwxcNPLH2Jiprz6by5bkKGpfF8UwWsuk2G2SGjWa0EgUgrToOL7K2lgbyThTw9e0R9IorA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=Qa0Fn3PTFpcQkAyNHaIptlo9XQpcbbtfm9V4Smb9pzvI5wUTxwe2-frqnXTErMCg7TqbPYxYYUPzAvMo9f_nSVkZ6qD9ZI3RbhYD9oRbMfGqma6RYHoCzRKVZ5Z011tDMGETA13hz_VIPQfaDbwgQMxb2pwe4w07_lmRRJdgosBOSkftEfSMnIbmZnX_ahdv6NRqAAJttIYSVcyTF2zUVAk7xajqV9aXXB_UnmIiNmPDNZQQGtCsrZXAa5HM2632_6Kjxt38-ugnNBp0mwxcNPLH2Jiprz6by5bkKGpfF8UwWsuk2G2SGjWa0EgUgrToOL7K2lgbyThTw9e0R9IorA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBrPIMtmBM0i0LoM0Eeu68B5M-qRkJy4WmiBs7IBb8wv-VTrJnSCNReu8dF6SSI_1bCWNNF0kBZUAiE3Vx_R-7gEJvuJvdL8yfpPGg9cdN3GbTi7oLbY_dGHd1hIS8Egorflbw5GvFUWpdrM6eTBr2SgY2dcuoMbSXGCLsNzgk9aY_tv3w3wHWHWgXEP8J0ZgUinqTlX1MdAm7yQ2FDopIOIOelphn8XoS-n65tXUbD4FFY6ebm8AHhC0RCIYzpaFDRVhc11o3-HB5vopA3VEQurZntA8qL_BF3hP9mIMMCnUBPxI5BDCdLTmVshCt1zthCmoRgxzQ7EFKhPjO5PNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSf9tAkEXIj-ouRuiyVDXNjZwnPwvLajDUpV3IeuhpZozc2sMxcTxcOKKfQPkcnmVv25Gz5Er6HOK9jqE15hvIzF4OQpVNRyhqyQN2_oFzQkQoW1He3tkLG9Rf0wzJw5ff4MRjLeP_h-tecxjKnZpaSkRyNi8WJbW-z4NvHuW0XR0BBWsypiW5ycW8Nv1lVbtzaDktx0d7WpTpUe4iPuFh3zDa_f1ZkH1lbYiEFaPIN5wxizvHlF8TqUofeqJWA_sIcy4CGO9BG3kXv-A2PBa-nIa0mIXFmhzB9gmUHcHobl2kleKm_AgqPguaiKp806dQ3y1ewOuQKdNTVLXDLjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ7eCwfY46RPcbTTa3T7f3-RGr_dT-q42ku_QmCVtoNTk_7-4BQsE0ElTsRAmWhkbgMwh-VLpADwwXs3uCm64Wn3DbE7wcKrC6WOKZzT2tfYA4iSEYErTun2MZxkdN-Bq3Wu5rsBgn5IhWKED8UB-ONy70ggx9Aj47axuztJxvodBqTykPIhdd9DLdbMSYsEXh-LDD1DBiaqlgU0HlmX1zjvMt_wXTHBuQ6KlgzphVi5h0Imbq_V3rPTmYYcmiR2SFEmOkh-MVjv1RcLDkhOmJzLksnfWcna6Nij2wQT5gKdUb-acz7Wrz7kbzRzc4-axPt4J5f8_FPK1oyXIQC5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=Xtl4eCIPu5hekO9AyKq8DtGsndT2HVDCMdbW12wxPq7Olz3qhhTgSez3nBmcRedekk5RRAaeEw3UxV24IdPVTU28nv5ubfBPQ2lpRL2nTayIycK2elPzjAL9MqzVcGVW-MqLfvYfkNjFTTu_6tghKbvaqHPhM_dYMUraxG6UwxekXYhOzvzz33OQQXqHLFK_ZvEIw9V74RQS2YuC4StVogDeGvtP5T28npytPbu_mguu-e30do86pqVo9tFVBNMoNUmxmwgqd4Q9MkuM8iWATe1y-E0QcHWTUVP7YbIPoyFbWxbn9qigRzfzlHrENM4xdQz6YYxZV4UAOrHOq6s8tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=Xtl4eCIPu5hekO9AyKq8DtGsndT2HVDCMdbW12wxPq7Olz3qhhTgSez3nBmcRedekk5RRAaeEw3UxV24IdPVTU28nv5ubfBPQ2lpRL2nTayIycK2elPzjAL9MqzVcGVW-MqLfvYfkNjFTTu_6tghKbvaqHPhM_dYMUraxG6UwxekXYhOzvzz33OQQXqHLFK_ZvEIw9V74RQS2YuC4StVogDeGvtP5T28npytPbu_mguu-e30do86pqVo9tFVBNMoNUmxmwgqd4Q9MkuM8iWATe1y-E0QcHWTUVP7YbIPoyFbWxbn9qigRzfzlHrENM4xdQz6YYxZV4UAOrHOq6s8tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKaxkrb9vI_s2dK1OiVG6tyHcVvqgSaVNEfmIVXmLbHYKhGvzlSTEFOryOhmVY_qPQQxG4jGvGlBJnQXHI080Mdw5wrSwWAELQ_RqfpxGuo_fXDxDKFjmPa1v4cWkbzBkVG_ej8FvRsi2Ro84HfOkNwqVJvRspO5_yFZLhjemOtf5Oty5PnGhNqXl6Dz6KqpYLIRJQ-y_QqyfzQOGFHLKH7RFakw9tk_7JD1tA16CASf8yjtfHh4q5m_SC59ecmE3bZu7pJjlBHjqmEfAI4aCftCDC6hhQTad8KkqnYlLthfkvvF11DV9eZGmEd1oaL36NWEGWcDzPOTHPIN3dLUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=d-vuflkv8Bf4nYVfboBBYoBOQzqQMVcsXVnyv1iWZgZD_1Bb8_GhWKsny66kgnIYRwlYL5SUmYJGlKP1cbxVkHl8rROdsBuO6FDbQg4Qa9ooqCGRukG2llTGsPPlhOrnp-HH1VP3spkLcUkvbLO11-6ASE3Mr0hzRJAzcW1hvsk9XjGcGzuzpElVsc2XNmS-Vp6ObIOL50eXseMrIIezAmHmDKlsHioK_zi_HLiLQkBFtr8ePiem8wHVo_UL8UKPRQto_KWN8qaAr4WMofEZ7_B9mq1LgzgGl9SbnZ-tQEb9z8LRROg0O5eD0ipPCQJSsecVIea-XH7haz2M48Wj8oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=d-vuflkv8Bf4nYVfboBBYoBOQzqQMVcsXVnyv1iWZgZD_1Bb8_GhWKsny66kgnIYRwlYL5SUmYJGlKP1cbxVkHl8rROdsBuO6FDbQg4Qa9ooqCGRukG2llTGsPPlhOrnp-HH1VP3spkLcUkvbLO11-6ASE3Mr0hzRJAzcW1hvsk9XjGcGzuzpElVsc2XNmS-Vp6ObIOL50eXseMrIIezAmHmDKlsHioK_zi_HLiLQkBFtr8ePiem8wHVo_UL8UKPRQto_KWN8qaAr4WMofEZ7_B9mq1LgzgGl9SbnZ-tQEb9z8LRROg0O5eD0ipPCQJSsecVIea-XH7haz2M48Wj8oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odIuhCTBebHYhQasbzSy_ep886Z5MFR7zjXNdSAMK3hI-qUvo98sN7rfpnPSnDK7D3-miumUPV2sCVnYJthppYe5Hre8dF2FH34M67YBth1QnfFhNrbQiZrhl4Bq80qAiq13-ISiwNNPB6k0HrP-m6Kvt1bwpf7gduKHtTso4yomP-XVB2kBVxd9TGLjnnteRY4zdiAktRwuSkXmTAr9p8HuNkThxNJDzpwfdNpJ4hAKkTfH83RtuKSbZKnaGCKCOGlKeFrqc3jgwWgLIKFtAGbtfCRrGJTvVA94WT4dxNqdybdszyFFq-EGlE7yDio9-w4fEOL3TuRBKCh254BT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEb3RkX7GcdmXPs8I1cQob_vxIv0EWfZ7VhHguehC2MmZaOxxmbhLaKhv501ToV3mchUu9SVSEEd-y4G-uTmDID471uLMsEa2zHfD0G_UZaN7fY-B524DuNxGwOG5MIxAp22HjnCJWPN4Fr5Y3HSUVtzVtorqScpKCLAk6OG1AhtoIo3OBFZMgZPEY6GPGoyp8Yv6DmXm0D2hLrJM3AuCkblBIauU-ihBaPCDNFl3F9y7vD8SjE_wGFSWCG_z5jiDyhRD1-3AieoQYssNyOAjaMJgV-9tNJxjnIv4dSh4hlcgtSPZfU-lzqU_I8UC7iklyjfztsu6ZJ2hWZCBv2F0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBLXS87R0lSJ79yVaiNaGPUDz7DVBwzdxgK5IbrxrdyL1H-oVlFi-81EravWTqRmqCA6ZpUO6XXO9uDG1E9xQGaGv0__NLSjCQ31vywTq9FtxJ0mMM_3UsMLGu8CTLYKrfS1GKNvjRSTed0YLDVUpCqSF2QkfvXkUqYlKD2lx0lwKKmzSkfjlQ9S2bQDCsGD46Fc1pbkVXRuGf_PYS9LTuQRlgsuwt98yOMe_03hX6oz380ZLEvZFGXfIRRqgUsw_pYUqtyGvxVlHCbhOhoS7t3VbWrfmGn-C3eVeSfNP1DDWwx_SOa1iPaWb7u5L19aw_KU0y1IlNM0CSi74xRSIEr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBLXS87R0lSJ79yVaiNaGPUDz7DVBwzdxgK5IbrxrdyL1H-oVlFi-81EravWTqRmqCA6ZpUO6XXO9uDG1E9xQGaGv0__NLSjCQ31vywTq9FtxJ0mMM_3UsMLGu8CTLYKrfS1GKNvjRSTed0YLDVUpCqSF2QkfvXkUqYlKD2lx0lwKKmzSkfjlQ9S2bQDCsGD46Fc1pbkVXRuGf_PYS9LTuQRlgsuwt98yOMe_03hX6oz380ZLEvZFGXfIRRqgUsw_pYUqtyGvxVlHCbhOhoS7t3VbWrfmGn-C3eVeSfNP1DDWwx_SOa1iPaWb7u5L19aw_KU0y1IlNM0CSi74xRSIEr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bg3YkCYGbUDQjLtE522KMFP4FmzK1htkZ0M-d9ufGeRnhgO3XIvtVNhhetVHtGHp6vvMo1fi0pPsce_YtOy5cLHGhBprTJ0rh2blm4WoNCeuY2VVnaqmm_fVNDXPPj5SmaUfgUXJdniRzyJ82D-fEYzFNdmw5XRjaQuKKk_A0Q3L20dfKL1cd8fZ96WbSvz0ph2kTV8ef993plb-KGEcl42HoSSdj1k4c5cYO6T5440VIP5TaKvKFzYEWPrjuKAmveHt1gV2h6QXM3gR3tRbIFby_jfCxBjEnXp1OVB1WK-8dV9HZhOojc_jw5aRnS0oxCu7C-IFL0o2ldFwp57V5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKViAMCWWVJsDSSh57OWARY4lCoNht8qE7Dldn3OjiKhTL7n3cyPRcz30JIS1ZychzCorTTex0l0p2cFz9GsP6gc5u1e9RvEp6Kc6gQicFlfAgThEIGKLDx23tOMNCck-Jk_9nirj-laNakz6CIS12o72GaKE9FJJph-fgPTdx3W05Zr6LHot-tnLmUSlyc7i0yt-59-WhkIpymJWqr9t9iG_GW0C8BGMrOQRkay5_NJrTn6SvF4OPbLN-jevmpeYPey-pYwtgkNNCdfwcjX5xCjJS0G6dn48MqCXLDBJY6A2diylvvz1juASCFednl8m9vmJGGGZk_CbeyhhaMcvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=LZJa1dtS5ch5p8QNTKAQjnC1oP1JFDqGog5Srko7dkvzObemyx0-ztpwwP12zPh5B7lm8GLXJrxJTyhh8uCM_hu-E3AIz54E_ir99jfFdDlzrilW_OaFw3UPMc2fXO3BDRRra9L_oarsbkNnXg_T8HkEe5PDe8GczIVx1ccXILkKwU46qOn9zgIyezeAUysgkiWN_qdF8seevB4-0053oWffUHOOEOC6-v4UTS7_YnWLp1088l3wwRp1uKW16upUnE2owVSqAHnlCo_6UtuDUi7AUdo8n58EK1b8RNNb5FL93WXpogFFK2fYPrDTzydy82gyyboZDfK9hhxueWyUQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=LZJa1dtS5ch5p8QNTKAQjnC1oP1JFDqGog5Srko7dkvzObemyx0-ztpwwP12zPh5B7lm8GLXJrxJTyhh8uCM_hu-E3AIz54E_ir99jfFdDlzrilW_OaFw3UPMc2fXO3BDRRra9L_oarsbkNnXg_T8HkEe5PDe8GczIVx1ccXILkKwU46qOn9zgIyezeAUysgkiWN_qdF8seevB4-0053oWffUHOOEOC6-v4UTS7_YnWLp1088l3wwRp1uKW16upUnE2owVSqAHnlCo_6UtuDUi7AUdo8n58EK1b8RNNb5FL93WXpogFFK2fYPrDTzydy82gyyboZDfK9hhxueWyUQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=LNERkHcgSHCj79c1KLIMMo0xLX7Ys06V9E0YOBCcP-MwOpfhKWN9uZXBAs1viXurTGYk7RvA5dh6qddOtGf2UjW4RY-K3Extf95OFr8_pTYAk5BJra2Rm0ak0qHJAB1UYeSF_CM1ZfLSemCalvTm-NeIAEMuBmk5D19iLbdekneTaCKBGMXPc3sNshKI1IVnnjsKAjMztFNI4v5Hq4Puy3UA1DYu_tR9qoGxliPmafWQGnqDoMpXcyPB8ONMMit7ZNLPc-gE90jKfZq8ANs9JJNwErqvC2caGxyANiYy7F4E3nlMMpLbDuPOC2jn6zUCkZdc8Wtcn4iyWlJYHqjROw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=LNERkHcgSHCj79c1KLIMMo0xLX7Ys06V9E0YOBCcP-MwOpfhKWN9uZXBAs1viXurTGYk7RvA5dh6qddOtGf2UjW4RY-K3Extf95OFr8_pTYAk5BJra2Rm0ak0qHJAB1UYeSF_CM1ZfLSemCalvTm-NeIAEMuBmk5D19iLbdekneTaCKBGMXPc3sNshKI1IVnnjsKAjMztFNI4v5Hq4Puy3UA1DYu_tR9qoGxliPmafWQGnqDoMpXcyPB8ONMMit7ZNLPc-gE90jKfZq8ANs9JJNwErqvC2caGxyANiYy7F4E3nlMMpLbDuPOC2jn6zUCkZdc8Wtcn4iyWlJYHqjROw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=ehN6lv9cKqX06EHzlyoYZt7lmxaWriF3Z4VfvHk-b9ts9i__YgCJGhn48KR1_K9IKunn5_W9p3OrFgeh2hOIz_kl8aLzD-8g4yN0oyLG-gMhqIwdZ_1rSHxVJ561QBmxtmxzxwGxZrXlFb5EmoalrISFFX4XoeYhsRYrghQD9sGY4tM0U3YcqiqSbpEFZRPmtNeASP_GR-NmM3E2b5KwYopHW4PPEIeNwNWE2VRWVMeG05XCUCdc7SdpUwwoAkvFkOrh9kZuSUTbzPN5j7Dom2nnDTo3Ps9YxCY1u47yWYfCPi6tbCWFtLM68zzUdpXlORSCgdrkd1-FZVEuWKI8UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=ehN6lv9cKqX06EHzlyoYZt7lmxaWriF3Z4VfvHk-b9ts9i__YgCJGhn48KR1_K9IKunn5_W9p3OrFgeh2hOIz_kl8aLzD-8g4yN0oyLG-gMhqIwdZ_1rSHxVJ561QBmxtmxzxwGxZrXlFb5EmoalrISFFX4XoeYhsRYrghQD9sGY4tM0U3YcqiqSbpEFZRPmtNeASP_GR-NmM3E2b5KwYopHW4PPEIeNwNWE2VRWVMeG05XCUCdc7SdpUwwoAkvFkOrh9kZuSUTbzPN5j7Dom2nnDTo3Ps9YxCY1u47yWYfCPi6tbCWFtLM68zzUdpXlORSCgdrkd1-FZVEuWKI8UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=s1AWPhRKFn2OkLfF5DmYKA_-RIfXlhroP5Ij7e2RagpVuyWm_lQOF2vtj1pKu5nyAz_7nSdYPQN6UXwC0qN0LXZGHPaouOAAdhQvAc_L7rZVogTRAuiaM7xzxERXKhgSLODX_SqJRBrWRXo61wU7e0bDLABFhLSt8EKLi4qB0N4usystKeVnRZVti7lLWS24kvSy1LL3-DhxKrMJOI4mlpeVDwewSpJi-iH6FlCyGoF9c7At1A0-HUHPOMYlaDLD0bnvrqCTn3RyqNBkofIgLzL3Zm9_1hVbuTPvqv1Ln1He8yGoPbG8mMh-lAQ8pkHogM7hhsTLp5XqIIbUlFdnQ4QoU4v9izhJqpUCwFAh-nAqvIfwKrxUedu7nQ-Ns4M5biVkBGWYahrV4EpqrCNAom2Rmr5DbmMXw991stpNWDKm05Lxcpev48Qyo11xccT0ffHp5J-9mNBhcX9Y9UOOgj63cMAkVyRyoHCVuzlaXZ1UlgJrNLfybCdyzjykIZf-YNqEq2yYsGwaFdMgST2E9ElAWFGFO740juOg-V57VpvQXgqVcFvrWxq8N51Z4BokJxSeI1_X35AdKBdCKbc9KUdeJGkSoYUVYKda_JJLN8zYjYarqw9MM88uFCQEBSxYGVbADN13Tu5bz7-fnm8_Kx02YeYhwpEs-P_GibD7DjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=s1AWPhRKFn2OkLfF5DmYKA_-RIfXlhroP5Ij7e2RagpVuyWm_lQOF2vtj1pKu5nyAz_7nSdYPQN6UXwC0qN0LXZGHPaouOAAdhQvAc_L7rZVogTRAuiaM7xzxERXKhgSLODX_SqJRBrWRXo61wU7e0bDLABFhLSt8EKLi4qB0N4usystKeVnRZVti7lLWS24kvSy1LL3-DhxKrMJOI4mlpeVDwewSpJi-iH6FlCyGoF9c7At1A0-HUHPOMYlaDLD0bnvrqCTn3RyqNBkofIgLzL3Zm9_1hVbuTPvqv1Ln1He8yGoPbG8mMh-lAQ8pkHogM7hhsTLp5XqIIbUlFdnQ4QoU4v9izhJqpUCwFAh-nAqvIfwKrxUedu7nQ-Ns4M5biVkBGWYahrV4EpqrCNAom2Rmr5DbmMXw991stpNWDKm05Lxcpev48Qyo11xccT0ffHp5J-9mNBhcX9Y9UOOgj63cMAkVyRyoHCVuzlaXZ1UlgJrNLfybCdyzjykIZf-YNqEq2yYsGwaFdMgST2E9ElAWFGFO740juOg-V57VpvQXgqVcFvrWxq8N51Z4BokJxSeI1_X35AdKBdCKbc9KUdeJGkSoYUVYKda_JJLN8zYjYarqw9MM88uFCQEBSxYGVbADN13Tu5bz7-fnm8_Kx02YeYhwpEs-P_GibD7DjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j96Yowtej0p7lt9VS0JtV9FazwJVrenaM9FIiNWmOfP_mP9Xdg39QFKJNtMkCbBw5F89GeCHjt21jk4SYRfNB0e8Mp4E8lCMoz1GJ9gvtvEWpGtmW3mG_thhxMyHq0xlC_7aklejJaTWdOoh6oE-C9zSrKIpSFQWv61kp-Fx9EJo9WHP-u0fue2vh7Y_6PEdLj_FdtG9_T2NrPK0H7mYAtVNDdEPA8J--m7SWNz2PihdYQoytSshobHIePz0MLQXbqRjyt9ekB4q3g4fsO3vISEIV7VHhn9Paet01Ip6JedmwnmidryCgJOGPwmcma-GcuOSnuFFRQe26h1SYiGiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTRMNdq8HyR2M0ArdKrXOEc8hoBGhmAhlvZmU9qjwBtL1Ds51ZTp-qUZKxC3WCMV0xSKiWnI6qp5sI21P8fALiXnFAIXfSWGDc_y_uZC0UUB5Y0mEZBovHpJBIc5EiLro23GTa0w0JsOMMMFwP4PXHnP4bM89T2Og7COd21CsvaQYllvR-Fp8ndiA6UfP_SNawI-yrERVH9IqiwtRdXQYIYoY6Gd1iOhoHeWobBz2qICal2cIp7pbQHDiYXVBEN__9PVNEJkNlacYRgLIXGNryfHO8RvTgF08suGlcZcWmPYHtw6iLMjOXKAbjDLeLFTxBR0AwpCDqI8BVAerEJeyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxEbYBt9gPMulN-OtBVXoPAJ1zR0ZjXN0AwQ4dHuqVYB_jza5F31EJ6EiMXswettRKxXv79gcEKTO1OLL1P2KI_pQRf3bgsUWQkm0Fgq92lTLogGXwjnpzNcqD2H4oIMELyJRK7A-_Ge0iZ0YTBAqiUIyEwDVR4leXj02tsWYq0dRCdVT7jDlK55qvgBp8Ds9qzviRNLwHXCFJFjcS0DJs0h1mVeCmuydFsNcyleYGOX7KguQlQIazYqNPWfLq0hJ8QExtrh_uIHTaMsu9OEzdKo-BgRocGB0J-wQIR-VANsdFjWtAZcB4AXf3I4yddyLucEpUVMWpVeU7Erlo-yKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kH3mRhgRT0AZmwbZV7GJ8bKLC-Nfxa3L1CQ-8yLnHDMaSNZkUwiOJMtyEK6HdTw6_6qEMvEZcPHkLJNkNP2Q9IVr98MUKbgekk5x0B59o8Yyk9EPzkjFLdvAKLAXPqYqHEA_CTwL8hKm99r3siyCccTTFreIot7ceH6ST17Leas-EDNpyuoP5anu2jr6lZ_vS6_SUm-KAvKHFD2s9FkXNeMrJryYN5sqQSLPbE0rvZ-b1GMK__CwjmjY5n1_ZJQixHBFpUp_MjtQZjQyGjaDwEdNLg84hH04nTv5sJv-oCtrZ8OWT-txitVryZYT6U8RLTST0Z6UcAfvX6_HJJ7MVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOaXSnBS-6J1pkSiaX7t5R68Oi5dCdsO3kA6KnAHkpBZ49C-l8FJ6WJ99q1bTbsZE3FJfKbD95Nwy-qw2IuTfdr4enBHp7cPC_eTpPhJ_LSJC3QlBAYP7veae820-eFrNhKt1MBLQrSHGsNiEX3c4YRhXCGnU2LaWLdetbX319K9ENqWXLoIAwSa9_kJSNMb5GZa8YTO4xUTCXARTz5PkMgo8Md0CvW66kiumk5IO5X33J6AerAQWCb4p5G26FVbKC6g7lqlXHG0WVLmzlBKYtUe2cvM51S1UDNDnUvtIUjXu_aFFvu868Hd774FRB9zgSejjYL93gkAOVnRJCGcLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgaEHuhfMF2KkvezAdkkFGI5Zy1xnHGhLidYRnWa98vNuew78Xp6GTA3HIIDe44VesKAin5y8ZDsjW60quy0Nuy8JjPe7SFutsBHRV-7YEBR2pcsKimswA-WnnnMbdyL3S9uyJBDwYtuUzrgyM3HffL-VzcpvZj136b7FiS9YgRiVzPliisM7mFOIDoc2qFj1aNrKQTV6uAqDdlaZGo7IzkOrWuOcqvRHBPI63-4GdlVkIopZbcGw_xofl9BUkB6ESCn3eIFihNbd2x_4z8UjNjgvnNcmkEHKA1FIvkGkqUwjKSNaiXn5ktJVmNpn_mTjjxBxI1CdoeTYsBLCIBNuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1xg2vdYCW8YSaXuDV2Y6TwWlaam0ZESBCJ8ljfIgJ9FAmUtjyNdstmrEVB4uQWHIFTHrrC0nqvaN3xoZTIoE2A0dGXLWVG5EI-YGuYwTYglur_CnE13te-10_RVTd_Z08iFaEIvNdvlYyRu7pJ3yR68d30pICUzUBOxK1fRtVIrfySBn-fZm_UZ8LqSELcO_hjv1ONoCaZOkBTusQpjLCJPvWWFw911TycG81jBNsg8N_V9_h8k7xDoofAl2O3Wvq-sZsFJr5M8tjhf4yxXuGJyC09nnTsNYurKJw3fXIWJC8RGRpgncDDUrrVwqyxym5aF1mPg6-IWa9CJTO07RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=OrgeTe2pTTDB2rv0g0kW5s_LUqP11TzSlK_Fys9z46pbXn2oMN8ptdUEhWa0IVL99da61AwGVjxAlt9WgAxuFJQ4xbxBH67gG4YFbutEuGkB15HzGFbTNXIgkbcK9CQwe37VcvernjPRcoRDuT3Z1XhzXlaVXaD2CIMjWcMY3Bi-05wGKOM1klqLCvzAfN4KZeaqH7MlMKfbfUxGajX8Pw8HDHEqUZppxqMtdz6ctYqJ7yqZ-W3NmNGwBCReZShXXSLJReLnYnRbCAv0ke-wXT4KRdXIwY8oQMtHb_R8fAvz-smp_alNXV1q-C7v8nD_p0mrH56eqsnmjWMuyMBvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=OrgeTe2pTTDB2rv0g0kW5s_LUqP11TzSlK_Fys9z46pbXn2oMN8ptdUEhWa0IVL99da61AwGVjxAlt9WgAxuFJQ4xbxBH67gG4YFbutEuGkB15HzGFbTNXIgkbcK9CQwe37VcvernjPRcoRDuT3Z1XhzXlaVXaD2CIMjWcMY3Bi-05wGKOM1klqLCvzAfN4KZeaqH7MlMKfbfUxGajX8Pw8HDHEqUZppxqMtdz6ctYqJ7yqZ-W3NmNGwBCReZShXXSLJReLnYnRbCAv0ke-wXT4KRdXIwY8oQMtHb_R8fAvz-smp_alNXV1q-C7v8nD_p0mrH56eqsnmjWMuyMBvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDiX9GKtBgwVVOwUyg82yLzSnqCJULsCLWRf_aAsN9K04Q8YzFZv2r8cLQP81dQO-8CNDCgIRv8E7f8uFgcFHhJXdBY_47DBg9DgOvTq0zQJiIvhq8BDam_4qbAJVya9DJZpWBU9Lfxf_PIRLchETcHFYtZ6Klpbtkfgcya_6bv1dqiaExy99vrXOQLNHmGVDdSA6ZpbeaN1wMoAyqJbGLDHc4yqZJO18Uc3kZ4Satadb0a-2RLSMZ_f5zTZkgnhv_K_5T4l-h1NBiqqBhg5hUtTFzsWeHjHmf20Ujx78VMaC-Tf_G6sQw67j0oPHgcDEE6mPZTnKiVusMJMJ1UwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkaS4SlrcfGTYVLKW9Xxb-Z2bxqDxmlh0OSUa_s8uLpebSn47kTtGWyWEGfCEdbv0r0icU-QWaYUlLqmyRS0j-OSTL_6hnzG3w4xQc4ePSJARJEaAzcswFWbZ9I99_fhHR0ltt5QYzuXLG5N3KKzVqQXTnqOFw0gp6318-jxfpsF89G_zlUVuUrwALNEdoYLV5QCtLFl_GUjTPDLaZM3XOirClhpuusNGHjeZfy1uYpaVuuu8SfwnrPvZKzOUkZvbmnUsvmmkKi1EyyrjUt7mD1Kf4THQGwbB-bIpTo_eCMaEKdht7m3BzNbkwzcq6MlnU2QykPj-MZSVEFLlKXcrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG3Qx_Vy7efegsl9lYf4lxNfq73iRT5UUoMWS1PjATM7Y3FYMZB9McTPk33N5pbkhjDj4ZLJpO7tqfjOThhVJYFe7QH53RxA7mQEMNl-RO3E7EjHfHEyu_r80hp9EN3S7cCQOpBSCcfhNDwod5KglSOISCMTAlZjYHN0Cgq6HwzHm9q2-b01PG_6W1EXwbIjADroUXGrNu9xQtISwap_oarSOifC-LgSKOKXxDbMzLZowZXhhX4T6AwbcOyamNBovPeGjrimJXG00m9y8AKAZ6BQuRwv7Nuy5k_LaOxRSsWDNjNNcyTDN2EILWm4XbqkqmskUQvd9I4nrEy_rwyyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9OHJxb2vk9yud-lAcWstpB8BzjTaBLL5M2k-T8-3VPJxZydT30mpyQbnqRNd7hHPZWfoJblXHtfQCsPoa7orC4PEUer7BhhsAnd5WdHb_Bh9PlQN3RxCx1vuffsNyDGXIRn_Aoqv-GeQLBOfS6q8tttERp0MFQ10r74Suthx-kCLen6SjSCGUmNMV4eXi61nRNL84wpO8lPxkj1BWewggOs_MCxbmKXBuamXIsCq6wfbTBqOr8zgCFMm47QEA23dEsPLwMYqMsjEXDlRKd7JMzwnS-59kW_D1LKbx4-woU0G9274sjLoU_1uIcXm4nr4EqYaExEND1gYA8-_Vt5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AOXgrW0ntJAhxFzggQ93RrZe4R8A6G4aiYsuM9VSEjCUaJX62vq5L9bMGkvH6QxptOLwi_eFSec8VnmCSpA0k3Ft9Y-hRkGQYjEJdfdK2PAOW8kt4ACYRi7wiIlePBVwoBGilRbvUNfPYB5oEGwAefxE9y6QEx6v6HY-3EQTLopFW1yc_lvNyoOSP-5Ksg6V1GjEqGuBq6jOwpi18tEwVcw9ujNaihVoJFXs78qHYbjktcf33imXB6tmIgdR0aZHY7LfNZrewxWQB8BS5wM4UgsTtUBNZrkptCY2E-d_JnCx6BG4kW7AstUFTT1jTcw0iIkCu-nSlrsCOmHDtylyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R88MxvD-53-XuWGUWnCJM0bU-HROjv0soYRLmqZisZG9BmzBOqMulV1NwzFS7OKtZUMWjgwWdHjbZeQk9DsuOfA0hpQJ_W0uvEhOWNZAV92UF3cToX7Ktl3SSxAr2_KuoPu_UdzUPEjTeho9XQ5HlZ1zb1WnDpQkjgFY1VCU38790n6gcXp9en8p30ay-21yYetFZX_qyDwKF1CW5CxVfZcH52GpI8UDNeI87NefIuQkTg9-oyJDDV43Xn137fIe8z0Er0wzdXrvwGw20ohRRz-Jw8XXoSwojzFnQuQvhjLLviGzI96qtuoc-7EzMOMQjVvuLz8UV9L-XGV_f4GSxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b02wh8D0L3e9WI44yPHlE3THBzysHujZrq8NiFfooxY7L8VXJaigpoEpzXsfQRbk70r7RqugBkIcC0_tnwwDqY_hRGlqEmYrHIxsX7ltEuX5qSH-G7hizqkPkxji8c0G6OgTmN7SWB6zbeZsYP3Hg158ix8dku_GYIgX50Mk4AKYXLkgfNsPkExnOQxGwvrPWA4qe39opzBtZPw3ssu4xeW_PG9yj8rCOYuxfWso1RyUL9EFLvgZJ5Oj2dVy5670PED2jNjAh2xj6Fq8eDtFwHLFkoiLbnauLdLpA71Gbu0F_qiZtlFfEo4k59GrSk473R2la2GwiLM9tguoo2zDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zwts3Uzd_hs-sRjjaUL8OsdO4tUJ30H0DxIvf98lhrgi73cQZIPoaf-Hx_BY_ZFD-VwINOjsAnw6e-o2-FBHG84j4Ptz3Ytnt7GuL0V3V6WS6edH-pNv-0RbOFHAkBR3k0-fIAqdOreC_BfJysBHvQmKgmI2QnhtLxoL1H5BvPnwiheJR3cg5GnLZ73AqZVyL995s6cyCG8Pq2OGkJXdviHwZFiqWOPcNW5LPXOjPgrwByJjAMKi8xYd3RbiwC1fCoqyS5NAakrWD7QZmNU_4t3tO06sDAh0MpBvlR6EzzFHofyRYtGs413Yb2Ngcy5R3wZcAN2okjp_n6ATfKVfnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6Yltf5uiSrFmobz5IGwAwl0dDaYO7njTGWAN5gvDi04wAAeHBWg00_taksI3-Z7CWX0r7p3PVyVFpSzMb9ILe7e3Tl_kBK9o_HROW1z3PTOTkF42LAYx_Z0kz2EBA02sYncR1t-7G_RNxTjXTg9CkT85ZAiCwKEMLf5l4BN54FUm2vAmb0Y4-6qBOjj3V7ATUKadDQQyR16UZgcRZBiqiWQ6VMQbXGWpIaQJPVPOEH1BlwHHlFd3KLqOErqtOqL4TZivricSrncVdIMy4NfzxMP-AMXCEJwKY92J-Y59Z8owriuY1Ahwoc-VzdBMrjHoBRHfNMTdDxWS0ilOZcrJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnU6OlbJ_1e-x2HWTrbxwIoPOnqp8F_uL1T6r5sUYdBm3KxM99qOBMyAQW4JBMJpFwl_L7mMbSVR3tATtH1dVJ2Xu_hthOE460QdrkM3ZKNgR9FsVmasizN_Bzc9vXYTd4M0XwYdOfHC0qxjlxKP5-WJ0Pwl2zYdEIrVEJgVlK5Y4IJCC4LUACxLM_IafeovazSa-SpSgvpR7V-Nb4vUbc8zM3GiN39DLRB1_Q1ovKlX7lQbOhEtt0ahTgqJiAW7uKFiyaqfwgQAkx9h8jSPmcIe5ITWwO_8i5Gn4WTxLWg8ttkkCf3dO4wsJlvQIwDo5Pzq36KJAoVW_u7jOJ9G-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvcqlbaVOByj2Mca3PGxinB-JkkA_5LqQ6MpqHXBBCWPSuoFzrU4FDo6xMhvBNtEatXvZdKYKKy_JfSo64sYxB-Qoj6NM2KFTHwvsJjo-NpMqQmpbRc_x32PyqJrXKMK5D5ssxLUb4ILZ_eHPJDweflCiiGAnF9LVfklHSF9c6vfObBNosg6BnUIiMxX7q-7CeREHybMhJHG6km1cobxpwN2uNRxa3Et0jumcIrNhDu73ZPx6nFEl8R4wVR9wBcKsxBCc7btVoqBel7qy3tdeapLGxdoQ5LfTS_0JeyPLZNo7Hao3nhv0VX64l6HHhyer2DarJEwSY4tWl2x76clCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYAQMWZejWQYRA1sWMhc3To5Lm6Y-_lFSeexoa05QV0p7LyHfq1HlIsWrPZ9l12SSUZ5U8lt138A-cwxjqHjN-CMNp868f1LhtAPUojmASWJWqdYopQWfAFiLre4vsqi7WG6a0-Fksp_wfL0GQ0Mzb9giwaz3kQhNByyil4qx9OKr0ZpBvDg8cg8U--Se49ey6rfuz_SM-sCcpJtSgPZpxckmXMpNbbvL44QrPP7RbWuimcSJvXPSWi1L7e7MvNjUs39a-FCj4-rNFA5SwsZto0HRztQZ9qK7naZeM4CKC1rIestLglY28OwMl30X1f21ZfBUJY1uPLP2WrNsoXklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8uU4VFhTrTLB9LLft7JgLGt7Hqz8M6yjyQEaipgggy8n3xBPmcTOJ-xP17tIy9Ar9CV_8y91DOwoeSCxwdoSMxHxDxOikcUFOVTWZqWgF2-7IsZtg0nKNCaOXXAs-nF-6Ap4pCNL_jTIQjuo2iqtCXLpkSBjfsK_MkZvlUn7Mj9V_lunIaVdM28SOAeKUr2xAGsxtbaWdqcC-sCYzuODlW2eMOi9LJ2snMlrtVHNaHcAyWAfw8SO-YL-CxQw0v08oMJOE_S4ih6lHBQVUk8m8qxvw5VwEZmhaS1KieC3IaVVHqfcgh2fkaXC2oyNsG41uyPHbigT1-nDmuV_j7izw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2SClgLk2JIIiIVEkxrhiFCkRKqb3zWG8wjjyFBs6k-Kd6esYecBQjv44GimDacdvA3oNnw9WWqlHpguxijOHCbT0kYs-A_cmaWyWyqgsa7IxhwLsmanMJ14P7Y8HK93BsR6WVHzF_0W0l9KHHp7BuuSjyvaI9wxzdbRwAXtcckkPjrDzrrnHgWY-ruRYhPyzFxOxDCvJK_N4OTApRdwuC5x5lbdAyfEBWzbwyBxQU6Cm8RBoXhuGFVitnc2R2HoyNwjTppjMCN_-GgWlaiSE7cSBi5cApIWueMGnsnTj4uRJP1SzhYoXt1TCqYeJD9YDNjX-6ZCr9L_zO6KDCAepg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
گزارشگر اختصاصی بازی‌های تیم ملی مصر در رقابت های‌جام‌جهانی 2026 ایشون هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23350" target="_blank">📅 14:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRGo3RUu49TyeRBFRI8VbhFZMIZ1FW8MKpIjUYukJVTMU-eq8l6zZbydiv9qA_Cb1kf-JUyaznduf7Xx9und7NsE-fxNMYQL6Ao5C55hQO3oPIesxHHWSSfyVxypSxxWdCozo2n_IR7HlNv0607yXaNBjo6D791tvCmLrU9R9pSfzFbMTh8XNw4SEOHhTO9P1-H_5sxDS9GIsjI7zhGqtoA-qYyHZsPSb1NX0cw-nodUVtHRG7T2EXr8OVH_oqpRTAG6m3tiqhBzX_1RRwCywpJD2qtH0zHgEVBbJsMj29jyuBtYPpE9Kf7U6DUTqY3qkh77gy9N_sqsv_4CazJZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23349" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=Ui7HlFGfTZnnIsdpxGXRjsTV90RPV6mQCz-A68ybv8rH51a7YKPoV4jm-B76skzkXeo38KC9gKOT56ACKvgKUYIBxORlbfZH9kBYdxOKq7Ir_7fZbvFuUjTMzuWCzyZNq3diqV3Wlu9ikUzU32KOUVWKdE-Nx3ClZn9YIThleVOayW1QruAz4savNkrQb-NGoh9dpvzc7TQj2GEoP41_ov16oaV0_7IfbWLS-MAxlE2dyqO1Ufg1kjcbwhs03oq1q4_C8yl81m0SoMpoSBdUd3QTWrjqWE2ip0Yy5ShNay3S891qjqS5A16A59UWEQ9UEGYfWjtisAOBePMQIKrKHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=Ui7HlFGfTZnnIsdpxGXRjsTV90RPV6mQCz-A68ybv8rH51a7YKPoV4jm-B76skzkXeo38KC9gKOT56ACKvgKUYIBxORlbfZH9kBYdxOKq7Ir_7fZbvFuUjTMzuWCzyZNq3diqV3Wlu9ikUzU32KOUVWKdE-Nx3ClZn9YIThleVOayW1QruAz4savNkrQb-NGoh9dpvzc7TQj2GEoP41_ov16oaV0_7IfbWLS-MAxlE2dyqO1Ufg1kjcbwhs03oq1q4_C8yl81m0SoMpoSBdUd3QTWrjqWE2ip0Yy5ShNay3S891qjqS5A16A59UWEQ9UEGYfWjtisAOBePMQIKrKHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
اسپید یوتیوبر معروف در حاشیه بازی بامداد امروز آمریکا میگه‌ رونالدووپرتغال قهرمان‌جام جهانی میشن؛ زلاتان هم این‌مدلی بدون هیچ‌حرفی بلافاصله میکروفون رو از دستش‌میگیره‌ومیگه برو بیرون بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23348" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzy0bTdPx6T5GqyelS7yOFssAHDXF2PYyXNjUuIYscddsXr9t3aKsMANR6IL5g6ujjzXXUPRNMMpG3CAjLgqgSdT2rZmMfSt4szSvl5ydtUKjh9FrJoB9zQdk-nn1jYABMpX9JVi5d5P3IyM6mRE_y2mG8-r0xRA8sCZUKh3UWdc7s64GRXEa5Va83yf7jSdXSF0S5SxZKTEdgBGGMRLLkibrDXXndk7uJOfPC0k2HlCc--QJgCFxQNJ-rR6YcOJ7ma2V1kxDHyjqDMfVWOCYEChnkprvp-1lbrPmQqkTXUewz7AzfEloCVahHv7hev0FQk7S0Y-Aa-0LpLCAWVtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23347" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiqJHlnEZwJhiVXKTiNleArJjn22huW_BNQlNyPdHbxqtDvOj1SKwMb90d_u_PA7tnH_FC6UUlQEECurvrCmYjEudkr6El3T5zC0f6pP3cgDkoULNYeH2xKN80VTEZhd3whsJ7uhvrBxlFOgOAtu41oh0janwX6ra66y3zIqxsJtucEfn7qoil3M1qD1pktFvg6UHhMltFPcxXCB-ah5ytTXx0JKj4KcjSdWMqevGnk7sF0480Z4Q5UWEgIuel4-btiSbNFSiAjF5he7Lzj_DH46d1uUDqGaLMXdj1QSfHoRVGS0NW6OwBppPyEXSBjPM7ygraj1W26-dKgW8BNcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5Krv-lbsUR95wMni0pptHsQp1DkgOQ67nVhnoKOkWe-A78An7-hhbTS2AlRKGO34HOn6gnB6wKIUpWb2ROPG_LEbS8vAk5k8ZYTGgMIeELmKDOGZXiyYOFHmIGHeeSxwUIm5csqod0C9qtSack48r6jiZ0ypf2sVv3ID1xn-BZBogzYhO5nhjkCGIidxqmrt37OApQjAXJYGgq8Ofks_dAq-P0HfVPJtpcged0qDhZPgoOnVHsxv0Ygee4Yyu_ZzKXECESVwVnWEl9_UZtQShNSy6gToBMhHnbavuxPDoMBZbQMAkg491DG0aqXu5QAxRFD__SRHZIHkOCZqUeDRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرنگار معروف باشگاه شاختار: بازی دیشب بارسا و پاری‌سن ژرمن فوق العاده بود. انریکه یکی از بهترین سرمربیان حال حاضر دنیاست. همچنان معتقدم که باشگاه‌رئال‌مادرید قهرمان این فصل لیگ قهرمانان اروپا خواهد شد...!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23345" target="_blank">📅 13:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23343">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzoROXQIIwEssJLg1cKMUq05mKWTjy7HSNOUq3izb8X_kyHB7pmNmh0Ut4_N7hitEpKufxR7IxdjQPto7khkFpV91ibzIiYOd6SIy0vtWENGZflqyK6YReP8d5IZEjgJsUQERcodkplNZ7o7TWu7QAahWiRy0E8CuZq4E-54Sqx-olSXjOmOUIa7h3y-BpeLw0qbWo4D0fdqBArklWwMocLMIXiBuaGPQ5SfTA8ja4ML1kj8JdW9Q6x7Qbd2c53kxocI3cCBXosRDr4L-vGyXOrGe3o3WtdG1ESYC4ciS_0-HAh6lqUtDwCl6GZIu2uW-zEX4iByA2FhHt0xsJPFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23343" target="_blank">📅 12:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23342">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDrEYEszUcw1pnFOaGae436QIWFpE7CWwVHo7URRoMx9tAiHsUsVhynq19QApHNy_DFOSB-zW-gC9TPggqiSK3LCBVgMP8totvjP7LOIyxLv7fBXDJiZOWTbzMdeAgk8PRfM5iKYdywaUpPqdTxHgKzJHu0jKOp3MRq3M9SyGwby3erHRLpm1YoW9OYSNrv9TsJ5sK2BIqwgqnuMfBKNmOprFSJmrnEpp6Y4Wrlyo_Rch_JHC126ziXuAl9SgzykznrUZ3CHc7iri51Y8VBmrJDZcZSbYmLAukvQ9obxUBPv_zjQUxh-q_IbMB80I5ehgoCULpuMWQ_XnGAB4LVETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیف‌وتجهیزات تمرینی تیم ملی انگلیس در حین انتقال از فلوریدا به کانزاس سیتی دزدیده شد. بنظر میرسه که هری کین یکی از قربانیان این اتفاقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23342" target="_blank">📅 12:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI7kaBgx9Q6oOL12scmd1NgnAaDhGDAzTkQBCkLOqpE3b5fCSqo6diddk-dvN6v-OhX_ADwq2bo84l9_VMzry_O-JTnaK2r2a8zsZJUDfV3yX8ec7aFPhoL7NfmWFRkDCAXcmeB4Je57Kv50xK0nom4Qn-9XxB9VsRlyjAsKgZqdPBg9cZKF-fjo4H2Q_WXhCdtcIHKSIIG9HfEzBJIBbyt7m9P8SijmIU8v-pS5YSNWZL7tI7Lxtn7frLDBzyDfGiivpZcgoMp8XsEudmiDiVT8WopySarwY3I93JElIxaJfxGNwL10XRL22th96j5AFV46M3ozE-erBDUyNQt2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23341" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVyMJuZqaf95QQL_9cpXpMtQtxQRY91S4e4ETBp1jYICs75zQHiNld5Eg5J8TdwTxHt0LVlY2IB_48XT97EzdVDdZCocwmHAlW-QK2GJBnjqijHaHLnTPBjnQOT4jDlM3TXa4ypp8RNTl7FaMRc6ROoRH8HUS8gUlLv9Xlz4fKTLIXc4ciNou46P4m1RHH3egnLLe98uLe1Crvfn5miuMQ8Q3Bi76_i-Sfpk0d6nYvpegB96KzMUVp7T7lx5EGhZYxJdSxcJ2aOdddHBNOeJiLECy5FsoYf5lYhivXDqi2U3lDCZ1BAugUU3RuoEVjIVFXFcPyz9h7FqrRj-8f3Xqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23340" target="_blank">📅 11:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23339">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jciEGXTnO4OKfW5hlUBb5e8iLEKgNMRy5-0TDmbqvIolDdytRdFVwZBvxVx7_V-T6RuUEnQm0E3ljuEbLM4RnMeGYLYpqFVQjOELkEScjv6uU5s9spRy167a39aqMYXHDQM5eefQ-xzydwCocr8RFeeFawkSVlymjAy6JmRx02jGD0NYre1UqMrhJ3FP7d3b6kb6udrS5qIb6tHHKlgC67-k-SqKtUr5PH_T4--ZXkIt00OcqCLAN6ca5Xtg5mDTkKfYJvOS9isALBZT5pvnCvAnWKcsyJ_uKmz48xlGvqK92S7r1ajtJz7pSvC3DWYcpzXPvgG-BsC85mGJPYQubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 صفحه برتر در اینستاگرام با بیشترین تعداد فالور؛ کریس رونالدو بعد از اینستا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23339" target="_blank">📅 11:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOTD6-9lyI-PfRrk2LrBNI9NempCv8Dshf-XNiD5r4C4IfSPcHS01p5dJU1aRjUNjE4KjkP-74tWvBzdCzKkPOoETZLjAeCBbYvOJcn_6fwHDGhZXRNEtKaVr10iUO-StVGmBt-20Pc0-aJkontxGvIyba7RMhig-TLmgMKOCTYx9MaY9Mwh1w_OcRRg0_nfLeHbircqeAiQU0D10ZcaK27DmHayFb09PMgUEGGYQAGbMgJjufWpCs1XNTDcQ5jD2Z8pURinaCHu5dHjTalGXlVnYP6fIJlZLj9XAhTPDedI00Qmyd8aWk0MLvBJcP3wCzk7-PmmhewbxyG41LeP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23338" target="_blank">📅 10:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnIylSSF1AqutDCPLlQ5FXOC-nxCR2ORoU7b7clPMRM6Jq4uL0XW-SoEk37oiD6wlTudxQZ5E2ZrtX_irrviTi9Jqlm5No4KtKHHxtNWhmlIm6ZXD928tfvZotuGf6evukAkix39W0eyXsh2ECa563nNZwc15VMCF6QW2rGU4YKWQISiW6o79RKrOaaDvDyjc3wzjfCKKEGkbtmBfzdK_A6JmhTOVMftJSdCZNdhNItacAPJsK-XSbhcUMevjaX9Io3BktoUSHMvCXMCjfJZHHInX1VDHwHNB4P2zSvj7aUAWM3WJv4BKkWqRFZuP6OVoTt3D3M8vsbXu1q7ov-6cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23337" target="_blank">📅 10:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29987e4127.mp4?token=IVQimFD7eYiwDZJz5hrAmynXbaxK9nCIVg_dUV_laBtJ-PivkQIfrXtTlpyETc8HXfJlulllvV3AerRznZUfkmFBxVcPVnt4UisEcb7-yZ6uZrL4Q5PRrCLVtMwJBfhLy1QQzVgi6i6pkOTvSWVMql-7KBH7CxWisFimpHQOXNzMkhNw8WWercxfWoBQnJFT_MtmNzSh8fBDVE0YFIbmhw47XsH6TygazVYZKHVbHZi6g3MI-nfRlPTl_5I-LP075sxa1XHP9NIxnDVRn4z-AgCZCHa3cHPGKyhfg8swfZtnvks7hS_N5Rq-CDDGXf0xd3PNqgfT6iQ8Qd8rqOqlvniAU13jpfmgWNulaGURy7mSCCIvtlh1kjxkDnc2J4XJrxB2gkrjzPlvtuy1jeGQZJ-sAYKQF6dSyg_p21dj-56I7yaKKRj-Ka6uypLwXzH2JIOHOVNIV58Cq8tX4NcgfecCvytb-Jw45qFcAoizvUJOEktiWRbFYmLzTzqxbRymkQ00AtC_OJXhqS4NXBEEx87wvkFeOcnJOdtcPOHiD_BICSligvyPo3lTwbGBCMFjUi-Xtw0SY7vovLAE01sGO2SfsfbeEHasZuW8OJ-k3f2XV7B364FCLcDsohEkT6lDdQ0ErgxICbJb720y_vb2VmVFas-X-cg1duTTMT0wfWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29987e4127.mp4?token=IVQimFD7eYiwDZJz5hrAmynXbaxK9nCIVg_dUV_laBtJ-PivkQIfrXtTlpyETc8HXfJlulllvV3AerRznZUfkmFBxVcPVnt4UisEcb7-yZ6uZrL4Q5PRrCLVtMwJBfhLy1QQzVgi6i6pkOTvSWVMql-7KBH7CxWisFimpHQOXNzMkhNw8WWercxfWoBQnJFT_MtmNzSh8fBDVE0YFIbmhw47XsH6TygazVYZKHVbHZi6g3MI-nfRlPTl_5I-LP075sxa1XHP9NIxnDVRn4z-AgCZCHa3cHPGKyhfg8swfZtnvks7hS_N5Rq-CDDGXf0xd3PNqgfT6iQ8Qd8rqOqlvniAU13jpfmgWNulaGURy7mSCCIvtlh1kjxkDnc2J4XJrxB2gkrjzPlvtuy1jeGQZJ-sAYKQF6dSyg_p21dj-56I7yaKKRj-Ka6uypLwXzH2JIOHOVNIV58Cq8tX4NcgfecCvytb-Jw45qFcAoizvUJOEktiWRbFYmLzTzqxbRymkQ00AtC_OJXhqS4NXBEEx87wvkFeOcnJOdtcPOHiD_BICSligvyPo3lTwbGBCMFjUi-Xtw0SY7vovLAE01sGO2SfsfbeEHasZuW8OJ-k3f2XV7B364FCLcDsohEkT6lDdQ0ErgxICbJb720y_vb2VmVFas-X-cg1duTTMT0wfWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چالش جذاب هوادار ایرانی با کیت های تیم های حاضر در رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23335" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c684a93218.mp4?token=LcbPH6rQZ4jnI5SxAILqWY_iPYhBZWaHsnmKMXmVRd9KlqZ3Ze_LO6n9E59IFh82XKg757sSFJljArLZRkln-gUNQ1ydjjjVpPpU0TcnbZuEWEYZJs042j47U1wpo7gKLu8Lf3HOJZAGrPXwqE_r6GgqurUJjCPwuZteXB_tB-_OMzVEaMixFggtsps2HdzkURKrfO_GeYPTrwHjhP2cusnAe4Pn7d4sN_XQy709XMZHSscxk3fJy0ZmQp0YP31quFHML-KV6_Xru-WN_KFau8ORl9YGwsStuotYPCuSwMMdnPMWtbrQdb-upyaJ4ebcRppJLV6S802nesy9httDgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c684a93218.mp4?token=LcbPH6rQZ4jnI5SxAILqWY_iPYhBZWaHsnmKMXmVRd9KlqZ3Ze_LO6n9E59IFh82XKg757sSFJljArLZRkln-gUNQ1ydjjjVpPpU0TcnbZuEWEYZJs042j47U1wpo7gKLu8Lf3HOJZAGrPXwqE_r6GgqurUJjCPwuZteXB_tB-_OMzVEaMixFggtsps2HdzkURKrfO_GeYPTrwHjhP2cusnAe4Pn7d4sN_XQy709XMZHSscxk3fJy0ZmQp0YP31quFHML-KV6_Xru-WN_KFau8ORl9YGwsStuotYPCuSwMMdnPMWtbrQdb-upyaJ4ebcRppJLV6S802nesy9httDgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
بازیکنان‌بایرن‌مونیخ چندسالشون بود وقتی نویر اولین بازی‌شو انجام داد؛ منتظر کارل بمونید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23334" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23332">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-8byVmGjFrrWdwTWoI3xevlGJ6-df74rDSCBhaBJqHH8DTRRR56wbINqzvIRQwsfqPgKn3ecRM7QosoqtFXjandzGl-dZ7I56kZXcncg4KYby_q_20vLqEacdsCJc_80Uf5I8RYKoKfI5O6-6HgQ6TdqgzT1haT48ZwjFa0iluqQXBjM0R5IkspjYN4XajjrJyFOUMvKETHtfbtKZRXZLtYEjtVV32jKyo1vRlORPwjFpRRDaqigjvoc1XJSwxLimwcO9WXombX0cnH7v6Mw207qhShT6ReOtq6F6C4GmQPiDpivrHawkyA_PbEHd8DDZjp3s8w0yg5B9ijfXWuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23332" target="_blank">📅 10:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23331">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|آتش بازی یاران پوچتینو در گام نخست‌ رقابت‌ها مقابل پاراگوئه
🇺🇸
آمریکا
4️⃣
-
1️⃣
پاراگوئه
🇵🇾
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23331" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23330">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3m_JSzzaJAKWFvERTwY97k094XHxtu09bRu1WtqyTUrJ3iU33603r3m0fYALf5BlWbMLHypHD9r-iOpSjOx1hObHQAd_QHy4UXMVO8Tlk8ZKnTCjRMGDWFtUKxsQOuOibkPRksnoQpFoDiNtQx3QcSGShH3VWfNKRomM7AY05TdBIooBWddK_MFejeeLFt_YHFKyBK-_YlIiOIAtXDDgMYvKyofGbM0MDhuGLezhzrImXuHZh4ea3K7iYHzhQtTrzopRTfmSnXRy64Vsum-5lCWjxQZvvfOQFSYuBCD6A9oX3p6t3_EprRh2y9jrPCFUccI4oMIP__F65bNgQlB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23330" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23329">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=IKJ7EuBWodgKuI8PZgat7-1p62LIUVZBiG4YxiQ7aWCmhiiUrveGYk59edmr9blIvdHbMycveEsgaq86Tt565viquXBiDKiGytuPi5-WIGPYGIGulXJ9Xo-QdumGx5NIiZxoQUPwWe73R7g55Jv7a-raONESDIOKYPwLe7Tr-rk-q7E9q7YtF2TRHRPK9MgTfRMTUISDT7v6i_ZuYVgo7UpuN_SX5gR5ncbpPWgYTJdW3lbdxmEZgtCVG9loTJVOhh2Q--n6voD7L1FsLIHNfSk_ZCBgquhyIusKlvcA7C6VeXMkImo87eNUF4tGItQ_MtNeYZjjSJgE9fdpm4snSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=IKJ7EuBWodgKuI8PZgat7-1p62LIUVZBiG4YxiQ7aWCmhiiUrveGYk59edmr9blIvdHbMycveEsgaq86Tt565viquXBiDKiGytuPi5-WIGPYGIGulXJ9Xo-QdumGx5NIiZxoQUPwWe73R7g55Jv7a-raONESDIOKYPwLe7Tr-rk-q7E9q7YtF2TRHRPK9MgTfRMTUISDT7v6i_ZuYVgo7UpuN_SX5gR5ncbpPWgYTJdW3lbdxmEZgtCVG9loTJVOhh2Q--n6voD7L1FsLIHNfSk_ZCBgquhyIusKlvcA7C6VeXMkImo87eNUF4tGItQ_MtNeYZjjSJgE9fdpm4snSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تیکه‌سنگین عادل‌فردوسی‌پور به امیر قلعه نویی بابت ساعت دستش در مراسم پیش از شروع جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23329" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23328">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=bgncdZy9DQV0HL9Hpl2JJARnjgNTo6Imwy3FYuzhr2N55GraZ7yCQlFy798bWM0AEsbBavvonuID-EJVXoTDjTqSpeiRsKHMJMkybp8-r7FCwte9ESeXzMUUpn5Zc4bQvdnIAQlIlrFDWex8628K7b-fz8ssqfXrgMr1Vh7i6lul2eHox6fz1vOf_QMGi1gXA23Y41MN6LA539RHn_5QNsFyY7rABSpC29vwnqVcgRR8BFplzDEOnnztJCUOk030IEs_ZzQzw05dzSIbkxOWcfgJo2_mOVSVpjHoiiEzi5DE6OChNUM-WEqYjS_xa8NJJj0obQ-87a10bajdgBeHjQYG06INvOid2GzWIYzeeX5TIn7iw-AnhY6N9_FN5nBaViHbPmspXAwzfqb1f2LmYtT47ldtcZYu3RXBRZ1NNPEB9INQ9k7u3f-qF73HtMcRf9SIsjBjZ0SR5xH_MzQe0d9Z9Oc2ssn7uQTpmWkJBxw55E2Rz8fxpB25XmYB-MEgBlhFk0-HqFtMekfl6KMrDJOE3bQjh_MJLmRuwUlfrQySnNv0TYAXkv6uPB4qZF_Afkb9n_mO9luJMEmoqNNO06xlSJ0z1TjEro5xymAPgFr9xd8ItLvs0jSMTLT73vB9e_8ykmLgW0XcUgFu8pfRtRnJKea7X3PqeYmBDLEFgOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=bgncdZy9DQV0HL9Hpl2JJARnjgNTo6Imwy3FYuzhr2N55GraZ7yCQlFy798bWM0AEsbBavvonuID-EJVXoTDjTqSpeiRsKHMJMkybp8-r7FCwte9ESeXzMUUpn5Zc4bQvdnIAQlIlrFDWex8628K7b-fz8ssqfXrgMr1Vh7i6lul2eHox6fz1vOf_QMGi1gXA23Y41MN6LA539RHn_5QNsFyY7rABSpC29vwnqVcgRR8BFplzDEOnnztJCUOk030IEs_ZzQzw05dzSIbkxOWcfgJo2_mOVSVpjHoiiEzi5DE6OChNUM-WEqYjS_xa8NJJj0obQ-87a10bajdgBeHjQYG06INvOid2GzWIYzeeX5TIn7iw-AnhY6N9_FN5nBaViHbPmspXAwzfqb1f2LmYtT47ldtcZYu3RXBRZ1NNPEB9INQ9k7u3f-qF73HtMcRf9SIsjBjZ0SR5xH_MzQe0d9Z9Oc2ssn7uQTpmWkJBxw55E2Rz8fxpB25XmYB-MEgBlhFk0-HqFtMekfl6KMrDJOE3bQjh_MJLmRuwUlfrQySnNv0TYAXkv6uPB4qZF_Afkb9n_mO9luJMEmoqNNO06xlSJ0z1TjEro5xymAPgFr9xd8ItLvs0jSMTLT73vB9e_8ykmLgW0XcUgFu8pfRtRnJKea7X3PqeYmBDLEFgOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
طرفداران‌کشور‌های‌مختلف حاضر در جام‌جهانی؛ از سری جذابیت‌های بزرگترین رقابت فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23328" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23327">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚽️
ویدیویی‌بسیارجذاب‌ومختصر و مفید از مراسم افتتاحیه رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23327" target="_blank">📅 09:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23326">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4TVUfNHUucfgs2ipDSkrAXT1lLDUNmUI_zYVZKYLO6UhikiuQ209pBRVz-XyLT4kFLgXODYWzcp_b5PRwvgVQgMOJxbbRQtU4AMkjkCi5Whm449PgjChzi9ioAHnTrY6ObQ24HBXN-GsEdkt4yqL3d2elcT4kkFODUBCSYobj9M3NMZrwS_vk0vPpbUKW3GUinLFYTzBkcJ1oQ_jCKxb_mceSQUnf4FdTlmI6iQGnh5JXaQ27iJZ9araOJe4Rsz5g1TFq_AxYkwQQvv6mORqSfDFM0D0z6Ltl8PcN5M1HcdWlXXb4Qc2GoXl3jQXGn04qCuXCploetEd14ityWbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حال بازیکنان تیم‌ملی والیبال تو بازی امشب اصلا خوب نبود. این صحنه دو ببینید. باهم تعارف میکنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23326" target="_blank">📅 04:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23323">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fiwdy1s9IbXg8NE_z_OE2hRgZ4KKv8Zx7vyACg5RJtpZGXSI48ml6bxPaTeni_01dOABhcbIXX_iFbg5Oc8wcYBg_oZMK0FHZhOBL8I7cZYkPwCX9ZNQp83Bs_EYJ7UdGiJZagDEO4ylKsZ3Uh2iuMzVrBKM0LorBAijz4bvRTjO3T5UKCZG1jnuxsNAdcUvd-UzIENcq3nEu5kTIrcc5Tst-auPRqXHm1rj2lKc-YP8RYFbnwS_CoTznnzHgJlR9TmY7r4y2V_J3wxI0AOdDIJk660lGXr5UUDSrLkF_cNoobsBpqBf7xatHKeXJ_VRp96nw6ujEuLOx4YUxdAvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8LQc5X3eG8z8I1c8Pdm5k21jVvcIotNK-PASh2JrNIhz8wUubp8yG6wENyXj3PTndyrwueV3fwBWMbnHsFtRd_brZdn-Amn_0PoNAzXLuRRmQGgxi2HmkyBDoq-w3Vu3ySV56qUZ4KKfZ8VrTt4TtJRxIRuhcGS6NQ7ZVK7RznVBfO5rTuhVY3qg46HVnaARtak8DMxnJr69MK1FDfHUDPlUY4Xfh3OrB4QxIECdqdfHc-_LOJqWnx2__Fdzu9ToDNuy9ubA9dGLRZFy8-WWeeXaHxAq6zsScwAq_bGxeK49Ovm8x-iCqRxbKjMyHaVZvKbWnnVp5Jl_42hfscOZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
امنتیت بالای شهر تیخوانا؛
در ساعات قبل رو به روی محل کمپ‌تمرینی شاگردان امیر قلعه نویی یه جسد توی صندوق عقب یه ماشین پیدا شده که در حال تجزیه بوده. این ماشین هم توی پارکینگ محل اقامت شاگردان قلعه نویی بوده که دقیقا رو به روی کمپ تیم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23323" target="_blank">📅 03:07 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
