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
<img src="https://cdn4.telesco.pe/file/X5R2wXrDD6cEciyNvySHLGByUgdAcPnvRTvqVFHpC9TppDK-ovFygsLCk2_ZjOaVnF_8zvwJ5biOP6CiQYAqQYATDVIMpb8rVb-yIOmI1mB-kUpS3L6lIobuJ9wCY910dy8R9YmPVCUIJIMRafpYV74qMKPf8EbK4VHJ1Wznnx3PXpyqKTJTcbcNum4CQ3l376LrAWvQq2UAnV88-A_7Crh6ak6hKoZFWwBQlltOQz5eGHp-UGesrOhAZSGHEzxAnCbc0QVzCPOXRThMykzhr17ZOailTdDMs5PB_xU9XmFIXaRSPG1TV7zgq6pAxudPwVXume7JeSKz53x5QBoh6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 11:50:28</div>
<hr>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKUu9gXFhA_fUxMoWr369mVKSnivi7o91DNAzbWSrUDx6kN9ICBBHYoP790Q1wjEuO47k07Ls0PGKVysV_2jFhdOxx0AlLtINSArcZIDYIdl0EWPZT--ihDfwKpfNTaJ00ZmNyficyohiY0OEoZx1KRzEq_fXC643kGrKEymANAwjSYCwavRxnwSgvQuWzXyQQaBlMZEWCHuWj15irMKnPSqTTRYGodKBk-qVLNjOt3nPUx7P2xXn49b921dfRSZO2x7LsPxImdQydC7dsl9cTfBBkg21YDamk_jndSqmy0e3SOY9ywvlkLeCTWEtM4fk6h6SEyesZDGZ_0Yz4ZccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نحوه استفاده از Claude Opus 5 و GPT 5.6 Sol
به صورت رایگان
📣
حساب‌های جدید در
Verdent.com
، یک دوره آزمایشی 7 روزه با 100 اعتبار رایگان دریافت می‌کنند
💯
🆓
🎉
✍️
آنچه دریافت می‌کنید:
👀
🔍
☑️
Claude Opus 5 / Sonnet 5
✅
GPT-5.6
☑️
Gemini 3.1 Pro
✅
GLM-5.2
☑️
Kimi K3
📌
نحوه دریافت:
🔥
⚡️
☑️
به
➡️
🔗
https://verdent.ai/
مراجعه کنید.
✔️
برنامه دسکتاپ یا افزونه VS Code را نصب کنید.
☑️
یک حساب کاربری جدید ایجاد کنید
✉️
✅
مدل مورد نظر خود را انتخاب کنید.
☑️
از اعتبارها برای شروع استفاده کنید
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 445 · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔥
KiraAI
روزانه ۵۰ میلیون توکن رایگان
🤖
مدل‌های موجود قابل استفاده :
⚡️
kira-3.5-pro
⚡️
kira-3.5-flash
⚡️
kira-3.0-image
🔗
kiraai.vn
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔎
scite.ai
— موتور جست‌وجوی استنادی برای تحقیق جدی
۷ روز اشتراک رایگان (تریال رسمی سایت)
📑
Smart Citations
نشان می‌دهد هر مقاله توسط مقالات دیگر تأیید شده، رد شده یا فقط اشاره شده — نه فقط تعداد استناد
🧠
Assistant
پرسش پژوهشی‌ات را می‌پرسی و پاسخ با استناد واقعی و لینک به منبع می‌دهد، نه حدس
🤖
دسترسی به مدل‌های تحقیقاتی:
Claude Sonnet 5 | Claude Opus 4.6 | GPT 5.2
🎛
Personalized Feed
فیلتر و شخصی‌سازی حوزهٔ تحقیق ، فقط موضوعات مرتبط با کارت را ببین
🔗
Custom Dashboards
داشبورد اختصاصی برای کلیدواژه، نویسنده یا ژورنال خاص + هشدار مقالهٔ جدید
📊
Analyses & Topic Classification
دسته‌بندی موضوعی، شناسایی روندها و گپ‌های پژوهشی
آموزش فعالسازی
🔗
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN6JSsuNnWss8WIcrB7squ-XHBVvzKXI11JkJTUBTU0V3LbOJGWvfVU7gLnr0V2mS-GLZRTOWn7Vp7OBwzrBEejQeAeeqwjX4GS8mCD70BdhEcBVj9puwf9KaLUiuqJnbsGlF8aa-OkBgIANz1eMdWbv4BFXTef07-zyxROB0GbDKz7vztOv4juXxeC4bJ9QEvi3yhk_CJRKAZuIQc8JnlMASRfG7L_zMPeCtPfb5bLBO9FCzainPumqUNuV5Ex7UfoRUUU8VRCVr2aFOl-a35D_l97DAvsP1pYGgp2IuXTlp6nnY1KQURHhuJQGvnzmpqC0cvFO_xo3xMfFpSGUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">keys.txt</div>
  <div class="tg-doc-extra">2.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان  claude-fable-5 | claude-sonnet-5 |  deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید  @kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url: https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnnXHhKiBnkZSQCwcwcfAJRuHUOskhHDqeCgz2KDxOQ2ApelHexbVu6VWZ9DAdR19Qb9qizgOCvTF0KMSSZdXzAqGt4rRQkZ4VWcVZTCQxZ-ShjuAwxITKUn3bRtE9Z45ECABAJ-Bowp9znbj6zSNdmxfiZ9H5e6eVdEV_vM0jLISVf-LS5B8Srvcin9FTYJmFAX-77__hiQ35sohXpBQVPG2Z5goH7d9jZ7OhrowpuCWdNsOzQsl4uWIJnyrl1q4aRsNm4tLKW4D92TZHS99WVhcGl5kk2e8EOSLcrQZ-FNDv_R86UEe2UcKSxT-kZKCk0131Y1HUvmuBlHhhdxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
