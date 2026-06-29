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
<img src="https://cdn4.telesco.pe/file/ScsA2RLzqkdg0Ukbwbc2p5wktukSj2G_Hu--yP4s7hqCFXmyXXZgujRqG1rw6CIJ73SmC6Ci2vT8Eofx7d1BC1ialLvY1xpIpPI_AxczicRtXn1nXEvBiVW3HBkammJx8uN89kLrOIEPOP-bSyk8CJjn3b29AF7BWaWxbAyI0Z15yajaISBkq1SoGXbynhEmhgAHZIUBqyUfgDpYqYBHfP2tBEm6cYukX9IEgo3fgpqHGZv_DqDgOg6j8h2XD2BHkQ1VPqfj99zKeDspC50YoS61Z6Rn55xj00mjIJcjsg_G10jg7EjmYsCwNkeMR_T4L3BcJYAcrYegHSvmHiJ_KA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 13:34:21</div>
<hr>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حجم : نامحدود
زمان : تا ۱۲ شب
vless://63b43d54-3bdc-4d9e-b3f3-10163c892936@64.90.7.102:8443?type=ws&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
وصل شدید بگید</div>
<div class="tg-footer">👁️ 600 · <a href="https://t.me/ArchiveTell/6620" target="_blank">📅 12:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xlwi-QuKmi4pCI_lVnmeLaGH4r9MjUMH6_GHzE4KXPzfGQ9s8ItdYWdqU2EzGstK1fGWFUMkVgc2-8zrXQ9zRFYffmpcDCNS5Jo1LjnL9TGHqvwJaBkoC0syb7p7BZTcN6hEeHmqzO5Oz0ZYZj-j8JlnPij7CgiJeZqHLH_B0tWp7AHvOK0IEjSodUS_jp32VvjfXB7H6UWJhiqo4BAk77tfWtTd0VoaVvL3TgP3xMFTmwHTf8WNhVN5YgfERgvgv_FwGInx1Ex-wvGXGh0AaiFoyStoY6TUeXYpbMF5JcvujGmSVuoKBeK7S6xr88fbGjCsWfrKeB7eUgW_DNAqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راه جامع علوم کامپیوتر: ۸۰۰+ منبع از دانشگاه‌های برتر جهان
🎓
اگر می‌خواهی به یک توسعه‌دهنده حرفه‌ای تبدیل شوی، این مخزن گنجینه‌ای از دوره‌های دانشگاه‌های هاروارد، استنفورد، MIT و شیکاگو است.
✨
چرا این لیست؟
•
🏛
منابع معتبر:
دسترسی به دوره‌های دانشگاه‌های تاپ جهان.
•
🤖
پوشش کامل:
از الگوریتم‌ها و زبان‌های برنامه‌نویسی تا هوش مصنوعی و رباتیک.
•
📚
دسته‌بندی هوشمند:
گم نمی‌شوی؛ دقیقاً همان چیزی را که نیاز داری پیدا می‌کنی.
•
🔄
همیشه به‌روز:
نویسندگان مخزن را مداوم آپدیت می‌کنند.
مسیر یادگیری‌ات را از اینجا شروع کن!
👇
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/ArchiveTell/6619" target="_blank">📅 11:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAqKjKHKW_7uX7tLWBE82cwt3W8wcsPtrMLhI4xp4OQVz8GG6nmpWf2ZfxpbHQoIfMcLg6_pGQLKe9E8qczgnGw3kveZfL7_VOUHJSr2Rkhe29ewv6IvVnHwV5pRf4uj2Y5tqP7YUnuDcmZ7hoWW180RNEtNDClcigHrroVDoxAtJ5RQlEzjLMhI6NkzXpBpVDRo94s-Jkd8VUYaZGiQrAY4u2_4Cc6j3LIWAEFpRJ7sTg6iRA1ZIp9JW3B-MUSQa9PKwNYfoTQNZ45j86u3KWMp9YoaxmCledU6H053Veto_EAaHC6JNs99CcMqIsbE7IG8fEjWoNm1TTJ5WUH8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Anthropic بسیاری از دوره‌های هوش مصنوعی خود را رایگان کرده است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/6618" target="_blank">📅 09:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1Z3MdUJEzOl8LK_dgoUdAjz5Nn3tvSLWRFRwa5gLKAEKB3ZPenJv5XP0ATekEgKOo_w42ouXgvBI8-7JzmKyeL5jWzxL2gTCoYENOUCoOlNctTy9In_WcuHfukFPq-V1pn87TvPkP53asD1hbgbxhw7nlxzhErknv4z-fPKPKYmnnqGmh3Qlaehvfk-seYYc00WYohKo1vhJI2_zm7T-r8prrYHP6HgetxIZbMhemenZBOXas5egZFCs0AZmOIa7dPieIs6bH4vNzSMW1I7VPrHLvceA1Ln76lS2LoeH-sBEPE9TXVWckKe3OuHdPsoKsQUlRMLjv75LTz4vWRQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">OmniRoute
۱۶۰+ هوش مصنوعی رایگان در یک API!
🤯
دیگر نگران تمام شدن توکن‌ها نباشید. OmniRoute با ارائه
توکن‌های نامحدود رایگان
، تمام مدل‌های برتر جهان را در یک نقطه جمع کرده است.
✨
چرا OmniRoute؟
•
🔄
تغییر خودکار مدل:
اگر توکن یک مدل تمام شد، بلافاصله به مدل بعدی سوئیچ می‌کند.
•
📉
فشرده‌سازی هوشمند:
تا ۹۵٪ کاهش حجم متن برای صرفه‌جویی بیشتر.
•
🌐
دسترسی جامع:
GLM، Grok، Mistral، DeepSeek، Qwen و... همه در دسترس.
•
🛠
پشتیبانی کامل:
سازگار با MCP و مهارت‌های پیشرفته.
یک API، تمام هوش‌های مصنوعی دنیا. رایگان و بی‌نهایت!
🚀
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/6617" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">10 میلیون توکن رایگان هوش مصنوعی Mercury 2
🎁
وقتشه ربات تلگرامیت رو با هوش مصنوعی ارتقا بدی!
✨
✅
مناسب برای ساخت چت‌ بات
✅
دسترسی فوری و رایگان
⚡️
همین الان فعال کن:
🔗
platform.inceptionlabs.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/6616" target="_blank">📅 02:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=opvYj1AMM2te8rc5bBMO2VMT7ANuedQEDL9X7x7zjk8D3I0_-J2TILfGNdoSAECDXucH6w9etyri-_k7XtZpy_h_IKkBxuqi9iyiCp8TrJ95xtdqJjhQiDWuxeJGSmZpNEDzPPZdpmaHVsDHDnrIhB7Up2NLxw-o9mmdyDiZIKaZTLfTT35aHX6BIqLK0ZVUWiLdbPa_olwr81ZXbUGqa8wmydplGjyXrpq5h2514VmbkJ2L1TZhRbOy2MQPafBveItI0_xpZ9oz11v7y73PzlXBl37mAPFoJG3_8UjpoIRNuSiFuPWUzrkodc_h2WhgTadn85YUfhv4ZWmg_GHVwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=opvYj1AMM2te8rc5bBMO2VMT7ANuedQEDL9X7x7zjk8D3I0_-J2TILfGNdoSAECDXucH6w9etyri-_k7XtZpy_h_IKkBxuqi9iyiCp8TrJ95xtdqJjhQiDWuxeJGSmZpNEDzPPZdpmaHVsDHDnrIhB7Up2NLxw-o9mmdyDiZIKaZTLfTT35aHX6BIqLK0ZVUWiLdbPa_olwr81ZXbUGqa8wmydplGjyXrpq5h2514VmbkJ2L1TZhRbOy2MQPafBveItI0_xpZ9oz11v7y73PzlXBl37mAPFoJG3_8UjpoIRNuSiFuPWUzrkodc_h2WhgTadn85YUfhv4ZWmg_GHVwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده…</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6615" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده و متن‌باز
PokieTicker
دقیقاً برای شما ساخته شده است!
🔥
این ابزار چگونه کار می‌کند و چه امکاناتی دارد؟
1️⃣
تلفیق اخبار و نمودار:
نقاطی روی نمودار کندل‌استیک ظاهر می‌شوند که نشان‌دهنده اخبار منتشر شده در آن روز هستند. با کلیک روی هر نقطه، متوجه می‌شوید چه خبری باعث آن نوسان شده است.
2️⃣
فیلتر هوشمند اخبار:
دسته‌بندی اخبار بر اساس تأثیرات مختلف (گزارش درآمد، تغییرات مدیریتی، محصولات جدید، سیاست‌گذاری و...).
3️⃣
تحلیل و پیش‌بینی با هوش مصنوعی:
با استفاده از مدل‌های قدرتمند
XGBoost
و
Claude
، سنتیمنت (احساسات) اخبار را تحلیل کرده و روند قیمتی سهم را برای روزهای آینده (T+1, T+3, T+5) پیش‌بینی می‌کند!
4️⃣
کشف الگوهای مشابه:
روزهای گذشته که اخبار و شرایط مشابهی داشتند را پیدا می‌کند تا ببینید در آن زمان بازار چه واکنشی نشان داده بود.
5️⃣
رایگان و آماده استفاده:
دیتابیس لوکال (SQLite) از قبل در مخزن گیت‌هاب قرار دارد و برای اجرای اولیه نیازی به خرید API کلیدهای پولی ندارید.
﻿
⚡️
مشخصات فنی:
*
بک‌اند:
Python (FastAPI) + SQLite
*
فرانت‌اند:
React + TypeScript + D3.js
*
مدل‌های AI/ML مورد استفاده:
XGBoost, Claude Haiku / Sonnet
﻿
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6614" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6613">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=V1Tu9wJNVIZSNPzx6rGIrmEhWwZwdcNhKY6B0y2O6rV9rm0DOz4ZkvBva2-GgQMBwo9YSAMHuMBZ_HfmRxv6xduwccw3TdxOaOyZFmaB0U7lfGRsY887IiFXSMumqBms4b8Sf62AtCdBPjZoQ8YwtfObCp02Yxnt4X8glrMTKhOhbWq8a35d6AjcPHEilgGhsI6PTFwEB0387brCMYLIjt2jLkIfAUHXTsyFdZPGMXDVc9Qxooj7Xrkb7ma5Pfr2Fw5rQ4FsY9Il5b4VUzaBzD2IN_Rx8fxKuyGdKpP88ihwcwWa8p8QO9754AIP0zmTlwJPK7c9GmIDlptw-oR_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=V1Tu9wJNVIZSNPzx6rGIrmEhWwZwdcNhKY6B0y2O6rV9rm0DOz4ZkvBva2-GgQMBwo9YSAMHuMBZ_HfmRxv6xduwccw3TdxOaOyZFmaB0U7lfGRsY887IiFXSMumqBms4b8Sf62AtCdBPjZoQ8YwtfObCp02Yxnt4X8glrMTKhOhbWq8a35d6AjcPHEilgGhsI6PTFwEB0387brCMYLIjt2jLkIfAUHXTsyFdZPGMXDVc9Qxooj7Xrkb7ma5Pfr2Fw5rQ4FsY9Il5b4VUzaBzD2IN_Rx8fxKuyGdKpP88ihwcwWa8p8QO9754AIP0zmTlwJPK7c9GmIDlptw-oR_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DewatermarkAI
حذف واترمارک با هوش مصنوعی در مرورگر
این سرویس رایگان واترمارک‌ها را از عکس‌ها حذف می‌کند و فایل آماده را می‌توان با وضوح اصلی دانلود کرد.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6613" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1cbx2GJfTUIqgy_vmwaJD5C2-GSZnAabuFB26SWwdzFm5RIZBA_aSTfV0bkQKyiffydq_UNwXNxH_NYS-rTT96lWmM0z7MfNLmGI2pgfg37vyeA6XC3wRuLEdChlLEU9j1-wBb3B6x-XI5mfDJQ9Ovh-TSv0R_4IRm50bZkHp7yZs-a89CpFfC889H8gxRatyrW8Xs-vyOwuLaWGUaWr0mja4rHQ4D0UlZb5p8QyuTa3Fd2HvfDhU1NWFFr9fK8T29A_4wbB0DTFa5c4MdlbUjQoQz6KoLzjwDFGvHSS5PHNaKdeWvC7PwbgduQN3gieBqpP4nFHkMJcByO9V9YJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از به‌هم‌ریختگی اسکرین‌شات‌ها خسته شده‌اید؟ Trickle دستیار جدید هوش مصنوعی است که همه اسکرین‌شات‌های شما را به‌طور منظم سازماندهی و خلاصه می‌کند
فقط یک اسکرین‌شات بگیرید و آن را به Trickle ارسال کنید. هوش مصنوعی پیشرفته Trickle یک خلاصه دقیق تولید می‌کند که اطلاعات کلیدی مانند متن، نمودارها و یادداشت‌های دست‌نویس را استخراج می‌کند و سپس می‌توانید این داده‌ها را جستجو و درخواست کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6612" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYsBXAddcVwyIrrWyPcsfgG79h5wAGsQT4u9VEESp0kNITjK2-w50o5XjFBL3NDfXi0ie5OAqrKZLpY24NPNL6rWlXYkOQO52imNY_uRHCTE92Lxkspxq8PiNmp3vdSKTtAE5EbMiDO233IffIUkqwvy0JMa7gD5u-CE_wUB_LoTOLB1iMfJMp7H4Jv7foSd_L5uNm1dYjXB5PaDxRfAKArdWmVU0Z0cIVxxN0MESIsnBmHKRZtlwWZCYZnErxJHggJvtbD4SJdGiXWj5YZtVGlcMd2wNiQ7VdTP9G2GG2ocZEPWCTkAoEXnECJ19kp1sVGkBpfL_47-j18MEWHahA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
شورای خردمندان هوش مصنوعی: تصمیم‌گیری با قدرت ۱۸ متخصص
آیا از پاسخ‌های ساده و تکراری هوش مصنوعی خسته شده‌اید؟ با این ابزار، مسئله خود را به شورای مجازی فیلسوفان، دانشمندان و مهندسان بسپارید و تحلیلی عمیق و چندجانبه دریافت کنید.
➖
مناظره کامل بین ۱۸ کارشناس مجازی (سقراط، ارسطو، سون‌تزو، آندری کارپاتی و...)
➖
بررسی مسئله از زوایای مختلف فکری و تخصصی
➖
ارائه راه‌حل‌ها همراه با نقد و رد استدلال‌های رقیب
➖
دریافت نتیجه‌گیری نهایی بر اساس جمع‌بندی بحث‌ها
➖
تحلیل واقعی به جای پاسخ‌های کلیشه‌ای
این ابزار برای تصمیم‌گیری‌های پیچیده و نیاز به دیدگاه‌های متنوع، گزینه‌ای بی‌نظیر است.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6611" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWdWnBBQ9z74T_QU9uBCuu_BXta0apP5SmjRBWzRDMObxD_50xQQPvF4_toapYZwpRHYlvTLsYi_5IgwHEQDuDxFfd-CRaLRm8nwR5pS_0dk6CUIx5muueQmrMwxgaJXO-zUeNX35qqy-ibOT3-HnczYoL8gzTUJpsxx2k2mKfLo5OWw4ywn7_zWnEgCwO7qATVaU8js509JoTuj0Vv9kjVYTTnyhqDUzAgcXYfJ72aVoDXeQS1NgMXgXNh2WMue_XjoCgRhDWgMkWx3waj9vR6f53PsJmKCJ5GQor-_O0-XxzK3fYnFZEmlg3KiH0vVTfFeqkvfvglgkRgkFU0a9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
OFPlayer: پخش‌کننده موسیقی محلی و حرفه‌ای
➖
پشتیبانی کامل از فرمت‌های FLAC و MP3
➖
مدیریت آسان کتابخانه و لیست‌های پخش
➖
نمایش متن ترانه (Lyrics) و کاور آلبوم
➖
تحلیل دقیق فراداده‌های صوتی
➖
اتصال به سرویس‌های WebDAV، Subsonic و Navidrome
➖
رابط کاربری ساده، رایگان و بدون نیاز به ثبت‌نام
این پخش‌کننده برای کاربران NAS و کسانی که مجموعه موسیقی شخصی دارند، بسیار مناسب است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6610" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei2KepgGyFmFAzEvBxddwOPRq9_F9VyDJB36wStwYmYb_OFSGx1A6cOAHPEKYDJZa1-yOBC8P7E8uTCdRWTpbXoUaFEspuBSEpsO55VmABb6e_epPkLN5S28YJGqjU8W14bs4K64lj0UJsNb8QQ7rIVjatHILNimJDjrnXEhixcVdnG024JRbno2BolPhvZU_U88Ei3Z7cASQAgftFgrADrVbAiPk508A9cc2B4JfWgQPgTsf6abPwcjcvzsqWG92kIda_xw9cjnQeXviE9i4Cz-xqhOuLMtUU-ntvNLQm40KwA2nu17sqnZXyInJSJNPXld-t6h5zhxwYhPS08RZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏋️‍♂️
مخزن کد با ۱۳۲۴ تمرین برای اپلیکیشن فیتنس!
اگه میخوای اپلیکیشن فیتنس خودت رو بسازی، این گنجینه رو از دست نده:
• ۱۳۲۴ تمرین کامل
• انیمیشن‌ها و تصاویر باکیفیت
• جزئیات عضلات درگیر و تجهیزات مورد نیاز
• دستورالعمل‌های گام‌به‌گام حرفه‌ای‌
پروژه خودت رو با این داده‌های غنی شروع کن!
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6609" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خب Claude Fable هم استفادش برای مردم عادی کنسل شد
چینیا هم دارن مدرک جعلی میسازن تا بتونن ازش استفاده کنن
😂</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6608" target="_blank">📅 19:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚀
تبدیل جادویی اسناد پیچیده به Markdown خالص با MinerU!
📄
✨
اگر برای استخراج متن، جداول و فرمول‌ها از فایل‌های درهم‌ریخته و پیچیده مشکل دارید، ابزار متن‌باز
MinerU
دقیقاً همان چیزی است که نیاز دارید! این پروژه فوق‌العاده که با استقبال بی‌نظیری روبرو شده و بیش از ۷۰ هزار ستاره در گیت‌هاب دریافت کرده است، اسناد شما را به راحتی و با بالاترین دقت به فرمت تمیز Markdown تبدیل می‌کند.
🔥
ویژگی‌های برجسته این ابزار:
1️⃣
پشتیبانی از فرمت‌های متنوع:
توانایی پردازش و تبدیل فایل‌های PDF، DOCX، PPTX، XLSX، تصاویر و حتی صفحات وب.
2️⃣
استخراج دقیق جزئیات:
بیرون کشیدن بی‌نقص متن‌ها، جداول و فرمول‌های پیچیده (ریاضی و علمی) از دل اسناد.
3️⃣
پشتیبانی از ۱۰۹ زبان:
قابلیت تشخیص و پردازش بی‌نظیر اسناد در اکثر زبان‌های دنیا.
4️⃣
کاملاً رایگان و متن‌باز:
یک پروژه Open Source قدرتمند و بدون هیچ‌گونه محدودیت پرداخت یا نیاز به سرویس‌های ابری پولی.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6607" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQfFJw2H5j8hsbo5p-nfvGTfen2tq-9OwUIw1DX6WdWRdgklezx2I3dypU4My4TYAaPE5fFmYMGyzMaz7x4I3JrxvJhIO9iks6rYyKvC5Dy4t-lzyd6iBvvXef5AGrozzzPpC4ZeK900FMh1obrsMq24T40TReCfNWqUVjVhXjyyB-iceBHaTIcOsDnqqGAUKktWJ7yhwwvOaG5NYXIGvefzIHIcqRkuebuc4IK_4KedxwCcIQgEO7oxQqBQ2Z0caO-bvElktN98y6XBzw5N4rNfqIrS51DyLzszNKL2jGKAdXfGFspZ95_dHwDpF62PZqAID0ltsKQUh7DAcqlNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها ElevenLabs را کشتند!
💀
توسعه‌دهندگان ByteDance نسخه SeedAudio 1.0 را عرضه کردند که هر نوع گفتار و افکت صوتی را کلون و تولید می‌کند.
1⃣
ایجاد گفتگو با چندین شخصیت: هر شخصیت متمایز است، دارای احساسات، سرعت، تمبر و حتی لهجه منحصر به فرد؛
2⃣
دریافت تا سه منبع برای کپی کامل صدا، احساسات و سبک؛
3⃣
تولید صداها بر اساس پرامپت، مرجع صوتی یا حتی تصویر.
آیا این پایان دوران انحصار ElevenLabs است؟
🤔
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6606" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2iGR_-5j_RoKli1zGPLUO8lvQmmgRSqi4HOoHEkPrkSH2pmMTzqtMUYBYlZ99LCfq30MD6SmCra194GiaTYfA-zItxkDhaAnlJrOz0l5VajdyZeMr-km_z5gUpqMW23OoGjiCFt5MlQNjZSIkQbsgI5cejVHesGCb_lOArm4VMjJC_bbtfjEn65t6lpxAvcy40TKPUphHWUIAZmMZ3-UGBNu1dO8gkqmSpCjn3qKDzQat8vRQEyTTCHtLiuM9hUDu9B0_m2BCcgJ516Vox--VobOX5A0H47jTK5Pvadh-iWSM7r5MxW3Efz4nh2-himKWipcCWg41FTu7RzBw6fZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
تولید رابط‌های کاربری زیبا با پرامپت‌های آماده
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6605" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
معرفی IstanPdf؛ ابزار قدرتمند و آفلاین برای مدیریت فایل‌های PDF و DOCX!
📄
✨
اگر از سایت‌های پولی، تبلیغات آزاردهنده و محدودیت‌های سرویس‌های آنلاین تبدیل فرمت خسته شده‌اید، اپلیکیشن
IstanPdf
دقیقاً همان چیزی است که نیاز دارید. این ابزار کاملاً آفلاین توسعه یافته تا جایگزینی بی‌نقص و رایگان برای سرویس‌های پولی (Freemium) باشد. در این اپلیکیشن حریم خصوصی شما در بالاترین سطح قرار دارد و هیچ فایلی از گوشی شما خارج نمی‌شود!
🔥
امکانات فوق‌العاده IstanPdf (نسخه v1.0):
1️⃣
ابزارهای حرفه‌ای PDF:
*
Merge:
ترکیب و چسباندن چندین فایل PDF به یکدیگر.
*
Split:
استخراج صفحات دلخواه با تعیین محدوده صفحات.
*
Remove & Reorder:
حذف صفحات اضافی و تغییر ترتیب صفحات یک فایل.
2️⃣
تبدیل فرمت (Conversions):
* تبدیل یک یا چند تصویر به یک فایل PDF یکپارچه.
* استخراج صفحات PDF و ذخیره آن‌ها به عنوان عکس.
3️⃣
ابزارهای کاربردی DOCX:
امکان حذف صفحات خاص و تغییر چیدمان و ترتیب صفحات در اسناد ورد.
4️⃣
حریم خصوصی و امنیت مطلق:
کاملاً آفلاین، بدون نیاز به ساخت حساب کاربری، بدون محدودیت حجم و آپلود، و فاقد هرگونه تبلیغات و پرداخت درون‌برنامه‌ای.
🔗
دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6604" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYJC--BOgCn2Rn0x7HsuWZqNbhH6kMvuDc6FpSC00aayGTt_WxOFm3PMmfAgyZ5mpwWagLyjQo1GlMaYrgpR7R4KZKOZ91tTtMXVhrKf3uwRfx2Lt0oCq6BPF_UH5iLq0ye2kgws0P0KQWriQNEKcNCioWLCcyzKjsBkI-R-8Z8uyTvxFZCDt0MawCiCN-0dNZxXW4VAYq5JL9SbCI6U5hXPec2E3ieHU8JXSRQ1XWC5J90kCFKdxMKvad54u5sf3cC7uDUCrZnMNPX1cw58rIn2tIvihiGBfws-psAb4XImrVWRpUFcI43YBmZgHDoVaXwDehPAfKfHEv0h0c761Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها:
•
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه
•
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان
•
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب
•
📝
فقط پرامپت بنویسید و کد آماده دریافت کنید
🌐
Site
#AI
#Coding
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6603" target="_blank">📅 11:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=r7UIb0Rg51rBm82D85ds8Oofl33NCzBdUoH-avFnCuNxufQAEf1QDIwm6iqfLYLw5X8nXggDQ7786LdY21Yp7gBMwf4vvpqka6cz7rFhJopb8h0UZZ4iwIs2-HKboFfpbajZYq7hdsBQetQWv5zSF3zBmdDYCalQZPj2WvG-34mNsCdmF8bvlVlTjFkSrIKFTzT1KwtFffRa6WdpZhd-sHCHDbF3YrAHzFJ8zbem3TzhxrpY93T3cNjsalOXO5Tem1RgSX1CyAcVHwQcggO0kDcDwMbHiKtZZdj2rJpR4vmW2Ph8zttE-SGwUR6K6GFVaZo2EwXLgZgrcgCFldshKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=r7UIb0Rg51rBm82D85ds8Oofl33NCzBdUoH-avFnCuNxufQAEf1QDIwm6iqfLYLw5X8nXggDQ7786LdY21Yp7gBMwf4vvpqka6cz7rFhJopb8h0UZZ4iwIs2-HKboFfpbajZYq7hdsBQetQWv5zSF3zBmdDYCalQZPj2WvG-34mNsCdmF8bvlVlTjFkSrIKFTzT1KwtFffRa6WdpZhd-sHCHDbF3YrAHzFJ8zbem3TzhxrpY93T3cNjsalOXO5Tem1RgSX1CyAcVHwQcggO0kDcDwMbHiKtZZdj2rJpR4vmW2Ph8zttE-SGwUR6K6GFVaZo2EwXLgZgrcgCFldshKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🔥
🔥
هر نوع رسانه‌ای را از تلگرام و حتی چت‌های خصوصی دانلود کنید
🤯
• دانلود صوت، پیام‌های صوتی، ویدئو، GIF از چت‌ها، استوری‌ها و حتی چت‌های خصوصی که دانلود در آن‌ها ممنوع است.
• پشتیبانی از دانلودهای چندگانه بدون کاهش سرعت.
• قوانین تلگرام را نقض نمی‌کند، می‌توانید با خیال راحت استفاده کنید.
🌐
GitHub
#Telegram
#Tools
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6600" target="_blank">📅 08:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دریافت 7 میلیون توکن روزانه AI به صورت رایگان!
🎁
🤖
مدل‌های موجود:
• Mimo 2.5 Pro
• Mimo 2.5
• Mistral Large
• Mistral Medium 3.5
💻
کاربرد:
• ساخت وب‌ سایت
🌐
• ساخت ربات تلگرامی
🤖
• کدنویسی در ترمینال
⚙️
🔗
NaraRouter
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6599" target="_blank">📅 01:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Metapi؛ هاب هوشمند و همه‌کاره برای مدیریت APIهای هوش مصنوعی!
🤖
✨
اگر برای دسترسی به مدل‌های هوش مصنوعی در سایت‌های مختلفی ثبت‌نام کرده‌اید، حتماً می‌دانید مدیریت ده‌ها API Key، چک کردن مداوم موجودی و تغییر دستی تنظیمات هنگام قطعی یک سرور چقدر کلافه‌کننده است. پروژه متن‌باز
Metapi
توسعه یافته تا به عنوان «پروکسیِ پروکسی‌ها» تمام این مشکلات را حل کند!
🔥
امکانات و ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
تجمیع تمام APIها (Aggregation):
شما ده‌ها کلید مختلف را به Metapi می‌دهید و این ابزار به شما
فقط یک API Key و یک Base URL واحد
می‌دهد. حالا می‌توانید این کلید واحد را در تمام برنامه‌های خود (مثل Open WebUI، Claude Code یا Cherry Studio) قرار دهید.
2️⃣
مسیریابی هوشمند (Smart Routing):
اگر سرور یکی از ارائه‌دهنده‌ها قطع شود یا مدل خاصی در آن گران باشد، به صورت خودکار درخواست شما را به یک سرور جایگزین، سالم‌تر و ارزان‌تر می‌فرستد (بدون اینکه شما متوجه قطعی شوید!).
3️⃣
دریافت اعتبار خودکار (Auto Check-in):
به صورت زمان‌بندی‌شده در سایت‌هایی که سهمیه رایگان روزانه می‌دهند لاگین کرده و اعتبار شما را به‌طور خودکار جمع‌آوری می‌کند.
4️⃣
حریم خصوصی ۱۰۰٪ و نصب آسان:
به راحتی با داکر (Docker) روی سرور یا سیستم شخصی شما نصب می‌شود و تمام داده‌ها فقط در دیتابیس محلی (SQLite) خودتان ذخیره می‌مانند.
5️⃣
سیستم هشدار پیشرفته:
در صورت بروز قطعی یا اتمام موجودی، از طریق تلگرام و ایمیل (SMTP) به شما نوتیفیکیشن می‌دهد.
⚡️
برخلاف پروژه‌های مشابه که برای تیم‌ها و فروش API طراحی شده‌اند، Metapi کاملاً برای
استفاده شخصی
بهینه‌سازی شده و رابط کاربری بسیار سبک و تمیزی دارد.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#API
#Metapi
#OpenSource
#Github
#SelfHosted
#Docker
#Tools
#OpenWebUI
#LLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6598" target="_blank">📅 01:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Awesome Android Root؛ گنجینه‌ای بی‌نظیر برای روت و شخصی‌سازی اندروید!
📱
✨
اگر به دنیای روت، کاستوم رام‌ها و دستکاری عمیق سیستم‌عامل اندروید علاقه‌مند هستید، مخزن
Awesome Android Root
یک دایرکتوری جامع و بی‌نظیر است که بیش از ۴۰۰ ابزار، اپلیکیشن و ماژول مخصوص دستگاه‌های روت‌شده را به همراه آموزش‌های دقیق در یک‌جا جمع‌آوری کرده است.
🔥
امکانات و ویژگی‌های کلیدی این لیست:
1️⃣
آموزش‌های قدم‌به‌قدم:
راهنماهای کامل و دقیق برای آنلاک کردن بوت‌لودر (Bootloader Unlocking) و نصب کاستوم ریکاوری‌ها (Custom Recovery).
2️⃣
پشتیبانی از جدیدترین متدهای روت:
پوشش کامل و معرفی ابزارها برای روش‌های مدرن روت سیستم از جمله
Magisk
،
KernelSU
و
APatch
.
3️⃣
کالکشن گلچین‌شده ماژول‌ها:
مجموعه‌ای از بهترین و کاربردی‌ترین ابزارها برای مسدودسازی تبلیغات (Ad-blocking) در سطح سیستم، اتوماسیون وظایف و شخصی‌سازی عمیق رابط کاربری اندروید.
⚡️
مشخصات فنی:
*
زبان:
Python (برای مدیریت و استخراج داده‌های لیست)
*
پلتفرم:
Android
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#Root
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6597" target="_blank">📅 20:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jn56X1ldbrqSly-ioEoW5IzlSnfQ7clCjEHv9t0gn_F8R_ZU67UyoM_hUPw1J0m7kDseICQ_PqQVW8EI2pYIuq5YdqJCY6ocYNKh1umFgzmcrPZrHFT_sJNw8QYRnwICrLoKMZnWVX-xiojMUMQnOcKyiw-og2IfGZhjewnpmVKsZIuWS8Q3JOGRuY9iOEuCFiFtyOiGodmtVaMr_AVMWuIqXGTPR9hEp28s2nYmYV6PlCb42uiaZpp3Xb_BieBA4r_sT5JOY53z6X1hQknYuGufX5qGwCzBTJZadAx_k7dhEEqQL6G6HkXWhDzd8eIVz7fDebmFjvXbOeqo3FhySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2xZd7OL7BNWm6-6CYFmVIlTfq2AFma35G_kipgjJnn0MPz401yAK1U9ApdxBm994JzkRDktmlMaAFvQWOudYNEpvZkHLlRkVzl-1nk9fUvlqSm8Vke0yAOXelOJVxqN3EzHvpWABlzg69Z-JddW-gbZgeYvMkOuG1r5WYXR_BTK_PsEGQzX1sFeJixd6MWqZJxNEl52XYHxrW7ID2h1FBTHHo6ROuribENTGcz2hWrpoIK2Eshv9S1WCtdCXFkmj_ZcgK4enG7enXgc5D_iN-8GXcPDbIyMxsrhkU9X_5d7oWmqLRQMimFJ-5gvAI3nVkHIaZGqmmQcxAoVCfHYvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن
Solipsism
یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی با ایده خلاقانه "Rail-first" تمام کنترل‌ها و نوار آدرس را به جای بالا یا پایین، در یک نوار کناری (سمت چپ یا راست) قرار می‌دهد تا کار با گوشی‌های بزرگ با یک دست بسیار راحت‌تر شود.
🔥
ویژگی‌های شگفت‌انگیز این مرورگر:
1️⃣
طراحی نوآورانه (Rail-first):
قرارگیری منوها در نوار کناری با قابلیت تنظیم اندازه (از کوچک تا Super Compact) متناسب با اندازه دست و صفحه نمایش شما.
2️⃣
زبان طراحی Material 3:
رابط کاربری بسیار زیبا با گوشه‌های گرد، انیمیشن‌های روان، سایه‌ها و قابلیت هماهنگ‌سازی رنگ‌ها با تم سیستم‌عامل اندروید.
3️⃣
ابزارهای قدرتمند حریم خصوصی:
دارای مسدودکننده تبلیغات (Ad Blocker)، وب‌گردی ناشناس، کنترل کوکی‌ها و WebRTC، پاک کردن خودکار داده‌ها هنگام خروج، و یک قابلیت بی‌نظیر به نام
Decoy Mode
(تولید تاریخچه وب‌گردی جعلی برای محافظت از حریم خصوصی!).
4️⃣
امکانات کاربردی و سریع:
دارای اسکنر QR داخلی، قابلیت نصب مستقیم وب‌سایت‌ها به عنوان اپلیکیشن (PWA)، پخش تمام‌صفحه و بدون مزاحمت ویدیوها و ابزار دانلود حرفه‌ای.
5️⃣
صفحه خانگی شخصی‌سازی‌شده:
امکان تغییر والپیپر هوم‌پیج یا تنظیم آن روی حالت کاملاً تاریک و بی‌صدا.
﻿
⚡️
این مرورگر سبک که بر پایه WebView اندروید ساخته شده، تجربه‌ای کاملاً متفاوت، سریع و مدرن از وب‌گردی را به شما ارائه می‌دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Solipsism
#Android
#Browser
#Privacy
#Material3
#AdBlocker
#WebDevelopment
#MobileApp
#TechTools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚀
هوش مصنوعی دیگر کدهای شما را فراموش نمی‌کند؛ دستیار حافظه دائمی برای ایجنت‌های برنامه‌نویسی!
🧠
✨
اگر از پریدن کانتکست (Context) در چت با هوش مصنوعی و توضیح دادن‌های تکراری خسته شده‌اید، این ابزار جدید مشکل شما را حل می‌کند! به تازگی یک دستیار هوشمند برای مدل‌هایی مثل Claude، Codex و Cursor منتشر شده که دانش و اطلاعات پروژه شما را بین سشن‌های (Sessions) کاری مختلف حفظ می‌کند.
🔥
این دستیار چه کارهایی انجام می‌دهد؟
1️⃣
حفظ همیشگی کانتکست:
اطلاعات جلسات کاری شما را ذخیره می‌کند تا با بستن پنجره، کدهای شما فراموش نشوند.
2️⃣
یادگیری ساختار پروژه:
معماری، دایرکتوری‌ها و ویژگی‌های خاص کدبیس (Codebase) شما را کاملاً به خاطر می‌سپارد.
3️⃣
بسته‌بندی خودکار دانش:
اطلاعات جمع‌آوری‌شده را به صورت خودکار و هوشمند بایگانی و بهینه‌سازی می‌کند.
4️⃣
بازخوانی در کسری از ثانیه:
هر زمان که ایجنت به اطلاعات قدیمی نیاز داشته باشد، در کمتر از یک ثانیه آن را فراخوانی می‌کند.
5️⃣
پشتیبانی بسیار گسترده:
سازگاری کامل با
Claude Code
،
Cursor
،
Codex
،
LangGraph
،
CrewAI
و سایر ایجنت‌های هوش مصنوعی.
🔗
لینک دریافت و راه‌اندازی پروژه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#CodingAgents
#Claude
#Cursor
#Codex
#LLM
#Memory
#ProgrammingTools
#DevTools</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh09pBWCzQPT-z_kJPTc5MZn_J7bqOjsLyx-O5YovkubjdE1Jac0rB7M9IFfLMfSUYts6sdMjqQcpU9Y2L0nQvJEZjWOKFKZAYrtPGqhgZmBFlmXCpdjuD2bQatplIa8MZpWZWXlsz6UGAL3K2I1XjSL9ehusbdxFU2ARA-Uu1bPSI_bIZJwl7Vjx02KqsszE3JOktkTjGrK3gsB-cRVQV9oJ0sEIFI2IwVCt7nBed_rgUTseMn2RCqsf1-FzOibzNut9attFE_gOpyMX4oAd8CBGvJRHnN9r45k7G_jJbaR9pzVQPFl8E6eCOUFe_gCkkeuOdS5x0HZGBbo7U327A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 1T کانفیگ شخصی
🔑
🟢
از لینک زیر میتونین شروع به ساخت اکانت کنید :
➡️
sign up
بعد از ثبت نام وارد اکانت بشید و روی
Quick Subscription
کلیک کنید و داخل اپ هایی مثل :
Nekobox,hiddify,singbox و ...
اکسپورت کنین .
به دلیل نوع پروتکل یعنی AnyTls بودن فقط داخل اپ های ذکر شده میتونین اکسپورت کنین و داخل اپ هایی مثل V2ray کار نمیکنن
😬
خط های تست شده :
🛜
🛜
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIsq4PykoOKOXbd7iGub6yMWs_trjVdNDXLdZIjC-i4Aa6wFexgowAielxOzBaS6Zs5Y62LGSSCHQcGiBryf-flIcBVGggkro-YAcATrZ1mbwmArP82JuwNBK81JhDt6QRobNDAT2UlBQEz0x613b5DGA0erFPIzvUuWz2SWUZMF4upSjJfJ1Alh45gYiUm5LnCMpXpeV-K1mHaLptLvWieeftflrRooBJyVmLqKzprmr6-g4-D6JjZSD1aV_ebwyXfB4dRnK7eRP8hYbezPhWV-VqC8bSjz4f3YYal6Hzvo4Lmqn8i2C7OR1E3kAJobftPiOtnHkpoJrrqJ5XPKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBMbQNHbg3XDXdiHa031FZcC_pnJNWNzi1Bia2MsCRNSgPKdbmOdl5wscxGJTYbo8at9PDcHgnVRSK7ylW-TsrvkWYHEfkZifxinAfcKZg-pbCzBqQtWGTV1JGEmU9IrzkPtaB_GZRyss5AHsaIEnZNkFj6KNYhm4eBNgR20bXsC8YB9jFScMpZQulaKFtcs-JJXuwww91BFhOjQ_8fzImDuLz0M4tUV8Mu0t7yIPSUVZb1fKnDlegK80GnDQyLM6SFK0LdvBPemG_Oo5eu0E8ZYe8s5TLMFctq3DAhOzH-7JsfzicARn4wrk1KykGcUT6h7jnyzeLwbhbBcPa_hQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYV8-vqPq8ZY7XNqrVyRIyP4aSPT0VDk34BNAMFrTuxuHguP_aBv1DyEE2zcT9TNvFpMCDt2FysihSNP9nD9PpmS7sqPC0gyQul1yOgEO-cZOteFrPr484mYmLpT6ddiF9uKnaRolG9Swhj7f5glMAPIb_HBe08REIRZaN9prIyIdXnwtg2yw-ie1OPAl7qMRiOygrmmIofY2Z-DQUrdotYbKXqvvS0BraaF52CkeyrY8Ffs-DF9TcY8MeNHHNHjllyqFpSZ_DJAbSeKZRIRSX9jI9XeLp8wrrwrtSNmgTeGAX41DjD4jO--nA-I1AdVCxBjUPSmDu7mO7gcAQ_7Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبدیل عکس‌های معمولی به شاهکارهای هنری با هوش مصنوعی
🔥
✨
قابلیت‌ها:
•
🎨
انتقال سبک هنری (مثل ون‌گوگ) به تصاویر شما
•
🪄
انتقال سبک بصری یک عکس به عکس دیگر
•
⚡
مبتنی بر شبکه‌های عصبی کانولوشنی و الگوریتم‌های پیشرفته
•
🛠️
رابط کاربری ساده و سریع برای ویرایش آنلاین
•
📦
بدون نیاز به نصب نرم‌افزار سنگین
🌐
Site
#AI
#Art
#Tech
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqFz0Q_f2OnggnsiCxiHNTE-NjRreCJC4Bp9Q49VEpg0QzKNy8dhhhmdpe_tTDUI-bjR9mN38RSH1z_78KsRxFxu8EOoWDIn_Iy4MHPzErVA_XBgvr9bOsbJwbYy9o6GRMeW5r160vZF9YrS0CHlV1lItEr9sOybMvREBgJj-KLm7-v9MF4gqlihQEbYNehDRbcY5GyIIxgOQNf4lmAzM5r5MAp1MkvYftuQywXMhGR90lWjNxkaezMfbvHS6_S2L3PHiEa0pdhAamJYoLfbdwhS1ADTsCHLViTRhbTRfuSKZBFBbYcWz6A051hlNL59cGCy8sQqzYPswnNABe2Xgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=Ftd2n9OCq1dDi5YxuxbfRc-Vyk0ZFo4Or1whc6pWIZplilobqUjfJReJzYKY1pi7YXQoV8OQKktJz9ihokAUmkDzoxlOOlDM2XJohb3UbpNUDMWOEtvlgzqjuRW7Vcw-LwkFBmhO4MicDqKdf5IXGfeluDv4rxN_QYFwk539SNX7lUoDunpiI_u_z-qlokHDElgFxJmik4Pj2fLWB8h2PEyeH3a4gwOiK8KAShaqgMMDU6Z7hbnRfnZvNVqvIk_PaUwL6Ubji7So-DoF8swngWJE37e3u1hMxRHoPaln0UhqMBzfosfXU3_05JPRPqG97MJT2Ox-DYLFIhdk57ylzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=Ftd2n9OCq1dDi5YxuxbfRc-Vyk0ZFo4Or1whc6pWIZplilobqUjfJReJzYKY1pi7YXQoV8OQKktJz9ihokAUmkDzoxlOOlDM2XJohb3UbpNUDMWOEtvlgzqjuRW7Vcw-LwkFBmhO4MicDqKdf5IXGfeluDv4rxN_QYFwk539SNX7lUoDunpiI_u_z-qlokHDElgFxJmik4Pj2fLWB8h2PEyeH3a4gwOiK8KAShaqgMMDU6Z7hbnRfnZvNVqvIk_PaUwL6Ubji7So-DoF8swngWJE37e3u1hMxRHoPaln0UhqMBzfosfXU3_05JPRPqG97MJT2Ox-DYLFIhdk57ylzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bw05VPKvgHqyftdo9gfaZpZJrtXzLs1wSa-gM01Whl7jWnooSmKgLilDbK4Y4jhv9wK7CUTfqcaLypU1HXeOOvhu_RP-VJssJzvhA4gMPteLoddhG5lMgoxrF6oS5zgBT-aS9o5hEdgHGTM49YOzQHEPEB2LHBHOy8tBmW8WUkTGfmnw5UyKFii76GZIakm9TWadP5njTRzROby_V5EL6yjkW2Jnyszxb9_rq5ZVMfj3CpjIIaEzRe1VHbe2l72GTD68HyCsvgE6NautsnKH4QXvayy8C844tHkJc4UuwmIHlLiJqfEkprGHt3jNYTlUF8VQr6ARWlRsJRzifOYrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrE7w85EhrCn6K3xMnP0a8VL5lDatNn9hfwWmQx-ckCvv_6_Ua15UxNJkJcLScCtjEIfilHu8a3O8WfjFtVcLSzwXei7KpL1m7Tzkgsbrybu_VifHIAW4vlFChZdlcBLuePK2ox16DELuzVhJUmXxS9VcffKJtNau03GV6Xc19OiPd5568tARAYamtesCCfNYJfnYs6IMOOAqcP3M1Ud5nACWpLyzYPMeGay8OB7yKminOuU9ehk6F1wnuPnEOzjOuX1soOk8HcZqVmkB9WZIFwKGEa0y9sSKwLhwJtGSLk9KiRr3QDU-xRyte_rPlfRNnBW5c-1K0Jb5lozCsXx0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR38qllEYfIdsXvYd7wruIFTnAhXCOHju67rYTGqRHMY1Pf5UotI9kddrkZxg8TTjaUJbqMX9Zrump9Ll4aSCnN7UhXo8xZnNVMYWtbwXUjvEjr1HU_RKkVG8r-NbFccPhmR-u2tuYV8oxXoauijRDnSxVFJeOuun61w0ff9-XQCCC2jtPBusKV-m-Npv2bE9svIbG_9Cef3f0ctbn_rS-b2blZ8c0DHxia36NRbbWAE3mVcc5TR0KJXLKGR-4O4t8Yk55SchnBKNfYO_y78BdVm6-_kEMy700bTSVPY7afrt6ahUTONI0KO44fG92c6rIHPn1mHHFwVDRcwh9_ckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
انگلیسی رو تو حرکت، باشگاه یا پیاده‌روی تقویت کن!
با این ۵ پادکست، بدون کتاب‌های خسته‌کننده به گفتار زنده عادت می‌کنی:
•
🇺🇸
American English Podcast
: انگلیسی آمریکایی، فرهنگ ایالات متحده و مکالمات واقعی.
•
🧠
English Learning for Curious Minds
: داستان‌های جذاب درباره علم، کسب‌وکار و زندگی.
•
⏰
6 Minute English (BBC)
: قسمت‌های کوتاه با واژگان جدید، اصطلاحات و موضوعات روز.
•
🗣️
The English We Speak
: عبارات مدرن، زبان عامیانه و اصطلاحات مکالمه‌ای.
•
🇬🇧
Luke's English Podcast
: تحلیل زبان و فرهنگ بریتانیایی، یکی از معروف‌ترین‌ها.
#EnglishLearning
#Podcast
#Language
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOK16J4n_iQgP8hsAZFey416WZf1WaJyYPaMUbA1y6brsyon72XRJySjQ9aShm_cpupcySdxf7ZnTli4vgonFRHYAxN3la3s4yv2AutvQJmKXvEaAfux_bQtOe8skdvq3owpOkjFepunWJfUxwRhfXGbBBI7d6H9RjTQWBFCUtOt1-LdcUnD8Gk30iGd2-ARHYrwQ2bNh2I-J4c-Ao9UNlL4Mq4Rpj_gzrg-QpFJd-HErlBfTM2XatO12YlYqXFUQ3EqqjzlXzenpMdps55LaLvDmbcba8XUFArLRnrfM4Ay70H4tF8oCaltJDQlkX-DfEsJSQ9z-nPbpab0-0I-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qFCswDmB6u5kWSgKyG4zL0KCnIek-s5yEB3YmaYNbqOozfDcO3ht5aFrBHELHnLIWG163vo9AOjU80-GfDl0pRYZhn4DZoisELiCC8RbK3pZInF_6in_Qey3KYX_PA4KWlqUPO-oGm78eiaXw6axMGjZDzquUpK5uab2_6K1GKiPxeO1XN6fVQX8ste4pmzw54Vt35zlIYp3Py49AhNadgXvBOdTH0sJ0qeqX1ZhRZvQ7V7Krm0yLUA7ZdVINzGKKWOxqxGkLeiBOiiL67gz69v10U4iDZFEBtQTvBAm_XgHpnycN-T7OAKDCumwVY0ezSVdNbStBfAUy9E0TiZr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVbLKXlHk0ZnMYKVH4cHmylPs9f4bbyoX9R1JB7ilUUiyPmqxhPnJiD6dME48SRCtULHYJh2cUAmmAg-45sdTQlGIj-CugJB-czEB3UxOUkQ8EmOf1HS31IU-KwBKrEZY8nuIBlZiYHWH3KBauCDqvFEVfAD9q6OaUUCZ235xWp6lStTIkigis5cCmt6prlYnR9kArYtjJwxQep2uimuXMLQsRRw1whlPw_ea_AAug5gxO3J1KMgOTMmK0KvHPqZCjJSmv1AI-3Gkzc0e1s4OUyhEk8Dr9dOiI5RB7wp4K4Pdnq96cs4JnlD7yG4wGP7M4lrzO73iiZRqsmgyF3hMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
OpenAI
مدل جدید GPT-5.6 Sol را معرفی کرد؛ مدلی که در چند بنچمارک مهم، حتی از رقبای مطرح هم جلو زده و تمرکز اصلی‌اش روی کارهای پیچیده و توسعه نرم‌افزار است.
💻
🧠
•
🔹
عملکرد بهتر در بنچمارک‌هایی مثل Terminal-Bench 2.1
•
⚡
توانایی کار مداوم روی پروژه‌ها برای ساعت‌های طولانی
•
🛠️
مناسب‌ برای توسعه نرم‌افزار با دخالت کمتر انسان
•
📦
معرفی مدل‌های سبک‌تر و ارزان‌تر Terra و Luna در کنار Sol
🌐
Site
#AI
#OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الان برای API بهترین
aerolink
هست که بهتون
opus 4.8
میده
خیلی ساده
لینک ثبت نام
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
نحوه اجراش روی
claude code
هم همونه فقط تنظیمات رو این بزنید
هر ورژنی از claude code هم بزنید قبوله
{
"env": {
"ANTHROPIC_API_KEY": "کلید",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلید'"
}
لیمیتش هم دقیقا مثل
freemodel
هست
فقط مشکل اینه هر ip ایی تو claude code قبول نمیکنه باید تست کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=p5Hui2tCEzOUjS7rvx98QuDZ6eCdFRl9GK9q6RStLpp-IREmP1UfS5ZSb99wF5lB5F_6MHPBFdEmPryJ13uD2SZyI_EizjosG0AKDBoX_1pKnuY9XOdvv7f1OfyIxekD6XK5OCwdq9QdseoKoLmRa3xyspyhTFSj6sW46UpkzCX1MsrGteuBO-KcavF1WRonXt_Mgo9zBbiRc3_ygq6Qx-qVFfx0MUYo22J1J0KsTSRGJKfTRTIM_SkpmGtEMqPUZhKGDllPcQgjBqnK-hQLnmYTkwfJXO9-yBpXvEuBeMjim1pro3XsLKAD9JQhVs4IbRP9CJRjQSCMrZbIsEN-GEQ44c7--4WvCGw0oarZXuw52aaxtCeGNnDy1TXT8O66VOGPrfFguWXvAFhomzfhMYpo0kjomr5g3xD57RM_6O7kawaw6PiGx1Stc5YnDiBepC-1X4khYusTAtNI2YSzKDW_8M-Tf2-O7aOzWX51KFVqfwFDWwpvzQ6ftSp1hrFG9QSD9iVgYAzZ2XhtG5JW1MhyQLM9Js_uecVbHYJFF60YtBQBAaOymLnoItzdRr5DZgzGiUziKb0swVRS5P4XWaFHsnrnoUEuFaP7JmecUizG0VPY4GXfEpPpcDLOzzOksgT98bgOCZ7lkQeNxP5eSjDq0lWW1Tv6vXP4GuFHiiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=p5Hui2tCEzOUjS7rvx98QuDZ6eCdFRl9GK9q6RStLpp-IREmP1UfS5ZSb99wF5lB5F_6MHPBFdEmPryJ13uD2SZyI_EizjosG0AKDBoX_1pKnuY9XOdvv7f1OfyIxekD6XK5OCwdq9QdseoKoLmRa3xyspyhTFSj6sW46UpkzCX1MsrGteuBO-KcavF1WRonXt_Mgo9zBbiRc3_ygq6Qx-qVFfx0MUYo22J1J0KsTSRGJKfTRTIM_SkpmGtEMqPUZhKGDllPcQgjBqnK-hQLnmYTkwfJXO9-yBpXvEuBeMjim1pro3XsLKAD9JQhVs4IbRP9CJRjQSCMrZbIsEN-GEQ44c7--4WvCGw0oarZXuw52aaxtCeGNnDy1TXT8O66VOGPrfFguWXvAFhomzfhMYpo0kjomr5g3xD57RM_6O7kawaw6PiGx1Stc5YnDiBepC-1X4khYusTAtNI2YSzKDW_8M-Tf2-O7aOzWX51KFVqfwFDWwpvzQ6ftSp1hrFG9QSD9iVgYAzZ2XhtG5JW1MhyQLM9Js_uecVbHYJFF60YtBQBAaOymLnoItzdRr5DZgzGiUziKb0swVRS5P4XWaFHsnrnoUEuFaP7JmecUizG0VPY4GXfEpPpcDLOzzOksgT98bgOCZ7lkQeNxP5eSjDq0lWW1Tv6vXP4GuFHiiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=I_5ZbiEqQo5ShXCGc2UL1x6TNXmZte0J9ihlObiux2mAKBBTd7LoPNfyba8toUHEc57UKspk3oEYdLpWKMaWqf1xi06estwf6D0Y06lsGcrLsJhc2dziScQHgwD6NTKlFo9Ep5kybOPbkn4RRCXaaCmU-RU6kG4HP9uIGQr8zD_f3ZXLzGHgfIrAKhl9gDt2CSsun5rGhFh-zE3SH3kcpyGPwaI1uzMl0Gv8MoFAwFFxk7621Y3Qib2KKjHO8aSqZPGZCOEn_wrT9zAu60HWUlukpA8AWCnjv2GLld4xqFWqNn0-_sGT_FlFaNzt-8uVJY-8kVZl7LtLZqzbq92BNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=I_5ZbiEqQo5ShXCGc2UL1x6TNXmZte0J9ihlObiux2mAKBBTd7LoPNfyba8toUHEc57UKspk3oEYdLpWKMaWqf1xi06estwf6D0Y06lsGcrLsJhc2dziScQHgwD6NTKlFo9Ep5kybOPbkn4RRCXaaCmU-RU6kG4HP9uIGQr8zD_f3ZXLzGHgfIrAKhl9gDt2CSsun5rGhFh-zE3SH3kcpyGPwaI1uzMl0Gv8MoFAwFFxk7621Y3Qib2KKjHO8aSqZPGZCOEn_wrT9zAu60HWUlukpA8AWCnjv2GLld4xqFWqNn0-_sGT_FlFaNzt-8uVJY-8kVZl7LtLZqzbq92BNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPtUKSDosAXXzx-AM5ZnpEqP0D8Kx393MmsKImkEVgFApN5ZrjyLcQer4YJtQTIvz7hMK9zCmzwTdkp3PT2yi4qR72TBUjzgkTBzmHakzo_ted4kRhQP_x3DyAyDS6dyQ_gUYwWf32U0huUZo25U-gjLS8CCH4q3EfJOFDA5YK8z4o80PGvOX8ud4MUvBtJGwsR-4Mmd72TAgst8jVPhDYM9SeZnqzpa0S_CjJb2jT84rkT0DGEHuXbKWrWISDRl-NtV_8R6DaqD13SFN3N1cBSfcOg34ja2U9Gqk5nGbVYbCKKhM37dHnCLo5w6DIC3EPFFVJw5mNwFgRIQCnsw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=JfAyE0ysywr5mGgJV3k_OGfVpcMubWUwkQ62S1HmkXSaBr-EZyTrbEjMbuuoVyscb5iVUd-NVzwKhc5ffs0Y6kdiW6UO_jI-7sr6QHU3RpqtYWJWmn7fVgZZ5oTWyp86yfY0cgKK9ucKKrk0ALRkZbSrD_1e_TBNwinp0LwNtPbhwOLTCHcoD5vK4He-nDDnE2-VU6Ixcx_bxxSFiu0KE089cePGKRrhbNw5q67BiWLirTKtAfm52jcqmVtv5d-bnOxS2kwB0H6zTV5PwkDrWf76PVlGSpg0xCBdsTiylNNDBJ2mqOcQw_54TI9RGSqxvlte8mN77h8oXtipVM3qNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=JfAyE0ysywr5mGgJV3k_OGfVpcMubWUwkQ62S1HmkXSaBr-EZyTrbEjMbuuoVyscb5iVUd-NVzwKhc5ffs0Y6kdiW6UO_jI-7sr6QHU3RpqtYWJWmn7fVgZZ5oTWyp86yfY0cgKK9ucKKrk0ALRkZbSrD_1e_TBNwinp0LwNtPbhwOLTCHcoD5vK4He-nDDnE2-VU6Ixcx_bxxSFiu0KE089cePGKRrhbNw5q67BiWLirTKtAfm52jcqmVtv5d-bnOxS2kwB0H6zTV5PwkDrWf76PVlGSpg0xCBdsTiylNNDBJ2mqOcQw_54TI9RGSqxvlte8mN77h8oXtipVM3qNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
دسترسی رایگان به API غول‌های هوش مصنوعی!
با لینک زیر به جدیدترین مدل‌ها دسترسی پیدا کنید:
🔹
GPT 5.4
🔹
Claude Sonnet 4.6
✅
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
🔗
zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=h3NPByFIXW34ti0HZpWONckk_3QJvbh8pgZk5vvT5_ddzTW-zkdCgQ3Ie4pnGeBkhvB0_NW9zXXN4ZIwr1za2aKJV6vUiXBfyuXkeR38FaHb2XLO5UWZQbT-ynUv73NGXb1xfWbmJeqHMGmLRWEbEnVw4XfdvJ8ApdIHiVwowCkI2EO28HejIEreRnPOePlCwQ860VdawgbcCU_qeMVQZBAgCH21O7hFqRQV7P21Z9rSfohCgv49MspPqB4wZ00eY5E5BZ6m1LJwACCdAHBG7D3OTsub69piDELMaA34UL62xu7RRWzNzLYiexo_NXA9Nz4YBlLTSFu-DTPOM63jNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=h3NPByFIXW34ti0HZpWONckk_3QJvbh8pgZk5vvT5_ddzTW-zkdCgQ3Ie4pnGeBkhvB0_NW9zXXN4ZIwr1za2aKJV6vUiXBfyuXkeR38FaHb2XLO5UWZQbT-ynUv73NGXb1xfWbmJeqHMGmLRWEbEnVw4XfdvJ8ApdIHiVwowCkI2EO28HejIEreRnPOePlCwQ860VdawgbcCU_qeMVQZBAgCH21O7hFqRQV7P21Z9rSfohCgv49MspPqB4wZ00eY5E5BZ6m1LJwACCdAHBG7D3OTsub69piDELMaA34UL62xu7RRWzNzLYiexo_NXA9Nz4YBlLTSFu-DTPOM63jNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlodS56MDx2oz-nPXmpU2FkARy9084ffcTmoRSRUlFaAUq2mgy09P5jrYS803wqtoLfFL8K_IOprk3ID4hNxXsFPvCbTVmpTaSVDhUsjJO2ZWIy-2GJpWkSgJaf4lLzg2siniplEBoY1euT4Q2Yl1BCVupIWBX2vijVnevecgAThq2aNWgcqpWNSx6YB11acvf9uVP9wF_mnGxVnmnpmocLzTeS5Rt1GprEK1z1uYL3FGGzZGBT8qCfMmmGZMI-eSf9j_4sjhNlmqCfLiqNd_5oFoO-OyroqeWqwRVGNLeXGe1wAdRfau6ZqGo3cFpCrGMyIZ8AUUeLXVzfwe41eKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یه ترفند خفن برای چند برابر کردن سرعت گوشی‌های سامسونگ!
احتمالاً شما هم فکر می‌کنید هرچی مقدار RAM بیشتر باشه سرعت گوشی بالاتره، اما یه گزینه‌ای تو گوشی‌های سامسونگ هست به اسم RAM Plus که به صورت پیش‌فرض روی همه مدل‌ها فعاله و برخلاف اسمش، تو خیلی از مواقع باعث لگ و کندی اعصاب‌خردکن میشه!
🤦‍♂️
🧐
اما چرا این اتفاق میفته؟
قابلیت Ram Plus در واقع میاد بخشی از حافظه داخلی گوشی رو به عنوان «رم مجازی» اشغال می‌کنه تا برنامه‌های بیشتری تو پس‌زمینه باز بمونن. از اونجایی که سرعت حافظه داخلی به مراتب از رم فیزیکی (سخت‌افزاری) خود گوشی پایین‌تره، وقتی سیستم می‌خواد اطلاعات رو بین این دو جابجا کنه، پردازنده بی‌دلیل درگیر میشه و گوشی کُند میشه.
🛠
چطوری غیرفعالش کنیم تا گوشی پرواز کنه؟
کافیه وارد تنظیمات گوشی بشید و دقیقاً این مسیر رو برید:
⚙️
Settings > Device Care > Memory > RAM Plus
(اگر منوی گوشیتون فارسیه: تنظیمات > مراقبت از دستگاه > حافظه > رم پلاس)
گزینه بالای صفحه رو روی حالت Off (خاموش) قرار بدید.
بعد از این کار گوشی ازتون می‌خواد که یک بار ری‌استارت بشه)
✅
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
معرفی MinerU؛ استخراج جادویی و سریع متن از انواع فایل‌ها!
📄
✨
اگر برای پروژه‌های هوش مصنوعی (مثل RAG)، کارهای تحقیقاتی یا روزمره نیاز به استخراج متنِ تمیز از فایل‌های مختلف دارید، ابزار رایگان و متن‌باز
MinerU
یک شاهکار به تمام معناست!
🔥
ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
پشتیبانی همه‌جانبه:
تبدیل فایل‌های PDF، Word، Excel، PowerPoint و حتی اسناد اسکن‌شده به متن خالص و بدون به هم ریختگی.
2️⃣
سرعت پردازش خیره‌کننده:
می‌تواند یک فایل PDF دویست صفحه‌ای را در کمتر از ۱.۵ دقیقه پردازش کرده و متن آن را استخراج کند!
3️⃣
اجرای کاملاً محلی (Local):
بدون نیاز به اینترنت و سرورهای ابری روی کامپیوتر خودتان اجرا می‌شود که برای حفظ حریم خصوصی فایل‌های حساس بی‌نظیر است.
4️⃣
بهترین دوست هوش مصنوعی:
پشتیبانی از پردازش گروهی فایل‌ها (Batch) و قابلیت ادغام و همگام‌سازی بی‌نقص با ایجنت‌های هوش مصنوعی مانند
Claude
،
Cursor
و سایر LLMها.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#MinerU
#PDFExtractor
#OCR
#AI
#Claude
#Cursor
#OpenSource
#Github
#Tools
#RAG
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7YIE-4kaFG1HcfySgrBNh7jgL4Eo_EHj1A1x0fGEPhYKZrzX4yDkqKsU0iNui56f5sZ0IfXy6VOwclZ1lADgjwK2yD-CNkUsRRgZ2PbP4_pWMUqeuJhKG_tT0z7CTf6-a2ZQ46AJBw1Kosxo8wZJFk4s5CHQnaMSJXA1jlZU6g2KvLxk11Ef2WhYB9jvRFu-5J7VkiXjYZcA-VbVh7e-4JZlSRpivz-ihU5qVUsxTSnACVJXMDHxtGRE5B7R92oItbvdTh7-mDVYmbYUaoaVwoKySAHh7ggVtPhYwdQCEUBY4Y2DEQBBsaQ1-UtabqJLi7bhu9nWov9c8n9hBx-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Popit Music: ساخت موسیقی با هوش مصنوعی و مالکیت کامل اثر
🎵
✨
قابلیت‌ها:
•
🔹
انتخاب ژانر و حالت برای تولید سریع ترک
•
⚡
ورود خودکار به پلی‌لیست و رقابت با آثار دیگر
•
🛠️
مالکیت کامل حقوق موسیقی متعلق به شماست
•
📦
دو بار تولید رایگان برای شروع
🌐
Site
#AI
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
معرفی droidMirroring-mac؛ تجربه اکوسیستم اپل برای کاربران اندروید در مک!
📱
💻
✨
اگر از گوشی اندرویدی استفاده می‌کنید اما کامپیوتر شما Mac (سیستم‌عامل macOS) است، احتمالاً همیشه حسرت قابلیت یکپارچگی عمیق اکوسیستم اپل (مثل iPhone Mirroring و Handoff) را خورده‌اید. پروژه جدید و متن‌باز
droidMirroring-mac
دقیقاً برای حل همین مشکل و پر کردن این خلأ توسعه یافته است!
🔥
ویژگی‌های جذاب این ابزار:
1️⃣
انعکاس صفحه (Screen Mirroring):
مشاهده و کنترل کامل گوشی اندرویدی مستقیماً از روی صفحه نمایش مک (دقیقاً شبیه به قابلیت جذاب iPhone Mirroring در نسخه‌های جدید macOS).
2️⃣
کلیپ‌بورد مشترک (Universal Clipboard):
همگام‌سازی بی‌وقفه کلیپ‌بورد بین گوشی و مک؛ متنی را در اندروید کپی کنید و در مک Paste کنید (و بالعکس).
3️⃣
رایگان و متن‌باز:
این پروژه کاملاً Open-Source است و بدون نیاز به خرید اشتراک یا برنامه‌های تجاری گران‌قیمت، ارتباطی عمیق بین دو اکوسیستم متفاوت ایجاد می‌کند.
اگر به تازگی از آیفون به اندروید مهاجرت کرده‌اید ولی نمی‌خواهید راحتیِ کار با مک را از دست بدهید، این پروژه گیت‌هابی یک معجزه برای شماست!
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#macOS
#ScreenMirroring
#Productivity
#OpenSource
#Github
#Tools
#Handoff
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqyfHk8NeMdc-tMdPKDZU5H5IqQVCFmQsZCALkvmNYxM7Nh1-mDF0Er1ieOmIucRyCwCxSErByiNifBGdRJnqxm6Wl1khWrPOuEGG0ga1UMFOpiVx_KIzw0CyddGH8vPsc5XLwK2ijkDjE5MpVCSS8w7TKfI5BR4DYWH63gnR6qCQlNKptJVKc4f3GbjI0KMUwsNSMJqO160rjOEv_6RK2vFfqPDYvWhOdRQpj2Av2BtvgKl9_Ya_yJzgqrN3B4qqxEOgVlkZ3AyBHHbHtEmCj0TbgZmp9mRpDysgyExRBIkwWu-a6plUAfsj1Ew7FUXdEjDXIkP6mkMCaTEM3EWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">> توسعه‌دهنده‌ای با نام مستعار slqnt نسخه وب بازی افسانه‌ای Half-Life 2 را معرفی کرد.
اکنون می‌توانید این شوتر افسانه‌ای را مستقیماً در مرورگر اجرا کنید، بدون نیاز به نصب برنامه‌ها یا راه‌اندازها.
بازی پایداری شگفت‌انگیزی را نشان می‌دهد و کاربران در حال آزمایش پروژه‌هایی مانند
Ravenholm
و
City-17
در مرورگر هستند!
🌐
Site
#HalfLife2
#WebGame
#Gaming
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=n2m-lFD0YeMQ52NyvN6Fk65E4vID_ePJCUb86xP8Xc_CAVjM3to_GjQaj24GZQ2nhxANcmEoNI51Vjq66EoBoYbHEa6Ei9TMzAl4r_l31SDwjw_2hS_PRFKA_EwkSOKTA1Zz9XCD9t16cCpKaJBPLA_m55DMYyBKx-WHbmEu5VJppAhPx1e7LhNs9YWY8Ej1a0QLxP4RUi5apFAhSHtsp3C7PiJB6OFkmNgk9xnKkAkpG1QQbHFBptysOvJtqAVUU6R_YZNWrWGm1C4yDY9vJHw00xQ1nEutfYLJ8HarVheEwyNWEasfSYEZr2vGeODdpOYXXai0H0mHsBBtGKCfbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=n2m-lFD0YeMQ52NyvN6Fk65E4vID_ePJCUb86xP8Xc_CAVjM3to_GjQaj24GZQ2nhxANcmEoNI51Vjq66EoBoYbHEa6Ei9TMzAl4r_l31SDwjw_2hS_PRFKA_EwkSOKTA1Zz9XCD9t16cCpKaJBPLA_m55DMYyBKx-WHbmEu5VJppAhPx1e7LhNs9YWY8Ej1a0QLxP4RUi5apFAhSHtsp3C7PiJB6OFkmNgk9xnKkAkpG1QQbHFBptysOvJtqAVUU6R_YZNWrWGm1C4yDY9vJHw00xQ1nEutfYLJ8HarVheEwyNWEasfSYEZr2vGeODdpOYXXai0H0mHsBBtGKCfbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم
Caveman
دقیقاً برای شما ساخته شده است! این افزونه کاربردی با بهینه‌سازی کلمات، مصرف توکن را در سرویس‌هایی مثل
ChatGPT
،
Claude
،
Gemini
و سایر مدل‌ها به حداقل می‌رساند.
🔥
این افزونه چطور کار می‌کند و چه ویژگی‌هایی دارد؟
1️⃣
صرفه‌جویی تا ۷۵ درصد:
این ابزار پرامپت‌های شما و پاسخ‌های هوش مصنوعی را به صورت خودکار بازنویسی می‌کند و با حذف کلمات اضافه، مصرف توکن‌های خروجی را تا
۷۵٪
کاهش می‌دهد.
2️⃣
حفظ معنای اصلی:
با وجود کوتاه شدن جملات (شبیه به لحن انسان‌های اولیه!)، پیام اصلی و محتوای علمی/فنی به هیچ وجه از بین نمی‌رود.
3️⃣
پاسخ‌های بدون حاشیه:
به جای خواندن پاراگراف‌های طولانی و خسته‌کننده، هوش مصنوعی را مجبور می‌کند تا جواب‌هایی کاملاً خلاصه، سرراست و پرمحتوا به شما بدهد.
4️⃣
پشتیبانی گسترده:
این افزونه برای تمامی سرویس‌های معروف LLM قابل استفاده است.
💡
نکته کاربردی:
ای
ن ابزار مخصوصاً برای کاربران نسخه‌های رایگان Claude و ChatGPT که زود به سقف محدودیت پیام می‌رسند، یک ترفند طلایی محسوب می‌شود!
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#ChatGPT
#Claude
#Gemini
#ChromeExtension
#Caveman
#PromptEngineering
#Tools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=ny46YyiPGygtHBYVzIcnP3pAoFO31kUMiMCHy8NLknjdwG-sAHsn6wo3-feaCiExtArVcIr_Mls0LvdYDojM8J-y-AbU1rI81RMJX9tfp1xlAO_bD24cw4pc_7YQMGx4bSt1ksxQGutw10Ak9iKmJ1eEcrCBBZzgNbZ5f7PfaL6wjEQbye_4oiY0OERjOesjdO51caJBFBtYzviaXcE9gvyFjKRMB4hWcJKbPCLdmGwUqljvxydOU9idRzCXAYiNcC0Le6rINSXvk3UDQOa1WAVTW8D-Pe68UUJPnQsJZvuybO7L6VN6p-q5HKMfARkPqrr09oq2rC7rbFrbdVtgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=ny46YyiPGygtHBYVzIcnP3pAoFO31kUMiMCHy8NLknjdwG-sAHsn6wo3-feaCiExtArVcIr_Mls0LvdYDojM8J-y-AbU1rI81RMJX9tfp1xlAO_bD24cw4pc_7YQMGx4bSt1ksxQGutw10Ak9iKmJ1eEcrCBBZzgNbZ5f7PfaL6wjEQbye_4oiY0OERjOesjdO51caJBFBtYzviaXcE9gvyFjKRMB4hWcJKbPCLdmGwUqljvxydOU9idRzCXAYiNcC0Le6rINSXvk3UDQOa1WAVTW8D-Pe68UUJPnQsJZvuybO7L6VN6p-q5HKMfARkPqrr09oq2rC7rbFrbdVtgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
ساخت دوره‌های آموزشی شخصی‌سازی شده با Gemini
🚀
✨
قابلیت‌ها:
•
🔹
طراحی مسیر یادگیری بر اساس هدف (مصاحبه، پروژه یا تحصیل)
•
⚡
تولید خودکار ساختار شامل سخنرانی، تصویر و کد نمونه
•
🛠️
شامل آزمون‌های سنجش یادگیری
•
📦
دسترسی رایگان و فوری برای همه کاربران
🌐
Site
#AI
#Education
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoTngDB1wf5oHl43yF-qmd7sVApwup4zn89cBDryZVTrJZaPHo2QB4zRZpEEzN5E8C2VzrZZFcjmlsu2cf4ESAEmGD_p3at3VvGpuKOLIQ4E8pBXGGsuG0ot7G-hGvuttzsoQe9885VaMkXycoDcCRSAINwCUBiQBE54Aa-8vIcSuN-J4ucb5Jj0_e9HpuqxsRJclg_B7eFExhBjUVccdEoEb8HolvNRfvUjgONiFpuW-xbgZ2iqScqkScHzLW7miRVld9Qpgj1r3fctTwHvk-iEGlK5Y3UPLtDhUW_MN11d9K-vk7JetaGfBR_xDWAaYdEpJVEuyP5IzQXQ5tI2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ویدیوهای یوتیوب را تا کیفیت 8K و بدون محدودیت دانلود کنید
🚀
✨
قابلیت‌ها:
•
🔹
دانلود ویدیوهای تکی و پلی‌لیست‌های کامل
•
⚡
پشتیبانی از کیفیت 144p تا 8K
•
🎧
خروجی MP4 و MP3
•
🛠️
ذخیره تنظیمات دلخواه کاربر
•
📦
دانلود دسته‌ای با سرعت کامل
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚀
Vibe
ابزار آفلاین تبدیل صوت و ویدیو به متن
🎙
✨
وایب برنامه کراس‌پلتفرم مبتنی بر
OpenAI Whisper
برای پیاده‌سازی متن فایل‌های صوتی و ویدیویی به صورت کاملاً
آفلاین
و با حفظ حریم خصوصی است.
🔥
ویژگی‌ها:
1️⃣
پشتیبانی از زبان‌های متنوع با قابلیت ترجمه به انگلیسی.
2️⃣
خروجی‌های متنوع: زیرنویس (SRT, VTT)، متنی (DOCX, PDF, TXT)، HTML و JSON.
3️⃣
پردازش گروهی، استخراج متن از لینک‌ها و ضبط مستقیم صدا.
4️⃣
بهره‌گیری از GPU برای سرعت بالا و پشتیبانی از CLI.
﻿
⚡️
مشخصات:
* زبان: TypeScript / JavaScript
* پلتفرم: ویندوز، مک، لینوکس
🔗
لینک
🔵
@ArchiveTell
| Bachelor
⚡️
#Vibe
#AI
#OpenAI
#Transcription
#Privacy
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
60GB
🧭
: حداقل 1 دعوت
👥
: 0/60
💾
: 60 GB
⏰
: 5 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌐
دامنه رایگان
eu.cc
با GNAME! (فیلتر شده ظاهرا)
فرصتی عالی برای ثبت دامنه رایگان
eu.cc
که برای ساخت سایت‌های سبک، تست یا پروژه‌های شخصی عالیه!
✨
ویژگی‌ها:
•
🆓
ثبت دامنه رایگان
•
🔄
تمدید رایگان سالانه
•
☁️
پشتیبانی از میزبانی Cloudflare (CF)
•
🎯
هر کاربر تا ۳ دامنه می‌تواند ثبت کند
•
💡
مناسب برای سایت‌های سبک، تست و پروژه‌های کوچک
همین الان دامنه رایگان خودت رو ثبت کن!
👇
🌐
Site
#دامنه_رایگان
#GNAME
#Cloudflare
#وبسایت
#هاستینگ
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚀
معرفی 1Hosts؛ سپر دفاعی پیشرفته شما در برابر تبلیغات و ردیاب‌ها!
🛡
✨
اگر به دنبال یک لایه امنیتی قوی برای مسدودسازی تبلیغات مزاحم، ردیاب‌ها (Trackers) و بدافزارها هستید، پروژه متن‌باز
1Hosts
یکی از بهترین و بهینه‌ترین فیلترهای DNS و لیست‌های مسدودسازی (Blocklists) در گیت‌هاب است. این ابزار از سال ۲۰۱۷ به‌طور مداوم در حال توسعه بوده و با وجود حجم کم، عملکردی بسیار قدرتمندتر از جایگزین‌های سنگین‌تر دارد.
🔥
نسخه‌های موجود در این پروژه:
🟢
نسخه Lite (متعادل):
ایده‌آل برای استفاده روزمره. این نسخه با کمترین میزان خطای مسدودسازی (False Positives)، تجربه‌ای روان از وب‌گردی به شما می‌دهد (نصب کنید و فراموش کنید).
🔴
نسخه Xtra (تهاجمی / Beta):
طراحی‌شده برای کاربرانی که به بالاترین سطح حریم خصوصی نیاز دارند. این نسخه به شدت سخت‌گیر است و هرچند بالاترین سطح امنیت را فراهم می‌کند، اما ممکن است عملکرد برخی سایت‌ها را دچار اختلال کند.
⚙️
پشتیبانی و سازگاری گسترده:
شما می‌توانید لینک‌های 1Hosts را به راحتی در طیف وسیعی از نرم‌افزارها و سرویس‌ها اضافه کنید:
مرورگر و شبکه:
uBlock Origin, AdGuardHome, Pi-hole
اندروید و iOS:
AdAway, Blokada, InviZible Pro, DNSCloak
سرویس‌های DNS:
همگام‌سازی آسان با NextDNS, ControlD و RethinkDNS
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
ارتقای رتبه هر سایتی در نتایج جستجو با کمک هوش مصنوعی!
🔝
✨
ابزار جدید و متن‌بازی پیدا کردیم که وب‌سایت شما را به صورت دقیق آنالیز کرده و به شما کمک می‌کند تا جایگاه آن را در نتایج جستجوی گوگل (SEO) بهبود ببخشید. پروژه
open-seo
یک دستیار هوشمند و همه‌کاره برای کارهای سئو است.
🔥
قابلیت‌های کلیدی این ابزار:
1️⃣
**تحلیل خودکار:** سایت شما را بررسی کرده و توصیه‌ها و پیشنهادات عملی برای بهبود سئو ارائه می‌دهد.
2️⃣
**رصد دامنه و رتبه‌ها:** وضعیت سلامت دامنه را بررسی و جایگاه سایت شما را در کلمات کلیدی مختلف ردیابی می‌کند.
3️⃣
**نظارت بر منشن‌ها:** اشاره‌ها و منشن‌های نام برند شما را در موتورهای جستجو زیر نظر می‌گیرد.
4️⃣
**اتصال به ایجنت‌های هوش مصنوعی:** پشتیبانی کامل از اتصال به Claude Code، Codex و سایر ایجنت‌ها از طریق پروتکل **MCP** (Model Context Protocol).
5️⃣
**اتوماسیون سئو:** دارای سناریوهای آماده برای خودکارسازی کارهای تکراری و زمان‌بر سئو.
6️⃣
**راه‌اندازی سریع:** به سادگی و تنها در عرض چند دقیقه از طریق **Docker** اجرا می‌شود.
🔗
لینک مخزن گیت‌هاب برای دانلود و نصب
🔵
@ArchiveTell
| Bachelor
⚡️
#SEO
#AI
#OpenSource
#Docker
#WebDevelopment
#Github
#Tools
#MCP
#SEO_Automation</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔥
🔥
ویژه
ساخت اکانت جیمیل بدون محدودیت سیم کارت، وریفای و ...
(تست نشده)
فقط روی ویندوز
github.com/ShadowHackrs/gmail-account-creator
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ویژه
🔥
🔥
🚀
تبدیل گوشی‌های قدیمی اندروید به سرور لینوکس یا هاب خانه هوشمند!
🐧
📱
اگه تو خونه یه گوشی اندرویدی قدیمی دارید که گوشه‌ای خاک می‌خوره، پروژه
Linux-Android
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار که به تازگی در گیت‌هاب ترند شده، یک اسکریپت ساده و قدرتمند است که بدون نیاز به روت (Root)، گوشی اندرویدی شما رو از طریق اپلیکیشن Termux به یک دسکتاپ کامل لینوکس یا سرور خانه هوشمند تبدیل می‌کنه.
🔥
امکانات و کاربردهای بی‌نظیر این پروژه:
1️⃣
نصب خودکار و بدون دردسر:
بدون نیاز به دانش فنی پیچیده، فقط با اجرای یک اسکریپت، لینوکس با محیط دسکتاپ دلخواه شما (مثل XFCE، KDE، MATE یا LXQt) نصب میشه.
2️⃣
تبدیل به سرور خانه هوشمند (Home Assistant):
می‌تونید گوشیتون رو به یک هاب مرکزی (Home Assistant Hub) تبدیل کنید تا وسایل هوشمند مثل لامپ‌ها و پریزهای وای‌فای رو کنترل کنه.
3️⃣
پشتیبانی از شتاب‌دهنده گرافیکی (GPU Acceleration):
با استفاده از درایورهای Turnip، گوشی‌های دارای پردازنده اسنپدراگون گرافیک بسیار روانی روی دسکتاپ لینوکس به شما میدن.
4️⃣
نصب ابزارهای کاربردی:
ابزارهایی مثل مرورگر دسکتاپ (Firefox)، پخش‌کننده ویدیو (VLC)، سرور SSH و حتی اجرای برنامه‌های ویندوزی با استفاده از Wine (به‌صورت اختیاری) قابل نصب هستن.
5️⃣
کاملاً ایمن و بدون نیاز به کلود:
تمام پردازش‌ها روی گوشی انجام میشه و نیازی به سرور ابری ندارید.
⚡️
این پروژه برای آموزش لینوکس، توسعه با پایتون و ساخت سرورهای خانگی فوق‌العاده است.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Linux
#Android
#Termux
#HomeAssistant
#OpenSource
#Github
#Python
#Tools
#TechHack</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚀
آموزش اجرای MiMo Code یک AI و ابزار کد نویسی کاملا رایگان و بی محدودیت
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب MiMo Code
curl -fsSL https://mimo.xiaomi.com/install | bash
4) اجرای MiMo Code
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس :
mimo
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر MiMo Code را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
mimo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWxrRJdB54Tp4iojPo0R6of1fOjJolwe1CdkxJvZcSlatiWTMQI2tbmykYMXSm01GIGVzp9gGUPWnx8wO5u0M8o8zDZ5W7CT35nsOxns7yiJJLbPfugIIhMl66fzu2rnNQGtFkb-H5tJmo_MqKvwSuDv_XCmK3xMqgzn33YyschMQlv3h1801rk7SJiweOmADoJfIObFxmwWClFbM0WQUuVhVi2KurEw8mt3HROcP1-hFb-0KAqSji4Ta-h9t8CZ8WZ09OkUplk-V_G7LeTgBOJ0KUgj5asrA-UtVypmGDe4MDT0LS_6iEENbK56e1AYvHoSlJJZu5Mo8-vYdzx2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
کتابخونه‌ای به وسعت ۱۱ هزار کتاب!  هوشمندانه جستجو کن و دنیای جدیدی از کتاب‌ها رو کشف کن.
✨
قابلیت‌ها:
•
📖
دسترسی به ۱۱ هزار کتاب با رتبه‌بندی و توصیه‌ها
•
🧠
جستجوی معنایی: «کتابی برای توسعه فردی» یا «متا فیزیک»
•
🔄
مشاهده نسخه‌های مشابه برای هر کتاب
•
🌟
مجموعه‌های پیشنهادی از افراد مشهور
•
📊
جمع‌آوری داده‌ها از کتابخانه‌ها، شبکه‌های اجتماعی و رسانه‌ها
🌐
Site
#کتاب
#کتابخوانی
#معرفی_کتاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIngc91iMBjixohA-wIMGGepOOQPhP_c2KuRkK4LWOmW0tyS3lw_L9QG0kfeUqtNLaT2K9X7FxXXZMObBQv4AeQuLvyAXOmbYB2KqoaPKyGcc-tcKht2D0fSvC5ucKD-Jk3QNetrIviRObrY9kWy5FvjFYz_2sVEcYnctskhKNyyYGvE0I5ZSeAF2x2DQCN-GVOL-uif8IHbGIwhgeDMp98W0jB3nVPzdIXm4I2RIjaeWtafA-nS66PBPp_3BvQfE7D0GMLtxkQYFTjk8Mtnl55ehb_NIBbbfG37wsWKljk8c2edDVLzT-VYDpnbGHdVAO8Mapl7EZhTXrkh19IFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_1pawoSklGVP-vfcnW6kAGuUqoj8ti32gA2rvFrCHh7RoUJGZXxThKAzSjMWwbIsgdM7It1v13GI3oLdJCw_2off6QNu0WJPGPyayLuu7Vc35_-aJc4OWUjdD95oxOUR8nkyvsk7hxrElCkp10HJ5pkjnJACggj2NtLF0DgVXw4vGLcZmbc7BW9Y3W__crvQRtPzNWTy6KUYFAyP9OYzrboqMN1l-A7ZmnRWDB5MNdYt0KmWaO7dSMVwA8CYxNTvhRdZUBVS0TvsYHjCL-CJ6C3bkuw_cdUrLKUHNRfi-GUY07J0tqCa5LInAIwEByBLzzQ74gHUKpYisH2jB3uHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qeZ9qp282cvh_v_938PJamE5OlDsJyEjkCdK-MiQSsTGlRkwjf3U96HIpsJvSAXZY1LX7MXHlHPICLc13v4-U35kDvJ5CBGYTnxyxA_y5ryphxCljHMCJ9fPONyLf-jSAk-VIAfAfCuI9ZfO0y9zYkX6jO9R_rhY_NVlOBrpt3XNVkDonga6OVOR3rGUn4z34lbPLepC8XrODXeH61dNUATka3l7ZIUevUZoinMETGi6R06YWecFkGFCC48dsxw0GO4fHeH2CWKBrSQ6752GeHwVZYB3ErtLOLZYMPLGNZqHMEYLKHgFz5-CAZXt_UsjIqA9rTuOv0qdgdUuzh_4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTDAJ-9tcHEmOYtsVwGuI_avEk1d7qAvBUKkbQDePbumr9UdAa6SJTtLaOVA-W7LJvpuIh2l4paZtmEcfbUM81VklernScq-90XZJ1rIZmQIkx4MAvCamU2Qje3hk6tXTu3JY6eDo76uQpmBt1uQfXEwSEq-ayGIkGVXyatTmkBHmMsX0I-DAC1B_mQjLudW_Ey2hPfozvn7E2YxQ79lVH3CEYmL1bRY0QjA2DRIcrVhxf9Y5vHPaw0hCGQtreXyDAbT7ycn0vMUhZ0Q4m8cetdbjEB-D8-wNqI4JNG1czzos5-LjoNpyNmU_tmFVVQLymtCJKgmiXlWTqpxgrrnxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🍿
نتفلیکس خود را بسازید — یک برنامه رایگان و متن‌باز برای تماشای فیلم‌ها، سریال‌ها و انیمه بدون تبلیغات مزاحم پیدا کردیم.
🔹
بسیار سریع‌تر از اکثر سرویس‌های مرورگر کار می‌کند.
🔹
امکان دانلود محتوا مستقیماً روی دستگاه را فراهم می‌کند.
🔹
از زیرنویس‌های فارسی پشتیبانی می‌کند.
🔹
بر اساس علایق شما توصیه‌ها و مجموعه‌هایی را ایجاد می‌کند.
🔹
برای راه‌اندازی فقط به یک توکن رایگان
TMDB
نیاز دارید که در چند دقیقه تهیه می‌شود.
🌐
GitHub
#OpenSource
#Streaming
#Entertainment
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">worker.js</div>
  <div class="tg-doc-extra">23.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سورس کد ربات تلگرامی برای چت با هوش مصنوعی بر بستر کلودفلر
