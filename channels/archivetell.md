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
<img src="https://cdn4.telesco.pe/file/r6u_8RasiwYfhoNpalzUBkas70Ylq0DdGiW-m6Kybp1gl_q4efC3TTu133h89EPz5qjhrMliufREqzOTetOGxBWeyd0wJmaJqE-xYlItFzPql5y_Q0U6zSMtjvWK8_MRgIW1_FGLX9Fmwubf109pKXq_F_Rww2pdmF-VOxye76zFcBnRdgy_jxQCV1iNU3-G1GDS-DJ1A7LqMmG1Hx48U8UKKYgZQHWYTQBW7NWtg6-x_rHN7f0TNzpd6B8JtbwnC8PbpXKWy5UX2j_kFMznjyvPSDIIfHU8OXiGvn5VaWASCcaKF0LjSjl8Ct4qsujz6-dlSQQyPA-RhJQZ7YkGWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.4K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 18:19:09</div>
<hr>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔐
دریافت SSL رایگان ۱۵ ساله برای پنل ثنایی با Cloudflare
اگر از پنل ثنایی استفاده می‌کنید، می‌توانید بدون نیاز به Let's Encrypt و تمدیدهای دوره‌ای، یک SSL معتبر ۱۵ ساله برای تمام ساب‌دامین‌های خود دریافت کنید.
⚡️
✨
مزایا:
•
پشتیبانی
از تمام ساب‌دامین‌ها (*.
domain.com
)
• اعتبار ۱۵ ساله
• بدون نیاز به SSH و دستورات لینوکس
• قابل استفاده مستقیم داخل تنظیمات TLS پنل
• سازگار با Cloudflare Full (Strict)
﻿
🛠
مراحل کلی:
1️⃣
در Cloudflare وارد بخش SSL/TLS → Origin Server شوید.
2️⃣
روی Create Certificate بزنید و اعتبار را روی 15 Years قرار دهید.
3️⃣
دو مورد Origin Certificate و Private Key را دریافت کنید.
4️⃣
در تنظیمات TLS اینباند ثنایی، محتوای Certificate و Key را مستقیماً Paste کنید.
5️⃣
در Cloudflare حالت SSL را روی Full (Strict) قرار دهید.
💡
نکته:
این گواهی فقط زمانی کار می‌کند که رکورد DNS شما در Cloudflare روی حالت Proxied (ابر نارنجی) باشد.
🔥
با این روش یک‌بار SSL را تنظیم می‌کنید و تمام ساب‌دامین‌های آینده نیز به‌صورت خودکار تحت پوشش قرار می‌گیرند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 735 · <a href="https://t.me/archivetell/6109" target="_blank">📅 17:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJ71nePDJG7c2LLi91HrNlU-mkbiI3nBjVkP52WF6P-MQPt7t_6WFfawp41w1SA8fmrvkYu3dKFYmKeOV-kcVmQ8n5uZkR3oTN3uMw3d8662Bz8ui1uL2lnEfyIxQQc8NcxMKUz8Dez-u_y35BCKUHKOrAxkDV6sdGKZAi9WQ_BrCdDnFNttyHBGfT8OP0PyeKSa3k7xkWo8w3Z0ugpyNyg_JyAlf96hYBwyJXPAzxnvzx7YO2p1qM_yZtfL0KMH7N2BxBcKHH69ICMRamldfQoM8qzY-9SI0ahkohu-aHo1Ug-qxWQf4AwRAs-AA90sNEggKdBHbiDCzwoE55-6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان برای پنل ثنایی و ....
قابل ثبت در cloudflare
بدون نیاز به احراز هویت و کارت و ...
فق یک ایمیل و یک حساب github لازمه
https://domain.digitalplat.org
https://www.gname.com/tld-eu-cc.html
@ArchiveTell</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/archivetell/6107" target="_blank">📅 17:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/archivetell/6106" target="_blank">📅 17:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/archivetell/6105" target="_blank">📅 16:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انقار میگن نقز شده این سری     .</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/archivetell/6103" target="_blank">📅 16:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انقار میگن نقز شده این سری
.</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/archivetell/6102" target="_blank">📅 16:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2541bf82.mp4?token=gaYZiPfeWsvxi0Yct1NPqwQ60IXAQeKGZVOp3XQ32KFEIpEZ0v5u4rO3CQYjoTfTr8o2iDm3quVkWdSV0TMCQBAEnFOZcipViloNNzjsk-_ias-eJu1LDQN-r86dsURHWLxsid7-0mdyUV_a7B8lNwN4KiAigArJPNPyNVSdVFDZbcbKOolSRyWjBgpbyCZnDRVrqz1yMbP5uQbkHNkrCTzils0h7pLP_6UkNKY1C9ymJjDSWyWubu9_TDCUSZZtbqKQLUMRCoOCfxVV1ebKyq3fUajxAj4OSMujIZQbZw9tTfHH9MvkVhioeo2ikhYRXN6hKnyUaVBaPzjrYefnbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2541bf82.mp4?token=gaYZiPfeWsvxi0Yct1NPqwQ60IXAQeKGZVOp3XQ32KFEIpEZ0v5u4rO3CQYjoTfTr8o2iDm3quVkWdSV0TMCQBAEnFOZcipViloNNzjsk-_ias-eJu1LDQN-r86dsURHWLxsid7-0mdyUV_a7B8lNwN4KiAigArJPNPyNVSdVFDZbcbKOolSRyWjBgpbyCZnDRVrqz1yMbP5uQbkHNkrCTzils0h7pLP_6UkNKY1C9ymJjDSWyWubu9_TDCUSZZtbqKQLUMRCoOCfxVV1ebKyq3fUajxAj4OSMujIZQbZw9tTfHH9MvkVhioeo2ikhYRXN6hKnyUaVBaPzjrYefnbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک جایگزین رایگان برای CapCut — توسعه‌دهندگان نرم‌افزاری منتشر کرده‌اند که تمام ویژگی‌های این ویرایشگر ویدئوی معروف را به‌طور کامل شبیه‌سازی می‌کند.
عملکرد: تقریباً از تمام ابزارهای CapCut، به‌جز برخی از ابزارهای هوش مصنوعی، تقلید می‌کند.
سرعت: بسیار سریع‌تر، روان‌تر و پایدارتر عمل می‌کند.
طراحی: رابط کاربری مینیمالیستی و شهودی.
دسترسی: در همه پلتفرم‌ها موجود است.
Clypra
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6101" target="_blank">📅 15:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یوتیوب و اینستا شماهم روی همراه اول و رایتل باز شده؟</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6100" target="_blank">📅 14:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">💼
🤖
AI Job Search
هوش مصنوعی که برایت دنبال کار می‌گردد!
اگر از فرستادن رزومه‌های تکراری و نوشتن کاورلترهای خسته‌کننده خسته شده‌اید، این ابزار می‌تواند بخش زیادی از کار را به Claude بسپارد.
⚡️
✨
قابلیت‌ها:
🔴
تحلیل آگهی‌های شغلی و بررسی میزان تطابق شما با موقعیت
🔴
شخصی‌سازی رزومه برای هر فرصت شغلی
🔴
تولید خودکار Cover Letter حرفه‌ای
🔴
بررسی و بهینه‌سازی مدارک قبل از ارسال
🔴
مدیریت ساده‌تر فرآیند اپلای برای ده‌ها موقعیت مختلف
﻿
🎯
مناسب برای برنامه‌نویس‌ها، فریلنسرها، دانشجوها و هر کسی که به دنبال فرصت شغلی جدید است.
🔗
GitHub
#AI
#Claude
#Career
#JobSearch
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6099" target="_blank">📅 14:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzHwhXaklUxzfDR8oshzSRKPpS3yAJu-9yfOGbnPQy1bNIYpWc2Vb0-aS7bGAi6VMNb7BB9Eo2gP1qdmCxKrCaP_snLAQPknVlwOery-6TiW-hDBXgZQBxvYUjh67MyVgzQG8k73mQPGwYqBPCl6C0AX-GCs081s-SCNW7tsl0zYZrnWgdIeWH4j4xi2jW8aG8N4fF0VdLvnC2-16BnEHMwtItiqC6E8XJa-Ri8qOCaHwFUdqLWf-PFPQ-kwyA3ZJEkPWfLEHLHRy4DzeMXvHoHpAqRIiBCMeg-J8nbo_BQsf7jRyUs58yj0f11M_SwfrUxDkQh-0mbiteMs1w3OxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
🔥
گیم GTA 6 بازار بازی‌ها را به‌هم ریخته!
با نزدیک شدن به انتشار GTA 6 در
۱۹ نوامبر ۲۰۲۶
، بسیاری از ناشران و استودیوها ترجیح داده‌اند بازی‌های بزرگ خود را در ماه‌های دیگر منتشر کنند تا با غول جدید راک‌استار رقابت نکنند.
📅
نتیجه؟
نوامبر امسال تقریباً خالی از عرضه‌های بزرگ شده و بیشتر شرکت‌ها بازی‌هایشان را به سپتامبر، اکتبر یا حتی سال ۲۰۲۷ منتقل کرده‌اند.
🏆
بازی GTA 6 فقط یک بازی نیست؛ بسیاری آن را بزرگ‌ترین لانچ تاریخ صنعت گیم می‌دانند و انتظار می‌رود توجه میلیون‌ها گیمر را به خود جلب کند.
💬
شما هم فکر می‌کنید GTA 6 رکوردهای GTA V را جابه‌جا می‌کند؟
#GTA6
#RockstarGames
#Gaming
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6097" target="_blank">📅 14:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نامحدود
🔥
vless://991898b1-426b-4108-9d11-188339714c53@168.100.8.115:443?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=168.100.8.115&mode=auto&path=%2Flokayb&pbk=ZqgdfgPqBr3zZuk4yw6Rtw5u1ar3pPBYooFil3IKzUw&security=reality&sid=4dc2accf4ae6&sni=www.samsung.com&type=xhttp#@ArchiveTell
https://168.100.8.115:2096/sub/4spf8icnqa5e6si8
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6096" target="_blank">📅 13:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">50gb-@lxhosein-@archivetell.npvt</div>
  <div class="tg-doc-extra">1.7 KB</div>
