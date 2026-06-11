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
<img src="https://cdn4.telesco.pe/file/SAXMoVtsV5vR8Mog_ilzAdmm--ujVL-CFGa14rQ3HeKF_xndggELlVFR2poMfLXUaQwW-KXF4Pj5nozdcBGlPcmbHltWBzYyjZ0ntuwc0lO6gw9Ro2CyBUehzORSYrpgO-BAKYKoNKYFtZv59lHR-d5xjs51a15wGQs_GEixklfEikEyc4HkaWJ5_hqbL5oF4OZQO7N-aB8Y1GEot1NVP2ZRuyOgVAsCrSLPzayCxckdBELFjoh2C3E8Jji13afu1T-p3l-cGXapQueKwZldNz40cHDtfKwAdx0ZegYeDLDmOjMVs0n3xX3wyQx3oXos9utSefgOyfKezXRsR7b3QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.6K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 731 · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj1RpKtqk7sKEcEi0Y1GtATFdk2JNaoXaDHJkGN6-yj7ogeqR1UKa8pRxzxqgtsmhc_4V3NmmA48eCzpd3HIDyrOYZutbXFJg4-gMbbLMIgIPQUrpNcjPvHk8islQlqn6vAN9Hlw_-Hw3ehfY3GcmQ2ftRtTcPe9aP9BzdN3QZ3FrFIG4sJ6wUJc4ggKrMZ9NamUZWsOxqakiH-YFgbgoRmyqczvr1AueMG_FMUzKKRGXqzgrniUlzX_mrTWA3bx1JfRxU9JA1dyIn6VEQnavL9YUkFgtxNcnHqRi7xFFxQmOSjmIwYX44C_nJLsUtgof_ol_d4VD8vYVwO01RyXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M7joD3iLYAe3PIyECkM94VFXkC4YiqpSn57lp64O1tXz-Hu-ieTnCGvGh0FW6ZAGqFxxNKPN5jU3GY79CgNH9JnykNfhFG1Ch6kyuNTRfB5rp5505z5EC3peRacLNDdtGhWbijfxipI3Oh9K2E5iUaoqeHgNeg9QCAVWGRP73_BF6i_dYEOilJLH06oPGalqbXZ86C651u9_IuLDbKR-jCber0_jxMRmwEbe5E57rqurj0-nBWStpJ-CYOFvAi07Oxwl396GQ9XadLfu5S0BTEH0bkr8CAzQ-0vRMfwhIdHTHmtfrMsFWLYwmyR4yzJGd_yBQBvui1emGymHNnjfKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M7joD3iLYAe3PIyECkM94VFXkC4YiqpSn57lp64O1tXz-Hu-ieTnCGvGh0FW6ZAGqFxxNKPN5jU3GY79CgNH9JnykNfhFG1Ch6kyuNTRfB5rp5505z5EC3peRacLNDdtGhWbijfxipI3Oh9K2E5iUaoqeHgNeg9QCAVWGRP73_BF6i_dYEOilJLH06oPGalqbXZ86C651u9_IuLDbKR-jCber0_jxMRmwEbe5E57rqurj0-nBWStpJ-CYOFvAi07Oxwl396GQ9XadLfu5S0BTEH0bkr8CAzQ-0vRMfwhIdHTHmtfrMsFWLYwmyR4yzJGd_yBQBvui1emGymHNnjfKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=vjbR-2-tOp4Evu3Dk2w0q0_961WyAAaikaR7_FADGd-L4REhmtNCWhynKFsDYO7Q6TTLpy0nAieg-av4xJI3JgCNj1MFE_uBO8-wq8MdSvHullpOSn55r-nR0HXqRW5JjiTOwo08K8xgQQI0kpyT_eu5591NMR8mYyJkZgW-znM__FaLZ7wJ_PqVyJvvcJdeDI5ifdnoxu1sUizZxAboylB_OS3_TT8SqH5-PO5Ss6_cugZGqjebeMFxDeQL_tNL8bbUSq8xi6CAMZcq0AFIaKhzAFsBeRgyRPf0Z21qmio4GTSh0fbiIZL3O-0PvAinJnyXQXMk_hQVnZ6c_8Kg_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=vjbR-2-tOp4Evu3Dk2w0q0_961WyAAaikaR7_FADGd-L4REhmtNCWhynKFsDYO7Q6TTLpy0nAieg-av4xJI3JgCNj1MFE_uBO8-wq8MdSvHullpOSn55r-nR0HXqRW5JjiTOwo08K8xgQQI0kpyT_eu5591NMR8mYyJkZgW-znM__FaLZ7wJ_PqVyJvvcJdeDI5ifdnoxu1sUizZxAboylB_OS3_TT8SqH5-PO5Ss6_cugZGqjebeMFxDeQL_tNL8bbUSq8xi6CAMZcq0AFIaKhzAFsBeRgyRPf0Z21qmio4GTSh0fbiIZL3O-0PvAinJnyXQXMk_hQVnZ6c_8Kg_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=vH9mjPR-TF2xhBSOMOxTJNKSlXB-4CAklw-c18gQ0Dims--dy8-mD03ekDzbDBDacHMl-PdndFrY8Nj01Ts9odYPWMxhLBemxMHj202WUGNQNMhoKD8PTtVwR34rzzfVLilUgVTXGFZmEg0bZsRoyPAWm2kmWN5b9e0W18xjDl2_epw-lcjGUtw94UrhBXqjmhAXpqO7QxM44MivOJ9pDpBWi3NYq0vfsNSjtt-tNgR1NsX8PW0ajUdiEIZKDQLhzW2P9KfO3ym5rxMN4YfWpcRA6-nXLoGQdnIn4JLG5_iGznJdZZB8b5F2SE65OyS5SoPbT-jUZjDxlfQ2GYKJMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=vH9mjPR-TF2xhBSOMOxTJNKSlXB-4CAklw-c18gQ0Dims--dy8-mD03ekDzbDBDacHMl-PdndFrY8Nj01Ts9odYPWMxhLBemxMHj202WUGNQNMhoKD8PTtVwR34rzzfVLilUgVTXGFZmEg0bZsRoyPAWm2kmWN5b9e0W18xjDl2_epw-lcjGUtw94UrhBXqjmhAXpqO7QxM44MivOJ9pDpBWi3NYq0vfsNSjtt-tNgR1NsX8PW0ajUdiEIZKDQLhzW2P9KfO3ym5rxMN4YfWpcRA6-nXLoGQdnIn4JLG5_iGznJdZZB8b5F2SE65OyS5SoPbT-jUZjDxlfQ2GYKJMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vd3Q-rfJ1nF9r576pgTVYoC5FHApl9FZ4RNrNC3mSplLfB3leQNGUy4W_f4pYhRMguY00501K3ypEJ7a399vyLuwcjUSqkh9TZ5KstcwgDWkvec0LFYlzYKHv1u00qwbWUvPm3w6AVws-FXRaNooWW47ozW6tK9R9jZF1Kd0QIAhx7kwWAXwzcZKfrUqJjyNSrMbcBabTI3sEzlKIR0VSHW3JreCClRXWVP6x9sSaauSNQ2revQjoLK-PppMTRhjvTiSojF27l18GaMt9hPwtFV69uuT7DsMfmMZTba6pnV7uYkzNEcH_nu0-e7ixz6ZdxbwabpU3DJgTOuQi2_fQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti3L8onMtqznfhME7Ut5wv_465syR7o0kyXgSmA506xCGaKdRRMLdI0nBz5PWLByeMBoiT12fSb9q2DO1tuHKhRNhyqiOUowWHjYL36xzy3vte2x05ZktCR8SaLJBvI5ANVLpLVL97gBPQih7gs4cmPxi6y3zQoWQG5HsXCNpt4wkQPjayAP3SUwBfXpvqNiC6Wth9n0UW_Z6fr4Ms9MOwlbQTs4sHFyL_BiPesB7iNP4T-9ZtnUGPER58PMsFVhd-hRvdlIvYt8GeQPjs3PQY8ut81CZZjQcZflg7ciRNclXm3tRFzE0Ya6V9YL6FO1QtmB1DiWedm9SocLjuFaLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=EmerUp3BXBxKJPuPuhAfAZQPEAh6QPF7XTD5a5W2LHjfMAmiSdyasjOqB0RI-Y4Q7436Rmtrj_7EHvJhi7XbBneqVeRh0dpvFrxwHSaXGIISGuhOWzxAhlbw40oLeJGM2ctQH49V--kuDe9v95GpmRG9z5SJ_KqRoN8lAaIYBiB1zB3CqnwTQwTQjt2xNXDSkiQ4uB8tMxhA2HnTwEIgdJyZs8zC7MvUQ93D4yh-gTCN1Gw7xwsDKUCAvtNb4Eop26vXJfRXa9LXRmwLETx1288N-2H69hu0hCoys96RMPMeZt3fEURaKxMmqge8CkrwYPoJwjtYYjs2YZnI0PAUToWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=EmerUp3BXBxKJPuPuhAfAZQPEAh6QPF7XTD5a5W2LHjfMAmiSdyasjOqB0RI-Y4Q7436Rmtrj_7EHvJhi7XbBneqVeRh0dpvFrxwHSaXGIISGuhOWzxAhlbw40oLeJGM2ctQH49V--kuDe9v95GpmRG9z5SJ_KqRoN8lAaIYBiB1zB3CqnwTQwTQjt2xNXDSkiQ4uB8tMxhA2HnTwEIgdJyZs8zC7MvUQ93D4yh-gTCN1Gw7xwsDKUCAvtNb4Eop26vXJfRXa9LXRmwLETx1288N-2H69hu0hCoys96RMPMeZt3fEURaKxMmqge8CkrwYPoJwjtYYjs2YZnI0PAUToWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOBp4Wgpc20Mqa4_ffqvRvr-m2uAK0iQjZouNY4-UDZeOHBmbTktaI-NphXTaxllOXLi6PEgrCAi7cGcmEjYfxXygDckxNRK457QQxAxhCHhBLcmw6Eaco5SJy7Q1-iqwyR9QWApw7z0f-AfVXoN6khHTVRdXMbneyoBogfHbh4vhP5J4p1YexsqYCIEs6Eb-YHDkBXlkVZHz8h8O7tQ6BQd72eylxp7TPz6Wvt5YDFFzhhP-iHtIACR9e8BgzliJKSBUfVOEDPStrBZN0hHLnf2Sk1Ptoiqfnn-stS6YVTodVHBCuT0nklbNTVflixt2TLwDN6D14VthoSiBFSIhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=vvH6Kaf4kBBozcDB8QUVCAnLeqwSJKkCNqho4N3ja5t9M52LPQqvLhTHx_SrrFHzyGtJ8p8QqnmcBjx6VnmXcFgcvllcXqOU5I0S6AXmVfIHM0fbv1T9Lj8aoUvswX53rkSCX7PjXU02DCW-rLl6tN1LM94D3klqwqBSyJHTDt3--VibNs1ov6LUozrRS38xiTQULEyNnKFFxLlIDS0tky2UBFT9ltA4JuVb53lCJiuxNGkEEyLfYl1J3EwAkM5zzJ09EtLEOkMKIvarfXMHVC4YDPMB076zwxXe01SfXDRr2hivVoCLz_eSnPo5MYKQRVmLezudxfODVLPTIMFW15JzCEa4BtXf5jM--VkfLDlI4jyWjW14ll7LFXpmVH6qC8_fp2mCEilUufQoNEVu0Lm5MOrxLqW8ATrCu6jUOD_gJZ7ldPVOS9vdGXqD78n-HeS9Mge9oDGtTwucHNUui89obHBoaeg3ooHd3dE2xJ1kVAwyUWYpKj6_Kx72c9yoR7ND8VhcQTpsxUPGEMbzHZoCgb5NulGMczBpTzGQq9ik9PdK16FhQq3-KLswotCcTULg-JhplSDkc0ggwX24-0UcqoWbxjXgP1reuthVnG63wBpc1EqGnzqkEDdgFWjSDZ_QVAGdhsFZJ8QeNaXcj6rUy_blNcB1_7l8tzHGm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=vvH6Kaf4kBBozcDB8QUVCAnLeqwSJKkCNqho4N3ja5t9M52LPQqvLhTHx_SrrFHzyGtJ8p8QqnmcBjx6VnmXcFgcvllcXqOU5I0S6AXmVfIHM0fbv1T9Lj8aoUvswX53rkSCX7PjXU02DCW-rLl6tN1LM94D3klqwqBSyJHTDt3--VibNs1ov6LUozrRS38xiTQULEyNnKFFxLlIDS0tky2UBFT9ltA4JuVb53lCJiuxNGkEEyLfYl1J3EwAkM5zzJ09EtLEOkMKIvarfXMHVC4YDPMB076zwxXe01SfXDRr2hivVoCLz_eSnPo5MYKQRVmLezudxfODVLPTIMFW15JzCEa4BtXf5jM--VkfLDlI4jyWjW14ll7LFXpmVH6qC8_fp2mCEilUufQoNEVu0Lm5MOrxLqW8ATrCu6jUOD_gJZ7ldPVOS9vdGXqD78n-HeS9Mge9oDGtTwucHNUui89obHBoaeg3ooHd3dE2xJ1kVAwyUWYpKj6_Kx72c9yoR7ND8VhcQTpsxUPGEMbzHZoCgb5NulGMczBpTzGQq9ik9PdK16FhQq3-KLswotCcTULg-JhplSDkc0ggwX24-0UcqoWbxjXgP1reuthVnG63wBpc1EqGnzqkEDdgFWjSDZ_QVAGdhsFZJ8QeNaXcj6rUy_blNcB1_7l8tzHGm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nO_oz9_DmOWecOXEvW-LYEhPWUi4DBz348Z1yUjOn_Wl5Jzngo_gfRz30cMBcqFHuwXlezT_qyPZOSAQA8IBr6wQrtAp2uTJttAgjmsB2p9NgT8f_gLGXvY6tOBFgk-qSWmWkTDZxGHpHjjK84m1KQM2FTE3JKuvMc1OhTXubRxPnovNIV3uBFxJv5WcAA6uRUx53FR74gT6CbsUuiBU-xq47VrVSPtqlbk9aJNBARucipi_zHmGbMy7Htwh7BmyfVoa9td2gj815mUFnZAOfiI2zAa8j0-LbBkqYAXYJZYQAGa3Om8qxK9yPabmRxCHahwXfjCWRbj3tmKQ4rrLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2K0UnVPr3w-7NZh3dWvzmyj3hlpd6mPqHtBXUQ1iqxg71J8K2RY-y-odh6Vjw55GHHkjYeUL680DbDh3m8_Eg0e7XxRcSmNI7vATJctQ7dAhlKeGY6O7cREOVyf0TcDlzoG9NwIIbko45gK3aXx_PAmsnKynQT-5E-40t7V--rcDhXBIb92-GKPRBEFPr9azVvH438Uyw3pm4YP7yer-ONsLD8cr7cEgYyZFPnXMKchsGx_2PYxe3Jrf9HRcdJ512bmKGc1BmpSDzGbLaks__W56d1diYsaXkS8lNhAX-FhXtofQZRAhjobResfdHY1wHKT3tJlzBG2jI8Ohm9oFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNo4Yx7PzN65C-mt3FPloR3u_tupgN-ZTvHlwY7rpdFaGA77A-Fqg6b4Ds7hxrUgs6QN9vr--3ZWWA_tXu3JW53b_GvWHbhj6Q2FBxtEDTHinDoryyI6oQkZAOLGys49Vpm0sXTyXcCRgbYqiyICBVtS6fCxzJklznKhNZ-_R6A9Hg3YUofk5ZE7pM67f2QVO3VRgLU06fcAx54tLRhOQE34DfWJvxO12MZ4cGZrSpysCJ-qWZP43y9po6-moWsjk4kWOT-1QinF5Qq39coz56vUY76tSEYdQeTwi-vLKW74CYYE34WhOaGH5eQfGdquCnIAlDaXs12wyhRUCKzMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3SuC7BuaSQjjd5-v3o7tBccqauy6qG1ciE_cYVH_rh4oG7rTAmUbyEb1XT2DqDB45QgHxgIMNRpMozZQ4OhkfVC2jIR8iHMbLlvrnAbTL7W92uH8S4dnXne46hgiOWBh5qXHcy4w01vvt0k78c0khm7ADPjExyrk4Pzv0omD-G3K2rWT9mYEMT84oNHStLihIYnVFX8oyoFVyHA_RvFEentUJYMn1ITnmG8rUATGs24hS68zQSbnlh5KLetF5Zc2xRAoCXfqkYmrwA6SZep6GlCsE2ryGd9AWI6JGs4T1uhUiZX5pQ7VkfwlPH_LM2befDKNO9ZYWojohX5GyCCUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6250" target="_blank">📅 10:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h58CpkseGg0Zf2dcEnriQg9goYaVmmFzPCVYtc4DPn9SaYyAKXhTfFIheKCVq4N8jYiFxpZcs8_CIXe4OWF5U8riG73RQgr9g2IpKWGNdOyi0YtGhSSN9c7l-flKimBs2fD67WW--xlGLJD5aqkOOtZ1gEoXm2aKap68n4N8IXy3WODFyGoONvRlHOYnaVXF8hmFhnL7IbibZ4BVsMwXbUOyJWlIrLxThZprcXI_dNPXNOEyFZY1HPyXZCSY-uyDToUYehisXjNGZFKNuKdyHv6IvjMUcacz_PXN4vraRV34ujyX2_pSUN1bfx4JQzFDo8lE4GySg-9Bniky2c6aIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6249" target="_blank">📅 10:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=UEbvjm0zbWxhO-Qfa4lW93ZVDJQ9IjKC5l7_dg72yRcPPUMT1vTnusTxxZHwAfzbNHy5pGtuU5yfYTwjLBmXheH-Mhzxy5208TMl_UfrhaIe1-cbe8aD7swVz4EceQYipuop2adREK7iKK4A_YdqKqeutYoBXBT7P7-zhCxXJXWbmSiUlMhLvgBGjuhFnLYkHj8bhYKILBHxDy3UFb2TKuJYif7TWmlq1QrXMTt1BXqNGjy1D51vuTg57nFSuuJALWl4WnwFbWAYttf-EVyID4A3KTKaxI9Ln9jtXuThhBqGS-uMdqYKNypmNXLSVduaYBU9sR01_WROCs9P5gctQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=UEbvjm0zbWxhO-Qfa4lW93ZVDJQ9IjKC5l7_dg72yRcPPUMT1vTnusTxxZHwAfzbNHy5pGtuU5yfYTwjLBmXheH-Mhzxy5208TMl_UfrhaIe1-cbe8aD7swVz4EceQYipuop2adREK7iKK4A_YdqKqeutYoBXBT7P7-zhCxXJXWbmSiUlMhLvgBGjuhFnLYkHj8bhYKILBHxDy3UFb2TKuJYif7TWmlq1QrXMTt1BXqNGjy1D51vuTg57nFSuuJALWl4WnwFbWAYttf-EVyID4A3KTKaxI9Ln9jtXuThhBqGS-uMdqYKNypmNXLSVduaYBU9sR01_WROCs9P5gctQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAu-CtrJ5YVaO4cwIUDuLrMDJy2-aXMs5-vp27b0Nd00zy3-kPKmtDtNzY3LcWeu7zXlt3GsuDLaaFWvqmSpnMYt8d5l4urmR9Gf9WivmqSWZ5-Ldh5IdTsCv_FoHkVojJJxNnKKoZ2JQUuUmckXnM9LmxuotGbrukP91OvATUu1dJrDDYmBWDNR_zMDWhL788uW84eVKtdMH2Szwu25wB1TyVSZAIcJOdw5pqgx02qmYOxbk7epabIA5bf7rLLiT-JhV6Vwdun_wW77WQtNTJrk2VZP0dmwsnptZV3s0nHKqgQNEp4vLLj50wDrcyykF-w1rtB_2ixvj__CO4u3uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2HtyNjJY77V-lbuDDHOx3ckoiv9nGdvAZgM2vbfTWtX90ltGVf52JXf9UQaB_YHd5pB5ojelWAXkvq4apeag5sqZ5llsaSNaHUYHXxHEp5xEIk-l0Q1STg0Vv3Pjd6lDZKpVwANKGVYlXE0xVEdq3iGQGPjf7HBxD83vCFU8EnJXs6lT1L3CXChAV5ARq4cxHoUjU8VvwxZHjlKf0J5LJ6j1lWlO3b93gpVR9kMbpcCaG2Yi_iO-RZoguLyChnz6zD8PhjUxtN4DXsWTtODmXzhDdGG3mIlKzVwbkZmpXvCi0B7E-HYyROvK1UfNC1K6UC4hOScLucMeRJF1Y5Pvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6243" target="_blank">📅 02:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueG4Prgl4haNyn4Snsdr_6mBSWWEjNWA-OeOVJgmqSFu7Nk-qmG5c1esAu_zoDPORx8sK9XMslTSMPHbfxkyRMsOxv6m6egAhYAWB7Nxdx4S1wB9d6xeBBpcaXsU6hX4Z30PW-6thIVpnWjGi56TRwHg8K99ceOddjQqfA8Iipe-Fq5oQh2tivEAMm--Oq9R-99PmmWVBcy31WYFS-3ZiRQMnoMKEC4PObWolPy4wCV3HIco66tPkb8VzlhU1DlaNwFSvl4KrElz6KHapihgiIFYbMDsMnDhZYGVsZXe91KdGIzWMaqn-d7UyFTQ1Y879vBZPl-HdvdTrNm0QMS_lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6241" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6240" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6238" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app
بخونید نظرتونو بگید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6237" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">StormDNS
a.cyntarix.com
25ffbc77bcfb23b2d4ee225eedcd2466
داشته باشید اگه نت قطع شد</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6236" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این پروژه پایتونی جالب هم برای تشخیص اشیاء توی ناحیه مشخص شده کاربرد داره مثلا طبق مثال خودش که با QWEN ادغامش کرده یه نفر با هودی اومده توی ناحیه مشخص شده تشخیصش داده و به گوشیش نوتیف فرستاده و گفته چه چیزی با چه اطلاعاتی اومده توی ناحیه.
برای دوربین مداربسته خوبه یه ناحیه رو مشخص میکنی هر چیزی اومد توش بهتون خبر میده،کد اصلیش با پایتون نوشته شده و از ابزارهایی مث ffmpeg برای مدیریت استریم‌های ویدیویی استفاده می‌‌کنه.
github.com/roryclear/clearcam
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6233" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6232" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هر کی 99 تا رفرال داشته باشه ی کانفیگ نپستر میدیم بش
😌
🔥</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6231" target="_blank">📅 00:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6230" target="_blank">📅 00:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6229" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuYvZDGdM3pENsUn8sfb9GKxGS8MrdckSRC2ppyJdyWMfzxZPHFtA23xL_CAAkna3ds-GNbfbbejam20LefGhj8R656vCm93H2S7PO1sTIheInfvRy-PPMMgAAQDvBlzHol42m5nmSF_THQ1ozwoll_gYgFlAfUP_gjqhL3R9mvV0MIa2SYMwcAfNm0LN_9zOZyVcMvIbyUGzzKnvyqU8eiqQjql1mLrakUqhHUrlxd1uhlGnqOOO5dJ6-myXWBAhXhafsOofjwQ9QQFRx5S9hiTOPfKqxietDcpO7KzzQxSllRtJvcO9p71p-vGm6-XdkDPg7yXt7x5qqQIsKwacw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6227" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6226" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=LsSQMnQgBrwc5wGvlvW8EmRTdkKQy3Wble7nTeWU8YeCR2k7cQ_C9hYQ01ij_EevTiyTHYzjGIwldCSujIcIgd9H-sAdDmbFhzSgEQxMRmk7bJ_sifpzhf8wmrF2MbOoMf4JgIYgWLoU9mvo08G-4FnrFH2bWsEwHTZwFW-_mWShWxbK2tN8YRkA9s3k8npJ0_g1X0iI8XXGqTPy0OTRm3J4_M5qLSu1rx1Lg2Ga35PMGg4nSEIVP5N1tkwIpxFd8gNNF38xGpRzx8VYKCexZMmUFBOqGl--gicQAea8tI32R-TTYnwUjaIkyttguGyxozDVQkXkofz4aT8GitIgwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=LsSQMnQgBrwc5wGvlvW8EmRTdkKQy3Wble7nTeWU8YeCR2k7cQ_C9hYQ01ij_EevTiyTHYzjGIwldCSujIcIgd9H-sAdDmbFhzSgEQxMRmk7bJ_sifpzhf8wmrF2MbOoMf4JgIYgWLoU9mvo08G-4FnrFH2bWsEwHTZwFW-_mWShWxbK2tN8YRkA9s3k8npJ0_g1X0iI8XXGqTPy0OTRm3J4_M5qLSu1rx1Lg2Ga35PMGg4nSEIVP5N1tkwIpxFd8gNNF38xGpRzx8VYKCexZMmUFBOqGl--gicQAea8tI32R-TTYnwUjaIkyttguGyxozDVQkXkofz4aT8GitIgwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6225" target="_blank">📅 22:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8JiVqvyHVoUxqTkZ9dhSfgQuKWVb-TrA2Axr8yXMk1AaknhHhwRAu7z5HjSJ9atbCrUhwxtGJGnVIAFuxhWOIKTMHhiUq-XKAvuShwxnqGiNQv5jEj2uxIf_T1pdQryvuiLzwt0HJTClXhOoRK8R7HyEqSPUw6k-LD6q1zr6Sm4kRLJpuPDOzwr3TwJK87dHTUct8H_6xS0qBas2xaH7hMNbc74HjIOUjn6FGXRgQB6Neio__QupVftmDAtXH7k9F9bTGbWZy1cGa1cxwNNhwGZCbdbFKM82q0dVl1pUJKmjSEbvomZUdAwwQV-RnfOkERd9-hZtVIMmHFNBw2Ezw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6224" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6223" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h59m6rpwRI2-a9cVlWVsIPxz8zMZsrZ8ZZNq001qBoCfVrR-gpGLNMCSAAfo8vjHR4O5Caybx9ahRAkFZIIxab1FmLp0XG6GScD9Vb7ff9OS6SQ69t9-ge1s6bO_yfKL22hw5481LVC7pvBbfA388ZvWIf1cpcAfA6Qc6hULFMezNcTANwahjZxXUiVXAGGiRNPRK07zOpYRHUMIUqrlAZbQTSbQ8Dfe9yuVApZ_m3owJj0a6mrOgI9tO1Pg5LSLe9mTAtnxEz3xmLC7U54Rq2Si0_woZMdBePPX5FgL9k_F6KLA7TfUv86cjkPu_dpokHX7fz3m4bFdExjS409VNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6222" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6221" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6220" target="_blank">📅 19:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خب یه پست اختصاصی دیگه داریم این فایل رو خیلی جاها میلیونی میفروختن در حالی که رایگان بودش یکم دیگه پابلیک میکنم
🔥</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6219" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqCG3IbJA7MrMH7AdQnG3ETB1rTFijy0UwwJmZ4Uc8J1i9SxeSTw6f7SnMJtraD_GWaSmrhisko6Mi3nnXjPNvDiYKkMGYS1Y2AUcU14CgP81NbxmFXze-VhnLSjg5ezTs3XrHW049oK2K6OmWQNXS4JD98FQBJCNTDV0d9HsKL5xbSzSLpX1lsMAf54NZi_8Ph_pfzJhzMj10nOeFlw9lPqVeAuIAZRBLRgCDQ-9bPgR7EEoWAAgFc3vHUZvf-PEV-OqAIP50tZgJA7eA2eeusj54VOYuN88wMNEGSQHvm5Y8M1oU35GDvccrgx_Aw3IuPRRUok3uAUp7cFHWk7Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6218" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6216" target="_blank">📅 18:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6214" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6213" target="_blank">📅 17:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
hysteria2://5z15av99psrlhdqp@32.195.51.20:39150?alpn=h3%2Chttp%2F1.1%2Ch2&fm=%7B%22udp%22%3A%5B%7B%22settings%22%3A%7B%22password%22%3A%22dlxmzvxvcp3i6v0e%22%7D%2C%22type%22%3A%22salamander%22%7D%5D%7D&fp=chrome&obfs=salamander&obfs-password=dlxmzvxvcp3i6v0e&security=tls&sni=32.195.51.20#usa_hesteria-%40u2vpn-100.00GB%F0%9F%93%8A
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6212" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6211" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz11iVppzBwtOnsePjQZKMJDo6phHXbCB5H_SLJPWsZZ3TvTkAItrrEULrbf53dHcI8zvIfJD_t3CCdZp-6DDIT-Vjk7HRICFuLpNfsEFKUFSntLRU0Ap9j6Q_b5A3k6tX8z2APVHpOysDA2JOiDNzClzD5hL2-lHWDBeKTVRWabSZ1LUQEKmn-Bh_Pb4_kG2I9kIKVYXlasfYMyG2L7EBZAUujAW8ITRlTt13NNTBG_QCyOdSfndId5VeFuRW1bC2gcNjLQaupUY7pDdPkrheBqkxqWanqlWWq41TrcUB4-jifTGiFkxCTQ7gaAAUGY_aXDQgZid_r1YCDfVI3nsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6210" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/br6DL2txhOtL5mQOjJMwD8on2GqXYNf0YUDRH12NUiGafaxDv94L1cQ2d5BsEpTMfKi7dyWBd4P5RsWF2Oeq36mDSb_hNgS_pLaJzPXJopRPlmq1epls5KrQMRnQeGa-jMa8EjLtIHFV9gyI-l3nL_AuGgb3j8gUwG_IfZXNS0qDVLuXGeOibOHIZbJL_1vjbFXTiQtTWdzJr-muw0vrXLa7kiXytjRvoz5236Ze_8-0HL_sXuNWldUCt4tfTQGEgzVM2yMCNJTKLd6CSbGb5vmPdMumeI25FedPmPXPwznxZTjF2Z7O0CU_dtzLxHpWi1PuHcajoDflkMHNqU19Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6209" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YM0gNIaIuXeMZLkCTDjxfggXv4_fztd5sCK69S22HmPD7s7-ggzMWSTZk2YM5AZma3snBbItAKN8iZ2oTiNvcmKv2JXdPtgk4ZDYaUSQxoJNJKP2nOqotMTDY8VAI2pSObl0W21xRRsLcgVUk3NGQ8aQnSfZp5sVw0gidU0osmwdmVtii4-Pomp1Xarca-XgdjhF0IB-55wbvJSiuiLd160fxgnypoPNFJ4CmR8lj5ANs-gsrhSp0cNTW1mRNipVUshiC394HOPvM3Dsua0dUdUKX685TESG7goSSa1_t2An45Jve3p-N-vj38desqqY2INVcBlIOcZXx2KIWidVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfyM9MR0bZCbRPwfTIRjqDCXP4PXz6FjnY7xUj37MnGJBT3RisEbgB73Aqita88rKXQRxe6Pw2DcAdqAAYgf6KDQUEWOnZ_cdow0N9ukMngfVnccDAlGFAGCydXuCzgbA5kNBHgN_y9c6IVcREIKrhuaVJrYaJ6h39JIRwEzx8Qcpl-PYxmVGb6yCdimQ0A50sOaASk6G-TEzSmwlQM_sEo7c9GFAydrJv2HcjJ7O5KOhjNX_22kPVbvIfR5P_TwdZtVFdYa0nd9I3VATaOiPKDkNTF0DESjV7WQ2CGy1gjg7_YqTtWMbIztoOD7hf-PbhEgNoEwAYowXRUpFFp3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjmLhM2FfE-lprqM7S5g9XaQbwSYf0lfswVXMr6NKNaamnu9cvsOtMr8uMF-iOZhMdy-5AwhTUX2QytA69AMN2atLIjMf-dR7NRUmgHOPgtuZell_gvuzolkT6GYTK_faJiG1KX6w-TgsfATZ0bHLWBQNS5w09BOu1fRT0Z5QaB-QG7-4OuBG200N1I1IIZqhEoU1AYibkjkrFLcZYssTb8CHluwE1MzUL96ZRMSUOh6gq4sbueHDp__p2hClZxn4ZunqjYOMV9FReA7tzB0SMU34ozHeDKKcVJ2sF-cHAIB8bATgjX7pXh-5vDwy6N87oHS996LY76pGPQYoXyI_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=LwqTjsaYG0aBLA9gg_O90xIvyWslRGWA_I-bKGNYZnuoIpHCzqIaN7qJRKVM4JNsQSicXosNe3r6_3PnJnwE6KqgrvmfBw0qFOPSy7OscM0CKSqMaqN1NGWjwGHAcC1b1RtrE4xX3YrYoPT2BWK0AfdCfqnkdbshag5b9p26QOSj5RLkUJAxfluol6WeBDpk8rTIpPQaxz6duZ5BwsBQML8jH6CeoBSRXweSPjaxJ60H9rxSjsgPO6aCya9gScsaHMOjwODQI5Hs4YGu_OQyiEVd7Oh7qfZAgwvDZRbGFaWKHoKHlgPhtm-Aabo5xenETJ6Ko0FqySIZ_XtRYDkorA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=LwqTjsaYG0aBLA9gg_O90xIvyWslRGWA_I-bKGNYZnuoIpHCzqIaN7qJRKVM4JNsQSicXosNe3r6_3PnJnwE6KqgrvmfBw0qFOPSy7OscM0CKSqMaqN1NGWjwGHAcC1b1RtrE4xX3YrYoPT2BWK0AfdCfqnkdbshag5b9p26QOSj5RLkUJAxfluol6WeBDpk8rTIpPQaxz6duZ5BwsBQML8jH6CeoBSRXweSPjaxJ60H9rxSjsgPO6aCya9gScsaHMOjwODQI5Hs4YGu_OQyiEVd7Oh7qfZAgwvDZRbGFaWKHoKHlgPhtm-Aabo5xenETJ6Ko0FqySIZ_XtRYDkorA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6205" target="_blank">📅 12:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcwUGXX01GJUmkDwOkcdPNZgmzWxv0SM5R2gZFU5G65WK2gPVMUmMQ-HhEQaQyN5BL7PSTKf_r8d9t7U5y64a0Q2rlC2b63d0Ufadf03VtWyGpzRSzK13TjPFui-LdRVPrr6SmeLpZIFO5_1_3q72VU0MTSICDjNuHxGczlRrJME42kCEhqozaLj_S3tUUu3OlBhZZxng-kfTR9_aubm7emglWhfLGqVsrJlDgOVNBN-sXuipV24OewxLNDyMmkGDNnHm2UzaMMLMfRr2U6Stqy_7Coi1Pk59jSYDjCpySxRCwo9fLDcZvRuAezBqKkvYDdiOaN05HT2N1bYp6SRhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6204" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6203" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=kI4Lup_pJu5sI1Hzhk50N6y9JljPO4CEcqDrRR36ZFwut1DOwP3wRI_rscO7SjRDhBPrIAaLYG1yaHfPAGZF2QaakuvAsi1AM4Jl0uLOxL0MmzdFoeoC5vLBKjaLHNNAp3Y9CNpCvba5gZx7PcGzp3eK3Z9B7qLyOJlf19RY-XH7NAGoPBjTloePIfqppbK1mNNXnM_XlOEsZ5m-VOtGam_v6JiauxPRYwRJHGJ02YhwoDZviJdrn1rdJm6VqKIApmNQjYSuviRc3lBKyDPtnnf4cQWL6bxOh6OUS_M7WkO9uybaGYhGYRVwhJiQ5cTUtPv_0p0QSV6lls2Rz4rkpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=kI4Lup_pJu5sI1Hzhk50N6y9JljPO4CEcqDrRR36ZFwut1DOwP3wRI_rscO7SjRDhBPrIAaLYG1yaHfPAGZF2QaakuvAsi1AM4Jl0uLOxL0MmzdFoeoC5vLBKjaLHNNAp3Y9CNpCvba5gZx7PcGzp3eK3Z9B7qLyOJlf19RY-XH7NAGoPBjTloePIfqppbK1mNNXnM_XlOEsZ5m-VOtGam_v6JiauxPRYwRJHGJ02YhwoDZviJdrn1rdJm6VqKIApmNQjYSuviRc3lBKyDPtnnf4cQWL6bxOh6OUS_M7WkO9uybaGYhGYRVwhJiQ5cTUtPv_0p0QSV6lls2Rz4rkpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6202" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6201" target="_blank">📅 11:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7h72iqDw4vwZHlDiyZLMpZGxdmG97eqSxWjODZGagiAfeZJxfPUG0du59YOxXoWooiNCbmvCkEfbXeFPrL2MmjjNbuC1VF5PXcD9JhieeEr2_x7TjvKii3gowNwRCZsHesS6MNwFQG3FiZv3_MxAP5WsZoZ2cCMDRVRuIut6q3eipSnx4QNlIPxiW15vDcF2fKKBNflw2Qq79Hzp0GOnvSyPjVqRTXZi6UhQDV6Z-NypNBvDfBTLwN81y_AUY0gY53pgm2zQd6PTjEWVzf9ft1S0dUSkdqcaeyN4qhScwWDgNlglA09wrGIklGELSvm9nX5ZtFOXvzHS7Ax1lF3Gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6200" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee5737315.mp4?token=mBroxZSfFc0F1YlnBkIoL4Ir3z6SmQ959HWEzGKi-40BwQI7oLVgxJImg3BEZ0ss4iT2g_TTaFlsj7Rj83XhaQYYh3CSjvNPLcdW9dEONorsDBH5HSTvqFbYIaeg3Q8rc77ldqE8JgJxFEAgJbAd69qQWnqiCNoGrAkdxIKwpLNqdCWVq4UmfW7O7E85QNzP_oH6aXPbsSQylJTUiz5OIZbmNG1WVqEugS5ikL4KWYXFo1Wnbe5bqgLhhYB6-2dgz4CxiVBlpx7n_zn7-2CtU-t1XdoAIimIEYFklRxrw9fzvLXTJGI01n29omdKY8jc17OjTFKyAYm0UgdCMXdUsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee5737315.mp4?token=mBroxZSfFc0F1YlnBkIoL4Ir3z6SmQ959HWEzGKi-40BwQI7oLVgxJImg3BEZ0ss4iT2g_TTaFlsj7Rj83XhaQYYh3CSjvNPLcdW9dEONorsDBH5HSTvqFbYIaeg3Q8rc77ldqE8JgJxFEAgJbAd69qQWnqiCNoGrAkdxIKwpLNqdCWVq4UmfW7O7E85QNzP_oH6aXPbsSQylJTUiz5OIZbmNG1WVqEugS5ikL4KWYXFo1Wnbe5bqgLhhYB6-2dgz4CxiVBlpx7n_zn7-2CtU-t1XdoAIimIEYFklRxrw9fzvLXTJGI01n29omdKY8jc17OjTFKyAYm0UgdCMXdUsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6198" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌐
اختلال VPNها در روسیه وارد مرحله جدیدی شده است.
گزارش‌ها حاکی از آن است که فیلترینگ در روسیه نیز دیگر فقط بر اساس IP نیست و اکنون الگوی ترافیک و TLS Fingerprint نیز بررسی می‌شود. همین موضوع باعث ناپایداری VPNها، MTProto و پروتکل‌هایی مانند WireGuard و VLESS شده است.
#VPN
#Telegram
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6197" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6196" target="_blank">📅 03:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">قابلیت جستجو در وب در ربات هوش مصنوعی وگا اضافه شد.
🔍
همین حالا بیاید و اون رو در پیویتون و گروهاتون تجربه  کنید.
😉
@T_Vegabot</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6190" target="_blank">📅 01:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6188" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=ubbCtvkrLgF0G5tRGKTaNcJzMROctIPXsChuVYIRRhncy8ki5CFRc96nfu0QGhjWCNDc40syuqGNXI9GKqpH1VdF-e7YHIGD5sT9KDFuHwlLhkWt4EX-TltQTR0qb0RmqRe3P7uFyZL6JJ97UcmM03qqIxT76X3XymBvTMW4dW6_cV9esCm1_qWMl8qM0Rq3iaCMWGDuycQKQO9sfp6ZTfaRWEdwuVtU5xG5UOqR_WVEY7FwktkIZZq_WZBdPo7sL_LALYtm1BFe-UssyZyAMOwHGjQrNBxo9x_tMDoKHnMw2K3BppT__cV2P1g4-cMSt1Iur7uQWfaPz_Gm1jbNng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=ubbCtvkrLgF0G5tRGKTaNcJzMROctIPXsChuVYIRRhncy8ki5CFRc96nfu0QGhjWCNDc40syuqGNXI9GKqpH1VdF-e7YHIGD5sT9KDFuHwlLhkWt4EX-TltQTR0qb0RmqRe3P7uFyZL6JJ97UcmM03qqIxT76X3XymBvTMW4dW6_cV9esCm1_qWMl8qM0Rq3iaCMWGDuycQKQO9sfp6ZTfaRWEdwuVtU5xG5UOqR_WVEY7FwktkIZZq_WZBdPo7sL_LALYtm1BFe-UssyZyAMOwHGjQrNBxo9x_tMDoKHnMw2K3BppT__cV2P1g4-cMSt1Iur7uQWfaPz_Gm1jbNng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍎
Siri AI: تحولی در WWDC 2026!
در آخرین حضور تیم کوک، سیری با قدرت گرفتن از Google Gemini به یک چت‌بات هوشمند با اپلیکیشن مستقل و دسترسی کامل به اکوسیستم اپل تبدیل شد.
🤖
این دستیار حالا با دسترسی عمیق به ایمیل‌ها، عکس‌ها و تقویم، می‌تواند کارهای پیچیده و چندمرحله‌ای را به‌صورت کاملاً بومی مدیریت کند.
✨
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6187" target="_blank">📅 21:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=TTMOC4q7DhvxtrmT06nbrwiELnZexmdSaE6gnnnbUOeigpKoqyUo8HrKtYi3j29VHyTukYWFlWAfxfcdnDmvApAhTggy2oCjt5HKUIm1rW1yt_hc8dU77_2q9nJhMbWnszKx8_YBd2fYv1nqsrw7LO8bFqRrQ0KVJ2yq0Z9jWA0zZ9juVcIDfeXivQ1bc7Ziqr4ASGjeDvBVZ2OnVFOeOLVFgbOjIdvr_H8HFxXrsisvp1N1o_8_rjRM3wLYMfI21cxynVmLGpIG1xHTem5Q74uH6r-FsrECbCnhgA6JoxL2rxbIIiwwt_UKGBl0XM1wtZoJbAMYT6QpRGE9UeLyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=TTMOC4q7DhvxtrmT06nbrwiELnZexmdSaE6gnnnbUOeigpKoqyUo8HrKtYi3j29VHyTukYWFlWAfxfcdnDmvApAhTggy2oCjt5HKUIm1rW1yt_hc8dU77_2q9nJhMbWnszKx8_YBd2fYv1nqsrw7LO8bFqRrQ0KVJ2yq0Z9jWA0zZ9juVcIDfeXivQ1bc7Ziqr4ASGjeDvBVZ2OnVFOeOLVFgbOjIdvr_H8HFxXrsisvp1N1o_8_rjRM3wLYMfI21cxynVmLGpIG1xHTem5Q74uH6r-FsrECbCnhgA6JoxL2rxbIIiwwt_UKGBl0XM1wtZoJbAMYT6QpRGE9UeLyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Apple
#WWDC26
has started
Watch live:
https://www.youtube.com/watch?v=hF8swzNR1-o
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6186" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY2xTry9WQHkykAtst03rY9ns2uwaj0vxdTDB6cBWPAeDWcbwCByFbJu65ktNBml-_cNOyHDXMpRZRyveQ_TQcLTstsKvyJl9P79klMaSRLiv1mX-lE0S9YnIMBg5SZ8ML6BLCDXksHYv4k6xnbafGmZvk5gxySOpr82AEqKibQI_sZdMgbIk7x1jite5N0GX5DuV4exjoqrDviy0rFSAQ0uNgi92omdzmFSCU0oOPIYFObGkhU-2lWxzOtKPx_Kyl8T7LAX1vOaFJ_O7JlOSdns4Y3PUyCEPd_yNZCj3X_ERlFYqynX7wbRoE3azjqqTpHXqbBYMWFWTdMt23-BCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت ارائه APIهای هوش مصنوعی رایگان
🔥
از مدل‌های چندوجهی شامل متن، تصویر و ویدیو پشتیبانی می‌کند و یک راه‌حل توکن مقرون‌به‌صرفه برای توسعه‌دهندگان ارائه می‌دهد.
🔗
https://agnes-ai.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6185" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🤖
Kimi Work
دستیار هوش مصنوعی که کارها را خودش انجام می‌دهد
نسخه دسکتاپ Kimi Work منتشر شد؛ یک AI Agent محلی که می‌تواند بخشی از کارهای روزمره را به‌صورت خودکار انجام دهد.
✨
قابلیت‌ها:
• اجرای همزمان تا ۳۰۰ ایجنت هوش مصنوعی روی سیستم
• کنترل مرورگر برای جستجو، کلیک، تایپ و انجام وظایف مختلف
• دسترسی مستقیم به داده‌های مالی از Yahoo Finance و World Bank
• سیستم حافظه برای یادآوری ترجیحات و سابقه کارهای شما
💻
قابل استفاده روی Windows و macOS (Apple Silicon)
🔗
اطلاعات بیشتر
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6184" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndBoxgT3SvdQazRzr6IKrwyJJFRwrh5B4yZ88b4iS20MaA6lvsy33uAB2lp0wJQbr9w-xMZTIw1NtTKdkkhu2Xxbe5fB8JZz5tHqtdsokbb_DdiD0KaqEte218_YkZopfvAQWUXDcULJpvog_zZ8xT0H13aztTR1x5Wnm8VXj5oPHiPmULRZ_oCSTM43VB-R3RGXPruayiMlBveJChIN25PMQWVTjUBS3r3OWz78QmKrqMu-J1dD7brzFxYg37mbYkeHUfOCvB7c_4IgWaztAu9ynQ0If3SVE05N9IqrxIbNCPRAxxusZ2_uSp2yKArFMYGpgGMy8RanWjDX2KLxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
جعبه ابزار رایگان ویدئو
🔸
فشرده‌سازی ویدئو برای صرفه‌جویی در فضا.
🔸
برش سریع.
🔸
حذف کامل صدا.
🔸
ایجاد GIF از هر ویدئویی.
🔸
تبدیل بین فرمت‌های محبوب.
🔸
کنترل سرعت پخش.
🔸
افزودن واترمارک‌ها.
🔸
ادغام چندین ویدئو در یک فایل.
🔸
همه چیز به صورت محلی روی دستگاه شما انجام می‌شود.
https://www.zipvid.online/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6181" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
هکرها با سوءاستفاده از ابزار هوش مصنوعی متا، بیش از ۲۰ هزار حساب اینستاگرام را هک کردند
شرکت Meta اعلام کرد حدود
۲۰٬۲۲۵ حساب اینستاگرام
در جریان سوءاستفاده از ابزار هوش مصنوعی پشتیبانی این شرکت، در معرض تصاحب قرار گرفته‌اند. مهاجمان با فریب چت‌بات پشتیبانی مبتنی بر AI، موفق می‌شدند ایمیل حساب قربانی را تغییر داده و سپس رمز عبور را بازنشانی کنند.
🎯
در میان حساب‌های هدف قرارگرفته، نام حساب‌های مرتبط با
کاخ سفید دوران اوباما، برند Sephora و جان بنتیوگنا (Chief Master Sergeant نیروی فضایی آمریکا)
نیز دیده می‌شود.
🔒
متا می‌گوید این آسیب‌پذیری برطرف شده، لینک‌های بازنشانی رمز عبور نامعتبر شده‌اند و حساب‌های آسیب‌دیده تحت اقدامات امنیتی اضافی قرار گرفته‌اند. این حمله عمدتاً حساب‌هایی را هدف قرار می‌داد که
احراز هویت دومرحله‌ای (2FA)
نداشتند.
💡
این اتفاق بار دیگر نشان می‌دهد که واگذاری فرآیندهای حساس امنیتی به سیستم‌های هوش مصنوعی بدون کنترل‌های کافی می‌تواند پیامدهای جدی داشته باشد.
#Instagram
#Meta
#CyberSecurity
#AI
#Hacking
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6180" target="_blank">📅 18:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaWsUSVx1Ru5hbm0gJ5jlgrL2DtZgzY_BHKsYsznhekgkfztWgya_ifO56WKyfWke8-KFH88wxx4SNOWGO9EDTlHeC0WN7p8xDWeEPYQ3oZxIn0LXEFDD3LcI34hPh4Pq8kp0QvMQ9xnnFqB4gjPZkiDf7foBD2tVgCq7l_HahtibjVbh7HccHwxGF2sAkI72t622HDf8tGwPzJWvuKpn8Yq6aHG4mQi4kB4OXmfuWDL8b-IAC05LytvQCmOCjSSoJMexAGHlN2XZu3LvGUhYuVYbHozEhTzvfzFjHPqzCshGXmAdAVzteYWKJCJsvPZYCRGvY6JMqI-1GDLsuMV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦾
شبکه‌های عصبی اکنون شبکه‌های عصبی دیگری می‌سازند — با عامل هوش مصنوعی خودکار ML Intern آشنا شوید.
⚡️
دیگر نیازی به یادگیری کد ندارید — عامل هوش مصنوعی مقالات علمی را می‌خواند و مدل را برای نیازهای شما می‌سازد
💎
مستندات Hugging Face را مطالعه می‌کند، مجموعه داده ها را جستجو می‌کند، کد می‌نویسد و آموزش را اجرا می‌کند
💥
خطاها را پیدا می‌کند، کد را اشکال‌زدایی می‌کند و شبکه عصبی آماده را مستقر می‌کند
🔗
https://github.com/huggingface/ml-intern
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6179" target="_blank">📅 18:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
کمپانی
OpenAI حالت Lockdown Mode را برای ChatGPT معرفی کرد
🔒
شرکت
OpenAI
قابلیت جدیدی با نام
Lockdown Mode
را برای ChatGPT معرفی کرده که با غیرفعال کردن دسترسی به اینترنت، Deep Research و Agent Mode، خطر نشت اطلاعات محرمانه از طریق حملات Prompt Injection را کاهش می‌دهد.
⚡
این حالت به‌طور کامل جلوی این حملات را نمی‌گیرد، اما آخرین مرحله استخراج داده‌ها را مسدود می‌کند و امنیت بیشتری هنگام کار با اطلاعات حساس فراهم می‌سازد.
💡
با وجود این قابلیت، OpenAI تأکید می‌کند که Prompt Injection همچنان یک چالش حل‌نشده در مدل‌های زبانی است و کاربران باید در استفاده از داده‌های محرمانه احتیاط کنند.
#OpenAI
#ChatGPT
#AI
#CyberSecurity
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6178" target="_blank">📅 17:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
ss://2022-blake3-aes-256-gcm:dxzSnG5le2y16bNqdyL2Hj2b9Qjptq2Ust7li7mLR6Q=%3AGZs23OkRjsO4i11hMhke9I48yENOx6VVuL23GKRXTi0=@37.32.8.201:8080#%D8%A2%D8%B1%D8%B4%DB%8C%D9%88%20%D8%AA%D9%84%20%D8%A7%D9%88%D8%B4%D8%A7%D8%AE%D9%84%D8%A7%D8%B1%DB%8C
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6177" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q947Q-s3w1568Bpbtial-bxZRP7KDMBctVwkGZ-IhvPu8pgpb7Tv5Gw07_1zvGwoVfIqwWU80dcy_N-DnYJslf6JgAb3hU2GA7zw_6sWggNA4ZjN2VO89L1yinxrra-qelWOJw-CQ5nD7ZVcGrHfeRtrm3tqloH1vF5lXzVm9ku1C2aFM2GhNvFjTggH2rWWwsng3h6Mld-bu4cZZzOY_La6k_q39WmQhsfnrSF7A2zVlr7AHPXaSkINdMAhV3vsJV0W2j6ZFshCic2aK0Vy3sUb75kN2QI0Zb2vZdWWtciLQd5wQvsIVUjpT65-N448rFLm13JH5pBZ5i2jGFMF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار تازه و ناب
🔥
@ArchiveTellNews</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6175" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6173" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=uuYnqNco-DLGcZ0x6oM63GfqXokgSkPhb9JCoTfO9PR4ZjHrt0ag2kYvuDgKsu_thtJM8aml5DGxivEhCwI0cSZhjFEL_yIuj3xPKcIaflWQHOM5572nv5zHFIZ0hn1zgiXcfVyCjXIkG8V_JsbSorJutSik1fanrolS8fIEs1GYHHRsym0k4ZV_h5TUk7Zl9Ghe4TRmwJ4XJ2JTsaLpJzM1XoFAfa4KkNiFe9YckImwGpAYg_XQt5Yl-APye0qItBOXLbZlWvrMyotgTgaGU7YC339fpHQdVgrZBeT1T5aJJX6wBd5KCnAQVl5DYJ7I9MH3SnCkhzFGLHo_wts4_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=uuYnqNco-DLGcZ0x6oM63GfqXokgSkPhb9JCoTfO9PR4ZjHrt0ag2kYvuDgKsu_thtJM8aml5DGxivEhCwI0cSZhjFEL_yIuj3xPKcIaflWQHOM5572nv5zHFIZ0hn1zgiXcfVyCjXIkG8V_JsbSorJutSik1fanrolS8fIEs1GYHHRsym0k4ZV_h5TUk7Zl9Ghe4TRmwJ4XJ2JTsaLpJzM1XoFAfa4KkNiFe9YckImwGpAYg_XQt5Yl-APye0qItBOXLbZlWvrMyotgTgaGU7YC339fpHQdVgrZBeT1T5aJJX6wBd5KCnAQVl5DYJ7I9MH3SnCkhzFGLHo_wts4_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
AlicentAI — هوش مصنوعی برای ایجاد محتوای متنی
💎
این سرویس پست‌ها، توضیحات محصولات و مقالات را بر اساس درخواست‌های متنی تولید می‌کند.
⚡️
از طریق وب کار می‌کند که در آن می‌توانید بلافاصله نتیجه را برای نیازهای خود ویرایش کنید.
🔗
https://alicent.ai/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6172" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">برای مدت کوتاهی اخبار مهم رو منتشر می کنیم
🙏
❤️
کنسل شد نمی کنیم
😂</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6170" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
تهران پارکینگ‌های زیرزمینی را به پناهگاه تبدیل می‌کند
بر اساس اعلام شهرداری تهران، در پی افزایش تنش‌ها و حملات اخیر، پارکینگ‌های زیرزمینی در سطح شهر به‌تدریج برای استفاده عمومی به‌عنوان پناهگاه آماده‌سازی و تجهیز خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6169" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم  بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6168" target="_blank">📅 12:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم
بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی یک عملیات جدید محسوب نمی‌شود، بلکه ادامه عملیات Operation Rising Lion (شیر خیزان) است.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6167" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نت رو قراره بزنن
ای‌ک</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6166" target="_blank">📅 12:36 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
