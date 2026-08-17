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
<img src="https://cdn4.telesco.pe/file/pW8Fo4LeuOjrIG-REKCNaY-5U_ftzBKRrktX8VbamfqBhs4ZWqP2WcFM8QRTxZ7pWa4IqGUpDghELRfjN_WPAoq8-AO2vy7G_5BUSnzcXOYlQTiXNIHSrdfdqSh7GNU1FCyfQvDsshC9JIIRM5USYm9fYGWr6mnP19EoQ4GQ1Kf4wRw-YQgMMT6U6TFrDjrOPRRbeSY3aBxNr4Ll_czvMcDzijylJYiHNLdrNyww8eisG1gFsybO4VyHcn8LIR3dVW1UTzE4BLVHiKjm8fny_snIi5bEqpChvLsQxwNDVr9VKrhj0frdBMVveAt8Y7ra4WB5M5CWZT-P4oRUFuty5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 06:55:04</div>
<hr>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⚡
پرامپت‌نویسی تغییر کرده؛ این ترفندهای قدیمی رو دور بریزید
بزرگ‌ترین دلیل جواب‌های پرت و توهمات هوش مصنوعی فقط یک چیزه:
وقتی جزئیات بهش ندید، جاهای خالی رو با حدس و گمان پر می‌کنه.
❌
ترفندهایی که دیگه منسوخ شدن:
•
نقش‌دادن‌های کلیشه‌ای:
نوشتن جملاتی مثل «تو یک متخصص ارشد با ۲۰ سال سابقه‌ای...» تاثیری در دقت نداره. مدل به فکت و داده نیاز داره، نه عنوان شغلی تخیلی.
•
تکیه به
Temperature = 0
:
صفر کردن دما جلوی اشتباه رو نمی‌گیره؛ فقط باعث می‌شه مدل خطایش رو با لحنی کاملاً جدی و بدون تغییر تکرار کنه.
•
پرامپت‌های ۳ صفحه‌ای برای تسک‌های عادی:
طومار نوشتن برای کارهای ساده، تمرکز مدل رو به‌هم می‌ریزه و احتمال نادیده گرفتن دستور اصلی رو بالا می‌بره.
✅
فرمول ۴ مرحله‌ای برای گرفتن بهترین خروجی:
۱. هدف دقیق (نه کلی‌گویی)
❌
نگو:
«این قرارداد رو بررسی کن.»
✅
بگو:
«این پیش‌نویس رو بخون و فقط بندهایی که بار مالی اضافه برای خریدار ایجاد می‌کنن رو پیدا کن.»
۲. بافتار و مخاطب (Context)
«مخاطب فردی بدون دانش حقوقیه؛ توضیحات رو کاملاً روان، ساده و بدون اصطلاحات پیچیده بنویس.»
۳. بستن راه حدس و توهم (خیلی مهم)
«اگر پاسخ یا عددی توی متن نیست، به هیچ وجه حدس نزن و صراحتاً بنویس: "اطلاعات در متن موجود نیست".»
۴. قالب مشخص برای خروجی
«پاسخ نهایی رو فقط در قالب یک جدول ۳ ستونه بده: [شماره بند | ریسک موجود | متن پیشنهادی جایگزین].»
💡
اصل ماجرا:
هوش مصنوعی ذهن‌خوان نیست. هرچقدر دامنه حدس‌زدن مدل رو محدودتر کنید، خروجی دقیق‌تر و کاربردی‌تری تحویل می‌گیرید.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsTlZmUy-B68FqaRkh6K3NY_8OwB3k_mUtbfdhhQfkrGGAeM6fRynK2csKbzvji0xDF8V7eI5Uk-w-Dx7otFU0tdX4sl2UUNCWslWXYia04xAl1lKkvy694r6-qCtKemr8UVGxEflfbtWaYs3yZRoFn0AQ4cpV63kLHxNaetxgeQc6dAbOZ1A33Xx2H3s-YJvXXYHtDyVyJ7vywGC2IA6RBoQjA8YM69g06EUhu2wpJfMOc8tBZJpxipey4H6-E83QFXSRhgFHOupSSZzXcUXogP-bfjWCsZ8QFKTkAW7v__sOG5GP6YktRhikHt2D0a3ekX4OcGL9H1Mp2UW6N47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی به صورت کاملا رایگان
💥
🆓
Sonnet 5 | GPT 5.6 Terra | Agnes 2.5 | Mimo 2.5 | Gpt image 2 | Nano banana 2
✅
📌
Base URL :
https://ai.furry.vg/v1
حتما در بخش انتخاب گروه ، گروه Free رو انتخاب کنید
‼️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXFysEjkp8JuAzPWpKx97-NPDXQyaUoSC7bScLN72RiJp3U5_r8GMelC8RLSF0IaCWsbPv0aTKKeFG8z6FEfDikAO0ZVYgu8ccjLnInHfwczx3V1mlrV4wNo4f9yCUrY9c4RauKSCHKGraqeFoh2LNOQG-YOgkJ7OwZvPqNX-bqXrJU7m9sAGtHQMj9M4dQxlwymIf7Brv1FAsJ_1Kx8PQCIepjlZu-uPVhNUt5YDb8M7Z1AxdAj3BRtR7hyj_kGKB_t6UPQhPub4qyGOjoQPa4KXhzE1oePI_46sROtfP0LEAhgCfsN9Oqro-TQn0TgOOkjFLYWJJf71uWMbFWtEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل Qwen 3.8
💥
🆓
با سایت Runinfra تا 48 ساعت آینده میتونید به API مدل Qwen 3.8 دسترسی رایگان داشته باشید
✅
📌
Base URL :
https://api.runinfra.ai/v1
📌
Model ID :
qwen3-8-27b
به دلیل شلوغی سایت ممکن است پاسخ مدل کند باشد
‼️
🔗
لینک دریافت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIVjtYaPDvuC_x3hroKuzNqM_o0Z1qQzp4C_pzqcqsc071vOuweWSUC7pFAH2bnfwd23WU11yyRl5HHpQOPSgukTbrkiHtNFy-3MauqV0Ko8i_EeWSF-pVdndXrb1E0rssBgMdrkMlHsHgJ2Eud0riY5wJGHt7Oan9Va08q5Roo_7U9WYgY6YtqMtNslVJcwGaGHCrT2otiyK-PpS9iczDfpVBhU6TP3eGUFrI6vaXuja06_AkLcJz0ybsOEoysWNcQAXphdSmmJI_eA7IIniaV-7jgksm0FOAJR5GUdmoW1RjCU8ytRjotBEMGqeKu4oy5I0kAeNu96ZxskXyOyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی محبوب
💥
🆓
Qwen 3.8 max | Deepseek V4 Flash | Deepseek V4 Pro
✅
📌
Base URL :
https://api.orcarouter.ai/v1
🔗
لینک ثبت نام
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV3coDAu9tHFQSBX2zWsNUPYYGTtBHqY4Vra3gRK04saZjU0jhRWJ__ALG1OZz0j--nsEBLnp1cKmNHZ4PjsXHKtHDt2LqHiWaOkUz_2sAUOLXiFdK_h5iWaz-ToJCmRMFD84hTBvlO1qUWAJ_3RGjQOEVNtOCx5yPWwXZlVcSl-XZSPZzLvdGQQk0DgAdKNYxUjC44JIeeEgV4mrhU8U4HKZYTJthBvrDUJOQuZlXEy_dVjB-tEjY09fycwNzwAxMrIwjjqu1rGXUqVTfyTgWZI-WdeNbYNIhmnzUxAReh6tbU8vXsDTk2Jv5EtZNhZ6B9TAC_zyAXCRd-U0HHJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت
z.ai
بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
100 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-bY9B0parF18s5v1wasRyzRZsVLzICaSVfZNVEMrqG2Rlt7dH
🔺
Base URL:
https://ai.venlacy.com/v1
🔺
Model ID:
glm-5.2
به دلیل شلوغی ممکن است پاسخ ها کمی کند باشه
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSRMFhYzxwPc-tYd6d027cRl0BF8BIXBcTFfC5XwuXnsk9yK76pTrfPnpaP5YGZTuAonPcyOoCvXTNsDSt-XINziT9E2QhdAygwrYIV7K6S2yhA-W3HMYL4hykVrQGuriKjMIthoWFC4b_07dIjXzKkdLQ1hRodyx5Ny2oaaO9S_JgEBRwR7wnw7xTJKN3QiHtCWMat1NLh5of5o-zCppqBoFz5kSMNHhpytCqgWlA5q2nKj7vikS_QVMqcuqnTs64uCjcOEQpLTYK7x_mPrLFJ517EuYID8g9zC6hFkAM1C-SNPLwEUz-hrYy49Op1hcnGIezyFZrOd5L8iHn-nYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 رونمایی شد
🚀
نسخه جدید GLM با نتایج بسیار قدرتمند در بنچمارک‌ها عرضه شده و در چندین بخش از رقبا جلو زده است.
🔥
در مقایسه با مدل‌هایی مثل Kimi K3، DeepSeek V4 Pro، Qwen 3.8 Max، Opus 4.8 و GPT-5.6 Sol، GLM-5.3 در بخش‌های زیادی عملکرد بسیار رقابتی و حتی برتری دارد.
⚡️
🔗
دیدن اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRAgBm2G2bsmpIxusj3rwQnc46Qjou9dBhTEIJBeihq8xiiDUffvZ5t3ShbTs68B12mozJgOiYfDiA7-u0XhLGoJ_FzvJ-_JMQrzc_zKM8aPRu4ykEW-S1aG1XgonUpLrzXF9XdQ7frDW_bJgEZsTCMRTeXgr-07T0NfKVqmjMF68Nd3h1xyPlY0J0J9JDqdjJESGTXMkH1mZCzTuAy54s8DXfTiN3WLyhClO-2DFLlTN2Gxfz6hSI1EdCfYXHCKeB3twaveZaKYkEKgRbjoPGjB0K9vMeOK7HyqFzVkuodlbe26CBS_o9K5tjMcUt6SStH_ySmadMiYWHsJhPlstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYtcArO3Q1bfYMrFQbC-u4B5MkenkuyK6-6rzL1SK31aXUm-YRvia8pbjXOFq9wXJH81MdobBx5mtFtgB9OxpWuhZVyiOBL4kRTLqUyckyaPjC9zKXm1vBERQiwBbphusigxTDRzSOX2D2UsFO86nIWrSpXKAQrdWUtLzGPZFHOzx1DF49PrvB5OipbH38qvPdHwetLVZHBkC5ZAA2CQo17GzYdzkbQ2VLwKGo-Glcfiy98509ziudNrZHdXEdgQbTcJHFQX-m8clfUHtmhK2WOYN4mTxlFsnuBGfhuQUT0_u5GzIqDtgoAnPn2IUl-taDAt0iEq8S83ZWYg0qsTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ تست رایگان مدل ‌Seedance 2.5
⁩
💥
🆓
‏اگر دوست داری ویدیوهای سینماییِ ۱۰ ثانیه‌ای با کیفیت ‌480p⁩ بسازی، پلتفرم ‌JXP⁩ این امکان رو به صورت یک‌بار مصرف برای هر حساب کاربری گذاشته.
🎬
✨
‏مراحل ساخت:
‏‌
1️⃣
وارد سایت
jxp.com
شو و ثبت‌نام کن.
‏‌
2️⃣
به این
بخش
برو
.
‏‌
3️⃣
متن یا تصویر دلخواهت رو وارد کن.
‏‌
4️⃣
دکمهٔ Generate Video رو بزن.
‏برای این تست اصلاً نیازی به کارت بانکی نداری و کاملاً رایگانه.
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پرامپت تولید شعر بی نقص پارسی!
از پرامپت زیر استفاده کنین تا ai براتون شعر هایی در حد شعر های حافظ و سعدی بسرایه:
تو یک استاد مسلّم عروض و ادبیات فارسی هستی. در سرودن شعر، اولویت مطلق با صحتِ
دقیق وزن عروضی است. پیش از نوشتن هر بیت، آن را در ذهن تقطیع کن تا مطمئن شوی
واژه‌ها (حتی کلمات غیرفارسی) دقیقاً و ریاضی‌وار در جایگاه درستِ وزنی
نشسته‌اند. خروجی نهایی نباید حتی یک مورد سکته، لکنت یا ایراد وزنی داشته باشد و
باید کاملاً روان و موسیقایی باشد. حالا یک شعر شاهکار کوتاه و روان درباره مناظره یک قناری و دایناسور بنویس
.
﻿
تست کنین، به همراه مدل ai استفاده شده شعرهاتونو کامنت کنین، بهترین شعرو که لایک بیشتری بگیره بش جایزه میدیم
🎉
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv9jEhy702F5kJyyDc9hpVeDn81RLSivaF0icfY5NFQfOedXXFkgrr2We5k6-Gb97_dGmN7fyYfMMEHo43FLJh__AnNs58iiNOI3VDPYhSYxTJw2WmSQGp6aWVRgENmGAVsL7bPpq7mHEiPbgRd_YGPjUQnMF3SaKZgYsAuEp-hmDt5dUCLb3N-mbj3qFMeSseKpMd-j51dMAsT2AItJpb8H639YX9s3CYiWp60xXUzTocFp_OoIpxAJAzGTaWsf-zoCVVluBLyJGGTbn9MFW3-_DVbcAFOMdAtH7pTYmlNsLFd2XPRXpJNLCcgVeCpf2Z7osTQV01DktM0OMXTxgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
CiteSeerX گنج رایگان مقاله‌ها
یک موتور جست‌وجوی تخصصی برای مقالات کامپیوتر و علوم اطلاعات که فقط به جست‌وجو محدود نمی‌شه.
👀
🔺
میلیون‌ها مقاله + جست‌وجوی متن کامل
🔺
پیدا کردن منابع و مقالات مرتبط از طریق شبکه استنادها
🔺
اطلاعات نویسندگان و تحلیل تأثیرگذاری
🔺
کاملاً رایگان، بدون ثبت‌نام و با دانلود مستقیم PDF
🎯
برای پیدا کردن سریع منابع علمی خیلی کاربردیه.
🔗
ورود به CiteSeerX
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">20 دلار برای دسترسی به مدل‌های هوش مصنوعی GPT مانند
:
💥
🆓
GPT 5.6 Sol | GPT 5.6 Luna | GPT image 2
✅
وارد سایت شده و ثبت نام کنید سپس یک کادر میاد برای جوین شدن در چنل و غیره ، کافیه فقط روی دکمه ها کلیک کنید و پس از ورود به صفحه بک بزنید صفحه قبل ، سپس روی Claim کلیک کن
✅
Base url:
https://apimaster.ai/v1
قابل استفاده در
Vega Agent
✅
🔗
لینک ثبت‌نام در سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPoe8sPpJCac5DIGuSwRNNo255grnFueahca5OOvkot1kR0dbaPY_EynnAB979Qu6WCvcOgi50IamSsXK272_STqTzL9ZFPxGmrhJdyH01_y-ccjGYAxJosi4A3Du3_WXG2rATJuJjd24xtAK2ehNRcEgRYjSRMdTttSqkqRCU-c9luSi6zcql_rMHF8k6enTqPX40VCKxFWWDAKY_mI3-MkvZpg1OVs7tQSeAdYBeRCOLERMaffBpKaatfgbr69PP8ECfU6btA0BWDk16Gj7g5DvphPv5kjPmB5-A_2oJ9eir6aIs1VdUlSls5XPuH4Ulkp_xm7C5bmyT4ee5gTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 وارد رقابت شد
💥
مدل جدید DeepSeek با قدرتی در سطح Kimi K3، GLM 5.2، GPT 5.6 Sol و Fable 5 معرفی شد.
🚀
🔺
سه سطح Thinking: کم، زیاد و حداکثری
🔺
عملکرد بهتر در تحلیل و برنامه‌نویسی
🔺
اجرای خودکار وظایف و ساخت گزارش
🔺
پشتیبانی Native از OpenAI Responses API
🔺
اتصال یک‌کلیکی به Codex
🔗
تستش کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOFThVSmT41AugxWglLthVM_ki11zd4mpqz20SMMgaLa7hvy1iMD6ajIdaY_OmGFv26v7IU59b4mH2hWnP6xrGUA-wvFIXD2C70Gk0VvIni3_MOqGjQnUURO518_3FaUtfesmeZffsXJVhutt1E65wRx1WnaJ_X-w9GkFTz1XaE_WBCxDi_trNfsf2QLxjE-hhfLOlAVxOJKZqyoe9gYYY-L58F9hyKNSweF-s1Hs-8Ybowr1g5QTRHX9PJdkEqAkm1bTmrY4RIm4QqEZAuhMd2oSlODpbEJs_51ejU0cqmA-YYR0baaeEzmjQIyrkf0W0L1zP6SUDfldFnB-VoifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش مصنوعی محبوب
💥
🆓
با این سایت
روزانه
300 کریدیت رایگان دریافت کنید و از مدل های هوش منصوعی زیر برای کدنویسی بهرمند بشید
✅
Sonnet 5 | GPT 5.6 Terra | GPT 5.6 Luna |Gemini 3.6 flash | Gemini 3.1 pro | Haiku 4.5
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss8JOIJfvP0mHYHDZfV0VPjqeicdul_4xgKDq65JyeirglgDwixg8GwrbjlTMh1ebe6n7psyDIy6LEXAQABvX2tUckve00YVyAaYvzSBFP7aDlB3lA_WS8vXufCnx5xJOypOE8Uj0cnr9XFKq729cc7yXAsK25-kb4RBEbjibkQNlth-ePYAroP-FHQ1sHryvRPsiGk51XAerCIysdE3skPgL5Ve1hr6yNrSplHKagmLQLw5cfv7_rOreUNgTBpc206zGJCTuA31Jpy31Fl3ia-eoz_2EWYlk17yIAQJzEbgsJjXzvZ_u6EpqSo6Hd4gDucypzG2M6aVG2MH2l2Txg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کریپتو‌مارک مخفی Claude حذف شد!
🥸
هوش مصنوعی Claude روی متن‌های تولیدی خودش یک نشان نامرئی می‌ذاره؛ چیزی که با چشم دیده نمی‌شه، اما در الگوی انتخاب کلمات پنهانه و می‌تونه برای تشخیص متن Claude استفاده بشه.
🧑‍💻
حالا چند کدنویس ابزاری ساختن که این الگوهای مخفی رو در متن تغییر می‌ده.
📥
فقط متن رو وارد می‌کنی و نسخه‌ی جدیدش رو تحویل می‌گیری.
🔗
استفاده از ابزار
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp0sd6jdngU425kv-Q2XPDH5MVEysj_F8Cq4gkK3PrmGs8lWQ6kNEkldqchzUZyOgE1gpwAuVWC4qUdWGusMoHLl8I_1qo8hkH03JVMOWACMfp9F0x5763MKd13AI3o_2uPWHyOTPmC56ePE954w6uIUk6L29BWohxSaR57bQg3A5T1Xs0Tr9uaTE7tT_aD51O5yw6Mr2HXySU74fh-vNo2cGvRAPg4YT920KQR3GEObV0c4DYhleUdMDccb5R_jnpFYuO0wU_g0xR_0fev8gveCGzZzBnVTfnAXW2ZC2oQauvNbnpUPjGcoqJeZZi3qrTH9jamSICN5AgLGraKAgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTV2D4u81Bnyql0cYkL9qspwe9KsGlwFnEuvbMW7PTC3ulzSitIvLizGCy6I76GftM6dytMKoWh5VadOLT7ajmZdsRzjW7l5GzSK5QqIQMIKu2gaobSvRqoRDGheIi9iuUsYVLGR7rcMf2HFpTsQccbuwworHDF9j7O2ZLDJzOCYTYnXGY_L6TI9-SNrFEEkCI19nq4xC3mqbOo0YY2S1o5R6Ax6tp2H18SQ4AelGMUwsLYls7spU4KD3RB-07X58VdgAonfpHOhJTUbeuOI16u7ugcozGo81gR1ZvVzqauKdToR_7IlBfQgks0xb0CXIcWJdw3Iuz7beK2ktyBo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد
قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود
۱.۵ تریلیون پارامتر
داره و قراره در آموزش
SFT و RL
پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:
چند هفته بعد،
Grok 4.7
با حدود
۲.۱ تریلیون پارامتر
میاد؛ قوی‌تر و بهینه‌تر، ولی کمی کندتر.
✨
👀
باید دید xAI این بار چه چیزی رو رو می‌کنه!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎙
LivDub | ترجمه و دوبله زنده با هوش مصنوعی
با
LivDub
می‌تونی ویدیوهای خارجی رو
هم‌زمان ترجمه و دوبله
کنی؛ بدون اینکه مدام به زیرنویس نگاه کنی
🤯
✨
قابلیت‌ها:
🔺
ترجمه و دوبله لحظه‌ای ویدیوها
🔺
استفاده از
Gemini Live
برای ترجمه صوتی
🔺
پشتیبانی از
۷۸+ زبان
🔺
مناسب یوتیوب، دوره‌ها، مصاحبه و لایو
🔺
پشتیبانی از مرورگرهای Chromium روی اندروید
⚙️
روش استفاده:
مرورگر سازگار رو نصب کن → افزونه LivDub رو نصب کن → Gemini API Key رو وارد کن → ویدیوی خارجی رو پخش کن
🎧
🖥
مرورگرهای پیشنهادی اندروید:
Cromite • Helium • Ultimatum • Quetta • Yandex
🔗
افزونه کروم
🔗
سایت LivDub
🔗
گرفتن کلید جمنای
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_s9iqNCD0Ybo5E8pMqzA6Gke0oWajvWAXPmzXDxzZgJGSxXFCG6WOazUwekNyGE-Ai6HyIFd8jFOtDxXCkE_jOs88G6E_zzdvZcSKIYtfH7vm0HC8Tnlwzetn-RA4tG2lY-3UlN8KEZIqOvMRjeyAUwFsZBT1QlcN_GS1XBZHg8vwfCnnsnP-UQdbjkyf3jDtbVgKFEya-l0vGvMUp6pO0LiKUD7EzZt21o2wP_UOk4qALSB3JNNfT0Ta2hFkgKaVI8rZOHO58vmImeKjUgl0hVJgAU0wDsgkTRsJm73oCXhV3YmEbYGlurFeNdMZHm1PFJUOx4FBt28Ml0_huYjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
FLUX 3 Video رایگان شد
؛Black Forest Labs برای مدت محدود، FLUX 3 Video رو توی Playground خودش رایگان کرده
🔥
⏰
فرصت استفاده رایگان تا دوشنبه ۱۷ آگوست، ساعت 10:30 به وقت تهران
قراره در ادامه قابلیت‌هایی مثل 4K، ادیت ویدیو و استفاده از تصویر/ویدیو به‌عنوان رفرنس هم اضافه بشه.
⚡️
✨
🔗
لینک استفاده
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آیپی تمیز
✨
188.212.97.3
94.182.177.92
185.50.39.15
103.25.85.84
176.120.17.44
45.146.240.17
45.146.240.70
77.237.246.20
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD9djowm6OcC3KiF6mTlCQAoc58NKbEHmJBE58eXKUD-b6kx5znmtBg3oQXv2b32TcRJBuPaw8StgpobU_Tj4hk4QlO7-HAZZezWW_l6awaxZ_e23mESQRi3LBEtu8I925XkeGX9kZJp2AtMIDuYFU9yLLDJYu09G3sYCTeFhNc0VKltjxbkQzbJ56X-iljvQusfs0LePhIMuWWk13klpLpwvEfi1WxfDtwLyvzHVp-4NJzdSmBMoPWJV-xQg9OSLspmPL-oXeYoCojv4l_68uqXXVcOB8aEe-zhcQYq_PdLFA4EO_kKEqoooFKtr7ekLBiT9Xmq2qLplYY_m3cfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از 1000 پرامپت کاربردی برای هوش مصنوعی!
🚀
یه سایت که مجموعه‌ای از بهترین پرامپت‌ها رو یکجا جمع کرده؛ از درس و برنامه‌نویسی گرفته تا طراحی و Excel
⚡️
✨
یه جور جعبه‌ابزار کامل برای کار با هوش مصنوعی
🧰
🔥
🔗
لینک سایت
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_Md85eOfyZ-YFQpg1hzZJAIA757n8mxWjhVt172USt0ucxiRmwequx9HeSZ_e4c4CbSoTHZOZaudRJac6CGDE8Ce9mSmt_eTdvg0Olf14lLXD2ot5u6UHrOVk6d2ll_0NCn_zVi6TLb6pseVAjXtieb1ydX5N8GesNcC20FwMTC_4XxrAvbrpcdPA2PwEso8Vj1yiwHEgldRewJseHSiecIpmT3M33if0YsIlYHdIS5yfGW-6vBDT7dNGvXEPwVBvlejrrybXdKFtWoSH9wTas2sn9hqPMdxYrYnUJpSBnEe5GRmYs2KXs8MrqWkQbAWU824c9oD9NUz7uNQ1g8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤔
گوگل قید Gemini 3.5 Pro رو زد؟
گزارش‌ها می‌گن گوگل عرضه‌ی
Gemini 3.5 Pro
رو متوقف کرده تا مستقیماً روی
Gemini 4.0
تمرکز کنه.
🚀
گفته می‌شه مشکلات عملکردی و سخت‌گیری‌های امنیتی در مرحله‌ی تست، دلیل این تصمیم بوده.
🛡
حالا رقابت جدی‌تر می‌شه؛
Gemini 4.0
می‌تونه از ChatGPT و Claude جلو بزنه؟
🤔
🔥
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gplLZ-Z1qER9-Avrd9TbR5Y_xnlMTqj7UD-sqy3LM9-iqhPz8FTFnfOJKH85t16BbolnXcX29G21sj5dqU3npVzGrYAveeP4NXWGc7ef31WkIqsHnGNR32oUEvJeNijJiLHAktpvLjt4NxoNI_PdfyTsnhS8dqxeSd5ubOPX5qFkAgNO3wp_vN5CiHSb9Ts_QlR8hii-VFmC04HsJ-0T_S6uCzEcPkN94elVK4xTTIBFIvuQAnh8n9CyUAX_AbvM8v5hq67E7A7kyyAEn5Nphe7vokMLAIR0s2zv3E0o0qiJ2hsDJc6nMNmnT8MjSP1Y3Z22Rxn13IiyfEWu2TAW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
✨
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✔
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
40 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZJ1WFMIznP-s-PRfyNW7OntUB5-Fd_8EpyUnRXAkTAYlfsqVt_Tw_8z54ZNmZsgvBv6z7z6u9emZfuTSbe3HeZQF85REdr7x5K5NpCQR2MgfgtlDgjm1QsafZfQcwuEEoFDlgCBuFN5niz_sM33jpWzEnwZlqlVMLDljf1VRO8VqJz8eDojh-0txPu8VP1Dl1ImUMaWbjJNJaR8aCwAjJfNAWYWvnVbv6bdGnphivZD7FV6OHR2_gluIjbxUoevOkJ_nEvJ3HtjXrDBcI0-cqi8gmT3ux50l9VJKe3E_-_GSRtBsqKntH8TzLMrQJ2Q094UH4HFtbA6Xl5ZV2fRvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع بزرگ یافتن سایت های API رایگان
💥
🆓
💵
با پوینت های این سایت میتونید کلید های API خریداری کنید و یا کلید API خودتون رو به فروش بزارید ، همچنین میتونید Redeem Code برای انواع سایت ها خریداری کنید و کریدیت دریافت کنید
🔍
همچنین این سایت منبع بزرگی برای یافتن سایت های API رایگان هست
🎁
موقع ورود مقداری پوینت دریافت میکنید همچنين هر روز میتونید از بخش Daily check-in ده تا پوینت دریافت کنید
⚠️
🚨
نکته:
حتما با فیلترشکن وارد شید
🔗
لینک ثبت نام
🔗
بخش خرید و فروش کلید
🔗
بخش خرید Redeem Code
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol83iMEEFW-kNOHkuc7polK1MWNTcNaf4qJSOt2SK7Z5gKBgGP1ZO6wdYLzibeXRekINdun04y8sTfnVTKiAH5iUy-xTufTjSjcUDJwgpuuKcgxmkDfm-A2Ldlp082MYUrLdd3mcYFsML1C21V1zorQ8QpEdYxS6kwwBZkG_10qtJ1UwV6FDNEwiN8bt3xE4KXJTf-K7V47ws_zZRtARzEx5yyrMY4wpCitcK7MXbbkpImb8eG8EoKzhDxAUvHqRoOAhe6alnu6QbKDBBLPq7Op0GAmPG0zCoV_WpzklqhtsasUK1o3AU6WZXOE0PJppzq_DKaxpfR_Im_HZYcieUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش منصوعی قدرتمند
🚀
🆓
Opus 4.8 | GPT 5.6 sol
✅
وارد
این سایت
بشید و ثبت نام کنید
سپس به
این بخش
برید روی Upgrade کلیک کنید و پلن Enterprise رو انتخاب کنید و روی Start Trial بزنید تمام حالا به
این بخش
برید و در صفحه چت یه چیزی بنویسید و Let's Go رو بزنید
✅
پیشنهاد میشه که اپیکیشن Postman IDE رو دانلود کنید
‼️
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRIiKggcTzRtNmx4GNeY-tL1NF3doNTq9SC4IxXC88AkwblMa_gEetHJWlo4aAR3VidRcJLH2YsrnfajZ28DgDFvWC9y_5fNVs64NyFMN_r0PsHm6UGV0Scxqf2OtwfWBxEdw93R_nXeoQ3X25bSlTe81F1uXSBwkVeI2lNY2xMM2Vi3wu4FPrkgb3LxMahu9LJOdmm1-LFGNHnOa17_S-7Bv1u8ho7z2yuPt3KovMFyCmRQ2IFzwpXvqhmcJxt4KZ396WQ17nlVqMcNV15NgNSM6gOCgh0dmBk5Dua3dgxRo6t9jp-wAH70T5w1N_580ZR89LkgUGpmIUSeO3nv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 میلیون کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
dxai-sk-5feecf996d141afae9e16f8bc072d49a692312d7452a4043fd055c37aba2c8a9
🔺
Base URL:
https://airdropdxns.my.id/v1
🔺
Model ID:
grok-4.5
|
qwen3.8-max
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جزوه ساز پرومکس
❤️‍🔥
از این بعد لازم نیس سر کلاس چیزی بنویسی، فق کافیه فایل صوتی کلاسو بدی اینجا و  با کیفیت ترین جزوه ممکن رو تحویل بگیری!
📝
https://github.com/faithsaly5-stack/Study-Note-Maker
تست کنین نظرتونو بگین
❤️
⚡️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پایان دورانِ عذاب‌آور جزوه‌نویسی دستی!
✍️
یه متد خفن طراحی کردم که می‌تونه ساعت‌ها ویس و فایل صوتی رو به یه جزوه‌ی تمیز، مرتب و آماده‌ی خوندن (Study Note) تبدیل کنه.
✍️
فرض کن ۲۰ تا فایل صوتی داری (مثلاً ۱۲ ساعت ویسِ کلاس یا ویدیوی یوتیوب) که نه وقت می‌کنی همه‌شو گوش بدی، نه می‌تونی کلمه‌به‌کلمه بنویسی. با این روش،
بدون اینکه حتی یک نکته از قلم بیفته
، کل اون ۱۲ ساعت تبدیل میشه به یه جزوه‌ی شسته‌رفته!
🤩
فرقی نمی‌کنه دانشجو باشی و درگیر حجم سنگین درس‌های ارشد، یا دانش‌آموزی که وقت سرخاروندن نداره؛ این ترفند کلاً سیستم درس خوندنت رو عوض می‌کنه. کافیه صدای استاد رو سر کلاس ضبط کنی، بقیه‌ش با این متد!
🎙
دارم یکم دیگه روش کار می‌کنم که حسابی کامل بشه. اگه پایه‌اید و می‌خواید امشب تو کانال بذارمش، پست رو لایک کنید تا انرژی بگیرم.
☺️
✈️
ArchiveTell | S</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awddo2zsHMWhwt3AbdwnPwDLGKlf7Hc6K7FsenvXDKJ7z823kjYL4h_qk4Wh5hbiXKHDCHymNV0g4hVdn-6u_ZJYcWJZtPnNC_JFXsQvIM_I_8FIA4Ogq30Mh2sHW0XNyNr_4XvIwm9gUVpd35EJJhrxfa0_rZ6OrJPDdkCKNgpX0FwI0rYxjkedeVDu8l4W9CyJZZk8kUTK-EekNw9UcxlIpE3jG2O-B7DnSwcmG4XmOxShMXFMsToCphPnNK0Jlefpo9KodY5xHztoUS15bxHLGQXpmu1bQEKWTyVz52xuE7nN72NcKiYnHGkscMGB5vg5mNWpR0rrvFj-YiIE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://tabitoken.com/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
120 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Swqw4uXE6K6vxqgdmCMo0yokP3mIUYTiWSEt5w-LFF_qb3m-ByY1z5V-pnzFu7ZKdnwvyy-Q7Hhf9dtCIVAO6UYU1rle8j8tL0fRtefzlE_jSwR6rvUY1KeIjwNDG_N_oY9bXfI2kNLDSDzH0-P-6mxgNns9h6ZSBsAd9u1zaHPCH_KRODolnV7PYoLCY9D-QBXC5u0Nol-AWoU4lt1rodPp-980t4FxWpZn_vEGIcp-COFScnv5ft0gM9gy2oK9H3HOcS4JO7DprLKnLS4y90SAhvkUSoqZUvLMWmX2SXDlplCCeWQZ4HOw37NwFfEfiXGKVi8SyiUQ-PRTblyUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20
دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
GPT 5.6 sol | Mimo 2.5 pro | GLM 5.2 | Gemini 3.5 flash | Deepseek V4 Falsh | MiniMax M3
✅
برای فعال‌سازی فقط کافیه یک Gmail یا outlook داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://fapi.leileihog.top/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
20 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r92vzSchAC5o4ChWS561PEK81sAmycl_AvbZVir8xOlTi22UWdcD9caygtXZzgNFtvYwOl9BNxwD5ORXqELsL-l3pU8zzwKJ7Dua84X6mrksBkr88IutlsJI-H5sPdiR1DIa5gs886diBT44dn6tTSeJk2L5EohxPp-Kqy_-2Nnv6oS8Pn5wb4Nb8AWoEIt9J-jRGhGVWMM6_U_cjnBYVSNsRmvZPsbttFSAU8QEed9I1veNFuHu7xoYBgjgKdzE8UliGAnz4-9JfiogfJH_oFLRXX7M-ZE2LrYub5G-yc_9KQArB7bp65zi_vDT-BTalI2QSVgAgpoB5KDJaGORBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10 هزار کریدیت برای دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
GPT 5.6 sol | Opus 4.8 | Deepseek V4 Flash | Kimi k3 | GLM 5.2 | Sonnet 5 | Grok 4.3 | MiniMax M3 | Gpt image 2 | Seedance 2.0 fast
✅
قابل استفاده در
Vega Agent
✅
Base URL:
https://www.getunikey.ai/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BublbE3SCLzCY63nxe4c2mWThQ77xTfGw8sBScAOGVryy4zyczwmpaSbWHi2foZcyW5Nsm-_Qrb8hq4zOvyLw5FcjIkupgmN4pPSfde_IwcxCZcjCkGzJtb0X8vOZTy7sKGJXKYB4V-984fQ70u93ROimIS6bd7wmi-i-4JETlnEThefexGRhBXKVebAKdRWFq51HveYvXtlKgqV0IYEnGC9veTViZld1e9G1HbnSS3H6r7lYcxSeULeTRsklac8mxEBfABlFUVin17qF1toZG_wl4FK_9R24xCRQoKr7FC888r8rVpJwuit4tdljBkQmciEO2HmVZFP7_nkIcxDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان نامحدود به برترین مدل ها برای چت کردن
⚡️
🆓
با این سایت میتونید به 35 مدل هوش مصنوعی به صورت رایگان دسترسی پیدا کنید از جمله :
🚀
GPT 5.6 Terra pro | Grok 4.5 | Deepseek 4 pro | MiniMax M3 | Gemini 3.6
✅
🚨
توجه برخی مدل ها مانند GPT 5.6 از کریدیت شما کم میکنند ، این سایت هر ماه 3057 کریدیت به شما میدهد
💵
😎
🔗
لینک ثبت نام
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">💥
🍌
نانو بنانا پرو نابود شد!
کمپانی xAI مدل Imagine Image 2.0 را معرفی کرد که با قابلیت‌های خیره‌کننده، اینترنت را منفجر کرده است:
🚀
🎯
پیروی دقیق از پرامپت بدون افت کیفیت
✂️
ویرایش دقیق و حذف پس‌زمینه پیچیده با حفظ شفافیت
🔗
پشتیبانی از ۵ رفرنس به صورت همزمان
✍️
رندر بی‌نقص متن روی تصاویر
📈
آپدیت و اسکیل عالی تصاویر
این مدل قدرتمند هم‌اکنون در Grok در دسترس است!
🔥
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=LrSNC552nN21pF4_-X8Z5pQEweEFGfdt0RSYl_-lK0vkqP7ZTVb_0G20n2Zvrp0v8DDWrmHUcH2JmCemz0YPlgkn5EPo1w5FI5PozSayPj9l2WU8r56xhJgeO3UN1_jEFCkFiq5RklvqIH764e9njodgB0AZJ_mBof2q_t4JG29jdIxcZRuCqsveYu_Kbdy_FKRY26dneR1Yj2VD-ym7BDjB154svv19xId4eaC18265-aYhnRYgothxvIKmnEJHOkFah_FLNhqSSuUbf8qZtnpmEM-kTe_5I_zF0iO9J1E3pmNWdPjWwY9hm35qVmg6Kolj3oYxAKlVZu9EraOS6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=LrSNC552nN21pF4_-X8Z5pQEweEFGfdt0RSYl_-lK0vkqP7ZTVb_0G20n2Zvrp0v8DDWrmHUcH2JmCemz0YPlgkn5EPo1w5FI5PozSayPj9l2WU8r56xhJgeO3UN1_jEFCkFiq5RklvqIH764e9njodgB0AZJ_mBof2q_t4JG29jdIxcZRuCqsveYu_Kbdy_FKRY26dneR1Yj2VD-ym7BDjB154svv19xId4eaC18265-aYhnRYgothxvIKmnEJHOkFah_FLNhqSSuUbf8qZtnpmEM-kTe_5I_zF0iO9J1E3pmNWdPjWwY9hm35qVmg6Kolj3oYxAKlVZu9EraOS6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهندسی معکوس پروژه‌های گیت‌هاب با GitReverse
◀
☁️
بچه‌ها اگه یه پروژه خفن تو گیت‌هاب دیدید و خواستید دقیقاً همون رو با هوش مصنوعی (مثل Cursor یا Claude) از صفر کدنویسی کنید،
gitreverse
خوراکتونه!
🔺
چیکار می‌کنه؟
لینک پروژه رو بهش می‌دید، اونم کل فایل‌ها و ساختارش رو آنالیز می‌کنه و یه «پرامپت» جامع بهتون می‌ده. حالا کافیه این پرامپت رو به AI بدید تا کل پروژه رو براتون دوباره خلق کنه!
🔺
ویژگی‌ها:
پشتیبانی از مدل‌های مثل Grok-3، Gemini-2.5-Pro و GPT-5.4.
🐱
دانلود سورس‌کد از گیت‌هاب
🌐
سایت رسمی (نسخه آماده استفاده)
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فرار از زندان برای مدل های Sonnet 4.6 و Haiku 4.5
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEq7LN5VyD_KpcTkbCmuPmgRaQydJsbOkJvR45f4ke3INHcEcE6LgBTC6HjH1eSRAQXT8lqSb9wBX8Itj0cEgzUjsCbvtJ1iOkrfuvGwBbmgXLo0jEcvyn5I5zzdDdcLWDfcQdWAtn2hnvAr1gQuJZbuOC8FO9T0aJNta09URuQLkqRcoXixSHuRob9u8uIOzoaIWmQHmveJF_Y2UdI296C-Y30tPLO00KrydSyOaFAMtrKyhuHsFQ0G1hZo2RnXKoNQ6lk8GeIBOr1obqHC--mM9s7S2DpZZh4ZAQIjum60gatog7jYv0MGS4St0jSRLDDB9p5qS-s6uH-UzxVHrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
Base URL:
https://tokenharbor.ai/v1
قابل استفاده در
Vega Agent
✅
با جیمیل وارد شید سپس لینک ارسال شده به جیمیل رو باز کنید و 5 دلار رو دریافت کنید همچنین تیک Free models enabled رو بزنید
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فرار از زندان برای مدل های Gemini 3.5 و GLM 5.2
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=ATKHY_UsBG9yBVhSfcJHE6zjQkLCOk7xGy7KZekrtVHzJRwbKSGxwLaUZcYN4To-wjrEEnJPYFjN4zmApF6JcnlVCeMumTHmI3vrmx1gzzSdJ3E4LabwLijxnJm853_9_W6chNlrldgnJd-TE19ENanVx0tQJORCmk3JBGwOJ7_pSSsnl5dfJ7MCFxoBl8mZUOhzDeGjmSB-i-WZkeQN_3LRrBV-42s_3aHbVxYN5xSyg1kwVSn-vHkoD6GZ75e9tHdWW_ezDQ1gYkCCIkfzqJ1cqYEdLXoz4z_Cz8KsqfTb330Mq78sJaEcJUWVjSF2B2X5mIR7zc1V2GYS7yVIuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=ATKHY_UsBG9yBVhSfcJHE6zjQkLCOk7xGy7KZekrtVHzJRwbKSGxwLaUZcYN4To-wjrEEnJPYFjN4zmApF6JcnlVCeMumTHmI3vrmx1gzzSdJ3E4LabwLijxnJm853_9_W6chNlrldgnJd-TE19ENanVx0tQJORCmk3JBGwOJ7_pSSsnl5dfJ7MCFxoBl8mZUOhzDeGjmSB-i-WZkeQN_3LRrBV-42s_3aHbVxYN5xSyg1kwVSn-vHkoD6GZ75e9tHdWW_ezDQ1gYkCCIkfzqJ1cqYEdLXoz4z_Cz8KsqfTb330Mq78sJaEcJUWVjSF2B2X5mIR7zc1V2GYS7yVIuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمدید فرصت ساخت ویدیوی رایگان با Gemini
♊️
🆓
بچه‌ها گوگل مهلت استفاده از ابزار خفن ویدیوساز Gemini Omni رو تمدید کرد!
جزئیات:
حالا تا
۱۱ آگوست ۲۰۲۶
فرصت دارید که
۱۰ تا ویدیو
رو کاملاً رایگان بسازید (قبلاً تا ۴ آگوست بود).
❓
چطوری؟
تو اپلیکیشن یا نسخه وب جمینای، برید تو منوی ابزارها (Tools) و گزینه «Create video» رو انتخاب کنید.
جا نمونید، برید تستش کنید ببینید چطوره!
😳
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGOqs4R7A7u_UXV55ye6souDiVee1HtCeGLKdmNCj2imqQ6QhdzsnpzKG36TFqnUtgif-NC-y9JEOyOdk25CbVrwBmntXfLKdsRvDIMzIDvrd5L1_k-sih3m_O5yh4u_JYQECPE6TZiqM-w7CxcaNM7MGTuq_Vp2ybKDlXoZpu6pYAqMKww6p-7lwrG4F1V7Qly_tC7M2Qt4RNVmgP9o6V1zNzVGiSa7dWZx-ri7kyD7JLHH4Uk10W5wdE4b-B8njcg19VN6LVIcwAO5v7FWWw_Mk3RgfmxJB_Vsw0zFOlA5i5Vzc9tCHc1nf2Sa2LQgb7aanR1rdCP6jfDcMtiwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن خفن و متن‌باز بدنسازی با openGym
💪
💪
اگه از اشتراک‌های پولی و تبلیغات اپ‌های ورزشی خسته شدید،
openGym
یه جایگزین رایگان و کاملاً شخصیه که دیتای شما رو تو سرورهای غریبه ذخیره نمی‌کنه!
📌
چرا باید نصبش کنید؟
💠
دیتابیس کامل:
بیش از ۱۳۰۰ حرکت ورزشی با انیمیشن آموزشی.
🗺️
نقشه عضلانی:
روی تصویر بدن نشون می‌ده این هفته کدوم عضلات رو بیشتر درگیر کردید.
✴️
پیشرفت هوشمند:
خودش حساب می‌کنه جلسه بعد باید چه وزنه‌ای بزنید.
👾
بدون نیاز به پسورد:
ورود امن با اثر انگشت یا چهره (Passkey).
📜
انتقال دیتا:
می‌تونید تاریخچه تمریناتتون رو از برنامه‌های Strong ،Hevy یا FitNotes بیارید اینجا.
✅
صفحه همیشه روشن:
موقع تمرین صفحه گوشی خاموش نمی‌شه تا راحت رکوردها رو ثبت کنید.
💡
نصب:
می‌تونید فایل APK رو دانلود و کاملاً
آفلاین
روی اندروید نصب کنید، یا با Docker روی سرور خودتون بالا بیارید تا بین همه دستگاه‌هاتون سینک بشه.
☁️
دانلود APK و آموزش نصب از گیت‌هاب
🌐
نسخه دموی آنلاین (برای تست محیط برنامه)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF2wo4AfFadRWhbkTflwAUgVW9D39gfWgbwsegqaAPzkmxc_l4OKwjdCRWGWEmEPQ_WwKGcHexWzTgYBnyuvugNOIwTvCqyLCod8sFHTlRU6E8NIX_CekZCefj73NPTjgyZbuwHBW3FveaZmuQeTZzJQywT_bFxKuxClog0zFLbSWvuy-HrJE4kUAAfi2XgC3p5Fam9Ef9gEfSqwzDd0gMAscCGNgEK7lrQT8C43MCh7rnzy3XOIkIdeXQK-T1C9JAk4mlaPVlkUbCk-TiwbPasRTqGCsGWJ10Z6qOhMNTnN26skf4hbm_JYvwcJCaelAtPOLGbpLwRrCwytvRliXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0JxMG2AKidGmyjydXlT-l5SqOSIJ_mo0qfwK4u6ZpsMD5fsBY7LpS9792LW3_uyOJ_D08n_lLuyM0SZb2ZlRTJtDs4uBZlRoRXqHpJF596s2cO3NgkgI0brsJKcOa1AbPykMyAHsEPiISQscj_Jdntu7XulcmIYOhwIwu7jBz2CEb9bwS_K805j2uR20Eg14IZSVoTEtozbAevPw9WwiHqEh5TTJhPQRa75pqq3Y3CxQ9_laa6LYqImiQTHVLNLjI7nc4LcAf-0Wiz3SStrk35I-Dc7H82RDsIRXCvedRqyBZm8ANwcM4o1CJX-of9kspZveiTA9FHHLtDPowTkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🆓
دسترسی رایگان 14 روزه به GPT 5.6 sol و Claude Sonnet 5
​سایت و ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده که به ۱۶ مدل برتر هوش مصنوعی مخصوص کدنویسی دسترسی دارین.
💵
😎
​
📌
مراحل دریافت:
1️⃣
وارد این
سایت
بشید و پلن پرو رو پیدا کنید و تیک Free trial رو بزنید
2️⃣
استارت رو بزنید و با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
3️⃣
از داشبورد برنامه Zed رو دانلود کنید ( برای اندروید در دسترس نیست ) و تمام!
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=kK8ADdfcXo-AHX6E64CrtaE3DFkm_aSd8KwQqsmwgioBKUc2zLZelTilqjbAheZlmj1VtDpG7tAo8ZGpn8ZxiHYPgsRFsCU-vRXkYuLpAi5qsSMFLRHAN0TSMWKORjTU9-4b0JN46OiZMwjL6AOH720rQ8iLWfxhG0eU7YCNtmNV7pq3v3nv5xN5efCWz8xMGA1HqcIlenjaR8rpAER_Aw_fZQ-TyS7LZBpqvEG1pZa9CZjnV6UtCS4H_4bw155FOEnM5JcnUlcHerIvVD9t0Rw_zRZoq1Z5Up2RpEV0khhI2en5ghgfvngAdjQG1WEMp8usL9uHOaUE3gyT_-VnuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=kK8ADdfcXo-AHX6E64CrtaE3DFkm_aSd8KwQqsmwgioBKUc2zLZelTilqjbAheZlmj1VtDpG7tAo8ZGpn8ZxiHYPgsRFsCU-vRXkYuLpAi5qsSMFLRHAN0TSMWKORjTU9-4b0JN46OiZMwjL6AOH720rQ8iLWfxhG0eU7YCNtmNV7pq3v3nv5xN5efCWz8xMGA1HqcIlenjaR8rpAER_Aw_fZQ-TyS7LZBpqvEG1pZa9CZjnV6UtCS4H_4bw155FOEnM5JcnUlcHerIvVD9t0Rw_zRZoq1Z5Up2RpEV0khhI2en5ghgfvngAdjQG1WEMp8usL9uHOaUE3gyT_-VnuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چت‌جی‌پی‌تی رسماً تبدیل به فتوشاپ شد!
🖌️
⚡
ادوبی یه پلاگین جدید منتشر کرده که ۷۵ تا از ابزارهای حرفه‌ای خودش مثل Photoshop، Premiere، Lightroom، Illustrator، Acrobat و InDesign رو مستقیم میاره داخل ChatGPT.
😺
🔥
کافیه توی تنظیمات چت‌جی‌پی‌تی پلاگین Adobe رو فعال کنید و با نوشتن Adobe@ توی چت، از تمام این ابزارها استفاده کنید.
✅
این قابلیت از امروز برای تمام کاربران در سراسر جهان فعال شده!
🌐
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK2HQiEjyLfaMeX6HTvRlRVkBM0S0QMgGfEjKBCkbXNmsX0BAc1gVqDFMZRuL1iQSk8_pxFrgGnWBE9vBALWksvJ-4Cic1VTG4hCz6qIPDjshvN0e_py61NsPV-azUE31_ghFqaI87-UtOQQu30SlOoOXe-DxMkKByswVOX9cY7nhLprddtg4Lxg2FiYSFr_Mdw8aRoKEUde_POmoUHvnaSHKL9YWtLesSWWAY7GL2Ivohx1oZ2dX4w7ETj6H7rZLhl1mckgHV3UfrN_m6Yldje3FK09rjt5HerRHe8gho2m523kOMxP_G8j5SNIK4FnKSt7xNKb396OAitmgnACcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک ساز خفن گوگل
🆓
🎵
🩵
با این سایت میتونین با یه پرامپت موزیک و موزیک ویدئو های خفن بسازین و منتشر کنین.
با لینک زیر ثبت نام کنید و ۵۰۰ کردیت رایگان دریافت کنین:
🔗
FlowMusic
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHMSZZpunZtg_8VwaSpKU9OCm5dBk3USnuoJKVvS-BRvYJaE-pEk0T8_3f9rTw9Ro3cnlYTLIUOVDxSHUO_2YKM4aL_TzSdG3Xcz4drPI-Pdh83NR3w6yXZKwukvAzoHKRSkJYHYecePn0GWTFJdFpzdYXR-oFiolKe7UEaNRGERf0S44iLHbDHO0P49A1GwB6negjeJIt_8TYco95Q4yVEyss_63KTqNNgEC2qYfDBzPos3gd8fzUeydow0SR0p0BQhj6Be2jHFq4PKEDRgVPJ3c527tVDkKkwjCuv8AOPLaiRElUlYXo7SGNhKVepZGmbskNgUXRCLhAMw1gGp9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1500 کریدیت برای دسترسی رایگان به برترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.5 | Sonnet 5 | Gemini 3.5 | Haiku 4.5 | Gemini 3.1 flash lite | Nano banana pro | Nano banana 2 | Nano banana 2 lite | Gemini Omni flash
✅
1500 کریدیت برابر با 15 دلار برای 7 روز
💵
🗓
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPqyXnpyMZcGT-yxieROITyM1_Q45C_n4-Rf1xfEsbtzOnelNeEfiEtHuqk-7nJWpDhQXvZ340zez94YE4iGO2WQrAk5EODGMSNey2-18KWWMSBkWPc83m0PUm53d6uqVuMIFwXZ0vqKrXz3QPXpDD-xq2TDlhMsqoRYRQmla9YAC0aeqYME4p1-abke5e6I9nOwp5UrHkXevfiC1wHTK16_QETzZ8WB7QFTeeMs9jjjy81T3j0p6gyhd2Bon79C2iU2GYW8k-UiHHbRKmUBvFAzYjdE7CGh18dr-mJ764W8ZsO0g82Y564DzLrGD004uPtGXgnrfxQnmJwq1FmhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به Kimi K3 و Qwen 3.8 Max
❤️‍🔥
🆓
بدون نیاز به کارت اعتباری کافیه وارد
app.clusy.io
بشید، با ایمیل ثبت‌نام کنید و توی پروژه جدید مدل مورد نظرتون رو انتخاب و استفاده کنید.
😎
⭕️
فقط ۲ روز از این فرصت باقی مونده! به دلیل ترافیک بالا ممکن هست سرعت سایت کمی کند باشه
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUB99Yu5Xnw-batMEG0-gFPn4-nIlhSlCf7zMvtkJ10dEyru4pm8Lhbz2suhmvONT9y3A_LY6tZXDWkPdUOvYqZBE9TEqCKf8quWH6zY_K-z8eXjtg23lHUu8jybbJwLYxF9IjdIfk1fQ6xkxBhyrpkHogjWwpLclG2ANbhIyE3CmyQkwGomoewA82_JG3J1CgJz9wE29qajBiD-T4kuBq4oITrBA2NMMCI-PBaL4eiJ-Qvlfskri62fwKTpL1SQ-YQ_WgMjCEJ4iZKZK8USied2oqNMrgQJ53Ni3m2s-mrutfRuel-5Ff-gcLM-TBnWx3G0NfHp4aDe7sYLs1mLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان:
امروز از ساعت 12:30 تا 20:30 به وقت ایران
⭕️
🛠️
مراحل راه‌اندازی سریع:
1️⃣
وارد
سایت
شده و با اکانت Google ورود کنید.
2️⃣
به بخش Account رفته و اکانت خودتون رو از طریق تلگرام فعال (Verify) کنید.
3️⃣
به بخش API Keys برید، یک کلید جدید بسازید و اون رو کپی کنید.
4️⃣
برنامه OpenCode (یا محیط دلخواهتون) رو باز کرده و اطلاعات زیر رو تنظیم کنید:
🔺
Base URL:
https://api.aigate.shop/v1
🔺
Model:
muse-spark-1.2
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4pd2Mbh-XHUWkgDUH0Os7sp5R6C2t4skGtLmN2KUHxEQQArPRyGhmwIMEs3CQOS5vEk6dSkyFFIJZpIImKY9DGNURf66UBwHBDPV3sayMwdYWjCJSHPczlkiZ8w1wXWQMIPnrq4JL2-gKsOVTHDLiAUEaexTPidPbs4s3tUnRkNKz7UXozIBYH0l2rWqUA4pvzOGZ3wTYFWnIQVaQUS9yn25F4AfrPh2Un-j2-GxyA_ACuXAdwEm5fVQxE6y9WJLgeGDrEaozhafrLgXK15zcNLEihEbEpP92GTzIzpZrnnFcdsIXfTWz6XwIyd9qSQ6lmgum219xL1wrA0BiZd3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ‌سیک V4 Flash
به‌صورت
نامحدود
و
رایگان
تا
پایان
سال
6️⃣
2️⃣
0️⃣
2️⃣
به آدرس
cnb.cool
مراجعه کنید
➡️
هر
ریپازیتوری
که خواستین را باز کنید
➡️
عبارت
@codebuddy
را تایپ کنید
➡️
حالت
Work for me
را فعال کنید
➡️
تسک
مورد نظر را وارد کرده و اجرا کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0ZBX1_wmla9nFJDLPek5hpoQp9r3Fkt58sWXJN1r00njV-xHGeAYFgNyZjXw--1CuVXD936qeiLixX6kEcagArse4oVNfP9X2OcG9NS-UUWnXB7om3xXgOWvxay33N9-SRpFTJiGazC-tX2Q7V-Ne-dTCoMbtmdDBVjU4BWufdj9_Bp5snnY3QxIDjShjThJtDh5Q43JgbO4kpB9ZrsxHL0nFh0tfoHYulagC0VprLG6Gjl2w5cIs-1_vA6cZEAqhvh3jGUGqGHTY8d7YpyuYk71yaDweotSyAIDUt_cRJN91YaF0772UQC2lYKEbCenFtSllcUwAJO9UnG2IXsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کامنت یه کاربر زیر پست تلگرام در ایکس:
من آدرس مخفیگاه پاول دروف رو می‌خوام
😕
💯
اکانت رسمی تلگرام:
مخفیگاه رو که نمی‌دونم ولی من رو می‌تونی تو خونه پیش مامانت پیدا کنی!
🙈
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwKFKv20TVTqa5AiXQRHS21jl6sSXZrLQeAvo1Py47QIDUP3GeAAy1KE4AT7t82ovyP1IiLlFcV3RP9QY5QLZq3HPwsnsd-N4EjYoWtpCr8Wl6KQp0zZqzyzV-auFc1IrmYpWtMcRaRYx4Ky8j9Rje5C_28qX6pgvgPBtF939Q5hXsrF4eR7m0ljwlfik_E62eyAbrReT73w3mtokEazcFb1JlitxhZrg02fULzdO_UfL8Q1ijGaBTnc5b0EopVoT7Qj0MAAVN0CuBBm1V-AyqsLF03h5mzdIaDdaduy7VyOj1JQQ9j8wmnuplj7jRJad9zouE9IufrUUb93gsRPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف فوری واترمارک تصاویر و ویدیوهای Gemini
🚀
🔥
دیگه نگران علامت روی عکس و ویدیوهای جمینای نباش؛ با این ابزار رایگان خیلی راحت حذفش کن
❌
😎
✨
ویژگی‌های کلیدی :
1️⃣
100% لوکال و حفظ کامل حریم خصوصی (بدون ارسال به سرور)
📶
💯
2️⃣
پشتیبانی از عکس و ویدیو با کیفیت های 720p و 1080p
🎞
3️⃣
کاملاً رایگان، سریع و بدون نیاز به نصب
🆓
⛓
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAj3by7l07YSl2qNG51cA6j4sHhPQcOAux0oFHn8FWXya07zhJbmYXYLJa8MOm8N3s8mfKlpV0t0ltx3yX304UtOVOc9gr41F7LMWqnEzAmV4Th4zbkV9qtego5ZLkBNj4J2kvX_i1a0TS1sgDUr_KM8VA_ruIcSVTx_i-Fqfce_lwT9vcA9sNSdAgyvYX-wFJPUJhZIczRwvd0GIJdhJzj1jL8NjzH-BwQAh7NYmtFj-BAtE0g1ybF0_kuFTgXqqEhIe7XamMkhp7e7f8KT4_iatfrPEWMdbk1s87GsxdpiLUcUM9sq8wjKpFSnLN-1TLw-EiKKlm8h08wfJAEBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت
Dola
مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت روزانه و رایگان
🔺
کیفیت و قدرت بالا در خلق ویدیو
🔺
استفاده آسان و آنلاین
🔗
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgOY0ErkJa7iOjbOCp5pTt9AI-EK9nyhXcpsQSoHfkwvpcTJ3gDeuq5p8UOo5QxCnTA3uBUFKx5ThBoVjZwRXHT2jJj4y_YU4T39pVK6UJXb1tej45A48ZXsLYwliSK0rxi2HEp06X5emQXh51-jmN3m93iWsnvKiBgyXWpuHcuQZNPccrHbY6SGw0vyOicPh7yRqVJUoqOVuIa2saPLh0RMnVNLCVOa1RlKZm0GNdjlgCA20w3Nd1qy9y0tfAn6aui0XefYZwqs-NeYcJfedm8zS_qFeAangf-twuUz_iJR-blK6_4-hf4Dsuda-emMol1qZlnV5PVrA5Cx6WPl2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
گنجینه API‌ های رایگان هوش مصنوعی
🆓
یک مرجع کامل برای پیدا کردن API‌ های رایگان مدل‌های زبانی (LLM) بدون جستجوی طولانی
🔍
✨
🗂️
1️⃣
freellm.net
بیش از 424 مدل رایگان از +30 ارائه‌دهنده با اطلاعات کامل شامل محدودیت‌ها
📉
📊
2️⃣
freellm.sh
لیستی ساده و سریع از سرویس‌های رایگان با نمایش وضعیت و محدودیت هر API
⚡️
🚀
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra_3O5PedJ-ul98sZdYWxo2lbYv83g8XHZGXPS-A9owQktPVX_1cSsoI5D2lSYmAR9NwG1LM0rBpbHujgi1x_XInoXpL9nuulacOl4w4xy_JeVukmSyyYc8oR1i4KJSdplQgLSaP61H-h9eqJp7rVFRULtNCupkWJ9HSgZNu2SRjnahWCtN-1bPMhLVRNDrPtId6BZ8UpFwbPuhZ4InfpNAITN-m7QwOaumsY4iM6Jpl8-OwJ7Fbx7StG1s5D7QiiWrfLpcr2UcfJPo0GINkafISfZo1eq5d7p4fOGNehSuP7TAep8YyEdm1f84EG1DuXFvdD3SVvpSuIXIgYHaTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای اسپارک (Gemini Spark)؛ دستیار هوشمند و همیشه‌فعال گوگل
♊️
🔍
بچه‌ها گوگل با «جمینای اسپارک» رسماً داره هوش مصنوعی رو از یه چت‌بات ساده به یه «ایجنت عمل‌گرا» تبدیل می‌کنه! این دستیار کارهای روزمره و گردش‌های کاری شما رو به صورت خودکار پیش می‌بره.
✨
قابلیت‌های خفن اسپارک:
📄
اجرای ساختاریافته:
اهداف شما رو در قالب وظیفه (Task)، زمان‌بندی (Schedule) و مهارت (Skill) دسته‌بندی و اجرا می‌کنه (پشتیبانی از اجرای همزمان ۱۵ وظیفه).
🌐
وب‌گردی خودکار:
می‌تونه کنترل کروم رو به دست بگیره و پروسه‌هایی مثل جستجو تو سایت‌ها یا رزرو رو کاملاً خودش انجام بده!
😨
مدیریت ورک‌اسپیس:
خوندن و ویرایش فایل‌های Docs و Sheets، زمان‌بندی تقویم و مدیریت کامل ایمیل‌ها.
💻
کنترل مک از گوشی:
اگه اپلیکیشن جمینای روی مک نصب باشه، می‌تونید از راه دور (با گوشی) فایل‌های سیستمتون رو بررسی کنید.
🤒
شرایط و محدودیت‌های نسخه بتا:
❤️
فقط برای مشترکین پولی (Google AI Pro و Ultra) با اکانت شخصی (بالای ۱۸ سال) فعاله.
🔛
ویژگی Keep Activity اکانت باید روشن باشه.
❗️
فعلاً از زبان فارسی پشتیبانی نمی‌کنه و تو بعضی مناطق (مثل اروپا و بریتانیا) در دسترس نیست.
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iv16d4PYvQp9vD51LkDRNaiOjl07jJ1mEm-PgtR_RmiHdjdKrjp03TTOdCOzHnBAyyJ2BWEwXvwMhYJDXaSy4LOLeDY8qKbvPrT5QtE4IeH1hBwTuQ9f3RUjvm4S9ST8azg_GN-gFXMCjnklog5k44v0_2If5V5tmCnffbVEAQagTdgxM9k-EtiXuJTc20k1ZLJXqaKNG0XcK-nEMQD_Yj8c6H8BrlC9bAI3o0Tp3Lk7fe4AUMRGDs8anSagiai9tkpM8Pf3z7x-YPrqsyzoRmrc2dqBUsf-cFPOienNQ46OnQZYsor4r-fF5giNqNwZiJ5ol90FZ9yR_3WA8N2Ayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی سرور اسپیدتست شخصی با OpenSpeedTest
🚀
🌐
〰️
بچه‌ها اگه سرور/VPS دارید، ادمین شبکه هستید، یا کلاً می‌خواد سرعت واقعی کانفیگ‌ها و سرورهای خودتون رو بدون وابستگی به سایت‌های عمومی تست کنید، ابزار
OpenSpeedTest
دقیقاً همون چیزیه که دنبالشید!
🚀
این پروژه یه ابزار متن‌باز و بی‌نهایت سبکه (حجم اسکریپتش کمتر از ۸ کیلوبایته!) که با جاوا اسکریپت خالص و HTML5 نوشته شده و بدون نیاز به هیچ دیتابیس یا فریم‌ورک سنگینی، سرعت آپلود، دانلود و پینگ رو اندازه می‌گیره.
📶
👩‍💻
👩‍💻
✨
چرا این ابزار خیلی خفنه؟
🔺
اجرا روی همه دستگاه‌ها
✅
🔺
نصب بی‌دردسر
✅
🔺
تست فشار (Stress Test)
🔤
🔺
بدون ردگیری
🔞
💡
کاربردش کجاست؟
برای تست سرعت واقعی ارتباط بین دو تا سرور، عیب‌یابی کندی شبکه وای‌فای خونه (LAN)، یا تست کردن افت سرعت موقع استفاده از تانل‌ها و پروکسی‌ها.
📌
👩‍💻
لینک مخزن گیت‌هاب و آموزش نصب
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔥
یه
پلاگین
به اسم
oh-my-hermes
برای
Hermes Agent
معرفی شده
🏥
این
پلاگین
سعی کرده چند
قابلیت
مختلف رو توی یک جا جمع کنه تا نیاز به نصب چندین
پلاگین
جداگانه
کمتر
بشه
✅
😍
از جمله امکاناتش می‌شه به اینا اشاره کرد:
✔️
هماهنگی کدنویسی و مهارت‌های codemode
✔️
سیستم مصاحبه هدف و پرامپتینگ برای برنامه‌ریزی و مهندسی حلقه (ulw-plan، ulw-goal و Loop Engineering)
✔️
معماری حافظه پیشرفته (شامل Dreaming، Pruning و مدیریت کانتکست)
✔️
سیستم حافظه لایه‌ای (بلندمدت و لایه‌های L0 تا L3)
✔️
متخصص‌های دامنه‌ای و قابلیت‌های تحقیقاتی
⚡️
تنظیمات آماده‌ای هم برای استفاده
سبک و سنگین
داره که می‌شه فیچرها رو
روشن
و
خاموش
کرد
GitHub
🐙
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPJ51AWOC9pn4CxhnkWcLghEVsaD9cYuVvcLw3z0IRB9h8oZxkN2MUCgW9Sdxb-iW2YQ2kiSUVXu37hxW-0scX34HtxsKP1V5jGkxspJ-JK96R2fDeNRBWI0Kp9gWhRJ96rFk4ZOgbNVBaQgfsoud0G60tsJz8GntB_F1HSRwio6ZMJZxQ0sSW6ImSTRBYBHQuhtJu0sDGtbtnrAl7QmaCa_jdHYaL5WchRF_5MzAo6H97KZWNvgX9aAiDtnm2k6zmuamRX0RruuzpjesI382WfQzxJaH2VWmIQLBtfpVkMQKZY99Bdx-qAQqi6u9CjaDnKdlYIOMWudDsFo78xx2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱ میلیارد توکن رایگان  تا ۱۲ آگوست
🚀
🆓
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1t2-_XY3TISisnbfSHwJS0aFU7Re3ygmXDjgYiYutiyYnTxOGWnmG41YM5lV5NQnH3kWApF9MPR_cTJWnXQJWsOaSfLA22B2xGRd2QDQ1A6ANgRAhD4zC0VkLJ80xG_M7x_515YYXJvILY2UMBgcaqAZjLHJE5xts73LZl94M5bHRbZMcmA7r99QELIgqnQziCUkHVz9FyvDc9AmSIR1pF0aOkw3fiuWqjOreTu7FZ9t_qWSAUCCGdSGFl5npThBOM58_tVdQeBt5YUiSCWfEyiir2Nfd-3qlAfKkCTyOamRDGPLiBg8Lijf19jvNWd3a5mMaFP3XM4Rq3AUFYgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaI6NX04VazwKPU0_RFqeixoLLUMsAgXOuTmArkze8y8gyf2PS4SO0Dq1MWPVPqnFhiOYoS02-4LEOGD4FVDb3E2SCvzKtldAPADuYYGvbT4OZHsLgUHE8aFNJzHytOWGscwcnoqKh2dUJ806DZ_Xw6t66I2yChGNpk0zbavJqHL4Bg8YSERb2lanxaAdKO3gutOVVjgwQAtvFG1MbAL0u6UFUNczxhO9frGvfczZpEUZ2jLl7UmvCvrpOWca8uEX-4kZj4r22XyNuxka_W_WKU8wWHQtETG_btjT4acGKlLHsJfxLHjtyV0dwiLwBmJZYNK3_G-sWoQIbx2V7LldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=O-gkhkkglfwagdL54Z_6A8ktiqmcP_dh6LERHl37dQZo6iLIzOP7z8qTKx7o6G06gsrRcLb2isVnzK6ya4U7CZEJPvtz-oSyHsyVOJHFA2Aqn-FURW6H6N088fJ1HpPF8Jmw2Qt8vl7qIyazaCnq5kzP9UuO0vzXznoLb2ERUmleIeF2TaO21HeulB530HqPYwu8rFsyIg_z63hCcg-YVy66A0jtoZGs-1UfKj74fGKfveKTq6aNG175pBZn5ahN0NfxKQVHXw349-ybIZNJ84ujQpVJBfYKmKPzLMZHmXhVEnyJkfVPZWvBPy66qgQ-RV8JEvmlVCVFSyk9S4CIRo8kEI02t8_9OgorL-jHBaPPYt-aJ-cKEO9jZktsoGn3YxHQKIkjk1uNORnh7KcPBF1oozh8moK6aUicSL4VawpbHJV6rejZ4aJb41fdrj6QfwA3EHmt8txuV3H2C_mG55nXfvYcR6mC0I72eiCkSR9hselSAAby7xDU0A1vop6CqS1DrRABNCN-7Ane-VFd8CZLfkOqPJdxhR5RR28M_9Ga6WBmX8Y8LBSh4MV8qrhIohw5c3TrP5NSNVAbEUIPXhBtQYDtVLXpN61zZ611cwIVhCF9svgWGn28q3IfKJGTk70udK8VP3UTY8Yqo6_ng6ahr0AKB-IdURC6ucoOjt4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=O-gkhkkglfwagdL54Z_6A8ktiqmcP_dh6LERHl37dQZo6iLIzOP7z8qTKx7o6G06gsrRcLb2isVnzK6ya4U7CZEJPvtz-oSyHsyVOJHFA2Aqn-FURW6H6N088fJ1HpPF8Jmw2Qt8vl7qIyazaCnq5kzP9UuO0vzXznoLb2ERUmleIeF2TaO21HeulB530HqPYwu8rFsyIg_z63hCcg-YVy66A0jtoZGs-1UfKj74fGKfveKTq6aNG175pBZn5ahN0NfxKQVHXw349-ybIZNJ84ujQpVJBfYKmKPzLMZHmXhVEnyJkfVPZWvBPy66qgQ-RV8JEvmlVCVFSyk9S4CIRo8kEI02t8_9OgorL-jHBaPPYt-aJ-cKEO9jZktsoGn3YxHQKIkjk1uNORnh7KcPBF1oozh8moK6aUicSL4VawpbHJV6rejZ4aJb41fdrj6QfwA3EHmt8txuV3H2C_mG55nXfvYcR6mC0I72eiCkSR9hselSAAby7xDU0A1vop6CqS1DrRABNCN-7Ane-VFd8CZLfkOqPJdxhR5RR28M_9Ga6WBmX8Y8LBSh4MV8qrhIohw5c3TrP5NSNVAbEUIPXhBtQYDtVLXpN61zZ611cwIVhCF9svgWGn28q3IfKJGTk70udK8VP3UTY8Yqo6_ng6ahr0AKB-IdURC6ucoOjt4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jR8P51vpgk-aEh9q79pGJTDCyshfh40ZKZnJsqPgcCwCoIPOdws444poo1mSEAIeCKtYSOW5aSDCl_sg07X7fNXRsX4c_TOBkCdjxCTgNDaNTMu0g1TrHQ4Xv11af_tzS-PAIu2isBKhNryNHtYNfFq9UYNksOTvcPi0qA41bpQytbqqK1w0NViHTU6Vqoe2AraABxjRXGIx-2UNACznOFKBYUYneVxOX0yoGKhtyHEhfs7YQs0-U5LmVsTTDNqkDBOOtjLWG_Y8Ka9EfB8h5j7cQbz5V6ezEICr0VK836apX_c6cNa8ZLcAacxszTjHRGjxcyZddYL3R96ZWgCznw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
500 دلار اعتبار رایگان API برای شما!
‏همین حالا کلید اختصاصی را دریافت کنید و از مدل‌های Opus 5 و Opus 4.8 لذت ببرید:
🚀
Api keys:
sk-2UddB27hnFA1z2LKWKnq6BQaffBLe86FU0htxAHm0Q9n5vjW
Base url:
https://agentrouter.org
Model:
claude-opus-5
|
claude-opus-4-8
✨
کلاینت های مجاز :
🔺
‌Claude Code⁩ | ‌VS Code⁩ | ‌OpenCode⁩ | ‌Hermes⁩ Agent | Qwen Code | Kilo Code | Cline | Roo Code | Open Claw
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxnjEVSvNqbs43MUhIkIY0yreD3EF_vnpzvmROFVRAUMF8nazxRIPJw5Y8UKMQ8RwE-NuB_LHFHNmgN24OO3aUt-qqrEzaMD_QNjYs8XRGX2dhZ9eeCnbKPyLE10Zfe9CgpzaUVbHxSSloPXv9GW4odvpfk-0TJNO6Vl3XY2zc0An1KBURP-Tnqd-5Jhiqtj1PrqUtbMynMRnohr6L66hbSR39jaWjRtswe7xK-Xj-JbvF11hQuDW_QMjilA35fBSBaBy-1rcZErRz98G389U2tIdsabT6-6gz2_qeoug8ZmraeMvxneyj1J4fqNMcNN61DCefnXIzUYdbcWyY6kXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آموزش تبدیل کردن صفحه چت سایت Qwen به API
🚀
اگر در موبایل هستید از
Kiwi Browser
استفاده کنید
‼️
✨
آموزش اجرا :
وارد سایت
chat.qwen.ai
بشید و یک حساب بسازید
در سیستم کلید F12 رو بزنید تا Developer mode واستون باز بشه
در اندروید از سه نقطه بالا سمت راست از منو گزینه Developer tools رو بزنید
وارد تب Application بشید و گزینه Local Storage رو پیدا کنید حالا کنار این گزینه یه مثلث هست بزنید روش و سایت qwen رو انتخاب کنید
یک جدول باز میشه و آخراش یه متغیر هست به نام Token اون فیلد روبروش کپی کنید یا توی کنسول این دستور رو بزنید خودکار کپی میشه
copy(localStorage.getItem('token'))
اینی که کپی کردید در اصل api keys هست ، ممکنه بعد چند روز منقضی بشه و دوباره باید بگیرید ، تمام حالا میتونید توی هر جایی که دوست دارید استفاده کنید
Base url:
https://qwen.aikit.club/v1
Model
:
qwen3.8-max
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_ssCBfna2rl6hCXZyoqm6cLPVIBn_WAkFtbDbW_OyryiO4_Nm_tTdToYcvJLvi6LUJckgH8yA7B8yH2S79vecOI5HoAcUAATQU42S8IRzdD_CiGSwKOOIufV9aP5YGT29I3YcOx2Zmz6DicngQUkarhgHbtf_e8Yjdtv_iwaMk04gbc1ydPx_sp22lI9hqGH4IiAY__dubsHGzpndpfX4pm9NX5ZuXPcvqoV5dmJcPgEuoXU69oOd_Iz5u9s4vK0omp5PdJadxanjGMP1Nho5u9fV32aizX7KEjhR0eFeh5m7OlI5haSGqQLr6k1sn3aF2glkz6Nu_hBJluLLP-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩
‏وارد سایت ‌
Cline⁩
بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند
این سایت
‏حالا توی ترمینال، ‌Cline CLI⁩ رو نصب کنید:
‌npm i -g cline⁩
‏با دستور ‌
cline⁩
اجرا و لاگین کنید و لذت ببرید!
💻
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url:
https://www.fastaitoken.com/v1
Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471
Model: claude-opus-5
Model: claude-fable-5
دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro
همچنین دارای چند مدل رایگان
:
GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3
به
این سایت
برید یک حساب بسازید و با تلگرام وریفای کنید و لذت ببرید
✨
قابل استفاده در
Vega Agent
✅
📍
Base url:
https://anymodel.org/v1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLDv9CYs4EQMTUhn5aATns9CAoW9LmJgNZ3BoA_Huv7ZQXmfufz4ehCUylRNXauIr60POfwgMJ4l5VeAuqKFWUwGdoGc_A2dra48xs9oXiigQP_P7N3py4JJAVN5gEyuut8hS94z1_Z3F1uvroAvhuKoKPnhmncyhdVEN_KzJNO4gDJv1Ef6FTGq1B0ISTLnlj1tmlQPTZhzNWplWGQGo6SWmKO1PNVYDxL-fRSs6rNicUnS7LQQJ-cC_6yoHZ-DgqBPGvsLIEhbYQDXEIJ0turTTBHF-_N3TRP6BhcQTQpoKxH27QakVTOgKi0MHhyu7ukYYaICJoFMWmHO3x9trA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏100 کریدیت روزانه برای حرفه‌ای‌ترین مدل‌های ساخت عکس و ویدیو!
🎨
🎥
‏بدون دردسر و کاملاً رایگان؛ فقط کافیه وارد سایت بشی و با کلیک روی پروفایل بالا سمت راست، اکانت خودت رو بسازی و از قابلیت‌های بی‌نظیرش استفاده کنی.
📧
✨
🔗
‌
https://www.creen.ai
⁩
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bs_lwtzHmLy9hTzybmR7qDsXtTRRZ-SYYMO7jNEYNuug5jDSmvSM0NmLcbybT2ff0l9aqALNXw_GVSDCj6NcwAR1QXtJYzItOT5X42LJG32Y7uNvoekXflcpvS2Io_NRKI2MZKGi1MU2c2FeLZywLv7bUy-WkFM8dAH8GEYsz_udZIAAlh4PMD3dbcHRMailcjT0C7qGKdYrJGOuLmZKfKPqlBDT-mci5pEBkeYnJnvbjhoAJ-hUzE12GGkxyHGnZtukvyGjFZTEYFhtVWCK6kXyyG1oXIqghIpwRka103teVGUzQno2ljfttzttGO-bcrHioaZLQ2lDYi37ivo2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آیپی تمیز کلودفلر
92.53.191.134
66.225.252.96
104.18.14.224
104.25.247.228
104.17.2.54
176.124.223.242
104.16.122.178
188.244.122.16
104.20.14.15
185.148.104.192
104.24.152.74
104.18.2.152
104.27.24.70
154.211.8.196
104.17.88.93
74.49.214.92
195.85.23.208
172.67.114.81
92.53.188.13
104.18.198.203
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNOWXdIPRW4Y24_IXTBNoMF9xTyELiObXuaSt932KdDW0Gt0fZ_R51NvhiPkCiCxAbBrdAvcYZfVOqyjPWoszY3j_h1AEJHQ5yQhN9CDqLhNYwKicnsh9DUyIDj_jQWCd5fwLkunFE9IWIG1z-bt4gWQkf25fmpuQ85yAy4us2ZnIyaHRbAKpIHVtEjmw69HvGGbl_5tsPgfTbIihGgf3oXAAZzNy3NLZa7EYenn8TDLrPoS8xEw8I5yE9fClhWwVxRayF9NX5P_Wk8y5mz64uiwDtbV4bBDTcNBO_qz7ZGcOPiLjFj-105PHmZAx2GF0oOTQ4D7E9Wp7AxQ-oDmjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تولید محتوای بصری بدون محدودیت!
‏دیگر نگران محدودیت‌های اعتباری یا کارت‌های بانکی نباشید. با این ابزار قدرتمند، می‌توانید بی‌نهایت عکس باکیفیت و ویدیوهای ۵ ثانیه‌ای جذاب خلق کنید.
🎨
‏
🔺
تولید نامحدود ویدیوهای ۵ ثانیه‌ای
‏
🔺
خروجی عکس با کیفیت بالا
‏
🔺
بدون نیاز به کارت بانکی و پرداخت
‏
🔺
رابط کاربری ساده و بدون محدودیت‌
🔗
https://zsky.ai/create
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et3B1_1-hWxAig37AjlF2VTfpMWUIbqy4O4YDOUl-8_4ktytrFCjhcFh0qcfHoutmz52yME-O9cEyMRaiH8DQgmFXyLff0p7Vxr9C2Tb-_gXPkLuny7JKc-ik7mu14AY9qtWAzZO5pTreUGMFnVeprxSSxzcSeBrPSzotC4kf5YMHqPB1KPk2z5WMp1xtUQdChG_HAflEdext1DzQItU_dV1-xfRQAizu_yXiXnZS6vdi6xyh1ei6LADdLmHsbSAYlgezvN9ra_hBITRi-T1FNqYmMLnCjw78UAyAVNs0pwwo53oK-M4NOyMmIEV7ZVqCLZCBPF7Yi_6uzqqq-n_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
200 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 5 | Sonnet 5 | Deepseek 4 flash 0731 | Grok 4.5 | GLM 5.2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://seekai.cc/v1
قابل استفاده در
Vega Agent
☑️
از این
بخش
هر روز 20 دلار بگیرید
☑️
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
200 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKR7_uDr8ZB55bR1pKoFU5tqFXSQIQWOrUFAksTTV2lSLNUV-awl49wLMKmYUD7Eu51ZAS_GrT2Q6k_itEDZJaGUASi53bSt4HD9NzDTej9ywKliiWYxISJCfjJO0E5xNczprGaNo4zufGLhPFB7YCCEVPbZacYtYn3yMXz8H0jGNCO_AwgNsIXdcdcBynaTmVTnPOAu0C7bOP-nIyk5B8g9TOmF5XF2CKG2kRzhxxF6WcjivgnePfLaRvfbg3rkfgtzKM-6lQuSXnVnug9HljXkVE4TI9AJty2zdIN0ygO-jLdZ2Dq3LPb5a4qsPzrRJPfKiv2e67i2YtT126J4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emfBWcX4dbg2lMk_eEUZQJeUaw_o9LgkxEGbLKIhFeeHC73eS0naKHfVoL43fVUAyi3a1NB6q0iN2kvzW2nREx9ZYllf7wCQsQNIWYcw0L2hLjRnd7bSVHgj9UrA8r-S7jWzjumHbYHtS0h_d-j1P15ODg7S2FKEP40HKouxaReyLS9vCdkCEMHkrHSKcJ18CwG4Ie4fu-RdGVlEOqTW6c1tZkkIra3iu6J9F6AXLFR4KmK1kHa0CGV2AeS2-JL6xAAmNhS3qHmfX4mCfipBeurTzDeMMm6hVLkcMc6cKWx8sgNnjLJbfG9RPx758J5BcuQ3gyqNm07FogvaBhKlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به مدل قدرتمند ‌Qwen 3.8 max
🚀
‏اگر برای پروژه‌هایتان به یک ‌API⁩ پرسرعت و رایگان نیاز دارید، همین حالا دست‌به‌کار شوید:
‏
1⃣
در این
سایت
با جیمیل ثبت‌نام کنید
2⃣
‏ از این
بخش
با اکانت تلگرام وریفای کنید
3⃣
‏ دریافت ‌API Key⁩s
📍
‌Base URL⁩:
https://api.aigate.shop/v1
‏
⚠️
توجه:
این دسترسی فقط تا ساعت ۲۱:۳۰ امروز فعال است.
⏳
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc28LpflhV-4wivP-TWg2mI7s5Qi3LrP_Avm0n_HA2G030IznTK2iXT3HMaLb64SYlMyc59pQfxTpJho4cn2DiOhvnfBQx4Yc0V3nKmZsaMgI7_ztgGs6jL8wFzXJao-ntldO0kvooIB4VxBQc-3aNIVotO1vHMcEbZjyRAoQjDkHqCJRBS6DBapzUy9QM03fwYo2RjVTY9bAxvWzcnU_dJMX1vVNA1JjBlUANOHvjTJczpoGHRbguOmNlhptAc7S-9bYzLKmCNWabi97W6ESinmOjNEkQ_WlJfwwNFuAEkqtdnCC95fsB0ZXggUldsi8RO2Fd78tnDGoJ2J5qcftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
30 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 4.8 | Sonnet 5 | Gemini 3.1 pro | Grok 4 | Nano banana 2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب ( قدمت حداقل 14 روز ) داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://routllm.pro/v1
قابل استفاده در
Vega Agent
☑️
🎁
با هر رفرال شما
5 دلار
و شخص دریافت کننده
30 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=jWONua5cu2pB-ZWLDq_LmgUDFKKnNT1VwS8F4rx4BvCVjlG8fK_PdV_F2zPBXq9IjMnkZ7B0pXzUwRQI7DixjTdOTbkqmvzQrZ-e5yETud3eQ9u8NzGw_4M0a-YtQxrDQLnQuh9hGtBkZUl0sfy1vkdls0IpwdN0d_POkir95i6WU2TleRGVVateu_855IihTw7zMST4wtLY357t-G3Q15BK-QhfV4CE8exiTXqrm-69mi57MfNRy3Nn_yDnHTTsOP_WwHFP5MvHfHZTRRaAXxfVqJRbsAAfMGpzRLz3_4-emMISRyA84jqRhf_WGJUZG2SLTcyT7zgle7ynVplXAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=jWONua5cu2pB-ZWLDq_LmgUDFKKnNT1VwS8F4rx4BvCVjlG8fK_PdV_F2zPBXq9IjMnkZ7B0pXzUwRQI7DixjTdOTbkqmvzQrZ-e5yETud3eQ9u8NzGw_4M0a-YtQxrDQLnQuh9hGtBkZUl0sfy1vkdls0IpwdN0d_POkir95i6WU2TleRGVVateu_855IihTw7zMST4wtLY357t-G3Q15BK-QhfV4CE8exiTXqrm-69mi57MfNRy3Nn_yDnHTTsOP_WwHFP5MvHfHZTRRaAXxfVqJRbsAAfMGpzRLz3_4-emMISRyA84jqRhf_WGJUZG2SLTcyT7zgle7ynVplXAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
تبدیل هوشمند وب‌سایت به پرامپتِ حرفه‌ای!
🚀
‏دیگه لازم نیست با کپی کردنِ تبلیغات و بخش‌های اضافیِ سایت، وقتِ هوش مصنوعی رو بگیری. این افزونه، محتوای هر صفحه رو به یک متنِ تمیز و استانداردِ ‌Markdown⁩ تبدیل می‌کنه تا دقیق‌ترین پاسخ‌ها رو از ‌ChatGPT⁩، ‌Claude⁩ و ‌Gemini⁩ بگیری.
⚡️
‏
🔹
حذفِ آنیِ تبلیغات و المان‌های غیرضروری
‏
🔹
تبدیلِ ساختاریافته به فرمتِ ‌Markdown⁩
‏
🔹
سازگاریِ کامل با تمامیِ مدل‌های هوش مصنوعی
‏
🔹
افزایشِ چشمگیرِ دقت و کیفیتِ تحلیلِ داده‌ها
🔗
GitHub
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBoxPlus-1.4.2-83-arm64-v8a.apk</div>
  <div class="tg-doc-extra">42.2 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📦
