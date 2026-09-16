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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 04:24:08</div>
<hr>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FISAJx-l7Ghe1RPYuC6Eq9kGG1jTBPHkDkX246Hu8fbzHUSlqh_U0HHP9JdcLloFfgzRslw9ImXTGULx_1H7bfRTIF8YGQeipjDvaJAdQHySw_dzkpWVoI2Ia2hHXkGFwMTkzqu02NlYugfmA5zcN6Zcm6fAfI4SLdRm0sMRMI5ce1CeZE0gjRd1oiAB4_sRu0FuBf7tLXxKAuiQA5vhswgVU3fnN_AhNvx7wTKRObyW4QG2aXEGg3jIFx9iMKoYGZa3_BiHnx82T4lA93XV3jan6CPFT1Mq2uhlqRQgvQ8DoR6lm37ftHn0ekGlLnIyHWw8y1Cj2BnRmv5U40wnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ohFdT6YGgHSFGDzSz6Mrk4zRzSdYbVJjGQ68p9AR4zDW-LuxiXoFv-kLVNqZv3XIP4yhQO2284FVy1cZ5FfuuWr19LjKkT0vniA9IOunfZf9YzYot5djpcQ2REFJU--GAlirTKNYmu8sNJ7dFfjvZAyWfbkaAkyyogZQDjyrPbCLe0J2ucORYZRp6qGLfBF2MTv8KlA4yWlP-q9ijyisFfG70GkQ2geFlwdH-1ewgqn_MW7A1qx4NSyG42s274JfjTUGcTdeJjSAAvGGyRLc2EMNPmMjjtg_3O--F0Edaanvd2MXfIb7H_aH-fkU7TZ477AwYNiHeYC2sywoL4PM2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ooBS9-5IoVc7dT4DEMrw_I5r6ijrjvyikXf2P3LoOqW9XGzS-4m4HbUCiY4hASGrZG75R6WNh4FIe2F3Uo0unDW39uNpyePBeoekdkdHA_fSP44iJ98Hz4yKXtA8QKsKE_UHjGSEdMnfCXUBGfnoPKRwPWLOPIQna4phd-XmZRyiXSS8IE_f7Y3cgano7xqki2h7dvhzAjLgRX-OgOKfd1GoqZg9oQhFKpRoMZ6-S69uBIL0ywQi-UdcL9SVEBkudI8YNEDtpGZnSvHB618dkhkwlDBfMyssUNgaLy7_oqsOKj3xf9avaFoUtB2S-f0oGpxiG3Gta_NfSPYYmW8EUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q66HHV9qC3Zw2d_w-O3R7rWOSWfSMPwGJaGelShV_p3LC3BudYo_p0y3AQljBH4CVag3IdQ4-9SbeqYqyZWH_zD0-RLrzOjdKcXrf9pUTJ4STHhjIpSg6dCL-7ywabn_chlkCQ6PNlROxgIlag9tlTKvkE2s-vE3JH5zxJP2BNeDuQTR_a9F-9PCZFErqBhXKMHqGFRBih_3l9qT9Q89EZZSBK6xtp8oA7kZsT8UiT2xcZ_L8jjVSZI6X1jSRzfV9jdq6wK3wVTbzUBM_mdc8mOSZKvAwxpvPQ1WqRR4ijNZequR-mOpqJr9yaQpIP1_BlxBWsPnoZAQNo4Rr6EJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ud-mlVxuJ0QhEAIUSNQXxoLasY_V39R-rNOoss3nUc1W-I8gLOJTXM6wKSq_RrPJpU3b1x_c7a1ZffP50Vr_acrZJ_OrRBwR-pgyZYQR0bdas5lIKg2DA1fXvzxh2phFXJ6jLyJvALFYKrROAR0FSzWQcRfUFbvrxjuf6LTzXSm8H1lQ_Iqi7iz9SoGpA3m-7w1KfN2XFJRSyX9aRkCttOcGjSW6irNljyTgMJOk88yW77v7z03nTQvjAjF_Rem91w37NxsClS_lBoPm-uBm7dqehxODooPQA-m0Nl_IXTedPFDBJP2P3YfiJF6nX3Ttq3cMDssaNI0WYqgiQp9Fhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JVeUVPg-T8ebvhoS1kvQFzU-giK8jC75e0ju9ZPnJQlclZUGW6mlJDz8CuArU3HvYezE1q3vO0NFFEkrbD-x0Z7H5v2fL6LJ2B6Cvt8SN5di1k5T3wys1vXR6A2ALvbfsTnhgukmFOvabrM1BGr9jOcdqsQr1RT2hVcJhWWW8n5ApheUe75QePZ-hk250a5Cja5s9RIuK02r4GJy9eIwOdLcg3jy9ryw92O0SR0ccFLEwK8w0JEZreYtTZKKJOQKbY9WhR3cn2php7xAssmOhxa65slAwUDhZgEBAvVrJU0YB5fUfdmLyomfBM1QoRUKD8-e9rd1uLvE9iN-Nhv38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AN8oI2FZCQNrDNxjnvdQyQZzwdNxLkKW5cs7GkywofBBf0IXIlzr4avk3CnhP7N_Wfxw634XdoguCL3Vt8e-9l8v0QPK5acMCmIPNqZMqJFs3Rnx6AQ1Tj1YM7GUYr7wFYqzCfJH46g2IdDGA87uuZRi8JWaopr4Hli0CtX2OdpOscqOtSwdvn4QCD9oLjt0m-jbZcOHXoaCXKGKyslGXbIfQKtTyXCgHUcnz0HgF3VzaCVUKXAJKY1h05ce-Utqy2_x7ytfRAYs5X2lzmpAk4qFONpWDyAx12CjdN8rWZ6LlriwsWAEDaRApeAo9YyPJ28oVvkwwFLJgn9V8hLTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eELcmFJk3R0qPM9MKaCHEdlZTTC9sPmT4bBaWN5P3IRkrzTz8DmRFpzxdMojY3Tb4r0Gj2yV_THK7bCrsuW3cHaUM-7o11mSz6XBehBqGafTJRu8HcmlpkZCQ_BDM9Ymk0NuAaHmwJ1LLTewo_L3gteNMXh86oVgywbO_iw1SHva0OyLoJCfvDHb2frCC1BUDhxSCIfU3Z6gmDV2aCmGNnTsSg2oTthrlVWI7rUe6wkUmqMNZhptS_hKQMXkS99XLr7LQYTvYyPjvLBamzWVNsQx0DfPU1tLU75BeYJg6vnc-LTgXNo1E4dL2nPHtSa3QzJTh50Eyd6O7rzaGY2Iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jYSK_bzaCuQ0NFqd2zOmsQTLrGtxZEQAY7tvCaj8mFwUHutikZU7ZpjBpButgMUk4rmclBUO0y-pPC8b4zFaHTKfnGKRT5GSMza89hgIIZfCX6O-fP1kUsd24KR5CmZ40JLDYOScjXHtYmgmlKF6QaqEE1lLWKN1QrxBGtZnxKBj2_6yTWPk0o-KaH9rgzcdWhD5uakUawk2iYkjeBp-csxX72ENlrMixX8p5n4RiWMByWcV7qLDzXOcBvKfGbw-3fErwkWozRaMK7J9MyWri0vFyrVM3avcSNzs6p_W6a2jSgvcg6XwLjraBuNrXQd3WsOb2ub41TJnosaA1CeMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I-Q4N0YgvbRE94i8ibAzMHiQPHltmNLNGJmVJQ0xnsoWDJN3sO-7TeZFMpZ1sPg-4WPZ42NsIYVkgkExHQmGKCDd2y9Zr_Wr-3BdlkfBTaqDty7biAGTbNUi88JOd6UTwZBXDsEf9TI71ii2taolU5lSUqvt8QdU9KAXmlRtIh0bN-EI0OkyK80gu6wQLEBFAy5-R5gYlZbxCTAqaz2Rbr3qR0X2lBpP5YGK6D8ECghpjpexbE_xpJgTEkBnFU17EqOUaHzwTZaXQNhkSsnPAQdWMhuYhkkmEcLcjiCy1MjbTt_7o79yKzOi5taUnpByHH8ONz4u4miH5rohbDeJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfgxHm74NhPPoD9B56qr_bu_HEFLqiPVeqPZXvFVK2Ys9L8zSysBiVLf3NE3cLvoOOdhvnkTh5k7JQWAlybvcWyDPGe8FiMxncuZDijbx9g1V9ypHzxY4Gu2_YzwKHlRtCSx-d78LTtqTG4iEXZDKlMOyZVBJAJqoyuHNsPAtECD_HZ94qh8ZeQvCMQgYqIlkiz1vmBsuNCTs_EgMGD7lxqImskILuIHFVq5NI2oYeSOeLBfbylJ09sB6jCeaPj7l3qrqFpGUYTm_DJG41SkYTkrP5sWNoNQ4J_YP0RwQz_GSeINMZsarcuHRCQ8rNBiMu7BgG5jbm6NokdidVTJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jmnLaau0NciDjygf61vM6A1aaqOe4wXiUwEgJyiqtG8I0p3wJjbABXCTYpVUhw4VW7X1B4D-h6_NbSVp8zfsE1IQ5O7Ub2W1oqGsZ1VOfLS-rZ9Ue6FhkfEsDfxOs-WKyRBbuzqHsWIaJwunB7rAhKQI7rkcZ68VxeFG1eIkXKoqjDbkd0LVGjSP68C8umMf3aL-Ox79wJf__Tp1qiob6gLZwUx5e-C9vva25m-uVcQUUqviB7MvmEMNpiFgIx4bt1Aio8T-HqtigP3oRtaOa0MDtdWMgdKFYgJJJsggDajSiXkLLA6FeEYAD0vgLtw_jFAxnCXaQD2D8VB0CnwWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QCfiweeE1d6RraA95vj-sYqEjeLJcdbODaJZkeMr8OaxOT2V1VgwdoWaJq2JpJUuEIuhF9QzZf7_vjJM8QRMrt28qHB3z-WEyedPNWcAqApLWUQsZVrtlWWpq2PvA17WhsKE3IHPSH7bVxx7V-itdKVI2adFgC5jOi_3IzBcgZei0DqBOk_RKhMPFiHrreElPe-AV8raHMs__8EJolBzUaUEcAKO5ecZQ7VegYFHYdOAQu1yagwMSxgutZBMZ9u7b0rKWp8m6yrtsrlr_1Wp04x5y70bpSv7nWFxZwEu43Rkkm2bh5lj7HimFfP7RrNEx2cDs2VPlzO44QxrgJKhSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tjLMU28529c1MSnDVHjlg_06pBnoz3qShodsCGZoQ8-0ax2bpOY_e-wfoLQn3sRcDFD-TG3kDF0nDoH6w-R6df-5DUAI1YoefFClSSkk4NcpKs-cJ5rP6iFIEr3VxdYjXGdxmBe0wtslUwEfFxuDXyYcfY4kOBg3aegSaCRh_0F03xGyQfLPh3lGajOt0_i4995rqpy55LfLIpq0VAj1ar9HuSUiH5pKmdnfa0k36rZKyHNdbms5-zx1WPnZrcrQE8iRZW8YGkNHd46JIeJgH9HtY52O7gbs44xzT3cOMckTs8qPU3qlLcSJ4iM6QRxW1gguKrSyBA1ro1f--z-ntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bpO7kfHDkouNFd24U9IEvnTRWHUIW6dqDx7SWtjO_-eHeDkubg4g9_vSlZYWR9zqcnI5YwNV4AnjzRsyU658_9w6cfy60cd6yfWurfddtvezsobdK0E9KsloVYB9x_QlGQegaPtOMRL8uv2-XdKvoTHL5n7_88FxwvNx2WS01XRChvJuVLdVphJlNqKY3Mh-hwYBqzTeP3oHenMuDFzY1ltIcqWcym365mXq4SyXYiALoqtUJGALTWlVVvQ8pbHcKW-tqyoumH1Wrw2DTXVBA5f-c4wMFvvJA_kQzX8TK8N40NyCz5vVGsocKaN6Xa8dfz0BqD8fg9cxU0FYC1_S-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z065RjrnEFkUls6wm_S6ZKOkvwNoRXP630eqUuzyuGMkauVHXOw1ayu5alLo_Yt8juBeHuVfdnje6UMy2RpdF71TnunP7PkAragdeFk2slVLbx1z7Mc2Mpsw4yq9TZWF8CG7w78iZQaBoH4TNirINAVrIhUTK5TmlJdSu7J4rfpb9DEqYmNEabAxAjbYSf0cgP8bQwyWpdnAcelh564dEEIgAiW8h5ivBENqwhPRVwMZjeOxEkKXiYz1M5etB8IeN8u70Ul2dCUECju8EKrj_1FxbNfADeZCTNbLQPnbGQ6O-pOi3fPhIsal4CkzJIN8QVWmCV97zyyzs2BttPZdNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mAC7GpebyN79MOg4M12k-dT_yDkP6l9RzMRux2tuhK6ky-eyOIdZZ_PMsepp0K-px4VmT0u9ciWlxHsCezQl7ra65N9wluQ57hdx-2jPRwZrZjMYnvOSczz-8hRctDRllFsfxvcalzOIi-QpabfbP1jjOPbj0bw5txbCJQ83NUNzL01Ic2QBfKJQfIZGUtjkzoMYzObFMeM78KsAjxEezF-c8zrdR3DXg9s41vB0Q2XiJPQ8rb3QiPK1rFsg_pqHlzKvRTnwEqPNvAnCktsS-9YrSu9xrfEwcE9tJBc-wDhrUEWu8Y_CC0i6Kwf4jzOap2EabMBmsOyB-GjuIz698g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
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
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=mKayJBXugLmtnIIsXTtpxeNJBjWS53D_J_axdXzPQiYTL2OVbO7Hk_HeFw6bsJhO7zYIlWiPt-BmSxRVtccuqcayZ69Ibovh54kC_8Yxh-mW6oX0lvA8PpvX0nm5WiAh6_h2CJs95uhVERun1Yj_-3AfqiR8gUY07chWI8jh-sQlXdY77hPp5JM1gzJ3ahmSoakK7WkS-Mae30DOXR6wcJ7vrNuEd2Tm8CDobHfzslI5vY5BpGgcgyyUfz228V7j6wXuPwpkM3cCMtiaEXGYSLqlMh-blEuYMaD-OOxKmpV0mNbMdtEPL8fTgwrUJRpfgl393aa40K0jv9KbVhVJpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=mKayJBXugLmtnIIsXTtpxeNJBjWS53D_J_axdXzPQiYTL2OVbO7Hk_HeFw6bsJhO7zYIlWiPt-BmSxRVtccuqcayZ69Ibovh54kC_8Yxh-mW6oX0lvA8PpvX0nm5WiAh6_h2CJs95uhVERun1Yj_-3AfqiR8gUY07chWI8jh-sQlXdY77hPp5JM1gzJ3ahmSoakK7WkS-Mae30DOXR6wcJ7vrNuEd2Tm8CDobHfzslI5vY5BpGgcgyyUfz228V7j6wXuPwpkM3cCMtiaEXGYSLqlMh-blEuYMaD-OOxKmpV0mNbMdtEPL8fTgwrUJRpfgl393aa40K0jv9KbVhVJpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZflAPPNJ6wdg2WA8Z3mnUdttCin7jhPPLJl0ODf_Y5hufsH-9vOYI9O2mDcz1fFIQl7EJ_jLvEevqI4vMDl6WiPgjD8wy2WTVe0h1v6zepZKV4WJ6rtSLGRxyRHPhABVSTE3LfDsjkZNGT9DNfcvUqdDzlMNZrNaSlKd9rVElZEFRFQtM3GFvPekTBRolVHHk0lIhxmxQexVIaYDA7u1mvqW94-xDU568jdpFLoW-D6dhrdYpfcTmaBH4b4z2_Z0_FQM750LjnWR2rqSUvw-ESvsPuVHfnJIJCpv-V7NPivUnV4KTIlABvF44sOTdrXBuq5AS_rQtwMcxBBw3fwucw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uDqvr5X-1ThB_7A3Z6kX-o75D9eVw6zwRa1EO_OYgAhesJOpmCTqn0go86SfR74fVlLzofMpL-12n5FN1dCS2R_BEJEzVcJ29zeKxFyYlrvax7dBGa9T6S-CvfHc9cXZ1dnp0svRVp5ny4M0zHdyvqPntHHbSCVtLWVf1RFlm7AQDc3o-1rKHyRsERoDTIyE37pEevrFYJGkBaRHPnySUkOO5UFgyZwtT9ewbehjph3ufAGcYUXv_7xteljEPOdkFah7PEmFqiy5e1XFeytsjrXCKaPogNevJFjwYV_inxO6OPGHMe8GHfs6x5YhBjyX7Nojrxvlyt4TOKuyena3qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NA8jDXdkyjRqZqj54YarMShlvI70f7V-bHUj--HOsE-HiVu73YWyHhHefVEnqWOAafXZ4SvezgHLwu9LT2fU0Zg6g0X6OZ8JisCESC34qgjU7mmPoTkAV6a8wnOU7TKKjeZqCnXfd77NrD0DMEq9dstOQfbzSeogpv_paD_9Ll3fg57_HnJseteoYR4EAesWO-hQ_2kEuujT1mrKyZkeLKyWqUywGhPt38XDrYDyYJrs6il8OtdJP69ukd_2akLkmd1cWh7Ps75XiNGz1im2ptgTrLecQIu1a8jshkHfQUDJf7AzSd0lDuaOVTYOZ0_Jtdt4Q30kzKUERi37a-WC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twnujJjb8UoA7zx2etYvyVAtSuJW269MLfkFX8BH3E_7dzlg0whSzq_vEUQV7_qEK38epJMRFdXze9I5az2ukFU45tLbQ-NzzZ7jav2FLkC1HVhfJTEYPPisP22lk6EtJnaIgqZVGMxsE6ijSW0Ub5cKGXzAzHS0eL392-yW4RMTv6V2GlHSr15hL63pXndtiPfU22b-IR6N7CaTaeGPgTetBmP3ZXkjdlEYG4NJ1phjUjwUHNMRMawRQwUfJm6zJo1yJgScPG_wjIApJQWByGep3cHiHqxprL9mkpcC7tSI5o7uedZosOb4Z1Wl0RdlVnA5YeO6SN1GZXBYLGnm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BoxhXo0-sn840yp4ilpfxHAiebtLW85CCeztcGuPiOz6NPf1NDkxAs63jKxOJsGbGH2MvQcJ5s6TEA-5pAeGaoToKbeL8AMjn39Fwhk4jEORXUkbihtClKHQd-F_sg6BuDuD-DW2VXEwPgRVLdWthY8BP4KnjJHo5krM1CS4nxQ1lJQE8geTekBQrBiUpnTmWGahjLWWGZ4xZF4Dmg6JWa33oSKMjtdmfliYLa6sG2jKCOt5rnvFvUe4ANBFLRzj5XxVmg9jHV32BrOJ-axuEIpJrJKRVIoaVoB5R1G5bmaKFH3Nyw8ZUQ8i4d2jJMlMliQd5jBMZph9uvMspIZFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kND9RLVcFiLZPcqIFCl7gTLh5icTD4uwZVoY7ztnGENxXXzzF7GgXQzd7nW9jbpcItsG1h8Dv8XJ-9FYYcmi9UsLs9XdKbu05MplOCE1fAT0-64ZTakn33chAbNB_xjvcAZWgxUyslu-6ZH4wWcqaCiL1KjfdjO0bCcoDLJJCvZKxQn8dGtyPESR_KmYAEO7Z7wk3BctC5pJjtFQFgLloLEEf5HMWCAaD_riM4JXUxp1zx6rIzgz10bRoQ4as4hjjywlk-8ngyZHoES_yl34PLbsGsfUUdehFCdEoeSoDixSGfMCRPFcHySP67n1589rGR2G7bTxCs81XSB2LU-lsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ezzo-vuH46isJVSHk3ugcyVJfGB8USgtMTpaIPbCjxoIEUXNDbhAAdE0cxVBQadFAHbaMpXDsqXEy6iONE7RwQszi3TAvhf3JgeQyXObbya5qk231Y-uQqnqXZVZDiPkYKiEdTrRYkPZmu7Fa687uvZYb0wvHle_QzdfCL_ewooWxxKajIC3T7KZmBq1vAGcULsI8NLvbkib7ylHFW06VoUMG_lm1rBjTiVcaa8TOqBM9YcwAAN-6fIXYPvf5CSc07G1RWNkBGequHH527SCYC8vkigFrlg2Q1keOE5offD7Q0SnjKysFV0rjF02u_9Zz3ZjNigFL0NakKEDL5ezMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RZ0BM5LG7vYB2LUY3PcyBeFA6L2aKCREM5Da2AcqOYQ2OH1nNjL87_fDPZ4gLAmNvRf5EBtS3KR0KoJNdK-hBzXPJBgeIOmjF6lusTsKKkBPJtz_NfSEPafeytQ8Ukl3MNd9gEyRnX1AU5TxHzTMuPAmJzZFQ-F5ABDkTGmo_IW5RNd6M-fCARWUVmv_Pb5Ko40kHX4B_8ABHJaKpa6x-YSxYbF09f_Z0wp4KIUGOfRwoNbI7IxHKY_FsUiploR-sLLw3m07oYODA5YXp4coYsqzQdB7GG0mkV4BOKZF6uy53Me0zgWCh4Paak_vdV6WJYhXGab5ng9c2f8ZAqq8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BFMEVtQEyuZ_1MszVW0tvoMiuT8aa089Rf2iq1US-DoOEzD1Qae2sOg7XKQPuf4iUtYRrbqDZ0yHR4KvUU6jzkh8o5b1V38NtqghhuEk4zsQI3SCPV_3X-JkUOpTUMJJxOqjmRJEkYfA6ZUZUebSdrcwW3jd6jB6DxIDphJ88vxFBLaZxMF4usiHev0vv_tWbsm6CBQ4Cf_e75y8Q7JwfwYeKUCpasUSMVflbbzet8C3zKdniOYE4AQIMOp-UoQF-fwEP-4whXiBayrKDkCPYOz6NceVupuJd7dPk1AL4tsnibIXA_wPFFnNqCUzVNdi90nAuLmfvyMzLWcs1W3kHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tOxcYZlWf_KjadCm11OkIFPOImqJlQYEsv4k7X1ST6lsre8jlRglMKTx7zaI1Ya14o3nKPG3xRtHhH1fweQl3fkcj0t4GfdHm9qzhyqcJgIAU7NbwbpTThbdLXvofN3NjW1_C48FUGPUk89XaZ_u0iuBz5IP7acg2RtOf76zBAx_7SbbeWY42BVafbH5rN5gwUnBH7lUPyoRGFpu4eeIgBVNOBubhaG1Be1XUu7PwpciRjpX6CTbCu0Cu19QVKJ-svFbgjjj3OujZRd7Si7u18bmLzplX9lCZZtRi_syHNM3zGKKNzwiTvqVQeWS4Ee4s6MH7CTsov9OjjyLH6TF9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DLIWoqCnvBgVJl9BbJgBNCXvRnTqYxF_7IkTKa80EnybSxuPoMUfQmw8jUAfQEsfmpVKKb6NO-KGFPGKdfVu8xJivYc3l8vrwYm4a0rsVfziq-C6kWC1OEOXhpbwC93vNtx1OpGvNqrVvVj7L3IMOftPqPJiI39VwSeuvMwMmz03dNm3vzbgc2EffpRcOHCIoEQZfT42m5_W7B0g4xFq6NP0KYGr1X9npa5_u2SHexfXlwdzMbKoRiypwS8IMVTltRGUXzDZ_8HrA-ptzjmR35utTolHZC0x36v4KQgvmg1mXowwVFNEnSUTH9I3ILnylRhVfU0RMY4lvPzLP2rr-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j--LCyOwZ-bRvzG1bWI1FMqzezcdknEqJlxydDHQa_9iSD13gxzX__nop7V1eHhcODa_IuTtWbFv70DNL0QDml9D5NdA0s1VjnZMpWfDOTKqyhM39gBzxY9Fexrymt1-7GYBV3A23Bm4BepVLFBFoURZKEwbTOP6jWD1o71shXWYMd-06go9SmWV3GgYQEKsgTO9CuXbWIH0xdl0rO8vjeL1vnHGn25Ov54xDOkT3MDgnlAzBgrO5I6pN8t-rSbeGxttKzboc8uih_qwOoWM89ZHEk0De1EIzLtseEloVQBxhuXs-l49Gt57NRaLU08tYz7NiI4Ylp-OW4_z_bhtlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bwfzKV_2385gjMJ5-KwXv3H8rwVDiesLKnKZAvDpiy3N5ke9SRQYTTWPiA66i-am7pqX9oohj9tYKBjdekVwNSyVjeXVoqcvO83NQk9Ycadoo0w-6M6Xe7K6VCT_u1kwwJwpRAhe9Y7ZUxmABV5madBABLa4S--2PU7dGYY9s1Cf86upd0oveXRL63_LJ0PWRP0uHSOfU6hCW5p6FlW-NzGELv5ozeiW_lQx_ql_f3FuFveolKRHmOzjsi2gjmHnNdGbzznTPcMikGTxUq_OjLg8rDgPZ4gqgLoL_Rx7rVgiWBa3eZy7U0nW7fxoU3Q5tAXP0g0aO-C6sWDDWjB_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LX93-Aw-po_ZRe4OLTd--AFohXltEi5H3sGn3Xrw-KXHS4Yq_PtZqronUT82eG8Dc1z3m6lLYFGlNhf1XMesZ-vZVL825hYce1TotabEsr9cKTLGTD71Ojgbeikhrl1iq_xueoP-AWe2ShU9rFVPfji6svIA3WM00inSBucqiDg8QacaBLXmwc6Yn-nU1ii_0odV3XHtXrBcDhVlit98LWMGvT4MTadsnioR5cXyOtWRE5RoUCq5r8PsNtnTmea053lYP60PqdJlBluUe0qy4i6ok8qLhupCX-zH7DBN8X_9um5TlNlP1oShUxMQwwt-R3UFN-mo7ndHuXw66EOSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lpzpg7KBNSG1rfwGxSm5xZk0R4em2zzqDbW4rs09HX0ISFgVJx8wVUVrV-KfTZHVC_PmFKWqX2wBAWaiGMpBxV-Uw_uK3phbFVoDjuS7riuKRZ9fr5XDaLHGt3-h4y2UXErSe-FGB4ihdLEgsVaUVPsOp7kXCavkf3lV5AEKHotK9wZKhA8pxR6Lz0sv4TU4axOReYFT8N2J0oQCVZoniKv1IAJClzEc0MwNSPpZEiH-k0arj5qGU4ZoqjKKGJFJ3bD-CYPH1YEUTSwWSbP9ESeduGpxmQYgEtnRrol9QLHddH7HBTQxutJ8iLQn4UPc-H4dFtyRpvUSn3am98QoIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u3yY9i1wyZwDRYwDdJAB-Z4xBMs8ovAqiM0Iq8Fc2KkRFaHc1mcJix4dqbhUJeSqcijYYtyB8h0LkeoFBaQQQ8Kg7bmBuCNP0AFNdmHXuPo8kC4u82Ew1Hio37xXCSJRHDigb5hamqvqshVpwQ2nUuxxsPnDbm_81xwP4rbLQJOqh1hGbyj6_T3dXQrIi6z3-CZw_MWKeiYH9YRhrk8bt_RBFWTSSki_eJzqs8B7Fiy6LXWbUBQH4yRUuolUJzVqh_2oGSeMJ-mnC6RU3R9lLdci7GZmfM9eTXZLsmyVIevSgQMHQ5mnUGc4ycNWodzi3EijvhhuevEpqDaB4UsuIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d5_7Om_mXKuwukvR0wqOxKYiKkZSzcrS11uUb7KNOI4xZWHwLFKWYGRTOsaNlL5NKBxiSVDdJ2C1w8_0iWYbb9W3pNw35EaKP1lBXxiLZ9H5QLREtucfzi0N2Wd_fTKgosgizu1V0mBuQbVtPYN6iiXci7sx1NR4Iq5kk6Nt6NXD-5nW9fNDzA0sfC93C79VMpLr8NkYcquZIDllSGA1jZ6Yrf8Dm53G_wsl1VAEKStclIvdh6pKh9CVjlTgbxMV8abS3S7JrJs7M715vN0ZvIls6WnaQoNtBIKSuqiZs8UwNzI2Pf2Ox02FNKZUzGtor3izz_DM-k6NrRTS0LbDwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vm4StutCH2FlhOJpFrIVCtW06XFIYXFU0olIhNCElY7XST6wVLa7sCg7_155R-6b2CrJgzJoghEyQnEvkik41Bf05egQxU9ff7J7h4i-iS7VOMExjVhS6UK-qyoWG2Sf630WQKe4TUujYntYRDvXkEJ7ctKJs2BB1-pTWKAH8PBBUra4UGgkL4-qP3mC14BIJBIDq-BfSkNrz5VXsRqoWgXsJSOXVQU55KpPNBtCQVThiLe5V47eluneQrkwUMJVgA1z1KDhL9oyLgG09Qk5ewK7-tAiWaroG5uw0BOxloavVqHZ7eciP001h_-jq2tzC-dYLCaNtUWz8Kn4m4HDiw.jpg" alt="photo" loading="lazy"/></div>
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
