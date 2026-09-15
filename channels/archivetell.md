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
<img src="https://cdn4.telesco.pe/file/oVg_f49cDyN2avvgpmRpN8NMLnUTEBWZ9tV8-54UYPWfVNyYlWGnUIZOUt_zWJg0o_GcU663QVzzpK12e9r4278yJQtOrbtE7PEpBzxCXNmfgsth_UI0ON9mB2b3jFgrIe3mktFZGZlNlas0nk5Ac6HELvsf874izhffBJCmpSRcfKulQ5iX9nTZitRpsyy1wAxm6M-d7IafJdeFMm6Txeqe_iwHr1o5VShRpMJEkl7qXpGNsJ59kLad3JxQcQaKJly-iQB2SWu7zNGiWj23-obPKn4LALklaufdQEiOwd2J9APUJsvi3WLM-TZoJ71s8JfIqwtuCvex9Gl7T2Zt1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 09:48:57</div>
<hr>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lVx-lPYiQtz7qpwR9KqCrMBn3DZN7XL4rFe17b1r_Q4c54J_VocDFNjAhr2ZOXd8EARj1IcRdG2ZTaAHQpgx4R8uWTOKP2iKAgz7AmcoY1tuMT6fJox0kHbmRqoOM3uIN01WUhexDWE7KZJ_UGWDpZSu7E2kbfVPV58bxROKdDVCmCaECHf2M0G_i9khJjN5nc_TCZUXc1C94OpG3I1kRHpkY0ige2F-uUzR3C2W-7edTj51BMmxoX2ysS7jPgltMo9LX0nwXjpVRJ4jcg7oc3Ylefe1KCKw3PTBxax52ksYwVaIpa5takVMlFeoscyJJMN6i6HyE9Phsal1mFwVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
از تاریخ ۱۴ تا ۱۶ سپتامبر، با ورود به
Z.ai
؛ ۶۰۰ میلیون توکن GLM-5.3 به شما تعلق می‌گیرد، بدون نیاز به اشتراک.
🔗
https://autoclaw.z.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cE6IP648CyiTUQSe4ZIIfXwybKcAg2keReEye2EqcI432iZo0pQX2vlmUhydoiRGa39sMN3iXdvbLbnGTzzkBEvcKilfJcnnkUX3d_b1LHEoWRunTPz5EFg5UrxjE7d5QeCA0UUEqAOlqijlMKK0_JeMQBycWhs5IllqlB5Jy0PY-yY0EeFvv52MNq_kAKl2P41wAdk1B9NcB2AcS8tsuPorG_aAEhbY2FQBlsf-t-1TjQVCh9HC7TrJttftNr707UqRu8WrtcL20696AYYN52DcLaDuJxJd2CERGVy7SzHMZU-CG5gZaEEDsMQ3BUdQVa9VEiiSU4pZVrolBhs_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
رفع فوری خطای ریجن و تحریم Antigravity
اگر موقع کار با هوش مصنوعی Antigravity گوگل با خطای تحریم ریجن یا گیر کردن روی Eligibility Check روبرو شدید، ابزار متن‌باز
Open AG Patcher
در چند ثانیه این مشکل رو حل می‌کنه:
▫️
رفع محدودیت ریجن:
بدون نیاز به دستکاری یا تغییر کشور اکانت گوگل
▫️
پشتیبانی کامل:
از Antigravity 2 و Antigravity IDE و ترمینال (CLI)
▫️
امن و خودکار:
اجرای پچ با یک کلیک + بکاپ خودکار برای بازگشت به حالت اول
💡
نحوه استفاده:
ابزار رو اجرا کنید و شماره نسخه مورد نظرتون رو بزنید تا پچ در چند ثانیه اعمال بشه (سازگار با ویندوز، مک و لینوکس).
🌐
دریافت ابزار از گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rk3VyAt_mlvh9RPn9h2c8Ajm2YkBXp-bFtV7U3OQj6Mpt74pXrhgvC25KRPITyuz2d53E05vH43bK5sy23HyIGo6iAjz2Oq2SxfUthqrNx3y8s4iNatXk16s0G1fRHoWrri4B1zlz-J04WO4MUmA6LRfkZARWtP0M7nmP3hD3M6c0mmOaFipDEzY0PNcwDyBlhAynUb1UgQKtZnM2vKu2wJYEpP-MAjqmfrEo0I2pnmug2A4XQRF7wmwEorWf-Gdh7e3Xy5t2HMndvPt_lifIFgWA8Yo61cRq9OiLRw5hCjwmuUoG-HU47ZIJq6855dJnkSCzTi-fpNP5J7XWeZ1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syw44rGBFlkwTkCdCwbTwBaRyahnT0UVAzWgVt8epZVKVR712R2W1mh64Oy4Bop-Syke5WzPcMNC5UL-8LRNWnLvvy6-FEgEpTxqnG5sLNIaceVlcd7CiB6FlAJMm5GwUU6bkdF1h02XNbj37Nkjx_lsmjjhr0v7Q7l4vjp2-TZzmcHU-OwEodPuYDXEyp_yRtBrbnoe7cqn8hqeMUcpiy4OG2tDejQAkcooKvkSUA1tBO9OdMvv6xteSKP8KYOAIKiNS_2YZwyMOpQX0qLzH_Ad9R6VUROJsfFPM5aPzRtcZJ_FjfhT53NVzcDeQO7mLR5E65fQMQ8PXuVDs5ZMQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=FQ2QNMV4Xf8dTpjPePBeBnqYaKwBArc1jmPMx1OyUV9GL6K7J8Ocbig0kS-xVcjVo-O7sXrrxb0HFjlwiU1lm63bsU_AK8GHEFhcAEhey5Qy_MQVaqHSAb1UzWu8C09-hAmtUoj9rn88MffTEqa4l1GJThkO__AsGhJlbcGyRiD_ozRTUkxgk0SjiPFsZq_m4QFS8Kz2wuWq98AxjSvuY3yKhPEz-Fdk3q5WNaEePW4OO-kAyl4Uk1k7qrvRLhrysTRw1gkkz-I8Ma0vI_gU_qcTdGWjMdpq1cV0tSUbU8O-xwNAQxKls5FJAZ9cLSyavqdvfAURm9VyzuPmE6CXZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=FQ2QNMV4Xf8dTpjPePBeBnqYaKwBArc1jmPMx1OyUV9GL6K7J8Ocbig0kS-xVcjVo-O7sXrrxb0HFjlwiU1lm63bsU_AK8GHEFhcAEhey5Qy_MQVaqHSAb1UzWu8C09-hAmtUoj9rn88MffTEqa4l1GJThkO__AsGhJlbcGyRiD_ozRTUkxgk0SjiPFsZq_m4QFS8Kz2wuWq98AxjSvuY3yKhPEz-Fdk3q5WNaEePW4OO-kAyl4Uk1k7qrvRLhrysTRw1gkkz-I8Ma0vI_gU_qcTdGWjMdpq1cV0tSUbU8O-xwNAQxKls5FJAZ9cLSyavqdvfAURm9VyzuPmE6CXZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlVHmX-RxhCEHZBIf3HSdHi-4ooKZhDEH-KRgHjCzZoETJy1pKh_9HXDyUShwUQOuhSTRA5AA-zvdTue4TU7itqDNPEdNfiLJN2PADzgcw9D4Kh6Lz57eiG88_Y9ETtkTGZjv-vLzzXpV-rmXQvWh3KrEaEyxoTPH-qseyPKBep6-LNu15MUwQiebA-ulhq9fvkYObjxRZtK7VeSk83_38i7tIEo_VUD5vt9zzgB3dQ-pnagi93YhChlQwP7guuJb4dBA5VzHNxDqjaNXIQz88zfBEqfEJkeNhT5fYYf9W4A6MNi4oLEW9wpG4eGImpWP5eBYs-7etqO1AWnIil_9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWoWBgqSF0OB8nh8giTq-gzj_R4EMaY7FPeJ7jwe3O7HPvMH6s2SVA3KuSKRbR7yYwEDLamdE2xFySfbwNkAuKo6_saxPlA6iRSL58xIvlV2lM3GeeRev3Ntl-ZQSYr4jWQzxp5y7HEveW4H6Ik_PEmlIbjUyCTXwkbTHOv0rUCOiQl6QICazHllz-TucLLFELbSNCF5AaU0WYxJAH7qpgdCA6_MrXSa1nbW3AFrpIg8Xte6TVTnjWyccbAUyyCsgY68UrgqPgbFHcYX7_KAgjSxdZ4oRzpMOBalO87RaCkrugVUgVEy6NOo7UFRRvNA9_bd6PRb-h0tCUUTr0UPUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0_o8ImP2b_E-QjaUid1oAgsNU_ekbuPqqhXD5sBQ9_UR3fJ7RkQIJtPv5UNaWCW6cdU08h8eWQ5maY6_QbsGUan0hJy3fCg0d8Jht0jz463dF7yMJoPS-E5UccMhRZ7QpnkLxc6LHFtjwznn7xnRO2egDy0cpu921vMKSGlA7Gxx24qr3oWxq9SULqgvvKdPec0CACAkRFN84gyh0373fRVUQFc0kx9eEBfEn0ISWOPBTpRxCvqTcDPwZAOBnKJsYQW_R8R2f_hn5TWUcZ_r1w6oEObwmLWnU9f9kbc1WrBFzvto2XfLEXxcWMl2LPjIynd8OA1PDGw2TR6BiQIAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WooyhMVaBFbntO6QZaogpdniArwgG6MAv_w6wtpjs3f7G9ltuJJzZ1H6SqKIN8ChcmD3sdG0lyNjXopNO6SkmEnPaY9tFAzD040l7r1HaMt2wiW5GedDegD0skdyDwR6mrambXSLGGVNILIgJKevFPilHyfT87536VFWVNtpFLBpfDzYX5in_wfFMsl9HMGZPFrJWCp5fU7sBT0q4ZnAF-vLE4Yvl5Rn42lohMYN-9TYGKEThSPfRvsgF5vlcDuA_BDk6s46gEQxSi_PpRTkJ4kIYnZCWKeIo9xohdzGMrOmsMvEb2P8QFEfHnC8wzHm2fFpRSJT_2-AphmAR_E0oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ktj4U5xBaJ8TTtA3FJvh_xbIFv3HPRA065m797QvByv_hUgItW_lBSmTa8RYBkb7WY1qmHysCIfHFVb8i-LxjbBy1x10tiBMfG9iWkR_Wt9gL_toNK-07tbuHeXXqP-6Ll55EF4-Jozpir9u7msPrx3umeFeqL_WYrz5F9SIhpxnhj9Xl-bfNTNNL2aroS_2osEYFGjUctOJ5r7fSvgaNRU9Ro4VUl2Su5BXQBCiVBWRktihCsjkt0k9TCGzbRwNw8uho6ECkQWmc_t-O2hC0y36Jf8-bS8TOGA43KZwA0AwKo7otFcTsJZ_TjUkV-xvJRT5o4ka5EqYS06uUlNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nEGgnIWZbwerC-Fy0RbIqhcwMQzV0CDuKBGV9aaaSQWO5zEwV2NFwYc9LRhWdgLt7VXyXw3nYwDYedxWhcExVq2us_nhsSLcCztcl4rGH2Sxz1WOCRg5H6wTS66x9v7tq6DSwM1PD2GfevZ6c4DvZnJESvNJ9zso44F050pCmWCmgFk8YNSw-YiHEW0NW2VsIFfbXVnXtWmfbiHVVFwY3_Rxtc7N2VrQhQlq5lLVY8_QAxnv_YhPhtasrQeA41L9ymtzX7eUMFBD6U9hqWJWqK4oJUvwpiuXY7uAKxvm3s5_hItS15QitnX2lMtlpn1m_FUkMZwtqNTXx41zYAlAzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2_1nGuEVDlj7EPbQuPRuf-Mofk79omWn2jZCdZ6zJa6QcZkhvfXBbwLjr4-2OLCMKwna_1RXj9DaCpID53CwG4N5b2kamFMvt_Xiu2piMzhm_2JY_g1rLefC54XTdPUdme1xDLssqde_gDnuorI9gC2CmlsrcQBJJAxXqm9Ho04sAiIb7mcyDzKEHiytutVVijUyOQ5stkycjHrI6uzYW9eQcg9yC6HHzDnhX5PDidKkmf4Vj2KK0PJ488HrYwyG1azFm74dfKFuGjZutu1MCT3MwSZkrb5lYWbabaASse6K3K8q0yT36OAQ8yT4jLNtDTZ8Tx3Y3hgYiDJ2EivxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxjmFHXUb3ss5NZneDi8GzvAdty_Y5D-q_XvpQrj46Qa8_ZZb7SjvsHTU64GzSMYhQsHVDW1UiLERQfmt_Fj87SJ6ZduKCI193ACthi-1L-xLhqXdlVWvPagThPJR2QKElhHzqK-hGalJAZujr9sjdORvuxUvUHfL2_VQpW_1NCwkD4EJ37sxBFDHfU2IA9cGIrC52CEtNXWxS5dYK65aklLk8jGdjrmSh36HQ_X26cp70MKc5twkk_0op6eZGauPAdA2nnGVY1r5Y1Hzu2rLzdge2zxFUmFTv7mTu-_BTI4fnXG12ZR9ZlVlZynCjfHZarYtSNQOnE9r7x4LqgTVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLmbT64ZbAwecJ-QdXZrISpGmCc2iS5O7R8SUUKLwnlLbkwbnRlufGnWEQDvEbDiqd6MPS8tojVkBY69gGF2o9pDCg-oOKP-yntvBaWRRHjTaFNZufQ02JG6dBJLKiZDHjc0kKDRBNKdA-IBQkbBroiZBkuY0x6YP6v6Jh-L2IKHI9zkfPAQvkzKkd3lZNwA3oYJJamyuEzoALVhm3csazBj2hacN6iOHvl1yIF7g1HoPTdXJTxMGrDzAaicOSBcyNZ8DqSAC9JbWeSj2_hz68wsJpVAjQ47ea0RHuA1ft-1s53L-gkaunkdocMmI-sgtKyaE4vB6uqxRw39b07Mhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAc2h4WDYflZxwJedgb1cfbl9Y74AVLsazicV9uq7WoUFt08Vep_fVLVvrFIah4Z1uG-l_0KA4HODWnZjw-CIaTqc2C1a-ijUFM0kq3iB3ed-Dl86jk2e_czgHBZt_y9-WAmVqbwBDNWHmHfPzWTSxHaz5eVKTW2xtYA1zloNjibMakjIkpegabL3sI769g5GmKRyMcwYv2SEFylyzcEfSInkYmRlfO6jug4K3I8KJO8YXc3bkgW3PMmNclb17ZedPDGye9RnPQ59xe3-YxMhJpyJlxj57BSk5Fkf3um_xy4KQROEKbv27mnAA4xdr0kWrSxAGa3imy-3HRDxaSavg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6YAxdmWss0ASWiO2RAhoZedNvXRdxOQ2KDTV5unLy7Z6xTa0g7_vjbMYC0M_f1tr3aHlHwFAXv8a3hFFrrt3g37ZFyB7ktCGXKRdELtc2Wnkn5WsbypHoHOzt1dxQ6Tzh5OvFkq9fXGiELKHZT0Hnroh3F_R-rnLdeFT5C7PSdnsU4I6JW-MofDp5iKX3l5_N4L51MIokGCvmOOofKLgNnikbX4jvyUOR368W4kKnkOz6UvNw1CDYT3soSxR_RvarDaGBqsIfYB_YvCGjRfRvIS7EcHBGwptQdyn9U7LdxyYj2wAC2B3QJ_iwT_VAygsHJOrmyir43JW3LZPOjvYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irH1mU55OB7iWFaLNQ7xpbGVZot-8m4_eQFySBhi14OoXjw9p0ucYpguCRMQjzcVQQCtnPS7C4YBnJd-6RX8MOlfEihbtq7Dw7fQzPp4NWvSMhdQDP8XCNw7I1vu7rzxUfp8E4sv0aQzQJH63xzZHO9yxVhw-fG-oTIQujw74z0aV03DCT3FS5BDr30wgMZKZjhMH7FJbPGPRIkKilg5R0DZlCktNEOwPNqUgbZejCFvRMESyhBXTvgX-sSUoIBSDg1AwwT7PFelSGtC0QA2hK3-HsSA9nMypSVikJSKZ3h_8yOqvt0ug92-xFnNEVzmBfwdBh-aFMsXsnFzupQuNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBrYDiCJy58zmfRAnSYeKiCOa2208YicajbL6oT5pWYrfxgGM5WiisvmQOxe7v1PeWf0_vQDjBW6I5-cDal0p_aiUo1oOpXdWreghoUollw9DBpPbxucA_3_BKr-E7JUMeh0AKTTK8noOfZ5makw_F06lwy6aaxB4C2Yw9p9YwPo4jW-d56QJd6mubX71e5upb0XmQyKD2Hy2UCeBSwsYGn1hyecNvRuzogoe6OMBp-66E9WTrbhhylGWKKbzrAK6QV97rmW9dNegxune1uz5Q1e1yXu2R6cQmw-6mqtOPveBi_GLRybAuR_1Z9a9X4W4FhKthyZr_yGPEXwwRTsEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riNfHNnY0a9W_egOHRoHSAZQAJNZm8d1YLN-tbK54htbHilMVziTtLEtbENv7xFgxNWspMX9ORVSajJHlu9AaAOJqpyQERk0XTinmQUN5U5z4NC0tatLeoWCiIURBpNRRpGm5SQq_LRWtiYaMprHFSCP_lu7F_56_rf1HuvtS2yv3GCPQmXsUZvF3F87MQlQXg8Glu-qo56h48XDI3Tng4t4toCKxmd30DZAimc3bM8bLFNI3lqNNJtzvA1gMO-zFsLszZ_efK05IEaAvmOPL6uQGetZYdbO16KrBKufBUXxYSnW0_smEO4IIS9NwVJdtdHSwxdaQEZPHeIDv-a1RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCGhADVzd1zR71iwPa6D3xwj1yIrcCiO3rKFciy7eTqBwz6cFQ1tDji9EzyVacnzepI8mU9vWjcc44zJ6goP3L7BNNF6RiLs8Kq66pR7BAbFhEXS9_IaY6fr8fI-P5VgZquoPC-4bH_W-d4tfqqfiXEb8Iy0R_jfikeMiWrq5iUtiG8UqTnx9Q17vT2SqOndtvDbY36FoQi6-NTPaNUZS4RfkfrKe1nYl7tXIGgo3JWr73AurWEBKAU63rygPbagTawOfCnf1znLiMKR94fAiyb4ZuXiBF1WpnfswSagYRMgYFPJOmlegO3R-GWN2FgiAWQOhq3Wj_izmyY_Y97yZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFUM6vfOJqlgP8-3DB9IQSspF6Q-glSXR0ioI78vnOdg2jWdrwQ_27jvj9VBhQyE7_q-Xipbt6n6pfTwV1eEhNCwqeTzg8KxkrWq6-8QHIwAgeeQQ7suU08n0cNUHV139uJcoTVYqo0hvCimmZc3Piqlrxs3e-WMxPCNY0cf_7Qax-O0YsqQdZxPG_1hSvdgRrMk6f9EOOJ3mWzErsDhv6RwflJb6GWdl0OYTt9upF4NyCGsfH3fp8PH4V7lWfLMba-LOVgRRQznqPqeFNt67N_kbDYrORsAQYwPeI-3sh-ORGLQQhE58ef_kpTm7PN8s8sAN-dUAhH8_MZ4GTZxew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFPuoaAT_vOWpuiq7Slxx5Xo1hMLu8Fa4FvHRN3_oaoO2NUyd-43EqODxm7qNiLtgCMLhm9nhMAjouKjCJZGNWTwUTf8gU1a6XLbqW2f1IyiqgP_HVVQhZcYWjseYPo1p90ifviU6mF4KtfcKg657epvj5A0Kf6zwvIYIsknIjp_7DFH_ZpbutXhFxw-vvqwXQiwY0bVq5lmi8r573o8OEF0UVmpQ_zwsxpr-bzIv7zsP7ufQYEexXvB-_D3Xm5nW9t3RZr9NWubWSjrFULb4JlYscRqQ7mPDbrWlvC89xsloAHk9LrRz4I5ah4-zgzH34YZ05yvO21WhwLl9WtG5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn7N-J-8Ee2cbU4fyqlBj5eH3UwUst_RfoJaNR4YlWs9kXUvnc8rRTASglp50gsm5buqUQOTicS8jCN-no2P3D6oB2IKtfobdeL7fvjYLHj7bjOTPnPqiGX3gsIbrrQfsMxWzAZgs407QXDVf4Fxw31tCblAVa95UWihWsRVLA_3Rg--uDl5OQxmxv6PwqWkatoWJjHro2hJZ_1YArIgo5KRubvZVaDmdX_eEF2zYCeHCEjc-7-A2XqB_-cAkgTCeIRA2LMoQbuALp5Br4L9hKr6QRyvGUQDDrEpXvksOeZWhlnOK-KvlZ18kFdec8DBdrfPMys7obmhf7hN5Xyexw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyvB9AZV-EjS3fMEq6ZQVvIw6GHpDGYmNwccNdPJl8Qzb43aPm-xbzc5mV57wYaexIjQFKaXeZPy39662txFYkxkB3LoYmGUdjMTxfN1Txr9V7txsWeylqokMORSLxLdopsQN4VsuT_Ggt4JwCqqWMlk_Hp8EjMdPMuWJlHxT-0t2IuKxEJjFbutOSOmc_h03vF5P8-pd9ZoF4vU_x7mIxbSciJ9mhk6uUA0O3di73hfb_cJCv-P5kQsT5C0LC5Sk6JJOvDT8zpGD15Dpgk10286-RR6mnJ9MXpatbrp42oWipCU9AmSD5sW_fHy7i11ALwwNoXVENzQP4WUVoEvtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZKX9zt0MxJmOb_Xy-CTuJh6etw0h8mDpGnckL4K0NVGDvJdFtqISdQZ9gqtDX6XvpJmW40oPAefoR978JiGeAvLfpw90Wi6-CBDXGCE3NLHrZn8vmBpO4qXXezwZV_tf7ODYVD6vgtrrtiYoO2OH1U7gerf5Wmms5r0prwXn7DkIy89nyK2Ge1edNMOfAtWHAvbGgomkA3s0fpMo5exrF_YxvDXrt4HhhRm_sncbEmVJqJNN9Tl-WaFi24UrNQh20MmiPfsUahyM3jIqh17QdN-N9mALX5NAd9CkVFZ8nXtZeMTTDgEioEGO7LIORuI16GxzeJ6mApDeWWcZaWicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=btufbAIthEZXIbSZudttNCC1ri0fE9irwC0gXwpKgwbOu3lpBuLsr0rKL1lZbHvKvOQKnURYxUuiE-UQw4R9lsae4u4R234MAZ79bnY7zjmBTcVlhvzYSXWKd_icm3gUglo0PqX82zp-rn8VFwoucaIto4VMbay6YvbkOS5lYDkwwMdX7iJZnvmQrdfHvhu0InBpt8CDkApFRnBRB2S03zb9NwWT_4bNwsdLsuQkUiedT2g49qRzVyWEIf1NMrJtmYHPwNFJoCrf291i4rYIVVuAcbEkMVLMPrDS39HweqLOhQiALHOApwJRT9DrS-kfeTN-4FLq--LGaHAo9LbApo_8OZKspyaXxpkFhj56SDS3LFIJFNzUQ3TuiIxSOflsFn6VZxmsBNVbM9iwuAchCPSQpmk6i8kXFiRzvLIdBrmmftTKKQS1SAmzTY5LPKBfbhrijGhvRz7USaD5H-D4vNQGJSBDxfbWot-YkgUqFsr-rLk4geP5ahBQcBMKRi8nfCFoFRfOZOo4LJqB_Va6S6JHWm-lqXqzzTKc2oc3h8YxMz_bYk4I89jMTB4xuSQ7BZ3sCOYIPOXOpZHgwu2hR6hZhHi-_pg4BN_nP1zrCIw4NuFq1cCofpi8CFuPgABLZcpxRC_fFmREhhQBkL3xCIafqQUi7bwWOYAHZSfMNyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=btufbAIthEZXIbSZudttNCC1ri0fE9irwC0gXwpKgwbOu3lpBuLsr0rKL1lZbHvKvOQKnURYxUuiE-UQw4R9lsae4u4R234MAZ79bnY7zjmBTcVlhvzYSXWKd_icm3gUglo0PqX82zp-rn8VFwoucaIto4VMbay6YvbkOS5lYDkwwMdX7iJZnvmQrdfHvhu0InBpt8CDkApFRnBRB2S03zb9NwWT_4bNwsdLsuQkUiedT2g49qRzVyWEIf1NMrJtmYHPwNFJoCrf291i4rYIVVuAcbEkMVLMPrDS39HweqLOhQiALHOApwJRT9DrS-kfeTN-4FLq--LGaHAo9LbApo_8OZKspyaXxpkFhj56SDS3LFIJFNzUQ3TuiIxSOflsFn6VZxmsBNVbM9iwuAchCPSQpmk6i8kXFiRzvLIdBrmmftTKKQS1SAmzTY5LPKBfbhrijGhvRz7USaD5H-D4vNQGJSBDxfbWot-YkgUqFsr-rLk4geP5ahBQcBMKRi8nfCFoFRfOZOo4LJqB_Va6S6JHWm-lqXqzzTKc2oc3h8YxMz_bYk4I89jMTB4xuSQ7BZ3sCOYIPOXOpZHgwu2hR6hZhHi-_pg4BN_nP1zrCIw4NuFq1cCofpi8CFuPgABLZcpxRC_fFmREhhQBkL3xCIafqQUi7bwWOYAHZSfMNyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=JJVqHs3mEQVxmp36sxy3ZuDB-j3Ib4njUt_W1YZZlFWoH579Y4fDLMxI696BX55diLchVlzRxnfutmYLefD_e8eTFRcz94890xTU6mhx1YbjsAAKs9yXBOFkSPVs3FQRqiiv5w9e1_vZZoWWBsRGb-V5BUPI_y_4tzFs2qagxdv8YaEDPxMSvhBEZZFX6PdfnEvKxBlK2dfXXURM-GMZ9Zq-nE_6edzC5oHu_ppGRAMKZwbC3XGs-JOo_Lqi21Wggwo9fhdrlAgTtHRuWpKs3PHsBXs4jqawnEmftPrXJWxB6LEd_JopAeBArnM8b6u5sCEqu4-YsABg_YK0LpfYqjCAfI0Hgvt_-ubWHpYtkqP2ub-0-uxttzQq0HCKcWo8jfv-h07lg85HESPLlfbeZoNz6Gsb4wN9zvJ1vY7zyFCm0eX20NgHK3bTC3kLP1qI7ouoTFXvMToOF96S4NJFqwYrUuDNAK0A2XTOTGUilkdrtlWk6wLq15lpe8g62APN-AqoyezLj01H8nQw6nasUpWs7j2E1KILSrOV6l0YYSMM60sx-9NlEYd2hy6_4kxqYJMl8i_0JdKg9SSIYU8KBJgKlgvHKwFb4Z-BHYej5eDS8m0G7u6hYq8hs16libEU7mQkOLhAqH1jvr5_k5clPBjq_eQkMMpJawYbU4lxUs4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=JJVqHs3mEQVxmp36sxy3ZuDB-j3Ib4njUt_W1YZZlFWoH579Y4fDLMxI696BX55diLchVlzRxnfutmYLefD_e8eTFRcz94890xTU6mhx1YbjsAAKs9yXBOFkSPVs3FQRqiiv5w9e1_vZZoWWBsRGb-V5BUPI_y_4tzFs2qagxdv8YaEDPxMSvhBEZZFX6PdfnEvKxBlK2dfXXURM-GMZ9Zq-nE_6edzC5oHu_ppGRAMKZwbC3XGs-JOo_Lqi21Wggwo9fhdrlAgTtHRuWpKs3PHsBXs4jqawnEmftPrXJWxB6LEd_JopAeBArnM8b6u5sCEqu4-YsABg_YK0LpfYqjCAfI0Hgvt_-ubWHpYtkqP2ub-0-uxttzQq0HCKcWo8jfv-h07lg85HESPLlfbeZoNz6Gsb4wN9zvJ1vY7zyFCm0eX20NgHK3bTC3kLP1qI7ouoTFXvMToOF96S4NJFqwYrUuDNAK0A2XTOTGUilkdrtlWk6wLq15lpe8g62APN-AqoyezLj01H8nQw6nasUpWs7j2E1KILSrOV6l0YYSMM60sx-9NlEYd2hy6_4kxqYJMl8i_0JdKg9SSIYU8KBJgKlgvHKwFb4Z-BHYej5eDS8m0G7u6hYq8hs16libEU7mQkOLhAqH1jvr5_k5clPBjq_eQkMMpJawYbU4lxUs4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7dG63JmznjeD6MpsveQh_N_yTRtdBoANWlE7agxMW0cvQvx6rLGIn63aXfuo_AnceIFdclg5UbtU8hhtP6dL281Tc0euLeT1B-7LtXUNsI6xOteqcAKTtT5ZNM4-RrCSdGE30FNYACu5CcjJ90tfqRG3jmfVlj2mf0rVm2FnQBN3V-4przr2i32XqWHBYRNfocqLCRsXQjQIkGv9_v8anetVhOHhMdD19HQyVhgqrX1urc4PV8X7E0by8jtZLvfEj2QbPAoiBIfhK04ukf3LwcYb7ue9v-uZVn3Cn0LAiDjK24x7FwlNA9FgCg2oO0_ijr7rIT-olQxpldWWECocw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=J1ZILFciOLh2W25VizgneIhRBYd67v7j1ebhuNpCmSMJFtdiQNwlnqghmatbqRaGBZxqOpnzF51i73aTj4_C7QSpTTHOilX4ITcqR-x7tlFl9zsv3wtoY9TlEjX_22H16tr4DKvJ8HmUL2t3NWnwsOaEvmNevUPZ2-WLwL3-IKmWuTBjbqFEYiyS06wsp372UrBTjLjSBvUJi9fDeye_1GDPb1lCyNNMgHLk7ikdAvo3UXvvyt9T13AXqNJrTE_77kIf2-XZ3NLwZw-lYBejx3qsn5pioyFTPhXq_KRnOQMxSwrbpeGsQI0DY5Yb4psO-knsV1IYZNIUBMeVC9naeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=J1ZILFciOLh2W25VizgneIhRBYd67v7j1ebhuNpCmSMJFtdiQNwlnqghmatbqRaGBZxqOpnzF51i73aTj4_C7QSpTTHOilX4ITcqR-x7tlFl9zsv3wtoY9TlEjX_22H16tr4DKvJ8HmUL2t3NWnwsOaEvmNevUPZ2-WLwL3-IKmWuTBjbqFEYiyS06wsp372UrBTjLjSBvUJi9fDeye_1GDPb1lCyNNMgHLk7ikdAvo3UXvvyt9T13AXqNJrTE_77kIf2-XZ3NLwZw-lYBejx3qsn5pioyFTPhXq_KRnOQMxSwrbpeGsQI0DY5Yb4psO-knsV1IYZNIUBMeVC9naeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXXLoHHbhnZqIETvSZ6vR5b0PsFMntvd6C3hPMdMUui6JLaR7EnPB4rcCgN6bxzJVX4hOk6UNBpvtfboBtQ7K8WC8ZKVJmucH-2E9tqix5Xurv0xIDcT0XP_5xekGI-7SKZe8CRe_uPXxrtvQVMN6FsJZ4BZ33k9Czi8Qjx4OvM2VxKyOd96eafVuWRuJgiqQWo2eASGbube5O_siv7adRrpIRlLJ76Yzp6YhkUo1eefG5zQRKXLYLDB1BJhPuGEL24TgKhBSmr7Y5SEVac5y_AJJUNVMvclf7nyivgMNMDNG10PlCv0ZJR7jTLycjxsm27jDNh3VkEcI2NvveePyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=pVueToqvX57tAswB75Y_FGi5oqSfFK_R_et94A3MnNwnLtWffZAF9ehv8EWbJK-Iw6k5TSboWUEQUYeyK5p8W8HEfYNPhhyZsz0yZueLgYR6VjRVbdBNTZzTvqKArLOh5zVvUaC5VVlaIDgIwO7AwCoZRcgR0_K9x79fmkMVfn-8bRMsKfk40lPofio7zqkIJqoMEw2eGVqG2J92L7hAM_DoAggCBAcxgr8KjhLl0fvvNDq2M0hODFuzHb7qtv5Qk4QYcE0ekuCLuoWVbpJGosiME14oniMUpkOFNjnqneesXS2tt70ZP_v_nCw8akQiy7jUs4mI0JMYnyYnUr-84A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=pVueToqvX57tAswB75Y_FGi5oqSfFK_R_et94A3MnNwnLtWffZAF9ehv8EWbJK-Iw6k5TSboWUEQUYeyK5p8W8HEfYNPhhyZsz0yZueLgYR6VjRVbdBNTZzTvqKArLOh5zVvUaC5VVlaIDgIwO7AwCoZRcgR0_K9x79fmkMVfn-8bRMsKfk40lPofio7zqkIJqoMEw2eGVqG2J92L7hAM_DoAggCBAcxgr8KjhLl0fvvNDq2M0hODFuzHb7qtv5Qk4QYcE0ekuCLuoWVbpJGosiME14oniMUpkOFNjnqneesXS2tt70ZP_v_nCw8akQiy7jUs4mI0JMYnyYnUr-84A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmQR_d27TN6R6_mE-Ari6R-hLTDS-iZ0mIPvgvUp96QOBJf7nqOpZxCXUGddE1Y2ZS-8wgF0NFtvvGyY5fOVJg4iRzgQgeIKtNxvn_eTJwK1SWCJ8y-k08lF79YjEoxdWa3tDCvvdxsQ1fA2HtaSHibi0v6cDTUCBzLtB6x-DJKuFe6tURBcqJtAHyabRBk2z6jitg7RuDU9lRg_EP7MvUeYQmRIQ8LN59mBqjgWI0p7REC4ne6ALb6MD5GoDtWl6oyKfFCX2bab0KAmUNo0k09ltOJ1mjuuazL2YDF9AE_DIA46Rcn1fdKINndLjpqQLxb-N0o7EKrNoUhBQl1F8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urFXzJk4Eb0BxMynS4HgFq77NUNTDERpW4iq9kiQ7pHcCjKd1soQiUl2RYg7PncjZ6XmW8ECTCXhq2hOQFquvge2f8DU3KmPJ0N4cksKIhb46A963cEgu9j1At0sEAU5Z_xdurmEk8L8Wi2XCPWASe_v8zLHXHrTo67pYU7gZ4lZ4WeNIA_57tM1v64QId1E4Tmhq_-Avy25Xizxah2QOm_-HXguxlfW8dzxvrXYUUEw1Vo4jmUYxbUVaPx5kT0baH8eB-53JmwL_-DNLmQWTenRkKMl8I5f6mp0njp_yBaRCLHOpzwZNKA9TeOx6oWrhXlvkIb6RBFbZHI1QoXehg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuZ8bQCGMI-bFy-2gBWbXva8UPr21nSrPZ4wJC0p5GrJMUApaYSaQjIAFy9VEfQpBaXUDN-zf05HSTX6tuSiQmSQGCyVevPgKE5hnUMS5Fx0JDJcPlTkWYFv4_Jh9_9Lk66yPYC8n2avMtFxWc5hScM2evkkOAXQYwbYfIQTC6uyp0KiLb3dv9_mFEvQ_rs_QYJI8FZ3hxWT0YIp_YmBxzILsjexZ03JbgZLGm0Fvt-5EStEhg_XoAHO4KNC4vSgasUVc1ZN6DEoESdg3Z2F2PFjAxuYWN51v18PpUMgZzjhsUvk0V2OGV1JaiCv7wHWer2KWLO4SdTol0tXCM2pUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOQfXkauPBWip8-tKJ1letchQprFWQgVmYcP63kdIlsG4R1s6TwZW9vjFT8oiLBYSdOZCMmZV_YtTASvOQ3xemTRhHJ2Y1mRO7xMSbY8mqf4jJn4SNQ_t0mu2SQsLdMZR6aNgV3Z7KKAAbaMkOEUmmIsKYzMgLR3I5m_pCBF_YXyVBTa086WKgnpr1ZxXmWvq1yrp62RoGUxvzl2U9Y4oy0WgeEhDaDTq_2Cu_CNFBzjYvzDH7LQihosJwq4DwKXD6P-d3Es8X7yVX6XpgLEcZJlwwMBGjJjZn9cYgQXA0FDjDNBo48oFjjsyNxeFkSh-Sg9ZM_jxp8Ouj70Aglzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_GMlDLyD4-lWP92Mg_ellG_VvMIHqKhmPwv7V_oVM8brbKy-F-wfV4SfUQ4EaPL-QDgpsf_JUp4VtZfR-y5nZSo0dwge3d8l5KrGG7_jb-6mZb1CSwSYAYwc52NYT4MZE1UifbDCXEbxiu4nN_NanCUjByKWdMkWMomGs9IMEBm4Ep8tqyLsC3zzs2O2xx1fGOSwrzeVuxp7yQUGNLdo3cRz9cQ6_Q_sdMTOqDg2wmazW4XQoaJgpjPadkPOeuedfhdpv9OvhPJxepNQZv8vrep0mnsZvZxYk2ANi0LRZ3w-W37xx_Tt96Il_xuViM6V3BX1--Ue3SGR-5k1MUQQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmGodeZ1OXRR40NOrmvQoidq5Cs2xyJDUEXwPTZ76dPKA620rPEtKSWOXfJ8b2bH-keExk-MzulGPCMMjNzRe97JIW0mIYD7wHbVV9wk9CkEwboEA-QyMfQcG_tQBE8NaTIH8yyZkLBwe-6wx6Q4l78wTlm3XdyHrWduVMTgXDYDVnjkjcA8K-UMSa2l6cOmqS_OWMVE_N3wFPBcEqNrC1RiGJ-LmnnDiwSPOjLTxvhSi-akyyZBsUuYhKu8-IP1B97AErp-g2Ab9ak86TBgXE9NhRXToWPE-HMpr_nguuOixRFmsbfyGj66wmaVfrP0n_F2Wk4VtxspUFD0z8_ekQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=NYJCW_xMW0oZahqu574vzSPRBOmZO5RaVXSDQFXhdq1nkL2Ln74uRUiVbGUtJvxiPCZ5a4Mf0taXuBa4NsnCfsjRE6p--PUK5dVYhjqkRzpZiAnVdjDIiJf0A-sjOHJuhW6g7MlFXVuIQUEQPzUMAUJ82IrDcAefEH3uk4AfqtPZjyj0RHIXsbvDOSdvsKgSB8kvIFZqWpSFHd_vlYD8ClRJjV-LBxoBP6duWWJXsLk9avTmHHRv1PR5SNsEJ8R1OHOUXV60rWulcIghOeXtklbs8XgTc2XA51rFDY80BVx9BuGmVq3IxlucdRSSDctr-jG9lOOIZeIe-S1WdDXjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=NYJCW_xMW0oZahqu574vzSPRBOmZO5RaVXSDQFXhdq1nkL2Ln74uRUiVbGUtJvxiPCZ5a4Mf0taXuBa4NsnCfsjRE6p--PUK5dVYhjqkRzpZiAnVdjDIiJf0A-sjOHJuhW6g7MlFXVuIQUEQPzUMAUJ82IrDcAefEH3uk4AfqtPZjyj0RHIXsbvDOSdvsKgSB8kvIFZqWpSFHd_vlYD8ClRJjV-LBxoBP6duWWJXsLk9avTmHHRv1PR5SNsEJ8R1OHOUXV60rWulcIghOeXtklbs8XgTc2XA51rFDY80BVx9BuGmVq3IxlucdRSSDctr-jG9lOOIZeIe-S1WdDXjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdN7Fdq-SXaLHx6cqcwWn2SnNZAMzbvo2lbr6F4iynBRQqJylL2qYmeSxHa5ddidJWoOF7VI0mrN45pqGrTMp1IQT2nSNixUC-cjznaBHhlXS4AonX_rd7BeNHp8k6ynSy8HEseEzMRvy5yzTuDx08h-sNdiuYmfi4nrL0_EJdt6MHV59b5pAIwLNPHX-9RGXOJyXcOIlurPCE1e19D82j0p6jLYlD1HCJcvKWZkPIucdvz6MAbSFVV1Kzr1a-zohuP9E3tJj6oR3fok0MhUrFiqCaXvhLE3ppy6Lp7_apZ5msVw9RDTViE0ytl3ODoh0VyG-FgliWejGidss-iVfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDWV72rMPnyp5oH8VRWOnTU91aMTLTDPvQGR_PU4ZmHxcNh_6lLyJr4KJ1XCMWzyyuFR0TyKxfFx3eDG1hz1KY52mGXsucZKDW54N-wPpM9BfdXBh-Snt1VBmmTVkwg6083NjhTyz1IrSomZj41Wi7SVi-vBRttQeD_2vMbi1DGhBebpLlnxOtLm-qeyQJnXwlRz41w3OGE3xLosg_ErWZzvVhZOwsIyXaWb7aqc2kroGkqzSALL8X3HNgoGDc-rKBh-s3gkshinsTN7k6nZE8Qe6bc-ZmlmxkLJkk2VoYtaMQ0dXu2WBikIlZmfQw2j2_mUohdpyv-GizMMM5un2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2HXoXUYBUh8RefM89Coa4z3zkKBiOjq-PmKajglkgHuaKxP5n5_N43tsNXYrs1lYdLCLIpEqeUiGTNPdv3X7tgjeAcQCHcfOvlyOVl2JnnVejgsByZ1ucMDF0A7DdcksKVTMYK_PdraxDnhpSGqveTipXAivDiOSvZub_l98GCi9GaYjVjlpvGoDiqWZhimXO_2HUY5SiB5peQT1PjF6-p14eGjBnSp6g5K0GE_AsA8lSmD9_-NtIF5lbrDIIdPS9980jVskpjqsw0qiwNKW-sPrihSI4dTQ6LX3A7CttlQMY8F-fv3Jhgg-DnvQxpaeYZDMeytonWBJ1-_wmg2mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAl-6aKUH2uFkxtUN5UO0jn5ImpG2v3QAABt4EZDQtFzC1WnJnDaijIKRfadCXNgbyh9XRBJdD9e4AYfO6_VDJrgWp8xITMPcLDR6oBPl6AFu5x2cOFWkH2ARljBPyq8WL6DjTFiFYw_O4qM80xJDkLdG5Jr5SAofk76JQ7FG9o1wCb5NzQDo48ReJKtzSuVBhiEi3j6Fibu0mopZ1W2dJ1_uR4NyLDT1e_eZ56snste8KkdqZJqhd5j_zJPW0uBWcyDGBTvHhUdCAz4MwCZEBzbh94lhobch5KWgDSVrIm2x-vmUJjUIaCs_xztiuiLELMfk56xNJGRYuS3XOSMtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJPpkczPpdSHIAF2-OF8K3EzeKUpX8tOBFjowPyNe7Cy-cZLpmVQlfzAFuCl55TmVh_Aid_LcO7Z4NqfFhpkeMnofYmK7St5GzpWJNStsOL7q5s8puCk2Ib5ox0bV4FX0to7sChTpuU9H7-8gBhDt4aFmdhip-3Vt1ogXiPYc3P6oiDbJfkBXCydkwxm8jFz8D7Ne9j4McR97TwIZ5ABbasuhLZ5-yMYjt2ekdfCIaBZsnpwPYR8DhJguY2r_c6El267tfSAVeEAfFso5ShVOjMdoTbOtaLTAaNQPo9f8F4WKh5rexz_UlLqk2ypZkNKbejPBXCsaP7_KRpc87JQ7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj18CPj0gXTyJDdnEPdoVTLp4Z5WHBi6a-u9d5MJLU_KKAOlLmcSbGXYA_bFLAJxOiKsmdd0KWyYA9DM22C-ce_GsqgVtNCRjd02TLHs3fjqEJb5Q3oZGRTo2lBVh567Eaza17C7fwAUfRzFakgNH4fc2kFkhfNqWxO83iOWd6uH4uS6CIg8tL4JnhoR2Zprjs5ccDUV2endUWOGa7MmZ-1QrSp7_JuZtq4dGPAgHGj9LOsZNkKzRk6cqc5Uxpb0_Lr6kTn5ZQV7QXDS7r8TMAjBwrcWjGE14MEIwhba38HY77-EozmfC3BXPO-kbTT0g8KV5KACEpGE5O4f5zVthQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhFwGtWpPaQjXUvr9JEUqxwJ_kAX2Vha7XSdbHTeCNWEOzLznQeWrxONY2f-Xzf-JIq4k8jFtnfF5ksmI2xRoEow3DUsKuw6N3NdzAknSejilMq6SN2Tb_IiBCHFqZEkDXmHBR5qLDabULAo0BtihXolZLbmplg1WIuBbZh8feAGXZQFuI1gXtd0zOLVtDpWUXS4uEJwPX5RqcC2AmoIp1t_EoHytPtEHJrWQngVmNvuWtofOZAtEPsiESgxvHi9YiCipPUAK5veMfT8qPRZJYrpc_YM7pJkAj16CWZR6EN3y39i4CCQi7gWo5AgJ43xRuvkj6wAvzg4l5VLKAbs0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFtHt1qHmvJZwtDPXTJHocyrguBjzj9WT11lL5_KA61455guiolAOCRgOs-9_2wjw4iDmx0I9mLeoNUzi134wxybapEiF0qQjtN6e4PUPsK_fLl1FIHDaFHS-arcYyUxNuI4plBbw7TIpNGNyBs-dOacxcXTNss3-N_fMJ0aLPzqiMbxmZVrKbqHafHEwvc9-kuMeNg23L9xNI5nexd-EQwNhvSE67rkcT7Z-mm7cGHCDZ4uxSHF0ov5BTBfzkSY43Njs7Xi1OPUAiV7lqJIog6VMRU9ta2kdavpuQBg0e6b9JOfkK0KBgoCr-LoL-syX_WQvAU30lyMssMDyK9mEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXfQvWwC4JRN0Zz58SODF-QdxypaklMW0lFWyu_IVezghKG_bK_wMxT0O-CgBRllWHoU-BaGdhpMMxbiELSckyumugm4BgZZlK5hSFrhLg_2k6vUMW88kAhyieidA7D0-w0wAmsJfDnBuB3Mzxb7R8Od5Puo5-9jqla6qffo-8hz4_NtihnGqap1UnNyv1IBovO10Yfs0W2-p_GIyKWvBTn6g3ni8hMIrnn2nddPI39ChSu-TQTiWPzWylWSlClB2M6NouBQSKg3VqrGgTE4TJVygmskIUYO9DDIpP_IkXLSif6OAUJw42uhg_ucwOsbdTniWOtnCAv76un76lZHYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsXBIVOLQQqPaCgLEm_eWrSqE-g5U7TwQ6C8QNZrCQkCtMGTqhYd2JqP1IBZYBfWOS2tUgl680q-qiNr6J2lm75updBWCrtLynABeTTM5WPRaYkZ7q7ha1stnQp0cxG20EkyP9MrzR-mlEO8obU6gFEvliQ9smN-8xM0Ff0GeXGs7u8iRKfIwIlBpSSIqYOEnEwu-datI--bGq8W0dqeY-xyQoEGjtaH3WqE0VLNUiDS2hQggrukoaDfBAtFXN3SKdEIJhBGt_7xl6gsmDmwcK1-EbJ5B2-HJu0orD5S1wiMa8lWDJyJoA8Yu2fYpqpENNeNat47cJJJf2EzSpCyRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INg1sfXz_zPXiWLuxDZvQ7OZg7L8U2nuLC7-r46gE9dnsoRdsLBUgtAK7LEhSNPjlrREzcj-UukwIBhcUAeL0wVeN6bIGdDMQvBxaDdLkkYqnT-GAm8aRU8SsuCHXWxt3FPP8kSDQclhNtx-nxQDouomwnKOqYTPrVIxbcitkeIhpWY9qu3Rcak6CZDMKL7sc6uHvARrAxSkSOgQ9uuWGRu1MH67w3kYQyypj6mmvi3oMKCMAp0xQwwsQblRiuoMZ8nQbrekQr-057wObqurZWdt6fhVYUu5PHW4P6tckSVDommZWdLdWHRt8u6MR8z1OouXHo6N4pD8JsA-xgCL4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV6lHOEuvJIn8-0PuqCokvh0HHVcUbZEGFapdy2HV5HHMNMY0SwsYbaVDQOWcddoJnSlD-H065JnguFJhp429z2iDfQ6CfoKcU-KGqIyH3v8EG5dc020Ma7G1_GPSOs7O2lJIOBtMwpI0XzWWj3hgSKkPyEOtK9ZOITx3qB5dQfVzUHIqSeqeOeUPUqcdEgHWskgMQYQaURAawlzY8RjzmDDfVrbVdUGjm8Dlj5ruDvVo3FT54cwYY6Peh5dqqtnPzr_3itHcEqBwxmFnRgOmHQfA3gi4d29BDxU8SdlG2b-jCBohszV5xgfx3s5BEtxWOEVDoEmKA1Xg3BqAhOQYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gpk9coAeH7_QjDo2--FSkgCrpjo4S11Yi5RAkLYrdY6qxY0tlZaIQF22qaT5mVkDyHBiN-vdQd4qM7b472uUMWuSxIIWgqtgHPiWmAvnOIIKxyd4GU5BaM6eeEGKUL77g3pTMhVcgaRMYE8ImOkDE16MCPNTgo07CTvcM3AytpQjcb7ufSwTGuiMf5RRf9OpgcAwOLu9g1j3zgK5pUahEAtWIdZv-dmMyW9SH7oOsRKIa01fn2y7b8pwi7DujPBG6Brss521sAxbbS0Zc6UNVkiOceo-numqYFSmxD7E3g59snkbOIAUet2Q9bqqID_4Ht80n4T72_nIoGo6AF9DmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULygRTUphrcGa-RxBzE4UEisnITutOMKBF1vIHXBTVBKCPJTDrBpdIQOvavrM6JbF5ws5Un8h68pwUFNNeJ3cUa8YTr-_iNjwK3V0WMSzz2uQBB8IUjdGkb1WUKqn7xF6V_eJAfM4rMiqNzLhrieDqah-Ah-w59ZKtrgn1Hsu8kfOTRtGCSVD2IdW6NBcw5A9j-uepfcG1CS3y0ExK35bmP6fMqc4FlNtv2EdTunT_jrVvJZF2jR44jARdvXByboxg7dw6XLQ7ZVKIucajXHJTeKtQfsQf6o8HBc4OuYW5SP62rSUho7vR84uQaKHOUpKHGBOgjhRUzEyjoO56a6Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gtr2uzYuZ7v3Hqi7KdDQg5PQDLPxoCSSQKEwtMYlFzFxnm1LXeo-IgyZrdRvjLBQmULl6NJPs9_vVOqhuuJKaayRe5B89nNoXZeiTrMxj5JJHmCDaVdjujEVXEzZ4NXCIufcCRdc33uqGJrD2WZNTj2TfE03EIpraSbfViqgoK5QZGhjtlPgy0WhVzoeLDzpnNrZ1Acg5Niil_gefbAcvm_mVV_FhZp9DcQUboYPQk_VDHOxiQcbfoKtxq9u-ramaTi2vYPBYDGz_bJZH8C6xFHyIuAwoCIot2rBg0uWXCJ4MzzP6x3D6zH8hck26noxnNdNMgZyddDBf0K20fhb4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-1rn2g4Gu-SfuS2hoZKIPKictA2hGnwCThle1UCi7Yt-qKmifFP6fJDVBGCtHy522YOek9Y8dSF7iD1ISiEVF2T5irNMJYhixOXvPAQpLz3LewjCamd6TzKxUXTy-U5QxQCrilFgi8KqbRbswpTSaAteLHjdEfxo-yiN-bPtF_fh3uIyevcWX4C2pbAJUfnX4qA7FRB4BHoiYnXjw-0_a_zW3Xv2gaSDBKsomXQbsaZ38Lx93g7M0cwOn9G-AtJ_b3UNWUOEOiQZhc2oAUM7LdmAnfWXZBz-sN7wokD07RRtu0LS06eeD7wcMTYpfOTSzkW9otORdozww93deVAhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxpVYGHpMI3wCt6cKErMsP8qAljlrNaK2Rb0YMDvOaGNAPhXcV-u7JJ7NtkQ-XOvUN79adlq2SCtVEnglgb7PvBfHoQEw-INtBdaV3azLvezVCnucS5vpTKg2XRa97hLw95k2M_N4PareszLkKCwRZoBeAtAzVLL4mOfSWD00IzGzZQs3qyFsHw1Y_lBM3sqI91NmEh_1jobpP_2Z0xdvLECLSxKNkusA1uzJMVGjkZmLR-Oy186bOOlZH0tVeBhW88_gYAJL2qbe0N_Z46DYnlaqvKWd1LTzhUg2Dhoj7Fojjqm6d1A43fbZvohBVYu1GMqye6uOD5GuRqAAP0kAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncJB0FJRQNsCA2O-twyeYPj0GtAhREDmMMhPC0F6qutS9DO87x038D3TMv1piMoYhwRHUROAFJ7418HSEP0ryWOmtK5BQF9pWStc62jgFYL1prlXbL2ApDss0jWq1xRcoIqMwfhFkCssjK7PMBrzLu7IeIggHl02Vw8cfZhTlbtJvIBiK7OTTZH4xD0hsWmZYwGwTomdrmo8N6vGaKWCZOJde_1lqE-JEJ7tF-7BJCPWBGJ2Td2gaeSav7c7J5nx9uP6twBVlzuqgYJVBDE9bmPnwwBYzIHuS5Yt0yb2Rsd-zI5Ya5Jgwrie8egOWqGnpj_KYznbgxe1dm1njjpufA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn-OgEg69ejN4Wvf8daqErXRuimlinX5S7Ob-sYi3Tm_Q3d4bhnY6hhtJrL3sKTd5Wu7mP81407ou9B_D0t3qxJDZDIqFSDdyVQppMIG9WkwBaBroF0dtqHeQAGoobgXKY-oKjAMVgOFV-dC_q4l-BPPSF_ZQpWY3APeUQS0mw8XKL_QAvZ5OhjjyBzHNB113z9J4dDFf0eRXCAGDh1NJXFmkW0l7GsqT5enbDXKSAPh-I7IKH2OR1FYZRV-G_XjU7mDHAVVjjwwPEJADvKnBkEHVoISDEswFU-vEbFTXMRZaqd4eI4fLLWQEBikPlt5GPwX8brcASbQMHLGL3OOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=ehFhAk7iH29lx7RY_L-IwldPIAvk7vCO4U4nWBzWR28qBB453TfvtxZXDeuXpbnnWPonH3_bMjq7Hwi7gJLb9n-2u3kjOftExzRMk38V3H2IC8BG_nypMhUuBh7GBDmQERq56WGMKNPN4Lhsf2tWGbjSuEA-2ndcCbik2_rpdMWWKjSORflQQDuEm-geSopPSCy2FKJ0BEH2bgHlOBinOQev_pYpge7N-SIWYWa9kTU4BR-IP7UpcMxzAkvTsxFSoDl3bTy2muSAC6YfR6QHclv32wiSQ7AjFgUqBPkuPIsE1LcFymChkdouGeiGwjfLx56vaBieKcjfR-VN-_RSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=ehFhAk7iH29lx7RY_L-IwldPIAvk7vCO4U4nWBzWR28qBB453TfvtxZXDeuXpbnnWPonH3_bMjq7Hwi7gJLb9n-2u3kjOftExzRMk38V3H2IC8BG_nypMhUuBh7GBDmQERq56WGMKNPN4Lhsf2tWGbjSuEA-2ndcCbik2_rpdMWWKjSORflQQDuEm-geSopPSCy2FKJ0BEH2bgHlOBinOQev_pYpge7N-SIWYWa9kTU4BR-IP7UpcMxzAkvTsxFSoDl3bTy2muSAC6YfR6QHclv32wiSQ7AjFgUqBPkuPIsE1LcFymChkdouGeiGwjfLx56vaBieKcjfR-VN-_RSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0N-9esoS1i68HeSO_QevCt6goHXeGB2IcFq5-uytTqD3G0yqiQAIQEx8SFZGbvNfkN9zWxZl8WSpSrx6HegxzWYrWM4ZwnbhR2yTYohvDx0QrnHuDp-UpaJ10UeGqIvpU0-VhxYgE1z9MnxrqNjJNbDzdQinJ5MlHa5HsC3wr8T-JoDIzRCDMFSZwgn8IcnW684Z40ardRZlzK5PnchlcS9Pr5Zudu_GtEqPI7DeYrFY2Wk-CrMwl1pJGfzMUxFIFm0put4JdUJx4vwEmZv3R02OBtbXWKHrGW47CS8VM3-Oi0xCWhEHE2sPRyiqqsYrA3t1i85d13JZe11fP9r7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9spKGfqoW1Y4cBhNzaSCS3MYgSwPPM5Mv-8wmFB0hL1m3g_sPX5hYiEwJJiYcAOidJOLihxtVvQ2I5igGh5P9l_0IeyHrVKyuFH3NXzQwY9Fhe7s3uY2uhEK6lyXzCQ6euEfNbs92ScgFg6a5aObTZtkBkbg0J3NthyaPt-KQkU7NqvUc_hAWRXkco7RmLZTlNPb2AaFXHAXgwCbmOfIeXUGskPw57PRHLAi6-Po4Q_k9gTcOjRE7nKniAvCDOc63AzTF8s2dJirOO3f259hTlRWOL99rB9HMWX3LlZUQt1PIV8EeIxiC5h99ssgJzlop3nnFgDpeKREZE5VLyMUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=LC_BbhEbmccxkJLTNbo20Fbfg-eEytfsk4S4hf4X-wlQSHhSgHAz_y96suq1sO7_xqk5-gF51egW_qISajOMdNh5yVnhyrJ6qDFXJIwRQabt4BF7Qg1abtjpFzpmS3q-04O84beOGnMwixu90Kg5CELdsfddBHAlRh1E9y-AjVjld9kQLA1AbE93jQ7lf-dTeUt4u-ppdH4PUHiBXFqeLnHsaWeghZtTGAQwiR1MAOmYy44U6rECLA9Ci0wFItcnjnw10kjwOdoSPao1A40XoDDLiU2niOcEvvWtXP5CEpRd8toX-oGyi6_8j3YGlFiGt86pxbQnZUAoiyG5C0nvMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=LC_BbhEbmccxkJLTNbo20Fbfg-eEytfsk4S4hf4X-wlQSHhSgHAz_y96suq1sO7_xqk5-gF51egW_qISajOMdNh5yVnhyrJ6qDFXJIwRQabt4BF7Qg1abtjpFzpmS3q-04O84beOGnMwixu90Kg5CELdsfddBHAlRh1E9y-AjVjld9kQLA1AbE93jQ7lf-dTeUt4u-ppdH4PUHiBXFqeLnHsaWeghZtTGAQwiR1MAOmYy44U6rECLA9Ci0wFItcnjnw10kjwOdoSPao1A40XoDDLiU2niOcEvvWtXP5CEpRd8toX-oGyi6_8j3YGlFiGt86pxbQnZUAoiyG5C0nvMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=pI3PmCmf8Y4yHkg5__p1f26uCQMQDT95-R_uOG77jNH54B9KPmHHul8hAPfYWzbIwtTBUuGOVXrHcp52hKFWsHKjqzKAO23e1P_VLwU19uwrUn5JWLmGnl0P8sDIdMVssT6QhX8TCylvQc9U54oZVydj7MYOAx6OoolUUdX4AQPqY4vzqb7R8bSTB52pq2N7Rn_IMisCOxe3EFIq7nFZij0G6DGYHzMI1nfOpu0yva_KxKYbe1AbRTBUgJYVSrAqhdZ0qKPzKVAqO1cZg-eM1dO87UhwkZ8BRMxi_13zilw3aWFBT0zfoa7hESfoLIbExsOpLRxOQjq4kttQF-lFYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=pI3PmCmf8Y4yHkg5__p1f26uCQMQDT95-R_uOG77jNH54B9KPmHHul8hAPfYWzbIwtTBUuGOVXrHcp52hKFWsHKjqzKAO23e1P_VLwU19uwrUn5JWLmGnl0P8sDIdMVssT6QhX8TCylvQc9U54oZVydj7MYOAx6OoolUUdX4AQPqY4vzqb7R8bSTB52pq2N7Rn_IMisCOxe3EFIq7nFZij0G6DGYHzMI1nfOpu0yva_KxKYbe1AbRTBUgJYVSrAqhdZ0qKPzKVAqO1cZg-eM1dO87UhwkZ8BRMxi_13zilw3aWFBT0zfoa7hESfoLIbExsOpLRxOQjq4kttQF-lFYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=uBc6CQY0dE6HAs3huXCg6M1iDcp7iSIQ21-3rci1Q-crvDo2uNKaCR3KCnu4yHhVH2PzXKLr2plSOeN8izSQ6jRsTsUFdG3SQ9YYCoei0DFNuoLMlUjga4ig6A2-VsfEoca_T7ER_dU4tZGRsd2Qi83LIOd96U3Qo3zINvqNHa_k6UA_IaRElk1OVCbzeuXbN2sKNCqOtVTKvckI5wUTxSu3W5wwNoFjFykYzguzLeXfMNI_ZCExBKetoMqA8zRvCqOszQKhjSUowM22GhTfUJDRScJ-DZ0iyj4CgYXqEJo5gNO0pXjbMfmVVmjMZ1rZ_MG7KJeau1mJUiph6Qqd_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=uBc6CQY0dE6HAs3huXCg6M1iDcp7iSIQ21-3rci1Q-crvDo2uNKaCR3KCnu4yHhVH2PzXKLr2plSOeN8izSQ6jRsTsUFdG3SQ9YYCoei0DFNuoLMlUjga4ig6A2-VsfEoca_T7ER_dU4tZGRsd2Qi83LIOd96U3Qo3zINvqNHa_k6UA_IaRElk1OVCbzeuXbN2sKNCqOtVTKvckI5wUTxSu3W5wwNoFjFykYzguzLeXfMNI_ZCExBKetoMqA8zRvCqOszQKhjSUowM22GhTfUJDRScJ-DZ0iyj4CgYXqEJo5gNO0pXjbMfmVVmjMZ1rZ_MG7KJeau1mJUiph6Qqd_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdPcjt3n7vusZ0mKbJUq24ewO3F_z_5mzkTpGt3Mj9jJuXfb1q4Kag4owsFjHq8BF3oq_8HSqTkq4liHdtf7zdLGwnBdwqail0Zy-Xz8agbTT8O9bxc-8hhOP1vsshjcLdIFld53MzwAao6BAI9gs4Fe9I7z0XgDBgiYMtY3KqtDUfJD27B7kqII76HfjyaAS1O-P7f7dUA3M53c4NVfweAE5CkrsTn4LNCV3tOCdcoVEg_4Pz7h-8TYaUyq6_zUsb8nAGBhLBYN2_FpTne8DIbJnSYLUSF80mM83V4ZMYpNBpN8gmc8BD6UPrEBRYL0NtAB8uu6RGvIt0_np62llQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
