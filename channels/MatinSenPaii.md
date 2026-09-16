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
<img src="https://cdn1.telesco.pe/file/nRh8CdBs7ZcD8qY6r8HphdsRCzOQYScWYfuP2sDzXi_SZw8d8bwlwguqnJEQitUJe4Gd96HW6tJ8YrF3JWadogc1WUneonIBeIU8g8cvZj_ldlnqCfaEVaiqpGTOryDpBFdUqXKKmjwG4jaS6ih0d0S_ci246D_6f6b-ZdPD1ZbCpRub1LxyA6PSeLerBC96l4iKpsz4Qrz4EmDFn8rcTppkxiLtrOkXgsJuCRCcjcdjyldhS5V1oKvuU1Vf19Gf-oz__AKjDZToU9URAbKN_QVadh1edmMZjU6DGyHwEEVsfAezDiMWCwErDGFjuZ6ZvS1rjRmMXCh5xYhFLVY07A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FISAJx-l7Ghe1RPYuC6Eq9kGG1jTBPHkDkX246Hu8fbzHUSlqh_U0HHP9JdcLloFfgzRslw9ImXTGULx_1H7bfRTIF8YGQeipjDvaJAdQHySw_dzkpWVoI2Ia2hHXkGFwMTkzqu02NlYugfmA5zcN6Zcm6fAfI4SLdRm0sMRMI5ce1CeZE0gjRd1oiAB4_sRu0FuBf7tLXxKAuiQA5vhswgVU3fnN_AhNvx7wTKRObyW4QG2aXEGg3jIFx9iMKoYGZa3_BiHnx82T4lA93XV3jan6CPFT1Mq2uhlqRQgvQ8DoR6lm37ftHn0ekGlLnIyHWw8y1Cj2BnRmv5U40wnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFdMFmBg7V4io0Crb0HreJvlXrcdtsCuaII3y1QFhO40n25AOUhkbfV78HzYFXA5qvAXG0NM7Y13503irsuQdJyA0jXIAyTa-_IqanoEix5JwaMFYiED3UpK5oE38Sq9TBCS4grkyL1-X8FYnKJ_ZIbwK3wfWlCTNPSJEu47p4VlKeY19aSN0MYWa7f3cFT2FWIlZntf82lw_eUDMLMoje2_sYgIjmyKa6-7tPebyQz7aDgV8Nd8t-k9dZ6U_VDcxkknKVHy2NHpCCuTMfudb4nG6vpl2FtFrqYuaHy-yghAvebGAAhagXZauwN9mF6dXXrArR6_wGu-3bku5lroow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-vVtFzuwBgbxNCSkiKYiYB3J610CuDHlhHpSFKS2_QqXIc-enR7UXO0fLn8rwZQzu66NnkvdR-h1YCjtKqjqxq2JDUqZ645zLZQbVM9MDX7M1IozCpTBbZcosJAAjTmEiF9MTNcEXUEC9lSr7Tm19DMj_JBCwD8ojvXrIovZHDa1UgeqpS5-C1DiytKSOXAzNvOaAw5SIBOIC2I6DHw1JbUbsrYSm6e5oCgqrsCR7viZec9OwNXKXik2x94b89x-DG9HgnVNSYHKyiZP1D5Lc8xzklpyQtasOB2hTW7tnoP2fd0YHDq77mzMYMnTghk_it0NIqZuTIgh5d8iNJp3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ohFdT6YGgHSFGDzSz6Mrk4zRzSdYbVJjGQ68p9AR4zDW-LuxiXoFv-kLVNqZv3XIP4yhQO2284FVy1cZ5FfuuWr19LjKkT0vniA9IOunfZf9YzYot5djpcQ2REFJU--GAlirTKNYmu8sNJ7dFfjvZAyWfbkaAkyyogZQDjyrPbCLe0J2ucORYZRp6qGLfBF2MTv8KlA4yWlP-q9ijyisFfG70GkQ2geFlwdH-1ewgqn_MW7A1qx4NSyG42s274JfjTUGcTdeJjSAAvGGyRLc2EMNPmMjjtg_3O--F0Edaanvd2MXfIb7H_aH-fkU7TZ477AwYNiHeYC2sywoL4PM2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ooBS9-5IoVc7dT4DEMrw_I5r6ijrjvyikXf2P3LoOqW9XGzS-4m4HbUCiY4hASGrZG75R6WNh4FIe2F3Uo0unDW39uNpyePBeoekdkdHA_fSP44iJ98Hz4yKXtA8QKsKE_UHjGSEdMnfCXUBGfnoPKRwPWLOPIQna4phd-XmZRyiXSS8IE_f7Y3cgano7xqki2h7dvhzAjLgRX-OgOKfd1GoqZg9oQhFKpRoMZ6-S69uBIL0ywQi-UdcL9SVEBkudI8YNEDtpGZnSvHB618dkhkwlDBfMyssUNgaLy7_oqsOKj3xf9avaFoUtB2S-f0oGpxiG3Gta_NfSPYYmW8EUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q66HHV9qC3Zw2d_w-O3R7rWOSWfSMPwGJaGelShV_p3LC3BudYo_p0y3AQljBH4CVag3IdQ4-9SbeqYqyZWH_zD0-RLrzOjdKcXrf9pUTJ4STHhjIpSg6dCL-7ywabn_chlkCQ6PNlROxgIlag9tlTKvkE2s-vE3JH5zxJP2BNeDuQTR_a9F-9PCZFErqBhXKMHqGFRBih_3l9qT9Q89EZZSBK6xtp8oA7kZsT8UiT2xcZ_L8jjVSZI6X1jSRzfV9jdq6wK3wVTbzUBM_mdc8mOSZKvAwxpvPQ1WqRR4ijNZequR-mOpqJr9yaQpIP1_BlxBWsPnoZAQNo4Rr6EJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyKVq0_4EcddyJ2pxPps-KY6GoaLQ7-9qmcZ12fyT10ZuYYhAxqqsMCnlfkRPyfU_aVTm1n0kbH67vLL6lqeikQ2ar-znQ8j8Kk1SsYsiGwK7o2JxeNizYu29E3w74fmGGcU478u9M8EdS02IXjIIJWDLnIwe3Rbjpzi9AKVL3PG4OxsS_JrX910qpBrfK1S27Jg6h9ZX-hoStpgdX5aK7YOw07NMzlMbtjuN6Ofs9KWmrIEaTkGP38JjwwKYxfFP8NXayPPUdg5Xrbn1YWWIDOXnJcQb_WBYsesrMbZguYu248W90TTaAIdWClA_hEwKbDO30asRzyHkv_hu2BfKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ud-mlVxuJ0QhEAIUSNQXxoLasY_V39R-rNOoss3nUc1W-I8gLOJTXM6wKSq_RrPJpU3b1x_c7a1ZffP50Vr_acrZJ_OrRBwR-pgyZYQR0bdas5lIKg2DA1fXvzxh2phFXJ6jLyJvALFYKrROAR0FSzWQcRfUFbvrxjuf6LTzXSm8H1lQ_Iqi7iz9SoGpA3m-7w1KfN2XFJRSyX9aRkCttOcGjSW6irNljyTgMJOk88yW77v7z03nTQvjAjF_Rem91w37NxsClS_lBoPm-uBm7dqehxODooPQA-m0Nl_IXTedPFDBJP2P3YfiJF6nX3Ttq3cMDssaNI0WYqgiQp9Fhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=JzE0_RTZGAb73tWEbMEh9c1WwricbJsACnk7wfVG5sizvwepL6T2QNPAK1DEpo907tT7QpOtntFIYoQF47T_iBWVht9YGsz0LmImEv-OHwLi9gc4UJ-ku9hLePpgXgQ7ZpnoA7lqfJV48I_X5tHRi1aXw4bp_W6-Xsvl7S_aoMila8qusmAHlUwzXvxUUIsmwF6mkXbPlog3BQSE6CbPOCleAppQRmVsGsNlUrRimJlvPX3PtBps6QAKyxI-dA8TC0cCvE7WI8aEu9k5vjl2k4ufuG2cvzKI8Ml_2yPPh-V8Xx_zAwPf52zijwJo6ju-onqJwVZmZGL8524o5Emn1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=JzE0_RTZGAb73tWEbMEh9c1WwricbJsACnk7wfVG5sizvwepL6T2QNPAK1DEpo907tT7QpOtntFIYoQF47T_iBWVht9YGsz0LmImEv-OHwLi9gc4UJ-ku9hLePpgXgQ7ZpnoA7lqfJV48I_X5tHRi1aXw4bp_W6-Xsvl7S_aoMila8qusmAHlUwzXvxUUIsmwF6mkXbPlog3BQSE6CbPOCleAppQRmVsGsNlUrRimJlvPX3PtBps6QAKyxI-dA8TC0cCvE7WI8aEu9k5vjl2k4ufuG2cvzKI8Ml_2yPPh-V8Xx_zAwPf52zijwJo6ju-onqJwVZmZGL8524o5Emn1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hcPLoPRmnuR-HA_tlkrs2ujZaezeU2ZTLfEX3kyH69xyabMm-f3CYTu80gG-KnKk1mOtUCJQPxx7n_aCihSPc3VDPlpv4IG7nSl3oGLl3uVWJGfLSELUuENl-A9EpOXkyVixCtbJcHc-SVPFsDialc2oReikD0aVRzrm-MydgOST-751gEd6yx_Cy_6GwnnPB0MhvnWh0VLdNEnNizM-APf8sYBMaA7vV3-BRy7PMgm-Q-A4fBdbuOVN_RXXF2VtcDfqtJW0UaElEJU0JhEpJG94Y6PaRi2xvX0zGqTMDkCI3uTQps2Vl8YNHFqij2lm5s-XMvANjsWKk2XK69ZjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AN8oI2FZCQNrDNxjnvdQyQZzwdNxLkKW5cs7GkywofBBf0IXIlzr4avk3CnhP7N_Wfxw634XdoguCL3Vt8e-9l8v0QPK5acMCmIPNqZMqJFs3Rnx6AQ1Tj1YM7GUYr7wFYqzCfJH46g2IdDGA87uuZRi8JWaopr4Hli0CtX2OdpOscqOtSwdvn4QCD9oLjt0m-jbZcOHXoaCXKGKyslGXbIfQKtTyXCgHUcnz0HgF3VzaCVUKXAJKY1h05ce-Utqy2_x7ytfRAYs5X2lzmpAk4qFONpWDyAx12CjdN8rWZ6LlriwsWAEDaRApeAo9YyPJ28oVvkwwFLJgn9V8hLTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzQ5Jo8U2ths2aoLoG1I0Qvp1t2n3yHGqKAPCZUwLUjeNAzYNyXiQEYW2jCF6IskQIlOcEbFYgqnJvu-bt1TEumE6hOCgK-_O-CruCDHbs6akyOyXzjArMMHmMHn6OUsKOHBw-p9LoCVjZlzDMhFr9pvAR0Om99ezWrjtsYuDUWuHRf6i4acbFEB-3U49BzVKc8S5R8M49QocimVvwiJ9qWDre9KtEyknsgDjFRP14zhAMYNKqzTi8OdOqtvUQtrW-8h5lGWixKUvh2p2cvohbG7swOgzNnLaNSkbrd2OMLvhVtwKLeRNrcwg57qTCdrxQ7pBEImQ51eCIIsEyv3hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=KQ9PaRfkmEVDq9LnApziiw2RqmMCnWNuhsIX_vmwNBcGrkXDA1v8cUosNLZ0UvgSBW7TIOUw9PbwK8Mh_jaomcwpVBPj1GQwyaKA0VFsERwsrK4EMVDgXpzLNERF227YRlbKeu2-6OZerFnk08huZPx1_bi9xiK8Irhnhs7V_9eohzqB9mxUJ6Q-szJsTL-Gm2Q5Klz8mu8mHFfjNAmsjz7IJvh9rYkt1vFqBFbuMw-6HLb9TXvxtcr7l-gVUS_eakr6a_gbkUGXqIU2BolrmeB-IIm_VenqcBKJJY37Jw2b72VhhEqt34l_kcQ8WJfo7oHLQr1QCxrtWgWqXZUp_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=KQ9PaRfkmEVDq9LnApziiw2RqmMCnWNuhsIX_vmwNBcGrkXDA1v8cUosNLZ0UvgSBW7TIOUw9PbwK8Mh_jaomcwpVBPj1GQwyaKA0VFsERwsrK4EMVDgXpzLNERF227YRlbKeu2-6OZerFnk08huZPx1_bi9xiK8Irhnhs7V_9eohzqB9mxUJ6Q-szJsTL-Gm2Q5Klz8mu8mHFfjNAmsjz7IJvh9rYkt1vFqBFbuMw-6HLb9TXvxtcr7l-gVUS_eakr6a_gbkUGXqIU2BolrmeB-IIm_VenqcBKJJY37Jw2b72VhhEqt34l_kcQ8WJfo7oHLQr1QCxrtWgWqXZUp_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eELcmFJk3R0qPM9MKaCHEdlZTTC9sPmT4bBaWN5P3IRkrzTz8DmRFpzxdMojY3Tb4r0Gj2yV_THK7bCrsuW3cHaUM-7o11mSz6XBehBqGafTJRu8HcmlpkZCQ_BDM9Ymk0NuAaHmwJ1LLTewo_L3gteNMXh86oVgywbO_iw1SHva0OyLoJCfvDHb2frCC1BUDhxSCIfU3Z6gmDV2aCmGNnTsSg2oTthrlVWI7rUe6wkUmqMNZhptS_hKQMXkS99XLr7LQYTvYyPjvLBamzWVNsQx0DfPU1tLU75BeYJg6vnc-LTgXNo1E4dL2nPHtSa3QzJTh50Eyd6O7rzaGY2Iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pz5hb39hj32hdoc-2ix3FqsWRZGfGkppAmXYtQiiA0lfNHK_FOQ-Uk4b8c--uR1egmVLK9kqcHYMZubOY2pjuvkxk7Zk78KYCRmbYtm_NBgY1wInhWpwPtCkhBm9_5nE-GgD_w5m1LXtl_j0hSYGUzH7nxO_qNaS3TymX1kanzJfFI0-5O8ICmaqHsMsSc5YuaYKo0_auJFXAZbGbuCfEc4G8UGAkBFmiy9C13e6lZhk2JOcY03pSs5EugbBjU67Hr2iwlDN3Oje0bygfOpGBr-6MWMkkNuzyJnA2g2EJkT7il1CRSo2gd3ME0_5wvAq-B5iZklLoHdTIKr1ms6dqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ydp7kItR1n3ZLj9pvSWzsNEJzqaIhi_CsYTHFze74dQWEAd8ufgGUznBJZySufEn7H-tGSNB_YrQAAxAK9wF3dI_Jc4irw43RXbchOcJJiLfA0I1xHbv_kQ7RvECFY5K-h7RnT5Q-yUDaeqa40CzwPYGMC3kxK35D9AWwZ0qQGkkHB4ynYTrvJlkxYWXeHOtuU5eHC5pFMJMPo0pSM90wKT7UkTco-NhtWlulJEP0bvrkx-GA-dBhGOoFz9KbeiZ6TUW0AEsioB8XeJ4E2wNI97kUEeC_K8irM_EMYpjPpKVhyhnwJ8e-KL-0h2LSPpIBIAXypruT5DcCDm4RikwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RwzWOhXWybsj9w4DDXtsuQtrD5zjyoQYILD0wUmSJKeR5v3KRApbHPtSdg0rxEmQb8udVFjAga5epIAm8wdoeyf6zgczvMFMdLiy3cUUXVEqUzi7zzZvLsKOEllcjdyCZeSa0Kbk00205GeOkQGa35hAz63EbaFPK-66gF-XVGMKMQyi9-k9axkxvHRMDwN-DWonpynhR6ArZSO8B0iLnRqJ0C9V2X5ss_JBi-5Z0vVhUbba8kbmB3ZvPahNKNdrN7XsHz60edunUNK_4tGySwRTPV2RqX1JbBzoHdS7cE9aT7ltDnnv2v7hXuTuDD0ZJwmCVbrPAokM4Uvyhr8PLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxQB2HG04NiQgupRFOoxfTWZGr9G8PnOBTeRN-hFqPf5aQ02B-HrJXq3nMbHE7tbTDUQ_xS1fCCcMlgbfTi7ILDUZ5zPiBWHSM93-vwcEJA4PjEiGGOWc3jcO-hv2iW4QqFnWDRGymipfKoItz4XT6AyiehYgSlh_NlHN4PcHoffUHVVc-x9BMIINqT4k33oVmbdC3ENmuJOcPEer7Utwy4IVFXYabZWCuQbPSsUBuD2mP3J1lK8nU9-NlAtaGgvnV-vnGDsYA_5VKsMLMQVbSBCWYvA8rh5dUzCdAF9IVHeCJrB9lbvJNCJRYd3PePfPkQCF8fJPqz1gW8kdDzUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jYSK_bzaCuQ0NFqd2zOmsQTLrGtxZEQAY7tvCaj8mFwUHutikZU7ZpjBpButgMUk4rmclBUO0y-pPC8b4zFaHTKfnGKRT5GSMza89hgIIZfCX6O-fP1kUsd24KR5CmZ40JLDYOScjXHtYmgmlKF6QaqEE1lLWKN1QrxBGtZnxKBj2_6yTWPk0o-KaH9rgzcdWhD5uakUawk2iYkjeBp-csxX72ENlrMixX8p5n4RiWMByWcV7qLDzXOcBvKfGbw-3fErwkWozRaMK7J9MyWri0vFyrVM3avcSNzs6p_W6a2jSgvcg6XwLjraBuNrXQd3WsOb2ub41TJnosaA1CeMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=auv7XT_-qKkhuSNB1PoOjMW3Na-qUfHsqx-xRB4_Ad6eK-esf7lPrBb_3SZdtK3soqUk7ALhAJ7iB0a2g0r88a8EOa9E8EFxgszSkhHUgsu-bWkWn3m2Vr9gZU_OnYx9LCpkj6LpaHuf7tvEhhjlaC3V_i3kzYv_l0gteDLtCR99hfHHfzpoXXyAds1bWZLUuVZtQm_gxku_tgyc7D3AShmGr9C9SiT2tu088QbLyR8cW9D_0dODru7d_4LGVnFsPDAiQhPYEplyyZeJpmUa5a0zankGvVM7zarGDngaPgQN7msl9z5yFwyS-N-M02SJw26DSJ-4ljUw3rQqPGHffg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=auv7XT_-qKkhuSNB1PoOjMW3Na-qUfHsqx-xRB4_Ad6eK-esf7lPrBb_3SZdtK3soqUk7ALhAJ7iB0a2g0r88a8EOa9E8EFxgszSkhHUgsu-bWkWn3m2Vr9gZU_OnYx9LCpkj6LpaHuf7tvEhhjlaC3V_i3kzYv_l0gteDLtCR99hfHHfzpoXXyAds1bWZLUuVZtQm_gxku_tgyc7D3AShmGr9C9SiT2tu088QbLyR8cW9D_0dODru7d_4LGVnFsPDAiQhPYEplyyZeJpmUa5a0zankGvVM7zarGDngaPgQN7msl9z5yFwyS-N-M02SJw26DSJ-4ljUw3rQqPGHffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KyWpLFiRk3D-wl_hIwlW2eAPqJJoKa-SHeuey58G9fXOhpY8HpVPfxQlWQ3lcJhCe-AqI8R2nEW0Y18VqfcCHJR6nE-NCChWJwNP6KPtAgbXHEDo-odj93bZiHUnagVeHSkDD32klRBxRKovdPdycDyZzV8faZRiQBEmV4vCRu070PvoqpUWo-6CqmzJpkTZ0HmxBYMXHWZFZh42429ujo7aN0dGxMe_iLNnx6nWISE0yA-QJC4SBTbGgY5xB4m4fr8DPa9i7Nm9T-hFXhbxTeh298kM3oLEJMhiEH78H-jSM2WKHlyBdnckBXYUw1MMRZTkLdrrX2wVtVSTqj_M1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lx6fiyIY-kEzpoFRlj9RWtkCLmE1IvoK2KOJRSGsRB41-ASiQXrFSaXcT5IifPswZiiIQJomUp3-23n7gMPiGJDPKUnmcaxNn-XwsdlJa8eLACSaGU050ynnhvB4U-k0JbFW7xF_EDfbYVYbyiGDJgG3piOPH9s3IOUySlwNxSnrEPdPgVm23oJETdM6atFdd2a4k8RHYnQtUlaNXMFoqV4FrQsSI8kW2di0UEBH2OhdnXHjcnO3RgQb5JG1VZEFgkGVSvwH-Apjws0fjV_Z_bKZR297kID6L2Cw7GJgC_qOUblCAYZlNFEFJz0Mwlxp1T7Mpx99bRRZySYbTz-Z3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pNULFncHDzGrXG5AgVORp1ddO3yJpi3cQT7Q-RCA-Paaq5DkrJHww8Sx0nZWFJPBQyACmUR2Wev3h7eNurpX9SyRZRPFRKVZS8VEG4wocBmUg26wkbdyLqpGaV_eSwwuxVYujgoW6nQoFMOErpgcx691trdVWckDQeQlVhXKUQSJu_sWDQvKhYCz4nzbJW7Fg0h95iqeU8RuZKE9GpG7QBL6g4ZvlMo-G5z7hMSpCygXykRP-6oSuo8U2FiKxoCuqCjwMaL5huIWRqcXWNKtIwMoM2e-4WVGvcqv_Szg4bb30pNYai82Nn3i-jPnGVuN4bz4mGhgz1_4sARZ8BAtjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJAToEfYhQGoUTVHELhJ5OLk12kMcGKskc3C_baQOF0QzE7_zZikjPUKhfYhHcKgW4XVoih1pfWZnxD2v_ZUSsGz0D5ZaOyGes7TyVLVYBQnRgopF83yM4V1bHYWpT7lYaujpqV4RyPSaBUOBWT126QFRuxX2DQV1eEYYkuhO7XV5nSfyGWo_-WmLHUQlko_P9ElHjpWTxveWrgRUP52YaHbc71MsrGOzTun8EwKcSMoZr1ya36wIjn0AIzt1m8bc5rncGaQY1id82334OROcE0ooRCWkY0XFffs5DLRkim71C3m-Ccd2c8YppPTLSrVBf9Mk04RuVbcalCP4QcJAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-DcpiUt072sO1Ia41YqfJqWcGUX5kShAFL1Vd7OCNHFPviGTj_ieg0ut28WkM2aKOq7rTr7uK5e9d6BGDNP_iE9r1gL6pheVOJG5rRayiXaz1rMGJDFTOCnB3hFO77Ji0-jvTGNibvuKnmwltUPmz1_vyaYFmWDGOYqoctBTC4ICFLOrqjPxIYLfdX1aaq84GiLL_g9koZ7fL_YfGxMsSzoPSPb6hSnQtZ2VfZ7p-h5nyHF2gWcyxXicukwIvFHwPgQlUAQ2EnvrZ9w5R1g9DDCP6QUTQhB21Gv3fWhMrAmHBKGIa376IyZ8-8QFmBbsmrc-2b5Q_c2kl5A_17pqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EMGfLc-7tHQ7ZW374xo0DBWTrxBKQ2gxLeyopecNO5j_4lWZKoplzAG8lMentTXFEZn2tkQWMMEC2zcK-xqztzJIanN4_ZQrHifB8G_487JT_AUkcZQ8Gklfwx1DKc_Po3A-wULzHKKJ9Mz909Zjweb8vm9KZNqgvXw0og0U6lX3jRBFzkgaSnvteC7bZjWdgiLvgbu41nl8WIdBp8cyB61GoP71a1L4e4E2qLem-Wmscoz3O5Sr_kmaCSbWrhghvlM1z9znGpG_JyeuP2qDL2NfvTIqlt8j-qSDQCPGasLZVmmLdW_-AbE2-vPDPSXX0u90S0MI7KrHGcoPz8niAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PSEaFrqFbE6b0lv0pHCxnh5e2710X38hM9IMIE2ychmVoOoRcpAkRHaLLkPE58mM4J8QcCPeq3AZLlVNEcCI5L0-s_nor4PfOaeIcnH-wohM9joAj36uNFPfkMK-VT6cXN9aExivSXcPY95v2Xq5OGL1ffQW8XYTij-LI6cMmSMCfoNj_NJ3sj3y6tzotv4fB8ClWozsQDjSjOhyyzvTJd0TIVAZ8_OuktESJuPw_7Ji06i8bH5QqXj1r4Jq4hOe0DnusBO5m-4IC1daJ8Op5bLPcoR33kSHTcX8L7wv_hQr23qBgZcWxsAvNHLtRHlrZrNcLAzmbXlFaq3h8NN6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XzSSzKItQrHsALlcf0cfFuqS9GzttMbJ1E58pwirfopKLiPaLyzAfTk8IQ91xeEzOLBQY9hl-wnEW6zwTYePN8OpFiQ8wqbZ6qWbCapfXZIMqfTJOo1u119dp3lPDzQgS_IUT6W86mhEJAcRkJ1VkW8hXfikA1mEAA4n7efcxPYVw8I3eVnLH5FBn4og0ChuS4hX4A3VtJVoojRvhx0FkMbfcLAmpRFniX-9K35M8yQmYP3YUQjbTZW6JWnCzxPtiAUDYX-rX1G0QaOMagF-q-146gqOuj-0q7-Hnxj0eVSp251ueJP5noZuzoJmkIZi6aGsBSFDujmHCBJVtxoDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=UiJDo8fMrFsjinXRwYM5xlfjT5hDOqWdTTKlaCoxCq7cilvaaG1PMjiyvHtLO56CD4ljxYvUbnLY5JpWcgUa1v9-S1BW0CX9tvoglrW3vYJ-ueOnreR6TXzNIj_S_JhFbduw9yqE1wsOXEliL97hddrXmTR2KDO37SIoRr-GImILml31OCRI-pFIXz-puuFmkdfhlnd0MAMimdWh1uP-_hHqXREiKMf9qHsNtODykakIbviAKNaVPJfcM8KcNy1-YNSaG_cq4PS5K0nnsA-tXCgBiLMOqeQNzR66zhrbCPwwB6gs3AqImx9GNJQFmvomN7NRPkE-XiMXtPJ_Sn9L-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=UiJDo8fMrFsjinXRwYM5xlfjT5hDOqWdTTKlaCoxCq7cilvaaG1PMjiyvHtLO56CD4ljxYvUbnLY5JpWcgUa1v9-S1BW0CX9tvoglrW3vYJ-ueOnreR6TXzNIj_S_JhFbduw9yqE1wsOXEliL97hddrXmTR2KDO37SIoRr-GImILml31OCRI-pFIXz-puuFmkdfhlnd0MAMimdWh1uP-_hHqXREiKMf9qHsNtODykakIbviAKNaVPJfcM8KcNy1-YNSaG_cq4PS5K0nnsA-tXCgBiLMOqeQNzR66zhrbCPwwB6gs3AqImx9GNJQFmvomN7NRPkE-XiMXtPJ_Sn9L-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CESwtchUGANfynJw-WBso7OR3OQyFOsbrFhUyCiab1g5xSq80yFLHVvDqR-fwdzNUbxT299DDJouAKb05R5AkFah6oCs2s0FINm2XDo-75cNjyNX1CCoR05-0os--i5eQBsKJcabpgQ9-FFhVJ8-F-Ig0hS2V203lAsBXFHk_oGryFf2dzVN4VrLwBNAzinfJ-_fJNSzLg6bBMMHRNX4Wsj0c2ouiUU_kedULL4XAdELQ07rE4w4jlPd58QHYDVmVX3s9ujQCk6_wyqVBu7SU1-OAj5WSOuCD-KPiEC5eBh8PjPV9HcFZoG99RDOGtQlfwoV_gXGbFfCXN_sgbKM6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XuyxqudJ0C25cjCV6CaDQzrZ5PSL_rltEUnzFtWyycXU_x6wa8NLVJXQonLFe6IKdSk4ukXA8zAbeXPGSzJqQ26B-kiOj_49JXNuzCcVJ7qCeZ-s8jayxosvYJzDaIK3hpMwHK6bGEPeS6_pj9Ll_h-ec5Hz6C-gxyBgP3qSeuK2Ir9HeBBc-vUlj6iD16RZjIS3TmgN0g8D6BavtFkReeVN09IjIwYTlO50TIiAKt6bErArO0X_AnXi02A2tZYA4rPZuJ5QtSDp550_xfhhmgwJjLfHiWiZPySL_1rFIUfz_s5oZZqelDwGTfEEHHgBmaAoac-j0492M7ir-3KKKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjSryEvhMotTC3gsZ85kvjqwP2PJ7CL95lmNwle5FGQgSevxaR0t733GZNwGo_epvjJZXt0qF4IR3zUGZZbvW4UDLVZDFm7c04IuUJh2kBMmBcr_F5TlIFuudkGWmUvq2qx7e6yrgSVykfPT47EKgRJ7eRt70bGf79NxtexJNoBhwOhqbO9mgmMM6TOv6FaP2QoIh2b2TB5qcLNDdxOesliX4_S2vsa5ZlsNb649cQDciUU-fiIPXVjOG6tnJUsY-2dGKqODbf0rfX5QYY3eqPO_nNoKtI2bxzQYULpz5GALCgSdJ6UEQycVdtH68BIv5g8xiSiV5S5aZnOdVD2wTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOAR_3JXcwA6iwuEzumQyzppQ9PJU-o23zyA8RJvtWZFVAa9XC_HNT7yiEirg6XXYPdZhPTa5Ev7VFJ2GRFsNKe0_0ssKqznL8IFLnzDj-rEy8Zc7B7cXrHfwH3L2hksLUWhIZKMlE5KG72gB80UMsgtFdSxUr6COT-93ajQDAceIScoSKQWrgo07Zduvj2hrRt9H9NiCVjWsiWKckAeb41AH5WN97YP0_FRJVRiSnay-x-GE3CwdszQ8JsJz2b_Tm8nqimsTBbUxyUKFIJdBpxpZ_IZZiW5TmqcOJamh1vjgSCf0pvNTzzPNC0nDwWQRWPrNrnXNxXgDLhVbzMlPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hIzFPmaOhi2KWhhf4kNZ3_i_4SMFTplVOS1FDT9whsoExVBvvQloJ0sT-4l9GsvuQVl-OIvVzvBPObYP7eFKPLVg9I3zRtPhTU_dIcfZ9S27o8ZaVvRqhEUku1ydmNOcrkF-xYQ0gdhj8ti6WBG7VIZHDRdmjWgekjEVYt2-3Jt2WA2K3yN-u_oFwOPUbWDis4VMvraark3YJKITDguXjb1UIAH3-PYi9lynHJbAXQjbBekQt2TYYsA0T0RAmZ5m468U2e3u1TGESnj087lxhVD2ikY946hu0E_VPyn00qHb1OdhJLCuDn3ZlLYtQW3qqfEgoRcMuRQ8xSSnfbQRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjjG7dzXqchNaTUa4aTik7BUSyftT0WFWgUorJJJ95u0o1pamy9vLM8EUQMFbQEHBhLXZQROsbNXh6bpzioMAu2TibS87UZGHd1hF1jQnkz4EbBSXtdnNbTFY5mvRsmT29COknEXHwMz7RCtcVYTnA5xFaCogjcHUo13rBTMSGciu-Sj2_cTk_xtNQ6p045ln7WVLO1ZtHVDHFRGUsMMBOtyPYUXH7Gys7n5S3mK010vGaV8tfWtIrTWX8mgaMQvGmLWWUWSFhSDHTCyC5OM5NQSfUMBGX3TzZqIBm91JveHcKZaQaMnXRCpN_x6XzqCR4yhx7ldCMAKqROwLFmYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FWk1Qzb1IfKzFI-j30ENvdAOMWc0czQsnYSOZQAMl6_xGyYFHaDQl5SjzLpqlvystKY3ZVCBwJdQLitTQYjKvkjzZ9Dv1sU7tadEEV-l9pxITaOeoUmYwP6vZvVneZnOcr2p1EhPrEiqTZXtvlHAd2skrR0jaPbRLKe5IC9czLKM1gigwRvKe7ArR0eZMsG2OrzydSeYWcSZApdOmziBGx-KgD0Dnc30dGYmCxo_NudPYkpckqiyogDQKYgNB11A3nUNfUT5zzUeIGZiCtqWUZx-qWnrPenY9lWgKSpnHQVOCz_ddzYIK55pYsYTzO_zSzbVViJ2mOifc-Sj6eQSkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dIRgaEJJTUA7p2sOTYBhQLVBsnHewdSJ6sJ1V2v6P6Q4_dhsfQ-kwjdC0DoQxYxn_xDZeje596rA95l8vIV46LdYN3Kuw_EuXOBUQ3yNq8wOlIQDgbVccyqGc9-z6u7tz-X8etI0rsdVZh8DNsmqjDPEKws0aTvxAvNXNtg_ga06z7NWvG_lWXLszXicQmhFHT08-_78XiAYZG4f8GuAmydE40_B6qdFt-PKteUmVMBV5lWbWgoE8dhT_WeioRSq-Ckl1d8b-5TjY_MzeYfO-r67RI7nCd-ytHDb-jA2o7kCULDKWrXz0REMfXP8kVPgrtFW2tvhGYcVz35Ktlf04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ydz1eOmW2_jNcxwWQUIhKstWtY-xXGJiH63voG2mxdgk1-g0mi3Px120Jbm_mAedR5ebqmeEXvlgspd0eBHzVsdN2dug3pZynEo20Lq1nAz8EZckHSrqPIpOMcOiZTUOLM9utvHIyYXEvJrUoZmw1btmd_fFhOp98XnAsKfRUfV_pUzPtvMdHvEJRVtbCTgBfA7KZwF4-s0O5IzHY6QbEDNXNrcZFtoS9O38jc2_WQ4nf2BQT2QdZUde765vtUZmyzyjk35Q2oaC1oEUlqUfUDN7y8T2qdd7hPiQGE5BfNRy7dwStVEgM4VHzXdoyeV28a9NpyJzCCCHZxzfaFTnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/liwxjrxbzVfQn6xm8jqZF1thA7IIT4254WiIUfylxjeaH4cTQuQe2t2ApHX5Kr_GB8zMPWVUwpQD_bjezq2N098PRCAtN_dYCsgkhd88WpH3eDFW30tNxjDuykgALh7LASojOl3xjlMqq7XSEG8pJdIvNScoxnsqxwAlhnaPHMTJicv5oyQWQQEp-HGIFU5-5QDXLx4yPfVBz2i63EFow_k7IY58WEd9Ty_tZIr5aD1mY6RPqa82dTPvhN3zm4GkFrcl2eyzikDN2BBIBd-kZuIEWNhf7Iz7e_6D8Qht-DJessKkVfFo2FFXvFoMqT7-do-GwSGemGq1RxrASymwqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mAC7GpebyN79MOg4M12k-dT_yDkP6l9RzMRux2tuhK6ky-eyOIdZZ_PMsepp0K-px4VmT0u9ciWlxHsCezQl7ra65N9wluQ57hdx-2jPRwZrZjMYnvOSczz-8hRctDRllFsfxvcalzOIi-QpabfbP1jjOPbj0bw5txbCJQ83NUNzL01Ic2QBfKJQfIZGUtjkzoMYzObFMeM78KsAjxEezF-c8zrdR3DXg9s41vB0Q2XiJPQ8rb3QiPK1rFsg_pqHlzKvRTnwEqPNvAnCktsS-9YrSu9xrfEwcE9tJBc-wDhrUEWu8Y_CC0i6Kwf4jzOap2EabMBmsOyB-GjuIz698g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=hfH_uKh_cMbM29WGXR9_qf3RqImmjaUILV77tKrBJGdP29QS5Ec2NtQ-y0P1BkeoBY6cfl_B41-opyyDOLq7Lwa575wZMjcB3eYysq0xWjqQ1Tk93bMK3dZoNORMrJie3nGu80iSGnhW_9Oed4ifCH7XPrp_vZKZK_ZhzZ6tCQ_U0z8Q5yC-_cBVBc-PUykjq1CcQEzZ3Os2uDwzVdebQUUj3Jhca5GehFuP9ZYaozzqSG_ZOmQjNrpF-PKZjAoSuFR9IbIVD2r9HbpAv3j6JxLlZJ7zU8B_T5nT4FqjdtlmI3U6EUIEqFDdRj-mo1D76p6CTt1J-OyeOxeZkyW8ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=hfH_uKh_cMbM29WGXR9_qf3RqImmjaUILV77tKrBJGdP29QS5Ec2NtQ-y0P1BkeoBY6cfl_B41-opyyDOLq7Lwa575wZMjcB3eYysq0xWjqQ1Tk93bMK3dZoNORMrJie3nGu80iSGnhW_9Oed4ifCH7XPrp_vZKZK_ZhzZ6tCQ_U0z8Q5yC-_cBVBc-PUykjq1CcQEzZ3Os2uDwzVdebQUUj3Jhca5GehFuP9ZYaozzqSG_ZOmQjNrpF-PKZjAoSuFR9IbIVD2r9HbpAv3j6JxLlZJ7zU8B_T5nT4FqjdtlmI3U6EUIEqFDdRj-mo1D76p6CTt1J-OyeOxeZkyW8ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tNB9AwsxffqpKs9BiOd6xbaqf0iyfFlLcYvZU0cEhQAl8UpT-Y2qCwfaP5ZVfYKQMCxxKNu5A5wpwSR_t1ZD9i1Gbz7nGlUXp2gyDk92LG59d-HpbN7grOoMPm3oAV1Pl9eY86oeUEO_qYOoxQbneFN3m61GznE3iP-Dd7q4U3s4lNxHUI8vpP45-JSsKd4NY2-FFoCl6qdYqxNU9n7AGUw9vmsDoeKO_h43oVTwdeWBg80UKBZxS9ydvobMHikFhWniH42APn7ecaf9QPQig47k0Z-yYkBfs_WdJkR-HWZ1ftfOp614k4-IlxWi29qQa21w1cAAJxfvaNFIr3yuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uDqvr5X-1ThB_7A3Z6kX-o75D9eVw6zwRa1EO_OYgAhesJOpmCTqn0go86SfR74fVlLzofMpL-12n5FN1dCS2R_BEJEzVcJ29zeKxFyYlrvax7dBGa9T6S-CvfHc9cXZ1dnp0svRVp5ny4M0zHdyvqPntHHbSCVtLWVf1RFlm7AQDc3o-1rKHyRsERoDTIyE37pEevrFYJGkBaRHPnySUkOO5UFgyZwtT9ewbehjph3ufAGcYUXv_7xteljEPOdkFah7PEmFqiy5e1XFeytsjrXCKaPogNevJFjwYV_inxO6OPGHMe8GHfs6x5YhBjyX7Nojrxvlyt4TOKuyena3qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b4-rsXVUQ1laP90JwU_qxJNQZvkV1j3vPRhZUWf2aTA2jNmchJNxDUYtuOO4B01BPs1Kn6CWW8I1WntlnErib9wiMxHH_2lgpzxmJJDOjMWAVyF2jyg5rIsvvBYdlqVCZw9RRg7P_IpIGXOrjEUGBlN2PQ854rf-qRVQd7il-ihRDxE1uZV-jcST02glAf0r7GyKBJUhYGQO1AAyahV8FmQIfIW4sVNHT23-EVv9iKmIn01X8kzjupB4az4_uQi8XDuGcHw0nkCwe1yGEFC0Ofzxw0sjnYwfdouMf6Gd_iExBKQFzoFD7Uyf7zmPuwQE4FuvZ86myepPop1ZxRfG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KZimlU8_Rzr5H1F_rkfHvQ3uU3UbqFBZG84RQ0BsUstkzh5sFW7Mbakpi1pE31xO5Uyo5JnNHzZJ5j2qOSFiMSF4CyXytBI7T6XgF3YnyYj6daN0en4RSWS8oed1U71TsjjaBkRmQVnlxZ5nsO1aHYkQi1Imw35OrrtnuccesuApi8x8DGeL2iZ8hcMFD1XF0TOKXFu85lyqwpFMwjoZl6cp7vu1UR6kHJq206TirUD0cELrkyGaDmAFRWsNNNNvgBcMF6YnCBs6HslMim_RbdtGiXabdvTjH8h4QIrfQx0PyLuyBAG08ait6jaYhxi53ruOlghHGq6gSsoWVHH9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n7bpg85aU4fjTUo8NnmXh8kiKeJVr1H_fIGDdHk0PcHokkLFGaD7gES3C84_c8ht_og82cSVi3pYVXUHpLCKi30lGFIPvj3hICnLa_4teo7OtSA_37Q4ox1RVHtX_4LJ2RZiRKPWJ8auHGsxChUX0H72EKCL9swPisyACoPBzdC8qRTnnmdSecfcbWjWFn1UxqlDQjsYm9uE948UJKirXxiHnhI2rkGw6gY2qmS40aXGEloVtemoIcU5OF9myFQ_AQWS__NQkTxnsHrOfz86QyU4o9kbYZFHy9_0BwIas0cUnfSDjzH8nKE616Z9ZqzecKsJEqXmaiY1JrtTQxWowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RRrIKdelk6nHooFhqXriQvwhgo6jmlqz-2KIq2BRUDF6Se2O6sr9Vd6LRqg7vSA9YeUi8An4zXiA6OfPfgOnTl1PMQZEnsZeQcPgXPB-aneMbQiHP0nIs4TMAwOUYb0BqZdCmYAmCqsgiG0sBFmjZE2MMFoxQe8Yh9HuvKNVlQCmf4xrB-_po9VFDd7vTs5RYgaQNczjabNjVYTgiQYI11xHgCejDFoE0hspifBDqt6tF9url7auRZKB8TcsK28-7VM1o1vKYrgkXpDMk6LV-v7OEHMdKTwEjjC6pZMWFfarV_xTM3wkLZ3CcG0ufu46qF09kNMCWJV5BOVO9dDo8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aagCrQsmfODMMDQQzj2ik19f2Vj7ZF8IK0P0oEKhp-rbr6_xcxuCdoLB4ZMcVdAosAHK0zdJuYJZnpOTNmKclkjNYD4Ax_N5awq19cWyo665ymlc11j8NOiT7h-85CUfu10ZmBHHZW_ohRQqzTgMWJUhtch1zARnkHhnJG7YyoRDL0Z1fIBiayUjy9ACnKO23nwrQCkA8tfMrcjiPHaNsqhu0VIp6COMFX2nZIuzTSrI9KFrv0wtB5zDqBONu9EcA2MHzINPLTh40DUVmAU7hz71pULXCEhIh9ZSXxlA8ncFSw6XEhy_I5FtTsFfc9-R625JFxVPBLdDp-ZBwIaIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tbU7FpX_2FBWMAIsk-rBmKONz76xtGMkkEhvohttD7mEqBE3hYdJHxfTyAX_H91UAhwbs_5cEffqYccQO4oSAEPTNCeyC7LVDFrSpRl0nSAtnUj5neq2APAaSqT60uQeQmY_bc-N9gbz_KivpQ4qwUe1MUUB55flBMguuyP-ooNejcyobvMDldvQp7vCY9eEkfAlc4RH7y9drONZF1wTkMLWVVkOkXXF1NMvnYV_VAkL8iXXjWbUqlPoYSmD4S8q7uIJuTgyTSJlP1GMLPG6ics9tAJoxqlG-P7qetgGYCWcz429javP-NBs9AWREOmJ2ypCYVWvdFr6b_Dlq1aVJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qec8z22AoYIhS2RK9BRnP-UmDuLM_n3mPIsGpVwXjydq487RQpseErup8njoVAjsyKHH8eVY5_yCCB2DkSdVX9VecIHA4q1hM0JtvtuMZUA3bAsdWYwthazYaIAlkNZoospevjoVUp8o4QhhapDKNMoufKuSZG5ifQ_1UUK5nVEC3ccfXDNzKhkgRQj-6gYNjw6IxcB33P_8_ECv9ADWMAwFDio2sqc9lBLviCosX6d5c_udaC4xZcZuBg6u5GuxJyYOB4nk1-IK1y-G2MSJM3wYKqy4cPkQvgAM4Q5QAXO1mWzOutJJdPpqh-Gs6IPwlGn_sbn_doVRi9LcSr0zUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O4UMuSyV0pOJR8I3F9i5kkJglYMMOyWyRYwEzyw12w6G6aS_kYl0B2Z18J2_TJIRS9n1J5rMFRzKPqypnzuUpmOM-z7RoAVnwk8REOQSy4EPuOE6XOwChMdxEtMJPC0S6IhLFYx2H3Ld4_8KX-BomvYAuKTxkbfS4DBncJ6DPltPjQfLvCGTp40Ys7jfcFwYGcO5LMAHzVi1F3_dZ2Hd_dgDHL8qOLbKBuhjIhBmMNRj3b3efc123sxyDT_NhV5AtuZNQUrH1Cyx9ka2QxV2IHl0EkC_Dkq-4urZLdAp5v_8ABjBxEPrKo0phCFuZf2ksC6BHE0sp1sFGcjP1T9Khg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sqHaHNiHobFAb1K7Z2jcbtsOysNvrH-DiB_8ECL4FlVbQFXenb72s6nyjzzZuiAAK-AH2G9xEnhA6hzYnloqU-s9jp2c-3-BISjlaj2ktqTC4K4SucIphIFqBuW3f0NSUaUBTTYnFOQ5v901lWGxuPDR6w-1_XOPOSYA4yLZQvZo3b_pbfffpH0FsaiKVW7myKHCe2dmb-wz5JdsXgVWNxuEKL4JMwN7vmWdraxMgb6eykTg1DA-yyMxFjwRxrX088mKYmRpyv0IJEagjOuCEQCimK_xmpsrkT0oUJZHqEporYo1UnJV5L_etZPYWZ15iAPbolTt-Qij3L5CMiO9wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EUSu_te0-57sifjGMqPHBXZR6_5mf39IYavc5GWwHtqPvNDH5ILhviCZ6XxacAsAVsgAdIyJbm32-qgzJ_yS1efCyaO1wo15WIgE_owSX542wkc2G-tOvgF_4a9zkTlqPLmjO4KnXlr5dr9KeZsyC7EAVB7evxQHtRDyjvrX3Ti5yOD_gxRUSgLeLOCU8OLMPyeuXA7aermmMXInlAmldYlToT1LWDZn98yBifVjSOOW1ju6T4BgRfwaE059U59jkuvQ-b_YC3rDQmgcwWvUJ5N43XxZ5N5Q6q9Ooo2GciKOn6OFQ5RI5s1DEJIKOUM--Msj7-wVkxQMJIOl30SyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h4_YcpynYSi9V1V6U2MebCCzaGiElhS1tfgWWQwUK1B7eYlMHxW9ghdHmqtCNFTGgyEaU87ZBa1UeE6Xw0rIgCW0UQXX8jIBl4vxR7Yh2eSHWuCIds4fByf62Tw5-S_x66xCup2iIGdhY5FUnnGspSn1vriI64Uu4bjjh5h25LC1pDvi7OZ_FLk1O7Y_FSuWUHPFicAY38pjBYjLvnTRp5h8pcEV5Y29V59q7v0Ykvz5N9C0s07w9tCzPxCnyr2xVEz6zy2SLPk1ZqTP-ytOqY_2pc-d3hdVxEPkiZQBOAprxNNG8JwUsc3GNdsb5_61oman_NXgZWQt-RMASzAidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nVsRkXa2uwH_Cz77QZrhgQHpp-I59SZc76bHDpVLvQNUN_cuAy_j9d9G8iY2W2eNg8I-f7-J8FKrDTrFcKh6z55vY62cFdaXbcYLVtXOVtIlC-hiq3qDgXsBbIehscKNnI4tTHq746HtP1IJ-kqZ7_7COJ55kuQgT4zobWDIi4t8YM66NxSElcUiL3pMbg-0VXoMqgRlMLfeC2ZncPwTqPP3GLH7bAbZz7FLWzflCoqmRPBVdnVgidVqDIowWZY55IZMyJ36Iu0SHy2KzYpu5mvrXTm14XOS9mSR79kNvcOB3wraDqR0miQAKN5PW3KeGTzrHm28zv9Wai7d3yFg4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kprrl4-1_7sYarI66HGjjKgS-45WXyynV-zwgzX90cmsaOVVlE-DL9XYO11tiysUzhANUW9jL93bh0wqCsr35zYns7siDtA_TZST0nPy6ANp8gTi_2ThXNXq80GKypoHpb1GE4JbHFrppEmm_O7V4nVOqsoMFMSaWpMVpjAI9pfQbgjTIeeNnIR__nG85anIOOLpXazLa3Q5yzXMrqciQScCsOzcnMtmDQLtV6W8xU_EPTWeU7H4D-mbMSwWmtyr2tF9aQEB854FaR290Euqqdw6rIVlmOYCCmRncric2gvZXhKBnsuJFaVZyRVFZ6UtmFGaCeVRNVYTs8aH590qsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FTukSgmCy8lZyhHC0fBNcfl-w6V5BFPWpZPFO6MX80h7HclzGJKILdYRiyHrFtgtyJ4HvUT9msp20YZxQUBUJQNhShRZBe2pMkDab-qtkCLF0pP1_NA2W5YLXJ2OuCghG2mgXkA5Cm14aXA2za0P4S5yA-xNFsi8uIKHegVBMLGO3a8rWI5sKGbka0LllLd2fwy7yoHwmoXX4qKwmZuGtxLFowN3CYCzLQ7C21eoe2dyKNMN-leBClOPyaJH_9vzPB-9ZVFDnRkJFiex20W6-rAWhFdr99CVJbYavlWF2JFrbiBJIluLXX90iQI-DHNHwjBP5hKAMmZJeW9GSZLP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BMyXLV3fKMVLyB3ItoUxyNq0NotMa4PUpWNIRv6Pm2lYtMM1Jop3zjEQhm4qW_UFWvGYjVRcr6-Cb8KoYYeDXSZo4-t7fLL3cqL6KWjxkrtspG91oWzaazMWc-aGKcGeX6nhnS_XbPV_2KgEYNeRQiLS8Wczvq8JMgVnde1RNUuubkOM-W21nFW-M07KSMb0O-fqeN7d7uprEwa2TyIHK_YrB7eE8dlIFG6YQrIjDa1s1oLPJArYLmLo2zXuvXkDtBX9YMO5GZIwJjOchxBHihf0zVv2PjL1krTQIjkXaPCwOjVjc_JMUL4AVlL1SfJM8xjyGsp0MFgE8jlkgmjC7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yy1PT9AlnKz2UuF_v5S6okLYWyMFE9uF1HAJHpxXdl_X8yR9edEsmmGDb0e48AdFRix-EyS4BO78ig-uwm5UwPpc10yahKBRJw_5F2N6BOpIf5SEGJATsgoh3EFRc4FCYJN0V3TWpPuhkxtNpwyPh1L3ZXrQVoLVP3j5FmdSabiojwr5SciFjQWGOU1mwjNI79fXYZf-dYXEMtTFntG1JZ4uX7zYJOvynMx0TKEkwmzhOBPNzZFvRooJWrmYzYJVwSu2BHikoCSqP2W01k65ZVhuj5pE5LU2yYVReVUNBAsOd-3MNytpQUSWJtsKXFdD979C8DgQbMNMBt9NURfMdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HYSva88x4Ip4Jz1NsjjIHpfOsgCPuscB5nUGZp_9f4NM2RDhukOVUppU0LJrLuUNbYl6eIi89L2Pcb3nn7fuWjylfexCtLkYBHLxsKBqhkYPvEDn9UZBWxO6Qoi8QOZwB76mQEBmrFg-EwToTDkr1wsvuoeUS5THYxe9m6hhGKZXAEKU55iCmGC8XB-NCJpmPt3J4erc-y0sWFDcGVQZR_1uvnuyIEA8I-y_C-RQyrnqKbQPJPAC5Tu0eRie6zWD6esVPvISLI0i7RHh_gmU4TmPmOG0Y5C9VOK7O7f_UurB7HkaOJf2L4M3od3HS8rQj3FL6WUv0-Apol3RUEyH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sBydlovaSI4g4306CoEKxRdph1vmrT75bJJQh690NFuUgP76u379fGiTHiA6gAiZt71ngTCzFhosH6NCEw2OCjXz9EOKjHQmJsbxgHlo-LEnuC7eD8J6F-V3RMojyS7wSgMBU0hWOjZeIvkqwHSrYWzoqAnHWMh_Y5aqqqWZBqxo1oJ4uQbhdSIjTiisoLPpbYN56EB4TOopVjLkuVHc0VFcP1oVu-l1Bwtr3WfGmKJTs-zpSQgZS4JYgcnLSv6ww5dInb0CDGd73oZZtkHq2uGC7AhNBC3OXYIy0L5IUnKobxTQsbxWvu7pNuT1vSyfQ3Hmr80XFcFcirx2xZ9DUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YriVnOo3tj0l8tdUk4jlTMqMtpmzO_mwjmCh-uFs7NXwH-BcMZXTQyWA09LfsI5HJHmPkzFzT5Gkt8njvPecLmRGNBC8ZYP4zT1On1OO29O5kTB7oM6DbLjrwEhdy8RmkNNT9WSo12AABCwIgkSZ2aEYAoRkACU4Fnohn9jRwcrEAosvx53DqxPLZb0OXOe_VEziqOfWX1lEL_4R4Jskr4WtHdyzzksi4Evm57oZii_M7Ta4ckgRBR021jppFbLNxLJIhLaFUlk3yk9osmzWxPbtFwKIX_z47qgkfLHxb2oR0b2fPqQ44ZvxN-vkAZaeWTtuUKnq31T5UpCOYyyr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
