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
<img src="https://cdn4.telesco.pe/file/G_wCbs8BWU0C2nl5NuCqMlHG9PdTL_uDYsRduZM8alQ550Xe-kUonwghcU2-eh6UDipHFBZsRDKFXeBk0ye8RkW3ArGnSFQ31GAs8anRvJSxRCUYyQsq8y0a3Pf-v12WxXoxur0yveGZ2xUUe4pXy93JfWm-HhSqlCXdRHC5lxLikLLn8jvxcWcRAKtfHeKdN-U3FG1LhTmR0uDRgZ5kXhb7aaIT03Tg1HtY7bigW8hg5tZ34cJgZaqcSvO3WTIFqKOk62w5ZCtDiKU_a_8w1XGJ90N7TK3XKWZZuhs5sXBJ4L7nS5FK9kbVi6dPcheD_wFk-zHroE1V7ftG8pmN7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 181K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 01:16:06</div>
<hr>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3s9Cgh0ZPmZzSVbSmi62KjJ0r2vHDHU3AFi7b2eo53ewWdUkO6vMGykDqT_Sjzs8EPddJ6k1Im_3tOtDdu9uPYJ5AxVqc5dPkQZrNDHogi20fLTtDyf-1E4MPeWCkpb_K4eLEcrYv4ZawBAZdfSuWL1vTd3AVE6seX2A-nal25UgvyD1HYzed7KH-wvUHy6ae72X_nPyGPWC4UACFTm6709FMtwIlXpUqS30b-Hbp548dxo0d_i7ct78mBEXCzOwegEXUSfnRFeB_CgdSQZZ1iIQXVnpQa6cGd5h3dinL87wrWzWhzCWYcOv0wduIaSWaznwXm_YU1gpXv1l8QwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKnLteNg5L9iuYm67FiZpzyIOsbORAnO_-AC_8U6G-GEjC7BunmralIlXbplYs6uPfSpoMlnX-kHqTGXBOq24srDLqoqgtPSxEopMyI_-3QpFMULe50-Hzuo-TjMquBWVutOqILtIHHxuo8VZul3enaCrA2ZM7gIjtHQaDmSh3BWv25OKMPwOPjuUZNoMvI7snvYxT1uXXu0fiy3-v7pLWn2Xh0XtPsBFZmd3dXfFx8VAKIlMJWdObkdeviS7o8of6iaprI0nzs3GEtO28wrsUYJEGp6_ngeKGu5xJV_CFW9tcul37zeeqLTAGwUkZd3BPD4xniWlk_GqYtWoy1r3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22444">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLkDCbaGUO017ZsujiMkyh1Zb3uERJrDGr4FZzfoiu0O1SXeE1XjKPKXz9oRsltie66U8jMfq3qkcnZfGoKNjnjJa0uS3LcoiybVR3WG9-157dVkQfYvb0r0ECMQ1lEKen0oGCRwNhYM81o-Nv6V8K0zbpQTccemVgzCIzuAWcEddkpwNf0O45O8P0FBevwtf_X0E0aaMHo7kTKTHR2f7CMsRbtL0cckf4WaplVaVu7VsB7KJ1UpeirQd_veG7qrETr7UfpluUxmh_BjQDAiSvpExBG5-fDmA9VcUFZDKCY-J-HfLLAfmez5ptObrGHGqJAvYPsbVNP0mGWmrsdUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تاحالابدون‌واریزی‌روی فوتبالها شرط بستی؟!
🎉
500هزارتومن‌بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنهاسایتیکه باعضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/persiana_Soccer/22444" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA2mk9HvN7oyNhScsCeoZj5Sz1SnxZarDAbjvtopEIxlo0zMxSA0HTY8laK1G6EtDrvqbUKpadx_ul8whBxO57D-6EQUfoK-wCfSGLUBFWH0JQ5fOGLZmzoREYYR4jHGecVfghQPX5kGARAFI_YTMqDJNy3ObRLkW1iqapRJNGlsLX6PEfQjvj_ZIQn6HrDMuw9_mRXJuoA6p1ikvSAHVp0jXQDNY-K5W4sgdtR_9vYiCcdW99oId-9jMYU_kuVfqZut7VMl0o_2FzDkwRg0XMzhrvSMYZDlZY0tZAHE62dEP3YCH7Lz2DE_jkyGEvKI-na1sylOYLCsJxSYKtzDIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeCC26haCesUo6rx1Zas6nmmw3EdZ-ziy-LKk1bK6oHY3NL00Ha5hF-wJLfkomDcNY1L9qY4Caze_EN9J6TsMd36VjYK7fLAa1VEp7XbpBgXvSO5cE7GiYsbmFCPhoSaGNJ2d0YFLFWBNgd7F1OD04PGDQN_ZfKzSgRgI4U9srOxrk9_hAPtNgAHaN1eC0WrcNvRx4XMFSnTAaBnyZSXad6KHLSBpnm0r4T7ir7j_O1TDy-W22x9BZxQWApeBQ0bP4dq9S9cW_FVolV6OsHiWFeUo7NYrp0PzpbtJrQwwBTcH0GwBgdD-Emvx7KDxbsgWEsFJv9eam54130rPLr0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFgabF-o-udtLH9D3hIAEO4yW1Y7djEIEtKnUrUnUlV1nLgYmULJ9Ey3OnqItMVsv7PRgF3I4Js2-vB-0i4uvF2HKGiuX5EDRgGyfHarz8Ol-UG84nbneA1cKX2e1zzKkTm00dP-W7dTDIWqM3_3NWdDWmW3P9elQkIxdc8b5e92IUR4Xh2Tua5AziSKXV6XCIKIpiQL9Ak84PUn7bN6GrF4YwbmHyDfp_7rY3TP0F4YsVs2MTttsft9tmJ1GOK2ptzTN-HvVV2ib-uVIyjj-TUPT7Nj5P8NNuyOKnoCk3yHJXAPv-IQBDSK-mz4DEPqQyVQaiJZ6Zzuzulgwc95Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFjgOX9vVHATKSfkTvyOQzgJeWVAoiz9cZkl_Igks6QjMQBVtHV9IOfHdSau8qOptJEtGe8EVZfk_FQz5gDbn_0Rg5Uu_dWdlSF5mkc5w5IC_pgD0S9h-PMDNYndKBeUiPrz6ydsAEA-SySOAibO2LvNA0EOzY8w-8ECBY-4X3nockSD1-eFvadctLOdFqCsJ0k25Qs7pjO3-XmF6ypP5OKl6KgjLybG8J8wbLHjIyAgoC6WXtMFz-okdHVw0wVoVw3anssOoAL7afHA9OH6MxOdBz-4NKv_kSleb1UsxdHK8GILpFGUEcZ5ElF70TKgsEUy6HAJPGb7vuO4xTRMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22440" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwL56U5IWcqFyW4p8Ylt40AHaIEm6VZL2qEspmccFVsuTKojE7K6A_Fq4afrd_2IbQcwGYfUmg_yR-E0oRWHvC7NNH48_ecEQveCLTmrN-jLYeGwHrQrJgESiC3NZJKiYp0tBv3_c5yu6fAhFv3JkbploAioAGzLla5fY29ypzTyAZ4kgrxdwyYGg_wG4-GYkbn0DwKQKU3fsKibbvLU1qakaPf9TfBkffWGEN_-hqGpLeBhrXX1nv9fyrNbnsvykBWvUWsc0Zq2fEli-SjDYKjfeb3wSZO5Webd7Nqf0UOiVvkv05_q9AksSaJbSCnbrRIdMHLNc2p7qfcnyO6rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHWQqevTT1jCmTRzMt7TDYwS36FOj0SxWfjfBy-15x9OkzOHQ16hNUOr3BnBOmh4HmLFgCU9jIaP7fmbiw6AvD-RTf1vzI9trI-PM-6GUYbfToEkOTXJgjr3nv8eUo6JXmYZSqks7VO_GTykXxhCogtcHN-ihi8K9Ev-n-zqH3eozpFrmFi3zxid2IzyG_tkRDBlOu0TV5E95snVtiE2a44pjbhU1xylIuK4Fxmr_Lt8uhjlQbs4HQNiHey82tnCk9-OmTtnekFRU9azuFHEBOoTk9cAn015yDx16ieSgdZkAVnihdfucaKuPgyQplpE0mcmyx0IPn-Qobn9TqF0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
تیم‌امیرقلعه‌نویی مقابل تیم دوم و ناقص گامبیا که در رتبه 116 ام جهان قرار داره سه - یک بازی رو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22437" target="_blank">📅 20:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW77n8e_ZwS-Pb2KuC29uSKvyAu0hp6d2T_VF-qV4f_GrkKtQ-WRAmEOWodb3W4IcI-vHKLLk_gfulvEZmNYZzqh8y3qiOpw4naYUSD6MP17Hhe8w8DCO_bsb5qS79jic_aM0UXWZ5dhHG4f8Iy3U63JvxRTur3T2DzM64vGJG-DQOHrRPi00OWsbLbCl46qT3kZzP4poDx15tXqf0LWkmpeXzajVhG_BjNQEvneUiz6TZxx0rVsETj5hGcXdUaK6JewE3eFaN3QklxR6YCZOXNHJEAcFKTgGYOZRW1JOHIVYiBaF5vcYrSWgVCFgZ_IGRkAjZOb5PaU3sFmsTKwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22434">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sk6t0D7bLwps_wajIZRz29VklLhxHcXWwc6U1oa6cONKUJi2e7AShNWduJUqSOfySMVjSTbYitC1GYfwTbsLfWw-gt73PIYLyfHH0fJC1F0XAHHsTE84fF8-NdG-X1GJM8nIBh8PVkOORt6bgsGHCzWCp2ZXYigFOUweSGYOSE4D4VHge36sKJL_7hmBx8Jhg4ircjFVVsLe8kYR5tWF8TAOREkSL9t0PyaNwlZ-KtFEC6liFTjVelE0JY8xQ31oR6s-uZKvwNtp6EfQmBE24KTI_SITFIAdt--E5Db20ZV-cQFs75kMMTXJZCDjdaFgevCOiZDsyk3uZ9Hc8UE8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان‌بدون‌واریزشرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/22434" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaKsqDwJasLNPJqlVTR4JVElWmdZaJPNZVtfnjNd-iob7xzN3alBy0wrMoDeS7okjDOIsADAlD6DuI79Rsol-6FOG3Aj5giDscYnHxjdC-FtHFBNI1ZTzDPVCv_qsds2embHC-YI8H4e8ll_90v6g92SzACsQXqia4GyaenzIg6KWKonwESyptaatooLzxOJBiNAtr8VNxAlL2YtRMPObyWGVLn-UcmYvs1W6C9bPQSTRUt7ykCkX5dX-X4p5xePzlBqr80hF-L8zz2eqAnrHPj4t5QDKiCCDoqLncF_Aao__NeQWcb15o4736H9yAAEvpcdAqPSJ3xJGCH7yvaZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwjgUcFSFOFPzKQrM-yClfi2ak1tvJKKlytZ-2sRKXnolqtfYnUER90pIhKWVY_VKq6DOAAbq81-_5PcnC_9s6P0Mh4RaV48JCrhUMUo9KOPPEn9k7ULDMpkeWHiGnmeOmF4MxsQTTQFqNvue4T9ahZ0rJlXadqKRIET665V7InUMfaHOTvnoRtRYC2KSqOqaut6agLXCTy5_thAw82b82_rwd0odpBjsHXq7R_iCAg7lg5vuXYcS1HqASo1mQuMt3-75DcXtVFt9U9XZ8G_3T0_0A7PKfDwTjRqn5ft_yg9dY815hyRwg4ddqMmER3dUzmWuSvBcB0Bdyy_g0gCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgBrESRFP9q5GIeTdEOGNqn6sTDoKUlXBqEH0VZejMQocHJv0d740VvfeaH9rIVIDos8IyHIMz4Pw01xWBECT9f6eWkOFYZ57yWZGVNhO32tUJaOpKFXddVdiKXkTmdGOwToTsAGaXVNYbrsStZmHbtA4eONwYyg0A-Hn3AixAj1NlnqddZXK8NygGmcxixmB7TfpN5aU6DP7TlrR3zZuw0fuRmYFLV-KZ32AeQu2RTN3RWhijZzuUZaE876Hex3Bp7FAQ9mkzP7-1t2cxR-c5AjT2GlUtULgYnehh6PoP60QXl2hHxq85PskrX4OCri4fTTufalSnzM9RspGpXNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7qVMwCp7dABu3R1AEFPC0jamSJDVlFOv3f85jGIuhyJrRdViiUOZEyd07rtgmtolfTd0Conm5tWvI_dzYWJbvW4LuymOi-nMgwowgtP59_buWHp5Q_0MdHPhxAPMYZdh1b-JN45zkVjcxbRyx7D2f98Yr8YGRY1lrbjwcTHP9QtwKvXB-tkn9sRSL-aKBW5mH03VoCgzdkJQDjhBIa0En9izrt_JcKnmBJCURVOvF0-Q4dneqZdiyACYsYYKakfU6uZ5f1b0OfwISazKf6SN5TyXecfyXe-eQsEThDRzQTrO1AiOonEkb1j-qJAnmdjf4i3b_58BqrJAWr2V9cLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=T4awkiHBjVC8NnM73lRoh7l7cvNALWjkoRo_NhbB6uK6O8UFk0PfmFM47QBaoQPLNgGkrcsuNLtztOuRcCrVUQgmsBNjCvh06iqhA9DtohZZUrOCtqYeVYYjnk5XoPiyuqNbo57e9qgBKHPk-y2FhCMbRjNXRL2fGL5w4VHa_4jLGO0O80yXSfLU6wlRWpzJyxihssv86D0oHJjY3BZygN_3m_AxQyTKNGSQn_GTQ-gW5xw_YPdtRO8PyucSSW4TLjGg02xcI-CSQfqBwmQiNzSmV2D_IfcSr3NZPfRpdOSrlMoYU27wt6bFFz8X9xG33S6PqhCUoWUJfm2aD-4agQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=T4awkiHBjVC8NnM73lRoh7l7cvNALWjkoRo_NhbB6uK6O8UFk0PfmFM47QBaoQPLNgGkrcsuNLtztOuRcCrVUQgmsBNjCvh06iqhA9DtohZZUrOCtqYeVYYjnk5XoPiyuqNbo57e9qgBKHPk-y2FhCMbRjNXRL2fGL5w4VHa_4jLGO0O80yXSfLU6wlRWpzJyxihssv86D0oHJjY3BZygN_3m_AxQyTKNGSQn_GTQ-gW5xw_YPdtRO8PyucSSW4TLjGg02xcI-CSQfqBwmQiNzSmV2D_IfcSr3NZPfRpdOSrlMoYU27wt6bFFz8X9xG33S6PqhCUoWUJfm2aD-4agQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsNPDERe-6HhVbcImpnQOs86DRNEDnLy4SuB611GEG8j7ibsgyQYHs82tcJpHuuT5mwVEeY0FL4AEt6J_ph93-gH-EjKlxdXswLWdJNUHR-p-z9_IK6kldzTJ30vUQ9cg1uWF9GXJ3IFmJ96NqovIy8KY2glF-kc7LHN6FKxozkE2K_WVbzdxpTla7xxxn-Mwkno2gd1YsQbR_YM7SQR45RflrsgIoW-AMTc0rW1F2IVn46bbNarui6gUDCGzTybBaAeSNd5iv88fylXMAiC4qxKRSrw9RdEzg1_WUN0CydPW7ZgzM-zemwBZ1pMewecQZH-qrrNPzdIHJBlf965Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBrd6wfgM1mT-JfHt986eUr_FekfkunGY1u_F7xMjBR8osUYOWPJDMSfuIx5oWjvY3hvj3Rd5hYlg_g-0GwnbzC8Mhb0smqKnv_9DpM2u6XcdgFh5hd9OzgLiKOvUJ5oQOx-Dd8BEAe_6EiZhb7uru_8Ezh3RfdXiw4oZTJQXRptmdeMiDES_RDguj1-PsLlFRxEQbfch29yhEyQyfzr5krf2nBvIGY13vUFZLiNJF5oj3QbHPcsaQY3zn45dMEkqc2v57bdp5MVdMxM0gcqjryxESajnfmIGountolJchOODcT3ZRVFWeZoEiFhxTIG9poMBCXw6rx8-mew7pEH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=b-jxRSpHuXpM_6SOcY4lfN0HSVsirO6s0Laqsze8X9Ml7tizh9SBFMqwdaAY9SFxnR7knmsvSqirLKRKgSqwxVuvIDX_gkT1EeeUIlUT2NY5FHt4FGSyvcYbXBsKdbkCUPSMLDzoDifOPBTh2LFWv6_X6onPOkP7UJvVlqx3dmQR7TYSKQlFCnlNyn8p216ASugdcucF-yqzJhlVjB8dt9QFyLzu6papcTb7_pKGSwXXDSc33mWlMUgDv-XGdc0g7Qqadh-kqquKZO_wNayFp8FPV8WixdWI5fFn756wzSOHrnfbywXwz7d7YqkRVoUVojrQn3IXb7mOMoweHYq82oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=b-jxRSpHuXpM_6SOcY4lfN0HSVsirO6s0Laqsze8X9Ml7tizh9SBFMqwdaAY9SFxnR7knmsvSqirLKRKgSqwxVuvIDX_gkT1EeeUIlUT2NY5FHt4FGSyvcYbXBsKdbkCUPSMLDzoDifOPBTh2LFWv6_X6onPOkP7UJvVlqx3dmQR7TYSKQlFCnlNyn8p216ASugdcucF-yqzJhlVjB8dt9QFyLzu6papcTb7_pKGSwXXDSc33mWlMUgDv-XGdc0g7Qqadh-kqquKZO_wNayFp8FPV8WixdWI5fFn756wzSOHrnfbywXwz7d7YqkRVoUVojrQn3IXb7mOMoweHYq82oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌که‌باشگاه ماخاچ قلعه روسیه از عملکرد درخشان محمد جواد حسین نژاد ستاره ایرانی خود منتشر کرد. حسین نژاد تنها یک فصل از قراردادش با این باشگاه روسی باقی مانده. درصورت باز شدن پنجره آبی‌ها مدیران این باشگاه تهرانی برای جذب قطعی این‌فوق ستاره 23 ساله اقدام خواهندکرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHkZE4Vrc6Mf2PYFRK260rshwUXmMHerr67CuDAp9XxmBNxFi1wSj4yXvoZhj7BlMcK_GsQ1yZPjl2P_F9hx97hnRJolGGesvOTOjzd8M4KY4kLEQg4jixCQgRYQjb3k64x9AYwIZOCYoYBqrSuhwFu3kS5laJHQsgLP5gIsGTPIamTqEq4OVBdN9BPqPU-l5WLNyndLgTRjBANryUghScM3wc_JXhI7Q5tbEVKcSJ62ixKjM0czp7tOAhxFtfJFGCXSbPJ5Y4w9lhF6O6z-nV0uPTmI9krirrC9esBczy93rMW1vKMFgh47-hmHHd8SAFMgmU88IjrQk6CSQlwDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA2QeNw6AQYtn59xWNq8LZfiFn2I-osK2tHQRtVacn_vgHrBRO8IH4DshTc2N3DrKMDK83XZW8mkPBkJMiH1gH25sp9HAVhFDJi1Wk8sfPyH4enJOMSlARiRfU4h3sUjxxVjElbObBs1B_Z9y4J9kTgbnOvAceGlT5vzh1qISIEPjCFhZbpK__6BfcWL1joUbzwkshfU0bET9pUmDUW0qmbUfxnKlgK5_UAZtPg_DuFhUhShrHrdY5j5fhKCarPjdk2RDflZO_-vNXlht9bLFJln9nsSZCMgjqufcYhqU1-EF3AAPB_iPZzF3sl0Gl7QJwiCpM9ljzqSwuD62wqrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do4m45Yt3X5m91rb3bqMPtd-FgRJjrwmmvppRunJOebxfp_UNyQ3xYV0TBWKtolNwxHtlfdUFvmsmkll00EA9fgPEE7GerBwhS43IVwu68HJSmjoPk9fL0qom0ET3safwaaM8judu67LYnni2RxX6ELaKd1aK3deApB_8T-61R-VGIQU1Vr4pQ54uG1K6okPlswqvR75_EFJq_CIcCF6sR7c0E6csWVWevlxGPjpTaBVrx77cOMO4FR-NBT3fykO6t2V5BD84unfutcFT040lD52KwCkspT_FLZhbk3v1yxtrUZhzQTJtkOFYnuTjhS2BRmhvwATM2jHmeG_cONZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5jpgXcipW6z4Vwg4OAETnl67lundILyPe8hYIcXLj4xOzr6Yj--9avJLLpygv130LfkVej-M3ghLlvZldNSPG1wYHhf_9gu6Su63zIHOS1Qs9kIzyKnSwy7A_5udfme49vEka8tpdBhyvPWWWXCugxeDDrQvgFdWHBN1yvnzrTeeVCFEKUdC2NQ5FrLzZ7JyBlsXT7PGPowTdfhjum8l_JAXchchL0NsEUz0MSNaf2BHOxDcg8dxRs0IpR3vznC6Ur3_xcWyVpF225K8JdIQ1qqqTSUIvl73iBAo75R0CtTYFsGvPdoy3eiYjjvpHj6p1wCcGriGNnEWq2PbRrpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq4b441M34tyELi16tz4F-N3OHz2lzWN-OK3j8ncDJ8TQcA9AzdvkP5ad17YLaxZf7y1KX8EcWswUseL1uqExrWLpSZNfSr5B7SE3E2ItPDK5OtFXpa_KvfkoBWC51lE1e1Brx0lg7VDAf6PRmigpv1um96Sod9JAF_2YJ0evzFHGZu2j5-CzQgErhmqiFf9a8cixPaRUCvnKmDAfUwfnCAJ3Pnkpc-zsuT1I_Rc8R5pgj87uqDUOlVUbpjagr1m7J-yGX0qyGSqNDaKdmLSCHQ_a5ndPTib7DNlLZicy6KUJMjMkyhWRX5ULhgLmd3XykIw41hq-0d-6qquJTCc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uim-hmQB83m5MwaH5enr-yZJVVTh3gmBOfoTUZ_ELE6RcJIE84yFbcwVDj-LKo-fBDSqKEskSiokH2Ed-AqoFO9M3BtrXcDFO7Zt6UNbGO9hnal2EtrnMadc5zUs2W_0Xuc7cTwmTEY6XaZ6uKRSnjymsh24HoKEvksMTEFm9WadL2NEdtNW-EYup4_w88nuMt5LPq_GdrSHQNXx1izO0rlo09L2KyMdb6sMH96_U9mFf3jXLgelIw8g5p8O6X-0bBGDuM1A-ATU5HGgUU2eLVf9D0r4EDEZlgfJmUf18hbCYNcxWaQ0ClVukip-kzBIt-fkXdwLP-rWXpxcxCrgRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgtAnZQPQewlYS7FFL1GShSrdfmWQjinP2edYd-DYOdXRtu6wCYlIZcAR-sVwIoCXUHVuW0IY_6ajftBCy1Jpyztg9xNNaGazXSj8dkCDf3kvoqSWtjGNviBqdCRHW8bGf1gCyD1dnxTdGHiVAJu4dK_gMPq4-H_FQtnccM8khFqfosjcbIWSRudhMoDcjNK92Pv7QLJ6L2cRZxjUxQvmITYKkbGn1mALfJ3LE8dcDgmMTvptgcZ2TzYc-4PYlS_uTiSITLF0oBOGgExHundvl0WvfrIx5ZZ3DssBVHV7weNhmiTDCgpBRAtqdHirA6d9koCOM99XFzsJ5cdLSAblA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljNFJyWM0pA_KOFiVM7wMmB2RupVnoT_pbUuTvBh3_xVheKAuIfcZgz66dmiyhTYGjeaQIAKd3Cc95WLNCTTOCkb5lbE8UfBRRgTFyd2I0jB7H-mylMF-pdtnndffSang8l_0FChZIL0wiqwEN349TBRYv2U-_Ar3TQHZIzDZTwpBkAztdpf01awUTZILFySpXb0uiMJC2ipRALR2_D6M64fUrA2TchvyeScfKjNupCWHmjeN17FDfwKgXDP8tHlzNIIoVvdOwtvL4Hoz_cPdWxpDLJYINDwoJsMsqpI9NruZUdy7eVEe6a0pnDDJGMOIzKX813BOEtL5CRsmHbYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDa0Yf5UX0v33THSh6IcxGgb9JsJkBLvfFQ9EWDS_AQ_mDJcY9Nl0Wq3bD1zlZL60yEccnH6vfjcCv6WoMap4aTUOoNnTq36FQ5Ppmx-l58diD-mqA64s1CLhDgkuivt1LNe9xY6V9VIqGwOhmUk9ecyqfshvXyF2aWtqrqHa8eUyHeQv2C3W0k0BmqwcgUC43hQWBEgx6tLrNwSifACJ3m-FvXOiuWcNzdGkzyd7EzPNemeYLits6wbk9wjbDeZniW7813xelNZUeiKmPb_Y5KKoRivHQ0YBIpJmSrI-sfkKK-CrN23kz6Zbf9wM0-RIKsZYJvjhDc_Judr5UDqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjnxXaREnzy3rjh4eNBjzGlmxUD0klK_iGJIG4yEX1AEOzEKQSofI4Ec3y5ldt-_MS_kHWZZ0CTgcLoh08q-kHoYL6U1vGwXuUseaAHXbGAwudM_FijmkFvlFOsdftokMnfwzhTQhUZTUMBB12jnMLu19mB9hEDkqn1-V3NBNyHUUl8EYyvTFjzmNsck-gv3Ok0xc3nayCGP_Wi8-BeEvNQBaJzNhzMPSBXMrcJqYQEVSytbR8JO1cHD1t0biB9azllrbjsCiyokcf5S-xg2GQaGcvSuoGLTCtvxQZuyzsFFugSORjqQzurtx4j1-Cmgwoc6FwylX-uS_92cNPr7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT7s5HO12TUkbw8DN66cHcPK7snLxGa4KzBkepkYqh2-T4BNL0HtLcwE2Ukkko0MbUR7GIM767U-yjeNZ2fKeCaTRTA-R5ebRcuCin9cHnZygsWlo0kJ8BnYyiQ_pG5fo7xu0EDd03BlVKrMdCMzAsr4QLCzFk51QNwV8P6frgJw2aKCt8xNaslVRk0fEHH1LJkkqydIIryNTDnEP2BXZV162opwPPJ7Q7cjIs3hUHTha9tc4Fz9W2oV9d3QfTm6i7ds7HplSc0sddroTdAk33CmhaXdJiUYswLRXX8TR9cElSFxaF9VmM5zKj5xzWIiEmoZnLbLWmpreww2lD58Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22413">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI7rrWcaQCPrbpOcv8uxyvD35a0wgge0srchUkaEBNlzDKJsIgOnjMxMbVGQJkXgMr7uL7V5zj_PtrsbJDE7oUV1eqSKKsmdd6pY99DxkJMdqz6fBs11RtbpNnld9FRdtVZab0J7SRQ1xFF3TBLMwN2G7QuHuzkGXSGf28cq6O47oHcR7ReKZU9lsmsw9noQbXLrqE9He4KGo9o_QhcKlwv-VH70Lrualm3mqnIcnZc-UQGKzwaB2Jl1t2CIY_dCbZiCxfMRm3WSuiQWt9Os6Krfm02ljPK1vb9blzCjf_u9lTVunKHr3AEcGIh2kfozfqf2jAa-NRMC3zHkhDPuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰ هزارتومان بهت میده
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22413" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfkJXdVRy9CW_JMITsWKbCTqtY4gtIrSamvbO99_QoNZhbg5Sr2yoWrDk0yqYWwACujQVPfg_vSjIAXqCmqcpShXp2u-hBimRKOmMZxxZezCE_Q-wjQxtvMrU2mW0WBxM3SiHPbOj_C3Fms95sPpCRqxxgoLTcyXrqUbDBEfjt5DzftYEVIhZtA7pPqcXtRAB85J-zoyfUrYb9dCSPwVr8skxh5aXutb5RIJyOGvoXojU_OY5YCZtr-Nib7khfcBgxeBicMiYyWUDMYlfOiWsPAdUpfVkULcouxVTFyA7MDKQlx_3T8gUOJeP0mxXk0v-NU0s0hzJ5CO_gjYQI1usA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8AIS2bYKnfldkLbWAKLYGJyUTFh1i6gUyy4nhQK39rgThu8nP88gn1qJ1tUsDk8xQx7q9z2Am03A6eDVE9V5XeCR4BsZ7wKU-0MTR7GJ6GA1Iqa4SKalWWxReOSZNLebZUcoeSQ6v2N77T_bFQZayMgeGFk2SkLqGLO-iFKK7K1Z--ZpTuedAuc2U3w7uEW8KTYMm-DtFpQPExT-rdJCX-R1mDcNdGSUFcwYrE879biflB6BLEkjdpiEPJ6aDtTac5t6Ml7C2orcqi0479AoWUz2v3e5JdEj5Vr1tsQw-XwgBpO9BPs7vHYX0PeZ3_epAFQisvq6XxJ7VeEj3Sl0HC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8AIS2bYKnfldkLbWAKLYGJyUTFh1i6gUyy4nhQK39rgThu8nP88gn1qJ1tUsDk8xQx7q9z2Am03A6eDVE9V5XeCR4BsZ7wKU-0MTR7GJ6GA1Iqa4SKalWWxReOSZNLebZUcoeSQ6v2N77T_bFQZayMgeGFk2SkLqGLO-iFKK7K1Z--ZpTuedAuc2U3w7uEW8KTYMm-DtFpQPExT-rdJCX-R1mDcNdGSUFcwYrE879biflB6BLEkjdpiEPJ6aDtTac5t6Ml7C2orcqi0479AoWUz2v3e5JdEj5Vr1tsQw-XwgBpO9BPs7vHYX0PeZ3_epAFQisvq6XxJ7VeEj3Sl0HC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وویچک شزنی دروازه‌بان 36 ساله و لهستانی تیم بارسلونا، بعد از ۲ پاکت سیگار و مقداری آب...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=YMSQqyL3Mw87ZpN3BdsrkGrOK266ZlqGqHG6DAJ6MW6eQ9WAL9gDcyuGAd1xn-PfgKZnuL5ju5F1jdAM__Y-B90bAbtz9pS5Pfd9c7bwNSYQ-RPCsx5cZVgisuuRzh-k1FoMss5mQFDTehdM4R2RiFIxaBwQ_ROxnR979giLjtZ2-a4lf9ULa1e2_qe5qHs-QAMelsYTMPOCZrCvn5s1EuqM-PBrRaLRN3gRUBNwdYh1nA726509-dEBAAg7zH9ZwYUVoItjZYZ1pMrf_u6bti8eVW0-bUjy7qXPvpmaZYJcFaiRG1gefdixmCqaMsxthC4RGpjoaeG4OidxjL25JjKLoaSBqvKpO_GrAnobHvPzvyJseucT3kbcJ-NwGAVVHZVjLT0zLgKTOXONvg9hvYDsV5SJwwoQ3ww7srDQDEMuRQyHxdaiqp7aCBnzk4a-ub-QROOK8mXRW9rUdykJsDaDWNvx-l6_jF2rOoNMYR4IQBdFOUHi3MRfPKqQFnwegkNunIeJoT7thVRTTB-5W5zv9Q0SwGEVD7HTHnHfjAQGYv8tNrvkB3TO57Um_NtIfKkAbOVk5kLMcc2T9WGmy4w8_DMm7UYN58ZviEYR6s9w2q1gT1LbEJhfUdd2k_DtyJQR2vjjdT02TCJ05iqZNBf4A_EJzLhnP1hNtGNYUUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=YMSQqyL3Mw87ZpN3BdsrkGrOK266ZlqGqHG6DAJ6MW6eQ9WAL9gDcyuGAd1xn-PfgKZnuL5ju5F1jdAM__Y-B90bAbtz9pS5Pfd9c7bwNSYQ-RPCsx5cZVgisuuRzh-k1FoMss5mQFDTehdM4R2RiFIxaBwQ_ROxnR979giLjtZ2-a4lf9ULa1e2_qe5qHs-QAMelsYTMPOCZrCvn5s1EuqM-PBrRaLRN3gRUBNwdYh1nA726509-dEBAAg7zH9ZwYUVoItjZYZ1pMrf_u6bti8eVW0-bUjy7qXPvpmaZYJcFaiRG1gefdixmCqaMsxthC4RGpjoaeG4OidxjL25JjKLoaSBqvKpO_GrAnobHvPzvyJseucT3kbcJ-NwGAVVHZVjLT0zLgKTOXONvg9hvYDsV5SJwwoQ3ww7srDQDEMuRQyHxdaiqp7aCBnzk4a-ub-QROOK8mXRW9rUdykJsDaDWNvx-l6_jF2rOoNMYR4IQBdFOUHi3MRfPKqQFnwegkNunIeJoT7thVRTTB-5W5zv9Q0SwGEVD7HTHnHfjAQGYv8tNrvkB3TO57Um_NtIfKkAbOVk5kLMcc2T9WGmy4w8_DMm7UYN58ZviEYR6s9w2q1gT1LbEJhfUdd2k_DtyJQR2vjjdT02TCJ05iqZNBf4A_EJzLhnP1hNtGNYUUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=mbnTJMDVY06JZOfSPV4hAkochUHlQyMM6LAhymuTE1_S2ffc-D6uWqkJIwi7r4NGBFRs0UOPrNL7sj_aGeeXi7dlVIi86ws9qLXZTPo3avgIn4IHvm6wJmTyNTPfZa47UM0d9z625osLJPPI7PyiLaPt4A3lhaWUeriM09KNcDS3YIjDnRkeS6aKq0p8VJKlqgrAcdKpxbHjJnPsHCtPjY7SeOftHX31oRaVuV78GHpzAeusaATtUf78hRl8TwFsWDQxW2DOHnuRsaJy1DpxSI4otJTn-8lmKru2Rv2n6AhmZrtOBL8vSZtUvBzBAfSgCmkHsMyCUqp0FdZfaS0reA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=mbnTJMDVY06JZOfSPV4hAkochUHlQyMM6LAhymuTE1_S2ffc-D6uWqkJIwi7r4NGBFRs0UOPrNL7sj_aGeeXi7dlVIi86ws9qLXZTPo3avgIn4IHvm6wJmTyNTPfZa47UM0d9z625osLJPPI7PyiLaPt4A3lhaWUeriM09KNcDS3YIjDnRkeS6aKq0p8VJKlqgrAcdKpxbHjJnPsHCtPjY7SeOftHX31oRaVuV78GHpzAeusaATtUf78hRl8TwFsWDQxW2DOHnuRsaJy1DpxSI4otJTn-8lmKru2Rv2n6AhmZrtOBL8vSZtUvBzBAfSgCmkHsMyCUqp0FdZfaS0reA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8j7lcbDamyAitgfrvvBP9Q3EKr45-RO2_0JzvR__h8-xomCbaPfKZUwoQUgiQzvP2RIsRBV3TLocpV2giG9nkfeLT2Yk6UmI2kDcNe491vUyRP8ggBJGoqpGWWOd4NAuBR1tPGWLIjdVh6aQ6MkWndG8wbzujxkDUzhDRsdQ1L4iXNyLMCjbaqUjWZp5FNJx4hYX6xlq8Lfhl_Tnz9R8CXtD1DIC6RM7wp-iIVQ_niY6Uab39PuBmThgPFJFhG9SfBu0XIyF03AGf4uQ4u_ts_qvr4vUcm1boRe16zqKmgwGWOb5LaLSFeZTOuYVTy5iMu_-8qVCaTlHC_OxfhXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkenVoMhc2kYWdwyrl_RXutXeHXMONtj5llGgxOgSHH24y2QUD7rS9WxKXFLEV8fxWIdlSJ-5p1mOILbv9uHrqwRKcSYe7-nME8SC_0HbDDZ_jj36S75gQqrJIDXMFYAxuyfJxh5TkrUEk9AMzDa9iSYQweVarisOKVq4GiF3Z1OE-Nyzf880v-9HdfOA2WIDC17-9GPBDeehTKMn3WTIJxoivROu4peNZvS6NkGd5jJFqw0WsnjvRYFv2-6LkGkNFMyqsRJjxPbRXH2nMJCUX1KPAYZrXBXtEtNWsIFPwE1sBqZ-aArhzamU1sW1vKGMLdvUae4FnUtvP57wo08xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-9CwYve22jzaRCnV2wQBErlUXdbVTsWVCNc7Fxqij-y17B4AhpuBHgxyhT_CF6SrAxp7ytEXDESQA3pXYJFSCPURnnT96q_zWo-MdSDqg4HN2c3XEEGiol35p6HXIW2kNYyCIcfdChB3QP-4Z9D5A9HKLQB-hAYZv1Wcbuboq_M7mK7jL6mPfj5MhX_iPz9gLBDx3YQKl411MPyHI5Ch-7X39oaMwxP_fVSJ9e_TWaWX6D-Et6QD4Q1kfCBhYUS6i9IeXKVW61l5olu7QVUnqVRmAb4J7eshMgB8ZqMHfF67rAx-l1QkRKdDl7hRimPhKrLjb0vfbDlBTWwybRQXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhztGGHv6SLjhBHYcij82yA3MvpwCjeb1lVHdY9HjzmSm59bMV-JLI8yWDBTVOteoQJhzfKrXUEUkjQjcWPm1RH2NDCXxHj1sWj55HeNwj6sWOn4-yVKhZgTApjReW3MZSvTXdXEbfTwDPW9shGu6NlX1fsNNewQdBjS8W6mjecZix-X4RsXJiGO_l_r0L3eaSduvpc9w7EQ_4hAN1j3kflguNWe4D9xef04RwtUf8taiMMYhq6JCfOutd3_pevjI29BqI7Ziu0IiV14jMOukJDTkAFdI1mssAvH1bPMuav0p9lQr1kblGknTaXq5lhxMEnRtn_0DjnWZm7Va8OmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQxHi-Dx-LaI8LOPCciROt2nCSftr6XD1bTv-70iB6z2fmyXCwJny1mOE47-s_Kxch5zBTb7RpWPy93YhlAA4ktvX8VLEKo75FFiybU6EZA4vql3G4UTFfAEGDwNNRzi8LC3HRDxpAX9OHzw3dfLlwiNI4BwzQ3ZKIahRMKKX0LLjRBmU99vAfJ9jS_NoCvKD4HpybwBczBbZozXuWMe0OcSxKjOcnBZKOzEwGg4lKw4SxAjYKhhlIEOELXs-KeebxkdUFNCsQVrfFPToLXGoxCO3Fl1XSEE5djNfYY8JBDW7Z6vIDbUeoKKMO1s3AqZjytfaFD6S8ef6smoJjlWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szKxNwGqVjEI4c3K7xRB5AZQv6FmAsMeYPVXX9hoM4xgDD8-tqw0NGukXgRoeIm-nm7Lj9kHd94_dmRG0GwPMOdQaGGges2p5EtaYA8LpzPzZqf2WgsTcHTQsbhp6z8zG8PjdhiMtUxSSIo09KELnwDcdL50q_n3bIs3aQMFqhFDMTrMsRws1slmDTY8TDIO84hzLXv7p33k7gtYy4Twh24uRi_NuulpF6oSpG33rl5CWM_qmvEsMOaYsHXU_-UZxcHhC0Uj7baBCxasBvSkzgI_RONVWbUwYWLpHqnxABVSa7bBb0KGIr8MYER4WTpjO_tTuOhqvQMFcDs5PouNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN1vRXLNyswqOPY_ibbglom3t7smlGgfASds8ODY6vBCM4Zxo1VzaDDdkR1hZQHsRa_pGWjxZXZhlYS6RC28OfRjNmA7LJma9_JBoi-RVGjagZvemnKPMCQGHi9OfdHabehKyRbuz_1RIFIzKwEyaM-lzVEQzgu5_wh5M2HJZGkvsJjHkP9l8_3ZrZJ7amC5vsIGow6jXUwe0adLqQlIJxXdNJDXScMT_ITJ2iMvIV_bS9ccEWfVeocXR8Ms45fFIAileCdhItqf1qxSNHv8eNhiXETRCE0vPzaTfiLgeFwpTW5dmqpdHbavf5sGKTegRiOcgR6z1aY4-ksWOGqAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL82k6PLSRJYx7YeX58jLfZUXC5fA0cmnwVPrbJovK1Ijla6G_wx4fxCIgQ8eWT5VCLqhCHAqRIwzWyEvXOXqI5Hsqh70dvSyiouCwGCCGASvoH0lH-lIf5YQghI5MbwaMdnk0WMg-AltvChrdCm7jWBH1_ywnEJGmE_Nvsiq4aTK5BtbhbD6rEhU4n8dptpQdjlI4wMPz49qP4MRZ9Qu9YuR-BRc0-Ufke32nCPQhRtnUjkHlmqgC-6eZljSEwbwhu_zQ5uhbGdIObUS7R6fZsSf-fzEla5-JEtCAAIK4enQV0W523coTxEaBfmZI21Q1abURsiFg7A2GUreJOfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsddZgjlxgY7SClA9aIq8kxpc62y3CnizHu5AWJ2ir7zoad0PupNU8cex4cebYVv6fqRPs4kqhs66DUOU8O0q1hQJyM32XsO1cRSA0M8EE63wkWQy9B2X-BfFtvTHZWENfqaiJFxSDiM7UnlWkt9JwV7ePKtTgQRUlLgwVLPfP5r1c8j5vlRqxxVPY11q5-EdHObTa2sARWyCSpWBD1f_HMYlTZH3AcUIuTluEQiPKeA2uannOSwm9kBBwSYTl4BXTXR4zgenFhWUAn_TrFU9mNIBIJJ14a8zrYBZ3yQWvtkIukuf94-fKQX0m_E5lHi9-82M2Jt5XxhJ8frj90Wgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=ZmTzx2sW265DSXXM_0JjIveVu0YxZWz-f2cZQnBpbYP_u5UPVV8aaW5LWAGym8GiP-4SOmw2vKTyhBjriH-NNvwUcSfr36AIlja19V5gnWXGAdoxLYPts9QXhf4L6ovJfbkuZSK3lXKNkfLinbSXAluQ3xNnTlLiL7qRH33j0RrropO6DE6ZKWoZturuy2oJnc5HKe8b3ynLlOkUj0ikJvdhVW8saT4CeLORJL1IgDNFpu7_pbuxG4c9wI0LkybW4d-b0yKbHhQAU4DVP0ADDA5ptwMPzjQR6CYt3lAOC22q_KwVAYBCzxxXwezCndAPOc1Zgsd43xmKpDJop6TSew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=ZmTzx2sW265DSXXM_0JjIveVu0YxZWz-f2cZQnBpbYP_u5UPVV8aaW5LWAGym8GiP-4SOmw2vKTyhBjriH-NNvwUcSfr36AIlja19V5gnWXGAdoxLYPts9QXhf4L6ovJfbkuZSK3lXKNkfLinbSXAluQ3xNnTlLiL7qRH33j0RrropO6DE6ZKWoZturuy2oJnc5HKe8b3ynLlOkUj0ikJvdhVW8saT4CeLORJL1IgDNFpu7_pbuxG4c9wI0LkybW4d-b0yKbHhQAU4DVP0ADDA5ptwMPzjQR6CYt3lAOC22q_KwVAYBCzxxXwezCndAPOc1Zgsd43xmKpDJop6TSew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz3ss6ulW24k6tNogVv6Rwi9kIYWisBb461lPRr2VPAzfY6sKHi-mVx0QLIYl15fEfA4i-i0n5sLBXx3KBZS35JSLrG7Hp9xcLSmezmE84A2VT0CXMAuJwrQL2xh928pJq5afAgjBbKmscT3geItSRc-KAXmBh1bJ6y6a3SBZCjDbl9s1QO5Ou2cCwr_VzBrjrIldr0toQerkErZHiJ99fYABP95-Cvr0RIG71EEz1MYNfF2usU7s5JpY8zsrBuF1I_9QCfE-khEYvR0EW9GS5NCbi7emkwtf86YBiZuJv1M5Bcgixe2KX_k5Covg7dKSirvXonTzkVNYnhBRNR2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=GAzDFA5tnYv0lDgLxqNE0D-tB5OlXm_E_mOdOuaMFrz67o_lS4PWF3IA98_8CO-waWq_ZYWAFrmqjIUp0AGnGpGt9wkgMmCNAvu11CiWqB8FB-Jx4qfFjkN-Hs8oABaHplCvQGlcrtH2-aWJaAV66v88TlxZeOGwuZynkLeDxdCaJi2b_zUQad0b-O1o-RM0YrbOPrH1mREK3BfigHvrtX8W39svJV4IH-RNyHDUKur87Kx_9-oV5_cgp7lgioTuBc2gkHUtZKA4sNxdMk18Bx7Mbg2Faiduj_91_1QrRRQfKYNfEotKhhrJibp1iYCqd4st9avnI6gzqvz0Cuy-1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=GAzDFA5tnYv0lDgLxqNE0D-tB5OlXm_E_mOdOuaMFrz67o_lS4PWF3IA98_8CO-waWq_ZYWAFrmqjIUp0AGnGpGt9wkgMmCNAvu11CiWqB8FB-Jx4qfFjkN-Hs8oABaHplCvQGlcrtH2-aWJaAV66v88TlxZeOGwuZynkLeDxdCaJi2b_zUQad0b-O1o-RM0YrbOPrH1mREK3BfigHvrtX8W39svJV4IH-RNyHDUKur87Kx_9-oV5_cgp7lgioTuBc2gkHUtZKA4sNxdMk18Bx7Mbg2Faiduj_91_1QrRRQfKYNfEotKhhrJibp1iYCqd4st9avnI6gzqvz0Cuy-1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=piZlHNXhqrFf1G0MJeVLYj-I6zA6G3C6llBQiLOJHF14eGSZxLFq_TJfcZvm-qE2-dZ9xkYVzINhVeG-CrUqLx3xn1q8fg4vskY6hphKTt0XK9C1Ek7mT3zB_XR10UqA5EStYD1tQLg6yfjuU7TqbXvuq2kFqUoDsrA1tE1cSVzQJhi00iR2tk8kqickhi__Iim1cVVeaMb4k98VtBVLuU2TA2WjX3pjAkthYBnWWYJbJHH25lO6mqpBAsALqa0m1r2Q3yj2nOCMrhh7nAgg8zznrDIzRrgRLgtLBm0D9uWLU5qKMwT_JxIwRh-4StgI4hIPSNPhRbhaPxfPMhPWI4Oyx9CNpoMowsIw5SIkMX55XskdwpmKAcHDi7PTnAwfBrASFCgIAOLh_hqMfAMyQMhKs296lQinSHtth-0sokOlS0C1wrbHYoQa9L1vw3dpZBAFHevsjdVM5Wiv-TfyHA1I42awOsakNZCcgtN9ylhQ3pnCIKuOzvYBzhfgmOIrUp1c0LDW4ryQqDYMPmIyT-hZxkJqJVaznI_vJVIoa18Y5SxyMdjixoF2zytNqUyPrhHOsdNA7ApAGiokkMdWNKtVnma4XGd427YByjwszbuNxYNBjmKsZd1QmB2NNUm-KbNZED1phM6-5klwpdRLvbmHiFFarUeq-pSDzLawQsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=piZlHNXhqrFf1G0MJeVLYj-I6zA6G3C6llBQiLOJHF14eGSZxLFq_TJfcZvm-qE2-dZ9xkYVzINhVeG-CrUqLx3xn1q8fg4vskY6hphKTt0XK9C1Ek7mT3zB_XR10UqA5EStYD1tQLg6yfjuU7TqbXvuq2kFqUoDsrA1tE1cSVzQJhi00iR2tk8kqickhi__Iim1cVVeaMb4k98VtBVLuU2TA2WjX3pjAkthYBnWWYJbJHH25lO6mqpBAsALqa0m1r2Q3yj2nOCMrhh7nAgg8zznrDIzRrgRLgtLBm0D9uWLU5qKMwT_JxIwRh-4StgI4hIPSNPhRbhaPxfPMhPWI4Oyx9CNpoMowsIw5SIkMX55XskdwpmKAcHDi7PTnAwfBrASFCgIAOLh_hqMfAMyQMhKs296lQinSHtth-0sokOlS0C1wrbHYoQa9L1vw3dpZBAFHevsjdVM5Wiv-TfyHA1I42awOsakNZCcgtN9ylhQ3pnCIKuOzvYBzhfgmOIrUp1c0LDW4ryQqDYMPmIyT-hZxkJqJVaznI_vJVIoa18Y5SxyMdjixoF2zytNqUyPrhHOsdNA7ApAGiokkMdWNKtVnma4XGd427YByjwszbuNxYNBjmKsZd1QmB2NNUm-KbNZED1phM6-5klwpdRLvbmHiFFarUeq-pSDzLawQsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtIE5eZ9T7meU-78LaU0WlYrIgn6-eff2vgxu8Z6c0maIIZfGDLq97eoG78qbp9KFEhvgRe5FbDgJrQ_jyZK5q_7QmOK7COx9pDngYNR8YsQZmfuKOgQ_Ad75qjwBmrdMnsqaO3AGVkOU68EqnjYl0L69n2Wkv8yLEbziSDKtYi70U0shyW5TMGakjtGqJG7V2URcB0loucPXzfor7FJmtdALWAOY4cb0bAZBs_HBq0rx4Nc9PTVCZc4ePKxz9fLEmDDweCyVBnt1TmuK-R3NqqXwCJ9zgimjL9ddtUfSybwADQXu5o3G81QCrJXrPmBddgU2kRpg3-STMZLlL3O5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv1k3IdUzH4XsokPA_7g5CgkXpNNjV3rtixd0_Gsx3KeRtU_3P5RbukpB1pEIZ2di-ZHJN-V5NqelbXP_XovGb443C6pED5_zjNVJpwng7HVBDg6S113LJ87OWJtZPc7yRULl4MB165TTadgvPEtJd15lOX_jYN7U20gpw4TuioXspCeC1kQZtfus4uFgrtkuPrlymoMgDuz4LSZYkFisyd8Bw9GO9QA79ZvH8n-SwUFxPV90crA2RTrhO3KrHkYxRB6k-nbJ9o0kdRULSiaM160pLBPmpt2CoZxSXLgv8pBdH_T-5vkF0UcgfzwauRXRotj6vAD2NN8kG5xYTAgJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvUJGo370wH97KeZF3iMZUnTKbPiHYJUpY9Qcch7G8_VSKthpdd0GpKhWXygW4691TFTK1i4nJYPgSZ5_Ruc7hAnbAn4d0pgeUcnWaAGh-lKPyeJZO78O3N34X4NKTYnMWoGYzqawLM0OUvJcDFaWVpHXsr-IwxAXuW9-C7jkpQEx28rxiDu6tWlkGj0RBHMQsLdcMArgi8eM9w-cNU6wCz8oFK7H_C_9AuLO6dOOljwaoljoNoIg_ef2DG78Idtg1DGTQdd_7Nz-QJ-92ybnHBraMCeOjA8Nfc40CSuFdlp96GIZ3f_b226Accgt1Brh-6di0MHicLMpYKF54utlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmAzViG3FnmdMxpe1MCW2KcobOHbJ4JnxPCXPXYzcip7Py1syqjDaAUYM0CF_GmIaXlWE52oF44UJQsl42Zq4hcq7Vp-K44xDnvYJ6N-ZrqHDggy1dekfAJ6JgIti7UzElX94UBvPCqCLCRIpIxhXt-uREYOShaBkkL2M7QgUOO9rdanbRRfzMajoqar0onM9N5G0QUaiQm4MRgvctHn0hC9TD90DcD6tgz8QHCJEQY1l-9BdY7SYR_kgvi9-kRLZWy5LfDYVxkua0e6iK6IeKy2hCPBPAdX_gZQC8dZXffxT5wThUHWicULRTQXa390MSnqPuPGdVByL0AQIvVDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APFaPjQmi_TdoTixp8FkKfbY_lz7DxPXWU98Ud2aYmxntE-bh2LCuNzknCwh9xLg9yhZwLq2j2tQcw85FW0--1l-_Q_8ANewKoxH_T0EUD4JRZEOoEOgyRUQdYchPe2cE3vH-Q1uYF7aFhMSeceYOgJHU_5YN9emjAYXrZMXQV-aUETe2TRrfWl5Kj2qm51hzVkxFmTRSNWGCWvGQPUSklhhqSNKlWf_z2NzvcMTZHeTl4vMxKBcN-seUl7lhiFzaxSBnuQAtb8p5O_nn9FTyp7veue5Iitr4-9gzl2K8JEM42ytaP7ydKJxk30pmB18H4IUB-neYMdSl-sovKkmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtHy3j8AcQ78btrmy0X-EudTiK-vtDQWjpvrntn5Uxi-zNQp2MocLqTHtJqSMAiSUv8uACMVfj6ViH5hVghJC3f_a6XLQj2lPqGWgE6Kwg9bCedLNHtAqbdgi7dLqz_jGl_lszCcGzI1Fni2vrusJtY_NNI0Q2Lch3YuWsWHDjI8lcX8qvzasOfqUItEVxNlKtiiW6Nhk4fb_Cq4QBqGiiNSwUqWRFiV52WbqRhdFjkMidBWSzRFsukkUd0yZNHomE-BHusL-s2WOmDvOwlSlTCX0BwFyJvkm8FNsKN7HbCvW0n2WaSMlWrZz-qA6Ce-DFJzqy0vabF0kcdxMhlglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=sQV_0xIFiKvHbN27vrEs0-24UFMG-BRMxRJSe9d7jlE84KBuNMTG3oLK2nHB6HCIMjDuW0eUeRHJEYmZmL_t-iDkO5hf6G3QBdO8IAZCTuiGtGVKolALfZrV4T0Xr27ubk5Un_THMnPoQVyPd2B8-qkexOvrwbbjuqCCc9l7zX0Hi61P2OcXS6CTAHYs4_arOgTJNX_7iIfZXuQvTZf0eLSkdylwEPR_2y18tfsYeZeGFlqCd3C2FoEe9PB0rV66Npa_xueNDHfcA39-e0KxeiMWCK4mox-AemxLtHWib0UIzNzad5_F2STOQwmu_WfO_jknMdfFBsCtWN76BnKCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=sQV_0xIFiKvHbN27vrEs0-24UFMG-BRMxRJSe9d7jlE84KBuNMTG3oLK2nHB6HCIMjDuW0eUeRHJEYmZmL_t-iDkO5hf6G3QBdO8IAZCTuiGtGVKolALfZrV4T0Xr27ubk5Un_THMnPoQVyPd2B8-qkexOvrwbbjuqCCc9l7zX0Hi61P2OcXS6CTAHYs4_arOgTJNX_7iIfZXuQvTZf0eLSkdylwEPR_2y18tfsYeZeGFlqCd3C2FoEe9PB0rV66Npa_xueNDHfcA39-e0KxeiMWCK4mox-AemxLtHWib0UIzNzad5_F2STOQwmu_WfO_jknMdfFBsCtWN76BnKCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=YTlE1QUJrZe4HE2HeRuD15SSayciz9ZE24uPTryTm41je9375Op4wX1s8llMFLQce5BhCZAtLYcgsSdw803waa_UY5x9CFtyTokmT0-1rWhvxffAirtf-kklhbNLNQSirzwjLbsFB6mjGISRIAThCgLnH8OhvIkIDNPR5Fa6oy_ve_8TzMn-UhbdFLW8YRCGID1L-AvAzNMm0lr1A7OTRevpHDvThvN0WBrevmLANUgWEYDjLu6YGKWo26wj3h2RMvmS9dN0hXRDJj4DH31YE5CpArkT0ggNHb_BzewBGdJ8HPYyj20cAVPr3Dbo6d1YZwqp73gge66gEu9JSPfCeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=YTlE1QUJrZe4HE2HeRuD15SSayciz9ZE24uPTryTm41je9375Op4wX1s8llMFLQce5BhCZAtLYcgsSdw803waa_UY5x9CFtyTokmT0-1rWhvxffAirtf-kklhbNLNQSirzwjLbsFB6mjGISRIAThCgLnH8OhvIkIDNPR5Fa6oy_ve_8TzMn-UhbdFLW8YRCGID1L-AvAzNMm0lr1A7OTRevpHDvThvN0WBrevmLANUgWEYDjLu6YGKWo26wj3h2RMvmS9dN0hXRDJj4DH31YE5CpArkT0ggNHb_BzewBGdJ8HPYyj20cAVPr3Dbo6d1YZwqp73gge66gEu9JSPfCeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce6G1U3kk6gObw6EDLOmpBhySy_Rdcm80Mip7YTgfnVSOxWHAxpdmVUE14gO7HiNE6HTC3I7edcDH1NPiHgDJ4ZVzP4fq1VCuqcdVdyvvIGoRat8z3lrWAyWvvMeSgqi8YYgK1nSlYyQoWIi-5MfBMI1_gHku76TWZ2Sbu7oGi5zXo_JSVsYYGPttpS9AfMCjEWRS3HY5KhK4FEHE7d5wlFF1mAaKpOLRqznrVncvDmipRSrDaTxQ9EoMNIW_kiCN37OOKPQR7dn5ClhLhgclL4NqpNTcomm0QTW0A-7MPs6rVBCZEoRVJW7KvfUxur_37RJ2y7tkdS3QcIJPjJnhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLXLSFuTleKcAT4jEh-OlmfEZwVPLOjrky-tUZXls7kYTM6TtuxpPcOXKTkBxiiOGzasqsbUysjD4K-2S6TTg9aYNfPeKmcHTBEtzsR7TcZKrv2K3ImK9wx9L2YBfbVrc8mIdwyInN6-ptRYvhK-DZ5ES567wxyt2oDSwBrB86ZT6up11YQzk4zqDmCMXFsxYa9JIODj0dj8wqLFI-SA3cANzRQ5YSBN1zojQgffKJaQK7lQHolvIjDTpnZRuENj5-hGeRQwgXriNr6Xw7ZmOhwId-uUALSlDCnMNRi1blT3NU8_XKDwosGq9B7EbwABXE6pn0ThemT0nEjjFZfoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZapYebBNxdnatBNJoMfjOySnnhlj_EHoIl9UH1LHnhoejathrMCx9P7icgujmAZN9WytPiqf93R1IvtaaX4RvzgzL95Ll6L_VSyp8JVgtuxfnflQ3iaoKFPf1IEbKJHeIcDT7qX8EgpFNOxGu5VpolbKbcTSgN8HrNKgmOtnPxcvXEt6vvcacgLc_yRRmvQOpSYs1z1F_umeDXZDKA83OD_9hpuCZTLXFXX0Z47UnSCiOiG0jXyIdaD8J_R05wZmROIxX6A7ODG2mGRaK8HMHE5BA5mg-XTIZoGwJph072wtBBJDt9hqnRO8Lwnj1N52huUb9oJ7VE4h1HFkQrTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gErH5fvbAYRUPl6mlRYwejRUEN3wK3A8rXWAxuiYK-_SfikTM6txof_P9CL1SDh3jYRs1kmbTvqAla-wo8UdRoAVrfwuBeA9USD9EFehP-VZ_BWWclVs-_Rklm2t4Te77Pq01Iw1Eb0X4erGAm6y5OT15Vu7Vhku6I38i3xo4xqw4z0XZPMnApJp9-iX9gbYgDKEGMA-9pCpOQ23XI6HTv8huTXViDOHMs5zXrJtMuzbeuLZz6Kp-ogig0HHrJBCZrETzLkTsErGt4GfD7XCrODQXYLtoUdCcyjuUWDdxpboW_7jLUQgbdk7vM-eKOYGQN_i1Z58qx-YNPQetB_CRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVKkCpSAWr_fa3kTag2JgCXCKxvA_EtMJLwi4NhDYug7wVecizRCI7l7yhpt3osD_sPf-2-99x7apmpnLJ95U5NhCicN8OU-dKl-PLqCnCYj10O0rbwUTN2Q09tBmFyNKalkCLiYFFxf-ZWlrYDlfNN8uMZxkZD1FXh0m_eTo8tlvgLHu2zAsQ3Fg7Am6_wsXZ9eJ4o5lr-ygouQsA4FUBY9p8UuMXGK_wg-WSXSK9590FVXX8ie9lZihfLuRo8I0E8DS3A8b3XzNWgSaun4rv5fH5dzHI5UG_0xV0C3wLwUgJTEfl4c4B94uRnXv7lLZ6ok-EAhDmPHL1eWwSsSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=brf3hRFwDFai2s-hbigQpOh8NnXt6nVY0x9cWu81jUmtXvkqmI8KmMgKfzh10yz05jlIEn1PYb-L1ycXxuMXy9oscF03YkEsgo7NpzVQQCeOeNmKQMIT2eWJvUA5f_9UVmdhGBnIvtagRbIk49MqeILTMrYEFbe9oJDnaGOXVTvvIOCG2BAdui-01lxSgHnyU_8WiWQ_4xkYo4-pvg88ZS2Yl95IU1mP0ksJ---lzAweDSS_6L5oxalLyWSCmkmEFPjw2YAzUkvHXKP5U9p722mdmsQHD9_zZKUHKO9JH5e0t1uk3VgTo6a5mfm2Xki8IXSh5CTSek6x4Mn0nSiI0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=brf3hRFwDFai2s-hbigQpOh8NnXt6nVY0x9cWu81jUmtXvkqmI8KmMgKfzh10yz05jlIEn1PYb-L1ycXxuMXy9oscF03YkEsgo7NpzVQQCeOeNmKQMIT2eWJvUA5f_9UVmdhGBnIvtagRbIk49MqeILTMrYEFbe9oJDnaGOXVTvvIOCG2BAdui-01lxSgHnyU_8WiWQ_4xkYo4-pvg88ZS2Yl95IU1mP0ksJ---lzAweDSS_6L5oxalLyWSCmkmEFPjw2YAzUkvHXKP5U9p722mdmsQHD9_zZKUHKO9JH5e0t1uk3VgTo6a5mfm2Xki8IXSh5CTSek6x4Mn0nSiI0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFNaubRfDNIWI48jwfMk-32z0YZllFJubPDHKpaxlVH-APsWuIE_zridwo5Zi_OIxkDj2A2zoNXqTqaUvQ0Ud9LzVESrw_RVpWubDNHKOPuLc5zw_jkkD5Z8bZz9K3r-OH7YApKp6kyhhwYFN0JqN9Rmxm0Igd6uKRjG_jrBj8g9ufjWpuVM2EPfyRzWqGt208gfOnoZV2sKdDMWg-cL_MUpOoUEXT5oBRN7rQy3HdqqRqIMdznJzmLqyY61aEt5aMrliZXZeCSgg-H_YFiQy45m8dSoOkQv_X4dqHwxIT_ep4XVRuMoxHqDw9SmzO6yamzR9EK1DNzKc8UaqrE7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPbOlam_yrhWUmH9lvhuG3ogioWGwKi8_384OEXk3dFnLeFndx1WZYUVLJVKNasuT9qixrKhIACsAUWHAI_rXFEiZMsKFriPE9qe6kDMSmx5rhzBYGjRU1kgtEpJF39uUefr-ivpR-Um7F9G9CnmubvhhLAOb9ItSFgcPjpZtwHz4LERt7Vv9TV5qpGzP2jV-nnzP-dIU9Jp5UYqU8L_iuSZjnEE15DPBsmZNfS3z_XU5X8VBDe0fQ21S-5EoVjaM21hIm1AAnAJHowSkNBjr8EHB-jKpTu6x1oijVJOH3YiXsx9GTXMQyddCn42ehkb6Ml0OCljK3a5CrTvSU2MQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzgCOooFyv6JTYWz8fQbUkLBhbP6cH-5a9f4EA1HwzYewYhTM_p3y_fzxOlMmQ8ENBehbdUKilNYvM9KbsVv0ZoeYtYjlHC1GD-HI8LBCxiMbtf79EDVUHNbzJR9NoEI1MduA9GFPqvDi3JtW4_QAbrk2e2XYJN0Y1ODswfCp1zeOFH4rZxD7Xtz9QM1zD9yrZuxiM3LhmTv9nDqU8XtDy4cGAtSlbanV8Gp6TH5VvCIF8XeDbJbsSGtk0K6-r4yV6U5-N6w_96peJoGp84iO6hjP7FE8hMmf-lHf3yHfwYyKOa_duSk7bOfRp87eCdezAnA4kMJbXa-TfvdJmtKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud_8CGr-DNOwBBB7qVKJuvhB25FQNAZykHk0NwW60TcKWMgcfG2J_jOEeWK3IPKVGuGwYt42AZoXLy2e_DfNseCUt729wwIRbEBK3kvlv56--GshBhCHetL7iJgegtHP_dET5n_QQnLdW2kwChkO_GQRyJh6cywg357SZSjE7uytzNKJO9xTiyVwbm4jg5hND5vBMUnQ-RxqDIpYuCB4BcFxpNbUDUWE7mHE6tmd5jkeqYS9RB9CFEHTQb7UoQtjGMLt59LE6KCuK3h8v-hOc2eMzZQXQ2rVyIqGJOwgfX36Atp6iad8AlqWRHO_6pGRT5gA1WTHJvw9_6_Ae9kr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=Vf9BjU7Vg4AdiaZwoCRPqZSbdwsWJ0eosFhN_qgcZ6KZ2DPAd8NUB3btn0eFzOl27AIL1_IRGlHBr54MzF8amtNmh9gTGbxM45YxBSOeUOLQnhb4CxWCIspcrOkSoOD1aUT9zcNiQUcxJnsEPuN2RJOfKOKj3zv-8JwzrzGNTjue8JrNgXgGI3276saGRAXFWXdRUNQQcAvRMRFmyQVT-6mRZXETYgu0nyA1TxZVGZbm317a0ILYRQdUYj3cL0tXOC1QqG3nz9ZrEWGxbfpTY2ovw2sUUpu54JFUATloJkjq47ihWQeerm2BJFFMtsB0t60VxjKbm6MAPB5OvblVdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=Vf9BjU7Vg4AdiaZwoCRPqZSbdwsWJ0eosFhN_qgcZ6KZ2DPAd8NUB3btn0eFzOl27AIL1_IRGlHBr54MzF8amtNmh9gTGbxM45YxBSOeUOLQnhb4CxWCIspcrOkSoOD1aUT9zcNiQUcxJnsEPuN2RJOfKOKj3zv-8JwzrzGNTjue8JrNgXgGI3276saGRAXFWXdRUNQQcAvRMRFmyQVT-6mRZXETYgu0nyA1TxZVGZbm317a0ILYRQdUYj3cL0tXOC1QqG3nz9ZrEWGxbfpTY2ovw2sUUpu54JFUATloJkjq47ihWQeerm2BJFFMtsB0t60VxjKbm6MAPB5OvblVdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFT8YuGbuenq_d4oHZaDC1w1mEaYmNPgr8pRtXfHj8QrsQt5NaOBCHNzkNgy2nDHcPNdC-sip2fDNd0MkftN35NWJFss5IQlOCO6rzKfeJLEhT06UQtBvs1Kink0e3NrVo-GgM2n5VCtyqB86wM7r-YwY_B5enV-AGbavH65GVdaUO8f3tOXCdk1clBUYkaZ5P98QieJOM2K9lVIKC56XtHThnQ-f_SaMlMn3hayIyS0BEU4dq4gfMW5Db525srtzkQaHK1vqGsfXoHXgttWeGJJDVf6ZB0mVLx7jjcvUrpqxQdDqQVwpGOhMWrwrL3ur5j_lZugDJ13EAm7yCfGeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXdEYr9qDOeFLNqnIIrmQ7BcC2m2cQC3JdILHB9pzHNFqaeRdSBGVb3Jn-UrScc2GK7nsxtwgej2j5gP6yw3t_O0wrHkpQwuoz4CjvrCxlVWUFVXntSvf51sv3mUvDhyCf1ioEYYlLpLN4bWaGNyWsXF4mUrmjuxSd_kGGQ3uoUKOCnkYzleoxV6GXHuLEAbEx7sMAPmDaPOsnZ84GCmLphbqeCgFDp-xdfFF9A4IA7lPYGBk9d6wbSQvG1mDYovEFG2Wiz9TVhO4fsAiopUOoZC5imVKUY0y5a3ZqD02TuLl1ExR8np_tzyizgeoozfBXN1k2ctOrZmM9nHB4_Dmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trrQ8jS2VVZnI0tgeACSP2s7fTsTHNY6G4FbdDXR4XG3EvFHZDgxzuQubRc91jSC1dODtA9jR9eTDQ876UWjzHr9g-gvfmcMV4qUMPed6POK67V1Q0zo-vJ6FHN3C2S45Vv9npvnivkZqaR9adyYKy4pXXXvFyjE6hSngruvbt7Sm2HFf7x49T7rqwf24JXcj8ZFqgrDp3DtTTsoCtrlU_heccpzq5-s7V6ATyAmkwNaWvkDopkKb5gw0e8dm-i2uL2qpA9gXcCHnBVpLha_R4vY4wR3HKXcPVzAZlsXjL78zn6bn1PU_a7M1WKluL7K7NOZoDcwyeWKEf1ln1IZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=HemKgxwU-xq-7wJD6v0TA7ODAh-oB_fdGtm2d8zXNTuBT-fMfNCAQcr8z6ii8HDfzEVgGGfGtRYOQT0_ooGGrXrqh-cZuy8ILEgvImM_jhEDItU--yKrZoH_2zTgSrKLzaJbWvnCv8Heni-2D-kmYsF-MJLNM3io932Z2DUxyZMuTTAIwS2BL62j1ZgRs86J-XLEo5BykP9oUJYk2p3cki3JhLwN1WJ6gqYL2L3c3c4Drt5irfIpRCDA-7w1dmbOJ0mrZNtOjOA3raou_2FqMhfl8ovamvBdpGz8P8BV6ZI4mS3JhzkYIW2PzUtrYkOFCqIUHCJFW-0iAGnVpD686w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=HemKgxwU-xq-7wJD6v0TA7ODAh-oB_fdGtm2d8zXNTuBT-fMfNCAQcr8z6ii8HDfzEVgGGfGtRYOQT0_ooGGrXrqh-cZuy8ILEgvImM_jhEDItU--yKrZoH_2zTgSrKLzaJbWvnCv8Heni-2D-kmYsF-MJLNM3io932Z2DUxyZMuTTAIwS2BL62j1ZgRs86J-XLEo5BykP9oUJYk2p3cki3JhLwN1WJ6gqYL2L3c3c4Drt5irfIpRCDA-7w1dmbOJ0mrZNtOjOA3raou_2FqMhfl8ovamvBdpGz8P8BV6ZI4mS3JhzkYIW2PzUtrYkOFCqIUHCJFW-0iAGnVpD686w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG_iRPmWUtvKO6cvIVnC8ju6dibzs4_7_zcKs_JLprml5bESTLo8117uPms4pIFi_JpyVcpL7wbXgXOxuHJ-spg7lVzzNFIjd1y1P84SatYqcAoyLL2z2FtndwaoUPL0oXZOnqz-wEc1lZDwcOlLlzSBEicFUuH4vXVS2AfTyn3vCpuZT_LGVvh5YE1oqA_9Da-_uPt1XBnJY5LatRqVMQ75J0EpXfVAXtRB2vSfV1T-KYBAxJA4ZL_iaGEaZvrHGqRJ4pKYBgKg1s7SgGBQUFdzbgNWRfgoIm3alFxXfKINoe7nXvxrvV8ldJLT6ZotMdp-BG240jjQSBYRZ8lV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0muWD-yeFbXYoH403QjvFEzaWSrY7WLHJcWAJODycIoA1kVB0vHUzAIpXmu8HBWjPfUT2oRaTr6ZyYdQnXfMPqh-uc3kG7n85zXU31duPJoLjWygoi8TMn3GYS1ZsnguJ8KHVwmXQURM8av1qc71hsDkN2fWWaJBrRjmz1-Z4ckonxeONOjAd4jFHn5Tv_Ssxf82y4UJpaHs5fGD-8TlMYP4FTFWt5qds0JTx7Jo4qjDGrf8HavH5aybbDDkFR1KraqjnBYIA8TandPmPUB94-MlrMCmeR_qBajPj_zzyygdyoTjy6g0LmjyirviOxjQDGqURayGvvQ9jMwVbwDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prK6-1HDmbzUPQjojNtxOt4ZVVb07ByQBaWap87z2Z9rQSkljd6ZA7g7N41zgLrsq2FGeMaHA2_K29OC83EzX433fpxCu0wlQ0SF3zziICN_6X1kdJ9tldhNhXlFrq166s362Q2jYYNNgKCafvfB00vUcsxSwpCCgfq7u9mOx4hfclLEeIKDBq414BYilcID7qGkrMuekMkNQPVi-fHWZG3yavrQ3OmIUUn6e_TOb-Qdcrk32PqXo-IU0IC4-NSYU7e7rwDWotrsCeFQbrkc9i7yUM2z07wONaScLPH5i0xjiGcc6idlykchnJ72ityeX-knR4f2taAzH9aRBgd2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJv0t6LFYk0cw9GpgF4YVKLSUlJahK9pcmDTBsf70NBRFr6WCju0kbhyYc0uBqXL2Tbf-Pzxkc95ezzyVpednuSECRx_g0RLprhacJBRaWDs2c3ghdcjPznflEI-lzQAD0CGOYrIDHdRoUafb0j0y3MZ14uhZ84PmhJMLPLv6p0Vh00Kqj58II1aklaDl3HKHJubk6UF5trIl0zyEny83cmBO5ftRmmZxP46dyHmRO448_mtj2bvv_SAbARIf7sWSUB9tyohV-5G3MNGHKq7DPfzGcIHyjtmVWwOrwSb0DmgFE21CRMPxx4R75lthyYSKIT3ZevkkntTaBoaJvMRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=EHmAIF6gKqnUy7nSjJLoJNmXq9f3SMdJllvS8PyscFVb2EHtI3aO6I2c0B1m0wORyPOdw6IBPzeQNFguYp8gKxTf67mk86Uv6GSf3Bw5RGrJWiJRgdLVxa5rhU74ve4npBSsPJg-1eIcsjSWU8lm3rnhONmVeUn8KAb-lIoVbKHCCFey0EGGW3Qu17eErgTso7tJsBaRotOW7dHvVa_d1xHTEwG0qdBsVgZyr4IKh6F-UlPFmMrcQJXrDyCmA-mHvuojcxiHfLFGPkX8XICMT7meVe5y8u53olXRjJm44kHIacIOYnZ4C0hOIXeXS7BGE1EVC1UhcSM8sX7xNaDqgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=EHmAIF6gKqnUy7nSjJLoJNmXq9f3SMdJllvS8PyscFVb2EHtI3aO6I2c0B1m0wORyPOdw6IBPzeQNFguYp8gKxTf67mk86Uv6GSf3Bw5RGrJWiJRgdLVxa5rhU74ve4npBSsPJg-1eIcsjSWU8lm3rnhONmVeUn8KAb-lIoVbKHCCFey0EGGW3Qu17eErgTso7tJsBaRotOW7dHvVa_d1xHTEwG0qdBsVgZyr4IKh6F-UlPFmMrcQJXrDyCmA-mHvuojcxiHfLFGPkX8XICMT7meVe5y8u53olXRjJm44kHIacIOYnZ4C0hOIXeXS7BGE1EVC1UhcSM8sX7xNaDqgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzeRLztZhJd9bSV9D6oCqPMsLA2OZ_dkm33F9K5A1QOSBtnPeQkm0bCBKKlYpYh9ppFvJleJ3zGEKrPShe_oabpST7IZV6eP2Pzr3vPh16OmNMCtSopQgjKR62gIt7opwg1cCjlzPo5ik_cSH4jw4x4Hm7LUNo8xIOtsfaFYkWEOl6PZ4FQit4aNqZQJ-6XFvLX44iqXrKmobjFQCj7Yi2OhXfYQw7o-YIYAzMpaRKL6V82JNkW7C7Aa4KMJ8jQLbc0WxaCpJ9xTG7GQL41hoQ8Dpj-JKmgSKqft5uyNhc6piTkQm3VwDSmhriCBk4wVshBbyWRu-VWvo6jl2i0PbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=EZJyWpGEy0pukZn2KJ_rljylyF4qwEuPoph7LPfZynEKPUzO6IfOi9f7Oo_k0U_mpgN8akXNGSZHsQglA3T2dR3o9FiYeQSQ1S8exvW5w61pavukv_uCL8scU_SrTRR7dmCFrgC8qzTBQQI2Bpt2P6W6pPS1HYQ_1sbIVawvMG5BNGbo96MwvApHuknNyQwN4QoQ4r4zFXgYf5YnGICxDDYuudDrGUX3agAV5pq05eYeASGWARpMfUd1dkzA2uVqp5IcaC1sa32i95_Z4-raoIX3r8wn1X0VZ4EbM5wXnYNz-iYD3T3ZQtXvxIr2XxM8gFfDdppuPpwyTT3KyvT7YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=EZJyWpGEy0pukZn2KJ_rljylyF4qwEuPoph7LPfZynEKPUzO6IfOi9f7Oo_k0U_mpgN8akXNGSZHsQglA3T2dR3o9FiYeQSQ1S8exvW5w61pavukv_uCL8scU_SrTRR7dmCFrgC8qzTBQQI2Bpt2P6W6pPS1HYQ_1sbIVawvMG5BNGbo96MwvApHuknNyQwN4QoQ4r4zFXgYf5YnGICxDDYuudDrGUX3agAV5pq05eYeASGWARpMfUd1dkzA2uVqp5IcaC1sa32i95_Z4-raoIX3r8wn1X0VZ4EbM5wXnYNz-iYD3T3ZQtXvxIr2XxM8gFfDdppuPpwyTT3KyvT7YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSXZc-iabKhMThSrS5Ls_TOS0UwbF9QTjRBl5warzCMzkFLBlfGmKNQpyMOaukDIgilcgoLxn0ZCQWkZC9TXjn3IhCoj4i3CdSvDpVDkEqwQ5ioqMGtFDIk_dLorni1XV6HKKK_lIkfl2RYQ60Xz30AFxgIBIXqg-fzm68LvyxOMlfLH-mtk65QIThehcUb9OGZ9fumFIiEo3qA9ORtIX5YCQ_Mi9T6tx8dcT-Yx5XpHDx4jNaC61wRkguKh0LhGLMzkNJhOFm5brHQfMMKBSzQddbLkvpZOA2Jyn56SCDhkWn5asQa2ZrEiAE96PlCBEKKBJKdgVd8wzHm0YRDB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agkh28A4v3UI-g1ByOUXTSrIKhZCiGgsrhtos6g84jH0jKswv8UQgFvfp6aBS_oKpc6pOIaYnjKl-HooVEhsKPQA8Jw4Ckm7V93sKtn9L-KKv6GI8u5LK7LiyDlqoOdu5Ya5icQVak6hLSsijmCUereBaOSbMbnSlTdxN3J9cITUP2KVL411eszmUKBW-QAYiRpdj_J-Ue3fdu54j7ldkkWLdBcMNl4JXswCGzPcM3F2U5B-wHG5dzAchj1yB1d8sKT7FPsHoT8O_skB7UvuepKJis3WLoDW4K_uOaNlY1_CLr7kb10LRlkFb220lNp6uHF4yWWuWd7D0rkL2FH5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc66rtFgS3Sg1WI0Lj5Hrf-oLB53SIbGnbCHWlb7MBpChQvqZiENGARm_Ec7MqWjDoEbcgWyGrK6H56rJWxTlfZCd-I1UF3LoVJ0aSrjsp6wjat7NVump8A_gRh_lqZTDESbIiKCliGYAKoNHI7z3aRQQok48UaWfjMDYH_crXkpk6ZZhjPsBy2jngjQRkJjnF35F2434ZQinSoOwSSyvv3N85jrQaxjUdwvAFOss-ukJ0ytesc96MDfkoVHBvy5zN27zbqMMYuf3TJhmU-YMmPke3rRzvm0fL_NRcXmomfhEv95BFc5RH7jHKO1PGIpQSAwKlm7vdRS_2nPuhIVuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0tXzYrfod-ri2Bh4MMbjL2KH9CtBshVM65jC2k63CxFMSm-p2Qlzo4ULldsFGCic1gDUoccbEmWrJwY1uIpaCK6Zz0AkI3f6RTGWZzy2fjtz_XDRf6_vC00tcM8bv_7E3TIxajeM-cimJO-Opv-MA3aRznOgdpQIQUsUBcjxBfQ4PNqCDNHrI2gew48u1d2SfkDww3Z-bIOYa_oCix0B9HBnrdd5p3JotluxwU5BGSFiX5njrLCUl4PAACXuEY5-bnb6Y7TX7DLkD_AwMY5xJ0k17kEUkQUStzsAbufkrn26pHhv8gHRu9eLOUEVlKNo831VNtf5k4m60YAz1cdNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9frCi54OsPrnphNX4qcnOrDkpB7ozXPrlj0h-Dz50eONIEHu4TeVAnZIfjx2mW3R-nWdMGZHJL_RvATVB9QcJoLSDcOwIq8_M3imeon_xThZhU_SYX5R92C2__IAKI-2WWMlfF-PouCziVT-6IY7tKPKp8hlYN-WKsUdxfueIeWsXRpCBfE8hWqyg3UgkVkmvBOHTt77t5b9blwlWPz_zZPCt1ud-lxTBrlgocgiTXbc1nMyh46TvSXZFSL2lCcIa1ibOQg5Ypd7xO_HZPG6YXXE_MDg8mRvGQhoWW_UNCAQ9o72ZpqcuhdFNhhX4TE5OuclgqQZBIz6-iasJt4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=INAyA2qpmqA9o__6TuSDdtxHrsHtpfPEAvgACr0Oe9dXyZqG8YF4DdGsjC-7cppxcAWz0538cG1V4U-KJ221qpbozAWpLmnl5mpmhRd0g9DOVoG1VnWfEuW8mSgfB1LTbPjXtZ3PHJrr1Omeueme0OjTDk0SmDziB3Pfw498d9bfAD02WjarT14WAIeva8zpI8j0XTCBD8aqnskt6se9B4msw51NtEBERDtRLjv_7tHHzP04STHIr23k03EFtIvOPyxHMmFtg55pVq99yQX9NFhDwCi812DnXKW1STpdEOnFp3hXbBZCq4BsMTfqPITldE9VjWecRr4eLiTSXilNOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=INAyA2qpmqA9o__6TuSDdtxHrsHtpfPEAvgACr0Oe9dXyZqG8YF4DdGsjC-7cppxcAWz0538cG1V4U-KJ221qpbozAWpLmnl5mpmhRd0g9DOVoG1VnWfEuW8mSgfB1LTbPjXtZ3PHJrr1Omeueme0OjTDk0SmDziB3Pfw498d9bfAD02WjarT14WAIeva8zpI8j0XTCBD8aqnskt6se9B4msw51NtEBERDtRLjv_7tHHzP04STHIr23k03EFtIvOPyxHMmFtg55pVq99yQX9NFhDwCi812DnXKW1STpdEOnFp3hXbBZCq4BsMTfqPITldE9VjWecRr4eLiTSXilNOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqmmvmY1fy9Btj183F5GjDe-V5bxFoPq0LB4WK-rNXO9qsiiiYU1iwo7MqrOdCwlXdazXJwXy9QNiN0mR3suLUnVxNKordP0VHBjv0snrmGYOxzwNUt3fkST3hMgigyNnmdFfxQwbKr0f692qbHGuMs7bkQLEK7NeBnO6eh3OjuYpSqXDHdXC_UgESxplwjMfyPcv4fCLM1ruuw03zWaHRX-Hx3oTGHZV2Pjry1JdhHMxTfWj85PctcifT6XgPejKPBz-AUdmr2E0UwZHTiKuULIXAD5pWsZXFZz4-RR470eJDIQGOzdcgk-Ojhq07QDS92JorS-fEZdRCA4F2h2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmUaxhBXc_CX8EZAzLnXU3KFjhEUW77As0zcT2_qUbqKlTfaqclmIg-oMw9GP8EEQDAzn-bVosTwzc8Wm3S2CvkIBP-M__bci9uzeDs0_jG_-EAhhd3XHGW8IUYuaIj97rKifQg_u1ZhmtNY7wkcthxfBO70BGpErUGeH_x7JQubGF8U1bCChFpAEwbB3ZyYd2EEBh6wSvckhi-A31EN57zW57i-kJbXMsI3mIWuqQrR0rkI3e0x5DCrgWTNCXSmHL6dtPGej3MXizi2pL8j9AxOMldlsYGO9FDsL8w06NNHl5bA7fYT3suJZ2GCj0F1PN-QozL05M8oS6h8V3Wzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=RxhUK5nkjY_9olkwf4fiGhafIMmZBvDMkK-rcI7-LwA0M2hy5Dnlm1WzKHzUygW_JkC77QVyxGsCywmB7szm6QobyN_cWjw6q7IR46bVqaSNicw8YTOm79yE_WFudgVr1ebdgoCMnzrgRIqONr4sq5b_DaLJuV47O-J7GOG0fR-29rV69CEuEWolySxcCJAFWJZYpxMPDnEtBhFCZ2acjCYo7fW3_ShqX6RHgXNYmislHpaFFpFkcdUQF38uuAmIAqT-MGVTip-Ehv1isLklzV2dvhc6Q4dNvaneOnds1GD2vPPz3QCr2-zjOX03AtrN1CziMrJIGgTL5SOzreBiug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=RxhUK5nkjY_9olkwf4fiGhafIMmZBvDMkK-rcI7-LwA0M2hy5Dnlm1WzKHzUygW_JkC77QVyxGsCywmB7szm6QobyN_cWjw6q7IR46bVqaSNicw8YTOm79yE_WFudgVr1ebdgoCMnzrgRIqONr4sq5b_DaLJuV47O-J7GOG0fR-29rV69CEuEWolySxcCJAFWJZYpxMPDnEtBhFCZ2acjCYo7fW3_ShqX6RHgXNYmislHpaFFpFkcdUQF38uuAmIAqT-MGVTip-Ehv1isLklzV2dvhc6Q4dNvaneOnds1GD2vPPz3QCr2-zjOX03AtrN1CziMrJIGgTL5SOzreBiug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os-xQTHW0Uga8PnYGeKyudfK1nl8-KAJkVApAMiBXCByJVrCmywFmfBz5Dno60PLUmVBOkb-2YnEEe7rUO8oUnNJf_fceenLiwxXxT1oE3X-MvnI0dKH4zUQVBqLNL9Hso11ep4IiNLHmSsAh8hdlz8Gg0WiPyKZiSa_73Fkmh82_qtorbLdQFl6Ei-t8wr373qRiqoo05t8aAiZsJouar5EJ_jTz6bIdm-GUP3a_9vBoJnp1aTUN2pmIv6qeiSBmbo1i6ggSwuUryHmgWuQVT9pZiKOoL97ObBXw9hFEqd_Q1NFKww_8VV6TNWzT-ktlc5B_hdL35eH7nnZdTFBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq4zTFr-yZb2pXIkEvBLfRHW9PF_dRM-TAVmGXmAbQbWTsomaHgX0BFh7tmjbpUGMpXAjXXx4bQcMfARvJtPMzkFKqFdZuszhHtxiMGAAuwZgV0nrt2UPIteqz3XSmo2JQDOQImOyuhXTnuv4yEFX9AOQ_-AtVwKKeENt9R6QAqqSFt599PhefXGo7j323AsOqrcU4_8ULYCIRAvCmDXmcJ3X0bqRD4LG5yEPwsH83Fk645izA-5G6F9f8F-Gfs8QSbaa7gvnZgHvQM9QO5keR6jumxXNBGBKHveC5W66dl7Oa4JEyG08ZoL1qQbdY-AyegN5mm1szzmm4syvPNCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUQ0kYwaKMLcaIIcBsee-i_pl7AERtjcqTuneV5cMlxdAgJV-sdLsxpPVU9F0pkmxJqwySoxT1mCbeGqzsGkDOdYBR308ZALYn08Vuudt5Yoo7gMXdsAF3vxNg56SorbANkzB-VsUmK-YVR_fhpCfMCpzhQjiTRlyGVFVlcFll4qIlScpYcHCOdFmJGg5Xv8z1159aL6g6wN2BO-NGXSLt5hRW8W-Hs2eZJUJeWPmZz9Oqpcpat7smsLKX1OAhA4F8J5aJfC5WaW2FiHSBgUWIsXStcJRQZW8mXcbe2nh_ptGqbZh3yBYUn_8hVHpNOuucKpZqRazxlVFBiMZPYAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtJUXVuvUWO-_eLxWYCpjws3AXx1R5HMePLPwfs23ozUyM5LtH4dcCK7i-g0cfJoI0SMoEOrWpdK4pWAATqzJRWzyngrP2AW9DK1fFgS46baLZorjUAXEA-7pD9xzDqIQ_A8X-2VxQtRXVdQhk_arFdohuPA2RjvFKZnTZnt1qN2mch7Kifjcz9cqZkhdXjIRX_eXamldGyNUuPJDulX4HfhLEAosUSYUvNbTpgMEALoV3EjbCZGcm5tSNu3unkFLzm6PkHhxNMzndPuWdfQP4-YIzHHPAZNccCQvJurfHpG_M8WeXzZHY5OGaDVcCuO4LhqTYI05oarrvzfgEMN6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7Db7V2rN7zzzyL4dcYKZwapVbdxteRBk6mrx6ujT4daDi6YuBsW1tpESaeRWRu5uQObeuQAGkHhQV5EciYq-cHm8c84ovcD9yx42roeEsGOiwop3wH0LpeLi_d3ZWSpDSrlNNbdFlHAMSHJsK4Lli04EfV3YGiv6fzmCpVPO_nJevbNo1sN56dZufB5ntZS3bBOH0idDH7Hn_o6eD4h2Y3lwUfVS1CRjFnoX1ib11UgtIVz0RB-qWDDGePdPJxZM3RzV7lQMhxqHSqLTFWCC-FyF_IzG4mgnK9v4hI6VYdCqGDOcUcxP1-NaLZ87ZK1IRLoCUcsvMWq4yHEpBs8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiJzhcJJR18D4a0FGqXbDzoLAYBhWEpkJ-fAh6hseEiys0LP1WFw74iNbUXhSlnkhKx3BFovGZ8_OXWfhuJxf8bot2DumFs9syu-0YxUPFIeWS9_jTwfiwCGucRsV49ygpk-1zNbn8MkGhQm5odLv44lMVBtcsLFN5RGEUejvg7wH3ZV3Sb2FPMjZ2NtoZ514cwyevn3BJwy2W3R07e7GvKPeKFZg6sHB-CaZp-Zqe6c3kOUCSWzN6KyBVQmfs0UgY54gRVLsHZPNfrqXbE06od4EVp4bXNxQQTyz5NXJhizXFoJDENK25qQLPJlky6gAy979T6lJp-uHwacpFW56A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmZzr2oyviN7cOlAcA-kAHf7Yxz-TUt6Gap7PwIcxVVMtllL__oHHYQCB-ohFnSLfHvRv8eaU_wKIHiEPrxH85gN6wMxT0_S_IHQMAs1Ha5bhcoXAdXOYrvQF8XIult6CoPCcvD8vtBTONbDWHU65rqoQhU9wiAAYaS8x3svy0tQ5mp5FYU552EvT0WZS6W8Kjwwlcb3zdLTjc5PomHuY2YqPOHdMtywp7fXlJdeKhSuznKwX_d4TUlUx-zpi0by-f5l5IEtVjV2W4ipPX2sYlKu0yTqXHX0Nn5FDvpoclbIdMxt2-m-jzcdFptt9FcIen3s9UJhapKFrJGj1hQ4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG1j1mRbKqdT2cTRypOoXFUZpZRvKkTdi_hlYq7A2iBYgxpulllth6Dh_ojbNd-Kn2IdXOKTpvBU79CMGUvD30KwlNVat-1Q4ZLMs-Uvktc3p2bc4F7vvCTcq6SEO4rP2wtRyDiUZi9ZGYblYNEwAeixmS8kMIdqwZHmkbOyDKodAoswQwmTbavuryDbTbbXVbJenOWIxqvjPB5nqv_S_h-qme2uTs2lyqfRsCoiE-b_gicYhOB_8pA3_id9DVbEvYOGUxstLbx752Bjw9eYAkZ9Bl1iAqbaqtsptGEocu0qkUbL8j92Mw6TRxcdTRKScyCdZFqMCCvJhx_veswacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJr-dIEZX1Fc-FSSLbh5j7ub0w3EXNJcigJBUx3GgYchl4WFI9CZrK3VPYT1PsrLiYn6U11r41cnsl5fXAPeManXqWvtUdRTGehrnCcNgClrHTGUNm9rIR-TeyiQqhNRfOuVLpvFkRvgGN2iDQlMZDilkP0TVojMaPw5jf8v2ybjESN3Fr-qvE_zM_uUmg0mZPc_uQOlyFuO6ebN-VFFjvEuWH3NNXJRqeRBqEDn_GRqC8WWisyZG4GMkPfTHeS7BNuGmSlq4xSqnORKMiMMYFR-rWhPoqTAuM9psG5up_dRzu4Mqodg_lQ7vEeKikAvdIGBajRyy2auqqFfljO74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbSakZdZMzhlEGT5qdC1-m9EvQy24HGZ-JyBYvFZ6Nsjl9vtrr5JGFxNH1TU2zSp-VKn664l17KBCh-3qaPlA7Wmcs66NotcAkrEWo7obNMZU5nWpEmnZSDnuLaHWqIwHHD6q84sSGSgcYoiQvQRlgvdmuzASAO39sKumQ8gdiUGIgSFjn0uos232-rSgfx2iVd_EYHjfm8AW3e2pEt6yRd-DlES787-r8V7WvPIindkLNxtkvH9vZ-pCCOgRAg1-IuQpHVeJXfaQtjwiuF-Cf3qcXFT28Xc6IgT20InAK_Sd_HDx3DWOGb_oOQyoEfvGiN3X1QxgwOpDw-6SZaUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
