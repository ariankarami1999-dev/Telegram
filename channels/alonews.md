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
<img src="https://cdn4.telesco.pe/file/ELypT830Th04NhLzYxY2_JTJUZ9oB14yBLKNW6x3fLCrPmHjM69rIO7aoFKKsO9JOvI-omLXAtP2irP80tLDbYXzGomE6MX6OM035hLOl8XxsHKhTksb-DoZd9YwjN9mVf71ci9JgdoWA3YsZP6hFfzZjAAxanDnBMUMN1ZRpxYWNrdaIM6K3ZKwwoiZRRKni6z66ybKYUVdhhs5RijU6OdQTItBSv4tDlRn1ZMwu2yfF10Zw-mMunEaxglU4sJIE30dj2PUjLnkNSMded5L2q5ZY93dRq6-py3QOfEIEC2TN3pCg2q_dPXE_tfCPnkdIfAB6HhFfSGVxf3HFCLiTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 995K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-148607">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7AmbQd4Z8SXQnVIiLCvbkpuA38DqjI51GQtrXZ-VRSvL4vs8K9i5jF2KMyaFPHlOj64-BmT4Hl6f5DOI5EGgtNdso_Ns-rw06K2ffB5ffYuBc9V9d_ke-FLOQvgkLl3fgVXmgd2b_LWsSiuimylQ_LmRUcdlsWc36KQ9gxHssSF1Bc_RsbtHwaxmSMmVBpiVRjSV_vOLp2DSJ9f2GUnslSYq6hdSO1nl8Hj5oPJqof_QvmsTzLamIgnJz2F7tKKSKiFhAHmarrkFNv8E46MKCvFJIgALDJXl28IRM5gHzBYfGcbcQfeToRC-MV5X9HvKTzXEaNl56yCt_fIynBbcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان از اولین خودروی تولید داخلی‌اش رونمایی کرد!
🔴
عربستان یک خودروسازی با عنوان CEER (سیر) راه‌اندازی کرده و خودروهای برقی با نام اگزوبات تولید می‌کند
🔴
امروز از یک سدان و یک شاسی‌بلند رونمایی کرده و قرار است خودروهای اگزوبات به هفت مدل برسد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/148607" target="_blank">📅 20:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148606">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
قیمت نفت بیش از ۴ درصد کاهش یافت و نفت خام برنت به زیر ۱۰۰ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/148606" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148604">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAtusa Net | آتوسا 𐎱</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdTnw98V1d4FwZEPiPf-s8iRJnjAR2lUtaWmR_3r3BpgjszNpWMDMVL6iSwcZEaV8e-GT7Fzw_E9Gxh-fJ7w7Vf5fash22hiNf9_I98PoeYxkJ94VwcFmhvSvyZqGTKSFunVBuFGRe_0evV9GKki6PxfafljwLHPBpaHqHo2OnK_Ge4cmjduwmQR4Ege27CU-_VoXvPVAtK0km9K2ciwFiO5MRLvZY3ls1g84iFAVoR8mXUkaCEaNUcLVq6HL_AcKUOcLs1W6EWZ_IhI_vxZyAqV0UiWvmzDyq3oTbZwSkd3G2VR6vSb4j-6cpt_4qPcOs0GGvixIdAPraoGKyE6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💙
۳ گیگ تست رایگان — همین الان بگیر!
🎁
تست رایگان، آنی و بدون ریسک قبل از خرید
✔️
مناسب نت ملی
برای دریافت تست، وارد ربات شو.
🤖
@AtusaVpnBot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/148604" target="_blank">📅 20:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148603">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e792e78e3a.mp4?token=hwCT1naO0Fz-63p6F7JEHF1jiG-SMgSYOoccfiLfASLBX1J_p3l4abFCCnH8WN4LE8itXZ1Bw6-UqX5AeqVLMglO_kIns8sNBASFKv25HbX09sAIKBNFSjuqJTyDkbX2wDw6EMuVisBM3VVDrsZo2uo5kAe5Q_19k_hmKJlR0ljPFK_GEVYSsm_ygq64FDIkjLvT4nl4d-LgqZ1MR8sFWWeLHzr-OyaA2x8Pt_ivTMJNzJIMbIMzkOgVffjSv_x3MRcKndwBPwWMitvgvfmZvCa1_opHdAaP_yVrY_t5PQ7e4oIBMGEBMs-zmVdG5yLFNzE2qJ231D6k-ZzGmMGEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e792e78e3a.mp4?token=hwCT1naO0Fz-63p6F7JEHF1jiG-SMgSYOoccfiLfASLBX1J_p3l4abFCCnH8WN4LE8itXZ1Bw6-UqX5AeqVLMglO_kIns8sNBASFKv25HbX09sAIKBNFSjuqJTyDkbX2wDw6EMuVisBM3VVDrsZo2uo5kAe5Q_19k_hmKJlR0ljPFK_GEVYSsm_ygq64FDIkjLvT4nl4d-LgqZ1MR8sFWWeLHzr-OyaA2x8Pt_ivTMJNzJIMbIMzkOgVffjSv_x3MRcKndwBPwWMitvgvfmZvCa1_opHdAaP_yVrY_t5PQ7e4oIBMGEBMs-zmVdG5yLFNzE2qJ231D6k-ZzGmMGEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / پستِ جدید کاخ سفید : اتفاقی در راه است.
🔴
منتظر باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/148603" target="_blank">📅 20:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گوترش: شورای امنیت فلج شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/148602" target="_blank">📅 20:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گروه حوثی (انصارالله) اعلام کرده است که عربستان سعودی اخیراً 157 حمله هوایی و موشکی را در مناطق الجوف، تعز، صعدا و مأرب در یمن انجام داده است و این اقدام را "یک تشدید جدی" توصیف کرده است.
🔴
جت‌های جنگنده F-15 و تایفون که از پایگاه‌های هوایی خمیس مشیت و طائف عملیات می‌کنند، این حملات را انجام دادند، در کنار حملات موشکی که از مناطق نجران و جیزان شلیک شدند.
🔴
گروه حوثی هشدار داده است که این حملات "بی‌پاسخ نخواهند ماند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148601" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرگزاری فرانسه: عراق پرواز ایرلاین‌های تحریم‌شده ایرانی را متوقف می‌کند
🔴
خبرگزاری فرانسه به نقل از منابع دولتی گزارش داده است که عراق قصد دارد فعالیت خطوط هوایی ایرانی مشمول تحریم‌های آمریکا را متوقف کند.
🔴
در گزارش اولیه، نام شرکت‌های هواپیمایی مشمول این تصمیم، زمان اجرای آن و جزئیات محدودیت‌های احتمالی اعلام نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/148600" target="_blank">📅 20:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ایران ۷ شرط برای بازگشت به مذاکرات با آمریکا مطرح کرد
🔴
رسانه «امواج» گزارش داده ایران برای ازسرگیری مذاکرات با آمریکا هفت شرط تعیین کرده که به گفته یک منبع سیاسی، مستقیماً هسته‌ای نیستند.
🔴
پنج شرط از شروط اعلام‌شده شامل آزادسازی دارایی‌های بلوکه‌شده، پایان جنگ در همه جبهه‌ها، عدم مداخله در امور داخلی ایران، توقف حملات به خاک ایران و رفع محاصره دریایی آمریکاست.
🔴
همزمان قطر و پاکستان تلاش‌های میانجی‌گرانه خود را افزایش داده‌اند و این مسیر جدا از کانال عمان دنبال می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/148599" target="_blank">📅 20:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148598">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8138881fc.mp4?token=vWfxfkeDzuqZBpMbh9Pzksgb_J4ysrdn3zD4qmWnOC0zJuimRieK23ov-el1RhNBISFQ4N_d8CX7jJLdOzr7jBcD7Pv8s2rfPh5hyR_qkG1HI_I3gnFDFZ0JkVQcgdZzVAZYs1ngfdOsE8ZNp-MjrAdY2W6AyvMUfCE4bUCXkeSlDoOW-8J2yaW_U4sEh0yCmIyX-UexuZVkrawqHktSgHjoStEErpiTv2mLAz65z561K8QtedSZTl91rvJvXG6OSCYLFAgtA-yDqf0KNrJNO7yZrN8GYVVgXgl6vfIlFOGTxCa-OHLK5ReePAilFZNWktxOH2jCD_hSKbC5PFt_hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8138881fc.mp4?token=vWfxfkeDzuqZBpMbh9Pzksgb_J4ysrdn3zD4qmWnOC0zJuimRieK23ov-el1RhNBISFQ4N_d8CX7jJLdOzr7jBcD7Pv8s2rfPh5hyR_qkG1HI_I3gnFDFZ0JkVQcgdZzVAZYs1ngfdOsE8ZNp-MjrAdY2W6AyvMUfCE4bUCXkeSlDoOW-8J2yaW_U4sEh0yCmIyX-UexuZVkrawqHktSgHjoStEErpiTv2mLAz65z561K8QtedSZTl91rvJvXG6OSCYLFAgtA-yDqf0KNrJNO7yZrN8GYVVgXgl6vfIlFOGTxCa-OHLK5ReePAilFZNWktxOH2jCD_hSKbC5PFt_hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکات عجیب یک نفر تو تجمعات شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/148598" target="_blank">📅 20:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148597">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ترامپ در مورد گزینه‌های رژیم ایران گفت: "در اصل، سه گزینه وجود دارد: نابود کردن آن، فروپاشی اقتصادی آن را شاهد بودن، یا به یک توافق رسیدن."
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148597" target="_blank">📅 19:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148596">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
در حال حاضر بیش از 25 فروند هواپیمای سوخت‌رسان در پایگاه هوایی العدید در قطر مستقر هستند، این بزرگ ترین تجمع سوخت رسان های آمریکایی در قطر در 8 ماه گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/148596" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148595">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73102782ef.mp4?token=Ulx0i_pOt6BpLPXXaUr_zbHfZgc0NbSBiY59T6zyavvrjd1_lBcqi1ciQ6uSJnA7d46zdeMdHru0oIA4YqbaIgAr07LexaFTri9WmYkQnliZEpSId9_8N7CkyLMLIyaeFxKWKCWopha7c8e88JSXp6RnseoorbKRdksKokZ7Ha5lJrjlbdSkCmuIfBcEP2coHRYU83E7X6YVcVjDkAg7YSKXNRVXDxuzP_hQpCAqD1-H26vNmmeksnAu7L9MHCK_vcJ6x2EgjZcZsOkJ8Boc3VWl65vOOod4bkWxgFHgRRuLTf2fyr_4xMG3XvOHGyEw18II4_O_VoT4Zg-dSYeLHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73102782ef.mp4?token=Ulx0i_pOt6BpLPXXaUr_zbHfZgc0NbSBiY59T6zyavvrjd1_lBcqi1ciQ6uSJnA7d46zdeMdHru0oIA4YqbaIgAr07LexaFTri9WmYkQnliZEpSId9_8N7CkyLMLIyaeFxKWKCWopha7c8e88JSXp6RnseoorbKRdksKokZ7Ha5lJrjlbdSkCmuIfBcEP2coHRYU83E7X6YVcVjDkAg7YSKXNRVXDxuzP_hQpCAqD1-H26vNmmeksnAu7L9MHCK_vcJ6x2EgjZcZsOkJ8Boc3VWl65vOOod4bkWxgFHgRRuLTf2fyr_4xMG3XvOHGyEw18II4_O_VoT4Zg-dSYeLHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده در سازمان ملل، مایک والتز: از آنجا که تهران در وضعیت تدافعی قرار دارد، لبنان اکنون بهترین فرصت را در طول عمر من دارد، سوریه در مسیر درستی قرار گرفته است و عراق نیز در مسیر بهتری قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148595" target="_blank">📅 19:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148594">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فایننشال تایمز می‌گوید آمریکا و چین هنوز بر سر تمدید آتش‌بس تجاری به توافق نرسیدند. آمریکا خواستار تمدید این توافق برای ۶ ماه است اما پکن می‌خواهد این توافق برای باقی‌مانده دوره ریاست‌جمهوری دونالد ترامپ در آمریکا تمدید شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148594" target="_blank">📅 19:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148593">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی بریتانیا: گزارشی درباره وقوع حادثه برای یک کشتی حامل گاز طبیعی مایع‌شده (LNG) هنگام خروج از تنگه هرمز دریافت کرده است.
🔴
ناخدای کشتی حامل گاز مایع گزارش داده است که کشتی بر اثر اصابت بقایای یک پرتابه با منشأ نامشخص آسیب دیده است.
🔴
ناخدای کشتی اعلام کرده است که تمام خدمه در سلامت هستند و هیچ‌گونه آثار آلودگی یا پیامد زیست‌محیطی مشاهده نشده است. کشتی نیز به مسیر خود ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/148593" target="_blank">📅 19:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148592">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCQW6hqalwKFm8S1qo4n_6lxRFEl_-N7Jf76A1bX7AYvOPZ0Qm2H7dskzS7Rb2Kc-rsL8_o-w_vg5NbEswzdxUsl32EPA3eTUMRHEUioOKW9T4MkQm2TL1nM67anLiWfZj62BfQD3BMC-lnnNHKtAAbQAXSMQNwZIAtxeSGy6P20_rgHF5W_M_1X2eNn5A9ok4wY8enio1y95PyvYTeAjxV2Tr8TJFu6amOwd5TJMmxpqPIJnbMPckyIPx2oLLcjIN77CcFRt25WBZOokIDzVojuZ__bGQiZo7cdvW1TYv4iBOxy1kSk-uz2LMKIbM0KOoEAjukZ9G3_c9SdWCBpVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال : هر کسی که در زمینه هوش مصنوعی پیروز شود، پیروز خواهد بود! در حال حاضر، ما از چین و سایر کشورها پیشرو هستیم، و من قصد دارم این برتری را حفظ کنم!
🔴
من قصد ندارم رشد چیزی را که از انقلاب صنعتی یا حتی اینترنت بزرگتر خواهد بود، محدود کنم.
🔴
ما با احتیاط عمل خواهیم کرد، و به همین دلیل، ما وزارت دادگستری و سایر نهادهای مجری قانون را داریم که در صورت لزوم، اوضاع را کنترل خواهند کرد، اما من فقط از هوش مصنوعی یا هوش فوق‌العاده (SI) حمایت خواهم کرد!
🔴
پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/148592" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148591">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A80gfNL_EGI5jlyjJxnsBbbCiPlCzP0W9ZpRIYYxLNSdhNodaDfZALqvw6fNPLam8VbObV1drX5Aoi9awt7HWc7zOWe3aRE9Z01bA8l7ZMh_krAkd6pkYy9blULhUrhafLqMSXP-4bRRCbtrq_ded3392JeZTQlK9ehtrEylpjGeouz0hgS_ML5BGmRTwlWVM9By7dAzA_vvYhyv5Y8B-nBNbFX4nwDOUBmf3k2oKiysxxulxrLZDPoKausj1xCMM35xP9LYRAvlndUfaXY9kab3nVefbjK7FvcVWLqaNoQTV0fjAS4nJIvHW_kLUrItc60AzNGDODuTpRuF2leMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عباس عراقچی
:
گروه‌های لابی اسرائیل دیگر از ابراز صراحت در مورد نفوذ خود بر سیاست‌های ایالات متحده در قبال ایران ابایی ندارند. در نشریات متعلق به مریم آدل‌سون، این گروه‌ها اعلام می‌کنند که سیاست‌های آمریکا باید به گونه‌ای باشد که اطمینان حاصل شود اسرائیل در قبال هرگونه اقدامی که علیه آن انجام شود، مجازات دریافت می‌کند.
🔴
وقت آن است که واشنگتن از این محدودیت‌ها رها شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148591" target="_blank">📅 19:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148590">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
الجزیره : دولت عراق طرحی را برای خلع سلاح گروه‌های وابسته به ایران تدوین کرده است که به زودی آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148590" target="_blank">📅 19:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148589">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=MdPDHUs_KwNpJkKUxPJ4s7sL5tPANIo_FCzCH5gFXpNIvcoiM-R9iEux-ZVnWq4p5Xx5RfPCs8hf4R54TyGPyGKlfo09k3TcIwZQNEw9h_f0dKSp79iILSi6cyYpBKpXNV_pGDRbw8YgTVlqrfuMjoYa4kvRxrxK3bHHI3a6FHqaQhytBZp3J2G8Nn2O-rgQfo5UxF9Sk6rMpsWwgKNSCCj0eHqFnXgp5EUyAl1dD1uOLZ9BHPvoSJWRqpK7VuRkIxsf-GTFAoBFu9lVfyOn-QCtJSynmQ9PCY3b7TjtUB5yn0H8ODuOHHBSRm2oNij3OueGbeRH6j3Jh_WXGYqrO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=MdPDHUs_KwNpJkKUxPJ4s7sL5tPANIo_FCzCH5gFXpNIvcoiM-R9iEux-ZVnWq4p5Xx5RfPCs8hf4R54TyGPyGKlfo09k3TcIwZQNEw9h_f0dKSp79iILSi6cyYpBKpXNV_pGDRbw8YgTVlqrfuMjoYa4kvRxrxK3bHHI3a6FHqaQhytBZp3J2G8Nn2O-rgQfo5UxF9Sk6rMpsWwgKNSCCj0eHqFnXgp5EUyAl1dD1uOLZ9BHPvoSJWRqpK7VuRkIxsf-GTFAoBFu9lVfyOn-QCtJSynmQ9PCY3b7TjtUB5yn0H8ODuOHHBSRm2oNij3OueGbeRH6j3Jh_WXGYqrO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جِی. دی. ونس در مورد قیمت بالای بنزین: ما به خوبی از این موضوع آگاه هستیم که به دلیل اقدامات تروریستی رژیم ایران علیه کشتی‌های بین‌المللی، قیمت انرژی افزایش یافته است.
🔴
ما تمام تلاش خود را می‌کنیم تا این قیمت‌ها را کاهش دهیم، اما در عین حال، به مردم آمریکا کمک‌هایی موقت ارائه دهیم.
🔴
یکی از اقداماتی که ترامپ در مورد آن صحبت کرده است، تشویق برخی از ایالت‌ها برای ارائه معافیت‌های مالیاتی برای بنزین به مردم آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148589" target="_blank">📅 19:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148588">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1594857d.mp4?token=csDAc2FSTdLnjWyjtQnf69tNA-YmQ3gm5J06bku05jwne19o6oxBzphZoigB7OLtyZKWdNKOcu5yH0QQ7m2JnpUn0bOePCM9dAbDfx3VpG35R5K6fnb1EhL-_ndLlP7d4ImrSLKfZGsoQ5lNUL5AJipB5ccNPm3sAo78tLr36dAJp_EjDJNzCUOf5CGzgAKjrcVGWmK4RUo3VMZRfUqrqiJjI0wbE6c2XGpCDrGYyYtcbyBEnq-UhLkBLifXZYJEJrpVmmGgoreOy2EQ_5x9o9uKoeB1hE-gIyeR4uEmCRY92FJ4orB3wOORHoJjAdvy3fNPP_Z8fhkkTj6OFqJJFInfn1j_mUcM_3CC_gU89sx9QBeQ91IPYjwxffvc-sGkn9XTPPmW0vXcoHzxaqGWxww-y3WoKJI0TZbcllPFcrT4aWLVMJKVpqea3R_ZLPLXKLOMkstFG8b2EiewlhFi01jrJ24riFoRTuk_Y9FQfZj-LYb7kgIqfHEewW2pgDJ5ernT9uOlpzbDpm95S6A1IrahW1Zh9_eI6-_hLy77IWJSCU00RtP6REt9wv1GN5gLW5v9XlWZaOE4nybznHm_DsLoitOHhmeyo3IJOWGiB5AUYYDJKyJjkUi6jPNolPjOsZe-cTgSjZkOADGJAqZmQJ7X9560ofYcqx78AbxH5OY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1594857d.mp4?token=csDAc2FSTdLnjWyjtQnf69tNA-YmQ3gm5J06bku05jwne19o6oxBzphZoigB7OLtyZKWdNKOcu5yH0QQ7m2JnpUn0bOePCM9dAbDfx3VpG35R5K6fnb1EhL-_ndLlP7d4ImrSLKfZGsoQ5lNUL5AJipB5ccNPm3sAo78tLr36dAJp_EjDJNzCUOf5CGzgAKjrcVGWmK4RUo3VMZRfUqrqiJjI0wbE6c2XGpCDrGYyYtcbyBEnq-UhLkBLifXZYJEJrpVmmGgoreOy2EQ_5x9o9uKoeB1hE-gIyeR4uEmCRY92FJ4orB3wOORHoJjAdvy3fNPP_Z8fhkkTj6OFqJJFInfn1j_mUcM_3CC_gU89sx9QBeQ91IPYjwxffvc-sGkn9XTPPmW0vXcoHzxaqGWxww-y3WoKJI0TZbcllPFcrT4aWLVMJKVpqea3R_ZLPLXKLOMkstFG8b2EiewlhFi01jrJ24riFoRTuk_Y9FQfZj-LYb7kgIqfHEewW2pgDJ5ernT9uOlpzbDpm95S6A1IrahW1Zh9_eI6-_hLy77IWJSCU00RtP6REt9wv1GN5gLW5v9XlWZaOE4nybznHm_DsLoitOHhmeyo3IJOWGiB5AUYYDJKyJjkUi6jPNolPjOsZe-cTgSjZkOADGJAqZmQJ7X9560ofYcqx78AbxH5OY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: چرا در گرینزگاد انتظار می‌رود که ترامپ به پولیتیکو دسترسی ویژه بدهد، در حالی که هیچ‌کس در رسانه‌ها انتظار نداشت که بایدن یا اوباما به بریتبارت دسترسی ویژه بدهند؟
🔴
این مسئله درباره عدالت اساسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/148588" target="_blank">📅 19:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148587">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6125f7658e.mp4?token=ZxZNUfpNvnXKOIxgUHx_lazr720XQ0j2KJ8GiW9Z7yWOwCnymRfF5AT4xv5hVJdnPY-TjadsrnwrJ5z0k9oF2S3aRRLLx2mFABHLPU_mAT6zypEHYFtT8qEkLsKO-kxgjx0xHOYzRUYPBeXOjRw7uu7qvZa9B6Mwo5eB2ZG-vDGD0X3kufhGM3ScDqoOIDiwqKB0LI5IYRKvWX72s-cSs9IgfoB332m1DHUbHl5B2rLiUq_iHJhesv3SBchOE1pNfIJAqU97kjxgKfLiKz3eber7nZ4qwG3R_MnWrPkAEURO1Uqku_oILUxj_4QU38cqL7MFy7hts2-dm7k-mwoZlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6125f7658e.mp4?token=ZxZNUfpNvnXKOIxgUHx_lazr720XQ0j2KJ8GiW9Z7yWOwCnymRfF5AT4xv5hVJdnPY-TjadsrnwrJ5z0k9oF2S3aRRLLx2mFABHLPU_mAT6zypEHYFtT8qEkLsKO-kxgjx0xHOYzRUYPBeXOjRw7uu7qvZa9B6Mwo5eB2ZG-vDGD0X3kufhGM3ScDqoOIDiwqKB0LI5IYRKvWX72s-cSs9IgfoB332m1DHUbHl5B2rLiUq_iHJhesv3SBchOE1pNfIJAqU97kjxgKfLiKz3eber7nZ4qwG3R_MnWrPkAEURO1Uqku_oILUxj_4QU38cqL7MFy7hts2-dm7k-mwoZlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس درباره اوکراین:  آیا فکر می‌کنم جنگ اوکراین در نهایت حل خواهد شد؟ بله. این فقط مسئله زمان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148587" target="_blank">📅 18:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148586">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=M2NbPxrzTFIjmYnirvtEKZZY2oROHoVXY81WM-WtiZZGoa0ITD4hj5LZGAXmhsTtI-2MvW4inaVaZ0e87iPQZrxLubaMt29NGzlB5IwDqfmL4TPVIlSto8RCpIxtF5LRQcMldzOyInId_bISOfmlbX-ddKCRAzJf6YeoBg6mYsF3w_X3p8iTSicZTTYAoClApQgmTYu9iY_4nvM11GwYQ1y3mjxDGSppWmYGQ264MzXsCo3Do2xV4aUqTPk6QmTSTMOvRxI7WxZVENKISRGV1uYfFfufvywW5ncfBbOAW_r05KwM84pl8fJ-YPh_uJcmhyGXCA9PGZ6Z0dYbOJswm2mvmlGq7scitFsDViQkNmn8uyN3Z_aJw4FlLvzRxWJbSQMbsyX4PIc6dKc25AKsXw-OLccZn_Ck_nrCk5BhtB8vPGbAR_3vmWe57-Gln2sphrUMqTcZasSe-K1KmkCjbibZab_sNhBHfOLVvoNEXEKCrcg-6XHOk-F6UU6gMuJaj7rOEsDqo_Fll7NUSJqoiHhvmkJY_7GmWjPigXo8Hv_N7eO7s9FDsI1acZ-iCWWcZdpMY_UprP1RZT6Vp2KfUVWsFlZ95pORJQJ5YgO_nQ3hfMqmOlMgLZ1EHuaqbKPxi7i_DUXDfrPa3Zo1o9UxE-6yY48iC6URm7eSsfjADBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=M2NbPxrzTFIjmYnirvtEKZZY2oROHoVXY81WM-WtiZZGoa0ITD4hj5LZGAXmhsTtI-2MvW4inaVaZ0e87iPQZrxLubaMt29NGzlB5IwDqfmL4TPVIlSto8RCpIxtF5LRQcMldzOyInId_bISOfmlbX-ddKCRAzJf6YeoBg6mYsF3w_X3p8iTSicZTTYAoClApQgmTYu9iY_4nvM11GwYQ1y3mjxDGSppWmYGQ264MzXsCo3Do2xV4aUqTPk6QmTSTMOvRxI7WxZVENKISRGV1uYfFfufvywW5ncfBbOAW_r05KwM84pl8fJ-YPh_uJcmhyGXCA9PGZ6Z0dYbOJswm2mvmlGq7scitFsDViQkNmn8uyN3Z_aJw4FlLvzRxWJbSQMbsyX4PIc6dKc25AKsXw-OLccZn_Ck_nrCk5BhtB8vPGbAR_3vmWe57-Gln2sphrUMqTcZasSe-K1KmkCjbibZab_sNhBHfOLVvoNEXEKCrcg-6XHOk-F6UU6gMuJaj7rOEsDqo_Fll7NUSJqoiHhvmkJY_7GmWjPigXo8Hv_N7eO7s9FDsI1acZ-iCWWcZdpMY_UprP1RZT6Vp2KfUVWsFlZ95pORJQJ5YgO_nQ3hfMqmOlMgLZ1EHuaqbKPxi7i_DUXDfrPa3Zo1o9UxE-6yY48iC6URm7eSsfjADBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: اقدامات ایران علیه کشتیرانی بین‌المللی باعث افزایش قیمت انرژی شده است
🔴
جی‌دی ونس درباره افزایش قیمت بنزین گفت: «کاملاً آگاهیم که به‌دلیل اقدامات ایران علیه کشتیرانی بین‌المللی، قیمت انرژی افزایش یافته است.»
🔴
او افزود: «هر کاری بتوانیم برای کاهش این قیمت‌ها انجام می‌دهیم و در عین حال تلاش می‌کنیم تا در این دوره، فشار بر مردم آمریکا را کاهش دهیم.»
🔴
ونس گفت یکی از پیشنهادهای مطرح‌شده از سوی ترامپ، تشویق ایالت‌ها به کاهش یا تعلیق مالیات بنزین برای کمک به مردم آمریکاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148586" target="_blank">📅 18:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148585">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMaO8NKg1zYSRzI2hsdrfyE4aapDRAZQSp_N33zxvX13rn2X8W4ZDq5DE5pmMbSgcEsKk8SqFzb22g8U8GqXOKy8XcqnFLbS-L_LIIKX9T6JVGDBTK84Gu84nzjHrp2uBJ2MkB8Rq9gAtweiqaTRKc5NmUCetwAg8PBEwIzeu7ee0rGqkEhaoYrrBCCbpwgTQkUKPmIkxB_Y-kD3K2Ao5WX9-aXJvtC0qzvqzbeIYvqu0wKT-__a7-5YcrFIa3YEtya003xcDm-aIiNwUy6Zehp_qshlN-gBa0lV-mSi801CJwgL6QI4LgAuRdnXApBQMjO7ZQmzmpgncwtOfWrl8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: فرمانده سنتکام گزینه‌های حمله به یمن را به ترامپ ارائه کرد اما ترامپ تصمیم گرفت فعلا از حمله به یمن خودداری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148585" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148584">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: ترامپ گفت ایران نباید به سلاح هسته‌ای دست پیدا کند و برای اطمینان از این موضوع اقدام کرد.
🔴
ایران هم در پاسخ، حمل‌ونقل دریایی بین‌المللی را هدف اقدامات خود قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/148584" target="_blank">📅 18:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148583">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f32fb7606.mp4?token=uAcT2zBLdnIoZYpVsZkKhd4Ew0gi8Bsb7NKO9S0TRZJjck_ON7q4juHUsMPMJ6hTiEfKQrE4tBZuHgaKceTOKnZ_8MkExIx2Hrl8ZO23qOT2t9v2DIYEavQU9HhvbuuLhMaSLqnnNFnkOc8FK80BGI2BoEbOW5ceCu5vGsHyjXZF1VwEfzqdqCe1brpxCaznGWqy_6joQ4_U97n-ELUTAXbyP7ksTb4kMWoWHA0eaS5zAq-Wx_syVRbGsQm8bq2YRgISUA2bWpBhS_zKgG3dYHy2rEVQ70sJoilx2VepkpX7ZbnCYt_bSlYchl4pm3qOHPX4Amc3_LXmfJtzaZhHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f32fb7606.mp4?token=uAcT2zBLdnIoZYpVsZkKhd4Ew0gi8Bsb7NKO9S0TRZJjck_ON7q4juHUsMPMJ6hTiEfKQrE4tBZuHgaKceTOKnZ_8MkExIx2Hrl8ZO23qOT2t9v2DIYEavQU9HhvbuuLhMaSLqnnNFnkOc8FK80BGI2BoEbOW5ceCu5vGsHyjXZF1VwEfzqdqCe1brpxCaznGWqy_6joQ4_U97n-ELUTAXbyP7ksTb4kMWoWHA0eaS5zAq-Wx_syVRbGsQm8bq2YRgISUA2bWpBhS_zKgG3dYHy2rEVQ70sJoilx2VepkpX7ZbnCYt_bSlYchl4pm3qOHPX4Amc3_LXmfJtzaZhHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران
:
ترامپ گفت ایران نباید به سلاح هسته‌ای دست پیدا کند و برای اطمینان از این موضوع اقدام کرد.
🔴
ایران هم در پاسخ، حمل‌ونقل دریایی بین‌المللی را هدف اقدامات خود قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148583" target="_blank">📅 18:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148582">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سایت وزارت خارجه آمریکا به طور رسمی هشدار بسته شدن آسمان کل منطقه را صادر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/148582" target="_blank">📅 18:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148581">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c7962a1.mp4?token=OEwmbJumvC0LCh4bQO-is_r5GP0yaot2bzMwtUPuhsL6dZu5rcsKrB5nH_Rmf6nOiU4MEyD97uedX1VarxaYoigeGNpdl72iPjNsXHGbEcLag3yebrMYuY-cPjmtFibqIPJwGkz9SOva_JoZ7TpEUfHXWkhN_FKfW_fTFRGlSuGafD14d-s1hMxyM1_Uz8fZpj5agOvmyBlnYifIRQUXDDZpOQUrPEZQHYjQ_4i9dGLDGthN9aTPFzzMqzcVRuYVdNJaqXYCA8sPICACn6K4cN4DVC3Dw76j1oiXfLKMSOA6JxyQT8n2pzKFcZZQf0nuB7kxIfhb8iVhOMk-bMbwLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c7962a1.mp4?token=OEwmbJumvC0LCh4bQO-is_r5GP0yaot2bzMwtUPuhsL6dZu5rcsKrB5nH_Rmf6nOiU4MEyD97uedX1VarxaYoigeGNpdl72iPjNsXHGbEcLag3yebrMYuY-cPjmtFibqIPJwGkz9SOva_JoZ7TpEUfHXWkhN_FKfW_fTFRGlSuGafD14d-s1hMxyM1_Uz8fZpj5agOvmyBlnYifIRQUXDDZpOQUrPEZQHYjQ_4i9dGLDGthN9aTPFzzMqzcVRuYVdNJaqXYCA8sPICACn6K4cN4DVC3Dw76j1oiXfLKMSOA6JxyQT8n2pzKFcZZQf0nuB7kxIfhb8iVhOMk-bMbwLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده نسل ششم J-36 چین امروز دوباره در پروازهای آزمایشی روزانه مشاهده شد.
این یک هواپیمای استلت بدون دم و سه موتوری بسیار بزرگ است (حدود ۲۲ متر طول، بیش از ۵۰ تن) — تا پنج نمونه اولیه اکنون با تغییرات طراحی قابل مشاهده بین آن‌ها در حال پرواز هستند.
توسعات اخیر شامل یک ماکت ساختاری که در ۱۵ سپتامبر نمایش داده شد و یک سیستم لیزری هوایی با توان حدود ۱۰۰ کیلووات است که در کنار تصاویر J-36 در یک نمایشگاه در پکن به نمایش گذاشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148581" target="_blank">📅 18:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148580">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏
👈
محکومیت سنگین قاتل کودک ۱۱ ساله در مشهد
‏
🔴
جوان ۲۳ ساله‌ای که خردادماه گذشته یک کودک ۱۱ ساله به نام ایلیا را با فریب از یک مرکز بازی رایانه‌ای خارج کرده بود، با حکم شعبه پنجم دادگاه کیفری یک خراسان رضوی به قصاص نفس، اعدام، ۲۰ سال زندان و ۷۴ ضربه شلاق محکوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148580" target="_blank">📅 17:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148579">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f3fc6cfa.mp4?token=hgGI79lzjBRWK4I4mMjLMx6ud44N9wkeImuiGOkoutd80rK17ynCpWx_lJD3uhjknKSO0sGj534HSvjf9SJQCfA-Yc4SpLHMsn49kjqAi-YnFmeTWKIfh3uctTXoGTdtaOdtUcdIlJlGAo1lEELd3B6jVkcgjfvp8PEnF9QXg7AXTuz_s8NfASKpO78uAlxCzynwGWN29B5XCz9O31smynZlhiZH8YnzevCdOD8GexKVYjQQMPVV-7UzHnE-OyPnI8MMYQcI-p7soy9CDkYwBAUp0QbRK8S9aB97B8sWFBb71b0az5djdbRe-b7V_DsmZrN1zfGfGXJeSNqpi9kq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f3fc6cfa.mp4?token=hgGI79lzjBRWK4I4mMjLMx6ud44N9wkeImuiGOkoutd80rK17ynCpWx_lJD3uhjknKSO0sGj534HSvjf9SJQCfA-Yc4SpLHMsn49kjqAi-YnFmeTWKIfh3uctTXoGTdtaOdtUcdIlJlGAo1lEELd3B6jVkcgjfvp8PEnF9QXg7AXTuz_s8NfASKpO78uAlxCzynwGWN29B5XCz9O31smynZlhiZH8YnzevCdOD8GexKVYjQQMPVV-7UzHnE-OyPnI8MMYQcI-p7soy9CDkYwBAUp0QbRK8S9aB97B8sWFBb71b0az5djdbRe-b7V_DsmZrN1zfGfGXJeSNqpi9kq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ظهره‌وند: تست موشکی که سپاه انجام داد اتفاق خاصی بود؛ موشک ایرانی بالای کشتی (آمریکایی) منفجر شد و تأثیرات الکترو مغناطیسی داشت و سیستم آنها را داغون و مجبور به عقب نشینی کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/148579" target="_blank">📅 17:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148578">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دیروز روسای دانشگاه‌های آزاد کشور برای شروع دانشگاه‌ها جلسه داشتن، بعد رئیس دانشگاه آزاد گفت : مهم نیست دانشگاه رو حضوری کنیم یا نه، یکی از دلایلی که دانشجوها همش به ما درخواست میدن میگن دانشگاه‌های آزاد حضوری بشه بخاطر اینه که بیان دختر بازی کنن وگرنه هیچکدومشون علاقه‌ ای به درس خوندن ندارن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148578" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148577">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4e6e2273.mp4?token=ZAw_9IXlFVuozcP1b1ZC4Stg3TOh29S85IbRZ3j4V-_eSBiwzPRoLhMbm0XPqgGmSlT_K8FJrvYMM1eFkgd7H1-qp2oTMQ9yTthCbqD07mqwtmaKGK9rZF6cc6PiMdTASZyx1CW8wQ9yshA7sERBeQjnPZMed6tQQSTnLe6DXZ8xTFTFaeQ9WfB5gxhW9jUaKtpxsdXyreC-T095_AiR6oXrXBRfY41t1Df4K_pZNSuOe3x1kdVVpRNixIZyvHIQUAu7mJ_F9F3mRuo0OKyrh6IxwhQLDKFbsaQGki6bEkYRwHkxJsrNVHQYlE-dtZPO0vtFySwr-8vz4KDIDq776A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4e6e2273.mp4?token=ZAw_9IXlFVuozcP1b1ZC4Stg3TOh29S85IbRZ3j4V-_eSBiwzPRoLhMbm0XPqgGmSlT_K8FJrvYMM1eFkgd7H1-qp2oTMQ9yTthCbqD07mqwtmaKGK9rZF6cc6PiMdTASZyx1CW8wQ9yshA7sERBeQjnPZMed6tQQSTnLe6DXZ8xTFTFaeQ9WfB5gxhW9jUaKtpxsdXyreC-T095_AiR6oXrXBRfY41t1Df4K_pZNSuOe3x1kdVVpRNixIZyvHIQUAu7mJ_F9F3mRuo0OKyrh6IxwhQLDKFbsaQGki6bEkYRwHkxJsrNVHQYlE-dtZPO0vtFySwr-8vz4KDIDq776A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان قبل زدن زنگِ آغاز سال تحصیلی؛ یه استخاره باز کرد که انگار نتیجه خیلی جالب نبود و سَر تکون داد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148577" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148576">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=Q9VKKL_34IO0B2fLWs3sQGxLQ-zj1a4lQdKPGxxyuBwTBnZ3TiHPjuI5PNoJLTJoTo_EntIEI7Hp4Pke3ANCAbu7700HcPyVZU2jv7lAJ4_a0mjcFGyoYOKztxgpO9Oo3Tlc4CCtWlhLWMeqrLICLqvAUrTaxH_KTm8zjEW2wrC6gvUp-SGX84MEZrp1iNZParXikbDgyE0YBebGDQESL0KBE0wvkSH38n1r6cQs5Jsq4QA_mVFeB7xTxQAmmiFDLE5EyA5Ub6snogKepfrR6_ZnBOyyTH-_Cn4t7DlWTQY4_rAMUjfHS9mrDsBZHmGEjRe898e0-mMaSK5vcu6yrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=Q9VKKL_34IO0B2fLWs3sQGxLQ-zj1a4lQdKPGxxyuBwTBnZ3TiHPjuI5PNoJLTJoTo_EntIEI7Hp4Pke3ANCAbu7700HcPyVZU2jv7lAJ4_a0mjcFGyoYOKztxgpO9Oo3Tlc4CCtWlhLWMeqrLICLqvAUrTaxH_KTm8zjEW2wrC6gvUp-SGX84MEZrp1iNZParXikbDgyE0YBebGDQESL0KBE0wvkSH38n1r6cQs5Jsq4QA_mVFeB7xTxQAmmiFDLE5EyA5Ub6snogKepfrR6_ZnBOyyTH-_Cn4t7DlWTQY4_rAMUjfHS9mrDsBZHmGEjRe898e0-mMaSK5vcu6yrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از پس فردا تمام شرکت‌های هواپیمایی ایرانی حق ندارن پرواز خارجی داشته باشن و عملا محاصره هوایی هم انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/148576" target="_blank">📅 17:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148575">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یاشار سلطانی: جماعتی عادت دارند گنج را در خرابه‌ها مردم پیدا کنند.  سؤال من ساده بود:
🔴
ماجرای واگذاری ۸۰ میلیون بشکه نفت به ۴ تریدر چیست؟ این چهار نفر چگونه انتخاب شدند و خط اعتباری با چه مجوزی برایشان ایجاد شد؟
🔴
اگر بنا دارید با کج‌فهمی عمدی از تعبیر «موشک…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148575" target="_blank">📅 17:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3jm0GtJe5aCF7K2oWlj6RFl77AwQSrEL17NZbeSESsytdzhqh_dNXxX5y41Sgn6t692PpC7Xf4pUYXBshEOqEhj2ggMvZ99CRaTsCk6gZbW8Mxr9PF6NZKA0911sQMdgSy0rSocbXZbYOE9CVeY2S20ZklGv1W_JGei2dcs1xj8WhxxFCLNt-RHJ0CiKXpPyuSBmreeyhe7s9t5_vE3zCGHj8ibnNCC4rIZ2kSkJP0Hx7MSP5JHWG0Bdk9gfwSzPVSlJsaMVXspfA_SCC84OIIcMKv27D2lmnixtknCISFkB1H0Q5YnK0xypw7txzDjfpF2LOzkZIxwzsSvAFyDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی:
جماعتی عادت دارند گنج را در خرابه‌ها مردم پیدا کنند.
سؤال من ساده بود:
🔴
ماجرای واگذاری ۸۰ میلیون بشکه نفت به ۴ تریدر چیست؟ این چهار نفر چگونه انتخاب شدند و خط اعتباری با چه مجوزی برایشان ایجاد شد؟
🔴
اگر بنا دارید با کج‌فهمی عمدی از تعبیر «موشک به توافق»، اصل ماجرا را منحرف کنید، از فردا اسناد بیشتری منتشر می‌کنم تا سوءتفاهم‌های ساختگی‌تان کاملاً برطرف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148574" target="_blank">📅 17:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148573">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
بودجه نظامی طالبان در سال جدید حدود ۷میلیارد دلار تخمین زده شده
🔴
بودجه نظامی جمهوری اسلامی زیر ۵میلیارد دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148573" target="_blank">📅 16:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148572">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
پنتاگون ۶ فایل جدید مربوط به اشیای ناشناس پرنده (ufo) را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148572" target="_blank">📅 16:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148571">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d41b639d.mp4?token=iKqyuNIOmOR8pocul9CB6vHXTh1YL3bm8_2nK1TJ51AFKSnj9eRZ19PwxdEW_E9nAh7U0DJdQe9DdLdj5CsiK0hoHF_yTChWkqVxx6oZqkgRtiSXo8FL7sUTMapJy2OXdLb40x8qwL45OUKu2i1HpLWzHVzQOmu7zT4wnBa0Y4ie0QYCqWZgeTX6n0OP4HEDUlEFm07U686ubckQLqcg4TxtoIPoXy5reD8XIAqTmVXX_VMTOzs4ElflUVQUg_EF9sGCUjgW_OTswOrlyjXDe8b-nj58vCo8yfhP1khLwd0XukPU_YOeVvCfY2tKFvekh8hlJ5cP74pboxieDxM-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d41b639d.mp4?token=iKqyuNIOmOR8pocul9CB6vHXTh1YL3bm8_2nK1TJ51AFKSnj9eRZ19PwxdEW_E9nAh7U0DJdQe9DdLdj5CsiK0hoHF_yTChWkqVxx6oZqkgRtiSXo8FL7sUTMapJy2OXdLb40x8qwL45OUKu2i1HpLWzHVzQOmu7zT4wnBa0Y4ie0QYCqWZgeTX6n0OP4HEDUlEFm07U686ubckQLqcg4TxtoIPoXy5reD8XIAqTmVXX_VMTOzs4ElflUVQUg_EF9sGCUjgW_OTswOrlyjXDe8b-nj58vCo8yfhP1khLwd0XukPU_YOeVvCfY2tKFvekh8hlJ5cP74pboxieDxM-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی و پشم ریزون
‼️
🔴
یکی از نوادگان شیخ بهایی بعد ۴۰۰سال اومده از آستان قدس شکایت کرده که شما برداشتید خونه شیخ بهایی رو قاطی حرم کردید و ما رضایت نداریم و خونمون رو پس بدید
🔴
حالا اون خونه کجاست؟ وسط حرم! آستان قدس هم به اون شخص ۹۰میلیارد داده تا رضایت بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148571" target="_blank">📅 16:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148570">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سردار عظیم زاده:مردم تبریک، ظهور امام زمان بخاطر تجمعات شبانه جلو افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/148570" target="_blank">📅 16:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148569">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaGVh9_WCO6uar4_VciT407mnTmU8cNUQaGHuZqYjhDaiGstdMTaYfH9gd3wGSySQDbSJ7LhgNV49w0BjCbgaCVUNmB4fRgxxwDua8HIiTwvsKzhhd-5FS61HHW1_jMpjb4_DREb0-w0FP5gf7tYYyvJzCe78VVYYdLm5r0UQlaP4WYP2cyqQsaaY-MkB6RK0ck4OJPdbVpL761LT7Y7dYslTXVDeDirnynwZ8yThza2mZWl6fYbEs5f9qAd2ihGDe5xdDoMbO70wNWkMW43f_U2FuZElSWiFpF3JJZgyaR0md5NEByHJU02F0Cc4rc30dj9UphbvKPs62IZBuM0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار عظیم زاده:مردم تبریک، ظهور امام زمان بخاطر تجمعات شبانه جلو افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148569" target="_blank">📅 16:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148568">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سریال انفجارهای مشکوک در انبارهای مهمات سوریه
🔴
طی ۳۰ روز گذشته، ۵ مورد انفجار گسترده در انبارهای مهمات و تجهیزات نظامی در مناطق مختلف سوریه به ثبت رسیده که زنگ خطری برای وضعیت امنیتی این مناطق به شمار می‌رود.
🔴
انفجار انبار مهمات در «الضمیر» (حومه دمشق)
🔴
انفجار انبار مهمات در «سرمدا» (حومه ادلب)
🔴
انفجار خودروی حامل مهمات در «بنش» (حومه ادلب)
🔴
انفجار انبار مهمات در منطقه «عیاش» (دیرالزور)
🔴
انفجار انبار مهمات در «العیس» (حومه حلب)
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148568" target="_blank">📅 16:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148567">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گواهینامه رانندگی ۹ برابر گران شد!
🔴
هزینه دریافت گواهینامه رانندگی که در سال ۱۴۰۰ حدود یک میلیون و ۷۵۰ هزار تومان بود، در سال ۱۴۰۵ به حدود ۱۶ میلیون تومان رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148567" target="_blank">📅 16:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148566">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سه رسانه CNN، MS NOW و پولیتیکو اعلام کرده‌اند در واکنش به ممنوعیت ورود خبرنگارانشان به کاخ سفید، علیه دولت دونالد ترامپ شکایت قضایی ثبت می‌کنند.
🔴
این رسانه‌ها می‌گویند تصمیم کاخ سفید حقوق آنها بر اساس متمم اول قانون اساسی آمریکا و آزادی مطبوعات را نقض کرده است. خبرنگاران این سه رسانه پیش‌تر از ورود به کاخ سفید منع و اعتبارنامه‌هایشان نیز لغو یا ضبط شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148566" target="_blank">📅 16:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148565">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوووووووووووووووووووری/ آژیر خطر در شمال اسرائیل به صدا در آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148565" target="_blank">📅 16:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148564">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوووووووووووووووووووری/
آژیر خطر در شمال اسرائیل به صدا در آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148564" target="_blank">📅 16:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148563">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا : چین به‌شدت در حمایت از کارزار علیه ایران مشارکت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148563" target="_blank">📅 16:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d80d29b4a.mp4?token=KOGfBCONNNr_CNZO-iqzYDLKBZ9YmZybqO3gXptXMIhourSLK_0ilnC7DhHAlrEYJs1nIu4J8re2JN-30hZjNRNCVQwMWDTrjPTTdmL6aY-IrHekpcZ1OpJcjkgU8dPvMcYWJE0y64iycURVi39BnaQOYTxn5uZvgoHbEtisaphALDuJluQC2WjhIBvZdOZvkEmpCulSTHhA9K7buDGLNkdJek_Tjt577-NFedRmVD9eOO-ovF_3d7AggXTMuY8oPXJylI-ceXzzvO2AGEx11dvyM89f6G8uymRV8Y_xrJOl-5ib5dCxzjF0JE1LXc9Hzs-Fbo8joK0rMnXBxRDFgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d80d29b4a.mp4?token=KOGfBCONNNr_CNZO-iqzYDLKBZ9YmZybqO3gXptXMIhourSLK_0ilnC7DhHAlrEYJs1nIu4J8re2JN-30hZjNRNCVQwMWDTrjPTTdmL6aY-IrHekpcZ1OpJcjkgU8dPvMcYWJE0y64iycURVi39BnaQOYTxn5uZvgoHbEtisaphALDuJluQC2WjhIBvZdOZvkEmpCulSTHhA9K7buDGLNkdJek_Tjt577-NFedRmVD9eOO-ovF_3d7AggXTMuY8oPXJylI-ceXzzvO2AGEx11dvyM89f6G8uymRV8Y_xrJOl-5ib5dCxzjF0JE1LXc9Hzs-Fbo8joK0rMnXBxRDFgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: فشار می‌آورند و مدام حقوق اضافه می‌کنند از آن طرف تورم بالا می‌رود و حقوق بی‌‎ارزش می‌شود/ به دنبال راهکار هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148562" target="_blank">📅 16:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6179dbe6f.mp4?token=pNSZNpNbT2tmPmys9sEmLsUSkcKTCVWkoTtawcrnjiWh-Cu0X7jsPiuNUkJ5-igx98CeSJeBmRv1IR8t0rWV1DoBRII72asT94ColLUeCNjwSRB3mG0FfhKuEfpb5ORdVlLA26bY1agwTIo2TZJQHTDrPVjppZndq8CWxL8c7opBRcCmzgAEENCeuOYpkmmWDV8gigOak24rsZAYfHesHGixg92oDOYUzYjDsv6JAUu6Ka7xCQJrwbr3CsBtMevZWoKRlUkfU1_gA_cP_r-Ew5dS2FWhwXqitD9CDlVzXCq9oN9o-FMJDTGqLfA7BkAtqOUf3CR9YNKH1y9iIfuOSbAkNwjj-D0L-N4K4LGb0v8tOaMomitjbtCSXb62Tse1bN8V2O9tdpIkNfAPq1gOFnNAhyJ_lTMVLD8_8snEC0qK55zrZNNdrsY6HG8lDpnyn6P7agUXQ4r31qK8CNthdNxUh5UjM1ch4lI5mDBUIcYioYKvf_qXmjxjcVi_z_tzrUUN2gbaBChfwKi30Vrilj5A2oO9YLNOpPGniXmlBm0o-HjvRxs58kdyJwHw_kLz3wOKbtpNaCCZLWfygfxM2YRj4vUJE2IVakqKVm0HHk1xXBZeOUzcqxvAGHQ9ZhWPR5NdifTeCHzGWVWS8K-9oH35GG4ykNZ_f8k3TsdHiNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6179dbe6f.mp4?token=pNSZNpNbT2tmPmys9sEmLsUSkcKTCVWkoTtawcrnjiWh-Cu0X7jsPiuNUkJ5-igx98CeSJeBmRv1IR8t0rWV1DoBRII72asT94ColLUeCNjwSRB3mG0FfhKuEfpb5ORdVlLA26bY1agwTIo2TZJQHTDrPVjppZndq8CWxL8c7opBRcCmzgAEENCeuOYpkmmWDV8gigOak24rsZAYfHesHGixg92oDOYUzYjDsv6JAUu6Ka7xCQJrwbr3CsBtMevZWoKRlUkfU1_gA_cP_r-Ew5dS2FWhwXqitD9CDlVzXCq9oN9o-FMJDTGqLfA7BkAtqOUf3CR9YNKH1y9iIfuOSbAkNwjj-D0L-N4K4LGb0v8tOaMomitjbtCSXb62Tse1bN8V2O9tdpIkNfAPq1gOFnNAhyJ_lTMVLD8_8snEC0qK55zrZNNdrsY6HG8lDpnyn6P7agUXQ4r31qK8CNthdNxUh5UjM1ch4lI5mDBUIcYioYKvf_qXmjxjcVi_z_tzrUUN2gbaBChfwKi30Vrilj5A2oO9YLNOpPGniXmlBm0o-HjvRxs58kdyJwHw_kLz3wOKbtpNaCCZLWfygfxM2YRj4vUJE2IVakqKVm0HHk1xXBZeOUzcqxvAGHQ9ZhWPR5NdifTeCHzGWVWS8K-9oH35GG4ykNZ_f8k3TsdHiNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند: امام زمان برای ظهور به لشکر نیاز داره برای همین ما رفتیم تو لبنان ۵۰تا شهر و روستا ساختیم اما اسرائیل همشو زد داغون کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148561" target="_blank">📅 15:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نفتکشی که امروز در تنگه هرمز هدف «پهپاد» قرار گرفت، با پرچم بریتانیا در حرکت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148560" target="_blank">📅 15:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-8TaZ5Rj6pvbiia-x-FrbsOiz9RaAXMaCZh9UStDGOBufYAZE5wGLn0q6VaJeMOqsCwMoE8-i8Y_VdSmTJXccY0ZWyDRHrI7TCiWPIVb_FU6RBknLr55wZhU54czwgU5b4qBDjPaHlmZtWMK-cPlbGA084rptVKkKusyS8FoHSU1kbtTyaapiqS2Twr7W_aCjlZZTzPvCsBsaacUczmtbX6O21NQqWJ3kSD_H4TMgNZL3hjF55ozKNUqpzF3EsAGYwe-GJE8hwxTQCyyE2JQ9vqISu_FkpCrhXAX8YpBeGfI1Ih3D_K-aeKsTxTilRxO2MlMQXnkaFbUU2ve1BCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:  متاسفانه، روسیه به دلیل جنگش با اوکراین، کنترل صنعت نفت دیزل خود را از دست داده است. تعداد زیادی از پالایشگاه‌های نفت دیزل این کشور منفجر شده‌اند و حداقل به طور موقت، از کار افتاده‌اند.
🔴
این جنگ مضحک و بی‌پایان با اوکراین باید پایان یابد. کل جهان در حال رنج است، زیرا هر ماه حدود ۲۵۰۰۰ نفر، بیشتر آن‌ها سرباز، کشته می‌شوند. چه فاجعه‌ای!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148559" target="_blank">📅 15:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148558">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تمام شرکت‌های هواپیمایی ایرانی از ۲۳ سپتامبر فعالیت خود را در سراسر جهان متوقف خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/148558" target="_blank">📅 15:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پزشکیان: هر دانش‌‎آموز یک لامپ خاموش کند، ۱۵ میلیون لامپ می‌شود. نخواهیم گذاشت چرخ کارخانه‌ها بخوابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148557" target="_blank">📅 15:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCaGVTkljpgjPvnCr47cMtMBidDWNRrzfmb_LmjLX59QZPfEhAm9DgSM-Yka8DGDfioXEJfoh3mr09brohuSqUBYNwpc1FcSTBw_7asRA2uU5qcWixF73UpwY227WW5WkXhY_PpygTutDD4zb7qHYwriKDLfwdQTBwMTR9GRboR8dPdRHBJAzpR2TZLuZHQIdrGoChThe1-2w-wF96hSKaSGrheHdWPlPkjDELeAqbAwyp0rHmP9Bon5D7cakp-fk2FxAeDjcVcHS6MEn7_B2CyrPtCEWJYjAf6lbnRW1amiqnu07LrCReOahHTYkbQsNyBRcvp05npF2f6UUCwCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کاخ سفید قصد حمله به آزادی مطبوعات را ندارد؛ چیزی که من برای آن ارزش زیادی قائلم. هدف ما مقابله با اخبار جعلی است؛ پدیده‌ای که مانند سرطان در سراسر آمریکا گسترش یافته است.
🔴
این جریان فاسد، هدفمند، فراگیر، کاملاً هماهنگ‌شده و خارج از کنترل است. اخبار جعلی تهدیدی برای امنیت ملی ماست و باید همین حالا متوقف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148556" target="_blank">📅 15:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRr-QDU8r0hWU55FE_yYXMpLcL_zg83A6vVnx8_mT8-H8-Ry3-qkDIy9vJ4Z6yIa0Rjq0pvQHDVo6VubdQweNkrGu9EulzH46bpHo9WAkNlG0wOQaVNZ9PmCXJLe9tjlg5ihzDHexnX8URkL54zLn258J7L4wZIfRhM87pRqhRVINQFxof-MYLtiL9J6Y33Na3x49W2Tnkt3mSNREEvEiUrn_woDEzWqX78x8eRKWqNXtrHcYtCH3NXoTur0w4sTSFcpQUokP_HAm5oPzJ_7za8oeFpBJhDyf6pE2pA0iBVfKWXBlHG5YrcJYApr0LFlRtONFYUhIHOzYn8y_jdzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: پاکستان پس از مذاکره با ایران، مجوز عبور امن یک محموله دیگر گاز طبیعی مایع قطر از تنگه هرمز را به دست آورده است
🔴
این نفتکش که اواخر ژوئن از تأسیسات رأس‌لفان قطر بارگیری کرده بود، آخر هفته از تنگه هرمز عبور کرد و طبق داده‌های ردیابی کشتی‌ها قرار است تا سه‌شنبه به پایانه واردات پاکستان برسد
🔴
به گفته منابع آگاه، عبور این کشتی در مذاکرات میان مقام‌های دولتی هماهنگ شده و این دومین محموله قطری در ماه جاری است که با چنین ترتیبی به پاکستان می‌رسد. این محموله می‌تواند بخشی از کمبود انرژی پاکستان را جبران کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148555" target="_blank">📅 15:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
استاد گودرزی: پارسال که نزاشتن پیاده تا آرامگاه کوروش بزرگ برم اما امسال میرم
🔴
هموطن راه در جهان یکیست و آن راه راستیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148554" target="_blank">📅 15:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148553">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">💢
قیمت بیتکوین ترکید</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148553" target="_blank">📅 15:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148552">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
یک کودک ۱۲ ساله بر اثر تیراندازی در مراسم عروسی در چابهار جان باخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148552" target="_blank">📅 15:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148551">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کلیه مدارس استان هرمزگان تا دوماه آینده غیرحضوری شد
🔴
بر اساس مصوبه شورای تأمین استان هرمزگان کلیه مدارس استان هرمزگان تا دوماه آینده به صورت غیرحضوری برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148551" target="_blank">📅 15:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس: احتمال دارد آمریکا جنگی تمام عیار مشابه جنگ ۴۰ روزه با همکاری متحدانش علیه ایران شروع کند اما آنچه میدانیم، این است که روحیه سربازان آنها خوب نیست و ذخایر تسلیحاتی‌شان هم در وضعیت مناسبی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148550" target="_blank">📅 15:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148549">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
قیمت هر گرم طلای ۱۸ عیار 24,255,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148549" target="_blank">📅 15:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148548">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-Zkz2qFtjSEXjXUSsJKXoVcU6Wxq-uuy6qIeqLbvJ4q6kwxVC6Yke0on2njnWMDMx66lc9MhMFC6ZV3GfVy29tbbV7I_VoQDZ3Vc4b9aih_ipbYWYjXxIkwUz3O9deVwGNBM2AebZryFlR09Bw7Vk9a8un_hG4Fs6lJipzu7fF2NKj77Tbd-z1MjHqPdhkdmv6t6ggFVY6pxlXsQdY_vwNtRDy2VWaVKQ2fUPO1sWCIoeF-lW8olF1NiyJQzDTr_3malY8nGJFfSZKnVgM2qq8Z9_JoZQEmpEjQHllowqGQjflzBJvfOoRHQ0T3NvYg--ZQbTvyXjIn1H6sHiUoMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معافیت به خاطر تتو!
🔴
تسنیم نوشته: بیرانوند به دنبال ارجاع پرونده اعزام به خدمت خود به کمیسیون پزشکی با تخصص اعصاب و روان به دلیل خالکوبی روی دستش بوده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148548" target="_blank">📅 15:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148547">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
مرکز آمار: نرخ رشد اقتصادی ۳ ماهه ابتدایی امسال «با نفت» منفی ۱۰.۱ درصد و «بدون نفت» منفی ۴.۶ درصد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148547" target="_blank">📅 15:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
تازه‌ترین داده‌های کپلر که رویترز منتشر کرده نشان می‌دهد در هفته منتهی به ۱۳ سپتامبر، ۲۲ نفتکش که بیشتر آن‌ها ابرنفتکش بودند، با مجموع حدود ۴۲ میلیون بشکه نفت خام از تنگه هرمز خارج شدند.
🔴
عربستان و عراق هرکدام حدود ۴۳ درصد از این حجم را به خود اختصاص داده‌اند؛ نشانه‌ای از ادامه جریان صادرات نفت خلیج فارس با وجود اختلال شدید در تردد دریایی منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148546" target="_blank">📅 14:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148545">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
انتقال سهمیه بنزین به کارت بانکی از مهرماه
🔴
سخنگوی کمیسیون انرژی مجلس از اجرای آزمایشی طرح انتقال سهمیه بنزین به کارت بانکی در پنج استان از ابتدای مهرماه خبر داد و گفت این طرح تا پایان سال به‌تدریج در سراسر کشور اجرا می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148545" target="_blank">📅 14:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148544">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نیشن: احتمال دور جدید حملات آمریکا و اسرائیل علیه ایران پس از انتخابات کنگره
🔴
نشریه نیشن گزارش داد: شماری از کارشناسان از احتمال آماده‌سازی آمریکا و اسرائیل برای آغاز یک عملیات گسترده دیگر خبر داده‌اند؛ عملیاتی که ممکن است پس از انتخابات میان‌دوره‌ای ایالات متحده آغاز شود
🔴
دولت ترامپ نیز به‌تازگی یک بسته تسلیحاتی ۲.۸ میلیارد دلاری برای اسرائیل تصویب کرده است که شامل ۴۰ هزار بمب می‌شود. طبق گزارش، نیمی از این بمب‌ها از نوع ۲ هزار پوندی هستند
🔴
با این حال، نیشن می‌گوید برخی منتقدان و تحلیلگران تردید دارند که با توجه به کاهش ذخایر تسلیحاتی آمریکا، فشار بر نیروی دریایی و محدودیت‌های مربوط به پشتیبانی پایگاه‌های منطقه‌ای، موج دیگری از بمباران‌های متعارف بتواند دستاورد تعیین‌کننده‌ای ایجاد کند
🔴
نویسنده مقاله سپس همین مسئله را نقطه‌ای می‌داند که بحث درباره گزینه هسته‌ای را، از نگاه او، نگران‌کننده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148544" target="_blank">📅 14:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148543">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
اکنون حملات پهپادی ارتش اوکراین به یک پالایشگاه بزرگ روسیه در فاصله 1300 کیلومتر با مرز اوکراین.
🔴
آتش سوزی گسترده و انفجار های مهیب پالایشگاه را در بر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148543" target="_blank">📅 14:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148542">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دبیر شورای اطلاع‌رسانی دولت: اکنون با مسئله گاز مواجه هستیم
🔴
نیاز به همراهی خوب مردم داریم و در این ارتباط باید رسانه‌ها کار کنن و فرهنگ‌سازی انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148542" target="_blank">📅 14:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148541">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFWp1lzqkh1NaLC5YXBRlP1yRsvvScJTb-0lGvGD7rSKTmSt4M4I3VQEdJIhXbpPuKwwKI0USEf2Xksn_tvolx3akz0vQ6Z4sJTj2bi_rZ7HURMX12l7woOm1l3UriJETEKDHPnnUHgmrWOhlN9AsithgJTHyX1IrQTlRyGhqlGG0TLUcD497fWCI6DfMDQZvNmDybpKxCaC_jYvpvdGK5DfsCkQ8hurNhBp9Y7GxOE6bF3lE-wOqBquAwR3qtXHKEoKpMNCrJdCtYfx03BlFvkCuLlBQADjF1xcgjb4oRKNMnD0orOpWOutZp06FHQkHYhm-X-S5z7oruNXduwXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست سردار آزمون در واکنش به دعوت شدنش به تیم ملی: خوشحالی امروزم مثل اولین‌باری است که دعوت شدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148541" target="_blank">📅 14:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148540">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر کشور پاکستان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148540" target="_blank">📅 14:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148539">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
تایلند صدور ویزا واسه ایرانیارو سخت گیرانه و محدود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148539" target="_blank">📅 13:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148538">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع در وزارت کشور پاکستان: محسن نقوی، وزیر کشور عازم پایتخت ایران شده است تا درباره تلاش‌های میانجی‌گرانه و راه‌های پایان دادن به وضعیت بن‌بست گفت‌وگو کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148538" target="_blank">📅 13:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کاخ کرملین: روسیه هیچ اختلاف نظر با کشورهای اروپایی ندارد که بتواند منبع درگیری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148537" target="_blank">📅 13:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOmTzEjvtqxWLz7dQ6w-XwGWFDQjWWO_2sT0oX0Z1pztO53bFfJoGovNMfRmF_Q9cla457GQECsfGCAGo0bcIVyAdIfP9jxRsYITjGaCaoevgZIjTgMY3L4QyKsIvzYnM61vDCYHFdi8CL0eGnGi-KM_hMYP_sLLy047BRYYLLgoNrEIkfoPNutwkED4FkEwnKQvns8R6aUA4AcMZeiYf2lIavSSjXhE2ZAiRB9tNVeCD5AZkulJ3JbjNy765ROJByHIjmlhlhh7fPrUPZ--LrWnmDh6eCa8_gnA7M58Wf4bszXST-Ps7c5My_BXPrY525mNtD7I693Adef9u8A77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شدن ستون دود در شیراز، صدای انفجاری شنیده نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148536" target="_blank">📅 13:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
خبرگزاری فرانسه: آمریکا از صدور ویزا برای تیم رسانه‌ای پزشکیان خودداری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148535" target="_blank">📅 13:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نیروی انتظامی تهران: نه تنها مصرف گل جرمه، کِشت و نگهداری از اونم جرم محسوب میشه و مجازات داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148534" target="_blank">📅 13:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKK-sahhjBNO44spKI6hD4hkqhiGJ7hB6yTfqOpMXDS4daPBsaqra9YZAsKcjMPyiB55rA0gT-eI1bGb5Lg0hoN7gbNfjdf7hpZVuj4xaB37BuV7KgDcNVYZasktcT9Y3Y06TuUQ35IL4kfzkD9xNesNwnUX2gBD_4BRsDrfsHxv5kqI1FPYL7RxmXIpsUDObxkWSX_BK5zo-VTRdmj8EsNdFoE2C1tagbKjbGWXvTdjbI4O_rFmp79MstAp3MUNnhvAFWj-iDjFk1JVTt-TrOKb27VSZPhRRRZbRuzUeKQeMt6AzEgkcA0fgchkdCG5kLrHi29rCzcfL7hZtNSxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از آتش‌سوزی در میدان آرژانتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148533" target="_blank">📅 13:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رویترز: قیمت جهانی طلا طی روز دوشنبه کاهش یافت
🔴
هر اونس فلز زرد با ۰.۵ درصد افت قیمت، به ۴۳۵۴.۳۰ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148532" target="_blank">📅 13:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148531">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزارت خارجه فرانسه اعلام کرد: این کشور پس از تعطیلی مرکز زبان در تهران، اقدامات مناسبی را انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/148531" target="_blank">📅 13:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148530">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6HIUXT0ANTabgiph9oybcd7wRDZ2qCVgnDAqEhvOvDi10AyzXrOhj2flQfR2V_oXUmxdoWzPLtQfEJtlv_WbfgTo7L1-TNbJfc7QXlqUefx3Sqw6unIb6VkvRaCG1kG8cwlax9TiaHz7soi7wwEK4YDzaUDs13W9C24NiMy0PUdBSWwoM9di78tAwphfVksjJ-xO5XbPyxFQSyxL70uqjHVx2egHzWbRtZo4uf_3-fF6ISL8FS6APHOD3qgIswlavrGTTwZ0mVMV2Y4lJXa8Z6TFzlAU8V7Rc_qAb9h4kspatKXgvO4Nf6944p_M3o_BV-gvyZcZcpD5jRm81WlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اداره عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که اطلاعاتی درباره حادثه‌ای مربوط به یک کشتی در حال عبور از تنگه هرمز دریافت کرده است
🔴
ظاهراً یک نفت‌کش متخلف قصد داشته با عبور از تنگه از طریق مسیر موسوم به «گذرگاه عمانی» خود را در امان نگه دارد، اما هدف حملات موشکی سپاه قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148530" target="_blank">📅 13:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148529">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec220c9e50.mp4?token=nC0YM8sBfhr6O1v-gi9Q1CapRdD34ep-bdyjC-Jd0SlQn4kQrL4rPqaU-UEiT61BMWI-Q-W2ZXGlubXfmg4maeWLV8eypg3DpZ75-C9CWqEyD1bw9kjS3giewR9mfp5pJeco8fpYu9zjKdiKvlhkReZ97mFD2mzRqvLrG5IXsEnrbut0QA8WRjtJB8efUghlSXyV51jrPb8p4NBEWWW5dXQJUx8tV4BbZ_j-DKV-uUojHRQ2ONHrmpPHRR-eLKZuMGKUNyS4QsgHjTUADPQSPHlc85tGP2h7SA4i-d_6ILHF-OF2qN9zrnJ79nkxpPn2eYy5HngMpymo26x4ejYjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec220c9e50.mp4?token=nC0YM8sBfhr6O1v-gi9Q1CapRdD34ep-bdyjC-Jd0SlQn4kQrL4rPqaU-UEiT61BMWI-Q-W2ZXGlubXfmg4maeWLV8eypg3DpZ75-C9CWqEyD1bw9kjS3giewR9mfp5pJeco8fpYu9zjKdiKvlhkReZ97mFD2mzRqvLrG5IXsEnrbut0QA8WRjtJB8efUghlSXyV51jrPb8p4NBEWWW5dXQJUx8tV4BbZ_j-DKV-uUojHRQ2ONHrmpPHRR-eLKZuMGKUNyS4QsgHjTUADPQSPHlc85tGP2h7SA4i-d_6ILHF-OF2qN9zrnJ79nkxpPn2eYy5HngMpymo26x4ejYjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرقت موبایل یک پاکبان در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148529" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148528">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بهرام یوسفی فعال اقتصادی نزدیک به دولت : عباس عراقچی پاسخ ایران به نامه ترامپ را در توقف کوتاه دوحه؛به عبدالرحمن آلی ثانی وزیرخارجه قطر  تحویل داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148528" target="_blank">📅 12:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148527">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نخست‌وزیر قطر: از زمان برگزاری جام جهانی دیگر روی آرامش را ندیده‌ام. بعد از آن، هفتم اکتبر اتفاق افتاد و از آن زمان هم هیچ‌کس حاضر نیست به ما فرصتی برای نفس کشیدن بدهد. از همه خواهش می‌کنم که سال ۲۰۲۷ سالی آرام و بدون تنش باشد. لطفاً، ما واقعاً به کمی استراحت نیاز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148527" target="_blank">📅 12:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148526">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/867f2a6745.mp4?token=KK0E6bGudLwdW0idvJf_pfBskTeDdnejOeyy7JoOjx3dUOrGv18cdFLaEe5XiC8E5XD_t4y8A0crxSNPu4bFrtPy3Er0Kvz4bOHkKYvhuvhIEiL7KYSP5pVL4MY1C0PPsLNjFtRwDm8jqIQ3aaYq8Jupm3qFJ-Zqbr2bsyXXSOyeHGlse5rSJgzpfyV2GDq_X9da9lKTqofAeF9DzDIQKCEzRXZuDKpW16Ou76hzF0HXnGIoSsLT8_7GgRR7b6qlLH1gnos_gOzormHsvIwTfxmGcf_2lDCGcYxbpDhSbgA20TQEbjF4Y5lBHWXACy72ISlLiz8LYsveuSDVA3FR8g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/867f2a6745.mp4?token=KK0E6bGudLwdW0idvJf_pfBskTeDdnejOeyy7JoOjx3dUOrGv18cdFLaEe5XiC8E5XD_t4y8A0crxSNPu4bFrtPy3Er0Kvz4bOHkKYvhuvhIEiL7KYSP5pVL4MY1C0PPsLNjFtRwDm8jqIQ3aaYq8Jupm3qFJ-Zqbr2bsyXXSOyeHGlse5rSJgzpfyV2GDq_X9da9lKTqofAeF9DzDIQKCEzRXZuDKpW16Ou76hzF0HXnGIoSsLT8_7GgRR7b6qlLH1gnos_gOzormHsvIwTfxmGcf_2lDCGcYxbpDhSbgA20TQEbjF4Y5lBHWXACy72ISlLiz8LYsveuSDVA3FR8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا صبح امروز یک موشک از داخل ایران شلیک شد؛ مقصد آن مشخص نیست و هنوز روشن نشده که این شلیک
آزمایشی
بوده یا به سمت هدف مشخصی انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/148526" target="_blank">📅 12:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148525">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
جهش غافلگیرکننده بیت کوین به ۸۴ هزار دلار؛ قیمت تومانی سقف جدید زد: حدود ۲۰ میلیارد تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148525" target="_blank">📅 12:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/67d93d944f.mp4?token=RpD7rwskxj3YDL3KZXkbXefqmNlhAjbbIvQrkSN16L13jvnrZHpxjCVEyabCxYCO1E0C-UWndz28pPCozBtO49EWGbjKhdY1K-fkgSlPdvS_N5Njlkbxzp_VPe2N1DCM4CBHOoAVjjv_AsSmV4YjOp2mwABhB9eawvw67a1gYtmAzFuXDbhO3YcypRtnDibLoQw2NzZm0mVG9Gv8Ca6wXt91Saa5S0HRG8QgrfL4fTRs0KABcbjhxSkr3wg5Te-mlGalOm4LwwhILdgMKAe1Raa4ZBNM4OsBI6lgwSu24I5HReWA4LGC_rvlVfl-_YyGuxB3XjdIolXIA_ieibIfyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/67d93d944f.mp4?token=RpD7rwskxj3YDL3KZXkbXefqmNlhAjbbIvQrkSN16L13jvnrZHpxjCVEyabCxYCO1E0C-UWndz28pPCozBtO49EWGbjKhdY1K-fkgSlPdvS_N5Njlkbxzp_VPe2N1DCM4CBHOoAVjjv_AsSmV4YjOp2mwABhB9eawvw67a1gYtmAzFuXDbhO3YcypRtnDibLoQw2NzZm0mVG9Gv8Ca6wXt91Saa5S0HRG8QgrfL4fTRs0KABcbjhxSkr3wg5Te-mlGalOm4LwwhILdgMKAe1Raa4ZBNM4OsBI6lgwSu24I5HReWA4LGC_rvlVfl-_YyGuxB3XjdIolXIA_ieibIfyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارهای مجددی در داخل یک انبار مهمات در منطقه
العیس
در حومه استان حلب سوریه رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148524" target="_blank">📅 12:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💢
قیمت بیتکوین ترکید</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148523" target="_blank">📅 12:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148521">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLR7TuNQtREIiYQmyDWFSBMXpu4FTk_wPBpxMpOrcVuDLD-hjnr3Yr61iwDBOAMWwdG0s6KKIHevkRjG2BsiWnOFmIuTUXi8p_I-4z9XA0nt6tKaYIgCECLzKrMpU5a7nY4iC5j4M5dLrl6aY-VeT3qhobP66QHda1qkk1ptydaegD9YGOuLbaVl68exPotKydxo8Y6I57oJegVWZGo5ZDQn9eUDtzFXbhBK3h8-DhsIRM4B7mrBm79fMpVD7QTen5i2pb5eQsM-IjgXk5UbeBcUkikYtRtzR18qX8dTDSFKnH1JcE_3_3oEsz9AYs-ApiCSLb2ggMXIXy8u4CtIsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-hD5TBLu_kpnvzEq82ozP8HzHrANspog_0pOzjUq6jAVymjfWoJg9vTbYXdyOHXDrPAYKTMo0hOeCt7crTs6pH59wWUKWChMwqbbPMrGnueuJI4RUcjdet1Oj2GGsCNixqm-fEZwmBbhfr4J_y6Q-6DnE8Y4om820N8oLjJeU6_MScGLcPPunKoCT4kx92rxATW4_OlaG_ixBdUrytc908lTuCVOnJ_w4DtC3frMRNp0cE3tgp4w2lqQ-OD4jQCJ5NmtB8ZhrBZDi7cFf98KeE1owsT8RqNtcIPqQcue61pPos4XDFpa5fQacIZkT9av_6_CTIsiQwbxS5J9sn9nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای مدل A330MRTT متعلق به عربستان سعودی و یک پهپاد، پس از انجام ماموریت‌هایی در نزدیکی مرزهای یمن، به پایگاه هوایی ملک فهد در طائف بازگشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148521" target="_blank">📅 12:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148520">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
اکسیوس به نقل از منابع: در جریان تماس ترامپ و زلنسکی، رئیس‌جمهور آمریکا بار‌ها از همتای اوکراینی خود خواست حملات به پالایشگاه‌های نفت روسیه را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148520" target="_blank">📅 12:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148519">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کارشناس صداسیما: مردم میگن اگه اقتصاد هم در اثر حمله دشمن نابود بشه ذره‌ای دست از نظام و کشور برنمیداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148519" target="_blank">📅 12:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148518">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMvMfCdYN3gERMBpbrsrt57VPjyIIragTALrsB1-hZ00h5-sncvItJdqe2UbYyhVWrEu8dUngDP5uAikmUONtHCv673X7EBzCkenFU3y5NXFv1H96MVp3Aw9YooN72oGEVVd3bd_LPjan1Rh_hY5W6ua17uckFNbmFkYOKZkp6d9UpzmxURCLUi28egp8dhD6Eu2Z5v171Aw3sBxQfa4qQEN_vg6gZlqZjnj897vBbeOfuXQ4XuZt81x6Jo_XysHqLIueSBa5KEwj-uKhTy7GfLlHPbsSi3IKhBJrPgqN7sO2Hj1-EYlDdKaAx-ILuUcs-nw_YJc5ZjXP2GxZf3pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس: ایالات متحده به عنوان بزرگترین تولیدکننده نفت و بنزین جهان هم، قیمت‌های سرسام‌آوری را تجربه می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148518" target="_blank">📅 12:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148517">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سخنگوی حماس: آمریکا با صادر نکردن روادید، مانع حضور هیئت فلسطینی در نشست مجمع عمومی سازمان ملل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148517" target="_blank">📅 11:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148516">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پزشکیان فردا به نیویورک می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148516" target="_blank">📅 11:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148515">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نیروهای یمنی(حوثی ها) موشک‌هایی را به سمت مواضع نیروهای همسو با عربستان سعودی شلیک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148515" target="_blank">📅 11:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148514">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نخست وزیر قطر: ایالات متحده همیشه متحد استراتژیک ما خواهد بود و این چیزی است که من مدام تکرار می‌کنم.
🔴
ما معتقدیم که اتحاد ما مستحکم است و هیچ چیز نمی‌تواند آن را از بین ببرد
🔴
تجهیزات ما آمریکایی است و ما به آموزش‌های مشترک خود ادامه می‌دهیم
🔴
ما به داشتن رابطه قوی با ایالات متحده و ارتش ایالات متحده ادامه خواهیم داد. و البته، این یک همکاری دو طرفه است. هرگز یک همکاری یک طرفه نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148514" target="_blank">📅 11:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148513">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سناتور جان کندی در مورد ایران:
فکر می‌کنم حدود شش ماه دیگر از آنجا خارج شویم. بعد از آن نفت ارزان خواهد شد و تورم در آمریکا کاهش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/148513" target="_blank">📅 11:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148512">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f645472.mp4?token=DkGecBkSBHBev8oSDycBWktCyRmONGDGCo8zR5jKj2lIyIyz8QhbTXPQMQOwcjf6e6wubeW77DU-czNqR1RSuaflgZ3cDNT8w9HPQ8boj6JJdOJ0nrVJc2kEkymdIVvP720YDF-uaNPXnfTMwtln7bX-oowzjRZBryEIf-2NmFXhYAvkvxUioSgLXUdVvmUQrowOQb3swyGoi02ZoMcAVBb1ZSZiwfEGwUPmYRc-jmlNyrciXGyPstzXvOnio1Yw_81jTswJ5gpI9yy8CGnrp33Y1PJNvOHkJ79jkTxzXqXADcJiv2jjLmyiXESkO6resV-WjjlL_tK6W1IUzwNM9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f645472.mp4?token=DkGecBkSBHBev8oSDycBWktCyRmONGDGCo8zR5jKj2lIyIyz8QhbTXPQMQOwcjf6e6wubeW77DU-czNqR1RSuaflgZ3cDNT8w9HPQ8boj6JJdOJ0nrVJc2kEkymdIVvP720YDF-uaNPXnfTMwtln7bX-oowzjRZBryEIf-2NmFXhYAvkvxUioSgLXUdVvmUQrowOQb3swyGoi02ZoMcAVBb1ZSZiwfEGwUPmYRc-jmlNyrciXGyPstzXvOnio1Yw_81jTswJ5gpI9yy8CGnrp33Y1PJNvOHkJ79jkTxzXqXADcJiv2jjLmyiXESkO6resV-WjjlL_tK6W1IUzwNM9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان کیریاکو، تحلیلگر سابق سیا:  اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت!!
🔴
صدها هزار پناهنده افغان در ایران هستند و هرگز تابعیت ایران را نخواهند گرفت.ناامیدند و اسرائیلی‌ها همین افراد را استخدام کرده‌اند.
🔴
این‌طور بود: «در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار. اسرائیل هزاران نفر از این افراد را استخدام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/148512" target="_blank">📅 11:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148511">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148511" target="_blank">📅 11:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148510">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e412d99b5.mp4?token=HgkPuFilm9iChSb2Vp3vpIqHNsNchrBaT786Tke9IdA0XIlB3l6G46YpHsShZhKeUbePq11eWxdghU0sJFKoGNAJ_7ObvICJQmW8wapKeAgzOysMBgt24jhdloOyBg4bA0xblBHCxMSfDkQX1XKLr3TlCUQpt1IUHv6_FoS1TCqybIKlHCg3XJMZN87ObCdiU1cfqzgZIDzu8F9HmgEY9r2bSX-x7aTxY7X7BCWgMoEUAcam4T04eFOY-jR79g_Jj9Yn-6Zjc4OvECFWCRCSEXlCiedJyoEJz1ZXq1xBRKLKPJG5XaLJDhVUHj0pJMWEJ2y2_YVHM5Q-vQEeOVsb-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e412d99b5.mp4?token=HgkPuFilm9iChSb2Vp3vpIqHNsNchrBaT786Tke9IdA0XIlB3l6G46YpHsShZhKeUbePq11eWxdghU0sJFKoGNAJ_7ObvICJQmW8wapKeAgzOysMBgt24jhdloOyBg4bA0xblBHCxMSfDkQX1XKLr3TlCUQpt1IUHv6_FoS1TCqybIKlHCg3XJMZN87ObCdiU1cfqzgZIDzu8F9HmgEY9r2bSX-x7aTxY7X7BCWgMoEUAcam4T04eFOY-jR79g_Jj9Yn-6Zjc4OvECFWCRCSEXlCiedJyoEJz1ZXq1xBRKLKPJG5XaLJDhVUHj0pJMWEJ2y2_YVHM5Q-vQEeOVsb-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما قیمت کوکائین را اعلام کرد!
🔴
کیلویی ده میلیارد تومن!
🔴
پلیس مواد مخدر تهران بزرگ ، یک بار بزرگ کوکایین کلمبیایی را قبل از پخش در پایتخت ، کشف کرد
🔴
این کوکایین‌ها بیش از ۵۵۰ میلیارد تومان ارزش گذاری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148510" target="_blank">📅 11:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148509">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یک آخوند عوضی کثافت: با دختر رضا رشیدپور تحریک میشم، رشیدپور قیمت دخترت چنده ببرمش؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148509" target="_blank">📅 11:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148508">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14f346d3d.mp4?token=qKA66gzL0H6jyUB-XkK8s5jcNFJ1-I303nvduOJcUsWt5HwEdLtqrohYEAJZleZbPgg-OX_GzgYSIetq9BzR_Dy5KrXPZXNAUB3QtSMqKUWLEH5jKd0M3lg0UlfMPUQZJpkABKlorC4mnKQWUIMN4sHoVk1GPbXQx-h_umz-hOxVL9lkDIMnI1gu1lIM5JpeAUtC81N-vVuErbFJDXD7hKH15RTq2DGbLD6_CgIq7kx-GPLAmavZpX0Ti62rBn9dHslmCkrKg0g4LQujLJOaHFVcgCu81pVp3YwkJ7uVBX0R9aSm31OaYIjdzpKS6ePrZcSOCJpk25Ct8hVjearknw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14f346d3d.mp4?token=qKA66gzL0H6jyUB-XkK8s5jcNFJ1-I303nvduOJcUsWt5HwEdLtqrohYEAJZleZbPgg-OX_GzgYSIetq9BzR_Dy5KrXPZXNAUB3QtSMqKUWLEH5jKd0M3lg0UlfMPUQZJpkABKlorC4mnKQWUIMN4sHoVk1GPbXQx-h_umz-hOxVL9lkDIMnI1gu1lIM5JpeAUtC81N-vVuErbFJDXD7hKH15RTq2DGbLD6_CgIq7kx-GPLAmavZpX0Ti62rBn9dHslmCkrKg0g4LQujLJOaHFVcgCu81pVp3YwkJ7uVBX0R9aSm31OaYIjdzpKS6ePrZcSOCJpk25Ct8hVjearknw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند عوضی کثافت: با دختر رضا رشیدپور تحریک میشم، رشیدپور قیمت دخترت چنده ببرمش؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148508" target="_blank">📅 11:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148507">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKYloxcALKL8UPwx6fg-MsmmQx1dTOAAjRXbPChkf63Lhn_BbCh7H8l2ODpevJ9ySV6V7DAYJrp2uj6j5tBIljK-zWO5qGfOhh3Gf7mO5GKxe6-LEZf4xAC-_L_tSKM8snixN-jpkB7CfJsJ9DBomhj5YntXUV3kxbdg04k9Bn5Mc_n6_aMJoSqcdzcmgcBukPW39c_zRLRfht4yoU7m2lRBnhOHXxJ6XNBuw3zZulhpdMIi9hNw8EHmjmWp5bPEfP18nuutw6x93drxK5lc664uScwFKO3tjDacj-NNrELRYvK8rf8390eCAeZG6IBxKqXaGMsNNQrzOJTVyFf4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استاد گودرزی: پارسال که نزاشتن پیاده تا آرامگاه کوروش بزرگ برم اما امسال میرم
🔴
هموطن راه در جهان یکیست و آن راه راستیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148507" target="_blank">📅 11:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148506">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c35e79706.mp4?token=f7dxt1CNzZ74NsvFwa0uNO6g61wxhzDvRVPktv0gLlwENCTQgGrB8dTrgsspgVDDpyWXYJELIS6P52WoFE0UqcfaxjWKZvA3aNVEFDmt5Tdg6abXphmZuzS7CH9kpUP7uF3AedLDodEoTkqZZqf3sPewBNLPjID-zF3Kn5Ww2HFmIgDvQ2BtbL6hDLh3_r4yfWfTggjmsld6q-vILLIbFg_mUCQES52PfGxNX3Ddm1YbpqzsaMWKmPs6yc2JPByXbbdmvzRZAIZ3VjwA3qgDMR-dhu0zHtDDTE8yEJ5LURKMcEHtEoJoqrbAbfjmhCV2vLPstJSn8dHTtvR1xf7BL4CrAGuNi9WtMhG2GRC7PmfFWdPDP8rBTB0jVEkk8IqQt1c1Skap7aZzkIRzAOWujDmibGbQnfrrrR3bKcSwpao4GQvT2pYhgPK7_5eWjcz8XS9g4GRG1FtRDINXCU8Y8qrK1YnFceIVJTrboc3uAfq9_wEUcACCiVVQmxI9z-xsqPSvHpdI1YeCng6FlbMzGndMwbRcHdDX3VGKH5uqUkS_Yn8kztNEEKfM-qctHzBt2Ws04JwfO5c5zPU_-EEKiFN0z4uWp1Lz2tZIekOG8Hd_M5oJb_ioXYwR6EHzXD1HJDcoHuteWLasN7aVsW8pP6aM3dxXGYnmODYoLUGJlAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c35e79706.mp4?token=f7dxt1CNzZ74NsvFwa0uNO6g61wxhzDvRVPktv0gLlwENCTQgGrB8dTrgsspgVDDpyWXYJELIS6P52WoFE0UqcfaxjWKZvA3aNVEFDmt5Tdg6abXphmZuzS7CH9kpUP7uF3AedLDodEoTkqZZqf3sPewBNLPjID-zF3Kn5Ww2HFmIgDvQ2BtbL6hDLh3_r4yfWfTggjmsld6q-vILLIbFg_mUCQES52PfGxNX3Ddm1YbpqzsaMWKmPs6yc2JPByXbbdmvzRZAIZ3VjwA3qgDMR-dhu0zHtDDTE8yEJ5LURKMcEHtEoJoqrbAbfjmhCV2vLPstJSn8dHTtvR1xf7BL4CrAGuNi9WtMhG2GRC7PmfFWdPDP8rBTB0jVEkk8IqQt1c1Skap7aZzkIRzAOWujDmibGbQnfrrrR3bKcSwpao4GQvT2pYhgPK7_5eWjcz8XS9g4GRG1FtRDINXCU8Y8qrK1YnFceIVJTrboc3uAfq9_wEUcACCiVVQmxI9z-xsqPSvHpdI1YeCng6FlbMzGndMwbRcHdDX3VGKH5uqUkS_Yn8kztNEEKfM-qctHzBt2Ws04JwfO5c5zPU_-EEKiFN0z4uWp1Lz2tZIekOG8Hd_M5oJb_ioXYwR6EHzXD1HJDcoHuteWLasN7aVsW8pP6aM3dxXGYnmODYoLUGJlAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخ مبهم مدیرعامل توانیر به احتمال خاموشی برنامه‌ریزی‌شده در زمستان: امیدواریم بتوانیم مدیریت کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148506" target="_blank">📅 11:10 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
