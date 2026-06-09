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
<img src="https://cdn4.telesco.pe/file/t_lD_O9vtDOjG8xFisZ-Zi4gbfTCblaJ6Fi9AnO-jDVbp41P-ahX7ZFCsWHxa6SPcq5eFQ0FIuoMfQ_9okzyTw0KdM6NLJvLNExhWVmVR-wFeEg1bqiQoy8FlkQTFFnvDTJZs5tcJeGY8VRQ3w2g06yJ0N52qeukL4eUXIZhTD6XoawNCGJKfxPPt6cY3ipeGSn_2QOCVeXUbTSWWVv9TmfD7l5MueIsGGt2AFoGHN0M_c2Pf4s8kBVU9aXRGVqBMlEp0u7jrycyDhrkDP74WtsSSbZAD3Y2_PFnub2SneWrvF3Eu1XgURznkpVByGaP8RCnF6D6tgDVW_AivWz5QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 10:00:44</div>
<hr>

<div class="tg-post" id="msg-126436">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فارس: تجهیزات هدایت و پشتیبانی جنگنده‌های اسرائیلی در جنگل‌های تنکابن کشف شد
🔴
خبرگزاری فارس گزارش داد مجموعه‌ای از تجهیزات فنی و سامانه‌های زمین‌پایه که گفته می‌شود برای پشتیبانی و هدایت جنگنده‌های مهاجم مورد استفاده قرار می‌گرفته، در ارتفاعات جنگلی شهرستان تنکابن در استان مازندران کشف و جمع‌آوری شده است.
🔴
بر اساس این گزارش، این تجهیزات در یکی از مسیرهای اصلی ورود جنگنده‌ها به حریم هوایی تهران مستقر بوده‌اند.
🔴
فارس مدعی شده منطقه مورد نظر در جریان «جنگ رمضان» یکی از کریدورهای اصلی ورود جنگنده‌های اسرائیلی برای اجرای حملات علیه تهران و مناطق شمالی کشور محسوب می‌شده است.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/alonews/126436" target="_blank">📅 10:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a89527e91.mp4?token=WYwuVRPH2v6B2z7jY9--W1Vu1aMkw96lYPbruB4ekwsZVojV16CrAKFG-U4TFjIicM_GLyj68071uSk7Hjh_RWxasPBMdIWL6bTV01q443IzM1skAOvVV5SfV1KhY_g0_edIgIOPy1tpExmXSS4E82qBXpQ91xDZ7tPesBuG28qnAnbQ1s6eqBaRkot1eUxZI24oZ5TTI_UbO-FKpkj4_dQFxdFP_B3rJu3fUrn2Fedayv7IgtqEPe7m_el82jVqHaq2z4OIKOrXGuLZsDWjqtdY5-ZxKWY0aUV3jIHAmM5CwUEXStWvwnSBNpfrmfXIboB7PyUSmLEjAFGDwRdefw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a89527e91.mp4?token=WYwuVRPH2v6B2z7jY9--W1Vu1aMkw96lYPbruB4ekwsZVojV16CrAKFG-U4TFjIicM_GLyj68071uSk7Hjh_RWxasPBMdIWL6bTV01q443IzM1skAOvVV5SfV1KhY_g0_edIgIOPy1tpExmXSS4E82qBXpQ91xDZ7tPesBuG28qnAnbQ1s6eqBaRkot1eUxZI24oZ5TTI_UbO-FKpkj4_dQFxdFP_B3rJu3fUrn2Fedayv7IgtqEPe7m_el82jVqHaq2z4OIKOrXGuLZsDWjqtdY5-ZxKWY0aUV3jIHAmM5CwUEXStWvwnSBNpfrmfXIboB7PyUSmLEjAFGDwRdefw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض مادر خانواده پرجمعیت با ۱۰تا بچه به مبلغ کالابرگش: ۱۲ ميليون فقط پول شوینده‌هامون میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/126435" target="_blank">📅 09:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4wZACb44MSFbVUqxFUtLo_wnBOgrebp-FPfyuyjGnS0IBJaNkDtIFckSsrFBa8CcMvNNZxlZqKdEUxmueBX2VSqNV8itmR1Fei98X0YTyAb0WglLmEu3UWtkfNjxEzCjI5h00AIKmK6mYQSv7bDpATMiXgQ2FUtxJ7b0boIBZ1uPDjWhAHTPeZ-zihv5LBrWf1xuoqWeVgxwygil4I44mQb2bAijhbvomGAYlhj8IVe_zlQ1__l7Gxg55Kez_Ds5DuIXuanqu8p08JQXdmFkImSNaLd-bmwrJePIFt2FXiwtO5bXAE8DS2078fTpArYFvQhFbUYxMnL8NmtxQtP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر جلد نشریه آلمانی اشپیگل:
ترامپ، خراب‌کننده‌ی جام‌جهانی
چگونه دونالد ترامپ از جام جهانی فوتبال سوءاستفاده می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/alonews/126434" target="_blank">📅 09:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126433">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teLkdZLBpcqqX3IfdIpjqe_uZF5pSk6MDgnPD1sB3aCgn5xr-c1tnzispX-_DOayRyLZl_XWtf6ssDbwQGhqZaCOoZhOKGvWLHsRk9eBZ-nMTOYr5IA3pO18FNeDWjygHoHiGy__kud6OE15YKrnJ3o9RXBWEJDMijZeKAUZymQ5VUcJL_T3e_3q_ahCAavL2B7xjtTfkmlDUQ3Zpa_feUzpVEfI2Ipq0MUKlht2y6x8NsVBfdGCsSRC1vfJoh4vY9GpfGl0sUqN__DUno7-4_r69YPHNPbQCf0O135cGQZTLPaKCUdclDy9vCGA7wx3IvRmxAutidzc9vV5dg3fUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخیره هسته‌ای فرانسه از ۲۹۰ کلاهک در سال ۲۰۲۵ به ۳۷۰ کلاهک در سال ۲۰۲۶ افزایش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/126433" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126432">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5QGCea6rAkiCWeWfgQjS5_h-WywY0uGiJLCzeeRxsR5Y6mGD3nGDYENkGBot57zVO9DyWguYQaryTh4lpFvwuPpZnrCep2oJmILc8B5tF0bwVf_1-hU5SOPn3amTldbCquMJhUFaHypOMZ80NSuOAE0JQmP02a0e31fyAX2m9swlS7R2r9C1hI8BsvXv8ve9u7hD4t2Mjf0nPlzGy1u4tD4lXp2jkjvaLOwgGq-ZRof5UlhqhwpCrkgRx7CrpP73IW46zQ5-g3TOHdVolOnkw2FjYBAwSOrpdwatMI9g8Ywqd8EWCeWW0VrTMSX08pO7vsSkl-4OjypajmKgn9tXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: همه ما در قبال حفاظت از محیط زیست مسئولیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/alonews/126432" target="_blank">📅 09:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126431">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=k2prF7LIcErFCyy8uYM0oPoxEoQlHTdYPKlapvjxOYHfyhKuvgC-k5z7y00nNCciApTF1d96LlRrZl-mtZj3L0Yikn4Osa_mjz6KE1Es7pOQ9O6Om9ySDI2lmYEb8oMRZ8krJRqLtB9C8C1v5uLxoLGfIs8W2wr3AkHcYhfb4o2bQCVERy4ExfmuBvyQP0gCZnBfVo8XFw3xMMDixvHGPUeOzG1FOjc38pBeRlfO3E59LkwDokKKsfnr4INxtod6noHImX7W9N987u1H1cPrRlzQ16DWm3vFkpGslxT1nQ977u8Y-JuwWxGw2uxcOyrU-6wUZFWqeqETDeihsxQpkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=k2prF7LIcErFCyy8uYM0oPoxEoQlHTdYPKlapvjxOYHfyhKuvgC-k5z7y00nNCciApTF1d96LlRrZl-mtZj3L0Yikn4Osa_mjz6KE1Es7pOQ9O6Om9ySDI2lmYEb8oMRZ8krJRqLtB9C8C1v5uLxoLGfIs8W2wr3AkHcYhfb4o2bQCVERy4ExfmuBvyQP0gCZnBfVo8XFw3xMMDixvHGPUeOzG1FOjc38pBeRlfO3E59LkwDokKKsfnr4INxtod6noHImX7W9N987u1H1cPrRlzQ16DWm3vFkpGslxT1nQ977u8Y-JuwWxGw2uxcOyrU-6wUZFWqeqETDeihsxQpkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا ظرف دو هفته آینده «پیروزی کامل» بر ایران را اعلام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/alonews/126431" target="_blank">📅 09:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126430">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad6e09e52.mp4?token=recvB2L5NQqLDp7bWFGtakC2bIoVe52kNt1eIYtIIvogRD6y08A4xQkjRQ4ZvrtRux5jiTWL6Mkjj2L7PLw-XrqyHWacFym3TuEUK8bCsY81oxZM2Q04qxS-dMA_2SZbX6pZumgRdx3jv2jzeMQ5SRbRzPuE0fRCsbBpSGF8_Fp98AdEwu66kryua9yuKnO7Tn9MeT8wh02DHkRSS8GoHhKU0i_CgaABjA-W_BHKi5Q0v9YsWqhXyUWEHKHEqXDzAQQ-rs1q1hzQqrH89tvYGNPWVTf-4Nme7eBTiSQ9xvj459KbpCtJaJpvzewA9QeiZZMuVMO3zuJ3-qAYNQqzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad6e09e52.mp4?token=recvB2L5NQqLDp7bWFGtakC2bIoVe52kNt1eIYtIIvogRD6y08A4xQkjRQ4ZvrtRux5jiTWL6Mkjj2L7PLw-XrqyHWacFym3TuEUK8bCsY81oxZM2Q04qxS-dMA_2SZbX6pZumgRdx3jv2jzeMQ5SRbRzPuE0fRCsbBpSGF8_Fp98AdEwu66kryua9yuKnO7Tn9MeT8wh02DHkRSS8GoHhKU0i_CgaABjA-W_BHKi5Q0v9YsWqhXyUWEHKHEqXDzAQQ-rs1q1hzQqrH89tvYGNPWVTf-4Nme7eBTiSQ9xvj459KbpCtJaJpvzewA9QeiZZMuVMO3zuJ3-qAYNQqzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا از نتانیاهو خواستید که علیه ایران تلافی نکند؟
🔴
ترامپ: "نه. من گفتم کاری را که درست است انجام دهید، اما می‌خواهم هر چه سریع‌تر دست از این کار بردارید. چون آنها باید دست از این کار بردارند، این به لبنان مربوط می‌شود و باید دست از این کار بردارند، ما می‌خواهیم این کار تمام شود."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/alonews/126430" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126429">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
غریب‌آبادی، معاون عراقچی: شورای اتحادیه اروپا در یک اقدام مزورانه، به اصطلاح تحریم هایی را علیه برخی افراد و نهادهای ایرانی در ارتباط با تنگه هرمز تصویب کرد. هیچ ارزشی برای تحریم‌های اتحادیه اروپا قائل نیستیم.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/126429" target="_blank">📅 09:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126428">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
رئیس پارلمان لبنان: ما خواستار آتش‌بس کامل هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/126428" target="_blank">📅 09:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126427">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل: هنوز به متن نهایی برای توافق دست نیافته‌ایم/ ایران و آمریکا در حال پیگیری و تبادل دیدگاه‌ها و نظرات جهت رسیدن به این متن هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/126427" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126426">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSQm1qoUQMjn9jlYKC9SfDMHAMbBPL4N3P0j2YN7XpOGhqOUr7xEuryXBX3kAelnlWXPA6A55EfAivHzIXBCbpVgj1lj4yHSsZKXrGv9OyneLMeKbQRGIjGZKh2OMmzP4FJ2MCuTiJp10D2ktUwkzDpKVtfjyaOI5M1kXa58ypzcHx1-R4l2T1PID7V2iUqunE_X_c82UsEzzUGMj3n4IXR4moB6sNTPc2O9lstHF2OWEEZPaVU0fgMM0Blq8y1ipgyHXdCxqm0pVB_Rs43JhcllFkbCxyXmBOt3NVt3rKPLWrEN57sHzzHxSQQQC7KKPzXVdC-_K3LGXynwVpI21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون رئیس جمهور امریکا، با تأکید بر اولویت منافع ملی ایالات متحده، اعلام کرد: واشنگتن به دنبال دستیابی به یک حل و فصل پایدار و طولانی‌مدت در موضوع هسته‌ای ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/126426" target="_blank">📅 09:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126425">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/017bc45150.mp4?token=Ao6gtOga4Mx3UsVaNNYCPzOw7bqO48yPd4-bhYAnLwDvXr8z6TVNjcQro3tVTcLrXlA6WW5VtuP97GJSw8LSlagLLVCxYM81LL-gnBMOH0P0AynI6WrMkpVJFO5lPTYF68YtWhYmwCvOMc-iKRHrJAlM233nF4d56jCNt82L810sk7wtAO_GPHslnH-tYYP5_mwZ_7IgBN27irtH8__Yq3zSD6sKlUQMialn9n1SAw2bfqSxIbAil3NKm95QW37AJ6mrFYulwZe1vUXSUxnKCuyl3LRu-j__8TCt87gUl5tpDnjruTjGjQjC843JNC_r5kBZWbfSsv9El1c8brxV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/017bc45150.mp4?token=Ao6gtOga4Mx3UsVaNNYCPzOw7bqO48yPd4-bhYAnLwDvXr8z6TVNjcQro3tVTcLrXlA6WW5VtuP97GJSw8LSlagLLVCxYM81LL-gnBMOH0P0AynI6WrMkpVJFO5lPTYF68YtWhYmwCvOMc-iKRHrJAlM233nF4d56jCNt82L810sk7wtAO_GPHslnH-tYYP5_mwZ_7IgBN27irtH8__Yq3zSD6sKlUQMialn9n1SAw2bfqSxIbAil3NKm95QW37AJ6mrFYulwZe1vUXSUxnKCuyl3LRu-j__8TCt87gUl5tpDnjruTjGjQjC843JNC_r5kBZWbfSsv9El1c8brxV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندین حمله اسرائیلی در جنوب لبنان، در مناطق اطراف صور گزارش شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/126425" target="_blank">📅 09:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126424">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
منابع لبنانی از دو حمله جنگنده‌های اسرائیلی به شهر النبطیه در جنوب لبنان خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/126424" target="_blank">📅 09:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126423">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از منابعی:
یک فروند بالگرد نظامی آمریکا دیروز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و خدمه آن به سلامت نجات یافتند.
🔴
هنوز مشخص نیست که آیا این بالگرد توسط آتش (پدافندی)‌ ایران سرنگون شده یا دچار نقص فنی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/126423" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126422">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
زمین‌لرزه ۵ ریشتری سرگز هرمزگان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/126422" target="_blank">📅 09:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126421">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سقوط یک فروند بالگرد نظامی آمریکا در نزدیکی تنگه هرمز
🔴
نیویورک تایمز:  یک فروند بالگرد نظامی آمریکا دیروز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و خدمه آن به سلامت نجات یافتند.
🔴
هنوز مشخص نیست که آیا این بالگرد توسط آتش (پدافندی)‌ ایران سرنگون شده یا دچار نقص فنی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/126421" target="_blank">📅 08:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126420">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ دربارهٔ ایران:
«ما الان داریم مذاکره می‌کنیم، و آنها می‌خواهند یک توافق بسیار خوب انجام دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126420" target="_blank">📅 02:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126419">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=TPRejzY-W-QgBH7WtpCILfBnHowl9JyzYvUaM85mBUK7gSx5_nUWKlUFgVfeu8rby7pWMKk1I8otu-8oIwUOHFdZrtx-jHW72M429ag9ZGQl2ce_psmnPobbpyI8AH1eNU5c0rXTMVEiPf_3oeWEVo7as2YpWQZoPi9OxQOl-1TbPSkUhZORKM1lYzFYdkKUYR8P0iXLDH4ERWA3g1-GncesDa2lPkCldGmyze8VKKwWD-12A5xWnrJLBd3nNirBlJnNLMUL3ha1EXIVKC1xdvyW70Fo7VofP6OgOz_SZDAzkuXH1C6l15K1w1_dGLr1R3aSqBjOCselytJv5Lz17g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=TPRejzY-W-QgBH7WtpCILfBnHowl9JyzYvUaM85mBUK7gSx5_nUWKlUFgVfeu8rby7pWMKk1I8otu-8oIwUOHFdZrtx-jHW72M429ag9ZGQl2ce_psmnPobbpyI8AH1eNU5c0rXTMVEiPf_3oeWEVo7as2YpWQZoPi9OxQOl-1TbPSkUhZORKM1lYzFYdkKUYR8P0iXLDH4ERWA3g1-GncesDa2lPkCldGmyze8VKKwWD-12A5xWnrJLBd3nNirBlJnNLMUL3ha1EXIVKC1xdvyW70Fo7VofP6OgOz_SZDAzkuXH1C6l15K1w1_dGLr1R3aSqBjOCselytJv5Lz17g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا ظرف دو هفته آینده «پیروزی کامل» بر ایران را اعلام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/126419" target="_blank">📅 01:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126418">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFmkfUnAw9uLBF8nz6qXyzK02m2y0ep4nL50qo4TotptmIzCOX2vKRhQdfMswtPk4ZQ98SWETaTqvXz-k2HDX1axNnrjk1Bo41dvNTc82FAOLZ3g9d3r3jLMyuYlpYoTfE-XLx7r85ZmsNbUO2cwv__cc4rE8_6CFQjrIhQMLBSYceF_Wgp7jGo8SQDLYnoxZ3KhxJyoBarkmFBRDn53PQAICGhl-O2gFeAwtIYRGBuYIusxpDlYYu9u_UQwJOREPgCATc95mkQs_Uth5ohXB-QTX6yc5TFNA4DrJXe0Xeg8rcdS0TN3nW1viJpSq__huLvYGEMX1Crizt2LJ7VMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لشکر ۸۲ هوابرد ارتش ایالات متحده در اوایل آوریل به طور مخفیانه به اسرائیل اعزام شدند، به عنوان بخشی از برنامه‌ریزی مشترک اضطراری بین اسرائیل و ایالات متحده که از فوریه تکمیل شده است، برای تصرف جزیره خارگ تحت کنترل ایران در خلیج فارس و ایجاد قلمروی ساحلی در داخل ایران، طبق دستوری که کن کلیپنشتاین دیده است.
🔴
این دستور که در ۷ آوریل ۲۰۲۶ صادر شده، به چتربازان از گردان دوم، هنگ ۵۰۱ پیاده‌نظام، لشکر ۸۲ هوابرد - گردان معروف «جرونیمو!» - دستور داده است که به طور «ماموریت موقت» به اسرائیل اعزام شوند، در حرکتی که پیش از این توسط پنتاگون گزارش نشده بود. وقتی درباره تعداد نیروهای اعزام شده به اسرائیل و مأموریت آنها سؤال شد، پنتاگون سوالات را به فرماندهی مرکزی ایالات متحده (سنتکام) ارجاع داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/126418" target="_blank">📅 01:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126417">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/903677489f.mp4?token=SrUcLYWZdSIRPgJ4ogyadUAWbY0WObejTtt7ji33Je4uVLk7RZIvQ7F4A1H2s2eqQcbRR_c6gToNBibDK4xAjcQhsgTE0nhDYtk61XCmnJ7C5J4JChcVjBtAwlqsLT_hT56x0gxaNU18e-ncetTGE3dPhqHPobvPvPz3nCbH6bEf_nOQNQ3IDZSGLmYPQEloGRsYN-7MZEmXYRTVoa5u0Vvk_SNxVe78YFrrsR126S0NLXbo2eipAhroacRAFCuoZoDRADXPFGZth4Zdlc2uktBeFYmjkw1lShTmGIcS80NFZifkkvua-WdWYlRQPKt0ox7sICVMgsrJCGiZUzTqIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/903677489f.mp4?token=SrUcLYWZdSIRPgJ4ogyadUAWbY0WObejTtt7ji33Je4uVLk7RZIvQ7F4A1H2s2eqQcbRR_c6gToNBibDK4xAjcQhsgTE0nhDYtk61XCmnJ7C5J4JChcVjBtAwlqsLT_hT56x0gxaNU18e-ncetTGE3dPhqHPobvPvPz3nCbH6bEf_nOQNQ3IDZSGLmYPQEloGRsYN-7MZEmXYRTVoa5u0Vvk_SNxVe78YFrrsR126S0NLXbo2eipAhroacRAFCuoZoDRADXPFGZth4Zdlc2uktBeFYmjkw1lShTmGIcS80NFZifkkvua-WdWYlRQPKt0ox7sICVMgsrJCGiZUzTqIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در هیئت‌ها چه میگذرد؟
🔴
کُفرخوانی در هیئت‌ها توسط مداح‌ها برای ریتم بهتر و جذب یوزر!
🔴
سالهاست که هیئت‌ها از یک مکان مذهبی به یک مکان جهت فستیوال موزیک جاز و راک با ماسک مذهبی تبدیل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/126417" target="_blank">📅 01:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126416">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ: فکر نمی‌کنم نتانیاهو دوباره به جنگ با ایران برگردد، چون اوضاع خوب پیش می‌رود و ایران دارد کاری را که باید انجام دهد، انجام می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/126416" target="_blank">📅 01:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126414">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV2Sxr2VEdRzimefZ7Q2ran2xAZhKKLFZCXQxjHMWO4e-ytkxFNVWxcLFH22X_pKMdlJI_wAPud-8YF366ZMDtoyT0Jh9Ix1fcq1Bl4fhE7JGhBGZO309OnBV48zeAq3Q87kYaGQ6_oqOuhJzUk5GISNY0N1hnJMo-NQ75l_llhpLoH7_2imlpUOPRT08G_2tiRuSFlHSljJ6sGzWdQeOTKK-ReWILCpDWy43J6vUp9swf2ldp_6f5apMr_Bxo4apJZfpbyUzUwDEbhlfEMiMHfUhh5U0qWnDL4fVB2lytcQMVhN2zn1o7JKCIIzHCGPA5ptOfYOFv0DTqUVus-7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0774815f0.mp4?token=UnE4kJozeKaPJCGDKBoa7g6HtLapWeBlSSmQLsQRBx3pDdoHym0frPIxkwwGDdF7sKtYl6H9pZAemymukDvlS6zYEpHAz6bz81v3tnrKOy65S5g3j1jpGijmWg5XQw79cBkkdm-IrO8uz4AexEFNLS-1EVE1J6_qlrE41McC7p7UUzVvOvu88RZeOa-g25KOBI05awy9LYYONQFfdiQGWZDJ-_L33xEr1EQ6rLjRy6MNBsMIA9GDYtVQLnO_jpkDxgmGFskqbo5Wrps1x390CZ92sZwiCtLir6IsnhE386cHwistltxfLxcIBpqB1h1Td-XomJSZzL57STKSrRDTbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0774815f0.mp4?token=UnE4kJozeKaPJCGDKBoa7g6HtLapWeBlSSmQLsQRBx3pDdoHym0frPIxkwwGDdF7sKtYl6H9pZAemymukDvlS6zYEpHAz6bz81v3tnrKOy65S5g3j1jpGijmWg5XQw79cBkkdm-IrO8uz4AexEFNLS-1EVE1J6_qlrE41McC7p7UUzVvOvu88RZeOa-g25KOBI05awy9LYYONQFfdiQGWZDJ-_L33xEr1EQ6rLjRy6MNBsMIA9GDYtVQLnO_jpkDxgmGFskqbo5Wrps1x390CZ92sZwiCtLir6IsnhE386cHwistltxfLxcIBpqB1h1Td-XomJSZzL57STKSrRDTbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو عراق یه رستوران به این نام باز شده؛
ملت همیشه در صحنه هم انقدر واسشون کامنت گذاشتن که آخر سر مديريت رستوران هم مجبور شد این کامنت رو بذاره .
#کاظم_صدیقی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/126414" target="_blank">📅 01:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126413">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ان بی سی: ترامپ به نتانیاهو هشدار داد که سر به سر این نگذارد و الا اسرائیل را در مقابل ایران تنها میگذارد تا آسیب ببیند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/126413" target="_blank">📅 01:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126411">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d7d98f6a6.mp4?token=dtUjt0Mxx_R5VeLLZrDCEUb_h2DgiV0LW2bsyjxECaETSPp4Es4du1FgD3ZPZExtH4X8LrUMS_CxcJxpWPYqMJNp7lQyQbrmwc6fbPbqQW9S_sWggwv9Ld6n8xjA5QIuJnPYwbi1ZiobKarT5BzzBDNiJ95yQ0whoFFXDPpsBb0u6aiXy4_H_Pyxl3GzM3rDySfjFrxKkQ_D_3zGRdB0p5BJ7zdmlOBn5WmOaYb0YY3Exfvm2OuTf-eNGVPraEoH7Qmn79qQmXhOkUMVxwRhrB4ojx0C_GXckmlIHTHIfYQmiCixu0jsfvrqnZXR4SFAMjDj6jEtCTBda3UrVpiS0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d7d98f6a6.mp4?token=dtUjt0Mxx_R5VeLLZrDCEUb_h2DgiV0LW2bsyjxECaETSPp4Es4du1FgD3ZPZExtH4X8LrUMS_CxcJxpWPYqMJNp7lQyQbrmwc6fbPbqQW9S_sWggwv9Ld6n8xjA5QIuJnPYwbi1ZiobKarT5BzzBDNiJ95yQ0whoFFXDPpsBb0u6aiXy4_H_Pyxl3GzM3rDySfjFrxKkQ_D_3zGRdB0p5BJ7zdmlOBn5WmOaYb0YY3Exfvm2OuTf-eNGVPraEoH7Qmn79qQmXhOkUMVxwRhrB4ojx0C_GXckmlIHTHIfYQmiCixu0jsfvrqnZXR4SFAMjDj6jEtCTBda3UrVpiS0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو موشک رهگیر اسرائیلی روی یک پهپاد در ایلات، جنوب اسرائیل استفاده شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/126411" target="_blank">📅 00:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126410">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWsMvDCmoWgHRyuWfNsMJu0OLMRSvUE9zkxNrHW5C-qWoX_UTDCxaozz9M8QTpHpvPPtn0O-r2jKmcxGpuX-PL07_nioIH1FA5smiZEhQE2u7GatLbplcxxRSq2gCgzQcVMlBVAkVFn1p1mQgl5wITGkYP5noU5fTEFmp8xutX_VsQQd_JcRyRD3UM1regRfnacvGmWLtIuD23FSBMWwF_Vx274qdb-xBzYJ0pTVTDsKm2tR_KP10RPo0qtkk_ievaZ3b8vqETUoaUrGsxDq9Fn8BQEjg0Otd3MAx_PvFMMRoj2AMaawjm257e70Rj-TGarXp5NgA_NLt-7iRPtoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر براد کوپر، فرماندهی مرکز فرماندهی مرکزی، امروز در واشنگتن دی‌سی به کمیته زیرمجموعه دفاعی کمیته تخصیص‌های مجلس نمایندگان در مورد اولویت‌های عملیاتی نظامی ایالات متحده در خاورمیانه گزارش داد.
🔴
کوپر همچنین فردا به کمیته در سنا گزارش خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/126410" target="_blank">📅 00:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126409">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBtVdrHHEeOyMp_ED24EsybfM_fhNgYSgoK4f2pE1iY1Je45Z2bKyDKcNBlW0WGp1o5JOtEY2MPxpedpc0e6RJBSZBY_USw3_vAoLUR_ldrKK2BAVdbhP643hCeClVSCrdl6n_GC5zJSue3ajucOTJhC6_o9rbrkFV8m-uSzWODkNJ8JB1JcjXIRA3QbBjsWyMGg_0bX9bdJWM6kW5y5RE9lsuPgE36ArjITxt8VDkiDQCFDhBOzfKiLnt62HX0Keh4SXPJHTARj7oOvxQhAXo-UNHdabuMHjE51V8Fo8pCQAc-ZQT-ndZ9RWvDJ1kIuW4exgcQ_emXbTZkFav_Cmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / حمله پهپادی حزب‌الله به اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/126409" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126408">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
امیرسعید ایروانی، نماینده دائم جمهوری اسلامی ایران در سازمان ملل متحد، روز دوشنبه اعلام کرد که تهران و واشنگتن همچنان در حال تلاش برای مذاکره جهت دست‌یابی به یک توافق صلح هستند.
🔴
ایروانی در گفتگو با «آسوشیتدپرس» ابراز امیدواری کرد که دو طرف «به‌زودی» به یک «نتیجه نهایی» دست می‌یابند.
🔴
او در پاسخ به این سوال که آیا فکر می‌کند این توافق تا پایان ماه جاری میلادی (ژوئن) حاصل خواهد شد یا خیر، گفت: «امیدواریم، امیدواریم که اینطور شود.»
🔴
با این حال، او تاکید کرد که هرگونه آتش‌بس باید جامع بوده و تمام منطقه، از جمله لبنان را شامل شود. شرطی که اسرائیل آن را رد می‌کند. در همین راستا، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه تاکید کرد که این کشور به حملات خود علیه حزب‌الله لبنان ادامه خواهد داد، هرچند که در عین حال از انجام حملات بیشتر علیه ایران عقب‌نشینی کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/126408" target="_blank">📅 00:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126407">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
اطلاعات جدید از کمک‌های اردن به اسرائیل در حملات علیه ایران
🔴
یک منبع نظامی در گفت وگو با فارس: بخش عمده‌ای از حملات موشکی جنگنده‌های اسرائیلی علیه ایران، از حریم هوایی اردن صورت گرفته است.
🔴
جنگنده های رژیم صهیونیستی به دلیل جایگزینی تجهیزات راداری و پدافندی غرب ایران، در حمله اخیر از «مهمات دورایستای هوا به زمین» استفاده کرده‌اند.
🔴
همچنین بالگردهای ارتش اردن نیز در عملیات رهگیری موشک‌ها و پهپادهای شلیک‌شده ازسوی ایران نقش حمایتی قابل توجهی به ارتش اسرائیل ایفا کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/126407" target="_blank">📅 00:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cadc07182.mp4?token=W2UAtTT-GwsL_Lecx-RqNmWjkJGonlJo5_8kmLzFSysoOpNJu9cbrqVdUVqkAA2SFUXOeH230sNjcVFtIMI3aoT0wu86_CDBl4A_umdMud-e0QIq5RhzWbd14NWfIAbXj5-DYZ0bTUe54OhES5uv2jjXpK-MkbfHIMlIkLNdDgrBZ-s_3sIIE-E640oMIF6NTAnLF8pUn8ImximTKK5VcJZBMmxz0M26B6LtZz-xiW1wof0AuRvyfW9RpDXLZiUJJBdWgBXST0ofteUjlPDMmMNq43PkZpIwA9ECbrWwmPx94TGfFuA7otgoc9yEdDlLotT-qeNFFUrgpj3g4RoxuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cadc07182.mp4?token=W2UAtTT-GwsL_Lecx-RqNmWjkJGonlJo5_8kmLzFSysoOpNJu9cbrqVdUVqkAA2SFUXOeH230sNjcVFtIMI3aoT0wu86_CDBl4A_umdMud-e0QIq5RhzWbd14NWfIAbXj5-DYZ0bTUe54OhES5uv2jjXpK-MkbfHIMlIkLNdDgrBZ-s_3sIIE-E640oMIF6NTAnLF8pUn8ImximTKK5VcJZBMmxz0M26B6LtZz-xiW1wof0AuRvyfW9RpDXLZiUJJBdWgBXST0ofteUjlPDMmMNq43PkZpIwA9ECbrWwmPx94TGfFuA7otgoc9yEdDlLotT-qeNFFUrgpj3g4RoxuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
هواپیمای سنگال که رسید نیروهای امنیتی ایالات متحده اینطوری ریختن رو سر اعضای تیم ملی سنگال و چکشون کردن
@AloSport</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/126405" target="_blank">📅 00:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnJ6_FYBukuNI-3OiJ0GQLr4wvFRaE5cB8XO5UJQaQ7yQV-2TZm2_VD6zEI31pillyLpUsOxtwECdPnyWPMzK3veWI1W8A_Kj_jVN6StGt8GMCQxFmJMRLfKC7tVSsgzKzkYtxHDP2-JGBIPbD8rgjtpPDCGglOa6xa9pqdbSqaYmjUIoFtPMZjEMtfBqLHBskZCncbdN0NXJlGTXmVcqxA_D5sJlPTa_L0gSCuKW4_F2J5Oo5wwilhENlRcaWBKegocgYG0KotVn6IiODuw2YRC18ZDB7F3jYVRfMKkXSuC_RbQh7BgHyH02yfZTS948Y9bJ54JG1EUxJhvE5E_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
🆓
🆓
🆓
🆓
🆓
🆓
🆓
هر ساعت کانفیگ رایگان میزارن برید رایگان وصل شید
🔥
❤️
سرور هاشونم تضمینیه
❤️
❤️
قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/126404" target="_blank">📅 00:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126403">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: حملات اسرائیل به بیروت تکرار شود، اسرائیل شدیدتر مجازات می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/126403" target="_blank">📅 00:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126402">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXmI4_s2CZpWVsxCRyTNDZSnlkXfAb7nNlyW4TyNFBqsYyCiV0ctTVmkF2DPw66YYOjFZRz6kOUky8ZzUfhgtwIpAF9fgs_3WLDOkLfObDfEkSqAaAagPsqYvMPckmpHHNj9_M1oqiyOYXWzYwd0YVf2HYqLCJTD7UaIKZljm6HRVnomQGo2mUorZYeG3GcvnA7L994KvKzxA0-Y23tEXrYhzVgRupjCdUUldFmXaL1eLILslsUHBLFpBzBalA0FiLl9l_wVjmNnKUCJThSFNM7WgwVvxNHoU_PkfFJ53P-RPKP3_D-8jeTXOplv6CPO9kbxjqWDI7OToltRyfZ-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ تاد بلانش را برای سمت دادستان کل ایالات متحده به سنا معرفی کرده است تا تأیید شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/126402" target="_blank">📅 00:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126401">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
مقام ایرانی به الجزیره: واشنگتن در پیش نویس یادداشت تفاهم تغییر ایجاد کرد و این موضوع غیرقابل قبول است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/126401" target="_blank">📅 23:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126400">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ به اکسیوس: ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/126400" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXxKF0zC9YHARbMwXbfUQ1OO3ftcGijTGlqYAHzGR0hi3xN5XKjQMv3OJJMTwZv-TIJ4SMd1CJrjOh4cPfkK4lTss42ngxRbKBBCWuQu1yRRoOHVQiJGJ3idoSe6g0BGum7U0MQgOeqmYlO7nlXoSZ0lUtZhdSadYnalbYuTiBCvZ_fKJ17curAyaPhcQnmkfAFnPsbrf3JL9AKinBRb-euh7m2Vd3nmAz98QUHFqjnHXpx-4mOgekicgKr0mpNEWP14VL78gS-Vh2AwSgb4oPJGFGFMdgEVq14ymxPnHSslokp7iElQIqZvTDcMQPMERvlBXfD5RBpo2RRgsZVlsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه عبور نفتکش‌ها از تنگه هرمز در سال‌های مختلف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/126399" target="_blank">📅 23:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126398">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مقام ایرانی به الجزیره:
واشنگتن در پیش نویس یادداشت تفاهم تغییر ایجاد کرد و این موضوع غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/126398" target="_blank">📅 23:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126397">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
منابع خبری از شنیده شدن صدای انفجارهایی در سلیمانیه واقع در شمال عراق خبر می دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/126397" target="_blank">📅 23:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126396">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoTMg4BoX2bNb4r-X97hEKaKvF2uG6nBhcG3YGWzFteoOQsPNi9_dD7apgdE8Ii26FFDSauwhoBYhEF-54axgEG_MWaPE_VJPclobBiKN04yVuJqYms9jvBbcccXf_11dIBp40pzyO_Uoz25X3SbiSaQZZkP5IY73v5RnA2XgLnYcCMlofs-fIs0xvAP94AaebAs-OQu1nFJAYyfM4q9Zx4UJNNBOj6WCdLYiKu2Ij94h05o4msrXE0huGuvJP3ppPdLHK1GgM-0BZI4eMFFoIjg8GzFpCAU9hcLvuUEirzbRZWwl6efBVYwtLqAU_q0Ywza_HmQYHGxwRQIstxPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به Axios گفت:
بیبی برای زنده ماندن سیاسی در اسرائیل نیاز دارد که جنگ ادامه یابد، و ترامپ برای زنده ماندن سیاسی در آمریکا نیاز دارد که جنگ پایان یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/126396" target="_blank">📅 23:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126395">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWzbGLF26hctoR4u-CF5un3Fr-3EcfeXcn9ZQy2D7aIMqurwtncKje_jZnVkj4HvYvpgaYK7U8P-AtNrSG0qveD26K_0bgmZGI2XMA3W_cMO1BB7BnaXXLItJGFepLMxu0K9wwnua2XuKJW0q8_omwyST0tmwz7t2sHVEusV3Hvm7iwe8BmHvu8ZczwF4uwVJI4iVSM8NOz0ggqcamOzSCcJ8l0yn8bHWZ-8ZQFHyP0znRoWmvNUwCQ5ltmNSDrkUtS1HV7fCWE2e_-pDhEj4LPEAwb7OmFiTWahnJD4KcoAdSqyTdnKghWmHltb3nwfOpIZ_oVi_MLDGbyn20chgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/126395" target="_blank">📅 23:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126394">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f522c1055.mp4?token=UZkqMdBm9RVRJPyY0ldrt76ftCOoBRNKeYtf3S7wULzdC64UBjw_Z9_MxsnrgxL8-Kb7_qTHfZd8Mk0_pxWPEXWny0Wpyy9CXbqIosXsKCrfbrEcLWTKTaKHaMHUb3GEyNJOeBf5_z5EQfVccuOyX_D3OdddiD5xy2-Rf6yRgvo20SdBUN2fBxFQRtYxyCnw-P9SKkngopseyP0ZX--s6pykxN1G5sjZRsSL_hTaXPAGvltX62l9O6iPPzavx-5yEajvBBjS0q34sHtH0IxIcXSjGRThZLMLVr-LHaoadogNhewXFNgxn3uS6VFcFt9idjxU5p6cA8bxWp-cB4_fLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f522c1055.mp4?token=UZkqMdBm9RVRJPyY0ldrt76ftCOoBRNKeYtf3S7wULzdC64UBjw_Z9_MxsnrgxL8-Kb7_qTHfZd8Mk0_pxWPEXWny0Wpyy9CXbqIosXsKCrfbrEcLWTKTaKHaMHUb3GEyNJOeBf5_z5EQfVccuOyX_D3OdddiD5xy2-Rf6yRgvo20SdBUN2fBxFQRtYxyCnw-P9SKkngopseyP0ZX--s6pykxN1G5sjZRsSL_hTaXPAGvltX62l9O6iPPzavx-5yEajvBBjS0q34sHtH0IxIcXSjGRThZLMLVr-LHaoadogNhewXFNgxn3uS6VFcFt9idjxU5p6cA8bxWp-cB4_fLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پدافند هوایی آمریکا یه موشک بالستیک از ایران به سمت پایگاه آمریکایی تو شمال عراق رو رهگیری کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/126394" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126392">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amURavho6UAIQfoT2QqcJKUzXnfTQ8vbUmk6DdXg13kCwpWSkA8CwlvDBHlbLv2eUUOuiHDX8_ycOUD_P34IHFUYZeG4LmK1QVQYmWYVQNteAPshKdzFTK9VzVWZbP2hCKRaHNIkxwHMTqSzgRnrvqZ3i-EtHwul8yoPzVZA-96JYZ4AHOru-Ft9Hv4oxDzBACSxSQe2HFjQECpvTPBRleSXmED1uGMegCK-u1qH0lj7UGzbnchI8ZpTdQwQPFzVJBGQ23WRbMxFr2Re-cm5GKbM9RnSG5YhXvYICwjOrltFgmXqpYFG0IzqKQBXYz-NA569-7QK1H9Yd3XfdyUzfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/934b102cbf.mp4?token=Oig95vlZGjHmddA-mphlymE5i-F2n-wGj7-JKoY6gnMaIuqc83q-DJ5c4LSQ4qVNcD4vgXmpuHAE_U6gcxNAXGJgnYKca6HAxFX0GIg3kGFNk8UA-yLW7qgmbxPuN8OqIkaS2F4fm8GvXMgA-MED0ImHTTE6MoQ-GisFuDgoOhNDCPynPYAZjkY34KPt7q05S0px2tiUfkmhBIvVI2lvDx50kCtx-Ggcs2UMU-cWVmMECv-n9cbbxUEi_HEQo7xqpVFGt7SF3mCjdoVBey3yam9ojp2T2l_47nKgvwRno7sWHJu_kGyy1Kh2xLyHVHwgFegy9rjOxxyT4fG5iEYY1osDq6an4dsOEz0XTIhjsPzJWFkeT4ZWydtHJPSxNyUbz0-BMAV56Qcr3FcXEu_LRy6naO-JP_wxxWmG40P-etyBpbFob5474LuOk1SftOLbj5sHzBle6OB5mfB5QqcjztwZm05QEg5RCEipjzhBOakXEkIwPWm5HV1uaHsiAJldrf6W8hN4xyM3X6Th5yaWnKbDOp6stVmrdOL0-oVUjrtFcdPhjIeIQiFquRqAuETqsZjQb-3fTfSFsP9-Oph2CYts3i0a2tsKEjygVDNIQ1ZAK9GqdDsZJS2bFd42HKlLIUzZhlwYhSQSXZe4bNzm4LwRh-JFWsMj01CDuadkCWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/934b102cbf.mp4?token=Oig95vlZGjHmddA-mphlymE5i-F2n-wGj7-JKoY6gnMaIuqc83q-DJ5c4LSQ4qVNcD4vgXmpuHAE_U6gcxNAXGJgnYKca6HAxFX0GIg3kGFNk8UA-yLW7qgmbxPuN8OqIkaS2F4fm8GvXMgA-MED0ImHTTE6MoQ-GisFuDgoOhNDCPynPYAZjkY34KPt7q05S0px2tiUfkmhBIvVI2lvDx50kCtx-Ggcs2UMU-cWVmMECv-n9cbbxUEi_HEQo7xqpVFGt7SF3mCjdoVBey3yam9ojp2T2l_47nKgvwRno7sWHJu_kGyy1Kh2xLyHVHwgFegy9rjOxxyT4fG5iEYY1osDq6an4dsOEz0XTIhjsPzJWFkeT4ZWydtHJPSxNyUbz0-BMAV56Qcr3FcXEu_LRy6naO-JP_wxxWmG40P-etyBpbFob5474LuOk1SftOLbj5sHzBle6OB5mfB5QqcjztwZm05QEg5RCEipjzhBOakXEkIwPWm5HV1uaHsiAJldrf6W8hN4xyM3X6Th5yaWnKbDOp6stVmrdOL0-oVUjrtFcdPhjIeIQiFquRqAuETqsZjQb-3fTfSFsP9-Oph2CYts3i0a2tsKEjygVDNIQ1ZAK9GqdDsZJS2bFd42HKlLIUzZhlwYhSQSXZe4bNzm4LwRh-JFWsMj01CDuadkCWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انبار مهمات عظیم امروز صبح نزدیک بلوفسکویه در منطقه بلگورود روسیه منفجر شد.
🔴
گزارش شده که این انفجار ناشی از هیچ حمله‌ای نبوده است، اگرچه هنوز مشخص نیست چرا این اتفاق افتاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/126392" target="_blank">📅 23:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126391">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
آکسیوس: ترامپ صراحتاً به نتانیاهو گفته که از پاسخ به ایران حمایت نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/126391" target="_blank">📅 23:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126390">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
آکسیوس به نقل از منبع اسرائیلی: ارتش اسرائیل پیش از حمله به بیروت، سنتکام را مطلع کرده بود، اما کاخ سفید را در جریان نگذاشته بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/126390" target="_blank">📅 23:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کارشناس صداوسیما: مردم ایران الان یکصدا میگن جان ما و لبنانی‌ها یکیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/126389" target="_blank">📅 23:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی:
آتش بس باید در سراسر لبنان اعمال شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/126388" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126387">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HViu4Jk1GEk-k_m0mDM-K5yckmPZEmKs4ABA1KHQyKlMgDY7EtKom15H4mxwkr-DJ5gGDf2jPImPghOWfb-u-yXkKpzgwAxwtlNHQTempgO3mzrQhDFi0y0JlQbhjMnkvTD2OkNPQjL5mBjYoHadyu7q1u6_1TWcCUwc1JSm4aguHvnb3Z6pqZB-C7L4jI0Vg3H1DQc6nxG_t9OPrjH5WbOezACKsSlllPoN2Mfg25QcjlxTsZwV-3wb37SgAURYJv4S3maWpNyUg27KXa82Ye01YFHNStiM-egsiGhHiTkV_Va0r0gdHWiklYaTVUhNIMxAuW0ocLtvobd13gKntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روبیکا به کانال خاله دنیا جهانبخت تیک آبی داد و رسما تاییدش کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/126387" target="_blank">📅 23:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126386">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🤩
⚽️
کامنت شاهزاده زیر پست فیفا :  آخرین رقص
🔥
😉
The Last dance
🇧🇷
@AloSport</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/126386" target="_blank">📅 23:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126385">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رسایی: این عنو(اینترنت) قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/126385" target="_blank">📅 23:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126383">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128f9bb157.mp4?token=XPVVW9WPx-MsBeXDrremhEeQSO18wbCFF60-P1WrVnHiwWJz9X-I_giLI3XdxfCudlrTrPvK5tsFWhxQJ0fz4Atf3aOkO0hHGr7SzznH9hiWF6KJfxng4jWm0R9czQ3DXZMfM9W1nnuzAnZYeApvzyd-ZGRlsDMLpIMJezp40dRbuU9DzSuwMMnvVyULkRslmZ2KQUz_oVlqRVUQkYSFPklqbFBQsDuOchqtSX6UFbi-ewg6tbEQBrYez-cI_RUZHWT1ovhkXwWNyTaDCy5PXBn8oQOnKrGftLTK-ZsQjkIplbGx3XNi5qBvoKMQ0Gj8tENtf79c3I0SehDr8Af6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128f9bb157.mp4?token=XPVVW9WPx-MsBeXDrremhEeQSO18wbCFF60-P1WrVnHiwWJz9X-I_giLI3XdxfCudlrTrPvK5tsFWhxQJ0fz4Atf3aOkO0hHGr7SzznH9hiWF6KJfxng4jWm0R9czQ3DXZMfM9W1nnuzAnZYeApvzyd-ZGRlsDMLpIMJezp40dRbuU9DzSuwMMnvVyULkRslmZ2KQUz_oVlqRVUQkYSFPklqbFBQsDuOchqtSX6UFbi-ewg6tbEQBrYez-cI_RUZHWT1ovhkXwWNyTaDCy5PXBn8oQOnKrGftLTK-ZsQjkIplbGx3XNi5qBvoKMQ0Gj8tENtf79c3I0SehDr8Af6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محیا دهقانی، بازیگری که برا نقش رل میزنه: نصف جوونای ایرانی بیکارن ولی دائم در حال خوش گذرونین و خوب زندگی میکنن. خارج کجا اینطوریه؟ اگه برین اونجا باید صبح تا شب کار کنین فقط
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/126383" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126382">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اتحادیه اروپا روز دوشنبه تحریم‌هایی را علیه دو شهروند ایرانی و یک واحد از سپاه  اعمال کرد.
🔴
این تحریم‌ها فرماندهی استانی نیروی دریایی سپاه در هرمزگان، همچنین محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه، و حمید حسینی، نماینده اتحادیه صادرکنندگان نفت، گاز و محصولات پتروشیمی ایران را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/126382" target="_blank">📅 22:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: آزادی اموال بلوکه شده، مادامی که ایران به تعهدات خود پایبند نشود، رخ نخواهد داد
🔴
محاصره دریایی اعمال شده علیه ایران تا دست‌یابی به توافق پابرجا خواهد ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/126381" target="_blank">📅 22:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126380">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f477f009.mp4?token=v6QjdrLjrqGLWy6xXFYY-h9_weeHeyiorIfIpcQrtGCIpxKfQgLrYVFeF6kxqgvz8WZeu1iit-QW4KD576CX0lS8eirPaJgebr5txGmizYLqOZFfWCWfS_BlShr4NdVEBcf9VFhUWDdXb9whIlPFxv_4vJWzzuNIiqXXOKZO2X5smGzb3Gg_4Dx8SLp6eTrILOZt8kdAn9vfsvPd9Eb6zLKUq-DrDPtU4kJTMjHy2bjuqiVWUNAoK1gEMvwxLQSPaphZXPz5e8urOjRgxAuPw3eoA-lDnRUsG4drChaLKiDIG6Es2e2eRC9jlNh7TZE45c0VHtsMxKiUJJwDY9bUmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f477f009.mp4?token=v6QjdrLjrqGLWy6xXFYY-h9_weeHeyiorIfIpcQrtGCIpxKfQgLrYVFeF6kxqgvz8WZeu1iit-QW4KD576CX0lS8eirPaJgebr5txGmizYLqOZFfWCWfS_BlShr4NdVEBcf9VFhUWDdXb9whIlPFxv_4vJWzzuNIiqXXOKZO2X5smGzb3Gg_4Dx8SLp6eTrILOZt8kdAn9vfsvPd9Eb6zLKUq-DrDPtU4kJTMjHy2bjuqiVWUNAoK1gEMvwxLQSPaphZXPz5e8urOjRgxAuPw3eoA-lDnRUsG4drChaLKiDIG6Es2e2eRC9jlNh7TZE45c0VHtsMxKiUJJwDY9bUmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله موشکی به مخفیگاه‌های جدایی‌طلبان در کردستان عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/126380" target="_blank">📅 22:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126379">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8efb5da491.mp4?token=hOyl0vcy6oeD0vJvCealEuT_VfhBWGmWlZZ0wlWCRyUvFaq0oBrlfskG_FzHHjsJlVk1A5GLNac0PhyBTBdIaD2JbloqjS6ZipXstUt--XXZiEbT2WNhu--du0gP8LVD7jhmO68NTv-wYGgMOCAbDh0SjLT-CCx8uqsAl_OT8MYzj-UtL68N2u1xGtD1AD5JDjF0TnEfqvg6MSIV1Tw3Y_ghaXF6JFmZsfE1RAn9mzwF5-WybA-_T-TaRAH28haG7JwRMub2iwBR6zbwPzcIYz_buAZTJhLja7im_KkfREoSTy1kJ8LLwUWiBeMpSznkAXJipL8dmzbXU9nr2PQLJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8efb5da491.mp4?token=hOyl0vcy6oeD0vJvCealEuT_VfhBWGmWlZZ0wlWCRyUvFaq0oBrlfskG_FzHHjsJlVk1A5GLNac0PhyBTBdIaD2JbloqjS6ZipXstUt--XXZiEbT2WNhu--du0gP8LVD7jhmO68NTv-wYGgMOCAbDh0SjLT-CCx8uqsAl_OT8MYzj-UtL68N2u1xGtD1AD5JDjF0TnEfqvg6MSIV1Tw3Y_ghaXF6JFmZsfE1RAn9mzwF5-WybA-_T-TaRAH28haG7JwRMub2iwBR6zbwPzcIYz_buAZTJhLja7im_KkfREoSTy1kJ8LLwUWiBeMpSznkAXJipL8dmzbXU9nr2PQLJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لبنان، صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/126379" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126378">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
شنیده شدن انفجار در اربیل عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/126378" target="_blank">📅 22:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126376">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgUWChU9O6szOJDZnE764f7mFS-jGYB8ERxLZUYW-ZOEMn2TjzMPCTSeBIzjD9_Ds0E721n1NumjoLBTwcqF-rtCEo4c50Xyf6HMgQzgJ4dRHXSf0hLZEfXWMM2D_50PkvgDpUheXnstawQkFq6OziZ7-CZbyPVwxK0ZwxiIJGhJzgsWRVWlPha4OQn2wAxaLDKmHmnq7YOKEZmN2OGwvFoZBwr2j4WhLFGOgyXuAKJs55-BYAu2pPT8map0NbsDMKg-wEJfavYXhpheLJw4M3aQJIRjY4Gni4RFgGKtjD-JFjMAAKH_54CAZy3X_9FkG-u10Y1femL6XexK0mchEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sdj_gA8eYnYt5LHVsSAfF0cFVJHgHEj-UI8XhDKS2qBCAFUPFiuNErrsoRNW9qYxjuMnFC-9LPWYYq8rHOiS90zwIZfJA5ry38lV5Xb3N9T0t7M5UhWC4E4de2Vyp_hg9IBAPMbBZRh3rQVQttBua3L91yWeBJJOaxifEzfwPCkY4Zrv3IZnXfDSvUCe1k-KHa-84Rlt1l0mDi03Ua6Els6rYfFMYU3cvuV9pJJHFd3XP8QWDya7btFthAMjEkothocdthms7BQG6o9N4XovjaqjiXVuCDAX7c_60C0UWznmFlp_TvHm65rXhI8mh6ygu9TLmsFaYEVJoT2mwXtGAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای Sentinel-2 نشان می‌دهد که به نظر می‌رسد یک موشک ایرانی به انباری در پایگاه هوایی رامات داوید در شمال اسرائیل اصابت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/126376" target="_blank">📅 22:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126375">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_CcVwqbRWVMly10ELO6hWCqR44f-9eAPgwzuxtcI0bjJ2CRA8bWjsEY7sZ0p-Imi-BNvkbcULhqMNAqOojRYd-hjl4ah-MMvMCLiPw1qaET-qbwhIRi-1NWKpEGBLhIoaFdNv8uiHCUaQoyEpi-0gLxvFE6CvKvI50glF8Pl43FEtiHE-oIahAmbM7-Z0d1w-BQ1yEgi9q6IpYRLpRMEuyNtSrYn5wWMkEneI85g1O3nMqjV5E28R56uWqVFYLASNhjhQxD_-j1jz05gPU3X8Fp5jIu0XjD6LCFds5Vzi9hyMU1oFLBrKjJgOsrNgxCDQb1oYmEmfZmazXUyyIu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خاویر بالاس ستون نویس بلومبرگ: سقوط آزاد ذخایر استراتژیک نفت آمریکا؛ در آستانه پایین‌ترین سطح ۴۰ سال گذشته
🔴
گزارش‌ها حاکی از آن است که با آزادسازی ۷.۹ میلیون بشکه دیگر از ذخایر استراتژیک نفت ایالات متحده (SPR)، حجم این ذخایر تا پنجم ژوئن به ۳۴۹.۲ میلیون بشکه افت کرده است.
🔴
این روند نزولی نشان می‌دهد که ذخایر استراتژیک آمریکا با سرعت به سمت رکورد ۳۴۶ میلیون بشکه در حرکت است؛ رقمی که پایین‌ترین سطح ثبت‌شده برای این ذخایر در ۴۰ سال اخیر (در دوران دولت بایدن) محسوب می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/126375" target="_blank">📅 22:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126374">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / نبویان، نماینده مجلس: ایران پیشنهاد واگذاری تنگه هرمز را داده
🔴
بر اساس پیش‌نویس تفاهم ایران باید ظرف ۳۰ روز ترتیباتی اتخاد کند تا رفت و آمد کشتی‌ها به حالت قبل جنگ برگردد.
🔴
وضعیت اخذ عوارض مشخص نیست.
🔴
وظیفه مین‌روبی هم به ایران سپرده شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/126374" target="_blank">📅 22:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126373">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24a75b678.mp4?token=myw4VNjousiXCDKnqQDJoGMyVNw11J5cL-oV3INDx-M3JuLgkFnOSyzcDVla4NNw4AsOvn-_1wXuP2MjbZ9sjPQ4_KKa7gKiS1pqagh2vCeUAvoCxqswmWPYyTJa1ZXP6M8dNEJLuUjlCr8TtocZ07YEroK2Nw-BeS3lb-yhSwazi7LoyYOOSRGM71NY3eyrWVq8KB4GSCDyFwYiZWemvjADYMUM9WFb1NpjT_Vj2nr1LlSzrBKLfrYPDsJ22vRUKSWx9-oOvpZS19k9Po66QJKtkYcsBimgTJ-1z3g2xt4rbzka1Q-J6QOWpTF-vz1Y7FUj1hhTpFAQPifaF4agBbFd-_-964w4Wg__we9c0iWEYlAh7gjQWGB1KX1Wop3jZG2P2MZVdgpvcJLoAz1hVe0oc7tVOLsRVSs8f23YMKiLu1Jl2bBcPEIctb7rhgR2iQUWOx-aXVbPTB2EqyT7THa9kpTAdQtWhSVR-3dOt4cJ31E0gDpGqWr1oeu7Hti_tu0X8HqgfC5PdQCLZMkCrvQCqpTxiUZ_p9GDiB46MxzzucKTT-8AZI4R2XzjRCpcqqs-tY2h0N9egw9sa1ZMNtfA6shzC8NJr4enAuK425xSNfiMQk6mS4cL6gnvXm7d3UGRSsmhKBnmdlWq-Ekdg3nshhAY_TElNFauckdV1KY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24a75b678.mp4?token=myw4VNjousiXCDKnqQDJoGMyVNw11J5cL-oV3INDx-M3JuLgkFnOSyzcDVla4NNw4AsOvn-_1wXuP2MjbZ9sjPQ4_KKa7gKiS1pqagh2vCeUAvoCxqswmWPYyTJa1ZXP6M8dNEJLuUjlCr8TtocZ07YEroK2Nw-BeS3lb-yhSwazi7LoyYOOSRGM71NY3eyrWVq8KB4GSCDyFwYiZWemvjADYMUM9WFb1NpjT_Vj2nr1LlSzrBKLfrYPDsJ22vRUKSWx9-oOvpZS19k9Po66QJKtkYcsBimgTJ-1z3g2xt4rbzka1Q-J6QOWpTF-vz1Y7FUj1hhTpFAQPifaF4agBbFd-_-964w4Wg__we9c0iWEYlAh7gjQWGB1KX1Wop3jZG2P2MZVdgpvcJLoAz1hVe0oc7tVOLsRVSs8f23YMKiLu1Jl2bBcPEIctb7rhgR2iQUWOx-aXVbPTB2EqyT7THa9kpTAdQtWhSVR-3dOt4cJ31E0gDpGqWr1oeu7Hti_tu0X8HqgfC5PdQCLZMkCrvQCqpTxiUZ_p9GDiB46MxzzucKTT-8AZI4R2XzjRCpcqqs-tY2h0N9egw9sa1ZMNtfA6shzC8NJr4enAuK425xSNfiMQk6mS4cL6gnvXm7d3UGRSsmhKBnmdlWq-Ekdg3nshhAY_TElNFauckdV1KY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: خیلی عجیب است که افرادی در کشور از مذاکره دفاع می‌کنند در حالی که رئیس هیئت مذاکره‌کننده ایران می‌گوید دشمن به مذاکره اعتقاد ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/126373" target="_blank">📅 22:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126372">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
میشل عون به سی‌ان‌ان: ما به دنبال رابطه خوب با ایران هستیم، اما نباید در امور ما دخالت کند و کشور ما را به خاطر منافع خود نابود کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/126372" target="_blank">📅 22:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126371">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
روسیه: پیش‌نویس قطعنامه آمریکا علیه ایران شرم‌آور است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/126371" target="_blank">📅 22:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126370">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07861131cf.mp4?token=omSd1DbNQMklSdukIVm2rEMNe4kKrZ_38NhYjG_0dUPY4I-UkbNv_EsghqFuCmVKU2HYdUw3PGAIJ-aImStcYF9-9N5kIFnTngM3Q1WWUbkiO5uuxzIUpzfZMWgbZ2685ePIr2E5GXqPwAgSab5is1GzQ3FT1wkUHFpSO0434f-fPkMpBj4__YsoWjzTnmVEuhh1aJx1nsmf1ke3EXdDez4f7l0DKxO7EMouX_sJMxfxGteYQ16ZKfvyPJ04vBwJl0REME8bsvDRCg9cAEwcHTyVC1xmpMeVdtVTBb3QPyuuhay8qfXdoO0o0R0ugUEImIlxmFlDam0fbSs6GELLlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07861131cf.mp4?token=omSd1DbNQMklSdukIVm2rEMNe4kKrZ_38NhYjG_0dUPY4I-UkbNv_EsghqFuCmVKU2HYdUw3PGAIJ-aImStcYF9-9N5kIFnTngM3Q1WWUbkiO5uuxzIUpzfZMWgbZ2685ePIr2E5GXqPwAgSab5is1GzQ3FT1wkUHFpSO0434f-fPkMpBj4__YsoWjzTnmVEuhh1aJx1nsmf1ke3EXdDez4f7l0DKxO7EMouX_sJMxfxGteYQ16ZKfvyPJ04vBwJl0REME8bsvDRCg9cAEwcHTyVC1xmpMeVdtVTBb3QPyuuhay8qfXdoO0o0R0ugUEImIlxmFlDam0fbSs6GELLlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنوب لبنان پس از حملات اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/126370" target="_blank">📅 22:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126369">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTrAFkPZFIb_xI4x2rtQ4iVxQ6GCrK7jg5fAAjYZJi5zBQ6H8LKnHUECeudiM-3IoBRqH4yDdPJ3d-y0GMiA-UhrTikIvotA35vuF7c9FzLFmDvT7obXReVJHxVmk-qUyVDojg4WA79yL4-B19_Hkf8CETBDj4K3_S98yuXAQ2JCkLuphWlj6myS8qZL6Bd9GboU01bFMeHmLOfR1EIG-yM-7QDLmMjOvWiKhbco1dV6FKu_lYwnMR9nKTVuuT_DOS451x6CqY_2dUHC3JiaNZUdcVI-RXKgWbY7xOdHINNolLgVcQleMeMM9nG-diNY4i7sW2QI8NWD-z1k-5PpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عارف: دشمن ناچار به التماس مجدد برای آتش‌بس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/126369" target="_blank">📅 22:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126368">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e489176d06.mp4?token=N--DJHUs_XiKRXU7Rs5gR5avC3KlyfMkFbwOmWW0pyCtxmAmzGYHppnIw36KyF_d8TuZrb3wXve1-FPV2OSlC30akXAQDiEG4_kaRyi20tzI1U6tAGfg9AwK4IQ3Kg6EFgQoITJtwDMf3PYz5RpliDayA5QOFPC9rHYAKWG_QB7Hfw2Bf231lv7MKrzLdqzpV53Ov8xbhQeTcKAAIDGAq0gshk9ORsjnXLg7-MftwsNP82nalsLKiAiPyI5Gj2WNZAYaGKlIqirriQCgnO50m0Cm1WM2OJc2L4CTzedOs6uVtkCH3HFGjML74AFUAR4DuhWJcxeW0LCxJhjXUFxbrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e489176d06.mp4?token=N--DJHUs_XiKRXU7Rs5gR5avC3KlyfMkFbwOmWW0pyCtxmAmzGYHppnIw36KyF_d8TuZrb3wXve1-FPV2OSlC30akXAQDiEG4_kaRyi20tzI1U6tAGfg9AwK4IQ3Kg6EFgQoITJtwDMf3PYz5RpliDayA5QOFPC9rHYAKWG_QB7Hfw2Bf231lv7MKrzLdqzpV53Ov8xbhQeTcKAAIDGAq0gshk9ORsjnXLg7-MftwsNP82nalsLKiAiPyI5Gj2WNZAYaGKlIqirriQCgnO50m0Cm1WM2OJc2L4CTzedOs6uVtkCH3HFGjML74AFUAR4DuhWJcxeW0LCxJhjXUFxbrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر آخرالزمانی از زلزله ۷/۸ ریشتری‌ فیلیپین؛ این ۳ ساختمان متصل به هم از یکدیگر جدا شدند و آب استخر به پایین می‌ریزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/126368" target="_blank">📅 21:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
استان یزد فردا تعطیل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/126367" target="_blank">📅 21:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126366">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef830c9ba.mp4?token=v8XMBMyuObD7Ds1Ux_fBPZAJIrd_XfpYHzFOVnQvKklF7NP7-ogjqvhiCp7e8xvCdXuuQUocUxHtwLWgqe_9w_pZdXFxFpEcG1MRRycvuGcmC0RuCXyETOE9LvtKcxqihqpo3n7WL0DgAQmAKHCilnBiqBGPnxDy4FH94KuZ2vK9uPMkPC7oqJOplQKA336VhJY8uboKptgpsg4C6wlcb5Z6Ax4inFJS7BMBbG0miUlh03NjSrBgRBZec5yR-tjq0ezOoRIh6LjK8n0RZdhW7ioXZKTxYa_0dR_6KAOPzm9rkUf-t3uLqj5xdBvDvCTpLfyzOVk8giaPWMgbnNIX8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef830c9ba.mp4?token=v8XMBMyuObD7Ds1Ux_fBPZAJIrd_XfpYHzFOVnQvKklF7NP7-ogjqvhiCp7e8xvCdXuuQUocUxHtwLWgqe_9w_pZdXFxFpEcG1MRRycvuGcmC0RuCXyETOE9LvtKcxqihqpo3n7WL0DgAQmAKHCilnBiqBGPnxDy4FH94KuZ2vK9uPMkPC7oqJOplQKA336VhJY8uboKptgpsg4C6wlcb5Z6Ax4inFJS7BMBbG0miUlh03NjSrBgRBZec5yR-tjq0ezOoRIh6LjK8n0RZdhW7ioXZKTxYa_0dR_6KAOPzm9rkUf-t3uLqj5xdBvDvCTpLfyzOVk8giaPWMgbnNIX8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله اسرائیل به مناطق جنوبی لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/126366" target="_blank">📅 21:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رئیس سازمان انرژی اتمی: واحدهای دوم و سوم نیروگاه بوشهر با سرمایه‌گذاری ۱۰ میلیارد دلاری در حال ساخت است/ دستیابی به ۲۰ هزار مگاوات برق هسته‌ای در دستور کار قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/126365" target="_blank">📅 21:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر امور خارجه فرانسه به الحدث:
بستن تنگه هرمز هزینه بسیار زیادی بر اقتصاد جهانی تحمیل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/126364" target="_blank">📅 21:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سفارت ایران در بیروت اعلام کرده است که «لبنان قلب ایران است»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/126363" target="_blank">📅 21:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126362">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
در پی تداوم تنش‌ها، شرکت هواپیمایی «ایر فرانس» نیز به جمع شرکت‌هایی پیوست که پروازهای خود به مقصد اسرائیل را به حالت تعلیق درآورده‌اند.
🔴
شرکت «ایر فرانس» تمامی پروازهای خود به مقصد اسرائیل را تا ۲۱ ژوئن ۲۰۲۶ لغو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/126362" target="_blank">📅 21:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126361">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
قالیباف: هدف ما پایان جنگ و ایجاد امنیت پایدار است و نه عادی سازی روابط با آمریکا و اعتمادی هم به طرف مقابل نداریم. البته روش ما احساسی عملیات کردن یا صرفا اعلام حقوق ملت ایران یا محکوم کردن جنایات دشمن نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/126361" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126360">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
قالیباف: دست نیروهای مسلح برای اقدام همواره باز بوده و بر اساس تدبیر و برنامه ریزی درست و تصمیم تصویب شده عمل می کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/126360" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126359">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قالیباف: قرار نیست یا جنگ کنیم و یا مذاکره بلکه قرار است به وقت خود جنگ کنیم و به وقت خود مذاکره کنیم و اینگونه است که می توانیم دشمن را شکست دهیم و این که می گوییم مذاکره ادامه مبارزه است عینیت پیدا کند.
🔴
لازم است روی یک برداشت غلط خط بطلان بکشم، برخلاف تصور برخی که فکر می کنند بین مسئولان هماهنگی نیست، هماهنگی کامل برای رسیدن به اهداف میان مسئولان وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/126359" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126358">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
قالیباف: ماجرای لبنان نشان می دهد میدان دیپلماسی کنار میدان نظامی می تواند اسرائیل و دشمنان را کنار بزند.
🔴
نه دیپلماسی مانع عملیات نظامی است و نه عملیات نظامی مانع دیپلماسی است.
یک بار با تهدید به حمله و قطع مذاکره جلوی حمله اسرائیل به بیروت را می گیریم و بار دیگر با حمله نشان می دهیم ترسی از قطع مذاکرات نداریم و نتیجه این می شود که آنها مجبور می شوند عقب نشینی کنند و ما حق خود را تثبیت می کنیم.
🔴
تصور کنید اگر ما در میدان نظامی پیروز نشده بودیم یا در میدان دیپلماسی جلو نرفته بودیم و یا میدان های نظامی و دیپلماسی با یکدیگر به درستی پاسکاری نکرده و پشتیبانِ هم نبودند و با هم هماهنگی نداشتند، آن وقت دست ما برای حمایت از لبنان و مقابله با محاصره دریایی بسته بود.
🔴
موضوع فقط لبنان نیست بلکه موضوع رسیدن به حق مردم و ایجاد امنیت باثبات برای کشور است و باید هر ۴ میدان در کنار هم و هماهنگ با یکدیگر این اهداف را تأمین کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/126358" target="_blank">📅 21:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126357">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cb167517.mp4?token=IWAn8LDlFCGy1FqWXH0bHeuj-NZD0WFAVVdYbR0Fhzr67xcmR0F82HXSEPpSh9qWEjU8ZE7O09SJg8IxnheG4uZI9P1T8ghtUkMEtDRJcOVrjtRwAfzVy_fsyuxPLFOXgOpqOpezHobTHynh0ldV616IpsgSKqGHEtws_Tvptqza_fa8Tcq_3GCGgB4cjgoQ82b1bxz8JO2JAQiwSmA5Z2IO0peuK0InL10eja9usuKNAH_SsyYoa8tvSXXy9r4I6n7DBhJ-HCiWyKJQyFgIxELnyeNoHfESg_ZLbagwDxqJA83A--HX-eCoevs7Lnht7FqBUqoRGIrE16umJQdsiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cb167517.mp4?token=IWAn8LDlFCGy1FqWXH0bHeuj-NZD0WFAVVdYbR0Fhzr67xcmR0F82HXSEPpSh9qWEjU8ZE7O09SJg8IxnheG4uZI9P1T8ghtUkMEtDRJcOVrjtRwAfzVy_fsyuxPLFOXgOpqOpezHobTHynh0ldV616IpsgSKqGHEtws_Tvptqza_fa8Tcq_3GCGgB4cjgoQ82b1bxz8JO2JAQiwSmA5Z2IO0peuK0InL10eja9usuKNAH_SsyYoa8tvSXXy9r4I6n7DBhJ-HCiWyKJQyFgIxELnyeNoHfESg_ZLbagwDxqJA83A--HX-eCoevs7Lnht7FqBUqoRGIrE16umJQdsiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیرو های نظامی ایران خطاب به ترامپ:
عمو ترامپ با توئیت که نمیشه جنگ کرد، این ارتش و ناو و جنگنده‌هاتو بفرست خسته شدیم دیگه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/126357" target="_blank">📅 21:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126356">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کانال ۱۳ تلویزیون اسرائیل به نقل از یک منبع: نتانیاهو به وزرا اطلاع داده است که انتظار می‌رود اسرائیل به چندین دور از تشدید تنش با ایران بازگردد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/126356" target="_blank">📅 21:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126355">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
عراقچی: همسایگان ما در اولویت ما هستند
🔴
صمیمانه‌ترین تبریکات خود را به جناب آقای نیکول پاشینیان، نخست وزیر ارمنستان، بابت پیروزی حزبشان در انتخابات ابراز می‌داریم.
🔴
خوشحالیم که فرصت خوبی برای استمرار همکاری های سازنده در راستای تقویت روند پویای حاکم بر روابط ایران و ارمنستان فراهم شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/126355" target="_blank">📅 21:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126354">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
قالیباف: صحبت های رئیس جمهور آمریکا درباره یادداشت تفاهم، مخالف بخش های توافق شده بود که نشان داد آنها نه دنبال آتش بس هستند و نه دنبال گفت وگو و باید برای دفاع از حقوق ملت ایران پاسخ قاطع می دادیم که به لطف الهی نیروهای مسلح ما با اقتدار به وظیفه خود عمل کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/126354" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126353">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قالیباف: آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/126353" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126352">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
دونالد ترامپ مدعی شد که پنج کشور منطقه که در میانجی‌گری میان آمریکا و ایران نقش دارند، از او خواسته‌اند تا بر بنیامین نتانیاهو، نخست‌وزیر اسرائیل فشار آورد تا حملات را متوقف کرده و به سمت توافق حرکت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/126352" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126351">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به کانال ۱۴ گفت که: بازگشت به درگیری شدید با رژیم ایران «فقط مسئله‌ای در کوتاه‌مدت است، احتمالاً در روزهای آینده».
🔴
وضعیت هشدار بالا تا اطلاع ثانوی، هم از نظر دفاعی و هم تهاجمی، حفظ می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/126351" target="_blank">📅 20:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126350">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: فکر میکنم ایران مایل به امضای توافق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/126350" target="_blank">📅 20:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126349">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
حداقل ۳۲ نفر کشته شدند و بیش از ۱۰۰ نفر زخمی شدند در نتیجه زلزله قدرتمند با بزرگای ۷.۸ ریشتری که در سواحل مینداناو در جنوب فیلیپین رخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/126349" target="_blank">📅 20:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126348">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ به کانال ۱۲ اسرائیل: به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت
🔴
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/126348" target="_blank">📅 20:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126347">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ : اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن
🔴
من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه
🔴
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه
🔴
من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126347" target="_blank">📅 20:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126346">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
برخی کاربران مدعی شده‌اند که دارایی‌شان در چند صرافی رمزارز خارجی، به بهانه تحریم و بدون هشدار قبلی مسدود شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/126346" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126345">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سخنگوی سیاسی جنبش حماس مدعی شد ایران به این جنبش اطلاع داده که در حال انجام تلاش‌ های فشرده برای گنجاندن غزه در چارچوب یک آتش‌ بس منطقه‌ ای میان ایران و ایالات متحده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126345" target="_blank">📅 20:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126344">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rngKHK3Edc0LbG56WLyqO6RtwYyxFsiBCfFd_jvsx8OYUcXEIF0bF8fd58-xpFi5lRuQNLuDG7UnEOLnJVyPt7nWDOyS-9tfCLMVea144fKiiiPurwxQmhYsB_2kbvA9_25L0qDf8rfRKrsIaMcgAs1NKp9lZKPEOMNimHlCdMEebABaGdhlpTI8c8wFFjQaRCvK7WVKN_Bgk-UvQmVN2qzEDGm8A6j7kvifCtD4IqKLsReE0xXodWjsHZfcjrlyxPt4mYxgIe-cvqP6KEWVb75B5mUZEoltIdc5b6HN7IzfyphILX5NdcrPUTpjYAHY5_l2akxltKnjR7SLLsG7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت‌های عجیب هارد اکسترنال!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126344" target="_blank">📅 20:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126343">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd75eece7.mp4?token=E0Waky-53HGRT0soRlw5UusgLmCRx9GRBFEm3I9SyvhbeYyE1zvs4XgArlNKcbcTj6OyI7IHIhD1t3JU-Yh5g0xq-5iBuqtL1CHm5aNn9iGKY9sf81l6LbjYPbdq8SoBCeDUTVy3wIiP8DFORrdo6jGEAkhaYnAPmdXNqvTwRh-wDh20uFPHjGyS-GfspVyieu0HGXMnFicsG1OK3M_AB2QcjSAQb_mZFiemdtggw0j_5FOlvpsbCKUYbcGk1cEqxep-754UgtPC3Qx8Uuk3TT8EEQbaxtIk-b0D-6bDwRAsv_pP5HVjdYeuhTn2HRHTWLijs29UPIdJfaTCT7EtWIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd75eece7.mp4?token=E0Waky-53HGRT0soRlw5UusgLmCRx9GRBFEm3I9SyvhbeYyE1zvs4XgArlNKcbcTj6OyI7IHIhD1t3JU-Yh5g0xq-5iBuqtL1CHm5aNn9iGKY9sf81l6LbjYPbdq8SoBCeDUTVy3wIiP8DFORrdo6jGEAkhaYnAPmdXNqvTwRh-wDh20uFPHjGyS-GfspVyieu0HGXMnFicsG1OK3M_AB2QcjSAQb_mZFiemdtggw0j_5FOlvpsbCKUYbcGk1cEqxep-754UgtPC3Qx8Uuk3TT8EEQbaxtIk-b0D-6bDwRAsv_pP5HVjdYeuhTn2HRHTWLijs29UPIdJfaTCT7EtWIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل چند لحظه پیش ارتفاعات ملکخ در جنوب لبنان را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/126343" target="_blank">📅 20:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126342">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
روسیه از شهروندان خود خواست به اسرائیل سفر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/126342" target="_blank">📅 20:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126340">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4242e53622.mp4?token=KZnU7dKX_ObfyyjI7na9bd-oYE36wls43BH-cgd1NNSiwzPPsFQPmE_Xrvr4K7cdKFRcwn6UA8gDkPpqOh1RKa6Zl9jM8KuYfMfzd3JjqJiIeyEwdcmv_skUOskzyW8mATcDM8gcrsQvAjLiMQA047Kx1zhs05QwMIdN7cfrxRBnjTK35AIZvBAnc7wZHz4AY_B9uu8CdWpx-bNMdXQDNImzGRoDkTkEYxQ2cRKTnR9XzKfDt9iXTWlkzjVsilKyqCnhEcrR61WOTyv8Q7kIzNdJEDf6rn9o4HDKMRv_hPUZniNsGm5k7f_Yqq4SoOKA8OM55MqWvnnNybC9AL879Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4242e53622.mp4?token=KZnU7dKX_ObfyyjI7na9bd-oYE36wls43BH-cgd1NNSiwzPPsFQPmE_Xrvr4K7cdKFRcwn6UA8gDkPpqOh1RKa6Zl9jM8KuYfMfzd3JjqJiIeyEwdcmv_skUOskzyW8mATcDM8gcrsQvAjLiMQA047Kx1zhs05QwMIdN7cfrxRBnjTK35AIZvBAnc7wZHz4AY_B9uu8CdWpx-bNMdXQDNImzGRoDkTkEYxQ2cRKTnR9XzKfDt9iXTWlkzjVsilKyqCnhEcrR61WOTyv8Q7kIzNdJEDf6rn9o4HDKMRv_hPUZniNsGm5k7f_Yqq4SoOKA8OM55MqWvnnNybC9AL879Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیستم پدافندی اوکراین پهپاد انتحاری روسیه رو مهندم میکنه، حین سقوط مستقیم میره میخوره تو یه ایستگاه اتوبوس
🔴
دو کشته و ۱۲ زخمی گزارش شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/126340" target="_blank">📅 20:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126339">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9417287cba.mp4?token=HGm5vt9taDJezxsd0DWvwPgA132TqW-kaKpUsF-lhIZCtsww3o34lhWqr8SsSny-bweFBK3VRmFsNb3-ZKaL8oMKWobAaGGAtBOYm-ZxZ9SpLRg3n1egWvm-zieWZuqu1p8yXkOkAn0YdYWTT2dYGb-HLQZYhHlrPltGrNdjg8TIGZ3nhookSPtZ-hs-1TixoaRx9wEqcNrOChFeLmTNo6A0jmB0RBcq66hHWYayoKGDzU0akj3H9Kd2XT2NXi1PP0FW45cSpd3B0ZJataULhuLo8pyDlvWEUnrn31R8T6ppMf-6stMp8QV3MkaCqcgenJBnq_tvt9vsxY4EVdDtADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9417287cba.mp4?token=HGm5vt9taDJezxsd0DWvwPgA132TqW-kaKpUsF-lhIZCtsww3o34lhWqr8SsSny-bweFBK3VRmFsNb3-ZKaL8oMKWobAaGGAtBOYm-ZxZ9SpLRg3n1egWvm-zieWZuqu1p8yXkOkAn0YdYWTT2dYGb-HLQZYhHlrPltGrNdjg8TIGZ3nhookSPtZ-hs-1TixoaRx9wEqcNrOChFeLmTNo6A0jmB0RBcq66hHWYayoKGDzU0akj3H9Kd2XT2NXi1PP0FW45cSpd3B0ZJataULhuLo8pyDlvWEUnrn31R8T6ppMf-6stMp8QV3MkaCqcgenJBnq_tvt9vsxY4EVdDtADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب الله تصاویری را منتشر کرد که نشان می دهد جنگنده های آنها یک تانک مرکاوا را در مجاورت قلعه بوفورت در جنوب لبنان در 4 ژوئن با استفاده از یک موشک هدایت شونده هدف قرار می دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/126339" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126338">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت خارجه ایالات متحده فروش احتمالی ۱.۹۸ میلیارد دلار سلاح به کویت برای سیستم‌های ضد پهپاد و تجهیزات مرتبط را تایید کرده است.
🔴
این بسته شامل پلتفرم‌های ضد پهپاد رودرانر و آنویل، جعبه‌های پرتاب، سیستم‌های فرماندهی و کنترل لاتیس، برج‌های نگهبانی برد بلند و دریایی، سیستم‌های جنگ الکترونیک پالسار، مراکز عملیات تاکتیکی، به همراه خدمات پشتیبانی و آموزش مرتبط است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/126338" target="_blank">📅 20:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126337">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام آمریکایی: نیروهای آمریکایی به رهگیری موشک‌های شلیک شده توسط ایران به اسرائیل کمک کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/126337" target="_blank">📅 20:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126336">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
گروسی در پاسخ به سوالی درباره ۱۷ حمله به تاسیسات اتمی ایران: من در این باره چیزی برای گفتن ندارم.
🔴
نماینده ایران حق دارد اعتراض کند اما من با آن‌ها موافق نیستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/126336" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126335">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
آی۲۴ نیوز عبری: هدف حمله اسرائیل به پتروشیمی کارون در ماهشهر، مختل کردن عملیات و توقف تولید این مجموعه بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126335" target="_blank">📅 20:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126334">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سنتکام: یک نفتکش مرتبط با ایران را متوقف کردیم
🔴
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی در ۸ ژوئن یک نفتکش خالی را در خلیج عمان، پس از آنکه این کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، محاصره مداوم علیه ایران را نقض کرد، از کار انداختند.
🔴
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچم پالائو را هنگام عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران از کار انداخت.
🔴
یک فروند جنگنده F/A-18 Super Hornet از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از آنکه خدمه از دستورالعمل‌های نیروهای آمریکایی پیروی نکردند، یک مهمات دقیق به سمت فضای مهندسی و هدایت کشتی شلیک کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/126334" target="_blank">📅 20:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126333">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رادیو اسرائیل: ارتش اسرائیل در ساعات اخیر در حال آماده‌سازی موج بزرگی از حملات هوایی علیه ایران بود، با ده‌ها جنگنده نیروی هوایی که قرار بود به اهدافی در سراسر کشور حمله کنند
🔴
با این حال، این عملیات گسترده در نهایت انجام نشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/126333" target="_blank">📅 19:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126332">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1tR4NwArXDWZd3CiC5kw9Zhztlfid8bDjjHFqWeURxUbOKGeYa_iiRrvI6Z_fkDt0LHHY6WS_eHE5dWY0FH7Snafe0HPpQyWcJWAZcXByxWx2mQQ9kX5-7aRqzZWHkwb4scXF1k-ZKYr1cUTMdDda457sZn6v65jvsrN73G6MEAidXWUtNl4IbuSVCHgYq64aaL3M48Slkd41B5BgPbFVLA9RDXVZcaqBiE3F4LoMiRfz2gy6zHyCN8iDQBo0qqDxglCcrRLaubJmi9Ii0ziT3oNckdj5MSMVVdUYJ-lOnJHt-lK3Fs8IdQO6QY_Z33ila2RXWUlcUEQtjrVrcbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک این از جنگ هم بدتر بود
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/126332" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126331">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpMxSVYIG5xsmcIBb3-kyUdV2skFyv5xb3q0Zg9m_vkhj-WW75xQSsvGlvmk7-AtLot5WFEzLdSQmJY5BKBPYQBBVRNoMimexIpgNysSopA-vpNBCRTMxGvlQuoE4-llWE57EBL0MkmCQAM7GkB6PSyYDbedSkWta1XoJB7ppY0PDtf9b1zM_hfoFjSZPF-F7AxPqeO3FM9azsYhPc4OpmxKyoXNsDMc78jZc8uMoV07SrYn5Aqg9ppXdjxs_8Rf0Z8JDNw_zNCfogvoC5rfV5Oe2mDro5nUgVphIICSSY809MxW8qQ_NxLF1plAHJhaXg8e2QMAINgEPNNvAyVZXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/126331" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126330">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4446250ba8.mp4?token=LQ8HFVBE93Rn8kogGuF6g5rvfehhf8gu6tbh6TiuvaU9w0aZR5_RcE-97XxxhaR6XtEG_qJqi0MknPDXyohGsN3vL_Wh9xzu6wvBCbsaRZwxBjEeTSb-4WCgMpm9rMYCLHaRXH3KZ2L0TVhg6WcCufJLZDm5gy4z3314boyhvbInDudv2gZC7GCoNJ_Ot7i3HoHwAms8QekI4A4zejD6Zfg3BP-tUGMxUL0mwpb-aEfzf74li5sZArEG6pnRu8kwOAb9qt7UELAV6_ebnDsGw6H6wa1p0816v-CZf4UID79n07z_TIhYPSBt16RLB1J3VnRG9Jd0iCgTJP1NBxQ1CAZWADgdqLJb-sJ8DTeXP4RqjuH9bbRAQh5EeR-lwFpBAEcmFn95CMtYftu3w-uLHBG17iSve10ri1oIGiteQEAQOoSDL4hGR0LqC5SV-D8f110z2BlU0qCp8oCTs1OOtnpot5dKLTU2lG7FOnXq7dK6xKPwt3wntz73nHH5w7FKJXqgGzTTSfb90BftOhutsEH9AUPnbeIht3oNmsfPLEcwrP3h3q6w05LN2pCAgjP7Cs_ixEGUPv7rBqdvsfC5xlGFHQEQQRGEwLMr9NbvXcwNVw5CpXr9m3vKjFv7EVcbwN-Lmglj_CheuaS_fSltc4ZhsoLpEuWHee6Mo6tcMRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4446250ba8.mp4?token=LQ8HFVBE93Rn8kogGuF6g5rvfehhf8gu6tbh6TiuvaU9w0aZR5_RcE-97XxxhaR6XtEG_qJqi0MknPDXyohGsN3vL_Wh9xzu6wvBCbsaRZwxBjEeTSb-4WCgMpm9rMYCLHaRXH3KZ2L0TVhg6WcCufJLZDm5gy4z3314boyhvbInDudv2gZC7GCoNJ_Ot7i3HoHwAms8QekI4A4zejD6Zfg3BP-tUGMxUL0mwpb-aEfzf74li5sZArEG6pnRu8kwOAb9qt7UELAV6_ebnDsGw6H6wa1p0816v-CZf4UID79n07z_TIhYPSBt16RLB1J3VnRG9Jd0iCgTJP1NBxQ1CAZWADgdqLJb-sJ8DTeXP4RqjuH9bbRAQh5EeR-lwFpBAEcmFn95CMtYftu3w-uLHBG17iSve10ri1oIGiteQEAQOoSDL4hGR0LqC5SV-D8f110z2BlU0qCp8oCTs1OOtnpot5dKLTU2lG7FOnXq7dK6xKPwt3wntz73nHH5w7FKJXqgGzTTSfb90BftOhutsEH9AUPnbeIht3oNmsfPLEcwrP3h3q6w05LN2pCAgjP7Cs_ixEGUPv7rBqdvsfC5xlGFHQEQQRGEwLMr9NbvXcwNVw5CpXr9m3vKjFv7EVcbwN-Lmglj_CheuaS_fSltc4ZhsoLpEuWHee6Mo6tcMRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان با دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، در استانبول دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126330" target="_blank">📅 19:50 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
