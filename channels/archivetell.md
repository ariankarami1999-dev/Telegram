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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
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
<div class="tg-footer">👁️ 108 · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 756 · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN6JSsuNnWss8WIcrB7squ-XHBVvzKXI11JkJTUBTU0V3LbOJGWvfVU7gLnr0V2mS-GLZRTOWn7Vp7OBwzrBEejQeAeeqwjX4GS8mCD70BdhEcBVj9puwf9KaLUiuqJnbsGlF8aa-OkBgIANz1eMdWbv4BFXTef07-zyxROB0GbDKz7vztOv4juXxeC4bJ9QEvi3yhk_CJRKAZuIQc8JnlMASRfG7L_zMPeCtPfb5bLBO9FCzainPumqUNuV5Ex7UfoRUUU8VRCVr2aFOl-a35D_l97DAvsP1pYGgp2IuXTlp6nnY1KQURHhuJQGvnzmpqC0cvFO_xo3xMfFpSGUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFNsLuAj_Dr9JCFqT372bq79NKWJoxDeh-BTZ6ymCBEvPYF_U-AdlVSySgUzlfKW8pYpxmpnkYAHCbBqSjfxAorC4x6uCqURb8rYPCxz8QexEgenhRJbEWwkX9PXIGFRnfwIl6MZDjI5Lr1bqSXNhp-3hBKLveK9wlZvUBpSBNqqdIk-Smk4nC_x-Q9lBEftoB9a2d12ZaFCMibsIRyi4DvWtz-EAsavxa_YvR3DvPdt7R3wUtzkpX2Pt7MukpFMwTu7n2UUxl3okQHquGbKHBIoORPGvzsiAOZaOnvdo7G9jV8PDtSp8moDon0C7Ai6eH5PTiNWyFT2puYMndzzHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E7tSd-nWRPAnaGKHrUkFquO1QhQESdlgUI028uaX9z0L2dZce2LO5TkrM0CVSnJZfFddsu3qI0sHxY5gCjtt_JNj7ajAo1c2IafIXOqhmmowEgQgTqbPWma1nsVhAogWlASPhEug9m965Aq4jpLw7EPf3Wy4LD4JOMedVsxDQ_FDg74Ah8x-mSqrALfUr_nj3Qg5bydXUMsyTXaQl-7J6scARHbaARyjnIBuoHhos3XP9dhfn-n7tM_M_phqwHo2QFCZxkf0hGr0omytyWxW8e1NaKwcoXVaZXY4KSzsWAa6vr1OaG2q1ToG2nWHm2Y4yw9g9QMAvMWwTUEjPX2Y7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8Ff4ZST1Jpok25-Uf3wAulm7dWyCYUfyj7K-mwVDe8K9TzCgu5lHPA1IEZXDd3lBbaOzBZ0iHARJ0O3TyTH65SI4XYCeo9Khm2Jxfg9P9t8Dl8WpI8FDwkMeE8wCkmhiU0OXLaEcGCxtlyjck_aGeGkyTswBv4i_KJOKxz9V9WNslbHZwqD1j1yEO-_sm1BOu2XA971LwPqGljYXcoxtngZINTfLW_efhlDBNpOaoQZ3RFf_WO9HA_WaimiGvLPFp_bodvxITKMltTqUZVoihQs3JddZalRZhOYFVXPyi-E3F6LoD8-JqUV97r7TLnuC2-y_Ljt_p4dKDdPZZRQUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC7n3eWTa-2CX8pecsgoejTBCPuDt6ewWBOj18b27RUFpQsHr5pJtw5DhXB9ojGiKriLbMy67afLwbFNir5FCUG2aVrHSuysOLAlY49JQMGP3GapNOPU2O70Cc81fHxmfM_SJC5HHWcHjzLc4CNT22zNxXnMTsDdDcsUpCQGzJa2DkurWau7pBJL2nl0DObeltwWKx3isY74KtT6K-_kDNxz3PAip2T2NDFR-HkOyhEhWdZRUb68ilThx__f-e-7YKPlFOsd9s9sSa1-92CrHnqW4Dmouc-mh1U9dLtAOSp5BW95EPpxHSo04LNrpMB6UGFwRhXM9CotawIFay2dXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUz1JKUn0kTr6s07d-HBov1Ws10IoBFhISbfeLVOdfcJKJYlvB7bbKGKtsQ5pdkJlIn_5lyTuu_BnnGP_vTtxeiZx3YTk62fLGnNLQ4sOMBCA6zDsm6Ja4WG3em6L45QmvqzGw6jFtyWG8BcG2e3h6gHblEZYiD1uri_NqvEeqnYke2F3tIflnb7_rG1eedlUBTZKO6fC-T7XTkW-SwRJ6YyojaBMWlz5UyazRuSyjBoddaM1TdjC9Ez9m6bHy9mxEva9eG50Nybesq1Zh2WSP2llRKlbZnSHPCwR2v2S7tEGXlSX1E1wCmvqZDfTSZ0GL1XWBzh_jv9CbDAPPo0CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni0cch0iRPMPVx_S_UXzCP7cqVLWGGprQgkitbI3_dMUcuV7dT-ht3AnaZmS2fIQ35pZxsiynR1j0DFdk9okZXcONKMu7H-vP-cP6SUlQmVTrwzdFfar-p0UulUn1w87bDovuyWIL8-SkT3mnvQ9NI-YXyR5vRZ9eUQ02GXzkY1S-scePcQALE8vGULJ7qBDQC_d7KUMYLMF0qvcX2axMB3cDmwGANBQFv9UQrdljNWFmKe4fcHxqcAnI8YrSDKj19NoqdT4wWDPcOHIQxGeRsUyknYg23DiRWu05ZrFSNhtiQl4Gz9ZHdojZK5FPDe7jBVjJ0VjKum0rdTpjQcWJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M38Eho4wECVXFw-xgu66TDYYJY-mI7E9DhZ_WozsiRt8la6NuNcG47lHw5muH4Z60diQiE1STbiwcHLmooXHHSWnnpeGJY0oiB97lCpFrL7bM0jWL2Q8nOE1_SYLdgxF-T4Pp7xEaJQwrA3x4aeCUl68OncOXoec8AU9IoyK7zb_CpnZh7PXTt-IRBAF-RyAEnIx9cIoZnWFvCidfnNzMR3-1-sk_RkSjiANrAj9TAS90P6-riv1TSsI6lpo4cXGX4lvpvZPT4e7qMkh2awEZGWDXLkLHohB6hls7pqSTdD7H5NtZM9y8mNqU1AjZl355GBRAb-XasKHiFh38SV41A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNc5S4axMZbDdSUj3gxO14A1O3ksCukgQ0tHbPVxUArQZNrctLsMWPim1QsAVDVcK07uTtwpbt65BJI8YnI3SfppnNJ_ZTxSq3orTjXwdElmvL1nYup-TXhdPqtTac9cI8t_iCTg4ZlO90G0coDoi0w_Vwo4bwM3F0l4QvtEWGASqanUly6N2MpEnrtHbUhLI34ngId7geR5xnXlHj3gc423wH-QpbOb9L-WVu9lEQKg_WtkonFkHzOf3scAaMCCEUb64J24SaaTWV06sHpni0fGUwRqiAWc99gtaMKM32PCT-JXOKohKJXnmfDFFWulCnsC7_Y11412MScj1bn2Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtiS1b_nO2NEa65e_175skkkTCTdxPPPY7v5ezv6JLyxUdROPyeGWkpPOcl6G6ZfLJHp9sc9jXpOEBCLt09sOUqGR4gbshqugKF30PjtpXUDa2VUeuRkhcJ6fo87m3O12E32Eyt_UOuiUQGEc6Jf4_KDkVld0jmgAwz4RNSC0csuJZRBcDqDU2mooAtMrW0LK1b4jh_E_zMob7PhdXdE1saIk76-RlXJiM0rWj6c8-Is_Q29snc4oPKXrMncdilzno8XQ9n0wvozc_gD0Vpt5tjEUSc4D9MME1wayaVn-rMzZ40erqXfJEMXs9xmbzKH8goclkUr-rTFUHuH88v2vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD7PQMFkRISScAW1AFbpYva24GjHcoiHdEzNmtLDwyb_qKncPOiLoxtLvvW2o2Eew_UmDZYMwFkKUqKo4vgq3xEa6wRTgBP23N4lGDea8eiZhK5h7JLbFaIrN8D6Kf7jlfhWdz9FOnd66iWZZ7XkZvLAzWXqR-IY37R80SIHTANeG3bJkrqBoBYWjNopkacGOgoN_VGYuqErNCT1lgD3sCrQTPSRqEDafBkyk2icpRMmSZn7Qtno1_1RD5eje8qZEH_ICMRne_QI5AGyNi0FILqFOWh-fGT2BaUB9Tg43d55eNJxfzPQh7DwgmipWxOvUgIUqIzE4Ko5ag0zIQhnnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7yszJPswPvmbKZYi9Zx0kqf0dIiquzGrl_knUkgoUhhybWa8DjA4M9hqIiz9gxrOlQ-KqOUjjcErzW5fcHbGG0e3s6qb9KWlXJl_7h4Y_nP9FSttLTpDtSoEzGNqqBUMqaKPKmHrUidlFjuLRHMmpEDqU-0-z81FlwoDagkBWCvdUY5hyyumKdAzwHHAvc7o68EC8EYrngQ52QK3WbUg9_bfecdDPBnGQ4xKBb99tQS_4Etw6ZTjrv_yGa9agwG7VGUkuV-TVC3p1Nvo9eRCKSM5qhblVQ9MUjNTja8oBVMPHwRTKzUphw3uqjxpaI-07kom87k3qyktayVmGgqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WptmG6tTjIv2xHt_sNLtlNeWq9h-XZaG74CQi4bKu3GyoUXSxtat4b5qYGz-O3hbcrn0Vl003EdGB8PP609FyXwTwNOmOIN3VAZGqlQUVo8ye711svdwXIA1nltaWO2pLtt3FdbGJ6cpmOfSjoGuM37osuVXNbwvYB6eTD6uQTCK5M0MAxcRwSACtAxiuKO0FZdrCf89yAyTvjVjvhaopw59Vnkq1mdz5GJZZ9Bque7Bp4sribsX4GcRf1QOsBti8ManpieCquabizYBe2SAaaJbsPdvaqBe5jm0mHC_0QEhe8eF2pbEk4djMC32X0pWhOe6CElz3KQukcQNbLWg9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJC0wLVm5ciSvOaOTKj3NkSw7zqyCJ2WgviRFlpLRTE4IueSFFGkIZuhY-jmVSURBVVp9JIFptLKd0a4WBJ86zzVWfXI2lEiYb8Ezkbn-QrkHEgZgh2wlQkPqipkC1NxscApOz8PlriPdWwV8m2YL24uaDJcjRTLaVqcG1ptLupJFCEu3DkYMf_KXrgG8SSlLQ6L0L6TR_-Q3JxzrI4TsEu8eJsAVyHbajNfaiSYUz8b4n1ELyXlVdl9obv60jEkO3IfeYJ9uaSPTARTsxt7F5GhDUb6XRd4UlZTCfv9oYT745JU-Pq0NakVNYeyDg0UMjdnF75tuhDhjQ90eE7p6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd4fAc-Dr35sm1FAc_eGMvbI0g-N8mwGqnDiIBe2-Q4vdSAXwat8YBX6YRsYoatMT8yFOzqGkQ3bb893wF-T7nGfIAQV1fU_C3FKVVEs7RfTXRYjMdUhs6aikTqTOpew15eN_PJbqkyYWDFrKERSi9iuvaoxm417uSF-dSUI2LaygVkKAq1oIvfCUmDB7ZyrLs7xE0r1FEaoTx-Ay4JE7h9wNcZycayGeF6r_UKJr0nGbAA8GIzIXT8M-v8D5QYH6QM2oURdOE-wtmR2yvP4wmpb58cTzOcTN5lXIvIL4cVq0gLDkfgIJh6hdEfcZsBi2HPR4BaeeRBx6Q9ecpoDmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMEbmRA0hvEQ1WYZIKrzwtIgD4UdAA9wSi96QbJYgoI4IeskY3mIGz_ZMdjt02O1vwuG3yMFbq5wiES5BuXaETZSFKqAhuibDSposJ2Ew4-ytNaDsvapdvZGTyCS02n8KVOEpfM8lTHtQ_yFdCfSCHmEULTVk7YkfSY4UXc3d3zArgGJ98HMcX02qVtGO91R_lrXUh5doJD5nPoyst5W4o0ecA0n5dlFbhxVLx-cBaLsFq76Nchi_7uPto6rUorzIolLhjAvVTsON9ug9KKuRFGbqUTi1B_C7BLA6zWI1YsfMRtlnWjH6VW9OdhljXsfoR7mSagbcrfgywVihEEgeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBF-XUwGWFvyAyd06zB_UG6fzRJpnknZ4roMF-sFIRzFREjW5uzqWey7dg7wldjgjxRZl1DsWeVISeVUTXrB5tzp945PCuB9Kmk-bzZ4re1BTDa55wko_1VOw6d_maXcSc4ZcGfRIXFKzpHziWV8ivkJV0WSRJY8fXMN-3wzXxKimcxij21k4slFH8gRRuBdXQr0wjQG5UniDTiwVTwVyw4yi8eiOP6BUE0DC9mNXVdqTitfb5wzjxQp3iO2VzB9dfZqUqjIgZeezoGe8kRByzKT1Mr_54tBZH078wQgmCNgoYuVAt-juUqYXr7qqUYR1I6qBy-ALtOkWOj7aTDlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=Zs6Kh7T3LhiQVkuFiGZrc2nvP5-lRt_6XqpuTxNfNsG3HJV7p1sYbV-Ds4oQfXffjZBYRYECGHWSFx1udAjWN7B0j3S13FV73lr_0nezZ2Gkq28q4DGMFXog2t0vhxqY7TdHwikvb5hCollXfN4QAxUWBl2dENEqOP9gBzt5sE-c6UwWSemm4NKHXbyDZBG5IKuONLgzSdF_ZNqN1eQuthNci7z8gq4_51KTz__vzRt3aspUvQzudp2mRAVOaaKtqJg5jyMGA6lEpo2D5qD5WQH4-PdhCAVflKSNIDK-0UZVUsKcrmABR-b_uxWXdofj7j4maBllldoCHNehAW5ORJ9oEnLMsrX-S5GC-eAmz2_lvw_E-zlzvS0yPckPkMonq7QrrzQcNfMxZVcJb8R-0WdbbVC7iq9ucdAtDGUZMm6WwmKrrVRzA4B3jWX83EESh_ctcd7Oref3lF7Z3pRILXERxIJsHmVWmxe6QkqGoFezYz6YrpMkEolSrr4270DmDaS6HeLhj1ymkWQvmH1GMMS-MLxJ9NtuC2v3k2AL0J9hwx6vqu0hOiVSrtnXQ1aGgDUvv9IMhM2IvBrn8PldZn_Pc9VnPOIrkB4LZR2eoIgUgmCW7JpXBkQTCJOW2BXQXgLg_ORzoQwgwCYVJhjAo18HyUPSzg_p1a5zcNZZd8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=Zs6Kh7T3LhiQVkuFiGZrc2nvP5-lRt_6XqpuTxNfNsG3HJV7p1sYbV-Ds4oQfXffjZBYRYECGHWSFx1udAjWN7B0j3S13FV73lr_0nezZ2Gkq28q4DGMFXog2t0vhxqY7TdHwikvb5hCollXfN4QAxUWBl2dENEqOP9gBzt5sE-c6UwWSemm4NKHXbyDZBG5IKuONLgzSdF_ZNqN1eQuthNci7z8gq4_51KTz__vzRt3aspUvQzudp2mRAVOaaKtqJg5jyMGA6lEpo2D5qD5WQH4-PdhCAVflKSNIDK-0UZVUsKcrmABR-b_uxWXdofj7j4maBllldoCHNehAW5ORJ9oEnLMsrX-S5GC-eAmz2_lvw_E-zlzvS0yPckPkMonq7QrrzQcNfMxZVcJb8R-0WdbbVC7iq9ucdAtDGUZMm6WwmKrrVRzA4B3jWX83EESh_ctcd7Oref3lF7Z3pRILXERxIJsHmVWmxe6QkqGoFezYz6YrpMkEolSrr4270DmDaS6HeLhj1ymkWQvmH1GMMS-MLxJ9NtuC2v3k2AL0J9hwx6vqu0hOiVSrtnXQ1aGgDUvv9IMhM2IvBrn8PldZn_Pc9VnPOIrkB4LZR2eoIgUgmCW7JpXBkQTCJOW2BXQXgLg_ORzoQwgwCYVJhjAo18HyUPSzg_p1a5zcNZZd8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=dDd2eFPjJlOAiKL996pYm2kd9V9n-wClhsFsO8n4ScZ3om-xSjj_hzC5lsvkPrcihpUR4pJnO8EgA14MtWVXjVct5ojmmmvnWyhXmU5v9ueziEJh9SH0A5t0IieaU8EkpPyO7lPj43QEoE1nNMJ2M8NVBdl6IjFV0tb74xVEte6Xg_A_wwzYFqkFcSz-cxniBlKruCsnZCOtYfyWb4bV2-6OVcznn80HmPHP1QqloGoAs9hYS6Rexk0EM17iZAlohk-3FfYoVTNTrDurbjSmF3PnO6yrir5jM8nwmuTD87J72rxZtH2oXIov6MPcTQO7XyN0spBW_Sgj7BCYsw_w7304rdTCTcDMRZEnD3F7byRobexnRgopYdd8bT1sZhhwKZbdpfDPgB-x1JNAneP-Bz7TDm2OhzYIQ__Mx1A5q4Uv5DKEAAbPJXtzcP4cML1YhOt_gefAqQxuTLSBp0Ay6TlK4CFVxfdH7ipicQxFXZ4UcEKdif9_kLyDv6t5OqEEUfzpj0s1x1aodNHoGvB8fKezh5_D6XixT7o1OHeYm6FeGBXN4ZfN7cdDZGsp1_UOLkaXQkO4k6GNRbYo2A9B5ZPsQgcL1oTf4GsLqDuHb2aO4oZXqwZ9kH0ieq50X1r5tG0udYQkEHJxWX-IRmP2HzpuF7SrP0f9nMercI8BzMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=dDd2eFPjJlOAiKL996pYm2kd9V9n-wClhsFsO8n4ScZ3om-xSjj_hzC5lsvkPrcihpUR4pJnO8EgA14MtWVXjVct5ojmmmvnWyhXmU5v9ueziEJh9SH0A5t0IieaU8EkpPyO7lPj43QEoE1nNMJ2M8NVBdl6IjFV0tb74xVEte6Xg_A_wwzYFqkFcSz-cxniBlKruCsnZCOtYfyWb4bV2-6OVcznn80HmPHP1QqloGoAs9hYS6Rexk0EM17iZAlohk-3FfYoVTNTrDurbjSmF3PnO6yrir5jM8nwmuTD87J72rxZtH2oXIov6MPcTQO7XyN0spBW_Sgj7BCYsw_w7304rdTCTcDMRZEnD3F7byRobexnRgopYdd8bT1sZhhwKZbdpfDPgB-x1JNAneP-Bz7TDm2OhzYIQ__Mx1A5q4Uv5DKEAAbPJXtzcP4cML1YhOt_gefAqQxuTLSBp0Ay6TlK4CFVxfdH7ipicQxFXZ4UcEKdif9_kLyDv6t5OqEEUfzpj0s1x1aodNHoGvB8fKezh5_D6XixT7o1OHeYm6FeGBXN4ZfN7cdDZGsp1_UOLkaXQkO4k6GNRbYo2A9B5ZPsQgcL1oTf4GsLqDuHb2aO4oZXqwZ9kH0ieq50X1r5tG0udYQkEHJxWX-IRmP2HzpuF7SrP0f9nMercI8BzMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DABSQaxjFu7ltK8CbJiN6_qBM-Vf83KILdRRCmsc7YZTUl4gbAxJI1gIDjRQpyekyijPEyYBsGohJonnBp9yCyn768ifIQzXH_ipptsQFt7X4fDXsTgJmzRMrl6QSu0oqYmuH-7KR3uiMgRJdu8uLPZOS0JvROqXpdpgxLMg1HSTQ1DMjBwoNvc6qqMGcLfmexA4OstjrrgCSvsJj4L2bF9aTiIi9esyJ-RSTnKnhQgIVg2aqUSTJ3hldRnU78vrHK2nEVlbxeVHuLU9b7WP6uU3PkNevF32PGm17nKRdOIv02vwOTIZMngf9hP8EKDq9biCQQEQVvVaA4AebFKI1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=WSmZ_RNg0c99pTHFSs9jB_wLGxg-BZ9Sy0X2Wb8lRi13zXUTIq5bNAe-o1hw0GX458d8xmeTA_QxAXOdYVk-v68LRryKPj0-m3ri3HZX7l8nqBO6pTQXC7YW1frfN9hN4v70CX515InJS4yBE7dJKXwqIjAbP0hDbD1ZoXeWICvgP0FvMvEulUqbZv-cOUKbAe-QQr4tmWMywosCuwqih2GwpadY7gRkpPs8W37APJKZLBIctmscT7pOMutkh-F79IOmOCW5Djcfqt7hfnkRpD59D8EoY2rR6sXyL-ywBbxsF8z0lnxHPDOwlsVUj8Xy316WWfH6pnTBclM_zdYZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=WSmZ_RNg0c99pTHFSs9jB_wLGxg-BZ9Sy0X2Wb8lRi13zXUTIq5bNAe-o1hw0GX458d8xmeTA_QxAXOdYVk-v68LRryKPj0-m3ri3HZX7l8nqBO6pTQXC7YW1frfN9hN4v70CX515InJS4yBE7dJKXwqIjAbP0hDbD1ZoXeWICvgP0FvMvEulUqbZv-cOUKbAe-QQr4tmWMywosCuwqih2GwpadY7gRkpPs8W37APJKZLBIctmscT7pOMutkh-F79IOmOCW5Djcfqt7hfnkRpD59D8EoY2rR6sXyL-ywBbxsF8z0lnxHPDOwlsVUj8Xy316WWfH6pnTBclM_zdYZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyqU9Cm_0bwtZxUPskJK0ZbrrBqHpmSi-ERce5DirVuCBAx_evunXDpdAvV-NG_dQlDvGhTxLZdBf13slRNyoSAXVVBAFBYQG6e6sTUQJbddu0Bfd9bv3wyDNsNtRa9lU76Mp0aZy7AMTm1N_frf3jD86I5S_xLmWGkpwJ9N4qEWfY6Ze_mxXgiDrR_7n1eXJiIoYv_slgVPcmI1PfnmaCL-YweRabbaq_IoTtWKfIJhtg-tkttXraylU_Jv7xXQEJ_gVy9QeBZfq6S5YyczhsvlWbotMxvFKb1CPZQNzYc2RpM_zyiJtKvo5dI5JATd8KnWCxfVER4whK4LxCb4bA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=taFUtm8mE480vjseSQBSyzA6uxeoAGbUxK8G1-1XmRwhRb3YMaP3sugzJINwMBNvv49x_qopg9KyBkg9itGd6M7H6paOZCwa3zsc_VWWKU-8oXN9Wq0KCUIAsVDrQXmm6aY4ouIaM1l1BNF7Bi1A6AbyhNEHWyKnD6Sq7J_XviV1l-JH1jLbrLrHlSO0PAAG36D4gc5pCqZ-_k0gGtXMr-HocH3ig8OIVgJBom-2EgaSwYaUosV0tOgQjuxO-Na9XFfiYzFMjG75R79l7fuBLjekiaD_t4X8cmtbXiY0wDT4bGrJgq_Y0UuDVJQUkra6bluvkI0ircCmBrGPlbpBUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=taFUtm8mE480vjseSQBSyzA6uxeoAGbUxK8G1-1XmRwhRb3YMaP3sugzJINwMBNvv49x_qopg9KyBkg9itGd6M7H6paOZCwa3zsc_VWWKU-8oXN9Wq0KCUIAsVDrQXmm6aY4ouIaM1l1BNF7Bi1A6AbyhNEHWyKnD6Sq7J_XviV1l-JH1jLbrLrHlSO0PAAG36D4gc5pCqZ-_k0gGtXMr-HocH3ig8OIVgJBom-2EgaSwYaUosV0tOgQjuxO-Na9XFfiYzFMjG75R79l7fuBLjekiaD_t4X8cmtbXiY0wDT4bGrJgq_Y0UuDVJQUkra6bluvkI0ircCmBrGPlbpBUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuUv6WUwGbg2dVKJt0kk9J6Y1gT8A55EOCLv39Y6rRgDHwqNUjwn5B6bP3pGrR0Y6fH-k_Q4slMKxEWKUw54mr-ukIVtjt46hr1PnvhdvpsV28I7oX4FeZaV00Nu5O9sY-Hs4mgppxJ8h7dNLVb-v_v4L8XLaDdhfgNQOoxZOzlAsWc7JtVPyNwlnMy0GqYht2vEShDOO1O6rLM7qCLnk-o2pCj5GSgATKbCpdHnvBEl2IUVeGIzaRdRT7rQcnQwfleBNKqYWnEI8KpWF9BZg8kyq0N8cxWd_2XTfSZlHFwStDtqGX9LAtYJt3esceFT8ReNNcIkmAJrscr_8GzCqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQuyowTWNwEoO0z0f0VONGqVYGHEfqO5DEyckHd6x0FlMej5TW5tXovfbQEV5-cncb0DSv-EmHuDdN-UNztlKliNiTF-ZECY6SXjHw0Z2qabFeqqswIiC2U5JSZKLfgcjk4znutmJmVd1YcsV0-QfyGRZN9uqOFHBW0giQs9sFrWoIujgEFgvhsxCvjMhsUqWoFCyhzNqpBrd6RVjARmreXO0FcoCD8zeM5r0N8aDNhoNytNOKVaPMxf-arnuFjd_kcX6_qSSDHaxuz4McoI-tGrzynovx9TkVgpmDvseuEqz3dd8yK-K1dyxMuGr6Oqb_KCCwtXulOkpJj8Ui1VrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzOlB2WqLSyq70lrfpi8uRpkOB-c1-740ybZAmSkX3LROQl0QLQV_dMCUpgNpP05rD_QB9VUBsZ5r4oH4oTDxkza7oTCA83GEfjeYw1gCUV1hAeq9S05F2yW4KeWyDLoOGbowkfLbKF1N-svl0fvBhTkautFwyZKp4PfbXZ0xMYa2mSS-tnKe5yjhxpZdBw3RTkruRtlDZJG_Sg6Hye38M-Rr4wwHxivN0skJgdxUhueaeUyoQRdbpGdj9_CfI_qyvwtNQMfN7d_U9TX7soG9iJA8c_lnL6WE-r8YCGsOY0tN3mZEu8xSLA2TJxrVYm3M49VkiVfChW6qqote1AYow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eS9kXrrB6dDSvQtc9ZZe0_H6BOb5SmT5fpY5KhKhmAlpNLCiEhZyitIayJmcI92826blCstpzQ_KkHLVYCDoPWGXLw5bUZ3W8S-jLrwnn4m5V81LH0DgoEcunhzOs1BmAOq9Owtw6jawmOLshOstcQ0GXr9Mcb8MbssmY0Feais1X-Z1hCNi9ayce_F9qM8y5-7D9yxo7Cs1hvErThWsdllY-PfyBfxR-0JqIGZCDKt_o7pNbMHixYGv9IvKEe6OxKzuvEDK-1HH1JID6n5NqwfxrZj4vij0vptlGsq-z0qorPPgThqj-eJweL89sOijj4lr_mxsi-QOeBvGx5O2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_rF0qMcaE_4wZUBw7Q5U4kPtHOem-dgU1y4uCMT6fnfPVT6Nug3P9rAbvirr9kKcKK5mjgk5ecXx3dj0DgQASItPWfYJ2aEkPi6may6htvE9RGd9XBEZ_08L3tp6ymlJBMGKdrjLlw5u8riufBgauKPOHDnuL0XPUuputTiAKN1g4Wpf5TBQq-n_tjUgBvDoBSoT6mYl5tdOBbDuG20lSFV6E-td4USkIlG5eN-wb8u_3aL9sXCdqQReUXdSjhO-yhanHw8n66UX5M8Q517fqD8ZtTSuJaITRSj0q4srwJBbeeg2zsIJqUe9-Be3_Fj4vbtOk_BVI6Tq7gmyhJj5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJ7xxHxHECNt1fnofpIklCqQ-HYRjRaHjEyh0d2v1spIN2ysEqe9Z49ast5_maViIliI2fwbjtXnVcJ0S-Qe-jiNWdsUdpqLrpcQh-BU-p6d6nqHOjGQ7OpmehV6Ikflg2ilvVpiEuowwW0XJnVT-XiJSkjpfG2l0AIrKz3TkMqP_jYCef0Pq26mBtvafF2OAIESTDEAD5luXw_7g4ypK14OruCjaq3LME7udcJv8B1IjFAkTuFHktZ3T3ZBon4alP98PQQQaoELypyoocXK5PfNKj7FPGzJ8EMxXPLRLrOwSxLb2LPivkXreDzhJVC9s2BtjuQ_cRU_jytPyr7DtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=NwsKof-P0FCsPHPqGd-GveZRkFD19_ZUVkyeXCBONi5pi4c8ZqJXskkvUt_kzZEbT349YdMRSBYxp0oSk5gLg0V3Ow9x8zVr4NftDWO1q20LjbLzjPUaVb3y7WiIsy8x_S66hPds6YDbyDareHY2Q4SQKVcGpEs-97tWHvn9AtV2TQLQe221tCDm1yYMHyQ_yavPYBLv89sWWnY3fQPFqJmqVPOWqvnljwkULfQmywoJzdC8HFZlEiIVRfRja1XoMbDzkH-e1sQuS1ngePqKfS_QI52ZgDqJwc5udgFxjkFHWJeaFkyVoDlZWdk3EUPMBjipxeiMZS3ZOz2WAXpGhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=NwsKof-P0FCsPHPqGd-GveZRkFD19_ZUVkyeXCBONi5pi4c8ZqJXskkvUt_kzZEbT349YdMRSBYxp0oSk5gLg0V3Ow9x8zVr4NftDWO1q20LjbLzjPUaVb3y7WiIsy8x_S66hPds6YDbyDareHY2Q4SQKVcGpEs-97tWHvn9AtV2TQLQe221tCDm1yYMHyQ_yavPYBLv89sWWnY3fQPFqJmqVPOWqvnljwkULfQmywoJzdC8HFZlEiIVRfRja1XoMbDzkH-e1sQuS1ngePqKfS_QI52ZgDqJwc5udgFxjkFHWJeaFkyVoDlZWdk3EUPMBjipxeiMZS3ZOz2WAXpGhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0-hwcMQznFfbXDgllkchWT-2F_RcnlY3ZlU5q8NOX3qpBJwLr9TVrlbn3tpUb1Hnv8xZ5oJcNRllHGBC9wm7izFOFs6y04x2Rc4TmucTJvoprrjDno7xtzxbX5n7M3DKFPw6f_Fqc8203nbsVZDS3OkmTwggLYYK_wAj-zOPoKEd7djBcM9MfXOxM7P6OKFBp5jTf6og_Mksq2FhSUayZxGedsAG156ye32PtpTGzebEFhwVznUWrTJM8-a6d3hDxWN5D7Bf3zUhD99qP9B-kQA2dUEj84dpuS5To-sxRIjo3--p3ewf_Kl7itXyshSE7vC9Pcx_52U5a8t0J-5Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCLTkpa0Cv4-r1bkj3rhC8AqaGwesM6qL8ekdz2p0YABHrxQVF_RiMjloUpjDYHcYjIDrxpt7dGrQUrKph55JtZ1ZpAgD9OUArzaagXYe403iJzoaLX9bbDDNQTzHlFS0P-1ubB7orjcyKgu9qcSE23Ym5WKzDeEshmKKP0rfz7-Bg3m5BSeAmaudNi7spXeCi1av1gP3xBwa0lFdcc90Rcf6dR9Qsnlu6Re3IGKuvYxV58SrlnDMZH3bz1HjrqSOl_JEAEyr_wNjIgfxkOd7_asV82q5qv9C0EyXOc7U9Ic7CbiS4w2QdteLufWWuDPCNka2lVO8ve16sMkjFUqAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJVXPxPkC5UgzW1BA6_-qD7PecSEElBcB06345KGfIzB2uahneBS2bKaYkpjAezw9OykIBxHOnl2J1XblbQ0j77aJIQd42FyGbfV2AIpEZSGzcg43kFbBLNzSywV-jKRO7JVu9Y6LbLemzCB1XDvi-O5A41Au-DLKqXob-hREadsc5qs5xHrwP05vCDCl7M_dH57WTPgxJSYVEoG4cgCbI-N3L0jfe4He_YEeJeLgg5Qmun2ilZzwJoP1hQQyPm6E6bZDf1nO3YVrEhUqrhO6SejaKOFMR9QFfjjMIZexf8862cnHTRERZq14y8HbYhKXJMBU8t6kQsKcliXyxGt1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8vivZq0KWBXiuK4Wy0B6c5whU1zAGt8OXyZAHWxIUD8YrjinbIlmg1jcybY0Ijpf8nR_gtJf16mgxThOUY3ve1tKVKD-T4giqLJC9tFWgJTKARl3EzFnAOSuS8KikKSwVFTKBlXvECXNdROZKpmF7Ff0jSD_8kTE0HsgpyF4d7cug3Hl_Rru1IlxZBBC9nZ7LKyL0IBqwk28Z2ANw1gYcqWy8o8CwYmC6aVtRVxNGedtornseWf2EryCCof04PHNeJDPbextX_hEGREOsPuiJ8rp7reQA13lMSZ5lxL0TvN-FDgZjGwF-PiJN4QH_8C3VY_yzCGR12DH52Qa-FTKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA_hGeWSfF2QJwR2le1LEL95aSVmfmvXUqvzoSeSS1HGId_NrCmbgccq3jn8EkJm5-C6vErdaoosV_qfv2dWlM18W9w1DdroFbzmK3Q026g2Q9ipviJ_hp9F-GUx1pslEAnedhooqwPMLZPEHhPlNnAdl-QKtDcwe31aKoGDQ_6qH5pZa2WCXk5zqEtQ5EonShen_YxPJu93fnYwDpB_jfrF4hULhylWsvhol0zeg1auevTkdp7v2FjpCo3zwHCvQE6VdzqNnByLvqYhbOigVOI4wuQzyWUeA92GNBWS6IyfiRsIBoMqov0go36NGhuI4vj65GFGKIOdNZLzAxwUuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvofCkbp1ZB6fuhmsZX1ny_JpY0UVn_QYq6Up9nc6mPU8xAqxr0bXVyKEvv013MTCqeuMMmBl6wKDphWX7mHvgHvW41Ph5KgHORUWzauyf4d4uOcw233B2Lne-0m0w_EAA49vbREtFLYgEJrMtAm_nUPQ8_01YFuUlGMcbJ4FtaT2l4lon2OT3OVsVy_bF3CmpFiZcWkWnzDPkPqdalmIoy3AjJZ52-WOQI9o67RNR70GOJaunYS3iVoJpOUQY3iBkjuky0w865TsamPTq0SEOQJmMsKnLeiqX7FMpJNAcUhP50rO6idiknHdrlHMGrZDhZEJV2-kHH5ggaH4T_3Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXRxMCEXo7sMiJyYs4sM0TcKMwKI0noRC_LW3gigjyTw3O4o7t9LXO6ND3cDjJglV23PHuOFrQAjSOLWKcQ2M7OPPnhpYg7b1A648mmNWSOW9O8A8WQQDCaEsO0VkMbjtE7WiaJA4afUUjbI1P1dJ2iv0omlZtA_CJKS91JOkVrllxhdVW0C3VbBqoixQUrpVHbPguxNhiC6JmTuhmwIkNDZs7yNkY8E21Lbhos_fpAJ2D4d02Iuhwk9j9iqrCmH8xALUmpKudptSPGS9lPe7ESoTBozc27rHRc1Tu2_TyUtXtX-bOv_utfW65KIRUmAUAFmB0K8YsTArq5kDvSySw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phvuq2i_j3UeyX4wZZM9lX2K0yOhi8jELJDMbEf-4oCJmI68Rbe4GfvnFghNWNbO3V1uBPXCypxYNV_mI2JT6HBbOqAekn4YgexqRveIOo-vVIHJuLCeiyVlBiHAZQVMrYbcuWwtSrtv5rfmKWZJtRHjB33cVdY_Tw0UnHHj_gplk0Vyh-huVAD4JsAIbpuW5Gb2wEPfPXXYxlGY9Nvqtk_8MDoAOlYNP9QsYsHmMWFsCN6bCsCZAFeWFgA3uS-8qQLHTTYQPq88y3MHubl74SU9Pwl9h-qIGA5X3qnCO_a48DD1scDmhzeL6uiIVj29sZeonPEXDO6SAkEEUC0vjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw6VlLgE1JIGty4irlqQuD21dTGbgP8OPcICQBxp88jp9IsX6dFHoPsvnnCxNavEuzHFbU5UPIZq_z2dwOmtcuZV6G1SAirl4PcSZ0Q8hvVIadxeQGOGc9fdPM-Hr00SnmxnFPSpt1L7EdtA7NxwfZ7KdxXNy__zgusj_wANz_2dGNryTOzalZnoJ0i8oYABUMGD9aJtGsqGRen5M6Np5D5Ns-ilmAS8UsyFddS7Nb6R0BvwsX6A4OCC1TsVvixoxrsiO5gTzP5aZ64ZwM_ZYKBZLEAoY4067qj61IhhVTt3Fsixf7SxmwVWhu-29oA05IQIGyVypJRq0fpGttib1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK3zANtakdBo7MwoemIfr70xz4MBBz6SPV3wLCqnNMiCGasg3Ag5YcrczVNzmPHQg40gYi8Wc8xx-mCC1hbI4Dp2hui88_RpppCwz-BpH1MTqUQG-w0XEzKVTWGgPj9G4OPKIZze08TFIOJ71vWZivS1sOtfRPvHrU63G64OsVPbSTlw_vIEej3i3oFYkYUJ8SMEF1XYFjZAHMfBcwCPx8UzoOA0Ain2WA-Hve13GtTJ-z1dIxH8AbIKjMaTq-GVUbOpocG1AX3W5DFH24JP6u3duYfEMLxUQKNx0mMAjed3K65ek7n4WpojGAmKIPU3gOC4kcTaHf5D48D9CVoEiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVrTrIppb-Qmn4H02lubKyGXAQLTMZdJB7nXMkP9Eqdshi0aeF-e7eXuAP0E0bMiYrJTqQPXkJoODZflri-71uW-ERdW2_xjaSNjUIdL8ITY6knql16g7xbyTnpWaVtspTKX7NZ_RA9qiAgVrnI5X60xmDeI7KiRCj4dGdtSAAOOH5PeM410k5qGY2FEUlXkUY6iVOPQHAGco_JOE2CveVxljfxTKrg3Fwf3rRbl-Kom4IIi4q6zrmX7lufchu_R3reU7EyZcPKqC_xdUiOwsbreuBu7Q7swzTqdOsPeNKPRtwLFqZEyzDeQuwcHbhacTSqRbiE5evXxjlcBP_qjiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCcbqLhbFt_7yquomMR_mWpU_Gf2Hg4xXD_axebex8VzQClK9c6i55kKpxA6RIYKjvNUyDYCaM5fDvdUUoWdODJyHcZLoFXSY6qD1Zdf-REmF-KD9ZbUqMfKKSjisfSIuNNQSb-QyaIQ1u1pDIdd-zJrfqUJmnriIsNBHzt03244-EYX7bfy55KiMkgYQLEmMEf0wowH_f8PMmY-sfozmO32B1YKUzYBFa_T5UTaU2OBKuTsaxLSlaECLyAZqHJOmW63iY0NK2SG1G-OZGzZ3iukqQGYmpSrtZajkfaEOuUDlVWJlP74TzcpjI-ov0ipXDKDOwURqPoyic_z_Cy2WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qfdt_k7A3TlCggNEb1z9aB_22j5WdRbvzHf3qWp0gaPBZS8pWWLNpnj9IPMaKBxrzvO-u1fgszWJ2QjZGoJ1nfhgyKjbr9Rqh3hpjPlaberMR6aoWJFYzel28AWJ50hbIlViJF88zg2mLFgtrKQn8qP7ilDB4QjwriAbaTeAV0yw1iQUXvhem0eI5ub76avLvKlsMRjBpWzF2zUyS1TEQj-MU0ACrFAnnBzgycEtrPtQxOyyc7PXuNM4yZmpntlDVLP0NBHpUSLy94T5Kf2FAdxiZyLA72C37Ec1VwX6IkofVV5iRlWCYK6SEvvSH5v5uYbevgE98Psa3OKaJv_dLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7Ocq2ghAm6IkEmH-x0W5LXqt_QYPSBWv3JzNw3SlscT6BBbyyu9tBBWQ3j41HFhjviJAaBz03bnf5lexGjipakKef-zAZkv_aAmvADIg5nGzTtolyChbMdudHxge_H3kKiL5L7Y7JBwozko6ysHTMfTp1f389CYJj2s_0HUL5OCK1tWSUapqgYDr_YBO8jfpacQF7TfKfqIvY-sZOMQG14lkoISwWjl54dw9kBiqQINEuFVIgqG7XAxjOo6MVWwfKJRTd4fE3qePjSxPD4Xmiqk3SUKtXz2BGsLJeG3UjziBDHKiQk2uoWmdpHAc3Q1z790CrSn8nQnZZpdvrtH7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne8ED8NituRBTFCwQbxfbi2YD3tkreGw3VqDpCOOlPNhtofUKozvbr4V-rqVCHAc3inMFcA7SV4NMdaIR8o7I5dbivnHc_miswOiGMeerdgW_akJPH5bevfSlr5R7SlJEorB4boPux6FKL_V1udtW_JRxwmdx9tQsdKVnnkgtNbw3Xl9riiqT8Qz8lrWWgRQ47T6yFsD7Lptz_RRIT_4wNvp9LuYEMK2QnIqQeku8tmh6_4P3t8OBPjmvPS0bdWYTXhEIKQrsoryQ_D2TaAnZi-rGZN5jaWMKMaPmia0J_TKQbY7dIEYfEG25Erthi4KqVCMfoPs3jv2h9A9c83DrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNgccUTsLwR4FOl08IofAaEckJIi89ALHuzONlH9DgOSVcqaNQr9f3cCkOux0K-BMvl1Otf5-EKrH1jiiaE_OPs4_HcY5ruTyxuUfftdtC5PmjoeilsFkTmLKXiq7Js0_ZAt-QbhzJfOizer3LQZ3IQW1QYMzjOBgg-YpJXrzNeNSdYH73QxEIZUMAM53OAknIw3cRUJKaoydLz2gKUJ5Ubped6SG3HpkEIULDnLys86CuAB966TbO0PkVmpqEapPjQIlGNCExRNH5o5z5JoaNVHRadJLc25C0pDeaWWwutBPPHmhxSC1Ur9IJ4p_yBXORKBHFdWw_EBBNj__ev04w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3Q-BJOyaA6zcCtRoqlcHFGNA0RCCGvNOuoCGhOi7E0q4pdauFdmTKWwWPp54mTtP8UdYnJ_aiCOCIrGto2xI6iqXGOMXGBscVf3beHvrKSsdj_r9HecAB5-352Z6X3DEPWPeVkoSonpgRaiuINoW4M1c7PMtIdTiOZYUPLOqoiAXryPSo_aHo5i0kGTzmhUGgVKOakeHmoRZGeOF3jbCS-D2s7jJgaS-JWe9N-fnz6vUe4FQ54cimXlUEV0aHTMX84ckcNrjGeibAJbZABhOXXvhebq98TZGmzmE5fV4OAdSjSaXL-e8HKeqwN59CBfF-SVnhcDlnZiH14jhQEYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaMuGDMLK5XCJiLvwsNdpC52bij3gG5Ms6nVwfU8IHlFuX29WXZwhVbROMrdKVMBHFC23gtnxoMUzyYnEEOSYmXKIKxlOKQD_FkyCnG7dv1igs-nRTcYhFhy6FPnS1ef1RP57DhvAbbgxB94Vp3u_QSDXFD4WMno75JhcMDuLrqv3gALxoja363I6p_ThcDyt_YJ19XYsirw8LpqYjX36oAVlRAR9gzEhMQtarVKTlISq0CeQJL2YZE0F-UP1FsyiOUnjG0TjZSxIfflE5gFEaTr_uzWJEmWTU7gHacyL-9X0bbCOKOqQEjdmODd-8LM8EFiafytTaVDKFDDnBxZtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKJ_bDZJ9NA1U4jZmYhkMFFGNCQsughPycHxBvvLbaLy_YMyIlIg5cn4cPIyRhpWvvrBffB9EumzEW3V8ZaIAe05ymv4nkbkPFn0J484EIt8eNLIXwOJDUV7PfFnGGrcO-JEijXmMVSIxaAG34vlBrPCX0M8Jsy1d-L8aH175dJcO4qttD6_hup-YIUMJJ-WQi2Pd740XEFLPwEMwsPSfMpq1g6r6iRW6maOLsBxHSveScyYCvTKozQlkBetDUGNGco8460WA2rjADkQfcbyVj0KG-E-Go85nIKOKQs2YJaAEy1-PfHh-bEPKrGKMGBzBQdJf7BfeCM69yZ7x_2Dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=Lv-J3VSrOfQsi8z9o68gYu2VY7SVBxFSMwCF-H7oAosgLzJSrIYXgUlLHKrou0h6PjyXx4s84oLNReBRhSBre6f3Z9oUscfEKKNKpq8BTBENbLwPn0fMm_gpa-u7DPZJb1_vqt3aTtIaTa442_nHLMUpfQ8Pxp-GP92sMPEQbOgZD1WCR6ZCkHZEo2RioWAZ1tuKJkHea3YGSRUZYxnTpUt9n0kPh5OOJ6I81dKGKQx-qTgnoiwSZX7yQSAiRF6op9Gydj4159c5v_gdPoUphNNexeP3DNV6sluoLkeu_xmcjlCGWr1QWmMVrHiGFGuLvwzzyW4mR3dY8Pbd7MEdQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=Lv-J3VSrOfQsi8z9o68gYu2VY7SVBxFSMwCF-H7oAosgLzJSrIYXgUlLHKrou0h6PjyXx4s84oLNReBRhSBre6f3Z9oUscfEKKNKpq8BTBENbLwPn0fMm_gpa-u7DPZJb1_vqt3aTtIaTa442_nHLMUpfQ8Pxp-GP92sMPEQbOgZD1WCR6ZCkHZEo2RioWAZ1tuKJkHea3YGSRUZYxnTpUt9n0kPh5OOJ6I81dKGKQx-qTgnoiwSZX7yQSAiRF6op9Gydj4159c5v_gdPoUphNNexeP3DNV6sluoLkeu_xmcjlCGWr1QWmMVrHiGFGuLvwzzyW4mR3dY8Pbd7MEdQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXIS45aRMAnc3RAoVJvWVwk9JqYQg97XM3GiE8E22yWeOrlyYASHPhwFRxiOAPdEPZ4A2Nn9Z3HWu9isTdDHZerANiUW2Dn5Sax0stnlbc3hrJhTAVPAZILEOz7Hx9SUz5-3f_QEm3HRm4sGjaEl-cLQ3IER5N0qxLMTc3GuQpbc3x_WQZJcp8bqQVku37B2kP1dUvSU-5AH4YIa5LuRBKN4GSOke8N3g83lU4SrPM0Nuts92jIoG9PY1eaosykMM-fAE8zm0E2EF5X_kob8eg6RnRJT98LQSdhmcE3MArXXwqNhPhDeWiNrC_Lqhq60H1rE--C3nBs-URb0zKkTrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uz-J5IlvGv8-obvj3P-1sawZCKMdT_53XNk5LDCRHKqhAPqdalywGZu3DjG9mWXdo_1ZYFIq5_8431AiuWFKw1vFgRrLjk9RzgsvkF40EMtggas47PozMS5a0KEYm9kkDflX3tXOAAG56SlLYuUAephgfyrvB94bX_uKxBYhc7fpacqtC-_zrL1nayzP5Q61JItSok2hYWIp8lR2zaSMlFaNfFVtMrfyGS5W4K9WDmFazD5u2XMH2JQvgPmjTnK4pd3RQhrj4Y2Vfc5W5CTen8frN8gtPhdDdqUBlv_r2_WU6AtEaHMgCOTYNgeiuv9Qqvlsrjilt9fMicT3Dx9mxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=kdC_tsTjKIf9UKqFno3WfggpFY01lpw5jvRNR1L5dAqgTQa8VrF99jBbflo0nqBsxhf16CY3shv4voa5KaHSaAlBkT4U3FWc6hTe5EbaiEKaIKCnx5xvufUSd-n4am6-ktUGNj5hnMpJttS9XKbtoeGu_a7T-br3rO1asgmv4PW42VTpzdV4rTt3hDdHH-UjYjxXriHQ5yWSLmUYACxljMtj6GIwHGhmirxdYEWmBtIjx8xaWIPFc8JkIPV5RYw0lYRzThIUgLMfO_Zr4Cd1oA8Q8loktGi0yIZcBfmFPZR9TStqYCb950wMz9LRD-99FOF5o29HeK7MAIwkHopJ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=kdC_tsTjKIf9UKqFno3WfggpFY01lpw5jvRNR1L5dAqgTQa8VrF99jBbflo0nqBsxhf16CY3shv4voa5KaHSaAlBkT4U3FWc6hTe5EbaiEKaIKCnx5xvufUSd-n4am6-ktUGNj5hnMpJttS9XKbtoeGu_a7T-br3rO1asgmv4PW42VTpzdV4rTt3hDdHH-UjYjxXriHQ5yWSLmUYACxljMtj6GIwHGhmirxdYEWmBtIjx8xaWIPFc8JkIPV5RYw0lYRzThIUgLMfO_Zr4Cd1oA8Q8loktGi0yIZcBfmFPZR9TStqYCb950wMz9LRD-99FOF5o29HeK7MAIwkHopJ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=rD8Rkwec6_SiBWesbRhZ08ez2TXrq6s1ItQXHL4DWjA1aEgilZp3Zgi5hYHwGS-Bf18nd7dcOZFSoGN4PmS22SHjUl4RTG04IZoTygaHDkijrKnutxNAs_LsMb0su84tcuDu_NX3QnsgQcLbHyXrN2WvFVaoQLOMKWgWIUNRRKxHMFCcDLr5-zoGJ6k51drnGrd8GC0yPAQydvCo-daLS7HB-Gq1CchMHpqfcADMH7BsO7m-aMqMKivIbyrO1SSp4CAsQRKaAxDIB20fl1AyOY97K-7E1x0Rv5gQcZe8qcIJQCrF-ALwxwSGtqo61_KNHlXr2S1Ub0od4WT2kZHfsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=rD8Rkwec6_SiBWesbRhZ08ez2TXrq6s1ItQXHL4DWjA1aEgilZp3Zgi5hYHwGS-Bf18nd7dcOZFSoGN4PmS22SHjUl4RTG04IZoTygaHDkijrKnutxNAs_LsMb0su84tcuDu_NX3QnsgQcLbHyXrN2WvFVaoQLOMKWgWIUNRRKxHMFCcDLr5-zoGJ6k51drnGrd8GC0yPAQydvCo-daLS7HB-Gq1CchMHpqfcADMH7BsO7m-aMqMKivIbyrO1SSp4CAsQRKaAxDIB20fl1AyOY97K-7E1x0Rv5gQcZe8qcIJQCrF-ALwxwSGtqo61_KNHlXr2S1Ub0od4WT2kZHfsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=I0laZ3cc24fLPj1yUjuuO6HkVvJwyCrLjuaJsjiWm4JlcLzBdrNp2wXiDgDPQnpfTeyrfsYxEgcD-Pk-ARyeR8bZzOKRgDXxhlBrsJ0crN7TWFfYnnQI5w2gnZ7Bq4RFiL7GQXgnJtH7zW0V9dsOLu_TTxIly8btDyhPSsrhf6pnUMASlhXTfLO_1RNrqJ9WV60UVCI3nZrbQyIggV1tjlKkrWL3r1w6qwtzY2H2nVHk6OwXcIySkcvrQhqaFm1K2S-GbrpePMtweRjGTI2oVu98lhEn_ZnvJsfOQ06luFncL3UGlQrQdFKUzdz8PSx7FJ5QtvDODORz_brMO-MW2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=I0laZ3cc24fLPj1yUjuuO6HkVvJwyCrLjuaJsjiWm4JlcLzBdrNp2wXiDgDPQnpfTeyrfsYxEgcD-Pk-ARyeR8bZzOKRgDXxhlBrsJ0crN7TWFfYnnQI5w2gnZ7Bq4RFiL7GQXgnJtH7zW0V9dsOLu_TTxIly8btDyhPSsrhf6pnUMASlhXTfLO_1RNrqJ9WV60UVCI3nZrbQyIggV1tjlKkrWL3r1w6qwtzY2H2nVHk6OwXcIySkcvrQhqaFm1K2S-GbrpePMtweRjGTI2oVu98lhEn_ZnvJsfOQ06luFncL3UGlQrQdFKUzdz8PSx7FJ5QtvDODORz_brMO-MW2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIuj_QKtrTg5lejl1savMs56x_Lt9TeEJmNmYFDtnEEHIJhuXZ37MM9YBh1DZBk_FU0ApsTBGKngpEMW1JRWvD3Z9-_JhFqbcxdVpBbeo9IxVLkq3G8hrM9Uazt4tqFrCBZTodv1L42YPeEcKsLPdEdbXLscOCAEZDEMRKKo-6RFMw7EeXyha56B9sw2uznv4Z4jl9CMc9eZ497KlbTzUdN8mcS52Mzk3dAYB7IoFFtByL7fn5rMT-mOC9maE3r-a0EQCvCSNgCQAi8Gs86lptmSzP9qB-Z6pbSiVtObCTfQKMS8qciZlKMb6uzbEGuyEd0TzU7B5nh-8xCXJXRX7w.jpg" alt="photo" loading="lazy"/></div>
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
