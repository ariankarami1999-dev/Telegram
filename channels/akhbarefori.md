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
<img src="https://cdn4.telesco.pe/file/AfcILezzwYHZNbc0Dx8ZI4rh_G7jP7EZhqh2YyOliUjfgbcxjyJMKypq7wSKu4pSd-wrF4rtE_deyZJ6ctpkShhv0gmna9R2gJ0VAC7_qJgHwC08KcIhl8-8J3cMb8q2XhR3I8SXzVA90HaDHfRrGL-tEaD3PmjttuiPF7AWGsr8P3FadUyhsfo2VcCje4MmdnsPuw2mBcMPx7Ppm7Hy7OOBZZ4nJgj1i0u3D72tABB2DLJgnHbnnBbqcjjXNZYiagMlhg1Jpf1tv_0BEdG1FaUcvr1gdsURiJ-HbUojLzcCBBFmcPSKERcshazC4hgVaxMrpMDDnGHtxd74vBHF8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.06M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 11:56:10</div>
<hr>

<div class="tg-post" id="msg-677983">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86e7c50f7.mp4?token=u-u25Bncg9BRDYw2qYYQsk1HUjq3oa2IVvDriMnuLNZt_lKc8DwniPojMRElwZZSW0Ruw1-Gqs0yM_XDdwHmwVAANDBHumfgJPi-bpugkNgPc5V90nSMKlYoIgbR7bAY1xUajtw4xxekh8sP357Z7jM8yHtAySDW-gwv1s1kPHdvS44qIQNdb7KjvqmkMRszOBepBNsCcoglw4XAbLozLn9BfaSghB8GevGZVxa8SIhSulnIprgWXNZ5_pv4CCweK0kkzu9Ab8ayVyZv5Pn_E2iOhbQc1loy3NINd44DyyPYzWQNiZyBCe7ujIrtPaVtD7W4a6oVROPrchEwzVpxXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86e7c50f7.mp4?token=u-u25Bncg9BRDYw2qYYQsk1HUjq3oa2IVvDriMnuLNZt_lKc8DwniPojMRElwZZSW0Ruw1-Gqs0yM_XDdwHmwVAANDBHumfgJPi-bpugkNgPc5V90nSMKlYoIgbR7bAY1xUajtw4xxekh8sP357Z7jM8yHtAySDW-gwv1s1kPHdvS44qIQNdb7KjvqmkMRszOBepBNsCcoglw4XAbLozLn9BfaSghB8GevGZVxa8SIhSulnIprgWXNZ5_pv4CCweK0kkzu9Ab8ayVyZv5Pn_E2iOhbQc1loy3NINd44DyyPYzWQNiZyBCe7ujIrtPaVtD7W4a6oVROPrchEwzVpxXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری به یک اسرائیلی: بر اساس حرف‌های شما، جان یک اسرائیلی به اندازه جان هزاران فلسطینی ارزش داره
🔹
شخص اسرائیلی: نه، این کاملا غلطه، جان هر اسرائیلی به اندازه ده میلیون فلسطینی ارزش داره.
🔹
مجری: اما این نژادپرستیه
🔹
فرد یهودی: آره هست، چون خدا ما رو انتخاب کرده و شماها دارید حسودی می‌کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/677983" target="_blank">📅 11:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677982">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانجمن تجارت الکترونیک تهران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae2e4338b.mp4?token=IOCs2Rp6hPt3LDwFe52fMFFgyEleL7mIm5pgi8yN0LExcg9-ayOcGcoIzFIr4lLQllCAP3dDFuVOOOZYgzRax_mU67m944ywGyaAZl2ErutBa1z8PX4bmFVHUwDv4GWGI8JL9mWyass0JU6TSg6AQL7brMJKCqhWvXpU01hsngr-2LFWayrlFhWrmsHVkkvV5NShziT71t2VKpxO4AdAcgjawlSqLdflEs445yLH2D3SxArKeYA1z9EHGPjSmmH7FkG3QjGAJZebAeEkXLw_T4UbNR06MVMJk1L1YNT87bDzkpAgHWKEMGkd8FueGNxPRliG14MHegkd0ho9NyPUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae2e4338b.mp4?token=IOCs2Rp6hPt3LDwFe52fMFFgyEleL7mIm5pgi8yN0LExcg9-ayOcGcoIzFIr4lLQllCAP3dDFuVOOOZYgzRax_mU67m944ywGyaAZl2ErutBa1z8PX4bmFVHUwDv4GWGI8JL9mWyass0JU6TSg6AQL7brMJKCqhWvXpU01hsngr-2LFWayrlFhWrmsHVkkvV5NShziT71t2VKpxO4AdAcgjawlSqLdflEs445yLH2D3SxArKeYA1z9EHGPjSmmH7FkG3QjGAJZebAeEkXLw_T4UbNR06MVMJk1L1YNT87bDzkpAgHWKEMGkd8FueGNxPRliG14MHegkd0ho9NyPUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسابقات جهانی مهارت (WorldSkills)، بزرگ‌ترین صحنه بین‌المللی رقابت‌های فنی و حرفه‌ای است؛ جایی که جوانان ماهر، نمایندگان صنعت و آموزش، گرد هم می‌آیند تا ارزش تخصص را در اقتصاد امروز برجسته کنند و استانداردهای جهانی مهارت را ارتقا دهند. این رویداد، پلی است میان آموزشِ مهارت، نیاز کارفرمایان و آینده شغلی نسل جوان.
🔸
انجمن تجارت الکترونیک و شرکت‌های آروان‌کلاد، اسپارا، بیت‌پین، جیبیت، دیجیکالا و گروه مدیریت سرمایه لیان کپیتال، در این دوره از مسابقات ملی مهارت، حامی رشته‌های تخصصی فناوری اطلاعات هستیم:
توسعه نرم‌افزار، امنیت سایبری، مدیریت سیستم‌های تحت شبکه، پردازش ابری، فناوری‌های وب، توسعه نرم‌افزار موبایل، طراحی گرافیک و رباتیک.
🔹
همچنین رسانه‌های ایرانیان استارتاپ، پیوست و‌ دیجیاتو، جزو حامیان رسانه‌ای این رویداد هستند.
🔸
اگر در این حوزه‌ها تخصص دارید و آماده‌اید تا مهارت خود را در سطحی نزدیک به استانداردهای جهانی به چالش بکشید، جای شما در این رقابت خالی است.
برای کسب اطلاعات بیشتر، آشنایی دقیق با رشته‌ها و ورود به سامانه رسمی ثبت‌نام، به لینک زیر مراجعه کنید:
etchamber.ir/worldskills
🆔
@etchamber</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/677982" target="_blank">📅 11:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677981">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7abafac1a.mp4?token=b4InKA4TZy25ZuA47vmBIP9UoPKZgLCTn-8SWkn31HyMytXehJriQYSbHxHiePVZ5iOQpMi2uZZ-bJFiW5-qc1TPmORrLLiho_iHEWixCroJohBdFyjtGOnzFJTIn9mRRuL_MqHvJEdtqLnR6baeR4oyCflxdYIwb3HfwzEhSIk2ncahh4A6CvC6L0nNPsOmW9aN_g7yd-ogO3dxjWIvG0I0YhTC3s8OfaIqsJ7_cbK7VlBUJQ_b28O_kHXBVJ4206GA_-xajvywXpuKO8k8lpoYT9SfwcCQotIXn7KeiqyGXmGLuYtxcUEJn3YF7_iKrIg_6GwNkZwYMhOK2DClpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7abafac1a.mp4?token=b4InKA4TZy25ZuA47vmBIP9UoPKZgLCTn-8SWkn31HyMytXehJriQYSbHxHiePVZ5iOQpMi2uZZ-bJFiW5-qc1TPmORrLLiho_iHEWixCroJohBdFyjtGOnzFJTIn9mRRuL_MqHvJEdtqLnR6baeR4oyCflxdYIwb3HfwzEhSIk2ncahh4A6CvC6L0nNPsOmW9aN_g7yd-ogO3dxjWIvG0I0YhTC3s8OfaIqsJ7_cbK7VlBUJQ_b28O_kHXBVJ4206GA_-xajvywXpuKO8k8lpoYT9SfwcCQotIXn7KeiqyGXmGLuYtxcUEJn3YF7_iKrIg_6GwNkZwYMhOK2DClpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در شبکه‌های اجتماعی ادعا شده است این زن برزیلی ۱۲۶ سال سن دارد و هنگام پایان جنگ جهانی دوم در میانسالی بوده است؛ ادعایی که به‌ سرعت مورد توجه کاربران قرار گرفته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/677981" target="_blank">📅 11:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677980">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
جلوگیری از خروج ۳ میلیون دلاری ارز توسط شرکت صوری در شیراز
🔹
سازمان بازرسی کل کشور با شناسایی یک شرکت صوری در حوزه تولید اقلام دیجیتال در شهرک صنعتی بزرگ شیراز، از پرداخت ۳ میلیون و ۴۰۰ هزار دلار سهمیه ارزی به این واحد ساختگی جلوگیری کرد.
🔹
این شرکت در پروانه بهره‌برداری خود به دروغ ادعا کرده بود که به عملیات تولید انبوه در سه شیفت دست یافته است؛ موضوعی که با بررسی‌های میدانی کاملاً خلاف واقع تشخیص داده شد./ تسنیم
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/677980" target="_blank">📅 11:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677979">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت امور خارجه به عدم پاسخ به توهین های ترامپ   بقایی:
🔹
بگذارید ما ایرانی بمانیم ما منش خودمان را داریم و فکر نمی کنم از گفتار ناپسند و رفتار دیگران الگو برداری کنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/677979" target="_blank">📅 11:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677978">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تنگۀ هرمز گوشت در آمریکا را گران کرد
مارک وارنر نمایندۀ ایالت ویرجینیا در مجلس سنای آمریکا:
🔹
قیمت گوشت گاو در آمریکا ۱۲ درصد و مواد غذایی ۴ درصد افزایش یافت. اختلال در حمل‌ونقل دریایی از طریق تنگه هرمز دلیل اصلی رشد قیمت از سوی کارشناسان این حوزه مطرح شده است.
🔹
طبق آمارهای رویترز، آمریکا به‌دلیل خشکسالی و افزایش تقاضای داخلی واردکنندۀ خالص گوشت گاو است و سالانه ۲.۷ میلیون تن وارد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/677978" target="_blank">📅 11:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enu2cQFbIChSxEnABcSPOxDpT_z0qYytmD0q_GYJMzOsxA9plKt1wIxOpVAWVsvfYQvnEy_CESACb-Iki8U17TP0r5LPXmEgg9MR_i_hi6qkD8I0pK_SXR0Yo_Y1lb7ew6GL7BZZHnoSZyluYuv6HvyKkULrbZaKmpUxoi6jljoKAfF5vcC4LmOkKAgNRSOIuivCdO_qPZGYjkTr-W2ykMh4HTk-IiQpKBNECAxgjo8C7KqpowD_Cy1WM_ARogwm4fB7oCLmq6BCjBLgF7FblE0A5fOVXVfOAbxCwfooz3Tp7hlJU_ac95puRgP2m7ToPV2ItLtY7UHUQ5-wK4TOGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آگامای خندان، خوزستان
🔹
سیدباقر موسوی
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/677977" target="_blank">📅 11:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677976">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامـیـن‌الـلّـه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d206ee0a.mp4?token=pp9mZjC-NqgYIV8DU6HCBJxjRCF2_QdD_OewG3oixxJCjfN-j1jmcdiwJNvXZ_kEnJ7djG58alffu1r4cm5vXSKgOWMsYbuGfKWAEzJDf6Mg_3NzRUgvlXsI8dE-Y-ydqWVSkK3wQPqOPPK26hZiPUoKn9raBD15BTxU5ftVB67jFVPIfmqEnfVTMknsEf6RK37eoNFvmGTK2Dl-3nO5-Ddhh6sYX5RVtt36iX7UEruErUoSq2_XHbvLltFaltb8YH0pav2UXTionVWvu2iwHvf85qHT6eiW4tOwJnHgyv16R2IqPyCIhyflbyqCpcBQ6PkocQUZ20Xp0tlyVvneIVwufpNe3fGhgVUgiLeS7JKpsibNmZ8zyXoISeaacV-vOFK-NsucG4JYxJ2HavNGXJqxu1r8oO6r-kSZ0lGqWdL6kQckZspXgJWfd1xqRPwv7rA8KLc5Zr8eR1MUgtkZKa4Zm3pgMxymw-cbWmF5pGVN8-xLxCBc2__LK-NOFj3opHDzRvpTfJ8IWGGeZ9SDpij_mHQdQ0jnG22ELU7LbocxLM5j_4N2oo1FPPnUYY6qex8zgag-d6-MVQBKIZizVmnMIwe28k7naRB4NC39WNHSvGsgHT7xnNC7mnWh5UamN6Shn4DKXmUwpT5AbceW-XVD4WFwvOu-tYTKjCEJOU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d206ee0a.mp4?token=pp9mZjC-NqgYIV8DU6HCBJxjRCF2_QdD_OewG3oixxJCjfN-j1jmcdiwJNvXZ_kEnJ7djG58alffu1r4cm5vXSKgOWMsYbuGfKWAEzJDf6Mg_3NzRUgvlXsI8dE-Y-ydqWVSkK3wQPqOPPK26hZiPUoKn9raBD15BTxU5ftVB67jFVPIfmqEnfVTMknsEf6RK37eoNFvmGTK2Dl-3nO5-Ddhh6sYX5RVtt36iX7UEruErUoSq2_XHbvLltFaltb8YH0pav2UXTionVWvu2iwHvf85qHT6eiW4tOwJnHgyv16R2IqPyCIhyflbyqCpcBQ6PkocQUZ20Xp0tlyVvneIVwufpNe3fGhgVUgiLeS7JKpsibNmZ8zyXoISeaacV-vOFK-NsucG4JYxJ2HavNGXJqxu1r8oO6r-kSZ0lGqWdL6kQckZspXgJWfd1xqRPwv7rA8KLc5Zr8eR1MUgtkZKa4Zm3pgMxymw-cbWmF5pGVN8-xLxCBc2__LK-NOFj3opHDzRvpTfJ8IWGGeZ9SDpij_mHQdQ0jnG22ELU7LbocxLM5j_4N2oo1FPPnUYY6qex8zgag-d6-MVQBKIZizVmnMIwe28k7naRB4NC39WNHSvGsgHT7xnNC7mnWh5UamN6Shn4DKXmUwpT5AbceW-XVD4WFwvOu-tYTKjCEJOU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">؛
جنگ نخواهد شد، مذاکره نخواهیم کرد..
چرا و چگونه؟</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/677976" target="_blank">📅 11:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677975">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c67d84f4e1.mp4?token=BUaNzcOjgN0Kp0lNV9MkAIu4eA7sGMgKvu97DyjwQoIzpAIGqGsQvZWAnxJntSt2EvME-rcRmcxAGvURKZZb71HSI7pikyiRvtWANE_5k85pxf9punwJs3fsclqcyeUUkRAxYI-Yd0rcgHK-z1sEFNDOvp8_WoHqu4r4ckeKJPZzplDse8aA3SI3ikkvrSQRYskKNYi0hfDVeBbh5IJ9nsEWCorm0o_U_9FfJUTTdD-_S89N8XXQWwLQtM3XfHJwv6Gv3x91AJxhgCBX67LDuNmky0Uwbg7Hy4ZtwpKrMTvwped2QAPWOGa63RmpP6du-Y2OKNbmxmVUKq7-gPZ6Vwul74nedCREVN3PZk4lL3jHkt9cfEQvBf99pySLqGE9b8OFBMLPjeoWALaKJcym1zU08cJuVSYROnZIzVt_r_QC28mrdY1Vlxq0XHp440HMXw0hMYqSQEK_YHUDU3at8Z_hKg7eBlFKFajg1FoddwizGq_xnsBBMu3ogMTOhgeVbDokMeIEiNJZJg2W8Lq1r--YpaaEZY0YgWhiSF0NmQ09zSoe2sLfwahyVg0eDVh4n_x-W1gdXGJNp0DXoi2w3XNdP-IvJZkgKS_IvzeRqNgKSiH-iLBRYp7kyhXJZTQcrEa0AXyCuX9B4_uQT9JN4oFD9NzDKEVvzE8_--ypOJs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c67d84f4e1.mp4?token=BUaNzcOjgN0Kp0lNV9MkAIu4eA7sGMgKvu97DyjwQoIzpAIGqGsQvZWAnxJntSt2EvME-rcRmcxAGvURKZZb71HSI7pikyiRvtWANE_5k85pxf9punwJs3fsclqcyeUUkRAxYI-Yd0rcgHK-z1sEFNDOvp8_WoHqu4r4ckeKJPZzplDse8aA3SI3ikkvrSQRYskKNYi0hfDVeBbh5IJ9nsEWCorm0o_U_9FfJUTTdD-_S89N8XXQWwLQtM3XfHJwv6Gv3x91AJxhgCBX67LDuNmky0Uwbg7Hy4ZtwpKrMTvwped2QAPWOGa63RmpP6du-Y2OKNbmxmVUKq7-gPZ6Vwul74nedCREVN3PZk4lL3jHkt9cfEQvBf99pySLqGE9b8OFBMLPjeoWALaKJcym1zU08cJuVSYROnZIzVt_r_QC28mrdY1Vlxq0XHp440HMXw0hMYqSQEK_YHUDU3at8Z_hKg7eBlFKFajg1FoddwizGq_xnsBBMu3ogMTOhgeVbDokMeIEiNJZJg2W8Lq1r--YpaaEZY0YgWhiSF0NmQ09zSoe2sLfwahyVg0eDVh4n_x-W1gdXGJNp0DXoi2w3XNdP-IvJZkgKS_IvzeRqNgKSiH-iLBRYp7kyhXJZTQcrEa0AXyCuX9B4_uQT9JN4oFD9NzDKEVvzE8_--ypOJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جدید جبهه پشتیبانی سایبری از امحای ۲۵۰ ترابایت اطلاعات شرکت نظامی ایمکو
🔹
جبهه پشتیبانی سایبری در تازه‌ترین ادعای خود، از نفوذ گسترده به زیرساخت شبکه شرکت نظامی-صنعتی IMCO Industries و امحای ۲۵۰ ترابایت از اطلاعات حیاتی این شرکت خبر داد
🔹
جبهه پشتیبانی سایبری در تشریح جزئیات این عملیات مدعی شده است که اطلاعات استخراج شده شامل موارد زیر است:
نحوه تولید قطعات خاص و دسترسی به نقشه‌های تولید
محصولات تولید شده یا در حال تولید برای سیستم‌های دفاعی
دسترسی به قراردادهای کاری و شبکه تعاملات شرکت با رافائل، البیت،
صنایع هوافضای رژیم صهیونیستی (IAI)، نیروهای دریایی و هوایی ایالات
متحده، ارتش رژیم صهیونیستی (IDF) و ATENA
نقص‌ها و نقاط ضعف محصولات خاص نظامی-دفاعی
اطلاعات شخصی و هویتی همه کارکنان
تصاویر کامل از داخل کارخانه و سایت‌های تولید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/677975" target="_blank">📅 11:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677974">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سپاه تهران: عملیات انهدام مهمات عمل‌نکرده در حوالی پارچین شرق تهران امروز از ساعت ۱۴ تا ۱۶ انجام می‌شود و احتمال شنیده شدن صداهای ناشی از این عملیات وجود دارد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/677974" target="_blank">📅 11:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677973">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
شاهکار تازه بی‌ام‌و؛ M 1000 RR 2027 با سرعتی فراتر از ۳۱۴ کیلومتر بر ساعت
🔹
یک سوپربایک آلمانی تمام‌عیار و یکی از سریع‌ترین موتورهای دنیا که با موتور ۴ سیلندر و حجم ۹۹۹ سی‌سی، قدرت خیره‌کننده ۲۱۲ اسب بخاری تولید می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/677973" target="_blank">📅 11:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677972">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q66WYdKNe4DWHlSHVpebT1kYkXuSFyirSKSBFdJI_HJVZetxDF2tuvKUAFk8jQCzvGJxp28kdhhucKteGZqE55Mj7pJiogkx3-vfVcTqZ8U0fuw0yV4FsEnLJmm9-k1jDn-6IyHzEoo5FQBvWHRsXK1Ifsr-4kcRdW_ySwSQYhYvnS3_nGJPtePcUT7SmsSHXMVVzA_NBtenJUdZtiZ9WfJbjAotC_L-VG-x4GDrE8IPqAF6pL7vF5GgpeB1pjZh-ziM8nTCLdWOlIs6XgOxFUgqyVb3VCF-DWeI-PoEPPCYyF_P2XduWOREctBVQSQ0qNlTk9OODk0SkyMluRqCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعمیرگاه موبایل شلوغ‌تر از موبایل‌فروشی شد!
🔹
مراجعات برای تعمیر موبایل از خرداد ۱۴۰۴ حدود ۴۰ درصد افزایش یافته و تعمیرات سنگین مانند تعمیر برد نیز به گزینه‌ای اقتصادی برای کاربران تبدیل شده است.
🔹
سهم فروش نقدی موبایل تقریباً نصف شده، حدود ۴۰ درصد خریدها اقساطی است و استقبال از بیمه موبایل ۲.۵ برابر افزایش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/677972" target="_blank">📅 11:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677971">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت امور خارجه به عدم پاسخ به توهین های ترامپ   بقایی:
🔹
بگذارید ما ایرانی بمانیم ما منش خودمان را داریم و فکر نمی کنم از گفتار ناپسند و رفتار دیگران الگو برداری کنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/677971" target="_blank">📅 11:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677970">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26fe6ccecf.mp4?token=DIZdYtPFOVHlHzDv9rEm5x5mzh8HA0HOUS7HkjM7rcPRWE1m5bKaGR1pvsbPWgIlzbMXqiDr8HBh63wNc8bTxuEbZvow7hKhh8u7NdM6d0ZMTS99HjrPQpUR44ioMVMYDeLYSyX4FiKEJmdUorOn6ASEB_n54gyZBAMEUa3vf9gN19ZU3LPXQDnVM_4hAMiXYe6WxZzgcio5I6dT6BbM2GWEh60E0kTEkf0Uhkj9YtPqelESagjCoTfFhPDYn4WIsHoXAbaKbje-7WHUZ5T6pkUwDPVEplWytMB9Z-g11RtW4CZ-AgcedDjybDZ5z9CgxY5Jz3lXdftwGOFJoclxByj46DnFoEAZjyZocb8LKsY4KXB58exiUZatHBhk00ddMIxnjaQd8aW7g-A2oVctx-IQ2WiiSMRer95C4bhzhS2QB59ctbVhWYEfyQkMgMgJA4tjsw9hqT7g1V7PMCbv4iv2uJfQESlhEJcD4HCwu1Do7i8J3E6k6sdpVkyEWwQPFa6paqoEBQpnAE-HPKSZOFID1N0h7cwMjlxFNN9nHaWY1KZIy-bSP6rxAGOP6UQ1teUC6fJVUyGNxjHKH8eoMEZljR22bBbNjIFBQi5yIcRU1EPO1P3OixliS27ANTv_YHh2CQn9pkqDtLZSiMOGBRevQParH1we01RdPl5ZKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26fe6ccecf.mp4?token=DIZdYtPFOVHlHzDv9rEm5x5mzh8HA0HOUS7HkjM7rcPRWE1m5bKaGR1pvsbPWgIlzbMXqiDr8HBh63wNc8bTxuEbZvow7hKhh8u7NdM6d0ZMTS99HjrPQpUR44ioMVMYDeLYSyX4FiKEJmdUorOn6ASEB_n54gyZBAMEUa3vf9gN19ZU3LPXQDnVM_4hAMiXYe6WxZzgcio5I6dT6BbM2GWEh60E0kTEkf0Uhkj9YtPqelESagjCoTfFhPDYn4WIsHoXAbaKbje-7WHUZ5T6pkUwDPVEplWytMB9Z-g11RtW4CZ-AgcedDjybDZ5z9CgxY5Jz3lXdftwGOFJoclxByj46DnFoEAZjyZocb8LKsY4KXB58exiUZatHBhk00ddMIxnjaQd8aW7g-A2oVctx-IQ2WiiSMRer95C4bhzhS2QB59ctbVhWYEfyQkMgMgJA4tjsw9hqT7g1V7PMCbv4iv2uJfQESlhEJcD4HCwu1Do7i8J3E6k6sdpVkyEWwQPFa6paqoEBQpnAE-HPKSZOFID1N0h7cwMjlxFNN9nHaWY1KZIy-bSP6rxAGOP6UQ1teUC6fJVUyGNxjHKH8eoMEZljR22bBbNjIFBQi5yIcRU1EPO1P3OixliS27ANTv_YHh2CQn9pkqDtLZSiMOGBRevQParH1we01RdPl5ZKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاله جای مادره؛ آخه سینا مادر نداره
🔹
سینا ۲ ساله شهید شده، مادرش هم شهید شده؛ پدرش هم شهید شده؛ مادر نداره که در فراقش بی قراری کنه؛ خاله جای مادرش بیتاب فراق سیناست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/677970" target="_blank">📅 11:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677969">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b0031944.mp4?token=fpYGH61NvTvdlLc_n53CTzTlqjPYWRZ8N7c9dZCaEQpQHbSPYtUWHhosdtSh0b81J_-cSnvKJ7F6g0BkQutyVHRq6bi0rOt_lX0BUkXwyBI6RD2CoVbvLwP6IjADWaSiwWnpTp3zn9dJB1gGF7E5cm2j_szTiMPdzth9fvJLSjZ_t_wnz8G8IYW1Nq5LfpW6_GZvRGjXI3908FkTIGiwZn0BQDrUlbbEIFM_KYaHpPsNtjmysiwXtZr_7bXaaxgwUFCOPr80PqDILMqZy2uMPg9eMUGta4BhQuVeB2O3wPyj5S1PYZX-f03Aajbyi4ELLNh6sca_8IebailcAG_tDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b0031944.mp4?token=fpYGH61NvTvdlLc_n53CTzTlqjPYWRZ8N7c9dZCaEQpQHbSPYtUWHhosdtSh0b81J_-cSnvKJ7F6g0BkQutyVHRq6bi0rOt_lX0BUkXwyBI6RD2CoVbvLwP6IjADWaSiwWnpTp3zn9dJB1gGF7E5cm2j_szTiMPdzth9fvJLSjZ_t_wnz8G8IYW1Nq5LfpW6_GZvRGjXI3908FkTIGiwZn0BQDrUlbbEIFM_KYaHpPsNtjmysiwXtZr_7bXaaxgwUFCOPr80PqDILMqZy2uMPg9eMUGta4BhQuVeB2O3wPyj5S1PYZX-f03Aajbyi4ELLNh6sca_8IebailcAG_tDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت امور خارجه به عدم پاسخ به توهین های ترامپ
بقایی:
🔹
بگذارید ما ایرانی بمانیم ما منش خودمان را داریم و فکر نمی کنم از گفتار ناپسند و رفتار دیگران الگو برداری کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/677969" target="_blank">📅 11:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677968">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10fa703e3.mp4?token=UMSMfBWRBGC-ny8_853PRyMaEH4NO56Fq0n_lug_nBOBZsO2j0AHQ-Eyzj5_mjQHYJ8tLqUK_kyy7Gj8cTQYNlzGwlwp_rkOeqCFK7QMJlfnZkbNJWLedvRuFEuhSCJWe7469-LE5upC5h7StyNVWx9x-wRhuy1D2u0FLeRvFQZo9oXVCoR2Kp0ccg8qLyUmAZUfQEhyLIDCJp7gpOb-BQsTNdMAMsPmzmKO5mtiUYTc5x-oV0W3QIt_HB-MbUXdAMb0Co4cJDps2Mo9bbi5PzxSfcilgT4YB-l-bgBYCVgWrYBu81SzpC1DV-_39RdaEn2jHAInF4wcV3oh6CfjpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10fa703e3.mp4?token=UMSMfBWRBGC-ny8_853PRyMaEH4NO56Fq0n_lug_nBOBZsO2j0AHQ-Eyzj5_mjQHYJ8tLqUK_kyy7Gj8cTQYNlzGwlwp_rkOeqCFK7QMJlfnZkbNJWLedvRuFEuhSCJWe7469-LE5upC5h7StyNVWx9x-wRhuy1D2u0FLeRvFQZo9oXVCoR2Kp0ccg8qLyUmAZUfQEhyLIDCJp7gpOb-BQsTNdMAMsPmzmKO5mtiUYTc5x-oV0W3QIt_HB-MbUXdAMb0Co4cJDps2Mo9bbi5PzxSfcilgT4YB-l-bgBYCVgWrYBu81SzpC1DV-_39RdaEn2jHAInF4wcV3oh6CfjpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: به‌تجربه برای ما اثبات شده که چیزی جز اقتدار دشمن را از شرارت بازنمی‌دارد
🔹
واکنش بقایی به خبر از سرگیری مذاکرات ایران و آمریکا: قرار نیست ظرف این روزها میزبان هیئتی باشیم یا خودمان مهمان کشوری باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/677968" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677967">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بقایی: آمریکا با بمبی ۱۰۰۰ کیلویی برای خانه‌ای در قشم کمک فرستاد  سخنگوی وزارت امور خارجه:
🔹
آمریکا بار دیگر برای ما کمک فرستاد و این بار یک راننده تاکسی در قشم به همراه همسر و فرزند ۲ ساله اش از این کمک‌ها برخوردار شدند و یک بمبی که بیش از ۱۰۰۰ کیلوگرم وزن…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/677967" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677966">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی انگلیس: گزارشی از حادثه‌ای در ۲۰ مایل دریایی شمال شرقی خصب در سلطان‌نشین عمان دریافت کردیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/677966" target="_blank">📅 11:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677965">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
بقایی: اعلام موضوع سخنگوی وزارت خارجه نظر شخصی نیست   سخنگوی وزارت امورخارجه:
🔹
دستگاه دیپلماسی کشور مجاز به فانتزی سازی جنگ نیست. وزارت خارجه برای خوشایند جناح های سیاسی موضعش را تعدیل نمی کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/677965" target="_blank">📅 11:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677964">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff96cb6e64.mp4?token=Q0I6UJ0tRTPu1lk_AE9AXUSj37ezUlGYZXyQwl5_eq5Yr4sNF_7FUb2bHk3I1-JP4bGMXDT--jliSoZaA8nmp7uI7lPn1tcpHKj7gMarAO945DynklO5CpwI0_eT_3-mX3zG1vWjvgOcnXzeCUEKQWm5RwSCVwi8uaE1mRjq8SD2f_3CBmzq2Ox3yAI7ZlWd0KAzTx4OEP0bFdv8FVE7lDL49K9j4jonHYW5pAJkVs6BduBy_uPKHO7KKx32XeP-D0SnfX3peEPt2JsuISK7Pg1bzS8Rog1IR57zur4kCDgbSlMTw-hm_1U75aqwsC3fgl8B425w0wyJsIjKkthbfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff96cb6e64.mp4?token=Q0I6UJ0tRTPu1lk_AE9AXUSj37ezUlGYZXyQwl5_eq5Yr4sNF_7FUb2bHk3I1-JP4bGMXDT--jliSoZaA8nmp7uI7lPn1tcpHKj7gMarAO945DynklO5CpwI0_eT_3-mX3zG1vWjvgOcnXzeCUEKQWm5RwSCVwi8uaE1mRjq8SD2f_3CBmzq2Ox3yAI7ZlWd0KAzTx4OEP0bFdv8FVE7lDL49K9j4jonHYW5pAJkVs6BduBy_uPKHO7KKx32XeP-D0SnfX3peEPt2JsuISK7Pg1bzS8Rog1IR57zur4kCDgbSlMTw-hm_1U75aqwsC3fgl8B425w0wyJsIjKkthbfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدید از لحظات اولیۀ حمله به مدرسۀ میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/677964" target="_blank">📅 11:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677963">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b89d160b92.mp4?token=NuVx6yJTbuGnGt6J0XbGl-PEp5LaRsDAczQ6pVLPZy62XtdcR49qjqFl2gp5Q8q43HXdi-QgBPl53y-W72AC673Y6feUXzCeU8DlBdTtsi3EvyuYajZf90EY674uVO0RA_hpLHV8o3VZh1jIiGMciz4bxq-1KoF9YTLB8RrG829rQLZMVM9IKZa2Js1w7D0gNGvjlgEBc14lfW8ZGo3kdOqSmC79GI9-57wX7PAIjfWRyMY11n0Ghr6g2gj1IWQAp7KuduqVCT5960Ykh7RRYgj91eC_-fqGpT_fgnocd9aMU8nEBoljme8cQjC8Q-hy0wus4PJhx6sVIZhy3G1Iyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b89d160b92.mp4?token=NuVx6yJTbuGnGt6J0XbGl-PEp5LaRsDAczQ6pVLPZy62XtdcR49qjqFl2gp5Q8q43HXdi-QgBPl53y-W72AC673Y6feUXzCeU8DlBdTtsi3EvyuYajZf90EY674uVO0RA_hpLHV8o3VZh1jIiGMciz4bxq-1KoF9YTLB8RrG829rQLZMVM9IKZa2Js1w7D0gNGvjlgEBc14lfW8ZGo3kdOqSmC79GI9-57wX7PAIjfWRyMY11n0Ghr6g2gj1IWQAp7KuduqVCT5960Ykh7RRYgj91eC_-fqGpT_fgnocd9aMU8nEBoljme8cQjC8Q-hy0wus4PJhx6sVIZhy3G1Iyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: اعلام موضوع سخنگوی وزارت خارجه نظر شخصی نیست
سخنگوی وزارت امورخارجه:
🔹
دستگاه دیپلماسی کشور مجاز به فانتزی سازی جنگ نیست. وزارت خارجه برای خوشایند جناح های سیاسی موضعش را تعدیل نمی کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/677963" target="_blank">📅 11:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677962">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG_6Xnh2sSWQhWiMT_t_P2jIPy3Bk2OY65eMAzrSY3mmZ6jtKUWXy63BV4k8qNbIV9lL--xJ1kBnmilamM0pWknUtXlfEJFcdn0Nr-vfP_EPBd_KSfjqlj2CObdfKSoG4Naw54ParktLjNbWR126Rb5loOi772s9vt5kop3ZUROzDNN41_8xJo3zmKEaN316Z_GgytgDJHfAkx3Dn98bywDgErcjhaB89hdT0m6ZuuJkF29XhCMMkQ4WT8SHOpee8ZctOxRaKgl8RzKfm7Kyuo8JsQzB4CdlG2cqPUbtR90C7yrWsyzoczg98aBMMYx7cUKFEa-0pi0VcPdLaQ8jkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای اسرائیلی: ایران، اگه بمب اتم داری، الان وقتشه. هوا انقدر بیرون گرمه که ما متوجه نمی‌شیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/677962" target="_blank">📅 11:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677961">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
بقائی: جنگ آمریکا علیه ایران، جنگ علیه امنیت کل منطقه است
🔹
بنابراین، طبیعی است که کشورهای منطقه بخواهند در راستای جلوگیری از تشدید تنش تلاش کنند. اما نهایتا این اقتدار ایران است که دشمن را از حمله به ما بازمی‌دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/677961" target="_blank">📅 11:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677960">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پاسخ سخنگوی وزارت خارجه به ادعای ترامپ دربارهٔ آغاز مذاکرات از امروز: امروز عراقچی راهی سفر اربعین است و باقی اعضای هیئت مذاکره‌کننده هم در ایران هستند!  بقایی:‌
🔹
چین با ما در خصوص اثر مخرب آمریکا در منطقه هم نظر است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/677960" target="_blank">📅 10:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677959">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973da53f7a.mp4?token=dg0Z13-N6jcW66YZu5rTHGM4yzOSxGClo_S_2P5YTYS1enbgr5qcN-oCER6hISNFb-aGzOI2_Vxp5Wv2ODgTJrod8e6vZmhnZjJmSnNZ0VlXeIuG5ipJ_tvTPSZVmklTDeS8o877wDUOL0nnyXPX-M7pUx61ulpUoliHb1mV-eku5carZ-Jpph4L13wkYe6QzWddOIYcNDrT0wedire-weH3Ybcaj4KXJhsM1-fGK_eFVSeI7EVc525jitMkeFjX9RA8MuhXVfUrZqFGNCzkXh0pWZB7eN1Ue06PDCxVI4uslgMvUSjpOOM2_0y9cgcEouR70siISmKHxD8EoicfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973da53f7a.mp4?token=dg0Z13-N6jcW66YZu5rTHGM4yzOSxGClo_S_2P5YTYS1enbgr5qcN-oCER6hISNFb-aGzOI2_Vxp5Wv2ODgTJrod8e6vZmhnZjJmSnNZ0VlXeIuG5ipJ_tvTPSZVmklTDeS8o877wDUOL0nnyXPX-M7pUx61ulpUoliHb1mV-eku5carZ-Jpph4L13wkYe6QzWddOIYcNDrT0wedire-weH3Ybcaj4KXJhsM1-fGK_eFVSeI7EVc525jitMkeFjX9RA8MuhXVfUrZqFGNCzkXh0pWZB7eN1Ue06PDCxVI4uslgMvUSjpOOM2_0y9cgcEouR70siISmKHxD8EoicfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ سخنگوی وزارت خارجه به ادعای ترامپ دربارهٔ آغاز مذاکرات از امروز: امروز عراقچی راهی سفر اربعین است و باقی اعضای هیئت مذاکره‌کننده هم در ایران هستند!
بقایی:‌
🔹
چین با ما در خصوص اثر مخرب آمریکا در منطقه هم نظر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/677959" target="_blank">📅 10:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677958">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما الان مذاکره‌ای با آمریکا نداریم
بقایی:
🔹
مذاکرات با عمان و متمرکز بر مسیری است که کشتیرانی ایمن از تنگه هرمز را تأمین کند. تلاش می‌کنیم در اولین فرصت با مشورت و همکاری عمان مسیر موقتی را تعیین کنیم که ایمنی کشتیرانی در تنگه هرمز فراهم شود.
🔹
بنابراین مذاکرات دو جانبه و بین دو دولت ساحلی است. حضور دیگران در این مذاکرات می‌تواند سازنده یا مخرب باشد اما موضوع بین ایران و عمان است.
🔹
تنگه هرمز به دلیل تجاوز آمریکا و رژیم صهیونیستی مسدود شده نه به دلیل اختلاف نظر ایران و عمان.
مادامی که تجاوز نظامی آمریکا و رژیم صهیونیستی و نقض تفاهم‌نامه ادامه داشته باشد تغییری در وضعیت تنگه هرمز ایجاد نخواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/677958" target="_blank">📅 10:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677957">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0d5058d2.mp4?token=cv42Z7bLpC-PvJBwCTd7unGbv_GrhsaWcJhVC7KY9-1NvE28mjm6pahE44CgUDlwgk3r6Ce_oQSuDBB1KDOHxy23yKxA2ST6G_1KE-hgh7FB2onWylEpcyU-odEazdMVdV9Rnn7MYn8GcnFuQUPcpicopa8ocBhSSUizN6A3m3r-fdy4z7pN5jMMkhTgZAcYf4QgxswJ8UktcUA0ax6g0nkbW4irBUDJeYuS7tRAK9Iv0kI-YXk86XjPrnTo9oEsZrd-1WptuM0eKcPbMNC4yDrUhdFmN6_-9tjbuHxHCOGsN31bhecDv_1k4SIic7ep9nPjAXbo5ab2nZDhMKulKbYpZVkDfNQQ7kky_FtcS8gHWtbNutie_8kbMrtXXmasu4rzxx2Am1WhONuecYeENELk33wiH2XSdsIFydnqvztpfTysk6kKcxD4RgavwU5TFeEpubjoX5iB85Hse4GCSkpiqB78og2DPFmULquPSG0MUc_en3oXWMt3yR4E7HERtx78iSN9GOfOp8_lxnrOl6eQRe4FHingptEoO84dMLNrkTSqaufTGgD9cdNXWL5892J39pSzXLrwCFCIUApOnCS2fOUSsOaGoMtzieu-uuyXaYkW47V_ro24fof7d7wAPzsOwEOK0rQ2dTGrg80lb0MWjPuCp7NsGYjcUgT3aZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0d5058d2.mp4?token=cv42Z7bLpC-PvJBwCTd7unGbv_GrhsaWcJhVC7KY9-1NvE28mjm6pahE44CgUDlwgk3r6Ce_oQSuDBB1KDOHxy23yKxA2ST6G_1KE-hgh7FB2onWylEpcyU-odEazdMVdV9Rnn7MYn8GcnFuQUPcpicopa8ocBhSSUizN6A3m3r-fdy4z7pN5jMMkhTgZAcYf4QgxswJ8UktcUA0ax6g0nkbW4irBUDJeYuS7tRAK9Iv0kI-YXk86XjPrnTo9oEsZrd-1WptuM0eKcPbMNC4yDrUhdFmN6_-9tjbuHxHCOGsN31bhecDv_1k4SIic7ep9nPjAXbo5ab2nZDhMKulKbYpZVkDfNQQ7kky_FtcS8gHWtbNutie_8kbMrtXXmasu4rzxx2Am1WhONuecYeENELk33wiH2XSdsIFydnqvztpfTysk6kKcxD4RgavwU5TFeEpubjoX5iB85Hse4GCSkpiqB78og2DPFmULquPSG0MUc_en3oXWMt3yR4E7HERtx78iSN9GOfOp8_lxnrOl6eQRe4FHingptEoO84dMLNrkTSqaufTGgD9cdNXWL5892J39pSzXLrwCFCIUApOnCS2fOUSsOaGoMtzieu-uuyXaYkW47V_ro24fof7d7wAPzsOwEOK0rQ2dTGrg80lb0MWjPuCp7NsGYjcUgT3aZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر: در کره جنوبی اگر کسی مطالبات غیرممکن و غیرواقع‌بینانه داشته باشد محاکمه می‌شود/ برخی برای رای بیشتر حرف‌های غیرواقع‌بینانه می‌زنند
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
مطالبات غیرممکن در دولت و مجلس و مجمع تشخیص و تریبون ائمه جمعه و غیره شنیده می‌شود.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/677957" target="_blank">📅 10:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677956">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
احتمال شنیده‌ شدن صدای انفجار در
اصفهان، امروز تا ساعت ۱۴
🔹
ادعای فایننشال تایمز: این ایران بود که برای آشتی با امارات پیش‌قدم شد
🔹
سی‌ان‌ان: دو سوم آمریکایی‌ها از دولت ترامپ ناراضی و به آن بدبین هستند
🔹
رئیس‌جمهور کلمبیا: سرائیل ۱.۸ میلیون رأی انتخابات کلمبیا را دستکاری کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/677956" target="_blank">📅 10:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677955">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای الجزیره: وزیر کشور پاکستان و طرف قطری نمایندگانی برای آغاز مذاکرات ایران و آمریکا اعزام خواهند کرد تا این روند هرچه سریع‌تر آغاز شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/677955" target="_blank">📅 10:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677954">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سدهای مهم کشور چقدر آب دارند؟
سخنگوی صنعت آب کشور:
🔹
متوسط پرشدگی سدهای کشور تا تاریخ ۱۱ مرداد ۵۸ درصد و این عدد برای تهران ۲۹ درصد و برای مشهد ۳ درصد است
🔹
لار ۷ درصد، طالقان ۵۴ درصد، لتیان ۶۵ درصد، ماملو ۱۴ درصد،  سد دوستی مشهد ۳ درصد، سد طرق ۷ درصد و زنجیره مجموعه سدهای کارون ۸۱ درصد پرشدگی آب دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/677954" target="_blank">📅 10:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677948">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5-hKwj0_FkA4W-uBH8p0NLmm0Mf4XtE5XrDqPe7urx2ATiTBvcKmQKW612wuIurOV2tc3q2HmowUfOFPOmC-0HM-KMVOLWtVH2_6rk5n6SX5XASWYWUv4H6CjWWAqsccWIHSs0bnwJCgnQS5N_1rt6eKZxlKJf-LYaEEnwR39b_JZbK88zfsFZoMU2TqNFTwUzmla0JUMZB4PjXXJ9i0ZYXnNK8LJQHuigBbyq3IGsg7FWmGuU3cLFvKG-qprw3x3tLNX-vWR0CTWbcDHZw2QxE3aPs_2-01M08ri1bF0u07D2TtfCuBjgjhkY3k9ofM8ilbs1a9mBQbZWqcoek1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxpmgQ0cROJdNl41ngrXOFs6UfBxWYSZUY3kNX0sj5RRUgHPJHeUtHH-7cCNwzD6ftlNWZ7BhQZyZt21aVBOC1TAR8szSFw6k5K5DrvlgyalGWrqz7xi5UA12PWymAdXNfb7XKc4Yoa2zHwJuq59a52l4qq1e2p2Ezg3NenmlBPqENQScDnT5LzrdKKG1U2gx-Bjhgn-g-qI_3xrUedTpCIHNxwwsZArPwrhYcsUEEdTYiLYnGBu2aWHf7DFi0-wkJ0TP1FoTbABcpF4kKirPl9OttHewhv-WTORYUm7I7X3V6seFv4h_isw3pxa1KMYp9XmwCeE6MEGWXeFDdnn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsrVhgRddsBs_yEsngoTVmpzwzjN4aiVqJJTEV48hJEobD0qjC2U9T_yJgCThaq6WtjlZvrfWi4jJnrm_aJMt5IxyLpDzqDc_bNtS0u9gFFgHa7dyr84-3n_Pq8yI1AcQG4ot_iFfHCQjXMFohzsSs8eHKMRHk1cfFReGBR2etfjj4t3GLPaGczmmHSoIygEqUkDhp4VvUHklXzpOUzt2yaylvZ--b3lI22t3ztWZH0PQmcyjXFkOeEUKaU5eAbft51Puvriw7g6cRcSTI18mL8s97JUCStpNeRSjRYNgqY5nE8rxRKSDfagDBkw0yP5pvBcFK5paR6ucbVPgmUdUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYDmJurMSw3hYeXPcWcXMna90au5eXR1SHxFyqRS6esSQTAbFF8205-dJZ3QcgHXGwD-QMcQomjAMGNWiKfi33217i4Np67yP3ulliyjdzKYXnrAilDaKZA-kANqPUn7SY0UfMluMmk3IZ4lTZ5vR7FioGQdOqUybAFtp6GHL-s5FUahHJyvNZP4trGirXmAI9JKmycPEf3ZXqRqUQfHhKroRCY3CXSqYyFBKHGkaa-9rLM3Z_lYFnk2XWZE__hz7lqhP4F6nPUz12BMq8Xsi0trB1q124jbRolsaXs5JvoV4nwGGBZtdZ74bEgMujwWwt_82r2ieAoC-W2i6754Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4tvByEKm-l3BMrgUKEExfSV-ZN47zrR2J6ekfaBkjJKVtIDv3_qBZQ5heWO4xmAmaqSuRGtbxrgKrx8-jSHGjxtw1ppjqErsHVVGg8Qg_FMSs0etdnelnqV__hE2NiNurJwVTn5Q0X3GVqBSKXH1kHz4LA__SlR051i6A3E1HxAqXyA-80-ny2-v4pTjV1wdmfmLmWGdweLlPxnYTWX5-sXscOwtne4m-3coEHh7uKRGjCp9Nn0V6D-4-0mTiFfpkajdZJjOJEhMfC6haQnkueMZ8J3_Stl6rWAehZrIoH96vAVYORd23UWwX3ccUO-cezM9wChM6Q-o_znXSSyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AY0hLBoK8FIw3BVP4em6kxTA1gnXGFm9T7tlQmRjjvVOksqCnjFEVrdVkBHSlnigCCWr1blHF3U6f5zZWhI6vaLXT4FtC3INr9DY4CcUjYISVPkcoiWG7QlXKZRJjGWEqb09FXdaN291ulUu0N0TVkacJoD2tJf_HcSz3MbwbgjCLZSHqTd3fMI3MINylLiXBCfELJ7l5JcKmPKjjFNyeOK3NIrNWEOgxi7hT1gVT59-OcKsvQRivlzGgJdba5fFNdSqEwRjZTMne8utbT_VQ9w5CCxFuRvk9bc3UNuxXQn478cwuhQ1wzRSRdQZoPHiyJB_SrHrYUw1gAEGTj0hbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هوایی از حجم تخریب آتش‌سوزی‌های گسترده در ایالت واشنگتن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/677948" target="_blank">📅 10:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677947">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ffcd59a9.mp4?token=Z5Zb268XMFNSwgO53sjC_3u-N7FxnptTsPXY_Cvfc1dxlsEXfsXjfZz8aVFb88crSrXgJ9ZWLAOPlanQ42kMoXThfE7WOY77yheLYclCQkujYy7f7Awl4EiRAvxavsnQzwSfvQy0sy2ZcjZ_iFf_5BUtKPvE2AkINzMO40j4IZ-Q6TXP7sOYEaPwE6_L7frpvYaYMg8lRzYCSjYVZV4-ywRHyFZDNRV0RVFXD0Oj1F8eYkL_bkVGcg8218bYwP6aNwenCzv1f3xWyYbcrbOvWCzD1PeIauQ-EZxqVjcY-cLVPcDGY0p6JaG1ZkEGphC4rP-JExREHIDWtWGvu1WyRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ffcd59a9.mp4?token=Z5Zb268XMFNSwgO53sjC_3u-N7FxnptTsPXY_Cvfc1dxlsEXfsXjfZz8aVFb88crSrXgJ9ZWLAOPlanQ42kMoXThfE7WOY77yheLYclCQkujYy7f7Awl4EiRAvxavsnQzwSfvQy0sy2ZcjZ_iFf_5BUtKPvE2AkINzMO40j4IZ-Q6TXP7sOYEaPwE6_L7frpvYaYMg8lRzYCSjYVZV4-ywRHyFZDNRV0RVFXD0Oj1F8eYkL_bkVGcg8218bYwP6aNwenCzv1f3xWyYbcrbOvWCzD1PeIauQ-EZxqVjcY-cLVPcDGY0p6JaG1ZkEGphC4rP-JExREHIDWtWGvu1WyRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در بخشی از مسجد جامع اموی در دمشق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/677947" target="_blank">📅 10:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni5e9YrzMx4As1orzGRYlvuDy-useBA9tqDXziM7eCrCwFM8vhfN6v1gvCxXpBMjHNawx-xFtNi4CtwUpONTjWammE-sEr3YoanTFin6fYakakV60Ar9X9jfgF5peEVVdPCovOisC5nm31MwWDfJW_k-Ag0ZXzgvHrPDWD0MZ4Mn732K35d-jPYVgBEDg8jW4-UXHJ_B833xdu2RL8AorJGXL2dsLhMwzA7Bdz1Hk6ENvDWwlVoh7Ld1_P2swJnAz5be9MOg5N0v2lowuSdVeMjWTCvf3eYMmXTHQUEib_TmBVYWqE_j_mZliHCicQ3bC3v7HnXya9XigYY19bVZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به لطف هوش مصنوعی؛
خوک هار خودش را به قاب واشنگتن و لینکلن رساند؛ رؤیایی که با واقعیت فاصله دارد
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/677946" target="_blank">📅 10:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS_nzSTQfV-j4o168nbOWXAyEifFhN1adG3qRc8wZaoCuSVW2HdOEVZuekTc2lf6QOjIUsQe7EEQrbn8gOAmsl8U0bg9w1HJHo9H1D6yUyT7feW4Cjujcq-uXdj0OKCD9UoR_zUnkr0tdmitP5-6xzaVA0br-GDqpIKUU3havgwjGrZH5JEydFqz3rpS_9R-2iMMniHOKESoMd1OQQmFX2A0kli_8EkRE6KTROl1IRwSa7Z7sovTuRAR_fQlQEhafL153uSJoqcWLOZhzPhxbZvUzj2Miw99_uNYinafuVc_CzNknq040uEH-UrLneHGkRWjTT70-pnc4x2m67evCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سواد رسانه‌ای در شرایط جنگی
🔹
سه توصیه برای استفاده بهتر از رسانه‌ها و خواندن اخبار در روزهایی که دشمن سعی می‌کند با اخبار ذهن‌ها را محاصره کند و فریب دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/677945" target="_blank">📅 10:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e0c8c52e8.mp4?token=ShFi6427adjI9hjtnPOoiQgf_kqG4KbpeDwRiUkZ_gVLxGiGZBakcxWNxVyLFTv7JpIeng3B7_H7Ot_BfQZdssc7lC3xrI0MTStB0uUhauMgm8P9hg6-6UbRm0FKCNP11lGtzQhPwh-IHe492EQboUsvQQfDxyGRt42Tf8iFTcBz6hHwZ8AM_8-Yd-6g5PWUu8iqEO6p78Kw-8YIWz9IPnTTyK8stRMQYLnYaePz1UoxSoD2vD2dsStFRe2nkHd6E-hv_Qb7-axCrOvnGuLt8wBaU_2zKGME-U4rs1s7ayvzTMNkhPYqU4bJARDW8vPytPMo3VBy_jQmlwPtpRTI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e0c8c52e8.mp4?token=ShFi6427adjI9hjtnPOoiQgf_kqG4KbpeDwRiUkZ_gVLxGiGZBakcxWNxVyLFTv7JpIeng3B7_H7Ot_BfQZdssc7lC3xrI0MTStB0uUhauMgm8P9hg6-6UbRm0FKCNP11lGtzQhPwh-IHe492EQboUsvQQfDxyGRt42Tf8iFTcBz6hHwZ8AM_8-Yd-6g5PWUu8iqEO6p78Kw-8YIWz9IPnTTyK8stRMQYLnYaePz1UoxSoD2vD2dsStFRe2nkHd6E-hv_Qb7-axCrOvnGuLt8wBaU_2zKGME-U4rs1s7ayvzTMNkhPYqU4bJARDW8vPytPMo3VBy_jQmlwPtpRTI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کافیه این پاستا رو یک بار درست کنی تا بشه پای ثابت مهمونی‌ها
🍝
🤩
مواد لازم
🔹
پاستا پنه نصف بسته
🔹
گوجه ۵عدد
🔹
سیر چهارحبه
🔹
رب یک قاشق غذاخوری
🔹
پنیرپیتزا
🔹
خامه دوقاشق غذاخوری
🔹
نمک، فلفل‌سیاه ‌و اویشن #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/677944" target="_blank">📅 09:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf841033b.mp4?token=Tyk6ndNwdwEJ2hAXVwkuOWeNtmeL9nkjCY7b-81lhfmrM4YCWc_HGBbAhxTWf2r6dCYt9qo8rcE-SoK73coQPQ7sS7Vvi9O34kUENbW6OLbqc_sfg-q7UKLflk5tI7sxrnJYexseOPw89GnoU9SJrbdPeZpv-hgloE1AMZFsHnHLToyVQt37bcIIJYuYid3dBRVzwUC1jt_HGActO2isbiPZTU1yKLSRd06BRpT5eyK32khCpJoI1iBGoU6-xCH_Cp-uBruIz5wvvbMeskXQUf7EZt8ANuuXeLZh9DLNi66tnqmwINqKuhr8qXa7hsedalzjCaBwAAgHVM6Ch3c524i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf841033b.mp4?token=Tyk6ndNwdwEJ2hAXVwkuOWeNtmeL9nkjCY7b-81lhfmrM4YCWc_HGBbAhxTWf2r6dCYt9qo8rcE-SoK73coQPQ7sS7Vvi9O34kUENbW6OLbqc_sfg-q7UKLflk5tI7sxrnJYexseOPw89GnoU9SJrbdPeZpv-hgloE1AMZFsHnHLToyVQt37bcIIJYuYid3dBRVzwUC1jt_HGActO2isbiPZTU1yKLSRd06BRpT5eyK32khCpJoI1iBGoU6-xCH_Cp-uBruIz5wvvbMeskXQUf7EZt8ANuuXeLZh9DLNi66tnqmwINqKuhr8qXa7hsedalzjCaBwAAgHVM6Ch3c524i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توزیع شاهد ۱۳۶ به موکب کویتی‌ها
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/677943" target="_blank">📅 09:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677941">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a087ef7e4.mp4?token=gbsh-Wm2mirbC9XBLUc8vwoXC8dVCcdS2zvHEQR4TG2YfOXjlnw4lqSzZhIZye-CI4qGDEJlT9XD6oFlLNPpypqcx0vO-GiWOVuLyeuuySIXfTkkZfSrOtp8KWy6n0xVYWleA8yMhWn_tQCGtS3UjfSx8P-QlM8HpGFpf7MOBkEjWT__8O_getd_Zgu6whI6fc7J6J7xCzAhtsWIARMX6rgsb0Eux1CJs_5q1orjK1MSRdpiL6zE603r4eqWj2f7TakvW8ooRoMYqfSnB3EkoYT3LhZrxKSQ1sQIvZXETas0OfqZOMQ1Gc2IWqnVtF6vlG30jxKUKCVLlX02qKK4J72cffLV9lkw4af9ht7Ft_9-7xCZR7yjKLyeHKR61PA9_v9AGfhhtvuMlCN57uICfZkAO9YTqCxAkFJES3xJh1J4uR_NZGL4CFs8qkmrfM4cupQwFmHcgnxgtNfA4NPTs7MW1p4HprRHujKATYqVMQhds0gtb-WThKOcDZVFKnXxSkuCZ9r3_b0ZC3-M7fCC6c6BxG30ioKUi8ORcP5FRF_-A1DlzfhRM0vUJlEcMEnSl9tAkIgLAQQx_knYWlFCj9r9fPBdZ5MvZQi6Ry8-zmq0vvdiTE4J3-B17uM1oNC4hB-IH0dNWJDrN_lLdxFpvy1w0xdBPFhfw_prdW1MHjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a087ef7e4.mp4?token=gbsh-Wm2mirbC9XBLUc8vwoXC8dVCcdS2zvHEQR4TG2YfOXjlnw4lqSzZhIZye-CI4qGDEJlT9XD6oFlLNPpypqcx0vO-GiWOVuLyeuuySIXfTkkZfSrOtp8KWy6n0xVYWleA8yMhWn_tQCGtS3UjfSx8P-QlM8HpGFpf7MOBkEjWT__8O_getd_Zgu6whI6fc7J6J7xCzAhtsWIARMX6rgsb0Eux1CJs_5q1orjK1MSRdpiL6zE603r4eqWj2f7TakvW8ooRoMYqfSnB3EkoYT3LhZrxKSQ1sQIvZXETas0OfqZOMQ1Gc2IWqnVtF6vlG30jxKUKCVLlX02qKK4J72cffLV9lkw4af9ht7Ft_9-7xCZR7yjKLyeHKR61PA9_v9AGfhhtvuMlCN57uICfZkAO9YTqCxAkFJES3xJh1J4uR_NZGL4CFs8qkmrfM4cupQwFmHcgnxgtNfA4NPTs7MW1p4HprRHujKATYqVMQhds0gtb-WThKOcDZVFKnXxSkuCZ9r3_b0ZC3-M7fCC6c6BxG30ioKUi8ORcP5FRF_-A1DlzfhRM0vUJlEcMEnSl9tAkIgLAQQx_knYWlFCj9r9fPBdZ5MvZQi6Ry8-zmq0vvdiTE4J3-B17uM1oNC4hB-IH0dNWJDrN_lLdxFpvy1w0xdBPFhfw_prdW1MHjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در انبار لاستیک و خمیر کاغذ در چین
🔹
آتش‌سوزی گسترده‌ای در انباری در شهر چینگدائو چین رخ داد؛ این حادثه تلفات جانی نداشت و علت آتش‌سوزی در دست بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/677941" target="_blank">📅 09:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677939">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شارژ کالابرگ جدید از ۱۵ مرداد
🔹
مرحله جدید کالابرگ از ۱۵ مرداد برای افراد با کد ملی پایان‌یافته به ۰، ۱ و ۲ آغاز می‌شود و سایر افراد در روزهای ۲۰ و ۲۵ مرداد شارژ خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/677939" target="_blank">📅 09:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677938">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/677938" target="_blank">📅 09:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677937">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thM4X9Z-1wvSPj1XkZJC69TH80kNHInRIoQ48UhpdUVd_t5NFaBqKFxDuHW2WEKOGec5MZou9drt3Lwv-6-QCSaIju8z2VtmdkKwkPDf8yNJrFK-pEbLAbyexBcU5qH_Kpday91FW5PlLABeNcEJ0Z0qCxyHJ9vewb3EnO7_rva_4xn5FxH51b6ePal7BiiNWtf0LHG4YJvXF_bed1G4IAZzM9wkbVZpJhUAfXcGQSrRFbcv3wYBGuTviEgFz-SXYpQfpKuLETa4bsiO7c0D_SzFIgzpszYMngoctt2nAxoSBkGHlOrRAI4qnCs3w2bVDXbcPTE6hKdTziv5YI9X8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس سبزپوش شد، شاخص ۵.۲ میلیون واحدی
🔹
شاخص کل بورس تهران با رشد ۱۱۷ هزار واحدی، کانال ۵.۲ میلیون واحد را پس گرفت شاخص هم وزن نیز ۳۰ هزار واحد مثبت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/677937" target="_blank">📅 09:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677936">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69db2d51d5.mp4?token=RmIfWlrQ3WzKxsaA3buKxi-7I1KHWFKhhUxA_ISOEGCEEbwvlE2Kv2_LWMfCloAEid6Nv5X-p4j5j8yv1Yxa4K_uxKcZxm4kVK_Q_vDluEiHtSr2kEsTYRbG9YVIt8BYz5s00wkX7GwW4AsxoqN2HVNdJ-aX9aH0xEoH5mcLEYYBMYMdyH3Dc8EFwjRA3eifRRrsyIzPpgf6KZ3X9mn_XNsz11mBJ8kH7CpFJw7QK12nHR80mGLrrWb-HpXjHJOE8TiDcGyrB148Flr-o4UqWT5-Mj6ZVk_3Sseu_1OFuPUw6dZbcBrCBXc1KuXVm4pfaFGhWSfVe373ZrOUw5paSn2k6OQXvMiVQPkjaQMJY-Uxml4LJj0miYd2gBzt9bmrctg23V_IVn6Mw_F3u0GXsxOKYA8mRDZkz-e_jT58u0Qc3sNcaaw7f1QBzXrlTQjzDdoxC-_PPTIRACH8YL4V5jBjc8bFhHsjFS4shXNWKu4XS4PoEZLeXvdmJXl4rjT_G5msoXZQ0XmTb0eAB4XHFi3j1yoEJOrnxSLLSgcCeqJKwHlDOHo0b1yUjedzjmbqSvoq83_RnNEI75vlOiMnuLiimQeKaMA1QOAC7ZsSbhX2UEVfnQpZSmLmvm-QLNgyOIRsDraOyZnxJ0Ne4s_Nw09Re6_Scz5DD7F1p6al4dI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69db2d51d5.mp4?token=RmIfWlrQ3WzKxsaA3buKxi-7I1KHWFKhhUxA_ISOEGCEEbwvlE2Kv2_LWMfCloAEid6Nv5X-p4j5j8yv1Yxa4K_uxKcZxm4kVK_Q_vDluEiHtSr2kEsTYRbG9YVIt8BYz5s00wkX7GwW4AsxoqN2HVNdJ-aX9aH0xEoH5mcLEYYBMYMdyH3Dc8EFwjRA3eifRRrsyIzPpgf6KZ3X9mn_XNsz11mBJ8kH7CpFJw7QK12nHR80mGLrrWb-HpXjHJOE8TiDcGyrB148Flr-o4UqWT5-Mj6ZVk_3Sseu_1OFuPUw6dZbcBrCBXc1KuXVm4pfaFGhWSfVe373ZrOUw5paSn2k6OQXvMiVQPkjaQMJY-Uxml4LJj0miYd2gBzt9bmrctg23V_IVn6Mw_F3u0GXsxOKYA8mRDZkz-e_jT58u0Qc3sNcaaw7f1QBzXrlTQjzDdoxC-_PPTIRACH8YL4V5jBjc8bFhHsjFS4shXNWKu4XS4PoEZLeXvdmJXl4rjT_G5msoXZQ0XmTb0eAB4XHFi3j1yoEJOrnxSLLSgcCeqJKwHlDOHo0b1yUjedzjmbqSvoq83_RnNEI75vlOiMnuLiimQeKaMA1QOAC7ZsSbhX2UEVfnQpZSmLmvm-QLNgyOIRsDraOyZnxJ0Ne4s_Nw09Re6_Scz5DD7F1p6al4dI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲ عامل موساد اعدام شدند
🔹
امید بهزاد و پوریا صفوت، به جرم همکاری اطلاعاتی با رژیم صهیونیستی و ارسال مختصات و اطلاعات مراکز نظامی و امنیتی، بامداد امروز پس از طی مراحل قانونی و تأیید دیوان عالی کشور اعدام شدند.
🔹
این افراد در جریان جنگ رمضان و جنگ ۱۲ روزه…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/677936" target="_blank">📅 09:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677935">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
راه‌پیمایی ۴۵ هزار نفری مردم شهر دیربورن ایالت میشیگان به مناسبت روز اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/677935" target="_blank">📅 09:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677934">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
محمدرضا باهنر: ظرف ۸ سال گذشته متوسط قیمت‌ها ۱۰ برابر شده/ برای بازسازی خسارات ناشی از جنگ عددهای مختلفی از ۲۰ یا ۳۰ میلیارد دلار می‌گویند، عدم‌النفع را اگر بخواهیم اضافه کنیم تا ۲۰۰ میلیارد دلار هم می‌گویند
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
اقتصاد مقاومتی را ۲۰ سال پیش در مجمع تشخیص مصلحت نظام تصویب کردیم و آقا هم ابلاغ کردند، اما خبری نیست. رهبری به اندازه مسئولیت‌هایش ساختار حکومتی ندارد؛ یعنی رهبری یک چیزی به رییس‌جمهور بگوید، رییس‌جمهور می‌گوید من رای مردم را گرفتم.
🔹
امام شهید ۲۰ سال قبل فرمودند کرسی‌های آزاداندیشی در دانشگاه‌ها راه بیفتد، اما به دیوار خورد. مردم باید بتوانند قانون را نقد کنند و بگویند این قانون بدرد نمی‌خورد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/677934" target="_blank">📅 09:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677933">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fecca349a8.mp4?token=Gz16OyAWbcHDhSzyZLoYy0bHeH0qhoPt1pf9eit_D7APlspC_t0lFOjhNqDaugikH6HkP3fYvh6RRTy6Lb1iMx6p0rXv_Md1Eku3LQuSWYRSDICmOupmx8iN1pRMaiKRoHlK_vBZr8gR95wcsxrt7-GZ7ZjOpYLqp2XvDnvppCUQPJZ8PoxgymkC5hvU53gfbjJLVrcWYmX6mhLjN3efJBaTU2Ad9HYL0jnYISn3RrCjr7iErWjAUV9HM7AymyiMhb9TiIWNslQpjkU4t0mVC5VJeU2ereFJE7_FWRT6HFZviH7N3eGOu0a8FTnEjY1_4Wgc2jQoNo2GYISOGyXWtTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fecca349a8.mp4?token=Gz16OyAWbcHDhSzyZLoYy0bHeH0qhoPt1pf9eit_D7APlspC_t0lFOjhNqDaugikH6HkP3fYvh6RRTy6Lb1iMx6p0rXv_Md1Eku3LQuSWYRSDICmOupmx8iN1pRMaiKRoHlK_vBZr8gR95wcsxrt7-GZ7ZjOpYLqp2XvDnvppCUQPJZ8PoxgymkC5hvU53gfbjJLVrcWYmX6mhLjN3efJBaTU2Ad9HYL0jnYISn3RrCjr7iErWjAUV9HM7AymyiMhb9TiIWNslQpjkU4t0mVC5VJeU2ereFJE7_FWRT6HFZviH7N3eGOu0a8FTnEjY1_4Wgc2jQoNo2GYISOGyXWtTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روز عادی در ایستگاه‌های قطار بنگلادش!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/677933" target="_blank">📅 08:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677930">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FP69l-m2eXufY-L5reVl_k5Q2Mobs_FfoIyBzGjQKIpWMqrjluIyURXVd9bDE_nJ0pRhmh1Hh-j3mGEigMqUc0hpgsdQ5_7yPS9xn8ODxBGmU7io92M_V-sUbm1RnW_-x37_K16YCXomPtjRbcvGbgyb8nADOcCwu4wP3Fr3GhfItpz298T2qeCyLrJVLMzoFSypnuPOal0FbV2KoLYHckF0XdSvriSFv5W9mYAHJ7WDcCWlI8M2gSzzoXJLD6OsJJe4aKKKcBV1hLQHlLNHZr7pS2xkOen3SlQ3p4JgwO4aOHwYhu1JPto--wk975-aaBwmP4rUNColS3o14rG8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مریم همتیان بازیگر سینما و تئاتر درگذشت
🔹
مریم همتیان، بازیگر سینما و تئاتر پس از ۲ سال مبارزه با بیماری سرطان روز گذشته ۱۱ مرداد در ۳۳ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/677930" target="_blank">📅 08:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677929">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
۲ عامل موساد اعدام شدند
🔹
امید بهزاد و پوریا صفوت، به جرم همکاری اطلاعاتی با رژیم صهیونیستی و ارسال مختصات و اطلاعات مراکز نظامی و امنیتی، بامداد امروز پس از طی مراحل قانونی و تأیید دیوان عالی کشور اعدام شدند.
🔹
این افراد در جریان جنگ رمضان و جنگ ۱۲ روزه با کانال‌های وابسته به موساد و شبکه اینترنشنال همکاری اطلاعاتی داشته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/677929" target="_blank">📅 08:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677928">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سنگ‌پرانی نیروهای مراکشی به شهروندان بازگشته از سئوتا
🔹
یک کانال اسپانیایی مدعی شده است که نیروهای مراکشی با پرتاب سنگ، مانع ورود شهروندان مراکشیِ بازگشته از منطقه سئوتا به خاک مراکش شده‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/677928" target="_blank">📅 08:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677926">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5b990f55e.mp4?token=cqbqQjNHrRSW493P11uZnLVe-5CEtr_Nr4FEobG9gkVITOukfiDG034_7BLdgj9Oc_CBrF7j3qJiymw_vFu7V99IT_Na-2w5As48K8buzYWKoD6Uf178tbfcEfXTpZXYJGLZIuadnQU8C39hyVMHtunJ6Odblr4-55Kb8s8lzldqew2eSMtjXbMcsL025Jj9VghwSBE72PsulPKCcI_sKyPLCZM2IjcP_crEzPhnw0CFSyg_psCxu4Y8C3SIhk94FGosiqfeAmR_IzFr0Qb5MTljK5LeMWH7viNVdn-eWL4qTMU7brpNVK8-0N8jUcVkvJFWCg-WyaLM4bleoGc7HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5b990f55e.mp4?token=cqbqQjNHrRSW493P11uZnLVe-5CEtr_Nr4FEobG9gkVITOukfiDG034_7BLdgj9Oc_CBrF7j3qJiymw_vFu7V99IT_Na-2w5As48K8buzYWKoD6Uf178tbfcEfXTpZXYJGLZIuadnQU8C39hyVMHtunJ6Odblr4-55Kb8s8lzldqew2eSMtjXbMcsL025Jj9VghwSBE72PsulPKCcI_sKyPLCZM2IjcP_crEzPhnw0CFSyg_psCxu4Y8C3SIhk94FGosiqfeAmR_IzFr0Qb5MTljK5LeMWH7viNVdn-eWL4qTMU7brpNVK8-0N8jUcVkvJFWCg-WyaLM4bleoGc7HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای داشتن عضلات قوی شکم حتما این حرکات تو خانه انجام بده #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/677926" target="_blank">📅 08:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677925">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664e4ad0a6.mp4?token=fj8vuVVdo4LRnnp9UGnS0GYF58GzHTpCm1kCthmSrAYlzNe3SAudV-Onk1rhGDejrla8vkMS3UEfL1XqTmURbD3pKTcLpgKwIH1CGMKzDKa7ZO1aMMjCmzqJ_1Ibopa_EVcX9o0MzI5nHaia-0fKmuWu2Hxpz6r3Oaa_V2lY5r8QOJWmTGV7FN2b92T1LTtDN8Vf5f39Cz406aZAwn5EnuolbsjLgwuNJGI3QHKmxyfKtkKYSpYKWAmrFMpo-OHSMWpY8Uh1nxrVkw1SxdU2DvAcbJ7orttsO1DhMXJ-nQfQUYoVwoK00qTxcMZj1FKpzQ_TnoupmLgw7iC3HJpaBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664e4ad0a6.mp4?token=fj8vuVVdo4LRnnp9UGnS0GYF58GzHTpCm1kCthmSrAYlzNe3SAudV-Onk1rhGDejrla8vkMS3UEfL1XqTmURbD3pKTcLpgKwIH1CGMKzDKa7ZO1aMMjCmzqJ_1Ibopa_EVcX9o0MzI5nHaia-0fKmuWu2Hxpz6r3Oaa_V2lY5r8QOJWmTGV7FN2b92T1LTtDN8Vf5f39Cz406aZAwn5EnuolbsjLgwuNJGI3QHKmxyfKtkKYSpYKWAmrFMpo-OHSMWpY8Uh1nxrVkw1SxdU2DvAcbJ7orttsO1DhMXJ-nQfQUYoVwoK00qTxcMZj1FKpzQ_TnoupmLgw7iC3HJpaBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مارمولک غول‌پیکر وارد فروشگاهی در تایلند شد
🔹
مارمولک مانیتور ۱.۸ متری وارد فروشگاهی در تایلند شد و با بالا رفتن از قفسه‌ها، باعث ترس مشتریان شد؛ نیروهای حیات‌وحش این حیوان را بدون آسیب از فروشگاه خارج کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/677925" target="_blank">📅 08:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677923">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn6ci2HnOZbfwvUkKqFslDBc0jXMjiFC7G6-hZKTgpE_2wKfjSGvLIeApHpVlosrCmAwx6pmp54dKs7LHi8aSm-UPX7x0zV_t5c7_gqBUZ6hx9TxxDYoFHtLsrIuREdmqHlqFKtHH69koDcCpXB28RkxUFwK4o1FeN30AZ5RcJ9yg6X0Jy80jPNm53I8iHbwrFvDm0bBC_ToD0FuVYTpZDIrcOVF81ka5p98ljawD_8IneNnpWWb_Z1Bzwsy5RB2kkSqUruX8GyFHhVqGTbiXGdUyehggg5b1vA4DIQRdYDvCglsTr5CPaa1oU44QJffcICJu4IkWfQD3jawWS4G_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش شدید قیمت نفت برنت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/677923" target="_blank">📅 07:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677922">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzSiw0p249vXJts2Jm43sUrJRd0YXBD3rnakhd7ltgfj1Xboa_HlClPfGFjaQelVdlQfI6OyNsm5ThQE6pr5roDFXZiRPR7qUjzYL0nr6fmpjeVPdArEtZY7EsRkVF6sx6zTLou4kxAbLNXbGSq0ee4RIpz7x_UgzkrTYY7IU99fulCClvq39T-j0H_NpOqpMYVBJO-9CSPwzMXD-QKSw8ZeR_F7ieHQYagpXiKJs_8MBnjbegno7VkR3Bqj3Nlh9QGhY814T_EBvQ5nsxDfh4HCfYrqjfAmxP094I9lG2gQAzfw0wGpZLuJbp6OqsQbxmPzQzgF6PU3cAgYhxXw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱۲ مرداد ماه
۱۹ صفر ‌‌۱۴۴۸
۳ آگوست ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/677922" target="_blank">📅 07:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677919">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای جدید وزیر جنگ آمریکا درباره ایران
🔹
«پیت هگست» در اظهاراتی گستاخانه، از آمادگی کامل ماشین جنگی این کشور برای تهاجم نظامی علیه ایران خبر داد و مدعی شد: توان نظامی فعلی آمریکا در سطحی بی‌سابقه از زمان جنگ جهانی دوم قرار دارد!
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/677919" target="_blank">📅 07:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677918">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سقوط قیمت نفت پس از لغو حمله
🔹
به گزارش رویترز، پس از لغو حملات ترامپ به ایران با هدف هموار کردن راه برای توافق، قیمت نفت بیش از ۶ درصد کاهش یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/677918" target="_blank">📅 03:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677917">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from📚مجتمع آموزشي غيردولتي كيان مشهد📚</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK5Ng3BN-W2j4vFFyhDcGz_3A23zEB3wFhIYGmovnQbQqRSje2hiwOonzTpIPbmgjTfgcvWso3IAeGo3lTZY_OcmwuKTzFOklwiPXnExB0kVzZST-KFmShVfVszY9sm2JzGJRMbkq7VHSLIoWQ9CIOJE0L0s8zTnacLobH_7O6xBSvQNkZGkixAoDHLZE-LUF90cwJqu8qKLEJvKnlozxQQ1Gcn7izOLaOUzdI2clk8TzrmheRE_VuzO9UNehkX9i-OFmoJgOdr73O2VkPaZLPvVE__rG6nqC5uM_DXAAL7orfeH03y2u9O1HpF_fMaIFKDXizBo3ivxu1WYusm1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#
مشهد
💎
خانواده بزرگ آموزشی کیان
💎
📚
ثبت نام مدارس غیردولتی کیان ویژه پایه‌های
اول تا چهارم
،
چهارم تا ششم
،
هفتم‌ تا
نهم
،
دهم تا دوازدهم
آغاز شد:
🔹
(بر روی پایه و مقطع مورد نظر کلیک فرمایید)
🥇
غیردولتی اول استان خراسان رضوی در کنکور و دوره اول‌متوسطه
⏳
لطفا بر روی مرکز مورد نظر جهت کسب اطلاعات بیشتر
#کلیک
فرمایید:
👇🏼
مدارس کیان (پایه های اول تا دوازدهم
)
کلاس های کنکور و تیزهوشان
سالن مطالعه و مشاوره
ثبت نام نهایی مدارس
💡
اینستاگرام
💡
اطلاعات بیشتر
📲
📍
دفتر مرکزی: فلسطین ۳
05138414444
📞
09155100510
📱
موسس:خدادادی
09154440510
📱</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/677917" target="_blank">📅 02:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سگ زرد: شما نمی‌دانید این حملات به کجا ختم می‌شود. منظورم این است که آیا همسایگان ایران با موج گسترده مردمی روبه‌رو خواهند شد که به کشورهایشان سرازیر می‌شوند؟
🔹
این یک فاجعه است. اتفاقات بد زیادی ممکن است رخ دهد.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/677914" target="_blank">📅 01:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677912">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
خوک زرد درباره ایران: گروهی از مردم هستند که آرزو می کنند من این کار را انجام دهم - به سادگی بمباران کنم - و گروه دیگری از مردم هستند که نمی خواهند من این کار را انجام دهم
🔹
خبرنگار: آیا ایران مهلتی برای دستیابی به توافق دارد؟
🔹
سگ زرد: خواهیم دید. من سعی…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/677912" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677911">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سگ زرد درباره ایران: عربستان سعودی، امارات و قطر همگی از من خواسته اند که حملات را به تعویق بیندازم
🔹
این یک حمله بزرگ بود.
🔹
وقتی متفقین درخواست تعویق کردند، باید بگویید: باشه، ببینیم
🔹
خبرنگار: در مورد ایران، الان چه اتفاقی خواهد افتاد؟
🔹
خوک کثیف: ما با…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/677911" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677910">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سگ زرد درباره ایران: عربستان سعودی، امارات و قطر همگی از من خواسته اند که حملات را به تعویق بیندازم
🔹
این یک حمله بزرگ بود.
🔹
وقتی متفقین درخواست تعویق کردند، باید بگویید: باشه، ببینیم
🔹
خبرنگار: در مورد ایران، الان چه اتفاقی خواهد افتاد؟
🔹
خوک کثیف: ما با آنها صحبت می کنیم. مذاکرات فردا بعدازظهر آغاز خواهد شد. این باعث نجات جان بسیاری خواهد شد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/677910" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677907">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198c9fbfab.mp4?token=t06CknhaJ33Z3IMnSHtp_kfNU4Vl98lpacvAWhiYSZMAL1_zSgUsFJxnjuRvFXy8EEGGpbyHl52qWnTvCk73XXE-m6ImcmeR6ey9s8PXezsL5x7l2nsnL3EqDkd-krKHCZzhfr0MiTJJ2AEyNHj1w23uS1-JN9L4bzjmiCpGsmpLdETu_8SeukgcdOMeJpiq-QIE8B1_I8vYo4M5Bqgy82Bibuffbx9MR_me0cAI2Tv62QRYyz2iUg1pLIlwtZmvEBIy64VIh5vbRdV_iY0n8NtqYuRIAHwqCu-fSRzT2_7chzDmxSzRIut0HlDhMDSbP67T9_tleZPP5zF6PFGaXqCB4JxcWKLc8k5bnl4uTPwaVCD0Rubdb4FwSbpD5VrRoaa0JqnqTF4_nvtiQo1CKfwVKehv9QI1VkcFq9q_hsvIq0MQBBxODQozOBO6O4Uwco_6i1wq-zilEC9IxrcXp94W2XwC6vTRu23RC7SwHfUMugaZ_EWFzia8_YcRkEAzRDdjyFzHJ7179pU-_UQZvFy1jfW9YlMkOzwVJ5B45w2RqRIVEggrgq4KLBW1sFiaLHN9i49vRd0IfiiKKKVf6R98VypVQvzpzuyRJp0fHnkvT8k7cayECxrU_dJKc6VXtgz1Em6N2O6S7YRUZjf92XhzuID9olPW1pdvs5V3B8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198c9fbfab.mp4?token=t06CknhaJ33Z3IMnSHtp_kfNU4Vl98lpacvAWhiYSZMAL1_zSgUsFJxnjuRvFXy8EEGGpbyHl52qWnTvCk73XXE-m6ImcmeR6ey9s8PXezsL5x7l2nsnL3EqDkd-krKHCZzhfr0MiTJJ2AEyNHj1w23uS1-JN9L4bzjmiCpGsmpLdETu_8SeukgcdOMeJpiq-QIE8B1_I8vYo4M5Bqgy82Bibuffbx9MR_me0cAI2Tv62QRYyz2iUg1pLIlwtZmvEBIy64VIh5vbRdV_iY0n8NtqYuRIAHwqCu-fSRzT2_7chzDmxSzRIut0HlDhMDSbP67T9_tleZPP5zF6PFGaXqCB4JxcWKLc8k5bnl4uTPwaVCD0Rubdb4FwSbpD5VrRoaa0JqnqTF4_nvtiQo1CKfwVKehv9QI1VkcFq9q_hsvIq0MQBBxODQozOBO6O4Uwco_6i1wq-zilEC9IxrcXp94W2XwC6vTRu23RC7SwHfUMugaZ_EWFzia8_YcRkEAzRDdjyFzHJ7179pU-_UQZvFy1jfW9YlMkOzwVJ5B45w2RqRIVEggrgq4KLBW1sFiaLHN9i49vRd0IfiiKKKVf6R98VypVQvzpzuyRJp0fHnkvT8k7cayECxrU_dJKc6VXtgz1Em6N2O6S7YRUZjf92XhzuID9olPW1pdvs5V3B8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعاتی پیش، ازدحام جمعیت در حرم مطهر امام حسین علیه السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/677907" target="_blank">📅 01:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677905">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWI3eWKjzd5n8Mrjxzrxb01wV2bMrcVlJLVjZLsYusOPIr0pTQOoQ5DMtElDxl3DPMN8eMvbD2LoHJfTFt6iLQ6CZy-VErDLvlQF8Bgt1D3_Hz8UVx3-p0Ghs5raYfy0jhasiS1mkGrop15_vowtavzzK7ACtp9ElwtoxvwSDga4x1q5KFvGlrRhYB9YLDm3Rlc0H8E9UXyL8hvW_lcxQjfg2xMDUUGt6Ljmt-QRA4stogz2JOAyNHo4RavMulmwwFpK1k0Zv-e_GIOgDGq_7dCnGLqSRRrzzKB_AFPTkIKfcj_f-I1EzxWjDSXDr2unlakrrlrqQNMfY5QwBsJi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخی منابع خبر از عبور یک نفتکش از کریدور فرماندهی مرکزی آمریکا داد و همزمان با ادامه «مذاکرات»، سامانه شناسایی خودکار ساعتی پیش خاموش شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/677905" target="_blank">📅 01:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677904">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
این اپلیکیشن‌های برنامه‌ریزی زندگی‌ات را متحول می‌کنند؛ قدم اول برای تبدیل شدن به بهترین نسخه خودت
🔹
Todoist:
اپلیکیشنی برای مدیریت وظایف با امکان تنظیم اولویت‌ها و ایجاد پروژه‌های مختلف.
🔹
Trello:
ابزاری برای مدیریت پروژه‌ها با استفاده از بردهای بصری و کارت‌ها که برای تیم‌ها و افراد بسیار کاربردی است.
🔹
Notion:
اپلیکیشنی چندکاره که می‌تواند به عنوان ابزار برنامه‌ریزی، یادداشت‌برداری و مدیریت پروژه‌ها استفاده شود.
🔹
Google Calendar:
یکی از معروف‌ترین ابزارهای تقویم برای مدیریت جلسات، رویدادها و یادآوری‌ها.
🔹
Microsoft To Do:
اپلیکیشنی ساده و کارآمد برای مدیریت لیست وظایف روزانه با هماهنگی بین دستگاه‌ها.
🔹
Habitica:
یک اپلیکیشن گیمی‌فای‌ شده که به شما کمک می‌کند تا عادت‌های خوب را به شکل بازی‌وارانه تقویت کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/677904" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677903">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f7279d42.mp4?token=CWtG6A8VIjns8i2WGgkXUfFKUeAV8Xy-oREXtVoojPlvC7foYCUdCDIuoqi_2F7JFqHQWTjWCH3LD06vQ1jHbfzyUiGQn4FQj49axgVVchM9jD-AGfqSVS-VGrADDqSrJcjWvyqlexrLjMkyvmjyFLq27M19v5aAdDVJmupovCrNuXwJEWZyPPF4o2g4YcgI3WxuAPR8n_7MrS-e3AdyG1kr6o3cL9W4wls82BKde5IC6OMTdCZo5cWfQXFLn4pLBqknN9uenR5VVRYkAE5pNMvPXpK4FOsc59PUIR5V6RuQhNvhs3hkTw9RQqRWf4o9fNIw66T8ZT2H3_ngbcs8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f7279d42.mp4?token=CWtG6A8VIjns8i2WGgkXUfFKUeAV8Xy-oREXtVoojPlvC7foYCUdCDIuoqi_2F7JFqHQWTjWCH3LD06vQ1jHbfzyUiGQn4FQj49axgVVchM9jD-AGfqSVS-VGrADDqSrJcjWvyqlexrLjMkyvmjyFLq27M19v5aAdDVJmupovCrNuXwJEWZyPPF4o2g4YcgI3WxuAPR8n_7MrS-e3AdyG1kr6o3cL9W4wls82BKde5IC6OMTdCZo5cWfQXFLn4pLBqknN9uenR5VVRYkAE5pNMvPXpK4FOsc59PUIR5V6RuQhNvhs3hkTw9RQqRWf4o9fNIw66T8ZT2H3_ngbcs8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه ممدانی و ترامپ از زبان سناتور مطرح آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/677903" target="_blank">📅 00:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677902">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be19caed81.mp4?token=vlYqK_cHMSfl5zl-DzDFgeGD8wm3juWScJlNPi5FzGYdzWZyVBzYL_8SKR7Ekrl8a1LZneUWUomx_lLaL3BHVHyJUggHjp8JG4LzjFKM9AqDKurzEBBXtxooO1oZ_YLopy-txnaHkh6tocjlu0Pxeicd5tPqA5DXyRSB3r8tThr60jWLC5ZBjVIySw4d9ZbTGQ5DHtDmNeyePBTqUskyMSvNczAR5Q8sWcg1mmDonzU5aBglZqAkB-e2u8Iqok072FryPWfUJh9nyMnO2TcEq4BI8pXLvHQ37-hQV5TldUcRDPIah4lqItNGD7rLf2JBMWvppYxyxGaI5YAmVwxavg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be19caed81.mp4?token=vlYqK_cHMSfl5zl-DzDFgeGD8wm3juWScJlNPi5FzGYdzWZyVBzYL_8SKR7Ekrl8a1LZneUWUomx_lLaL3BHVHyJUggHjp8JG4LzjFKM9AqDKurzEBBXtxooO1oZ_YLopy-txnaHkh6tocjlu0Pxeicd5tPqA5DXyRSB3r8tThr60jWLC5ZBjVIySw4d9ZbTGQ5DHtDmNeyePBTqUskyMSvNczAR5Q8sWcg1mmDonzU5aBglZqAkB-e2u8Iqok072FryPWfUJh9nyMnO2TcEq4BI8pXLvHQ37-hQV5TldUcRDPIah4lqItNGD7rLf2JBMWvppYxyxGaI5YAmVwxavg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار رادان: من یک مشکلی برایم پیش آمد که گفتم نمی‌توانم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و سردار غلامرضا رضائیان، رئیس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و به شهادت رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/677902" target="_blank">📅 00:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677901">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61555f46d8.mp4?token=PVjtgCmdXZbONcFXvtF3P9UtT8RoDN12Q0x2jqJY8TH2k0Goer7ZRz-DpAqdJOGve8ChE6hYTv1EdiIH9Yr4jvTQVWOG159XU7QmOG-BL2Y5d-f2lKzWure9z6gdoE8fzu6Dt9y9h5CDKcBgeB94jz-iOQaXLivbGh5YfEK3LSYDXBREw6iqItQnMyEyuAS7dp6wB-HZJqLVyrDJEJNeG8Ku5x6Sg9y42WMUxeG6_KyF51s9Xm1tgC0MSMkHWCSDlGerKByVxGCc6jvcj4in0fERiye4W43up2Y1ZtkBrzu4PlL-zZxecClTppTN58XXPCbQ0EHU_zPNYv-F0zO9aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61555f46d8.mp4?token=PVjtgCmdXZbONcFXvtF3P9UtT8RoDN12Q0x2jqJY8TH2k0Goer7ZRz-DpAqdJOGve8ChE6hYTv1EdiIH9Yr4jvTQVWOG159XU7QmOG-BL2Y5d-f2lKzWure9z6gdoE8fzu6Dt9y9h5CDKcBgeB94jz-iOQaXLivbGh5YfEK3LSYDXBREw6iqItQnMyEyuAS7dp6wB-HZJqLVyrDJEJNeG8Ku5x6Sg9y42WMUxeG6_KyF51s9Xm1tgC0MSMkHWCSDlGerKByVxGCc6jvcj4in0fERiye4W43up2Y1ZtkBrzu4PlL-zZxecClTppTN58XXPCbQ0EHU_zPNYv-F0zO9aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاتز وزیر جنگ یرزمین های اشغالی: ما ۲۴ روستای لبنان را ویران کردیم. هر خانه ای را ویران کردیم
🔹
آنها برنخواهند گشت میدونی چرا؟ چون جایی برای بازگشت نیست. همه چیز نابود شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/677901" target="_blank">📅 00:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677900">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3c943d32.mp4?token=gV7MKrLuMQOpVfoaHiVWFq8GqmzavwGKcBbdgUqB6JQ0ElKKdPqfc78XT2C2hMmOpT--81jDzZBMdSiLyj8YksowMbyJoky44OvyLpmH5HbWrTPjckwXMjBm6rzIUCGztpYHxPFskbDngRisFlXd422qPPnUfaUq4dw-ZJw2gDXS3LG0CtWhUhESR0GftE5upxgzKZHiD75MeW_Fho07Fd9sSPdRBS6I8RaPn_ABYIiIYtMkdRg9JK_iJXTctT44VGYAR7OHCOBOmxRoZARKRUMwFwiys4WLNb3z5oreLPYXEHdqAbcXO9kYSXzG-y5qm3-ZEbmW_5iRab6rOhxKgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3c943d32.mp4?token=gV7MKrLuMQOpVfoaHiVWFq8GqmzavwGKcBbdgUqB6JQ0ElKKdPqfc78XT2C2hMmOpT--81jDzZBMdSiLyj8YksowMbyJoky44OvyLpmH5HbWrTPjckwXMjBm6rzIUCGztpYHxPFskbDngRisFlXd422qPPnUfaUq4dw-ZJw2gDXS3LG0CtWhUhESR0GftE5upxgzKZHiD75MeW_Fho07Fd9sSPdRBS6I8RaPn_ABYIiIYtMkdRg9JK_iJXTctT44VGYAR7OHCOBOmxRoZARKRUMwFwiys4WLNb3z5oreLPYXEHdqAbcXO9kYSXzG-y5qm3-ZEbmW_5iRab6rOhxKgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظی عراقی‌ها با زائران در مرز مهران: اگر کوتاهی کردیم ببخشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/677900" target="_blank">📅 00:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677897">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
تعداد مجروحین ارتش آمریکا در جنگ ایران ۶۵۳ نفر اعلام شد
🔹
بر اساس گزارش شبکه ABC آمریکایی، تعداد مجروحین در ارتش ایالات متحده در طول جنگ ایران به ۶۵۳ نفر رسیده است.
🔹
از این تعداد، ۶۴ مورد مربوط به افسران با رتبه بالا بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/677897" target="_blank">📅 00:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677896">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd733b7b6d.mp4?token=H47RCQ853rwXnlxspr7vnBh7ICZ7ZVaQHSiVhqHhnUEGpNkw-OYy9bHvjlkYMYwzz4ow1mbso75SPbkN7v89mdUOxBcGUlyLeMO1MLn9vAh_nncDLBcjEKcjj1T_MGa8soiQ9yLtDxB-LON3atHh59u_1OEXOHhEmljZOGOnQ2QS71z8w6FBoRnQ0_qWQJTKi5svsE3ODFlz3wwJIEnGYUXk_NxQf3s-hk4uiCLA9tVu-_JdPlfzo2CyZl59JMjN5iS034z35Lj969ndmJDi_Vn60oElv3H-XrRedD-3YtPqQPzVejeq0Xck-KjBcFFCcfgO-Sif5rzqy3q99ExV1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd733b7b6d.mp4?token=H47RCQ853rwXnlxspr7vnBh7ICZ7ZVaQHSiVhqHhnUEGpNkw-OYy9bHvjlkYMYwzz4ow1mbso75SPbkN7v89mdUOxBcGUlyLeMO1MLn9vAh_nncDLBcjEKcjj1T_MGa8soiQ9yLtDxB-LON3atHh59u_1OEXOHhEmljZOGOnQ2QS71z8w6FBoRnQ0_qWQJTKi5svsE3ODFlz3wwJIEnGYUXk_NxQf3s-hk4uiCLA9tVu-_JdPlfzo2CyZl59JMjN5iS034z35Lj969ndmJDi_Vn60oElv3H-XrRedD-3YtPqQPzVejeq0Xck-KjBcFFCcfgO-Sif5rzqy3q99ExV1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت جنیفر کینگز، فعال رسانه‌ای آمریکایی از اقیانوس انسانی اربعین: اینجا هیچ دولتی هزینه نمی‌دهد، همه‌چیز خودجوش و مردمی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/677896" target="_blank">📅 00:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677895">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
نیویورک تایمز: جهان به سمت یک جنگ جهانی پیش می‌رود و به نظر می‌رسد هیچکس، از جمله رئیس جمهور آمریکا، کنترل روند حوادث را در دست ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/677895" target="_blank">📅 00:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677894">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واردات موبایل از ۹ اسفند متوقف شده
مهدی اسدی، عضو هیئت نمایندگان اتاق بازرگانی و انجمن موبایل، تبلت و لوازم جانبی، در
#گفتگو
با خبرفوری:
🔹
با گذشت پنج ماه از سال، آخرین ثبت سفارش واردات موبایل به ۹ اسفند برمی‌گردد و توقف واردات، باعث افزایش قیمت گوشی شده است.
🔹
افزایش جهانی قیمت قطعات، رشد هزینه‌های حمل‌ونقل پس از جنگ و جهش نرخ ارز مبنای واردات از حدود ۷۰ هزار تومان به ۱۳۰ تا ۱۴۰ هزار تومان، از مهم‌ترین دلایل گرانی بازار موبایل عنوان شده است.
🔹
در نتیجه این شرایط تقاضا برای تعمیرات موبایل، خرید گوشی‌های دست‌دوم و استفاده از لوازم جانبی افزایش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/677894" target="_blank">📅 00:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677893">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e4715e7b.mp4?token=OMC0rrj96tPo4pkdsi0b1u9ncHhSIVVyufrhilmTlBThGdU4ldD-uuv4DTkk0jtsj2aL2GeXltytqQfMWjYk_gUD0-IGugg7LyDLJAd3g9rqh6lMdsIlJ6G2jLTZm8Z9tqhTAGikz2-1_1Ydy_DEmSxJmUKvnEfca0gXnZeqqMLQo0TM1KgPQ0AkitMC962VUjuR3ZAgYdI5HlzKIawocjomozpdPUOFSrWrx-daCP8dw8PdWAHBuAE2uwHSFJJc5FhhjeG3GQJ62UcSJYFcgj0em9BKn8QMvKcHFWBSoj_GmsLegBWtZZTYNtEMnSKrHVRQcTzUPNpaWbaaxA19gGt-5oVjcjzmwSUUibXQxPLAFIsRlXe5QkGZsyrpWhSQdNlguPHM_Zx7oxEXbNsvuwdUmOIfRVKOI_qgTEz2X4dXHT3BujXkKDRJb1_Kyins8zG2ZgWvN26nWEYOqHmGD94soVO_ZawBu-bV6LecuF6pCyweNGOwlxNP2V4TpIh4qjuppeg-ob7dYJN7FLhrE2aX6wKWBrKBgYE-E3yJlmO_YOfZQpXnsXMr9HQbe8ek4Mdll1baRFZp_lyoztbjzMRXuat6llA59PfpA6s0kCst5-1o4KsdjkG7_daIJkWpJOUkPSMPFvbqKaNbo3ol-hDo67eXK8lPyZIic1PBzE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e4715e7b.mp4?token=OMC0rrj96tPo4pkdsi0b1u9ncHhSIVVyufrhilmTlBThGdU4ldD-uuv4DTkk0jtsj2aL2GeXltytqQfMWjYk_gUD0-IGugg7LyDLJAd3g9rqh6lMdsIlJ6G2jLTZm8Z9tqhTAGikz2-1_1Ydy_DEmSxJmUKvnEfca0gXnZeqqMLQo0TM1KgPQ0AkitMC962VUjuR3ZAgYdI5HlzKIawocjomozpdPUOFSrWrx-daCP8dw8PdWAHBuAE2uwHSFJJc5FhhjeG3GQJ62UcSJYFcgj0em9BKn8QMvKcHFWBSoj_GmsLegBWtZZTYNtEMnSKrHVRQcTzUPNpaWbaaxA19gGt-5oVjcjzmwSUUibXQxPLAFIsRlXe5QkGZsyrpWhSQdNlguPHM_Zx7oxEXbNsvuwdUmOIfRVKOI_qgTEz2X4dXHT3BujXkKDRJb1_Kyins8zG2ZgWvN26nWEYOqHmGD94soVO_ZawBu-bV6LecuF6pCyweNGOwlxNP2V4TpIh4qjuppeg-ob7dYJN7FLhrE2aX6wKWBrKBgYE-E3yJlmO_YOfZQpXnsXMr9HQbe8ek4Mdll1baRFZp_lyoztbjzMRXuat6llA59PfpA6s0kCst5-1o4KsdjkG7_daIJkWpJOUkPSMPFvbqKaNbo3ol-hDo67eXK8lPyZIic1PBzE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/677893" target="_blank">📅 00:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677892">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d77fe50a.mp4?token=S_SS2Zy-RHbNO63OHAaunHqpRWNYzDVfU2sDatWCnxmIEhRdoMSYeUtQaKxCGGVvvts4Jm7ARTHC1SFTpcnU6tzok8gzN5B0heL-Wi9KrH6GHeWDjxx7Isd3YoC4kH7KXNVSnsGipkIrMonAXtjyI6db4gJuNW0KfdaYTlbylJIqlCLCq-bWYJoBPtF-8_RQZpSOWFAKjx6E15-Bc7S_Oz9D620WajkImRWMP0U5hmnosm9h-3yrsEyX2zuEvc9xAl03y9bK4SDyokVRcxZtm7HZ-3yEUbgRekdvGCfEztNMDy2MuCQmPlOskS150SpfhqSAfQ4U8H67FS6aXPD1xBsZ0wo1K-ScbXL_rkh78qU2npamRc5sUcwlEW8Nwdvn02fRGRSM2KOOQ9kahpavvrrT6bUpdHCihD8UwYdbqRj1ATk1jPi9IrR0aDo94klZbGmlMlbUPYSXub-_NxZvhks_wlUR2gwfysa6l9YqKGZFFCO_ps2eX583m7RXpZybb3TlyylT5HMeHTQ-cvKsv7kFI-qQdnWpBkQHonEBDiX5Gfxn2BMAz2DreAFANKSdx6dqX1Hc-_u43rvsYUToHSrBA1MPDTZW7GjUO-IvU9OET-o6cncxECbQduJFfdvApUIAR0rRL4I927GaDMuQ8JnJtk17w9Yo_qHue-WlYc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d77fe50a.mp4?token=S_SS2Zy-RHbNO63OHAaunHqpRWNYzDVfU2sDatWCnxmIEhRdoMSYeUtQaKxCGGVvvts4Jm7ARTHC1SFTpcnU6tzok8gzN5B0heL-Wi9KrH6GHeWDjxx7Isd3YoC4kH7KXNVSnsGipkIrMonAXtjyI6db4gJuNW0KfdaYTlbylJIqlCLCq-bWYJoBPtF-8_RQZpSOWFAKjx6E15-Bc7S_Oz9D620WajkImRWMP0U5hmnosm9h-3yrsEyX2zuEvc9xAl03y9bK4SDyokVRcxZtm7HZ-3yEUbgRekdvGCfEztNMDy2MuCQmPlOskS150SpfhqSAfQ4U8H67FS6aXPD1xBsZ0wo1K-ScbXL_rkh78qU2npamRc5sUcwlEW8Nwdvn02fRGRSM2KOOQ9kahpavvrrT6bUpdHCihD8UwYdbqRj1ATk1jPi9IrR0aDo94klZbGmlMlbUPYSXub-_NxZvhks_wlUR2gwfysa6l9YqKGZFFCO_ps2eX583m7RXpZybb3TlyylT5HMeHTQ-cvKsv7kFI-qQdnWpBkQHonEBDiX5Gfxn2BMAz2DreAFANKSdx6dqX1Hc-_u43rvsYUToHSrBA1MPDTZW7GjUO-IvU9OET-o6cncxECbQduJFfdvApUIAR0rRL4I927GaDMuQ8JnJtk17w9Yo_qHue-WlYc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترکیبی معجزه آسا که استفاده کردنش بشدت توصیه می شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/677892" target="_blank">📅 00:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677891">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: ایران در آتش‌بس برنامه جدیدی را برای جنگ طرح‌ریزی کرد
ادعای نیویورک‌تایمز:
🔹
در طول یک آتش‌بس زودگذر، ایرانی‌ها مخفیانه طرحی را برای افزایش هزینه‌های جنگ برای ترامپ در صورت حمله مجدد نیروهای آمریکایی طراحی کردند.
🔹
در طول آتش‌بس کوتاه‌مدت، ژنرال‌های ایرانی مخفیانه با فرماندهان شبه‌نظامیان نیابتی در مورد چگونگی گسترش جنگ و افزایش هزینه‌های آن برای واشنگتن، استراتژی تدوین کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/677891" target="_blank">📅 00:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677888">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdNg6iV6RYNp_Wft1Zq3i9f7A2EJsc9epkO8ot6emM8IQuL_Dbs_Cjz1bFxcGeAztHg1zqxcrEYT2S_Gju6SQBeloPBFf34O_PYi5dNUQStm3Q_Zf1wY3xvkralGLz9xPHOQrxyYRHWUfhER6-wCAGdKyvSH1_X4aCZAONbtRX6WB5GQmuGjhxiADqxIToIy1k3qHHqLT22UYdKIP3PyAOTA7sZgHhALWV9a22rD1RKEYvBElbBjXPnFtcnX6-p5TcfnSOAccXJ1xWKAfBzQ2QFrjYfQJ-xtwgzCgYss6lFlPokXqs-dNsiZKmrQ5Cno6IFIYi75uM9aeUP3ls84aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/677888" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677887">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azm1wUeCPxJdbUJROE_wUitOAbzhnhCB1No6wZK7pEvt7lnwaDpw8veDHHKK6cQhM_hSPSuYLZy9sXuxQ1nnZh2cqZzYXOa7t-OQJ31BMAQ-nl_xTJ5nxMhsj-ZjHzB28LXWFqz6gg057wvLR34HduooHWtANzjw83tM70kzzk1cZH5gB6RzYZqaJ2b0T9kXIplE76Ql-LQj7wm0XF82Ub0jHFxD5DC03UfKqRKeD0qhwuTX9fG8aRGJCYZlEA7W7Jjn0gtcSvQChoyUwpT5BJQEIKmcsexMPyuW7iwiWuA186M6XapWmA-8dnYyLK_OtvuMgH6gC4SPU9E8yzN80w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هفت لاف
🔹
دونالد ترامپ برای هفتمین بار از مواضع پیشین خود درباره حمله گسترده به ایران عقب‌نشینی کرد؛ موضوعی که برخی رسانه‌های غربی آن را به نمایش توان بازدارندگی و آمادگی نظامی ایران نسبت داده‌اند. همزمان، شماری از تحلیلگران معتقدند تکرار این عقب‌نشینی‌ها می‌تواند بخشی از یک تاکتیک رسانه‌ای برای کاهش حساسیت افکار عمومی و بازارهای مالی نسبت به احتمال وقوع درگیری باشد؛ به‌گونه‌ای که در صورت هرگونه اقدام نظامی، شوک کمتری به بازار نفت و بورس آمریکا وارد شود. در همین حال، نیروهای مسلح ایران بر حفظ آمادگی کامل تأکید و اعلام کرده‌اند به هرگونه اقدام علیه تمامیت ارضی کشور، پاسخی قاطع خواهند داد.
🔹
هشتصدوبیست‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/677887" target="_blank">📅 23:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677886">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJGlt212PEeYfIgQ7UywVtwOnEktBu3vHpuSTBnb3ODB0qtpjD3mZb0QMJ9p0GDq0QBBC4frpd2eMBXj6Uq4lTVKBGJyeHWbP6HFJf7Wtn5d13VElyycvJ86_NhfwtjJ3zezlN41UIlMhOR_4KvBVLWwTd-YN2lobA1ODn5FEmp74Wp-TY5c28qbhBrbcjPwvVPgxkNOCB93UDIf-feoHT09pmNqrf9NIql7Zb29TKOpXGcxzieASmEoDgI7bWFA_5rir8Jmh0MJ2OmQmGahARd5IInrlPkAbQSqR-ALHdtYjDfa2lt10eRUYdcoYvaS-XYbJ-IoFJnGoCb6HLf6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سال‌هاست عراقی‌ها پای کار میزبانی زائران حسینی‌اند؛ این روزها ما هم می‌توانیم با قدم‌های کوچک، همراهشان باشیم
#میزبان_باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/677886" target="_blank">📅 23:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677885">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufax_izp7Tz3hlEoTM_ClckZ7Jk4Zud7QS7zaEtik324w8S8w7mefkAtCvNWuDkGcHIQaJ8pLqu3oc89QRq2g0OIAoxAJix7_6PywYv56qTcwPjQo95iA2kql51v7Xsp5FCWYiIvmREuIIhuZyRv5iUjGlWi0JX7n0EKLrjpsIWAX5ZuiKMDaYuLzbyTMpfSPW2o4SxA08UvJsh4VIIK3A5LGC-qVw_s0-Bt_0DjaW033jVrt2v4Z6p2ZU6kkoe8hS_1uEedZ3W6BWP67qgoXN9_GU7lZJx7tIJ3N5GS4eXb9Y4DjyK1unj_BDwhSDvipzrqu1RHxNxTMUbx6LdY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گفته برخی منابع خبری؛ پرواز ۵ هواپیمای سوخت رسان بر فراز خاورمیانه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/677885" target="_blank">📅 23:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677884">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQbaefl8ZLY-HdnZKQQLuJFkVO6pyVEBa6u_i39PmyE8f1B1Ol3Bk6No8emYMiAyEzKivmIlVsGRmHNDbrKOoircQJIADjomHmzqdifPZrehu2kSqxpoJT8FlhF-k3uXM_H43njLvV8s68k2hoeQc0tmfUzqYrnY3tDOMjc-qSq3uk-L9SXxqdXDsySuFnkkqDNrEXHW1zTRH1epwPQScuaIyRQbpIxREs6mhIXQaZ1sSDVtBZD24uxtZsTGRJq0Zpum22so6-1NIUP9bEzxzcmCB8rpxskfYmqIi0ZJSobMRlrTmiKZeX7dQ4K-XWpWbbGexKKLNyuP_XhJmOiLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عباس جمشیدی‌فر با انتشار استوری برای وطن:
من غیر این رویا کیو دارم
دیوار امنش عین آغوشه
یه قطعه مروارید مادرزاد
قلب منه! اسم وطن روشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/677884" target="_blank">📅 23:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677875">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQo95sgeVCh-6LV8GWDKoHjVf0HLLZl161kC5nVRdxzIvK44H03jFPx60WZNk-4nkAcUC9r2Gn2RC4fn6fwJ_JijmTO-n6JWiHXPckYMsruLBaoqg08lEjRosi2qBU0fLh6jSvf_FU7RR7MFPJJ80fMbwhb-k5-pFlHKgcbtV2xO7cRUsDBFwxsDU_nXDybP9rGslLBMzzrjmJ6iXgqN-2PlxN_p3vFp1zHxts878o9k7HlJQ6snn9l8jG7zweEMfXPrqpP8JY2MJoJz05hjhRGtnHF_xYqaeQ9ws3Qb5UXXz5PUGZiw9701qZef9jMM5Qwztxbq3YwfntWfh4L-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NE3E-wZjmcNTlAaMpCh-QjAyEFHo77Qisz1rX7ABaeshcNHNQmMF-o6oWkLfA4zpq68Uln5plBInkRAUQZRq1CeUCE0Qp_f9_Eocg7yjc9pD2TrR6zM-8lWJ8W2Tivda2iDKxF8ed-NPtS_XkZ-eR5qHvjr-wTMk46djZBwomRGXICdFiwR8AoaDmHo7WAhFnJAM-PjnvHXM9MjL3tz0u-Y7_IgO1ohFr18NaqIFAWSPWLByBzgaJe_WY2YlT37Fuzk-zysTidLqbaiDMW1WfuW3nGYJrMdA8L5Ovu3zJ7tNxMxdNBIKVx3oqSR6HMGb1iU9UJhk8GQgFqGJUNN8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPoYgpCZeTovBfi7qNZVaF0Hl2dshLrnE0OixL9m1Q9Qr1oHDZ9xclcsyH8j5J1HQSHX9MnbTXo6oWO5CsMalIGxxwtYHlBNvYhKwEpT06vQlWI8e39HEm0bKjn44bR8P01DSPrfhKvtpjBq4tgBkLm0hhFX2TGGqAAHCWzoOKuAZdTVFbLDpeYpn8OXvM08yxrn_3VEaheLb7muk-Q3ZZoYq9KRszWx-dMwaBoppMfH-VixNXdH7R5DG8-jcam_4bKeVmv8I9_jEwIKrlMgYjhyGJ0Zf0UnfBS8jKXwXgFIH-NCAeArNburJug3tdPF73clat1NHnVWfy9WCcCZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGg22cX5P93vTsIcuSL2KsC7duSPN6888PdxNI-FlDC6YbGmCa0ccEi0k2G6ZU--sFNUwegZIhcV3wHDodEQ0je4bgatrjRvFjXE239nPdrkXMDWKa03CaKOhbH7C3m4Y57jzboJ_fdenrgQf3wPWouhszYbDub2StIuO2U4mxfZPzybb2bJxWrW8FMiC4GpH3NxWTqrSnHWfelDce9w_8Cn4RuKd4pLtCSzniEz5Awu3FXJe79iman1FWJ8T0Morixjj7gnnx-UNuXueLyqAn4brKEJ4LPrCazfA3pLgfGOGUrI63ZCVKRW0BtrHbZfcxBckFawtM-KwTkFBHYTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAVzIuJg-3uJk-RC8HE3opC-IQsPBSshNinRqnQGJr-qKboqM2_D3zHPtidZlMFdPBKUREWDD8Hr4xdxV8yQwF8q5IR2zmDVICfBPbo_2voQ6vgtJm-za8xpwTob1X6ov1bem3oaiQkL_EyNhWSabDkzYtatJ_D4QoTgqOYv0p8acqFn_RnjBSiLJOLiGn0HPNG5CB5aZ7fWEAxoO6Pm8f-WEXECRynRIsMabjI7Yauhkc3phYZ8E-6IGKh1kVKyVSIvGD5DM3eJg02NbsMW9oCCHPAZgRnqw9X0ACu9WRjNy5X3buBXgojN-nxN9EM4S832TBq-S7GWDKzliNwTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knlMLIORSpSPC_Sm-uvmoAaCmqPSlK1qmpEwQbZF29IJKrgUwXKd0sweTYnUgakBB1y5DuoO0y89UBJdNgjAdTpk-bTuSWNBr3vpFaV1H0A7h-y0LUY2q0vSrYvzEV1fKE5X4hDt3iSaVluhpVZisdJcO90cQaamYuU0Dj8n2rsA5Qs_fDvj38OrUTqYtArYuSkpZeKMHqJwOKuMUmZp_sGg7KjjgKlyf7ZCCrlvMqzMcq0LjeH37zohIvfPf5MF__0d2qFzO3PMfKvjzTz6ics1o-QCJ_0a2B-VKyENjIaz68JO6k909fjo-JGuZavQ16dRWmsfAfkzpFllgnDfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rwCXRESaMmFsmnXuVMnSS0KYwoY5unFGj2S-gYF2HAyOMMR9CALv9xc4YFYYfvtoU7jmgdQLPuU-sYCoidf5RdsYbCFi1QoBXQ5gCpVl6FLdhuXalqK6i69XZzJPumaPB1hJswfsH_KOwY3zpj7jGvIhwumgz5rLMGm77ODyrXCPKF5yAoBcfOMzSKjJiMRbGzDf2ssq_kPzIpQ4rw55NMReawoSMpi265MN4fQVEYTgAi3fVG4iZ0CSBLvqC_EnbmNnIa_pp2Oo4oI0QYS_4aAY0URURDvTQQK62PK5NWIY-qe-0aGlnriKd-umSwQU8amlE-5l8apNnwD7DB_cdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUpdb2OACW2c3OoRjTt7VlTZgP421Jlj2_gI5zXCvAA721Op8MmWrg9uI4kQewsqzH9LueA1hR8D7V--qDK2Y9cHQOc1u4IqDF9ELx0ub0fUs3JrczCt10GlLsm1HkKxoGG7hjPhcOm28q68GAAWHUaK8kF81FweZvdHHzS9q6I_aeHdVFFxvY4vV3rVbwgdhr_3O8bXP5ivqTcBmCCYr1Fl-GlBVJLc3jBTOM2NqJ9S4qoo078SJD1h1MaTzzTC40dQyddhmuogOlGHE_pVguBfh2sDe-jCiRtV5IN7tMx-pGPwZn6TsocH9AA41JY_Nz8zlcSp2jZ37-V29CkXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S77P92FtOrafSdZoXlFnqrluA4twjkox4JUJxohKmbX5U9jLrDQ6jOOio5I9Uey1Q0wFgTJ0JY1C62KLbXA4JreFhBNuDEFQRx6ge43nNUYi0cnk9v3fbLj9kWRcwsAouioPs9SDivoCGOF7ZiodVx_1zBLXpzpRz66dovU9vUR7jSSfeqUyRy-xPJc4KEWu_nLD8pGTV3smgOsd6uMlQ6bvLKIz2ptJdb-Hf7Cnu5ygIcSOJDLRp9vdQfm9hVIUQH8i8jhkGwtVMl-cGOqS8h44UoKENApK_fMXnRMqwFDJIjCbjAkS2jxEUZZ6rnXlzD6GYGgf8IZcE26CJHC-4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت دستگیری
💫
✨
از مکتب امام حسین علیه‌السلام آموخته‌ایم که دستگیری از مردم، یکی از زیباترین جلوه‌های ارادت به اهل‌بیت علیهم‌السلام است.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با توزیع گوشت قربانی، در کنار خانواده‌های ایرانی ایستاده است.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/677875" target="_blank">📅 23:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677874">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4069a62fd9.mp4?token=vLCpu4BtwfsPY8i0OYIy5K65mP74L3PD-tTLfo9Q6SxZAPCyLjiShuAaZ6T7OWDVDGGJu68z83Zgj_k1TbLFxMDTCgMzMj0CHpDFDHcY6rQPXi46uBVCOzuAPIov1tMnZulc1GE9ML0ktbDO60YXxG3rfGQNdH_IcWpSx9dfz6OKS7shfVuwpiNLyje5bIr8Q8eUMaUxa_yCQzmV0QKxdwrP6c03gpqbSiAMvHlPEez7BIfi85mX-1T41ViAqtSkWA5ddPBi-qSg_I1JLXP0jUWLh5pCXQjRc1l6p3bcwNxSSNV3yH_hkoYMUhf83ZTZQ1s9RCo-2P7hwgGWUPiLF2oY_ATrizSN8RJeky_KyikBeZ8cYimEHb2YXH1vQVGJNEKTDxlEhr2NvCuc8k2f24tCUUbahpziwZImHNLQKPypWKkpks_Ku3Tzw3qJh4ea0x9iwnB4ScTEA5mqHtjLJTmoL5ByFDGfq0XvJ7v9cv3EuLyFNhNf7qwW-Nh8Sb4CiRBNZTasMuKf6xyoYB-7Z2_Eu2rzsroWZ9Cd1D-ZtjjmimReQCm4N0qf2_q-VEBUcCh8O8GHLcPA4dsV-rGj29HdAf8uCt2Ks0E9_NjwkrSkZtX6VlpRgaWewEZVIzuw1tcsjnMzBhjGMRIMjzevf4RkDEYy3abUnkRnzON-vmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4069a62fd9.mp4?token=vLCpu4BtwfsPY8i0OYIy5K65mP74L3PD-tTLfo9Q6SxZAPCyLjiShuAaZ6T7OWDVDGGJu68z83Zgj_k1TbLFxMDTCgMzMj0CHpDFDHcY6rQPXi46uBVCOzuAPIov1tMnZulc1GE9ML0ktbDO60YXxG3rfGQNdH_IcWpSx9dfz6OKS7shfVuwpiNLyje5bIr8Q8eUMaUxa_yCQzmV0QKxdwrP6c03gpqbSiAMvHlPEez7BIfi85mX-1T41ViAqtSkWA5ddPBi-qSg_I1JLXP0jUWLh5pCXQjRc1l6p3bcwNxSSNV3yH_hkoYMUhf83ZTZQ1s9RCo-2P7hwgGWUPiLF2oY_ATrizSN8RJeky_KyikBeZ8cYimEHb2YXH1vQVGJNEKTDxlEhr2NvCuc8k2f24tCUUbahpziwZImHNLQKPypWKkpks_Ku3Tzw3qJh4ea0x9iwnB4ScTEA5mqHtjLJTmoL5ByFDGfq0XvJ7v9cv3EuLyFNhNf7qwW-Nh8Sb4CiRBNZTasMuKf6xyoYB-7Z2_Eu2rzsroWZ9Cd1D-ZtjjmimReQCm4N0qf2_q-VEBUcCh8O8GHLcPA4dsV-rGj29HdAf8uCt2Ks0E9_NjwkrSkZtX6VlpRgaWewEZVIzuw1tcsjnMzBhjGMRIMjzevf4RkDEYy3abUnkRnzON-vmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آدم‌های ترومازده از عشق فرار می‌کنند؛ درست از همان چیزی که نجاتشان می‌دهد
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/677874" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677873">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwwlbCAt91kvYZ_h1U0AQTLwW4TRANwU7fQjo3-AndfxsRziAys8-M6eCaQs9yKfTCLm35K1mPv-y2aGfZAEl1rLsahys1o92ha-L6mGBV48VpL5SeF_PAagV4OvY7Aut7-pP_zfS1gboujWcJE90msYlSheVSQqfrojLuJnPzsieKMGnyBWPRkSh63gxu4UDKWV97UBtxE1FYuuhbyT3_4zTB07t3TeKcDMd9W9o7XkuO9ePBQXEpODVgafpllKAKeE4yv2lt32zbS58I1KeIAub0fIXwhnP6psKA68CSmtXhh8Q2_olU2q4IW0SfYtw1PYICmfkH8QF47sBhRohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«پرنسس تاریکی»؛ زن مرموزی که صندوق مالی ترامپ را پُر می‌کند | مردیث اورورک، شَرخر کاخ سفید کیست؟
🔹
در دنیای پرهیاهوی سیاست آمریکا، جایی که دونالد ترامپ با سخنرانی‌های آتشین و حضورهای رسانه‌ای، تمام توجه‌ها را به خود جلب می‌کند، قدرت واقعی گاهی در سکوت و در اتاق‌های دربسته جریان دارد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3234989</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/677873" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677872">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای عضو کمیسیون بودجه: ۱۰ تا ۱۲ میلیارد دلار از پول ملت دزدیده شده ‌است
عباس قدرتی، عضو کمیسیون برنامه و بودجه مجلس در
#گفتگو
با خبرفوری:
🔹
نمی‌شود در شرایط تحریمی مردم در سختی باشند و تراستی‌ها با پول ملت ستم‌دیده ایران در خارج در ویلاهای خودشان تفریح کنند. براساس شنیده‌های من حدود ۱۰ تا ۱۲ میلیارد دلار از پول ملت ایران دزدیده شده‌است، ولی هنوز آمارها قطعی نیست.
🔹
از طریق پلیس اینترپل پیگیر استرداد مجرمان هستیم و نمی‌گذاریم پول ملت ایران صرف خوش‌گذرانی تراستی‌ها در اروپا شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/677872" target="_blank">📅 23:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677871">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/576e15e56f.mp4?token=IEkU7J3i_Cu-fxAPQkakZOzI1E66qeVSqRHlcCdiC3JCqRDByNF_9HGZQDHgPfsF7xaabUEvj9VAvKqW4Y_7gVqWWVKRKUPCva6dJFXIExJgxhEEEb-WBvksdCwuPIbLNHXi3bkUtlkF8FJNFwWjLMkTG1JVYk4Zw6MbsJHfTCOhH_rz5cTKK2IvDCXNEGXaXkBPbL4pThB5ae088nX8Pwpcjwd-CAs7fJPi2WqVlIrw4YVz6TaGKat-WvT1ylqWKd46f0rKLjUcBBVwSAqE1eDhruLOyWKXQZNNJelTAk93DaqnYP8intN1QtQku-3RvVCPoRRUT7q4lIGZLreT76BKueB2gu_XtiGAqFsyHq1zzCa4NNxeRK0cEd_e7YJnoD8KXdzsXof7mfrb0RSjzLIDKJkln1L5_QfiyWodh_sgGyg8p8foIumM6eAo1YldJ1ZfdvqBJ3Qe3ROPiWakaZqCa5ke3E1LA3eoy2G0cfQPCUppngPGSH6bzMUBiCcx4hKhCbRQpVB6XVQbMbFpdXPPCklNhtbo4khh3QieRLf4CGTi5ZxZngmQFomeTBBgmhNmmYRcMp0pjIEj94mRxVHcosVq8-drO4IRJ_Y5ShE1dRlhBtyJ6pOqaRLJH3toN55qS_vtZsjz8ndm_KkpPShgmShdTrwsaPAetSKPTLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/576e15e56f.mp4?token=IEkU7J3i_Cu-fxAPQkakZOzI1E66qeVSqRHlcCdiC3JCqRDByNF_9HGZQDHgPfsF7xaabUEvj9VAvKqW4Y_7gVqWWVKRKUPCva6dJFXIExJgxhEEEb-WBvksdCwuPIbLNHXi3bkUtlkF8FJNFwWjLMkTG1JVYk4Zw6MbsJHfTCOhH_rz5cTKK2IvDCXNEGXaXkBPbL4pThB5ae088nX8Pwpcjwd-CAs7fJPi2WqVlIrw4YVz6TaGKat-WvT1ylqWKd46f0rKLjUcBBVwSAqE1eDhruLOyWKXQZNNJelTAk93DaqnYP8intN1QtQku-3RvVCPoRRUT7q4lIGZLreT76BKueB2gu_XtiGAqFsyHq1zzCa4NNxeRK0cEd_e7YJnoD8KXdzsXof7mfrb0RSjzLIDKJkln1L5_QfiyWodh_sgGyg8p8foIumM6eAo1YldJ1ZfdvqBJ3Qe3ROPiWakaZqCa5ke3E1LA3eoy2G0cfQPCUppngPGSH6bzMUBiCcx4hKhCbRQpVB6XVQbMbFpdXPPCklNhtbo4khh3QieRLf4CGTi5ZxZngmQFomeTBBgmhNmmYRcMp0pjIEj94mRxVHcosVq8-drO4IRJ_Y5ShE1dRlhBtyJ6pOqaRLJH3toN55qS_vtZsjz8ndm_KkpPShgmShdTrwsaPAetSKPTLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابداع جالب یک کودک ایرانی برای این روزهای گرم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/677871" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677870">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
چین، موتور رشد قیمت طلا را روشن کرد
🔹
طلای جهانی پس از چهار ماه افت متوالی، سرانجام در ماه جولای با رشد ۱.۳ درصدی به روند نزولی خود پایان داد. تحلیلگران، افزایش خرید در قیمت‌های پایین به‌ ویژه از سوی بانک مرکزی چین و کاهش انتظارات از افزایش شدید نرخ بهره آمریکا را دو عامل اصلی این بازگشت می‌دانند. همزمان، نقره با افت حدود یک درصدی همچنان تحت فشار نوسانات بازار باقی ماند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/677870" target="_blank">📅 23:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677867">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
توقف 2 هفته‌ای حملات و خوشبینی نسبت به شروع مذاکرات ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3235009
🔹
شاه انگلیس دامن پوشید و بین مردم قدم زد | عکس
👇
khabarfoori.com/fa/tiny/news-3235041
🔹
توضیحات خبرنگاری که ویدئوی جنجالی دست دادن عادل فردوسی پور و وزیر ارشاد را منتشر کرد، درباره واقعیت ماجرا
👇
khabarfoori.com/fa/tiny/news-3234848
🔹
جنجال پیامک پدرشوهر ۱۵ دقیقه پیش از عقد برای عروس
👇
khabarfoori.com/fa/tiny/news-3234767
🔹
چرا از رهبر سوم انقلاب هیچ صدایی منتشر نمی‌شود؟
👇
khabarfoori.com/fa/tiny/news-3234931
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/677867" target="_blank">📅 23:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677865">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763e412b91.mp4?token=Weo0UklZmhr8D0XY4R1_AfPSZZPBhbAvUojfg-K2BxevzO37qyGsw0YMqwCfAZfeOKIRk9WZvQ6Y5kObEEjaABSVudTTFC4BY8wT7a1Rfk24VLu_XELpeP5v7wFEWJOcBl4fwQBFycWo9-DAvoQxaJzjgd4tpr9CDZUmqL7wXUuhbm1rD0vMG0aiRjmqWvBYOg7gU6_fvudCDPHDVic_DwEZ1J5D43RiK2LeWCZKaQ28aMzgVAE5K823nKxlAW7kxofqpIGNef6Br-Wt3POuVv2CYEyahqN8_g6L_EilQzJzaOYkXYZIzylAjRV_xI_4Gr7VuiFjmUkVB3p9GXSahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763e412b91.mp4?token=Weo0UklZmhr8D0XY4R1_AfPSZZPBhbAvUojfg-K2BxevzO37qyGsw0YMqwCfAZfeOKIRk9WZvQ6Y5kObEEjaABSVudTTFC4BY8wT7a1Rfk24VLu_XELpeP5v7wFEWJOcBl4fwQBFycWo9-DAvoQxaJzjgd4tpr9CDZUmqL7wXUuhbm1rD0vMG0aiRjmqWvBYOg7gU6_fvudCDPHDVic_DwEZ1J5D43RiK2LeWCZKaQ28aMzgVAE5K823nKxlAW7kxofqpIGNef6Br-Wt3POuVv2CYEyahqN8_g6L_EilQzJzaOYkXYZIzylAjRV_xI_4Gr7VuiFjmUkVB3p9GXSahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ماجرای خانم فرانسوی که در مسیر زائران اربعین دفن شد
#طریق_الحسین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/677865" target="_blank">📅 23:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677864">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7adbcc0a55.mp4?token=AqmXUiMaJA1kWoNfvjw4ZmXqm4AXK7twBPgRYoSoRHPmslPG3Y58fbg02o-yTN8d_kbuEIlrfq3RLWoq62Jip1O2osh8MaY7L_LJeE2EAkThrFtDfngG7hUUO8ykfCdTaSQzqD18FU0bl7bt94dL6KonOJnwdtlxUhtlR_d1vFsORrcBf2gb4FkhBdAk4gBLdFPe-2EV4QWoNTWyiyniRGpGNsCLLNbHBQHsCZ1T5EPmYYYcW3MuHRa4fTLWoJo7zhS8-keMdDxENTvORoQNwhu-V9wkDFsSWGBboZ_REMZEvG2YP0LpOullQChWCnWwdMc-7DSFp3YpSDFPlj1g_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7adbcc0a55.mp4?token=AqmXUiMaJA1kWoNfvjw4ZmXqm4AXK7twBPgRYoSoRHPmslPG3Y58fbg02o-yTN8d_kbuEIlrfq3RLWoq62Jip1O2osh8MaY7L_LJeE2EAkThrFtDfngG7hUUO8ykfCdTaSQzqD18FU0bl7bt94dL6KonOJnwdtlxUhtlR_d1vFsORrcBf2gb4FkhBdAk4gBLdFPe-2EV4QWoNTWyiyniRGpGNsCLLNbHBQHsCZ1T5EPmYYYcW3MuHRa4fTLWoJo7zhS8-keMdDxENTvORoQNwhu-V9wkDFsSWGBboZ_REMZEvG2YP0LpOullQChWCnWwdMc-7DSFp3YpSDFPlj1g_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جواب عجیب سربازان آمریکایی به سوالی که پرسیده میشه ازشون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/677864" target="_blank">📅 22:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677863">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a716599120.mp4?token=usYSXNy90fVwJ-Lty-lzwHvzy2MIYjOBQffCW9nGIKJz7siVUQnAjDts8wjwUcezHc5rgb0ot1VsLS_aVRBKuZo5SJAIiHFgKZMGJmL_ictCO95Nzbck6Nj6v0iORW_wA-M9R1eHFMHEW_SEA2_EZvp1R9PtQmzSfjSDuKNsGNCcz1Xbh8-nmfIWMrPmHeNvTxyNB78uuqu7JlBnUoQiJlMLdHSfA9uK5Iz521NSK4jq7Ek3AcP7GcbLC4OPPhydKJlV_GSKV-pb2MtdVHaY5udutWMuIS2hIWEHHvEP1pbpbD3vfpHDCMy2oXMuxYGVSZlKEgJl-dRhs4Kxd6S-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a716599120.mp4?token=usYSXNy90fVwJ-Lty-lzwHvzy2MIYjOBQffCW9nGIKJz7siVUQnAjDts8wjwUcezHc5rgb0ot1VsLS_aVRBKuZo5SJAIiHFgKZMGJmL_ictCO95Nzbck6Nj6v0iORW_wA-M9R1eHFMHEW_SEA2_EZvp1R9PtQmzSfjSDuKNsGNCcz1Xbh8-nmfIWMrPmHeNvTxyNB78uuqu7JlBnUoQiJlMLdHSfA9uK5Iz521NSK4jq7Ek3AcP7GcbLC4OPPhydKJlV_GSKV-pb2MtdVHaY5udutWMuIS2hIWEHHvEP1pbpbD3vfpHDCMy2oXMuxYGVSZlKEgJl-dRhs4Kxd6S-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ به ازدواج زد؟!
🔹
فکر می‌کنید در ایام جنگ ۱۲ روزه و جنگ رمضان چند نفر ازدواج کرده‌اند؟
🔹
این آمار چه تفاوتی به دوره مشابه سال قبل داشته است. در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/677863" target="_blank">📅 22:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677862">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
تصاویر دیدنی از داخل حرم مطهر امام حسین (علیه‌السلام
)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/677862" target="_blank">📅 22:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677860">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smJuBhRvtKS36sNZZJxiVlidpO2FPNm4uZPYASsu7FiR4atAIbiqO5n6nd3e_2_dCNeAPX3gEFx7u00ac3oGv2giPZYWVlWx8PDeGEqiQMKeiw-sKRQJM8zzs-tlkN2K2pAcBg6SVDwZXxn64Ux59LjK97oO9lhn-uIAioYXwJ65XWGgV1b4mGcJAex07dVWRkbr2_JCLV4PcLKYNSHrky5ESOLiQi4kY3-EtdndvXIW7rIzLXP_umIfPMDvQzUvlNQ0I3HUiNOsIozunh0qcl-mpyI8LXdG5xyVq6JNhAs9_6Em10Y50_NXffpis3skOZvZjPG_vFBhgUeLuTYVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پولیتیکو: ترامپ در ایران گیر افتاده است
پولیتیکو:
🔹
ترامپ در قبال ایران با گزینه‌های دشواری روبه‌روست؛ توافق دیپلماتیک احتمالاً مستلزم پذیرش نوعی کنترل ایران بر تنگه هرمز است؛ موضوعی که در واشنگتن با مخالفت روبه‌رو خواهد شد.
🔹
از سوی دیگر، تشدید تنش‌های نظامی می‌تواند قیمت نفت را افزایش دهد، بدون آنکه تضمینی برای عقب‌نشینی یا تغییر راهبرد ایران وجود داشته باشد. ایران نیز پایان خصومت‌ها را منوط به پذیرش کنترل تنگه هرمز می‌داند؛ شرطی که برای کاخ سفید از نظر سیاسی ناخوشایند است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/677860" target="_blank">📅 22:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677855">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
الجزیره: طرح روبیو برای دور زدن تنگه هرمز فعلا شدنی نیست
الجزیره:
🔹
روبیو، وزیر خارجه آمریکا، از ایده ایجاد یک تغییر ژئوپلیتیکی دائمی برای کاهش وابستگی به تنگه هرمز سخن گفته است. کارشناسان این طرح را یک چشم‌انداز بلندمدت می‌دانند.
🔹
جایگزینی نقش تنگه هرمز، که یکی از مهم‌ترین شاهراه‌های انتقال نفت جهان است، به دهه‌ها زمان و میلیاردها دلار سرمایه‌گذاری نیاز خواهد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/677855" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677854">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ماجرای فردوسی‌پور و دستور ویژه رئیس‌جمهور به روایت سخنگوی دولت
سخنگوی دولت:
🔹
در جریان اتفاقی که برای آقای دکتر فردوسی‌پور افتاد، من در سفر جنوب بودم و آنتن تلفنم هم رفته بود، به محض اینکه از سفر بازگشتم، به ایشان زنگ زدم و گفتم که من خبر را شنیدم و پیگیری می‌کنم.
🔹
بر اساس ابلاغیه پنجم مرداد ماه، هرگونه مسدودسازی یا محدودسازی سکوها و سایت‌ها، منوط به تأیید ستاد راهبری فضای مجازی و دستور نهایی رئیس‌جمهو به عنوان رئیس شورای عالی امنیت ملی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/677854" target="_blank">📅 22:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677853">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvNnmC6IG9KBmoQArTacDGRR_fC0d8OkGJ5ut9KSc_pJrLra3dT65NZBJxQNDECm-buoJ5d5UHAISlrGlzaBXw-TgbOtWu0EuhRc55_CxV-TeaullfpKrmctGAXP2fBKBZWTxtqId9cP5lf5JpUjf4BbR_VYrSmieWggnXN8vBD8vfEdOTZpN3HL1bz5xb-hk7Azo8H89FVAA379QfTQjA5eMftX1RHlTnEHF9zE6GcHN8CasbcvlgxNSKgmkFnsQtPuB5pQ2QjuBxRgn-At5vlOFfH_f-obrElRmdholCpBgOCwUIUzHXHyLNIYL891fVUPuF8EjkhYXfQXtUOvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت پیکر دریانورد جان‌باخته و خدمه کشتی تجاری «آنا» به کشور
🔹
پس از گذشت یک هفته از حمله اوکراین به کشتی تجاری «آنا» در آب‌های فدراسیون روسیه، پیکر دریانورد جوان جان‌باخته این حادثه به همراه ۸ نفر از خدمه کشتی و با همراهی مالک کشتی، امروز به کشور بازگشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/677853" target="_blank">📅 22:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677852">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مراجعه به بیمارستان‌های دولتی ۳۰ درصد افزایش یافت
محمد جمالیان، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
هزینه‌های درمان به‌ویژه در بخش خصوصی به دغدغه اول بیماران تبدیل شده است. مراجعه به بیمارستان‌های دولتی ۳۰ درصد افزایش یافته که نشان از ناتوانی مردم در پرداخت هزینه‌های بخش خصوصی دارد.
🔹
بیمه‌ها با کمبود بودجه مواجه هستند و ماه‌ها است که بدهی‌های خود را به داروخانه‌ها، بیمارستان‌ها و فیزیوتراپی‌ها پرداخت نکرده‌اند. پیشنهاد تزریق ۱۸۰ همت به بیمه‌ها برای کاهش فشار بر مردم به مجلس ارائه شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/677852" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677851">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2e000076.mp4?token=WVStMu0awa0rX1Z8a8w6r82JiDuFlhmyPYdl_Bugqphke6WYdy_3LrkFQwgvEWuV-w2dHtzn5hjGehx6FajsVyE74ILPzGg71gG-LfVP_KWUvuQiCbzSxd8vGXNlUfVB3oi6FMDuNqpknaIGJE2VFtm5MDUCqN70CeuEomw5eL_VuemIIf71A13a2AEHLaZcg-UBydUVsoSs--OdYIkE7MFs1tskttwmCqIpTLFsVigQVtqQvnkSaXq3YncVFxClkRr9vIC3cGN_lPmb7uEFVrhFSaieEM2wKfFWN4WdlrZAkjephKxUHqQJBYV42YofdOPeLGSqfa0l0kHmFy0kTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2e000076.mp4?token=WVStMu0awa0rX1Z8a8w6r82JiDuFlhmyPYdl_Bugqphke6WYdy_3LrkFQwgvEWuV-w2dHtzn5hjGehx6FajsVyE74ILPzGg71gG-LfVP_KWUvuQiCbzSxd8vGXNlUfVB3oi6FMDuNqpknaIGJE2VFtm5MDUCqN70CeuEomw5eL_VuemIIf71A13a2AEHLaZcg-UBydUVsoSs--OdYIkE7MFs1tskttwmCqIpTLFsVigQVtqQvnkSaXq3YncVFxClkRr9vIC3cGN_lPmb7uEFVrhFSaieEM2wKfFWN4WdlrZAkjephKxUHqQJBYV42YofdOPeLGSqfa0l0kHmFy0kTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی دولت به شوخی‌هایی که با او در فضای مجازی می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/677851" target="_blank">📅 22:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677850">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40631b97ca.mp4?token=ZSaWjov-q5vJs-LeDJWGDH4fGYX19IET-9WcYGGY4ikqMN7OEKwyOEQskrgdDXVXswpJYxtCem4veiq7nDu-d6iel0ogYVPQelm5uiGAUNr0tcZjdbgPgmA4jG_Hx9km6Mr--wp-QDb457s96qJPO01wENG_JU6GBJpLeHzEitWkBFL1C2GKX78le7UfrwEkMEUCbcs1UyJgzR3Wg6D1HIRtSkIejyAYrkCimmkLaxkx9E_5c9PoLCa1sHfq57cCoGMyOJ8XKO5X-0sKDfcOvFFdmdQl1YkqiFwDbQQGSNrMX7-zI5UAKdw-v9Bp1U9MTpBJ-J2_lfLPVd3zKbBA5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40631b97ca.mp4?token=ZSaWjov-q5vJs-LeDJWGDH4fGYX19IET-9WcYGGY4ikqMN7OEKwyOEQskrgdDXVXswpJYxtCem4veiq7nDu-d6iel0ogYVPQelm5uiGAUNr0tcZjdbgPgmA4jG_Hx9km6Mr--wp-QDb457s96qJPO01wENG_JU6GBJpLeHzEitWkBFL1C2GKX78le7UfrwEkMEUCbcs1UyJgzR3Wg6D1HIRtSkIejyAYrkCimmkLaxkx9E_5c9PoLCa1sHfq57cCoGMyOJ8XKO5X-0sKDfcOvFFdmdQl1YkqiFwDbQQGSNrMX7-zI5UAKdw-v9Bp1U9MTpBJ-J2_lfLPVd3zKbBA5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نامه‌‌ای که دختر شهید مدرسۀ میناب برای پدرش نوشته بود: تو همۀ چیزی هستی که من دارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/677850" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677848">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdWqTYwKv532hnweOwG0eflMi_TsYLghFIcKIYORIQ4-N1HXW5STKlgGGDsTxXpoBEW4HITQk2MGihEJBAOVkqVEYRet4qGzHV9T2ZyuqZkR9GxRMIlPtOG6Sl_fQ5AvBUJs3ugb75__U1ymZpnNGTy8iH8rPoxTG-Odccq7hwAliKeCV6T5ZflI-NLP9BM0Zfxdqc5bH_gEGZPXTIobTR4-BEyHualnFqmNi2qVml86O9vHb1jo2l98OzR_WUuLkSftXwDoKddK5L05IyckfJfQkyw3UdFWVUZ9LgewzHG8ufXTlQNZWxzRketD0bOUPPVk9_jeLoByWZWEQ3OsUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رسانه ژاپنی: پاکستان میانجی شد تا ۱۰ میلیارد دلار وام از آمریکا بگیرد
روزنامه نیکی آسیا ژاپن:
🔹
پاکستان برای تقویت ذخایر ارزی خود، درخواست دریافت تسهیلاتی تا سقف ۱۰ میلیارد دلار از آمریکا را مطرح کرده و در این مسیر از میانجیگری در موضوع ایران بهره برده است.
🔹
با این حال، کارشناسان هشدار می‌دهند موافقت واشنگتن با این درخواست می‌تواند به افزایش نظارت آمریکا بر بدهی‌های پاکستان به چین منجر شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/677848" target="_blank">📅 22:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677847">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Veglpo4S2--qrdGUkR_8vdcoS5IO0rvnLOiXB0dBhBy0XZDQ-Y_fqaYLNmWAn3-n_R1e5jKnn9nMMmFXR9pR5H_85-aarQGf7RwTllWEztN447DklOEqecGHrSHrmJIO0nCF7_YodZor4m-VoUJ3Cc5sNR4juTALC0CJvgoM-3w76UNCy5mk_eX4bUYyWCLFeI6EufY12oTZfR2k3UZQQL-CpUxtj5UPb8rY7t_F1-Q-3nZgJHCqHfIVrfTV1S8WFyKvVGsTV1k8wXfwIxmbkPBPDuIKiOKdScukChdP8UeND-4ot59ifWDHAxvsKi3Kho-OyLOLterprPbC6W9PgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارزش آدم‌ها فقط به حرف نیست، به کاری‌ست که درست انجامش می‌دهند
🔹
در نگاه امام علی(ع)، انسان با توانایی، مهارت، دانایی و کیفیت عملش شناخته می‌شود. هرچه انسان در کار خود پخته‌تر، مفیدتر و دقیق‌تر باشد، جایگاهش بالاتر است. این حکمت یادمان می‌دهد که برای ارزشمند…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/677847" target="_blank">📅 22:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677846">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
قاتل را بکشید
🔹
پرچم بزرگ دانشجویان ایرانی در پیاده روی اربعین و فریاد خونخواهی رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/677846" target="_blank">📅 22:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677845">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Fg2K4OpQ_x_KLZur2sQxk7ChX_JhhLZySPeLE5CQRsXHO2gM-24QPUu-hdKD1kka_nqa3Dow_RalIy3x4f5aP1DWE8x_LekPvdnsIYuLeJGHQgBEbUU1qvZdcKudmhdAl4xZO2TiM6kP-Jg9CuCnEX5duKM97RdjE43ovQ3vkW7K3U5MTqU14P_Pod7sPpKAht98LaMVcatXjmq4kEowHyKURi2mjw4UJ08RPSifxkO4YM-60BXT-WW4nGfdqRkIyFoCyF-NIsAJx3gSJlrya1dv08ky_TPVE3Vbmnyg1OPoStqpn6xZkD53xHXY3xmdBfnDUeztzkyUeibT-JXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/677845" target="_blank">📅 22:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677844">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2241265b.mp4?token=tAStjb-85Kg0WX22NSudcqzCnOFsFJOwDMzDKj8S-u7iMemLS_XN1YCbuT6nlXNUOwkqfdK-Fzyw8_1p35ho6qD519wa3JuenJieu6q8gZ0AIIvkPhntaGxiVSY2-wpzSe-6ik8IJlZ6-y7vUZ_B3skeUMHUxh0gnNPNthQPOcwD8qQvCSQoSgfgTQWkanfo9T6Rr2ehnnG0ni1SSslz2j6jCb4vmIgyRuMJizn6WcgLaCow23SydiDlaKpkdqxKqiBgzyIkPh2_tEHg-o6h1UgG6vvzpiWw2VZn1bkcOBwMC8_o1itBfHd7WcaSLLGmQNr_yxMe4MwRUlDoUYAf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2241265b.mp4?token=tAStjb-85Kg0WX22NSudcqzCnOFsFJOwDMzDKj8S-u7iMemLS_XN1YCbuT6nlXNUOwkqfdK-Fzyw8_1p35ho6qD519wa3JuenJieu6q8gZ0AIIvkPhntaGxiVSY2-wpzSe-6ik8IJlZ6-y7vUZ_B3skeUMHUxh0gnNPNthQPOcwD8qQvCSQoSgfgTQWkanfo9T6Rr2ehnnG0ni1SSslz2j6jCb4vmIgyRuMJizn6WcgLaCow23SydiDlaKpkdqxKqiBgzyIkPh2_tEHg-o6h1UgG6vvzpiWw2VZn1bkcOBwMC8_o1itBfHd7WcaSLLGmQNr_yxMe4MwRUlDoUYAf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوابیدن روی زمین؛ درمان کمردرد یا یک باور اشتباه؟
🔹
واقعیت این است که بدن هر فرد متفاوت است. بعضی افراد روی سطح سفت احساس راحتی بیشتری دارند، اما برای برخی دیگر، به‌ویژه کسانی که مشکلات ستون فقرات، دیسک کمر یا درد مفاصل دارند، این کار می‌تواند باعث تشدید درد شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/677844" target="_blank">📅 21:59 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
