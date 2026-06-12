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
<img src="https://cdn4.telesco.pe/file/qONBb2GlmMX-iD2P1oV46P-1ZMm_88oS-RAaDECW3XL1Gzb8r7UZrbqTg87Tfj3BtAfLyYzmoS55WCdsXcVrUSAXBSAYEJ3-ARawWVXA88Z2n8ecYXWTzIT4vDCV_MRo8G7HgwDnaeyA5H55heQVG6kCYFBlGAoyadI2PuFCW0D3qWldycdJsqoIY0QzG1F64mAAy1Mz_xJuq2d2pxPNJ2Oi8sfpopJdZAgZmFTNiKOzz_xTLb8ZWMs7vfYUNFYJdxg_IPaqUlKua1mAzHZqFrKmnM8K3gAINK8viF5xq9P01VrnAex3lIG4JewPEIAqvPmjcjWDz1vJh7v2BGK21g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.6K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 05:12:38</div>
<hr>

<div class="tg-post" id="msg-6309">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ :
با ایران به توافق رسیدیم،  توافق خیلی خوبی بود، دیگه هیچ سلاح هسته‌ای در کار نخواهد بود.
به‌زودی مردم شروع می‌کنن به برگشتن به خونه‌هاشون. تقریباً همه‌چیز نهایی شده و ما به هر چیزی که می‌خواستیم رسیدیم.
مهم‌ترین بخش ماجرا اینه که ایران هیچ سلاح هسته‌ای نخواهد داشت؛ نه خودش می‌سازه و نه از جایی می‌خره.</div>
<div class="tg-footer">👁️ 710 · <a href="https://t.me/archivetell/6309" target="_blank">📅 03:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔥
دامنه رایگان 1 ساله!
اگه دنبال یه دامنه رایگان هستی، از سایت زیر می‌تونی کاملاً رایگان برای 1 سال دامنه بگیری:
https://domain.stackryze.com/
✅
قابل اضافه کردن به Cloudflare
✅
امکان ست کردن نیم‌سرور دلخواه
✅
مناسب سایت، پنل و انواع پروژه‌ها
@ArchiveTell</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIWzH-x68xyFtzN4-lRIFjHMtlriawo0V-xQYEPH6pKBiAXwmS-_2cx31vt8k8b5G28eNcPrpQsIXuAl3VG-UPQLCY4WDxpaH1xMD1A8xHEB1EZeUPEJnLcPaSNWSp_8RKKJBF2QWC-ekwzV-gN9xx6Adz0cGJAbSkgiXz-mIheI5S6WdM2y5WUnakfDuPBclkjjkOfDX3Dmt73itVWci7v8HLFoBnK-AcXyFgmXhKjBkEL8wIipuMASjE0TGgQmzW-k67_SmnmWvuM-dxmQxJr6n2YG0OHdtRf132ie20dBX65NbmjyxI7qn1pcCSwK-fkxKmDSFv2lSQBqTl77Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵️‍♂️
CloakBrowser | مرورگر ضد شناسایی برای اتوماسیون
مرورگر
CloakBrowser
یک مرورگر مبتنی بر Chromium است که برای کاهش شناسایی ابزارهای اتوماسیون طراحی شده و تلاش می‌کند وب‌سایت‌ها آن را مانند یک کاربر عادی تشخیص دهند.
✨
ویژگی‌ها:
• مبتنی بر Chromium با تغییرات در سطح کد منبع
• سازگار با Playwright و Puppeteer
• قابلیت اجرا روی سیستم محلی، Docker و سرور
• مناسب برای تست، اسکرپینگ و اتوماسیون وب
• کاهش احتمال شناسایی توسط سیستم‌های ضدربات
⚠️
توجه:
هیچ ابزاری تضمین نمی‌کند که همیشه از تمام مکانیزم‌های ضدبات عبور کند. استفاده از چنین پروژه‌هایی باید مطابق قوانین، شرایط استفاده سرویس‌ها و ملاحظات اخلاقی انجام شود.
🔗
GitHub: CloakBrowser
#OpenSource
#Chromium
#Playwright
#Puppeteer
#Automation
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUz1-np2DAfyP8zrWDvw3UGyoscPmMpYAtifLkhR-N--4BKOMb9C3DKpo6tIxQUc71HdApU9GEePW7zL9lcKkmYozT3vMP6cX7JtfjxqIwkBlYjpJf4yHyFWx-n31LUF1_DZTWbfVjIkHO_3L1EYCPAwiPJCeEtME5kPdTlERsnb0iwLGyT2zAUHGM7gybQtM8vmyL2lHO3aSpzeNANsjt35Pq3Hxn9W5kcf7MKpDSwG8USsWcNpgCjNZ9h0p4FcHhyWWu1BjeKzYCEJKEvy2E5VAZFGgk-i58gfTAc9vxlbNpdLp63abTNRZxaMvFsB4LSRMaUn8QLzF22A8HOMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
📚
حل سوالات درسی در پیوی
🔸️
در بخش سرویس های هوشمند
🔹
امکان ارسال عکس سوال
🔹
جستجو در منابع آنلاین
📝
خلاصه خودکار موضوعات گروه
🔹
هر شب ساعت 21:30 ارسال شدن خلاصه مهم‌ترین مباحث در تمامی گروه ها
🌐
بهبود سیستم جستجوی وب
🔹
نتایج بسیار دقیق‌تر و معتبرتر
🔹
دسترسی به اطلاعات به‌روز تر
📰
آخرین اخبار هوشمند
🔹
هر ۸ ساعت بروزرسانی می‌شود
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEAdbwhkV9_wWrEzve7SAuc9r5bT8xMQSQEkoXqKPq7J8cXxJCqSpClphcC99I-ya4OU2mJZUdibDFKheSHiuQrVECsM42HL35h_2-dex9Td07ClRZRkGdIsMKSyV0WtGfbNB_EVSy9J8o6OmlRFsrOkYTiMMY4GyoTWXawS35ZJA4x9jXOLCqIM2lnPImJ1VwOi2roz5UPrickivQgjOfGdJHFnTKJmcizK4azVmakrU6dx4qGY1T9np0b7XQT5Cf3QDUAKx6haZp18mS4snN09iKnln_RTpXqo8gVqrbE3yccl7T0_lbbUR5tNnyehGDtQwVDeZ61OgDBro-tKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
OpenAI برای برخی کاربران API Credits رایگان ارائه می‌کند
اگر از APIهای OpenAI استفاده می‌کنید، می‌توانید با فعال کردن اشتراک‌گذاری داده‌ها برای بهبود مدل‌ها، به سهمیه و اعتبار رایگان دسترسی پیدا کنید.
📌
مزایا:
• سهمیه روزانه برای GPT-5.5 و مدل‌های Mini
• اعتبار رایگان API برای حساب‌های واجد شرایط
• دسترسی مقرون‌به‌صرفه‌تر به مدل‌های هوش مصنوعی
⚠️
توجه:
با فعال‌سازی این گزینه، بخشی از داده‌های ارسالی شما ممکن است برای آموزش و بهبود مدل‌ها استفاده شود. برای پروژه‌های حساس یا حاوی اطلاعات محرمانه، قبل از فعال‌سازی شرایط را به‌دقت بررسی کنید.
مسیر فعال‌سازی:
OpenAI Platform → Data Controls → Sharing
#OpenAI
#API
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=V9dTzqrYBNPhCYgfXk8vwes6q6NwMt7-87jmQHICj3DtNPXsNFLSOz3nM3pbjjtseK_kbbc_oBgfRFBu_1SCX4afbDgAFIMvfhDZqhFTLBOJn61QuMO-mlmg3M7wK4o8hcjz9BEZm2weOl1ydbAvV6DUwo-koptJTVAjC48qUeN5y7Xx8khOg6NSoarCDkzJf9P6ocescX05HiBn49fy2nM-x_lcgiYMO_xnrU7ZpRvnGH_1FW_aH8UBxwk_3TZCUB2JPRgkvKcBdHpTVgAZv1P_xA6eUvVYCHqgoZyNTlHMXjUC1JZz5lh8uAB-nZ7-a0-LMDEhM3OLKpCDSEdjIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=V9dTzqrYBNPhCYgfXk8vwes6q6NwMt7-87jmQHICj3DtNPXsNFLSOz3nM3pbjjtseK_kbbc_oBgfRFBu_1SCX4afbDgAFIMvfhDZqhFTLBOJn61QuMO-mlmg3M7wK4o8hcjz9BEZm2weOl1ydbAvV6DUwo-koptJTVAjC48qUeN5y7Xx8khOg6NSoarCDkzJf9P6ocescX05HiBn49fy2nM-x_lcgiYMO_xnrU7ZpRvnGH_1FW_aH8UBxwk_3TZCUB2JPRgkvKcBdHpTVgAZv1P_xA6eUvVYCHqgoZyNTlHMXjUC1JZz5lh8uAB-nZ7-a0-LMDEhM3OLKpCDSEdjIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsZYAzSWhF-ezMG01Gc-oG99UrJBsm3B9ZStBwbqMo1ZiA7d_6zyZx6fdc38kWv241oF4BqsLQT5oQTEcyXCAZlfqa2vP9WGPFrwpWon8H9Ar62WsISA3rhwucUCq9LqQqDhAK1SAuABqjYhUI_Uut5toNzWSKkatA3OTda6F5iJdSeXqwgaQvA90Ji-fu01zKqff3rDGN7f-hoSgZv0O0L09V4swNKlmOna5GDnDgmvqOw0giUhku1Az7wp4GMBgh7tsuAlbHBp-May84vg4F5dPCGFrmQG6MnNilhzwCN8phoenfZ05-ayx5n5uiNw5AfnVZDvYooDPKFyyb3oGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
RuView
با استفاده از سیگنال‌های وای فای، بدون دوربین یا حسگر، موقعیت و علائم حیاتی افراد را حتی پشت دیوارها تشخیص می‌دهد!
✨
قابلیت‌ها:
•
🔹
ردیابی ۱۷ نقطه از بدن انسان
•
⚡
خواندن تنفس (۶‑۳۰ نفس/دقیقه)
•
🛠️
اندازه‌گیری ضربان قلب از راه دور (۴۰‑۱۲۰ bpm)
•
📦
دیدن افراد تا ۵ متر پشت موانع و ردیابی همزمان چند نفر
🔗
لینک:
https://github.com/ruvnet/RuView
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌐
Javid Mask | ابزار افزایش حریم خصوصی برای کاربران استارلینک
اگر از استارلینک استفاده می‌کنید و به دنبال راهی برای مدیریت بهتر ترافیک شبکه، فیلتر کردن دامنه‌های ناخواسته و افزایش حریم خصوصی هستید، پروژه متن‌باز
Javid Mask
می‌تواند گزینه جالبی باشد.
✨
امکانات اصلی:
• محافظت از حریم خصوصی و کاهش نشت اطلاعات شبکه
• فیلتر کردن دامنه‌ها و وب‌سایت‌های ناخواسته
• راه‌اندازی ساده روی سیستم‌های لینوکسی
• پشتیبانی از Raspberry Pi (از جمله Raspberry Pi 5)
• دریافت به‌روزرسانی‌های جدید از طریق پروژه متن‌باز
📋
پیش‌نیازها:
• سیستم‌عامل Linux
• حداقل ۵۱۲ مگابایت رم
• حدود ۱۰۰ مگابایت فضای خالی
⚙️
راه‌اندازی:
1️⃣
سورس پروژه را دریافت کنید:
git clone https://github.com/rowdy-ff/javid-mask.git
cd javid-mask
2️⃣
فایل‌ها را بررسی و دستورات نصب موجود در پروژه را اجرا کنید.
3️⃣
پس از نصب، تنظیمات موردنیاز را اعمال کرده و دامنه‌های دلخواه خود را برای فیلتر یا مدیریت شبکه مشخص کنید.
💡
این پروژه بیشتر برای کاربران استارلینک در ایران طراحی شده و هدف آن بهبود کنترل شبکه و افزایش حریم خصوصی است.
⭐
متن‌باز و رایگان
🔗
GitHub: rowdy-ff/javid-mask
#Starlink
#Privacy
#Linux
#OpenSource
#ArchiveTell
⚠️
قبل از پیاده سازی و نصب، لطفا کد منبع رو بررسی کنید.
چنل ما هیچ تعهدی در قبال این پروژه ندارد.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n49BAMwRbDsZJqAVtou4f0alkTvV3gThExWzPIVPjBqpezWXz8newJlaj8LQSjqUCYBz1H-dS7H2JtspLagY-2Gj1jvC8lcBGVuwh_PUKOBHNsbzyDSL3iKjl2m1FAeZhFs3boXxejoMR13w59mxn_n0fhX3vjqiauakiA4W_S0HzNhBTqvVyg3opTHLZzmvoMloWQS63cQgR3N74wD51--VwxXrF1eMV1wep1PmhNUd3iselrtN14P6OZ5TKVjDMbl-x3yB_N4D_ZcMTRn89mQuyollEXu7CY8DdgIQ_65ICGwqWkw9aEEwLXTkePepap2VXU8-NE7DAonSS4vmFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2Nsi7i-V8kAQxI4SMOHqPKj_c054ghaxTj0siNBmn0xTjrSRulS2j4MQmQdktaTi2movZ4zVR_4jgCbFRybAqeB6cpyVtQhaEsf11qdQbODTV1BU-Kri1kHfPBLev8_fohHd79Ahtt3xaFzKgm1MV8-n5yuDEKraGxIZtECXNLhYteWSsSR2Ba-ZOaKgjqB-cF4EOCGESln3DO74X6OSzSW25_1B5R-cbgO948WnNatLD1p_CgjaFyrWRx-0AItYz1MNA37cHFDstp3aZfoxR3ueT_0iCN_x2k3C0kfENXR-aFr_YiDpagKS-4LVatyx8TpUSPQO6_nO4TJwbh-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMyrUuh-LQZl0c2vkEzlr4lxRTxvo4r9oIVBANS70uDxR6CIB6bS2mi6wuK9QgIdBdJiBXdqcs77cDOpqpTL2iw1F1ttzMgdB-HXiwHVqK90hFV2t4zEa8eV8QjTBDqs3ApZKMcPBXlIuXhlb_pfR5nRfOOHREV33zRCz45B0EToDzitsyaC6TpE5cyDk4URZDAz10vV729pNcr0I2jld-Eb7erSRuO84aSYjsi7x88B1hcqqbXNA0rs97y_HxqJrlCbHG7UkBgmzKSv9oQSYnH6QIxuB4iZpo0_PdhRSv7b5xjrw0hwctYOu0X_gt6hcO-XeVcc3OWZm4FYLM9sGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
شیائومی MiMo Code: مدل جدید هوش مصنوعی برای برنامه‌نویسان، با هدف پیشی گرفتن از Claude Code.
✨
قابلیت‌ها:
•
🔹
کار با پروژه‌های میلیون‌ها خط کد بدون محدودیت
•
⚡
پردازش مخازن بزرگ بدون از دست دادن داده‌ها
•
🛠️
آموزش مجدد مدل در حین کار روی پروژه
•
📦
تمام این‌ها به‌صورت رایگان و متن‌باز
🔗
لینک:
https://mimo.xiaomi.com/coder
#OpenSource
#Xiaomi
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=D-MZPSYv6-HW9JLassoioJEKjuz6LUMgQfM8FM_Q5egACrQNw14HWl1NjZNF309Zftg0vDUsr9b9Aa4xsadiiTewHinxsKPM9Jp2IIifofvp4PJoCvbg125OiNPuOMv2i1vTxwl-KPQ4uQSRiMVJ87BAeDsNrlkvZPP7m55RJp8tKL_XWLSBU7Mc7QjmVF-iNI3xEwS2RNQPPAA2l5jkrkhMl46mAYtV6nxFg-fkEHV0g1VLA0M7UNg_cWqN53i8BkQGtZim9j5MKdC_uIre4tpdvE30tTw1AUeiQDlYadrfF-CHnxoWdg4hLLoa7eFhZwtFoXBU35Mz_vst9kZaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=D-MZPSYv6-HW9JLassoioJEKjuz6LUMgQfM8FM_Q5egACrQNw14HWl1NjZNF309Zftg0vDUsr9b9Aa4xsadiiTewHinxsKPM9Jp2IIifofvp4PJoCvbg125OiNPuOMv2i1vTxwl-KPQ4uQSRiMVJ87BAeDsNrlkvZPP7m55RJp8tKL_XWLSBU7Mc7QjmVF-iNI3xEwS2RNQPPAA2l5jkrkhMl46mAYtV6nxFg-fkEHV0g1VLA0M7UNg_cWqN53i8BkQGtZim9j5MKdC_uIre4tpdvE30tTw1AUeiQDlYadrfF-CHnxoWdg4hLLoa7eFhZwtFoXBU35Mz_vst9kZaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Every‑PDF
ویرایشگر رایگان PDF با پردازش محلی و بدون ارسال به فضای ابری
✨
قابلیت‌ها:
•
🔹
افزودن متن، امضا، تصویر و واترمارک
•
⚡
تقسیم، ادغام و تغییر ترتیب صفحات
•
🛠️
رمزگذاری
•
📦
کار با فایل‌های بزرگ به‌سرعت
🔗
لینک:
https://github.com/DDULDDUCK/every-pdf
#OpenSource
#PDF
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📊
خلاصه یک سال فعالیت گیت‌هاب در چند ثانیه!
توسعه‌دهنده‌ای با نام
PankajKumardev
ابزار جالبی به نام
GitStory
ساخته که فعالیت‌های سالانه کاربران GitHub را به شکل کارت‌های آماری و قابل اشتراک‌گذاری نمایش می‌دهد.
🔹
کافی است نام کاربری GitHub را وارد کنید.
🔹
سرویس اطلاعات عمومی پروفایل را جمع‌آوری می‌کند.
🔹
سپس آمارهایی مثل تعداد کامیت‌ها، ریپازیتوری‌ها، مشارکت‌ها و فعالیت‌های سالانه را در قالب کارت‌های گرافیکی نمایش می‌دهد.
﻿
💡
اگر توسعه‌دهنده هستید یا می‌خواهید نگاهی سریع به عملکرد یک سال گذشته خود در گیت‌هاب داشته باشید، GitStory ابزار جالبی برای بررسی و اشتراک‌گذاری دستاوردهایتان است.
https://github.com/pankajkumardev/gitstory-2025
#GitHub
#Developers
#OpenSource
#Tools
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
دریافت ۲۵۰ دلار کریدیت رایگان برای API
اگر دنبال دسترسی رایگان به مدل‌های زیر هستید، می‌تونید با Agent Router API Key اختصاصی بگیرید
👇
🖋️
Claude Opus 4.6
🧠
Deepseek v4 pro
⚡
GLM 5.1
📌
مراحل فعال‌سازی:
1⃣
وارد سایت
Agent Router
شوید
2️⃣
اگر سایت به زبان چینی بود، از بالا سمت راست
🔝
زبان را به English تغییر دهید
🇺🇸
3️⃣
روی Sign up بزنید و با حساب GitHub وارد شوید
🐱
4️⃣
وارد بخش API KEYS شوید
🔑
5️⃣
یک API Key جدید بسازید
➕
6️⃣
طبق راهنمای این سایت، از کلید ساخته‌شده برای اتصال API استفاده کنید
⚙️
💡
با این API می‌توانید:
🤖
ربات تلگرام بسازید
🌐
وب‌سایت طراحی کنید
⚡
ابزارهای اتوماسیون ایجاد کنید
💻
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت عالی برای تست مدل‌ها بدون پرداخت هزینه
💰
﻿
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=jMgnJfIbe09kinAVPj1Xbfgfz0FllYksXyeAZf76WVbNC17_IXgWcAjSt4CfNljnAG1GSHhNkhFlMDnPInelLjzBogRFUOUbF65KPlzS8krSKtOpt8hEjBRwgVwl0kShW5FP2d1-anVGFsFIa7zcN5lyPao60TsxdeEluvq7Qpimi65_Fey2aJmV7byWJlew_XS2J3vHms7P7Bp0B1HcPx23NxP3MmjVFwefh2xHA94MNKImwS_Z7JSorf8G_46VE04mXS3v6v3y_TBQJFxZ4RomcDo0f1RQaCmoTuIFs6QmelqJT-a-cNMoM_cuy0z3NrehpRuL0tQsHiUsYNYMzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=jMgnJfIbe09kinAVPj1Xbfgfz0FllYksXyeAZf76WVbNC17_IXgWcAjSt4CfNljnAG1GSHhNkhFlMDnPInelLjzBogRFUOUbF65KPlzS8krSKtOpt8hEjBRwgVwl0kShW5FP2d1-anVGFsFIa7zcN5lyPao60TsxdeEluvq7Qpimi65_Fey2aJmV7byWJlew_XS2J3vHms7P7Bp0B1HcPx23NxP3MmjVFwefh2xHA94MNKImwS_Z7JSorf8G_46VE04mXS3v6v3y_TBQJFxZ4RomcDo0f1RQaCmoTuIFs6QmelqJT-a-cNMoM_cuy0z3NrehpRuL0tQsHiUsYNYMzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
OpenAI
تا ۵۰ هزار دلار اعتبار رایگان API میده!
🎉
•
🔹
۲۵۰ هزار توکن در روز برای GPT-5.5
•
⚡️
۲.۵ میلیون توکن در روز برای مینی‌مدل‌ها
•
🛠️
تا ۱۰ میلیون توکن در روز در سطوح ۳ تا ۵
•
💥
در عوض، داده‌های شما برای آموزش مدل‌ها استفاده خواهد شد.
📦
این ویژگی برای همه فعال نمی‌شود، اما ارزش امتحان کردن دارد — وارد OpenAI Platform شوید، Data Controls را باز کنید و به بخش Sharing بروید.
🔗
لینک:
https://platform.openai.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3JZIRE1RLVNckL6I-n5IL6alp26IFY-954mTQtCRQVd54Bil_vddMkNUggHrSX3PL71GuWo66xgYagjovoPmgAh5tiSmbJmZkSJJFiD05CWBy8tpWoKeJbKUYhMD0kvd6M6Nvh3M9K-0CfNuxr6CMPgkf68w9XTnhUTrwEMgjOJTEe_edYCHbDMcBF8nqC_ItDoNyEcqsrYPquJ0a78Rvwlu8BWm2FP3_nvp0v6wTIPj9wVw3Z9F8jc22MtXDyfOrA4liKyweszCsss_OFV41NXsBwDQjteNxhjBJ1TI_smhgFEGHyf1iKsKh6fXfZr6ZWotfjyKYkCT913AwJabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
BrowseryTools
مرورگر خود را به یک جعبه‌ابزار قدرتمند تبدیل کنید! 136 ابزار رایگان برای فایل، رسانه و هوش مصنوعی، همه در سمت کلاینت.
✨
قابلیت‌ها:
•
🔹
ویرایش تصویر و ویدئو بدون نصب
•
⚡
مبدل‌های فایل سریع و آنلاین
•
🛠️
ابزارهای توسعه‌دهنده با Next.js + TypeScript
•
📦
هوش مصنوعی محلی: رونویسی، ترجمه، حذف پس‌زمینه با Transformers.js
•
🌐
متن‌باز و قابل میزبانی مستقل
🔗
لینک:
https://github.com/aghyad97/browserytools
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=rsnFdIbQ7EdUW4SriP8UxysERPj82vv61oCmIWG49QZiZLpzKYH9PphtVFC9gImmtZQ_gjg5YtNQrDid1Gno8e9SaN68DCjw-qt2u1IDRxDxRDD3CX_KwqIhw42iANtE5QyuQNZ7xGsfKw9npQaRwjXG9blSkeoUg_X3o23-SvY8xe4suXf2fohJ9vPZY0f25nuwWZDYclSG1x1Dp8qyxm26ckyrxf40eiDBGbRvrn88POlIr9jPoPB5jDMS7OUuZCCfqErO2AwAAtKLA42vgwqjpTJ8Jls-Qnpgk21Ib5pNLxEdwrTZtuiQg4BSm_Z6l39KMA6aUerd2h48NgKV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=rsnFdIbQ7EdUW4SriP8UxysERPj82vv61oCmIWG49QZiZLpzKYH9PphtVFC9gImmtZQ_gjg5YtNQrDid1Gno8e9SaN68DCjw-qt2u1IDRxDxRDD3CX_KwqIhw42iANtE5QyuQNZ7xGsfKw9npQaRwjXG9blSkeoUg_X3o23-SvY8xe4suXf2fohJ9vPZY0f25nuwWZDYclSG1x1Dp8qyxm26ckyrxf40eiDBGbRvrn88POlIr9jPoPB5jDMS7OUuZCCfqErO2AwAAtKLA42vgwqjpTJ8Jls-Qnpgk21Ib5pNLxEdwrTZtuiQg4BSm_Z6l39KMA6aUerd2h48NgKV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه ImageToPrompt تصویر شما را در چند ثانیه تحلیل می‌کنه و یک پرامپت آماده برای مدل‌های تولید تصویر می‌سازه.
✨
قابلیت‌ها:
•
🔹
تشخیص سبک، اشیاء، نورپردازی و ترکیب‌بندی
•
⚡
تولید پرامپت دقیق برای Stable Diffusion، DALL‑E و …
•
🛠️
بدون نیاز به ثبت‌نام یا حساب کاربری
🔗
لینک:
https://chromewebstore.google.com/detail/ImageToPrompt/pgabcjhpgdcgbflabemecpficpknnpfn
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt-H7owtya1EUVM7_UiAaPX2d2OqGoT4UhBE5bHw5A14XnuKlIdtORwtiZfGK8Vt2k-tQac_N1Wd_rtFAY2TyKM1UfDPc6mB7F5Tnu2X3Sv5zVYFpDalkc36WPujM5OIrCQIcdVhlLaLuQW8skDuFzdWlZoGFFU6LuxshLN8v-se8MdTl4cm3IbXVNaSb2I51wHJVbvshxZpk0La5ihWJvIRkrFoSmcIsG8pjP1UeosjYz3Xr0eO8aBuAbvJlQ3XMLiXMR8nVH8tLjK_Roc4jnWxFALvClVXyJ8bxVxbmvo5MCLqg0dVvFE4SVjB9VrL5UwAH3QnphBBwQCzqKgErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتقال فایل سریع و پایدار بین دستگاه‌ها با قابلیت ادامه‌دادن پس از قطع
✨
قابلیت‌ها:
•
🔹
انتقال همزمان بین چند دستگاه
•
⚡
ادامه‌دادن خودکار پس از قطع ارتباط
•
🛠️
سازگاری با شبکه‌های پیچیده و متغیر
•
📦
انتقال تطبیقی برای بهینه‌سازی سرعت
🔗
https://shrimpsend.com
دانلود فایل مخصوص ویندوز ، مک و اندروید :
https://github.com/shrimpsend/shrimpsend/releases
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD7z8QsHw4ZjxzoEC7u98um3K4Vzn20Yof6wMNzjcgA5aQL319THDnJiHPx-_DUTHDaiZJYxikGYrz3yxjmiPSiXI_Kh1Gg0LT7YJc3srkkFlaVbj8kL40UctH7qTbZ60EcjBp5vbrwiRXI5GE3dRhiFiXIlQd4CccGsd9Z5aQAlNb12NTY4o2heYIRAJd4etGRcE9YAs4KjazVm4hzY04GJKTYdUWmF_1Hmu0P0iNHGpgj_hwCuuz8PYigiO5rEjgSq6KgXfi8O7cr2tTR0PsQNb4dl9hnCsyxjdiQLvHs6sBP5GqDq6mjW8n4_lXcrlYQOVlaZ8aqN7PJIMJpRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=qligJ1zp77J8v8MUnU_oJXRBska_Ij1S8e-uVATNGDkJuXvodilTPU0zgxkJlENAEIUTKyIdIz_Tb_9WTvQJkJ_zkNUbDpANG9L1fiImlsz1PFjLDIafIaEihriDh9Zo4ZOXUNsBsf8AAW0tqkEMiCGv7bMcIvyucg9DCyXjYE6Zkobu3YFtKUEFRjmIDFm4Ad3hb0yomkiq7Chc0ITSyukKbfjvWh0ChUl6FgdgeoD4jVDJtW2pTfkZJ2-9Yd_FbG_zW6AfMlWSRpIpQgHnCcEFcyR1Iyv9eJbCpYlKOW9CjaKbscpOn0TqLiQEFDBeJbZGZelk8Ad2w-fwtYew6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=qligJ1zp77J8v8MUnU_oJXRBska_Ij1S8e-uVATNGDkJuXvodilTPU0zgxkJlENAEIUTKyIdIz_Tb_9WTvQJkJ_zkNUbDpANG9L1fiImlsz1PFjLDIafIaEihriDh9Zo4ZOXUNsBsf8AAW0tqkEMiCGv7bMcIvyucg9DCyXjYE6Zkobu3YFtKUEFRjmIDFm4Ad3hb0yomkiq7Chc0ITSyukKbfjvWh0ChUl6FgdgeoD4jVDJtW2pTfkZJ2-9Yd_FbG_zW6AfMlWSRpIpQgHnCcEFcyR1Iyv9eJbCpYlKOW9CjaKbscpOn0TqLiQEFDBeJbZGZelk8Ad2w-fwtYew6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=R2KFvMNhn5VBlZqyspYo6B0tqSwdA-SIh6yXyRCdj6c1dPcw2Ry6cka0kcmZWnHirUUzuJxFfsEmR6fVfIloXJSpRDWf_94I78gMEAcKfsDpD3kS4AZbreX-N18TMDyzLhDfw7eRtpkS19pbZV6k1bOe75CvlVANANWhOJG1vk68VRUdzCAbtCQV4VOUsJhDRdSOt2jp-u5W39mK8_7NSR27bPG2bOEgUvby4UEXbRySVmrXJ8hgzBf5Am9pRT15DI6D2NhE39NSxiZBMoVcjFpkgNIhZ2M9hk4-fjeszYNGLVLA-3Jy40vOuV4EDAXysDh7hjP3mua0uVR6WX0nnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=R2KFvMNhn5VBlZqyspYo6B0tqSwdA-SIh6yXyRCdj6c1dPcw2Ry6cka0kcmZWnHirUUzuJxFfsEmR6fVfIloXJSpRDWf_94I78gMEAcKfsDpD3kS4AZbreX-N18TMDyzLhDfw7eRtpkS19pbZV6k1bOe75CvlVANANWhOJG1vk68VRUdzCAbtCQV4VOUsJhDRdSOt2jp-u5W39mK8_7NSR27bPG2bOEgUvby4UEXbRySVmrXJ8hgzBf5Am9pRT15DI6D2NhE39NSxiZBMoVcjFpkgNIhZ2M9hk4-fjeszYNGLVLA-3Jy40vOuV4EDAXysDh7hjP3mua0uVR6WX0nnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=Fd5sJJjllUUtUNqvqxDrMFz-TuNqGp-9BCD3jLEFCoKmZKhvERbjeu9KtVSll7XqzpZeGjma4nooyC9ockQ2HMiCGKm0aXQVJXg_aWYWLZpgn72zF0a-DFtKBrD53q4l9zLCyl1OHBHlNJ0aJYjgUJMdrxCjPaRGT4A5FPJ27WXmmawaPUUxT22vkzeTr_8n3aP3GxnI7VI2hD0hgMSdvQEFy7z04V3Tan2T_vWQA6BZTW4HaCQfmnODv5YtRIvJ93EHi9-jFwEzTB2iGLi8PuI9LQ94FjULi_mrxzqEB4H2yLbZDQWIUFqEgZcbdnvjC0CEkwuhSkgTnr8zVUchJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=Fd5sJJjllUUtUNqvqxDrMFz-TuNqGp-9BCD3jLEFCoKmZKhvERbjeu9KtVSll7XqzpZeGjma4nooyC9ockQ2HMiCGKm0aXQVJXg_aWYWLZpgn72zF0a-DFtKBrD53q4l9zLCyl1OHBHlNJ0aJYjgUJMdrxCjPaRGT4A5FPJ27WXmmawaPUUxT22vkzeTr_8n3aP3GxnI7VI2hD0hgMSdvQEFy7z04V3Tan2T_vWQA6BZTW4HaCQfmnODv5YtRIvJ93EHi9-jFwEzTB2iGLi8PuI9LQ94FjULi_mrxzqEB4H2yLbZDQWIUFqEgZcbdnvjC0CEkwuhSkgTnr8zVUchJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📝
جنجال جدید در دنیای آفیس‌های متن‌باز
پروژه
Euro-Office
نسخه 1.0 خودش رو به‌عنوان یک جایگزین اروپایی و متن‌باز برای Microsoft Office منتشر کرده، اما این ادعا با واکنش تند تیم
LibreOffice
روبه‌رو شده است
😬
🔹
بنیاد LibreOffice می‌گوید Euro-Office خودش را «اولین مجموعه آفیس متن‌باز اروپایی» معرفی کرده، در حالی که LibreOffice سال‌هاست چنین جایگاهی دارد.
🔹
همچنین توسعه‌دهندگان LibreOffice معتقدند تمرکز Euro-Office روی سازگاری کامل با فرمت‌های مایکروسافت، عملاً آن را به یک «هم‌پیمان غیرمستقیم مایکروسافت» تبدیل کرده است.
⚡️
به نظر می‌رسد رقابت بین پروژه‌های متن‌باز برای جذب کاربران و سازمان‌های اروپایی وارد مرحله جدیدی شده است.
#OpenSource
#LibreOffice
#MicrosoftOffice
#EuroOffice
🐧
📄
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvgmJp61mDFyiklTWVZMGE9ntcQ0Zlos6WZtw4m9TMw9Sc5gmxz6xSgNxz3GPx4A3kvdtmvqDdBQj7e2DlzmkbJp3Ec6uMOJX4-7ZkgVyCwZtr-FMxF2yiR7eV_KQMzHuTsVgjaYsFeyhts0vuiN1XV-p6z5rfucD33SjtJ7yKvuxu9EysnjcGf42ulEN0mOrQ6hwbhMS5DkD9wc2nCLk79Vc6xZ2GnoDN2hzxmVDq3KlSsjVaxOMDZv8Bn1UU2tmZ5UcipQGsKZvzmDveAUdfheb6txRShqhZHEIHSDkrs6Y81MR7mO8rpOP0qMO8nli3Jw97pheuSya_lbY_RKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ZOOOP: همه ابزارهای خلاقیت هوش مصنوعی در یک پلتفرم!
🎨
🤖
✨
قابلیت‌ها:
•
🔹
تولید تصویر، ویدئو و صدا با یک کلیک
•
⚡
کلون حرکتی برای انیمیشن‌های دقیق
•
🛠️
قالب‌ها و مدل‌های محبوب پیش‌ساخته
•
📦
یکپارچه‌سازی ساده و سریع
🔗
لینک:
https://zooop.ai
#OpenSource
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM68W7YxhY5inPBKQj5OdRe9edFqKbBd5B1pbjVhaAAuNx1E4flM9DRU0-VslcZLoCkSE85aG2xYF06VvR_xa5Cw2eXuY_mIByVLu9O_GtYCD0Ts-RaZrpStBTqqFiLoYBeKDZjIYlblR1kR0s9IGYP3voSr9LhVGKzh4tKTjGbaH9Xc8j8ic9PTGZKmSKQdiDm7HfEaSHIf8rnOzZk5kDDmmC3CnOIyeM8qT4xUdsUNitSkbUIamXZKaH4I7fX7nI1yH8Us3yP5XX89Tn-KBtyddhAljFBRcjG7OXghzx_y__f422r9O_CBHdeJOcGSl3ql2FAExa7MCcEt2NPCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵🏻‍♂️
با این ابزار می‌تونید فقط با وارد کردن یک نام کاربری، حضور احتمالی اون رو در سایت‌ها و پلتفرم‌های مختلف بررسی کنید.
✨
قابلیت‌ها:
• جست‌وجوی خودکار در صدها سایت
• بررسی شبکه‌های اجتماعی، انجمن‌ها، پلتفرم‌های بازی و سرویس‌های دیگر
• نمایش تطابق‌های پیدا شده در یک فهرست
• اجرا مستقیم داخل مرورگر، بدون نصب برنامه
• امکانات پایه رایگان
🔗
لینک:
https://whatsmynameapp.net/
#AI
#OSINT
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=UTUIWsKYEbQuglYfRQWdY5HxwOc60hTloUbtSDXb0T3TCepVdMLuwOkXgKtoZPar-i7S5icyMY581SECe8ef_JCHZSequCCNROPMy-_gAJdY4O1ZmzKCae8VYNgWp7yJNiJP8p-GO0_udYXsr7LwrtlO0Sahz2_ZtRWHlXAdqlZpG1ylV6oL28ReewYqyPgijsspbgco38haz62hXIvUUkRJyJI9EYJXEt9Uqds6KpYW4wV49WK9tyjqAXG1lQjia1vIq73VB6ywo9dgpC0bqvI2HUIla65mxQXBPUNLhV16CwuMS7jYAXyzA0kMYIAPcvRpNHYipkHOwy-quEGYuYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=UTUIWsKYEbQuglYfRQWdY5HxwOc60hTloUbtSDXb0T3TCepVdMLuwOkXgKtoZPar-i7S5icyMY581SECe8ef_JCHZSequCCNROPMy-_gAJdY4O1ZmzKCae8VYNgWp7yJNiJP8p-GO0_udYXsr7LwrtlO0Sahz2_ZtRWHlXAdqlZpG1ylV6oL28ReewYqyPgijsspbgco38haz62hXIvUUkRJyJI9EYJXEt9Uqds6KpYW4wV49WK9tyjqAXG1lQjia1vIq73VB6ywo9dgpC0bqvI2HUIla65mxQXBPUNLhV16CwuMS7jYAXyzA0kMYIAPcvRpNHYipkHOwy-quEGYuYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تست رایگان Battlefield 6 در استیم شروع شد؛ تا ۱۵ ژوئن می‌توانید این شوتر را بدون پرداخت هزینه تجربه کنید.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان محدود تا ۱۵ ژوئن
•
⚡
شامل ۵ حالت بازی مختلف
•
🛠️
تجربه ۴ نقشه چندنفره
•
🗺️
بازگشت نقشه‌های کلاسیک مثل بازار قاهره از BF3 و جاده گولماد از BF4
🔗
لینک:
https://store.steampowered.com/app/3028330/Battlefield_REDSEC/
#Battlefield
#Gaming
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سیستم جدیدی به
ربات
افزوده شد.
✨
از این پس، در بخش
سرویس‌های هوشمند >> آخرین اخبار
، امکان دریافت اخبار روز ایران و جهان فراهم شده است
📰
🌍
هر دو ساعت اخبار بروزرسانی خواهد شد
✅</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🦀
Asterinas 0.18 منتشر شد
پروژه Asterinas یکی از جاه‌طلبانه‌ترین پروژه‌های متن‌باز دنیای سیستم‌عامل‌هاست؛ یک جایگزین مدرن برای لینوکس که تقریباً به‌طور کامل با Rust نوشته شده و روی امنیت حافظه، کارایی بالا و سازگاری با اکوسیستم لینوکس تمرکز دارد.
در نسخه 0.18 تمرکز ویژه‌ای روی اجرای Asterinas در محیط‌های کانتینری و مجازی‌سازی بوده و قابلیت‌هایی مانند Namespaces، cgroups و بهبودهای مختلف VirtIO به آن اضافه شده‌اند.
از دیگر تغییرات مهم:
🔹
درایور جدید NVMe
🔹
بازنویسی درایور فایل‌سیستم EXT2
🔹
پشتیبانی بهتر از نرم‌افزارهای لینوکسی
🔹
اجرای برنامه‌هایی مانند Firefox، QEMU و Codex
اگرچه Asterinas هنوز فاصله زیادی تا جایگزینی کامل لینوکس دارد، اما یکی از جدی‌ترین تلاش‌ها برای ساخت یک سیستم‌عامل مدرن، امن و سازگار با لینوکس بر پایه Rust محسوب می‌شود.
#Linux
#Rust
#OpenSource
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3-GeXdlfmye2mobNKMzrAcFGxRYEtb1C2xneoV3KVMqoC2W7R3tq59berEmUX67Ng-ieFlFRVaZ3QHL6dD4tlGmO_qvH2_rzBqZ0wqFwGCz-F1MSyVJOJeTqkuYedykZsbWduJu_PV7vdYGsWWQLBg6Xi1nMnpwtItSfDvhRwxcUMeNLBDZ1FMieZqliod8cSleRSP8kWoEsOtvThhkSpvRvQYfMevi_SF634aHltkYBQ6iwgpVhF3xNeChG-g4BKcdYM9iLMrdzghfQFsMF_N7fSRZRoa_eUkVV1-TYP7wvHDkHKWZt_J9rqN6xSboNhekyNI5kcS9X4HcWXB9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
یک ویرایشگر ویدیوی رایگان که مستقیم داخل مرورگر اجرا می‌شود و فایل‌هایتان را روی کامپیوتر خودتان پردازش می‌کند؛ بدون آپلود در فضای ابری.
✨
قابلیت‌ها:
•
🔹
ویرایش چندمسیره ویدیو
•
📝
انیمیشن متن برای ساخت محتوای حرفه‌ای
•
🎧
افکت‌های صوتی کاربردی
•
🎨
تصحیح رنگ و بهبود تصویر
•
📦
خروجی با کیفیت 4K
•
🌐
اجرا در Chrome و Edge بدون نصب نرم‌افزار سنگین
🔗
لینک:
https://github.com/Augani/openreel-video
#VideoEditing
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=SjjYtaVCqYJoSaL_LTsZkB4DF9SxOb4uRcRl2R-v8yJY6huEV668R-PHi0eaYakFcj-mVOX9JzjVd-W8cLjvSY_jYP6ByJWUGIxigcgDikoPzhtAZvYEfOgE3P0E04kRUUIGZ7O3M7JPB8jbDaJYCB72TYurM7xYOqR8PTQywjpuRLweLtZu1uhyIFJLWMZxxNR4bJrHC00VCC_MChRl0nnZsXxRSFVtcwTGvtaGP9j2sbXt9_cTSN9Leewtmn4CZJgfKrlvJ84hbCu1nyg4i1bZh4kpAMEXJmCDpHPu4TFcfmbdteEKb3uVYT4TjprEhu-u8EHtmJZO2K3iMkTYVLRsrjbdTpxshV_DKlL_fVZ0vnkA29ufAGuQjzO8g4_IlJnnOsEa_5BKwTcHHNWUDsGTl5fj2E7vT8gdUcjMzc8mDOPCK9SBk_xeXt2uPdCAA2ZchNMqmTywpNgGqQcRTzEz0fnuVPoQiPd8u4VTsw9FFXg3xnWo-G10zWwc_VrIfd1Uh5zWI-qM_X9cv97Bh11OeXYKkW0svduUQVKUG6TdFMDN8tR3UHFuDjsIPBl12Ycwr-P6XuDbTzghSRrWonTSBDPRSljoyGqfKw__vr8MEwVsAZWGj-xO1aOErB4MKiEVJI0baxy6VfRe8U4mFtOUSAotlnmhbwXlSGn976U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=SjjYtaVCqYJoSaL_LTsZkB4DF9SxOb4uRcRl2R-v8yJY6huEV668R-PHi0eaYakFcj-mVOX9JzjVd-W8cLjvSY_jYP6ByJWUGIxigcgDikoPzhtAZvYEfOgE3P0E04kRUUIGZ7O3M7JPB8jbDaJYCB72TYurM7xYOqR8PTQywjpuRLweLtZu1uhyIFJLWMZxxNR4bJrHC00VCC_MChRl0nnZsXxRSFVtcwTGvtaGP9j2sbXt9_cTSN9Leewtmn4CZJgfKrlvJ84hbCu1nyg4i1bZh4kpAMEXJmCDpHPu4TFcfmbdteEKb3uVYT4TjprEhu-u8EHtmJZO2K3iMkTYVLRsrjbdTpxshV_DKlL_fVZ0vnkA29ufAGuQjzO8g4_IlJnnOsEa_5BKwTcHHNWUDsGTl5fj2E7vT8gdUcjMzc8mDOPCK9SBk_xeXt2uPdCAA2ZchNMqmTywpNgGqQcRTzEz0fnuVPoQiPd8u4VTsw9FFXg3xnWo-G10zWwc_VrIfd1Uh5zWI-qM_X9cv97Bh11OeXYKkW0svduUQVKUG6TdFMDN8tR3UHFuDjsIPBl12Ycwr-P6XuDbTzghSRrWonTSBDPRSljoyGqfKw__vr8MEwVsAZWGj-xO1aOErB4MKiEVJI0baxy6VfRe8U4mFtOUSAotlnmhbwXlSGn976U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
نسخه ۳.۲ مدل Ray از Luma منتشر شد؛ اما طبق تست‌های اولیه، هنوز با رقبایی مثل Seedance فاصله قابل‌توجهی دارد.
✨
نکات مهم:
•
🔹
پشتیبانی احتمالی از خروجی HDR با فرمت EXR 16-bit
•
⚡
تولید ویدیو تا ۱۰ ثانیه
•
🛠️
ساخت ویدیو بدون صدا
•
📦
ضعف در بافت‌ها، انسجام تصویر، دینامیک حرکت و درک پرامپت
🔗
لینک:
https://lumalabs.ai/ray3-2
#AI
#VideoGeneration
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXOD0caqzz9yqnfaCrxZAv3McqOZTvoUR79h7W58AaRGCEDfzYqt5-7EowzAJafHjx2gLk0_3OTK5ptmAMPpPgQ59cOrEZZYdrJhPgUGhzJRVhPuF4PiZK5kCdLZvjrWsWQJHAY9VqWGH3DCHXEdnWuifR42orOrKRxDH5tuB_JF05-x6JwU5O7qEuSFJPNYMlNeDIk1OrNIVzPgn6jItGhWcTj-Xwsmm2kbQzRxLmVlXeX3K29ORAkiZLQUA2D8bxMiquiDv2IU1tF3_y-x9df4SuxnYhd_Jj3FIRtlJSD_lobgNrYDAqFf-ECVxs5A1kGMYe5kF9kk0B4OsVBdvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttH0vohhR3kR0IbgG90Pa4eMFdPOD2PT5niAbiHu7WH6pZKhLDo4EM7jr6I3yo-RJ5rCu2SeYlFWtBDWCyxiAhTmdZk7J7U-QYH43UyVpcoD5VW3GBPS6R0LVX9pGsHt2y5yLpoEUYx5Hh-k1-uvUmdwy6AOQpBDexiUVjs3ZGQCvq3atV2e0cAJK_21PtJmHHWRPIjSdKBTtJtSGUrMys7r0IKRXRNxsUSZ-eXth2ppMIJwnWkAfTspNGog1EIJ83r8IBTmAMGsmZzErlTla17haiNe80XgM2jejM094YEmQvLmrPC37GhAVjvN2Tc6jPTRJqaNlHAefpNryBcomQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
CodeWhale
یک عامل ترمینال رایگان و متن‌باز برای کدنویسی با DeepSeek و مدل‌های محلی است.
✨
قابلیت‌ها:
•
🔹
خواندن و ویرایش فایل‌ها داخل ترمینال
•
⚡
اجرای دستورها و کار مستقیم با Git
•
🧠
حفظ زمینه بین جلسات کاری
•
🛠️
پشتیبانی از MCP، مهارت‌ها و ابزارهای اضافه
•
📦
اجرا با DeepSeek، OpenRouter یا Ollama
نصب سریع:
npm install -g codewhale
🔗
لینک:
https://github.com/Hmbown/CodeWhale
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آپدیت جدید
ربات وگا
انجام شد
✨
- اضافه شدن GPT-5.4
🚀
- اضافه شدن Gemini 2.5
⚡️
- اضافه شدن Flux 2 Kelvin
🌡️
- جایگزینی Lucid Origin با Flux 2 در گروه ها
🔄
- حل مشکل هنگ کردن Gemini 3
✅
- رفع سایر مشکلات
🔧
>
آموزش گرفتن API رایگان GPT-5.5
<
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💵
گوگل اشتراک AI Plus را ارزان‌تر کرد؛ حالا فقط ۴.۹۹ دلار در ماه با ۴۰۰ گیگابایت فضای ابری.
✨
قابلیت‌ها:
•
🔹
دسترسی پیشرفته به Gemini 3.1 Pro
•
🧠
Deep Research برای موضوعات حجیم
•
📒
NotebookLM برای تحلیل و ساخت پادکست
•
🎬
تولید ویدئو با Gemini و Flow
•
☁️
۴۰۰ گیگابایت برای Gmail، Drive و Photos
🔗
لینک:
https://gemini.google.com/app
#AI
#Google
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📱
اگه حافظه آیفونت زود پر میشه، iMole می‌تونه حسابی به کارت بیاد.
🔍
این ابزار فضای ذخیره‌سازی آیفون رو بررسی می‌کنه و دقیقاً نشون میده کدوم برنامه‌ها و فایل‌ها بیشترین فضا رو اشغال کرده‌اند.
☁️
از بکاپ‌گیری افزایشی هم پشتیبانی می‌کنه و می‌تونه داده‌ها رو با بیش از ۷۰ سرویس ابری مختلف همگام‌سازی کنه. بعد از اطمینان از سلامت بکاپ، فایل‌های اضافی رو هم پاک می‌کنه.
💻
روی ویندوز، لینوکس و مک اجرا میشه و خروجی JSON هم داره که برای ابزارهای هوش مصنوعی و اتوماسیون کاربردیه.
🛠️
پروژه کاملاً متن‌باز و مناسب کاربرهای حرفه‌ای و علاقه‌مندان به CLI است.
https://github.com/chenhg5/imole
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cj1tiyuXGFWMj-YQkR1MGzatrsesMur257kUTCY7zmdtTQOFndfT9R7T6siH7E-ZyJ1t7Z5MkH1F8GJoy9BWCvUYlg_4J3fkJ3EklkEfhAXzDk57_6pJcK1qDERHt0Hrrd_RalJwLQ542e1nMmAZyMxl1Zc0McKH3c00mwqE4_BX8CQWr3UWRXONL0SqSJKLI_dzKf5mhVbqydA8t6sYRwpfbrZF96wWxcB6jzAUoD_ZlxFHkhvxqJjOAysXy_EKKgrMER5m3LmtjdhBCQCrvNHMdAxorlVKW7ddWenQWjQb42OCyTM2eoArRSl0Dn--CW-DlNcv66W_r0PXpORMVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf0sjlll7DFFBB61nxe_Mp0EUKDDtHDrL6E8sNgl9qzq28G1E9dsgUPCgv4qXa_x0WpSNV5HHf-Bmhkl4Q4F7Cc5YO6n1nhj6mttRRSsok4eqfhKToY1JDMdEakUlqTlnT3hSqSm6w-i0kYf67Lh9UIo4fsrAkUOrwH2M5qrSl_lmPJ7ZTCkutqmSztqXrk4z8C6AsZ2A7ssckd2ViDDwZUFV6kRX4y5MNzWwBEpj9RnfgUii_4ZKGHEmyVhbhapQmSRkUNf3uvkKZQ4sBPj-o2InbBwt-h8hFKYrois2pCNvXhA2SsvTOEwMwTXdr3DdHj5ZOzYsemtegyv5psngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با «تحقیقات عمیق محلی» می‌توانید پژوهش‌های محرمانه را روی سیستم خودتان انجام دهید؛ رایگان و متن‌باز.
✨
قابلیت‌ها:
•
🔹
جستجوی خودکار در وب و منابع علمی
•
⚡
پشتیبانی از arXiv و PubMed
•
🛠️
کار با مدل‌های زبانی مثل Ollama و GPT
•
📄
بررسی اسناد شخصی و محلی شما
•
📚
تولید گزارش نهایی همراه با ارجاعات
🔗
لینک:
https://github.com/LearningCircuit/local-deep-research
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6250" target="_blank">📅 10:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZT2NN_IisMoZPc8BbH2_7cBtAGDicuQ-cywkZiI47SrIVJa5YFCLGfHIjhmtGngdBsTGtGmkfsbZL39QUdeVNr1xpB5u2t67g0sVFVUfi7eWXiW_evE3VvTeI8c8JIzm5xc_TPGBUycHgpK9lzqn79Hfao3_lM0Nuf0SDFr49VF6ex_mCRW9y0R4O_N2dKhrH86rl_pzW67m4iNuAvPRneObry0kkRtMt687FMfCtxm3Gq4kBrjaMX22chv7EELHP14U7RrUOdd3hSORjgaWohcJeses5vs0APeT7Djq7lZTdLweyGrWp-vzVP61w4UJ3chyU5yZRZZiPXU7YreMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید
اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت Split Tunnel برای انتخاب برنامه‌هایی که از VPN استفاده می‌کنن
🔹
پشتیبانی از پروفایل‌ها و سابسکریپشن‌ها
🔹
متن‌باز و رایگان
جذاب‌ترین بخشش اینه که از روش‌های پیشرفته عبور از فیلترینگ مثل Hysteria2، AmneziaWG و حتی olcRTC پشتیبانی می‌کنه؛ روشی که ترافیک رو شبیه تماس ویدیویی نشون می‌ده. همچنین توسعه‌دهنده‌ها اعلام کرده‌اند نسخه ویندوز و لینوکس هم در راهه.
⭐
برای کسایی که دنبال جایگزینی متفاوت برای v2rayNG، Exclave یا Hiddify هستن، ارزش یه تست رو داره.
🐱
GitHub:
https://github.com/yanisplugg/olcvpn-client
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6249" target="_blank">📅 10:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=UTPvAs-_L4k9Z3poqT4BfxzW-5nqfRs5DzCXCHgGs2tDQ4DbEReKzu_6m3aAvOKlv-Ii11y9GEVJuk8Y6mrw7AbWnS5bSRvVIke8PRfeHc1mRGzOp0vH8VkA4SXd_v4rvNqf-u5wUZkFvmfy95a9pJ21mizsu-8q6dvLup-kAopCAJmN2IbIvxLXOX0wtynWE1QEj06uJSbfirSmlQauzWZ6MZcKM8c0Hf6oCWv7Jfxm03cpEM-TZXvyH_MQx5NrmabGdhKsOPAPPJ0GO8GwdnACPQeptaxd34GdkIOvJgNfk2ZfcaS0P4bInNA2fzuOUlsa8_WoF4Hjabv0MHumjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=UTPvAs-_L4k9Z3poqT4BfxzW-5nqfRs5DzCXCHgGs2tDQ4DbEReKzu_6m3aAvOKlv-Ii11y9GEVJuk8Y6mrw7AbWnS5bSRvVIke8PRfeHc1mRGzOp0vH8VkA4SXd_v4rvNqf-u5wUZkFvmfy95a9pJ21mizsu-8q6dvLup-kAopCAJmN2IbIvxLXOX0wtynWE1QEj06uJSbfirSmlQauzWZ6MZcKM8c0Hf6oCWv7Jfxm03cpEM-TZXvyH_MQx5NrmabGdhKsOPAPPJ0GO8GwdnACPQeptaxd34GdkIOvJgNfk2ZfcaS0P4bInNA2fzuOUlsa8_WoF4Hjabv0MHumjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhubLAL6B9ryzN8OLeAiqcLy1qbxqGLhNrJPDvg-4RtBzvUVzx_YghSPTjjOVKXimyRiuXs5nzsP_DrQiS6PMeTAdEfSXa25uCi7R29rc06W3dl5OtpvKmXGMFcBF00Bw_0FEIw5fG1mrit582ZdhEfwpUIfVikunNLNOisCdSnNS7YbpBCKArnR8zbFE6BsASg_8gkfGFmaN1KGL3JX30E2wcVDSjaxa4x2-QUqGbUfpLUq1q5MLCR375xeFN5omVI1CVGX-A171gwy92cBlJRyyxY9hHm79zjOK4c6nCoyqNYWRtnx9-uOUp-pcU-djKj4mmDGsIs0Md5ZYS4dOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک فهرست بزرگ از ابزارهای رایگان هوش مصنوعی برای تست، توسعه و اجرای مدل‌ها
🤖
✨
قابلیت‌ها:
•
🔹
مدل‌های متن‌باز؛ از مدل‌های سبک خانگی تا گزینه‌های قدرتمند
•
⚡
ارائه APIهای رایگان برای توسعه و آزمایش
•
🛠️
اجرای محلی مدل‌ها با تمرکز روی حریم خصوصی
•
💻
دستیارهای کدنویسی رایگان جایگزین Cursor و GitHub Copilot
•
📦
فریم‌ورک‌ها و دیتابیس‌های کاربردی برای ساخت سیستم‌های چندعامله
🔗
لینک:
https://github.com/12britz/awesome-free-models
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💻
NekoBox 5.11.18 برای ویندوز، لینوکس و مک منتشر شد
🔹
یک کلاینت متن‌باز و قدرتمند مبتنی بر Sing-box برای اتصال به انواع پروتکل‌های ضد فیلترینگ.
🔹
پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria، TUIC، WireGuard، SSH، Tor و...
⚡️
🔹
دارای حالت TUN برای هدایت کل ترافیک سیستم.
🔹
سبک، سریع، رایگان و بدون تبلیغات.
🔹
گزینه‌ای مناسب برای کاربران Clash Verge، Hiddify Desktop و v2rayN.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJU0GylyaownB1aUMBWci168WH3TVCzBpfFd-Go8KVhRbWJoiXwApWKu5Pc4Hk0s-IB9gTC5Bi7AaHLFndhBOY3khUov17_Npz9B4oGsgA3RAMMnlFGlsdx4lAYmWVkX5kJrOqK6b1rOZ0o7P0HSyPpwgfcO4tEf3SEolV3JCvmzX3lmq-hrlRLd0dHZzDNcEQaiMEgfindoywH4j385EMtuB5Yvte848APNpVGib8S-ktutx0JTz460XTjR4jwjqIWFbUcQU6wUuaWsHuuRFHFjOAZisaryWJdU5kEQM0PYD2xSRdBVXFpQgV5rzuy9-OSr3HrveBO_OYP0JCfmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
😱
💻
اگه با 3X-UI کار می‌کنید، یه پروژه جالب به اسم X-UI-PRO منتشر شده که کلی از تنظیمات REALITY و WebSocket رو خودش انجام میده و دردسر راه‌اندازی رو کمتر می‌کنه.
🚀
🔐
این نسخه Nginx رو هم کنار 3X-UI میاره، SSL رو خودکار تمدید می‌کنه، روی پورت 443 کار می‌کنه و حتی برای مخفی‌تر شدن ترافیک از بیش از ۱۵۰ قالب فیک استفاده می‌کنه.
👀
⚡
از Sing-box، Clash Meta و Cloudflare هم پشتیبانی می‌کنه و برای Ubuntu 24 و Debian 12 آماده شده.
🛠️
اگه دنبال یه پنل کم‌دردسرتر برای REALITY هستید، بد نیست یه نگاه بهش بندازید.
https://github.com/mozaroc/x-ui-pro
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hala Hey _ Live In Concert</div>
  <div class="tg-doc-extra">Armin Zareei _2AFM_</div>