🌐
ویژگی‌ها:
- گفتگو با مدل‌های GLM 5.2، Kimi k2.7، Gemma 4، GPT 4 و Llama
💬
- تولید تصویر با مدل‌های Lucid origin و Flux 2
🖼️
- تبدیل صدا و موزیک به متن با مدل whisper-large-v3-turbo
🎤
راهنمای اجرای این سورس در بخش کامنت های این پست ارائه شده است
👇
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚀
معرفی Save to Yaps؛ ابزاری برای ذخیره هوشمند و خصوصی مطالب وب!
🌐
✨
اگر از آن دسته افرادی هستید که همیشه ده‌ها تب (Tab) باز در مرورگر خود دارید، یا لینک‌های مهم را برای خود ایمیل می‌کنید و دیگر هرگز سراغشان نمی‌روید، افزونه
Save to Yaps
دقیقاً همان راهکاری است که نیاز دارید!
این افزونه یک "Web Clipper" فوق‌العاده است که هر صفحه وب را به یک یادداشت Markdown تمیز و خصوصی در کامپیوتر شخصی شما تبدیل می‌کند.
🔥
چرا Save to Yaps متفاوت است؟
*
تبدیل هوشمند محتوا:
مقالات را از شر تبلیغات، منوها، بنرها و پاپ‌آپ‌ها پاکسازی کرده و فقط متن اصلی را به عنوان یک یادداشت تمیز ذخیره می‌کند.
*
ذخیره سریع تصاویر:
با قابلیت Hover-to-save (نگه داشتن موس روی تصویر)، می‌توانید عکس‌ها را به سادگی به یادداشت‌های خود اضافه کنید.
*
حریم خصوصی مطلق (Private by Design):
برخلاف سرویس‌هایی مثل Pocket یا Evernote، در این ابزار هیچ اطلاعاتی به سرورهای ابری ارسال نمی‌شود. همه چیز به صورت محلی (Local) روی کامپیوتر شما ذخیره می‌شود.
*
کارکرد آفلاین:
حتی زمانی که به اینترنت دسترسی ندارید، می‌توانید یادداشت‌های خود را ذخیره و مدیریت کنید.
*
سازگاری:
روی تمام مرورگرهای مبتنی بر کرومیوم از جمله کروم، اج، بریو و آرک قابل نصب است.
💡
نحوه استفاده:
برای شروع، کافی است اپلیکیشن دسکتاپ رایگان Yaps (برای مک یا ویندوز) را از
اینجا
دریافت کنید، افزونه را روی مرورگر نصب کرده و با یک کلیک، مطالب مهم را به "Second Brain" یا همان پایگاه دانش شخصی خود منتقل کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#Yaps
#WebClipper
#Privacy
#Productivity
#Markdown
#KnowledgeManagement
#TechTools</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx_NkLHge9ZZ_U5o3UqkniiiFiWY85cE9bykChbW4gsYJW86ijQcM2l3jHioP_L4Dh75a4Mv1E66BRczCPVpQbfOGQs_fVXWRO1KMAcL74SLB-7iuUtpbrJ6_YcqacmzjGU8fSRzskuRSqK_s5x_DqEkJVNQxzT6MBITBtp_FyssmrFXkr-aHzQPNhSlPQwepKawfr7DFwcgElsHmOsDRpkEknD32GdBFuR-IRFF_ht6zGQ-n7sgZLF3Y5PZULg3iAHLE6ZnBZ96XwiTb8NnTCfUZkz9ZPJe-o1VwuWxfmennK0J1MuG-Ts_Uxb7IHW_9T3JurdJQ78DJNnTiZFJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش در سطح MIT و هاروارد رو رایگان تجربه کن!
🎓
بیش از ۱۷۰۰ دوره از بهترین دانشگاه‌های جهان حالا در دسترس شماست.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان به دوره‌های برتر جهانی
•
📚
شامل برنامه‌نویسی، ریاضیات، طراحی، کسب‌وکار، فلسفه و علوم دیگر
•
📹
محتوای کامل: ویدئو، جزوه، تمرین و امتحان
•
💡
مناسب برای یادگیری از صفر تا پیشرفته
•
🔸
یکی از بزرگترین آرشیوهای باز آموزشی
🌐
Site
#Education
#FreeCourses
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPkKYujHDnFlPiCPZw4qzCtWHgxJkZ5DYmrUOpWNgaOVGVozUaEOR0Hx1eFCwI7V9fVwGK0QCOeTohAIW8Pq0q_XakNhxzPVI-YAKVIHyXejTbEzEUZ9fb9sT7P7wsi97D1AbiQts_xgMOwjjSwAUkIErOFDO_UsAWtb9ZGFPyl5jpi0QodHNiJ9ju8ykwC8AaOY4stuo0mny6kQF4OTHNtrSZGFAp1Gb2F7ed4K12_hGaPCek1i4MVhVGRuuD4n2B5QkmpLgw2Cwm8N5KkmSUoyFRY28o2T2kl470hfPWgZclZ6vdXCT5RCmaXRUsr065PKkoXYnyBZJwS1jiuPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsibpR26M3vLrqXXCDbPi0IbelLczkGP2G_SKlncvP3jhBUCkam4QQcgFdYpnHIoYXm9Zsq4QnGEDSq0PcTPfcwNfPz4KyJFs__15AtBugAT2xoVdUKxlkaHMVbJkYABC8uU-eLG6nFfTMkmfWDAuigzjmj328-VbaxhBGQaZqF_tXm1Hczq0Kw-yqQ7drOLXf0HGJaPUFX7IJ3VwLtrgcNNoKIe1kix2vbquZRd_flod3AQAQ5Zba2Uz5jG0JAlUg2jA9UwMK3kIyRNSvoNEiwyn6GQ-sZPgMRs9D1vv-qrwYL4vu66tF5SkW9qMg-O5JIkak7JyXZauiM9w2c_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivyPGafAQZwr-yTlchKAx2mfhb1sAb2gbmWGW24pOI9AP1blEppyondZMjeJDq1iWDkqb1sR7_SRIo1kFQlMqL3_BrSFLek_lP2ughc7by7V7ZPbtq5Qv3Udnq1WVh-8Cm62O7lre3gx_rhZSarcA03qy7V8Puy7X8znCYnADTvC2Jv2-ocL3Kx0dJJWVoW-lKUx8Xwv4VEEe-NqGlEzaGTyIorACf-r7vCcL8Pk9Q1lYfmXunX9w3i7RKOHuFjaRWWsIvBDQEQSz9Z-VtPvbqWU8wYCsahG9LAVNEWjtmxcJR3VT2K0ryvpS8vQdMzp5rlb2-kIAoPCuczoHMdx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/untQup5VVG8sJnUzLkDIJnnACc3oUGJpXZVg7L8v3bafVJcS6aPe9-vSHm9OCP0MRxAoKWnViEL5QExDRC99xJ8OqRfYE1eidkC6WDxvUqAHvbNJCaDNDfgibmHOaAHcpmK6-Mjue4Z65O-LV0mPjMGLOl-9iYrGXreWiE88daUSi7qDdnskofEfzB5qfcN84G1eXU9AsZrnxvtmz17v8MuUfb8POQzW7KdQ9VoRnKD4W_C4zwcBlkRXgTsxydNn1_qsfjuhenDwc69ncXV5jDmGqHwG5E623UAa5H27eLwa1gwTxtA4wepF9QbTX_q19SAZey4s3DqHKeyTeTceOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsS9JSznzP4MJVGGtMi2hvUhej6hY7zmZoVa1FtywWan4d2oyR-CYnPrNewC-KoikuZEvU_P18MSFSI53Ine0ZkrnoehMPiFi40uOCSqURAbR_sAYlQcrTaaqi7Ew6XUVHKlJidh2uc-DtcaLdztcUZx_7jgQ9OoYdRqmhvSO7jGTP3a_jgxVHG2MDN_89V6Xkkl-jiY7aisQTkidFPEQCMWudg_H1mkYapK_Pb3LRPtjQTqoon3rXTmWZ4d53_LNRPfqmGMmfN48zBsAm705x_ZrymUlLmLJyfLi98KYr7J19oF6eASYl4Ggw9Sw3frUNp3Ly_x-SaXD3a-3FCE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u21YR98feplUsLBioCfXlvNYEMUtueil53y9kxHIsnih5zZb2ak1ruOYTuDKDvDAw0npxnpHuh8SFHLhDcysAHbP5mPDQFaRIdk7RJPGYjUcRD_3uUtUGWQ6h3dia2QwzyCAYY59ZGPYziurDrKNLc56qoxE5zijGGFXP944F72_et_ZPgEJW4tinmBOiGKFJWWYr1VOxMKVCCnhpR42FBa9uVEOvVQCQnHMHHwDxBVySH801vdrzSaCPqsxSjCX4ONVNu-BEA_aEPsikq0sHy3ipoigC4fwVz97GQCvaLuwEP0ujMo_OszUv61Xzuo3RsnEN8W1HQ-syeP0uzHdTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsS_i5pEpmOX_enq09Fv5pN6ywieoY61bxNA9UE_dR0oQPtqfJRo3hHpiPqiuGKUjA5tUlI8sgJoSH4Vzgu2Ma7AoFTDAlWKOYdroWwju0Rxgr5Ev97x0PQ1VpBP0vzp9KXkEbVJ3EKFfLO8KLX1G47kFzUudj02ICoakuPy1-vzoKv4bxTCKp5C3ZF4vrvprPInJFPVpWj4uhAmZs9ab1XLzdPOvMF0gbdHs-vd-q_jo27SwWua02X3NkHZbp8h275xNglYW3bGeYfqO6E0VMtOBkBwEg4yD8jlWGUMsu3hvhUd6xaT2AOz_oIUoxcx-_qw8H3rcpAcVLI152eMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر تورنتی که بخوای رو پیدا کن!  با "EXT Torrents"، یک موتور جستجوی قدرتمند و رایگان، به دنیایی از محتوا دسترسی پیدا کنید.
✨
قابلیت‌ها:
•
🔹
آرشیو عظیمی از فیلم، سریال، انیمه، موسیقی، بازی و نرم‌افزار
•
⚡
جستجوی سریع و دقیق با کلمات کلیدی
•
📂
مرور دسته‌بندی شده و رتبه‌بندی محبوب
•
🔗
پشتیبانی از کپی مستقیم مگنت و دانلود فایل تورنت
•
🆓
رابط کاربری ساده و بدون نیاز به ثبت‌نام
🌐
Site
#Torrent
#SearchEngine
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚀
معرفی winpodx؛ اجرای اپلیکیشن‌های ویندوز در کانتینرهای لینوکس!
🐧
✨
اگر نیاز دارید برنامه‌های ویندوزی را در محیط لینوکس اجرا کنید اما نمی‌خواهید درگیر سنگینی و کندی ماشین‌های مجازی (VM) شوید،
winpodx
راه‌حل جایگزین و هوشمندانه شماست. این ابزار به شما اجازه می‌دهد برنامه‌های ویندوزی را درون کانتینرهای ایزوله در لینوکس اجرا کنید.
🔥
ویژگی‌های کلیدی:
*
بدون نیاز به ماشین مجازی:
اجرای مستقیم و ایزوله در کانتینر با عملکرد بسیار بالاتر.
*
پشتیبانی منعطف:
اجرای نسخه‌های مختلف ویندوز در محیط کانتینری.
*
توسعه‌یافته با Python:
ابزاری سبک و قابل سفارشی‌سازی برای سناریوهای مختلف.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#winpodx
#Linux
#Windows
#Docker
#Python
#Containers
#DevOps
#OpenSource</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
معرفی AI Website Cloner Template
این پروژه یک قالب حرفه‌ای برای
تبدیل هر وب‌سایتی به کد مدرن (Next.js 16 + React 19 + Tailwind)
با کمک ایجنت‌های هوش مصنوعی است.
قابلیت‌ها:
*
مهندسی معکوس هوشمند:
تحلیل سایت، استخراج توکن‌های طراحی (رنگ، فونت) و ساخت کامپوننت‌های دقیق.
*
سازگاری بالا:
پشتیبانی از ایجنت‌های معروف مثل Claude Code، Cursor، Windsurf و Gemini.
*
تکنولوژی روز:
خروجی تمیز با Tailwind CSS v4 و استانداردهای strict TypeScript.
کاربرد:
بازسازی پروژه‌های قدیمی خود یا یادگیری نحوه ساخت کامپوننت‌های پیچیده وب‌سایت‌های حرفه‌ای.
🔗
مشاهده در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=uQTvjsdC6sq8Djk3Ykvrz82QGz56yVdMWlHns4DWWj3_-nIiBEIxAzgr4uIT3O2e1FT9zJfOLv-_7QOIdFishgw4R2tsQPzC2vIsFTkzWrYDDcVU70-YzHoRrsJdfix_bbuxS0woY8UpbDQmabebgjnxFMCUrQj4e_EDuuybqxSYToIK03CKxJIao1ls1CYNQtu8UFqM3l_-SQaZCsbVNgbXOnAXYLiEkj8Q8UUBbeMcBML8xWxsTzN43Smw1C_oUgSSRwlaeeoHNYV9PNFdnFRadqprErnuJ1hxnVu2IgPqFZZa8kXmn0pibM3Na93kmt_vlSyHhQmQXNkqKBPdrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=uQTvjsdC6sq8Djk3Ykvrz82QGz56yVdMWlHns4DWWj3_-nIiBEIxAzgr4uIT3O2e1FT9zJfOLv-_7QOIdFishgw4R2tsQPzC2vIsFTkzWrYDDcVU70-YzHoRrsJdfix_bbuxS0woY8UpbDQmabebgjnxFMCUrQj4e_EDuuybqxSYToIK03CKxJIao1ls1CYNQtu8UFqM3l_-SQaZCsbVNgbXOnAXYLiEkj8Q8UUBbeMcBML8xWxsTzN43Smw1C_oUgSSRwlaeeoHNYV9PNFdnFRadqprErnuJ1hxnVu2IgPqFZZa8kXmn0pibM3Na93kmt_vlSyHhQmQXNkqKBPdrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡
یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده.
این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway
را فراهم می‌کند.
از طریق خود ربات می‌توانید:
✅
پنل موردنظر خود را بسازید
✅
مصرف و وضعیت منابع را مشاهده کنید
✅
دامنه شخصی خود را برای پروژه متصل کنید
✅
آی‌پی تمیز را مستقیماً از طریق ربات دریافت کنید
هدف 𝗥𝗘𝗡 ایجاد یک روند ساده‌تر و خودکار برای مدیریت پروژه‌ها و سرویس‌هاست.
🤖
ربات
💻
سورس پروژه
━━━━━━━━━━━━━━
👨‍💻
توسعه داده شده توسط 𝗔𝘀𝘀𝗔
دوستان اضافه کنم اگر رندر شما ساسپند شد اکانت رو حذف کنید و دوباره با همون ایمیل یا گیت هابی که داشتین ثبت نام کنین مصرفتون ریست میشه
برای حمایت از پروژه star بدین
❤️
(در گیتهاب ترجیحا
😂
)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVcF5J5CXbBrgCanfUBcOQHtZWS32RsnySfVwkYj2bkg1jHw8Nunngbg9rACLYYaJsg3rhNy9ALqkZdF_jOXH7OgVw9DXb101g5vnsEVPezhMeT3INevP71iQ6u0xCvJ9VWC1AO44wSHSml2oYVJUi40O1d2s2cDofgArQWJVzPHK8UxkfqzEyq5mFZ81T7nf1ijLUwwrETCe8dYOLs5M5TJvMA5vxkZ6okpj0TeXvrsR9eSUhsLZGkYKdidtI1wjyVm9y8XqZG8x6uAH9h4u4yC60rr1KaVhrehlon8WwpYzQMNT6hMNRVKueeuBWWDg4ULgpIAd2LCsnj8l0H6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی shadPS4؛ سریع‌ترین شبیه‌ساز کنسول پلی‌استیشن ۴ برای کامپیوتر!
🎮
✨
اگر به دنبال اجرای بازی‌های PS4 روی سیستم خود هستید، پروژه
shadPS4
یکی از فعال‌ترین و سریع‌ترین پروژه‌های متن‌باز (Open-Source) در دنیای شبیه‌سازی است که با زبان C++ نوشته شده و با سرعت خیره‌کننده‌ای در حال پیشرفت است.
🔥
چرا shadPS4 در حال حاضر ترند شده است؟
1️⃣
توسعه روزانه:
این شبیه‌ساز تقریباً هر روز آپدیت می‌شود و بیلد‌های جدیدی برای سازگاری با بازی‌های بیشتر منتشر می‌کند.
2️⃣
پشتیبانی چندپلتفرمی:
به راحتی روی
ویندوز
،
لینوکس
و
macOS
اجرا می‌شود.
3️⃣
رشد سریع:
در تاریخ اخیر شبیه‌سازهای کنسول، shadPS4 سریع‌ترین روند بلوغ و افزایش سازگاری با بازی‌های بزرگ (Major Titles) را داشته است.
4️⃣
جامعه کاربری فعال:
با بیش از ۳۱ هزار ستاره در گیت‌هاب، این پروژه به یکی از محبوب‌ترین ابزارهای گیمینگ در اکوسیستم متن‌باز تبدیل شده است.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#PS4
#Emulator
#Gaming
#OpenSource
#Github
#Cplusplus
#RetroGaming</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚀
معرفی OpenSERP؛ دسترسی رایگان به API موتورهای جستجو (جایگزین SerpAPI)!
🌐
✨
اگه برای پروژه‌های هوش مصنوعی، سئو (SEO) یا اتوماسیون خودتون به دیتای موتورهای جستجو نیاز دارید و نمی‌خواید هزینه‌های سنگین برای خرید API بپردازید، ابزار
OpenSERP
دقیقاً همون چیزیه که دنبالشید! این پروژه متن‌باز (Open-Source) دسترسی کاملاً رایگان به نتایج Google, Yandex, Bing, Baidu, DuckDuckGo و Ecosia رو از طریق API فراهم می‌کنه.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
بهترین جایگزین سلف‌هاست:
یک جایگزین رایگان و قدرتمند (Self-Hosted) برای سرویس‌های پولی و معروفی مثل SerpAPI, DataForSEO و Tavily.
2️⃣
خروجی مارک‌داون (Markdown):
قابلیت استخراج دیتا از سایت‌ها و نمایش نتایج جستجو به فرمت Markdown (که برای پروژه‌های RAG، ایجنت‌های هوش مصنوعی و LLMها یک ویژگی طلایی محسوب می‌شه).
3️⃣
جستجوی ترکیبی (Megasearch):
این قابلیت به شما اجازه می‌ده تا یک کوئری رو به‌طور همزمان در تمام موتورهای جستجو سرچ کنید و نتایج تجمیع‌شده رو تحویل بگیرید.
4️⃣
کاربردی برای همه:
ابزاری بی‌نظیر برای متخصصین سئو، توسعه‌دهندگان، برنامه‌نویسان وب‌اسکریپینگ و فعالان حوزه هوش مصنوعی.
⚙️
این ابزار رو هم می‌تونید خودتون هاست کنید و هم از نسخه تحت وب و آماده‌ی اون استفاده کنید.
🔗
لینک مخزن گیت‌هاب
🔗
نسخه آماده و تحت وب
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenSERP
#API
#SEO
#WebScraping
#LLM
#RAG
#OpenSource
#Github
#Tools</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
آموزش دریافت یک ماه اشتراک رایگان Duolingo Super!
🦉
✨
اگه از برنامه دولینگو برای یادگیری زبان استفاده می‌کنید، الان می‌تونید با یه ترفند خیلی ساده و جذاب، یک ماه اشتراک پریمیوم (Super) این برنامه رو کاملاً رایگان دریافت کنید و از شر تبلیغات و محدودیت‌های جون (Heart) خلاص بشید!
🔥
مراحل دریافت اشتراک:
1️⃣
نصب اپلیکیشن:
ابتدا
اپلیکیشن Webtoon
را دانلود کرده و یک اکانت جدید در آن بسازید.
2️⃣
جستجو:
در نوار جستجوی برنامه، عبارت
Duo Leveling
را سرچ کنید (این کمیک مشترک دولینگو و وبتون است).
3️⃣
اسکرول کردن:
سه قسمت (اپیزود) از این کمیک را باز کنید. (اصلاً نیازی به خواندن نیست، فقط کافیه صفحات را تا انتها به پایین اسکرول کنید!).
4️⃣
دریافت کد:
بلافاصله بعد از انجام این کار، یک کد فعال‌سازی رایگان Duolingo Super به شما داده می‌شود.
👏
5️⃣
فعال‌سازی:
حالا وارد لینک زیر بشید، وارد اکانت دولینگوی خودتون بشید و کد را وارد (Redeem) کنید:
🔗
ورود
🎉
تبریک! اشتراک یک‌ماهه شما فعال شد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Duolingo
#DuolingoSuper
#Webtoon
#FreeAccount
#LanguageLearning
#Tricks
#Education</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚀
تبدیل عکس شما به مینی‌فیگور واقعی لگو (LEGO) با هوش مصنوعی!
🧱
✨
دوست دارید بدانید اگر یک کاراکتر لگو بودید چه شکلی می‌شدید؟ با استفاده از تولیدکننده‌های تصویر هوش مصنوعی و یک پرامپت (دستور) مهندسی‌شده، می‌توانید هر عکسی را به یک رندر سه‌بعدی و فوق‌العاده جذاب از مینی‌فیگور لگو تبدیل کنید!
🔥
ویژگی‌های این استایل جذاب:
1️⃣
حفظ هویت و جزئیات:
لباس‌ها، مدل مو، رنگ مو، حالت چهره و حتی اکسسوری‌ها کاملاً شبیه عکس اصلی شما بازسازی می‌شوند.
2️⃣
رندر فوق‌واقع‌گرایانه (Photorealistic):
اعمال بافت پلاستیک براق لگو، درزهای قالب‌گیری و نورپردازی استودیویی که باعث می‌شود تصویر کاملاً شبیه یک اسباب‌بازی واقعی به نظر برسد.
3️⃣
رعایت دقیق تناسبات:
سر استوانه‌ای، دست‌های گیره‌ای کلاسیک و بدن بلوکی شکلِ استاندارد لگو.
👇
پرامپت (دستور) برای استفاده در Midjourney یا DALL-E 3:
کافی است عکس خود را در هوش مصنوعی آپلود کنید و دستور زیر را به آن بدهید:
>
Turn the person in the uploaded image into a realistic LEGO minifigure, preserving their individuality, clothing, hairstyle, hair color, facial expression, and accessories as much as possible. The character must match the proportions of a LEGO minifigure: a cylindrical head, simple facial features, a blocky torso with printed clothing details, standard LEGO arms and hands, and a molded plastic hairpiece. Use realistic LEGO plastic texture with a glossy sheen, molded seams, and studio lighting. Plain white background, full body photorealistic 3D render from head to toe.
💡
نکته کاربردی:
این ترفند برای ساخت عکس پروفایل‌های بامزه، آواتارهای تیمی و پست‌های خلاقانه شبکه‌های اجتماعی بی‌نظیر است!
🔵
@ArchiveTell
| Bachelor
⚡️
#LEGO
#AI
#Midjourney
#DALLE3
#Prompt
#PromptEngineering
#3DRender
#Avatar</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzOwkP_O9KTLgVKqlRldS4v-6WXW0UiK8bynEpfbkRCSvLXqZHjMZlbMDeD-r1ujYSB0MpsF5rEBjnnK8XO4FoRW7IyClSizU2UWZNcUgolCJHaYP-U0xXYNWtyjZ4KYhpdirzyT69fEm66slf9DZQdGCNJjCNAI7EFoZhrnvz9Y-7rcmQfBhxychFgp809C0s5Im-CJxIP6Y6gOmQQ3Oiond05brcx_p0Jt3ttZgaieuBZEqf7mjlM3zmncwnCoCJqViz9dK46SkHBudB5iofhQNDsQk3J_xJJT734cfIdMraP1V1ATMAEHVI4Nri3iBtzB5N9JCgAe0IgfSqe-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی پریمیوم با مرورگر tabbit
🤯
ChatGPT 5.5 Pro
Gemini 3.5 Flash
Claude Opus 4.8
و بیشتر
در دسترس برای
macOS
و
ویندوز
مرورگر را نصب کنید و استفاده از جدیدترین مدل‌های هوش مصنوعی را به صورت رایگان شروع کنید!
🌐
Site
#Ai
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX2_734BITRManGzSAFbgEfnvPAI9_vDuzM83k3xa-yJQV5Td2kHxEfFgDax_HOu70FuRXORARdHRpXMWWjFuI2jO5kkY04Wh4prICW9ndMXkt8GTmyD9uJ8FS0P79b1MYLaNFoYX4lYRUF59KLyh0nZ-BJDBmiVJ7lyWnDfcZ03_KwPYyQC0HJTUc0Cm5NGIcVFwVziPS8Es8nico0Gihb3spbrFLeOHVMcwRrFKxk4sod6KNVFrFor5T1IA1OrTE-e6l-d4w-PQEJcHOe-vyW5ikBiwwsBbkIPZzRLZNE4MCZJnU-7k9ydjZo78YYvUDtRRHbtHdFyVKC_C-eqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها مدل Qwythos-9B-Claude-Mythos-5 را معرفی کردند که بر پایه Qwen3.5-9B است و قابلیت پردازش ۱ میلیون توکن را دارد!
🤯
✨
قابلیت‌ها:
•
🧠
تنظیم دقیق بر اساس ترکیبی از Claude Mythos و Claude Fable.
•
📚
پنجره متنی گسترده تا ۱,۰۰۰,۰۰۰ توکن!
•
🌐
انتشار کاملاً متن‌باز
•
✍️
همه‌کاره برای کار با متن، کد و اسناد طولانی.
🌐
Site
#OpenSource
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWpZwbeoc742bL9MBCn9ftxTrC1LcPmjAwe8Ujz5MApPOZqD3efaes5bwpFHUYs3IjkSqOOi6r8ccapTg5j-ozz14RK39ET3XV5TZs8eZhiIeStrxj3Y72OPC8NuW0h9Fk9kI8F_ukmc8l1aD5Xl2XpFz4_EyWa_LnleU-d5Zyq_POMjJs9XhoFaUxwPUAXNNQRV0ka-83k33cI-j8xRSr9tyaj6CGTDiCAr2QusLDQbADqWWOKZdK_qNOr39g6WFSi13oaB4LscweTBtKBbKx2ULKtZjne9AKbItqnfXzr_RT7gfkEB91cpFuqyQuIDt4-wLFcqqzqMpx6Ea5lqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=aITHswUiCw053nEKOO9nM3tIoZDBHxEG95Dh1ND9IchVa4xvQZ2Ll0QDWYTkfRrzPQ359xb-iBxiU8GK3_AS1U8HL0MY9n5HUC68B3KnLTHyek_LIl1Ua4yMtPJJzC1yZPYygXljoXWR6jzYRI8Lj7UbwWMKxZL6Pf0MUnk6z8IV7Xt6jSBuxP_DhsS7SWrcxyj_FvpsbzAPRiRhZ_fH6a_6AyAJYQfMCRR5newAx34hNDqwFvwsL3i1l0CZcND9Xbi87rtCVJWYhLbNghDSgoIsUsWy9NGoj8a6362DW5THXU1VaJFzsICyvxaluXQiFNsRjpp5FDVEh_oG6G1Hhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=aITHswUiCw053nEKOO9nM3tIoZDBHxEG95Dh1ND9IchVa4xvQZ2Ll0QDWYTkfRrzPQ359xb-iBxiU8GK3_AS1U8HL0MY9n5HUC68B3KnLTHyek_LIl1Ua4yMtPJJzC1yZPYygXljoXWR6jzYRI8Lj7UbwWMKxZL6Pf0MUnk6z8IV7Xt6jSBuxP_DhsS7SWrcxyj_FvpsbzAPRiRhZ_fH6a_6AyAJYQfMCRR5newAx34hNDqwFvwsL3i1l0CZcND9Xbi87rtCVJWYhLbNghDSgoIsUsWy9NGoj8a6362DW5THXU1VaJFzsICyvxaluXQiFNsRjpp5FDVEh_oG6G1Hhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗿
افزونه Caveman پرامپت‌ها و پاسخ‌های هوش مصنوعی را فشرده می‌کند
به‌طور خودکار کلمات اضافی را از درخواست‌ها و پاسخ‌ها حذف می‌کند و در عین حال معنی را حفظ می‌کند. با ChatGPT، Claude و Gemini کار می‌کند.
نویسنده ادعا می‌کند که این افزونه می‌تواند مصرف توکن‌ها را تا ۷۵٪ کاهش دهد. ایده ساده است: کلمات کمتر یعنی هزینه کمتر، و معنی باقی می‌ماند.
🌐
افزونه
#Caveman
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚀
معرفی Firecrawl؛ قدرتمندترین API برای جستجو، استخراج و تعامل با وب در مقیاس بزرگ!
🔥
✨
اگه توسعه‌دهنده، محقق هوش مصنوعی یا دیتا ساینتیست هستید و نیاز دارید اطلاعات سایت‌ها (حتی سایت‌های پیچیده و مبتنی بر جاوا اسکریپت) رو برای مدل‌های زبانی (LLM) یا دیتابیس خودتون استخراج کنید، پروژه
Firecrawl
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید!
🔥
امکانات بی‌نظیر این ابزار:
1️⃣
استخراج هوشمند (Scrape):
تبدیل هر URL به فرمت‌های تر و تمیز مثل Markdown، HTML، اسکرین‌شات یا JSON ساختاریافته در سریع‌ترین زمان ممکن (میانگین ۳.۴ ثانیه).
2️⃣
پوشش ۹۶ درصدی وب:
به راحتی از پس سایت‌های سنگین JS-heavy برمی‌آید.
3️⃣
خزش و نقشه‌برداری (Crawl & Map):
کشف آنی تمام لینک‌های یک سایت و استخراج کل صفحات آن فقط با یک درخواست (Single Request) یا به صورت گروهی (Batch).
4️⃣
عامل هوش مصنوعی (Agent & Interact):
فقط کافیه به زبان ساده توصیف کنید چه دیتایی نیاز دارید تا Agent این ابزار سایت رو بگرده، باهاش تعامل کنه و دیتای مورد نظر رو جمع‌آوری کنه.
5️⃣
متن‌باز و خوش‌ساخت:
هم به صورت سلف‌هاست (Open-Source) و هم سرویس ابری قابل استفاده است و پکیج‌های آماده برای Python و Node.js دارد.
🔗
لینک سایت رسمی:
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Firecrawl
#WebScraping
#API
#AI
#OpenSource
#Github
#Python
#Nodejs
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=vhUMGdlzuM4eymzBOLw2EaNbEQsrcaSHf2MQdjzyKsosAqVwBEHSwW2NxJX47165y9fCtF16fsJfPFDPXaSA6gfwRQ9blQmkjZrc-CwhMEcq8439GZ1wurBfdSOgOgLxr6Rko-5M8cClxZZddRzmWBFbmK_185ffYnt7EV9b7Eu4Z6zbIZqRNn90YqdrIXewMtj_np-XjFbBJWGq99Ivpo7dppBwuZ-Bo2SiK67HO5IsvJPL009Zmc5VsymMep2-SJPDy0yNfF2AUPj0c-2u-0Ge6pe1CI35ppxUK529DgutdNTFVP3RsaSRqzYgfjKZUp4Vete7gFXSwalbJlGcvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=vhUMGdlzuM4eymzBOLw2EaNbEQsrcaSHf2MQdjzyKsosAqVwBEHSwW2NxJX47165y9fCtF16fsJfPFDPXaSA6gfwRQ9blQmkjZrc-CwhMEcq8439GZ1wurBfdSOgOgLxr6Rko-5M8cClxZZddRzmWBFbmK_185ffYnt7EV9b7Eu4Z6zbIZqRNn90YqdrIXewMtj_np-XjFbBJWGq99Ivpo7dppBwuZ-Bo2SiK67HO5IsvJPL009Zmc5VsymMep2-SJPDy0yNfF2AUPj0c-2u-0Ge6pe1CI35ppxUK529DgutdNTFVP3RsaSRqzYgfjKZUp4Vete7gFXSwalbJlGcvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی KanaiAI؛ چیدمان مجازی مبلمان در خانه شما بدون نیاز به حدس و گمان!
🛋
✨
اگه از اندازه‌گیری‌های دستی و خسته‌کننده برای خرید مبل و وسایل دکوراسیون کلافه شدید،
KanaiAI
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار هوش مصنوعی به شما نشون می‌ده که هر وسیله‌ای دقیقاً چطور در فضای خانه شما قرار می‌گیره.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
مدل‌سازی دقیق:
اسکنر هوشمند این سرویس، یک مدل کاملاً دقیق و سه‌بعدی از اتاق یا محیط خانه شما می‌سازد.
2️⃣
خداحافظی با متر و اندازه‌گیری:
دیگه نیازی به محاسبات و درگیری با ابعاد نیست؛ هوش مصنوعی خودش پارامترهای وسایل مورد نظرتون رو با فضای خالی اتاق تطبیق می‌ده.
3️⃣
تجسم واقعی پیش از خرید:
مبلمان و وسایل جدید را قبل از اینکه پولی بابتشان پرداخت کنید، مستقیماً در دکوراسیون منزل خود ببینید!
🔗
لینک ورود به سایت
🔵
@ArchiveTell
| Bachelor
⚡️
#KanaiAI
#AI
#InteriorDesign
#TechNews
#SmartHome
#Architecture</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaGAzjwWhD7rnAkZiOkm93BL2lOnY7NvPORcj0ZQ1O10LRABn-qk-SzYSimZtPQBm5EO31_O5Q5XqwSGgC3GuQaCx8MzVyXJapzowkhQbdBRTFdwozWSd5z9UDHWdPMZBHRVHSN3aSIKMESAXdvxr0XMeMZ7LBSaKeMt58pFUkufgWvWdGokSTXlfoYvwx0IaWnyTNQRo8ao5VWbxcYx2dwp1Os6KRYYMdG9iISFpky5E6TQZeqSTPNl_vGTVt0aWo5_1NVCoW3F23eeWu6AFNtLLqi5MRhuTLWFxImnGJGI4d8TV5ZsZ0eituPxIpW1X1k5ASzxXZH5KjhLxEsByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
Navidrome — اسپاتیفای شخصی خودت رو بساز!
سرور موسیقی رایگان و متن‌باز که کامپیوترت رو به یک مرکز پخش موسیقی خصوصی تبدیل می‌کنه.
☁️
✨
چرا عالیه:
•
🏠
رایانه شخصی = مرکز موسیقی خصوصی
•
📱
دسترسی از هر دستگاه: اندروید، iOS، وب، پلیرها
•
☁️
پشتیبانی از فضای ابری — لازم نیست PC همیشه روشن باشه
•
🍓
اجرا روی سخت‌افزار ضعیف
•
🎚️
کنترل کامل — بدون سانسور، بدون محدودیت
•
💸
کاملاً رایگان — بدون اشتراک
🌐
Site
#Navidrome
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=O4DGgv6VrZYRgYakmT7QMbCEchQW5reSENutAGjQFVyn4hdhe4bN8QpsIq9dydSZ-o23oeuUGcJho9oUqMfJGfkxlRdjUKBY4sPsSw4U_uQHjJhKROoPLc5jNKd29e9YQ6k9om16QUA1i8WFrEDHoK5ut0Ndlmqjo8BC8lww3AH0pgoLj73pd2qmyYoyYZVutDtt3-1PXGx-xR7997tJlLvGsOi9uEK-XxnavZ65Bd7fkCvNJfMZEyYLT8XgvdWbfudF2wN6qscyL_LmVg7vOlf-cJ0UKp0zBPuPdJYEqoI_e85n46q2K_9SADf1eT68oTlrMawFXs-JS9w8R-_SuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=O4DGgv6VrZYRgYakmT7QMbCEchQW5reSENutAGjQFVyn4hdhe4bN8QpsIq9dydSZ-o23oeuUGcJho9oUqMfJGfkxlRdjUKBY4sPsSw4U_uQHjJhKROoPLc5jNKd29e9YQ6k9om16QUA1i8WFrEDHoK5ut0Ndlmqjo8BC8lww3AH0pgoLj73pd2qmyYoyYZVutDtt3-1PXGx-xR7997tJlLvGsOi9uEK-XxnavZ65Bd7fkCvNJfMZEyYLT8XgvdWbfudF2wN6qscyL_LmVg7vOlf-cJ0UKp0zBPuPdJYEqoI_e85n46q2K_9SADf1eT68oTlrMawFXs-JS9w8R-_SuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
OpenScreen — ضبط صفحه نمایش، سینمایی و حرفه‌ای
✨
قابلیت‌ها:
•
🖱
حرکت روان و طبیعی موس
•
🎨
پس‌زمینه شیک و حرفه‌ای
•
✏️
ویرایشگر داخلی: زوم، سایه، گرد کردن گوشه‌ها
•
💻
سازگار با ویندوز و مک‌اواس
•
💸
رایگان و متن‌باز — رقبا ماهی ۲۰$ می‌گیرند!
🌐
Site
#OpenScreen
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLRLs7a10h4-o4bgUhpp7MfOepnyPgJG39OYNvzp-OnsPl1ZwfBX-_VEBF_grJBC6nUCGw3AkjCTlyN5cjVNJgOkoujJ7vm_6UWBc2-UrNiZlh-ObMReqA5c_MEQy6YtwObJJhksSp7YONFBsaQwTEnTrfVE6zGzaTgbsF2vG8VOtY6vAvisTArDSxX-hiFEDHiCR4wGwoU9DRIaZZvHtCJO0qAn7IQ4ZS0b3qpiN877d0rL8tBevCe2PbhnoFkfbaajO1XX-sqMEQnUnOtFK2xobViGY_1ccD4IgFM0zjK3C6vpedfAoD4tIWMgxw2feSglfXps-ouAgqLaol4B8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG873vOC7JPd4Kzl8dkC_19aW_cTHZ9S6pYR-B83HRpAs8ymWq_EvX3OmT4XlhMqAEK-YUqg8eqkj1v5hOSQFwDijrSem9--VlIbet86sZZUoMVWrC1gLwE_fFjCJKZCXhdllryXEw2cHl5EXZhsKwlBi4SxfF2vsm1Kgw-u6H6ks3E2Nm6BABzqGL-mlWcmJoyyIw6tHKYN0jnj3bkIYYALUXjwt_u4BNStn4Vef7vMJ3GalOG-9YRrd-aLaEz8wngPOKOYWwA1qGgKnDrAK0TLupFwSl2wXAcr28a0ecNcmtHAhYpZqlGJpUn6g0xZPU4xOZHiScN49z6QEJ6BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗂
PostKeeper
این افزونه توییتر یا X را به آرشیو شخصی شما تبدیل می‌کند
✨
قابلیت‌ها:
•
🔹
خروجی پست‌ها، لایک‌ها، بوک‌مارک‌ها و لیست‌ها
•
📥
دانلود فایل‌های ساختاریافته برای پشتیبان و مرجع
•
🔒
آرشیو محلی و خصوصی روی دستگاه خودتان
•
🧭
جستجو و دسترسی آسان به تاریخچه حساب
•
🛠
متن‌باز با تمرکز بر حریم خصوصی
🌐
سایت
🌐
افزونه
#Twitter
#X
#OpenSource
#Privacy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beI3oD3z-N6RYpZ4PAqqe0cDSW0V_GUGc7kwn-zS1KaCbd288Lm92JaUiLkV5PUiW0DEogfrveLD-2RGrmYU7qhdOMmnYPlW0oTDDdYb1mFA-zAsMGFDZTcRboeRAgnGHvkixP50-bDTd6qUKjMwh9JqyzTwmZXSS0uqDw60vIz9ZXJrvY_a1WBBG5TKwvCp0rqOHqYD5LOs1XD1GM6Gl4CbR1DQG7iVKtqTz7U19j-zUVxxStMoJi4GX9r3iXg3-KacdB9MkKtZkKM2gTPT_7eOctXo0ckOHs8JKTID2y2cFkDJ5JMI5X7-dpm8PIrxns-DO80BNdRvey56vJXwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
80 کریدیت رایگان برای دسترسی به برترین مدل‌های جهان مثل Opus، Fable و GPT
✨
همین حالا وارد سایت
kie.ai
شوید
📝
ثبت‌نام کنید و از امکانات فوق‌العاده آن لذت ببرید
🔑
همچنین می‌توانید API Key اختصاصی دریافت کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTBh6fDhk2vn9xkaYZu-vWg_x7uq4r1lLpQ_HU4-DhnU7CcpfwI4c-kbRwMfr5BpJq_7u93sEuJhfnrVl-iumZIWKsmLtYgY06kBA4_dGrLxOgTb3vMiMK9r4m_2UV948L0dcHxEsY7SvEWA-VKDoRGA4qwEVAPYZlUlOxEPUf8tK9KKVhIhqq8jNWfEeAPEF0REHZtI8aCNJjYOS823Q0pHbzhZBs66QzpC4FtutsRvB8JZxQi5EWc4YGvRJ96aubB2jTULZGbwDYov0_5Ed5xl85Kmt9fcLBBhw3_k42Q9f5e0JtwzO4_7bujwL7UE_eDph8OZX2XN0F6lEU0KtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=V6ZfuB5QB3DUWslacH18kxCoByXq9g0X5Hk3HxeqPuB27ArMdX9qmOqE-7eDK3A22JwWdoHhhHtspRIoCflHvoTgA7jN-qiAKobqSpRs-5LEAFPghalXYot5f0TouHdyNt2SLXQrrfg1kFjqtswoug5ZW99-FUzfmt6H5IsfT6cHvLYSkXQgFugb2czHD1h1jImVAGrWTeiWNczc-DnbrD-KhABDV1sgih2iIKzHRk1C4VCffh1REwE2paI3UMbXClrh_Gr39V2Rvvh0RnxyQGPddsLIe_jnoK53Ji8VUIGWUOSw0gjkVlec--wyaTHiLQleFRnLQusMzSQ5wyybhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=V6ZfuB5QB3DUWslacH18kxCoByXq9g0X5Hk3HxeqPuB27ArMdX9qmOqE-7eDK3A22JwWdoHhhHtspRIoCflHvoTgA7jN-qiAKobqSpRs-5LEAFPghalXYot5f0TouHdyNt2SLXQrrfg1kFjqtswoug5ZW99-FUzfmt6H5IsfT6cHvLYSkXQgFugb2czHD1h1jImVAGrWTeiWNczc-DnbrD-KhABDV1sgih2iIKzHRk1C4VCffh1REwE2paI3UMbXClrh_Gr39V2Rvvh0RnxyQGPddsLIe_jnoK53Ji8VUIGWUOSw0gjkVlec--wyaTHiLQleFRnLQusMzSQ5wyybhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">MagicVideoAI
تبدیل متن به ویدیو
🔥
شرکت ByteDance (تیک‌تاک) ابزار جدیدی برای تبدیل متن به ویدیو ارائه کرده است .
این مدل از نظر پارامترها از Pika 1.0 و Stable Diffusion-XT پیشی گرفته و ویدیوهای فوق‌العاده‌ای بر اساس متن تولید می‌کند.
🌐
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2dXGIkNiYIa7Rw6W6Lq3zHtOHZp8emQQtVUXdcq3H4hTEfi-mFUWiTcGsBQoPm3QLCS9e9n7YtQymJvV1kbK_o2DTdWqBp1ozDBdV9roSGTsMzMb6C1rnAigcY6a-0iIowKOrj9iurFl4VTplY2VmEw97U7J08pB8pKnYV6EpqSEVDG2hRi4kOabxUht_YpJiE75JvP6G4NK3OyssMdhZ0NHhz4naUnGN3aRcSSx82__mwEj--nzrAhCDGesVngjaxJDFf0dHeirEkshwG_Gx9L3aezSatmcBJDPqHYCik4Lb0oAhyiuPGU_Rbp8CALhUD5V-Gkn1A6pHz09OXxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام
Sakana Fugu
رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک پلتفرم هماهنگ‌کننده چندعاملی (Multi-Agent) است که در قالب یک API واحد (سازگار با فرمت OpenAI) ارائه می‌شود.
🔥
ویژگی‌های شگفت‌انگیز این سیستم:
1️⃣
دو نسخه متفاوت:
نسخه
Fugu Mini
(با تمرکز بر تاخیر بسیار کم و سرعت بالا) و نسخه
Fugu Ultra
(برای پردازش تسک‌های فوق‌العاده سنگین و پیچیده).
2️⃣
معماری کاملاً پویا (Dynamic):
برخلاف سیستم‌های قبلی که نقش‌های ایجنت‌ها از پیش تعیین می‌شد، هسته Fugu یک مدل زبان سبک و خودران است که بسته به میزان سختی تسک، مدل‌های «کارگر» (Worker) را به‌طور خودکار فراخوانی کرده و کار را بین آن‌ها تقسیم می‌کند.
3️⃣
خوداصلاحی و Test-Time Scaling:
این سیستم قابلیت بازگشتی (Recursive) دارد؛ یعنی می‌تواند خروجی‌های قبلی خود را بخواند، اشتباهاتش را تشخیص دهد و یک گردش کار جدید برای اصلاح آن‌ها ایجاد کند.
4️⃣
پادشاهی در بنچمارک‌ها:
نسخه
Fugu Ultra
در تست‌های به‌شدت سخت استدلال و کدنویسی طوفان به پا کرده است! این مدل در تست‌های GPQAD (۹۵.۱)، LCBv6 (۹۳.۲) و SWEPro (۵۴.۲) توانسته مدل‌های پرچمداری مثل
GPT-5.4
،
Gemini 3.1
و
Claude Opus 4.6
را به‌طور کامل شکست دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#SakanaAI
#Fugu
#MultiAgent
#AI
#GPT
#Gemini
#Claude
#TechNews</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚀
معرفی یک راهنمای جامع و فوق‌العاده برای یادگیری زبان انگلیسی!
🇬🇧
✨
اگه دنبال یه نقشه راه اصولی، متفاوت و البته رایگان برای تقویت زبان انگلیسی می‌گردید، ریپازیتوری
English-level-up-tips
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید. این راهنما با یه رویکرد قدم‌به‌قدم، یادگیری زبان رو از یه غول ترسناک به یه پروسه لذت‌بخش و طبیعی تبدیل می‌کنه!
🔥
ویژگی‌های برجسته این راهنما:
1️⃣
پوشش تمامی مهارت‌ها:
از درک مطلب و دایره لغات گرفته تا لیسنینگ، ریدینگ، اسپیکینگ و رایتینگ؛ همه‌چیز در این آموزش گنجانده شده.
2️⃣
یادگیری با قدرت هوش مصنوعی:
یکی از جذاب‌ترین بخش‌های این راهنما، آموزش نحوه استفاده از ابزارهای هوش مصنوعی مثل
ChatGPT
و
Gemini
برای تسریع و بهبود فرآیند یادگیریه.
🤖
3️⃣
مناسب برای همه سطوح:
فرقی نمی‌کنه مبتدی هستید یا پیشرفته، دانشجو هستید یا یک متخصص؛ این مخزن ترفندهای جذابی برای همه داره.
4️⃣
جامعه کاربری پویا:
یک مسیر ساختاریافته که به شما یاد می‌ده یادگیری زبان یک مسیر پیوسته است، نه یک مقصد نهایی!
🔗
لینک مخزن در گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#English
#Learning
#Github
#AI
#ChatGPT
#Gemini
#Roadmap
#Education</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDFpG8GCil04sW7kysGfIp9jnwu4_rne0T5dNg1m6RBz3WBbbmFmPPR2dlh_bBwhCUgFwvMh2L2gf2Pw-GO5i0ZnHHcfKfpCaUCHwWyX_v4f9n-QR_so1-0H7qnhVaaRNd7at0RpVqt_d7Q_NKsl9A7V9CyDG-LkQOzeOmJNoPORVkhfyXm1uCld8_qPZ8gQgi2P31oDyGZ2O9F6jZbh5VGrisws6pU6AZa9B6yi6b-cv-rt_gJ7MPm0GNVkYwgciZWM2mSndCABmvMy9vcVJ87UrnCNnvGMVVwEIvIEP4pKhzOim3G5Spe4UsdlsPKjmKSLjk8S_-hVATlrT050_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
ساخت آرشیو اینترنتی شخصی
ابزاری به نام Monolith می‌تواند کل سایت‌ها را در یک فایل HTML مستقل ذخیره کند.
دیگه نیازی نیست نگران باشید که مقاله، دستورالعمل یا مستندات مورد نیاز روزی ناپدید شوند.
✨
قابلیت‌ها:
•
🔹
ذخیره کل صفحه در یک فایل HTML مستقل
•
🖼
نگهداری تصاویر، استایل‌ها و منابع صفحه
•
⚡️
استفاده ساده بدون تنظیمات پیچیده
•
🛠
اجرا روی ویندوز، لینوکس و مک‌اواس
•
📦
رایگان و متن‌باز
🌐
GitHub
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
معرفی OpenPencil؛ رقیب متن‌باز و رایگان فیگما مجهز به هوش مصنوعی!
🎨
✨
اگه به دنبال یک ابزار طراحی جایگزین هستید که هزینه‌ای براتون نداشته باشه، با
OpenPencil
آشنا بشید! این ویرایشگر طراحیِ متن‌باز (Open-Source) با قابلیت‌های شگفت‌انگیز هوش مصنوعی منتشر شده و تمام ابزارهای پولی رو به چالش کشیده.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
پشتیبانی از فایل‌های فیگما:
می‌تونید فایل‌های با فرمت
.fig
رو مستقیماً توش باز و ویرایش کنید.
2️⃣
اجرای محلی (Local):
کاملاً آفلاین و روی سیستم شخصی شما اجرا می‌شه، بنابراین حریم خصوصی پروژه‌هاتون کاملاً حفظ می‌شه.
3️⃣
دستیار هوشمند (Agentic AI):
دارای قابلیت‌ها و ایجنت‌های هوش مصنوعی داخلی برای کمک به پروسه طراحی.
4️⃣
خروجی مستقیم کد (جادوی فرانت‌اند!):
طرح‌های شما رو با یک کلیک به کدهای تمیز و آماده‌ی
Tailwind
و
JSX
تبدیل می‌کنه!
⚛️
5️⃣
یکپارچگی عالی:
قابلیت اتصال و هماهنگی کامل با ابزارهای برنامه‌نویسی محبوبی مثل Claude Code و Cursor.
🔗
لینک دریافت پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenPencil
#AI
#Figma
#Design
#OpenSource
#Tailwind
#JSX
#FrontEnd
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