دامنه رایگان همیشگی بدون کارت اعتباری!
‏بچه‌ها این
پروژه گیت‌هاب
با نزدیک ۲۰۰ هزار استار، دامنه‌های رایگان دائمی میده که واسه پروژه‌های تستی و سایدپراجکت‌ها کاملاً خوراکتونه.
🚀
‏•
دامنه‌های متنوع:
پسوندهایی مثل
.us.kg
و
.qzz.io
بدون هزینه فعال می‌شن
‏•
کنترل کامل:
دسترسی کامل به
Custom Nameservers
و تنظیمات
Cloudflare
دارید
‏
💬
نحوه استفاده:
کافیه برید به سایت پروژه، اکانت بسازید، دامنه دلخواهتون رو ثبت کنید و نیم‌سِروِرهای کلادفلر رو ست کنید.
‏
🔗
سایت پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⌨️
ترجمه سریع و هوشمند، بدون دردسر!
اگه دنبال یک مترجم ساده و کاربردی هستید که فقط به یک سرویس محدود نباشه، پروژه Translator می‌تونه انتخاب خوبی باشه. این پروژه با پشتیبانی از سرویس‌ها و مدل‌های مختلف ترجمه، امکان ترجمه متن، استفاده از قابلیت‌های صوتی و مدیریت تاریخچه ترجمه‌ها رو در یک محیط مدرن و ساده فراهم می‌کنه.
🤖
قابلیت چت با هوش مصنوعی؛
با استفاده از API Key با مدل‌های هوش مصنوعی گفتگو کنید و پاسخ‌های هوشمند دریافت کنید.
🔑
همچنین امکان استفاده از API Key و ترجمه با سرویس‌های هوش مصنوعی مختلف رو داره.
🌐
نسخه آنلاین:
https://codewave4.github.io/Translator/
🔗
سورس پروژه:
https://github.com/codewave4/Translator
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=QxdAAO4W1G5hqkbhEcHYYSAbKksuIfV6RvfFhSAVwlhQsamp7j9CL_FzSsQnQywHavWGIpFNUfuZlG8cNNqvW8Nl-DCcE1xCIpdZAuv8snYA_msXZFFHbyCWLzKGpR5zA5V0Xp8heA248d3M-NyhgBZ2fg2K9EHy_AEbLviQLib0tAAXS6J1LUvYdAWO9FAxv1XC5ofHCP6vWDa5o60qlzRC453xuPaA-UvMG5ouzJf8IG3syJ04Gke37yZeW6buIwTVYvwk9pvtrsj7slm8cnyKqMOieDmAjULsIYZx7a_fIBeMZmqKZAncdIorTlnXr80q_OaDA3DUuu-5SpriqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=QxdAAO4W1G5hqkbhEcHYYSAbKksuIfV6RvfFhSAVwlhQsamp7j9CL_FzSsQnQywHavWGIpFNUfuZlG8cNNqvW8Nl-DCcE1xCIpdZAuv8snYA_msXZFFHbyCWLzKGpR5zA5V0Xp8heA248d3M-NyhgBZ2fg2K9EHy_AEbLviQLib0tAAXS6J1LUvYdAWO9FAxv1XC5ofHCP6vWDa5o60qlzRC453xuPaA-UvMG5ouzJf8IG3syJ04Gke37yZeW6buIwTVYvwk9pvtrsj7slm8cnyKqMOieDmAjULsIYZx7a_fIBeMZmqKZAncdIorTlnXr80q_OaDA3DUuu-5SpriqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🎬
ساخت موشن‌گرافیک حرفه‌ای با یه پرامپت!
‏این ابزار هوش مصنوعی کل فرآیند ساخت تیزر تبلیغاتی، از استوری‌بورد تا تدوین صدا و انیمیشن رو خودش انجام میده و خروجی رو با بیت موزیک سینک می‌کنه. خوراک بچه‌هاییه‌ که سریع میخوان خروجی باکیفیت بگیرن.
🔥
‏
⚡️
دسترسی به منابع غنی:
۱۵۷ مدل سناریو، ۲۱۴ استایل بصری و کلی الگوریتم انیمیشن آماده
‏
⚡️
شروع سریع:
کلی تمپلیت آماده‌به‌کار داره که کار رو برای پروژه‌های فوری جلو میندازه
‏
⚡️
عملکرد هوشمند:
کافیه ایده‌تون رو متنی بدید تا در لحظه ویدیو تحویل بده
😎
برای دانلود ابزار تولید ویدیو
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zn0rgzjXGTSr-XogC0HBnXYqpNKlzVcw4z_hNhiRSbdvj-4Nu2bZy4OTUTqHP4rbk9vuhnZRPSPssvrkjagwJQMSn9eNW_asB_wokN736peg_AcKQhEXT8E3UsOreFw3aK053lWTbVVf1mzRNRQxDzjNSVRxjoN_9Th7_BVkUH9f2NZUIepyd4JIOHEXlu2a7R0_C7FruEf2w5B0zDa7zg-yWbqKkcQAmxbxkd0JdvvqzB1ycWdTttDf2slZ_tyHT6jSkSCDtxY-0KyTWpE4XeiPiPMdBQgnE-7T4WZDyVNvuJUAtpCLrRDk1GKdB5LqFx3cWymuK-09zYVXv7S9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
مرجع خفن اسکیل‌های ‌Claude Code⁩ و ‌Codex⁩!
‏سایت ‌SkillsMP⁩ یه کاتالوگ تر و تمیز با بیش از ۳۳ هزار اسکیل آماده‌ست که تو کار با هوش مصنوعی کلی جلوتون میندازه.
🤖
‏•
دسته‌بندی جامع:
از برنامه‌نویسی و ماشین‌لرنینگ تا امنیت و کار با ‌API⁩
🔍
‏•
دسترسی سریع:
لینک مستقیم به گیت‌هاب برای هر اسکیل
📂
‏•
کیفیت‌سنجی:
دارای ایندیکاتورهای کیفیت برای انتخاب بهترین ابزارها
⚡️
‏خوراک بچه‌های وایبکودره که بخوان پرقدرت‌تر پروژه‌ها رو ببرن جلو.
🚀
🔗
skillsmp.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🛡
دیگه ایمیل و پسورد اصلیت رو به هیچ سایتی نده!
حتماً براتون پیش اومده که برای ثبت‌نام در یک سایت مجبور شدید ایمیلتون رو بدید، اما بعد از یه مدت صندوق ایمیلتون پر از پیام‌های تبلیغاتی مزاحم شده یا اون سایت هک شده و رمزهاتون لو رفته!
ابزار جالب
AliasVault
دقیقاً برای حل همین مشکل ساخته شده:
💎
این ابزار براتون چیکار می‌کنه؟
⚡️
ساخت بی‌نهایت ایمیل دائمی:
برخلاف ایمیل‌های موقت که بعد از ۱۰ دقیقه می‌پرن، این ایمیل‌ها
کاملاً دائمی و همیشگی
هستن و برای هر اکانت می‌تونید هر تعداد ایمیل دلخواه که خواستید بسازید!
⚡️
دریافت کد ثبت‌نام داخل خود برنامه:
نیازی نیست برید یه ایمیل دیگه باز کنید؛ ایمیل‌های تایید و کدهای ورود مستقیماً داخل همین برنامه براتون میاد!
⚡️
مچ‌گیری از سایت‌های متخلف:
اگر یه سایت ایمیل شما رو به تبلیغاتچی‌ها بفروشه، دقیقاً می‌فهمید کار کی بوده چون برای هر جا یک ایمیل اختصاصی ساختید.
⚡️
نصب روی گوشی و کامپیوتر:
هم اپلیکیشن برای موبایل داره و هم افزونه برای مرورگر، و خودش پسوردها رو سر جای درست پر می‌کنه.
💬
چرا این ابزار فوق‌العاده‌ست؟
•
ایمیل‌ها هرگز منقضی نمی‌شن:
هر زمان در آینده بخواید وارد سایت بشید یا رمزتون رو بازیابی کنید، پیام‌ها باز هم به همین ایمیل دائمی میاد.
•
سقف تعداد ندارید:
برای ۱۰۰ تا سایت هم می‌تونید ۱۰۰ تا ایمیل مستعار و رمز مجزا بسازید.
•
کاملاً رایگان و امن:
بدون هیچ هزینه‌ای، امنیت و آرامش صندوق ایمیلتون رو تضمین می‌کنه.
🌐
ورود به وب‌سایت AliasVault
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM3bjlVQD6n5b834KoMHofwwWo4bDl7BcZjxz6frkwJp4bya_7TySLMHlIszmPcThYwBssPG1cnDnahUUiZd8VsbPq1pgyyZAQk3bovhgC65-lk5MgzpHT95ey1Zz3HgkSFYL43ChoQTZ09sX4zLOYmyrvZ4FHMh0xR_iMbcdb7VrbG4s84lOOKoaN7YK3hAsZS3aVEIqcVZ13VzJs0Ljk75vO6dsHKVZq_K8NrNmE799pqToj6XMJUhIkeKJWPu2a1zepGkyJCESSC4NB2_am-cVUlBQCWiellO6aK7L8QryZwv8NJ-remszFR6DZ3ktGhl1iK4MhPx6Fhisv3KLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سایت، ده‌ها مدل و ابزار با اعتبار رایگان روزانه
🎁
💬
Multi AI Chat
GPT، Claude، Gemini، DeepSeek، Grok، Qwen ، Llama
همه در یک چت، با امکان مقایسه جواب‌ها
🎨
تولید و ادیت عکس
تولید تصویر از متن (Flux، Stable Diffusion، Ideogram…)
حذف/تغییر پس‌زمینه، حذف اشیاء و متن از عکس
Face Swap، Upscaler، تبدیل اسکچ به تصویر
ویرایش عکس با دستور متنی + تولید تصویر سه‌بعدی
🎬
ویدیو
تولید ویدیو از متن و از عکس
Face Swap روی ویدیو
خلاصه‌سازی، زیرنویس و ترجمه ویدیوهای یوتیوب
🎵
صوت و موسیقی
ساخت آهنگ (Suno، MusicGen…)، Text-to-Speech با صداهای طبیعی
شبیه‌سازی صدا (Voice Clone)، تبدیل ویس به متن، حذف نویز
✍️
نوشتن و تولید محتوا
تولید محتوا، بازنویسی، خلاصه‌سازی، ترجمه، گرامر
تحقیق کلمه کلیدی و تشخیص محتوای AI
🌐
لینک سایت :
app.1min.ai
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان
claude-fable-5 | claude-sonnet-5 |
deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید
@kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url:
https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🆓
هوش مصنوعی رایگان  — بدون ثبت‌نام
Kimi K2.6 | GPT 5 mini | DeepSeek V3.2
📌
امکانات:
⚡️
چت هوش مصنوعی نامحدود
⚡️
تولید متن و محتوا
⚡️
بدون ایمیل، بدون رمز عبور، بدون کارت بانکی
📌
نحوه استفاده:
🔗
وارد
این سایت
بشید مدل موردنظر را انتخاب کنید و شروع کنید.
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQqoQmj4hdELEep3RRU7Co0TpFWEh4gXEUaL9IBDa0QPMGMrguCcHaDAZZuWB3D9rRPo3KR0HFT7a0qV6iLAS_K8O7nBtvkp4PoLYQPNaKd9FLZ2agKb_T6lPjS9Wbzb2VO3GcGDCRA4NfFRwStgtQModrRUAzMLyreGY4JeAv8tJFaZ_igNROQ69izzVR94n__peRzsg5Xu7b7tnpCfKMUpwn4VfnT9kN3Gh4k7qE8DKDSss_b3ODIYQ9vx-N_Z10Xh-LZfpkeaEp4QhJqgOgUahvTBq0SDArvS-RLA_CjxDPRzmv-3qlPNIKNUaUNzwtNWhPKum6thxtmgt_BzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
۵۰۰ مگابایت پروکسی رزیدنتیال رایگان (
proxyma1.io
)
یک سرویس پروکسی رزیدنتیال که با ثبت‌نام از طریق تلگرام ۵۰۰ مگابایت ترافیک رایگان می‌دهد و API هم دارد.
📌
نحوه دریافت:
1️⃣
وارد سایت
proxyma1.io
شوید و ثبت‌نام کنید
2️⃣
پس از ثبت‌نام، یک پیام برای استارت ربات تلگرام نمایش داده می‌شود که داخل آن یک کد هدیه قرار دارد
3️⃣
ربات را استارت بزنید و کد را برای ربات ارسال کنید
4️⃣
۵۰۰ مگابایت به حسابتان اضافه می‌شود
🚀
📌
ویژگی‌ها:
☑️
پروکسی رزیدنتیال (Residential)
☑️
۵۰۰ مگابایت ترافیک رایگان
☑️
پشتیبانی از API
☑️
ثبت‌نام آسان با تلگرام
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkVGxT2-kl-r99f0rchf0TcDKvgxHPfzH5J5WjSNEphJcvHSBdW7HiiBh9O9Ojb7YRn_Y_77faS7raFi-h9L2iJgSr_GyX6OHJud_1w2hIJZ10LGSqyzvbCs1okSkRZtxHr_BiuBFGoInyMdtEk33QUjFU-xng9BpSstHfvDvTBYhiKBff0LX5QqTdot2wX9sKr46Z8qfPakgnOUQd5ymI99IowRVlQ9zt8vGzcnO6eIy-LkHDcwLuFaun_MY-TPcmuSG73LppEOVLLZgT20iWqPjI7sNTf4SE-2PAwI9tp6FREAONj1Bf0eiajAlCIxGkK_NZnVjcLVRMQ1FAcb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۵۰۰۰ اعتبار رایگان برای مدل‌های برتر هوش مصنوعی
پلتفرم جدید در شروع کار ۵۰۰۰ اعتبار به شما هدیه می‌دهد تا با قدرتمندترین شبکه‌های عصبی کار کنید: تولید متن، عکس و ویدیو در یک جا.
📌
امکانات در دسترس:
☑️
چت چندمدلی
☑️
تولید تصویر
☑️
تولید ویدیو
☑️
موجودی اولیه: ۵۰۰۰ اعتبار رایگان
🪙
📌
روش دریافت:
1️⃣
ورود به
getunikey.ai
2️⃣
ثبت‌نام یک حساب کاربری جدید
3️⃣
ایجاد کلید API در تنظیمات پنل
4️⃣
استفاده در رابط چت یا ابزار های واسط
base url:
https://getunikey.ai/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔍
Hidden File Hunter — شکارچی فایل‌های مخفی ویندوز
دنبال فایل‌های مخفی و سیستمی توی ویندوز می‌گردی ولی پیدا کردنشون واقعاً دردسره؟ این ابزار دقیقاً برای همین ساخته شده
👇
؛ Hidden File Hunter یک برنامهٔ دسکتاپ ویندوزیه که تمام فایل‌های مخفی و سیستمی درایوهات رو پیدا می‌کنه و توی یه جدول مرتب و قابل مرور نشونت میده.
✨
امکانات:
✔️
پیدا کردن تمام فایل‌های مخفی و سیستمی در همهٔ درایوها
✔️
نمایش نتایج در یک جدول مرتب و خوانا
✔️
خروجی گرفتن از فهرست کامل مسیرها در قالب فایل TXT
✔️
کپی کردن خود فایل‌ها با حفظ ساختار پوشه‌ها در مقصد دلخواهت
✔️
فقط می‌خونه و کپی می‌کنه — هیچ فایلی رو تغییر نمیده، حذف نمی‌کنه و بهش دست نمی‌زنه
✔️
ساخته‌شده با Python و PySide6
✔️
تم تیره و روشن
✔️
رابط دوزبانهٔ فارسی و انگلیسی
یه ابزار ساده، سریع و امن برای وقتی که می‌خوای بدونی توی سیستمت چه چیزهایی از چشم‌ها پنهان مونده.
🔗
لینک گیت‌هاب:
github
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
اپلیکیشن Bifrost (بایفراست)؛ پل ارتباطی فوق‌سبک تلگرام بر بستر ورکر کلادفلر منتشر شد.
بایفراست یک بریج لوکال (Local SOCKS5) مدرن و بهینه برای اندروید است که ترافیک تلگرام رسمی را از طریق پروتکل TWP به ورکر رایگان کلادفلر متصل می‌کند؛ با پینگ پایین، بدون قطعی و با سرعت دانلود فوق‌العاده بالا.
🔒
بدون نیاز به VPN، بدون روت و با مصرف باتری نزدیک به صفر:
این پروژه کاملاً متن‌باز (Open-Source) است و برخلاف فیلترشکن‌ها از VpnService استفاده نمی‌کند (هیچ علامت کلیدی بالای صفحه نمایش داده نمی‌شود و اینترنت سایر برنامه‌ها کاملاً دست‌نخورده و بدون تغییر باقی می‌ماند). مصرف پردازنده در زمان عدم استفاده دقیقاً ۰.۰٪ است و امنیت و رمزنگاری پیش‌فرض تلگرام (MTProto) نیز کاملاً حفظ می‌شود.
📥
دانلود و نصب برنامه (از گیت‌هاب):
https://github.com/Qorvhex/Bifrost/releases
⚡️
کانفیگ تستی برای شروع (بعد از نصب، کپی کنید و داخل برنامه Paste کنید):
twp://telp.qorvhe-x.workers.dev?clean_ip=1music.cc#Bifrost-Test
🛠
سورس‌کد اسکریپت ورکر (TWP):
https://github.com/Qorvhex/TWP
📁
لینک پروژه و سورس‌کد در گیت‌هاب:
https://github.com/Qorvhex/Bifrost
لطفاً تستش کنید و سرعت و عملکردش رو بهم بگید!
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🖥
مرورگر ضد ردیابی Private Browser Pro؛ هویت جعلی و دور زدن بن شدن اکانت‌ها!
​بچه‌ها اگه نیاز دارید روی یک سایت چند اکانت مجزا بسازید بدون اینکه سیستم‌های امنیتی بفهمن همه‌شون مال یک نفره، یا می‌خواید ردپای دیجیتالی‌تون رو کامل مخفی کنید، این مرورگر اوپن‌سورس ویندوزی دقیقاً همون چیزیه که دنبالشید. این ابزار بر پایه نسخه فوق‌امن Ungoogled Chromium و Electron ساخته شده و از زبان فارسی هم پشتیبانی می‌کنه.
​
🎭
جعل مشخصات سیستم (فینگرپرینت):
شبیه‌سازی کارت‌های گرافیک قدرتمند (مثل RTX 4090، سری RX 7900 و تراشه‌های اپل)، اضافه کردن نویز به Canvas و AudioContext و هماهنگ‌سازی هدرها برای عبور آسان از سد کپچاهای Cloudflare Turnstile، hCaptcha و reCAPTCHA
​
📁
مدیریت و تفکیک کامل پروفایل‌ها:
امکان ساخت محیط‌های دائمی (Persistent) برای ذخیره دیتای هر اکانت در پوشه جداگانه، یا حالت موقت و یک‌بارمصرف (Ephemeral) که با بستن پنجره کل ردپا پاک میشه + دکمه پاک‌سازی آنی
​
✅
پروکسی پیشرفته و ضد نشت اطلاعات:
پشتیبانی از پروکسی‌های SOCKS5 و HTTP (با یوزرنیم و پسورد)، حل آدرس‌ها از داخل پروکسی جهت جلوگیری از DNS Leak و غیرفعال‌سازی WebRTC برای مخفی ماندن کامل IP واقعی
​
✨
محیط کاربری تمیز و دو زبانه:
کرومیوم دست‌نخورده بدون واترمارک‌های تستی، تم دارک با کلیدهای میانبر سریع و پشتیبانی کامل از منوی فارسی و انگلیسی
​
💡
بهترین سناریوی استفاده:
ایده‌آل برای مدیریت چند اکانت در شبکه‌های اجتماعی و پلتفرم‌های حساس، تست وب، ریسرچ‌های OSINT و حفظ حریم خصوصی بدون نیاز به خرید اشتراک‌های گران‌قیمت مرورگرهای ضد ردیابی.
​
🔗
گیت‌هاب
​
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">📥
تبدیل فایل‌های تلگرام به لینک مستقیم نیم‌بها با ربات Leecher!
بچه‌ها اگه کندی دانلود از تلگرام یا قطعی فیلترشکن موقع دریافت فایل‌های حجیم کلافتون کرده، یا می‌خواید تورنت و ویدیوهای یوتیوب رو مستقیم به فایل تلگرامی تبدیل کنید، این ربات لیچر ایرانی حسابی به کارتون میاد.
🇮🇷
لینک مستقیم با ترافیک نیم‌بها:
تبدیل آنی فایل‌های تلگرام به لینک دانلود پرسرعت تحت وب (سازگار با دانلود منیجرها) با محاسبه مصرف اینترنت به‌صورت نیم‌بها
🌐
دانلودر همه‌کاره (لینک به فایل):
پشتیبانی از دانلود مستقیم لینک‌های یوتیوب، اینستاگرام، وب‌سایت‌ها و حتی فایل‌های تورنت و تحویل فایل داخل چت
☁️
اتصال ابری به گوگل درایو:
امکان لینک کردن اکانت شخصی Google Drive برای ذخیره و آپلود مستقیم فایل‌ها در فضای ابری بدون مصرف حجم گوشی
🎁
شارژ رایگان روزانه:
۱ گیگابایت حجم رایگان در هر ۲۴ ساعت بدون نیاز به پرداخت هزینه یا خرید اشتراک
💡
نکته کاربردی:
لینک‌های ایجادشده بین ۶ تا ۸ ساعت معتبر هستند؛ کافیه فایل رو به ربات بفرستید، لینک مستقیم سرور ایران رو داخل IDM کپی کنید و با حداکثر پهنای باند خط‌تون دانلود کنید.
🔗
استارت ربات
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A44MI9lY1i54dIHYx8Vs1zyOdHe2_qNq-DZc4blBfJfSs1sR30CefBqRFu5RpJ5308QCxZb3prPYnAsS2OunFzQA_iXVbHxgKHpYglubwZfWcVFcEsXIYNe2Z2rvuLDCxKloNj7dm73pOjUZegqmbtlGFW9Cl_2LRfn7loD-pb0nFLooX-jSX9cpejCYXMXcpNlkg_mqLPAj56i9wNTXwZN3qdpX6S6fM2qxhZ5CxMjEvv5xqOf6243RwIAu_29fUj9zsWyRfC5iQFSzqj8-cl8cpk_84pAVKbreCHBVAZiAj-Nd_qi5bYL2gQ1Om9UNqU9Cxzp8AhfLfnHIuEcvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید (1.8.0) برنامه MSN-GUARD منتشر شد :
💢
BOOM
💢
تغییرات :
1- اضافه شدن متد اختصاصی SHARD برای اولین بار
-_-_-_-_-_-_-_-
2- دسترس‌پذیری کامل و پشتیبانی 100% از صفحه‌خوان TalkBack برای عزیزان نابینا و کم‌بینا برای اولین بار
-_-_-_-_-_-_-_-
3- آپدیت هسته
-_-_-_-_-_-_-_-
4- اضافه کردن قابلیت Backup و Restore و Reset Factory از تنظیمات برنامه
-_-_-_-_-_-_-_-
5- برطرف شدن مشکل دکمه Reconnect در نوتیفیکیشن
-_-_-_-_-_-_-_-
6- اضافه شدن Theme کاملا روشن برای استفاده زیر آفتاب
-_-_-_-_-_-_-_-
7- برطرف شدن باگ اتصال خودکار پس از قطعی اینترنت و چند باگ دیگر
-_-_-_-_-_-_-_-
6 روش دسترسی به اینترنت آزاد:
1: متد Masque
2- متد Wireguard
3- متد Warp On Warp
4- متد Psiphon (اختصاصی و اولین)
💯
5- متد Tor (اختصاصی و اولین)
💯
6- متد SHARD (اختصاصی و اولین)
💯
💻
ریپازیتوری گیت‌هاب (متن‌باز):
https://github.com/mbm110/MSN-GUARD
📌
لینک مستقیم دانلود :
برای گوشی های 64 بیت
برای گوشی های  32 بیت
برای تمامی گوشی ها
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✉️
؛ Turbo Mail ایمیل موقت، سریع و بدون دردسر
اگه برای ثبت‌نام یا دریافت کد تأیید به یه ایمیل موقت نیاز دارید، Turbo Mail یه گزینه ساده و سریع برای شماست.
⚡️
ساخت فوری ایمیل موقت
👌
بدون نیاز به لاگین و ثبت‌نام
⏳
اعتبار ۲۴ ساعته
🔒
مناسب برای دریافت ایمیل و کدهای تأیید
🚀
ساده، سریع و بدون مراحل اضافی
کافیه وارد سایت بشید، ایمیل موقتتون رو بسازید و استفاده کنید.
🔗
https://mail.turbocenter.shop
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎧
دستیار هوشمند و همه‌کاره موزیک‌بازها؛ دانلود با کیفیت FLAC با ربات MelodyAddict!
بچه‌ها اگه عشق موسیقی هستید و از دانلود تک‌به‌تک آهنگ‌ها، افت کیفیت یا پیدا نکردن موزیک پس‌زمینه کلیپ‌ها کلافه شدید، این ربات فوق‌العاده با پشتیبانی کامل از زبان فارسی دقیقاً خوراکتونه. همه‌چیز از شزم اختصاصی گرفته تا رصد خودکار پلی‌لیست‌ها رو براتون یکجا جمع کرده.
🔄
سینک خودکار پلی‌لیست‌ها:
زیر نظر گرفتن لایک‌ها و پلی‌لیست‌های Spotify، SoundCloud، YouTube Music و Apple Music و ارسال خودکار ترک‌های جدید با امکان زمان‌بندی ارسال (۳ ساعته، روزانه یا هفتگی با دستور /digest)
🔍
شناسایی جادویی آهنگ:
پیدا کردن نام و فایل موزیک فقط با فرستادن یک وویس کوتاه، زمزمه، فایل ویدیویی یا لینک ریلز اینستاگرام، تیک‌تاک، یوتیوب و توییتر
💎
کیفیت استودیویی FLAC و Lossless:
قابلیت تنظیم کیفیت پیش‌فرض خروجی برای گوش دادن به بالاترین بیت‌ریت ممکن، با سرعت عالی و کاملاً بدون تبلیغات
📂
مدیریت پلی‌لیست‌های ابری:
امکان دسته‌بندی، ساخت و اشتراک‌گذاری مستقیم پلی‌لیست‌های شخصی داخل تلگرام
💡
نحوه استفاده:
ربات رو استارت کنید، زبون رو روی فارسی بذارید و برای شروع کافیه وویس یک آهنگ یا لینک پلی‌لیست موردعلاقتون از اسپاتیفای یا ساندکلاد رو براش بفرستید تا بقیه کارها رو خودش اتوماتیک انجام بده.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r9dKDhuCN6ZTwMBiJdU4QRp26DMiq1Qf1Z9l9T6s0y7TPU7Mg71hdYSI8jvlluXG6cJJw60fcp47E4UcPSobQA6twjKGXAxYjywahrJX4kJ5KByn0hwBolI5VWVaARqrUTv1uW347SNQHDgvw9qsUfzYY_NibjpP5lPxvrdfOiIjSGqrrT-tLHhEwsypGdu5AuhM7IJ0IzFDNJ23izeySQ5F_chDtt_xZbhWZaBqvEJYa8fvsIYtmpKZ_9n58AM-8L6gDb0mcSC7gWBMRRUOswThcK9_7BZ-qSOz2kZpN4Yy-yEXOXfo2s7nS721wW0KDAttGF8okn1xdmb6T9c15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید ArasClient منتشر شد!
نسخه جدید با اضافه شدن بخش Free منتشر شد و از این به بعد این بخش به‌صورت مرتب آپدیت میشه.
📱
؛ ArasClient یک کلاینت سبک و کاربردی برای مدیریت و استفاده از کانفیگ‌هاست که تمرکزش روی سرعت، سادگی و اتصال راحت‌تره.
🆕
اضافه شدن بخش Free
⚡️
آپدیت منظم کانفیگ‌ها
📊
تست و مرتب‌سازی هوشمند سرورها
🔄
انتخاب سریع‌تر سرورهای مناسب
📦
پشتیبانی از نسخه‌های مختلف اندروید
🔗
دانلود نسخه جدید:
https://github.com/ArasTey/ArasClient/releases/download/v1.6.8/ArasClient_1.6.8_arm64-v8a.apk
🔗
سورس پروژه:
https://github.com/ArasTey/ArasClient
💬
نظر، انتقاد یا پیشنهادتون رو کامنت کنید.
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlYmoUfjzP7_4DFKfyI4hOZjyq_oTCI62zm3xTi5uOdwQ_2zmh-yegfqpzIxngwpTFm9ailZWWIf26nwOCiwQU_8BYux0inuyO3X9c1yVMVJ4X9szHUHxFIBX2AhZA3AeMo1zd3O0rSB6pxQUARzeXbAWkLYDs4i-iWMLexrILcBvjT_X6pcZP4ISuXnzE6QtyZ6EsIuY0fhfJoY3rOtyJn8m4VQSbS7MQeWK_bkdMc0QiF3NIHlmhtJ1SqBj85pdbxsJHpKcntYVsgMQHHS6JZa1X3Fmp9m0nz7l8pgC-xpHSuqzEgVehB3otawarhNFKH3hoIlbhkQOOzIHxBiaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
اگر می‌خوای شبکه‌های کامپیوتری رو از پایه تا سطح حرفه‌ای یاد بگیری، نت‌داد دقیقاً برای تو ساخته شده.
از مفاهیم بنیادی مثل آدرس‌دهی IP، سوییچینگ، مسیریابی و امنیت گرفته تا شبکه‌های مدرن، همه چیز با پروژه‌های عملی و مثال‌های کاربردی آموزش داده می‌شه.
✔️
۱۰۰٪ پروژه‌محور
✔️
۵۳ درس تخصصی
✔️
۱۴ بخش آموزشی
شروع یادگیری از اینجا:
🔗
https://netdad.vercel.app
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYYMo0BybpG8tethQFA-yTG5a15g4-L69hR5Ag3X7syp1WBrqfoEoOr95RHRJ1tUCOXFwFFxqdPgdckstKWCFMJG3yDlxfELu3W72PbAoL1IuZoXb7zvBN_3VR6oxcR6CYQFQjoYhrNW2nDQFyJJVE2Ly8f0pnv5FfAAszKJxAMpXeBODZmbPZ1wKf1H2nvUvr9WZNfA31DJkuOaCg863CsTc8svWRtxA7mLl_bFJdGqAgQ_gb11nLFfPn4XD_JSuMvB7Gs-Bj7qnx4bg41tXDFkoVfmJ7l3QwtwW52UKf5ViAToiaBpSBzCOVWuWVJ62-qQCL3Ro_WveMO45vZlfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOh2CKEAIIcnggGImsZefWISmRo4-VeWhwH1A3xTYeNREc3oPmMbeplecQWx-GDfigNBJLAO_PROWcfnSpJw5AJ-q2ss5Ge4lu0_U6A-bu5OA2Pcblx97PL6nT-WoVPRhW3Itkk9pXmkBUOrNmVu5SZIP7GepmZ1fvI6IcmE-DZqlOQ_iC5p7oCcbrgFrWEa1RYtBWwb3mAj0J2DPEO4yT4TNo4WbyQe352Tk8QJFy3usXDUQwkj8cUlZQ5hoBg44wSKbC3ymNWCO4ElNt8_jrZ073lHAWoJt8tZO5sjvcodlsixo-AP-BvdjsmDwN9m3DQFCpdvooj265dGJMNnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Forz0DAdheFax8L5csrqq1Xr-fxE48APmwlfbtyBr7eD_Zb2jfmI3PI9RKVX8W086rGyDW2F5b60tvDe_UdbMKW5nJa3P2cjCHGX8mWjTomOQUb1VaQk12x9w7SHp7bsO2bwDxxJlSR9XFh7c8bFD0iR7jnkyELpE3rqDt5_OqB8zz2pavgXC7eRYT8RwPfjxHrA2BpCnG5z2WBRq0pYdKmEgQ_XSFIvE6fWAgXRgHr2aC1KofbVu9cek2HmE9obUiD6dTQBUmzrWQfoPEmNYwcKFCG1jHrvolhhLOCDxhTCrpSqfqyKK_RXrZfAD2-PQM9OJ8L2d5Dd9V5tlmh-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2ymIaCguGjwN5zLQeFa2nQkiB0Ngvn5eWQhv0fKqlUn3W6Y_beRSmUbd3bWcVHrekLscWTw9E6P7ER0td2-9QC6BqhI1OMHScnksaRpgO1k4D3lzzr5KPA6J9bGgTmIJQXtfCTigYwgIh-AVrYSLGHMd8-xVBC-cDxbrOxTl8zgkaBTarD4kU_8KPAn61rkf-uBzEwm1Uz3KsVAIyZWPSxoy_ZjDVIWBSLHiZMi13HXdBc7opx82DYDZ2c2GAv7Plm3z5IXcPOR5cDgqBiJkNIzPAF_uEXRRNXBVNn2ktbFJX0nsg3d1lJM-fG1d6I8l_I9BsdUSHYbNlJ2cfFm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXNeVcxQsuVKHq6xsI-kz7hZWJZA17jLXVoXZt-fTM0FEYRfHcWPCmD-41ApRT_Zl6H1RbzAjvYXKou6i0C8txveX61vk0MwR9YCjprQbNeUolSZ2WMPsUfqurV9f2jJN5Eh8lYc8twc4Q1l4mgoCdICcrTZxIkABCN5I2IUJ5D-mARVVttR6ueBP3vaRxHeZIstgk9mVcpwrP4S098-2cKJ52i3gFwEEH9J_nMdBD3eKU8807bhXfWq3qJ4_sp1-MakrsxdtWyATXRoP2pwTy6pptozMFQxXpk4XGV8Gr7X1psUfe-XrQzRBdC-4ELCE3siVtj5Vp4XD7_lCzSx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zap2qnrEIng_LCwwTr2ZfqfxzMiq8a5J_hrVZjzd0RVYHdiPJ9NWQyiDIP8P81HOW89NbURUDZyry93OpqIiaSbV_LVSJYFgTWdDz-VqOpU8-Nx1bNAEugma2vAgTLoDEeEX5M9IZQTuL1pqwFYom_lekMPBgrLeeap6SKM9YRdc7_aFYMavsfrME75B0o7iKIplKNj2kW6GxlkMXH6Ziv1Q-SWtzWOYde8KOdyTH7iYUJMmZRq07r4MpIPj6zxItw8Ik5-baYgtBBI8rDpvDQXIwGkYmNXBt1q_JS5PJcNyQOQdh7jjIacKr6l0wl6I5a_zW9tU8cEZMIKOsRbqLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1JK5cyOSkcsUx7_hUTj69FdMaxD5TGHdQ6u2mzTzoFdVHgAKZjd5IzFZY18lk9CeZQxGkHclUzcil7nhsg1-DhoINrU96xWmVntcJwOI-U7hBMNgJno3d0TVXTg8yDUjc4TnqECOms1RiKVC6anSJL-JTKVXdtAWENd75HZwRdLn9Wb-7ZJbVc5bzmScDlumtz2Pyvl-bj4Ax2VsVHYXSdOke36aPbV7G6ZfmnTImYwsJHQhjrIwkww4UiSaluGQbOqO7FYDJpP9TzGjXUlBxqtMSWMQJLa_JhhHCCm3ZlophPU1hD9A3jcKSc2Rdu-2qUJwtNM-NcH5T0HUPwQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwrXx8gpKAaCg0O8899xpgpBYnoxFOpO0ItPApTLzOLVZ25KZ3DxXZTBO9dEWpcqDmFviNTVl19r7_Kb5u4OKoBoUcYX04OB7_jH3vn0i4aph0mP10kuG2gIW1FBpgzaFXV0vCi2DpBVLppMuSpVzkyR8M-_J1boEbU5sBH-fPlG8UxBbdPL9BencoclvC3uvSxNC5SE5ui2_z_45oeVTLpxlNoMu4LRdZKhhOCDK2KVljobVpWLXQV7RCpAz-416icSAx3Z0vebmcECLbsMKGJSj1Rfe39dPv4r_WmTdE4hSvVKmgoj6LY2DdyNCKvSdlgY9p9_cY3V7peYXa0PUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O06n_xf4BgOSRYVxB8lJSkAnytUoA7fmtYsvOa7ZAaAvplk5gbX_chjSQVqQwfU8MNWa4zoMgjXyh997peJiarJmoK3NZhRAfvT1KRi4OjCskvqD6JVX_SgyJ5ycYjyzU7qRpdHK2gpWy9Urvj7In-QmrvBmAH4FtbKdznaimM3y8ulWjohEUwWMC6ToJyJI2h49b1tDVBr9gDpdwHLWhAWf-0pfgeJEVBRF0QMD-uh1vW5tmPGvbQ6AyXGN4dTYOruFq2b_FY2yd0t8Rh9vCmZVzYfVoP-m5KiBwtVzPT79umdcu5kQ9pLx04shjjvYzS0GhdKAL-OU0AL3Pn5tWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrcXzN0-vbugzdTYr1s4AVM_8fJ7BmmtJjQdhIKefkDuEn86MQkOgP2DfZD6uuWo8mGqfnshlB4Zb8o6Kgeus_MyMVllhNXqJvg7dYpMHxKgDbkLUtiCi3tuz8t1IX9ID6c-U5DDEHrkLBGS3s5ps3lmFhP0tUS5QGE0tLDWlw1K7Y-AoPj0IFPDOWC8wsVX_cUQQCuWFdKCp96HMSwCvYekEzDwYkfhv7SzOkUgvwrY3e9pHr_B_tG12ZpUItfYJ8kMMCEI0lYSoIXLc_tLxe0RFrSiAaXBwAkNRepj8jguT8jlmNuk3A79RxkBmkFeZsZyFM7S-yH34dgQ4UaYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7rQ1cWZ_FJWWL8NuDHP8RvZuyI1bMt9-rR1K3O5T2t2zkpTckdr8cQRXo1JkipC1ffjUMpD83HygOt4MIoJ-U1j1vNr6Vy1ni96DEald43QQGp7oNpIH3R0f-hu6kXe6GDxBrGDXkjb7Sv-MZVxhQxo9OBWsVHtwZFjucwBMoJjS9v_NOGIDHvqDTca4rMgK69Fq9clRc60HCRRATEh7Z1c8YxHpMcuOyvL3aV4sSIeHY1oclALC6YP0L0Elx1rTnjZAMmxzqgPr7xcM5PjF3CWqiNyYc2PZPjXkR48SdA7wlCmhfYD8RdW0H-aI2kF3GSjPo0yuMCDCHI-sY2ssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/synrapQbdIv2R4KTCoTrn8e716FsQl9Gm5dX-aPRkumvy6HOnQctstGfDn_uXIMpYzp2s05KnyNtLvEJs7KlkRJjk8u-qhf-pb3xb4N7FxRX5ZljWe5C_8bnFE1ZzZ-04O_xOywcSpwgpS-C11cUPXp50sxAzfP6Jw0x2O3JaLF08uqBY08-7d07_yVrHrMVL10sSXdfG5QjMlEQws-OMa--MZxVMuBYwrfH3PgAcCBm34yrpd7uAEm0iiFzofCs74Q1Ue4sjbO7GlydEJsTguPTGgG4KeeVVN59YPcrbUOwCseEDipGnasMHxcn_yKTp4NK-vsZQe6cFJkHvy2m-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXdaYhvYTWIaNqG_Yys5vs9CB2Irnpp7fTJ9f4Cd-oxz94xF3n10kgIpFS__pyUBM4jmftgxO_y20ZcC4-0ihsHwACOH8FvcnvJMBk51yYhUaqHl4ZTEe3fNGT8HDi-EKfEFGO3b9P-53uChLpwA0fzQXxRorrc9woRMl-ZStTIdzfqwUEcvEGpaTRIxUo1ZtlSgJc_LjWUN_hZFGuJPem5LuEikVObsLQclkCrvA9Yt6UC8dy6LcY2foWk7yqfO-NLaPqsmBtJYniEgwYG3nwVSbWkpIMhhadvEdXp_d9LD278QiFu879SyA4Ev02yEIOQjQNvrWNjWrR16_dxjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=rkhrmjCAAgeQzMV4KNSFo9oxd5UmiSx5fq_VSaV4yrj7P7oGbeEI3VQMAlJohq-M559YBTTp9UC2AHd14qyJ2ah7tUopJftW4TMOd5663b67g8toy2rjx4-zgSUClU81ob4ctak9TToqWlVQsM6OJZBj0RUXM4-hgfcoJnHhiBxO3Z1Bepqte8lhmncwRaNKFeAU4gFbYTVCrQxfIvAUqgSI5lOnDao00S0sYGddOCi-lS-P8s-WYuX6_uBAPZa5HSf-cETOLwKxiOOpiMghBg_fA4uu80PuAHi5dyNp5LbTTQ18wW5zW0I3IV0zavb1Hspl5iuzzzrMAunaUBeThiUhHq4g_v6mCydJTp68AyfPTLcbkYTX-Gnqye2Sq431r72kM2j5I8Qf2RlhqJD8ozYVhGljW5Rg8mr1ag8t6-CBH-74pE64WRmEdhY5U6PVUkuNCi6jzmpaMLwiCP-WSDtIwStJvtbotD6lxzvhJhNHF0VVdMmCcZBlOYbjHIUeiVzG_WLONCEmwfWQ1jH23mYhp5Fh3i5RdC7wKUrXDdqsQQnb49V3rXQC8My3suH_R3OqXNCwpQBaG3BOwRbRUi7d9tPpU9sGkl2qjVI2TNxx7vx4O3kft1ygIQPwfPEtfpcIjiNx9E6G4lswKNfwxYAu7B-xlyCvgSh1iUsxn3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=rkhrmjCAAgeQzMV4KNSFo9oxd5UmiSx5fq_VSaV4yrj7P7oGbeEI3VQMAlJohq-M559YBTTp9UC2AHd14qyJ2ah7tUopJftW4TMOd5663b67g8toy2rjx4-zgSUClU81ob4ctak9TToqWlVQsM6OJZBj0RUXM4-hgfcoJnHhiBxO3Z1Bepqte8lhmncwRaNKFeAU4gFbYTVCrQxfIvAUqgSI5lOnDao00S0sYGddOCi-lS-P8s-WYuX6_uBAPZa5HSf-cETOLwKxiOOpiMghBg_fA4uu80PuAHi5dyNp5LbTTQ18wW5zW0I3IV0zavb1Hspl5iuzzzrMAunaUBeThiUhHq4g_v6mCydJTp68AyfPTLcbkYTX-Gnqye2Sq431r72kM2j5I8Qf2RlhqJD8ozYVhGljW5Rg8mr1ag8t6-CBH-74pE64WRmEdhY5U6PVUkuNCi6jzmpaMLwiCP-WSDtIwStJvtbotD6lxzvhJhNHF0VVdMmCcZBlOYbjHIUeiVzG_WLONCEmwfWQ1jH23mYhp5Fh3i5RdC7wKUrXDdqsQQnb49V3rXQC8My3suH_R3OqXNCwpQBaG3BOwRbRUi7d9tPpU9sGkl2qjVI2TNxx7vx4O3kft1ygIQPwfPEtfpcIjiNx9E6G4lswKNfwxYAu7B-xlyCvgSh1iUsxn3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=VsZcoTackuAxkisD-gJHOs8qOAvabQbKVzlFZbOo21CX4UIUbWPnrkKH0-apHvZlRuxpWjsOJVUvNiasc6ieL3au6WFb3dtxuPaHtrDCqU1rpftWd8gpKB7QZBL7lgNIgvL1BuckqI72YQqD4Ts85jG6bqDsg6ggDUcC8C6vCxF7pvNM9xrbOdqIhHy1Yet4EC7Yg02CjKv7xLqKGuZKdF7B5ee5Je_Amz8Zc1yyyEvzhM739-Qu3UBJZ7zOO7t0hLCwKPcjBMB6ozAZcBY30JvJIzSmc1xqBQLSwtUE-ptWM809aE2wA_FqsC3yJJ-AnrGS6cYijlpV2NeTlMd3F3kHAOMU6rnWOSn5to_BphpaqS5iOykvQi3F7XIlkavJzN3jzbV8_6iJhRHgyaB5WWxF4cYi6AymllDoqSwLqbTSKBSaW4WbC_7g2bwp2qRc1FHILsdTQpiAv-Ql8K8LWPGu7bFi2bzyNg6ORHNPEq7Qg3UjbXXECcdVy5UYNKUGkHJ0qa7YUw4k7_xjedrCnN8m4WMfL7jszZJSiixOGhLkje1-1OdCqiGXrIL1UudX0hT6LF_NN2RbvVEZHmpD5b4UycnG1M-A6xUP1P0LG1MituCknd5FN_01n5awHmNetCMKXK_x2iVUURPw7S4rxbqHuz8TM0V-Z3nbynoqAcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=VsZcoTackuAxkisD-gJHOs8qOAvabQbKVzlFZbOo21CX4UIUbWPnrkKH0-apHvZlRuxpWjsOJVUvNiasc6ieL3au6WFb3dtxuPaHtrDCqU1rpftWd8gpKB7QZBL7lgNIgvL1BuckqI72YQqD4Ts85jG6bqDsg6ggDUcC8C6vCxF7pvNM9xrbOdqIhHy1Yet4EC7Yg02CjKv7xLqKGuZKdF7B5ee5Je_Amz8Zc1yyyEvzhM739-Qu3UBJZ7zOO7t0hLCwKPcjBMB6ozAZcBY30JvJIzSmc1xqBQLSwtUE-ptWM809aE2wA_FqsC3yJJ-AnrGS6cYijlpV2NeTlMd3F3kHAOMU6rnWOSn5to_BphpaqS5iOykvQi3F7XIlkavJzN3jzbV8_6iJhRHgyaB5WWxF4cYi6AymllDoqSwLqbTSKBSaW4WbC_7g2bwp2qRc1FHILsdTQpiAv-Ql8K8LWPGu7bFi2bzyNg6ORHNPEq7Qg3UjbXXECcdVy5UYNKUGkHJ0qa7YUw4k7_xjedrCnN8m4WMfL7jszZJSiixOGhLkje1-1OdCqiGXrIL1UudX0hT6LF_NN2RbvVEZHmpD5b4UycnG1M-A6xUP1P0LG1MituCknd5FN_01n5awHmNetCMKXK_x2iVUURPw7S4rxbqHuz8TM0V-Z3nbynoqAcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Rii6SEAG48BwKtZrpnP-TKEmVtiyRWNKtDK_WdKHCDIvj7pSpujnvzY4gsgBzPxZA26Lde-ZxI967SXQykoVXbq2dxdWjV8Tbj3h6oXyYfduLjCljQICGBrZdUgAPN6YGdPr-jvJusGQxNeGPGXggpzLF-f-j2r4cjaJyIYkxmsiZBfCXuwLBpFzPj62oxHl4Vx8s7vR_q_cSk8YeT28i2qzoRY_cpGmx6kzD4WPEMGf4nUThhlvXk3k86hH4DTJDUvCgf4oiLvvhHQ2yHpSNQEjHuv1-gVGFWC50QU8BLA0NdBTe1N677r8-KGRy_gJCfY6UC675tvoWan6U0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=hZCmoQGXtedxQa3WcI3WCs1R0D1FlPPsLryEDiPRmS6vdEBCcVIJr0rC2PjBr-hMcX3aRXevtJ5rENhJsNj_rwqOpF9LeWNvpM_YpUpzshdqn6naFREXeuLzYo4qZcrVlimb7mAtHYr949jkWyAwJLyE0VJT18BHanzwnyMvuXCmH90lyD9GfdQQFteOeVai0UQMNMfDWHLpp4q8_MA4HN52CVpTilO_wFnO7HmzRmbWDTUiBAnAvdeXK9UIl8TYhcHM1YPtJRvg710IhaNCi_fyBohbqIZa98XBOfc8tIAyWiP8wgmDg_n6KSVpFnfUKvgaZwjP004giE1VcH9Wow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=hZCmoQGXtedxQa3WcI3WCs1R0D1FlPPsLryEDiPRmS6vdEBCcVIJr0rC2PjBr-hMcX3aRXevtJ5rENhJsNj_rwqOpF9LeWNvpM_YpUpzshdqn6naFREXeuLzYo4qZcrVlimb7mAtHYr949jkWyAwJLyE0VJT18BHanzwnyMvuXCmH90lyD9GfdQQFteOeVai0UQMNMfDWHLpp4q8_MA4HN52CVpTilO_wFnO7HmzRmbWDTUiBAnAvdeXK9UIl8TYhcHM1YPtJRvg710IhaNCi_fyBohbqIZa98XBOfc8tIAyWiP8wgmDg_n6KSVpFnfUKvgaZwjP004giE1VcH9Wow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSLy8W5i-BXgnwsAphUksDfUjswX3u25rNXUV9m-vnNAHarVGn5dk1xtFhXDG_pMR51HLLgWP1_bHowwSto1HsATh7pv-jJ6OiuPNmeDSDt9J6d4hvdP0XrzPbP0nJVPourj7bz77dzk1unbFBJ44ouXQrs6KGrWAxQ08hWKMhfFlJ4E9NUcZ2VQW0US6mAmvTB4c2uodlvcvrmrBxHHCf4tXu6O5FAD7TKwvJsMoNQwIXRk9wD1xJltSWVyPKqcOJn35GLtaqWFAY3bDxlOnpWZb5niQoKuUKcvPgvdO2BX5XsKh_-3sFu4LhDSPJti6eG7iV9FM3PdXFHnCPd_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
باز کردن بی‌دردسر فایل‌های آفیس روی اندروید با OpenDocument!
بچه‌ها اگه فایل‌های متنی یا اداری دارید و دوست ندارید برای باز کردنشون تو سرورهای ابری آپلود بشن، این اپ خوراکتونه. تمام اسناد OpenOffice و LibreOffice رو کاملاً آفلاین، سریع و بدون نیاز به اکانت باز می‌کنه.
📁
پشتیبانی کامل از فرمت‌ها:
خواندن بی‌نقص ODT ،ODS ،ODP در کنار فایل‌های رایج DOCX ،XLSX ،PPTX و حتی PDF
🔒
حریم خصوصی واقعی:
پردازش کاملاً لوکال، بدون اتصال به اینترنت، بدون ترکرهای تبلیغاتی و بدون نیاز به ثبت‌نام
⚡️
سبک، امن و باسابقه:
یکی از قدیمی‌ترین و پایدارترین پروژه‌های متن‌باز اندروید (فعال از سال ۲۰۱۰)
💡
نکته کاربردی:
بهترین گزینه برای کسایی که با فایل‌های کاری و اسناد حساس سر و کار دارند؛ با خیال راحت می‌تونید حتی در حالت Airplane Mode به تمام داکیومنت‌هاتون دسترسی داشته باشید.
🔗
گیت‌هاب پروژه
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=P2Xw1CXO-RZQMMMHMxRx2Mkdr0CXfpip1L-VOnUo3wemU5wY8yWdkTC9ROn8EtP58eK03DJAkqaNPdaf_eFLXu9CSui531M9i5V5B5rX91pkAZMUkmN07miiEIaviJibTOKYlVsl_PAC49nM8GIVSrP4J3KuiEeC7DiLBQWEog4GkrIJPcH2lOWv-uXJkTLlPSyj8rWqTHTpFe5RYD43df_dpK-aDU0vgn9uMWvwR4o_sPbHRDqw2OY5gqz0TEGt0pUclayqLlCLNAU_2wU0l131cIWHo6MQgKf694tJkzKRRuwnz1XxwkxHDDcighU1UCyWdgzqLSLo4gBQC-tZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=P2Xw1CXO-RZQMMMHMxRx2Mkdr0CXfpip1L-VOnUo3wemU5wY8yWdkTC9ROn8EtP58eK03DJAkqaNPdaf_eFLXu9CSui531M9i5V5B5rX91pkAZMUkmN07miiEIaviJibTOKYlVsl_PAC49nM8GIVSrP4J3KuiEeC7DiLBQWEog4GkrIJPcH2lOWv-uXJkTLlPSyj8rWqTHTpFe5RYD43df_dpK-aDU0vgn9uMWvwR4o_sPbHRDqw2OY5gqz0TEGt0pUclayqLlCLNAU_2wU0l131cIWHo6MQgKf694tJkzKRRuwnz1XxwkxHDDcighU1UCyWdgzqLSLo4gBQC-tZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
با GeoSpy لوکیشن دقیق هر عکسی رو دربیار!
بچه‌ها اگه دنبال لوکیشن یه عکس رندومید یا اهل چالش‌های OSINT و ژئوگسرید، این هوش مصنوعی خوراکتونه. حتی اگه متادیتا (EXIF) پاک شده باشه، از روی خط‌کشی خیابون، گیاهان، معماری و تیر چراغ‌برق مختصات رو براتون پیدا می‌کنه.
🌎
جست‌وجوی جهانی (Global):
پیدا کردن چند تا از محتمل‌ترین کشورهای دنیا حتی از روی اسکرین‌شات یا عکس کراپ‌شده
🏙
مود شهری (City Search):
اگه شهر مشخص باشه، با عکس‌های خیابانی مچ می‌کنه و آدرس دقیق پلاک و خیابون رو میده
📸
تحلیل چند زاویه‌ای:
امکان آپلود تا ۴ عکس از یک لوکیشن برای بالا بردن نجومیِ دقتِ حدس
💡
نکته طلایی:
کیفیت عکس اصلاً مهم نیست؛ این ابزار حتی فرم شاخه درختا یا مدل آسفالت رو می‌فهمه! موقع ثبت‌نام اولیه هم یه سهمیه سرچ رایگان بهتون میده تا تستش کنید.
🔗
وب‌سایت ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmL4v_eKFNDcUQWe14ZR97tL_whDynblFNfSSss3EcZD7Jv8iUJxG0NXSfaNNho7rjyE049tjUwlNn6Ci-dG0QHJu6MSt1KEPx4B18edUg1SyBHjCQSYIkS2Uj-0O9f1UDPZsoYkFVm-Lar1j-E0GPOi_b7psiGGNqhfWiHbbZrh0NjBxxuAyqz87NhcKWYAtS5RQiKjVuvsHlGpeV52pm1Za48X5A4fSms2WnuTIvgwaVTso2k1pkLyXt22ddwMzqvbqyABPUfNncPFT3vq9e5KfrQ7K-tcz5VsHFSpFWhid6Q-WGhE8mqaUa5LYpXH2PpYcmFm3NZpQ9vZYyi4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕸
با SpiderFoot ردپای دیجیتال هر چیزی رو توی اینترنت بیرون بکش!
بچه‌ها اگه تو حوزه امنیت، تست نفوذ یا اوسیانت (OSINT) کار می‌کنید، این ابزار دقیقاً خوراکتونه. اسپایدرفوت یه ابزار متن‌باز و بی‌رحمه که کل سطح وب رو شخم می‌زنه تا تمام ردپاهای دیجیتال و آسیب‌پذیری‌های یک هدف رو دربیاره.
🎯
تارگت‌های همه‌جانبه:
جست‌وجو بر اساس شماره تلفن، ایمیل، آیدی توییتر و تلگرام، نام، IP و دامنه‌ها
🤖
اسکن تمام‌خودکار:
جمع‌آوری آنی داده‌ها از بیش از ۱۰۰ منبع اطلاعاتی بدون نیاز به سرچ دستی
📊
نقشه ارتباطات بصری:
تحلیل داده‌ها و نمایش گراف‌های دیداری از اطلاعات لو رفته و پیوندهای مخفی
💡
نکته و اجرای سریع:
راحت‌ترین راه اجرا با داکره؛ کافیه دستور docker run -p 5001:5001 spiderfoot رو بزنید و پنل تحت وب رو باز کنید. (یادتون نره، فقط تست امنیتی قانونی و اهداف آموزشی!)
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n442sjP8GDnxE1XrSEINuf2IkD5-WNAcSSyOtj5dN5H4eTVKcftSG9M-9GG0QnWryXOCQI0WlUT1iR0vKWQFD0moCWZ43Xux42oybrEv2j_EoeReA4cHWnMQh3pdo9Cdr4kbi5XEwVQIvNOT1-fyKBjXQVKKquFHIcC7kKotnJ7YDYaTlFTwkXE3NH79vu2q6fOJhLhQM8BJTIuwqjTcILohAbfROjBzCfPxRaEV9-Q74BDRH6IAsNJ2B2SYoxZGXqvonZF7tZdeOZ3WeqUukkhhco6zlJjnVhHl4cBVjvahimWp3CuHEGU2m3s1jlIwNAWNaJuWde3BEG2_k-5ZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRENcd5DAiVTDc6tCZAZZdp_i9lo1LbkG0gLeHPa3lNvSt8RMSyXeEvx02RqPGgyk3JOmhhjSVR2kVlNt0bO7PoylXY8XzUoc9IQpLo2OAaBeMm0LADvoPniLZ-O0fmBdl53tvxq-UeNdttLEC8aJufzQmSJDi4RzLY0yYgzbA6cQaKeBEGr5cpyZLgn6Pz0_O9BXiIEcDrT1WF2Y-sjK89oVcOX8ShJ67uanu93pGuXBidwn7ZGyHcmdXAJUFFI9k9YXdND2T9BmHn4uP0drbC1EsuvxBKqxKtpaXsgAPUyoeIk289v3MJOh03KYVjf9lcUf1cmO0Por3-Lcu_8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eS9kXrrB6dDSvQtc9ZZe0_H6BOb5SmT5fpY5KhKhmAlpNLCiEhZyitIayJmcI92826blCstpzQ_KkHLVYCDoPWGXLw5bUZ3W8S-jLrwnn4m5V81LH0DgoEcunhzOs1BmAOq9Owtw6jawmOLshOstcQ0GXr9Mcb8MbssmY0Feais1X-Z1hCNi9ayce_F9qM8y5-7D9yxo7Cs1hvErThWsdllY-PfyBfxR-0JqIGZCDKt_o7pNbMHixYGv9IvKEe6OxKzuvEDK-1HH1JID6n5NqwfxrZj4vij0vptlGsq-z0qorPPgThqj-eJweL89sOijj4lr_mxsi-QOeBvGx5O2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3iTFH0ALhjmR8h8CdY_UaDOGwqiGjD8GemqAGUjuKQXpdSQPx_9l3h6rCqtYd-IXvS11YoBZgP8HjQx0m6sg4JHJXIFB3RtC7Rn5cV_p7kMfIn7DH_XALTHAgTOOYUqTvQJxR8VfsnzgFhMY4XWYstbT0cfQRj-hbpyQRSAjiQNHdTBrl2e1sEVXzyOOce4ORvhJdmhKaHjGY6meTr7Gx9urDtuWjO9_386wPekahFPfQKXJLj_ynSidWk4bVTUQpN6td9k_AulB6BB70zuRLKYpHXr7W5KFnDmnEqtVH-nFgxzt4J1bGhqyCPooJypyZ121ahdy2FQmRj4G9eTMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📌
مدل GPT-6 Astra بازم یه حرکت دیگه ثبت کرد؛
بازی Portal رو تو 23 ساعت و 43 دقیقه تموم کرد!
مدل به طور خودکار شخصیت رو کنترل می‌کرد به طوریکه هوش مصنوعی یه تصمیم می‌گرفت، بازی متوقف می‌شد. GPT-6 Astra با استفاده از تصاویر، موقعیت شخصیت و زاویه دید دوربین، تصمیم می‌گرفت که چه اقدامی انجام بده. بعضی وقتا هم تصمیم گیری هاش تا چند دقیقه هم طول می‌کشید، اما در هر صورت تونست بازی رو به پایان برسونه.
🔥
این کارو آقای "cozyblaze" با کمک اشتراک ۲۰۰ دلاری Codex Pro انجام داد.
🔗
سورس پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayv4DCMX57eP6rMMAojA1jdKJb0BgUzejQj5lD0vdv1YBtkGZstaXz1g7LFOKj2DDfRwL9WhVCQHT8rvXyT_R1KLrygx5JKUHFIQh7B8dBJRj_aTVDIoCBd4vXx1ccapNYx-zeeHCIvo2TVF6fNB8oL48bFOXeDXT8EmIfTD9AypqJVXGyUdE8SVj7m9MPXDRjbwPhqhmyVlYfderLSqjzQnJphIS5JVuwc1wD_0NqbEWfNjoR6F9kErxRnCo439-sM3ikApXVvH_LBZYuTFqquQh51C0KIgDMX4YmZsVzvGi2O53s00Mo-4_lF1gQuIaio4Sh3rec4tNkpfkNNG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعبه‌ابزار همه‌کاره برای برنامه‌نویس‌ها با DevToys
💼
اگه خسته شدید از بس برای کارهای روزمره (مثل تبدیل JSON به YAML، تست RegEx یا دکود کردن JWT) مجبور شدید سایت‌های مختلف رو باز کنید،
DevToys
دقیقاً چاقوی سوئیسی شماست!
👍
🔧
بیش از ۳۰ ابزار کاربردی:
انواع کانورترها، انکودر/دکودرها (JWT، Base64، QR)، فرمترهای کد، هش‌ساز و فشرده‌ساز عکس.
📄
تشخیص هوشمند کلیپ‌بورد:
به محض کپی کردن متن، خودش می‌فهمه چیه و ابزار مناسبش رو پیشنهاد میده!
🛡
کاملاً آفلاین و امن:
تمام کارها روی سیستم خودتون انجام میشه و دیتای حساسی سمت سایت‌های ناشناس نمیره.
➕
پشتیبانی از اکستنشن:
میتونید ابزارهای دلخواهتون رو هم بهش اضافه کنید.
📌
لینک مخزن گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=quu-eVoSJ9utNqeeq12RrFQgs36CZMoAmCCbR1d-3ZNCFxsli_GMvP4Q8lV_d-9fzy3sruBx_PRBSsr1XeAJtm_XUNU_0rtic-k0MQaniGeVnRXeEzFWx2yFPKSqcl7iZi3O1sFbrdcIQ2MmxZHaxh3cT2IlhLp521iieU4hwi6B4jGhmsmxwbBllhZOyMquKdInM_p9ItAgws7-FwXO4OBSox-rLDm5h-Aw8Gjq16sD0-9zeQxgIyGuB1CPlH8SQ1fJhX7WZJ_w1O3sIYejlIRx7AAFmYnmg_MbFc49SP8Bd9orv--nrxjbG3tB04vb-W8qzKhOugySQtpNSkBidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=quu-eVoSJ9utNqeeq12RrFQgs36CZMoAmCCbR1d-3ZNCFxsli_GMvP4Q8lV_d-9fzy3sruBx_PRBSsr1XeAJtm_XUNU_0rtic-k0MQaniGeVnRXeEzFWx2yFPKSqcl7iZi3O1sFbrdcIQ2MmxZHaxh3cT2IlhLp521iieU4hwi6B4jGhmsmxwbBllhZOyMquKdInM_p9ItAgws7-FwXO4OBSox-rLDm5h-Aw8Gjq16sD0-9zeQxgIyGuB1CPlH8SQ1fJhX7WZJ_w1O3sIYejlIRx7AAFmYnmg_MbFc49SP8Bd9orv--nrxjbG3tB04vb-W8qzKhOugySQtpNSkBidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم 7 برنده خوش شانسمون
🎉
:
1.
@reza1629
2.
@mhti9
3.
@KIING_ZOG
4.
@Gogogrugo
5.
ＮＯＢＯＤＹ
( 6641463426 )
6.
@an_Y008
7.
@AshenOne2077
برای دریافت جایزه به دایرکت مراجعه کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🥇
رکوردشکنی دوباره از GPT 6 Astra
خبر رسیده که GPT-6 Astra تونسته تمام ۴۸ مرحله بازی «I'm Not A Robot» سایت
Neal.fun
رو بدون غلط رد کنه ، خیلیا جوری جو دادن که انگار آخرالزمان امنیت سایبری رسیده!
😂
طبق معمول، ته این هایپ‌های رسانه‌ای خبری نیست. کپچاهای تصویری سال‌هاست که عملاً مرخص هستن و حتی مدل‌های پارسال هم با یه پردازش تصویر ساده دورشون می‌زدن.
سیستم‌های امنیتی واقعی وب الان با تحلیل رفتار موس، کوکی‌ها و الگوی کلیک کار می‌کنن، نه با ۴ تا عکس چراغ راهنمایی و خط‌کشی خیابون
😁
تست کن ببین رباتی یا نه ؟!
🧐
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmkh_FAhuHcNtuDMUoMHwWCQ7OsH6cY5oWyVpL_GxVE_uTi_eFiXUhzCHkM6saKDPOWymjC9blR8PkNTIDHRkiv6oyNm1eF1ZVR2v9W_n_GfxwXLdNGbvQ1jI2pVs_QfQBwpBuLWVDEnmmyKviHI4AEeh4MG-njUkI1lCHdjo9QE9BfhkKl8ENNWj3diSEVBVOWAGTrh0CtWBN-D0Cq4Wgr1PF_a0rj2PehopRbLhpn8OnktWwy-ftJ__YPcPx_bClcyq6vTMv84Hrzxpt9ZShg4uQduupeSUagEUzNR60JWmWkznqmd73KFbuXXknhT2Zm84QcTIrESe6hsr7sWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جداسازی صدای خواننده از موزیک با هوش مصنوعی؛ تمیز و بدون دردسر!
🎤
🎧
بچه‌ها اگه دنبال ساختن نسخه کارائوکه هستید یا می‌خواید صدای خواننده رو برای ریمیکس بردارید، ابزار آنلاین
AI Vocal Remover
دقیقاً همون چیزیه که لازم دارید! با استفاده از مدل‌های صوتی AI، وکال و ساز رو در چند ثانیه مثل آب خوردن از هم سوا می‌کنه.
✅
🔺
پشتیبانی از انواع فرمت‌ها:
هم فایل صوتی (MP3، WAV، FLAC، M4A و...) و هم فایل‌های ویدیویی (MP4، WebM) رو به راحتی قبول می‌کنه.
🔺
بدون نیاز به ثبت‌نام و کاملاً رایگان:
پردازش تماماً در کلاود انجام میشه، قبل دانلود می‌تونید آنلاین پیش‌نمایش رو گوش بدید و تا یک ساعت خروجی MP3 یا WAV بگیرید.
🔺
کیفیت و دقت بالا:
تفکیک دقیق لایه‌های صدا بدون نویز و افت کیفیت محسوس سازها.
💡
نکته:
برای آهنگسازها، تدوین‌گرهای ویدیو و یوتیوبرها برای برداشتن کپی‌رایت یا ساخت بیت‌های بی‌کلام، این ابزار سریع‌ترین میانبر بدون نصب نرم‌افزارهای سنگینه!
🔗
آدرس ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri1OwLnJJfipXjFjdkJd6V9owF7CQoBwq0gff3pZi2-uxf7JtrTTZ7Ynu4K7PLmMlhzb6y6ymof_6gyiCstjgmfIC9xRrKmI7nztFk_YnO9s1S1j0JmZIZYZg7qVjxi9LeaJ65dG2Xu4LAYAdVm4PMvF3EPZMhiT2AGZq-t4n1LfRkyWwxhstZDBj-xZKOFB7QMof-hE-uaWCzzGEoBkelBIFKchVEy8yMegF3UJ9m5xGPfbGy1HuUT-rZAprQRd9HSzHEjuI8-mqX6ba9cGvp0nhpfzcPzc3Fq6tVQ29Sk3EoYz7eCvETWbZ8UKP8VL467ZSvAszG-AWb0drLGyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل گوشی اندرویدی به یک کامپیوتر دسکتاپ کامل با Android DEX!
🖥
📱
اگه از قابلیت محدود سامسونگ دکس خسته شدید یا گوشیتون اصلاً DeX نداره، این ابزار خوراکتونه! نرم‌افزار
Android DEX
با ترکیب جادویی ADB و موتور قدرتمند scrcpy، گوشی اندرویدی شما رو به یک سیستم‌عامل دسکتاپ واقعی با پنجره‌های شناور و کنترل کامل تبدیل می‌کنه.
🚀
🔺
تجربه دسکتاپ چندپنجره‌ای:
اجرای اپلیکیشن‌های اندروید در پنجره‌های تغییر سایزپذیر روی ویندوز، مک و لینوکس با اتصال باسیم یا بی‌سیم (Wi-Fi).
🔺
خوراک گیمرهای موبایل:
کی‌مپینگ حرفه‌ای کیبورد و ماوس، شبیه‌ساز جوی‌استیک WASD، قفل دید ۳۶۰ درجه شوتر (FPS Mouse Lock) و حتی شبیه‌سازی ژیروسکوپ!
🔺
دور زدن شناسایی امولاتور (No Ban):
چون بازی‌ها مستقیماً روی سخت‌افزار واقعی گوشی اجرا میشن، آنتی‌چیت بازی‌ها شما رو شبیه‌ساز تشخیص نمیده و بن نمی‌شید.
🔺
امکانات یکپارچه سیستم:
مدیریت اعلان‌ها، پخش صدا، انتقال فایل با درگ‌اند‌دراپ، رکورد صفحه و تعریف پروفایل‌های اختصاصی برای هر بازی.
💡
نحوه راه‌اندازی:
فقط کافیه گزینه USB Debugging (یا Wireless Debugging) رو توی Developer Options گوشیتون روشن کنید و برنامه رو اجرا کنید؛ بدون نیاز به روت!
🔗
گیت‌هاب پروژه
🔗
سایت پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXlokN_5V1Lbytmktwob_jW_vxE9ommGAWrY34C8RsW8uyXPHbFaRHwsJRxvSuIICA7JHsVU6YZ8PmgfmHF4j-tLc795dCIIWJ2RCERE1ETzAd85xLZsc2rQsw5Z7mgqAW2hzUvaw8qgyiKTEdV-116N7aX5L_rAibJ8ts24YgvPIi78_TrSYBAMSwQulohHj1yZuCtdc4QXo0M04SMWKnyZQNtMm5-MxDDSqYVMn_H81vWvbGUj2970Y8NhEApD5uOF31C4mfA-U8lwCcGWlTsyLmTgAXsKxPDmST3fbCkP8WwYkg8s5Rb6mCFxcg_jUBtuWBTp1BphIG7Sh1WBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن مقالات و دیتای آکادمیک اروپا؛ گنجینه‌ای که کمتر کسی می‌شناسه!
🎓
بچه‌ها اگه دنبال مقاله‌های خاص، دیتاست‌های خفن یا پژوهش‌های پروژه‌های اروپایی هستید که جای دیگه پیدا نمیشن، پلتفرم
OpenAIRE Explore
دقیقاً خوراکتونه! یه پایگاه عظیم با بیش از ۱۳۰ میلیون دیتای علمی دسته‌بندی‌شده و رایگان.
✨
🆓
🔺
آرشیو عظیم ۱۳۰ میلیونی:
دسترسی مستقیم به مقالات اوپن‌اکسس، دیتاست‌ها و حتی سورس‌کدهای پژوهشی پروژه‌های اروپایی.
🔺
بدون لاگین و کاملاً رایگان:
بدون دردسر ثبت‌نام، پی‌وال یا محدودیت دانلود، مستقیم به منابع معتبر دسترسی دارید.
🔺
ردیابی شبکه‌ای پژوهش‌ها:
می‌تونید خروجی‌های مختلف یک پروژه (مثلاً مقاله + دیتای خام + کد نرم‌افزاری) رو به‌صورت متصل به هم پیدا کنید.
💡
نکته طلایی:
برای پژوهشگرها، متخصصان هوش مصنوعی که دنبال دیتاست‌های تمیز و رسمی اروپا هستن، یا کسایی که دارن روی مقالات بین‌رشته‌ای کار می‌کنن، این ابزار مثل یک میانبر تمام‌عیار عمل می‌کنه!
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVsm_UkyrO2f0Q4x_Hl19Vc162DHZxf0YN2R-AI7DjtB7ssRWYEB_c2wROjp5cIEhab_qPNAPUBB6EvQUKWc5CdLPr5a-4cagVG1HnLK52NPkx9QlUZ-4wJ1xkdbX6NmlppmLIns9lm5A7tEDgf_-mjt17u4vqTS4WMJn3dknO2hnXro4R1UddiC-63IZkUlo-3GW8rXT5v4Ba9RX0n9wM4_F6zdRVJnWq3Mhnkp3Oy_n0DHSRelgzrhQQ7y9YoKFrTmqIo8B85gnEGPMmca7VEVqioXwmupz09kv4CcIwxfeT5YMxvrfETkzC6Iq080bbKStkUhyrU2E-_FFzqBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیبورد «شریک جرم»؛ قبل از ارسال پیام حواست به جریمه و حَبسش باشه!
🚨
بچه‌ها براتون یه پروژه به شدت سمی و دارک آوردم! این کیبورد اندرویدی اسمش «Соучастник» (هم‌دست / شریک جرم) هست و کارش اینه که موقع تایپ، متنتون رو آنالیز می‌کنه و آنلاین بهتون می‌گه ممکنه بابت این پیام چقدر جریمه بشید یا چند سال برید آب‌خنک بخورید!
😁
🔺
کاملاً لوکال و آفلاین:
نیازی به اینترنت نداره و داده‌ها از گوشی خارج نمیشن؛ با llama.cpp مدل جمع‌وجور Qwen3.5-0.8B رو آفلاین روی گوشی اجرا می‌کنه.
🔺
سیستم دوسطحی سریع:
اول با یه دیکشنری سریع کلمات حساس رو بررسی می‌کنه و بعد مدل هوش مصنوعی جرم یا تخلف بودن متن رو می‌سنجه.
🔺
پروژه کاملاً اوپن‌سورس:
کد و نحوه کارکردش روی گیت‌هاب قرار گرفته و برای گیک‌هایی که می‌خوان اجرای مدل سبک LLM داخل اپلیکیشن‌های اندرویدی رو یاد بگیرن عالیه.
💡
نکته:
هرچند قوانینش بر اساس مواد قانونی روسیه تنظیم شده، ولی معماری استفاده از مدل‌های فوق‌سبک لوکال برای پردازش آنی متن موقع تایپ، ایده به شدت خفن و قابل شخصی‌سازیه!
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyk-sfYJtAaDvFwMYSs1Mrc9sTgZYThxWw3oZfA8KHUUrHx0hU2GZbXJz-4mb88t8IFaTe5LrSTCWRIKWD3P4EHGpXYfRKqDn1OEfR4pAYkpMh0k8buLB5Ou7SFiUqjuopRMJlSpn0XoNdfqbZdp64SFx5xRSmct8QIS80cW5PTPL8at4gpfCfUBvqjqrfqNF4IiHXLYoUnXIxrwRJnP3s4CsTsaUGitUCVq1ufUYYxL7QCsVkDc9SvjWe_o77Ka04Ee6qWw2AZQkJs4o9MKzgqvhObZC5RDyjF4kV-KOwzsjn3iatUR9bBL1idbaf8dEgqWGT0-HQEu8sHi4nZ5pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoTD9Wu3s6EvA_BhzvdyBwhLObg7ddWrrGI9qcY2FXoObVq_e_JGbhWL9f2OYkpO_B6ekLZIKivwAt8tmrqBt9mtIgupedtrJQFLjKoivw882PEX6Sp93Cna1M1c8vXMMZj_p651U7vI0pGoKlhiFGfnvUZcBIRgZyyp4MHcWDEuxVKZ3XMzj4k7tIB5YY1G4SwpNJKfNAJvBgSI6e1KtXjCtZ_Gk8FMrfSGNN3VSPBSNtPys4XFnTrnhSQXr3lC-wZdeau4IoxJNAQN3YxEnNDIPzoR6e4FdsgIk0kdrpo1ClxEvTEA7L78fM5hsKtQ0gE8ZUPZfqevNvHazI9jCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKBCft8P8-AHWju9VLT6UD5u6ywvelYmp8IRzQReWJBPYV_bpgVmJ41v0-24Bl84ZlsZU6RWpC26hQgjiStV_YOTJbQdlVdQ2zUSuVYUvFji_Y7trdNbwrSDrMiO8ye9MkdXelLjjFEOiskE3v2BalNOSHnsGlfC8PJeI2DpSoVDbvFROGWgMEfvDJZvPF47OcVCIUX7ANRFhSi-CR_OvOYwFplrVByI_fM099_nXIw-4raHqIf6kH469iPW_4HEBdAq9SElQ7vW2aROJuqi5PajnNNHJug5I0OIfhuVz3HcIYM_ks7Ccz6TQEA8RHP39JPweSYtQnnCE9ukwmmv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSLg9rzWgfg99dDftMYwFlGnjEv6RAf2IaJ28zf9ph4lylTkHZT283Sox9L3k_QZihjaA-ZBG25kweLYV7LOsoaYiM7PifOVThdcde7udPgEwZgsH5beX8bZ3BnJrYVyTOtHnNg1VWkPpI3vXO1aSl0aeUUvMCw6afEXHxalylLgYmj7ab4u1PPgiJ7ZPB2ngErFiOQO-3vYtGszNxzK9AmGd1IIgbRBSPE73RRhtJjW20PUs4kZnXTS-rdtUvGZExeAw73rS51aXQKEpajVRjSgPe7Fgpd0DgYjueYq032gqCFNmwF9zcRE583qtEeerJ7dWCjsMPv1RAzAHuo8Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV1r578fwcD0B31vaGUPpUqups4tgIGxHf9o0awJsusRHnW76yR7GIZPuamhODWtUFhh-MFu97Aq7QNPzY5CoU7YuPqsosmcJ7uJ0tedawxalSYkALRcl8uX1hslrrFCqhGOADE9PZwBHZoe8zyR6dtDURGnu7tLeYjYPUBrWhd_YnkE_cmVlcFmaRX9HyAlq0MY4Wzm2G4Hq5u3zl-5PWX1_Ejgt7TxzvAYGCXyBarP9XWFKrTjf4BZskmF_yvAdK8wIgQtxHnw6ly-HjPmaIFolezuRoPznqlY8WykeDyHOk4KqKFL2tPKG4pRmEUcCeIsNHe9KRGieXhYMr-LYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buwx8uu5-xqoW5aki6brhZglC7PmeXsayCASwqF1ufEoUTDBTmqosicH1Kj3rmt94Z7ZNUKf47FaVEOYAievfMtQ_j3-H4Pw_KjVqLxvVvCChijvd0t5_k5xhORufP_nGmq65IXxxZ91UInAtt-4jSryPE7CTpaa_PX61kIxtxGYV6CMYocOPMrKByNR4dpgKXQFajKem8BibUI6xLs4Uz0ubisgBtW1jvMXtbVEIRA2fbvrlQROOrHro28j6ooHh1RsBrXjuMQjVlDo5POp0rkFgZfXlQpEgVszxh2Uc6ZHi98lAnqyu4WAFhiSKVc-M40aZ_mlwQ4rq2Yp0VsB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ3l1Z3gysminu_kl3NrB5WSHG5Hy5Rb1oprOG_Ma9HOQ2cROGYhMqzFKIULSmRXVcZLhD13-yPy7GUjufg5QAAAF2Xmn9cWsG7G-tWUTXmxKPN20r60Qg4Zy7Sb5dCcQoySzLFOqe2c2d550yRZGeutL13OU3TFCZN_Zbqwkvc3gi9T4iOgCjTdlCqih_Q4vlwxGQQAdk5hGt3-EsmlMlZjCJxG1haJyzXZyRE-Z8XSEOvu5M5FrSu2l2PFEvbD0kriscAm55e14KJHMQH2VW9Y12EIDWfbYvsSvWf0oEsE9j7G6SKzZPfonqsGGcKiiWaIiVV5tH32yun-CSbElw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeZksLkojSi4YqEEGl1ohXlzYk9Ja1E5Qx97bVZxhEqQAFGZDpvViqB5ACf9M_1vVjdPW_Tcb1VqK88iDTM5d6tIiRwOxpr5OSVzMhlm9wiJP3eHMLIksZcz6gVWSESc4zLcLKSu06qkfg94MLn2sIH_5JyCjBAE7rTjCKyke6CQF4f-xrUD62OW5P4h6p2edEDM7mJZb4oka3-lv1-FftV90BwaXiYvDp3fMzVSbqRZBdBIZByq4baFlGwX1ceDw48BkDAYoWGPMYC7UW934cNBXDhWezQbyWHP93OzXsAtwJv4v4ymaBJ1jIJVLhR9D8n35HeAsM3Rfybxa63ylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnfmrWAAfn4fljev-1y9dDA62LmKLuj74oziabEpjc-YKAZ1tIDVveJSdBsEI5CStfG_MJfBsoeiaRzRnetNdiCZbGLycNkRL8mqf5f4FSJMbjc-AmrX8aoRyHZgeu6mJxvhvJCceXsF9Yi4o1qqqpsfNLtjICL59eiMCWYrQ8cqW1hrlCiWIHHOpq-xGj-uNmVXOlRsgm6cF7tEmg8jgtN_jSb0-Ns4hdECrvmGTE0Gmjzj1fUPre6MB1k3wSLJaMRE8tRaHPuWQWkSDIy1JTHesTSoLO35awvLe97LvsiibTG2twWaVZONM-UX_qF2Ho2TZQM9S_k6vIWPvS6JMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXBvEvpIIKga5u-_fzJVa80txQMdHlVCzCSdFt_nPOtqbuWlhWAaFb5BqvSTlnCk36DXyr0WfTBocZ7swh1f0MmGje5MN4vMpZLVj3yRrEv8zpv5lwbu5oF9XGZN1-ZobNVJNWYi2ux5UeH20L16oV2SjStN0zo0kukrLjOrXsAPOBrZIv9QEJ8TI09R87VvwmM570jvcuykmzKZR2Kux2cKIvSE89KWbbZJUxWwZlUhucA4V2iNyP1NvJut9PhAKgdG9PRmmya5YqFOwnpZc_45dQkibHJ3nSyhAAiOmk2jLyO4J-U4hXnT0on5ihCExR76r9syf5NM7wzmDuGErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOBgseAe-WUOYKkpExsTw2LJo72lRnd_0DJ_329nCRVDO5jiMkYR4a3MSBqjsMUrD3D-CfFXlAbN_bsOPD2sfN4ZJqftVZ1X19crZHrziUatIUnVccQwpNHOLbNSRRtaFHOIFE78Pg2j4Ae2rLV45s4muEkVMtlXx9PZqE849KDsqdeRLALzCmiirS0SmpoqPY81qtPfvfem-6QijvaeW5mLaAP1Az4Cd66K_ntWMi4I_CZd3ii6urNW3EXgAEX899hjt-ZDAlTBl9oyKxf9shWEDRsvvc6ZKRKjSq4iTzmYWZq6og_QC3RYV5tZ5H1yMirwv-7U7h2b7Y_njdbw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8Gyh5BbCUyxjFnSi26_6zaECAhlCKL-BAVxRoZSRmxAbMYe3gsWUTCfZlyoz7P436U2nnUEFJGHOQtruY855A0Kx2C6crf33DHs0Vb3-dI6qoc1TG2nUsG67dPM-x53cy-2nplPRSIkuNISzUTxkULjjcFdPBOGTHhXRpmKl1nFheavexZZe0d6YSl3QmPgkao7yKQhyBPW0Dzl8dIjeOh4wQ0wJuxEqQpTXr0S8VoytQ3rxFeLpLuQmkmXh4ZcX2z3Z1SZ1ArSeJQgk7IwjTaC29kIcSe1NmLRFoMpZ8BFUwidzZlWBlyKXxnWwXU7Xta1njwxV0k5Yiulfmj2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLMyFf2p6wG120ATVpiY0oqP6s4JNd1aNKxxOqWJ45hCF2qnc4vVJEz9XA6PiP28fKNEl0hpX2-y8cxzphjpTkYYvcYIOU440uxinG9JBnJqD0uT-8EWmc3_OZxdtFPmzP-rrYD0vGQnXG6OVWBMMB5S1Wei2IS4dMfVD7x3VB3mJzMTuq_sobb5Sd3FX1qGam8Hv3mqbseWCetKwzRRBMwlMJggIfzXOQIUNrhkWeM2vyzxo0xo01suuMfB9bueRhKCC0C9akXDiyhhIaLFMGZ8rGYjSMCHnKpwv3MA2VBUxIK4Rc_fKA59wzR8UEnkVr2GF0GrsfOKjbIwx4KNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7pR-m1NYgeTzDe79oH2YWDicWGYhYJl5KgTuPw1nrANsCEpcY7IGQJHeo1TDOtZr1SkS8_rOTlx84hApOi8Kq8exKD4RNHLcCn5VEImrih3ukVW285J8wbV58CPpaQPdoFcUzakKAxgc0rrO2IB89YVdx2y2PvLlTqckzhPB11ZVZhscqBxKkJQK0F3ClfYEKqpi2GTA_2aU_POLDsNue2QkGyDcw5rAGptv6s4akuJzC1ENfnOzOzh6y7HYYTs7iZJk-s3XP9-0tPcjfro1hhY9Hl1-k_ToR8YlPFnvkMa9FpOxaECgmcwVUUUBMOXBj-cd2XShsk_l4yhHod_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqViTym7CTe9ERG5O3j4boKfI8rsvqKLMddGBeW7UczJiiXNfI1NkUcN2G_g_fS5N-umyI313WhxTDelCPfjy1yM-8NFEe_PScirHhPBdQwNsnDPajGESeuiea9N76Jy_N6ymU3IIRTskxGkLsEeNC3ACao3g5Kc_QEgz6dkaEY87OMcZOqwx3uAwxWy68aC09YPwRz7V3FQzFRCnpGLOEFEHah9ANZwzKBl2KRsQtb4HLWGN3uuODFxF2a17GF9qtKwXYBJW-IbOqs_Qw5DoYc6aU_RsPqopvcER84S286f7lfgaoeT6jGOmhINYXaeF_fnYuiDwjsJHt5IvI6G4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=Na2YSHokq3NMLRw38rjODEPhAc-yPgdo3SxWiIbbiaWGfP2T2_PEOgsRbdAN621rX2rkEmJnR7IbiREyuLectaprd7bygfUOKZ8XRejMG-hqQ61LcrRCm0L10-oQtIh1lk2KqLbo3k-ZS0TRgDiNMOJ7vHEJ130QHzaeskpLiNIj7ZzNTJyjLm-I7dW9PXhX_y0lRU_UzVmXVMCDdbv9dGXoHGRPMiTpmL7dVZIpkws9zdWhtWr-d7lew76L0fE03iRR4pxVqmDzWFlHVjTgHyiLPiQLNjTASR2rRftUiVeUOFhegnRdnXqJm9o_svuesxbTN8_LoFV0K73HkQiMlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=Na2YSHokq3NMLRw38rjODEPhAc-yPgdo3SxWiIbbiaWGfP2T2_PEOgsRbdAN621rX2rkEmJnR7IbiREyuLectaprd7bygfUOKZ8XRejMG-hqQ61LcrRCm0L10-oQtIh1lk2KqLbo3k-ZS0TRgDiNMOJ7vHEJ130QHzaeskpLiNIj7ZzNTJyjLm-I7dW9PXhX_y0lRU_UzVmXVMCDdbv9dGXoHGRPMiTpmL7dVZIpkws9zdWhtWr-d7lew76L0fE03iRR4pxVqmDzWFlHVjTgHyiLPiQLNjTASR2rRftUiVeUOFhegnRdnXqJm9o_svuesxbTN8_LoFV0K73HkQiMlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_LjgG6HxlBeLRg8P4R1k-UEfrTHZDFgn1MC4pgPaK0a3c1w8-jnStaz8acPW5UzT8lHyk37PLRXE6XxulLKAQiEbCxlIkqLQnOjyutYUm2eLqr6MQm3R27B69C_SMfgV5-DZjF86-QFy-UWZrxKatm73mxxkWL47v7t6Uvvmia1s6-RedpNAMlBTc7Vr1rOzbyZAa62oKabHNnQffOiHFtrvPbA83Gm2zdabBZaKYPi5Hw5PlhVgYUKL5VUXdotHAaIvELaHp9L25uuGQugWkehztnLy8NsL99YDf-rooKmyk1vRf9uvvRmtTqxtokTikLbNnFXgQV0M6a2wxVyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhsC1f0PI03k4H8RILBNtDjtng9z0YsNm7Xmgw-9zLHDJiKS6vHpw_ayANsjkvc-tk-JwJSaQmpX0UIs0wil9u18S_y5BIJ0lSWpZmGYTTr_rcP7eQxEPkw-tOLjAEzACXV_DEDGiq7pF4ZA6jOKjxV-lCO3_HJo9FPs-89PxQ2n8kxDZWR9mf5GLCLYwLHBHx06dGWTXeF0e0SPdHX8753g2cs75aLSw1aXBMdMDcZudghMNZ6ZAj07Da5t1L__hBz6tw61SoYx1fXpB4AxR9Rkv7kNAgB6QaAsnSOoaGyBjz3bbeji-H4GKQijyUb-vDSdF7rzb-H7Dq6KnuEVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=TAKpMkdU2M0GfTt2ZGzDq8M8JWus33aeHCKKihkl9a7cvUamq57GSl2VLXfQ-iTr8769ssZIncAUCHqG7ov4-xpBVGxQM5WHmFL6dUiqDROQofznF4IAlAGwLXoNYCryFjvpkO_3fKN_aj02uV7RvbW09J5aGO-DVW9OyazDJlpkAAjktFDqXuX03geyRaFHApndPnRP3406g-nnHTgiVf6ar4I-xpWxxLm72UNAioWE3MU2zFgZIx_HodWdDcdq7xnB-FIjRyr8BF4YIZHxsMBmavY-ln_x682ZbOxnkHP9KBAlS5eAWKnwrtgVy0g7_YBUlEABsrkFOFiVbfI2Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=TAKpMkdU2M0GfTt2ZGzDq8M8JWus33aeHCKKihkl9a7cvUamq57GSl2VLXfQ-iTr8769ssZIncAUCHqG7ov4-xpBVGxQM5WHmFL6dUiqDROQofznF4IAlAGwLXoNYCryFjvpkO_3fKN_aj02uV7RvbW09J5aGO-DVW9OyazDJlpkAAjktFDqXuX03geyRaFHApndPnRP3406g-nnHTgiVf6ar4I-xpWxxLm72UNAioWE3MU2zFgZIx_HodWdDcdq7xnB-FIjRyr8BF4YIZHxsMBmavY-ln_x682ZbOxnkHP9KBAlS5eAWKnwrtgVy0g7_YBUlEABsrkFOFiVbfI2Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=DBP5vlZflosEBZXC3a3eiH0JOF1bzQBa-_JA1K6MuIpx6rMLfPEY3Cnv2fu-TVEoWpDcM9R3FgYbzPa8v4EHoh0h0UakSHE8pIgZdKpkYar7wBgubg0yXGqKaHOaSqMXGMjb4PJD4JG55flPR0UZhH4veW9Jtv0uVFLLevU0_-psMS-6fuh8ANTzwg-VyDJLNbkBrJIg0XOLJQMsYESwPaMggX5-MR8rfm8yNb1mBwIWszEnCeLqNtFBV4hj6CuWJv2AydDOLG31ZYeNdXyqKvylRNl_TxHKklIttOOVovDMPTDKuiGI19n42MCqFiDW7rgoXEsT69u4wToVQFVq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=DBP5vlZflosEBZXC3a3eiH0JOF1bzQBa-_JA1K6MuIpx6rMLfPEY3Cnv2fu-TVEoWpDcM9R3FgYbzPa8v4EHoh0h0UakSHE8pIgZdKpkYar7wBgubg0yXGqKaHOaSqMXGMjb4PJD4JG55flPR0UZhH4veW9Jtv0uVFLLevU0_-psMS-6fuh8ANTzwg-VyDJLNbkBrJIg0XOLJQMsYESwPaMggX5-MR8rfm8yNb1mBwIWszEnCeLqNtFBV4hj6CuWJv2AydDOLG31ZYeNdXyqKvylRNl_TxHKklIttOOVovDMPTDKuiGI19n42MCqFiDW7rgoXEsT69u4wToVQFVq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=I5ZKSbqXUFNen6iNXWmBA2NvmGZh-jBqrimdZ8aZYdNdwoe440KS8JQy2PcrNsZfiPigcAb9ee0eQJ6NZunzvF3B-tE7d_isnHT02jWaBqI14duodMN5DUtqeY5OIeA0OPOXnH4p1yqhMBB9vkn7b1mVxZRUS_VcfNXvy_vaRGRMjwJ2I8w1DMOS-3ENZm9JnB0N7ETFJaXy4e_K0E51D6j6auCNGAFzZBT0gvvxCtdO_Ww91kEXiayU32C3f85KgSwtofNt96Cdb9UCdKpMAuseWV6Wdjq2oukhp3twP9bgBWxARKjdjzEMPFyoYLVjNsLr6EUyFMXU8Iw3ukOFYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=I5ZKSbqXUFNen6iNXWmBA2NvmGZh-jBqrimdZ8aZYdNdwoe440KS8JQy2PcrNsZfiPigcAb9ee0eQJ6NZunzvF3B-tE7d_isnHT02jWaBqI14duodMN5DUtqeY5OIeA0OPOXnH4p1yqhMBB9vkn7b1mVxZRUS_VcfNXvy_vaRGRMjwJ2I8w1DMOS-3ENZm9JnB0N7ETFJaXy4e_K0E51D6j6auCNGAFzZBT0gvvxCtdO_Ww91kEXiayU32C3f85KgSwtofNt96Cdb9UCdKpMAuseWV6Wdjq2oukhp3twP9bgBWxARKjdjzEMPFyoYLVjNsLr6EUyFMXU8Iw3ukOFYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/no8VTWDP603bct3h-Zh6mndMEByrMa7XJDjW9nhfjnA5bgT62FB6JhQGIiKGVHN6AasqkhwFSn7KEG1FFvORB2EiH1iTlMHUps_K-8VKy8siOdEmXHpUlN50dVFEsgBTntd0n0oVemxyz_lgXJz29xaxl1k_glzErTQjTpPEqlIqJnNZANFEzT_WTzhJBkjmb80KT3DS0pKy3eBQ-PZ6X01cURJiHE1Hzre5Pe3i6Uvg3UXxqStqCdutE_AfKE-5TBdsg3lxXblR5OKUV3HaL3SbeSilFwuQ8S1KqLDejpHiX9bkERMK13RIdgJ611VjUGaQRo_hJt4f6xBtSRsOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=N-g2cDS4XYQuz6IJBNFq6gsd139QENlHtWqT8BFA3W0KtevE5-erw7PQeWeaVj1VLXcJjlh5MV-8HiYqKrzfc5RUTSmXf7qrHSOA1bLzMhyOv8TTIDFO9lQF50Qc8ijmiAwK8-0Om1Nc3XsGpFbrjSKSu35sKw1h43Gme_EJOKstTSoD7RBfj_Srn2WN3JhC7iH_iJtec9_9aB8o0k8lWlHBMAwycxOOUorJ5kQ65mck6XSFhKBahdkgO-7iyXunLxQPImO_SGnvAo30IvbpapmZJ-luLQut8JDdg0kTSy_2TOOd0Ir5vRyJYs1btOb-5d7dPkpyPKG1OVbkkbJwsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=N-g2cDS4XYQuz6IJBNFq6gsd139QENlHtWqT8BFA3W0KtevE5-erw7PQeWeaVj1VLXcJjlh5MV-8HiYqKrzfc5RUTSmXf7qrHSOA1bLzMhyOv8TTIDFO9lQF50Qc8ijmiAwK8-0Om1Nc3XsGpFbrjSKSu35sKw1h43Gme_EJOKstTSoD7RBfj_Srn2WN3JhC7iH_iJtec9_9aB8o0k8lWlHBMAwycxOOUorJ5kQ65mck6XSFhKBahdkgO-7iyXunLxQPImO_SGnvAo30IvbpapmZJ-luLQut8JDdg0kTSy_2TOOd0Ir5vRyJYs1btOb-5d7dPkpyPKG1OVbkkbJwsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
