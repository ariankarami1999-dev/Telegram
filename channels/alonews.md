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
<p>@alonews • 👥 982K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 05:12:38</div>
<hr>

<div class="tg-post" id="msg-127284">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یک فروند جنگنده اف-۳۵ آمریکایی بر فراز امارات متحده عربی اعلام وضعیت اضطراری کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/127284" target="_blank">📅 01:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127283">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
پیگیری خبرنگار فارس در بندرعباس از منابع محلی نشان می‌دهد دقایقی قبل نیروهای ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه شده بود را ندادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/127283" target="_blank">📅 01:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127282">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
صداوسیما: دو انفجار در بندرعباس شنیده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/127282" target="_blank">📅 01:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127281">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKgeDm25op9ms1lBnHFYMFwODnc8ouPO_mIwZH27NYcWcdAElh8Jy_WTPXw4DQb-VNB-kEngSFlQdg39sCNjUmR5RLVX0V5UBSPPCakCuuxMtaYwZ2gJOjHQJ3avA899F3S6U3kDNbHNYcNwDQ8CJkyfEVDLtiR1X5LOBjKqxGBnbTYpVHZfIU3EZRMBhmjubuMA-8JXYchJc_Sq_b4hSL9dmyvL9pnEa6ombB6v_r3g5gMosyvZ8OWyUFSio1dZNgw3lkOenUkqXx9eQ9NhCa0bli1hPJ7199JJJbX8OIGb2L4Rcc5YgCECmVvYwdV29V5-eoHrV3344YtMt8vsWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند جنگنده اف-۳۵ آمریکایی بر فراز امارات متحده عربی اعلام وضعیت اضطراری کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/127281" target="_blank">📅 01:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127280">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
تسنیم: تاکنون هیچ برخورد موشکی یا درگیری در سیریک ثبت نشده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/127280" target="_blank">📅 01:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127279">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم :
تا این لحظه، متن تفاهم‌نامه هنوز به تأیید نهایی نهادهای مربوطه تو ایران نرسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127279" target="_blank">📅 01:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127278">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
صداوسیما: برخی منابع آگاه صدای انفجار را مرتبط با مدیریت و بسته نگه داشتن تنگه هرمز می‌دانند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/127278" target="_blank">📅 01:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127277">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
صدای انفجار در سیریک
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/127277" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127276">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
امواج مدیا به نقل از منبع آگاه سیاسی در تهران:
🔴
متن توافق شامگاه چهارشنبه آماده و نهایی شد
🔴
دوحه با ایران و آمریکا در تماس بوده تا زمینه دستیابی به توافق را فراهم کند
روند اجرای تفاهم در صورت تایید نهایی، آغاز خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/127276" target="_blank">📅 00:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127275">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
صدای انفجار در سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/127275" target="_blank">📅 00:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127274">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6mFzkEThsy0lrjJ6_e2CaLf3LsIUw4NQF-4GEIPb7eiCC2sBqduxFLELWl1RoOnTiVgm2iAAn329HD2oVNWgM8FzkhcOQScid2_rm16bP44H3InEbhN3xgImrPQROTz0SzzHHp30wUkzkqaxvuZUohLFibM0rbdkxRe7xhtx_E2vOjMu5oy7LtSeHs9tRxl3QbM2qgvOe9lylSdmy7hldO1eJvLnZKQgoJUR8aI3YEcxcc5OmESfFcuc-qNkB9LYBT_646pBoQ7gj5Uo6y3QTiIdwU4joAdUidXVLgQvjAi55gXF9E0_BTQp-VDcSTkdyxLkaSk0OTxaa5m45fiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مکزیک فاتح افتتاحیه شد
مکزیک 2 _ آفریقای جنوبی 0
@AloSport</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127274" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127273">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
اکسیوس، به نقل از یک منبع: نتانیاهو هیچ اطلاع قبلی نداشت و وقتی ترامپ بیانیه اولیه خود را در مورد توافق با ایران منتشر کرد، غافلگیر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/127273" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127272">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VimB8cl-ELGvz57V7sWU2Nb5DZEgZQbv4TPPUQZVVDquHEK2QpWa6g2dVUBEo4Q3fzHZMLEOckP1uzNGFm-XW5up0vorztL94eRRqOcyWbOCldc8mLTsnitr3upKvMQWJaF3-cmVRNU92H_81Em1NRb5cFereg-6cdyr364P73yfENIQ8QWHOFOmGel4kJProwA2jEKlGo09oduEpiYXVL1lz_2Vlj5Z0qbHmaiAyzrHDRGKwqQG4FmlM88c9ThHTUxnNWX-BUd3JYR8zFxanZ_subuRBmCIvDQn7oeXRxING1cHwsUG8jX9-2h0hv2C5CLUm98ruVQQSbxgfpYhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم دیشب تو شبکه افق گفته بود فکر نکنم توافق بشه و یکی دو هفته جنگ رو داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/127272" target="_blank">📅 00:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127271">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خبرنگار: آیا رژیم ایران عوض شده؟
🔴
ترامپ: بله، نه یک بار بلکه دو بار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/127271" target="_blank">📅 00:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127270">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
واشنگتن پست: توافق قطعی شده و بزودی در ژنو یا رم امضا خواهد شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/127270" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127269">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
واشنگتن پست: توافق قطعی شده و بزودی در ژنو یا رم امضا خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/127269" target="_blank">📅 00:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127268">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
العربیه: آمریکا دسترسی به دارایی‌های مسدودشده ایران را تسهیل خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/127268" target="_blank">📅 00:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127267">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الان یعنی با قاتل  حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/127267" target="_blank">📅 00:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127266">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ :  ما این جنگ رو از نظر نظامی خیلی زود بردیم، تنها چیزی که نبردیم، رسانه‌های فیک‌نیوزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/127266" target="_blank">📅 00:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127265">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بقایی: تا الان ایران به جمع‌بندی نهایی درباره توافق نرسیده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/127265" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127264">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ : تنگه بازه؛ ولی این تنگه‌ها از چند ماه پیش هم باز بودن، فقط شما خبر نداشتید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/127264" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127263">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بقایی: تا الان ایران به جمع‌بندی نهایی درباره توافق نرسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/127263" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127262">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
اسپویل نوحه جدید در تجمعات:
برادر برادر امضای آخرو بزن
به رسم عقیله امضای آخرو بزن
غیور دلاور امضای آخرو بزن
به امداد زهرا امضای آخرو بزن
بگو یا علی و امضای آخرو بزن
به اذن ابالفظل امضای آخرو بزن
تموم برگه‌ها رو بزن
از هیچی نگذر و بزن
جای مقررو بزن
حیدر یا حیدر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/127262" target="_blank">📅 23:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: می‌خواهید آشوب ببینید؟ می‌خواهید مرگ و ویرانی ببینید بگذارید ایران سلاح هسته‌ای داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/127261" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ: آن‌ها در سومالیه قانون اساسی ندارند. آن‌ها پلیس ندارند. همه‌ی چیزی که دارند مردمی است که دور می‌دوند و به یکدیگر شلیک می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/127260" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
دفتر نتانیاهو: رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد.اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات شامل حذف مواد غنی شده،برچیدن زیرساخت‌های غنی سازی،محدودیت تولید و برد موشک و توقف حمایت ایران از گروه‌های تروریستی وابسته به آن در منطقه باشد، ابراز قدردانی کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127259" target="_blank">📅 23:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
مجری شبکه دو:
ما باید از دشمن بفهمیم چه خبر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127258" target="_blank">📅 23:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ در مورد ایران : این یک تفاهم‌نامه بسیار قوی است. این کمی مفهومی است، اما چیزی است که قرار است انجام شود.
🔴
و اگر به هر دلیلی انجام نشود، که نمی‌توانم تصور کنم که این اتفاق نیفتد، آن‌ها به اندازه من یا بیشتر می‌خواهند آن را امضا کنند. من می‌گویم آن‌ها بیشتر، شاید خیلی بیشتر می‌خواهند آن را امضا کنند.
🔴
این یک تفاهم‌نامه بسیار دقیق است که توسط بسیاری از کشورهای دیگر که تأثیر زیادی بر آن‌ها دارند نیز مورد توافق قرار گرفته است. و همه می‌خواهند که انجام شود. پس قرار است انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/127257" target="_blank">📅 23:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری / نورالدین الدغیر خبرنگار الجزیره در تهران: دیگر همه چیز قطعی و تمام شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127256" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ : ایران به‌هیچ‌عنوان و تحت هیچ شرایطی، سلاح هسته‌ای نخواهد ساخت و اقدام به خرید آن نخواهد کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127255" target="_blank">📅 23:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ درمورد توافقی که از آن حرف میزند: آنها به اندازه من یا حتی بیشتر می‌خواهند آن را امضا کنند. می‌توانم بگویم آنها شاید خیلی بیشتر بخواهند آن را امضا کنند.
🔴
این یک یادداشت تفاهم بسیار دقیق است که توسط بسیاری از کشورهای دیگر که نفوذ زیادی بر آنها دارند نیز پذیرفته شده است. و همه می‌خواهند این کار انجام شود. پس این کار انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/127254" target="_blank">📅 23:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2x5-A6mKJxvTpLflP7UP5rPiFdcYAvC_FpjjBj10XBNNhSkS4EOm6s88mABysf20E2cT_nQy1JJfNS6xQrRMEbNIJgttTpePMSFWgzQBSF3igmjoDO6dZeJL44-dOCabZ6gAw9HVNOCrniWyFRV85jtjp_99l9EWNxgH16Uk9IzYKZBfHHdMpLM-ycJDd6WDjenHXRPxwc0hCno7x9tSy6tmEndGaOeuVa3jHLv4vVwgwCdg7jevao5FCjxYvVHSodr0ocklZ9BtO5eEilYPfbl0ndqJO2sQxWaREo0otpQjVF0xu6DQ3xMo4S_wIq5j305ycQ8CDmsf0kAwuTf3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسماعیل بقائی سخنگوی وزارت خارجه: از شبیخون حوادث لشکرش در هم شکست، هر که صائب در مقام صلح، طبل جنگ زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127253" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ: عملیات جزیره خارک از دستور کار خارج شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/127252" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
خبرنگار: وقتی این توافق امضا شود، آیا آمریکا فوراً محاصره را لغو خواهد کرد؟
🔴
ترامپ: بله، این بخشی از توافق است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/127251" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdc227ec7.mp4?token=P-Ry2z9-TPyiFP2XotOye-tmjuZgfDJMq79NJ3KcD18WWYZ-1jbfOi7hjnaB-SceDQ2WGO2sjUesRhzvlsUdF0UNuGA-9SajM90knbSd2OnFP59zi5nLaHfXnAVH3e8ju2rF2Y7YMuthqcceps2UmCfzYy0HqugSLAQK5gZVIxxhxE327yLFtrC3JVlGWx73c51xcddGOnbHm-R2VtXW4DDYgjhExevP9e66r-QejTljJfwutlg2MT2k3aozlfyBoy859YGYgzl23QmWsNwID3F9HP21EPodgPNgHJwMGSgUcPNC741SoH1-dEz4_TUGxjkMf-_YCkcxgQixnSVkVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdc227ec7.mp4?token=P-Ry2z9-TPyiFP2XotOye-tmjuZgfDJMq79NJ3KcD18WWYZ-1jbfOi7hjnaB-SceDQ2WGO2sjUesRhzvlsUdF0UNuGA-9SajM90knbSd2OnFP59zi5nLaHfXnAVH3e8ju2rF2Y7YMuthqcceps2UmCfzYy0HqugSLAQK5gZVIxxhxE327yLFtrC3JVlGWx73c51xcddGOnbHm-R2VtXW4DDYgjhExevP9e66r-QejTljJfwutlg2MT2k3aozlfyBoy859YGYgzl23QmWsNwID3F9HP21EPodgPNgHJwMGSgUcPNC741SoH1-dEz4_TUGxjkMf-_YCkcxgQixnSVkVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا رهبر ایران این توافق را تأیید کرده است؟
🔴
ترامپ:  تا جایی که می‌دانم پاسخ بله است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127250" target="_blank">📅 23:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEWv88COBnhP2fhgm0fhwMZYHljaJmLn_jZCfbWfIxQimP2qJxbPAFcnGN6yEXoN9ipcplPeBsrVhCseEfuOhJ7RD73T8eFUq0PoktJRzfOBZbHl86UquMAJOSiHN3lj5RGUVAn2Y3HdAblV7c6jIOzx9obzmcS8YQRBmfttAtNUNcxQV3CPJojDgmnrV7zbyGVxpotghVodADh7dGiZnztKCWjm6OQItJzPu-sziLRFLj8PYJx0AA4cd3ARPQJvJXgnKWdUN8cD0mxhnZ30C96MtuPcmdIVShIA2ON1aP4FGrQwRZgndSdAoJs1RWScl6BC3uHbNtqiqAqXfWnY5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای سوخت‌رسان KC-46 Pegasus نیروی هوایی ایالات متحده از مبدأ تل آویو درحال پرواز بر فراز خلیج فارس.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/127249" target="_blank">📅 23:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bh_IZfVfibm6F6puduTIJCUuVJoXZTbLmekAwF-1Z3DizA440T-pzwuz7c9XHXkatJP-yMTaR_jFtvF2V8KXYBqjYMp__tmBzIx4AYFFz06RXwHJ4x38kZo6fpisBYyJaAbhdC8wa4YarANhr2PkxuUynZLupaUANPZoaAyivNgHNOkNBwHf0JNDCAexqpqGtkjR1PLIDbF9miwFwAtsJVFjTct0jRBgC05z7fpRz9cWL8bCG2JQo-aj5zYtJpdw5MApoanJ4GcGcahq2nd_Bh3OjBKxYwcavT1YE4nMX5M5FzqfXX8CZW07J5vfJ-Q7lG81rD2GUQ3k8va0JaEMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو فروند هواپیمای ترابری نظامی "C-17A Globemaster III" نیروی هوایی ایالات متحده وارد خاورمیانه شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/127248" target="_blank">📅 23:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksbalaGM7FucR4E0v4jZyP6SCwPgXMhmkxeNMaHTE3WhPqEgeA8C-n6cNJgxB-fKLL5K-d3d8sHgS4sFFe06TcK_VVjOIJFHgkygsBl6A48vyp6--YC2kE78tbuZEIgJe8aTUtHMRuvvdFACs-pTQ2W1ljkKGP4lL8kpbF-UH05w9J5qQmczOsPiTTFtKPhKjuyvOs7-L3U3Q_SFyKSef2wHPyyHEdZCV1G-rvipiRLhMNMUkgRBY0ZuVufK0cAa0xlHQnqPQobAzD1yYcpdh2YsGxlvr1jBy1nVJK8YUUEaYutGao7GIT4fRNOo4hro3IZCK3pBoJaUiH0t6Jaq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیما جنگ الکترونیک E3 هم در پروازه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/127247" target="_blank">📅 23:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127246">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTGydzLUyYNl_UyC8gIYzpMoErSWZYTVtXgsCkQYNfAdmpyB9pez71jRvlfOcR2u60mFzttb8Lje8rh10cy7OwFyj6cOhU3cLCYhHawbFoZR2pHCrRs2guIRZrHOPEKpcS6DynXf5NmBrLE-PqelE-n-O5DcCKRjzTOEqwiPwuOPXIx8IFzBlQbRj54bgpK5bLhhQCbgfftKMMbZ0dug3lmysZOx2IcYR9JGzoLssFQECjis3M-rrcFpwwsgeTOpxYUeNxlOKXZyjzst53OwtkHizd8xJEKEXXQ95ekfkqWb7lklcdEBmpBYhNeZV-FLea_JCfaXdNPspYyJ89Tw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه سوخت رسان چسبیده به کیش داره پرواز می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/127246" target="_blank">📅 23:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g81jfB6lH5uQoMii6ZuuUImMwUI1M8rqMtAcbvGqfxSwp-DYfDz9Wmm9zabbg4ifFROnd97ucLzfx1qQzE2JggK8SrcQ8sM-ABG8GnpozslOOhQDs6Kpmh5vSUnfqeEUAz1tmOEqIqGsA2B5PyOBPRi8QHwh7t7rEcYNfhs_6lFZz8MGzQ2NRXvjPvTLediRTzybLD6UcuWirxd6IQqVqvEY3ZCztuH6Pn0HuRodS2FX1QkRfEyHdFlBuLctmVePG8r9mM-FyZfzVbi1zURUBscVPzQyVFyZqeUjltSLDt5Hh7ePHRdvodWmhWXP7Cl1KJ6KJQ2DmzYAgMqeXJU23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/خبرگزاری فارس:
ترامپ دروغ می گوید تفاهمی امضا نشده
🔴
ایران هیچ پیش‌نویس توافق یا تفاهم‌نامه اولیه‌ای با ایالات متحده را تأیید نکرده است، که با ادعای دونالد ترامپ، رئیس جمهور آمریکا، مبنی بر موافقت تهران با متن نهایی، در تضاد است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127245" target="_blank">📅 23:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127244">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127244" target="_blank">📅 23:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127243">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vS8vS5RfLfT3mmkcF0_j0oxDMRoOJos_xob3O-XRvoGLLrfRDeJ0GSD3vae9G97ShkIo3XnX_emzhwwX8cOckyJLZCaCq6eSGBBHCZDujAqe1CCWhP_0waJAw61DlvAPP58pRE48qsh__rFdmqCCGVhVIRmXxwQly9IOqBuPbs42uzlC-l1ghaXyaTm5DdKGO5WfA2Wyu1yHHB97N08wuuPZolHtFTj9IYXty3-wiQD9FSr0bxwU1Z7saEGc0VpYaTuMxowbobU7dKg3IiJEIzsCKiMYUog9FY1OFcBFALJAaFGSohloXHqb_nzCDa15mWn0TE5LAIrOjVmE0Gm3Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/127243" target="_blank">📅 23:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127242">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سپاه پاسداران: اگر امریکا تمام خواسته‌های ما را در سندی که ارائه دادیم بپذیرد، به احتمال زیاد ما این توافق را تایید خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/127242" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127241">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ در مورد عاصم منیر:
«من او را "ژنرال" صدا می‌زنم. او یک ژنرال است. او ژنرال بزرگی است؛ آن‌قدر بزرگ که در واقع یک فیلد مارشال است، یعنی یک درجه بالاتر.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/127241" target="_blank">📅 23:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127240">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سی‌بی‌اس: احتمالاً تفاهم‌نامه آمریکا و ایران هفته آتی امضا می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/127240" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127239">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0273b84647.mp4?token=E1zadFWvjgwRK-i7OXbFVVlAMvbiAyYfYgx2lpgzdIhCT8gKJ3c_f0jbC8kuVoJS1B540lQ2UkILKB2gZpQdB4CMRjU9d3Am7PWzeViql6owbbAgJQJdTXW2-7lfoiGHP0VNJGKhisQJFKI67o0kKtHEOMsYpCKWVgwRzfGUf5hRPO6F86HXnP8TiZc210HXzFPqIK6CfGHyzmSWEOslolGqsRmVhmPa0AwbWUu9iMoZxOSzxmCawHaIqj8zk-DJqhWVUqAulk0Pr7rEkPJ83pjoJkipISE1xNDSa0qE3dQY3US6okEAkdO6UtOFl4Hr6-gM336shlt3y54BFgSVZiOHv6VLl1RHgcQKN1UcLfTVwet8hcSG-n7XeiuIWWpT72ucqjfpOkckq0NuAMqRcNWVbk4l5Rz2HiRv3QsSlUCv56S7b3EP4ZTYDMmXqZZEUa5k16trKh620qp8nqEWIKSElEY96bTHcw-RnbOiNYW3FbNDorQEOLQKG7tV6dFD7nZtOSwuArf79aewecbsSHsWbtXzHJbyFh-w7L12Tigh0AFSeUCJn0IVe0UAmJg6KZC5TBvVHVi56tm9mVSSvy3tGh6ZmCE_dNw0wswMhhzS--6my7VccucWFHQe_74RuIxY9TA9YUVSRpMthoz3SORpPddvJe8PnC9x99xm7pY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0273b84647.mp4?token=E1zadFWvjgwRK-i7OXbFVVlAMvbiAyYfYgx2lpgzdIhCT8gKJ3c_f0jbC8kuVoJS1B540lQ2UkILKB2gZpQdB4CMRjU9d3Am7PWzeViql6owbbAgJQJdTXW2-7lfoiGHP0VNJGKhisQJFKI67o0kKtHEOMsYpCKWVgwRzfGUf5hRPO6F86HXnP8TiZc210HXzFPqIK6CfGHyzmSWEOslolGqsRmVhmPa0AwbWUu9iMoZxOSzxmCawHaIqj8zk-DJqhWVUqAulk0Pr7rEkPJ83pjoJkipISE1xNDSa0qE3dQY3US6okEAkdO6UtOFl4Hr6-gM336shlt3y54BFgSVZiOHv6VLl1RHgcQKN1UcLfTVwet8hcSG-n7XeiuIWWpT72ucqjfpOkckq0NuAMqRcNWVbk4l5Rz2HiRv3QsSlUCv56S7b3EP4ZTYDMmXqZZEUa5k16trKh620qp8nqEWIKSElEY96bTHcw-RnbOiNYW3FbNDorQEOLQKG7tV6dFD7nZtOSwuArf79aewecbsSHsWbtXzHJbyFh-w7L12Tigh0AFSeUCJn0IVe0UAmJg6KZC5TBvVHVi56tm9mVSSvy3tGh6ZmCE_dNw0wswMhhzS--6my7VccucWFHQe_74RuIxY9TA9YUVSRpMthoz3SORpPddvJe8PnC9x99xm7pY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ما در برخی شب‌ها ۲۵ کشتی، در برخی شب‌ها ۱۵ کشتی را از بین بردیم. در ۴ یا ۵ شب گذشته، به ترتیب ۲۵، ۲۲، ۲۱، ۲۶، ۱۸ و ۱۴ کشتی را زدیم.
🔴
چه کسی دیگر این اعداد را به خاطر می‌آورد؟ هیچ‌کس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/127239" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127238">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / منابع شبکه العربیه: طبق توافق، آمریکا تحریم‌ها علیه ایران را کاهش می‌دهد و محاصره را برمی‌دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127238" target="_blank">📅 23:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127237">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ: با نتانیاهو صحبت کردم
🔴
من نمی‌توانم در مراسم امضای توافق شرکت کنم، اما معاون من، جی دی ونس، در اروپا حضور خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/127237" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127236">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ادامه کاهش قیمت نفت در پی اعلام توافق توسط ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/127236" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127235">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز بلافاصله پس از امضای توافق باز خواهد شد.
🔴
ما توافقی داریم که بر اساس آن، ایران هرگز سلاح هسته‌ای در اختیار نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/127235" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127234">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: موضوع توافق در روزهای آینده حل و فصل خواهد شد. احتمالاً امضای توافق ایران در اروپا خواهد بود/به زودی امضا خواهیم کرد، این باید انجام شود و به سرعت انجام خواهد شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/127234" target="_blank">📅 23:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127233">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
قطر: رایزنی‌ها میان آمریکا و ایران به احراز پیشرفت در تفاهمات مطرح شده منجر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127233" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127232">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: موضوع توافق در روزهای آینده حل و فصل خواهد شد. احتمالاً امضای توافق ایران در اروپا خواهد بود/به زودی امضا خواهیم کرد، این باید انجام شود و به سرعت انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/127232" target="_blank">📅 23:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سی‌بی‌اس: احتمالاً تفاهم‌نامه آمریکا و ایران هفته آتی امضا می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127231" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
دفتر امیر قطر:
ترامپ تأیید کرد که تفاهمات ایالات متحده آمریکا و ایران مورد تأیید همه طرف‌ها است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/127230" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
اسرائیل هیوم : انتظار میره ترامپ با نتانیاهو گفت‌وگو کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/127229" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سی‌ان‌ان: یک منبع اسرائیلی می‌گوید پست ترامپ در شبکه‌های اجتماعی درباره توافق با ایران، نتانیاهو را شگفت‌زده کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/127228" target="_blank">📅 22:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری/فارس: احتمال تایید توافق توسط رهبری بالاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/127227" target="_blank">📅 22:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15bd7379cc.mp4?token=lUpOny4PJpr9uJjM75mPtPbBg4QEKnSpLPNaQL8cQa6vriqZCqf8PkWtWOB1DB_5EfTS1tiSWB7N0dqeyd8go204rzRL6EHeZhIsLVigKDmKuq3Hgpo0rzQb1l1BiIfDu1SkuxUQ6LcGQtVL3w67MOtxb84jbKal0zx5_V3s7hQEHdQlRWji18fCaknlrZdtCbQk8aM1-Fx5aScwJcg6Du4lk7TKWMioBJR0i6GxWOuyisaLDLUMCQavqzPLQPB_ul_RBgvTz89Z9LkNaYcTyJAdJOKxzZ8Q_fehx83RBrD_JEW6F0Bm-mGz-cZ_gXWf-Ti-N-LajFMwfvWCzCCCs7dmYh6Sr66hq410eK2gL9ilf97f_R8kxvgPVmxOWkWmESHxdc2ZG6Kw80_t1z6ixAh6e2g7R4MYngxO_nX5S_aZ-AcJe26gn84GCA8Zga97xtxr9TxwNh3ywhTBO6iqwvdZ-KTN5DK39ZRIsVRmbL4MPybrRAj1XqTvwo54mQQexWplpsFzCAWYOw-BHGtg-FAWjkgGTMMH62Er59jT_z384N_O1fIaj85XNW1Vp1a6dbt4BzNgzotd6sa5i45SIQ92EA6AqYIc7DJkM89v7b5dxlUyUnZp0IZergp53oMWZjLWffWBWd5Y4KmseZE01kip9cwglPnYKWLiYsbYslg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15bd7379cc.mp4?token=lUpOny4PJpr9uJjM75mPtPbBg4QEKnSpLPNaQL8cQa6vriqZCqf8PkWtWOB1DB_5EfTS1tiSWB7N0dqeyd8go204rzRL6EHeZhIsLVigKDmKuq3Hgpo0rzQb1l1BiIfDu1SkuxUQ6LcGQtVL3w67MOtxb84jbKal0zx5_V3s7hQEHdQlRWji18fCaknlrZdtCbQk8aM1-Fx5aScwJcg6Du4lk7TKWMioBJR0i6GxWOuyisaLDLUMCQavqzPLQPB_ul_RBgvTz89Z9LkNaYcTyJAdJOKxzZ8Q_fehx83RBrD_JEW6F0Bm-mGz-cZ_gXWf-Ti-N-LajFMwfvWCzCCCs7dmYh6Sr66hq410eK2gL9ilf97f_R8kxvgPVmxOWkWmESHxdc2ZG6Kw80_t1z6ixAh6e2g7R4MYngxO_nX5S_aZ-AcJe26gn84GCA8Zga97xtxr9TxwNh3ywhTBO6iqwvdZ-KTN5DK39ZRIsVRmbL4MPybrRAj1XqTvwo54mQQexWplpsFzCAWYOw-BHGtg-FAWjkgGTMMH62Er59jT_z384N_O1fIaj85XNW1Vp1a6dbt4BzNgzotd6sa5i45SIQ92EA6AqYIc7DJkM89v7b5dxlUyUnZp0IZergp53oMWZjLWffWBWd5Y4KmseZE01kip9cwglPnYKWLiYsbYslg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه
مارکو روبیو
و مدیر عامل یو‌اف‌سی دانا وایت در وزارت امور خارجه بر سر دیپلماسی ورزشی و گسترش هنرهای رزمی ترکیبی در سراسر جهان، یک یادداشت تفاهم امضا کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/127226" target="_blank">📅 22:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0ad3ebf6.mp4?token=ADzMN_gCEI_FwDyrlkj958Xbi3gYsqRv-NpuE0CFquOvSTbdaT3eqnF9bJtFA7tTmtuTlvXaRpX1vNz9QEFSo4QDsbYjczjxYrbEwQ2QMGKGzVNUtTYu52sn_Ai73g_OYcrY_1lt9-QhoAtg89rpHiL4MTHbEgWaMAnBJgsl5Zj_tPnfQoLAGcBL9kkICNqTUbGN1Z0vUsxkIpRNCQ4spOjSNXEIECZbxYa4MVl3O50BkyWWd-CgaEcOsw0twJt9h4pYvY0ZonAEzXSbrPS1ty3NOdkMdU1NTBD1zggM6pYjIk3eKhsydCs6SoFgXP9QSonvqfs2rw3AR10fjahx0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0ad3ebf6.mp4?token=ADzMN_gCEI_FwDyrlkj958Xbi3gYsqRv-NpuE0CFquOvSTbdaT3eqnF9bJtFA7tTmtuTlvXaRpX1vNz9QEFSo4QDsbYjczjxYrbEwQ2QMGKGzVNUtTYu52sn_Ai73g_OYcrY_1lt9-QhoAtg89rpHiL4MTHbEgWaMAnBJgsl5Zj_tPnfQoLAGcBL9kkICNqTUbGN1Z0vUsxkIpRNCQ4spOjSNXEIECZbxYa4MVl3O50BkyWWd-CgaEcOsw0twJt9h4pYvY0ZonAEzXSbrPS1ty3NOdkMdU1NTBD1zggM6pYjIk3eKhsydCs6SoFgXP9QSonvqfs2rw3AR10fjahx0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه مارکو روبیو شوخی می‌کند دربارهٔ رینگ یو‌‌اف‌سی در کاخ سفید: دونالد ترامپ تهدید می‌کند که آن را رها کند.
🔴
شاید فقط میزبان مبارزات هفتگی بین افراد در سیاست باشیم و امتیازاتمان را به این روش تسویه کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127225" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f10af992.mp4?token=ntQNY66RESxT7znX1AVQbmRYk-LeonMgGGwjiBCCxwMimrCKPgestd69ItAFe6M_KvuqXwAYQk3xGlfQPRmtJrNuoIP0UyRKW3NtJmmP2vBUFLw-pL_6D3cqFdli3ZKBn7bMw6BhC6RsjBgyz5o7jiBctrjPXOe-TQQAv3bmXb9DNL_chSE4w46U-kZyBzkZnN5_gE67M3bhUWFr1F6Hfrhn6-Q_rO65tCTn_Cd6Exw36mgpAUN5sm2leuueSIe1esos5Ou5QSMhcz5z0_RQYwK9xp7U-l0VUpg-Setoq8jK9eJQwjWuyiO1KDj75JHDEVLe9AL6V-ZcMEVurjsbcQnQ98pyqmHAzVksd5BQE54jNj552wWbAQ5P8mB_Pq_LNyXWseCJyY7RrwTO1ATP8swJtDpbru6H_nkX9tfWvB2t5ngxYavd_s6DCFcVGdDfWUyDMp9nOfW0bXoK7NnJUWDhM_ZPduWm_XsxajF7j10SGQHDtZ5Q3wUYhu9To1cVNYwwOI38gm_CKBLeINW1lqZ5QhPK0I1PhRKPQxfR7iaUGkWERSMnGYo4ZX__DPMzsgnxfx8nUKTl2OKMYJ3PlcR8dwQHuNS49-1G2rvjq0Ogx5JHoqvd0WRrGL-HrSjodNry8rcQOwk2Jf14tgVwTeNPFPu5IMHYfx56RYACArE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f10af992.mp4?token=ntQNY66RESxT7znX1AVQbmRYk-LeonMgGGwjiBCCxwMimrCKPgestd69ItAFe6M_KvuqXwAYQk3xGlfQPRmtJrNuoIP0UyRKW3NtJmmP2vBUFLw-pL_6D3cqFdli3ZKBn7bMw6BhC6RsjBgyz5o7jiBctrjPXOe-TQQAv3bmXb9DNL_chSE4w46U-kZyBzkZnN5_gE67M3bhUWFr1F6Hfrhn6-Q_rO65tCTn_Cd6Exw36mgpAUN5sm2leuueSIe1esos5Ou5QSMhcz5z0_RQYwK9xp7U-l0VUpg-Setoq8jK9eJQwjWuyiO1KDj75JHDEVLe9AL6V-ZcMEVurjsbcQnQ98pyqmHAzVksd5BQE54jNj552wWbAQ5P8mB_Pq_LNyXWseCJyY7RrwTO1ATP8swJtDpbru6H_nkX9tfWvB2t5ngxYavd_s6DCFcVGdDfWUyDMp9nOfW0bXoK7NnJUWDhM_ZPduWm_XsxajF7j10SGQHDtZ5Q3wUYhu9To1cVNYwwOI38gm_CKBLeINW1lqZ5QhPK0I1PhRKPQxfR7iaUGkWERSMnGYo4ZX__DPMzsgnxfx8nUKTl2OKMYJ3PlcR8dwQHuNS49-1G2rvjq0Ogx5JHoqvd0WRrGL-HrSjodNry8rcQOwk2Jf14tgVwTeNPFPu5IMHYfx56RYACArE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقدام جدید در جام جهانی 2026؛ بازیکنان ذخیره هم در مراسم پیش از شروع بازی شرکت می‌کنند و سرود می‌خوانند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127224" target="_blank">📅 22:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کانال ۱۲ عبری: از توافق امریکا و ایران بی‌اطلاعیم و از اینکه رهبران ایران موافقت کرده‌اند متحیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/127223" target="_blank">📅 22:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127219">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfUJ_XGgZhDU69h9y029P-ONSA_USFUgsVvWct3Ll0lM9-CJxa-93PnJF_2xJw6CpEzWwwqZhW7A5cukvv72VLp1CFedjX1As0DtC7qziotyDcCy_VcQNYJj6k9WTVkdBdpwjQEhQemUFHWvqUyBfw6jnz5edT7-8dkry_DmNUZfdjKGXRwlFoQKbch6OBT8ZjmnbFepwDiiSM_VU8EpKkBNFacsWHE4aHNPmBWq1WecGA0gse2o9HnMx6K0fVZedAhqPDTGd1YephQ9C2wHlHEnhr77UJkPo9a5AK2tRjLYKgfYKtrdh2oAbijEAFNRxIlQoYolVbz9y306N4fUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdYWRY3jJk70F5YHNOyPT1rlMKEOLMzYlE9Rn3gOYUgTgFi6FNjy3-xb1jWbvrhmLX6gywxa3_hSLk-XFve2p_hI4oEtlnIOdM-qQ4IEHkYjITNIQcmSuM5P3t22KJfFGE2jtcYz6FaiIvDLrivhm7nWo5CJa4e-49doAj6H7QFhYRoS_wJ-WYaUYBP0Zg4CYgatJdrMDgNkbVGk05y35gWvi1ypR7W3qSqzOvtTfSdvP2_TCFfca-VYFrnXwmRE0u9huke3_T7cfT2rFBeCODhCXUB1hgso4Q6cmaso9Ol1UVTAWvECdm3_fTvpRZFksEpJaIrmHTyT0b-21zJGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dl56VRQzaWU4fEnraFNsL6ovY8hO-hKvnSqLIE83_L-Qvn7Benqquae1Iu3e4vnE6MdgF34zbVJlmNSCzAEYrh7N5TFWpa3-lzzPfKSQeC6Ehmrz7xnkpONUyowfU-ljXxcVyCwYx58D7RO9jnV6_VxAcvx2yIrsN-Yj5Hf395ZpiJvhXkibkTBozLG0UIkS6g1SEXlzOKIMlxjVkdcs3zWSntPDvEveG5gJr_lKBWSGDWMvwITijlhYpYehJB9nWUbYLu_UghPRWk8OP9MGXV4sT_1RENVi0SBv7MTZDXWejP9dPRTeE71btZ5dSKnbctNTFk6KmpVAcDSad1p8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AemsZRsOejyzkFTZQVPGeeNL2sAlG88I2Y3OPzeRXBmAWCFA8XaLFC0yLhD9uDYadxTmxMFQ-Aoece39tZLL58ky53ecgPdlFNYfR-nAo8GONHE_UF_qop809BdY2VFHojwBmHMNaQ4di9s-4hRTprdmOzx11ufMMXS_oL_VMztapxPfvsXTbcoH3WP5lnfRcC9Tp-oU0kgDHTFu7inmgupd7QiTTUY6Q1lGR7ovbTTL0lQxe35EOhpvw0eS5MPbV5iDbDoC2uNxKk6Farys_tbGF111yheI9jUxQGTa6tQ6f0QbS-FbkCgurDRFTIiTC0USSMuJectZ3pehdbi7wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از مراسم افتتاحیه جام جهانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/127219" target="_blank">📅 22:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
الحدث: هیئت قطری در بازگشت از تهران، موافقت ایران با پیش‌نویس نهایی را منتقل کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/127218" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127217">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKrO_9QmlSxoFCwVIlo_DwTSGpdRsG5BPMvgZwgWZgh8vBfJ-GOTGF19DLvfIymEKCLQEojibaym01ENbmZD3D12zaw8bJZQa-u1TI5b_GxHhbKgsu2LQAJrz_JlH1H8biBFUw-3Ev5zNAX_D6b6gW01H29WYKVYj-qfMRffkSr5tW55lOFXufLAmloRY-3XqqHd3t3TuMFXxAU_kii0jxrmB9aL8j5CK6sakXI0r9ELsqsPnvMfTYq8XeY8HYHes09n10UOBTdnfl82EEOh1nSB-u-E8Th6IYqugR661XDyxdpuvYvYQahjOCIzQDBtpYstyjrrxub6qjSPBSiFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی و سیاست خارجی، ابراهیم رضایی: من یکی از کسانی هستم که خارک و نیروهای پشتیبان آن را از نزدیک دیده‌ام؛ پاهای ناپاک شما به آنجا نخواهند رسید و اگر بیایید، زنده برنخواهید گشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/127217" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127216">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نفت برنت: ۸۷.۹۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/127216" target="_blank">📅 22:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127215">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogBP_sKNheveKVi85X6D7qUVtV-NElA4zxR-A7IySTKHq9MY3LtXUjyy8I706Zpide4JiCCsJm6f5MNXy2yh_qmPtYeie_ZlKPlcw8xjQW8PrK5YkGvxUqlY9iDj07Sh0ZYAqJdoXDGdCTV4Yix6JS-1DntvUdLMZ4SyK17Lcg3dgHCxucQ08WgVw01vhJiR4c1Z8Y8WphOH_d-bnudpucK9lLpHxT9AqU-tkg0I2rTacIjghgGsRxGSrbFusFf1x47glC8H_sxBa8w-a0yAmIpRj1bmYZBKEkxtOwY2NnDK7G-WPBtt83gXWHeVmYcszo9m6rWkiMu0PUnzG6yyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🙂
شمارش معکوس برای بزرگ‌ترین رویداد فوتبالی جهان آغاز شده…
🙂
🙂
افتتاحیه جام جهانی ۲۰۲۶، همراه با تمام حواشی، اتفاقات ویژه، تصاویر اختصاصی، اخبار فوری و پوشش لحظه‌ای مسابقات را در ورزش پلاس دنبال کنید.
🙂
⚫
از مراسم افتتاحیه تا آخرین سوت فینال، همه چیز را سریع‌تر و کامل‌تر از هر زمان دیگری پوشش خواهیم داد.
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/127215" target="_blank">📅 22:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127214">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ادعای اکسیوس: منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/127214" target="_blank">📅 22:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127213">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نظرسنجی شبکه ۱۲ اسرائیل : ۶۲٪ از اسرائیلی‌ها به ترامپ اعتماد ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/127213" target="_blank">📅 22:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127212">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رسانه اسرائیلی : همه چیز در پست رئیس‌جمهور درست نیست!
🔴
هیچ توافقی بین سپاه پاسداران و اسرائیل وجود ندارد و اسرائیل ۱۰۰٪ هرگز آن را تأیید نکرده است.
🔴
تنها چیزی که برای گفتن باقی می‌ماند این است - به اعمال او قضاوت کنید نه به کلماتش!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/127212" target="_blank">📅 21:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127211">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
طبق منابع العربیه، عباس عراقچی، وزیر امور خارجه ایران، ممکن است در ۱۳ ژوئن به پاکستان سفر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/127211" target="_blank">📅 21:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127210">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
فارس : منبع آگاه: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127210" target="_blank">📅 21:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127209">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ_pLRavlgiainAGQrepR_Pt5khhR5datDLww_mi7Su4RXkUleOhl9WShWfE-gS3fwNrELutepKVjgIFxXCAqJVNWUys8nkN3r7FuShq6ZIV6craU6sWEyvlf4P4iAQUX_Zt2RqlYGBspFoF2cIV9K_SQFtG1TjldotsH7CuyHIz672WpJ5d8Dje7N6vrxpwUVcmm3h04_rC_sJZ5DZLowxZA3A1derpjrQpJaldJa1mqEuJpDdtJp5bBWf1ZS-es4xIYUngWs_N3mv5kOp3jF-FCvgO5PJPveJW8Lyxeh9kzRXdSUBvWQXy8HTgLYJjXkYhfaLcca3zzQT4NISDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیبالا تو ویژه برنامه جام جهانی فوتبال360: من عاشق ایرانم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/127209" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127208">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وال استریت ژورنال: توافق قطعی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/127208" target="_blank">📅 21:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127207">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سه منبع به اکسيوس می‌گویند که شکاف‌های کلیدی در مذاکرات ایران در جریان مذاکرات چهارشنبه با میانجیگران قطری حل شده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/127207" target="_blank">📅 21:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127206">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مقامات اسرائیلی از توییت ترامپ غافلگیر شدند.
🔴
یکی از مقامات به i24NEWS گفت که مقامات اسرائیلی در حال حاضر به اظهارات علنی ترامپ متکی هستند و تأکید کرد که اسرائیل پیش از تعیین صحت ارزیابی رئیس‌جمهور آمریکا، نیاز دارد ببیند پاسخ رسمی ایران چه بوده
🔴
او خاطرنشان کرد که تجربه گذشته نشان می‌دهد این ارزیابی ممکن است همیشه دقیق نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/127206" target="_blank">📅 21:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127205">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فووووووووووووووووووودی</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/127205" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127204">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فووووووووووووووووووودی</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127204" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127203">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سه منبع به اکسيوس می‌گویند که شکاف‌های کلیدی در مذاکرات ایران در جریان مذاکرات چهارشنبه با میانجیگران قطری حل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/127203" target="_blank">📅 21:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127202">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4B8e0fU3H_YB9RrCks3LK5Rd82kbZJ-VqShFedbud7D7XoUzL0M1X0ZOFzuHHwAcn2F8bBCKNBhnHKc0zwKh1oDE_06HbzLBhykaRQ_j1SWYtHs3LWVTV9Wl0sW6-PgBfY6EmrcoVwt1qtAIFt1_MlTpY-K-hJD0tRytfG27p6tXOpMSR3QgPWe4mzqMoCu0KEO6t6scxqo7eJGGxcIgNM4irjYz9kl8AVQBVtsnBVG7X7pgYhr_NGPXQYbdi6nM7vBMTSCT2avs_FiDxP4KbZUE2bvtb3jwVCtMH4goM7lSVIVJcMO2R3UbcHn8DDUybMXQiZlYtfWfWvuLYjTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت به زیر ۹۰ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/127202" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127201">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سپاه : ما کاملاً آمادایم تا به هر اشتباه یا اقدام طرف مقابل، با قاطعیت پاسخ بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/127201" target="_blank">📅 21:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127200">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
قیمت تتر ۱۷۶ هزار تومان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/127200" target="_blank">📅 21:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127199">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
صداوسیما:
ترامپ بازم عقب نشینی کرد، الله اکبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/127199" target="_blank">📅 21:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127198">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
شبکه کان به نقل از یک مقام اسرائیلی:
آمریکایی‌ها هنوز از مسیر مذاکرات با ایران دست نکشیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/127198" target="_blank">📅 21:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127197">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YscMO7U4LpYnCvAsGXCno5cZRK3dTf5Wqzu1elgmJt4IWVM4KsgptwLnK7Md_K-pJLIpbFGKPtXZrmMuSdIfGlNTI-ARNoVLsxB5HqzAiHDvvTwjMVuft_pag080rZUDA3-djCChGdUoE45ozmFOUWPzpeO2hJh8Uw3s3HwIb7APDS2wzi7ZlHXd_G8R5PXHhTo6r2yS9B7a1Np_2sawmEX9ahEiWMm46hssFAuX4PMKi7_mxg95vbsFP2xxQDyvY3HCkPqqXOyAA3VOqPRr0ksPYHGDwOn80yipcVMiK3gMwk-urSYrv_59uzLxTruBN0rRcmCuErSLCi4DwCnG8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ: حملات امشب رو لغو کردم
🔴
با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایرانیان برده شده و تایید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده علیه ایران امشب را لغو کردم. مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات فراوان، توسط تمام طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران، تایید شده است. محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل و با اثر باقی خواهد ماند — زمان و مکان امضا به زودی اعلام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/127197" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127196">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
کان: یک کشور منطقه‌ای در طول تشدید تنش‌ها با ایران این هفته و در جریان حملات هوایی نیروی هوایی اسرائیل، مانع استفاده اسرائیل از حریم هوایی خود شد.
🔴
این اقدام برای مقامات ارشد اسرائیلی که انتظار همکاری مشابه درگیری‌های قبلی با ایران را داشتند، غافلگیرکننده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127196" target="_blank">📅 21:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127195">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
العربیه به نقل از یک مقام اسرائیلی:
پیام روشنی از سوی آمریکا دریافت کرده‌ایم مبنی بر اینکه در حملات علیه ایران دخالت نکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/127195" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127194">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4056b84464.mp4?token=IhsVBsDvav-JIwp7SNQisBDpUJisFwP9UeGX1A_ZFI28GWQsmSZv1BlSDl_ZzxxrODzRqxWcCN6appnkUECzWsnQlOow4G0gPMsAjofICCq1mGT09v1mqPIfXvcqZuO7M4iqo0ODA_QP7CvVqqW6O_rt0R2Io7-lLfS-RIzaLXgHiGYpHxzqp9prDRtAYS3eoaVacOICoxGjD0o9dB5tWwKi0ZZJMLH8XAZMVNSqkeJknqq1upCkrFSMjOLf0dS8Q1_SnHkI_5q9wR9N96ifsW0mchTN8sFVAhnDBMNpXQEeawyEBo1g-7mTZUH4Ytji_hznPhKMn_eBk49BLQ5v_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4056b84464.mp4?token=IhsVBsDvav-JIwp7SNQisBDpUJisFwP9UeGX1A_ZFI28GWQsmSZv1BlSDl_ZzxxrODzRqxWcCN6appnkUECzWsnQlOow4G0gPMsAjofICCq1mGT09v1mqPIfXvcqZuO7M4iqo0ODA_QP7CvVqqW6O_rt0R2Io7-lLfS-RIzaLXgHiGYpHxzqp9prDRtAYS3eoaVacOICoxGjD0o9dB5tWwKi0ZZJMLH8XAZMVNSqkeJknqq1upCkrFSMjOLf0dS8Q1_SnHkI_5q9wR9N96ifsW0mchTN8sFVAhnDBMNpXQEeawyEBo1g-7mTZUH4Ytji_hznPhKMn_eBk49BLQ5v_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اولویت من همیشه تصرف جزیره خارک بوده است. راستش را بخواهید، نمی‌دانم آمریکا توان تحمل آن را دارد یا نه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/127194" target="_blank">📅 20:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127193">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از منابع آگاه نوشت: ارتش اسرائیل برای اولین بار از زمان امضای توافق اسلو، در حال تأسیس یک پایگاه نظامی دائمی در شهر جنین است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/127193" target="_blank">📅 20:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127192">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ab48468c2.mp4?token=K5NvysCv1qZiPBK1JlJZNiKfuvaDopaaci9oiNQLV3WmrnAdUozN0GXDdMYjThHbJ1nyxNurZk50D1TEr6SCVC_6q6Iek2pcBWWLqOGuEThZplwlEghEiTF1sGksnu7V5hC6etnrCntmPsA4Be8_f0ZDzZosuK7Ay_Bh7dEo7OtzC4bCYlrDHUzLnpcFykuwlJAm1el-VP3hU2Cpi58pH8_UM5BRURk47G22HtE7FiNYAqVoJewPYTZEDvZXuKSXarQuVTMZWVpoGBljtotBk5mh9gYpx7o7mPUZ-eHgZ4e5c7qBeJRyrKs4xgaqCBlPAVOOdZuTeI1IeWROr3X2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ab48468c2.mp4?token=K5NvysCv1qZiPBK1JlJZNiKfuvaDopaaci9oiNQLV3WmrnAdUozN0GXDdMYjThHbJ1nyxNurZk50D1TEr6SCVC_6q6Iek2pcBWWLqOGuEThZplwlEghEiTF1sGksnu7V5hC6etnrCntmPsA4Be8_f0ZDzZosuK7Ay_Bh7dEo7OtzC4bCYlrDHUzLnpcFykuwlJAm1el-VP3hU2Cpi58pH8_UM5BRURk47G22HtE7FiNYAqVoJewPYTZEDvZXuKSXarQuVTMZWVpoGBljtotBk5mh9gYpx7o7mPUZ-eHgZ4e5c7qBeJRyrKs4xgaqCBlPAVOOdZuTeI1IeWROr3X2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / انتقال تعداد زیادی از ادوات زرهی  توسط ارتش سوریه به مرز لبنان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/127192" target="_blank">📅 20:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127191">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل : نتانیاهو یه جلسه امنیتی فوری با مقاماتش برگزار می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/127191" target="_blank">📅 20:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127190">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: برای دولت کوبا عاقلانه نخواهد بود که تلاش کند به انواع تسلیحاتی دست یابد که توانایی هدف قرار دادن این پایگاه یا خاک اصلی آمریکا را داشته باشند
🔴
آن‌ها در این صورت وارد تقابلی خواهند شد که نه خواهان آن هستند و نه توان تحملش را دارند.
🔴
هیچ کشوری در جهان نمی‌تواند با توانایی‌های ایالات متحده آمریکا برابری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/127190" target="_blank">📅 20:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127189">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_l8HTSEO_c41GdHR4b9QuBEvfSyINQ4DaIj25wC05ZFuJ7CgjZgaw5qO3ps6VrKdImlxcNw9AtD8AvHAi0_wpqSvVd72JCSa0-hT6dHBxJIn4TVH6CWlW6cOGo_87THl5kmzvR4VhxdSovQFa2S08TsznS00fwMODZngfCJ5rOeg78fDQOENINNOnr3DzofInWwO3ZwBqomSK5XA2PKwBksFfW9GKDSWsM_gF-nBHto2vaqKIY_5SDrJAJQYVdmjuiQ9GUYsNI_w0cFA8o-P2N5nU07_ysGHlEb07oX8wRxJ4lJO-IChT8Hacm44pT5BnS2-rNY99EIDkQUqSjBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظاتی پیش یک قایق ماهیگیری در سیریک هدف یک پهپاد قرار گرفت
🔴
مصدومان به بیمارستان منتقل شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/127189" target="_blank">📅 20:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127188">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبرنگار الجزیره: حملات پهپادی اسرائیل به شهرهای کفر و تبنین در منطقه بنت جبیل در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127188" target="_blank">📅 20:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127187">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98745e731.mp4?token=q8jFjRVBQaKF9JFmWNv1nya5R-BswW1ZbNpWi47bfy8yOP9lo83E41ZOASKR4lpynlo03LbJARyDv7rvj8BVKNaY0mQIsBuVVUleASh0s4ubniGdvaFF84vEQc7STZlQj5wNcVk0lBgdBa-H0Z9YX7oynRD3h1IgtPbRJcg8rHPGwThQeExmIJyPTs37rjG8TKFwDPr36OOIarjIAPDaZJkCyA4qqy_jEocTVAU7Yu_KBAGz-4lQA6T6rV01s5sx7Pvlw501oYAZ6gqfIuGhSNbHGtPVlK8gCxsAbP0XnAIT5wt_vgJsqiilm2G05eKQK3bigdZg-rBzSPq1VZKwww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98745e731.mp4?token=q8jFjRVBQaKF9JFmWNv1nya5R-BswW1ZbNpWi47bfy8yOP9lo83E41ZOASKR4lpynlo03LbJARyDv7rvj8BVKNaY0mQIsBuVVUleASh0s4ubniGdvaFF84vEQc7STZlQj5wNcVk0lBgdBa-H0Z9YX7oynRD3h1IgtPbRJcg8rHPGwThQeExmIJyPTs37rjG8TKFwDPr36OOIarjIAPDaZJkCyA4qqy_jEocTVAU7Yu_KBAGz-4lQA6T6rV01s5sx7Pvlw501oYAZ6gqfIuGhSNbHGtPVlK8gCxsAbP0XnAIT5wt_vgJsqiilm2G05eKQK3bigdZg-rBzSPq1VZKwww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کمتر از ۳ ساعت تا شروع جام جهانی؛
درب‌های ورزشگاه تاریخی آزتکا مکزیکوسیتی برای ورود هواداران باز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/127187" target="_blank">📅 20:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127186">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlQ8ROelYuEXWzhj7NzRYraRQ9OFZci2fcltu91elbiRU7ZAp9HHYOhpgkXsA-xLm47WAD_Xlg04Uv-ge_GNXoe0yUPnZZUWa2S5G7uWgPkknNSk3FeO3o9AXgoCFjyYCMje_GJMl5roMsbSqJQXnQ6UHrrsy4FmfMpCxZXPeuI2djy_Zl-B_OtW0Ot0RzAQ94SH4anoap_t8_DdAaHcQettEKHnrgSoVVHwi4kRctMBu3Zb21EcEsgoZoZRMGEy8akyFhGqugLNdWl9WTTobDOjxFrLdc1A-arwI7UcicZ8n4AgnALqhlyS2WwczQ54XOaUOtjoLWFcY7r5tnA0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران تو گروهش در جام جهانی دوم بشه و آمریکا هم دوم بشه در مرحله یک شانزدهم نهایی جام جهانی باید باهم تقابل داشته باشن
🔴
و بدین شکل ایران و آمریکا در 3 تورنمنت متفاوت با یکدیگر رقابت خواهند داشت :
🔴
جنگ ایران و آمریکا؛ هرشب ساعت 12 شب به بعد؛ از جنوب ایران
🔴
والیبال ایران و آمریکا پنجشنبه 4 تیر
🔴
فوتبال ایران و آمریکا: جمعه 12 تیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/127186" target="_blank">📅 20:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127185">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی سپاه: اگر آمریکا می‌خواهد شکست‌های قبلی خود را دوباره تجربه کند، پشیمان خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/127185" target="_blank">📅 19:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127184">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDA1lkd5R5XMcdcplMLWUngueG0_5wDejEG1VQGUPZeOi5dHpqRBc3l3edaWOM-OmeRDB5zqMSm8abtlfRdeEMEGGVDMOH9U7Do6uPmEL9WW8VKOoE7wfGy0z2UZCFvlhJl4mZBA6SLsbJCBRk3jnOBTkfCJ2j2bO_8MsW4SclRJ7126nNG-acScw6Y6d9yyFW_g89Nn0hnjCyDWH3MtYpOfFf61dLYdLyQc4-z3PRYe5XU8GzbJIojkoruySyOx-kZAj5And7eegndji0N5ePLNYfTZdmUdWIu-n5P5oqhFwVQTEaruW1V574PjYzwhOOHWIPr5gz49jK_415w-MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام:
تنگه هرمز همچنان برای عبور و مرور باز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/127184" target="_blank">📅 19:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127183">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مدیرکل مدیریت بحران استانداری آذربایجان شرقی: حادثه خروج قطار خاوران از ریل در ایستگاه ترکمانچای رخ داده است.
🔴
این قطار از تبریز به سمت تهران در حال حرکت بود و در این حادثه  یک نفر مصدوم گزارش شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127183" target="_blank">📅 19:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127182">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38adcb12ff.mp4?token=o7XBfsYsci730njTb-p3C_z5EevTbZrYVOW71ND38u4cQXFAsa0q5A199MjeRWb17sO2Xn--pdoP1gwZpRtqxmwbjub2AOXUIrwKAC0B-n-TX7zEh8ysWKASP5CyMcnNSBDX6qzhHKo6CireNWTuMS7eL89ohYOEkdFAkqD1Ra8S8j248KDLBUuTn8_uXGjf5Ojp4GvQKM5EWhJy6oCYW1bhCr5nPDLYedbaiyYDD5X4QVvM_EogodqiRNmMJT6E9cg46hbJudNIyQgH-FTZffoMXmn6asuM9wPDItuhK7yiRZQ21bwKO6DODViIBdtPUexybb8M9CHmrxXrjQFPEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38adcb12ff.mp4?token=o7XBfsYsci730njTb-p3C_z5EevTbZrYVOW71ND38u4cQXFAsa0q5A199MjeRWb17sO2Xn--pdoP1gwZpRtqxmwbjub2AOXUIrwKAC0B-n-TX7zEh8ysWKASP5CyMcnNSBDX6qzhHKo6CireNWTuMS7eL89ohYOEkdFAkqD1Ra8S8j248KDLBUuTn8_uXGjf5Ojp4GvQKM5EWhJy6oCYW1bhCr5nPDLYedbaiyYDD5X4QVvM_EogodqiRNmMJT6E9cg46hbJudNIyQgH-FTZffoMXmn6asuM9wPDItuhK7yiRZQ21bwKO6DODViIBdtPUexybb8M9CHmrxXrjQFPEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پنتاگون در وضعیت قرنطینه؛ تیم‌های هازمت برای حادثه مواد خطرناک وارد شدند
🔴
پنتاگون ساعاتی قبل به دلیل «حادثه مواد خطرناک» در قرنطینه قرار گرفته و تیم‌های اضطراری هازمت (مواد خطرناک) برای بررسی وارد ساختمان شده‌اند.
🔴
طبق اعلام آژانس آتش‌نشانی و خدمات اضطراری شهرستان آرلینگتون، واحدهای این آژانس از جمله تیم مواد خطرناک، در حمایت از تیم هازمت PFPA (پلیس پنتاگون) در محل حادثه حضور دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/127182" target="_blank">📅 19:36 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
