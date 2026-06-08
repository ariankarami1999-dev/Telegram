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
<img src="https://cdn4.telesco.pe/file/KwC_ryRjtHHEGFN7gU-5iNFhcqsVdZDHRdbcmbtqZTlulhePqA53tfdNmONQlCVsSK6Kv8rTDCbN2_w1ZSBHERQKYEglBcF3xvtCMLQsgGfWDr1ZDRisagrWEBxqkR6FUOV72zLsF-q5-tSglEmBap5dmtTElZHufCB_JdZz8BS86WOIP0PPe7erMsj3U8EEUC3-1C1tiT7pq1Af_mSnBMiquTW0762eZuSjFXJ2KyoSwSHvxxFwvLeuQ2dqRMY0ynqMYYf3kqqTnG3-FfZTPKWaJ5ugkc6XPNoz2tYjvXJpEoqepjmvPjh8uL9Uvls-rgfp9mlTEi9FBTh1dPHW2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-133037">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
قرارگاه خاتم‌الانبیا: پاسخی دردناک به رژیم داده شد و توقف عملیات نیروهای مسلح اعلام می‌گردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 304 · <a href="https://t.me/SorkhTimes/133037" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133036">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
🔴
فوری ترامپ:  هر دو طرف، اسرائیل و ایران، به دنبال آتش بس فوری هستند! مذاکرات نهایی در مورد "صلح" به شرط دوری از ناآگاهی یا حماقت در راه است.   محاصره به قوت خود باقی خواهد ماند تا زمانی که "توافق نهایی" حاصل شود.   همه چیز باید به سرعت حرکت کند. با تشکر…</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/SorkhTimes/133036" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133035">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  اسرائیل و ایران باید فورا«تیراندازی» رو متوقف کنن رئیس جمهور دونالد جی. ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/133035" target="_blank">📅 14:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133034">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/133034" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133033">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAVoKfiCzFvNjGFf88b1SyFutiW-lvkYjzMUkcGYcjORb6f1bO0OH2gmcdxlEU8P_AKZtIzo6lQdOHzsE-WfbQt-ksktRJUpsE7HfMlJ9mPxGhHxSPW9OKoA4dsefh0TJMpmmttwxi0zSZa4rv-rZv7QWft346T2R0bIna8mO_2ybQz4e7FSz7JLNiFTyJZzFWo8r3Cj3CMqRPY1knZ7ah1mv0W1sJ4lTrkBlqA5vgPOzGKlxrVmsQGqjjs92DApNry42Eqc_rfEVgHbpmWbmDKhRghxTYf7a7pZwnl07D5aYIfhdhaQJgsac8VrRgAliHx798Rjlj0aO67-3aqm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تمرین امروز پرسپولیس بدون حضور خارجی‌ها و ملی‌پوشان و سروش رفیعی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/133033" target="_blank">📅 14:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133032">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 750T
20 گیگ 1750T
🛜
مناسب شرایط اضطراری و جنگی
ثبت سفارش و پشتیبانی:
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 484 · <a href="https://t.me/SorkhTimes/133032" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133031">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
فرشید حقیری: امروز جلسه محرمانه بوده و سرپرست جدید پرسپولیس انتخاب شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/133031" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133030">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/133030" target="_blank">📅 13:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133029">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
مدیرعامل و رئیس هیئت مدیره پرسپولیس هیچ اطلاعی از سرپرستی خداداد عزیزی ندارند و تا به حال جلسه‌ای با او نداشته اند.
♦️
اما منابع دیگری به ما اطلاع دادند خداداد عزیزی در روزهای گذشته با شخص احمدی مدیرعامل بانک شهر جلساتی داشته است/شاهین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/133029" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133027">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq2X4yaB5WXUHh-tT9G6vRZHLrwT5oT-MTCzXDEOy5MMqq_yqxHy2fhI_SBkVlJLnNnS8ihOAzMhNOxub_X9wZZCr4mG1BDu9DeGsSy13rzw5MuVF21ukIX8uB_SNzFe30e8NF1Ppp72782XscZHCYtdAImoPMguP0ECzyYjfiZA4LxcyoEzTZ-Y5L4yMu_fyHt-ulVDVL3Vh6roNEZIAZ2i59VEYlNR2wdfu7-XScyGJG9A8s0Wz4JoUDqHhqmXn6jen2bxDhOGMtAqnXOBSaBClatN1jpXB6gAT0hR3bHZrB_9IeOnUu-ut8u6T8mLB7qDot09T43z1CoEZb7vtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ:
اسرائیل و ایران باید فورا«تیراندازی» رو متوقف کنن رئیس جمهور دونالد جی. ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/133027" target="_blank">📅 13:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133026">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=iHv2CoxggYHSMcNPXttoFqjKcVDz-4sZw-LN2LfsPwmEnjzKb6Zmd32jwz-iOnRORxlNx--5tRyOSvgVx0z_55QQECLaJCpOaExLd6Evg90MX-VSbEXKq8KNmPx1BNg6nHUUJ0NOFPBmKJgItGoHZNJBMEBW2O7m9dusYEqe09edQ3EIEZ1jMbqnZFscJu8huWNFpjLCEhnl8lD9g2KMX1Pe7IhbHi1mIfFiqWq6ZijN3rjn9vmO1rB3_NUz8aYgMZGddR-uW8Y3QVV9PYbDmeIDDbj3UEVPP7_tzHNpAMxCi54hqim5nsTiC1fXYz_pdTQrRhe2hNJVEDwJ7B6L2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=iHv2CoxggYHSMcNPXttoFqjKcVDz-4sZw-LN2LfsPwmEnjzKb6Zmd32jwz-iOnRORxlNx--5tRyOSvgVx0z_55QQECLaJCpOaExLd6Evg90MX-VSbEXKq8KNmPx1BNg6nHUUJ0NOFPBmKJgItGoHZNJBMEBW2O7m9dusYEqe09edQ3EIEZ1jMbqnZFscJu8huWNFpjLCEhnl8lD9g2KMX1Pe7IhbHi1mIfFiqWq6ZijN3rjn9vmO1rB3_NUz8aYgMZGddR-uW8Y3QVV9PYbDmeIDDbj3UEVPP7_tzHNpAMxCi54hqim5nsTiC1fXYz_pdTQrRhe2hNJVEDwJ7B6L2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SorkhTimes/133026" target="_blank">📅 13:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133025">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
غیررسمی/ خداداد عزیزی به عنوان سرپرست جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/133025" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133024">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/133024" target="_blank">📅 12:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133023">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
‼️
اختلال شدید در اینترنت. فیلترشکن های رایگان دارن از کار میفتن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/133023" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133022">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 250T کاربر نامحدود
30 گیگ 300T کاربر نامحدود
35 گیگ 350T کاربر نامحدود
55 گیگ 450T کاربر نامحدود
100 گیگ 650T کاربر نامحدود
دوماهه
50 گیگ430T تومن کاربر نامحدود
70 گیگ 500T تومن کاربر نامحدود
150 گیگ 750T تومن کاربر نامحدود
200 گیگ 800T تومن کاربر نامحدود
سه ماهه:
120 گیگ 730T تومن کاربر نامحدود
160 گیگ 780T تومن کاربر نامحدود
230 گیگ 850T تومن کاربر نامحدود
320 گیگ 1T تومن کاربر نامحدود
400 گیگ 1.2T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 546 · <a href="https://t.me/SorkhTimes/133022" target="_blank">📅 12:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133020">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
برای رفتن به بله و روبیکا آماده اید؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/133020" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133019">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
🚨
فوری؛ انفجار مهیب در غرب تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/133019" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133018">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
برای رفتن به بله و روبیکا آماده اید؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/133018" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133017">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
باشگاه پرسپولیس:
‼️
ما با آقای تارتار مذاکره نکردیم. این حرف‌ها برای بازارگرمی است. پرسپولیس تاکنون هیچ‌گونه مذاکره‌ای با تارتار یا هیچکس دیگه‌ای نداشته و این ادعاها صحت ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133017" target="_blank">📅 11:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133016">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
همزمان با صف شلیک موشکها هموطنان‌ هم صف پمپ بنزین رو تشکیل دادند تا این سنت حسنه و ملی رعایت بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/133016" target="_blank">📅 11:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133015">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
🇪🇬
🏆
دیدار بین ایران و مصر در سیاتل از سوی کمیته محلی برگزاری این دیدار از جام جهانی بعنوان"مسابقه افتخار"(Pride Match)برای همجنس‌گرایان نامیده شد!
‼️
‼️
پ.ن:طارمی و صلاح باید بازوبندی رنگین کمون(همجنس گرایی)ببندن.
🫣
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/133015" target="_blank">📅 10:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133014">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
آغاز رسمی جنگ
‼️
سپاه پاسداران خبر از آغاز رسمی جنگ با عملیات «نصر» داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133014" target="_blank">📅 10:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133013">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
🚨
دستیار اوسمار در راه تهران/ ساعت تمرین تغییر کرد
✈️
جولیانو والیم بدنساز برزیلی پرسپولیس فردا ساعت ۱۴ به تهران خواهد رسید تا اولین جلسه تمرینی پرسپولیس برای آماده‌سازی جهت کسب سهمیه آسیایی را برگزار کند.
⏰
تمرین پرسپولیس که قرار بود ساعت ۱۱ برگزار شود به…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133013" target="_blank">📅 10:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133012">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
آن‌ها مداركی به دست آورده‌اند كه نشان می‌دهد چادرملو مجوز قطعی حرفه‌ای نگرفته و مشروط به يك  توافق بدهی حقوق است.
⏺
چادرملو به پيمان بابایی از يک سال قبل بدهی دارد و هنوز سندی در اين مورد ارائه نداده است،اگر چادرملو تا فردا اين سند را ارائه ندهد بعد از شكست…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/133012" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133011">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
🚨
دستیار اوسمار در راه تهران/ ساعت تمرین تغییر کرد
✈️
جولیانو والیم بدنساز برزیلی پرسپولیس فردا ساعت ۱۴ به تهران خواهد رسید تا اولین جلسه تمرینی پرسپولیس برای آماده‌سازی جهت کسب سهمیه آسیایی را برگزار کند.
⏰
تمرین پرسپولیس که قرار بود ساعت ۱۱ برگزار شود به…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133011" target="_blank">📅 09:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133010">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
آغاز رسمی جنگ
‼️
سپاه پاسداران خبر از آغاز رسمی جنگ با عملیات «نصر» داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133010" target="_blank">📅 08:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133009">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
آغاز جنگ ....اگه دوباره قطع شد همه چیز .مراقب خودتون و خانواده تون باشید ...خدا به همه رحم کنه .بازم جنگ .بازم استرس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133009" target="_blank">📅 08:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133008">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2e80c06fa.mp4?token=SYk28O1FDzGKPf9nutrm3ypaR89p0C80bY7Qx4odyau7BFvFlgMcH8b7p_fK4pezQuJWEMMfBvCc0RAkyEXixEhy0BWKYV4pO1VP8qgEHi3gODlGf7X3Ba8D61j3CGt_00YTzk9gA8j4UyMQJu0zK8KcDUeOJS_1bFbKuokgYkJVYQoaXGqsqu0x_qK38VLJoLo95fHVfR_78PZBSz6aeWxxLxb7yR8pf8jxMWvPKTXKbDT0nAy-ZO3uAj6GRREkNt_AHsBqSCT6kRihBPVneg0-y7ntP8eKi0zgNao4EGOPRujwnEUUQ_nw7yNby8IBVLSygY9d-u6v2zzLUDU4FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2e80c06fa.mp4?token=SYk28O1FDzGKPf9nutrm3ypaR89p0C80bY7Qx4odyau7BFvFlgMcH8b7p_fK4pezQuJWEMMfBvCc0RAkyEXixEhy0BWKYV4pO1VP8qgEHi3gODlGf7X3Ba8D61j3CGt_00YTzk9gA8j4UyMQJu0zK8KcDUeOJS_1bFbKuokgYkJVYQoaXGqsqu0x_qK38VLJoLo95fHVfR_78PZBSz6aeWxxLxb7yR8pf8jxMWvPKTXKbDT0nAy-ZO3uAj6GRREkNt_AHsBqSCT6kRihBPVneg0-y7ntP8eKi0zgNao4EGOPRujwnEUUQ_nw7yNby8IBVLSygY9d-u6v2zzLUDU4FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| کانال ۱۴ به نقل از یک مقام اسرائیلی:
🔻
ما تأیید می‌کنیم که یک تأسیسات پتروشیمی در ایران هدف قرار گرفته است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/133008" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133007">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
ساعتی پیش ارتش اسرائیل به اهدافی در تهران ، اصفهان ، کرمانشاه و... حمله کرد ؛ این حمله از خاک عراق انجام شد و بسیار محدود بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133007" target="_blank">📅 07:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133006">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری، زیرنویس شبکه خبر و تایید شنیده شدن صدای انفجار در تهران، تبریز و اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133006" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133005">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1OxG6vMAJdkwBndIrjU1FrfV_7F1OesFRDxkAzh5vvBLAoMn6fXh6WAsJGbADrqtdm5cHf3NrnV-Gcm-4aX-IUX9UTEb3jEDkucGuWnedEumoLd7-AsMV8WagcaQQYEljnCeyMVUWyWc4Tq4cowkq1ksW33CgWw90OncqaKoFbnJHAlQz7T1ARTcqWe8Tzl40jPVIX5W1MLKpAT195QaO84N93ZbPK_UkrC1i8yaH01DnPl7l6BgrvaI0KCCMUJqcJ5jfYonmZjtz_8rzY5N4PwH75dwlQnQLwaSY-QGWQr2SmHflN9PbnCx6ClJq84fPZqFsoZYWowcdNdbA1Lrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری، زیرنویس شبکه خبر و تایید شنیده شدن صدای انفجار در تهران، تبریز و اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133005" target="_blank">📅 07:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133004">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi3kqbqiq7XUi3qReQQmNqk4MAK3o-ZH4SGMpEbKff0iC4Y2XYaAgw7EFIXhq3ozWUlznMXVpyCgRz7w6eqJXf1vt05cxCvGDBXCstyxtsHCdyJ3MIQWa6swTKU5oUfWSLs02Mkc-VNskPGvA21BsTJ1M1FRurbsk_T5FRUsUxju5ybZVFW22nPBPvoDKXT4Qkj58Ze_lJDXjkS2rOrkJg1Yc5-8pAWYKBjkoyQA5UT_lLgNuwphiSEZ68uq8VNqQLMOxXsF-zhMbtSVHZH5uRtLOJOSwMjIqIb22jU5L9sLh2bPXONEcT7JwJMmkeaEl62WDNngMZd7UuY2rXFJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/133004" target="_blank">📅 01:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133003">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
🔥
الجزیره: امشب ایران حدود ۱۰ موشک بالستیک به شمال اسرائیل شلیک کرد که ۴ اصابت به تأسیسات نظامی دیوید تایید شده و چند نظامی در این حملات مجروح شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133003" target="_blank">📅 01:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133002">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
محمد عباس زاده با قراردادی 2 ساله به فولاد خوزستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133002" target="_blank">📅 01:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133000">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
کانال ۱۲ رژیم: ترامپ و نتانیاهو اکنون در حال گفتگو هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133000" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132999">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
باراک راوید، خبرنگار آکسیوس: ترامپ به من خبر داد «الان دارم با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132999" target="_blank">📅 00:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132998">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
🎙
بازگشا، سخنگوی باشگاه:  بعد صحبت هایی که با کادرفنی و بازیکنای خارجی داشتیم قرار بر این شد که براشون بلیط بگیریم بیان.  سرپرست شدن محسن خلیلی هم تصمیم آقای حدادی بود که هیئت مدیره هم موافقت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132998" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132997">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
✅
عقب‌نشینی ترامپ: حملات اسرائیل به لبنان با من هماهنگ نشده بود  ترامپ در گفت‌وگو با فاکس‌نیوز: از حملات اسرائیل به لبنان خوشحال نیستم و این حملات با هماهنگی ایالات‌متحده انجام نشده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/132997" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132996">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
ترامپ به کان نیوز: فکر می‌کنم اسرائیل به اندازه کافی پاسخ داده است. نیازی به پاسخ بیشتر نیست. ما می‌توانیم پس از ۳۰۰۰ سال به صلح دست یابیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132996" target="_blank">📅 00:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132995">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
ترامپ به شبکه 12 اسرائیل
🚨
📰
:   در حمله موشکی هیچکس آسیب ندید. اگر نتانیاهو پاسخ دهد ، این ادامه خواهد داشت و ادامه خواهد داشت  ما بسیار به توافق برای پایان جنگ نزدیک هستیم و این توافق خوبی خواهد بود  نمیخواهم این موضوع توافق را به هم بزند. هر دو طرف حمله…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132995" target="_blank">📅 00:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132994">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
باراک راوید، خبرنگار آکسیوس: ترامپ به من خبر داد «الان دارم با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132994" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132993">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132993" target="_blank">📅 23:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
دونالد ترامپ به Axios گفت که فوراً با نتانیاهو تماس خواهد گرفت تا به او بگوید که به ایران حمله متقابل نکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132992" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
ترامپ : موشکاتونو شلیک کردین بسه ، بیاید پای میز مذاکره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132991" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فورییییی
🚨
🚨
ترامپ خطاب به ایران: موشک ها را زدید و دیگر بس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132990" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132989" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
🔴
نت بلاکس: ترافیک اینترنت ایران 25درصد کاهش یافت/ اختلالات شدید در اینترنت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132988" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
🔴
نت بلاکس: ترافیک اینترنت ایران 25درصد کاهش یافت/ اختلالات شدید در اینترنت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132987" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
آغاز جنگ ....اگه دوباره قطع شد همه چیز .مراقب خودتون و خانواده تون باشید ...خدا به همه رحم کنه .بازم جنگ .بازم استرس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132986" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132984">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132984" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132983">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a27b87875.mp4?token=X3LJKk4H7FYZ-balgn-DQhtjzDm744BdxoT3slRH4KiKmlFMqT0CnS7CTntIeokaNe7hTKOlc7jSKCLfpwnKwpIgP6zzCS6ZcfmkndQGG22F8QAYDLV6kqpet0swXKFxK3AkUXJoWbj9EJuek5N2_2vz43rZT30OAMj5X15VRMtYEpHkNAGodHugRA6rm7Sy48Ub2X48PnIXop5FhNIq2jQqL9EM9eWE5tS0MxKs0ZWZ0ioAu0RjmlJ5-Uepakknz8loG7X2epdMuWRmDa7xPnde4ZE44ssb5I-rT6YS2Mbgud80vGJAjcCp2LSeRZcvfTUXV4pXWihAffIkW5Ty0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a27b87875.mp4?token=X3LJKk4H7FYZ-balgn-DQhtjzDm744BdxoT3slRH4KiKmlFMqT0CnS7CTntIeokaNe7hTKOlc7jSKCLfpwnKwpIgP6zzCS6ZcfmkndQGG22F8QAYDLV6kqpet0swXKFxK3AkUXJoWbj9EJuek5N2_2vz43rZT30OAMj5X15VRMtYEpHkNAGodHugRA6rm7Sy48Ub2X48PnIXop5FhNIq2jQqL9EM9eWE5tS0MxKs0ZWZ0ioAu0RjmlJ5-Uepakknz8loG7X2epdMuWRmDa7xPnde4ZE44ssb5I-rT6YS2Mbgud80vGJAjcCp2LSeRZcvfTUXV4pXWihAffIkW5Ty0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132983" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132982">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132982" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132981">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
#فرهیختگان تکذیب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132981" target="_blank">📅 22:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132980">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
#رسمی
🔴
محسن خلیلی موقتا سرپرست پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132980" target="_blank">📅 22:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132979">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
🔴
کانال ۱۴ اسرائیل:  ما بهتون داریم میگیم اگه ایران بزنه، از الان باید تهران رو تخلیه کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132979" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132978">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9405d969.mp4?token=oxN8rTxEi_GnY98DoJpE4j97ECvDjMjlNbGf7N3lY0JjCnyE9siEl42r6F267biku-HiTp8uDigHIsh3BQuahYGMDvt5W6a9LVU6-PPJrkJ685SWdDgY0_RUo-s0ZTMQZPzaWPrqZyt0hN_Se-NiYqtzbi0aXLgv1DDchMCw6gDP9iZFIOB0NLp3PT9WttfVcFRRPr2mIV09-Wy_VYwbofBFIibuJlTwcWvaOXsxoKDOVc0Be9l4pFfWBzrfXD36TdnTa9jZYyEj77cqlrWWFTGzR30tsLjIdOGnH_vncUP_p1_8HljSYdBmdyq-jxC3JNE75zXgcciOS-JzQpkBSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9405d969.mp4?token=oxN8rTxEi_GnY98DoJpE4j97ECvDjMjlNbGf7N3lY0JjCnyE9siEl42r6F267biku-HiTp8uDigHIsh3BQuahYGMDvt5W6a9LVU6-PPJrkJ685SWdDgY0_RUo-s0ZTMQZPzaWPrqZyt0hN_Se-NiYqtzbi0aXLgv1DDchMCw6gDP9iZFIOB0NLp3PT9WttfVcFRRPr2mIV09-Wy_VYwbofBFIibuJlTwcWvaOXsxoKDOVc0Be9l4pFfWBzrfXD36TdnTa9jZYyEj77cqlrWWFTGzR30tsLjIdOGnH_vncUP_p1_8HljSYdBmdyq-jxC3JNE75zXgcciOS-JzQpkBSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیدار دانمارک و اوکراین به دلیل بیهوش شدن کریستین اریکسن متوقف شده است
◻️
اریکسن پیش از این و در یورو 2020 هم دچار حمله قلبی شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132978" target="_blank">📅 22:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132977">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irjMv2pCS1YOs_nhLhMsThtyWSLBSM5qja8D1wjnVO4dx14bDaYQPzm6S0Hm6-MlQVcyPxH9NpKDjO3rXDaE5-eGRpiuanPm4kDQpw6QlRUxQQg78ZyikIMyLc4f54yXcstOIxiya2COZRay2TCKglBuTDkHIuXhT1sbwm2aMMa6l28cCrqVms3wa4Dx0kZm_2NvxLiwhwjCkWOILjT8UnwnfIuOru-OxX63Itcx6bPqkrfF30mV1kJc-oe0sZJr6YBghikMDyB4oEUSBTPVRn3Wa9pF8_QJjGaUHKAEB490ye227H83CWGHCP_GG01BFcKW0wL9aJrR4ao-0lRWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اریکسن دوباره وسط بازی سکته قلبی کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/132977" target="_blank">📅 22:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132976">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
غیررسمی/ خداداد عزیزی به عنوان سرپرست جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132976" target="_blank">📅 21:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132973">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwYembzZVHcgtKxWU05Hd1BxNaIZZTQ-PRtcZBJ5CdifdrF3bkLl4DqN32MxelPpTpSJ7HlyAKbZtUfOIqSohg9sTdNPfpqqsUCzGSMaIquhPCKVfJ_e37ICVAhCaZYM7xAQOUjFf5INeKHPkm-nvxAKZHG8-BaU_QKcOa5Svoi20mUGwbKTUuq51_tH3C3yXjcJplYbs4nnURjaEi0_QbETe6f1CQJkn9_-E55L1Dtu6d-t-x0jUwEesEC0Qx-dCNUFa2zdG5ZZEwHo45XJLSOaf4nn2LFpYWpqqnYV4JODw39LxRcfPw4FF2CUHkP14iofB9dMIhn55FFo6PSiIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
دیدارهای جذاب دوستانه ملی امشب رو با آپشن‌های مختلف در سایت اسپورت نود با بالاترین ضرایب ممکن پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132973" target="_blank">📅 21:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132971">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
فرشید حقیری: امروز جلسه محرمانه بوده و سرپرست جدید پرسپولیس انتخاب شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/132971" target="_blank">📅 20:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132970">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9383ef4fbd.mp4?token=studeCzPy08njU-OJVgPzoYTTy9fxNoR0qriCeiLE_05oj3OPQ2SXgmYh7FFfLeXmpJIbIAKpLRXwUEr6IaY8E9RlwhymmqrYTTuKIikk55ohKl7K_Tk_wMlJf57CTaGupfm8O15KbrbmbKOZoeiVL2Hs25kwkY0_GvOHHJYx-3cLp5kJTWoCHFPaqRu8iHJ22WiG9RJGyBlMJtEhPN4567v0zm0fnad0MzJFDJY6n1XhVEWs2CEZ3HWoia8JupfK4XAuiSewBuNYh5-hpKRIbFiaGNdpexsDrfGzXxsgjRbWjz_JAXlDRRDb3JXwFm_2kNx2mjrfZAIP32cQoQ8mUtZT4F5_MPS1fIld5awaJEsK8bKCC266DT9URtSoy57EVsn5en2QjE-ZvdefYiCzSM5WfLgLxoh4l8YrDpi_aRDY5iGsdPmA1kjw4-KTLSyEQhOhO_SYMhT_n_uj7S5oOFtnjY8Nh5jnqvzEtU_3upRCEaxSzj-1KM0yi_iIxJvjhuDEB2L35-R9BsHM6CmL_o_2HnMZ0lgjNKP_z4bMwmb2DKlb0LoPKAMzYzdSOcBjpiPUQbqb0ZJCT7MujjVbWyd3i5fswQ7qgKtyO5xbiEQ3PDEVw_F4puXiXLNCAOH-8fdYOi8NSK4ebDhB4WJ8HNv7WtzvD36qS8xr68qRJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9383ef4fbd.mp4?token=studeCzPy08njU-OJVgPzoYTTy9fxNoR0qriCeiLE_05oj3OPQ2SXgmYh7FFfLeXmpJIbIAKpLRXwUEr6IaY8E9RlwhymmqrYTTuKIikk55ohKl7K_Tk_wMlJf57CTaGupfm8O15KbrbmbKOZoeiVL2Hs25kwkY0_GvOHHJYx-3cLp5kJTWoCHFPaqRu8iHJ22WiG9RJGyBlMJtEhPN4567v0zm0fnad0MzJFDJY6n1XhVEWs2CEZ3HWoia8JupfK4XAuiSewBuNYh5-hpKRIbFiaGNdpexsDrfGzXxsgjRbWjz_JAXlDRRDb3JXwFm_2kNx2mjrfZAIP32cQoQ8mUtZT4F5_MPS1fIld5awaJEsK8bKCC266DT9URtSoy57EVsn5en2QjE-ZvdefYiCzSM5WfLgLxoh4l8YrDpi_aRDY5iGsdPmA1kjw4-KTLSyEQhOhO_SYMhT_n_uj7S5oOFtnjY8Nh5jnqvzEtU_3upRCEaxSzj-1KM0yi_iIxJvjhuDEB2L35-R9BsHM6CmL_o_2HnMZ0lgjNKP_z4bMwmb2DKlb0LoPKAMzYzdSOcBjpiPUQbqb0ZJCT7MujjVbWyd3i5fswQ7qgKtyO5xbiEQ3PDEVw_F4puXiXLNCAOH-8fdYOi8NSK4ebDhB4WJ8HNv7WtzvD36qS8xr68qRJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: زمان توافق نهایی در متن مذاکرات نامشخص است و پایان تحریم‌ها به آن موکول شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132970" target="_blank">📅 20:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132969">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f750c48735.mp4?token=jySBQaGT84Fqm95YU_hOxNOML_tIK6sXk1XbN9AOMaGYlYAFa3yig-9wYDHROdBHeWN-yi8btMnD7_v1_3kZeXBsJCJdLwJjmxae0SGTCb_VK83beX87wnzc7MpI07oy9x9e9ERekZ_Y1A4a9126hji7QY0Ij3XUdCCKxepGNfjSrlx1uNeSn85zpm8qXtjIu2zDqXlZXiDrM_XYrWNXhz_-wOV0WB3zubo6dTaeud0QmOADLC739TfW-nscVv7FFaH8ETyTGYbYGxW3UyLkx8bIkNRnjWgCPqNTRtBWquoHjDL3tmKYtqs0jKGd40wKZpvFWRDFdggVgSDZq432MbFkg50AnLGcsG5E5m-sY--r_pjvXWDWXJ0PwQcmSZzN5GNf0mONpSO0MDu1KECC6MWoy9dNjK6JfUxGswS9o3fEQ3wkxHeHgOc3iaLVrbwLeJZRKYWVA_Zb6QAJqOWXRRC5qV4t-L7yI5A9OEb9mcrztZK7zIAghKgX_z-YzRqNrUvkL-uVL24dcZ5yuZkI81Eg-jkd0DuGIVuOuP02RjPqgE4KPxEr9c9ohocjDXD5-0-mjWvYkX6J1nhQyVCpuhO77w96i06OGRkXfQ9MN7Scm4-5ny1Oiffnrfu8uTyq4fnkBV2vypp4u0UKPB7rQPj70IFrZAzznkmf3wkZEVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f750c48735.mp4?token=jySBQaGT84Fqm95YU_hOxNOML_tIK6sXk1XbN9AOMaGYlYAFa3yig-9wYDHROdBHeWN-yi8btMnD7_v1_3kZeXBsJCJdLwJjmxae0SGTCb_VK83beX87wnzc7MpI07oy9x9e9ERekZ_Y1A4a9126hji7QY0Ij3XUdCCKxepGNfjSrlx1uNeSn85zpm8qXtjIu2zDqXlZXiDrM_XYrWNXhz_-wOV0WB3zubo6dTaeud0QmOADLC739TfW-nscVv7FFaH8ETyTGYbYGxW3UyLkx8bIkNRnjWgCPqNTRtBWquoHjDL3tmKYtqs0jKGd40wKZpvFWRDFdggVgSDZq432MbFkg50AnLGcsG5E5m-sY--r_pjvXWDWXJ0PwQcmSZzN5GNf0mONpSO0MDu1KECC6MWoy9dNjK6JfUxGswS9o3fEQ3wkxHeHgOc3iaLVrbwLeJZRKYWVA_Zb6QAJqOWXRRC5qV4t-L7yI5A9OEb9mcrztZK7zIAghKgX_z-YzRqNrUvkL-uVL24dcZ5yuZkI81Eg-jkd0DuGIVuOuP02RjPqgE4KPxEr9c9ohocjDXD5-0-mjWvYkX6J1nhQyVCpuhO77w96i06OGRkXfQ9MN7Scm4-5ny1Oiffnrfu8uTyq4fnkBV2vypp4u0UKPB7rQPj70IFrZAzznkmf3wkZEVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: بیشتر پیش‌شرط‌های ما در متن یادداشت تفاهم با آمریکا نیامده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/132969" target="_blank">📅 20:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132968">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
🔴
کانال ۱۴ اسرائیل:  ما بهتون داریم میگیم اگه ایران بزنه، از الان باید تهران رو تخلیه کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132968" target="_blank">📅 20:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132967">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132967" target="_blank">📅 20:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132965">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
اعلام سخنگوی باشگاه پرسپولیس محسن خلیلی بعنوان سرپرست تیم انتخاب شد  پ.ن : علی بازگشا توی مصاحبه اش از واژه فعلا استفاده کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132965" target="_blank">📅 20:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132964">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7496233f9e.mp4?token=S-ab-9j4H-S1I0xezOvxz6MqIacq7WX4re6SMAQRTYoYVtoAPlbX040YbiXXHOGpXewUrCCn5NeZPQBgURQ5bxVwycpzR5qaEer6G_-Q-biWyrEPORZpGZgLNRpRF02bYN1q1chcFlqNQvGgy-jD68cgDzSpnHs7RinBFFiitSpeOmTY_2E-GHtzot2PHTE3oYLU7bz2uDTOUjByDG9PsApqlF1Y7mhxcn46icfYA2ug3-4nh9tcsjIaSLQyDcjg7Ts7u0_2xCYGrUp3yBgTMwZ1Rvo7kKa84gwqAlCytm1P-sSo_eWh6S3G8DBMEC59cPC7CZ0CTnomN7688OpsFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7496233f9e.mp4?token=S-ab-9j4H-S1I0xezOvxz6MqIacq7WX4re6SMAQRTYoYVtoAPlbX040YbiXXHOGpXewUrCCn5NeZPQBgURQ5bxVwycpzR5qaEer6G_-Q-biWyrEPORZpGZgLNRpRF02bYN1q1chcFlqNQvGgy-jD68cgDzSpnHs7RinBFFiitSpeOmTY_2E-GHtzot2PHTE3oYLU7bz2uDTOUjByDG9PsApqlF1Y7mhxcn46icfYA2ug3-4nh9tcsjIaSLQyDcjg7Ts7u0_2xCYGrUp3yBgTMwZ1Rvo7kKa84gwqAlCytm1P-sSo_eWh6S3G8DBMEC59cPC7CZ0CTnomN7688OpsFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور پرسپولیسی ها در مراسم ختم برادر حبیب کاشانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/132964" target="_blank">📅 19:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132963">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132963" target="_blank">📅 19:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132962">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
سروش رفیعی به تمرینات پرسپولیس فراخوانده شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132962" target="_blank">📅 19:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132959">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e27207295.mp4?token=T9a1RP2eM8Uhu0QqBuknHatm1jN8IC9RQOwHh9527rZznzRHBEbwwQ_TZtVAC2z_PseWUMuqXZ6W5QZBOaM0d_NOGucqgrqGhyZXE9jc3v77F_9-yYwfOqHdYLIyqqoMvOIIQf17LPVGIpXiiPw6-tp54RXFrBAca8suGg1uymQCCd2hL7umzVLhlh9xlF7pszG-LoAMnCn_KOm8Byqd4Zbx9uAM922h_pZ5k1uoYjSl1vz8vlRxPv-5gzb1C_1r9HxPxMLTh05VitRHlykj8UWeUqFhSuSl0QDQuCgBEgwvF7BcM4dYCkzVtBGjTe2wYyqL-J2QE84KPmFETDAktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e27207295.mp4?token=T9a1RP2eM8Uhu0QqBuknHatm1jN8IC9RQOwHh9527rZznzRHBEbwwQ_TZtVAC2z_PseWUMuqXZ6W5QZBOaM0d_NOGucqgrqGhyZXE9jc3v77F_9-yYwfOqHdYLIyqqoMvOIIQf17LPVGIpXiiPw6-tp54RXFrBAca8suGg1uymQCCd2hL7umzVLhlh9xlF7pszG-LoAMnCn_KOm8Byqd4Zbx9uAM922h_pZ5k1uoYjSl1vz8vlRxPv-5gzb1C_1r9HxPxMLTh05VitRHlykj8UWeUqFhSuSl0QDQuCgBEgwvF7BcM4dYCkzVtBGjTe2wYyqL-J2QE84KPmFETDAktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
🎥
ویدیویی از ورود تیم ملی ایران به هتل محل اقامت خود در تیخوانا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132959" target="_blank">📅 18:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132958">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/132958" target="_blank">📅 18:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132957">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
شورای صنفی نمایش، با پخش سه بازی ایران تو جام جهانی در سینماها موافقت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/132957" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132956">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB3-NpEcCOcsj8R5rqm-X46p4lJyT5-y_v80o-NBTocaq-PJlUyIh60HSmRVzGeVCimyimT_nCcPBC52J0iqqvs1Um1y0oMWh8g-ZYvQAaJisG_Rk2OCRtSJhb7PxLD00zinzqI1e6Pu05h40tHe9HUM8n2iT3wrEyweflt0iAa4JxV_7QFljSMmfmIensl1X5ML1E1wuQ_6HTNT98w7exrfHo2tuY6E-VAMNlU9-SDLDLGuZv-DIVd8UiX9vcFxnXk2kiJvULO6tqCjYVB66ceAqjTuVNgWgIPJbTzIKDXNqRgnb5tH85ykumYzJJ0zzvz5Q3OWX5uFINboKH65bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
PulseGate | اتصال بدون مرز
🔥
اینترنت مخصوص نت ملی
⚡
سرعت بالا
🎮
پینگ پایین
🛡
امنیت بالا
📱
سازگار با همه دستگاه‌ها
♾
کاربر نامحدود
💰
پلن‌های اقتصادی از 250 هزار تومان
📩
ثبت سفارش و پشتیبانی:
@Winstn_Churchill
@PulseGatee
⏳
ظرفیت برخی سرورها محدود است؛ برای فعال‌سازی سریع‌تر پیام بده</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/132956" target="_blank">📅 18:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132955">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132955" target="_blank">📅 18:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132954">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
مدیرعامل و رئیس هیئت مدیره پرسپولیس هیچ اطلاعی از سرپرستی خداداد عزیزی ندارند و تا به حال جلسه‌ای با او نداشته اند.
♦️
اما منابع دیگری به ما اطلاع دادند خداداد عزیزی در روزهای گذشته با شخص احمدی مدیرعامل بانک شهر جلساتی داشته است/شاهین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132954" target="_blank">📅 18:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132953">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5WNCb3kWk05PLS7lEf0XpEvjrAoRWDJXVX_Z1E7CFT9yQJ4CSaVmtNm3E2V-wwgr6iCH1lOJiY_ihY2EzQoJnTYDbdP8UDUAKe8YIQz5DZqegQC2nw_N3XQJozaqhB8lbma2jBM06ixGZuP08vDgcJitluv3vCgX7mmp5TA8wGSXr42Fa7YOL5wHvDWi8-uo8KIBOVhVqOoXsY3uwRiCDewcVW-9mHFKA29a94rBn9-8F64kCnDL9XbApVflHAhjS93ESPpPz4n32pv-YRBuzcolpKlextX6Vq0puQimTg4I4DdedYZ55auNqTuU8FYotEIObf1qmrPOFemZK3G-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:
اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید
پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132953" target="_blank">📅 18:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132952">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
مدیرعامل و رئیس هیئت مدیره پرسپولیس هیچ اطلاعی از سرپرستی خداداد عزیزی ندارند و تا به حال جلسه‌ای با او نداشته اند.
♦️
اما منابع دیگری به ما اطلاع دادند خداداد عزیزی در روزهای گذشته با شخص احمدی مدیرعامل بانک شهر جلساتی داشته
است/شاهین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132952" target="_blank">📅 18:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132951">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
🚨
برخی منابع معتبر:   خداداد عزیزی حتی قرارداد هم بسته!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132951" target="_blank">📅 18:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132950">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
غیررسمی/ خداداد عزیزی به عنوان سرپرست جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132950" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132948">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
یه سری منابع معتبر اعلام کردن که با وجود اینکه محسن خلیلی سرپرست موقت شده، خداداد عزیزی افغانی سرپرست قطعی پرسپولیس میشه!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132948" target="_blank">📅 18:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132947">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvWRjuN7hwR3n3S9rf2QPG9amiyLQpepkqedd4JP1elshXEPmJiN7j3cerFAant-7CpIuJL2Cs0t2zdXR-SIBp8G0ylcHK9BZxkeVfPEkq5uBsqQECEd2rErvwzevcQ9m0DFLbyi6Shx41IcwH5PayLUuDUdV170F3q3hMVzRBKzDhoU2WOwMbDDUhEgU9voWDG9xzygTrGNsKLtqheKUUUefn0xo9itFkZjzvZ0wplfdqoiSndE1GiMFWuXEVcEZZQNxY8PyRPXptxb3JC2y92jIdDZLtztXwRQyeh_Z6AtF6HgYjDWeo_JqXRORlO3gWmACCoopZo_R84RDJgZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه سری منابع معتبر اعلام کردن که با وجود اینکه محسن خلیلی
سرپرست موقت شده، خداداد عزیزی افغانی سرپرست قطعی پرسپولیس میشه!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132947" target="_blank">📅 18:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132946">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHfEOSqskYHMKyCcfYctLMJWasJUehanVQHOMyZ4G3xhB7dvNnPzFzW0c8DMxuY2MbMcX7y_2WZcABnOwtMkTJp3CmJMGvSUfdPV905_wLUbjl8GW2ypnXA_mRnUhzjXMb2kiOH4GbAIr-QtPtqQ6q2q56iP8i-K2xD_JlblVMac6qyw6ny9EDNMSNxlI6Q2dJ_Ix56NAv2dtlW6JX5q08OZiPQTCSPtjtzcGXFQ6qBgcDeeGM0Wylcf0zj2snIq20fu2CUAcVr8yV6uGRN6T4lBmBHJCZSQpIPBmi6XFRp6orwU9KGF098V7ns-nnYTkhYJngboA-c5JA4eBvwu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مارکو باکیچ در حال گذروندن کلاس مربیگری در سوئیس هستش تا مدرک A اروپا رو کسب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132946" target="_blank">📅 18:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132945">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
👈
دونالد ترامپ به NBC گفت: اگر با ایران به توافق برسیم و روابط دوستانه‌ای داشته باشیم، با همکاری یکدیگر اورانیوم با غنای بالا را جمع‌آوری و نابود خواهیم کرد. تجهیزات متعلق به ما خواهد بود و این مواد را یا در همان محل از بین می‌بریم یا به جای دیگری منتقل کرده…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/132945" target="_blank">📅 17:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132944">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
فووووووری و پشم ریزون
😐
🔺
به نقل از فرشید حقیری: با تصمیم بانک شهر خداداد عزیزی به عنوان سرپرست پرسپولیس انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132944" target="_blank">📅 17:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132943">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
🔴
ترامپ به NBC
🚨
:
🔴
مجتبی خامنه‌ ای بسیار زخمی شده پس شجاعت خاصی در این است. بسیاری از مردم ، اگر آنقدر زخمی شده بودند ، درباره این که وضعیت ما با ایالات متحده چگونه است؟ صحبت نمیکردند. ذهنشان به چیز های دیگری مشغول بود. پس شجاعت خاصی در این است. اما او…</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/132943" target="_blank">📅 17:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132942">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/132942" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132941">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
👈
ترامپ درباره‌ مجتبی خامنه‌ای : اون منطقی‌تر از پدرشهِ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/132941" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132940">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
فووووووری و پشم ریزون
😐
🔺
به نقل از فرشید حقیری: با تصمیم بانک شهر خداداد عزیزی به عنوان سرپرست پرسپولیس انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132940" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132939">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
فووووووری و پشم ریزون
😐
🔺
به نقل از فرشید حقیری: با تصمیم بانک شهر خداداد عزیزی به عنوان سرپرست پرسپولیس انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/132939" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132938">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
باشگاه پرسپولیس معتقده مجوز حرفه‌ای چادرملو مورد داره و تایید شده .نیست و با چادرملو بازی نمیکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132938" target="_blank">📅 17:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132937">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
ترامپ به خبرگزاری ان بی سی: ما می‌دانیم رهبر ایران کجاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/132937" target="_blank">📅 16:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132936">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/132936" target="_blank">📅 16:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132935">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">💢
ترامپ: اوضاع با ایران خوب پیش می‌رود
💢
رئیس‌جمهور آمریکابه خبرنگاری که از او درباره آخرین وضعیت مذاکرات با ایران سئوالی پرسیده بود، گفت: به نظرم وضعیت با ایران نسبتا خوب پیش می‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132935" target="_blank">📅 16:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132934">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
❗️
شایعات؛ خبیری به عنوان سرپرست پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132934" target="_blank">📅 15:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132933">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
با اعلام مهدی تاج ویزای ساعتی ایران بدین شکل است که یک روز قبل بازی وارد آمریکا میشوند و بعد از مسابقه خاک این کشور رو ترک میکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132933" target="_blank">📅 15:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132932">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
✅
حسین خبیری مدیرعامل خیبر شد و خبری  از اومدن به پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132932" target="_blank">📅 15:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132931">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
همه تیم در جام جهانی هستند تو این دو تاریخ  ..و باید بگردیم یازده نفر و پیدا کنیم و بتوانیم این دو باری سخت و بگذرونیم و جواز رفتن به سطح دو آسیا رو کسب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/132931" target="_blank">📅 15:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132930">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">💢
شاهکار پلنگ مازندران مقابل شمیل ممدوف را ببینید؛
رحمان تا ۴۰ ثانیه مانده به پایان مبارزه، با نتیجه ۱۰ بر ۳ از حریف خودش عقب بود ولی در نهایت ۱۷-۱۰ پیزوز شد!
✔️
🥇
رحمان با بی‌رحمی طلایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/132930" target="_blank">📅 15:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132929">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/132929" target="_blank">📅 15:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132928">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❤️
تمامی بازیکنان باید تا فردا خود را به محل تمرینات برسانند و در صورت غیبت غیر موجه بازیکنان با جریمه انضباطی مواجه خواهند شد.
👍
دنیل گرا و باکیچ دو بازیکن خارجی پرسپولیس هم فردا و سه شنبه وارد تهران خواهند شد و برای این نفرات نیز بلیت تهیه شده است
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/132928" target="_blank">📅 15:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132927">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgUr08yPg1Uc11ZENVD1tTXgABUWBMXlD5kLQKSw21tGkqMZjCanY_jJ9ItL8J8ybKcja7nP0s3NexjrhMhsxuVVD-_YRAXVBs4euF3caT6z1z-bgXh6NZNkuiriGRmTY7SA9vTxHofKviZ2mC8KWgoYLvhNN3g4zY0MXFt3Stzp7AkTYbFYsegZosDzDh6c2yPc2mLoLBx_r0M_db9aAUyZTZM75DsCFJ6yiLgAwcpy0Ldqr_VcuHWk3Dw-KNIqXXZ3OSraWJXyO0N8vIi9RbYKRLsN_CX-3cozy4hRMwxDUTFep9MOJwI55Im7hDfB2txaUF5CbptKcDB9mfalfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/132927" target="_blank">📅 15:34 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
