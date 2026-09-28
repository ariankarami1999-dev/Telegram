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
<img src="https://cdn1.telesco.pe/file/LwlM1CKz1pbO6rPiW6KUfoSh0t8Hp4f7RSR212ONpZGWlaxybiADK5IFzIQxwhcUKsaPiTZ4Wu83NVSGO2O8iRZIKDhAVdDT9Ni-esKw4iMOHfqHpSgLWg4BHBLiSM3ivPWlZtdbzClm2LLTItHLw0WNbrSmwzDfHgWzS2CERAcfy6vdAgdgA4iIqQGv6SAD_3znhp27eAS5ImVVYFpAR8kbgfvVOjBu1Ojac61ur87U51BMq8DHRWnEIDzvs1OGNAnG2jcIScCxuYdmnXdTJH9W0NNdIuXxUjjwvMGiXpOHW1Lq1Bi2ktzRQDMdZMI5Oa-tqpLNKvW0yx31eGwwpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 12:39:35</div>
<hr>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jNaeZa7Ub4Lc4fYYQJbFiAU6ETMjNVujGHfYjGoV0P4UDWmAdOpI4A3qUWoXEJC3I8-312bSeKGJ3Y7-cHS6CRINR4Dz66wSYJe7LX3FUG6rk8A13-REPLequf8KoDoFU83Qzc4sEOWjR14ndVbCActniY9sy0VZQZW3T1BKlGOrQBwKpyiub3HBX9ycDtv092aCCoAlUrwE20zDxT-eniugP_8otC7fAwalLIDp_5uN1bHZ2HjXGXgbvlc8YdmJ_rIf8dIo3UXnBF9y5p2B8u7S-wTJZg9VtlMm8j0R_79qODOHLwkzHia66eyft6umv-DPS--aHK1SLi_ImlCP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUZBDvoFdXEvW2kiXUxN_Vjfx0Sue80srTZVW_EaNugU-U4N5ZccocKhKCgxNyuxjzJQ82M_S0ZiST91DBtSt0CJkJF-vSu8PH46pwTVtDO6fjqEkuTZciSxPCzVFczjFu1fBC5jnumx9Itg67IDtEOdlBT1Ikr5bkBAxUVaVbUrydmtD2jWLwzuRmmDb11l_bTZXbtsMK8_B7Rsi_tLUecdii0PL0_FuFWwkzXhBMtK8LrK97ufl_a2RUqYLOhyugMh611mILd5ynWE1R39v5TxEG0WKBtFa-Th5511s5musFZhLI08tfJQ1z2I5duvgD57T86WSPDp8cYvuWc5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EJDnZVq2cQrN9Tj7sHAiq1xEwu2iDDL09yS2IzWD7JqqNLUBmb8DIG1rEAFtlpNCdmdZhPtleAHIO0cNPiQJ44C2vZblBTrAAyGPFnbWpMxXoySTF2I2G057DHM0YEB8W_g37RkRf9XT5IOvxGUtva4ZI-s-BU2Z-A60YxuFH0SqJ9zrpucB4U34LJUgpRjG9gDI77iIxIjLbTeXpNaW91DUeCEAvb4Tg7BiIPLJRWDBTA9UWPwk8mcEXDs9PO5-_sEjw7R3u_dkNpczFXieYyjs3NxGsEciLyg0B8ZvSSxD9hbzQmRoiTycXatCn5k71_SsZ11vv8KtdpPTtyZAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkszzl0HrLnr1iByFWt3152Z9Ve-XFnqSQ3uAYNpTfZZgQEF3gBsr-xEqUiBpqX0mhb43PuUuM9bcPmIKAdI0EYilX3IcVfTuzhpMzO2VJlWpLvRaAZX0XHIJCIm5y_uzHMa_syFivgALSPYH83v37WAxDbtng0yT-mmPc_rrM-RhwZjy2ijd86nRBeZlBROUrt4s0Bvo7lC1yQ8xpPsOfM2AQJDft6upZO3kECRNqshViqMNssWnyp63AwqUQ-FpA55ANUj0y3OfFsDIBkz3VspuB3kzdKYl88HN6wJzPp455qDM-HnTTfTgelOE-gYsr9UpRMnChC0ptLX2u9pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=qt95u7mYANfssZ7Otx3mpoHjQiQJXNvFW5JGQuykwCxP4q7sTpX_hkux-6mF3cxIhTXG3HI3YMQCfbqBrM1u8zTmOuToRbSXEEyBuCTr-PeWatrEk5dJYJwE6qOpFexLrUj-0Gu3SGlOA5kxPHx7c7woDTjOEUW89bcgsWhsIB6nTQzSq976LujSR3B6OJq5UFc7PhQ4kQ9feMAbJP9wokuG98AZgFSNLzX7Wkpc682vn6-6C0FyVltYdqxSZCtj8koEYAiWxncWIpRvC_sC-GTGtQuVploZPkr4nFsPmw_OBIsLhcdopImCJAUKxmlEfz3-xLhnWYeArn5W10sT1Z7k_XIg9RlushNMg8njBZor_gMA_QhfBIJ1woMEi5WlXRyro24So5PxskxHZyf-Yb-LoDMkZxLn5_ZMrvXVprE7ZIQ9niv0U90zDKx8bbqw3baQ6qYP19wq_qSvmMVx5Y9hHRmXJ9Y5ECx04f3fPizkDUoFSv-ynVLICy7fkE-xRL76pFkQB7exQFiG4wAwEozgU7tXctZQe6gqF1yPkQfMJ04wwhhTQ8Oq4XVXQAxFHLW__toLvprk2wjkJPVW1x85w4FaVk2J1fGX8yF_i9OoHG7HMEVIn-HQPU9i7CRW-ZNb4-yZ0s6ODChWqUhTk7booa4XgQGS05-7jnxE9Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=qt95u7mYANfssZ7Otx3mpoHjQiQJXNvFW5JGQuykwCxP4q7sTpX_hkux-6mF3cxIhTXG3HI3YMQCfbqBrM1u8zTmOuToRbSXEEyBuCTr-PeWatrEk5dJYJwE6qOpFexLrUj-0Gu3SGlOA5kxPHx7c7woDTjOEUW89bcgsWhsIB6nTQzSq976LujSR3B6OJq5UFc7PhQ4kQ9feMAbJP9wokuG98AZgFSNLzX7Wkpc682vn6-6C0FyVltYdqxSZCtj8koEYAiWxncWIpRvC_sC-GTGtQuVploZPkr4nFsPmw_OBIsLhcdopImCJAUKxmlEfz3-xLhnWYeArn5W10sT1Z7k_XIg9RlushNMg8njBZor_gMA_QhfBIJ1woMEi5WlXRyro24So5PxskxHZyf-Yb-LoDMkZxLn5_ZMrvXVprE7ZIQ9niv0U90zDKx8bbqw3baQ6qYP19wq_qSvmMVx5Y9hHRmXJ9Y5ECx04f3fPizkDUoFSv-ynVLICy7fkE-xRL76pFkQB7exQFiG4wAwEozgU7tXctZQe6gqF1yPkQfMJ04wwhhTQ8Oq4XVXQAxFHLW__toLvprk2wjkJPVW1x85w4FaVk2J1fGX8yF_i9OoHG7HMEVIn-HQPU9i7CRW-ZNb4-yZ0s6ODChWqUhTk7booa4XgQGS05-7jnxE9Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nFPhlf536hfQgUFvlC4reP6RC0Ladv3AUk02SGscUfkzzh4hR-uxksV9vcZWYEmLWy9J6AdQ7DFGrZvcFrAP82AuIZw2qg8pLipgxKEvKdvU2mKghHgCKHg_R-zelV1NRO1H5R4WCMHjE-mWRzq8JS_61Vb7bvQasPXVo6QJ_AT7zRtdzg-KCZD6nH-hLpNNI9KhbxUz4Sd09JbGnGxeZCaur1Ib9AQCc8anfsgLJur2RimsWFz8PrHq4O6Uj8QgAf1GxL5qt1oziy4UeBgl3ik0w64j1QzhmpYPLwuWSmJ8ayb1-AB4MmxY8Jv6w9xOQJtZ5IrGQ4rQJDuKSPy1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBnwhx9CTHnDCQFBOPxKyo9vUXe6CRzAWKTv9ACYndUndGZklZ1WQrRyLSkL45EzVm9-cZ0Cw2kMvpGaE5lpQtn4E1RfqXUUQmqKo4_7VTb0pSSiMS9_Ik2On7-4vrvRVMoHOihv0_zNTHyGL8M7LI0yVQz6oCln44WBRESL3tBLWodYhU69OeckD-OYch-PB4Fpwh5Br-bdDEohUn8uVhcmFt5bAPka2dSrlDald-wbgQw9HC6N7S0VGc8kUVpjtiCqk_NXG04JS7DVahWrLFeEuTdQrWnLqf_NmEiFYx_2fszKSPQh1F6a8vCJBxk0UTYgb2RV29vcIxY3udVWmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YCdde2Ia6XvCfjGUgPOXvybKiHWz5HhOCbbj6RJaBFQ6hH6Rrs0BRZJRsow05ROwe2izgYTQXJeLoooisaWo2kNOfr5LZAbTuCIYJkiFpHX6TODxnyE772FJg_1r7MFjnJoA3AnUm7ue74I7pSfeSn2uQsIOZ64mM1ar63xSLXxbjuBxT5WUI6vPorkUa9VajvZ6MUOsJo3iPmDfQRJMBAVtlqFEeKUJzbW2HmH2bHDrHvNYjQ_gdm4PYx1uTyzu9oSeKPUOPOf27oE8oDl3ovvWDjLXrzovUr5JPJxj25gQWIGwUY1l-2-in0HfZtI7HYyZl_iPlIxM3i8Iof3mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPRonpmAaqHc1-hBS7NMhpK0Msh514716LU-3jAePdVENUZ0mvxnc5-kMxJjgdZK6Q-TsFKTAb5AMtqgB-Xy7MJUnr09FyKmsfWdn6icOluFiINk5dXBJ1Cw-W03S-s2PBc9gsxobS4gnz-O5i-7Y_32Dv2xrpArlZLx_pB0Ndy4HKgReqVcBkvY8mw8hNH5TGAm87tmU5mAXcqnnd1XA_xJ0piMurEW9zTy32nd9tkmS4XEx_z6X_Gqt31O8NZQ9U1cK3vgc1MZqs7dA6OY_5av2nb1iUEagG9pvSC41Dr8btpH-OadSE1J0i1HdGetKjFEwQf_reyxXsiNb-XdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A3qedbjlstbjOBESg6sWEdCBnKbOrCky_bJ_SZ89S1sP3CQVx_swIig_xSN93gE0xoKAxUqVtJG0D5Riy-BLASE-iaVXmTbWmN2jSmVJQ1F09Y_fzPsHnPKQhyK1mzO9OYa7LTiHW96uFyMRO1yuaIBaqM_v5plTszfyphAExBlnoxlTd5Ji7W7xkt71Dmqe-AlDUp_Sstpa0Pr9CeiVM8RjESKeaf2WJ1EcDQqmfdhNTqCJdVgXvW8YqnITaRgMq71N_49u257Pv_2n-_KExKPspy37M8Dz4cSM8zSfXyQ9x0GZEIKIDKMUs8QcgCzU-OKpFqJlQYDuSvaU5A97eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qAIYadfcu5VLUFR0NqUamqzk1HIoEGKHJtwiMoGP2jg4_R8kUe-pP9x_GrkHHNQUb20dMWts7SvME3SlnYmCIw9ng72jnxIk3XUxwN-oOBtP9GqvRw-a6U1szZJ4-XgED5jLlqaf8NAeuDoCB5T0_Er4FJPYtj15JPJzefQ_1ApyrkRlZeWMbFMOd4L_gvKVKAPeNfEkUu8nsbHI84x_y-7P5q3sPeZvlqP2t5acCfDwHIue4PAMVGfvY9jBsnEGZcTdUAXlSmRcdg_7BNLWHCGj8KFtyshXq7wKfX-FAhxZVKGGEfWeMJXgpxcs0OAH95mlBZ3gUgHF7ai_5C2hZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=OYWLMjj5tD7h6YYJX9tcfbp-VhWPffBztvwHuEZpA-5WtimBlrn3rXF995z-krx4ubc1T_1543xNKim2p4dJEq13-DYpmLjMoW0OqRx7vZC0LrLsFTZ_mK8sACUXOhOEBoKyYcHOEmNz5ShzdALhSBc9uqLSresRDL3XvoUxkoA4UqSI_oAH8syXzqmQVYQwR-CbA2Nclh1qmOTdu430QMNF1GiJ2ySO5YnsjlnHYiH_MnqK8JAgXRKDQ_27jqE8_OVqnCPIDhEVj78M48QnDBIvW4he9TYPDvBM3Jkgm_xuFYf0hyC74majhuUtV2-Nn_YfoHoycZ3LiZtAWn7xxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=OYWLMjj5tD7h6YYJX9tcfbp-VhWPffBztvwHuEZpA-5WtimBlrn3rXF995z-krx4ubc1T_1543xNKim2p4dJEq13-DYpmLjMoW0OqRx7vZC0LrLsFTZ_mK8sACUXOhOEBoKyYcHOEmNz5ShzdALhSBc9uqLSresRDL3XvoUxkoA4UqSI_oAH8syXzqmQVYQwR-CbA2Nclh1qmOTdu430QMNF1GiJ2ySO5YnsjlnHYiH_MnqK8JAgXRKDQ_27jqE8_OVqnCPIDhEVj78M48QnDBIvW4he9TYPDvBM3Jkgm_xuFYf0hyC74majhuUtV2-Nn_YfoHoycZ3LiZtAWn7xxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NcSZHB0wZZCEPWsKEW6xFEuJIsu4UyqIIabGwFqag4_eZ-snAoJPj4Dn5JXuwVV95iYLJ1ZmpTqkVHqATmmCCXeWBOQqRj75rKl9iy5bX9kko_nl0fkSouDKqaeGxUTfi6gpp_mQ2u95hPLcW2jAm2Ran0pSxYzLmYOtsH80H-OsBwhvJWOBkkgvn_QjvGxrybljBkx9BDOAMLdXddBJok0hTAil5_IZEkk6ki7tOkjKv_cePlcBQDP5fbTUX_RS_fkUJpEQR_HQmj5Dte0_Zxbdv8y7ur1r5RJ_mE81GCvLNe8hcYf2wIdDk1ugr37UX-Xe2zNIXwTBhk_iojLGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Oc-OmdIEmc-fCFDPqKGHtbuGDNDu2_vxxpDMNryIA5rtD9WdYUQkAived4uEDt_7GXXEplwZ7zJ9A1iR9IsoUd7eMZ3851RRwwL0yoOpsNlVL4cInxZ0TaWmVcc2jO7UHO5daLZnS6GiPTn6pd2m358IvyX498p0bq1msItyI3RRABMuRCCU9dwKKQQjmiGgMCCFq2U9Icv3hZfbiGPmdGHlBJ0NZpGW4y4KUvTAs_jOJueJxzRHjJvq5JASwlMp4Cr1IN-a3GTiKjyUxx92Kanx7Qe3aV5h9sLloIf5xJN3wEstcAwbZSZjrkt04AIs8HFOvfgJeB0oTL7U3xO94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kSnzxRfFCbwhw1rAYqxDXQh781gtjn24EpyuTDczkkZKhJSHGu3TXrw27CnTfYmQe-ewD9d5OpS4MSQsN75MoiVniTrgl0RWiN5DMZmZAP0hWEAbVtGVotV4lr9IEHuHuyCC_oU4Kbx16nP_pmcMtCoFz22H9RoeinB1rf-pmWeZjrne7SvlKQIiVDNRpQ2QaP0mG0vmAYrlnPG95GOk6qO9GxOoshb57yzCWwUeBxWNjWJ7_BErHbos09FqrncfNr6T3huOplEYbnHsWUwNHV71AOXFNlCqdBygdXAKc8OUqTv0e15apfe6hVbFw5PAIoc-SI4Zxx9t9onep_zS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vkzb7AaG3_jZJ5srsX1E3IMPAlQpWjjkUCvaRFDuUEvi1nsbXAMMxAi8n3Et40bpLCBaMMwisPN_FWFF287AVIHkM58MF6fb-HyTGEvVu5ypXIVFJRgBP5Uv3hg4StF8EbUymiKIxShKkXqhGRE3_Oe1pTvwW8triVbbgTjkhCICjpLvZx54Y3Sk8iRq0n0XCVarZrfIStALlIzLwzt3CFtOT8Zc-YwDBWhENgCoweSpizQ6P1utY13ZPjqskTNbH5XaYCmXcKLvFz18Ynbl2IkYNbXrFxBe5EqtahpjMoDbPfqO8tLEXPRCio0WMP8fANbtfm7Y_sWll-owg2obNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اروین از توییتر
یه سایت بهم معرفی کرد شبیه به Mpay، اما بیشتر برای بیزنس‌ها یا کسایی که تراکنش نسبتا بالا دارن؛ با قابلیت برداشت مستقیم از کارت و کارت‌های تبلیغاتی برای کارهای حساس مثل تبلیغات گوگل ادز یا تراکنش‌های سنگین و گرون
از اینجا می‌تونید ثبت نام کنید:
https://finup.io/?code=MATINSENPAI
لینک، رفرال هست. اگر دوست نداشتید میتونید کد آخرش رو پاک کنید. برای شما سود یا ضرری نداره
نقاط قوت:
1- برای ساخت کارت، MasterCard داره به جای Visa(شانس قبول شدن آفرهای رایگان معمولا بیشتره)
2- قابلیت برداشت ازش وجود داره به ولت کریپتو(هنوز تست نکردم که KYC می‌خواد یا نه اما توی مستنداتش چیزی ننوشته بود که احراز می‌خواد یا...)
3- آدرس BIN آمریکا داره
4- از ارزهای مختلف برای واریز پشتیبانی میکنه برخلاف mpay که فقط تتر داشت
5- دو نوع کارت بیزنس و تبلیغاتی(هزینه‌شون یکیه) که کارت Advertising شانس پذیرش بالایی برای کارهایی مثل تبلیغات Adsense گوگل و تیک‌تاک و متا و... داره
6- کارمزد رایگان روی برداشت و تراکنش کارت‌ها
نقاط ضعف:
1- هزینه اولیه ساخت کارت 10 دلار هستش
2- برای KYC شرایط ثابتی نداره اما توی تراست‌پایلت نمره‌ی خوبی داره
3- حداقل هزینه واریز به خود کارت(نه ولت)، 50 دلاره
و اروین گفتش زمان واریز مراقب باشید از صرافی‌هایی که امریکا تحریم کرده نزنید. ترجیحا بریزید توی تراست ولتی، جایی و بعد بزنید به ولت این سایت
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZx2btAIQ0h-JHdM4CoWex3PhpEC9zYwMu8aMowfkmVtkFSKMzE0gD5wLIOGr0ZOXBK76TQqG4TFTFKKOrSTlYLv4EPeHsc5jRSIKhhU0ZDJx4yKfef7ShuE3SLDwQvZWFZtbfxEPYVA4xx27uCLFdQzlBdJEskjMGGGudjs_6phzOrzb0L5CDZGDpr2-avaqLjAqO99hNTsGabAF5Pt8HXkNiTifg_RJL8yQoSUC_piyNn9-GZwA6JYQFu7WVUfP4DPUqFdtW94gfOTinISxnIeV9wjEsTKBfmkIDALL78MKDU6YEkpWhE2IIHJ8DXqG02Ih2HwdlFWMYXXUR1Wi6h3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZx2btAIQ0h-JHdM4CoWex3PhpEC9zYwMu8aMowfkmVtkFSKMzE0gD5wLIOGr0ZOXBK76TQqG4TFTFKKOrSTlYLv4EPeHsc5jRSIKhhU0ZDJx4yKfef7ShuE3SLDwQvZWFZtbfxEPYVA4xx27uCLFdQzlBdJEskjMGGGudjs_6phzOrzb0L5CDZGDpr2-avaqLjAqO99hNTsGabAF5Pt8HXkNiTifg_RJL8yQoSUC_piyNn9-GZwA6JYQFu7WVUfP4DPUqFdtW94gfOTinISxnIeV9wjEsTKBfmkIDALL78MKDU6YEkpWhE2IIHJ8DXqG02Ih2HwdlFWMYXXUR1Wi6h3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=V8AwdZa7x6eKnt8GwfUKO26PxR6nIvb_cjt0X0wyAqwqSvq7IIotn0nnvIHDZYyc0PFgJJxdf_SYR9He1DW2J4teWuy5eTxB6O0BkzSl4cSGtLYlasQUgJL8deAXSSNH0EsySREdCe2E4rb5ePsVn-gv_WDY1ug_1Cf1TcYyXrgXE0CfeTT6NYX5gfuOsCBXmimTUHO7BqPQDN6NoigptTUv8BQXa18D0KcWWudH0FPUMTKFTdAryfQFkoPcrhmWwLD5iUxKPDmk-spe7_THED7nvrqaFtmllYUQ8ePlwhzJacwa5wXtWzi3HAkxnxc3hmNduKEJ2KOpmP5CrWZhig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=V8AwdZa7x6eKnt8GwfUKO26PxR6nIvb_cjt0X0wyAqwqSvq7IIotn0nnvIHDZYyc0PFgJJxdf_SYR9He1DW2J4teWuy5eTxB6O0BkzSl4cSGtLYlasQUgJL8deAXSSNH0EsySREdCe2E4rb5ePsVn-gv_WDY1ug_1Cf1TcYyXrgXE0CfeTT6NYX5gfuOsCBXmimTUHO7BqPQDN6NoigptTUv8BQXa18D0KcWWudH0FPUMTKFTdAryfQFkoPcrhmWwLD5iUxKPDmk-spe7_THED7nvrqaFtmllYUQ8ePlwhzJacwa5wXtWzi3HAkxnxc3hmNduKEJ2KOpmP5CrWZhig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_U7OPeoO31KUiiJMUWTtMykRjrB7baGijW4vGWQgi5PBtHfbNi4JR8PkB7hb5BfbiBq0FLJo44yf0X_Ltuudr9gcYBj0cbGGdFOYFy2_odV51hsd5nvfreyY558I1PJmQycL-Mlh-Be_M5jQZ3Ii5JJOT2jIOFcnzKiDAUfdIUU4OwqrFRF5prZHj0JYLO2Ajb9YyKvH_4nmu7s9icK2ue5zEW5cUX9_VCCkoHdyHw0_6HdaHRBeAPEc7g-Xsmyt_KqS7P8lIBfkcjhqsiZvsTkUh0r_IYfgvNV26Ev0IGkwduM9PiHqUM53tQ-CkqW4KshXfTXX6zc2KqJuPjoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YR4p1Ed5-S75VwSsPVSKTEun9qTq_QleOFHRIxb22N9KBdMZ-8UmMVesE5ycrRliiGjOt7UqAM4h3VyO1d94puc1arVjhXOdo9rxgm_ouMVC3hDgrhkXzf6oePEMNBZGiNIGmR-surnI44su-xHKwW3EOKTB3trSf26ikjzAhwJYZKeUO_HL9sLenuy2t3j0iSPFT7j_CwfobpZIAkrs0bNc677FRPDKc1cQ_WmWjjfgMlEIny7Eumm_DFFt7XeLI6oTzjFEKZxilYiNH4xD4H8YO5h1huTYsjg5B6gMMCGpiUCxcnPJ1VhOYYEND6Zcb6Gbd0ZLulDP_ojELgDiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">زبان‌های برنامه‌نویسی توی عصر AI چی می‌شن و چه بلایی سرشون میاد؟
خوزه والیم، خالق زبان زیبای Elixir، یه مقاله‌ی فکری نوشته درباره‌ی اینکه وقتی ایجنت‌ها بیشتر کد رو می‌نویسن، سر زبان‌ها، ابزارها و کامیونیتی‌هاشون چی میاد.
چند تا نکته‌ی خلاصه از صحبت‌هاش:
۱-
کامیونیتی:
هر زبانی دور یه سری سلیقه‌ی مشترک شکل گرفته؛ پایتون «یه راه واضح برای هر کار»، روبی «خوشحالی برنامه‌نویس»، لیسپ «تغییر خود زبان». وقتی دیگه خودمون کد نمی‌نویسیم، حس تعلق به این کامیونیتی‌ها چی می‌شه؟
۲-
اکوسیستم:
فاصله‌ی اکوسیستم‌ها کم می‌شه، چون پورت کردن کتابخونه‌ها یا پیاده‌سازی الگوریتم‌های یه مقاله با ایجنت خیلی ارزون‌تر شده و زبان‌های کوچیک‌تر سریع‌تر به بزرگ‌ترها می‌رسن. ولی از اون طرف، وقتی ساختن یه کتابخونه ارزون باشه، چرا کسی بیاد روی یه کتابخونه‌ی مشترک همکاری کنه؟ خودش به ایجنت می‌گه دقیقاً همونی که لازم داره رو بسازه.
۳-
سینتکس:
سینتکس‌های خوشگل (مثل optional chaining به‌جای چند تا null check) دیگه اولویت نیست، چون ایجنت از boilerplate خسته نمی‌شه و از دیدش همه‌چیز توکن ورودی و توکن خروجیه. به نظرش زبانی که ادعا کنه «برای ایجنت‌ها ساخته شده» و تمرکزش روی سینتکس باشه، داره حول محدودیت‌های امروز مدل‌ها طراحی می‌شه.
۴-
کامپایلرها از بین نمی‌رن:
اینکه ایجنت مستقیم اسمبلی بنویسه منطقی نیست؛ کسی نمی‌خواد برای هر معماری یه نسخه‌ی جدا نگه داره. تازه هیچ زبونی توی همه‌چیز خوب نیست؛ Rust، زبان‌های اثبات قضیه مثل Lean، Erlang/Elixir برای سیستم‌های توزیع‌شده، SQL، هر کدوم تضمین‌ها و سطح انتزاع خودشون رو دارن.
۵-
تضمین‌های قوی‌تر:
اگه ایجنت کد می‌نویسه، می‌شه trade-offهای زبان رو بازنگری کرد. مثلاً type inference برای آدم‌ها خوبه چون نوشتن تایپ حوصله‌سربره، ولی ایجنت حوصله‌اش سر نمی‌ره. نوشتن صریح تایپ‌ها اطلاعات بیشتری به کامپایلر می‌ده و دست زبان رو برای تایپ‌سیستم قوی‌تر باز می‌ذاره. به نظرش زبان‌ها در آینده با این متمایز می‌شن که چقدر تضمین می‌دن: از طراحی‌ای که حالت نامعتبر رو غیرممکن کنه، تا تایپ و اثبات، تضمین‌های runtime، و تست و fuzzing.
۶-
دیتابیس برنامه به‌جای LSP:
پروتکل LSP برای IDE و آدم‌ها طراحی شده و با فایل و خط و ستون کار می‌کنه، که ایجنت‌ها دقیق دنبالش نمی‌کنن. پیشنهادش اینه که اطلاعاتی مثل سیمبل‌ها، رفرنس‌ها و call graph به شکل یه دیتابیس با زبان کوئری در دسترس باشه. آدم حال نداره برای پیدا کردن رفرنس یه تابع کوئری بنویسه، ولی ایجنت راحت می‌نویسه، حتی کوئری‌هایی مثل «همه‌ی مسیرهایی که یه مقدار می‌تونه nil بشه». برای همین هم جادوهایی مثل monkey-patching که کد رو غیرمحلی می‌کنن، بیشتر مشکل‌ساز می‌شن.
۷- در نهایت
Observability به‌جای دیباگر:
breakpoint گذاشتن و خط‌به‌خط جلو رفتن کار آدمه. ایجنت می‌تونه سریع کد رو instrument کنه، trace جمع کنه و اطلاعات رو کنار هم بذاره. پس باید runtime و state سیستم رو جوری در اختیارش بذاریم که بتونه برنامه‌نویسانه کوئری بزنه، حتی روی پروداکشن. اینجا هم طبیعتاً یه اشاره به Erlang VM می‌کنه که این قابلیت‌ها رو از اول داشته.
جمع‌بندی خودش: زبان‌ها قرار نیست از بین برن، ولی سؤال اصلی عوض می‌شه. اگه دیگه برای «آدمی که کد می‌نویسه» بهینه‌شون نکنیم، برای چی بهینه‌شون کنیم؟
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSzUYE4rJKZg8OXbsrgY8wsUS-YdDg-5cXVC6FHGuvc8NLFnHWiiB1eN0Oc-L6DrVQTKQTriC4F7-HbNTbSsE0ymE3u-kAR5e968orkjt0MYhe8-nl3WqrZqnv530MdeDIrI6YLNAZyC00WREMWula6g30ifASdYttowya7tjlZaWKtEW4UwR5e77POlF_SmVJnzezg087n1CS22aBSY8-z-qnKFVgFVVk5uvEI3cjqk7R7NOeRpTuQZYN_vc7hD5wvgLov9a7RVbs3x8WsDD7emPdDj7HYe-dIQTA__xQbCn_mtOlGISyh7aske2RqOORpqPWsz26UWcWyGWTR9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TEqnQHWRfozIvjvxv126XUBB2ebZK8NtbBo6k2GxsKuZo3o_uShztdMMl1tutfk27HvYHC0YOmfoVy-SpsleClO-lZdI_MMbTMMh8Z4F8UtA7iDm0_QoXbSq22gHy0b5JXtrDAMnynKQXjJHRjuuns5aG7SO5c9QkeiTRE_UkgbUweur5shSSbEatBAtQ64ONnfDsMx0uKn09joPyRjJ6JD6ozl2Zy0fott7sWo4ewE-6kYVrbVXvvBIegxKyFBIzOWD2z09DK3de17OVSOZ3xWSGuTvapzKdSp1zip4CpdLufmRENWgaMzs44YSXjPUqpCURTSnWo_LMwzvuWz2mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPzRkRbq8Kt5U7chEkBCXHE4oBLhxvEe-tAR4itvz4n_nsWE_-_0gAnNt9EBbhf2n87EJuUsddouwOBdcaqhh_xW4trkRCGLcqX5n3FxQXPLlX1Xrt2P7yxHKR-Lty_yZRdhgN44TwmOSLsta_MuBB6lyKBsT5Clz5DRxFkKu_paf7w5eZ0wAkaC7Bxk73hg96jrEXKR4uOxI5hCYUk6FPwh9a4SFxwdspl4za0AnBfwP0jGNnkm5IWWraSTeO1U8D311xRSBw69nFkapypd7eZnp5ZsOgUgdScwJO9CcCqeiuIZodIfiupKAncrKorbFzj2qIl5FW0ciqcINJvIng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oYFv6yldcZ34XCDLNI8NJWWhvf-schQofkE_fHKUMyo3GKQmELm1sUc1Oc2MSxYrtf-MGJ1774GrhliVNYcgQAtbsggpOihIUig00mdq1ni2lL1Eim6cgLCimTvxHzxy7WY78LXbu7KyCWck1gMB6BTbrM6JKDAIWVGPLuHAZx6Kjjt7YnkTmbdRcaGzzgzbet6njjv0g8xw5QA3rGhK1EYQD51XfgrJS9fxaSBfLx6-9_hdIlYj9L4Bi2B7maeb6_k9Fzs9w-r8GAuw-5yOIfNxWmGjUmhe6JvvlTUg9zv1RbMgaYuh96PO8axFzm00xdeLZULleWdz-gB9a0QZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxoMLtm7CTymW_r2JZlt5Qa8dFSpDxqQ078KF2ULVBoqKaDc9qNS0kuVvkoZ84-O4iYiV2ZroOK7PdkTHm76Hk0olnysO_6d6CMxTT8hIFC8N6oieGOrSGuolNKY6r2B2DUWtEROS96ZCkqXC-ntMb4VceXMn6Iegy8cD0s9k-zOFQpamB597-sQQ4xfMNh5BR8e80eWd7uLK7RXdTfnMUP7c6KobF96ZAazjBBRnJqtcUOQfAp8s2cFgUOXqdK33sb4I1u8VwLMjrVYKBaEF2G9nRzouxMDgqp4fwugdRnJvvmg9GmkLTC0APzIYow-epxcZJrfdivKA6ggcMfEcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/si75zl7hHUECk8OOi3JUjAG2JfRuSApfmKYiSBI4eHu9HHcTkJLyVYyDKH4F2hgloXfMNYcd3K75uOq4TiiQqoDtDP_AO41-EzFzvflKhXaWXcwRo3-oEWP0X62CS6I2O1frA2JW6LFRasAYnGuUgKLJmnbSijlPBKSk0Xd1EpcLvFQuRWvknvN6-kcwKg9SyOBXaejlQ68YScbPbepxFsz3GZlt37NPsaJ7zYZkRMXaymaNF7QszQLx2nAtAxWxbfatYtCz-aQ5vgNlWPNcZGquafYEeCfADkj1iRVrHvGfAlz4aBEOITzZtqX3vyd7MzWW8-S2MqNjIA4WZ8Ku4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=XM8K_yp8cS_endZEnXp45OnjN5CkchYcCeDgihOT7QDiHxZwx0y7N5jkICiTg0fwoE2hGgJRsJcWs2W9b4dfRmxkzDdBb0T28Wbh22FsrVnxuLVCtbFNAP_9ic4adjo40MaPp-P9FGRqViP5hTntvCCQNuvbtbgFill66-KgWTuIxDchlMRhU3wrGFQdkifsfsRnh_YQIrBvmr2_79CpEN-DYjllG0vVxYT3Neh4zBv6XmCM4H0pc7C_OKYYtgnEWuDP0Pfeu7YO5JPz9P-RYgtlAl80K7Dev9xC_NUBYmycZMWlpcmom_T9mNRsYC5W1hMeMOOwi90E4e7q_93BbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=XM8K_yp8cS_endZEnXp45OnjN5CkchYcCeDgihOT7QDiHxZwx0y7N5jkICiTg0fwoE2hGgJRsJcWs2W9b4dfRmxkzDdBb0T28Wbh22FsrVnxuLVCtbFNAP_9ic4adjo40MaPp-P9FGRqViP5hTntvCCQNuvbtbgFill66-KgWTuIxDchlMRhU3wrGFQdkifsfsRnh_YQIrBvmr2_79CpEN-DYjllG0vVxYT3Neh4zBv6XmCM4H0pc7C_OKYYtgnEWuDP0Pfeu7YO5JPz9P-RYgtlAl80K7Dev9xC_NUBYmycZMWlpcmom_T9mNRsYC5W1hMeMOOwi90E4e7q_93BbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، Jev از زمان عرضه داره روی GitHub منفجر می‌شه و همهههه راجبش حرف می‌زنن؛ و اینا چیزای باحالیه که مردم تا حالا باهاش ساختن و شما هم می‌تونید بسازید:
- پروژهjev-trader — ربات معاملاتی واقعی که سفارش‌های limit زنده روی هر بلاک ۳۰۰ میلی‌ثانده‌ای Monad می‌ذاره و فقط Jev تصمیم می‌گیره. ۱,۹۱۱ استار
github.com/jarrodwatts/jev-trader
- پروژه jev-ultrafast — ایجنت مرورگر که هر کلیک رو خودش انتخاب می‌کنه و فقط وقتی واقعا باید تایپ کنه، مدل متنی صدا می‌زنه. ۱۶,۷۵۸ استار
github.com/browser-use/jev-ultrafast
- پروژه jev-doom-agent — Chocolate Doom واقعی کامپایل‌شده به WebAssembly؛ دو موتور روی یک نقشه، Jev هر فریم تصمیم تاکتیکی کلان می‌گیره.
github.com/lukaske/jev-doom-agent
- پروژه jev-t-rex-runner — همون دایناسور کرومه که هممون هزار بار بازیش کردیم، حالا کامل توسط Jev بازی می‌شه: بپره، خم شه، یا ادامه بده.
github.com/joshlarsen/jev-t-rex-runner
- پروژه‌ی typesafe-chess —خود Jev در برابر یه موتور جست‌وجوی واقعی، دو بازی با رنگ‌های جابه‌جا. موتور جست‌وجو هر دو رو برد، ولی حدود نیمی از حرکت‌ها نظر اولیه‌ی Jev رو وتو کرد.
github.com/TholeG/typesafe-chess
- پروژه jev-drone — یه کوادکوپتر شبیه‌سازی‌شده فقط با دوربین مسیر مانع پنج ایستگاهی رو رد می‌کنه و Jev نیم‌ثانیه‌ای یک‌بار وضعیت رو قضاوت می‌کنه.
github.com/RomanSlack/jev-drone
- پروژه tax-doc-classifier — فرم‌های مالیاتی IRS واقعی رو با دقت ۱۰۰٪ روی ۲۶۱ فرم دسته‌بندی می‌کنه، با هزینه‌ی تقریباً ۰.۰۰۱ دلار هر صفحه.
github.com/kyotofin/tax-doc-classifier
- پروژه killmyidea — ایده‌ی استارتاپی‌ت رو توصیف کن، Jev از هر زاویه‌اش امتیاز می‌ده و بعد kill، fix یا ship برمی‌گردونه.
github.com/monteduro/killmyidea
- پروژه jev-curate — ردیف‌های Parquet و JSONL رو با قضاوت‌های typed با سرعت ۱,۵۰۰+ ردیف در ثانیه پردازش می‌کنه و فقط چیزایی که از حد رد بشن نگه می‌داره.
github.com/AkashPriyadarshii/jev-curate
- پروژه pg-jev — افزونه‌ی PostgreSQL که بهت اجازه می‌ده به Tableهای خودتون سؤال انگلیسی ساده بپرسید و جواب واقعی بگیرید.
github.com/realZachi/pg-jev
✍️
imryven
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O5DSeuLPz8yIw4AqrRdEqdGyr_5ws9y9viXy3TdVpLdUWKvglKFAOLRm5EB_4e6RN8Um5whLo1on2qpyWUCOnZMqatoCz8-1CvpwnEUrlWECPlJZRvaPbPkx-g-tN6vqqbmYlsUJQZyx-teqdMLh9wh1PNkpI36_2_-MuPECngLsH8wTDW9EjBEzJdRrypln42TMytybldpbNQ548S5rkhg5S39YfTa6vBHT06obg-HyhyQuyOv_5CDeyM8p8ss9cSo4nT5e8UguoSOhfZo7Pf14R1N7yZwTll5HSnRkC4-7kS3YEueRDoEHdinWLm2zMzxB6Bim4rgONst5bAaIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هکرها چطوری ChatGPT و Gemini رو کردن دستیار کلاهبرداری
🥸
یه تحقیق تازه از Vigilance Security نشون می‌ده یه کمپین گنده (اسمش رو گذاشتن Dark Sourcery) داره جواب‌های ChatGPT، Gemini و Google AI Overview رو مسموم می‌کنه.
قضیه اینه که: کلی پست و PDF و صفحه‌ی پشتیبانی فیک می‌سازن که با تکنیک GEO بهینه شدن، که هوش مصنوعی شماره و ایمیل تقلبی رو جای «اطلاعات رسمی» بهت تحویل بده.
تا حالا دست‌کم ۳۷۴ شرکت قربانی شدن؛ از Fortune 100 گرفته تا Delta و Lufthansa و Bank of America.
چطوری این کار رو می‌کنن؟
1- شماره‌ی فیک رو با فاصله و نقطه و ایموجی می‌نویسن که فیلتر اسپم نگیره، ولی مدل راحت درش میاره
2- شماره‌ی تقلبی رو قاطی شماره‌های واقعی می‌کنن که معتبر به‌نظر برسه
3- محتوا رو فوری می‌نویسن (جابه‌جایی پرواز، قفل شدن حساب) که هول کنی و سریع زنگ بزنی
4- پست‌ها رو می‌ریزن توی LeetCode، اینستاگرام و حتی PDFهای سایت‌های دولتی و دانشگاهی
پاک کردنشون هم فایده نداره؛ کمپین اتوماتیکه و روزی هزاران پست جدید می‌زنه.
بدترین قسمتش؟ Google گفته این خارج از scope‌شونه(
😂
😂
😂
😂
) و OpenAI هم گزارش رو بسته، به این بهونه که reproducible نیست. چون عملاً به سیستم خودشون حمله‌ای نشده؛ فقط خروجی AI دستکاری شده.
۹۱٪ آدم‌ها جواب AI رو چک نمی‌کنن. شما جزوشون نباشید؛ شماره‌ی پشتیبانی رو فقط از سایت رسمی خود شرکت‌ها بردارید
چون به زودی شاهد همچین افتضاحی توی ایران هم خواهیم بود متأسفانه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fydl3Kba4DOAdJxZWYFOrP9kN-_hAOp-_rmMurrkoOA1CCxL8AI6-GoCqbCg3wOLovnHSDHnr28WFyGqWQNy1c4ukyl2hKAiaCL4LXNOvQNSIRGFpdI51_156x_D18lKb6PKk974VKgeDideX3vmxSvVI43E1ijLANpbVtK6tbIORvN68gEenqXInH_o_wvFFaZ9VjR4wusWXv_85m1HZDbxJ0DiKc-7vwC8tOZtMxKurWV8A0IIWMm521VO7bEFk4ybjs8HACzfXhrkAgS5lBH_6JSz7VsegccJAmTLfJDrk9h-DDetNtzQzhC0YJkKVzpGuQqjDF_BX41v3yGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O4kcTaFa2TMr9Bx-UuKmQbhotF4gtSYk-eP9_S4xJ1BKDfOvslUxre4_fbwzoZXYjdEU9faOpbh0tknUuZDkjFCyEGyyE_Lq-hIZOEULH7bFdY3mw5cS_8VUBlMdtMhGXyRlS5swZWXWmYhuskJxmSfpDtnFypFrwFyWOfbJeMEmQVUPMHs9_ZBxJbpKPCtFQFEmegj5DdulMQV3aZUiyX5d-MT-mEG4ZoEZfaOe1pB5L76SV919gyc5xNY5x_KUv-bohnM3Q9WXXSSd9nZ2Boe6zgjaeXn-4SfIDc-_1tNb2BQon5UhQZ86nSn40Ba1X4wsEZNMFFu4HT3TuIMAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXwoFpi0FSHCmwVxrNE2x4-1mlRVc1mIRBYpfEeNAHvmXFcegYohtHk2GJiTl9iqc6r9b4K1Muuyp6wfBB-UNIE5DSeBl4ICq3dtWbif3sSLdva5bNxPXlkND0qsjO3vGapIXm6YN2ObHxwZYQ9TaM67CZBRexrnkmtVCo9rFfkY7_OaD4GX3S5NeTmYS937NOmrxe5BwXa4T3H7qmB1mngWb6NI4V8E1OQv8XvKIHBWE1F2dozMZe3qiNMZnAzFrNgiVSHIe8uedFjhWLf0hhf7nfALPdgmjnn90b-C_kWoyYWslY5neMck5ZLcWP1zRFHF8Klqv8RDViXn8sG04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=kpwYWM775msvTX3WWspchibgtqmAYIOw_bxwJCbqeVdT-SaszMwRXXlX6BqMpjRdEFm_rftRN4C99tv1GzpsyTY2YPhkvh49OK_LGbXE8qYO-wcc60NpctQ0FX3rRlpi6TgYjW8eJ36JYCZNnRuakPEICgfzKMpmnnTLZn04jwijgJ7MizEgZEkM-nLK60lcxae_83iATdl2qxwqjT7kVEacHKkFHDwT1KXdnzMfu_srnRbcDumBYKIiZetyQJ9cQLVa18pqtyVT6Cof6PrZ-UmDkX7FoKvBIVpHBTAwolcMPL8BDIC677o6dGXcoKRJzKgG3ruZLrpAPO8PTxJ1vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=kpwYWM775msvTX3WWspchibgtqmAYIOw_bxwJCbqeVdT-SaszMwRXXlX6BqMpjRdEFm_rftRN4C99tv1GzpsyTY2YPhkvh49OK_LGbXE8qYO-wcc60NpctQ0FX3rRlpi6TgYjW8eJ36JYCZNnRuakPEICgfzKMpmnnTLZn04jwijgJ7MizEgZEkM-nLK60lcxae_83iATdl2qxwqjT7kVEacHKkFHDwT1KXdnzMfu_srnRbcDumBYKIiZetyQJ9cQLVa18pqtyVT6Cof6PrZ-UmDkX7FoKvBIVpHBTAwolcMPL8BDIC677o6dGXcoKRJzKgG3ruZLrpAPO8PTxJ1vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mksLp_1Puyn0pHX6iNiKk7dQccCCQ_F0WRK2Hzoeayvc04d-oJNLG5UA_vIjEGXL6btMw0WACB-siiNKbiB216MOPuJ2C70EWaEN7aVWjO-W1ZzwWQL-FoznF0q-PbqDEQ00iBViSBaq1D4iivF7u0L3AD4IwF8rzLuNIxHQvsk2v0acHzRivqFVPfl_3xTDQkmgR3xBPYszkz-tLXwQ3jgFAYkjYmnh0yiaoY54Y6pIBkPKmwLM6cs94GFhbaMZP4Goqom5G0ITHJmX7APggYK7-5-lY5L0opo0ZGicDIi6Y_GEE1Lt4qvnW3nBADVvZb-tVteKtRJQcvBim9anAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=SNwsa3VD3CRTaPUzhiDg8shUD-EG3FJpBCKGjkfzEUixvCeR10iUBlpQ7zO7JNV6B8MonvahZiIH53ScXdG7_bIbffIA2Fns6Egfk0IJxGi2n6c1_Dl8Rx0y_GwnVPNPz2bzuL7VGS0zgYr2i8vvZw0FDqSOUhWazO9KMmr3wCAK59kfrOPGkLmxxU0rkuZKMmPUcY_io-QUwBKXwEkzwBfQJDomYJTE58SfBPkI5uKQZXRqI0FJJvBZhklnuA76CoD3j2GTVtLG7D3-LW8B7TdMsMT3kMO0JLxuCPNJACQTLRp82jAHf9w2BxOdEWhLEA8JKmCHM9brs5QGanDJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=SNwsa3VD3CRTaPUzhiDg8shUD-EG3FJpBCKGjkfzEUixvCeR10iUBlpQ7zO7JNV6B8MonvahZiIH53ScXdG7_bIbffIA2Fns6Egfk0IJxGi2n6c1_Dl8Rx0y_GwnVPNPz2bzuL7VGS0zgYr2i8vvZw0FDqSOUhWazO9KMmr3wCAK59kfrOPGkLmxxU0rkuZKMmPUcY_io-QUwBKXwEkzwBfQJDomYJTE58SfBPkI5uKQZXRqI0FJJvBZhklnuA76CoD3j2GTVtLG7D3-LW8B7TdMsMT3kMO0JLxuCPNJACQTLRp82jAHf9w2BxOdEWhLEA8JKmCHM9brs5QGanDJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugu97Ak8z9aieJlQrC9hrzM-UH9KVnI6NaHOlipN2hNkq4HfFofmOzBVH_6QWiGjmkV9UJ-4f1QZUupPrnAxgX2KBuwe9OTRB0rNA0Wmlqlm1_jSYQnOOOj3o-cC1GIm1JcOb7Jx-PyGtVjfeRhsioGGs9EGIaPu6VL9VGxVJ7nI2B7TQIGtK4L8ZemQ4G66bAwRTPmPmZfrQ9A6biVIZstyNZsflDdhJWIVaAgfpa5SZ6MTJZAXo_oO0BaHd9eweZ2vyc4kVEGURwZlHJWY5vLHEa_yW85_4ouTsMUXGhDtzG2vT8-maxl_XhNK0qN7O4jS3mVyaftaec8cWj3cYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aMjXCh-6e-eOkyaPvchYlYB9_5acj3lWJTloG0ozVwApyJJkByTqCCVl3QsWTXqdG5FFeEuBhdh6zt-wtdY1yV8oOOjI6r5vkQcFV_I-tKbJEzhTIOPXqOKVWQdEkP6fdk1NKBoqV1ae0L3TQOHQGGm8sOwfG207zzXBiN3xonE5_Rd60c2pU3s8e5_f-A8ECKQnacM7fv3upe8g9OWAF4d8aTV5AQps6ZeUrHY2GMwXfP6IXg3fLytLYL_pCTM2tjdEsYa6tW4o0dFsDzv-kSr2UMwf9eUuAAvLon9p9sy0eA9KwcEv_igAOUrCab-LHk1MtCx4Me0IHfuFvNOhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cyjm6s_1O6Yek3MJb5EqBf75JZNYB7Y8S06jkViGEmGyj44hSf4sp0zQ2ElfyfLx4EVws__m7OX03wnazggAWlGKzAQc-d0m2swJoFh4Mr6w7nm9p1ZYS2r-kmaMuscgvkfzHMIUqI1oNoq_VmR0WpRuf5126uFqse1ECmp_ql0d1njofnS-4PNV7a-XJXwpGnkJT6mQTwUDQ0qEGV7GtxLYA0Bg7DX6HrdaA3wNpVIv9wkKfpCqpaOafi8tAJoyZ-Ug-zi5nNLMuUY6bNyQBWw8iz-P7oBeRk26hF8Zj1gO3SNYOHvV26FKJgZOrCs5qSq34z3p2Z4-4cQN2RYGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F5QevJ1dhupagDKZCwMRCyRPqRMzIg4RrDuPb3iMXH0VcYe3X6jLmlD9WReZq8wDHUuL71zdwxM8eljYY_q09UQO4RwPT72fZ-KQpElWePlkuC8wPKgYTQpob8PKQkaNw1bl7ZOKAYaYoMznjfJrDBAvC7UxQRD36epCfVFkwyncCLmVPOPDKniRR7zDN1AyX3IydlKR6v-_zRCwm9yEHorgoLE5Dl3ygE1MtX2nCD7Yks-Kz7ecP9zLVO4MNI1MeqNd-lPyrQC2-KqU3ujC-j-UF1ud7LpsBr0qCk-owHiWd9HDyXzfuWlsbtb5zVrfwLsH-75mS8RuF3HdhBANyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UvReQdVnoj82vcC_z31Mt7E7ezTddiF_P4HBj6_RJD7aVH7lC7nxTX-u9p7tIzPcLzY_BCaI0kR_C2b1K6Tfo6LGzGPv6cHZlsy9cDyEuiodtACqLrmAKN5IcmQx26zTmVYLRhngN65GJhXJqKd62nVyHyrmHhiyiT10c8HSz28wq-nfs1h0-GqnWcoCH8JZkap1WBdGotuweoDOeQUGCTRJSgNYWJcDXzU6exmgrYFPs8L5IZYQUJdGwOrJd6TMM3hotncJoLcTIVi9oxsQfFJGWh9oizNwyXyCqoga_c5mOuDOxAdHfOb9TVGh0E5blX3yEYSWuJRhxBarinU-EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hWuvn2u8smGjbl_h85a0rpqNdKi02-YJBh9CAEfWE9Y5TGHRCZ155deHxBj8lZ2NV1848CUGRK8s7uMyzTqk1iybtOgPxk2Ud9qRb37nxOA5q0JENjJVsmWG1UdNCf2_WyfF8zAmp9LBbUF1sAqOuZShR3OWb_QUoQnncZaxnt9eflMEWB29v99Rw1Rk2gANaMLPxNSXpAIIJy6UjdtJFsXrJQg2o7cjMJ5j3nlb-Kp51VbEYYZ70PZOuE0Sqhrqv6qe3xro8rtMuP9qcrZNVjOokHh0XQaUZYrzIGMIFuv6JVO_q4vVBpsj9ns7jEnkAz_uI9_g6GFSlqAzmeZyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U7N3-C97c1-Fe-3WpxNAfQBujscuass8TxzGcu2_jwUDZ2LdaLu9BoqhV_wzZ9AgfapGzWaB8_9iNsHNjR-_27Zg2PuTGJtHiFPYcBMsq5REW2PpV07w8KVE8BA2xLUUeLTa2sNuqqjuLJmdrEizIAaLX0bo7yKsJiuz3W-FBmGWNNjNy18p3fpO7WvaBRIbvYapkH8DckelkZNsabb-C9dx93FsoeryOLsp53R3WJYW-8Cpf3e0h1ORLGteJxEkSiFqZlujlxlqxBhw55gl8HH46IP6PWWFWF-Mk5KYWdKn8Xcf-bNunmis-KNe5VZKUPdiVnVggDwzsyBzotVxbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UfB5eCe5Z7evwvKBlq7K2RSK3IpJLiC1yC8H8lRyF8FlPaoPavCEqTxACY9Ufdo5FQtNxLeQFFWC4-J4O5jnRQ4YXPqAVT8pLqUhFDJbNuJ3hCJQlAD4qAddfXA_PPS5SPsXJQfMH8CsvcojYPMso4vmC59ejSGsevBR-d5qSl7umRxYBogOGiX3TcM3cWnbxKz9UGaX1spa8NGyYOgJY2qJVMWKb5jXUV6OP0GT29cNA2hBV7QAmIjyCCPZdIOOVaWL2BMSilZGnWQRQS0Rz1ZP4bzaAgMGYMDFKLSH1ZRJD-n9f6Ort7sgPia4eWyPfVFYOqen6v01B6wzLz9Pnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bB9-Po7OuGXy1Tb7oqUOCKKWwWBlH_2-AgeIAtQc-BYqlsS6J7Q1PlH6d6fPPtZzAgwbwEhTvvjtdrZoycLhKobh9nfOTiF3kB-Rbf21PfM16NIoPW9xUHrYpNFvicaWIucpMQDqq5y7uvgAMg83qGY8di9J690xPWdRvvpzPs7gQh6rdgSaDc2UZRX7Cs7DUW4YH3UUnx1D1faZvifSvo8c5t2LlCdW4IbgNbOVuEw18o7DamWrEK--88bbRPUU9PZXVAbbjLeuNime5GlUdQ0Ad8w7ATO7ITdsCwjepk22pjMBm77ZZS5wgccA81JK9fAQxMxH0f_HeaVoBPZKeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TiOb4_usdVblqy_j2WVPrcXOw9g2TJLZPIoyIqaou1KgMFiBGbrEbIMmeIHYBUMskTbCL3LFuJxKLlEY0s7H1od1DmtbQdR28wg4Qxf6vOmo4KDgTYSNSMpMTPpmSapV_BW40pZoS4Da6ddiFyr-_HYJdxMCEKZPYbmFdXeZUgXEWkIpdcnvD16C_67lJibw6Pn909OWF71r62BkKGqr4t2SSn6v5t9mIghl5Kmc1cCH-RcKbB9cMtNA3c0fiA11U2lR0J5MtbyqaK6wUBhEMDy78wdi-g85PmMvmkSj0EYGYkJ81UaFH9zhwf9w438uqOpBTFwxwPyOluvMdTj1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y6R8nDunuh9eM2Wg9qoG84UmaJqhxeR85dzPVQBJkHJUgcMqHDW9aVpGNIUWsVGX7AZ1_PVn8rp4_mL-2DH9lcKm71pRLn_E4Gb1jeCKgNhDucLHHSdgHDQHWhaLGGeIMTHUCV4r1AR1FaP1NzxEqWLY4HDtZABiDWgLY_HNw-m9wLHt259-5AfzWcQCPVk3xjiqQd9DwRJ0pyrtUIinkxCpv9YM8FZb7Rz7IZIX36gxbSviMVChBkx_KMvMPB86B_FBHxMuAzQf5pI0uYbfzHvHF1OY7Rz16xtcWdUMaoNn8Qf0rjYDBDBMpoAGNoOlF3t9hQ7ZwAkhYgf4jnwK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gC_maVFH9mkkSI2qAfA12pi5YNNAvjeONo818IRINzzSXpV0_xLQHIyA7HDbuqT4Etg3LZjmjXLwETKmRMwgvLoI0KQ2cCowMTy7HfWT5CxxljnoxVmSYZfhgle0cWjsqh2waYy-lPQyNkhS9eq_y-TforarY9r_7d_Zq7Y5oV1GSQqvofmQPX3vCXHfO2pUJm0SvWpiAVXM8dnlCjptbPyHLkjCTfPtzn8L2SSX5G8iWvzJIvA_hqMVRjZEo5AbFpCu-KYA5BlnCjceg3anPkwj_9zK7FOObaRuSBuy58u3E4hjqISSbxsEFaTF-i-bPDGkdRDRe_bX5lXmPMJXWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MRkx09QdzSbY4qIgsCGnXvFKTqKyk8ftf73xpaUshYMAkiHDsGw3XoXhFzrop8C16I3NvhhApekh9QCfkkCnlmLVxkXOSKW-PH_IwQtmjbM3GbfFcBOS_W9INFEAFJ2zf1iWjjkyIeNCueJ_mUqZlN6xNh_DC_u6n676y2xf3mrBla_UKoKUPEcNueOwoNsx349spO4T7gN7ijwQJlxFgfj4nhRnUK_WPegLtSxTjS5WU0wF0wcKDE3TpUs2KOnuVjxLm-3FY6rB2YMREWPZ8xg7QQ65eyIHw8IVJIKzClbMZFF2CvQCZLmzIHbxg7Y8c_vbtAM0vA45jC9rB2errg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s89dfKtEMrv4nN9XqJ-3l2Tfn2RNsOerqAF8Hr7b0wjIvNT3-AWd8CFtX_3WsV9-oSj-Mn2unxnT8ANty-Pbs4XgBD8hTBtKo3xVV3j5RsZS7V5lbb2o6_M9UF0ILi_kCSGmVEgYbbyB5SIFHK_jViY0ZBAVSNRuIbzdK0KV1UZQa43osl_tMmYHpPVGJdGZhwvinibzG15RY-VEFPBe4XyLotE_azeNX35xtdt1EQcw2fxz6gpmZZc4jMr6RaOvx7tHWj31kGjZKsbhpYWz8e5aVAKypqp0WM-H6VG_J-osfqt94dyDnGNAebWHU9FJdPJ24sdhg4OIVssMcZuUBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pg5_n18ZpooQi39-P2kgMI5TqAUhWtIe9_4ek-TaB_IAsRglMqSO-hYYJXEOh2SqnWetNjgMG_5lzA6RtcTAmarwh97TX8fe1Cnsgor2hFoYqUKxp4T9Abe9m_MmuEy7oClar1Sa0r2dkv7X-_bjMWWrSkaUPXcYdSV5g1LgTVTIpSkP8qAPTLLoRue40W27vfeXJWUyAM9MjH8ILJLyBHFJrRi2ULvX31m3auROqrnxe0lgDDopiPMF1OJ7IiFTILWcR5TpqoU8lJkGbH_LQMSZWhso9nKuRnvX6uJSidqPwamUdTLSGUzEXbGjl6qMAfw7wyn_M1y3g1QRu9NIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev
توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev
از برادر کوچیکم دعوت کردم بیاد کمی راجب خود ماینکرفت توضیح بده و کاری که ادعا شده ai تونسته انجام بده.
همینطور در مورد Jev صحبت می‌کنیم و اینکه اصلا چه نیازی به این معماری حس میشه در کنار LLM ها؟
و می‌ذاریم ai ای که کدشو نوشتیم، ماینکرفت بازی کنه برای خودش ببینم چه اتفاقی میفته
😂
لینک سایت Typesafeai برای گرفتن 5 دلار اعتبار رایگان:
https://console.typesafe.ai
لینک سایت هوشیار24 برای تخفیف 90 درصدی API از GPT 6 Astra:
https://houshyar24.ir/?ref=B2N4W9SS
پروژه رو هم توی ویدئوهای بعدی که تکمیل‌تر کردیم می‌ذارم گیتهاب واستون
🥰
📹
تماشا در یوتوب:
https://youtu.be/l-o_fQM_9AI</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مدل
Grok 4.7؛ آپدیتی که بیشتر ناامیدکننده بود تا پیشرفت
ببینید Grok 4.5 نسبت به قیمتش واقعاً مدل فوق‌العاده‌ای بود؛ سریع بود، کارکردن باهاش حس خوبی داشت، قابل‌اعتماد بود و به‌عنوان مدل پیش‌فرض عملکرد خوبی ارائه می‌داد.
مدل Grok 4.6 از نظر من یه قدم اشتباه، البته قابل‌درک، برداشت. کندتر و گرون‌تر شد و برای انجام هر تسک، توکن خیلی بیشتری مصرف می‌کرد؛ درحالی‌که فقط یه برتری جزئی از نظر هوش داشت.
البته دلیلش رو می‌شه فهمید؛ بالاخره تیم سازنده باید خودش رو توی بنچمارک‌ها بالا بکشه.
اما بخشیدن Grok 4.7 خیلی سخت‌تره.
1-
مصرف توکن برخلاف وعده‌ها بیشتر شده:
گفته بودن مدل جدید توکن‌بهینه‌تره، اما توی استفاده‌ی واقعی بین ۳۰ تا ۸۰ درصد بدتر عمل می‌کنه.
2-
بنچمارک‌های ضعیف‌تر:
توی چندین بنچمارک، امتیازش از Grok 4.6 پایین‌تره.
3-
سرعت و تجربه‌ی کاربری بدتر:
کندتر شده و کارکردن باهاش دیگه مثل نسخه‌های قبلی لذت‌بخش نیست.
4-
هزینه‌ی واقعی خیلی بیشتره:
هزینه‌ی استفاده‌ی واقعی از Grok 4.7 بیشتر از دو برابر Grok 4.6 درمیاد و حتی از هزینه‌ی Astra هم بالاتر می‌ره.
با توجه به این‌همه تبلیغاتی که برای این مدل شده بود، باید بگم واقعاً ناامیدکننده منتشر شد.
البته بنچمارک‌ها همه‌چیز رو نشون نمی‌دن و Grok 4.7 توی بعضی کارهای مهندسی واقعی همچنان تجربه‌ی خوبی ارائه می‌ده؛ ولی درمجموع حس می‌کنم هنوز خیلی به مدل‌های سال ۲۰۲۵ شبیهه.
مشکل اصلی، قابلیت‌های Frontendـه:
عملکردش توی کارهای Frontend به‌شکل غیرقابل‌قبولی بده. قابلیت‌های 3D تقریباً وجود ندارن و مدل دائماً توی حلقه‌های تصادفی شبیه Gemini گیر می‌کنه.
حرف آخر:
این انتشار واقعاً ناامیدکننده بود. امیدوارم تیم SpaceXAI این موضوع رو بپذیره و توی نسخه‌ی بعدی بتونه دوباره ما رو غافل‌گیر کنه.
✍️
theo</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WPxAMpxC7Wd5pJqagrdfutdA6PzXst-_kLIEb2qG808Y-iJM_lSY9xH2mVClOVxP3CNBmwrA5_Za5tqk5BuXPCxh-TKjBwCB4lVRmz5WUXgXl2xoKQkAhdrCPVi1nxnKcwGC4hFEdoj0TcxO6VDLVvCoj891jjMKapmiVRZLiYGcjtwcckSbcdSq4O_DDmDp3NyEGa44KgSpNPT49ctt7CBNYHdX5cZgYx6NI19tacAAvdDenp_cUfrsDXNgJEueLgbv3aAeK90Q8l0yqvKGCx73832tjXunACM9_uPnMErkDf4oQ9RdtZ5rN5Awuu_cxCokHd-n6erZzurbMSAD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qKRV5706CxoEHhx97BofZpveIFLYZShit7J6ingFbFB8OsBvCa1aCwGQy1PEIohfZaX1ilMi4LsGtE1C1DqJ-bY5JO5k3vmE_hymmeuxd7KxbVBVzYjPPEzHJjw6puywHpfwnEN2HwLylt8OGDjS4i21vf1ZbsRJsal3ieL6DXRtFWVCDMBZrMBfyCq0xAN5I2vwg21VUejhvnUxdCccdQensPAimga5PTqT0boy5yN7Y-RgvhrEk2jTOTsz36yjbBRkYLBt8tIe7oX8_nF5EKT1XvHvIgxgG44Dj7NuucKPwuS80hLN3WlP9LGQ99tvzckwoxo72Zh-pjjjG-Om-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FXEcwoHuhUyE5iggc38ksR9ycpLWdtc91bkS7WkqqUM3jVgIwmbPy2wxwuXWHm_Jc-Sp27gecEDbwuOfiUKYu_Lh5EFCaJ1u2APXZCT-iYMC06JH90wLgGR8V0x6rdXvThxcjOjNtbnNyWvpeHLl1LieBxApVpUXBKdoYxwg5D2gr7n07i2T-hQ6F2XlcMp7x_uSNAoVPGCubsFbO4UIGMOP3upXuG2fxxf_D0BIfX3edRLnUdI4b307x6l5f9AtEkLHHyliwsOKapxlEkL7D5gKxYQpbRw3DO4n_XJv91Es-YSVC9A9mt8zktuFNM6sWy1PlbOWmYJ_I9m0GqYIug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WmVtpEZyv6_1orQO-Qzgj42SAUvQZ0_cq8jZNPcB6w6ONwWIs7H91WLXApDbzqJlZcF7CIGq6OgUFJk8kjcwVFwlwQUbk0yUFTE2hOWlWTDrsa9uU4TEHL0u5PYNgmtKMzBK4vF-zIZUE-XGJf9FWaNjQN5WxGeZH6b2vH7cUcDAEUZfYN1hI9mDvQ6iBJV3MeQT_GcC3jLmqkrKAKNUPxSAF755vDdzAYymzE9i5oZq3PmYB8oar0PINsc0StnkQM44ocdc3JzRGIPkRS_63OjfAOXWWovJ6pf7xTMI3NUOuJHhCMulnbNs30TysRPHRmbjfEB3UszCD5ppLvIFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J7m6sNNLPwcvdvrkLJyvKW3-Bl11UfyuJfrOtpCqfPzC0VPqNrvd8II7ytNXvhTCcMzSECkVcuNQEMPzsDHIoc0EMSi8AhoxetJ9SqVr_yDE5IP5IljhE1Y9ixQzzvVQSixTID3FP2ARjTcaWvrrvACbFt4SizpwCSLh-NwSfSaqRjwHYjTx9sYkFB-KqoskmwR0OzPA43wb2-aYob7aD4h7s0hPdWeITvrGN33SCNb-QNDLXeFXV-FG4I58cbcAML4rrM3zB7TNu46lxYmb-au79F4McJu_pBtcX4lUfyoFz1Uzdx2eJJvFZCUaKyBZ7OXaUgDsgTi_R7JKCiCiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cs935Kwhy4-fbwcJFk0EKXfOxnHRPIrtIkOFtnP1L_eVLMkO6uwIvYIcTccwvrbr41GixRzgKCHKUpS_gQ2R2b5cN-mfSNShWEOA_J9I7hN5FoQ-QoDMg_Xp05-QxdXZoeXLkGKwUISmbkmzcwi2URO-AeGwc_QQVF0svmUhhUUGM4kD7ntU4dHETN5vyAl8F2L5h7Phc1SK8ndW5vFntQNzUXxmCa8ubDNtaF7OoTZCqoFLFKGGA95EHNduvZsoXs3aasAFgAblyA7SWfF64xaPfIKuruUs41ThUa_qSnhL6BHOV1OfT4udswV6pcMp8r89dRAmhcQG01zBCq1eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwQg_LMujzceEAnV_9Uq9JH4odD7nQEoZq881u_R-l01W6GF4OMdF6hUFJ59UFYY8-OgZ6bBvAjB-0DPYm1LUIsHBJLeCt5ZzFjUou3fVDwhhkui2k1k8RbYa5ond79JGb4xfDUIQtoIHXf8DJ_A3RiS2SZTOm37UE1SZFCvBu8FNS-sB621Hz5JbxfeGQ1yO6nSBmtYQqyO-SLs-TzYcxP3ReJlshs7W4tA5R7tsFiGOZ3fuu4vajAOkxsgftnWpSFWblgvCwEiLF01t2_2RN8EDUaN8231h6AzpcaXMdIU9K7wjGOClpj6RTgNGVErTFz8Bld1kRHji53CXwa-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VoYFJkUguBKJESDEw54i9BOdlOCyan-erAiEXu0HvWmyEMxaO_UOE4g4vydIMPEBzl0f2UgNvgZS8357EtM665DzWSLMhjcn84K7_CW4TAMPE-Q2HpmynUySZPpgWYKa9pHwCtLb75OooqrVhr6krfcMzZwCj-HvhPERb4SCuu2GzKWFFEjIGcF_G2XTQj0LMk0DZ7gJDHgcrg9ZrBi-GBEAUC42caPlUDaNk-CeCd7OadSyqn9sRCwBafFUMSFp8mrwt3ZAd4WXGKnY6p6kvMR41U8ocgfhV2JgWZ4iXrIYEosGAcQOL2nZoGGkFUaTaZ8Gh8L4VhyCAmC9D-L30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ghAZxaHAjLgx6KAFtiZPvyV0AIaIYohg8ltFCdbS9jEwST4rmALCmxMJitbqEHlTipX_oxjdn0-aKkXhgp35ptWt3Kff4MJukLGwEFhahehdRiRLS1HzvsaOd6MY-dXVPVNBRKYGNy0chSWtvER6yvmB_eODJuLrhyqGRo3CU9-5I7QK1kD-9wgMtTfVMuEOrAyLx60X5S11OqCFDjxJnNcYhmx9wiDQy_UZhxTmSkEoNA4iZ6uYtJtg-j1aQFl8xC2DaXT1ZJvcWWcOBMFZj007Y_qZk6HXuas0iHXQsSjaoLLlJoh2Xx7MqYeGevW0CUft0HP154iU8NvdM1rmyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VIavA7CEtK1kz2DpfqUupzwC9kjHsBraT9Ft1mmEw6jCiTMN8tV2bM2r1-Xbm12or5OECq3kiozCEYCizJUpLJxhecboaRAFKhhIlyX07KwMquDb40j3lBJyzmayPr1tSAXnyUP-j4weH4CYXxWFNLo3iyqajZW1Vq-AP66PLNd-hDQnWjCgDiJCRq-3japyfX6YOg0lfPdI38Vj3IDQdtTYFrLokcqtajDjBpDhCWgZF_C5Z59PVtxJO0padvTLqUQCPsrbQEHxOrUie3fvA64z8lHilQZTrF27PcyBTYk-0GwFZwD52iqVbOa8YZLjqeG9UaLwsFMWRmY8Cw5k6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbFzB0zFlLcAfVPhpgkXvtVEBSev5_NJMHOhhYYOLQ5R5X1Jmo1Kil6ds-KNc8zB7ZFrAAVeZ-_gV_s3AtzMqc9tQihtLrV1RPDfCZK-W_yS5zv5Tyg7oLxiWWtnm4x5sT0JyBQ0_oT7BO3xbH0MuL40oeYG8FKcvjND7HnNSVOhwaGBRTEX2ci6m7Ax8fyXfC-bl5ETKH66zHp9-NVzllVANRFjwxkemGi3F6X-_a5AFsnZe0QvnY-fh4sSVZ-0YcTtttk5CxzNL0DrJD0a7j6yA04S_uF9QNq83hvGIKf4hu8n5Dxj6ERp1oK3S7LVB-FL8Iv6y102eXuIkj39dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=G2-bhIVoWScSO1e5vYsVzs_EDt0dNXoiyuZf0qOKZeMrAanLP-kbTB-W9a-TF3On14GLXldqNuHXUg_RQ4CNx7sWSZZu7JmUr6xS6agraoWAyZW3f816rCxmOXewaTQMoJEfHT8bBm9w2nvA128SXRhvFZQFJX_SjxI_Znw39R3FOUSSgeiTdsAsWycjVdv3Tin8G5ypjfY1ySBCQ6XfjsXEg2-2qGddYpMIxOGkwsqpWOce5qXh6HjEdl5xm0PUrDKJDnv5exDf1yMJfbwvnxfujnmgnPF2BqHvoGPmiYPnA0MMH9pJz_idJ4ABIqI8ciZe8f11aWVG01cDOcFxxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=G2-bhIVoWScSO1e5vYsVzs_EDt0dNXoiyuZf0qOKZeMrAanLP-kbTB-W9a-TF3On14GLXldqNuHXUg_RQ4CNx7sWSZZu7JmUr6xS6agraoWAyZW3f816rCxmOXewaTQMoJEfHT8bBm9w2nvA128SXRhvFZQFJX_SjxI_Znw39R3FOUSSgeiTdsAsWycjVdv3Tin8G5ypjfY1ySBCQ6XfjsXEg2-2qGddYpMIxOGkwsqpWOce5qXh6HjEdl5xm0PUrDKJDnv5exDf1yMJfbwvnxfujnmgnPF2BqHvoGPmiYPnA0MMH9pJz_idJ4ABIqI8ciZe8f11aWVG01cDOcFxxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=qF4SKX4gqdczxgIXRhxm5UFKHht6ko3jEBQTWbpaN2UA5HFuL7hyoZDRP9H0jbvd2qy_l6c0NJWmMiCB-VN0pyrhJtRshO8oJzNo4VwkZvc1CX5xKQ4k48gIKixDJ6zo9KBIn2EphVWNzxaTl1BOt4Je714RFgHjuGvNc7xbglQT_dSk9SDIxLYKW7S-JPSVA0yd6yhbnieRebtkoRw6x1RxBgJC2ALCutfFDniAKzUaz5LHz-zAdFhz6AdkHY1yaBLK1bRe3j4GKLbxPXaY55XXACPvlQXdfFDcQ1Cl7d9_nVfcVQlMx12U4gImYSFEZLn3k_glHLPYYZi6nPlm7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=qF4SKX4gqdczxgIXRhxm5UFKHht6ko3jEBQTWbpaN2UA5HFuL7hyoZDRP9H0jbvd2qy_l6c0NJWmMiCB-VN0pyrhJtRshO8oJzNo4VwkZvc1CX5xKQ4k48gIKixDJ6zo9KBIn2EphVWNzxaTl1BOt4Je714RFgHjuGvNc7xbglQT_dSk9SDIxLYKW7S-JPSVA0yd6yhbnieRebtkoRw6x1RxBgJC2ALCutfFDniAKzUaz5LHz-zAdFhz6AdkHY1yaBLK1bRe3j4GKLbxPXaY55XXACPvlQXdfFDcQ1Cl7d9_nVfcVQlMx12U4gImYSFEZLn3k_glHLPYYZi6nPlm7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o7oA0TeweQ5vnjx6nEHA1rUadv60fH7ULtoWylmrlwlUGEm2SW7oKccnGL12Vzm26nPEPtI7D3gkpVEQzS67v-scKRRLXR6E_POBt6H9SKIJSlbZKW12B8wGe6Z-MEJSeRGpRywS5TiHu5PGqD519PU30SzpU8rJQIbMaH7pdTUmYUbUG7sFvIVjxLNDWWiCosq-FbGBnyu2AMPTMu8M3pCkw0f5BV1LO_BTvSOecjil8jFuEWoS-ZSCldQAFBAxZuksMpJ3BCdzBZ6mHFfPFAS0Io5hdKEVULhPosACARQOwIkmgDOg5PSGv575eCz3ATRKEHLzPJ3o_3Gvbmezig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X3IBIUr8P3wNlwZ6v6G5UWaVKcPFvGknpox6yhmRULY4bwoCnwji4KS9v0_4gJDsTvh34P784WPP5XvwP0l0Atp2cLCMyCoyusAEj8H_Vk2bOVojiOkdE0lKLD8-oKV1B-k_NpaIeV8PdYmGcNnAGCIyTY-KB-83R-3r9dkYWfz8Wtub6nYcL1Sv0-7EOhm2W-ayTNlwKvVVtx1SapSR62gun_GZ2eTak1Lr1gTiv04oYMOs6mnpj-OZq8Ige6qK4zrLktxoZYfsHDTK1ud9MMrRxE9mZYSlyZKkUc_gqs0mh09OyLieslXTbeuzDY3uxFf8JEktQHYGa75NE3AbXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=B7pTkddN7-DAujJ0TQK9u94freGDgTAw7wkMSo5XXF07VpFdPuWAB8o6ShlG1qljW1JHZ7hPpmMMmNm_2Q51_1lq2GUZLzZDXhu5sLBimKWw5V5m3Ciu8TUmaMVm2dognsk3uFk3g54O7E3gtsZE6m3RFe7vGEdC8wvOtgNpQLOmx_8Uim4uFQFdkuDJ7UcI_2GIe5vYfX36widt3xqNGjJpUH69uLy_Xf_zaoSCsk8iTNK5m7uXS3A4_PAS3uXcGW34BRFsNGyPfnC-MC4abildaGMiZd60lib2FEKGfoBkZv111hjUHWZIvbOpMvULy_zwpMq4PgwJswSviDobew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=B7pTkddN7-DAujJ0TQK9u94freGDgTAw7wkMSo5XXF07VpFdPuWAB8o6ShlG1qljW1JHZ7hPpmMMmNm_2Q51_1lq2GUZLzZDXhu5sLBimKWw5V5m3Ciu8TUmaMVm2dognsk3uFk3g54O7E3gtsZE6m3RFe7vGEdC8wvOtgNpQLOmx_8Uim4uFQFdkuDJ7UcI_2GIe5vYfX36widt3xqNGjJpUH69uLy_Xf_zaoSCsk8iTNK5m7uXS3A4_PAS3uXcGW34BRFsNGyPfnC-MC4abildaGMiZd60lib2FEKGfoBkZv111hjUHWZIvbOpMvULy_zwpMq4PgwJswSviDobew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
