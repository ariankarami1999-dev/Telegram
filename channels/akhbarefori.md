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
<img src="https://cdn4.telesco.pe/file/qVKtTtaQs8NtqspdAxpgljvwLJ3urYk0B6hzFfbaa7azqy_hQDtoWwBfZWXNcRsxHEedhi9gYnnBA49Q3OsE9ue4hN4L86VfpBWsU6E0C2Nf5BaARbE1b5rMYTBV-E8BEMOtXE9eeFgNy5NX9UwvtVvVY1LaWYAPKl3FSReuAeE04sx8bj7qKKDuL_7U7GlOrUWEwUSkS2e5saPn7szmnlx62Ue0jrP66akwr0Ssb-erdVeK3dAv6Y2lMCseApTGM0bguE-ORniYqGdbqL9BBtc3jlXbldOQpdsE8ZUgfRf0VzVaohKCQ1LBR7eByxV_lCqYbUFdSD3HJ-46pXHNig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.97M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 23:33:35</div>
<hr>

<div class="tg-post" id="msg-653313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
معاون نیروی دریایی سپاه: دست به ماشه‌ایم
🔹
اگر ترامپ در ذهن خود فکر می‌کند که با زور و ناو می‌تواند تنگه هرمز را باز کند بداند که همان نیروی دریایی که گفتی از بین رفته، تو را در قعر دریا فرو خواهد برد.
🔹
دشمنان ما بدانند اگر فکر می‌کنند با زدن زیرساخت این ملت عقب‌نشینی خواهد کرد، اشتباه محض است و این ملت در این ۴۷ سال نشان داد که خاک می‌خورد اما خاک نمی‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/653313" target="_blank">📅 23:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
احتمال اصلاح برنامهٔ توسعه و بودجه ۱۴۰۵
🔹
رئیس کمیسیون زیربنایی مجمع تشخیص: باتوجه‌به شرایط جنگ در راستای اصلاح برنامه ۵ ‌ساله و بودجه ۱۴۰۵ بررسی‌هایی انجام و پیشنهادهایی آماده شده است.
🔹
همچنین جلساتی برای تهیه پیشنهادها جهت تدوین پیش‌نویس سیاست‌های کلی پساجنگ برای بازسازی و اصلاح برنامه‌ها برگزار شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 332 · <a href="https://t.me/akhbarefori/653312" target="_blank">📅 23:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
از کنار داغ‌ترین خبرها و گزارش‌های امروز ساده عبور نکنید
🔹
احتمال اعلام توافق نهایی ایران و آمریکا تا ساعات آینده
👇
khabarfoori.com/fa/tiny/news-3216395
🔹
رمزگشایی از پیام مهم سپاه به آمریکا
👇
khabarfoori.com/fa/tiny/news-3216611
🔹
گزارش جنجالی یک رسانه آمریکایی درباره رئیس دولت نهم؛ دوران گذار با احمدی نژاد!/ ادعاهای عجیب نیویورک تایمز درباره حصر و مجروح شدن او
👇
khabarfoori.com/fa/tiny/news-3216619
🔹
عکس فوتبالی شکیرا اینستاگرام را منفجر کرد
👇
khabarfoori.com/fa/tiny/news-3216595
🔹
استقبال متفاوت پکن از ترامپ و پوتین | پنج نشانه روشن از دو نوع رابطه
👇
khabarfoori.com/fa/tiny/news-3216539
🔻
ویدئوهای جذاب را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 677 · <a href="https://t.me/akhbarefori/653311" target="_blank">📅 23:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tno-s0DuRgdZAvnSDbc3MBT_EtY4goIYCQKeo6u2Nk13s5B3T3Y-ksWg7cgTm1wKnOokDhMZDIpHDq1MNR_QPmcxEtGu-tJqShHlh5pM6yAnYxEqWFv8yv41IfvEhDBWoRCZQMH4yQQWp1l1cEUvkasDSzNHigDPnyUC5b0yrcBEalFe4nC321iUU75oT8vmDSr-Athee76OZg4qlaEZOpj0UNdvoaxX7i-Uc3P-dvYkH0Z4uoCSvOi25x5Zt18VyIKLyY7oivavhBdolTfLe0iljoScI_-D1pA5j7mmfR_vKyAhc2uMKxk27SKyo2CJVMLr3PXHqX80uLR0FehNbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد ۴۲ ساله شکسته شد؛ سقوط ۱۷.۸ میلیون بشکه‌ای ذخایر نفت آمریکا
🔹
آخرین آمار از کاهش بی‌سابقه ذخایر نفت خام آمریکا حکایت دارد. در هفته گذشته، مجموع ذخایر تجاری و استراتژیک (SPR) این کشور با ۱۷.۸ میلیون بشکه کاهش مواجه شد.
🔹
این رقم، بزرگ‌ترین کاهش هفتگی از سال ۱۹۸۲ (اوّلین سال ثبت داده‌ها) تاکنون محسوب می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/akhbarefori/653310" target="_blank">📅 23:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f94115f3.mp4?token=I2sZcE46KtLXVbH8KUQsn8gx7cfuCGC7Gt2Xql4wOPBSYZkTKbtLXqRQJXG6UQPQe1G3myeHQRuSQcxJIzb2TRVoBGcQkKmgPDETRWB2kUWe3c01lgkliYx4WHlNrK4dof4L9rccAH3FL388Inn-MAouY_Ce2DObLpXYuzHQDUnChdwYRHcshjJMweRL6DVoxNLX4iJX5z379DawW9ynRgzR_pm6tCkmN4tCv6UjwULE7BbIzpqmG9Tg5-KOApby693h1odlMdQwOW4oRKFlSHXOV5ruAo9o4w7PpqSo-t96lZh1A3nypQNg3veaidhbNmurdmt82pQUTx1r4FtZ5lSxfKmpeU-lUb_4opC-oE6ZcB6hNq8y_hdw0GqIdXnOs33pm2tllB7BT7fc_PnlpsXNCnsnvNbCSg2AieOokfy_dyABME6cpnRVhx0vNVdBZ7yixnmFQrc0eKh2Hv0N4mQLOvBsXxJvzBo1NQDr2FcARqcMdHxzX99NekhYk429QBbP8442saqQYtxqHWz9cc__IlNGY7Lnf_Y9YSb8uoUPI_D1Rxn9mS8PoBKh8rCWMyrliOtp1UBTXdbv5cUuL8KlMwqpQCiuGWnkEAK9g0M85p3G2nNevlKKyyIzm3Jd47sa94uo9UOzjHXR6VUTkAtQdQw8Ra_m2RKWWn8f9rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f94115f3.mp4?token=I2sZcE46KtLXVbH8KUQsn8gx7cfuCGC7Gt2Xql4wOPBSYZkTKbtLXqRQJXG6UQPQe1G3myeHQRuSQcxJIzb2TRVoBGcQkKmgPDETRWB2kUWe3c01lgkliYx4WHlNrK4dof4L9rccAH3FL388Inn-MAouY_Ce2DObLpXYuzHQDUnChdwYRHcshjJMweRL6DVoxNLX4iJX5z379DawW9ynRgzR_pm6tCkmN4tCv6UjwULE7BbIzpqmG9Tg5-KOApby693h1odlMdQwOW4oRKFlSHXOV5ruAo9o4w7PpqSo-t96lZh1A3nypQNg3veaidhbNmurdmt82pQUTx1r4FtZ5lSxfKmpeU-lUb_4opC-oE6ZcB6hNq8y_hdw0GqIdXnOs33pm2tllB7BT7fc_PnlpsXNCnsnvNbCSg2AieOokfy_dyABME6cpnRVhx0vNVdBZ7yixnmFQrc0eKh2Hv0N4mQLOvBsXxJvzBo1NQDr2FcARqcMdHxzX99NekhYk429QBbP8442saqQYtxqHWz9cc__IlNGY7Lnf_Y9YSb8uoUPI_D1Rxn9mS8PoBKh8rCWMyrliOtp1UBTXdbv5cUuL8KlMwqpQCiuGWnkEAK9g0M85p3G2nNevlKKyyIzm3Jd47sa94uo9UOzjHXR6VUTkAtQdQw8Ra_m2RKWWn8f9rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با پشتوانه مردم می‌توانیم مقابل آمریکا و اسرائیل بایستیم؛ ما آینده خوبی داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/akhbarefori/653309" target="_blank">📅 23:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1xnmIcde9g3h73P9Zse3Ly-Y3zO0Q5RRuEbV7MWiSVva1KlSoU7HMQnN5Lxvde5SDVYGVE_SjckNPA-zNQh7h2hUbNPqdJMeOZHSZ116Q_dbHsWg5bPe41E9pdAONqQGt9MjRQmrXzUX7UcGevLWaxuXUAHkg4CYORyLKGOP-TUU-Qco5DuZBEFhC6I0ZgWiIolHHyjee69SJ-Cwg-JKS6IEd6AMPSMK2InMVEUaRTEPGNq28kfmIONyH0_zG6YpAwaP5yqBOWEuNrZt4Jgm9FePSiK_9itNarZSb8Q10ydhWwg7hOT3_TayDRco0LvuVb7PF1mCNcM5BjC68ikgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد تمدید خودکار قراردادهای اجاره‌خانه روی میز سران قوا
🔹
وزیر راه‌و‌شهرسازی: پیش‌نویس مصوبه‌ای شامل تعیین سقف برای افزایش اجاره‌خانه‌ها و تمدید خودکار قراردادها تهیه و به نشست سران ۳ قوه ارسال شده است که در صورت تصویب، بلافاصله ابلاغ و اجرایی خواهد شد.
🔹
تعیین نرخ دقیق در استان‌های مختلف برعهده شورای مسکن استان‌ها خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/akhbarefori/653308" target="_blank">📅 23:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌سوم - پادکست کافئین</div>
  <div class="tg-doc-extra">بهرام چوبین</div>
