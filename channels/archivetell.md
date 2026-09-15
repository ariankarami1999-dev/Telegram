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
<img src="https://cdn4.telesco.pe/file/l6CZm4Ux9hx7PQIFTr-k2AyYKQ-vbWgpfswCUHUKmBymnYgbgpefuSvmRuLLFqED-BcxU94hZMGqNn8kUyV48Cu_k0nKlV-MjvU_P4DCmr4_8ZAJ7GIuKNlzVuO6vwuoFsxZr5wM5On1JKV4iVD6fEMH3YzsvD0AJN8JmZytsgI3r9uNTetJ3CDMC0oGGVMXOYV48oW_xWWRsMTFW0zXQPY8xlhmdWiMj3fnLvFbp_vP1I6GqP41jMqlbKH47tvUNWWiplfQh0Yr1rsap6E8lnXKUYe0hCaeYA06P9lGZ8CP-BfuoBQLf4JcLx_k-d3n--it_Ui3lJQIgA_HgV9wPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 15:26:15</div>
<hr>

<div class="tg-post" id="msg-7750">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانفیگ مخصوص چنل -
سرعت خداا
vless://e4b11ac9-46f7-4cc0-92ed-bb9dfaaf3600@94.237.92.65:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=lkMM9FR-o7Z6NwmmQVK8rLhCQR1mbJTgjY_0upeS2SY&security=reality&sid=0436301fb0178b&sni=google.com&spx=%2F442987454d44398&type=tcp#@ArchiveTell
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/ArchiveTell/7750" target="_blank">📅 11:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lVx-lPYiQtz7qpwR9KqCrMBn3DZN7XL4rFe17b1r_Q4c54J_VocDFNjAhr2ZOXd8EARj1IcRdG2ZTaAHQpgx4R8uWTOKP2iKAgz7AmcoY1tuMT6fJox0kHbmRqoOM3uIN01WUhexDWE7KZJ_UGWDpZSu7E2kbfVPV58bxROKdDVCmCaECHf2M0G_i9khJjN5nc_TCZUXc1C94OpG3I1kRHpkY0ige2F-uUzR3C2W-7edTj51BMmxoX2ysS7jPgltMo9LX0nwXjpVRJ4jcg7oc3Ylefe1KCKw3PTBxax52ksYwVaIpa5takVMlFeoscyJJMN6i6HyE9Phsal1mFwVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
از تاریخ ۱۴ تا ۱۶ سپتامبر، با ورود به
Z.ai
؛ ۶۰۰ میلیون توکن GLM-5.3 به شما تعلق می‌گیرد، بدون نیاز به اشتراک.
🔗
https://autoclaw.z.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7747">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaBFy_6aYmzZJzneZmEDXORfymB3R-6CUF9-ZsgOWXv_2bSv87xcNuQ4wR34jhq6SY3fpxLdOikp5zNJyeSMvD1I_LWpsRgCx8FhWO6_Do2ED6w99PP8uM1pxO9G9fxmLuI5L5cHB06j_jftPRa-zRQa7YD9iDbFXHGsLzsWQZaMsl_uV8a_5MiD1AZz977y43PfOnXB3uGmhRqcb4Uhflb5UlkbdyBXU2AyzYXG10xN4IKORM9gHVerOQfoR6P7dFS-EgaPkbcFqHrOuiaVkp_Jt6Uh5hEk-AOf595yVnr_X4t78M2uqFxBbP2mN8wnW9rZNQ_P_bmYm1WZYXVN9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rk3VyAt_mlvh9RPn9h2c8Ajm2YkBXp-bFtV7U3OQj6Mpt74pXrhgvC25KRPITyuz2d53E05vH43bK5sy23HyIGo6iAjz2Oq2SxfUthqrNx3y8s4iNatXk16s0G1fRHoWrri4B1zlz-J04WO4MUmA6LRfkZARWtP0M7nmP3hD3M6c0mmOaFipDEzY0PNcwDyBlhAynUb1UgQKtZnM2vKu2wJYEpP-MAjqmfrEo0I2pnmug2A4XQRF7wmwEorWf-Gdh7e3Xy5t2HMndvPt_lifIFgWA8Yo61cRq9OiLRw5hCjwmuUoG-HU47ZIJq6855dJnkSCzTi-fpNP5J7XWeZ1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6agoWhm-yfF8kKuBFHia72PO3Ynfkj39qTMp-xi3-yngr866CWjfkoOTVxyQINnjmWIOrPMeNkeDUL8IRSuSGf8qXKRg3rfzir0iZvggEBGhwql7KzKCnPXmDDlBXsXgXarYDtOAeEU6H1k-YS_9has0iDjmg2QpVyl5KHFu-F5zYVqbV1s4RdR0y8Zjw2m9XEa4ckV-8LojeFwBrk0rAG1PNsDXctmHh4PPP6AcN-Izv6ZN2pHpq3WVofQl4_UNK9DQvc-aRl3XIcMgut2S-W6jIdswl_EEbqiV59s6v1OhE8Ky1x07Ntm8pIfnCa2iWmRO85XoTlzvKTvr8TbSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrupLcIL_HOIcRPcoGXxHw54sjUyIpxDRrMx-LAEj5IfPVuFchZdDOBVvyglEU34MZAKQrdgcrMeK4e3-7R274FrtZw8dFeOqj3OAFTEYo4-7qz_8gR0SRuQfCI92BbVyydr6qClMVp5ZS8ylQ5oK3BArV1QmXzWY8stZa9ll1OUlQVxavTvytxsf2nMnqo2-1jkbn29gOzHFrKyP_37yP6qorr9A5ZC5YFnYVO-7JqKsa8HssRm7_L3qG_umudEkc0eNSiU8qOX6r8Ci2lH7Lljcw6gsGd8N0JIM8t-VAJFUq6HLZsTYoUJfe4ZzqYyndhqDt1qyy9BeCCL4lN2uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyj8WRbDFGrl8c8cU1s3zMEgQP7aSpW64zqmuYAYz4BnV7yeyk9NA4UBGSKcfEj2VerASLcfrnArSZYh1Rhzcc5Ndo9X5CJcuPhcCSxFAU833bNL9A9_zgQx_5gObDO0wd9QIuTIOlLSDhCc-WZfuephN00czCsrIFS6rZ6IbEQazQxK7Vk6YmXmeo4vLMviq0OrRotL7YQgM3h95VopboTpvovKfYzHVba-v4z6F0ehOywFOis6L5hfjNzqOeDxh5NsM4zbApvrPF56HZh3Xwh7xi2KPQNUzvtQJaE7kXu25uzL3AExKk3n6NzfYBWHsYEK9XAIYiITtr1t268JYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BPEFYAPBTsRDb8LHVErUYcbQnT-XgdYjw1IHcPFRvniVls2QU-xCyvMKoYBTgigavfjBw07jJKJm2NzBjXcXn0QqS3GeRMuZT4NMDmt15Gyihy34bOu_v4F0UhjmLeRWSKm3AVTGPpCCxqkAKYpC1Y2CiCjmOb-bhSufg4ZFiIB5m2WxD4BWGKnqX7CJE-hm9CZ1JEa0xKH-U415BMBW-RmA0raOqexSrB5IefZ-_tCIu5QyjCQsUj7BbzMxGZJCXVNKtuBd0zWFzWi1G9pNHXTp6n8bAFWhtmuCfzri2lhQeN9CQvFlpiFT_2L5PQxHbEEABUOZmEAHz9DYXpi-Og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9W-jquDCXzAu8xSo2l10NpcuFw89C5CYl53hG7s9ELrF6NfZxXCd9e_ZN7JPdFIRsib3ub8qyxQvCJEXynXrpUK7g-ns6wwlgRfU153dUmoGjc2mkibnL0TrbWW_k-aPZl650_RhmUVMV7c81nKYwLEQXQzDTUXgbGBBCwfKmKGCnNr5J7VWE1lsLd0yrP8Pix7LUdc9edsPX6zmiwq4SdUpUvzets_Y0avuva_Xj2zGefgqgRdRPjTFX0TgZ3atPPSjq2IA8OCa7rKsCgaxisvgEs8lL3WDCnugMJLa2mdvtDJuVF6iJ1NpTj5HeWXjx5Rac7flOretRBCFA4jKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6axW3r3JSv-CA5HQ9iOTP_BXU64rxiOflNmlHOqEXZT1ZqXrpQbLAzC-eB8-_hiDQMl6fc4J2cKK4UhuMsoUZPJcha4D6mCz9knX3_AKe7E6m32z2HPT3wuvhUMz9tbYiRDdvTgObMCp2zQHvLUfeBms-VeEK4EuWw0cZVjsTAAMObliTQWkym-wp9eKJEvyEOzQr1qv37bfPk1lYxFBNZsRfd5xDkTAAg-FLSKZn_P8m-UHNoBx0kh75wimRGWBkNttWS5-xCkCcSxtSc-ITZ-BSEbd8AJq8-xy5BIoeZPvUGjLdYEbaQxoA5TZ4IrnxPfDeah4UBj9juF0cWDdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mzq2A0RrITul-QzaE8hazgQZWP7PmEifMHA9R49oOZuOD8blQnhRCakc2NqMTXpGQNiBjMXOCwtNrTQDuxqhKocw1_M5prjUzO5bcec-DgxKrgW5UzibMMGrFCuypGiMYO_GvayIj1hkaLJTLjkav37NwXdA6C-LSYQYlenbj9kgp2wieD3XXT_Yqv3yxdtK0YWKW6YUwet6q1McN-ixdgoZ5oiKB94LHnCoBiBsrwSolilCRAuXh8RUPgv31TyYq94IFiJRUb_zQ8Ksi7CrgrlP2TiXO3iex_X6izzIVjbvTsxTmq3PUXWbiY668Gre8YHCcIv-FrpXcwnMu0tW0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McKER5gFvbPwLduPBYFLL7IN0v27N58mtJmLkFy1GTopcAU64erKjFEiFSwOexlNUW4kURtTJ-QtTsk7HJszj65q3jDIkvPhrITTI-eaI6iUmfjicwQ_Swl2yP4AQnb7ltlW5aApIv-Gf4VyFUl0GsNrE2JTAE7FDTCto0hOcPo5qJbIOBediSyefjLC-GlYg5AbxuJp4PT-oRt2Tu0VmaB9FTgXy-1vNEeT4avMv74IkgsgsmHpOABGlqUjQiKT3BZXKjxtvzOFgaf-wInNNVwq5QEq2loNWSPq10ArZYcMrL6poob5SLftfP8Nt9PvHyAWweQ5qyge4p_Ia1j-QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHqLJsQRtQ0FRYYvqVlJpou15fapwBYqr7RhwATGd4qNyG9b_DrJBf6YsJXfm73djNGs1uCnYFbm0rHg9GcR6ObIUtU_XT6D0BoYcPoglyfFNatsoi6107UEpYgrUzthHyS2kI5iYdUbiu-MLNx19D8P7F4h4Zwdwi_xIWriMS_CPF7dfQB02HgkUjfYt9jP9hpS_DptE7CfwpQ4L4ffGiw7otNni69IVl4P7Hj2FvMCHUfMRAs1B1a7OK85In2k8hGhxzOSVxlBXq5aOwG1BVJHJpD9ILKlyjvsoOmhvFGIx7YF5a-VYj0RQQu3o2Qq0C392O3LvHV2RlNKX1fkJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLR9YmYeEV4xlypE4jXepjVUNWr3hOohpy-XI68251X3etzf2FFJSRnEYFHfwBThBDlhxVna5yEXrGtIzgKJSgXKFyFMiRaa14GsY0B-WsYm4LUa7gIbbIQh9bkrMIS5F5VxaLQhch-o8dgVUIwJkO49ivwYq2p4VSfxlWmgfUGZdsUuWyCMwxOg2XP1_6HFZAVxGL3TKrr7Eug1MAtHB0HntUi249ycXYH1TIUIcU7ZN1eA6Fmlae7xDWTw2Aqg5vMLyftsZUHcMwd4W_5sfgCvKNkpM-8tbs95V-_RA154HMO4HY_sZLEVOh1AGa5EtTnSxKGFLYOoPC2b_YHxHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URfyYudnlRp-teTz4mctTPRz6NM5HuRC6wXg8_fwVR4-KbAXSOqFWqSNfz-CLXEqD5XMJ87e__hFDdRMDLvXtzOkbNdLnycBYayTlniX_7FmiAUiW2qMsyi10_qCueFLSrcnc2oxgB2bOQsst0QF91qyk7nKMGIRpsuW-RPTifichVWJOtakfbYnBq_p-LWgNS7H1ZatXf2brpeQ5eOlm3yYTM2i-q7Y-W2tV06zInTW5Gs7As7HgyO5vn403g-P-SnarPsFMk49NQQJf9lfhdyLhgF9lMljX48WM2DHve-cUe1xUqp9Ym3n-eOnyWJrZSigYKrQYiePbU_47uKkwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RspH6nTPXsYvBAcUFiP43dTvA5fLnfOdHuxfuOTfhY59lyYxghdDurwiUpytTW_fY-FrVQZAKXxl6SK7WlDUn-tTz0G9GR6K8raECzXPWzm7-IOzSOJc2WQGy9Mrlvnd8hV3QyRLoB5wHlzPO-GMEBZwdi_rgVsemv8YI_Vxg93WQF72zBJJYdJswyMNF_7x1Z3nrQ32HhUFJYhXQ35gtpKkzi1SHk1eKmSmWAP4eM2ZW4e04XP4Pu_3ldKUBDfyI4rnK7auPCg9t-fx6sL6liqd9JDPyg2Sj0GCQyA4MKoQb2ndJUdgM3yUgsulVwP_R0R4bHeA3__IgODbkJi3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGqyxUV9AWgmI8yJRDn6MnA9RkdR2H2k2Vl42CvLOTQ7tUE54PUBODDsHciIWK_QXwOUMWu6cGXgP5LD_jSR5mQpDjS8flFbuWzEXlHve4UzegXHnAuAMvPEwWYWM8ip5YzzrU_oU2k527_4hOhC7vAaINxHACblnisuK6v4oHZKX-zldfrWvyv0B0pA5nzv1TW9aELud4Cf5acLDE9tToxDRdc78E-wRJD1LOwCy6BhxZmNjOohy-IzRxH4F8kJqeUB1CCRFQa9VzwjKxmc4dofXmDfXMiH03zLkDYDnwK6x0dMcgpR6I4YSwx0uRQQYjxqe668SOPjR5Y8zFkhzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaFGHhgppYpTanZ32ZtjLrqOI15JsnxpQEqyCdUX9nB-DYP-lJw3MqwKrGUWFlW4koE3qd4jbPAyQR8kCNVVSZGUV39HPdmNu8-ofdnzHe7TOfE25l1MAmRlXnOYfFLX-OY0bulVDoyoSkWar4EQ-2bS3TOmVEiG4dJlynOIULf64pbkg-h_5vhh83Jb2lP82i3IygPDxe_xU5tEVM0ARJOKNNvbjR6jVUpj6W6Bd8LF27SOpRNRqRccaXpDioWpn89v9kDs8w15MUBSCIE6SMWenmILGaI5RbXGuU_8o7ox4-hatu3XYw6YE6uIPov0pjyclKZWRtkmWf_ojvQm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpSlpsE7h8gJiSlw4KKlBhj2HgTKuyHVwhm6ax2Zdbw1mVjkjKpmFLXIqv48DUZXyXFlPs4tvUslQdLJ5PJHeX--1yw1TGZwpbZRaEdtiSsHBEyHn-2ndjsy9G4TlwL3SVexSt9cGsS1APboZx3NvsC1JIUsMATpb0sOTugI2CBOVGDdGCBlyGbV1ZswpVo1wd6_TH2c1FifAuAnspC1iJhhuiFwx62MyvT-15dS2ADI3iIZkih8sRHj0WrEZb9XassbM37-Ukyu7rf0iIrK3mx947GxGE2VqSKDdHk3cw5_lrcPcWjGsZqtDC45DgUohIObdUqO8ORCqpkAroGByw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bo1gebTZE_JR6PbHaOq18Ak5Rq3PbTrntrbS7uCrpY9U6FpMvoFzy2Oh-P1KfqW0mKdSNQVSFe_s3wpo3ObrErkkGkiDh5YBa3zg6ycBKZKb6bw2RyNv6NM1NOQnvhcSL_K6bKZJGMVF3k2YQgANTgIZ6aW5gNwvOJJsnRcmfcalWYgH9RF29EwYqKNBk_c79pfK91A61GerBrpX2CvWOpG_wQG6zYc003FAZBeKJCtIQMA1s5QGWDz3WIfcNhgcIpUVwdU5TQjZctTzBqe6D0a5aV8_GqIps_C5mty9P6xBjY5oy5d9GMFGygja5tff_jq_A9V2r394dabZmWhPnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3Rj23WCPT_WT09BSRCN70MUVkf3LnYb7nAFGIuRoM51EcLpOl359D01Olpv2MgLM77-q00CIeGaLmvT1DxjikwA8MiOtSVT4igdgXPYiI4kpCkASI8HdZsgT6Ny3RY0oimabZ6bvH2XnTERGpmt3HawUGHvth3-4Udi6HY2sw_18P9VpCO19QNFXxmhG3Y0xPF1YnnlvRrQPyGQuNcI7iJRnJRRrszWPPOenZKnjrY1u-5XbCseZ0vSDLndXDHY7P5s93xa811DlDA2jdcLqVxDZ4-Sbss6rysw7jRgNJBiFP3wCgf793dIJ7KcC5oDxoECHZc2cGuSgDpghfBXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=I_HtivanW88kC4Hy1JTK_wbiiFcebH2oJoYIQrKq4Hdb-8ncJPKp4WreegMBKzzJE3tp37E4hn_F2-MoxSsB-9SzZy5OpKvsATYwNifl7l26-74b66YN6AWAg0YHOsrkZvGPAU6JwYJ_gOJL_432isCl6RFVcD4cWn811LMrlOL9O3ecWqIn3LUZLBYrRYWdbk7kyVEk5_O0RsfsN0i9_MULUqGK6MGeblD8TUh9QUEV7m413GQe0fNTVPj2Oq36m-TntZ_EVvF2rLh3D3v7Pz4nYIjRQwV4XCfWh6vH_VnyzF0KYA-C-f_xIKaaGkY6J0_gc0DcRGCGUNB_FQvC8aQY5Ex_AdIwcgqEt2LwL_-Ha6sjsue0NsqodwppISpLd8Si4kEoJSiPdB-8SEzsR2kADGH-dqLD5IksqGk_vrXXltJlua88vX-elWJmlWWS_dNgHgk3_ToK4WlfqzNB8xXFhjLkzjTXTT1zdlVgW4IKDnW1bKoD9bFZSOoLpUUMpVLKJ4G8EIZvVb4BdbrDpqlpcxuI_PTI5_jUKKz5YuSCGrzb249v2Ju2y7biP73jdH03QFzB3gbHg_xfE_3-Pn_jmSDrCnyrqwLwmOAFL9PC-HOAyLcrdKvW1tlbmeyXi1nrb0zyY9yZO-RixbVyNGtHnstor7QUli5eu_R8NlY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=I_HtivanW88kC4Hy1JTK_wbiiFcebH2oJoYIQrKq4Hdb-8ncJPKp4WreegMBKzzJE3tp37E4hn_F2-MoxSsB-9SzZy5OpKvsATYwNifl7l26-74b66YN6AWAg0YHOsrkZvGPAU6JwYJ_gOJL_432isCl6RFVcD4cWn811LMrlOL9O3ecWqIn3LUZLBYrRYWdbk7kyVEk5_O0RsfsN0i9_MULUqGK6MGeblD8TUh9QUEV7m413GQe0fNTVPj2Oq36m-TntZ_EVvF2rLh3D3v7Pz4nYIjRQwV4XCfWh6vH_VnyzF0KYA-C-f_xIKaaGkY6J0_gc0DcRGCGUNB_FQvC8aQY5Ex_AdIwcgqEt2LwL_-Ha6sjsue0NsqodwppISpLd8Si4kEoJSiPdB-8SEzsR2kADGH-dqLD5IksqGk_vrXXltJlua88vX-elWJmlWWS_dNgHgk3_ToK4WlfqzNB8xXFhjLkzjTXTT1zdlVgW4IKDnW1bKoD9bFZSOoLpUUMpVLKJ4G8EIZvVb4BdbrDpqlpcxuI_PTI5_jUKKz5YuSCGrzb249v2Ju2y7biP73jdH03QFzB3gbHg_xfE_3-Pn_jmSDrCnyrqwLwmOAFL9PC-HOAyLcrdKvW1tlbmeyXi1nrb0zyY9yZO-RixbVyNGtHnstor7QUli5eu_R8NlY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=RpmmJE4z2oaYUquY2VMj6VBH7Mwy2-hgpeWqXjjybsNDHSzhJ2iAo7_rDZytea5HPpUGxdpvLoZ-uQOLHNEYRPc3FTJoFGfXyP7zMRoh1GJYADAlRlP9QQUHk7h7mj4u33CmiMGGpsCNaO7M0-yVknG9y5uY55EHb4U9QpWl4Fe2P5Rr_8GtPsfX8iC-K5-pO5pjI8VqRBmMJmUDFYAEUH4KBLoqKkbCJbmX91k3t_C6BOx3cA2fs7TAz8KNtie8dPIKW6aPn8yva8vaL5zzTpfeXeAkImCcV26ZB8jWz26PurRnFuPW54B0J8J8ijKxhtizbCXuUA2glw3ov2y0mmxQkK22_WEn-3JHH71JNUAFVvNBiLG4TchscLOflbWa-fTnAXgY34bO_vM2Y9hzZmgB-cnScapDXY5Q2EbHXnMi5UnZz1EVthmVfMPsh_AILgV951mOsKi6NY-WE_EwdWiswmi3wezoVzs6Z4I0bAIV913k7V8v-Mwxa9OfCf8i27Eg5RO2YEwqbbILtP0aDyZ5AVfbyrbO0148FQHi8bm2cz1ozS1zFV9vztvOaKtkWMM6Bu1qDOrpAaeUXWZq5TtQdFVENmCpTZBvwgc7tVm0ie5FR207HCyepCl1Co0nd7rL7xldmOU0o5ARKviIBiefcKEINtFYy7i0okmExjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=RpmmJE4z2oaYUquY2VMj6VBH7Mwy2-hgpeWqXjjybsNDHSzhJ2iAo7_rDZytea5HPpUGxdpvLoZ-uQOLHNEYRPc3FTJoFGfXyP7zMRoh1GJYADAlRlP9QQUHk7h7mj4u33CmiMGGpsCNaO7M0-yVknG9y5uY55EHb4U9QpWl4Fe2P5Rr_8GtPsfX8iC-K5-pO5pjI8VqRBmMJmUDFYAEUH4KBLoqKkbCJbmX91k3t_C6BOx3cA2fs7TAz8KNtie8dPIKW6aPn8yva8vaL5zzTpfeXeAkImCcV26ZB8jWz26PurRnFuPW54B0J8J8ijKxhtizbCXuUA2glw3ov2y0mmxQkK22_WEn-3JHH71JNUAFVvNBiLG4TchscLOflbWa-fTnAXgY34bO_vM2Y9hzZmgB-cnScapDXY5Q2EbHXnMi5UnZz1EVthmVfMPsh_AILgV951mOsKi6NY-WE_EwdWiswmi3wezoVzs6Z4I0bAIV913k7V8v-Mwxa9OfCf8i27Eg5RO2YEwqbbILtP0aDyZ5AVfbyrbO0148FQHi8bm2cz1ozS1zFV9vztvOaKtkWMM6Bu1qDOrpAaeUXWZq5TtQdFVENmCpTZBvwgc7tVm0ie5FR207HCyepCl1Co0nd7rL7xldmOU0o5ARKviIBiefcKEINtFYy7i0okmExjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBXRUkqXhgISX6caePqZb5JejEE7kmyK0N8rBOZgtauYNa899Nepf1AbdTI2PwggN_1lnxGZViK14xZN7iz-OwGjgQeLVB9Swcgq26jA6ivYfB6bUQ0EzPKD_8egFu0lG9H7Y89CqECrJlV2sH-2P4JT1zvACbED7wkaUphfyFeSU5FupGxk3If4WjWPNkZa7CZH6CtEMjo3AzxEE-hwnOuGn1rA-nCT8rX8eHMJLLBUvZOJaBUXN6LhcMreQ23HBB6T0ZscKxD5A1wrFaJ0_z5gDra9SgOFL5Q9QDqayChuuHBZGGtEU_3hXB6RQRBC_GTJ54a7Z3JzFc2rdnSaAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=h-FK_iHu44S1Q7_ROabQ1cW94WIay5qI59dPyz1txWBrn9WAMe1bJAJNmb2F6iqj177Kezo58P98tEC0CIZp6jQPreZOLDuQQTvUsnA26fjUUUEp2Z50QjlstIvO7NHjz5HyT80wWsnGsmB-p4hVa9m-L4MZGLfzazPiU49k1w1uxw6vLQaOEz5ATj9vK2IDI5m-rqeyKNypImcJm62J3VPU8nNDqzLeGcpKAy79ys4lngg4Tp7l17wmU9QZxzkGGVq4Th6t-xQljDhr2_bR7LkRemeR-n89nnC4mOuBNBv4PZFxfmnyc8l4SItCZ4_DFVHGGFtDfXr0ue-pAW7Nyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=h-FK_iHu44S1Q7_ROabQ1cW94WIay5qI59dPyz1txWBrn9WAMe1bJAJNmb2F6iqj177Kezo58P98tEC0CIZp6jQPreZOLDuQQTvUsnA26fjUUUEp2Z50QjlstIvO7NHjz5HyT80wWsnGsmB-p4hVa9m-L4MZGLfzazPiU49k1w1uxw6vLQaOEz5ATj9vK2IDI5m-rqeyKNypImcJm62J3VPU8nNDqzLeGcpKAy79ys4lngg4Tp7l17wmU9QZxzkGGVq4Th6t-xQljDhr2_bR7LkRemeR-n89nnC4mOuBNBv4PZFxfmnyc8l4SItCZ4_DFVHGGFtDfXr0ue-pAW7Nyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LraCMce7iUFPwASv5Uox16CWArs-r1xsqK_rvmYhlpazkr5Ig_4GLOWofUUYsK2VDgg93j61rnOLLd2x0UqhHChCLjw8zFBjHtip3MYsqeRvAQvpxhEfz8FogVHZkVKx6DFgAoicPUAspq2lDwq6OfTPsBKot6vWiUfyI1s2OL_jmWjgvzK9z3ctqUi-gWijApW_oKfROU33SWiVckIgdAecBWjI5yxBCFOtJFtEBN94A2z5WCEvjrkc6w0j2fXjgMUR9xakCy7IoKhjT7CVBL_-9kWMKANuXXexwwAsqD9SbN2gH86CeiEuq1GOh1uX-X2ISwxEicrAZy4jOkWhSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=DBrJDw-w94LswJ5KPihiy-RmapyybLJnb-CsPc4NV0av7Ac-Y4xNgIXZhJtI495dki2Dl1MdrO5pEP4motNLqRCgOenJroQE1OGpi7z8agXSqVDz_l0dCS0G9ZxWc_UchjKlaTQY1EoAz6RQMMPh4jCDI8WgwYY_x0PJ6LnM8-UhuPq1Q2Ol7uCesxahfx7C9yqLBcmCLHmNF0BKb1lTwJsw9r0f4Ojo8ZCdpUriVgDMPo9o86aECB36wXFY3MXNFoT_U_lxRGTaUzjHds8J__JPjHFsOG0qjm5sxNxV6NEeD2QPveVJICNXbE87QSttfnwUkvgkaEY6palcXk-xKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=DBrJDw-w94LswJ5KPihiy-RmapyybLJnb-CsPc4NV0av7Ac-Y4xNgIXZhJtI495dki2Dl1MdrO5pEP4motNLqRCgOenJroQE1OGpi7z8agXSqVDz_l0dCS0G9ZxWc_UchjKlaTQY1EoAz6RQMMPh4jCDI8WgwYY_x0PJ6LnM8-UhuPq1Q2Ol7uCesxahfx7C9yqLBcmCLHmNF0BKb1lTwJsw9r0f4Ojo8ZCdpUriVgDMPo9o86aECB36wXFY3MXNFoT_U_lxRGTaUzjHds8J__JPjHFsOG0qjm5sxNxV6NEeD2QPveVJICNXbE87QSttfnwUkvgkaEY6palcXk-xKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAQH-sU_8iq8n7LTQZByc0UJthwwUX_BNqQF3tl1tuhqNSNwRpJFknVGEAKRb--zmCMmqkwJTv4RnaCE6lQJ1nHxOkUESTb_XFrsKf0CbVYAAHCPDCyoayednIHLOWgcpBR49qiR1kvNapH9bM2PVhkNeDiqQtCc2ksf17-KFoFh4byUavIVGUJuxs6j9DNhPiYYfWYfkw6Ky5lq2S1sV3c4trIDz81OPluhke9OV5QKG3efdVJEdWZI2m3WYogpVNHYOSEJ37_f6BrGTkdAraJCWXmoI_MrSy1MXxW-N09Aqtmr4NGgvCm_YYC-10q8-d7P81rWQIVRtimR04rg8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN4RYMfiJI98GLNsJi09gxf4YN0ciAIF4lFWW-040nKyviMuCqd9RaqW3EJCAxeuymqB1PFIAoWiZeRfUEygzc6E91XEwfgLNJu02Nelzygtxdl-uD9octmzToLnA5j2DIMq4KxkwrrRm2NrIkg3vZBpXKjtAnye_X06jDeWI1y1E8z1MFPY-WEzj8U5GDLmzFnp2R8AZ7YoGnCQHJMibLoQW-nFzO-SoW3oyTaZ8_Zpckj_5iv67MmdA-Cc6_jg2E5U7OxfLrBf1eL_Wsa5oCxnjzBM3Cu9TJm1mENkOtRq3VrX33VpZ0xl2Yqe_IrE2a6iYIKM50z2v9m0TYWbvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqGGTjz5k5tuZJPLbicU35B85BjS_dOi3bys4_gkm6N7xPxZI4eKIP6QUfBI8eiQp-KGT7KlNRXatHFu87jMW5HWgkW8oyydL3AGQu-t761I7G165vBoJNsZ3FuohCSi1ZzzLanHadPejYC0873l3F9q9cpb4PFUw4DjhD0u3R5adrq4umCNqfHiXBySum9wd7w3WfU3qpK53eqJar_zKwwF_K5__Ut9Qg7wbYDSYDxjYBU1OxqxHKZrWD1RzHMScRgsTj7lbbDErDZcpR0_P3kq4CTB2-cYR6_Cc1ci_XfF7J5RBUmVR83K43MDnikbrsoggzoSAfuJ6nI0QSlyOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOQfXkauPBWip8-tKJ1letchQprFWQgVmYcP63kdIlsG4R1s6TwZW9vjFT8oiLBYSdOZCMmZV_YtTASvOQ3xemTRhHJ2Y1mRO7xMSbY8mqf4jJn4SNQ_t0mu2SQsLdMZR6aNgV3Z7KKAAbaMkOEUmmIsKYzMgLR3I5m_pCBF_YXyVBTa086WKgnpr1ZxXmWvq1yrp62RoGUxvzl2U9Y4oy0WgeEhDaDTq_2Cu_CNFBzjYvzDH7LQihosJwq4DwKXD6P-d3Es8X7yVX6XpgLEcZJlwwMBGjJjZn9cYgQXA0FDjDNBo48oFjjsyNxeFkSh-Sg9ZM_jxp8Ouj70Aglzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmn4ypasx_0XqcTgNjNr-izW9H2pUSmym11pEF81kwUkK5O3ANlaq5OYhxOZXQ5tJAZ5UitiQdhTSrSRY5aQRKTLEh62twDdaSdEhO_8f7vAyvYA0oCoZmgoZNT1rnskN29Z3Z3T8BtG6LSpZFJW3DJNBH73n2Ebf5td16LrsfG9LVNx7HJHqCwbJvBxgogCj_zNmx0NklbD1v6g8MMa0QxnpnULWJY679L9xJBvm7eIfR9XLwG_sJ40ildBpnWpKhVxyVE_-_uzdSLgkfqGP6-OQMMNJQs1hND7WryZxzuc_gTRDLrhkaOKcEHglDuxPt2nIihatCqPO4UGU5RGlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alCARzZvSf-WUtSvhO5PQVMRltjJeHTFW3beQqsg-d7zSCqno53bjyLUVbywQGSLuVRH11QQRQme4ioBS01DcmQTsg7_uT1o94R3bQVlXgclO3wgo95eo51CpbKmpLUpanUUm5aX0bYRcY0Wu2Z-LYeKFi7KkoGhamiYz_d8ViDnPxINH2k5mjvz2QNZqUjkWuLqHxqVH1DF_anrJcxCNEGFCgyAPgj0u1LRpWQjzwSweTZPke88pPBKzH4dovbxzOE-9mnGzUgJpBBzlGnTAsWQX2lGsziMY7R7mcib4OqQfFQVk5VcaJOhAl34Ej8GYlpyeG-L6x2DfwmQLdcDVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=k8A-5wsQZSZAmnqiQMe809F9V6QhnWT0OFA3a4-lNusbgNL_tHLm-3yxnVY8qziXlWMc9yU-m61XGFHwT2mJzaQiZtQD2QGMB7gMbMWD8yGm9CTEguY-xl31FhO5O_OOB0251xT9pArwlhSDTSfasaokQAe8AslVnOFwJb4mJ8K2Cd9lk7kBe1qY1hzCma054CU1XoDawswJ7ez5ZV9YYaI1wWOg_Sr9ypGgNCBVjN2-EvACADvT3JUb9Wd1f8XOQom2tPOEZdgaqzAPVgvs2WuZAUEeursgZGqgyIYgKz3DShl-dbEnSPoAeQANge268W08sGi-hGNRvcgkI4qf8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=k8A-5wsQZSZAmnqiQMe809F9V6QhnWT0OFA3a4-lNusbgNL_tHLm-3yxnVY8qziXlWMc9yU-m61XGFHwT2mJzaQiZtQD2QGMB7gMbMWD8yGm9CTEguY-xl31FhO5O_OOB0251xT9pArwlhSDTSfasaokQAe8AslVnOFwJb4mJ8K2Cd9lk7kBe1qY1hzCma054CU1XoDawswJ7ez5ZV9YYaI1wWOg_Sr9ypGgNCBVjN2-EvACADvT3JUb9Wd1f8XOQom2tPOEZdgaqzAPVgvs2WuZAUEeursgZGqgyIYgKz3DShl-dbEnSPoAeQANge268W08sGi-hGNRvcgkI4qf8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwQO382qsa-XFwFcFvitnU8F4of_dyJND6xUv_kwF7ZrDmMxY6lYfjMsTBf89l-QieWY5WCP1_CBDIgxLBieSr2wdfY70oUR5xyrAuyj_T96DNGWGubCsv43PYsUGMn5KLru8WN_qZJz-rDyZ-pmVjAH5bdBXs_isACNNHWjrOpV-JgzikN8WSfzDmJYvLRHAp3XGbdMQ0mmPsMCoMNPVqhYrWUch3MDr7qcNMBCPbrJDt9mtuJw6ne4bTFuJjh3z_ofQEhrlt2ML8rMOFw1lqLudNoaxeSLNglywPAEdOGHki1YJBGT2kYnFL0W1QEi1aII-VWLP_CELV5Z21DuYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YirhTzLuGCafEFsl8xDhMEpbFqPK2Cv5lgMZU-JWMlIpfOPjKdJJEMCiAHqBRES-2zrjTIOsWIrXEKxLFffHx4vBh2k8DuT6erPhseiFA4fU7hfVpS1rZMBNisUy3j1s8ym6ugVdUil_aml7p0xNvtwDuhshngXO9a3t_tJe-VmASTYAJs6meWnFDilCCmJG7wyPsjmxwHVMCBgxDCCPFNAAzRXffrpEGFIGtZ3MXK53fjQeczCF9GWm8EUVJEwFt0vX1FiYwGdcYaUC38uTtXzcI7gH2My7k_TggvYqK9FStzhdoL78aelUClye0LqU_H6e2bAv-mvyFd2XZzgFMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgBdGwnai0D_bafXzBHE0uSvhufIskZ0QiVGuF_vtHVkarHB4bE0o8OKQWvDHeoDDndbvFqj9HBqf8kWxvokAC8hyM6GbQFPmFgAzavex1mnzlpYOPFBhNoMywF47dReTkGaBFc5vt0VOSiq-Rg288L_-p4mhDBmSBFCKyz8dnGxmpb0E9ViqBHwgIjVT4pKcvqoUf-AMHm8Nhe2CJ2IPtQQopnh0LGIIDzYqjOP3dcJAwLnr-Pk8dR-oNVC5aXO8lM00pd-FUBh4v7ypnZQACAnv-IFODpADrmMybUrcWuzedc59eZRRktbOGEbyouXN35cweowPC9p9MI1kxnHBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDJt7ZW0Sj_jEw08HgtQQXflxwcFwSUyHE8UMWF2OUOZ2Y4p9YDNzscqQSgJC_Zbu0CiLEEjczLi6gfg9lTlUsBUeKklog03I5zg6ctsag32bVRNsG7HJqvqn5t0VvQE7GYzzG9_fGuwrCeFu54ovFq7XCvDl5v2GCbdByTVo-y3Drb7wWnXdD5gJRUMjiRziaVetjuOMjtTn4nPiGXM8srv18xtGn4SoM1oLXgNZJJEPJ7s6DzhWghOoy1x3sURnGMc0HSWsaSMqV2TDqBaJJfNlJSJV-V2ueGmeDuIN2J-z2kJ30-AlN0zXGONHptv7yM6pBeUl5V5JACerCyrcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLp7l7GAxPt92bIF9IdNczLVSt22x9iAhk9T-O54CHwdKq7Tj4jy83cs-SggNSQC4fuC3XF5PZcEqjT_7iJ-LzbCYAklbcHGkVbhlISXyqAXYy-aSosXIPMtr5Vt5rsggcBzo5JgLOavrmDRgG5f6ZkwYZIqzUgLKq_ierW7RqX1TKi0xg5oHAZ7ee83HGcAhVpfQGZucllLSQwd5hq726NPrp1zZLpV82FAeyhXXHbAoHxbrQDXV2mtsFDXQF_hL_thTg4QP8kr9d_JfU84c1X8a-JLK96nijfeA27Z7VJLsHp45Jj1k4_z4c63dFFrErXYUx212UU5uDY2NfzhGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJnckzriItV5hvoW8NZgZ_E6B8lV00WGqPhnqY-sBg40HKQnMZLCTYLWVXOFQmz4nmA-VK7bPnx_p0tBBnylO10kq6_LhgfSFWUx-dQMJcrJeCT9YLi2kzRPmu0M80e18ZwqLQIfa7rMTUItH7YJuDZsLgOruFgb6xr4FZZCNqQieBMrEZnETOcmOn1tYa7uUsiW-HQ5KYWpyStAtdLI4x_q6sB4mFGFyZpPZMKVeVnmFMjYWrBmMaW7XJogBe38bbl3YaxVcLSVE0IfJgIDQxBIriw-uLcV120nNF_etuOLTPLXpVXbXTILu6iZOrfaqWkfrzpcey948IhKaVduSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIdY_-h5LCP6OG8JW6w-mmMX0E5ukcykN156xcAOBBnotq0s5I_j3iDxc_-r70_mB33wQOkpQVgQNObipkLYzD1EKL3Vb3V6oAFRKi9SDxtikOSMtKvzLYpw2zLwcNH4l19EWpBnQl69Ufwh_1faCZASUKe8dpe78nGuYsaKYKHQX6gph7UQ1ZjTqzFS52s29w6szeZEVqV7JurFCPey0EKarmY5gO7ob3vPXIE8dOWp2DOMZertZAJA0G4dCVPW_2lMHlvHYhMfrkCPR_ih5x9TQANzGEbt4xPHMSzGTiW3ztKKd5hkP_9MQI_AQPxDyqEprldQYhnSzGeWJuY4jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSr6_9y2L4IEYY9dw0-dvn05SKXPdK8KDE0BqkNemZmlnjizxhqFh2TSould4Sel0jHqsZe7OYzuQx4SAzpEqYJfHcaIUh2-vuJTy2vLkSUFi4d1Ol3HQupsxV5myn-uWO4oNg7QO6VB_BBZVVgzC6R_STKWzrM8jmcB85AEFOEr3v2w7-mwhlqPulgV-SJyGLTdH-pdnDnH4ONbqrJAHX2mW9VnInEB1vEAcxLrUQzIKf6Of66KPzBg8B_R69xFhFn9rjAby29S60xcw-fZZHtpeM3y-ezdCOsseSGmZj9CKK1TYYmjvZu5mSbuaxowFoEf3lud9hgScOj4tL_xBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnXH4r6rbS3mVwCVRK2Lc7prlLFYI25FtSTxbX1bMTQTAajGiCwL6sfLj1gIO_hAb1b5p-8RNnlTUtZVz8BR48VheHsZe1npY6yRasL3TXBGh7L44iZfF7oZtU3iDrss4kaFgVyacARdGcbGPoaxdaZqxHns1Q3tfY8gNjvYX6C-ZDbUzwVO8sOOmLDQ7xhGtIOkQfwhiTOOXOnVsmi6QcvJiiupG1DMGA4zkPz4-KLd63DbtX4RwwmCs6IZhtLE0jZBJAo7vpei-VwBmCxW1j4WpsOjtsJDcr8rEPCDCulK6dLEpd6Nj-KYvyNwGuO9D3r5H7YLyqYrVpKP4KB8qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWQAn8XSfBxWDCurSue1ukzuMaZXIFudvp6GqDdJ-bPKffRX2YivZlLAgdM8-7pu-0R1fwYs596YDu0p5xKsfnOvjxNrlkW2q9TYwCNOMy4NArRMpq1_FjHgWzvCmj4rzYVpnoAHGhnVWbRZ3YfkSsuBmqfFRIac7FHhU3dPbhDZATwVrLQ6wg1KPvbsEvqej3ogNuEyZYjimudcakWtAi1aJz7yR6SAdPtBYAQTxhBlTmQvEaYrskFYs41DOjNqPI42C8Jrn1IqaCJNl_Rut8VLGyxShu5O6H0y4-K4AhoWfv0QxSXk3-07xPgjfq-5xiMxI2FtcNNykMQL6nnFyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xef9ap85gA861Ib7jKdJ7yJ6nyvGfbfYTaaaUjo7U8Ngj9qZQE9d9uqt0HJY6xfwpgtxZFMFsuJNmWC2Rc1XVcpDcRl8aFYJb4qUtHWkwxKsVstMgMk1t10JeIu7swGyLkqTjVkSSY9ZH6xQYbGhNEOQTQdwyCFVLPOb9CmvXtcj1Jiwuv7UFTSInFl6MwQxkayRU_h9kiImmUiqR3WPQCGgcxonaitL4YmatHvpLgWqVqbvi5rTannd2t4wSA2iwEKY97_98n8zRSH8uFd5YLn97YNxrx_9fhofkaujIsKkER8BMijYMXkapFkVyjGFz5AKLtUdb6zXC3QDacUx5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Isv9wmcZtv9aFnurCzol5SBuWLm7hyuq_GqGEk9oW8IbaUWZ1aWk-qm-cJODf59pXzahRxNQAQsSUxcB4VbDLjQvDxNuQH1T1TpNGdWB3SZpITlwF5R2fmBVb415uuhcTSrmZQpe8pwYgnsuADe4Cl3sINc5Vz20GA0x4Be5gTQxWDPT_Lw7XbLsSSJecrPN8Mn23r63rSlRmDPrsvqxIeHONVzyijckCEPpPCeRyTz9cRWjEldWh4zzST1iE2HHK-iekIVo3wHgsAmNyJI1-eWh1SGVG9FUQQinuHoeBFQ4_GqjoArJPzM1fydhMdXG4K1_FGAASSk-XWKI78MZfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qmm2Ahz2dMm2YplVgw6OlNT9lpJcuNZA8m0o4ZO_q39QY8RNgy7uzAm_RqHU97TYyChVcloxSLeMG93Oy1VI5lQZdAC18tyLm2LQfWpCeok8hqrxSoxieEzDCMcbGGt2LJ3snzpfLPZ8NYuSluxSXBbp5Z3Jlo-3O-nKTY5UjbAw7fdS9DXXZB9kQje-MyC7r7PK_xTXQ6AWe0uEXH1VZQ3p0ukD_JKIsapBb1MDiDmDyG2kMuCE5nsJI3bQKoO1cnuSwx02G17FCUnf-gn_DpJWWWz1X2OXd3iCjdjQ_WwYv-zpwfB_91KozVJfBQsi2_eaPX7Ueta0kJ5YhLW2FQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Unv3DApdkfqXB1j5UIJlK9SrfIlMJSmcdgDA_kUW58d5Wou359U-TmD340y-WshC16gM_kSzrAcIx34n6fnQDOJ4q1l-0d6u9XQTVJpT3mlQ_h-v5rnkmw2NLnQp9LRQ32vuEXiHKCcooZDUpXOEa6UwVwMeum8eecBqn4ZN728LpkNK7Ym6VgdOOB1ebM8OnTdBKvuyzm0FeH9D6xQSnz_YErKxdv_JziWu-jU3WoeU3GPU3IedihwBsxrmUjFF4bEjptOAr_AblvfAVqchDdGWAriivc8JrKPyl1_A37YJ21PNyuR00SsxkQgB5PBB46RLFV2ARojUlG75XlQSYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFb1pfCJG2V68uhQ6raW9uKhfTTfHbkB98WUA7tg0BM_cLN-PXRIaVBzKSd1gE3jyCVt0ZPXbzeiTqf8ixZ_IJQPCUntEBdMVbnJ7AJlGuTmqSWEgr0fmu04pxXPTbj-WLdXWt6KmEiShNK53ikRmDpwyxNKf2BKy_6hdJjIchP2Q213hX7ZSokbptQevaRnCMQi6YCBSxP8L5WIURYjt4W3pHSt9c9y6xzXgWhFMJ32y2jseo1YOyunl05unmlXi1OuMOEE9zX1bO9wJr4Uezl2HyjCuvNEfoetihcMFF4BytNe1EbKgJiArY1va7s0T903OBEuPsOnhzDqPrbZ5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kc96dcxQrAKA5pMvKO-dRMm4g9RWCzAveR89eeCy7lDU_eg09Zz-CdmwWLVMx17-Fkn3FiEAL4AFutYroPJZHmufyk0Tg9-urJGPjXfI0u_SImzaKeh9762lK0n7OnYugieXECM-qgWPIFlnfA5EKaNAoGUr5nN268mmuQEfoIVJt3i29jcvCF4tSAqWqJ6HNjeB45pRb00Qbs4AYAjOUnyqkJal0xkTlGwHusTUNrHvBh4-1J3hA7lnM7-70PNXXHIfaD4QyDH5Xu9W4tYL39ffaZJZhtJmgqxOkgh7iUubelL_-TLpwDHR_HeAuv2wmy8iygw7v1ei26vRVKAQmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayxO2w_AgI63xbTKYcTRYyufszWdVU9j0WY5EmHUNq2bUCINJyi3auMKPkYgNhldviKsiorrZ05Kz2OeVCA42lUpDkOKZP1tjWEO0bZ6mRXw6bLN88NBJ8uexftUZ4Rm21nwfZabq-SYxsMXZAbhaeAzPG9R6hrpnOGSHkpa6nFzJVAcjb0pwv4gXZyOoeP1qOUA5ekOdWQjiR6VU-iacqYYVUDF6zsFZURWzq3msTsHrJ2K_RrfeWVQL1BkHBqXD7IH_qxoDwtdRUwEnU35ANLckHYky0NgBzu3QXxYaUaToTH8juicxeqd558IZEdKuN5XfaDU1LsCWxpdOKZA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ0gZYqX6bzBEZtncLij3qWz7AZHU694y_h4sMkwbMe2DEPktmYFdeLrgMk6j5DBivm_SRZ6g-uSImhU2sZqCA3iWoGxiTlelfj6c7gqXuIGV6nhPbDfDD9lKVaGDDjx4UCzlO5WfG0F_US4qp6Hsv-PFg3QMLp8WxDVezah2uLmPpL2PcLWYb-7SH2TX_2qgk8G1x7uP2ZNd6SYPO-8eFUOPTnQrGQzhJ70sS3bc3KhGGuOQcPQKB4UpTIfIiR96fXjryqQAYrRWBryXve-PsDNuqHWYdQmW73mZGD6JooTk7ICpGvOyi0DgtAtEYjW7f2t_fFFFJg-ucV75VKSNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUB1wYGbMvEnsTKQoXEREpqMndSD7lOny4L0Z1SDHtAmccM56kAHU_Iybe7NnzQ13hi9JWnePfD7vUhbCNVMwcWwajpPnUsPfJrdtYIGUmpdQypbIxDqi2hFe7Qc9qBexP7P-ODmNxzOfzsUwpST4HNmf2VR91SoKAX0h64jkyEuEMUpI9mSeiaJpU16edsPI8Dt0MZIoVVeKpt3Plh72F0auQBznTEV0CUVjWCojElPw7SxQIMeHjYOEyG10ncGqHxfbziBIJYKvi-cJ-TR3iV882V1EAlOlCtmnEUnV33rUctWiP3du9kjRJ-GHZzQUDy82D1hpK0ZZa2P1nUyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=IHVLtzSY4mfQS8xyP1fPI1ooAYq7XnMVGZRlMq3_jok4PDwyXqaIgvv7OIvipQvqtfNhXy_Ufn5kuBgdVtqTTupmXD0f2aAPgRekZ0aCnVKvjF8tKPBtlfcqnR5Zu20evRbnsZeZUO-qTHq3Zlp8B5KSskdXCFxDcgVTnKWVHBoquhMWUFtBmBYGlaPoXGTh1nZC0jzTxgJGsXjEUObLW1KKXcnkBlikNMnkd3eobxCZKmxKAyXjm3uh4EpJkm4YCtrwpVo7pBQTnNlogNH4BLDBRD2H2R5KJ-g74FOeDx4GmAPx-rBkTsPdY9gWBwWiCzSF6aurGqwFP5_FdbhZ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=IHVLtzSY4mfQS8xyP1fPI1ooAYq7XnMVGZRlMq3_jok4PDwyXqaIgvv7OIvipQvqtfNhXy_Ufn5kuBgdVtqTTupmXD0f2aAPgRekZ0aCnVKvjF8tKPBtlfcqnR5Zu20evRbnsZeZUO-qTHq3Zlp8B5KSskdXCFxDcgVTnKWVHBoquhMWUFtBmBYGlaPoXGTh1nZC0jzTxgJGsXjEUObLW1KKXcnkBlikNMnkd3eobxCZKmxKAyXjm3uh4EpJkm4YCtrwpVo7pBQTnNlogNH4BLDBRD2H2R5KJ-g74FOeDx4GmAPx-rBkTsPdY9gWBwWiCzSF6aurGqwFP5_FdbhZ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5X-yEuhZntMKYDclmbVregfuYqnITDh8cMUCWvA8WMqaB9HS_pEchBf6xZnPjeMdm3tQxQEoUpl3Ojz77A-6IIfqsgrPdFXrngIdP9lVVM_vw72sVa64K8CRQEkm4lh6b9PVlvgoR1T8OQYOx35FdhstAUxjtfj6lxnAEy4kBjAkfsuGn5rVnlZDiHQZ63C_95bqNo2nVljzQZvhAvtk0YET9RL2pV6PPF8G6_Ai25E_SSKydgKBlg0AhfpjSUvZm4TiI4R53VuZPbezV4G_QEA_1eXvd6vb8xQqlg4t3--X0Es5DBru3j1uom3j5yNz5IkAYKN_p2zu9vKK0rOkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeuQwA3hUKIs0Vx3qMUX_QWD-gtW9VfQEQjLdVsOSSGDP2e3V9DD-k83Mt43oqM90fbUHupjvDkdNOpzSZiTzvgFIwfRPz-hImi2M3J4NdUXllN1nm_eNSl-fM5SGyCyXpFxAjlhFlEBbfLj6SHTgwpaCtAIqfHE_kGcKJGMpIZg382mMgJnGzuuZ9qqdW0d2_Ek_HBVvEcNBaqfZrCZJMp2ZJaaaoiddQfyBoO7Xbq_19T_WFRCxAWM4y36vVlw0oecRKGpgxnKVW7rKluBk8qd8miZYU88J94ntEY_upMn4r5r7iHsSvzZPHS1bw6vIaXcIcEeGFdfnTmslBcvOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=g4Rnx_f1KR-D2YBzEWndwnXN0u0ADvwl6WUrLsVY9dPWb9HJGXD0dYM7sH3673qDnsWnQ8hIl1YWIC1m8wa8CLGHR5osm4oLoqN4f6QjWY53NzaQqJYTa8i7xeQDDFCO_fKU5EDjbdePThEL2lSNZLMRl6-sD-7UyUnWV553Wlf1zB1Onj54raQQMZU_d9pJI9ILUUK0rDn0s910NRBQh2scCep-3tGU1MGaHDSVLV8ae7McElx63dWLsYVNgZ7astODJducraRireSWmCNv7rHOTymbrOXy-4Snvggiyqo6VShdHC_qzKVRogG_PCB-gt8QRkA5Ad5t7DagcBeuZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=g4Rnx_f1KR-D2YBzEWndwnXN0u0ADvwl6WUrLsVY9dPWb9HJGXD0dYM7sH3673qDnsWnQ8hIl1YWIC1m8wa8CLGHR5osm4oLoqN4f6QjWY53NzaQqJYTa8i7xeQDDFCO_fKU5EDjbdePThEL2lSNZLMRl6-sD-7UyUnWV553Wlf1zB1Onj54raQQMZU_d9pJI9ILUUK0rDn0s910NRBQh2scCep-3tGU1MGaHDSVLV8ae7McElx63dWLsYVNgZ7astODJducraRireSWmCNv7rHOTymbrOXy-4Snvggiyqo6VShdHC_qzKVRogG_PCB-gt8QRkA5Ad5t7DagcBeuZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=N9pho-JdlSyigwCQW3g8ufcsVsOyE7S0wUOeVK2vyLcAzrMf7Fq_AG49bAHETNUJ-kBAS-kfRMgxKH2NUvkXBHDoUwYbhG418t21MOIjyeTOpogl1OhEZinL1utpeoDoZVWaHhDutOdlSE0kp5L63m4esO1SlQAOIr4QCaC0OI6Rn_kQqK1__GdUbVSRz_tUCcCU6tlaPdvBb9LQjwBTuVfcMbZr7-sPmYTKaz4vBSP66pTQJohI2usqHqXi5BS0aDkgp3aKa44CFUFRke7oADsjAsAjOCrqavgKjsKEMmEYYgFH74Z8NmYgf0Ndpg1WsEPw9UQz33uSfFkzA3z8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=N9pho-JdlSyigwCQW3g8ufcsVsOyE7S0wUOeVK2vyLcAzrMf7Fq_AG49bAHETNUJ-kBAS-kfRMgxKH2NUvkXBHDoUwYbhG418t21MOIjyeTOpogl1OhEZinL1utpeoDoZVWaHhDutOdlSE0kp5L63m4esO1SlQAOIr4QCaC0OI6Rn_kQqK1__GdUbVSRz_tUCcCU6tlaPdvBb9LQjwBTuVfcMbZr7-sPmYTKaz4vBSP66pTQJohI2usqHqXi5BS0aDkgp3aKa44CFUFRke7oADsjAsAjOCrqavgKjsKEMmEYYgFH74Z8NmYgf0Ndpg1WsEPw9UQz33uSfFkzA3z8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=Wn2OISxdq3EDlmmxVweQHzqnsK00njlzdDLY62k6Ir2qSqo6Z38M1tjzkVjvR3P_Qm7Bi4NcIJoxQG3TU-0t5Oa1aJprxIQEHZwxhCVuNFtWXSxO2jNf4_H1dPNXn1C6id2I5kml81_1yacwgDy0Nzk6pAnDZKrMYKg3UTK2HBHx2LV9Q2LDlGdIz-nC4h8sLaPgGnGaYBUkjz7BAW8BkGulFhKbh_2bhudow11PPaOdOXjQZBBPtNu1IfmDJcOPGt2FQokKorkfCXU4pGZmA8hHvDlnH5cR97Jz4XQLkmaz6Uyr-gJcEelp6IhzYTFjwCx6crzha44fd0uugHsQ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=Wn2OISxdq3EDlmmxVweQHzqnsK00njlzdDLY62k6Ir2qSqo6Z38M1tjzkVjvR3P_Qm7Bi4NcIJoxQG3TU-0t5Oa1aJprxIQEHZwxhCVuNFtWXSxO2jNf4_H1dPNXn1C6id2I5kml81_1yacwgDy0Nzk6pAnDZKrMYKg3UTK2HBHx2LV9Q2LDlGdIz-nC4h8sLaPgGnGaYBUkjz7BAW8BkGulFhKbh_2bhudow11PPaOdOXjQZBBPtNu1IfmDJcOPGt2FQokKorkfCXU4pGZmA8hHvDlnH5cR97Jz4XQLkmaz6Uyr-gJcEelp6IhzYTFjwCx6crzha44fd0uugHsQ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