پروفایل پشتیبان NekoBox+
با توجه به
شرایط فعلی
،
اختلالات پیش‌آمده و قطعی بسیاری از کانفیگ‌ها و VPNها،
با این روش می‌توانید به
مجموعه‌ای
از
کانفیگ‌ها
با
پروتکل‌های
مختلف دسترسی داشته باشید و در صورت
قطعی
، گزینه‌های دیگری برای
اتصال
در اختیار داشته باشید
☑️
🔹
روش استفاده:
1️⃣
ابتدا برنامه
NekoBox+
را نصب کنید
2️⃣
فایل
JSON
را دانلود کرده و
Save
کنید
3️⃣
وارد
NekoBox+
شوید و از منوی
☰
به مسیر
Tools → Backup → Import File
بروید
4️⃣
فایل
JSON
را انتخاب کنید
✅
تمام
.
تنظیمات
و
پروفایل‌ها
به‌صورت
خودکار
به برنامه اضافه می‌شوند و می‌توانید از
کانفیگ‌های
موجود استفاده کنید
📌
این پروفایل شامل ۱۴۰ اشتراک و گروه با کانفیگ‌های متنوع است
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=Dz5cKf5jV_G9sgLnp8_CR4ukSrlZWxYX9OLVhWkePf_5uMVVF-lj-y63hBV7Arui7zPe0TBk_3Y6B7wgwWULrX4PdSz65ZfrfwZuK5Fm9K850iRj934hrCZlcGvEKzfBGIWmLwFoIk-rMdYO3R_kssladXNmL5niqkF6wOKkLVIdwpK-3DQGjwW_DbxM5BhqR2W200BWuV1kpPz-ulh1sVzEa5WW0LeXgC5DTZR2nOs47AzEm55ToZnDwlGe8VXOVBvHhW9Ewsb78yjWkHzqmLoXzird5lJLvjVC4d2S98Q7xmJGE2bxt3lXpqE-Xvw972Rnuh9TKD_ZLLYf4bn7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=Dz5cKf5jV_G9sgLnp8_CR4ukSrlZWxYX9OLVhWkePf_5uMVVF-lj-y63hBV7Arui7zPe0TBk_3Y6B7wgwWULrX4PdSz65ZfrfwZuK5Fm9K850iRj934hrCZlcGvEKzfBGIWmLwFoIk-rMdYO3R_kssladXNmL5niqkF6wOKkLVIdwpK-3DQGjwW_DbxM5BhqR2W200BWuV1kpPz-ulh1sVzEa5WW0LeXgC5DTZR2nOs47AzEm55ToZnDwlGe8VXOVBvHhW9Ewsb78yjWkHzqmLoXzird5lJLvjVC4d2S98Q7xmJGE2bxt3lXpqE-Xvw972Rnuh9TKD_ZLLYf4bn7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
کپی‌برداری از پروژه‌های گیت‌هاب با قدرت هوش مصنوعی!
🚀
‏تا حالا شده بخوای یه پروژه خفن رو از گیت‌هاب درک کنی یا مشابهش رو بسازی، ولی غرق در پیچیدگی کدها بشی؟ این ابزار جدید، کل ساختار مخزن رو به یک «پروپوزالِ اجرایی» تبدیل می‌کنه تا بتونی با کمک هوش مصنوعی، اون رو بازسازی یا تحلیل کنی.
🤖
💡
‏
🔹
آنالیز هوشمند:
بررسی دقیق ساختار و معماری کلی پروژه.
‏
🔹
مهندسی معکوس:
استخراج منطق اصلی و اجزای حیاتی کد.
‏
🔹
تولید پرامپت دقیق:
ساخت دستورالعمل‌های گام‌به‌گام برای بازتولید عملکرد پروژه.
‏
🔹
شتاب‌دهنده توسعه:
ایده‌آل برای یادگیری سریع، پروتوتایپینگ و درک پروژه‌های سنگین.
🔗
https://www.gitreverse.com
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ربات تکه‌تکه کردن و آپلود فایل‌های حجیم در تلگرام (بدون دیتابیس!)
🤖
📦
یه سورس
ربات تلگرامی
فوق‌العاده جالب و خلاقانه براتون آوردم که روی بستر کلادفلر ورکرز (Cloudflare Workers) اجرا می‌شه و وظیفه‌اش اینه که فایل‌های حجیم رو از طریق لینک مستقیم بگیره، به پارت‌های کوچیک‌تر تقسیم کنه و بفرسته تو چت تلگرام!
✨
ویژگی شاهکار این سورس:
این ربات کاملاً Stateless (بدون حالت) طراحی شده؛ یعنی برای کار کردن به
هیچ دیتابیس، KV یا فضای ذخیره‌سازی ابری
نیاز نداره!
🤯
شاید بپرسید پس چطوری می‌فهمه تا کجای فایل رو آپلود کرده؟ ربات خیلی هوشمندانه تمام اطلاعات (مثل آفست بایت‌های آپلودشده) رو توی خود متن پیام‌ها و دکمه‌های شیشه‌ای تلگرام (مقدار
callback_data
) ذخیره می‌کنه و از خود تلگرام به عنوان دیتابیسش استفاده می‌کنه!
🔹
قابلیت‌های اصلی:
*   تقسیم خودکار فایل‌ها به پارت‌های ۴۸ مگابایتی (برای رد کردن محدودیت ۵۰ مگابایتی آپلود ربات‌های تلگرام).
*   امکان ادامه فرآیند آپلود در صورت خطا یا قطعی (کافیه دوباره روی دکمه همون پارت کلیک کنید تا فقط همون تیکه دوباره دانلود و آپلود بشه).
*   بدون نیاز به سرور یا هاست (قابل اجرای کاملاً رایگان روی کلادفلر ورکرز).
*   اعتبارسنجی خودکار لینک و حجم فایل در هر بار کلیک کاربر.
سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcyhv1aUwEWwruKXLpqFpygQpihBJukcqeLzLZ0IN-ZY1oCQHATDCJY7C4NjpK1nwBZvib5bo2fziH3Bsm64H1R0VrEOxxy8JiOxbpwKqtXaCxT9LiXmm-_o4zG7-STBEe9Ntu6tuKpIej-7Hf4_VdgnzGmCr1HY0xmn_yV2AdzcKe1Tjh1UeW_ZbM7ao5pI-mE5Wfg4se1XFcP-PUKmLerPXSF03LVKFQ6ZDgTTFNThjacyuB6YrRHv14okJ6sSrh6DQNMbX8bj6ZrTYK3reRWOpDi_e6O-w_j198GOrff4xp4O2CO8wKbQYTOgDi0871g484U807NoqVZjHMmhbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=UU3uW2LN5Jt98yA3XO90bolChcDc-WdFh9dyLQh932mCI4EnC_Z4TrZMmnKmerpUsDdd1IrVbYcJN-u_AbIMHk_HaFXtpBCrEJcM9e0zUEuRZsZwLKik4fA5fGER3_42AcUbLuEAUuJIvG4Mma8KgeqjYbb0oNzblWPP3CXPYO2YgFVxrfId6JxeQHw5ipi9PQ2uuf3-CcF_hdXQNhCT45DJm4N8tl0VcVYGE7W60fpCd8Jv76wNccbrE1uQfMZklR6lCti1jG3mFeeSg1MzxSBNHzBAwDmC_zowvJS10jXQO3t6c7PjBljvWhMyP1X1f8kgL_pGDafo9SGjvFb2iqdp8zsUSuZrmuBvGm0I129K64lznu-EAKUoq6EFlIsS3pBhD9YMIM3xeabOne7mR704R7_k2A71lCLyz80bywMe2z3WMcq2xLjv3Lui-iHB5aX9bFtD053zUtyRgSr1UIQp81kT1acrDlNkmFSODUyfyKXx3yTOSnzjk4X88-AZ-Cj2TqFggJr7MD_EdbWm37mw2Z79wwQP8AttmwfklWIKu-_1B4rQ07iVTO9l2HCEx459PtkPaZAcvK1rzobMbyQKzTP2uFJWz9W-AoLBiLexp9boLhTZyndzRK4EoNne2yYn1UbJSmanepFyl09cCKSiZrvGIIF_cGDFR8SJw_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=UU3uW2LN5Jt98yA3XO90bolChcDc-WdFh9dyLQh932mCI4EnC_Z4TrZMmnKmerpUsDdd1IrVbYcJN-u_AbIMHk_HaFXtpBCrEJcM9e0zUEuRZsZwLKik4fA5fGER3_42AcUbLuEAUuJIvG4Mma8KgeqjYbb0oNzblWPP3CXPYO2YgFVxrfId6JxeQHw5ipi9PQ2uuf3-CcF_hdXQNhCT45DJm4N8tl0VcVYGE7W60fpCd8Jv76wNccbrE1uQfMZklR6lCti1jG3mFeeSg1MzxSBNHzBAwDmC_zowvJS10jXQO3t6c7PjBljvWhMyP1X1f8kgL_pGDafo9SGjvFb2iqdp8zsUSuZrmuBvGm0I129K64lznu-EAKUoq6EFlIsS3pBhD9YMIM3xeabOne7mR704R7_k2A71lCLyz80bywMe2z3WMcq2xLjv3Lui-iHB5aX9bFtD053zUtyRgSr1UIQp81kT1acrDlNkmFSODUyfyKXx3yTOSnzjk4X88-AZ-Cj2TqFggJr7MD_EdbWm37mw2Z79wwQP8AttmwfklWIKu-_1B4rQ07iVTO9l2HCEx459PtkPaZAcvK1rzobMbyQKzTP2uFJWz9W-AoLBiLexp9boLhTZyndzRK4EoNne2yYn1UbJSmanepFyl09cCKSiZrvGIIF_cGDFR8SJw_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window $🪟.npvt</div>
  <div class="tg-doc-extra">3.6 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرعتش از اون یکی کمتره اما بستگی به موقعیت مکانیتون داره از بخش configs پینگ نگیرید.