</div>
<a href="https://t.me/akhbarefori/653307" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
بهرام چوبین؛ و پادشاهِ شکاک
🗓
وقتی در سازمان یک نیروی «ستاره» داریم، چگونه غرور کاذبِ مدیریتی می‌تواند حکمِ نابودیِ کسب‌وکار را امضا کند؟ و چرا برای یک نیرویِ متخصص، مهارت‌های سخت (Hard Skills) هرگز جایگزینِ سیاست‌ورزی و درکِ قواعدِ بازی نمی‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/akhbarefori/653307" target="_blank">📅 22:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd95c8661.mp4?token=dXs55NQccUDUO95_Jrx86Fzxywyx4i7P74xkrb74omHN09iKU_lRsGUrbVpt_b651CdUCRcn7_XNtJoUF7qPViuVkyr7G8OE4-b8zjzt5CIXkW5MSD19JQnnvctVU0jykGomGZjVJ7zJr8OjVCCYNh2OlpJKthDBLuuxnAKIfNwQK6GD2NqiUoy-KRMMIGRUwmCim4kWYtOG5I7M9Ma1Rv2Bjv43-JtcfhefCENRzP5qRJaAFICoNofhEUqQ5uAjoah5zybYOHZQYwKridmkFOMGWkERvLwTgWWN4GueyggQkfK6LQmq_GFSfkfOyfpg7to5Y78mjgGlGLRbNuxejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd95c8661.mp4?token=dXs55NQccUDUO95_Jrx86Fzxywyx4i7P74xkrb74omHN09iKU_lRsGUrbVpt_b651CdUCRcn7_XNtJoUF7qPViuVkyr7G8OE4-b8zjzt5CIXkW5MSD19JQnnvctVU0jykGomGZjVJ7zJr8OjVCCYNh2OlpJKthDBLuuxnAKIfNwQK6GD2NqiUoy-KRMMIGRUwmCim4kWYtOG5I7M9Ma1Rv2Bjv43-JtcfhefCENRzP5qRJaAFICoNofhEUqQ5uAjoah5zybYOHZQYwKridmkFOMGWkERvLwTgWWN4GueyggQkfK6LQmq_GFSfkfOyfpg7to5Y78mjgGlGLRbNuxejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهرام چوبین و تراژدیِ مدیرانِ کوته‌فکر
#پادکست_کافئین
| قسمت سی‌ام
☕️
در این اپیزود به سراغِ سرداری رفتیم که تنها با ۱۲ هزار نفر، ماشین جنگیِ یک ارتشِ چند صد هزار نفری را در هم شکست، اما قربانیِ ناامنی، پارانویا و عقده‌های شخصیِ پادشاه خود، شد.
بهرام چوبین ثابت کرد که تحقیرِ یک نیروی نابغه، چگونه می‌تواند پایه‌های یک امپراتوری را ویران کند.
هر روز صبح با یک شات غلیظ از تاریخ آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtube.com/@caffeinepodcast2025?si=yIYlag9mUMtn0O8D
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/akhbarefori/653306" target="_blank">📅 22:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgIOfsouFE6Qtq72nFqxSXG3YdNGiJ9Ahy0F5y9N5M886qeqT1s970X5g9abtK64doqzzAfbDkp760Dbs15__3STkpLfjzzo2qgeY-2lHxwGonlHg6X9olUqs63d7C1kIr0iDOHLO77vGryag0AEeybLKeKfTBsV-vGNCM5CpTGr8OlbjIyGXmaZet4MLY8J-M6UDnzgLRDc6F0OPqaJWbjPNiclH99j4izT4QkmG3P00zEMpU9EigH6RnE2THGjDN8E4nI1r2db-KxWH8-strH2rZ0zQQNKN2D12Zu_yijp6KOdieXt2AXAyheQYrEeRrMGSai2HCdiT9OjnqG81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مک‌گورک: سوال مهم این است که جهان چگونه می‌تواند با بسته‌ماندن طولانی تنگه هرمز سازگار شود
🔹
فرستاده پیشین آمریکا در امور خاورمیانه: درباره ایران، سوال کلیدی دیگر این نیست که این وضعیت چه زمانی پایان می‌یابد؟ بلکه این است که جهان چگونه می‌تواند خود را با بسته ماندن طولانی‌مدت تنگه هرمز تطبیق دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/akhbarefori/653305" target="_blank">📅 22:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6ed86ac2.mp4?token=qAo8VawF5fc_TSAA0I7R9GfJE9KYYoFery6Di-DIH889jrnQIzy89z3X-7qQ77PmYiTNFwlcERMc2n9WJRehv9OkbpdjRZHL1ngDmCYnMnXYAbVcFF_3hWmdqeoqZ1oFqYPozei8EioLWgLtLYeuV2R3nWd1P7II1nIzCQKVB0NNwDj3Swpi9KxVa3Qet89b-V_D5O33e7ZyXqxVQxR2zwenfia2FNMAY0TOJVUorP41tQYIQVa3mdusPAHpUSAqsPee9lYY5AbANLu_VhL1nJ4vWJd_NaQ_HjUvmddI-BpYdkMdwxNC8elUFG_RKwWbOq25ucJwOQs8-RSJjSC77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6ed86ac2.mp4?token=qAo8VawF5fc_TSAA0I7R9GfJE9KYYoFery6Di-DIH889jrnQIzy89z3X-7qQ77PmYiTNFwlcERMc2n9WJRehv9OkbpdjRZHL1ngDmCYnMnXYAbVcFF_3hWmdqeoqZ1oFqYPozei8EioLWgLtLYeuV2R3nWd1P7II1nIzCQKVB0NNwDj3Swpi9KxVa3Qet89b-V_D5O33e7ZyXqxVQxR2zwenfia2FNMAY0TOJVUorP41tQYIQVa3mdusPAHpUSAqsPee9lYY5AbANLu_VhL1nJ4vWJd_NaQ_HjUvmddI-BpYdkMdwxNC8elUFG_RKwWbOq25ucJwOQs8-RSJjSC77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاکانی: پشت سرمان بمباران بود اما ما به آسفالت کردن خیابان ادامه می دادیم
🔹
آمریکا نباید احساس کند که می تواند کشور ما را به کشوری جنگ زده تبدیل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/653304" target="_blank">📅 22:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653303">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5H2tpZfzoeHHqaTORzTddr6-lxrf2g1ct2bCuFOO5QqBVVEVDDVLHvD4-_tJ8XcYZOnIMLlS4bAS-sHn_VZsE6ViE7xCKGSNik6zmBAXia_fAZpcQI-NPimOXg_U7QzHOSU5oDZKK5u7PWKIwZdD14JWKnYCXWVcWgXS_H-lirOGnyXdE-ZSlGAkyLiQbclTtycMTgan4G_yLemuVY2QN4Vqt6eUYYqr63Cbyk8jMRgYZmdMP9aq6Wk7a7WlNWkAebNFZq5NohC6FLOWtYP3QC_tOLmPUos0LVi7W9VlHn-SGQ8Nrd3XtukIB3G2pyL8zZVfvBVjr7ypPjEwWZHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنس بدنه گوشی‌های آیفون تغییر می‌کند
🔹
اپل قصد دارد از نسل بعدی آیفون، تیتانیوم را برای جنس بدنه کنار بگذارد. منبع این تغییر، عملکرد ضعیف این فلز در مدیریت حرارت است که باعث داغ شدن بیش از حد دستگاه می‌شود.
🔹
در مقابل، نام فلز مایع (Liquid Metal) به عنوان جایگزین اصلی مطرح شده است. این آلیاژ که با ریخته‌گری دقیق تولید می‌شود، استحکام فوق‌العاده، مقاومت در برابر خوردگی و انعطاف‌پذیری بالایی دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/akhbarefori/653303" target="_blank">📅 22:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653302">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACzsjStI2mOh18Rt_i0TP0DEkZCOPaHETyAW2NXlnFMN2UgIaKWhG_qE7PgN58kibJHIOxuDIbn8D590ye7kmcfIW8bwUbNbAa1LNezNyhhJTzRaRsmhg0XTHJwKCj2Ejfb8i0fT4_c2R4tzz8ZEBKbmzTSsxxoAv5Z1Uoz_uw6-FpLiXpblJ6ztCSl4tRwpqSMzqKMbL7EhotMF2sb6wUzlflL1VT4lowSNvXPzs_7vN23qiLPgnnqkbq1YcYCqxCDhrs_wbHYuHX6EZnqb7Wve7Mpbfb0J6M68JvHIAMQdYsHaiXn_mmEZk8ljaAXpL_Bw2RrKUpTEvOtsGgJp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: پیروزی‌های ناوگان صمود ادامه دارد
🔹
دیوارهای تزویر آزادی های تمدن غرب را فروریخت و فاشیست صهیونیست را بیش از پیش رسوا ساخت.
🔹
فلسطین را باز به کانون توجه جهانیان بازگرداند.
🔹
رژیم صهیونسیتی مغلوب را که به تشدید سرکوب و جنایاتگری دست زده، سریع‌تر از قبل به نقطه پایان نزدیک کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/akhbarefori/653302" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
واشنگتن تایید کرد؛ سقوط ۴۲ فروند هواپیمای نظامی آمریکا در ایران
گزارش جدید سرویس تحقیقات کنگره آمریکا:
🔹
از آغاز جنگ علیه ایران، دست‌کم ۴۲ فروند هواپیمای نظامی آمریکا از جمله جنگنده و پهپاد، منهدم یا آسیب دیده‌اند. بر اساس این مطالعه، برآورد هزینه وزارت جنگ آمریکا برای عملیات در ایران نیز به ۲۹ میلیارد دلار افزایش یافته است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/akhbarefori/653301" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
فرماندار جیرفت از کاهش شدید سهمیه آزاد جایگاه‌های بنزین این شهر از ۲۵۰ به ۸۵ لیتر در روز خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/akhbarefori/653300" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
معاون بنیاد شهید: حقوق فرزندان شهدا دوباره به حساب مادران واریز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/akhbarefori/653299" target="_blank">📅 22:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دارو داریم، اما مریض نمی تواند بخرد!
همایون سامه‌یح نجف‌آبادی، رییس کمیته داروی کمیسیون بهداشت مجلس در
#گفتگو
با خبرفوری:
🔹
متاسفانه مشکلات دارویی کشور رو به افزایش است که دلایل مختلف خود را دارد.
🔹
قیمت داروی پلاویکس (مورد استفاده در سکته و جراحی قلب) طی ۲ تا ۳ سال از حدود ۷۰ تا ۸۰ هزار تومان به حدود یک میلیون و ۳۶۰ هزار تومان رسیده است.
🔹
داروی ایرانی این دارو با نام «اسویکس» در حال حاضر در دسترس نیست و فقط نمونه خارجی در داروخانه‌ها موجود است؛ به همین دلیل با وجود موجود بودن دارو، بسیاری از بیماران توان خرید آن را ندارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/akhbarefori/653298" target="_blank">📅 22:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9067f9764.mp4?token=VpYsvHgEQVIMi23tfhwyP8_dBmX6oXWyXT8OADszufr3B6g9qeIIibqegtkZqqPyzhYY68g9mgNGAfjz5tN_OV66cgmiPmeXxpGovK2VfdFIfxc5TcCU_CvVajnefo9az3eIamoEfYGo-q2JP8E32zSZ0a6EOkNQHp6gKPFn6x0SIQVBcLA1FSy5iFlkoMO62m9cJgWofl9uZh4xtVYnrcsrmZsgrmZdvIp2FASluOPwyXdPok3hAlgnG-mvyECJK19_9vjloKHlrjGQDlTYsBgzdP9kvC0_g4q3TBfkr3zOADcR7kgeVgooufZUa92eZpC6h9Rs8xCXbF--wCUnYHABdTYh6aF_fYzJqLNDbOWGkqBfGkyWsAJBTXHDgnzBGO9Ie6Yy7PfNey5EqD38v_VsVkUrYFngizqGJmxlxaIb9tqcoJ0O0EGvybyfaUOGyRCsftymzS_SiVucS1MePJO_Q0nu7EZfKyb99Zt1lawdeaE9I3mu1I0PynjPJLLTWauJ5bHUt4LXk5-GrLhMZ-iMSfJ217XIdYAI4OXDdaIaomNtMYMsIw8QUHX3EK7EXubSHTxZpzY-8wGYSqPzHLVq6wvkqhdUV26b1Q6_Ta-Bg_HLrhjllATF7ZMCsQTyMNNQMqS4CavT9wqblgulTaV98HtzZMR7pZAOanEvjMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9067f9764.mp4?token=VpYsvHgEQVIMi23tfhwyP8_dBmX6oXWyXT8OADszufr3B6g9qeIIibqegtkZqqPyzhYY68g9mgNGAfjz5tN_OV66cgmiPmeXxpGovK2VfdFIfxc5TcCU_CvVajnefo9az3eIamoEfYGo-q2JP8E32zSZ0a6EOkNQHp6gKPFn6x0SIQVBcLA1FSy5iFlkoMO62m9cJgWofl9uZh4xtVYnrcsrmZsgrmZdvIp2FASluOPwyXdPok3hAlgnG-mvyECJK19_9vjloKHlrjGQDlTYsBgzdP9kvC0_g4q3TBfkr3zOADcR7kgeVgooufZUa92eZpC6h9Rs8xCXbF--wCUnYHABdTYh6aF_fYzJqLNDbOWGkqBfGkyWsAJBTXHDgnzBGO9Ie6Yy7PfNey5EqD38v_VsVkUrYFngizqGJmxlxaIb9tqcoJ0O0EGvybyfaUOGyRCsftymzS_SiVucS1MePJO_Q0nu7EZfKyb99Zt1lawdeaE9I3mu1I0PynjPJLLTWauJ5bHUt4LXk5-GrLhMZ-iMSfJ217XIdYAI4OXDdaIaomNtMYMsIw8QUHX3EK7EXubSHTxZpzY-8wGYSqPzHLVq6wvkqhdUV26b1Q6_Ta-Bg_HLrhjllATF7ZMCsQTyMNNQMqS4CavT9wqblgulTaV98HtzZMR7pZAOanEvjMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیاتی از خرابکاری تروریستی در ۴ خط انتقال گاز در دولت شهید رئیسی
🔹
از زبان رئیس دفتر رئیس جمهور شهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/akhbarefori/653297" target="_blank">📅 22:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758abff899.mp4?token=hwZ78iMtsIZVQVWzHkl2LV888yvE1S61Mo22aeNWBN2SClXRarbQeoOOJRl8VnQIumsgT1bC7f444enDgnbJwI9Fbre92PCIz06-KrUi1r0S1xsPt24J6RMQ8hFS_5FBrgzKLNNtbsRK1TZITxnil5VyaEYN3m5z4McDgkoE2kCLfwTePfLDua66afhnX4s8d21u6Xc42-uvlpLlMLYIHNSszLg3UDpPktDKI-ZX6bV7XZL83KZ7TfKPe6yfMYVTppcBnnaP4WmCVeAbay5uJb9KczH2j8-dF3w_8ztg3rnL0Q7UcjMl8F8lIdpfZszjND5PeRjRp-x6EH6rRJUX439XF7L1LgZq_IwGY2pzTx-U0ppwFJm2FOvMjqQKCzZ35H4hWYSOG-Z7yj74Ck7YWWS_kWxCx0oZAomNtdjiRy9AsWQMaDFvf7e2Chivqk0pSso1f9_OFDn-_gz8kdeTk7s3C35c-5GjWZPi2cYvxw-5_u9HrSGmWrHcbbfP6j-a13kRdHl9c2-1SlC_ZvxBHRW4BGU_lhUJ3CMkpcVnIlXLozTY6fr2JTJCAPFGrZeDCBPA57c7pDTakMqHX2k3xW1FTT3IrA9oeVTOs0Ndcet_M3KIWYDz8z72WEuQUFrvr95yznsrcp5q6mLsGzB39NrFR8YOERuffl9T5h927c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758abff899.mp4?token=hwZ78iMtsIZVQVWzHkl2LV888yvE1S61Mo22aeNWBN2SClXRarbQeoOOJRl8VnQIumsgT1bC7f444enDgnbJwI9Fbre92PCIz06-KrUi1r0S1xsPt24J6RMQ8hFS_5FBrgzKLNNtbsRK1TZITxnil5VyaEYN3m5z4McDgkoE2kCLfwTePfLDua66afhnX4s8d21u6Xc42-uvlpLlMLYIHNSszLg3UDpPktDKI-ZX6bV7XZL83KZ7TfKPe6yfMYVTppcBnnaP4WmCVeAbay5uJb9KczH2j8-dF3w_8ztg3rnL0Q7UcjMl8F8lIdpfZszjND5PeRjRp-x6EH6rRJUX439XF7L1LgZq_IwGY2pzTx-U0ppwFJm2FOvMjqQKCzZ35H4hWYSOG-Z7yj74Ck7YWWS_kWxCx0oZAomNtdjiRy9AsWQMaDFvf7e2Chivqk0pSso1f9_OFDn-_gz8kdeTk7s3C35c-5GjWZPi2cYvxw-5_u9HrSGmWrHcbbfP6j-a13kRdHl9c2-1SlC_ZvxBHRW4BGU_lhUJ3CMkpcVnIlXLozTY6fr2JTJCAPFGrZeDCBPA57c7pDTakMqHX2k3xW1FTT3IrA9oeVTOs0Ndcet_M3KIWYDz8z72WEuQUFrvr95yznsrcp5q6mLsGzB39NrFR8YOERuffl9T5h927c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عقب نشینی‌های پی در پی پس از به پاکردن آتش جنگ بی‌محاسبه؛ این حکایت حال و روز رئیس‌جمهور آمریکاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/akhbarefori/653296" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سه پیشنهاد برای خروج آمریکا از بحران ایران
🔹
یک تحلیل راهبردی در نشریه The Hill اذعان کرده است که آمریکا پس از حمله به ایران، نه تنها به پیروزی نرسیده، بلکه تنگه هرمز را نیز از دست داده است.
در این تحلیل، سه اولویت برای توقف بحران ارائه شده:
🔹
ائتلاف بین‌المللی برای بازگشایی تنگه هرمز با مشارکت اروپا (قابلیت مین‌روبی) و چین (بزرگترین خریدار نفت ایران)
🔹
احیای کنترل تسلیحات و میز مذاکره با حضور آمریکا، ناتو، روسیه، چین و ایران
🔹
گسترش پیمان ابراهیم با پیشرفت ملموس در مسیر تشکیل کشور فلسطین و گنجاندن عربستان./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/akhbarefori/653295" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2pwg3b55BpTC6pLc8NAK2kSKAoBUcoSBBijmiceWCmDpq7YfblhiKbnuXhOQ6DN9y5hcVR2azd0u_kMhEZmjYwQxBUt7a3LAEtky97DB1nbSWKhJMOmLb4-u8_bgQf_dXmNSI8AUu0I6rcI0av8jz-rCu3LPSEiVe-MyAj5QNZW1rfTWdaQ6sRtO2GmyokSC3gECzFenM23GogunOPUB9p0_1OiR437X3wK_n80HFEY4AHtgt_mafHAMaimrJlLFetq-gUuZB2Yzq1pOSfx-1egUVVoRKfqQ7sjATCt5RQGLmNA_mfr6cFZdkpQsv3udUIr3Gs5L5YWDwD6wQXjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزت زمانی؛ معاون سازمان تبلیغات اسلامی در نشست خبری پویش «جان ایران»: پس از انتشار پیام رهبر انقلاب، تاکنون بیش از ۷۴۵۰ گروه مردمی در لبیک به فرمان ایشان، حمایت خود را از پویش جان ایران اعلام کرده‌اند و این بیعت مردمی پس از جمع‌آوری امضاها تقدیم ایشان خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/akhbarefori/653294" target="_blank">📅 22:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9052bbd568.mp4?token=LK1ZYof7Cv85mSKBCoel8uYzklJLOVr36vvv5Y1_-CpZBsA0mBsDUPft1WTdWoYH81BK8iv9X-IcqQuqwcucI3EkPNcqQLE-J_IRAZ30y8K2PciBYyk1-fG5FPE1lFB_xmuxQL1jfh0n91XU3yG-yHPwfepYtms_-45ebaTc66tuSpFXarlyLcKKImLLOT0AOoIQkd15nUwvdJPktZPyWsG96pMe1I0L9afwABoSAeTsqt7eRv3rSoFxHerrCn94fItnoZjyE1y330sAPA83pFGedR9Kg1h3xwovuFtfuStiJEEDMojUT_b0Ifn2FEDla2e3PbJgmDAHhHZwLAKBBRHLPoLH04loUZF8gaGuS6xNq7rchWU4asRshx8rQ-pNZ04xmxWq1JKZ3wOKUkmrz-efMql5T-WFpx5xqr0R2p6ZZ50XOJ25xCv_w8NkTHDR7h2wc1gqHY7u9Jn09yMy5DLd2e3KC0gg2dpuTaonLcFln0qp1cm2sznqlvVJzI2twhHCGUDSVlCFmTXo0VCMzXG-O5Xd8W7rGlm6dcgit0DsniXIFKm7n8o8_Cw_kAUKXCbJWXnxSiCJ1nTAaBdX1i3EgNlj5sJ2LpPVXW2uKpRZ8HB3rbknpXmFSJ2rkSN0ZFGqZfU16FB3CWA2n3kK0hmP2L52XdHSl8sjnRTxPO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9052bbd568.mp4?token=LK1ZYof7Cv85mSKBCoel8uYzklJLOVr36vvv5Y1_-CpZBsA0mBsDUPft1WTdWoYH81BK8iv9X-IcqQuqwcucI3EkPNcqQLE-J_IRAZ30y8K2PciBYyk1-fG5FPE1lFB_xmuxQL1jfh0n91XU3yG-yHPwfepYtms_-45ebaTc66tuSpFXarlyLcKKImLLOT0AOoIQkd15nUwvdJPktZPyWsG96pMe1I0L9afwABoSAeTsqt7eRv3rSoFxHerrCn94fItnoZjyE1y330sAPA83pFGedR9Kg1h3xwovuFtfuStiJEEDMojUT_b0Ifn2FEDla2e3PbJgmDAHhHZwLAKBBRHLPoLH04loUZF8gaGuS6xNq7rchWU4asRshx8rQ-pNZ04xmxWq1JKZ3wOKUkmrz-efMql5T-WFpx5xqr0R2p6ZZ50XOJ25xCv_w8NkTHDR7h2wc1gqHY7u9Jn09yMy5DLd2e3KC0gg2dpuTaonLcFln0qp1cm2sznqlvVJzI2twhHCGUDSVlCFmTXo0VCMzXG-O5Xd8W7rGlm6dcgit0DsniXIFKm7n8o8_Cw_kAUKXCbJWXnxSiCJ1nTAaBdX1i3EgNlj5sJ2LpPVXW2uKpRZ8HB3rbknpXmFSJ2rkSN0ZFGqZfU16FB3CWA2n3kK0hmP2L52XdHSl8sjnRTxPO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت شیرینِ مادری که ۶ فرزند دارد
از سختی ها و خوشی های مادر بودن در برنامه «جان ایران» شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/akhbarefori/653293" target="_blank">📅 22:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653291">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 52</div>
</div>
<a href="https://t.me/akhbarefori/653291" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌ودوم
رائفی‌پور:
🔹
0:07:20 تفسیر ۷ نام جهنم در قرآن
🔹
0:19:00 تفاوت عذاب گناهکاران در کتاب تورات و زردتشت و اسلام
🔹
0:41:20 ویژه بودن اسامی اهل بیت در حروف ابجد
🔹
1:05:30  تفسیر ۱۱ بخش خطبه غدیر از ابتدا تا ظهور
🔹
1:46:30 بیعت با حضرت علی (ع) ۳ روز به طول انجامید
🔹
2:07:00 چرا یهودیان در قرآن لعن شده اند
🔹
2:14:00 خداوند حامی دشمنان صهیونیست هاست
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/akhbarefori/653291" target="_blank">📅 22:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653290">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
تروریست‌های سنتکام در اطلاعیه‌‌ای مدعیِ تعرض به «یک نفتکش مرتبط با ایران» شدند/ نفتکش بدون آسیب همچنان درحال حرکت است
🔹
سنتکام در اطلاعیه‌‌ای، مدعی شد مسلحینِ این گروهک تروریستی ساعاتی پیش، وارد یک نفتکش حامل پرچم ایران شده و پس از «بررسی»، از آن خارج شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/akhbarefori/653290" target="_blank">📅 22:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653289">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
اکسیوس: قطر پیش‌نویس توافق جدیدی برای کاهش تنش‌ها میان تهران و واشنگتن ارائه کرده است
🔹
هیئت دیپلماتیک ویژه‌ای از سوی قطر در اوایل هفته جاری برای پیگیری این پیش‌نویس به تهران سفر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/akhbarefori/653289" target="_blank">📅 22:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653288">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d5bde06c.mp4?token=VBbdVhyQl6IFKRH0fzRENG4NWqR_ttjFgCIp0Av3zS7M26yjyli7kw9SslzIrYHFRjQcgvDR6g87niJVkA6aNzVi4dw3_PsY1QUoLNcmrwXJU-LHqXipLl8R2CmOKKHYYaOFpThD0Cu6quUOvEIhtmSLMpE08LKsns0t_heLkqMY_r0FtP18EbqkMYmXSjY4mlaj20WvQOpx8sQbqkUYZsxy-JqpKTu6iznUrQRcbMygWgcFguUsIgFm_XmBEUTsR5uHaFb_hm69hx8e3l96LIiuJAsQG55SzDv9eaCYB62I46UzgNU30BaM-AMoJb7uTh7-9DgJdK2Ko1YvTTFsLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d5bde06c.mp4?token=VBbdVhyQl6IFKRH0fzRENG4NWqR_ttjFgCIp0Av3zS7M26yjyli7kw9SslzIrYHFRjQcgvDR6g87niJVkA6aNzVi4dw3_PsY1QUoLNcmrwXJU-LHqXipLl8R2CmOKKHYYaOFpThD0Cu6quUOvEIhtmSLMpE08LKsns0t_heLkqMY_r0FtP18EbqkMYmXSjY4mlaj20WvQOpx8sQbqkUYZsxy-JqpKTu6iznUrQRcbMygWgcFguUsIgFm_XmBEUTsR5uHaFb_hm69hx8e3l96LIiuJAsQG55SzDv9eaCYB62I46UzgNU30BaM-AMoJb7uTh7-9DgJdK2Ko1YvTTFsLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عدد واقعی جمعیت ایران چقدر است؟
🔹
تازه‌ترین داده درباره جمعیت ایران منتشر شد، نکته حائز اهمیت تعداد افرادی است که در سن ازدواج قرار دارند. از دیدن دو عدد در این بسته تعجب خواهید کرد!
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/akhbarefori/653288" target="_blank">📅 21:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653287">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eao8ME2m2Uz60ngKrAKaZGPXuGzmrxDwvZnkpXlBX4UJ5JhxHbtKfPDtcclqudZJYcUq-DTpS0ZtIC5ZQ262UwfyAJD9IApmpqEzsVMA3oHSixrl3eftVCDBEXlkVtRL1h1MbSc_-44UjfHc94UuIBk5L9rGTuJnUyzb8GJiQwxSabWIOev6QNjjSyoB14yZoxc9HppmvGbkFzwtMc9vewdR-eWOCrzrkvhfvNu0JWH2b3RFNU0Oriv7iBxHAPiukSLKPkCVN6FQfr0lMBxS-oZBvGaGFoXFr5rem-ZJBisE7BFexW4djaZxPc9YlGIlXQOs9xZv77CP2jn7n-vwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقبال متفاوت پکن از ترامپ و پوتین | پنج نشانه روشن از دو نوع رابطه | از صرف چای تا موسیقی پیشواز
🔹
چند روز پس از سفر دونالد ترامپ، رئیس‌جمهور آمریکا، به پکن، این بار ولادیمیر پوتین، رئیس‌جمهور روسیه، وارد چین شد و با شی جین‌پینگ دیدار کرد.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3216539</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/akhbarefori/653287" target="_blank">📅 21:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653286">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66d570f341.mp4?token=srdhxH44Z0RGRWjLMLCaAoXCckMp6cBxjMjK4KvamRe-4nvFND4VyNcEnUWqHM1TbG1HfI8UKsZ8qIlNRm6fUkTq2cxhZNcmxW7-qc7OdnW_sxtkOr0_YdTNNlrFnq-N802XOi3wxMoxdGftzYelMgaLf1yQa9TR9dk9XriB5KTiy4EKkfh-jhsj_J0_XXTd142qBCkv_s1rcwccahFAI1uJJinQdHRm3v2CtubmxTT8A-sjjrUF86aN_WEofKgCfoxqG49x41f_ubIuODyA3dSecqGZxwza8DrxIRb2ZqgS7s6w2UVKfThK1hEn79WhKyPPzFmwLyljqgwkC3ut9rkrbrQlFD_akVSvJOQ3cgMZ2N2bSiuesHc2EvJ4pcz-QyVL3jAPIvIcZq9RRUq1fpqhDzzwAp6rs0Prr70v-mRCLMkq8Hf2T_wcWXTY3Qc1NStAEEjCCY5So3fxFvrgJ3G5gJiHsJV3SLq2vKU7jS82X-cMLGx23DkXh1bsA4kFlN3w1ZLfWTO_waaz-zV-hEzqVyKNnPd3eYFALMyP9d5DtSMCxYTcW8o7swxEbjT5_C2SsDvn1yrIO7jnOAOveEwbJoJLZeNwccBl1_ffKcyZf6Sx5D-Az-HWfJralqiNJooiw5LAXKelbOhhzySR87uHtzF4P2X62LofsxpaPq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66d570f341.mp4?token=srdhxH44Z0RGRWjLMLCaAoXCckMp6cBxjMjK4KvamRe-4nvFND4VyNcEnUWqHM1TbG1HfI8UKsZ8qIlNRm6fUkTq2cxhZNcmxW7-qc7OdnW_sxtkOr0_YdTNNlrFnq-N802XOi3wxMoxdGftzYelMgaLf1yQa9TR9dk9XriB5KTiy4EKkfh-jhsj_J0_XXTd142qBCkv_s1rcwccahFAI1uJJinQdHRm3v2CtubmxTT8A-sjjrUF86aN_WEofKgCfoxqG49x41f_ubIuODyA3dSecqGZxwza8DrxIRb2ZqgS7s6w2UVKfThK1hEn79WhKyPPzFmwLyljqgwkC3ut9rkrbrQlFD_akVSvJOQ3cgMZ2N2bSiuesHc2EvJ4pcz-QyVL3jAPIvIcZq9RRUq1fpqhDzzwAp6rs0Prr70v-mRCLMkq8Hf2T_wcWXTY3Qc1NStAEEjCCY5So3fxFvrgJ3G5gJiHsJV3SLq2vKU7jS82X-cMLGx23DkXh1bsA4kFlN3w1ZLfWTO_waaz-zV-hEzqVyKNnPd3eYFALMyP9d5DtSMCxYTcW8o7swxEbjT5_C2SsDvn1yrIO7jnOAOveEwbJoJLZeNwccBl1_ffKcyZf6Sx5D-Az-HWfJralqiNJooiw5LAXKelbOhhzySR87uHtzF4P2X62LofsxpaPq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفت‌وگوی تلفنی رهبر شهید انقلاب حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه با همسر شهید رئیسی، پس از حادثه سقوط بالگرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/akhbarefori/653286" target="_blank">📅 21:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653285">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05e0804ab.mp4?token=Mk4SKdzma1-j6n7qFDPAClhqKuVIBkjIvoNkkViW5Onr6YHOJEYoF_OauPX7yEpoIOC0jwk8MuaZBaqMEHq_MgtCdyZBOnUfPfNfsE6i10bw6RtnzhHhNbhIAlryEoLb34_Lz_tbcNrJ7qx_-MLrx2Trppa1076vILch5hF02KOEdk9n53QOqZYSzOhufV7ZY3qdHH3yTQrR33dfouQywrJxnaoBrsxsENBlNsovXi6i2EgY56_DISz6OsHm6IZh1UfArwDNx7M84DdU1WIP6VSjvtCq6ipaE31yApQbNJlkhIfWc4uPVZJHFvo2OpEBB0trfL6krhvEkPWkBUyuTQENavylVoXSPeS76HPGNMRSRZ7EIubwF7JWUBfIoMIZI_jPn_6wXcHoO1v0kz8qKVt_94P9qbG7Xod-qN5eCDDBJ6n53uqdNsI-ChciWyzkAnHmWH0kCQRxD5vZq-HVVO5pmZP_pLma96YdbA1ZCSePRpBlabLmBoYxHy9GePE3tg_tzUGgJC0_FxD0VY_7oydalT3UqQISXhirc-7F18-V6Q0fu_F4nI7xB4TS1kr9lHi6Baw_zCgkbHU7eF7vEyi1EjZGiaHPw-NFcGbsMuRl4Cycj9kglylD-depEV-JViGvI8QJWneggEhv6KegLj_BJ4vI5Xln3Sz7z_xY2q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05e0804ab.mp4?token=Mk4SKdzma1-j6n7qFDPAClhqKuVIBkjIvoNkkViW5Onr6YHOJEYoF_OauPX7yEpoIOC0jwk8MuaZBaqMEHq_MgtCdyZBOnUfPfNfsE6i10bw6RtnzhHhNbhIAlryEoLb34_Lz_tbcNrJ7qx_-MLrx2Trppa1076vILch5hF02KOEdk9n53QOqZYSzOhufV7ZY3qdHH3yTQrR33dfouQywrJxnaoBrsxsENBlNsovXi6i2EgY56_DISz6OsHm6IZh1UfArwDNx7M84DdU1WIP6VSjvtCq6ipaE31yApQbNJlkhIfWc4uPVZJHFvo2OpEBB0trfL6krhvEkPWkBUyuTQENavylVoXSPeS76HPGNMRSRZ7EIubwF7JWUBfIoMIZI_jPn_6wXcHoO1v0kz8qKVt_94P9qbG7Xod-qN5eCDDBJ6n53uqdNsI-ChciWyzkAnHmWH0kCQRxD5vZq-HVVO5pmZP_pLma96YdbA1ZCSePRpBlabLmBoYxHy9GePE3tg_tzUGgJC0_FxD0VY_7oydalT3UqQISXhirc-7F18-V6Q0fu_F4nI7xB4TS1kr9lHi6Baw_zCgkbHU7eF7vEyi1EjZGiaHPw-NFcGbsMuRl4Cycj9kglylD-depEV-JViGvI8QJWneggEhv6KegLj_BJ4vI5Xln3Sz7z_xY2q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ای که این خبر را شنیدم...
🔹
در سالروز شهادت شهید رئیسی، صدای مخاطبان خبرفوری را می‌شنویم؛ روایت‌هایی از لحظه‌ای که خبر شهادت شهید راه خدمت آیت‌الله رئیسی منتشر شد و قلب میلیون‌ها ایرانی را متاثر کرد.
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/akhbarefori/653285" target="_blank">📅 21:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
شکار دو تانک مرکاوا توسط حزب‌الله
🔹
حزب‌الله: دو تانک مرکاوا در شهر حداثا در دو عملیات مورد اصابت قطعی قرارگرفت؛ همچنین حملات موشکی به تجمعات پشتیبانی دشمن انجام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/653284" target="_blank">📅 21:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
جنگ با ایران ۳۰۰ دلار از جیب هر آمریکایی کم کرد
🔹
از زمان شروع جنگ ایران، قیمت بنزین در آمریکا به میانگین ۴.۵۰ دلار در هر گالن رسیده و مصرف‌کنندگان تنها در ۱۰ هفته گذشته، ۴۲ میلیارد دلار اضافی برای بنزین و گازوئیل پرداخت کرده‌اند.
🔹
به طور متوسط، هر خانواده آمریکایی بیش از ۳۰۰ دلار بیشتر از حالت عادی برای سوخت هزینه کرده است.
🔹
این پژوهش توسط «آزمایشگاه راه‌حل‌های اقلیمی» و «پروژه هزینه‌های جنگ» دانشگاه براون انجام شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/akhbarefori/653283" target="_blank">📅 21:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653281">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63ea7c9e7.mp4?token=ofBDi_FQ-2K7x9RyMyVSnaqKxnKKQU3rl-esyZ5U3UoLs58enApkSqBXLTut-eCNJY85QIIuF4iuvHdIeUk_ce7sLXw5PEt3V5aKAzf1pGkvYoiyIkT1Uy2b6Ei-cI-xq7w2iHve8-JibBxh3otTzCXRrfG3vZE-FHMhMysd8E9A5I08o93cQ72it4HWtFoc7cGaxcq7kx-c3TI2IbRKoK7fhMx_hDRFe5Id6MolZSrcvBuJnROz10p_RyKamNjMXIbP3Kl_QZqMKhVR_YEHrI_c92TYJGjBiOXKAuWiR0eKV7zae6rF0_oVFfVwyIJfZSMpo5pglbrIkxKRz6OzqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63ea7c9e7.mp4?token=ofBDi_FQ-2K7x9RyMyVSnaqKxnKKQU3rl-esyZ5U3UoLs58enApkSqBXLTut-eCNJY85QIIuF4iuvHdIeUk_ce7sLXw5PEt3V5aKAzf1pGkvYoiyIkT1Uy2b6Ei-cI-xq7w2iHve8-JibBxh3otTzCXRrfG3vZE-FHMhMysd8E9A5I08o93cQ72it4HWtFoc7cGaxcq7kx-c3TI2IbRKoK7fhMx_hDRFe5Id6MolZSrcvBuJnROz10p_RyKamNjMXIbP3Kl_QZqMKhVR_YEHrI_c92TYJGjBiOXKAuWiR0eKV7zae6rF0_oVFfVwyIJfZSMpo5pglbrIkxKRz6OzqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار وحشیانه با کاروان صمود، برای رژیم صهیونیستی دردسرساز شد
🔹
سفرای رژیم در جهان یکی پس از دیگری احضار می‌شوند
🔹
بعد از بازداشت کاروان صمود توسط نظامیان رژیم صهیونیستی و برخورد‌های زننده و انتشار تصاویر آن در رسانه‌های جهان، بار دیگر جنایات وحشیانه رژیم تیتر یک رسانه‌های دنیا شد.
🔹
همزمان با این تحولات، دولت‌های دنیا مخصوصا کشورهای غربی، یکی پس از دیگری سفرای رژیم صهیونیستی را احضار و بابت این رفتار خشن بازخواست می‌کنند.
🔹
تا کنون ایتالیا، کانادا، فرانسه و هلند سفیر اسرائیل را در کشورهای خود به دلیل رفتار غیرقابل قبول با فعالان بازداشت شده کاروان ناوگان جهانی صمود احضار کرده‌اند و با توجه به فشار افکار عمومی، پیش‌بینی می‌شود دولت‌های بیشتری، دست به این اقدام بزنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/akhbarefori/653281" target="_blank">📅 21:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653279">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573359b1bc.mp4?token=N85IgcYG_VHYaufh-m3qeM5-IFb8KqO_cAZTSdT0Jt7YQGoLC0JMygeXUSx5Qg94vK8x6nJUQmNJNjvm0DFy9B3gibrImM0Z4gBcbsM6gc7dLOcVSLBhrl8oP2IE41ykhZQ4eXTR1f5ij--D_0EM9LjesEPeYHW1aTgtS8HFxW-N1Z5J6bB__1sV9uDxRgbMeYY-lCS5HHWZNagRF4HXjwTsAE4H1FUFq8gmrv3Xve0WIIyWMmSmMSffjTRUX6fEbFTyhie8eA6g74iwhXUH6SwNUH_UatFZ06FwlEooJn-RBGpj91ub9C8uleQ7jBlvnS9cNhMlB4y4_e06BTHmvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573359b1bc.mp4?token=N85IgcYG_VHYaufh-m3qeM5-IFb8KqO_cAZTSdT0Jt7YQGoLC0JMygeXUSx5Qg94vK8x6nJUQmNJNjvm0DFy9B3gibrImM0Z4gBcbsM6gc7dLOcVSLBhrl8oP2IE41ykhZQ4eXTR1f5ij--D_0EM9LjesEPeYHW1aTgtS8HFxW-N1Z5J6bB__1sV9uDxRgbMeYY-lCS5HHWZNagRF4HXjwTsAE4H1FUFq8gmrv3Xve0WIIyWMmSmMSffjTRUX6fEbFTyhie8eA6g74iwhXUH6SwNUH_UatFZ06FwlEooJn-RBGpj91ub9C8uleQ7jBlvnS9cNhMlB4y4_e06BTHmvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: معادل مصرف چند کشور کسری برق داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/akhbarefori/653279" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653278">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avKVuLsd0xAn-gAAXcF2UYqVzMgoalXUGwdmNyoI7bDKKLAtk5PKnVw3wgLSgtWdse-Jfni85655sUpZQWbBeYzNM2YXNUCmJ8NxvNVHoFbfy5TJorMaSqufqIavVcSDChQQZNcSlX-2wbd_2TegCLuVvBZJ2Ash_O7qJHlLGYylX-lKEPcmTRFMo-9vENRpO1yF_M9sSe7W_3jEpv5LYTUKfr0i6OT1saAkSgInPrsWK_3ikxQwLWJWRNeQluCwamiuafIkGFJ4ixJmpwFQffPm-8bUyI9w-sFQ5Wsi_n1-kIr-RVx80CtfLXvpC1YmUbnu3sii3vMvKL5zvqlYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عواقب جنگ با ایران و کمبود کود شیمیایی، اروپا را مجبور به استفاده از «کود گاوی» می‌کند
🔹
گزارش پولیتیکو نشان می‌دهد که اتحادیه اروپا قصد دارد برای مواجهه با کمبود قریب‌الوقوع کود شیمیایی، به کود دامی روی بیاورد.
🔹
جنگ آمریکا و اسرائیل علیه ایران باعث اختلال در کشتیرانی از طریق تنگه هرمز شده که حدود یک‌سوم کود شیمیایی جهان را تأمین می‌کرد.
🔹
اما برخی مقامات اتحادیه اروپا هشدار داده‌اند که اتکای بلندمدت به فضولات گاو کافی نخواهد بود. هربرت دورفمن می‌گوید: «کود دامی می‌تواند یک کمک باشد، اما هرگز نمی‌تواند جایگزین کودهای بر پایه اوره و نیتروژن شود.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/akhbarefori/653278" target="_blank">📅 21:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653277">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqbpG4eOSbyZxpOBiipJ0_K25yrUmjbFFZtYNRLFwtAgsdVxJJ8EOh0LZDdVVEw104if0ztOJQpw5ovOKr7SEltm9POgXrfcRy6PVo3QxFYiIZhcHv0cU0oA5LtnU1UcDTxzrRToAwpzbg07Kxu0pTTLcifdIIRHQrLo4hAttS87bTeVhyhnkCtqewaRZWzuTgGtU42i9w5fVWt4ukrb_5C_HnFv9A2mMwH7HloBSDttEz_JbKEDqHffT99E7_SeTli9Id8EzvFHpqzk9iIbMZRAXBotC7uGEZlD8CUYQaC34kgC2PrF2qEKk3pf-UlSVhaBa6U4nw7sqDDgQXsRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهم گروه‌های کالایی مختلف از میزان ترانزیت از تنگه هرمز
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/akhbarefori/653277" target="_blank">📅 21:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653276">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای آکسیوس از گفت‌وگوی پرتنش ترامپ و نتانیاهو درباره ایران
🔹
پایگاه خبری آکسیوس به نقل از منابع آگاه از تماس تلفنی «دشوار و پرتنش» میان دونالد ترامپ و بنیامین نتانیاهو درباره تلاش تازه برای دستیابی به توافق با ایران خبر داد.
🔹
دو طرف در این تماس درباره ابتکار جدید برای رسیدن به توافق با تهران گفت‌وگو کردند که به گفته منابع، فضای آن «سخت و چالش‌برانگیز» بوده است.
🔹
یک منبع اعلام کرد نتانیاهو پس از پایان تماس، در وضعیت خشم قرار داشت.
🔹
به گفته یک مقام آمریکایی، ترامپ به نتانیاهو اطلاع داده میانجی‌ها در حال تدوین سندی هستند که واشنگتن و تهران برای پایان دادن به جنگ آن را امضا خواهند کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/akhbarefori/653276" target="_blank">📅 21:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653273">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8zTehZGabJH68yqMli8T2GsxhPOcKqnuMBxFT_Uql6A3TVnMS1FM-sy2vBrBObBi8NR11s3dUM-Kxf7t9BQ3XfxgFuQ-86OHfNYwehOCl1yLBPHZhxexOfO2Fwya7JYctsXPHxPjSAgm_kpVC3h0bVK0VWzGyYn8c10IsEm-aAM0Ew41P-B_3IodefNIjb8-d9uhnRe86mW6tooGx22qycMmeLt3_JWjSvcaJZCEFXHCFIqYe6iFs4darVhDhykLHgUalbhUJfN2CDvQv3VmLcnpnoMSn3KxUyKv8ecuUCXzqONKFe8l6IS_D1NYBilbjTvzUGxMkifPwMqm0HthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه پاکستانی: عاصم منیر فردا به تهران می‌رود/ احتمالا خبر مهمی در راه است
روزنامه ابزرور پاکستان:
🔹
فیلد مارشال سید عاصم منیر، رئیس ستاد ارتش، به عنوان چهره‌ای کلیدی در روند دیپلماتیک ایران و آمریکا، فردا به ایران می‌رود. در طول این سفر احتمالی، انتظار می‌رود اعلامیه‌ای مبنی بر تأیید تکمیل پیش‌نویس نهایی توافق منتشر شود.
🔹
این سفر می‌تواند به عنوان یک نقطه عطف دیپلماتیک سطح بالا باشد، جایی که تکمیل نسخه نهایی توافق ممکن است رسماً اعلام شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/akhbarefori/653273" target="_blank">📅 21:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
امارات وقف آمریکا شد!
🔹
آمریکا نقشه‌ای مرموزانه کشیده، جریان خارج شدن امارات از اوپک را حتما شنیده‌اید. پشت این اتفاق اما نقشه‌ای کاملا حساب شده است.
🔹
شاید جنگ با ایران هم برای همین نقشه اتفاق افتاد!
🔹
ماجرا چیست؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/akhbarefori/653272" target="_blank">📅 21:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOFeOH2meMMHqtg7QlinhEHiI0AwIhSEY0IfslJzlo_AAuNXyqMYuwniq4BsHA40xBFMVLeFXS8B1EqOIOaONCGt-T0UowwKefeA3D5bH-qjikn4Fq2yKnGsrxp201tUxV6iZMKumRkiE37rpib-KmFsmUqla5Le8_4Z35EiGfwTexbHg2KWod3vXstY7A1drjOb2CfebSj_74Za9WjHpo8MJ90_TT93BpdPRYxOA4bEsv1xYZvls3ExXyOsoKbq0VGp9jDGnUFdO3tqxarW4-8-gMJWD10xZa_70wgLABSIxLCF_2DLLgMZ8Yu9cvZKb7wLxJN9zj6M6BfsKFEN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی در پاسخ به ترامپ: ایران شگفتی‌های زیادی برای آمریکا دارد؛ برای هر سناریو آماده هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/akhbarefori/653271" target="_blank">📅 20:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653270">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWSa7u7XyLPRQaTou_XJBf56AiSq0P3YF9oS1anIHxc-gu7pSqVvZ66ZtLAvQXE2AZGROgYftFKV2zToUu_ajYTpao22PRkLLShJW-r1uCMcCfsqkZQpGrdoWb5s3ip9jgmSDJzsKc0vsKBo8q3abgJs3Vvo2HY3tJd7DUVSMjlbaOUW6lBs3P5CEp_1amItcFT36B5CS5IPB_JyHbzXRZb755nOdQf7ZV05IVx8EV1pP-4KICjkWY8T-MHny-HYpNQwpo6TvU_-qXzgaJFRpTinYt3VsXMw9nx3gJfcZZSXXrEiqE3OUoqGSZ__brisgBsIm6e8rHS9Gm6TntzrXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت روی تخت بیمارستان افتاده
🔹
هر تکه پلاستیکی که بیرون می‌آوریم، یک نفس تازه به زمین برمی‌گردانیم.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/akhbarefori/653270" target="_blank">📅 20:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653269">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: در این مرحله متمرکز هستیم بر خاتمه جنگ در همه جبهه‌ها، از جمله لبنان
🔹
مطالبات ما مشخص است؛ موضوع مرتبط با آزادسازی اموال بلوکه‌شده ایران، مباحث مرتبط با راهزنی دریایی و اقدامات ایذایی که علیه کشتیرانی جمهوری اسلامی ایران انجام می‌دهند، این‌ها مواردی است که خیلی روشن از ابتدا بیان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/653269" target="_blank">📅 20:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653268">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4nGaDCPJ2WjW2g7ZpMYthxrMaUZMUkVF11n_pL4UMCMLcAneCBvpI2bv5MPBMYJtwyEUt-kpQBPnz5Ze2Lag0mae8EM7vsjQj2IMa-wacmTbuteRNobCY9mT_9wZad2Y1FL0s3F0EeeB9CnIA0Alh5uZx0Eu4j-39tlQihXmafHrv6t0P54FNUIsqtlS3vQBCeQus_pcfWmXFfpzTk-aDNc4vrvGdxAWs0L7XqphRPVFsaG4EXWmoZQOFbwZ0OI8faFr2WORFB7WiNexm2qr33JzOWrAqPWwIgh38-sk6P2fQsg00CXu5Shql2k36vbDLsxRyfmW_P2J1gGr2MiAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ادامه موضوع ارتباط شرکت فیلیپس با اسرائیل و جاسوسی این برند صهیونیستی
🔹
بخش دیگری از این مقاله قابل توجه است:
🔹
«شرکتی مانند فیلیپس علاوه بر این در سراسر جهان فعال است، ویجور (افسر اطلاعاتی هلندی) اضافه می‌کند:
🔹
«نه تنها در هلند، بلکه همچنین در کشورهایی مانند عربستان سعودی، لبنان و امارات متحده عربی. این موضوع به شدت برای سرویس‌های اطلاعاتی اسرائیل مهم و مرتبط است. همچنین به این دلیل که بسیاری از فلسطینیان بلندپایه و صاحب‌مقام به این کشورها پناه می‌برند تا درمان‌های پزشکی‌ای را دریافت کنند که در غزه و کرانه باختری امکان انجام آن‌ها وجود ندارد.»
🔹
حالا جالب اینکه؛ نمایندگی ایران فیلیپس در سال ۲۰۲۳ عنوان best seller یا همون بهترین فروشنده در حوزه تجهیزات پزشکی (همان سی‌تی‌اسکن و ام‌آرآی و آنژیوگرافی و...) را کسب کرده! در نظر بگیرید که چقدر دستگاه در ایران فروخته و کار گذاشته شده است!
🔹
حضور مأموران سابق اطلاعاتی اسرائیل در توسعه نرم‌افزارهای داده‌های حساس پزشکی شرکت فیلیپس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/akhbarefori/653268" target="_blank">📅 20:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653267">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe81d225d0.mp4?token=CHpiZv8LNiugEB2sAP9D1cwAyxF773qKT-UQ0KZVaGWJYONKRSiuLEHhZh4c1Z1tk-IFUQbDFcwYxWMJF8JcCJmBGhaXVd_E7S1X0EgmP05rRlXLGHvflDxjzMKM0xCLr7JBh6c0BcvhJKzC4x-ynBJE8XmTPIxftPM7hSI8fiBLohVwu5PwPZzico-XYUG4FlItOsP8Yj9HKpOcWTzcyJD0YOibukZ6hNKivl9QKFFGQhVBrVVPnq6_Da2C9BbLjSFkwWEbtuuEL1EnEBqBQ3XfdF331KLF9dGvzMgOUpvSmtc-Z9CBSjnnVh1OdRdv9JDrwfv20TSXTxQI2R2jIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe81d225d0.mp4?token=CHpiZv8LNiugEB2sAP9D1cwAyxF773qKT-UQ0KZVaGWJYONKRSiuLEHhZh4c1Z1tk-IFUQbDFcwYxWMJF8JcCJmBGhaXVd_E7S1X0EgmP05rRlXLGHvflDxjzMKM0xCLr7JBh6c0BcvhJKzC4x-ynBJE8XmTPIxftPM7hSI8fiBLohVwu5PwPZzico-XYUG4FlItOsP8Yj9HKpOcWTzcyJD0YOibukZ6hNKivl9QKFFGQhVBrVVPnq6_Da2C9BbLjSFkwWEbtuuEL1EnEBqBQ3XfdF331KLF9dGvzMgOUpvSmtc-Z9CBSjnnVh1OdRdv9JDrwfv20TSXTxQI2R2jIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: آمریکا با «راهزنی دریایی» زنجیره تأمین انرژی جهان را مختل کرده است
🔹
سخنگوی وزارت امور خارجه با محکوم کردن اقدامات اخیر واشنگتن، آن‌ها را نقض صریح حقوق بین‌الملل و عامل اصلی ناامنی در آب‌های آزاد دانست.
🔹
اقدامات غیرقانونی آمریکا نه تنها در منطقه خلیج فارس و تنگه هرمز تنش‌زا بوده، بلکه موجب اخلال در زنجیره تأمین انرژی و سوخت در اقصی نقاط جهان شده است.
🔹
جامعه جهانی باید واشنگتن را برای پایان دادن به «راهزنی دریایی» و رفتارهای خلاف عرف بین‌الملل تحت فشار بگذارد.
🔹
این موضوع به عنوان یکی از محورهای اصلی در تمامی تبادل پیام‌ها و گفتگوهای اخیر، از سوی جمهوری اسلامی ایران به طور جدی پیگیری می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/653267" target="_blank">📅 20:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653266">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
حنظله: در صورت خطای دشمنان به شبکه‌های دیجیتال و انرژی آنها حمله می‌کنیم
🔹
گروه هکری حنظله: در صورت ارتکاب هرگونه تجاوز یا بی‌مبالاتی از سوی آمریکا و رژیم صهیونیستی، حملات سایبری ویرانگر فراملیتی علیه زیرساخت‌های انرژی و دیجیتال کشورهای خصم اجرا خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/akhbarefori/653266" target="_blank">📅 20:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653265">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: نسبت به موضوع حاکمیت ایران بر تنگه هرمز تاکید داریم
🔹
قاعدتا هزینه تامین امنیت دریانوردی تنگه هرمز نیز باید پرداخت شود.
🔹
طبق حقوق بین‌الملل مجاز هستیم که تنگه هرمز را برای کشورهایی که آن‌ها را برای خود تهدید می‌دانیم باز نکنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/akhbarefori/653265" target="_blank">📅 20:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653264">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsLm7y7c3dgn7ars835oRWU-hyVkRSu-v7uEq20gM-DflODZWtAcXuLYKtEDaB_ewQYU6YnkUn9RRsOMof7JVmH61yswF-v3AmfGk5Xo3O2qE49nTZ9gicKC_y4osd3V51pUXskvRv3hk1az5CQPRJZDIzm1Rec_YRb15OjnZhNGPkfSVFv8-vM0n1IubGabrl8Wqim7U9cR11KAr_OfTsZk8Dc5ZVlEHRUmZQXzLpd3BR8lzYWQbR5ikOBg06S-AbFFxH3t5NimQEVTYeizk8MLJyfFb0IoeqU8ucSql-cvqMuNaMl7v_pOWiMBZKG-GMhzRk307ElkkIa-03iXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گره بگشایید
🔹
رهبر انقلاب اسلامی به مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت پیامی اعلام نمودند. ایشان فرمودند: امروز شکر نعمت انسجام ملت و دولت و تمامی دستگاه‌های جمهوری اسلامی، در تقویت انگیزه و خدمت مضاعف و مجاهدانه‌ی مسئولان، گره‌گشایی از مسائل و دغدغه‌های مردم خصوصاً در عرصه اقتصادی و معیشتی، حضورهای میدانی و مستقیم، و تعریف نقش جدّی برای مردم بعثت‌یافته در مسیر پیشرفت کشور و حرکت امیدوارانه به‌سوی آینده‌ی روشن است.
🔹
هفتصدوپنجاه‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/akhbarefori/653264" target="_blank">📅 20:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653263">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
العربیه مدعی شد: دور بعدی مذاکرات ایران و آمریکا پس از موسم حج در اواخر ماه می در اسلام‌آباد برگزار خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/653263" target="_blank">📅 20:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653262">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
مجاهدان حزب‌الله: تا اخراج اشغالگران آرام نخواهیم گرفت
🔹
مجاهدان مقاومت اسلامی لبنان در نامه‌ای خطاب به دبیرکل حزب‌الله تصریح کردند که ضربات مقاومت به ارتش رژیم صهیونیستی ادامه دارد و تا زمان اخراج اشغالگران از خاک لبنان، آرام نخواهند گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/akhbarefori/653262" target="_blank">📅 19:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653261">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg2DIehjTLBXfxkpmD0N9nkgMzFZobIzjKc9t43B8LyKPoWiuigsoLHDQO10YTZE4JbI4UMpdq83sjnXQlyoO40uIpfS11wbwb7y14Uuj2Sh3A744UEkBtAVDazqLdDXaKRXzsxFGsS_kdJVRM3I8nElIlPNr__GOk0XLTqMmaInCHql4jNYzqvcQZ32cWqxH2N_DZiDI2qx2g_10ZiM0DHFNCMc6TXN9VpBV7Mdxe02N8X_d-ms2M5xj9471HqqslMak_PXvUkhumFlIC85oYWuJjhv7d6bfMdGtFWUxa6LGoHoIP6fKz8kI0APkXY-_nFxHKZTuYswpcUJw2Rg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رمزگشایی از پیام مهم سپاه به آمریکا/ آماده برای جنگ در بیرون خاورمیانه/ «چراغ خطر» روشن شد/ این مناطق در تیررس موشک های ایران هستند!
🔹
در جنگ قبل، موشک ها و پهپادهایی به سمت دیگو گارسیا، مدیترانه، قبرس، ترکیه و ... شلیک شدند. این شلیک ها اگرچه غالبا مورد تایید قرارگاه خاتم و سپاه پاسداران قرار نگرفتند اما نشان دادند که ایران می تواند در صورت نیاز، مناطقی بیرون خاورمیانه و غرب اسیا را هدف قرار دهند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3216611</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/653261" target="_blank">📅 19:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653260">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ترامپ: ممکن است لازم باشد به ایران ضربه سخت‌تر بزنیم
🔹
رئیس‌جمهور آمریکا در سخنرانی خود در ایالت کانکتیکات درباره ایران گفت: «ما به آنها سخت ضربه زدیم. ممکن است لازم باشد سخت‌تر ضربه بزنیم اما شاید هم نه»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/akhbarefori/653260" target="_blank">📅 19:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653259">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIv3HiMEkoYiT7EiFwCWsGhaGoyp8Uw6r75eI6ZGiw_GskTjeDRINzqXqa1MVpaFxgVvXMzMsc2lZm5AeF3b_2NwMTbJHoSFPhPmQB4Uv-sKCOqYZZctOYe6w95Eurx9VsZO1iVSP5StqoGtfxi0Huu9BFaZyPUWopxpRqEnVA0-lMhUi_EN0tBdmC383Jc1BQfnwpMlXbYxD-v9qIgtDGTXUS2OSqniZ_32p3UUZ61K_ELGMhTd2FRK1ZatCVxmcIpWj2Ia8wj5nXLdtQJIf7hoHqjnSSJOUSUzA2N5q2wo4skRb2lHLpuEPX9SHic_aCOjP6H1OyGyIgj10IEHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهمیه وام قرض‌الحسنه برای زندانیان نیازمند اعلام شد
🔹
بانک مرکزی در راستای اجرای قانون بودجه سال ۱۴۰۵، سهمیه هزار میلیارد تومان تسهیلات قرض الحسنه ویژه زندانیان زن و زندانیان نیازمند را به بانک‌های عامل ملی، تجارت، ملت و صادرات ابلاغ کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/653259" target="_blank">📅 19:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653258">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ccda1ed3b.mp4?token=HlDKCut-Vs-WMw34WhzLKXlIxbDmb_OUMj5mPQiPTnosvxqhzdpad_I4-WptgtXpS5NpIaN9rxqF11XZxa2gg-BCStYroHAndy8ZaCKCC7RTJn-Hff4YPXfa6VBCu1WFa9Nuhm2R6dE8AGGGFV7f76-yLbD9nNInqKuPobU7YNPALf5sYxNWN2jDqWulSc4MLJBWtGAl4eROXzOelb_s8JJyXMbShSp1lD8SCEttD9ACiPyaFQ2MzkWZc-ElyYUHa02Ne28ag58_Vq6__fptjTHW94IwQOdbD62EDDgHD7Vu1-pQt0yiLeaAQwu46CQ0TDJYkqT7HnzzVPizJOyHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ccda1ed3b.mp4?token=HlDKCut-Vs-WMw34WhzLKXlIxbDmb_OUMj5mPQiPTnosvxqhzdpad_I4-WptgtXpS5NpIaN9rxqF11XZxa2gg-BCStYroHAndy8ZaCKCC7RTJn-Hff4YPXfa6VBCu1WFa9Nuhm2R6dE8AGGGFV7f76-yLbD9nNInqKuPobU7YNPALf5sYxNWN2jDqWulSc4MLJBWtGAl4eROXzOelb_s8JJyXMbShSp1lD8SCEttD9ACiPyaFQ2MzkWZc-ElyYUHa02Ne28ag58_Vq6__fptjTHW94IwQOdbD62EDDgHD7Vu1-pQt0yiLeaAQwu46CQ0TDJYkqT7HnzzVPizJOyHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: کار را در ایران تمام می‌کنیم یا آنها سندی را امضا می‌کنند
🔹
رئیس‌جمهور آمریکا در سخنرانی خود در ایالت کانکتیکات برای چندمین بار به دوگانه توافق-تهدید نظامی روی آورد.
🔹
او مدعی شد: «هم‌اکنون در ایران همه چیز از دست رفته، نیروی دریایی‌شان نابوده شده، نیروی هوایی‌شان از بین رفته، تقریبا همه چیز نابود شده.»
🔹
وی اضافه کرد: «تنها مسئله این است که آیا ما کار را تمام می‌کنیم یا اینکه آنها پای یک سند را امضا خواهند کرد. ببینیم چه اتفاقی می‌افتد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/akhbarefori/653258" target="_blank">📅 19:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653257">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXsVuTdi0wRgwTeI0hLv0SZ6qp01WEpD02e2yscxGSu5B1k_qrh1-J43E4lbbNiV4MjCdQ5CW3DzHFw8-AmiLPf3uc22u0tuXBih-vYRhIwwpROddgphbkhYsTdQeiGo9GF3v3EtIgrBW7J4oCYHJ8PY2-zUV9mY8_fVmfe8cqi3m2tbivgFhrEnwG7mIEnxkxQUoTRdBoPzASIS07-Wxb7Z2SkKJ7ngIl_QZhlEpX-NfM_svULVyD60cgn5SOE2KdHp9PxlxcB_ANiIJOl4lgPoxUK2STtwT2RlBi-MFUMokgSNmBb81bQUiJOOv7PsxsWkmei8rEWqGvpCMQHNhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معنای جدید «دیکتاتور»
🔹
فایننشال تایمز: ترامپ و پسرانش «برای همیشه» از حسابرسی مالیاتی معاف خواهند بود.
🔹
وزارت دادگستری آمریکا به ترامپ، خانواده و مشاغل او، مصونیت از حسابرسی‌های مالیاتی می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/akhbarefori/653257" target="_blank">📅 19:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653247">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gM6JQcZrlPapjPaoKRS8KjaIt8qXScdB9kireE6Toguy84XL-sfK7lAjjXasbAMTjr6RoTqEx0prDE-UrNRw0gIgoAouxzMwUfirNxlHXyDrSSMZ759QT3Xs5iwbS9fTHOnJvRx0HF2u9JE0RvqlTzmzfoo3wN2EPLz6dPNum0OC4nZq9qUnm7cEtmMpHfbU6sbYCTixavYH3CMQTkfyMBlof6kkADtp9OwQhLHU9O7-3Rd-QiYW09vG-SfUiOYVXnKc54lEjh3SgyzqpH92PAREBAz1LTagdgRU7f5uKay65QQ02NuSfODgy7gAqf9EKqxWsrg592Op6TfHDHPRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BskZddYP_JW-SlmJG84Ox8DvMioH7m_NSAuHF0Fr4ULez-2Aj5ltHccMdAlL9H2tPw9St9xmOqWNfIVsjqz4zPTrCsln3-UjjvUhpMXu-aRAkuuf2vprv_OD14CuCk9GenMXyjB9mGk84XKXYU6nQtYB8sKY0H4EHSUVubSMWMQJkf0UQmbgLheaSxjA_n6LVHZecXdr3Wbm1QXZ667JAUaoCCQ4DSI0iBwL5fLGGFRMS09-EFzB0or2ICNO7cBEDpfB-174iQe133Hjngr8ReMP8-jda_GUSRXGBJAtOdU2ykk_7y_0Jo9hy5A_wzvInVFDqWszWqImsrfqD51Itw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYyNAJhKvTtgTlAU4kCvMycIDMiUm9sspUawUBhiDx2uhNt6zZp4Unh_UBcFQn19M5Xsj1fGubfCp6v9O53EnfQetTkwNJ_pWAazbukn3vuIuijMqWdKDh73c5FfFOb5_ZVngR3gRAStpHKPYJg-thTLqcZZyPDWDMM81lyQYwjom79LS-ybM45ZJ-vvqWy7Su0lTQq10_WIEjj73op3DON7JGh9Jk62Nu4H7uLo5aPhqYUSSz6CLOeIEWaGjHxBZIwa-RuBHSDhhY_gR7uVBzm7x2V7-rGY_zeWU5jN4K8weE9NLefZKZn1gQanCbZ_1xjJm4AeEOq8qnUHM3zHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVPsqO97S1FVFrMbb-zkwq4z2XocXxK9tmEpxCc5JVHDFkRsFfth6W1dGxX1WVkaXmIVPWxPJabzpwUiYwEJWfEnLuh5MUNQXyGqZ8iAOUkvMOLZtqIdnY9IxY37zwX5yy7K2MrTGc6a9MlzB2h5roULNFYTNObHsvZ10d5mwVyoZeHeaFFNOUih7eG_DIpiuax0okreh2_dNrrmHgggit7PhxtBuHp0oWhB4rZkD2c-1oENCxsgxTMCxgjcqDfWNFSL9bb4ydPtbLIKvETh-klkBudYDARIqULpTjmQmxfZOGTeEnTk0MJzOcSSaHqcU1T_8PeyrqYj_UQu6WYKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/budCALh4Y8ZbMUhWTOFRFhzyZNAUiKCtOHrsPxw-rrBqs6DkCYgS84uVrZsnaF0cgIhWJMEFuZYosQaHQcjveNRZSy3jfzR2PcOt4W7MkRrFdLCJiDA1JqNkeVk4P7Ros4hcFU_iBWbsKEx2KY7Be0IwSqPWQwPVGrsrFd7hVJwvtBDDhYlH7N-nEeoIObq8ma5ReU3eHpx0JKzhEoZyv4ZRMsc97qbb5wXkeRnfslF4L6RimJ2QIUGkIopwqJiLrsv2QJnjjtk8UMCyKqdJp1ZQMa7FWkaClTnlfEW1mxlUDkdTCTvMRoJt8Rf5qZj1UcSJx_IwZ0mcqj9pJIrIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMCPzSp7kgFdI1Xvz3PtP7nnxldquaPMkDnElV0odlEB69x1HXTgEJMN54SpPsiOCjbBepnhoBIPq7eQfib_e3-kOrgy5xVizqW1MCewXCrQes5G9DOiyIf1nGa3PF_PwfEGn28Ut5lr4eHxiiAH0z0iuBAermr9onGlVU7H2P6uh1QXDwgr7UB20Ea-iflG1owzoN87zl954Tu8l9U7ev6Do6h3O4wqzfr5LhimOXHS4Jbh6NOultXYDBR09ame_c9WSgmH5OUq247BBUiCYRziWLP9TIxhCxVlqhpLr8ZiGRaJxqePNghMGgYRhPzmjKwhlOwnsYQb59f41OT1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbaG1VEr5sqWniAXiPpDu3XO1Ws8vlFwMaGeXRBsrHXh-PLRcI8YUpOi7irCBDmGreuwgt8dhEoMIKt6NNp3dlKeR3xFqRc7rwRUsuv9hxx7pMcBrc3zd0XzIJtPUOaaFEDgYmIAOk98oD72pKf3LYvNfvbqtPdXn45X4t4TqdIytmp6BxEtyi24hwvn44YE-DZ3XElpr4TmQ1J-4Vm4BGzLJ0bl-HsyJ5J8t4Aowz8L6mbYWkJmAiacSUfOg9yabWBiIRgQkHNaIgjg2VS7SaFovP91MZqc9Y9iISFz3dZB-Y12x2SyLRLMxxVWChmmcAcdBbVXgIBvFjlZVSxtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lm5jAi4vp5JOEzI09O23q2_e-XpsKPalXfApacQJI43_0pYeHEFweYhWxEAZGMwY64fM7BHfTSmpKxVo1W247VPc9hb2ILVoxPorDDoeY3pfCDQSuhoy5DRAJe7IDMpsVA0TUyOmQ7VL9R6UAJQMSSifphX_869E7wbBq8oitQHSObGJ4ftWLKaC5KGeelBugxxCpEZHg3V8x3wFugv4lJ4g8nuXKMYr6WljvrkUaGV5CkvzBWf9OqwJWRB4pCTKogxzhwb9U1pSYqIXk_YuiZgM2pV_9KSy5F4yaEny8AUJrGPT6V-lYH02NkCyK99eFEvRVSTLMI2HSI1W1vtzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gD0BFW-m_sgXo0vYlP7VS_X9PcDZ0LMHeGmvjUouZtvkRRQKFOcJtAA3eK_1raYD9NYZ8Ya8Q5f43tfXiywrlnP0Cn4XVRbfI2JuBOLH8s581mSgJZasFxku53hQwNHKccnWakZHCwhR9-L1HYH3eWn3dY0lEnN819rMg-1OjXwS2-LGFeyRV6__oNfItfDsrUu22lT8YrMfdf_4kgeFf7bhHOj-DSkWPRRmF-WtQ9iPOdE8ppsTzuACecnhc0Lu1NRlVUe55_w-KjDRDLHklomSZJQaiMYDpaYg-Q35vRfWtZbjrDKHzoylSVXSmj7LMMc5_PkVbJ__V_-8WqM15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwfI7ZdYPJRxC7l1aZmyGreiYS8gObTtzcn4XVCFbTMV7n6CP_qV901u_KoJ-lCLklxHkXbE95MClVPJs04CO9LaFDoZcZWbm-tDP8J2GToDv7DFfeHUlKo9F9t2q3KZqveEFIi1fUEXroopg8ORG7gIyObpCL7RSolID9vtD9KyZ0tO6OEermrBUJRVrUHoUlMNnNpWjVjG_4qwWU7HIIu7T-jVgJ-scIjI8EWFVKrXnlCgqyD_Uw1u62RvelBbIidPWFunubAt2XODhILRhyHVzRRlwQztAphVbn5mLavuM4gOEWVhlnVQxomxqcKbUFRdxK8v0fdo30kjQvWCuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت همدلیِ واقعی
💫
✨
#همدلی
اینجا یک شعار نیست… یک جریان واقعی است.
#هیات_قرار
با همراهی شما مردم عزیز، ۳ رأس گوسفند را قربانی کرده و گوشت آن را  در راستای حمایت از خانواده‌های ایرانی میان خانواده‌های حائز صلاحیت توزیع می‌کند.
این جریان، با شما زنده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/653247" target="_blank">📅 19:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653246">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
معاون ارتباطات دفتر رئیس‌جمهور: افزایش رقم کالابرگ تقریباً قطعی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/653246" target="_blank">📅 19:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653245">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588caef96d.mp4?token=tOgeE8dSPXWsGkjGt4O7X1YblCsgfpAD6JTiQNZpybNY1SHDKhXSZBreFnFu68TL9qf-BKOwnR_l3vLLq5gzT1ov5CwutvngxayswATJn7jUVbzmnSiNduL49qNyNDWFQFRo1NyfWby0Qp9QiBw2wdJ0utBpvhGj0voLvJjaSLy6FVPVXrqkvwVmDtNR5755yRNJmZhHGyKfE07MQlNMmzTfMATnLZM0C_klYixYNxc1kJ20Upg9rhTdbk9bMg_IRSdVuwlOz8O0XXEu0y8iAdR2DAC2RDm2nZA6-wWBXTYwJAcTF7okP4KuL2KdZoAowB4HeBtjr0U2Ct6FT9VOiSxOpaUQnpArEth75b7YmEIf_HD6ytDOM8R1DqlKY9z7q0OCPqfQ_YNQZC4wl7Fdw9-7j2TnhbPH43q_g_bppuuebj15HY6MBO4PVql92N3PePzFCQBPGqKPkd1fOayHQGJxg_s8O_sF__srMH5au-4CC8Wywj-Oalw6zXhyGR2sitnb7av8AoCC2_C-gIothd5btduSRAyGNo1iqYzMJoctsbcAaBnFKNRTkO4PArNg7W8DScRAbGKPCvcyYzwtYMyMbX18ABU3pC0srXWhbQ6d0KAwGjo-yf0Hu9-akH6mG93NCZFd2Vo6epHRB9inBkvJoAsBEMXixML4F3GL4iI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588caef96d.mp4?token=tOgeE8dSPXWsGkjGt4O7X1YblCsgfpAD6JTiQNZpybNY1SHDKhXSZBreFnFu68TL9qf-BKOwnR_l3vLLq5gzT1ov5CwutvngxayswATJn7jUVbzmnSiNduL49qNyNDWFQFRo1NyfWby0Qp9QiBw2wdJ0utBpvhGj0voLvJjaSLy6FVPVXrqkvwVmDtNR5755yRNJmZhHGyKfE07MQlNMmzTfMATnLZM0C_klYixYNxc1kJ20Upg9rhTdbk9bMg_IRSdVuwlOz8O0XXEu0y8iAdR2DAC2RDm2nZA6-wWBXTYwJAcTF7okP4KuL2KdZoAowB4HeBtjr0U2Ct6FT9VOiSxOpaUQnpArEth75b7YmEIf_HD6ytDOM8R1DqlKY9z7q0OCPqfQ_YNQZC4wl7Fdw9-7j2TnhbPH43q_g_bppuuebj15HY6MBO4PVql92N3PePzFCQBPGqKPkd1fOayHQGJxg_s8O_sF__srMH5au-4CC8Wywj-Oalw6zXhyGR2sitnb7av8AoCC2_C-gIothd5btduSRAyGNo1iqYzMJoctsbcAaBnFKNRTkO4PArNg7W8DScRAbGKPCvcyYzwtYMyMbX18ABU3pC0srXWhbQ6d0KAwGjo-yf0Hu9-akH6mG93NCZFd2Vo6epHRB9inBkvJoAsBEMXixML4F3GL4iI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس مسائل بین‌الملل: در ۴۰ روز جنگ نظامی نفت می‌فروختیم و وضعیت اقتصادی کشور بهتر بود اما الان در آتش‌بس تحت محاصره دریایی هستیم و فروش نفت ایران هم آسیب دیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/akhbarefori/653245" target="_blank">📅 19:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653244">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fe887bed7.mp4?token=kGhL_T0lxq8qBrJJyNfKGYxKKUTm6tNtJlB885ScfJ4zl6cA1ziWs6NJftYSOzJ8MY8QgrTtVROhObGrRi4-yZQaRgPyFR7n1CxFnxdkSR3gnvvcbEHJzELOcc5gmQWmQBY3QS3SrJIItf2Qce-BlF7Kun1CMlewYWUvfKNIUBdk1edIpnUa53zbq1gKReWtRRiuHQaGuhmnJpYbBijDod1AjEC9PzhAP71_WODUSJ_1ZJDBgET57IdUZHURJ_v0ukE0s1h5_7zOKo-kp4IZcERW5-7RyDSLFV5-wfXQUEW6XuCusXISQ4fqMzTjZQho4blMcFN-a4muwf7gVSVcrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fe887bed7.mp4?token=kGhL_T0lxq8qBrJJyNfKGYxKKUTm6tNtJlB885ScfJ4zl6cA1ziWs6NJftYSOzJ8MY8QgrTtVROhObGrRi4-yZQaRgPyFR7n1CxFnxdkSR3gnvvcbEHJzELOcc5gmQWmQBY3QS3SrJIItf2Qce-BlF7Kun1CMlewYWUvfKNIUBdk1edIpnUa53zbq1gKReWtRRiuHQaGuhmnJpYbBijDod1AjEC9PzhAP71_WODUSJ_1ZJDBgET57IdUZHURJ_v0ukE0s1h5_7zOKo-kp4IZcERW5-7RyDSLFV5-wfXQUEW6XuCusXISQ4fqMzTjZQho4blMcFN-a4muwf7gVSVcrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: رویکرد وزارت اقتصاد رشد قابل‌توجه بهروه‌وری به کمک اقتصاد دیجیتال است
سیدعلی مدنی‌زاده در حاشیه جلسه کارگروه ویژه اقتصاد دیجیتال هیات مقررات‌زدایی:
🔹
بحث اقتصاد دیجیتال باتوجه به رویکرد بنیادی افزایش بهروه‌وری در اولویت وزارت اقتصاد قرار دارد.
🔹
اقتصاد دیجیتال نقشی بسیار کلیدی در افزایش بهروه‌وری همه حوزه های اقتصادی کشور دارد و ما امیدورام که با توسعه اقتصاد دیجیتال رشد بهره‌وری اقتصاد کشور را به میزان قابل‌توجهی افزایش دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/akhbarefori/653244" target="_blank">📅 19:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653243">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
معاون وزیر خارجه: ترس اسرائیل از کشتی کمک‌رسان، ترس از آشکار شدن جنایت است
🔹
غریب‌آبادی: رژیم کودک‌کش صهیونیستی کشتی‌های حامل کمک انسانی به غزه را متوقف می‌کند، آمریکا هم فعالان مرتبط با ناوگان کمک‌رسانی را تحریم می‌کند و نام این همدستی را «امنیت» می‌گذارد.
🔹
در این منطق وارونه، غذا و دارو تهدید است، کمک‌رسانی جرم است و محاصره‌ای که کودکان را گرسنه نگه می‌دارد، «دفاع» نامیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/akhbarefori/653243" target="_blank">📅 19:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653242">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
تیراندازی اشرار به خادمان امنیت در سراوان
🔹
یک پلیس به شهادت رسید
🔹
دقایقی قبل سرنشینان مسلح یک دستگاه خودرو سواری به سمت خادمان امنیت در یکی از محورهای مواصلاتی شهرستان سراوان تیراندازی کردند.
🔹
متاسفانه در پی این اقدام شرورانه ستوان سوم «امیرحسین شهرکی» به شهادت رسیدند.
🔹
اشرار مسلح تحت تعقیب پلیس قرار گرفته و در منطقه پیرامونی طرح امنیتی و انتظامی در حال اجراست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/653242" target="_blank">📅 19:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653241">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
اسپانیا: اسرائیل وحشیانه رفتار کرد، باید رسما عذرخواهی کند
🔹
وزارت امور خارجه اسپانیا: آنچه بر سر اعضای ناوگان آزادی به دست اسرائیل آمد، وحشیانه است و ما خواستار عذرخواهی رسمی اسرائیل هستیم.
🔹
احضار کاردار اسرائیل به عنوان اعتراض به اقدامات غیرقابل قبول علیه شرکت‌کنندگان ناوگان آزادی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/akhbarefori/653241" target="_blank">📅 19:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653240">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
بقائی: وقتی پای مقابله با یک متجاوز به میان می‌آید، همه متحد می‌شویم
🔹
سخنگوی وزارت خارجه در گفتگو با روزنامه فوليا د سائوپائولو برزيل: مردم نسبت به قبل از جنگ امیدوارتر شده‌اند. انگیزه بیشتری برای ایستادگی، تاب‌آوری و مقاومت دارند و فکر می‌کنم این یکی از جنبه‌های مثبت جنگ بود، چون ایالات متحده و اسرائیل باعث شدند ایرانی‌ها متوجه شوند که در برابر تجاوز خارجی چقدر می‌توانند متحد و مصمم باشند.
🔹
ممکن است اختلاف‌نظرها و اختلافات زیادی داشته باشیم اما وقتی پای مقابله با یک متجاوز خارجی به میان می‌آید، همه متحد می‌شویم. احتمالاً مردم را در خیابان‌ها و میدان‌های مختلف دیده‌اید.
🔹
در حال حاضر ما با ناامنی‌ای روبه‌رو هستیم که به دلیل تجاوز ایالات متحده و اسرائیل علیه ایران به کل منطقه تحمیل شده است.
🔹
باید به یاد داشته باشیم که تنگه هرمز پیش از ۲۸ فوریه، زمانی که ایالات متحده و اسرائیل اقدام تجاوزکارانه خود را آغاز کردند، باز بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/akhbarefori/653240" target="_blank">📅 18:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653239">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
امنیت و ایمنی تنگه هرمز برای ایران از هر کشور دیگری مهم‌تر است
🔹
آنچه ما می‌خواهیم مطالبه نیست، بلکه حقوق ما است.
🔹
نیروهای مسلح ما در صورت هرگونه ماجراجویی از سوی آمریکا و اسرائیل، فوراً و با تمام قوا پاسخ خواهند داد.
🔹
هیچ تهدید قریب‌الوقوعی از سوی ایران علیه آمریکا وجود نداشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/akhbarefori/653239" target="_blank">📅 18:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653238">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رئیس اتحادیه بنکداران مواد غذایی: از عید نوروز تاکنون قیمت روغن خوراکی صنف و صنعت و خانوار در دو مصوبه دولت افزایش یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/akhbarefori/653238" target="_blank">📅 18:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653237">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
کشف و خنثی‌سازی بیش از ۸۵۰ مورد بمب، موشک و پرنده انتحاری در هرمزگان
🔹
روابط عمومی سپاه امام سجاد(ع) هرمزگان در اطلاعیه‌ای از کشف و خنثی‌سازی بیش از۸۵۰ مورد بمب، موشک و پرنده انتحاری در هرمزگان خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/akhbarefori/653237" target="_blank">📅 18:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653236">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای العربیه: کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است
🔹
فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند.
🔹
ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود.
🔹
دور جدیدی از مذاکرات بعد از فصل حج در اسلام‌آباد برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/akhbarefori/653236" target="_blank">📅 18:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653235">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
مقام ارشد صهیونیست: ایران و جبهه مقاومت، اسرائیل را در آستانه سقوط و فروپاشی قرار دادند!
🔹
ژنرال «اسحاق بریک»: ترامپ در موقعیتی قرار گرفت که اصلا تصورش را نمی‌کرد؛ او در واقع می‌خواست ایران را شکست دهد و توان نظامی‌اش را از بین ببرد اما ناگهان فهمید که دارد اقتصاد جهان را به سمت فروپاشی می‌بَرَد!
🔹
ما جهان را از دست دادیم، دچار آشوب داخلی شدیم و انسجام ملی ما هم فروپاشیده؛ اسرائیل در لبه پرتگاه و در آستانه فروپاشی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/akhbarefori/653235" target="_blank">📅 18:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653234">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc8ILrhwlgjctIa_s5RFYtFFHyLaYEiujrbqLWds9Zxp7p7XU-qBmt2xlp2VhirC4itO72_L5utmCvz-ck6Q7oNcfM4gW3dKOXGSdsY32fSeHsTRdcxaHhSBrIlZikFQBiHz907SR3xFdM9PqgXcXuEDH5coOWX4Tf-3AZqp4Blm2UDRatQe0c64b9JVwL6DioLtvL-_olPfESuOs40HxmayPoXVuI_-w7Q2RBxF3DkU5Zk_iVbeHwIxilrjvWR0OvCuO1KV4Nq-ro3va5gkJqMN9HuZnuDkMK8vGmT6_3YxxK1Wlf2mxxgGOEXShG5W2AX0m37VG2QY0B3NuMppqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارواح پلاستیکی در آسمان شب
🔹
زیر نور ماه، شهر نفس می‌کشد اما کیسه‌هایی که روزی حامل خرید بودند، حالا روح‌هایی سرگردان‌اند که بر طبیعت بی‌جان سایه افکنده‌اند. گوزن و لاک‌پشت، شاهدان خاموش این تراژدی مدرن‌اند.
🔹
آلودگی، ارواحی می‌سازد که هرگز آرام نمی‌گیرند.…</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/653234" target="_blank">📅 17:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653233">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
کارشناس مسائل منطقه: از نظر آمریکایی‌ها تنگه هرمز محل تلاقیِ منافع جمعی از متحدین آمریکا و رقبای آن‌ها است
🔹
طبق سند امینت ملی آمریکا از دست دادن حاکمیت تنگه هرمز به افول اسرائیل منجر می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/akhbarefori/653233" target="_blank">📅 17:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653232">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a20a0646.mp4?token=MkX6OrMxhdneoOA02YGM83yghwa8Ax02MstLsRznqhI5lvhRbxe4JAmvwhyej4s8JjTsgVHWs8WyDAS1YnS-gaQrcB6-hZipMXoFhk7GbDBlqo9nvKLC_IJoXxGmP-t1H7zuakd-MYg3HLLUvEXTDtEczS7coWwscf26mqnS2nxssLARHrqWFHZYLJEOI-pAXRkzLq0soMEKblHCHJ1ODYYLEOKiY2ox4uka37X7u3ofcumNDT1qwpsdFrseJpDnqmbFKebyhOiEs3o9AU3rTZNJezdsnvBQ7PflawHnpx5Hk2rCr9fmbFlDPF473ZcHRWLR4NIlZmTB_Dy7IGLo-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a20a0646.mp4?token=MkX6OrMxhdneoOA02YGM83yghwa8Ax02MstLsRznqhI5lvhRbxe4JAmvwhyej4s8JjTsgVHWs8WyDAS1YnS-gaQrcB6-hZipMXoFhk7GbDBlqo9nvKLC_IJoXxGmP-t1H7zuakd-MYg3HLLUvEXTDtEczS7coWwscf26mqnS2nxssLARHrqWFHZYLJEOI-pAXRkzLq0soMEKblHCHJ1ODYYLEOKiY2ox4uka37X7u3ofcumNDT1qwpsdFrseJpDnqmbFKebyhOiEs3o9AU3rTZNJezdsnvBQ7PflawHnpx5Hk2rCr9fmbFlDPF473ZcHRWLR4NIlZmTB_Dy7IGLo-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره ایران: عجله ندارم
🔹
رئیس‌جمهور آمریکا بعد از آنکه دست‌کم ۶ بار ضرب‌الاجل‌هایش درباره ایران را تغییر داده امروز چهارشنبه گفت که درباره ایران عجله ندارد.
🔹
او گفت: «عجله ندارم. همه می‌گویند می‌گویند انتخابات میان‌دوره‌ای؛ اما من عجله ندارم.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/653232" target="_blank">📅 17:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653231">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای ترامپ: در جنگ ونزوئلا و ایران تنها ۱۳ نظامی از دست دادیم
🔹
رئیس‌جمهور آمریکا مدعی شد: «ما در جنگ‌های ونزوئلا و ایران تنها ۱۳ سرباز از دست دادیم در حالی‌که در جنگ‌های قبلی صدها هزار کشته داده بودیم.»
🔹
ادعای ترامپ در حالی مطرح شده که پایگاه اینترسپت در گزارشی افشاگرانه چند وقت پیش گزارش داد که ایالات متحده آمریکا در اقدامی عامدانه آمار تلفات و خسارات جنگ را پنهان کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/akhbarefori/653231" target="_blank">📅 17:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653230">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
خیالبافی ترامپ درباره تصرف ونزوئلا و ایران
🔹
رئيس‌ٰجمهور آمریکا مدعی شد: «ما ونزوئلا را تصرف کردیم. می‌توانیم بگوییم ایران را هم تصرف کردیم.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/653230" target="_blank">📅 17:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653229">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMM_3HxzOCeaNJFcYuzHqgya3G8PZIsbtNe0FtnHw7BBzpGumC9NMNBfGRqpFTLO5U3CiZDQHkwDZ9Zz-oe3v7REa7V9T4QxsDb02maKIROwJWCant94UUJUr_ja4l9OdaRWn4Jp5fGP9LDdAhVyZe6Oa7PH7t5jQDs_IUOu_bnmqZxizOFK5BqjuKrpgf3RxnYkRlhqFkzQjFv_vw-HADtIR4-paFFUzVEl25awAfyOVEqifR6OMorPUAKRpNjF92qBDlu9HSLZdI4ro5fxvZ_QlBzTrk-RLTnyxKBT0EDuwJk1aMJlAUCp0IWRXBunXapBlpLbZh40A25saWlOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: نتانیاهو هر کاری من بخواهم انجام می‌دهد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا امروز چهارشنبه تلاش‌ کرد به انتقادهایی که او را بابت راه‌اندازی جنگ علیه ایران بنا به خواست اسرائیل مورد سرزنش قرار می‌دهند پاسخ دهد.
🔹
او گفت: «نتانیاهو کارهایی که من بخواهم را انجام خواهد داد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/653229" target="_blank">📅 17:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653228">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
قالیباف: در شرایط جنگ اقتصادی روش‌های عادی کافی نیستند و وزارتخانه‌های اقتصادی باید با روش‌های خلاقانه دنبال حل مشکلات باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/akhbarefori/653228" target="_blank">📅 17:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653227">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
قالیباف: مردم انتظار دارند همه مسئولان هم‌راستا با بعثت اعجازگونۀ مردم برای حل مشکلات معیشتی به صورت جهادی تلاش کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/653227" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653226">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سومین فایل صوتی دکتر قالیباف خطاب به مردم ایران
🔹
تحرکات آشکار و پنهان دشمن نشان می دهد که به دنبال دور جدید جنگ است
🔹
مردم اطمینان داشته باشند نیروهای نظامی ما از فرصت آتش‌بس به بهترین شکل برای بازسازی توان خود استفاده کردند
🔹
دشمن را از تعرض مجدد به ایران پشیمان خواهیم کرد
🔹
از جهش قیمت‌ها و بالا رفتن هزینه‌های زندگی مردم اطلاع دارم
🔹
همان‌طور که آقای رئیس‌جمهور گفتند ملت ایران هرگز دربرابر زورگویی سر خم نمی‌کند
🔹
یکی از خطاهای محاسباتی دشمن این بود که اگر زندگی مردم سخت‌تر شود، انسجام ملی تضعیف می‌شود
🔹
کمیته نظارتی ویژه مجلس برای بررسی مسائل معیشتی و تامین کالاهای اساسی تشکیل می‌شود
🔹
متاسفانه برخی با انگیزه‌های سیاسی و به بهانه گرانی‌ها بدون در نظر گرفتن واقعیت‌ها، انگشت اتهام را فقط به سوی دولت یا رئیس جمهور می‌گیرند
🔹
برخی انتقادها از دولت بگونه‌ای است که گویی جنگی اتفاق نیفتاده است
🔹
من منکر برخی ضعف‌های مدیریتی نیستم اما آدرس غلط دادن، به وحدت ملی لطمه می‌زند
🔹
تأمین پایدار کالاهای اساسی باید اولویت اول همه مسئولان باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/akhbarefori/653226" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653225">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
قالیباف: از جهش قیمت‌ها و بالا رفتن هزینه‌های زندگی مردم اطلاع دارم
🔹
دشمن تصور می‌کند اگر زندگی مردم سخت‌تر شود، انسجام ملی تضعیف می‌شود اما مردم ثابت کردند که هم‌چنان در میدان مبارزه با دشمن حضور دارند و انتظار دارند که مسئولان مشکلات را حل کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/akhbarefori/653225" target="_blank">📅 17:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653224">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
قالیباف: باید با تقویت آمادگی برای پاسخ موثر به حملات احتمالی و همچنین با افزایش تاب‌آوری اقتصادی، دشمن را از خطای محاسباتی بیرون بیاوریم و ناامیدش کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/akhbarefori/653224" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653223">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
قالیباف: دشمن را از تعرض مجدد به ایران پشیمان خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/akhbarefori/653223" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653222">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
قالیباف: مردم اطمینان داشته باشند نیروهای نظامی ما از فرصت آتش‌بس به بهترین شکل برای بازسازی توان خود استفاده کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/akhbarefori/653222" target="_blank">📅 16:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653221">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
قالیباف: تحرکات آشکار و پنهان دشمن نشان می دهد که به‌دنبال دور جدید جنگ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/akhbarefori/653221" target="_blank">📅 16:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653220">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf79aa6c71.mp4?token=jdUqhEblXMNteGe4n7Vms0sKpyVq5oZPOMv6-8ZPRNxnNYPSk138M0QgXs-8lRAKgOE1OpMeHtCrHRVhlZv2iOZ550UdGiaXF9tOYHQJeDLj-onYpfd1R4ky1T1DeY42GRc4ULUhJOUXB67oTdChQv3VGLwzcX4g9uPLQLif5Aol5S54eUuc2U1dvdntP0VnE3RGQd-Wv3JQVvPYQYmUbiw7pokhj_diega4GLJXo7HHtSyZnIiZkazqKcc99yCSd4NlhEv6eJi_xFn0MYo2nyOIgzEH-ARg_3jdH-IWdmEPg6XNZh47n9SEPR0rp4xXdby1yhjxi78fE8fKIImEDbeWhfnZ1MBwkSm1crWZAnZM1HSeXYpj_cm29IQKE-e4OxVrgttwEx0VzjDlb-ltJRcxuhywXm2XKcCuHf-0vn_eXbv2Waub24uxdXuU-nyAOzSTe20w6X1XuB_4mbPYj4P5T7AFQIYfgHvk4pSQu5ZXa1cqdmevGXXIWSodH_GLEw0n1ofzBAAepVFeiWl_C-IVnIriMYnvaIAJ-VGb1aowLaVNpHxAudYPtPIQ7Cnvwhol4gis1Ae5J4IfPwa4QBCVfWIU3kGNBfUzwaqsFC7WTITGQRVBCT1v_1UFwfTe8xzay6RBursnllmb2oShEveamJttGs4xO7oUsjFxTWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf79aa6c71.mp4?token=jdUqhEblXMNteGe4n7Vms0sKpyVq5oZPOMv6-8ZPRNxnNYPSk138M0QgXs-8lRAKgOE1OpMeHtCrHRVhlZv2iOZ550UdGiaXF9tOYHQJeDLj-onYpfd1R4ky1T1DeY42GRc4ULUhJOUXB67oTdChQv3VGLwzcX4g9uPLQLif5Aol5S54eUuc2U1dvdntP0VnE3RGQd-Wv3JQVvPYQYmUbiw7pokhj_diega4GLJXo7HHtSyZnIiZkazqKcc99yCSd4NlhEv6eJi_xFn0MYo2nyOIgzEH-ARg_3jdH-IWdmEPg6XNZh47n9SEPR0rp4xXdby1yhjxi78fE8fKIImEDbeWhfnZ1MBwkSm1crWZAnZM1HSeXYpj_cm29IQKE-e4OxVrgttwEx0VzjDlb-ltJRcxuhywXm2XKcCuHf-0vn_eXbv2Waub24uxdXuU-nyAOzSTe20w6X1XuB_4mbPYj4P5T7AFQIYfgHvk4pSQu5ZXa1cqdmevGXXIWSodH_GLEw0n1ofzBAAepVFeiWl_C-IVnIriMYnvaIAJ-VGb1aowLaVNpHxAudYPtPIQ7Cnvwhol4gis1Ae5J4IfPwa4QBCVfWIU3kGNBfUzwaqsFC7WTITGQRVBCT1v_1UFwfTe8xzay6RBursnllmb2oShEveamJttGs4xO7oUsjFxTWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: هرجا لازم باشد می‌جنگیم و هرجا لازم باشد مذاکره می‌کنیم؛ ما کاملا در خدمت منافع نظام هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/akhbarefori/653220" target="_blank">📅 16:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653219">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ij2geZrIuRSv96fuGdFfugKIECv71nICG0lYRN_QWW2P85NMSJMdOJUstmkZJVUvSoVKXNZGMpsAubbYd27hzMFnq-737_E_1IOIFJr0Nr78mU7Ld3TRjH2fH-OQJpQyKTxgsDsxY5w9dvWoAoIH9nDq9mGADoB5l7OihooyWTIZtDPVwb3_-46Yq7balkpFzwp7KdjjHPEjO3TXdYGvw70crBa9WKoxo7Kg22EJkxJXi_LJb3jFX4RAieR9CMj17CqCmddttULe9xiWBxNI8uICJrXQUHRSJL-XxVEm4ZPRtLcEcBfQ6znj_Yf0Enk-IWscyy-ecVka0Zsdvzgh6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکا دوباره در جنگی بی‌پایان که در آن امکان پیروزی ندارد گیر خواهد افتاد
🔹
رئیس مجلس در حساب کاربری خود در شبکهٔ ایکس، عبارتی از فصل ۱۱ کتاب خاطرات ونس، معاون اول رئیس جمهوری آمریکا نقل کرد:
🔹
«ما احساس می‌کردیم در دو جنگ بی‌پایان و بدون امکان برد گیر افتاده‌ایم و سهم نامتناسبی از سربازان از محله خودمان (محله فقرا) آمده بود.»
🔹
و در ادامه نوشت:
🔹
این وضعیت (گیر افتادن آمریکا در جنگی که نمی‌توانند ببرند) دوباره در حال تکرار شدن است. این بار فقرا و فراموش‌شدگان آمریکایی باید هزینهٔ جنگ‌افروزی الیگارش‌های نزدیک به کاخ سفید، افراد شیطان‌صفتی همچون جیمی دیمون و لابی تاجران جنگ در واشینگتن را بپردازند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/akhbarefori/653219" target="_blank">📅 16:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653218">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffbb74799.mp4?token=fp3aDzpcIa0ipxCjih-3-QJuRXHWOpfFIsEhIwWPSvEa-vKFd-uqJu9hXlO4Fbu6DOg-HVXADg-Q4GlviLK5fsIqFfwgN6Gqd8cKjFeNyqwI1FM9_WcIL076RYqzxue_EtgeH7hnm_PdSt6_-MGXjs43qhrCVChDGblwErfL86-e7eJkkax8y8txQ8ESs2HU1LFvyhvSHzakX9nfysjAeDKD3DvhJXvBDWDxsQpSYItV_xf-d8nkrBL4dNe47ObU7ogPGjR9CnAC3j54IBb19qeE5pKTAoYlAa6fk3hGMn5vCJLk-86sBMMTeZ6PWV8JEy4SuGqkh754NZ1v2sK_1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffbb74799.mp4?token=fp3aDzpcIa0ipxCjih-3-QJuRXHWOpfFIsEhIwWPSvEa-vKFd-uqJu9hXlO4Fbu6DOg-HVXADg-Q4GlviLK5fsIqFfwgN6Gqd8cKjFeNyqwI1FM9_WcIL076RYqzxue_EtgeH7hnm_PdSt6_-MGXjs43qhrCVChDGblwErfL86-e7eJkkax8y8txQ8ESs2HU1LFvyhvSHzakX9nfysjAeDKD3DvhJXvBDWDxsQpSYItV_xf-d8nkrBL4dNe47ObU7ogPGjR9CnAC3j54IBb19qeE5pKTAoYlAa6fk3hGMn5vCJLk-86sBMMTeZ6PWV8JEy4SuGqkh754NZ1v2sK_1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ضلع چهارم خیابان و مردم به ارکان دیپلماسی و میدان افزوده شد
🔹
وزیر امور خارجه: پیش از این، ارکان اثرگذاری در تحولات شامل سه ضلع «میدان، دیپلماسی و رسانه» بود؛ اما در نبردهای اخیر، ضلع چهارمی تحت عنوان «خیابان و حضور مردمی» به این مجموعه افزوده شد که برانگیختگی حاصل از آن، ارکان قبلی را تکمیل کرد.
🔹
نیروهای مسلح در جبهه دفاع، نهادهای دولتی در بخش معیشت، دستگاه‌های امنیتی به عنوان چشم نظام، و دستگاه دیپلماسی نیز مأموریت دارد تا صدای رسای کشور در خارج و مدافع منافع ملی در عرصه‌های بین‌المللی باشد.
🔹
دستگاه دیپلماسی با همان قوتی که نیروهای مسلح در میدان دفاع حاضر می‌شوند، در میدان گفتگو و مذاکره برای تأمین منافع کشور عمل خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/akhbarefori/653218" target="_blank">📅 16:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653217">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f944b32f.mp4?token=VSe43xL2imxU2PJaXiJmB5IgmSzFuDRA6MSfpXK_EtPH07VBT-wXmb_XRIvvYBHD8GLXGKVTvQqihTDW9d1Nyij2n8_TDVyJGKDaFB6M09zV9ys0GYG6Lqhjc_Ol8g4ylFcw9_trsXM2vd_UHGY4WHV4IvS2mZ4J-t175Lmp4KIXPrZPLIfpM7OeithS7tnztgYDzLXLlY--Fu1jEQfCOH0BENthfi295mDKqm8-tsiaoqSZF0uryxm1k4-N_Ql2hATIR0tpfZ_WYHl4bCMPpSQxlA9_ysSU2hZ1Kobs1W2RRDgomY_kimGs8aZpmzTR4UZWi91lWTA6II6Rufm1wUwqj30oU0J1MH_EVhvWylkw4xJJJUoiSwkKroF9JtgAsT11hkYLzHN2TtJ8jYFGfWAMVJG66zat32nbX6tHREDB5CFSubpgxNKyI6z0C2y7HbZmi1WaMT6C5uVvLrWncT371YTJa-l_HFSOmpWsOFvedzSpP1p1ipC5tSBX3W5aGtZ3xlF6udL_F5pzxU-OBSH6mDOSahyYlFcwLrDwN_23Qu-62Nla2rkODWOfCBhx-m3OsLL0UcXjRyonqVkWrD66cEheot19hoqo1wp5YnfxNTVUVRiUBvaPWWfumdsA-EvIJP6G9V0HC3yUx9X58rdYUPRgSqEy3cbwZQylFgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f944b32f.mp4?token=VSe43xL2imxU2PJaXiJmB5IgmSzFuDRA6MSfpXK_EtPH07VBT-wXmb_XRIvvYBHD8GLXGKVTvQqihTDW9d1Nyij2n8_TDVyJGKDaFB6M09zV9ys0GYG6Lqhjc_Ol8g4ylFcw9_trsXM2vd_UHGY4WHV4IvS2mZ4J-t175Lmp4KIXPrZPLIfpM7OeithS7tnztgYDzLXLlY--Fu1jEQfCOH0BENthfi295mDKqm8-tsiaoqSZF0uryxm1k4-N_Ql2hATIR0tpfZ_WYHl4bCMPpSQxlA9_ysSU2hZ1Kobs1W2RRDgomY_kimGs8aZpmzTR4UZWi91lWTA6II6Rufm1wUwqj30oU0J1MH_EVhvWylkw4xJJJUoiSwkKroF9JtgAsT11hkYLzHN2TtJ8jYFGfWAMVJG66zat32nbX6tHREDB5CFSubpgxNKyI6z0C2y7HbZmi1WaMT6C5uVvLrWncT371YTJa-l_HFSOmpWsOFvedzSpP1p1ipC5tSBX3W5aGtZ3xlF6udL_F5pzxU-OBSH6mDOSahyYlFcwLrDwN_23Qu-62Nla2rkODWOfCBhx-m3OsLL0UcXjRyonqVkWrD66cEheot19hoqo1wp5YnfxNTVUVRiUBvaPWWfumdsA-EvIJP6G9V0HC3yUx9X58rdYUPRgSqEy3cbwZQylFgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ظریف در مراسم بزرگداشت وزرای خارجه شهید: ما نیاز به تضمین از سوی قول شکنان نداریم. مردم‌ و نیروهای مسلح‌ بزرگترین تضمین برای ما هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/akhbarefori/653217" target="_blank">📅 16:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653216">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
رسانه‌های عبری گزارش دادند، در عملیات زیرگیری با خودرو در ئزدیکی منطقه عیون الحرامیه در شمال رام الله، دست کم یک شهرک نشین صهیونیست زخمی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/akhbarefori/653216" target="_blank">📅 16:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653215">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW8-xeX_vZbiPuCHr4Nrad-BOPboNgmyxYA-vZsQTzt7fSlQ_7jToMHbHI7gzNga1Ye-C0SaoQB21jTAqMWnIFlhZyzcq4TbrQfmQZC9XzTgYvJEQZPTcX7GDmg1N4vQhhTA3w0BHMI5BU68ngl5ZZ77oNd0-ydDQRr96XHEk3xxCX8DdhMqAFUW2M2D-ItawEpzH81xSs4PMnISCG-HqV_5ejxsSqN0a2-FwtnbZhdcGnKP3qrGBm4gBS4q9q7Hq0bz4734YqsJMVVAhy5RF3vOts4GZ9nQ4iGztkINKrMI5P8CRZOxaFKl-OTC8oA-q-H39Kewqseh0cobIOnhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افت ۱۲ درصدی رضایت جمهوری‌خواهان از ترامپ
🔹
نظرسنجی رویترز/ایپسوس نشان می‌دهد ۲۱٪ از جمهوری‌خواهان از عملکرد ترامپ ناراضی‌اند؛ در حالی که این رقم در ابتدای ریاست‌جمهوری‌اش در ژانویه ۲۰۲۵ تنها ۵٪ بود.
🔹
همچنین میزان ارزیابی مثبت از عملکرد ترامپ به ۷۹٪ رسیده که نسبت به ۸۲٪ اوایل این ماه و ۹۱٪ ابتدای دوره او کاهش داشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/akhbarefori/653215" target="_blank">📅 16:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653214">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
عراقچی: وزارت خارجه با فرماندهان نظامی هماهنگ است
🔹
دیپلمات‌های کشور در صورت تغییر نقش، با همان صلابت پشت لانچرهای دفاعی قرار می‌گیرند و نیروهای نظامی نیز در صورت اقتضا، با همان اقتدار پشت میز مذاکره خواهند نشست؛ چراکه تمامی نهادها هدفی مشترک را در یک مسیر واحد دنبال می‌کنند.
🔹
نیروهای مسلح همواره قهرمانان ما هستند. در مسیر تحقق آرمان‌های کشور برخی جان خود را فدا می‌کنند و برخی دیگر از نام و آبروی خویش می‌گذرند.
🔹
ارتباط و هماهنگی مستمر و روزانه میان وزارت خارجه و فرماندهان نیروهای مسلح در سطوح مختلف جریان دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/653214" target="_blank">📅 16:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653212">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۸۵ درصد از غذای کشور در داخل تامین می شود
مجید آنجفی، معاون امور زراعت وزارت جهاد کشاورزی در
#گفتگو
با خبرفوری:
🔹
بخش عمده ای از کود اوره مورد نیاز دنیا در کشورهای حاشیه خلیج فارس تولید می شود و می تواند چالشی برای امنیت غذایی دنیا باشد.
🔹
فکر می کنم بالغ بر ۸ میلیون تن  کود اوره در ایران تامین می شده است و از این مقدار حدود ۲ و نیم تا ۳ میلیون تن مصرف داخلی، و مابقی صادراتی بوده است.
🔹
ما متکی به تولید داخلی هستیم و اوره به اندازه کافی تامین می شود و کشور چالشی را نخواهد داشت.
🔹
حدود ۸۵ درصد از غذای کشور در داخل تامین می شود و بنابراین ضریب امنیت غذایی کشور ما ۸۵ درصد است و باقی مانده هم از مبادی ای تامین می شود که برای تامین آن مشکلی نخواهیم داشت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/akhbarefori/653212" target="_blank">📅 16:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653211">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD9NJFO3OYC9t8uZZ5w_AscvSEVn7zAUCC3bo-iq9isEkvaRScMLXa71EKYZkNglPdWy4hgsTr2HPUOzkxlvMv7KIVaXAClGC-XMEREHuzFPYwfkrcyEuEBr25JibHGGp2XnzgQBNLrAks9MmiyMUy9doybJ4YeIGDH1jp-VpkssmQ_siNxBuKOTLMxmXfxsxuEk6c6CHdMxXCzSR40TIqahWnH3NZj1Zboj4aRhqm12Q2sqOrTvk7rYrcCixAFzqZtuot8qr0fioMrw4EUUNzoM5dpYatGEhnHihKpm9sktlq0Z7DsjTy6-gs1IfK_J2EeK2v6FPxG4miGwFZqbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استعفای مقام ارشد اطلاعاتی دولت ترامپ به‌دلیل مخالفت با جنگ ایران
🔹
عروس رابرت اف. کندی جونیور، وزیر بهداشت و خدمات انسانی آمریکا، از سمت‌های خود در دولت ترامپ کناره‌گیری می‌کند.
🔹
گزارش داد «آماریلیس فاکس کندی، یکی از مقامات ارشد اطلاعاتی دولت ترامپ و متحد تولسی گابارد، مدیر اطلاعات ملی، این هفته از دو سمت کلیدی دولتی کناره‌گیری می‌کند».
🔹
طبق گزارش، خروج آماریلیس فاکس کندی هم انگیزه مشابهی دارد و به گفته یک منبع، «دستکم تا حدی به دلیل مخالفت او با اقدام نظامی ترامپ در ایران بوده است».
🔹
در این گزارش آمده که در ایمیلی به تاریخ هشتم این ماه (مه) که به رویت رسید، کندی به همکارانش گفته که قصد دارد به بخش خصوصی بازگردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/akhbarefori/653211" target="_blank">📅 16:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653210">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcGzPTK4TTi1xmKwSyRNhEPV5Osi7iNM7h8se7G_dGjZ4qGiYQJ3aKW3v-tvQ40PfNnajccC11llLW3PkiPRqWqrNfpJUrP3pH6QDJRIO2rTwvEl6KAOo8P62c7TG96IckuoX8el2Xr4rvqQm4Lisnr5tzAduo4ZH4j4bvcgM3GnrQb7A8MfH4MsCz4KRMm9lF5Y8TNYjl70ulZLMIIGQxZdsVwOgsYlgcnP67lgA2ntYbnyPDgNPacfAkmpsy3Ch_ofZ6Q5_2HgJCtEFEA7tT3UOlxm-TAB6h14LJJT9YLjvuA6kSZXEvvKkgEqXP80diPepp3ezrlN-dtLLBT03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه غربی: مواضع ایران تا حد زیادی، بدون تغییر مانده است
🔹
وال‌استریت ژورنال در پی ارسال آخرین پیشنهاد اصلاح‌شدهٔ ایران به طرف آمریکایی در روز یکشنبه، تأکید کرده است که تهران همچنان بر بسیاری از مواضع پیشین خود پافشاری می‌کند.
🔹
به گفته این روزنامه، ایران همچنان خواستار پایان درگیری‌ها، لغو تحریم‌ها، دریافت غرامت برای خسارات جنگی و نقش نظارتی بر تنگهٔ هرمز است.
🔹
این روزنامه همچنین افزوده که ایران در برابر خواسته‌های آمریکا برای تعطیلی یا تعلیق طولانی‌مدت برنامهٔ هسته‌ای خود مقاومت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/653210" target="_blank">📅 15:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653209">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1236795a.mp4?token=i4RHSBmmCdDJpGqqL5_CEW0RyB3PUATrj5T_FA5nRL7bO9EXPNaDrPXQHqXmQKOMnpfqG6R4YZeFKqA3Iamkz2hJXQQ_wHSe3mNDptmh9wM1ijxxiy16Qp3l_nZ2wuD49Nk1fvwUrLoLl0OGcvXAi5vcki4IWkp4VEdD7A-hXqmkzQ-pBoKlqno7NyuO4l49fR2rneSBPZip9NBGLGBK_05xuv9hIvX77zmIJm1CwZBO-SV5uHvDb2Qznco5PURFcb1A5DVNkxnEbg7p2CBUZ7X8VMHvmZGl1xQlZK54uXYBs8v5VbyFwpqEntFxIee31mUetORMH0f0t2LhiumXHk5-mqGCA1xAhi3qYJgoTa648Fkns9Ixwt_W_evgzoTiof2YRFvvEJ4EVCiLbOuTJ3ONPYwc5o7CFwAWzLBKar-YbDT8pfGKbxTrEiO9JambM6zyY5ju4W02X1VZlaaGjUE6Jz8rEP_On5N4OmkHpHg_qKNzcacOmKDN8_fFJMdAy-v57_SfajSHVixZD5GJC2EMQSuj8p2H5SmvmbUawK34CrKVkc6l7vH2dvJZxgm4wTzlP02feAGO0IGXChrfd3mplDmwR5rT42UTWKJ2BMJJfUvmxO2oNpE-YJVfZCUTHsNvqGQWK9ITqVtk2CIJSJbaeb77r6FSs4cLwmK3YfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1236795a.mp4?token=i4RHSBmmCdDJpGqqL5_CEW0RyB3PUATrj5T_FA5nRL7bO9EXPNaDrPXQHqXmQKOMnpfqG6R4YZeFKqA3Iamkz2hJXQQ_wHSe3mNDptmh9wM1ijxxiy16Qp3l_nZ2wuD49Nk1fvwUrLoLl0OGcvXAi5vcki4IWkp4VEdD7A-hXqmkzQ-pBoKlqno7NyuO4l49fR2rneSBPZip9NBGLGBK_05xuv9hIvX77zmIJm1CwZBO-SV5uHvDb2Qznco5PURFcb1A5DVNkxnEbg7p2CBUZ7X8VMHvmZGl1xQlZK54uXYBs8v5VbyFwpqEntFxIee31mUetORMH0f0t2LhiumXHk5-mqGCA1xAhi3qYJgoTa648Fkns9Ixwt_W_evgzoTiof2YRFvvEJ4EVCiLbOuTJ3ONPYwc5o7CFwAWzLBKar-YbDT8pfGKbxTrEiO9JambM6zyY5ju4W02X1VZlaaGjUE6Jz8rEP_On5N4OmkHpHg_qKNzcacOmKDN8_fFJMdAy-v57_SfajSHVixZD5GJC2EMQSuj8p2H5SmvmbUawK34CrKVkc6l7vH2dvJZxgm4wTzlP02feAGO0IGXChrfd3mplDmwR5rT42UTWKJ2BMJJfUvmxO2oNpE-YJVfZCUTHsNvqGQWK9ITqVtk2CIJSJbaeb77r6FSs4cLwmK3YfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تامین کالاهای اساسی و صرفه‌جویی دو موضوع مهم نشست استانداران سراسر کشور با حضور رئیس جمهور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/653209" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ضرب الاجل ۱۰ روزه دستگاه قضائی به شرکت های بیمه
🔹
رئیس کل دادگستری آذربایجان غربی: طی دستوری به شرکت های بیمه ضرب الاجلی ۱۰ روزه برای پرداخت مطالبات آزمایشگاهها، کلینیک های درمانی و مجموعه های مرتبط با بهداشت، درمان و سلامت تعیین شده است.
🔹
بهداشت و سلامت مردم جزء مهمترین شقوق حقوق عامه است که به جهت عدم همکاری موثر و پرداخت مطالبات مجموعه های درمانی با اخلال مواجه شده است.
🔹
به بیمه تاکید شده است، نسبت به پرداخت بدهی های معوق خود در سریعترین زمان ممکن اقدام کنند.
🔹
بیمه ها ابتدا به صورت نقدی حق بیمه را دریافت کرده اند ولی در پرداخت مطالبات مجموعه های بهداشتی، درمانی حدود یکسال تاخیر نموده اند و این امر به هیچ وجه پذیرفته نیست چرا که موجب اختلال در روند درمان مردم شده است.
🔹
در صورت عدم پرداخت طی ۱۰ روز، اقدامات قاطع و فوری قضایی از جمله برداشت از حساب و تعقیب مدیران خاطی از جهت ترک فعل در دستور کار خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/653208" target="_blank">📅 15:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c381e0e43.mp4?token=e-CZM7_s8HXpzg7dGLvL1RSevt2MLk7rqveKo_eMOOro5EkKWBahGyhXnc5dfz5K6fsBkBC79FgYKVti9veSNL6nEqwTsZjzQbHfz6JzBnWBSBcxbRvhJ_AK1lEg-4F2SgEgZfWBkHXQ0DMQsG9L_72EWxJAKQAAKfXundaZ0pT7gV4lDIp5t0DZzq13W3HRQiecyuYLEOEkp27pXFA7Zoni0bJrzkly80aFINtGNklV5dDd648UTDOXHN658T7U-4OcN9fpcP72bbVGdAmDxz8UyIwmdmW-SMZtDByD16qADMzsy37JeADhlZh0L1XebwJghq0PvH0EyQaK_YSKWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c381e0e43.mp4?token=e-CZM7_s8HXpzg7dGLvL1RSevt2MLk7rqveKo_eMOOro5EkKWBahGyhXnc5dfz5K6fsBkBC79FgYKVti9veSNL6nEqwTsZjzQbHfz6JzBnWBSBcxbRvhJ_AK1lEg-4F2SgEgZfWBkHXQ0DMQsG9L_72EWxJAKQAAKfXundaZ0pT7gV4lDIp5t0DZzq13W3HRQiecyuYLEOEkp27pXFA7Zoni0bJrzkly80aFINtGNklV5dDd648UTDOXHN658T7U-4OcN9fpcP72bbVGdAmDxz8UyIwmdmW-SMZtDByD16qADMzsy37JeADhlZh0L1XebwJghq0PvH0EyQaK_YSKWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستیار ویژۀ وزیر کشور: اگر مجدداً جنگی شروع شود، در کوتاه‌ترین زمان ممکن محاصرۀ دریایی شکسته خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/akhbarefori/653207" target="_blank">📅 15:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0722b179b7.mp4?token=iXZYBEGa_9f2gb9jhQjbPQ6jj2yIVwHsGI-yWaJS93t8xd9YMi3F3xgHaOU3JNOPngBbatmxvOsgRlNFPUrb4zkueY10AFzXnIqa5waCgFfPnHaZAmWgFDrfwHwdSMKIRPWSIsm3pJkjREaLAT-4hi2PfXFm386yZCg1EgEiKyILAwxQq6tGjWQfyF67x07TTsx2KQLCYBeVX6Ay3ts9LGPOt6ksdYaYOk7w8Irp9c09yBrYlqif_5doscAq--u3avSxTHGlOqP6XOsn4afM7W3oC5T68XsQkQ_yqQk62jjM5odMy9HvSfbXHJIWfyCjYn2GBEUXylznC7A8evcAaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0722b179b7.mp4?token=iXZYBEGa_9f2gb9jhQjbPQ6jj2yIVwHsGI-yWaJS93t8xd9YMi3F3xgHaOU3JNOPngBbatmxvOsgRlNFPUrb4zkueY10AFzXnIqa5waCgFfPnHaZAmWgFDrfwHwdSMKIRPWSIsm3pJkjREaLAT-4hi2PfXFm386yZCg1EgEiKyILAwxQq6tGjWQfyF67x07TTsx2KQLCYBeVX6Ay3ts9LGPOt6ksdYaYOk7w8Irp9c09yBrYlqif_5doscAq--u3avSxTHGlOqP6XOsn4afM7W3oC5T68XsQkQ_yqQk62jjM5odMy9HvSfbXHJIWfyCjYn2GBEUXylznC7A8evcAaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرب‌الاجل‌های اجرا نشده ترامپ درباره ایران
🔹
روز دوشنبه، یک روز پس از تهدید به از سرگیری بمباران اهداف ایرانی، ترامپ دوباره گفت که چندین متحد خاورمیانه‌ای معتقدند آمریکا «به توافق با ایران بسیار نزدیک شده است». من این کار را برای مدتی به تعویق انداخته‌ام.
🔹
این ویدئو تهدیدها و مهلت‌هایی که ترامپ برای ایرانی‌ها تعیین کرده را نشان می‌دهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/akhbarefori/653206" target="_blank">📅 15:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653204">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30fd02dbcf.mp4?token=TFbM7wT-PN6m24XQAilBHHqpW8RLs0Mdkg3hXFxIwkL7u0VidPu6EbV9ZBN8ppawL4ZVS8Pwu6cV3jiXjaU1ZqJqVFIqb5p2SV9SD5eULKOS9QRUck-9CK7JnqsRPk6hkKVCegxqX0fZJ_-UOSrDFPCRrsqMDcV3t61llWdgW_31OlfA5QYkugBgdkBtQxGs3g4KSKxgeL3FLCuVDJsvAws8B7ZLmYJWQ1g5PA7bOeBwc-RvGawP1XdKDQfBYB-GAzkgoCVKPbfJ04Buw1jP3UhSen4ace639VhJ1c__Mp2jVstXhY3taEOuZEWIkhEr-RBYwHGcAa3yB9CNdC5gjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30fd02dbcf.mp4?token=TFbM7wT-PN6m24XQAilBHHqpW8RLs0Mdkg3hXFxIwkL7u0VidPu6EbV9ZBN8ppawL4ZVS8Pwu6cV3jiXjaU1ZqJqVFIqb5p2SV9SD5eULKOS9QRUck-9CK7JnqsRPk6hkKVCegxqX0fZJ_-UOSrDFPCRrsqMDcV3t61llWdgW_31OlfA5QYkugBgdkBtQxGs3g4KSKxgeL3FLCuVDJsvAws8B7ZLmYJWQ1g5PA7bOeBwc-RvGawP1XdKDQfBYB-GAzkgoCVKPbfJ04Buw1jP3UhSen4ace639VhJ1c__Mp2jVstXhY3taEOuZEWIkhEr-RBYwHGcAa3yB9CNdC5gjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویر شرم‌آور از آزار و اذیت اعضای کاروان صمود به‌دست بن‌گویر و نظامیان اشغالگر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/653204" target="_blank">📅 15:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653203">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNmaOvBtROdXB-Y5t44-Cp3KCGNEuKWfLd4H3UPwUGl1g-aRzjGzAYQ25fnXiyAtuyaEhnEIpQp5uhsJiJ2TjWJlgkqKtw_zxGb17wiUbYmPib_fmz4kTJSy2oU72XCqyRerzSCcTiY5k7gs7zQNl_V7Tm6uG6wnLWGswIDN9Rp67kTNO-7kfgIhZl5Kppv2zpiDyzs0kwBle9ivJi8Zzmzgkb4XX-u-zO0W8etWOnhmDjuhu-_QF4-3x8FPp2JQsRmk4GLi-Bbr5X2emWV2czAI4bhL2UMUjkK8NxrGVzpYAhFDnoEEOaF5BnEVCToG8zbuDBiu7psIroCjWOiKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: ایران خط
قرمز خود را جا‌به‌جا کرده است
نیویورک‌تایمز:
🔹
بزرگ‌ترین غافلگیری دکترین جدید ایران، خروج از انحصار تنگه هرمز و تسری دادن بحران به دریای سرخ و «تنگه باب‌المندب» است.
🔹
بستن هم‌زمان یا مختل کردن ناوبری در این دو شریان حیاتی انرژی و تجارت جهان، عملاً مسیرهای جایگزین امدادرسانی غرب را مسدود کرده و تیر خلاصی به زنجیره تأمین بین‌المللی شلیک می‌کند.
ایران خط قرمز خود را جابه‌جا کرده است.
🔹
هر کشوری که آسمان، خاک یا پایگاه‌های خود را در اختیار جنگنده‌ها و موشک‌های آمریکایی و اسرائیلی قرار دهد، به عنوان «طرف جنگ» تلقی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/akhbarefori/653203" target="_blank">📅 15:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653202">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33243e624.mp4?token=qLjagTMafMu61I5zAQIsjjy36_ItTRPBmmuDHmI1TiMEi2GXiet2oY5C3U1yxv7qj6eIQXgdRMft22QLZozFRyrieOmgCZB9dpj0pRtGOGhz91wu5YOjAe6kX24mX4Zp1376gxLWFXauCO2lzJcrb3pvGpcHIjbOfofJynE-kUZGJ3meDeknrEf-x-VvmK0nHaEAZrSVODli07ZzcUPWivCvPWa30Bx0diF6O210Ne534iYgvkWqQwKT9Xx1vWe1pR4eH1jNfrwQYO8t_FBJLlG7EQ3711FbsfTyMkmxsg8Tni3unaP89wH2K4RWJBVvlfePn8Y_gsu1-un3XcU72w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33243e624.mp4?token=qLjagTMafMu61I5zAQIsjjy36_ItTRPBmmuDHmI1TiMEi2GXiet2oY5C3U1yxv7qj6eIQXgdRMft22QLZozFRyrieOmgCZB9dpj0pRtGOGhz91wu5YOjAe6kX24mX4Zp1376gxLWFXauCO2lzJcrb3pvGpcHIjbOfofJynE-kUZGJ3meDeknrEf-x-VvmK0nHaEAZrSVODli07ZzcUPWivCvPWa30Bx0diF6O210Ne534iYgvkWqQwKT9Xx1vWe1pR4eH1jNfrwQYO8t_FBJLlG7EQ3711FbsfTyMkmxsg8Tni3unaP89wH2K4RWJBVvlfePn8Y_gsu1-un3XcU72w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنبیه نفتکش‌های متخلف در تنگه هرمز
🔹
نفتکش‌های متخلف و پنهان‌کار در دروازه تنگه هرمز شناسایی و تنبیه شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/akhbarefori/653202" target="_blank">📅 15:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653201">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شما اسم فرزند آینده‌تون که قراره به ایران جان تازه بده چی می‌ذارید؟
خیلی‌ها توی پویش «جان ایران» شرکت کردند از جوان‌هایی که ذوق فرزند دار شدن دارن تا پدر و مادرهایی که اسم بچه آینده شون رو انتخاب کردن.
شما هم می‌تونید نام فرزند عزیزتون که قراره به ایران جان بده رو به شماره ۳۰۰۰۱۴۱۳ پیامک کنید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/akhbarefori/653201" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653200">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0_bfM5Zo61EHNle_zDqY2XcXOm_HoL4F3zNj_TILBCYZbxwT9m7HCLItRvCVmRt8Y3hLe8kLg8AhWHng5iVPVzpgleRsIG9eV3sJcSlhIhwi5ZM9xHpgMnB32AcfL1aQQi8Qu00llJqMRYKMaQpGE8KM-cTeM8FA9NB6Anz3-VCTs1OBu2HCM5oGAT529VuSwTdoRBlTwY18tdVNUu--RYKzFRiOUOVIpE2SoJhlE-Gpq3U9Hni4GcZyO9mAQQ70glM5GGZIrMNNOYZTZ5UeQyrISiqzPvVJdsjtMwWlKKCKdBPbxbrIOo4Xfyow5fKoa0JgP3mrBrKt5RVmKdCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت بنزین سوپر ایرانی به جایگاه‌ها
🔹
دولت به پالایشگاه‌های کشور دستور داد، تولید بنزین باکیفیت موسوم به بنزین سوپر را از سر بگیرند.
🔹
از سال ۹۸ کمبود تولید بنزین نسبت به مصرف سبب شده بود تا تولید بنزین سوپر متوقف شود.
🔹
بنزین سوپر نوعی بنزین با عدد اکتان بالاتر نسبت به بنزین معمولی است که برای کاهش پدیدهٔ ناک (احتراق زودرس) و بهبود عملکرد موتورهای با نسبت تراکم بالاتر استفاده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/akhbarefori/653200" target="_blank">📅 15:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653199">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iohyg6IBVPJlp0G3AKAMzDhlxjgvJ7BGL5hpjedOWKfEDCTOpPmT3gavbEPEyAz9VdJB6drCwjnubw9gYZID7WXiW8-G_9f3AF6kmtFAP9bZXG2Ds-XatPaldoNS98tlDy4FZD1EbrZB2M48QtKAqa6LArxhHi-iJoB_tl42TLr9NqhL04kDYccNEUFgpgSM3T9efOnoOzt3zcC_77cMr1AIZDKRlcP1cHwzkEeli_i4a_aisJNyyie3B5gEygJ89zSzoH0uxnB8w57HiUEUTUON6KPcYZOnI3ybXEI3TqETwPayuiDmUPB4ZeBlT19iMf9oHhxe79MGpiLC-pQfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران؛ پایتخت پول ایران
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/akhbarefori/653199" target="_blank">📅 15:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653198">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDIfxgrzI_csQfMOxPmPLmc2f3D_OUJIbOyUfyrICSg8TFzj0Hf6SEMjJ2VPIeCnFNeuZXtXOk_c39822l0gNiofc84PaTMXba2kq_b8iEFMsV7fNxCBXk3N_0U4hqdCsJNImEC577G91fiAdBmFxX4-qNasnG1RTqr9RPZTZc-Y3rlz0_1_sRGMta7J7d3UgwpIS2xpoc8NGwOCHiQvCYb4xPl_WZ18zd1DvXi3LJSGcYwlAJhA538WYihkdNvNlNslNHio9Ng6r-l_wPYwUspIZJWMxs7OL6R6b7a2HhO38BsOqrRDsS9bSiiQPc_-rtVNPJ6iVMsyFjhyR1ikAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت جدید گوگل برای تشخیص تصاویر و ویدیوهای هوش مصنوعی
🔹
گوگل به‌زودی قابلیت شناسایی تصاویر و ویدیوهای ساخته‌شده با هوش مصنوعی را به سرویس‌هایی مثل گوگل لنز، سرچ گوگل و مرورگر Chrome اضافه می‌کند.
🔹
قابلیتی که تشخیص محتوای AI را برای کاربران ساده‌تر از همیشه خواهد کرد.
این سیستم با استفاده از واترمارک نامرئی عمل می‌کند.
🔹
فناوری اختصاصی گوگل که روی تمام تصاویر و ویدیوهای تولیدشده توسط Gemini قرار می‌گیرد تا محتوای هوش مصنوعی به‌راحتی قابل شناسایی باشد. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/akhbarefori/653198" target="_blank">📅 15:03 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