</div>
<a href="https://t.me/archivetell/6095" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حجم : ۵۰ گیگ
زمان : نامحدود
متصل رو همه اپراتور ها
✅
پسورد :
@lxhosein</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6095" target="_blank">📅 13:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🤖
مدل جدید Huihui بر پایه Gemma 4 منتشر شد
یک مدل 12 میلیارد پارامتری که برای اجرای محلی بهینه شده و روی سیستم‌های معمولی هم قابل اجراست.
⚡️
✨
ویژگی‌ها:
• مبتنی بر Gemma 4 12B
• اجرای محلی بدون نیاز به سرویس ابری
• نیازمند حدود 16 گیگابایت VRAM
• مناسب برای چت، تولید محتوا و کارهای روزمره
• قابل دانلود و استفاده رایگان
📥
دانلود از Hugging Face:
https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated
💡
اگر دنبال یک مدل سبک برای اجرای آفلاین روی کامپیوتر شخصی هستید، ارزش امتحان کردن را دارد.
#AI
#LLM
#Gemma
#OpenSource
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6094" target="_blank">📅 12:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvc7HPNWkfPmyL7a6ZBNdqkVFykbK5Tjszq-vmljkjfSSqUq_lYwgwTvNsE_b3TGKXQTnuVZrjKiWIERXkQWg0FYz0tGnw3_-6Ib8B9M8U9XJddkMzF4rzotsou5Y1UMvU_EaNK6X9edVSHNLjB2IemHTVT2xpX2eeeefmlczYY2CIxEvGOSSEVGjCdquq5IZEqyKwreyVqI7jeRi1gwvSy6kZSrmMeWtEVvqqd5OC6CcAdJB-ygIfXZsA3wikohcqDSB33iY2aHWil7RqSxBHTr6UOcgLEysG8_volFLr7UKWLSzekqTiB5MayCTIrmrqvmCgXiFzYFc7Cz384fFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
خلاصه کردن ویدئوها و صفحات وب در چند ثانیه
دیگه لازم نیست برای فهمیدن محتوای یک ویدئوی طولانی یا مقاله چند هزار کلمه‌ای وقت زیادی صرف کنید.
⏳
✨
افزونه
Summarize.sh
محتوای صفحات وب، ویدئوهای یوتیوب و حتی پادکست‌ها را به‌صورت خلاصه و قابل‌فهم نمایش می‌دهد.
🔹
خلاصه‌سازی ویدئوهای YouTube
🔹
استخراج نکات کلیدی مقالات
🔹
نمایش خلاصه در پنل کناری مرورگر
🔹
صرفه‌جویی در زمان مطالعه و تماشا
🔹
مناسب برای دانشجوها، پژوهشگران و تولیدکنندگان محتوا
🌐
لینک:
https://summarize.sh/
🚀
ابزاری کاربردی برای زمانی که فقط می‌خواهید اصل مطلب را بدانید.
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6093" target="_blank">📅 12:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKjh744UDdEMD3xBamJNwjy836w-UJVH7vZsf_qiHlIbZdLqwCot1uHrX69G1Tjh11eSW03UBSZe_hhIMP2jOTBnSeukNjcMAJ2s3Zp7AOjuSZjtHaXO75cJBm6JUTU5WsftWFCmUXyrs3BjrufU_iWRcj3MAqzNNA9sAh_ZrhHVWyTgKpg0GBPibqMeFR1En3kU-trJwNDzj8IMdtzCLnLogY7zHarHPa26hW-LdDhbH4aHGgtw3bpvWHm93wIZ_TkaAcD1L_wGOtiQPK4XGRegfYwXVRfecIofFAFnZJkHU53aOYNfjaOWnh-byfUdv6DdF6RZBTWFetNOvbD3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
مقالات پولی اکنون رایگان هستند - دیگر لازم نیست برای اشتراک در سایت‌های محدود شده هزینه‌ای بپردازید.
1️⃣
آدرس مقاله محدود شده را کپی کنید و
http://r.jina.ai
را به ابتدای آن اضافه کنید.
2️⃣
تجزیه‌کننده هوش مصنوعی
Reader
تمام متن پنهان را استخراج کرده و آن را به Markdown تبدیل می‌کند.
گیت هاب پروژه :
https://github.com/jina-ai/reader
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6092" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📚
BooksBunch Bot — کتابخانه‌ای بزرگ داخل تلگرام
اگر دنبال کتاب هستید، این ربات می‌تواند به یک کتابخانه دیجیتال همیشه‌همراه تبدیل شود.
👇
✨
امکانات:
🔎
جستجوی سریع کتاب‌ها
📂
دسته‌بندی بر اساس موضوع و ژانر
❤️
ذخیره کتاب‌های موردعلاقه
🔥
مشاهده کتاب‌های ترند و محبوب
🎲
پیشنهاد تصادفی کتاب برای کشف آثار جدید
📖
رابط کاربری ساده و شبیه اپلیکیشن، بدون نیاز به نصب برنامه اضافی.
🤖
ربات:
@BooksBunchbot
⚠️
قبل از دانلود یا اشتراک‌گذاری کتاب‌ها، قوانین کپی‌رایت و حقوق ناشران را در نظر داشته باشید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6091" target="_blank">📅 23:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
200GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6088" target="_blank">📅 22:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
آپدیت بزرگ UAC Spoofer Android منتشر شد!  نسخه 1.0.5 با امکانات جدید برای عبور بهتر از DPI و فیلترینگ:
✨
حالت‌های جدید:
⚡
Fast
⚖️
Balanced
🥷
Stealth
🛠
Custom
🔹
سیستم پیشرفته Fake SNI Probe
🔹
تنظیمات حرفه‌ای Fragmentation و TLS
🔹
ذخیره خودکار بهترین Strategy…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6087" target="_blank">📅 21:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت
🥳
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 81 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6086" target="_blank">📅 21:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100 گیگابایت
🥳
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 81 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6085" target="_blank">📅 21:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚀
آپدیت بزرگ UAC Spoofer Android منتشر شد!
نسخه 1.0.5 با امکانات جدید برای عبور بهتر از DPI و فیلترینگ:
✨
حالت‌های جدید:
⚡
Fast
⚖️
Balanced
🥷
Stealth
🛠
Custom
🔹
سیستم پیشرفته Fake SNI Probe
🔹
تنظیمات حرفه‌ای Fragmentation و TLS
🔹
ذخیره خودکار بهترین Strategy برای هر مسیر
🔹
امکان وارد کردن کانفیگ‌های شخصی (Manual Mode)
🔹
منوی فارسی
🇮🇷
و English
🇬🇧
🔹
افزودن Certificate داخلی
🔹
بیلد و انتشار خودکار توسط GitHub Actions
🔹
لاگ‌های پیشرفته برای عیب‌یابی
این پروژه از کانفیگ‌های VLESS و Trojan پشتیبانی می‌کند و با استفاده از Xray داخلی، VPN محلی و تکنیک‌های مختلف SNI Spoofing برای دور زدن محدودیت‌های شبکه طراحی شده است.
⭐
اگر پروژه براتون مفید بود، حتماً داخل گیت‌هاب بهش Star بدین.
🔗
GitHub:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6084" target="_blank">📅 21:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">😎
پروکسی‌های اختصاصی آرشیوتل
⚡️
پروکسی ۱
🚀
پروکسی ۲
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6083" target="_blank">📅 19:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P21LAa-Zlv9mCGqBlPd52MVYjJoRsDxBOJamEUTcBNSgThPe0ZCXUy5M2X1-Fvm9lZgb6Mwp8L-qc638_HkbQIX6LG_3ylCVZGFFUN1Zkd4WBOUYH6P9kW2FT571xpZEwpo9mzCd0hCRjYxrhqRydwQWeam9uWyTR0H1wgmSpMlhp2LAv5BHqOquOhiDQpu4cku2z8hJjTG67_UnK5H1P3ioespnRhydV2hOIXVpapdMYUjPGjaJUizlGDN5xLa565DzOMJdkzc-57WbY08p7DUGnRU4BfKvQbypJXZiN5w1fYWe1hCpy42_5-g7YeXxehNi8a-afguUd2GswbzSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📄
✨
آپدیت جدید UPDF منتشر شد!
اگر زیاد با فایل‌های PDF سروکار دارید، نسخه جدید UPDF چند قابلیت جذاب مبتنی بر هوش مصنوعی دریافت کرده که می‌تواند حسابی در زمانتان صرفه‌جویی کند.
🚀
🆕
امکانات جدید:
🤖
AI Copilot
تبدیل، فشرده‌سازی، محافظت و مدیریت PDF فقط با نوشتن یک دستور ساده.
🔍
جستجوی معنایی هوشمند
فقط دنبال کلمات نمی‌گردد؛ مفهوم موردنظر شما را در اسناد پیدا می‌کند.
📑
AI Bookmark Agent
ساخت خودکار بوکمارک و فهرست برای فایل‌های PDF طولانی و چندصدصفحه‌ای.
✍️
AI Editor Toolkit
بازنویسی، خلاصه‌سازی، گسترش متن و اصلاح محتوا مستقیماً داخل PDF.
🎨
AI Creative Studio
ساخت استیکر، مهر، واترمارک و پس‌زمینه‌های اختصاصی با هوش مصنوعی.
📋
AI Page Management
شناسایی خودکار صفحات خالی، چرخیده یا دارای مشکل تنها با یک کلیک
⚡️
برنامه UPDF کم‌کم در حال تبدیل شدن از یک PDF Reader ساده به یک دستیار کامل مبتنی بر هوش مصنوعی برای مدیریت اسناد است.
updf.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6082" target="_blank">📅 19:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc7ad03ba.mp4?token=UJqABYY-YN8lzGXlb_UnSDQT3CMGyzpTpVCpDS3Vw9HQmL48oI77-xLd5G6vmEJmAWvkY5X5CQ-5_ElB_S5S8MNQZ3WA_DLyPy315HdtIbEvNjCu-M6-x-gSmpvsB46NN6fQvxc9Ipz9IsTETXjDf1Mk8FHNH3IjhEc5tWif-7VvFP5-F9Pq8wzMRxS6oXzNKmgHvKSwn2MaVYYZRB--EPV1J66punI_W0uiBqDtoBnfeRzTnzAGoB61wn3jFI-5KsW8AwK0eJcoNyI-2biEPm5MXdidsbMRwx_VSYOsINgJGz1XB2oGvIR792rVATZ0bxzdsBsE5Ut4bzzxTuNMkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc7ad03ba.mp4?token=UJqABYY-YN8lzGXlb_UnSDQT3CMGyzpTpVCpDS3Vw9HQmL48oI77-xLd5G6vmEJmAWvkY5X5CQ-5_ElB_S5S8MNQZ3WA_DLyPy315HdtIbEvNjCu-M6-x-gSmpvsB46NN6fQvxc9Ipz9IsTETXjDf1Mk8FHNH3IjhEc5tWif-7VvFP5-F9Pq8wzMRxS6oXzNKmgHvKSwn2MaVYYZRB--EPV1J66punI_W0uiBqDtoBnfeRzTnzAGoB61wn3jFI-5KsW8AwK0eJcoNyI-2biEPm5MXdidsbMRwx_VSYOsINgJGz1XB2oGvIR792rVATZ0bxzdsBsE5Ut4bzzxTuNMkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎵
🤖
گوگل یک مدل رایگان برای ساخت موسیقی منتشر کرد!
Magenta RealTime 2 (MRT2)
ابزاری جدید از گوگل است که می‌تواند کامپیوتر شما را به یک ساز موسیقی هوشمند تبدیل کند.
🎹
⚡️
✨
قابلیت‌ها:
🎼
پشتیبانی از ده‌ها سبک و ژانر موسیقی
🎹
اجرای زنده با پیانوی مجازی
⌨️
کنترل و تولید موسیقی با دستورات متنی
🖱️
واکنش به حرکات و تعاملات کاربر
🎷
شبیه‌سازی انواع سازها و صداها
⚡
تولید موسیقی در لحظه (Real-Time)
🎯
مناسب برای آهنگسازان، تولیدکنندگان محتوا، بازی‌سازها و هرکسی که می‌خواهد بدون دانش تخصصی موسیقی ایده‌هایش را به صدا تبدیل کند.
🔗
امتحان کنید:
https://magenta.withgoogle.com/mrt2
🎶
آینده ساخت موسیقی هر روز بیشتر به هوش مصنوعی گره می‌خورد.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6078" target="_blank">📅 18:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaYDJ71qgMxijNOES-j8JGnh-nxEaw2ufK62Bgt6W5esb1P7fNP1cCpeQiGknUA98WfB1aTalflo8dDUpd9KR9hfGJ3f9YLTq-FSGXVKxc4mzYmMIOMCWP9nJgfnTHkG9lC3tiUSO4sEFkWOnyyjYJJmi7oBhBqpZCMElo7IrEdoCJbejunktNlbTSPyj54PhrUYYLP_sHFI68XA6isSdOLeuOyQQ17Q_sPrd1-USsUnxsp44IqTwaQZXYQ060aWSRVrsUOkE3NYykFK5ymuS5sJde2iSVgHZtQF8zbGVEcgPlKFUtokoqpATNW3YIB_ctMqcaij_afsnsDPlwFv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه اندازی پلتفرمی توسط OpenAI با نمونه‌های کاربردی ChatGPT
🔥
در این پلتفرم حرفه‌ای‌ها از حوزه‌های مختلف تجربیات خود در کار با ChatGPT را به اشتراک می‌گذارند. آنها توضیح می‌دهند که چگونه شبکه‌های عصبی کارهایشان را ساده‌تر کرده‌اند و دقیقاً در چه زمینه‌هایی کمک کرده‌اند
⚡️
🔗
https://chatgptpro.substack.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6077" target="_blank">📅 18:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">زمان : نامحدود
حجم : ۱۰۰ گیگ
متصل رو همه اپراتور ها
✅
اتمام حجم
❌
vless://d601f422-a626-4533-a3d9-8fddf16517b5@171.22.136.84:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#100gb</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6076" target="_blank">📅 16:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
80GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 80 / 80
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6075" target="_blank">📅 14:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✨
اطلاعات عمومی
[5/23/26 3:48 AM] ᴍᴍᴅ: ثنایی یا صنایی یا سنایی
[5/23/26 3:49 AM] XrayUI Group:
ث</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6074" target="_blank">📅 14:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpJWnVBRzJ3d0RkaWJMV2R1VkZ6YmVY@45.95.233.55:443#%40MohrazServer%20-%20%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6073" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانفیگ مخصوص کلاینت happ
زمان : 40 روز
حجم : ۱ ترابات
لینک دانلود
Google play :
https://play.google.com/store/apps/details?id=com.happproxy
Github :
https://github.com/Happ-proxy/happ-android/releases/tag/3.22.1
happ://crypt4/vfb1onL0njkmd47DHXNPUKKEEPQNrpfahCf5vmgczvqBX6IcP0JkObKmWDw+hAZ2VwZ21pi6REi4WyyLXGQxIbppw+LrTNA2hI/+0Mv4HBgFZV3AEzeh1kgwD0yr9nppZJsSGofePhJLN2CcRV095i4udLU52HxgvaCcMSlW+MxM5BQyQycn0iznnAt+/d3fjhtJbMsGGPwC3VAK25ERXDg4IQVlPdk1K7QOfMqddVfnbPKHx6cYrLbYlh0jQS1ya2pgxEDHAHnKBapy6ldkGRojSL5NkZ0hDNhagnbvlB6EG+7WXfXLGBG4HTDv18z8kKwMcd8SqxlQs7xoZnsmUaMDLdiy7WLZ1feY8Z0upkOTj72B1Iwj1TIShiG1ZNyvKn9pPLCrNhntsChX3ckLrAMCI8U3iIRjoTgfW3WftxxTLfTN45xFAYGkektT1C1z/v1Bs+E5FZujJdzi/rCA+RoFpO8p7CvIbbCizV+dYY5deDml/Y0aBtTcy5J/Haukal2Wsx3Rrhcb8V1+L9FM6PfN0aKuZyzZ6cEZ2BCJTSEG4CAv0PSOwqQHts5lpfRLDdE6M5em9jkYuS5sdwxU2PULK4QDUn2a4LmkW5NMWQq/QOYuNTaiPsN1QqLKsTi0eXaGC9sJNHRLFOXahzwCgnKKr+ios8lIK98MoQ0KoUU=
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6072" target="_blank">📅 13:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lx4L2soGncLi1dU2osOqM2Q-pvyN1F3gvT1t4d7YGFBUuQAgA6AY-0swP7jIM4tkvk2Y6I6z9rlHZLDVJjICoa5ngQXP259wIMuSlXJ1OVfIVZhYh0DhTgmW1Zb2gofEETJaM4fBox1muZjuY_f5XuAGvjPOnzFkCt_bRavtnfvaxkZlBxil-u2Me_WDLZcHptG8c1X4JdlSqmLDdaShp4FR2jSewe7CeGdM00Uj6d93TbNjRhGFNgBmBOSZLXskQteJNl9DXekcC2hW1CCzYEItOVOlEZcTI3QPyp4hHOzXzmwU9vNTdmJll8vtVjtpEhbAMAl4tJ6IDUaV0b2LVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوب پریمیوم و بدون تبلیغات
https://morphe.software/
قابلیت ها :
اوپن سورس
دانلود با کیفیت دلخواه خودتان
امکان تماشای ویدئو در پس‌زمینه و با صفحه خاموش
امکان تنظیم دقیق پلیر به دلخواه خودتان
گیت هاب پروژه :
https://github.com/MorpheApp
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6071" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6070" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔥
آپدیت جدید NipoVPN منتشر شد!
‌ابزار NipoVPN یک ابزار متن‌باز برای عبور از محدودیت‌های اینترنتی است که با مخفی‌سازی ترافیک واقعی داخل درخواست‌های عادی HTTP، سعی می‌کند اتصال پایدارتری فراهم کند.
⚡️
🆕
مهم‌ترین تغییر نسخه v1.1.54:
🔹
اضافه شدن پشتیبانی از پروتکل SOCKS5
🔹
امکان انتخاب بین HTTP و SOCKS5 از سمت کلاینت
🔹
بدون نیاز به تغییر تنظیمات سرور
💻
پشتیبانی از:
• Android
• Windows
• Linux
• Termux
📥
دانلود:
https://github.com/MortezaBashsiz/nipovpn/releases/tag/v1.1.54
🎁
همچنین توسعه‌دهنده
چند کانفیگ رایگان
برای تست و استفاده منتشر کرده که بعد از آپدیت برنامه می‌توانید از آن‌ها استفاده کنید.
⚠️
قبل از استفاده حتماً برنامه را به آخرین نسخه بروزرسانی کنید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6069" target="_blank">📅 11:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_2uZNCLEK_qlqa0NniHXxa3hwz-x-E2Qsg2I45f8lqsdGdzOJ4j7_gDTZDilYrxC3SS3hGYrMuynIJlEC5543iJtyfLPUHaAWkBl2NyWRpMhCBUtbAOjX5jdNldtNAZ8hNd4Bfou9tONVnSKnIpFrM0YIPfQvqBDfDIO7oc3JzPl2fxW5cyC5Da0q_O8rqquRVqxJeLVySYajwDj0Ii42fFVH6Xmx_5_BdfobaqcsDBxYHTA8bVvpa5MSr18l1M59QyAdd6D_fZfHX9wc_-q6b31ZpNn-h4S-FXrsfklnUb2NCWdTfwYDiRLYiz0NmkDfhSJ-PRvecLTDIWiGhm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف سانسور مدل های محلی هوش مصنوعی مانند Qwen , Gemma , Llama و ... با یک فرمان ساده
https://github.com/p-e-w/heretic
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6068" target="_blank">📅 11:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1602b4fbe6.mp4?token=Mq35_D2BlNRG7EdQxBKxIBphQIHQzzW0o2qQucTFXGHOyxParfd3WA-iL3oEMZt6F7IwUy1tLHdWj6Z2rKZhaIiI5sVqfDdhoLH9wex2vJxkPPXDJ391Gu-ysGkwWwO9yw1aYI5qHluLH1YMZMreLZiflkK7zDpA967gfxS0xoI_oF9JQnHDkBxhMI8_9OVIuXaV71Q-lSMmaHW5yVyKgA6FAfeTwXq3SN73MhUV7nD7DMFfeweM1r42VxJ8plI1FGeOWrU44K652DBtc9hS3CkAwthuxGhoUfpWaBQ54_8P0eNzkHx3pBXAPlNkHD7kN52R7fk-C9QPB3XmZj7Ndg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1602b4fbe6.mp4?token=Mq35_D2BlNRG7EdQxBKxIBphQIHQzzW0o2qQucTFXGHOyxParfd3WA-iL3oEMZt6F7IwUy1tLHdWj6Z2rKZhaIiI5sVqfDdhoLH9wex2vJxkPPXDJ391Gu-ysGkwWwO9yw1aYI5qHluLH1YMZMreLZiflkK7zDpA967gfxS0xoI_oF9JQnHDkBxhMI8_9OVIuXaV71Q-lSMmaHW5yVyKgA6FAfeTwXq3SN73MhUV7nD7DMFfeweM1r42VxJ8plI1FGeOWrU44K652DBtc9hS3CkAwthuxGhoUfpWaBQ54_8P0eNzkHx3pBXAPlNkHD7kN52R7fk-C9QPB3XmZj7Ndg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🤖
آیفونت را به کنترلر مدل‌های هوش مصنوعی تبدیل کن!
تیم LM Studio ابزار جدیدی منتشر کرده که به شما اجازه می‌دهد مدل‌های هوش مصنوعی اجراشده روی کامپیوتر را مستقیماً از طریق گوشی کنترل کنید.
⚡️
🛠
نحوه راه‌اندازی:
🖥
LM Studio را روی کامپیوتر اجرا کنید.
🔗
کامپیوتر و گوشی را با LM Link به هم متصل کنید.
📱
اپلیکیشن Locally را روی آیفون نصب کنید.
✅
با دنبال کردن مراحل داخل برنامه، آیفون را به LM Link اضافه کنید.
بعد از اتصال می‌توانید مدل‌های مختلف را مستقیماً از روی گوشی مدیریت و استفاده کنید:
🦙
Llama
💎
Gemma
🌊
DeepSeek
🔮
Qwen
🪨
Granite
🐬
Dolphin
🧠
Nous Hermes
و ده‌ها مدل دیگر برای برنامه‌نویسی، تولید محتوا، ترجمه، تحلیل و...
🔥
یعنی بدون نیاز به سرویس‌های ابری، مدل‌های محلی اجراشده روی کامپیوتر را از هرجای خانه با گوشی کنترل می‌کنید.
📖
اطلاعات بیشتر:
https://lmstudio.ai/blog/locally-lm-link
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6067" target="_blank">📅 09:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
سایت های تولید رایگان ویدئو
⚡️
Dreamina
— تبدیل درخواست‌های متنی به تصاویر و ویدئوها. هر روز چند تولید رایگان ارائه می‌دهد و برای پروژه‌های تجاری مناسب است.
🔥
Pika
— یکی از دوستانه‌ترین تولیدکننده‌ها برای مبتدیان. حداقل تنظیمات، شروع سریع و محدودیت روزانه تولید رایگان.
🧠
Runway
— یک ابزار جامع برای کار با محتوا. ویدئو، تصویر، صدا تولید و ویرایش می‌کند.
🦾
Wan
—  می‌توان آن را به صورت محلی اجرا کرد. ویدئوهای با کیفیت می‌سازد و نیاز به سخت‌افزار قوی ندارد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6066" target="_blank">📅 09:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: 184
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 94 / 184
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6065" target="_blank">📅 08:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCi1WBMPyxgWBiKxtXkpZ6lHh4n1MVg_PwmiHzjvJzaZvyZsNT4D3Szc0lrjfwQS71lxaqk2jYVRmaEq-1SQV8zZhgmaRsue11_-9XDNK3ImSP1lutkqjbmtLsR9H_-69NAivikOVtwuEHtP37vIYCv6IVemMh-11p87GUMhcVPVJU7ULOTuP2K3c2V3haIK929q_0beYCxsdkpfDjShIqXnBhzCZBSaqJU1jiz20toCOe_5WqcakDFCt3Qf_LMDMbqeo0LFEyG1wF55WAG8VKAtgjnxcsXURYcH7h4Nglv-Rq5J_m5TTlw7Vxz8RYXK0HlPN84ExYlyIW34WQ0tIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفر 91 روزه F Secure Vpn
🔑
ابتدا شما به یک ip سوئد
🇸🇪
نیاز دارید ( حالا هر vpn )
برای ایمیل هم میتونین از
@TempMail_org_bot
استفاده کنین
📩
وارد لینک زیر بشید و ثبت نام کنین
✌
link
حالا رو add subscription code بزنین و کد زیر رو وارد کنین :
BNAUH-EFCTO-EQOCZ-RXHES
و در آخر ایمیل رو تایید کنین و تمام
🤝
دانلود F secure vpn برای اندروید
🕹
دانلود F secure vpn برای ios
🌐
اگر اروری دریافت کردید حین ثبت کد مشکل از آی پی شماست دوباره امتحان کنین
❤️‍🔥
تا تموم نشده بزنین
🩵
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/6064" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
184
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 94 / 184
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6063" target="_blank">📅 03:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6061" target="_blank">📅 02:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پروکسی
🔥
https://t.me/proxy?server=channel.t.me.tradeip.store&port=8443&secret=dd7fe6d9803aafad7823ee9eecbf31886a
tg://proxy?server=channel.t.me.tradeip.store&port=443&secret=dd9c214385c44ee56c5f8d0a0f07475c3f
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6060" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی
وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان
GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen 3.6 • GLM 5.1
🎨
ساخت تصاویر حرفه‌ای و خلاقانه
از عکس‌های واقعی تا لوگو، بنر و طرح‌های هنری خیره‌کننده
🎙️
ویس چت هوشمند + تبدیل صدا به متن
صحبت کن، وگا می‌شنوه، می‌فهمه و پاسخ می‌ده
🔊
تبدیل متن به صدای طبیعی
ساخت پادکست و فایل صوتی با صدای مرد و زن
🌐
مترجم هوشمند چندزبانه
ترجمه دقیق متن و ویس به زبان‌های مختلف دنیا
📊
قیمت لحظه‌ای ارز دیجیتال، دلار و طلا
فقط کافیه بنویسی چی‌میخوای
مثال : «چک تتر»
👥
مناسب گروه‌های تلگرام
با قابلیت AI Agent برای تعامل هوشمند داخل گروه‌ها
🚀
همین حالا وگا رو امتحان کن:
🤖
@T_Vegabot
📢
VegaEnter
-
ArchiveTel</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6059" target="_blank">📅 00:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eO3DHnyn_hctWatQqmPGEkiKgpjh-YuyDj8m3qH9frccI9yqsNEnM9lV1-d0Stc8YGyQQKUk_CcPcOPZ3Qs-S-RcocJRDyqozIyueTDbpPnKQhRprc5PjrSN6g5hOeQYnUYZUT6bIIVphW_kXMpirHwV1-glqO8mguVyw-RF_o7uvDUA4NeXGocU5CMoYE6l0YoHckbZCXPKuf2yjcrDPW-tTFmymq2svSWbS3-Sd52N863VGAc1hCE9zRoV6PzpsLG90EiSoVYtLCY0dt7q-_bgi9TqBaVlXrsbhLKCqrbSe5u9fofvKvPRI9TqG9419JNm8LsUksunR9h0qjLigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➡️
Atomic Chat
دانلود و اجرا کنندهٔ هوش‌مصنوعی در موبایل‌ها، بدون اینترنت، کاملا آفلاین
🔹
Android
🔹
iOS
❄️
atomic.chat
💬
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6058" target="_blank">📅 23:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
معرفی اپلیکیشن AzadiTunnel برای کاربران iOS (آیفون و آیپد)
خبر خوب برای کاربران اپل! اپلیکیشن
AzadiTunnel
منتشر شد.
این برنامه تمامی قابلیت‌های کلاینت محبوب «شیر و خورشید» اندروید را به آیفون می‌آورد و دقیقاً از همان هسته قدرتمند سایفون (شیر و خورشید) استفاده می‌کند.
🔹
ویژگی‌ها و امکانات:
✨
اتصال امن و سریع تنها با یک کلیک
📊
نمایش لحظه‌ای وضعیت اتصال، سرعت و ترافیک مصرفی
🛠
دارای بخش عیب‌یابی (Diagnostics) و تنظیمات پیشرفته انتقال (Transport)
🛡
کاملاً متن‌باز (Open-Source)، امن و مبتنی بر حریم خصوصی رابط کاربری بسیار ساده و تمیز
⚙️
آموزش و نکات استفاده:
تنظیمات این اپلیکیشن مشابه نسخه اندروید است. در حال حاضر بهترین تنظیماتی که خوب جواب می‌دهد، استفاده از پروتکل
CDN Fronting
است.
همچنین اگر IP و SNI خاصی در کانال‌ها پیدا کردید، می‌توانید به صورت دستی وارد کنید.
اگر کادرها را خالی بگذارید
، خود برنامه شروع به اسکن می‌کند (ممکن است در اتصال اول کمی طول بکشد، پس صبور باشید!).
📌
پیش‌نیاز:
قابل نصب روی iOS 15 به بالا
📥
لینک دانلود مستقیم از اپ استور:
🔗
🔍
(همچنین می‌توانید کلمه
AzadiTunnel
را در اپ‌استور سرچ کنید)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6056" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
800
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 76 / 800
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6055" target="_blank">📅 21:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-v_k3cmzok19Oxs2S59iKkC49oM_SWncTARovI-FVpssa5ZneVJGfTy3vlXzteo4dBa6L_UILkvPB_SB0vb3ZPOR38siHNL0YQLDM5DWp3I1egMbe1VF4hZxgqcIsomfWdGPmSBIO9Xi-BoLhdiVVHdCa2Z_A1BOnRDrakQR4xb-q9btT-FHAZTFdRJ0Y-LooTkBNhdQXscbIFolgCC43hKb3XGSkZdcuVik1zF9Y95bCZ2v6IFu7s3s6Sdnat0Zb7Y8YQgFLv7v3rYSpccHT768zu42W_3bE9esrRjijYiLPXCmRpZDsolbhU24BpVKieiuxXv_wCiDNxcWCMkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرشیو تل؛ مرجع محتوای ناب و کاربردی
🔥
گلچینی از بهترین مطالب که نباید از دست بدهید
❤️‍🔥
به همراه پخش کانفیگ رایگان
🎁
عضویت در کانال:
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6054" target="_blank">📅 19:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdMP-v7jX5XK2NUUpW1CMpafEBbpH6s26_RPQGQwrqhAIPyMONTCxwH7RW6VzUXWbcrSvnKfL-uss87jcYr_y3PL9H-x9iSuFkjJSXjFKVp6LtPrcHK0m6XjDAPU35ShQVOYryPaZmlTI82IM94RzEvriTQA99jrfwElKLQMDvXs51f20Y78GaFkcbH02XGDgucFJpBjuTb6d-nG1Edmh6deTSzAp0d5n0_B1j7NEKOxhjvM_c3Rx-p1SavfgPX5OZG5x-Uti1vx92QRgrhGIMIVNPY4--ixBf_ejCZCWMROORlOiMMMjx2wGJBQ7-exblxVF6C7qaa8y4sf_QEm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید ویدئوی هوش مصنوعی از متن یا تصویر با کیفیت 1080p با Seedance 2.0
با ثبت نام 10 تا credit میده
https://seedance2aivideo.app/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6052" target="_blank">📅 17:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ربات قرعه کشی هم داره
هر کی رفرالش بیشتر باشه
شانس اینکه کانفیگ بگیره بالاتره. یعنی 10 تا رفرال یعنی 10 برابر شانس بیشتر نسبت به 1
امشب قرعه کشی میذاریم
یدونه کانفیگ اختصاصی خودش حجم بالا
ممنون از توجه شما
پرزیدنت بچلر</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6051" target="_blank">📅 16:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6050" target="_blank">📅 16:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6049">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sorrow of Sophia</div>
  <div class="tg-doc-extra">Draconian</div>
