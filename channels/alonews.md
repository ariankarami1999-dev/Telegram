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
<img src="https://cdn4.telesco.pe/file/DGuTU-AmW67wLSqyIDJBbm3N1Yt4345HJCPahSokEtGFL2nxz_nFxcuQXC-snOYwJGdCjrU_2dX7F7EJQn2RrftnuCmwwQcY6MwdD2d5mekoj-XLSw2oUVVxpteKCXj5HPLVI2inDzVXggJ0RFHHTS5jEaZkimS5TUxizHP1AQ6Pvza9kXKvJSN601ICXyzY6JsJ2I_GYDRbRxm2cqARdVcKb4W61OmWgBfWavYEb6RZ7J8adOIjw--tY6MAyBW3fuKS_9LokFTky5YjEQ2sg6poWWpaHrjql-ctA1DARqhB_kmloUNF1pYWTtDky2rErLtEZh-zqB0qT5ptF0b3dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 22:28:39</div>
<hr>

<div class="tg-post" id="msg-136788">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947be4f21a.mp4?token=Eg_RDL_CCdO8rJLu3dAYNve9nrobyQLnVvXnh0eJEkKaT7-iA4W4IUJCRyaaTzQ4Quocf1tkHhRGLPOyxsY1l5W6p8bDZo0Yomku2gn71CNymBBKx100l_yEHoCg0JcTF-DZHtTqG0Qrrf3mN3puhAia2F6Kd4gttYqRaD-3TuyIM32OkOzCwAwpmrPmqoUPN65Fy_jzjTXIhlHrNU4RGiSEzQ339UuztB9bOzEFrL-Oyenh4iH_eFPoBcRrbk1oVCJ0pP8_POWiEZefvVppXWCYrOi6DsmzyZhDyFVxd4xYihmnspezV7ARC3fHxQgRZbNs89sFsXkQyqw48wrD-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947be4f21a.mp4?token=Eg_RDL_CCdO8rJLu3dAYNve9nrobyQLnVvXnh0eJEkKaT7-iA4W4IUJCRyaaTzQ4Quocf1tkHhRGLPOyxsY1l5W6p8bDZo0Yomku2gn71CNymBBKx100l_yEHoCg0JcTF-DZHtTqG0Qrrf3mN3puhAia2F6Kd4gttYqRaD-3TuyIM32OkOzCwAwpmrPmqoUPN65Fy_jzjTXIhlHrNU4RGiSEzQ339UuztB9bOzEFrL-Oyenh4iH_eFPoBcRrbk1oVCJ0pP8_POWiEZefvVppXWCYrOi6DsmzyZhDyFVxd4xYihmnspezV7ARC3fHxQgRZbNs89sFsXkQyqw48wrD-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: چرا تو تجمعات شبانه کسی با دخترای بی حجاب کار نداشت اما تو کافه‌ها گیر میدید؟
🔴
چمران: هه هه هه
😊
😈
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/136788" target="_blank">📅 22:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136787">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
بریتانیا: از شهروندان بریتانیایی که در حال حاضر در خاورمیانه حضور دارند، درخواست می‌شود برای احتمال لغو پروازها، بستن موقت فضای هوایی و اختلالات احتمالی در سفر، آماده باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136787" target="_blank">📅 22:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136786">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بریتانیا: از شهروندان بریتانیایی که در حال حاضر در خاورمیانه حضور دارند، درخواست می‌شود برای احتمال لغو پروازها، بستن موقت فضای هوایی و اختلالات احتمالی در سفر، آماده باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/136786" target="_blank">📅 22:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136785">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/136785" target="_blank">📅 22:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136784">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuQe8RfSBNUfUa65SUL7ZSd8JW__Ca3h8JsY6vGvCCccCSPzCChtIiMtPmQbyHEu51Cv-79dlRz6sdTV8I40mZiBPxjAOF7RMsaRMvTzo0pezDcWHs9Hqpted4j4TjJ_kIUJOmhhcsw6WYJ8ZRRPA2jLC73KQRpaJJIeBpxiOY56JZZTBH-c3ueaHB0WlKegwmaH7HpVBNlYB1Ywvrb9UvTK3xfNUuP1Hhx5cYUmr3gg7kZDy_EwWBakLGspL4KolMvREBU6xVlpLWIkAllgaWZx-82Bp9KgMmcHIuTnWhnmf2twglVhjQ0t11TgvmHND1wPIr03Sux-_3r_5zN4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما تعرض شود خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136784" target="_blank">📅 21:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136783">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759f0f62bd.mp4?token=oWFLG4p0lQXOIqO8n5TOLds4Vzla0DEJDP_-OsDBRbu5RooCfNnijG-JvEgO-6ZEO0gbxXzRm06Lp3CM-gKlYKKfHXYrAd_-L6YbAZUGQj0NsXQXjEsa7gdGjUxZEqhTurvq7RMq6Aie2dnogvk96wWb9Hvz3DWrX_Yx4hDvOaDFKw0GNm877SsWa-2dxousvjRD6pYDpdGzEs0oEZbQ3n0_mYEQnXUwIXxsdLWU5L9jpi3qzojt7z5o89l5TdKVadWeEdf0s58tyqs_QeB6NZJtg5HWvEOSCuavJvDodG-5kno9isSh99o85xENuhxsp4nCcnonPB49ht4sjwNWuByPfEUuYgSgWfZRiOGqR4yoBzO2ojP-1-el1ICFAVaDj9M18eTv0JpQRS_jA3GUUQ-XwAvNY8pVDRniLe31kODIRy64dyKljlX2ZwLd6XECbyuFNN_aPHPIwPH4b8GfFlVzudTMBzZFjw6FIJV4bVdHplDOto-T7X2mNOkPslxpzFXdzR6Kznq2mLPDffyiskibqf4QEhRTw-rWY7-7qcMMm5jczIkrk3uY8tRMSB95VVXB38Mw5BDM1RF_TVQgwGdRdXCe7CyHOpPcMZoYkIvgEFxBofAZng_vfrPDntoA6-JPjXVaN1JDdhiHUzObAjIqDBoUJ1d0I4QtzvuW-Yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759f0f62bd.mp4?token=oWFLG4p0lQXOIqO8n5TOLds4Vzla0DEJDP_-OsDBRbu5RooCfNnijG-JvEgO-6ZEO0gbxXzRm06Lp3CM-gKlYKKfHXYrAd_-L6YbAZUGQj0NsXQXjEsa7gdGjUxZEqhTurvq7RMq6Aie2dnogvk96wWb9Hvz3DWrX_Yx4hDvOaDFKw0GNm877SsWa-2dxousvjRD6pYDpdGzEs0oEZbQ3n0_mYEQnXUwIXxsdLWU5L9jpi3qzojt7z5o89l5TdKVadWeEdf0s58tyqs_QeB6NZJtg5HWvEOSCuavJvDodG-5kno9isSh99o85xENuhxsp4nCcnonPB49ht4sjwNWuByPfEUuYgSgWfZRiOGqR4yoBzO2ojP-1-el1ICFAVaDj9M18eTv0JpQRS_jA3GUUQ-XwAvNY8pVDRniLe31kODIRy64dyKljlX2ZwLd6XECbyuFNN_aPHPIwPH4b8GfFlVzudTMBzZFjw6FIJV4bVdHplDOto-T7X2mNOkPslxpzFXdzR6Kznq2mLPDffyiskibqf4QEhRTw-rWY7-7qcMMm5jczIkrk3uY8tRMSB95VVXB38Mw5BDM1RF_TVQgwGdRdXCe7CyHOpPcMZoYkIvgEFxBofAZng_vfrPDntoA6-JPjXVaN1JDdhiHUzObAjIqDBoUJ1d0I4QtzvuW-Yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند
:
علت قهرمانی اسپانیا
،
عدم کاشت ناخن، نزدن لاک و عفت زنان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/136783" target="_blank">📅 21:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136782">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گزارش کانال ۱۲ اسرائیل، مقامات ارشد اسرائیلی نگران هستند که ایالات متحده ممکن است به عربستان سعودی اجازه دهد تا در چارچوب یک توافق هسته‌ای مدنی پیشنهادی، اورانیوم را غنی‌سازی کند.
🔴
یک مقام ارشد اسرائیلی این پیشنهاد را "تهدیدی برای امنیت اسرائیل" و "خط قرمز آشکار" توصیف کرد، در حالی که مقامات امنیتی هشدار دادند که این اقدام می‌تواند باعث یک مسابقه تسلیحاتی هسته‌ای در منطقه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136782" target="_blank">📅 21:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سفارت انگلیس در ایران تخلیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136781" target="_blank">📅 21:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
منابع عربی: صدای چند انفجار در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136780" target="_blank">📅 21:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نیروی دریایی سپاه: اخطار می‌دهیم که از مسیرهای جایگزین تنگه هرمز استفاده نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136779" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
در آیین دریافت استوارنامه سفیر جدید پاکستان؛ پزشکیان: تلاش‌های مسئولان پاکستان برای تقویت صلح، امنیت و ثبات منطقه‌ای شایسته تقدیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/136778" target="_blank">📅 21:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فعالیت جنگنده های ارتش بر فراز کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136777" target="_blank">📅 21:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
منابع عبری از شلیک موشک های ایران به سمت اردن خبر میدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136776" target="_blank">📅 21:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار مجدد در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136775" target="_blank">📅 21:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6gMZW2YEYsHNLVlvEzbdXHEZl0e7Ezk_lwq2n3A9LrcrUcgtFv1zug446cjdnrxYtdwWvoKQf8tg5NHUpMh90fmQSuGUX5QuH9CJB5xGEtf02oIVAP466BzUIOqQ5Nrq5TL9oayF8YzXiKvz1NhbTkbzCJkG-oTloK_8Y6c3K4rG2UKrh74xmIkqRhCwwdPM3r5Nf9G2rhELcq8m29auoNI6XTrQFv9l3CJzNYsnQF71OGHBxKa6afVMdyJAbgRs2NAQtq9PQyEX_fJNUZNcju8ohqI1zHOTo7Jno__6-wffK8SKWlMN1NpNUIKEptqEPWLoANst_x7Q6j0upv4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور آمریکایی: ترامپ به‌هیچ‌وجه در دستیابی به توافق هسته‌ای با ایران جدی نیست
🔴
کریس مورفی: توافق هسته‌ای ترامپ با عربستان برای غنی‌سازی اورانیوم در این کشور موجب به‌راه‌افتادن یک رقابت هسته‌ای در منطقه خواهد شد و انگیزهٔ ایران را برای محدودکردن برنامهٔ هسته‌ای‌اش بیش‌ازپیش کاهش می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136774" target="_blank">📅 21:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136773">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFogKSwRUBcdVw9EMPzTxm3TezN4rJHOMYgg8Q-KyEcFMlF8-l9cmBqdTTA4cqEhowClY0dfGg-ndhyu0L0U046wziTvbGXYc-tieLkmwyUciZW9Jgclsosozi_NSSQJuW6ir0HaXU360BubasN19QMRyMmhb419HsrIdalEP5MHJkK1mgiM4J4CDzku0UHizBMV_W6kTLJl_lzV67Q80nY1DyPB1q_KLPDrvfITkCk2lB1JByYR0mpbWPctpAFiIZqi4sg1Xq7f9eAdgL95Y2cKmtOf-4R2fE6NAfDZ1_nZsbKInir07G4EAXQSuzS_873LBR2LYZzvXUZQwA75bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته دو منبع مطلع به آکسیوس، رومن گوفمن، رئیس جدید سازمان جاسوسی موساد اسرائیل، دو هفته پیش برای گفت‌وگو درباره جنگ در ایران و برنامه هسته‌ای ایران به واشنگتن سفر کرد.
🔴
منابع گفتند گوفمن با جان رتکلیف، رئیس سیا، و همچنین مقام‌های کاخ سفید دیدار کرد.
🔴
در حلقه نزدیکان ترامپ، رتکلیف یکی از صداهای تردیدآمیزتر درباره یادداشت تفاهم با ایران بود.
🔴
او پیش از امضای این یادداشت تفاهم هشدار داده بود که ایران بندهای این توافق، از جمله مفاد مربوط به تنگه، را متفاوت از آمریکا تفسیر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/136773" target="_blank">📅 21:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136772">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
روزنامه قدس وابسته به سپاه:
وقتشه که این گیم نت ها و این مراکز رو جمع کنید و همشون رو بکنید پایگاه آموزشی برای جانفدایان کشور تا در صورت حمله ی زمینی دشمن آماده باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136772" target="_blank">📅 21:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136771">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">💔
مادر جاویدنام
#عرفان_رضایی
قلب هر انسان باوجدانی رو به درد میاره.
🤔
حرام زاده های حکومتی که دم از وطن و دین میزنن، قاتلین هم وطنان ما بودن و هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136771" target="_blank">📅 21:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136770">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سفارت ایران در اسپانیا خطاب به آمریکا:
تا می‌توانید تابوت آماده کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136770" target="_blank">📅 21:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136769">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
گزارش اختلالات شدید در سیستم GPS در سراسر خاورمیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/136769" target="_blank">📅 21:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136768">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q478gblWV6TTLQYZo1DkiyZNl3wCj2oxMJUbNe9rwZ3AYble1cS1T8FRsP0gcemQ9QOSJjBNgTq3ObKqCZNdaXaKELqTyqZ9aa8qabhLepC2TmpZ5-9Q3JwkI5GhjYjsv4_nyiWuU8ZNp2L-N54djmOFN6EWpI6vIvZ0HsPg1KTqHqM0PlWGU6ZjU4uuz4yY_dEOlL-Iv4_sN5V6_xAme8GHjAS8X-znLz0yOoBPvorVDUJT-oZfmkFzvcUsEpdhcenGkTxO9rqb0H7pAtDA0fHBOf9_Nc0bqVxJXOMbxqZEGf-N2MN9VTJQZhm11hnCkH2_coyPhVu3MxT-HmL69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: دوست داشتم برم بندرعباس باشم اما پروتکل‌های امنیتی نمیزاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/136768" target="_blank">📅 21:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136767">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
گزارش شلیک موشک بالستیک از اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136767" target="_blank">📅 21:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136766">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
هم اکنون حمله به اربیل عراق و فعالیت پدافند هوایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136766" target="_blank">📅 21:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136765">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136765" target="_blank">📅 21:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136764">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2AYcwXTL9sCDcPQrxi6UL3-mpTwzsUic2HaTvH0isWZDjl-T3Les_hQYyACldSkAaq5Aqr2fASFPkErR9KidKn8CIo06b8fJvIkXR2pvCmM4bPbdXUAubwZoxrpjbH-FDnKtzdYlsmsFNatrM7egFFByxoMVeK2Gpnjl6UAeAHosbop5jAe7N-xxY4NnnDmmvVwg6mAjQ5HnKCQIoRHfgDrWorzLmyV07iQb4goCtKti4KQ7bAMhvhpVB-xxtTKOGQxSUZktprJSHNi5EJAwjsEUXaNEDhSs3upy-IrgWWsBh8f-kDjJsULsCOhq4bO6qGFCfQRR850qExshMDCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: معادله این جنگ کاملاً مشخص است: یا همه، یا هیچ!
🔴
در منطقه‌ای که ما نفت نمی‌فروشیم، هیچ‌کس نفت نخواهد فروخت.
🔴
اگر امنیت ما تضمین نشود، هیچ زیرساختی امن نخواهد بود، و امنیت تنگه هرمز در غیاب نیروهای آمریکایی تضمین می‌شود.
🔴
ما بارها گفته‌ایم که وضعیت تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136764" target="_blank">📅 21:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136763">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سفیر چین: پکن مایل است نقش سازنده‌ای در بازگرداندن هر چه سریع‌تر صلح و آرامش به خاورمیانه ایفا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136763" target="_blank">📅 21:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136762">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CigfR1Qif4-qxdeqdKgSYiOCXqvWEhm9fJ0zdEYnVTMRdIZHpH9eNqor6ocO1sXJO0LJaE4OTUHP84hZVVlLDZT_Fa6wrF9C5frjX5m1ADAi54fL8WO00WjUlsJl54EQDkIvIIR6w3ny4EK67VaRaTm_o9__S3jxa4yUcqauasmIhqNNIUTSBiYZkqnkCAkCP9J7t-aCxGX3qz_V-ctVo-MkePjEA7XJx2KYZg2ytiQ23GKsyS5aZsIdIW8NSVV2rXOwUUNjrx6u67YdXivRzQuudwK52_wRdiUK7f8LSWtry8l0IS2Q5_db9jYXqZuojjb2fEuZI7X95__TpddylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136762" target="_blank">📅 20:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136761">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
به گزارش واشنگتن پست، دولت ترامپ در حال بررسی امکان انجام حملات نظامی در مالی علیه گروه JNIM است که با القاعده ارتباط دارد.
🔴
این پیشنهاد باعث اختلاف نظر بین مقامات ارشد دولت شده است. گفته می‌شود سباستین گورکا، مدیر ارشد شورای امنیت ملی در امور مبارزه با تروریسم، یکی از قوی‌ترین حامیان این اقدام نظامی است، در حالی که برخی دیگر همچنان مخالف آن هستند.
🔴
یک مقام ارشد دولت آمریکا، نقش روسیه در این منطقه را مورد انتقاد قرار داد و گفت که مسکو «به عنوان یک شریک امنیتی موثر برای مالی شناخته نشده است» و ابراز امیدواری کرد که کشورهای آفریقایی دیگر «به عملکرد ضعیف روسیه در مبارزه با تروریسم توجه کنند».
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136761" target="_blank">📅 20:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136760">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
پزشکیان: سفر نخست‌وزیر عراق می‌تواند نقطه عطفی در توسعه روابط راهبردی دو کشور باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136760" target="_blank">📅 20:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136759">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc7VxFd_nlTHe8Sa4j9uA0vBZyT2Mu7Hh9rJxxBEfjVw8ifGgl-TkHnNxHW50FtB79QON1TrrEW8ME4_1332Q7qvulaRp3JAkMG4NpUvfeeEzhX4g47LNgYWqMsCBVOIUQ4_YRDWcwW-qsfWQX6Bgu4c6nOwBdQbmIcUCr5J6EHTTysgq2T59m4qpcj2gRNf9-WlkwM1YIhDKYvTB5Xu6A7GIvgBfYXRx8M51zJ57KSFtt0k1PtjL4DbiFji_EhQBVwvxpmYU8U6ee8GlKU_TpwTQGRoMB7wFuw8sTPhmRwF4wwfVInfCEf9W4MoCI7scKeMA4Xv9dmmiR2xmxWHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیباترین پیامی که تا حالا تو الونیوز داشتیم
❤️
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136759" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136758">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8ff091ba.mp4?token=mPyk_qLQVwUn7DTw_7zAfnmxc9upslg29YcxpHsaFtpGPyX9CRI-Z3PLU1aspusLcv4YI8-HjF9SbvMgNyyfNZ4Wc7AvC71xvRmPM7wIGkhwHeW24jB5XUfH5GxxNQ90clxEKylqQJcX9P9kQ_1ECJFRYCaoPDyl-cECJk_omrmhJt06e4WfkiRZ-TsgGjj6ZFyARmw49t5s9n8tcQNyHKifeqnIAWUcceddlNzju9Q7GMm6CC1WnmuA7hrnxslKDSxz7wBzHbnhZWS3o9WgkJSh_q8bYYzASA8SFipraopCgiWFOym7LaPAY6K6wE8WuTcgxzCiNe5yeHRMrxm6gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8ff091ba.mp4?token=mPyk_qLQVwUn7DTw_7zAfnmxc9upslg29YcxpHsaFtpGPyX9CRI-Z3PLU1aspusLcv4YI8-HjF9SbvMgNyyfNZ4Wc7AvC71xvRmPM7wIGkhwHeW24jB5XUfH5GxxNQ90clxEKylqQJcX9P9kQ_1ECJFRYCaoPDyl-cECJk_omrmhJt06e4WfkiRZ-TsgGjj6ZFyARmw49t5s9n8tcQNyHKifeqnIAWUcceddlNzju9Q7GMm6CC1WnmuA7hrnxslKDSxz7wBzHbnhZWS3o9WgkJSh_q8bYYzASA8SFipraopCgiWFOym7LaPAY6K6wE8WuTcgxzCiNe5yeHRMrxm6gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسیر جایگزین پل کهورستان که در حمله آمریکا مورد هدف قرار گرفته بود؛ نه تنها فعال است بلکه آسفالت هم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136758" target="_blank">📅 20:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136757">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
دبیرکل شورای همکاری خلیج فارس: ایران با نقض اصول قوانین بین‌المللی، به حملات خود علیه کشورهای عضو شورا و سایر کشورها ادامه می‌دهد.
🔴
ما اظهارات خصمانه شبه‌نظامیان حوثی علیه عربستان سعودی و تهدید آن‌ها به بستن تنگه باب‌المندب را محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136757" target="_blank">📅 20:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136756">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0HkOezMYrdhMs9uQ3fvjqcOgJMrF6_EourbCJJriYXtuNhQrmLywi4wQu4uYRl12Wy5zMI53HTxd0NbKpWJekEsyiqB-GjQJ4Qk2AWeW4BhYgZiwHjsWHhoTCWb9hOFfHm_RR8wee88d9deYvdlwV6XEVYAFLfaxZz9ZsTyZZiZjsGjPmjazufN8YB7_ulpa7Dy3iBbgZGUxO99mY-NdCLTllYAhJJyIFS0i_70dmy5BVEfqV9td-3JdkAZIImqTldLoZrrcfEewx3qeZRkBOcmSe7huEk_KtoTXEawwcArYVxj0EoDZrz6n1xqAUecYMx-PRdsmavkVzxiiMdZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ یه پستی رو گذاشت که توش نوشته : پس از کشته شدن سربازان امریکایی، ترامپ به سنتکام دستور «دروازه جهنم رو باز کنید» و حمله به ایران رو آغاز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136756" target="_blank">📅 20:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136755">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
محاکمه نیکلاس مادورو، رئیس‌جمهور ربوده شده ونزوئلا در دادگاه آمریکا آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136755" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136754">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
میخائیل اولیانوف، نماینده روسیه در سازمان‌های بین‌المللی واقع در وین:
بیچاره بریتانیا! رهبر جدید بریتانیا از ابتدا کار خود را با اشتباه آغاز کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136754" target="_blank">📅 20:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136753">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی مسیر ۹ کشتی تجاری را تغییر داده و عملکرد یک کشتی دیگر را مختل کرده‌اند، از زمانی که محاصره بنادر ایران را از سر گرفته‌اند.
🔴
افزایش یک کشتی در تعداد کشتی‌هایی که مسیرشان تغییر داده شده، نسبت به گزارش دیروز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136753" target="_blank">📅 20:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136752">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwd_Amx_nzvg8wXMV7nEeffAWK1jjhfrYIdG8NzbFK4fzEUMNIxOutAYB0kMfpIoNZ7SeW9f44xBDMjUj8knEa1ixdSgeOKkM7Uojc1eAGqcpgEQHocAhWbAKPlZd8EEhl99M5HC_MlKRgYFr79xq2xbwmECWqwgTsjrahwE-weodQFlVmCCr1wnNRF-2NK60nojCYw4cp5XDSyf3909GZwUAkK9A2O7GrLPE7xrqeXnN8C3e8ZIwLSxsjvg9N1_julbrRN7vePB4lzYWe9-Sn_3OtQ7ZrE5SWoZlktf3kJdscApCFya5BqP9-CB3GE5tI_yekbaqxdSOUQI_NrEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محاکمه نیکلاس مادورو، رئیس‌جمهور ربوده شده ونزوئلا در دادگاه آمریکا آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136752" target="_blank">📅 20:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136751">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YS8jQXUIvMb9DoM7JYRu6kqMCvf8Fxy7LHFnwraGeZQfb4Z1QeGzSZw8niAedMqxinj4TZ5doPcq3IozHrPKVGZQ_m19xW520-fNsjCv0P6ikgF7eU8I2Irwad-wIQmBgvDtywWZWs79w6EWnqJpSsyXHFVShpfKLtZV3j8v5sQMgIg9RnRUUoR9mvS3Uy7eu3DOjlg0MMro3auWpJBEAxvT2IXhlCA3m4bLtWG1QGvbV1_HuNxwMRkWJ8rlwQ9BdOMPfB2FhQgJ8GRS58L5NnP__HVUwP5i9eDAoOzlgzyype2rM0Bmp5DvqKE2vO8ea6_pMjWO9Fs3Xvr67VMZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گسیل موج جدید هواپیما های آمریکایی به سمت منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136751" target="_blank">📅 20:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136750">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ، با حضور پیتر هیگ‌ست، وزیر جنگ، و سایر مقامات ارشد، در پایگاه هوایی دوور، به انتقال با شکوه جسد چهار سرباز آمریکایی که در درگیری‌های ایران جان خود را از دست دادند، ادای احترام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136750" target="_blank">📅 20:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136749">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اکونومیست: جنگ علیه ایران ممکن است ریاست‌جمهوری ترامپ را ببلعد
🔴
او امروز می‌توانست در موقعیت بسیار بهتری باشد، اگر توصیه‌های سیاست خارجی اوباما را دنبال کرده بود که می‌گفت «کار احمقانه نکن»
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136749" target="_blank">📅 20:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136748">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhtSOZDJRvCZyI5XRZlUMI1BmrYKy3CUvB0gPl78qmNfq4xUTUzXfk3MnRCJGFca7F_w9la_UtD9qU_EZYb34FN5aVJFKNL9W3ZwyTEfeNu5SWoeMw2gKE7VZAkWnHICr-v7N_nxtW10FqTmr5ayZ661pIlWQAxcBztv_FRlrmqKm1fuQVlzfRuDVKGvrTq_7ENxCM0dRxmna3cQACADCl0lss0w81Lw5R3QSTrRNJR_PHSPKRRMQIlKBU5HOB_zSb9xXTSio5W9ycoCaufYDGGxAf3w3v7Hdi-5Xjw1VSUI_I-segPCTZxPBOGxekNiVXp8KCXJCCiFf-PFE4APPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفتالی بنت ، نخست وزیر پیشین اسرائیل: توافق هسته‌ای احتمالی آمریکا و عربستان، شکست راهبردی برای اسرائیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136748" target="_blank">📅 20:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136747">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
اساس مکالمات شنودشده روی فرکانس VHF، نیروهای مسلح یمن به یک شناور سعودی در دریای سرخ هشدار دادند:
🔴
«برادران، مسیر خود را تغییر دهید، در غیر این صورت با مرگ روبه‌رو خواهید شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/136747" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136746">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💢
فوووووری/کان: این هفته حملات به تهران میرسد
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/136746" target="_blank">📅 20:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136745">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
هم اکنون ارتش آمریکا در حال انجام عملیات تخلیه تمام هواپیماهای سوخت رسان و ترابری خود در قطر می‌باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/136745" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136743">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU_9xMgt_BpNDH49OfvJnLQ0VAeDwGEDZaqtGfPVhIThQLjcnuN4Rt3_229ZJY-mxdK_LzpTQ94ZsxcWoejOwigo5xkRlbFiTBolc7XCgxS5v5R1giJC950AU2TNIig4wOxwaJPyFfRuvypHMb7m9Ywb3gkptkHUiHEOOTLyTEgXYQ7bARzwxQdomgB9R_OpTBWJHvsDYS4ajwQCCyDBZCFeOTTGQ79uJJR9GhvWSxqqCcx8qhGhst5eTkyTNOxsjo2MsTjOOayH_C9eAtkRp7K1b6KhmCEonPLzazbsHKKWVP5qGPqVd6B4FtxhvhpJwOeaD9ZTYb0rn1-BtPKclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af19d389f.mp4?token=ABFr21H6UvkSzd-a7pAVRnipxld6aamIs0TAhMiVs2D0OnAPJSKAxMrUeswex_devhhewR0QYMnfUQncofcozLOcLy1tkClFMmgOOQVA8ytQCA0a89-o2qZYxYUwSa-fgzIthc_09MV25k8MrpDxLC_s2_ZV591yNAhtj7kx2P7FJ-Fs8VOkJeOzAtgJUABo2dBEapAtauHqcz_3VC05OagEae3yYbrA-WyGLPHps0C27pOIslRgSJ9Q_JnP7I1z59HKTshnwb2ZRFaUMgOQKVdZJKVdSTgUynBcstLTOsFhCNcKWHHy8pXqjTCCA0OsH0iM-kMfOBg6NBEJjfx-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af19d389f.mp4?token=ABFr21H6UvkSzd-a7pAVRnipxld6aamIs0TAhMiVs2D0OnAPJSKAxMrUeswex_devhhewR0QYMnfUQncofcozLOcLy1tkClFMmgOOQVA8ytQCA0a89-o2qZYxYUwSa-fgzIthc_09MV25k8MrpDxLC_s2_ZV591yNAhtj7kx2P7FJ-Fs8VOkJeOzAtgJUABo2dBEapAtauHqcz_3VC05OagEae3yYbrA-WyGLPHps0C27pOIslRgSJ9Q_JnP7I1z59HKTshnwb2ZRFaUMgOQKVdZJKVdSTgUynBcstLTOsFhCNcKWHHy8pXqjTCCA0OsH0iM-kMfOBg6NBEJjfx-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی اخیر مرکز فرماندهی مرکزی (سنت‌کام) به نظر می‌رسد حمله‌ای آمریکایی را نشان می‌دهد که به پوسته‌های خالی بمب‌های هوایی یا مواد ضایعاتی مشابه در بخش نظامی فرودگاه بوشهر در ایران برخورد کرده است.
🔴
تصاویر ماهواره‌ای نشان می‌دهد که این اشیاء سال‌هاست در همان مکان باقی مانده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136743" target="_blank">📅 19:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136742">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
یونان در آستانه تصویب خرید ۳.۴۲ میلیارد دلاری سامانه‌های پدافند هوایی اسرائیل
🔴
شورای عالی امنیت ملی یونان اعلام کرد آماده تصویب این قرارداد برای ایجاد شبکه پدافند چندلایه «سپر آشیل» است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136742" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136741">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d166f5f8b9.mp4?token=c4TNv01rKfR6qslnZJieqYmyKEXMesA83O4UPGlDER21r8JpQazWSNWfSaeGo2749Z2mAfwZXa_Y7lH7i0ckK3ghCC29L1KJZ_XLYCLtd_q8QltCJhw-NjHs1rndtbvwd7no8_SwUtQ6blK8K14xl-Lz09FotNLvFJSry47sG4V5kValdJh50lYZPi3eIMU7h6UWha3GW6zagBfRg9ljFQcOKSi9bQfDfiW_tYEWjBx9BXAe8vr2vpoi3izrDUQHayz3knjd45tPNY9Eo8JaTsCMZ1J9QgPAPyy9v2bz63zjmmJr3L6oxHCqsYaCbhNjnJeEzDDmp4LZY0Xddyl46w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d166f5f8b9.mp4?token=c4TNv01rKfR6qslnZJieqYmyKEXMesA83O4UPGlDER21r8JpQazWSNWfSaeGo2749Z2mAfwZXa_Y7lH7i0ckK3ghCC29L1KJZ_XLYCLtd_q8QltCJhw-NjHs1rndtbvwd7no8_SwUtQ6blK8K14xl-Lz09FotNLvFJSry47sG4V5kValdJh50lYZPi3eIMU7h6UWha3GW6zagBfRg9ljFQcOKSi9bQfDfiW_tYEWjBx9BXAe8vr2vpoi3izrDUQHayz3knjd45tPNY9Eo8JaTsCMZ1J9QgPAPyy9v2bz63zjmmJr3L6oxHCqsYaCbhNjnJeEzDDmp4LZY0Xddyl46w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عصبانیت شدید نماینده کنگره از مایک والتز به خاطر اطلاعات ناقص او درباره جنگ ایران
🔴
لیو، نماینده کنگره: تو حتی نمی‌دانی چند سرباز آمریکایی در این جنگ ایران زخمی شده‌اند! شرم بر تو! تو سفیر آمریکا هستی و حتی نمی‌دانی چند سرباز آمریکایی زخمی شده‌اند! تو باید خجالت بکشی! تو باید استعفا بدی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136741" target="_blank">📅 19:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136740">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رسانه فایننشال‌تایمز مدعی شده است که خیریه گیتس علی‌رغم هشدارهای کارکنان این بنیاد، بیش از سه سال به تلاش خود برای همکاری با اپستین با هدف جمع‌آوری کمک‌های مالی برای حوزه سلامت جهانی ادامه داده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/136740" target="_blank">📅 19:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136739">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650663bf5e.mp4?token=svgmpdK6WFPVB1ny3nYOHLNN6iyqPssuK5QAcf-bSqQqqMfA44pNDuWk7oUqBL57wQPDPwU1x6-Osf5C4g6xHFYTaBEt0RSuL-9-apbFXvV8_ti8IL5-Lw4dZgAZqWAsJo6QJ2cnZog9Ud0rePfTNHuFT0IL-resmUWQvqZ7_D8J-EcCKzzYsW0-QAE3TvZJawdQYchFYcc4GFv8zjMYOwIm0eAJ1nPN1s4xDCB7vNatm20fZxxZmG6GBvCdCkEnMLeoVEUebtKooDKN623f0r_3-XQZC2_jjJNSTZLx-gXEvsdsCTKK2F5Wp4GJ2LM8f69wKkbYX7ZQWyRzo9NZVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650663bf5e.mp4?token=svgmpdK6WFPVB1ny3nYOHLNN6iyqPssuK5QAcf-bSqQqqMfA44pNDuWk7oUqBL57wQPDPwU1x6-Osf5C4g6xHFYTaBEt0RSuL-9-apbFXvV8_ti8IL5-Lw4dZgAZqWAsJo6QJ2cnZog9Ud0rePfTNHuFT0IL-resmUWQvqZ7_D8J-EcCKzzYsW0-QAE3TvZJawdQYchFYcc4GFv8zjMYOwIm0eAJ1nPN1s4xDCB7vNatm20fZxxZmG6GBvCdCkEnMLeoVEUebtKooDKN623f0r_3-XQZC2_jjJNSTZLx-gXEvsdsCTKK2F5Wp4GJ2LM8f69wKkbYX7ZQWyRzo9NZVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک افسر پلیس هندی در جریان حمله به یک ایستگاه پلیس در منطقه کشمیر تحت کنترل هند، کشته شد.
🔴
هیچ گروهی مسئولیت این حمله را بر عهده نگرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136739" target="_blank">📅 19:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136738">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/136738" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136737">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
پهپادهای اوکراینی در تاریخ‌های 21 و 22 جولای، 13 نقطه از زیرساخت‌های انرژی را در کریمه و سایر مناطق تحت کنترل روسیه مورد حمله قرار دادند.
🔴
این اهداف شامل چندین ایستگاه برق 110 کیلوولت در شهرهای آلوشتا، یالتا، آلوپکا، لوچیسته، پونیزیوکا، زیمینه و گاسپرا، و همچنین ایستگاه‌های برق در بردیانسک و بیلماک در منطقه زاپوریژیا و اولگینه در منطقه خرسون بودند.
🔴
نیروهای سامانه‌های بدون سرنشین اوکراین اعلام کردند که از تاریخ 1 تا 22 جولای، در مجموع 117 هدف مرتبط با انرژی در مناطق تحت کنترل روسیه مورد حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136737" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136736">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
روزنامه عبری زبان «یدیعوت آحارانوت» به نقل از منابعی گزارش داد دور بعدی مذاکرات بین لبنان و اسراییل طی ماه میلادی آینده و در سطح سفرای دو طرف برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136736" target="_blank">📅 19:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136735">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
لحظاتی پیش سفارت آمریکا در اسرائیل یک هشدار امنیتی برای شهروندان آمریکایی در اسرائیل به دلیل تنش قریب الوقوع در منطقه صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136735" target="_blank">📅 19:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136734">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رویترز: چهار نفتکش روز چهارشنبه پس از تهدیدات انصارلله یمن مسیر خود را در دریای سرخ تغییر دادند
🔴
کشتی‌های مرتبط با اسرائیل، ایالات متحده و عربستان در معرض ریسک بالاتری برای حمله هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136734" target="_blank">📅 19:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136733">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35436f215c.mp4?token=dka8ocur8suCL53mnWF8daUuMitiYS61lxGj87rRJtWiSqHuI-HJyz-aSChQ1qX5I5oMpVw3j4ol3ACGgqipKku8rLRBekynWGotDDq68FUHI3VxKvGmF9MWjZBJorxMQKxhQnXXc46LytASPHrukaIF4FtB2uZt25wAL9TW6TVa-S-eyEIcJSyZTr_jpxgMkCUTaQ0EhU5JjTiZpAGPTSVmSj8FkgTh4o683PfvaRG1-k3NGk98VaiChrzl6ngiZ_sb-dxo5a3z3Cllhw_TR329mZpsmjNYVRoeMvy1MQQcAhNVACOmEScia0siAE8CvoupYlPHPrKHQ6jqY_ZtVDNucaoK5749RlxWci-HTWHRb37RCsETg9reTqWBwu3WhHPCkOFJjYUcdHyuS80hdHIZnWcSZYfioCdLQ--Gb0doWTpgzq8QTlpfpLOeHKyJ9CJOKs5HfWPPN-tAAfzL332N3VXRijUUB7csq7zvc5ZbEiuX8JyyvD-46EVlrLSYqyOnkB1xIMSWTfZpB_6l6G7jH7FTNDbU6B3sGGzQxEAlabyA5KlxsYbVRBLAvVb_0A_BxBmfdINuErBDVjhievFzSsNneDqqqjJrLriXxe-Pmoion-AmjSjrr2fGmKm9XxlE7HA2-FQR26DscEENxrGInw3_l5hST_MfIaEIQHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35436f215c.mp4?token=dka8ocur8suCL53mnWF8daUuMitiYS61lxGj87rRJtWiSqHuI-HJyz-aSChQ1qX5I5oMpVw3j4ol3ACGgqipKku8rLRBekynWGotDDq68FUHI3VxKvGmF9MWjZBJorxMQKxhQnXXc46LytASPHrukaIF4FtB2uZt25wAL9TW6TVa-S-eyEIcJSyZTr_jpxgMkCUTaQ0EhU5JjTiZpAGPTSVmSj8FkgTh4o683PfvaRG1-k3NGk98VaiChrzl6ngiZ_sb-dxo5a3z3Cllhw_TR329mZpsmjNYVRoeMvy1MQQcAhNVACOmEScia0siAE8CvoupYlPHPrKHQ6jqY_ZtVDNucaoK5749RlxWci-HTWHRb37RCsETg9reTqWBwu3WhHPCkOFJjYUcdHyuS80hdHIZnWcSZYfioCdLQ--Gb0doWTpgzq8QTlpfpLOeHKyJ9CJOKs5HfWPPN-tAAfzL332N3VXRijUUB7csq7zvc5ZbEiuX8JyyvD-46EVlrLSYqyOnkB1xIMSWTfZpB_6l6G7jH7FTNDbU6B3sGGzQxEAlabyA5KlxsYbVRBLAvVb_0A_BxBmfdINuErBDVjhievFzSsNneDqqqjJrLriXxe-Pmoion-AmjSjrr2fGmKm9XxlE7HA2-FQR26DscEENxrGInw3_l5hST_MfIaEIQHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: تهدید نابودی را عقب راندیم و به دستاوردهای عظیمی رسیدیم.
🔴
به یاری خدا، جاودانگی اسرائیل را تضمین خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136733" target="_blank">📅 19:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136732">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
اسرائیل هیوم به نقل از رسانه‌های آمریکایی مدعی شد احتمالا «بنیامین نتانیاهو» در هفته آتی با سفر به آمریکا با دونالد ترامپ دیدار خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136732" target="_blank">📅 19:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136731">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
منابع خبری از تداوم نقض آتش بس از سوی اسرائیل و حملات توپخانه ای و هوایی به جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/136731" target="_blank">📅 19:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136730">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر خارجه عربستان: ثبات پایدار از طریق قدرت نظامی قابل‌ دستیابی نیست. ثبات از طریق راه‌حل‌های دیپلماتیک پایدار که به ریشه‌های بحران‌ها می‌پردازه، حاصل میشه. به‌جای تن دادن به تنش‌زدایی موقت، باید راه‌حل‌های سیاسی دائمی یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136730" target="_blank">📅 19:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136729">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
استدلال این هم وطن کاملا درسته که میگه سرباز آمریکایی سگش شرف دارد به کل جمهوری اسلامی و طرفداراش
🤔
هرچی از حرام زاده بودن طرفدارهای جمهوری اسلامی بگیم کم گفتیم.</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/136729" target="_blank">📅 19:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136728">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نخست‌وزیر عراق علی الزیدی:
ما اجازه نمی‌دهیم عراق به یک دولت شکست‌خورده تبدیل شود و دولت ما متعهد به مبارزه با فساد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/136728" target="_blank">📅 19:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136727">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزیر خارجه روسیه : ارسال سلاح به ایران را رد میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136727" target="_blank">📅 19:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136726">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ca8e4ec9c.mp4?token=E-X7Xwk75H6_L2lDCYIcT2PYRjwxpO8kbNsigfeLs5AdKPrkDuFnHABBKCE8GbnKRmOaIjqPxF0a9T3t6BkE0ivD9q50ZrP-Xml7t5yvmLY4npDhUovXiBysKBhw51AC4aj0DZbsgw8jFNcS0VhxvAif20eI2-ownJRGWYUCDEYCc9rMCDVLyrMLoTwqibYFw7pnxZpUxrS5PkCZA0b4KqN05SzZYvoq7JpTEgQN1EqX64C4s77T41sOzFi0smH1EqJKpZpqO9vT8SA5XgaJyl6ASPLOBkMGzCfoUmn1ly9DNbKe88OEAh2KIhKUuyC-6G0VXgozJaS8ogHGQdnbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ca8e4ec9c.mp4?token=E-X7Xwk75H6_L2lDCYIcT2PYRjwxpO8kbNsigfeLs5AdKPrkDuFnHABBKCE8GbnKRmOaIjqPxF0a9T3t6BkE0ivD9q50ZrP-Xml7t5yvmLY4npDhUovXiBysKBhw51AC4aj0DZbsgw8jFNcS0VhxvAif20eI2-ownJRGWYUCDEYCc9rMCDVLyrMLoTwqibYFw7pnxZpUxrS5PkCZA0b4KqN05SzZYvoq7JpTEgQN1EqX64C4s77T41sOzFi0smH1EqJKpZpqO9vT8SA5XgaJyl6ASPLOBkMGzCfoUmn1ly9DNbKe88OEAh2KIhKUuyC-6G0VXgozJaS8ogHGQdnbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت خطاب به کارگر لنج:
من به دستور رئیس‌جمهور به جنوب کشور سفر کردم و اومدم به همه کسایی که دارن تلاش میکنند خدا قوت بگم و ارادتمندم.
🔴
کارگر لنج: باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/136726" target="_blank">📅 19:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136725">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lObhwrrvR9ypxmMIZdi6mAvgpWtzr58lmveYtQRr95-Yv6W86ctY97Yq0IpdQahs1R44BRFPSaZwPPZzIb4iLrSFZ_l9UdeS45cNnYFMp7iQ31_piY723V6FN1lEV4GoWtiInEKRhzfZPo0NNtIo1rJzY7diqW3oYYTGAjFZ08h7edjPCexRKe_bz1iu3_2SCwTKBW9fjvIMAWBbQOYjrEGod0tx_djLHx9tWQmG9h0r35Be054jb52Z6MnayMJZ0DoLd3vveZlPk8FoFxthxnyWwAm5-kqQXqOtz_8JsYd62T_WuzQ96ZLg4qo_ZMjxbYMLeZgGkxz0xHJ1iKEGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت گاز طبیعی اروپا همچنان در حال افزایش است و به بالاترین سطح خود از آغاز جنگ رسیده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136725" target="_blank">📅 19:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136724">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ در واکنش به حرفای ممدانی درباره بازداشت نتانیاهو : آمریکا به هیچ عنوان و به هیچ صورت ممکن نتانیاهو را بازداشت نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/136724" target="_blank">📅 19:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136723">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
منوچهر متکی، نماینده تهران:
قرار بود قطر ۱۲ میلیارد دلار از ۲۴ میلیارد دلار منابع ایران را آزاد کند و حتی اعلام کرد ۶ میلیارد دلار خود را بعداً پس می‌گیرد، اما آمریکا وارد شد و گفت یک سنت هم نباید پرداخت شود؛ تا امروز هم این پول پرداخت نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136723" target="_blank">📅 19:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136722">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز: شرکت هواپیمایی کی‌ال‌ام هلند اعلام کرد تعلیق پروازهای به دبی در امارات و ریاض و دمام در عربستان را تا ۶ سپتامبر تمدید خواهد کرد.
🔴
این اقدام به دلیل وضعیت بحرانی در غرب آسیا اتخاذ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/136722" target="_blank">📅 19:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136721">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
اختلال در متا (اینستاگرام، فیس‌بوک، واتس‌اپ)
🔴
درحال حاضر اختلالی از سمت شبکه‌های اجتماعی اینستاگرام، فیس‌بوک و واتس‌اپ وجود دارد.
🔴
این مشکل به صورت سراسری است و کاربران ایرانی هم شامل این اختلال هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/136721" target="_blank">📅 19:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پوتین: می‌خواهم بار دیگر تأکید کنم. مشکلاتی که در بازار سوخت ایجاد می‌شود، بدون تردید موقتی است و بر پویایی عمومی اقتصاد روسیه تأثیر نخواهد گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136720" target="_blank">📅 19:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سی‌جی‌تی‌ان: تصاویر ماهواره‌ای نشان می‌دهند که هیچ هواپیمای آمریکایی در پایگاه هوایی العدید در قطر حضور ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136719" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBt77Y9a79N9f-fioVwERLm-CwnqAWMHCu6aAaVuDVWst6NGA40O64MtJbmT3m75E88Vv_gmpHB1t9IkhO97NTJT761ZoBMLnzDItB_oaImDBtFxKvIBfxyYcd0NYrxzlU26mjb9Dg6RNRBJiTLjeuko20Tu5ZDABzrhfTrqujZ3BT65gTi6gTDiLYvHxJ7jEyGaj-TjTfbSw2OhmEg-bbcaRREzpWdX02gJT6Hok7jgB3D-s_sAEItvbmqrQI_EWbjS59O0I4s45t2WlxCTXdf0K2rAqnSEsh_d44KaccdERzjDgGDNsRBPN1yrghuBJ7Lc4QAUTAP_oUz28PSuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دستور پزشکیان برای رسیدگی به موضوع فیلتر شدن سایت عادل فردوسی پور
🔴
در جلسه امروز هیئت دولت، وزیر ارتباطات و فناوری اطلاعات گزارشی از حادثه اخیر مربوط به دو سایت «عادل فردوسی‌پور» و اقدامات انجام‌شده ارائه کرد و چندصدایی در حوزه فضای مجازی را همچنان از مشکلات اساسی کشور برشمرد. پزشکیان رئیس‌جمهور در این خصوص دستور پیگیری جدی موضوع و جلوگیری از بروز مسایل بدون هماهنگی را صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136718" target="_blank">📅 18:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2801c386a4.mp4?token=D53BC1AyEsEktOyDT9jGRS1M_fUbCNHXTLaF56rUO9otcLEsnhN1uVaCZci3-j1nHWhW_cVSAd2JQAON9dNTkLVPp1SvU5oM6Va1oZ_XwFoih9SOX9xQZqUrhEz8P4dr1HFgAgg8639JRQyxAz1U4gtJb1jgTfr--otF65kKM0oFNcfVnapukPwC9y5lHhR3sRcVIrW1ZctaT-NktvH3z4e5oMh01TVr0hXprC-viMFaL1_WnHqyZSId6cqoQ0WG9Zx_fyN-LafyB8J7dWXiHhZ65_HubIEj4qZv9K1zSLp8HvUtXipDQOsFwhJnywu6rQIveFkAVS-Ti7bAOmzMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2801c386a4.mp4?token=D53BC1AyEsEktOyDT9jGRS1M_fUbCNHXTLaF56rUO9otcLEsnhN1uVaCZci3-j1nHWhW_cVSAd2JQAON9dNTkLVPp1SvU5oM6Va1oZ_XwFoih9SOX9xQZqUrhEz8P4dr1HFgAgg8639JRQyxAz1U4gtJb1jgTfr--otF65kKM0oFNcfVnapukPwC9y5lHhR3sRcVIrW1ZctaT-NktvH3z4e5oMh01TVr0hXprC-viMFaL1_WnHqyZSId6cqoQ0WG9Zx_fyN-LafyB8J7dWXiHhZ65_HubIEj4qZv9K1zSLp8HvUtXipDQOsFwhJnywu6rQIveFkAVS-Ti7bAOmzMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین: بخش‌های کلیدی اقتصاد روسیه علیرغم تلاش‌های خارجی برای بی‌ثبات کردن وضعیت در بخش انرژی و سایر حوزه‌ها، باثبات است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/136717" target="_blank">📅 18:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
اکسیوس: شرط اصلی ترامپ برای برقراری آتش‌بس این است که ایران حملات علیه کشتی‌ها را متوقف کند و تنگه هرمز را دوباره برای کشتیرانی باز کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136716" target="_blank">📅 18:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2371f68421.mp4?token=mvzj26OqhNxdOQRgcYAdNZK_8BOoTiD7abeusSACRGCUAZfcKcrJ-Tz95zOU9qxx9a-146R5T8H2_ptuowKPZ0moxKH5Mq23JmlqIOFv1QYEm2qSDoAkvUysCMTz3TBzebGV9ucG8FamguS0GBbC2yeCfGd_cs5b-dp3O-gjySxoYdYtjTqxxN65WjJkc4eVxWcUq5-EAhd__WsXkneDNswEJAwQU6SOiyfRPPsH4UMw_YPyV2BD8d4QYsiRo5_hnPMozu2_i_1HQGgR0jWeypZNR-9A8gsoVGJjA7BF5weGOLd19LisxszMH8Cg_MmNGGSZ8w5njZvaNmHKQJFtkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2371f68421.mp4?token=mvzj26OqhNxdOQRgcYAdNZK_8BOoTiD7abeusSACRGCUAZfcKcrJ-Tz95zOU9qxx9a-146R5T8H2_ptuowKPZ0moxKH5Mq23JmlqIOFv1QYEm2qSDoAkvUysCMTz3TBzebGV9ucG8FamguS0GBbC2yeCfGd_cs5b-dp3O-gjySxoYdYtjTqxxN65WjJkc4eVxWcUq5-EAhd__WsXkneDNswEJAwQU6SOiyfRPPsH4UMw_YPyV2BD8d4QYsiRo5_hnPMozu2_i_1HQGgR0jWeypZNR-9A8gsoVGJjA7BF5weGOLd19LisxszMH8Cg_MmNGGSZ8w5njZvaNmHKQJFtkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی که نشان می‌دهد بعد از شلیک موشک از ایران، سربازان آمریکایی پنج دقیقه وقت دارند در محفظه های که برای آنها طراحی شده است پناه بگیرند، این محفظه های به دور از هم طراحی شده تا تعداد تلفات به حداقل برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/136715" target="_blank">📅 18:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
هشدار سفارت آمریکا در اردن؛ بیرون از خانه ناامن است
🔴
شهروندان آمریکا باید دستورالعمل‌ها از جمله آژیرها و دیگر هشدارها را دنبال کنند.
🔴
آن‌ها باید به وبگاه‌های مرکز ملی امنیت و مدیریت بحران برای راهنمایی‌های ایمنی عمومی، از جمله توضیحات آژیرهای اضطراری در اردن مراجعه کنند.
🔴
از شرکت در تجمعات بزرگ اجتناب ورزند. از تمام مناطقی که پلیس در آن‌ها حضوردارد، دوری کنند.رسانه‌های محلی را دنبال کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136714" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / آکسیوس: ترامپ در آستانه اتخاذ تصمیمی سرنوشت‌ساز قرار گرفته: پذیرش آتش‌بس جدید با ایران یا آغاز یک عملیات نظامی گسترده و مشترک با اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/136713" target="_blank">📅 18:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136712">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شرکت اسلان ترکیه قرارداد جدیدی با وزارت دفاع بوسنی و هرزگوین برای تأمین سامانه‌های ضدپهپاد امضا کرد.
🔴
این سفر همچنین شامل دیدارهایی با مقامات ارشد دولتی برای بررسی گسترش همکاری‌های صنعتی و دفاعی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/136712" target="_blank">📅 18:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136710">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44376769e1.mp4?token=pkCC4fcWaPo2q7lb55UavUmfX95Qq5xHeVOUSWDu4laEE7HTUNky1s7KtXKF2H9pQBEopI6YS_pG8VfsUcqgLd67Ma2tNLXfw26YEOSDg0P7W6xKRalRwUo7p_SXuxEuPQPY7qoAmulbz3OVuzC7QiFcpAHZFDCzjIBkMGIJAJUrkVfjNLpJNwVoFRTnGip1YMsX3RsOs1dHOiMp_U4HzzxaqISFQEVP0iVsmMWZw-rfekheZUt2WubWq2JD8ZvkOK3BvPxPuiBRjtgIw7rjb2GW_b4PQqwJrLaBUmSz5Dj2igTpYTKm8VdW3Y8p9FExJtWca1ntFbcqQVFBKBQOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44376769e1.mp4?token=pkCC4fcWaPo2q7lb55UavUmfX95Qq5xHeVOUSWDu4laEE7HTUNky1s7KtXKF2H9pQBEopI6YS_pG8VfsUcqgLd67Ma2tNLXfw26YEOSDg0P7W6xKRalRwUo7p_SXuxEuPQPY7qoAmulbz3OVuzC7QiFcpAHZFDCzjIBkMGIJAJUrkVfjNLpJNwVoFRTnGip1YMsX3RsOs1dHOiMp_U4HzzxaqISFQEVP0iVsmMWZw-rfekheZUt2WubWq2JD8ZvkOK3BvPxPuiBRjtgIw7rjb2GW_b4PQqwJrLaBUmSz5Dj2igTpYTKm8VdW3Y8p9FExJtWca1ntFbcqQVFBKBQOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که هواپیماهای نظامی آمریکایی در حال ترک پایگاه هوایی فیصل در اردن هستند. این اتفاق پس از حمله امروز ایران رخ داد که در آن حداقل یک انبار هواپیما آسیب دید.
🔴
چندین فروند هواپیمای ترابری C-130، به همراه چندین جنگنده و هلیکوپتر، دیگر در این پایگاه حضور ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136710" target="_blank">📅 18:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136709">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9eYpkgfA6Ypl4rrjwwwG158st-OBR9orcU0B0S9p1sFKJ3uWwj9habP8LbHDEP53d7YuS-GH_gHG2cWhZOjNED0kURb0vadnN7ZuU7TqN63iYizQlUFFeXeXONMp_ToY5CnJ3Nzl-_MbaePQsAcA8UOPhPw6Ozi-vCdoPFf0NfRZh8uB8TagAij_7Y-NLZuVkY3x2_A5Bghc27SYVNprqZ48zFgYeFlxJD5MtECHkdhpgFJheg4oXsnzYTsoziLGzUL8X8HRCQKSqt851brrV5GcBU7XOd7Iyg1ox7-d1I_cf9hhOAvpIMysAGZSDDsPQ9k2L4q0L1caI6NqNc2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای MV-۲۲B Osprey متعلق به نیروی دریایی آمریکا در فرودگاه مسا در ایالت آریزونا دچار آتش سوزی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/136709" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136708">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
خبرنگار: آیا ایالات متحده تلاش می‌کند تا سوریه را به درگیری با حزب‌الله بکشاند؟
🔴
روبیو: ما به سوریه توصیه کرده‌ایم که بر چالش‌های داخلی خود تمرکز کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/136708" target="_blank">📅 18:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136707">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نیویورک‌تایمز: اگر انصارالله یمن از تردد کشتی‌های عربستانی از طریق دریای سرخ جلوگیری کند، حدود ۴ درصد از عرضه نفت جهان از بازار حذف می‌شود
🔴
خط لوله سومد در مصر و کانال سوئز نیز به عنوان مسیرهای جایگزین، محدودیت‌های قابل توجهی دارند؛ زیرا نفتکش‌های بسیار بزرگ قادر به عبور از کانال سوئز نیستند، ظرفیت سومد کافی نیست و در صورت استفاده از مسیر مدیترانه، زمان رسیدن محموله‌ها حدود چهار هفته افزایش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136707" target="_blank">📅 18:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136706">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApLLLgwyGqH7QgKHufuDyY3jPh5WAl5oALaMvMJldLOdHoTSpchMrTswUuACsdrwNXC_oXfXkqDLG6kK5WHyxb5-NAv5eyMPbVGCxRY2LqfxzKsL80oQxOcW41uH3n4FSguqNytBxBrOoQet33ZkAeS9OZYldkIjj3OEF-t7DNGb8AvgsCSdLW0jIWewpblm6Fdx9p0Czyl8wWui2uzcbivxmwirPlAj-G80Vt1ZRrg7Z0f9z26ZxnA4oB1cUM4ZS-4A8AShpKV9WxlFmbQSVnK_-qSsYJ_jAsXslIRAvC3idk3jXpkLOuHmgcgIHS5BMxiaBcWgKnT9YFWNTg3KTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمیخای چیکلی، وزیر امور مهاجران اسرائیل: ما باید برای جنگ با ترکیه آماده شویم.
🔴
احتمال تماس مستقیم با ارتش ترکیه در دریا وجود دارد. این یک سناریوی غیرممکن نیست؛ این اتفاق می‌تواند فردا صبح به وقوع بپیوندد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136706" target="_blank">📅 18:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136705">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81cf502373.mp4?token=I8mSpddhLqz8q-tZAsyZA3wZgA0iBb03oLfPn9uHhXs2NFkOGD4Kx0_5aOGZq7t7kxbSWWTbS7bA838kXxr0UVjjSIzWtnr92D-gaZh3cUY6noYeEWIb6LuNSp7Jix02EPNlpqvM_KbTZa9aXtV05VWhs8UkWUJu7kdwycH2F3X6MN-GoTO6IKG8cvnGtVpdzxX66MYVBpZKVq912IGayKTZ1ee4tVjstqVGlxN0zYUCKY_XQB0CB3Ph2hThqbTI0c7wCEw3N9mxmPJErV106WJzOTKPR5KB4A4DsLjc6s5dKxP23q5fN_l97P6Bugws-5PVxTq-1BEqnRL5nzuORQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81cf502373.mp4?token=I8mSpddhLqz8q-tZAsyZA3wZgA0iBb03oLfPn9uHhXs2NFkOGD4Kx0_5aOGZq7t7kxbSWWTbS7bA838kXxr0UVjjSIzWtnr92D-gaZh3cUY6noYeEWIb6LuNSp7Jix02EPNlpqvM_KbTZa9aXtV05VWhs8UkWUJu7kdwycH2F3X6MN-GoTO6IKG8cvnGtVpdzxX66MYVBpZKVq912IGayKTZ1ee4tVjstqVGlxN0zYUCKY_XQB0CB3Ph2hThqbTI0c7wCEw3N9mxmPJErV106WJzOTKPR5KB4A4DsLjc6s5dKxP23q5fN_l97P6Bugws-5PVxTq-1BEqnRL5nzuORQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: چین با اقدامات ایران در تنگه‌ها موافق نیست
🔴
مارکو روبیو درباره ایران گفت: «فکر می‌کنم چینی‌ها ــ و البته بهتر است خودشان در این‌باره اظهار نظر کنند ــ طرفدار اقداماتی که ایران در تنگه‌ها در پیش گرفته، نیستند.»
او افزود: «چین به‌صورت علنی اعلام کرده که با دریافت عوارض یا هرگونه محدودیت بر آزادی کشتیرانی در تنگه‌ها مخالف است.»
روبیو در پایان ابراز امیدواری کرد که پکن همچنان بر همین موضع باقی بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136705" target="_blank">📅 18:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136704">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4239c52d4.mp4?token=tyscZWZ1hj5zHITVrEU3Omo15fk6_EOigO8lNuKr4bgDu9R8MK_m11SdV2cQTdha53SHpAKKOGtuvfmvaZl2dUJdT_p6p1XLGj7ZVOH2JHHiwEfcz51t3HOZmqRb9fPIO-dHox-k4doH8o9SlQNTPbl2k8NHs-C2wlgJCMz7CwwXa7MNEYovLr1JmjuUDzzEmgBb7IllwYW-ZGERjl-UI1dUpGVY5vgH_OH-ANLQlCYh7-QBuWnkwpQOpo5XV4ZemTsotQSf_vH_DtX1_Q4adxdaAg57ucWwM051F6Cg5KBHlMlgQKrKiOqUawfEKIHRVbeMD6p7lfTHI6vdNhx7ymJOUXQv1CqpI2RKTCeJN_W3EP4zJJhMxi5srlW_VEf3QPyhqLmER9aWvO0OGJqBc1uvy2Vqxx7R9nED_4zokAh1euCf_mS2O0-_UYYM4TOHd4WPJtxVWWUFolUzTzjzWzML-vhSQaeCK6vO2rhiBOw1q-y5P4hsBrkBmT1yTlOwIKytt9Wfj1QFeAFXpkXtJndcz2On3vKSFJIo0pu1GUh9QdjrLpJBG-Y8RVWrRzLErgAuUDWQQIo6heAkkkJAe7Pa4u7ulcQT8nMddwxmrWsnB-BobQ7bxwq9L-FNXaPhZZpwBHqRWzkYmYPGIdNdk3gaUO7KCatATlLX8qZozVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4239c52d4.mp4?token=tyscZWZ1hj5zHITVrEU3Omo15fk6_EOigO8lNuKr4bgDu9R8MK_m11SdV2cQTdha53SHpAKKOGtuvfmvaZl2dUJdT_p6p1XLGj7ZVOH2JHHiwEfcz51t3HOZmqRb9fPIO-dHox-k4doH8o9SlQNTPbl2k8NHs-C2wlgJCMz7CwwXa7MNEYovLr1JmjuUDzzEmgBb7IllwYW-ZGERjl-UI1dUpGVY5vgH_OH-ANLQlCYh7-QBuWnkwpQOpo5XV4ZemTsotQSf_vH_DtX1_Q4adxdaAg57ucWwM051F6Cg5KBHlMlgQKrKiOqUawfEKIHRVbeMD6p7lfTHI6vdNhx7ymJOUXQv1CqpI2RKTCeJN_W3EP4zJJhMxi5srlW_VEf3QPyhqLmER9aWvO0OGJqBc1uvy2Vqxx7R9nED_4zokAh1euCf_mS2O0-_UYYM4TOHd4WPJtxVWWUFolUzTzjzWzML-vhSQaeCK6vO2rhiBOw1q-y5P4hsBrkBmT1yTlOwIKytt9Wfj1QFeAFXpkXtJndcz2On3vKSFJIo0pu1GUh9QdjrLpJBG-Y8RVWrRzLErgAuUDWQQIo6heAkkkJAe7Pa4u7ulcQT8nMddwxmrWsnB-BobQ7bxwq9L-FNXaPhZZpwBHqRWzkYmYPGIdNdk3gaUO7KCatATlLX8qZozVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: اقدامات چین مسیر درگیری آمریکا با ایران را تغییر نداده است
🔴
در پاسخ به پرسش خبرنگاری درباره احتمال ارائه اطلاعات هدف‌گیری از سوی چین و روسیه به ایران و تلفات سنگین نیروهای آمریکایی در حملات اخیر، مارکو روبیو گفت حضور در هر منطقه جنگی با خطرات اجتناب‌ناپذیری همراه است.
🔴
او افزود: «این حملات در واقع نشان می‌دهد ایران طی ۲۰ سال گذشته منابع مالی خود را در چه حوزه‌ای سرمایه‌گذاری کرده است.»
روبیو همچنین تأکید کرد: «هیچ‌یک از اقدامات چین، مسیر تحولاتی را که در درگیری‌های آمریکا با ایران شاهد هستیم، تغییر نداده است.»
🔴
وی ادامه داد که چین در برخی موارد حتی همکاری‌هایی نیز داشته و از انجام اقداماتی که امکان انجام آن‌ها را داشته، خودداری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/136704" target="_blank">📅 17:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136703">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
قیمت نفت برای اولین بار در شش هفته گذشته از مرز ۹۵ دلار به ازای هر بشکه عبور کرد، زیرا افزایش تنش‌ها در خاورمیانه نگرانی‌ها را در مورد احتمال اختلال در عرضه جهانی نفت خام افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136703" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136702">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
یک منبع نظامی به تسنیم: هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136702" target="_blank">📅 17:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136701">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3168e57cc1.mp4?token=c83CbN5Viq3j9vVMfJ0r14ufvkfCY6IZueEobwmYCQiH8dNv1Ju7IunukUo93ZrbZL8SBbCyz2tkwOHi66uZvHKrawZpld23lsKxjn522hFbC2Ti47qOIOe75KoqSznsvpOam1DqwAigqpKue6xzLq-9aDnreVbPKJ6rS5pbHXY2C0MJutHLUf_YPfx3wYE2_XHiieACJl4rGXgqcrYxjWNX2VZCAQsQIPh7qjL4ES9PMm2byXTO1A0brLY12S9d2TtOB2WwgxSS9g23LjumJCkwXfE_VpyleY7RagNDvM-4UyGw3r1RKcgS4HFCa0KzaBrEuxlZPj2qpCSNEnx9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3168e57cc1.mp4?token=c83CbN5Viq3j9vVMfJ0r14ufvkfCY6IZueEobwmYCQiH8dNv1Ju7IunukUo93ZrbZL8SBbCyz2tkwOHi66uZvHKrawZpld23lsKxjn522hFbC2Ti47qOIOe75KoqSznsvpOam1DqwAigqpKue6xzLq-9aDnreVbPKJ6rS5pbHXY2C0MJutHLUf_YPfx3wYE2_XHiieACJl4rGXgqcrYxjWNX2VZCAQsQIPh7qjL4ES9PMm2byXTO1A0brLY12S9d2TtOB2WwgxSS9g23LjumJCkwXfE_VpyleY7RagNDvM-4UyGw3r1RKcgS4HFCa0KzaBrEuxlZPj2qpCSNEnx9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: امروز به خانواده‌های آسیب‌دیده چه خواهید گفت؟
🔴
ترامپ: فقط این را می‌گویم: «ما شما را دوست داریم؛ ما فرزند شما را دوست داریم.» تنها کاری که می‌توانید انجام دهید این است که تمام وجودتان را در این پیام قرار دهید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136701" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136700">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / بلغارستان بااستقرارسوخت‌رسان‌های آمریکا در خاکش موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/136700" target="_blank">📅 17:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136696">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9eeec050.mp4?token=ryCFV-Fjki4-66o80mWiLaeZfF0JoiecqWFLLCfu7IRJG2F4dS89kR1SilxYDPFvBsYwh866FARlMf_lralL-PdIdIcxo315bluVq5BfrdTcZ-w0kzjKk3GhCxdXJUDDiGYVKB984vLZWITuCp9fXf7Ues4oEHgiungHuLx30_xfeijRIyK92CKsMLrBvNdg7i4F9aa7ycV7kB0pscMaRImR_iz2kMTqeJDqtXuQYIFtVahtMOvZh0vEcm9jd9GRyzhWd6BGXjXmri23iheHMWLeobtX9m-f6ds87rqz9T0dSybVxeNlybaqvVy6TOwDTeEZ9hKg0FQVsJaRlS8iig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9eeec050.mp4?token=ryCFV-Fjki4-66o80mWiLaeZfF0JoiecqWFLLCfu7IRJG2F4dS89kR1SilxYDPFvBsYwh866FARlMf_lralL-PdIdIcxo315bluVq5BfrdTcZ-w0kzjKk3GhCxdXJUDDiGYVKB984vLZWITuCp9fXf7Ues4oEHgiungHuLx30_xfeijRIyK92CKsMLrBvNdg7i4F9aa7ycV7kB0pscMaRImR_iz2kMTqeJDqtXuQYIFtVahtMOvZh0vEcm9jd9GRyzhWd6BGXjXmri23iheHMWLeobtX9m-f6ds87rqz9T0dSybVxeNlybaqvVy6TOwDTeEZ9hKg0FQVsJaRlS8iig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری بین گروه تروریستی JNIM و سازمان تروریستی IS-Sahel دیروز در منطقه گوسی، در شمال مالی، رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136696" target="_blank">📅 17:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136695">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec324d8d1.mp4?token=U6E2Ot0kDoQZ3qDgV16TNikZmATh_B_xdAlshwQEyZGHsSYA4I8OVw3Yl0o24cVTEAA2VwnFIBFu7PXHSSC9lNtXk2PC87YYPF_MhcT7_tcaumBPDZZWENPHTQnu0QzxsMnvyeQDtoO3jKDms8wWBm0PNgqZYey4uPdNlWquaPNuXSPOop23iJjvhyfgH2XEXmhhukOC-ZNhay0FcvKshVLaJGpztPpMOxazdwdOmoQw1zMErW6CeEaviik9k8wtUVt9liL2L_921EZQ-ib4APmW7PO1VFHIpCZ3c-A6lOIrOXbI4G8aASoz1Q4bElh8D7F1iY47RPxIuSt4RvxIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec324d8d1.mp4?token=U6E2Ot0kDoQZ3qDgV16TNikZmATh_B_xdAlshwQEyZGHsSYA4I8OVw3Yl0o24cVTEAA2VwnFIBFu7PXHSSC9lNtXk2PC87YYPF_MhcT7_tcaumBPDZZWENPHTQnu0QzxsMnvyeQDtoO3jKDms8wWBm0PNgqZYey4uPdNlWquaPNuXSPOop23iJjvhyfgH2XEXmhhukOC-ZNhay0FcvKshVLaJGpztPpMOxazdwdOmoQw1zMErW6CeEaviik9k8wtUVt9liL2L_921EZQ-ib4APmW7PO1VFHIpCZ3c-A6lOIrOXbI4G8aASoz1Q4bElh8D7F1iY47RPxIuSt4RvxIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: آمریکایی‌ها مخالف جنگ نیستند.
🔴
آمریکایی‌ها نمی‌خواهند قیمت بنزین بالا باشد، اما مخالف جنگ نیستند.
🔴
هیچ‌کس نمی‌خواهد ایران سلاح هسته‌ای داشته باشد.
🔴
آیا شما می‌خواهید ایران سلاح هسته‌ای داشته باشد؟ فکر می‌کنید این خوب است؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136695" target="_blank">📅 17:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136694">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=XDCaE97PkyF1l875s6H-0KyKC0_pOPi2RhCaBmLS9-GsXVtr5awbycLroU3JTCEEWRW2U8U191kJ3USyV3CzbGkiEI1VoZt3plto-R0Dah2uaY6aV_iMFcZbLAmCjez_QXO-HPPyFXZksK4MO0CENuAVMDzx7YY3BsVj4cT_ZCu1Hkt4pGzhU8ZUzrpQ7s_2WIs6FchDIA_eUgoBVo25wVghzOR6tROV8_BOdpS55FV-kQ_AA99PnzoeXeeEkEcEkfsONPtDA6XjCNbByVsCk2K8_nTE61K-T2rlaHXSKIti1Hky5wjmr64i_Fk8wcYE3jFyTw-QPN5nMx7EZ9aQGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=XDCaE97PkyF1l875s6H-0KyKC0_pOPi2RhCaBmLS9-GsXVtr5awbycLroU3JTCEEWRW2U8U191kJ3USyV3CzbGkiEI1VoZt3plto-R0Dah2uaY6aV_iMFcZbLAmCjez_QXO-HPPyFXZksK4MO0CENuAVMDzx7YY3BsVj4cT_ZCu1Hkt4pGzhU8ZUzrpQ7s_2WIs6FchDIA_eUgoBVo25wVghzOR6tROV8_BOdpS55FV-kQ_AA99PnzoeXeeEkEcEkfsONPtDA6XjCNbByVsCk2K8_nTE61K-T2rlaHXSKIti1Hky5wjmr64i_Fk8wcYE3jFyTw-QPN5nMx7EZ9aQGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها بهای سنگینی خواهند پرداخت. آنها در حال نابودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136694" target="_blank">📅 17:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136693">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb67cefff9.mp4?token=pB8mvJMP7VPVoytURA763xnznT51cYPcwHvmAivtVXx8aD97aO96TL1KBKTuIuaS9plU9lAMR1hz-uwhgEZ1TbSRJ-pXQlKy-g8C-eTXu0QOCx6e012NrtfUMADbzOZ4PzMIjwyivyFJvgyncY4uP6tiOMrmDFzEDIz-HgvfuMkz3QKth5cqL5xjBvnUQ8G3RxJhgrK1G58Xu5iC8O5bA5lSD-PSH_OwmGeG93Yx_88Up0Tsgm2oZEDNVaiTefnJh0vLvOZbz8la8vNpsLSJeW3rATt1KmtgP7ixcuSJ6EeFF2gznp0-woqJ8FB9crjNRKXXER-ah3MndTpqPdtr7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb67cefff9.mp4?token=pB8mvJMP7VPVoytURA763xnznT51cYPcwHvmAivtVXx8aD97aO96TL1KBKTuIuaS9plU9lAMR1hz-uwhgEZ1TbSRJ-pXQlKy-g8C-eTXu0QOCx6e012NrtfUMADbzOZ4PzMIjwyivyFJvgyncY4uP6tiOMrmDFzEDIz-HgvfuMkz3QKth5cqL5xjBvnUQ8G3RxJhgrK1G58Xu5iC8O5bA5lSD-PSH_OwmGeG93Yx_88Up0Tsgm2oZEDNVaiTefnJh0vLvOZbz8la8vNpsLSJeW3rATt1KmtgP7ixcuSJ6EeFF2gznp0-woqJ8FB9crjNRKXXER-ah3MndTpqPdtr7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره سربازان آمریکایی که در حمله موشکی اخیر ایران کشته شدند:
آنها واقعاً قهرمانان بزرگی هستند. همه آنها به صراحت گفتند: "ما نباید اجازه دهیم که ایران سلاح هسته‌ای داشته باشد." آنها به سلاح هسته‌ای دست نخواهند یافت.
🔴
ما به آنها ادای احترام خواهیم کرد. برای من، این یکی از سخت‌ترین کارهایی است که یک رئیس جمهور باید انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136693" target="_blank">📅 17:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136692">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-Az32lvruAOt6BlS7jzTsoF8pFFLaMnMLF6EOGVUgkOe1svhTB8dVzcPywCJvbVYeqjHyYDQcpKHMPW_6Sxbh6vOjUJlUcWFE1npTKRXrXVZYxF4V6IXxd6xMntPunH-cQTSac9QNOtMUhCAl7F57zxSQ2FkcmP8AN9aeOUo1CuEegILKgar-A6Hek9FJNMEoZoC_Th68RMU9a5WYUKCUtkOSa5dXCHVo4Gj7qyT8jtejJ3dyosorQS0WBjXFm2zFKtRu8cakREZiGGxmJhxc3VDYvTjuyL98R7rvAS1Ul4gkvnPOcbd0Khk8tYY_nydTRC7aImvg6tRZcKQX6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس: کاخ سفید و دفتر نخست‌وزیر اسرائیل، بنیامین نتانیاهو، در حال بررسی امکان برگزاری نشستی بین رئیس‌جمهور ترامپ و نتانیاهو در کاخ سفید در هفته آینده هستند، اما تا کنون هیچ جلسه‌ای برنامه‌ریزی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136692" target="_blank">📅 17:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136690">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOcIbld239oPw-JgbzvRYchXKAKMoVzAbTrUSRHAeqDX8i73pM5qDYAsDHwmRJwS1YJHSGSSiQL0qJox20E7LpyQ8q9X_Mb-qfe4leRLIQaoD89nFP_SZ0MKzfs5u33eOjWHWRTKx1Ry5KKyxZj-TpjJTo3Fn0rrgoSdG4KWJSImsnzZVXc33BsUYx_3SGpwJyjvQYzfRH8cYPfzfnj0PGwCkYS4Nya5i_LPos5WBq5pdtSli0neET_a4_Hbc9iQFsZsCO3UAZvtuqzMbu7vkb6dWYn_MMbQBM7Vy0K06N4syQ8UCAzcGLdHFJnk2G6meovwYCDpeBdVywMhMbsTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec16b7119.mp4?token=lguKxTjFVb1zHejT1_yzU6WPI7sKomEmXDr3jaHuitEt6dCxZ_fVDl2K_BdUZwyavH2YwVgMMuMLaAxy54n-OoBLq87MNKnKA_MFMbMWHiTw-RlV1WaJjjovRm5-wuWFetXnLeb61PVq54aG_gnzTy9xOJqpdH-865nqTAwsQwVSAGVpBk9XcCfSFJtpJugMldTjJdteghwuGLxLLfEiDqZkctYnIm03PwF81vlYp4sg96zdTckWwRR8N0p2Olk-P9W9USPruvdYgwdUz_V5yDY-PG-XDG32gWtEzB2pThMYNYWitHZjG3uotwqcoS2hnT-ktlhYLQeBOlPuIBVaPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec16b7119.mp4?token=lguKxTjFVb1zHejT1_yzU6WPI7sKomEmXDr3jaHuitEt6dCxZ_fVDl2K_BdUZwyavH2YwVgMMuMLaAxy54n-OoBLq87MNKnKA_MFMbMWHiTw-RlV1WaJjjovRm5-wuWFetXnLeb61PVq54aG_gnzTy9xOJqpdH-865nqTAwsQwVSAGVpBk9XcCfSFJtpJugMldTjJdteghwuGLxLLfEiDqZkctYnIm03PwF81vlYp4sg96zdTckWwRR8N0p2Olk-P9W9USPruvdYgwdUz_V5yDY-PG-XDG32gWtEzB2pThMYNYWitHZjG3uotwqcoS2hnT-ktlhYLQeBOlPuIBVaPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیف سطلی هم با قیمت ۱۰۰۰ یورو (۲۰۰ میلیون تومن) مُد شد.
اگه پول ندارید بخرید میتونید به جاش همون سطل رو دستتون بگیرید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136690" target="_blank">📅 17:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136688">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KievP3gmRvfZze3nu8aY0bUvAvLHm2jqhF2CfI-GhzzP4oYp4waSG452diSuptNWYlq4t6IOBdKqjfXGEylC1QZYFRhqVkRPxXUVS0Q55mUWX0XybbUnSz-QUiWZsdT6cXrXxQk2_XHwL-CqI_eTNKMdSnTrFWNqUHVv5BIVKLSSVOSRoZvwKbjnf211ufHApNRtFkSJgFbzfmIgy12V7iowGQI_54lARVkhS-ReOiqOFdRkspWw5wXDuznPxZAU6blSwqwJccHfijp402UNa4KqEBmMPnHZP9MOvzkvjOtV0YVf3LjlbNI27s0fCBq73RdutJNw7uDjZFGiboMUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
۶ ماه طول کشید تا تونستم دوباره اینجا قدم بذارم.
🔴
جاویدنام
#غزل_جانقربان
تک فرزند ١۵ ساله و هنرجوی کامپیوتر ، ١٩ دی ماه به همراه پدرو مادرش دراعتراضات شرکت کرده بود، که نزدیک زاینده رود با شلیک سه گلوله وحوش رژیم اشغالگر جمهوری اسلامی کشته شد.
🤔
حرام زاده های حکومتی که دم از وطن و دین میزنن، قاتلین هم وطنان ما بودن و هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136688" target="_blank">📅 17:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136687">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
عون: لبنان تنها زمانی می‌تواند امن باشد که یک کشور با یک ارتش باشد
🔴
خلع سلاح حزب‌الله تنها در صورتی امکان‌پذیر است که اسرائیل عقب نشینی کند، ارتش لبنان کنترل کامل و انحصاری این کشور را در دست بگیرد و برنامه بازسازی تحت مدیریت دولت اجرا شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136687" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136686">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
به گزارش مرکز اطلاعات دریایی مشترک، حوثی‌های یمن (انصارالله) آمادگی‌های لازم برای حمله به کشتی‌های تجاری در نزدیکی تنگه باب‌المندب را به پایان رسانده‌اند.
🔴
حوثی‌ها موشک‌ها و پهپادها را در نزدیکی این آبراه استراتژیک مستقر کرده‌اند تا برای حملات احتمالی به کشتی‌ها آماده باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136686" target="_blank">📅 17:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136685">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
اکسیوس : حمله به تهران احتمالا می‌تونه؛ واکنش گسترده‌تر ایران رو با دنبال داشته باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136685" target="_blank">📅 17:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136684">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
زلنسکی، رئیس‌جمهور اوکراین: امروز حملات دوربرد ما اهداف مهمی را در مناطق کراسنودار و استاوروپول روسیه با موفقیت درهم کوبید.
🔴
در پهنهٔ دریای سیاه و دریای آزوف هم یک نفت‌کش و ۴ کشتی باری از «ناوگان سایه» روسیه هدف قرار گرفتند.
🔴
ما آتش جنگ را به خانهٔ اصلی‌اش یعنی خاک روسیه بازمی‌گردانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136684" target="_blank">📅 17:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136683">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0-fKRlifvYeIUhcIG2TjeI-A-X56gtxZSwWSZiV3nk-Blu8Aw5mvqXit-KCHHbQE-y-rGxyNwqd7OoEkiq4XO6AMN0y1MLbpjxn9Q2oJ9Ru7YlWRfYUbuYtHv2wJXM8vt_K4vOI8d9M9odRVSYAcgUj6yKM2LhUxwxVtBWs6QmoMTEHgipOEwBZVAJon_RMmF1Xu5HLiJT_syuewkAhUREKJBJyNbaiOynAD4FSA8zuxgwef9mNkojqqIGLI2jlTpCw7T0-n8VG2ZF9RRwYw0kWzOr8k6qpbMRMLIa5knpSHPLRKi33CD8aehLL-8DFgPPo5d-w7H9Cdt8WDYvZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: به نظر می‌رسد ایران هر ایده‌ای را که شامل یک جدول زمانی برای آتش‌بس باشد، رد می‌کند و هرگونه مذاکره‌ای باید مبتنی بر بازگشت به اجرای یادداشت تفاهم باشد.
🔴
تهران معتقد است که مهلت‌های آتش‌بس صرفاً دوره‌هایی برای تجدید قوا و بازگشت به جنگ هستند و نمی‌خواهد در این چرخه گرفتار شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136683" target="_blank">📅 17:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136682">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
معاون امنیتی استانداری چهارمحال و بختیاری: در حملات دیشب آمریکا، نقاطی از شهرستان کیار مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136682" target="_blank">📅 17:12 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
