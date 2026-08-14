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
<img src="https://cdn4.telesco.pe/file/k-Zhw09HePJAiv0qptQewWFKbeofcYVBB6viAkN-Ae4K_FBVTIoHfXdHjFRCo3l-E46UVFO78WZJQk8WBnMcCZENixai7QZQ0ft-yLlMiChc_hWk3sB9piu4INFRQc_HDaT_0mQByhUsebfcSTtVTfFXomxlTOQ2krgS8pmw6UsRunyAXTyUCobunpIT842XmONydlt3UY-fD9w7Yn6XmZQreq1BQLS2gci3OzvYJ48DE9f0eapD1NkKa-Gez5Ugn2MyOvQaHkCRHnnTSE7ptGLNeESTiJX5fLBc2hw56T7i-JKhiuoL1mHx5zdxgOolvVgk8kjvu-MzTZEy1ZHbRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 15:07:27</div>
<hr>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 549 · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahkM3P8DEYX3PPoHPYN70zwvcHyvAV0w-To2OtZwVW0C1_7ATRDTwEKBx3blkCyvRkNWf16DRfY-UPEFy6se9vY1N8MlY8y31XSHt_AScaxGHYt9RtNs-tJ0NPxfLpT2ALizkyaJIrPqbeM6l1HR6baiJC6dLt3ha0b6yTwqsKaxx8pYmsdPqkgFWgDQFx1FR7FvT6H_vPNBSupvl--RwJcezj69r99zfXYBY3XQFPQA6zGDsog49FnHqZ86ETSUlmZONuTTOjbgurjAvtRu6q0RD70lOfyAnDIR0hfm2o-1w273mecygSwFPUDkeqFePZAcMFuSYyKr7H4hhF5QVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 675 · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRPLvbTN2BPfcjIpzUZUaEVijjZDvWbTPcY_8uvPXDaz0JW93lNu574GmbL699wHQpk2ZNyJ-_DX1A5A06OVyuitRKp8KUnyHUob4SZofxhCSJpM7A9AdBjBGKS4B5qQ1iTOagn3aE_u5tQDfYZmd5ZrTFoBvKBPnwG1he0FaPNrrBYt--wbFY8xUFeRFcFQYPfK13eQ_Ld-C3-C_utouDqK5tk_-ejfMTZP7mQzkijLct0B_T9wTSt5sr-Hjki8nu7MQEVFPi_4VVsZ6kEmnsWuwbaN5zTI8fhKq--F0xVspnPMcmSJTJFvSStNlrLhkqWX9aONk_Ci_oLt34NAug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eW1EUeonAxZ3g85BOgi-HfgJdhjFTAPGdmtPiOzALN0CdubNftkOR9z1xFaAx-MP_nuYrwd4SLJwv0g1kNid6JxLbo3EleRq62mIgMZiQnhHenQC86oq0gN6VKv7Bgj4O--ER3fPID7HMq7fRBGzqZGn8EtTlT7x1KzddOpqtFNmSux5KRazhqkUDeu0uYz6-d00Ep8yOKzKNHSFW4VSLEZd-yZvu-uCxUZ7FxcLM5CaFhnj2-1e-Bveqgqh5bhDuZwQfNNX357XPQynFRqa5C3DWL7goneQ3Q8_S1xJiw4grsr0MdEC39v4BQCfcoAvwec6SgJ4Pj8XV218FGguJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyeMctGgxJycMO0kWCoII3Jgb1AubbDkbXQf4MZRmOv3esB7sGXa7pr6tBR31yHQ-bsOdRHUfnNT-T3wLTVNAXW6yYVs17twmUqOJE_8gVy-EIG4b4C4t-WaOerA6mNDrV-_BijFc3ORbIrQNelV6GAAlG34cOSaAL0dWS_SQO2_P4F-xk9x2H0PWVlHogLK_FK4-SLt6W47X_sM9BIDYlec-xNxyoPGk9AHQW2OFfnzADcsMA7n_LZSLEdWOwwqKMuqOYoaR4aHVztEwhpcCdzVv1Elztk3EBwI-m08-zdbpc_v3OZSLJznIqkR6e-Qwh807JVkd_DXv1QjVcr8Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlwPrF2D7D3Heh1pO0ihVbOhlWsct5fGxn4JO2o4IwHKBQq9c1Sz7sONp907BsflhpmIOkaSoanbt_q-p3em4dOD2zPg4QPVYNevOpwmEgwmXxkugvz2Zj5ClHI9HLXYVPWMPkt6_w6Q4lEAhMJ2iwgPP8g0EvWND_fcfseXikGbE30hGikVFOtDH2DjnJtdcISLhYzTeGBz5tZBJtv6nfntx9sNscEnFNJ_IM9zQnK2_7JehFRvNeSIA4Kqk2ipch5S6JEoSHrdFQTPIqukEXsgMv24rA2Z1DmS-IWHNQOvgp1OZ_SJKyqDUJH8lJ8xpw6hN5dGM6WKIyyuc8xZXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt_3A4eRJaVVR12KT3STrQ0j8ndD5zKLZRam63QBH0S5SWzhihgwWDsHckrJYOT6822MfqMe2rh3oS6vUmuC6CeNafWedg7HdqyFROtgo5iH5Je57pbVZENWJqRcECy5szT0sdlUIA6RM3PF3yfTztLsiLaj23Z0LANneaToRhDmio0VaK1fWeDG-20v75M7FBNq7O37bstDlqSnQFpOwzhmQe38sqGNIKX0HAIznwuJLjaHH1iiBy8bt-jLw3MCW_zRXbR4yr25e_xCKxu0AD9KjBgGb-Q_dBUNihAR1BvHFM-h6vwPJfFWOM128qRIM0gdvJ0Z_3qNsSUaZMPavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2U9nNU_RmT_FRc5DAozxuLOgyls9_34GiLoIpflP_KZgsC8-XGZUHEAsRdHBVTH3GTG9RYreZAkqbQfg96yWyEClGoKLeJGOKg1JuZx0j_Mi4ec3kh91YaQHEhbrecXvVvFZHkQI1a82Ih25eHiX_S7RVaVlFwe5j8ZxNAqOBBArlf34AsyrQEkibKBrwQ-wwZXyHdv1lnXyRd29_0INP4EJinDJnTrbRiLO-ueMRj3uPKJXQjqdmtysYsT3FDslsvG-uqnCwc-dmRQcwp7mhtBYpPMBNCszIbPlFLN0pfABcbB01Q9HebnXG5xfqe_V3LU9vilKs0P5UC4Hjls2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buofYSaDJKdKVrYZsWkFBLj-XvFHhlMoqO16rdXxhzA7PYKOaD_etHsjY4ZzvzMY54eiqxhKnTs1X7FGJgtEtQRjXu3dv9ubz8g6XGbnrCtwLcSlNOG4f0v28NsqNcO9Vcw9PQITbyfQnwdJyDmCEBbb22_8ul_byjbGxlZr79iWzS-5JlAqQ55aYwqh2DMeTvx37lb4E-Y5g4WD95lqYgGyW7oG_nxy2jC12rYatK18H0eVEmq_6flK0Dk9ecpChI1KxmlDQZvUj1eY1q7lhbR21hwD7bPWnpGL9sLn2aT1WNgsI-ihExR4-aydbOh2PshMoXsQdKHVibB4wEUFCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPI5n-VcpvpRlgKsPrPqcRq-Lv7uPlXBEBxyFvrTjmuqaFKeCRXYl5AnOkZEV0fDIK1UJ0Nvbjsu3Gdbpu-JKFxH4HV5dA-MwzNloF0TGV0DB4tTlC3L1OdnINy7SASvn4AGmBQu61wJwjhYvUKbsuCU89Lw1zgWmIfOjqoJs-ww6bGXlWyk2Ypsws3Mv2Hty95_2CuADt_V1wggmVlMfAagea2t4llzS_puCZt1nGU4jNdpvZT72JvCi1qVKUS51NMkmPygvaC41zE_lPZ0pvKj8fIk9ejIqVXpEX2uHMCzZN1_vX3m6oyll7tZm_yc9XpYMyIvy3-Da9uREluKcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnEflfH6UrTZPsNVzrT78b8IYRoXv7vIs2OJG1miAV_Stddd4wa1UTP06--AMggv8oeoLHyV2-lSv82dTnOFROcC6b6sufR_6jOYQ6nnrhjRcz-V3UqieG5kYonBUjPmxdDovdmVh4dF7KoAeJT56hV9Tb_QIfBrAxOI3_aPp-EDQ80m38KoLqROHgpLN-xnI1xUOQSyDQBwu8dru3haslJ4HccLcaCAWR_8Z1jsz0O3NMp4k3m4zOZ-SL1npBxGvHiVL6BBJeGATnomrc1PTskTYSMCI-BYGiB4dYIy-E1e5iIrZ23OB4pP_yo7B9U_Znagcdj9zkwV5aIvRBXUqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpaEwZTlVKX5o-XeAbNMxVjHei6C9_59UQfyRT-wwmum6eXlc2PJOGzb_F7nWQcsVv9xX0s9Py1a3W94HpMWvo_E_otV2jyVe2j7hBwmOO7IGo2XmaMwcifoQFrSzOPxMdg6M0iaxGRxVYvi_3hBX2Uj_be5Wqhf2ZXAlT2FyCu88wWh6xcFgntsUygfN1pRZS3AD6gwFxS3EvNOnN5XUKKv0YNQhx8mLfNWdAZOQ-T6F7tizj7cdYJClonMsTyUhE14yiS78pkkytajkzELTO3Z1YYt9N5GE0rNoRPcqZtzn3oEEzrbBA5jvx3linXLb_J6ISW5Z1YOwIBpdW3pmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI3dtM3K-hjCUpLeaMAvQQK9oyED_6En0TK5RHA7t6NfCkN2r76tdtiqs1IcVOr0eTh50648Scvq1NM0GVjRxgigQEPQZdYv8vNQBeK73knfvcUyb0DZx3H-H2sBIfpRGyRdJs9Zq3RQYdTemlwcT1NFm_dToYIGj4ckuCZ7Vi0gIF4efO3JInawFGU8tGH2o13iYhROY-fLgnVcnHGZ1NnEutXCytH3wdRmlEc2ey9n3_udzgWDPW8i0EIgCYOJTNtXNV-FlIIQDKB4SYYxumGovD8VnV5aGyvGnB_83_whn8Im7sstukrbElzxJz8TWEvfh53FCKEUfpanTxS5Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd487UUszf8sP9STAxoaILJvqI56TTHSd5_w5wBt7vHRaltb-5RBKSv3VNvLARaRADxWc6MXtKWSj6ydKbM7vjR6hdnbSFa4TiHfCm_6naFlEx7BIhaE1WjLmIoZaD_cTalU6WUsPrMK_Kx9CPMMBAhZt2UPhrRzNIKy-sH5Bib4pCLDFJfZXsgP0ZQ81FDBi9pBxYqZiSJgSAdtQ-YnV-O9_9oBB7KGnQFiMg1ZPnuDbDhkERY7X7HJ2Jy17rJxZ3cFCGCIbBDJXg7EETen3BRNgUBLNmK5Ctw8WZ8rVvOEqHTJhk_r-7hGTHPffCIQvx-oormlTj_-26mzTH8Ynw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glTbpVKGscr-CG8Vqp2HyDscWUcIZITrVTAEgwD1QQBqjNPxfK-qHnH6WzeQ2moTdl8RWGpfL564hFYg6UFQ9vJkqTreIffpSvvdK_dGA_xwHwLZRC-RtP9OvWVcHZcX0Y61RjHERlFKKwFxLiDezxJUuSmgDj1tUzxOCDT9MTQ7Dd_4OmFWjKpFpE2qyOALKjcpZPATLma9jb-mYBlEi7B4rMSQ3axziVffuaDHwoPBS8FrhjYWnh4FRDKNYwuValDXWu1EbZ9OGTsjVrAheLghAP2bprhvGWy00u99uvKicHX7ODgydPhgloOmoy9jhP4qixGyE9bmTDAEv2uohg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN8_7NzsBz6x9UcwvQ3riqINqIQI3Fav4D7x5r9gl3oIvY_zx1LxfdQFJlpawvRf487zEKnWAXahjriO9lzzTD48MZn7kEEwdNnptHdEM3KhxD-epY306AzsWyIC99mISliQ4RqAd3WFVf4RSXxrlSNaNUeb9pyxko0tVGMSItEMCRNrHUsAtVFY5rDIF_-G2qH2gy_1aS7LCdCczDDlHuv5f7rAfJ-hiDpn4jThsCZYYYyoAI1FlCMAHeHdXysIchGTFAFIst18LvYDI4YvhZ_dBUGrHMsR5og3RdKPyPOehsMusVTP_rD6YnOfGe8IV1AsrSMmFt1wPlotNZdEgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKsoKHBM5KAusU7HJTS-JGLozyTdO62KHV_E20dwY-HVT7SYc4npigwmu9QtuBN28V5_T2lJYieskRpRoDF6h76l-e5F-8bm2FGu9Y4CBGSqa6fzSYOas_iLTs-nxkAJh_0K7CeKl1XBp8_rBqC5aHX5lvEfybq7GgcazjoQWrfk8o0wkI3JaUjz3BGy6GY8RDr94qmPWhg-oL036op_IZl_9775UlbcpWxSrhhwLK7APAF_uWoj4kyUbJ8W0ZfYhWhk1S9pvJR2yQq2pW98bDyiv1v5QcUmzgyRXAYXMjux5Qbalo4uZAuOMvLzXIkOp9560xkjXFyBvUKXfcWizg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtfprLlKURMyOT6PzRKRWfWGMH7k50vk6TbkcRarpU0Bezsh0-vRECDxBjNpGqzTDxvoHYj4XTZhp_CeOIkTF2gzKWxhkQ33xcpQUm7Pdli5ygX4BJF0HUKgie7V02V5eoVNmnMEo8XCblrIQjy5GbXpm6PREgWHNm6bcRYuDMdri9Er7rtFWt93TdPc9zcrqBCpPOX4S6taWQFAcbn9rmSu8wRfB-yqDfvk567NXMLDoYxd9g8-5D1kd0GNU4LUW5U-NfBTUGj1nsn3X7pfZa0kOxMndD61u1ZyuxPOOH61t3K4D6ZZQpqL9WgPXY8y_Z1khHktEWanNCZglqqfWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRE2Y44h5IJp1V0pcCU5K_DzNHetjCzR1YvzECXOlX9beXrWOnP7EJH6xyn2XlxRAHElWBFu1M4zAOHyRrsZXHFstJLsJFs1Sh2YunJgW05zbFgyuywiDbViLLszb8Q8_XAvYz9UCfh9YB4x5145a5vH2Bf58GW5TrwqVLTefLpMMiLriqy2K6nijmRJHq5AuBXPbdtEFjs_O0z7mYM9kxiPZejx3yXXF3Azeaylf8IpjhEJp1-QNEszxZZ6x72p7M-knRYpCjZzzQ0bS967mgqOwwvPcah8e6PpScyql0v0SGKU73Sp5swfHWqWP-7rKZy_B8sjRBPwaaeA4oLTgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=vC81p3h5zoHeiX_eZWgLjKNtLyoFVSo8D9S4_rmEEpVJmBezGcyeH1-wMx-Dy5f8ATzQQOLIvd0JHLAMTwGbGhXtIkJhWzYfu6itohECBnJn_A1Y0wO7nhNzfwK_AXaD2tjh5puIq5Hzr7TtJQ1HxDtn9M_C9SPWO2sC4q4aG23qyoTSazvgiYvOqS--m_XlmgWQzyfc5N-U72QqhcYWjDxhO8uaMJ8oQlizoAccoYUkuH8519Lx2ebVqnMLeTieVwkSECyXURy1O11CMqsYGPWH0L45qEoHI9rH9kC9HgD7p9GVH8HHswzIyLk0WGNaUP03vPxcD89cKPQqAkWvcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=vC81p3h5zoHeiX_eZWgLjKNtLyoFVSo8D9S4_rmEEpVJmBezGcyeH1-wMx-Dy5f8ATzQQOLIvd0JHLAMTwGbGhXtIkJhWzYfu6itohECBnJn_A1Y0wO7nhNzfwK_AXaD2tjh5puIq5Hzr7TtJQ1HxDtn9M_C9SPWO2sC4q4aG23qyoTSazvgiYvOqS--m_XlmgWQzyfc5N-U72QqhcYWjDxhO8uaMJ8oQlizoAccoYUkuH8519Lx2ebVqnMLeTieVwkSECyXURy1O11CMqsYGPWH0L45qEoHI9rH9kC9HgD7p9GVH8HHswzIyLk0WGNaUP03vPxcD89cKPQqAkWvcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMtLHOrKYRzaK_xysyF1QSlqHau-UmftdXoys90wISHyDjR0y2AnUvGLJoZcFpTqnbGJZrbibHrbrSsrUx_5SNt3W8IdYRqnPFH_U_BIno7DG0aRQLJVXuVXyuNTqjlO1icaxxlT_5rsVCMjeIKtOwd9CVXb1LO1g44h46DUsce3LQ-12sAupf9xY3bsibuVb-Z0koRiygxeT9kfQnqtwNJFTJWWWXGpKDBSy0lOZZan-jdx5b2Zw6VtY6c2OqwgGSQwCCkrmoISrTV5IV2wDWZQUsG0XbU6ZBnUk57fwVG8kM7yjTAXpsY9co-zbv1vp7ew4bLhT8_5sB9yOc5ycA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=EpDocgu0FcEXl9e0QjJmQIMzESaR35gbu1jCDkVTwoSq8XiJ8a8tRvTZ-2WHH13ST42inKmyQWkD7aV5anclqYdBSI0SKQybfVVAVGygFIrpmXkqe6q97ak2zJg1MjGFQVg5HNs8x_RVgfGfJKLPOt99Jbu_MiCEOfpnTjJLFxnVuUJtu1UeeOSxC3ASZyDFrtgmGmXv3lOSj4ErsgKk24lS22y2gonsIJZiXvcUja3K-1gW48OxmnkCgPWrD5v82W7MZdQrDaE2UO-RjaO4mOm_C1jywrcPNlK91FJ7Ksmt99g3Nw5Qz9Nva8-MyRq6pSMIdnRl3mpK5Y8bRo7zKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=EpDocgu0FcEXl9e0QjJmQIMzESaR35gbu1jCDkVTwoSq8XiJ8a8tRvTZ-2WHH13ST42inKmyQWkD7aV5anclqYdBSI0SKQybfVVAVGygFIrpmXkqe6q97ak2zJg1MjGFQVg5HNs8x_RVgfGfJKLPOt99Jbu_MiCEOfpnTjJLFxnVuUJtu1UeeOSxC3ASZyDFrtgmGmXv3lOSj4ErsgKk24lS22y2gonsIJZiXvcUja3K-1gW48OxmnkCgPWrD5v82W7MZdQrDaE2UO-RjaO4mOm_C1jywrcPNlK91FJ7Ksmt99g3Nw5Qz9Nva8-MyRq6pSMIdnRl3mpK5Y8bRo7zKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpTnlpq_aaqovnNhN9icDyAbhPhM4_pj2Eln1yr0zjFleapZeo1DmGnPHMnR1EY3jv6ViC8fNpaRghbyVL8y1ANoiQAJF9HBVkgbjO8WdrES9dEfVJpOwQisgFqjIajDZLyJ4hqW98h5GaNsG7m7O6kRh85KRqNsgSvjowT4l49OFF4zm5fiMVYjY48FqMl2a1TSFmUW-cukXMcwbjpA222cEV_lvpYkH1QiN6R8_I7j8Q-J31c8m7fXvK9mX_dz_xFvtB5-tInRkJKHLU9fyGJkPwr9JfCYNsvhiwke-RdjA0H5b9mLYAiq5Bp_ezuDVjj1a6liM9Q9jBKF1vl9Dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m37slxzddojkh3s0qz_k3H-DgKMigOdeIjwhteyC2Pms_gekMIcL8rPn7dUQMUby04XlLIlebYdFMH2bWuCGD8ncoxJiISr5VMEwKK7oKWCowC3xdeWvPAG1zVCnebo7qrDXfP3_6sNFP0-s_la4m-logMiyXTIXafJUgLvAjqKo5WTWlxeqDjrpnR5zsKiHLWk_-V26Rrq4JJGRUsgK9DoFjNv30O1gunSVih7nXLjZ-kF0-VElLPtcuPwLisq0_WE3b5Cl8NTrwJWKEjCUeeZEAaDUKmHwrPIMJWMsG86fS2gXfWfFdATju5V-GO0ZqsmTN3HAiEfN6Z26AbIYRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D718KEThDUYmiWEnmN3rwJ8cmqkSd2eM7FPrGGa_H0aJjcxRzUXBi-KMLgqJ_hPfFZDmxTVqcY2JNERHlUdBkTBtv6of_KfPlCcLfIr9vwinJsf3IsAOcb4FgPvZYrVb-Vlw37Q6S6a1ziGi6ygO4vL-aNg0x_teFfEnxVv6yxvEu5JjIIebukcf23pBia-1k-xkHcq-IGgMQbF06ZHeNQv0ap4ifBZ3fIiSsvbKbuKAtzuYWgBEGnRWZoPAL54VHGbn3IlHEtKdcNOKhOQwkg36kqJMU3XUtYmFQMS3v_JRcifkz_H8e_jWTYqUpTVoGwDWapVlvki-TZSf0aIfHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=FdMLaR6iPzRus1-4zZ9BAcBQyerd0HKNuGKGYcmRox5X4hLrnHz7eDur89RcsTa2UxrkFTwS3poHv_HO_VfknerYPxOyddoR90ErE_bdsght-w1fU8bTR6OEhv4PCpJCW3uE_tZp1Ceq7-yhwb3GDYZosDZq3-IkHDIYyTqWf7AjlixjsvZRXJlyp13geM2RhDbYfYYtjdvEu7NEbyaGQHlPwc1-_l8HltTzL5QmwEgnc9m9E53tMsfXxoPc1BT3JB4KmTBaBSnAy6XpZkwSNQ3zN601eP85_tni4Who3yeSswi9tZ6sb4RAxKOrP4qKOfGeFNK0_Y0Sa33AAZr5lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=FdMLaR6iPzRus1-4zZ9BAcBQyerd0HKNuGKGYcmRox5X4hLrnHz7eDur89RcsTa2UxrkFTwS3poHv_HO_VfknerYPxOyddoR90ErE_bdsght-w1fU8bTR6OEhv4PCpJCW3uE_tZp1Ceq7-yhwb3GDYZosDZq3-IkHDIYyTqWf7AjlixjsvZRXJlyp13geM2RhDbYfYYtjdvEu7NEbyaGQHlPwc1-_l8HltTzL5QmwEgnc9m9E53tMsfXxoPc1BT3JB4KmTBaBSnAy6XpZkwSNQ3zN601eP85_tni4Who3yeSswi9tZ6sb4RAxKOrP4qKOfGeFNK0_Y0Sa33AAZr5lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FflHP8a5hJcHtXTHIvdQvzaX6RCIsAD9-0nrVBvRQlYAHeGkshZBI48fIMEWcEDLn0XXP9vH7g47UskaFbgAnyNt-iXGZjCHK62NG82-aduI3Wqu9KIvj04vwdoWuXwDEnapNkLXc-qhvLCDQwtBbOZ6fLT6z2DdwRoS0JO2FZ3nr7GDEWL_l24aqo2s85s1H8F2jrkCNIgaPzBytil6VAHRUjtRy8fVtyvRWq81Ar3DDWFADoItSnYa_Fnm0zRmv8xO9RWSSiit_10h1V-Uxo5y-Mzv74mCIm5sLHByk9kHDVn4OBcbHUnoQRHqJWoXJlQ5B18RKjGwWIVcWVJceA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD0FQIfeMY5iIen6wegTl61XP2iMm5gW6HEKNWqYaPOqBZLzGpcNo8MRcM6beEnqE4fcH0svOqrucDYjj90lxvp8oM0t4xEwlbJgPLtEsNPGW6zPa0UIv1FiGcwxV2dZ8vs26nMWeHRAukSxcD4LaJcc_Dprh9qMj2ynSAfr6wbyVHShbeqdbpZlIgHs4Of8rf0c5hkXYpIsTc5aYm574noAuKPDbRVU0SeLcM_5v8Hk_YqBIZSkGvcTBq02FVryspheAfESprqvONoABWk1jzfq6ceVIZ4quW23uBZj4GuexdXkKjZ_xrqTSxu4wPMwWs_T4PifVvFZvIO_OC8fhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnX6aom3FkqDQSaOhnwPMz97Qrb6ov5nyJzIe_a6Vdj1TobdPksywyvQ4o5sgYwsrU1bIqsFYJpXWYlY-b3XsrfXLHT7FNPDSLfuSyRuxx0JxdEl0pxHdiqhEqVLfSS_OYJSnmhm5zuOrcaYELaro5mpj7jihQfr3YfbUkag6HD11JRgP9EyZn-NX8ndDf3QjNcieHnvgVo7lgialuzFtA5mqCdxcqVrjahjWkIf04Vj9gkMhLkLn37Xlu7WSvCeJL9q90E4d_pxYSD3hMIfv9KErtM_6sqgi3Yt1qCnw1HJ8viXXdJvtIq2sBNzlFKqZ2aYEEH4crOTtR_oqayuVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGX_5iJ-nvVwCAV9jiDnfbnqnH5xSLf5DLWIfolffGYfKTtUhh0bG6FQUYOblAlc4xUWlfvbzyJXXiJRxNzlh4cggHj-G5I9Ss47yaxVl4qCoQVdHoDC1kC0fHb3x85APRfOi5ZSPN2iT2AHEPIMjPYSXmsihC8M7C35CDnBXn2XRmUQ4a2A93RyyEgIfDEod-eTjNP-MZ4hEWEhsHSH099ThPKbEU54qFdjWpKHYPoliiL0f0gThAvLCRkvwyiz8trXxFbM-tvFsq2KvddtZ17oCKLGAMa4eLayNp0ly5g2qLADJTpLfBwRgKjlCPdXZy0gTNbGaoRgX97oIVTiGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqVjhwTIDN1pVlOtWbsfYu6ZWlvackG3FQlL1S4DdUsP9NknpQkYWsLTAqO47oS-WvShQ6EVW4dcJGgbk_bQGMwq1m40zR4lBn7RTc9IvytO60nKu0q8rTgN__lg9EbSS9OOJe5_GYNoBoU4g3PpaYDvPamtecMC8qbPMUZiYo3BdnU13EbuwFlaxoXAnWUiRkpNwX1diqQUsw-1G_r_N7Q0IZmNJ-gM6LkdpjjvAzZGu9bUVFVYXJ-vOPQbjqlC3wkBaC3Ux-B69px0Eky-RGZZGiI_VLPd0tsZ5L-l4JPyUgdKaWWq6NSb_WFHQ4ooenV3E0DWMik-1__qgfLDGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2-RcFnNL1Vf2HTGTVi3aU1qVq6T3wLUI27Me9scJrfSllrXgq9wQia5yxNfmnZTGHRhhsy0l-OHoYxjZMT3zJRsX-BZ0uOjvKIxFMOSi2MR-ZlX1x79cIGM08LqjfRYX-B_HlPysHO87jN_yrKgaZVCXv9-mqFRtRTm19Nn9ZIMTGiHDEwVd9Owttg623CNtlISzMw23UQ5J2NMYM4-myO_Hy4hdt7dEdQ7hozYwdClQxPs3bEFu94IQZ2WJvBwTzfd0rydatEXlzWxmOUCF-a6ttMklGjc1iSc8bMsvAETaKRV4vUjCCoOdXHTXJV10EGfD6aWTcsLpfYVxs9AgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hls5HZDF14YRHQxYAMPQOtnQQ5EfOwBCUcRYeSELJJu8uxIBN2tp3o0XY78pFLa6JROhw_7uNbmAvC6d9UO5py54wvpE9Qc-HkKCD52gaMJERrvQnbEy0snUEVFaakkYCG-9dFzG8RejrSiJTpe3F1rCZG0CooU4-L9ViricxHD4fzrpJfAIiwlzo7AqfWlj7S1ZCkNd9WrQ7_oF5uV46VNmIsmatCpKCJpm_Gn7aKqycn-qgqvbur915fcsD63IcFsDmbXFX1-HYFr9DTlkoq65pfUW74tlS7cjiBYQcUdkX3udiesuZcURV1Okc3LWc_zpsDODDgh-lmkr-LHedQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAwZiQLmYe48k-k7zVROb6BzNSihi2_nBAtlgTrD2lu8ECXMaNXyDy7jOuOBHycvQj3Xg9UZSKgN_wS65Wqko8gdjhOthvR-X3Mawlb04V3iSwova0bMqiVhvSMAWMmc9OSL737ZcnKSdvT2FlBV_1rgD3lnJkYXz4EwI4bhjAo3bgf6zpnYTZgKDzeiqB5C19jGT3R1iVcVVO5FhyqMn165_fB_JsMQ1Xd8kGhajotz0tyJ7-K9Utur-9udj9pNyrz6K09S0-92nRurelUZmEsvxTAb-C90HJCh5fRV_3V5WGUDV2YkX-Qyn0RvhIenqA2uAvzUxk92AjRyex88Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDzKRBhmmTMX4BN_xxHG-FADTZHxutDABI3a6S8PwCeqoLwaxdKGhMTLCXo4N027HzXygkawTLyZbS_he6egjEydzVYq_ZUms0TuSea_zvgS0kcGLUWFWCGV41F0e2gligWvYGHNqlDtXM2Xu7O1ZZ13pE0C_wpQvD6HY4mMutv_0sBR66_mp4MSYofJGZzbo_swZN1Cjb6s1i9ZcV-kulsTxDb8cH37EMOAKsLfDgCT4tgIpb5TMSgWDNMMUQeUw3MXWShFHnFvZGYYZuXIKaU5PJHdhp77hD19H0t55LFmMB0FhlJYR9qB8jDEgUfrBnE05HQmIG-fMtXEnziEew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGN91E3JtIERs-7ke4Ljtbn-4YqGq5b0VbOR1fAGCLDukhPHfVLIjzi85T0IWgXec8glyFENhu2Iz2HkbGM6RuVGxtRqRdSV7m2bjwJerFNPqzqwvgHN1-cbwNqRzAaRcweaWtrTd5hMqc0gKiuKFYZ36F0vqdwybm3iyHP2an8o3H7OZEe0a6xLIJbqRaJf-pzFAdyySZMZOwht7vc1_-S1HOgf0vxnT6dbQONb7dyG52443pDT8Acq35tKm2MVZ6tF4GgB6Y8XMVRlZo1tURsPR9WWmsIYnHAtkvqJpTpMxrI3bryZkKiEIboxGdku_B2axvJPFHWSAuqo4xCTzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOvu0j2TTeVvaRUpoZwzICeVeMr0Bxmzv2GMXpatMvgN-goTSasqHMDGZ2QCs5tsSu_jcDDaDFMhfRZSXY1cgs5zrVoOgvoxUAonMoeUeiOuRy5WJ-Sudwf9QTTbZvmgCKc2R1WdXmyGHh54vuSZbqpXX5QUZNq-ddhuoqtGz8U9cSy3BF5-QKNoaTiCjf1IAY99gZwcahQXXm1fH93k2LCvcHI8GgzJaKs5zflHvCTqRgtffe0TbSCBlK-EpiJklMWiX4yjbiC4_5uisawLnibdMLQ61r4-YgXL3jYOugl4tWAtTyb8yJpkAB6_QVKvSAYWagUhD14FL3XJmkxZGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQdVl6czXKbQu5igAWNRNgu84JwHEaN2E82NlbmhXZcqwA46OH59KR_gRDxB2dktWd83eh8KKD25EdtMH-wsJIZJMydbVEAJHJ9lOWVkaToL4oWXivdnWPZyokG--GaTYDiM_fIcqwg0jLqyUt_W9DBiuUXjt41T7Pl1UqPMenONfNMHDeFOrfLJj9d7tMbX1Ei3FjmSVKVGyrWoESYyKCX6xfzzqUECRiQDmAtSMcapVnsGAKMB0oKTr4AKwd847in-NEvvNP_W5806Y4d0Oi9Yiux5wSZT-Ce0Lj94OjuEgoLChH1eItQHHnHbN55EA0yvtVOMCwosUP3nJRjxYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSC7aRiQlcaXH9oehXUa2k-PX6Ki7JobYeJ1zmbL4ZFxB_4_PGzdnwaoi9JiHXqXM0XYuxZlzwKMoI-kpQpyqvJAxJkes-tFm6-kAz4QgpGmMLVYZwgaP35rtEzf9RGTTostfHwRS2LS9w7IANCSQG6oI12aawXH3KDUTG4OG_jvzlnZONMxXeliTrbmcrLwForVMss76heugkO82Gl76iTGBEcN-PAHSWRep7OztAJcUux888tB0Do-ej93J0ZioqOUfIk9UKBkulqWtqT2rcRjwjdByds6rh8OnuNDEMRkczo5o-wEMDgu5q0SB3XM5tHwPfYFev7UooMzpT0NQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC3L6aHSCxyldtevD_aIIPiiW61GFaTPw2509VRvwL0GcchgZsfqja5MQkJqcciowfaqeDa1c4GYNWsh3KVyOdGf1kCzfXc2I1AP6l42zsRHwnKkGEg4eiWOkp2ns5i8ENL5KIC7oOEptTTj6FIJxUuFtbI8LMhk_f32pCzHl-ctCY46Vg3iVKIyW5UlW3CjAOZXzv5oUNp7GlvfD3tc4F0cbyxEgrfjNuY42hWjSBAycxtbyNsGuWekuhoUS37txe6P8hoyhzXjY76WWd1-HaNj8R7q9N5bB2k8Im3EP_lvVRDe1YTioI49QFNKquz0kfJ58ZJp-09zVgJbpAmXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=S8Rn4RWWnzQJ0ZeceqE5BBZMBRaqdrIUUrWtYElGzGgdqOhKf9OSUes54bILCWLA_nf3S52pViTXsxQrviPLjBxBXe6eCSITbueCJHryDvkZx5XL5RpwNVppkcdhywYsdRRubJAimDQLnSUImxDm1yZGmUKMAcMf-oWv9buzTF-hK_H4l4M2qaFZP_oJkPongo-QD4BAQdcj5xSeG9EkM0TcdpO-S2TNCS9tVZpEsqacc02XKaKtDPIRRI6JJRmAlAar1nxPp4M7MC48aBnWyWIQTgJCS6BNK71ajSqfaIgMTVyHU16Ed_Q7dDhOln-JNxXwruSHZNU7UXtooPoZ7RBrpFMuRX6JNRA2p8BXMwl8OC08LGn_HUwz6Op4SmGDNKDuLLsBAzVCKSGk2cjNyymnX6qF0xEDazW3YhGjhc9K5PqdLfMkmXQCzKSMFnxVm8Sa0703SdaxqSVDOgCezKTeZ4DLgg4soJOv_WVIoQ-Q_1EsAB9u4U64qBni10vC945zUwKRCUz9jO55w1WMMESiUqKxaNCoSgg6ZGPuG4OEDrYoQUJxHd9h6fU4bl6JUzUeeEpexfHPjR1KLse5T8bysWu6F2E_LuntYCQZb4_6x5qL-8vqCr1qP8UzrhwlkgCsvQYLKqsZcq10FDWhCX-EV84gXak1GrH7xIkvRwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=S8Rn4RWWnzQJ0ZeceqE5BBZMBRaqdrIUUrWtYElGzGgdqOhKf9OSUes54bILCWLA_nf3S52pViTXsxQrviPLjBxBXe6eCSITbueCJHryDvkZx5XL5RpwNVppkcdhywYsdRRubJAimDQLnSUImxDm1yZGmUKMAcMf-oWv9buzTF-hK_H4l4M2qaFZP_oJkPongo-QD4BAQdcj5xSeG9EkM0TcdpO-S2TNCS9tVZpEsqacc02XKaKtDPIRRI6JJRmAlAar1nxPp4M7MC48aBnWyWIQTgJCS6BNK71ajSqfaIgMTVyHU16Ed_Q7dDhOln-JNxXwruSHZNU7UXtooPoZ7RBrpFMuRX6JNRA2p8BXMwl8OC08LGn_HUwz6Op4SmGDNKDuLLsBAzVCKSGk2cjNyymnX6qF0xEDazW3YhGjhc9K5PqdLfMkmXQCzKSMFnxVm8Sa0703SdaxqSVDOgCezKTeZ4DLgg4soJOv_WVIoQ-Q_1EsAB9u4U64qBni10vC945zUwKRCUz9jO55w1WMMESiUqKxaNCoSgg6ZGPuG4OEDrYoQUJxHd9h6fU4bl6JUzUeeEpexfHPjR1KLse5T8bysWu6F2E_LuntYCQZb4_6x5qL-8vqCr1qP8UzrhwlkgCsvQYLKqsZcq10FDWhCX-EV84gXak1GrH7xIkvRwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKFNF9MHG6Cyefm4KBtSna3Hc9MAtkKCeAbFoT6pEeOR0RpjIsEaQn2kzU618yHz_2Tu6Q4ekt3kNMwjaLYabJfMSOg7PWPG90aUqiQT720szSZQ0GE3DPbgV73UKsYQpv4_k5-H6eJLNScs2vcAdbMnjrMfj2XUWS9adLE4bYvatVZ84gM2QFBvJUcmcY8ri76-KngvmHA6_e8rjVuuR4xHxaLCHjlQA_5prql0fdpcf2AAMUBjui5eAxLbJ71yc5-lLwobjdpcpmA7EpCnJwa0ZeDGVONOWOo6HPIFuKejPO5ri1-amiURoznE_KnfL5BQEK0eUiUHrCbUU8CGsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_KdQiu9FqTY1I_-kDSVlOWjPoNLK-EFIy4Je-fj88d7vwge7N27_naImgFjdveK4YHKTZ2zq_MQ__mkHBjm1auLqe1UuMXEFxQCna5CsLEuyA6mCavlcFMGVO7CcLUtzfoXDqHNG1aqUrPjT2zIKGjag689qXOJeLiN5Yf0iVG0h9KoSzdw7i48SWEVG_-86qMfdWQl7EdFwBMjd-6C58d0x4uj9HfWAhXo4BJUFXTLXysloo_E8kRcPrQDftU_VnmaXx5Ws2npTFZGVsxMjRaK-qxpPTrpMYoBGoW4kLfNbNk8imZ8lgjaI8mm6J17r8luvTkLoe3VijuAx5aeIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W02PU0sanKFq_PyXdJtaj9u6infmu_OqX4f0Z6zK-w6Q6-bFn6nQHBW5d0yh6IAK9QUhE47g_ddESMJ-NcIBVRqDyhdOsBNdaanWR1tfrgHZl84x1uEQo-u9LSI4Sfa5MCFKdHrT17gCDASyHaTH4D20Vzfvxo6hbcS7k0SbpTHRw3PRiHWog9Ktqpsrtqai2TLpAWVkuQtSGzzVVdm5mak2HCG8s-wK23K4nvrP5o_tz_ZaMOdJxQTILncbZHAsKJWxqmUXuxKT_ZpXFMvP1x7PPKap8yaJ2TjCboqrqWmBRhpB3RKhJZfOWSLCNj29dTRlLr8PrmHwbRqffcMxwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPcW5KvrHMZbMGzjRegwJTqKcze5svIoNAsxGfVq_rvR1s8oSaEkRdVUf-dX-7DKdQVOujkaBdmunRlcw6i2JVT-HVLtrbL2V_Ub4W77iDJMCiaFVqo4OMgXmFnf4Wf1DWjwTntrsojZJWKU5WscDhK-RhqYTyDvsd5NaW3Bn5UDCVvMAtOh3i7BwG53W1iOjJj4kTtJPxf76CHuNDGfG7CsuK6reRw78X_XCmUmsVoV_OdMOtIRZkTvRBhvC_srOzhZN_K5xeeuccmbM38NMrb26h0-AotXYH4OS_zlBIFTb4HwOMC4MQwejBwfJibdjeovRhSTMFwnLqoI7aZPMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrmEaJ-wr2ICcKGYy1x-JSFxEYu_3jhVawhcpc4zX4qwiwATDFkC3VruHP0N6l7l52kerKAOB-m7mloOuiqYycQVpDqxYLf3AmNBL6vNa2JyHdul24zWBFtoFox7FDwiqfRJksozBM2ZGAXZc3FdOvx6Nd2IqwKNhXajOIn3lDhJmHZavJmh6_c1U7WNU9H4mXbtcqTmxtJv51UMby99MJK_xlBQdKRsFo2YU6dvGCwCojETBtUT-o4Geod9PfZX7TYqtd98p1szI5MRg6dIQwt5iHx_t5KQA1lWCNLZb5inRnuEkE1LMQPDCuV6JjKDfiCCh2dCeOmDQNB5KimFyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQvlPbJgeT8blmuHbFNhjS6S477OaTV8wwlcxjI8RMtz89KcSx0gaRvd976Wx7rIa8f0EUCH1GssMUjXj9t85kU6gt_fLRmoVXGd9dJX6b40qPEDiBqGlzX-8OqewGkPxo5YYXRJSESxUJCVmBo8nar-2QEHrT1O9hLnuLEiwcqUU-Z03GPRxbZltTJ7O2xeqiUiSxOODo-BMBT6ucdKXwkmwC4r4U-fmvh83tR_Ckd2SBXo230OL6aqmOTXdWSLVgfrlIjzmgYZlEMTYNFmclJ1BPgUmcONFszRUfEePpfu2mfwlBcJKgJ6E4qbQhmvFrh1O5BPhVlNtiBEOroYhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVi4eSmF504fmwPDniRTIzKCD-N4kz04gtXle8oPMvgShfZ7AK98boYYmWOLsTlueEjJdxdQvrl1KsNL_3C3ndRusW-rBJh7bEAGYpr24ue_EESNg6ueYpt3KMXvAGOrP9eEm7Z8Fj8egIkeRHxF4WeDKzn6nhuJXJ8CNVjEBAsA5MIrN2LGJRPkzB_iJcF_ZEONMvWXJcX_TWpUz0_slFlzavlNWt7Ggq9ZtU-dJ03LM4bfI47ocGyMKBCRUrpnp3qWXBl_Fq5RvHb4L9XiFjQthYdbbR_hq9RY6u0JTttU5U1s7ICLtlK8zRsXUrLFSaMgbdbeyz4UgQgPx62l7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KD7bHr3du9Ob_1tRdL8r5n9fHYKxQCrrtZ7T6ff3Drbn69TJrpD2N3PMFOw9IG4HX8lWxn3k2J54EGjRLqgQbUrFc0t8Juh10khsO-WlsSJlUUbyVdoYAdTBa88OjqrN8uoz-f-Yd_SumhdaZax8ntKz1Ivvpy_Sq9fpXJvEUCG_i5S83aqZvfuomB87bkU2TKLBL9rtwURZv0KdWUKXycIIlqyjwJbrgPVSA7mEEjAiWKox0dYhuyagSJzdoUttyDGIt__tLP6VzxnmInc1CioUaqFh4Ia1YE3D4lMCnDzEn_5WZZyBFqHF7Hdh3gzhNmfV1Z0kdfRFhrV6-q0cyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQFXbjL3BdUl4-_43u_cpMdJHflJBgWbJbXsh5cEJzaDm17LcSqMfKpO5y1OxMu5hK2ER3xfUQmI3TRuJGBZuC_3Ln4rMdDnOLJTuQTvMprxOchUR2hTpbu-ON-9AvVg_Ti4cSOubW2IKYNJy-lrZnYvkBTg46DBKkVTvpWfAXuKGm66mEBqolRs4_i1W_ZhHFIjYTIKhhD76k8R6DsuL72hk6pi1cU8ovjW1JqIQXIhp7xTCL8zH2NrzWgRfSb4FXVOLgTAwOVzA5WLMuNVchzmSGcXMjkMMRL4NTEmyOPOoYLIIoUON9wxbkVNv1ZZQGD8pQgXrZi7Varl3J8qPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP_UHloyrnxlGaL8LnKzoFhHvwaAix8D814zolb5F4jXkovRSPrpMpLpABl3mU4BCM7I1fEGUpJ2DvLn_vyEfoiPEnHCsGsda8PmzsuVj38J1zrEeYYnGfgfZNGVm3VbAPNSyCR7u5rTkPxDUkFWRzrlsTQsYS8OFlmIX_fk4QHYWs_loYSdc8YKlMn34MjcBNyCJp4eIJpX1cRlcsdKxcC6IdQ0sAHKpUrTeXRA8j52o33Hzmq9BRM0qKN1PdBbWH383LlCtyhuS0ZctmOGFQ_XUxFqn4clT9DZiHhg7gTzGCSiwd_rHYDMqYAPL6YF_wRu6mXkCrbAKN9pZzwm3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=sFdR87VQikRMvqNT3lVn5IkzD0EcfKJkkcAwMtLZmI1j-__S5ikq1RTHIRQztXty27qT2di3hA94GfME8EypLLoVXlj_utQjaqmyyss9lH0CTju5JPz5ObrbgVY0oNFOXcMVOj9t7j3t1TDPQeP4nTCJAkuOxDpZ1ofslc2CiNB6nbVV4QBXxI6EGD5iRANez5JuiReT9yRdrOGzNw-BFDJqY38qsZBeYYhd7oHEDLShjGVit68noLT7021zcgf8Gja-kvq0d7NFbyu4szLNPfn7wArRl2UbyKNx6sEz25nFnKmxQQxDC3wHR0f5rGYAkoN8WFCf6ABsYZRqXKkoxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=sFdR87VQikRMvqNT3lVn5IkzD0EcfKJkkcAwMtLZmI1j-__S5ikq1RTHIRQztXty27qT2di3hA94GfME8EypLLoVXlj_utQjaqmyyss9lH0CTju5JPz5ObrbgVY0oNFOXcMVOj9t7j3t1TDPQeP4nTCJAkuOxDpZ1ofslc2CiNB6nbVV4QBXxI6EGD5iRANez5JuiReT9yRdrOGzNw-BFDJqY38qsZBeYYhd7oHEDLShjGVit68noLT7021zcgf8Gja-kvq0d7NFbyu4szLNPfn7wArRl2UbyKNx6sEz25nFnKmxQQxDC3wHR0f5rGYAkoN8WFCf6ABsYZRqXKkoxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=UO0qH9xZ-ih460MvEunt0-JkYvYX35UvbBGywqLxdWAk9xQ2mbkhqaOcdwCE43GmZrhJC2QICrh52Srw9cZhlfT6ew6-OjOTuM9uzJiPSSALKBcexmoXHgXzhxdXnvt6BJ3QPiwlF39pBi24zoRib1w0lYByLbDRB-P7U_QXms8JNkIzRfQ3h856PaPlgLMUuv9bnP-knZ89Xor9uHTD7LS5R6gB32Xa2DpsAsAjjxD0aAP2ZKirpJhXsFQGWBL-IpLFu2e2whu7JxcpOMauGJ3JREobKIgUEdFPpAFjIza8vT8a0tDnk7_H6PzUTklcmX6bqu0TUrj9VN9mk4tAog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=UO0qH9xZ-ih460MvEunt0-JkYvYX35UvbBGywqLxdWAk9xQ2mbkhqaOcdwCE43GmZrhJC2QICrh52Srw9cZhlfT6ew6-OjOTuM9uzJiPSSALKBcexmoXHgXzhxdXnvt6BJ3QPiwlF39pBi24zoRib1w0lYByLbDRB-P7U_QXms8JNkIzRfQ3h856PaPlgLMUuv9bnP-knZ89Xor9uHTD7LS5R6gB32Xa2DpsAsAjjxD0aAP2ZKirpJhXsFQGWBL-IpLFu2e2whu7JxcpOMauGJ3JREobKIgUEdFPpAFjIza8vT8a0tDnk7_H6PzUTklcmX6bqu0TUrj9VN9mk4tAog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO5L7EvZvWoD9NdSwJwix1j_EDlijrs8xgx8p7pN8inu20velQo1vUwWWuuN-hoDbVcUuTQ7oCjl8DlaHyjJeRY6ljrZX14Y3owYj9mfxbkwU0yhP3nkjmYNGbVMKwHKauslVtUFgmBY5He-wvC8-w61HBjvtfFI1c3IhaM4hkKySuRJUAcBJhsJoCzH-wLNhVAGNKW1jvOSpWUGfpLBmR--VxwnGkRxq4mgmSYg_wLnHLRLep_Wjme9W6KHxfOmLGjRwU2wUcinaL-xg_p2CLDzn-G9mT39z_jSZlkJ-sJ_AQueB4k1uhazJTWKaIRc9BnGn3otTta1DUp3YCy08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2LvdGCHd1_Hn9Zt7cxooonI6wUebTlmJp2vPBaNlzj3gXgSd0LtyUpNLoyHMjhVvl1KduI1uQd6B4wMcEk0NQGqMJXfORF7xjmJlSplZ2U05VpXzETVVcO1okBCbOUNodZqtxHwTfl769KGwpQvqBOVHNpFBKWRajN9yOrCUMvE_n6Abs4NIt3ryoYjgX53a-ouj8jbtzAbMHkb5_7arHa9U0HRVAdoVjQYDkou_DivH48Zw09nGytiIAoF8e6V8oL_UpXjNRmfhUf52LoHWOFt2eJJL-4Ur327y8fwCCOlShR7FVyrApreGmJQ8C_v9akjcjJxRmJpMFG02apwG_Gc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2LvdGCHd1_Hn9Zt7cxooonI6wUebTlmJp2vPBaNlzj3gXgSd0LtyUpNLoyHMjhVvl1KduI1uQd6B4wMcEk0NQGqMJXfORF7xjmJlSplZ2U05VpXzETVVcO1okBCbOUNodZqtxHwTfl769KGwpQvqBOVHNpFBKWRajN9yOrCUMvE_n6Abs4NIt3ryoYjgX53a-ouj8jbtzAbMHkb5_7arHa9U0HRVAdoVjQYDkou_DivH48Zw09nGytiIAoF8e6V8oL_UpXjNRmfhUf52LoHWOFt2eJJL-4Ur327y8fwCCOlShR7FVyrApreGmJQ8C_v9akjcjJxRmJpMFG02apwG_Gc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbpzB2k1v5gS15iMB3MNRha19o_Tkz6vEU3V-AimMP2xEGubc8wn7Q4DzE5zPFhSX8yGRGikfuASZlb8JjopfRUDNkz2vKqqNaCOv0yWAfnq0puFizbVbd9H-mA4Tpa0syXYsK3xREuNbjmRPRqec1xHSc-Xy5EGFw_5aE0PHP6GFAdFAmC72HL8HQ6pVcGdtQPuRf7EQgNdxfQqs2Y-ip5vlw2Lh2ETpPzAnKubwe1nObslc3xzCmiJ8bVB-nWVl9aeDanmbHf5YWkKhTpe1cStQmnCAIHAJXTg8-orBNn9dA3OCTu3Fconi2A9LfZYvGQ7H40zRxh_aMmhfrV_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHBiLGZHFW7y2zpy4kH-CJFE7V1UCl6I61aY_WdiJCQDR_kcPqmCEdYXs59KiEwyoqoQPcMPW7GeGzz3d984Xs04cG-pphcnVaoPG7NWe6PeworgWnhKoCtgGS3brVK8Nr32BjMRUhFmwk8fLwMh_1WXI7Nvelbn1qCuON8MV403ff1rxcrtA1s61cUUY3gMruJM_fyA0sN-MtrQCQpS-mlw0P0bJAfu4tPfduBxJXkgFrMh03uQmVi1tb2X51WUHUHRqB6mhGvBrYcGHy653peJb97JBVd9LtiIyZUBT5FNaHlDttqustcc8j2GfTWQPbJ1ukPvc4Smn7hO6n_mQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtA99HIDoiEdQsdM84B1kUEYGRK4vbLKf9yF3GjcKp-qqOiL0_jZ9FGo-Lg7uZNU_hlkrrq9t_ZOzN4I4xpspITq-wEBGvd7cagg9pjca_m-y99rT6Y5SmM_ljRBi-mZUbGL5dcrH-R8DcrE_OR2-k_OZuGIKOs6ZXRjOqQac6KaqSmPLEO1BwHbKtFnklO2qbPZCY6KoxXBDegac8cmjzF-UVlpFSrIwHF8ioueEoLwTvQGJEfQwOl_Q-0OgsmZgn-B1OKnR33Vg9cj1bQL8-kLAkNHaN2J3BP-ZbLtqBd9RoRxnKidRCn1o7Ne02gO9I1wd98q0FlYzBv0lq8aaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها: •
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه •
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان •
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب •
📝
فقط پرامپت بنویسید…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKbB33mKccqnSK7wMYp3Zq6CwaysIf4QPK3uH8PvXajMatOzZVGPGE8_QugZp88-zG9cP61dV7YGx2Ufw4PeiskqX-w-lu1Y3P2avNH1MadA7q1tB6yWq7Y9Bb-82OcxTEvH9RqSAlW4T-inrl7owpwGJPFGup9wx_bAlm_4FXwwc_RRpLzTXj0CyJG7Luhw-xfJe-dHOitNRJjKXFPqwcHPUtwKCWdlkCDSUUJSKBeEZdFh2guWLVPem-0bHyyRhSw6uy4h8EDZkuOon3136ha_qsStyFnPwpH3fHDF9zYVPRhYBTpaa6ESIQbVDQoXRXFCOeXdNhkI-REog91AEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrS-r8SrpuXESxLU5VIwPZdkkjpXm0ZF90QceQ3GSYNBmk4O57X6NwTHjsW-9YRryvglurks6lSQZoy46Mr0sOb8JFP5IHq0M_UeRjH1sqCzj5zWgvTmzowVKU_eXOLW2KHHmvfdwlQvlmxKYY9KWQ-Flfq27dYhpTR1tKrap4EKg6pZ8qTlCgrNRx4AOUgro7TXZDgC2bxuPq3dnPNWMudt8PNEAKhxeeynMg4vSUARQamhQd9ilcX7ZoKuyEOZX12rvYtPWu4Cs6iZG0ho4sN8H4AksY29niV4bpARIDfnjlbdleNKlyFnb5VIKSV0jYxjJ--GK71iijRv4cmK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
فرصت طلایی: ساخت ویدیو با هوش مصنوعی گوگل
🔥
‏گوگل تا تاریخ ۱۴ مرداد ۱۴۰۵، امکان ساخت ۱۰ ویدیو با کیفیت بالا رو برای همه فراهم کرده
🎥
‏
✨
ویژگی‌های کلیدی:
‏
🔹
تولید هوشمند:
تبدیل متن به ویدیو در چند ثانیه.
‏
🔹
ویرایش منعطف:
امکان تغییر و اصلاح ویدیوهای ساخته‌شده.
‏
🔹
قابلیت ‌Remix⁩:
بازسازی و تغییر سبک ویدیوهای موجود.
‏
🔹
رابط کاربری ساده:
دسترسی راحت از طریق منوی ‌Tools⁩ در ‌Gemini⁩.
‏
⏳
زمان محدود:
فقط تا ۴ آگوست ۲۰۲۶ (۱۴ مرداد) فرصت دارید از این قابلیت استفاده کنید.
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at7BOyHiLqjapkYNPRJaIVJdfdiuHBMLBRwpLiVOGh20vooD7kbILkBlQGICUwN9cPD6Zo6YeheTyRfQ9Pef_MzsMfqrt7SKyJQzg5yAr9iiPKtuGeIZbdvQY7ZuoSM4iTvMP6OnWAaTpv5UEHPrgRpSYkNYmt7W9yVmICSklDZHzmrryqt2q7Gxax2Dm661XteaERhC0a-RDecY-YFvgElxMYhfFZNinuLoZvd3PgV45IEzLXr3A62t5dT090DGYykZqCekdpLbw-TyALyk8wngATlBde5f3DMXx8Q9OrplGwC-vJNQeDj6mXc9EWHD0EbZGJlQM-b5wMPzdszFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API مدل Deepseek 4 flash 0731 به صورت رایگان
🚀
وارد این
سایت
بشید و یک حساب بسازید سپس به این
بخش
بروید و یک کلید بسازید
✨
محدودیت:
هر ۵ ساعت ۵۰۰ ریکوئست
‼️
قابل استفاده در
Vega Agent
☑️
Base url:
https://api.p0.systems/api/agents/v1
Model:
deepseek-v4-flash-073
1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cohef4DUzouaOxqeemEfkaZsgWklINPXiz9jR3Qp5K9vk1b8MNffQcBRs3lyIyufl-N9ROcP04PBXqxFQ-kH7eIHUvavzA36J5R_Pf64sLp3jHV94AcO3-HVcnal2IesjuZKEVY4rudLAQaDDt2-went0cioVeElVhG2GhEAKA1ZnI7n4EXksRDF4EO5J2Mk0xDZ1YmAHr011ROBzwpfnJl4lBSFV_RG4OC2LM3kFneW25w9vVWIryUvj_MnKjHzq4oEZkB8H3_Jpr1oYAsOvLpRg_XTNutx88ZkVVWXFYcFff8XxoI-C5U1OcMQkTk1xtpnMs5HeQo-l1kDBQS4SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر خودکار و مداوم IP در لینوکس با IP Changer
🔄
🛡️
اگه برای کارهایی مثل تست نفوذ، دور زدن محدودیت‌ها یا وب‌اسکریپینگ (Web Scraping) نیاز دارید که آی‌پی شما به‌صورت خودکار و مداوم عوض بشه، پروژه متن‌باز
ip-changer
ابزار فوق‌العاده کاربردی و ساده‌ای برای لینوکسه.
✨
ویژگی‌های این ابزار:
🔹
تغییر خودکار آی‌پی:
تو بازه‌های زمانی که خودتون براش مشخص می‌کنید، IP سیستم رو از طریق شبکه امن Tor تغییر می‌ده (Rotate می‌کنه).
🔹
سازگاری بالا:
روی اکثر توزیع‌های معروف لینوکس (مثل کالی لینوکس، اوبونتو، آرچ، دبیان، فدورا و پاروت) به‌خوبی کار می‌کنه.
🔹
دو حالت اجرا:
می‌تونید بدون نصب و فقط با اجرای اسکریپت ازش استفاده کنید، یا اینکه با نصبش (توسط فایل setup) اون رو تبدیل به یه سرویس پس‌زمینه کنید تا همیشه فعال باشه.
⚠️
نکات مهم:
* برای اجرای این اسکریپت باید پکیج‌های
tor
،
curl
،
xxd
و
fq
روی سیستم نصب باشن.
* از اونجایی که ترافیک از شبکه Tor عبور می‌کنه، ممکنه سرعت اینترنت کمی افت کنه و بعضی سایت‌ها آی‌پی‌های خروجی تور رو مسدود کرده باشن.
📌
لینک مخزن گیت‌هاب و آموزش نصب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r29TUmeh2QJSc292I8VxdOavS0T6lh5GLvd5gNMZ9slOKCsEmfkLuCcBxZjOTl8iAI9pwMh3J69AoSyyJD5Yp44qbesigXNRsXI5kwiQkXGacmGP73JS5JotvZDXaQZgwxEgHcPiB2VPN1Zv-XQfGJlMgxZFOna24NmSbRzXllyWl3i-RhvCPgUXgPRZy_owFzhG5g2XnSxxA8rtCP83DyNA48sRcGFpKYMrwxrD1VEHAahMsxomvcM_kR8IC71zI2SAVa7j32gCmG3Pq_s0-kwaeqbeAyusESG_E9uR6Z8rvUP0dxmaU3ypLhNNfuPvydI_Bn5i7wRAdExrfKaEZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Deepseek 4 flash تا 12 آگوست رایگان شد
🚀
میتوانید کلید مدل رو از این
سایت
دریافت کنید تا
12
آگوست بدونه هیچ محدودیتی قابل استفاده هست
⚡️
قابل استفاده در
Vega Agent
☑️
Base url:
https://model.inferx.net/endpoints/v1
Model :
deepseek-v4-flash
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AffNINX7XYicAijiPVMN6hVayK8arWn_TjLkJSvI95Q4U3t-XTBXaC1bizp76OtdFHwThdzkDy5rZwTsGcYqmrlu0cWIUAt2vRelz0l2QMLovfINFyfGJtq4_k7AScSwoQZrP1TWGLW4RwSwilR0QFujgCWsGqvHQIMbBuA0ydsyAS_7cSP_BcK7DV6MMaHoNL4aIXeL43X1drf573TKqJVcmPPqGJlvepeCdKMyBj1cZv3nnGEc5iC4Jx1gIPws0qTpMVXbGXfAAVyp50RIiD5fU9Nuy74xcYabiqpYVKBk3Y1Hp8xJEP_L7memUCdf6Eud6NyKak9XUITGkC0Qlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان
Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید و سپس لینک ربات تلگرامی ایی که میده رو استارت بزنید برای وریفای
✅
5
دلار اعتبار برای مدل های پولی
☑️
قابل استفاده در
Vega Agent
☑️
روزانه
5
میلیون توکن رایگان
☑️
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
