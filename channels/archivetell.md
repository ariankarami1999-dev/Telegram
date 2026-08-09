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
<img src="https://cdn4.telesco.pe/file/TRKzmWwH2Iys8N1LVOLYb_qkl1XOVNkN5BnCRsourlFuCOFVyHiUJEy0b8U5YI-u-KBJhKQBouch5XwndF4baw4xAR24KHLnooJF-1QBLSFu-MQgBvODSagR58FehTXqdDh_7nor1ofsvlQAPfe8zz9mYygiGQ0WLtqdO2ndVhiDDvs-0_el-lH9gnEEnKQhyS6ZZoB4XusEcLSjL7IwocmC1Vzwpo3o8zcfIfTHkoStdBkpaPGpOzLhjhGBMP5kQWLvLWeWn5KJ9h96knuR6FuEnpb5b8HkKLlcLOygSVshoixpaFGoGU2OwvveIxNl1h0yl4-bsU92XM1tyezNgg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 23:51:06</div>
<hr>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جزوه ساز پرومکس
⚡️
از این بعد لازم نیس سر کلاس چیزی بنویسی، فق کافیه فایل صوتی کلاسو بدی اینجا و  با کیفیت ترین جزوه ممکن رو تحویل بگیری!
https://github.com/faithsaly5-stack/Study-Note-Maker
تست کنین نظرتونو بگین
❤️
⚡️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 619 · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7451">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7451" target="_blank">📅 21:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToEzh1p4yxzlokv8tZCy3EqgRIDyMBZtzcI-2vCE3lnYJz-sHt0i31GWZOuz7GOEb4ydOo52kFx04kDSkfavvClcftBRHA4bax-daE2ja2CbfEIioqb873rWccH03so6o7iURp4OUGiVLLUti7r6JRFAt9-NcI602oRcjf-LRx-rmWY74B6Kcl3F3xk2dGcCkLJn664JrlAx9vDFMJyPCfcoRU8WXCrCz3YsVTtGlMKK-hLwvL8F8sDF6eaez65NRENg_9d6GugVDwT93Cxij8pVHpz3nsmpYBN3eTRsTo2ni9joImUMN3sZNEQU01PQK_HrSjWtdfozx7Ow_BbQXg.jpg" alt="photo" loading="lazy"/></div>
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
| VeGaS</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5UN55lKa2WwO6pgjX6x0Phb8QwCqe9M19JQe8EneaqcskgjsPD5R_yWr7rV9wwl0RsVW7q3nhV5cUT6JmWBsBrnkuDGU5k3p67Dkt5V1nIKqkLmZGEmL5_4Dd2_tlcKik3o674VVi7ekC0pw__FRDyTr_cihdJAHjPljGaT4FJ8D8Tys9uPlj3Hna8jUg3L89NZxXH0Gi0hYh7F0KtJFRvbqZjKUM5fZF9jSHFltOPO7H2nzpgCwmVd_cf7OrYagVTi0BF8GkffoAdt1XNvZmc4lbCoNrlCg2K1fgVF7mr8w-h9vyJrVOaHbEAkfSeoZgsf2oiFZJEdVjqQ-YF-Hg.jpg" alt="photo" loading="lazy"/></div>
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
| VeGaS</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpFIyL_Of2wPn0089cM2Iewgcz5QLZY_wiUyyGtJ91gm8wjXkKqPYdEKMTjTtXADrUF_kGNZiQrwDOeXmU1ZxBLDEnuUaHXfW4xZWF7dqzboBmQzfPxXP3DN_nR5xWGTAcjYJjQev3fRNtSPjEfmiuZUzAVh3yQcnVip4Nep4bJuTa-5DS02b30ceeYoOQm4F_yG4pixjnDdja0VK0vvJXbHbwqOjCwJZIBitItAhhn3JQcWzpEE0bJVjCHd3DBCBjzUoT300Bhc19tyWC4nKGqgONSXyOwl0oWLUfgaoFe9wpzzefT5hRyGbeepm9FEgs84hpbRc3XmPLcGmzgUcw.jpg" alt="photo" loading="lazy"/></div>
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
| VeGaS</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddH5ynnAIZafFC-Nvaou9gaf26CB8asuqtOYP9YNiBac_kbUsiTVVrCYZjFUQeW3vWdD1xvNKmdDG7-e2apmuxfHmU1s11F5am5MsUGsiwd3AeND-XS4Ldi5t6hhJiPmZV7nHunvcgnO3o0LxQOSfnAdMG05bPBROjHso8Fi6pwnWHlmAdskRVM6JCVcdCmTpHLa_hEB8BsUIvnrl5gD5j-6iY-ToJ6GBbtGg9rvk3RNcXRrqHtpqe4RHQbfZB7OA-cQXf7Pi0iru0en3jQQGNiPKXuv232K_8p8YepZG6tB5geLrXRzUCmlFyJC9JJD7qcL0t3SBWHEBQ5YEgUBKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=dmdKOAqjVmoLov7KnpTNQ07XRVxb1mMZMsaB3mpeY_ZcDm1h2rhLYO1M8EzEGkmg9ZKoi65vZ3SmlZ3rm0kMbGjLEJyFOQF-yKujEV7atRif2zTORox--n8W4XHtP2a-BVo-ATKkLKKnAuQCTMmyiUAzeTy3zjyxlKaCMIgjnr52POUJSchV4rUSAIaa9cWHM1N0oaE-rGzpOjL3XTtsbSPjeBELzYq5HbJn9T-eHBtFu4OJH0q8UkBjwjZTWMKgP8GCNUFZu_d2eu3beCpMmmrtccr9QL0WK2mtNKG1TR1KFnaZI5kjP7d0eAAA5-mhwEqKBN31d7ackByLMkOY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=dmdKOAqjVmoLov7KnpTNQ07XRVxb1mMZMsaB3mpeY_ZcDm1h2rhLYO1M8EzEGkmg9ZKoi65vZ3SmlZ3rm0kMbGjLEJyFOQF-yKujEV7atRif2zTORox--n8W4XHtP2a-BVo-ATKkLKKnAuQCTMmyiUAzeTy3zjyxlKaCMIgjnr52POUJSchV4rUSAIaa9cWHM1N0oaE-rGzpOjL3XTtsbSPjeBELzYq5HbJn9T-eHBtFu4OJH0q8UkBjwjZTWMKgP8GCNUFZu_d2eu3beCpMmmrtccr9QL0WK2mtNKG1TR1KFnaZI5kjP7d0eAAA5-mhwEqKBN31d7ackByLMkOY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYLzlijmZ8tFZQCCjJ4mbBDbeXxBeyRMcln4NNEA7vEYEKOj3X5D_ouR3Duib3nw4ObGqYmMZD9nrYRZhSwZcJH8SSvDPNG_7zmgVjnEeJ3fnuNd2IYS466hIasOUtOBgWkHvrhQSwgUYkxZtJPt3MCmdPX0ILg7KwVWixuPSY55m9z-pjmpkyfLY2EfdI9zl7ElCw7CvSB1l2yspI_pXWW8tdmPx_KaWNSST1jsXBr0qEgid5RRjqm7lfUsiO-g1k9m_uMtTIjG2hgHnKEHf1gx0Lg4-0w6nAlNLZEEa2iHOuX4eyi7PXSDMa7vCyXR9-LnufRoVu4CUianjHIwaw.jpg" alt="photo" loading="lazy"/></div>
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
| VeGaS</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=tKE5nfTY4vpiWaN-WNwB5Wz0i8fbMtd2io9VtfPJn4q3yBA0OG6GUieXe8YpCY_vsyEhZDsKPIBbgJaOdKA02LJksMsQOTynXjiwG81p2a0TSZZoPtVrTJDLVH5bhqAu_AfFLe-xJJHk2dccQZw-XBaKAawv6VRgwjcCBGC04vYvRrJlgqRgoyjT7Zb8snsXk0w1AdfUegnB1BY3CbTHZraQf6Dzwb1wF-7LUGiDleeJV3qq6gYQ6rRLtud_93n64Y2HGSYSxoRjg6V54r37RpRZGOC0YW8CuES-HZfNjH-1twRR4GyAihod3U1FX6nd9i3u7lxezPwT7hmarc64Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=tKE5nfTY4vpiWaN-WNwB5Wz0i8fbMtd2io9VtfPJn4q3yBA0OG6GUieXe8YpCY_vsyEhZDsKPIBbgJaOdKA02LJksMsQOTynXjiwG81p2a0TSZZoPtVrTJDLVH5bhqAu_AfFLe-xJJHk2dccQZw-XBaKAawv6VRgwjcCBGC04vYvRrJlgqRgoyjT7Zb8snsXk0w1AdfUegnB1BY3CbTHZraQf6Dzwb1wF-7LUGiDleeJV3qq6gYQ6rRLtud_93n64Y2HGSYSxoRjg6V54r37RpRZGOC0YW8CuES-HZfNjH-1twRR4GyAihod3U1FX6nd9i3u7lxezPwT7hmarc64Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG_D_WQoVMh0Zcf6KPsJXZVuw2GM3_xvj32bhsro11bDNruZMk9Q5fmPAd2x0cGrzrw-6UkfE9aSxnXw3QDMCmRBFT3u-TKwYgi8OpMzuVD_UPlOh_bG98t_lpSpP4Dk1eYZ0paCZJDzHEPaIRWOR4pPQcbimses54muOn6PqhIQgnLN1JSyMBJxqHmVErs0XaZzghy-aAAqTKYhiuqadv2SBGl4lGEO_ZfAhIU-YF9FdCuSf31HxCTHCitKUXu5kxZ3csOxh7n9coe4HE0tOzPEqb5HICaSAkwFK8Iyr5hddNuqKr8imgS0w8QMiVWEd2pq2545v_NBInRyhGvYOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXzhxEVRvPnbVybuH6I1vx-L7wmd7xZPTpEzfk4VLCO3exNPPgzD2XeIf6_XOWsbHQgth_ZAVX32XyslRBTr904CJILVm73ZT6tNtjYJplrKTUVrwhEea0KhN8HFQvI2OIa6tmAVKVHjBMOtpONqr3tPttqA26rUEjWIMZ_HkrkM8q8fiBSdci7fyNB8YVkIFCwQut_kOgCQ5cz-QWe6Yjkd0M5WcD6oOlkFoWg_nPd2qrDbvNUbBO9Ck-5q4M0kzXH6icgB35IRW5tMjR-vQ8UaGN15BHlxXYUeAUGj3_4tmZBv4DkVFyWM7yohH_6iGwSeA2eVb8-IVFstK4b-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPT08iNqJey0XA5rQ2RY5dGJIiv6lkN0hfA1r-9t7_FZBXvzfj991_6-tD1hzIoXCUkSNzQHGioVcnSzgAZuu1LoyVL9eKyBLNj4-0dIqCTDP36gJesx-k7ZdGJigFhYupHoZzgLd7YG6zIdfpvQrpTyBO1MM1ECMJiLQ_ohydc29VDgRxMYSq4FvYBE6rVwAn64IPnqZZMWw9NkVc-RWUiFGLC-USgbuNZ9u2j9CbVxQPvhnp20PUSy4Yqma9dblKNr6HtIrQnQNrmws2KdHjv5GHku2mSB0UBUyP0qGzx0-dMlEC26aXPx7n_vLYJhJf_S9IjppQiaLauasbPKJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=GfKiYLsh8wQQE7xy_o2yOAGMcIKIkWK5F-J87KdtGflmAMZ0JqiQrRaafych9R8YOW95neFtYUNKN5-FA0wTIm181KpHHzaf8NWgCyuyhCURJAs5vm-9OffZnLF4txkhzL8bVP6_vUOuHm-KLBq8-H5u7stg4Wr5nXvSxyMEo2o1g2oHg7Pry8uBfIGjQU3ZuYWLz-9_W0k0Ba2g3WeRGN0I9T2y0D2RPPL7x53bNw5fDm8VtSwew5_pusfQIjPAjkB3C0p6FhSzvs3vkjUfrci2hfs1dbMxhQaWGQ-Og0CXhD0m7RufDtaS5xJ0_ninpS5qAIl4mvjoQLQKZ2kvdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=GfKiYLsh8wQQE7xy_o2yOAGMcIKIkWK5F-J87KdtGflmAMZ0JqiQrRaafych9R8YOW95neFtYUNKN5-FA0wTIm181KpHHzaf8NWgCyuyhCURJAs5vm-9OffZnLF4txkhzL8bVP6_vUOuHm-KLBq8-H5u7stg4Wr5nXvSxyMEo2o1g2oHg7Pry8uBfIGjQU3ZuYWLz-9_W0k0Ba2g3WeRGN0I9T2y0D2RPPL7x53bNw5fDm8VtSwew5_pusfQIjPAjkB3C0p6FhSzvs3vkjUfrci2hfs1dbMxhQaWGQ-Og0CXhD0m7RufDtaS5xJ0_ninpS5qAIl4mvjoQLQKZ2kvdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAtST9sezIxl8_9yHrwF0P7PORejyjd267MzNeicLMAr6GXDPin_-VDMNjrO8v74qtr7jePJy3bLgS1AFrrkiPNIDY_4hlHmPPl8crxxJlU5QOVstNMZMS0GVRtLqaDw6gy9T6aPvqH1CidGRIXz1828ZR20IcmjOH8ak-XUCbOaDBzQ-Y1fyl3vqlNRF7tfCISfIlC1EKqoSguwkkJlQ4cfVoRQgPT4zDRkOyh_efSydH_ALaz3WSLJ_Om36xBV8Lq49cdYfR7q3fIqQ3lf7nRAiM-aVmc0Mp_RY0-aAklCp1GLfrP9KL3tlYyjRUvbeqO2xRaQ9PkQ1k53mkk5CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7425">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔗
📥
دانلودیار؛ ربات تلگرامی دانلود از اینستاگرام و یوتیوب
فقط لینک پست، ریلز، Shorts یا ویدیوی یوتیوب رو بفرست و دانلودش کن
✅
🔹
دانلود پست و ریلز اینستاگرام
🔹
دانلود پست‌های چنداسلایدی
🔹
دانلود ویدیو و Shorts یوتیوب
🔹
انتخاب کیفیت دانلود
🔹
ساده، سریع و بدون دردسر
همین الان امتحانش کن
👇
@DownloadYaarBot</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7425" target="_blank">📅 22:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cj5yxs99K2RKtQe9NkFvC4mWb7iE4fRbzkBchL36CakqunZcihDUohhUPcscrhoxyECxWxGmfh_G6IoV4dJ_4rTrKe4exK0sMbIoAetB5hmWtE8eWHowctdH6KBmdvgbT5Vn2I38Etp0vAESWyMbSrs3ktRDzAA1ssNBKRrzA4DmJHcBthfVMfe6Rf0LDnPPDsmVZkcJ05dlQJme_zAYRTOVyGyU1xpyG_MsrcjdOkzajn-xRBCuPbCkHntmCNeKYE9_yx8QajY6Ow6RcY7W0sIvUmGnpMAOKGect-nWHNuRXUBgAIDWEwdJdrHmrXyHhH-jw2VbscNY5sdqbsTM9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByVTLHUpm-Ybwt6oNYfFXVyPXetndKpf51XkpN0XsOffI9ZvazqDfAaAEgZrRabtYWDIrlp9059Ayu6K6bwIaB-U52zptNN6IW0NL7o0g55nbXBysv2GozD6V8n6NEOC8Ykapw0NmjnmyTX41FZm0qH4T_QhipTw7wLmgv7ivzu-NmwNQsSIBqCtSw1lRplYwXGbLTaQ4E7gOTuTuRXmyGi7ycWly3nnbFt9F3fWjT_-upe5QYt0BBqxstwAs9URqECZ4ijJdDsKjAxE5QPvNH6yqKrlDLm5SNEZvUPdIyqyijm7E89kwpzlrnirTVE3exeMSnVu15PGIqTFQzpvVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETQ0m9WqJu703PNRXxASCvaEH4g0scMUrAM1DLp_sDnkq0DWsExfyiHUb-e93NLPfU2z6UCkN-QCvHNQ5S7aGh2h-NSin8tlPcz_yhaICFgVr6ldp2r8ejwFOUjbfQIQ3sp0D36-WIcckF5vwSaZj_jmBXx7a0UJGmsphE9jPf0I18pZUsPWnu72TtvRt5AyomInVXy1qRTRA5aRLZ-xLjKz11efYJvwQebRCYXYUFMry0v1tdHUDPX_QfeeFVB5vmFTKYQ2j3uEpBkiuMOzIRQVu6Ml7b8NhhZWvdutmSATcubeyJwIsgtN-5Wb1mNu-NGm8_id5F-O3KYniXwlZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQwYM0w69wCjdrbdQzxs-PCwcKfYjfFW7dBnZqAZ8Hq--OVQ5iQCt3B0T600b3Ao_7LxZ_M2NF7J-ohUFJE5-Sy_6WVth8-M6AxGOPsJe4wX19gKb0tFc2dzzPTowvEu3LIUfvBkdPAexfqQGpRMPq9S5Fzq_kx_Z92pmWlu1Not0OpIVNRWZqPz032OWmTckVm3Yu1N4k92eJbedSwd-xLbmuv4jtkHriH9BQ9x-Ww4SufokAyySmAqviWZC8V8rwIGgrV3-5UVA7lyeVbawnNZWgmF1GJWfl1AJIwoBtry9THpEleU3WQI9BNoT04v4twDKV2t2byaHKq6rWuMSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S34Z3jH89AG48PVlr2gCwRW1u3SKkR_rzO99N0AXZ2ARO9lbXq3XIJH-lfHPlPb1ZnJ97yimRo0BsmRbBWmoHwKKvIug4YruossidvHiNirk6mkywBGT9GMSHAesI0lcz05yNMfa54XV2YuFvzyw6N2_UAa5DYLWfD5RVmwTP_vShHC3DIZRDgpF6y9XiJr5Lx3H5Y764jdD4LEFZ_bxMrMTIlEsXhNaB9UQqK_gamg_mMYmeM-9SV9IUHyDUw109kOoqWZGjaPMeQ5Go9IE0ad3VFVYSPXvxa37iSf1YNSWGHOwgor2wKqjkGdlI4JzCATm2O3Jnt-qf3lTLjRKUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN1MNuXnNttTQL88KZga9ZshhI7QYREaQxw41cmw2H5zbeSHRVznmctwBCTf02HiMqhmzE162ES4R99bkJL_fjXmjd8s3ujlDtsefsL5u8t-UEuMBbtlTOKDknWFqo9QmxZr_B-X_HA_X1UcbmDQyySTKJuoRFtLWHn3eeZbakO800rNXz-bdNDByqbPxY8YEg2ebW8MeymahJw79liwWj3HvACRL1VGbhQCR3CkuSivFGQr0plYaUzbdwo8LJ1ADGvfFrXmd1_dh9y7viCLECjor9Gg9JxI6jNLlEDdD8DVoaldiPLv_5kzjkuhTHB5gcpgoCRk3J79AiY19zR0ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVisvt-5NhB7AF77oEN29ZrghpWRppn_c9X2m7_prskHN6llJdQJLqYhMrSad1koteNj9Somvb2m1yl03OyaMH1X47OfWTRMxSP5WQgph27oKwtpdpJa6kEqkKcQTiH_-8lyVP0svRVyv2Vdn_eZ3RCWWaqWtI2G3lk2HhckFXUIB3QEEFFBp2crbrvBbP7_zWUutN9uf-psvygh7e8PzGwJHl9AHJgXsAAoYpCLwLNK4h2z5yBhlQIUKUINo-p24w74T3Qbu1fFmkIxpUnqiSsKG0KlpfA3L2iYaIK-68EnrScPuKHBY4JQD-Z2S6mijizAnwgnDZX5xudVlEqBWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fScXrnkEdmxga6JYr6cDqOIBQw74e6k0VVvPMFjMtE0uGBhituoC6RSthmzyyofJIO9QH8PuPxoWppWXJhpUo--sL1a383ZxPGI4KH7_cRfLTQLkt7MTBEL_FQDQbgtJWrXspp_L5cx_5J3t0R0gNDy4haF4Fy3E818AisA0vYFssSmEO0UtWrUo7V3HY8tmjhXxv9blodVblfjp9d_id3Miq1e_CoRH6gPrbgtmeVYP_k4NjXjK7w2ihzkA6qSmVL82qCCBwUX_LKKXWHcudyFYNcca8R4pVTVCCWNEy99e9irZ-jenDCC9fs96zyjdJ9nQQBe78eJN8ZETsaXkxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J265uCsiJQDc5y1Hb7CPaGXbi5mKV2jRj76sweor6u0zVI2IR9cptNIrWMXIF_MiXLniQGAjN9KN-qpcQUDPzm80jlGa64YFBScj7ON9qgBvAcoOaqS46Qm2N2pgx8RB7czUxu7_IFUSH4EmyTJgBzEsjx2KxoZS2wscSIgxTkyv5wisMGUXOx4joEmvIlvhvl8lKmhoOfqhYQhFzrOnSicpCxd8qAGuP9euP71LENnmyqfsnMik3Faq7xjEb1m7wo9uqhzSN3quv-4PcOzw0UCif8lmgr-pgFAVrc0TDw2nvuDtFA6wwfQKBZDL_WGpYwq2N6xCSFeGLVyOVz4XkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBEIXTLz04XlIXQV4WlYHCb7fU2ato3_mmJQz4pMWFlNhKZvJzrte2N0Kn8kaBnURFtVTCoJIQ8MfSqoJJm07R7sSUwd1fjOWCuIcr3lEYwU-CGDBXxsIwZ2hKHeK7l3rKqoZc0olsa4j_zQSKc0CUTHCqQ1ndAUqycREP9_qKLUsmvNyGFCtrdrXUzh1AUYmdT9U9fL3ZY3_7bLljZVKsh2JXX7QDZkZBhp3PcZV5eqTFr6lHwtdnmA9i7hRhbtAw2AdnsuQFy22jxR8BC7uI-1ETGKmPOBWd-l9Pxg_Z-PtBhl4X0NfqDTK-fH78cli4-vC516IbZLcZkdCnRPrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU3n6-hNMPLNL8Nc0w7HWf6f3-oclIaEv-BBBiMmNoFZkE0UGZLehno6FwB21RpW-tCFwNqzi86gzkAW29VvU_wVHksVnnylUEnYxMfscZWsxYqUxzckXwB3733INklVeWWgKZjF-JOJ8WwdDE30F0V5lLy9Zl-PRdht2Re8fYD5OZdxisJMUR7Fr-v8QB2Gs6ypIcsWxjRgu5djye8AfvnqtCFWRrpUFP1W7u_f92zPcs2k2rwgK5hBrXVnoGbZv0OoG3CteCrw-OAMIWEBp9yK6f9aI4DxFFaeG5TXdla6u4Qqd_M3-gF3DOT74JzaWYsuWStK8dBBENlKaaQmnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT9_VBelnxBD1SA3k2XppAB6uq3cXMBHTs_sQTy_vm0mSUeqBf_y0fFY_k7GpPSg6q2TPv3bq298iM4a4Amu-s5QG2O23s2Ql3oiU69Rnu_NsJkqLWgxxL-iuwqAzpxY1A27EebIFfQdC8_s4BH8CLibQWMU7bQA0x_Ijp1SOh5qtVxvoihFYnAIOoiReMpkWPPAc9g_z88_AngIjw5NMNqm1Y__SoemSkwFEyoMeA33Zh8IFCOhtyBFu5aUUXipON0aE4vQ8p9BSX0P1LWEzUCsXMfH1TOEsj9fjuCkYpHYK9fhgdjYtOhP0OqSgNIVtzEKPAfqCFaF0A2bofLOxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_4ihX8FpknEOkDetNhHs9qI9WvAZe1extBuLgkCGo9kSCgI8OG69Scx9tzf5CCgxs5z44ncLC77GJWUVEsT45qsufOAIITwAqcWHmIud2VbWXZql_NNTkTZXr1Hcsvu0E2SKnLF4RDabM-5WJGd8qyEmOhaw6A7rLF-MuMx6fTC8Bf09Df26sszyAaByK0_gMUtN44rxAFf2nw1rYudbV8nA-dXNU-D4vGNJntDUKkOzddh75O0m_KSQ4I_0cylUcyukBreazBOj54sLKcGEmVbC0qByCX3y5ZHgxTe3hkAjhgCDICM4DGl2RqHIUsk016dUcIndOAIL5a3EsE4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=MUVDdaKmW-e86VotkXD6H9569tBRvFYbFhz9DeL_iUnk2oRSDAwyZHQk5SP67Bbw0ITBZMuy37CZWmX_Zje4AEo_44bcJPrhoQzT3OfmnLQVeVrX-fiMDO6jJzN5KVA3Hu4Q_VNdo9JAiPzqHr-nkNWIR_sPLznAmpz5L--jKdTPibIJsNJvnpaZUTBMYWiXrqG9R1jqIxSfemm1TBSGB6ZY0VTJIlP4x-5YukJhsAmLl1YRwqK731iCAy6Tuqhn7-uY5RFJCCB3WZ9D_kgbI8ifxJ9pGwsVMEn_Z_fVkWYsVZ6NHZUuhsiM6CaS60QSw3w47raAC3aZS0NyykjnSHYCzhGUEbzw7x6zQfmx9UhwYnTF8lcanyakzPFlUFudK78eiQB0Nc41HhoY5fadDuftTUmYRvQpGlciK6PUh9DQlWfnthfuZjyxiAC-Un6cqhKT6nu2jLr1P_nmUHn6f4Ygqz11yE7iJNAiozhO4cEQXJ4oWcROH7yZlq1zG8gHS1AhFgbZDCY_p1sxm_03u2gy-wcT9JjkA1tGrI3eBZ0ZRVxmcNnC0ZKrx2V3nknacZiK7ZjFkH715ZGgea6uk6LXNHcZKfKIXI6_u2TX2wUWfrAh82kvqnVZe4s8yQVn3CWvLWnHVesh-aqAR0pdIscU9hAgbgJ4mLGKLGWtlgo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=MUVDdaKmW-e86VotkXD6H9569tBRvFYbFhz9DeL_iUnk2oRSDAwyZHQk5SP67Bbw0ITBZMuy37CZWmX_Zje4AEo_44bcJPrhoQzT3OfmnLQVeVrX-fiMDO6jJzN5KVA3Hu4Q_VNdo9JAiPzqHr-nkNWIR_sPLznAmpz5L--jKdTPibIJsNJvnpaZUTBMYWiXrqG9R1jqIxSfemm1TBSGB6ZY0VTJIlP4x-5YukJhsAmLl1YRwqK731iCAy6Tuqhn7-uY5RFJCCB3WZ9D_kgbI8ifxJ9pGwsVMEn_Z_fVkWYsVZ6NHZUuhsiM6CaS60QSw3w47raAC3aZS0NyykjnSHYCzhGUEbzw7x6zQfmx9UhwYnTF8lcanyakzPFlUFudK78eiQB0Nc41HhoY5fadDuftTUmYRvQpGlciK6PUh9DQlWfnthfuZjyxiAC-Un6cqhKT6nu2jLr1P_nmUHn6f4Ygqz11yE7iJNAiozhO4cEQXJ4oWcROH7yZlq1zG8gHS1AhFgbZDCY_p1sxm_03u2gy-wcT9JjkA1tGrI3eBZ0ZRVxmcNnC0ZKrx2V3nknacZiK7ZjFkH715ZGgea6uk6LXNHcZKfKIXI6_u2TX2wUWfrAh82kvqnVZe4s8yQVn3CWvLWnHVesh-aqAR0pdIscU9hAgbgJ4mLGKLGWtlgo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8CSl2TJhwFlPCT5ybKOwxVBGEFBgiwy9BwktINIz4eScbzRmYY22OHWZY_W3qAXwAtK7geNMhzLmramMFPT78lnlbUg2JpSnhIODLNJ13JBqn5JXoeaD7HBVPrLq2I-dxsD13-LzEBe__E2beWob8JGw1kBFJ7vFohz4MtTykuX1i8F6w3-squbcY_7um9j9-Npq8IOLAFs4IZ7mCixb6W4abFT-R1QY1nlMkbf1cOU5VK8JhTUMvr589TfWy0D9poL0TnKqioBJCjAVeH_aDG2El6DQI-WgUqD_rg0mM2GwWFpmic7Cryx9HmTjNtIyxINEmsaWXfZQI1vvqf89g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J__wj83LK6lQ35KaxUYiS5Ig8hO6Tw7wgzNzDm7ErpBqmIDQj-gOVgLsOaNIDfi58SX3-7NCyEB4yxhXyGAv6q_Z9Ej4O0C6boRYOp-wrigGbOULR7Qr6Ss4h20nsFtL93-5jaQPRi_xAxtivPPvayxCyMyJ1RDzITxVZbi9bKcbgTLAZkcAPr-EJHNsQ1GW_fpYKuYKxw70P2sjwjQ6V8U9TX0gEhhIiTM0bGDOvzSSEPg2yAIYiHIIEJte-rHJHSkTe_QoBMpSYNsy2nhe-Wi5k8Yqn8XWX4dpSENn8sy5xHRmIgTpeOBj_6ATqodQvrGrshsutgdMUmbD4CaacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNX1BZTUcORqzuNsz83KeW_WdLx1W8FBZABbsvCr1zdrR9EJvaNbPsnXUzLyliMfzx0amoUdY2tXXXBx_cuNLN5IG9UgxNIGwcpNuVzQYX8zuqB0_8d_vA59tpRhLHxTsfKtavs432l8hDO8az_PwXePMKHU8cdjM95w9nAkquKlIDGMFkMsU26_aUzlKNbsISzVTx9Cn5bU4UDLwrRnA7XEQW3FOyDlMBOrGMqycPtgjNgfQ-nTkX-H10M7sRgJ4gt-oRbbo8Ot-yLZBen0ZM7aFhU2xq6qPH8IH5YxQGpJP16gOPqBsEcduq6xNSXVJGfMXW0txqVXRwR_4FCAxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIWNOTryUh7FokqtcbsdZuQ1ZE0RPTGVuffqyb-7Kupj0WkIt8teqE1M6DkWnXwqgR2w3yT3JugMbhlQc2yCB2G9_OdVjLLfDVpcFuwyXaQgUJREO-6xn00NAp8Da-B2LNfDZ82VNUf4jgHOCeJRCkfIubWkAcuoPDpzpav1_h9F0BSft2VQPRfyE_RWy1u6YO-KGoUvYQpnlOq_fk0FQyJC7Nt9uqEebeLXmqfVC4bkWmuL9i8UEykUuI1hdZHioB6u0OGIBVvjoNl-IFgpG7EYHc3vlz8McP3k84Yr3gTbau67SAS9SNbZ-4Mh7lfbIwawN2CVoLoXutGn02elGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaRxyrycVJdc7mg8xHTlCdUxlQ04midvBv2v6DFdLv-PjXDaLKBLnFKkUSnJFyF8P4wJuYditMWAnm8uNl1ybemDEBnJ89T_MflkESR-y0KmCXFXQgYplnEsAeFz2fjmmedvis3lo7aL_DLUqk0scOl6UaaOCyetMvHF3Cec45EYcAgftMtqoU1_AoEAIgDLKpDZZOND_KsrmhftC-RSYgA-meOxghintBUnXe4u2r3XGw6EjIw6AJkQ-F7FQjpWPcmG0qg9IEjU0c8odrgRjBiGJFiKGm5mJtU5-drh2S-h1_efZol1pi4oPHQ9oj44cFAkt9jTcjlQVKMv5BphAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWB5ykiq9Z7ZpvaO0uoeeLh0-QrfBVtle9TbdcQT_VCwj9vuI_a5dYIfCBBb__AziF2ZIiFL_uh0diZZFDo6aHtVWbTDY7g6wFuAZHtgkF5eQI-jCooUdso_Tc1WmRNTzEEt5QY6DInpWvG8lbEJAR4waOJgUFSxFgSXNMEyQff5ino38_CU_i5RZePta9W0mpYNCvnfwXBa2HWKqLn-P_niv7-uPQLh2FA4ZOiHjUsaAALnQM59Uq4LS9v5BY_NzrnqwHHYTqLlp6P4aJNtgABtY4p3B8gsbTnGHi4gkhI1fWSmw0HtgtirEhghdxOb7ijKDTM7pYtJMDIJafkpiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOB0bdwleKPfGTxbyUJhQk5qGobQ2BHlM4Ad8Z3yzOykqvX9hgsR7dUEDDFOCtcnPrXdYGljIueOgl-cD-OCCld8Pnf73N7IRf4fnSrznm1Vte-7k22UEzHQtjOWkMH3Ks3IqDWDSkSATjAZvq6UbbH5bywe-8DX0NrG35_rMwEy1pLVHwAzuXnhnbdd8WVQRom4Vxuj6R1iY1B9zF9kDXW9OBpuq4XmcTj2AAciSwJ8kRRaSxIkL1Lt9wL5ibWZg7QJ-6k9sHqfsI4RzF7IRizEyqUIwRrfs6CbwE0_37C8D01Y1wumwj6r_BIlUOa7rQ2UALMV9PDUBQXmsn8Jjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei7JlbiUlwOmxRN1BDe5NzfI_0Q5hQ_NiyOrfnM9-B6kMoIZkVzZLAgtsBnnZ9ZbZRXCzlXTgD9nEZu9Q86E22vnP0ugahGlMh9t7J8jcbMlRkoIEH_oLjlfabSKNgbRjDeMf_nEi1jWQSyskPBA6BlaebCKRY73H_tWyj33aZNJZaczV08x6QyYS66fS4f11gcTsZT1KluLNQ6CYULgnh-zBenNfi3B-xvNirMtHYkW6WaComZU4tFnQOzrqwVnVF3zM5qsZLJ5bFBx2Ok3W5g5WR_PZfrRXOvRtdvHj-5jKr3Dfo47NpzzRF_jiqXysKnOMxgoZukDdlCOVP9Z3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCOhZZ-rrnTJdM95x-nWhdYeb9jW_uOzApq1FWbf-6ZpY8SSrm24vWGp7z8r0tNjfJg0D5jiAMfstakjkJIRhjQq71A_BB-L3mW-a0Q-hu6QOU91JYpmXNRUrtVzCKRJABgvp9r8035h9ZH1RZZ0-oOqHy2PaV_ZAms5Q6x6ZacINUU-lnRXRILgakLCsEFwbqjkAJ_taBcK-3FnyLUyy00M7va3uHBpWw3ggJTB4p_CVTc9Jzf5NL0jKzSLgPa57D0Y4p_5JTTXM-KmfFd9-LhmieiQUmqok0LU2GoElFMRIsnfUlYA8vEqIu2lQYCKiWNOqOZF2El2KZyLeTv39w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHXsbx0Glh14aePFOAwKuZ4cO63C_mvR5W2r-dQSneiA7XY4mI7L1HxryRETwk-vNoBFeh5mbNvPZ5um6Pah5r6xn6LVJnN0kviHC-QXyuZMTZuTeSPOz4isMEsGNtBYAwXL4WNR27aAACeBzwOkIpaX1tAbaUyKhqBSQdcGuO5wFwwx8ALtFTXKaB46wLckGlfeFnKZDqiFF3YyE4MRZa_ryS3ja5E_QVZk2tQ8CACofNZfxRCeEzVWnEFjVnujdenC1A9-USB2kqB8mo4xbK2YYm1-T9uki-nG4PCmbQEloojxzouFTC_iJUFwYrdI4rrSS3GTFnnELmQzAUW28A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=n8xSwkGo1F0jvFfC3iHrRVvZEMaJiaI0H1TSqCU8XpNc8rBai9FCoRwLVwr2Xkr9-KIDJOcWhyPuyr4GfLHxG6lcEinUY0sBJUlj1DTFHoNyGdG2zwt26VXDgsXfbaCr8DsT5kSISn9CQdCevgK4a4fhOEqfSfXYzYVwlQhcMV9PapeTzOgrN2U5iDd7PUgEpDICnqWo-0QPxr1lk7Sm8QrGbC_ujTpupokq8UUgWBvQ_YkB4k2PumnynAlxiy3hI9seeMH3fw7Gl1yWRyYQi5YCinEBY4dbSPCIYcWhImJqfT4fkYxmx7Mx48pg9JBRCIfH4jWRgsXXDnpV-fur6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=n8xSwkGo1F0jvFfC3iHrRVvZEMaJiaI0H1TSqCU8XpNc8rBai9FCoRwLVwr2Xkr9-KIDJOcWhyPuyr4GfLHxG6lcEinUY0sBJUlj1DTFHoNyGdG2zwt26VXDgsXfbaCr8DsT5kSISn9CQdCevgK4a4fhOEqfSfXYzYVwlQhcMV9PapeTzOgrN2U5iDd7PUgEpDICnqWo-0QPxr1lk7Sm8QrGbC_ujTpupokq8UUgWBvQ_YkB4k2PumnynAlxiy3hI9seeMH3fw7Gl1yWRyYQi5YCinEBY4dbSPCIYcWhImJqfT4fkYxmx7Mx48pg9JBRCIfH4jWRgsXXDnpV-fur6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=R7d0qgVjLPb0K2_BAUQkSGO_3ogH1ucd52-xRu6ZuzBL3USqzoTC8_p60PUBvYX2iyLA31Cwl8q98Dtbf34coEDTV-XNEHwMgb9TE1S8hCzY8UKUGU3Jkks2GlbRABcEHSi4H93ZOGfLM_JmNcUdCYUhlBbrIZ1ZOx6ZThf1t9WNTH72_q0pjAUfoeXVQ-S-dlY7d2XwZYo9SZhZSfAEawt5GicTdTTcyM15qgc5-wCDFlafSF569JP-LwV7xBDVeOtK-Igei4ZNd4WSBNGfhLo0_TmFKk-6aigpThASpO9OmULTQyBTAH8bkpegFK8I24Woi8C5DQsY0QD6-J_KcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=R7d0qgVjLPb0K2_BAUQkSGO_3ogH1ucd52-xRu6ZuzBL3USqzoTC8_p60PUBvYX2iyLA31Cwl8q98Dtbf34coEDTV-XNEHwMgb9TE1S8hCzY8UKUGU3Jkks2GlbRABcEHSi4H93ZOGfLM_JmNcUdCYUhlBbrIZ1ZOx6ZThf1t9WNTH72_q0pjAUfoeXVQ-S-dlY7d2XwZYo9SZhZSfAEawt5GicTdTTcyM15qgc5-wCDFlafSF569JP-LwV7xBDVeOtK-Igei4ZNd4WSBNGfhLo0_TmFKk-6aigpThASpO9OmULTQyBTAH8bkpegFK8I24Woi8C5DQsY0QD6-J_KcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j01cPkOkb3InLb7XQ2MU1pVYvlYTG3hrN4ZxuWeMwrukTHPZRTjH10RrlbYpeAiLEVe8ZKd9VniQuPWNkC9Zqnc51TxsBANPh63xRC3iqwOToYQmLnSEjrV5ZV1n9VTpyIi0thShOVQBkq2Rg_bKDE8SwDxadjxOr3DbmyZp1ZEKfmfc9ywozWu4f3lmMweKgVK-MnnwgHPEdk6s3oMpRltqoVTRtqoW3M-mUDnf7ONU7EBdF2IjqsysWAhX9qFl-teGZVxfkbulbdQ8bge6UcFCLmzh8ria4VfhfH3tkXSZso30m7w9D20fPlj9GpjiIIwzHKRKeRMvdbmdN5u2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2F8ep4ekMBWXa362yN3rhGFCPnjgQvT-OaNL4UddZuy8xpPX0EJwVO-6BoA1PY0297EF-Iz8gyJPUC-As8nm_3wAF_Dfv0UI47l9Fa13d9GYPYJG48oRMUUk0Ndojz1GD4T0AL-RNbUH48481pPrNV-_0oI-qmos0h8r87_tJG5q241zCQ7tzQmg6SNbmd-w83D2JVREFbNdEpvXzD6Rs2cNdP17CrwI_Pynn7xuyA8QRdlO2EicGk0-s5HVnWgyyVRJDXc65-OVLBdn727iFX9PQtXcTIruerAX8R0rUw_0-x8UEsHZsek7Rro8EXKIOZ04opvJe2aGflWZZDlgK5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2F8ep4ekMBWXa362yN3rhGFCPnjgQvT-OaNL4UddZuy8xpPX0EJwVO-6BoA1PY0297EF-Iz8gyJPUC-As8nm_3wAF_Dfv0UI47l9Fa13d9GYPYJG48oRMUUk0Ndojz1GD4T0AL-RNbUH48481pPrNV-_0oI-qmos0h8r87_tJG5q241zCQ7tzQmg6SNbmd-w83D2JVREFbNdEpvXzD6Rs2cNdP17CrwI_Pynn7xuyA8QRdlO2EicGk0-s5HVnWgyyVRJDXc65-OVLBdn727iFX9PQtXcTIruerAX8R0rUw_0-x8UEsHZsek7Rro8EXKIOZ04opvJe2aGflWZZDlgK5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1wuRQWkXdy_2bZjdjfKYzUfjaOslnnwNkEB_n4Soz0yupJqGd6azszZXyZS8TbAafuAso_HZLE976yPehT3jb1GHDYFCJtdRspjrN50--A7oebT3plH3c8fSEi-7YyczJZvFvs8Gv7V46P6xdfxGCsMrYU1oy1ctfNZCcCeWEGoqx73Fd5VJANOfAHe_3_9zcPL-mDbUHApaRjEqwHe_QctMAl0zzal45NlHfiAh-3Zc1ZGRnUqfN5bEioFIW-KOKddC0NqEP90UeIQG7IcsomRexY6YRxnRUEJQtUn5yqKcVrmoMIkSwgMnQ3LlmzvRuNL_mMEdJxo7BYimVPVaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi97S1ha5eHTeQW-vbO6UYcA3UJJaC-kRhl6FlQnc9zsZeO_ILMzb-tOXZjeORF1y8aoMkh92oJFLoJhf5zthPcGtJHTQ-dWrvc4pSd7E3euPALcUAOQ-ShZV-hK5AHZe5-lsZoxTd_2iXfqjeqVuC1dTbXvgp0AIA-pnr75V7dKnviXEj2FZ6pc_tmU49QVuaR-gHdgZd738OyXUW5sGHj4zvFttuITIh0XDpKBSVVdd13yuZ5QK7-NFsW0eUPwtauIR-3UX1ySoYLrm6XffjcX309dr0jr0Waqf5-OU5DjiwDN3jIJ3VnDg_x7_OZMjdbVMGZmU_5WcPqkBv8aFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWh0YCSz4jd5w-G8198V_nUxc2Est35zfr4SSSt1iKU_TpuvGeE14nOxPBK6HttDRZoRpt7YzIG2y-lkq540gTxJjtHYA3rQfCvQgVN5tiEgEJ5BtZb-EOQe84I9Ka1TycAH4LKEcTbjW_-Cgb-yRRydhKiwYCR7nXxIFQ5yjODz_hOq6diNVElD6mk8lrLI2Bl_YWVyLWkLYTYW0CQdhaHL2EFB60t7efkvA5LC1nM0ykmORrh0nmeeEPRRN8nPwnG45lgbkTN3kZDcUVu3A5l5MNtmoufHgYv27cfRdRL7Hk6ipLiSvQLrEX-xCbqR-kkTkCYENABKq42hyRWhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3tPSuMI4I1iARhnXGBrWK8W1WhIlVpDYZlFsAopx3yJdcyXCSQy4uf4HKi9LjWW4lotfgkE8ZAFYuA-VL3Yv59TOQq5MrtEkI01jhAEGzLZi6s4plMayNbpJrK3-SQilO9Mhi84F7Nvrh3U_9nDk1iD7Sx0_e_xXDBaE96TDIqmoxFcplvTPNWf1Xnvw7rJedUz4VMWO0RVUMRLpa87oW-a_7OulWV4Ex1gPXOddtVqwMYyShfASX1VdaMgqFNLvseqYG9RfSI2ls9phXLzOnL3VUMPIWRLC-tuWt5faWQrmD1QgMlutLOU6dUe0bLsSoyoWJFheQXc6Zc8l65dcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-tE8O441W55hbwCOhmNooj37FnXxxbXi7M6xyZyf3bqoVGUP7XJJ7C-m52QhnOMEAQ6Dlb4ju2xgjsbPkzbn1YWDfw9nOngMOOp9rCYndQNXojo3HzCZo5UDoR0guucaXaQfP5-lUtKZtRU8J7UdNRmcurVNM0xjHT9L8Z1MEdg3L7urD0cCVqwIGyPs2SJRtUn7TQPTqo14vNW3TMWbX2cLqgT0Au6nkgVATegkJjio0WbHgZVikx3baJkXygsxbcPiBuJT21h797vCQTXbKqRPfBDMoLzWT5q0z8a14O77ZF5utx5xLgMMepWK3uL6Jmnv8UujdlYmuvubpxuFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spoaCmQ7MgEa7pCeNSz2plyso-rkm-WeqgffumiiBZj5-uQqjOJSfEbqchARLdftE5kbJuH5Qk5Od40r8RE7p0Txi-bgecfQmVgcnMm3nrRAovKMymgEP9uadnJlt_OEvPul5kuJQsn3fNfmVGDPwz5mQILoVtQtLF5a_10wMZG6Ox2EfqbogdQKxkO1jarScTr3O1iBDBtV9gNu_eUuee1oGGCL2QkZI7d4q3QgIrkfiAkcrHS2pV4xx5jyqBRBm49_vETtq-oNZcAIBTa5F_7pY4yqsDPTFA8epbK6cpbnM4A9z5LBZzu5GA5ygodxYkLPENrHpo-Vw6yN4gX05A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKLNdyYni2dXe_uXDSQQfoI7HKF_MVlY_RCoViIFUxOxbVk-Dd_IFgdGO5jGsgWveG2U8MEOQb-AmJ_9rHYzXl4XPqWnAB01DhXZIu60DWcFY85yCuuQOTVoc4W2FIMnrtk0TJP-qciRVgrn0MufiVmubGgttRVhUpkEgahzrKg3WSlg84nEgfngYWnwsDNFFUWCCygsonLgxEL89jzIxjmsGaWwTS3Xrnoemg9MB7YczMc4rqgjqsAHGdDs6PuTgFZgBFhfZG-hgrBM9jyOpRN0FDe4nczsd7TQRMoLUf3ylzddFexOmHCbSrg02jx8cH8C288_aBrJ8cfTKltz8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM1LOKRNUnO5HCdCXRWV9D0zrJP6YjpApWDnlkA-J2lyojWI014_vDarORI11YKmf-gKdNX0o_jQsYffE5Wbw54gNhJdcTFgMmhDkoBh9R9mZVcbwqoUVUTLUPpjODA3YeRow16VoqZTQe3Pgwe5A8m5BnWxVjZ6Nw9X_1DreZ7AzrZWQtuwPME0KNfRFZeYEEtBYxTxb2s_Hw_yw2DUq6UXD7_jv29xuUvcvV056dtlihNOomK54xRqtqUPVkq4lCGLDXFRuo_YSiuAzSxImkY_iMaERbbeuKDmJTH_9XMAE0p_wADxRHxgLSMGo_iG-Vn19JDxa0WjDtrHk7Xoqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHQ40_0t-X-SyKY_-qqkagsN9o3xCLqCGzdeTbV-QGothDpbGEFGzfyKu3DnntWTQmjZHAfUghVuPhQfry6mVgoB5YxHLTAczO5KsngOSoBYTzMaWfTpPhfzTLAdabRw5n1jbaAmqr4XRyfwt1eZ8CBiskG-lXaV4GtPSLOa3SVz6P3_NRdfiIrdh-TcQ2Vlc0JnZI1WH9PMpLX5cZOKgDNj1Q7vYKuCwn60O9Z9qN8y0Onva3ivKG55Be9ANn1Q4oU-MaZeIcczIwwGkq22CUnb2fnvNgm-IkjB4MpSnxf-agCGloGWPLqWH4mNpjMaiVxIlWGCpRWS_6Q9cV2Qww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ArchiveTel
pinned «
بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا Vega Agent رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7350" target="_blank">📅 14:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7349">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ2Ffwqj7Ow5-Ktir6JOrjisb-tWFdTB5jq-E2Arx7QtAQ4_SbcM5_eHYfFYADtp6Uc-_Hpps1GEWEb_YD1Tu8WsQFwFbhwkUYVeS2jJ1UcSssr8RyT7117Y63HkkmVNe675So6QfM9Rn2KERkN_tmLsw17rKIWhc78ZnxcXBQ5KRvIVZzWjI2tfmopxa1huxwQcW6gtMC80kDlzg5Q1pI79DwILGzKukuu6E-QA6zO-RTin7YWPmR6OuwGLCoU1JmakpwRJPx9x-Ki2XrkUBPNginapA10sMo0l8FH46HX7hFAJUkiH36Oldocu03OlUmfZxekvzGWPqUBcFzRvFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmmGggXvaD6ojTFAkDd9dL6DiyC147VF7ZFg64yt2FnBA8dpT_iTNQmqFTOkKRqlqhh8HgjSbZEiSujU5q3xf2ei01UZbj9hn1NE68J0OTS2Yl6fZYWLhzaPbygDNz2_JqNFlEVB0fThHcq1hTPgzsFNOOFDo2jc8nhOtbLAG_eheo2YwBq5wZkPTUeIffnQtB8CjOeo1iDVIAGKW-Cxsk06IbWQXEZZX6yfKHyLuLcq3vsGY6gkOJb6fi1AHXYNb9qjuBjMS6qpBGlYyX2voNTgHNxLmM4PSET1cMyjRnQ321qn0iubgyCLy6Av7bCqj-G7CxzME2_I6a2-VjBnpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید
✅
قابل استفاده در
Vega Agent
☑️
روزانه بین
5
تا
50
دلار اعتبار هدیه
☑️
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
50 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0u1H4ho7N68C09H_y8v0E0JMCP-pB3iIA7XPlFgWSd2t7AtmbDrNwL3HxyrO4kmor0H3xKNTP6-6Bce-Cs3GLqZxgjXyKbqR6f4v0PqVU2EaOFZt-Xx2ufIWnKHyZNuzTfo8jHMcdjJd2H6GsBUh59n0E3ikV_0H-QVp1nISVN_6uw-7WV28CtO9i3YqAUuDsgZFsAnagOFAuWMT_G1HkjPE2OqEmeBm9P0Yt8dhddpSD1bIbbQDamEeJfqI_28HnwUGmKtebrv1RcaUhlnRKuoXbKOIzJNiuuOmBwRxXCxrG2Y9qyWWPV5bdlcAluG0-Ael08egzxwizYA8AQ55A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCZ14ofzMjqr7MlV2k5wcKsDo8uvZhFhv6Ecgn6HFVubF0G6ekmb7mrPXoQn5ZSHbY7d-YABA428qaTgz6ZA6ZNE7xfGM6attOya21UdIIy0gVX62_OGMQoVOzoiIDckYC4N1VI6BpZ1acVG_S_jshvC7vYrfNoqntog2uF0A2m0wcLQ9oeO3CN97o6GPEKMW2tacwp1P8JhUXHrqgOH5SPlboZnvG_yO-DjPFos6u5-uXXgPP42wevTJsNptsZlun0C5f0MNxRGLseApkmvexBU3J86qSB6Vf-ZSiIUnvs58TlUWR0R1JOBl8_kRfWwH2qQZZKv0zTWRUyvHTf98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7lYMgRnJg9koHG62zbhCjBi-GqlVRfzHN6ZCrpkpNfEbEmgSoZJcM8vqGU1rtHpQqHWaDOaak9VxI9oeZU2zo58oZnWZ4D--U4CKQRMhBXGv2sUf7rOeh3DX_xZS_-b5RKXO5LhP-yUidKBmzV7cKuZX6tnmC-4O_2uafs3s4rMdTbwmo9lIPJDH0AYpsTc7fLce6CEn2R0NE32woi64nf9HhfqETttMQ_l1CnkPSP6LiXHexjkaMx6wkUv0YQ38tlHTl3hZ6E2pgqWVcXNSv4LwBGHHrCX-VygiHZzP7VsgfqC7wxFpUQePeT0omnZ7FLOFckAQoEAmGgUWlW2Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQyVwaV3etbEkr1tDTTfSmQ6e6o40-xeGwtoCJD5tSpHHTYjcMftvl_wTPCq6e4JfNP17RZTq3YiYY6j0aqOty9bothfT-TSqaZR85FlIMTUujImIORWQfmVcOHB-StXOBvZqAj8k0F0HZIvqOV_KGlPK4JJdHM_kEjPnsoh247PgZBq3TnGCiMC-ULTD9PSzNXqeqmSiBFGPq12CtJ5OgKhShtnzc8ojkDFadteBWUDzE4szigML0OTGXLAX3YdMxAPgWZDLrpDmBvLYqIj8X1LWAm9OclhmOn6ZVegDCku7naPuG-KkC6UsYcabfKBVcce7s23I3vqYq5YTS6Aug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWDk4e5gHUwMYEydJOZ9Cca_6H-5sQKUdRQoRuf826JV0u6WfJ-u-6PkLDEn0R12SvL0gTfnu6izeRYjEOKJ8N3nk3a1jgm-n6z2E3vO6WDnY-4AggoygFyxvz0d0g4raG7nZ9InR3LRV9W-Yl-SDNLN3ov4Slr_RzcWxpZi7mGX2Wo12rO5nhbfQ3WdY59IqL-v3hCAF-9nePSTJOt77YvRZIF_jibBeREPSQXMvEaoHljZ8pN-tbu8K4MbypC-GWn5N10JM-C5RF1xswRMH8OUDjZ2PJpEhuv0hMl3v3X0HP8stkahHMnJ2klASudqd_H7VYtspRCf3VeXn2DEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/obpjBfgzKH16yUtpOaH8D5Ob8N3Ea04_weQ75gRXahbJFc01XL9dWhlbGHTfHP10aMBxTDpedSR17YNs8fPpah1YETYznWR0W8IsYtw8sRdhgAgYJqsCOQTwl3_4-KAgZyoPX29AZFxSaqSLAXeAcmP18egqsXxqr1pmQ71tdb9nYWPLlER4tbGXGqum_DhBZ6Y8g3JyMeTIeGIlcJFGR6TGl1g6IcUIdN_eqEJK4VNLs4Jw0sSMiA0ZZj5Uy7tkRkKcEqPCZk5ZWfdOZHYIsezt6H9m8e92l1d5fvqY-7C6hpH3xkxCcPVW8DeOxJ7cZT5wWwK_rcd8XxzEPZBwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHYFSEfcrBDDA8E5NeXN05N4va7M5En10iLxXLvT-bjqaCFjBFD5Qf7jhBQEpmz91JlECMy7o_Ruds83MiijztAMiiZtZL5ehCMW2v_3uVuJtenZO8U9zuOgSO85uSeFDIJFzahOGrcQEFhaMxg_xFH0rhLimQignhlz-TCEzjy1GN1hv1MMT9UTDw04KP4ohfpJSZDrctAX8TNmWSMhdfjqiYJpIpArZa26RipNV2BHZC29VvdLOV-rtLwQw8FRQjqPk0Hg9psXJ10mJxCxBEwU7myJ3olW-pQaRCzBS70jXkJMFR4xl8-AicqKoFKPpsvU0DXjhxP_utXumEwVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOIsrIHeHeHlsq7Uf6W7PDV_sJ20E6nLHRY9We43-tnYYs4tQ8Bg7KppDeL3OJAt9Qh2rQ2bDb-xLhlCJU3rjTR8NSsg5NNmGpsqS0Cs8PajlAZLyFNSAva-gXkEVIY4JbwrHpZet3Ypy01mmRxxBvVI2v-E8eax8-Ix9UWimgHyZo7qKm2SWrM6YzsmWyUS_H0HfIotNwQnDc96-QdilY5iBCgCOrzFE3U8FhzrLDMDSIDgeCsmy3kvsP6-frgA2y1yxurcbZatqUubo7mA5dBq7DicQ80EdCVqlWgXkKVbNDargeSUafnr-buQpgdRGIQmppAhoBgUBRWbBlj3Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا
Vega Agent
رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ سرور واسطی این وسط نیست) و مستقیماً با کلید API شخصی خودتون (BYOK) کار می‌کنه.
✨
چه کارهایی براتون انجام می‌ده؟
🔹
پشتیبانی از همه مدل‌های معروف:
از OpenAI، Claude و Gemini گرفته تا OpenRouter و حتی سرویس‌های لوکال مثل Ollama.
🔹
مدیریت مستقیم فایل‌ها:
بهش دسترسی بدید تا فایل متنی بسازه، کدها رو ویرایش کنه، PDFها رو بخونه یا فایل‌های زیپ رو استخراج کنه.
🔹
۳ حالت اجرای هوشمند:
برای اینکه کنترل کامل روی تغییرات داشته باشید، می‌تونید روی حالت‌های خودکار (Automatic)، برنامه‌ریزی (Planning) یا تأیید مرحله‌ای (Accepting) تنظیمش کنید.
🔹
مرور و جستجو در وب:
خودش تو اینترنت سرچ می‌کنه و محتوای سایت‌ها رو برای تحقیق و استخراج اطلاعات می‌خونه.
🔹
امنیت بالا:
کلیدهای API رو با الگوریتم AES-256-GCM رمزنگاری کردیم و کاملاً امن روی خود گوشی ذخیره می‌شن.
📥
فایل نصب (APK) و سورس‌کدش رو تو گیت‌هاب قرار دادم. نصب کنید، تستش کنید و اگه خوشتون اومد حتماً با دادن ستاره (
⭐
) به مخزن ازمون حمایت کنید!
📌
لینک دانلود آخرین نسخه از گیت‌هاب
@VegaEnter
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_5DIaXGyIbd2GN02bmxRwh6B0yF5gzvlOrSY8Y0FP-hbfXDxc33gJcTmajbnH2gAH7_BAwGP9-WkcRfm0hseA4EgpaQsfTz5DvKxsLzb90B3jwpEobCpVWd1iIWejrPOfObGY3bepvW6VHuYDv2XuJXkB8ra1aBgL14SdIFnsRSUVSg7XgL-u8RioLaAnR53dJtiSyAQQQJhHsTU4xa9oE3jKB1hGMyCcgNiBV2Ty9SaUP6hC9XYU7y1XtuJiBaetkPsnPcQJGJX9MDDx5yns_OsREEsPKtZcpvr_OSVYpAyiMXrLPi7VatKM8hQahvfGnHHl0A66mdz648cD-TYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت ویدیوهای حرفه‌ای با هوش مصنوعی، اونم رایگان!
🎬
✨
بچه‌ها با وب‌سایت
Dola
می‌تونید روزانه ۴ تا ۶ ویدیو باکیفیت رو با مدل قدرتمند
Seedance 2
تولید کنید. علاوه بر ویدیو، این سایت ابزارهای چت و ساخت عکس هم در اختیارتون می‌ذاره.
🎨
✨
ویژگی‌های کاربردی:
🔹
تولید ویدیوهای حداکثر ۱۰ ثانیه‌ای.
🔹
امکان دریافت خروجی در ابعاد و سایزهای مختلف.
🔹
کیفیت تصویر بسیار بالا به کمک مدل Seedance 2.
🔹
دارای ابزار ساخت عکس‌های خلاقانه و چت‌بات هوشمند.
🔹
سهمیه رایگان تولید ۴ الی ۶ ویدیو در هر روز.
⚠️
نکته مهم:
برای باز کردن و استفاده از این سایت، حتماً باید از VPN با
لوکیشن اروپا
استفاده کنید.
🔗
ورود به سایت Dola
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_BwLjCScsbs7UkIosdT-fCYFOXoQKyT27BRohG33xIRwcWGvxrgX-nNmS5YWIUvf-lnPY4g1GqQK781sTw5kdxiRUu6TJWLo-IC3kroetqE18_TaUmsoL0JCJgS3tNgUMBDon_CnRCkVLjf2booyrOcP04QW0UVAZSQTjZiXz6HXUG3DFKW3astPn0s_vYeH1Q1q2r-b2HHUyAFkCkuEv7gFxhBTCtqe0q08btc8HrKhl5QQf-kllOkmBLGBbpn2i1-i69kmmxDQqQL_u4ztf2eWk9-YVUr4vaGYC2cb745LdrZ7ukcOe1pYT8qodods1dGxEiplT8OLRqPTJEolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Türkiye'deki İnternet Kesintisini Aşmak İçin Güncel Yöntemler
🇹🇷
🛡
Herkese merhaba, Türkiye'de yaşanan son ağ kısıtlamaları ve internet kesintilerini atlatmak için şu an çalışan en etkili yöntemler şunlar:
🔹
IP Spoofing (IP Yanıltma):
Şu anda IP Spoofing yöntemleri filtreleri aşmada sorunsuz çalışıyor. Xray/v2ray yapılandırmalarınızda paket parçalama veya IP yanıltma tekniklerini kullanabilirsiniz.
🔹
DNS Yöntemleri:
Bazı ağlarda özel DNS ayarları veya DNS Tünelleme (DNS Tunneling) yöntemlerinin de erişim sağlamada işe yaradığı görülüyor, mutlaka test edin.
Lütfen bu bilgiyi internete erişimi olmayan veya sorun yaşayan arkadaşlarınızla paylaşın!
✌️
#İnternetKesintisi
#Türkiye
#ErişimEngeli
#VPN
#Turkey
#InternetShutdown
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXC6VQGmTess_-deIIeuED7aizz86GCvpBvyZyEvN4z04g2xj6Fl8t_K7Jx8VyEqaLJDZxvHcIdqBcPyO5seTg5jHuemuuGy7udmg59alChRsisOVgpENLV17OiI0z8XHdlvtgMuNJaLVWIpbalDPW-Hg6FAw81jmLUrv2k_ktcH5a4tcC3818dzw0xR8IAUu6Pr_z1rFaoMfRZUBOsCPVbEA1aX7nVXQ-7WexuCbDvxY_gDyOfx0ABX4jU9p0geCImkixaiwhNZsIFzqc-ASgkRFoweuLR7nbwhSMmDhWG_uLhKtvQyzukqKWWkKEmSpVBWjvfXAvW2idChUmSxdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به هوش مصنوعی‌های فوق‌سریع و قدرتمند در یک پلتفرم!
🚀
‏با این سرویس، تمام مدل‌های برتر دنیا رو یکجا در اختیار داشته باش. همین الان شروع کن و از قابلیت‌های هوشمندش لذت ببر.
⚡️
‏
✨
ویژگی‌های کلیدی:
‏
🔹
دسترسی به مدل‌های پیشرفته (‌Opus⁩, ‌GPT⁩, ‌Gemini⁩, ‌Sonnet)⁩
‏
🔹
مجهز به سیستم ‌Agent⁩ برای انجام کارهای پیچیده
‏
🔹
۲۵ درخواست رایگان برای شروع
‏
🔹
۱۵۰۰ کریدیت اختصاصی برای استفاده از سایر امکانات
🔗
https://app.clickup.com/login
‏
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XEMDC_QSv_L9RyjrMIqgnadU2dQfj_PqplZ9Wl_6iK_PddCrwSob8Jzv44qNlKNq2EITlwprdJzbBNemfgGbshIx5ikMWbWIhwmFCSnU6xfwjxRuH5LCpXRMvXPDX7l7mUPXlQG0xiEx0nZAz3XmW5hftVS1Mi2snwsLJ24NlT216t38BdfVFH2xkye6S4P_E9Zkt9RmtWYxCLLkfjQHwTsGSjJzLbtVoT-gtDPQAO-QzegJcDuohjdEXp6iyfdMxPaVt0ugWLY6txmQF2uUc2TjUg7iNjju1sZaszAMmmiqQHVIbVPJfsXeZPE3O0_6hCGbwp4fXx29mjIb3Jbtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kl_PakcclG7boHpglTUtlgsjvhEbPonnRkJswpslQT8VvhyGFP3dXFl5B7Ulg6hrLP8NS6VstpemgM8NtqDcNkglE3BBm_7dSlAnps4u-1K0GCIPq8qATxu_642LnAC3mr_GH5FJOdJ0LvB__giVHwvK_RSFmrEmTgNdJ3tYpnJc-eUQhfD2OGTu2Hq5aLNgyS4o4E1lhYhw3-m0fHkgIJOWrzEHMRQNmxWSU61dxbZ_8EfToywSyTqPQS_xZZIMUipwzriBKX4uW-gXvMOX4WQelBlv1A7D45wXCR2qbIFhdHmYot2SYwszjufT-aL3JmrdYe4sbM3EK6MukQzioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_Bs4C_5nz3L-_MAtR46FG2PAn0In5CpJGMJjacO9f37oSq_4eimFFBFHOa9TOPi36jYUCcqkgjNdfYPre7y_WnoI9f-ePRxj_jYfoTS92sR5QxYT9bG0vVOfww0C1gqjUyjvixoz0hvnAMDhgO83zoYsYUylh12D9uLNT2yByRlXZlX6cx47zPCCUoVa46ths49fE_-At7vJXD9Kbbz69Pr-CYGQcUDLKDscsO0dmX5n3ZxOitxUAj64_rRGi8uMunzxMZTUhQoq5rzVvu6usAhZS2xeQ4NnVNXEou-aWAXLH6wy0hYEE9GzHg3MMmeqrJoWIHOcFXJR7NgYP_W5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG:
github.com/patterniha/v2rayNG/releases
۲. ویرایش کانفیگ (
✏️
)
۳. فیلد
Address
: یک عدد آیپی تمیز کلودفلر
۴. کادر
finalMask
:
{"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"],"delays":["0"],"maxSplit":"0"}},{"type":"fragment","settings":{"packets":"1-1","lengths":["109","1"],"delays":["1"],"maxSplit":"355"}}]}
۵. فیلد
Fingerprint
:
unsafe
۶. کادر
cipherSuites
:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
۷. ذخیره کنید
✔️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.2.6-P2-fdroid_universal.@ArchiveTell.apk</div>
  <div class="tg-doc-extra">68.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7323" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود نسخه یونیورسال PattNG (نسخه v2.2.6-P2)
🚀
📱
بچه‌ها فایل APK این نسخه (Universal F-Droid) روی تمام گوشی‌ها و معماری‌ها به‌راحتی نصب می‌شه.
🔹
پست مرتبط در تلگرام:
🔗
مشاهده فایل و جزئیات بیشتر در تلگرام
💡
*دم توسعه‌دهنده‌اش گرم، واقعاً خیلی زحمت کشیده! اگه دستتون بازه، با زدن استار (Star) توی تلگرام یا گیت‌هاب ازش حمایت کنید کارهای خفن‌تر تحویلمون بده
😁
⭐
*
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7320">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فردا شاید ی سورپرایز یا دو تا سورپرایز بزرگ داشته باشیم
🫠
❤️‍🔥
(البته از ۱۲ گذاشته ساعت)</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7320" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7319">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7319" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