</div>
<a href="https://t.me/archivetell/6243" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">امشب رو با این معما بخوابین
شرکت در کنسرت این شخص، از نظر اخلاقی، غیراخلاقی هست؟
#Moral_Dillema</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6243" target="_blank">📅 02:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIqmt8QOsOkD-4D6nnfnR9yIZIc7nO9N5kFzZ_Lxlkl20pJtEDykdD0pzeGXcJ9hVTxBNULwsphmCd3GAptha_0qm_LaqNFH97BcV46-W2ULmnjmcPFDqwjKciq4-pQsESdbnYAwJ_3yv9LHJr3yqG6l8pOiHWWvNL0A9wtleo36GMDtj-AUDNW7O5p76F1FfHDIgdM5AgYet-C4GtwGjOUxgRq7NtVHMsIfbxKMP4_mk9yBTkqTmVK7a3hk7i9l_M6p__7rq-Z-UbB7CLbtV5n-ymRM6FjZqn4beOm2PtBMzLxG9euG-D-nOgtaqktB7gfe93Q1424cw3gxAZT1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Gemma 4 بدون سانسور منتشر شد!
🔹
یه نسخه دستکاری‌شده از Gemma 4 اومده که تقریباً هیچ درخواستی رو رد نمی‌کنه.
🔹
روی سیستم‌های معمولی و حتی آیفون هم اجرا میشه.
📱
💻
🔹
حجمش کمه و با Ollama و LM Studio هم سازگاره.
🔹
جالب اینجاست که با وجود حذف محدودیت‌ها، کیفیت مدل تقریباً مثل نسخه اصلی مونده.
⚠️
طبیعتاً دیگه خبری از فیلترها و محدودیت‌های امنیتی نسخه اصلی نیست.
👀
🫠
..
#Gemma
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6241" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
بی رفرال
🤐
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 140 / 140
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6240" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6238" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app
بخونید نظرتونو بگید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6237" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">StormDNS
a.cyntarix.com
25ffbc77bcfb23b2d4ee225eedcd2466
داشته باشید اگه نت قطع شد</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6236" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این پروژه پایتونی جالب هم برای تشخیص اشیاء توی ناحیه مشخص شده کاربرد داره مثلا طبق مثال خودش که با QWEN ادغامش کرده یه نفر با هودی اومده توی ناحیه مشخص شده تشخیصش داده و به گوشیش نوتیف فرستاده و گفته چه چیزی با چه اطلاعاتی اومده توی ناحیه.
برای دوربین مداربسته خوبه یه ناحیه رو مشخص میکنی هر چیزی اومد توش بهتون خبر میده،کد اصلیش با پایتون نوشته شده و از ابزارهایی مث ffmpeg برای مدیریت استریم‌های ویدیویی استفاده می‌‌کنه.
github.com/roryclear/clearcam
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6233" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6232" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هر کی 99 تا رفرال داشته باشه ی کانفیگ نپستر میدیم بش
😌
🔥</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6231" target="_blank">📅 00:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6230" target="_blank">📅 00:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6229" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTTWEx7VzOKw8NpVkqI5w02vk3hWpoFZRNXA4mV7Q_Gr8P7RCUPaZsRpPfSguy9tezPSp25SkmTJgtO8aTeCqCfXiMzrsYQ4qjJlxdsh9WMrpIBbAvFzKYp59TOAj9w4RW31FngeDF7vOpD7f_h9VwpYW-_CpH7jUwFZ0YUksL88NxKxD6XCtYsYidrEMELWAJHCntAYyCG1Lj_gWcxFKocjurenA9LTNYo98P4QNM6xWsmt16GStjj9xI7ryXGgPWXJtNu7vqEvCTpEiyLAou31vuJWygPE5hlmcQkgFtuFgeTaCDWbtQkGA62bVPlO4RjDUV4brW4eZc5mr-5Dwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Gitdot؛ رقیب متن‌باز GitHub که با Rust ساخته شده
🔹
پروژه Gitdot توجه زیادی جلب کرده و به‌عنوان یک جایگزین مدرن برای GitHub معرفی شده است.
🔹
این پلتفرم از ساخت مخزن، Push/Pull، ریپوهای خصوصی و عمومی و مهاجرت از GitHub پشتیبانی می‌کند.
🔹
رابط کاربری آن با الهام از ابزارهای CLI مانند Vim و fzf طراحی شده و روی سرعت و ناوبری با کیبورد تمرکز دارد.
⚡️
🔹
قابلیت‌هایی مانند Pull Request، Issues و CI هنوز در دست توسعه هستند.
⚠️
با وجود استقبال کاربران، Gitdot هنوز در مراحل اولیه توسعه قرار دارد و فاصله زیادی تا رقابت کامل با GitHub دارد.
🔵
@ArchiveTell
| Bachelor
⚡️
https://gitdot.io/</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6227" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🛑
پایان uBlock Origin در Chrome نزدیک است
🔹
گوگل آخرین راه‌های دور زدن محدودیت‌های uBlock Origin را مسدود کرد.
🔹
پشتیبانی از افزونه‌های Manifest V2 به‌طور کامل در حال حذف شدن است.
🔹
فلگ kExtensionManifestV2Disabled نیز از Chromium حذف شده است.
🔹
مرورگر‌ های Edge، Opera و سایر مرورگرهای مبتنی بر Chromium هم این مسیر را دنبال خواهند کرد.
⚠️
نتیجه: نسخه اصلی uBlock Origin به‌تدریج از دسترس کاربران خارج می‌شود و کاربران باید به uBlock Origin Lite مهاجرت کنند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6226" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=K0gCX28Brekg5RNKMN0GsUONRoxmYUxm5BvRoOw-fDuxWQtkgR862jcCL0vnoSwXDR3cilr90JqpTDYIF5oCbUD3QrRdN9weqxSnwRJKr9RaZPOtgSyxOtvfb3LDlARWkQc3V_jqVNFq6Rh3B3OodtGQuP1TxJPoeq8WPasrw94b4H4AUhPBAoGHPPwOryEZzoVG2bbEAMu7f2yF0hXMR7d4fVYvSLxPGtjiJOFI50Ixu20XUSgGHs4-AKdYAxgIXk5Ho8QSateb-BZdGRVh6kC39puUP5tZC0OFIlJl3OeaIWMYErfiahjZWJdcZ6TSPWh6yzHJv7XgtL5C2-stQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=K0gCX28Brekg5RNKMN0GsUONRoxmYUxm5BvRoOw-fDuxWQtkgR862jcCL0vnoSwXDR3cilr90JqpTDYIF5oCbUD3QrRdN9weqxSnwRJKr9RaZPOtgSyxOtvfb3LDlARWkQc3V_jqVNFq6Rh3B3OodtGQuP1TxJPoeq8WPasrw94b4H4AUhPBAoGHPPwOryEZzoVG2bbEAMu7f2yF0hXMR7d4fVYvSLxPGtjiJOFI50Ixu20XUSgGHs4-AKdYAxgIXk5Ho8QSateb-BZdGRVh6kC39puUP5tZC0OFIlJl3OeaIWMYErfiahjZWJdcZ6TSPWh6yzHJv7XgtL5C2-stQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6225" target="_blank">📅 22:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Awuvm5mhXjHcz-0NnGjb4X6etFq8DNPCmZH9ivuOkNggNlpLnu5tKFbnquUZvzHt72wR9k2Dq37FDAhD-7-8yytm_ShVjyceWKQy_AnS813RwGZsxvi6zTC-ME6oKLNDUR_W0yODOFpbNdbHI0da2S44mHRJxgcyeogzFZ2NgNsNE0SiIaZtW4LRpYKUucCe1e5jcgHGW2U7j7LJ9xFCIrxGGG1qNJnpWtcq4yWkGG7GCtX1CHthRxKZSfZJNYBcT1k4XbrLTAfx6a8r6nTljzRTX6ONbJsI3lWVym0pjszLJ91ZD_b_6N85qKXYAJ6-4kGknkX6aGXf3rrTcf_ofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک ویرایشگر ویدیوی کامل که مستقیم داخل مرورگر اجرا می‌شود؛ بدون نیاز به Premiere Pro یا CapCut
🎥
✨
قابلیت‌ها:
•
🔹
پشتیبانی از چندین ترک ویدیو و صدا
•
⚡
رندر سریع با شتاب سخت‌افزاری GPU
•
🛠️
افکت‌ها، ترنزیشن‌ها و ابزارهای تدوین
•
📱
قابل استفاده روی کامپیوتر، تبلت و گوشی
•
🎬
عملکرد پایدار حتی در مرورگر معمولی
🔗
لینک:
https://tooscut.app/
#VideoEditing
#Tools
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6224" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">طبق درخواست شما عزیزان
تمامی سرویس هایی که API رایگان هوش مصنوعی در اختیارتون میزارن رو مجدد قرار میدیم
✨
Freemodel.dev
🥇
developers.cloudflare.com
🥈
console.groq.com
🥉
aistudio.google.com
build.nvidia.com
cloud.cerebras.ai
openrouter.ai
console.mistral.ai
llm7.io</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6223" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry9i13PXSIx9I8poqK52U7t9zMvJgpCk2Gg0817dcGqEX1PBGJHrh29pRBhSr6mSmzmkaz35iqvWJyMgBpHRVWKAzGUsegOXewV6kArOuOUtTsxoV8zHGwY42X3kau6sw9LmHm_OdzDiuIUK9JWkHoPEQrE_kZZjjwhIncrZD6nETTZAunN-QWtYjAkDWxmYyYeTtaBIQGkWG8rtJgjc3s2F1I-Eu-v-PYPKZD-lnv56QDB4pMqB0z4QcsqM5Vno9VCq9Nlza02Ifk8kOqSFS-BYf1WHdFkkwrvczZyxahGZBDK0sSsRTtrxXtlU32zLOY06XYiz2pJDKViuATKekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
کاهش بار اضافی روی حافظه در ویندوز ۱۱ — غیرفعال کردن فعالیت پس‌زمینه Edge
😎
این کار از طریق ویرایشگر رجیستری انجام می‌شود:
1️⃣
کلیدهای Win + R را فشار دهید → regedit. را وارد کنید.
2️⃣
به مسیر زیر بروید:
HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Edge
3️⃣
روی فضای خالی کلیک راست کنید → «ایجاد» → پارامتر DWORD → نام آن را «StartupBoostEnabled» بگذارید و مقدار آن را 0 انتخاب کنید.
4️⃣
کامپیوتر را ریستارت کنید.
پس از این کار، Edge دیگر در پس‌زمینه اجرا نمی‌شود و منابع را مصرف نمی‌کند.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6222" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">walf.zip</div>
  <div class="tg-doc-extra">12.9 MB</div>
