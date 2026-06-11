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
<img src="https://cdn4.telesco.pe/file/YPO5RjznOiyMGhISp0pVl4Edv01brtpJVfeHftxgiTe0kT8kFfxtsRmWLznrpyDLdSZwTbngc9HpnMzzPOpjt73f5rO_jhVrmrSQf4L9ZsUTnKLdV4PERYJdhfKaHJofvo7FKOyx4x-NdEpGZdV7sDUI0RToU3KQjgt4OnKSEZTxmDKes5Mu5uG8YP6KNk3K_M56_MBpw7A-e1CD4-6wQqQtArhCUC3fKPPp1r0RnYsg599nsTgE-zsxbFxJiNWlK8t3eFrfBX8mD9ROsTjby5gfK69Fdl5d4J_qvUk-H1E9snK8Ub2Ig3HZUHNDBIw5evxehtashM9vMR5kALTx9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 19:08:14</div>
<hr>

<div class="tg-post" id="msg-127175">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdd68900e.mp4?token=RpJL9s0c4vrPxpuCBARGabCd2r0FP5qGlijNGvDRiTTeOIDuntQVHDM8pR-Cyc2bsmyDxue_UfUzqfKaUx1wvfmClI6ni90f0kw_QrNrLDVub6c4IU3nQhbccP6J1oYfx--N2RM9ALq5heMDk8ogZjcbdm6skNVOHIYqR1xFbuHOftSODeW7SokMh4fJGrTGE1LxHC3wp3a4XIPImFhxhsEZzz1yO40HKL244V8krzp3T9b09CyChMfU0R7phrofgYGXSy_n3-3Qi-plkYrH1Dphlkz5qygVlNUsGku4uyMKWLY0UoRYLmm4uhhnqQGv5yNz_CDkg0m5NdWUYe-1fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdd68900e.mp4?token=RpJL9s0c4vrPxpuCBARGabCd2r0FP5qGlijNGvDRiTTeOIDuntQVHDM8pR-Cyc2bsmyDxue_UfUzqfKaUx1wvfmClI6ni90f0kw_QrNrLDVub6c4IU3nQhbccP6J1oYfx--N2RM9ALq5heMDk8ogZjcbdm6skNVOHIYqR1xFbuHOftSODeW7SokMh4fJGrTGE1LxHC3wp3a4XIPImFhxhsEZzz1yO40HKL244V8krzp3T9b09CyChMfU0R7phrofgYGXSy_n3-3Qi-plkYrH1Dphlkz5qygVlNUsGku4uyMKWLY0UoRYLmm4uhhnqQGv5yNz_CDkg0m5NdWUYe-1fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون ، طوفان و رعد و برق در تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/alonews/127175" target="_blank">📅 19:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127174">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
هلال احمر: امشب در آماده باش کامل هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/127174" target="_blank">📅 19:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127173">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
الحدث: ترکیه، مصر، پاکستان، عربستان سعودی و قطر قراره جلسه‌ای فوری برای جلوگیری از شعله‌ور شدن جنگ میان ایران و آمریکا و پیدا کردن راهی برای توافق بین این دو کشور، تشکیل بدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/127173" target="_blank">📅 19:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127172">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmf2G_3nVDSlJBYwf-Nh3hSyJwBp3_a_CohLhHfcfnaxYy6Uj-p1d16bxHecoY_owwCD4GUZKRWmv65Rwie48PaejxM2z7LnXBYsHGPY7j8CGaLw090eY7YMOD4iSLRf5wxNa2UCMwL-HEBVCrPv-Vc92gz4olG3quZdlTE0OATyWG8fPHMjABV6_nCZHn5YEZTPpAIpMrtGrE-0xbgscraSWv3JYlkme_EIc1nXwP3SQjodxWPvdJ-Wo64N-VqIXh59L_y8-joQxW9ZlgX11Rgb9jClG0t29ungYYWkQRNWJP_8waRlIblYk7FGAUHW6Zmds_phsv9K8JgjR_UdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/127172" target="_blank">📅 18:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127171">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری/ سی ان ان: پنتاگون در وضعیت قفل (لاک‌داون) قرار گرفته، یگان‌های مقابله با مواد خطرناک و بمب گذاری (هزمت) در محل حادثه حاضر شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/127171" target="_blank">📅 18:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127170">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
منابع الحدث: نشست قریب‌الوقوع کشورهای میانجی‌گر واشنگتن و تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/127170" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127169">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e13_gUsXieEI2g55PHJuylPMe-NN5OSbHuz_A56_4Iy7ZrPC7ZcsF9TgjybcKF_aacr4uZ4yGk857bMgqAIXHnMg52jFdZn9PDtSLsn9bAM142zl2a28qts6d3ODC8wApry9u295Nf95LPfLxtCDWJ-qWfIW54BSIKxx7X2-4SGcGoKsHNFq1CUTqnJH3IW7slh81Q4zi3P45m_5RqnvrBAs8HhL-Rlq8V92mBjN58DdS5N2EtQA1LL-GX7HhUiddGQ0ef6Od_fn1ztUEP3cAe3PXlkLeU-NUIMBvc4lQ4WLu-iSMaT67TsHwqqxlBSQcyUc18HnEEm8tuBJSYRzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌ داری آمریکا: هر آسیبی که به متحدان ما در خلیج فارس وارد کند، با وجوهی که از حساب‌ های ایرانی برداشت می‌شود، جبران خواهد شد!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/127169" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127167">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری/ سی ان ان: پنتاگون در وضعیت قفل (لاک‌داون) قرار گرفته، یگان‌های مقابله با مواد خطرناک و بمب گذاری (هزمت) در محل حادثه حاضر شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/127167" target="_blank">📅 18:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127166">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی در حمله‌ای جدید، شهرک «مجدل زون» واقع در شهرستان صور در جنوب لبنان را هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/127166" target="_blank">📅 18:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127165">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
منابع عراقی از اصابت دو پهپاد انتحاری شاهد ۱۳۶ به یک انبار گروه‌های تجزیه‌طلب در منطقه «قوش تپه» واقع در شمال اربیل خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/127165" target="_blank">📅 18:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127164">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGAPyN1MxuC-lHf57R9PqHSf8kWkt0d2IECY5lRUognL3Z2Yahom66B6mlLlC-9-dDItaPxcXk_XOFUgJaXepMdoYDmi1k3uHX-zG7EEzJrsfKwWuxjQV6SMh74UD59GFj1RNDpocsUyLU8bl4kFRG-0gAW8_dcns95SD8CRy0844RHiVRVsGA32H3sgjuCavuD9gBXNJZwnwT_O0Gs0ppQnJsTz1cdy_vj7bp18rrxWmrzj0OA-rwNk4WT-Y9OuDayA4Eg31X-Kr8gVAh4M9VFgvlpmXhJomNHvRQFwHKWNu-9mm62UY8lGUqIL7jfLOi63HOvZG10ZWx7ggd8zaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی عجیب در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/127164" target="_blank">📅 18:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127163">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پزشکیان: باید از وضعیت نه جنگ نه صلح خارج شویم اما مگر در خواب، تسلیم شدن ما را ببینند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/127163" target="_blank">📅 18:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127162">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بلومبرگ: امارات و ایران اولین دیدار امنیتی رو در رو در سطح بالا را از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران برگزار کرده‌اند.
🔴
این اقدام نشانه‌ای از حرکت به سمت کاهش تنش‌ها پس از ماه‌ها درگیری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/127162" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127161">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد از ابتدای ماه مارس گذشته، 30 نظامی اسرائیلی (افسر و نظامی) کشته شده‌اند و همچنین 1302 نفر نیز زخمی شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/127161" target="_blank">📅 18:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127160">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری / خبرگزاری فارس : ایران داره بررسی می‌کنه که دارایی‌ها و کسب‌وکارهای مرتبط با ایلان ماسک تو خاورمیانه؛
🔴
از جمله تجهیزات استارلینک و سرمایه‌گذاری‌های مرتبط با اسپیس‌ایکس، رو به فهرست اهداف نظامی خودش اضافه کنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/127160" target="_blank">📅 18:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127159">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارش CNN: ایران در حالی که ارتش این کشور در حال انتقال محموله‌های موشکی است، سامانه‌های پدافند هوایی خود را در جزیره خارک نوسازی کرده است.
🔴
ایران همچنین در امتداد خط ساحلی جزیره خارک مین‌گذاری انجام داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/127159" target="_blank">📅 17:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127158">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید تسلیم موشک‌های جمهوری اسلامی شود یا دیپلمات‌هایش...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/127158" target="_blank">📅 17:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127157">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سی‌ان‌ان: مقامات ارشد ترامپ تصرف جزیره خارگ را به عنوان گزینه «بازی نهایی» دیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/127157" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127156">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
آکسیوس: تهدید مجدد ترامپ به بمباران ایران با هدف اعمال فشار بر این کشور برای نشان دادن انعطاف‌پذیری بیشتر در مذاکرات بر سر برنامه هسته‌ای‌اش است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127156" target="_blank">📅 17:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127155">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
جوزف عون در مصاحبه با رویترز : آینده لبنان در دست مردم لبنان است، نه در دست ایران یا اسرائیل.
🔴
ما نمی‌پذیریم که ایران به ما دیکته کند چه کار کنیم. ما یک کشور مستقل هستیم و ایران حق ندارد از طرف ما صحبت کند.
🔴
ما نمی‌پذیریم که لبنان به عرصه جنگ دیگران تبدیل شود و مصمم هستیم که مسیر دیپلماتیک را دنبال کنیم؛ هیچ راه حل نظامی وجود ندارد.
🔴
ما چاره‌ای جز مذاکره برای پایان دادن به این درگیری نداریم، و اسرائیلی‌ها هم همینطور.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127155" target="_blank">📅 17:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127154">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHYSBYyWizFPg8wk2bTTcLUoNHPU0tKT5x2dbRC1RqyeBmADJcDnDIrbr7iFX5HEPL0SCxtKeozSx23eCIIGr_Gd5HgvY8FVuGeW4M1hXQ4X2kmX8DD4948aYCjBaE2rQukNS5GrukT3j4n7o78hteEbmdJcVo9OXWaW8wsK27UPuE0-8c0hfHu2btaZDraU-JteuXVK-TbPOK9fs_Z_CBw7lJGf02ZhhsWZwhs3fQsp2G9fC4OZVCcQgR7mcMR_ZvTNrnXgRBErDRRrUn9qJOs8hOtWBi5CG8P9kAlfstrDVsPd9ZJYTSv8yv0My0kK1pZ_Lp3wstW6crLxDMoelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران ماه‌هاست که برای یک عملیات احتمالی آمریکا با هدف کنترل جزیره خارگ آماده می‌شود، گزارش سی‌ان‌ان.
🔴
ایران پس از حملات نظامی قبلی آمریکا، دفاع‌های جزیره را تقویت کرده است، از جمله استقرار نیروی انسانی بیشتر، سامانه‌های دفاع هوایی و موشک‌های شانه‌پرتاب (MANPADS).
🔴
ایران همچنین مین‌های ضد نفر و ضد زره، از جمله در امتداد خط ساحلی، برای مقابله با عملیات احتمالی فرود قرار داده است.
🔴
مقامات و کارشناسان نظامی آمریکا پیش‌تر هشدار داده‌اند که هر عملیاتی با هدف تصرف جزیره، خطرات قابل توجهی از جمله تلفات سنگین احتمالی آمریکا به همراه خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/127154" target="_blank">📅 17:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127153">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
حزب‌الله : یه پهپاد هیرون اسرائیل تو بقاع سرنگون کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127153" target="_blank">📅 17:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127152">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b01cb957f5.mp4?token=S42upN4ZU6QchT7DB02R7g7RclhuLewpkYD9zHPLcHO4Of7f0R8cuikwGaAQZITJRIk7hvuo5TTv_i9k7SyG8Fdd6fTLXC5SNAMRhXgV8l7X1nDlptvWsm1Zg25Nz87ZXR6ZLqtOZb7tF9tkOHL8akmDjHwRSfZKeMM9xJ5Dn4uifkvtKdn5rPOdtu3bCScMICN5yscO6ZqGV5zSH-CSF9M3c8eUQ5WQO7vTsTndg9RNLUE-2lOXnGpsLcWalG6vyuUWdgWfKMQhcio0iWYpC7uO9PM7CdC8n3JM75XiCcywgzTBE5ePBbHglWdkypm_HTLZb4sNIeW40mCtcYvSWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b01cb957f5.mp4?token=S42upN4ZU6QchT7DB02R7g7RclhuLewpkYD9zHPLcHO4Of7f0R8cuikwGaAQZITJRIk7hvuo5TTv_i9k7SyG8Fdd6fTLXC5SNAMRhXgV8l7X1nDlptvWsm1Zg25Nz87ZXR6ZLqtOZb7tF9tkOHL8akmDjHwRSfZKeMM9xJ5Dn4uifkvtKdn5rPOdtu3bCScMICN5yscO6ZqGV5zSH-CSF9M3c8eUQ5WQO7vTsTndg9RNLUE-2lOXnGpsLcWalG6vyuUWdgWfKMQhcio0iWYpC7uO9PM7CdC8n3JM75XiCcywgzTBE5ePBbHglWdkypm_HTLZb4sNIeW40mCtcYvSWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان:
اسرائیل تحت مدیریت فعلی خود به کارخانه‌ای از تفرقه تبدیل شده است که تنها مواد اولیه آن خون و اشک است و چیزی جز بی‌ثباتی و هرج‌ومرج تولید نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/127152" target="_blank">📅 17:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127151">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در استان اربیل در شمال عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127151" target="_blank">📅 17:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127150">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP-tgSjnYwS0nd8sG5DMcDo8rstdXgveXAKpbeawqDP5sQBgFZ4rhlGjg4tyCJ4wuXMV_v1OLDdAQmtBWQ3r7qXb7_goFgOkKVl244iEEz94BiLDS-B2e62tDBBPtTuV5vf3kCbxDccBX4_UJDh20T4J5ucucD18j_mFtn6uHDXRYl0A7FlJliOIBDTf4B9KQBRpQckx2F4mfIOA3i_kr7_oA3HSSiZfTAaX5jbCTQzo3m4ydC-8HfjifTMh6C4Go7rrX6neNzRPtGQEG5jbwbJWC6ONler--cpMySe-ZlS8Z9yNpcUpVzrRDo6cBaSv9uRO_g0rJMPVcjEU_Fek7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلویزیون سوریه: احمد الشرع، رئیس جمهور سوریه سه روز دیگه تو کاخ سفید با ترامپ دیدار میکنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127150" target="_blank">📅 17:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127149">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وال استریت ژورنال: از این به بعد آمریکا «هر شب» به ایران حملهِ میکنه، تا زمانی که به توافق برسن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127149" target="_blank">📅 17:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127148">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6599e2d096.mp4?token=IKblTu6tzTIuVJMeNrtQ2DmedQ75htSfPhBrYK94vi8AU4T_2g-cZIUK1ue3KCpuaQZJLR_br5O9egIJQKeJTqzWXoPSFK19BXny0Xcv--gHtFHNuigkFLxhZkL8vY-RRX4Vn1z9GYkQorSX0W1uwNGcTl6JeWnKGoILO6z4MN5Rhrk24vy8qABCzf4bqCfJvn63RBFeVTioq3GxqR_zSpp34IWT9HB6Sq3FOjpIGNtXvlNRNbB-eVBd8w3OKXEjck62LnFTHORltTAZmT_6GI-JlYfJiTcuvyzn13wVjDZ5X2v436b41cCjr5_igreSLcTwaJNiDsgMX45LBUvAfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6599e2d096.mp4?token=IKblTu6tzTIuVJMeNrtQ2DmedQ75htSfPhBrYK94vi8AU4T_2g-cZIUK1ue3KCpuaQZJLR_br5O9egIJQKeJTqzWXoPSFK19BXny0Xcv--gHtFHNuigkFLxhZkL8vY-RRX4Vn1z9GYkQorSX0W1uwNGcTl6JeWnKGoILO6z4MN5Rhrk24vy8qABCzf4bqCfJvn63RBFeVTioq3GxqR_zSpp34IWT9HB6Sq3FOjpIGNtXvlNRNbB-eVBd8w3OKXEjck62LnFTHORltTAZmT_6GI-JlYfJiTcuvyzn13wVjDZ5X2v436b41cCjr5_igreSLcTwaJNiDsgMX45LBUvAfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کرد ها
: ما واقعاً برای معترضان ایران سلاح فرستادیم و صادقانه بگویم از کردها خیلی ناامید شدیم. کردها ما را ناامید کردند.
من با این تصمیم موافق نبودم. می‌گفتم: “نه، فکر نمی‌کنم آن‌ها این سلاح‌ها را تحویل بدهند.”
فکر می‌کنم آن‌ها سلاح‌ها را برای خودشان نگه داشتند. به نظر من این یک رسوایی است. اما من این موضوع را فراموش نمی‌کنم، کردها را فراموش نمی‌کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127148" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127147">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزیر خزانه‌ داری آمریکا:
هر آسیبی که به متحدان ما در خلیج فارس وارد کند، با وجوهی که از حساب‌ های ایرانی برداشت می‌شود، جبران خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127147" target="_blank">📅 16:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127146">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: پل‌ها هدف بعدی حملات ما هستند
🔴
ما برای معترضان ایرانی سلاح فرستادیم، اما از کردها بسیار ناامید شدیم زیرا آنها سلاح ها را به معترضان تحویل ندادند.
🔴
مسئله ایران تمام شده است و ما می‌توانیم فردا نیروهایمان را بیاوریم، اما نمی‌خواهم نیروی زمینی اعزام کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127146" target="_blank">📅 16:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127145">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:
ما در حال مذاکره با ایران هستیم
🔴
ترجیح می‌دهم جزیره خارک را در اختیار داشته باشم
🔴
ما هنوز به اندازه کافی به ایران ضربه نزده‌ایم
🔴
من از ایران ناامید نیستم، این توافق خوب است و ممکن است بزرگترین توافق تاریخ باشد
🔴
هواپیماهای ما بر فراز قلب تهران پرواز می‌کنند
🔴
ایران در تبلیغات خوب است اما در جنگیدن خوب نیست
🔴
اگر ایران توافق را امضا نکند، آن را به شدت بمباران خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127145" target="_blank">📅 16:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127144">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf4jOZTdP13w5ibbx2zNO3gEa17GO98xXzc0iAtTmKyC6Kh_-DBS0ZOUpQIptdB-BcbT9zRBedWnPzF0d0KVjDZmUj3vtSyGcbMNvBP0fBJH-qHknsYgP5kWGZ1wt-bb9o0Lln__bIVIj3mb5Y0cbG-O57C1Ief_qeEqbUXtyw1CT7XxTzUaZ52NtoMD5GFWioaRtp9hqLAuNBpt8ziKcYzxFFUevJa6v44SrGX96BGKMDyINCbwinqk3lfz3ZgpIFzIyrmJDtQsIsUBoMRNx5llngSXT2wqWphkSw52qvB2zwlNsQQzes75kqyqePJUykvMuPIOHgoySZg81z7uIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ونس، درباره نتانیاهو : ببین، قطعاً یه جاهایی اشتباهاتی داشته
🔴
ولی راستش بعضی از این بحث‌ها بهتره توی فضای خصوصی بمونه
🔴
چیزی که می‌خوام بگم اینه که در کل شریک خوبی بوده
- ما به همکاری ادامه می‌دیم، ولی هر جا منافع‌مون از هم جدا بشه،
🔴
آمریکا کار خودش رو بر اساس بهترین منافع کشورش جلو می‌بره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127144" target="_blank">📅 16:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127143">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epqu1YjW4Bag6qkXWfegrjcAvE7uZtTpi6t4Gan4LW51Blr_XhZc8ySI2cdixEVbZsTQWZyvKApQgELHytLaHz0HwYsspOghktM-swkksWNqQKWC29wH4pJnQIt4zYvfTBcEqaY-o6csHzKK0sb_TjxkV52vK7_mukefjGOzJvlfvhNCVrdTGpNOarwQ5WgjU0j2lCE9WwiPQKXTusrel9vTA-cHoU5a2tqC4YtzZxcdh0ySjD_YCWmMf7rYvXNhTuX9MhZFoqq6Nu-dew2l_YODu8noVd20qVMW4EqASWqT1eOLazUluvbeDdmZwO7TEgdfRCug4CElgUy8HpThVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اصابت پهپاد انتحاری ایران به رادار هشدار زود هنگام آمریکا در جبل الدخان بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127143" target="_blank">📅 16:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127142">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb295fdb6.mp4?token=ScX4uHeGwz7qnH_o-lxtHCUV0EIbOePo64k10z4a1dAMNlNMgig_rKr-N15kBnPtPAIgT41i3nfWBDzZuZccQmKBrd-ZnmUjc_kRuzHo1ZWmTUaGgq6N0nZPro2vBMTHnPTen2TLW8QS9U0TbLHMats5MEDPvLndEnJQYINRc43B5F6o3jCdrYzRRTbtpSl4p-Ix5BYlLpgFY3T72AA4qvxfSLGGwvdn7t4lDCTx6rxVD8EC4ORzXh6rUjRuLbXRitTeRLudhgNpa3A1czSWZ8KLiCZDFzrpSXLcefjY3_R7ooRkOQ6KdCRxj6840S6T_8iSSNhTSf6zv6ULS21HLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb295fdb6.mp4?token=ScX4uHeGwz7qnH_o-lxtHCUV0EIbOePo64k10z4a1dAMNlNMgig_rKr-N15kBnPtPAIgT41i3nfWBDzZuZccQmKBrd-ZnmUjc_kRuzHo1ZWmTUaGgq6N0nZPro2vBMTHnPTen2TLW8QS9U0TbLHMats5MEDPvLndEnJQYINRc43B5F6o3jCdrYzRRTbtpSl4p-Ix5BYlLpgFY3T72AA4qvxfSLGGwvdn7t4lDCTx6rxVD8EC4ORzXh6rUjRuLbXRitTeRLudhgNpa3A1czSWZ8KLiCZDFzrpSXLcefjY3_R7ooRkOQ6KdCRxj6840S6T_8iSSNhTSf6zv6ULS21HLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ویدیو رسمی فیفا برای شروع جام جهانی با نورپردازی خوشگل
☺️
😍
@AloSport</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127142" target="_blank">📅 16:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127141">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">😳
هنوزم ۱۰۰ و ۲۰۰ گیگ رو به اسم نامحدود میفروشن؟!
🚀
مخصوص جنگ
😎
@NetAazaad1Bot @NetAazaad1Bot اینجا از اون خبرا نیست
😎
⚡️
💎
نامحدود واقعی، بدون استرس تموم شدن حجم
✅
مخصوص این روزایی که اینترنت پایدار از نون شب واجب‌تره
❤️
🚀
فقط امشب با خیال راحت وصل شو و…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/127141" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127140">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K_kUEqOcQVh9XUdKNxeZnd0v1mQVFTcZvRuXM_W-7q_JycP0lYc6KlKjmt6yLtwgUpNEBPLAEsGNpesoJGOERPl2sfQ_tEHwZZIQxCacWLlpdtfAT_xB1R5M8uHtuUJAJX5O6CRlkzYhfOj7FbNNnK8dk7CJsrph_xWsXy0EgbEW9EI4Z5X5R_YtY9VXsq0XMpsSeFYadnB0iyOoYtQTSaMcESlmXkIkX7g3fsndzNubxhZaGw0vOaILX40IYDkYnen6lV3bqma57XCbBpC49VUg0tp-OZ_gEFrHpZQqtr8hH2MvFxnFMiI5bIvelcvK3u5qigwTf4Rxmvs2SnXxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
هنوزم ۱۰۰ و ۲۰۰ گیگ رو به اسم نامحدود میفروشن؟!
🚀
مخصوص جنگ
😎
@NetAazaad1Bot
@NetAazaad1Bot
اینجا از اون خبرا نیست
😎
⚡️
💎
نامحدود واقعی، بدون استرس تموم شدن حجم
✅
مخصوص این روزایی که اینترنت پایدار از نون شب واجب‌تره
❤️
🚀
فقط امشب با خیال راحت وصل شو و لذت ببر
⌛
ظرفیت هم محدوده، جا نمونی.
✅
@NetAazaad1Bot
@NetAazaad1Bot</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/127140" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127139">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر خارجه بحرین می گوید صبح امروز 36 فروند پهپاد ایرانی را منهدم کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127139" target="_blank">📅 16:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127138">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⭕️
الونیوز فقط در تلگرام
💬
و توییتر
❌
فعال هستش
🔴
سایر شبکه های اجتماعی چه داخلی چه خارجی که با نام الونیوز فعالیت می‌کنند مرتبط به ما نیست و پیشنهاد میکنم که لفت بدید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127138" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127137">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0kH1Y9TddHrF-z9whG0QUT5UXgbqktOdWFWe6s_3uW_qxrxolfL0h_9tYrlEWFFFLkv72rxHUkHWkY7fwO-KVTzgR7ITz2T6SoBc9E1vzR8FDCD0-5LTWOmMHRdOc0NSSuhpmiSzsv5qIyCBT066kk0KVJRMYnJ4gavG6ah6dYWra84tfeT9dcrDLWxvMb62U1bmYJDvZsXzE6KkNYjXPA38qL6jcpASuDTBxzJjHVqcCeuTrx5NM_u4w_fQIu-OhBHB050auva9dGTcSEztUayo-5AS01LMYVz-XEnL6QCRU4QFZ6VXI_M8uqEOJtm9MGBHRWZAbY9gqWvZQMFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووری/ترامپ:
ایالات متحده امشب به ایران ضربه‌ای بسیار سخت خواهد زد (ناوگان دریایی، نیروی هوایی، رادار، ضد هوایی و تمام اشکال دیگر دفاعی آن، همراه با بیشتر توان تهاجمی‌اش، از بین رفته‌اند!)
در آینده‌ای نه چندان دور، ما جزیره خارک و دیگر نقاط زیرساخت نفتی را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت، درست مانند کاری که با ونزوئلا انجام داده‌ایم، که برای هر دو کشور ونزوئلا و ایالات متحده آمریکا بسیار موفقیت‌آمیز بوده است. از توجه شما به این موضوع سپاسگزاریم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127137" target="_blank">📅 15:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127136">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJDY1SzRai6WRzSiT8G9tqmJD8QJ1j-POiTmC_5KEMzQOCDJfXtU_8OS0zGi7NXG_vuV1AEuBu8yhnvtdG0pLJhrOLuclgAUwlahLIKNQmFkGJb4c1CnsKTekLQmY7ssbyUHYU7uX5dq_xd_L-l3bJaalSj60QlMpikRE8IkjY62i_Oqjvsbj6YKMHEleEJxKe6E_CST1oouNK6alPKKaIN45pH8lFGEjNC4F7RXLZORei79DmT4KvL5ZpZD5PnfwxKkVNq_Y-lzTpKfVdQPwZiR9pvN1aLIMEQc44CCkUqpFYvdZi7MxH-sQ-oLNVbTAK8jewS0pi6-7bJSaCdPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری معتبر فارس:
ادعای سی‌ان‌ان درباره مذاکرات جدید ایران و آمریکا تکذیب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127136" target="_blank">📅 15:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127134">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lvBkUwMQkAh8aqTfgDH-narFDEmFWZls1PVyLyqRrxAb-FASsg50_eMYSxKpsa6dXdO9fiB8SB6Wd6Uv1RrvMzCkVXqaMalxgYkzuSCatcWisz9W5Z8ajRRTYINTu4JJN-w76X-KJsCsz9yb99wgiZRKF-BSoWxLp_vhC63c3CMP_z-1YGHOx4wg4k4DepV4BUAS1zqM2o3x7k5FNIfIBtyfucB45Os21YpTrTRvusmibqEG6SrjYXbx992VRyGJjgU6ELEpO4EainItX0ZLvq8qcU8njC7A2mlleXbvx7ZL7N_8m1_hUJssO1ChSiCOuBIuuiEs9IMCJf_zANOywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gbAnHL5aFcpKLP4KxDXOE_pIOSnFJUupo8_AiPvwhdZ5CCzslP6W8v5lbYS2LB3KfK8KC2ZDd9ZdeaaDod7TvQkIL-EehMMiAThNVnGRN2hDnJ7IS1AY6RAFXt01St-Y7Wb2DvRDe0ACsblEZVwUWdQ8DjuwnPwchoKli0ll5GfTUPO_UK6SYTcemiqZ6stByBKUkIwbvHIekVCAl1VS3hFVg5Lu2p-EdfLUsobdEV6IJGlCLqKVOfgziVc2-HZvhLxx9Wux-EKvwuVGVZSXnEwWBt8gSqCKz3VL6R0PighXvLJctf_EZq-LkAhIAnxsELEio59hVwqK35iDuGlz8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دو آتش سوزی در نقاط مختلف پایگاه هوایی شیخ عیسی بحرین بعد از دو راند اصابت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127134" target="_blank">📅 15:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127133">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
العربیه:
پاکستان و قطر در ساعات گذشته تلاش‌های خود را برای پیشبرد یک توافق افزایش داده‌اند و این منبع گزارش‌های مربوط به عقب‌نشینی‌ها در مذاکرات را نادرست دانسته است.
🔴
منابع ارشد همچنین تأیید کردند که ایران پاسخ خود را به پیامی که وزیر کشور پاکستان، محسن نقوی، تحویل داده بود، ارائه کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127133" target="_blank">📅 15:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127132">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
کویت: رفتار ایران نشان داده سازمان یافته حمله می‌کند و ما مجبوریم پاسخ ایران را بدهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127132" target="_blank">📅 15:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127131">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس درباره نتانیاهو: نتانیاهو کشوری را اداره می‌کند که آشکارا شریک بسیار نزدیکی برای ایالات متحده بوده است.
🔴
اما حتی زمانی که شریک نزدیک بوده‌ایم، گاهی منافع ما کاملاً همسو بوده و گاهی منافع ما ناسازگار بوده است.
🔴
نتانیاهو به شدت منافع کشورش را مطرح می‌کند. گاهی این به معنای هم‌راستایی ماست و گاهی به معنای عدم هم‌راستایی است.
🔴
آنها در بسیاری از جنبه‌ها شریک خوبی بوده‌اند، اما ما همچنین باید بر آنچه به نفع آمریکا است تمرکز کنیم. و جایی که این منافع متفاوت است، متأسفانه برای اسرائیلی‌ها، ما باید طرف مردم آمریکا را انتخاب کنیم، که همیشه این کار را انجام می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127131" target="_blank">📅 15:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127130">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
یک منبع دیپلماتیک عالی‌رتبه به الحدث:
ایران پاسخ خود را دربارهٔ پیامی که وزیر کشور پاکستان تحویل داده بود، ارائه کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127130" target="_blank">📅 15:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127129">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be3c800123.mp4?token=f8XK-urS6MfhQxQsTEh7kjwQLpJu_j44pOc84DO80rYxL0eslp9KfrWxdWHeN_S0kguk3tloGue8Ukj3jufOxRUMawBslcAENFuQE1Kp5TQ0w9uMXlqHb91NwaNS32gMERM2i_ErjAq1JZEJBWHFR5xbWj_O-NZQmnZm-bV9A4ay5LmzLI0MSBOSam4knXkg7ZzvMEvX4XmYsOwa6qAjuyOLhc56scT3MntGUP1Mwdj8mcoOrmBL0ZAorVTV_iL1vfy11Q6nhk-DL-ohk86jvWQIgmOdW47h6qIKDQzmA25tmRr7Yd7MYTTQEk-rHDXqBES6FAuTApRySVx0v6MECoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be3c800123.mp4?token=f8XK-urS6MfhQxQsTEh7kjwQLpJu_j44pOc84DO80rYxL0eslp9KfrWxdWHeN_S0kguk3tloGue8Ukj3jufOxRUMawBslcAENFuQE1Kp5TQ0w9uMXlqHb91NwaNS32gMERM2i_ErjAq1JZEJBWHFR5xbWj_O-NZQmnZm-bV9A4ay5LmzLI0MSBOSam4knXkg7ZzvMEvX4XmYsOwa6qAjuyOLhc56scT3MntGUP1Mwdj8mcoOrmBL0ZAorVTV_iL1vfy11Q6nhk-DL-ohk86jvWQIgmOdW47h6qIKDQzmA25tmRr7Yd7MYTTQEk-rHDXqBES6FAuTApRySVx0v6MECoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام:
نیروهای آمریکایی یک نفتکش را در خلیج عمان در ساعت ۱۱:۲۰ شب به وقت شرقی در ۱۰ ژوئن غیرفعال کردند، پس از آنکه این کشتی با تلاش برای حمل نفت ایران، تحریم علیه ایران را نقض کرد و این سومین کشتی تجاری است که این هفته توسط نیروهای آمریکایی غیرفعال شده است.
🔴
فرماندهی مرکزی ایالات متحده (centcom) علیه نفتکش m/t jalveer که پرچم گینه بیسائو را داشت و تلاش می‌کرد نفت را از ایران از طریق خلیج عمان حمل کند، اقدام کرد.
🔴
یک هواپیمای آمریکایی دو موشک هلفایر به اتاق موتور کشتی شلیک کرد پس از آنکه خدمه بارها از اطاعت دستورات نیروهای آمریکایی خودداری کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127129" target="_blank">📅 15:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127128">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0R1AT6hZLOup7IuQKDuXUs9et6oy3uPZVNuOLK91AoGtpeoBDbqtv38KF6oUR6F301LPP6jkFtTlZ5COQWMIsHyO0J_z1Lwv0NS1SCNERZJznVSssIKHs_sUKdqS2VnfTeGGCf__09ZZs_MyMowCXakwsuGcBoo_zDJoABxz2152HaUJThSo1I2rxtCK9KBOIpWWvlXsFCEvgYk4drRf4l7ZkUzw-EdEbGIt67QeU6IRs_f7E9V2zNaKkPSbMoRNnljNrlZ_jD3EqVQME6Xou18U1-m_rve5S5ylkn2b7y291QzdJzivCljf1eK5GlBzARsHETSewdqqw56CUE48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127128" target="_blank">📅 15:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127127">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رئیس جمهور لبنان: با وجود فشارها از مذاکرات عقب‌نشینی نخواهیم کرد و تا رسیدن به آنچه به نفع ملت ماست، به این مسیر ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127127" target="_blank">📅 15:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127126">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcP2H0pneYDY6WavzgTWlK8WxN9ryUc2IWvn8EihcISlWXH6p-C4sZchfIG-Ri3pdQC9QoThXyVb2QcUpjOHaIrS57y6lqHYTeY8wW6XPubId1LmjNSYOdTetXWklkmh2z-lqWJzOtyHyjpFjotV5Cji_iSmS2w_eYFIvlryr6SH_3RTKZC-tFm8edTLPGWIVuFoBo1GpF2TWjLITKExbk9iu3WNN8HAQzs4Yi9p63bhQ74mRm574poB6WLE80nQ1Mx1K5wA9FT9fAiuOgUj8LQnJ5wxhUXMNjYoF3FIYEgrQ6n5lZc3B5Jhm25qU-8adgl_9pwJTyPd_xsOxfPfQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۲.۰۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127126" target="_blank">📅 14:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127125">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
خبرنگار صداوسیما: لحظاتی پیش صدای انفجار در محدوده سیریک و از سمت دریا شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127125" target="_blank">📅 14:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127124">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpgr6DFJvrn1_9zY8lWiBU5YowkLPmTvxAZv2GPuOiWmLqImFcampRGjYZKTsnF0AIa1DSMZ9tJWzvFfOCwWJ7_vxmrx0gg_cYsDwwKQcCaRQRXKj2FoTBwDS-xaiRDGmFjaJNc4RGP-Dow0vBYwrqpJ3iPCVqgLOQuy5KZXOOZGhdXBfhwDgubc3KrimEldR4AQ8Wu3ef7H-3MnPXgDjTAIpLxh1o7a1Oi6O7eCC26zsSgUoTwYT3hqRlgs6_E0QedwRDaxLrisU-ya001M7XOI74VE4ztGkwvFBJ1VzuQFtoqRwFtwKECQr4zbXRN5Nn67HETH8fkCIrRC1pdYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع بریتانیا، جان هیلی، استعفا داد و اعلام کرد که نخست‌وزیر کیر استارمر و وزارت خزانه‌داری منابع لازم برای دفاع را در برابر تهدیدهای فزاینده تأمین نکرده‌اند.
🔴
او در نامه استعفای خود گفته است که «طرح سرمایه‌گذاری دفاعی» پیشنهادی «به‌طور قابل توجهی ناکافی است» و هشدار داده که این موضوع می‌تواند آمادگی نیروهای مسلح بریتانیا را کاهش داده و این کشور را «کمتر امن» کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127124" target="_blank">📅 14:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127123">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرنگار الجزیره: یک پهپاد اسرائیلی یک موتورسیکلت را در شهر حبوش در منطقه نبطیه در جنوب لبنان هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127123" target="_blank">📅 14:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127122">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
گفت‌وگوی وزیر خارجه ایران و مسئول سیاست خارجی اتحادیه اروپا درباره حملات اخیر آمریکا
🔴
عراقچی: این اقدامات آتش‌بس را بی‌اثر کرده
🔴
مسئولیت پیامد‌های خطرناک آن نیز بر عهده واشنگتن است
🔴
انفعال جهانی، موجب افزایش ناامنی جهانی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127122" target="_blank">📅 14:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127121">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا: اروپا باید در صورت تمایل ایران به مذاکره، تحریم‌ها را کاهش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127121" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127120">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9650d1637f.mp4?token=XRdMclMZnUf6NL2vcj4cupqSZXrR-ra1qBoa2e5paQsyJOYlw6Zs70cEv-7EzfSowFU3wpHptHrucicOs2bh8OUtvCYy3c3oJ_7XjIsx268oJ_68AMfk4wzmzt8H3hAI_RSCKAn3DyPsbaM6MSrh_J096F8WDmb-7H15Y0r05xOrxiSg6Cx-mq8SuOlYMKwXd7-dLOtagbDpYTtFqHyOZOIOAhnBOVEXrnSh3tdFp_uNS1nDzolGhQi9ntpYtiJhIGVUMNVd7wUez7pdlpJ0yVOCTFTKSdq6aQ2VT49o0XMzsItEuoY42ufKOAfMrJIS-Q9F6ngiqMzDFuKIIYV_K0nplzW_EdCOVcNkMa-OZLNSBDryOT3tsXf0xREuCW9meOmmskPQ-FVqjWlf6uCNNqTtaPzYGDFF5JAlBLTquYN7c7BntF77lYG65Q8x2wuXpOTmTt09kPwxGMVnDJVHUkgqC9v1n2tM4fgPOOmZ7b7eWf4GRM8-gek5PmDa95pdJ-UfNK4TBgh4B2g9onjQnhfk1ew2Nk9gDrM49REUto6ZXEfQYr4GN_fPESFn4GrSoVcg4DJmLY6NHhPCOifs-BonK2xSCOUw6E47_zGBJsrkWiald20ijTdFs0QIVO_pZ9LTWN3s1VNooCPPex_dIA6qzr40ldfc_WB7OUM9Nnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9650d1637f.mp4?token=XRdMclMZnUf6NL2vcj4cupqSZXrR-ra1qBoa2e5paQsyJOYlw6Zs70cEv-7EzfSowFU3wpHptHrucicOs2bh8OUtvCYy3c3oJ_7XjIsx268oJ_68AMfk4wzmzt8H3hAI_RSCKAn3DyPsbaM6MSrh_J096F8WDmb-7H15Y0r05xOrxiSg6Cx-mq8SuOlYMKwXd7-dLOtagbDpYTtFqHyOZOIOAhnBOVEXrnSh3tdFp_uNS1nDzolGhQi9ntpYtiJhIGVUMNVd7wUez7pdlpJ0yVOCTFTKSdq6aQ2VT49o0XMzsItEuoY42ufKOAfMrJIS-Q9F6ngiqMzDFuKIIYV_K0nplzW_EdCOVcNkMa-OZLNSBDryOT3tsXf0xREuCW9meOmmskPQ-FVqjWlf6uCNNqTtaPzYGDFF5JAlBLTquYN7c7BntF77lYG65Q8x2wuXpOTmTt09kPwxGMVnDJVHUkgqC9v1n2tM4fgPOOmZ7b7eWf4GRM8-gek5PmDa95pdJ-UfNK4TBgh4B2g9onjQnhfk1ew2Nk9gDrM49REUto6ZXEfQYr4GN_fPESFn4GrSoVcg4DJmLY6NHhPCOifs-BonK2xSCOUw6E47_zGBJsrkWiald20ijTdFs0QIVO_pZ9LTWN3s1VNooCPPex_dIA6qzr40ldfc_WB7OUM9Nnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : ما تو همه جبهه‌ها پیشرفت قابل‌توجهی می‌بینیم
🔴
هر هفته صدها نفر از نیروهای مسلح دشمن رو از بین می‌بریم
🔴
همچنان چالش‌های دیگه‌ای هم پیش رو داریم
🔴
یه چالش ویژه هم موضوع ربوده‌شده‌ها (گروگان‌ها)هست که روی اون کار می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127120" target="_blank">📅 14:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127119">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=BATnC8PB5BT9kcGrRkIZC2oyaUIDEwil-8i0uE0LOjhfq_Gc28xyHpqRFCvKfdH0E7SoXOWHg7rhXxmMgpXIH_g_jU1elEXuU5pgtviAFFbgcDOPte94DAZ9DAIkgGiJf0TuJ3CSekfCtKzdEoWIwMuTOV1vLMD-b5buI2fClZtG6U7lJ4Cu-Ie0aJ8vGnO4yk3EBMQE6t4URJ6Fkra7aFY_0I4bR6maERx4auim2fBShCwhvxADdrdPwb9WD-fY1M_XvqRT20pean7zh-sverjMbXZQLDK1OuGdR0AqHBcaBcck2_aWXZBVrNDYCwuO-orYMplJioS-ULtE32lYLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=BATnC8PB5BT9kcGrRkIZC2oyaUIDEwil-8i0uE0LOjhfq_Gc28xyHpqRFCvKfdH0E7SoXOWHg7rhXxmMgpXIH_g_jU1elEXuU5pgtviAFFbgcDOPte94DAZ9DAIkgGiJf0TuJ3CSekfCtKzdEoWIwMuTOV1vLMD-b5buI2fClZtG6U7lJ4Cu-Ie0aJ8vGnO4yk3EBMQE6t4URJ6Fkra7aFY_0I4bR6maERx4auim2fBShCwhvxADdrdPwb9WD-fY1M_XvqRT20pean7zh-sverjMbXZQLDK1OuGdR0AqHBcaBcck2_aWXZBVrNDYCwuO-orYMplJioS-ULtE32lYLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از حملات امروز اسرائیل به لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127119" target="_blank">📅 14:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127118">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TA1UA1joihq2lfmk7mAHj2orwD64YZNLFyEnQ8_trFkqt6VsapDSO5Q878ozS-r7c5n79BNQyiha9SjSTCtFy4T2VELu3JVwHE7EvhQLc0kYlYrzEF-NZR_ay5rePutHg47Ou20e1YFsXIfHViTKsLu0Lf3Iw4yiON235oUkTYBf-kFlULgc67ZwUokhFVk-xOaVB7ZmZ57aq3LB-Y_neDGggcNfjjLTq3Rm_I8Efq6V_MOhzbdHQOzKGstFHuQjX0TG75UPo1naL11-W6p4Cy9qgSx8LcxlWwPyskxnL8u08NOddaIJGOdeWyj1f86x7UFIu02UdDeCch4J6XmgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد ، مارشال محسن رضایی: رئیس‌جمهور بی‌ثبات آمریکا تصور می‌کند که بمب‌ها می‌توانند او را از باتلاقی که خودش ایجاد کرده نجات دهند. اما موشک‌های ایرانی او را حتی عمیق‌تر در آن فرو خواهند برد.
🔴
واشنگتن باید بین پذیرش شروط ایران و از دست دادن آخرین ذره اعتبار خود در جهان یکی را انتخاب کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127118" target="_blank">📅 14:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127117">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
صدراعظم آلمان فریدریش مرز:
ایران باید برنامه هسته‌ای خود را به طور قابل راستی‌آزمایی و دائمی متوقف کند.
🔴
امنیت اسرائیل و کل منطقه باید تضمین شود؛ در غیر این صورت، صلحی در منطقه نخواهد بود.
🔴
امروز، ما در حال کمک به شکل‌دهی نظم نوین جهانی هستیم که در آن اروپا جایگاه قدرتمندی پیدا می‌کند، تا اروپا بتواند به عنوان نیرویی برای آزادی و شکوفایی، برای صلح و دموکراسی در جهان باقی بماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127117" target="_blank">📅 14:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127116">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزارت خارجه کویت: حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127116" target="_blank">📅 14:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127115">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تسنیم: ادعای رسیدن به متن نهایی برای تفاهم بین ایران و آمریکا خبرسازی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/127115" target="_blank">📅 14:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127114">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رئیس سازمان اورژانس کشور: ۵ نفر در حملات بامداد امروز مصدوم شدند که ۳ نفر در تهران و ۲ نفر در هرمزگان بودند.
🔴
همه مصدومان پس از درمان مرخص شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/127114" target="_blank">📅 13:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127113">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت خارجه هند: ۳ کشتی هندی هدف حملاتی قرار گرفته‌اند که توسط نیروی دریایی ایالات متحده انجام شده است.
🔴
۱۳ کشتی با پرچم هند در تنگه هرمز گرفتار شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/127113" target="_blank">📅 13:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127112">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه: ایران و آمریکا باید حملات را متوقف کنند و برای پایان دادن به مذاکرات به میز مذاکره بازگردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/127112" target="_blank">📅 13:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127111">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTytdOSaQjibMuCo0qS8A5S0bMXtS3G-a0k0oNfgeTFLIIS7I0_oMhTfTqWqzOsdRr5STEBZMDyMaVr0QRoK6xhGTVc4aV1L23US1nNRlYC1ssldGfjD8rA9RYODcoSgK8jfFQzEsW1fE-85JnXq70ZeeMZqJkjbVZdrFJHrD09NZef4Tpk-yDRB3kMUqqe-iQrgr57z2aorqtJreM0V79y1VLAKChs6QWECiDhtLWALiyfn0l62OwDpmKwyvDoOLyHhc74JxnXwC3IbuY71LuOomzgO3uam2YwQphXCv2EDO6xL-RkITyQc2mjPuQ3Q4WeW0yEa0yh7CtL9OKmVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: هیئت قطری امروز صبح پس از برگزاری مذاکرات شبانه با مقامات ایرانی که با هماهنگی ایالات متحده انجام شد، تهران را ترک کرد، در حالی که حملات آمریکا به ایران در همان بازه زمانی مذاکرات شبانه صورت گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/127111" target="_blank">📅 13:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127110">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fd611e5ea.mp4?token=vDsHZzmobBLc6l3ROEBsqzKjzD4ekXHcpdkuIlPuXV0I10hrNJm56wWMgAlTX7Q0STbE7QweGqvWUlEqbJFbBnR5NdwTc8p5xOfglmoJgwLtS6Z9DJ9tu0Npw1eR7azf4l5TUzA_tkcqj2wx4yYotfVudRZy1kxIEy_BUC1etUWlaK1Fs52Y5izyZu-X7ob5QfnwZUI-uyIpaGksl1sq4sgqG6dYQRDLrPp8dKSb0Q1p6jw_JgQwVIAZjuyb0MtEAGnyesn0sSJsZt9qWl4R0SwYsStcrEx0EeQ-roi5a-5bS8VOG1uMStWqCKy1uWVV0IgscjZ1D7auxGZD_ELktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fd611e5ea.mp4?token=vDsHZzmobBLc6l3ROEBsqzKjzD4ekXHcpdkuIlPuXV0I10hrNJm56wWMgAlTX7Q0STbE7QweGqvWUlEqbJFbBnR5NdwTc8p5xOfglmoJgwLtS6Z9DJ9tu0Npw1eR7azf4l5TUzA_tkcqj2wx4yYotfVudRZy1kxIEy_BUC1etUWlaK1Fs52Y5izyZu-X7ob5QfnwZUI-uyIpaGksl1sq4sgqG6dYQRDLrPp8dKSb0Q1p6jw_JgQwVIAZjuyb0MtEAGnyesn0sSJsZt9qWl4R0SwYsStcrEx0EeQ-roi5a-5bS8VOG1uMStWqCKy1uWVV0IgscjZ1D7auxGZD_ELktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط بالگرد ارتش پاکستان با دست‌کم ۲۲ کشته
🔴
ارتش پاکستان اعلام کرد: یک بالگرد MI-17 ارتش دیروز به دلیل نقص فنی در کشمیر تحت کنترل پاکستان سقوط کرد و تمام سرنشینان آن کشته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/127110" target="_blank">📅 13:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127109">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کرملین: از واشنگتن و تهران می‌خواهیم خویشتنداری را رعایت کنند و به مذاکرات ادامه دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/127109" target="_blank">📅 13:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127108">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سه دریانورد هندی پس از حمله آمریکا به کشتی M/T Settebello مرتبط با ایران در خلیج عمان در روز چهارشنبه، جان خود را از دست داده‌اند، گزارش CNN.
🔴
دهلی نو نماینده موقت آمریکا را برای اعتراض احضار کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/127108" target="_blank">📅 13:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127107">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4d7ae260d.mp4?token=pBoouTEHQtEnZhiz98cVsJPd15_yvhZ-piNHDJ_7vWJ0G7ReIz6k7f-6DVWcWWBaua_PDHV2CNQ2OTJHG5crF8xKH4DfiFsmO2VJMs0k8ocGfdDtZmWjPLvxaYNlKGhueAFb1DAL3D25qColujU4eM3EEyZ51R-oHsPxVJE0KK2Tawxh9uCcF4HLzexBYTwzSZ6fCsrJMaBkjN3omqOTFx4KDEwsucJ6DCPt2Zc3Ly0ThTndSzZdbnQtSiS0RFv5v_55UMwF4_v5gDkyGzEhfya6R9pTWD18kchTbcGzMZNfKb_essnjq5d6o-H0gnDA2r7ONQ3SUeytRutnsgfB5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4d7ae260d.mp4?token=pBoouTEHQtEnZhiz98cVsJPd15_yvhZ-piNHDJ_7vWJ0G7ReIz6k7f-6DVWcWWBaua_PDHV2CNQ2OTJHG5crF8xKH4DfiFsmO2VJMs0k8ocGfdDtZmWjPLvxaYNlKGhueAFb1DAL3D25qColujU4eM3EEyZ51R-oHsPxVJE0KK2Tawxh9uCcF4HLzexBYTwzSZ6fCsrJMaBkjN3omqOTFx4KDEwsucJ6DCPt2Zc3Ly0ThTndSzZdbnQtSiS0RFv5v_55UMwF4_v5gDkyGzEhfya6R9pTWD18kchTbcGzMZNfKb_essnjq5d6o-H0gnDA2r7ONQ3SUeytRutnsgfB5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تهدید تلویحی ایران به حمله اتمی / کیث کلوگ، مشاور سابق ترامپ: «داشتن یک جنگ طولانی مدت، روش جنگی آمریکایی نیست. ما باید به روشی که در جنگ جهانی دوم و جنگ جهانی اول انجام دادیم برگردیم و کار را تمام کنیم، آنها را نابود کنیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/127107" target="_blank">📅 13:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127106">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
انفجارها در خارج محدوده شهری دزفول کنترل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/127106" target="_blank">📅 13:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127105">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzKH2XDbCUEdWJ4GGMDMboaC9_Kvm_sYNlqop6o_li6ApwskNCvSfS-SfXgXGhvlMldkcrkqoV_v6AyHF_VIJq1H0OZmI66jHQsy3DuOTbdKC4eC5awosEVDB0SouV5EDsnZZly-D7vS4oiPEY_KrF9z3h5Fyg0fEgwlt2fofcdhQha-EwoIxJm8G_dljYtD-4Qg9TZe8O8xFXmZRO6yecwEmZ4-_USj820ngcyUjcQ-Lqsqa9yZ7ankihobFYzc878Ca3OqpWGuBdRlMXnCdCSxws9mDcRDJOxs4Q2_y3t2VHgHgkvv5bzNI-QYPQ3axD_lNaQUupwl7S_PE0l0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج فارس: تنگه‌هرمز تا اطلاع ثانوی بسته خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/127105" target="_blank">📅 12:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127104">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه پاکستان: کانال‌های ارتباطی دیپلماتیک بین آمریکا و ایران از طریق پاکستان باز بوده و همچنان باز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/127104" target="_blank">📅 12:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127103">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f715d743a.mp4?token=F5v8I4lZEo706UJ02G0r__L4Jwc_whczUMyovEL-2dHOrX02VG5R9E4o0QNCGl9gi3GgS9uGuUo_wUctfAFD8jbVOXCyrPGsY7fUdOfwgyR7nCTutx74PnrK87HfWFDU9qpyJA8DraU5MdQuyAsQDI-U4sJNbUDG1rNxF9Eo7WQITAK-6EKcKaniQP2wcshkeDU3xWy6dO5GEqd7C7qpnnOTlQjes1yQjfWvUxD5xHKR5X0f0Har2JJ9VbrZYR6HwJ-MUoxo6GaACGJeS6A-_9wygtyDcUQCNC2_GDdc-XZ33GPzFphGpMa93RNxKDd0coKVmlDnoH6jv8RSB0KnTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f715d743a.mp4?token=F5v8I4lZEo706UJ02G0r__L4Jwc_whczUMyovEL-2dHOrX02VG5R9E4o0QNCGl9gi3GgS9uGuUo_wUctfAFD8jbVOXCyrPGsY7fUdOfwgyR7nCTutx74PnrK87HfWFDU9qpyJA8DraU5MdQuyAsQDI-U4sJNbUDG1rNxF9Eo7WQITAK-6EKcKaniQP2wcshkeDU3xWy6dO5GEqd7C7qpnnOTlQjes1yQjfWvUxD5xHKR5X0f0Har2JJ9VbrZYR6HwJ-MUoxo6GaACGJeS6A-_9wygtyDcUQCNC2_GDdc-XZ33GPzFphGpMa93RNxKDd0coKVmlDnoH6jv8RSB0KnTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله ایران به اردن، صبح امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/127103" target="_blank">📅 12:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127102">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رویترز به نقل از منابع: تلاش‌ها برای دستیابی به یک توافق اولیه بین ایران و آمریکا شدت گرفته است، با وجود حملاتی که دو طرف انجام داده‌اند. این تلاش‌ها شامل بحث بر سر مکانیزمی برای آزادسازی دارایی‌های بلوکه‌شده ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/127102" target="_blank">📅 12:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127101">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری / ادعای رسانه بریتانیایی امواج:
پیش‌نویس توافق نهایی تهیه شده است.
🔴
متن آماده است. دیشب نهایی شد
🔴
اگر تا امروز به صورت نهایی تایید شود، به صورت رسمی اعلام می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/127101" target="_blank">📅 12:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127100">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
شب گذشته ارتش ایالات متحده با ۴۹ موشک تاماهاوک به اهدافی در ایران حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/127100" target="_blank">📅 12:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127099">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
منابع ایرانی به رویترز: ایران و ایالات متحده هنوز در حال مذاکره درباره یک توافق اولیه هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/127099" target="_blank">📅 12:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127098">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بررسی داده‌های سامانه‌های پایش اینترنت از جمله رادار کلودفلر، نت بلاکس و رادار ابرآروان، نشان می‌دهد که اینترنت ایران در حال حاضر در وضعیت پایدار قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/127098" target="_blank">📅 12:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127097">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXBMw1swsH6gLEWW08dg_ThPV0q-txZjZBand-60wkqvkRbkVeDe2Z5OaMP3o3apAmJ_loc8p8ahAEjyuBg6gIF66sGBRbdriJeMWMBDAF0VHTwtKG7ZiUd6TGDNA7G7WGi7qkKczdIcFj3UYAOoV7UHQa7l1kaan2Q00W6BBGdVnhnIiC5X_KDgqYUZT9bMxEXPmfn31e_eWmt33VmGexIgTU_SoYy80hHGBjD316aB3Uylk5fvIRw2S3qM5lYOyImHx7HwoyZ2-NWnXaJfb0bSd7ImcvFLVvE9anbu3IZPeXZSqxJRPkhMx42l_i5QIM3Y6uJtB61nPzwNNfBCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندوقت پیش یه زنه بعداز این‌که ۱۰ روز از ازدواجشون می‌گذره، شوهرش رو گول میزنه با دوست‌پسرش پا میشه میره شمال؛ وقتی برمیگرده شوهرش میفهمه و زنه با کلی التماس شوهرشو قانع میکنه که دیگه تکرار نمیشه
🔴
چند روز بعد شوهرش حین تماس تصویری زنش با دوس‌پسرش میرسه خونه و مچشونو میگیره.
🔴
این سری با دوست‌پسر زنش (امیر) یه قرار میذاره و وقتی میرن سرقرار، یه چاقو به امیر فرو میکنه و میکشتش و بعد خودش رو تحویل پلیس میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/127097" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رویترز: مذاکره‌کنندگان قطری پس از مذاکرات با مقامات ایرانی که تا ساعات اولیه صبح پنج‌شنبه ادامه داشت، روز پنج‌شنبه تهران را ترک کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127096" target="_blank">📅 12:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127095">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت امور خارجه کویت: ما تأکید می‌کنیم که  کویت حق خود را برای اتخاذ اقدامات لازم برای حفظ امنیت و دفاع از خاک و تأسیسات خود محفوظ می‌دارد.
🔴
حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127095" target="_blank">📅 12:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مخبر: اگر دشمنان شروط ایران را بپذیرند جنگی در کار نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127094" target="_blank">📅 12:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
الجزیره: حملات هوایی اسرائیل شهرهای سریفا، برج قلاویه و طولین در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127093" target="_blank">📅 12:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وال استریت ژورنال: کاهش شدید واردات نفت خام چین در طول جنگ ایران، در پایین نگه داشتن قیمت نفت و حفظ رونق اقتصاد جهانی نقش مهمی داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127092" target="_blank">📅 12:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it3pUd-l9KTvZipHdfMD1hKxV5iioJsDJ2vTBBqNpiYLbcRi4rpb1EY0xmOeMK6nKPcrXEutVGWxMpTDTJMZDnb2e7A7GY6qoR-PpGZ6R3IPIZNdn6pzo9_Z9s5fiuAHKqc4Whv2BBYFobyZwqMPciqIwMXHRa4cFTTjVNF3fDi1Zx5TXjchLfrEoX1lFAm39ARbx233Pk0_c6x_-FlZfidD9v1yhXURo2zFUaD0_gJDe7xSThjHgczK-3QOaG2EK7j8814nsGNvVM-25QhGUE6e4Y-udSb1Ly46kuByh1T24iryA9zBD4-3k_P_dRmkbVtnCgdIDYUNAp-MUsGJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: با هضم تشدید تنش‌ها در حملات آمریکا و ایران توسط معامله‌گران، قیمت نفت افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127091" target="_blank">📅 12:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127090">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554c9942ea.mp4?token=mdFB1DiWe8aSM8f6PhC0GwvVKApRGaId64ZYgI03H-RCn9DFvdssiQtWUE-FSLft25wUfcvpd0anzlmhxSSbIhjqX-vrI-qeUBQMuNgiWpDHEysp8Ichoiz_-0qhhnhzCKkYQP06PQTeIsMaDWRijLEI3Ureb-6Ylbv9ofDBIzTyCpjfhOxd6yei4BF4azvIXw4aW9GC936kxwcezKz8tEqX2QQzyRjNwqmF-v5GCizPy3j3VAv30nZti380ILDkjtLTG-MzcnNBr0QYhUFNYxDFTXl8Gf8YaQ57WAQFfZiqjMdKOeuOPLxm1lpc9h-X_Ep56nAWVDyPCykyThXrRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554c9942ea.mp4?token=mdFB1DiWe8aSM8f6PhC0GwvVKApRGaId64ZYgI03H-RCn9DFvdssiQtWUE-FSLft25wUfcvpd0anzlmhxSSbIhjqX-vrI-qeUBQMuNgiWpDHEysp8Ichoiz_-0qhhnhzCKkYQP06PQTeIsMaDWRijLEI3Ureb-6Ylbv9ofDBIzTyCpjfhOxd6yei4BF4azvIXw4aW9GC936kxwcezKz8tEqX2QQzyRjNwqmF-v5GCizPy3j3VAv30nZti380ILDkjtLTG-MzcnNBr0QYhUFNYxDFTXl8Gf8YaQ57WAQFfZiqjMdKOeuOPLxm1lpc9h-X_Ep56nAWVDyPCykyThXrRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جواد خیابانی: سردار تو تیم نیستی ولی هستی، بعضیا وقتی نیستن، نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستن
!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127090" target="_blank">📅 12:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127089">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت خارجه چین درباره حمله آمریکا به ایران: باید امنیت کشورهای منطقه محترم شمرده شده و حفظ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127089" target="_blank">📅 12:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127088">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرگزاری مهر: یک حملهٔ آمریکایی به یک کشتی باربری 150 تنی ایران، در خلیج عمان در اوایل امروز انجام شد، این کشتی حامل کالاهای ضروری را از خصب، عمان، به ایران حمل می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127088" target="_blank">📅 11:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127087">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سپاه پنج پایگاه نظامی در اردن، کویت و بحرین را هدف قرار داده است
🔴
پایگاه هوایی موفق السلط (اردن)
🔴
پایگاه هوایی احمد الجابر (کویت)
🔴
پایگاه هوایی علی السالم (کویت)
🔴
مقر ناوگان پنجم آمریکا (بحرین)
🔴
پایگاه هوایی شیخ عیسی (بحرین)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127087" target="_blank">📅 11:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127086">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/191eaaade8.mp4?token=jZoM4NMsKKKxsJOApdfmeRW_mFOWEsaJgme364Gn_dwUHkuL4KLmX0rYK9iMGmAL6CIrTVUhbxXYs-c0QY5e7_2DylE6Zc90NNouuCF0uHAb3sVstkt8-a2qsFgEInHgcZHQP9YWertI5_2N0T-MuLzHgZfmJCTj3QjPzQinzYP2WpS4xXA85NEdRHt7HqqlIWd17pz70BGMDYOPj40zUoIK4kTfPu5ag0_CQYpU1E8MLzAXt7wQOFFr6iYHWj1OmAe2h87VQhXj2h_oloRrd2QVp-yViq57ewYcyAZGaPwfeKK_09CZRnnUHmkH5IjWT59v7lRXmEk1xePyHd9wMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/191eaaade8.mp4?token=jZoM4NMsKKKxsJOApdfmeRW_mFOWEsaJgme364Gn_dwUHkuL4KLmX0rYK9iMGmAL6CIrTVUhbxXYs-c0QY5e7_2DylE6Zc90NNouuCF0uHAb3sVstkt8-a2qsFgEInHgcZHQP9YWertI5_2N0T-MuLzHgZfmJCTj3QjPzQinzYP2WpS4xXA85NEdRHt7HqqlIWd17pz70BGMDYOPj40zUoIK4kTfPu5ag0_CQYpU1E8MLzAXt7wQOFFr6iYHWj1OmAe2h87VQhXj2h_oloRrd2QVp-yViq57ewYcyAZGaPwfeKK_09CZRnnUHmkH5IjWT59v7lRXmEk1xePyHd9wMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه وکیل: دارک ترین پرونده ای که داشتم؟
۱۰۰ تا زن متاهل با یه پسر ۲۴ ساله خیلی زیبا رابطه داشتن که شاید بچشون به اون پسر بره و خوشگل بشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/127086" target="_blank">📅 11:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127085">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
پاکستان درباره درگیری‌ها میان ایران و آمریکا: میانجی‌گری ما برای دستیابی به صلح پایدار ادامه خواهد یافت
🔴
عمیقاً نسبت به رویداد‌های اخیر که حاکی از شکنندگی آتش‌بس موقت است، نگران هستیم
🔴
چرخه خصومت‌ها را نمی‌توان رد کرد
🔴
از همه طرف‌ها می‌خواهیم که به تعاملات دیپلماتیک ادامه داده و به صلح فرصت بیشتری بدهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127085" target="_blank">📅 11:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127083">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/127083" target="_blank">📅 11:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127082">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6fj7UJIsOxBoYaCqdSM7tUW7dzzr9_XLjmFgwYam8QU6mVHDPBfn7MWDbcocXIumAemYxP0PGRzd4UHZkfqjzKH_Fq_lcF8RNBo2wmu5_NxSkl_xvA3IwN469-m2UOS7Dy77u02OIv9N7W6f34MpKm1kx4NQvF4_MntqT_1b8aE7HWA1RN2zD-FUaeR5RL3a9_i7Y03JLnNo7cddoFaCWgxszYiatq3pARlvU_PpEeloRJkXSDS2mEjl7smftbVshKjpppXTMc4oh5MGwANwg2pIi3NkQYpOEDCLlCcTe8tMQOwfq_ylcKEEN14FtJZH9jFc3Zzr-9a3Zrh5wBbIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه وزارت خارجه در خصوص نقض آتش‌بس توسط آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127082" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127081">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع دیپلماتیک: مذاکرات ایران و آمریکا همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127081" target="_blank">📅 11:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127080">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8736eceb33.mp4?token=kW5JxdaYD_ccZRNahClY5MFPtb9Ks4cFzJSHPgFiqGfxSnEuBlQRan4brDpPXr_7iX2T7LbaRffRKDYKKUfuwHE90sbQhVL5_FseO-dcYiIxOqufunIWQskfMMgX_VSEZ1P4krZiDM1CluDPT4LMv92gh8W2Xi9RA7KqHuoy_D4ZTs52XSB5VSLsYHffe7RIEgzDr3h-nFUMI-4dgxOGtIL0UDveFxjuCs1UIxtn6aLeFSZqSDl7Ou4DwTSk28qw2EU-ic4aoqKISiLRIJbPXIqaM6oqJlogj41EynvPuhmPxlVmvoSlW7-PyMxBVOrOr3omwJz7WiX_Us4cdQ4BCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8736eceb33.mp4?token=kW5JxdaYD_ccZRNahClY5MFPtb9Ks4cFzJSHPgFiqGfxSnEuBlQRan4brDpPXr_7iX2T7LbaRffRKDYKKUfuwHE90sbQhVL5_FseO-dcYiIxOqufunIWQskfMMgX_VSEZ1P4krZiDM1CluDPT4LMv92gh8W2Xi9RA7KqHuoy_D4ZTs52XSB5VSLsYHffe7RIEgzDr3h-nFUMI-4dgxOGtIL0UDveFxjuCs1UIxtn6aLeFSZqSDl7Ou4DwTSk28qw2EU-ic4aoqKISiLRIJbPXIqaM6oqJlogj41EynvPuhmPxlVmvoSlW7-PyMxBVOrOr3omwJz7WiX_Us4cdQ4BCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از آتش سوزی نفتکش هندی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/127080" target="_blank">📅 11:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127079">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: ما حملات مجدد ایران به اردن، بحرین و کویت را محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/127079" target="_blank">📅 11:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127078">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptvFJRJPmUclezGMNbQN6pb8qkQ3MEqxdgqY5dMd93-ffMaXi129g9NFlx3vJm9KriHDW-o3hLP9PbPFpDYgZbl6NRrF7GAvt5OWLfWm83kWujUTqKUpvBy3KBw7UAqMOBD1eQLh3pFW_keJQiEGVwFwxNLbjMLKVQZC8rQjNMRdhKC9wZDuwh47J-oripdoHIZgMOu-o-dcQggPGeQR5os8cm2-m_7xYvbKV2_Rh0eYYvNqGgN3UkVaqb1zZB0vbYpGTkdp6TyHu_cItywcyXAxNl1RiMIbcPPi8C9QUBZj_W9076k2MHT48sGJgkGpOLGUiYKZxWUhbn1Otuaz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاهکار جدید رستوران های تهران:
پنیر+ گوجه+ خیار+ گردو= یک میلیون تومان وجه رایج مملکت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/127078" target="_blank">📅 11:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127077">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">😳
هنوزم ۱۰۰ و ۲۰۰ گیگ رو به اسم نامحدود میفروشن؟!
🚀
مخصوص جنگ
😎
@NetAazaad1Bot @NetAazaad1Bot اینجا از اون خبرا نیست
😎
⚡️
💎
نامحدود واقعی، بدون استرس تموم شدن حجم
✅
مخصوص این روزایی که اینترنت پایدار از نون شب واجب‌تره
❤️
🚀
فقط امشب با خیال راحت وصل شو و…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/127077" target="_blank">📅 11:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127076">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zz0yKthiaxwQUm5zeNuiZnvMFiUWs-r5__SzuhnHCe8EC_tFxVez8S3EzUfxvy-_6nEYKgYQyyESwzyPFbIUocd4LoxHfsaiomeQaiXKq2OHJYwmdrExd7hiyu6ypt_Pmkzsj-pVF82h4osw03N9fi0_ZQr0fQICIY4bQ3wPbYvUWRvuA42vdLBF1KEy6U2tZaQqPCrcdpEAivT7IPwHIT5D_KeBGBNFdGS9TazG4AvuJ1HFlksVWBPlB8XuHKme4ZxYy9uF0vO7UawmDH9Ptih6UNGIsk56hrAaVJW0kAdfQ9NsvIIL3z0V9G6lIwmPd-jDMF6YNyN6AymVSSOvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
هنوزم ۱۰۰ و ۲۰۰ گیگ رو به اسم نامحدود میفروشن؟!
🚀
مخصوص جنگ
😎
@NetAazaad1Bot
@NetAazaad1Bot
اینجا از اون خبرا نیست
😎
⚡️
💎
نامحدود واقعی، بدون استرس تموم شدن حجم
✅
مخصوص این روزایی که اینترنت پایدار از نون شب واجب‌تره
❤️
🚀
فقط امشب با خیال راحت وصل شو و لذت ببر
⌛
ظرفیت هم محدوده، جا نمونی.
✅
@NetAazaad1Bot
@NetAazaad1Bot</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/127076" target="_blank">📅 11:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127074">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7ZRfhIwrqgMOurDGJOzQm_-yIw2VYREc51Ym9icDctYDOIeeQJGLmSMGtDz5XNyrFSTaz-G66dcp47_dqvarhXUDnax0sBgLYz67XVtgPYmOC2XS3sN_gpadoYUakT0rjvFN7sXJWl1Gl53vEU7ftyjhTEJE477pe4t0VGFtRwADx_G6BWXxKT2a6rUx6La8rEJQ83IgU_4tlKEDPT8Ypd1M4yP--t7aLZq-npB3aTHPsMmb9B3dhMnuUoBBrI61tgOj6meeYCzAj2sJKT3mZsXTijLzll0jTbBZIwPOIKAhwy-uXyNrmTnhFVmM1KnBpVgOHMW7sbQtHLcsoM-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-fNmlNUlSFGY0oLqxmmCfa4I3RNuV3nPBADzuLXyYKrB-zq-sic0q9fO_SzCrmkHnaQOJHhXW1S_C1F0rFWMCRYl9VbXg6EnmDcGe1oS7yyB864UCwOqpkiZpzbUFbV78mgBibbf5Zz59ZU7apbmWZgZskTCSI47HzxnPhh_k_tB5Ts5Gn3eh09oaP9pSd9XhfzGJp3VoRETQfv31ZA72S1SjfTs-iBzyTXoKh1hYiBsjQPpGug2fLGkou1Y15hIXXwtGCMZQCBqyLn6PLk2YmN6nTFV8IRdbndA_rTxKQZD9Nv_uWAWc9h1NTCOKTMv6e3EJsgofxGQFRHlDRGWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون اومده آبجوی ۴۸ کشور حاضر در جام جهانی رو خریداری کرده و کلکسیون تشکیل داده.
به عنوان نماد ایران ایستک رو خریده.
یکی نیست بهش بگه اون آبجو نیست داداش.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127074" target="_blank">📅 11:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127073">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رسایی:
این اینترنت بی،صاحاب رو یکی قطع کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127073" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127072">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtVoZVH5te6CpaFvIpX_lHJBPkUXuU-bez1jei0042BqItFEozRqlkw_6J6zfbr8__m8acVkZ_o3wHLVl_kjPVtIBFpbkbwFRm7IgSGeEAFufZU9MNSX_2TK22_2OqA6x4V8i0n8ZkuUHLFUJ8bTE4ea7z3_yoF5W4umrvUgVsrRDHswdg9yMUacHGsAQlcIng6RkWwdf5PCSQ7TASHjj1dBsJz1spCiWODqnTMpuHshi1H52_IITM5YJYQf4STyMn76slXXROT-Vx2q-NJXr4rmpWTsxRF4JBmmJ0e47anMSMciYaZB2_VgAZaK74cHb3_KfVTycPKzFNUj8WQ64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: مطالبه مردم حمله پیش دستانه هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/127072" target="_blank">📅 11:04 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
