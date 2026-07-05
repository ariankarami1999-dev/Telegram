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
<img src="https://cdn4.telesco.pe/file/UG-LK1EYlWz9COmr4lP_sl9h8ykmlVWAwHCuIFFKaMqztIgcKkaX-5nbUv8gBaP6AqH7RdPhbGFRgDPhdIu9WBEHo6tbq3lMMjX7zYI7yJjotft9deY2naxxMn-UK_ecs-XkvDFVD9IlBMFDDarMKG0UMUsvqQlCJY36JL1KaPobpsTh_eZK7xu7jvXiJgR8cQY46wJLX8-fqll8opRLakxSIqDzoKciXa8-zDYYfBfnosI1H5Vk6wV0WlLR-tj9aLd9gcfKgz-nCK3q6H0KC-0J0vx2vjl6VKXq1Yv5iEjzAjEqNQhVIj92fsQnerMW5v3I63pM5JacN72WzKcBkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.7K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 15:39:41</div>
<hr>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">https://x.com/ArchiveTell</div>
<div class="tg-footer">👁️ 653 · <a href="https://t.me/ArchiveTell/6723" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دیده‌بان لیکفا منتشر شد
🆕
افزونه‌ای برای مرورگر کروم که هنگام بازدید از وب‌سایت‌ها، اگر آن سایت سابقه نشت اطلاعات داشته باشد، به‌صورت خودکار به شما هشدار می‌دهد. متن‌باز، رایگان، کاملا محلی و بدون ارسال اطلاعات به سرور
👍
Download
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/ArchiveTell/6722" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sikz6I5phaCn4qDTjGbKKdLO-0WB0ezE_demJFo7odX1iLVpjNeibdsY3Jo7043FoGPyW8WVKu4qLlaIv7BgI55ptKtkOuNFxraeG9S0kA_jsH3bWAYLwitT-PFgH9IQIh8Zo7ka9OZt0KgfIUaqgNTs5uD_bLi2T-6WxHzUQP5xIUb2dh0FzpnajG3zWe7g5cm_0F5w7HNkoSrWuWyYOlp70eCV6bRu2ga1682c-ZDqcTXASKIlJ-QfHA9kBInB1avQbgBZ-NtFWgAPMxtfRZThE-m5rXukmOGa8U_9TELpC7EeB3LiYiC8M0_FApM_iiXBDoodgVkfvFGxadQaZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
سیستم‌عامل شخصی، مستقیم توی مرورگر!
‏یک پلتفرم متن‌باز و سبک که می‌تونی روی سیستم خودت بالا بیاریش (‌Self-host)⁩ و همه‌چیز رو کاملاً آفلاین و امن مدیریت کنی.
‏
✨
چرا جذابه؟
🔒
امنیت مطلق:
داده‌ها فقط روی هارد خودت ذخیره میشن.
‏
🛠
ابزارهای کاربردی:
ویرایشگر متن، ضبط صدا و پلیر داخلی در یک تب.
‏
🚀
فوق‌العاده سبک:
بدون نیاز به سخت‌افزار قوی، فقط با یک کلیک.
‏
⚡️
راه‌اندازی:
دریافت سورس از گیت‌هاب و اجرا با داکر.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/ArchiveTell/6721" target="_blank">📅 12:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🐦‍🔥
اسکنر قدرتمند سیمرغ (SIMORGH Scanner v0.3.0) منتشر شد!
🚀
اگر برای کانفیگ‌های VLESS خودتون دنبال پیدا کردن IP تمیز کلودفلر هستید، اسکنر سیمرغ یکی از بهترین ابزارهاست. به تازگی نسخه 0.3.0 اون با یه رابط کاربری وب بسیار جذاب (نئونی-رترو) منتشر شده.
🔥
ویژگی‌های خفن این نسخه:
💻
پشتیبانی از ویندوز و اندروید:
نسخه ویندوز به صورت Standalone هست و بدون نیاز به اینترنت اولیه یا نصب پایتون، به راحتی با یک کلیک اجرا میشه. نسخه اندروید (APK) هم با بک‌اند بومی Go نوشته شده و کاملاً برای صفحه نمایش موبایل بهینه‌سازی شده.
🎯
تست همه‌جانبه:
می‌تونید تک IP، رنج‌های CIDR و لیست‌های ISP رو اسکن کنید. این ابزار دارای دسته‌بندی لیست‌های آماده ISP ایران و بین‌الملل هست و حتی می‌تونید لیست اختصاصی خودتون رو به صورت فایل txt وارد کنید.
⚡️
امکانات دقیق اسکن:
دارای قابلیت‌های نمایش پینگ (Latency)، بررسی مجدد (Re-check) و تست سرعت (Speed test) به صورت مجزا هست.
📁
خروجی حرفه‌ای:
در نهایت آی‌پی‌ها و کانفیگ‌های تمیز رو رتبه‌بندی می‌کنه و خروجی‌های مرتبی مثل best_configs.txt و clean_ips.txt بهتون تحویل میده.
🔗
لینک گیت‌هاب پروژه برای دانلود نسخه‌ها
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/6720" target="_blank">📅 11:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=rVsFsmg4Zu-0f4tjvW26zYH86-u53rNV7wyYv-Bovosv-emQplVOohtsOfL-LLIqTluL59VQeBBw8IrxWlOUgdLRceI0HO3K53PnQJUwbA5j-mDXDCZ6hohTP5dEdimVMv921LSeTy2Y8FRb83RHi3iRPq_EsOY6xzREfkRnXXVn76n4VOiP58I6CUZRxSLAsRntdWKErf0A64H8QzUgCFToq2RKZKMesPlmau-pKrc5p4lTi2ZPCJ43Z9xNjykmKpm6MOLFYi0OJFxICHsw2kVOaWKMgeCt3lYYGtjK0FLpsB3YoESgvX9tEWYgEeSLm9_vhbe4a9gTPwiElbA-JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=rVsFsmg4Zu-0f4tjvW26zYH86-u53rNV7wyYv-Bovosv-emQplVOohtsOfL-LLIqTluL59VQeBBw8IrxWlOUgdLRceI0HO3K53PnQJUwbA5j-mDXDCZ6hohTP5dEdimVMv921LSeTy2Y8FRb83RHi3iRPq_EsOY6xzREfkRnXXVn76n4VOiP58I6CUZRxSLAsRntdWKErf0A64H8QzUgCFToq2RKZKMesPlmau-pKrc5p4lTi2ZPCJ43Z9xNjykmKpm6MOLFYi0OJFxICHsw2kVOaWKMgeCt3lYYGtjK0FLpsB3YoESgvX9tEWYgEeSLm9_vhbe4a9gTPwiElbA-JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
‌GitFut⁩:
رتبه‌بندی پروفایل ‌GitHub⁩ مثل بازیکنان فیفا!
⚡
‏هر توسعه‌دهنده‌ای تو دنیای کد یه ستاره‌ست!
🌟
‏این ابزار
رتبه ۰ تا ۹۹
رو بر اساس:
‏
🔹
تعداد
‌commit⁩ها
‏
🔹
ستاره‌های ریپو
‏
🔹
دنبال‌کنندگان
‏
🔹
زبان‌های برنامه‌نویسی
‏بهت میده!
‏
ببین به کدوم بازیکن فوتبال شباهت داری!
⚽
💻
‏
👉
امتحان کن
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/6719" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwLYwDO_hqUCu0FfctSRJJLf9yRLvGymrIXKdY7s8KClzKIyszBYvnlWyLin9mo-eBKfz_b64YT_HCfgwS1XW-RKCxM7KT-jozm8jea68ntkesWpO1eI93UNyc3ML46mXj2ALxgk71WrjrYqBrajqUbYBLM9D6MqIwUq_rYzDgON3TCgWFa7gkCkeoSNcVsLcW_jxvgyUd-vKXMxn43Kf5vLtKKUZFqqFwu0agMEStzAka7CGHyvgxjMJPTIqvftKQjqiPBgUO88mLpN0-u2MPx4C9_udwLWC8O70pSRmkET8CMtmx0ArHEVlB-_SJYhcuI5yHRJRbKmT6Ki-DUemA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
‌scrcpy⁩
— کنترل کامل گوشی اندرویدی روی کامپیوتر!
📱
➡️
💻
‏
✅
بدون دردسر
: نیازی به روت یا نصب اپ روی گوشی نیست! فقط با ‌USB⁩ یا وایفای وصلش کن.
‏
⚡
سرعت بالا
: ۱۰۸۰‌p⁩+ با ۳۰ تا ۱۲۰ فریم بر ثانیه.
‏
🔊
صدا
: انتقال مستقیم صدا (اندروید ۱۱+).
‏
⌨️
کنترل کامل
: موس و کیبورد فیزیکی شبیه‌سازی میشه.
‏
🎥
ضبط صفحه
+ نمایشگر مجازی.
‏
🐧
سازگار
: ویندوز، مک، لینوکس (بدون نیاز به ‌snap)⁩.
‏
🔗
مخزن
:
‌GitHub⁩
🔵
@‌ArchiveTell⁩</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/6717" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏
🚀
‌Arvix AI⁩ = جعبه‌ابزار کامل هوش مصنوعی تو
‏
🧠
متن:
‌GPT⁩, ‌Claude⁩, ‌Gemini⁩, ‌Grok⁩
‏
🎨
تصویر:
‌Midjourney⁩, ‌FLUX⁩, ‌Nano Banana⁩
‏
🎬
ویدیو:
‌Kling⁩, ‌Veo⁩, ‌Seedance 2⁩
‏
🎧
صدا:
‌Suno⁩, ‌ElevenLabs⁩
‏
🎁
توکن رایگان + دسترسی به همه مدل‌ها
https://arvixai.net/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/6716" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🚀
آموزش دریافت ‌API⁩ رایگان ‌Nvidia⁩
🚀
‏‌
1⃣
ثبت‌نام اولیه:
‏وارد سایت
‌build.nvidia.com⁩
شو و یک حساب کاربری بساز
📧
2⃣
‏‌
شروع تایید هویت:
‏پس از ثبت‌نام، روی کادر زرد رنگ بالای صفحه کلیک کن تا پروسه وریفای آغاز شود.
⚠️
3⃣
‏‌
دریافت شماره مجازی:
‏به سایت
‌2nd-no.com⁩
برو و یک شماره مجازی موقت و رایگان دریافت کن.
📱
4⃣
‏‌
فعال‌سازی حساب:
‏شماره دریافتی را در سایت انویدیا وارد کرده و کد تایید را ثبت کن.
✅
5⃣
‏‌
ساخت کلید دسترسی:
‏به بخش ‌
API keys
⁩
برو و کلید اختصاصی خودت را بساز.
🔑
6⃣
‏‌
انتخاب مدل‌های رایگان:
‏به بخش
‌
Model⁩
برو و از گزینه‌های
‌Free Endpoint⁩
استفاده کن.
🤖
‏
🌟
برخی از بهترین مدل‌های در دسترس:
🔹
‌GLM 5.2⁩
🔹
‌Minimax M3⁩
🔹
‌Deepseek v4 pro⁩
🔹
‌Kimi k2.6⁩
🔹
‌Qwen 3.5⁩
‏
بدون محدودیت توکن
🔓
بدون لیمیت روزانه
‏
♾
40
درخواست در دقیقه
‏
⏱
🔵
@ArhiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6715" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=HXegJ9wFEgy98Tp31xR3ldGjnaNhUPpun3RLWheSYzNAHAzG51FgulqDZkoKJr-C1lycNeSEvsmuOfsmtEiReOploFNJ-bMHuGnaJsPRStQp7fvVcrFkGjPh4LMrxnO9zAKqSM9JsgdBssPKfbQjgYFFftmozRuDR5BAxlqWX2QPHeKEOJ-eVtZr-bmq91QUxoNYGIIDtxQtscUmjVEAZMwqyEMaCB8CIzPUEJFCgvupcxdWQqw5gBf7IW8sQpTPmP8HS1f4-HHONyINburIFq1k2SQ5KwjhUpCF7F29stdgoFQkeoJjOtlPB3OXKKs6zjjpXIbuTTtkZRn40bq8qD4iZkC4oxx3cdHZKeEG7AqsKGWspMyxa7JnhEIDr3N_YiBFCsVYXBXuPfX7wGJ-g2mjdUXV8pdIXGrd4jxalH2MaAyzsXheyD5hu2KtxGhq-4bzat1Z5bXd2qeh5KJKmKfJX9HgZjwyUvV5I_P_UMvnCnuEImYtHIprJI4rf_v8bpxft_nCR65jiSIAe-BeC5VTDU0HcjqInW9swHYYOkLwDaOflo0FkeHUkyKtVNB6lDsQedUNM8DzyCF7GsHFmWs0z5ZDzknNdP54IGgIAkt2uh065Oy6uuAWbhvovQJp2nl_KNmYET2TqRSZ2Ki65IHwKAkIAzouFmyHcYjWd8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=HXegJ9wFEgy98Tp31xR3ldGjnaNhUPpun3RLWheSYzNAHAzG51FgulqDZkoKJr-C1lycNeSEvsmuOfsmtEiReOploFNJ-bMHuGnaJsPRStQp7fvVcrFkGjPh4LMrxnO9zAKqSM9JsgdBssPKfbQjgYFFftmozRuDR5BAxlqWX2QPHeKEOJ-eVtZr-bmq91QUxoNYGIIDtxQtscUmjVEAZMwqyEMaCB8CIzPUEJFCgvupcxdWQqw5gBf7IW8sQpTPmP8HS1f4-HHONyINburIFq1k2SQ5KwjhUpCF7F29stdgoFQkeoJjOtlPB3OXKKs6zjjpXIbuTTtkZRn40bq8qD4iZkC4oxx3cdHZKeEG7AqsKGWspMyxa7JnhEIDr3N_YiBFCsVYXBXuPfX7wGJ-g2mjdUXV8pdIXGrd4jxalH2MaAyzsXheyD5hu2KtxGhq-4bzat1Z5bXd2qeh5KJKmKfJX9HgZjwyUvV5I_P_UMvnCnuEImYtHIprJI4rf_v8bpxft_nCR65jiSIAe-BeC5VTDU0HcjqInW9swHYYOkLwDaOflo0FkeHUkyKtVNB6lDsQedUNM8DzyCF7GsHFmWs0z5ZDzknNdP54IGgIAkt2uh065Oy6uuAWbhvovQJp2nl_KNmYET2TqRSZ2Ki65IHwKAkIAzouFmyHcYjWd8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تبدیل ویس به متن تلگرام کاملاً رایگان! (بدون نیاز به پریمیوم) با هوش مصنوعی Cloudflare
https://youtu.be/Xq7e2k3qlqA</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6714" target="_blank">📅 02:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستان وقت بخیر و خسته نباشید
این چنل زاپاس آرشیوتل هستش
داشته باشین بهتره
❤️‍🔥
ی موقع اگ چیزی شد...
https://t.me/FOSSArchive</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6713" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=tE37zTt8JmEVYx7EWp2M9UNxokScJr9y191g-WKMdsgFeprILtJ5VorI0pmBz5caZ9VDfI5rwWiuC_XffzjKvqDdHhNUL1832s1KAfK7HMqWlTvPsLLAXeuOZQ2YXnAs-CNlFxN3yzoKGfh61_hf8m-oAQZ9FtLqAlxz31Q6-MOLQ7ikH_yBavkyCYMO1L5Ue7xOXdfgT5V97NuC9vXqyllPbbVCsPl_bqP3mrn8VnVoENhBFApLodOt0l7OwVfHyCI6EakLGdeGAy-r3qVGBsNgfnQDo7X2fVLVVRQOXogwE-S68DlfH89Gn4w48a14uobEW2tQUnHXC7f9Oi-D3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=tE37zTt8JmEVYx7EWp2M9UNxokScJr9y191g-WKMdsgFeprILtJ5VorI0pmBz5caZ9VDfI5rwWiuC_XffzjKvqDdHhNUL1832s1KAfK7HMqWlTvPsLLAXeuOZQ2YXnAs-CNlFxN3yzoKGfh61_hf8m-oAQZ9FtLqAlxz31Q6-MOLQ7ikH_yBavkyCYMO1L5Ue7xOXdfgT5V97NuC9vXqyllPbbVCsPl_bqP3mrn8VnVoENhBFApLodOt0l7OwVfHyCI6EakLGdeGAy-r3qVGBsNgfnQDo7X2fVLVVRQOXogwE-S68DlfH89Gn4w48a14uobEW2tQUnHXC7f9Oi-D3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
ImageGlass
ابزار سبک و سریع برای مشاهده عکس ها در ویندوز با پشتیبانی از طیف گسترده ای از فرمت های فایل.
• پشتیبانی از بیش از 90 فرمت: WEBP, GIF, SVG, AVIF, JXL, HEIC
• رابط کاربری بصری با سرعت پردازش بالا
• مناسب برای کاربران عادی و طراحان
https://github.com/d2phap/ImageGlass
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6712" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423195fff7.mp4?token=sGcZ5CvPm7-nnc_QWX659-CxZM2FxvolPmqekv5a9Be2aDU7xP8WcFDegcyUl5G-DelWvdEvH5W8vRveHUDdta8ao2X4nLqNhI0WtkFxUgQ5lD73MQtobgLqSVdS4FghxYp4JGWHdRgnk1tczMLRXwCt8vd0-IvSL7ieP-brpvOrQ5cmwP7bo9SJAG4RQusSRlbVJ9bgqfIE1xYyxhvG9B2JMtDKividreqZc474TxWQsWJfAkUe1hSTlthc-2PeYglOiK4agOJv36NkcDbp2FbMGeHRM8n3IXi6cK8kW1pzQ8-c94Eusx6AmobJwoH2eavnqBaFGWiztDUjut-dhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423195fff7.mp4?token=sGcZ5CvPm7-nnc_QWX659-CxZM2FxvolPmqekv5a9Be2aDU7xP8WcFDegcyUl5G-DelWvdEvH5W8vRveHUDdta8ao2X4nLqNhI0WtkFxUgQ5lD73MQtobgLqSVdS4FghxYp4JGWHdRgnk1tczMLRXwCt8vd0-IvSL7ieP-brpvOrQ5cmwP7bo9SJAG4RQusSRlbVJ9bgqfIE1xYyxhvG9B2JMtDKividreqZc474TxWQsWJfAkUe1hSTlthc-2PeYglOiK4agOJv36NkcDbp2FbMGeHRM8n3IXi6cK8kW1pzQ8-c94Eusx6AmobJwoH2eavnqBaFGWiztDUjut-dhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کتابخانه‌ی معروف ‌Pad Shaders⁩ (منبع غنی گرادیان‌ها، پس‌زمینه‌ها و شیدرهای خفن) رایگان و متن‌باز شد!
🎨
✨
‏دیگه نگران لایسنس نباش؛ می‌تونی تمام پلاگین‌ها و ابزارهاش رو تو پروژه‌های شخصی و تجاری استفاده کنی.
https://shaders.paper.design/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6711" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6710">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚀
دسترسی به قدرت هوش مصنوعی در سرور شخصی؛ آموزش API کلودفلر (Workers AI)
☁️
🤖
اگر برای پروژه‌هایتان به یک هوش مصنوعی قدرتمند (مثل Llama 3 یا Mistral) نیاز دارید، سرویس
Workers AI
کلودفلر یکی از بهترین و بهینه‌ترین گزینه‌هاست. برای استفاده از این سرویس، باید یک API Token اختصاصی بسازید.
🔥
مراحل دریافت API Token در کلودفلر:
1️⃣
ورود به بخش API:
وارد پنل شوید، روی آیکون پروفایل کلیک کرده و به مسیر
My Profile > API Tokens
بروید.
2️⃣
ساخت توکن:
روی
Create Token
کلیک کنید و سپس
Create Custom Token
را انتخاب کنید.
3️⃣
تنظیم مجوزها (بسیار مهم):
در بخش
Permissions
، گزینه
Account
را انتخاب کنید و دسترسی
Workers AI
را روی حالت
Edit
قرار دهید.
در بخش
Resources
، اکانت خود را انتخاب کنید تا دسترسی‌ها محدود به همان اکانت باشد.
4️⃣
نهایی‌سازی:
روی
Continue to summary
و سپس
Create Token
کلیک کنید.
⚠️
توجه:
کد نمایش داده شده را بلافاصله کپی و در جای امن ذخیره کنید؛ این کد دیگر نمایش داده نخواهد شد!
💡
نحوه استفاده:
شما علاوه بر توکن، به
Account ID
نیاز دارید که در صفحه اصلی
Workers & Pages
پنل کلودفلر قابل مشاهده است.
آدرس فراخوانی (Endpoint) شما به این صورت خواهد بود:
[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){ACCOUNT_ID}/ai/run/{MODEL_NAME}
✅
حالا می‌توانید با استفاده از این توکن، مدل‌های هوش مصنوعی کلودفلر را در کدهای خود (پایتون، Node.js و...) فراخوانی کنید.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6710" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMCSqKGLgEeEusBdF6b28peAlPejlKWTS5rRXxfc3rDvp7utq7GlLAIFG6C8LveOnDG2CYf6BJPC_cf_J5o2s7NwQxwcBCCrnOQs-_pOCKyo0vNGvTt-EDH8winpqvgxRAjne9SYmkr_nwSlHGEf6JTst8UmdbCAz48Z7Zq-FzmNQqvrZjsjiDMtxdZw8tvUczQLySvck_ZiAnLRgtKu9DEyTQdtep3HHz9UZQOOEkZhMkbH3SGyJNzNf0lOHXK2LySH4mRsDehkiTfx9572uHP65p4JcDHEofoXlqrIbEqyHhBTT4tTbRDCzKIEoxpoRhQmb7K1yACB0H8qq2v0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5
هوش مصنوعی رایگان و قدرتمند شرکت انتروپیک
10 دلار کردیت
با لینک زیر 20 دلار
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6709" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سایفون رو اپدیت کنین خوشگل شده
🔥
(نسخه بتا)</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6708" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=rmuTsm-K5ZBo8uvwt4AEXmtFsT5ECPWYyuZN948Wt5TiFMcEv-XnhwmuWY5-QLQywLFPMsV3-_IeqLBlUVUWDj94E3hEIyev1bN2R49PJTZeslNVPZ8-XYyzT13s0vW9htuzyGuiYmlgKaehZjDSRdpHqL6XMfhU7FF97UUmd-dWnTpQ2JyvomyKSpskbc0-SKZUk8hsOTxkM0DHqqzi6EjrfkjQeS-fAt-Xm-oFm922uuwUSMWUEuPUlWqGIQ71WKfmnBgHEdmej5oeA6uUamwByPEOXRL1biIxOTDf5ZlQiJbcHlpACqF6tXxcoFKhrg-y3F9HfXWn6IThwFBtyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=rmuTsm-K5ZBo8uvwt4AEXmtFsT5ECPWYyuZN948Wt5TiFMcEv-XnhwmuWY5-QLQywLFPMsV3-_IeqLBlUVUWDj94E3hEIyev1bN2R49PJTZeslNVPZ8-XYyzT13s0vW9htuzyGuiYmlgKaehZjDSRdpHqL6XMfhU7FF97UUmd-dWnTpQ2JyvomyKSpskbc0-SKZUk8hsOTxkM0DHqqzi6EjrfkjQeS-fAt-Xm-oFm922uuwUSMWUEuPUlWqGIQ71WKfmnBgHEdmej5oeA6uUamwByPEOXRL1biIxOTDf5ZlQiJbcHlpACqF6tXxcoFKhrg-y3F9HfXWn6IThwFBtyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت 10 تا ایمیل رایگان با ساختن یک ایمیل اتومیک (مولتی اکانت)
https://www.youtube.com/watch?v=XHJ3TwrwG-g</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6707" target="_blank">📅 03:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag_aDSe7SGU8lKpCJw3AtrZrnJCmV94YUcMne5OqzeszUwIRHGg5MqVwwZLae5nmBSdkOKChcBuY9lb0_PdBkSEEs5yMNutN9B_QkHELebuWMl2EaqeL1BuwVFe_zhF2CX2MfLrBcyZYyr7cm3jg0UTEOjSJ-MKmpAp6bevLtWafAnAaDGPCFMgD8DSLWXJIxEh_qhmYepgkZ27CntUggBYSSSu3gU-TuzyqhBQW1kJHk2BxwbA1PJfgbjWSEZGdVqiXhR6GKmUxh5fFocEpLixVpYm58_fD5vAXXcWfeLPL1TDBp74P5cWobK-qcg9OqinnuWbgWmTtQBUPxVi8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
قابلیت جدید «وگا کد» فعال شد!
💻
‏همین حالا وارد
‌Mini App⁩
ربات وگا شوید و از قدرت کدنویسی هوشمند لذت ببرید.
✨
‏
🛠
مشخصات فنی:
‏
🔹
پشتیبانی توسط مدل قدرتمند
‌GLM 5.2⁩
‏
🔹
سقف
۵ درخواست
در هر ساعت
⏳
‏
🔹
ورودی تا
۱۵ هزار توکن
📥
‏
🔹
خروجی تا
۱۶ هزار توکن
📤
‏همین الان تستش کنید!
🚀</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6706" target="_blank">📅 02:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghbq0BS2P9c9Yig86GZm9h9GnW-eaWwAqEhD4h55T8_VLNTe_tQRFcB1ul0CVgiFxP93IVEZx9snHKmsPSbHn35pn3OyQ2T_7MRc3IbXeIU01WV4FMhoLGzJV3WvnMgFX85MzTTYv_guictujOgc5A_V4EHUFDndSETnF4dts_k3UAH2Kr37fZtgW5PfwcDeo5M2ChHIw0Kj9ejAthLOrxef0swBcE3aieZVOc74z5NNsfYENFNnsbqq47Ux744uYqPfMtuG1u2s9AdwrAvXhghEimZHZ5-GG8eUpR1F9Bfry7K4HSZPS4LsstBQ6J9stgiIF83mduyzvkuhqoQgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک میلیون توکن رایگان Gemini از طرف
گوگل؛ بدون نیاز به کارت بانکی!
🎁
✨
گوگل به تازگی یک فرصت بی‌نظیر فراهم کرده است: دریافت یک میلیون توکن کاملاً رایگان برای استفاده از جدیدترین و قدرتمندترین مدل‌های هوش مصنوعی این شرکت. برای دریافت این توکن‌ها به هیچ‌گونه کارت اعتباری یا خرید اشتراک نیازی ندارید و همه‌چیز با یک کلیک انجام می‌شود!
🔥
چگونه کلید API خود را دریافت کنیم؟
1️⃣
ابتدا وارد پلتفرم Google AI Studio شوید.
2️⃣
روی دکمه Create API key کلیک کنید.
3️⃣
تنظیمات و محدودیت‌های تولید را به دلخواه مشخص کنید؛ کلید شما آماده استفاده است!
🤖
مدل‌هایی که می‌توانید با این کلید استفاده کنید:
Gemini 2.5 Pro (قدرتمندترین و هوشمندترین نسخه)
Gemini 2.5 Flash (سریع، بهینه و همه‌کاره)
Gemini 2.5 Flash-Lite (فوق‌سبک و اقتصادی)
💡
کاربرد: این حجم عظیم از توکن‌ها برای ماه‌ها کار فشرده، از جمله کدنویسی، پردازش و تولید متن، تحلیل داده‌ها و حل مسائل پیچیده کاملاً کافی است.
🔗
لینک دریافت کلید API
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6704" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhYtww-RWp7eXxyolG996eC0JdBpiCaagShQGg4r2_f9btvnUmIztsxKcR7YBLwLrp7dVOgHSmnmJdjXq80Xa3i7-NuktBuk4gpdGHibVKJv1hNRIMV340dDdD8_jmnmzDH8oPoLMDwfAiD6tputUysERRWuQv8ttDaCwob0-eVADGLMfHUVTefXVS8R7XPM3oVrDOkWDwW_o3zDhIq-pwza8ikSMyYiux6IGVIGA5Wz2j_P4HMgs_fymeM7rB8KeXtn5EDfCAjCkN5d0w-fTxIxJzi9oybYV-uaxhZLPviCgLyNdxgxxGErjktjmpNL6Iz8Mb1Vu7J-JoLwGk51MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفسیر خطاهای ویندوز با ابزار داخلی
راهنما:
— کد مورد نظر را کپی کنید، مثلاً 0x80070422.
— ترمینال را باز کنید (با فشردن Win+R و وارد کردن CMD).
— دستور
certutil -error 0x80070422
را وارد کنید.
— توضیحات دقیقی از مشکل را دریافت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6703" target="_blank">📅 22:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSQy6RoOsqXiBRrrp2HPmDLLIIrNsBJ8OWRz3fiOPd42yGGIsP8h7tt3SR9zHb_eMrFOb3awP3yIruOgj8qkq-IWn5s58I8xOdhI11_qyBVnNp3_j5781N99sQK4IIj501nodA8v9M4YpzLZFMXjg0lH0Lw1w6cw0pNuQRAn2vSc83uCRm7__uUvaduN1-noNKKNKk4cmVhKbL8FOwjPe29OakxdFmX3J3GeyQ9xjBcKqvon6sxdgzhrx31K4vtYb0HihjayyhnBIa5z_3IWslN0xfRpbjU72Lg_iEIxwJ948MkFZjwplpIeFBkdxW1KPrrYAYWebRzNgWnqCMGklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا پولاتو چیکار می کنی؟
پولام:
به زودی ۱ میلیارد*
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6702" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilZCtUTvnd8q_LoajaTow7DHa_1cHszaegzXj1L_vmFftWUq-qe3-ATCNygTl_QlqO_eVGa6Sq0-IK3u1EMiJF869eI9LLQp7r8otmc1wPPQit-yfZtMgMUCMM2rOe26iu69sDFbH9Uvuk3a-GI0wmXqW65PSjvlbdUOUJWHwEzrT62VNKy0BRIsKq5aBMG7n2zADHwFsrgujjAM1uCcjpj940rHq0RSsUEs37QVYOUwax3aJKvjkVDKK7hdjXrqHq4DOwtKQ-P_ioK-IKM8rmK8fbJLHAod5XJYBYuUCFRtH1B2Zh0WSBww5gYbcjFdB0AD--YWbVBzSf4z-GzoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_ZLa0cXQgMCtPWL5foGkf3prKTSr00rTanCjexIfxfegLTnIw2SrxZTro-fgqOfTabC1Ri0r0yi4CwP2RSoRyoLtIg0Z6gyvaxz1pYlaA6XzC3exMtgKgh2klp_bi5o3Tyv0zbWJOZPqCODEbmK0YjgCUFWpOWfewym_dydRVAT6khP1smrYgTGP8nkZS6EzLJXEoz-rcHMZs49fDjzoAaJA9sVy3z8HTRkHULxFIzhAHE6MDj5c-QuIRqDf6hBrdBmymsQS9GjOLJUmYv5lmPIMMPlnXU8lNYENZOTvpEk4GACX_CLmIzCBzhw637o3w7tUtklytVhWZDQqWB8CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQ4FwdxEWknYnmA1rIx2oEJd2LNnmfHvDZk1VcM1FKl6gypL6Q2cPjSa55fBnL5FHXfYPRGK8WM_3VmoPRyVT8VcoMeesNflBV5hLGhBqZa-OKHj78NnObdWdUhf4wKpOG9REID68_hSd4XH06_9hnbwc8c1AAKObNQWgDIi5ubxY7-732PEDyATOIM3_QTegmWYGeuliyQxsoLRmG583_UxPWyLlP-ezAaCIbjHae3ZPAjRYEmbWIqzIHos5THSqNzo8oHUCiq0rKmUROsVWrwWfpcBIWzGG0cKkV6i2BnwcGyenK7SxotWrihU_5KpMgJzsggsiT0as6MoiY02VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ra0CgDULnGy6ZyA-Lg4-XFBYMaYwRLJyO2c1eVcs-Y3ymNrBVJwZ5u3T6kZqr1q1gappw7RkmfhGWDLHwG5e0MAuI-QC8Jn-dwSDGsQ79G6yV63SbI-he34hblbqDPYZfbqsDO5npfYGVZHuta_AzM6NUo_0LTcALmpWU8BUrpEWf9_yDEZ2sof0gAGKbZZ-WEkbgxpsWDZW3mFX8p8yGvYHbAgihVXAeiKpfjsHhj8njKrnlhxWksRtmBZYmF24_o_I3N8Zj6OJjA06DQWRZhsR9-QuYea517JmU6Vcb9Pa3X_OgcBWHmmZDUIAdm8um-_CNJs6nQIqpwcB4q1nbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFmHZ3ohst--4TjlfLCAmmTGOPxt9pdveIXgpu9Fe_ah1bYXV24_JcryDqkLrncHQgLJrpYu7CmQ_t7--t_vyCFEZtulFvAPhkvzPy156PKLA4zbzcKH4zrP9IIYAjBOUCPAPLXZ9wFcn97BQxxSC10S80Ndr_9LhNHau5Cx_DaGZz1ZR-SaBf8NF1O19O7ePh-_HUwKNi-Og-uQEGFr-hL9IzlzzBOlmMULHSIG1qqarGFRtvA_pziHD5mNkfnd1h4P4FjFWco76Fj5Wx2nvTC7mXd2jh6aZu4OA6sgGyp5l0hxSGd_NwMXvzlRp2oSCP9RaRsR4Ya59PLZGr3Ilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSBBo70tJkxjtjFM6nYjgweEk-CTW0jn52-HxDcw28JOD528SuvQ0jDKTDLuw2srpUXQgbMZ8u989Vp_517tEv77Q8vN9pDSd4z-sBY99HIiZTRsT9yX-Ly93YNb8vQv9KkfP-tLyZAAiUsYlPXLLqKrwuM6Jr8XS3exZb5xCQNX3HALY5rFSCkDZhvObfndqTmNG5E2VLG79HbUcaD_rnG4UWkjTogtB8NWDTjvOh4P267hLXYm3ty2MqxrA9SpcWYGUvglXRyEl2lFutZ1DnLVzUO5WriGBD1lt7H6S_Y9mvOALWErV2qnQmOl92DBEexUPdRsPDSH5YIoUiMkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFSyKZSF3_d8p9m-eaxz3rKsqzN4CLwcV-1d8kdrmQh6VF3TlDCn4qut_gVkVFPgnhRX3gBtKZDgSr6CT7EVTHZDhgl8CLKJDM1jJZDdG726AlA6fOKUDfh6WwsqSDXzCXEJranjV2-C8xC_vXDgrLM0cB_lFdeLPi4iRRWev9ft1318YcvLBwOCwF5kkogW2zD0iceC4bASNXF96sr2qNjdNKyTMo7ubKcIs5gfZmaOVG_P4I0W4aZ0UXCfcDL-tg9xPwH-QAZi7dM9ZKZe4V1LN5ZQqtsQeJ3ethZb1kWuTxYSgAkoO702NeNJ-p2kRF0OOuxVxCY9MOx22E-9Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج
جایزه عکاسی با آیفون اعلام شد.
در این مسابقه سالانه عکاسان از سراسر جهان بهترین عکس‌های خود را که با آیفون گرفته اند، ارسال می‌کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6695" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STUu0FMU5JLQ4v_mu8yap0WfRcatc5GePFMbIaXURaqggPYe4pJ2OUV3sp31cZsdMLwPA8VZ1Xl4OcxgrQcOMQJnrhSTaBZBvBUPpVc-UJUnVw4dLP1MugMkBiqDDEBKlSpQSgkfDDCj7k26CZzmN7PgdE0AxrO8Hif_VpzA0dJHGuegHHjTwx-JQBaxJYPruI7zdNPaaNhxjLkOSPDFJmr6kBOFZwJmlmx7ivQ1TVUEmzJERRVmyjumqpOtHQd3DlEvlRFEQhGalLHgKlWLkbTpEs9uQvC5HHNzWDcL5scmk8wOY14dkR1lHVtUJjkDf3wzkZeV3wu2jX4ZBQipEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AITwitter Generator
یک افزونه برای تولید توییت است.
این افزونه که بر اساس فناوری پیشرفته هوش مصنوعی ساخته شده، خلاقیت و سرگرمی بی‌حد و حصر را به حساب کاربری توییتر شما اضافه میکند.
https://tweethunter.io/generate-tweets
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6694" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFZTy6cOf-OTCYys8yD89Xb4p3tfkOlDixR7IsTziAhiXaRVYTYT8ZfTy4RaLP78JGFXhjoBpGW228AFRYT3hhbhjGqdxDjfqdv4rbCROeFfEFlCJk7fZj64WCtYP9BMJQuek6OUo-CuyC5HbckDdgqhYMYkKBiJ-coxO0aReMpsq8c6CZ53ca_b_5Z8r_cFMrfu6AVr5WPEEQE5E56FrNqRbi5WnC0Ep-fZe64dcapikBdyeGLjGsUXpwaOeZcKGB8cGTv0sZbpx5gSv0EwAtsejvcRWHDwmg3C9_43hwNU6CjvGP9dNXkaipVIAw1y9grp7hUg7wBuuV9v7ouDiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک مجموعه‌ای رایگان از پرامپت ها برای Claude ارائه می‌دهد
🤩
این مجموعه شامل ده‌ها راهکار آماده برای بررسی امنیت، رفع اشکال و بازبینی کد، خودکارسازی وظایف و موارد دیگر است. برای هر پرامپت، توضیحات مربوط به نحوه عملکرد آن ارائه شده است.
https://code.claude.com/docs/en/prompt-library
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6693" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEq-eLpSKYrMMUlxo0cVcUI9Rvv7l11GVl6MjAmXD8IyhesYz1hjtzVXd1Mvjs18qHT1P4_vajNJyONlQUK0zMikJqYzVFT9QV3UtCHC4cBxhqx8nfddMhM33w6qYVNRmGvJdwmF10XZWI2n_YVlYZr1MoSw_oIgzp9MhqQVfmBbWA0h-up2qjKJhOczHGX83LIJMPSKbaHArnPciyKPBolugRrITe2C4BDHPiFRPUMrc0DpB_AuH5LDGgdACYHE2HiChzox9FKylaWlnTHjBnjkoZcubwvw4DSTx-O5iMoKNITz6FqO_b7nGiX6BoWuADp1HmOwqeC7xLjOEcFhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فتوشاپ را فراموش کنید
🤯
یک ابزار مبتنی بر هوش مصنوعی می‌تواند تمام وظایف را با دستورات متنی انجام دهد و برای این کار نیازی به مهارت‌های طراحی یا دانش فنی نیست.
🎨
✨
🔹
همه چیز بسیار ساده است: یک عکس یا تصویر را آپلود می‌کنید، پس‌زمینه را تغییر می‌دهید، اشیاء اضافی را حذف می‌کنید، رتوش انجام می‌دهید، کیفیت را بهبود می‌بخشید و از ده ها امکان دیگر استفاده می‌کنید.
🖼️
🛠️
🔹
بدون ثبت‌نام و مستقیماً در مرورگر
🌐
🔹
کاملاً رایگان
🆓
https://ezmaker.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6692" target="_blank">📅 14:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏
🎁
500 کریدیت رایگان ‌Opus 4.8⁩ و Fable 5 هدیه بگیرید!
‏دنبال دسترسی رایگان به قدرتمندترین مدل‌های هوش مصنوعی می‌گردید؟ با این روش ساده، ماهانه ۵۰۰ کریدیت رایگان دریافت کنید.
🚀
‏
1⃣
وارد سایت زیر شوید:
🔗
‌www.relay.app
⁩
2⃣
‏ ثبت‌نام کنید:
‏با اکانت
گوگل
یا
مایکروسافت
خود وارد شوید.
3⃣
انتخاب مدل:
اگر روی آیکون پروفایل خود کلیک کنید و وارد تنظیمات شوید
در بخش اکانت ، اولین گزینه را بزنید و select model را انتخاب کنید و مدل مورد نظر خود را انتخاب کنید
4⃣
لذت ببرید:
‏از امکانات پیشرفته و کریدیت‌های رایگان ماهانه استفاده کنید.
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6691" target="_blank">📅 23:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🧠
یک سرویس جدید که قادر است مدل‌های سه بعدی را به کتاب‌های آموزشی تعاملی تبدیل کند!
📚
✨
هر مدل سه بعدی را بارگذاری کنید، سیستم به طور دقیق ساختار آن را تجزیه و تحلیل می‌کند: عملکرد هر قطعه را توضیح می‌دهد و نحوه کارکرد آن را نشان می‌دهد. در پایان، یک آزمون کوتاه برای ارزیابی دانش شما ارائه می‌شود.
🧪
🔧
برای آشنایی اولیه با قابلیت‌های این سرویس، مدل‌های آماده‌ای در زمینه‌های پزشکی، مهندسی و علوم طبیعی در دسترس هستند.
🏥
🏗
🌿
https://atlas3d.space/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6690" target="_blank">📅 23:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=M9zkLOuO_i1yxRQpy5xfMvJVeiv8lfWbkTtjCVFMuLN3W5k4ZJFM7p7lTX13YylB4anI8W-C9ZTriSAG8YJd-7kwLkIMYBkI1rEHhTBFz2_r3O6aMyAO2TYCAwiL6Uw2vG_a-orFPAnh_-asy7YzOpyFnkYYvI6pYQRUuqbUFWozrMCmQ7mOY1YDdBpRqNxU2aPuhPsgsVd7nu4N5roJpYCqWhwGigbPPU3v-8YEqiyDVjeNJtXjKpc0XnHg36v4TVgyYfuUxJkM6KaunuqleLaJ5zIkj1zl4w9dUJ-Ju3LscODkHJ6jDCgZnLqYqDLWD6Zim5VCAX5H7dox9vLQRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=M9zkLOuO_i1yxRQpy5xfMvJVeiv8lfWbkTtjCVFMuLN3W5k4ZJFM7p7lTX13YylB4anI8W-C9ZTriSAG8YJd-7kwLkIMYBkI1rEHhTBFz2_r3O6aMyAO2TYCAwiL6Uw2vG_a-orFPAnh_-asy7YzOpyFnkYYvI6pYQRUuqbUFWozrMCmQ7mOY1YDdBpRqNxU2aPuhPsgsVd7nu4N5roJpYCqWhwGigbPPU3v-8YEqiyDVjeNJtXjKpc0XnHg36v4TVgyYfuUxJkM6KaunuqleLaJ5zIkj1zl4w9dUJ-Ju3LscODkHJ6jDCgZnLqYqDLWD6Zim5VCAX5H7dox9vLQRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😂
سووو رونالدو با رینگتون های مختلف
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6689" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آموزش‌ گرفتن Fable 5 به صورت رایگان تا 1 ماه هر هفته 70 دلار
💰
برید توی
Aerolink
و ثبت نام کنید
📝
لینک ثبت نام
🔗
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
📄
نحوه اجراش روی
claude code
هم همونه فقط این تنظیمات رو بزنید جای اون
⚙️
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
هر ورژنی از claude code هم بزنید قبوله
✅
لیمیتش هم دقیقا مثل
freemodel
هست
🔒
موقع اجرای claude code بجای دستور claude این دستور رو بزنید
👇
claude --model claude-fable-5[1m]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6688" target="_blank">📅 22:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚀
معرفی Qwen Gate؛ دسترسی رایگان به API مدل قدرتمند Qwen 3.7-Max!
🤖
✨
مدل Qwen 3.7-Max در حال حاضر یکی از بهترین مدل‌های هوش مصنوعی است، اما استفاده از API رسمی آن هزینه دارد. ابزار متن‌باز Qwen Gate نسخه وب (
chat.qwen.ai
) را به یک API کاملاً سازگار با استاندارد OpenAI تبدیل می‌کند تا بتوانید به صورت کاملاً رایگان و لوکال از آن در پروژه‌هایتان استفاده کنید!
🔥
ویژگی‌ها و قابلیت‌های این ابزار:
1️⃣
سازگاری گسترده:
قابلیت اتصال بی‌دردسر به دستیارهای برنامه‌نویسی مثل Cursor, Claude Code, Continue و سایر کلاینت‌های مبتنی بر OpenAI.
2️⃣
چرخش اکانت (Multi-account rotation):
پشتیبانی از مدیریت و چرخش بیش از ۳ حساب کاربری برای جلوگیری از محدودیت‌ها.
3️⃣
امکانات کامل:
پشتیبانی از فراخوانی ابزارها (Tool calling)، استریمینگ سریع و دارای یک داشبورد حرفه‌ای برای گزارش‌گیری.
4️⃣
پشتیبانی از مدل‌های مختلف:
دسترسی به Qwen 3.7-Max, 3-Max, 3-Plus و سایر نسخه‌ها.
💻
نصب و راه‌اندازی سریع:
برای نصب کافیست دستور زیر را در ترمینال اجرا کنید:
Bash
curl -sSL https://raw.githubusercontent.com/youssefvdel/opengate/main/install.sh | bash cd opengate && qg
پس از اجرا، آدرس
http://localhost:26405/dashboard
را در مرورگر باز کرده و اکانت Qwen خود را اضافه کنید. حالا می‌توانید از آدرس http://localhost:26405/v1 به عنوان Endpoint (درگاه API) در نرم‌افزارهای خود استفاده کنید.
⚠️
توجه بسیار مهم:
از آنجا که این ابزار بر پایه اتوماسیونِ رابط کاربری وب کار می‌کند، احتمال مسدود شدن اکانت توسط سیستم‌های امنیتی وجود دارد.
حتماً از اکانت‌های فرعی و تستی استفاده کنید
و به هیچ وجه حساب اصلی خود را متصل نکنید.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6687" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚀
ساخت بی‌نهایت اکانت معتبر با یک Gmail!
📧
✨
سایت‌های حساس (مثل صرافی‌ها، ChatGPT یا AWS) ایمیل‌های فیک را مسدود می‌کنند. اما با ترفند پنهان «پلاس» (+) می‌توانید بدون نیاز به شماره موبایل، بی‌نهایت ایمیل معتبر (برای دریافت اکانت‌های تریال) بسازید!
🔥
این ترفند چطور کار می‌کند؟
قانون جیمیل این است: هر عبارتی که بعد از علامت + (و قبل از @) بیاید، نادیده گرفته می‌شود.
مثلاً اگر ایمیل اصلی شما ArchiveTell@gmail.com باشد، می‌توانید با این آدرس‌ها در سایت‌های مختلف ثبت‌نام کنید:
ArchiveTell+twitter@gmail.com
ArchiveTell+vpn123@gmail.com
از نظر سایت‌ها، این‌ها ایمیل‌هایی کاملاً متفاوت هستند، اما تمام کدهای تایید مستقیماً به
اینباکس همان ایمیل اصلی شما
ارسال می‌شوند!
🛠
ابزار کمکی:
برای ساخت خودکار هزاران آدرس مشابه، می‌توانید از ابزارهای آنلاین
Gmail Generator
استفاده کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#آموزش
#ترفند_جیمیل</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6686" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaYPqvm-vjeJ4il7R-J96oLQBnVL0LoUhQbJYAyfuSIL98PVROQP7PwItrKEjbhMIEg_BnMmdaSBf1UCiuDVkUK8fVow0qF2t6C069ZjF0wMUH4SyAyqAZIXUm4d1jWtrXncJcMn8LrS3DAF9fFF5R6KAcuqb1Q6cb32O8qeeDw0ckeNlHpDb9u9ppa1dtPs53Rocz9CEeTmKW-SmqaD4Rgj0Y1QDXxMyQOQk1A6QAAFny38vZmli0g2b98TsjUKtE770gDnNjWdlQJAxoiSffKZuJM6Kclk0nQpZoe1nl9jly7ULx3BlnvbP5I5aLo8Mb7OZiIjB9RFyQXFEOWCFWw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaYPqvm-vjeJ4il7R-J96oLQBnVL0LoUhQbJYAyfuSIL98PVROQP7PwItrKEjbhMIEg_BnMmdaSBf1UCiuDVkUK8fVow0qF2t6C069ZjF0wMUH4SyAyqAZIXUm4d1jWtrXncJcMn8LrS3DAF9fFF5R6KAcuqb1Q6cb32O8qeeDw0ckeNlHpDb9u9ppa1dtPs53Rocz9CEeTmKW-SmqaD4Rgj0Y1QDXxMyQOQk1A6QAAFny38vZmli0g2b98TsjUKtE770gDnNjWdlQJAxoiSffKZuJM6Kclk0nQpZoe1nl9jly7ULx3BlnvbP5I5aLo8Mb7OZiIjB9RFyQXFEOWCFWw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیه‌ساز هاگوارتز ( مدرسه جادوگری سری داستان‌های هری پاتر ) از ‌Fable 5⁩
در این قلعه افسانه‌ای می‌توانید درس بخوانید و با جارو پرواز کنید.
🧙‍♂️
‏این شبیه‌ساز مستقیماً در مرورگر اجرا می‌شود.
https://hogwarts-production.up.railway.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6685" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ظاهرا کلودفلر اعصابش از ایرانیا **ری شده و از این به بعد دیگه ایمیل فیک قبول نمیکنه اگرم بکنه تایید نمیتونین کنین اگرم بتونین تایید کنین بنتون میکنه
😍
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6684" target="_blank">📅 18:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ArchiveTel
pinned «
دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...  https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6683" target="_blank">📅 18:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🛡
آیا وای‌فایِ شما واقعاً امن است؟ (یک تستِ ساده و حیاتی)
خیلیا فکر می‌کنن چون روی وای‌فای‌شون پسورد گذاشتن، امنیتشون کامله. اما حقیقت اینه که اگر پسورد شما ضعیف باشه، نفوذ به شبکه و شنودِ ترافیکِ شما برای یک فردِ آشنا به تکنیک‌های ساده، کمتر از ۱۰ دقیقه زمان می‌بره.
⚠️
چطور تست کنیم؟
در دنیای امنیت، ما از روشی به اسم «Capture Handshake» استفاده می‌کنیم. وقتی یک دستگاه به مودم وصل می‌شه، یک تبادلِ اطلاعات (Handshake) بین اون دستگاه و مودم انجام می‌شه. اگر کسی این تبادل رو ضبط کنه، می‌تونه آفلاین و بدونِ اتصال به مودمِ شما، اونقدر رمز عبور رو حدس بزنه تا بالاخره یکی درست دربیاد!
💡
چطور نفوذناپذیر شویم؟ (اقدامات فوری)
۱.
پسوردِ قوی انتخاب کنید:
رمز عبور باید حداقل ۱۶ کاراکتر شاملِ (ترکیبِ حروفِ بزرگ/کوچک، اعداد و کاراکترهای خاص) باشه. رمزهای ساده مثل شماره تلفن یا کلماتِ دیکشنری، در لیست‌هایِ هکِ «آفلاین» در عرض چند ثانیه شکسته می‌شن.
۲.
غیرفعال‌سازی WPS:
این قابلیت که اجازه می‌ده با فشار دادنِ یک دکمه روی مودم وصل بشید، یک درِ پشتی (Backdoor) خطرناکه. حتماً وارد تنظیماتِ مودم بشید و
WPS رو کاملاً Disable کنید.
۳.
ارتقا به پروتکل WPA3:
اگر مودمِ شما از WPA3 پشتیبانی می‌کنه، حتماً تنظیماتِ امنیتِ وای‌فای رو روی این گزینه بذارید. WPA3 به شکلی طراحی شده که اصلاً Handshake به روشِ قدیمی تولید نمی‌کنه و عملاً در برابر این حملات ایمنه.
۴.
تغییرِ دوره‌ایِ رمز عبور:
حتی اگر رمزِ پیچیده‌ای دارید، هر چند وقت یک‌بار اون رو تغییر بدید تا اگر کسی قبلاً در حالِ شنودِ ترافیکِ شما بوده، دسترسی‌اش قطع بشه.
این پست رو برای کسانی که هنوز رمزِ وای‌فای‌شون ضعیفه، فوروارد کنید!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/6682" target="_blank">📅 13:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBommOY6-jxU0y15k0Bb9m9_St6-JQhMAK-NieUVk46hr_jNX2Ip00m7tmE-x7GiCdbLGtL3glfGHkleDv0og5sqYAmTWz-IfdZezPUFGe9HhG_CRy6zcnciOykW6Zmj2CkcC9DMLMtBCsur0POZAXXDdrDq5xwxNmFvvhvwhDZt45ifHJpcmyowf0naDD00FKpjf__djFIgXy-ivWELcVpepYWou6sncnEFFBtF7XVA-fOcFebPhfjCk7CfHY7Plmg2jpqTo58EaYvb_Z4LTlR6Q819k4OEu8w0MEVKYDqjnM5v2P6W0na3KHjZczqs5nfXLCPp57DxA0QkWabpQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است. با اجرای این ترفند، می‌توانید نسخه گران‌قیمت Ultimate را به راحتی فعال کنید!
🔥
آموزش قدم‌به‌قدم فعال‌سازی:
1️⃣
ثبت‌نام:
به سایت
gitlab.com
مراجعه کنید و با یک حساب گوگل جدید یا یک ایمیل معمولی اکانت بسازید.
2️⃣
تعیین نقش (مرحله حیاتی):
در بخش تنظیمات و شخصی‌سازی پروفایل، نقش خود را حتماً به عنوان
مدیر سیستم (System Administrator)
انتخاب کنید.
3️⃣
انتخاب نوع کاربری:
زمانی که پرسیده شد چه کسی از این فضا استفاده خواهد کرد، به جای گزینه «فقط من»، حتماً
«تیم من» (My team)
را انتخاب کنید.
4️⃣
تکمیل مشخصات:
کادرهای مربوط به نام شرکت، پروژه و گروه را پر کنید. (اگر با خطای «مسیر گرفته شده است / Path taken» مواجه شدید، کافیست چند عدد تصادفی به انتهای نام گروه خود اضافه کنید).
5️⃣
فعال‌سازی نهایی:
روی گزینه «ادامه به GitLab» کلیک کنید تا لایسنس آزمایشی ۳۰ روزه Ultimate شما فوراً فعال شود.
⚠️
نکته بسیار مهم برای جلوگیری از خطای دسترسی (Permissions):
وقتی وارد داشبورد شدید، به هیچ وجه چت هوش مصنوعی را مستقیماً از صفحه اصلی (عمومی) باز
نکنید
. ابتدا وارد داشبورد خود شوید، روی صفحه گروه یا پروژه‌ای که ایجاد کرده‌اید کلیک کنید و سپس از آنجا روی آیکون چت
GitLab Duo
ضربه بزنید.
در نهایت، از منوی کشویی انتخاب مدل،
Claude Fable 5
را انتخاب کنید و از دستیار برنامه‌نویسی حرفه‌ای خود لذت ببرید!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/ArchiveTell/6679" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...
https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/6678" target="_blank">📅 02:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUmtJj2fli_ZZqfikiSqeAXgKGsVXM5oqPzgCl03StBWcWwhosQmXImtDErtrFIrKKJjnOb_x2fpBlKfoMD7obK0wXzXV36rUkD9sKlgwzxcWRJ_KnrbEiz7Fe4BY78CxEtEfzAxvVqKmbI5h5JVclK12J3uNv1M05KDVgBJyRafj0tIJGjMXGL8B9-Xsm3dWh7iychp8GuRaFhqnfKu_p42jfQdAlXXIx_PPdni1nMFv-XTs78Z710mXUf910V7vspDL229kXdPdc_ItMfwV8i0m_D1-h61icEwCJfnDz7zgo0OwWks2VTIuvN9ugQk-LHy5pUR-lF_QLcdsWyuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعه‌دهندگان چینی GLM ابزار قدرتمند ZCode 3.0 را معرفی کردند
😮
این یک ابزار همه‌کاره برای نوشتن کد و تعامل با عوامل هوش مصنوعی است: همه چیز در یک پنجره جمع شده با امکان کنترل از راه دور از طریق تلگرام.
این سرویس به صورت رایگان در دسترس است.
http://zcode.z.ai/en
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6677" target="_blank">📅 01:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfYikNcwhtImDBD4HPwypZn5wmgO_A5xAiHljEhokWmHgplhkeF199qrrkmStxvQlPCEO-DgFX7TpvE5rYOeN7mY9ZV8Uev9NLovRYuMzrc8P067wRj7NjD2Plm0D-lgkg-pxfBP2kllkNOK-q0b4wLwfKKSOe4jX73lLdxKSyQv1ouskl2p0FMyXzwqSKnTVhaYvKTgU2GppP1GCKYDS3hpCTSdjck9x4kaiz-SwcZR2GzmGVBeZCOtnIvWLFzHzrSUwRCdhNMyx9pVnaEW1NxZXhNmVdoqUjVF8rbYT-wKM8Ott675EKFqd9GnLQuBVodH12_kzC4f2KHUh8Ning.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=GjcAhbq2-WQapE7m9kbBAY9g_ROWiTMUqGv9aKh6ASjQud0k6umZwW__83F2RJvu2fC8vEYxI-Sh0mYqx-RPodB_vIxh1SFNTOr5ajmaevinsyZqFXXmx-8g2CkDK7nck4k2ivzr55Jo3Ezp3Qi8ojm7IkwCWEbUCcLNqtFMNYFYBSzWrjixkRHIxHLz_6T-Wi0aEqQFTP9IVQUkHBbEkc_XVvClgE3OT1wfC1RMnI8JqfxcAwWvnmls-Fl3f5f8XNUB8yu-QyU_YiDf9EdFJve1JA9_kcMwc54LFoP2JENVmwJHBfzIeShpQWqxY_u18dTI0mnGQJj2iQLMMUyHUBSCeLPDbPHBCPsgOovt-wJxtjsB_lvwKHGMDDwoyKXrnJ0ET39etXvFgM5Jg-y6OpYxpFcQrll3XqF5fC9EbyAMP6z9kYnXlXFIr33DkmyBDnUNt3Cp07GIqFci6Ox2pHKsaE6lyUiAMlPzOm1W1_MrcHcweIeTdkAQIK6_FpFvHGQi4wPx4D5pqb_PZIBQySNSrDX2BvbLyXjoaIljxWwXhDSQJ_5879A_NaYY-Q1EjKLcgwp8WwblhFkkC7hku7a8ORw9ti2X1Z_yFWai5_ddjdPS2GG1N43J4e0rshV6VXDJaqwMxif0xtS8Xa4Q2wUxZIQ4dcP49xx6cj1ogoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=GjcAhbq2-WQapE7m9kbBAY9g_ROWiTMUqGv9aKh6ASjQud0k6umZwW__83F2RJvu2fC8vEYxI-Sh0mYqx-RPodB_vIxh1SFNTOr5ajmaevinsyZqFXXmx-8g2CkDK7nck4k2ivzr55Jo3Ezp3Qi8ojm7IkwCWEbUCcLNqtFMNYFYBSzWrjixkRHIxHLz_6T-Wi0aEqQFTP9IVQUkHBbEkc_XVvClgE3OT1wfC1RMnI8JqfxcAwWvnmls-Fl3f5f8XNUB8yu-QyU_YiDf9EdFJve1JA9_kcMwc54LFoP2JENVmwJHBfzIeShpQWqxY_u18dTI0mnGQJj2iQLMMUyHUBSCeLPDbPHBCPsgOovt-wJxtjsB_lvwKHGMDDwoyKXrnJ0ET39etXvFgM5Jg-y6OpYxpFcQrll3XqF5fC9EbyAMP6z9kYnXlXFIr33DkmyBDnUNt3Cp07GIqFci6Ox2pHKsaE6lyUiAMlPzOm1W1_MrcHcweIeTdkAQIK6_FpFvHGQi4wPx4D5pqb_PZIBQySNSrDX2BvbLyXjoaIljxWwXhDSQJ_5879A_NaYY-Q1EjKLcgwp8WwblhFkkC7hku7a8ORw9ti2X1Z_yFWai5_ddjdPS2GG1N43J4e0rshV6VXDJaqwMxif0xtS8Xa4Q2wUxZIQ4dcP49xx6cj1ogoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/art2eSlseGMKQMDmVXdry-cualRhEyDMHYqdN_SkHwaTxNUHHxaoUI7HS0ho3zVQg0ZUh-MvEaCGtpHgi0flADm87QevtNN8hGeACGh4BFL--g9rYBF_961shFoQnnScPosBfmeytdp8Omp4viv91A_krK_bviCQp11T3fYeF03xJ_e9vNlN7tbFgk55dIpQ0FwImdZIi0EBKohII2r6_Ai2bkf5gsuYnwvBOG5LaSzdUfqeIfEhWc8rAM6OzchGdax34vGALkTnlR5ft-F3vBC9IDjV-7uzadndjs295zW37j1Lu3zO1vRA6cGQRzCCpuw3J6HtJQm3amvR_59eBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6672">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoSs4Zm9TYCTHulNoUre5tAxIiNdnIqqK65mPKVFNvT2oFYZGmPDXvMewAmM0fOo4cD7wrMVuSiLyDjaiU9mHbS8Kwgo-X58gf3YxfcBb2CbK3I9u_xV6t5X2gWbrfdyrc9fgDsspBXMB06xaRQTih8WbdjTuJCXa52QHZkO3LRsWx0bz_P-gA4czJbimFU5FWaFutZ3Q0KgDdWDUOP69-QmJo6EF_jIMGVrYDNkO5FaoYHNQWAuGnzeLCnzuVKVb0q32i29Gpi1oWE5sAfSGw28V4AX5hk-XyxzHIDX3of-wOJs2dWvm9__ZWUpPoB7dUmztWlvVhj4n-7dvBHu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RevPDF
ویرایشگر PDF سریع، بومی و متمرکز بر حفظ حریم خصوصی به صورت آفلاین است.
این برنامه امکان ویرایش متن و تصاویر را مستقیماً در سند PDF فراهم می‌کند و همچنین عملیات‌هایی مانند ادغام، تقسیم، فشرده‌سازی و تبدیل فایل‌ها را انجام می‌دهد.
تمامی عملکردها به صورت محلی روی دستگاه اجرا می‌شوند و حریم خصوصی کامل داده‌ها را بدون نیاز به اتصال به اینترنت تضمین می‌کنند.
https://github.com/Pawandeep-prog/revpdf-release
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6672" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6671">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=fRcYMIOMfJ7z5TfuNgtj5yckNhFFTIe3X3EW8_nDbLqjNMq6sOjTxhZRYT-FPiu0c7X5S_w56ngUL7_ntEtGIQXeI2TAWx-qdsSkIKu2r4IHSpcO1etMBhNj2e2mnNIVXYYaJIjUZXMKRMO5md-qUzaVaejtCBZaEhC-evtfYRIq2kUd7OHv0gI23vVgEUMi3tfafY8WTK2mUp9CyD5X8hkBKBAjUVWRr26lCo31u9RYBuBHPJjBMT8evh8wOdrOL5Zqh9fb7_hxVXK6zUVr3236XC7z0EYjaLJFihjMPzL6K9XaaILkBiFRsQBxqKdY_H505dHz4texNGhp-X5CT1avARNV2wkewjtidelSGaCVsarw925s-01Vur5beP9BncHws5BoS7BFuKl9cHvDYuQ0t2pbdZYw7JIZPcqioffvv6L4FK4-3A-1w2aWBHi1Wbd7JNoUKXY9SU1FRlV-TOTfk6uZGqUYmb7TI7zryiklwXq6WwpjjhTdq0xJDB5e0z-tST-StPyY6v3i3EP0GwSYvJ5ymHhj-0MiFhx9eDRe_bm7YRREXskz5Isw6uvlYiyPO7nheZ_QcOKPoMw76Wu2uiwE_OErLGKDt-slukbjgrLGhDvUgcOOvI6CQGjsDwyzM4Hg62mzA1YveBKDUAWCL2UB8uf97wfqy2pnU74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=fRcYMIOMfJ7z5TfuNgtj5yckNhFFTIe3X3EW8_nDbLqjNMq6sOjTxhZRYT-FPiu0c7X5S_w56ngUL7_ntEtGIQXeI2TAWx-qdsSkIKu2r4IHSpcO1etMBhNj2e2mnNIVXYYaJIjUZXMKRMO5md-qUzaVaejtCBZaEhC-evtfYRIq2kUd7OHv0gI23vVgEUMi3tfafY8WTK2mUp9CyD5X8hkBKBAjUVWRr26lCo31u9RYBuBHPJjBMT8evh8wOdrOL5Zqh9fb7_hxVXK6zUVr3236XC7z0EYjaLJFihjMPzL6K9XaaILkBiFRsQBxqKdY_H505dHz4texNGhp-X5CT1avARNV2wkewjtidelSGaCVsarw925s-01Vur5beP9BncHws5BoS7BFuKl9cHvDYuQ0t2pbdZYw7JIZPcqioffvv6L4FK4-3A-1w2aWBHi1Wbd7JNoUKXY9SU1FRlV-TOTfk6uZGqUYmb7TI7zryiklwXq6WwpjjhTdq0xJDB5e0z-tST-StPyY6v3i3EP0GwSYvJ5ymHhj-0MiFhx9eDRe_bm7YRREXskz5Isw6uvlYiyPO7nheZ_QcOKPoMw76Wu2uiwE_OErLGKDt-slukbjgrLGhDvUgcOOvI6CQGjsDwyzM4Hg62mzA1YveBKDUAWCL2UB8uf97wfqy2pnU74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
«اودیسه» نولان - تریلر نهایی. این فیلم یکی از بزرگترین آثار چند سال اخیر خواهد بود.
با بازی ستارگان: مت دیمون، تام هالند، ان هتاوی، رابرت پتینسون، لوپیتا نیونگو، زندایا و شارلیز ترون.
اکران: 17 جولای.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6671" target="_blank">📅 18:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dswLoiQVYQTRgQlXSw9DLEDK5OmTcVFdni5WVtuOgzySqns9tkAXMa5__iBPI0aDMFFurxGSrhVObv2J0FjMPWA5gMt3ZTL5Bbg0WPPKLZJhmbv_uBw_xlpcAUGl3_O1jjVsy_PQmZnMEuQ5tTgQ1GHA65bkMyvyfAaN45Rz48_AsVNlQgq7iJ53sJbVPdZKR_6uKsuLwn-Rf1PHJ6PhgWvpZhNXumFhfP52xtCjB1HSBP0zdOHBmD8umrmh5Qi1MlRbIgIrgR5PG9kAwW8PA9_6rxEri_U6h8-8dfRIPzld7BPZ3SUljKGAzrNxAkiwsiFhLmtCU9ak73-8y-Y3uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض چند ثانیه هر نوع کپچا را در سایت‌ها و منابع دیگر رد می‌کنیم
• به سرعت بیش از ۳۰ نوع کپچا را حل می‌کند، رفتار انسان را تقلید می‌کند تا هر محدودیتی را دور بزند.
• با چند کلیک روی کامپیوتر نصب می‌شود، نیازی به ثبت‌نام و نصب نرم‌افزار اضافی نیست.
• فوری و به صورت محلی کار می‌کند.
https://github.com/clawdbrunner/captcha-solver
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6670" target="_blank">📅 18:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268d269709.mp4?token=TuQOYZPfDHqi1gBC7POK9OTOL7fkn2bwPGHPmL76pjteOCmfUj6gl6M8ogQ-kP11ei-Cubio2LI-10C6CuaBfg34-xhO3mwBwgx0Jmps92JqvYhZhujDLia6OE5ixINGpG_RPRSKQYiXZMIayjnGElweuRKODi0O1K1DAL2_GiOtiHHRYPEbj-ocLyE6hVypWDuxaTnBPYt99Qlhzt8nHIt4hJT4NFsjPHsnsEwEkFHGaUn-Oxqk-Trnwg8PXNtfxIvLdL6QZQ61schjieVqb5lSSM0hbgcJorC4x2oahu_k8N4TDZNSp6VeA50OfGktjvpRJq__49ZF5H2aAN3MhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268d269709.mp4?token=TuQOYZPfDHqi1gBC7POK9OTOL7fkn2bwPGHPmL76pjteOCmfUj6gl6M8ogQ-kP11ei-Cubio2LI-10C6CuaBfg34-xhO3mwBwgx0Jmps92JqvYhZhujDLia6OE5ixINGpG_RPRSKQYiXZMIayjnGElweuRKODi0O1K1DAL2_GiOtiHHRYPEbj-ocLyE6hVypWDuxaTnBPYt99Qlhzt8nHIt4hJT4NFsjPHsnsEwEkFHGaUn-Oxqk-Trnwg8PXNtfxIvLdL6QZQ61schjieVqb5lSSM0hbgcJorC4x2oahu_k8N4TDZNSp6VeA50OfGktjvpRJq__49ZF5H2aAN3MhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شبکه عصبی Gamma به ChatGPT اضافه شد — حالا می‌توانید پرزنتیشن‌های زیبا را مستقیماً در چت بسازید.
ابزار هوش مصنوعی محبوبی که صدها هزار نفر در سراسر جهان از آن استفاده می‌کنند، در ChatGPT ادغام شده است. حالا کافی است ایده خود را توصیف کنید یا متن را وارد کنید، شبکه عصبی آن را به یک پرزنتیشن آماده با اسلایدهای طراحی شده تبدیل می‌کند.
می‌توانید تا ۱۰ اسلاید را به صورت رایگان تولید کنید.
🔗
لینک
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6669" target="_blank">📅 17:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjyQ2pGBeR32tTLrJUzlaVXbF4yPBgHFlmDpjEPbl1Yk16MbjVMYcgtrI1IaiE-0sOGhdiqzRvpuKLW8IBW6QQTjq9KwE8q7KNDH9ZxPd4UDxlmMNTziWVcglO0IZwETYR15xbpQysFWgMTTDiLdgKUXxlSH4ePm_fUSlOYJisMbeUtL_K1RrZr_wtOlUkjDrrHn9Iy6p3awjCjFLlwhHV6-GMlG2E1VpmyXgYnIKcvep1LbAQAuj2W49P4XJp2vHnvHh5EkVdMGoOsNK5lmwUSGhIGczlVkpfk7blX9xhnVVnpD2iw04CZLnr2r6iA5tn67xUkMWbRY5UyT-dEuxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دیسک‌های بازی پلی‌استیشن سال ۲۰۲۸ ناپدید خواهند شد
بازی‌های جدید فقط به صورت دیجیتال منتشر خواهند شد. همچنین سونی فروشگاه PS Store برای PS3 و PS Vita را خواهد بست.
یک عصر به پایان رسید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6667" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
معرفی Superfile؛ فایل منیجر مدرن و فوق‌سریع برای محیط ترمینال!
📁
✨
اگر از طرفداران محیط خط فرمان (ترمینال) هستید و به یک مدیر فایل قدرتمند، زیبا و سریع نیاز دارید، ابزار
Superfile
دقیقاً برای شما ساخته شده است. این ابزار با رابط کاربری بصری (Intuitive) و کنترل آسان از طریق کلیدهای میانبر، تجربه مدیریت فایل‌ها در ترمینال را به سطح کاملاً جدیدی می‌برد.
🔥
ویژگی‌ها و امکانات برجسته این ابزار:
1️⃣
پشتیبانی کراس‌پلتفرم (Cross-platform):
اجرای بی‌نقص روی تمامی سیستم‌عامل‌های دسکتاپ از جمله لینوکس، ویندوز و macOS.
2️⃣
شخصی‌سازی بی‌نهایت:
دارای سیستم پیشرفته برای نصب پلاگین‌ها و تم‌های متنوع جهت تغییر ظاهر و افزودن قابلیت‌های جدید به محیط برنامه.
3️⃣
نصب سریع و بی‌دردسر:
قابلیت نصب تنها با یک دستور ساده از طریق پکیج‌منیجرهای معروف مانند curl، winget، scoop یا Homebrew.
4️⃣
محبوبیت و پایداری بالا:
توسعه‌یافته با زبان قدرتمند
Go
که توانسته بیش از ۱۷.۷ هزار ستاره (Star) در گیت‌هاب به دست آورد و نشان‌دهنده استقبال بی‌نظیر توسعه‌دهندگان از آن است.
https://github.com/yorukot/superfile</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6665" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L27idTKADMzRk9CIArhnw_KRyj5HGQuQEt_9jEd9tDRDIrx4fb-4BMBL-pie1nzhmk6E66tVgU-X_Y_AgctcGHE0EXIb8BWrYldknanBdxoZeB8k0nikm-Gyg2zpi_jITHKXmnD21dyqnJSswNy2o3gTut9JJF1MxwJeFCVyZscBTqiHS_rZqj2a15er3GoOC8JRhX4CTL9nQz34pc4v1m-OK-kTwj5D_9PgZ_IpSJWTbJ5AAhpEVs8KXq9Z9yPbzELbs9k4mds3q4xtZCqukNga786Vow6XHWpyIfp2YDxR6Sqid7hHWe6R3eMXBK8zCpa38tYCbgQUi2b_7ZHLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اروین یالوم خودکشی کرده ظاهرا
😐
اروین یالوم نویسنده و تئوریسین روان درمانی اگزیستانسیال</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6664" target="_blank">📅 15:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoPyTUWQAdSxcQvO-FToCToOaLLgywJcFxbBLVfic2sFkZ0YV65OmuE1Z3ijSGXqiJh0bmRxlmaXyjK1ZtdS4HWjXdPMYumOv5ZvQioK14_A4YFmBjgB4NO5PrQ_mFajIEJJr1gHMnT2FJw8H-vUif4kVMBPLeaL4Tpoxu9_QRgrEnb6j7cyMxKILsT_uGk5Xg26Dm7B22XJzNEA9JrN_uEvyIYgfzhmHNMIg7aQqtJhuUBQfVRYdPhYpKhwbruxkxv7706U5UmEsDHeajH1nR3tsT8HJMij8RFl9tMfJ9fz6graJupEIgrfRtk5n0SbSXI8kQQbYOnK_Cf3phRVIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر سرویسی راه‌اندازی کرده است که پروژه را از نظر سئو، جستجوی هوش مصنوعی، احراز هویت ربات وب، MCP و پارامترهای دیگر بررسی می‌کند.
سپس به سایت امتیازی از ۰ تا ۱۰۰ داده می‌شود و یک پرامپت با اصلاحات ارائه می‌شود که می‌توان آن را به شبکه عصبی داد و سایت را بهبود داد تا امتیاز خود را افزایش دهد.
https://isitagentready.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6663" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6HQBtezPEz223AxIraY4B9FPtmrShmBcV6UruG7E1oGs8T4OIaGdkpDFMtRq6_he5yg9qcUmnwyLZqNK4ardcaX4DyLiDzTmLjRGMkbrH6mBXvLa73Xtaqu3W9eJki7Wsj0947o16exgSjL8Xif8e2X4XSAn5oBtCW-ctWzes0xvKmMsWCPs2KPXfclXfUmYFb5tTqEfrkAwlsBcOerdTYNdlQKkPdzKtNLqkC0OHMPXsnNkmGXkBZKHqn5PnzVdZGRtY3g-NmKdCyIl1p4dd5zatxsXV00kLObZYgTQYYEPtcEJiiHNf4Ty8hdTbUaZc8tNN1THdMseU-i-Jn-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع مفید برای توسعه‌دهندگان: در گیت‌هاب یک فهرست عظیم از APIهای رایگان برای همه موارد زندگی جمع‌آوری شده است.
🌐
بیش از ۵۰ دسته‌بندی موجود است: از آب و هوا، ارزهای دیجیتال و مالی گرفته تا یادگیری ماشین، نقشه‌ها، موسیقی، اخبار، انیمه و میم‌های بامزه با حیوانات.
🐱
💻
https://github.com/public-apis/public-apis
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6662" target="_blank">📅 13:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2mBI1lY7zOEb-c0u3sa8PKgZvKN-5oymq1Yj-9euRDvGXjutSY-bBzVQIwZ4twGLOoN3BXBLYeTacFybCYiEdqVgrlBdCvypPtsj7e7tYRAP1hIzq4l3X4qz3zhiNkSHrQHzQZoYSwHXGHqk4ibXProqw7XMAX5XS3EG329IwYbWu5mxDhPU_jWL9jpX3XjDXaKy_VT3JAWMSLIuWLggRDoY-_U4X4fckv6Blwo7o-V1o20n79olH0mOxA7o9asMWYWTJhBuaTPgEmn2pdL1UsGnva-8iLU6peJ5TbYJK64e_3a91-SGEp0c5xwkNUMZUIirFcjtgf7a9JplBuMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NM6IM77sDyl9vnabXCLOAYwLOYR0MN_s4dJSg9hqCJFMPqQv90z1gvszS4chheoiBzLSvAqn1pHsiAxI1MF4xrWGuTrZOxR-wYoxgg7SkcqocUWtM3ybYEJb_03HZa02Ofm6o9qYq3vACi_o2_1FAt7mQVJ6DkZJWAIPi-A3vDqnPrYkpc13PfBsCAtOyZs2seMYn7POBAp3t8LjZ2YrBHt6g6yHPh9TIEW5Mj0tbRaJ8AeDx0W89iYomGECoBd5mWPkeGh0Mk0GlMkngEEzhRgjw9V1Sa0IkfbyL9OnyzYb6MekGd8oqfVXK5_-fSeIDW_hv5K_p13UReH7hrE_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acnERI3och1Gim_rrh6pvox6Er9i7v6Ps7ub9jBfDguiygj8JQEbHxuTS1k4mjGfvVJOtlaDIbEiDD-hEa3FlZLkWMeAbj8XBOx_ECjszTEqloB4B40DeHCHXupCk1U94APZvt2gCOY1sRqoU0N_cjur2-A-X4nAJPSpFk53l-fhWT2ar9NpdeI8rsr3wHUsGMNmqs3tnucCXR8h4UQtBxIhnidGyYxpG_FTvwMQ4Xi3EIs6VNouwWNP_qZL7HgmJ8r59mdDm3PkqAphygyJ8igGuGP5ZqSpD1a78Hofw5315GTtNcJqUPyZ8KYzUt_DYY5E_iTvqBRGA9u-YWO8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObHgbMin-ReYIDDedSUPQM696ar5mVnWApNQ0qXMHLTEXQstuTrSDmzXFh1bMzs6m41zIUuCL-gYUb5JV9xVBYmR5uVoUtLVH0-IdmDEJwBDQFxrWCHy4xf3xFlgBpH545PYc10J1tAKXrKm8YDNdjkBnS5HWc5oIBMO2KAZ0yok-KuhCUWNNX3hDaRNO-PZBWWFU0c7nxukovEpf9q0UTghSrPkxlzYSFidElUF7jmRRxrQzkFi0wc4-D43XXiUHilWLIJeI1oxyS1w4DGtqIyYvLCl-ihwsBoTt-_FRRx43a4SyHr1IIpAmYxIY6Hd2U_U-moH-sduE2fcRSLstg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">PlayTorrio
مگاتورنتی که همه چیز را دانلود می‌کند:  بازی‌ها، موسیقی، فیلم‌ها، کتاب‌ها و هر نوع فایل.
https://playtorrio.pages.dev/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6658" target="_blank">📅 09:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5SQXzgvREHkqDQ2Pd5Wr7foBsmtDgJHHXpsxjgP22DOGVUJ5Huy0YpElvCcHI4f0rIW51TL4d8HSeg6BIB-1JHu2cQo_DOCCyrDOffxAd-aZKAhLx4LCiXBxoqOIIN8RhSMrxwxvTfO7R9zUfP6y5BkDvtRamoyont1vhCigA5TAZpMdVdClR8UjBJLH4a_re2C9bNmFuEELxusLGSRqA22ToUvhb8cN4XGpbff2Wf2OaFn9ljNq494bdtaS1wWCqnaOYtq7_29T8Zf8x47g4lD6vtdQ0vwqK9Zlzbiz1LuLxKbQG6z6gcNir3znClb2ZVxKx9dUJNjzhA0u7QXcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود Mythos و Fable 5 برگشته‌اند! دولت ایالات متحده این دو مدل‌ رو از حالت مسدود خارج کرده است.
امروز Fable 5 برای همه کاربران در دسترس قرار می‌گیرد و تا ۷ جولای می‌توانید تا ۵۰٪ از محدودیت‌های هفتگی خود را روی این مدل استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6657" target="_blank">📅 09:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2ExzGPNT879oDGvA0-sM4847myxb2GVXstncKgrk796etEkEO76qcgwt1Ne09cJ4XH2U25ASPWvMlz_m8ywtYstG66EdtwWQzZMbjJsIImJnTyWiXcajUMFR_GM1-U9c13pYel5dUBX7vVEc1df7DtdzApEVdZ9iLKQru6vDLIEvizVJd72NSjfgvms9yP4AOp-JwefUVPdgZC2znPyGh58FHWA8MXOqIaqffhbTyqgnCQJwJWusIPJnqsZrT4usB2Rs7ntBKzqEAlLfjY2qa5Kew6f5AoDOaTCMkxkkUndtlSGNuj9zHSm0Ux8jrKvyJf3OZE1qOz7ci3N5rhn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود اوپوس بدون سانسور منتشر شد!
توسعه‌دهندگان Qwen 3.5 را با داده‌ها و استدلال‌های Opus 4.6 آموزش دادند و یک نابغه شرور واقعی ساختند.
• محدودیت سوالات فقط تخیل شماست.
• می‌توانید هر چیزی، حتی ترسناک‌ترین‌ها را درخواست کنید، اما مسئولیت آن با خودتان است!
• به صورت محلی اجرا می‌شود و بسیار سبک است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6656" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ArchiveTel
pinned «
🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6655" target="_blank">📅 08:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">درود دوستان AssA هستم
بابت خرابی ربات
@REN_WZA_BOT
دیروز معذرت می‌خوام
حقیقتا به خاطر شرایط نتونستم سرور تهیه کنم و ربات روی کلودفلر ران شده
فکرش رو نمی‌کردم که قراره انقدر استقبال بشه که سقفش به نصف روز نکشیده پر شه
😄
خبر خوب اینه که یه ربات بک اپ گذاشتم برای وقتی که سقف اولی پر شد بتونید کار هاتون رو راحت روی ربات دوم انجام بدین
جای نگرانی هم نیست تمام اطلاعات دیپلوی ها و کاربر ها انتقال داده میشن پس عملا هیچ فرقی برای شما نداره
مورد دیگه این هستش که خیلی از دوستان بدون اینکه پنل قبلی شون از کار افتاده باشه یا مشکلی پیش اومده باشه ده تا ده تا میسازن که واقعا عجیبه
🤔
خلاصه که دیگه قرار نیست به همچین مشکلی بر بخورید
و نکته سوم هم اینکه ربات دوم کمی با عجله ساخته شد اما از تست های خودم سالم بیرون اومد
اگر باگی یا مشکلی دیدین با تگ کردن آیدی ام توی چت بهم بگین
@Assa_7788
(بابت مشغله های کاری و پی وی شلوغ به احتمال زیاد پاسخ ندم بهتون پس ممنون میشم پیامتون رو با تگ کردن آیدی ام توی گروه بنویسین)
و عذر بنده رو برای طولانی شدن پیام بپذیرید
🌚
❤️</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6654" target="_blank">📅 05:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الیوم اکملت لکم دینکم
🚶‍♂️‍➡️
😂
(حس تکمیل پروژه خوبه)</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6653" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6652" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyjLU8wRovST5rPhNTLGW8nkeVtyNpFWgA9Cyesm6wxBqZVXKIoTbKW5HjIPMIBhTuTI3J8YqCQCZ0wDNKybJ_0b3Uq38JVdk-kR6BH_jnP8XEcEcD9fYzn37e6U48nj6HbbHoI3Njm7QGNOzwAdXxTy-gzBzlC7cFVU1YfLvHCpg78lSxuUOz-MrcbkuhnZUSrYnLVpaLwUedofKawIvYGtmZd0dPqEuJvpfis42Z9HeS_mPtcCawIRDNH2gHWT9bMqBtbQHqIJmLiEbxG_td-g7gW2JBdhFMylH1IrWHzYnz0RI0F2NiShCwiHhQeMiYp3l4nrASNm3nclKXRZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=JnpHyg-Vc40</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6651" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFMail@ArchiveTell.zip</div>
  <div class="tg-doc-extra">471.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6650" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6649" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام!
تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک شدن.
تو این آموزش یک ترفند فوق‌العاده رو پیاده کردیم: ساخت یک سرویس ایمیل موقت اختصاصی روی دامنه شخصی خودتون با استفاده از زیرساخت رایگان کلودفلر!
🚀
این سیستم کاملاً ضدِ بلاک هست و می‌تونید تا بی‌نهایت آدرس ایمیل فیک بسازید و همون لحظه پیام‌هاش رو دریافت کنید.
🎥
آموزش ویدیویی و قدم‌به‌قدم (از صفر تا صد) رو تو یوتیوب آپلود کردم. حتماً ببینید:
🔗
[لینک ویدیوی یوتیوب ]
👇
خلاصه مراحل و کدهای مورد نیاز برای رفقایی که ویدیو رو دیدن:
۱. مخزن اصلی گیت‌هاب (برای فورک کردن فرانت‌اند)
۲. ساخت دیتابیس (D1) و کش (KV):
یک دیتابیس به اسم
mail_db
و یک فضای KV به اسم
mail_kv
تو کلودفلر بسازید. فایل
schema.sql
(موجود در مخزن بالا) رو تو تب Console دیتابیس اجرا کنید.
۳. متغیرهای طلایی (Environment Variables):
موقع ساخت Worker برای بک‌اند، این متغیرها رو دقیقاً با همین نوع و مقادیر اضافه کنید (راحت کپی کنید):
DOMAINS
(نوع JSON)
👈
["yourdomain.com"]
DEFAULT_DOMAINS
(نوع JSON)
👈
[]
DISABLE_ANONYMOUS_USER_CREATE_EMAIL
(نوع Text)
👈
true
JWT_SECRET
(نوع Text)
👈
یک_رمز_طولانی_و_رندوم_انگلیسی
ADMIN_PASSWORDS
(نوع JSON)
👈
["رمز_ورود_شما"]
ENABLE_USER_CREATE_EMAIL
(نوع Text)
👈
true
USER_ROLES
(نوع JSON)
👈
کد زیر رو کپی کنید:
JSON
[
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "vip"
},
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "admin"
}
]
🚀
مرحله ۵: آپلود کد بک‌اند و هدایت ایمیل‌ها
۱. در منوی
Runtime
ورکر، تو بخش Compatibility flags، کلمه
nodejs_compat
رو اضافه کنید.
۲. روی
Edit code
کلیک کنید و کدهای فایل
worker.js
پروژه رو کپی و پیست کنید. Deploy رو بزنید.
۳. تو تب
Triggers
، یه ساب‌دامین اختصاصی (Custom Domain) برای بک‌اند اضافه کنید (مثلاً
apimail.yourdomain.com
).
۴. حالا به بخش
Email Routing > Routing rules
تو دامنه‌تون برگردید. اون پایین قسمت
Catch-all address
رو ویرایش کنید، Action رو روی
Send to a Worker
بذارید و ورکر پروژه‌تون رو انتخاب کنید.
6. اتصال ظاهر سایت (فرانت‌اند):
مخزن پروژه را در گیت‌هاب شخصی خود
Fork
کنید.
در کلودفلر به
Workers & Pages > Create > Pages > Connect to Git
بروید و مخزن خود را متصل کنید.
تنظیمات Build (دقیقاً این مقادیر را وارد کنید):
Framework preset:
None
Build command:
npm run build:pages
Build output directory:
dist
Root directory:
frontend
تنظیمات محیطی:
یک Environment Variable به نام
VITE_API_BASE
بسازید و آدرس ورکری که در مرحله اول ساختید را در آن قرار دهید (بدون اسلش آخر).
تنظیم SPA:
در مسیر
Settings > General
، مقدار
Not Found behavior
را روی
single-page-application
تنظیم کنید.
روی
Save and Deploy
کلیک کنید.
ارادت، Bachedev
✌️
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6648" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سورپرایز امشب
اختصاصی
🗿
❤️
از یوتیوب
تقدیم به بچه های گل کانال</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6647" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PY5PJrT3EASN5uw8re35p2uVKu6vBtVXyU8IPR-e-Tyf_T2Ovix8zwHvuX1_ZRv8C-0QlZp_niQDI3HMTjGOQxA77JritQt6pwc06ut93hMOUeDblI9c70_EdnEvXWr3ThkgY0w31w9ulJULH7Xa2lYw3MYDMFUXi0-IEv9hntBMpKjGu6nXcHLrWmaojS3GPgUWr08aL1ZSk0MU_o4df6zSQwmNomr4atl-IY68AwGlemAiwfB8c6_9U5AosYmPZmJjNnJBEwHS5jhjEQp3t2VPYuiwOVWJLpPbwM3K5jfBdUfz29FlYuVmN3Mqy_PRqU1t2w7PUjqGjzXr8zzY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude Sonnet 5
منتشر شد!
مدل قدرتمندی برای کارهای روزمره اکنون برای تمام کاربران، حتی کاربران رایگان، در دسترس است.
• از نظر عملکرد بسیار به مدل Opus 4.8 نزدیک شده است.
• به مناسبت انتشار، Anthropic همچنین تمام محدودیت‌های مدل‌ها را حذف کرده است.
https://www.anthropic.com/claude/sonnet
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6646" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_VTxu3MgiQ0FgWg3P__PBv_NaXx0x8U0c1-YMknBKM7y_EfRKHm3Vv6rXUm3gjY5Wh5418ztIoTrNVAWcvpx_u3TD-qXXiTmAtC825J3dpvBMqsaPamnm-x29zA9RemTLDa9pG4rYFD-jb_HsT_kung5tF5hxIA9s-81VRyAJSwGpz398Ulfn62osP4OZQktEui7c0hhhHupdXSxgGD2A-JgueR_jLewfnYPtevgQktmwwGX77xUUzPtmgTKlSlYPuCxl9CczahMLYA4Z4gjPIeSzBH3oGvwp2ekjFcng3H8s4bnNi63jVghGigXYJKKm_5oUnq79cUsAlV2hPltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rdiF_lHEsm8YMxnEM-sv9ath5qmkFnDkzrSl_9EXaPPjJ6FcwQDvATXEM4go9KTxDfm3S4CsInPKXuXvkU_jEpdk5wZgE1DbR0nbkl5qIWpLctYIxCrrJLyUF9ox7u3KxnN7iXYuTxU1SCOXifr1jLViTKAICR_ZSCjUJHaRxn0wLZEeyabkK1Oz6KBIMQRy8PHiCBJTVTq3hy3YHGsc300Kv42S0OYR-bFdHBLXmz4K9JeYFQX9_2T9ezUO424NHhCV4d5SAoXlgtlGNt7S5rFli0AyPxCADXX7uCdzws_gkHI9WEjZkr4iQ7i7C1tTRL1E8vHu75HMjBYH88727Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcUeVfUvQhWdaXbLT0AU5xYTXXotOMn6CnhPI67AL7WSSZg6qPgucSlcfOAZAkLzd5id3cuJRS5_-hOHO60lhTX_2t-a7ciRNpMEXyQKFCwxmAU1Gv4smccgEA3E9_hcAsddUvttOZ8yU2opxR2xvajkSEvmThmblSoS8633zSOlBdwFSrbR7UKICjy4i31eXpLVCDljIR0IgjO-mk4hA3SN3Ga9q3xBCh-_V2W2r4rT078_lxHaJTJGnnmfThUNvifJy4hhz2GqBIGdlrjSoKQACebfG4F01UHaFiQJYtyWZtq_m_tRS1893W4n9Ops09j2nHyZ7tUn-LPpGTY_-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=FsFWpBuVJYwYEQwLf49uRH8RDIZ6pITKqEMyIImkKU-K7MuCGWemP0sg6hD5Xkyl38fjsPoPE_sznucS0x3G3QCyG7qjNk12iVfUU-SH_LDlMpEkrJwFknOAhaSI6UD6UXKQ1297hqbNOWs0CMnlPeI2Y8cx_Di2cuy615tk6GlQswzeZdUGUrzQhGSKf5S3FFRGr_K9QvZ-IR-hd5MWAxpkAhv8X8WpI0DuhwANO0wK0PVyVfZ-JbmWTg8w16WcELqMqMh9u9VFSsTRqQiDdD-tTZS4i0O4-fSPqHEy5zqppZGqYNmxaYSgLDsF-WohV5_pWj1UJyHW_TYSkez6Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=FsFWpBuVJYwYEQwLf49uRH8RDIZ6pITKqEMyIImkKU-K7MuCGWemP0sg6hD5Xkyl38fjsPoPE_sznucS0x3G3QCyG7qjNk12iVfUU-SH_LDlMpEkrJwFknOAhaSI6UD6UXKQ1297hqbNOWs0CMnlPeI2Y8cx_Di2cuy615tk6GlQswzeZdUGUrzQhGSKf5S3FFRGr_K9QvZ-IR-hd5MWAxpkAhv8X8WpI0DuhwANO0wK0PVyVfZ-JbmWTg8w16WcELqMqMh9u9VFSsTRqQiDdD-tTZS4i0O4-fSPqHEy5zqppZGqYNmxaYSgLDsF-WohV5_pWj1UJyHW_TYSkez6Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
تولید محتوا ارزان‌تر می‌شود — گوگل مدل‌های Nano Banana 2 Lite و Omni Flash را معرفی کرد، نسخه‌های سبک‌تر از مدل‌های محبوب خود.
نکات مهم:
؛Nano Banana 2 Lite تصاویر را تقریباً در ۴ ثانیه ایجاد می‌کند و هزینه آن حدود ۰.۰۳۴ دلار برای هر ۱۰۰۰ توکن است.
با وجود قیمت پایین‌تر، مدل کارایی خوبی در زمینه متن دارد، متن را به درستی پردازش می‌کند و نتیجه‌ای با کیفیت و بدون آثار قابل توجه ارائه می‌دهد.
؛Omni Flash مسئول ایجاد و ویرایش ویدئو است. هزینه تولید هر ثانیه حدود ۰.۱۰ دلار است.
از نظر هزینه، Omni Flash در سطح Veo 3.1 Fast قرار دارد، اما کیفیت بصری بسیار قابل قبول است.
ویژگی اصلی — می‌توان مدل‌ها را با هم استفاده کرد: ابتدا تصویر را سریع با Nano Banana 2 Lite ایجاد می‌کنیم و سپس آن را به ویدئو با Omni Flash تبدیل می‌کنیم.
https://deepmind.google/models/gemini-image/flash-lite/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6642" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuZtXFtOEfGFRfliT_8AqdpHoM6dCvyZ3jymLI6qlpmwQ3px43t9CIHc_bjCy0tPfgBhPZoX7gD17gZOo8U5U4D4srsgmuf0vrcfDU5xAz_X2b7ljzQUVLe1SVlQ2Wk0cqo1qlLRefH9bTiOONEWt4g_sO-SmCPduBlBsjB8NBG71pHf4z-KP2o9Va811I0RlA8tO5mU3akWoRwEtFFRJYwxYip8kxX3UZ7YI-9535XSbX6DiMYcbB4uKXSwd7kmXJ9hMXEjMdO-NpF4z1u1FXxWFhgvhpO_4BsN9WHJXPPfeFsUETQz2EiPnzGLc1PzOAJqhdxJXsl2Mv_WgqL-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی Opus 4.7
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
http://zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6641" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=XGDq0W_UJiq6g-JA4zrHgwQlnvWVy3UvtQ-ALdjmbRt1pnsMPTOOlWOF8Y1FPvh16AC9csPSZBAJRVUl1MQkKC_QtYgeq07-DwIvdT-oX_t1bHBId5rtN_8-dPWAV0rAvscgxzTYVCB1lirVpYR9EnO8IHfDfA0AB_M98ceBQgJ4tDNTWdMMHPOXPDBmVcFhLPVxwcW24h5om5hvsuyV5R8SeAN1CH-J-9DAfNaV6VpnGWwPCancv0PExIa_8Oe2MopL_iQb9pv6gTQuUgEGZlBhmfFVvl0n6urm6MKVoyS5VUV5Zu-XnCgh8woRDm7Fs-bPUGzWrl2T_yerAnJ1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=XGDq0W_UJiq6g-JA4zrHgwQlnvWVy3UvtQ-ALdjmbRt1pnsMPTOOlWOF8Y1FPvh16AC9csPSZBAJRVUl1MQkKC_QtYgeq07-DwIvdT-oX_t1bHBId5rtN_8-dPWAV0rAvscgxzTYVCB1lirVpYR9EnO8IHfDfA0AB_M98ceBQgJ4tDNTWdMMHPOXPDBmVcFhLPVxwcW24h5om5hvsuyV5R8SeAN1CH-J-9DAfNaV6VpnGWwPCancv0PExIa_8Oe2MopL_iQb9pv6gTQuUgEGZlBhmfFVvl0n6urm6MKVoyS5VUV5Zu-XnCgh8woRDm7Fs-bPUGzWrl2T_yerAnJ1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا همین‌طور در سال ۲۰۲۷ رم (RAM) خواهیم خرید — یک پروژه با جاسوسان هوش مصنوعی پیدا کردیم که برای شما اینترنت را زیر نظر خواهند داشت
😋
ایده به این صورت است: شما سایت‌ها یا جستجوهای مورد نظر در گوگل را مشخص می‌کنید و «جاسوس‌ها» در فواصل زمانی مشخص اطلاعات را رصد کرده و گزارش را به ایمیل شما ارسال می‌کنند.
https://github.com/firecrawl/open-scouts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6640" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_0Pr97wQ-24jRIPuDBGNga0xfAfNvJibrv2-JEyU4k8_MkgRx2o3XeU_3xUm-Bv1KChASIRenPHJGZWxNuO9lQG3yKqUagaXxHjAtp1AoCsR48W_kTtdEyFayySXjqnPTu_6sBrhChgCb7aa16xyASsZc-e4WJpxSUUrMSivkxrj-bWDefd9E4a_TnZ0LF-bv4NjclsoB3auKuI80Rxd648JZB_ORg1NCwgDMW3MQhckdKESbs0nrekVtvMxzkTCJw9wYKhXqiGxgfI-0zVgei_pb7ohRBpTV7xhiI7_VGM_3dpWknW4ozxnCa_8vGN_0SBgYLOEejbHYn4JPOttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DocumindAI
راهکاری برای تحلیل اسناد PDF است.
این ابزار قادر است حجم زیادی از اطلاعات در فایل‌های PDF را تحلیل کند، داده‌های کلیدی را استخراج کرده و رابط کاربری منحصر به فردی برای تعامل با خود سند ارائه دهد. این امکان را فراهم می‌کند تا به صورت تعاملی و مؤثر در سند حرکت کرده، اطلاعات موجود در PDF را درک و استفاده کنید.
https://www.documind.chat/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6639" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJjx7XDSPDGd3RH69xeGI7lSfqyr--ZCpJhRFjGp5yUEZla83mpYRhC6cfgUmtn1G82U7IHjCLu21shXHWH2YmtuIKLsHm5ZKlR53-xOt_OxgMZUQsjC6KoIq_D-qPUUhPWqJIzGXAs71MPjLXfIM4a0QPwZ6lr-ykYa52fzRDPqlmdXfjJhpMfiwznulp6JtqRvWCGHL-Yo7qc4wzWI0M8Rb1E4JUP7vyQ2M4rmyTrWP71ZqBW_GPHO-dpV0MOpYC4BYEFvPHlHR3S-e9Zog-BKMnOSl8CwEPR-0jZ3XAiwbCqe7_UVaQNT7UqP-3jJe-uVnHOaO0uatQEvRxlX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
نورون‌ها بالاخره دیگر هیچ چیز را فراموش نمی‌کنند — OpenHuman حالت Super Context را دریافت کرده است که بین جلسات، زمینه را حفظ می‌کند و کار را از جایی که متوقف کرده‌اید ادامه می‌دهد.
🔹
در هر بار باز کردن چت، زمینه را به خاطر می‌سپارد.
🔹
مستندات را مطالعه می‌کند، لاگ‌ها را تحلیل می‌کند، ایمیل‌ها را بررسی می‌کند و می‌تواند آنچه روی صفحه نمایش اتفاق می‌افتد را ببیند.
🔹
به طور مستقل اهداف را تعیین می‌کند.
🔹
به ۱۱۸ برنامه متصل می‌شود.
🔹
با سبک کاری شما سازگار می‌شود و به صرفه‌جویی در توکن‌ها کمک می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6638" target="_blank">📅 20:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPEKqWkMx22xkKsS--OKOWAlm23Xwg7FbaiejA2HQyE1ggC0br30J64Nr34P8bhmAI1861NfWLR0IaBYuSyFL7lf6ScywX3fumKWzOIiBb6QHU-NtFMfE23RZcef0mtslLTiPg5wses0wqxlzeT5Vb3hRnyfDWAEyZ3bRqjkkzieiBnJtqY07Sj92PjNyaLn1lS2FW6_-bm4uMR6s4Q3whxpafIJhWHXYTFS2FY5GojX2q1_kpbrgAX9pEAl5hN62FEeSwOcuBXoG5FRPkX6LJhWzpXq02V1IicFX00m2Ly0Xik4G3oDY-WUerx0C7qul14S8-bbaLd9CPCD9SWPSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاک کردن واترمارک، افراد، اشیاء مزاحم، متن، برچسب و غیره از تصاویر، با تکمیل خودکار پس‌زمینه توسط AI رایگان
لینک:
https://magicremover.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6637" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8GyRoqhI52T6Rxgoe99vSKRvXOuhNloTCCfh69xx3ilRGU1_SGdgdKcAwTYRPPhv7x34Pjzyd8spHoUQ0EJtWIBABM4zLwMXEXqH7-LO2_VwuYetN--qt5hulaJm3bKnAVq50DmFG8D46UVpsHN9MCJb8ybWppCnBzkQZA-cA-akCVzBjzZtFR-4_hpaSh_IWd1_GPOFc67P67V6idRRZEhJiW7XHyhTjBpq-LhfgZ63ti9FCRqEt4Nxec3vU2rb__VuLNLJ__LiGhHgl5nRIp83YyTeBctJr3Flw_W4krtfQ2PF__Kvzaf1-N-0H-54dT-LKtl0ce8clIfAcZIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
گوگل را دور بزنید! ‌NotebookLM⁩ رایگان و لوکال شد
🚫
☁️
‏نسخه متن‌باز و محلی ‌NotebookLM⁩ منتشر شد؛ دقیقاً همان تجربه قدرتمند گوگل، اما روی سخت‌افزار خودتان و بدون ارسال داده به سرورهای خارجی.
💻
🔒
🔹
چت هوشمند: تحلیل عمیق، خلاصه‌سازی و یافتن تناقضات در اسناد
🧠
‏
🔹
ارجاع دقیق: لینک مستقیم به پاراگراف‌های خاص، بدون جستجوی دستی
🔗
‏
🔹
تولید چندرسانه‌ای: ساخت پادکست، نقشه ذهنی و دوره‌های آموزشی از روی ‌PDF⁩ و ویدیو
🎙️
🗺️
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6636" target="_blank">📅 16:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke3qiWrpfHvpC2izRYyao-VWES6JCDerAPQZQiawVRZ_-9_y2KefdNnJlQh-EGy9HPPlRPChgzHgMKBAohWVfM7PUIfuvNY0kl7CVzMTGjIhdpp9_E7Q82qOcoTkHheO_2LXBeSYhdqFC_CGWIs8W30cygNIbYVFgJL9Oco3Vat1nRyvsOjPnpESGGYejOSXRdW0HA_FKcVZz1hwEyolQ-xSoRoIASbXlSkPcn0xHUYFDSUoOiUYOyVr7tqfNehnwKp3lRu_vQ_8dz4V08ScfNXWMkBJfzgt4yv0CadVL4ehb21ZME5D6g-_ymcJyclgtCKrhatPHyNaW0c9gfAU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود فایل از اینترنت با ‌Torlink⁩، سریع‌تر از همیشه
🤯
‏این ابزار خط‌فرمانی، جستجوی فایل را برایت خودکار می‌کند تا بدون دردسر به منابع معتبر دسترسی داشته باشی.
‏
✨
قابلیت‌ها:
‏•
🔹
بررسی هوشمند منابع و یافتن فایل‌های سالم
‏•
⚡
نمایش دقیق حجم و تعداد سیدها
‏•
🛠️
دانلود مستقیم از محیط ترمینال
‏•
📦
متن‌باز و بدون نیاز به ثبت‌نام
‏
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6635" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=e4YQ5dMdl5BmjHzwKg7p4587DN5ewC0oa6fWAPeCMbU-oL_-YJm8V8tE64UxYV-RfMGDpxNQNf1sTuIi89aulxSqXQ5YiyMG-LN9dL6etZz9KYglOLUZFjra1XrPeQMZor_CG_26zJle97uvPCB3nJ0m--wCIL6WdtdUos8TZNEJCLvdcPc4S9-KOh1Vuvo3TWOChxUv6r5QReO1SBV-GrKIC_iA4-V4R4-xsuM52jZa5myZkQfwfWe4qR5xkfBKDnc5wJg-zYUjuTKp3xt3pgZBf1OY5MvWszvU70Xp2YUBlEFGz5jyD9HovUbIyeqETZ24ZgHfXWe1HOPQd2xXGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=e4YQ5dMdl5BmjHzwKg7p4587DN5ewC0oa6fWAPeCMbU-oL_-YJm8V8tE64UxYV-RfMGDpxNQNf1sTuIi89aulxSqXQ5YiyMG-LN9dL6etZz9KYglOLUZFjra1XrPeQMZor_CG_26zJle97uvPCB3nJ0m--wCIL6WdtdUos8TZNEJCLvdcPc4S9-KOh1Vuvo3TWOChxUv6r5QReO1SBV-GrKIC_iA4-V4R4-xsuM52jZa5myZkQfwfWe4qR5xkfBKDnc5wJg-zYUjuTKp3xt3pgZBf1OY5MvWszvU70Xp2YUBlEFGz5jyD9HovUbIyeqETZ24ZgHfXWe1HOPQd2xXGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل تصمیم گرفته که پشتیبانی از API پلتفرم Tenor، بزرگ‌ترین مخزن انیمیشن‌های GIF در جهان را متوقف کند.
دسترسی مستقیم به کتابخانه عظیم Tenor از تلگرام، دیسکورد، توییتر و سایر شبکه‌های اجتماعی غیرقابل دسترس خواهد بود.
اگر بخواهید یک گیف انتخاب کنید، باید خودتان تصویر را جستجو کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6634" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtHhfl6FM7-U8ejo5vqgejOMsumz1RV4LSx0H5GGB5AoAY3geoCwkCqMZNV5-tl04tSike7mcAKfYsxYVnHV0NTE4s2L9XCm1WvixAaQRqmqO8Ez8xPTK2SD2aAJSYRlHaboy531IDrBBqSdCw6jgb_RLSCEXNvzBgi093jooXVmF61IJLvC1QGX2HZl0e5oQW_EUaOp4vBmh7C34rMObWdKcH54GqUzyCL5jjqOGNNt7WvWvxMF43nd69wTOYFx7f7o1Au_acV7dew1AsMimTSD8XFzsrmDYVQuqgwHRl85A9CQt5Mp9IxeCJOTAeCB_8llcn470GLlfklWdz96bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
غیرفعال کردن ردیابی در مرورگر — راه‌حل ایده‌آل برای کسانی که از جمع‌آوری گسترده داده‌ها خسته شده‌اند و به دنبال حفظ حریم خصوصی واقعی هستند.
افزونه
Fingerprint Detector
در سه حالت کلیدی کار می‌کند:
🔹
شناسایی — نشان می‌دهد که سایت دقیقاً چه اطلاعاتی را از کاربر استخراج می‌کند.
🔹
شبح — داده‌های واقعی را مخفی می‌کند و آن‌ها را با مقادیر «میانگین» جایگزین می‌کند و دسترسی به canvas، audio و WebGL را مسدود می‌کند.
🔹
جعل — رد دیجیتال شما را به طور کامل با یک رد جعلی تولید شده جایگزین می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6633" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWfX9jKGxWE0zv4SiJFH8Yt_AQa6wEKHrz2xVuDKdZDfSpDq31t9eWl6-EaEfP8aGKLpoJmYjX3YMD1o5Pf0J1W56p3zRy289LX0UPCoPRF5sAfn-E8exC-81xQVY2rBnAyWC9sWXRCjdlZUYnsdbwZG0h2dsVjBMti0vunR__X-lpkZWNkw1ySm1H1LC3Nh2EVaK_Irve9JKgV9XHbJfOgc7Sd58cwagnT7HMBDMq4FwJBkZOnbZ5sMsc4_KZeudBPIhYIpu8yOO3eACMoyt6JX1IK4PyjKm_Z6C8roKSFdaf4KD97373rIrUAMTZ4KzJTWFap_l1cYKAQFhuMhaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
هوش مصنوعی بساز، پول دربیار!
‏فکر می‌کنی ساختن هوش مصنوعی فقط مخصوص نوابغ سیلیکون‌ولی است؟
🤔
اشتباه بزرگی است!
‏تصور کن یک جعبه‌ابزار جادویی داری که از صفر مطلق شروع می‌کنی و تا جایی پیش می‌روی که محصولت را به شرکت‌ها می‌فروشی. این دوره دقیقاً همین مسیر را بدون پیچیدگی‌های خشک دانشگاهی به تو نشان می‌دهد.
🛠️
‏
✨
چرا این دوره خاص است؟
🐍
مبانی:
پایتون و ریاضیات را مثل آب خوردن یاد می‌گیری.
‏
🧠
دانشمند:
مدل‌ها را آموزش می‌دهی و بهینه‌سازی (کوانتیزاسیون) را مسلط می‌شوی.
‏
💼
مهندس:
سرویس‌های واقعی می‌سازی و مشتری پیدا می‌کنی.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6632" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این هم آموزش راه اندازی</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6631" target="_blank">📅 05:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚀
آپدیت جدید بات تلگرام ما منتشر شد!
✨
بخش جدید
Hugging Face
اضافه شد!
از این به بعد می‌تونید خیلی راحت پروژه‌های خودتون رو از طریق تلگرام دیپلوی کنید:
🔹
فقط کافیه در سایت
huggingface.co
ثبت‌نام کنید
🔹
از طریق بات، توکن خودتون رو دریافت کنید
🔹
پروژه به‌صورت خودکار دیپلوی میشه
🚀
⚡
برخلاف خیلی از گزینه‌های دیگه، این بخش فقط از
سرورهای آمریکا
استفاده می‌کنه.
درسته که سرعتش به پای سرویس‌هایی مثل Render نمی‌رسه، اما در عوض:
✅
حجم بسیار بالا
همچنین در بخش
IP تمیز
می‌تونید این IPها رو اضافه کنید:
🇮🇷
Irancel:
52.214.248.106
32.195.122.200
108.133.38.41
🌐
All net:
amazonaws.com
108.133.38.41
34.196.7.222
3.162.112.2
18.185.80.10
23.162.112.25
2.92.189.25
115.185.114.108
18.138.171.15
135.160.210.199
🔥
تجربه دیپلوی راحت‌تر با
@REN_WZA_BOT
💻
توسعه داده شده توسط
AssA
📌
سورس پروژه
⭐
برای حمایت از پروژه، می‌تونید وارد گیت‌هاب بشید و با دادن Star از ادامه توسعه حمایت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/6630" target="_blank">📅 05:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سورپرایز تو راهه...
Ren panel</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6629" target="_blank">📅 04:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOTP33AaeJoS3y38a_7F7s-hpVD2iWsjn2QbQGfxUO12HIQ3cPul_6GswrDmm84L8IHKLqVUYggRkU2Leq8SEDgNyN79LUUYFy_dKTytUDNvTPDCjJxIhJp_gcQAd9EZjkYDCv1wGATovPkJz0LljHfHR7rXPS7S4oxrRxxFFehBWjt4NQVFxsdmQDL_n15I4gWZXKPFCHYVko9NRblIJIFlFNtAo0mgnLcJco8r0U94c-_Ni8vPIMy-BqEFvHR2B5gbRDQfADhlNzjBWjn6UqQ1YR65FVun7bWl0z_B4nbSzRpqrFGycyhkAPP63yvUIjq2ZPN26p-qshJ-n8_UxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتس‌اپ پس از تقریباً ۱۷ سال از وجود خود، نام‌های کاربری را معرفی کرد — می‌توان بدون شماره تلفن با کاربر شروع به گفتگو کرد.
تلگرام به انقلاب سال واکنش نشان داده است
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/6628" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=SIJcG-obCIkQ42NuVnmvkyxF7Fvl501-VJTaYPk1aj7M2guKwTNjJGyX_2H-5e-9q5H-aTrT9H7qTbyMjk-hTPxTpcJpFmMwxv7rP5uICepqkIGzYg6UsNJMO1uqzP6vdArwEwgJ7pFghtoBk-mXg6qJpXlwSDbB_pgSQSTfz8U2LUTmFGGnto7wx4m8XNB2t9y2UTdeHA3HtCKeYuCuTIafl4VdnoOpei8s6Zy-_joNuiTTcPpL8hdnUcah6lDsxC3kzJPBjvZ-0j2mrGYa7eqSOSJyM_9h93AVBEMPkQcFLmgcacnkutq52ogSZcf2PlEMcqF75uIo1E5a4yn4lJTe7Be5iAYASyu0rzp9xIr10UcyjEJw1xXFPf7vgal6iia410jLLkkkAFnZINjUzn8hY2QvbDt4McTaCOOltbmUeI3gF_uGsIcfCOn9DOkCq-cEciN_MzRa94KlahBBugz9R82-K5LhknMwO0sDl9HfuxiHnBkqt6x-cpLqeNrfi7BrZ2MqkiCdMcKgKaN9XuloIJWzEka0qyrfAd11ywTFMez8pGUyP4tE5fjDzEq9Y2x7zZF1i_OI8eMLXj8v2G7y6GcraIgJyvWQlfOsdDoR6g8j3XQQwP9FzzJ8fIyBv3NrGslTcREqq4lSr9R_iZ2z-Hgrf9IqGDawd0dlo14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=SIJcG-obCIkQ42NuVnmvkyxF7Fvl501-VJTaYPk1aj7M2guKwTNjJGyX_2H-5e-9q5H-aTrT9H7qTbyMjk-hTPxTpcJpFmMwxv7rP5uICepqkIGzYg6UsNJMO1uqzP6vdArwEwgJ7pFghtoBk-mXg6qJpXlwSDbB_pgSQSTfz8U2LUTmFGGnto7wx4m8XNB2t9y2UTdeHA3HtCKeYuCuTIafl4VdnoOpei8s6Zy-_joNuiTTcPpL8hdnUcah6lDsxC3kzJPBjvZ-0j2mrGYa7eqSOSJyM_9h93AVBEMPkQcFLmgcacnkutq52ogSZcf2PlEMcqF75uIo1E5a4yn4lJTe7Be5iAYASyu0rzp9xIr10UcyjEJw1xXFPf7vgal6iia410jLLkkkAFnZINjUzn8hY2QvbDt4McTaCOOltbmUeI3gF_uGsIcfCOn9DOkCq-cEciN_MzRa94KlahBBugz9R82-K5LhknMwO0sDl9HfuxiHnBkqt6x-cpLqeNrfi7BrZ2MqkiCdMcKgKaN9XuloIJWzEka0qyrfAd11ywTFMez8pGUyP4tE5fjDzEq9Y2x7zZF1i_OI8eMLXj8v2G7y6GcraIgJyvWQlfOsdDoR6g8j3XQQwP9FzzJ8fIyBv3NrGslTcREqq4lSr9R_iZ2z-Hgrf9IqGDawd0dlo14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی با چشم‌درد دیجیتال!
👋
👀
تا حالا شده بعد از چند ساعت کار با لپ‌تاپ، چشمانت بسوزد و احساس کنی  به یک لامپ ۱۰۰۰ وات خیره شدی؟
💡
😫
بیایید روراست باشیم: صفحه نمایش‌های امروزی مثل آینه‌های صیقلی هستند که نور را مستقیم به چشم‌هایت پرتاب می‌کنند. اما تصور کن اگر بتوانی یک لایه نامرئی از «کاغذ واقعی» یا «شیشه مات» روی مانیتورت بکشی. جادوی
Paperman
دقیقاً همین است! این ابزار با تغییر بافت پیکسل‌ها، صفحه نمایش را از حالت آزاردهنده به یک سطح نرم و خوانا تبدیل می‌کند، درست مثل ورق زدن یک کتاب قدیمی و دلنشین.
📖
☕
✅
چرا باید همین الان نصبش کنی؟
•
🧊
حذف بازتاب نور:
صفحه مات می‌شود و دیگر نور چراغ سقف روی مانیتورت نمی‌افتد.
•
🎨
تنوع بافت:
از کاغذ کاهی تا E-Ink (مثل کیندل)، هر سلیقه‌ای را پوشش می‌دهد.
•
🎯
هوشمند و انتخابی:
می‌توانی افکت را فقط برای مرورگر فعال کنی و در فتوشاپ یا بازی‌ها خاموشش کنی.
•
🖥️
همه‌کاره:
هم روی ویندوز و هم مک‌او‌اس به زیبایی کار می‌کند.
به نظرت کدام بافت برای کارهای روزمره‌ات مناسب‌تر است؟ کاغذ کاهی یا شیشه مات؟
👇
💬
🔗
دانلود:
Windows
macOS
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/6627" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اولین تریلر Cyberpunk  Edgerunners 2 منتشر شد!
🔥
انتظار داشته باشید که هر ۱۰ قسمت این فصل جدید،
پاییز امسال
پخش شوند.
آماده‌اید برای بازگشت به نایت‌سیتی؟
🏙️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6626" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حدود 900 تا کانفیگ مختلف
📶
https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Germany.txt
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6625" target="_blank">📅 20:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">#اختصاصی
🎧
استودیوی کامل AI: از ایده تا مسترینگ
۱۱ ابزار برای ساخت حرفه‌ای موسیقی:
🎤
تولید: Suno, Udio
🗣️
کلون صدا: Kits AI, Synthesizer V
🎹
سمپل/لوپ: Stable Audio, Splice Create
✂️
جداسازی/ویرایش: LALAL, RipX
🎚️
میکس/مستر: Sonible, iZotope Ozone 11
🔊
پاکسازی: Adobe Enhance
💡
نکته: ترکیب این ابزارها فرآیند تولید را از هفته‌ها به چند ساعت کاهش می‌دهد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6624" target="_blank">📅 17:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu7o_umjfjXq8DWQzPpBgzbnCmKho5v_TVG02Au800aXKKAt0uDHZf78aAOUD9jRLKRzR27vgUo474rydQDpAu2nSOgcaydoqyE9cN2ObxSyVqQ7uxaNXtksvj9wz_QN2koHV41gJ14hRxDSPRCl0fYRM9l0QsnBisjk6BFOPtJ7y2XeKR67XNYEuuWTxEIMXSv1OMQwxKyw85aPvR5gFgvpeu66BGDRkdXk0wSic0ndcw39Ihd851A-lMsgKuJ90Nsv6x-aiXL4ePWZ1txeQpr5uBVDVlYvJ7-iruPN66UOwNXshG6tS5uEdQ4mad-gkdxBZq1AzMfcgIiKr_ivfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GTweak؛ جعبه‌ابزار همه‌کاره برای شخصی‌سازی و بهینه‌سازی حرفه‌ای ویندوز!
💻
✨
اگر به دنبال یک ابزار پرتابل (بدون نیاز به نصب) هستید که کنترل کامل سیستم‌عامل ویندوز را به شما بدهد، GTweak یکی از قدرتمندترین گزینه‌هاست. این برنامه با رابط کاربری نوشته…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6623" target="_blank">📅 15:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین   بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .   irm https://get.activated.win | iex   اگر کد به مشکل خورد و اجرا نشد دستور زیر…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6622" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین
بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .
irm https://get.activated.win | iex
اگر کد به مشکل خورد و اجرا نشد دستور زیر رو بزنین ( نیاز به ویندوز ۱۰ یا ۱۱ به روز داره )‌
iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
Github
😀
📱
@Archivetell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6621" target="_blank">📅 14:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حجم : نامحدود
زمان : تا ۱۲ شب
vless://63b43d54-3bdc-4d9e-b3f3-10163c892936@64.90.7.102:8443?type=ws&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
وصل شدید بگید</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6620" target="_blank">📅 12:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNOQNbkNgplCw9E2JJKzoPYG3lI1ncBYiM4FAypZIYOkxjfPs4-70SbVKF3IgvLgmgsaiOkaRpAQF5gCe7P5duLPjmb4GR1_tEpDAwsx8H5pX3WMz9Z8DF82QbjhHw0xzcBHV8bYQYQJwrCLIfcIzA1WwOUiC3EQIntH0Tma-1nxh7NouSyhb_WbGNz_UWTG9bYax8jwv_NRQJEJreg9g1IizPtBTu5Odd9scYdRlnxdkyQSeMqtD53sa_yw3XSLn5kdqimRKXygLB6LXZR6PUPmDy6lQytHe-A8clymFej-O_ewPSEHeoYrZY5pJvQx9WLvpvsRBM2XivXhhfVTtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6619" target="_blank">📅 11:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqoUqQSZ8jv8Mg3dmhEdUmUuZc9Ih9wg0DBimmX8PeJ7lWFBOGKYMtg7Pabsn1pNSqNWfNHDuGxAFPPsBftqplh7Y6Qenl5CfTwpwcUNr7U9XX8mccbCAx9-gSXfPIqP4zLFKymk33nDHZZDR9bcB35GaZw-lnAX8LnICw994UV1Kzg9wKUe5emOhMYSKi7YK8LrFmjZk3e9a1N5OqpQqNhbWSLQKfo5AESYoA5x3SkI-SzJp4OSVi8ql-7L-MngsYiBzC1UyrS4b0Jc5ewnNDv8Yh7tSlHSHtMfroQBVDOVMEaQfTtpH835A5vY0t6JgNMm55dba3C4-fd9sBSUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Anthropic بسیاری از دوره‌های هوش مصنوعی خود را رایگان کرده است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6618" target="_blank">📅 09:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4WX1IVpNgHcsfkhbqiBIa7d0icySbn3QXe_oKmx974JNP9Uod1iLcF7nsVFmISwFnjOE3RKDvDBYM2b8xmA5nljmPUzWpA7S91MaDOIcA6Z8pKUE_4RdweHuizubyTSlj3JgR5J0pSCjLCY4q4tNOkdSK1ntmC_inthLeIoFY6rplvAf_oF6Fi3hNcZP3Y2gRRKg7KEqhi060kgidVXmJNYmf_Pup2rttMH6D7JGMxNFn4nAwun5iuFByZhAFInkIsU8DikOkwk2mpqZ8lLmMuXuQAbkGYiCkZFK1-SKIxIV-SUN045h-6YnrtG4KgCvTBZaXLeI58z-KAQ3ejvMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6617" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6616" target="_blank">📅 02:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=NNMp--wpI810-5bdObXpbuOMVLdkjcC9w7dYy2efRUCtPdiekyLMvF0y8JkIFFcPzSVPeC7115ZzFMzIbuLOSCxoiDa3XwOrgCCOBHnWdKW4-AT7AkoPh_p0mqTmLN2PTkb1UFalnby4dBTsCliCAP1XTxp9NqNKNgcOWzLTQYUFZnw0bBw3EDJZo4eqZoI8ScxfI_8P0Q9J7pZLtJ_L2oqeD7ww7Zw3gkhOPHsukceh65-qQ9a0Dw7J6S8-j8aMMiJofqrw3cA3g2K6Oze1XfWdOMDyjGF_sGDC8Ul1bU0jpisemNR8alAK6nSJzxtSWN9DjznSUWDiJe8-3eG8Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=NNMp--wpI810-5bdObXpbuOMVLdkjcC9w7dYy2efRUCtPdiekyLMvF0y8JkIFFcPzSVPeC7115ZzFMzIbuLOSCxoiDa3XwOrgCCOBHnWdKW4-AT7AkoPh_p0mqTmLN2PTkb1UFalnby4dBTsCliCAP1XTxp9NqNKNgcOWzLTQYUFZnw0bBw3EDJZo4eqZoI8ScxfI_8P0Q9J7pZLtJ_L2oqeD7ww7Zw3gkhOPHsukceh65-qQ9a0Dw7J6S8-j8aMMiJofqrw3cA3g2K6Oze1XfWdOMDyjGF_sGDC8Ul1bU0jpisemNR8alAK6nSJzxtSWN9DjznSUWDiJe8-3eG8Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6615" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6614" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=iYeD6AYXv7JM29477gHbV8N86uWN1cfhtYDUMBccmC7F08x_yONyOJ1HPjgDm8uEEpPBHRHIPmdOqD-aZyi1BfwKsBJP__c5-74NtYdVrL81S_eaVjHWHbX8Dtp1eIXCrsX32n0dcyXN9fbnA9-EPE9ykgowz9fM5esM3BEpL3dOz9-pdPLRItWWDBuJy7QvCqgWjJf6qoHk7FVmirdlXeO0dPUbeqMyBOk7i6vJb1AKcUiPwNCbCYPgD0NNzP3n7KscijPmPnX5Oi62l4lPlJv9G6lhIRBfIILRavsg-Y4obyDZOfjmABJSAvBw-glkh9qtCo89btOI4nqV6s-9uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=iYeD6AYXv7JM29477gHbV8N86uWN1cfhtYDUMBccmC7F08x_yONyOJ1HPjgDm8uEEpPBHRHIPmdOqD-aZyi1BfwKsBJP__c5-74NtYdVrL81S_eaVjHWHbX8Dtp1eIXCrsX32n0dcyXN9fbnA9-EPE9ykgowz9fM5esM3BEpL3dOz9-pdPLRItWWDBuJy7QvCqgWjJf6qoHk7FVmirdlXeO0dPUbeqMyBOk7i6vJb1AKcUiPwNCbCYPgD0NNzP3n7KscijPmPnX5Oi62l4lPlJv9G6lhIRBfIILRavsg-Y4obyDZOfjmABJSAvBw-glkh9qtCo89btOI4nqV6s-9uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DewatermarkAI
حذف واترمارک با هوش مصنوعی در مرورگر
این سرویس رایگان واترمارک‌ها را از عکس‌ها حذف می‌کند و فایل آماده را می‌توان با وضوح اصلی دانلود کرد.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6613" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCe8AfA0WEdYttK3oaxaM_ONKbWzgqqW4Z8aR210VdHoSWLEzNQx4WRM11JIg8ypyqMf3JtDhFUYj5N74QwJ1s9OxNsYq2hBKXajcxNjpPnH5glTMa7sYwnyxhJyG0ucuFBV3VFFI3cSePdrXu98dGn4792EKnNGQP2FOhyB6oJuP1c5Q_2kpz4GqaAy2I478WO_MYzbtMtrd06RSbHPxntNPekrpkGayX7eHTPzJpxjPgWohuzi5-UTSrm34GMkslIhu9Ocl5tUYLWP0G7jW8fqsje7ln6soiEBLhfhSf5w8DURXLqTBo-CpUoc1C2wrCscV7mrWpo246u004T2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از به‌هم‌ریختگی اسکرین‌شات‌ها خسته شده‌اید؟ Trickle دستیار جدید هوش مصنوعی است که همه اسکرین‌شات‌های شما را به‌طور منظم سازماندهی و خلاصه می‌کند
فقط یک اسکرین‌شات بگیرید و آن را به Trickle ارسال کنید. هوش مصنوعی پیشرفته Trickle یک خلاصه دقیق تولید می‌کند که اطلاعات کلیدی مانند متن، نمودارها و یادداشت‌های دست‌نویس را استخراج می‌کند و سپس می‌توانید این داده‌ها را جستجو و درخواست کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6612" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKYyNpssSZlSfDeXzsK1jfPfuHlU_ZR-EusLeCjoaLS8hVR14YZhfEPADsbFD57WGvrTd2D3miVQJobvFDLVHOKP8iz2nFGllyN1_JSlihSLoMOdQp8DN5w4G3Rx0aXU-c60BBbEjz-jF6uonxJwJ7rNqB2QOqHHr__XL5ynFsfX6WnK96gOOywUNqT-5IsoPtDbNUYY8ZTzFbTv-dEfCMxK5C31wfciMtvyoKoFN0BDAHhHu_GZYPdWgcsFJ1pV7UfAkH2aoPLHBNX5v2cZoY_H0q-snx6Bi9r-REN1S5SaGN_F7M_d6Wl30sqTztdsgWIpa1fVg0la9NZ2IEv52w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6611" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGsUO-lHaXqg_82zsCTNaaJyHeWXGDByNhhOF_O9hK04MPqcJMMQDbXQC_navXmowm67_7X6Bl1zGv50uklFp2-J4lpKSw7m0ccTtDvxJ_Uz-EGx4SyuA-RfJ7Q4HqIEUYNvuvYn7VtU_4tnbmu0Gz-cmtOu90VhgLWTVKsh2RdNE_NWrFtFfII4ddknTIzC8-R98BxubZCG7iTUKCnuJBRcrdUWC7wDDYSQOL9jXyD49C82X66zIy0cQ7tMlNIGV7WrVAjASO3rR1Pg9S_gvYygNidUwtbwzX7JfXzC2F3IciZIE9TeG_oKZsQKhyUqAGphZGg_SoVELpY9sfTugA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6610" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3_Y3x4PR98FMuIEtfsSPIu2FBvVQFT_VHSXi9Vd0T9MZ-mXHq-T0c2d4GN5mmTsm-ynZuLTE2HeAZnHNQlv3Azqaca5cMhJuEWyMTcerGLKtxVOkF9RXFDY4STNwOtm7v61DTyHj9Tkzjpac7qY5tOSEmrj8doBKQhBFQ-VZ974tHEtxgttK8qPQ8Ixmq4Ob2QezxvsyAQW6Nhml2e_wR1b1JUxh_n0k57OOzGNFOkG1KnRRp8o83KrNsMTjbAyzW0oQjczEMpHEvle3c2p05lpGJPg661t8cYnfSmhiad7Yl8ZZ-riG2ZORhbkaqsl7MNY23opNhiUZrq0_jHwiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6609" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خب Claude Fable هم استفادش برای مردم عادی کنسل شد
چینیا هم دارن مدرک جعلی میسازن تا بتونن ازش استفاده کنن
😂</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6608" target="_blank">📅 19:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6607" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8x_ILgTfCIbKDNRXJ9l8s8-wrHqBTc8QlCx1DmytBALNSHMmXxsNiV_BlJNQVSlaCLf9ppCFhBPsw6C34LneSDaTFxmhM6hC2oRpfltMBHYZk1K2Upc9kDVQ6kum9AXNHEyPBEz-BvN3N79onm47mrnqtxR3-tir-uabtu2-pmGRGjgEPixaDOqem-x203WzUhRHvq2xm0Z2z9EG9jsIadA0pu1s0M8VV8wdJf8NnMV3Ap_-gLZE_BZa-PFkah7TihvLLgJgiDOWb1tZIBmhv3MaFuXw0Bs1oyqLHHOQmyWHx0nKYAXXTZuyMTDlgEtNPOQ9zuD5t5seOOmGr9N_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6606" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