</div>
<a href="https://t.me/archivetell/6221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ℹ️
فایل سرچ پروتکل و سرور ویندسکرایب
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6221" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
برنامه WALF منتشر شد!
اسکنر خودکار سرورهای ویندسکرایب نسخه PC
اگر از عوض کردن دستی سرورها خسته شدی یا دنبال یه راه سریع برای دور زدن فیلترینگ میگردی، این برنامه دقیقا همون چیزیه که نیاز داری.
کار برنامه چیه؟
برنامه WALF کاملا خودکار و بدون اینکه نیاز باشه کاری کنی، تک تک سرورها، شهرها و لوکیشن های ویندسکرایب رو روی پروتکل ها و پورت های مختلف تست میکنه تا بهترین و سریع ترین اتصال رو برات پیدا کنه.
👇
چطور کار میکنه؟ خیلی ساده:
۱. فایل برنامه رو از لینک زیر دانلود کن و از حالت فشرده درش بیار.
۲. فایل walf.exe رو اجرا کن و دکمه Start رو بزن.
۳. تمام! خود برنامه اگر ویندسکرایب بسته باشه بازش میکنه و شروع میکنه به اسکن کردن کل شبکه تا بهترین اتصال رو برات ردیف کنه. (فقط مطمئن باش که قبلا توی ویندسکرایب اکانتت لاگین شده باشه).
لینک دانلود برنامه سرچ خودکار پروتکل پورت و سرور های ویندسکرایب در پست بعدی
⬇️
با تشکر از چنل
@CubicDreams
که زحمت کشیدن ساختن
🙌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6220" target="_blank">📅 19:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خب یه پست اختصاصی دیگه داریم این فایل رو خیلی جاها میلیونی میفروختن در حالی که رایگان بودش یکم دیگه پابلیک میکنم
🔥</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6219" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv4mUfeZwhpFcbkW49kaiUstiqmZEKiTtdKBAxh93mf2hKXZJCSUV4NxbyRe_SZc7jo6QoVzvF8qEVUBJ6ncGDQDo-c4gOcUMRAnRPFodS4GedVWIwtRzJreTxpNQ0N4CI0yzmzcsl3Ung7nFmQLcGWQQBEQfiWMrBnznBxR_z2DMDMvo2VIMNqD4u9alsP4tnxff34YmNjwRXedZuBkVUqO2v8OwYHer2Uwnj8rg8kYUfgLW2_lQlUOdROFYrI9l4EEKEm5DXjIW7xSohOCsn9ygRfKhB-SzqZuaFVPUc1JSLdlXaUKK7oh2v3wCiS-x3d7789iP0fxzutpWCP_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel  اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت Freemodel شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6218" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚠️
اطلاع رسانی برای افرادی که اشتراک ویندسکرایب پرو خریداری کرده‌اند:
پروتکل
ikev2
روی تمام لوکیشن ها (تقریبا) متصل میشه
✅️
با تست هایی که گرفته شده با فیبرنوری مخابرات  سرعت همه سرور ها دانلود ۲۰۰ مگابیت و اپلود حدود ۵ مگ فعلا قفل هست
(پیش‌بینی میشه پهنای باند ikev2 کم کم محدودیتش برداشته بشه و به قبل شرایط ۱۸ و ۱۹ دی ماه محدودیت شبکه برگرده)
سرعت کانکت شدن به سرور ها و امنیت ، این پروتکل خیلی بهتر از tcp هست حتما استفاده کنید
👌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6216" target="_blank">📅 18:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6215" target="_blank">📅 17:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel
اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت
Freemodel
شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
بخش اول: احراز هویت با شماره تلفن
🔹
بخش دوم: احراز هویت با تلگرام
✅
گزینه احراز هویت با تلگرام را انتخاب کنید.  لینک ربات تلگرام برای شما نمایش داده می‌شود. وارد ربات شوید و استارت را بزنید
🎉
پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار  هر هفته: ۶۶ دلار اعتبار
💰
4️⃣
از منوی سایت وارد بخش API Keys
شوید و یک API Key جدید بسازید.
5️⃣
در بخش Docs می‌توانید مستندات کامل استفاده از API را مطالعه کنید.
🛠
تنظیمات نمونه:
model_provider = "freemodel" model = "gpt-5.5" model_reasoning_effort = "xhigh" disable_response_storage = true preferred_auth_method = "apikey" [model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses"
🤖
حالا API Key و مشخصات بالا را به هوش مصنوعی موردنظر خود بدهید و از آن بخواهید برایتان کد تولید کند:
✅
JavaScript
✅
HTML
✅
Python
✅
PHP
✅
Node.js
✅
و بسیاری زبان‌های دیگر...
💡
می‌توانید با آن:
🔹
ربات تلگرام بسازید
🔹
وب‌سایت طراحی کنید
🔹
ابزارهای اتوماسیون ایجاد کنید
🔹
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت خوبی برای تست GPT-5.5 بدون پرداخت هزینه است.
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6214" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6213" target="_blank">📅 17:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
hysteria2://5z15av99psrlhdqp@32.195.51.20:39150?alpn=h3%2Chttp%2F1.1%2Ch2&fm=%7B%22udp%22%3A%5B%7B%22settings%22%3A%7B%22password%22%3A%22dlxmzvxvcp3i6v0e%22%7D%2C%22type%22%3A%22salamander%22%7D%5D%7D&fp=chrome&obfs=salamander&obfs-password=dlxmzvxvcp3i6v0e&security=tls&sni=32.195.51.20#usa_hesteria-%40u2vpn-100.00GB%F0%9F%93%8A
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6212" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پروکسی‌های اختصاصی آرشیوتل
😎
⚡️
پروکسی ۱
🚀
پروکسی ۲
💥
پروکسی۳
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6211" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwm6GSwNnWAlT1za6QweNJMzCEEH5NbaQ6N9RAD6mNIxgO-LIfu062QftHwoClYf42QPOUxEWbsLYaSs4QU0-gYKTWQxcJohCxDnHfTAxlOdxsOWmK9Fq9mllL23CmnJMgxE9gUiZrPjUcWE73I2S-5-eiKilcZh1JS_djQTi-mHJw0r1MCFl-0wyu-8uwVpoBzdMCUjKzevN7Q5dXjr_Mi9TbkTyEXd6IKEQHEmYJ8XmH948GhhySc5vJeRkJsiPJRlW8fhltT8GR7FVt95ZdUc2dzFYB_DwVduXegZkzovKByynhEY5GTEF9rl_vx5FjyX_MZKNbCAqgbvyoHB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب یه روش مخصوص ایرانی‌ها اضافه کرده، رو همه اپراتورها عالی کانکت میشه:
Settings → Connection → Anti-Censorship
گزینه Protocol Tweaks رو روی Enable بذارید، بعد وارد Configuration بشید و یکی از دو گزینه آخر که ایران هست رو انتخاب کنید. گزینه Large TLS رو هم روشن کنید.
پروتکل های udp و tcp رو تست کنید
ایرانسل tcp 587 france
مخابرات همراه اول udp 80
با فیک میل اکانت بسازید
https://windscribe.com/signup
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6210" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1wOb9ZLRXjhPgqiYoumgXjmF2kM7aH0fr0NKjzWq69AVEOvEgQQlSoYuZivn18sCMh7kiGwPvlPwrw2q-nIt2d1keJFQcW0gU33Z2gFm33ehmpQciEPeQHxMExJvNo4aPTyg4DvLSfPxZ7bbqQoV10YWJq7X-HjJ7GVXnHZbE92Mn-_7TlPqt0wg2lnPW8dpnsFpDTOWWEyTRZ9E7wha_Z817IGYLd6J-ZGYjSwffYKWx9VFk3hVnd8YJHQtukB3bGPYm26dhYKMpYjEBWdRtSPdKl0UBulqG6ea6N9QKGKlN_LCz0ebrj7RKv6DZouNye4QPuiTXy_zhv0eDC6XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
Impeccable
‏این ابزار به عامل های هوش مصنوعی کمک می‌کند تا وب‌سایت‌های منحصربفرد و بدون الگوهای استاندارد ایجاد کند
🔥
‏
✨
قابلیت‌ها:
‏•
🔹
آموزش عامل‌های هوش مصنوعی برای ایجاد طراحی‌های منحصربفرد
‏•
⚡
کار به عنوان منتقد، توسعه‌دهنده front-end و نویسنده UX
‏•
📊
آزمایش ماکت‌ها، برطرف کردن خطاها و بهبود طراحی
‏
‏
🔗
لینک:
https://github.com/pbakaus/impeccable
‏
#هوش_مصنوعی
#طراحی
#OpenSource
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6209" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdwERbXmIj1bOxGN7SswVXJqOBoHk4Y0LQJVeCEiN1aNyNSTYJoT5p_FMaydh1amNJGvEm5STQlYnRPX1NW04eJEvGiYrTo7klqXQn5NkSzIkMReIstP5geCmXhW_aK1vLcg42xg-4-E6y4uG0UQDbrGAfgjfDrN_zOpmCj4-xDhbmBoqQvZf2OS5qgMLBZ3KQKOPUYSs8CTGLn0zosA_iOVcdqtGjc1qGBWOnXcF72ssAI-HP_ePAX7uc3uOaBITgFzFHymiT0RFhub0EK_FldX3_2kv5G87k6L3n9HjNs7qWg-pYnZWABlLsNk0xTzYDhGukMaSOu3nuubaY6YjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkdE__OLsIoD04J1uhm_YcSk4CM8qkbd6I5w6vuhr7HAusY55fTVaxg2nps1jukj4RShcNRa10H_aTwGw13S2QBhokt12oXgCP_xZmo7MsGfiCrpeOFI2LBq3GIKggWIQZ5NA9MTUYlZB9a0VO4z7RmCSquQZhNnaYVyGBYuCH4Fo0uzxhKbyJKkc8H9odruUS2MX0VpWEUekxBJjAUNDXyqHb7hNJhROm2mbxBhoEbWnPZyYgSHEzZLR9BT2q9kMZZROdSMIhSCTTJYmp4v019SdKmVqnQKU9lMx97jFjh2Q6Q1WQ-kdCqVUilBKIMnrF0D6rpWay55F_vYniIPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEoQc0tu0Qe9gvuNtS5sWxd1szGxhlbxdp75CI0TNaE54EgCVMh-nDXsruN7KOIL9j0IkQVi10k6srhFXdtJLLnPbJlmoOt-Z3dBB9L18LS1Jxw2n_L1VURN1-Ex89e2FTIbX6mcMJdkQjEC-ciX-FOiY63DEiNEPgcC0QvxTA0IQ7v5yvUbNiw_V8erK61n_u7GpjSpvpKSumLu9nfu2UC8SEqJwNXjv7Uq9d_XJId8k2g9pW5-mGig1WNpe3QfaxQhJ-li-66kAqeSXZt87LMBtMIV6IpMVo0WhejkB6ulkylqhmbifPPcuo28wcd7BXeMNx_gyVhf5KsPT0tOfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=U0-I56x_-unmnn18HCB9P_F7oCpwf0lAczeOD_YJG8kUjzoyGpFwJdPzicH8IsZxBMGFBqgBxHikLKvUSR1o-1W6x4CT78Z8yz0FnxxhNfZHAk_svP3AbNNSpTBFGsBa9E_Sxte19IAugjM6vUpUgbjqZqfNH8HjP9VSbVO_H5609r_sAO-TdefeUBzmEqqg6y-RugLNDpd8yVejVo627vDh-iG2owdDTGoYREydL6BYV-xWPYjgbTRSKE9j1jTjx3ThQv_CW4ynHzn_x8pzyIIJFIJmbabMmPLhACfhyJqS7GkN_ghZmp5SstDK5w5daaVqtxhoGAzwcVDAd4QU-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=U0-I56x_-unmnn18HCB9P_F7oCpwf0lAczeOD_YJG8kUjzoyGpFwJdPzicH8IsZxBMGFBqgBxHikLKvUSR1o-1W6x4CT78Z8yz0FnxxhNfZHAk_svP3AbNNSpTBFGsBa9E_Sxte19IAugjM6vUpUgbjqZqfNH8HjP9VSbVO_H5609r_sAO-TdefeUBzmEqqg6y-RugLNDpd8yVejVo627vDh-iG2owdDTGoYREydL6BYV-xWPYjgbTRSKE9j1jTjx3ThQv_CW4ynHzn_x8pzyIIJFIJmbabMmPLhACfhyJqS7GkN_ghZmp5SstDK5w5daaVqtxhoGAzwcVDAd4QU-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
هوش مصنوعی Siri یاد گرفته است که عکس‌ها را مانند Nano Banana Pro ویرایش کند.
✨
قابلیت‌ها:
‏•
🔹
«بازآفرینی فضایی» برای تغییر ترکیب، زاویه و پرسپکتیو عکس‌ها
‏•
📸
ویرایش پیشرفته برای ایجاد عکس‌های خلاقانه
#Apple
#Siri
#Ai
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6205" target="_blank">📅 12:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDP-aNCajMYt1zCJBzJZKsmMQCsORJIdpp5QZN9CMHOwz208ZV5FnSCp3TcOh3Q_L76i2oQuueaC1Li7cm4hIQEkFOXHmA4GsNInYX2j9D-9Rhpn2Q4weywizMbT3cHcE0opXd8JnwLg5tm5gDz0qKcXldWPXy1fdjr5enL5nBcaJR7eRhqipJfgoFTvfKhuWdzOdsRjL7IDIY0OKMSZo5grnM-qG51wVF--7Vxeaj4d6nLr7msze4UmfeQqgXkvTq39Wje0VF75plpFfv292k8DuESZKOtNy7ktHQ5z7RLKL67SccX4K6Qo84jnBP5iGawADqF4IGV1cPdyhttHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
.FrameCoach معرفی شد!
‏این ابزار هوشمند تنظیمات گرافیکی ایده‌آل را برای هر سخت‌افزاری انتخاب می‌کند و حداکثر FPS را استخراج می‌کند
🎮
‏
‏
✨
قابلیت‌ها:
‏•
🔹
انتخاب کارت گرافیک و پردازنده
‏•
⚡
انتخاب بازی از کاتالوگ
‏•
🛠️
دریافت تنظیمات بهینه برای حداکثر FPS یا بهترین گرافیک
‏•
📊
مشاهده تأثیر هر پارامتر بر عملکرد
‏•
📈
تست تنظیمات و پیش‌بینی فریم بر ثانیه
‏
‏
🔗
لینک:
https://theframecoach.com/
‏
#گیمینگ
#بهینه‌سازی
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6204" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">با پلتفرم Cerebras به مدل‌های قدرتمند gpt-oss-120b و glm-4.7 با محدودیت بی‌نظیر ۱ میلیون توکن و ۲۴۰۰ درخواست در روز دسترسی پیدا کنید
🚀
شما می‌توانید کلید API خود را دریافت کرده و پروژه‌های هوش مصنوعی‌تان را با سرعت و دقتی فوق‌العاده پیاده‌سازی کنید
🛠️
. این یک موقعیت عالی برای استفاده از مدل‌های سنگین بدون پرداخت هزینه است
💸
، پس آن را از دست ندهید!
✨
cloud.cerebras.ai
🔗</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6203" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=PYW2THU9r6VgDeWlqz2tx3wXFff1mrmDL7D8PC8CqEsyRShrzn92VyyW2r9C4AbmL-AU60WzQ4rNYHEgxxnqrD2xQiNksMTHAHXIDMzs-DF_wFRfdEOTfi5e7yvWJ0K26lrPck0iFTEVAnsSdfbwVP9Zla3GsOLSQc1l66Z_nSsshZAPDPpLvBS_drKpyr-FEA7O32A8RFsB4c9px0FWtaBAQQkMCxRz3bksZKR5lJXWW8e32HMZrznkSm51TBPJopg3sk5_M2tLz8_KY9d6KbLd1_IWuTdbwNLeKtvN2FkE-IDZE30HiZQs-2uRa0CSiBKNrfm64cr1xU1jXOkDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=PYW2THU9r6VgDeWlqz2tx3wXFff1mrmDL7D8PC8CqEsyRShrzn92VyyW2r9C4AbmL-AU60WzQ4rNYHEgxxnqrD2xQiNksMTHAHXIDMzs-DF_wFRfdEOTfi5e7yvWJ0K26lrPck0iFTEVAnsSdfbwVP9Zla3GsOLSQc1l66Z_nSsshZAPDPpLvBS_drKpyr-FEA7O32A8RFsB4c9px0FWtaBAQQkMCxRz3bksZKR5lJXWW8e32HMZrznkSm51TBPJopg3sk5_M2tLz8_KY9d6KbLd1_IWuTdbwNLeKtvN2FkE-IDZE30HiZQs-2uRa0CSiBKNrfm64cr1xU1jXOkDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🤖
چینی‌ها یک هیولای هوش مصنوعی با ارتشی از عوامل عرضه کردند — Kimi Work می‌تواند تا صد دستیار را به طور همزمان روی یک دستگاه اجرا کند.
‏
‏
✨
قابلیت‌ها:
‏* تا ۳۰۰ عامل می‌توانند به طور موازی روی وظایف مختلف کار کنند
‏* مرورگر را تقریباً مانند یک انسان کنترل می‌کند
‏* دسترسی به داده‌های مالی را بدون پیچیدگی در تنظیم API فراهم می‌کند
‏* عادت‌ها، زمینه و اقدامات قبلی را به خاطر می‌سپارد
‏* با فایل‌ها و اسناد محلی کار می‌کند
‏* کد پایتون را اجرا می‌کند و فرآیندهای روتین را خودکار می‌کند
‏* کمک می‌کند برنامه‌ریزی کنید و وظایف بزرگ را تقسیم کنید
‏
🔗
https://www.kimi.com/products/kimi-work
#kimi
#ai
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6202" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">78.2 MB</div>
</div>
<a href="https://t.me/archivetell/6201" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">12.8.0 (6913)
Directly downloadable from
telegram.org/android
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6201" target="_blank">📅 11:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAPO9a9V5dMk3AF-YpWIh3IBFYzEsCevU-OKXMLL96uz6e8IA8TaDrOyGplbn-bzLcWrK0Siop7H3vWpjSi-egSLYsiZ2jw7LKrqVpAS7uZPQnmSrb0d0kSGsjWr9EwG4jpJaNBIpfOWogEnlTOaQbvoAuuuO65Ak-5JwuCJZQSbc8OEs17RDIvj9x8aU3u1O3lmXGEg-f5X-oYHEueSQzJmE5AGAvtmr3mD1Vvv7SduNa8Qxz63KkIyPpfMcINPrIUsgUzRUodHmup4ewWmVm_vfB8nWgzxdeQvMDC3NUo45ZpQFlp2u9A-5KJaTg3Whwm392mY8EIBCe6H71v1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
گوگل NotebookLM را با قابلیت‌های جدید هوش مصنوعی ارتقا داد.
حالا این ابزار از مدل جدید Gemini استفاده می‌کند و می‌تواند فراتر از یادداشت‌برداری عمل کند.
🚀
✨
قابلیت‌ها:
•
🤖
پردازش و تحلیل بهتر اطلاعات با Gemini
•
📊
ساخت نمودار و تحلیل داده‌ها
•
💻
اجرای کد مستقیماً داخل نوت‌بوک
•
📝
تولید اسناد و گزارش‌های مختلف
•
☁️
محیط پردازش ابری اختصاصی برای هر پروژه
🎯
ابزار NotebookLM کم‌کم از یک ابزار یادداشت‌برداری به یک دستیار تحقیق و تحلیل کامل تبدیل می‌شود.
🔗
لینک:
https://notebooklm.google.com
#Google
#Gemini
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6200" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee5737315.mp4?token=Hxr5PA7eS8gqpDmF6_1lI4MYhS4ySEBeN7okc0vIPTPlxGt9aU5Xn1u47irePKHgushgNKkqh0oST1o30GixPxiaKTIL6a9naP3EcI8Xo8UqN_LOfKF_EhoJSQflH-to69ZRaq3AQHndnBTAfKizLwwuGRHihWtkq-UBgzEXrltVDWyl1mf--5mTxkOnPeALGwj8Bym_cufB1S6WrN5LrnL0ZuoAIlNz1POuv6w9nJWfDu2GiipZr4bxWL4UT89VnimFFIcvedMNaZ0wctzBjT2AXHgxjsmfR1EttGo-uV5s21lD5nZc1IN29vED5974triZ4OXY2f8nyJYGXNp1yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee5737315.mp4?token=Hxr5PA7eS8gqpDmF6_1lI4MYhS4ySEBeN7okc0vIPTPlxGt9aU5Xn1u47irePKHgushgNKkqh0oST1o30GixPxiaKTIL6a9naP3EcI8Xo8UqN_LOfKF_EhoJSQflH-to69ZRaq3AQHndnBTAfKizLwwuGRHihWtkq-UBgzEXrltVDWyl1mf--5mTxkOnPeALGwj8Bym_cufB1S6WrN5LrnL0ZuoAIlNz1POuv6w9nJWfDu2GiipZr4bxWL4UT89VnimFFIcvedMNaZ0wctzBjT2AXHgxjsmfR1EttGo-uV5s21lD5nZc1IN29vED5974triZ4OXY2f8nyJYGXNp1yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔤
پیدا کردن فونت هر سایتی در چند ثانیه
ابزار
Font Stealer
یک ابزار رایگان برای طراحان است که فونت‌های استفاده‌شده در هر وب‌سایت را شناسایی می‌کند.
✨
قابلیت‌ها:
• نمایش فونت‌های به‌کاررفته در صفحه
• دانلود فونت‌ها در فرمت‌های مختلف
• پیشنهاد جایگزین‌های رایگان از Google Fonts برای فونت‌های پولی
🎨
ابزاری کاربردی برای طراحان UI/UX و توسعه‌دهندگان وب.
#Design
#Fonts
#WebDesign
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6198" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌐
اختلال VPNها در روسیه وارد مرحله جدیدی شده است.
گزارش‌ها حاکی از آن است که فیلترینگ در روسیه نیز دیگر فقط بر اساس IP نیست و اکنون الگوی ترافیک و TLS Fingerprint نیز بررسی می‌شود. همین موضوع باعث ناپایداری VPNها، MTProto و پروتکل‌هایی مانند WireGuard و VLESS شده است.
#VPN
#Telegram
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6197" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚀
پروکسی محلی برای تلگرام دسکتاپ
TG WS Proxy یک ابزار متن‌باز است که ترافیک Telegram Desktop را از طریق WebSocket عبور می‌دهد تا اتصال پایدارتر و سریع‌تری داشته باشید؛ بدون نیاز به سرور واسط اختصاصی.
✨
قابلیت‌ها:
• اجرای MTProto Proxy به‌صورت محلی روی سیستم
• انتقال ترافیک از طریق WebSocket و TLS
• پشتیبانی از Windows، Linux و macOS
• رابط گرافیکی ساده برای مدیریت تنظیمات
• متن‌باز و رایگان
📥
دانلود و مشاهده سورس:
https://github.com/Flowseal/tg-ws-proxy
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6196" target="_blank">📅 03:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قابلیت جستجو در وب در ربات هوش مصنوعی وگا اضافه شد.
🔍
همین حالا بیاید و اون رو در پیویتون و گروهاتون تجربه  کنید.
😉
@T_Vegabot</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6190" target="_blank">📅 01:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">موتور جستجوی ربات
Vega
چگونه کار می‌کند؟
🤔
بخش جستجو در وب در Vega از مدل gpt-oss-120b پشتیبانی می‌کند که API آن توسط Groq ارائه شده است.
🌐
همچنین در این سایت انواع مدل‌ها وجود دارند که سرویس‌های جستجوی وب مختلفی را ارائه می‌دهند.
🛠
سایت برای دریافت کلید و تست انواع مدل‌ها
✨
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6188" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=WBPwRkBJfpQ2Dw5Ez8sz_Sc1hAwssLZ5u4s0oEiqGVGGugaenAow9wMAZotmMWYDek0pnLQ3IJv1ejXEuEh7X727u4S0iOHz1ATeDqppX-aPvqzlhGxjaOw6K6t1riKop9zgbaSv2JYf7LFzkJuocuA9sjRtmX4smdwTJB520ytCSaB1kQqXWy_C5y87rC6hzD46LMQmMvjxztAOTSAOYqVG-zxZIpaknt1q2E4RAsrUDlXQPj3BviU2XjIsAy40fGnHQrowGnbU5g4cBqC8VSUb5HJQz1WYgk3MfwOBH7zbsQSwF5OGNKMNk_-u9gRBeJ0AVLBJupAZNS7CcaUtUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=WBPwRkBJfpQ2Dw5Ez8sz_Sc1hAwssLZ5u4s0oEiqGVGGugaenAow9wMAZotmMWYDek0pnLQ3IJv1ejXEuEh7X727u4S0iOHz1ATeDqppX-aPvqzlhGxjaOw6K6t1riKop9zgbaSv2JYf7LFzkJuocuA9sjRtmX4smdwTJB520ytCSaB1kQqXWy_C5y87rC6hzD46LMQmMvjxztAOTSAOYqVG-zxZIpaknt1q2E4RAsrUDlXQPj3BviU2XjIsAy40fGnHQrowGnbU5g4cBqC8VSUb5HJQz1WYgk3MfwOBH7zbsQSwF5OGNKMNk_-u9gRBeJ0AVLBJupAZNS7CcaUtUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍎
Siri AI: تحولی در WWDC 2026!
در آخرین حضور تیم کوک، سیری با قدرت گرفتن از Google Gemini به یک چت‌بات هوشمند با اپلیکیشن مستقل و دسترسی کامل به اکوسیستم اپل تبدیل شد.
🤖
این دستیار حالا با دسترسی عمیق به ایمیل‌ها، عکس‌ها و تقویم، می‌تواند کارهای پیچیده و چندمرحله‌ای را به‌صورت کاملاً بومی مدیریت کند.
✨
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6187" target="_blank">📅 21:50 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
