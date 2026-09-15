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
<img src="https://cdn1.telesco.pe/file/FKQbNYoaA5Y_AStYhdvBaL0dsvPC8hyH15S5p2H6a5lCB2E5CtdUacvk-KP4fErhuRcCKExRVlSqRVAdan1U6YHyism_RrF0daJ8TIscNzhfbZ-9hdKK8RMYIpIHLYIdQIOPkWnwbTkcwMOArj4hYL8gmSjt5HLfxC_0o_ewsk4O-KDhBMOAr94_zFgR1P95mF-HBl_x1dEZdAKbGK5LWLPdBQ5zeHQjF0g5HHQWZ81SdpBbKb7Ax60R6wOOOTDi3kq7EB8i5M2k5TGjYK34P7oENpt6nJZ_61cWnkSZUrcG_QKhNLzL7zLb2KvqZj6XA0E-dqmiG2Y4in5o_1vPqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 23:14:42</div>
<hr>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FISAJx-l7Ghe1RPYuC6Eq9kGG1jTBPHkDkX246Hu8fbzHUSlqh_U0HHP9JdcLloFfgzRslw9ImXTGULx_1H7bfRTIF8YGQeipjDvaJAdQHySw_dzkpWVoI2Ia2hHXkGFwMTkzqu02NlYugfmA5zcN6Zcm6fAfI4SLdRm0sMRMI5ce1CeZE0gjRd1oiAB4_sRu0FuBf7tLXxKAuiQA5vhswgVU3fnN_AhNvx7wTKRObyW4QG2aXEGg3jIFx9iMKoYGZa3_BiHnx82T4lA93XV3jan6CPFT1Mq2uhlqRQgvQ8DoR6lm37ftHn0ekGlLnIyHWw8y1Cj2BnRmv5U40wnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBjwF-9Xt3NhI6X1ziIxHF_eEZsTfZ5WJN2D94d7pXBSxWKn6COHHOP4qfMW3AGB5J7gPhzMH6xaDMMmU8QZVQKuet3-RFK3pWLu8VamqK39vn0lP_tl88lPBl3_gmufP4ENSnEHTNmcpe_b8z-DGncTyzw6HgzbDrwkIPKiKpa19GCVpTWhgIdp_SohSVGbRNchPS_7zIpLybsTsscP-jqtXI7JcrDHfVOQ2ie_901RUI5pe5QxSEChIPKEKAFhSMZBDWK-BYll0PNiFYq9hxGQvTd0ZBSeAJm5QVb_qb36bKoywCgtKp0pTSAdjl4AHOMjG2m-O4KY70ARU796cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2aaLwqAFnrOdwts1eTJKEnPlSsuqYglU4TqAVTRyThIJXiAwcNKG3FQ34hzGBt0YNMt1mJq6X3IPjiwQzszqwV2vSSe4BtiYsCC6Zoq8H22MZTzGx6IgRYyMlfQJ_Ncr2LxxiWZa3HtICBmLqE50q9SQDMfhQhS-87d7nMSDgdtHL6BTTVz6eQexK3f0MflHzNXhgw30eBscpoJ-gqRSNS-1xnmy4JlaN2IaxlqIYIg5QUYT9dLwaGqqZ4i67sRCdSnMk9FLa6t5rd9S1KdhR2-lCYDh7QfAMwGNCde9U_ugAyywNYiDGWxeJ0QiyQ3a9vMVMDThirVMVFB79Earg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ohFdT6YGgHSFGDzSz6Mrk4zRzSdYbVJjGQ68p9AR4zDW-LuxiXoFv-kLVNqZv3XIP4yhQO2284FVy1cZ5FfuuWr19LjKkT0vniA9IOunfZf9YzYot5djpcQ2REFJU--GAlirTKNYmu8sNJ7dFfjvZAyWfbkaAkyyogZQDjyrPbCLe0J2ucORYZRp6qGLfBF2MTv8KlA4yWlP-q9ijyisFfG70GkQ2geFlwdH-1ewgqn_MW7A1qx4NSyG42s274JfjTUGcTdeJjSAAvGGyRLc2EMNPmMjjtg_3O--F0Edaanvd2MXfIb7H_aH-fkU7TZ477AwYNiHeYC2sywoL4PM2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ooBS9-5IoVc7dT4DEMrw_I5r6ijrjvyikXf2P3LoOqW9XGzS-4m4HbUCiY4hASGrZG75R6WNh4FIe2F3Uo0unDW39uNpyePBeoekdkdHA_fSP44iJ98Hz4yKXtA8QKsKE_UHjGSEdMnfCXUBGfnoPKRwPWLOPIQna4phd-XmZRyiXSS8IE_f7Y3cgano7xqki2h7dvhzAjLgRX-OgOKfd1GoqZg9oQhFKpRoMZ6-S69uBIL0ywQi-UdcL9SVEBkudI8YNEDtpGZnSvHB618dkhkwlDBfMyssUNgaLy7_oqsOKj3xf9avaFoUtB2S-f0oGpxiG3Gta_NfSPYYmW8EUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_W4hOGi3lmF7iXF_9MGAwVUUbYrZOu_hSN0n_mPa4hmo7ZIzbIL4Bx4Qwf8-9D-BiWweSx8ifcE0Vy4V7LpN6cAuSeRlwFS3jh1sqEPNk98xd18Pc1e4_tpcNvbOJO-6dq6sJosaZJjwqwmurbzFd9tCpwOJgKgppMCB60ksf0oCFzWCQ57XVwJFUR73tHrOmKWfGT_DlX5ANI7FtY6sfuJRDXHrW076ntOkpn-A0bmEoxQ8trlDbu7dAfJf0s92KmfqeqNO0HAuAsi5SZPUYtz37cmb4UDnftV53PMxQvwkfjIiWcPTyF1thK_aWCxZJ4XiJtfN1x_VR9xGRcNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iJ6k3X9oosyyFmzALKF5dxpLe2n8K4ErL8xUAMbK6mz46EJ0u7Kg_x-vtgeupvPgnYw4UdApYrAUWFePjZPCQm6mv6_0JIbGs4Ccs7-iNyBGPzV5SdQqMY_wq2dMhhVB7HDcClc11SGARjKiLBMa976Nx5pewf8GEUlrFplHelOvbfIKoIoGkGPE0fRCWRQokUWcEl_QQjQwDFAZVg5uf4pkglr8emt3qyQgOC3rJS9F03_G_IJl0yCvqYQdLAt_he1O3z8fPR0urLOMZJdBaYk6-DhrF1oXTnPOIwifHKR7G6fSpQCOeJLgFGW9N0GEVk-SkGivs5hmT19moy9E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=QZalgbGsLGoQd2hsric45bfrqrfoQikI8l_TZ6faoPjE5WWK3lHTkRKN0MNZOW0kI_r9BUe4WCsY4ZSftmBywtgcYO0wqI1FXdgM2u89xkRxnU5xxEFt7zMl4tQRZ7H-whskT5ykWkGJKf2kad33dsn53dFmrXQksfxg_1ZFcga__AEB5EGsXew8AFAJG1L4CYGSYrUtV9uj-tA9KRksK2e_0hxHwzp5kYjqtCOqrPHwneDUZHQ6t-iSLDorHhnkAl48MnEurE-1ShW8U16yP6uwmGRt-rykO4v7JzeNadW9atqNL3GOTtSG9AxJ0q7W8lo8x6XASokCPfKBHgYfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=QZalgbGsLGoQd2hsric45bfrqrfoQikI8l_TZ6faoPjE5WWK3lHTkRKN0MNZOW0kI_r9BUe4WCsY4ZSftmBywtgcYO0wqI1FXdgM2u89xkRxnU5xxEFt7zMl4tQRZ7H-whskT5ykWkGJKf2kad33dsn53dFmrXQksfxg_1ZFcga__AEB5EGsXew8AFAJG1L4CYGSYrUtV9uj-tA9KRksK2e_0hxHwzp5kYjqtCOqrPHwneDUZHQ6t-iSLDorHhnkAl48MnEurE-1ShW8U16yP6uwmGRt-rykO4v7JzeNadW9atqNL3GOTtSG9AxJ0q7W8lo8x6XASokCPfKBHgYfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JVeUVPg-T8ebvhoS1kvQFzU-giK8jC75e0ju9ZPnJQlclZUGW6mlJDz8CuArU3HvYezE1q3vO0NFFEkrbD-x0Z7H5v2fL6LJ2B6Cvt8SN5di1k5T3wys1vXR6A2ALvbfsTnhgukmFOvabrM1BGr9jOcdqsQr1RT2hVcJhWWW8n5ApheUe75QePZ-hk250a5Cja5s9RIuK02r4GJy9eIwOdLcg3jy9ryw92O0SR0ccFLEwK8w0JEZreYtTZKKJOQKbY9WhR3cn2php7xAssmOhxa65slAwUDhZgEBAvVrJU0YB5fUfdmLyomfBM1QoRUKD8-e9rd1uLvE9iN-Nhv38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aepdKSU2yOjDVqYCB51LrZ3TUTxnNLz-IaZiwyQ7T1Ey_2EbUgeUYph68bF6jHMROUJppSfrroUNquK7yiF0FHDY6VzSiM5TN3u0Ce-Prwc-W05_poeSEo-RUxrKNx9BOQJm1Dwh_8ZQc9-Dkp1v45WYSWgtrL48F5h0i3AVHKEGTN67Zza7c3GO3XB8ouV_QmTcObBOWZQ9icIlQtcF4ikUhFE8O8KMT94EuqgiCn5w6ubx51jKlUDH95QBtHqLd-f8p1GFS54E89aPU5OCc7woBkgWh0ZW-NXLM-YaA1QNhnjet-OPf26i-K0pf5jOLKgoM9jnSwoFvlFxNCq2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc3NMgMAZaUl6kf6suEfBbyaeCTM5Oud32ytpPqMBRk6-70pMBxqfRoQIXhNliPhDMa1LEOjLhl7iVEeREBJb9kHxB88HdhO1zg-8I5XsmhY5TNLR7bUrFglVreuAjADuj-oi3hG5zHDW-N7nlvzitA0zsBvTnOmo1mv7autR7ffvluk6upjVVE6L_vrw_Vro8ar-tslkgpAWMC7mKbfILkQ1hQCgcmGiAIZMWXjLHDJi2T2MPDCf4YfweVNsru_RJ-feO5K88XQSRxKaDArHfvQ3Z5Y8sEpBg4-jQSRZw6UPklEIE_uT5Kd9ttO2d6JFSSZDpDVFyhJO3Hex7qH1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eELcmFJk3R0qPM9MKaCHEdlZTTC9sPmT4bBaWN5P3IRkrzTz8DmRFpzxdMojY3Tb4r0Gj2yV_THK7bCrsuW3cHaUM-7o11mSz6XBehBqGafTJRu8HcmlpkZCQ_BDM9Ymk0NuAaHmwJ1LLTewo_L3gteNMXh86oVgywbO_iw1SHva0OyLoJCfvDHb2frCC1BUDhxSCIfU3Z6gmDV2aCmGNnTsSg2oTthrlVWI7rUe6wkUmqMNZhptS_hKQMXkS99XLr7LQYTvYyPjvLBamzWVNsQx0DfPU1tLU75BeYJg6vnc-LTgXNo1E4dL2nPHtSa3QzJTh50Eyd6O7rzaGY2Iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pz5hb39hj32hdoc-2ix3FqsWRZGfGkppAmXYtQiiA0lfNHK_FOQ-Uk4b8c--uR1egmVLK9kqcHYMZubOY2pjuvkxk7Zk78KYCRmbYtm_NBgY1wInhWpwPtCkhBm9_5nE-GgD_w5m1LXtl_j0hSYGUzH7nxO_qNaS3TymX1kanzJfFI0-5O8ICmaqHsMsSc5YuaYKo0_auJFXAZbGbuCfEc4G8UGAkBFmiy9C13e6lZhk2JOcY03pSs5EugbBjU67Hr2iwlDN3Oje0bygfOpGBr-6MWMkkNuzyJnA2g2EJkT7il1CRSo2gd3ME0_5wvAq-B5iZklLoHdTIKr1ms6dqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jYSK_bzaCuQ0NFqd2zOmsQTLrGtxZEQAY7tvCaj8mFwUHutikZU7ZpjBpButgMUk4rmclBUO0y-pPC8b4zFaHTKfnGKRT5GSMza89hgIIZfCX6O-fP1kUsd24KR5CmZ40JLDYOScjXHtYmgmlKF6QaqEE1lLWKN1QrxBGtZnxKBj2_6yTWPk0o-KaH9rgzcdWhD5uakUawk2iYkjeBp-csxX72ENlrMixX8p5n4RiWMByWcV7qLDzXOcBvKfGbw-3fErwkWozRaMK7J9MyWri0vFyrVM3avcSNzs6p_W6a2jSgvcg6XwLjraBuNrXQd3WsOb2ub41TJnosaA1CeMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=IJPkJIHixY1YKVFN1W98nL2WWqL8wbBxy5D_t7kCrwGHCzyA2_xlTkVzF_tDPTzGicCCMypyGFOijTeK7EMGBUny_Bjmdmf47tlnxsi5F5xVhpF0j2JrafRA0sFmt0Sbu-MYSSrEqg0KR-JYtO69L6DiRrMSlwHeh2oXn8jTQS8tiy00LS4KhwvyzUlE_814tBBgViwscHwq1oTiGdIg_qAVLyLac85-Ht5t-6AQLaIMFliqvv-oRFDvgIsba5A3af6f7cohlDGuTl_O5c1Vs_H5ieUAvhr8o30LMlt_PDZpp9jrvsJcjK_NKJsMZdRwyCD75g6DaI8znMR2TXaZSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=IJPkJIHixY1YKVFN1W98nL2WWqL8wbBxy5D_t7kCrwGHCzyA2_xlTkVzF_tDPTzGicCCMypyGFOijTeK7EMGBUny_Bjmdmf47tlnxsi5F5xVhpF0j2JrafRA0sFmt0Sbu-MYSSrEqg0KR-JYtO69L6DiRrMSlwHeh2oXn8jTQS8tiy00LS4KhwvyzUlE_814tBBgViwscHwq1oTiGdIg_qAVLyLac85-Ht5t-6AQLaIMFliqvv-oRFDvgIsba5A3af6f7cohlDGuTl_O5c1Vs_H5ieUAvhr8o30LMlt_PDZpp9jrvsJcjK_NKJsMZdRwyCD75g6DaI8znMR2TXaZSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DaC5djR2BeXNNqVXzio4-rHn-CHdb169TOCikMtVfEHySHV9PfzAPXLGGxQ0-fZ2SXHp5DsEhML_Z50lh5rJP3YpU6nffNaSBnZkUGiJApZBF5N0ANtDGELfCsf3naE9QREjdA4Gqkaj_bY9XkZ0SDsV1ro0KRg78v0C6-I5qIzP6fX145lTSX5UMwoD2hOdImxDCT3pznkoi3pjlBn7KdHpcF5q2v35ml--NbXJOPDCnJ4SI-BOA9z2Y9MSSWKcv5SN8S-S3APe68w_XqGvhbT_nn3YpibWy9n3Bxod70zbp-SnQaEUHBRnzcn6XiOYa1gtxMHTTuWhr-3Gh2D1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t8eCxNjZxMmfWVT7-aRYUGDmJkLRLe9oBkc5RUv69I1GafAKUorV3-4x-bmvDkeR2eFvW3gptCYsbXb14-iGwttujbJRDCbWUdP-CFS36uVzCn4LxVY7-Wdf1NoBmzcO3YU-gMdF5Awq2Ht2sElh3QTRFzcDK5eACsCAM8LyMIomdJFM_xeS-cDlCEUxXgYBhvDKo0qdBVQeLJ1CDE3AsHF1VoqUYxkcLTW3fmJRbCQplhxSdiM1-Xkpv_U9iDU2GgXehS6nu5VoXMmQLNr-yJ3U2WawtCoPy0_nOgmAE7tpHTGraEFd-TRkVBKGKFiXOO2HUQm1oXf2ob0TQ9ijtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i4vpFoy_FhpHwqZ0As7IiDbJAALSd5AwgcAb4fG-iRUKgcPvWVYZaLNhIZZ3JXiiWdnH1LZmxdnHElwQ_rkK8ozxiv_aJnh0gJEMj1jdiLRch3soH-qGcg_eqbvtkyGfz4yufSjBPFaldtx2UYL-ZrZlmqzr1F7ajZru__7HKEtV9o7Fbufn9UiblhJb4VxqZTpKOLej29CyW3s7DkYNB4O3XkVyQwRITy8osSZ2g9891dUxu1fXJdkUkxFRGuMbCPkvs5e7aUVYqGeI9QIcHUm99nJ0JNoD6wk8qnfdqVS21Dv-ozdKks0JytKovNCOVIRPygK5B6HBmi5gwwwtOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2GlBiNnodIkwEUq3Cb-qxaLgZu6NhiqxQXg5i2BvgFDfQjar3PNym_sZipJVs4HRFaGDP0KClLvvjx6XD7bR6tlIGOicR9PoS3n9ATD2klqFaL7ns4tbK8MlrPkXx2y2mBzTRs46NG5ksel9yxE0c-rE5FmvaDG5xBKv_KmeRJiDGPtKvES92uNks5UbSx0m99Qg-R-5sVZmYSXqowZ22YKjEQfeOdXG3CLef3sPhvTBjFKF_X1M1fdEw_Ql5H0Ov06SQ_uFwcaejuxuJ595sQdpjq1MwU25yRaj9KG-9u-lPidQ3N6onc5r8dmOIHVQ8767no6ETyG9ldf9BB5Qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I-Q4N0YgvbRE94i8ibAzMHiQPHltmNLNGJmVJQ0xnsoWDJN3sO-7TeZFMpZ1sPg-4WPZ42NsIYVkgkExHQmGKCDd2y9Zr_Wr-3BdlkfBTaqDty7biAGTbNUi88JOd6UTwZBXDsEf9TI71ii2taolU5lSUqvt8QdU9KAXmlRtIh0bN-EI0OkyK80gu6wQLEBFAy5-R5gYlZbxCTAqaz2Rbr3qR0X2lBpP5YGK6D8ECghpjpexbE_xpJgTEkBnFU17EqOUaHzwTZaXQNhkSsnPAQdWMhuYhkkmEcLcjiCy1MjbTt_7o79yKzOi5taUnpByHH8ONz4u4miH5rohbDeJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XzSSzKItQrHsALlcf0cfFuqS9GzttMbJ1E58pwirfopKLiPaLyzAfTk8IQ91xeEzOLBQY9hl-wnEW6zwTYePN8OpFiQ8wqbZ6qWbCapfXZIMqfTJOo1u119dp3lPDzQgS_IUT6W86mhEJAcRkJ1VkW8hXfikA1mEAA4n7efcxPYVw8I3eVnLH5FBn4og0ChuS4hX4A3VtJVoojRvhx0FkMbfcLAmpRFniX-9K35M8yQmYP3YUQjbTZW6JWnCzxPtiAUDYX-rX1G0QaOMagF-q-146gqOuj-0q7-Hnxj0eVSp251ueJP5noZuzoJmkIZi6aGsBSFDujmHCBJVtxoDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=CyLuxnFdAWrY9JbciSTVoWdxGzwF6f7e3M9DEfLQF30VNR9LLBzXR58op6PHznnRdh74dHt7jtyzNj6zoV_XR1F2vwF7DbQgYPJ2ckh_FguOri2KB0S1rNaOako14clnXlj4vsqR45oeGD7_64H5FAR4sw3na2vwnGRTPmtDLXOezX-ojew-70numUk7aahr188buNf665IokEDmhyLwVSRu6wwQkgZ4MU1BiZnw5vmOavGwWqqv2D5txjFdVR5hlqM_LW6bLlTjjWfWRb_8MNr1xrNS37tI4spA8xIYgvA8AcF4VGeaenz1n3uab7D-jdztC_-QE6WMxms0Qq2Wnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=CyLuxnFdAWrY9JbciSTVoWdxGzwF6f7e3M9DEfLQF30VNR9LLBzXR58op6PHznnRdh74dHt7jtyzNj6zoV_XR1F2vwF7DbQgYPJ2ckh_FguOri2KB0S1rNaOako14clnXlj4vsqR45oeGD7_64H5FAR4sw3na2vwnGRTPmtDLXOezX-ojew-70numUk7aahr188buNf665IokEDmhyLwVSRu6wwQkgZ4MU1BiZnw5vmOavGwWqqv2D5txjFdVR5hlqM_LW6bLlTjjWfWRb_8MNr1xrNS37tI4spA8xIYgvA8AcF4VGeaenz1n3uab7D-jdztC_-QE6WMxms0Qq2Wnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TMDWHXPLBtA1_x4BP8Q9_8IVq5im51UA-lYXkR7O3ShBjg3sO03SgrkHXac8CtnS9uK-R4Ci2sR5WwvAkmH3mHBt1ZQs1jXG5Uv3tOnELgaUaPCFuS-qu0qR-AXyUzOwnHGkIr4e2GJLJ_1YAge-kAbaqkkKIyq568P2f5u10ESdoW8k5sy-kxKUp4kEz8rdT4LNXlUNsfCXHYreLKnID-DjoT96sV3_2A7tjJWGxlqfFkvsOgnmNCl9smNO6rgmjNsIuV2TKDQtwEZwOm_joyj94EkAVl7hC2XDbbVFK8jvmbhZzAwBjvIbNlZIthv3D_8TbTem886hfRWnHO0gvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AX7_L_8MZ8D1Z6rxvTGwThVry2ttMCrK5CNR24UL4BtT257wplZ3b_TTLnG7JTsMylgm3IzMJ3MqwX7V_QJRFMvhVaoY-i6GmacsySLhul2Chlg-aHOu6HH89rrC5rIl5FnY1SL1Tbl-4sYImiC2tzxj9Cx4aGuKNKNFxFQ5xAd0I7abEX7R-Y-j5_ILbLe7t165nEY2WdaIA113lcqrJzXMJK75S1qvoqtd0nI42KPwH_18U13EJa-jZlSYpbj93frnDN-jPtyBjwkaM10jmPVZQ626u53KrALOuhSGUr5QbRwJGZvNsBu--gP8uXD88SBgm2RF53qpfp_Xwfo5tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvqTKZpAcKvOvUqWOXwhPciE8dUlSakw1d5xNI54WhuKftgmmFv_O1jgtyS6g5WSVe42cB5dmSY1WWbKefDT79k3R1WF7elat2mFKJUnuJXOGp1cEb8EO44C3Vg_FPOlFjYNStux1seA3-zw87kY8yQUQTtzFnQgdYfzTTwISsPIzrzPMatwLkoXyyrD9vPh0GoAzOK2tXreTodwdwsagnHm2CVyHvXcv5t1LHcsD_epqbCF2va0ctbI8Krud75wteHnQxZW5o83_UWdnPp7gjvtdhQ8U8dDNTprXZSurGsusP3IQ_CuSwJvaAtWNf3vKLqHX6dAaxrauvmCOh22-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7YCKelNIAVvIeV4nS-QxgEiSHVe-ZIbmGXbyYTss5d7eChvnqetOYAUJX-XKiGgW_ZeiYk00GKReNb0LNjv49GqEwhuMYkmk3Ew25SuXgZZgYY4p3FHFvz5FM1FwPeZz0GxDuzesKzSJP9adqXel6_NBJ2oFpsJ5_NFBZ0Fhv73QJbVR8eRs2FhTxzHNqYWhm74GrbEjhDEA3WXPQLcdoT_nW2YTgpxM0w2lXPOxRLSJ9tOKyyilxVNHdwmdFw81mKNA3sdMDhnzNPYrIv3-UCcOwp5YOZJNulmEa89BsOE31yvZ4Jhj5K84rfN2VYJGbfgiwPPXB47zRBi7vsW1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BBd9Q7hh7C7qp_34ritCvH7HE8G1cMAsz8uCi4yi2LFY-VRQgGnFpxMI1Xx5xC5WUnwxC5zpJnVf0Bq3_IW9ofrMckK6Dz7m0joIqEwS28VNel8UAHlnbH1jtIXPwi8qd4d4tg-egIwZ0Ccntl_zj8RWBHY4oBSrJbbKNU0SxwKPiLt-SIWE53NG8PFyHUYrcM8wyCYP648lAYJ2dmLQzeR8pAfkt8_KrJQ3wh1htARmZ4KtFSdZwGfpIBd6GcHVA3_hs3hHIisa6PV_Dn9KDyIUMgBusELyXIrOwqStuIBXslUvlyJrcrKkSH4ldS0owN0XgBo2cqye_02-qt8Stg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sRU37hpUq0rNXBlPOQzoROM2u2kEyloGlWEggjUrnqhBklNqvZmXX4Npv2AexNAOTOA5w3Q2E2aPZnMxGvD5Pc4G1_2EqhSViw97PCFGTKADtGrICSo24NLIrlVqfcD0UGTxy-KnY7d-Pe7AxRGlYz_OOLW5Xdjh9G15IeNv019C2LxKZ_SW3UT7Y1_gOA0B4demuR-jpiitQjSYeacDN1d7fnguz4NQ4pJ_XkccZMP4RRVS3sMkAVCmOpJgx61qn-rU2XOEru6-fQMlIgy4P-u_HQaNQ8ywc9MzZQ38yBu1liRbO6lWBfNDLFwSIUYoj2mIOHTptZmpDsTCh0Kl1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DWe2rfUxYhkOGepAhpmhtuwrZuibYCSxyU4SB-8RO3k215foF8ISaPGvirfMZa9MyBFNeJiDCziB4rNMLYeF1VspRwHlNx7A_NRqq-Sz-tJEwSYd_TZwwE8c16xWRGXpJ06edLJe3tD4cYugH2_tP4g83tOCAyFd3CUB8gEhg5UEG3Ji13mz5CjcWNrqzx2U2hSEqz5b8R8naJWz7kVXVyJFvkoous-0IC5BWLcbLOSWSKfg45hEYD7Y4vICqui7tBjumLEvD2beXKFlo5dSRKBfTwqRS_85z5yIPaMjG1tmTq-P3uEjfnDr008qEuVt_2_6WMxYiwK2zigLvcHQng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vP4uKGl81N0vbicCigdf2lkak8U5NV3nr49xukWYeQPCctMDkl5kSrXECWWDF1g2gWupaPvglOh1Bd24m4m2pe8MhOHlVI2OkflzB67GlFmUqUPUO39o6nBRhjPWP91T9MhFtrbTS7ZlhWopqkDIGzbE_hN-f_-_AR4RwcP1IZz58g8HGQgUSdBidr5WYtjukAzOCRFizIrVmpvwMwcw8mDil3j5j5F_AUArx7Gh-kMlEDPAz6zHD7JXinPfy27E-iCSqOJWg_3SjHOd0vWn3LQOVnRTM55ECmdDGhwyZtQ0T8SCxMHjllxXXF4lAs5cCCGbGuNDdA0w1i9Ja3nWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vnTdGmRqw-aRMnDuBAJlJy459KEDInl_csjMwSWNEWAveStCcuDruXgjOoavMVBXZV7vQ_yefK1Q4jmxjELl5no06q5hFffd-qemB8NfjJE1Vqm6e4WX3rqgCsvngmWCSIAKuf6EvdyUcsQCi9zKpmd6nbOSvZiK6uNePrcvNWVm2zqdkIN_eOSQFc-zuY86cyuoeao0-RrFdYmSjm-glDjh7-fuf7apJJDyMWrurPF-PcyUzu4YmyqLyMnPyDe_bV_NaxBrBL-3hPq-SFDxIQ3hgFkBRJrHAUeK-Lk5A6gfpYVOGGhQjTm2axnLf3HP_ypZOO0pB6CfKqKy6YoXlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EcDP_AFGvjZnie_X0k4GXdXESzv8-fkOf3JZuRlDQOsWNU39-0kQoMF5PXrp-w6d4RCNTWR0P6ZH6H61eL6dt9bb0RJtWIyguNab4Uj7Dng5X-DAeD3hbg7SiiZRHF4CIusw_ymFsZx6ZKb4MVHT0dxiFhVYUxBQiJnhn6vqpTOjZMyAhDz3tpn_odhd5MiDhrVZM_xHljThPkz5r3C8LR6RbDyxEFqfXA94MC8DUjlIm_2Z8VSooC9Zt0IgYh8hqu0_uRJ-JugVwEcbFCeijYDf58N9PgDMMdaLUNp5hqQSGsbp5FnxjjEkOK4hZuxzfDjzq0Pp4IAYOk5R1CPiKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tWWyF3oZjVK23ArjxkXMhWTVr_qkfZUKL1kjrJdIxS4edObhC36kzQYmz-xbjii5yKyTTsmjMX0xkGOBSnmIQ8UPRVZ9aWzsptkOON_8dn1HHUudcFXu_6PRZMckq-wStkwVRfGK9tM0RJngpwefw3mOsE-NzOvOqecROwWiiVfXyc2zG5tsRqZANsbrr-j1H611YLuzSMPeWeKh0HxuHxDh2eHV0Kz1iaXwQuvcR0EYKXm5tmBROsH95XKX81FI5w_-YTJUSG52bl-cC7T7yyquARpsNqrP4ZqQ0iT94LFbNO_OyBeiDDc1b2n2MISSUXVguYWQlImmPUGzWHKGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=kSOhx42B62L_bIUO_44jeCP5hMmRelWG21PEBNlBY0xiGZ4GeNvdol9oNqhPNsaKCQeKmZDxnYgXBn_aJ_sb7wZxFfBGgxhJYo78foqsWC64W8EQdMILk8ySa0wLo9nOo--1W2K-Oa0fod0rZX34--lfWmeaWk5J1wNK6BrXdel9vIrpPgyXO1RXrH7PRyUP6ohZitvukdhucv_gSGtq6ccGh_XKMVVTY_W9oxFiHyFbFXS0Rg5ob4ip3G-qYHQpw7i8gtlDD02kB9qjcF-ztVWWc9m6Q8XXsgQlLZiEXwKAHQ8r8hiNLf7hrEg76g8_6uESCRoYU7x2Si9sJSP2oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=kSOhx42B62L_bIUO_44jeCP5hMmRelWG21PEBNlBY0xiGZ4GeNvdol9oNqhPNsaKCQeKmZDxnYgXBn_aJ_sb7wZxFfBGgxhJYo78foqsWC64W8EQdMILk8ySa0wLo9nOo--1W2K-Oa0fod0rZX34--lfWmeaWk5J1wNK6BrXdel9vIrpPgyXO1RXrH7PRyUP6ohZitvukdhucv_gSGtq6ccGh_XKMVVTY_W9oxFiHyFbFXS0Rg5ob4ip3G-qYHQpw7i8gtlDD02kB9qjcF-ztVWWc9m6Q8XXsgQlLZiEXwKAHQ8r8hiNLf7hrEg76g8_6uESCRoYU7x2Si9sJSP2oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ngNPUhHVYW2AG0qpgamO0OkEM_8T9dtTU2_r70brQ8os3K1rtAfkGNU3kmCtV6CwaDp9ujFrFgYlKikWxGNFXHcXQ7Lf-ofr55QBiWL5cHBD_KBPUeYHFakvoifYUIBkZYzctxc4Hf77RkhJu_ZJ4T2zEphQwIVd38pbSM4k0vEeUE3quojfMIi1b44X6ngEHNZ_srHGVvgP2FmO2W4IVRuChI0ZIT2HHsFbCdPLJJaB275yibIPCnUt8ZvHh4GAIyvXYaQeM5uMAcIY1iMLJj87nohf6fxcjFNhSFiIhfVEUbmi7qlfy1XjQ2eiip9MErqWpmURwi61rR2BhurYOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CeVP4R7aWd5_sVv3fw6dFSLvz3BWKGq6nrwh_0eFqWC6N2853S4iWK5W7aoXtW2cqxMlxhys9E34qWTuwPUIzStw2q4GZQ5GoNYfj_20CHIv9OvSw_TbNboHLKj84T6-VRUFxPEE5iIOQe-QJefsHPzixRU3hpc3Cg9PH478ALEae7NlWm79U07SrFqe9MZdkwp2iYWGH_GPie8hzuofNMLVMr0OaovQQLxrvz9lzCkhXaDD4knB9KTh5wH_X8p56ssuzL-CrIEMLu65Dr5DFNEocan524VKvJvmB5K0RYmGJFJen1HXHuGv6_SHjL4bzXujLAQJMvTsxYcW-DRY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_Wz3cszrCZ50GIzxc1SvgwEgrGdcJhBcn8TxWx_mEKBVJhyEx3dKTronO01PUD7AN7elCGNSGjbx9TJmIVWJ-gtntFOcogHns7USnCHb5KpDYDwY17aMXoC_QDQSLQ1_YP3SBeZhrDC-n-hf9Mf3f9FW54nqA604zbZqEAPV6d7K4UVU13-b0-eWHDQnDQlk-C60p8okSSwZ0ladiZvi4XaO3eTHYoKZcIRGPeq7Oxmr26Vj6623C8roJkQoV7vcVy45Xb_9idDJh7SbPMEraiQ3z0uyF4Rvwwr5ajccVNHnZ7OzD0nt5c-xcvuH96-D-ggIHk90CFVGLe9HqJcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ov0In29TahtBHjGLYF8d8SFGHg5U3Zbt_xwuzH-E_-zJI2--MZQhC8loQYIzXosSFsa6HD0ZggJuQ14Mg-AecCcnTPe0VYf1VYfVedpieE8ePrqwBPI7nxawQc32u4dtzvBSLlnw21-GTZ4fHX3ZpHb63UgIiTedcygIfy5r63G5SrsgXH6L9ixa3TLLjopCmqzayLN1ug01_z5Gv4KeJhLGVdLWzbzVnU42zquwg2xXd-Eit2ls9BjpSNJQkwxXvAFMOYmn1NmO5odDsCWIB7Wd5b-bS5R9KmQK_0uIt6qcQ4m6BTRXlKcXIwSO69wXNFzh2rCRN2JD4IOhYatFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cShrWg-qsHssYro6-zm1vyNet1jL787pOMmfbrwDgPhpBng6-ePNBByRR61Pf45vbqPBIv3yh0YSBmHUjUIW4C3xl9x9WVbKvdH8fxQsm7bQEre6xm2LvFMkTAV4wd9990mbhaAMhaSK2tMMbT4lqMw2dZNq8EaA-_ebK2VMKoIx-MlprjRot1TXUj60jrplVuFu17ESzjMg2jcCZANSKVjCq5r6G7WxelofXrJ4fmCVJLIO8e8SD2ek1cvuU4MqQLepmyUpEDPspxS2RbiLhnlIIeHKHpVlNrceFu4PociP0WlPB9oQXxrwbYSw8HV0JkBiQqYQ9e4QYbnRFszUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dMsd-pUeIWwDv98EK3udG7zO3qd8KWntTbKcWT4dsEHDNmn7F304ZBuQ9J6RSxXiiBIhGyYRVK-y-W_7Z88WgYzUc9CDZNtHZEqBeSEGdcms3H-6ek_3dctmAz69WkfW8o6lokwIkEI_MTxROdEDddsjrnaKxdYeP3jABHbZkkuS1dimZOPpi7xuv2At2zUjdOC-XC99lpmauh5PrnRtu_JCKsOsNWiN3dryTwf16ZPeIsNsCP12TRVgwXZK_0WzXiftT1U842MzNci863IR7PC3yqsECc1gqcty3kMmDmO9g8tFa-7VcRllGmwDff6lLA6KSFpi_YOMroGE-uY6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ooPAAAY30412AKvRqNt6eJ_PoF1IeArDKJuXqTB4t5znphCtuQh0pv6a5jX_5v9iDDPLjv--9LJrWIyvM-ToWCOpHuJcCpz9I5YtmQEmGp_u_doV5dBJe8HlPKwpGVPrM8vfkyOKz_W1ztltDcc9NqZrVonUcOa69_TVjWTW4QqrvPIqn_egR_-LM6UMVPaAPIMTTOuAM_ovQzFXDIeJ_IUHdJPp9gnOCTWhL3aT-J93f0d9ND1MFsgJue9y4lbKuIenWFxLmA9Gz0dnXbIuu7GqvyVYbPQRJhfvb_YrQii1zfaYuOmhKsdFCNoaX6lidMYoipZ5ptG8N5B94epM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KHHEsnlt2t6tWAtoHzLro-nN3CQodvPwmHTyJ-bl9TL-hPFUvQQOBNymJdY9dh1y3HBaZg7qcdcUuBU8WoOcq_vwMaXIFun9hFmaIADGUONGvMvCicuxss_jwas-vE8Inz_mXFsFICai3FwzcfK5m478AOkeNmiQ_F1BUWepuMH7XuY_nWuVrCG4KVtdGsIXVJQQ4ooqkG4IKqIlZ496_EvOWmlYeFjfP3536SnQHZM4Fzsvz7Hk40cBoHoZU8hcTB11NW1EpQBNJWua3-36eS7Y21fVBd45yK4TuFQwv5JW1lnWZzL5Qw2wgCOJo7pz7g4p7iCOO1NkXZZfQwaaWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pD6VfBowhoUsLC92PGNqEcaxs32_poZUJfhW8inXTN3vIbXfH6YQHkXL-FoMv0VdLf4N5AO9H1lbkp1O-fqKTviBc41dF8ixVwZzt7qvGLQKuo4B2d-jWlB0JnREyfMtJBf8ZI7t-bwb4bLH1EJJSNZUDo_BQktBO8zX6fhAePI5aFIxRSRup8ncO_LmwSWzywXrWWgXHq9xpBNmx9meiSpzGPx9cWNhmVx7K-J-f-hdaNl-1ZRRMWRXQVf5sLRAMdT_vyG7A440fD5uyh6c_w8ODk2WbrkydbYWl_47h03Ecb17hl0re1flUSXAPOiTAUscednFSqDa5ZcvmxaIGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K87qzfaCGl85AcdNGzxvjlayu5HCS5BTCFX6vzZnbtb6EEAw4XGVzUOwbkapKdJ6y6zeI7gJud0hRHVo3Az8oUIXuaWGZBpukg93vZc8FOFwOW_RJhi1cjLBKNaun3lnBkUlPG_t11HdNXneHpMHusakxlcUbuAX0r8fsrZ7FjrxJnk6xVa9GmElYN1MsEbKLUtW1D5qoyK_6sTZdKvsbHD-o3hbHblt414baLS8eOBpeZK-TBF_glc0oVaPqPONNyRlRo5ACdAUhwP7GZMUlTofsoAVtnA4InZbzBqvQyS9hdhbJGlMnME0wOjjMGyD3vbuDA13dZFRalk0t6cIdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YvM4pdW1TM3OtEQRF1ZnwvoKsGvg8JUlSRr5rnP3bj4FZjRG0BNXOPpCU_NK4iU-51hYN1jQum2zDg5rhh1RlU-0V3jr1T8jQnM9h9QFZm_4qAfUaWgYk6u9BdvlxjHFZ5m8wj4OyI4khd6zCBTI29dG6VrPtydE-nxOem5VIXtWjz_GkiWdQdcNS4yTBcgXowh1mDexj8-3i_X7YQrxAQWosQ9SzsQx7-3sqToelVA90JWtrdyJuudHUyIbV_DeRRrgL_-1A68jDN9zkpe8E1XyuCIzMo8IlOTwufTZH8xWkaqGlvsF4IuyqKiG0JuJZIXR_ALwEELbcoH089QOPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FOSsjB0x-spBEGnCqgDSMUYP1Dp4kiDetuNuyUAUmyWzsg64wkDuCOoMuoc7Rv0VkgL-m18zP_F1OFS1tCUUxOHfzPUbf7TXCMqZ52fBxv0bMwHoZx4mUWozj0DkGlHMESyVlaVwqiA9Wqr7mYAxHds0gRCiRyGws250QtnKfxDiGjJWon6HhZvbxuk09wf0CJ8G2qzVHHq4brm3Wh8aebDq_ICjcr8hangCF8Y_rZJGRrS0PrzUUxerSqnb2RjDv2ZuwC_4T_jY0hBG67BfhHnc8kDymQuWWeZSy2TnA7VhURgPV0H8BcvJwIj2kK_uyxOYWi-RxRcbFf0Nn7Ch3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UkLJIuFngAuSG6P_nYvwxWq9Q5qW4sjlmxEANo-qtNi3bwd-zLL0bJIX6uFJ_Lox672H2SLWWMQiX0QoAGZDPy8uojng9uQwJRNKvSdjb2UXvQWV2f1Byu2Fss3_9QXWJ10qbyoj7cIT1aouNmrF3TjRhiR9C4sZZdPgCNoCDOLsGwPXSpuDI_PlQCsi18832XKDbQ3ynQCRxdZZ8VKQBBFmOafmL_KJ9Fu75GUpAI4-e36lmW47ATYDlpyr4k7n4W6wH7MWPtnhp-NEGw0CpoWoGpGrslQeVt1S0MqFk5TDPyxfHgPd628cy6dwXrW9Sr8gmXdsOquZaKrrTyHUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t0hQ_ODK0tTViIs0kZq0F3kEBBp6IzfJZMQhV0qdzpvNz9IlJp7Y3tnwZ9eKCsjOXg6rb82gUFevLsK0U23mmCrnvB6tS9nB4y4Fqz_nTH9mLrnH7tRPvUZg_38STM_P1gUFl3mJhgCef3mxUTGBhQEl92vSJ4kwX4ESaLFs79uCUNGkWpyQ6lZ0k9ama1zsKpHSZCtG-i4WJHHLEk1fKIP-Cfn7C3NRIhIiRZUNyl8FZTrOxFk2Oa9UMDJAUvF3bMt4Pz3GQ3LaWtYDHRz9lwhOeStj7MGI4BbkMR0JJpAnSKWWsS43L1DF-JfuNEvMBbCTohogG_WE1lrjMaROHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F2GNEMnZz3qaD3rB3XaFl1D3UGXG0Vtl8lA7ENmfVa1FwfhYHLUEGoPXM_3HA5pZ391587oi5bIIyKEE1CZ0n3SZPr1dr-bwtc28Pp2M7FmbxPD5GKHV-5T1157Vg8ptmKlqDF09fDLvVc_fMxoB7FBNR6V0wxiaak5sBhReygyyUsAbKBTqQpjD97ehwgx4S3LD_9XpA8utgS7OZ5GXxKaRxvlkd9bmkmgbjXwEPKSbBeXQBWKjDtZi-IBNoWK0Ceo8amf6XUaZR5npVachvQjkeTVGvFs-cbH1rmGrP3yAxaXg57y07WVsZShzWUfO3-fUb_iIrOftNMtFOMD0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ra7lpeinaOOwbSyrXM3Cw8DdDI7UFkZ7pF0qQSaTwV6Y6hxfq9ujXsfgPxpMEqTwuAdlfqoC7LayL55bTVXbfEoliVfiUl0OBM9wJ3iYuXM1TSMnXd3_BoGQwWm3TxxqnKdZ3Illbz54UlU4Q5jiQT48ZUr1L3-0GZW3aJClP0atnpgHVlYF_6tu7OrFKhp3KVl7wJLaJaMxbhDZM8LxAmdMiW7EoDiIDTTM1ZD_UETK0WD268LPZ8_5JED9tMo7h219iEBa8x3qFQDoqoYwJIYe-pvzDTC3Uj6Zq5iIUuykJHD5FAjoc16XO1F2ICXNn_xlvtznyclT5PpLu3q7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KAYwI2INY-ddSTJIfTHhQdejqiS62Frj9VQOHOtbUx7qYhRaqIYiVP-5o1VEA9PcQDvydEbQG02G1wZVe3OPQQG4lxUx5DvmATYL6DiiPc-imGRkmbWwq0fsvWsrHVoc_zRMg3NU0FUQa-3m6EXpeYkLGGmSAtT9VFUwHVxa9yqaRkGmi2JnVY4dyBxIPIb-AI7ZDRybgNhaapMHV69oin1f5fVF9gUgIgY1Iqd5n_kMMiDgdHXLuXXNCnVfuQu7uDEZzbE21Isw9QlbkQRmPo92IxopNWLuBySHm4UP5yqb94OCICPhxDiCU3lIEDs-9x02jZ6W2hxuHkKskOHOkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VwDmopgBKcj2dF0ZVqDwYTVWlsUaKXC1d-QY5Om5ytHh6m4HAfn6zDQ-V609eAzBXp1Q31Lp3BespOyWmCcCgV93Tp-Fez4bJvzYfBeWCbMhMxDLehtFO-sAEPf0FnB1Sk0l4gypfkQ-NT7pSZX2F2g7MPLqceN_z38-NxsHLb9VwXIIpuILIyu3vumTs4qoDYeXauWP9SrTa-_IiWA26Av1Io60GGMFVCAQwMS1fab5WB-GSEhlnOCVNdK2B9cDyerKzZsWHsXK3Do4xnMLHcyZ4-30gZaPgUM72O6aFoEB-jVsjdnlH_Kh6Bq8gbKSyXMRn4yVxNMBMw_J9KLc3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DfDW6Tm9p_T3XKMRVLQtSbtJFjnk25uUVERmuN_k-Vixix71jeCHOAphsFA3QbIFTNf1cBGUu3B6HmyQt3B43p_96Qv9NesjuBXjbPEf3eM67i2l7t6DZsdemzgs3ZGalgG41fOyw4sOmqdn1a95oJO9hg8fyCLZN_TYPHRwcIf23cLRSUPxRtEU3pk50mVGO-THU4iZEMufG2gr2rPFWHmyO-tZ1ElaMyLPTMHZfqhUxDEFgZMJPhNuC1-K0vs6JjyqK5xHR5trgWk0RyGaasHjEN9DhpjU-s-u5SP0b4s0_y5NuLLPWLdfZ_AK7FqCA8yxuJXN2n4DwZXEHWLUDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hwSnre2iBdHZ_4sI4xyOHoOcAb9QmDEGrwjCRlUqu_DduYv8avzbQ6eyAA0-K_NxBERw7zSSv4u7im_3BKiTxNokV7idvjyE9ioxbU0n5M1fEcFfBu1qFRF5pWzpPdndOfujE4LmHZbFYwDZMqOUPCXR4dSgBUXnHSoaPshT47eoD4S2CMel4gjBSvNjU60LhpDw1CCyoxdxORiYcSOiCd5YNQjlcJTjDz5WYuKYxlDw0U3iKGH910R3SPyEmobXoTmHvp_1KpViCxmZYiuWGzPgjwA0eDI8OJpJvuFEuxPeRtl59i-4cYc87l5Xq_wRBywEvw9YqV1CWFVx7EcBvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vZ1YeeQiIesV2Pt6biiHFcszbHe9Y26LZ309-eecQWct9-r0p-3dg7rf7_gdtLoUNwW53TA52OabzKDg_sEHqG0FO1qx7FV5f7Rt6e7KhiuwEshxwCBxGizi2AcHj_D3c-LIQb9iI4diK0_XM5YiApx5OhDzl51UTv47XcUGuSeXigbtWLJhiGNOj1tELOH6S943lZIYVRH8-4chS7EQJb8AFLfNKBH2PLfkI6-1tmRH1T3ypKpCY8u91XP5jzi5hDhJkcB7ULVWgZ82waPFINx6OKZqS2ubSiutSK-FZa72-Kk2RgM4Bdn8EwwF1aQNlfKFxaxA6oV8Pi7vsiRzzg.jpg" alt="photo" loading="lazy"/></div>
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
