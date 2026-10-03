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
<img src="https://cdn4.telesco.pe/file/mO5IzfKLgXNTU3Afdx1zJjQbAbzOvCqh3Dp0VHaIhMrXmeEeAQSMYlRTveZv6i8Nrp1IyWx0vgRmcVfbsTbgBgti6ZZH0YE0d6KL1GoTedKDsPmAHg07QA4XJ5G0bBSq3_JrQtnx2HyzhZBosx6GkbqQLp-ZOKN3hFepKaSEdahwYicqHHaXKOEZYXOSWjGpIWPb8HFKLEPiSYbyH-5YyZOzQQU0TQ7upTgYOVkd4betpLW62LWJf_E7aN1fiqeSvuzB8utcSl_5VsV21iycjEq-0MhUxWg33J7Lw64A0P3FOJEcXurpnu5XtT80t7cXIhbfjnn5VY5xyh5t8uz3xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-150764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قطعی برق در اثر طوفان شدید در قم
🔴
بر اثر وقوع طوفان همراه با باد شدید و گردوخاک در سطح استان قم، تعدادی از فیدرهای شبکه توزیع برق از مدار خارج شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/150764" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150763">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d34c7efd.mp4?token=o2Ec8jwgC5GTrGeM8LSvmjLfSFYqpHUzx9HSGE4UQIDBIF66x5B1MpuFwtohrUCPUTd2ZJsfkzx0NITZU9cwl9BNRn416Byq6w3mJAL2gNNc0OtL7oBTzmS5N7koMtD9UELX1klZ5aXoX7t41eQ7Yc4GVJ09umY8rW2XZgY0gW0ytQ3CwkTAFCluSWRtw509AjVBL0fvTqDnvPKPFMe7Hb9euMw4d-dpxxjh6igw_Tz7uHgsh9QLhpVZC1llO5IZKwwxLgM19Bkf8NOY3sfGOmmkwcYhj9OpcvDztmqN2D2drXygqf7JAb3gPO0w4y0DHkDezwfKASH2jFPmqjHBN6pNntKitze4LnG3ouYEyK0EmW0Lr3luvoqJZJvHUeO905Asyhq1O2gVNPdAdKVTFl1LA_zIZF5WO6IHFShD_PkekmrTdYkTY1jt77elSBHOUDWDh10hqBalUldyJPxrq7Q7sTmxBGvYZLz-0l2yGfFspJGj1lPMT6CzW2R0UfVJZzVnlP8JY-pUOo2cMpwad4dDKfPXCA8clYOi_Ck_iZttW2Eyrla5pSaCnyCQtRoc06AjxmSVdvkIyXUWFinwTKDOQp-r4cI9PnP1eRvSvqvwj1Gu_zXRpBLyLut3AL7pykIgG7QZEd58-VnSS2EvldFvcPR25-OcHjs2t8QBHbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d34c7efd.mp4?token=o2Ec8jwgC5GTrGeM8LSvmjLfSFYqpHUzx9HSGE4UQIDBIF66x5B1MpuFwtohrUCPUTd2ZJsfkzx0NITZU9cwl9BNRn416Byq6w3mJAL2gNNc0OtL7oBTzmS5N7koMtD9UELX1klZ5aXoX7t41eQ7Yc4GVJ09umY8rW2XZgY0gW0ytQ3CwkTAFCluSWRtw509AjVBL0fvTqDnvPKPFMe7Hb9euMw4d-dpxxjh6igw_Tz7uHgsh9QLhpVZC1llO5IZKwwxLgM19Bkf8NOY3sfGOmmkwcYhj9OpcvDztmqN2D2drXygqf7JAb3gPO0w4y0DHkDezwfKASH2jFPmqjHBN6pNntKitze4LnG3ouYEyK0EmW0Lr3luvoqJZJvHUeO905Asyhq1O2gVNPdAdKVTFl1LA_zIZF5WO6IHFShD_PkekmrTdYkTY1jt77elSBHOUDWDh10hqBalUldyJPxrq7Q7sTmxBGvYZLz-0l2yGfFspJGj1lPMT6CzW2R0UfVJZzVnlP8JY-pUOo2cMpwad4dDKfPXCA8clYOi_Ck_iZttW2Eyrla5pSaCnyCQtRoc06AjxmSVdvkIyXUWFinwTKDOQp-r4cI9PnP1eRvSvqvwj1Gu_zXRpBLyLut3AL7pykIgG7QZEd58-VnSS2EvldFvcPR25-OcHjs2t8QBHbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون؛ بارش شدید باران در برخی مناطق تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/150763" target="_blank">📅 17:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150762">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ: معمولاً در انتخابات میان‌دوره‌ای عملکرد خوبی ندارید و نمی‌دانم چرا
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/150762" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150761">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مهر: شنیده شدن صدای انفجار در جزیره قشم از سوی دریا
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/150761" target="_blank">📅 17:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150760">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی ترور دو تن از فرماندهان سامانه موشکی حماس در دو حمله جداگانه روز گذشته در غزه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/150760" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150759">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترکی الفیصل، رئیس پیشین دستگاه اطلاعاتی عربستان: یمن، تنگه هرمز، بازدارندگی آمریکا و جاه‌طلبی‌های هسته‌ای ایران در حال تغییر محاسبات امنیتی عربستان هستند
🔴
خویشتنداری دیگر قابل ادامه نیست
🔴
چین وظیفه دارد همان نقشی را ایفا کند که هنگام توافق عربستان و ایران ایفا کرد؛ باید منتظر بمانیم و ببینیم پکن چه کاری انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/150759" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150758">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گزارش‌های اولیه از سرنگونی یک فروند پهپاد آمریکایی در نزدیکی سواحل ایران حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/150758" target="_blank">📅 17:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150757">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95b509824.mp4?token=LNcm0I5si0K-9RvPMmntHLv8tCCj0IEV_uzCY4Nf_-rNMYuP045BS34U9SQtSXnaNwTxLGI6j4vRPNfUKGPjL0acOoNE0UweBGYv6y2sgu_jeyI-kwzFeVAwo7bx6FvZCKmJoU1NT1lZYejBg2gDyA7asKtrg6iJHz6-Z3EuwpYIGFLxQZCl1gtpskHKeoMo1ca_bYAgsP55eXMiEzZIZHeVIFtnGzrieTErB2UbJOyHuBhBz0gXePnlpMjhZ3Gu-yzturKFmlcJLGCKvv2o588cOs-SGDkGV2oNxGzvRw9Ju456CmMNVV5zdTom48hGJ-wZ1NWhz7WEKYH_C-_gIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95b509824.mp4?token=LNcm0I5si0K-9RvPMmntHLv8tCCj0IEV_uzCY4Nf_-rNMYuP045BS34U9SQtSXnaNwTxLGI6j4vRPNfUKGPjL0acOoNE0UweBGYv6y2sgu_jeyI-kwzFeVAwo7bx6FvZCKmJoU1NT1lZYejBg2gDyA7asKtrg6iJHz6-Z3EuwpYIGFLxQZCl1gtpskHKeoMo1ca_bYAgsP55eXMiEzZIZHeVIFtnGzrieTErB2UbJOyHuBhBz0gXePnlpMjhZ3Gu-yzturKFmlcJLGCKvv2o588cOs-SGDkGV2oNxGzvRw9Ju456CmMNVV5zdTom48hGJ-wZ1NWhz7WEKYH_C-_gIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای از فعال‌سازی سامانه‌های پدافند هوایی در جزیره قشم ایران برای مقابله با یک پهپاد امریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/150757" target="_blank">📅 17:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150756">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnhiLRrUTlioAugmkjuuzYTC8Li4l2hF9fbGJFxhV8FLl-KP9goysceUabZb_2zMiHJs5JC9Rc0cqEcYbY169ibiAcxCnfpkB6EbntUavF_SiCtHTZiTJFirrqOxI_xxtgBaI6LaNH925BGiVE2rBghIzvWDe1uzNfEeSb1QTHRCBAHgXzzhXOAxEwurNaUB1ZYl2baW65NgI4LQ1NeFlMaRBAZvjWxexkTo3_yI0QlQ21_N-zA6wBIzM85h5_-Pe8QB3LwklQiKBUbnNg7NVGV-LSLNP3q7WH7A2neKt_T9Bwc4ear0YUsQvWWCURPpWRmuXXfg6VDJCAMmiESTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌های اولیه از سرنگونی یک فروند پهپاد آمریکایی در نزدیکی سواحل ایران حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/150756" target="_blank">📅 17:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150755">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: آمریکا در حال تقویت گسترده نیروهای خود در خاورمیانه و ارسال سامانه‌های پدافندی به کشورهای عربی برای احتمال ازسرگیری جنگ ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/150755" target="_blank">📅 16:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150754">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/k4oZCBWMbm0lpfhsCLULDXr4Y5O730MGWBHF6XHYlL11gbnSk4i9l64VEt8bwFjd71VsB8gUu79CrOccZdCnxfab91afAuxeTw0zKu75Q6zZ6uWl_E1K8_HdaBs4noErXM_TvgJU17KTwJFO5Vci4Wo7xHYKq2Q2xUnCnqfLqnGCq3Aj37GHp7SxjHFWwFlJJvdZphZC5jdBcQF3EwS96D3UH8ddaFfqeTl098WPl6iypfsTlDwBFrhlgkxKdVC7xJ-E13nZG9gqsYIF7k7Qw2RVcJFXJUwpT8I68c2xXRKspo4m9bICj2zB4LK6lkHQNCY-ifHqla-eunCgzUYZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دریایی ایالات متحده ارتباط خود را با یک هواپیمای امدادی که شش نفر را از جزیره ناکات به سمت بوستون حمل می‌کرد، از دست داد. این هواپیما در حال پرواز از برمودا به بوستون بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/150754" target="_blank">📅 16:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150753">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
منابع عربی: وقوع چندین انفجار جدید در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/150753" target="_blank">📅 16:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150752">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی سپاه اعلام کرد که سپاه موشک های بالستیکی ساخته که میتونه اهداف متحرک (مثل ناو هواپیمابر) رو مثل آب خوردن مورد هدف قرار بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/150752" target="_blank">📅 16:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150751">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwXe5ldBKEYHyRcXmFGbHByZxzj8hhcpF39rZ2yRyIRyRLb_4p9Hj66DaOlur52CsDyLbaqOCjw2ENrho2GYWbVpSlI0TDT0_cSiLbHdSx7PHefA6StW5FvGH9nyD6HpFgAub8pcD1ypL_lvYzg9J2Vvxv1V4SG2330CQJsTc553jIPDe8NK3uC5h_XsDN6XttiulLd91W-yHI7AhW_K_2iclXZLE5R8M3qAT2oNcHY2NK9Pz8mMbO-kAwQw8DII1tB7sJ0KTg0Yru9OjmTcVMOd-Jerww9D4-IW1PaPJ-VTEJ_PHsuvWtNbpdR5cinkiksfOV5jZnfLPBN5hW2SGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادامه آتش‌سوزی در ریاض عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/150751" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150750">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا به خبرگزاری Axios: ما ایران را به شکلی بی‌سابقه منزوی می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/150750" target="_blank">📅 16:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150749">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری /
رویترز: جنگی که ترامپ بارها وعده پایان سریعش را داده بود، ناو دوم آمریکا را هم به هرمز کشاند
🔴
رویترز: ناو جورج واشنگتن به‌طور غیرمنتظره از ژاپن اعزام شده و مأموریتش پایان مشخصی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/150749" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150748">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تحلیل فارن افرز: چرا ایران به سمت تصعید جنگ خواهد رفت؟
🔴
تهران ممکن است حتی علیه اعراب عملیات زمینی به راه بیندازد و پایگاه‌های آمریکا را تصرف کند
🔴
ایران در حال تنظیم نسخه‌ای از راهبرد «چمن‌زنی» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150748" target="_blank">📅 16:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150747">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری ایالات متحده، درباره  ایران: برای اولین بار در تاریخ، از زمانی که شروع به پمپاژ نفت کردند، این هفته هیچ نفتی در آب نخواهند داشت
🔴
آن‌ها هیچ درآمدی نخواهند داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150747" target="_blank">📅 16:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150746">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ایران این هفته نفتی برای فروش نخواهد داشت
🔴
ابتدا وارد درگیری نظامی مستقیم شدیم؛ نیروی دریایی و هوایی آنها را منهدم و توان پهپادی و موشکی‌شان را به‌شدت تضعیف کردیم و امکان بازسازی آن را از بین بردیم.
🔴
سپس به «دیوار فولادی» و «محاصره» رسیدیم؛ اقدامی که پیش از این انجام نداده بودیم.
🔴
حالا با «عملیات طرد اقتصادی»، آنها را به شکلی بی‌سابقه از نظر اقتصادی منزوی کرده‌ایم.
🔴
در حال حاضر، آمریکا حدود ۱.۱ میلیارد دلار و ایران صفر است. برای نخستین بار از آغاز صادرات نفت، این هفته هیچ نفتی برای فروش روی آب نخواهند داشت و درآمدی هم نخواهند داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/150746" target="_blank">📅 16:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150745">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6caf83dd9e.mp4?token=V-Z7hdS85LtQbHW9mRfUrH7hjjBQokb3C23Hrc4_SPgpEFfF0ioz49k2cDIRPoNURjGvSvWc6GZd6S1B2Y4v2H2nFSlEm5jyIlc8rVKvsyaypwwdQ0CMGhtMFvRQTlTVd132n0xH_sz0XqqO8G4cNmPGW4jhv2dqZq2VbHrbVhQJxmvB8D1ak4qF88ShtrEyYY1ibndQLcuyGqRUMunu_HEHijKrHrv0lYhNDOPp9_YN1HcrzRLfLzRa9fmtkrCmDylvmmN2t6PNbJCnj4QtX3TgA2D-gtSPi4m13KmxaDAVyYtbiqE5jqYitkYGPjhkyDT1DwcSE02CXPRilDP9wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6caf83dd9e.mp4?token=V-Z7hdS85LtQbHW9mRfUrH7hjjBQokb3C23Hrc4_SPgpEFfF0ioz49k2cDIRPoNURjGvSvWc6GZd6S1B2Y4v2H2nFSlEm5jyIlc8rVKvsyaypwwdQ0CMGhtMFvRQTlTVd132n0xH_sz0XqqO8G4cNmPGW4jhv2dqZq2VbHrbVhQJxmvB8D1ak4qF88ShtrEyYY1ibndQLcuyGqRUMunu_HEHijKrHrv0lYhNDOPp9_YN1HcrzRLfLzRa9fmtkrCmDylvmmN2t6PNbJCnj4QtX3TgA2D-gtSPi4m13KmxaDAVyYtbiqE5jqYitkYGPjhkyDT1DwcSE02CXPRilDP9wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری ایالات متحده، درباره چین: من فکر می‌کنم که آن‌ها — در ۶۰ روز گذشته — بیدار شده‌اند به... من فکر می‌کنم که آن‌ها ندانسته بودند که مدل‌های متن‌بازشان چقدر قدرتمند هستند.
🔴
بنابراین مدل‌های متن‌باز، تقطیر صنعتی انجام می‌دهند، که یک کلمه زیبا برای دزدی از مدل‌های ایالات متحده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150745" target="_blank">📅 16:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150744">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=BBRoSK2HmqFfh5Ad6sRuB2emb9UobmlWJOeZiPkEHpizy4OYCHUT_-4wgwbQVhiY1Bl0ckus7HTzC_J_mU9UDt8pHq64ENwVBL0l8P7CV3uis8-hkIdVl21QsTQ96INEaX8TrHKA5_ZI05ftI8UfyRZ8HDWPFjytMqgPb69mn17DYGqEZe9HBSJh60a0k6SrL-EUfk8nOJisaxXmZzLoNiZpEqoHxwX6xEgibIr9QP6n9Xaei0OiV5V8a3wY5c7UEVWCjvNPa8oBeRbJETxcffsE_HicZn1HUMRjsBx5oWSIh0MaQZCbbED45GLBIxeL8uVovWSU9jJ3CM7nA3daqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=BBRoSK2HmqFfh5Ad6sRuB2emb9UobmlWJOeZiPkEHpizy4OYCHUT_-4wgwbQVhiY1Bl0ckus7HTzC_J_mU9UDt8pHq64ENwVBL0l8P7CV3uis8-hkIdVl21QsTQ96INEaX8TrHKA5_ZI05ftI8UfyRZ8HDWPFjytMqgPb69mn17DYGqEZe9HBSJh60a0k6SrL-EUfk8nOJisaxXmZzLoNiZpEqoHxwX6xEgibIr9QP6n9Xaei0OiV5V8a3wY5c7UEVWCjvNPa8oBeRbJETxcffsE_HicZn1HUMRjsBx5oWSIh0MaQZCbbED45GLBIxeL8uVovWSU9jJ3CM7nA3daqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده، بسنت:
ما به سوی دیگر این اختلاف با رژیم ایران خواهیم رسید. فکر می‌کنم عرضه نفت بیشتر خواهد شد. فکر می‌کنم قیمت‌ها بسیار پایین‌تر خواهند آمد.
🔴
افزایش دستمزدها ادامه خواهد داشت، زیرا ما در حال رنسانس تولید هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/150744" target="_blank">📅 16:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150743">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10dd1f1bb3.mp4?token=vpvWZtOzn9WuaCouScdzEjmmY_bFXrMLbFasygHPcfv2VdrD81szFUkjD5wocuIn0u1eWp3WYaNyuj6rE2s6dILvvJX3LWNigXTihVA1GpqFfOfONavwMc1YOsT06lmTB5kJbHxI3dMCvtiZyurCKz6M_36kynul-iW4trxsLAxj_ztmw2jORS8cKkoDb2kQJ3L1yAqqoVQ9mU7mB96LQqh89ZlcqXIcWURaeGHQBSWtpW3aF-BFoglhToHjoiuVYpIJvs7Ds-ZhMo4Dmi9ZtMCFqJQH4BfcbL0FU5ykfyw680HBUlqnyOcv8rkUd_ODQ-wPejoWv7-yPtJyXssOGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10dd1f1bb3.mp4?token=vpvWZtOzn9WuaCouScdzEjmmY_bFXrMLbFasygHPcfv2VdrD81szFUkjD5wocuIn0u1eWp3WYaNyuj6rE2s6dILvvJX3LWNigXTihVA1GpqFfOfONavwMc1YOsT06lmTB5kJbHxI3dMCvtiZyurCKz6M_36kynul-iW4trxsLAxj_ztmw2jORS8cKkoDb2kQJ3L1yAqqoVQ9mU7mB96LQqh89ZlcqXIcWURaeGHQBSWtpW3aF-BFoglhToHjoiuVYpIJvs7Ds-ZhMo4Dmi9ZtMCFqJQH4BfcbL0FU5ykfyw680HBUlqnyOcv8rkUd_ODQ-wPejoWv7-yPtJyXssOGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری ایالات متحده، درباره چین: یکی از مدل‌های بسیار قدرتمند آن‌ها، کیمی است. کیمی فکر می‌کند که کلود است. گاهی اوقات کیمی به شما می‌گوید که کلود است.
🔴
کیمی برخی از طرح‌های سلاح‌های ارتش آزادی‌بخش خلق را به آنتروپیک ارسال کرد. بنابراین فکر می‌کنم چیزهایی از این دست باعث شده که چینی‌ها متوجه شوند این یک فناوری بسیار قدرتمند است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/150743" target="_blank">📅 16:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150742">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
تریتا پارسی: فقط چین است که می‌تواند جلوی جنگ سوم ترامپ با ایران را بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/150742" target="_blank">📅 16:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150741">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e853be9f.mp4?token=Ls4mmDFjsdNKspFCk_hSaBxhl0mKUgeKboUYTSfj5w0rAUeHknjHZSD-Pn48yGEN7nlVd0iUUwZjC7L3rmC1r4-TXDpLkBcAHATMtuEKLidcZFRypKnOjZB14j7LrSj2U4QRXURxm6zZ52BiPqzTsrztUTi866_YuV8PT4XcdA3_Z_CavQZT9nxeqDxQvdZJOOG2fv2sAfmTN6Ok82OZtgriWXWfWtf53V6X8WQGCZQb9dlKVmOg-xWJJ-mIJhEjs0UjJyREifRYRRbXRez8wbS3tQG0KIEytDHSaTI1ANDUekio62uKJkquPw2_WboYwO6ttNNKxo5GsrxYKJnRig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e853be9f.mp4?token=Ls4mmDFjsdNKspFCk_hSaBxhl0mKUgeKboUYTSfj5w0rAUeHknjHZSD-Pn48yGEN7nlVd0iUUwZjC7L3rmC1r4-TXDpLkBcAHATMtuEKLidcZFRypKnOjZB14j7LrSj2U4QRXURxm6zZ52BiPqzTsrztUTi866_YuV8PT4XcdA3_Z_CavQZT9nxeqDxQvdZJOOG2fv2sAfmTN6Ok82OZtgriWXWfWtf53V6X8WQGCZQb9dlKVmOg-xWJJ-mIJhEjs0UjJyREifRYRRbXRez8wbS3tQG0KIEytDHSaTI1ANDUekio62uKJkquPw2_WboYwO6ttNNKxo5GsrxYKJnRig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری ایالات متحده:
فهمیدم که فاینانشال تایمز ضد آمریکایی و ضد کسب‌وکار است. آن‌ها تب دارند.
🔴
آن‌ها مدام سعی می‌کنند برای ایالات متحده مشکل ایجاد کنند. اما بیایید آن نشریه‌ی لجن‌گشته در لندن را کنار بگذاریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/150741" target="_blank">📅 15:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150740">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نتایج اولیه کنکور ۱۴۰۵ اعلام شد!
🔗
my.sanjesh.org
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/150740" target="_blank">📅 15:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150739">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9110f11b37.mp4?token=mEi0vboFZ16qwjb8SwEN_PLt-6ykZPxPCbosXJojVcumDCVrFIUdrXCPoZSBsphUIMeFdhv8mdPJKS-NvDKOrr98vbdpQ0o0UQJ427esA5aKvf2lH3ax8jrbLc-AKiRlWu4cFdInx1rq6mkFaYm0k5XvUfr1Z9GPpfgx86izGlrxiJnUVTKWsqr649vXUHydQXVQ7voSeHYlSv0NwGMeywG0WERzqSL3rWPyKUTenvFFAyhps0RisSgWpWg7NechfUuvBC823zaQB1n3vZSmedqGAk3FDM2QkFGElJMkH_B5esgIryZ2hMUPm2A2oi46O_Jf39umD2TZrPm17fhW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9110f11b37.mp4?token=mEi0vboFZ16qwjb8SwEN_PLt-6ykZPxPCbosXJojVcumDCVrFIUdrXCPoZSBsphUIMeFdhv8mdPJKS-NvDKOrr98vbdpQ0o0UQJ427esA5aKvf2lH3ax8jrbLc-AKiRlWu4cFdInx1rq6mkFaYm0k5XvUfr1Z9GPpfgx86izGlrxiJnUVTKWsqr649vXUHydQXVQ7voSeHYlSv0NwGMeywG0WERzqSL3rWPyKUTenvFFAyhps0RisSgWpWg7NechfUuvBC823zaQB1n3vZSmedqGAk3FDM2QkFGElJMkH_B5esgIryZ2hMUPm2A2oi46O_Jf39umD2TZrPm17fhW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت: ابتدا وارد درگیری نظامی مستقیم شدیم؛ نیروی دریایی و هوایی آنها را منهدم و توان پهپادی و موشکی‌شان را به‌شدت تضعیف کردیم و امکان بازسازی آن را از بین بردیم
🔴
سپس به «دیوار آهنین» و «محاصره» رسیدیم؛ اقدامی که پیش از این انجام نداده بودیم. حالا با «عملیات طرد اقتصادی»، آنها را به شکلی بی‌سابقه از نظر اقتصادی منزوی کرده‌ایم.
🔴
در حال حاضر، آمریکا حدود ۱.۱ میلیارد دلار و ایران صفر است. برای نخستین بار از آغاز صادرات نفت، این هفته هیچ نفتی برای فروش روی آب نخواهند داشت و درآمدی هم نخواهند داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/150739" target="_blank">📅 15:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150738">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOpx7qUzjFocSiiKi0X_XIozUhv7ykRZdbLMnaOgXP6WVG2v45Ac8YVCdYk5Wp7d0DPX4yYFEA3WGP3fUfub63JkayU6jVRmkHWP0dYs-FbckhOlsTjlKnxsf99BCCY1DiFMTJI4lJsHFxJFnUbOq1rjtVmHdRRRm8xeJM5MtoDUW-SEZyDMip9vA0LmBkWpX69oP482BkfqggzCA6ePTFazfmVqBNeyZc6Y5yXUh1X3DCkl6VjGW8xzbu3EQyKNdsq1Eo2mS2qEpxXBNCGOVrAgNUgqPgV2VreB8-szjKBtQ6wOa5ph8RfRY7ouRseQ-2iMXxmub035BT_aXOJEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای حجم آتش‌سوزی‌های رخ داده در پالایشگاه آرامکو در ریاض را نشان می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/150738" target="_blank">📅 15:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150737">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXXhsHquhlGYssSSrmVNDL_xtcGJkMDMrgko8rNhmwmJ9Z2Z5ZyoLI4DbBBzA0JKMAVx6YuuohTYHYCgvXx-s9zZYDLvns_hWb5n2uAFfCM78BSxHsVo14bILZxXt-iJv7cL95MYK8yeNNBNVQa-h5hwW3yp_jatiod7YsKlq1oDZkZA4psgtPARWuTgrmiMJAHJqdrmzGRHbR2CkvNGpnwmpat_ZonyhZdvg_Xyi-aQon5l1ip_3nn3rRRnUUMSbAJ1i9RclQUaNRx_Szj4stL54AKENt4v37yMNEGBZZIkTsuEE3OdDK8ZKBDlPuqC9nQW9XMfMinRQfuY8gi5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فساد در سازمان بورس ~ قانون بازنشستگان رانتی شده ~ یعنی هیچ جایگزینی برای پیرمردها نیست؟  عبدالرضا داوری در توئیتر نوشت: آقای دکتر عارف! ‏
🔴
عده‌ای به‌طور غیرقانونی در پی انتصاب دوباره صیدی، مدیر بازنشسته، به ریاست سازمان بورس هستند.
🔴
سکوت نکنید و مانع تبدیل…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/150737" target="_blank">📅 15:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150736">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkF7WELJJOENjPa7Jh7ny9MLatRD1U0OkB9-U3KhA6cE1dtI24vuz4oZBOO0Om9kbsxreY3QSHy3Kwp1UcKQuHNHo_FutMtpZ1b3FbCek7HXuutJE4b042zQVe-UQz-s_9_kR1OG3FSFCHOBRtyWqdL98xbbJQtp8rLoF1EVgjHdzPSADTlSzQJPw7IBQvpzCplQtl6SlgTxub7W2bs2lJJgkkJs0pZOUQs3gY8ZmY5E3bW4DB8gxhaf_EPwbGfca9tzIR9rgdAktxoDLuaxy9iJjNUEex9hFvaDeeiS5ixUvlsZOdrlDALzMci96UH-w9t--V26TeRL7uIJbkJNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون ، حضور ۷ سوخت‌رسان آمریکایی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150736" target="_blank">📅 15:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150735">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
گزارش ها وقوع چندین انفجار شدید در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150735" target="_blank">📅 15:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150733">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
رویترز با استناد به گزارشی از نیویورک‌تایمز: مذاکرات میان روسیه و آمریکا اکنون شامل یک قرارداد نفتی چندمیلیارددلاری مرتبط با دونالد ترامپ است
🔴
بر اساس این گزارش، این قرارداد نفتی مجموعه گسترده‌ای از میادین نفتی، پالایشگاه‌ها و جایگاه‌های سوخت در سراسر جهان را که متعلق به شرکت لوک‌اویل است، دربرمی‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/150733" target="_blank">📅 15:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150732">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22b115038.mp4?token=KidAF5aGKCqm05n13keZNbVirPHt1nwf0Wp1_f-iextEA9IpRCHTzb0JOtSlkNpQ4m-J0xPN55JX7XjzpS7QUY1nA0BmlvQkh5fVUIwUfsAbpifXAizvMXtc-m8KSHw--UykeqoU6fDCCI4N6nL5_ST1Gv5uIKPm6-M0Z2cO6sGl0NFUi4FLG86290BOHibInrKtki8brbH3AvI021MCFD6JznL9bbN9HSEQDhQIkWofo6OhfyiuihgQkOXncEFe4LPYPL8LeT3pgFrLOOagygLNfXcCpoSZIKwwtu0uPDT0GbG04syky5_8RAMmS7wQmoM_bQt9UbCdZNrgvfsriA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22b115038.mp4?token=KidAF5aGKCqm05n13keZNbVirPHt1nwf0Wp1_f-iextEA9IpRCHTzb0JOtSlkNpQ4m-J0xPN55JX7XjzpS7QUY1nA0BmlvQkh5fVUIwUfsAbpifXAizvMXtc-m8KSHw--UykeqoU6fDCCI4N6nL5_ST1Gv5uIKPm6-M0Z2cO6sGl0NFUi4FLG86290BOHibInrKtki8brbH3AvI021MCFD6JznL9bbN9HSEQDhQIkWofo6OhfyiuihgQkOXncEFe4LPYPL8LeT3pgFrLOOagygLNfXcCpoSZIKwwtu0uPDT0GbG04syky5_8RAMmS7wQmoM_bQt9UbCdZNrgvfsriA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رگبار شدید باران خرم آباد دقایقی قبل
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150732" target="_blank">📅 14:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150731">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki1Dz_lBMscf2J-wH5bPsGDLNhVdsg_NbZwO8PaxcKDpeyavwpeQbvV_QypSZZZH7pAaqO3YCeaksM_4Qy28CseH7MtJk6lIeS3v1TG4v3td5cABfdX75VGMGpUgpyZC449Od5VKxmGB4hVnbj4QfPm3--c-EJhjz5EfHJ2Q5gPam-x2qFAPwXhojjZFHkJ11vE0T8djQTbebGhF9dr0YdgC_fCe-mqTQXfoWwvrKwwnL8jjxyIv2v2ih3Nf6TAs9SvFgUicVNmfEZahEYILifkRe23DEqWsRBhjvQp-3tT99-aAbiEMVfC9QnhGcuOEMqawGO-A3H4uJ7mEwuPRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : من خوشحالم که اعلام کنم دولت من، از همین لحظه، شروع به ارسال "چک" به ارزش تقریباً 100 دلار به بیش از 20 میلیون نفر از سالمندان عزیز خواهد کرد تا به آنها در پرداخت حق بیمه بخش B برنامه "مدیکر" کمک شود، که ما قبلاً میزان آن را به طور قابل توجهی کاهش داده‌ایم.
🔴
این پول از "صندوق بهبود مدیکر" تامین خواهد شد، یک "صندوق بی‌فایده" که تنها توسط دموکرات‌ها در کنگره برای پرداخت هزینه‌های مربوط به فساد، تقلب و سوء استفاده برای دوستان خاص خودشان استفاده شده است و در نتیجه، هزینه‌های مراقبت‌های بهداشتی را افزایش داده است.
🔴
ما سرانجام از این صندوق، همراه با توافق‌های "منافع ویژه" من، برای کاهش قابل توجه هزینه‌ها برای سالمندانمان استفاده خواهیم کرد.
🔴
از آنجایی که من در این موضوع بسیار مهم برای مردم آمریکا به وعده خود عمل کردم، آنها همچنین می‌توانند اطمینان داشته باشند که "سود ترامپ" به مبلغ 5000 دلار، که بسیار محبوب است، به هر شهروند آمریکایی پرداخت خواهد شد، اگر و زمانی که جمهوری‌خواهان در انتخابات میان‌دوره‌ای پیروز شوند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/150731" target="_blank">📅 14:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150730">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884f668d3f.mp4?token=NJiMXAnq5sAzXQwsn3lUeMn7YfcqrXk6n8WYJi2YarVAUn9No5eYoEzYXdSO7iDmCiV_E7Nn5weCSe0esqvKBMPvwebxoOHks-Itz58FxiBtZaMT0uDnlNZQlg2b0XlO0IRXj6sQtj5sK9HXThCutA8faVdVkIW2_5a2DIiZekASbLGDxPJ8Q8-39xVw9kSTVpV9HDFyYiA3dQ5smUM1kiHRkRFt7PkllHF6wFWw0Hsi3GPYzladRMnmOO7vEByYg_N-rfg5AsqubkaIrpk8huKb_P6Rv3jr4imP88cq9BRlP-O9RZotN2byFpHfQae9zgg1FDvl9u6j28_NzbkzQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884f668d3f.mp4?token=NJiMXAnq5sAzXQwsn3lUeMn7YfcqrXk6n8WYJi2YarVAUn9No5eYoEzYXdSO7iDmCiV_E7Nn5weCSe0esqvKBMPvwebxoOHks-Itz58FxiBtZaMT0uDnlNZQlg2b0XlO0IRXj6sQtj5sK9HXThCutA8faVdVkIW2_5a2DIiZekASbLGDxPJ8Q8-39xVw9kSTVpV9HDFyYiA3dQ5smUM1kiHRkRFt7PkllHF6wFWw0Hsi3GPYzladRMnmOO7vEByYg_N-rfg5AsqubkaIrpk8huKb_P6Rv3jr4imP88cq9BRlP-O9RZotN2byFpHfQae9zgg1FDvl9u6j28_NzbkzQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا باید صبورانه فشار اقتصادی علیه ایران را ادامه بدهد
🔴
مت پاتینگر، معاون مشاور امنیت ملی سابق ترامپ: ترامپ در نهایت به راهبردی رسیده که دقیقاً راهبرد درستی است: محاصره اقتصادی ایران؛ یعنی تا هر زمانی که لازم است به این فشار ادامه دهیم و هم‌زمان انتقال نفت از طریق تنگه هرمز را حفظ کنیم ... در کنار آن، باید مسیرهای جایگزین ایجاد کرد.
🔴
دقیقاً همین کاری که عربستان سعودی و امارات متحده عربی با احداث خطوط لوله جدید انجام می‌دهند. در نهایت، باید صبور باشیم ... امیدوارم این مسئله خیلی زود حل شود ... باید تا هر زمانی که لازم است به این فشار ادامه داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150730" target="_blank">📅 14:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150729">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
اخبار تایید نشده حاکی از آن است که تأسیسات آرامکو در ریاض، عربستان سعودی، هدف حمله حوثی ها قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/150729" target="_blank">📅 14:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150728">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزارت امور خارجه روسیه از دیپلمات‌ها و شهروندان خارجی خواسته است که شهر کی‌یف، پایتخت اوکراین، را ترک کنند و در آنجا نمانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150728" target="_blank">📅 14:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150727">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">دلار هر ۵۰هزار که بالا میره یه خواننده میارن
رو ۱۵۰قیصر اوردن
رو۲۰۰ نامجو اوردن
رو ۲۵۰ بیژن اوردن
رو ۳۰۰ معین میاد
رو ۴۰۰ داریوش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150727" target="_blank">📅 14:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150726">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رئیس کمیسیون اجتماعی مجلس: احتمالاً ۵ الی ۱۰ میلیون تومان به حقوق کارمندان اضافه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150726" target="_blank">📅 14:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150725">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de51u0euKfXh5cVTbm411bWJXgNmOzWuQbm-kOohQxu-Y7VmdqRKXVfSqMDzH2JPIHyXK6BEUDCrkadWbhFt2QG7MWzRdHoE0HfbbTUksMnyqZNK2i7Xaz1NMk-4Ah6yX0HEaCP5HHcuPTjqBu9ZuW5GeTWYNQxl8XswWi2PwfoPxkByQOVHoJhg_Dm8KQ5GAC8OlyUBrAlCB7s3_GGv-STrZ_Ck_h_a1jFdy8o6dqrMsPB9JH8y3i89zZeprzLZyjfl0U_Eegk3Pzo-6f5heqZE2A1l5kzpChBiKRpt1RJ5zqqlSrKTQtBqPxz5RzfID3NzRjNc1vHsITu5fDQVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با حملات هوایی عربستان سعودی بر پایتخت یمن، صنعا، تعداد هواپیماهایی که از فرود آمدن در فرودگاه بین‌المللی ریاض خودداری می‌کنند، به ۶ فروند رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150725" target="_blank">📅 14:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150724">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKV_t-1cZiT5Fup2-lJhxjzi6AreZkihBxS5k0TY9Ff5xAPNFDnZUH2it1CnIWyXljFTf7rzv_IYGReaH-WTj7tNDCk8Beg3JJ2OAPi2J8n31cK0uZ5NDYG68lrqEfv3R00rf04hAptY8AXhp7L6Y3WPusFcxBODjp-FrjL5XNELmvCgeW6Ad-U5RHJ6q8WaTHJ8bgswbS1NqEDqYpsT0ndEpkqTA5YFEU9R3nOqTbB3cRd5fvVkMlJAVItcJ6oyBkz_bkhxTdwoJd9e4rzDJTnDLV_7WGqdsW5oCHxbf_7hsNkwevjLjtMOCvz_QYBbfSJvmGa0BORdDcUG5hwHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کره شمالی اعلام کرد که در آزمایش یک موشک راهبردی میان‌برد، از هوش مصنوعی استفاده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150724" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150723">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqE2femuDES0Ylkdh_Tetsuzv1v2R2ih_grZkYtnBhkKCm3cHcw3rZ3TEMOJ7OA5Hd2y2hVix4ZzvjqVL8xLkXeN_ntQienUyzvmKdMDziauzpIYoDx1ROUPcd83BBcdoLUBHSzxs2kZVUk19e5pgr7Gbbv2dVUSSu6J24wcbpfx50LM15aEO3H44zPusE1kCBXFGZ8E82f-0Zrgi3tY95iB7tQ9nDZJKY6q8qKyRmNP6esE7v38scntZvyl022LP5UghTMbiuAISfJm3KtiovNAcXxx0TFfgY5AiK-cfL-_FYQT9UMFPhpQ4uvC1pIfZO1rwOMpySD7izfq9LQ7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از هفته‌ای پر بارش در غرب کشور خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150723" target="_blank">📅 14:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150722">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تحلیل نیویورکر: چرا جنگ احتمالاً دوباره اوج خواهد گرفت؟
🔴
احتمالاً توافق اسلام‌آباد بهترین توافقی بود که ایران در مقایسه با هر توافقی در سال‌های گذشته روی میز داشت و شاید بهترین توافقی بود که در آینده نیز می‌توانست به دست بیاورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150722" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150721">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
اگه میخوای تو بازار دلار و طلا سرمایه گذاری کنی حتما اینجارو داشته باش تا ضرر نکنی
👇
https://t.me/+CEe6KOyxOHdiNTE8
https://t.me/+CEe6KOyxOHdiNTE8</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/150721" target="_blank">📅 14:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150720">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
دو تا رعد و برق زد دلار ۵ تومن کشید بالا شد ۲۷۰ تومن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150720" target="_blank">📅 13:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150719">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
دو تا رعد و برق زد دلار ۵ تومن کشید بالا شد ۲۷۰ تومن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/150719" target="_blank">📅 13:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150718">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaxOYEnkcQYnBpW9yOV4E7nx-bF-ZFRyXznFaRvHStSbgMYzuDZCPNYGsOTbQ76Uai-OAmAjGo6-41wvVMKkKc-qqgMJRGH5gbY9QeH7U6UthGD8SNh73CdSI54fPq5M7_rK_qUXVrElN0wiNHeROnKfHW_NUgSeuLZ_duOj8C3aYj55n39WQ9zLdjLclwkCcXjeEB2x1oqa99kMbiG-TnEK8MU--vmp6wwWn1A6uvWakd_Kthy93rC6wTf9Til_E_APizKfiBBmkLNq5K5d8Wq7Laq2rWOzVh5-2WUe3CXHow5YIR7RLulD-HATBGjbN3-9lBfNWTQVMCJL5E7lrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله نظامی عربستان سعودی، کوه عطان را در پایتخت یمن، صنعا، هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150718" target="_blank">📅 13:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150717">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دلار از 268,000 تومان هم عبور کرد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150717" target="_blank">📅 13:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150716">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
هم اکنون ، آسمان برخی نقاط تهران شاهد وقوع رعدوبرق سنگین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150716" target="_blank">📅 13:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150715">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
صداوسیما: روحیه ساکنان منطقه تپه علی الطاهر همچنان بالاست و دارن ایستادگی میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150715" target="_blank">📅 13:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150714">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سردار نقدی: حمله مجدد آمریکا به معنای خودکشی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150714" target="_blank">📅 13:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150713">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDI-44meyEZLBjhzb4CheeUQPgPCmY0Gp5bRdXo9gIWB-YKEE48cRzAR6BJCt18GmNFLTBgnkXwzO6gvNAsi67fBzqG44KaujGAM-Yb579PV3Aos2VgiNBIFQ3gzo3Cb4w9X2tTdIX20-aDFWbgSR_e03dLZDz8TYmrMZS1PxOeClgxOfg8k9-UrQu-ExscfKjexqKFoSbzUonEqvazyxFILEQyQYV5TC6fXaWBFEyGMG0C04ZuslqsuRFhQtHHDfVb4cxzybJ2CNo1pFWLCuaC7gHbcShAXeU-VQruN5MVFJq7JVbcHy1dEJJgdIIwEfpD4ZSPTV0c04akywbeu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طعنه فرزند پزشکیان به مجتبی خامنه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150713" target="_blank">📅 13:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150712">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7bGplGHddHps_70xu2r9xSNIY5qlOSoSgik55xbg9qeRyiTyJuam1wFc-yTg31JhzYpoMtOPHBGxSf_Enqb722Z-L8m0E8qvtIFFzg8_sY8IeuZS66OTSvCWHKx6qWRkjaUfnfi9gErc6_7VK7_5Y3ahtrfM4r8VdSp9Io8w1twcMobXZFOeI3DFetxIRK49ppZ-boHGJZ5yFrByrIWhHWI8OT12PC9hdAqseOIaVon5e59mjmgFQl0UStSO8uiNj4IQH1yJSuJI9bH4DTQ2Juyi9htpU_z7G4dNgCOl4Xus82aqHna0Q4yD24GRiCGgdnS7rwC8sNkwLVOUo3emg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای حوثی به شهر عدینه در کوه حبشی، غرب شهر تعز، رسیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150712" target="_blank">📅 13:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150711">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
دیلی میل: بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره بریتانیا گفت: «فکر می‌کنم اگر بریتانیا کنترل مرزهای خود را دوباره به دست نیاورد، بریتانیا را از دست خواهید داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150711" target="_blank">📅 13:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150710">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fe16c54f.mp4?token=Y8kDOM7oAzUszJaH9K6zm6Ze8SiS_veqQv95QjjD2f07qsCRVtJ2Mf_XEt0ZxO4asW1SvT3fNjmUqlYoZouRNh88y7cht0AVo1stFC6KvVcnuImVtZDAX0AsVHmGkObE1hnTvOMxEs8qoeEn5rowXY2gU4P5qjvoGKhqq0yABubmNUUVu_UA0Z3uKWwv4zLoShbNuYEEf_IyEICcV_ZdIccVnBzYeOpNzz2C2yV-MbuAqtmhhncWU8t91is-B0EKYSDfMJySK6ObNymQuJAW0UH5fcMV292cOxWbJZH5rEi78OsUbKPkW6CCq4SyxLjippkk3Pdzmx3Fy4R-U3p0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fe16c54f.mp4?token=Y8kDOM7oAzUszJaH9K6zm6Ze8SiS_veqQv95QjjD2f07qsCRVtJ2Mf_XEt0ZxO4asW1SvT3fNjmUqlYoZouRNh88y7cht0AVo1stFC6KvVcnuImVtZDAX0AsVHmGkObE1hnTvOMxEs8qoeEn5rowXY2gU4P5qjvoGKhqq0yABubmNUUVu_UA0Z3uKWwv4zLoShbNuYEEf_IyEICcV_ZdIccVnBzYeOpNzz2C2yV-MbuAqtmhhncWU8t91is-B0EKYSDfMJySK6ObNymQuJAW0UH5fcMV292cOxWbJZH5rEi78OsUbKPkW6CCq4SyxLjippkk3Pdzmx3Fy4R-U3p0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل: «اسلام‌گرایان و چپ‌گرایان باید به‌طور طبیعی در مقابل یکدیگر قرار داشته باشند.
🔴
اسلام‌گرایان همجنس‌گرایان را اعدام می‌کنند و زنان را از هرگونه حقوقی محروم می‌کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150710" target="_blank">📅 13:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏
👈
تیراندازی در مقابل دادگستری مهاباد  ‏
🔴
خبرگزاری صدا و سیما: دقایقی پیش حادثه تیراندازی در مقابل ساختمان دادگستری شهرستان مهاباد رخ داد؛ حادثه‌ای که در پی بروز مشاجره لفظی میان چند زن، با ورود مردی مسلح به سلاح کمری و شلیک گلوله همراه شد  ‏
🔴
در جریان این…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/150709" target="_blank">📅 12:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150707">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfbcca65f4.mp4?token=PdMMj6lC7-s9rouAvveWH5l_XlFnCLiZL5ktnPqyEHQxpvd2NXbrjn82ebHfqCL2DQpIaHnElrXREUMQDO0MHaEx9vqe7OYECRN9K7QzCiPAlVSVgfyoyw5zdkMxpuKEnXCj_sY65UGipwGQ7HA6Ix-pSmvRmtBetBu4tgoaNNMoHrhYeDHcTvvUaH63uHGrOR_bKSKz4qCdfCZNTOf9vO6M7DFUoeD3UIG3WD69x3bNAbtTYRwt2GBBx_x6Bj06mjLdfKpOQmLHg96squ--4iQ7SnyC4HtBo-IfAzV1BAp5UzFIuD5kTFzPTc-vy2L5Mnqzp8VUQyvMbrDhmANoGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfbcca65f4.mp4?token=PdMMj6lC7-s9rouAvveWH5l_XlFnCLiZL5ktnPqyEHQxpvd2NXbrjn82ebHfqCL2DQpIaHnElrXREUMQDO0MHaEx9vqe7OYECRN9K7QzCiPAlVSVgfyoyw5zdkMxpuKEnXCj_sY65UGipwGQ7HA6Ix-pSmvRmtBetBu4tgoaNNMoHrhYeDHcTvvUaH63uHGrOR_bKSKz4qCdfCZNTOf9vO6M7DFUoeD3UIG3WD69x3bNAbtTYRwt2GBBx_x6Bj06mjLdfKpOQmLHg96squ--4iQ7SnyC4HtBo-IfAzV1BAp5UzFIuD5kTFzPTc-vy2L5Mnqzp8VUQyvMbrDhmANoGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی‌ها در شرکت نفتی آرامکو
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150707" target="_blank">📅 12:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150706">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">روی دلار ۲۳۴ هزار گفتم بخرید میتونه تا ۲۹۰ هزار بره و فک نمیکردم اینقد سریع تو دو هفته اینکارو بکنه تا ۲۹۰ هزار فعلا هیچی سرراهش نیست و میتونه بره  روزی داره ۵ هزار گرون میشه  اپدیتشو میذارم براتون امروز
❤️
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150706" target="_blank">📅 12:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150705">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
استاندار تهران: در جریان جنگ اخیر، حدود ۴۵ درصد عملیات‌های اسرائیل و آمریکا متوجه استان تهران بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150705" target="_blank">📅 12:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150704">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
دیشب در کمپ دیوید، ترامپ و کابینش جلسه محرمانه‌ای داشتن و آکسیوس گزارش میده که دست‌کم تصمیماتی گرفته شده.
🔴
موضوع مورد بحث این جلسه، ایران و یمن بوده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150704" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150703">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abPPaXyeNGgGcDsaqGmr2aMlbW5NvNTwnQ2Qc7UXzaNWkkYcTw5LVmaw9KJ8bv_VoYSkkebwK6wD_chuHIr5d98gbA9oFntc6IiGxzgY3_mlLgszh1a8JqnhS_-Ip2aHOLWuXJJXVKN3uguzi6z-GJ0seyq7VRv04OxW32ii92s6qI-T4kcqSqKFE8yDqa_CrFW1hYHZZp4KD_p9Dcai1ULpSZ3kFHEUX92WPnJ4ibIURuT8QoYBn9Rp0WSod3L-xiW3MYqOo_FmyKX6DWy0vT8P7EuG4WdOjZYF1Hj8rsLEbW93V0d8jxXgKFjxc3HkqisUPJEbafCVDsijWqx4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از پارک جنگلی چیتگر در سال ۱۳۷۸ و ۱۴۰۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150703" target="_blank">📅 12:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffde0cb90c.mp4?token=nTgJUIRUMFkQT7MHBeiFV_Qn8X_EK12OeOfZb9gtUM5sOHnrULbFNyHJy2Pe1LVhxib852Smig7b5vnH2-leWtS7PQJmLQ6cv1E_EZfhk4dEiMvc_cb5TNF662C3nSFLMFHOuZucoWshUI7kwhVmeizLunhI637kKFA4UClVnYxpZYk_zwf5C7Ip4q6DDGYhr0wxT3WmSo9wNHLYUF1NJzlveliYPx1-AzXv0sbwlqTkpiQ30mUDM1cgq6dKFV7lBrCYP4T8V0gJd952Lmqo9CFETVUG24Oselg8wwbm9Srf5D_VxQzD6R4Cq2YG8BQnd9PEJdaY-Ut8Yt6_8CGu5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffde0cb90c.mp4?token=nTgJUIRUMFkQT7MHBeiFV_Qn8X_EK12OeOfZb9gtUM5sOHnrULbFNyHJy2Pe1LVhxib852Smig7b5vnH2-leWtS7PQJmLQ6cv1E_EZfhk4dEiMvc_cb5TNF662C3nSFLMFHOuZucoWshUI7kwhVmeizLunhI637kKFA4UClVnYxpZYk_zwf5C7Ip4q6DDGYhr0wxT3WmSo9wNHLYUF1NJzlveliYPx1-AzXv0sbwlqTkpiQ30mUDM1cgq6dKFV7lBrCYP4T8V0gJd952Lmqo9CFETVUG24Oselg8wwbm9Srf5D_VxQzD6R4Cq2YG8BQnd9PEJdaY-Ut8Yt6_8CGu5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ریاض عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150702" target="_blank">📅 12:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150698">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4829d2be.mp4?token=KeKvu4HtVRoZAXCXh1j6m3uIKSK2qAjEPiz3vcxvFKgDLW4avc5clnVfFpLAO6SPsTgYItAAjUe-j47SxJKCbHKo6Oi9VRzHQg_i6BvmBZ3vJijglSV3wjdY3DnL4Zb3L6zQWnhflg6gYIBxfKMdywgzc6gs1M68801YROj8B1Q6uMw3b5wdgqtQ7b87i6z_iSrh--SB7Cpa2zuRHQVgSYVUQBLf-WhJ_WnP9dg2xIsxj1cLHE0ERaStOwkpWLVNxOBGf6DoLEyespOEo63NZFeKfyIGCctN41sl4lA7ylJhzwjz4lQQBCKJGyJ6-dTIfO62ZyquFiB0pYMjkzyjWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4829d2be.mp4?token=KeKvu4HtVRoZAXCXh1j6m3uIKSK2qAjEPiz3vcxvFKgDLW4avc5clnVfFpLAO6SPsTgYItAAjUe-j47SxJKCbHKo6Oi9VRzHQg_i6BvmBZ3vJijglSV3wjdY3DnL4Zb3L6zQWnhflg6gYIBxfKMdywgzc6gs1M68801YROj8B1Q6uMw3b5wdgqtQ7b87i6z_iSrh--SB7Cpa2zuRHQVgSYVUQBLf-WhJ_WnP9dg2xIsxj1cLHE0ERaStOwkpWLVNxOBGf6DoLEyespOEo63NZFeKfyIGCctN41sl4lA7ylJhzwjz4lQQBCKJGyJ6-dTIfO62ZyquFiB0pYMjkzyjWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات دانش‌آموزان در فرانسه:
🔴
۶۲۵ نفر بازداشت شده‌اند
🔴
۸۳ مأمور پلیس مورد حمله قرار گرفته‌اند
🔴
۳۲ معلم زخمی شده‌اند
🔴
صدها مدرسه به آتش کشیده شده‌اند
🔴
خودروها و کلیساها به آتش کشیده شده‌اند
🔴
دانشجویان آفریقای شمالی‌تبار و دانشجویان چپ افراطی علیه دولت فرانسه اعلام جنگ کرده‌اند
🔴
تا کنون کسی کشته نشده !
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150698" target="_blank">📅 12:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUwOlkdWzRAnxKt9-cEJnsw9nPdW0PDJYj_0gfd6k0j6z-ccGq2s2peJAZlnwXa0lJXUdOzf-4bMrOrqs8ljyLzkZqVLQybuGn44hSP1aixeRwr3sENMKn-_rISqkB0M9pTao7KHLrZkbFd00uGJ5G2_Fmau6w_ioKIKjehIa9y6OncPf9a1UoxyaptC4ZRCY9qOrWIp9nMk-mIhDjXXpExdAGlypvyC6VCZ6utcjaB8fAz1y5GoewixnqHzrC2GIuiUxYF6SlWDavLRUWBoqqNiPgj83tmSuYxLV31TI80tng2whspcXTFhOx7FK_jSezPSIQg7aU2TGzzU3qilPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکم شهریور 1405 همین ۴۰ روز پیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150697" target="_blank">📅 12:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
هر  یک دلار 267,200 تومان شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150696" target="_blank">📅 12:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJqXQc6zQzuiu9zOZXePi3hpBAg8bVrLJ4c3CPG9yJaPejYEcS-3aIbzr76BNsx_ynwpuHDG_l97w10f4scpPJxKCRiz4XT1YD3F_N74nYzQBBHAA9XLxJUhYNN5aDLgoL_TgceaRP1eL8Oj7TtR895ezwHJ8Uue2kiLBFHACUPuspncCvmCRnzQmjBmVjtLuFXu_QPKYxtvutjgRpyGawB6CUHfUxG8gRDN4QtJCtBmzFBvs828Ck3Ec3XNfsebFV9r7nFJPn3pbDk6BpiIwi24DIIZtCNRLx8xyDadEGZd1oGbw-6NvFDeNBHwcfn5U7dvs6A2zg8eFuXf8xIVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری وایرال شده از رژه جان فداها در اصفهان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150695" target="_blank">📅 12:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
تعویق رأی‌گیری سنا درباره توافق هسته‌ای ترامپ و عربستان
🔴
سناتورهای آمریکایی اعلام کردند رأی‌گیری درباره توافق‌نامه همکاری هسته‌ای غیرنظامی دولت دونالد ترامپ با عربستان سعودی، پس از برگزاری انتخابات میان‌دوره‌ای و حداکثر تا ۱۳ دسامبر انجام خواهد شد.
🔴
این تصمیم در پی ابراز نگرانی برخی نمایندگان- به‌ویژه دموکرات‌ها- درباره خطرات اشاعه سلاح‌های هسته‌ای و احتمال شکل‌گیری مسابقه تسلیحاتی در خاورمیانه اتخاذ شده است.
🔴
این رأی‌گیری به کنگره اجازه می‌دهد تا پیامدهای انتقال فناوری‌های هسته‌ای آمریکا به عربستان را بررسی کرده و موضع رسمی خود را اعلام کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150694" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150693">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
👈
تیراندازی در مقابل دادگستری مهاباد
‏
🔴
خبرگزاری صدا و سیما: دقایقی پیش حادثه تیراندازی در مقابل ساختمان دادگستری شهرستان مهاباد رخ داد؛ حادثه‌ای که در پی بروز مشاجره لفظی میان چند زن، با ورود مردی مسلح به سلاح کمری و شلیک گلوله همراه شد
‏
🔴
در جریان این درگیری لفظی، مردی که یک قبضه سلاح کمری در دست داشت، به سمت زنان نزدیک شد و اقدام به تیراندازی کرد. جزئیات دقیق چگونگی وقوع حادثه و ابعاد آن تاکنون مشخص نشده است
‏
🔴
اطلاعاتی درباره شمار مصدومان یا تلفات احتمالی، وضعیت جسمانی افراد حاضر در صحنه و همچنین هویت فرد تیرانداز منتشر نشده است. همچنین علت اصلی مشاجره و انگیزه احتمالی تیراندازی همچنان در هاله‌ای از ابهام قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150693" target="_blank">📅 11:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150692">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b5ad2c555e.mp4?token=lRuzpqAWDPlUl8h3Rbwe2xoTi41sX8uPEnCGHIHNRMA7-OX-ZeJqgssBSwzjxoxro-5_OlrGuZ0QzL7P2jQOMeJ8tTRyxfUDuGekFbLtpPDji5-EJ6GkKZPNswPKtkKYWw3TlC28bkmm_-S1KwVqBqlvezGAPq3SyMFDvevxSfJpdGxbd25SUwiToTKqDFkhuaqG0Z1tvecVHzqPwuRp2V2LfrCSdeLlBv-Lur026Gg7AETRbOvpsirV73D4byhsz0hoFMSSdqqW_m0aYi2h-6udSzPur0bhSPhDIurzg0N7Iy6A5RQ94eaQd1oiGcfx3nB_3WXoPKj-PaKxGVu8LB7oM9ipSmaLqL1VYVk_ZBRVMdAj3STZPRhRDGqSJFS0n3l802Q7NLlUlnzAwJBO99IvgNnZZht5FH96p-wn2z1VJIw4xwLfuTBPhV4sqd0m2sXuCKSqYNbzZPWQeZ7g9UyQVcDIwTsQLNCo3vCA-FOJ6VrURLEPyqn0rx2axZ3jFHiz_fKRKpEjXgPiwR-3AfgWisr-AE4pBcqi6UWzS7yCaGDdjysWroEm9l8GGXIVYscKMCZbosr-ftvRKlgy9U2_rV5NPj2p-AvHGX3m4rnWkZQ66TdeXH5enMUeimjisMIOVTnY__Xs4JUo9e4WxDKN3Xxfj9EZUikyqE77K-c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b5ad2c555e.mp4?token=lRuzpqAWDPlUl8h3Rbwe2xoTi41sX8uPEnCGHIHNRMA7-OX-ZeJqgssBSwzjxoxro-5_OlrGuZ0QzL7P2jQOMeJ8tTRyxfUDuGekFbLtpPDji5-EJ6GkKZPNswPKtkKYWw3TlC28bkmm_-S1KwVqBqlvezGAPq3SyMFDvevxSfJpdGxbd25SUwiToTKqDFkhuaqG0Z1tvecVHzqPwuRp2V2LfrCSdeLlBv-Lur026Gg7AETRbOvpsirV73D4byhsz0hoFMSSdqqW_m0aYi2h-6udSzPur0bhSPhDIurzg0N7Iy6A5RQ94eaQd1oiGcfx3nB_3WXoPKj-PaKxGVu8LB7oM9ipSmaLqL1VYVk_ZBRVMdAj3STZPRhRDGqSJFS0n3l802Q7NLlUlnzAwJBO99IvgNnZZht5FH96p-wn2z1VJIw4xwLfuTBPhV4sqd0m2sXuCKSqYNbzZPWQeZ7g9UyQVcDIwTsQLNCo3vCA-FOJ6VrURLEPyqn0rx2axZ3jFHiz_fKRKpEjXgPiwR-3AfgWisr-AE4pBcqi6UWzS7yCaGDdjysWroEm9l8GGXIVYscKMCZbosr-ftvRKlgy9U2_rV5NPj2p-AvHGX3m4rnWkZQ66TdeXH5enMUeimjisMIOVTnY__Xs4JUo9e4WxDKN3Xxfj9EZUikyqE77K-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، می‌گوید قیمت بالای نفت هزینه کوچکی در ازای هسته‌ای‌زدایی ایران است
🔴
«۴۰ درصد. اما درباره نفت یادتان باشد، شما دارید هزینه‌ای می‌پردازید، اما این هزینه بسیار ناچیزی در مقایسه با چیزی است که اگر این افراد به یک سلاح هسته‌ای دست پیدا می‌کردند و از آن علیه موبیل، آلاباما استفاده می‌کردند، باید می‌پرداختید.
🔴
خب، چنین چیزی اتفاق نخواهد افتاد. و ما حمایت فوق‌العاده‌ای داشته‌ایم؛ واقعاً حمایت بسیار خوبی داشته‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150692" target="_blank">📅 11:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150691">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رئیس سازمان سنجش : نتایج کارشناسی ارشد اواخر مهر اعلام می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150691" target="_blank">📅 11:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150690">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3de2fd69.mp4?token=eytkRHf5jVkvvNgipZyy56X20PKwXpJU-FUkKFt9NtBvA0KaMRxqwvBSpCwXvyl1o0aLPGq3Uc8_3hERmYkbl4hgmqx-bkbNg66sHB69o8gJ7jmQvmTvpY1XGNfXWzimHcH257-IFx00HoSCZQDzF8pJeLD6tUVxgQGlSQWJmhsJUlnBxL1uQRVZeptxQv88qeavM-FFDbujvx3HgdwUAo8Vlt8hgjjFCdv86OEe7mp1VQ6AdMsXFTpeUHrDWNd7ZW73x1lfPVq2ywOfIQA9wbDF58tTsoaJfiOhuZGRMdZuc3HZgGlsIJXXLGfi-Y3ytzY9w_KW2sXdw4_sLeL3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3de2fd69.mp4?token=eytkRHf5jVkvvNgipZyy56X20PKwXpJU-FUkKFt9NtBvA0KaMRxqwvBSpCwXvyl1o0aLPGq3Uc8_3hERmYkbl4hgmqx-bkbNg66sHB69o8gJ7jmQvmTvpY1XGNfXWzimHcH257-IFx00HoSCZQDzF8pJeLD6tUVxgQGlSQWJmhsJUlnBxL1uQRVZeptxQv88qeavM-FFDbujvx3HgdwUAo8Vlt8hgjjFCdv86OEe7mp1VQ6AdMsXFTpeUHrDWNd7ZW73x1lfPVq2ywOfIQA9wbDF58tTsoaJfiOhuZGRMdZuc3HZgGlsIJXXLGfi-Y3ytzY9w_KW2sXdw4_sLeL3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر جدید از تداوم آتش سوزی در پالایشگاه آرامکوی ریاض درپی هدف قرار گرفتن با موشک‌های یمنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150690" target="_blank">📅 11:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150689">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مجری صدا سیما: اگه به رهنمودهای آیت الله العظمی امام حاج سید مجتبی خامنه‌ای دامه برکاته گوش بدیم مشکلات حل میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150689" target="_blank">📅 11:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
هم اکنون ،شلیک چندین موشک از صنعا،یمن
✅
@AloNewd</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150688" target="_blank">📅 11:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
دادستان کل امارات: کمک خلبان پرواز فلای دبی قصد انجام اقدام تروریستی را داشت
🔴
دادستان کل امارات: تحقیقات پیرامون حادثه پرواز فلای ‌دبی نشان داد که کمک ‌خلبان قصد انجام یک عملیات تروریستی را داشته است.
🔴
طبق نتیجه تحقیقات کمک‌ خلبان هواپیمای فلای ‌دبی در حین پرواز شروع به اجرای نقشه خود کرد و با استفاده از تبر اضطراری به خلبان در داخل کابین حمله کرد. تحقیقات برای روشن شدن تمامی ابعاد و جزئیات حادثه فلای ‌دبی ادامه دارد.
🔴
پیش از این مقامات ارشد اطلاعاتی و انتظامی اعلام کردند کمک‌خلبان هواپیمای فلای‌دبی که متهم است روز چهارشنبه به کاپیتان حمله کرده و قصد داشته پروازی به مقصد اسرائیل را ساقط کند، تبعه عمان است؛ فردی که پیش‌تر به دلیل شناسایی به عنوان یک تهدید امنیتی، از سوی شرکت «عمان‌ایر» از پرواز تعلیق شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150687" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150686">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd1ac59b80.mp4?token=LS2GItuNcGOca2Clqi1-RbG1QqYuvIW6YI6R8XBb3cnx2kYb2WDIO6FqcZbgDFGZQO3DLLuzAPQ2_74pkbFGwjLxFwWy6_JuJuLhykAwpp8BBkxq5B1AAo5zWcsI4d9zbm51Cwa2Qv5rAkH1_AjnKjjRWvXkOOMgZ-Rx-GwjxKAX-LdfvBm7oFgMKWV7pZCFiQjbhg9EsxNkKMZY4b3z9RZr_63QwG4aXmxgHFufrs6rVWcc5cCyTk3qjHDGca_M5zs_j66RtN44c9NsjLFTAQQy1lJ3jDkrPZonkDcNrIAKmX0KqGQrjniU9FakhCcx_ZVtOCeZZXFP-XETqumF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd1ac59b80.mp4?token=LS2GItuNcGOca2Clqi1-RbG1QqYuvIW6YI6R8XBb3cnx2kYb2WDIO6FqcZbgDFGZQO3DLLuzAPQ2_74pkbFGwjLxFwWy6_JuJuLhykAwpp8BBkxq5B1AAo5zWcsI4d9zbm51Cwa2Qv5rAkH1_AjnKjjRWvXkOOMgZ-Rx-GwjxKAX-LdfvBm7oFgMKWV7pZCFiQjbhg9EsxNkKMZY4b3z9RZr_63QwG4aXmxgHFufrs6rVWcc5cCyTk3qjHDGca_M5zs_j66RtN44c9NsjLFTAQQy1lJ3jDkrPZonkDcNrIAKmX0KqGQrjniU9FakhCcx_ZVtOCeZZXFP-XETqumF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسایی چندسال قبل: زندان اوین هتله
🔴
هتل خوش بگذره
❤️
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150686" target="_blank">📅 11:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150685">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKI9O3iWF_iG_zChz2xNZgJLS7WAU8Qotqb0r7kKoHec_3nrYLExrW_g1maHWtIcxGW8d_wltD1CZ8HjLGbz2eOZdMv72M9BmAfmAot1_fBgKu4pET4qgXkGCKncs_nM3uOR2f8xivw9a7CAjDtDYOA6PBzZ6P2Dj851ulLxBWk60xK0NqQtbfeIbABMucNg8VNhva8jmceIfyAardRiykoJGHqvz9pPadt-q-MqSOXzFUQ0tyPcP5_w3n2ZDfr2mPdEYdDtiSCJ9zn6P24lkv6RMo4UmZLIJQT-igGo8eqazz1Xln6vBdcMVYdyIzCGYPgjoJrMGTeKCVTm97kUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخستین تصویر از کمک‌خلبان فلای‌دبی پس از مهار او منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/150685" target="_blank">📅 11:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150683">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G__61qWSFx5kgs6kZmGe0N1FJ-14HRSFpWzqF4QbHvQ__AlMZBLfrp85_tNmUC1UF8GNETELMdxmaqTpb8u6e5uiYFcLVKUPbQ07f775wL49JmPsgdDKznNQjboLfgLHeAWF8a3JE-w-tuvxS1ieGYfrEMbMM01jAxuNoC5tJj_ChuoYFNVv0UJDqqUsTRuBA5-5CBrRBi9ihRbU8XgU96o7UVINeBDFh5s5UqE9DnaNVnZ7AqbhVIafY9oGAA3GkfKCRINjj8t0MtURXwKXHGg1XSYedrwHAbjEbei-SapmTdu9pHiunIknm0mcszS822Dj3cVWQ_qpbA1puQu19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdXA5ye3kY6L62jitSP28w4oKiqXvTAUe7mfcRzyN7JhrAbYoMKRm2YA17O7tAywRFJSZAdc8nkSbDcccj21WMyP1xKD3YRijpx5rae75gyGbMQZnetM1BCyWA_76oSU9t7dKYkbx36OrginopOkiUWpHc8SBcRH7jsnEQultled2-2cjWp04bFi2KQrGCkCPZlWExba9WRK868ZcnYh6ayWoW0RSpDfnXtKQCB9prgGG0tdGIVYuHg_ylcrA4mbD3t3TBye9wvpYgcCYo943HDCQV2R33W4MMyMhxgHXowFDTTJaXlCDw-QPWRN2U-46d6UMahFAmn-UKx4OoNxqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اسامی نفرات برتر آزمون سراسری اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150683" target="_blank">📅 11:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150682">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/معین خواننده مطرح اعلام کرد بزودی به ایران بازخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150682" target="_blank">📅 10:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150681">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
توقف پروازها در فرودگاه ملک خالد ریاض همزمان با انفجار در عسیر عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/150681" target="_blank">📅 10:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150680">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
طلاگرمی 26,012,881
🔴
تتر[USDT] 265,300
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150680" target="_blank">📅 10:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150679">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhbcGLwOndj1vikgQLbMkFbIt1SL-P_gCDFEWofPiyHFfFOav2MrF5bREd9jDjTuMZ9Z9YcgNNpC7MVRYWldmkuuTPtloKZcAJzD_BfFymz7Bu8pIDT_2HQAxKSNHGlY6XFlM_7VlG5QzkBtsmMsaAQx9T7JisEs9-2zC3wVnblORcNcC9foHaShxiLTkjfYcwyv1Vw0b8ciG7_1kaY5cdU8QSkKw4fL9v3tXK8Rdc28Ov1_xSpX7zEVv5Tk_2HkgSjTEiJvrisRcWi3AEpCF2pxlLprhiCQSrK8hf2CNBOrLi4lkxRfHIkbePQqLXyKH7bLxEzef2T2ONRYgzBWHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آمریکایی: ترامپ بعد از انتخابات به ایران حمله زمینی میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150679" target="_blank">📅 10:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150678">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbsOF4c8tTK64_pjcVqItKIq7eeZRMRY5wmcEciEqkuVS86WeCLQRChYTpSVR1WHZBWVYrQJlgN9siAsheR5jTUBqLBB6P63JOkf0vWDKc6jxPQp4K12v50It6mkOk7lg3r4Yeu-PaAsgVSMxDmvnTKsoUpZmfZV_Xx68TT7QgsnmORMHN0FYh_FdpuyIfmQ_rpJsb-dLilGZ9kC0xMu7STXM9ZcmzB8VT_Ma59uICTzGQ-Ly6eSPSayX92LetwGkt3sos9Ojv-tbFFiupInsopkK4-iDNLp7IberEe-xTDg3RCc_Kh3iDIfKryDmTAgauNu2xh8hYuGiZf-UxbJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقائی بدون اینکه خندش بگیره خشونت پلیس فرانسه علیه معترضان رو محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150678" target="_blank">📅 10:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150676">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S2lDqIEx9x488lzuyDCmK45eetb4eSBuyjKybyzzcxwBBtgw8d9_eNRSPgDwk4HnDGg1CiZk5XaA8u9ppw5y8LCD0wHZ2glfg-zh3b4VX_9uWPq9xX7IiVE8D2NHC-CTLsL2xvGBNIVI9Kd3cSwNOsSAKmBglE12_MJdjvWtSRcq_b6MHjbYLIfXHCribbMqD8Obgm5l0Zemol-4gfkqPdQzcEPA35xNg087B_YuSgRzXs_IOOIiH9esmB_9dQvZsi44jVmgPzBDnXrzMMugHpJP6GwKXoyfZUPd5Hzy0q3lQCRWtnaZbWT6h_KhCGUjOcIfi8UMuMSk0hPyJZYITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=AasXGMGmZR0yvtM_SPW8cW7HB1cYsS8_7y8W31aPOzK57HYrTe03Vo--OGKBVphKUWOqZmtmSGvfKGPvA4DSak-E9Rjsc0qKgUOeOmD11zX7X9vjuO7KsXcMWjnB3BruoLiV21DpCRjKYWcZlSrTgiBrHyo8PhyfW50bXns4Wf8RdtkK4327VxfXdMKglksu2m31UShKtdXmqt1QmiPOEJJ9SXFWG4vvnUO49McjGcYkS6sTGBQb1AyFCbwEybNixHpt_xl6pXmdUPXlYqmhTpsCc5XjcbUULK5tLkBxsW6myLquMTOVevERhGJGnSZKCNhhPgW5v-wwahpQlM2FIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=AasXGMGmZR0yvtM_SPW8cW7HB1cYsS8_7y8W31aPOzK57HYrTe03Vo--OGKBVphKUWOqZmtmSGvfKGPvA4DSak-E9Rjsc0qKgUOeOmD11zX7X9vjuO7KsXcMWjnB3BruoLiV21DpCRjKYWcZlSrTgiBrHyo8PhyfW50bXns4Wf8RdtkK4327VxfXdMKglksu2m31UShKtdXmqt1QmiPOEJJ9SXFWG4vvnUO49McjGcYkS6sTGBQb1AyFCbwEybNixHpt_xl6pXmdUPXlYqmhTpsCc5XjcbUULK5tLkBxsW6myLquMTOVevERhGJGnSZKCNhhPgW5v-wwahpQlM2FIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی جنوبی ایالات متحده (SOUTHCOM) تصاویری از فعالیت شناورهای سطحی بدون سرنشین Saronic Corsair نیروی دریایی آمریکا در پایگاه دریایی گوانتانامو، کوبا منتشر کرده است.
🔴
همچنین SOUTHCOM اعلام کرده است که پایگاه دریایی گوانتانامو میزبان یک مرکز آموزشی برای شناورهای بدون سرنشین و خودمختار خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150676" target="_blank">📅 10:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f36095dc2.mp4?token=IBbtSfxlos_0F8umDT5yqtApKkws01gPjvLTK6lDV2f0PeO_kdKxPRetusd8H8EYf2Jo1A-m8Spy3VgcUfwRttw7wLn6KCgxKlP57f-I0e8VGNRqFcwALZzVhfomEonJ91gYbjCV8w2bcJptrm1mcOqLI68k6NjedDX3fdRhKO2wTCmyMqfeLWXI5sqMcnbd3GO5tz1zRf2okG319NysZyf-jAZ3LZv8ozntCZY-qUZQhDxylR8NOEXUcaMsDSImSjUgkbvibAjZEVILn5TQvXQqOR3zOchvBOQ7GJS8KiQkTjHN1WO-sEpPE776TnFEkqTB5QmHmNx3eZxRlNdjzixahCFgEZGI2ATaIhnblrjzVKUE-kQcs8wBM3q5T67WdiiaA1dYELPsmHg9BhkjxmCBLKOQgy2uGRm1m0a-ZBysfNTUfCFWVcDpDh3I5s5t34lQWfo-tkgUHFoN-VBlUtzwh_zxPEiBf8ChT35RmEOQkoqgKzvCn19Rx2ztqdagVM869rucUs9yRs_OLeESX8U4900h1ADA2KWOESk1DLO_EvxdNRRBaBy75DXT-T4MJW9q13WBVREZAUgP0dPTEJNB8SOwSv4CzfQIwcoPbncwzFwv89wDSXPnWToMUOR9fnMDz9nyD3FtVwmMo3E-xVDoW2zXXiQXwThz_ZxmAiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f36095dc2.mp4?token=IBbtSfxlos_0F8umDT5yqtApKkws01gPjvLTK6lDV2f0PeO_kdKxPRetusd8H8EYf2Jo1A-m8Spy3VgcUfwRttw7wLn6KCgxKlP57f-I0e8VGNRqFcwALZzVhfomEonJ91gYbjCV8w2bcJptrm1mcOqLI68k6NjedDX3fdRhKO2wTCmyMqfeLWXI5sqMcnbd3GO5tz1zRf2okG319NysZyf-jAZ3LZv8ozntCZY-qUZQhDxylR8NOEXUcaMsDSImSjUgkbvibAjZEVILn5TQvXQqOR3zOchvBOQ7GJS8KiQkTjHN1WO-sEpPE776TnFEkqTB5QmHmNx3eZxRlNdjzixahCFgEZGI2ATaIhnblrjzVKUE-kQcs8wBM3q5T67WdiiaA1dYELPsmHg9BhkjxmCBLKOQgy2uGRm1m0a-ZBysfNTUfCFWVcDpDh3I5s5t34lQWfo-tkgUHFoN-VBlUtzwh_zxPEiBf8ChT35RmEOQkoqgKzvCn19Rx2ztqdagVM869rucUs9yRs_OLeESX8U4900h1ADA2KWOESk1DLO_EvxdNRRBaBy75DXT-T4MJW9q13WBVREZAUgP0dPTEJNB8SOwSv4CzfQIwcoPbncwzFwv89wDSXPnWToMUOR9fnMDz9nyD3FtVwmMo3E-xVDoW2zXXiQXwThz_ZxmAiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات تو فرانسه  همینجور داره بیشتر و وسیع‌تر میشه؛ از درگیری با لباس‌ شخصی‌ها و پلیس، تا حمله به ماشین پلیس تو روز روشن و حمله به یه لباس فروشی و غارت لباس‌هاش !
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150673" target="_blank">📅 10:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150672">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d3a8a0d8.mp4?token=o8e_2eQbpzbkoqwGiHFkYQzYSIi-NlcNslpbb91Xjr_8NM-ZDLeQE_onC7KiQsK8TuqSAFaWzj59V95eICvZEDSAIwzGdtYGjXCkC9dhE3xeJcawbBBXUhVGiyuSyVmj4qOjSd3nnPgQKn01e5Cn67bmPfBkU3YfpMxHq4ck3Zh6qPjXCLqSW0Xs3AzibjrrxouUIaetygREMN61dWHE5MTvZf_domWLiS0d93HBfHIiDJn8pbxTKLiBnKxhFDlfK1BryEAB8geTfQ6jw1-L37RRBexWjHMSyu92eOFYIeExJSwaKaD-kcVEm8cF2FgN6bSgCQNw4K3L8ltfSNuRMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d3a8a0d8.mp4?token=o8e_2eQbpzbkoqwGiHFkYQzYSIi-NlcNslpbb91Xjr_8NM-ZDLeQE_onC7KiQsK8TuqSAFaWzj59V95eICvZEDSAIwzGdtYGjXCkC9dhE3xeJcawbBBXUhVGiyuSyVmj4qOjSd3nnPgQKn01e5Cn67bmPfBkU3YfpMxHq4ck3Zh6qPjXCLqSW0Xs3AzibjrrxouUIaetygREMN61dWHE5MTvZf_domWLiS0d93HBfHIiDJn8pbxTKLiBnKxhFDlfK1BryEAB8geTfQ6jw1-L37RRBexWjHMSyu92eOFYIeExJSwaKaD-kcVEm8cF2FgN6bSgCQNw4K3L8ltfSNuRMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود از پالایشگاه ریاض، متعلق به شرکت نفتی آرامکو، به هوا برخاسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/150672" target="_blank">📅 10:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150671">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb79ecbf18.mp4?token=V3xqsEsRXKc2t8drnMCxocnitEbcsi-oUT5BsF3YaRV8MXUZLFT3_jBax6nDBEdTAlK2juHZ2aVPEDG2ifmBoNC-2Tfj6SNx0VXeuZJEQnePNNJEOZWne3iBG9m8emuMpR2opq5LDgaWo8EfZX8h5_wA94yfMcgomZaBu-EKp6TOB3hCbw2E3ayf3Ey-85hCNVIwXfEHJK_iTT4PPELGCl9WP9i88xV7k7IFLMXTPXxBYPLPTZd13Dotpw0ek49PYK33MjDWDlOQXqqn_mxnU-bhhN21oc1DiNjPCOfAqUdhPlZmij-qOCoNF0028CmwEOf1VClguwC6f6lMW8c8hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb79ecbf18.mp4?token=V3xqsEsRXKc2t8drnMCxocnitEbcsi-oUT5BsF3YaRV8MXUZLFT3_jBax6nDBEdTAlK2juHZ2aVPEDG2ifmBoNC-2Tfj6SNx0VXeuZJEQnePNNJEOZWne3iBG9m8emuMpR2opq5LDgaWo8EfZX8h5_wA94yfMcgomZaBu-EKp6TOB3hCbw2E3ayf3Ey-85hCNVIwXfEHJK_iTT4PPELGCl9WP9i88xV7k7IFLMXTPXxBYPLPTZd13Dotpw0ek49PYK33MjDWDlOQXqqn_mxnU-bhhN21oc1DiNjPCOfAqUdhPlZmij-qOCoNF0028CmwEOf1VClguwC6f6lMW8c8hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: نمی‌دونیم با کی مذاکره کنیم
‏
🔴
کسی در ایران نیست که با او مذاکره کنیم. هیچ‌کس نمی‌خواهد رئیس باشد.
‏
🔴
می‌گویم: با چه کسی در ایران صحبت کنم؟ در می‌زنم: تق‌تق؟ هیچ‌کس خانه نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/150671" target="_blank">📅 10:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
گودرزی، هیات رئیسه مجلس : دشمن بدونه ملت ایران به کمال نترسیدن از مرگ رسیدن و هزینه جنگ رو کمتر از تسلیم میدونن و ما برای جنگ بعدی برگ‌های رو نشده داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/150670" target="_blank">📅 09:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
آکسیوس: ایران و آمریکا مدام حرف می‌زنند؛ اما حرف هم را نمی‌فهمند
🔴
باراک راوید در آکسیوس نوشت تهران و واشنگتن هر دو از ترجیح دیپلماسی می‌گویند، اما توافق از همیشه دورتر است؛ طی ۱۸ ماه گذشته دو دور مذاکره شکست خورده و هر دو بار به جنگ منتهی شده و تفاهم‌نامه ژوئن نیز تنها چند روز دوام آورده است.
🔴
به نوشته آکسیوس، مشکل فقط مفاد توافق نیست؛ ترامپ به‌دنبال توافقی سریع و قابل‌اجراست، در حالی که ایران مذاکره را فرایندی طولانی‌تر می‌بیند و خواهان تضمین و دریافت امتیاز پیش از اقدام است.
🔴
این گزارش «بی‌اعتمادی مطلق» را هسته اصلی بن‌بست می‌داند؛ تهران آمریکا را به حمله در میانه مذاکرات متهم می‌کند و واشنگتن نیز می‌گوید ایران پس از تفاهم ژوئن آن را نقض کرده است.
🔴
آکسیوس می‌نویسد اختلاف بر سر این است که چه کسی اول امتیاز بدهد و چه تضمینی برای پایبندی طرف مقابل وجود دارد؛ شکافی که هر دور دیپلماسی را دوباره به تهدید، تحریم و خطر جنگ می‌رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150669" target="_blank">📅 09:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeHKMrnouDKld76pE9Py6P3csDGzWwzqFEkUOOzB5ErPcyyrnCFE9eYw-NiMGn9OlOtZCeiQVMggsSHv2OlgbdXEX3dFY23jTKoXumwgflvwFcQHDGGtRGiQ6_JX6qRlergDQ09n4nKVoEZhJ-zkxwJ93dkdwy_0tAVgWQZxoBCAQSLsojPQ823ClXxFhi-bS8neARaYM5az7-nPJIHjqdqDMi3anWqGYFP4h2BVhvFRo6KmdkilGv46rMfL9cdLG4slhbRE7kUKponNALcb0VByshcSlxfw9ge6G9KvmHTrNOciSA0uPPcCxI5L1CBPxPt1WJgxB-ovjPxkusxp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخستین تصویر از کمک‌خلبان فلای‌دبی پس از مهار او منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/150668" target="_blank">📅 09:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
گزارش استیضاح وزیر کار به هیئت رئیسه مجلس رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/150667" target="_blank">📅 09:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150666">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f398c56e.mp4?token=LCOYSKKtpOPdA8eq7LW9orXoKW6JQLaTlqbWOCJp0ESljRuBxU29dZvpnn7DEg1LFtuS52wdvuzVJJRCOT2alAArXtWKydZNNWwVG1wMYD7yLPCJxWZHfyCntVnnQzZK2A-OmBHGcuntc1aK5icxa7L8f-dR3ISQ9U2VdwuAyXCXlFpBU27GyF2duqk5ucjdhibLGHXL-g02sXQ3E123MfQ0yrpyLAbkSudnVaAzucFNH3PtEZAt5-jUTVyTuCC1-a1IQ9qFj_0Khbx1P2Awuc-EFzigbYY3gP0kSZABNBkoT1v1kEIOmJWTn_tSa337y4kWDrECN6_freA2jp8RIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f398c56e.mp4?token=LCOYSKKtpOPdA8eq7LW9orXoKW6JQLaTlqbWOCJp0ESljRuBxU29dZvpnn7DEg1LFtuS52wdvuzVJJRCOT2alAArXtWKydZNNWwVG1wMYD7yLPCJxWZHfyCntVnnQzZK2A-OmBHGcuntc1aK5icxa7L8f-dR3ISQ9U2VdwuAyXCXlFpBU27GyF2duqk5ucjdhibLGHXL-g02sXQ3E123MfQ0yrpyLAbkSudnVaAzucFNH3PtEZAt5-jUTVyTuCC1-a1IQ9qFj_0Khbx1P2Awuc-EFzigbYY3gP0kSZABNBkoT1v1kEIOmJWTn_tSa337y4kWDrECN6_freA2jp8RIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا: «ایران برای ریاست‌جمهوری انتخابات دور دوم برگزار کرد، اما هیچ‌کس در آن شرکت نکرد. همه می‌گفتند: «من این را نمی‌خواهم.»»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/150666" target="_blank">📅 09:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150665">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d072f8ec59.mp4?token=NgjHItl_xn4pAbvruGHOp0hDy8TI0B9XT27btFC60brZD7SeP_UxJJNLtCULwVAGLmtmY19o56GlOj6lvvoIaCfehSD5pm5W6e1VV0q1mLgZFYfCUlkjU8D67GvzcKMJqJ-WoyuYITR4fGtzCAKUbnwayHpJfqYvzlY9LmH6u-j_ZtstYmcX_jKcX3RBVbaXkVsAp4DkNAx3h2cgVjZ_gT8Mro791DqdR39NIdxBs6RNP-cpEpycRQIxn_L38auOGcIrczxHL3uGyAiK0T0s5vM3CqjUF144yrEe2O7SpBONw-THNzPjzhOlmNbQrod0LbC655R-TXljupEAQEb4rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d072f8ec59.mp4?token=NgjHItl_xn4pAbvruGHOp0hDy8TI0B9XT27btFC60brZD7SeP_UxJJNLtCULwVAGLmtmY19o56GlOj6lvvoIaCfehSD5pm5W6e1VV0q1mLgZFYfCUlkjU8D67GvzcKMJqJ-WoyuYITR4fGtzCAKUbnwayHpJfqYvzlY9LmH6u-j_ZtstYmcX_jKcX3RBVbaXkVsAp4DkNAx3h2cgVjZ_gT8Mro791DqdR39NIdxBs6RNP-cpEpycRQIxn_L38auOGcIrczxHL3uGyAiK0T0s5vM3CqjUF144yrEe2O7SpBONw-THNzPjzhOlmNbQrod0LbC655R-TXljupEAQEb4rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: گروهی را دیدم به نام “همجنس‌گرایان حامی فلسطین”. خب بیایید یک روز آن‌ها را برای مذاکره به آنجا بفرستیم.
🔴
دیگر هرگز آن‌ها را نخواهید دید. آنجا کارهایی با آنها انجام می‌دهند که باورتان نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/150665" target="_blank">📅 09:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یک نفتکش حامل نفت خام در تاریخ ۲ اکتبر و در فاصله حدود ۴ مایل دریایی از سواحل عمان، هدف یک پرتابه ناشناس قرار گرفت
🔴
تمامی اعضای خدمه در سلامت هستند و تاکنون هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/150664" target="_blank">📅 09:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150663">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وال استریت ژورنال:
عمان در گذشته به دلیل نگرانی از پذیرش خلبان عمانیِ حادثه فلای‌دبی به ایدئولوژی‌های افراطی، به خلبان عمانی ممنوعیت پرواز داده بود، این در حالی است که طبق گفته منابع آگاه، شرکت فلای‌ دبی او را استخدام کرد و به او اجازه داد خط هوایی شرکت را به تل‌آویب اداره کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/150663" target="_blank">📅 07:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj5MI4qgPn8x0EKiaOs-aLjPsSXSi6Y8muGlUmLHhFzAAh-akuvVRp22uMQ6mBFHNWSwHPGS3pnY5C4MbJnnxx8l9gaepRV3yDCwmkBKGZw6PT2faBglNgv2k-yTjEmFhky9C96acWBrg024IELqQ6F78ank50gw-tW0WkLAp_CnTc_o76uFltbp-juY-GLlAZjGpqxasdgSH_E7yyebl6SA2QNH2HIrIb5Ws6iV2yPWnM_Le2jJktLCBCD_idTxX9hzwDQVMBQIyjYfEfGJfgSvn6agYoT6w7OHTyWuXN7Iahr3etfYCLE6-zzCbPKsQEpAlg3BeOU4cWpbbbAVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس بریتانیا
: دو فرد ایرانی به طرح‌ریزی برای اقدام تروریستی علیه جامعه یهودیان در منچستر متهم شدند.
🔴
سلام احمدیان، ۳۶ ساله
🔴
رحمان صالحی، ۳۴ ساله
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/150662" target="_blank">📅 07:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5-H-hd-QGtL_Nkrhm3dXzhzg554BBg6mgRaTbNkdmVXJmx_rKrNcH2ZWA5EBrQL7i75o7cvU4v5xwdPQ2fAFbnJaeHxBN3-v1_jLRwKBXGIuXfXjnRg8Xb3j3FQLkBwgX1UHMKUJXgAAIh6-eRit8G_pBnBOe2_bKo-_-X1BKd-g_RsSoLdm4zXCM_KNAT8eID8yLEe0ZNa5XbAthCyACCGGD4zwH7_PT-e8FExF2zvSkfkmTb0qv0TET3qSt4BJnKt0Aekz8OpYXK71R_Akw8_ShpGLMwaUBcpOx_IOdRLhS-kaWZVHwi44v46rGRwSLhcC4SR1F8jyAXy8cgVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
قیمتارو شکوندیم!
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
مولتی هوشمند
لیت
|
۳۰٪ تخفیف
۳۵+ لوکیشن • ۱۳۰+ لینک پرسرعت • IP ثابت
▶️
یوتوب
و
ساندکلاد
بدون تبلیغات
🔥
فیلیمو، فیلم‌نت و نماوا رایگان
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کد تخفیف
:
LIT200K
اول رایگان تست کن، بعد انتخاب کن.
🔥
ربات تست رایگان و کانفیگ:
@
litvpn_bot
❤️
ربات مخصوص
همکاران
:
@litpanel_bot
❤️
پشتیبانی
۲۴ ساعته:
@mahan_lit
.</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/150661" target="_blank">📅 01:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150660">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYeIrpsbhE-Dzj9eWU-qpJbAqof9S05SzVZ5uFBzFwTHHOyEPfreIgUlQzw60vjgkF872rZ3sDYbUMTHgxNfolA6ve04Ifhfns1vWHFyC_-djDVB8UjXPI8Z2PbDB-UScAG5md5XZ27bTMzxTcDyWs4p5RP9JQ5_QVK9fJ-9z-XMCgXGujBG9xQ43lFcouuciq-m0SPB9zAGlKIEmqbV9Nj-WOTPPz5AbCoKsz3tbIUmnG-gM_80sfMgRI-dVIIXGGncrsXwU_7jtASyPy-EMUOKLvpUXkhfMA3g9vee2egNecKA64q8bqWCTXzcwlYLny83T2AI2051VPqRKNqvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: رقابت سنگینی بین ایران و آمریکا سر ابرقدرتی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/150660" target="_blank">📅 01:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150659">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fh0enwkGteTRXqYNApPvrekoWGr8ivM-TpvYwYkHERRVKDi64J7RiOj6vPey7D6bCzDKxr5wnRX6RoLxIXbio5c-0zxLd2FOdwTFRRFpLfJbGU5lq0VxxADh3KvPtwNbHLjWiWjP1czE9mXbUaPjdljy5Qbv2J4CoTPW5FLAqld-aW1yGxgdbhOa02T_64k5M_8wixPSZEdSWaHtjndZPbupbxeVGJu27B7juKaK2l9UQbJscMRp1lNUazDCpL-32-endOMtRoSJ1UCAbRVqIZgQ_QgZXF74WJofhSkE5GdYnfC5C98bL3VCyzwr69fUcECoZ9tqz44LS9f-cLPtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایت رسمی استارلینک نحوه عملکرد استارلینک موبایل رو توضیح داده و گفته ماهواره‌ها بعنوان دکل عمل میکنن و هیچ نیازی به دکل زمینی یا تجهیزات اضافه نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/alonews/150659" target="_blank">📅 01:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150658">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nitXKnffdoNJTJdMpeBf1_2ZpH_RAGIncqX01vGWtOfvMBcxh-oKxFVmI8hSADwTMtu0h8au48ugA-TEwIGY-tEKb4-LK3Xz9lxgTF4TZkHkCqlDu6z6rd5VlakqhuI3EsOppShd2KCVUVMvukOopvdRtBEju3WBvSatIp_FkSOt611tBphjpck-YA-Fye4A2EsTsMRgU8bQWoSHezDSiyQlU0teTCbRe5tIHuNvC-g8Gn-rAT_6XvajKfStqkIGfaUuxwcerKrghpp8w-oQX54KcJ31GpapLol62-z1qPGB0kB5CUUdcjdgzgej8Z6-RS_ZgjCKfONnv__CzeOMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور فیلد مارشال: ‏آرایش‌ها و آمادگی‌ها برای رسیدن به لحظه تصمیم در حال انجام است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/150658" target="_blank">📅 00:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab0eda5713.mp4?token=jdR__FETobKRVnR4-XpyMaDdwxpCvGQEzfvjep939_lUm37XvjxfY4z6jzvXtEIO6LWoCJoRY-4cIRLYqC6dOJsZqVcidnqiEcrOVl3rqIykwdMpd9IG5KBBe9tAJgXl1_P6yY_OuBN8fA7eioE8smhijZvkMiI80AdtN4zSsD3uGaUIVUM9-ha1m0ENL4Fh2svmbKHNAHXQD0Ucsrmkpm2cGPKQUjBjv_axSFv557FYLGaBMu5QfBSmjDd8ARqy4dbryz5nTH4mtKDs2Y6tPU9ZmJ8ifur5pJ4TMqxSYhXXw9mGawETaRsh2R9W-sVDacDwMtDscDhwnsyjKrHxIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab0eda5713.mp4?token=jdR__FETobKRVnR4-XpyMaDdwxpCvGQEzfvjep939_lUm37XvjxfY4z6jzvXtEIO6LWoCJoRY-4cIRLYqC6dOJsZqVcidnqiEcrOVl3rqIykwdMpd9IG5KBBe9tAJgXl1_P6yY_OuBN8fA7eioE8smhijZvkMiI80AdtN4zSsD3uGaUIVUM9-ha1m0ENL4Fh2svmbKHNAHXQD0Ucsrmkpm2cGPKQUjBjv_axSFv557FYLGaBMu5QfBSmjDd8ARqy4dbryz5nTH4mtKDs2Y6tPU9ZmJ8ifur5pJ4TMqxSYhXXw9mGawETaRsh2R9W-sVDacDwMtDscDhwnsyjKrHxIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس تلویزیون:‌ حتی اگر بمب اتم بخوریم باز هم تسلیم نمیشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/150657" target="_blank">📅 00:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150656">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d0d925a5.mp4?token=ELHS3zv87jLwm9u61xACB1mPYOym8jcuhixZxiezjDLfqkX0SGTEEJiiVeDNyEdGTSe5jambkTVY5CJtTV3jvQ4-ylxfZfvFapTBvNNQ8OtdojqoprIIc-OPH1cJtUCg56d-NhbI0ndghMId1T6h8tTZsZ8PKEtkdoBY1_KhxuhSnXPWaYWCnOEvLV1WlHMUPZgPqSKU2QIIfLUHpiQR-qFZe8RJXywfO0XCat9Jhf1dXFNfgVmiJPZ_eQsKEJAPWBBwqdJAmqzNE0FaQmLu0U-HMsLel9MlFr7oAB_LY5w_Rzvkng5zM9t_X2w8on3K81MNQYxYhuru529KRNzMIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d0d925a5.mp4?token=ELHS3zv87jLwm9u61xACB1mPYOym8jcuhixZxiezjDLfqkX0SGTEEJiiVeDNyEdGTSe5jambkTVY5CJtTV3jvQ4-ylxfZfvFapTBvNNQ8OtdojqoprIIc-OPH1cJtUCg56d-NhbI0ndghMId1T6h8tTZsZ8PKEtkdoBY1_KhxuhSnXPWaYWCnOEvLV1WlHMUPZgPqSKU2QIIfLUHpiQR-qFZe8RJXywfO0XCat9Jhf1dXFNfgVmiJPZ_eQsKEJAPWBBwqdJAmqzNE0FaQmLu0U-HMsLel9MlFr7oAB_LY5w_Rzvkng5zM9t_X2w8on3K81MNQYxYhuru529KRNzMIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اینجوریمو نگاه نکنید من همرو دوست دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/150656" target="_blank">📅 00:27 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
