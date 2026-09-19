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
<img src="https://cdn4.telesco.pe/file/C8mdvrnepZewpqBIVOgnhrZ_eJI9jRG4D03fKEnqKY-EZeXUzVBWOe4s9alUCZ6r9ps46iim00Ep6h4-NGqzGobqt1AnARsZZ2KP6tti0z0YMXcu2xY8PC4ylW35YyzzVQGLF6MFnSYKYrrz4EvC14IT45-IWi8HW5grbl77g4rMsrLPprUU54g6BbA7n78OLrfacsUHh1cJbr1_WrfLQohkEhBkji3YyWvkosDVwIoxnkwdJdTVZGE9hp7Cl-l2HbpQB573BLBRpzP45Alp1KJsVxAkwJ39QKLW_z5VqZ2lDBLtBOe4DrLmxe5XnhIE8Z3NhfL_DRGMtHqgI8PMxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 482K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 19:05:31</div>
<hr>

<div class="tg-post" id="msg-30074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=akfxGfP88l7oyWZMGxHQnSpleMzOGeQCsSmuNK6odIKracjqZ91gUBgyFfgNOJRGW9OvZitergnI_hE6pl0wQd1NLPIZsmVUm05AlAbRRe2ndmShEJSLF6QeW9gzHtZ45Zz9YKz5wq6DScRhacCv5QDFSsAoCsfse0R5DZdPqaoEDyOEPH_NOTrg-ULbsyO1ZcC4FayApk7XKaM4423AojvMTpYfKTk40rPugepYG6yy9C-bTNLmcKHVr-c6DrxpVKMHlbRb7nOGXerjO4SX9BKrsXCme5e72YRFVFi7FAmTQcdgsA8-YW-CASjkBRGt7F15sxrypSORd4eL9XnspQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=akfxGfP88l7oyWZMGxHQnSpleMzOGeQCsSmuNK6odIKracjqZ91gUBgyFfgNOJRGW9OvZitergnI_hE6pl0wQd1NLPIZsmVUm05AlAbRRe2ndmShEJSLF6QeW9gzHtZ45Zz9YKz5wq6DScRhacCv5QDFSsAoCsfse0R5DZdPqaoEDyOEPH_NOTrg-ULbsyO1ZcC4FayApk7XKaM4423AojvMTpYfKTk40rPugepYG6yy9C-bTNLmcKHVr-c6DrxpVKMHlbRb7nOGXerjO4SX9BKrsXCme5e72YRFVFi7FAmTQcdgsA8-YW-CASjkBRGt7F15sxrypSORd4eL9XnspQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/30074" target="_blank">📅 18:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30073">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCaWz05mtsQeGSQX64CGuOqS8wHN8TdoTsuWzYWwuQmFQvTEF1tOC30_7tR0kKIFD2UMnQrgxYWwcZNyu-QOyYn9vi7qA6rqy0CP2vHZAGlsGkqO0ovCvV3ygD1pMUQrRZaTmvxdG6j8vN9IepaHrrpBeIUPb0TTGBRe4x4LrXJLMGJvIj-yazwU9znC3cn3-LKv2Mqad1qB7V491wBlQhRcwAIMJvBK-XHw5tSKSYmFHdc5ia2TJgSe65uOlWK8exQxsPS2ssKWlR7QieP6aq6Ej4GeOfczYtFdmpDMid8jOQeVlnu7r105CTBqHM_HaEKqDeI9Q3e5WtSJ2_9YvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ دستمزد بشار رسن در پاختاکور سالانه 600 هزاردلار بود. این‌بازیکن در نیم فصل قراردادش به‌پایان‌میرسه و علی‌رغم اینکه پاختاکور دنبال تمدید قراردادشه اما گفته علاقمندم که به تیم پرسپولیس برگردم و اگه باشگاه بخواهد حاضرم مذاکره کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/30073" target="_blank">📅 18:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30072">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=WSpzLq0yQH6K570TqGcHmVr6zCJW1HbgkFjVh3yyxWfhYAdUwopSHjIvBP5U6BeVutCiy7dFtJF8lNkBt5-gyby9UUPKvEyZpAT4jJm-WWRbNg5Zr67wh0yPBp3MIJTq-puTN5gUWENUAJncZTAKlr-14SxlriZ6swaUPfDHpMCMMg_bKYq8pRiiZF3xujTWepp2KjX-GDtOT3SY1pZzOs5PxDScFKSD1ucXhNPlEOOq3Is1LDmjXN6Nda9McXHK_MkpLIUPwoFHB5rfAEKgNa1ujf1u-SGoLm91IqBeL_9dZqEnEx9skvMHGDRZ7z_ilFmjXe2L0u49hiXT4fOhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=WSpzLq0yQH6K570TqGcHmVr6zCJW1HbgkFjVh3yyxWfhYAdUwopSHjIvBP5U6BeVutCiy7dFtJF8lNkBt5-gyby9UUPKvEyZpAT4jJm-WWRbNg5Zr67wh0yPBp3MIJTq-puTN5gUWENUAJncZTAKlr-14SxlriZ6swaUPfDHpMCMMg_bKYq8pRiiZF3xujTWepp2KjX-GDtOT3SY1pZzOs5PxDScFKSD1ucXhNPlEOOq3Is1LDmjXN6Nda9McXHK_MkpLIUPwoFHB5rfAEKgNa1ujf1u-SGoLm91IqBeL_9dZqEnEx9skvMHGDRZ7z_ilFmjXe2L0u49hiXT4fOhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج الطلبه و دهوک که تحت هدایت علی رضا منصوریان و گلمحمدی اند در فصل جدید لیگ عراق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/30072" target="_blank">📅 18:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDJWK9emWXq66yAxjVv2c2GevtCBvRn-X4jHo0fFXVAAVMlt8A9Rl9PW6GSawH2ICy2fSbClYk5xZSpdVDM9Nr5-mwP9vuJaUe6soc1UocZzBmjZL1t3h7FtUzPkU69lI2ujDM3P9wgKU9VvltsGOXr4TMG-LhWm5TB7kB5VNrT_Aufhmg-fMbKiKzOFXcqJrl86LB3K4lg2OokZAstXe45Zf2N8VmzODTUrcdsczuzXe5a1g9f8AOqHSORvzViYC4F1685Gt_DxQ45jWLDmx7z9ii40UyVzzkTYmuzjrZnv6yw3wBxcyJSH0YAn88l4lAfsEPunZvAEFnkhMwCYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/30071" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30070">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUJKf5DItL38qdgIBMc5doNb-DyZdKUIHfqQ35BZ5IompZOuzYV7D9ECA17A1Xocc0_nDujmqrIpDZ2ApKTpghQVVqgzCa1bEbCi9IG258uW4omaeEJI4P46bEhfZrHeoSFhNio6LBU-2KlZozB8lqbU_OaodyJ9iBcB8mSedCNTHDZiEGDdXkgIDQukO6Tue1pi7ESbneki2NaG49swvN2qPKZSEVpAxXj4SkJ06d6-3alY7jZAQzAm0JHa9Lq1uOaV8oLoFmyb4AZwyKqg9hS_sIJKo4LCZ4vb8IU9CbE1ivDWV2yX3PR-5t9K2S6z1aAf6xcfNfme08CPeZC0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/30070" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30069">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnUlpJ0VUAls4vOa4Mzb8fMve2hI6Jd4M96IcmyyH4tGTq0avJW5XLg7FUhRYyYDB25ztN6EfGRNdHEsBIAJd7yeCrPAYiLRAvLqGMBBqUZPB8DX7BLKL5AvB7mJwBxRvF7JECgXeSP_ADXYPYwwwSP-brOVvY4xZQBELwV_TisDRoFVyFgLHnY3UpMOhFH0vHSsuLVwE8Xe1TsHzumo2gPUydtKjgDy2Od7LMtCSaamHsK_nQHinulenLsqRzaJbUE2vNCkXTGZXhpT01pB-z5AbckIqZhlN8sLiESnHzdPUsbTMqgOp2yL-S7p2S5wdFRjw8PUwRy5Dvt7SU6fMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g28
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/30069" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=lEgOV0KeUh1hY9-b5u7GrU50dpQGjcTD6XPJo1KhNhXfcQds8aGreJB_stHe0x1CuJrQTy2xp7h7maWGhA3azh-FgnyapXIMx5mX7spgrt5g_fu7BvrAINwj-v28R2C3ynwaj81foWJd8Ssvrf7uY-c7VHHSrqcR-eQWry4tSplFdVElA_sH1EeCrhK5vwD9fQdvGBMRwd88sl1mSqxtKZuEq_XMiICay8rIsrvAS51q4CM11QPEWjerBK5oFnhgexnDAlS31M8tShHkRCXkn-TMrKW6S3a4aZFAKvfaHQ8GoSydXMS6zUwMKa8Q88VYvnoDjIpfO_qgKZR53IALvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=lEgOV0KeUh1hY9-b5u7GrU50dpQGjcTD6XPJo1KhNhXfcQds8aGreJB_stHe0x1CuJrQTy2xp7h7maWGhA3azh-FgnyapXIMx5mX7spgrt5g_fu7BvrAINwj-v28R2C3ynwaj81foWJd8Ssvrf7uY-c7VHHSrqcR-eQWry4tSplFdVElA_sH1EeCrhK5vwD9fQdvGBMRwd88sl1mSqxtKZuEq_XMiICay8rIsrvAS51q4CM11QPEWjerBK5oFnhgexnDAlS31M8tShHkRCXkn-TMrKW6S3a4aZFAKvfaHQ8GoSydXMS6zUwMKa8Q88VYvnoDjIpfO_qgKZR53IALvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد لژیونرها در رقابت‌های باشگاهی امشب:
🔴
الشمال
2️⃣
-
1️⃣
السیلیه؛ پیروزی‌مهم یاران امید ابراهیمی مقابل حریف خود با گلزنی بغداد بونجاح!
🟡
اتحاد کلبا
1️⃣
-
1️⃣
العین؛توقف‌اتحاد کلبایی‌ها با وجود درخشش ستاره‌های‌ایرانی خود؛ سامان‌قدوس ستاره تیم ملی ایران زمینه‌ساز…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/30068" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30067">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpRT8Dp6GEGF5RuR0wVVsbzCJ9yyK59HrgRm7RNJ5G3BhTbrpTRtXSFbI9_cAjAvkht-EPC37JfxDqjUYuLq-9DXXXgMmdTsKXc3qOX-Ps8FjlU1USEsV_8aJJAGEWhzL9uqG_jpXjfLBshlBA1HWvjPCjkDxzV0QSyDpOFsQwVNdnSPfTO3QNNTKBkjhpImvnEbcU-AwZOTOpEB-4pflp4qxQpE85P4iezLTe8H8lq90VSvSYnl0dCrKin6vPxqwgLOr1kxgfx6P7RfbUum8CwBpdSFYHskVOQ6n6Z7dCYUyDPzuNbM1Om_0A0_WeBBXABz_3ASXSABTxTQXDg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/30067" target="_blank">📅 17:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30066">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtbGFZvbb_9znM8Xa8Sb4lnZCrALLI4psh0AuWk77_EYGyKcdCfJwzvWyL3cN_u4UAOxW4jcmgUYvolSvBzIclnOX6b3fpFWc2UOCxou6-UJnTNaT9AwISlFoVVKlEmg3QrX6sHwkcgwvKE-729TXR0tkbVmFl0OKnt-rDCHXXPG1snVDVRBMFigV8-I_dkqSqFbSQaIvq52x2VG__f70f88ntQyRhEH7dwyc2JIpYzTBmlnTdkLvT886gWxrrtVCoSKRNqJQEiEgMcTDZcw7Zref-InEGINMja9VMpM3GhgxMBxzk8Ruf3OzC7JZoXSGtUguzdpbDkfSNkMCxP0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
به مناسبت دعوت دوباره CR7 به پرتغال؛ نگاهی‌بیندازیم به‌عملکرد فوق العاده کریس رونالدو در تیم ملی پرتغال؛ نکته‌جالب اینه که پرتغال تموم افتخاراتش رو با حضور CR7 به دست آورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/30066" target="_blank">📅 17:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMOAnUzdVduC697Pjo868Zntg0st8J1-r1_qEdPcfu_ZMeOHkIwkf-aFg0sUz_oV5s6rYmi0H_KaOCKQ1KdUZTrYw6GXEuzPjWcmvQPOva3nvZk76o_ZMG6J1GzXQTdX5-1yzX112uUSL_76ND-RUM8Lqu1RZEY22rsL_RRhc8WJ1aYXzlIT1HTcOFmwz4_XnNcKBaaEWYlBNf0E6f2DPTLAg6xQaZr-7CG1ZUOdUoPP2RSwsUfPAFDkYbjoRs2Q0d1PW3HIrM97PW4t-C9fg9Kea1d4UgBhft7NJpurbuGqImb5NMZJTkPQmuXL2a0iCSzeZtDxnM9cYL_p-i98rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکردفاجعه تاتنهام دی‌زربی در این فصل لیگ جزیره: 5 مسابقه، 3 شکست، 2 مساوی، 0 پیروزی، 8 گل خورده و تنها 2 گل زده در این فصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/30065" target="_blank">📅 17:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig4DHNG-ttUbcyHrsZQ8-rTYCJ2IL7J8AS0bCOfyYeujEp6Y-sqXv2H5jmZbKdQBOUM6RAnaoGcXg9wfKiQJ4foesVOj5kx9rJjdGCBFWdEPB45v-l9H3-zHburTaIlw-Tlu6qNlFgvLJ0DHtI5SvkvoOm-7iC9B_s0CmOFV06igDPtm1ELnusQBNuITe7i84lXZfJAruL9HErskXI9dvsq576_1f9EkuP6m97r6z9XJO5njRBF9WKlpexb-fRlg6M-kYNhbQsdcZ-zepGrdnspjoarg9aMI-viAfaMHerVrMgWnF2LS-ORuQGE-90aKR0oGdQr8LhQ_1fdLLXiUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شب گذشته پرشیانا
◽️
مجتبی حسینی سرمربی آلومینیوم با عقد قرار دادی دوساله سرمربی تیم‌نساجی شد. درحالی گفته بودن بافجر امضا کرده گفتیم فقط مذاکرات مثبتی انجام شده که دیشب مالک نساجی پیشنهاد خیلی سنگینی به حسینی داد و مستقیم رفت نساجی.
⚪️
…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/30064" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=ZPJbOValGdbKk2faZw0IB85Ev2OsYWtcFvXG23dryZvKtUKjt0Ro7vkpacsZSa5ry6rfCpaRFmj9_7XWY2fgU86ufB-hAS_eTxnaFnNDtKJRdbfymZZrAXAgJ2TFjzb7YcY09I1Ij8g6ymwDoAvpNOEIBhOT9MwtNarJQRsYKO1Z4CtaY_5-4Ws7uYGRAunOfARiuUBIo069Y9Ie5eG7RGG2ux23M4jIxEJJH0rDIaBsgwc5jXQcsEe2a5i0q6TUgDzzxvnRQF3YCvYIE_jEv2vJNnZZwpfVdCObw7vBqUPgHKNyeiS3sCRJg0SOmEzK3wNGY9x-LUzLxMnvlZqn02OENKcVmdPQFvU8mH_eMj37FF5KsVWMHc6gbm1TFMPf0h1LBFMDZTi8Iq-mUeBnmIN8nid06QM4sDgrP1HDGfdkWy4lmU9k08Hwa78GhLpAoqrKIzLqwPXfAh0ZqR7I8DFV-FOBskFhDJSV2CuV96Vy9SNH8alNd5-1DsDbzu4XR7maDIz-VHK7oZUGyddfkiSq8HMgFxG0piEjRn86ptWCND1Ybqfmnn6ynDtKJq5TEMTDolgeTpSGpgj5lo81x4aLn8wLcL-oBbmQW85Xn1JuUwpQ2oa8iJXo8qzU3ibrkPe2jA2ixVetoKKZnj3IWYAJu9BJj3hDXApUh2aui50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=ZPJbOValGdbKk2faZw0IB85Ev2OsYWtcFvXG23dryZvKtUKjt0Ro7vkpacsZSa5ry6rfCpaRFmj9_7XWY2fgU86ufB-hAS_eTxnaFnNDtKJRdbfymZZrAXAgJ2TFjzb7YcY09I1Ij8g6ymwDoAvpNOEIBhOT9MwtNarJQRsYKO1Z4CtaY_5-4Ws7uYGRAunOfARiuUBIo069Y9Ie5eG7RGG2ux23M4jIxEJJH0rDIaBsgwc5jXQcsEe2a5i0q6TUgDzzxvnRQF3YCvYIE_jEv2vJNnZZwpfVdCObw7vBqUPgHKNyeiS3sCRJg0SOmEzK3wNGY9x-LUzLxMnvlZqn02OENKcVmdPQFvU8mH_eMj37FF5KsVWMHc6gbm1TFMPf0h1LBFMDZTi8Iq-mUeBnmIN8nid06QM4sDgrP1HDGfdkWy4lmU9k08Hwa78GhLpAoqrKIzLqwPXfAh0ZqR7I8DFV-FOBskFhDJSV2CuV96Vy9SNH8alNd5-1DsDbzu4XR7maDIz-VHK7oZUGyddfkiSq8HMgFxG0piEjRn86ptWCND1Ybqfmnn6ynDtKJq5TEMTDolgeTpSGpgj5lo81x4aLn8wLcL-oBbmQW85Xn1JuUwpQ2oa8iJXo8qzU3ibrkPe2jA2ixVetoKKZnj3IWYAJu9BJj3hDXApUh2aui50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال زیراین ویدیو که یکی از فن پیج هاش گذاشته گفته همین‌کلیپ‌مشخص میکنه که من در حال حاضر بهترین بازیکن جهان هستم و مستحق بردن توپ طلا فوتبال جهان در سال 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/30063" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30061">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwJIgCW_1JGNvlYOU4mffP-Y1nZKVjg_4gJbA3yjV91pEMMfucIRk50pH92as5dvxXLTP5_SZG2PvEmAwv7HBK45cdbS18FQTpqbfGySPmXbB6YncbIYmYV444s5QHG4ZmS7GKw6ARvcjBEw5pA32D_8cMKOQkNBvoVvitkFr89ddWxuP2x1upl7v4kOQEDqj_CY-0LjT-DLo2N3aZ5FL0smRICVZvJbi8EW4LQuhaVHZG7P73lzRZLgRgeC0T9fFNBWs1a6RqJglDx2CYU7IJLaSqvh0SD7fCVJZxpG_ry-KB5FBFlpsGDeu-X6nnWW4qKZbscfZ10o7L5UVSdObA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه فولاد برای فروش یوسف مزرعه وینگر جوان این تیم در نقل و انتقالات نیم فصل 150 میلیارد درخواست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/30061" target="_blank">📅 15:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30060">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOIfCNl9gRHm8Uog2DXJpG4olmDAjikFuVbNOEf6hpCfQPldUZkSrZQCRhD5xyK_VZ8e7KUgMHVMqUO3u8Nq-O_r4yvllCCsNstri2LPoI1DCudRbD9AFZGF32J2EPyAQWWh4lNZs60yln1vV2nGmwiX8corLUZBIgeD8ftQo_XDNlatAcgdR9iGtn1rNUF-pEDzQsyYuMbGyy-0eqZ9UwazjaP0fBjDfQDvyG-Q_JiNM6Dp2bqqr1L_M0HUNKBGT_ozu-mlTOMKqZc_NUY7gWIWK7QHPTYF2zpJA9djZrsyv0FzK7YVFg94JCa4EFSHU26SwdkehpTdhB4dZ6iSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛رقم رضایت نامه عباس کهریزی 20ساله150 میلیاردتومان تعیین شده. حال‌باشگاه پرسپولیس میخواد که با رقم 110 میلیارد رضایت‌نامه کهریزی روقبل از پایان نیم فصل بگیره. کهریزی از استقلال نیز آفر دریافت کرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/30060" target="_blank">📅 15:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30059">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUxcqUNZwEM5ZN_AHoZTZMD6AoW-ctJE0CDzafLzSX2aUHSFH0Ubc6GtCGZYv0ruezYefl-ufhkVBcDE7bvgaB4DebZOXu3yt1jtbss8x1j_QoX-u0qMHjaWm5enlhSy1NqMu05ux3Ff60RDxWv6k4bdsG5PIMK-6N8DyMWjKvKjX6mQ1x8edk7OGNmBmyw_zeWA1gzlbkFYJCpRgBRhoBWd-KIsAr-F-XAbx7ht6W36qU43oMOWLFQrK27b7TGC0E2irJEtT6qSG674axWzQyniPPXqpcYoDzg-lt96G-_pyV_Pdt7Gf6BsQk-uTTLCpx_3K6wd2-9ue7Xx7nSUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
خبرنگارت: بین کریس‌رونالدو
🆚
لیونل مسی انتخاب‌توکدومه؟ مارسلو: کریس‌رونالدو تا ابد. بنظرم بهترین بازیکن تاریخ بدون تعصب کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/30059" target="_blank">📅 15:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30058">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C907D7I9pc6lrtQVwRWz9fla8xVDNG99Ww9uZt4qZiJnwYJm16a3T_EmiTjXDvQVXcLmmAYYK9zYbg815j4MfB7GioRUbb9kSaCBPpaCkR4gASI0Y_wQOVyku_UdkYcR1v4P7paVITiA9RawzmM2DYQr7YK7wOPibA_7lUVKbJ8Gzhnb7AWJJ0C-ipm0TEdQjkelm7M4IXAhyjGqFdoDiaBejOmCaBqSNNhgzWU1dlHeYDOxGbZ9YKmHAE9Gk3YhAmGuq-AzBrzIO1cLUSZNbYPep2DOO91a4nx4vEZVIswszdhTmGpiIokzMTwurdPHNsZ34n8O8tJ_iQkGpLXTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/30058" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30057">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKS77uwWB9J97UPMoe3x49gxP41GlQZnGWSJSUQ4aO07Xh53-xVVAoABvFyloYkBMULO834NKO9pa_clSNCbpO4WOIXQ74U_RHdMHwL5ajnitFgeMOGOWNkyAfJb2n8DEqu5jh_eBKYPXrq-wOgnqAngK5B8DNDz-h3YZFUVoqwiY9k-W3EF4qfA3-5z6bIhWit2C7sDwiQ0FjYHvm1GZwCQ8oYscvB7acn1LptYU8GbcaNWN1OzwPn0CWErQv3jKLpTM9V5NQUIyUtiu_w8bMeIIQT3sG7R4FLUQaSParB5v3LCe4AOyLSeJ5J25-T175VmNlPWrE8tGceJnIQ6hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیانیه‌رسمی‌کمیته‌انضباطی‌درباره شکایت باشگاه پرسپولیس از یاسر آسانی و رد شدن این شکایت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/30057" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30056">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGxUWbHA-B6Id5-eN2mQYk-KmpTdYfdsj7QYosevC3redE5dPcxz8xCNcojzHAo5AwErNp7IHcFaKdP7BXxIMwhKKB2eL8cOYa3wf8rnsxYvpJko5I3MyXsL_quFWat6WyEveRYDUBMa7vxSp92wCneFdZS3WXzAAsO5pdE4NRO68ps-8awDjDYMdsyHfehUCBIstQEBlJBP75hsBJnZdJXHBp5plZtIf4IeC3DL3Iy6BG5ibyKJIQFhUgMcNXZyr0ZOqQ4tAX8q1QJ0Js_wRPs_mKeWtKxHTg3vU2yLDD6V4jgRLFol2XpgV8tIjACyg_1rod2_DYLx8BNBlBE2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی پرسپولیس در دوهفته‌اخیر بارها به مدیریت این باشگاه اعلام کرده بود بین امیر جعفری مدافع چپ گل گهر و ابوذر صفر زاده یکی رو جذب کنند که انتقال جعفری حدود 100 میلیارد تومان برای سرخ‌ها هزینه در برخواهد داشت اما انتقال صفرزاده به شکل…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/30056" target="_blank">📅 14:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30055">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30055" target="_blank">📅 13:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30054">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMjFKqg-w-F_aIXryynWc1qpQtJ5n5ugAW85QdJc2j5-iyTUaQbiKdZvEbXkeWaGSKVjRRI-7gAwribqzLmjviOGyv7gm_qY-g1NPhx2sWWM9lCdC1Do_Q8JOxzc3i8N8ru2h86apkcPJlH4p9QYPyOtaSeVDJ7wiau1ZGr9BTvARFL7dgnhqSEvAzLT017b1CUaQ84pVewvMbRnpSFDxMKi_MUWYKCZtQ4tC57BoMJ9Q7kKWdo0lI83gl_0hzeMPPXfOHkjVBT8e3xGrfAukxo0keZLeppMObzj4E8fuTuYmnQmQRNDq7OEKvlnuB7VXEFL-Ll6nzRf2H6lGpyxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇱
وسلی اسنایدر سه گنجینه گرانبها از تاریخ حضورش در تیم هلند را برای مزایده گذاشت! توپ نقره‌ای جام جهانی ۲۰۱۰؛ مدال رتبه سوم سال ۲۰۱۴؛ توپ بازی هلند-برزیل درمرحله‌یک‌چهارم نهایی ۲۰۱۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30054" target="_blank">📅 13:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30052">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjvawPDppa5ezPEVDuBkp8chimq26JO-XRMVZqyZ30reRuWp1zjT6V35YVGIMqRms3zwv4rBJ-stKWugebnLlJxjZrwt3r0UxspAMkkjD-sytsl6Bo3kZDuruGB7LAPzGYjOf29ItoJ8e8Y62St-uEx0xqSagl48smOEATkgJ6wVHOdy_EeJ2azfDJeOsRLmv1vr_90Ku5B4qbeBQ_dPJXqJzP04PuPiE-mZ9qfF2q3juch382jvzn52DMA_SE36zybjOyjxAV2qd43f4wJFSSRNqTsihl_0STBsGN10ylejKTEYtqjiqZO86dtQmGwFEvIubyTeOUs7w--Ie98OQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=eSRhY-UZHAhV3fotEePrZUy6BbcQZRgHvcjuyV2izLXzroqMRYIN6hkd36_QUq0-QvYak_ABFYgUxBvyksm7d3AgvLbPHTQiNqUQ1AuOQ_r2iyhsF7yrPIyic3qaXJILT0bDrHt_btZa1TdqUPczmSjI9HHOgdNR_5wTfLkLJPNnUcimDaVNml0xU2eNn3MZ9fxYxwgeKykMsV2bla0aAJxnijcxtn5gG330-G30lWAQpFGNoyfm-yqvsDVDaPTkuIQL6q7jtSVx11yTXhSQoR0YbM8lD-mz-SuQNrSwXFG_OkoYxRIZdWPXJMN4iqvzvjWX2y__40G0B4UO8Kduvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=eSRhY-UZHAhV3fotEePrZUy6BbcQZRgHvcjuyV2izLXzroqMRYIN6hkd36_QUq0-QvYak_ABFYgUxBvyksm7d3AgvLbPHTQiNqUQ1AuOQ_r2iyhsF7yrPIyic3qaXJILT0bDrHt_btZa1TdqUPczmSjI9HHOgdNR_5wTfLkLJPNnUcimDaVNml0xU2eNn3MZ9fxYxwgeKykMsV2bla0aAJxnijcxtn5gG330-G30lWAQpFGNoyfm-yqvsDVDaPTkuIQL6q7jtSVx11yTXhSQoR0YbM8lD-mz-SuQNrSwXFG_OkoYxRIZdWPXJMN4iqvzvjWX2y__40G0B4UO8Kduvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/30052" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30051">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI4H9mX3KYUktM4XxgxR3aJVLKxatbMilwWlijKE85PPGoL6x9cxAwHTpxaItORQfdM6KG3mxWQPp4xaEIXvRNP06kuYLmATUMWFkfLb1Av21rjvp_KiGCCq_J4HWWUWpCvnIrdxW1UZ_1zRtDh6n0K7T3zleEKe8VMpiuM6LIalgjMWbVL6S6NqeuFjUZVeerSanaNzuyhqTxrFovh3w_Iz75g-iY0KtpKE4gPORQ3bEhM0D2CiYN9WI6VZlJ7W5UBz7v1LI_cIxsU8zIr3M9bw_j1RSVlJgKIKEVtCn1o7uLP_Fj_9kvXzRUhO58HrWQneoKA8GSIWhzG4JFIfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
هایلایتی‌ازعملکرددرخشان کریم آدیمی وینگر فوق‌العاده سرعتی‌ بارسا باپیراهن این‌تیم؛ آبی‌اناری‌ها برای جذب آدیمی تنها 20 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30051" target="_blank">📅 12:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30050">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=hjJ_J6a0UdRd7DecaKceJAb2H7VZeva6t1ou6p6f-Gc7ribSfgb9H1qvfSJr_peXWE33CUibjxcU9Qs7SJgyIgYUQ0HJc29YQIyERu8BtBF8g9CXu8Fqic4nTa91T5y1Uj-Zr8Jm8My7mBlWwexL7Y2eNjAhuC280Qkpqi0EReu2Sk0A-CX3ycTbtPLDyguN2SucDvnAIbo8ng9Evp732oZ1qS6wuOZ6jVplqCdaKykmgK8nEerj24sER49tzkA4iWU0sMe3PxJDtogsN1ocyqRBZsi_HDIzWDvZ7WHhWxo_bkuggxEWA4a2K_s6zshKdya8upTjCXRBhacuEKTjhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=hjJ_J6a0UdRd7DecaKceJAb2H7VZeva6t1ou6p6f-Gc7ribSfgb9H1qvfSJr_peXWE33CUibjxcU9Qs7SJgyIgYUQ0HJc29YQIyERu8BtBF8g9CXu8Fqic4nTa91T5y1Uj-Zr8Jm8My7mBlWwexL7Y2eNjAhuC280Qkpqi0EReu2Sk0A-CX3ycTbtPLDyguN2SucDvnAIbo8ng9Evp732oZ1qS6wuOZ6jVplqCdaKykmgK8nEerj24sER49tzkA4iWU0sMe3PxJDtogsN1ocyqRBZsi_HDIzWDvZ7WHhWxo_bkuggxEWA4a2K_s6zshKdya8upTjCXRBhacuEKTjhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
سوپرگل‌دیدنی‌فرانسیسکو ترینکائو ستاره الاهلی بعنوان بهترین گل هفته لیگ عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/30050" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30049">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlgwwVSknJefbxru4lAWI5GxVBr-NPlHfjsGDcX5chIg3_gqL5Nqmn2rulDSKEmSjF93y9kpeAmjU2VcaL8__Cg7tQsrHbRm69sZ6BWq4epAT3O7_j0erMcBkMw0alGoJQCC700rdu2yo_xdgAOavAs3IDOmbUs7__9LgJGO1LpmY8NKC86ESWJ-L-Z6B5R9TE2liBFoWs15OJn1TeSXvWDzI_w32-D2wQ52KrYeT6hVWCb7y7XSRPDtLGWjl31s85jMjwMdWzVI4od2hkuR_madZMXMntD9CLJ6KjjhJpTeyrSLNZrqp84FhGoThgqT8M7wNktu7Nz25xTODWoClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آندرانیک تیموریان دستیار قلعه نویی در تیم ملی بعد از سه سال کار با او از کادرفنی تیم ملی جدا شد.
طبق شنیده‌ های پرشیانا؛ در صورت موافقت سهراب بختیاری زاده آندو به کادر استقلال اضافه میشود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30049" target="_blank">📅 11:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30048">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVH8cgpkgihcvu8smJ1TGjDwEiJgSwIjJMsgDSXsIZ_2cP_wsiFXYn5oM2RPOb1hM580O5lkk-fJWtQhtlbI6jSLH2Wsgj_Vg4JNXPQCp6YFj35UXkVmEymfXPHyOilJt4-4Q9B8aapkd7YpXII6DE9tD-Ic5F23HGdLivDWJQeQkrEc-T-sB30g0cSs-rKZ2z5aZ4Z2l00gOVZll9cVjuOQ9lk8qxCSHZfUdgz8ffvwIH8rgwHB-mvylLvSNVI0yrMDcSAKh3EgeVAmozIrwjrymLoeryy9eqovwr6Act9GYBjGF-i8pqyW6niEFPuh9o9SFsEm3cjRadnztskISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جالب یونیون برلین بعدِ گل هفتم بایرن؛ کاش این پسر 19 ساله بارسلونا دهنشو ببنده! کین و اولیسه امروز واقعاً روی فرم هستن و ثابت کردن که شایستگی قرار گرفتن تو جمع مدعیان توپ طلا رو دارن. واکنش اکانت بایرن مونیخ هم ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30048" target="_blank">📅 11:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30047">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kChq9aAdsNXQjX7QmuQ09hXMi6lGo9Epf2CjtsvD092rWn7uY_qGiN9AMDwCq9HgoCQYPHeiR2aEJ72WScbUOX5LCnGViIA1BxbTBOlxU9CBl0hctniT-VtMVamaAqvXCu6b1Pr0o-VP2yKpHco0pHSzmIt8JERsGNIprYaCUcXITIrJD5zEk-HAItmWUrK5gWaL3qreKFiUbA0OiQd1c4DOhm7hApNrUojvZq3IKlXbtPv7zquoawZa9fzGZCAWuRGiZQReIfu_f93CIMJ09wd62wfXML2rPQu_R7oPSm037Z294Lwu6Fj1RN3kYepeuKe7y88HORo0Y6zqrOqp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
یه فلش‌بک بزنیم به زمانی که ژوزه مورینیو سرمربی‌پرتغالی‌رئال‌مادرید برای اینکه خشونت بازی پپه را کم بکنه. فرستادش با تیم زنان تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30047" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30046">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joc4HbUX4dC7Rtsqbc1QaDKQ5b5Zk3qemOaBE2nDlVz9K9pEurVUp-94Fv1je-mSSXNcUUsqneDEzkW0G0OK23oysoU59N3Z3izI_4bwhnlO4uhD1IftdooKc229kap4wrtFdao0BRmpQvPLbHdTnZnZ1sigbBzlQQLKkUnxRuSzXZZqjEqo04E1oUUoT0NelgjLlNOPNiRmt5dtDv_ptowLMP_58E2_I5WgJIRU9WiJQEKvEsoexMgSBoo4t4LIC7Icg72XV2P_dI-CuHAsIFFgtUIYe9CU9jc7utdAAGwrcULTKRe9N4130a_H5wj_gjP-x4rT6JqpfGg8OLpCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کری سنگین مارسلو ستاره سابق رئال مادرید: خودم به تنهایی اندازه بارسلونا، چمپیونزلیگ دارم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30046" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30045">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIX4MF9cOxZ_iHRv3ZZgztHudlRXQioMHp3AzT4M4jfRUgxdndoBUPYgwtaHPYSO2fEMzz_Msa9NT02tNL02Fnm5ciOQGVMqJC998fO1t3ny20kYdyBLozmS2XDkd71qlAZtYGPEfZ7w5EpVyUVRhaZHXjWN6k_AQ0Anx45IqpK6gi7r9dpvWuBjpkKY-__72s15WalrwX3WMwDgLuD_w9WVTEigYOPuuxnBoyo1a1XbdA_Y6pYkqk0lAfRHdW-YP-Ow15muG-y53Z-ZT56rSiwESOYNc-4ZQ6gHR6yGphpiMdOMNXEUcCcqjuxwiCsdNK5OvYqLBeXu8ARctzwiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌تعدادفصل‌های‌الکس‌فرگوسن و لئو مسی برای رسیدن به 49 جام در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30045" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30043">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=vQ7yeBS2-jAzgamBPr0nws3maSsvAPt3UQkjW-hozqsBPqVivwlXpUPjsnRMOPNzDavlxXpSXO1LcqLdqkACXXRhb4gpXNf3LCLpwPqji6LJqp_vgVnNcc8OhPQ4reVSQP6t2WFVuGCW6aoGCBSv2VJE8poK8OYU-0IOt7tfUZJE7vJWIFSeqdKti8rTOlr5FSxO3BIFuFcaiqt1qFhQuGrhMtNkTFFqonFmShFDcdy3OyXbhQR5h_jpyVhoAznKKTnhUvqsURi6XMO3nMuUZ4LOpLtfyRDoGaMEmr-TvsOnOFIs5wU8YRnqhvh3XNAuu8F2lMdm8Ij-DwYQVXAO0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=vQ7yeBS2-jAzgamBPr0nws3maSsvAPt3UQkjW-hozqsBPqVivwlXpUPjsnRMOPNzDavlxXpSXO1LcqLdqkACXXRhb4gpXNf3LCLpwPqji6LJqp_vgVnNcc8OhPQ4reVSQP6t2WFVuGCW6aoGCBSv2VJE8poK8OYU-0IOt7tfUZJE7vJWIFSeqdKti8rTOlr5FSxO3BIFuFcaiqt1qFhQuGrhMtNkTFFqonFmShFDcdy3OyXbhQR5h_jpyVhoAznKKTnhUvqsURi6XMO3nMuUZ4LOpLtfyRDoGaMEmr-TvsOnOFIs5wU8YRnqhvh3XNAuu8F2lMdm8Ij-DwYQVXAO0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد: وقتی گوش دادم. دچار شرم نیابتی شدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30043" target="_blank">📅 10:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30042">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIhv2dx0Fw3NnbWqO-9bnW80jnel5UaHzLQztHKppzKzNFgZcWkQ1XLpLMHm3sOiP2aLS-Ons-bMUfzh__02eVCiYq0keDQ2csFCXeuCyix3ZTG_lRsPJd0g9Moley2VgezsVzv_mPB8wjzHUk-sA68rjgyh1kZtyJXBnTJDbf6MUbHBSstVr0vr4-PhXKN9E_HibExP-TMw0jI3M07a0s3812nOhmP6uTGGgws_QiFmElPV_Na6o8BV3z5-REuElrVSIn4e9dOkpzx8O2nqQQg-zhBsUvROv-yTAx9K8DHo6YYGnkoJRgv_DSZg289pBOVmF51gTJ5Ba4ccYZ6agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇪🇸
🇧🇷
ادعای نشریه NC اسپانیا:
باشگاه رئال مادرید بار دیگر مذاکرات رسمی خود را برای جذب عبدالله اوزان ستاره 17 ساله مراکشی برای رقابت با وینیسیوس جونیور ستاره کهکشانی آغاز کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30042" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30041">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwgYD3HdLxrwn5dE04TIYsQSndIZZKVpyzEZI_ZhoDCJwyuvTAA0U7vNojxcxR_H9FowBDHUe_o02jUFr0RUTxW6DfqN2-EOrAfSMxanqP1vYaNJ_AtPOIfekcN6EPeaBDQsmqAgJ4m-HLG6NGJLCVO3nXxru1PN2Mk34anKTIB7uAW0AoRYC4k91kSZka8uiEM1JkssmnCpQvSEPbYdElMXNVpmJyZ95iLJWzNeCdf9rJHl3PdB4GTpNnYGD23PJNWJEFPfvQ0SfwWjurbQQ56-nSvL_SPK68TsfxW89wj2ky8zvKfmuAp6MgzCn6L6LJBNEPjRlWjddd_BqDdq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
یکی از مدیران باشگاه استقلال: محمد خلیفه و حبیب‌ فرعباسی دو‌گلر تیم‌استقلال هستند و فعلا هیج برنامه ای برای جذب گلر جدید نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30041" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30040">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjlVuBBMMW1HgTiugD0sDRvq-m9ZPkHV8Khk7-jOgVWN2DIH4OO75hnih2A01WmxdlFA3vow91TXdIWjvOcNHZZaNzJvY8Q-WZRBc0TX6_Wb64FWPeO8mlgHhEE1DtVQRdPUTrUQmg57hLdG__fOw1SiwjIgUnKXSlHV3M6rVnAcDG7uiA1E2qKDMHZLL_A90MXHc2TUsl1r7Ub3ENSulbAKOMkn0wSkGTj6efPyDjeFU9hhpMm7-LEMVq46jLNjkmULSqmaEXN4v-q7qs0BEWSOllziWZCFnYGXG4u1m5SSQY8q8LTiezxXDcutpCj-CjSHl1XlhjI7wDfGpI1XJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ محمد قربانی ستاره‌الوحده امارات امشب دربین دوستان نزدیک‌خود گفته از وضعیتم در الوحده راضی‌نیستم و نیم فصل یا با پرسپولیس قرار داد میبندم یا استقلال؛ هرکدومشون‌پول رضایت نامه ام رو پرداخت کنید مشکلی برای عقد قرارداد ندارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30040" target="_blank">📅 09:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30039">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135cc26708.mp4?token=MGwvazXaOTO0J1gWrJAXAsaSDn6GB_X3f9KXtPLCmXSGFeUah1t8WSkPfpfewpm98C8JXXYqdOZrs7UgQ6lXymQ0ZRBdKNfGSH2PQd4d69C4XcqgWhVtDcAPioTWEIozlDMkmEWIBpIYvBxUFci6_qDV04QZLOmOyy7CQiLdhHhysWXh1nHV9X8AlGqrvR736HoDXlb6i-OfWAMU6T_Z0ldEg6E9TxCGOB7iBsz7gtT51Z4GbtOyaM68AqfJ2-9NRFu80XEPprhe1bHH4aiIAeTfXiXaClGUnXdttOWObn5wqESXc_t3EXY1u5UxEP9YNLrh-79e2tOEicFBTPQnuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135cc26708.mp4?token=MGwvazXaOTO0J1gWrJAXAsaSDn6GB_X3f9KXtPLCmXSGFeUah1t8WSkPfpfewpm98C8JXXYqdOZrs7UgQ6lXymQ0ZRBdKNfGSH2PQd4d69C4XcqgWhVtDcAPioTWEIozlDMkmEWIBpIYvBxUFci6_qDV04QZLOmOyy7CQiLdhHhysWXh1nHV9X8AlGqrvR736HoDXlb6i-OfWAMU6T_Z0ldEg6E9TxCGOB7iBsz7gtT51Z4GbtOyaM68AqfJ2-9NRFu80XEPprhe1bHH4aiIAeTfXiXaClGUnXdttOWObn5wqESXc_t3EXY1u5UxEP9YNLrh-79e2tOEicFBTPQnuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌سنگین مهران مدیری درقسمت سوم مرد سه هزار چهره درباره فرهنگ سازی تو جاده چالوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30039" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30037">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=FRaXTZF80vi6sUqFqsil-_uSLEM2iwPY0klFe23UF3UH5n9IpUX2LCBNpK0j1JvKjBaTUog1YZqCTj2jNms8yHXrJQx8u_Ak_MRkHFeYXktPtXrzfsh8OXL9UGnGpBAVRx4jYRLTsHfdPHANH3dqY3aUIT3C2q_PmJ94EYSGM5c4eSTFphtp_0uRVTj6Khk9DCpbarcIuv2RUUbQO6uTm1eFbI2ua1KHoyab7SQ9_syaQ252q5lds5A0niumVzOT8rrNXVCKdstrC_eGuMeuywDKvqPkIZaNffvAx3vBJFDeTsdGwdDRkDzZWh2LudN82tnFHcZthRo6nvCZG_v2fKR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=FRaXTZF80vi6sUqFqsil-_uSLEM2iwPY0klFe23UF3UH5n9IpUX2LCBNpK0j1JvKjBaTUog1YZqCTj2jNms8yHXrJQx8u_Ak_MRkHFeYXktPtXrzfsh8OXL9UGnGpBAVRx4jYRLTsHfdPHANH3dqY3aUIT3C2q_PmJ94EYSGM5c4eSTFphtp_0uRVTj6Khk9DCpbarcIuv2RUUbQO6uTm1eFbI2ua1KHoyab7SQ9_syaQ252q5lds5A0niumVzOT8rrNXVCKdstrC_eGuMeuywDKvqPkIZaNffvAx3vBJFDeTsdGwdDRkDzZWh2LudN82tnFHcZthRo6nvCZG_v2fKR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌مهدی‌مهدوی‌کیااسطوره فوتبال ایران و باشگاه‌پرسپولیس‌درباره‌پیشنهاد 2.5 میلیون دلاری باشگاه چینی داریان که به آن پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30037" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30036">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIFBKtHTRDs7aU_1KvoqQSHF1cacWu8hNvj_Ez7UcKXU3Tr_3rZ7NprCr6hxGoFwnMw728UBI16-b8QDde_7d5b8Ktq-XUtLnsQ9fWHt0tynxnC2jz-yrF_Ift4-tTw5IDBirpNRYFzJTf8LTdie-7WmXKhd5yeSdPcWJs3ByTB2gU2XdYeYaOTnwP2eFE5wbqfGQRkerY4Hdh0RvCToF-CGoqmNTW65Y9zTZYd8orzvmsQGrr5AcB_OC6mUwCisAn4ZhBrylyn6khvvcgVLNjVYPpfxXR21VWVlrsgtFFOsGGXfJCeVTJA3l0NhowCF7x0KRuJV27GNJpErWsEGdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل‌تمام‌عیار یاران دیبالا vs لائوتارو مارتینز برای صدرنشینی در رقابت های سری‌آ و مصاف تماشایی شاگردان فلیک با سویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30036" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30035">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJoSAL7CgUIDvFGkkEZpKgCyoB36xI9zqzvn07ESZbMXAFY437U8L_ZjZpzt8g1Wyod788l8H0vXBLb5L7ZA8izwSHiCeXAtuBJBxZA-7SnHuNaSLaxg07zFhfnIQT7kbdemhhGY9qNcua_YrMmA7b4gTTeYBfgV76BYESI9zMWA6yJj1ht8jyDYewczJx4VT3g1g13Og2i04_m9KRw22PKHmtH0jFNVXifzBiaQk-BHRiMjgGS3BH-vIAVfvU-jiqhC4kD9riOoJwhh_d9y17iFHCoq-5awVNJXEK9u69PtUGIe9Q9N3bZQEECLjpwXTkFUa7QuuNu9NfaIbSjMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از نمایش ناامیدکننده یاران ژابی تاجشنواره گل‌مونیخی‌ها درشب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30035" target="_blank">📅 00:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30033">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
#تکمیلی؛بهداد اقبالی مالک‌جدیدتیم چلسی: از کادرفنی‌حمایت‌کامل‌میکنم و هرچقدر نیاز باشد برای این‌تیم هزینه‌خواهم کرد تا به قهرمانی لیگ جزیره و لیگ‌ قهرمانان‌ برسیم. به هواداران قول میدم چلسی رو درآینده‌نزدیک به جایگاه‌اصلی‌اش برمیگردونیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30033" target="_blank">📅 00:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30032">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUTi5mX67TmHAhdSa8VRDnECWQniUkGU11hY8us44zKkBFjAqNQSMH4EfkbqKMWIIcfbOL38zqKzd3uNy5qOY10EWjHs0xM4DuvT_V3J0wjlrNSN3IT7gTJxXQiqzS77yL6OzK-S5MYm8a63PiuOi-qk5mfttrd7ru-aQEiu0lTJ2ksIdSZaqE1HyUTAuM5IM_GC16Fsi9-vIRoeS0Nj3hDIzW60N7FwdPHFkzqJyBO6sdOXuZErXxNxuxwaugN4YvKQsczN4RJM1DmfLfu-I-MxiRsUavCQ2QOQuGUPEJvaUczG0BRmrHBxWGKPXF1Zxcn8bC9lKNClBxmDsYQjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: دوس دارم در چمپیونز لیگ به رئال مادرید بخوریم. برای‌الکلاسیکو 3 آبان بی نهایت انگیزه داریم و میخوایم یه نتیجه تاریخی رقم بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30032" target="_blank">📅 00:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30031">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30031" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30030">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1lIe1nxCLn2YULoY7okTlG6BJ-EnbafdYOWYtAm1hV52smbT6pjgfjSk3xBKjmd8Ta9SF1P--YDDTxH8cBhFcxvrCUZ6fnS80QzMYEfWKoFS59dk3PHs1M2yka6tPpgWtUADBgRx0b-yHS1tljH2vs52CY6ndn2h8QMtnXWXOnzXEluylzENrflBfhYL-Nt2T94kGF1Q1WKTEZg2ek2uV9znATkLVSi8oTHeQp_QOER6BNrq39p5df7pD4zk91s_cfYe_bbWUg-GYauRYzGcRAFe6WVAWm3xHR2SEu_mZD7kZFgdcaCBoS1NJ6Z1oh0VR5iFlWiPcSTQcQ1PygFBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهم‌یک‌امتیازی‌یحیی و علیمنصور از هفته هشتم لیگ‌برتر عراق: دهوک‌مقابل المینا به تساوی یک بر یک رسید. الطلبه هم با الجولان 2ـ2 مساوی کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30030" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30029">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY3yhPGSOuYqPbSll4_o8XNtzbg9od_eROi5c1YKkPwmVABHyOk82pivbHXDrfoSO7z9xi0WFqoR5Mn_FEpKKEh7eSkGy4oUFuTactw1wWBAynHQTf9HNPDZVhfLIuz5N9IV_A4ENJ6gcJMVAN7PAa8vXdtUjyVNRxi1VzngnCgmgAJB00GH_EpJeuFneSmcqKHq-LoZo7t5eQCof4MHLHDr1Nv--zsAko4mcYvw1_SZPnC4OHbmVeBQs2jPEj_0Nv_W5e_YVvgaSF_5wPx1HgEHcx8HBMlLvZXGLkDNsrUJlMVEDrmVWzJL1slh68FsFoPeZm7c3FnF-6r2_AOfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدارهای هفته اول لیگ برتر بانوان؛ استارت پر قدرت استقلال، پرسپولیس و سپاهان با برتری قاطع مقابل حریفان در ایستگاه اول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30029" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30028">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=BO8pDdt3oUbUPvNduNTpaJ18cOKKh2b8k6yfQn_dZcxz6GOQ8nOlNAhDkPCVIWRB5HJ_VVOgkrFDO21aKXokIKQD_f7xEvisTaztTdqkfukTcXRvFCXJfQNzyjh7jR7tYWeeVAlo_0pkdPXJqfJeKC5H-P08gPy_EXv-9i8ulLNtNMA4SfQLXTy4MQqmtaHKW1RrzJtFRjW6QCaSqtyXcEQIjxcro3ghEbj9tsOD7QRUAdlBMR89Khqvc1tXBDu9wXFIa4eQZY-PgPM7CWq1mZt-A-lz2WzNE1n_8KjjboCKL0e0KoR0D5h5luGQLk3AOD8qGi8XXAqcgvOUqfU2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=BO8pDdt3oUbUPvNduNTpaJ18cOKKh2b8k6yfQn_dZcxz6GOQ8nOlNAhDkPCVIWRB5HJ_VVOgkrFDO21aKXokIKQD_f7xEvisTaztTdqkfukTcXRvFCXJfQNzyjh7jR7tYWeeVAlo_0pkdPXJqfJeKC5H-P08gPy_EXv-9i8ulLNtNMA4SfQLXTy4MQqmtaHKW1RrzJtFRjW6QCaSqtyXcEQIjxcro3ghEbj9tsOD7QRUAdlBMR89Khqvc1tXBDu9wXFIa4eQZY-PgPM7CWq1mZt-A-lz2WzNE1n_8KjjboCKL0e0KoR0D5h5luGQLk3AOD8qGi8XXAqcgvOUqfU2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نحوه وام‌ گرفتن درایران به‌اینصورته که میبینید؛ تیکه‌سنگین مهران مدیری به وام های کلان بعضی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30028" target="_blank">📅 23:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30027">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=q2JV-5K57btPTJ5NC_ItcAcx5fc5Yg_DKPboBa_1LrS6dhfRKmEZKhq9-t1hY6gxJPCfHJC2uMxgL3EjCv_uhV3Lb9KgRUx5Fa9nhLM_8W1fPSANSDAR15rc_qMayPZvhQIz5KNsHJoC_j_lNP3of4H-qYrLKaWKgw_lcISaZVFuJQBgI09hbTqCComTGY3txOJ9OjfxZnneNMU6xQkz-gq50aekFsOQbkxT94WPK6aWpWusJ-bX5g7tkVgNqZkAQIb9Iaqt7gfwp9qbvs8EWMn2ykuIfB4NlDX5a86t3hHq9O9mvrwHfhLb9GHIKoqmDMe6Q7kmMndYBtOO9HUlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=q2JV-5K57btPTJ5NC_ItcAcx5fc5Yg_DKPboBa_1LrS6dhfRKmEZKhq9-t1hY6gxJPCfHJC2uMxgL3EjCv_uhV3Lb9KgRUx5Fa9nhLM_8W1fPSANSDAR15rc_qMayPZvhQIz5KNsHJoC_j_lNP3of4H-qYrLKaWKgw_lcISaZVFuJQBgI09hbTqCComTGY3txOJ9OjfxZnneNMU6xQkz-gq50aekFsOQbkxT94WPK6aWpWusJ-bX5g7tkVgNqZkAQIb9Iaqt7gfwp9qbvs8EWMn2ykuIfB4NlDX5a86t3hHq9O9mvrwHfhLb9GHIKoqmDMe6Q7kmMndYBtOO9HUlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو باشگاه ماخاچ قلعه روسیه از شاهکار تماشایی محمدجواد حسین‌نژاد دربازی شب گذشته؛ تکنیک‌ و آگاهی محیطی حسین‌ نژاد خیلی بالاست سریعا هم تیمی‌اش رو در موقعیت گل قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30027" target="_blank">📅 23:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30026">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eV7aAd2uP5jYYxmO3QM1wp1q5m5U-1ZwYJSS-kPwdpEOqdmnltUTRXTYJBbuxYulveV6BuBa7qHjabW1HPEL7pcTDtOISEnj_ozVo3UI-J5sm_DHAEgM9S0pHa_Ib6sCYi00pkjdXUklj32ttHpM-ALEUh9K_t67f3XnuwpuRFqkly5Q-qtJZfsu__hjhIa2DcedURb-VlMvSu-Xh6yBsPZfmL-Ul24fxZTNgpLAhTrZ7gruns2vbeSAxavG8oUKzBTay0-jAh_bwsHZARPQBrJwotUXlDqOSzhD8VoEndNDEFfPPwGMuJmOrF4GNm6Qvz9GM4dRlkxS5TVd7HGT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بااعلام مدیربرنامه‌های داکنز نازون؛ بازگشت‌این‌بازیکن 31 ساله به جمع آبی پوشان منتفی شده و این بازیکن به مدیریت باشگاه استقلال اعلام کرده علاقه‌ای به بازگشت به لیگ برتر ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30026" target="_blank">📅 22:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30025">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU3BG6Uu8eu_d9gH5W5nL4MJSAErKUZVodlaZVIjXZpjPyxFIr0NVAEFI82QGhY2rzZp3R3mwx-bwzzJ1NplgSYLSsBHGMJqmoV2oBHrenWue-J-rS0UZRc2euQo4XBkdFzjm9FTpIJTgPRzXhU31wV2v0MeZo1Q5nMmipdo8Rf_eeHv4Q4O0Z1earP5omW0lz95DnL3NT3OYW7JwfRwn0zSh-iZ-ZFFwx3uZxgejgG37GqT81vyVaDf_p-QMflXaeDQFK705KiXSXvE8PibBjlz9gOo2l7Z7Wwtd6yrYBro02B2f6-MZHG4CQAioZNooPA5Ds07X8eNfLednt_9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30025" target="_blank">📅 22:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30024">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmDF-LTdqdE50ZLjzzpxKVr9GsRN5KBNzDOCnHITbU2qygY-KhiMh_nPYUkYwQaN-cuaH07BeMNh2SS4G2OtUqaJN3sr9xk2oOAxMAS-2mQizAlepuxvvB0-m7xNP_dDW0xIjaYNOyWzD9hrgBFJjj-HX8Z_JHxdipjlVYnq--1GpIrUcJEqB-4kF1eKtwFOgT_aiIgaRGALttD4sL563qzCmEgKl8tjsW70zzGjE7Pu5FTyGh1fMlTe37nPH1v9Lha4Q37lXiE4cQDKpgjyrBBhlEfl_i4sqVjg0y8bt40bn73qoUAPRF6Wq8GBcpe6uWUlj-mUrHfOgf9V7QOPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30024" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30023">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyVJP9Tnzv3M3ksfoA00wejTXgjI06wTuF86BKBwHJ-EpF67h8dABUbxYy9COXQeCAqXsaeccfhFa6jvy8pfOYq_6XpY54fdfwPdXx-qk9PiQwMDIVC_7_0LwIWdfdFsLMXeWvObW8q4IOTefFkQwioohZynkuQcmJ-W67-LILNwqsCxHQVe8--dljGkl_6J97ueRpiE7DHLIUadXXzOzDaNZEm1a8FgLiXWMitDr1ZCLUQJOs3JAOGrwhX05biUG9mBu06Ads3UUUE-5wiGzAlxdgOsnLIEoifKFww0rvOe25UU-ScODr5ljJOZRFTPVW5KcbyMcFpdgHdJK75BvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی تیم ملی پرتغال؛ کریس رونالدو اسطوره پرتغالی 41 ساله تاریخ رو برای فیفادی پیش رو به تیم ملی دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30023" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30021">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AITz_6TGvlAxlaf-YEJtBkFUrBEl601HUxxLKcjpIBJuRjhFp8JkspHFuMErX9xxbPXNBiLgdmlarctP88UIXRsGwsgi0HZn4qHzxOpNoWs7IW8viHUL1tDe4SLbPgS4sFwXT_Qt9zyC5Qq1zEl4l5EdJT3ALazgo9L7pBSYjj73-ae1OmFzRuJDbNaO7GbMB69A33GkYUlZ30Zr2NPjqbwEEVt-BdRAeIGEO5hhrk2uQr_0-1Ljq_gDKKUxwuNP8wyrDcvJntwVmNHIHgifFqRGjXx1tV1nkoz3u7D9teCZTW0DfNMqJjZ3dOirsd3awYtOm5Pqgd7oHmzDdE2JPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30021" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30020">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🟡
👤
سه‌سال‌پیش‌درچنین‌روزی؛
حین ورود رونالدو همراه با بازیکنان النصر به‌تهران این حماسه تاریخی و فراموش نشدنی توسط مردم خونگرد ما رقم خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30020" target="_blank">📅 20:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30019">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC8YRnyJzizE-THOkbMKiHRjohmbBiYLc9tfZunjNgjVtyykmwyDHZ1MJd-S6RItOZNBhn7fhVL-a56eOXl8Q_sG7W6Tfvybsktg13cvjvK8ZfK0nHa84Lh4rdv3BcEnPnf8Xv8ORoKT2sVcA_xs1t61BBM8Jw7MZIXhPkUDNKnHHe64f6fwSayKD0MMUo2S1CU6kiUVFotknuxYPyQDm08VV0EUS7_qokxMY8rfyPg4y88i4DczAI9rpFw6EBGbceRNVXI-8qwyxYFAahlnRFY18kvDmBAzJ2AuWhOesDd_8ctqux9VgKW5OJIjPL2CljgiCihTNfH_2H9hSloubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30019" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30018">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNm_fAuUKgqFKuOkIwm-DacY9vHE7jo11HlfMaOs3D0t7-Qv7XK3WBhR1b_hsah95M57P-YXzJL23CA-VAoN8HhYyEEz4H8WJuFnDav0KBfSbD5BDYXBIVthyKz2SKCEkodMP8b7bTOwiYw102pNqOuoWHNq-B60vSL726ipw48WEpyBPp2M0jOtNRgWl9RbSlWzGTRuuyERu6NqAX6limQR1hNPqCaAv1CUMXIH2kXZtkzOt8bpTpkMD5bbZvopllPFczGD9XBLIIpK6jfgD3ZtQvurhh14gol1kgYdhaa8SVrWc62OO5YDqtXb9jBZoc8TPz8ObmxqakAyVdSWzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30018" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30016">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_LAr-HQ-GadSours5GDifmX3DO535Qc_qHP6E85Ac9I5GqB_pnAY5H-Ip3SG27GNZHkk5XRa1g675dtXtD0Pc4W8FGA1gbRan2jL9aARp-pGyDi9DFj9-qWdQoRDpcUSx-nkiipydOiaPDjcPeFcUy4PZZqofvjnfs_5c6Wx9DVOhLnR4Gzwk_ph_x9WOKu6FnXZDgHGJvfCfj7F7Dl8kdSBfC4lhXRp4TJg70w_sDM6iPeeDB5ZimCCMO2utcvtJSSrYE-PKmDfVKuPlPsP0vGqdWhrPaOb3z0hxhCRh8_W-nMRlbG4XK0Egz_8RxwKRkosJcjdsclRyXVKanxoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WSfEqh8oqg97wtdwm9-WbeFga7FTftguUrfoE_6TN8V-875Oo_kb57x0QAQ1KALgGLiuSSQnDPsl2jOGrVlkVi9P_VIVDTn_wR6O6YoIiyAdKQC_4-zRpe1aEritnB9FAA7963C_iZE4cmEEyRaThdXjkH5jUKJVn6AcmEfhjNwAepPT_Ev76FeCAeLEAZsI6RrVkp3VOnZkflh9rdij_o8DNjLdrER7iHNnyCHkoiZ4kJnkVfzRNT-IEzv7Lew31OS0xX5ol_F8yJn-nDKI4i7Seue9qgWEGJPNjZ1v4cc2e792qDH2zNlcKpQ3XXgH36un6FSc6Qp14gf3Obbykw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30016" target="_blank">📅 19:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30015">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RZylPAJw99Wqbj7QuYhmmy7oAkITH9-nfNyXmATHKe5OAR-6PLERBdGTPINWs6couMnEdfkVEAuWfMn3QWslx_xe5slMEi6CQznr5OTxuCCtCFbThcrKnqoNlAWB-IwzNeFDNe7zAXBKRwzOoxm0x3TbY9kb-KfX8XPzREt5IMKn-8f6bOfnwshG0qNY2AWRS8TABnzsqlXiF5ueWzs8WgolBSXmZxtvbVnJ4QA40S2rMAk8AxFj7WAH4zPV6TtvMN0G3MoJNW367lP-c9BCmOGs7I_2-t8bx3wqGXX4CZ7Q6iVM9dWuYDWCrV12otcElwjWKKE8jKhDz3v81nSXCL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RZylPAJw99Wqbj7QuYhmmy7oAkITH9-nfNyXmATHKe5OAR-6PLERBdGTPINWs6couMnEdfkVEAuWfMn3QWslx_xe5slMEi6CQznr5OTxuCCtCFbThcrKnqoNlAWB-IwzNeFDNe7zAXBKRwzOoxm0x3TbY9kb-KfX8XPzREt5IMKn-8f6bOfnwshG0qNY2AWRS8TABnzsqlXiF5ueWzs8WgolBSXmZxtvbVnJ4QA40S2rMAk8AxFj7WAH4zPV6TtvMN0G3MoJNW367lP-c9BCmOGs7I_2-t8bx3wqGXX4CZ7Q6iVM9dWuYDWCrV12otcElwjWKKE8jKhDz3v81nSXCL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابک مرادی هافبک سابق استقلال: واقعا دوست دارم زودتر بمیرم. خسته شدم از این وضعیت!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30015" target="_blank">📅 19:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30014">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=qCujdzFbYFU6ERBOZMMSLjn8qY-ZL4QNHRi8fNt5mwlzjV_k-eqMaPfUwPtfC_dDVcx8NOoiO2qqiyVtrMBU_im9jNer54oUfunLNhgWoVL7dGuqWOHZWfA3KtzkSCDQVh-nP-P8SIXbfKPbDqP6MZu-NwvX7qaAM1mi6irqPD4f7VNHi3IvM69ukV4XdexEfxHtsxGUkpIvFT6A4tzNJy_deRzd-sD3GJgZu9ZIq3i4F9schU_G-n8aX7ZvPYYAUpmhBK30_RrqTGUr8uj_7ore3PbhNg8lTVzVg_NYOKCNQzTI9vgLEqVYAmBJkmP96tFK0v5rbA7vRIZfBgzXnTBuqe6MXa_oXBvz-cqLmfmZwjDX9h6Ic7AZm-1f3vrkv7ZrbMLEcNOHWDDLis4Fq7L1YhAHGWRfoj3nG50y8jyn3H_W-HugVCI27a3wLWas9plkM2ZXwskOTjTqhVdl9XdeS_NMtb2a3PK9MOsxNKC9pZqdS8_kCCnSGaQFET65UEZUcqHHZYAxV5xttufyEHLHIeCs4A51b78lhBXnj43AFgqNdOCZrnMbiS6DA4ao-Z4Vs5XHxmBQaTLoSktsHkK1oVtlY9DtM934Mco0XJABj3U9tQ0iO3_zCffjz85kl1S45Nk73UP3YLdzBE7mxa_3n8VVqbbofuwHZVx8L9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=qCujdzFbYFU6ERBOZMMSLjn8qY-ZL4QNHRi8fNt5mwlzjV_k-eqMaPfUwPtfC_dDVcx8NOoiO2qqiyVtrMBU_im9jNer54oUfunLNhgWoVL7dGuqWOHZWfA3KtzkSCDQVh-nP-P8SIXbfKPbDqP6MZu-NwvX7qaAM1mi6irqPD4f7VNHi3IvM69ukV4XdexEfxHtsxGUkpIvFT6A4tzNJy_deRzd-sD3GJgZu9ZIq3i4F9schU_G-n8aX7ZvPYYAUpmhBK30_RrqTGUr8uj_7ore3PbhNg8lTVzVg_NYOKCNQzTI9vgLEqVYAmBJkmP96tFK0v5rbA7vRIZfBgzXnTBuqe6MXa_oXBvz-cqLmfmZwjDX9h6Ic7AZm-1f3vrkv7ZrbMLEcNOHWDDLis4Fq7L1YhAHGWRfoj3nG50y8jyn3H_W-HugVCI27a3wLWas9plkM2ZXwskOTjTqhVdl9XdeS_NMtb2a3PK9MOsxNKC9pZqdS8_kCCnSGaQFET65UEZUcqHHZYAxV5xttufyEHLHIeCs4A51b78lhBXnj43AFgqNdOCZrnMbiS6DA4ao-Z4Vs5XHxmBQaTLoSktsHkK1oVtlY9DtM934Mco0XJABj3U9tQ0iO3_zCffjz85kl1S45Nk73UP3YLdzBE7mxa_3n8VVqbbofuwHZVx8L9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
#تقویم
؛ چهارده سال پیش در چنین روزی؛
کریس رونالدو فوق‌ستاره‌پرتغالی‌رئال مادرید این گل استثنایی رو در دقیقه 90 به تیم منچسترسیتی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30014" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30013">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKnzOQfJNaKJb-eZRNxTgO3KJAJTpCFpdGSVsee5GZQVmpFRCx-dHnbBiiDSJcc9eNaLyljGTWp4CegDN5sPScxp0ycK3cCbmEI01mDTK44ueicOkIR7rbtannEtN8OK79dvdRYXz1daIGXREmli1B0I7aF-O_p51s3Ndk_fzwQBcda279RGievagMcbtb-r8L-Hr2_Mp16ixKf8FrlSwuhrD240lJMhx6qB3aB9n-DzbRq9cZ8CkMiHUWI-nhMPVqY421hanrPYnLDzTbh3jo6oiEDJXmBAdFyIwjX9J293nBZwRM-UVut2j4WDnlvK0AP1F3si08vxoHh1rM8O6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تقویم؛ سال1999میلادی درچنین روزی؛ تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30013" target="_blank">📅 18:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30012">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEjXNGksy1rznazUe_WLVPYTNSRV4hx3Q1M31Kol3ptwc9jfMelzvVvkcW7jD_SWDXHtxnHUyAHh-Yu2__UD7K-B4l19u8axD8MziHv_zfjqwN5-L6fRydojbkZ3eR_2puiEKmdTjtLHkyXplP0AVb0UKh06Foz7fDLhWgEnwMKWVlZ7eJMr7nrUrVmBaat-SNETfiylKv-Nxsx4sYNgLGDskiLujA96_CIUY9EZ0-81PQfWAK3BhcJ5QxLBvRqDpfSO7kCI2GJ8Hgh9j9u26dxDQ3tvNgn425PPc2ZD9wt77k4Vz_F3f0rnwFfnOF2UkVm2jFoeLG9YPiXM2Bt0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30012" target="_blank">📅 17:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30011">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r287cGEM5UpRR7-EV7mWfnurGYVY0mE0XblHZ7JDv9kBTiT8_4FXZKVAgpSfutYousSGwTZKdWqDO-z0aeoKQ6rqSjsWXFSa0UzZRdusnqSXsUuwKo7JH126TlgVLnTFizE7_xSLeB-GdHT2xenC2erdBAb5DJGBxgKj4VrzSwEJ7f8epyCstEWQ1TNyJwHxXE8cdI-O6gFpA7wIisZI4FiXhQj5u_xRHUA2iP5cqNNrdQIIdbwBbUjW13wKXOl91n05RLkIsz9pyjAcDvcBU3Ys9tePlVp2QU5NjyoFO-hm0o8tTEfFlkBahwwDkT-Bz_nM7HMn2n8TDvPfJY57IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزنی آلیسا لمن برای تیم‌فوتبال بانوان یوونتوس در هفته گذشته رقابت‌های فصل سری‌آ ایتالیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30011" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30010">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=WIxOFKi52uy2cK1aKNXOE4YE6KMako2aUvu2mjvxkTDk3lGBlozEZZIXrTJ57EGmcWRdYlAwPC__pxClenB7qHtALcCRmmMuYVMk-FQL_ZFhC5B57h-y1w6Aw6iZQC-teQsYKtXQTQ9EOP4V4R6sEGqKboV-WPJ5EQPDxU3YMOK905p7JBfO-wNXJ-mJNtkDK6rRdNMfkJZX2p8Xomno5y4eEXGj50Gkon0dNd0O4OHDm5JIRd-Zhv1WGGmcheU-0K7F5wGP4Df-9aFcqa9P-sPuRj3cVnOnJ-20xIOixVfTjU5uHFOrxXRPJ-1Q4jwFKpbWTatxJNBTocR4R-SCZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=WIxOFKi52uy2cK1aKNXOE4YE6KMako2aUvu2mjvxkTDk3lGBlozEZZIXrTJ57EGmcWRdYlAwPC__pxClenB7qHtALcCRmmMuYVMk-FQL_ZFhC5B57h-y1w6Aw6iZQC-teQsYKtXQTQ9EOP4V4R6sEGqKboV-WPJ5EQPDxU3YMOK905p7JBfO-wNXJ-mJNtkDK6rRdNMfkJZX2p8Xomno5y4eEXGj50Gkon0dNd0O4OHDm5JIRd-Zhv1WGGmcheU-0K7F5wGP4Df-9aFcqa9P-sPuRj3cVnOnJ-20xIOixVfTjU5uHFOrxXRPJ-1Q4jwFKpbWTatxJNBTocR4R-SCZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ سال1999میلادی درچنین روزی؛
تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30010" target="_blank">📅 17:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30009">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCzrSXUTcAMML9VsB7JVMyphcFieAHFRAZAVSTFn2mE7rYhLHMlgGMqkoCuxh8Qp6pHSclmjLBDInDHAOvMJ2utbJrIJ2RADnh5zSnoX7yMD0nsdpgWMfd0VdMEFhq-QZ9N9nzUj0kNQiNWDJc2w-zaS-t9eF4eQKaPrXol-B5fHnVJh8hlB2vBwFQTxVfLBhGYYzDu57LSW5Ex56XhgZ60PtUxhCT4MVqtRj7fFhISkJG0DAATeiVCZKV3XuLbD4lKHjZqEv7ostMHD7UmSxmq9N8zZ1f6Y5SPFZ84No-wM6AV4YdeBOVzmSTr9SFCzdToxMUbh2g08TH0X_OZa3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30009" target="_blank">📅 17:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30008">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=Mrhd8g0XX-Ye5hhBZd2YQe9wWoNpXoscHrivZIORjy9ilsq33scHc258ontfGrE6AYL1Mo35XfWqYB4pi2a7HUNx7gs6NtVeL8_q8RhT2uN36Gde7kQJb2bZqherS3LxhOJ8UDQsg2ujMw_rUF7tmbjgVtIjbuKvVI1RT14_iMCG2ykNw3N5qqM8pdgTj24yhze5m8wwupq3IPivQ4FZdLPLEEtySkLCl78ZaAdrceSWaKLO9ehPf_2IqK3B6XToVT5jv4tAVYK5erVG6t7FrwORnkT_WEB0UBqgMr4yYdR7tjl73NdJeCMNnjuuW1WWDgLmX4zicBzim-YDwani_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=Mrhd8g0XX-Ye5hhBZd2YQe9wWoNpXoscHrivZIORjy9ilsq33scHc258ontfGrE6AYL1Mo35XfWqYB4pi2a7HUNx7gs6NtVeL8_q8RhT2uN36Gde7kQJb2bZqherS3LxhOJ8UDQsg2ujMw_rUF7tmbjgVtIjbuKvVI1RT14_iMCG2ykNw3N5qqM8pdgTj24yhze5m8wwupq3IPivQ4FZdLPLEEtySkLCl78ZaAdrceSWaKLO9ehPf_2IqK3B6XToVT5jv4tAVYK5erVG6t7FrwORnkT_WEB0UBqgMr4yYdR7tjl73NdJeCMNnjuuW1WWDgLmX4zicBzim-YDwani_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروزصبح‌یکی‌از بزرگترین دوهای ماراتن ۱۰ کیلو متری کشورمخصوص دخترا تو بوستان ولایت تهران برگزار شد که‌ چندین هزار دختر توش شرکت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30008" target="_blank">📅 16:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30006">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHtzxH7sgzToHOqapcIIF6v0C9sPHZ6FB9nGIMlSG8LyjIpQLiI302p_4bM6-8gemODMJxla57g81dIl2u50wHs2jUeptE0HlwS4lXkdTS_wjWQWc5kvj-ilL3opGE39O3ihOI05hHcsOh3QpHjTURawm7vDRwan-2phdTT_2bKgEosGDvH4hv0qRMyBPo4kDffP8yV3zcDqcP1herSvGhRkz1aW4lsHR-MnimRbx4jAaaUnfZscXPB3qEh_ArRtsy-lUawSUvMnAZ6EoT9VDoPhR08e6Je-yyo2IPHvSYiSh0ItvigjsI92nPnH3H_ASfKZ8BK7Xj7DY2FQa2gs-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkUH7TXe5Vp4Uikg1_e4PmBy6QicF3tPPKAulSEUiXONXpl6zVUcMm8hJ1KtUbQQz1zamoVZsqWmxqeTC3SBsaM0_W-KLR2pyH-IJYRpKRmxwGb1whKD0tT9ePI3asWl7mpeOJsp6-5N_WgPepbdjjcJc8qKHqaMe1RvcUA214SAipTRuqiXeO53mnyaFXJwydSIyJLsDwh2ftZC0tyEapPkAZi9X7xSuZNHJW6fyKvB1g9mlspeK6f22T1ZepFqZFKi_qmlDmWn3CB9obtkXXWWLeD0NAjoq_ZRfZJ-9lgp8sZLgXgJqYPVqfgp1ulSbIQThUxOZS4Nebjth8rnHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30006" target="_blank">📅 16:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30005">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ajo3K7cO8-t6fp9vWJznDzU6wP8g4sTdGHxag23ZXzgR3nUFw_Iyggfk_X0n3GWP51M4wjgf2oKRaD2JlngogmfA0Yp0BRfOlvmQeH6LwMq1-qwOoBWF8sCKYG8Li0Myosz1cvN3fCgPj8WPEHg5K7Wer61nqIb5TfrRLIVupXq2YANkO0J_kMVgtAMSujyJNn38KJuQXr3tl9h84aFI8fLv2hOBPrX_Nqe6GNi6A-7ofFi3GP16eicUs1rwCozXly-hYhir4HpNy9JDRGeJpO1k-1EZkBHrYUOzG_3nsfOVqooi5LlPSVZW-zhrLSFzLRgqA14-817taLWhwTZvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30005" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30004">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRUeMNO9cmkqFR5mYdAsnYbPvCOv9cm6lWmiRkBrAqu3tqiFDizrkdwMZ0mAEEqQsALjzUdj1M8jETk_JnIHTYcK74QTtRTjakTxjXHckE5Q7RveSYo5asruu9yunwOa0q8U1NpkIsJJ0JmOKKbx2Gjr9KpOPmOyUDgExD_SOB8VVShjxjlw-7MmWq78j0sPvIH0-eqDboFRKLQkb68r9VbyI64DJumydsQtpusGArPjfylnVsGiYI3_Umr0k8rouMsy1byZLwDGroImJEowdLguyvd7MMFT3E_YXlRiTvNUf3ywoUN3ChyBnuKprQ02M0b225BYslHiU4Ci39ef9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30004" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30003">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ485uLpLJirWpf5zXpZu8UTiDa3HweGfpR4MOHz14Q2zJVVVixxoeLNAKBe0EXLwIUTueXqzi2gcJCysA6b1KdQPEPPI9Wj9-zjcxu7ulDE-cBCj_YTUJjGF62MnepgkfbEGFdWBJvMnP7ivHRoNDcnK2ihMYkpgC0QebWkFg9XR8aNoNUmOfdA7uIYanGo8iWvUwnd9668AH5y_xBJ_7X_haFpawWNm1ygmgez6vO6-rtizb2ANKpVD7EVv1Sac9sPJkt6Ezn2VpMUwQiJLhk4Vj8yslVkw71DMomPasVCsUm6yeAzQhweiWJXsm1X-mOBqrNDOT24NcXkVEPEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30003" target="_blank">📅 15:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30002">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-pxcjXC7dbffJ0z6nx4MJlGXtKjPUTDNaQbSLDnzQVXIFby2Ad6vPWnlcAuWKqymFhqGDCaBeveGFL-2BRrmXRyuTB8WWyb3-ByTC5-Q8F03ig2kjjPREb6FH8nzIHt0n3OkRJIJjCPeC5G8UeHcqfdwy4iBXL9UVRL14zKbiJAkAsEzXHZNO-GvBy0MdMKAq4xip0NMfD_qhA5ZUPTo2-55ZyAG0PQepbhbKkPSDx2fsCJhoOXCznYQ7wc_cuZUKZo2Um3ahvhc9FqP3P8lRFn2JuKqrEvphWYE1oMgv_EKDrOqJ1PLfLmS_o8G19LQXZFbEHqYHyIXqLFgj-4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30002" target="_blank">📅 15:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30001">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=KvNNMKrXwybgupnXgRPQkVOD13rkCcqgEzN1YSs5t7YnPgT57Rq9x1rvuezTgTru7oSuY-4GFKwYPvrycBx0aBm2VQZF61O5UMy7T06kAH4d88NBoIzYTdFWrTAMaiWxUsJQEMDRu4ffqTxJtTRIIwqRkAyWxTTmcnPmLjy5DPF8Odmd1o_DQKeNHEeMesBiQXYMIEBItw5KQaSaqDyga7kxMYzIhvV93EyM4GvaxAbYsUP0cSzeOQFF3TVNSnfDJ3Y-GfOcNU_KsIZafxH9Bo1qdft170HxrNZRBh4Tl0MW8cU2yljKIUL5-1LY7FF6pfay7EdHfGWg0xLAAy24lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=KvNNMKrXwybgupnXgRPQkVOD13rkCcqgEzN1YSs5t7YnPgT57Rq9x1rvuezTgTru7oSuY-4GFKwYPvrycBx0aBm2VQZF61O5UMy7T06kAH4d88NBoIzYTdFWrTAMaiWxUsJQEMDRu4ffqTxJtTRIIwqRkAyWxTTmcnPmLjy5DPF8Odmd1o_DQKeNHEeMesBiQXYMIEBItw5KQaSaqDyga7kxMYzIhvV93EyM4GvaxAbYsUP0cSzeOQFF3TVNSnfDJ3Y-GfOcNU_KsIZafxH9Bo1qdft170HxrNZRBh4Tl0MW8cU2yljKIUL5-1LY7FF6pfay7EdHfGWg0xLAAy24lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو ستاره‌برزیلی‌سابق رئال مادرید: حاضرم تمام پنج قهرمانیم تو چمپیونزلیگ رو بدم تا فقط یک قهرمانی جام جهانی با تیم ملی برزیل داشته باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30001" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30000">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N44-WFrpEsJfzd1i5UnaX9Lr8_Cn_XAnusJGRedggUEa5RLHAPeyfRu-TsINOquIXXYDknXCEdwNf_YAO7pY5BUrs5GiHUisBvPb9WzS7AhIk84q9UyN8LA0Vhb2DnA10u47Ufpk3az3RZBx93x8r1C55y-vlJOQ-sEsRnc3PrfSpd0rlsHfPvz1dNepW8EfM2zk9tLze7UvWCV8N41R9r88SMzUdK6jPlE0YbXLjZmnntbR0TKVcWJefs5v39aHc5JEPDEVRRgmnRAlqQFNavaEtQZ03uRZxva0L_g5ggfMQeJvQbjW0G_mn6epG1uVdaOSKPTEh2Opt3gDQ6ovrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30000" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29999">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmqAJCci8kHvTpQiP3_VNCGDjFaI1Fedj0kh4AX10CApVZ_LDlmKfmlbQ_KScd6wFG9OiU3q8RElDQzZ2z5rgdxwjKlHVo1Fxcalt18ZZ4_ilEm1ahSu7j-zHXVrQNpv5xRVMGMT_ijXogDJ0vGnSJMNkLKlletvj03Tcx5a0NC4xShdM9-PH3eRHLC_G8q7nRCXwnGoqe1rak5aRRLnJ2Dt6FZmpR9_L1mTljyiP8sU2eiALtH-cyD9eMK7kM4KM2UC6NeegWFM8BkYfjlt0afvYsANlSluTIQ0ZK-JBGAHGBGXuvzC57k8eUBLR-lqyLLHd20-3GSyu4pYlRzFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
👤
عملکردفوق‌العاده درخشان تیم منچستر سیتی انزو مارسکا در فصل جدید در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29999" target="_blank">📅 14:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29998">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptqkuiphRRPt9f0BHeLD-Eu1iIJBowXeCilrDczlYB7Com1bwnJngiCRI128OMcgC-wcXvyDb3yWO1D4pAi6KcfyeoUKcOIpFaQv_YC2UCpofQlNyWovJzSpom69NZKvXiV9fiJdPXHvY6KfBCSHm5OUwUp8JuXRGQzU8RDN7qz2fg_AY1cqZUAz-UuOtATQI9eGmF9We0F_SiPVdT8c_erG_g5_n1gNlJZa9Ze4p-0yH-TGWSp_pn1X-JZgAe0qp4iSXenXiaK6ITB2CslJ5SLbcHhgwqVuraJ3_a8reqPWEL7d_Q_5aA4TYqHbrtMvA9DsPPGi5qrb_bckQHeq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29998" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29997">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=ohZMuDyC4yLnjRgYWVJRqd_-MKintnY-FM63upxgKAYaZ3pgt-VlMD4_rlSjkYvgF8IAsQw3HOUqWe2gCyiopvOJiYrBbf1fiNded6gCFjCSFG2HipjNU-aGzJiSXzFqwcZhyQ5i_YvoV1xLHXqlIFIkYF5OdJjq9Zy7nF20L-oNTxWDHaztXvTb9VWzyL6oLp7MqA8tu-J52A5H7RwSpM2GdZu5kmtmtS9OPeQIYcAB5hEjPWSXi6CQZQPPYFdac28vsWY_ebO7hozhNVLdNumrcFCQFenXIxMnDTh-F4Z6t7bPVjk4p6d5aH_RUUbEtWjdj1uTwvylCkGNM2yaNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=ohZMuDyC4yLnjRgYWVJRqd_-MKintnY-FM63upxgKAYaZ3pgt-VlMD4_rlSjkYvgF8IAsQw3HOUqWe2gCyiopvOJiYrBbf1fiNded6gCFjCSFG2HipjNU-aGzJiSXzFqwcZhyQ5i_YvoV1xLHXqlIFIkYF5OdJjq9Zy7nF20L-oNTxWDHaztXvTb9VWzyL6oLp7MqA8tu-J52A5H7RwSpM2GdZu5kmtmtS9OPeQIYcAB5hEjPWSXi6CQZQPPYFdac28vsWY_ebO7hozhNVLdNumrcFCQFenXIxMnDTh-F4Z6t7bPVjk4p6d5aH_RUUbEtWjdj1uTwvylCkGNM2yaNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ 15 سال پیش در چنین روزی؛
نانی ستاره پرتغالی منچستریونایتد این سوپرگل دیدنی رو در رقابت‌های لیگ جزیره به چلسی و پیتر چک زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29997" target="_blank">📅 12:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29996">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOxuD3W3vJGDBOrLGI4z-QDxCDJho2JYzCwEcPC5VGZ2CEzVv_kNTeiM98xrttIxXNF95D-womQB84n3kMSlNtwVrat8ZEQ2_N6N4i9gjufySgYVJ1oHX8kib3sh_va_QRGUKkkaTrcV_ZB40QUrLTI2zNj1VMiem-Z2-toPZXWsQ-9vyghA0yBK-2lJ00KWLzJiOnxeeJ07wNpHCEkknTMYoEiG3HcccSV3Z91BqpM_W07igLksFxO5vuHzVqUnq4-DK5J6hGC0EZBpCeq8wTPsP6SJgdoAFKtIIBtQQ_lAFiFFQt8B0fNqKIqwi6XcXcODKqFrUwkEGwST1vIA4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب پشم ریزون و استثنایی فوق ستاره‌ هایی که همگی‌موافقت‌ خود را برای‌حضور در مسابقه خدا حافظی کارلوس توز از دنیای فوتبال اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29996" target="_blank">📅 12:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29995">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRGjc85jIlKPI552A8WypkBEhuVipibFZhAjm5f6BRy5aGvFDLoQaaZXp4Mr7goyzYPFOSMaWKpp2LHkkVQQznE9AYm1p0RNlbxvFMgzg-Po2Kd7kWWafK4wd-vkbjDQC0ywKI0qyRjd2xo9lIDn5M9xWH1K4lIRHUhOU1tlrKJW9iKwWkY99Mx8KuLUHEHIhipLcb6SvyryCX5h9giI6Uj9AEqUsU0gwrU9O7bYvsZrzbvM9o8_MSIWWqJsWlV5WBzmH9QZTJ-I0q3rcwEkdFL0llrVDygBgfcWXzeGkCEYc06b-6kMEqMpqg9PihY_V0V7-6zxLWwTWHuk8YBB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29995" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29994">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCorBF_rVTh9dnVjpnBo7adtlqtN4ONayROug8Rzaomd0KSwry3pzNutqK3p-FA2xa8zFxH8fxdNK8EHU7sZ0q3Gm55N4j8XHZ3eKDsKz6bAiX3HlHYSrUgz5vO-FAcGjzUwPtMiJ19cUQkTWhtpNYODmeLW7WcLtppheRVArRcjE_Igv1zss4DJYMQN_XjXKdfM6mrw_wOHNbELL30-4xMJPUA6G8dYh0BsjgMKo4lInVQDlLHzVTzBXlJiPqb786Cnz1S0uF1PIHxpGOrms3X7JPz9zNkZusQrCbYtBgG3b7gsbVjodqsvGImQLZDv9gK7pBvt30X607A6OP1Q9UsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCorBF_rVTh9dnVjpnBo7adtlqtN4ONayROug8Rzaomd0KSwry3pzNutqK3p-FA2xa8zFxH8fxdNK8EHU7sZ0q3Gm55N4j8XHZ3eKDsKz6bAiX3HlHYSrUgz5vO-FAcGjzUwPtMiJ19cUQkTWhtpNYODmeLW7WcLtppheRVArRcjE_Igv1zss4DJYMQN_XjXKdfM6mrw_wOHNbELL30-4xMJPUA6G8dYh0BsjgMKo4lInVQDlLHzVTzBXlJiPqb786Cnz1S0uF1PIHxpGOrms3X7JPz9zNkZusQrCbYtBgG3b7gsbVjodqsvGImQLZDv9gK7pBvt30X607A6OP1Q9UsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از کاشته های دو ضرب در محوطه جریمه حریفان؛ همه خراب کردند تا اینکه بالاخره یه نفره یه بهترین شکل مملکن دروازه رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29994" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29992">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVD7-8kH86NzRc5yR15XdGs5jyJppStCIbH1G7Qn_WUoQxPqFCK2bh86YpcW1SzW7jKDfoEt6N6R-NhB4pSuo7EDPqKHvvyO0425YjDx9yyomrOKZTp9Fa9SD-O-swPF3RXLwy1NF-fJSw0uy9384v_CasUIINxI8CfUXh2JB0sOLZXnR5Uz44w7tHIVyeG-Dhxrm82ZjGcrIjD9Eh5cThcFdRjVEQG6dmoKRPimDtvfWxH2u0iJoMp7a6EKIpxxBNgBiuRxUaslpxZL1ztvP-VsquscVzT7tgQdclH9jkh7yyGBlhrepR7I-AVCpiMayoFxZZ-ZdjJnf7A5_D9kXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29992" target="_blank">📅 11:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29991">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zYBr2-z8HUk7a_7nbt3dqs7hr2meNgTVhryPin45bkhuxu6lwu9q1evzYPtIvuFmGLpIOKPJmo9P0ZaQf3lN9mHOTkoxPepmYSnnIdZ84l7htUXMygsHSZzbjwAnv3PwuW4h5uyrRhQUUGAa3KdXBkFHdptG6tLI1EE9SXYxMUhCK0jt4VlT2j4EEr-uA5PRFMS3cP8PhA1xcudPxxdkj83K6IFEx8C6dPCfOTKStZD6LuX-ZqI5xbD0nZ4Z-NgTh-nDq-SNbov6zcs-n6284KJwtcD1HVPiwHcS3ixtsIPAhQMyivpLC6ohj40AdYA6mwx5fblw05vFo0mMcODgtmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zYBr2-z8HUk7a_7nbt3dqs7hr2meNgTVhryPin45bkhuxu6lwu9q1evzYPtIvuFmGLpIOKPJmo9P0ZaQf3lN9mHOTkoxPepmYSnnIdZ84l7htUXMygsHSZzbjwAnv3PwuW4h5uyrRhQUUGAa3KdXBkFHdptG6tLI1EE9SXYxMUhCK0jt4VlT2j4EEr-uA5PRFMS3cP8PhA1xcudPxxdkj83K6IFEx8C6dPCfOTKStZD6LuX-ZqI5xbD0nZ4Z-NgTh-nDq-SNbov6zcs-n6284KJwtcD1HVPiwHcS3ixtsIPAhQMyivpLC6ohj40AdYA6mwx5fblw05vFo0mMcODgtmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دقیق و برگ‌ریزون عادل از پاداش 20 هزار دلاری مهدی تاج و دار و دسته‌ اش سر پیروزی شاگردان کی‌روش مقابل ولز درجام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29991" target="_blank">📅 11:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29990">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_g5vpuAfGiZa8yZlyZtDjhVvyTUzzlOzxzwBvl3VJpaP0oKvIxmUO_vbOSJ0ADSpaQF7WsOyBw5TkpLRCgENf3lLmvKs8swI4_END86aq4VLCUKwG-_6PH_rG11qY4CpmSPaEg-4kiiAOD2ud60J71kh-CU2Dp4MuzP1sTAo2YOpy0bd3QGrXo88WE9L_0IM4mEZ6-NjpWigNL89rmbMrF7XGwRywnAdljDh_H0_bWP7oYMl05-JFgDz6IIk4ZDqWmdgv_TyGm4MJnq0lXzGyM-LhFZY8oCUPkEfGjZJtvyFcmKdSR_SliEcSoQ2WOGcHB42FC11QEmW5zKzJsapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور
🆚
رافینیا دیاز با پیراهن بارسلونا؛ رافینیا همین امسال به تعداد گل‌ های نیمار در کل دوران حضورش در بارسا میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29990" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29989">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG6AEzab0tJWBBSwLYdNKZmdYRLBtCGfzi_7w1MhByibzgOnnbqNVmrTPMR21tDuMfwXNBskVhu7ttMabUBkyt5tZWvam8Rw2y3JtowG_qVKjyboYEQeanYJkvLv_8whKRg9RRWIbHr3-CzmvRqWlz4_7XCsln5pA3JEScyo5Fr8wZ5NOTkVLJwXvDAEZpyfdaWTcji4KxLsm1uC5B5gOh2Kwx_Boa89C0OaBGtNgNU282YqHvOMIDWmGXR3b8o3Yodx15sTbwoq52YXVWUw3OpD4dRuyLZ46ArpIJyXIqFX8S-3rIr6Tm6RN6CJo-FlI9NWjNb2UakPuGJwGeb_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برترین‌گلزنان‌ پنج‌ لیگ معتبر اروپایی تا پایان رقابت‌های این‌هفته؛ رافینیا دیاز با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29989" target="_blank">📅 10:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29988">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry9kyZb6uzmw_QdBuT-REZ_NtHB6kiH7B2fCrd3Eree00Lz50yyf_kZjyMbrjCpawVJWrfOiW7kbluAGeWMJRADI_MtwdxralIsu9yW0zzTIvYGOfHHDPciEvYTone1QVpEOlOG1mbYi2drZIn7yzFUKrpxwn6sTsjAa-lny8L2mnJRNUNvFVutOuMDkYZBr28wnHPQ7iBj6yGXHcJL6uIOr0Yjv2nBiNGahfCbPr6a5CcINTcl7KiVYXJIMgQCLQC6dI9ayA65Arx_Oz5yIbntmD3K9jeRhWUUCjzrEmspsfXCI21fuRzeJXUaMjrrLWdNZorD0Y44OB6ywLmiT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29988" target="_blank">📅 10:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29987">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=KOLL_uh8ZnyRNuAC5Lrcc2I0FQo0DmoHR4xiRrk-U0wpecGzgtqE32YnsUdsbUPh4yXBu3WHa3ZkUjTwuyPJDj_zeRgEGGk1-8rFe9PHxIMyBLsCN9Lgzmu2bKqsxYn9lhNDLq1EB2Pq1epQNDGZ1YZtst_ULjLkd9yRPrfwSZH61XQX_C55ujBCo0Il9NRo3nNzp5RSxrzoERzXRxo0mFdGnpVwSzrfWRqOjvNQYzdZH1Lu_bgySoheIAupZMkjK561uGL1ZLZj0laDTLNJ8TkqshmbPtLtnmQpETDhOa0ny3-hYqDlDAae-qCOFZLQQa-xFouCLcMh77H5HFM9qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=KOLL_uh8ZnyRNuAC5Lrcc2I0FQo0DmoHR4xiRrk-U0wpecGzgtqE32YnsUdsbUPh4yXBu3WHa3ZkUjTwuyPJDj_zeRgEGGk1-8rFe9PHxIMyBLsCN9Lgzmu2bKqsxYn9lhNDLq1EB2Pq1epQNDGZ1YZtst_ULjLkd9yRPrfwSZH61XQX_C55ujBCo0Il9NRo3nNzp5RSxrzoERzXRxo0mFdGnpVwSzrfWRqOjvNQYzdZH1Lu_bgySoheIAupZMkjK561uGL1ZLZj0laDTLNJ8TkqshmbPtLtnmQpETDhOa0ny3-hYqDlDAae-qCOFZLQQa-xFouCLcMh77H5HFM9qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی مثبت 18 مجری‌صداسیما روی آنتن زنده؛ طبق آماربببنده‌های‌صداوسیما از سال گذشته تا کنون به یک دهم‌تبدیل‌شده. مثلا یه برنامه تلویزیونی زنده شاید روی هم50هزار ببننده‌داشته‌باشه تو ‌کل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29987" target="_blank">📅 10:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29985">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a52708609.mp4?token=a8X1eHvaetmEWoOWe5Hlz9WGrkPRtAkbqYTNnbV4EsTvupz9W0W2GHwj2vVYRw6Quo17Ss6OTHJy3Ogo3tc7kyNKCR0R6OYvFWZpcOqQMzfHbUHy56p0XY7MzrAKJhz6b7udvObrh88rCW6HRUfPg07JZ8eQcr4diPgMlcAfIvUJn1ktbaSxE4el4A2v7vWV9ycY9wE-tdHmAdswk7WmcQRmSWqogH3joO0UqQ_Gi0UHh48tZHasE_1bCpYSY6fThT6cewqQTk98bXI344FsnLs1KBFox9SdC1-NNldsTJoEkCiiXJeD0_jwJCSXiRHLyrl7hXsf68WxTp7UepTT3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a52708609.mp4?token=a8X1eHvaetmEWoOWe5Hlz9WGrkPRtAkbqYTNnbV4EsTvupz9W0W2GHwj2vVYRw6Quo17Ss6OTHJy3Ogo3tc7kyNKCR0R6OYvFWZpcOqQMzfHbUHy56p0XY7MzrAKJhz6b7udvObrh88rCW6HRUfPg07JZ8eQcr4diPgMlcAfIvUJn1ktbaSxE4el4A2v7vWV9ycY9wE-tdHmAdswk7WmcQRmSWqogH3joO0UqQ_Gi0UHh48tZHasE_1bCpYSY6fThT6cewqQTk98bXI344FsnLs1KBFox9SdC1-NNldsTJoEkCiiXJeD0_jwJCSXiRHLyrl7hXsf68WxTp7UepTT3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
محمدجوادحسین‌نژاد که جدایی‌اش از ماخاچ قلعه در نیم‌فصل قطعی شده امشب از نیمه دوم برای تیمش به میدان رفت و با اینکه بازی رو سه بر یک واگذار کردند نمره خوب 7.0 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29985" target="_blank">📅 09:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29984">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiXaF9tEJQ60Fzwjq13_l_QSP_qKptBIbZZbxzCMtPw-p-2mYVAqAm3jHzI-DB7FFBL7EpRq8cZ9qEpHiJ4vTkZ6xynqsZ_r6jEjEl7u9vsM6SDqaFQcN1AvdENMW6DWFT52uUi0tELiYmaay6q6AiWxucxNb1XmAwisVrjnkJszxBsAYToY0lP3NrQtDPGbQZhRDTmGEcbEnmz-1AUPRtaGMKFQcPtIeuh46GOTFHKdwc7V95tbaFwlXbmnRZVbGm-Ba_LGkwNfdZnvmc7kmVoTKS8TWyRJksarHceuDWtEvT-hiZkBz08OqxDgT4KWF5gMr7RKY8B1kCBE9Nog-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امباپه‌ستاره‌رئال:
اگه‌میتونستم یه بازیکن رو به رئال مادرید بیارم کریس رونالدو رو میاوردم. او در این سن هم میتونه موثر بازی کنه. اگه به رئال مادرید برگرده قطعا میتونیم یه زوج خطرناک تشکیل بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29984" target="_blank">📅 01:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29983">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV51MFoS6J_RFEOGyWT0X1n_AKdBKfOq9tRCAzuAwoHWDAamqIj-pHVGqwh5e-I040It9F0d5XNAeRQYqMEsRJxkej0NIYsD0KOYFKLPF0C_KlIP82mn7_6_0zKu-q6KPfUWvYorh70CYt9fcHC_U-iO5fNUe9JwuuffcASETCmb2Z-477A5HbJ06ffOl_s241JBQ_F13lIvqrIdHvAq-57I7R-PY_bOwPI931IXExiJKdSH6XKIx_SrDiyv69yJ39aUaLI1XkWkftARxW3JKk-rgZTrKhRmIi03OG5PFzpXbD5_xM9mpYiQc3wVzMaiQwDeww5vtu6WdPV0363URg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29983" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29981">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCmDG-dto1tsbIFKWrkDACjtng94Gj4O9BYZxGrOUhzHSPzp_sL3RETuOgE6xOEgA3NRa-g0V6R0_M_HeD_a5xcmvPQqTgGlZqmXf62NbLvWwLKNJC60WbZ9Vsj6C7kcLe1QnsqDEXx_7JauWynhdcyOD5oPYvsfVpmUVyKKF7YTw4yvAauLU_Cl4zprrnqh7X2BPMyswaXaumCbciO64XTIpaa5wUy_-nUBDNfkOcs_gXqNmQoFDWmfM4g5u-nOlBIKZSeui_LJ-6hTKv8xNt7lM2x1O2NK93mXqHqb96dIFgNFS1KeOnVP6rF4I-WJbzQQXQxe7ZX03-ZoD9Vsxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛جدال آلونسو و شاگردانش با برنتفورد برای بازگشت به کورس صدرنشینی لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29981" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29980">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMy_VVn1tnxEFbmqOS5MekcSlf5K58Q53MToWXnBhiVsN03WpM3FIEd2PEtaGTKV0SLj_7TeVfDgZDKE2qxKPM_j-PIlXnuKcIt4n5laG1j1UIaehKpwrrDcpo_ENYISSsfE65L_2rY_GgBsLFKKAH_0W6rVXekV_wlHieRflCrFtSSiGxHBYP5-FgAOtCB6UxrpFCuvMpaE_jt59wvh0UTGa5P_nt3BPNe4ck0Z54s7kf_veuUSmVx0Nco9W5YYFFW8KLNc_PCU_Xob2I00ZdMaQhaC8uYnzdwvTQ5RSyC-vg3WqrAdFVtxJ9SVg8FMpD3BdMsvJGEovVU5Lyy5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازچهل‌‌نهمین‌قهرمانی مسی افسانه‌ای تا برد پرگل یاران اسپالتی در آغاز لیگ‌اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29980" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📊
عملکرد بازیکنان رئال‌مادرید درفصل‌جدید؛ امباپه با 8 گل‌زده و 2 پاس گل برترین بازبکن کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29978" target="_blank">📅 00:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29977">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhS0o6fAO2uJXbX9r5Zi7tTZnfos3WB-DAViA6s5E3_wtkEHDBgnxJpmNrhYY6WFTLKIvYn_Fdqu2q_TFEy2zJwFvxVgfpeZrVy5eXnV1PR68kCZ5MZF0-Hmws4Q7V9cC3vqhuny-U-kHT-u2UanGi7n-QXaSLotebbiSM_Lsv-bj902IyTXZVelf9xBtvgDXtwJ2LRSJS29kxzHE8DZ8vnww6O2eTUue3H3BMzr0s8Gr0_Y6o3yaw6sc4AjUVAw-7CBnW9fX3ISiV-ULZalzfdh-ltAdD0XL5dsVPlbbS1xesmWa_i7b24DbklQplzQOIEm87DbxbHQQNJqNjubRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29977" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2gk2uHIwVQpUNZuy_3_Lo3L9YheNu1uTNkil5jOuvG3SxSR1Q-JhiIsCxZoek-Zjty88n2P45yPBHMYec9ufal3mCQ1ykodUafqbbzHrz7WcA5xAbCICgXLSplLF0RsJc2oP34TnU8srgZu2Pm5CIleUlwJ6sXHYS3Kh3bEuqXy4a6XqGoS2xXRdfeoEWgv5sgKP3bOu3LOwtAxawdwLSCBzQkP3tn2Ttr3ZhwYUvvq2DZMWcYQlqWGMH7OR-54hDkEhghGabSSNAB3Eek-NVF-cSC_62lcvq-uHNsxq6RNrbKozC3K1TKyRaRwKrd7W-WrwCCatVN1mxXFDhvkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29976" target="_blank">📅 00:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29975">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6e479TcQDA9QYUg9tanu-n16VXiTykm2V0sa-bsaOigOazn0BScsT23qe_wbkei-sv4ZRgIVwj1wQHcdft1DWYwS6g5a3SYMyyXv_N99CTnb9Y6eUGebg6duiLS1dcxwRZvdb7Wknj9bE5jJj4S9lir8_J5FCmV66mNQ1Qp3M5lgWz2eY0QMZoZxDUPb6NliM1ryIvYYkEboM5-B7CdSrKlo2dPAMvDNjGWF3DLt6cvAFXWHgzmiBNpX5HEyCEkh8VShbiPEXA_QIqcakOkLZbgEYG4ligwA-TqADIlg3tw2jNyCDwOFzAplNmGH1qT_LWZVW_ZbX92WvknbiGvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این پست برای رفقایی که بدنسازی کار میکنند؛
ویتامین‌ها و مکمل‌های‌مهم برای وررزشکاران در کنار یک تمرین خوب برای ساختن یک بدن حرفه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29975" target="_blank">📅 00:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29974">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQiWIgqkx2ePzGv5yhJM1qx9uW2F56HOHBHsbFMth_W2dALIcFdudgvbxbjH5lVe9ZxdmriDpcHnOARuFdJjSywjYabyTdqeAw1wtos3TPmZecodnVBAnUwgyNrn3wCyuzlPD1CMKkARyHDjSRIQOWWSLV8bNNJXcgsJcFXNemzkPDUG_aK1me5Qn3T6hI5y6VkYdZHufTO4oN2OI6_0-OZTQBTHrHF8OZ3cw8fkZthDMvMJ5BI16yQePUpII1FLTLcY-CEHlP851mWva3eq9-YvMnqV-TMbVxSen7-15wIrbSzHzubmO3iKmj-aZFOL4tVyvWzNB_NwmUYhxFTm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29974" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29973">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkJRQpqwbeS0z7v0RXlMYx5uAa6xWewk-iZotdzMjnNHqlnprFjVn3c1S2QVwONIQu_JnL1pQia7LNrgm3Qrl8Zb4f9EUrFX8rrcfbhyyhd0UEc6J6l0lGdWh1FTzQNKJOfBXDEv7kXbuitZFTQAGPSWFI_3Yax3o7HeJUNv5N8d4qBQDSbL2-i7BT3JSd44koUBI2FQcDjLr_q0DDp3o9Y7Qn5KrumI5Tjic2q7yPPVEQ34lb1zV_8eFn8crGPEt6IPWs7X1dzBOgQbFZT7WJqmOLqZgEYIAKRw_cUlv1TVq3xXAZa0bo7NHFumWRmvPFFVKxkBUtuM8gkJ7QebgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN
: درصورتیکه‌هانسی‌فلیک امسال تیم بارسلونا رو به‌قهرمانی لیگ قهرمانان اروپا برسونه لاپورتا قراردادش رو سه ساله دیگر تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29973" target="_blank">📅 23:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf16k6Byf7nTUJ7o9EETNPznanLU7NZN_si_efQZ3YQ2N8PXWl2uxVjt19ZNz562FTHc-e7uizNJPyVqJyDO1ms-cOqePSLAJo38OgH2s21i9AyE6cIXnDrHR--wqiZV3G1gZ5BuzEB4YFk4A_hznZisONa4321nwlPDzxCTPpQeW0Bk7S-PVnNKcS3dVGLVuEFVOvgSF2uk29bBicRi6aCbsoRE03RVkBW_E9LkF2QZMxBBGBY64CuRsNUc-KQ4dvX1N_g_8ewQygSYAjnCOu0XG4HjCxos8-FmsR9k78EhkvmMMZGAU0AQJUgNgO7UCG4jp-iCVw_RBwkl0HvugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29972" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29971">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhTepQLuhmSCNLCI5cz2XB3y3IutbkXgjhB769idR0Ie3OAC9wcurIUgRko7YPOkuuQt8AQO6vFRz8STD9Wi_yd4D3TGVwfm6IcuPzog0GCdcgEp0mLmazxYg3fjXupYMrcWHaAInDcgU_Qd4uvIMEt_FV9dg3aaOd3jKfd2B9R0vB_yoD414dMfbeWMNEsvaqWMereZZi4n0zsq4Etl64ioQIQpbqke7EJxWK0bpcmBb6q0Z_0WTbQUXmtXgeTiOPNfoqHyeCFJ1lkju1alWeOaDvvEoge5B4JlGB_Z8AExplJVjv8pGaipEC9Q98Zhw6WrDscr41kwpCzpkSlLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29971" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VutAFuYDPupkRvtCZQnPggswPqZ_f5ZwPa-6pq08k3SVoTaWWql0-Dm6YBzdxOsTtZZa8vI7Cu7VUHFNmJwHRgjcXcFm9FewQyvvGflwiNh9Y4Lg-rIZVDhek9l8p71wNrywUm3dRttCwqbKiBzY1YIKqq_V3fBPxP_oyX1djy3LYHbC4twZF27iAXJt8TfaiqS3kXxLQRx-Esid3LqzjBAN-qLJxCkEYH_wc6TJrOrng4TKKU07R8Ru39YOdJSGXbSgLGYPBoPLbp39bY8bOdmBQbycO9_illl2jN8Upz1ry668ZKOx5ImDloH95PhqCVth38le6lwSk7PoAn4DHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29970" target="_blank">📅 22:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=A2gO1l4xZiqNJjuZI10y3bMYOsLP1MKWkh2PIgLJEdptuP36dw121qlf12y5JKC7vRtAKI2zuW2_dbyh6DKPCwQ0RJqCu3sN5l_qrVXp3DviILn-7IlZOR55b1FKiNLLs451hlsPlsqkMfRmEKIdSaZc1cFN-_mLv__tT0YkvI3XCvECvlmwefeIhQJiVOq0wVtrrz5StE9q0OUD5asApaIMYbxSDeTHs-6hUSI2AsLwnGvm_pKDQSq1UeEMlxj3ibLSti2GsCtIBtWTxZN4JnbNSG5HmB2Cu4bxlkJZgdKmBHpldGSXBmV9jmP0U3WCoVzm5gQSeg3BolAh8CIjmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=A2gO1l4xZiqNJjuZI10y3bMYOsLP1MKWkh2PIgLJEdptuP36dw121qlf12y5JKC7vRtAKI2zuW2_dbyh6DKPCwQ0RJqCu3sN5l_qrVXp3DviILn-7IlZOR55b1FKiNLLs451hlsPlsqkMfRmEKIdSaZc1cFN-_mLv__tT0YkvI3XCvECvlmwefeIhQJiVOq0wVtrrz5StE9q0OUD5asApaIMYbxSDeTHs-6hUSI2AsLwnGvm_pKDQSq1UeEMlxj3ibLSti2GsCtIBtWTxZN4JnbNSG5HmB2Cu4bxlkJZgdKmBHpldGSXBmV9jmP0U3WCoVzm5gQSeg3BolAh8CIjmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29969" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=XY3K7qBBijTejFLDV_g2WcjDQeWEirHpPwHW8cawB8h_6MgK7NllS9xuhrgixQuUVBMwPo_tLtlGjPZaqZSYYXjc0EUf5OUq2xjMQmxaIjDo6WT9Zq9qzFW2Yv0hbGQLqsFvmWdgzCp2GTPAbUr124p07ssEpeNZKQHeYb-JTkovCkyhVrVmgUdcAJAnrO5cLMaWW8a1vGMLgfoHHxyiHl0I5F2cwQ7OoDyXhyztVJk_YXXfcTZo3avgQHjGTAQAO7Ox34ScjDWcxT2eUCaQ1bxyovv-pb9rq5vfFwtH8BxN8IMyIHamLqjUTtSv0dAKQ0Pvww4ZHWpdfgf3FCNQHppCypY0vL-Wxhp_lT_M815KTFSLUcWVnBRp37yICAfqgsUk2mT0sVFDNQjnW3shDKKcvC84XZEK4U_g3vjgcCBKva-YFO5HOOEiVlChnMtC4uayBayMKSSlOKc535nQYsjp7tMZErkPtspEhvsAhPhJi8KRVPb4D9WssMq2_6QmVEIAPzU7xeSqzwPGQKZ8Sk9CIernbYTksljOpXrputdKsPmZgDTGPqRLrzid9hf-4IvYYs_822_FektG8hTpfgqK5eNjU2JLUjFyEfPaBfR8zdMX69wlwvXIqWnBpsX49nq_7gqHAYpoiE1bYcpgx0ZqmeZL5gP5aHHqWef0iy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=XY3K7qBBijTejFLDV_g2WcjDQeWEirHpPwHW8cawB8h_6MgK7NllS9xuhrgixQuUVBMwPo_tLtlGjPZaqZSYYXjc0EUf5OUq2xjMQmxaIjDo6WT9Zq9qzFW2Yv0hbGQLqsFvmWdgzCp2GTPAbUr124p07ssEpeNZKQHeYb-JTkovCkyhVrVmgUdcAJAnrO5cLMaWW8a1vGMLgfoHHxyiHl0I5F2cwQ7OoDyXhyztVJk_YXXfcTZo3avgQHjGTAQAO7Ox34ScjDWcxT2eUCaQ1bxyovv-pb9rq5vfFwtH8BxN8IMyIHamLqjUTtSv0dAKQ0Pvww4ZHWpdfgf3FCNQHppCypY0vL-Wxhp_lT_M815KTFSLUcWVnBRp37yICAfqgsUk2mT0sVFDNQjnW3shDKKcvC84XZEK4U_g3vjgcCBKva-YFO5HOOEiVlChnMtC4uayBayMKSSlOKc535nQYsjp7tMZErkPtspEhvsAhPhJi8KRVPb4D9WssMq2_6QmVEIAPzU7xeSqzwPGQKZ8Sk9CIernbYTksljOpXrputdKsPmZgDTGPqRLrzid9hf-4IvYYs_822_FektG8hTpfgqK5eNjU2JLUjFyEfPaBfR8zdMX69wlwvXIqWnBpsX49nq_7gqHAYpoiE1bYcpgx0ZqmeZL5gP5aHHqWef0iy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌انگیز و نوستالژی از تکنیک برگ ریزون نیمارجونیور در دوران حضورش در بارسلونا. اونقدر خفن بود این پسر ویدیوهاش تموم نمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29968" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29966">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMfU3XygCjkJj45dL4-Ea_J2x3bu8cYkknlGGniyHNrJyqJ2XfKgAvw6KvdYBcyEYiMJUjhf3NTi97eAYIq99GPceLoE6Jg1929a5S4yn8CSJ9lUm_bslJYPGkHWSsl61DdBzfD2BZ9DiT3IG2A3QWRww_K9ZPUD-3VcicjJAFGTjSFVOk0629KOpcqPHFVMr2-k5oRjHF-TjEDQ7IJIKTZvOjOv3X6WuEptYVByp-iShlxbeXxAcsoBw_yuZejxCuUeRgdEmupqT5SkZSPsC27fsDggWPe8YV8SaEEQzUBx6LUDJE9RUJlTIlOVy5-mK2u34axZv_b00nqmC6e3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29966" target="_blank">📅 22:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29965">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4eo1KCfKsCk1E5fHa_zJj_95C-RlFi8A1uu1cR9gCC-gCswVzNPIRcEguqSS8omjW_xaeQZFyo3iTG9Ob7NcUE39qzM9Xzg39GZBUJGYhi7o9HYeyzLFIWH3Tf3vHPFocvSnlXzuSJhWgiEJ-H7UEzsWjbIIB4GpoReknA0iQ3FeaxpuHOb-k_78yQZHnWzQTDe3XJj4H40naWWo822z2gYdhVhT8lujyigkjETLB4r1ysKbFWIDyW2UOFRSQF-3fgof9R0nojW2LWlNv6nlP1LZs-sy_PZtImueETgJzxI-LQ1lTdW6srljbE-k4ZOgpdI-32Xvw7bSulJ8CJi4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک‌تعدادقهرمانی‌ستاره‌هایی‌که‌بیشترین تعداد جام رو در کل دوران حرفه‌ایشون بدست آورده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29965" target="_blank">📅 21:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29964">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSjenrYCA13YGp-fbrlSnlZ3MDOUcax9UmltptS13RWVFA8v6u6whO_ZK_rVi6WzckoHHmh2c5NLDGlhsWc3-s5CYiiaOH5EjNquj8MgOUIt8TSqLl6F2r_ALPt360f9rGOvuvJbAY0VIvVbp-LIr_Q2-ok0f1YBL8RdzJXOi9nogO6a2eeQ9TZZVXkQIv_9M51FLf_Tto3xcjmrYxBF95319B5F6JaBAHpUXvoeIvOK3AB1HkY2RKCMm5jOo6t8T6Y5NpHAmtthlihhZ3DyEB36XKQW1n71ME6x0Z4MQsz8eUP_JySOuLjzNxY_wd9hqcwbsQLl-45pbVq0Vy3VCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29964" target="_blank">📅 21:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29963">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5TmNwdDrPM-6jTAZ6m4BCCk-C7p0gG7Qy2_X76NQLS3CrBQIsas5CuI6WL4qJmS0JUIV_APW6_BxwyhJd0GvDcNBPNu-gcvrBmI6r2dzjWnUJjarstieGq974WtzQfeevYwIRZzqADjRdIOgPsiogXHSNxiMv9Lbo8EWT_cbS2zztXdehdQ6uFhoA_uyQZx2JVfLZrhdFs9-Oz8VDPU_cAT1gjmrXFuWvFD8uuxW82Hm9GU910eNyer7fLBVQzPeaciqD6gNnBOUXKpc5yPjk520IDvvuhur-VVcoDUlCgFwD18cqR90EivKlZn_bKOxUY4MtxVPjqWNcO761TIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضا بیرانوند دروازه‌بان ملی‌پوش تراکتور قبل از اعزام به خدمت از تیم تراکتور آفر تمدید قرار داد سه ساله‌دریافتی‌کرده. درصورتیکه بیرو به‌این آفر پاسخ منفی بدهد بعداز خدمت بازیکن آزاد به حساب خواهد آمد و به هر تیمی که بخواهد میتواند برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29963" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29962">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip_QP6SiAFIVl_NEjkDhhSEsKuQH6WsEuihnVutOK_PlFzOA7bLiKIvSqV2lmLylwM2n0O56EupsPSqmmEpIhc9_8gGzeyQdEyG-DG3seJDc2RYhgAea3ovzZjoNxznbfx8oj19lJFN_V4vL4AGXe-avHX1x5-I5XZIeFLYDOui2_9ozQm9SXZh_2y1uj0v5rmxjoNZMEYBTz1IUtywUw6_EckdHdwxbP6zaZBFZpLq1s0x8Yg_a2MN7zeyf7UC6HxVpoyxOhqOYV5whOt8OSS5jVKle12EPgBNdN0s_cRbje9WF6DPV4ugBc6pmPWY7TNMSXIOpdj1Z3vKsZmq6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛ ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29962" target="_blank">📅 20:50 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
