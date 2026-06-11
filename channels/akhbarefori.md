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
<img src="https://cdn4.telesco.pe/file/HmsxHDhPuocH5cLFOPCvFIc55pEw_CRRkdzsNxfnSnEqjy7OpHOSuwlEsUBkh67PqGqU5hDTkl4rB5Q9vxXvKMKLv6LqdcxscMulP84h2KNLgXkBhII4fIHBEoz1bHjLxN3jKjFok8KYAgJ6DswJpwAQGuE3X456q8qNPTr0fEp0qPuZfRDvp5K1fvhL7yCj8ht_EGzmLjZWHAXstADl1wzS8KH97mDIk2QsXWZsT0CW8vECZLYrFntijYp8NVViu7BZlklop2DsL_fMfifldgiuXCH8VacErZ9jHEUREpL9LIwK6Ynzkau5UXtsHtGw8p86lEidJ4WEpuw6G_WKZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.6M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 10:53:40</div>
<hr>

<div class="tg-post" id="msg-658369">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
۳ مصدوم در حوادث مرتبط با حملات آمریکا در تهران
رئیس اورژانس استان:
🔹
در حوادث مرتبط با حملات وحشیانۀ امریکا در استان تهران ۳ نفر دچار مصدومیت شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/658369" target="_blank">📅 10:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658368">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا در اردن
🔹
سفارتخانه آمریکا در اردن طی بیانیه‌ای ضمن اشاره به حضور موشک‌ها و پهپادهای ایرانی در حریم هوایی اردن، از اتباع خود در داخل ساختمان‌ها بمانند یا در مکان‌های امن پناه بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/658368" target="_blank">📅 10:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658367">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257539272b.mp4?token=lhiPBtABYb0uI5Sq5vCWJnKlz-BezLcTf3os3y6f4CuFn-9auUjrc7gNU3DO1ngJqjsfHNEfF5vmG14A_yqd-JhuOlk_U6KsyQ0WqucB7lkow0rC5oj-GNArJ0YHRO9Nf1fUyPEj7azWXdm7IaJA_04Y21P7sTwUeAzxtNeiTvofxqiuq8vy3xACiR1L8LlzzZPrwrLxC1FG_jSKokEPk4Jd7azkZEZts9btdCiPmv-LiSqJSzwf45HaYu39fsmmQQB0FeSvKHK9Bu3XEjBm9QdEVGt_VD-T3C3a9mAYXfL00Bm3oIVsVwn7ZgwLO4efvHE_gv_GfL3gCzPxqqLU7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257539272b.mp4?token=lhiPBtABYb0uI5Sq5vCWJnKlz-BezLcTf3os3y6f4CuFn-9auUjrc7gNU3DO1ngJqjsfHNEfF5vmG14A_yqd-JhuOlk_U6KsyQ0WqucB7lkow0rC5oj-GNArJ0YHRO9Nf1fUyPEj7azWXdm7IaJA_04Y21P7sTwUeAzxtNeiTvofxqiuq8vy3xACiR1L8LlzzZPrwrLxC1FG_jSKokEPk4Jd7azkZEZts9btdCiPmv-LiSqJSzwf45HaYu39fsmmQQB0FeSvKHK9Bu3XEjBm9QdEVGt_VD-T3C3a9mAYXfL00Bm3oIVsVwn7ZgwLO4efvHE_gv_GfL3gCzPxqqLU7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رالی تماشایی بازی ایران - برزیل
🔹
برزیل در خانه در نخستین بازی لیگ ملت‌های والیبال ۳ بر یک ایران را شکست داد.
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/658367" target="_blank">📅 10:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658366">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6eoCRY4ZYRZNpHLblbbSFhqpveRTM7XRWOqo-qi1c0Q1RFw7Yc18tVbfQzpp0KH-JLpigJ-37AmOihzyasuoniJBxa8YmuCOSkoJo4zHXLOpLmG5_K0YyskcVVPYm8xx2R3tdYZaifJ9XrMynVEsYwPFM9sj4gJydGSNLkLvY2OoYTbc5nA45UICUs5ddYXyia3DFqdBu0S1G9Y4_PZhKpKtMJ7hoEkyK6P3t8B_koOFcaizT0tLJtkFRP7N1XwA7gdCsu1Ae3ypk8kDTzt0gHMXwg5TAcEwpG4ENrhkUNwNYEMGbt8hhce5nIu1cTgc4SHwLfvVoZRphEJMVrUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش حادثه در ۲۱ مایل دریایی شمال‌شرق صحار در عمان
🔹
هیئت عملیات تجارت دریایی بریتانیا از دریافت گزارش حادثه‌ای در ۲۱ مایل دریایی شمال‌شرق صحار در سلطنت عمان خبر داد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/658366" target="_blank">📅 10:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658365">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3494c4c7ae.mp4?token=ZC1wnEJOrsJAxgAIUD2XOg8OsbdiAsKFZneoexu3h5c-ko42NCkl2jDJXaZhlTT6de3sVdFsn0CKqSMZmH2dB66a54f3-WR_TbP3XuGLNaSjeL2t5T5MysVklVSLdb6P7R7FDyFejWg28FvP0iXN9R6tDGhm6Ts4ozVyg-RzbicgHlMXuJRI_J0WagZc4BkqeWRWV1z0mAVMOt9_LBGQ23CFArSjI0VrpJKvuxCaKb8ozcSDipiYfq37kR_7rTPyt3EliAKu8QiPJDhEkgejJ7y0GDLjimblOxTMgmBOZ-g4N3tfBX04t8m7AxKXH86e-g7dyvVAG9zzfDswKLwEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3494c4c7ae.mp4?token=ZC1wnEJOrsJAxgAIUD2XOg8OsbdiAsKFZneoexu3h5c-ko42NCkl2jDJXaZhlTT6de3sVdFsn0CKqSMZmH2dB66a54f3-WR_TbP3XuGLNaSjeL2t5T5MysVklVSLdb6P7R7FDyFejWg28FvP0iXN9R6tDGhm6Ts4ozVyg-RzbicgHlMXuJRI_J0WagZc4BkqeWRWV1z0mAVMOt9_LBGQ23CFArSjI0VrpJKvuxCaKb8ozcSDipiYfq37kR_7rTPyt3EliAKu8QiPJDhEkgejJ7y0GDLjimblOxTMgmBOZ-g4N3tfBX04t8m7AxKXH86e-g7dyvVAG9zzfDswKLwEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎁
اعلام جوایز قرعه‌کشی حساب‌های قرض‌الحسنه پس‌انداز بانک رفاه کارگران
⏳
فقط تا ۳۱ خرداد فرصت داری!
💰
بیش از ۳۰۰۰ جایزه ویژه در قرعه‌کشی حساب‌های قرض‌الحسنه پس‌انداز بانک رفاه کارگران
🏆
۱۰۶۶ جایزه نقدی ۲.۵ میلیارد ریالی
🚘
۱۰۶۶ کمک‌هزینه خرید خودرو ۲ میلیارد ریالی
🏠
۱۰۶۶ جایزه لوازم خانگی ۱ میلیارد ریالی
✨
به همراه هزاران جایزه نقدی دیگر
برای شرکت در قرعه‌کشی کافی است:
✅
حداقل ۹۰ روز، موجودی حساب شما کمتر از یک میلیون ریال نباشد.
✅
در روز قرعه‌کشی (پاییز ۱۴۰۵) حساب فعال و دارای حداقل موجودی یک میلیون ریال باشد.
✅
کد شهاب داشته باشید.
⏳
فرصت محدود است…
امروز حساب خود را تکمیل کنید و شانس برنده شدن میلیاردها ریال جایزه را از دست ندهید.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/658365" target="_blank">📅 10:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658364">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
پیام فرمانده قرارگاه مرکزی خاتم‌الانبیا به مناسبت سالگرد جنگ تحمیلی ۱۲ روزه
🔹
سرلشکر علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، در پیامی سالگرد آغاز دفاع مقدس در برابر جنگ تحمیلی ۱۲ روزه آمریکا و رژیم صهیونیستی را گرامی داشت. وی با ادای احترام به شهدای عالی‌رتبه از جمله شهیدان باقری، رشید، شادمانی، سلامی و حاجی‌زاده، بر آمادگی کامل نیروهای مسلح برای پاسخ قاطع به هرگونه تهدید و ادامه راه امام سیدعلی خامنه‌ای (ره) تحت هدایت آیت‌الله سیدمجتبی خامنه‌ای تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/akhbarefori/658364" target="_blank">📅 10:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658363">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eccb52d99.mp4?token=t2mM7ZsomT6MLmfnnToDMkvCQPQYygKkIHRvgm5HMZQh_8GWyt7FnQuF1QObLIZBn8FDc5U9i56I19XtcIvOheB3fg7b2HNrt-1Ggce-jEPSiSZz9IOd_qoOe8F_S_IkFk3ErpF2CDRmZzSa_mHJOg8OhNgQBwbkr8KGrCw_w3dZTX4npZXNCwkuOKJJKhAFMSenOSSDh43COIy0cCrCp9hrA6xzL2nIF2goQlzundUJRko4YSr8Yoxl4DKuMN7Sv6SGipMBshD8oGljaGgvGJzahrAG_Swjf3uf3AI9ugfumyQmJ0qw4vq41X_sK_hqS45F12rZvC29oFZ_JF88ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eccb52d99.mp4?token=t2mM7ZsomT6MLmfnnToDMkvCQPQYygKkIHRvgm5HMZQh_8GWyt7FnQuF1QObLIZBn8FDc5U9i56I19XtcIvOheB3fg7b2HNrt-1Ggce-jEPSiSZz9IOd_qoOe8F_S_IkFk3ErpF2CDRmZzSa_mHJOg8OhNgQBwbkr8KGrCw_w3dZTX4npZXNCwkuOKJJKhAFMSenOSSDh43COIy0cCrCp9hrA6xzL2nIF2goQlzundUJRko4YSr8Yoxl4DKuMN7Sv6SGipMBshD8oGljaGgvGJzahrAG_Swjf3uf3AI9ugfumyQmJ0qw4vq41X_sK_hqS45F12rZvC29oFZ_JF88ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون هیچ نفتکشی درحال تردد در تنگه هرمز نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/akhbarefori/658363" target="_blank">📅 10:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658362">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
زلزلهٔ ۴ ریشتری در نورآباد استان فارس
🔹
زمین‌لرزه‌ای به بزرگی ۴ ریشتر  حوالی نورآباد در استان فارس را لرزاند.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/akhbarefori/658362" target="_blank">📅 10:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658361">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0ac0ab15.mp4?token=jDEXTv9n4j8N0vrgtgfbjgQcsJiVcs7jaisLw4lPPwcn1lnF0k5FNd_0W42BaDdD-mGmPZyUnTnp_bCfjcVm9y2J2O3xn69jyMGjUt5xF1E5jWMoMbBD4Rp0dh_AaxifSBXnYhP_jHZM0YPd78BzmGyfQ31DLLR946fWT1XFcDHVMVV77HPplIK7nQnWvYPuLg5d2goVTR7s6zH97qt7W3cdnrg9LNXjoVsvdAE5Fob6WTbZiFbSPmB9i3uLf7qGz9VnYzDaDH_C9-K3IhEO-0SGHTqk3B_9ts5RCQRCgpVlVsIqLEEdcPvUF3TaVRdpsojeE2h3zKaW_kFeyfvlgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0ac0ab15.mp4?token=jDEXTv9n4j8N0vrgtgfbjgQcsJiVcs7jaisLw4lPPwcn1lnF0k5FNd_0W42BaDdD-mGmPZyUnTnp_bCfjcVm9y2J2O3xn69jyMGjUt5xF1E5jWMoMbBD4Rp0dh_AaxifSBXnYhP_jHZM0YPd78BzmGyfQ31DLLR946fWT1XFcDHVMVV77HPplIK7nQnWvYPuLg5d2goVTR7s6zH97qt7W3cdnrg9LNXjoVsvdAE5Fob6WTbZiFbSPmB9i3uLf7qGz9VnYzDaDH_C9-K3IhEO-0SGHTqk3B_9ts5RCQRCgpVlVsIqLEEdcPvUF3TaVRdpsojeE2h3zKaW_kFeyfvlgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن مکزیکی‌ها پیش از شروع مراسم رسمی افتتاحیه جام‌جهانی ۲٠۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/658361" target="_blank">📅 10:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658360">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
پزشکیان: بخشی از دهک‌بندی‌های فعلی مبتنی بر اطلاعات به‌ روز نیست و باید اصلاح شود
رئیس جمهور:
🔹
ایجاد بانک جامع اطلاعاتی شهروندان، زمینه ارائه خدمات عمومی متناسب با شرایط واقعی افراد را فراهم می‌کند
🔹
داده‌های ملی باید با بالاترین استاندارد‌های حفاظتی نگهداری شوند تا امکان نفوذ به حداقل برسد
🔹
قابل قبول نیست که برخی افراد با وجود دارایی‌های گسترده، از پرداخت مالیات معاف باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/658360" target="_blank">📅 10:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658359">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ne1q8o5QPaKeJiu0dsyyJrd4AJ_EgPPIBD0oQDxnQNR0rVeLQFoWLJmTkzmAmznHy4cNWfhEt-4LvFUIy36Qg0OtS1amhFUOx1MZINFiqAymFCmhkLKXnsLZT2SsI59GFH6hDERsrCyXv70Hx6PvuoHw2Rg7JGJGCjwIeJz6EnjAUvZF_Lujsfp1uMz9z-iYBDmkkYCpXdgmA9VLLu9ob5BktZnd8ocqdtBnYxsoU2gARhRJReKgedRlWfwsvZ0Xr4E8wdNivhYr1XTtqHqbBe036POvDd4u30KK8YiNdrwgxfG7YlDMnRUKR5VYZx6uGbXMBPNmBWBVpA0XqImTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه کامل دژهای نفوذ اسرائیل در خاک سوریه
🔹
اسرائیل از قله جبل‌الشیخ تا القنیطره و الیرموک، شبکه‌ای از دژهای نظامی ایجاد کرده. این پایگاه‌ها که برخی از آنها، زمانی متعلق به ارتش سوریه بود، امروز به «چشم‌های اسرائیل» برای رصد موشک و پهپاد و سکوی نفوذ به لبنان تبدیل شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/658359" target="_blank">📅 10:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcXiqHpZNoQf5Xvjx_zS8ciD9-pjzQgQjNtcGNyYdZPb5NnVqMW7RLnkaHoMq-UTypneNfs3iLgc0E0U4Kr18bI1QQwcIOnmDTTCDlSI86aPcfZx4YkW7PUHd3b8HThnQuwvqfyXs1gSe5_DsEcgyqsOhhLvgS7ifb81a25trGGMxZMbfnjDrLqZlxicVHK2g95nfxc47f79DxStt6q76vpGetSvtfYUnT2G8bdfGKIG8Im04jzdMEwJzY3Sg8wp75W5iVTbkOGzTGnkUMuXPXRfaix7-OI73Oqhn2ms2Bp8Y3E1MFt1mNArzxr7SYL252YFT2Dm45yMiqcHkE5oHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDlZIpDdZCetiTvfUYnlz4gXhDk9H_bcl6LR4v6yKe95CDilXpRcdcZzuGGwPTDMyldlmHfECyJ6EzW2zMA1wI1le3AA-X5-ktV4FDUkrUvMq9OdZI43q5nIvFLQWdelPLwvd4_bd9EEZauOzD0LTHLc4J5touW7ULb77islSgHaFelz_k73suu4-OaAzLF76d9z5chWxzilKnQguiAlINee4PpvigIppTP_sT4tc-qVj2ef-PvNO_lQYohiRAeqJbiHYhiFouGetVdRVyR8GQsR-nPpFLCx9rYBSbpzok8tCD3VlHEZtj7Ib8136AVeEfgW0CXGMXYXje2VUIPNew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پاکستان؛ مرکز تولید توپ‌های جام جهانی!
روزنامه نیویورک‌پست:
🔹
شهر سیالکوت پاکستان به مرکز اصلی تولید توپ فوتبال در جهان تبدیل شده و حدود ۷۰ درصد توپ‌های فوتبال جهان، از جمله توپ‌های رسمی جام جهانی ۲۰۲۶، در این شهر تولید می‌شود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/658357" target="_blank">📅 10:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658356">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
دو خدمه هندی در حمله آمریکا به یک نفتکش کشته شدند
الجزیره:
🔹
در پی حمله شامگاه سه،شنبه آمریکا به نفتکش «ستبلو» در نزدیکی عمان، دو خدمه هندی کشته و یک نفر مفقود شد.
🔹
آمریکا مدعی شده کشتی حامل نفت ایران بوده و به دستوراتش توجه نکرده است.
🔹
هند در واکنش، کاردار آمریکا را احضار و اعتراض کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/658356" target="_blank">📅 10:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658355">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d06fe35bf.mp4?token=eFXUUg06TNpZly8BMh_hQw2CfRsQlvgV2gv6L3mn7_Y-YtsG_5O79SHLRy5k6AlPRMULx0PZmRYvBBcqhHiXNz1Kh4pfWNPOQbgWwfVj8No_D2yY6t9GxNeqUMCp0W4HNof3BYq0PqdOC5CIHGLkbOkpS4yI3aVEm46NTFqwDfUDC742_UERpWIGJucK20DM6WS6Ml8MZ0kzVUehpxyyNlLjY8tVFQ0bbPGeMAKtfPInKowBI7lsHExzEWnd1nTDebMBP57s2sbzYwk6-_jIaaEjw29LIR76lc8wQUSEBmaj1ZFpeXSjLZgyrltxHhTMKu_-LqHtnTCbwEaWDxEaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d06fe35bf.mp4?token=eFXUUg06TNpZly8BMh_hQw2CfRsQlvgV2gv6L3mn7_Y-YtsG_5O79SHLRy5k6AlPRMULx0PZmRYvBBcqhHiXNz1Kh4pfWNPOQbgWwfVj8No_D2yY6t9GxNeqUMCp0W4HNof3BYq0PqdOC5CIHGLkbOkpS4yI3aVEm46NTFqwDfUDC742_UERpWIGJucK20DM6WS6Ml8MZ0kzVUehpxyyNlLjY8tVFQ0bbPGeMAKtfPInKowBI7lsHExzEWnd1nTDebMBP57s2sbzYwk6-_jIaaEjw29LIR76lc8wQUSEBmaj1ZFpeXSjLZgyrltxHhTMKu_-LqHtnTCbwEaWDxEaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️
⚽️
جام جهانی شروع شد؛ وقتشه ردبانکی شی!
❤️‍🔥
اپلیکیشن ردبانک رو نصب کن و با افتتاح حساب، ۱۰۰ هزار تومان هدیه بگیر.
🎁
👥
هر دوستی که دعوت کنی = ۱۰۰ هزار تومان جایزه بیشتر!
🏆
تیم ۱۱ نفره خودتو بساز و بیش از ۱ میلیون تومان هدیه ببر.
⏳
فرصت محدوده!
✉️
عدد ۶ را به 7007666 پیامک کن
📱
یا #6666* را شماره‌گیری کن.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/658355" target="_blank">📅 10:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658353">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7510f35165.mp4?token=l1gMPiLOnxecLBezt7fzl3owuKfAKU_AVHADx8i2CogyMae0VeISADJjL1kEaokJVDRX2YyPgPH09TUo3xtD7ioRexnBtmJj-dUxQ_6X9Cuwc3VKftrq_08Mvj0n_zvuSAlPkOPUPI0NiKw_Vk--hHXzsYsy8TGhbi-v2KltiGsailPcjZvYysSUoWH3KVueoEFuaQt9AsqOW0E0GXUR0b4JxTUpRHLtVsVkbcIanv-Ypq4A8rgHDANyHHls0nIZkvQNDf6O6qJUg8kV7yj0cwHn4wVrJtLWVGIMNFOVT5AuEURuTy6Nh9NI3XPNA1aWX5CxED33oDu8wT2ArP5-QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7510f35165.mp4?token=l1gMPiLOnxecLBezt7fzl3owuKfAKU_AVHADx8i2CogyMae0VeISADJjL1kEaokJVDRX2YyPgPH09TUo3xtD7ioRexnBtmJj-dUxQ_6X9Cuwc3VKftrq_08Mvj0n_zvuSAlPkOPUPI0NiKw_Vk--hHXzsYsy8TGhbi-v2KltiGsailPcjZvYysSUoWH3KVueoEFuaQt9AsqOW0E0GXUR0b4JxTUpRHLtVsVkbcIanv-Ypq4A8rgHDANyHHls0nIZkvQNDf6O6qJUg8kV7yj0cwHn4wVrJtLWVGIMNFOVT5AuEURuTy6Nh9NI3XPNA1aWX5CxED33oDu8wT2ArP5-QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلبانی پروژه گردشگری کوشنر در جزیره سازان را متوقف کرد
🔹
دولت آلبانی اجرای پروژه ۴.۷ میلیارد دلاری اقامتگاه لوکس در جزیره سازان به رهبری جرد کوشنر و ایوانکا ترامپ را پس از هشدار اتحادیه اروپا درباره پیامدهای زیست‌محیطی موقتاً متوقف کرد؛ همزمان اعتراضات…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/658353" target="_blank">📅 10:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658352">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6pbNJ7E9p5Uk02NAfb_YMXObWbrwRGFaYIOKqbSQvaVipW4VsD9SIzQtT3W1xdyyyRvRNdq6Tpe5n8Sn-9_wHpjnoX9ngV4NBfMV7Jyg6EhG9krWBMCj8ICvkJirgnF4y4B1zuyXG2OLjXaHuXM5XwBA5xybXqerm9rhcMdJMPTAHkMpu2PfINHBjNCgMxCYejLs78RJsRNjD3N4R_a8Uy_Il8MvOO16MZfiDmK-ijd9c4tls777-5dfyw96q2MF6Igs0Bxf5V-CEoVwMdnpr3l9T3NhwKz2Em7MaksojJDFM5azN8-w2WLAO4BiKxyZJMxcGHkd1oFt2A_PfzG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم‌های جام جهانی فوتبال بر اساس جمعیت کشورشان
🏆
🇺🇸
ایالات متحده آمریکا — ۳۴۲٫۶ میلیون نفر
🇧🇷
برزیل — ۲۲۲٫۶ میلیون نفر
🇲🇽
مکزیک — ۱۳۲٫۸ میلیون نفر
🇨🇩
جمهوری دموکراتیک کنگو — ۱۲۲٫۸ میلیون نفر
🇯🇵
ژاپن — ۱۲۲٫۱ میلیون نفر
🇪🇬
مصر — ۱۱۴٫۴ میلیون نفر
🇮🇷
ایران — ۸۸٫۸ میلیون نفر
🇹🇷
ترکیه — ۸۵٫۱ میلیون نفر
🇩🇪
آلمان — ۸۳٫۹ میلیون نفر
🇫🇷
فرانسه — ۶۸٫۷ میلیون نفر
🇿🇦
آفریقای جنوبی — ۶۱٫۷ میلیون نفر
🏴
انگلستان — ۵۶ میلیون نفر
🇰🇷
کره جنوبی — ۵۱٫۴ میلیون نفر
🇨🇴
کلمبیا — ۵۰٫۱ میلیون نفر
🇩🇿
الجزایر — ۴۸٫۴ میلیون نفر
🇪🇸
اسپانیا — ۴۷٫۴ میلیون نفر
🇦🇷
آرژانتین — ۴۵٫۵ میلیون نفر
🇮🇶
عراق — ۴۳٫۸ میلیون نفر
🇨🇦
کانادا — ۳۹٫۵ میلیون نفر
🇲🇦
مراکش — ۳۸ میلیون نفر
🇸🇦
عربستان سعودی — ۳۷٫۸ میلیون نفر
🇺🇿
ازبکستان — ۳۷٫۵ میلیون نفر
🇬🇭
غنا — ۳۶٫۱ میلیون نفر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/658352" target="_blank">📅 10:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658348">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1wTbGUfR_si8GjoHo3Vz212BXfVHfkVlb5mxbm-i72JMrUJBhsFHQ90fCKLUUjugupIa5cD-Sd_LO1G7mrlH_WOAGfGVbegWvCKL1-NhW5RkeM8zqvzBmsneHoKyvJ5B-BXlNixjZr41ODVi5Gg1CYxdvlhG7RQzm9V-cwC49L0R_DXoz4ZyD0lvu3ctzL50PEtTyyko8D999wxqvylrgTo8DNzrywR1-ZjatIs-Y0Mbyr-0PBs8RnRCPeILGPL6zjHmAwwQh_CTrLRObyC_6wVezIT4gxNWwZp-gBJfDS_bLcQFpgAU9-MYFGFU41KGCQhveQSaPC6xbuIasJiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGpsxMaF1V02yaq9nl4riL_eK72yHYsKeFxRbr4nEPsmGILbQpk2B3OlQ68418-yHzdfZEi9E6lWmR-X2WagAxw_d334r0j11XSmGJctbSITBNl4Wr4pgppu_OgfmFGzhHnKEy9QDYJ3okqccLekDOm3eSIw_35faUf4P4TBJbSW7rmq4xniwo4yT160gGENhrE0-nh7fH1XgCOnz3N3sMVw1nUX9i9CZ10Sx6PKYzUNIcpJPEEjj4_rOGtWGpQUygVDtaMJX5u37uAtKzQQmy9qLMbrzu7XFEz8h0jCLXT7WpgD-d3J_SduWp5lxlru5cFXoJ8Eg5WL7QS7ECTQjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AneaNVqV1QrYottvY8CH6B0uEqYc09i1x7056eQNCaBMV1QkcfAqZt9YymkzpUsWzl3AggLYmf_DOZeQc4olbp30bhmaTmJykTEPopNvMKZqfwgvmV-DwiIR8uM3ctXASD2p0tQdZmt48M16liL52tBQ-olngD2oSZx-Q3jsMjwHwfICMZzvGY1uwAbo3k3AocKkKUNYe-LOnPJ9TxHHCo_30zaYj1m4pEqpxODrkDqc6l7qOWvdnsxPOpl861XWqicmMv2fKV9ze0Cv4TlWvli-ftPwBAc7yzONRFsD283iWi_mzjjCjDit9AuIjKibyUYLjWM5PxGEXBqzngNyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBIBvwdfeSl1QVbJpUh_h9BT2dS7I6f3yf-ZhYi0BH0-NNKIQlNkg8ad4qmuzzc5vMbWhUk9LCEkvWf3yfP4keomTmQbdgz_Xmj4xJ5j2PCcWHzSH96i8f_3BNyb_GiiFr1rSf8i9DrBLNjC_FnnAlF_a_OgvT_33pezTY24ZeMl8sK2onIoY9LU-ddNwnjSkgEyNVzk4BnSHg2nJseem8cJfbJvFv0t3Qm5b5M3Os6eS_4zQbDZJjTRA15JOD-oW0jroUPUQtPO0cj1s_QDzvl5W0fQLY6JMsXI8OfUvU1EGULQeX3nQClk0Vyf6Cgvx24Wlx07cJTngxafUpwJ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا نسبت به آدم هایی که سردن بیشتر وابسته می‌شیم؟؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/658348" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658347">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28d94813d.mp4?token=M69Xz3c5PzqJ_Eca-Wk95RsUtJ8R-0LtirJRyk9wxijhaimuu9NAJNZKAHytPx2IJNCH57yyKFkC0xETz4G7e_gTc9qwMXIZDx4ib2nmfpDaOXQl6J2SoXh072EG6I-nYn_Ev5cAbxXVHKpyYGgEMwK9knLbC9cF2mLrEXoGM64m5Ntas30CBkaFEoUThBho-B-mCmiVoFtgcXdqeMImtcKVmcrlmsPPWoseogz4aDSyWn39Dm6s07bVXkaWkhX0adN3xKlM-Psuco0y5CIZthTPuxJF0Vr95hUL85p6e-S-krRCEUev-ags0FNDTrKCvtU2-ebwgQcFWzesTPZRwjArkI_ul377jNnfxPjB-WVQWSdNQUd_D7Mxs3EaiLuFLan424nJwGZk-9nxhHxH9mO1K_KTmgy05diX2Z6t8Yo18sOkORQXNwx-JjlO15MJQMhKWw-Q_SgAdbu-nArvT7hKK6TikAa83-rkSUD90vg0eXEti0J5mhmUXAMhAI_JR5tNCO5f8pwV5dsy48nehLJvYnh6Ck57wFGGrtRLPa_V35RzGrft_jTN2UpbPz2ZXYWwooyzpPx86Gp7IkBr7VAesvGNKW-9XmZxg_I0nCRgCAb_NVlLB3RDVa5KbyxUGF2YFiOldLrcbEvoS6DndpBu7vaawUpARUVZHOcPImY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28d94813d.mp4?token=M69Xz3c5PzqJ_Eca-Wk95RsUtJ8R-0LtirJRyk9wxijhaimuu9NAJNZKAHytPx2IJNCH57yyKFkC0xETz4G7e_gTc9qwMXIZDx4ib2nmfpDaOXQl6J2SoXh072EG6I-nYn_Ev5cAbxXVHKpyYGgEMwK9knLbC9cF2mLrEXoGM64m5Ntas30CBkaFEoUThBho-B-mCmiVoFtgcXdqeMImtcKVmcrlmsPPWoseogz4aDSyWn39Dm6s07bVXkaWkhX0adN3xKlM-Psuco0y5CIZthTPuxJF0Vr95hUL85p6e-S-krRCEUev-ags0FNDTrKCvtU2-ebwgQcFWzesTPZRwjArkI_ul377jNnfxPjB-WVQWSdNQUd_D7Mxs3EaiLuFLan424nJwGZk-9nxhHxH9mO1K_KTmgy05diX2Z6t8Yo18sOkORQXNwx-JjlO15MJQMhKWw-Q_SgAdbu-nArvT7hKK6TikAa83-rkSUD90vg0eXEti0J5mhmUXAMhAI_JR5tNCO5f8pwV5dsy48nehLJvYnh6Ck57wFGGrtRLPa_V35RzGrft_jTN2UpbPz2ZXYWwooyzpPx86Gp7IkBr7VAesvGNKW-9XmZxg_I0nCRgCAb_NVlLB3RDVa5KbyxUGF2YFiOldLrcbEvoS6DndpBu7vaawUpARUVZHOcPImY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون: چه بخواهیم چه نخواهیم، ایران به طور منحصر به فردی در کنار فلسطینی‌ها و مردم لبنان ایستاده است
🔹
بقیه جهان با وحشت این را تماشا می‌کنند و هیچ کس دیگری کاری در مورد آن انجام نمی‌دهد.
🔹
با وجود داشتن آن ارتش، با وجود ناوهای هواپیمابری که از ابتدا تا انتها ۱۲۰ میلیارد دلار برای به آب انداختن آنها هزینه شده است، ارتش آمریکا نتوانسته است آن تنگه را برای حمل‌ونقل به سایر نقاط جهان و کالاهای جهانی در ماه‌های اخیر باز کند و هیچ تضمینی وجود ندارد که ما بتوانیم این کار را انجام دهیم. بنابراین ما قبل از هر چیز محدودیت‌های قدرت نظامی آمریکا را آموخته‌ایم.
🔹
کارهایی وجود دارد که ما نمی‌توانیم انجام دهیم. جنگ ایران به ما آموخته است که در واقع در مورد مسائل بزرگ، افرادی که شما انتخاب می‌کنید حتی مسئول نیستند. شخص دیگری مسئول است. در این مورد، بنیامین نتانیاهو.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/658347" target="_blank">📅 10:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658346">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5ib-dH_6abGdi1y1lAmOH5Srite0kHYdhRd5chI6g_gRyCIv8QTtiAERVhOvNfW_Dgzm3M3QinByfFSBB3B-hPr1d4dYeGzhQUIpX21HE7h27-DFMTihryE-PC-tfUvmYOb2TZ6BUNfLimiyVDg1XzMS1SuAg9UmIkSVKDHkeS6ECslZZH8FhT6ajAQV7GvDaJ-XBrUPkbRqRiyXXLnsbTGLozwE-9BAXaRJX-jkuxvXJgyS4r-p-HHrZHGYT-VtgSh_Do8acw8w4VhYdf5Ebdw1Vmen4RA6N3g6LmJJGQVZPMd4AdscH7iUd93ZhMnsl5KUXhQ3MCoORt5IYU7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👠
استایل تابستونت با mono کامل می‌شه!
‼️
تا ۷۰٪ تخفیف بر روی کیف، صندل، کفش، اکسسوری و البسه زنانه و مردانه چرم
💳
پرداخت اقساطی با اسنپ پی در خرید آنلاین
💳
پرداخت اقساطی با اسنپ پی، دیجی پی و زرین پلاس در خرید حضوری
🆔
@monofashion_co
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/658346" target="_blank">📅 10:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658345">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSw1VleBlciEoBO-nZShsI2SgEXytda8W0Ox4y-GmAlF4t0UlZJQ5T8fmTXpYH4R14JVvL9o06Al5ZTD-X90DPUQorsCrhj6mzAlZO1E5IVDQELGaabs-8_FUphgfbWcKNbEm0KXLTuMyH2X0YIWjcIT604ua5K3xKSpAv5WxA7USr_YQnS3P-YzVWgV9OZDshtsh__r8DrgR4eCtTN84fR0btRXDiabYP5pNv_9VC7qAtOEUFm_IixFYimUEX1GGbg8wXnm8ccKCXfX1fs-Xfuzv9UY0llIA2ajb2xWRoPE3IprZSFDPGx4LxFiIBw7Ro7NnJXFTKEKJO4iPzqD3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
جام جهانی ۲۰۲۶ از همین حالا در «همراه من» شروع شده!
برو توی اپلیکیشن
«همراه من»
، بازی‌ها رو پیش‌بینی کن و جوایز هیجان انگیز ببر
🤩
🎁
۵ گیگ اینترنت رایگان بدون قرعه کشی
🎮
هر روز یک  PS5
💵
۱ میلیارد تومان اعتبار کیف پول در روزهای مسابقه
📱
قرعه‌کشی بزرگ S26 Ultra به همراه سیم‌کارت ۰۹۱۲ برای سه نفر برتر
✨
3 کمک هزینه سفر به عتبات عالیات در هر بازی تیم ملی
پیش‌بینی از تو، جوایز میلیاردی از همراه اول!
🔗
https://www.mci.ir/-9VEQ3HH</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/658345" target="_blank">📅 10:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658344">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUqO5FjzMr2OL0q72YUwXvf2fL4_KyQLWdxZyaOrqiBaaSFaOstvDNZvDyGFuTtuWkiVdriCkedub050A6GUIhrmBUKErLvBjO9SALqNDUz2uBDJCrvuOGztdk5r3spLilrGJLMHEmWz9aHZW-fwYeRqmHrKeOaKyjtCRBzxqABIlIjKWxj88E0cSSZqXIUfo3Y8roQtFh2oCvavn2-aeHhjTH6B18O-42fERErkJI3xzLZaiuZaCxYhsE3r1WaOFyVLBl-_kSsLnz0KKZADF3GCB8LPZsOkQMTRODPjGJNswqrhYN9gfhjlz6ZChiMLAGCjvgwoKils-vbNfJ7AMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهاجرانی: با تکیه بر توان فرزندان این سرزمین، ایران استوار خواهد ماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/658344" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658343">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سپاه: ۱۸ هدف مهم متعلق به ارتش شرور امریکا طی دو موج عملیاتی مورد اصابت قرار گرفتند./ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/658343" target="_blank">📅 09:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658342">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYzt_TW59oXWR8F63nEwe2InsoDdiJQ11Ec8eMFrMZGPX5-dPDgBIw_Np_vEUup2qlxaklUh1vEwviyDLs2oeoMzXrMwuPbpGlbQE69UG9qDx1CZrX5bykHPtTwLpikkfjWguQaRHR9-JvpnSbGJDvkLYh76FO5SMy_XpUBAaMe09iRNuq-CAayV02eBaXqxg-kmKicJEVTju8Iv6a2bDUSyib4b1x-DD1MnNaciezddlK5rFq4gvANtyCnNOl8WgbeTtQWT31hkD9Wm5C3vCaIEkmXVQklsoAzthoF_vrf-S__1UuOpJpBl2L7wsjw4VV_8wG44FeYZfCkaAqg04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جلد روزنامه اسپانیایی مارکا و استقبال جالب از جام جهانی با تیتر «ما متحد هستیم»
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/658342" target="_blank">📅 09:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658341">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNiHDsDcVNXHmnijcnJ8rhC0yWRFI4xCxmdoc7u0ok803pG8YpBPHsQgN00eolMfpc5kJWTaI4fak3_fJCFyKlOXRwcBJBiZhsSriTSlRYnTxgWOYiuyX21VCLBgamBNr9LUk6DvXVR312vySpTX_bfYeEJoe310DW-6aKp1_8_NLpMgXS9N5j588LTtMDIapXHKpQ8jBHuntkzhGie0UYNbNbad6p3b9I-i9PGAgk-yr5VMgHrd5b482yVBlHRoAv4jHwtrH9ZauvBZ4Ayxb0T405iu4TXCuB5oit9VLcsoA2JFKj2lop2XfIA_nSMBzRm1bu-i_2pdTXRGooy_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان نیویورک تایمز به احتمال جنایت جنگی جدید آمریکا در ایران
روزنامه نیویورک تایمز:
🔹
براساس تصاویر ماهواره‌ای، حمله آمریکا به یک تأسیسات آبی در ایران انجام شده، اما مشخص نیست هدف‌گیری عمدی بوده یا نه.
🔹
اگر زیرساخت غیرنظامی عمداً هدف قرار گرفته باشد، ممکن است مصداق جنایت جنگی باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/658341" target="_blank">📅 09:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658340">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpKA-td5yXbageXR7NS8HqiDtBFhevkYiER0ymQPtTj5A7yBGp6mJsgPuwEMurKZLMlrkiS21VE_6-zp51QljaK--5PsKOEE1sx9bys1wcnAcYc2zhXw_t4VF5DIJ1pgMRvUDKQopmoUuQ_hWQZzyoA98YiSS1phgT_x6snyV_7Ap48oqcmA_OLKOf-G5qrF4lSsWDW1qsdGq2Lo7xJApiUblTa83C-Iul-NVI7wI5-NyurVnev4JrROghpJyBBqXTdFO5L69eA70asGS1448o0wqaT0D_6O3-BGWyZoDS0WAl3Yj7aGwwwbRzb_mCFpJ0Eo6xS-X9gPON3l_9mCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت ژورنال:
علیرغم صدور مجوز حملات جدید به ایران، ترامپ دیپلماسی را رها نکرده است
🔹
مقامات آمریکایی می‌گویند که او در حالی که همچنان به دنبال توافق هسته‌ای با تهران است، از فشار نظامی برای وادار کردن ایران به امتیازدهی استفاده می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/658340" target="_blank">📅 09:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658337">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ac068b03.mp4?token=fcOUeXFuxsl5ty83M3rYBp8s0CyoP7IzxtdF83u-c4ir9lYd1GpFr1yLaLHD2ze-dAqZdH0TFgIprA4A6QAt5SPPzebM3ZHpuJrRhF-qArBRoCegbXTytLoL_SMbDZ9XLoHDJTLguFusn32fBbUu4LV70TEKFKVNUhzDIvr0cgcL7SjwbchMPYpd9iyHRozGLxhXZqNYWaGpkanjbxihsSZvwmHIiCIRGY2AZ1gtrQPOuhtB1Iq9vGGxx7YaojyPI6K_oyM2BOUuGt55taaS23igF7uAfbPEd_lrhvCUU6FLoUqWAtHqn0-kMeor6_jEr_seV6AD5CBg0oUU8iGaCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ac068b03.mp4?token=fcOUeXFuxsl5ty83M3rYBp8s0CyoP7IzxtdF83u-c4ir9lYd1GpFr1yLaLHD2ze-dAqZdH0TFgIprA4A6QAt5SPPzebM3ZHpuJrRhF-qArBRoCegbXTytLoL_SMbDZ9XLoHDJTLguFusn32fBbUu4LV70TEKFKVNUhzDIvr0cgcL7SjwbchMPYpd9iyHRozGLxhXZqNYWaGpkanjbxihsSZvwmHIiCIRGY2AZ1gtrQPOuhtB1Iq9vGGxx7YaojyPI6K_oyM2BOUuGt55taaS23igF7uAfbPEd_lrhvCUU6FLoUqWAtHqn0-kMeor6_jEr_seV6AD5CBg0oUU8iGaCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر بیشتری از پرتاب موشک ایران به سمت اهداف دشمن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/658337" target="_blank">📅 09:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658336">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b50b401f4.mp4?token=bSjQhQ0EGjHh_dgSrK1mZKStOhAACuc5eKOgyKoUSXiQDcd-VV5-C_TG6t837hmf7KGh8pSi8NbVVdre8X2230jD2rDCF7zYmvM_KwXneHEanMtdqX6r1-fB12vDdsLUnV50c_0hYgVobIZJbNDRJbicF7-XjcGPkPr2H6c_RHOUxNzuXyzM7q7eOC0AEl0YXAi1LBECjcdr6pTMcgauWLCTZOZBjIsVWQJeUWexDAuHmFQHuwzReE5cfuPp_JrDHE-XWE56f-MHE7D99JHkhIQbYgJlzjwZYSh3WBHRfZ93D7yUFf8KNXDJ-Nitwg6mE1CCODYX2adm7OjJdNulvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b50b401f4.mp4?token=bSjQhQ0EGjHh_dgSrK1mZKStOhAACuc5eKOgyKoUSXiQDcd-VV5-C_TG6t837hmf7KGh8pSi8NbVVdre8X2230jD2rDCF7zYmvM_KwXneHEanMtdqX6r1-fB12vDdsLUnV50c_0hYgVobIZJbNDRJbicF7-XjcGPkPr2H6c_RHOUxNzuXyzM7q7eOC0AEl0YXAi1LBECjcdr6pTMcgauWLCTZOZBjIsVWQJeUWexDAuHmFQHuwzReE5cfuPp_JrDHE-XWE56f-MHE7D99JHkhIQbYgJlzjwZYSh3WBHRfZ93D7yUFf8KNXDJ-Nitwg6mE1CCODYX2adm7OjJdNulvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز داشتن یه کوکی شکلاتی نرم و کافه‌ای!
🔹
توی این ویدیو طرز تهیه یه کوکی شکلاتی عالی رو بهت نشون میدم که دقیقاً مثل کوکی‌های کافه‌ایه! ️
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/658336" target="_blank">📅 09:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658335">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djWLoO4rAq6BH9NAn-ZuWKRzLGxnMcx1WLtU2YXIQUjlXWtfxILms3LZ6B6HipiAKDjIODenqcnQIdFrH3EoYdul1zVcU85Y85DxBMne7r_bzAwb7xXVpI5x267aI6s8celaiLLmt7HKz57gCRnkBp9B1DHxJO-1st9yPmen1l2762CRAxV0jaizEyN2u4A92DZF3bfyEKseKijOxlXaYcxH4W8dLziR7_kdoIkFayeT38niezovfc2RHte0NPOyQDCAU2dGM2glVhcgyfPamhjUVED7h02xyrqUgsTdHTieDKa9Ef_5wWCyiohvThtgdk_2in_bp_01dtTeOIurJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضاییه: مشکلِ سردمداران آمریکایی آن است که هنوز مفهوم غیرت و حمیّت ایرانی را درک نکرده‌اند/ اکنون که پیش‌روی ما، ماه محرم، ماه پیروزی خون بر شمشیر است، بیش از پیش برای صف‌آرایی در برابر یزدیان زمان آماده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/658335" target="_blank">📅 09:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658334">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e8cc2456.mp4?token=GSmFZ61A80j6622-QR-raMDYuDV-so7EP64y38qyNK6FC8-ekbbZ5QLk74bdNDZ4bFoW_30xmvRyoPgRYf0fDkSGSN4SnlfRA_r-rGV0Ht9YZFvmxsQ0RgrGz2P_vneL5MIhOTupNCSzD-RxnEucBtYeuB2YS_M0YaKeMDVcH6O27I2w7s38oWTZm3A8ce5Z2SARQKyn9aYVURk8Jnx3w1MzmcQ54-axHwN19geU_AmEGcHHx7LsD_UA42fca7_w4PYvIrf8WEBBdh6P6Xc31J9_WnCkZmWJViH4dTfrw54wX4biZpMYfxoQB2Faqf89yXyJVroX3YOq8n_Z8B337A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e8cc2456.mp4?token=GSmFZ61A80j6622-QR-raMDYuDV-so7EP64y38qyNK6FC8-ekbbZ5QLk74bdNDZ4bFoW_30xmvRyoPgRYf0fDkSGSN4SnlfRA_r-rGV0Ht9YZFvmxsQ0RgrGz2P_vneL5MIhOTupNCSzD-RxnEucBtYeuB2YS_M0YaKeMDVcH6O27I2w7s38oWTZm3A8ce5Z2SARQKyn9aYVURk8Jnx3w1MzmcQ54-axHwN19geU_AmEGcHHx7LsD_UA42fca7_w4PYvIrf8WEBBdh6P6Xc31J9_WnCkZmWJViH4dTfrw54wX4biZpMYfxoQB2Faqf89yXyJVroX3YOq8n_Z8B337A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی وایرال شده از مقایسه استقبال دو میزبان جام‌جهانی، آمریکا و مکزیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/658334" target="_blank">📅 09:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658333">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ایر کانادا تعلیق پروازها به تل‌آویو را تمدید کرد.
🔹
دبیرکل سازمان ملل: «آتش‌بس بیشتر شبیه به "آتشِ کمتر" است».
🔹
شبکه‌های اجتماعی در کانادا برای افراد زیر ۱۶ سال ممنوع می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/658333" target="_blank">📅 09:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658332">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvocYEEXbpSR06uPHX4A4IQBsBZKdsEn5swhGzGeMyx08JhwuXi1rJgBz13J1dONzMoGte5gGONM4Fbc1LliBaB06H-yjP9y0uJ7Yg4KJCKSZY8GtRQ4cxXyrUwkMqxoiBhMTsp1-QupBu2qn25OdZrxCqLoAUoPFgvBNVrjSD-LuZvekYkd-5LtzcT53MGn74daLlk6D0eCTe8LlVc33YNfLrLEifNhNgCDq_Aolk4dI_2RSVfJpWWsAJVzg5MPIvT4oNeXmu7GUItPbleFWX5paQnKPR-qDkzAGEx_A9QN1NRyqcMTh_UNKDLpKvkEnZR865cSw-YdeFi_lj7GPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تاوان همکاری با شیطان
🔹
تصاویر ناسا از وقوع آتش‌سوزی در نزدیکی پایگاه هوایی عیسی بحرین پس از پاسخ موشکی ایران به تجاوزکاری آمریکا حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/658332" target="_blank">📅 08:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658331">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c2a641fc.mp4?token=qlXlANktGnEEiOX9ME6r3gHFz7h6x_KNxsI01vF_L7OkOwid5fNXpzUgFT4flccmGCO_9AOFxuvCkknVwDgIEP296Qg5SO_z4bAr3wzXWGbNHSFMRGhL22FhFN4jj1gRd6ZVpyztXCyY_ZokRwYbQmTDMoHNiyV3x2Y4NqE_dzN4l-dEAYESUgNoSXxlspWtANbOfzz5_FB-4qB0wEKo8DLBV_j_zdAnpMe__f54t1Ri_ra7i-5qOxQOUeleZEc5RTuyYBLGBslhv3eBjPijnWZ23r2N-FI5m1eLNCCtsod9gB-gG5SsJJ_1biXubLyzH4PGWV7j1Y-FkR9xE9gacw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c2a641fc.mp4?token=qlXlANktGnEEiOX9ME6r3gHFz7h6x_KNxsI01vF_L7OkOwid5fNXpzUgFT4flccmGCO_9AOFxuvCkknVwDgIEP296Qg5SO_z4bAr3wzXWGbNHSFMRGhL22FhFN4jj1gRd6ZVpyztXCyY_ZokRwYbQmTDMoHNiyV3x2Y4NqE_dzN4l-dEAYESUgNoSXxlspWtANbOfzz5_FB-4qB0wEKo8DLBV_j_zdAnpMe__f54t1Ri_ra7i-5qOxQOUeleZEc5RTuyYBLGBslhv3eBjPijnWZ23r2N-FI5m1eLNCCtsod9gB-gG5SsJJ_1biXubLyzH4PGWV7j1Y-FkR9xE9gacw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دقایقی پیش انفجار در نزدیکی سفارت آمریکا در بغداد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658331" target="_blank">📅 08:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658330">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
واکنش نتانیاهو به سخنان اردوغان: در جایگاهی نیست که بخواهد به اسرائیل درس اخلاق بدهد
🔹
نتانیاهو، رئیس‌جمهور ترکیه را «دیکتاتوری یهودستیز» خواند و مدعی شد که او علیه کردها مرتکب نسل‌کشی شده و مخالفان سیاسی خود را زندانی می‌کند، بنابراین در جایگاهی نیست که…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/658330" target="_blank">📅 08:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658328">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رویترز: اضطراب ناشی از جنگ عليه ایران باعث شده نرخ جهانی ترابری کانتینری سر به فلک بکشد.
🔹
روسیه: هیچ برنامه‌ای برای حمله به کشورهای عضو ناتو یا اتحادیه اروپا نداریم.
🔹
حسین شریعتمداری: باید از NPT خارج شویم؛ دارد دیر می شود.
🔹
کشف ۹۰۰ کیلو تریاک در جنوب سیستان‌وبلوچستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/658328" target="_blank">📅 08:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658327">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzqR0L-g2xjlX2-uLZp9P89P2F0imAnYPkjKPgsLsvisow5FmSOfbLFjDDvX72RRhR22je4s-H-5UBldFaFu1qoCr_P-W-YAQb5QQPBBzhOSwFgjhu6Z33kpKy4V3nojj1I3Wjtpl80mhkbkldQfnN8HirQe9J905y4EuDtX8pDQc3QD_jxHOAjctyPM6b5Ut0uP1pQEdBn_CEDlXywrlBFokFJagvFAtXNUdsdaErOe3C6ObtEBzMwlzbnS7vG2RrRJMXC4UfbXWLM2vfLlvVWIME23cDTMHA6XYfO3kN3Ykxy8Gm87aGrkvzEGg4vGwARQerFKrBj1X7mXi0lc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارشناس آمریکایی: اگر محاصره دریایی و اسکورت کشتی‌ها توسط آمریکا مؤثر بوده و زمان به نفع واشنگتن است، چرا باید ریسک بازگشت به جنگ را بپذیریم؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658327" target="_blank">📅 08:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658326">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOUVSKVcZY6uNweO3t7N64GqBtXj_wcujjSLXYbS7kAClpl4cqHPYIb1bPycgDcEvL_erWft69WlBE9qXNDOSWg-RioVf6pyeg26pL-dlc9QypdNEM1kRR7IWxpYjGaGRAU1r_vymvUvxMEVGgycE6lDqnxWsxUBAFshUMmhLaHhNkO64jbGZTVitvUJQ9yuAG1ZhZUZFfciBWigjSEMxTd_bsl3b2RSfXmAG8yjDOaf-rK75M8HkNunw_HSmMhNoMt27rQvoLr5iX8VdC3ImAF2vuMhy9--dEUWReGNmwQnyntAGINBxP4I6pffEodIOK0IeVjL70SZYBXWnFNzMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد دانشگاه شیکاگو: جهان به سمت یک بحران انرژی تاریخی می‌رود
رابرت ای پیپ:
🔹
ترامپ گفته که از زمان شروع جنگ، ۲۰۰ کشتی از هرمز عبور کرده‌اند این در مقایسه با عبور بیش از ۱۰ هزار کشتی در زمان عادی در مدت ۱۰۰ روز است.
🔹
۲۰۰ کشتی ۲٪ از حد معمول عبور در وضعیت عادی است. جهان به سمت یک بحران انرژی تاریخی می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658326" target="_blank">📅 08:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658325">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9011bfe3f.mp4?token=usz5nzLnYQWyPt8oexnzZTzG3BAYeOAKJ5er9E6uw1o-Dqaiv0mRpiCityeg86Csebw16cCMp5ZJKo52anjSsAOjxO9itEcTMZmg1b2wm8XkBsBOy9ep_73l6sRnE5T-CyRXAC8wne1fAy4r33n_U8FePNmZYpI808H3KRtyXrCYUzlQe4UdyZ4sRimofkeB4oqoBXOyals8jOMHoyAudh8uJLr5b-DJJZWagPynHAObtP3TvsI92kpqG_BMUqS9bkkNgLOoCokg7oJiA8Go7_yceeBpEDzC7U3F8l81Sl3g5b-x08jGw-hbt_hPe23Dd5BeOc3V0iFhhJipqE3Q7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9011bfe3f.mp4?token=usz5nzLnYQWyPt8oexnzZTzG3BAYeOAKJ5er9E6uw1o-Dqaiv0mRpiCityeg86Csebw16cCMp5ZJKo52anjSsAOjxO9itEcTMZmg1b2wm8XkBsBOy9ep_73l6sRnE5T-CyRXAC8wne1fAy4r33n_U8FePNmZYpI808H3KRtyXrCYUzlQe4UdyZ4sRimofkeB4oqoBXOyals8jOMHoyAudh8uJLr5b-DJJZWagPynHAObtP3TvsI92kpqG_BMUqS9bkkNgLOoCokg7oJiA8Go7_yceeBpEDzC7U3F8l81Sl3g5b-x08jGw-hbt_hPe23Dd5BeOc3V0iFhhJipqE3Q7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرینات منتخب برای قسمت های زانو، لگن و کمر با استفاده از توپ سویسبال یا جیم بال #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658325" target="_blank">📅 08:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658324">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
محکومیت ۲ دوومیدانی کار تیم ملی بخاطر تعرض به دختر کره ای در هتل / ۲نفر کاملا تبرئه ۲ نفر محکوم به حبس
🔹
حکم دادگاه کره‌جنوبی در خصوص چهار دوومیدانی‌کار ایرانی اعلام شد؛ دو نفر تبرئه شدند و دو نفر دیگر به حبس محکوم شدند. این حکم هنوز قطعی نیست و قابل…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/658324" target="_blank">📅 07:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658323">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mb8hY90jWRQqrNtsd8GxBbRYhQXo_Qf0Yxh7bOwjO8D2M35Lsb1lXWVFTwij8suALv_vle1l4Xp0d_gfJ9tFtju4rJdwo1oKOaxJt4e-f-2zjXC97IfKv4GUUWfNFNYNekvNQzCaHFm6ObgKUvjqeIiwZ1sF23J35h-LZl4hSeZleo1BKi1htr68Uj35PxLKyYnO02dpzdcPbMqXk7MWxZALqbDfYtTcz1hNi_MywkfXsQcwWZwVZtuGxJWid8ggKc6TNzjoS-W02yZrBl-plfqntvZ128RR4Wg0AuNmbgK700SUa20imImJQbVyUyFE6CtJ5D9uG9ngeFGQyBXXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محققان چینی: چای برای سلامتی مفید است اما نحوه نوشیدن آن اهمیت زیادی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658323" target="_blank">📅 07:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658322">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ترامپ خواستار تصویب بودجه ۳۵۰ میلیارد دلاری برای پنتاگون شد
🔹
ترامپ پنجشنبه مدعی شد که تا پیش از او «هیچ رئیس جمهور دیگری تا به این اندازه هم به بازسازی ارتش متعهد نبوده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/658322" target="_blank">📅 07:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658321">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhC7JOUwqcw26L_0S6U8fzM3IcZD1jarW1fRn2tLW0knlt5Szk5NSMD1DHMD8L2QN03rhjMFnlD7fwxkuWswsfd0JH8arijKxi56vV-RwJbeETPJ3XZTmvKAbkAWGiNnqJbjA9qobQqAr1LPb3Q2taHdBayVv-IjNUFI2zunrfia_MWMlroQsXUlORTVc3xWZVacUvm3ieJejug-crO5QJPPLvi-q-jg-jl_JuZnQ40B5UeAZYGL0In48rbiMDHB_-eQOpTvb9ocMqmzW6XKC4OxTVG3uLYvfsJwVsoekQbH1G4UUVHIn1IfsE2N-PVJ7PIkj2u92Qp6-ji-pCp44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۱ خرداد ماه
۲۵ ذی‌الحجة ۱۴۴۷
۱۱ ژوئن ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/658321" target="_blank">📅 07:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658320">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
هنرستانی‌ها باید از شنبه به مدرسه بروند
🔹
آموزش‌وپرورش از فعال‌سازی کارگاه‌های هنرستان‌ها با هدف آموزش پودمان‌های جامانده دروس کارگاهی از ۲۳ خرداد ۱۴۰۵ خبر داد.
🔹
قرار است فرایند آموزش پودمان‌ها ترجیحاً ظرف دوهفته آموزشی به پایان برسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/658320" target="_blank">📅 07:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658319">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D29fkjpEJ_oxqQBLgJJ84Ixuzwjvx58OftW9QO2E_5uIHCihOF3QdySIrG3tHYI2i3nDumzaW9g12vqJORIgIqG0pGHWg136g1XkWW3PxxRB2Qwg2g1usF_AgV95vbIPaGV_muEl1qXfHsSmq5ILDIgNP-D7USCuJvsYCRLsr7Yyt_dusvfYyQajUtmMKkgalAJ1tJGSHhl8JkG4fDtTEc7wNA1dOpV2F8kQ7m0_0yARa18wyAmYal1_DtwY_ZyEPhQ1RZ3UOXS2KDK_U9CgkZHLRNxVfk5ej8AvTRY1thnHoJFxKoK9rBUmRMa2zHAF4Pg-qlcAmte6ro-WkAi4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تداوم اعتراضات خشونت بار در کشمیر پاکستان/ شمار تلفات به ۱۵ نفر رسید
🔹
اعتراضات به برخی از قوانین انتخاباتی در منطقه کشمیر تحت کنترل دولت پاکستان همچنان ادامه دارد و این وضعیت به درگیری های خونین میان نیروهای امنیتی و معترضان منجر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/658319" target="_blank">📅 07:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658318">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا در اردن
🔹
سفارتخانه آمریکا در اردن طی بیانیه‌ای ضمن اشاره به حضور موشک‌ها و پهپادهای ایرانی در حریم هوایی اردن، از اتباع خود در داخل ساختمان‌ها بمانند یا در مکان‌های امن پناه بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/658318" target="_blank">📅 07:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658317">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkUOvkUTlIJE6Aiytd2CeBC0ERLcunat_cu2K1JoiuWtXymRq6eYvtogWl8moHdEzNktKOmpnXrcK8uF4DO03YgFuU5Ouulfl9_ayqCLTM4Z88KVQpAMgX9iYV8DGWJJJzIH5m7bsuX61k6wcSxxHkAn0m59VlQki83RAx6L3FMYQ1evA_bxkQi_4UQiJM5kuwUjtQ2wlwX7avzYHz98vCGWO5HsJ91YJ-GTxLkQ_fuO47X4TsccUDn5dDYUIeQtgsXRR19kEIMcTtiZIijesh7LOQD3jj1FbE7UFBcUgzIenB1HB9PoCht48pWXtzYEnnKJoQ-PcalARMgdq9diqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسمان کویت بسته شد
🔹
پروازهای فرودگاه کویت به فرودگاه های جایگزین منتقل شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/658317" target="_blank">📅 06:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658316">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا در اردن
🔹
سفارتخانه آمریکا در اردن طی بیانیه‌ای ضمن اشاره به حضور موشک‌ها و پهپادهای ایرانی در حریم هوایی اردن، از اتباع خود در داخل ساختمان‌ها بمانند یا در مکان‌های امن پناه بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/658316" target="_blank">📅 06:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658315">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924506c361.mp4?token=RkenmvkYOFFLNpNJsPN2EnalmsWnYt3m4RZFMfRQT9wmhjuz3al2pfkYwdF2mdj6vdfzsrxFPnfVl1C3XEjDX0ErXfhfrooWKR-ZxgtIszS8rQ4BDXvVo5JO65eVGWQ-Utol6ucQep3XxaNg2qGtmiHMdxqHrbREak5zqBJ9X5-wJnS_u3Xe9aZ4SXC0aQ4cIx9t8AGm-fGkEwjVN6btePaMNgOba8JBqafOcs8zNocxaLWPL9YgD8cPurkfZ156fUpZPpz4VePV7OCcGR-oIAHXwSLBJYHmvqYw7NPjIbhuIlFSuX5cWM6O81V5DDOXISNi_tPzOZ3fuc5D9p1p0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924506c361.mp4?token=RkenmvkYOFFLNpNJsPN2EnalmsWnYt3m4RZFMfRQT9wmhjuz3al2pfkYwdF2mdj6vdfzsrxFPnfVl1C3XEjDX0ErXfhfrooWKR-ZxgtIszS8rQ4BDXvVo5JO65eVGWQ-Utol6ucQep3XxaNg2qGtmiHMdxqHrbREak5zqBJ9X5-wJnS_u3Xe9aZ4SXC0aQ4cIx9t8AGm-fGkEwjVN6btePaMNgOba8JBqafOcs8zNocxaLWPL9YgD8cPurkfZ156fUpZPpz4VePV7OCcGR-oIAHXwSLBJYHmvqYw7NPjIbhuIlFSuX5cWM6O81V5DDOXISNi_tPzOZ3fuc5D9p1p0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادهای شاهد ۱۳۶ حیدریه در آسمان کویت به سمت پایگاه‌های آمریکایی در حال حرکت هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/658315" target="_blank">📅 06:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658314">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
محل استقرار جنگنده های F۳۵، F۱۵، F۱۶ آمریکایی منهدم شد
سپاه پاسداران انقلاب اسلامی:
🔹
در پاسخ به حملات آمریکا، با شلیک ۱۲ موشک بالستیک پایگاه هوایی الازرق و محل استقرار جنگنده‌های F-۳۵، F-۱۵ و F-۱۶ آمریکا را هدف قرار داده و بخشی از تأسیسات و تعدادی از جنگنده‌ها منهدم شدند.
🔹
عملیات تا زمان ادامه اقدامات دشمن ادامه خواهد داشت.
و ماالنصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/658314" target="_blank">📅 06:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658313">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
حمله موشکی صبحگاهی حزب الله به شمال سرزمین های اشغالی
🔹
ارتش رژیم صهیونیستی بامداد پنجشنبه تأیید کرد که چندین موشک از خاک لبنان به سمت مناطق مختلف در شمال سرزمین های اشغالی شلیک شده است.
🔹
تاکنون جزئیاتی درباره خسارات یا تلفات احتمالی این حمله منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/658313" target="_blank">📅 06:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658312">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کویت، بحرین و اردن
🔹
منابع عربی می‌گویند که پایگاه‌های ارتش آمریکا در کویت، بحرین و اردن مجددا هدف عملیات موشکی و پهپادی ایران قرار گرفته‌اند.
🔹
همزمان با وقوع انفجارهای جدید در بحرین، ستون‌هایی از دود در منامه، پایتخت این کشور به هوا برخاسته است.
🔹
همچنین گفته می‌شود که آسمان کویت بسته شده و پروازهای فرودگاه کویت به فرودگاه‌های جایگزین منتقل شده‌اند.
🔹
ویدئوهای منتشرشده در شبکه‌های اجتماعی نشان می‌دهد پدافند آمریکا در اردن در دفع حملات موشکی ایران به پایگاه‌های «الازرق» و «موفق السلطی» ناکام مانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/658312" target="_blank">📅 06:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658311">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed62bd9527.mp4?token=vSU5zIeLEJOn5c8JvulA3xcUsXDC9uwzkviD0Lep0TCoweu1rnyvVlGouH4n9V64brUbjJZyKbpLbarlsY5ilKzefC0UzdxKn8aAJjolUjmT_Ywuq7RTaFaq-W1arwY70SHq9ve7qtxW-f1SkBe5Rxp9wmx7rr4u6Q3lfIjQZOrmfBLfBwFnbW9_zEBvfAm4tIFQHhJnlc7x5Dh5N76MiwEp26OHrPBVwBczSisCdopN1t0b3GtW1Ghj9fGyOQFlM8zIqvXfLXocSAMhHKgjKIH9kC99VNoq2azl8FVdWiFgoj5jI7-EhWyn1VZl4nr8V3EQslnoio8UgYCF_1zpYxPkS8Iq94jhmSubDgTst4FMAUgxBMP2vtSCV9G1a76TYXoqjc9IAPc2NHcC2z4vQyl3n9lTX90RSGXBjL3M9UX-Ldo2CnRjFBKsmwAQ_CrBk-3b11GPMzjUJEOB0Lq7Ys_UdPnn9V4gpvl5q4UREJZo70xQ0xq7GSMEhecxzjTqPu-IwY1HW0O5pc5Sz2x95xplY02wWDHYkyo4FkQclOH2zCI9aReke_oJ767o2_2q61zc0mDBqg4sbrBhMTdO6dRPGWcmUBFlatTTSI4HUcmswx5ug-GZ8nrnnfIMtJoEmgWRAbaV7Yq7LQyOm5S9hPOFJOTBTIaDAgDOJ5szv38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed62bd9527.mp4?token=vSU5zIeLEJOn5c8JvulA3xcUsXDC9uwzkviD0Lep0TCoweu1rnyvVlGouH4n9V64brUbjJZyKbpLbarlsY5ilKzefC0UzdxKn8aAJjolUjmT_Ywuq7RTaFaq-W1arwY70SHq9ve7qtxW-f1SkBe5Rxp9wmx7rr4u6Q3lfIjQZOrmfBLfBwFnbW9_zEBvfAm4tIFQHhJnlc7x5Dh5N76MiwEp26OHrPBVwBczSisCdopN1t0b3GtW1Ghj9fGyOQFlM8zIqvXfLXocSAMhHKgjKIH9kC99VNoq2azl8FVdWiFgoj5jI7-EhWyn1VZl4nr8V3EQslnoio8UgYCF_1zpYxPkS8Iq94jhmSubDgTst4FMAUgxBMP2vtSCV9G1a76TYXoqjc9IAPc2NHcC2z4vQyl3n9lTX90RSGXBjL3M9UX-Ldo2CnRjFBKsmwAQ_CrBk-3b11GPMzjUJEOB0Lq7Ys_UdPnn9V4gpvl5q4UREJZo70xQ0xq7GSMEhecxzjTqPu-IwY1HW0O5pc5Sz2x95xplY02wWDHYkyo4FkQclOH2zCI9aReke_oJ767o2_2q61zc0mDBqg4sbrBhMTdO6dRPGWcmUBFlatTTSI4HUcmswx5ug-GZ8nrnnfIMtJoEmgWRAbaV7Yq7LQyOm5S9hPOFJOTBTIaDAgDOJ5szv38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه عبور موشک ایرانی از سد چندین موشک پدافندی در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/658311" target="_blank">📅 06:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658310">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آسمان کویت بسته شد
🔹
پروازهای فرودگاه کویت به فرودگاه های جایگزین منتقل شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/658310" target="_blank">📅 06:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658309">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رسانه‌های عربی: پایگاه هوایی «علی السالم» محل استقرار نظامیان آمریکایی در کویت، هدف موشک‌ها و پهپادهای ایرانی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/658309" target="_blank">📅 06:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658308">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
انفجار در پایگاه‌های آمریکایی در کویت و بحرین
🔹
منابع رسانه‌ای از وقوع انفجارهایی در پایگاه‌های تروریستی آمریکا در کویت و بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/658308" target="_blank">📅 05:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658307">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سازمان حج و زیارت: زائرانی که پروازهای آنان در روزهای ۱۸ و اوایل ۱۹ خرداد لغو شده بود، طبق برنامه‌ریزی جدید در ۲۲ خرداد به کشور بازخواهند گشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/658307" target="_blank">📅 05:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658306">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
انفجارها در بحرین و اصابت موشک‌های ایرانی به پایگاه آمریکایی‌ها، همزمان با فعال‌شدن سامانه‌های پدافندی، ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/658306" target="_blank">📅 04:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658305">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
صدای انفجار در ورامین شنیده شد
🔹
هنوز هیچ‌ یک از نهادهای رسمی نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/658305" target="_blank">📅 04:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658304">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
صدا و سیما: شنیده شدن چند انفجار در کرج و اشتهارد
🔹
چند فروند پهپاد در نظرآباد مشاهده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/658304" target="_blank">📅 04:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658303">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
شنیده شدن مجدد صدای انفجار در بندرعباس و سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/658303" target="_blank">📅 04:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658302">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
صداوسیما: شنیده شدن صدای انفجار در آبیک قزوین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/658302" target="_blank">📅 04:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658301">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
صدای انفجار در ورامین شنیده شد
🔹
هنوز هیچ‌ یک از نهادهای رسمی نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/658301" target="_blank">📅 04:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658300">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVYuv98uSrATBYF8LHhTvHbnFM1C8GhGFxPeQdoWgoaQvlEXUeSAHYlvFOfLdUtKQnnJsMM9Mk-3Y-eLui6pJ6ZagPBH8i5zYZCwSj6LMFMH8BwiXU4gRfD-VHlvWcaJJo2TzsgWxI5kvfOpSX1LEuYWzabyZ2uTsTiGsE1ZQkNGqwuB1SGF8rS2gMwtJUOjt-eN5W-3HhhssC5ciDFXKBsLJ4zxQbnESFwedjjenmoemti9gFSVkPvkIV17et3Ev8QhJqR-ezQzFbsStft27NqjV4U55sefXsjLR6qxNMmYKN311xx1Hi4txq3jxsMg5iokRIJ1UY3JtVjabyuzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار موسوی: تنگه مقدس هرمز را ناامن می‌کنید؟! منطقه را برایتان جهنم می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/658300" target="_blank">📅 04:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658299">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
صدا و سیما : هم اکنون؛ شنیده شدن صدای دو انفجار در بندرعباس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/658299" target="_blank">📅 04:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658298">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
آژیرهای خطر در بحرین نیم ساعت بعد از اصابت پهپادهای ایران به صدا درآمد؟
🔹
برخی رسانه‌های منطقه‌ای و وزارت کشور بحرین، پس از گذشت بیش از نیم ساعت از اصابت پهپادهای ایران به پایگاه‌ آمریکایی‌ها در بحرین و علی‌رغم سانسور اولیه، اعلام کردند که آژیرهای خطر در بحرین به صدا درآمده است!
🔹
این رسانه‌ها پیش از اطلاعیه رسمی سپاه در این‌باره، هیچ اشاره‌ای به حمله ایران نکرده بودند و سیاست بایکوت را در پیش گرفته بودند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/658298" target="_blank">📅 04:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658297">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
شنیده‌شدن آژیر هشدار و انفجار در بحرین
🔹
برخی منابع عربی بامداد پنجشنبه گزارش دادند که همزمان با فعال‌شدن آژیرهای هشدار در بحرین، موشک‌های ایرانی به مقر ناوگان پنجم نیروی دریایی آمریکا اصابت کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/658297" target="_blank">📅 04:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658296">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
صدای انفجارهای شدید در کرج همچنان ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/658296" target="_blank">📅 04:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658295">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMG0yGicefGiuRr25GDIo6Yxf5qAA4mQpLvjrIV3DrZeemh4IXeLk4HGHz2XJOFBZneT6SEznThCXcquv0rBj2Jjp87McG8D7ECCLMWTSwUUj94zvkzFE3E83b1ALgg1YaBH9_xOqoY7McKd2XXUcr9XS1xXYdO4iBWlqa9GZc3c2LD6rePoz_nPW9WKpHoRESn9EkkpdybeWf6eeXTbilp_FayxV9-yqVPyX9JRqlmbKgyats1o8PFDAMbpyzxFv9Eg27DnvoG_UYoEWzpRd2PnlA1kDxh1ePN-Yl5QeLROv2SdZscWKNWYWczOazZsoe3PBSwd0u4bDFp_BMMViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره ای نشان می دهد با اعلام انسداد تنگه هرمز عبور شناورها از آن صفر شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/658295" target="_blank">📅 04:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658293">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
شنیده‌شدن آژیر هشدار و انفجار در بحرین
🔹
برخی منابع عربی بامداد پنجشنبه گزارش دادند که همزمان با فعال‌شدن آژیرهای هشدار در بحرین، موشک‌های ایرانی به مقر ناوگان پنجم نیروی دریایی آمریکا اصابت کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/658293" target="_blank">📅 04:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658292">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
هم‌اکنون| شنیده شدن صدای چندین انفجار پی در پی در کرج
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/658292" target="_blank">📅 04:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658291">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
صدای چند انفجار در اربیل و سلیمانیه در کردستان عراق شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/658291" target="_blank">📅 03:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658290">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
هم‌اکنون| شنیده شدن صدای چندین انفجار پی در پی در کرج
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/658290" target="_blank">📅 03:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658288">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در آبیک قزوین
🔹
بامداد پنجشنبه صدای انفجاری در محدوده شهرستان آبیک از سوی منابع محلی و ساکنان روستاهای اطراف گزارش شده است.
🔹
هنوز هیچ‌ یک از نهادهای رسمی نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند. /مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/658288" target="_blank">📅 03:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658287">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
صداوسیما: دقایقی پیش صدای یک انفجار حوالی سیریک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/658287" target="_blank">📅 03:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658286">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
دقایقی قبل ؛ شنیده شدن صدای انفجار در اشتهارد در غرب استان البرز
🔹
منشا و علت انفجار هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/658286" target="_blank">📅 03:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658285">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
۱۸ هدف مهم متعلق به ارتش رژیم آمریکا طی دو موج عملیاتی مورد هدف قرار گرفت
روابط عمومی سپاه قهرمان ایران:
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
🔹
رزمندگان شجاع نیروی هوافضا و قهرمانان نیروی دریایی سپاه سحرگاه امروز در تنبیه متجاوز و پاسخ به تعرض ارتش کودک‌کش آمریکا به بعضی از واحدهای خدماتی و پاسگاه‌های ساحلی سپاه و فرماندهی انتظامی و محوط فرودگاه بندرعباس طی دو موج عملیاتی، ۱۸ هدف مهم متعلق به ارتش شرور آمریکا در پایگاه‌های هوایی علی السالم و احمدالجابر و همچنین پایگاه‌های هوایی شیخ عیسی را مورد اصابت قرار داده و منهدم کردند
وَمَا النَّصرُ إِلّا مِن عِندِ اللَّهِ العَزيزِ الحَكيمِ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/658285" target="_blank">📅 03:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658284">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
تسنیم: شنیده شدن صدای چندین انفجار در پایگاه‌های آمریکایی در کویت و بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/658284" target="_blank">📅 03:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658282">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx3bwZk6msiSHdhoXWl4mcJNjdsm1AXaVf1bt4WvJfD0LVG8M7n0zun9eXB2IvrLkgIhHRDkGE1zkW9UXUvyeuyYoYnNB-pHNv3iZlFOacdrDJ5CzXaBHgBbAdoVbYx2Ts6KORJK0xGZw-2g9kPU9bP5wZpQR7fBxtlZXPTl9E1tOLrsW2xd2B46bi6bCm7GBDzUu2F1tdlF7IvmcYjIwl4UYXLNrp7aDH6Aae4x7JDWgpvoxuPJ_BKOo5Iu6sAyONcyA3AEJ54Gc10OFNm4LTRa9a2wfCDOaA6MxZ_rl4zEKPzLbk55pqcpcjBcmvMu3ZMJ-cWqYkXWYCXzYfwcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره ای نشان می دهد با اعلام انسداد تنگه هرمز عبور شناورها از آن صفر شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/658282" target="_blank">📅 03:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658281">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd9f7c8b7.mp4?token=Rbn32sGS7Bpa3_rIGwZPjBHA24yVJi15SKVMmcn2SlVLIN2QnJRXoxOjNxGTxvMqj92zJz3kDLiaCDxDfG0L-Ub9D7lRBlvkg0EMRzJAtQeAdn--l1jcsmvhSsVzlAlVcgtKU_L1ZadAjhY0-zI7fHaKVNRqFvGVkgkAfqs3oOqRrrsM93ixb4qiegALguK_QPI7YFV0-sEeYYSP8A-Cbx8OoQ9bJTzdtWp6UjVNbEC0QTxbkxPbczQrLZsb9QrdXDe_jTH3SEkoRb3II5sphixcVL-xVyCznh2NAQwVt_5ZM1d2b4RcGRCQHupwUJ3bNwGrdEg-rlz8PPwMbl5U-7yFcE7VMfqNbT19d5ts1sxc3n9M41StJQtD1UuF6ES9BWjrIa4xKDb8KGAjOsvPZZSZ0iH1WnhwkBlopXgP9riEiNphbxiwo2RD2ANdTzIVXSj7ZOpTN6ZzsTqo83JcybAjCAorBOUpbcqcu9xQRuhGG3Nn-eQHBIvYF4Eh0NmqIFWkzYe2nNaeG6REvjqFT9yya5rLnzebRFGvxfGKrvNmpYpIbF6tFM4i8aPIvpK-4m6Tnko8-muUtXXfqS47iopI9d8MqFqQlrHFBRCFukWPAt1p1z0yeyxdVUhnoBxyl8Y1IypP5Ef4vcFVxoVKoJ3wCAHT2ZH-XVe1BjGVz0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd9f7c8b7.mp4?token=Rbn32sGS7Bpa3_rIGwZPjBHA24yVJi15SKVMmcn2SlVLIN2QnJRXoxOjNxGTxvMqj92zJz3kDLiaCDxDfG0L-Ub9D7lRBlvkg0EMRzJAtQeAdn--l1jcsmvhSsVzlAlVcgtKU_L1ZadAjhY0-zI7fHaKVNRqFvGVkgkAfqs3oOqRrrsM93ixb4qiegALguK_QPI7YFV0-sEeYYSP8A-Cbx8OoQ9bJTzdtWp6UjVNbEC0QTxbkxPbczQrLZsb9QrdXDe_jTH3SEkoRb3II5sphixcVL-xVyCznh2NAQwVt_5ZM1d2b4RcGRCQHupwUJ3bNwGrdEg-rlz8PPwMbl5U-7yFcE7VMfqNbT19d5ts1sxc3n9M41StJQtD1UuF6ES9BWjrIa4xKDb8KGAjOsvPZZSZ0iH1WnhwkBlopXgP9riEiNphbxiwo2RD2ANdTzIVXSj7ZOpTN6ZzsTqo83JcybAjCAorBOUpbcqcu9xQRuhGG3Nn-eQHBIvYF4Eh0NmqIFWkzYe2nNaeG6REvjqFT9yya5rLnzebRFGvxfGKrvNmpYpIbF6tFM4i8aPIvpK-4m6Tnko8-muUtXXfqS47iopI9d8MqFqQlrHFBRCFukWPAt1p1z0yeyxdVUhnoBxyl8Y1IypP5Ef4vcFVxoVKoJ3wCAHT2ZH-XVe1BjGVz0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش زندهٔ خبرنگار صداوسیما از بندرعباس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/658281" target="_blank">📅 03:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658279">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
صداوسیما: در حمله خصمانه تروریست‌های آمریکایی، دو تن از اهالی کرگان شهرستان میناب بر اثر ترکش پرتابه‌ها زخمی و به بیمارستان میناب منتقل شدند
🔹
هم اکنون آرامش در شهرستان های بندر عباس حاکم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/658279" target="_blank">📅 03:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658278">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
صداوسیما: تعدادی از شهروندان در حملات آمریکا به منطقه کرگان شهرستان میناب به شهادت رسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/658278" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658276">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
وال استریت ژورنال اولین کد عقب نشینی آمریکا را صادر کرد
وال استریت ژورنال به نقل از مقامات آمریکایی:
🔹
ترامپ به دستیارانش دستور داد از طریق میانجی های قطری این پیام را به تهران منتقل کنند که این حملات واکنشی به حادثه پهپادی بود که نزدیک بود خدمه بالگرد آپاچی را بکشد، نه شروع یک جنگ تمام عیار./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/658276" target="_blank">📅 03:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658275">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
مرحله اول عملیات‌های تهاجمی موشکی و پهپادی هوافضای سپاه انجام شد
🔹
پراکندگی مبدا شلیک‌ها و فراگیری بانک اهداف، جزو مهمترین ابداعات عملیاتی سپاه پاسداران در مرحله اول عملیات امشب است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/658275" target="_blank">📅 03:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658274">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تسنیم: ایران به تجاوزها پاسخ نظامی می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/658274" target="_blank">📅 03:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658273">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای ترامپ: آتش‌بس با ایران، نقض‌شده‌ترین و ناقض‌ترین آتش‌بس در تاریخ جهان بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/658273" target="_blank">📅 03:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658272">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
عقب نشینی دوباره ترامپ پس از مقاومت قدرتمند نیروهای نظامی ایران  ادعای ترامپ در گفتگو با شبکه فاکس‌نیوز:
🔹
ایرانی‌ها از من درخواست کرده‌اند که بمباران را متوقف کنم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/658272" target="_blank">📅 03:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658271">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
عقب نشینی دوباره ترامپ پس از مقاومت قدرتمند نیروهای نظامی ایران  ادعای ترامپ در گفتگو با شبکه فاکس‌نیوز:
🔹
ایرانی‌ها از من درخواست کرده‌اند که بمباران را متوقف کنم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/658271" target="_blank">📅 03:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658269">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای ترامپ به فاکس نیوز: حملات شامل ۴۹ موشک تاماهاوک بود و از شب گذشته شدیدتر است #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/658269" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658268">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اسرائیلی‌ها در این حملات به ایران نقشی نداشته‌اند/انتخاب #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/658268" target="_blank">📅 02:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658267">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ترامپ به فاکس نیوز: بمباران ایران به زودی متوقف خواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/658267" target="_blank">📅 02:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658266">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
عقب نشینی دوباره ترامپ پس از مقاومت قدرتمند نیروهای نظامی ایران  ادعای ترامپ در گفتگو با شبکه فاکس‌نیوز:
🔹
ایرانی‌ها از من درخواست کرده‌اند که بمباران را متوقف کنم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/658266" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658265">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
عقب نشینی دوباره ترامپ پس از مقاومت قدرتمند نیروهای نظامی ایران
ادعای ترامپ در گفتگو با شبکه فاکس‌نیوز:
🔹
ایرانی‌ها از من درخواست کرده‌اند که بمباران را متوقف کنم.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/658265" target="_blank">📅 02:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658264">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
معاون سیاسی و امنیتی استانداری بوشهر:  یک منطقه در ارتفاعات در شهرستان دشتی مورد هدف قرار گرفته که بدلیل سخت گذر بودن منطقه هنوز منشا آن مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658264" target="_blank">📅 02:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658263">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تنگه هرمز تا اطلاع ثانوی بسته می‌شود  نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
در پی نقض مکرر شرایط آتش‌بس توسط دشمن آمریکایی، تنگه هرمز تا اطلاع ثانوی مسدود می‌شود.
🔹
هشدار می‌دهیم هیچ شناوری از لنگرگاه خود در خلیج فارس و دریای عمان حرکت نداشته باشد. نزدیک…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/658263" target="_blank">📅 02:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658262">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
موج دوم حملات تجاوزکارانه آمریکا به جنوب ایران
🔹
یک مقام آمریکایی بامداد پنجشنبه به شبکه «فاکس نیوز»: «حملات نظامی آمریکا علیه ایران ادامه دارد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658262" target="_blank">📅 02:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658261">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
هشدار آمریکا به اتباعش در عراق
🔹
وزارت خارجه آمریکا بامداد پنجشنبه به شهروندان این کشور در عراق توصیه کرد که آماده باشند و شیوه‌نامه‌های امنیتی را به دلیل خطرات احتمالی رعایت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658261" target="_blank">📅 02:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658260">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64da998bb1.mp4?token=CAEp8VkrH3KqQgtniJx3-2AN6xLNL_yeEhR90c1j1zgxmRz7ftboCRIFxKLJpnPY9KHdMKJl76b8Uq-7fgSJwuw2YEH-65eLNAeDekUJDUqbY-3L8ybAgl8WOa9_PcaxQEK2NoA8-8PuUW638ZZyxxJ-k7p5OTvAl4SNKYmdDx_bYAgTw-8Kjiy-vPnP8W7n2jKLckin5e7V2WgU08OlVAnDm2lDX8DYlRUBGFiqCrl1bZKhP-cS47yFHf2bD3iVQNWlbEkyMNHqL50ruo_UKUIiJGiIQuKlLRK_GZEV0Yb7fyZx5u1NQ1DVmRrGgWxzAEAmee8_uq5arUM-Y7-nyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64da998bb1.mp4?token=CAEp8VkrH3KqQgtniJx3-2AN6xLNL_yeEhR90c1j1zgxmRz7ftboCRIFxKLJpnPY9KHdMKJl76b8Uq-7fgSJwuw2YEH-65eLNAeDekUJDUqbY-3L8ybAgl8WOa9_PcaxQEK2NoA8-8PuUW638ZZyxxJ-k7p5OTvAl4SNKYmdDx_bYAgTw-8Kjiy-vPnP8W7n2jKLckin5e7V2WgU08OlVAnDm2lDX8DYlRUBGFiqCrl1bZKhP-cS47yFHf2bD3iVQNWlbEkyMNHqL50ruo_UKUIiJGiIQuKlLRK_GZEV0Yb7fyZx5u1NQ1DVmRrGgWxzAEAmee8_uq5arUM-Y7-nyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار شهید طهرانی مقدم، پدر صنعت موشکی ایران: جمهوری اسلامی تسلیم هیچ گردن‌ کلفت و هیچ آدم قلدر بی‌فرهنگی مثل آمریکایی‌ها نخواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658260" target="_blank">📅 02:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658259">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
گروه هکری حنظله: بخش بزرگی از موج اول و دوم حملات ارتش تروریست آمریکا تا این لحظه به‌خاطر عملیات واحدهای جنگ الکترونیک مختل شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/658259" target="_blank">📅 02:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658258">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
نخستین مرحله تجاوز آمریکا به ساحل جنوبی ایران بدون دستاورد در حال پایان است
🔹
برخی منابع مطلع از امکان توسعه حملات کور ارتش آمریکا برای عبور از مخمصه کنونی خبر داده‌اند./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658258" target="_blank">📅 02:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658257">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
تردد هر نوع شناور در تنگه هرمز ممنوع و متوقف شد  قرارگاه مرکزی حضرت خاتم‌الانبیا(ص):
🔹
از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
🔹
در ادامه شرارت های…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/658257" target="_blank">📅 02:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658255">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
پاکستان: به آمریکا اعلام کردیم که دیگر دست از تلاش برای میانجیگری برمی‌داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/658255" target="_blank">📅 02:34 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
