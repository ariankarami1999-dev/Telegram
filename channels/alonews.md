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
<img src="https://cdn4.telesco.pe/file/mO5IzfKLgXNTU3Afdx1zJjQbAbzOvCqh3Dp0VHaIhMrXmeEeAQSMYlRTveZv6i8Nrp1IyWx0vgRmcVfbsTbgBgti6ZZH0YE0d6KL1GoTedKDsPmAHg07QA4XJ5G0bBSq3_JrQtnx2HyzhZBosx6GkbqQLp-ZOKN3hFepKaSEdahwYicqHHaXKOEZYXOSWjGpIWPb8HFKLEPiSYbyH-5YyZOzQQU0TQ7upTgYOVkd4betpLW62LWJf_E7aN1fiqeSvuzB8utcSl_5VsV21iycjEq-0MhUxWg33J7Lw64A0P3FOJEcXurpnu5XtT80t7cXIhbfjnn5VY5xyh5t8uz3xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
<hr>

<div class="tg-post" id="msg-150791">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
محسن رضایی: معادلات نبرد رو موشک ها و تاکتیک های ما مشخص میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/150791" target="_blank">📅 21:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150790">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
تلگراف: خاورمیانه در آستانه دور جدید درگیری نظامی گسترده است.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/150790" target="_blank">📅 21:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150789">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edaa986fe9.mp4?token=ASgp91U3grvj4GbuA-rnoUi7wa5KUGMwdW5xB2KjSurAjDvtkRwxjTnJN8XinmyLWVYo19041zDUCYA3hmeCV2VAp_Sg7qh8eTF0zm647N_g8MQQyVwujbsBOxmwHnAmeZNAEN3arD22S1cZBYyBcr9T8o4s0NF6vrHOMfYCMfqT2j-xb0oOFwc9LUGMGYqaWOsT_gRIWJQfAI8jYSOpQJxE4XIYdI6Sy-FHupCemt27j0a5lWCu6zwKt_5PZVrW3qC_kLn6zk79Yw7GhBu5P7o8RF7xNAt69qESRjpwLbJ6Pd5ReyFIaHbms3GlqjQx49hH6JEDjk0KvH81Wjcawg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edaa986fe9.mp4?token=ASgp91U3grvj4GbuA-rnoUi7wa5KUGMwdW5xB2KjSurAjDvtkRwxjTnJN8XinmyLWVYo19041zDUCYA3hmeCV2VAp_Sg7qh8eTF0zm647N_g8MQQyVwujbsBOxmwHnAmeZNAEN3arD22S1cZBYyBcr9T8o4s0NF6vrHOMfYCMfqT2j-xb0oOFwc9LUGMGYqaWOsT_gRIWJQfAI8jYSOpQJxE4XIYdI6Sy-FHupCemt27j0a5lWCu6zwKt_5PZVrW3qC_kLn6zk79Yw7GhBu5P7o8RF7xNAt69qESRjpwLbJ6Pd5ReyFIaHbms3GlqjQx49hH6JEDjk0KvH81Wjcawg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پای رپر ها هم به تجمعات شبانه باز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/150789" target="_blank">📅 21:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150788">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkb5ktSW9dFhwNKwhVJ2ZO0TuuU-c2gag56lAELl4ih78S0CQ2sHLDVGyDbrRDs947jgeHMy1isLNCcnVfBESWBdwjhAM1Ta8wlYrek-qRg2bfsazxRtXmeKWxIkZ0hNUW3j1N1tjKEAHBFueeGfkDMXwex_OGKCXpYp05Ba6G6rRSp4IkT-D0v-FKRDpJD6aeh8YkFfFrn6uqZc4db6hdASNQA-o7uoCBA50ksIVb_GPM6Qt9f-H5auob2me_gOqYwFD6SamgTuD0t3_wo7dTwHCJhdQ3EjotWHQXW7yH6ycJ7aZgOV1cbnH23GEnqMOR8lUkjf2RYulelORpe24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز
:
مقامات بریتانیایی و آمریکایی معتقدند که افرادی که در نزدیکی پایگاه هوایی RAF Fairford دستگیر شدند، با یک عملیات مورد حمایت ایران مرتبط بودند که یا به سپاه پاسداران انقلاب اسلامی یا یک مرکز فرماندهی نظامی جداگانه در تهران مربوط می‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/150788" target="_blank">📅 21:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150787">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OeYSEW6f7HDjf1BoX4AAQbnKjk4MIYmz2wDXW-umo0FGrEhrRUFTbFpDCZaS3CddXhk6l-qJnASEA0zOhlgk_TDjPnVRxIMVGAn6aUXb4iq2ngqRHNg3BhJlXMwq8WJJWiHcjGPIWfKl9EdIhoXU-LlDSGJzshCJy_JVRd5I0KOIpqWnBGSpUzgkRnZ1i4L1RqTf8_q8BlCDUk7UBJuPTcbqWWAE6kH7iRAKLN_sbDTG4tBM0pUiiVMjiuYJzHwNYCImReBl4BuiKVkh-EQmqxzBRSXVkcwoNIHDaDdH4TKmQbT9HEu3ULhCU9gbC5ZrqHaLxpX71UveqtQ_xK0nwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری یو‌اس‌ان‌آی گزارش داد که ناو هواپیمابر کلاس نیمیتز، به نام یو اس اس دواایت دی. آیزنهاور.، به بندر بازگشته است تا بازرسی‌هایی از سیستم‌های پرتاب و فرود هواپیماهای آن انجام شود. این اقدام پس از حادثه‌ای صورت می‌گیرد که منجر به از دست رفتن یک هواپیمای جنگ الکترونیک EA-18G Growler و مجروح شدن چهار ملوان نیروی دریایی ایالات متحده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/150787" target="_blank">📅 21:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150786">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
پولیتیکو: ترامپ با حملات هوایی مجدد علیه حوثی‌ها مخالفت کرده، علی‌رغم درخواست عربستان برای حمایت بیشتر. او معتقد است حوثی‌ها نمی‌خواهند بجنگند و آتش‌بس فعلی را حفظ می‌کند. حوثی‌ها همچنان نیروی نظامی قابل‌توجهی با پشتوانه ایران هستند.
🔴
مقامات آمریکایی درباره تداوم حملات اختلاف‌نظر دارند و از درگیری گسترده‌تر هشدار می‌دهند. واشنگتن فرستاده ویژه‌ای برای مدیریت بحران عربستان و حوثی‌ها منصوب نکرده و تعامل دیپلماتیک با این گروه دشوار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/150786" target="_blank">📅 20:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150785">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwIZ_lmrc5uUy34kgupx3ZdPyiI96gjMcG0Xd3u3R7U8kwpnLAToiOD0Tgy8g2OhyvqdEmSq4XeV6ML6Ls6eQe4vxbUluMf1R9B0WtgJzu1Ll3yYht9HZbsxY_ljyVUaC6YXaNLq70n1fEbEsdJR8bNfqOkkkaszv6lDCObFEq6kbHga4jml6su2JDVWYGsemXGbCIqv1zI9YM6NJyLOao5C2j6wjO1QSX_wQcLcQkn5Y0Byj_XKyvKvAiN1BV6x0gH0vM4vv9XY7DR-jz9tZP83cLnJqiaKu2CQHve37UkHxJ1oefDaQmShHGW2Uygmk5wKbr9nyOUPa-QOLdYfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس، ابراهیم عزیزی:
🔴
از افغانستان بیرون شدند.
🔴
از عراق فرار کردند.
🔴
بعدی: اخراج کامل از غرب آسیا.
🔴
این روز را علامت بگذارید؛ نزدیک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/150785" target="_blank">📅 20:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150784">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQRp6krYhFVsP2HIQCK9VemcrbV9Fx2PgmKhatUWoekCCaZ2WARs1HZjIzH9lNZe7sJmJyLcPpgxIV5NGpKdDoxDBq37UgNIKXyztGeuu-GGXqjy8mJcr6nX8ipxO3mGSUjoOPToZQJalmmS-QwCyP5oJKhPNT_29GSatMfUtufw8HCg9fia059Zy3B07Xs5yvZU9BmmynQ_4hHs7lOpaxTbU43a2DUqYXitdEH65J5P_S_qBk-FGyM5teT0x4WR3c2Xx4QYL8IKwu3FZ2Hv0Mowgm-Xlu4Sj3t0NUgBtvkAxovfyLNj-I8-mTWv4ICQQlZPmwrIagHVG3VP4s2VWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوشته های سردر اتاق رتبه ۱۳ کنکور ریاضی ۱۴۰۵: دوست دخترم مادر شد من هنوز کنکوریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/150784" target="_blank">📅 20:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150783">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KG5iC57JI41O3FQUUawanaNZpOxpFT15Cpgk8GD1wKQX7me33-zcgObIdl1Fr0wOL6c6Ne9hsWtETAoHquBonOvN3CaScnkcqa38R2yLqRq4NRCJ_DIzUKfghxpdtqM-Dp02PRQdDN8Oxut0PpO_DprGfIF7BEITM-_Ccufz_UrS7wmBo01Bt-VNRRmlI8FV10sqKEVAk2xDfKXCa-jb_FHsJH5jglIStWgzhcgCOgsIX3WQ4MjQmDS-toDWvxnvva1ExJMnVOKRAdvAEK1quvE14IlOJNFekOnRfiPeeRtzC5OrJqlxU_3NJ7xGZbsvfODygLZr-1XLygaygqkqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تابناک: گلشیفته فراهانی قصد داره به‌زودی به ایران برگرده و اقدامات اداری لازم برای این موضوع هم انجام شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/150783" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150782">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
زن بیژن مرتضوی: تو مجازی فحش میدید تو واقعیت دنبال عکس و امضا
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/150782" target="_blank">📅 20:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150781">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzL1n8qqX88bcUlPEVYV7xmfDaxsmN97L8AjyXjWpwkpGlYwkdS9gicLRq_UIpqHxMfHV4DNSwz22skkGAcbD-Ljlc955O38TKDY0vf6Ba6V328PDmWWPjoaEhYC4eecKLXZxbyx1X-PXeD4cpNU_a7yZtTnwtiPji_PzVkt5zeuSsnb-5-qlof3YGslaChEaz-KyROQsD8C2MQUIZzLqWoiAr0qiXzjbqWkpxO96jLGECE4qOjVNGrCCnoVy_A0TXLH9anVeTL5DOQOrOs95JkBVkrobv07EYGV5k_arkm73zxcIzHBmKbdjttn1Nr8K9IAmEBvHplSe9GHFTTlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به خاطر اعتراضات داخل فرانسه، اوضاع اینترنتمون بدتر از چند روز قبل شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150781" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150780">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b387287a.mp4?token=suBsdIQbqlsJRY5KN1yWEvPvlTdcfuyF6pGuexLDiMk1NVdnkA3ozLK1mVKIOYislkIrdiIEMXdAr5dBqgYBHL-_X-8y02nnhbNuqKCgCQbUmd7ZwXCaw3486F2CwwD38K9Nol5R7U9l-kTB2Q0AdM9d2pLVVzkm3TJK4UNl72p0NRc2V8alRWmWIHXfmPrCgMWm9lV7HGcEB_NR654CmNp1R_1lFlO9vw6pgl6ixYytW9Yea4QbdpSAW4mLHVrIQpLCOXGxmAWIUiH4crriHJxTSGKQk4R9ZTthybHmS469rc3SlPpyOPAQ1OzbyN7h9MYZM9tmAD7DPgLJG7XIxT_KeWmnUKtZ6ws_3sfkROTqmiNDPRuoUyregtf8DHdYiOUu_LbsauG4atmd-67FsRodkMWyRT_JM5LfBER9fgt8gxqNs2QgamsqUy9vP80Gfhjw6N0BjFRys83PovUn3IHLu2Y1lWrcP-nejHy8oAJjEV_tHf9GJd8bnKaPIDCcRHYlb9aCC9_4Ti3RgIOtnBETCFnB2XQNOEYG-m-ylpcJcIPdEIRLWAOqRhdl6ZXSMvNswoNz3KLOZ67tSIXXWg2jwlim5uRT9X4hxSv00_NqiQWRtkiWndyfjECEDtU7ZOkMzNQ8Uvje3_xVySe2XDcYe4mhcMJPw7KQS26xGMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b387287a.mp4?token=suBsdIQbqlsJRY5KN1yWEvPvlTdcfuyF6pGuexLDiMk1NVdnkA3ozLK1mVKIOYislkIrdiIEMXdAr5dBqgYBHL-_X-8y02nnhbNuqKCgCQbUmd7ZwXCaw3486F2CwwD38K9Nol5R7U9l-kTB2Q0AdM9d2pLVVzkm3TJK4UNl72p0NRc2V8alRWmWIHXfmPrCgMWm9lV7HGcEB_NR654CmNp1R_1lFlO9vw6pgl6ixYytW9Yea4QbdpSAW4mLHVrIQpLCOXGxmAWIUiH4crriHJxTSGKQk4R9ZTthybHmS469rc3SlPpyOPAQ1OzbyN7h9MYZM9tmAD7DPgLJG7XIxT_KeWmnUKtZ6ws_3sfkROTqmiNDPRuoUyregtf8DHdYiOUu_LbsauG4atmd-67FsRodkMWyRT_JM5LfBER9fgt8gxqNs2QgamsqUy9vP80Gfhjw6N0BjFRys83PovUn3IHLu2Y1lWrcP-nejHy8oAJjEV_tHf9GJd8bnKaPIDCcRHYlb9aCC9_4Ti3RgIOtnBETCFnB2XQNOEYG-m-ylpcJcIPdEIRLWAOqRhdl6ZXSMvNswoNz3KLOZ67tSIXXWg2jwlim5uRT9X4hxSv00_NqiQWRtkiWndyfjECEDtU7ZOkMzNQ8Uvje3_xVySe2XDcYe4mhcMJPw7KQS26xGMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ:
ما جوانان آمریکایی را داشته‌ایم که گفته‌اند: «من را برای جنگ با کلاه‌قرمزی‌ها بفرست. من را برای جنگ با کمونیست‌ها بفرست. من را برای جنگ با نازی‌ها بفرست. من را برای جنگ با اسلام‌گرایان بفرست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/150780" target="_blank">📅 19:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150779">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278c1d4127.mp4?token=KKXzt6wsQfjYFylyvAg70qJl7aqqE1eyghGgCnQ6NO7KmPAIv5C62khRwDa_FYOCU6_zQqXMbp7PIoUCOoTatmuB16l9dNVBL-dTiRYena01ilcgHBcBktTmOsHRs6pGgsuFljXFExxx4PqG358Z8HeMF6XC9qAxXu8Dm0ULj7Uyv2SmHttij0gamaSz3N5Sq3N0jFbxvC8nYMP160ly2iDnvhsDxvA-Zn6eNJDjpl3E7jNxRXLTmd6pAfo8nZDzmWDrVm7TNwxMKA-mgT7H_MrmWr2-AkvEMxs6IcrXAOEmCH86N9FwwvLPVR8y30QCSAWfxLpe5Appn-hVHU1EgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278c1d4127.mp4?token=KKXzt6wsQfjYFylyvAg70qJl7aqqE1eyghGgCnQ6NO7KmPAIv5C62khRwDa_FYOCU6_zQqXMbp7PIoUCOoTatmuB16l9dNVBL-dTiRYena01ilcgHBcBktTmOsHRs6pGgsuFljXFExxx4PqG358Z8HeMF6XC9qAxXu8Dm0ULj7Uyv2SmHttij0gamaSz3N5Sq3N0jFbxvC8nYMP160ly2iDnvhsDxvA-Zn6eNJDjpl3E7jNxRXLTmd6pAfo8nZDzmWDrVm7TNwxMKA-mgT7H_MrmWr2-AkvEMxs6IcrXAOEmCH86N9FwwvLPVR8y30QCSAWfxLpe5Appn-hVHU1EgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ، درباره جمهوري اسلامي ایران:
امروز نفت بیشتری از تنگه هرمز عبور می‌کند تا قبل از شروع درگیری، زیرا خلبانان باورنکردنی کنترل فضای هوایی را در دست دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150779" target="_blank">📅 19:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150778">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=Epkc4n0qSLyrzi4w7Xh_Opl0jxvM4WvPuEoawBHrwekr1N3yphoWIX1vdF4eUymnk4c7brBreh-ijcJ532Hf3Gfmm48XQChvpdunz_TOTe17qiIXDSKNgLRL66l169Z33UqOaD4K1jEhHv30OeAAIy5PilAi-1POJFwqGmjd0l8NbXWfKSR-_RpXxASQdf-2-54cOpPkTF08yqozVdJCzE0zMljiIeWqANudhosEuBTQrT_HYd3VPpg1A-ruZrCeD0Mum_a0Fi72bDJZpVnM-5FBNtEUUUYSNVa8AQ8UE2H5gD_7R9F-iECoUZTEDQnRxueRUrrhn5DTNBVtgdNNkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=Epkc4n0qSLyrzi4w7Xh_Opl0jxvM4WvPuEoawBHrwekr1N3yphoWIX1vdF4eUymnk4c7brBreh-ijcJ532Hf3Gfmm48XQChvpdunz_TOTe17qiIXDSKNgLRL66l169Z33UqOaD4K1jEhHv30OeAAIy5PilAi-1POJFwqGmjd0l8NbXWfKSR-_RpXxASQdf-2-54cOpPkTF08yqozVdJCzE0zMljiIeWqANudhosEuBTQrT_HYd3VPpg1A-ruZrCeD0Mum_a0Fi72bDJZpVnM-5FBNtEUUUYSNVa8AQ8UE2H5gD_7R9F-iECoUZTEDQnRxueRUrrhn5DTNBVtgdNNkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ:
میزان زیادی از اطلاعات نادرست، اطلاعات غلط و پروپاگاندا عمدی درباره ناو هواپیمابر یواس‌اس آبراهام لینکلن وجود داشت، اما ۸۰ درصد از گروه ضربه‌ای این ناو برای تمدید خدمت ثبت‌نام کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150778" target="_blank">📅 19:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150777">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih4nlecVwhbY2oEM71PrKhhUGjJtt7IZOuPAr3uTzihynXhlt03gHWxW2PJlfvBa8f5rCBU6qweqfhOvh9WV1tGfI16u6PeMxF_pd5ObCBArg6t0x4J2_CIgehLT_xtX5Kt6p2voF7P-QTXAjY7K59o_4AlpQJJp4zXjMjgCAzOOLmcIAVEFowaDFaVsSyiU3D1_5WZWJ-N-32NLOa8GXEnJgbE0iLnPYPUv3QFnu0961Yk7vPOHBB_48JGVkvLCIPNrUOgDWwGNGdS-I66aLpiJsINb7JTDOvGYtwCcDunGep4awsZaT6zc643tIdbLqnU9bNl7D8mSR7uRMYAioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مطهرنیا، تحلیلگر سیاسی: وقتی عراقچی میگه ما برای «جنگ آخرالزمانی» آماده‌ایم، یعنی ترامپ در پیام‌هایی که برای ایران فرستاده، تهدید به چنین جنگی کرده و ما باید خودمون رو برای اون آماده کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150777" target="_blank">📅 19:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150776">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
پرزیدنت ترامپ:
کشور ما تحت رهبری جمهوری‌خواهان به‌خوبی پیش می‌رود که تنها من می‌توانم این قول را به شما بدهم:
اگر جمهوری‌خواهان در مجلس نمایندگان و سنا پیروز شوند، من به تمام شهروندان بالغ ایالات متحده آمریکا، ۵٬۰۰۰ دلار می‌دهم.
جمهوری‌خواهان می‌توانند این کار را انجام دهند، اما دموکرات‌ها نمی‌توانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/150776" target="_blank">📅 19:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150775">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔥
کپی‌ترید پرریسک راه‌اندازی شد  برای دوستانی که ریسک‌پذیری بالاتری دارند، کپی‌ترید پرریسک  را اضافه کردیم.
📊
عملکرد این کپی‌ترید دقیقاً مشابه همان حساب ۳۰,۰۰۰ دلاری است که هر روز عملکردش را به شما نمایش می‌دهیم.
🚀
این پلن با ریسک بالاتر فعالیت می‌کند و…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/150775" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150774">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
به گزارش نیروهای دفاعی اسرائیل (IDF)، دیروز دست کم هشت سرباز اسرائیلی به طور جزئی مجروح شدند، زمانی که دو خودروی نظامی در نزدیکی روستای "راب الثلثین" در جنوب لبنان با یکدیگر برخورد کردند.
🔴
شش سرباز به بیمارستان منتقل شدند، در حالی که ارتش اعلام کرد که شرایط مربوط به این حادثه در حال بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150774" target="_blank">📅 19:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150773">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
حمله موشکی بالستیک عربستان سعودی به زیرساخت‌های مخابراتی در منطقه مجز، واقع در استان صعده، در شمال غربی یمن که تحت کنترل جنبش حوثی‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150773" target="_blank">📅 18:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150772">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8afbd943.mp4?token=livMNXlaBZ3EZP7Q0GqAs-6LfhC4s_5uJneuIpysPegGqpyxjI6aX__tvZOEhyDKyDvZ1PK0OYvH44FR6dBO3UYypoeyuwQgrxJKQX2Q3Hduv_6cnhb4sCiRWsmqqXy7X2HEHRmkjeVYChbiMbCXZn-U6M-v_qvoeYI1lMcJq5-mvIFpMiNAmVcdz46E5ba4K2X16jqzndm1na8EXwiZSneidLYGs4GkFuIaCA5jZ5Ax5Y7d_sKowV1rCd5Mkqr3wSWYA9o6ahFQZwlYR1-KKaBT6KMz26FUGnI9oRQdFk42EvNicooFKJISpL78mldJNGqIxTBtLxXxFngFLw0BsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8afbd943.mp4?token=livMNXlaBZ3EZP7Q0GqAs-6LfhC4s_5uJneuIpysPegGqpyxjI6aX__tvZOEhyDKyDvZ1PK0OYvH44FR6dBO3UYypoeyuwQgrxJKQX2Q3Hduv_6cnhb4sCiRWsmqqXy7X2HEHRmkjeVYChbiMbCXZn-U6M-v_qvoeYI1lMcJq5-mvIFpMiNAmVcdz46E5ba4K2X16jqzndm1na8EXwiZSneidLYGs4GkFuIaCA5jZ5Ax5Y7d_sKowV1rCd5Mkqr3wSWYA9o6ahFQZwlYR1-KKaBT6KMz26FUGnI9oRQdFk42EvNicooFKJISpL78mldJNGqIxTBtLxXxFngFLw0BsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری نزدیک از آتش‌سوزی گسترده در پالایشگاه سعودی آرامکو در ریاض، حومه جنوبی شهر ریاض، در مرکز عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150772" target="_blank">📅 18:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150771">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
از دقایقی پیش به دستور بانک مرکزی،
نمایش نمودار قیمت تتر، دلار آنلاین در صرافی‌ها متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150771" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150770">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2JbUSKfbJ0mFx_aI_9zJmg3f9xwls3-ATlEDpA-BsF58BKhsFjnlbuLU9P12ZK_OcQQpmXrp1Edo-gyZmqnruVAYmTr65Ahs1L2uRn81hjnPzwuWksn8RnFN6zhpqhS3NKELVdvbYIYecISKgvyTIPQ7HqE-B8uNd_U9Zpdm-A_binTXDxc94Yv1nqGCR9f6MfOQ6i_F8UfaMhLOFLOt2KbnC7mY_tty6Ffx22J2U0vWQ_OMZomJKY5j4k37YdvGCvatlLttDl92Q1h-P2bYTaZExE5JlnwEsM4eJ1RsEAsCz1O5iLg9ydQ6ds1QH2dptpiS9LeEifk8D4lgpSo5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز: به طور خاص روزانه بیش از ۱۸ میلیون بشکه نفت از تنگه هرمز عبور میکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150770" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150769">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b3e7c6b.mp4?token=Rerl2J-cs-ox7vhcJO8-zqKSlCZoiiU1JDUFBtbQc_O1coOCR-bg1V-jzZk9ysuw6vCj8avOWZp5QVpZq8CIAKAEBtOBWOWHPsVo3HxTZu1sVASiQal0AmZ0a-7l6RD1S2tz00lNyfVpqoCgFQISCsrcalM7_D3VrVWpHJE-gV7IKMwHa7BF_Y8uj-W7ircJkiaJvWA_TInfRW5rKXi6BIuoEgUqhM-LvSQ7CK7dcj-WHR5j6qr1v9ELO2_poB4Z_zoO-meVWwQPCD2R7T92nPs8Si-EDWrf_dN6P4zr5Kw37cuKkPAJtKa_KZMSHtparaGMTu3PyWWXLysSlkVTlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b3e7c6b.mp4?token=Rerl2J-cs-ox7vhcJO8-zqKSlCZoiiU1JDUFBtbQc_O1coOCR-bg1V-jzZk9ysuw6vCj8avOWZp5QVpZq8CIAKAEBtOBWOWHPsVo3HxTZu1sVASiQal0AmZ0a-7l6RD1S2tz00lNyfVpqoCgFQISCsrcalM7_D3VrVWpHJE-gV7IKMwHa7BF_Y8uj-W7ircJkiaJvWA_TInfRW5rKXi6BIuoEgUqhM-LvSQ7CK7dcj-WHR5j6qr1v9ELO2_poB4Z_zoO-meVWwQPCD2R7T92nPs8Si-EDWrf_dN6P4zr5Kw37cuKkPAJtKa_KZMSHtparaGMTu3PyWWXLysSlkVTlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
الهام علی‌اف، رئیس‌جمهوری آذربایجان، گفت: «آمریکا و چین دو ابرقدرت جهان هستند و هیچ ابرقدرت سومی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150769" target="_blank">📅 18:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
تلگراف: خاورمیانه در آستانه دور جدید درگیری نظامی گسترده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150768" target="_blank">📅 18:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
حزام الاسد، عضو دفتر سیاسی انصارلله یمن، در واکنش به تحولات اخیر گفت: «تشدید در برابر تشدید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150767" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ec018bef.mp4?token=SXc8Ezf3AU3rzn3wEl0lTJh7bNuYbVNUHhv1cwmoKvJS4nyzA7j_gSA9MCSQQtS_Dafoqnm7IpcBylBnqu6gHgFwFirKKQBdQG__VNcUfNdkKp0Ojts8xQMj8qm9p5xcwp2QKfXfG85eYCd5hihERq1jivtayViylIbko8MwbVnBVDJhtyrMVfPPLDkfFC0BIXnmxfY9iiKhAkSf7MToApPDngr7HdQgtjFJM7umW6S8NEgHajNpzgfD9W4JTyoa_aFX2eglcHg5sT1LcfF32DY1me7sQFrnNxH1gtVcay15KIXX8MDMYoogGWzm0jKcWIZQdQSHSty-XqC6YcYloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ec018bef.mp4?token=SXc8Ezf3AU3rzn3wEl0lTJh7bNuYbVNUHhv1cwmoKvJS4nyzA7j_gSA9MCSQQtS_Dafoqnm7IpcBylBnqu6gHgFwFirKKQBdQG__VNcUfNdkKp0Ojts8xQMj8qm9p5xcwp2QKfXfG85eYCd5hihERq1jivtayViylIbko8MwbVnBVDJhtyrMVfPPLDkfFC0BIXnmxfY9iiKhAkSf7MToApPDngr7HdQgtjFJM7umW6S8NEgHajNpzgfD9W4JTyoa_aFX2eglcHg5sT1LcfF32DY1me7sQFrnNxH1gtVcay15KIXX8MDMYoogGWzm0jKcWIZQdQSHSty-XqC6YcYloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی پویش جانفدا: در میان ثبت‌نام‌کنندگان افرادی هستن که اقامت آمریکا دارن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/150766" target="_blank">📅 18:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
زن بیژن مرتضوی: تو مجازی به اقا بیژن فحش میدید ولی تو واقعیت دنبال عکس و امضا هستید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150765" target="_blank">📅 17:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150764">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
قطعی برق در اثر طوفان شدید در قم
🔴
بر اثر وقوع طوفان همراه با باد شدید و گردوخاک در سطح استان قم، تعدادی از فیدرهای شبکه توزیع برق از مدار خارج شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150764" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d34c7efd.mp4?token=o2Ec8jwgC5GTrGeM8LSvmjLfSFYqpHUzx9HSGE4UQIDBIF66x5B1MpuFwtohrUCPUTd2ZJsfkzx0NITZU9cwl9BNRn416Byq6w3mJAL2gNNc0OtL7oBTzmS5N7koMtD9UELX1klZ5aXoX7t41eQ7Yc4GVJ09umY8rW2XZgY0gW0ytQ3CwkTAFCluSWRtw509AjVBL0fvTqDnvPKPFMe7Hb9euMw4d-dpxxjh6igw_Tz7uHgsh9QLhpVZC1llO5IZKwwxLgM19Bkf8NOY3sfGOmmkwcYhj9OpcvDztmqN2D2drXygqf7JAb3gPO0w4y0DHkDezwfKASH2jFPmqjHBN6pNntKitze4LnG3ouYEyK0EmW0Lr3luvoqJZJvHUeO905Asyhq1O2gVNPdAdKVTFl1LA_zIZF5WO6IHFShD_PkekmrTdYkTY1jt77elSBHOUDWDh10hqBalUldyJPxrq7Q7sTmxBGvYZLz-0l2yGfFspJGj1lPMT6CzW2R0UfVJZzVnlP8JY-pUOo2cMpwad4dDKfPXCA8clYOi_Ck_iZttW2Eyrla5pSaCnyCQtRoc06AjxmSVdvkIyXUWFinwTKDOQp-r4cI9PnP1eRvSvqvwj1Gu_zXRpBLyLut3AL7pykIgG7QZEd58-VnSS2EvldFvcPR25-OcHjs2t8QBHbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d34c7efd.mp4?token=o2Ec8jwgC5GTrGeM8LSvmjLfSFYqpHUzx9HSGE4UQIDBIF66x5B1MpuFwtohrUCPUTd2ZJsfkzx0NITZU9cwl9BNRn416Byq6w3mJAL2gNNc0OtL7oBTzmS5N7koMtD9UELX1klZ5aXoX7t41eQ7Yc4GVJ09umY8rW2XZgY0gW0ytQ3CwkTAFCluSWRtw509AjVBL0fvTqDnvPKPFMe7Hb9euMw4d-dpxxjh6igw_Tz7uHgsh9QLhpVZC1llO5IZKwwxLgM19Bkf8NOY3sfGOmmkwcYhj9OpcvDztmqN2D2drXygqf7JAb3gPO0w4y0DHkDezwfKASH2jFPmqjHBN6pNntKitze4LnG3ouYEyK0EmW0Lr3luvoqJZJvHUeO905Asyhq1O2gVNPdAdKVTFl1LA_zIZF5WO6IHFShD_PkekmrTdYkTY1jt77elSBHOUDWDh10hqBalUldyJPxrq7Q7sTmxBGvYZLz-0l2yGfFspJGj1lPMT6CzW2R0UfVJZzVnlP8JY-pUOo2cMpwad4dDKfPXCA8clYOi_Ck_iZttW2Eyrla5pSaCnyCQtRoc06AjxmSVdvkIyXUWFinwTKDOQp-r4cI9PnP1eRvSvqvwj1Gu_zXRpBLyLut3AL7pykIgG7QZEd58-VnSS2EvldFvcPR25-OcHjs2t8QBHbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون؛ بارش شدید باران در برخی مناطق تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150763" target="_blank">📅 17:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150762">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ: معمولاً در انتخابات میان‌دوره‌ای عملکرد خوبی ندارید و نمی‌دانم چرا
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150762" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150761">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
مهر: شنیده شدن صدای انفجار در جزیره قشم از سوی دریا
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150761" target="_blank">📅 17:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150760">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی ترور دو تن از فرماندهان سامانه موشکی حماس در دو حمله جداگانه روز گذشته در غزه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/150760" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترکی الفیصل، رئیس پیشین دستگاه اطلاعاتی عربستان: یمن، تنگه هرمز، بازدارندگی آمریکا و جاه‌طلبی‌های هسته‌ای ایران در حال تغییر محاسبات امنیتی عربستان هستند
🔴
خویشتنداری دیگر قابل ادامه نیست
🔴
چین وظیفه دارد همان نقشی را ایفا کند که هنگام توافق عربستان و ایران ایفا کرد؛ باید منتظر بمانیم و ببینیم پکن چه کاری انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/150759" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
گزارش‌های اولیه از سرنگونی یک فروند پهپاد آمریکایی در نزدیکی سواحل ایران حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150758" target="_blank">📅 17:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95b509824.mp4?token=LNcm0I5si0K-9RvPMmntHLv8tCCj0IEV_uzCY4Nf_-rNMYuP045BS34U9SQtSXnaNwTxLGI6j4vRPNfUKGPjL0acOoNE0UweBGYv6y2sgu_jeyI-kwzFeVAwo7bx6FvZCKmJoU1NT1lZYejBg2gDyA7asKtrg6iJHz6-Z3EuwpYIGFLxQZCl1gtpskHKeoMo1ca_bYAgsP55eXMiEzZIZHeVIFtnGzrieTErB2UbJOyHuBhBz0gXePnlpMjhZ3Gu-yzturKFmlcJLGCKvv2o588cOs-SGDkGV2oNxGzvRw9Ju456CmMNVV5zdTom48hGJ-wZ1NWhz7WEKYH_C-_gIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95b509824.mp4?token=LNcm0I5si0K-9RvPMmntHLv8tCCj0IEV_uzCY4Nf_-rNMYuP045BS34U9SQtSXnaNwTxLGI6j4vRPNfUKGPjL0acOoNE0UweBGYv6y2sgu_jeyI-kwzFeVAwo7bx6FvZCKmJoU1NT1lZYejBg2gDyA7asKtrg6iJHz6-Z3EuwpYIGFLxQZCl1gtpskHKeoMo1ca_bYAgsP55eXMiEzZIZHeVIFtnGzrieTErB2UbJOyHuBhBz0gXePnlpMjhZ3Gu-yzturKFmlcJLGCKvv2o588cOs-SGDkGV2oNxGzvRw9Ju456CmMNVV5zdTom48hGJ-wZ1NWhz7WEKYH_C-_gIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای از فعال‌سازی سامانه‌های پدافند هوایی در جزیره قشم ایران برای مقابله با یک پهپاد امریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150757" target="_blank">📅 17:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnhiLRrUTlioAugmkjuuzYTC8Li4l2hF9fbGJFxhV8FLl-KP9goysceUabZb_2zMiHJs5JC9Rc0cqEcYbY169ibiAcxCnfpkB6EbntUavF_SiCtHTZiTJFirrqOxI_xxtgBaI6LaNH925BGiVE2rBghIzvWDe1uzNfEeSb1QTHRCBAHgXzzhXOAxEwurNaUB1ZYl2baW65NgI4LQ1NeFlMaRBAZvjWxexkTo3_yI0QlQ21_N-zA6wBIzM85h5_-Pe8QB3LwklQiKBUbnNg7NVGV-LSLNP3q7WH7A2neKt_T9Bwc4ear0YUsQvWWCURPpWRmuXXfg6VDJCAMmiESTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌های اولیه از سرنگونی یک فروند پهپاد آمریکایی در نزدیکی سواحل ایران حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150756" target="_blank">📅 17:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: آمریکا در حال تقویت گسترده نیروهای خود در خاورمیانه و ارسال سامانه‌های پدافندی به کشورهای عربی برای احتمال ازسرگیری جنگ ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150755" target="_blank">📅 16:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/k4oZCBWMbm0lpfhsCLULDXr4Y5O730MGWBHF6XHYlL11gbnSk4i9l64VEt8bwFjd71VsB8gUu79CrOccZdCnxfab91afAuxeTw0zKu75Q6zZ6uWl_E1K8_HdaBs4noErXM_TvgJU17KTwJFO5Vci4Wo7xHYKq2Q2xUnCnqfLqnGCq3Aj37GHp7SxjHFWwFlJJvdZphZC5jdBcQF3EwS96D3UH8ddaFfqeTl098WPl6iypfsTlDwBFrhlgkxKdVC7xJ-E13nZG9gqsYIF7k7Qw2RVcJFXJUwpT8I68c2xXRKspo4m9bICj2zB4LK6lkHQNCY-ifHqla-eunCgzUYZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دریایی ایالات متحده ارتباط خود را با یک هواپیمای امدادی که شش نفر را از جزیره ناکات به سمت بوستون حمل می‌کرد، از دست داد. این هواپیما در حال پرواز از برمودا به بوستون بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150754" target="_blank">📅 16:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
منابع عربی: وقوع چندین انفجار جدید در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150753" target="_blank">📅 16:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی سپاه اعلام کرد که سپاه موشک های بالستیکی ساخته که میتونه اهداف متحرک (مثل ناو هواپیمابر) رو مثل آب خوردن مورد هدف قرار بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150752" target="_blank">📅 16:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwXe5ldBKEYHyRcXmFGbHByZxzj8hhcpF39rZ2yRyIRyRLb_4p9Hj66DaOlur52CsDyLbaqOCjw2ENrho2GYWbVpSlI0TDT0_cSiLbHdSx7PHefA6StW5FvGH9nyD6HpFgAub8pcD1ypL_lvYzg9J2Vvxv1V4SG2330CQJsTc553jIPDe8NK3uC5h_XsDN6XttiulLd91W-yHI7AhW_K_2iclXZLE5R8M3qAT2oNcHY2NK9Pz8mMbO-kAwQw8DII1tB7sJ0KTg0Yru9OjmTcVMOd-Jerww9D4-IW1PaPJ-VTEJ_PHsuvWtNbpdR5cinkiksfOV5jZnfLPBN5hW2SGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادامه آتش‌سوزی در ریاض عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150751" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا به خبرگزاری Axios: ما ایران را به شکلی بی‌سابقه منزوی می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150750" target="_blank">📅 16:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری /
رویترز: جنگی که ترامپ بارها وعده پایان سریعش را داده بود، ناو دوم آمریکا را هم به هرمز کشاند
🔴
رویترز: ناو جورج واشنگتن به‌طور غیرمنتظره از ژاپن اعزام شده و مأموریتش پایان مشخصی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150749" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
تحلیل فارن افرز: چرا ایران به سمت تصعید جنگ خواهد رفت؟
🔴
تهران ممکن است حتی علیه اعراب عملیات زمینی به راه بیندازد و پایگاه‌های آمریکا را تصرف کند
🔴
ایران در حال تنظیم نسخه‌ای از راهبرد «چمن‌زنی» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150748" target="_blank">📅 16:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری ایالات متحده، درباره  ایران: برای اولین بار در تاریخ، از زمانی که شروع به پمپاژ نفت کردند، این هفته هیچ نفتی در آب نخواهند داشت
🔴
آن‌ها هیچ درآمدی نخواهند داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150747" target="_blank">📅 16:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ایران این هفته نفتی برای فروش نخواهد داشت
🔴
ابتدا وارد درگیری نظامی مستقیم شدیم؛ نیروی دریایی و هوایی آنها را منهدم و توان پهپادی و موشکی‌شان را به‌شدت تضعیف کردیم و امکان بازسازی آن را از بین بردیم.
🔴
سپس به «دیوار فولادی» و «محاصره» رسیدیم؛ اقدامی که پیش از این انجام نداده بودیم.
🔴
حالا با «عملیات طرد اقتصادی»، آنها را به شکلی بی‌سابقه از نظر اقتصادی منزوی کرده‌ایم.
🔴
در حال حاضر، آمریکا حدود ۱.۱ میلیارد دلار و ایران صفر است. برای نخستین بار از آغاز صادرات نفت، این هفته هیچ نفتی برای فروش روی آب نخواهند داشت و درآمدی هم نخواهند داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150746" target="_blank">📅 16:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6caf83dd9e.mp4?token=V-Z7hdS85LtQbHW9mRfUrH7hjjBQokb3C23Hrc4_SPgpEFfF0ioz49k2cDIRPoNURjGvSvWc6GZd6S1B2Y4v2H2nFSlEm5jyIlc8rVKvsyaypwwdQ0CMGhtMFvRQTlTVd132n0xH_sz0XqqO8G4cNmPGW4jhv2dqZq2VbHrbVhQJxmvB8D1ak4qF88ShtrEyYY1ibndQLcuyGqRUMunu_HEHijKrHrv0lYhNDOPp9_YN1HcrzRLfLzRa9fmtkrCmDylvmmN2t6PNbJCnj4QtX3TgA2D-gtSPi4m13KmxaDAVyYtbiqE5jqYitkYGPjhkyDT1DwcSE02CXPRilDP9wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6caf83dd9e.mp4?token=V-Z7hdS85LtQbHW9mRfUrH7hjjBQokb3C23Hrc4_SPgpEFfF0ioz49k2cDIRPoNURjGvSvWc6GZd6S1B2Y4v2H2nFSlEm5jyIlc8rVKvsyaypwwdQ0CMGhtMFvRQTlTVd132n0xH_sz0XqqO8G4cNmPGW4jhv2dqZq2VbHrbVhQJxmvB8D1ak4qF88ShtrEyYY1ibndQLcuyGqRUMunu_HEHijKrHrv0lYhNDOPp9_YN1HcrzRLfLzRa9fmtkrCmDylvmmN2t6PNbJCnj4QtX3TgA2D-gtSPi4m13KmxaDAVyYtbiqE5jqYitkYGPjhkyDT1DwcSE02CXPRilDP9wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری ایالات متحده، درباره چین: من فکر می‌کنم که آن‌ها — در ۶۰ روز گذشته — بیدار شده‌اند به... من فکر می‌کنم که آن‌ها ندانسته بودند که مدل‌های متن‌بازشان چقدر قدرتمند هستند.
🔴
بنابراین مدل‌های متن‌باز، تقطیر صنعتی انجام می‌دهند، که یک کلمه زیبا برای دزدی از مدل‌های ایالات متحده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150745" target="_blank">📅 16:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150744">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=BBRoSK2HmqFfh5Ad6sRuB2emb9UobmlWJOeZiPkEHpizy4OYCHUT_-4wgwbQVhiY1Bl0ckus7HTzC_J_mU9UDt8pHq64ENwVBL0l8P7CV3uis8-hkIdVl21QsTQ96INEaX8TrHKA5_ZI05ftI8UfyRZ8HDWPFjytMqgPb69mn17DYGqEZe9HBSJh60a0k6SrL-EUfk8nOJisaxXmZzLoNiZpEqoHxwX6xEgibIr9QP6n9Xaei0OiV5V8a3wY5c7UEVWCjvNPa8oBeRbJETxcffsE_HicZn1HUMRjsBx5oWSIh0MaQZCbbED45GLBIxeL8uVovWSU9jJ3CM7nA3daqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=BBRoSK2HmqFfh5Ad6sRuB2emb9UobmlWJOeZiPkEHpizy4OYCHUT_-4wgwbQVhiY1Bl0ckus7HTzC_J_mU9UDt8pHq64ENwVBL0l8P7CV3uis8-hkIdVl21QsTQ96INEaX8TrHKA5_ZI05ftI8UfyRZ8HDWPFjytMqgPb69mn17DYGqEZe9HBSJh60a0k6SrL-EUfk8nOJisaxXmZzLoNiZpEqoHxwX6xEgibIr9QP6n9Xaei0OiV5V8a3wY5c7UEVWCjvNPa8oBeRbJETxcffsE_HicZn1HUMRjsBx5oWSIh0MaQZCbbED45GLBIxeL8uVovWSU9jJ3CM7nA3daqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده، بسنت:
ما به سوی دیگر این اختلاف با رژیم ایران خواهیم رسید. فکر می‌کنم عرضه نفت بیشتر خواهد شد. فکر می‌کنم قیمت‌ها بسیار پایین‌تر خواهند آمد.
🔴
افزایش دستمزدها ادامه خواهد داشت، زیرا ما در حال رنسانس تولید هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150744" target="_blank">📅 16:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10dd1f1bb3.mp4?token=vpvWZtOzn9WuaCouScdzEjmmY_bFXrMLbFasygHPcfv2VdrD81szFUkjD5wocuIn0u1eWp3WYaNyuj6rE2s6dILvvJX3LWNigXTihVA1GpqFfOfONavwMc1YOsT06lmTB5kJbHxI3dMCvtiZyurCKz6M_36kynul-iW4trxsLAxj_ztmw2jORS8cKkoDb2kQJ3L1yAqqoVQ9mU7mB96LQqh89ZlcqXIcWURaeGHQBSWtpW3aF-BFoglhToHjoiuVYpIJvs7Ds-ZhMo4Dmi9ZtMCFqJQH4BfcbL0FU5ykfyw680HBUlqnyOcv8rkUd_ODQ-wPejoWv7-yPtJyXssOGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10dd1f1bb3.mp4?token=vpvWZtOzn9WuaCouScdzEjmmY_bFXrMLbFasygHPcfv2VdrD81szFUkjD5wocuIn0u1eWp3WYaNyuj6rE2s6dILvvJX3LWNigXTihVA1GpqFfOfONavwMc1YOsT06lmTB5kJbHxI3dMCvtiZyurCKz6M_36kynul-iW4trxsLAxj_ztmw2jORS8cKkoDb2kQJ3L1yAqqoVQ9mU7mB96LQqh89ZlcqXIcWURaeGHQBSWtpW3aF-BFoglhToHjoiuVYpIJvs7Ds-ZhMo4Dmi9ZtMCFqJQH4BfcbL0FU5ykfyw680HBUlqnyOcv8rkUd_ODQ-wPejoWv7-yPtJyXssOGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری ایالات متحده، درباره چین: یکی از مدل‌های بسیار قدرتمند آن‌ها، کیمی است. کیمی فکر می‌کند که کلود است. گاهی اوقات کیمی به شما می‌گوید که کلود است.
🔴
کیمی برخی از طرح‌های سلاح‌های ارتش آزادی‌بخش خلق را به آنتروپیک ارسال کرد. بنابراین فکر می‌کنم چیزهایی از این دست باعث شده که چینی‌ها متوجه شوند این یک فناوری بسیار قدرتمند است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150743" target="_blank">📅 16:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
تریتا پارسی: فقط چین است که می‌تواند جلوی جنگ سوم ترامپ با ایران را بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150742" target="_blank">📅 16:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e853be9f.mp4?token=Ls4mmDFjsdNKspFCk_hSaBxhl0mKUgeKboUYTSfj5w0rAUeHknjHZSD-Pn48yGEN7nlVd0iUUwZjC7L3rmC1r4-TXDpLkBcAHATMtuEKLidcZFRypKnOjZB14j7LrSj2U4QRXURxm6zZ52BiPqzTsrztUTi866_YuV8PT4XcdA3_Z_CavQZT9nxeqDxQvdZJOOG2fv2sAfmTN6Ok82OZtgriWXWfWtf53V6X8WQGCZQb9dlKVmOg-xWJJ-mIJhEjs0UjJyREifRYRRbXRez8wbS3tQG0KIEytDHSaTI1ANDUekio62uKJkquPw2_WboYwO6ttNNKxo5GsrxYKJnRig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e853be9f.mp4?token=Ls4mmDFjsdNKspFCk_hSaBxhl0mKUgeKboUYTSfj5w0rAUeHknjHZSD-Pn48yGEN7nlVd0iUUwZjC7L3rmC1r4-TXDpLkBcAHATMtuEKLidcZFRypKnOjZB14j7LrSj2U4QRXURxm6zZ52BiPqzTsrztUTi866_YuV8PT4XcdA3_Z_CavQZT9nxeqDxQvdZJOOG2fv2sAfmTN6Ok82OZtgriWXWfWtf53V6X8WQGCZQb9dlKVmOg-xWJJ-mIJhEjs0UjJyREifRYRRbXRez8wbS3tQG0KIEytDHSaTI1ANDUekio62uKJkquPw2_WboYwO6ttNNKxo5GsrxYKJnRig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری ایالات متحده:
فهمیدم که فاینانشال تایمز ضد آمریکایی و ضد کسب‌وکار است. آن‌ها تب دارند.
🔴
آن‌ها مدام سعی می‌کنند برای ایالات متحده مشکل ایجاد کنند. اما بیایید آن نشریه‌ی لجن‌گشته در لندن را کنار بگذاریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150741" target="_blank">📅 15:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نتایج اولیه کنکور ۱۴۰۵ اعلام شد!
🔗
my.sanjesh.org
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150740" target="_blank">📅 15:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9110f11b37.mp4?token=mEi0vboFZ16qwjb8SwEN_PLt-6ykZPxPCbosXJojVcumDCVrFIUdrXCPoZSBsphUIMeFdhv8mdPJKS-NvDKOrr98vbdpQ0o0UQJ427esA5aKvf2lH3ax8jrbLc-AKiRlWu4cFdInx1rq6mkFaYm0k5XvUfr1Z9GPpfgx86izGlrxiJnUVTKWsqr649vXUHydQXVQ7voSeHYlSv0NwGMeywG0WERzqSL3rWPyKUTenvFFAyhps0RisSgWpWg7NechfUuvBC823zaQB1n3vZSmedqGAk3FDM2QkFGElJMkH_B5esgIryZ2hMUPm2A2oi46O_Jf39umD2TZrPm17fhW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9110f11b37.mp4?token=mEi0vboFZ16qwjb8SwEN_PLt-6ykZPxPCbosXJojVcumDCVrFIUdrXCPoZSBsphUIMeFdhv8mdPJKS-NvDKOrr98vbdpQ0o0UQJ427esA5aKvf2lH3ax8jrbLc-AKiRlWu4cFdInx1rq6mkFaYm0k5XvUfr1Z9GPpfgx86izGlrxiJnUVTKWsqr649vXUHydQXVQ7voSeHYlSv0NwGMeywG0WERzqSL3rWPyKUTenvFFAyhps0RisSgWpWg7NechfUuvBC823zaQB1n3vZSmedqGAk3FDM2QkFGElJMkH_B5esgIryZ2hMUPm2A2oi46O_Jf39umD2TZrPm17fhW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت: ابتدا وارد درگیری نظامی مستقیم شدیم؛ نیروی دریایی و هوایی آنها را منهدم و توان پهپادی و موشکی‌شان را به‌شدت تضعیف کردیم و امکان بازسازی آن را از بین بردیم
🔴
سپس به «دیوار آهنین» و «محاصره» رسیدیم؛ اقدامی که پیش از این انجام نداده بودیم. حالا با «عملیات طرد اقتصادی»، آنها را به شکلی بی‌سابقه از نظر اقتصادی منزوی کرده‌ایم.
🔴
در حال حاضر، آمریکا حدود ۱.۱ میلیارد دلار و ایران صفر است. برای نخستین بار از آغاز صادرات نفت، این هفته هیچ نفتی برای فروش روی آب نخواهند داشت و درآمدی هم نخواهند داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/150739" target="_blank">📅 15:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOpx7qUzjFocSiiKi0X_XIozUhv7ykRZdbLMnaOgXP6WVG2v45Ac8YVCdYk5Wp7d0DPX4yYFEA3WGP3fUfub63JkayU6jVRmkHWP0dYs-FbckhOlsTjlKnxsf99BCCY1DiFMTJI4lJsHFxJFnUbOq1rjtVmHdRRRm8xeJM5MtoDUW-SEZyDMip9vA0LmBkWpX69oP482BkfqggzCA6ePTFazfmVqBNeyZc6Y5yXUh1X3DCkl6VjGW8xzbu3EQyKNdsq1Eo2mS2qEpxXBNCGOVrAgNUgqPgV2VreB8-szjKBtQ6wOa5ph8RfRY7ouRseQ-2iMXxmub035BT_aXOJEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای حجم آتش‌سوزی‌های رخ داده در پالایشگاه آرامکو در ریاض را نشان می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150738" target="_blank">📅 15:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXXhsHquhlGYssSSrmVNDL_xtcGJkMDMrgko8rNhmwmJ9Z2Z5ZyoLI4DbBBzA0JKMAVx6YuuohTYHYCgvXx-s9zZYDLvns_hWb5n2uAFfCM78BSxHsVo14bILZxXt-iJv7cL95MYK8yeNNBNVQa-h5hwW3yp_jatiod7YsKlq1oDZkZA4psgtPARWuTgrmiMJAHJqdrmzGRHbR2CkvNGpnwmpat_ZonyhZdvg_Xyi-aQon5l1ip_3nn3rRRnUUMSbAJ1i9RclQUaNRx_Szj4stL54AKENt4v37yMNEGBZZIkTsuEE3OdDK8ZKBDlPuqC9nQW9XMfMinRQfuY8gi5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فساد در سازمان بورس ~ قانون بازنشستگان رانتی شده ~ یعنی هیچ جایگزینی برای پیرمردها نیست؟  عبدالرضا داوری در توئیتر نوشت: آقای دکتر عارف! ‏
🔴
عده‌ای به‌طور غیرقانونی در پی انتصاب دوباره صیدی، مدیر بازنشسته، به ریاست سازمان بورس هستند.
🔴
سکوت نکنید و مانع تبدیل…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/150737" target="_blank">📅 15:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkF7WELJJOENjPa7Jh7ny9MLatRD1U0OkB9-U3KhA6cE1dtI24vuz4oZBOO0Om9kbsxreY3QSHy3Kwp1UcKQuHNHo_FutMtpZ1b3FbCek7HXuutJE4b042zQVe-UQz-s_9_kR1OG3FSFCHOBRtyWqdL98xbbJQtp8rLoF1EVgjHdzPSADTlSzQJPw7IBQvpzCplQtl6SlgTxub7W2bs2lJJgkkJs0pZOUQs3gY8ZmY5E3bW4DB8gxhaf_EPwbGfca9tzIR9rgdAktxoDLuaxy9iJjNUEex9hFvaDeeiS5ixUvlsZOdrlDALzMci96UH-w9t--V26TeRL7uIJbkJNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون ، حضور ۷ سوخت‌رسان آمریکایی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150736" target="_blank">📅 15:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150735">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گزارش ها وقوع چندین انفجار شدید در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150735" target="_blank">📅 15:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150733">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رویترز با استناد به گزارشی از نیویورک‌تایمز: مذاکرات میان روسیه و آمریکا اکنون شامل یک قرارداد نفتی چندمیلیارددلاری مرتبط با دونالد ترامپ است
🔴
بر اساس این گزارش، این قرارداد نفتی مجموعه گسترده‌ای از میادین نفتی، پالایشگاه‌ها و جایگاه‌های سوخت در سراسر جهان را که متعلق به شرکت لوک‌اویل است، دربرمی‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/150733" target="_blank">📅 15:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150732">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22b115038.mp4?token=KidAF5aGKCqm05n13keZNbVirPHt1nwf0Wp1_f-iextEA9IpRCHTzb0JOtSlkNpQ4m-J0xPN55JX7XjzpS7QUY1nA0BmlvQkh5fVUIwUfsAbpifXAizvMXtc-m8KSHw--UykeqoU6fDCCI4N6nL5_ST1Gv5uIKPm6-M0Z2cO6sGl0NFUi4FLG86290BOHibInrKtki8brbH3AvI021MCFD6JznL9bbN9HSEQDhQIkWofo6OhfyiuihgQkOXncEFe4LPYPL8LeT3pgFrLOOagygLNfXcCpoSZIKwwtu0uPDT0GbG04syky5_8RAMmS7wQmoM_bQt9UbCdZNrgvfsriA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22b115038.mp4?token=KidAF5aGKCqm05n13keZNbVirPHt1nwf0Wp1_f-iextEA9IpRCHTzb0JOtSlkNpQ4m-J0xPN55JX7XjzpS7QUY1nA0BmlvQkh5fVUIwUfsAbpifXAizvMXtc-m8KSHw--UykeqoU6fDCCI4N6nL5_ST1Gv5uIKPm6-M0Z2cO6sGl0NFUi4FLG86290BOHibInrKtki8brbH3AvI021MCFD6JznL9bbN9HSEQDhQIkWofo6OhfyiuihgQkOXncEFe4LPYPL8LeT3pgFrLOOagygLNfXcCpoSZIKwwtu0uPDT0GbG04syky5_8RAMmS7wQmoM_bQt9UbCdZNrgvfsriA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رگبار شدید باران خرم آباد دقایقی قبل
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/150732" target="_blank">📅 14:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150731">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki1Dz_lBMscf2J-wH5bPsGDLNhVdsg_NbZwO8PaxcKDpeyavwpeQbvV_QypSZZZH7pAaqO3YCeaksM_4Qy28CseH7MtJk6lIeS3v1TG4v3td5cABfdX75VGMGpUgpyZC449Od5VKxmGB4hVnbj4QfPm3--c-EJhjz5EfHJ2Q5gPam-x2qFAPwXhojjZFHkJ11vE0T8djQTbebGhF9dr0YdgC_fCe-mqTQXfoWwvrKwwnL8jjxyIv2v2ih3Nf6TAs9SvFgUicVNmfEZahEYILifkRe23DEqWsRBhjvQp-3tT99-aAbiEMVfC9QnhGcuOEMqawGO-A3H4uJ7mEwuPRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : من خوشحالم که اعلام کنم دولت من، از همین لحظه، شروع به ارسال "چک" به ارزش تقریباً 100 دلار به بیش از 20 میلیون نفر از سالمندان عزیز خواهد کرد تا به آنها در پرداخت حق بیمه بخش B برنامه "مدیکر" کمک شود، که ما قبلاً میزان آن را به طور قابل توجهی کاهش داده‌ایم.
🔴
این پول از "صندوق بهبود مدیکر" تامین خواهد شد، یک "صندوق بی‌فایده" که تنها توسط دموکرات‌ها در کنگره برای پرداخت هزینه‌های مربوط به فساد، تقلب و سوء استفاده برای دوستان خاص خودشان استفاده شده است و در نتیجه، هزینه‌های مراقبت‌های بهداشتی را افزایش داده است.
🔴
ما سرانجام از این صندوق، همراه با توافق‌های "منافع ویژه" من، برای کاهش قابل توجه هزینه‌ها برای سالمندانمان استفاده خواهیم کرد.
🔴
از آنجایی که من در این موضوع بسیار مهم برای مردم آمریکا به وعده خود عمل کردم، آنها همچنین می‌توانند اطمینان داشته باشند که "سود ترامپ" به مبلغ 5000 دلار، که بسیار محبوب است، به هر شهروند آمریکایی پرداخت خواهد شد، اگر و زمانی که جمهوری‌خواهان در انتخابات میان‌دوره‌ای پیروز شوند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150731" target="_blank">📅 14:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150730">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884f668d3f.mp4?token=NJiMXAnq5sAzXQwsn3lUeMn7YfcqrXk6n8WYJi2YarVAUn9No5eYoEzYXdSO7iDmCiV_E7Nn5weCSe0esqvKBMPvwebxoOHks-Itz58FxiBtZaMT0uDnlNZQlg2b0XlO0IRXj6sQtj5sK9HXThCutA8faVdVkIW2_5a2DIiZekASbLGDxPJ8Q8-39xVw9kSTVpV9HDFyYiA3dQ5smUM1kiHRkRFt7PkllHF6wFWw0Hsi3GPYzladRMnmOO7vEByYg_N-rfg5AsqubkaIrpk8huKb_P6Rv3jr4imP88cq9BRlP-O9RZotN2byFpHfQae9zgg1FDvl9u6j28_NzbkzQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884f668d3f.mp4?token=NJiMXAnq5sAzXQwsn3lUeMn7YfcqrXk6n8WYJi2YarVAUn9No5eYoEzYXdSO7iDmCiV_E7Nn5weCSe0esqvKBMPvwebxoOHks-Itz58FxiBtZaMT0uDnlNZQlg2b0XlO0IRXj6sQtj5sK9HXThCutA8faVdVkIW2_5a2DIiZekASbLGDxPJ8Q8-39xVw9kSTVpV9HDFyYiA3dQ5smUM1kiHRkRFt7PkllHF6wFWw0Hsi3GPYzladRMnmOO7vEByYg_N-rfg5AsqubkaIrpk8huKb_P6Rv3jr4imP88cq9BRlP-O9RZotN2byFpHfQae9zgg1FDvl9u6j28_NzbkzQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا باید صبورانه فشار اقتصادی علیه ایران را ادامه بدهد
🔴
مت پاتینگر، معاون مشاور امنیت ملی سابق ترامپ: ترامپ در نهایت به راهبردی رسیده که دقیقاً راهبرد درستی است: محاصره اقتصادی ایران؛ یعنی تا هر زمانی که لازم است به این فشار ادامه دهیم و هم‌زمان انتقال نفت از طریق تنگه هرمز را حفظ کنیم ... در کنار آن، باید مسیرهای جایگزین ایجاد کرد.
🔴
دقیقاً همین کاری که عربستان سعودی و امارات متحده عربی با احداث خطوط لوله جدید انجام می‌دهند. در نهایت، باید صبور باشیم ... امیدوارم این مسئله خیلی زود حل شود ... باید تا هر زمانی که لازم است به این فشار ادامه داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/150730" target="_blank">📅 14:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150729">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
اخبار تایید نشده حاکی از آن است که تأسیسات آرامکو در ریاض، عربستان سعودی، هدف حمله حوثی ها قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150729" target="_blank">📅 14:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150728">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت امور خارجه روسیه از دیپلمات‌ها و شهروندان خارجی خواسته است که شهر کی‌یف، پایتخت اوکراین، را ترک کنند و در آنجا نمانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/150728" target="_blank">📅 14:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150727">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">دلار هر ۵۰هزار که بالا میره یه خواننده میارن
رو ۱۵۰قیصر اوردن
رو۲۰۰ نامجو اوردن
رو ۲۵۰ بیژن اوردن
رو ۳۰۰ معین میاد
رو ۴۰۰ داریوش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150727" target="_blank">📅 14:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150726">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رئیس کمیسیون اجتماعی مجلس: احتمالاً ۵ الی ۱۰ میلیون تومان به حقوق کارمندان اضافه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150726" target="_blank">📅 14:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150725">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de51u0euKfXh5cVTbm411bWJXgNmOzWuQbm-kOohQxu-Y7VmdqRKXVfSqMDzH2JPIHyXK6BEUDCrkadWbhFt2QG7MWzRdHoE0HfbbTUksMnyqZNK2i7Xaz1NMk-4Ah6yX0HEaCP5HHcuPTjqBu9ZuW5GeTWYNQxl8XswWi2PwfoPxkByQOVHoJhg_Dm8KQ5GAC8OlyUBrAlCB7s3_GGv-STrZ_Ck_h_a1jFdy8o6dqrMsPB9JH8y3i89zZeprzLZyjfl0U_Eegk3Pzo-6f5heqZE2A1l5kzpChBiKRpt1RJ5zqqlSrKTQtBqPxz5RzfID3NzRjNc1vHsITu5fDQVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با حملات هوایی عربستان سعودی بر پایتخت یمن، صنعا، تعداد هواپیماهایی که از فرود آمدن در فرودگاه بین‌المللی ریاض خودداری می‌کنند، به ۶ فروند رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150725" target="_blank">📅 14:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150724">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKV_t-1cZiT5Fup2-lJhxjzi6AreZkihBxS5k0TY9Ff5xAPNFDnZUH2it1CnIWyXljFTf7rzv_IYGReaH-WTj7tNDCk8Beg3JJ2OAPi2J8n31cK0uZ5NDYG68lrqEfv3R00rf04hAptY8AXhp7L6Y3WPusFcxBODjp-FrjL5XNELmvCgeW6Ad-U5RHJ6q8WaTHJ8bgswbS1NqEDqYpsT0ndEpkqTA5YFEU9R3nOqTbB3cRd5fvVkMlJAVItcJ6oyBkz_bkhxTdwoJd9e4rzDJTnDLV_7WGqdsW5oCHxbf_7hsNkwevjLjtMOCvz_QYBbfSJvmGa0BORdDcUG5hwHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کره شمالی اعلام کرد که در آزمایش یک موشک راهبردی میان‌برد، از هوش مصنوعی استفاده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150724" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150723">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqE2femuDES0Ylkdh_Tetsuzv1v2R2ih_grZkYtnBhkKCm3cHcw3rZ3TEMOJ7OA5Hd2y2hVix4ZzvjqVL8xLkXeN_ntQienUyzvmKdMDziauzpIYoDx1ROUPcd83BBcdoLUBHSzxs2kZVUk19e5pgr7Gbbv2dVUSSu6J24wcbpfx50LM15aEO3H44zPusE1kCBXFGZ8E82f-0Zrgi3tY95iB7tQ9nDZJKY6q8qKyRmNP6esE7v38scntZvyl022LP5UghTMbiuAISfJm3KtiovNAcXxx0TFfgY5AiK-cfL-_FYQT9UMFPhpQ4uvC1pIfZO1rwOMpySD7izfq9LQ7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از هفته‌ای پر بارش در غرب کشور خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/150723" target="_blank">📅 14:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150722">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
تحلیل نیویورکر: چرا جنگ احتمالاً دوباره اوج خواهد گرفت؟
🔴
احتمالاً توافق اسلام‌آباد بهترین توافقی بود که ایران در مقایسه با هر توافقی در سال‌های گذشته روی میز داشت و شاید بهترین توافقی بود که در آینده نیز می‌توانست به دست بیاورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150722" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150721">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
اگه میخوای تو بازار دلار و طلا سرمایه گذاری کنی حتما اینجارو داشته باش تا ضرر نکنی
👇
https://t.me/+CEe6KOyxOHdiNTE8
https://t.me/+CEe6KOyxOHdiNTE8</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150721" target="_blank">📅 14:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150720">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
دو تا رعد و برق زد دلار ۵ تومن کشید بالا شد ۲۷۰ تومن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150720" target="_blank">📅 13:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150719">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
دو تا رعد و برق زد دلار ۵ تومن کشید بالا شد ۲۷۰ تومن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/150719" target="_blank">📅 13:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150718">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-APMu1WmJLIKF2bvyJNru7FTzHOyUPHNLzAdj5fvIzd92dYDPjkpXyFfQYDKMrC3MHaSS4zapg-X8FKFWTfOmALTTuG29lsnpnjsCvhoZmLZxb8RLGkmKby3PrZO8uxG-GgG0pY4_DvL-4b7G9eKQO16zgkqU7_SiJaiaZZzUncR_qq2m_zADZZjGsupHfoKIMq5Pw_F1HrBoV7A46TeDCpKhRC9hfkCF524yOBQWYoQbopFWKxKmNtmFecLJeyEufFq1vlmfxm3LgLTS7tiECMeY_kwFbAz02VUJXDYzj4stXXDFhF98VKiK98XOAMLDtHmwIMzUdMK7v42qdsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله نظامی عربستان سعودی، کوه عطان را در پایتخت یمن، صنعا، هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150718" target="_blank">📅 13:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150717">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
دلار از 268,000 تومان هم عبور کرد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150717" target="_blank">📅 13:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150716">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
هم اکنون ، آسمان برخی نقاط تهران شاهد وقوع رعدوبرق سنگین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150716" target="_blank">📅 13:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150715">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
صداوسیما: روحیه ساکنان منطقه تپه علی الطاهر همچنان بالاست و دارن ایستادگی میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150715" target="_blank">📅 13:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150714">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سردار نقدی: حمله مجدد آمریکا به معنای خودکشی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150714" target="_blank">📅 13:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150713">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcUwJv4jk5gC4nnuFgUV598GUzQmq-Zop8Eb-uo3lz6GXRMzjFzgebXbNaxg9AiQkEw19wB19HmEG95U2NyJ_pQzWOmwQnNjjn12FiVNTbOdD24PAUcdX2fltAazHaUn4aF4az1Z7F1znysFy97xbEN1u9Djh-Nztqbz0hT9GzM6tBSGrKsWY6dVt3R2blBWR-j2VFyZo1wttPaIgCXc5W9MCkbau9lXUtIU8ipLciECAWmRQ53xHWX4AA1ATFFIHv29H9V6kKMFIZ3c-LOiulFPYXZNM61oG4OOsGbCyBDsVrBmP511DRvbz-UrUp0BKw4huGdyS4rP5YXgSghdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طعنه فرزند پزشکیان به مجتبی خامنه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150713" target="_blank">📅 13:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150712">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJMY4jT5ekfgLX3IgeVhZ_wl5yYIW_-dOs6oHV7B0HgrTN9hvT-ipEh-uGD8DXRuJhzt2KLKgXJrpDqPyPG4pFPaD6xG6KeNabMJVyIiwxdAG3qz7P-T6entbrmLO-UG0OKV6xMAh_BIinVqpSKPmrCj6xOez1kVihn_gwpkqFZ5OFc_xV0rmxyurFRbocPfz_2e98rjLyEU9xhnVPSwUBpkUFCfsIydnsPdWplVfPMYiErmHlsI9Itw9VW5ifHG8NlRv4DpmyHE0t0a3qBkzuLHoYFBQokygLDYTqYH8c9bjOW2ld9hlPe9ZfFPy_vKlLIqZksyP_s9DNz6O-JM3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای حوثی به شهر عدینه در کوه حبشی، غرب شهر تعز، رسیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150712" target="_blank">📅 13:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150711">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
دیلی میل: بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره بریتانیا گفت: «فکر می‌کنم اگر بریتانیا کنترل مرزهای خود را دوباره به دست نیاورد، بریتانیا را از دست خواهید داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150711" target="_blank">📅 13:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150710">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fe16c54f.mp4?token=SfBUjZjlXa1FFwkjChbI8HunjlZC2EgCSLkoeTkyUZAEhk_gnrqMu3bVrb0BtdrH9wWMcf6w05LUhINULchIfYQi-F2ueWI6KYfU-Ob-Qqf4zmoX8CjXFwIcJheisqCpKVVcFsXhbZgJqMAbLdRWVjwQ3BFOv8sr7Y0V327YaQ86p1B2YtTPaNKK003DDAdAPRifmHrm-OCK3ePih4JfPSsb7kxCaUrI3IwVt_MHmFoGmxoHG_sH3ymm78epO1-0AsEfPulow2Pj9JU-aiAVDvYdc5V56ZDGRcxsUREdVycz3H0wA1AlyqRYwz0ZxpdU2vqFr1CBCItOzZbkLJxqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fe16c54f.mp4?token=SfBUjZjlXa1FFwkjChbI8HunjlZC2EgCSLkoeTkyUZAEhk_gnrqMu3bVrb0BtdrH9wWMcf6w05LUhINULchIfYQi-F2ueWI6KYfU-Ob-Qqf4zmoX8CjXFwIcJheisqCpKVVcFsXhbZgJqMAbLdRWVjwQ3BFOv8sr7Y0V327YaQ86p1B2YtTPaNKK003DDAdAPRifmHrm-OCK3ePih4JfPSsb7kxCaUrI3IwVt_MHmFoGmxoHG_sH3ymm78epO1-0AsEfPulow2Pj9JU-aiAVDvYdc5V56ZDGRcxsUREdVycz3H0wA1AlyqRYwz0ZxpdU2vqFr1CBCItOzZbkLJxqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل: «اسلام‌گرایان و چپ‌گرایان باید به‌طور طبیعی در مقابل یکدیگر قرار داشته باشند.
🔴
اسلام‌گرایان همجنس‌گرایان را اعدام می‌کنند و زنان را از هرگونه حقوقی محروم می‌کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150710" target="_blank">📅 13:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150709">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
👈
تیراندازی در مقابل دادگستری مهاباد  ‏
🔴
خبرگزاری صدا و سیما: دقایقی پیش حادثه تیراندازی در مقابل ساختمان دادگستری شهرستان مهاباد رخ داد؛ حادثه‌ای که در پی بروز مشاجره لفظی میان چند زن، با ورود مردی مسلح به سلاح کمری و شلیک گلوله همراه شد  ‏
🔴
در جریان این…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150709" target="_blank">📅 12:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150707">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfbcca65f4.mp4?token=MIukON0qcDqToVi4YeUs95a25ebd31mCm4YJDXfxjx4__-zbwluVQLsJVqSCUjfdr0K_cAD4E-ugVkMmLPZgEdVwIKUayjLIcKHhCnthOzOQfOBWaUJxiHnSQdnSHJ7TH1B0EUQX7OPOCC63ChPsj6MTPwUSpx8-7HjSbWv1UmZs7WGG4rC1JNnIpawiVjZ3zBuNueX26OdyDERQJwxURU3uH9EG3Jmda4qfPmEhfll-JBeHkprL5TKV0t-nVug-z1E4Lq47i-ZoSMedbUYqHNDkRA1ST7QxroYSIFVQdGs1B7LVvbSQThaTfW7T14LxJchFMvz3rn3MVIdA7cktCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfbcca65f4.mp4?token=MIukON0qcDqToVi4YeUs95a25ebd31mCm4YJDXfxjx4__-zbwluVQLsJVqSCUjfdr0K_cAD4E-ugVkMmLPZgEdVwIKUayjLIcKHhCnthOzOQfOBWaUJxiHnSQdnSHJ7TH1B0EUQX7OPOCC63ChPsj6MTPwUSpx8-7HjSbWv1UmZs7WGG4rC1JNnIpawiVjZ3zBuNueX26OdyDERQJwxURU3uH9EG3Jmda4qfPmEhfll-JBeHkprL5TKV0t-nVug-z1E4Lq47i-ZoSMedbUYqHNDkRA1ST7QxroYSIFVQdGs1B7LVvbSQThaTfW7T14LxJchFMvz3rn3MVIdA7cktCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی‌ها در شرکت نفتی آرامکو
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150707" target="_blank">📅 12:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150706">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">روی دلار ۲۳۴ هزار گفتم بخرید میتونه تا ۲۹۰ هزار بره و فک نمیکردم اینقد سریع تو دو هفته اینکارو بکنه تا ۲۹۰ هزار فعلا هیچی سرراهش نیست و میتونه بره  روزی داره ۵ هزار گرون میشه  اپدیتشو میذارم براتون امروز
❤️
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150706" target="_blank">📅 12:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150705">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
استاندار تهران: در جریان جنگ اخیر، حدود ۴۵ درصد عملیات‌های اسرائیل و آمریکا متوجه استان تهران بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150705" target="_blank">📅 12:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150704">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دیشب در کمپ دیوید، ترامپ و کابینش جلسه محرمانه‌ای داشتن و آکسیوس گزارش میده که دست‌کم تصمیماتی گرفته شده.
🔴
موضوع مورد بحث این جلسه، ایران و یمن بوده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150704" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150703">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghAS8dtMdPd8RgL2-zudq31NIUa1Suisb8c0ac3BvZX3VrmMc00Z1Ej-eNinCnby5rpVXC2fQzIRiwIfZEpWU0apzxDxg6pNH7eZ9DBkhqxzMaXlzxBtMYtp2RQsfHu-ilI4EzdOMkd6WuBS9_3Mycuf8w7ZRxID6mIuz8-Avkv5UXN5SJ6WEwiN93d7e3yjnrVej0sXS4e7ucW-Oq-6r0O-ZOt2geTZVA8jdoK0tgqWESyhbciASeK5cHuO-_I6BDirqsvIFr8-67nPKDvAAV3_0T7zu6v16e1yZaDHXMjNXVvJcGPnPZEsKHWKINirJIu94KjNwJaRfdCzsGDC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از پارک جنگلی چیتگر در سال ۱۳۷۸ و ۱۴۰۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150703" target="_blank">📅 12:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150702">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffde0cb90c.mp4?token=nTgJUIRUMFkQT7MHBeiFV_Qn8X_EK12OeOfZb9gtUM5sOHnrULbFNyHJy2Pe1LVhxib852Smig7b5vnH2-leWtS7PQJmLQ6cv1E_EZfhk4dEiMvc_cb5TNF662C3nSFLMFHOuZucoWshUI7kwhVmeizLunhI637kKFA4UClVnYxpZYk_zwf5C7Ip4q6DDGYhr0wxT3WmSo9wNHLYUF1NJzlveliYPx1-AzXv0sbwlqTkpiQ30mUDM1cgq6dKFV7lBrCYP4T8V0gJd952Lmqo9CFETVUG24Oselg8wwbm9Srf5D_VxQzD6R4Cq2YG8BQnd9PEJdaY-Ut8Yt6_8CGu5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffde0cb90c.mp4?token=nTgJUIRUMFkQT7MHBeiFV_Qn8X_EK12OeOfZb9gtUM5sOHnrULbFNyHJy2Pe1LVhxib852Smig7b5vnH2-leWtS7PQJmLQ6cv1E_EZfhk4dEiMvc_cb5TNF662C3nSFLMFHOuZucoWshUI7kwhVmeizLunhI637kKFA4UClVnYxpZYk_zwf5C7Ip4q6DDGYhr0wxT3WmSo9wNHLYUF1NJzlveliYPx1-AzXv0sbwlqTkpiQ30mUDM1cgq6dKFV7lBrCYP4T8V0gJd952Lmqo9CFETVUG24Oselg8wwbm9Srf5D_VxQzD6R4Cq2YG8BQnd9PEJdaY-Ut8Yt6_8CGu5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ریاض عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150702" target="_blank">📅 12:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150698">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4829d2be.mp4?token=OwMIj58kUwRQzHGtyIBMtO1QrpiK7VOkxkjBBQUb9SW3CmPh8f5wQ5fUR-5oQfj8V5ELxZNqArd0Pc5JEso87R3cfimNL3x5k1kbGvyADJ8nAPMrFJC3oJv-cDvGD97f3djj6jvxntF1su3Swse4ENOXK-ItUrgOxTAmQ7xV_NKJrOFuE-1rcslpEzn9-wZcPrTkgYSoPZmqzjFqESQgNW1FlAnCYN-2m4vUsefk3UMTcJur2gLzjFWOCrDzniE9gjXrHW4iaqkt-nev_9o9mfHgDamwjIvbfOYSox_uHcL9iGM7HBjhPTDhqlStXhtKNqO5UdBFXrXWIwe1fcTO2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4829d2be.mp4?token=OwMIj58kUwRQzHGtyIBMtO1QrpiK7VOkxkjBBQUb9SW3CmPh8f5wQ5fUR-5oQfj8V5ELxZNqArd0Pc5JEso87R3cfimNL3x5k1kbGvyADJ8nAPMrFJC3oJv-cDvGD97f3djj6jvxntF1su3Swse4ENOXK-ItUrgOxTAmQ7xV_NKJrOFuE-1rcslpEzn9-wZcPrTkgYSoPZmqzjFqESQgNW1FlAnCYN-2m4vUsefk3UMTcJur2gLzjFWOCrDzniE9gjXrHW4iaqkt-nev_9o9mfHgDamwjIvbfOYSox_uHcL9iGM7HBjhPTDhqlStXhtKNqO5UdBFXrXWIwe1fcTO2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات دانش‌آموزان در فرانسه:
🔴
۶۲۵ نفر بازداشت شده‌اند
🔴
۸۳ مأمور پلیس مورد حمله قرار گرفته‌اند
🔴
۳۲ معلم زخمی شده‌اند
🔴
صدها مدرسه به آتش کشیده شده‌اند
🔴
خودروها و کلیساها به آتش کشیده شده‌اند
🔴
دانشجویان آفریقای شمالی‌تبار و دانشجویان چپ افراطی علیه دولت فرانسه اعلام جنگ کرده‌اند
🔴
تا کنون کسی کشته نشده !
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/150698" target="_blank">📅 12:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150697">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is_8_78D1uhTbY7T8_kJak3jy0MV9mhTju19IWaEVdl4ijMuxjTf9KvoKQPH2a5QxkIS1DlncNkMSmw107TqrY7-PmKOUyNYAyulULS7xdibJUCKp_qi6M31Z8kYHFcABu0OC5_4Eirw0Bt_pT-vF31FuHh3kLOszDMOudhT1MtsSF_Mkg6wmR_axIrjEumOTcQIZ4o1wzNOBj38jyHLPJh_ZkdiB_NZYXoOEscz8jjo6mTg0xZp0Ndng4D5WOlDPr0WKlE0zLzHR_tkqn5TpLfymqlUMwn8obJgEg6ifVvSvlP-CmQ96NCgrQb9e-OFP8oVEcwNlbyZg51N_0adtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکم شهریور 1405 همین ۴۰ روز پیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150697" target="_blank">📅 12:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150696">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
هر  یک دلار 267,200 تومان شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150696" target="_blank">📅 12:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150695">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFQUtOXOoD2jK_QfeIN4kChtvbqbvvdZdYpE0O2YWBly8FsH7xFWP2rcgVan-8M4yvNnBKO1uDQN_7Frp-euoIgcXiaY-YUEUfUk3-GhuIYlld1baY9MrQ8ZphMxlULKIpSKoQM2H9-psOoZbITjaXblUS--UQ_WIUfn3zthSGKAbWoD4Q2EFUP2TyrFVwcnZ9N4u3JCnT3n91TJmam_mURR23QWpWSiA14sZuxDXtkJh3rJohtb02JJviEyr1j_Bwni3MJ3J1wPNs_MeglMm0VXARpYtTQAc0yySwwCQekZ4D6ykuX5M-Hb6PPmbxZ50PvDAahg0Jvwp-C2h73_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری وایرال شده از رژه جان فداها در اصفهان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150695" target="_blank">📅 12:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150694">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
تعویق رأی‌گیری سنا درباره توافق هسته‌ای ترامپ و عربستان
🔴
سناتورهای آمریکایی اعلام کردند رأی‌گیری درباره توافق‌نامه همکاری هسته‌ای غیرنظامی دولت دونالد ترامپ با عربستان سعودی، پس از برگزاری انتخابات میان‌دوره‌ای و حداکثر تا ۱۳ دسامبر انجام خواهد شد.
🔴
این تصمیم در پی ابراز نگرانی برخی نمایندگان- به‌ویژه دموکرات‌ها- درباره خطرات اشاعه سلاح‌های هسته‌ای و احتمال شکل‌گیری مسابقه تسلیحاتی در خاورمیانه اتخاذ شده است.
🔴
این رأی‌گیری به کنگره اجازه می‌دهد تا پیامدهای انتقال فناوری‌های هسته‌ای آمریکا به عربستان را بررسی کرده و موضع رسمی خود را اعلام کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150694" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150693">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
👈
تیراندازی در مقابل دادگستری مهاباد
‏
🔴
خبرگزاری صدا و سیما: دقایقی پیش حادثه تیراندازی در مقابل ساختمان دادگستری شهرستان مهاباد رخ داد؛ حادثه‌ای که در پی بروز مشاجره لفظی میان چند زن، با ورود مردی مسلح به سلاح کمری و شلیک گلوله همراه شد
‏
🔴
در جریان این درگیری لفظی، مردی که یک قبضه سلاح کمری در دست داشت، به سمت زنان نزدیک شد و اقدام به تیراندازی کرد. جزئیات دقیق چگونگی وقوع حادثه و ابعاد آن تاکنون مشخص نشده است
‏
🔴
اطلاعاتی درباره شمار مصدومان یا تلفات احتمالی، وضعیت جسمانی افراد حاضر در صحنه و همچنین هویت فرد تیرانداز منتشر نشده است. همچنین علت اصلی مشاجره و انگیزه احتمالی تیراندازی همچنان در هاله‌ای از ابهام قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150693" target="_blank">📅 11:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150692">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b5ad2c555e.mp4?token=NLWQh-sRnt2VPvQRvCmyn3tglH4ewJP53J4wP4LnuqvGEfwBMuZT5NJ5bwazUqw9t85aIQ9A2WV1eEm19-m0oxCOj9cFBibovaPAiXZeNqgnUbG2TwjW5BwOhiIHF_o5o9H717tdnarCuZZmdop6-rzwZGxwZdwi5Tguf0N8lprzb24uRRgxX-vV5WRUbB2WdV2CSUpekU5DogewBunLcSH0xM2N9PplNnnf4-EtcplhpAMij64rb0AfggWIF0NcQqZM2YxuWCo7Shk7M1apOZ-0-pq9DZ29UtGXLE0ONQRY-DYMQrblPbvcvTFaOAe1adeEPyl13DP6WvvHVdoBTiNeBbHmZNXdUnK8ywIozhKEFGbtGu4HdXqlOEABQJPy_aCZ5bkpbFynN2OstGcF1WJmBLeB-DYE4yWtE_vkOyTU22eua4Q0EQvdpHNp2cFdOMeo_r6eX54OuFvpo1YBlzgRrOxCJ32GgWabALPj0oONGa7zBIVDuQPrec3Z9mDpEJJx24-txmyU-hYLRI0uE9oA6q2YN0kVWpw3yansZiaQSljTpkTbbmLSdES6-YlWYPC50llPNXzrBIg-g5leyPWpZCLb08znbIFTgXH3j04AKQYwyC8u1cC3dQsenduXifx3jXZBnDSJkN-S4n3TRi69hCaOqZo-1BbIFJrEAZM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b5ad2c555e.mp4?token=NLWQh-sRnt2VPvQRvCmyn3tglH4ewJP53J4wP4LnuqvGEfwBMuZT5NJ5bwazUqw9t85aIQ9A2WV1eEm19-m0oxCOj9cFBibovaPAiXZeNqgnUbG2TwjW5BwOhiIHF_o5o9H717tdnarCuZZmdop6-rzwZGxwZdwi5Tguf0N8lprzb24uRRgxX-vV5WRUbB2WdV2CSUpekU5DogewBunLcSH0xM2N9PplNnnf4-EtcplhpAMij64rb0AfggWIF0NcQqZM2YxuWCo7Shk7M1apOZ-0-pq9DZ29UtGXLE0ONQRY-DYMQrblPbvcvTFaOAe1adeEPyl13DP6WvvHVdoBTiNeBbHmZNXdUnK8ywIozhKEFGbtGu4HdXqlOEABQJPy_aCZ5bkpbFynN2OstGcF1WJmBLeB-DYE4yWtE_vkOyTU22eua4Q0EQvdpHNp2cFdOMeo_r6eX54OuFvpo1YBlzgRrOxCJ32GgWabALPj0oONGa7zBIVDuQPrec3Z9mDpEJJx24-txmyU-hYLRI0uE9oA6q2YN0kVWpw3yansZiaQSljTpkTbbmLSdES6-YlWYPC50llPNXzrBIg-g5leyPWpZCLb08znbIFTgXH3j04AKQYwyC8u1cC3dQsenduXifx3jXZBnDSJkN-S4n3TRi69hCaOqZo-1BbIFJrEAZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، می‌گوید قیمت بالای نفت هزینه کوچکی در ازای هسته‌ای‌زدایی ایران است
🔴
«۴۰ درصد. اما درباره نفت یادتان باشد، شما دارید هزینه‌ای می‌پردازید، اما این هزینه بسیار ناچیزی در مقایسه با چیزی است که اگر این افراد به یک سلاح هسته‌ای دست پیدا می‌کردند و از آن علیه موبیل، آلاباما استفاده می‌کردند، باید می‌پرداختید.
🔴
خب، چنین چیزی اتفاق نخواهد افتاد. و ما حمایت فوق‌العاده‌ای داشته‌ایم؛ واقعاً حمایت بسیار خوبی داشته‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150692" target="_blank">📅 11:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150691">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رئیس سازمان سنجش : نتایج کارشناسی ارشد اواخر مهر اعلام می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150691" target="_blank">📅 11:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150690">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3de2fd69.mp4?token=ZVtQ_cp4_OR2AsB0Uovm-r1yK9JC_4gmljmKH3SyGdbiir_dWDtGdxEEw1DRwalpyXuc6EGBzW5bZT1Qw3zbToT0vRxOxNnJkc5HlKAyX3Q7b5PpknXe4eBYn2LYh7_UB1dYgXfEvZE7p0SGPjclA1FbKxJ1WuqKmxO_76eeSqf0WntSNMbm_hH09sQVW7fGUm30af1NIzy8avxFK8s66tszEjXP_ogB4VIbqQrBns6hPhT3k3WD75mDHcrAOnD3p2fCxcR7kRYkJR622zn7n8rlxRXWhqO_5zSdCneCzdiu2tKrm-g9jCLlKoBmWJYDEwRzgJBURmWHPbY4JNMAXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3de2fd69.mp4?token=ZVtQ_cp4_OR2AsB0Uovm-r1yK9JC_4gmljmKH3SyGdbiir_dWDtGdxEEw1DRwalpyXuc6EGBzW5bZT1Qw3zbToT0vRxOxNnJkc5HlKAyX3Q7b5PpknXe4eBYn2LYh7_UB1dYgXfEvZE7p0SGPjclA1FbKxJ1WuqKmxO_76eeSqf0WntSNMbm_hH09sQVW7fGUm30af1NIzy8avxFK8s66tszEjXP_ogB4VIbqQrBns6hPhT3k3WD75mDHcrAOnD3p2fCxcR7kRYkJR622zn7n8rlxRXWhqO_5zSdCneCzdiu2tKrm-g9jCLlKoBmWJYDEwRzgJBURmWHPbY4JNMAXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر جدید از تداوم آتش سوزی در پالایشگاه آرامکوی ریاض درپی هدف قرار گرفتن با موشک‌های یمنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150690" target="_blank">📅 11:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150689">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مجری صدا سیما: اگه به رهنمودهای آیت الله العظمی امام حاج سید مجتبی خامنه‌ای دامه برکاته گوش بدیم مشکلات حل میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150689" target="_blank">📅 11:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
هم اکنون ،شلیک چندین موشک از صنعا،یمن
✅
@AloNewd</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150688" target="_blank">📅 11:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
دادستان کل امارات: کمک خلبان پرواز فلای دبی قصد انجام اقدام تروریستی را داشت
🔴
دادستان کل امارات: تحقیقات پیرامون حادثه پرواز فلای ‌دبی نشان داد که کمک ‌خلبان قصد انجام یک عملیات تروریستی را داشته است.
🔴
طبق نتیجه تحقیقات کمک‌ خلبان هواپیمای فلای ‌دبی در حین پرواز شروع به اجرای نقشه خود کرد و با استفاده از تبر اضطراری به خلبان در داخل کابین حمله کرد. تحقیقات برای روشن شدن تمامی ابعاد و جزئیات حادثه فلای ‌دبی ادامه دارد.
🔴
پیش از این مقامات ارشد اطلاعاتی و انتظامی اعلام کردند کمک‌خلبان هواپیمای فلای‌دبی که متهم است روز چهارشنبه به کاپیتان حمله کرده و قصد داشته پروازی به مقصد اسرائیل را ساقط کند، تبعه عمان است؛ فردی که پیش‌تر به دلیل شناسایی به عنوان یک تهدید امنیتی، از سوی شرکت «عمان‌ایر» از پرواز تعلیق شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150687" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
