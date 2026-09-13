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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 22:38:00</div>
<hr>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN6JSsuNnWss8WIcrB7squ-XHBVvzKXI11JkJTUBTU0V3LbOJGWvfVU7gLnr0V2mS-GLZRTOWn7Vp7OBwzrBEejQeAeeqwjX4GS8mCD70BdhEcBVj9puwf9KaLUiuqJnbsGlF8aa-OkBgIANz1eMdWbv4BFXTef07-zyxROB0GbDKz7vztOv4juXxeC4bJ9QEvi3yhk_CJRKAZuIQc8JnlMASRfG7L_zMPeCtPfb5bLBO9FCzainPumqUNuV5Ex7UfoRUUU8VRCVr2aFOl-a35D_l97DAvsP1pYGgp2IuXTlp6nnY1KQURHhuJQGvnzmpqC0cvFO_xo3xMfFpSGUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 200 · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 364 · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 992 · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 971 · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKUqeExmmsHO7NKWvDhrkn9aptlNqf0BzIDNp_FeI_JjTW620-M8VTdtg_KL1Xc8V1rS3M-jYRK2sVbJTKmLEZi5PxqdAtVlkpiqdDYsUA6gyEN3r4-QtSzBfjJuCLhxuklZzPvvd3tDlshQnGDV9skp6Rl1qHkABQKzcy06_90KFrCZUlo_CCJSdsMn2qAhcli30fB_WW6Ca2imckzPFGo77RjlGonhcmgn_Zg7_x8WAm7CfM0eeQO5FOkGPvXbkrbWq-FdPWJxERMNOwu1SctgpUeHS0foejmoBCnCwHdAsc5D7tJqbCeXmEfyi-LnJ-cZaSfM1Ei-Yn7XujL2UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksdZ2-sNSE2U6mdOGPgVb3WKpAkdHf0jedEAjtQESy8PEYArNsihBJflKwUDZooWQMLcZojcz47_M5Xhl0BfDXHq6IKGM0ZayExb7yjbHh9i29oZV5xRX0KizTCrH1QYUW8qT2KYvmsQSavaiLPT35_g9RMbF-vmeRE6e9iQdF9Iwz3YBAtnJeu-W5sbOOLXe_hzX5Eh9qz3cDUCpD7nARyhg4hoRVk_6NYjPO9OZ2OroqOYhym0xJ2_jqjrb8jVRMobQznPbPlJ4kc_HWAHWse4Q59q2P14LiiTIQ9byfE6M9AM6YyGhY09WQF4g5j4Kw3LpuE6TnhbGEC63FBevQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jVgYfmWz1XO6pnwy_fTqzTBlaG8USKOmT43JUX7aWSa5RFKz32kiZb3LhdaBq4lB85aQc7rb5NuDZN5e67ECGfV8RZIBMou5XRgB68eFNaGvc_DD4gScrGTvgAoOdBAA5iduLydt1SXJ0ab1hgFYxrctRi0BlNKiYI-SWgLpyVU2OmzcjMnG6x_Jfn-_VgGzmIH_5jCHaF9mgRDNyVM61hmkLNa8nSaFozfBRa9oX5V3aidn9JxfrGOwCkMZ-6KINFD9Tx0iaZOnJ0h7S25DpGxNTeqUsmQ4Id_AvKxYE_uUB82MSYSWHty8nfUPHaTA9wI2XkRZMc5bEBkwCYW7KQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPwMUSduTem8GwbITsVuboRhVWArR1Z8L0yFOs9RtwBF8WK3FDaBd6AJt4F9XVI-VhtY8m3UukSmhsKJDgMUJmUj8LB5c3CaiPd58Knv3fSpauWSeqoD6ne7ClQhBabnAn20DtwOANF3c9G70KGk-rAB4-k3EXqpIlqb97iC_bya1ExSVWWoj13UfSheuqkOxiWfm3ZIt5QupQS738yfagppbOXLQqITyZB_uGzhH-gAx0Xih7_NthEiG86SYj4HQ6seCk4BAl0H-87M2mgq5NgX8S1oP4XVbb6D3ZfAs8yzOVK2XheRCNA_socaXrSNUDuE5Uz25PJ3ucOVIIPZvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZFWytPvgxIlQzph4NDoDrJVdspJ5Lh8gBz-rqIgDUFcXia6QQRdFvu_U4uSOx7REVvxoD1NEk6SyI56bA69EoKVNh2E7JG16wiaEWcwqqefJinMoghQHEX1bxfxCykyHzpqnnIYPpwAjH3NHCJgw3wVHzRXZJAg4RWT8mm7DsrPdmKF9tFrHVYAVae9IegsHsPMO4Jn09Jf3GzDR1YV_tyPRWetdK9rHuAl_fi7hwmFU0P9dAMkdQcnglBENSEvEEji9kDCiciajBfQT-lFfr200mDFH-EgQxaN5lJzovYypuAABDtV3Vl0UuISX1b73lD0HmD1-1JIBu2jQP_6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnZZHz4mLBgPO2mbcEFr1ItXPd0l-2d5Z2IWV_8AAMmhA5mCBHi6ThGgECBfWLF2U7RvuCUQNQcpCA6W6Pw1tnsdlEThTACVIXjtNV6fy0czFtHPvo6qCRrdfdQasgQeHeizDvjT8j5QGVG1_wqr5pDXqwkuvLUuOb96OG1Y8jzqyBtV6dgFoQVkjP_BIbrRVb5Ou82x2cFd3X_n7653lpBQ9PCBYG_-4CChz0RS4ECTp0fUMmh5iIfLyDNPkWlLyqp4VE3SfkQU6bpupP3yYrVtqM-bPDyQIowpwqt8mkC2mTGlGStgwaCwbx86C6kxXiDUOHISZmnZbz_Y4N3c7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMAEx-t9-9sa5yX-cMK5agh6hQ-GFHn8NcfVM3Kffnga45xOJt3Bp-o94ohnuEV3_NZrrObMuXu0tcv3DlDfXGoz3D_CiUBEGBaX2vRHwAjjXBnnMRrjPiPuxh44PQFoOpCPqZdn4jyR81VsQvcBG6YTZlZpi6oi3e6hYo_ouhLHgFqAq-820MJcQJRgAK-BnxL7ZWtQL9FpOyxTmTvIjA9aXgTWPsN1k2fthMa840FK1yoUbq0aIrUUYjFOLeB3Y63GaU4-XytYp-NI9Bxn1hz5c8vvElXMo5jO4XGfnQCgubfcHmjYOCcCUACX-enPnUamz6ivV-iktY48SdWF_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYW3ouU8tRKB3IOL4CeVsEcA3YjUpM4TdTSX0dYOOKzF3C-X0WNJEFoiWZ-e6n4sYKviI0fPW0pzRIfeQFmFmGvDHReew1r1-k8_Qp-UmMsGv5C6Bzr7uaTfstBXSL1wgd1d6mpYxuzeYZAnhIm0WmK1ywWo8WIndmfCcDA2Ojcakhd3VVoSSjTj-iT73I1TMIwM_9fYoML9oD6gvqJm0hQ433MGssxf2lBntF2N9qk___ECtfi2KvpVIJqEO31VCau-mzy4TLaNGyDl0GiIGFfoOJfOcTPrPgfeEKU-NUzYkf6r3eivNDWNAIsJdpKBvL-hzLZUmcW3dl6aV2qxOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKrV5Bruwde72G3XpWjFsHSorOnEnLeqVO72Sq1kbroh6ZnVdhi1iKvinx1NQ6mSnrEB7JBxJjq02fJvF4VYJhoYJzfppAJkwuLKFGzSS9xYawgUI5NNsu9_TFTfGn52b88XvWYj-LFPPj-2R4fdXpRlovpt-S66deod2sqeT510UakDhKgkk8tXgThvIhgHfuZrdRqUxzA-Fig4pUWtG3-5_7cW2UtnIFBmhPfadvsk28MMmJm_w7FW3J2Al0ICP8gjKNRgPl4Dy9T_fPDwAutcyvjw6otNxPJvQ2-SsAs5LZSWwNumis9u0ofhJgFV4zRetJ11GTK6Yx5X2a97zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-ncj4pC3_OmPBWHdfTkM_3vdj6an4T6e-qnyVyEPMxKM5D0twmPLfRaolfFsKrAWzjO3BkHtLJcJVY6vp081eg7c2gwZCF6IkVTW-ofWR6cnJQAMc25-8EkK1jdKRR0uwqDrPjyuIteWC1u2KgQb42j2JId1EE-AA4plegOWWUW-Vv8LT70kc4gAztYYOaB-a-2NLGPv6ROBHNBP2eevFDwRmE6OI25XqKfYUUkwxcEfpcjElv84jPVJahd8acoflRsnf5QYRaH-ZFbvBPSQmlulTQcB7p634G8Are_ALX73h6AwhKuqKAGrUx-L3-LjbgkqPiHygV9-IZkUvFcPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6jYATpWkbd_6zYpjS_HQTmog8vHKW8Jb4aNJHOHDsGsmmf9X-lTpShWb8VK6nQ5GefAu8SGoHUcH93IvAa2nb-ii0QgmRA1qWOLrxRZHv77lHzZy6ymELAyzbK94wCN6Y8F8CnMQ9YnXrPrJe1EEs_MUVpbkpnzs6M0Vy0JtSCR9HG4Uuvfunv0BiYhBZ6r73tZNfuenvHEv3US6mUdhscC1u2uNwa1IAL5K_u_yGOZxbSxnlPVwR4q7xk_HzmrH_jeNr4q68QEOpn2v6IwmiRZbCwXyY1bN0SpHVByWwBLwmq24Itasv99rSynusbEioDwQpDpdfTI20bd0jpDOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8XbL3qRlIcO747hrLgCvFfIrbQB75WE0-ovEpFxDHWbIU4KzAR9Am4_DLBPXGE3JDHapsAxG80UNwWDUn5iGRNOHxlnDGmEtdaBYnb8ETIY37JkoeFuDKLWwZI6nqZNRsSY6366eObyr7Zp8Fa2pdBPIGiPppF2HEt_CFJFZP_jSu-9S2XC-PHlPaT8F5pHFpXHTWqjldAWln1CJB7L8mB2MlPsnfsZ0eeepBO0k7-L3wY3N0ukHm7PNDZHxO-S7lrO7fGtI0MZZoY4svWGjQ-JAFf4wm1XlTvDUKi3RttdzvcK9-tlBOGkl-owAwUSTZnXvH5sMDNvGKpoWu_FQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbJH8M6iqQeYgBWg3RTGt5mKrNOhHjg8yT298vxEYH8kfRHTnOfk4nGl76Ap49xsX2mUvhOyvIIAeuHodmQqqwqSugXmGe6JR73zEjIQ220IzmiLpFLtb-QTnS7tuIkw51UhK_E1C9FZvkRH0kU9gJfg_fQ8M5fBNPXNTrv67fr0mhUcZ5XPdCrd1RoCQV-hieeVQz8s4o3cOUrcSeRpcXKnCTLtFPPChWwKDp1PebTX7swoOKY8d-qyhrGsWN05J1ta3NJcvY50HQXLsoY0jbxe6lCEIxhi3QzasM7PnmsaAsW2Wde86Xxc-CGwh7-W08qnvj6-CSXxT1PGOptU7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vu-T2tojfZwLlhp_pcTAhcUVbiOaYMDFu5Rj-urJaMs7dr_xG-R7rTsHqtmcoGQjCNog-l6PTBeyKNcfo8fz3WlGDtW7Z4KlnBkB8wNauCMgfHJYyiYcAzO-__3YF2TvOWGL2pWGRKq1YXac5p_v-WNjsk6397X4z_9Zie4golKIgVZ3ZP5KNl-_b3Cl8sOQ8htNaA6olPEh5cRDnpxYlTSIrabc79Avaug4ydtijLIK23w_eJeuv7mweoBcTVdUzs55LTR2GTAnrJbjbjD32ugWoW8BGgWtGoQf8CMCEXW6mi3jXxgQ1z3DaMuH51PWidEpeqD-5Am5rnLCd3WgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTGIeoBdCmqyzhwr_hiSPydE--ZOMWvy6EYDUgAFdt9sZn18Kij__QtdBSYy4qDebaWDUkp8FrqyMrekW_0m6n9ryQQ5tuzaxURhXKdUJppLcTgxkY0_HS9WoEhNKGJA8brVKhx9X4bdXXbc_E9LGhtNQfLpyda4qjz4OwRb7uy6woF0uTJf7NSAmzGo_W_Z8qF0GKnyPQCtHpVlkX-x7-VqyRCyp2qUb5L9PdGomExryPFD1kSD-ieIu1hJJk2afecJsCKjg736uNBBTF_4rWU0c8M5lisvNoPxLqIvYYv6UlkIiXul1x57u9j7Fc6psmtpyLiuIngfoiMFkZ1ESw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSRVWP1bc9Bt_AEbDrgSao7z4M3u_XiXs2_ssBzCsX24ENqy4jfIq-aAGLSk_qX4LK18BEy3QzhnxuRyxlmynYcD1ZFxWHJw4WtWcvC_aRPHbOwp5sEA-yvIYohtHjaUhW3VG107CqLJcN-w_--TG7IFFWnsXNFbt3BhPTmKozn-GHXU0kpY4R5hbQ74XOrqwOl5w_huW_0AxicO9rNkvmQt7K_dBDJa3emBqtVdslMhGpIvF2WYoLIbJPVz8U0GanHJANAZC16g_vXSmhWNT9mw4-euWfCvXgY1iKDWFlWUJihu0uc5tLk_RpcUUdqa3Vum3C57rmRE4WeBjXvvgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=gM2RCatNSf_adxrxgmaV7SenvtUkLq5irGyovJxIyVxckDxLeooXhRwJ-Jv2xa7EWEjxzJtf4EKfnkqXV2yyAK4f2IKC3ix6Y-Ur8kqPC3a-Gc2eIZXSn_go7f52PFKaM_OJrj-TC7IXofMJuSSWNHPT_50v5i2qOoqt56_q4QfipIHEJ7subYbJYy1Ssxeotyyrpvqd13WMQZtbntLw-lC8S7HlBt2QQqO1vbvvJApeHNUXhNL4nJFLplRXk_0gmYi2K0tJsPxcXumE4b3wVUPl5x8Y3n_pHdTQGg-4ZtZHiIewjYVgasesNtVdSJ9jjdRuap1WJaO4U2EHKz90fZtMtmyi6MCx2euvP5Z_vZ35VIyaMvIY_IWfJJAj86fqelettObSfmT31EZQiVD3CfwyHxDO-ykuyvzublu_6D33b2sxUofapeyfwuZ0iiRKJjgeH0J0wJIlLQ2VeH6EbfFfTwGnz__-JmhXE3Ea5H8ZKs_RfQD-RyhztBKrjox1k_DxEsZ1YS3MU4GLOESrSDfO5-Hsl2zPRxptdgYBFfPlNyrd0XsqwtIUR6QLGay0GemDgqVKoY-GIkaZZYSzSf2eRYROAJn5pfowaWTb0h8Hjy7C0pSq3Eh6L9jBzJo-ZsY2T62tMIviNAY-VrDbeuW0JHchQxPCY2UMd4ro-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=gM2RCatNSf_adxrxgmaV7SenvtUkLq5irGyovJxIyVxckDxLeooXhRwJ-Jv2xa7EWEjxzJtf4EKfnkqXV2yyAK4f2IKC3ix6Y-Ur8kqPC3a-Gc2eIZXSn_go7f52PFKaM_OJrj-TC7IXofMJuSSWNHPT_50v5i2qOoqt56_q4QfipIHEJ7subYbJYy1Ssxeotyyrpvqd13WMQZtbntLw-lC8S7HlBt2QQqO1vbvvJApeHNUXhNL4nJFLplRXk_0gmYi2K0tJsPxcXumE4b3wVUPl5x8Y3n_pHdTQGg-4ZtZHiIewjYVgasesNtVdSJ9jjdRuap1WJaO4U2EHKz90fZtMtmyi6MCx2euvP5Z_vZ35VIyaMvIY_IWfJJAj86fqelettObSfmT31EZQiVD3CfwyHxDO-ykuyvzublu_6D33b2sxUofapeyfwuZ0iiRKJjgeH0J0wJIlLQ2VeH6EbfFfTwGnz__-JmhXE3Ea5H8ZKs_RfQD-RyhztBKrjox1k_DxEsZ1YS3MU4GLOESrSDfO5-Hsl2zPRxptdgYBFfPlNyrd0XsqwtIUR6QLGay0GemDgqVKoY-GIkaZZYSzSf2eRYROAJn5pfowaWTb0h8Hjy7C0pSq3Eh6L9jBzJo-ZsY2T62tMIviNAY-VrDbeuW0JHchQxPCY2UMd4ro-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=HqdbFYQ857gDpU0XYKf2KY4nnec3qswPKUPcNODIN3Fzx9caQpVpLL1QEWdSKjEOevtlBBHYXPb4g0723tZlYUWStkkYIukJz-dozureWKsKvPh96ayl7qyVG8vd_-v5W1fqL5O8EA2BJ9ayn_v8k5Unnx96YhXXkY4uc0iiwLpnKmZWmWRiO19IY8M0oP2LhTxWQXdEUYcas7EDX5PvQWuQS2H2rjLdSAt9zhtNwHlzm9xYc6BiQs8iSqSeLeXIBkeiHheZOOxYk3QmM7X59B3mdFBU0O4S7lXr1CfRGso8rTEOpqliJ3pouRZofRxaDcFP_Zyn5TdIXa18tJ1ODY8PnZfbjwQ2bzK7Tuc5jhTw9_l2H_L5ClyVZ7A-bVPtlmFdXQJ1yfo_vislTaRRdbtMvHdsNHyzNImS9urvi_V5K_3INlIf-HjKl6ez4_jU2Nt_VVvM79BAd_S4ClbACoD7LaxiwwRUf_AWzd0Cw3ticc2HYZ0NNKdtDs8Mk9HLnIZCpZIVk93X5QCt3qplUbCaG3Da-eg2gRxKp4CRZpk9q7o4DYZQLLW-eheG0rLh7d0hpEHSXRvhpil7_W1DhEx5mM6YtVm5CE9fIWrQHSeOStbq2NOPTCspuq30vWzZr2GbNHN0-iVxIarScnyia7w27RRAvAWxmKqeP7PiNCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=HqdbFYQ857gDpU0XYKf2KY4nnec3qswPKUPcNODIN3Fzx9caQpVpLL1QEWdSKjEOevtlBBHYXPb4g0723tZlYUWStkkYIukJz-dozureWKsKvPh96ayl7qyVG8vd_-v5W1fqL5O8EA2BJ9ayn_v8k5Unnx96YhXXkY4uc0iiwLpnKmZWmWRiO19IY8M0oP2LhTxWQXdEUYcas7EDX5PvQWuQS2H2rjLdSAt9zhtNwHlzm9xYc6BiQs8iSqSeLeXIBkeiHheZOOxYk3QmM7X59B3mdFBU0O4S7lXr1CfRGso8rTEOpqliJ3pouRZofRxaDcFP_Zyn5TdIXa18tJ1ODY8PnZfbjwQ2bzK7Tuc5jhTw9_l2H_L5ClyVZ7A-bVPtlmFdXQJ1yfo_vislTaRRdbtMvHdsNHyzNImS9urvi_V5K_3INlIf-HjKl6ez4_jU2Nt_VVvM79BAd_S4ClbACoD7LaxiwwRUf_AWzd0Cw3ticc2HYZ0NNKdtDs8Mk9HLnIZCpZIVk93X5QCt3qplUbCaG3Da-eg2gRxKp4CRZpk9q7o4DYZQLLW-eheG0rLh7d0hpEHSXRvhpil7_W1DhEx5mM6YtVm5CE9fIWrQHSeOStbq2NOPTCspuq30vWzZr2GbNHN0-iVxIarScnyia7w27RRAvAWxmKqeP7PiNCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuQf6UrSOtxjsdaZUfcGNv8RkWsPeX3vP4P8r-7z0KkYWaY219otrBTdR-fcuhPE39HFHDfIGEzAvi3UpljW3BNEDekxD1Itf4HQjs0wTCMIDH5wv--FItNUVqSc6u09Zj4x_ZwY8g3iWWGqEExqTBM2cd9W6EPlCVJHsO-1DI-RDZ4ome2hPKhZm1BYZstLPlhuv7IxD71rB24IRplYNm1uY39SNtlOEwvRiVpJXrqkcsQOzmc2QI2yIz1GAppItvAGHMsZjdoNf8-x6s6CQsjJ5H3Bx05FTFarriDSbQDT3Wh7XSqKs8PPLlkVGCZHaxBhfPI38DeOSGu_MUc5xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=tKgodd__qvYWLEHUFWzZRbYuGWl_jl1rvhT4AtWoE8Zvx4wd2JmsUgofZ1xVhxKoYI-aYD4HxyqYqSI60ZHvxsFZQL-C4KFqEP01eRYJmf8K3A-PjjPehQsbysBWqsheKt_406MmEoDWEJi_21nn5Kcizc3dXFgdCJRRjV3okcBjQH5dZ6qH7ibZy56xu1s1uhX_ya8pJ0fn5WVL8AfrZ7KENIA1rld_7Gy7iL-uH4CJ5skiTrjL603ZrxNnCYC_wk98DRM9eDlLzESsvGURxTcWvty0B5kRI9nsB0Y-GV8T_2_WYDRrM5rcW_DBTZGo-JfOJsH0W3Gn4A1KYbM5TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=tKgodd__qvYWLEHUFWzZRbYuGWl_jl1rvhT4AtWoE8Zvx4wd2JmsUgofZ1xVhxKoYI-aYD4HxyqYqSI60ZHvxsFZQL-C4KFqEP01eRYJmf8K3A-PjjPehQsbysBWqsheKt_406MmEoDWEJi_21nn5Kcizc3dXFgdCJRRjV3okcBjQH5dZ6qH7ibZy56xu1s1uhX_ya8pJ0fn5WVL8AfrZ7KENIA1rld_7Gy7iL-uH4CJ5skiTrjL603ZrxNnCYC_wk98DRM9eDlLzESsvGURxTcWvty0B5kRI9nsB0Y-GV8T_2_WYDRrM5rcW_DBTZGo-JfOJsH0W3Gn4A1KYbM5TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSKiz9ERiEDxR7uQxgTqMiVkhdcUPmmrf-AYiZEKrzxfZzy5svILo7QbhSLsTAGRf_HWY9eGsYxKsSUFLS3fU3YxT9nlU19imrIa3COXDaTtcDzg6l3q9U6b_Bq1XuwBEDBe1MgwrUSsMq4XdE_4kjmM7EeQPyAiVXIeDeUtNbfQyWoTM8d6PXjT7_9IKnIYJFPB34oOVVV0Br2gNJ-s2Om-yJygdPuEUwW7OMhqmG5c4O14sQck2F0dRwYupV1SxUNqp1ODyjeD7YrcaNCVRT4sq_aMg6UamXF9LFOW_8nHNA5DDwVCkTlYdAbjtZQf4pJai41o6iIr9yTVl5DvaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=rB1TBhkf5LWG8ng9YDOX73Xr6do3yK965WtV8ULsuYkJ0v5oPYIi20cj1syoFPA_EZignRQSJe5n8EWBTGNBo0wAf6vAZOr_EY9vcCk9EY-dYLpWpsiZstAZjZ8s5e0PCpQ14s9bFuDfDwkl5GEGBwliMT36T9NIYGKIuM9phgmgXOyohOfDsAF5wCzSTAKX0dTsboH39afXi4hEcy-8LHS0IaVIikYO7AkbPSWUYClboJ1gK_gQwiianrVmeoNUG3hpOLEPc37JunUMlsK9MxWm1rQDIg0Y4_YLUuy8_Acqt4A4dKCvNWavGcYwo_7dpYL_n98cOTeYjdKeDH0dQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=rB1TBhkf5LWG8ng9YDOX73Xr6do3yK965WtV8ULsuYkJ0v5oPYIi20cj1syoFPA_EZignRQSJe5n8EWBTGNBo0wAf6vAZOr_EY9vcCk9EY-dYLpWpsiZstAZjZ8s5e0PCpQ14s9bFuDfDwkl5GEGBwliMT36T9NIYGKIuM9phgmgXOyohOfDsAF5wCzSTAKX0dTsboH39afXi4hEcy-8LHS0IaVIikYO7AkbPSWUYClboJ1gK_gQwiianrVmeoNUG3hpOLEPc37JunUMlsK9MxWm1rQDIg0Y4_YLUuy8_Acqt4A4dKCvNWavGcYwo_7dpYL_n98cOTeYjdKeDH0dQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amB2RDxAihpZZwXqEMXjoBKcHj1znLDkalGyAs2XaS4hA06jTPWiUs3IVf07r2ulFHq2kY3aJR1AovtHmGauKJQr2n1rwC_IMIJ1NvfGHLg9HFIHot5cL3lpf6J-eAdRKutA-nSBu_hq5EI7_10i4-_E-Fo5nZZ0MqqW_pHZ_oM2aEu0JnWiejZ45QGtwkdvmDBLuNQr8JvWu0qAeCJufXdRShlIjidt1PpcNXTTiATcseH1jnN2wceaZLsRtr51VI_o6J9z8sZ9aDKqIe6g0PhTo-La1maC79cFEzUzX4kc5qL30S1ctBnSviZF1X1F05V70zOds19p6zIywB2U_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfvBBgv62o4hAbiaorooAAxrgLAOMBqIuJIrjduJOQsNitqVtDxmONhQY0aH124LJKm-GlPrfQ0-HKKGjNfH2CQ0cNkp0WwjIR6jRzsWSUhJt9TFTHOvkYJQ3KHY5IoB06Gpgb12CPym-hWvHZ8Sbzs3aZ7GvMB1vxsvfUwVgbW3GxB-nHhBPprVzp6ih2yw8JBoUhIKGKNekyeQWCJn_W06YSnKvJBeDwnpp2zsR_dZGFVAgZwB1QuVbzqQGKhLM8Rwb79NG76G7OldVPMiyzwssgnhJ_yOO0s2aKitDe-Pg72t-lDyuvIjAfv10KhCvLlDA-OrETJJEqeaJ41u8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyKqBmJ-OTgS4UcV2yPtGu-ae7jeSTn_3gEcykN6U2BoOWqZYEhHga9xaLEtTXJo3UMtzBW4clQzZfR2w-EDMvY_HCUOJUBGvFkwfth1TCwV66Dkclb_7Vnbma_iRbDydZtcFPC1DzNsoB3_Azez1TSjuBIrP4WVpAQQ5B8sKNwLt4kDI3RU-81mCTGFmzYBrgM200NYNnoxO9m1YBUalwwnJNX3GnxABQ7LkNdGF0mQZ9_-4FXu2PtiSN2FVxVfpdfk_vCetW9W1axLAPj_hyOfZi4NkMBpyFvzV9OmmdcFK3_oGnFPPe_lCuOMyIsBHCNEYoZH3SESm0xnJihKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqnnEMxUi8CSwZYMVH2zIEnZm8NrlJn3mnXApk8iFpX_CKEYMQAQKNKijPe07kWJD24yV77Ld0lCysxHmFsd5TWcRXnVkutahd13mpzTkSuvkd2Rlaj5Y9JS2bfInak1XURry2T3tb6IuXAZ8h-0g9oJ2Vb_lQ33jvkOII-iOJsauGCmCERUD6JMDOqzjlY_qttlYw7kLspa-gaVcgNQ7o39bTB-RpAgsND0QC_GFKpJCQppFbCxhA4bSuheXLWVD976gNRm67ovYAwCAXCO8GZkn04pm-sEvLEiMfG6eyJKr-6UOctH4F-5BDZ9CSPzMOlTvgANcy-Dp3yTYEYXHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bu3pEoYDDYHJKD8XdqeEK53txtNqqQeULBK__0aAGB-WPSekquLn7O_EHWD0TLr2Z8EBIc8VeB_ifP_tPkWH8EtGt9QVzquBokvW0oT7r9n8wGkSd1zH3jjhhnLZbC-ujqb1PRxfffwqx66MuMdEPjrThFJtbe44luanO2_X180q805_vRFQYVa8pyVOFQonW_M93WpwqkeM1oCv3E1UQfumqiWRrPTMZgJqe9n4MwBPG7ILkKNjDuqfW0fRqRa2pRQsUSAYEfe9PPJ0_Gq9SKtESV1YMzcKkx9gOTiTw-ZZptTZK-DEvrRwqtTbBgU-9YWDMYIB0XiXCmUofLnizg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=s_ZWSeRP9KcezqDK0JYeZe36uhhfecroUn20kYP1dKAIKW8q2vXHLdIwIzmJonyhxGPUGVxEYnapDJE1kSw6knDwgQP4XX_9rWzSvWG0cgI0Ucbniw6oECkBNVtyXSCbhEMoQWOJDfqOzisdVwGxAP7VgoGpphX50sf6ia6-VUXpCoaue0bbzmx2FBQpOW2NYJZY-4gbniD74MqtOWCrFWdKELoslYxP83vjM8vCN3oRgSbEg8jDv2uMqd1nnXeJycYQlhITlD3VKnhrSwIBnJfZO8dgxjai12XdigoOGHa5v4vc2K5W_D5WW3KN9eSXYjXWKDt1zRSGAAL1nYJmvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=s_ZWSeRP9KcezqDK0JYeZe36uhhfecroUn20kYP1dKAIKW8q2vXHLdIwIzmJonyhxGPUGVxEYnapDJE1kSw6knDwgQP4XX_9rWzSvWG0cgI0Ucbniw6oECkBNVtyXSCbhEMoQWOJDfqOzisdVwGxAP7VgoGpphX50sf6ia6-VUXpCoaue0bbzmx2FBQpOW2NYJZY-4gbniD74MqtOWCrFWdKELoslYxP83vjM8vCN3oRgSbEg8jDv2uMqd1nnXeJycYQlhITlD3VKnhrSwIBnJfZO8dgxjai12XdigoOGHa5v4vc2K5W_D5WW3KN9eSXYjXWKDt1zRSGAAL1nYJmvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmMyulKCb0v9am1YrXuSDbC4sDtjN0-7KO03VUMYtr3gyWd5z7dd9fWkaEqqo7YzUbTFo8PE9JGouS85qmywSw_lsY9voRYV-yEuxA4I0XBy_HQW1tia97wWyY7BNNF0_L2lXftWMiW9ncQti1q__bPPbdYDsfxXQKNr-xZYlqRaEaiwDDt3dIHjU6AHv9ZgsziOH8TNvJsIeYvafG8pOg4Pa9mV4n6vA-LvhJRX6ydr75AglUrOPA7IdMONy5EuYqqa7lIpDbZ1HS0GMsdFgDymK6BS6kNyCVNvjVDVGN_dytJeMqeO6FFMcxT89Zl4nErEA0mvBwz70S4RHTIYkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmQAgudZK5Jfu69YMpuQf5g5sCV4V07ikjPkTBNmi08Odts9ydpp7An4aNGN8F2nDUeHWHB9yQFJZIKef_1l-J833oK_YzB-XKMmxA7f2Gkinq41m2hcDLFG8JMU8A2JSRdACZz6kwdhpwa7yIncKVNjY5f_VdMR4d73esBrqW3FgThS7jo3a_ji2fBVZUCs1nCWd_XG_DD3uaeFyijAAACjC8tecjvQkrGcgoCFPl5rHBSXGiYuglprWkZGrJF8fUgWpgngDGZ2cIb00Ne9HW3ARuFVii3hSEBCFQttQcW70qzUeEUEtlJR8gexfC6Elgtz21lfHSXSSVQmuyiCAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGDenDQcXud1fz-37WZwyChcPlleZ-Ldp8RhNiSTBC8pj23_yHaEAaVyTDQrLLN9R296PXQts96RV6hMwCDWK0eFnN_ZLg2oOQw_-kSk5a4ZtYzAzXHSWp7BzXaVO2NLoomXRLaA56UtApL5VQcxKxsdurkiqXFPSQdM-hBPQFoDeeQXIenZBZPebx9JCYPIoo_herggRRSHzUqaC0I2v0UThcXiUtSHcO4VAQMK1cYOwzmFBYt6Vcn3Cl4npUsTF_ABm6NB6BMbQzJsGyp3yJqF2tLpxZCgmkRsMPZ2jQLAKpGK2FN9FuzTNxEeQKh651F6nPIXaoSCgfBl_iVouw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYMyxFE56Eklm3k5Od95UproPQQLiRWSSC_Ej9Y8pw_JYW57OUV5YGZhWqsMHPjkoKJgodbYAZYs_YVnNg578aJvwlQTPpOJlTBAhVZOYyzfcc00DpyWKxjFEkiKp6LR7ndyNoGFmkKTyd3p4QsQVvBQLM-tyEA09C_dh2vJvrkbx1Q_wqERH1g8uMhqoAjaZwciMiX7WaCIaDI_U4Wh9r4IMMBZheQrOVu6xTeST-z1nkLDAqe4pmUkmqXjNWEsk-Dwg3g2Hoq_PKqhfle03Hxg2EpDlUDfqLZ9zd_z9pbpLp6kH-Zoj6x5OlrlXwnXjkPaQgtOxABHt46_2ES7yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYf92ofQ20i3zKNAdlyH6yk9WUcLzD2TwnUxpRVCr9BOYpSkAoaWpcMpYq_4LxcRaZw5LiCxTC0f4PmhIlPx1txpf26CxhMcki2kwoihEVtC4waWiQcDQi_WNTkw2FQTz0a0rGh70kjw5tQ7pvwbvdRpTJmFuDhrbhFYy1sYJcf86gGZ8Tl3bz3rAMp-QOir-ZkpH-_odtaRfJFZ2F36MGAyW3QDOdgLuHPPwVvPLJOZPEhCUhPLOJg90bYVGI_4_A8LWNcXcW9Sqn4Z7HZc3pD-XcBdZYFjV2COKzC3SzTW0EPYUj7tQanS9cpx6-WURW02Jse2LN5_P0j661Y5lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vid1MzgGNXLweDfgC6pBPccKNpMNWXEFloR9yaB2FbBXlpG_wbtQ_LYsVJWJ7bAdrJvprRzd-jVahJLqQ9FzYz3ASqUry00lwXR6EP7DZHm04OoWhz6msBuUdKa9K8robVV0RSR1K-RrF1VbQhOviCKE4bbp4DVj1oQfj8Xd_FhfcTeKy6PhUVbaZEul0fy_nhyzfbyw668q1SM_cx9wQYxqGfgttG2ocp1J3PEm_kF16YAlZd8BTQLtHeKXvvv7fZVHL20igCcdcdSRi1np3lERWnaryFxYJTNEwtdNbVrLcNEp5Gkcey0nakxqhORYWe2iXQ2NdISSeuBbxrHAzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVbK88wYn3bhJPYfHR956sqOlPoCmfubhBa-2hMrQxsk4OL6Du8SQ-29EpTap8L-nIrCQ5cgVpj2cdHnHNEDe6wKiBRCSCoxeo4Bx1s-AhDrN3zP2ZLeM8197H8pQj9QeremSHmVzyD5D51N34FlHTbMymrC0QchZlhsbvFNaDqK_3zhQvhZQhb2xRuI0L79ZAkOulTcqPtiv41ahLlBoimz9rjCX_i6wa1LSk5ltUnro1e9y7-7RRIzy-NW2F--XpNrFpdZmls1HjiJ2Xf4POx0PSHTIBQCb8gH9kkQWrNssH4TJvSwRyWW4csboQZRidIAycuKrBBY1J0hTbraQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDjVHY_iQVA0CUzicmHrHOYSZDa7pwR8hmrrpolhvqffD29ABznGfFxFrZUX4odvbj7EAIF0nMAw57TzuDNyZJ0FBV1d1_dXHfym0UaOvCTn_qiRqpNRKJeif7K-7Se0kJWjsEtxmQJaKYCkEDloYU309cawWPy5lGNTeunvtl9oafoKgXi5kVctwNUwXv8ikG0gNlUi7ZKVc1C2QsaaJwBEYOt8qNuBeteiw9_hIWlnONX_wpriBtVDSPPnYjLs8RzUiR69L_5w-NKWoqhej6YSSrr_JtbEtpIsypSoslwIhIsXV_whOEqRqL6fsP42N5503lyazf-zrdkL4L_0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPjWnWIYVevIWYPPXUXxuG27VwIgzxvLHq1gjC-3dghFiiAVSTPN0MVAQ-7BSlsX92F10n11u0MkXDeRFKfUypJ4CFeBKrkDeYuANf3o1cCHuYRvYGpi7ZpzIKuuyGeEnnJdEnuWz5Hv_D04H37W2hAMrb7nI35v9VI--cTi9qgM9UphRyKf_FumpzqBQX2OpycLV9RJc_tA_FnM1cmnBXzo088vM19cl4SIxdvL3o6MWHIbjy9aXXzlfixiq-eVdZqCoz7DAPFVuJhSri-_MZqIkrwqLCH1iY3AtJPrP4l5BtgT94tn19hldYUXc1hJ6zpWhoZ5bxFH4XIMoZme9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJCTaZJdXHzSqGrkf0vvLRWJHFLoiI5Kn5RS8HzOgSn3T7ad6PYjaWxBDxzU6uesq6-teITkLWpMbUZfq0pr7VfytzCwzn9aDWzYXeUSfdQ8ICJLoZhg0pk-W80oolSTXdRb2tW4NEr2-shRXVhwhjxrzaB3eoWX63S5Dqvaegi979mvKGNSaiRJ7oY6C_C6NqbpjvhsbDw09qvjqmXHS_gmlQpkCYCnBxtsIoLh4BwElDgPbDBtWMtvdg7Um5MncHDMs3k4kJSKE8Voxm5aRcUE4y5_qVbnIKFmEzU0eOwTSWOhFMUTEqcn0XdN9J7CJteGatMUWCLUnkw1KAJf5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Szb4WVLXgqpWcc6jIL9MdSd6hRTm-OT2anQGzv8d-O-tRK9h32O5nlogV2EzyN4i_4H86hPaLg4Vgloza9RNAicj6E7UONE50vLz6ntDXuEISO7ri0NE97guVhte8kQ0KwNzplPjjMfLr8z17NBy-jHN88pH81A7hqYF_sr5hVq0KZDxqOEMOBEZ8FAtUKQhT9qkqFVw2iq2dDEDm-kodm973MnV5n6uJ2q4Vw_ytCIJa4S4rUrhofj0RouberUH1USLHSM-2bg0gMF_MpOiP9Oe4d1aqe_7KJscN5bCbkDb35fjld_FADv2ERMaynQFzqYge335yaPUE--ZaZSqlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGLKCZ_NbPrDXyMXtCh5QVcLaPNw06RBRv-kwJlIUehRoZdritx7ucK-Qq70oTkeU-SijQnzBjEODPy80w2INtPhl3SN5TkCUFQGVtZ0Lj90LkqwpnhDhumOrwhHhahL0iQJcKYRDDCUgisjhf11_6DshIcDNbH3lTnetS4mOFBr9rrSNxtYYiKaBtUzSAaz6K5ARJ7BgDFpmE_MQpBtNLg95aYAUmJozVt2FAFc-Z-G8EkFkT_h9aNsVgVNEA2-ja1pxp7-jYyGS6ytENofb0S4B1WXKhylR1FraexiuTeJ7X1fbq7NKhKMmz65pC0KOKRDyXQJ-XIX48A4ETweQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ5xMWS6kJNQVXHQrKrOAdfYXeuqC23P_UTixzmHrmGJV5ZvfjRwo_GpU_HXqEpcWQQoNvYM0iq0cwduks8nkeGC_imdIDmJAx2aVwc71lG_DZmoVQjuKGHdbL0pyKWKVR2KEsCDKKGXlCJ_lTRjjxwREvp6gKCQrYg0Th-t8ksr_8nOHNKKiAFf4leb-6hBQgmQuN0RKxS9QxwBJMpkq8dLjFF7GQYiyQELux_exXwE3wPbD5jPiAq73RPocjQ149GQLwDbtX9AWxFERr8h5bX1QOQcAc4JtSXMk1cZPikwmoeuTs9IED3tE4S85etYzE_VJIjj1vdoPKz-IQsenA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cASHGqQfhsaBnEfqqmswwGcwebt2Cv7JEq8IQx2FsTDywK8fVK9G2sKG3PK3XT5Gwe6nFc4oOSAwlSw2gmRUh-tOhCjOqrkqSbL1fk22QJmR9tSLYKc24Ljhx29_GGbkkiUImTDVeiMgVbkpv65TgjXVH2gGHD2iD1kNahuc9mnEXi_mh_rkVGm830fDpXuAhDBwywukZG17ZolBxsqsL5ywugv9Iz5-sZRRG-Y4dPYYAhb6JUqviSuh-1pHJz0CaCQQTl2kq4Jl-6vGWRkOzKOAuWOGu7D0ABVQHSVcmTLQ10Exggd3RMyyTFHpmlHCbsU90big-s31UAdSskglCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW8qNxwvjFPVRk-PHHyq9SH2RmwcpluMxQIIZJdjJrrwACGaorAX3jeEiMu5PtGiOQayL3Biwq5nXJ8bvXbgxVo-WXriStLTrtPUT0emSKk9TbgdQQuRcDMqyOh0j-co6UgLB6LNDRaCmB7k4LLY7E3KUXSLiOo86pAKT2jLyr2ySwGzskoDWpwgdiuExJuttGCEAFb1qqnRXhVKdDFnyEshprAoZrwrBuHNka9E54gnEI3R-4smKSc6fxrbrB8FemrCUnWA8M4FncU0Zod0d2iSKRBQclgEsDyf-Sd8M-8knA52BdbXQ0EgH8l8MtckWaF0FM8Ma0vrKHKKmua-sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUfECepItvB-omVAyhNIQu5aav15UdkNzkxWuRjpcdmW1Xf9AKoEVgeDiEGTZA_A6OZvQkANSbaFjdhMYkIndyXINYrk0cqtCm9htAZjoKCufEggdNhlIh3vctu9cH7Yitvz1tYfMAWNaBzyd2rhs8L2oOgc_aguk_j9xuBgP1yJl8r7PCBnWkIJkS-75OnzyJtFMswaFa64KxL8jlE-7qHck_wBa0YDH3XFHxpm1eNRm5B9NPtN_D1gL8gC6ErG2bAgtMWMWChg3F70jTCIg2DcyMGb2rB28fP4MpF0IQMEZ7o2GQcz75y2usx8_AW1JmYVjzBt79GIjXPzxyo7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvKp6ioAwP8t4-GArDV3H7f8KsMsgJSlXYSPxP4dH-xgzW9SI4cGuzuFasEDggN7qr6_5BKCh3i5ZvlatZw7Yld775yBf8WSzgzwVkh_sA6ndaZxcRJ7ais2OvSG8oiF-RzN-_daYo5h2l-3BqHQWWoOWNQbm3Lv9AUelgTk4-jOtHTyYRb1oH20OMalVzBYTrAegfPwPZCXCNC62GB2uwWoKK0hLe7DbfCDOE1e9YZNlw7Fff6ETSpedlWJ46546TPO3J_xNhoSJQlGsJabMrCkcEvMlIe8n2PyjEXNSQThIJVkzgwSn48Q9ds0KXwtX5k67L7tqwlHcdQqJSqdew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp4QyS5fSOxNbVyGK9wUef4uUEP9-St4eCESAj2jGB2CkbgXRNBW1-mqFUQaw9zca18S6kpu9m2QLfdcp3hOuu_Y-6eosGn4ZzLKxuNT7cDQ5JyoZw2i0h98u7CmZ8ss2A3EHtsYfXp2cdtHtEHyebGynalsj1WpYFliXT9Cv1wzDnhda9DgqTO9edjhm2g1cedyGmwbuG_2NsyQHNshhhHN1r6bgHALKSq0QSK5zZzp7SueoGgm0agQ6ROUoQOd99igfvq1XBFXBBok_MMo281MSCoSJVHy_DVRSA9HH4do4HghgAzO6RKZ5FV8iNc_c5yP7XDBJbTAsEp6kE29Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=OZYd3DnBzBSaIpBUbBNiFEziW4MFFBElyI7g6ur8W_xbZR1f3H21iqu8vmeXGNuVEyqy4QMf30VGTNej_wpIoUFxxb2BQkyFKRUKRVZ2tru6GJMU52zYMKCxq28p0f0BRkDiTwNmgPrJguH097U41L30_MOKLDGRWq-_yRlubAk2Qv_N14LE_uz-lv-7mMm02NP49Cw5_oIJZ7JFne7u45qIcO-3XgGFFvuFETsz0fsuwVDTG2-ne1Gz1S-07RSBypTjn4zoNXXZCD-qtMmz3S1C2tn4DpFQVV8jxxr1vs7EqmKnqorVXF80fhjVuQxoQe7As5_z_PWdm2fNzM3tfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=OZYd3DnBzBSaIpBUbBNiFEziW4MFFBElyI7g6ur8W_xbZR1f3H21iqu8vmeXGNuVEyqy4QMf30VGTNej_wpIoUFxxb2BQkyFKRUKRVZ2tru6GJMU52zYMKCxq28p0f0BRkDiTwNmgPrJguH097U41L30_MOKLDGRWq-_yRlubAk2Qv_N14LE_uz-lv-7mMm02NP49Cw5_oIJZ7JFne7u45qIcO-3XgGFFvuFETsz0fsuwVDTG2-ne1Gz1S-07RSBypTjn4zoNXXZCD-qtMmz3S1C2tn4DpFQVV8jxxr1vs7EqmKnqorVXF80fhjVuQxoQe7As5_z_PWdm2fNzM3tfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKDxd1h6Iz8i94O4l4QCGxs_6RgCoNRDQxI0NN619eKm1tvIjpjVEW3-EC2GZsOmQoYsqounCv0_L-De37Bb0aHM51eBYCb3CzOhwn6dzNRVrT8y0cRSSTZ3RR0-bM5-AqKLkKwapS-beTL2th9fOeyBRyg5_FjwP7tGlvMnhgYk5-94PCXo5NEBnttPtiiIPFxwhfhkvulUTpx0FLe9ujmlAsPg3k7UokkAAdz8sqImcsGe1_06Vwd-AP7l9KXkWN8q2ruSVXmewCoeLSJiWVBPK0G8IY035CZ9FyX2QZ11-7nTQFy-ug0Gx_FZ24_KqY4oMqZxo8yufi9FLUKmNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3w8vMsOYAgKghmMLR2wCQElOrCDilophL5JrrDQykD-oyAQsn-_779gVeVoY5G46pkd77zLscJtWjE1qID-i3KFfzxSPM6N0CfO2BJUcB44eFopTt0pnLwhGDMvqGb2IFBhNjqQTyAjyoGfZ1fk6njiah_SP-xfGO0oydHUmQggQqkcsYMIQK0uyLxpY4hNSOJVEGh1Aw_id5qZripzlmwBTF1kAoIvLIm8Dma9zryE7lHDWKg3QeActqsigwfgMW0kw2LhreB7YbzjshX9TibtZKMYYTg00bxTLl_e2GSLdd6j6KYP9lMYz8sanK051v1ckHBbFnTHZfc3IldQlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=E1L2UcQ-dpDZQK_Go3pC2rNbr3zdki9XdPefTL5GjJYQkFcufBxWtlEkY7X7DThRBzYPqOequnCFu0za3V57bum_Tfa6swTjjnSczp0lYZEFLIw7Zon9SuOY3oOm45cvV-fMwCdq5fvHI_C1urRrfCEH2Bi7EKeM2EjtEZmUXqQrXvlIDmoliTYg6LOQMfMNtpJ4jcMsnvVirsi7lhaSr-RKs6_xVW6Vk20TD4TXlsXjRCKUfvAZlGuHcD0jQXfvt8chjsXm1lYIYeztBQ2vjuBLx4mTKI9SPv2V2qwc4RDNvDLo3o5jVcAWzbd1e7AW4JTmnk-C8EFcHP4aIIkvBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=E1L2UcQ-dpDZQK_Go3pC2rNbr3zdki9XdPefTL5GjJYQkFcufBxWtlEkY7X7DThRBzYPqOequnCFu0za3V57bum_Tfa6swTjjnSczp0lYZEFLIw7Zon9SuOY3oOm45cvV-fMwCdq5fvHI_C1urRrfCEH2Bi7EKeM2EjtEZmUXqQrXvlIDmoliTYg6LOQMfMNtpJ4jcMsnvVirsi7lhaSr-RKs6_xVW6Vk20TD4TXlsXjRCKUfvAZlGuHcD0jQXfvt8chjsXm1lYIYeztBQ2vjuBLx4mTKI9SPv2V2qwc4RDNvDLo3o5jVcAWzbd1e7AW4JTmnk-C8EFcHP4aIIkvBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=bEj2xIdfPm9ePNh7PFR0s3efaVBrnpfN5BvAVZPblZj65hzRl5j9CwlGiy_mGRnMMPsWal0tACLcQb5MtP_6YAzOt7DG3kLh9C_J0vo1DXqLgPwsFp8qi8WBuLdlwtzKN0EbaOGmsiNrECCF69f5RUHv_5MCfP0-WfkjfdAytIW5B3cKJh8e2ZQ9N47QtSf54a7OSk-XlQiefwg9kNY_jLe2o-DZihAj1zjp99_RxHQ2HSpqbn2RADgc_SunupLWnRjmK6Gb0Ci9_cn8PvZ4BpJN_395BIpodoYKX3nLWZATm_Y8FzMRtsIYOlQMeBzmbZxxYd57Oe0pxce7KGmQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=bEj2xIdfPm9ePNh7PFR0s3efaVBrnpfN5BvAVZPblZj65hzRl5j9CwlGiy_mGRnMMPsWal0tACLcQb5MtP_6YAzOt7DG3kLh9C_J0vo1DXqLgPwsFp8qi8WBuLdlwtzKN0EbaOGmsiNrECCF69f5RUHv_5MCfP0-WfkjfdAytIW5B3cKJh8e2ZQ9N47QtSf54a7OSk-XlQiefwg9kNY_jLe2o-DZihAj1zjp99_RxHQ2HSpqbn2RADgc_SunupLWnRjmK6Gb0Ci9_cn8PvZ4BpJN_395BIpodoYKX3nLWZATm_Y8FzMRtsIYOlQMeBzmbZxxYd57Oe0pxce7KGmQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=HcHiia-hXTwPVdV8GCHueqAXdAV-XLJ2D3-7lhvAqfMXafM3hBSfJ0JoXR6-3DY9p72MfQXfCERTd4vm1D7wjF4aYqG97SztSqf2W-C-JGVRQdVf799mzaVqAIdsw3q0PJmSb3Y5Bxhdl98mnyjd_Pta0Xk3LEvAsINrvO6uXm5S3A0zkzEWcwI4m-UfyPA16H65LOkedA8NJkmt7FWq2yCgzjdU4NlMayRT-EGqPzi7tg1FEdm6ZZMt5H4qaFQgvK7d4UqkL1IfkEo3A5MQXoRqze4lViDrOm7W6v2VWEeJP55gnvWimFH_lQynHmzI8kmRf8yCNRq-aCDwEfZOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=HcHiia-hXTwPVdV8GCHueqAXdAV-XLJ2D3-7lhvAqfMXafM3hBSfJ0JoXR6-3DY9p72MfQXfCERTd4vm1D7wjF4aYqG97SztSqf2W-C-JGVRQdVf799mzaVqAIdsw3q0PJmSb3Y5Bxhdl98mnyjd_Pta0Xk3LEvAsINrvO6uXm5S3A0zkzEWcwI4m-UfyPA16H65LOkedA8NJkmt7FWq2yCgzjdU4NlMayRT-EGqPzi7tg1FEdm6ZZMt5H4qaFQgvK7d4UqkL1IfkEo3A5MQXoRqze4lViDrOm7W6v2VWEeJP55gnvWimFH_lQynHmzI8kmRf8yCNRq-aCDwEfZOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uv0PCthcZZx637T_rHizbs_wNue2O3mD1QZhX4u5aDp5HTwS4VTz-fiuEcV5Nj2zFs2qTOyf6sWtl7QVy6jS3-C36rulH54TP0pJv-kDbLxmDVxmBMfa_Znu9nZlwGLQDgysAaJUFHRe0gegBXz4jI70o-PY7IHgZu4XnO8FlxyjRi9X_6hD63SucQwy1kCmuOvhRNqjRPoi_2dMEZt1wUFnEvyrjR1reD8pL-HosFbNZoZe4u88AWihFyscuomWm2ahALuihNFKXZWfKD93JYzjujB3OURAv67mKIQDbkrhQs1NRnPGoZvnlJBKGYb2AXcaTSZuL13hPkphmnMsAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=Rt_H_WXR7Hvdqq1pxZ2NCUxCp1jJ0hsarWEg_SFx0cRBhHZC8glMlyFojyn-zJY0dR0_XIdpP0UxiypGWuoxz0ZqU84CYlPv0L0MWjWeCVVJyZw1OMbxDq0CdBRxiBFoS9a56RD3kQxAHCjJ0Xu81MnGJbfrBBoU296UlcXL4_ecNP-92I-X9DnK3q9x_72WjYRR1CXRz6nvwLMNVhwDtw5Eyf57_mWNl4Iq6a8ZAc81hK83S6-yGeVlwS3yNKmhted2s3hJgCcV9Cw91biDLXxpN48RKxYcc7q8K9P-QvczMw8MRhJb5BJt-oOl7JkdPNNcC3OdSzQxyfYKUsjerA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=Rt_H_WXR7Hvdqq1pxZ2NCUxCp1jJ0hsarWEg_SFx0cRBhHZC8glMlyFojyn-zJY0dR0_XIdpP0UxiypGWuoxz0ZqU84CYlPv0L0MWjWeCVVJyZw1OMbxDq0CdBRxiBFoS9a56RD3kQxAHCjJ0Xu81MnGJbfrBBoU296UlcXL4_ecNP-92I-X9DnK3q9x_72WjYRR1CXRz6nvwLMNVhwDtw5Eyf57_mWNl4Iq6a8ZAc81hK83S6-yGeVlwS3yNKmhted2s3hJgCcV9Cw91biDLXxpN48RKxYcc7q8K9P-QvczMw8MRhJb5BJt-oOl7JkdPNNcC3OdSzQxyfYKUsjerA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMDT0GPebxU4DOZ69QZm4Eww8evGsPZX7IE6uB0VmEFOIiowUDLw76iLguqucKO_K_GK4bSWkpFC_5szULdLkQMql2GWBnfaBDjJMPIx8aGDQNoGo5mlFn_RNLdUDMPdqfksSFC-eNFAFdHFTxE2naVYiU14qyvV6C0R3-V1RToaOlmcyAkKisk4EmexblXmyab9lPzFdOcS8T2WHEBKrl5UPmxgxYJX9rHfNBqsWtCdTEbU7YylCcP2du_XSGbnfeSP98uYcjHtbdqozHcB4pNyb_R21AnQvYYggGPFjMyuC6txc8HcwiDbbWHOzNY0R7_LtpT384mezYubcEUmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
