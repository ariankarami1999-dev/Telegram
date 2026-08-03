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
<img src="https://cdn4.telesco.pe/file/LHOFFhiazTWK7cVhJgmWtwL7gCMmVeMTDmPvPB-VYMQQ7oprYo_Q2SlDuiiRLKtY_r2jl1H0ylOKDqHnXkk0HyUJGCCZqkosH_Nl4lbMknjVER8kTbcMojyFiecAbosRqZ3lK7H5v18s-tASzdgmoK0vGp8RraI78Qi3nJhOZfPN5tt3VgTuv7Qb_Ce9q5lmObkDnmKNPCvh7rZUFGMIUEm3XxxOqiqL1mVp7Zm7RWRH57TV6iXBrsnsOeiZjgbTkzkgQ4HrEF9EHPzk-F5d31LHjy7lyV-HR61llYsSYbg952r7sK3zv33pG9sALRdUqVqdlqiffxyc94mWCBEYPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 618K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 11:56:10</div>
<hr>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwQ5OBpHPx7pYSYauVAm7SyyqcrQR12S2FVk5UJdljRJf_FXb1HJ-eWYoFt0WYq8at7aHmbXIfRxEAeVRNnX3ApExP4DPeTME4a1wjTDDLMtX9UMvgUM32h91haDItmwx_TU6vdAaEaM1vdHzehCTQKXdOc8_DlzGpOQdJhi6KpR6NPnv8qqoSqUQ78fL5r3mz0V-sTL7B5KqeZp34q4fCeCeQTfW16zyAnwz6bLetL9lti61WwNmyBKgVJKQlBGLM1WDgC_d3_LrLZKzie4s8Fj5_VOpPJ7cdGatelnJ-VMrf2bMkFbeldbNK18dAs5UPAAymJN-BBGbS_zS4nJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahm5JMMp_dTaKJXmsYQKDa3V1NSPh5fMwRWKM8X0j24b7BITpoXbDwfW9Cjg8klCVv-OrbzZ2QFkRPQL6HY2u-k0AJusCaZcr0LXmkWeJmXRb3UzNyRAvqoxvc-nY0zJDJ4MNJvZ2NeMUrkEUsBmEGfSNXMTsul-XsHuvqvswXHV6vtfkXOjSx6y88s0ojkB_ktzKhI218bVhi6jZ4bFcwK3035afobNggWo-HKIyvamsxr_Mfan0u3rhAhJIp4uJ2ANql1Av7eVlNwYtT4zNRe5mqtj15XRa4gk6F_r17csQCZsJnH_A1u1gV9SOOaksA1Bem9uG4bYm4XYDFiFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWKlj2Q2SNYbehEmjcLUYnrHSgprVuOM1pt2IRf4FXPYFXjZLrIWfJgRAAEVuumICY5DEfo-IPQbsjR_nnj5WME0DR82N-lCdk8i2yjx4LKdzJMcyGFeVJNUP4cH4yyYb5RwLoa3IkqUTbnCtKaEJW3MrS4mshSfN1a-ivd06Un4BSlSTFVkJZHsNFmpc_1dwRB0821ApZCtBi4RBwm92PXyDaI6M9ZEAlLgBF9v0-Quoyk2ePItr5TPYKLysaJ116qPyVGh8qYKsKfx0RVKwZrPWxVpg7kAnDyL-NieIqJjKkjKnoRxeakHKPwVzVy_37XbjSnMR9QNFXCi4w4TLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-rNqPJcouuWsOqSu3e1kTCiWohimJkl7w-0gfnFMujmv76MM0DiSewLNNaGke8riyFSzGbKlotNlkMKZmJAENGvFVQJ1n9u86FNiH8wPrGDDvP-BLcBveNIGRAHoby7zuA6-eyh3PZ5x1-FvoRujEPruipAQXPpC0z71gDJ4MFE-dX7bB9TnR3nVPURkGGOxdPomZh9OhqKSPQTfelD0p_RbXgEatHyQyYpxJL-CW-uucHpzai7DjkAwVFurcUDKljw4tAG0zVOZXvWzj5rdbxEakzCWdYfZL0B51aZ8zHGQAjpEXZLPMb4J47aGnXH5o4tynconpXv9HbydB-lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5EGC-36J6cPMSMH7yz2DedDrR66rKHzDq_NIhRGQl3069m7S5m7N5oe8zhYyYIsh2WeOC6fxr2rTPIgb9eXOCyUz6NK08Ss1JSmJGGqvV2Pa7yJBYEK5SrCu-GgrPerXnCTuHAkahjVKqvTqA6ab4sw6nWeWAAb10GIoqGmeKigVbJVFTuhGWSu36uzQ1qRQT21cB6NcggLe-kr9bUqHzUhcEaJ-amYE4NKKUXhxlkNznNCBg7V4UkZbaN2oeHHfQh-IGR1WuMtPQBfNfQg4qfbhvVIPFRhJsckTTtcf1wxGoapYjCzblpUy4QBSii79PWDY3WtgZy_YU6MJtCTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFA6-I_HHcCFGVn-0kd_wF7_vF2E-YPA_HSp3eLBF1roahFI3Cc_F4oz_6AGf5iuHMRi6hi2073fxYEm04BSBGyp1NrjSbqFA_gVrllktv5VLHUWm20XQEj4HSJsjD8o2xyXKJTVFF464A-BljBBn2zS48VO4KDtQfYax62RFxdZ2HVBbqmGdagzwaN1XeXpfYTljGUKNM1lWtNS5LvB_Is-dq6NjwGXq0BDRVUkoyCJcfyyjgjMG54YRxHq7O32ZmQyQ0SnVHuwizAT-B3o-UwvtZr2NN3E_fOK6BxNCh7I3MmZHVOxIU6Ah0q3ZveJKD6vAuH4y1phExXFZ7g4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvkvtPvLbNxXMvPqOx3nCzzCxgX7xfKnfpdw1sAQGcgX8GNArXh-UU6m-5cfGHL8V5tOzJexwEyqqbUjqFa0F1aTriJ4tINWaa_iXef2LFuU0lxM_R_Uk2VbtMdunPIzNgD_RL2FRrU73vHM0jm1T-dPBiEcs6HGnjjThkwwuvdVFmitSSzqN934nH9gTCihhlAzXVg7SblL-Om3O1P-8m7BwR2vKeBTlsk0aLe3Y4bt2fsVXvf7QcjCcTTd6VghnVFi5nGlVGRrpPE45qPg8iPdIuCccUs5Sm2Sj6BE5nB7O8a3WFeDfLS_yEJVCs8xJi2cQfzRbEUe7h2gmx1JpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=bKWBaWbo3hNW9s6r6bWwgTus5ClTEXv1XaZ5N6i4O01t4zH42SdOKe6IVnBa2rCRw7dsvAy6aDUYdHeOiwBczG_aqWBR9eyTZzcL887YXUro55Ee6Czc3Jb77p8XY9yI60Oj3SRM4QLspbCcqVKNgTEcfdASxiAX7MBNoITtdJTiGUYKFm-A_Uhqtb3owX7faV-7FrSzDD8__2u1zXV8SiD4XoH6CY0xcCJh9KMdte8sNu39vB-thCNZ2lFauEYbEYBYxr0w6q5LE7FldyXezp8JKqwv_Yq6hvvcGwRnVdq4QVMo211IDXhl4F5fN8X1XHt6j0g4xtMNn2BsQ-avZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=bKWBaWbo3hNW9s6r6bWwgTus5ClTEXv1XaZ5N6i4O01t4zH42SdOKe6IVnBa2rCRw7dsvAy6aDUYdHeOiwBczG_aqWBR9eyTZzcL887YXUro55Ee6Czc3Jb77p8XY9yI60Oj3SRM4QLspbCcqVKNgTEcfdASxiAX7MBNoITtdJTiGUYKFm-A_Uhqtb3owX7faV-7FrSzDD8__2u1zXV8SiD4XoH6CY0xcCJh9KMdte8sNu39vB-thCNZ2lFauEYbEYBYxr0w6q5LE7FldyXezp8JKqwv_Yq6hvvcGwRnVdq4QVMo211IDXhl4F5fN8X1XHt6j0g4xtMNn2BsQ-avZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371eeda394.mp4?token=WVWHg8KdGYsPwmfM5yPVEQPpf3CbDam7soEuel5T0WljmVw-nJzb0LmkuJZOD_HAOM8032ebutGXhCOKtKuCjg5IK9t1SO5uwVJuoNQS7s18nwMrfdUYw6q_6b9qYAFZjTzd2wHiBVcTScNpZS77BMZaZ98c3hRvds35xFhA87e4wEfVkmel1-iVJZ8ApAjJI_2a7ym8mvGRVZUGDxZrrWltpHbyhxREGXGwvJ9W_zvOL6v3fh1zXHUsBkS_LpLnZyc9lNgs8b6YjzgXVzm-VlLeci7PJki4GNgYiWr3iUd_Xhre7eFMB3uYZz3zvR6a1hqhxnzZsB7X5D5xd2u7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371eeda394.mp4?token=WVWHg8KdGYsPwmfM5yPVEQPpf3CbDam7soEuel5T0WljmVw-nJzb0LmkuJZOD_HAOM8032ebutGXhCOKtKuCjg5IK9t1SO5uwVJuoNQS7s18nwMrfdUYw6q_6b9qYAFZjTzd2wHiBVcTScNpZS77BMZaZ98c3hRvds35xFhA87e4wEfVkmel1-iVJZ8ApAjJI_2a7ym8mvGRVZUGDxZrrWltpHbyhxREGXGwvJ9W_zvOL6v3fh1zXHUsBkS_LpLnZyc9lNgs8b6YjzgXVzm-VlLeci7PJki4GNgYiWr3iUd_Xhre7eFMB3uYZz3zvR6a1hqhxnzZsB7X5D5xd2u7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
آرتور ویدال ستاره شیلیایی سابق یوونتوس یکی ازبهترین‌ پنالتی‌ زن‌های تاریخ. ببینید چجوری میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huvTI1lTJ5T0fa5iHuckWZP5AJEIR2hSOPVg1RjkgFJbvG5QxYJO-NokWhKRjtrClIG4YYNiINFVlGofcWDyI75_hJvqfjKTG8yFq3SVt6E70U858U0Xk1LA1n2y8UjZwQIW7W5kRxyMW41LHEC2hfIwNHVwAUHQtvxPpO2r0_gapbEu2u-mLqN2ciU0bsxBCHUEx51F0BGxQWwe1fE6k0HU6FbZfMYGX2ieAk69ZOJDaVzKef6ZgBaPOUF5C7_P2bJq-6hZF8zgqBrFExsTPnLRjWewFlgyUm3RXvgcZESjmLdr1110ZEd9Ee-qb8gjHZnnoZaA1oLM5uj04b0Flg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=jHYJZAC_1OxYHmCSWa24VX_2eK1a785YF-_a1bk_HPCPDLCx8QiM8LpII1Y7Lx9NY-1Z6KXvI0h_6geGhbSebHa5bsg867uurO4GwP_omdyrYmmWcAZh1C3VFbYcaJUQcFHR_UxZ9vuvh46g0KKtVQ-WSpKBwDmeZCXot4lUO6AABMaU0XaFZwKbRYZhipFv67qzQnKIJVpMFUOU79QaDMXRu3wHOCk7dTDr3ssz-wI9MulUDJ1i2_2xpLZQwgnF0b9NjIaF7TU0zdMcELOjFUG5W9PjaS1N-U5P5zPrxphCBC9r4c8-PcShUuZl-ts163vEACAL456ABtsNESfOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=jHYJZAC_1OxYHmCSWa24VX_2eK1a785YF-_a1bk_HPCPDLCx8QiM8LpII1Y7Lx9NY-1Z6KXvI0h_6geGhbSebHa5bsg867uurO4GwP_omdyrYmmWcAZh1C3VFbYcaJUQcFHR_UxZ9vuvh46g0KKtVQ-WSpKBwDmeZCXot4lUO6AABMaU0XaFZwKbRYZhipFv67qzQnKIJVpMFUOU79QaDMXRu3wHOCk7dTDr3ssz-wI9MulUDJ1i2_2xpLZQwgnF0b9NjIaF7TU0zdMcELOjFUG5W9PjaS1N-U5P5zPrxphCBC9r4c8-PcShUuZl-ts163vEACAL456ABtsNESfOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODVKBsvp33LVPzlWNvBejbR28J0kJvnIb8nfSCVfLG8t4f3NgIb220AQ2zEE6N3JeUfS9jlv469b-ZUemeHA2-L1aGA78SjxxlAnfJInAoRrwruJkVwLzWMZEhJE796jYjHMWAZJIIeqIVqId47i89N94u9xX0cOVXalckTg2qqiQOSzR9qlOq5bTiq9AeGeOlYTt26aX8rCWcK2hIg7arpCi00L9MspHiOZwnWg1TqwVYXdMukK_CVfRa_RoKF7IsjAohPhzghyY03lAfWq7dwLPpGmL2y7k_iSMbo1pJCxmINRK9zgZam4485xVWmNAUJ5wZ_wXYM_G0-lwEzVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMXV3VYGb73K0vFtmL5Pf57-jq0226FVbi76ZNbTMaWQlcWkIDYzixccL_rdZw6NU350YjmWNUg-xA6Q0Vle2f5X5JTRRYmhKYDsfIgCvVylemSA9OnhYSxHkWLBvqnEGnlanVjkc9HH7k7wCAGG2CzH5i_idOpExpon9Sv5lJ--HzhqMslkkARaIgLqKtOrKbzDizAw6bFNw0tnLLYwp5oQODygrL_sxXmM11tA0eb0aRs6I9wkbbObl52auCWGsJ1m2xQdRA8j9saRNLARdB8UCf6NeaPwUdwlERgtoYuwaR1V3YXWUo7qmUTDdAUTszH9FBAQCXGZIS0nPbqX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJo9enwt4zy58rIfDVqfnXv3kl7voNMgPrEsI2ERojZtXbn3__8m3DSrF4UOpYszAh3yBo1goNI0Uq1xZXD8md_5vwzitfS6b-Mvt2ljkIR7_ecJV0NuWGRHot9DtBTKyzmFI5ADPswA6LaydP-4m1B9QJFQjh4Hw5nJrnpcqHTEfYbXBHudv9jvALFKWMq_IcPXQ3p5oqdgQcHMgkLX3sLs3drSes4dqI8lBG_gNHGOdZC4vMFuL-YrnYZW2Y9iTaVGFJ7Oo-rgl15YqDnDD2Rz8d3tfZ_DHXwLGQYYxVxVelVVaTb2_lJo6R5Gf3noUuD-a76IaK1wHCpLcRYE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0AKEHVxaRhZK1UUZdxNVs9PBb5MRaz-cujCXOlLZ4c_PttON8vJHaZ0nwyaUyan4rAe7eEg7L4nopTAAqrpEnbGzIhtPHgZK2h8bTykdurj6j-Yz0HyGLJHTYfCGQBUR68aESYpYhpQtDFGDVkfOw7aCga-qKRW19QXpv5Ut-DULw2c-Qux6vFcj1zMD9CvFN50DNwj1Id5TAtD8RkMVp2bn_XGaDo3b4lMxbKvixP2v1gfRu-SZQpRALdf7OISaLWEZTPAoBW4S5UxTjHbHyPpMbqPPxSzngnrfG3Kqss7qc1gybwZ2a_6xeku9nsmDpPkYhZ1FsEv2tGGu8mJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mes7OGWkTAMIN169w8KBJG_sh4houu5KyWO7pexV3zsVnD25Dhtm_IotW8iiNWpBT-4ci8TUT0x1g-mrrjC__v9fmFdmesykSow9GL3X3xlXXjZWLmip43UUJBN8MjHplBVJ-TfKTIkUF8QU5GRNWaGLOk6v6X_cGymsngeBkWgeFhtnD-Io7dmWt-QhwYqcEa4B0pERhR6JlT00tu4c5vmDmZ7kRcMJ0lJWEBO3Ow6O3dCxDHkXmk7iOvMunjuQQFFKdpQ34GNsXLL3vtzZaxcNwiezEfcvx4VGIojzfFYcuHRwU8FUalyJuFC1i0y9Mj-G-HSqZfdwjZQTjnYz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrNzNh6bV3tJJcOW60H0j7U9q01LECRyOK85_LUZ1WU8MLoOCotjh1GKdtMu3MQaA2zzWTm9IUkiFHtPblVy-XbdLH6mJTGjSYy_69HDkKVtMSuOdulPw0N_s7v-BMaNeak9AxQ68UB9Lqeh4ZvIgHF0FG3BwzFFHmBZ5JHWOKUNTEuwCl9SBCue9vkw8yLsgEXKTETkuuYSCEIwyEc-i8_t-zt8tlj-phr8wDv0v2nE8ZD7rq5X2uqEt-PP0EBuYncR20XtuF5wvHSmrLIfwWbiSFQ-ng9TfvCbqUQX56QJLkVdgXiV8BDnCStPvn-r98N4Dq81b7_FsS3RQc8jIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27023">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGo9NwkkDziBUxWOOigOqedvpCTetYt1SPhSLAi7Sy1d_OtDEOB-_xLA6OFmq-aufafP6ig8wfIcGzKC5SqKU8M6DH0Xm_yIAdPK2mhIjMuDv_q5e4TeXD5gUXhkQDFrwzosk5tmhxfvBOyjmny0iqMmTpQUi4pybpkWT5LWDnYsxtJHrG5Uy-nQ0NurlY3tnQOlDIG8J5y8QkCLZk3k4mLaBefhw7gKpDBLA97lNABzhcuwYOBe0YYP6xB7lv5ztVdrpsw4Bukc4c_b23BsX3FYmPXqV2VNmcK6gZgdX4gjvbaTGQMFyvHmEQKMYgporijzk6X7xfOSHl32Ni4WPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27023" target="_blank">📅 22:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27022">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMMKvOvdjzx80lvPNdW8CVDcDMz1ELu288W9WSclaAoTxdWoVe6H-sMn_FU77sjpGJVPmjeFffflNY1dno2gWSGYVedX5L-qKke_d7x6_Yii0JbH2sVIplGomTBR2iibL8NCb7oNEzfkMLUmDN6RQEJQl0sz0neWy2utXW_yga5tpR_6zotFanGoKTFBR2F1XSZBCjMFw8rkcF9KW6o-Aqw_yBakY6zBgtxp_eNbv465tkX3T2S9G8Q1LmFaZ2zOErVNSCm6DolBTIy_Y9MnkEKh3f2Oze9cc0SnuIu-sXlQV3EpnN6hvVQxto2labNI7wtNlGBje67Zap1p6TlNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27022" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27021">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi-IfJfrN77ghCOQbMKxdwoSqsd-h8TiZrsW9Ssi__f-9dbn5XZo6_NeBeg9Uxi1MnujX3N72B9Dsc2M_Rx__UC-dWljzMIHSDL3utsKpwzILWf5v6_BLMamDW-KL5N08L1KSPbMvEllea84qPhEPsjNfqbkjgjg-FqOPvteV3enYIKg68WIaqpmszeks-LG34jPHkgNxt_vtr5HSdW1SSdN7GgOtT0RcoeYVD8OBj8ZlZrkOJ25G40TYnlISSb2pjK68yzdTh0jXDzrEeHkJFk8DaPTpoq5rPiG-7i6akee83khSQKoa6PkHnD74llC-hJVE-8qvWl9RIgrwMn37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27021" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27020">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjGulgGRZquHXDPRWDXxV-vMy9xOcXzfe4CFT6FgmPY7KXpK1OejKL1DDFowRGjpLXIkplUFMweVQP2_a1D4Gj5qKsyZ4EdDrnwEu5pYIrFTTqgBGp_TxyTBeez-cYIjSd8kutWJRDEqn2kqKF_X1kISWphvWdw3Ki5EzDk2Vjt35cgoakkm8UnVJDT5_sU85F-zER2qm_hHYIjdXuOY39Cb7SYt0lgszXcKWbo_zMez7I6CottSMxaDcGtTdGIpajLUXEKhPamY10WaDBXFT_JkRzgq0M6OzVj2OMK-15B-vUk75C8rlClsUIdFMoLQpEyoZVnb0PjAvmEd-GW6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27020" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27019">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=qP88JUVm2HEFcLuoUx6otWffHwSbFiP5udcLdCjK-5EDWAzWlDo9Qy0Rmftlyr4PIYzBh63MpuWrshZBCTnVigqbHXIQbh03yuxDCrqGt8MdkLi6Ykw66dK716lxkwTXSJdIDqhNnmuHjb2wdOpJqVtG4Ls_wEDaIOAtgxjrq1jmFYFyM40V2vEQ0yufjg0Ztb7_Q_JTBnI1V-No-uUwNUx-TDgOvC73AbN2W_Ab6uP_-Ix5WOqF_ORGaWUrpPgKIdtoB1GQO-ERtz8_-_vaRt3ycCfeQ7a6BTXVlkMtM7qbqaW83ywUQ7bXwRhVyOTuxE5zQ4fcSe-ffHRDwsrpKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=qP88JUVm2HEFcLuoUx6otWffHwSbFiP5udcLdCjK-5EDWAzWlDo9Qy0Rmftlyr4PIYzBh63MpuWrshZBCTnVigqbHXIQbh03yuxDCrqGt8MdkLi6Ykw66dK716lxkwTXSJdIDqhNnmuHjb2wdOpJqVtG4Ls_wEDaIOAtgxjrq1jmFYFyM40V2vEQ0yufjg0Ztb7_Q_JTBnI1V-No-uUwNUx-TDgOvC73AbN2W_Ab6uP_-Ix5WOqF_ORGaWUrpPgKIdtoB1GQO-ERtz8_-_vaRt3ycCfeQ7a6BTXVlkMtM7qbqaW83ywUQ7bXwRhVyOTuxE5zQ4fcSe-ffHRDwsrpKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27019" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27018">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRML64vNqrdwk_xGQgEF6CQhv9oWzTsMjmk9xwYNmti65FtA4wpiK3PQjcnTX-WH3dkizz_ZVZkzXKMRhDBcvv-GVCIPxYKo1_Vq5SLpN9X8T6frO2JFjbjjxfqL96PLVTv6_sEeoBgj09PHL4vF_jDfRp7Z5LHLufYr3yFMNd-pjh5dSqvxHToEPkxlTBAR0svmLX-FPD6LCA97Sq2ydLXGS7lzT_d314wNN9wsUiBG1oNhhPM8uaNhf61APvTgbwkNSAZWph5Ldj4aqITmYwCkvWtp0lBn2IVqpL4GkwdGf7fB6yCzICvqMVtA8t1-NdhVaJjqqJMhbFAlUQT1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه گل گهرسیرجان‌رقم‌رضایت‌نامه امیرجعفری مدافع چپ 24ساله‌این‌باشگاه رو 70 میلیارد تومان اعلام کرده است. مهدی تارتار بشدت دنبال جذب این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27018" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu2Hw68RqogfcpuztEdpHZ7B6kMoq1Bl8Jz660q_QQNTPbUR-wCcUWDi_BctUH0Um9FtwhjUKoC3mVe5HiVoJfWk27WxhtJWRIUOWVEPfv0K2u2tqik6N8HbrKD8puVUDgjcw-ASwwF5oi1xEZHCQg3M9zePYh_VsDBt9HvXE95kCbldtTjUIS8fpxbqiCHu1QIAtKH1OPyTKO6gR3vaCQ3clKgwWBz3GG-sI1t8GPRbaxadONuEGA90aei2W11VwI-4nXRKqSXde_0WQkVAsDUbSuVVsBM6fQB2eW9BLF3KGt2sC_fxTWpBYq_MTdbIwgrzH2Pmwv5FDblANRQ_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق صحبتی که با یکی از نزدیکان محمد جواد حسین‌نژاد داشتیم این‌بازیکن‌هم‌آمادگی خود را برای بازگشت به لیگ برتر اعلام کرده و به احتمال فراوان راهی یکی از دوتیم پرسپولیس یا استقلال میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27016" target="_blank">📅 20:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27015">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtnqiEvNMF0c5X7eslOduDPgGqj_R_1pX0MaO8qV_elNJ6jV069I5GWHcr2f-z_aQ2CkJXyoqBCK7YNnmEf7WV0QlU3KBUD7D5GjKq8LN7Hub-Q_Q2LfF5eqr7FQOqr6GhnxVpSSPDiD_n8S6-ipRaC41OxEy-FxrhN4iaIj3fXiHeWhVW7mm99G34oXkn0JubKxGakJFwfOrW3mf2Z4pP66fsFXl2S3_FIIzDKmzwRMonA_zaaYnS-ypWnyKG7YPic0VstxGNfuaBAqFBNmtqofOh37Qh5ebAn5Tn41xw20Kdrd1Z4Q7JxeYTK5b1sf6PXDjb0H4ovIcaXewlHi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو درحال‌آماده‌سازی مراسم ازدواج با جورجینا رودریگز برای هفته آینده در مادیرا است. این‌دونفر در کلیسای جامع فونچال رسما ازدواج خواهند کرد و سپس جشن‌ها برای مراسم پذیرایی بسیار خفن به هتل پنج‌ ستاره و لوکس ساوی پالاس منتقل می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27015" target="_blank">📅 20:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-lrXivIsqZPFGKxIlb6qUQrn5kwcO1cNSfUk1ZkJbom7CuHlnQgHV0NTrQjT7x4aT6T_3liigQRPo0dyQaCt3xYkzItqTMxBhICChGEdR0aF1mGkLzBSQXpNdyIpsXsXREi32wpqjQrdtV9Ed73yOIy3XYIpLLkth7BfDI7S8EpX-CNt384ErxKC8ENOcgT722PuwW24tRUhaffXth8beFD7Sz6dFob1cYyNqgnaUU-iSJ5onNIfLjuS802nX4lOaDly0EyfL5vWalUk2Wat5fWOX1sNb-bau__YgcocPpQ0FNnNWGdKslGTuWMUfoh_2_IxDjyuMZ1pJnOpkiJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27014" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27012">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=K4UMRLRL-C1BR9Y3Umzf7BNyUITxkGzC9fiAV0uS16Dkkk7uMDJjBzu6xKOGfNcWynDfY7oa99RLRt5NPlATPk2v_7d2C4ZX9UlKCiF5a9KloNEd7ybLj_v6uluSbeD0EHeFOJY7BqueqZi0ew6jpRlB2nr8QryBbEugSTNRTVG3nH8QaInn9e8W0Y5AtfHnHoMn22RETrTJj0f7SPUuHrmLN03ZxCw9z3KD5bGjA737fEuUXh1CK0NAejj4nSEIqGefNi6dRkdS27J4-ZjEaCS6MT67V8pH9Xmtk5XNUsIL1yKTdmUzcPyYUJsyacMxJjHxRtCqore__woNX34snQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=K4UMRLRL-C1BR9Y3Umzf7BNyUITxkGzC9fiAV0uS16Dkkk7uMDJjBzu6xKOGfNcWynDfY7oa99RLRt5NPlATPk2v_7d2C4ZX9UlKCiF5a9KloNEd7ybLj_v6uluSbeD0EHeFOJY7BqueqZi0ew6jpRlB2nr8QryBbEugSTNRTVG3nH8QaInn9e8W0Y5AtfHnHoMn22RETrTJj0f7SPUuHrmLN03ZxCw9z3KD5bGjA737fEuUXh1CK0NAejj4nSEIqGefNi6dRkdS27J4-ZjEaCS6MT67V8pH9Xmtk5XNUsIL1yKTdmUzcPyYUJsyacMxJjHxRtCqore__woNX34snQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27012" target="_blank">📅 19:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27011">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJXBfn1CLg5xBsWn6hlEcc8sdTEV0sZmiX-XhQlWsyPim49hZ3RoQ5VdfAGwlMin-65Ci76fDc2RQLn_2FfbHFYOaykJ-FobIlmnmgFYVM9QhhhXijF7MN0Vx0hT321fps4HU1305HyB7Jw-mY5red8gyexF0hnYsL_bpmZjRRdAkKNIU2fXrZpGpTQ89v8XclKiJmLy2uVg8YE23K10Mmo-i_I6Q7KDNT-F1qf2vYoabXwtLe68KGoQczUnRf6Fglx74AJ8TonsWnUsczQRJCpvZM-AtMBJbU7v6uNqOo7PgKqUZ9tcY-tJ18WfwXh0fIhy6SyDJVvg_V6sKFJKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27011" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27010">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeCMp1KmcGY8NcfIV_fK4F5u_r8401-Kk6xZpf_0_zj1FTl7knjKkf_ippvkS2HPHLHoV1_RVBY6o1cEYIS_Tcbf3Bg5Gy5Y42FMhVJYTeJztHzpMeLwDq-MvQe1FhZI_M873VaTlrP-xNdF42EghcpRktMM1apc7U8yKBiuzRcnSFxrHuXfW7lHT_Wdw1E3q1MDZ05JVh8FvuRXpf_pYRrpGyDxptgS1qUHazMxeEGEM634WXdvpZbjqstFd2U7kxrXYSFhlx44EVJyMLEchu758OC2UYScztp9thP_-wrIqACjSO2go-CkSgG94bvOaEYICKUjCB-QRnuibi0QiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مریم ایراندوست سرمربی‌ سابق‌تیم‌بانوان ملوان عصر امروز با قرار دادی دو ساله سرمربی تیم بانوان استقلال‌شد حالا زهرا قنبری کاپیتان تیم پرسپولیس به مریم ایران دوست بابت سرمربی شدن تیم بانوان استقلال تبریک گفته و گفته خوش برگشتید انشالله فصل خوبی در باشگاه استقلال…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27010" target="_blank">📅 18:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27009">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP1BeqBaOZi4K38FRHenY_tVHHseW6PKJS73Yd4mUB3O_gIBnAH3pCJHG5C6Y6dnuEbfTRuRTZPPmi3D8z5i2lWs2cAhkRh_aSKM-QcmU_2MbYYMFYecErjTrtUbwWWJoypvCz4xPVoVeEySyHRGYbuTYLzjCIj9Fk_Nmg49_Jqu-vd5uImnQi7FogNiI8XovghDmv7DpJahOCm01iCE52bVLgHxkOIRuiEzC7n5ovcnxiYs0J_51JKQuUo2aIFGMkTKiUc8hPGivYAKz-COr4JHHbwm18Y7QWroddg-LXldmLZ2qBvxVZEnpFnsOe7Js97Q2WtRUUETao_NPgMoIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27009" target="_blank">📅 18:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27008">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
در فینال مسابقات لیگ ملت‌های والیبال لهستان تویه‌بازی‌سخت و نفسگیر موفق شد آمریکا رو 3_2 شکست بده و مجددا قهرمان این رقابت‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27008" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27007">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7il336NRPpXbyHYYBpkWOJz2FB0RUzPyF50hQo-fyNlgHYX9qUZftBarh6tHhYQBq2vERuWP-Ne2abCYWcqyxgtvGXd3TuspKHT_NgmhDF9NENelFXTeX9uILUmUW1W3VRg2H30ubvqsqhivbCLeQ2qpjKDfKwrprAcx03PwkTrnbfjNH_uZSmt9NG2vkZkBH14Bs6E5gloLGQDLFUIEwuzbkzYFo3XbGeZzwf-xdPlc1rlEaGkqlbXnER-10x1hE3MnZz5sjekcuXh4oPAlptVmAMePyvWyQDKdJx39UiRkzPPZyRs6wo0TDHc8Zlu5YhsIuCwztLyy5QzPcz-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رده‌بندی‌لیگ‌ملتهای والیبال؛ اسلوونی با شکست ژاپن به مقام‌سوم رسید. تیم ملی والیبال اسلوونی با پیروزی برابرژاپن دردیدار رده‌بندی‌لیگ ملت‌ها 2026 به مقام‌سومی و مدال برنز این مسابقات دست یافت تابرای نخستین بار روی سکوی این رقابت‌ها برود.
🏐
ژاپن
1️⃣
-
3️⃣
اسلوونی…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27007" target="_blank">📅 17:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27006">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=aTMEICLJtDH9DFbAvBCrRwQY6yFuoUkar3RM6LsZM3fYtF_bEwVaxG8eUuhAA92lfY8s5_0jD3xTVLtCd3yOASl1oho6sN08LDWUrDdVzyI4SuRFDQ-k5ISKB9VOwYAMYsFRGrCtz5Pd0OIFMW6Qh6qKeiXzTdK21Z9uqoPKLHDrIaWP-VLa9iEOffkqKEiSgznKpaaQQCZ0mJv3gtH050rUFTvZJPtxEdwIrR7ckEbJudA-HB7cFUlZuIbS6uIp2A6tFfzDVBHmeCv2xjWG6SrX1PbXnh_lYhXRQPN8v1dyi_3Y-Iwsm3Fv63hQBOKnThrtlzHHyrj7VuC7c88lpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=aTMEICLJtDH9DFbAvBCrRwQY6yFuoUkar3RM6LsZM3fYtF_bEwVaxG8eUuhAA92lfY8s5_0jD3xTVLtCd3yOASl1oho6sN08LDWUrDdVzyI4SuRFDQ-k5ISKB9VOwYAMYsFRGrCtz5Pd0OIFMW6Qh6qKeiXzTdK21Z9uqoPKLHDrIaWP-VLa9iEOffkqKEiSgznKpaaQQCZ0mJv3gtH050rUFTvZJPtxEdwIrR7ckEbJudA-HB7cFUlZuIbS6uIp2A6tFfzDVBHmeCv2xjWG6SrX1PbXnh_lYhXRQPN8v1dyi_3Y-Iwsm3Fv63hQBOKnThrtlzHHyrj7VuC7c88lpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27006" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27005">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWMqrd7NjMuoNTynUp7lxBNWN7HwdAU2OPamPfZJyjBOreBKXOoVqcu_YmvvbwF5VHvkFbnn6CXtCrXuxApc-QPb6SHLh-vWZAMPxo79bhPJ1aY3C4JKIcUee5297DPvofAUxaj5N5vfQWtVyap6MGoA0OJwEtLWsrkXYiKMDY5qNlQFpEDOYbZdIp3n-cJmrNTM0o09fz9QZDxhbDOUy9mRGlFWru_FXjCJoJ3VTYw6UZdp1aCIAOHp0XGnHVaTtzJmvOcWbSg9qvSihH6kbqHlmUlIL6kgHaBYikIAeEDbCJzA6tY3FtSynSgojgLUJacfbxPBH7q55ZSsMkZEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27005" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27004">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suQ3-q0Qx8xJ0qBMWZUzTPjQkXBe_XT1pPtS2buayryq9YbJnWcCDj3oPq6jiObc4F_hS-e_5j38te8aO-Rg9GrJWQ-obDjY6VWXoq8pi0OpRpSELcp9jPSwm-LaNGy5xUUu7cP1seL-iXv2LraQAzqlo7U25MZBE6bcsMVBtPEVx2DMMFImw2DYdkELL8TxtLaTwU2vfUPUr6gyRajHHRvuepXKtWsjx-PA3X4vBf3lIQA8vKyC09zh_sU5aq7uejH7l5tB-3gXM8Sfx0iLTSWyjUylTszp6e7LZhE_7XV_7Wk04oPzEqr0D9rnPmx4IhpwcFC7u9jXGl9t2qD1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27004" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27003">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb60syzutHYf_LIFRRNfrYosUkQMjUOdGygNQzooXjJjSwtk_z-HLetduX9SwcYHQS7_yFmhrtGY63oSZf_twGgvrmkzC-CLmpD4Op4NgOrL-ecDummP4zT98HWtMV7cvO6qPg7wBy8lclZMKGGLPD1SEtHEuH8NpFyGAzL7jYviPE-2t97U4Qd538ej9J_ymFJep-FM-1yIPwAoFSs-FiuZ7260u7q3ST6xUROwEUwpUCJc7-Ro-eBIyAeX0k_RVX7G3ZYR9eSgLo92XUCPmaie_-wyEOPKAX4Kpt-YtRwoGTXCziNtRRD_99aLJ6ioPN4a8-V99EdOCZl-TdwBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27003" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27002">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlmPw9jeHSLC-WcaYBm19hmevwkjdXY8qkGX_Y3i9o-HL6vPXBBHHVxGi7sLHXuzUK9vzK8qQbbXGdHiXbZoK4Y9aZYy3gfk-RdycjzUgMjzRpnqZUGuO-UZa9IiBQ0MBPnT6fwgoDqrq2X64KpQmMMhUZ8rBzjagxHuunBMcUMMLDJ8YJd8tTDBZApJcukDOsWCZ1GyM3DzW1t_NlixHZgPgZY0rz6oUpADsxOiXs-jHbMIGHtDldO4UTvsygWLTzdG9_59pOTM8Kxn-Cm7Hdghr0f0blAaw6m4KTcasp1Mde2OeIDQJQ6QCefdzUpFXuutr0lM0lIaOaINoyxmgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💰
گران‌قیمت‌ترین بازیکنان در فوتبال زنان
🥇
آلیسیا روسو - آرسنال ۱,۸۰۰,۰۰۰ یورو
🥈
خدیجه شاو - سیتی ۱,۳۰۰,۰۰۰ یورو
🥉
الکسیا پوتیاس - لندن سیتی ۱,۱۵۰,۰۰۰ یورو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27002" target="_blank">📅 15:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27001">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTDNcPC55xa3RzZtmDxAyxZgOf9hX_Srpv_JVKpiLg-WGp-FJSN7IFVDTr8ZWt-16mVrOFjlIZvEZpMhTmGtOCw6OP85sGbx9w2HTiZ0C3JHXf2ajapcdTMgHjUzATglpGUNpFFrgi8z3XAykGKralLsDpIEz91CRW95ADdQZW5evVI8zhUE65uDKOQeKMftiNo-pvl9ZupXgjnMNv0AjmhF2t1Nj-ubx0ugeT2o5Vwg2yNK7avePlzO3C9UxbkA8bXy8JA7XQ7RzexnzLCYCwzhEIKvkqsh2nnx5stNbwQD9kQzzfrJtUN62MQJ1lHQXGPI-mm5wskp9m10k7jt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27001" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27000">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp9nLHpIPhYJxCh5Bj9mvGk6ELrofafm1cq-vbbGTE01k3i5B1fGidTN2pc9vxqqEQmvhS28r-lDodMgso8xHGP3cFgQPM5PrJgvNKTZeJuim4QsKen14u0gZn3GV4CehRNSlXyrP40mqRxvZAul9i0WMmpq_XutU8kPjs84_4WcWKgQe9kSWlXbM7DMrI9wCZAOEIdCeJEZelxr9tt_9ItbiGm29ptSbZda12iFLG0R1qB4_UduA8OTHsEga-xVp8N4J7TIVoyCfVgi5W24uO0X4JNy7dz-huDTKaRKBuUaYeC-gCJbV8NRawgO3Yn5ZqMubLy7TgaJzxCd1h2TzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27000" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26998">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPywgJl4AXlkBKlO9vCsKscbGDP1Xj-SQlZuyhnjSmtx8r1pdfkdUyn6tTWrLhn839BR495fT9b_-PqLrO1yN9WDnFpqp0ZrSd3tbWSViE6dvqus327bj_nBsMlmya2kUOdZQQ7R3U_IkyYyJT0zUprmrtxMzFvhPZF8AfoJoxcZ1_Ccj4COujImkbGwzqF_4Lm_5WtetSQhneexraSaArlquEpifp56BTTfIoUHpKyLUnKQ1ucqxY2B8zJNLnEYupTW5hX33qfjddcBUeKh47zHAhAAD6zW6HS64CJKA7vsy08_H-FpBzQLaCmNASpbjWywnCl6j6Xg2_IRBopppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpFQoWdAangLHxzh40kElN7bKjHAZLJZqPFUCYVGp3FXiLtJx4XMNRK39nCGJgOiYG7sy8t_c92Cdt3SWP3p2r0_p8dMNFbhwEJf0gwcyAlbooozXMbiAnFvL06ZP2tHe6P_vb4kfjBbwopRvlb5egZ1FIKVf4Dy4vc2RPZ6gYpAMElszlziwhxSi4e954hLjkRrKxpKdc7ri9DjkGH0uZMw4xb3qwLWwRzJCYtAuZMV-P_nbxjRHFJ3Uq5k5Jh0k24mAVMbOg392mf6ObrrESpgHNQfhvu0Zz428WO9mrmV-320SjK1Akg8Bn56UuJlmLaid6L9AF83vOk04jlu-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
کریس رونالدو و جورجینا میخوان‌؛ مراسم عروسی خود را بعد از مسابقات جام جهانی در جزایر مادیرا در شمال اقیانوس اطلس بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26998" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26997">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boQKVdJ2jddg9wjR7dxmgzxAU9ZCkxZSp2KkJxawPPP4DiWyjfBZmmZHUQm-AuA_nevaB4dNO3Pr_IHAo9zJRTQpg1V7sVz6HjQ8zuNw0nqOZ2wak1LVCkjOl2-ZpEjohq2C6JfzIXl5wdTEUN_q9NLQSE5Adl2FaSPx1pKTH9wOwqllxOPkioBSb75vmq1EM4CTBZUOni6iQKu6FjH7wGuaAfjGUmUrwmVkdUJnKatbzDVKSt69Zt29aAF_zvIwA2OqoDvsg4UUjJyOYEAf_JRTxC4saspmkButMqANlUz9ZTuTX50S3IkqovJ3VhShkfjNwVK-D10Cfe6NhXSDVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اینم از توضیحات کوکوریا: خیلیا بخاطر مدل موهام منو مسخره میکنن اما دلیل بلند بودن موهام پسرمه که اوتیسم داره، این تنها راهیه که میتونه باباشو از بین بازیکنای دیگه تشخیص بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26997" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26996">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP8RKHHMHs4iwx5G59ANnqYE6lbIwos2f5mLf9C12i_-Ni4dZBMr7UPIlpPkNlBFKUaCwUiPVwc1a_j-An67RqjZt5un8u-NMgVMEYKxsPcflCwLB8fc2ELOIAD1QlxfYOB84m7Z2FhCU0qNRqhNU3lclfJ-0wWbtEPEow0midPIwGvRVfbUQZ-y15uWltRkrjebE0Dnww99OqNiij_G4pz9Y6Kgpu5Gcv6-R0vMYMHZNtojH2yLpPNrLd2BIiOv3XsoeyvyoQP9meV00QOCFFjC13Egf6eqVu5pWZHxkYVlntBLFGpWRgpHGc4oXAxDwpgqPh3mfkB1duaVzmLq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس‌نیشیموتو بازیکن تیم‌ملی‌والیبال ژاپن که باعث خنده خود او شد؛ یه لحظه تعادلش رو از دست داد. بازی فینال هم ساعت 15:00 شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26996" target="_blank">📅 13:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26995">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=VCwxrZtqkn_aCeGzsFDVMOiQkMpWWItU7KUGLuOfxK6UV68CA_fii18rqfDeBTgwFC-_OO2zHyKF7sTopwLuF-ZCkDa4qVhTbpVEfy2iruzo3zYgjZqjcCuctveyNc1KTBsV40IosFSomrqU8bxCHbfB9_fEuKuencp9fcpetvaEidSSUhMrq3Ggui_gMAANKSuHZOy4Ssqaw50nk6-kZGT7S-aYNysoGfXci5pEB01wHG_pO-3aome_DrMjkGmcmzaFfVNfj2UyXKLCYsw2647uB59_0U5CZrTgG-0nDJMYq3hyyFOsOiMWiZVVUcO_RFyq-Y7ehQuwnUm2oCaVkRf8NeJWUMxQlYJTNqr9idb0nrIA6vqePMksljdPP_dGjkLXLDcz4QWmrUarVQ2wYS9keNo0QeTG260sizeHTDYhxBJat9UG8qx0sExHrwWkDfNH0Mx77AyWJAGTggs7e6EUcX3pN5OX9KGdCa6LCw6mfVjseICqgQrI0j8EnIs6uDH9hPxLpiI-hGHR2XNcmjyVuYdgQQ5_yGF205U1HpGRhuS_4tlvBabWnq_WWzdibp-eTny-XKI5Sm7mRIVtxGmDkRvVmSGrA-hDnbR_EgWi3GODg_12zEwNOpzWXCU8aYJ8lZb3goXwRH7szxZdSFAmX9Ol3-T-da5sXm_lmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=VCwxrZtqkn_aCeGzsFDVMOiQkMpWWItU7KUGLuOfxK6UV68CA_fii18rqfDeBTgwFC-_OO2zHyKF7sTopwLuF-ZCkDa4qVhTbpVEfy2iruzo3zYgjZqjcCuctveyNc1KTBsV40IosFSomrqU8bxCHbfB9_fEuKuencp9fcpetvaEidSSUhMrq3Ggui_gMAANKSuHZOy4Ssqaw50nk6-kZGT7S-aYNysoGfXci5pEB01wHG_pO-3aome_DrMjkGmcmzaFfVNfj2UyXKLCYsw2647uB59_0U5CZrTgG-0nDJMYq3hyyFOsOiMWiZVVUcO_RFyq-Y7ehQuwnUm2oCaVkRf8NeJWUMxQlYJTNqr9idb0nrIA6vqePMksljdPP_dGjkLXLDcz4QWmrUarVQ2wYS9keNo0QeTG260sizeHTDYhxBJat9UG8qx0sExHrwWkDfNH0Mx77AyWJAGTggs7e6EUcX3pN5OX9KGdCa6LCw6mfVjseICqgQrI0j8EnIs6uDH9hPxLpiI-hGHR2XNcmjyVuYdgQQ5_yGF205U1HpGRhuS_4tlvBabWnq_WWzdibp-eTny-XKI5Sm7mRIVtxGmDkRvVmSGrA-hDnbR_EgWi3GODg_12zEwNOpzWXCU8aYJ8lZb3goXwRH7szxZdSFAmX9Ol3-T-da5sXm_lmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
۱۲ سال پیش در چنین روزی
؛ منچستر یونایتد و رئال‌مادرید درمیشیگان به مصاف‌هم رفتند که ۱۰۹,۳۱۸ تماشاگرشاهد این بازی بودند. این‌بازی هم چنان رکورددار بیشترین تماشاگر در طول تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26995" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26994">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=LHLUmSfgEn8cUotvvgCz9rak9wfkbRpE5sN414C-4IpawVN9RXoM34KzfRZ1KfmLm3QKTMe57Yd_IbqFffMbsFFijJIu0YsrHwuwnJFOzNnIbv9Hs5d7p4mmxRM8tm1cDp26L6k3qoRsivAixfFUMt3cqk_z0Yb8FFDY-yc2Dq_Y5_8oB7UvlyyADKxjAHWt7s91cbU02OVCLdecZvTe-LGtr2CDlqPu6zdxkgDI1u-tgMtzuMtaYUgtwMORrnryxK_klOqLqrDZj7VMBPnOhYAxBCm0VL5wS14e6RuVHT5me-m51Rw5MUJaQdfuuFb0E1Jj_aGxVSJWRJtm_m7ooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=LHLUmSfgEn8cUotvvgCz9rak9wfkbRpE5sN414C-4IpawVN9RXoM34KzfRZ1KfmLm3QKTMe57Yd_IbqFffMbsFFijJIu0YsrHwuwnJFOzNnIbv9Hs5d7p4mmxRM8tm1cDp26L6k3qoRsivAixfFUMt3cqk_z0Yb8FFDY-yc2Dq_Y5_8oB7UvlyyADKxjAHWt7s91cbU02OVCLdecZvTe-LGtr2CDlqPu6zdxkgDI1u-tgMtzuMtaYUgtwMORrnryxK_klOqLqrDZj7VMBPnOhYAxBCm0VL5wS14e6RuVHT5me-m51Rw5MUJaQdfuuFb0E1Jj_aGxVSJWRJtm_m7ooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
رسانه‌های‌ مراکشی: منیر الحدادی تاکنون دو آفر باشگاه‌های مراکشی، دو آفر باشگاه‌ های برزیلی و یک آفر باشگاه‌ های قطری رو به‌ دلیل پایین بودن رقم قرار دادش رد کرده است. بالاترین دستمزد رو باشگاه استقلال ایران به او میداد که فعلا راضی به بازگشت به ایران به…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26994" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26993">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu_qEZ773Ii6g9ZLze6ylQxyIEpgTvfVCnPSjS-8jRNoOXap7BrwAk4WXzGuDaPvJQBskqeq11WnZ5zXoopvDn3DO2tPumIEBAbu1Mlidt_CvqNKhxDlaB1HzsOsGi1vOMum00gFKCpp_u0hL35eiF4jqBqZBfE9T15pmge2fdFIEKtydC005eiZZG1KynZtoWX6q1MgMv3dLGSK0hwPBvt_vnSyIx7_uxLY0BZ_8s81RU-jeyUCmJTr7W4NB8lOIyeGQxpFnM3PTBkj32bZ0FHP-bZqeBHNY7hLFti6AZQiJh7hwZxTNnU5VGbzhZENpGd4orDimt9_bSrEpHcN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دوران اسپانسرهای شرط‌بندی روی سینه پیراهن‌ های لیگ برتر انگلیس به پایان رسید. از فصل جدید، تیم‌های لیگ‌برتردیگر اجازه ندارند لوگوی شرکت‌های شرط‌ بندی را روی جلوی پیراهن مسابقه درج کنند. این‌قانون‌فقط شامل اسپانسرهای روی سینه است و سایر همکاری‌های تجاری همچنان مجاز خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26993" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26992">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewzBqOuv22KOXE0NfG_HErcocgWkFSgMjUIWJdfPTJXJaDFG7dA40DAqKWX5Af709fSbFKy637f8G4itPKSVeaSd7m2uTFKv462z5dlZO-s8uAXfqczO6VfM0yz0opMoUwJNeeYFCoxRmYL2lCFvuDrVDHZRK9q0ig5mZUcH8MMPg0TPjxFy5Q1NBsjDUJaOHJD9WmT5NeauZ5nrKMJndDgSk4dhwTQa85jv0y4ADa35l4HpRr-a_Bu8QQQeujPQDc4RMrKDlpSJlEAClJztffSdgybUwZeDG0gVstrB5WRJGSVbVeVZAGjIMlr3fRDw5I2hrhjDc_A697gWfU1j0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
#تکمیلی؛بااعلام‌رسانه‌های اسپانیایی؛ فران تورس بزودی قراردادش رو با بارسا فسخ خواهد کرد و با عقد قراردادی چهار ساله راهی PSG میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26992" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26991">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKuZwRjc89gCgwm_HK47ecVqg498Z-9UeUWrCckfhJ0QV8gnCnSnGG8MhN4911ievxw9z--ziu-GRvzlJtZoITQBju4KMUhcfRxcZ3NJT7qDH4kN7E5zst6Aw51JOwdMiu05oDOPir7ASIVByWiV7-jGamwO_TgUz_PH8F2Hj4usQcbcpxrwhJQ7KdcNBX7AtiFXBdincZ3TD03Zh_f_0VxwnUc-UEm3My0cv0ZoLsnYrYtuOIwV_wrnaD3pbjE38Q2GgayO83yp0M4Avg3hmHCblAyoS-T5BEIyObgVeemG35v4BXs5Jz_ECnSxdhl7jUS0DmsqSzbgRvnzkivxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26991" target="_blank">📅 12:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26990">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiZdn5BE1kdMOQBPq6pIkfNo4mecgBpxO_qXogupwIgR8Uxi2uKWrBs5FV6btBsbT-ZsNFWRXxPlkYeoaqY1_CqfLYbpRqyNd9Qf8KS3eIswBlNlDfE3uS_nVN2uNshWyHXYXHQCdS-zkX53W7actKyitPwPdaLScj7XblgPiyKxktmaAgHaLIEwhWv2pkNRXNYdo67SvcOUdvApGRAriagqfbjZ645N_WACQclNmoYUlnVA0f55GIcTWNKYj_fxTlmeiuSiNDrbD672bIvPxhcKCaXyOOqayt1CBJflzslzsOlSY9A9qcmmh9wslVxEoORCJxWjBmju8Hdob56l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیج بارسا اومده صحنه سجده حمزه عبدالکریم بعد گلش‌رو استوری کرده و دقیقا تو همون استوری تبلیغات یه‌برند مشروبات الکلی رو هم انجام داده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26990" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26989">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58235729a.mp4?token=pKkrSe4Dj5_cAHM6tGHkLn1UrfbdoBrydTIdSN8XqC7HBOFmpRTHXE05jVC0XxrObelYiY2chY_-9L3RK1d78L5IPiMxNJT9xsHtlhYEjLqVygqbTnAm4DMTTezlSpfvBGUkCsbJuMdoxw0um6pJttjtF-FaOgZpt862k8IBhWSmuFt6rnwmlv-iIxorfVXclirV8X49g3CSj5dJgQ4ul9C_Q8qLOmKlKVfTqmEJ_c73h6Wfo6BiNlsy6zgcfB14LiTLm_hZXRud5zwksnC9gMfKfVXvDxMUI55LiO4X4Y5hRv07qls3EqRoYRVMdGnCrszfo6d7Wtq8zopRrpoFmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58235729a.mp4?token=pKkrSe4Dj5_cAHM6tGHkLn1UrfbdoBrydTIdSN8XqC7HBOFmpRTHXE05jVC0XxrObelYiY2chY_-9L3RK1d78L5IPiMxNJT9xsHtlhYEjLqVygqbTnAm4DMTTezlSpfvBGUkCsbJuMdoxw0um6pJttjtF-FaOgZpt862k8IBhWSmuFt6rnwmlv-iIxorfVXclirV8X49g3CSj5dJgQ4ul9C_Q8qLOmKlKVfTqmEJ_c73h6Wfo6BiNlsy6zgcfB14LiTLm_hZXRud5zwksnC9gMfKfVXvDxMUI55LiO4X4Y5hRv07qls3EqRoYRVMdGnCrszfo6d7Wtq8zopRrpoFmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26989" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26987">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436452afaf.mp4?token=v3feSwymCx0AwgMadwP_LnNSEnP-10W8LdtZ4MypvQo23HE9N-Nx0A_hhJ9ayEJDaPU6d_PWfKGwjBpbjC0sKVW4pMu3BDKjXbC6-z96m7DdwpVJLeIvuylyIcyDCpIjMhqEbMQxYERgKVP_q_3VyZZY7nZY-MkDi9ifV6k7Gy6z6awI4k4eTOntCXrDvISJt5PfwKuC_qfZCSpm-9W7i_x1u9XKEIJoAy4RI54xdMWQV2afvzRrhi9jZsKzw5aFQ3jCJAPBa3BSi6vltPjCjlb7IS0OtqEOndEDvZK7NkIzdmBmcwvtv6DZDth_jDFMM6KFA5JQPtdmo_87C-yi3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436452afaf.mp4?token=v3feSwymCx0AwgMadwP_LnNSEnP-10W8LdtZ4MypvQo23HE9N-Nx0A_hhJ9ayEJDaPU6d_PWfKGwjBpbjC0sKVW4pMu3BDKjXbC6-z96m7DdwpVJLeIvuylyIcyDCpIjMhqEbMQxYERgKVP_q_3VyZZY7nZY-MkDi9ifV6k7Gy6z6awI4k4eTOntCXrDvISJt5PfwKuC_qfZCSpm-9W7i_x1u9XKEIJoAy4RI54xdMWQV2afvzRrhi9jZsKzw5aFQ3jCJAPBa3BSi6vltPjCjlb7IS0OtqEOndEDvZK7NkIzdmBmcwvtv6DZDth_jDFMM6KFA5JQPtdmo_87C-yi3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه بازی فینال و رده بندی لیگ ملتای والیبال؛ فردا ساعت 15:00 مسابقه فینال برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26987" target="_blank">📅 11:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26986">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJoYP-qlPwOLqYOSYRaTu3ZTlOrKXM4l-RMc_14CVu6af3sdsBsJqxwvipgcitYTk_9F4zd2ljLXTTGtw6hhNl3TNI_Ygk_nkRbsn4nbLA6Xxev-ywG3AOUb1FO16NETFADvwRO-Ec8SAB2EAPM_oQXV0YVQIQxDIOdYQ7ifPyCvxuAP2XPgmH8XGCfnSXwNWg525GURXPvRIeKW8DAKyh0UGAm-gkBF_yeoqSamgzl-dBEn5axsdIPz2oBPZmheZ_I0apeT99vybnB2beHTdWX_u-ms_D2WzCHTxcFtOicMev-orlslbw62MxX0St-hqFz0gcH7yHXYKlemBEl9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوری از دیوید اورنشتاین: وینیسیوس در حال تصمیم‌گیری برای خروج‌رایگان در ۲۰۲۷ یا پیوستن به آرسنال درهمین‌تابستان است. آرسنال تمام منابع مالی رافراهم کرده و بازیکن به این ایده علاقه نشان داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26986" target="_blank">📅 11:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26985">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9GGI1WEZuhZWTj3_7xHD9Xyvefs_K-igMRoIV-pKiUQuVg5GnbS3zygEuZsdJfRhHjLK-V-BvCDCY0cVUJWvTlN0FN2tjLLiV-oZYAa7OQ7iK4j5GZt9dT6qtE8zsR8XMT6rvrTUGfk_TsduaSbRzDWQKp1O5swiZJPO_11ResOYbEOETwY50ULJ_WvbEWSvuFBEmV_IXZuJRGB45muihJqAW2TeBAC4d8ER1p9sWTxQ6m9cy719ZmDYDAiZ2Xe7mIeDsoOQ1cLxwqTNCAlsDLEclpJZJErXunbw_Om6ltkVhIT6WSuz6FeCQfj2q4kNirYh0_Ms5APyfEPSZeUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26985" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26984">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12920f454e.mp4?token=gEhhpyj0EHgm23ooYrhBTjMzVV0PUvy-zCcLFovr8dUHN8LMqfHLevOfCZP-FdOX1Rtx9hSEfw9fvfv-ghR6vro_6ID5ipNDnOQ6NQcQOK6l7Dg2bWuNyToVVfBTjLDlXPl8rWNVioTFafKUDBEqCiasUTBUyagSSkwgfT6ItqX2NmZkkPKKCcw59_SRFuEtM271agNhURGSFfE7g2zkuNsTMwBFbmm79YTwfS4AWTqQnL7um4n7FFhtoGEuniINe-r9M49GyNqJQ4G6sd2wpFk69nVzCMfNgh-bb3BIKyk2ksU-yrbLC8tW2rGD7ObFRay2TjheIdoVcjxHaO-sSFwR_ZQd_x6qCgOBIf3LETkAs1s3hVaA_WgcIsihh3DuzRmmLwUti3DrSWnPecAUYjWnWQw51h1T2ZesE4woth7gyf09VpAVQdqjiJvHlgwYCOx20KstgvJEY5uUVufL3-ec3_QjZpaYCh6QKVKVo-DKMZTaamfIfeDOuiPowRCw_INRkQWBieVZg5lj6Bu5tfRjnpsI_vdJS2cBxmepOEYIiBmK6Y8sFw7fVJazvKgcPgkjDfO9yXvOQ6AwP5jIZgubSa02Aic1nNSE3ilozFG9izAT3BSyzLDzpqt-1CcALm8wNCrPMHZLEYSPO-ahShbiztFheN_d1liSZlwbZV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12920f454e.mp4?token=gEhhpyj0EHgm23ooYrhBTjMzVV0PUvy-zCcLFovr8dUHN8LMqfHLevOfCZP-FdOX1Rtx9hSEfw9fvfv-ghR6vro_6ID5ipNDnOQ6NQcQOK6l7Dg2bWuNyToVVfBTjLDlXPl8rWNVioTFafKUDBEqCiasUTBUyagSSkwgfT6ItqX2NmZkkPKKCcw59_SRFuEtM271agNhURGSFfE7g2zkuNsTMwBFbmm79YTwfS4AWTqQnL7um4n7FFhtoGEuniINe-r9M49GyNqJQ4G6sd2wpFk69nVzCMfNgh-bb3BIKyk2ksU-yrbLC8tW2rGD7ObFRay2TjheIdoVcjxHaO-sSFwR_ZQd_x6qCgOBIf3LETkAs1s3hVaA_WgcIsihh3DuzRmmLwUti3DrSWnPecAUYjWnWQw51h1T2ZesE4woth7gyf09VpAVQdqjiJvHlgwYCOx20KstgvJEY5uUVufL3-ec3_QjZpaYCh6QKVKVo-DKMZTaamfIfeDOuiPowRCw_INRkQWBieVZg5lj6Bu5tfRjnpsI_vdJS2cBxmepOEYIiBmK6Y8sFw7fVJazvKgcPgkjDfO9yXvOQ6AwP5jIZgubSa02Aic1nNSE3ilozFG9izAT3BSyzLDzpqt-1CcALm8wNCrPMHZLEYSPO-ahShbiztFheN_d1liSZlwbZV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26984" target="_blank">📅 11:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26983">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=ltNp3L1ggrATblw2K-p_jLGtl74VBo0L_SQ-tVMVOfM5t8dL1EGvFR9ti7YxtrItClypw0N3MhY67-6QJt52_FmZmiJ6RpL6IttQIK3MjkZac2MV0QKni0AYBXFsItnVaVuim8O-WQRepRU7VuYCQcC471PAjmWGDYCDFAxfO9tLW5gzHOmSRKgn1KCT1bbkI9WxBtOd3lXz7rxRUricnxQTFlYmg7mVkXRaex5FPWJW1Y0c6DPHNfJNg68uKqWQstpv96C-ezlUeTrrMArRXE91Q07m-GE3irMUaqlIi4MmicX0SH2_3Qh4g_0fB1AGwG21RiTMFN8ky19PKlQQXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=ltNp3L1ggrATblw2K-p_jLGtl74VBo0L_SQ-tVMVOfM5t8dL1EGvFR9ti7YxtrItClypw0N3MhY67-6QJt52_FmZmiJ6RpL6IttQIK3MjkZac2MV0QKni0AYBXFsItnVaVuim8O-WQRepRU7VuYCQcC471PAjmWGDYCDFAxfO9tLW5gzHOmSRKgn1KCT1bbkI9WxBtOd3lXz7rxRUricnxQTFlYmg7mVkXRaex5FPWJW1Y0c6DPHNfJNg68uKqWQstpv96C-ezlUeTrrMArRXE91Q07m-GE3irMUaqlIi4MmicX0SH2_3Qh4g_0fB1AGwG21RiTMFN8ky19PKlQQXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسمیرو بعد از پیوستن به اینترمیامی: اومدم به لیونل مسی کمک کنم که جام‌های بیشتری رو برنده بشه؛ برادر در بازی اولش برای این تیم امریکایی:  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26983" target="_blank">📅 10:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26982">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evuS-gKa5-tDCIZqVYkukhcdg_rQ72Fkp294SOKcfsmU9y6qAebCqdssami9fvOKZPM3-fZE4potmzmhXhnKL-qIXFi_5np_s5rEdYsUhKw1cwzYDxbL3LhdZkUd5olUfc-P6BO99BQINbsmkApMV3n29CMrAQG0OQghplRtEOqkVrp0k93rJKQi71rKMdJTkX066q0WCx48zzMgrVfvys6VHF-u1vjRbRQDEVBVFGJTAMnK28fUgI0egHg3ZDm03isGbi0SLWnWhzdjwyibTgH3oPPpuuysHR6JQWoZ8iy-_YfDfDRHuLaIiVjAtQnIEsp6wce77pVAwk96TpX8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایدباورتون‌نشه ولی‌این‌دراز فقط ۱۸ سالشه!
‼️
«جونگکوچ ماچ» بسکتبالیست اهل استرالیا با ۲۲۹ سانتی‌‌متر قد، درحال حاضر بلند قد ترین جوان دنیاست و عکس‌هاش‌این‌روزها حسابی‌وایرال شده. حالا بخش جالب ماجرا اینجاست که پزشکان گفتن ممکنه از اینی که هست بلندتر هم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26982" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26981">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=bdikkq8kuxBukdgnQvqKL0Ybflg8XskS6-5X5-jsq0RaJWNLE4DWb7W5Q7kqgti7FaW-RXo83Re5mA_nrjL_goCAVbmFh_u7rhCY07QAYF2JAOl5f-mJ9nm6isu2RiDLdXX_J0bePyteRSnjIVgS3Y7LfD2iQh4ZAf1I5KDTxx3rZRisfgvCeZvUqam2ERGvasTKmGFOvovatv1r9wAlQwNgcMa6zd_CLe0dlobaucnlcdTsP5AOqlhhmOTuIZBS9pcE6dUjIoPCklxNbwzhmcdgFpepytLxXndJ7gCM90Do8O-lsPoFd-JBEWzeiAnOBWAJkAvudu5rX4am0t4faQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=bdikkq8kuxBukdgnQvqKL0Ybflg8XskS6-5X5-jsq0RaJWNLE4DWb7W5Q7kqgti7FaW-RXo83Re5mA_nrjL_goCAVbmFh_u7rhCY07QAYF2JAOl5f-mJ9nm6isu2RiDLdXX_J0bePyteRSnjIVgS3Y7LfD2iQh4ZAf1I5KDTxx3rZRisfgvCeZvUqam2ERGvasTKmGFOvovatv1r9wAlQwNgcMa6zd_CLe0dlobaucnlcdTsP5AOqlhhmOTuIZBS9pcE6dUjIoPCklxNbwzhmcdgFpepytLxXndJ7gCM90Do8O-lsPoFd-JBEWzeiAnOBWAJkAvudu5rX4am0t4faQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
محمد نوری کاپیتان سابق پرسپولیس ملقب به جمله معروف و تاریخی "هرگز نرسییییدن بهتر از دیر رسیدن است" با عقد قراردادی یک ساله بعنوان سرمربی جدید صنعت نفت آبادان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26981" target="_blank">📅 10:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26980">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDcReFWmqzOUiduaRPP54o9FWBpcdyUxI4HMGO9tWfCr9u5qjLXnBZLc_eW13OXvnsDl2NXpOlpF-DnJSjrDmPWLvKmfu5WV-wORm3wo3q-p4E5DxxfdX6VQZdn5UOccmYVPvMqGrS2ntB7np6isEoMlTsgrx7y_9FOCdhGnQW5o1aa5-2_wJlrdm6I29zQljX3URYeovXUh0JhBtK_0scMPifgY-lIkgM4nQWvHC_NNWdRgZQxDs--Sfcaww4wz5SJ7bCarjyceHhzooIsmeH8fi6dhMGlGlzuQW1o0ShW-QUBilqArNv-8Sv0z-AkjGZRpBwphoKaTmSMk_M0mgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رکوردداران بیشترین‌تعدادبازی درجام حذفی:
🔴
محمد نوری: ۶ تیم با ۴۷ بازی
🔵
محمود فکری: ۳ تیم با ۴۵ بازی
🔵
مهدی رحمتی:  ۶ تیم با ۴۱ بازی
🔴
مرتضی فنونی‌زاده: ۲ تیم با ۳۹ بازی
⚪️
پژمان نوری: ۵ تیم با ۳۹ بازی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26980" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26979">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4EJO4WmxGV7p9YdMRtcd7JxG6pfz2747qc3E_S78SEwvQ_zhyS0wNQOt03wu6LdQ9fZbEibO17arutz4JXEs0n2q6SC1KGvHXPAwPrUdewX4qAjwOL4qcqNasFgAZWLHUzTlC_BTbvc-1LsEygTjzt5pWvhokDjndyLxCMehytUO0u2pg-s08CGaAJSCd2adO5btucF8YdZJUX95mkkk_iKteCIRVQhk-rrsoBx4nHgPs4RiPgEFt8R6wAtSX_Q4xlh6hUBPV-_gaySAJHZkUX4Lgcm3Uma5OsPX5GT7iXbXLoeJ7ILg0xUYhSL5AS3aPAjOhOlgR84jjxTlfOmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تمام‌برنامه‌های‌هوش‌مصنوعی مناسب برای تولید محتوا در اینستاگرام؛ یه جایی ذخیرش کن به کارت میاد. برای دوستانتون هم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26979" target="_blank">📅 02:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26978">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz5y2W_OYw_kKt80hoylpcJnmDO5XvjM2a9MWZ4WKLE5N1PrgZjLDaBxKb49Xz9uIQ_Y4L4VC6lrO-11zczhxGh2Ng2g0uGnrLh6eqvioNPLkdJKiM2ibA05eXW3OpZNiQXgIzU1VDAHBYUol8Q03m6mRVLMJda3_JNVliik1hzuhqaydk-6V6oal78sdKe-9dYoxo7tM_0uoNOKxmQGZrc6ZT586uDgRIvfAyaZO63rGQvL8ER4i0Fq6bI6kAfWvOqvLKy0FdOM6GNf3alUL9E1mSafpmanSUmSWcnUwUNw6toxW1CokBxJYkyOd1rF2-M4LpGf-yVAkFE5WQ6vkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دپورتیوو مونیسیپال پرو که به خاطر بدهی های سنگین در آستانه ورشکستگی بوده و به لیگ آماتورکشور پرو فرستاده‌شده‌بود در یک حرکت خلاقانه کیت خودش رو به ۱۰۰۰ قسمت تقسیم کرد و هر قطعه بین ۲۵ تا ۱۵۰ دلار برای گرفتن اسپانسرینگ به حراج گذاشت. جالبه بدونید تمام شرکت‌ها محلی و حتی هوادارصاحب‌کسب و کار به طور خودجوش اسپانسرشده و باشگاه‌رو ازورشکستگی نجات دادند وقراره این باشگاه به لیگ برتر پرو برگردانده شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26978" target="_blank">📅 02:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26976">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqgKIOr8kSoEomWmxoCNNTKzJyldAQjlV9nqBO4CF9MZcpNc-gMCdMbPpKY6B9lFrYsXq9mAQ3I8myOo_0zjT-ACS0cNOil2x3iryN-0ArmYVuQzC7FTmLvulZaStuogx5DYQeSuxMorx8R5gSqZLztN9qkzBSNjus9BkLT3CRYvjD8_Pp39GxTWSOSSCdbNvmErwZOt8AHbNy-5WuuWF8wkqf8WR-Q1u9V_ZKk-49rZ0qzUC8G3pgPAwXijry8pX0ZwAUPwGScpgCbT8-exsewvekjRrKjqmCi8oyzxK9XbzCGSaw9BY_CD6n-QsceaRZtSGXf-NLX9CBjIDlSkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
بازی‌ میامی‌ برای بازگشت به صدر و دوئل‌لیورپول‌ولیدز در اردوی پیش‌ فصل!
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26976" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26975">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrfHv6EcQV5dsuS7oqizZCau9I7aOwDNrKEcMz9QvhilQjxYtC3RydxSUNeYcu4h7I0jJE12-7LciqHuRH__VsZZqIFQLaMeQG9BoaXbltLfSnWU8p0VYmvy9Vb9WxArCxP222f8XRnJalw3RnmZoGzb35WHXU9KKaLKpcRKGUqeSCvrpsw03aubBS3TcDPYmg86SgOIaepuQCaSjU91Gyc2SWk-FSl2wOoYujBo_VgRb7eNyAmn8-AY-66CMI-uaPCbOZPZpLq998ToBf1DOV321kbBzAni1nLE2zf0AlAbDtFN745L5Rd70uITGcFes-moADhIGV9Jtl-GMvNOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برتری لخ‌پوزنان با سوپر گل صیادمنش تا توقف رئالی‌ها برابر یاران دخیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26975" target="_blank">📅 01:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26974">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGz2cCpEOnk-qvAMXvBZryjH6w1g_PrlPSPWvIdkH20VfOvzyD2qL2MUfF7QBwwqeWzCzDbDf129EhePZBbV-GN8eJ2QOmSYMmKLwc2VCPkYrDBNidYWQcBYGowDZtfWfQi7VrnLkB_WiENSl_1q31Y_AcWH2MdRNKTmkv7gJgXrnB0yDPNKA__OttN5OWVTDQz_jdoLDpbrnL1NRSg11Z1NJInH0XzannUfDZLOIDxImFQ0YERDgmMk0Oorr-5Ys1tsxGgKg5jpljwLtlmL0-LbBpePLFL3cltwDPOf0WGH7Y-swmCzX5p6aFjKBGpHhd8PKC-pVk1DcMh6tGdmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26974" target="_blank">📅 01:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26973">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp0_VqdBc33CseRE66J36wUzZjNK7fNK1rzL5Q4AnBE-qeVaEBeKPj1fm19CKY7pqS322r3kwjwTBarXVoJsHhshCKK_6Qc7YRMgNPEBxfYAI1ewyKcqpOs66Lku40WCytAOzk0xPL6vlZ-WvzYcdPEI3Us2UhQFWe_8jMnp5bdInH7fzvBcYY3PvwU1hbBHgvQz9gegVdy0aPTwcY-8TTYkitBrqmZgKK553_DUedssFfL5dN-sgwCSi68ikpLPdjBwlrNufbKYjjf6C1guEEybxlCqBM2vsplFxBgIn7a6WQ07sPqb_hEBg5lGxAnNG6Er4sI6NbkaU8ZibqqeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون مهاجم سابق استقلال: دوست داشتم درتیم‌استقلال بمانم امامدیریت هیچ علاقه‌‌‌ای نشون نداده. بارها گفتم برام بلیط بگیرید تا بیام اما باشگاه هیچ پاسخی به درخواست‌های من نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26973" target="_blank">📅 00:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26972">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8pIe99EXHd6KobuEJttnd0c3bjNDh_ODYhS0NjXHyzRYYPFh_Yhze678x9UQfZeRCSwViQhAEyIL1TVthcCRpzYyANVRsaPcwzmGUQBm4-NzyzwmgRQljlVvnA87S0a7hRqPA4T-iu-A3xfKoLttUzD7LXQ-V0F5A6X379o866qOfNq4u9dn6o3wjKZrOkqJIxzp_2I_DTeX3g0Za6bLiMc12-ltS6YwYI7y_FeSmmxqmZdwN8Ulz65PimQAUQs_oZmflIyYSejdnJ4qJcvaS1ZVUMiX-hv1Ruz9T0kk8RyG3V0yuzyw7K0F_uS27E4Cm9WK1P3r76h7NZJZZiVQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26972" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26970">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlmo9kuh12ya2UBEfnSWIgmlC7-LqPNBVmcMv4Lfr_1bfzf-Eh2VhJYqHqG6RBud-3usWA_dG8EorYTXFB5W_1uKjVBg7mHARYsSKtnPydQafuQ7WNyrRiQ3371jXhYfNa_0Fo_Q4OAzzZbGRTjssuz7WzEiGfYTy-AGCqy7APcTR3-RNJTGZjcITXnYvJldpcW8q5ygaBt2e5u8piYfDW2OOSPXwvZ9kGOt6H5sb9xD91fxsc-OkJyQh2QlgT2YX1dVFznq1sntznxArXVq3uKGim9z4vYmjpq4iGyxGXo7R4vxrWryGB0BOjbb7YFcM7Cys1rZ00TdWFFurnFdKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8O5IXRbg9OmYfaB8NK6MM34LNEG3fcOUar068i4xazuiMq90aY7usoeIXIPyBptrEPM9N86CcpKArAWaVdeedMJyu-9gZVCZGs6tao9NY7la0I5N_YwBMArQyvz4lgdRtCgkx-T7TIFGcNit52yhAq4pIYQ6irxAqZgkLd_WOGYpvc9vXTsOnP30BswCj-sa3KCD_26AJY3UkRUXVbPqqAelDs7ORVSFPR6IKOa3qYs7Ee5dgojgnTcWc_5Gf4bnAOvFGxLLDWHNLukwMrphuKhtVnwwRGlJXAlr2Cx3XDQXjlMzgNo3ki3hYeboBCNwpy1UVLlnnUIahv6WJYK_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دریابنگر دخترخانم 20 ساله محسن بنگر: از بین بازیکنان ایرانی سبک بازی محمد جواد حسین نژاد رو بیشتر از بقیه بازیکنان حال حاضر میپسندم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26970" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26969">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm8PcjObtNxfiI0LVsv1wOQ_WZF2Ml-Gh9ZDYCzQzqvAcA4PjACGp-p-qI_aLHdGw6f9ETxRq3Tdpa-d2HXPcLxjld-ELkV8iMo-rD3ppKUNxTVTWdMOVIxXsBJ0z8NsUoQy7QUs8cxczRm48u3E6uD41jYUGiccZOVaNTkz-L5VnkSanLR-BQVijLnO3F3zrZ3qk_8XCI_Gk1G_7uTVNmA5is8n-u_glpbYZNUOkRABEjBH_QpXsxOztQkmyDQhwfsdOZTtMIggu0KQHPRlhtpouhR-z8_uBjT_sirE-DsycQYOY1_oWA56DmR3dVIfuPAupehLJNAxIT75rZ4tOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26969" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26968">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmWDnluEoYThuiRvcFA4ZrzbBkbFl8HeqTjMXiNt0tb8vnM2lIT39UWWQs2GqbIzH2fnp4ZbPUS1WEMVKl2A-CTAh5o0_Yo1sbjo4ZHpMi6fPQWrXxZleYjcTxl6Bu_i-Fn9qgua1YZMdnczqnatLeXmXzAfLn69uvAreQELHfxqUpkEliBeelzbbrh1DvGB3lO-D9hDxiKcOsrRn4RVNxNQv5BvR1asEaldfLrR5i2LhHyMEscQnrJDEqrRWh2DVcGTaYqK1mIGZ_PnIkLrhitoFadpwcB9mSh4LrUlpaljL7p9mbpgHmB8PujtXQOjpQ3Q1cAMjz49W0ZScefV9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های ما از باشگاه پرسپولیس؛ علیرضا اشرف مدیررسانه‌ای سابق‌پرسپولیس‌بار دیگر به کادرمدیریتی‌سرخپوشان پایتخت بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26968" target="_blank">📅 23:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26967">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtEHubxsLRcBl5euoJrpEwdarKQ45oGdREloATC2C5PLlWcSNlOIczg7_JkTTVZQZnAP2-fq9_AALe_jd4HzieH6CgMVbfjkcNMhPH64L9etf4HjgU8sfsChj4K-hClOqXylErwovVjIrOAYPdOKHFAArdXHD0WezqAwn3KOL6wU7AFTpjR7AqKMfj_7NFtt86Y6WkKeqJN8TSz5BmGp4tWhbCn4jtYHrlrzcgxzf3sbxvIOKTdAkvEnQKKP8i6CFZSkVuR-PTGhc5v0ZbYkMpOcQDCNnXq7jtU9ze2Y7oBnPZDXZjCKvEGMnKsfTU28RK0OjEQNxFRtX1DJ2JHXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26967" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26966">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Et2g9K6qYr6sxamydFqMeutSMK153judJWL0JgEjTLq4jxaeksxVKW7pxvBUqf0ROUBxq7SnxJukEyh4dDxEJJcWzWriWMwIfi5ewW2J5FHWw59n1NfDeschd7RtQpl8URQBmtwo446aRIs-Qf8CQYysFh8Naq5WT5yGoUZeRoetkqBnkVgX16fewsefkFZ6IU-Kt2BWhNwHSJnKHcABMMv4wApH9Pc0hLe4Rs8T77ZaFSbTtqBsYiZ13jUeUYi_Zyo895Mf7DDqoWrLCD_F3UEnCky5AOSwaMvQKusJ2LlCeUPR2AVAJLsboSIb8AqGb8OM2tuoiFqO8gKVAXnogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف‌شایعات‌مطرح‌شده؛ باشگاه استقلال تابه امروز هیچ مذاکره‌ ای با آنتونیو آدان دروازه‌ بان سابق خود نداشته و برنامه ای برای جذب او تا نیم فصل در صورت بسته ماندن پنجره آبی‌‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26966" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQp9JWOH3skh1AiPwHQTpZcw8pyuVj9ksGgHKmUUnPpi6SXYFSkziNUjB-IXDBbbZMBS9ueD9cmCuefGL2tUJzeevzxJedIshlhI5RrMPbn_MGMQ94eyVHG_ljawTKzU4inG9T_ocjhCqnK_a8IORq9KKe_AdbBGctBZuXhO_aXnDVPgeuU3oj4aSe_83TxWbG0T8EkIYLCrav9zY2P7N58SF_6snMC-5_eKiCPnzjdfpOLf86eQHLYEquBMsTK5F4bDbCzJxllpT9fc3sSZ90NA4v9qbHRwJV0CNRJ0bOU8HdEE9QobOVjCv3XHq2ELgpLL0EW6xycXbLyUfFYPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید شد...زهرا خواجوی دروازه‌بان تیم ملی بانوان ایران و سابق باشگاه گل گهر با عقد قرارداد تا پایان فصل به‌تیم‌بانوان پرسپولیس پیوست. همچنین زهرا قنبری مهاجم تیم ملی نیز سرخپوش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26965" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOZaZnk8cHWOalaf2xzFciiHWeSVG-lZ-8fmVLge6N6wxX08uecOghTnifmhRo9lqhYZSZ3kuES7GtX31EDLk0qDdJ36xmfK8z6-IcSuZVVNgCMJv9r2Fmx_9UvNNJDG34EqXyTVi8ON8-Yw_q13-Wy4oWS74Tm9R1FRIcdlEeNdAu_in88YBh0NDj-EA84XIwR0lHsB06_ay8vLa3hld8r1nT2MLcseTR1zLuPE4hheSRZWlFzMyEoFHHkUkSOH4CKP6EqUc9Vck71pfVjpI_4PJAO8iwVQiAfTF9WmvgkZ-cOCJSJzNExxDKnPsWArneFv8O3ywX3rGBPUQ5fdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدید
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26964" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26963">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXL3qqa41pHXRhtYi-XuHpD3U_M-vJFUYob8rJzbkbv5de3aTlH4Om_r8szxNnhAcXAtF7DKiS5u4K4dLFtfDehuOOFZbZa0AFeDrrQCcUj4mRNhO0UZyYMmSU5XTx_9yRRatKMcFUb_3jddpMfDugcaWtJDXNz8Rr27fa6VXr39dy53ha7kEvmElJ_xvjOp1579KKL9ajv4zGjhBphFgpLF4B9awr6OZ0R7RlRCuLlwOC_g2KfWM8YSkHBFLIaPIkiaWPR7HLAFEkofz9KPqqMhH10GxK6HZ-A1KftFbADriVk4vjmypmS1d06sIaVOAlFVTnMTtID6rjGnK23TPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26963" target="_blank">📅 21:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26962">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HthF52sjwnSbnGFMP2LZeX0WcKnuKyU2fzoSj6CM7rd9KlXOUG_DFWgatu4Tm0aLhLHIGpbhDZpVuTMRrl8UcseVMBNvxYMOVYBz91FAFWVfHlCLYmL6PYQi13nI7tuwc0N6BD9cEK4xjRVuFw5cbPG6HWJjM2RTcBB00X_i8VaAiWnyrWYd6uwZd-MUPPg7hXLUqE1TB5zV800GvN6m7jXqWQMn_UfcT-w6MhhId6ehQALG6GDY24fhj5bolvf4_2dEXrz6fN5MQGC7dpC3ukJt4NfL8sZjNIjrghYSA6lDeEib2yUF9UwNQEZGGDz2Ehzy4QnI7gz6dC8yOe8ypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26962" target="_blank">📅 21:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26961">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxj1qyouA1Bmq0IAQaj_8up-PvjYuK_mHpayF50rTLSRdGLGmkFq3WOYyj6eSgwODWiVT2uOAHuachsdjuiCVcC7Fl0QW413_tz5YOs-ipo0vH94yXUe24CsXBxwBYP-hTT2hRf_rb_5xbrvFreYtmT_P3XFZzeJCOVMJxMPkO_WvkQT0iYDFtwOXtZa76KwmD-4UVty4Iu59IZsRtrFHeJulX4_nC3Ke8j1uTStDlycg6nnal3FZrbp4GWJkw5NlC4CHgSj7AJheGWNszs3baGaUjBUMypKes3MiGprHEYsXg0uPX_J2II5R1R_dCgB2afKKhpeOcP1nZfzTh3IjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ های رسانه پرشیانا؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ سنگالی علاقمند به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26961" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26960">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI8k2hjsYiSxNwB_u_EOnq2sMOw7NOlyjbWD-bPs-TALru5cwdiXKkew0d-lHjINsiAE6eqPuC3JCgRdVa5DaclnyV90cUeaaA0-dpS-q8IaMUWrq05iOEF9BA8k7jw9yt6YOS2sCP5G-17PDkl2ArXxT41zPxrf4O2LfSTXQ_iBZ3wYB3-IsSw4guR7EbdtIs5aLcClnqCyvDhpAPR3DZ2rcx8Jw3MuwkZaW66xyGQASn5St35lqiKbb6NrszJd3bWCrawL7gbygtI1AxcsjxF7e0lXB0uYEcCX96TQNe3I8h7nE2ThE7vKOpHjrKMiyv3z4jfHNhginYRGTp_oyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26960" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26958">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=J3Lfd6kqm7Wd0BQ-a6w-maQArmzl9c1AC8pMY0kO_zHzZWu76Oryn8lMGQkfHYJaVoB8S6FOAva23UH1cxEeTT0DeRZyrhlHOTRfR1I0NRDuyge9APTiu0x8alzuhzDE7kmrH1thYjVthPEMgVkJmQfABCYYfICxnCdWRwnV-ZYAeqiD5EqNT3h-hAXPds3HBStmYJ6kXmiwF1RnpIjiZxlQd14bWBsQwemj-rFxjEx-oeBEEsSpiCKLcL8A05ddqCAwXaZ6xjnw-SbAeihc448-xgc7xUvmxx8ucAUKIbTIdB6eafEEcl01g74NGzTF5XabMXBO626G7MZna4zIsbVE5TjhLRaJ6q8pZhlGhcgLAc43ukFlxqS7JCUy-JEu-UiwywYkHmO0asxocm2eLPVgwEUziEtai1dXL3b7za01moCUv8EO5R41t8OFm65OKgauIsU1_B5a6I39f-SOiAxbj3Du2H4OkFoLeXvrK2NI1HtaiTcV-8NkfymcTrYkakffFUAKc5wKS5UUoeLmdwJsnstJ1FkVWcmybosSM2U0tA3EM79SXo5EZdfj7fCe6beQIfWE18U61Z0fEj-aPRd2b8_UZclsXiZZEoOf1RjcXW1D-kTt8b_9JvcXwBKNO_4LkNLQ5_rq2yCxjeGaQN-9_dxjE_FpsHRcRxZwpuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=J3Lfd6kqm7Wd0BQ-a6w-maQArmzl9c1AC8pMY0kO_zHzZWu76Oryn8lMGQkfHYJaVoB8S6FOAva23UH1cxEeTT0DeRZyrhlHOTRfR1I0NRDuyge9APTiu0x8alzuhzDE7kmrH1thYjVthPEMgVkJmQfABCYYfICxnCdWRwnV-ZYAeqiD5EqNT3h-hAXPds3HBStmYJ6kXmiwF1RnpIjiZxlQd14bWBsQwemj-rFxjEx-oeBEEsSpiCKLcL8A05ddqCAwXaZ6xjnw-SbAeihc448-xgc7xUvmxx8ucAUKIbTIdB6eafEEcl01g74NGzTF5XabMXBO626G7MZna4zIsbVE5TjhLRaJ6q8pZhlGhcgLAc43ukFlxqS7JCUy-JEu-UiwywYkHmO0asxocm2eLPVgwEUziEtai1dXL3b7za01moCUv8EO5R41t8OFm65OKgauIsU1_B5a6I39f-SOiAxbj3Du2H4OkFoLeXvrK2NI1HtaiTcV-8NkfymcTrYkakffFUAKc5wKS5UUoeLmdwJsnstJ1FkVWcmybosSM2U0tA3EM79SXo5EZdfj7fCe6beQIfWE18U61Z0fEj-aPRd2b8_UZclsXiZZEoOf1RjcXW1D-kTt8b_9JvcXwBKNO_4LkNLQ5_rq2yCxjeGaQN-9_dxjE_FpsHRcRxZwpuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
پوستر رسمی باشگاه لخ پوزنان لهستان برای اللهیار صیادمنش مهاجم جدید و 24 ساله این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26958" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26957">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODvGAgAmxV_oBDCrQmDTNJ8hePokmQ6YGGwoK_NffjJ3485h7UVQcCYvsw5ffgSodTwuDaQfMq2hek2ycoPC3MY-SjK_lQf2SdbBlvLPH2qfq_PR3ovtbYs5DVKr9nCMJklu85eqsJYxuZZLD8awjGQrpO9PpXQCiHGCkS1DGsjSYJzH1TNJJcctXEELjulCCFcvnFA6GdmJwzxcOHPt6H5M8adFxabIg11svr8e7wugUZ8b3ZAiKwGZo_sCTNwgbuJ0Uv7FmP4_wZNDrN_MIbtvxQ0jPrlgClnN5Z9SaQPE9Doi_uwVmB5G4OlMD_qBI4S0MB7TBEjhUt4_QLPh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26957" target="_blank">📅 20:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26955">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rsz_WuLnXF57xTdsVWt4lNjFp1-5BDVYDWhO70grA24SNICL3WDx9BxoGDkyvqxRLVnZhk9qDF7bAtx9oImitHSrDxiP2vyJ_x64caVtLQmH-Ic8yswANrZQKpTAr8oX48F1xj9pr1tVNeYGjbTWLn4J8hiCmoWAV3hxdQChFW0HNr1DEwyywhWjYCAedXDWQ--UQdF8cCJb-hMtZyYUJS1gLcAwnr8ZNLWeyt1yzbBzieZuyQwHWau0uqcNqwks2t_ks2jmH7Y3DVTzO4luUT6-rBPA3WQ9dPterlbpwK2C-h8FufvAKayNPaBlPWx2ln89Cma0PsldCu3rtARhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HEZaLVHpJj_TotudD6G8l6K3-KYJoN1FOouAj1BLjWoJ065OAPP6cMGiR2sr9qIH-uLIhZXMl_SulM8WoiAIqVCfWN_Io5OsaO8hwh-enwspvyJ12LYw-M3nbYNx2LFkXMPaao5f5CUh7CNNmJ2E9wJU0tFiidcToXnO5702EzZtw4spmgsAR4k1dTt6EFAFfpBQbZpKyCoEDFFaiS3uvA_XlMOetNiajKSsrU2VGVyabPFnq_9BnaKu8AKAQ8EGmqG7pb_7SrF5kyyD_JJoJbGNhKdUIRgPjdQUseeiRAc15SKoih3gyXgaDo766JVF7DNnQjNfR3m0W_VjNs20Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📍
برسی تموم اپراتور های اینترنت در ایران. این‌‌ پست‌رو ذخیره‌کن و برای دوستات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26955" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26954">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_z2J880cn3K9gdRlnrMJIyR3SosBeEepHeqnEhqi-DQ3GtBrcO9AEgEni4ewF2IJEfjxTTR9RzSK4uHIdJ4PQasWyW3sj2Z8zvyj1VFvXtIC1sr29E2fEZ9lvqYqVR8dSxe3ry4zt6mgBc7hc1FLiOY6u-7zrhJFVSZZlVsMtmWqfndjxyLK3yp6g8WzmvfsecU-M5XFje2GG6AvYLYTazEvNP_W1BWCDNJO0RCD_jwayYUbdOh5xJdTdvh4_R5KZEIkE6X7Dghp-G_lfk-C2CuqTiM1gsefHL1fvpmKTZXX-oNCLQtcovXNKs-OKujHuDlK_bwj8qRxfwxMsV9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26954" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud_pD1TvEJ_QNxAYTobP5TmQS3CJ8sz-ewmNxDWrocTMHyppuUwE3Dn5voKdsPwHydG-f5mXn03hvdnbUbeC83ZAd0Efiy4yFzqkJ47MfQCk4vJdxyEHYiCIYTKjatz24sgTMyJILeQe2e2Awx90BdHL6Jzuuo3PphDXg6aUMcI3CJZVqukeKABDdaHRiAyKowz5G33FF3dGUT3s_2ISFZjOhxRHpRJXajEK7zzX3J7DeJHQzjSej7419MLHUYYWsqH1gH3Q3cgdEVEZuSr7cXP0ppzGkN6zbB-xv7LuDbAbdzmnuFZrWjkpopWfUX64qkDW6MQjsWBI3GqT69Cdmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26953" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=F_zWKkX6GdmZwWkvkeoUANqA1HdCKSJAW4bESEkBwv3ZAJOJ7ka90YUFdLnCNO0WaGg8Yf_u0H95P-ZsrFjYCMxiDqnEiywV9z8Su9KUal-ufD3u_X_J3rXUVc5jXJDwp59RlpWsDSqiuH-kKI5RSa6OlZ0pKE8Z5lm4LqnhbHMnyJG-539KHFcEYBPdwJqD-FgArSMn0lWWNM6pRbiCQw8dOl5tkv4jMDPxP-KjJ4VGvk06UuP9JhOY8SVBqEs659bAcyLD5RB4TmzntM4WZR5wDNhpzKXbf-bNITmb24NonTAYWJ8plkZc2wc51jcjQ846QhHlKxPhtYUVqcxczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=F_zWKkX6GdmZwWkvkeoUANqA1HdCKSJAW4bESEkBwv3ZAJOJ7ka90YUFdLnCNO0WaGg8Yf_u0H95P-ZsrFjYCMxiDqnEiywV9z8Su9KUal-ufD3u_X_J3rXUVc5jXJDwp59RlpWsDSqiuH-kKI5RSa6OlZ0pKE8Z5lm4LqnhbHMnyJG-539KHFcEYBPdwJqD-FgArSMn0lWWNM6pRbiCQw8dOl5tkv4jMDPxP-KjJ4VGvk06UuP9JhOY8SVBqEs659bAcyLD5RB4TmzntM4WZR5wDNhpzKXbf-bNITmb24NonTAYWJ8plkZc2wc51jcjQ846QhHlKxPhtYUVqcxczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26952" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26951">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7UZnbOnX7RNvQrN_Zx6FDM_7S7ieOjIB0dMRDZvO0YnuUrsLjAnn4GrlSOVQagCFIgtThMKqhB0lkrtI9razwzqzg6ePLTTaLB2rYtbvMG2gn0kqGL4UOfEXYHjFAOSMIfgvgk4UZfo8vaoflI1tZKFJG3jieYPzIOSuA8V13bJlXKPfyv4EJ6s7cceHRejIFTYUWdFQqC-35j-kefrChZadvGmllP_PxJPFe9JZC8S7E8RZZhpSthZwIokLZcP1CJMY11H0neDI873HHBKcg_LkoGswmkzHTjTv-GxzobWYacEUIDD-0GGFKTv9622pYjnAd4bCgQ-GzSziEWTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26951" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=Hns8PfsXSFBHxku9BCEPcQ7TwTRGJYcMUjsQki4-0DkZfDFDqM93CJ2Lcydb9hprt9papiE1OgKjTU-0xGFjUescF6_uyn8mvhAb2rF33VDoSrO3WFHwhBbFUakNq9ENjfCQRGcBwwV4E5mOoP06t1V4n_wRfGZjl09znW2uT8h-JjJF7jWl_Zv8EITXBPDmBX7S7_6WBAvEEWcs7QzxN_QD-FFofHQ1e-GAoWwfkPzgUgsQLABmaVX_tVWroK38dOFLzPA6R3kN6lzftQ9_KOMXS3a65Ckem_Xuj2d1bszoBwKWZd-kGidrIGjtz906_Mur94ZXhgF4zqEqHZ4OSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=Hns8PfsXSFBHxku9BCEPcQ7TwTRGJYcMUjsQki4-0DkZfDFDqM93CJ2Lcydb9hprt9papiE1OgKjTU-0xGFjUescF6_uyn8mvhAb2rF33VDoSrO3WFHwhBbFUakNq9ENjfCQRGcBwwV4E5mOoP06t1V4n_wRfGZjl09znW2uT8h-JjJF7jWl_Zv8EITXBPDmBX7S7_6WBAvEEWcs7QzxN_QD-FFofHQ1e-GAoWwfkPzgUgsQLABmaVX_tVWroK38dOFLzPA6R3kN6lzftQ9_KOMXS3a65Ckem_Xuj2d1bszoBwKWZd-kGidrIGjtz906_Mur94ZXhgF4zqEqHZ4OSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTyQNmlXmxiIXaARnEt5aGM4dPHFbzJAO2qJCadxmDtqRYXt6BvHb-7QNgvZk19eiOJ4EN5TmMe4mRqcvXJsi_pmQToNDqLBWHd1U4mreaEo-HTpgi5kEqDTnpo1UxdfCSOFNrHMk61Fsm8dDkT-SyNgBpkU1RSu_BrBi64xTJPCBORQElrxHproK9Dn8w1tGd8kAtwyiwicPWaq6auiJhrS07KgvPOkC-K7Sy7RSDr6YsbszJQoczLsl028pIe89WcVRdK3_paI9IqXwoOS7s5PnTwP1KRmu7akQe4NS5DmyWqHOoKwQgExXxgXvIVw00iSe-r3thYVH2wEXFaNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26948">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McbDrAQZT4yNSuPCY_2zj9swcVswSd3fMQPfY_kPWLQX81fW2aLkaKPrXNS-4Cwc-qXqsfKhiXhW2ijeDopkHHzmTkDI3bjStMcV6az3ax8mk-xsTWu_-hFy5-ApmFbU28muEigr_XCf1XRwQB3d5tfTmMDlYMnIGrIPH-OhXTXSjHPAwnD6-OL2TNbXF4YQvEJLYx-IZue7I48HCycyLJ81Qts6gx4vhHeCcU3JY4X2OdxH3YYRxVFWGUoJxQ1vCvPQMm0G70KEvN_lbbdNFgwf4D88rU74kR90beJWHQEwlqaWkssnr62HNQjU0fOuqaVTEmA_20ysU6_uFQ8USw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26948" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26947">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiaLK872YGZjQZ578azpaceAo9q3eTPfXDeifSWxDGiTBP0o2HZ3B-nwAleLYJKLUuU8P9hMbgmm-lKmdEGy35JHyUy_FN_TzIU7uilQ8dJhvnGv2w41IPkK0R9nG6PkVofxircRJIiEbGFMjRD-f0ZQZqLzjxFthSsT5HTeJphsV1VVEdWw_DJJg_VSF3DWKF0j-E6IT-24nH2Df1SNnzVNrdgbugqD_op1MPnt5gJA-QEaHrJq5ZtAEl0ECUVoPQNK87PYl2pnmUIizd2iWJcqpdSBUU4phIsJ_3v7mGI9203XwjhKPeeBPcQmUAgcwJ-2AoXIWikp1hc1fvWG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛ اسپورت: PSG این هفته از فران تورس خریدجدیدخود رونمایی خواهد کرد. تورس به لاپورتا اعلام کرده هیچ علاقه‌ای برای موندن در بارسا نداره و میخواد شاگرد پدر زنش در تیم PSG بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26947" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26946">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWxzW6q7EBQaQC_MAaTAkWVgJQEhvp6v6MK_Dymwv4kVcqtQpXNjuBP44V35ZPDQWEklevioxt_l-1B9b_fuQNmVK3R9TTeLGALXMmjChy9pMlwgzvvajwk4247x2fW-XeKxlpMyx1024eLYhqUEwyfS55N6MZ7IT2qtdIyjJzFtMcrjMM0woFcONKSeZ-Z5etW6NXBy7jpRFisFcXDbGbBlFFrvDcFihIW3HWm9MaBpKNMJzhhKFOf07OIaFrFifbXrWuc40eMCrpPGTk0MiegqPMRWMZ_qsKULdqIRi03Dcn3UJ3wdF3B7d5yCMZpH_eahcN58yZA5b2lT_CD8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26946" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxdLMqpaJrL4yh7guLyihfBx_ZdpPYGR0O4sryFTIZldc1NSSvEiXZOvJQi6bHD_dimsDLJCeePKnpODwnggWuuLvk7Jez5Yi8lH0E43RPdogrlIcDx665iUe6MuEkpfi4DGt-O-tLAN7Euxpo_0_aoU4jgi3MtJOFDYTUssnJ301CebXbxxnie7My_-uYyJyQy-C8RmCr46gjZpu6NOVho7ClK5du3Ut7FkvUNaIfRJrDHcCjoYOhLgRo2FasH--oBW3BWLl27qUm1r53YvBQootACDVHMMHMDfXrqtGrkFcvwLuN-6Jlf7Rm5wwyhwVIgu72ayQ8zKENIP4nqCug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyOhIXAuYV8T2eJ9QFKTyjOm8El28GqintyQMpLkgsZLt1rsyNHWBE36MrmIVjGIryaJ5ucJKuQQNcuMukXiiW9c198Y_orOdQFk7ZQT6b8h9pslAQQPH66p5SJXE6Ou4xUs0sXA2rhEPkXQemXXqjbTEJMG2D0l_EdwhhTmdQ8523-eziWurcbDpLb-C67R0rvmpBOa_bxjR2ceVt79xL1l8AT7kA4MVDzuIjVgGavDoM1OK6FFnMsAsd-FeO-IhPWu3PPs9sRELPL2XmaSVqwPq1dchOm1E_5MYLLUSrCcqjJa1Xaq9DubiccLIYrjDHSM96aD-9BEusaece7hjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26942">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU1Ew01-Ppl4h0oA-XKIn5fZBxNEaAe467YHkWcvbJzNyQsZINVk_Ez3g1wHbeGbmFhhC9-tpd83LXljw0fEBIk5kqCnlRmvZJ_E7fn-dkaOEz-CBrlFO5_xD1ZGrL8jTWyfaGD93NkThhkjC4Ml6DqPQCujGSl607m3KbQpUVeBN1mrfAHADzEoT26-q3mzrx-nbcxg9qLgs-uTPkfs4ZmFBJ53e3-UvPjQrjs2MM9eNgJldSc10SeLkQla4V75XCuBoglgjQTTmQFhfxtKTWgqgfYNDiioEdr6yquUN-b9kAhTYdS3AJXUFXVUhxb7K_IZBa8Lez8rxqkYRLdQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=LGhy4Ahn5TA9nWTfjU_P8XDUVgONUrB3RIYNvq7mrQ9bWHdfmLDeUORkCzOn7eicZN_RXkzkISCnZ1PXYAuRhv9oSC7bIpBe7_kVptq6qNwrUNC0nD6eLGPwgg94wDpYkKJvZjWFZY5gI-G5m62zC_fqK64WDHZTif4DQ__mcfHhq0fYcBkAfwYVBZhzIbBXXS8QEdfLuJyhkrGV5pMW47obbCOnElURR4xftdKMXNcwmeBCstXEIFN-ogHo6_iTMGB1tBIOFYrI-6Zi7bI_QzDMYvzuJgHDfXHtdomGTsuIlySHPF5XRAFYwS0te2TU_6uZvsLQiiyYnIUiZVQQiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=LGhy4Ahn5TA9nWTfjU_P8XDUVgONUrB3RIYNvq7mrQ9bWHdfmLDeUORkCzOn7eicZN_RXkzkISCnZ1PXYAuRhv9oSC7bIpBe7_kVptq6qNwrUNC0nD6eLGPwgg94wDpYkKJvZjWFZY5gI-G5m62zC_fqK64WDHZTif4DQ__mcfHhq0fYcBkAfwYVBZhzIbBXXS8QEdfLuJyhkrGV5pMW47obbCOnElURR4xftdKMXNcwmeBCstXEIFN-ogHo6_iTMGB1tBIOFYrI-6Zi7bI_QzDMYvzuJgHDfXHtdomGTsuIlySHPF5XRAFYwS0te2TU_6uZvsLQiiyYnIUiZVQQiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/26942" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26941">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=gaySJbO0yW5wQDS2irDoIagCW6X-CU-oULa2rjdI2fhdT49kc7vsmME3pRJjxVoCjVt1wjML6BGDed5EqGEPzgSSn4tTBnw-LDWBHPjrB5RLHWzR2GEB86bWNw-fAkDMRzJfeJphmVALZsFDKsgi-04veO-hDvqzCcW_dQiT2hpKfHRKnwOfNzugBVUoXbmXKUGEgNgKnGVFeMvPht6BkaFBAB2Y9hRIFIE2YTSEld63GcbNGiMqf0Z0Wq6QDR6ObLiw8OBvdcWV_KqYFpL_YBsSWhWQSgS6VHUzoIyS1oDMxNK_1LMfag8_7yKLhUSA-xh6lQan1P_pfYCV0wd4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=gaySJbO0yW5wQDS2irDoIagCW6X-CU-oULa2rjdI2fhdT49kc7vsmME3pRJjxVoCjVt1wjML6BGDed5EqGEPzgSSn4tTBnw-LDWBHPjrB5RLHWzR2GEB86bWNw-fAkDMRzJfeJphmVALZsFDKsgi-04veO-hDvqzCcW_dQiT2hpKfHRKnwOfNzugBVUoXbmXKUGEgNgKnGVFeMvPht6BkaFBAB2Y9hRIFIE2YTSEld63GcbNGiMqf0Z0Wq6QDR6ObLiw8OBvdcWV_KqYFpL_YBsSWhWQSgS6VHUzoIyS1oDMxNK_1LMfag8_7yKLhUSA-xh6lQan1P_pfYCV0wd4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن…</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/26941" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26939">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfJ8cq4Lm4iSQoLbIy-q2BsU02vdev_RyPDlfitON_aATx8qgwJIUfKetF1a8ThTp1LOrcX_snl1ZwJE0LjfMzNh6H9Ak27eg_UBck22Edm7-QDeyNNhPcHwHg7t4SavzGk-9Fbt1MHrlZnCAuGJICinbW34LBTWlkf26zaqdd9wcnp7jzecWxvH8hyw7dJg5EsW4WMk_6lfcfNtYFlusf4Y5xVYYoj5osA4Id83bJvUMlgKrc52jrBYK98EeaHFrVJf9vGCMjSAmR8pbuhKkhlh8MwC6qr1Sfn-yaQY_Y4-SBeNY-O0x0l7RHfzZ0f6z6Wba7H5FxUURc2WnMoQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOmRSmzyrKd8RPZCInnnbbyeB-EVp2XyXWlncWq5wHjKXrKqhgSYYPn5-areJc-bEc9Fqqod_wJU32oY2ByPA8iPisCKTlEoy84R9IsKFGMWVwQP8E6836RN7aXMprM2XwVMQk7r7uW4TcFaYuDLf84unB9clKSdObNHhNkBIHb9G6KyeI40od_EbPd2oIQf1ZaYH0VHnMZcM2ifU_y5_cIuViHa7J3XfiMSR403I3zU4GyLb0t47qWd-DyMEGVQlTZjjT5bpXU95CMx2qieHM3EWHuAkefGvi4VJChe9SdldCBolsUKti6pUTr5tR8SFYZe53buZEnypUPse1IBgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/persiana_Soccer/26939" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26938">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPYAK9DPhtQaGjwNpC9_jL99HonJoCLeWRcPyLIOOd-69LxBLc8eoQXufwOberJ8niNLlMKoz-zodAAiv743jQqeUDwbYxgA9YbtAXrWGCOBkbZPnDsCIhQeasMldw8cXhToqeCuuZAwu7_S2DUTvOxeI02cxGrMDzHHjwdNEecEUBg_LWXnRwBkdiDkynxRndChBwmNgiKvITnaHgX9Qi-a2491lh3ke6qGrItxeJX2yuumRJXgkxolI5ezsRAPhkCbs-LBsONG7drTBMJNftS6jGLm5WpRN75F0zdd0TL7s5m5I69KSeiaOmHf1lbT22wPTDoZ2EuNcaQ9YjQHEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پست معنادار و تامل‌برانگیز رسانه رسمی باشگاه خیبر خرم آباد با استفاده از اعداد تاریخی 18 و 19
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/persiana_Soccer/26938" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26937">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=PeTEHQK91kpmkavedh9If-FstWLbyl--iAaGUpmnLskAcU-Ov1KYlvyeGOz4j_NQGGihGfDV2dnKdjUVC9ZildlKbYctpskNfmHoM_wzaWp4Nw4tXtnhD6bPHzBaiuV9-1v0ZHHJOyZN_joCFjECIDpwyFeMGDBO_MZJALoUFPc7gaXkBME-F21FhB3dnLOM1s3fd2CjvXJ3JqwJGck2g8K7g6uGke1u3yLA-xtPiFrqCdfzMRRIbtJ5v5GgGdEkKAEN8EIpIOkDXSN1kzW45JvmBiuqdFwu3gB1c9Z4cggkla7gJCDYNYKXCp0HrraiPauiCI6VGuvcNnLc7GM0tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=PeTEHQK91kpmkavedh9If-FstWLbyl--iAaGUpmnLskAcU-Ov1KYlvyeGOz4j_NQGGihGfDV2dnKdjUVC9ZildlKbYctpskNfmHoM_wzaWp4Nw4tXtnhD6bPHzBaiuV9-1v0ZHHJOyZN_joCFjECIDpwyFeMGDBO_MZJALoUFPc7gaXkBME-F21FhB3dnLOM1s3fd2CjvXJ3JqwJGck2g8K7g6uGke1u3yLA-xtPiFrqCdfzMRRIbtJ5v5GgGdEkKAEN8EIpIOkDXSN1kzW45JvmBiuqdFwu3gB1c9Z4cggkla7gJCDYNYKXCp0HrraiPauiCI6VGuvcNnLc7GM0tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلیامیپرسن‌دارایی محمدرضا زنوزی چقدره که هرچی خرج میکنه تموم نمیشه. این ویدیو رو ببینید متوجه میشید. امکان کز خوردن پشماتونم هست.
‼️
طبق‌گفته‌خطیبی؛ زنوزی قبل از تراکتور خواسته بود استقلال رو بخره که سلطانی‌فر بهش نداده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/persiana_Soccer/26937" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26936">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBv-QMoxaLxWZh_QCBhOMDTNS7f1UU7g3a0uMUKzubyUXLifMhiBzBJFkPvY7uy8_mv1RchiUPGK_VXzrEE2XKH5YOLLDmEvOFWS-oRpH28Sq38NU6fIPLylHD_WTQDfVNImIol3lQ3mKsCi6t4xivmik0flciIg1dCgWxqzY0J8zGorh1aMkAs7eOqTELyXLEkThE8e8Za74tCDQFj0gkr5RZU4fuArsODxbJAQAZGRyn_bX-QbVZ2A2JwwAWh0q3O_w7oLqikvey2T_zOWlsKBSE68RboUf8nC7cufxdrLjtnv5-HCl2OfogPq--GF-sYY1va1ZV4RGnI67XlMoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/persiana_Soccer/26936" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26935">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMIGZFiHVjwgHG1dPjNjo0kwDpVnXtKT4d_1R8LOPZvyWKJGR2YPMYvpqniTPLbgNCedNYXCyYhCCP6LsR1eE_A_0GCro2RzKesjg2NFnWrKa-BuHo8wesfyXE-BLWf81QKjRyDK6mRQqcvg3dtYpqjMj3KJl-4-n-29pd-7g7YUBNRiRXbAIFPdPx_80zlqOeMU7y2UoPEp2i_TbUMeyYbjvfVTEqU9YwDL0f0o1Hyhzl7U7fIA_TQfxW5RumfgpQCe38UZ5cELYwpdXwN-UtjXuxxNw4HBJ0R9xVu4QE5co1cYjedh5tUysSOTd5hD-YpOmKVlu5dAPdu3zWy7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/persiana_Soccer/26935" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THxmyDxzGoCC7JMnk5SvtbW_6jx2C-0H0oPy2dH0bsgdKbe2bErGQofHrExRAVof3aifXCFfQ1eWeMjhbqoejDecnkiJK-k4_VlqikI9Ey15YKw8h-iExZ48XQ5xu14pMxeINtzEaFOzZksn20ITWJvWgO3DoyuBSSTodXlOVKiT4ykEXDnBgw_cd1c2O8Kisg5LG3ZLicrqcIRd9zj6qU1cRDh0EXrBjtxqEma1Go-wuaNelEbnxWb4vfnvto-ByB13Btuxy_lIXNHOaqQ_rSx_nkOVaUXF7I0v6U17ezeudFvEgpE9gnKDt5aysosr3C-LcO1yCro0ZGOqYsvj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdFexdv53fmYwxvserIgUJR48vfp3CSf_4kLgAv3_A593QY9vIyJcQve_VPB7TO49gQvpefMx2k2WAR7zhz6SsjuLELZn82Ivw5pDIWh49_X04E0lKH0QKEcHwq3TBWxZAZiwRWYMvsiB2_LO0YgRdpGgGZv1gM5zIHzEtS47Et0tsd36tqPZCl90cgZySGW1e7eFoAIMdBoYulxxz2LgX3ip6nii3XRJfmFWfKRd22kkHj36dZuKVtxuO0Zi652LQ-MTJqHxU8CsHwuiyVCSkztWRPfMQwrwL4gMDoCeOSx3dhkfd5MB5XfDNGeXPERefRZr-DyquIErMxPB1KTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7G0QH5sSHJ2fPG15GtlCjyEKKd_e6tlqH-hGODuAiw13OrXYIjJ4VRRtqVjE4t39ZZH0BOo-TjHMHzWAvA6dQE6ByeMTrrELP7csbNOTo4WCyDRn1Tqous8lzUWOl_PuaF-QWHWmEJIS1ogzwJqbtpHHSx0MSdjobsLHoDaxOZjRHZBV7NJvFi5ZBogCcW-ij81P-XIi5wRQiI1TGSXftM4dlXzjwlwNO7di8CigkB2br5cXlowxQT91RLPUJhckxyEhI7t5NGvy8ebzRSm4YY99etEwr5fjPVA9LKG4okLX1nMqsbJTCoZfX-bGiIPr1qS3SPKyZJGkX3XBwu6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8jNWvKZSK50lQ-1p0ISZkDqIMAKVJslferJE0RNYGZbz58CrIIUizWqJ0th0AzZlL71KxbbaHPV8vw5e13ETJUvTL5CcziWe82tVd3TXKCEDuDpBVD5PAaq1_nrc642jjGIoopwwz7qMFJUvTxwQV5YwFBcNhTQtjrMtusLrjw_fnEoyv-TWpH4iVjmBGQNsVYL-TwKsy5328uaZ6tzKjEvTn-ol0mCeklyQT9yQCoJ6AF0ABbN1oRwFgGEi_zmFW_Ocw3Y-1WuG3TLgL32aqMaPYVejfIFxutq8JE8aP6QmiTNoWjZe2aeod84FUF_GRGnhx4YK5QycB6RRr3Kgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
