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
<img src="https://cdn1.telesco.pe/file/ZOnJauZn71VPrriNT3adYTCHiguEOvSE48Vw2ND3VkK4fsTnFbs-Xid4RhK4XUoB3ql6cUUeRYArbnguwVZS4n1cNwU0PuxMD2cErX-_GLFujWsuVvhXOistw3zaq6S3oPxS_A3Cjt2b2u78ZcgaUveD83WgCqDEc87gPFXFIeLqLBmKCZ1_WkFhnADEwbLTeyVa_KVSUd-D-9pf7G-H4vQLRvapZJJrX1BMaW-dNsPm5u7Qy2S8h-J0tjU540VvMTdd_T2_k-BPt3QYAKc_zA9ncLEnADO_ze-L66CpuvGjoWLeYj4wq6KOXKHr7XR0Js-fMaf62Rq4Fk3Hup_wVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 05:52:39</div>
<hr>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XWbHWcEMKqno0B1K15Es3YKOrA_UgAHAPfkAEKPsQHCQsCd5FogYv6S6XEwpME6pFFaOi0vkUowV1prECuO1q8uyO_h3S93rcUH-daH0iLMqeFyNjGq6e1hY9KtFXycwnQGMY9aSxphDM5eRppo-4AfMpMJsmSGMd5n0uqJOAVSy75U9m2Vci3tQ86TOY3Iy2Iz6ssPJ6KMgrPKMxhJ7i0ai9V16PpsX1kzA5NkFKAl-Eg4HL1N_AptuI5w7gITPetPiMBZXK8g8a-Cf6GY8PHrFP-Tq8_9p3y6o6f7Oedx2Z1LyIfhCGlJOVxKpkatFfZzQi-Km9qhKr4jdRu_ElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkN_vQ5dWI4qboxGtDWR0-X--ugjvr9beTNgBQgaw6deMjcXIgky33PcephF2KcOy-YQiQDbNoNHwpeGLdgUocEjKeM0wqoMC7Fxhxy7HJ9kSBtpYaljO8JmnQytR9VbLzP3AebzPnc09OxwV-Cj9PP75F9m8tN7V7-9FJnQCqJeb3BAi4u2YnkqGn1WNp8J0h0_OR-E-idncz5lG7c6drmqFOx-zygu8BwHHB0MQSSWo7gzOBmP26kKTARgtXQiqUGTMM-qb4z4mxzT8Vzj-PGXBf9jeZdLwGNYlc8mkiV_oShA6U_czeT6FJIt3Y6mQ2Hk31dt7qdSkagBU4oskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdMFPP90Lyor30K5zUbNbIKtxvck1g9gsB97mU-s1AC5_o3gUW3FMa8oOO9ElQ6C15EcIlMF_xTADyylrHS50I6YyUImh4cIexWiDwAgEvSJangDC2dqC0JGv4O5x_GS74V9q2sMRc2T6LTWPS9apQujYoHUCQa0bsc7sWoHoQh62tBGBiEcFbo940wZwsZjgm_lJzRgJFu-cDdUWs6H71Aftucq0KXGenX8dOy88-W2R2n3ubtIYRksy8aUHx-NGdkRskAxqswpOxSzmcNrnCtvc4OKQvLSGdSIVYRcDCJ5tbNOwiYoM_zwEO4zPKP43-4l06GZ0F7xxFQtbt4h8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFxZFsAJWnwqfckOsIMm1BIZ82R6p7hsYbc5fYe6UxMQ0BJy7cc4aNzb_iOYR1QcMGMYqYeiFVTmj9xubLfVNd9I9AmONotk5P0w3MHYK9D5e9XdzssRykB2Ua4q5Sfj0lhndZuEwmy19mwFXzrFxGhlmF4ZfYQlrp6oh-9mThMuGgI4_1SKSJX_yVdGtiLekyHb39ePV2QxU7HgCQft4vUeCPscmcgXpmgM9u3x6wjojThxAXl7FrQQPyHG-yRpEKligxTNi8cBZLos-qA3sjPdH4CwBQaIxEHSa0d37reYJ517jNrK83tAmVA0HTBrmOUL7uxgZ3gL8opyNQqdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mW9Iy1outj-CXH8iEVKknwXm4qJtQRWxLUw9PNRfr5lCiKHxFkr8ckq18bdMKLtnXeRhymhBaL4GwKwHetA24lcpz5bTk1jCDlArUgOP1BCDOKEYX5K3ak9HBPoHocGoje4I9h0a1_3ncBMaVtacK6pgv4HZrr2GuF4htEr4M8MluMt8ZY3Uo7QpgiSQAdn03mb9sdhMRh0ncDICTZ9Nc8q5PC4s8BiEQw0angVPPA9YXDLeUAj1wwL5-JaX8PZu9MPq7rwL-NJGkssm4AkJzSaXuU52-UX9SDTlDSywYAa1Phexyd-qmqCqqMxGrAoPbAlDoHUwCr1wj6vyOsQlQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lm0yBAIcsQu-5Jrp0le1chu_P7PN5kjoHSi4Q-ww8L-JwOhxHVzUmRDUDLJpJ0lkoSsghvQVLgeq1mhZ672YZoTdsE6b9_TWoZE49zmGXqAsCzzSyuuST1vDvm6RcYanUlSQOv96qNJV5l__W-6EyWf4UwEcu8FY3L17fzG2zR1hELSFNNg9YW8ImhaosGPRMpQKghcpHoTHy0Wm_KZPE89C4tfCcSsjGoQM_IEhKml_pOTeccMO7C9euzd2rRhu9zPHg2ZN784aQ_SKtMTcw4PKNXOcqo38if685xz4TK1bh4TO3R78TXGYI77OfYKOdYJ78qZvbwnnwjXg-e0Y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDOYdjWCu30zT9caC1CL8qpWiwOs6XHkrSvgLjtubhbiKDUktB09eXjTi28OwCZ8aN8iq3WQpnaBeMmTp7Pb17PiyJZyshxHA29ksGEGOpp2cgGD0DxwSfyu-Q_mGO12ecf5qJUGGqg2CoHayWG00PY4AfNw43X3A6CzYvISeSEqvrB1GHUf_CIq5tGebW0AUKmj6-yAWkjY4zr3aM5m7XkodrBQJYy3sslDpqXwn6nlbDfQzWlcGxLSkfx_antABTMs_xYDBdLpbUeXV2grVOKIOYiZM8d3Gw4QHk_HLWlUPv0vLFoynLZ9T1tO6s7oJ9PVYFX1Ft0KVl76PDJk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY9oONKpYdQYSHiYdHVSPhmUBWkySQDL-AD3Nxinr2KTzOBcpjKsD-9WYAHwc3l1VOhVqYY6H7oZ_-757_4pPM0iJRmwsomv5_Mx1eACddJH9zeJw03LD1isiWbd0cdkGLUdYVo7pnoEoKnjt-wyPBWUbKmaL1f7v_QPjE64hPdN8_JrVmaqaIjq5XfuLZouriwXiPuQNae0OC56YWbbzqJWL8FUbLfS7Mh2StkF2YQUVtMVxiAqTyrlPqKlafTN5q9hh6_SzVZBFfErV2EFZsTCHBLsiFsiccz9T8x0Y6RbJBZH8rzRw-up4lMnZHTXz8STBdauK-Rd1wtPd8mb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cs5NrFuFud8-nT6I0HP1iIauj5Zcq6HqF_dGZwsUIlcY76aT5b5jVk_rLq48Y1PDChdtjmFcjcfN0eOVKHxCNPB26-0II8s-N-_rwMswM_Ta6pA4IZ_wYhXopTAko5lAlKLblhW5qywB5wzg-sQ_xtBYHsxg356Nsujrqo5HKypazwNHKHjqBaMl7R5LQP-m6jsp2ekfCmJ2EvGv7mhpLxLFRM3Z_1Ad33VTKAOAfwMIFx66nshmiq4010azbHvV5DA35tN4nDOiiBh3GZVjI6BNuvJDnONNrGN_CrFV0kABqyDrrBq64o8zkGP4a2Xfp-5gyM-GNba5BCgFBV4Ueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=l2A2mxldPHLBCbYyLQxvnzvZxXTjClNxD_y9sMdL-mi2aeNieN_7IL7TzFXzjm4WrS2xChsF1buat4ndbW5pPUqS5p_Q1ppWfm1gmDLCUjJv_PdHEmt6jl1ymDSMfeh6kspMI6aywD1He7ljr-TWH3RQrfI5S_d-ZjV4cnEsNvBxPGu34AZ890MdkRD3TDJAe0HcdCJb2OdAUaqdPNImFK8se9Tece-hvuFtMzYrgupXNX7Jn7dnO4NaZrZPy3c-2mNhNvC8kiUXNjdThzWU6MidORl4I8LW2Ggooreo6gO-I67NaQR5wF7_-PBXOm-WlJVcsQsQdcseSSIO_THvcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=l2A2mxldPHLBCbYyLQxvnzvZxXTjClNxD_y9sMdL-mi2aeNieN_7IL7TzFXzjm4WrS2xChsF1buat4ndbW5pPUqS5p_Q1ppWfm1gmDLCUjJv_PdHEmt6jl1ymDSMfeh6kspMI6aywD1He7ljr-TWH3RQrfI5S_d-ZjV4cnEsNvBxPGu34AZ890MdkRD3TDJAe0HcdCJb2OdAUaqdPNImFK8se9Tece-hvuFtMzYrgupXNX7Jn7dnO4NaZrZPy3c-2mNhNvC8kiUXNjdThzWU6MidORl4I8LW2Ggooreo6gO-I67NaQR5wF7_-PBXOm-WlJVcsQsQdcseSSIO_THvcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LuExoQBtimR2ta5ncjUb_KYgTovRU6USt4R_7u8ytUAi7hni_68_UIlCSI-agtLuTQlRZhbA5P4pAu9hSC38f8LzXlzdXZKXiQkSomJpjoHBXNtnAvmQJhCGS4URIbFrFI0hbjPfhHqIMob7UPmXo3fd5S_AIElOBQwYLNQvds_7YShffZoN1DCdqO0ai7xZnX3s2bSOWpFgjibvEqUhYnoohvhly3HHkI0FYrGlMYvvBELZ4jEgokvZNReFhoqxA8M3xpwfRLxqxyH5Ayqppp6-CnvVSxsDLMaZw-b-uimx0LlWlySeOfFJl9UX8lfb1FeeRielpHFrSA8uanuP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FYZqnkqnD0L0-8zeZ4pJGJ0yyV9WcbohMTP3vLSKaLQbJki388EX0kmaGE8g7AeDgMkYY2pGgixGblrlkqQfrgF4Xcv24768wCoc3Yu0AWWArCiho_n2Rwo8bmKYLkbaYANvKt-YRgdjDAbeTuTS0q5U9ut93AYar_CBq4kBtDg1pNk4Fg_p3pAjKYN-IS04CzmL0sBpMnectQcFjjaA-LJhTmJ2msh8E_SWCuE8qIDBjsBSji8FFftrSOc9aC1knU-axO1SYQpsu-lXg4PR0yOyjRyt4JO2rSzCLvRiKTKoAkoup1WhRkeDLIeQIUVFYM5Y0zkhUtR4wz-CLNJv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSApaBz3jAusFhlr6o9Egyc0E9URjllR7ifUgn4SUFP7nukyD6t73W8xd-1KLkbegrwJe1rigbowEfdPDKYWSEhyVRVB5aRb2Qw55oWPWGiiPoh_ChU5v5u_F9cfg0oYycHEZ29Kfh_etFYhY4gzI66DHNX_zrwfImAxbxJfV8wSbTB6HXUTDKJXTWeSj4oQLgR6DbYBeEKodyX8bVvh759K0iZnZopbB9m1uH0UC4KaRT9L3KrYwDyWCmXQttnGf2GkqdaFNS0Riok3GfjozV-wuTFJb5qCJ79VkcAx7ArCl-gfBIPmXsHUFN5V7TFMMvSdRCEFkciWpwLCBzkIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=MsUz9vu80zze6OQ9zC8ZBqwe1ugJIN8YaSjbZ30WipwU2MjI1zfFupXmbjcgFGiPOLPcv0AQ6eNONmttOCAOwfAqpKpBgxTTyiLLJN7JKfIC5edpv5fna11UQbOtcIgvSqsoO2SX1Fv-XmcbYw_5H3ha7PbBheZi-lMfhf163-vAWpRaXzK70XE5HCVG4R0-HevI1toRtmqNQF1ecR4Qiu6BnqUaQq1XBAnw1o5L7BhkO5l37KMT8EXU2sBn_cVpJb3fcIudXOB_CxFr0_-C0DDkrWEtiRaPbHAkiNwXu-m_rh0V5aoZMcX8JEuMSL8IjrV1A3OpKxNL6fq0q4zhKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=MsUz9vu80zze6OQ9zC8ZBqwe1ugJIN8YaSjbZ30WipwU2MjI1zfFupXmbjcgFGiPOLPcv0AQ6eNONmttOCAOwfAqpKpBgxTTyiLLJN7JKfIC5edpv5fna11UQbOtcIgvSqsoO2SX1Fv-XmcbYw_5H3ha7PbBheZi-lMfhf163-vAWpRaXzK70XE5HCVG4R0-HevI1toRtmqNQF1ecR4Qiu6BnqUaQq1XBAnw1o5L7BhkO5l37KMT8EXU2sBn_cVpJb3fcIudXOB_CxFr0_-C0DDkrWEtiRaPbHAkiNwXu-m_rh0V5aoZMcX8JEuMSL8IjrV1A3OpKxNL6fq0q4zhKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixoP_SSbSVWNMfJ9UzXHw7jk-06cYRb5fFks2m9TO_6XCyIkO7EojRygl__kClHZekBtxUCOUanz_4WF3t98gSVNYr-U3TOwEIBdrAlOTWhmhPFvNhUuk6ksRYWGRvtztiuVdLM5KfmeGN59gPfktp7LSdjMx2OWjEeXEd8jLK91wB07OheADPmC1hOd4AmABqlVdz0nNtaRyV-500LA3A7hYxazQWnKchjpVgj24lTkz2sY6n76MR4aD7ZTsc0y2RIG2ZNf2p04znB936xX6io25P94Jw97NXz3nqb8ju2DAl8sOyE1X_4dPY5wmWFVtoZV35MAHeF2POSDSA37-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cXJax0bHZGqVK0AZVGeO78lbtizTNIXUD5WWPNMXLjkvPRiB3apu5qCORQ_s3jbwoTiMAbUVugloV_aOueZvV3Zhd57wkTzwnN0TOJwWwyUo9Vc3bliZNtsn3RzvYeOpoIKTNcxzNdBX-1OlsMSDECoaKVPSQP5ZKCNiRveREtI6Pk4wh0xw27FaJ2drzdNuGuNHUVg4UinXGpUzsPhnqRRistrwSp_dwNwlEVxIzL3vVLvGrX-39ASEcy-y5v_p6Um1kjxkaCTCln-UK-UBUpmv4JlONeOrkFzfv186-GIasEhrq3BMNHpLyiYWA52wuyAGT5WCmxpAPAgwTGV6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eIQM3zXd8NVLkseSP-6Q2Xs9obzMqkfbEFQ51aD294XAUsPDaHWawh31W_KUckm0auTw2fyLSA323rBo0AybwSHEI1Q7RfUa56GjshbisAjYq88fuSPY3qEN2wOl7_WXgZ8Rxi1CmjBc-Ose3sz3ILsXwT7yIWh6oicyPjepER0f6Pp8logXk2pu7H8Q7FmtZgV5iDa-5PyfdHvS0qHRSvfvNJdP3eq0jACpBeXZIWhjsply6EVW7O0AIeO-3pDcuNDm2up1QvVmdXXuqCZCdKCCUTWE-BxX3hBr415_863Vh5kKRPXRV0246vKFrd7-gQvqITvhsBA7aWou2X8w8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XwluVKI7UxIXDgOuI8oATa6-Ig56M6Ms0CLEkIS51lWTgIIHii6GLbPrpGM4KHhHQrhBaSIT_RRlCE_y0yy4qRJ_zin99SULp8mEZy5_aoSRg6ptbeEKmHg1Xt7IpNRZpaRLtBcCnP__bWiG60MKF13sI51heAsOfnOzu8W1I8hiCDmJJlwsjEtsrOw5hggf-027QIHkiTMFaFLOFtQ3nXj7KqYJbc00zO8CiiQW5OV0QRgY313MMm4MhPMw924iyd199qU3rVgDDOkiuMzHEWL2zNqhiPg6-Qh9nDWrwQ6sDLofmAFsEm1xLJRgGwAYXwXB9afL_qOLFn6cG33t3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfp7CKtj1PAVndvH1Ywy3WVl2dmne91EB8kK7sv--1DxLZ7cuibQgTbBngFzYaJTlUQJFsyrO0xbgu3EVuLVCjRr49ZgH56yf6AlMaZGSEQgwFW99Z1lzYzb-UFq-bz5BUd3ZkDQ97JO1vH1SrUrkJ-dY2S42uqBMDx16N254GJXmmEalJiWRY7iIt8EChQ4NT0QGVCz9DAFIdQrBK2-LtIKsGljp7m4sPSAH0pxODfD1ERziAWaYj0iLItj0JuTbAtjO7xcF61sjvL9WQ1fa66C_YRi37QOft0_KOs5Y9g7V1i0FBytI3fF9o46JT0CnwT3GIz-sW9sI_1Y6sbXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NGbry2v3nwcY7c2FYt_RpMz3PJc3yqPchaT-Oje_Y8e9fCxHUL2Cw11jvjbgakx1YidDY6jSxxTgPsaxEwVfshtsAbmajmwRKwQHSBas1Gw9ti4ex3g8GnJFRlmCc8QAi8guD_Y05SaLYX9FF6OV67WNlNoXTXs0v0ZVR2mZEbYPdhj8y2bkcQs_1tEZnaBGyDeNNWierXEYQH4FoIr0XKp_umg2Yt2GS2XQjGonxH5cJ_mj0Z68SJaKvcwZXeyCHdryaKYcyNItw3iflrLr164h9LNajnCu_CRxvYYnO52dTxiRBLnR8p7Jq07tXbuadDtbybElLJp6Kr56hxI_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=leY2MphAAesamWNxF2qoVjfx26kZRDmCvEQX2h5HotfKeealgXu_PGMsmFPR0azrruKnKzWQhvqC7SHPe-q9BX2Pp70qaN5DSAb_cfkw65ephfVbP_L2gOj-Qz1ba5lAVp8eFolw-_ZyBcbymBF08s1PZXHIfbw4jHWJa63Idvb4SuSvBFbwTxKjewdkbxV6jaxzSiJi929M8hZMOdWQIfMNMXLmtORz9F0EFfvQ_tA93QC_ZvLy-Ud7qPeW3CTkD6VsqkImvevlBdLZwcespSInKz4CF1k5mPsInMA1bkBy-6bi1DB_8T8iqRXkCRuCJKybJ0xpkcTOu4DiV-dUfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=leY2MphAAesamWNxF2qoVjfx26kZRDmCvEQX2h5HotfKeealgXu_PGMsmFPR0azrruKnKzWQhvqC7SHPe-q9BX2Pp70qaN5DSAb_cfkw65ephfVbP_L2gOj-Qz1ba5lAVp8eFolw-_ZyBcbymBF08s1PZXHIfbw4jHWJa63Idvb4SuSvBFbwTxKjewdkbxV6jaxzSiJi929M8hZMOdWQIfMNMXLmtORz9F0EFfvQ_tA93QC_ZvLy-Ud7qPeW3CTkD6VsqkImvevlBdLZwcespSInKz4CF1k5mPsInMA1bkBy-6bi1DB_8T8iqRXkCRuCJKybJ0xpkcTOu4DiV-dUfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o0CtdMJHi1tYZxPPXTh6oHz9z-sv-gWq0d0_uO5ovr0Bujl0HoN0HzKnE7NGVIlZcKwuuXuwSghwQ2h6r-hAu9IjQF0ybrjDdPF_96bTxYKcNC7Hh-zlewnh_mIdgswhimwrVcR6ZpAVqliJbDXQCxWH6ZDKMUomVmaL1R7oMqkCyDQ0xxXJbIrhpWZE40C10iommCJdrh_bj2PE-Iu4jv_R3qjAGiDrmAA_Pb5M9sPfb0cQJC2KUXieZ91U-FQP_a8hnPSxSFdone1O8GBhT9sc5MS348Z3imlyZi8-m2XsPU0nv1itGVnnZ-ShIm3lRnl7vzpFI39bySiHgPSvSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fwdpUhH9q9B8ELL5VPUz5IIXkQR94UCmoGeWqWTEA566Hg9f6FHpfSEKxtsa_U6D5E_Jr9obGqdx6rMxaFaHruwPQkLFe3eh7-Rkk9Bryjo-nYFJLMng5aKZfoukT_r8pcNVqwZHjy36RLRNHQIxf19CWUSiaOky5NJMVMEE9G8DtExZZtj0KThFI8FmpBbtDA1YiUc3QX8fcjizXAS_ZvSghCP5X6ktaZSg2rni195B8fK-rRe-vNSeZzNLkGFBJo9MAcp5OYp4jIf80W93l_-WIMpYcDdk3dcKrNdSeIU0NCM1K7kgNW4zcccmfCZFrMfWQpVqQ9F11Jp4lNc66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K2iauLR9xf-Lpvq80pIOUXfvk7utHprrSeVBHKfSq8ZqjOTOybg5lheGjP7tkXU5a5Gk5i2KzggcODU7h4oR2-YuItZ2pFg-YUl62DJho_CnHu4RvCjRg5z_yH6tHvNI7dUgVRShKUs6FkmCk_FrxX6qwyTBEQIc9llNThzZXaG2k-7OeG0ZNogL4zT1o-ptkVDgPG1SrY1z6CVozSSiiuKZuHxNFtDnnQJmG-QgJeuqOGIPqXVZvMylmroymdyGv2aIUfNn312dQzlryHvehWxetN7pJbSQNXC9ehYCXDirjvV-07XemntWRqwDsy-6FBTiYgMxxxL7EWMiPjPnxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jn6iDVhdYzIugdI1nrwKlO0-5MgPWVFcDGWnX6bK0ygacOfMi_hU6L71VliE_SdNh4jPrXVxHU7In8dB-WuNKrcxNy4cEMGwmflGATzFe3q3h16JITrAvr2fSRuSIDp2b7xTgDHJduWjNsjZH-Z69G616Kfrr28Ozqvlno3MrVI_-N6IZqyjrspUgSUEgvNllAO-j79fX9weeVyIb05_2S7Kz1IiI-B1SMEHjFtb2xGKfdTi1CcWXEf6gP_TRrt46uvxIihV8DdBSpv3newKPNRPgt6SR4waQlqw2_eGFu-OCfxb_Qon6MZQ-v7qlfvak1Val2-0EL9VS1w2jXpNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDCPQeNLlT4AOpV42mYS067Jt8isjhSNy1243ialntB88jmrPy82or_fTgFSBXgnKwz95cIJ3dFMPAZmC7QbLpekdA4OnINJf3r9GVr47G-Eba4l1nbWZ6ewehr6YfP50pakziUTgHiSPM0OfSA5J-dDwamNUKBfOaPuCBmOG-BL0F_7PlyywxmhCoDQirs1GWejrWTXgrQhpZIu2Td8-haJQrc4ChbHhx5ocQA7rFHWD86ZXDxxB5Y-mJHYLx23z4apVPY1Yq3pmlm2NP0Hk0K04bwPcSx_GFB6LQ2uWFIiQXsn5KQUk0BI68aPS4XfQovb0L8bUSDZnb3v8GWEgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PIOlKjYNOXYMiSDkgYB8a9Zk6yek9NvOaNxQ9AERcIHWlwCl9Hd3wbfD-TrgDqv-lzob-FVg2cPoaCFT47NjCrcq5OBUtdi8BFezhXweVhwo6D2bNIRgH0Q2vcFvSdNbk31ux13ZLoDvDFig21Y4uehVrPvBLpXcTOLrCxEkxodHRuH94PflewTVhLMsktzBPIK4fH7-0OTwmBjVrf-IspSWjWrYwAYTkHECz0RwEt7tFQwuVkO4zNYICmgXqi55_WKcpQ_BrV5CdcM56HzvyFhgPVV-zgemoslLPeHC4uhIHhQ6xtTEqkmH_3gw5x197GDBAFWI6fQ0xB32Jf18EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ml7U4PMJSyc3PTSUSL-qw9wTzihqvWWxZ8J0YgWCHqsxnv1T8kscOOQNGS6D5W9cHAO7ElNYUb-J4cEYlJeqzddAW1I5_r5-JspupgHWWWkxAxAY6UQDJXoPmy121VV-_MPEMPGo8oLXeako4wSxhDWiOxzvM75OQbCtIgNo9MTKFBMpm9WCGIUHQNUtA_EOs_QvG4HcqQbRjHHHtUsxS1rcY6eDVdF2zQAmhbz7TUZ2i6eDtncH4R4H3OdzbYaTMgH6BCZ30oI-XjrZ64eoBHLyPj0y3POl8JoNT6CHj0npzANoF_7Jy__p996O56bGx5NQtRXUA0Yyxb6VeQC45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVD75X4Yui0JDZYdFqrDnEzy2NN8wQOpI5tMe_AZ2YkGfLhWXsO5zLmyz-WomWvhbdt2D0DZ6cSKSCPZr9adZyqmNPUcLW1CRzAD9Esq-fmVLyXyHm99i2hX90uxlQeFmE7GGo1BXNRGchJuPNJCVoXQAnjsqtwDbK_fnht7RZ5zidL-bLP-OY9qeX7JBW7b2wCICjJMiKCU_Y1q6YT2uJEtQxUd21TEW3k8xagj9eeRYXzrM-y7pk480KIq0vmz8s10o3Y1TcjqX9YOiKSwInhJ_X894NR2usAYaXGP2yD3Dw_RNJ015Itn58iUYAzccc_NpNVpxbDodmihX8Hu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=h0Typ3e635kI8CyZukLXrqsn-hkM7DrrdKDVodvPh1Ts-BeQ3b8y67VzqDGiL2yN71SRk4xcBCgruWpQYEQJH-PeRSJYzpCKjYgYdFI3xH94XTkT4AqtMnByZgiMRF0kFKZT9mu20zfuYNLpo_3vOoIrlggckU-3Y7lWEPnYmXarGtJGNr_z7fyWj-vM4sHx4hYnlRuMkryvCLIwx4amaqr-aB-5lzybxSxIMqXqFPyZPgFW8IvxWE7fBdR8t5Vsn8yHRC_ly0zwr6vh2YjT8kcR5egsntmJZU4kTeNV6R1ZffC6Ha0kul_XEWgBOn2tlvhqBw4MU3QaCifEb_iLJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=h0Typ3e635kI8CyZukLXrqsn-hkM7DrrdKDVodvPh1Ts-BeQ3b8y67VzqDGiL2yN71SRk4xcBCgruWpQYEQJH-PeRSJYzpCKjYgYdFI3xH94XTkT4AqtMnByZgiMRF0kFKZT9mu20zfuYNLpo_3vOoIrlggckU-3Y7lWEPnYmXarGtJGNr_z7fyWj-vM4sHx4hYnlRuMkryvCLIwx4amaqr-aB-5lzybxSxIMqXqFPyZPgFW8IvxWE7fBdR8t5Vsn8yHRC_ly0zwr6vh2YjT8kcR5egsntmJZU4kTeNV6R1ZffC6Ha0kul_XEWgBOn2tlvhqBw4MU3QaCifEb_iLJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hRQXU1Lu1q0o1xdJ0ROEP2sdLIZYXDVO9ZSn6Sp2NqNPGR7rpCeN7XbRM4mLWuhvOz4vJzaZ9lKHEwbKW9AWILETIDyuOAesIGGb-PcX5BYAXH2pHlEf7mJkBbCqsBFzKbcHmBfJcYlMUfpcVqFDBOlcPD0mFAWqVaZp0xbhd03utNfJm7OVUCm_Yu1RsNPNYlDvbGLfg4dHqDadxlqC--vw1CwyRTN1nc2bsesCnzJHe3o_dhJiUVCz5HA7vQIjy2EqMzBN3jV5gwA1e0rBOflavhDqpSBnayKEObiPp7q3juA7Qho7LkwBP3eDSZXZPJowJNnyejpVpM-KftCu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rLU6H6VSTHhZVXtP4_jaZLnk3_dYzRWujxGzx68Zk6lt8-sNSLoqJsjT-yCvewOe7euGKoMa1xOUFZkR6fZbZTqugWBiMGrcd_7eRCqihPkBhruKTTohsfeO5mbLE-9yNEUzThyaVWmVBqD_Qu4pAQMrtBScauD7RBU_jm2hKaztxhxkD1qP-DhmPFF0UIFhdnp8DphDcv77SKJMeH66-xEzIHQh-9zNibrS3omvlLN6HZhXZT31qBUBJI4zObzMBGuTpEXRceoz0ojgacOKG6jJAWzIXk79QxMJIr_Ruf_wxXMRbLKB2BAFEGX9B8J4BnNOn0DcYXZw5srJW_kSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJ7hW5XzvTXGhXaN7FFA5PTMd8ABaq-IQQCsnwO7PRZB77EiIEr8yeGZYMYVcN8-lRsJEfVp0P8p-2FPqGFq_65kWMWXEHfKOurBCInQGPowXVPVHIOghi66X28JfFGKHxmS5yhX80TqR_m96XpeERs_sfndIgIlC2ENtBkYgojNTW9crHXO0zG4ikA1c8SwHVwAf0F32Mh4I1Nl33NUbvbB8RONX6AuSVCzLarWvAk6tSDnksoN-d4Wmmb8H66x61sbcZLjg2cHw_7GL_QouK7JpqZwqdSE1gYiUmmZ_JoI8jNsGd4AWqMlhuCGysDzggplJLNCcpvY7Roo55Hwmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AirdMyFQsUYxR39xlVi2TOYNADihXorZHDGoQaXpcGlQ10KqDNj9gOVgvImoCJADN47NzEy3k93XSx0AQDr5l5EYk9_mSkrutzK4Uikpfq8y1IfjB5E6_Vdq3J4pUGNsIgUdloD0hR8FH8EXdaZKLMSEgoSSkMT0OvVJ9OT7fH5b2EoSvzt6shIQg7OjxnTO9NN2gxTeV_MH6W5e7jA1hy1BOhpFZypaEUXwbD2IWejdaaEgonz6Bs_TP39SihwDEqsAII6rvb9AMac6Oil5xSwZ9qomaFMmZk2e3cbbY3-sBeNu_Aqr_AlmcFfGEX9n4-JCQulxcJRKU3i5PaqNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Etxd21wcxR94UGHA3bXs-Gz67VrGk0H7htVtYAgpEULMhByt6oWPEZBAAnX4vVf9ibkGFZvgiOVujtFYEOF1aGcA1gpvm7EwL558TzZtD3ihiphLOOZOHyucnPGBvkDO-HkILD7B009mVEe-lSqYWLMessWlZHjiMO2ftZKujAnY6eXW_6ZxB7XO1-MRZTsUrmzHPCB1YYXI89v3gBpcPBT5hiFCuduo3C8Q1HYhtFuUjKk1IcUkFYRiCkpGGzvzupoya3xhOwkRLBPD1oJ3A_8ufOxEvOsnxs8EsTZ1ZE95ibRzaQItmuGbe5yYp4Z3LX5xuwBUUlbPw2bPeb4cJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EzzfincCBnXEOtJx82cKHwnOkOotMXxSAaHH8LPSVy-n32a6-u0dCtIkneD4aUHVIjdz-HLqNjoYkMKRlTY6QyX_ik25fuT-I8ytnyPXlIqEriFIhbeYLtwjrrRWWUYJezs1ynPw8U5pYI9EO_Q6NaqTvMwh8dCN8E3nA9YCHqUhlBgrNZ-wsW1orqNdUPZRLFWZK9f4x9OhMHrt1zFkLW6xNX2hUjdPSIwngOz5iDO8hWP2raA9xRXE4WtEbQd3bbw6hYlVo5xnmuf88RdKWs8hfIPn4KiGlGWWSSVA68LBaq-2Rxxd6AKXmrmxj5uy_iWyOfrELVZa3hVod0QVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vHzTA6qBsGPzHsmG_-CnWfZtaR5-Ofbxo2g4pW8zUFrl6r-PJvELanF8OjndbvSRYp6DJ-HuePedLNs2SKrjCa6rz1o0vWg8ygdI7QHLqXlF4QtVfptUEwJEyP_GJoeI3BGeW1YWH6I5NrshRAjXiXbPq0v7vMEXYar-4n6SUpSiwbePIGZJoT6K-rbGrDH2dda9MxetNZHgbPVSt1IPAn82qaoBGfTsnJb2X7K0ITCLnFQE10V4928z7SVo10P1Kg9ulORjNn7_cbxXkpOS3jKEhoKklp6bRyUvzs7Qj0GqnuO1DDWXn3PMudIZFqXJBmEYO4St028zmkJF5D--Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BK_kX0Xjiseb6Er5dz0HKiP5TLqMrrkOp9NwsrQOrcafqJqn37F5h1W2X-eEwvAMAIaqBM9qR8f7GGpc0-rYKkbdSQsCSX1DXaRSGkCjp2mM2B0PbxKI4rmF8OjpN2agdwKHQ6qmFHPrfGTkRc3PvzAdd4fIAxgc_YIEoVqqh9og0ZAokWusplc8F4zTDxbviF59IwdFlm7SK0E8xwq17lNrMfm7Xhne5q24pjc93HDg9AKN1zKcCxr8xW2ks3Ch1azLMFLD9O9TtMlBnk7qfjI_Q2OpdFdwPpnfW870RoTHXkm6ATGfdOZLDbPwkhrEBA1JlSzNRpp-lG1hmuw2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XT6d9M7264xVQABX0KjvQDApseXyDrqX4bF09_uwbXg-mjPa5oQ56nN9yjfH_40IZy8cn90JC6tMQePhm9-J-iVnw60fYpeXr8VpC5yIc7IMrxLPW07d2dbV7-lI2s7wDYISDoQ6jEM95O7ZmrEPXyOgArj-evLjsJYoNAB5czvfFCCdJIz2nXTjv4NXEkrvMbIFs9b0-wlZS3_XjuYvnh0_Xjk0lPbypVpFQGqJzCzQTcF8T_2UgAgix11uDYZAYHYBS_dOGQMzM0dtTt-Mi1WYKc_PaabjzhEoM3WpmdJ0E5NWVYslftNwEYtyYuWHCKjbTLfi_FS1gCrHxVVDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OExyzQDkR42_s8YlPLsWO_Tw6_BDK2XprDD90QwwF_rPtGcJIGRE5eFm52FFFtlT4K7jiQB2Z76HGRw783YfOhEMjk31_8acF9IHUmqMKUP8xuRqRUdT-ZoeF2mhEBirU8GzSdHWSLJ1eC2IxonLHFRGD7kVWAnffJh0Xxe3ZfjwHKx161EfGxLcKfo0N6k-ul6G37nwgeOljlABZ8GBsBi2Yz-vTPJODfNmBkyGFNET79HQn3eVfq1MlH9Go-OkpZ7PYsVQZ67TAChl0taHIRzCby-ZSPen8JoOoGUutWnvMYsJYkQ86Z0s9JrxktdHdY6DSbw4d8EHRosBr6ID0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/snR6levG1mfE9-bXOrYEOYiCpKwudvhFIh_s-owNyZyCAw5AaZ1f5iwkq93bNC0s30pCdRmnmqVVETdQQr092Eh6LIgxqQ-5OcBXw_q8En6su6RlaRHQT3uUlX3CsDzj9pmCidDuL2WxyXbuz9NjI3vX8eirQmMYbt4w4cJvD5p1OOX4IANL-IYUea88NMorJprEnuS0yTOdXi_9ktPc3ZK2F2smk1CLA3tq9qSISkpVdKSKxtjxAn0NNKnZlfl_US4uOY14DEG5LpO1BuYWfpdPSptV61yN56k-eHZx_CjJ2YWOd734lyT4z8ZTjT7HaBBWzL1w-5cNUCQsaxcI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=oNTOVHAJN9s23C5N3gglalqhzqjmcDbsKLZmYONav0mZyGOarm9SDQUQlmi_2p52_O_Dj5SfY54Bf6Vw-aDaT7kzMgaQ_bdMemhRY5yF3JxWmoLpoMsApClTGwNSmNuEnREMY7bJLo6hnlucYTD4g91gZLFVAP0hVbavXufim3JGRfms1G7bpOuOSKUPvA1XGBIR1OSTqWUGo9XsvkT0v00LmaRIQ2xx5B1epEp6xxZh55e2svib-fFFsglkYGaCyulfo-uP2IXucRbf9WlfpapJ3Yl8YV47qxse5YZa1FD8hAoWYeX22jiOIpppOCIIOxQgKa0ee8Mh0eINowjFlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=oNTOVHAJN9s23C5N3gglalqhzqjmcDbsKLZmYONav0mZyGOarm9SDQUQlmi_2p52_O_Dj5SfY54Bf6Vw-aDaT7kzMgaQ_bdMemhRY5yF3JxWmoLpoMsApClTGwNSmNuEnREMY7bJLo6hnlucYTD4g91gZLFVAP0hVbavXufim3JGRfms1G7bpOuOSKUPvA1XGBIR1OSTqWUGo9XsvkT0v00LmaRIQ2xx5B1epEp6xxZh55e2svib-fFFsglkYGaCyulfo-uP2IXucRbf9WlfpapJ3Yl8YV47qxse5YZa1FD8hAoWYeX22jiOIpppOCIIOxQgKa0ee8Mh0eINowjFlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g6lDU3ZIhuT_gLRpn_Mi6kZ4H_v5Hv_o85j_ygpFDBogZDeGkwYuGw-QatY01rNHdfZJp-Cevv6NH_v6hOZdInfJgViFfEM4d9D3tsP98EIpTCQwgYzfYdKzN5t4kRbfFzJoCoEF2mvDXZOqDAzSzeudSH4PrMiMaRbXvlOoflZ4F1Pw88Py9G43G4oBZ-jeCRX-3Atlrhq1v3zYLxbrGKCKMnJ18g4RCo2IUiBCU3AIi-IBr0c_q8Qs4Moa6PF193mbgMQwdHit95nfzCt1efP7ug-4vwf3gOFPXcCyJ127qKFhrVbVAxbiLSp0FLusKmOGj6wVMgBQ6nFS_rc4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XeNSD_tLoVARixxTOQbeDYSbf-i91pDKgtp0LtkqbBuJXuJBrk5rVv_0ZWEi5HUVL4WEHiKp9NU32YkV9e3o-2MSAxp_7aaTxvHSPXPhJDeEi2iOm9hv2FH8zOCd45DIp2-aCN4ZwPK2eLYd0l7Y0hRg-D_r6OHNWlJ_j9zmWdvNWY64uPjzHotkU0qB0pJx94gTKqQOE9eXOp7auC37VdvUlJH9-HsyuTPBSaY4nFrS25-QoSFizt5gwPQ5HhGpVm5LPIkFz5w3Net5VSC-nFOyJ2zKDKUvm1RDJOX81jIIVxdgZFz8ZW4dOGh1A-lfVWhGf6lVBjTJyDU0gbCkRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sCkfyIwCwrZau98_KNzGCLLCxW_Ateu-flIIby3kE9Q-bpKwqhxn8m5zUMenRAQDY7RzWJPXdcgWZt_BvFUC1j6zI51he95PUgIl9tShG0CndYhgaN9enKPLbAaLHJPpBGtTD8nyUw7ncMo-F0SBhT-MHpPI0_rhG5EFIOgnlPbcPzg6cS-KdmRMY8ediAglK1B4-Q6BlO9aISdZFHBW6S1dA8v0Yz00l9QTDh7zu1b7Xk65xqTkebNxhZ2kr4ZBDQyjeXkugBjSMxmYXujJzv7Jqsu09EZeCM_gs7hAs290cVnqFxvrtzi_dMrolWQAbbzfOj1kci63uftULL78eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uqwkO3ILmqKOCXAeHeBP6hpJrW8n5gUutX23t5sIawnBy50iWrQIQoRbjsT_Y7H0eP1oEfrtv4sUd0_jUNbZl935zv5z8zcxVOwIHn6hYp-xob1ilONwX5oUAsKM55BVfNpn5ZZclhiaLZTLWaG4ZVcgj4iHZ41yiCqwL1b6chT9oicdDKZRCBmjzMBkLJGMM7etB17H08-syLeWavhmOvxLsFEO02gNQqNmq7DLiqPUas4_OYwV3ZeNnqIbcDTzdDbKKRoKSGthptnsIT2YTxfJvmBOA7cYY6PDDGUZ_Y05Ubx-kHH4QdgEoZl3ZfuVJK1eqqsY7RPFeO7Kn-__8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HXRQjKYgsXqFNae39GTJ3mvmdHqdp_P66nWe0IwpfBrv2lzIrE8yhpRNwO-ZChNH5EkYdbJ4txsz8JtV62kkRmzYbMyJHSztEB0IJ3epi2AcFORvpmHIxz8U44MSBwo2lEXIsua2mhNQFglAIhmob4t3OLpOVenye8c01HIGHykxM8okm6BhZaupEwDhuowVlXyeBAOBP4lFpvWGTsCqdBPUvCzQxbX_eD_WAkaiqtQcWPgrnoeE01qPuGae01hNjzD16s-U--aV4LgO1Onn3AHV3yi_TkKXYkXZVGoB5UaB5I-eVaY6-O2h7gb_ksQxLZJvP7fJVkWERwUI7W7nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I3Q1m1VcpcCnLfGdN3Q-Og7G-3iLvbQSs60wVxGFiPE9SQrCjui08qmIUp-kMPlp9dFOJQ403GB5eKffy4pb8-KnXXr7pWYmNTFoX3jLJFVYPXubYmDoY7rGoraT5r_Y43TTJgipHViPvgsk982n4ElfJvHzYCx_WBfwnRrhkfDqq4L3vsns8aynBzDd-Ot1XWUrOJcNVY7LZ9ZYw8GCDNuuVPgwcG3K3wL7VhWeBPj3kuy6ndURb1WRXQ3dDrRLJyCdsS_bB4Bl0mCQue-RPNtkBjlv6FrFTjYNPsiqY6j2tGTEoybJJ6OJvs-TBdxFCUoEzR60VixJ56dr1zfy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iSbgkXgKdzKdg9EEukkVeZyL7AhtjQnFt1crJcdvrCeMI0Bl-fluweXxiguSGpKTFcsn-YyBbeJK5L9vxEbIt5bDo3Rv92Qo9yhzMUYWAGGCJUBn64rXXpmhw-S8luKAAjojFPiI8D34S0DKoudz0j2M9q9Jky2I63iUVT-L08MqX74sh6LafjsaYMRbKvOtIdwXVmljvN9vCQeQgNizyF5l25Rk3egTRXhn6HYqzFQ3t2pCkU6wC75O7xIiQ3mxxSxaWQmlQPrFDmJf9lsUmwdbpVETllvjAPlNzkIRyUKAVaVSeU5rXNuO0XYC2ev3wAPf0Z9pgrKNWs4irQTlLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nT8PX9tqhQqKE6GCuz_Jv__GTbQ-JTAlhoEo20dqp9JPN79FR_gZr8gMId3E-n-gkPo9i5ksOa95QTJHEqTdYzpIuW_TwRIsJkbHGwBj3I9zsPjjLTesdL7NYQRoqLkand9EifwwiRFSdXpJY4rpoM84Xb3fk5kzjTM1RanqV96ZcQ-wVJoU8MOLcuPb8w4TtCp3iz0uAshwaBFhQcbTBIEme8Vqa83VfpDA5kpV9APDRiCFwvIF1sky6CuFv5OBiHlxObL1SFLNUrdDBOBO__lKIJsNA7yzP6VBAlDiSv-hNNA1KyseWxSzSK0aVo9QGWvFtrmzxyU4qUXF5P5UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hI-6YUuUXEuwVBi5ht35bsy6OxC_C24oUKSlc0foJfEZ_7RepLvscDtlQYYqaCpRV7PHsYacsq-uHEr-EoaaZoCxvy16NPC1jz1RBC54X9Yi1UhvgwAbdp9o0IqpIFTaIkvzbxYuCOSlFCk2VMybcFatqz_ddppMeIC3QkEQBg2Oa7rpySjZGZRqbYo5Ta-qkvdmNxaFwu7YuF2RBzn-gFjCeS_R6TZRIx60ojJdpHU10G9nQz0GD36E-3P9V8n13xJbi393Z38g2qbTuuKPhQtajXZ4fN5Ky-wkgraKJtnBM8K9pgsqP1XbDlvVxSP5PurRslUHLnK2shgg_2unAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fenv4avsEH49VfzzbkWsPNGBE6uhFPKZeg7wpF8_BGpkmkgZqW-lNPmDtV8yGySj6LOV4lCXwrP_EOOqmynR5Vx0C45Rs_RKsgxKcjyQmIRBvY_mQic7PDVgQqH5MmHwXfYyGevGX8BNz1UV_Zf6KRm56IGVUcWlruKR_Fc1SUEH1mUQXAcOKJT0kLaUa23AgtqF88oDuJw3Ck1njDWhedsXLYzNN0Zl_KkXtnPYVHoP2yXqoQNlq0ciU6zwSSoE4Ms6X9y2mguvSFi2S2tXjh9N4Q1HSznZhDZAokaws1AoY-eJFtpnjWSdVgP-B2EoKGysqU02afOoVgrZd_5jqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/We11RnJa9lNdVSsPXPrYEUGFM9IdII1u94yIGUJtzATPjCuvwM_WYBSijuqTAPqLoDWjbpkgdDxYVwH-cc3U6t-tGiVWRgquHqlY2vGhgZfpJmPUnV7Q5q1Sb_mr0QTwKXmUqWF5tvo3FUa7tNjZ6-nBwajISORAz3l4NeKoFiaTa4F0UydxVlbNNSkTmDIcb8ahc8z6GOg_GGEGsxrWHAwC7KP01a1yJQh_x4Cuc07eNnRVjWdTDcZGkhr1aXDgp_6Q-wADdLEHzKxHyjmkdtO-iosDjITyfQRyJ3HjGGpEpmoQT7IQfLobNZ2JCZTgQFuR-vBWLYh8Zot3_OY-ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYxUfEhqG8RLHS1O-I_IngXkVNWyS2eqfopS7uyO6MVia8UUMC5YcK-y85MVLM1RDGi8EvtLnED2CExlJkTx0YXKEi57uZaZRQY6A6Co9eq9uD-vE1EJAQuTDmHgy590KAWo-nW6xhIg0HDD0W0Xw4UliFFBk0zH-2wZnpVqYVlxSK5hiBH9sCoA7UCR45e7N5P_7B3Ojn9JvKUr7RfuulQYmHbiHaVmtsPwwm3yEZeN9Lxj0mimUs1M0mIi0OLNdn-60WsM77mnJFEZw9nJZDtWqbTkDwneCDmpF3YL6cOpdGddtIfq7mFn_fSTpV7aGOlAb-D9xLOxpNupYRed3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S1bMGtPsmayYD0k0G-VKU6F7w-6zdsgnS1bxRrfRJut0rlikPWtlSc_uzb1dLCjKOmHhaFP2kg9kgssSH9PcXDoGdMNx5tLBJ27Oy3LLaOEJClJAqnO_CBWwfYdQKJ3XV8FOQXqpFjDJKlTr6MC6eYs167DGf9HLC94tigcc4x7hj-EkfWVOlxgqsQRpQg_dZqfIXlwZs4nqoAV_KvpPDUICwKzWADJGQ4Z9yR0c9Uv-eH90De8QwR9ygftXEWsCP1RtD9KSPCXsPB1fE7Jyur7E7qv28o-Fw_ZdTqrIYuCvZKnVXryaacqdD8YG1ov_IwZJGlUlqquaEq49LJki6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N7miNJoYsn7yoyspI1ah0-q3BCpXtWU7s-Y2bFwkF3XjYi3SZarlqsJkMUkfJd2sLRe5pe4Werv2xmKiJGklSSlrwbS8cOgr9P25kHaFiTFQviUiDJz-tsYYKq6Us_HoISG9F0cM-_GX-Ii5-pgM4l2SwUI-T8cBsZq7BblxE62gvl6dqQWG_yCIrlzhsPqFDaKycMBMLe3KClOSQ-sJAqTp1Ir8d-ENKF8-F-f70Q86SAmu4GZuTbHUracS0oeDibKef5CQeBT7vGpmekLp5g1xRjYJEUibKYqZrPZuh14XSskKp4jCczF7O5ZYrOEO4VcNSDcrRrEcHP09hX8LdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ai25xNqtE0Ps-6MZKtxRvPeo729Ulb4hGz0qgRqlTtmCcIcW_zxPP1MGxhw2qSD07Ifnb5MF-usxq3PRDk0_BIZo2eI9xaKbrN44RYayOrzFUEqpXEdBeoWAuW2uxitbt8RKCYpT1BIwArOdhc_1W6fEakQ9gHelj0urj0EO03r8joE7Kt8zKYFNBeapSWGgk78a-DO6kcEQsVCO6hYLXWPfYbn7YIcVJ4IhOXSOZl-uPEO84bUIGySAKQalHOu24nn-p7LaYqthUWFBC4GQOnYzkKjWH3CAUpeGR2FD1uf2Pl5p_1nPe0klAD4NHhrqDXF_ynIvaKhyG_Qgs7c1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tG-xayh6Z6ewQeUBtjgmn4akgpVIbhCR6-P1OS-J6gHQVZo9zWCSOV62ZrPbSTLv9XOi8CE55MFy-BtbK7GXc4hOZBRhtIE-h_LPdjuyRMr4kuF_YvJOmPeP3UQVJDntZUz35VRBNtspr_VAgtTpitHIuuHQYjhCf0wFMq_TujgxpMl21vW8PGWK__LmbQ0mAEwG2sGLuWqe1DpZqnXHVML17_-LCLRAY2FP4Bj8I2-pE_la6St0sQeiDMRkKnNH99WVHK5nKs6XAV8HO-eZiO4lNlPudW5aFuLfNvKtxn-pEOoNNqaX54WIFYMO0BdRxjQH5B_VZVQ0zuJ40PGsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gz3lJMX7v9F8uFytgSrOpv5PBAoMh3nUzYZ-TT_bcBNwj7GXXDKs_tgYyuwgudzasPKH3YBAk0_LpvUyLklqdn3HlA97XQm6B4kZKhDV2duGiP-i5daoEjFSR7OMsTe0S-LfflWOpyzB3jnPnHbQEyqFTvubySXdxCBupnaKXHY-khYEIHiJZ2fwEJLzCn2ywCwwdTnUe6eg24JeNnr8IT5yBPzDPMb0WBdVM6qm2QFBG9TH8lqAttWsIFmdJdn1RWMOh8xxp1nEGTYQHPSi6F_oQoxi0h8pX82MgoRAZ5p20iH97iigQYeqKLZkzrdOTJCDDcY0Bjw4i4cbxQ1DFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KLsHVcV4iqDIu2LsaZTdj3AlhMW6fv9zDfAigjVpNF-xaCylcZNYhY2ONa_KGA89FxBFfPb2NlYzS5Hl4C82mExlZxQl4CRwvkvog-AcUaDSv4aMPSxIrpXss8st_qcE8o4TJaqsXxkqNxnqSRDyJuN1re7y0sA-QX7AvoFLTNL9m1g0eIGLUR5q3unsb72F5YgvAsnPUiKRNL9GERbCa0cIw2-EZFbngq2MQ9Rfk-mcho3eZA5o85-DV0tIo4hoZXvaykuW_5AngOM5xVR5lfFEiSs19jE58e9ccGMaD5zYVYViJTBDjUjiK53oX-3xTiCLVnvL5pnzZedEgp2kBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gt53PoM5RGcBrJ-wpEBGT4UQm4QIpBJ_ZKXjuYZrbinG1sHgA-t75l0-YTJDlAoo35_yheFo5aeE2s8Ht8DUtm_ZISecDFKswOmZj-iF2sjP1Fnsx4OGd3xQHo2yNjfEPF8yU0Qq83ZPmumzwH2uoaknvKdIK0q5et-8RHJz8B2iAbrTMKqeERfNM6-oF4DRoMIOUBWOMTpgPc-27SeCEhduA9x8UN2nhYfLMlnFwFfycwTMLst0F8JTa4dcShV4NW-cmnXuU35hDLoz0lAZSulHU45OwNNbQfNq6RjV50yis_6MHnB0wHMfd71vgPcuaql8ig3DpeXLqg--7yOTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
