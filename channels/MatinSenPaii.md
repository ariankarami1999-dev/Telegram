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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 18:02:50</div>
<hr>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkN_vQ5dWI4qboxGtDWR0-X--ugjvr9beTNgBQgaw6deMjcXIgky33PcephF2KcOy-YQiQDbNoNHwpeGLdgUocEjKeM0wqoMC7Fxhxy7HJ9kSBtpYaljO8JmnQytR9VbLzP3AebzPnc09OxwV-Cj9PP75F9m8tN7V7-9FJnQCqJeb3BAi4u2YnkqGn1WNp8J0h0_OR-E-idncz5lG7c6drmqFOx-zygu8BwHHB0MQSSWo7gzOBmP26kKTARgtXQiqUGTMM-qb4z4mxzT8Vzj-PGXBf9jeZdLwGNYlc8mkiV_oShA6U_czeT6FJIt3Y6mQ2Hk31dt7qdSkagBU4oskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rf5EJ1zUizRt7HhZnPrgPMKkFoP-lvUXqUeoPdz2YeF6Gu53WyfomqYmJ6XY8yvOKmh_D6E58oJaAcYIKXoXJKTsTprGREQU_q2yVN-re2R1w4QzLk4VpcXtiudImMvbSKV1v1FbFRnZtNzpH9lLRQf1vl782tVM06oBBSUi7pwQukiWdhPgFEl_l0c3FsrhZRUEo9Unx5LJnA3eYTk1MwIu9clBfjfLSahfHDR1GfHNKAphqsHKpYrPAbheB7nnYppJ9mciIKWBVuYtkjQMV06O_tZi71yf18SZrz4A5k_cbXeZe_7UVWZbaJ9SQlCodHJ7NLXhjAhl2MYo-UuUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lm0yBAIcsQu-5Jrp0le1chu_P7PN5kjoHSi4Q-ww8L-JwOhxHVzUmRDUDLJpJ0lkoSsghvQVLgeq1mhZ672YZoTdsE6b9_TWoZE49zmGXqAsCzzSyuuST1vDvm6RcYanUlSQOv96qNJV5l__W-6EyWf4UwEcu8FY3L17fzG2zR1hELSFNNg9YW8ImhaosGPRMpQKghcpHoTHy0Wm_KZPE89C4tfCcSsjGoQM_IEhKml_pOTeccMO7C9euzd2rRhu9zPHg2ZN784aQ_SKtMTcw4PKNXOcqo38if685xz4TK1bh4TO3R78TXGYI77OfYKOdYJ78qZvbwnnwjXg-e0Y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RQ18ajsMtM5YP1ViCes28xZA6zg85FBRuT6H4frmVwp4MBjVkYVDE4I1EgV9Ka2wriO4Tndw4FqMdUksVE_hFC74ENmV2Px4DuAdeB3IrjHKYXWMIGI2hbrKVYnyV9gsLnbr1MoXYMuGBcDDAdd8ueVdBgXraS_cysrWoqOtRuY0XvvHInd6ek4QpABVsMYp_Kq0HEMepR5jgPEG_39u9oMx14Ys2i_UgrYPR5R_eC-0hQEfQXzS5lKciAMBqwlVKPEoKzq7e2b18Z7CSKF-oOKen1VYkhWePq_ETB11w1rcxRawJh2heRo279pnokL1cF30J3WPqB6mXn1FaMaZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixqWLPdY0WZRyZBAX89BoZG5jeSIJOxHAksGheDyvOhMoXEzvod4W9o9XksPB7PHiMN4UtPFqd2KSlI3yHBdBpXCLGglI2UXBSv7K_lr7OLkiIiXTvbs6DJG1-i7NKewBRKqoslEmC3Fa26b8Qb1eI7Nx5RKVUAGtq8nCsiqeUSrK5jLoqHKBM8KoMTULgMFy2a60CJRDXQIaiRuLrIfL1R4QVHKacQmCzPoyvD-5jMxjOjqbVjxS8yoqhvhuHtkUmnWsTnSGLzn-VKE7DFIPyHVqLjJEYgRErOdmVly8k4TikHWqyxOg_4V_RV2v0pkBkaHTnGcGwel-y80xRZe_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BJg_6N-2fLzKya3KoVmFY5eEDnuDLN1Ws1GG9T5vUK5x1NpffHdoctw8jPULvF2a8GeYcEPiJAfp7NPiRo9_ALC6jQCguzk2_II6wNbXMc-v2n7r1hawym-ri50_rvvECFLNiD0iv-0ea5VUPUzwUpM0IG1sDjkAqNLCRGDBLgAW1uQnV322QexiGgG33ANv-FA3ewrHtXmluk63sKdfJE7WBAHpNOVW1oXOS7pdia8Nvlbgl2iHVd8Av70iQPefuSCx9iyMIwl3V7aAG-9K-ocfMZs11LHX4jcelKocLkwrl7IHBWFQ0Eot-x-TCZKt319z6NimzHujHLDAKvR0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=XyM93RvFCa-TcnZRUPCDS8UMOF3ElFZhERWphalUVeoSQ2DMQaue_5QxwloVt2HwoDPa1RGkziN01mMBiLxmQUDs099j95ZK8HT32f97xu8tt6lJlZ-Y_hEQrnHuz2A0jdsXe5KAhJOQi9GIRyu3ZpUQ_R6p4F7qrbW8Twb15mVyfnsfKqABURqobjV1A7GmxUeUMOKLZ1kpzhO3b5OBAvfHkHs9hQV4SZO6DzNQBShUr7zD1R89uUxZnSqq2-CalJp4ho-kU_aZS7-S8rpWJh4fkvwGK24_UXD397eGRgpVd8XwKrlG9iO9DxauxP6Ps3lu0hmsV81pLjq881-sZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=XyM93RvFCa-TcnZRUPCDS8UMOF3ElFZhERWphalUVeoSQ2DMQaue_5QxwloVt2HwoDPa1RGkziN01mMBiLxmQUDs099j95ZK8HT32f97xu8tt6lJlZ-Y_hEQrnHuz2A0jdsXe5KAhJOQi9GIRyu3ZpUQ_R6p4F7qrbW8Twb15mVyfnsfKqABURqobjV1A7GmxUeUMOKLZ1kpzhO3b5OBAvfHkHs9hQV4SZO6DzNQBShUr7zD1R89uUxZnSqq2-CalJp4ho-kU_aZS7-S8rpWJh4fkvwGK24_UXD397eGRgpVd8XwKrlG9iO9DxauxP6Ps3lu0hmsV81pLjq881-sZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T6sIcn2_6Zaj4XHlVCCfpSVrBCWXOxmBv1WMrhMqOffaKyPHFZt0-a5eNcucg9G5qi5nkHhwBb5rckqt7pfG_yrduqOdnTgW_Xpbsegzkgpgqo_C_DQC5sHUUSbEKAacNMJcANDqqnlFexQptH__xG5-xXovITJkSViNgh83EuWoGNQcyfGOTdr6x2RssIdPy6cdM8Xf1w9zd9boKhQhPAX1-VTiNvf8-4n1YkUtJXDYfffjBADuSYPbbcvjRkEpSP-_Q4lB1xT206qSZtHhsK0Gsbv6rU0fo3H-oq2ugycnKXBg58olk4gKqgow11ta8PfRJ7Jt-7xFK34JMuJDTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gR6TZX_mH2v_zeJ_6ibTVk2fJhwLnIg1vgHRuXKJnIlmnTH13FD8I2SDWs9K7_rGOzgR0yYufxbd3YDWeZszoluqkjij_a3VIpKYiWz02luZCSk7x6Ycslr5Va2E5kCkz63Qh9EEyVRwNn7aTtakye5N9moOudKnk81OjzwtJwfw4OMoIFs6mQl7i-JrC0gIJ_4d1Reanbp2TVzEIT-_VWdL8ZEyrt7kTS_nDrPD0TYDbtzzhjZ50Yyh5qUlwdrDrZSXHofQg3XW4830SsWX2pLIZeZq2dDK5jGyO2Oob34S9J5KYLqFXy7oSMEPoELenC_OWFKNgyubBLJ6SRSFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlFMjVNz3lLSatDEuLxrTz8bKnzxGEO5vW4wnj1xi_Hat4DNmq3ZspSvKS16V4Ll9nLz5sEm0dXRHFoIUkXDm2pmYT-tdCqGSTXiZ-W_ogYr0NT_intlnPnbzLET62qCSGJ3zAfluvVUSpQ33ebnhPRa4Jp5QmdRkz4cGfkoT0cGbrASORD_i3E2qgmUFO3IP0zddP9QbYso2Z_JxYU9ZNRw2Y2di88pVMrxteu-hjCxSCXXO4DBNMdbqlfP0jZSTw0f9dWKsThM9_tLIS2hgqGRfyYX-w7blAs9dc237r-gvGbQZePJkqiKcYvqwisGsIzmoHwI2E7Ole2t3GFXCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=aOz_3OcOyiEynC07R4dWlHNXrkpkApC4ouhAZPUBawEkydfb4TsGe4Sndm6bpC94fxazTBEXoWnLuZOevzW7fF441-sppUCZwKbplHK72ZLHX1SbW6KofTiWMJAGX9CSyA5psxN62U56h580Bowe-5btDfBguIapklEv8G_bwvpeWpNSAdNNEgt8hpKBrDZ2rO4k6YQxk0gl8cNN992q88N8NruJG2mwQb8kLG1J7cDhvJl4iNJttari5HbbjuSGwIlmqg7Ao4Mo0k1vkB5XfQ9sjcuTb1hq1rDwYMhjT-JeVS9GhA6TU0jJ_13q7_r9ehvMxCTtim3YCyWk1dg9FA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=aOz_3OcOyiEynC07R4dWlHNXrkpkApC4ouhAZPUBawEkydfb4TsGe4Sndm6bpC94fxazTBEXoWnLuZOevzW7fF441-sppUCZwKbplHK72ZLHX1SbW6KofTiWMJAGX9CSyA5psxN62U56h580Bowe-5btDfBguIapklEv8G_bwvpeWpNSAdNNEgt8hpKBrDZ2rO4k6YQxk0gl8cNN992q88N8NruJG2mwQb8kLG1J7cDhvJl4iNJttari5HbbjuSGwIlmqg7Ao4Mo0k1vkB5XfQ9sjcuTb1hq1rDwYMhjT-JeVS9GhA6TU0jJ_13q7_r9ehvMxCTtim3YCyWk1dg9FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwDxxnqdPsM3jt_du3GNFoPOivBcLAuYqQ_Ejp6Zw1o-0kI68Ax5cGp0s41FMbNnYxlyxII4PUG1L2fn-Uv65-gFzJPvHgkYhOY15ohHC0GysWpDWnLM1iS5uY8YtgD7rjirnmptKWgscI3CJnx0bl1Ksp0kVbPcn5BBZQ9khBlM9wvpTWFZkdDAKBVFhvt0X_fh-fM-3uovcp4WJafc1JP7BdUwvz8SGB6utZBpqATnBN0Kk_aWsOUNEfGGNjNSGA7twedmB78fE-VxDJiovvzzcwZkcYSJEkZ_2GejUGypHF50xc0QSPDoMvuupg6mUzAe0cH4m18oYr9NuCoouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SkD3Oa08ZMtWOMz8OQ3W_4QWcv5zFdyKJmuOujig7awFFeaqPNtAbjqTL1DPbSduxDFVccHRnWMHn4yUzcWWYA3OnR76yjy2n2B6ErrhfDGqIUd9joSFOk1DOkm4cLLOJUiksUmAS9IpH7F1IhKDxYn1C-_G610QR3nBZdkhWLWmGpTE3yasjUVLabD0Rya4IRuhDGGFTDtfiA7CyKRB9Ucv3A8zd_aXZWCqtoZBDdJ4fWE2xsu-29C9UaLyjmF1VDrp8vXwaTRJi19_NUoDV8uR7Cv-U50rv5FmNTHXJ0SCAcxfCzVa-_IiP8Lx-XpdXWVsGbTF9KSvvLLdIXnQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eIQM3zXd8NVLkseSP-6Q2Xs9obzMqkfbEFQ51aD294XAUsPDaHWawh31W_KUckm0auTw2fyLSA323rBo0AybwSHEI1Q7RfUa56GjshbisAjYq88fuSPY3qEN2wOl7_WXgZ8Rxi1CmjBc-Ose3sz3ILsXwT7yIWh6oicyPjepER0f6Pp8logXk2pu7H8Q7FmtZgV5iDa-5PyfdHvS0qHRSvfvNJdP3eq0jACpBeXZIWhjsply6EVW7O0AIeO-3pDcuNDm2up1QvVmdXXuqCZCdKCCUTWE-BxX3hBr415_863Vh5kKRPXRV0246vKFrd7-gQvqITvhsBA7aWou2X8w8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IQVpZfCzBiGVW33qTCD6IYnSIuMElF6neRCjC-7LgLE4vwchcOh_CgLAnaQER8icXeMT6DVB89YSjUdb7NDf0HDW5Tta1uFZzIRgbvy-mwWEE28MiKQvlVjlA8sDtRe2RXmR8yE0M8xgN0g1EUQdDx68ZhLgAmxg_FnQ0bjN1_o49dThfNA68xLi-MyBp1Na2iFbvljYK6PDCeE39qniCP_VSDVZpd8uENW75JHWfRHktOCkRD5uwqGpKzKK3WPrIF2vawhSBPTpDtkuZv659_4rTknP08d00CAHpP1XXBUYZh00HTaMLKALuRSJp1OOERc_GrvVPH-4By0MXMa8Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NGbry2v3nwcY7c2FYt_RpMz3PJc3yqPchaT-Oje_Y8e9fCxHUL2Cw11jvjbgakx1YidDY6jSxxTgPsaxEwVfshtsAbmajmwRKwQHSBas1Gw9ti4ex3g8GnJFRlmCc8QAi8guD_Y05SaLYX9FF6OV67WNlNoXTXs0v0ZVR2mZEbYPdhj8y2bkcQs_1tEZnaBGyDeNNWierXEYQH4FoIr0XKp_umg2Yt2GS2XQjGonxH5cJ_mj0Z68SJaKvcwZXeyCHdryaKYcyNItw3iflrLr164h9LNajnCu_CRxvYYnO52dTxiRBLnR8p7Jq07tXbuadDtbybElLJp6Kr56hxI_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=aoThT7YIsyZ93B5m-DRXJMV1rJgfAY3lRomcIF6CqutjJdRZQwWyULQlxg-l6tXfgQlT0UDlIT-5tDKBjc4bwRnHFYjMc4_k_9NRqZUckC0DWGf32bXL_n6O8rVo797Aff9A9qRf51yhdAc8-z4OdSD1M0hhimH1DY2UGtpUfHnc2NZ85_p6LIvuXiV_p78nlfHj9g7KayJBcyJwqEcUbNZNsqtGm5z4UV6ToFHHXCJlNfeouWMPmM69xPS-5lfwA9Tr09Ejc7KoRx9qoKJDhGcx1DP_ovhSfFglxhkd8Rue2AJkNCRIZD4O4NBEWtCs3e435Iw7sQItp8zWNLDFGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=aoThT7YIsyZ93B5m-DRXJMV1rJgfAY3lRomcIF6CqutjJdRZQwWyULQlxg-l6tXfgQlT0UDlIT-5tDKBjc4bwRnHFYjMc4_k_9NRqZUckC0DWGf32bXL_n6O8rVo797Aff9A9qRf51yhdAc8-z4OdSD1M0hhimH1DY2UGtpUfHnc2NZ85_p6LIvuXiV_p78nlfHj9g7KayJBcyJwqEcUbNZNsqtGm5z4UV6ToFHHXCJlNfeouWMPmM69xPS-5lfwA9Tr09Ejc7KoRx9qoKJDhGcx1DP_ovhSfFglxhkd8Rue2AJkNCRIZD4O4NBEWtCs3e435Iw7sQItp8zWNLDFGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ktFoZ6JeA2dh8ap3FNvORq3HXTVtOtWcgBxsTVLN2_PA2kFvC410l3hlMkkwZs1DXAjsLVjLyL98GX4OY8YZlUFSmTOF-oA0XL1h2rbVK1lnPIExICwep4Yeesq5EhwTkkevmP029OdziCCbhDq0h4c4QJWOZGz3whBd3zPbDdLkQftOgJUmrLQ_sAMb_xdVcxggn9cCA9wyyPjM-aZZ8rJ-k-Gf6scS373UKIHWAX7F5UD4mBQvvtk3nO8DlgsYAr8mD42PDh5WQxwTsVd-qvUeI8EfZnhQ978_qAN8fhBMx8QTKahTc27ocxZJa38BrT1a9vuogy7k8T8ZH3L2-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fwdpUhH9q9B8ELL5VPUz5IIXkQR94UCmoGeWqWTEA566Hg9f6FHpfSEKxtsa_U6D5E_Jr9obGqdx6rMxaFaHruwPQkLFe3eh7-Rkk9Bryjo-nYFJLMng5aKZfoukT_r8pcNVqwZHjy36RLRNHQIxf19CWUSiaOky5NJMVMEE9G8DtExZZtj0KThFI8FmpBbtDA1YiUc3QX8fcjizXAS_ZvSghCP5X6ktaZSg2rni195B8fK-rRe-vNSeZzNLkGFBJo9MAcp5OYp4jIf80W93l_-WIMpYcDdk3dcKrNdSeIU0NCM1K7kgNW4zcccmfCZFrMfWQpVqQ9F11Jp4lNc66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X-Odgs7GMBFYzK1nFUN0wXWYqlpEJF_axHMVHN2WQBqJqC4e4X8FW_FkBXW6BrkdbA3ijOnsxy419PFFzRD2SOZwlMfDAPE7fk3FT5OhJiF58dN1YaFJ2BBf8MKpRA5N69JbDH4acrdsdY4OH42v1mXHozvo_QEDe9zB8WXXI99GZNJdgjE5YXurKffwg3BvpxLS78-vGp1nfBfXXJDuCqTq1K1IchQOCK6hLUjK78E7D-cmV2-j3w1jqe7LSaor98Ss65aGEJ6kVr0q5HmKaagNduMtJXQ6YjZ5rQIgH9EXvK9n2zio-2g2ZXbYiH0Qwxiai9ihRBQhthGrZJU5JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jn6iDVhdYzIugdI1nrwKlO0-5MgPWVFcDGWnX6bK0ygacOfMi_hU6L71VliE_SdNh4jPrXVxHU7In8dB-WuNKrcxNy4cEMGwmflGATzFe3q3h16JITrAvr2fSRuSIDp2b7xTgDHJduWjNsjZH-Z69G616Kfrr28Ozqvlno3MrVI_-N6IZqyjrspUgSUEgvNllAO-j79fX9weeVyIb05_2S7Kz1IiI-B1SMEHjFtb2xGKfdTi1CcWXEf6gP_TRrt46uvxIihV8DdBSpv3newKPNRPgt6SR4waQlqw2_eGFu-OCfxb_Qon6MZQ-v7qlfvak1Val2-0EL9VS1w2jXpNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKZp7L1nRYQUb93DIEAzG-cIj6TYE3VNqLFLxn7Zs0Jfsi2rk05nUl5pskVulicFQt1IYqyhYlqmFwa1JRk-wtd3yxp4s1-WimYXoDlrLU-h6BYJMmUN12Or4Irt_cgmS1NsJDvcz3SL9jmUAp6eQMvxocDwU8U8VqxoTfcMmTlKrgK1RBkpCxXaxoAgOiHROHHq88nOMePqwfS4O3IyFpS7uoDKgNNo2s661NzdQVDP8dW4RIWpHmTk-PbkNh8IkoAz0uuBXOnh5ews27MVqehyB084NDbM-M9cNsl33dysb64pY5RjlB_FOcr7m0FSRL--CRfM8rTkxBKfxhkL2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dMeAQB25CoyFiZzMOglrnxLS6-uKDIUCGN0lPjirBDfhZ5oGay1Yr62mohcHnRFuYJmr2XY7BXHCG2WemnLS56rm0Z5lVyDBPZju53bmOtTJTdOKXDrerV5p4tCdabPXQOCWifHKT0z_1XDGXc8l2_40ixnZkTecuErJRSNvy0m7lZH0Kl1JlJX1yI4UC2WWdO3E69Ua9LO3QcRTgaNHN7ot9NqBVfH0RDiHO1jsFY3pG7Ew7Ylycv2kJ76rhTTqEE95ufkh9huH0SYq3y2MgFfAAd4BIW6fpNNAcz-FJ43WteENwmKh8fibjfeCCdALo6fzmj07IhCBOF0622h6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ml7U4PMJSyc3PTSUSL-qw9wTzihqvWWxZ8J0YgWCHqsxnv1T8kscOOQNGS6D5W9cHAO7ElNYUb-J4cEYlJeqzddAW1I5_r5-JspupgHWWWkxAxAY6UQDJXoPmy121VV-_MPEMPGo8oLXeako4wSxhDWiOxzvM75OQbCtIgNo9MTKFBMpm9WCGIUHQNUtA_EOs_QvG4HcqQbRjHHHtUsxS1rcY6eDVdF2zQAmhbz7TUZ2i6eDtncH4R4H3OdzbYaTMgH6BCZ30oI-XjrZ64eoBHLyPj0y3POl8JoNT6CHj0npzANoF_7Jy__p996O56bGx5NQtRXUA0Yyxb6VeQC45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVD75X4Yui0JDZYdFqrDnEzy2NN8wQOpI5tMe_AZ2YkGfLhWXsO5zLmyz-WomWvhbdt2D0DZ6cSKSCPZr9adZyqmNPUcLW1CRzAD9Esq-fmVLyXyHm99i2hX90uxlQeFmE7GGo1BXNRGchJuPNJCVoXQAnjsqtwDbK_fnht7RZ5zidL-bLP-OY9qeX7JBW7b2wCICjJMiKCU_Y1q6YT2uJEtQxUd21TEW3k8xagj9eeRYXzrM-y7pk480KIq0vmz8s10o3Y1TcjqX9YOiKSwInhJ_X894NR2usAYaXGP2yD3Dw_RNJ015Itn58iUYAzccc_NpNVpxbDodmihX8Hu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=ppd6bFw7WAWX5N2DhvmTnqs3SsyRnmiVbg8iHyqZcdfW17yzl4KowpuUOO5zBJF7ZbVpZMf96xUhoEVwFyBFHAtJcMCGIkwZxa-BTZf_GtIidIvYGhp4GKGc2h6Ql_9g2I4tEOspBYXLjF2R-ql9K5f3ZzlbcrVcEY4PAF2xWL7p2uZVG3ZeyCBsQr1yGjp_N_J5H8LlIKEE4VaZvccFHShMc6t2Eb9GsDojhBjvBq-2FuUX6U3tewvo9v1HtgF-l2XK87lBm468AJSM9w-eKTbF5Ol45ib8aI720Uk-aA_69GoVV2fHaDbKJ34totLvTfn-xX_nr9PpcAL_EPFIoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=ppd6bFw7WAWX5N2DhvmTnqs3SsyRnmiVbg8iHyqZcdfW17yzl4KowpuUOO5zBJF7ZbVpZMf96xUhoEVwFyBFHAtJcMCGIkwZxa-BTZf_GtIidIvYGhp4GKGc2h6Ql_9g2I4tEOspBYXLjF2R-ql9K5f3ZzlbcrVcEY4PAF2xWL7p2uZVG3ZeyCBsQr1yGjp_N_J5H8LlIKEE4VaZvccFHShMc6t2Eb9GsDojhBjvBq-2FuUX6U3tewvo9v1HtgF-l2XK87lBm468AJSM9w-eKTbF5Ol45ib8aI720Uk-aA_69GoVV2fHaDbKJ34totLvTfn-xX_nr9PpcAL_EPFIoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qiFjDQiSPn70wI6D3_wf8vlCUYKv5_Am7sgeQqDWwPamLXr1O9c4zC9et8yKksBR_piIYuoi9y4wOn2Yj-hr7LJFQMVwbXBqC4gx9Ei8E7UeG4GG7uG1SsZ13zmu_ft4CnwMmcAbavwF7eqAsuvj0VfPQjyPWzNQFsd6JciCeTHSZqRDgcetp7Vfliqz-Py0pjgVlAhfyHxTYGT-yHGjBZGTH-xQn8N1Q3l7dOIU0Pkp4lrQdVPEkthiV6MkeUY_To0A7IryyUEOEYIsn0b3aOlaVnl-kUVbGi6HKpdiLtTipsiDC2-WSjV9EVBcp73lKLVenhyPOGvEZ6HNrRs8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fvPjltNg9g8C94rp08ooy3c5B8T5hMoH-OEU9TTCbJxLsl2ee_asMcj_84xmFzIGsWtI6Aesrbqd13Z5PpMKrxzxyQVP6c4nOlQRvCU3OJbZowu_e33ezwL22Bmm2Tw3y1_mh4aKcEgg_SsyRtpBjuCPUtSNc0DNiyROl4cCdtTZUn1_v-oc0ILQ87NmkULVPgCtcJC84U8KnAmLNRcvsnqy4bQ_CBVOcGB3A5Ji9ZM8_2O85-PIp84JVOqkRRUUq-WgSzboAg_PGUgPLBPpuL7Qtht0oACp8ziwFdLd2U-0-_9KgEIuXke550WL_Sc6uQv54Gz7Mhw55aaBM6XLbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPeklEERXDQzY4D46fwdpklkGeNlf38kubzEO0gSzychArH0oRUJJh2mBzEEwqaIXkyovAUghSsHLNtphuT9I74K1DfSm4_D1byjwCR_s4KN-xcxS4OhY_me2gq4QVng8zUM80PxeZozvLsHVpAcAxK3fpEP6LBkL7NR4e2A8woUTk2UY-SATtIJ5681rIborcV6_Z8v_UVmJYbQJKLe36DcWjlIjpb0URvM9k5ihjxFIF8iMTZ9RUuifB0DUJ9gXxZWfP-lMST2e-i4rykJC7_xFmxNZzbqK1Lr_R64_KZ_DAzylgFYSlWkD9VmfhdCLqHc__F5Amwg2FcufFzcHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-dpG9Z1i44hx0MA0MCOqCzA6jp-ra6e8km82Sh90ANPToScJMhuCs567Cxl0vIOIqQzBBDtlNzihhz-mrY3mBFbbKrly3iem8TJ5kF_uz9VKz3htxUxbtdFOC6WUdIWa_YuIpy9clKt0mtrQ5OOfRHekW685G8j0HeryoGKhe859sXYSHrsHHZc6zX5yDHt-sX0IupT7fJKn-aokF7j9zWKvqajzUYHvEhfR1Dy7u0sZRc8zbCGzKVv2kXxxcodWwV3doI1hxOBk_ti21OEt8QTfwLWaAtB_oqgu6MdaPHp9VLYxPds550x-KosIQUcr34u4-pVFIRSUZ3u_OUAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uz3hnnry_Xxy-NaJnAlMKRzPGGKlozi67JR-xHoS2ak-Uc42PX-RGQWoXJeMFH_cVAmWkrrV_nuz-tuepOVXyjzX4mB8VwxekYva7eGrYYTMMUdJPuaCeYR7n036Y2Xg2R2A_dLal5NxSah1mmTz7nxWQNgyrYXUPK-UPssUljfdXPjcCdl9hNRf2gVAr5qcotkKFOg6XdBylQZfDmMl36u4yEHrbZj5eOcQ9i9-jrhwFutQlpwfhCZ3VMzfF3galp55VKgIprbI6o8qc_6LP9OkKX31G6aONs7Hf1BveNZv9u2IOk1oNE5ujxwkvfEfQJY3riRMdLYNbeZoqcW8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TZsXIdrUr13w3GjW0DPGYMyqg-R1eY8eO1lVI9aiAefivLmC9WOMZ4aJGKodz20iX3PFWMKVWX3O3FPM6vmYkoroq8cP9btiT-XmvcW8MCX1L9o9TNaG3NfW_VsqPevcVx22QhNzdtDrjlnnEsVeIvN2d3NJTo-ug4qAPjnHgQmCm2EG8pjmh5ECUOaKy-G8ogfPaKSNbqM_baFYJNeFko-SfEFVpM2gBbD9_RVXDzeaimoKIkyGXMykwfmnjGB7HG5wsUANESTePci7jWevnT6bzSnwi8jFQc5MDlnjoezK50U__R0V1vIJIaHJa9Sa_pG9STUJHDn9nCt_Iu3Llw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V9I5MI6D2sRzOq1kloDvQawsz8_a_aTZTbFJ4B1fNWEES1t0iN64m0a0OtFsLJmZI1oFtshpnVv_ctQVdCDwFoO9llr47mINO_KcLzilIgPj2qoJrPR8Pu-EchxwTYMYbHn12GYzEGS8rNq4fzjMp1O_2KzXGAbB_j0OFcAeC2cI8meSXOx_TbHn7HvLLuwHZVPw29OvBDGRzBmX4dzTLot_Y4wjHHAc7F98vKDIxY56mJEZ_18Zg8y8fpFaUoMeeRUbH8DzmF52i9V00skm9Ye1PqWGk6WGSJu9bsEuzohyog-3fBw4hw77RhnngPGefjcr57F4RCAeRICHLpWgfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BK_kX0Xjiseb6Er5dz0HKiP5TLqMrrkOp9NwsrQOrcafqJqn37F5h1W2X-eEwvAMAIaqBM9qR8f7GGpc0-rYKkbdSQsCSX1DXaRSGkCjp2mM2B0PbxKI4rmF8OjpN2agdwKHQ6qmFHPrfGTkRc3PvzAdd4fIAxgc_YIEoVqqh9og0ZAokWusplc8F4zTDxbviF59IwdFlm7SK0E8xwq17lNrMfm7Xhne5q24pjc93HDg9AKN1zKcCxr8xW2ks3Ch1azLMFLD9O9TtMlBnk7qfjI_Q2OpdFdwPpnfW870RoTHXkm6ATGfdOZLDbPwkhrEBA1JlSzNRpp-lG1hmuw2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eIMAFx-oXkSl3DJ3aHeqAaA4W23AmC-ULI_kK_pQEZIiIMjVNC505LW8NhHU6TRvGXaad4oMDioiy_9zGpwpGpp7NNBXDuj4rAY-YMf8MwHopRIgPv0kJWAbr5d7qgPBUs0R0saISKJHsP06lYq7C9ZsMPWmemWjAefLfVmUH6A3M1pTQxVnrlQQSIuN9XqhaM3rSSnZmyDQRESygDeztZVqsVhnGImbtJ-fEZwe9d2CdcTWz7xxa2QZ7_n5NiJlz-sp12v8-5NjVUlIuBV9zjpu-QIicVVVWRt2VwUI0q5t92iFYYjiIUq4WfUrs5V7TywP_Tcv8ktdTEkF-A5UUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uI2tjF0wEBoTymvj4vTveV4ncTR_ZkM15C0SXDmIORm9xHBObVlUt775lLHHSzFp9CWOVSjLgle07WuilrO4XjyXcewVbCUcYKLAV4T4-j7z2uj8H7FAYb8It8-ZbzaqByD0JkBHpUpH-4aHXroISmSFlNAACSHD7UqakT2x2UVMzblYwt-cYzys84y_cpsPaYIbC9QfkVq46aZj0w44s4D6W5eX5qnZbdrz1r7xxCsfNrYYP5Arw1MwoqmmDOgVN8bZ5DOES9NsVxYOcJnhiExKSBiuEozIjl7ZGwfKO9hvvE5eIbL9OJ9yDuJcYOrS9xDMFRR0eaz3PYGkF8jfOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/snR6levG1mfE9-bXOrYEOYiCpKwudvhFIh_s-owNyZyCAw5AaZ1f5iwkq93bNC0s30pCdRmnmqVVETdQQr092Eh6LIgxqQ-5OcBXw_q8En6su6RlaRHQT3uUlX3CsDzj9pmCidDuL2WxyXbuz9NjI3vX8eirQmMYbt4w4cJvD5p1OOX4IANL-IYUea88NMorJprEnuS0yTOdXi_9ktPc3ZK2F2smk1CLA3tq9qSISkpVdKSKxtjxAn0NNKnZlfl_US4uOY14DEG5LpO1BuYWfpdPSptV61yN56k-eHZx_CjJ2YWOd734lyT4z8ZTjT7HaBBWzL1w-5cNUCQsaxcI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=Fwl7qc74NGyxBhX8W2qgJx3PpcFH28d3gNW_nBAdracpUR3KHuITgbpY_f8iI2oLYpivhkjHeWBOropxRn3PlkUJ5uajKDIMR7k-J2XTQfVkLbG5AoLm3IMu7leC2-wZJVJn3KMQ8F-blVL7CSSFEIJayARBxDjM9w4IS_y3G93qxHEma18fXzGgNC7hcDCsPU7720nYNhqHx2XyAsHwodX9Oh0XrjB8-JMua8uOx7dMJPNn07zeUF1Wx8CvDyHcXvQiWC8sPGAMAuHfyM47ncdjmx3TP8D_DvvRQY-7CgknadtBbmyjYwikDbfFXZD0QASuebTHzSQ3_GcqmXP1yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=Fwl7qc74NGyxBhX8W2qgJx3PpcFH28d3gNW_nBAdracpUR3KHuITgbpY_f8iI2oLYpivhkjHeWBOropxRn3PlkUJ5uajKDIMR7k-J2XTQfVkLbG5AoLm3IMu7leC2-wZJVJn3KMQ8F-blVL7CSSFEIJayARBxDjM9w4IS_y3G93qxHEma18fXzGgNC7hcDCsPU7720nYNhqHx2XyAsHwodX9Oh0XrjB8-JMua8uOx7dMJPNn07zeUF1Wx8CvDyHcXvQiWC8sPGAMAuHfyM47ncdjmx3TP8D_DvvRQY-7CgknadtBbmyjYwikDbfFXZD0QASuebTHzSQ3_GcqmXP1yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJpUMx14kCfrkCjpqhsqxM6kUcz2MzxLd8qNoUW4ExIwxh023hYL9SVl5SdBPuqqpK9Slfrh6aKTBBAQtDc1E_LBqUDILO5CtwOZT61UQixsaeTW9sKNLBjnURGoFSSXXZBBsNdp2nAfsP1r6-rROm3FcXh9erjrCOT-wclUFg6BT4l_A5HMgZVIXxG-ST-YWWifF1mE-DOjjw0Akzhsd15F1Iv4mhGyS9Yx6_KneGkaXDbM2NhWcvNzn2NRupaSPDhAl9CsKzPpi_XgEc9jknTBnf69OFHXb1FTcWKKdphox0kP79EXjCtHTkVSfnbYMqGdpFXm9aSn4DVZKwH0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uE9RX1O_9COWu2FG07gIwn_uCqFzWvuHV_R2j4XMAAqNsNKJY4ngvwR-T9DDtGxh5E5Nu-44_lALTcCl9NzGbAcE4l_weONzeYrabj9VfsGxp6bo1C6JIbjGL26t2VpH5DjebnJ92gEXmmptWbNS-uhZlwrBpWcfxDVm_bHrHE9YZ8n4-wvPls6PXQEA7rqiaIi_Oc3RhG4WBZReSV5sOvj5fCzvKrCvSk1u_V_cYYfjsMr7zmLkv3XTF49rPsjrHjZ2mc9VaArEwUcbikBY12wfplsy9Y33yuE6-TBzBCLvKPasoeXcyxjSZKHyWmL940gOT0QNljU0iUa1pKfxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GoTLt6KQiQaj-UJD7fTMGy-aW3a5wIHovHK-0kRSDU-1kSPDdjXxPIsEEBV1oiJ6R5mbDF3X1wiOKDt6Eb7KRxUbD1IJ090cGTNpNtCAbigP5KVkxjhZJ2N31Y3azjSKahJImUFBUIPiDyIDqyWb5Wjsb89M-MCgSTIuyisx7zvh3N9JHawh4qnUCf373tHlptHvmu8NW9vbQMVryiVM3vG6CUGDWwCyNJtNOG8s293x7gmIYcU3rwCVt_UApTKkVsjrV6PW1SN1bSzvVqmCU7PCFw26VBPbRtzfEU-PAcU5skGVGs-Z7g_N_K4C-NgBgMhENp3Aldt0lwMxZhrd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWW8eSOO9DF24_BSnwJkQamQ0ZvBQ6jHTvj-LXeKK1IrHQSUfPwIsrxnm1uMA84xPYgDbHl9yFVPc4hzfefKXD6gwl8C5H2w_V1Fqdtntc4M0OD19bzcVkcbVZbO_4oJ4WlLOhEauFLgT0FgAFik7edQOs9HkfelyC99gTR-i0qiqIzObFybwc-H8b1hG9h33FX2t9a5fPOob-YDq_DFyGZBg-fFdx5B4RzwIVC7iEyDJYObAaLHVy6y4nlIo5cZjPYoHUC8B5WyBTljQzX_kMF3ail7btMbzJ1esuvqP9NziQN8vHcNoHMAwTqX9qjM87GaNXfqWswEQOdme0UqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G788BJmRS2ox5-ju0a0uGk0NqqhkMMcmhX1UgSu1g-QKYenfk9aEZie3473OPbJCY_2hnQmx4HpjG8sjS6rILbRnOBBZaUrsqYmv-fs4vSxmLJOi_iauaBAT3LN-wuVbxlGPSHc2AOB3Yq03jhKhRfyiXZjjEuRwXrpMzI1rkV9M5BSSR6n24QXwledNAWPAX4c5PQKvB77IVVpZUXEuAHjIMdDmeMZZOK1KiXXuddz5DM9xWMbVjsushQnapXwenJPPB7rc9SQwM43-QBtxB00oI93lkiuzX96ncJOn-ZOqu-28UiUnutiZt-9Qy-56wyo7Zg4Mnq7dffLHi3H68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lfG5Q1yxWlI4taqX8SU2mlgr1RuNernBAvD6zatsDEeIiK9i-6uh6MQAlljpbhvExot4SxxzG0OGLIhsf1EaRMKA88AgLkRorMMeMqsYyBIyg8NZG0wXqPdbAdKe6oT9vt5X9RivRmzLR7Y1zhFwNPdMcXHL_rGIF2SNFS2lvSG7AQvHGa8_EFDMPtuorK7ZmiwD8TQJf8WWWyWApSSeB9CXM_N7WDl_ndMLQpegk60Ls26U-j7NbMWYIbllykc6mXUxSDEh9-aIQB1kaUFWyvtoOTdq0ElgfQ0qxqQhPn1iw9BLtmtVfq3kj_kULvn5_U4Y3wkvB6GkGnhmByxpDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RXk6hwHy_tBFDCrquR2rqqSeJ0SCpifr03k5K8WookkDgZg1ghFUF5ooOpG6CX_DwDa3s2Ot6daOBhL-KPB1Lr1KJOU6ihuUQRYQl8eHOGhbV0GSa7YzULt37nvLweQYbUf3F_WnXnx-62b4k15_iP4KkwfERC32GjDcerkDXwYNY7ajOq6nWGuC_hSB--y9ClJXJ0IWo2hVZEBP_LeN_QvtUlZsIj90pX8MlKjHMuaA6jL5QZjrb7El4beBMvCgrjFjzFQ2THRC4luLXu3YwYx9RgJnE7Tqr1BVlg2TzZZBaZ-xZyXdRbWTrWPAwGQyyzC93_gvDagP02xYo1LoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j6M4HXpCiAhqgTN3l2BCit5VWH0S6EaRQ_k49r7s7EiC69sH_5dQ_BWV1HyUgJRKUIQRZmCJPXfnT9WvHXj_eTn-ro04NQHP66do9QiFCvxUhfrmc3zApKi836lxuuNGUDOQEO4Oqtak1-fo6QDNk7e7KF4fk6c_4yTC4nyCHhOGHy7J4tM95WUahcYuS4xk2BB1yMKrcR45VTSDlIDWmQVBL3M7ddEjHvtS9aD5HPNMl7EI99ela9U-V5GfqorMIzGa5oa_HmuJvv7HZtinlcTugHDN0MMaV2qtVcsbIy_6pblezf8T15HXc6cA4KeKOqV1FYT1YA3VZHim1yEjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dw9XqSdbHJS6bAtcZtdv4Q49aSYPEqm63zHv4Rle0f9Irag_0rb91SaorC5Uv_s8af-HEUtHXG1Mswp4HjxNBzDD_3aTf-lK1luZ3Kzw_p1A-sqWI8CmGlRMvClRO2b3eO5h9pX5ie4PjzfaBGyC1IJru_TSvuSnYfDD6uGwr4x7DyruyvU8wlyW80_hPqxZeFmXlL7HpdKTdig8ReeI-p-MShwLwKR_hS3k2tcZNcI-BB1a2_OoEtT9vMufPQNM4dL0twFswQTEWlR_buE8pZOJFt7T2he-2XybDHbYfexIpY6hnfeZWyPHIknJztfUsI8gkOCCTmLMYaZQVbV23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qn81Gu1MmnQ1-CuXBzo5Fvkafj8WLY3L0ueiI0bQF_09MpRcg2TMTNB3tT6pCcrZ1i3g8h6iw1pyEnHPXGuFLTJoGM7NC82XTI33AXNuqRodNgroUiBX11ixTAK_fGqr3r_hwP_caGIhpQ4Ih3KBRsaodWF82TImW6eWok2zqD3Z06Efc5DpOSapJwL3MJmqLCF2Pv_JmaBBNalThBNUYJ96d_ijP8ua-WK_-c5b53AC1oKxzgbQ3093wyR0K6b9g3eOSBc6HnE9GM0FgwAsqW3XQUaOTjobe4A0evoj1kn6tIOHKlyZuLuPbC5Q2Mc9suQKZ1IKd48F5xcDkME6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ijL1S2DcFh9MPCMjJ2heMDOuvLBqTK3dO9X559IDsHMSQ7jMgj-Po6ecSac6RgPaP6rt8A2brKHtIh-CBwIzyfIQK217Bsb07sgYJ7pJOgtWb1j3pWyknG4dRzMn6quVflALyK-EonkwpEpkZuQmxPKc1TcnPhlGDRT6QS4MN0V-JUz6X9Te0JJUohnDIgDT0KAWt6z18XmAUut8u7Ak9ecC818oH1DYuzD9ug9QeHkjRbNDtrqQ4K3ZSwura6ocLb0J_pOwL8Rm12evbeyTmwxw2qS8qb83UoBKr_25-pW1TrNzY93TCXvSSfndk-_vYC-sbRZyy_KW7FQu8QX-bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DHajt3_Vgi2AhyJ2ScE2KStK-EhlAdWr7u7BIloj8uN5yF2L2WR2f6BUWvnkA8yJuugZsHcuQ2Ql8iCIl5fQbF6CXE02w4ZSVM9VBYailblXMnZ0J6izMMO7t1VIW2G6_x8TnfAP1cvPSM9QBSu92X513nM64bua7HoOYjLruUZgYs_iif62Pg91Zh-U9k4j46IXmjUG5Dx_DQzL8gGdHcuv_CRyAc29hXgWdRG_FjuUhzXcdK3lS5BYQB_cuH9lyKadPjqboA16H22I7JVKxQqQjxrWbVAqbg7jBnfsTB8jYig9k_0936AHrGHmyrSyHc7iGLLChgoB_QmtZtyykA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hBbZiKKE5eeZyy7h_wXadcdlro3JIYiZ-hGxhy-F6rpMb8IJ5WLub6Kvyzi2tFFclOpAyZyXwnZs9g4O5YCzH2P-EaktceGAICqepuPjFjdWWQgeBbHtTeIZWNP-_pW5289Cq2ZqeZZFqbPMo-4vlwI0VUZXd98e8MK9G0vCEAsN6b75WQb3LFy-xoxCZVpQbZxlZk_lyDJv2ZBSjeEyRR_X-Jjhz94SA-iG3iL8vG4QUs2wgMyu0mFzMHbxENzEmQWH2tKap67VJu-28ouYCmNuJj5v6HIjH-0sBCO88tOzw7jAMLqPWs0u3ILM1r3P7DhU_5nI-0zioIAUOu2CGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ATIB86BAFeEBynhkPhdvUOBz7iRNn1ggIWZghTw9rhapGVYzX_xU39V85XitnFKRB5SiJll_q5CBPhZt6_SP_llE2GWPG47ZpBAvZZ134EwBxqaGA9lqBVdauPUTSuEKWGVGVc7JkC13mE1q6gxRnWtPrTyNwS2xzQowiCeDVNRndHUlFB6tYKC2i0fNKvHtxDpX6v1KcDGCPOWCxjg29iWuLZySKtcFyGKqT0mW9Q5brzaQKVtTt-hVU1C_8fj4Qfp28hFBMRZN0tHGQ5rcTgul7dlY7AChgJgiJB1ThZBZi3aBuEpwHLu6CBdHBeUCnxKa7WTocCBX8Jj1F0MlZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PeWyb9MonQ0ABBnpMxOQZXBdnrIsZ0ebcc_5tIfH736_IHRMVpSWb7mBe0omO6m3RkO-h57bqwZJpiqmA-TFMrsanNSU-Fvm1ApPJJOmWDrP78LZbBxog1vTYUJwUhWpnINHl0Ad0aa4i32lLjcuAFTpmizfNBS0IljcjMj5K8n2mXeizCU8pQGFP3HNQNmpsls790fq1LPeh890GQOR5cU0Sa9EMEYvnz15YkWJotMa3W7VEpLkvmZdnSrV7ZpGs-rx_aBC6NZqH2BVKhJ8tuz3iWAmC_91gU9YkDaLTlSxciBZd-oH4_Ac8DsoawH5ARLMEqb8H38nV4gMF-TeMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qaIrVS1kF4LHkmfw-jG8-f_szdPI2esU4YIOZWmY_frtOobnp7xwlFAg54GjTFXUz_0vz4yoo57YlfbCZlsALLTySRkel0Fnzkg7TpJrEDo3zw8uIyeH-rD5bLNb8S3LfUpt92Ts6mK7w-587tSrF45KatwhVwE3YFYmhvXhwzeP9NDnosIzzcVoZ1iKwMmQCrp0nVVFyvD8HyryxUkdm4Sb7f2JmDybWUheBcncmPoeqY8CELqgRTgThBer6ZSfkDN8DQWPrUqf-kPW00XACysd6GPdAXJDNSPFNylpUXEVEj5K21feTP7zSU_rg0U-0qhhJ0E0_wTJHNOgr36lcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D5RW9yGuOg1I7_IaNaFOUAFfkKeVGYE_N518CtBwMNmbcSW_zyXT1uqi6arPOcYC3Eb6NQCfZgWkgWgncDKgry9BWr0hfyjFEdQnOLkJ6YaBogoy0Ou_YfIgFCJpCxO2w56F8bYOhdGBPauQbrW7_wP3w1fcEAWAoipMixe6XFO6Zvb9Z8e3VC2fPQlIPCue6Yw5QuD1OW_pAMqdZ-Ak_DbODIztb6YDBcmZCgW3MCpHwZu3KQiE73FWnnvfKb3HM-fBqag8hgqyj8zh5P8r6PFqM0Rlb3sCFuQSBiUgT30ajiJoLw3ALZXFXnSwQgR5K2pP3D847WKhEvmbB14eng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E-HqJ5o_2BZ-LqufnEmPpc-d93gSOs9jtl-WM-GYJle8kxnngBYaNUCF2xY6kJXJ-1NXvvvzzGrRJmyW2c0WTzSKWy13KKh4l_br-46B_u2ohwi8RbCzG8_sCjYwVIcN32ygpmTB43-jRUlc4wmLS6CB94LX7aNqe-ExlAPPl-83gCqxiED8uzp6-aop47xlg3IiL8H_5oZta-h4jaQbsIgIsG1LwHtDOI6eWHCbftgBB_cEonpd9fWCuVBfMWJQB--QCv1_yW4tqR_vDojSXI2PTl40u3wuYakBLXqQljM9Nz6x-e6-tCEARUi5NR084Imn2c3F5mhW8DAAjhh3Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nsgcZ_37h4QvZqp1_kGNvXSjtukPq3JgdkPDxJUuribtAO3dWFeAzy9m8Zc_0o-qCjP_kyVlz8CVWEMl3U5ZnZHBiLRy8yhC3EYVW5oVr0djsFMX8S8TH2mj4A9gIgUYmBhwXbV0VORuW5s0wiopTlhFNOOOt2788SxmfKWxGcX4Xke1Gi5n12hgl1tEf_x9l0lBeR1-JCncdu4HHt3YWPkubvx8BTNihZJWoHLgTpEuU_8nizX1081rCrdkQSrrEW4QbSut0bC9SGeXWl4oExXS71BLl7-__8C8xZrin9WZv25Wel3pPJHLgK6gfbUL_V3Sc9TSzzyVXO4C6Re5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ux_slKEvfkSMCZKF-ZW-8JziJ1ZaWYEAQ3XcD1vyTQJTUQW-Uzs9ucZ0Jj2xHOn_KRATOcdSxAKkRDWruxZBSENBzULd4UKFt0oTG4i4_soBCJcEVHTVrU3hgg3WpD38Vi9plqxmPO9qTPplQhLqsdaiTPxkx1aIAtlw7vgQG8q9Nl_6Z64QrjUL-x0fZqjmbwCuucalok8nO-ivqMt4dJ9T9mfMPranlkCA68VmLhraO6knQgamKaIWdk0Sz5OZBGUwcn_EK5YZ8kv2glYkb-_VTtY-oFQb1K5R_CBQYJ52ilP5Wv_yQypqpEt85QyI7odASqkHVwy7To4FbKD3FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KyAIBz7CtPLmNxhPEfOiZvuRpcJT3wlZdVmvg3ikZ4PS7W0l2JZNDq0sTS73GXsLtXIYmi9HY9Qbm77E43D2nHI32Jz2MnsA8zM45gYPEACcFNvkbK92zRZKVyckFKTxdv4IBZq4_nDHipZ-1VN5Mv7TJnE_bJEqCR4EJHs6OpgAqW0E2Z4PhHg6TS_Qsm_15Z3M7jvmo3qrXjJuu8lBddxaIXBGGhJOmI2bwDdzNA0QUHZECW7IvYBPwiCTWJufAZjk0l8U1pN2vp8arskiOtzFMEVV_YjIy675VwCuSfGv76LRx3bE6-CA_BXXjbnvW-0e5mIt6MHix80Has2LHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