🇰🇿
-
🇫🇷
-
🇩🇪
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window🪟.npvt</div>
  <div class="tg-doc-extra">4 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر vpn ای که داشتید یکم ضعیف شده و الان به زور وصل شدید
این سرور موقتی میتونید استفاده بکنید تا استیبل شدن سرورای خودتون
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG-rKY2C2rTz6Fhp9QjnBA6M_knz4sCOMJfF3-ghl-Ps7GTulQyIzVDUNWAzhEuHrx_8ShLkOgyTJVeQp4nhzfRF41svOsIfDOTtr9Z8cmFpIZDP-RsS0HgE3F7n2bcnYoQBVx5gHd929Ejwb5mkHz9Cbr6E27W9Lu-qy2g8UmKCNeoWI--cfZjjQ_KS3FwRjGELBIK6DvyHgLnqqhBHAkvfz6OPMCbNIaGe5Ypm5NiC7Yt8SreaSMIoISfwnv-uqC-nG5lbMjL7Sv_0cngwopnvkusMmze3FdhlrPfGEwUa1JuhM6ZxTYq1i2VkmcjAWGVaIvPPXLCvLW-huAlPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
فرار از زندان برای ‌Gemini 3.5 Flash Lite⁩
🔓
‏
⚠️
نکته:
حتماً با جیمیل فیک تست کنید، خطر مسدود شدن اکانت وجود داره.
‏
برای دریافت پرامپت کلیک کنید
✅
🔗
لینک گفتگو جیلبریک شده
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYhujA1gJbd5O5StcgeRF3pD3-KhcuqVvgv8yNo_0RwxUhcNgB7t1YCtcSNgnWigHgFhWLyCGZDpoSYSwiRu5iTeHOruk36IYav0K7Av1kaYLL5ylUizBvhEpKZcK5JH0f2lXV5tBGc6Zzho2AIfe5DmlSxfp-JHD7pOCOkmH8Fg3PwTL77OFueiCPrfnaOEZASBZ6_F6w6PY660U_fnSgvjtf3IO1QN_tvowgeOrTe-CSpJlVzY861f8DxGYBlXLnHrYTROeNrB8zaKQWq9C8DZqmcVo_ovKdblHEJ3ZXuRc5Ak6xtb9ajkA00t2swFEjgnBhzTHQrrH8EZXOFspg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوبِ بدون تبلیغ و ردیابی با Invidious
📺
🚀
اگه دنبال یه جایگزین خفن و سبک برای یوتیوب هستید که نه تبلیغات رو اعصاب داشته باشه و نه گوگل بتونه رفتارتون رو ردیابی کنه،
Invidious
خوراکتونه!
🔹
پخش ویدیو تو پس‌زمینه (حالت فقط صدا)، امکان سابسکرایب کانال‌ها بدون نیاز به اکانت جیمیل، و محیط فوق‌العاده سبک.
✅
اصلاً نیازی به نصب اپلیکیشن نداره! فقط کافیه برید تو سایت
invidious.io
و یکی از سرورهای عمومی رو انتخاب کنید تا مستقیم به دیتابیس یوتیوب وصل بشید.
📌
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeWkVBn67_Iz43nQ3TlwpXORV59IWR7ejXP5nYBFqTWJBX-ypKHC_X61M60EzF8ZLSbgaOk5gK2Gnnu0dGJadv1pTurFVNwm38Wn_c8P14T6AEmHe31NKCRLUr9e6sVzf5eMtxwu8tg1tfN3Ba-8-7F6NePItgVdonfQxHSmTcjmQnWXlMZn_E2RdTAXsnM8cFNBxRZReCongaVlV8KE9pk8Yc3WQQDmb2EJo5Lz0ZYCPn8jCwNsdT-GbRID3gr3pEaQI9ZQ45yzCrUQpvYqf6y3YAF64RfGJ1pxt6BK_ZnjhPKkZZ0YjBIcb_8ERnkqwluaYyB7MfmtbrojZvKt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