</div>
<a href="https://t.me/archivetell/6049" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6049" target="_blank">📅 15:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6x9X6C-BcAaOS8vS8gcHqmXMiAL1stT3T-IQPTZwOgCEyN6yP_1xtzhqGghxWb81_ULn8LmuvrN7z1pqL2vWdB_f9PsfpukwADcRweEC0mPy7xSrp-xbjTWeR6dAAqzkDXB9zInY5Lu8QYAj9vQQjd1MRxwK8D0VbGLeDhzpwQG_RtjQi88XxnVlqlOXVG2nml-a5n9RjnHv6rPWD74PcA4RT4qF-HNmNp_I4bA886jilM20SSfcFfAkQ7Te6AM8JmsZJGNMHPnp4YvBq7nq6VucD-EhdcQh5WcVwvRiY4WwPiGi2OimRrk3xHTnUsXEcgmRooe1xhjYqUkmjq6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📂
⚡️
FileShare v1.3 منتشر شد!  اگر برای انتقال فایل بین گوشی، لپ‌تاپ یا کامپیوتر دنبال یک راهکار ساده و بدون دردسر هستید، FileShare می‌تواند گزینه جالبی باشد.
🚀
🆕
قابلیت جدید نسخه 1.3:
📱
اضافه شدن QR Code به پنل برنامه و صفحه وب
🔗
اتصال سریع دستگاه‌ها بدون…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6048" target="_blank">📅 15:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw9EYBc657lUovC7brBut28TeKzYaS79mDAgWrhTg2DaUymlTvwQEGKucaQwvwYJbVTHgX6cV434p5htazpOZ8Audx6asZVqY10eiExCGprRdKouMzlmCjt0xLlaPGo0ZeTWVwnJm8AkraW2TSIgB11LwSA09_T7EJPsTgRVNFb2Q4jC28Lhi2aHX_GGlyNU4JXbC4CiNCvUKr2zKirrBPBWjG1ph7eyH0WohUuKj1wGV3s_l-CB8gH3jY1ZnyhZWXhwPR_j4agYbaKJ8dllM_KTdVxo_sN-8w70cBtKUfkYeF1HTNUwAnAEfd2rjY6Vh7wZULmIu_6YBN_-l5SRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">FileShare.exe</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6047" target="_blank">📅 15:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎬
دانلودر یوتیوب در تلگرام
دیگه نیازی به سایت‌های دانلود و تبلیغات آزاردهنده نیست!
😎
فقط لینک ویدیوی یوتیوب رو برای ربات بفرستید تا:
✨
ویدیو را مستقیم در تلگرام استریم کنید
🎵
فایل صوتی را با کیفیت اصلی دریافت کنید
📥
ویدیو را دانلود کنید
🗜
ویدیوهای حجیم را به‌صورت هوشمند فشرده کنید
❤️
بدون عضویت اجباری در چنلی
⚡️
سریع، ساده و کاملاً داخل تلگرام
🤖
Bot:
@youtubedownload12bot
👨‍💻
Dev:
@Bachedev
#Telegram
#YouTube
#Bot
#Downloader
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6044" target="_blank">📅 15:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
کمپین جدید
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 64 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6043" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
همراه اول Happ
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 192 / 600
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6042" target="_blank">📅 13:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXKFNtqHJJPa4J4-ZzpyCB2VVDUOSo_EIF63_s3lxszHwhBDatUayFo_Vny-CPfg-pOhpDe_zDDdmob6oreDNWn4036X6kqqoz1BroZM02q36taEHNBRmghJW8eDkukRSVwDHgySKmRlD6hi7cZ7WS9Ja9n44MdFZjBs4nt6qXIAGOs0c8tXsGcMuIlKhtDP8FA1II2jKYvCFA1LvnUfyuGSx9v8LKk0drdb_sri6gHL4oeLrECpnmZdRJ7uIY6xdx-MSvq6czzm4dMxAHPBJ_zdoRHlIsf0E1y47ZdqGslofU7afzTB6N36qy7U9WF3a32ukvmE3DP0Mydi0Nk43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ابزاری که مصرف توکن‌ها را بدون از دست دادن زمینه به طور قابل توجهی کاهش می‌دهد.
به جای اینکه فایل‌های عظیم، لاگ‌ها و تاریخچه چت‌ها را به مدل بدهیم، Headroom ابتدا آن‌ها را بهینه‌سازی می‌کند و سپس برای پردازش ارسال می‌کند.
این چه فایده‌ای دارد:
🕤
قبل از پردازش زمینه را فشرده می‌کند و مصرف توکن‌ها را ۶۰ تا ۹۵ درصد کاهش می‌دهد.
🕤
در صورت نیاز امکان بازیابی فوری داده‌های اصلی بدون از دست دادن جزئیات را فراهم می‌کند.
🕤
کمک می‌کند تا با پروژه‌های بزرگ و جلسات طولانی کار کنیم.
🕤
از Claude Code، Codex و Cursor پشتیبانی می‌کند.
https://github.com/chopratejas/headroom
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6041" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7b603d8f.mp4?token=TzutCBY4iKX0gaOWpcW210wHhmYr0QFj6JEELQgWupPoxHlKHSEzUaX0cox7cSUHsLm3P63ZaaRm_U9ZFm6XCLSDgP8A4SPt5Z1EPWbW_nrWP0E9s5a5ftfmEIeRa-TZ8EqWijaTy4_E2VlPdyoaL7cnV2gH2cisafU3h7U_RCC-AVwkNKNEKWWAJPJQW_k-KntGsVBZUD1viToTXaZxnvw9FZgQghTzs0f60NmdGQ-qDFkwRBTYrJM79CUApAacBqBAW0acP0k1LD_sa84H8Yz5_6jJjQ1CNX_luC5w7CJ7-qIY3L_mAM3AeBBmrdAQzNdpLHj4fxKgDJPMR59-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7b603d8f.mp4?token=TzutCBY4iKX0gaOWpcW210wHhmYr0QFj6JEELQgWupPoxHlKHSEzUaX0cox7cSUHsLm3P63ZaaRm_U9ZFm6XCLSDgP8A4SPt5Z1EPWbW_nrWP0E9s5a5ftfmEIeRa-TZ8EqWijaTy4_E2VlPdyoaL7cnV2gH2cisafU3h7U_RCC-AVwkNKNEKWWAJPJQW_k-KntGsVBZUD1viToTXaZxnvw9FZgQghTzs0f60NmdGQ-qDFkwRBTYrJM79CUApAacBqBAW0acP0k1LD_sa84H8Yz5_6jJjQ1CNX_luC5w7CJ7-qIY3L_mAM3AeBBmrdAQzNdpLHj4fxKgDJPMR59-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗂
ارسال فایل‌ها به هر کجا و به هر کسی — ابزاری که همه چیز را فوراً ارسال می‌کند.
می‌توانید سرویس‌های ابری را فراموش کنید:
🕤
پشتیبانی از هر نوع داده‌ای: اسناد، عکس، ویدئو، موسیقی، آرشیوها و پوشه‌های کامل.
🕤
نامحدود مطلق: هیچ محدودیتی در اندازه وجود ندارد، حتی ده‌ها ترابایت.
🕤
انتقال مستقیماً بین دستگاه‌ها انجام می‌شود، بدون سرورهای واسطه.
🕤
رمزگذاری در سمت فرستنده انجام می‌شود.
🕤
رایگان و بدون نیاز به ثبت‌نام اجباری.
https://github.com/tonyantony300/alt-sendme
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6040" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4fpY-e1CN7j2Q6jd1rLPYJX-t5SrgAHn2CcQpHUfA6Z_akTXUlU6mgg8NjfWEwhLNG2VOtRTWus0MePOrOKeekAUDcWD6ZWA44N_2vXREotz4NRoCaWrCfr_SrTo2pGq0I3ifZaHkqldVwuB8Mmzrkx_qUAfJ9wHLLdaw82V-mj_Q33TlQWdNJyd30KI3OTg_-vvqxDgNTBRcbijnkrCWe7efbpgYMN-6T3Wm6KtjR0-wkT44fqwVBpmKMa4YHvdGGR7GLRVrnz9ym0Ykc0XlELDjADt4DBDdLnG34JPnT1NBfayIg3pE13bvFW5PuoHgNELeGkL2awymqbXse76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان پس‌زمینه تصاویر با هوش مصنوعی
پشتیبانی از فرمت‌های مختلف، پردازش در مرورگر به صورت محلی، حفاظت ۱۰۰٪ از حریم خصوصی.
https://quickbgcut.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6039" target="_blank">📅 13:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6YdEDMKcm4KNdb5q1clOydS-ig4ST34CwWnZY-4n7uJzressPCOvEoWpAuZj4XXGniT1Xc3v2eaPq2F9tgJ2QiWLP160Vh54C3eUpZmEsW98NFP7u7gCVrUR1jX1sLvUFFfeqo5mXOSs-1H4wQxPo-7KFK6-UtCtGxpc1VlI5BmekME6PUNL0GYfPd4sb2kE9RrPrO_PEI48CBCegWTE1Hhx5SSZ8FCQWFt7Rb_P_FAGGdv8XiQFzL3RO-cJ3_XxT330qCMjAlhNr0tQjgB6ElJKMkion8RZFTxzaJTu2nSTPY7ApeNLkoGa7hxPcAk707Q16NtbeIC8TsTLjP0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
✨
حجم پروژه Node.js رو با یک دستور کم کن!
اگر از Docker، Vercel یا Heroku استفاده می‌کنید، ابزار
untracked
می‌تواند فایل‌های غیرضروری را به‌صورت خودکار از خروجی پروژه حذف کند و حجم نهایی Deploy را کاهش دهد.
🚀
⚡
قابلیت‌ها:
🧹
حذف README، LICENSE، CHANGELOG و مستندات اضافی
🗺
حذف Source Mapها و فایل‌های توسعه
🧪
حذف فایل‌های تست، نمونه‌ها و پوشه‌های غیرضروری
🐳
ساخت خودکار فایل
.dockerignore
▲ پشتیبانی از
.vercelignore
🚀
سازگار با Docker، Vercel، Heroku و Yarn
💻
استفاده:
npx untracked
برای ساخت خودکار
.dockerignore
:
npx untracked > .dockerignore
🎯
مناسب برای توسعه‌دهندگانی که می‌خواهند حجم Imageها، Bundleها و زمان Deploy را تا حد امکان کاهش دهند.
🔗
GitHub:
https://github.com/Kikobeats/untracked
#GitHub
#NodeJS
#Docker
#Vercel
#DevOps
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6038" target="_blank">📅 13:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
اهدایی
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 292 / 352
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6037" target="_blank">📅 03:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSb3F1Y2u3P5cqTOBU1kcyby7rB9vhpwXClOrAqXFJKpnZe5gLIWIDpFih3ZeSSZk7-DHj9Pp50UaksLCHNhpnezzu2wTKnpuOcLu6edaxqiQkDpRTrJO1nwifU8zyGnJ3J1pFAllYBzl6Esa4nBIr1I5ikZ-lDZdgib9w4Ho4UfjimMgNSQZskbkJXBvm_FFuCMNzsgEGMMO094bViy2MmzUQz7dvWLO6Pgzyti1yre0nQssFh_B2nGYynugS3bN4-mnXxtbylQMVq1FxW-M8p4oi03KC2SaSYMUrcQwpFz4lTx2ISa1iRMYvBJEr2N65_SNjENAiZFAJoLBWucow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6033" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6031" target="_blank">📅 01:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6030" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
UAC SNI Spoofer Android
ابزار متن‌باز اندرویدی برای اجرای کانفیگ‌های VLESS و Trojan همراه با Xray داخلی و قابلیت SNI Spoofing.
✨
امکانات:
•
🌐
اسکن خودکار SNI از لیست دامنه‌ها
•
⚡
انتخاب بهترین کانفیگ بر اساس پینگ و اتصال
•
🔒
پشتیبانی از VLESS و Trojan
•
📱
آپشن Split Tunneling برای انتخاب اپلیکیشن‌های عبوری از تونل
•
🌙
حالت تاریک و روشن
•
📊
نمایش لاگ زنده Xray، VPN و خطاها
•
🛡️
مدیریت VPN محلی با tun2socks
🧑‍💻
پروژه کاملاً متن‌باز بوده و با Java توسعه داده شده است.
🔗
GitHub:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android
#Android
#VPN
#Xray
#VLESS
#Trojan
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6029" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🤖
Private Link Bot | اشتراک‌گذاری فایل با لینک خصوصی در تلگرام
دنبال راهی هستی که فایل‌هات رو سریع با بقیه به اشتراک بذاری؟ این ربات بعد از ارسال فایل، یک لینک اختصاصی برای دانلود می‌سازه.
🔗
✨
امکانات:
•
📁
تبدیل فایل به لینک دانلود
•
⏰
تعیین زمان انقضای لینک
•
👥
محدود کردن تعداد دانلود
•
🔐
رمزگذاری روی لینک‌ها
•
⚙️
ذخیره تنظیمات پیش‌فرض
📌
مناسب برای اشتراک‌گذاری موقت فایل‌ها، اما توجه داشته باشید که فایل‌ها از طریق خود تلگرام و ربات مدیریت می‌شوند و لینک دانلود مستقیم خارجی (Direct Link) ارائه نمی‌شود.
🛠
دستورات:
•
/settings
— تنظیمات پیش‌فرض
•
/help
— راهنما
🤖
ربات:
@Private_URL_Robot
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6028" target="_blank">📅 00:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چنل های رسمی مهم:
🟡
چنل شیر و خورشید
🟢
چنل MahsaNG
🟣
چنل TheFeed
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6027" target="_blank">📅 00:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cy8ERUbIxfUD1zBJ1dm1UYk0qLzJrAoEArsl1gRVPutmcBDUwKBBm7fpVYKnrl0_zQ-43RjkV2fl_c0q_mpRk1HEzuQVCXmmnp-V7yUqlLTYYWT3guHPasFirejpiCaMKNGiZsowuHo2Qq3naTBPxlMv_LLEFXglhfwLaWNLNBkfaPhX4Qp7zE4vbW3Z80DYMf1gHKVZsd48B2uzpIh9tqNWOxD3HC-P904JrqwpHGMJ6GZ6a2wVIZk2269wb1k42fIbObcJkM7RNESGqIYk7Smpxo-pAQsK02K-URuvtbbRFj_9KX7d-bBADV02y98HsqUDTKwEK6Ansrxvl96oJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال کلاینت شیر و خورشید را دنبال کنید و به اشتراک بگذارید!
https://t.me/ShirokhorshidOfficial
دیروز متوجه شدم چندین کانال تلگرام که خیلی هم سابسکرایب شده بودند خودشون رو کانالی برای آپدیت های این برنامه معرفی کردند. دقت کنید که فایل نصب برنامه رو از کجا دریافت میکنید. فایل های دستکاری شده و ناامن در بعضی از این کانال‌های جعلی دیده شده. تا جایی که امکانش هست فایل نصب برنامه رو فقط یا از گیتهاب برنامه یا از همینجا (تنها کانال رسمی در تلگرام) دریافت کنید.</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6026" target="_blank">📅 22:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستانی که قصد دونیت کردن دارند، دایرکت پیام بذارن
کانفیگ ها ازین به بعد به این شکل توزیع میشه تا سهم کسی ضایع نشه و بهتر بشه مدیریت کرد
فرقی نداره اوتباند، کانفیگ یا هر مدلی
ظرفیت ها هم طبق کمک شما عزیزان و تیم خودمون اوکی میشه
❤️
افزایش پیدا میکنه قطعا
ممنون از توجه شما</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6024" target="_blank">📅 20:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6022" target="_blank">📅 19:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بعضی کانفیگا تو ویتوری ویندوز وصل میشه ولی رو اندروید با همون نت وصل نمیشه
راه حل
😁
از کلاینت exclave تو اندروید استفاده کنید
😎
لینک دانلود از گیت هاب ؛
https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.41
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6019" target="_blank">📅 19:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1QBNK_Vw_JV6u60dBp2qdPCg8crMRp4p8PlN0UsEL5pLiec_h__JQOlD0ooOMvpONjFKO6GRpFkjUyuMOg2QEISjoOpRgIVWDxEoNcdq08-2wALxT6VspyCHHoy1-mXmYG15gcW0dZKnpzV3E8e7U8y3-Vx1eZ6tZsMPv9G2dJCA-TB_0ZIjsoeE_o-h6bktOt-VHGiMENCpGcrf_V-LGqNOM5qC7wGQD1g5JCkIWLa_QO7i-AMY1NrcMu0rYKZir6MxMyT4VTiXVKL6PWIT74HC4PUAVPQKQeVVRLfmOxmMEEyQdaKOF1saAqV_oXT5Ko6qihMwp_70nlVYTHWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJqgq31eO_2Eocpp1p2NR9EOy9YGhPK6zpildYaJ_pZGZMw8XeCuTvrRQ1Z8A0jV65S6DPd18EyI1IK9HaJyPpXXYLy2Uy8HLnwZpw_hkcHoP4pkFFYhjjNxB5cPPhpujQVyhLtj0X9vSPjbso8vklALphqN3ArqLuKAMrmwTymyEDWstmXzb1QP-YsyD12hHTrVtR5nWvjn3EibCTRv59TvaPGENjAFTAeY6HmdrZCr0jZJabSZ1s4TVm5QQPdOGNFEnfTZcRWe7cD64QqqJseQtOqGDyti1YO0ET2h-uKBOEkyEHpvgQSM1TM9iLl0kG0CiGfDdG4tZvuRJOEy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4ciK3s2ZHtwCJyd6OZGxzwQs4714h3_4fSu11lqhqCgrh8m5CsjbROKzs1E1_40f96nByGs2IWEGrqHSTlpbG1WBufoelH99Je6Ot7zS6plGPWzqkL9g1A4lLZPdSwVY2tJqTBDRCw9LmPQ8_SNGVWtlaq4vzYYx2sPsh2BymKq-WKStGwP_amkg9Dak3RLL3fSuF7ExYgl9jj2tBuCtNprzyKnOYgX266cX9PxNQzMYMqOP3wfxdKUElvguPPRx-0X4DoK1_pvt99S6q7akcW3REz9I-7a9mMLAZDR8OlySdYhysMIiXG9qJwlzRmX2nWFlMYHPfvFPIcEYwEbDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Nano
🍌
²
Faithfully restore this image with high fidelity to modern photograph quality, in full color, upscale to 4K
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/6006" target="_blank">📅 12:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عملکرد بی نظیر جنریت عکس
Reve 2.0
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6005" target="_blank">📅 12:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6004" target="_blank">📅 12:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6003">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6003" target="_blank">📅 12:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
ابزار V2RayEz — ابزار متن‌باز عبور از فیلترینگ مبتنی بر DPI
ابزار V2RayEz یک پنل وب محلی و تک‌فایلی است که مجموعه‌ای از ابزارهای شبکه را در یک رابط کاربری مدرن ارائه می‌کند. کافی است فایل اجرایی را اجرا کنید تا داشبورد مدیریتی در مرورگر باز شود.
✨
امکانات کلیدی:
• پشتیبانی از Xray و Sing-box
• تونل SNI با قابلیت‌های ضد DPI
• دامین-فرانتینگ سمت کلاینت
• کتابخانه مدیریت کانفیگ‌های V2Ray
• اسکنرهای CDN، SNI و IP
• پشتیبانی از Psiphon و Cloudflare Worker
• رابط کاربری فارسی و انگلیسی
• بدون نصب‌کننده و بدون تله‌متری
🔧
فناوری‌ها:
• توسعه‌یافته با Go
• پنل وب داخلی
• قابل اجرا روی Windows، Linux و macOS
• متن‌باز تحت مجوز MIT
گیت هابش:
https://github.com/macan-dev/EasySNI
آموزشش تو یوتیوب:
https://www.youtube.com/watch?v=Y3tVfMqgys4&t=28s
#OpenSource
#GoLang
#V2Ray
#Xray
#SingBox
#Networking
#GitHub
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6002" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان
دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:
1. وارد سایت
cursor.com/students
شوید.
2. با ایمیل دانشگاهی (.edu) ثبت‌نام کنید.
3. فرایند تأیید دانشجویی را تکمیل کنید.
4. اشتراک Cursor Pro برای شما فعال می‌شود.
⚠️
داشتن ایمیل دانشگاهی (.edu) الزامی است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6000" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از ممبر عزیزمون.....
🇩🇪
vless://6d3c8903-86c1-46e7-a5dc-b45823dec9a7@fmmgkzjac48e.dxdx5.com:9023?security=&encryption=none&type=grpc#gum0fyg1
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5999" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان کانفیگ رو آف کردم   یکم استراحت کنید  بعداً دوباره فعال میکنم  به بزرگی خودتون ببخشید...  @Sina_1090</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5998" target="_blank">📅 10:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5997" target="_blank">📅 10:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-obito.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5996" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وایرگارد...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5996" target="_blank">📅 09:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">40 گیگ کانفیگ سرور ترکیه..
🇹🇷
vless://8df1328a-9ba8-4135-9b6e-b00f0b7455de@obito.96s.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.96s.ir&mode=auto&path=%2Fobito&pbk=qYkuXrr6eqa8zJz6r_AWFaJCFjMF6fe4_8yl7Vo9-AY&security=reality&sid=54bd5de0&sni=www.yahoo.com&spx=%2FUicYvHKFefj2yqr&type=xhttp&x_padding_bytes=100-1000#OBITO-.obito-40.00GB%F0%9F%93%8A
تست کنید رو همراه و ایرانسل وصله واسم...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5995" target="_blank">📅 09:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/5994" target="_blank">📅 09:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXZ6jfODF77gbw_nwStQZrs9VNMokPpTyHCDCNS5wcV82OrMD_D1cN4oquWQePZUiGegJwDOlceQk958h1Pe37EuWxoNGziB_MrC5FEvttoq0QAsMgN72ERbzj-V_1QiYRw_M07FCoydHfO6-uxmzLZI7uN2iEc_EpVb47S5nbxTIb603PGbugMexQkDU5fzPwAfSr7JTmBrnbtq33_e5ZIAA0-8H9bMSYtPefNtauQm7f4O4wS91E_K8JRRSoVpM-C1frr1KsObo3rtw-DranQERpESFufSW1Ocx2dm-FKC7eFTLVvuOliCTi0InpU0QxPo6f3625tv1Nc1z9ckOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cMLGuNQedhXyXhpeEost7WNGWx2dqsERHsBQLCoTYsQaK3jPolvk137hAEEGzXfcgYtR9nh9yDXz_Ims3LtKRCU8hTxPDgVXnTduCjn7iKEN7WdGp7RtV_nQ5EcPuyZr7cC_-0VC3mkLBAgU8SAnBrCZmEpac6E6uKP6q1a_mtI5TM5lDTPKjQrvF0o0Kf09IVqUV9kpITo3X_d8SH92oIwiZWUxhmVdHe2PS0KpRrCqd6rZ8ypvQD0v_1fKzI1XcooujvhaiWpK32pFCAXjuuCZIT6zn7Xe0f4iK_7kSVS-REiRMwWJriFCBCWFXnZpS1LJ-KESQksU62khgMcyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kz5RlXiCRq76BdYv1cGQ5bVdefgFW2k0kQOn59F_g8Q_YscCPGsI7cDxmKI-BLGwQ3PAD6AuKEBysF4_wqiyesdH9y-YfQ0AgS-ARjJENHEkWB3eoi442sXX0R-037--9ROp-vJx4ZSibY_uIGrW_Dn6HwktBv7DLk5yOT8EF5pYg9jGI-73paw2g4w5uxGdxi1GUkW6ReIR6cclXQUGC1zM3vGUHc2nK6stUycZkpyaVQ2ha1EDXc6Aw1r1tiUzRd4NqaoXiPzXgMT5EkdRzQrGO6oZDd2kTmM0sEXYSjF-Fxc7lRLwBc-BZBkxV1U234vXtAxmDZAd5VSDwphFCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Ideogram 4
منتشر شد
https://ideogram.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5991" target="_blank">📅 08:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک استارتاپ به تازگی ابزاری برای تصویرسازی با هوش مصنوعی ساخته است که در جهان رتبه دوم را کسب کرده است - بالاتر از گوگل و Midjourney.
👀
🎨
نام آن Reve 2.0 است و همین حالا منتشر شده.
آنچه این ابزار را واقعاً متفاوت می‌کند، نحوه عملکرد آن در پشت صحنه است. هر تصویر به صورت کد نمایش داده می‌شود - به این معنی که هر عنصر به طور کامل قابل ویرایش، قابل دسترسی و تحت کنترل شماست.
بهترین دقت متن روی تصویر در میان تمام ابزارهای هوش مصنوعی فعلی.
رایگان با محدودیت های روزانه
این ابزار در رتبه دوم جدول رده‌بندی Image Arena قرار گرفته و از Nano Banana 2 گوگل پیشی گرفته است -
🔗
https://reve.art
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/5989" target="_blank">📅 08:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پروکسی متصل .
https://t.me/proxy?server=87.120.186.57&port=1337&secret=77806a58288a20e94ae9424dc0a4eb60
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/5987" target="_blank">📅 08:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@archivetell.npvt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/archivetell/5986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پخشش با شما
❤️‍🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5986" target="_blank">📅 06:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=nert.96s.ir&mode=auto&path=%2Fobito&pbk=bPC70WXyPEUh8l4LSTdbACXer6Fhpw4tVwoMYLD_oxc&security=reality&sid=9d7b90df3283d95a&sni=www.yahoo.com&spx=%2Fy8WnnkZfDsyXZ8T&type=xhttp&x_padding_bytes=100-1000#Obito
همراه متصل
با نت های دیگه هم تست کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5985" target="_blank">📅 04:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از دوست عزیزمون....
vless://d2ae2b13-2532-4e95-90bf-8b94e856b51b@testhol.shompolexy.shop:443?type=tcp&encryption=none&path=%2F&host=www.speedtest.net&headerType=http&security=reality&pbk=7ucgFrVZ0LjQV554F0ogN9sKlt2yuqiTinH1ptSdkk0&fp=chrome&sni=www.samsung.com&sid=d7002a619306ab3d&spx=%2F#MOHRAZ-kxl1tmid
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5984" target="_blank">📅 03:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صبح واستون سرور ترکیه،
و وایرگارد می‌زارم عشق کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5983" target="_blank">📅 02:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">100 گیگ کانفیگ اهدایی ....
🇩🇪
vless://5bcaed47-9082-4e34-ada4-1d7d17066f70@obito.homan554.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.homan554.ir&mode=auto&path=%2Fmarg&pbk=Fdp4TeOj4ZdzucCR4dEoxNWtyS2gWnUg0q819GYENQU&security=reality&sid=798210477fa214fd&sni=www.yahoo.com&spx=%2Fa93dgM4XpaaJ2IB&type=xhttp&x_padding_bytes=100-1000#Obito-100.00GB%F0%9F%93%8A
https://obito.homan554.ir:2096/sub/8y88zn5phoxy4lhe
@Sina_1090</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5982" target="_blank">📅 02:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">@MohrazServerBot
دریافت 1 گیگ کانفیگ رایگان (از بخش تست)
ظرفیت‌محدود
🥳</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5981" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331520d70a.mp4?token=T8FoNJhorCm6QvvwtcR-ENGR7RAkDTpRdtQMWf8HiuOabTQuf74_cOy48c2o7gnMwLXFdqz8MiYH_RC8ZMgi3KgOUwncoJs6XVEAl4ze-HrBWxrEhm2OMTRMFKDdoUPwK1PTuJ0OmFgbTz4hIiXJUAl0dnaO74X0FeYnV1a6c3qC7E0yG-1oo1LwibVdyDwllovH5XzKTjSbGrXNNZ4MZwZAUZ-HvT8ewhofA22T726DyAo6rIrCYCRD-V4JJX6XH0ZWlqgWj3u2-QiNMRki3epP0L-_rYN-pUHQArAxgtgTNuy54aFPvMr82TdNY81IwC29FDZ_rI3-lJKOLsHX-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331520d70a.mp4?token=T8FoNJhorCm6QvvwtcR-ENGR7RAkDTpRdtQMWf8HiuOabTQuf74_cOy48c2o7gnMwLXFdqz8MiYH_RC8ZMgi3KgOUwncoJs6XVEAl4ze-HrBWxrEhm2OMTRMFKDdoUPwK1PTuJ0OmFgbTz4hIiXJUAl0dnaO74X0FeYnV1a6c3qC7E0yG-1oo1LwibVdyDwllovH5XzKTjSbGrXNNZ4MZwZAUZ-HvT8ewhofA22T726DyAo6rIrCYCRD-V4JJX6XH0ZWlqgWj3u2-QiNMRki3epP0L-_rYN-pUHQArAxgtgTNuy54aFPvMr82TdNY81IwC29FDZ_rI3-lJKOLsHX-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
اجرای مستقیم بازی‌های کلاسیک و نوستالژیک در مرورگر
اگر به بازی‌های قدیمی کنسول‌هایی مثل سگا، پلی‌استیشن ۱، گیم‌بوی و NES علاقه دارید، وب‌سایت
gam.onl
یک آرشیو کامل و کاربردی برای شماست.
مزیت اصلی این سرویس این است که برای اجرای بازی‌ها نیازی به دانلود فایل، نصب شبیه‌ساز (Emulator) یا درگیری با تنظیمات پیچیده ندارید؛ همه‌چیز مستقیماً روی مرورگر شما پردازش و اجرا می‌شود.
📌
ویژگی‌های این وب‌سایت:
*
بدون نیاز به نصب:
اجرای سریع بازی‌ها در خود مرورگر.
*
آرشیو جامع:
پشتیبانی از کنسول‌های نوستالژیک و پرطرفدار قدیمی.
*
سازگاری بالا:
قابل اجرا روی مرورگرهای موبایل، تبلت و دسکتاپ.
*
کاربری ساده:
فقط کافیست وارد سایت شوید، کنسول مورد نظر را انتخاب کرده و بازی را شروع کنید.
🌐
لینک سایت:
https://gam.onl
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/5980" target="_blank">📅 01:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay0vZm8s1QUraVIhkXagRlRc-Rpb6y4dgHKQkUiJRBpZBbDQp4iuzM26WfoUda0vV1aOKRZMyQHEH_UInNZwJ2v7RMimjMgHVWmeBXRukViw0dSXp6PlBC97GKkObGkqktOtJtQ2XMzAPfN7vHiGuAQHsl1WTKaBjaurAOzQqCU08q-kIiJZt7mbDG5gqkTzy89kAyTyo0o5bJHR5ONQP2rpoWtrS4zpsvF93gZdOBGtM_psX4f03H6kluAi3hnCs6gfc9C26p_uAF_yYP0bAaGNCZjuH0wHkXkDkEw7sZ0T746sn-pdo54fJ9yCjjPgk6_kDwu_sV7HnOmp3As-cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
در حالی که اکثر افراد به صورت دستی گیت‌هاب را زیر نظر دارند، Trendshift به طور خودکار پروژه‌هایی را که همین حالا در حال محبوب شدن هستند، شناسایی می‌کند.
1️⃣
رتبه‌بندی مخازن ترند در بازه‌های روزانه، هفتگی و ماهانه.
2️⃣
جریان انتشارها از توسعه‌دهندگان و سازندگان پروژه‌ها.
3️⃣
جستجوی هوشمند بر اساس حوزه‌های فناوری و دسته‌بندی‌ها.
4️⃣
فهرست‌های جداگانه بهترین عوامل هوش مصنوعی، دستیارهای کد و سایر راه‌حل‌های محبوب.
یک روش عالی برای دست داشتن بر نبض گیت‌هاب و از دست ندادن نسخه‌های واقعاً جالب.
https://trendshift.io/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5979" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">معرفی ابزار AutoWorker؛ راه‌اندازی خودکار پروکسی روی کلادفلر
سلام دوستان
🌹
همان‌طور که می‌دانید، پیکربندی پروکسی‌های مبتنی بر کلادفلر ورکر (مانند پروژه‌های خانواده Nova) معمولاً نیازمند طی کردن مراحل مختلفی به صورت دستی است؛ مراحلی مثل ساخت فضاهای KV، جایگذاری کدها، پیدا کردن Proxy IP سالم و تنظیم پنل.
ابزار
AutoWorker
توسعه داده شده تا تمام این فرآیندها را ساده و کاملاً خودکار (Automated) کند.
📌
قابلیت‌های اصلی AutoWorker:
*
بدون نیاز به پیش‌نیاز:
برای اجرای این ابزار نیازی به نصب Node.js، پایتون یا محیط‌های برنامه‌نویسی ندارید.
*
روند کاملاً خودکار:
از ساخت ورکر تا اعمال تنظیمات پنل و دریافت آی‌پی تمیز، بدون نیاز به دخالت کاربر انجام می‌شود.
*
حفظ امنیت اکانت:
این ابزار پسورد شما را دریافت نمی‌کند، بلکه از طریق پروتکل OAuth 2.0 یک توکن دسترسی موقت برای اعمال تغییرات می‌گیرد.
*
پشتیبانی از پلتفرم‌ها:
فایل اجرایی مستقل برای ویندوز، لینوکس و مک در دسترس است.
🛠
نحوه استفاده:
۱. فایل برنامه را متناسب با سیستم‌عامل خود از گیت‌هاب دانلود کنید.
۲.
نکته بسیار مهم:
پیش از اجرای برنامه،
فیلترشکن خود را کاملاً خاموش کنید.
روشن بودن فیلترشکن در روند اسکن و دریافت Proxy IP اختلال ایجاد می‌کند.
۳. برنامه را اجرا کنید. مرورگر شما باز می‌شود تا ورود به اکانت کلادفلر را تایید کنید.
۴. پس از تایید، به ترمینال (محیط برنامه) برگردید و منتظر بمانید تا مراحل تکمیل شود. در نهایت، اطلاعات ورود به پنل و
لینک سابسکریپشن (Sub)
برای استفاده در کلاینت (مثل v2rayNG) به شما نمایش داده می‌شود.
📥
لینک دانلود فایل‌های اجرایی از گیت‌هاب رسمی پروژه:
[لینک صفحه Releases در گیت‌هاب AutoWorker]
https://github.com/marketnoobtrader/autoworker
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5978" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5977">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9nOmYyripHPIlQCubE8cuhOkliNKWn1-P3pEmxujpg5yBaVshGIrQOVfABEKzmQ9N-2_DJlHxI2KwfUlaYOL7CVcvnYDd2-fjpQYOztbMoxU6n44mOQmXH5DlVTAUZ66t9XFzAZqmT5TkwBL4e-PG2qdXYnBVdWzzlvQ52h7val0cmhTHwrm0173y2BPnwASV3qhG6d2qtAxQDuwyZWK4ceZSk2YNv8rGNBod2aARRRdR8Ntz6oIJcUtcJg6YMHKm4siwql2_baJFsgjUh2mrdBmiwmZ9ZnPo7BJxj-hnT_a4y_z7SKDHde-FQP58xHLxvKLs02VD7sr0e6LZ9QNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
متن‌های هوش مصنوعی را کمتر کلیشه‌ای و طبیعی‌تر می‌کنیم — اپلیکیشن AI-Text-Humanizer نوشته‌های شبکه عصبی را به سبکی زنده‌تر و خواناتر تبدیل می‌کند.
🕤
افزودن انتقال‌ها و ارتباطات بین افکار، با حفظ معنا و ساختار.
🕤
جایگزینی کلمات ساده با کلمات تخصصی‌تر.
🕤
کمک به دور زدن شناسایی‌کننده‌ها و بررسی‌های هوش مصنوعی.
🕤
نصب با چند دستور ساده — بدون نیاز به برنامه‌ها و اشتراک‌های اضافی.
https://github.com/DadaNanjesha/AI-Text-Humanizer-App
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/5977" target="_blank">📅 21:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=ljpuzovGk1viKMYeWTjjeOd8bn_tvfvK0a8Ps6AEetrsOMSyfR1WcmmrTtGHICdCB4O2JwezFfD9NUec4YmtFy41pm0ppFzBs0sYfzGx-L8LKadZMuqkDhz4GdKg01rPwuHkfSS2xt7l4qtHKAxKvMzzgKAOfPjnk4O03tXZW2FTVfw_oeJ1JVG0oPW4es96dBRmZ_4XY0Q7wWp8X7pTMrYpQYMOUvFJGuVWzwWpWJN-MiTwDZClIlf_bJD_cpIWhenCRtLeft7mT_aINt199pRvIM3gzbmzDOzAtYARXrZX379KIPtqBkH2sKJRJTeVChbV1lVXC4Bwn5xqpYCSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=ljpuzovGk1viKMYeWTjjeOd8bn_tvfvK0a8Ps6AEetrsOMSyfR1WcmmrTtGHICdCB4O2JwezFfD9NUec4YmtFy41pm0ppFzBs0sYfzGx-L8LKadZMuqkDhz4GdKg01rPwuHkfSS2xt7l4qtHKAxKvMzzgKAOfPjnk4O03tXZW2FTVfw_oeJ1JVG0oPW4es96dBRmZ_4XY0Q7wWp8X7pTMrYpQYMOUvFJGuVWzwWpWJN-MiTwDZClIlf_bJD_cpIWhenCRtLeft7mT_aINt199pRvIM3gzbmzDOzAtYARXrZX379KIPtqBkH2sKJRJTeVChbV1lVXC4Bwn5xqpYCSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
Perplexity به ویندوز می‌آید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/5976" target="_blank">📅 21:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPooFfMF9wkfyqjyoBdfK5Dbk9yh7O-sRX17wOLFkQczY5MPLzQ3wLW1q5U8Mwk3QD6fDs-sk7IF1qhWARYED0KkoQeo_DjpN4TLZWhfscPApv4omHqIsABT9hUDbkYSV37jRBJGG_-IZCdE0Dkao3nAzj8AQuxs546zZ50uwCqThYoZfwl2auC8Qso8hXBisL31Av3rAM8Qa0rNhK30XB9tVZHUP_AExus3lldJwzVAmzN63oMogzzA2hzWPJpwD7FsuU3Gxn-km3qCVt3qzNGNZXvWI5FjcimasKAUQTXHA3g64l5KBpmUem4zYOfno-Ze4zq2vgG8hDKv0Z5yUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون می‌توان افراد را از طریق وای‌فای با دقت تقریباً ۱۰۰٪ شناسایی کرد.
محققان
سیستمی به نام BFID توسعه داده‌اند که افراد را بر اساس ویژگی‌های بدن و الگوهای حرکتی آنها با استفاده از سیگنال‌های معمولی وای‌فای تشخیص می‌دهد. نیازی به دوربین یا سخت‌افزار خاصی نیست.
قسمت ترسناک ماجرا چیست؟ این سیگنال‌ها را تقریباً هر دستگاه مدرنی در نزدیکی می‌تواند دریافت کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5975" target="_blank">📅 21:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">trojan://humanity@104.19.229.21:443?allowInsecure=1&alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#Cloudflare%20
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/5974" target="_blank">📅 21:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎬
🔥
ساخت ویدیو با هوش مصنوعی Seedance 2.0 رایگان شد!
مدل جدید Seedance 2.0 که توسط ByteDance توسعه داده شده، حالا از طریق Dreamina در دسترس قرار گرفته و امکانات جالبی برای تولید ویدیو ارائه می‌دهد.
🤖
✨
🚀
قابلیت‌ها:
🎥
تبدیل متن، عکس و ویدیو به کلیپ‌های 1080p
🖼
پشتیبانی همزمان از چندین تصویر، ویدیو و فایل صوتی
🎭
حفظ چهره و شخصیت در تمام صحنه‌ها
🎙
پشتیبانی از صدا، دوبله و لیپ‌سینک
🎬
انتقال استایل و افکت‌های سینمایی به ویدیوهای جدید
📱
مناسب برای ساخت محتوا، تبلیغات، انیمیشن و شبکه‌های اجتماعی
💡
فقط کافیست متن یا تصاویر مرجع را وارد کنید تا AI بقیه کار را انجام دهد.
🌐
لینک:
https://dreamina.capcut.com
@ArchiveTell
🍷
Bachelor</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5972" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=VGLONEFwSYd_14OQ6H9K5D9CwwMBf_8-se3eOFer7JjSCnhMM1Tgsj-3vy_3eiUp54NJ3VkY1IaOvQYdp4VqCwFjPNyN5ly2k5gRPDE5j0aYZ4LiRdLyeOJumaB2wkn5DCz8VJ0Ye8NT9dKvBO9Tw5CLyppqsGXPOTukjIKhGe4je4t_ybXZz42mC0-isvR87VSoDPXdv-Hh79cvh1ceXOJZ28wIijG2f_c0NTWIupMb1qw4TJaw5DB_VJhutivm8y8DKNnnnyoKTDAI8ZIOjCm3stfoCjJIVqeDmxlXKoWMyvqf0kW_OnxpP3fwk5nMjXfPAX21zABZkcOyEpcdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=VGLONEFwSYd_14OQ6H9K5D9CwwMBf_8-se3eOFer7JjSCnhMM1Tgsj-3vy_3eiUp54NJ3VkY1IaOvQYdp4VqCwFjPNyN5ly2k5gRPDE5j0aYZ4LiRdLyeOJumaB2wkn5DCz8VJ0Ye8NT9dKvBO9Tw5CLyppqsGXPOTukjIKhGe4je4t_ybXZz42mC0-isvR87VSoDPXdv-Hh79cvh1ceXOJZ28wIijG2f_c0NTWIupMb1qw4TJaw5DB_VJhutivm8y8DKNnnnyoKTDAI8ZIOjCm3stfoCjJIVqeDmxlXKoWMyvqf0kW_OnxpP3fwk5nMjXfPAX21zABZkcOyEpcdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔎
افزونه SwitchSearch — جابه‌جایی بین موتورهای جستجو با یک کلیک
اگر از محدود شدن به یک موتور جستجو خسته شده‌اید، SwitchSearch یک افزونه متن‌باز مرورگر است که امکان جستجوی سریع در چندین موتور مختلف را فراهم می‌کند.
✨
امکانات:
• پشتیبانی از Google، Brave، DuckDuckGo، Perplexity، ChatGPT، Wiby، Marginalia و Yandex
• امکان افزودن موتورهای جستجوی دلخواه
• جستجوی معکوس تصویر با Google و Yandex از طریق منوی راست‌کلیک
• باز کردن نتایج در تب جدید یا چند موتور به‌صورت هم‌زمان
• کاملاً متن‌باز و قابل شخصی‌سازی
🎯
مناسب برای:
• پژوهشگران و دانشجویان
• کاربران علاقه‌مند به حریم خصوصی
• افرادی که می‌خواهند از «حباب اطلاعاتی» موتورهای جستجو خارج شوند
• جستجو در منابع کمتر شناخته‌شده وب
https://github.com/thedmdim/switchsearch
#OpenSource
#SearchEngine
#BrowserExtension
#Privacy
#GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5969" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
