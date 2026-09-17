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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 07:40:32</div>
<hr>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwI_PkERPesTvF2AFgcKustIHXpN7eU40KNc2FD-jm8nMC937n2thzplMyNqovmdssY6RJxj2hvTZCHyLp48DWRK5fudUMapDJLr89WEVNCxiymD7kZd-dVHVfIQM4rPtBIqW-Y91QsBNuV8-YELK9P4be1w6P5JPr_-0kL7CMJcoVCtVT62BcLxP9gAxA-cC5R5lFVJA7Y3CIAktQPZXJczcIP8ZeXXQccvwBDAPn4A5dbrcMG2sTWTnS_0tol9No8swXbhfwVFlHjdnq0vwyKrrOOvqMoiwK-NuqutyThkS-uJhNeVJ2q3cXo0XSgWK5V7iw_dl8-4Yf2D8IWrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rf5EJ1zUizRt7HhZnPrgPMKkFoP-lvUXqUeoPdz2YeF6Gu53WyfomqYmJ6XY8yvOKmh_D6E58oJaAcYIKXoXJKTsTprGREQU_q2yVN-re2R1w4QzLk4VpcXtiudImMvbSKV1v1FbFRnZtNzpH9lLRQf1vl782tVM06oBBSUi7pwQukiWdhPgFEl_l0c3FsrhZRUEo9Unx5LJnA3eYTk1MwIu9clBfjfLSahfHDR1GfHNKAphqsHKpYrPAbheB7nnYppJ9mciIKWBVuYtkjQMV06O_tZi71yf18SZrz4A5k_cbXeZe_7UVWZbaJ9SQlCodHJ7NLXhjAhl2MYo-UuUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VWsKmgR87wDHJih7tO0nGdQDhHMprdZ-LLONdgWz5AvM_SUpFvG6I-fMYlVyEFkFSULY8RHfOoSWKXQjcYJ78ih4B6Xs9Sygk14J1MjYviB52mBnSnMOBtdW9GMsVgMjiwKTTuoz4Ly-omrw_lkdaE5UcF0XtOQ_SCA8vMxQvyrkk5wz7YBdAGUMRMiv-9m9pA4XtKF8JHCIcTHJohM2BAUuhCpHyoc1mOvPY3VHfGSmIMDkt9dmnqyQkkTKwjH21uKUPiz26xdfyAxYkLI9rcmE4-wCbuQ9oBR2l8c5j1VkSxwKwJOOzMCL-JB8DhZOHJszB8IFX6CtnG1723CplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RQ18ajsMtM5YP1ViCes28xZA6zg85FBRuT6H4frmVwp4MBjVkYVDE4I1EgV9Ka2wriO4Tndw4FqMdUksVE_hFC74ENmV2Px4DuAdeB3IrjHKYXWMIGI2hbrKVYnyV9gsLnbr1MoXYMuGBcDDAdd8ueVdBgXraS_cysrWoqOtRuY0XvvHInd6ek4QpABVsMYp_Kq0HEMepR5jgPEG_39u9oMx14Ys2i_UgrYPR5R_eC-0hQEfQXzS5lKciAMBqwlVKPEoKzq7e2b18Z7CSKF-oOKen1VYkhWePq_ETB11w1rcxRawJh2heRo279pnokL1cF30J3WPqB6mXn1FaMaZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BJg_6N-2fLzKya3KoVmFY5eEDnuDLN1Ws1GG9T5vUK5x1NpffHdoctw8jPULvF2a8GeYcEPiJAfp7NPiRo9_ALC6jQCguzk2_II6wNbXMc-v2n7r1hawym-ri50_rvvECFLNiD0iv-0ea5VUPUzwUpM0IG1sDjkAqNLCRGDBLgAW1uQnV322QexiGgG33ANv-FA3ewrHtXmluk63sKdfJE7WBAHpNOVW1oXOS7pdia8Nvlbgl2iHVd8Av70iQPefuSCx9iyMIwl3V7aAG-9K-ocfMZs11LHX4jcelKocLkwrl7IHBWFQ0Eot-x-TCZKt319z6NimzHujHLDAKvR0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T6sIcn2_6Zaj4XHlVCCfpSVrBCWXOxmBv1WMrhMqOffaKyPHFZt0-a5eNcucg9G5qi5nkHhwBb5rckqt7pfG_yrduqOdnTgW_Xpbsegzkgpgqo_C_DQC5sHUUSbEKAacNMJcANDqqnlFexQptH__xG5-xXovITJkSViNgh83EuWoGNQcyfGOTdr6x2RssIdPy6cdM8Xf1w9zd9boKhQhPAX1-VTiNvf8-4n1YkUtJXDYfffjBADuSYPbbcvjRkEpSP-_Q4lB1xT206qSZtHhsK0Gsbv6rU0fo3H-oq2ugycnKXBg58olk4gKqgow11ta8PfRJ7Jt-7xFK34JMuJDTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gR6TZX_mH2v_zeJ_6ibTVk2fJhwLnIg1vgHRuXKJnIlmnTH13FD8I2SDWs9K7_rGOzgR0yYufxbd3YDWeZszoluqkjij_a3VIpKYiWz02luZCSk7x6Ycslr5Va2E5kCkz63Qh9EEyVRwNn7aTtakye5N9moOudKnk81OjzwtJwfw4OMoIFs6mQl7i-JrC0gIJ_4d1Reanbp2TVzEIT-_VWdL8ZEyrt7kTS_nDrPD0TYDbtzzhjZ50Yyh5qUlwdrDrZSXHofQg3XW4830SsWX2pLIZeZq2dDK5jGyO2Oob34S9J5KYLqFXy7oSMEPoELenC_OWFKNgyubBLJ6SRSFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwDxxnqdPsM3jt_du3GNFoPOivBcLAuYqQ_Ejp6Zw1o-0kI68Ax5cGp0s41FMbNnYxlyxII4PUG1L2fn-Uv65-gFzJPvHgkYhOY15ohHC0GysWpDWnLM1iS5uY8YtgD7rjirnmptKWgscI3CJnx0bl1Ksp0kVbPcn5BBZQ9khBlM9wvpTWFZkdDAKBVFhvt0X_fh-fM-3uovcp4WJafc1JP7BdUwvz8SGB6utZBpqATnBN0Kk_aWsOUNEfGGNjNSGA7twedmB78fE-VxDJiovvzzcwZkcYSJEkZ_2GejUGypHF50xc0QSPDoMvuupg6mUzAe0cH4m18oYr9NuCoouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SkD3Oa08ZMtWOMz8OQ3W_4QWcv5zFdyKJmuOujig7awFFeaqPNtAbjqTL1DPbSduxDFVccHRnWMHn4yUzcWWYA3OnR76yjy2n2B6ErrhfDGqIUd9joSFOk1DOkm4cLLOJUiksUmAS9IpH7F1IhKDxYn1C-_G610QR3nBZdkhWLWmGpTE3yasjUVLabD0Rya4IRuhDGGFTDtfiA7CyKRB9Ucv3A8zd_aXZWCqtoZBDdJ4fWE2xsu-29C9UaLyjmF1VDrp8vXwaTRJi19_NUoDV8uR7Cv-U50rv5FmNTHXJ0SCAcxfCzVa-_IiP8Lx-XpdXWVsGbTF9KSvvLLdIXnQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RveDd-PR1QRmTD1DfabBJdZi90paLFrbIKpqgUNx5UNG3kliOi66QPrDyhu02nXpErb-qEKPdnELeI5kK5HHB4urZcAuubf22vozxzTnnqMhJViCsfAVjrTCO-Wl99jOvBYt3p1-ayx-bJI1d1kgJgfWJJTsr4deeYzWE_7mllyezoTmH9s0gETwew1JqeZ7dHBjzxgzyGtWaXj3pr_1gSTKg_dslV0szZ6KlV3kZ2QLBQ_Je40GH66SN9MRCvtFtmP_zbgk4L8N9-bfH7pNmyxfS4YwO5cqn2q8GGXUEaCbM-trMDSnWRogd4yXY5ywRb2BdSDJ-91NGcr-phLBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IQVpZfCzBiGVW33qTCD6IYnSIuMElF6neRCjC-7LgLE4vwchcOh_CgLAnaQER8icXeMT6DVB89YSjUdb7NDf0HDW5Tta1uFZzIRgbvy-mwWEE28MiKQvlVjlA8sDtRe2RXmR8yE0M8xgN0g1EUQdDx68ZhLgAmxg_FnQ0bjN1_o49dThfNA68xLi-MyBp1Na2iFbvljYK6PDCeE39qniCP_VSDVZpd8uENW75JHWfRHktOCkRD5uwqGpKzKK3WPrIF2vawhSBPTpDtkuZv659_4rTknP08d00CAHpP1XXBUYZh00HTaMLKALuRSJp1OOERc_GrvVPH-4By0MXMa8Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fY869M5lxe3DUcy3JpFqgrEtoEy6ifbrDD2XnG8dbF0jp8wWhpysirKz8xc1xST2_Jtx4jx5NceJSipyrQv4rWcEDcZJiH6jZr2geLyBjDkCulWqi9IwjU30HAANbfpmwKiC-XCBxO4b83hnOls3RMQFyfxRP9SF7e8yHbxA6eRKvtKmU09dDN4wcsIoEBFYAUsnK2hKHWVCuYm03ylpIfsIIIp0QTLSh0LTUOn3EAKIj7w838e-oK44UaB1HbkKkghy1fjy0W73o0TZzvKLKqIoQJFxuQTbb8y7lcYrcykGAvno9ok4dchy7dJAkoN4aReBHAQdCjl-04z_M6TWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uzn0OAQeH0wPaRvVz9mr103ghnJhnKhp4DALzmglZe829Qu1TWN6uc-T3GH5lJRV9kAfQ8f3gkiDPIUJawb0_rPzUetgIFX_fM6VpWWdhfX7dYF0KaQUk8rkReFSerEdo0XtFp7kJoSE2SWs-mRNgZgQckaeLua2WkvUyexLXKq2BPXri_11o3qqr9bzbXNJ2SDpOQ6Sye5RMqB--sO-ywJtN0Lb9idx_RJs-fK7XzXUESoeU9RkKKa30R6LMWxO6WoxKiLbCtUUfV1GrCWBYar1B-iFQrAX58IJ-ooMPyleDxFm_dJ54usj8BhgV1Y93pYwOJzkIJ1--dsQJPFGvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v9UX0bQ9uIPSd_zVeQJyB_NIaPMKIQUXGhG0JADLNvHIBf2aScTv9O2c66Ff1tZ2-M9BI1hKGqgAMJ7NskFEjoa7LNxCCRQuiLkw4VgyD6s3l_FNoLiHPueepacM9DqC8PurrOMGeRRQSep2BfULy3LoQOMK5hPv8QbHY9w05ZgQtLQhUUoCQolX9SffDzvRSqQ0tWwQQR0mO2Rn3Z8-0OoWkxGoxSoeP6GLdf7fDv1Q895LHtVFv76YcbQ957tZgKSGUrZogVguVMej1csbDiGX0lRQEmdLk_ZpejUlaOSaHvdcBnfFnS6uRV9Qf1v50Jt4bEy5zCU1RVoO2dBGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lx6fiyIY-kEzpoFRlj9RWtkCLmE1IvoK2KOJRSGsRB41-ASiQXrFSaXcT5IifPswZiiIQJomUp3-23n7gMPiGJDPKUnmcaxNn-XwsdlJa8eLACSaGU050ynnhvB4U-k0JbFW7xF_EDfbYVYbyiGDJgG3piOPH9s3IOUySlwNxSnrEPdPgVm23oJETdM6atFdd2a4k8RHYnQtUlaNXMFoqV4FrQsSI8kW2di0UEBH2OhdnXHjcnO3RgQb5JG1VZEFgkGVSvwH-Apjws0fjV_Z_bKZR297kID6L2Cw7GJgC_qOUblCAYZlNFEFJz0Mwlxp1T7Mpx99bRRZySYbTz-Z3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cJqvyn-Sp_1Ck9OIHbPSFPYM-pIehBFVuKDM_1HMm8B4ogTt_ziyOpUL9wcmWveCRJ1Wwug-tD4qoW3XenXyBbdBUcB4JBmJOEPCR-YA18_KNNEKvpDhMTyn-YYeC_BDA7LnRWzRuhI8vtkG21Y55hBCYqveLND7rYUUmOoJ8ABWp3Mj2EdKv4OPUt-SQofugp9H46nArVrraueqg21YkvjO8Nr7tzgnnJ91WwRurfo7-2OjZmDwNSG-xcd6j4qiGvO3YjXwNAlYXxhp90_Amc7qSs_mer-q0-CgUChff2ss6nBwTj2Utjzr1lxC7WWFOb5CfivqdVJvoKaOQar3Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJAToEfYhQGoUTVHELhJ5OLk12kMcGKskc3C_baQOF0QzE7_zZikjPUKhfYhHcKgW4XVoih1pfWZnxD2v_ZUSsGz0D5ZaOyGes7TyVLVYBQnRgopF83yM4V1bHYWpT7lYaujpqV4RyPSaBUOBWT126QFRuxX2DQV1eEYYkuhO7XV5nSfyGWo_-WmLHUQlko_P9ElHjpWTxveWrgRUP52YaHbc71MsrGOzTun8EwKcSMoZr1ya36wIjn0AIzt1m8bc5rncGaQY1id82334OROcE0ooRCWkY0XFffs5DLRkim71C3m-Ccd2c8YppPTLSrVBf9Mk04RuVbcalCP4QcJAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ct-LPo_MOoM_0-4sMeN5TXb16aI59BfJQvsMYXGuIlc5TS15dxENHzRNr1D1uBbR0ORb2LHacVP_tdeDLgK7VMVgP7OO5Y4_ds1ib4kpsibSe_1hyFkUOimu7oMP3GKmUaumimpH6CLRYdRgvBFJKc5cgP4VnaLszM5RW5upMzkJRVciVk0Ynuk6Oi2ydU4sSmR9kni1ndkMWKSFVlASrmIstFPr6Pf-TA0naUdeJ8GXRnyLmANtWPZiydbl9_0oMLuNw86udZyzYr72tG_lWrkSUp2fODWzesZ88ddr_pzPTe3X5raDFdpnIkhe8Nhq9NQPNMBP2L0eTUba_nfCvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QXCUiCHX1fUBxVvW0I7KkOXsMajorr8hW5syicD9cC5H29weTw-0wqakg7BmQmviO9IPYVI7Y8eKLlPYXen6n4dgW8TP1ev23jYTaJIscJJdAFvWDtq670OfnzluHpu3mvbwwzXCVcJ1_9zxvWuGXOTwYGTyrNZyeB5GC_wMpnrTq07y66uRxyY0KzplqHfFqgrQ7MW3iEEnY-PVR8stdLkkOXhVMhbPSDHzTxr8pMJFNSrMbEG9oqllCYrcvyTR8RBq65eXEtwb0mgElryeNPb67eZfzs4GkfwqJwSlJJdfjd_8dM-1bE24gY1U0s0VCKMsOiIuOBJLo9hr-oojPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KsNU4hzHux4K2rDZWQibhdiY3gC0QrTBWM4sf6a6sZrskNaCe0hd24gTVCr46PvRgrlXSynga2Wjr_UiDGlN3SI-2mlDFCBEynC1_hIVXXq3CFU9II6L-zPaoSXkkbojRSopOTukPU5T5LDKCzxIir-dFhOnzhkWxSnsLFfF-5WTso5jbKD0dG-5_hrc36PNoBwl5HexshYX12bC_AA4TtNYCJLGYUuTTYxftNjGwA3g8Uo04-nd_8H3Lu5Gcq0ylEHWSUP5IHNMdLrYTdla4GytckECCH0IV1VglZMxLD7LEapE-FBPXh3MDqvi0lJ7qxJAfihbSiJFxXdofupQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NUFT-Zo7SmWAyslI9m8p0XtVXPR2xJLswiLsn8W2uI4mYqoCggxwcFlDkRZyouNg3NtpPlwDPqCdFW1XmOtvf7vZ67-aWQcqr0F-jsIabuxs9lxJkFePON43TJJ7DmeBABXMlsmHQRlLHMiPv7wkm1lzHq-ERNI3B_PrK7rJxX1dhqqduwsXZ8uZWPVA8ABXNE294lMI5hTKs2xIwvDZIYhtmIidfi9oH6NOoLUbCIq2swCS4iQ8tIo-75WET9Y8zzyPvNqc8Jp430FyGvYWSWYj04vGa2QipTl--thqWFYvxpAQ-TQoX_bGAN65iMxPF1f7Q5qsrpVu250XWU-qGQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=OtvxEaieGJ_N_VmZ6Lz3w4lnzLrZ4ikFQDceqZENDneoJuVOKB19BgowgOJB-Z-PzNKA8KHZdU6zDIO_YbF8ZqnspvXgwUze6LEZIcrNagDTypIXUnzvLB2ykAjXal2mTqC8Qw23JfobwRbY9aE7twgjNsVbkieezqOp6nbjXlHdHmlWy_dU3HLSiJMhfKE3dmIQ74iYIP-nZPwG4kCfLxLld_XQZhZE3nmipTtH88rM3FAAvE9iYU2KHkvKuKiFAvZ8_dy54FhF717V-hlA7q-W3o5izeCiM_Pjdb_qWTCPgNlKiOi9vkgTKdTZ0DUpcLUqHdNmgqZAc1xpUHhE9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=OtvxEaieGJ_N_VmZ6Lz3w4lnzLrZ4ikFQDceqZENDneoJuVOKB19BgowgOJB-Z-PzNKA8KHZdU6zDIO_YbF8ZqnspvXgwUze6LEZIcrNagDTypIXUnzvLB2ykAjXal2mTqC8Qw23JfobwRbY9aE7twgjNsVbkieezqOp6nbjXlHdHmlWy_dU3HLSiJMhfKE3dmIQ74iYIP-nZPwG4kCfLxLld_XQZhZE3nmipTtH88rM3FAAvE9iYU2KHkvKuKiFAvZ8_dy54FhF717V-hlA7q-W3o5izeCiM_Pjdb_qWTCPgNlKiOi9vkgTKdTZ0DUpcLUqHdNmgqZAc1xpUHhE9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iy3qzK2M3Tz5c1S9e6jroIFHJMK3HbJcSmjL1kyyIVZwUTI9er8s_pZAQLOuM35X6tPISuTzdM1abCev2K0Xl_qFPlERfmieujca1MQ9ZwUNPRGCSBw52GVsLTiHkWepnLfu6ALORgGQhxMytCwVGkFJ_E3zYB81CmLr588S517xuQ5nkqi1ZubvM9oYtCOQ_mXnCRMgo5y4G-4unKg9P5ICzm8mak1cSr3lzHrOhB_q2yd5qNftq75y6aQqVwTyIIG5CGTqka1qsiDQhPhAIM-6nOh5IUBKts74_WoyiBQ9CiO6qc_j84hmazmErie3V5ikYLotetLP0bHBiqRg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OOeCz2MjvXvnZxzR4P66E1sYT6zvLZlvjEyIAX-McOiokSdsWjhJt8a0ceF6ID7IVFHrQ0M76FmLh3y40Ap38O-ca1xckTgbmBGn0CidNTpztJruZcF7rGik6QAcu6oL4QbI3cA0LNaV1QmFeSFV5EDnO5s4JMAA5mxx-FT21QJ35ZJGeaCQwLK9_2KHIOVuNswVtehuA-Pq4D3_XGSJTG9Dq0UMTvBdCsCsRgj3rNPMNLy3yN9g1vofKoCt299Z9Iwc0USuEMXSERzCz9S5qVchwGucEzF2dj3OjOZk2_Wvb3_CmaBYr4f8dpVeZV1sRD8MRAtEUYMwVmzFfpOLcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShYrYH80aqJAlJumX21YJcyFIcfCghfxZatENXNgPwffmKxNcghjYpTaWEURRuCdrRojEtPS9wIDNS89yYKLwN_FW_iEHBQDN7dU0i1uL4BfE4hTuRwoXmwznfP53v8gwjAatXvPjFLiNM3oujNzwJSWkor4GBr9b9-Ef3702E0rhPTSVwteraSOwSxAOTgQOK5D4ey6p2PI1KLUM-8RpzAgJc2vnbqozjKI0jOBfRhPsMZij9Ai7GsbJ2GjZPKYMcXo4pC9Nd1cCBnwVPT8u0HFJf0GgyOthYqzLVkvhQ4yRGM7gC4ciCS3ndi8ND5PV8kG8PjjQdAqddixi1hkeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1p29vAKLQ3XmTiHuJSOqMZaCvCTeaEKsMLWnNIBKxd3u0Y6aKIwktFFls89ShOfidizwQ4zvPFr-RbIdBcnebL66NcH6PrypN4Pf2Ma5kXuKxv14wZnbkfvQ9dlS6xtMoLrtSDjU2XGJsCJ6oYadnwYcm93OoYHQI9-AAgYqZYJzBRxp2fls23S_o1I_CLSYISD2DXTqnsR8btgY_K68QDSSGRyIob6umF_NN-SIBEyDWt9DwlSU3sYP2cnDc7gbKrAq9dDg8h_anVX0o0oU6yKqOIItB0L0Lqz_jTWM-Cm0AMjrP3QimPatu5-Wv_ximwQcECT0eTKlUkjy-VlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X-1BdgZD69LPyg9MibFP1pZSy2kACyp01D4ZhT7S9l2o0ayHnJ1fq6oHoQvJfvl2oXFRbI7j7SxYJvLDrl-za-gAo8sKYVT-T8lFI9qBncVSu2zeDShwHS49kka3t5g0F1IuvBfkd1r9wNXp9b_FL71LCA7n8IXD8u4YVXDnWlXjra9wtAfue9cJijllU91MRE3yT7TTZ9ejESViEGFie89okyW__uLOZXSx-yJVzumpTWlRB-VzbI_N5XqP3DAr762qO5-A1hzRz-YEJmsLMBUYkN5nSp1eEqmNOb77ilSMDS1bFlwp6dVqZDar59XdXa2L-2YmTpAQqefzFx2-Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3wQll9a3DhQ6rsj0IidvA70IHqzpEyZd2WMbFFaSlUikug2-jDDu0ehkhW4C_wqI7ve92zJ3uDLNmLgNhzthBynFKndUHkt9AXhrvYQhX2HyFe47ptABV7A4ZjxtE9ClrWvOxYuLqYM_So9JmGmzgn0tY1A8tPzbdWOt-9b4l72eVb8wo6F5LOY02_txgbLFkwi7NMV4EJqqkh6CnulUYiw3ecrSnDBG4WvFvk4HerEaZ8Uc1fhIsi6ASTatlmD2gJe7j1yCjl22MQcgdXXS46r_N72CxK0fh8uvTd4Gs3vd4iwtpLeOX0vxVg5hvJyJ0vZLsxixYHNarxtrNGRIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nECyqlgFLeU5eQudfXZKtUOWGmljmBdrpu6D4k32S8slkK3V61UZGKCJMFUy5ttf1AKgzymXSrAG_ZtN7LEPfm-0RMq69LM7HszczgMA0BxCmafk4WmW7AzpLIb0bfkAyzEkPHQCwIsVh1Z1r-DpJVc0s3L7iR4_aj-w-8weYI1tVuAEhIJmzPafGs3vZfMmL8LiRjO81OMkOyRxsIrZ40ecVwAS9IJh-VbZeoA2xNBVhEau33iN793MDYs8DXeQ4bf_2V9nKQxQ6lsScfWqrLVGrsXEtNCLOPIjGRFwM4dyBoJb86cLdrOrLp9R2ciQoh-FQTkHDeEJYiPTs7lr-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/izMg5zDQ51fKCuqFhC5wMwMzIM0fRCJ-5zFGTBMcNg3sD_pMF98v2IffkfSEvh9O4X95aLOJh0i7fL-ANwVTMlYtl7BJ_SnPf5OKEO-OyHIB8Wlkmy6pZj-F3NMYUrJtNgVHdtv3aPT4qjKCclgLyuSt4YppoCCP40tGu2XZTa0OM-chihxg1S8rxwA23lvP5dJU28RCOTPp-2Z7YTqKSljSfNNX5N2RHPDtOdNQ1HnGP5w-qiryC8OI4fG8ik9SxclsdZiFVf-aNn2EG-x9ArpaGKkzp9hDj42v9_66CHC_WGFDd0CXd8sGQjM3MJStR4CN81S1LsvAcWh_CRrPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eIMAFx-oXkSl3DJ3aHeqAaA4W23AmC-ULI_kK_pQEZIiIMjVNC505LW8NhHU6TRvGXaad4oMDioiy_9zGpwpGpp7NNBXDuj4rAY-YMf8MwHopRIgPv0kJWAbr5d7qgPBUs0R0saISKJHsP06lYq7C9ZsMPWmemWjAefLfVmUH6A3M1pTQxVnrlQQSIuN9XqhaM3rSSnZmyDQRESygDeztZVqsVhnGImbtJ-fEZwe9d2CdcTWz7xxa2QZ7_n5NiJlz-sp12v8-5NjVUlIuBV9zjpu-QIicVVVWRt2VwUI0q5t92iFYYjiIUq4WfUrs5V7TywP_Tcv8ktdTEkF-A5UUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/wAM24rzOOhC95zUnnxS0K21qSIMOlkVD9KCRt6rFKfUmvMgspDWywjrx_t3V5deI4SF3sR7nGOJLTP3ZOlTn7cERCBZgLzOl6r5oqBPps3i6Vb482HtwGDBmEmCckIek2SFFR4wVSN_iRFWxTVPkGybGPaE7xfusFk2fkjzhHxjImoi4WfVVnPc_OYbn4ZzZwn1vB7hvC-jsDVh7abCiU-d9krAw_UhBBY7-g9yHGQbSTcRiiUy5lLErNMrznzxELFx0oXiYSpXw7OZFcbvRZOnuiQoYXYz2riPljJ840acXXT2O8aeOUy-URncHUmd12t4LITxB3fNMx-mR8Wxa0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MpiwVUfD41JoKuyhaPqRDn0jOuTdXHnYqRGzQ0txmWhixKzAdao-mRzAUPHMxfEoV_bZgZUaseqm_FvoUlcLaIX7p2_AwqveVdXRvaI2Eh00M3AhSq7Hef63OdqAl-v-ZywI6UBneG-YNxTdnvFA6xyVVZmrsioHfScUD8yy5thYD5C1HzCsjtihUIQuPlJFydfmcQRp0pshIegfCUdKa8cIcYd5rEyTl8bYiq_eTNtT_Z_22Iyl4yFAMBKCxzNkRakq0ibsZhQFv2XG1WSlcbTLYB5_0p_EuRBIp3Ns_6k9j5w_SM-V0RoXIgW6966XUaBjlBDfkiYrn-C-bJfmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=VQNxv9pEYOR3ozno_xo8_tIbN_25c2-dvP1PjGOSE22cFauu5PowdgQqH91Q7KIY2WIE7tyAspulQiXDECJDTvdQxpL7yRPe3NRHH2uk4vEXAjhNeBHbQI27eYe28Ghz5oorzib9Nser1ogKRFJu-kCbMBFdm9GQHKBZog7aLSA-aVPsZW3bU9TZhQpOOk9jLvv72Ky4RG_IQhig7Rm4AzRHexgur76xmb4gAYzXTcA31CH2_WY8LcFklJM3UKKVDfwXY1PaknI6kV1fFtb1cpJE9UwU_lWMoyYzpBjNnoaDUoOwNo5dK9_mctzqylSkNaVPK53yWp_qZWFbaiVRtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=VQNxv9pEYOR3ozno_xo8_tIbN_25c2-dvP1PjGOSE22cFauu5PowdgQqH91Q7KIY2WIE7tyAspulQiXDECJDTvdQxpL7yRPe3NRHH2uk4vEXAjhNeBHbQI27eYe28Ghz5oorzib9Nser1ogKRFJu-kCbMBFdm9GQHKBZog7aLSA-aVPsZW3bU9TZhQpOOk9jLvv72Ky4RG_IQhig7Rm4AzRHexgur76xmb4gAYzXTcA31CH2_WY8LcFklJM3UKKVDfwXY1PaknI6kV1fFtb1cpJE9UwU_lWMoyYzpBjNnoaDUoOwNo5dK9_mctzqylSkNaVPK53yWp_qZWFbaiVRtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/unSGUr9xIWVzxDUh-aFBf-xU5-U8zauboIYF5qMCpOF-zqpGzD7mzsX3M0fxVWK8Ep_QVGWRD-v8wmwJru0WqKt0qRq9Q7dfMZybUSEcQkiP9H3CsSGD1Pge8HJJAXHmIVprEiHITpNqSSaXxGTe5XnMBCdMLxDFKxp3RcpxUkkPeztgvxtd5VunybOT4L_xxlU86AC3KQ2458Z2LsfrMGy5eGfEcLtBx9oHFCH6D9H-gjqpJHESZcSf8hJ0igUyANfYEKLWBEkvPDP3aAQTu_Fmta8_oYihniiISXuI99T4fQStSqXnpiuxz_hKzl-l9vznh9W56s6rBg_yPtqHIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uE9RX1O_9COWu2FG07gIwn_uCqFzWvuHV_R2j4XMAAqNsNKJY4ngvwR-T9DDtGxh5E5Nu-44_lALTcCl9NzGbAcE4l_weONzeYrabj9VfsGxp6bo1C6JIbjGL26t2VpH5DjebnJ92gEXmmptWbNS-uhZlwrBpWcfxDVm_bHrHE9YZ8n4-wvPls6PXQEA7rqiaIi_Oc3RhG4WBZReSV5sOvj5fCzvKrCvSk1u_V_cYYfjsMr7zmLkv3XTF49rPsjrHjZ2mc9VaArEwUcbikBY12wfplsy9Y33yuE6-TBzBCLvKPasoeXcyxjSZKHyWmL940gOT0QNljU0iUa1pKfxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c2Hm4mcUI5qbnDmmuJi9moDVuxgLiKbg71Eu0XG9ij7nDtC7S4fQmB9CJcd65n6dlsszV-BCjSce1KSo96MHlr0RgdtXc5yDb_yNyeiMbywKCZ4ugECgGb8gVI2vn7Q0QU1CU7YJy_quY046re8GY3WOYAgwMAk7HwAkyu04QK80JUeaHUgWO_k6iylllEaSOQn4ImZpiZzS9F5nfagK1gC4lVRqQbh6ekr7a77NU2ClelYZ5JNGkM4b4eY_yngLiX3PKTockqM7EU1mYBsXoL8nIByqV8PCREBkcnnH_-Qq40T8AbC60CFC9Wl68CuD5Qe4Prbd1wUuJ8DJXPWohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lcquuE2QQHcdqgJgc9UNnnH3HR2ZaA5xJeANhAYf5w142BYm6q9-7R_A9ImyScebVGjo47CSseZ2HXD8jUX-tqwZOmZ0UBDfCbZTscH0hY9amR82lKJHXV9uplKMpah_na2XPUSUsMvTzZZB9BD2ED34W82tl0uMRI5lgvVdvzFRuiyMeFoITF3bt9afvrzgDUfd4ewoswLe9FlpsOKZkOkjvR8ap6DgXiI8pMiKxJEB_FiX5uonE8hgKszPrPYEbi9KiQSTTTn63XKG4zjDaQwVLdfSRE5oZ08cmR80Z1X2T9wTRUOEdpEob8HuIRP_9HTVfF3qbs9i36_4d13E9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ci5ruQA2XRXlSNmXlvuGRNDzHfEu-TfysHONCS5zDGfLpTxy1kkDc3wOfoy6HixxzZYuJwenggvGwU5X-_0PR7YRuzomQqY35SIJLCeLTwBckUrCOSIT-PuF5yy5mEUmCWgtYLQ_MHAmMplBeEvBU7k51S7slx1eq1tCdsSPz_Zj2uzz1vjPv9sSUEaoNU3W54eV3dqHyjC-aXcYcPbar0n6V-j2pcyTUib3QtzDssHUHHOf6x-uRGLQcBJE2EV1bzO9cyUy73QYNfuRsrF65-gLuznwmgAykt0-YeHDtd0egSB44TrTEfshf0MBGsZkwz8dCmmzhz-9GiuUENmRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BVgz71tJF7yhubH98UnwVKhsqCYKdBs4hwMUD6zlaOZgk_3uX3a75cPgfDq-hl_q4ruckYK3i9Tu_bwS173C167mHbRuVlPIfW492ETl61QyWgNY13lEo9lQN0llPzFvMflvrFJwTB1-tYw7Hz0JbABp2px7V9e72oq_ET1YPCNKHy8utxEa8nts-XNRaQfS74WTbUHFsiqnFK05krsY7Z84FemP9L8DFI3iTIHyjbIWik2neH2eayAoBdwS44LnpvJzMPOmw01TX3ODmqafftPfPql-hGwTv-EklF0FoS_piv94SKFINpP8DF3Jy18blKsyM5_ejKc448QOsYlZgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gLuWWZ9DNAAgFETzCLLlZMClyqgu2oUraVNW7bm8916PkmmbEOVsToE8q5ir-M72vt3rWai25a0gCKBzRyZdH1NuKStt5HAt_CM2S-pUK-KO94QlGygkbLPg0i5A6A64TjiGZUuBVLRpjEyUqmFiTtKVSgIdQbORTVpA5uvcQJuNhToZ_37sHmzVlEQF4zXNgiSGn_B8C3TWscMwlJoe6wea4-EkUuZ5mvdNJnNSA0AMY896cPyJ1tOyY3PLDc5WQ-ieEGe9BwnCNlRSh6npkf9vR2I-nUZOQ53xImBqXrfww1zUPrUWChET0zFshXfrR-Jr7p9o0qevbtzYgwOFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e609XHQYZwdVUchcD7XAoST-L4RTIevleRtWSFUxuIFhO3DB6kfa28sdqokvVbyp7p65DSp0uH6oE3GQqac72E0-fh9LuK3aK1DXxlboGHWIWQAsTejHURrqFxIg4vgeojIU3-lYXAmLGech60ORD9qjtlpW7B74TmGt9z5KHWD7JVYajiDWOP0jbvocsQMmIN5w6wn2A4ALry4qT8wPjrFBAJYd3AaIePHT1WnS6QO4ETn_hRzW7otlNeT58fuAFhAZ2Hz-J4NfiZR1O9xBoZ8aZrB8TgYMSstp-sdq-VazNKN6MD26bBE3iq92N2ymnnH7e6Gt_tAFUNHxxpxWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rM-VtAX5sEB1ZsfYdB-YSJOAx3wRRmJpm4ZAvbEhikS_a66Tk9GVMOA9NU8l6Qp8WPhtV0YPoVrg2dUWWG9jmaieIBSwEfCQLb9zy8HS4Qb_o_H7S_lQMk9ETDo96LFmA3NXPrUKJQZv84zWM71iCS5Ya0f6Y0hXmRdLHsC-b4GK8AEmpK0gJEchF67sh-N-mHk8ONdPIVDmq31s5LEKC37V90iogl0M6aGtum5vQjzEb40SNJ-nKkBb3PMAxiwipnzH4PPZpPC1NdlgCvQYchdFTBpggpnN-GK54rNJU5xxFztnjMTPFVXZM0nCrhTCvfujhyAVnU3Il_bwwGFkig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dd_oOuwOqdL7sNCJ2j6OTgzrh85gjebs_NLATqurtE35nrUCtk7bAzLNGEE56r_VNZ4bXoKpDeHxEVNF9R2rW3sBDqazbmPF52JnGrVyuk4lC0_9h0sQn4LFCEfhtgKHt41UhoQU49Smmt2l7EUSvoX3n19ucJDfn-6GPLxlQW0QwiShP8LAOrtQXyjVc5eed1y-l9zA8Yq3EPbTsGNHT0B20CRrFz-TEJBfce1KGDJiHj7vInUVtAZ-nEdPO9YMooqWFsqU8DKdzmwXxSCKDIkENHiMUSL9fd5Nitp3vRsZcdoUQmIBFzpyfJ2HEQeyNvm6lRZLMLT5Ve7tdYp3pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l3KtMBQ8AXLc6pvXKB0VyggWRgBAIQWLRL5-FpauEYUdlFGSXM7FR0V2v7UUS8dXal_ECBQ0wCGkeq2f3MfaMBrkKsJ16yaGiVNrBRXSU1kqpXSV_T6Vj0xejZ8Mb7E58VzdDZ9tAMi804HooP9H_6cXqgo72U-SilgZqqiDiuMmHwJqub89FMJEDyofwTYaW7NzzdnT672Ioqz159PCBENREmgxVUtGOWSUJWXDGLS5HDeckqpMHnAIc_2fPshIElCW4dDGBMNJofMjLc5-3HDvtpMt-McEDxgOwH4SjvnMt914XMTq3DbFs-C4LoUaxOLJEtNMMTgN1ne7AElq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rI9cv4XtBKS9150duamooses9lZjqxFbNmi8GvJfSfaTR5L6dujKzVW1Ibrz6dH2HYLbl6IOjQbD7nyUhs_l2jlhaY_pgSqTL-V160xjWjOJ7QYOqnWcsRVn6yZ3DeJQxRKa3q5g8EoNFJxWO9XQzGfjzWEgaUk80HmhI_CbPZXSPdxt7sIlVFI0zsCxPdXM2IQtWBfcsPu4pede4ooYv7s0lPwBjS_ftp_cDBnRLaeYQrFDhkVfACNTn5GrvsWpbxYj1L3zphw2n50wONd2scBeCVriV3txLbqQpLxFK4l8_M0kIl_H5UP2Lzw47Uzw0TaYgFxpaW4ElHMQqR8CPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sldNQJd3TBVU1mMeKMVPeJoVe9XNM6Kt8bS1pQVxL7mcREiEoKzvvHDuE8RhK-nZa0SYF5V34DKtta99jCebqePQO4DJIKYupLjj-JGBj1a7Jhh-okbeQpPp7ry7kIm227hUST8v7H9PEZr_fqAmgAqbDkvgr8yH4ur1G6fwIGy_VKBkXiULpLmkG1VDvE-ct6KA-jsSMwfmtATRVHxpoTl0H68FXYeJst4BNlupSwo91QVRcSUAJtTXj46_UrtX7Nv4zy5gn5doveMm_Ieuuhy2sVLXrDpSKP_f4OtHbKL3BOjommMzz79kXse38nrwVtoZ3_ioVHMu9712vFK1Xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DBp_Ir1wCD546xBOv1Dz4OLjISo_Hw8kvBCmZ0cex3GPBthG3TVs4-OxwdIxozFAub3JG8d17sL89fO1Is-PIx0VouRCGj72pfXJ5gcs4ZrWoARKEfsZ8h4yNuzXkc56jBm7aBlJLbBPn_zKb6ZVNafxUpIZTRlfv3ohnT3wATRu7V1UiuLYyTUYt0cI-FOyzqzmBF7AmcT_7UNEyqvkcawB2_wnAZKe59CG9QXOp2z9AMUnSyrc3tDsag-IcrHdZJ1jDVxMbBvls_tLgVMtVi5HGnYWG5aCKYsrpMIttA-9GkCI_x4GErAKdSb3OIWL-p1yZ_L6yfIZVqg3FhyqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RDzE46p3QqlRNLL9i0Rfq_18eWqQdHEwUQaw9PX3cw1ljRvoBqTEN3nlsiL9N7m6nX4Sh3H37xg6RLBWsdz729iXACSdIChx_6CyWhYyw-j7dthRxqAiGfSg3WvM4SIHze_hvyUNo9OCruAWy2fwEEbF0pe4vrZ9gNGV9aBvgFRe3l_LsffsGIvLP1iEaY6-Clpf6BiOy2Dii-E23DrxUC5wn749syOe8HAYushEGAOvRmG8-L0eYpWfnCT3Skivz5A8DCQY-ncLFeq3A-nWC2AmckYZKcGuH8o1OwI9WljeRSVKxLD4Qj_RwrMFs7JiDXwiiR5Ny9S4RAmNy7fUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t_9pUedNc55EOlfGRzmPPFZVEMSSXd6dTBR3Q69gDWBOEvsu5-XvGCQnO_EWrcxScZgY0c0gcghTc1_XHjGFdNCb_pblp-YSXTtU83MqObjeAAAiLxVcD2SZyNTpn_qhhJ8RWPOk8gRZ58GL6k3nL0NYmubm0GcolQoV89FyKHzOMgmZb2-1WXo4jgfITShuu1HlkBKls9QbLe_Jp8Gmk1Uaw9M9OkVGVdMZhi1MGG7pxLIN0nAGyb9cCzxq-bPYaRkEbFHeX8h7d3CIUNAoT6Ac-cMB-dntFqH0W5fdbVwzC3k1Ss4zZiV6r9iZjK8xI9np3bfM7lt98GB11OxtQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CiBkfLwUSqAXO6DSxI2qKpZiMsvNtHYDgRs5EpzVolroYJI5ye9ezTDBE8fo-owBVO6wZG9Djh1Q0rEgRFEPJjxK-WYSeUT-xAvLppRFl-gj9NUdeaTLeKehMx_a4IH37wEv67sIEaP59kv5vrwHynlg85oL5rHGCXUhM9G_FSCzXhPmiGP0JM6xY5gychRBmXpQWkXGoyJnVh7mczmVEBJZAdztNbqU_bkaR8--9SoVtAGsUSN1FweGxJoplj_yX4vmEwWzbS-U2aUKQAbIoDkqCezxl9mwjWKG1OnsTA7cgvOhR1Y3ci9JE6u_DMI8EWok1kFEOZJ_LxFiaTYqjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jtxe9vWDMgGpvXIkYC6s5-NkmG79F_2R0iQkaLEYFcEKHpxCWreo0WO7xkGwQaJ9SfYu8FGD67iPYDZBIgiqeck7ng4dlQvk_ZWND_gAeTisrPWdSx5IoXi8N8vtxskcBBxvENuQeuOsGCDxG3svYSl9YWfDJEjxjpT3GJ8rlspJM3juFf_aTBPcoomgI_n0PMVgHwKCGP_pYl5oJeFCnZYnJiMvvYrQ1j3Q6hyGk_tS2IxxDz74pgBzkOsRnc4GxidaGIb4ODY9eH7mjQ1qGuYIuIB5nRBfRlH41aSbB259eieDm33vttFenxFi7-vblIP6RNoWLifBgllw9sTZNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HbGFxwpzQRvNAJZ-WaHC_k1-Wcq92ck43fxXX-DAfdlr60oMmMeIGHbnesxT420P9dMdjbQC-W7cdDGXsrXZ6uobY6kdUPPQOFaJEvFEUzyqdHPHuKj77mWjWHNzffWV1jLQX6KtnCBF9GHi71pDIMtjGZw_HGO4bvbTBznyTLDD6g3brLhcOvrkSWf9tjTdrCJpOEaVnl38PkYlFmI-ghP8Sl_djq58_45bDsyqsaL51UA5wt4QpO8wAh2U5faZGyidD0hemRgtj7s4SGAxRzv6pZwEKc_P7VRWIOXCbI-6jnzpFBQieQq3kflkDlk2tpmkVAN5ubZl5svQd7qT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jV9-setmtMbVOM7ikdcPJNFoEHbw6Lxq6P__wESs5IGn3h5UXnoWHWVQxS9JGyS2xKk83gJfiI-JwwANPznlNn1NEnula7jxwYot-jDi0DzmkvVwYbZg2COeptzBClfK5QHB2Qkj8exf5TR518Cr08fphsqJKML-tTIg-HCTicwgpafBne6WxWZmMYJwP23xC3Q1QH3gF3GmxMDV2G5pB7NWkTHX4DJIVm5ICRaNT8BbU9TUgsGyjd8wBX1fuzKD53VuxTa2AjmKuV3lBK-XnM9md3OodGqZm12o6xcXx2dGNnfF525bFjLgQyJp79aXnDnDFDlIjvEwJGuuGJxcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
