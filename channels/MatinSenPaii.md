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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 15:26:15</div>
<hr>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/owmtahqEDCeiNaHEMUSurdLK0ustKOg9K1oTjKRV_CJEjZjV_UvcZP45xl5FOZfKl_XfozlgVRsOhINz2c9i97P8qabbd28Bcc5U1xXKDIpAh8Riv-Scnh0n_Q27An2IVf5f-P7C1-OU6NZx54ZqEqPKBrJXXOLUHFSFgtGtDT1ozIAa3QNBMz39uQ1RNLFXbgCP-WWjRjfxnp_uzv-xQ8TGHkHBVoPFLLeWwj25PjaavPHccOgVrdrG2MhR4BkSgz1e7RbaOWQrUvc60Aj0vnO9iNXWhW5NNP466-z_pQ-QoEbSSroTBXOjS2bBYgSN91p7QTnjS94cmjnShG1F3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tTW5qVFVHmTPwy3lwJj5IXrsX21_iUFn0Mat8VXzORTSP4x-mKl_c3ikCFT8S1zl8fD0Acp6L_yFZnSF6WQ6SfdSZ3OuLwqBQPUYeZe17qJynUxdm532XoHJJoJuZ9MI3YRimiTWs_xNPUaJld5-MSnofsuxt3nXMWMrSccLWFQN0oRaVsJtYVprKfe7JTkK7JHw3MiJvggmzo43X-_OnKD-1YoN7n-5xO73nN90MQomlK4cTcV4QgnCOACo4zJ6CwOsrQqacGdkT8VatL-IDJnr1OHaUMtQZ38Z2ANQAd1RvR4rdGeOZV_n_5n1sLwPKz-BPEXb2hYS7O3nTuQrHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_W4hOGi3lmF7iXF_9MGAwVUUbYrZOu_hSN0n_mPa4hmo7ZIzbIL4Bx4Qwf8-9D-BiWweSx8ifcE0Vy4V7LpN6cAuSeRlwFS3jh1sqEPNk98xd18Pc1e4_tpcNvbOJO-6dq6sJosaZJjwqwmurbzFd9tCpwOJgKgppMCB60ksf0oCFzWCQ57XVwJFUR73tHrOmKWfGT_DlX5ANI7FtY6sfuJRDXHrW076ntOkpn-A0bmEoxQ8trlDbu7dAfJf0s92KmfqeqNO0HAuAsi5SZPUYtz37cmb4UDnftV53PMxQvwkfjIiWcPTyF1thK_aWCxZJ4XiJtfN1x_VR9xGRcNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN5hAlj0zOOwQyYbQS3C0SLQk310jsw1yGyBvhXK34K91ZSY0cSdOxmo8O7ed6pBFvWXZsp-Po4sj_S5KXv2xT6aSIXICE-RLnQil_-W5T9p30d6li1ZWrr85yeaTTWFXvGhubtGZE9sSYOcFl3PQKFU7_5SlVTtq15-mxNRi8SJhysytWG7kGApKShpKuVoaxvlKXHTtIBAYTomBY6HL1k4eFsFAXr2LkD9tsnaYQ0zbxY6haY0HTVaF8CzbAALTTRKxeVzxWICe6LfnpYaexR2courZuC7c9uiBSYNqmrxdQIE-FVI_kzoJnUAmshl6WXgU4tAMvuazN-tJ0ikcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iJ6k3X9oosyyFmzALKF5dxpLe2n8K4ErL8xUAMbK6mz46EJ0u7Kg_x-vtgeupvPgnYw4UdApYrAUWFePjZPCQm6mv6_0JIbGs4Ccs7-iNyBGPzV5SdQqMY_wq2dMhhVB7HDcClc11SGARjKiLBMa976Nx5pewf8GEUlrFplHelOvbfIKoIoGkGPE0fRCWRQokUWcEl_QQjQwDFAZVg5uf4pkglr8emt3qyQgOC3rJS9F03_G_IJl0yCvqYQdLAt_he1O3z8fPR0urLOMZJdBaYk6-DhrF1oXTnPOIwifHKR7G6fSpQCOeJLgFGW9N0GEVk-SkGivs5hmT19moy9E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=QZalgbGsLGoQd2hsric45bfrqrfoQikI8l_TZ6faoPjE5WWK3lHTkRKN0MNZOW0kI_r9BUe4WCsY4ZSftmBywtgcYO0wqI1FXdgM2u89xkRxnU5xxEFt7zMl4tQRZ7H-whskT5ykWkGJKf2kad33dsn53dFmrXQksfxg_1ZFcga__AEB5EGsXew8AFAJG1L4CYGSYrUtV9uj-tA9KRksK2e_0hxHwzp5kYjqtCOqrPHwneDUZHQ6t-iSLDorHhnkAl48MnEurE-1ShW8U16yP6uwmGRt-rykO4v7JzeNadW9atqNL3GOTtSG9AxJ0q7W8lo8x6XASokCPfKBHgYfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=QZalgbGsLGoQd2hsric45bfrqrfoQikI8l_TZ6faoPjE5WWK3lHTkRKN0MNZOW0kI_r9BUe4WCsY4ZSftmBywtgcYO0wqI1FXdgM2u89xkRxnU5xxEFt7zMl4tQRZ7H-whskT5ykWkGJKf2kad33dsn53dFmrXQksfxg_1ZFcga__AEB5EGsXew8AFAJG1L4CYGSYrUtV9uj-tA9KRksK2e_0hxHwzp5kYjqtCOqrPHwneDUZHQ6t-iSLDorHhnkAl48MnEurE-1ShW8U16yP6uwmGRt-rykO4v7JzeNadW9atqNL3GOTtSG9AxJ0q7W8lo8x6XASokCPfKBHgYfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JVeUVPg-T8ebvhoS1kvQFzU-giK8jC75e0ju9ZPnJQlclZUGW6mlJDz8CuArU3HvYezE1q3vO0NFFEkrbD-x0Z7H5v2fL6LJ2B6Cvt8SN5di1k5T3wys1vXR6A2ALvbfsTnhgukmFOvabrM1BGr9jOcdqsQr1RT2hVcJhWWW8n5ApheUe75QePZ-hk250a5Cja5s9RIuK02r4GJy9eIwOdLcg3jy9ryw92O0SR0ccFLEwK8w0JEZreYtTZKKJOQKbY9WhR3cn2php7xAssmOhxa65slAwUDhZgEBAvVrJU0YB5fUfdmLyomfBM1QoRUKD8-e9rd1uLvE9iN-Nhv38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aepdKSU2yOjDVqYCB51LrZ3TUTxnNLz-IaZiwyQ7T1Ey_2EbUgeUYph68bF6jHMROUJppSfrroUNquK7yiF0FHDY6VzSiM5TN3u0Ce-Prwc-W05_poeSEo-RUxrKNx9BOQJm1Dwh_8ZQc9-Dkp1v45WYSWgtrL48F5h0i3AVHKEGTN67Zza7c3GO3XB8ouV_QmTcObBOWZQ9icIlQtcF4ikUhFE8O8KMT94EuqgiCn5w6ubx51jKlUDH95QBtHqLd-f8p1GFS54E89aPU5OCc7woBkgWh0ZW-NXLM-YaA1QNhnjet-OPf26i-K0pf5jOLKgoM9jnSwoFvlFxNCq2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=r-5Xth_i0jgEF2Vc4GnsKqDb1ijK4B3mIO6qQcZopCpg6cWPc0GSWEzHGPifk3BZc9yQtCWxFUv34_SFGux5UqzXAxEmbwS8JWT_duX__NRS1-f91krzFFIhOm6OIWmuOjXfC5XNT1HnBIT2N60DLFutv-49y-iFxcUWcSS9TwWFhz5TVVpudbjjfIfCIQRsmecg3K-gL_cqsA-YQ-096n8EbGoAzNTWgfWarVxdV1JRN4c4UvUXig8-utmkuE6wSNMTuImdn4944Qra6akyW8Q7uHqy0ddrcqjWAvcO4e3t6-kFcW2Ue7tIcCC_uQq8fjUlVfajwHZ1XPvTzxL3kA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=r-5Xth_i0jgEF2Vc4GnsKqDb1ijK4B3mIO6qQcZopCpg6cWPc0GSWEzHGPifk3BZc9yQtCWxFUv34_SFGux5UqzXAxEmbwS8JWT_duX__NRS1-f91krzFFIhOm6OIWmuOjXfC5XNT1HnBIT2N60DLFutv-49y-iFxcUWcSS9TwWFhz5TVVpudbjjfIfCIQRsmecg3K-gL_cqsA-YQ-096n8EbGoAzNTWgfWarVxdV1JRN4c4UvUXig8-utmkuE6wSNMTuImdn4944Qra6akyW8Q7uHqy0ddrcqjWAvcO4e3t6-kFcW2Ue7tIcCC_uQq8fjUlVfajwHZ1XPvTzxL3kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUqzxDVJwvn5XGW8iLzhfIXllW2YwlcKIqIYXxIEa562A5Qo33-qpaXm8yW5MbJxJkMTmPyr3aq0jWCBj0btIV65K3TqDX3e0tfmrcUhKmgyL2v4LqK3WvTmbEczzInK-99Fv3uBkaLPAN6PwxOuBu-TnhlsvscBC-Il9QFrvu2fKDk90DiQN9j3eVoC_fhetlyFWjw8QwwtavFVzyqIW-ZgL_VIpiuhOVS3ZmEos4N6j9LFq7Rhtet10tPQ30wsikeKOts5o869m3f-cEVaU0glSgpdOYdBeYMmDGNXPkRzHrJd5BGPsu-vAvhUh02IYG-ZLMBwlbPxY38AbB1N3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5IAzhVGcvL50pDK8QTwyDGvH8VoQGrXHlQyrq-nlZSxVO5ZN4dN_1J8lAmzpHOVtMdlEWqPCgCpPd3r1X--MH_Pm263QlGvw9KgkJiIbM0eXnmOSQnxwNClmWmaQpdlJCdTCSQ7-vD4ufNovD7xLN_yKUp3IOdvkgU13wBSuQP_FumlzZQdZo93P4M3wqjMqiSJI3-NTA6gE_3Lc6NBMGaS-zTZC44XN8MATQqltsKMg-oge8226VaLXGAHO3WQ35iTmAZRrrVRHZskWBm5EwuRtiA3OsfzAB8KeWhgV2tSG7b9yH1698Y_bwkIYChZGMl2zxHNq1dxYgpbBoT_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c9rBLBmeUyefmpV0mz6jCGvC32_Q4-d9uz_WCn3PeC4rdddmE1IKRgAP739FXJwSdiTbwz806WIIhWH01zxN11vTBgso_mneEoQF5c_zyfUQjD1yGnqzGZkzIrt9IfYoAE3riPKJqpiQ-U0PlS2ERk3ATLBwc_gbY1W8QGd3Ly6Xy3KKHXiD2sFzH-YLH3x6y3eT282tPd3IA08PU46H-2yT5E6AJ28oVTgWc1YwBWh_aLaKJ2-48GwSZvgq6rgRQILJRjNhb-YJgUt1w4lvohZEXJFczmNJVVC2n4RZfaXGEaika0EHaTQrANot8ci2CPqf5gddxvd6mrfyzHiAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ftrNMq0vWExcE891ZplDsVNImBDy76KWJFa701iAkAy5ahmgfomMR7C3gB4bPSlTinITu082ZbQVaQFdjfE6oxfR-vpp96fEvGYlXgT4CM_6jO-xJn_IcCsZFTawtKM6xxGnsM5y7wWrnsa6savisXUhX4zUQxTvc0Zj_exA-O4m_TDJHQcLXSlHDbacx9Y3BdDsjG5ze2eoLnylxBKO5RLL4rXf9QYkD5TQFMLzcYNOneTJdpr4qY21oAHO2u1oz1KqxkpcR-nZHEGlZ8X0N6ML2EgyVYZIjAOPlR5bz4ackpJqe7aFddgGTXt3HFgPLkQxFdNUclzF4MdlAC4rGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfA3FcyyUF7pB16YJhK6ccvoWLUeVBn0vxzp4vLQ40Xjd8lnbJLh_0FIkWFY_4qpU0He4FPzdWG3-hYwH5M2UVruFGh6KF2U1zvYuRW83NBqEflQC2xO6upICkwzYVzWx0SqTwwrtG-3LMmn0YXpnMNbo9l0zV92wNCcofdhRNJvgkcQV4Lf3bovLnnFuHHj21EPzFM0roZHqa0Axp0SoDqJ6qxaFfpNd4w31OcrwiOf5Uaszecv2p2cJSmgOOWj05U9DkhZoaHYbOC_-HkX2NLHzA18HGyBXKLY3deU8EjVoCLAJYo3A8gkrCxrh6tK7edHCtMHbWjmsjMXPUT68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-lwKWwjsqkmwYtJqNEVbUXf3YeO9ACpE6WyHZnEtMScKr3jpwYzdNM7W5LYk9z9pzX_z9FSx2mpV7QcEsLL9jJMbF2wwjle9F3IK91Zvo1gN5eiF63uJ2bIQWGa2X83kPSIx0NAr3du-mDI4D3ERpCyp_IRe2UsWjCPljOygYjaNNsUqRSC4dbPAw6t-G6VQiAtXCv74vC_R5GNo76SQAVNooR2bQJR4qQrgBgHDn-OXSyWMcCDsDpAxRAXIN9T_WYsuk4Skt5OkMQV1WQZKkX7YXBpJVsLV88hDSSsyAGDfFtI5S06fGPUFKqxSS0KVMra1h_wI-HTgf_LnKB5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DaC5djR2BeXNNqVXzio4-rHn-CHdb169TOCikMtVfEHySHV9PfzAPXLGGxQ0-fZ2SXHp5DsEhML_Z50lh5rJP3YpU6nffNaSBnZkUGiJApZBF5N0ANtDGELfCsf3naE9QREjdA4Gqkaj_bY9XkZ0SDsV1ro0KRg78v0C6-I5qIzP6fX145lTSX5UMwoD2hOdImxDCT3pznkoi3pjlBn7KdHpcF5q2v35ml--NbXJOPDCnJ4SI-BOA9z2Y9MSSWKcv5SN8S-S3APe68w_XqGvhbT_nn3YpibWy9n3Bxod70zbp-SnQaEUHBRnzcn6XiOYa1gtxMHTTuWhr-3Gh2D1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t8eCxNjZxMmfWVT7-aRYUGDmJkLRLe9oBkc5RUv69I1GafAKUorV3-4x-bmvDkeR2eFvW3gptCYsbXb14-iGwttujbJRDCbWUdP-CFS36uVzCn4LxVY7-Wdf1NoBmzcO3YU-gMdF5Awq2Ht2sElh3QTRFzcDK5eACsCAM8LyMIomdJFM_xeS-cDlCEUxXgYBhvDKo0qdBVQeLJ1CDE3AsHF1VoqUYxkcLTW3fmJRbCQplhxSdiM1-Xkpv_U9iDU2GgXehS6nu5VoXMmQLNr-yJ3U2WawtCoPy0_nOgmAE7tpHTGraEFd-TRkVBKGKFiXOO2HUQm1oXf2ob0TQ9ijtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i4vpFoy_FhpHwqZ0As7IiDbJAALSd5AwgcAb4fG-iRUKgcPvWVYZaLNhIZZ3JXiiWdnH1LZmxdnHElwQ_rkK8ozxiv_aJnh0gJEMj1jdiLRch3soH-qGcg_eqbvtkyGfz4yufSjBPFaldtx2UYL-ZrZlmqzr1F7ajZru__7HKEtV9o7Fbufn9UiblhJb4VxqZTpKOLej29CyW3s7DkYNB4O3XkVyQwRITy8osSZ2g9891dUxu1fXJdkUkxFRGuMbCPkvs5e7aUVYqGeI9QIcHUm99nJ0JNoD6wk8qnfdqVS21Dv-ozdKks0JytKovNCOVIRPygK5B6HBmi5gwwwtOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I-Q4N0YgvbRE94i8ibAzMHiQPHltmNLNGJmVJQ0xnsoWDJN3sO-7TeZFMpZ1sPg-4WPZ42NsIYVkgkExHQmGKCDd2y9Zr_Wr-3BdlkfBTaqDty7biAGTbNUi88JOd6UTwZBXDsEf9TI71ii2taolU5lSUqvt8QdU9KAXmlRtIh0bN-EI0OkyK80gu6wQLEBFAy5-R5gYlZbxCTAqaz2Rbr3qR0X2lBpP5YGK6D8ECghpjpexbE_xpJgTEkBnFU17EqOUaHzwTZaXQNhkSsnPAQdWMhuYhkkmEcLcjiCy1MjbTt_7o79yKzOi5taUnpByHH8ONz4u4miH5rohbDeJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PSEaFrqFbE6b0lv0pHCxnh5e2710X38hM9IMIE2ychmVoOoRcpAkRHaLLkPE58mM4J8QcCPeq3AZLlVNEcCI5L0-s_nor4PfOaeIcnH-wohM9joAj36uNFPfkMK-VT6cXN9aExivSXcPY95v2Xq5OGL1ffQW8XYTij-LI6cMmSMCfoNj_NJ3sj3y6tzotv4fB8ClWozsQDjSjOhyyzvTJd0TIVAZ8_OuktESJuPw_7Ji06i8bH5QqXj1r4Jq4hOe0DnusBO5m-4IC1daJ8Op5bLPcoR33kSHTcX8L7wv_hQr23qBgZcWxsAvNHLtRHlrZrNcLAzmbXlFaq3h8NN6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XzSSzKItQrHsALlcf0cfFuqS9GzttMbJ1E58pwirfopKLiPaLyzAfTk8IQ91xeEzOLBQY9hl-wnEW6zwTYePN8OpFiQ8wqbZ6qWbCapfXZIMqfTJOo1u119dp3lPDzQgS_IUT6W86mhEJAcRkJ1VkW8hXfikA1mEAA4n7efcxPYVw8I3eVnLH5FBn4og0ChuS4hX4A3VtJVoojRvhx0FkMbfcLAmpRFniX-9K35M8yQmYP3YUQjbTZW6JWnCzxPtiAUDYX-rX1G0QaOMagF-q-146gqOuj-0q7-Hnxj0eVSp251ueJP5noZuzoJmkIZi6aGsBSFDujmHCBJVtxoDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=CyLuxnFdAWrY9JbciSTVoWdxGzwF6f7e3M9DEfLQF30VNR9LLBzXR58op6PHznnRdh74dHt7jtyzNj6zoV_XR1F2vwF7DbQgYPJ2ckh_FguOri2KB0S1rNaOako14clnXlj4vsqR45oeGD7_64H5FAR4sw3na2vwnGRTPmtDLXOezX-ojew-70numUk7aahr188buNf665IokEDmhyLwVSRu6wwQkgZ4MU1BiZnw5vmOavGwWqqv2D5txjFdVR5hlqM_LW6bLlTjjWfWRb_8MNr1xrNS37tI4spA8xIYgvA8AcF4VGeaenz1n3uab7D-jdztC_-QE6WMxms0Qq2Wnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=CyLuxnFdAWrY9JbciSTVoWdxGzwF6f7e3M9DEfLQF30VNR9LLBzXR58op6PHznnRdh74dHt7jtyzNj6zoV_XR1F2vwF7DbQgYPJ2ckh_FguOri2KB0S1rNaOako14clnXlj4vsqR45oeGD7_64H5FAR4sw3na2vwnGRTPmtDLXOezX-ojew-70numUk7aahr188buNf665IokEDmhyLwVSRu6wwQkgZ4MU1BiZnw5vmOavGwWqqv2D5txjFdVR5hlqM_LW6bLlTjjWfWRb_8MNr1xrNS37tI4spA8xIYgvA8AcF4VGeaenz1n3uab7D-jdztC_-QE6WMxms0Qq2Wnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TMDWHXPLBtA1_x4BP8Q9_8IVq5im51UA-lYXkR7O3ShBjg3sO03SgrkHXac8CtnS9uK-R4Ci2sR5WwvAkmH3mHBt1ZQs1jXG5Uv3tOnELgaUaPCFuS-qu0qR-AXyUzOwnHGkIr4e2GJLJ_1YAge-kAbaqkkKIyq568P2f5u10ESdoW8k5sy-kxKUp4kEz8rdT4LNXlUNsfCXHYreLKnID-DjoT96sV3_2A7tjJWGxlqfFkvsOgnmNCl9smNO6rgmjNsIuV2TKDQtwEZwOm_joyj94EkAVl7hC2XDbbVFK8jvmbhZzAwBjvIbNlZIthv3D_8TbTem886hfRWnHO0gvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCTNjk5eo-1DCNQg8s08pn_jLYX-GWVOfs-R85XsDVPKwokOniHpTrAwQyLH4kOz6dXE820MTvNBlMAI8G28z5sC-pivZXRFHYgVz7JHaIQfqnpgQRpdOpLkQenF17QuFTJxqrmoMv_cisVhDTCr8TptX-_LB6d9SKpj08ZFx4Z6oEb1gxbgEhjbqYJARJAuvIgHziS7uUtDxNP6m6mENfUwWcDKKVft0rO1WVeweC0ljOcDq_St2zGVF7t8acDyRLM5XLIH50wzDnYt0adTpf-hJcieVUmw2uzveikc1hl_2CQJRYoKr96UVvZQZu8ms6mYU8i4W75LQgsHxYARdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k86eze-eYw9go5z8RA1ydsjeEaTqbWAebS-gTL8H9lPaE48lfnieFNkx_zj_fRjvY5dEpgcnQVVTXG9FRv28I9Kv8eGnP29qUVig032BINB5RFzGNu2k7T07R6m_FMgLBun2HSI6znqF5nP4Xtov3dDgHQIwDhL-TRTGkk0QPlh0N9z85DoN1h-9Jloigzxe8o4yWfZxEZgIDlHcengIYvg651HhGWfy_Uwvu7OP-TrHT4-KKtc8D0KWyY26jCRy62X71BR0eFAvVXlKNCVoCjBramySyK0Hqav9vDGOnb0W_g-foojT6Xb6_8XtBb95ADYUDz3xig9jd_m8aSKFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/InL4U9ZVJy9UC-LvlZBVxWuO2hzlCr3JTvXTeJgEzCoCuAfKoOk-1uxGPA2hhtiKp3LrX8lINQbQyLgyEk41pvNxHX97EovLqADETnvDQytuXYnKO646cMnTElQKqL_TUErKA-xkneNRHTp6pIWX05PpAXumS5I4B0K_jF3ltD0POEs-BQxlW4staoDxK_OnCMgmULzprYOOGrVVfBPeWEYjmrUY6lXOPWHG-uIp2LKwC0g0WagGClQ-dBLnQyJ-_4DLvrc8nxUBT3BabCc4CH_0ATr-TFpTxXy9C9jUEMw3TgFqHqrbcx5pQcfgbQYg9tK_coth1zMMgtg8vhDbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M0QsyRTfnzwtq9UgkJu8NNGyuC0TR6krZryDY822EJu-PTuDsXJPqiPJGtIEjSbQbbqw2UfbnZLKklB5PwqgR6RMEOPA9M8dEmCZ5SrLupl9jCU-_oOkDfefQq7WTBweQBn681_8qfbe4byDQ1zaON_t_UnJmNhmsNZx3wFF_LdqyA6x504q7BGTla9sjlUM-knsFpTJaJnJI7H_oJJQTaMzHXbuQBdK9eOin8mkbPFAAD8xU2qdo97BQYd2XkXXNhCHTFzfXXL_luTuYj-OGtA7QbzkydOx7zItka3T-u1SQczjKFKFQfqXo3_m1ivBd2yX7xpMKJJMTO9yGujs5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tGmK2KI9-RrKRv8-mFfSXi4ZN-gWqA5V8VK3BY0BpPB7OyV65L2-4t3VArOxVD9bCchOdlMlorz9LXMMn5SOLFX0CpQ-oKX2XP3SKMTg0DwUdF2s0aobI-jglQwZ3UEA83L1pYCBlPPSYB9Pc-EbgbWlQCagOesY-ksV0WujZISCsZ6_D2ZghgnGq4fAhhgI2Yc7eiNUTMuhgu_PDpQsMnRCagJj8dXm49qJHBb7D3YZL-7Z6xm2gGeEqTy0kp0HprxzoTmoXyxuck1hSwNTHGeh8q0WtbjnFES5O-v1yj3G0FQj2s4ITLXDY4Pl2rKp66RjBK8W6sJtsbxapxkm5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qI7rofEvT1OanmXrw9k3H_kLC5pc9QtMZRDzmjx7wjmqIRf_u3AHOzbMjO4PfZUXODsxE-70IjVKzqmveasz_7Dc-4TQaXpPJL2dqRbYl_LJKAZh59P8yQ4jkYJPfEUkaNVLhr5tQQkpQV_Vm39FbOtfi0eCa_ukeoh94RjPd-AiEaJ3KbbZiZDo6kZcrtiNUPFcuRa0J9EGoqMRzNAPRCj3soBsZkuwXn-hI5_RLn9U55mjpBYNTCPcPkNzyTJnNQf337Ro5EH_MGyRK0JqGEtGlc_ot5WH_vO88rh5FYW0fo_Rj1mBl14Fwf1pAon4BUXwfsjKneCdusjQAk4HuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LKgvOE1eD-owoRUvIXqxyxDwmN_VvvR1DUC8XCKPNzawW0t3ykb3NRp0n3SUki0LFsCkuUtvQK92Orj9S8DoN4jVHf2j_wtCdgJ6XZd348CQp5JgbYfPS_A8AK05Oo4L8ursz_Z9j3onK_c_g-GC7BM4Y61-r7kG1_1iVtpkdgJcyQ7C-O4-Td7CDxCzzrKOKgikSbrdm-zv-DNOKJRx9dW8snNdhIiI6ofcWowWOZ1Kj8DEnAZZO2LwQnQ5rioR3eK2c-8zN28C9HqRMcCaK8XUC04-HosZG3_EFpKjwVBCaNpeojwSyD4XEc8ZH6ZD_Iq6DJK4KqRyXs_619VBTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FDIX3fct1L2BqlyamykYcWLqq3VOSfCrS9NfEDvTxf_XDwrDsKBSqpIU0n2bjmGhIRBo8i80jCqcfdNhz8AKp3XlolA9aqdR8RzoyKbjb8kzS5xCUnqnGKCwYNeiDoZYrhVponcqefIcnmxK8-8R42L7bPdLn_w3NpF48lBEvEmLi1rK1L_8U614qo7fXmrR2K6VTOkQ-qWGPG2PxbdHelhTYCNfFWcEfDtj4VvS7-yqZMqaFO5sgH1c7rlSFBqd1M9w6kzNJNEbxBqALgY7gvINbKHKuOH147FOrREknhBc_vk0BVHG4y5YihOogH0vfN1D9zdKUAkdMwXhXfmU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=T4HOAWFyWcU6xaRqKkbAsvTRcV6qvEG8X7ufeHGOcBQ-uAorY59hxosFbk0OkjT-_TjvB5565ehHHWsCXwk-us2pLZJFzWgPv6t8HlJXQQOV0LbJMy7gWO9fh4S11pN-fY1A_o-UnZpE1bL1ZnWvrIrhJECmEzk948EQTUhUkZ63aFQpqarxHnaox6KPVmRSqYmAVFm0rADOaEHfdpB2k-hY0aMnFEhVL_a_wlSwSDkWBjQ8EflA7k3_-HzjMOrr4hWZawNPrCkfOuR-RtW72y5GZXtb9Ds2FTVgOJhvEAR8LlzoaJgbgGP4RPkaDF34QEsU2Ii42nj0z8n7jBULww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=T4HOAWFyWcU6xaRqKkbAsvTRcV6qvEG8X7ufeHGOcBQ-uAorY59hxosFbk0OkjT-_TjvB5565ehHHWsCXwk-us2pLZJFzWgPv6t8HlJXQQOV0LbJMy7gWO9fh4S11pN-fY1A_o-UnZpE1bL1ZnWvrIrhJECmEzk948EQTUhUkZ63aFQpqarxHnaox6KPVmRSqYmAVFm0rADOaEHfdpB2k-hY0aMnFEhVL_a_wlSwSDkWBjQ8EflA7k3_-HzjMOrr4hWZawNPrCkfOuR-RtW72y5GZXtb9Ds2FTVgOJhvEAR8LlzoaJgbgGP4RPkaDF34QEsU2Ii42nj0z8n7jBULww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UTxl9x7hnDbE0ZrCyBOXQ0zWGo8EQOl0QZ9IOq9pcE7EVzsFs9PX1p9Ajp64nKFndLBA52hAn5_RZ4pseeCPF0Cp9XLy5Tq0Lm91rRc3uGrhLzdJdzY5reboeRzxs4O13ru5gFvrwUrzRTxU9nb8bPMBSC7zwDsHHd4n5AXYfq6KYJPQRSkbOXxivJTPNuHe9V7N2pOZhoitTk6FpBmq0liJIl68V0xDs5Mf29_veaDrTdmUt5tTkb94JwRecIGlinON_dAVNrtj4Wyzb6fcaOJZki_KcZUVXPqf0aShIOuSog1uUAJKD1hDrKWwWYtbhnfe5YebzH8U67BPbANtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CeVP4R7aWd5_sVv3fw6dFSLvz3BWKGq6nrwh_0eFqWC6N2853S4iWK5W7aoXtW2cqxMlxhys9E34qWTuwPUIzStw2q4GZQ5GoNYfj_20CHIv9OvSw_TbNboHLKj84T6-VRUFxPEE5iIOQe-QJefsHPzixRU3hpc3Cg9PH478ALEae7NlWm79U07SrFqe9MZdkwp2iYWGH_GPie8hzuofNMLVMr0OaovQQLxrvz9lzCkhXaDD4knB9KTh5wH_X8p56ssuzL-CrIEMLu65Dr5DFNEocan524VKvJvmB5K0RYmGJFJen1HXHuGv6_SHjL4bzXujLAQJMvTsxYcW-DRY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bAYSVGxuMPhzt0ZFD1Tur2kukvbSIM4ZDwbPeZZnvA16zTes8_wqc9sokmLxlbKzpbprTnQUuakc38TtXUEoPqIqezPYGHNgVJzltewYip1_ySmfiMni1A1xfAFJfhk3XHgVHnZjOB0WA7dLB22H_BEBsRaBAvPGzrrDTZEgSWEAXmL2h9W_qH9CMlzBy2CZxdoJuzGnk8kATZVcqfNDm2tlbcnczBO62-C8rfnRaxCNjQbc7ZoTyoNA0qwY5nAK4Uuttr5tvmhawTur0hCMvCj26SDp6Kn8KWjNzmCj1HrCsFvPUVu54UZGamrCQZnWAMLc1X7AdUb-0vGsPAIRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQbQlBPrqN2Rr4HRs8rW_qPhSYObBd_1fW2FLLIOcia_bqGR_J7XJQICpTjoJwlAgXZh6DLJDsRDnYhYGz4bR8Gx8O6KaFHvfRqcw4gNu296ahFMDmNuLfdscY2aP-UbMMLlBKezm8TJt8moKAPeH9CGoxpF9IOoc9bRBR3BsRyox5FLL8TLCu9C8lHz7tgzBeS5EbBuxEKtoR8_Tcf3G8Y7qMIppNMKP_VxcQht4H8LCFCDzN4xywK18bZdUx4MfUWQ8L-XGZoQZqDjFxuLGsWpIw2FkuZawI1dFJCaCbt3FQ9FLbQBsgoWtw_kGW1anvylK97F-lqgTUBz-AK2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FgGpEB7DQiEhO7gs1oP21gy0BuQNGCF8rWyOROEJdzOCq74nu33-xkfdbv8Th2Mnkp8Sn2a2tLtFmGUBy1434FOUCVIcbynCSzlEYYPC73I9OkWgSOz-YkUgJRS9HtYNpsf0f9JNQyK4VRo-wpesLTR9B_JC333svu_rwDeNyPH5oSTU0TKlFTiUMVy-y3p4mE3E8qTRDMEHZVxljZd_xZOcdQqqV8EyWm0NwU9FFJPnzFs8LNMgAi3AaFyEogILUeQP1LkUhhd3c61Q-w12O67PLpfgAoGMvwKBP1EewePbRW3__ltY57oE44GyRtbQP3nmmG0olHJHb44G3GqSXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jN7RTkcCXzmyR7WxRRoE31MHcll1cJSxQwACWghjx3IAmoiy5dtdVRUrKF3wPX8Hj_fl0gFdj1M1YfoMneViMcnCZDoCMBQmBYtYLQT9P0RDUXpMhYxyNTWQ0Vp1RypKCK3YF9Z5WaVIBc3j6BCrSJs_TXG6lCZOO7P2fJQkg2cH1GEY23qmDnLQIW-GjvdLU9KicNe20n0N4B50F1ls1YOybizu-OliWe1IhlHYjB5KhX42pog5F_Y6dr0sowcUfG7CGzEr16USKZYgukDCj8KGGBQwq6UfIUa1casvgJryfBlnJuCJ9V2MSTUPS9vyl8B1krenF496Xqc905nF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vTzhOf63eJdzH3MtAsi9XtYsRXOGKOxciViQNLAzrOu1c22H13WyWIDahiJs7N6Oz-BxOrjAh2lQeFqgD_9sUkfDsBM2xqiqqhEF654bRSLeEjx333eoL6uEMU4sMESCeigz_JLPdypz50je3grYxDl8oXH9eU4eJszfwZeYpjxt1-7Kdnrsy6w1AZHSSP0AajG5esbU9sW93Bw-EtEcI8BY4AKVkhUJJJs1o1tSSLlKsWpYEcUKnDHLmhiyp4wNwO01jzNNA8P5TKvYhQ8QoQNsSk3Rw15Q-yXFZNHa5EgcQdrLEyp2AHxu5ICt1_jx3CkT4T_CPF95Wk_Ai9Tnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QAYfkXiDb5Z46-d4Cq09qeJHHmtamrtiYAbpbdmbdIlA1m5lTWmgHI9hxO9Fw1_JLpgO9-iMAeknD1D1DiVm80AzsSs6v_IdiyE1c0WHR0PvlE-t5xI2K4uml1TLh59MtzxrH3zc_uK9hoEw71KdUFS3UDIRxaNYHs7DGhKIpRLW1PT_GjeQDQ_LY1-m3AYHrspita0vBSWVcZaCwRrbg_ZSHVzZ3dByWJ16_OBkYpWbKdmoHjZl-9wTNdXTME6eDfMS0sudVlSHxNqfavDEbAs2wu8ajgt_bnoMzCF03IrTg9ux3Br2a3eVEG3fWUgaCB-Gwy9Spk9_XVtvDLqQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rnj9sEK8mVCjkPge3XmdJ72rV4DP4tumbaf46gU6lTH2CFbZABdJijzus9WvrsiikeaiSHwg1Snc-gNYXkwNL4piOb2TiUJdOJ0z8jreg2a-uYhjPLnajvGqoJer94ei54794odrbMygnuHpic7ZtafhRCLe2LW-Fnok1Vb48OreEepPotbsv09VJaOWMdBjpFsZI9eow3tNlIRfLHAY1byDMDwL6tLCQfsA16fNvyeVCiIxisntpF8Wtu9P0PE9sCIX1WU6eXVQlWdf6ynl0o_pCLXW2pZ96TSvI9tTB3br5-h4mVH8AqjrhSe5h01PUBPqUShKgU0Oux6j83iTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UHvHBvjCEwE0Zt4QRVQN-VreiEn6vyiHXOJb57BR9797VTAiycIOb3gPdOp45mNiE897EcW3fh7sLyikv3mlDGtwMU1NMk5V1oTc-S5PlEw_8ZEw258ai_TW3jmOOSs5nqYA-SEfUQ8uETjrB8owQow8mRi77VXUvbICvQm2agDvEfB5RiXmspBNTMyGJIwE6oIqTDWxoBKQsGsVYW7GKGUr1UPOCbvLbFiOoGzaAOc6Wde7ufOLGTPfCeI6dGTRna6FJyIiuH8nT1Cu1nVRtV1GH-_mGej3tYfZoOZNEJGZURpPPYHDRy0BthtMgxP232ufGjBRqAf9TYIlJ04FAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/djn_btpQahI0u7qmS8xhdNREwOp7kXLZpQv0oGQymX0JfsSk7VuBdOH3kG5C2AyekEZwcbshnwjW7AwpQNWY9tZp9nFXSEhxUVLurNbngZkV9hVMLjmTndTD75Q-tGVEm750icy4IZPu3aSAHpN5e6kLXR7eSqBaGC3Zkr0FC0CTUncGq5NPyLbWcgQc8-dgABdDP9yGl9WG6y3y7esFOZEKF8Kz3b4X0b50rW6RM4FT5fZ-WuN3_E4vHsKza44B7bKtFYmE-ZAyZJQx-L2YUFDeCKNJ5ojaIEgttfZvJJXBpd8jaRlays0_8FVcm6ng18Rup1tQblHTwaxgzASlSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HTYwgUtd8-MkuTQCQ28NYeSUbDiAsAuYwPrkm-AG52AOqvq6vedM2xhjwa3wHfWOZOUVPksWaju8KauZPkkPoNFD_rmx8DReuWHszBLBfVdWa46fcJ1zQZo3t5Lp4J9LqrXUx850jvty-ixTzUtSHRFPBZ201FAj_oZCvBaxdc_5xIipX6gx5GH7tUEszVBYrKpUJPt4U9UBs0ccFzpTkBZ0u2upudCuJkMnhxSPc4qWolBrwMyNJblKGu3tN-N4XHnf59Wn4O8CtfUznx12_h_ZvuVwkE3zc2CsqvHTSrPVSHck80HqThBTaudNnXHuTAvnLofx8sDAIturEkab2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVQMpDdEtCImn7CJRnNXDrj4Wh3Pzg4vxW8voR2vcYqgwn-5IDr8c8DP60svORk06RgfL39USxXGCCHltF-ShKQC6p9lW588AmuHoPWvy8lh8mA_dT5aHcLXgt9pYBcG8EsCPoCG7Ig24S-5znpVjRodcgd3ClnKdg9lfH-usHUmkpGhlI45WwkJDImrpCzebKNxh1eM7I2EXKAlS7XZg3u2cewz4TvnlhQezLOtLta0mBA0k6-DaP4bSsM-MbM8EBl0HfFlrM5yV84HRUTIm-Zn3c41fxtDYJ-o1U521m_NAMn47baTnvC0Z16BHetmQ6nM5tG2N5rapH6QwtDhww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kdhqp0NgdNy3AamHd6v7ebsw69d9JFf9zq7V-qO7YjEZFWm97JCo7fOaMAkbk1wwdVid7oQBB7pT7f0Yeq76eVBMn01pQbgYO3L6v8TiGJLVjpD2ZSzdN7TssR7m0-qWvdTjptz3NkYxflZpQovg-31NGc5SWwjwFsb4C3W0X_sbMK3RNYvJf0AGEvn3cOzYPgtklIsLEzXZVmgXVvNDYI2Qn0H0VGUmphxrowVufqy2Xl1bTlyJgmRSe5CSfzyXSMTNO7N6z17xtZfmH5YeM9mKBIClfbPy8FGjiMk2hcKCaHlI_jTOeKnGcIMUk6pj-BldSSSBMJMCVNlEG_mJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MUYBpuKml-4zYde5V7wT2fjv1bt6drY0FbbyufbMktCS0qQs9bHytwYAKggO85wXsZ4qO7MGtRc4MfxXdrcghryuN_rJP1VjblLp5HzUcG2XlZxDOlsm39kuASK3ERCOcs-g7BZKfXGiqaqpzGUPzzB8hRLD7R4Ty5cO-lC0kCjGvFt7QLhbM53_gSZczbESmhp7hJYvtRLLWPgY01ff4hmk4X0cH_zW-U3F7pGp0HeFUJeUwXeH4SMSBfxrfYQk3c__noZfr_Pa1yWW8Q2B2x_aUjQp77ChNImBmjGJT7cwQjFnZIkiX1lKNZeU0bIGbzUqPs4VtY5ZY1gkDJS8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vNuqL9qO0VkNPQSkIib-HQ417s74qcuBxZUil_tB7SrkVwPs_Ydm9in2r8S6UFVYxgG3t1tZk7gNp2wQaOBlvQ-1FUzLqKd9_zllb3H7v0ojAL4sCeB4nzdCPYia39drHKpQayGuJr_H5CAyFMEYqQjGsfUadDgEgQk8xCJoetpDUDEeXe3mObQc8c0wVnCuwwm35jaZIi9PETdEQKh8X5gJdmF_5Vr7fn_PeBw8zIgyWOMNhXa58wIW26Eer91VsI8GFug7G2Zr44BsE_SdVM5S8L6i-MOvONkPRwBnSGQZFK4dwFMexA6jsucuFcDxTOpiRsPa8BZvZ-AYp9lq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YC1tUf-4kApseSblJGPHaypz6-Q1clVtLDELhc1AH5-n1acDD9I9aXo4zYiRwFvNn9ap9lgb-oc_qh6YSkdY8xaV1Ie0zlqoFX-S3uAGWIs9btiYJKWphC45TXalD3wXBZzDq_Sxbw3u59x7RLqzV4fd5vU4NXduzK0vjohQsE1k9wZH_K0sW30Kbp8UUKz-9J57-gncfnO8_dlwEW2gOhLOB4rna_3VNeoJO_2ctcg16x_752BHkNf3KbgOkmaU6GAYOLBtVO_RKqC_dc4mH6Kc5VZOOmU7qljYWT9FZU3NWe7p3CDrmYdZ9eJsADnTWND5d7dpDM8qd4QtHzpXew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BIzqkBvIDwUcCIOkz5s2UkeiTGqmGknbgJw7lVnm77N1x4SJ3iwIY-pNlx9ODiUMgrdWlQNeMqmRT3ImyfYiEk54xkZZM8XysLXv1w0XcnC6kzdv-WJ5j3ycRDWmNkda1flInfFel65wgHLJpfj46kCbZHRd_jE0gLLbLV6Bz_xi9Wbs3aYqdte_61uzuBV_-bzAAmLUdNW1Pvo_H7tw8znmbkKFekrLKaKbnEegKKcSJF5AbjHtq0WKUBOomZhTNCNMAo6TnxJhOF_sZouu9keJ8V470vB2MQx4qSKPeR1VeqXTEzuVIyzn0O8Sl8LZfuG2Rx4hQKuxVN5xw7-EoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HjoqE4qY3KExhIZ1R50_cL9KXrKN0UqJc49iAG4F1cILHFzdcW3-rEmvgbEnZao9kOt-TfhGiokaDeux4XYYR3X9BmK-KnoIYkP6dUMia2YUy3CXOJPTOxuwiOY0iD5sE2EW0gta6oUBTcsCUHe8zVN3erij23ykIiwsXoyqspeVhI_rhzMuSZ7s-Y_2QVIb2hQIB82Nn48T-n4s5_CPPyKGCFGKzhLUIHevZ9wHVM9fYxKLpqy1x8FlA58-abFVkpelxoelIjzujVa5NEkN9FOTrXYLjsl81fc4knt4w5-sfGQXl2qcRvWij3vi3juV_tBEaJL4q3lviCIH2g0nnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PUfwZDXzW9pOfwy7agCcsQLfDR67wpQmBSpdFwKAoTwZD36z0n-BNIsEuBNFkCQZbOUiIhuMBC0J9XWhlCjtzFzS_sqoTC09bKRUddpKwno3j83KuBQLTcrm_KEP0msf1l51YuXoKakj6pCmBwPcvyZyR6bs6R_w01dIdluMDS-TcwN3xB1P5M719PhUFrCf53Q9StWmvMuD-8ZOM_NdV5OT9U6QnE34LrAGFySupJ8_eXalMkWvyCxHpUuDiWDrul58qt2eZAUA6wbpWs2vws9EuJTxI1hevlz4VtCkXzNPWgxpQH-8-d8tu8qkccISY6kSvM5zMwHtencvUo0oKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g62FpeZdyLU-adWr2TR_n8kVBJ-Pr8UI5MSjpoYUZLIJbnlf6-z4y-d_6jcjbWNnPejVs1ZICyUyIXqvylKk7FoK-UVx0mwNiZG7WgHxa2PLknhY7abnV-ELpFUAZb2RS9dinf5W_8DBhDun9imivJC0SIl6Uqrd5ceDg9eywPdHXPHwbwlfgoNf5VR5y8dVD1zTM3TlMfVsya4hjsfUvMmMoXR_aKibJyCTl7Gok9nUdnyEFo7tyrMFV8F_AXF-BvM8kvQ45xXAZQ8sN977dRwLXmC1vJAB56Jsa1BR8H0rZWLdvXxXJ7eGMPMVi17oh3RmLIxZmzz543nApu80Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W9IBq9HfZ44fFKndFucktSlmPgmc2zYevGwmNOmuqJWzaU1wTfXXQDZL5evgU11L4YDqiJjKwgHSPdYHK2KbwVRy2vki8jjNeAuqwJTVyiva8zpbj7bPGlVoE33RebjEy9ZInvpGbwkAQIZAB7FsWn86FhCBW_iIyveP1QWB6zL3ZSQefkbWEVM_8u7fbg2XUfZvxcZ4cqBHIb2Iwfmhi3hUq5ILsjJaUk_v8IBhH-gOyQPtHeFv-PgxC3E4KeD_2P6P5MhxHpvJ4k4Tz3ab_zjB6ncjSDmhbUb6AQGwy6MzOQO2pFbHD_sDpztqgig2pv4UUYQ2VSGM9Fd5MA6bSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
