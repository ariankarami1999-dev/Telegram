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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 03:00:22</div>
<hr>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUZBDvoFdXEvW2kiXUxN_Vjfx0Sue80srTZVW_EaNugU-U4N5ZccocKhKCgxNyuxjzJQ82M_S0ZiST91DBtSt0CJkJF-vSu8PH46pwTVtDO6fjqEkuTZciSxPCzVFczjFu1fBC5jnumx9Itg67IDtEOdlBT1Ikr5bkBAxUVaVbUrydmtD2jWLwzuRmmDb11l_bTZXbtsMK8_B7Rsi_tLUecdii0PL0_FuFWwkzXhBMtK8LrK97ufl_a2RUqYLOhyugMh611mILd5ynWE1R39v5TxEG0WKBtFa-Th5511s5musFZhLI08tfJQ1z2I5duvgD57T86WSPDp8cYvuWc5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OB_UujMFo1f7iC-SrKfFYMlI6aWc6nvfLUaBjfT5fs5K_VclwxaDmMvKacTZxb0mG0fzYd2WkeFmK3X1zR_dBQag_fidBK6tdMO-eLN86_6vNlLcqigg1xqWUhHtLlwbDeEGVCwldyGuFsg3oM6R0EHs7rjgP_Kq11ef7wTMFxBP5cEzhuztdKSq8m_X6dbuOctEebu5kq_fkCP_SrCGfh2qHCQKh-lma2RTaEqu32DUuMp383b10CX0zxQi1lVv_mGTA6v46sfYA7LuQRPc3fBw0SnrhUF4zdznAT23v5MIU6IQs7IPBR7QwKGCQpKji5fi7aeypcy-baL0iqf2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=kXrPPH0YGPpgZ0p-aYLgycuuCd6TvXdqIFn4bLisYuubQK8gIKLqZFemmxj08RL-HlSOkOCOM8P06mbVU6km62NbdaZ5k6Rvckv6jlnOJGqs54GGMrOT5RSKmWng2vTlbths1lGtD_SEaDp-A0MB_zTBZ31_G3MUhEo6IiY8n0prNPo3Ud5zqcMzg1i09vevOW6FKEhzWQxhhubLzwoDU0_Fi0-tJu0OAd1ltRqctqxn3cJT3_wq6YWWqwViV5gl3aM5A04GgiW2MVqwA_l1w4NrDMGTMIieiPuD-GlqGlxKAju7snpun5-xTtDbjHytVQmS_fnTZsWbgBs_n2qVNRvTNumFqVIjOgVbt6RDUS5Exb7bAmFuv6mK8T6TaJniTKVxR-y0_wlF4fEnTDlQgtslXPFTsliPOLcfV454wCTZp5UcOvFMW70xDCCGgKOHlCdS6vQi68_vjT30wGR9z0_rjt3ZkHgsjpqyshJDnFRsVSA9JRW-szMmpdcKFPXDg3DplGxPbf-rCTLB1HJI7TJiKGt5gMJPBAstDLZShPAp_AJZVapoW6PDY_PDoIl6C-wkNa5fTm_PMWaJJ8MzL9BodMQ68qa7Fx-zotcec4qrb7_FouFwKz7oGpqakspeb_b-e2vV7EDkEDow7sMf35W5jxElq0g9nHwHsBfaTHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=kXrPPH0YGPpgZ0p-aYLgycuuCd6TvXdqIFn4bLisYuubQK8gIKLqZFemmxj08RL-HlSOkOCOM8P06mbVU6km62NbdaZ5k6Rvckv6jlnOJGqs54GGMrOT5RSKmWng2vTlbths1lGtD_SEaDp-A0MB_zTBZ31_G3MUhEo6IiY8n0prNPo3Ud5zqcMzg1i09vevOW6FKEhzWQxhhubLzwoDU0_Fi0-tJu0OAd1ltRqctqxn3cJT3_wq6YWWqwViV5gl3aM5A04GgiW2MVqwA_l1w4NrDMGTMIieiPuD-GlqGlxKAju7snpun5-xTtDbjHytVQmS_fnTZsWbgBs_n2qVNRvTNumFqVIjOgVbt6RDUS5Exb7bAmFuv6mK8T6TaJniTKVxR-y0_wlF4fEnTDlQgtslXPFTsliPOLcfV454wCTZp5UcOvFMW70xDCCGgKOHlCdS6vQi68_vjT30wGR9z0_rjt3ZkHgsjpqyshJDnFRsVSA9JRW-szMmpdcKFPXDg3DplGxPbf-rCTLB1HJI7TJiKGt5gMJPBAstDLZShPAp_AJZVapoW6PDY_PDoIl6C-wkNa5fTm_PMWaJJ8MzL9BodMQ68qa7Fx-zotcec4qrb7_FouFwKz7oGpqakspeb_b-e2vV7EDkEDow7sMf35W5jxElq0g9nHwHsBfaTHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wa_7S39YtpsQg8vggxPZ1iJH33WvuhrqFXU5TVm6ixhZdHp5yvhXJ69dy1b39q4DhU7mtxdcj9dvJlV_HPYxHeZtp7H_R9dyVhVt5QFTp9oaEii4k4yM_MHsHTnhWfHtLPZaZAIis_J9DxNG2f5RZa6AXO8M9uLUHWJ0TkSaY6yAxEA6Y6twmN16oUIkCEn0_BcrChMWTWWbJ96PvALUWLK5bpdPqnRc7z3-74a0SHxJdBKsEKESBLhocw_VK--pb9mVtHf4cP_u0cyX8A8gY5xdIgogVMJ5iJP_MjIafZ53QH-BQou2_9csVRxo_oSrfg0jZUygcmECDGpvRv440A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpDG2yUnmCRKO-DR9vwe-uroJTETdAEwwEX-G4CmTC7ccEKrficbIsqdY-2iAt0MdDMHG6ob38VDnr-Tq5EVS9OzKXk6WgyewPj9B3mDkRT5QjVBk0BQfd4JRyl2WuiDVbZHH7HDArjtmVFnrtxb6G9KUMgGYt1rJMCDL0UDiYMyDj4t2EMDcIbOPfR3FmndfHriXncMtBVPnjQkOyukB0297wivo3CFVfZaVPFU8ZPggfPqfP2r9zrf1k5Ut4gjXnA_WuJiZ5JqodlOKPTb44_4ucHvFhIdfhL3Fqr_dtWusLeYdMj6qicaLtoLXvoqW46kHL1mTqJ_L4wFLAs16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YCdde2Ia6XvCfjGUgPOXvybKiHWz5HhOCbbj6RJaBFQ6hH6Rrs0BRZJRsow05ROwe2izgYTQXJeLoooisaWo2kNOfr5LZAbTuCIYJkiFpHX6TODxnyE772FJg_1r7MFjnJoA3AnUm7ue74I7pSfeSn2uQsIOZ64mM1ar63xSLXxbjuBxT5WUI6vPorkUa9VajvZ6MUOsJo3iPmDfQRJMBAVtlqFEeKUJzbW2HmH2bHDrHvNYjQ_gdm4PYx1uTyzu9oSeKPUOPOf27oE8oDl3ovvWDjLXrzovUr5JPJxj25gQWIGwUY1l-2-in0HfZtI7HYyZl_iPlIxM3i8Iof3mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPRonpmAaqHc1-hBS7NMhpK0Msh514716LU-3jAePdVENUZ0mvxnc5-kMxJjgdZK6Q-TsFKTAb5AMtqgB-Xy7MJUnr09FyKmsfWdn6icOluFiINk5dXBJ1Cw-W03S-s2PBc9gsxobS4gnz-O5i-7Y_32Dv2xrpArlZLx_pB0Ndy4HKgReqVcBkvY8mw8hNH5TGAm87tmU5mAXcqnnd1XA_xJ0piMurEW9zTy32nd9tkmS4XEx_z6X_Gqt31O8NZQ9U1cK3vgc1MZqs7dA6OY_5av2nb1iUEagG9pvSC41Dr8btpH-OadSE1J0i1HdGetKjFEwQf_reyxXsiNb-XdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A3qedbjlstbjOBESg6sWEdCBnKbOrCky_bJ_SZ89S1sP3CQVx_swIig_xSN93gE0xoKAxUqVtJG0D5Riy-BLASE-iaVXmTbWmN2jSmVJQ1F09Y_fzPsHnPKQhyK1mzO9OYa7LTiHW96uFyMRO1yuaIBaqM_v5plTszfyphAExBlnoxlTd5Ji7W7xkt71Dmqe-AlDUp_Sstpa0Pr9CeiVM8RjESKeaf2WJ1EcDQqmfdhNTqCJdVgXvW8YqnITaRgMq71N_49u257Pv_2n-_KExKPspy37M8Dz4cSM8zSfXyQ9x0GZEIKIDKMUs8QcgCzU-OKpFqJlQYDuSvaU5A97eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=OYWLMjj5tD7h6YYJX9tcfbp-VhWPffBztvwHuEZpA-5WtimBlrn3rXF995z-krx4ubc1T_1543xNKim2p4dJEq13-DYpmLjMoW0OqRx7vZC0LrLsFTZ_mK8sACUXOhOEBoKyYcHOEmNz5ShzdALhSBc9uqLSresRDL3XvoUxkoA4UqSI_oAH8syXzqmQVYQwR-CbA2Nclh1qmOTdu430QMNF1GiJ2ySO5YnsjlnHYiH_MnqK8JAgXRKDQ_27jqE8_OVqnCPIDhEVj78M48QnDBIvW4he9TYPDvBM3Jkgm_xuFYf0hyC74majhuUtV2-Nn_YfoHoycZ3LiZtAWn7xxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=OYWLMjj5tD7h6YYJX9tcfbp-VhWPffBztvwHuEZpA-5WtimBlrn3rXF995z-krx4ubc1T_1543xNKim2p4dJEq13-DYpmLjMoW0OqRx7vZC0LrLsFTZ_mK8sACUXOhOEBoKyYcHOEmNz5ShzdALhSBc9uqLSresRDL3XvoUxkoA4UqSI_oAH8syXzqmQVYQwR-CbA2Nclh1qmOTdu430QMNF1GiJ2ySO5YnsjlnHYiH_MnqK8JAgXRKDQ_27jqE8_OVqnCPIDhEVj78M48QnDBIvW4he9TYPDvBM3Jkgm_xuFYf0hyC74majhuUtV2-Nn_YfoHoycZ3LiZtAWn7xxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZx2btAIQ0h-JHdM4CoWex3PhpEC9zYwMu8aMowfkmVtkFSKMzE0gD5wLIOGr0ZOXBK76TQqG4TFTFKKOrSTlYLv4EPeHsc5jRSIKhhU0ZDJx4yKfef7ShuE3SLDwQvZWFZtbfxEPYVA4xx27uCLFdQzlBdJEskjMGGGudjs_6phzOrzb0L5CDZGDpr2-avaqLjAqO99hNTsGabAF5Pt8HXkNiTifg_RJL8yQoSUC_piyNn9-GZwA6JYQFu7WVUfP4DPUqFdtW94gfOTinISxnIeV9wjEsTKBfmkIDALL78MKDU6YEkpWhE2IIHJ8DXqG02Ih2HwdlFWMYXXUR1Wi6h3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZx2btAIQ0h-JHdM4CoWex3PhpEC9zYwMu8aMowfkmVtkFSKMzE0gD5wLIOGr0ZOXBK76TQqG4TFTFKKOrSTlYLv4EPeHsc5jRSIKhhU0ZDJx4yKfef7ShuE3SLDwQvZWFZtbfxEPYVA4xx27uCLFdQzlBdJEskjMGGGudjs_6phzOrzb0L5CDZGDpr2-avaqLjAqO99hNTsGabAF5Pt8HXkNiTifg_RJL8yQoSUC_piyNn9-GZwA6JYQFu7WVUfP4DPUqFdtW94gfOTinISxnIeV9wjEsTKBfmkIDALL78MKDU6YEkpWhE2IIHJ8DXqG02Ih2HwdlFWMYXXUR1Wi6h3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=V8AwdZa7x6eKnt8GwfUKO26PxR6nIvb_cjt0X0wyAqwqSvq7IIotn0nnvIHDZYyc0PFgJJxdf_SYR9He1DW2J4teWuy5eTxB6O0BkzSl4cSGtLYlasQUgJL8deAXSSNH0EsySREdCe2E4rb5ePsVn-gv_WDY1ug_1Cf1TcYyXrgXE0CfeTT6NYX5gfuOsCBXmimTUHO7BqPQDN6NoigptTUv8BQXa18D0KcWWudH0FPUMTKFTdAryfQFkoPcrhmWwLD5iUxKPDmk-spe7_THED7nvrqaFtmllYUQ8ePlwhzJacwa5wXtWzi3HAkxnxc3hmNduKEJ2KOpmP5CrWZhig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=V8AwdZa7x6eKnt8GwfUKO26PxR6nIvb_cjt0X0wyAqwqSvq7IIotn0nnvIHDZYyc0PFgJJxdf_SYR9He1DW2J4teWuy5eTxB6O0BkzSl4cSGtLYlasQUgJL8deAXSSNH0EsySREdCe2E4rb5ePsVn-gv_WDY1ug_1Cf1TcYyXrgXE0CfeTT6NYX5gfuOsCBXmimTUHO7BqPQDN6NoigptTUv8BQXa18D0KcWWudH0FPUMTKFTdAryfQFkoPcrhmWwLD5iUxKPDmk-spe7_THED7nvrqaFtmllYUQ8ePlwhzJacwa5wXtWzi3HAkxnxc3hmNduKEJ2KOpmP5CrWZhig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_U7OPeoO31KUiiJMUWTtMykRjrB7baGijW4vGWQgi5PBtHfbNi4JR8PkB7hb5BfbiBq0FLJo44yf0X_Ltuudr9gcYBj0cbGGdFOYFy2_odV51hsd5nvfreyY558I1PJmQycL-Mlh-Be_M5jQZ3Ii5JJOT2jIOFcnzKiDAUfdIUU4OwqrFRF5prZHj0JYLO2Ajb9YyKvH_4nmu7s9icK2ue5zEW5cUX9_VCCkoHdyHw0_6HdaHRBeAPEc7g-Xsmyt_KqS7P8lIBfkcjhqsiZvsTkUh0r_IYfgvNV26Ev0IGkwduM9PiHqUM53tQ-CkqW4KshXfTXX6zc2KqJuPjoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YR4p1Ed5-S75VwSsPVSKTEun9qTq_QleOFHRIxb22N9KBdMZ-8UmMVesE5ycrRliiGjOt7UqAM4h3VyO1d94puc1arVjhXOdo9rxgm_ouMVC3hDgrhkXzf6oePEMNBZGiNIGmR-surnI44su-xHKwW3EOKTB3trSf26ikjzAhwJYZKeUO_HL9sLenuy2t3j0iSPFT7j_CwfobpZIAkrs0bNc677FRPDKc1cQ_WmWjjfgMlEIny7Eumm_DFFt7XeLI6oTzjFEKZxilYiNH4xD4H8YO5h1huTYsjg5B6gMMCGpiUCxcnPJ1VhOYYEND6Zcb6Gbd0ZLulDP_ojELgDiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsF5BASKJDABmK5mXGymIHEXlRPZcJduhT7l3_Ae47WNtiYurBygprj2_EKr3THVTH879exIv7h2XxIHhAdhcKk-0wJg1jbx7NN_NZD-IEpe3Zts6uK2a4qTFFIo7GJ73tKoBg-FJGjO20Qmsk-J59pPGLvBTvT2qvTa8vgQ8MGkEyehrRoXaZCim8G3Yd8ODGfJBFwR7pvyGI2YJIGSHVxbDYf3bCcA9H9_J5YeSsupyJKUWiDDDK0Q0LGkE7kRdsL6lU2x6O7vBJ5XyOSLnUv5jsDgUwPVw0zFqJgQOeaFs650NpHQ-vPUzVKG54H91FkYxLql7jEKLkvS0P-eSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TEqnQHWRfozIvjvxv126XUBB2ebZK8NtbBo6k2GxsKuZo3o_uShztdMMl1tutfk27HvYHC0YOmfoVy-SpsleClO-lZdI_MMbTMMh8Z4F8UtA7iDm0_QoXbSq22gHy0b5JXtrDAMnynKQXjJHRjuuns5aG7SO5c9QkeiTRE_UkgbUweur5shSSbEatBAtQ64ONnfDsMx0uKn09joPyRjJ6JD6ozl2Zy0fott7sWo4ewE-6kYVrbVXvvBIegxKyFBIzOWD2z09DK3de17OVSOZ3xWSGuTvapzKdSp1zip4CpdLufmRENWgaMzs44YSXjPUqpCURTSnWo_LMwzvuWz2mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaEojTmFj7HLXrimzyOAw8CRNd3QuRmJi6hBsVb5SpJL0NVUm1SlGRnWXceCHU8CmP3DpPzmNnPeOdZvE6JMbf7L5x9ULNxoPCXPP2aLtGwoqGYI-XaLH9-MsISuABfKpbMa-zQXWldBxoU7kZW6lgCF3XlVU-2QUoACHZY1yUUT7L-KEKjaQMDxySfkQURZ34gWpjmLwW1LCdRuCCNEXP3nxVAjjarXus4yAugJIBPLvq69F9oDMQI_Jk8r3p0tHuwF1eTshBN_TDAVgJkg4ZPYilYsnO53HoW733EudO52kksoDTnJbYw4J1wVh75tTKTDy_y0qRY4-0vt7Nwlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oYFv6yldcZ34XCDLNI8NJWWhvf-schQofkE_fHKUMyo3GKQmELm1sUc1Oc2MSxYrtf-MGJ1774GrhliVNYcgQAtbsggpOihIUig00mdq1ni2lL1Eim6cgLCimTvxHzxy7WY78LXbu7KyCWck1gMB6BTbrM6JKDAIWVGPLuHAZx6Kjjt7YnkTmbdRcaGzzgzbet6njjv0g8xw5QA3rGhK1EYQD51XfgrJS9fxaSBfLx6-9_hdIlYj9L4Bi2B7maeb6_k9Fzs9w-r8GAuw-5yOIfNxWmGjUmhe6JvvlTUg9zv1RbMgaYuh96PO8axFzm00xdeLZULleWdz-gB9a0QZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-hb_RKThbQ9aFM-GsIOPdV4JvnfmB6O3yRJQKE5ow2usj_ATpOe_kfunE31sg3fojOGUXxL0ygyg7HYUj9MQyc8ITM94eunqvKngabxqnWgG02xmBIyBn4ADRGnHvrkt5cZAu3pgA7vmTYpeEeZFS_ucwc1yp6vKBxDiFqbd0JDfZzFafkEIELkYBCB1ppP-PolB3HnHS5n3j8KOGzBdkrr4xmMQXNgmJafpxSs6Dnm9gpa4Z1ivqVfMBg7kST2Vgs8N5rtx0IQceHWOP9OVX3C8-YiXRMrbjr_2lyRlwQDifyVZc9HO9swTwU6L6tI-mRYlEJ-oJu2QhVww_6ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ozy3hm4mv0PWcGyfCMRs7bzSJ_aMY61oBhCK2qjG6PXKM_BzhHhFT0s6t0IHm7A9QebKgEcDncudhbtnQ_7Q1bHYGkrq5V7SvWNX1Ba-XurdowBNsglVyxHPD4AaOhoJDDEaBTTIKzMKF5qXbTvY1rETfbEBQZe4O5rDGJN5ThcCh6ACttHx7vAUsaeGBLhjLHPVd5qiOD24XdQiazipIOZ0SDE4p3gZYgMVn02DLCjqZ-cWBVjZS1yQiOgJZJBjw-JyRAqSK-vMVRpWqi6V7A6qG2LqsB4HXeKVi2VmQGo7XaM1-lmwjZ-6ycNFTbF-of30E7G6ffW8ZVWu405Tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=nSUYNF6L9ByFBA45Nz5hLdaUJ_HvHT_eo95zptx4bvAbP9dO4QFIIgxitqWlwH6x8USvv8cQYq-GrTtTaiIfRvo_7pINP7_cIQuiSsiHCm0x24ZLrrlADE-6DK7Xh04jjMtYP8JuWIkJx0TpgVF4J7QrslbSukuppMoTG-nS8ThjMrekIrA8UG1Uz18F9L3e5rkM-Q8cXxQpKs_qoT8jF_5s2l4W9PN2h3TSaDGvRx5yqnXDKU15fe8ofZKkyXt8B4mB_lYZkKtu6_hRbBR0d3KD7ew_eomh6o1B2b74YuG-alyAoubT__DatslwDloYz9Olij2SLK9877ef2-HIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=nSUYNF6L9ByFBA45Nz5hLdaUJ_HvHT_eo95zptx4bvAbP9dO4QFIIgxitqWlwH6x8USvv8cQYq-GrTtTaiIfRvo_7pINP7_cIQuiSsiHCm0x24ZLrrlADE-6DK7Xh04jjMtYP8JuWIkJx0TpgVF4J7QrslbSukuppMoTG-nS8ThjMrekIrA8UG1Uz18F9L3e5rkM-Q8cXxQpKs_qoT8jF_5s2l4W9PN2h3TSaDGvRx5yqnXDKU15fe8ofZKkyXt8B4mB_lYZkKtu6_hRbBR0d3KD7ew_eomh6o1B2b74YuG-alyAoubT__DatslwDloYz9Olij2SLK9877ef2-HIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O5DSeuLPz8yIw4AqrRdEqdGyr_5ws9y9viXy3TdVpLdUWKvglKFAOLRm5EB_4e6RN8Um5whLo1on2qpyWUCOnZMqatoCz8-1CvpwnEUrlWECPlJZRvaPbPkx-g-tN6vqqbmYlsUJQZyx-teqdMLh9wh1PNkpI36_2_-MuPECngLsH8wTDW9EjBEzJdRrypln42TMytybldpbNQ548S5rkhg5S39YfTa6vBHT06obg-HyhyQuyOv_5CDeyM8p8ss9cSo4nT5e8UguoSOhfZo7Pf14R1N7yZwTll5HSnRkC4-7kS3YEueRDoEHdinWLm2zMzxB6Bim4rgONst5bAaIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DZkfx_dmhfjxvJ1XlRL3vQtx4NX_MderAbKD1gRSJeezLddWSSaXRixSL4_8QGYstE3wyjMSXXMYelAtVHDEit0R23ZzO8ROU1z0iYCOz4gHYQi8D0ls4KmfrO_qiOsU0lOH7eSJeydV6e7-QrENJ2JZMtP2_y5pmv8p-ptYJiP2c08xsn_CUqHrcFLY30a24zXUrJVMAGCS4D64vTa6TH5Y_74hqzOYsW2uJ41peJXl_-V4A0pxpwVToXH_Zcdo_uyU7sMRlnT3JJTy55PSezyo2Kule63iXto5Oo7wRe4iOSusbvHB8dd4Ud98S_AYT0IOvt2vcOwGNl_WhpuPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O4kcTaFa2TMr9Bx-UuKmQbhotF4gtSYk-eP9_S4xJ1BKDfOvslUxre4_fbwzoZXYjdEU9faOpbh0tknUuZDkjFCyEGyyE_Lq-hIZOEULH7bFdY3mw5cS_8VUBlMdtMhGXyRlS5swZWXWmYhuskJxmSfpDtnFypFrwFyWOfbJeMEmQVUPMHs9_ZBxJbpKPCtFQFEmegj5DdulMQV3aZUiyX5d-MT-mEG4ZoEZfaOe1pB5L76SV919gyc5xNY5x_KUv-bohnM3Q9WXXSSd9nZ2Boe6zgjaeXn-4SfIDc-_1tNb2BQon5UhQZ86nSn40Ba1X4wsEZNMFFu4HT3TuIMAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXwoFpi0FSHCmwVxrNE2x4-1mlRVc1mIRBYpfEeNAHvmXFcegYohtHk2GJiTl9iqc6r9b4K1Muuyp6wfBB-UNIE5DSeBl4ICq3dtWbif3sSLdva5bNxPXlkND0qsjO3vGapIXm6YN2ObHxwZYQ9TaM67CZBRexrnkmtVCo9rFfkY7_OaD4GX3S5NeTmYS937NOmrxe5BwXa4T3H7qmB1mngWb6NI4V8E1OQv8XvKIHBWE1F2dozMZe3qiNMZnAzFrNgiVSHIe8uedFjhWLf0hhf7nfALPdgmjnn90b-C_kWoyYWslY5neMck5ZLcWP1zRFHF8Klqv8RDViXn8sG04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=feKsGsYvr1qWcIkABPvye-ERlsGZU3JyHTngZ8Ea_SiHtPiv2UMT6d-IBNa6Pz7gs2aIYPyPv8zMZJSDN0G4fggYGz4IgBNzgMXgC-iGGUgEY5qUAQ-mB3rwu2BSwdtF_hVUzzPxXWQRkYbxWoRVqX-Vsf6Q4FUuVoja47eO3vAMNWSCWUJz-iWBs-8BRoYhdLK7LETq9bW37O2oDly09pKXGBZSPcmGgVTacjb0SUQpBik2myItPcCpEN7tLZnPIHUSkqkMKTIR70-zB0m1VzxVb8tZqZ7TPYEJ6nK5lfJP-Bi5H4YaeSkrWa_LEEpmbaq2FHNfTLE_-R48NmXq7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=feKsGsYvr1qWcIkABPvye-ERlsGZU3JyHTngZ8Ea_SiHtPiv2UMT6d-IBNa6Pz7gs2aIYPyPv8zMZJSDN0G4fggYGz4IgBNzgMXgC-iGGUgEY5qUAQ-mB3rwu2BSwdtF_hVUzzPxXWQRkYbxWoRVqX-Vsf6Q4FUuVoja47eO3vAMNWSCWUJz-iWBs-8BRoYhdLK7LETq9bW37O2oDly09pKXGBZSPcmGgVTacjb0SUQpBik2myItPcCpEN7tLZnPIHUSkqkMKTIR70-zB0m1VzxVb8tZqZ7TPYEJ6nK5lfJP-Bi5H4YaeSkrWa_LEEpmbaq2FHNfTLE_-R48NmXq7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mksLp_1Puyn0pHX6iNiKk7dQccCCQ_F0WRK2Hzoeayvc04d-oJNLG5UA_vIjEGXL6btMw0WACB-siiNKbiB216MOPuJ2C70EWaEN7aVWjO-W1ZzwWQL-FoznF0q-PbqDEQ00iBViSBaq1D4iivF7u0L3AD4IwF8rzLuNIxHQvsk2v0acHzRivqFVPfl_3xTDQkmgR3xBPYszkz-tLXwQ3jgFAYkjYmnh0yiaoY54Y6pIBkPKmwLM6cs94GFhbaMZP4Goqom5G0ITHJmX7APggYK7-5-lY5L0opo0ZGicDIi6Y_GEE1Lt4qvnW3nBADVvZb-tVteKtRJQcvBim9anAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=PoqB8Rt7k8FAvW5S2Gvp9e1sl-H8I0ZQJo3VxJebEFRv65zR06fo1btDi2DQKaXBCEYFwXxYGhFxrjhRYvO3ezisI4lF9CNVRwwg8sRmnNkMq0TCnPIgcE0rd8Xbq94UpbF5z0DmgX-dAccuCQbAJKjnTxGN72Zj3X92PKXFVJs6G0vMEIc3UcWqZdNYaWyrAcBq5_QhhI_uhScf7DzxkQfQ0J9FnGptUKhtXU197i-5c-UiTkT7bpM4zoKgL2Ne3cUlo7-RIZGJ8WpKFtzZmvOOjaZ7y0v4GBHgD6XfP9vQIO1VnmslDsBWYADuBemHDnKkvmEikNnSr-gQQl0n0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=PoqB8Rt7k8FAvW5S2Gvp9e1sl-H8I0ZQJo3VxJebEFRv65zR06fo1btDi2DQKaXBCEYFwXxYGhFxrjhRYvO3ezisI4lF9CNVRwwg8sRmnNkMq0TCnPIgcE0rd8Xbq94UpbF5z0DmgX-dAccuCQbAJKjnTxGN72Zj3X92PKXFVJs6G0vMEIc3UcWqZdNYaWyrAcBq5_QhhI_uhScf7DzxkQfQ0J9FnGptUKhtXU197i-5c-UiTkT7bpM4zoKgL2Ne3cUlo7-RIZGJ8WpKFtzZmvOOjaZ7y0v4GBHgD6XfP9vQIO1VnmslDsBWYADuBemHDnKkvmEikNnSr-gQQl0n0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKoY4NdHvktX6uycUcee-GlhOXnbiV4yqNA6F5lUi-fgB1iZgP9eK2SkZS92xmMrjeAvzhkNrVrlaDIHil_lsNZIWt774XMbZ8FzBe7aDZ0mxar91nhKxsAWbOIeABJ6ltkSNfvIyLOHm6qJoB-cNAn37LWI9QaAwdViJDbKuEaXicBTj_z0Gxm_REMkleO9dfyaaATAMzb90KDDrOjxzhei84tlCQ8y7I_OE_ZhndSK7ycO3oaOUmzouvbg4tgicBVBM-g7tnfXLbWeofq3T0WLCJbuGfq0KDrcjbDW4TQUPVoMgb4tzwh2WHVK0AnlFsGSv9V0okQPXlqWgqwCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dIE6Po5qIS7_izyv9JGRCCItLKIoZqL2L0o9Tnu3QJtt-cHw5rYraL-clJEm6lSj0NWmja8b6MYJGUZIwdFkqGYPnfxktGwUjAl2yZqj3FLLgs7ey97xBDh5YxgL3bq-qW0oBHv_Se6Hz4ME81jtRMiqZCCrEd8u5vkkoppzFxJKcNQ3xWjUHpqJBTM5RX9KPgCiraLBfK5EUJI2VR-9dG0tUg_pSdW1jy2PHyGU6p4lTPubfJOIks04ZT3SbazaIUAA4xB0_A51g0pW0dDJE-pGGMaFKuUhIpS4n_u0UHa1D9rOnrYZVgaS6K9oE_GWmjGlpSBqyuv3dgqT3vQFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/StIHM7MN_DJR-TD9BdUjrDPFDaupTxsom0OMTbp0uxBZzuMAjMy-NEjIYL8HeRsi_QHQiGO2I8IFDiQpU5M6JCQyDlR2nIBrNv4xV2WBA9I7FI_a-L3-puRKUl2EyiP9-ryXi7_sHsotFDTNsoIv3xQU-avnAoipvYGIBCi4TTaE8XbLm6p8VuUYTkHBd3My6z6YbN-INnpuBzCzf2wRVRIIRFfSKF8xdIh3zV8rDA0mHoMmDMADfFktzmioP8EZKmMVxFwJvWDhnjRwb2rMeSD-TSfEWFdBolseEFricJt5vgz_T35CAHeJaMWlS9_1yFBduab03_7W_yCucH62cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F5QevJ1dhupagDKZCwMRCyRPqRMzIg4RrDuPb3iMXH0VcYe3X6jLmlD9WReZq8wDHUuL71zdwxM8eljYY_q09UQO4RwPT72fZ-KQpElWePlkuC8wPKgYTQpob8PKQkaNw1bl7ZOKAYaYoMznjfJrDBAvC7UxQRD36epCfVFkwyncCLmVPOPDKniRR7zDN1AyX3IydlKR6v-_zRCwm9yEHorgoLE5Dl3ygE1MtX2nCD7Yks-Kz7ecP9zLVO4MNI1MeqNd-lPyrQC2-KqU3ujC-j-UF1ud7LpsBr0qCk-owHiWd9HDyXzfuWlsbtb5zVrfwLsH-75mS8RuF3HdhBANyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/enT7Jy5tO6iF0Jz5t-cbHZivzWbre31LroBEIBUOLGtkTiUthkteTGuiKvfeh_j6R9hlWUymNiMcEdosBimDgM9Dbv2Z5Uqu9vCTZr_JTHqquuhjc3wPQYFKAe4pQQjJbMGvRadZOE4Vts16OIpJli7QVWNLMBa9fJ32aUFsOxp3v5ip0jo9Yb7E63vpPB7hBAFrpfbwbI84YSZgPEmZh-wYQBgqpESxKcW0-f6aene3hdosNUp8-KkV1Jj-P0janBNMZWcVeXnET-Ozp-EDDaNWFSs3o6UZ673aIqp5k4vI8CCkDSIdVh43ZNWxCi2f-mLnIxeJMxGi8NUq-PgWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hWuvn2u8smGjbl_h85a0rpqNdKi02-YJBh9CAEfWE9Y5TGHRCZ155deHxBj8lZ2NV1848CUGRK8s7uMyzTqk1iybtOgPxk2Ud9qRb37nxOA5q0JENjJVsmWG1UdNCf2_WyfF8zAmp9LBbUF1sAqOuZShR3OWb_QUoQnncZaxnt9eflMEWB29v99Rw1Rk2gANaMLPxNSXpAIIJy6UjdtJFsXrJQg2o7cjMJ5j3nlb-Kp51VbEYYZ70PZOuE0Sqhrqv6qe3xro8rtMuP9qcrZNVjOokHh0XQaUZYrzIGMIFuv6JVO_q4vVBpsj9ns7jEnkAz_uI9_g6GFSlqAzmeZyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BarmqQLigcFuDLzzAFTanzhHMBQ9ZZzQxB_7rZ9WML4jO4qPjYPUUkXdz5qwX9S-Vl3u95e7EtCuxEkj0866dLKiqps7xog2Kioi6tMhRbAd4U92FkxoxzShV6KVWqTFXPgLi7lzrSCym3do-7TpZyX_doSPdYeoweRZYmucA0phzZQXvB7AB9AiPcRrlMMleeR6BgHSR4kzvJpaeuDXDD3jzgf1IepeIrgA5KPcQ8pvzHyM9F6wP5MqevAt9zta42LEqdpvYHqrViRFdFRsLXGTnPpQJ-jJ1MF_7Iq0iCPqR_92VgvDVX01OKIWYvKTsHN_IyLynkPnpZfrpY-iHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XGklBn7q0Jt0aM27qTXFkbvc3UrGbDXlqzEvIQDfmPfYAydk8y22jlRUSagLfWlUUmY-2geQyryVbMJIvnLWNk_YmHGV9VrvEGPrG6-QtZTUsooweU6IIklU1S9lO-zYlVg1GZJXqwq5IVy4CVGIF1AX53kMP0XEZ_QbMZxaXvbBazG8Q8Mzav4idjd8nuOkWqY91_19q9IAWRlvyvkQxcD_sOWqXQd048-_hdpnmtmxWXo2vvmCcvi-x3_hZ7dE4BxoP8ofblzCrl0PkoOjwOgxYj2YZONvJhVPAFV2CF3A2T-u3BABDhh3tI93JpkCXRSmZtd3IOc8J96c7r2HcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eIXAuITZkN3CNN9ME9u5SX76Uemvv_r-CUCyJPh3XS2RCmSQHp--ge0KVyaCOQHzR0HnHSRKlNddl8sEOiCKQYO_30tQgvWNPzrKxtqc32GWQImxZaVq7-7rmbTqFd8ayK8OHnUyIYNuSvt03pZYLtyS5uUw8N41I-LpehlgBmovrGbKY5z7VJ1caCCuceKj32e4NDfLy3CFohWnUzfrPJQdk9jF6KkPI6vR_O42nPOL6oW4bBe6wyR-WdrJqBLO75FjRo5DmWY3bnAItFrdOxzFGK1BjbEqucUpYwUsIh9306LvcZJF-2BrUQkJ5zZ7bY4tHkF2cnEXMWHYI5NsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TiOb4_usdVblqy_j2WVPrcXOw9g2TJLZPIoyIqaou1KgMFiBGbrEbIMmeIHYBUMskTbCL3LFuJxKLlEY0s7H1od1DmtbQdR28wg4Qxf6vOmo4KDgTYSNSMpMTPpmSapV_BW40pZoS4Da6ddiFyr-_HYJdxMCEKZPYbmFdXeZUgXEWkIpdcnvD16C_67lJibw6Pn909OWF71r62BkKGqr4t2SSn6v5t9mIghl5Kmc1cCH-RcKbB9cMtNA3c0fiA11U2lR0J5MtbyqaK6wUBhEMDy78wdi-g85PmMvmkSj0EYGYkJ81UaFH9zhwf9w438uqOpBTFwxwPyOluvMdTj1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VRXaj2Sj52UO0pg0aBXlScszdxOp34tzolGOJlqUxLyVx5N3T0pyvfRWYxvFlzpInzBJjSTPydty6pqkLhNJ9cjoz8KsSfr7R4q92uXvAFODZAcRPjZTxy-_DTlf0dSaIYermbr5H-NlKYhQFiHOttbocpqzjJLUF7AxX4TXD2ESxrrzrgSqiWKucDw_EqI-mXQrhWXXp0tWY_M63LjQtC6z-t81FL2NLcYBfEkGGfz1qPvv6UYpHTCGGaAFEGT5--s57glR9NWZ6f0hieRwI1fxkav5Yp7PCWpPGJzeeEUgRap7XiTBVZnzXiPBEJ9-Q2Dvirx4RZkatFGu5NcKcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dL1s7QYz3JRVPG7Fnpo-jovGqwH8gHAJhfS_MtMfIzAmLf9T38S8MR9fAXV0-JETQlnu7X9P0gx6VLD6LSd4r_CB5VDQT3JWzDDbkZdG3ziVsB2B21f-IA2rgkklEfESp40gV8HThtls_EwlaG_isN8k_OMwGxfmc40s3ADNbUZxa_e2RwuxYWeUyyIcX81EMApjYjJfcA5uQR2xHfXJm988TMRG7vh5r7-zcQk85gGLbPwfbqHVlDktn6_EPU2cFmtGFNnd3Q0KvO32ow_f_oU999k_eaDrDKgTAgOZq9B8iKZMpPIE9Rn_4Jsf5zuCegjUG1htr0JevTDafxw84w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D7X7vYdKfNEamQIwPVux2q9eLiZS5ND9E9MEJigaor-j7KbfEzHtsMm98rllM0Tud_4flpqTEt1nGcqQcxY7Xc9De9KOVhIq-rtWD_WTR8Ytm3i0pzFHORIp5zXdSGtUXI-gQvmTJhhfvYflngBM_4w652DOv1a9qJnDRChoOMCr_DQJDj6sqlqukdKJ0HQUMDnENoiKokEqwlKP-2qzk-oJwV-hq7du1HY6EjtfATeJ-RbmuDZwm_GHKX6BwBfuqjFsC5Tm4TPD-8u5F3iZ0XLvYoFbLhvnin-Y33AgytR9RhzukH6w2yHHFu5CAFEIAFjeaq4xg49lHYeUvmgpgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s89dfKtEMrv4nN9XqJ-3l2Tfn2RNsOerqAF8Hr7b0wjIvNT3-AWd8CFtX_3WsV9-oSj-Mn2unxnT8ANty-Pbs4XgBD8hTBtKo3xVV3j5RsZS7V5lbb2o6_M9UF0ILi_kCSGmVEgYbbyB5SIFHK_jViY0ZBAVSNRuIbzdK0KV1UZQa43osl_tMmYHpPVGJdGZhwvinibzG15RY-VEFPBe4XyLotE_azeNX35xtdt1EQcw2fxz6gpmZZc4jMr6RaOvx7tHWj31kGjZKsbhpYWz8e5aVAKypqp0WM-H6VG_J-osfqt94dyDnGNAebWHU9FJdPJ24sdhg4OIVssMcZuUBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eL9fZ86LGfFQT1EkAKRK8-uZz0t1zmuVEdJX859YLuEO3ZPNI0fYz_BHjqGmy1c_4b3BVeWEyyVKArSk5ie82_E1bHxd59mBNJLE1EmcBBo5l2NSIoVbumtnEEtLpHJNg0Gx0t3ouhLjJ7mVkC-8U4y1sbw0D4Ady_XAIkzvXkwBjtkkXMbD9QDvZXP1ddXRAArWQFm80_CdqIyt0YJMFZcoG7Xl_3_ZcI-0p-EelH4tc9SnpoKrtp6KPQi7OjRlGU4Kz06c14NuvO4mm87k-OonEBvmIEtbiP4saoOeoeaSqKpoZQiZDTN7Bz9460lc5agdHWB0UmKW61ch2ovHEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WPxAMpxC7Wd5pJqagrdfutdA6PzXst-_kLIEb2qG808Y-iJM_lSY9xH2mVClOVxP3CNBmwrA5_Za5tqk5BuXPCxh-TKjBwCB4lVRmz5WUXgXl2xoKQkAhdrCPVi1nxnKcwGC4hFEdoj0TcxO6VDLVvCoj891jjMKapmiVRZLiYGcjtwcckSbcdSq4O_DDmDp3NyEGa44KgSpNPT49ctt7CBNYHdX5cZgYx6NI19tacAAvdDenp_cUfrsDXNgJEueLgbv3aAeK90Q8l0yqvKGCx73832tjXunACM9_uPnMErkDf4oQ9RdtZ5rN5Awuu_cxCokHd-n6erZzurbMSAD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qKRV5706CxoEHhx97BofZpveIFLYZShit7J6ingFbFB8OsBvCa1aCwGQy1PEIohfZaX1ilMi4LsGtE1C1DqJ-bY5JO5k3vmE_hymmeuxd7KxbVBVzYjPPEzHJjw6puywHpfwnEN2HwLylt8OGDjS4i21vf1ZbsRJsal3ieL6DXRtFWVCDMBZrMBfyCq0xAN5I2vwg21VUejhvnUxdCccdQensPAimga5PTqT0boy5yN7Y-RgvhrEk2jTOTsz36yjbBRkYLBt8tIe7oX8_nF5EKT1XvHvIgxgG44Dj7NuucKPwuS80hLN3WlP9LGQ99tvzckwoxo72Zh-pjjjG-Om-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FXEcwoHuhUyE5iggc38ksR9ycpLWdtc91bkS7WkqqUM3jVgIwmbPy2wxwuXWHm_Jc-Sp27gecEDbwuOfiUKYu_Lh5EFCaJ1u2APXZCT-iYMC06JH90wLgGR8V0x6rdXvThxcjOjNtbnNyWvpeHLl1LieBxApVpUXBKdoYxwg5D2gr7n07i2T-hQ6F2XlcMp7x_uSNAoVPGCubsFbO4UIGMOP3upXuG2fxxf_D0BIfX3edRLnUdI4b307x6l5f9AtEkLHHyliwsOKapxlEkL7D5gKxYQpbRw3DO4n_XJv91Es-YSVC9A9mt8zktuFNM6sWy1PlbOWmYJ_I9m0GqYIug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WmVtpEZyv6_1orQO-Qzgj42SAUvQZ0_cq8jZNPcB6w6ONwWIs7H91WLXApDbzqJlZcF7CIGq6OgUFJk8kjcwVFwlwQUbk0yUFTE2hOWlWTDrsa9uU4TEHL0u5PYNgmtKMzBK4vF-zIZUE-XGJf9FWaNjQN5WxGeZH6b2vH7cUcDAEUZfYN1hI9mDvQ6iBJV3MeQT_GcC3jLmqkrKAKNUPxSAF755vDdzAYymzE9i5oZq3PmYB8oar0PINsc0StnkQM44ocdc3JzRGIPkRS_63OjfAOXWWovJ6pf7xTMI3NUOuJHhCMulnbNs30TysRPHRmbjfEB3UszCD5ppLvIFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ABuqo7_SMxYC6ezdP2ZwT_oR5jOlZSrmHo4tdlgbboKl-fYgvgR5zcaAHcWXgvKUDzaleLE3iZYmVgD5YNp0aCCqEau9TtU8VExyVvtOVaMP_MOR-hEeL6_Bj-rGuKHZ5qnUtVEmJM32zmndUCv9cWIoA7H2UNqLdTKfvtEFrH_f7TJ4DWbKnzl_Itj8fkNdR9rheEF2Cte0VgKsNFVzwxgmF3fp9sfTksygJUx9j1FiS_7zFBXoHuRZ-TL7me0wreW4KImul-R8VVJNDN-_HNVqhxYebBqVZQYgQLsA9SGafKBXT7IS146IrfmBoHdOwK7R_VK0S5K0b-2MAofsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DGPaCYF9GED2YOpBM1TE9JjlcdvM8jmJ9AwD3cxeNkZqJLs54lnYuM5MSRIvrI-Kb1reW6rqY2zo4l_bRrtzpmU7DuzVSPhPo9jKPuK0oPbDjNWhbqO4qsfrbtdBHqGDMeG9WCCkYvwbhPr23Z6QYtS5znEtNNm7eDTke1SqGkzLm_1RNPNr-d9XPHkoT_dF1TdDnl1SiJaYfqBuvNc4-46tOMliN4iGUImj2JqgmH-caI0UoH7Cn0jTmwefmvWmodE2v47rbb5o87rCNQ--Mnu5YxOYZ843pjJ9y-ut77YJoenVnuIsfwndT8nIn1L40KrANEkU_53n_zMzfaN5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwQg_LMujzceEAnV_9Uq9JH4odD7nQEoZq881u_R-l01W6GF4OMdF6hUFJ59UFYY8-OgZ6bBvAjB-0DPYm1LUIsHBJLeCt5ZzFjUou3fVDwhhkui2k1k8RbYa5ond79JGb4xfDUIQtoIHXf8DJ_A3RiS2SZTOm37UE1SZFCvBu8FNS-sB621Hz5JbxfeGQ1yO6nSBmtYQqyO-SLs-TzYcxP3ReJlshs7W4tA5R7tsFiGOZ3fuu4vajAOkxsgftnWpSFWblgvCwEiLF01t2_2RN8EDUaN8231h6AzpcaXMdIU9K7wjGOClpj6RTgNGVErTFz8Bld1kRHji53CXwa-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VoYFJkUguBKJESDEw54i9BOdlOCyan-erAiEXu0HvWmyEMxaO_UOE4g4vydIMPEBzl0f2UgNvgZS8357EtM665DzWSLMhjcn84K7_CW4TAMPE-Q2HpmynUySZPpgWYKa9pHwCtLb75OooqrVhr6krfcMzZwCj-HvhPERb4SCuu2GzKWFFEjIGcF_G2XTQj0LMk0DZ7gJDHgcrg9ZrBi-GBEAUC42caPlUDaNk-CeCd7OadSyqn9sRCwBafFUMSFp8mrwt3ZAd4WXGKnY6p6kvMR41U8ocgfhV2JgWZ4iXrIYEosGAcQOL2nZoGGkFUaTaZ8Gh8L4VhyCAmC9D-L30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ghAZxaHAjLgx6KAFtiZPvyV0AIaIYohg8ltFCdbS9jEwST4rmALCmxMJitbqEHlTipX_oxjdn0-aKkXhgp35ptWt3Kff4MJukLGwEFhahehdRiRLS1HzvsaOd6MY-dXVPVNBRKYGNy0chSWtvER6yvmB_eODJuLrhyqGRo3CU9-5I7QK1kD-9wgMtTfVMuEOrAyLx60X5S11OqCFDjxJnNcYhmx9wiDQy_UZhxTmSkEoNA4iZ6uYtJtg-j1aQFl8xC2DaXT1ZJvcWWcOBMFZj007Y_qZk6HXuas0iHXQsSjaoLLlJoh2Xx7MqYeGevW0CUft0HP154iU8NvdM1rmyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j3BPYkegviMgtXyX09fA80hyPrMmLf-uWGwpvw8hCyWcl77_WQDIC1Hb4PKbhXGO3b6kWj0ECaJeA4_TKDXiZf84ASEHzejywg12Aq5WWV6kEiXw3AGEkbdpZQOsN94YrAcDiYHii0Kf7RqcGbDo8F9K3lp4emL7IdJWvlHqHU7A3GUDc3i7bVJmrPsfW-uB3Uht9KEOeHnmKXbYkM6glASI5s_NDXyZvkE2bcRwj1uNEk_mXQCoECgjz9CHLzijNmGYM5lud2SrpVoFa8EqEgRCF654Qlb36BS_OmWkk_OrxbazbMdMxxkACgRftYR9kWWdtdxVdbwZCTK7W7RRvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhcfPHU5_Cpqaenjpgy-P0kCrCrNS2EWByHvVjih14s8g2SR18schh5gwp-A6NxvUxU6Ha4_ftyjiPTnCMlG6EZ0dXlZbh5yTp3DWpi-z7H2e9twEffGReFj_nTJcxQmiQK2dOaTCHF7xp7iLdQTlxGky-u4HhuITZJJSg2rHEU8D4_LYUatt5Rs9f4iAzNhxqfSXtf8fkdQ4e3wYvjUQ30NLCX2y92a1B9sCpuZS25k3drUcRuRqTv8MwSvlJUFrp0E-Wd0RrHMvVWlkPW5Zm9ickuMNbqX8_y8lBhZ_sViSpvWRRAGhShHAsW-9NvJ_N4ijP-69RJWN1c9PcfeKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=uObjWFDIQvhsRt8WSP5TSdWDNuim-rLGrAnxiZSklj_e1dyUIPIJcCVtOMF6b90rkpCz82jcbxtyiJGPGQVXjuTyNXbyOB4I_g6PgHkeffYZ4TmpXrZCB9rRFpCPH5iVGW68Vyw_7-3xbPXpqnCD4S4B3yDW0l1RzNFD-9-Shj-Qje-0t8tIZKNkXrF80v0Ka6DUuPhnDxI0E4-w5oSwah065QXacAM6ZfGqA3nmqJO0ewcC5XvDEL_x7Im50lPj2fl47sb3wBbM-OxIG_UuCO2BliJV5igv72nsGeCexHicmC70NP8lFmxeOOqHRWMyv8eQG0HC_v9anlsPig5lXYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=uObjWFDIQvhsRt8WSP5TSdWDNuim-rLGrAnxiZSklj_e1dyUIPIJcCVtOMF6b90rkpCz82jcbxtyiJGPGQVXjuTyNXbyOB4I_g6PgHkeffYZ4TmpXrZCB9rRFpCPH5iVGW68Vyw_7-3xbPXpqnCD4S4B3yDW0l1RzNFD-9-Shj-Qje-0t8tIZKNkXrF80v0Ka6DUuPhnDxI0E4-w5oSwah065QXacAM6ZfGqA3nmqJO0ewcC5XvDEL_x7Im50lPj2fl47sb3wBbM-OxIG_UuCO2BliJV5igv72nsGeCexHicmC70NP8lFmxeOOqHRWMyv8eQG0HC_v9anlsPig5lXYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=NQCqZR8tNPujnB0ETE_Ll9TcWsByCuZEgWcAM5GYycH8lUBAp2kcDbBp7cyNpSEvL9kGKVrztJuVArQUe62fEnF6xZI4lysmLI8CjfHWN9DeNhjiw7ki2n-aUaMJnXy8V1AslfoPS2hFQhdYeT-0uv2mEwC5t3-yWptmthfB7JLSDqFSfBykHxgSRHWIbWC6G0VstsfRLXUXq2iNXoKltwYBpdHk6W4XwR8JlHUcGyAsId1CofIvaicnJ7aeitIWyhDPsqbmh_gGNjbrJQAVgnr4aGcS7ZwQtpk7xp3CpdhWWseXNqR8CXJSnQxrOD46oZ15NC4_G1C29kJ20NXKVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=NQCqZR8tNPujnB0ETE_Ll9TcWsByCuZEgWcAM5GYycH8lUBAp2kcDbBp7cyNpSEvL9kGKVrztJuVArQUe62fEnF6xZI4lysmLI8CjfHWN9DeNhjiw7ki2n-aUaMJnXy8V1AslfoPS2hFQhdYeT-0uv2mEwC5t3-yWptmthfB7JLSDqFSfBykHxgSRHWIbWC6G0VstsfRLXUXq2iNXoKltwYBpdHk6W4XwR8JlHUcGyAsId1CofIvaicnJ7aeitIWyhDPsqbmh_gGNjbrJQAVgnr4aGcS7ZwQtpk7xp3CpdhWWseXNqR8CXJSnQxrOD46oZ15NC4_G1C29kJ20NXKVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NdvZ2kx6TG7k4G-2_DUC5g2z92sMJR2yoFYZfOf-n4RWPC2cfW7gnbvvCXOhuHP86zh5jqvi0CvSbSenPNC0wCUEZPCMyvDr2x2VUNuTsryRcPui2iJMY4teW9N9U6dmmFiSpoaZJ1eYog0YQC0D-UhjVkqb2iTKLCeN-H01ueQ5kGG7F5ydFjNl9-mI5425j_DGLmb46ulus4Oo4w2QSqKnog93-ynueiA7edxoOYU-8NzpJJKiNzvCpU7TuOFtR_lA7RIkEHO_vrVdYXV7cNC7sHv6NgsqbnWA7rGT-gkThMpGNrFNtPA89zj58lDptKYPm2zaWiKHnoaj7z5G1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/axVwZXGt6loBJxaVTwthRdAxTqrv2CeSEj6uVU5tYxUxQxgvFbjW5ydQNGxgCWFZ5l1BOmqy1mUH8Q9ruvifN0AMM32K1CFQSlHsGxomH44-X5zhTvo_A5g00_UaWethENC1msedXe3AShSkbIanAUssMFqvKTPWr8mV9xQLr78r8Q2hzbS98ZUv3fLqgTcUUmVmfd-EW1W1Re6fZwhOvF_YGZ1D42ktJa_TsyIm0gcAI1urVqfuBhBNre4Ese_dfZhDhC97-JP4QZSe-25iHdPbk69_m0pmgFxSWuu4H6knLh8TGAy4aGeDeTfJ-YdmJkthHhfzP7iCCf8_zgmMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=IUjByIx4v3M3MwqUhIz-TSCd654hensxvM1yt0FqarscgQsMk1KplthM8fcEGNrbTSbZcdbZaAbuKPNUm60OguaSx7dT7s72kfLgm7dI6dSMEXf95fMtpFSnPO33ZDDN5_aM-jpcysb0Y2Xke4fMGOWGUlcppuo2ueiEN0rXVas9kwczM07Dlk75JcFQqHXZoJlzKtT5iqc25yWIxn-XB5QHVtGbpc78u-Gjj27WjqFITvxA0k4Tm-w5ymmr-xlEMehD_dF4RyaKO9fiDTVJQBcyLFLw0Rvl4alL5yIxb1FhEmGw8gNLRD-yRZQy-Vj8GdMzMt6VmuDRRkjErw_osA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=IUjByIx4v3M3MwqUhIz-TSCd654hensxvM1yt0FqarscgQsMk1KplthM8fcEGNrbTSbZcdbZaAbuKPNUm60OguaSx7dT7s72kfLgm7dI6dSMEXf95fMtpFSnPO33ZDDN5_aM-jpcysb0Y2Xke4fMGOWGUlcppuo2ueiEN0rXVas9kwczM07Dlk75JcFQqHXZoJlzKtT5iqc25yWIxn-XB5QHVtGbpc78u-Gjj27WjqFITvxA0k4Tm-w5ymmr-xlEMehD_dF4RyaKO9fiDTVJQBcyLFLw0Rvl4alL5yIxb1FhEmGw8gNLRD-yRZQy-Vj8GdMzMt6VmuDRRkjErw_osA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
