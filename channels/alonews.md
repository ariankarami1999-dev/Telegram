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
<img src="https://cdn4.telesco.pe/file/kj6FYt6MiYv7UqQB4ePZW9H_3yEoLRJgCBIdHqn3kTJs5IFDgp2OHNgxxg5RsFzbx7xy0bA-bU-GMWs90JvYR6OwotU_ikfSgWts4mpDlxjyR_8B_HbcFOpo74MAnpvd90n9iNCKP5HfMmgl281Jlz1_RjZCkqJzdYywyI0roVA4fiA7Vp7Ztf9kP9diPl_jwjk6BtB4QJfN4N5uwtoC81e2WVBnJITraTs02ybrJ662ek-InhaSAo2jPJW_FaWVeuk0uPrX1o6Omb5mVC8Eaw1cjoA7xhqPUhiNFC9Ewy8eDXDAQtLlFQjIKP4Jg--gkjcO40YBQMzgwH9wgi7MEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 948K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 14:16:55</div>
<hr>

<div class="tg-post" id="msg-121054">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGWWAwCiKUwEwT7t1CtEOC5Q0Og3HsyE8FGu37xTj_-2xT2_MjL5X0R3CvxfADiEVWcKvBuDnPvmaH2JTSWaUEsryuv7wKQF39GRrQ6z120TvdJpzjZ-6oIEEyMVUYdqsZkueelG7NyIOXZ7xo75tn143Rq3oNXVAwY9RUIT5YdCe9ZDTQm3BGGCdPr1pFBzvVL4pLpmEYDWiwxScYhQTLnycmXUpTC2Kc46LFf9J0EgLjYGGvo56H58gkk2COlTvViLnET5_DgyX_EySexC4F-E2V2R8n9W2-lFNkroXuVf-kGI9ipEqDNVp-fh8B04mPT8mKi8qaHg-6lgY2Zljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت هوای اهواز امروز ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/alonews/121054" target="_blank">📅 14:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121053">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
امتحانات مدارس در البرز غیرحضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/alonews/121053" target="_blank">📅 14:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121052">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17b16a4f1.mp4?token=BhAxBbux5JLEVQ6ftY5Nia_sSsORuI5jhK2U6Hi6GLlCGnuBu2i9dX28afHkfi8kmRJspIAWKCcdEyNtndJYvsXwdYOu0iNB5xlfzBce2jV_lp1RePqnaWvn33UrvvwFcHszSIy5q4iUeKUuEYPtjtEmopkXyNtYBTolwV_Ju9wvtO4dA5Kmb0PzxQfEqufq5sNo5j8mf-s4Esy-C3JaZOFDR58_g0-OSyYgjFr_0Z3-y4F9S7LzM9JjHSHYfUEATbQLaMoMcxWWNponHFkUA8pHsuL3zCOUeHnt4X1BPJS-9psfsnMBZM_pepdD9m7p2OBdcMEwzz2QEcKG7OYcwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17b16a4f1.mp4?token=BhAxBbux5JLEVQ6ftY5Nia_sSsORuI5jhK2U6Hi6GLlCGnuBu2i9dX28afHkfi8kmRJspIAWKCcdEyNtndJYvsXwdYOu0iNB5xlfzBce2jV_lp1RePqnaWvn33UrvvwFcHszSIy5q4iUeKUuEYPtjtEmopkXyNtYBTolwV_Ju9wvtO4dA5Kmb0PzxQfEqufq5sNo5j8mf-s4Esy-C3JaZOFDR58_g0-OSyYgjFr_0Z3-y4F9S7LzM9JjHSHYfUEATbQLaMoMcxWWNponHFkUA8pHsuL3zCOUeHnt4X1BPJS-9psfsnMBZM_pepdD9m7p2OBdcMEwzz2QEcKG7OYcwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی شورای شهر تهران: از فردا مترو و بی‌آرتی در تهران رایگان نیست و مهمونی بسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/alonews/121052" target="_blank">📅 13:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121051">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
امتحانات مدارس در البرز غیرحضوری شد
معاون آموزش متوسطه اداره کل  آموزش و پرورش استان البرز:
🔴
با تصمیم جدید شورای تأمین استان، امتحانات در استان البرز بار دیگر به صورت مجازی برگزار می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/alonews/121051" target="_blank">📅 13:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121050">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فارس: تخم‌مرغ از ۵۵۰ به زیر ۴۰۰ هزار تومان سقوط کرد، اما مرغ گرم از کیلویی ۳۸۰ به ۴۵۰ هزار تومان افزایش یافته!
✅
@Aloanews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/alonews/121050" target="_blank">📅 13:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121049">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt1Av4VTaXkCMu3R2Excn6mgd6fJKKpliMuSDhH4r5ZpKi5mdty-amK-HWpHYd_IxefF1OP6pwyVzwmshenSSeEF_MpbPvMOEAZnPJimb9yRKroDMP4a2XAkehtTBc2lRPYPRH6qKRi_lsI9MqxvdsRuxOmiBElHkjmp94oc0mkKhDHVi1zeCj85LX-Ck5boFFVRq3gLxEcbuSSCT2NKIbOrrpABjkirctCT66ul7tGeu2fg0WW4tdRmOhDoNQC_aCuJK75b0kYQYk3TTyCoO_sSYnpXWGFAqU75QENzdjTC3MHyuqlBbkS9eokJGRVvo8GyQty0RLYOwJedBK2NiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس اولین روز بعداز جنگ را مثبت تمام کرد
🔴
شاخص کل بورس در پایان معاملات امروز با رشد 2500 واحدی به 3 میلیون و 716 هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/alonews/121049" target="_blank">📅 13:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121048">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f98735351.mp4?token=UB-r3daWX05uHPt5VwYkHH9NxB6XJBOrgDJZ4g528la8bE6nYJGvklqpbKVYrCr27hgcwF4kvP14Qv4J3lp8nlvuji8SmKw-q0EMtKAWcaR9qmrml3ecymq3Xln26m9iT9EZqebYeZwCWxPt6TIrh6Z2-6Wpdf9P4kEkHCdA3H2hGrph9SeOr9y1k31AuiC1NBZlVsGTq5HUbN3mvQvZPGx4DvTrIkKn7W5wziFu-G00HruAWb2r-NDwHsbnDY8hyEUwZDm0aTKIjOeSoc4YsNuNbf4Y5B20DLGJgEet3B8jOmJrahGJaGGxep5aWQsaNR7Hyt8QEKX19zwKKvDIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f98735351.mp4?token=UB-r3daWX05uHPt5VwYkHH9NxB6XJBOrgDJZ4g528la8bE6nYJGvklqpbKVYrCr27hgcwF4kvP14Qv4J3lp8nlvuji8SmKw-q0EMtKAWcaR9qmrml3ecymq3Xln26m9iT9EZqebYeZwCWxPt6TIrh6Z2-6Wpdf9P4kEkHCdA3H2hGrph9SeOr9y1k31AuiC1NBZlVsGTq5HUbN3mvQvZPGx4DvTrIkKn7W5wziFu-G00HruAWb2r-NDwHsbnDY8hyEUwZDm0aTKIjOeSoc4YsNuNbf4Y5B20DLGJgEet3B8jOmJrahGJaGGxep5aWQsaNR7Hyt8QEKX19zwKKvDIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌ی ارتش اسرائیل از صبح امروز، به لبنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/alonews/121048" target="_blank">📅 13:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121047">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW3G4iZJfxqUaR2OqR3CPPiMzEqnHLVYeuE6fJdqSfyvnfZ9R4d4AOT1Ivvd_XZzXYnvcVMLg6lW1T49tKcm5e6VyiAEdJaukVDR2i_MjFD4xYgDNz4e6awYWzYs7viggj2j84f9dZZSfBhWyf9hcF1rSv6dsPZPGEZOseStFhqRN8CgAuQA3p3dO_vE9YOGV88wQp3MJ7Vjks8YEAqGSfOBp1chskkau7Sdq_j0YMeQbZ_x-QZ4otoUaAOJH7oGXnUU6kGKxcyypzFpva8LeVJtiE7Cs63UFfLaXci28og3QgGbwZQA3vrXo4WxZqOFsC2zLp6KvLJmZMeckMDaiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه واشنگتن پست به نقل از یک مقام پاکستانی: ایران می‌خواهد پیش از اعلام توافق هسته‌ای، به توافقی برای پایان دادن به جنگ دست یابد.
🔴
واشنگتن می‌خواهد توافق بر سر همه مسائل را یکجا اعلام کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/alonews/121047" target="_blank">📅 13:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121046">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی ارتش: ارتش ایران، دوره آتش بس را به منزله دوران جنگ تلقی کرده و از این فرصت برای تقویت توان رزمی خود استفاده کرده است.
🔴
اگر دشمن حماقت کند و مجدداً در دام اسرائیل گرفتار شود و دست به تجاوزی دیگر به ایران عزیز ما بزند، با ابزارها و شیوه‌های جدید جبهه‌های جدیدی را علیه آنها خواهیم گشود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/121046" target="_blank">📅 13:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121045">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
باید ایستاده برای این مرد و سخنرانیش دست زد.
🔴
تامی رابینسون از روز اول کنار مردم ایران بوده اما امروز سنگ تموم گذاشت و درمقابل ده‌ها هزار نفر از انقلاب شیر و خورشید حمایت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121045" target="_blank">📅 13:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121044">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
اتحادیه اروپا کشورهای حامی روسیه یا ایران را به قطع کمک‌ها تهدید کرد
🔴
طبق گزارش یوراکتیو، کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا، کشورهای در حال توسعه‌ای را که از روسیه یا ایران حمایت می‌کنند، به محرومیت از کمک‌های اتحادیه اروپا تهدید کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121044" target="_blank">📅 13:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121043">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
صدای شنیده شده در دزفول مربوط به تست سامانه پدافند بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/121043" target="_blank">📅 13:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121042">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر دفاع پاکستان : احساس می‌کنم جنگ ایران از سر گرفته نمی‌شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/121042" target="_blank">📅 13:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121041">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نشریه AFP : همزمان با سفر پوتین به چین، روسیه قصد داره رزمایش نیروهای هسته‌ایشو برگزار کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/121041" target="_blank">📅 13:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121040">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
منبع نظامی ایرانی المیادین: ایران تاکتیک‌های جدید مبتنی بر «دکترین دفاعی تهاجمی» آماده کرده و هیچ مشکلی برای دفاع از کشور ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121040" target="_blank">📅 13:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121039">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm8AI5zp9bqsx97jd7vxWsluAsOw_yQOTb0StRN3ZTG8XjjCnL-OBjIwDkO5JhmACqJrljsOrxuufJMkKlN1-uCsOj_1_8BqYc585rbWp8eswGdi-b26TixTVuwZlurQ7c57B5DWMVgB9eNk6OLdRSXnsdNp6ZAjbGYqLE_uAWbeXvp8Hy808HPaabDRHfvLZ6so8g7v7AIq29QTDNDXwzb0GkaKQLCb6gPVO2drWXhcQ4p7SN-ohARbzJqnY3gCRvZbMiPzpc6bcrLV9QoMq8y4zWJEnYZjQGZfaTItop9hsE8hUUKzdvD1_AuaNUp_fuYJZCsYp1hWSxvzQfJqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس شرکت میهن: جوانان الان گشاد هستن و کار نمیکنن بعد میگن اوضاع جامعه خرابه
🔴
منم جوون بودم و زحمت کشیدم ولی الانیا چی؟ تنبلن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121039" target="_blank">📅 13:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121038">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-_ItyDA_fCok79bJJMh41cTCXA4yEDXrtZ9Gv1lvee2FJZH0tOVQftsLO1M42WnE7iCYoFOpfbM3hZDN1BbJJhCsIzycEsg3JlDAR_DPQolNITnix9KeQno4S5yykWHPoz28ucJtKkTEgQiXqzkxsGLLw8Mau0cP40eQ1HRnrE1K5bqOCmDZfoEXUO8EYT8-e0zSbCCDzNTRTT-cFIA94gKygXLqu_gOCnzjjCN25fuHF8gIkhkQFjhl0VIb7aCMQQx6iECrilQPCAHFTtc0-lyNY7pH1pM1wLbDBd8qfK7Zv069Odw8V2WemTFRFLmo1QvJPA2Rez94aRO5O0Raw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرعامل صندوق قرض‌الحسن جهاددانشگاهی:
به دانشجوهایی که ازدواج کنند ۳۰ میلیون وام تعلق می‌گیرد
😍
😍
😍
😍
😍
😍
😍
😍
😍
😍
😍
😍
😳
😳
😳
😳
😳
😳
😳
😍
😍
😍
😍
😍
😍
😍
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/121038" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121037">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
منبع نظامی ایرانی به خبرگزاری ریانووستی: ایران تاکتیک‌های جدید مبتنی بر «دکترین دفاعی تهاجمی» آماده کرده و هیچ مشکلی برای دفاع از کشور ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/121037" target="_blank">📅 12:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121036">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
از فردا (چهارشنبه ۳۰ اردیبهشت) پرداخت بلیت مترو و اتوبوس در تهران به حالت عادی و پولی بازمی‌گردد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/121036" target="_blank">📅 12:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121035">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ هنوز تمایل به حمله به ایران دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121035" target="_blank">📅 12:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121034">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
به دلیل مسائل امنیتی؛ دادگاه نتانیاهو امروز کوتاهه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121034" target="_blank">📅 12:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121033">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ایران ابتدا به پیشنهاد آتش بس ۴۵ روزه پاسخ منفی داد ، بعد به آتش بس دو هفته ای آری گفت.
🔴
۱ خرداد، میشود همان ۴۵ روز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121033" target="_blank">📅 12:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121030">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8699847b18.mp4?token=D752L_4CIgbAwujwGONhf5KdEf2N8chYuFJeLR-ReoxBg1b0C2JKdSzRKty1SyeJ9YJmOIGn8QxuIvk1swT7ivDfR7Yax2dGJiTiE9MjRZ_Mu1VHxQMh7rtCGn26NCDgHMlQWbPVrmt0AfgTFcpKMsEPGfhBe6bi5kVk_yUliFuUpVDDDiDx85YGI11PHO1peymtXb8T6kqW93D8g5J85VNphft1xh9GoIdkMtLUwYSyN7JeOU622BPYZpiLkUMoHZSYlBdKDSSTFHsvJgppnTtAT1Xg0i-o7Ljra-2AbUzUwWbiOEIlbW9PJqHv1uiPNHWe-mNh8Eiku90sfSLLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8699847b18.mp4?token=D752L_4CIgbAwujwGONhf5KdEf2N8chYuFJeLR-ReoxBg1b0C2JKdSzRKty1SyeJ9YJmOIGn8QxuIvk1swT7ivDfR7Yax2dGJiTiE9MjRZ_Mu1VHxQMh7rtCGn26NCDgHMlQWbPVrmt0AfgTFcpKMsEPGfhBe6bi5kVk_yUliFuUpVDDDiDx85YGI11PHO1peymtXb8T6kqW93D8g5J85VNphft1xh9GoIdkMtLUwYSyN7JeOU622BPYZpiLkUMoHZSYlBdKDSSTFHsvJgppnTtAT1Xg0i-o7Ljra-2AbUzUwWbiOEIlbW9PJqHv1uiPNHWe-mNh8Eiku90sfSLLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم آتیش‌سوزی‌های جنوب کالیفرنیا؛ آتیش با باد شدید پخش شده و باعث تخلیه بیشتر از ۲۳ هزار نفر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121030" target="_blank">📅 12:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121029">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipkDtfgjTgr2qHeMDc9Rxb9jrGGv6l7u0FSl-Cys-kgyYWgtK-UiDxOjEU0AyQOQH6N1ZMF0XfDwerG-1PmNXSeP1hlMYDboJISjM0HpR5F008GrTFn6OQKjj11h2GN-TemLMlfmhyfEzgclZMFpyM-Kqo0zOJE4G4dijN0rl8e48paLnbn4Hr1n6x_i4ANsLcQ9WR-WnF_UzIchKjDI6D1IfbhLcxHOXKtxOwwV04WA2EiILjrqLA5nAUGbdml33fuEswgyQf_70RE-m2JoTagPEDZO4zhgyRLl4hZC_x0GgyW7AF4TvEkCwbxUh7aShwmalrEP0Atc1QwOUPicFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پائین‌ترین پینگ‌ها رو با ما تجربه کنید
✔️
🔄
کانفیگ‌های استارلینگ با پشتیبانی 24ساعته و لینک ساب
🔄
💯
مورد تایید مجموعه الونیوز
💯
📌
تحویل زیر 1دقیقه
📌
بدون هیچ گونه قطعی
💰
خرید آسان و سریع
⬇️
💎
@FastProxyMakerBot
💎
@FastProxyMakerBot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121029" target="_blank">📅 12:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121028">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی اعلام کردند یک هواپیمای دولتی اسرائیل لحظاتی پیش به سمت ابوظبی پرواز کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121028" target="_blank">📅 12:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121027">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رایزنی وزیران خارجه قطر و ترکیه درباره تحولات منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121027" target="_blank">📅 11:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121026">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
روزنامه واشنگتن پست به نقل از یک مقام پاکستانی: ایران می‌خواهد پیش از اعلام توافق هسته‌ای، به توافقی برای پایان دادن به جنگ دست یابد
🔴
واشنگتن می‌خواهد توافق بر سر همه مسائل را یکجا اعلام کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121026" target="_blank">📅 11:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121025">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نیویورک‌تایمز نوشت: در صورت ازسرگیری جنگ، ایران ممکن است تاکتیک‌های جدیدی به کار گیرد. ایران ممکن است به دنبال اعمال کنترل خود بر تنگه باب‌المندب باشد. در هر دور جدید از جنگ، ایران ممکن است روزانه ده‌ها یا صدها موشک شلیک کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121025" target="_blank">📅 11:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121024">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
بر اساس گزارش‌های نیویورک تایمز، دونالد ترامپ تصمیم گرفت حملات نظامی بیشتری به ایران انجام ندهد، تصمیمی که عمدتاً تحت تأثیر هشدارهای پنتاگون بود که تهران در حال موفقیت در تطبیق با استراتژی هوایی آمریکا بود.
🔴
مقامات دفاعی آمریکا اشاره کردند که فرماندهان ایرانی مسیرهای پروازی و روال‌های عملیاتی جنگنده‌ها و بمب‌افکن‌های آمریکایی را به دقت تحلیل کرده‌اند. این مطالعه تاکتیکی عملیات هوایی آمریکا را به طور فزاینده‌ای قابل پیش‌بینی کرده و به طور قابل توجهی توانمندی‌های سامانه‌های دفاع هوایی ایران را افزایش داده است.
به عنوان شاهد مستقیم این تهدید رو به افزایش برای هواپیماهای آمریکایی، مقامات به دو حادثه اخیر اشاره کردند: سرنگونی یک فروند F-15E استرایک ایگل و آسیب دیدن یک جنگنده پنهانکار F-35.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121024" target="_blank">📅 11:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121023">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cfd4a7e.mp4?token=mbW7VtQkGeXQcmEuSawcu1rv4108N9wCuFN9TVaxKowezNvfnVlIswDEqagLpIqNn4nkGPLl2fVHaRjZhDcOyqC6CtzY6mgKjx1ata0-XDiDBd7q_In9Xw2Rrf3gGL1XHL8OYu2klkZsM2oEBRWXZpXVtoEO2plJAj0My_uiC5tkdm4edFPeHxCmu81EEpQpDgW_vy05LEYUYyfb1kCdIj0hc6GowC3ljkO7N-339YurW1zCS1RI3J4eWRTJMHtHsLErpT0aPSc09FER0nyOo26VRS5wbOFG553JcgbMhRUv1RIDw-NGkx7oy5_nOfiniXxKN3y_BLyXSHRmjP712A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cfd4a7e.mp4?token=mbW7VtQkGeXQcmEuSawcu1rv4108N9wCuFN9TVaxKowezNvfnVlIswDEqagLpIqNn4nkGPLl2fVHaRjZhDcOyqC6CtzY6mgKjx1ata0-XDiDBd7q_In9Xw2Rrf3gGL1XHL8OYu2klkZsM2oEBRWXZpXVtoEO2plJAj0My_uiC5tkdm4edFPeHxCmu81EEpQpDgW_vy05LEYUYyfb1kCdIj0hc6GowC3ljkO7N-339YurW1zCS1RI3J4eWRTJMHtHsLErpT0aPSc09FER0nyOo26VRS5wbOFG553JcgbMhRUv1RIDw-NGkx7oy5_nOfiniXxKN3y_BLyXSHRmjP712A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت شناورها در تنگه هرمز؛ هم‌اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121023" target="_blank">📅 11:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121022">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یک عضو هیات رئیسه مجلس: انتخابات هیات رئیسه مجلس هفته آینده برگزار می‌شود و به هیچ وجه به تعویق نخواهد افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121022" target="_blank">📅 11:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121021">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
منابع روبیکایی: ده‌ها مقام اسرائیلی در طول جنگ ترور شدند اما سانسور کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121021" target="_blank">📅 11:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121020">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOaI7QUwLke8vbp2-vWMNH_Iih5OsnLp5Gl03A8PTlUFqF3tT6NTXYcETviM9CW6gvtpbRKAqlwFpod4EDeMgOUlGroappbzOUoOsK1OHi1cxU0kO8dmzO0WXhdqVqdXeWkCQ82IYQ2HUH1EezLtBDvNovTTrCXZANLguou9v-3tRCqlDI1wt1awbhyK6BnCs76lWtphjlAOy3I0JuHPvfU2x5z6y_D4yg8db8kYdF76MY_D5EFNYUfs4cvYoKDB-gBSGCPXytj82Fp-rMGQ8Nronlydlh8cwEkWwT9o8gOM3Tf_cu-SFc4gohMrdt9Ex92KanHKS_aFxq453fYZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وحید جلیلی، داداش سعید جلیلی و قائم مقام صدا و سیما: باید رسانه ملی تبلوری از یک مسجد باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121020" target="_blank">📅 11:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121019">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
الجزیره: طلا پس از اظهارات ترامپ کاهش یافت
🔴
قیمت طلا امروز، سه‌شنبه، کاهش یافت؛ در حالی که بازارها در انتظار تحولات بیشتر پس از لغو حمله‌ای بودند که قرار بود توسط رئیس‌جمهور آمریکا، دونالد ترامپ، علیه ایران انجام شود.
🔴
قیمت طلا در معاملات نقدی ۰٫۵ درصد کاهش یافت و به ۴۵۴۶ دلار برای هر اونس رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121019" target="_blank">📅 11:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121018">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
فیلم نشان می‌دهد که کماندوهای نیروی دریایی ارتش اسرائیل در اواخر روز دوشنبه یک کشتی ناوگان جهانی سومود را در آب‌های بین‌المللی تصرف می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121018" target="_blank">📅 11:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121017">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سازمان بهداشت جهانی: نگرانی بزرگی در مورد گسترش سریع ویروس ابولا داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121017" target="_blank">📅 11:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121016">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
معاون وزیر امور خارجه ایران: لغو تحریم‌ها، آزادسازی دارایی‌های مسدود شده و پایان محاصره در پیشنهاد اخیر ایران به آمریکا گنجانده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121016" target="_blank">📅 11:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121015">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
بر اساس آخرین سرشماری، جمعیت ایران به ۸۶ میلیون و ۵۶۴ هزار نفر رسید که ۴۳ میلیون و ۶۵۸ هزار نفر مرد و ۴۲ میلیون و ۹۰۶ هزار نفر زن هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121015" target="_blank">📅 11:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121014">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در کانال
#الونیوز
به کانال زیر مراجعه کنید
👇
📃
https://t.me/ads_alonews
📃
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121014" target="_blank">📅 10:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121013">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
کانال ۱۲ رژیم عبری: اسرائیل پیام‌هایی از آمریکایی‌ها دریافت کرده است که ده‌ها هواپیمای سوخت‌رسان مستقر در فرودگاه بن گوریون (۷۸ هواپیما) به نظر می‌رسد حداقل تا پایان سال در تل‌آویو باقی بمانند.
🔴
وجود این هواپیماهای وابسته به ارتش آمریکا مشکلات زیادی در بهره‌برداری از فرودگاه ایجاد کرده است، زیرا بیشتر فضاهای موجود در فرودگاه بن گوریون توسط آن‌ها اشغال شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/121013" target="_blank">📅 10:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121012">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
معاون وزیر امور خارجه ایران: لغو تحریم‌ها، آزادسازی دارایی‌های مسدود شده و پایان محاصره در پیشنهاد اخیر ایران به آمریکا گنجانده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/121012" target="_blank">📅 10:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121011">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl2txsYjDz-aCZFCoiBqBYhuV9YJA64ezl3Yof6-uVOWAXuP6gOLoID74o1F7JovNMgIJpqrmSpXQiVDVH9UFTHLuXYJ8A26e4rlFqONmLQtsbCA6xCEckouGv7ZtLZmiNRxtBkL7JLtwEmEdwDajqWctQEVcIeN6tY87-8fArjoWMwCA1y8C4jWzjLAS0ICsARhr88Tg6jEbnX23RAOxpUXHqC2oLQ57nMW62IuVL5KFU3rPzXlKB8hZkyiW8HZspWF_2uaGtE6DfJIhfjvmvBieONGQHPXlvDrfTJcAtggQZZa9zMb3uwgtYPpSIl-ZBWs9ItcYpTx6R2tFnTKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت سفارت ایران در سیرالئون:
آمادگی ترامپ برای حمله به ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/121011" target="_blank">📅 10:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121010">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
پدافند جزیره کیش فعال می‌شود؛ مردم نگران نباشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/121010" target="_blank">📅 10:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121009">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ایالات متحده بیش از ۸۵ میلیارد دلار در طول ۷۹ روز برای عملیات نظامی خود در ایران هزینه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/121009" target="_blank">📅 10:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121008">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
شبکه عبری کان: پهپادهای حزب‌الله ۸۰ درصد عملیات ارتش اسرائیل را محدود می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/121008" target="_blank">📅 10:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121007">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPWG3_nAXE9fPQdFvIZcGNNQCuhTS0sL4ruTlzkWn5PdsmlTVSenLOX-UH-jzOxkWgtcF5ZP0447buJr4gUZl_qXdezraz2Eg2VJNaNIiY6JweK6FCpOB_USvsIErJjFRPMUhy-cTkDA_opV1zGtUETNMCgQUt2yF9oQlsKIzsguG1WT6RW4Jkxs1GxvqN1LO9d1_EYg6eiZvfSaCd_OaT6dAh0TVbJ-IcCugekYkNB4Wp-qOaiTeknJ2_QifDJ0zT6lSiRucXx8ILprHqh5Yi8kFXUn1mRNP-U4tb1hZVUYNMRWDuv4JzIXCmsRq7-L2Z0gxEemFWqmJAgbsoqVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده بیش از ۸۵ میلیارد دلار در طول ۷۹ روز برای عملیات نظامی خود در ایران هزینه کرده است، طبق وب‌سایت ردیاب هزینه جنگ ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/121007" target="_blank">📅 09:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121006">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SekSxoVXKPmVUOAW9bHP5kJvdBULzSWP9PqxUduL8aC2unfcRT4zFR1HoAg7v4Wwbnv-QgZi-9ctk4ocOspP-nQuU2XAXCYH3aEEPSv5Ae7WXE0j-HhP0GlZduaIP31gGkrSrRe8v8z7JI0eyRdBtxpHyRP61ELlB3YenBln45u46os_r14zkyofql5C0NiVT5HqW72W4cRePTG3m3PAVQ-NPSNee8sR92SlhzS06go0gcOTm7DUuMEWl81bObyyjaIrqk6rKrEm2wrGONmN9FX1lUneKpaWhs8IpgUMjUrfj6nv68u0pqY7QIxZsUlfQgiKNlDEFEpeIEvwDeMOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دریایی ارتش آزادی‌بخش خلق چین اعلام کرد که گروه ضربت ناو هواپیمابر لیائونینگ برای یک مأموریت آموزشی معمول در دریاهای دور به اقیانوس آرام غربی اعزام شده است.
🔴
این تمرینات شامل عملیات‌های تاکتیکی پروازی، تمرینات شلیک زنده، مأموریت‌های پشتیبانی و پوشش، و فعالیت‌های جستجو و نجات مشترک برای بهبود «توانمندی‌های آموزش رزمی واقعی» خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/121006" target="_blank">📅 09:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121005">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
گزارش فایننشال تایمز: شی جین‌پینگ، رئیس جمهور چین، به ترامپ گفته است که پوتین از تصمیم خود برای حمله به اوکراین پشیمان است. از سوی دیگر، اشاره شد که ترامپ به شی گفته است که ایالات متحده، چین و روسیه باید علیه دادگاه بین‌المللی کیفری در لاهه با هم همکاری کنند زیرا این دادگاه «سیاسی عمل می‌کند»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/121005" target="_blank">📅 09:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121004">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نیویورک تایمز: ایران از آتش‌بس یک‌ماهه با آمریکا استفاده کرده تا ده‌ها سایت موشکی خود را بازسازی کند، پرتابگرهای متحرک موشکی را جابه‌جا کند و تاکتیک‌های خود را برای هرگونه ازسرگیری حملات تطبیق دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/121004" target="_blank">📅 09:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121003">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKe4FWOhl2JsbXGhVNIeuIwXcLc1015esEwAi7PIlLfGMAVHr5puwh9HXe3yYgcDNOzt_mMqq-uCuh0zIbXeLdbAZlryTUYaYuPHWGnYJxAY24qGZs0XHnVUSZgdHMKfTYZ8_ln8nISPyjF1VBFNypa3GLmNRUEuYgEU_R6uCuoJWJ7gg_ZQ8Np3C12a7DtaJdrMNkHLIw8UJXhGGweFZtnlkd_LP_mMXNlPodeJYYQ6BYTPDAv_44s4do0GEimRNfOco1dGCwI0tcyd2EIYWaoZwG7sf05e1AuGd5H8q4m2K13TpF2Nvai-GYy9ybPZVqyZBGpFzdvdLrnAZnnsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه بورس ایران بعد از ۸۰ روز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/121003" target="_blank">📅 09:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121002">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b51f38da7.mp4?token=Okc57wlvMhTKOBocIDYxVFP8Jc5_M1vjrpvEiDEcijI9_lpqNOmiEaj07u5iNmLy2A_v3SV3i1OEePlULhXNXKNPkrejemNHN2GBT5EbyfCkBy9Lj_U5UuD24FZhW43L_spswP9xUjp5eN4qPHiaJWZViA5xPA5Yk7qzS0j2jnnNnaSZ3tkXpqn6cy2CraCvufH55D1Niea9sHdvBm_gjYgWpK41gZV-r4BHD9dz8wvyYL4BrY30Z4o_Ejvxe-52GZxoq4BideXBgSuo88Ngh6llMNVEYdNmgDiUNYZByqx3chqIvjRbhq5D_dbp4PDfwTNcfqF-yBv4U4dxJZMHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b51f38da7.mp4?token=Okc57wlvMhTKOBocIDYxVFP8Jc5_M1vjrpvEiDEcijI9_lpqNOmiEaj07u5iNmLy2A_v3SV3i1OEePlULhXNXKNPkrejemNHN2GBT5EbyfCkBy9Lj_U5UuD24FZhW43L_spswP9xUjp5eN4qPHiaJWZViA5xPA5Yk7qzS0j2jnnNnaSZ3tkXpqn6cy2CraCvufH55D1Niea9sHdvBm_gjYgWpK41gZV-r4BHD9dz8wvyYL4BrY30Z4o_Ejvxe-52GZxoq4BideXBgSuo88Ngh6llMNVEYdNmgDiUNYZByqx3chqIvjRbhq5D_dbp4PDfwTNcfqF-yBv4U4dxJZMHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مشاور ترامپ در امور تجارت و تولید، پیتر ناوارو: نیروی نظامی آمریکا در حال حاضر کنترل تنگه هرمز را در دست دارد، که به این معنی است که کنترل عرضه نفت نه تنها برای چین بلکه برای کل شرق دور را در اختیار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/121002" target="_blank">📅 09:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121001">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فاکس نیوز به نقل از معاون سخنگوی کاخ سفید گفت که رئیس‌جمهور خط قرمز ما رو تو این مذاکرات واضح بیان کرد: ایران باید یه بار برای همیشه از جاه‌طلبی‌های هسته‌ایش دست بکشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/121001" target="_blank">📅 09:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120998">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a185f915e.mp4?token=r8-g0-nRoig-cmRiHHg5IgYOdo_aLI6xl-0PgwUOBglpi96LxlB75Hp9okcXJgYhVuBWrWt2XuPwCdNGRzkSpmXSqJwBV_Gl50iojLyf0ohh5lGgxUQAJaYMEO3j69Fyqyuc51qcxyTbhT5PBfWBqHXQ1nEhgV6OUffKWnIsmyHQePiwWsJNQtmaqK7cjfOSKFXSOkNfbbrTWY47HJv1ZzQ1zsYd0b7ETvi7aFIMKAAbLdf1fL5lnkG5d6I-fU1Q-pU6fuLUr9t2hiCpncsV1idLJi7zWZ84EiQYBfqcwH9Pesu8NkyJCb0TmiL4xEEPp8f-ziX_UTE9nmkASjF9kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a185f915e.mp4?token=r8-g0-nRoig-cmRiHHg5IgYOdo_aLI6xl-0PgwUOBglpi96LxlB75Hp9okcXJgYhVuBWrWt2XuPwCdNGRzkSpmXSqJwBV_Gl50iojLyf0ohh5lGgxUQAJaYMEO3j69Fyqyuc51qcxyTbhT5PBfWBqHXQ1nEhgV6OUffKWnIsmyHQePiwWsJNQtmaqK7cjfOSKFXSOkNfbbrTWY47HJv1ZzQ1zsYd0b7ETvi7aFIMKAAbLdf1fL5lnkG5d6I-fU1Q-pU6fuLUr9t2hiCpncsV1idLJi7zWZ84EiQYBfqcwH9Pesu8NkyJCb0TmiL4xEEPp8f-ziX_UTE9nmkASjF9kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده های ارتش اسرائیل (IDF) به ساختمان تخلیه شده در مشوق در منطقه صور در جنوب لبنان حمله کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120998" target="_blank">📅 09:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120997">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اکسیوس به نقل از یک مقامات آمریکایی:
پیامی واحد از دوحه، ابوظبی و ریاض به ترامپ ارسال شده بود. مضمون آن چیزی شبیه این بود: به مذاکرات فرصت بده، چون اگر به ایران حمله کنی، همه ما بهای آن را خواهیم پرداخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120997" target="_blank">📅 09:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120996">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: هرگونه تجاوز جدید علیه ایران با پاسخ قوی‌تر مواجه خواهد شد و ترامپ را شرمسارتر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/120996" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120995">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
الجزیره: نفت پس از به تعویق افتادن حمله ترامپ به ایران سقوط کرد
🔴
قیمت نفت در معاملات اولیه آسیایی امروز سه‌شنبه، پس از آن‌که رئیس‌جمهور آمریکا، دونالد ترامپ، اعلام کرد حمله‌ای که قرار بود علیه ایران انجام شود را به تعویق انداخته تا فرصتی برای مذاکرات جهت پایان دادن به جنگ فراهم شود، بیش از دو درصد کاهش یافت.
🔴
قراردادهای آتی نفت برنت برای تحویل در ماه ژوئیه/تیر، ۳٫۰۱ دلار یا ۲٫۷ درصد کاهش یافت و به ۱۰۹٫۰۹ دلار در هر بشکه رسید.
🔴
همچنین نفت خام وست تگزاس اینترمدیت آمریکا برای تحویل در ماه ژوئن/خرداد، ۱٫۳۸ دلار یا ۱٫۳ درصد افت کرد و به ۱۰۷٫۲۸ دلار رسید.
🔴
همچنین قرارداد فعال‌تر ماه ژوئیه نیز ۲٫۰۶ دلار یا ۲ درصد کاهش یافت و به ۱۰۲٫۳۲ دلار در هر بشکه رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120995" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120994">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e41bce7fb.mp4?token=BM0sD9infduu0m9I6niESsyHor_e6cARnaZ03X4IIxy8TNYkxh5msPRVe2SPboEEpEhZY39U1Mm2sReEsfeGK92KhMm6fkr4jZYZATytzvTsBekViHYC9V-lAkscreD22GYHvRx3yR0Qu5EHz1xs9ARZmBz1PGZV6YOVuQW1RoKkTaUUTWBDUtJAiLdhsfnSOxQS70Gkf33YD3MYoeSB1fdgj2PAAO02ANYH7YeJoHL5QtT4IR4kCmOCt7rWBDUsSndeUm9-NpxuJTbbtATLYDuEZOxGy3JnsGw093pkOayUSMGS_gsRbgYt0RGv42Jh2m0SANOT4Zh5IbKG9YBA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e41bce7fb.mp4?token=BM0sD9infduu0m9I6niESsyHor_e6cARnaZ03X4IIxy8TNYkxh5msPRVe2SPboEEpEhZY39U1Mm2sReEsfeGK92KhMm6fkr4jZYZATytzvTsBekViHYC9V-lAkscreD22GYHvRx3yR0Qu5EHz1xs9ARZmBz1PGZV6YOVuQW1RoKkTaUUTWBDUtJAiLdhsfnSOxQS70Gkf33YD3MYoeSB1fdgj2PAAO02ANYH7YeJoHL5QtT4IR4kCmOCt7rWBDUsSndeUm9-NpxuJTbbtATLYDuEZOxGy3JnsGw093pkOayUSMGS_gsRbgYt0RGv42Jh2m0SANOT4Zh5IbKG9YBA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تقلید صدای ترامپ توسط هگزت؛ وزیر جنگ آمریکا: هگزت با صدای ترامپ، او به من گفت:  «پیت، باید مثل شت سخت باشی.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120994" target="_blank">📅 08:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120993">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
نیویورک تایمز: بسیاری از موشک‌های بالستیک ایران در غارهای عمیق زیرزمینی و تأسیسات کنده‌شده در کوه‌های گرانیتی مستقر بودند که نابودی آن‌ها برای هواپیماهای آمریکایی دشوار است.
🔴
آمریکا عمدتاً ورودی این سایت‌ها را بمباران کرد اما خود تأسیسات را نابود نکرد. اکنون ایران بخش قابل‌توجهی از این سایت‌ها را دوباره بازگشایی کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/120993" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120992">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از یک مقام نظامی آمریکا:
فرماندهان ایرانی، احتمالاً با کمک روسیه، الگوهای پروازی جنگنده‌ها و بمب‌افکن‌های آمریکایی را بررسی کرده‌اند.
🔴
این مقام هشدار داد که سرنگونی جنگنده اف-۱۵ئی در ماه گذشته و ضدهوایی زمین‌پایه که به یک اف-۳۵ اصابت کرد، نشان می‌دهد که تاکتیک‌های پروازی آمریکا بیش از حد قابل پیش‌بینی شده است، به گونه‌ای که به ایران امکان داده با توانایی بیشتری در برابر آنها دفاع کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/120992" target="_blank">📅 07:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120991">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoCUTMkBHaXk-rbz5qfKbY0N2sM6EbMNpvUvPOqk3ikX4YSgua78JuHZ2-sbnMPVSs5JY_hTVsOKqP039Y_egz4GTKIyC4uA0k95njeN_Lhy_HyTnRV6rZB9io0z2GK1Ge7EkEbyJPrfjmkzwjEk_dNv6I-d_TH9vljwpzAKNy1bCgWQKD2JVCnuMnB3MvuAQwjW0ng3zGQRMlrxFyL9kPK9AmiEZ2c2jIWRMbgDm3rWD22ivnti-DxqJt8tiBivIR7BM6PwUn6RNoqtVGERLK3xV1SoPeJc2Mp40ElV-h4ZG-q2mIe9ciPxjLHga7EdA60lbDNHmOXbZw2NKykPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: ارزیابی کلی این است که هیچ یک از گزینه‌های نظامی موجود چه حمله گسترده، چه هدف‌گیری رهبران و چه عملیات زمینی یا دریایی، راه‌حل قابل‌ اعتماد و کم‌ هزینه‌ای ارائه نمی‌دهد و مسیر منطقی‌تر، حرکت به سمت توافق و کاهش تنش است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/alonews/120991" target="_blank">📅 07:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120990">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPR7LAb2Ochc32sdd4ZIhwBB-QGqmeENumgYpJfux3QRMTX5oKuUl-uqyt40Jo3S2MZq0Jk1lPZV3aFOisimnLGMvICDvPgbYe2So16Ds49NVfQC8ICCGsInebZ09JJUFt8xORRb54uVz6ydxg4IH5v4FTMGvK7sqmxLF5y5bRo4JQ5n5eQpDzsJ1HlVN0SoMhHcgwjFHOU5dcMQOImL2xxb5vy6IJGUpumOQMvp9w1odjktoFKOkyeCjZStXSuT5E77d2YNEvIkOFIgAussLJ9cOlW0KoSTn2txBbxNxDpXnmTphyb1Qbn9PseS4S9DZXa0hj2YNxxg6J4SQLZTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
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
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ ظهر فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/alonews/120990" target="_blank">📅 01:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120989">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: اسرائیل را از تصمیم برای به تأخیر انداختن حمله به ایران مطلع کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/alonews/120989" target="_blank">📅 01:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120988">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ سه روز بعد : بخاطر روی گل افغانستان یه ماه مهلت میدم  [@AloTweet]</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/120988" target="_blank">📅 01:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120987">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ: ایران نهایتا ۳روز زمان داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/120987" target="_blank">📅 01:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120986">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152da11d16.mp4?token=AB-Mta8RLdl1dfFOHpRcYB_NDiWDMenf38OAqpS6l-AWDcG_RM-n9IDmElZlx8nFfA0Q_yjtWVvLDu75Lb9-VqKbYKDyMwYPVf4U5o5yjWzp1P03c1T5ixz5vfv8HezjLxJNRKQx58DD_dsxaVxW6uNGQ59KFZShkvZQjy_DnvykijBB0efXr8LNMSCwsbw5aih1iPYiL_CTJ6DUqF8UvYda_rGO4ZnTH76fm_8sfHAzykkW9d71vlQKLihmDETefSktI5XAg04eaoLnRNjxXSUlHOy4Ly1fVhLyLM0pzm8qYvy5BnsA7PGqK7RGTrhJTADtDnF3vw68WxhEc-gsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152da11d16.mp4?token=AB-Mta8RLdl1dfFOHpRcYB_NDiWDMenf38OAqpS6l-AWDcG_RM-n9IDmElZlx8nFfA0Q_yjtWVvLDu75Lb9-VqKbYKDyMwYPVf4U5o5yjWzp1P03c1T5ixz5vfv8HezjLxJNRKQx58DD_dsxaVxW6uNGQ59KFZShkvZQjy_DnvykijBB0efXr8LNMSCwsbw5aih1iPYiL_CTJ6DUqF8UvYda_rGO4ZnTH76fm_8sfHAzykkW9d71vlQKLihmDETefSktI5XAg04eaoLnRNjxXSUlHOy4Ly1fVhLyLM0pzm8qYvy5BnsA7PGqK7RGTrhJTADtDnF3vw68WxhEc-gsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ در مورد ایران:
ما به کشوری که قرار بود سلاح هسته ای داشته باشد رفتیم و عملا ارتش آن را نابود کردیم.
🔴
ما میتونیم همین الان بریم و 25 سال طول میکشه تا دوباره بسازن فکر کنم آخرین چیزی که اونا بهش فکر میکنن هسته ایه حالا بايد اينو به صورت کتبي بنويسن
🔴
ما ارتش اونا رو کاملا نابود کرديم ما رهبری اونا رو نابود کردیم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/120986" target="_blank">📅 01:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120985">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ:
ما با محاصره دریایی، دیوار فولادی دور ایران ساخته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/120985" target="_blank">📅 01:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120984">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d41fab57.mp4?token=ug7NTT2xzWpCnMQjeaMx0Lj29clt9RlFhTyPesbOcoCf4cfnz9mcGaOBkoR37CCvmwSxJ4T5LGIQftkTj-e1PS9FXjV32_yTu-OIUU-Zuqb548J3H_1_IKZJEbjWVnp2bODKusF1F8uIPZkUS1YhmG5F7MqgIPUgIqz2unh0ds4FGkdi6V4pC0vK3OYFhqf3XlMFm0eS9SpdGyYGJ6tcb9cO5jnsA7p2LWa3LoU3erZlnfofw7Ip-VYDqQv0KoMEBz-EVR7GYkzn9R9Hg92bHEn71sSS5u1enBvDV4UnOh7oigOmzEegZ6uu3Ve9gnSQFHvqiCzJQAZ7dErg9v4JrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d41fab57.mp4?token=ug7NTT2xzWpCnMQjeaMx0Lj29clt9RlFhTyPesbOcoCf4cfnz9mcGaOBkoR37CCvmwSxJ4T5LGIQftkTj-e1PS9FXjV32_yTu-OIUU-Zuqb548J3H_1_IKZJEbjWVnp2bODKusF1F8uIPZkUS1YhmG5F7MqgIPUgIqz2unh0ds4FGkdi6V4pC0vK3OYFhqf3XlMFm0eS9SpdGyYGJ6tcb9cO5jnsA7p2LWa3LoU3erZlnfofw7Ip-VYDqQv0KoMEBz-EVR7GYkzn9R9Hg92bHEn71sSS5u1enBvDV4UnOh7oigOmzEegZ6uu3Ve9gnSQFHvqiCzJQAZ7dErg9v4JrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به زن‌های داخل جمعیت :
- شما خیلی خوشگل و خوب به نظر میاید، شما دوتا، بیاید اینجا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/120984" target="_blank">📅 01:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7b1ceb70f.mp4?token=vSwiPlpIayledo9Qx-qF28YDK0urvjfU_oKBdSfvMG9NMRWZkAtlQEd8d07cRsML_q-MxXRX-c06EUniYIpFOh9r9MOQeoT3HSp60nzNhtCCOF4Q8Zcbbhd24uCZa4--t2QpFx7xC53rrkcHUqlmSw-YgIXR00sEsLd03X9zzaxfOilTROSlqcRfBzt4Jy9d97hDUgw3ttNymdYCyFUFQnLszjnB-9cK8-Rnv-mfh4g-l-UH6o1JoNGd86OXzSDaFKei3X9XZyxXqn7iSus7vTfHhQkqObnxHTX2-awQKiAIPFrSI9FrHQlWSQ1CxSmt1SZMla0jlDoCcXrv449N7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7b1ceb70f.mp4?token=vSwiPlpIayledo9Qx-qF28YDK0urvjfU_oKBdSfvMG9NMRWZkAtlQEd8d07cRsML_q-MxXRX-c06EUniYIpFOh9r9MOQeoT3HSp60nzNhtCCOF4Q8Zcbbhd24uCZa4--t2QpFx7xC53rrkcHUqlmSw-YgIXR00sEsLd03X9zzaxfOilTROSlqcRfBzt4Jy9d97hDUgw3ttNymdYCyFUFQnLszjnB-9cK8-Rnv-mfh4g-l-UH6o1JoNGd86OXzSDaFKei3X9XZyxXqn7iSus7vTfHhQkqObnxHTX2-awQKiAIPFrSI9FrHQlWSQ1CxSmt1SZMla0jlDoCcXrv449N7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ:
ارتش ما بزرگترین ارتش در هر نقطه از جهان است.
🔴
من تازه چین رو ترک کردم و باید بگم که رئیس جمهور شی خیلی خیلی از ارتش ما تعریف کرد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/120983" target="_blank">📅 01:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120982">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری/پرزیدنت ترامپ :
ما به جمهوری اسلامی هیچ امتیازی نخواهیم داد. فقط تسلیم کامل!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/120982" target="_blank">📅 01:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6258c2ef8.mp4?token=U0PXBU8Fa4EE46UYpZ5bCtF9TYuNW1l5Wpj3iesRwAuX_UphbqYqY1y4vsdRMzNaE512jUtIy2LPWWWfEk8T1fKCE8aTogJyZVnNUVY_YGBRy8UM3_3x3iYdSSizTUJHJMPYVhEFyAUBV_ljZsczNLvCkbwYVql1Ta7RlOyYCYqAaDve69-NY8G45t9npSQGv74b7yjaLdoPL3aEeXDAVqtjt3BiOZjFIwCZcDHVaIcESwJ85v11fmDJ2sicaunsnhF5y8-2oQjWuKQqdKoAPpMEyFEUCheH4KelS3GmdeW9VJkv1l14un2BYz2lSthjDpQUTfHmH-6T1nmjn96foQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6258c2ef8.mp4?token=U0PXBU8Fa4EE46UYpZ5bCtF9TYuNW1l5Wpj3iesRwAuX_UphbqYqY1y4vsdRMzNaE512jUtIy2LPWWWfEk8T1fKCE8aTogJyZVnNUVY_YGBRy8UM3_3x3iYdSSizTUJHJMPYVhEFyAUBV_ljZsczNLvCkbwYVql1Ta7RlOyYCYqAaDve69-NY8G45t9npSQGv74b7yjaLdoPL3aEeXDAVqtjt3BiOZjFIwCZcDHVaIcESwJ85v11fmDJ2sicaunsnhF5y8-2oQjWuKQqdKoAPpMEyFEUCheH4KelS3GmdeW9VJkv1l14un2BYz2lSthjDpQUTfHmH-6T1nmjn96foQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
آیا آمریکایی‌ها باید نگران ابولا باشند؟
🔴
پرزيدنت
ترامپ:
من نگران همه چیز هستم. فکر می‌کنم که در حال حاضر به آفریقا محدود شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/120981" target="_blank">📅 01:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: به نظر میرسد شانس خوبی برای رسیدن به توافق با ایران وجود دارد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/120980" target="_blank">📅 01:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120979">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ درباره «گفت‌وگوهای مهم» با ایران:
«این یک تحول بسیار مثبت است، اما خواهیم دید که آیا واقعاً به نتیجه‌ای می‌رسد یا نه.
🔴
دوره‌هایی را داشته‌ایم که فکر می‌کردیم تقریباً به توافق نزدیک شده‌ایم، اما در نهایت موفق نشدیم؛ با این حال، این بار شرایط کمی متفاوت است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/120979" target="_blank">📅 01:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120978">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: اگر بتوانیم توافقی را منعقد کنیم که مانع دستیابی ایران به سلاح هست‌های شود ، از آن راضی خواهیم بود‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/120978" target="_blank">📅 01:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120977">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f3ba75465.mp4?token=tflAYOo78SpUrkUMFpYm11wUZhtMQ6qfXcPIRExsnp2iqMTAZ9gSm15DIonz474v-2gl59psDoJGIbCeppv_ZpBd1CSOCQ4N7JOkP0CzLHqhPFS9lpF_qnzu4Jba7plpN0jE6TcoL_KNbhLW0GGLb35aphVJ-64whIh4O4ZQHkZNN16Qp4nqtkwx2cluansiSPxciBKGcB2KeISoR_wGhhbjvNtHNw08SDod4BeRnH4DxgjFlpJRkzBEo3-WR2laAepmCEJvqg4TbeW46aV4dSNEDmBkmhdUTf0-h4oFTT1wQVcc_f2Fvy-S7LZIKCc_jLQCkPkzfF-Ji6lyMx_clg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f3ba75465.mp4?token=tflAYOo78SpUrkUMFpYm11wUZhtMQ6qfXcPIRExsnp2iqMTAZ9gSm15DIonz474v-2gl59psDoJGIbCeppv_ZpBd1CSOCQ4N7JOkP0CzLHqhPFS9lpF_qnzu4Jba7plpN0jE6TcoL_KNbhLW0GGLb35aphVJ-64whIh4O4ZQHkZNN16Qp4nqtkwx2cluansiSPxciBKGcB2KeISoR_wGhhbjvNtHNw08SDod4BeRnH4DxgjFlpJRkzBEo3-WR2laAepmCEJvqg4TbeW46aV4dSNEDmBkmhdUTf0-h4oFTT1wQVcc_f2Fvy-S7LZIKCc_jLQCkPkzfF-Ji6lyMx_clg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
- چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد
-  از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز عقب بندازیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/120977" target="_blank">📅 01:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120976">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26879febf9.mp4?token=rtTPxozp0pBd_ktzfr8rH7ampu_wVXaGBDr06vHZIkWUsRSxrvhPbSPShr_6uu1ZJFHwVz2_XbLfzPK9z--e89neangLDMTelJEKwtzRUJDW9B99e_JnJw-gdoBQYGpfs4blJPRB8MUchFOcqdAI-QX10yg7Fi7OMn-KI-82LcxLOV5SmZB_0tq4QzlM4nBHfyZReJt0a_tk2IDO2xWPL0AqzLeUUVR2X6YpOlpiWizop9D5ur5vlRP47cGL-tl42LQcCuG0BqULyzN_rJuyeTJ_pry5bH9pSv-gtdRXzeWNEYn3saSY7YGm3Dz-thM7xez72m-7qoB7-OeqHzfdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26879febf9.mp4?token=rtTPxozp0pBd_ktzfr8rH7ampu_wVXaGBDr06vHZIkWUsRSxrvhPbSPShr_6uu1ZJFHwVz2_XbLfzPK9z--e89neangLDMTelJEKwtzRUJDW9B99e_JnJw-gdoBQYGpfs4blJPRB8MUchFOcqdAI-QX10yg7Fi7OMn-KI-82LcxLOV5SmZB_0tq4QzlM4nBHfyZReJt0a_tk2IDO2xWPL0AqzLeUUVR2X6YpOlpiWizop9D5ur5vlRP47cGL-tl42LQcCuG0BqULyzN_rJuyeTJ_pry5bH9pSv-gtdRXzeWNEYn3saSY7YGm3Dz-thM7xez72m-7qoB7-OeqHzfdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/120976" target="_blank">📅 01:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120975">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678a888387.mp4?token=HSfJZsdGxMIrcLscdsEvnnilnMsoyuQ6fXx2HBvjOszUji8N-uZ6OPhhGcZj5v7gsd1TDGJgS5pFdl8gXss3lllO7KTQUpaeIvfvYsP3DVeMKwZ2MuXTJNF3i130y5Xk22z-U3Rw6L-ZoiQaLBk5KjV0vI5ypyCFdjqo29tU3ItsfOrwrPQ8JsuP8y65pGX6tiDg9Qc807IKnleV8LNktgGOHkQU1Vymw8tk4hJwLJExIxKoVGy7vWJZX4UiNYx7xuEfT9_E8cafFD196frhHGYVveuzpnk51YIkWmH-H9sHC0tBB4bhFFnrlrsgVz2EC_v7AjTwwj5n_4wLx8iang" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678a888387.mp4?token=HSfJZsdGxMIrcLscdsEvnnilnMsoyuQ6fXx2HBvjOszUji8N-uZ6OPhhGcZj5v7gsd1TDGJgS5pFdl8gXss3lllO7KTQUpaeIvfvYsP3DVeMKwZ2MuXTJNF3i130y5Xk22z-U3Rw6L-ZoiQaLBk5KjV0vI5ypyCFdjqo29tU3ItsfOrwrPQ8JsuP8y65pGX6tiDg9Qc807IKnleV8LNktgGOHkQU1Vymw8tk4hJwLJExIxKoVGy7vWJZX4UiNYx7xuEfT9_E8cafFD196frhHGYVveuzpnk51YIkWmH-H9sHC0tBB4bhFFnrlrsgVz2EC_v7AjTwwj5n_4wLx8iang" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ می گوید که قیمت داروها را 400 ٪ ، 500 ٪ ، 600 ٪ و حتی 700 ٪ کاهش داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/120975" target="_blank">📅 01:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120974">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
تیراندازی فعال در مرکز اسلامی سن دیگو به نظر می‌رسد حمله‌ای وحشتناک باشد.
🔴
تصاویر هلی‌کوپتر نشان می‌دهد جسدی در برکه‌ای از خون بیرون ساختمان افتاده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/120974" target="_blank">📅 01:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120973">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5J6AwYF822YrRmMA-F-ESYM9BtWZ_i1QyaAa-SJgpKY57ui5DhHFVg1DMGYoNJQMcpSomJTmRDWmmdhCShoj8V05rbJ49qFHDFhaO1Jip5WnwVEha1zCtwx2_se2kFWxFl87XgqYdQyktobpj8G8kf6BF1ppCUf6brlfxWaVOH6gQ6qwEWUXhlVjJ2pInp0uEGhN8YYNdjvWmq96G0b2ZZz6I4bZmvF3RSHFseCsp9FW1KDAufJvJegU_KwOajnQFb0CpsWO99HxLKyF915tpkQJyPfO9dpziVUUixVS7AtemIu_XA7ZN8iMpZSWPtCix1F8cGQHargxIZwvrxQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلهکی
، ‏
فعال رسانه ای حکومتی:
ترامپ «شنبه‌شب» قصد حمله داشت که صبح آن قطر به ایران هشدار داد. علت عدم حمله پیدا نکردن لوکیشن سران نظام بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/alonews/120973" target="_blank">📅 00:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120972">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fb57441e.mp4?token=nhlucf9H6kKjdcEINMr5qtsGv3Rsstw3ebhq1lEz3JU_0dEUYgyLalZAIVt4DGE4oZUZ-hRtx8LVukzKXw4PG_VDNOp7gx6noKgSStN6OYOXvlWUuh-KkLhj8wOO0DGUEafjjNXhqb7qFm9iNZ-KYzoDc4Og7uYjTOtlDH74QSNM9xGlUnTZJXna2mEaXKl67Scvd-1TT2HqTGrto7MisjKV5V1GcYmygwYfDp0MTL0arEjL2KPuZ8Tz-jYQBwekB0WqN3SV6Y45SkmP5J9TfVTCjv2-V_5qJCSPSnw5K1FNDb0VnydK6ZZGbsdG9-nvtx0h2gLZMpIl8ixjuXuQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fb57441e.mp4?token=nhlucf9H6kKjdcEINMr5qtsGv3Rsstw3ebhq1lEz3JU_0dEUYgyLalZAIVt4DGE4oZUZ-hRtx8LVukzKXw4PG_VDNOp7gx6noKgSStN6OYOXvlWUuh-KkLhj8wOO0DGUEafjjNXhqb7qFm9iNZ-KYzoDc4Og7uYjTOtlDH74QSNM9xGlUnTZJXna2mEaXKl67Scvd-1TT2HqTGrto7MisjKV5V1GcYmygwYfDp0MTL0arEjL2KPuZ8Tz-jYQBwekB0WqN3SV6Y45SkmP5J9TfVTCjv2-V_5qJCSPSnw5K1FNDb0VnydK6ZZGbsdG9-nvtx0h2gLZMpIl8ixjuXuQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار جدید رونمایی شد
‼️
🔴
تندروهای خیابون امشب شعار مرگ بر "امارات" میدادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/120972" target="_blank">📅 00:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120971">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
هاآرتص: مقامات اسرائیلی از دست ترامپ کلافه شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/alonews/120971" target="_blank">📅 00:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120970">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=gAzVcvLvgokwYZ4zvcMXI4lfILPBb0hQsTpwX256z21850oaMn40TBDy-nXl537ucgflJfhqbJeW8XdUlWdzBw2-dyXEr_aFqBbK3oeqjaRn05qBCcpSjMVs0swCDbwR5N-WUeakFOZZJHrF1QD4xMd2Fw4vilTh7-RDs4nKEMGGpg0p-6NEtD1EHrdwsFbJYRd30Dr7EFVntGQnKi00nTR-K_me8TeMMpjfwSe4ju7ScSAR8kKpM6gROYkxu1qzcBzUPqkjYF1oIIvLFjgqRkYY3DoSxa52v8HRpd-F4xcnq8XJeERXTI6u8NkuM95St9XOwyeLIPDhvOpAIUsr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=gAzVcvLvgokwYZ4zvcMXI4lfILPBb0hQsTpwX256z21850oaMn40TBDy-nXl537ucgflJfhqbJeW8XdUlWdzBw2-dyXEr_aFqBbK3oeqjaRn05qBCcpSjMVs0swCDbwR5N-WUeakFOZZJHrF1QD4xMd2Fw4vilTh7-RDs4nKEMGGpg0p-6NEtD1EHrdwsFbJYRd30Dr7EFVntGQnKi00nTR-K_me8TeMMpjfwSe4ju7ScSAR8kKpM6gROYkxu1qzcBzUPqkjYF1oIIvLFjgqRkYY3DoSxa52v8HRpd-F4xcnq8XJeERXTI6u8NkuM95St9XOwyeLIPDhvOpAIUsr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واسه اولین بار تو تاریخ؛ صداوسیما امشب یکی رو
کون لخت
نشون داد...
@AloSport</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/alonews/120970" target="_blank">📅 00:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120969">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0gcX3aBSihf0fCs6aujmGCTgbjbEDrzRO5XmJudZwE8J1C9DFcST0VCDmduQu__Tua9HL7X6XZkzp_7QWIeV2oBaRuPYBBRqWsl6wx-TjmTTHD3xXADcDuY3HeKeHzpspGPvW3Z4S7ToBcR9Dr3UizWnSR8K-Rmr7OKX1O6Kqic5gQK7kJtKC_Six_WQsjOzmdiJ-M_PY2IQ77p0z9QnaZlcvKox1U1GeTZUSlPYUwLNff5tgAvofdGpeezSucB99dwNXj4X22pfviUgRFyftGLHC-36mIERqP9w1XpMv8Xm01NY27v2gsfctx1p58osJx-pOZJlS3yZvxH5FSMwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم هفته قبل: آمریکا تا ۳۰ اردیبهشت حمله میکنه
🔴
ترامپ امروز: فعلا حمله نمیکنیم تا مذاکرات ادامه پیدا کنه
🔴
پ.ن: عوستاد همیشه برعکس پیش بینی میکنه، سری قبلم گفت جنگ نمیشه اما فرداش شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/120969" target="_blank">📅 00:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120968">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه آمریکا در گفتگو با الجزیره: ترامپ برای رسیدن به توافقی غیرقابل قبول عجله نخواهد کرد
🔴
خطوط قرمز رئیس‌جمهور روشن است و آن اینکه ایران نباید به سلاح هسته‌ای دست یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/alonews/120968" target="_blank">📅 00:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120967">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bixUgO_0dAPLGHUKDNNxZ-572oI-j70t1gCqSjn1XMJNvZBJSiFtEHhwTBhcH_UDs2FrmmomYNUpcMC6tnCsNraAiNX_nx5aN85yVVFqFcxQqNlXUwFC4c6Fqy1tbjIIIe56mMKMY4UkupsxcBCGUyRBUVUKIzDBtEdHwKFEr-xA3swL3kkIfzn7yZByyczL5xzNLc9-oYbp4RDk7Ob8NlNiOOBfkjE4hcAWA4OEHrL-mAs68ffeKdMsLyL94lYk5ygz6P7pzb2bKSYSqjGNjg6BQBS5IAEfSTQ8PAtyNYkdqonMoitDUemMMkQu3tS4cJzv_OW0gbOC625Jwe2_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط تو صدا و سیما تانک آوردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/120967" target="_blank">📅 00:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120966">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
صدا و سیما: دیدید ترامپ ترسید؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/120966" target="_blank">📅 00:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120965">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پدافند اصفهان فعال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/120965" target="_blank">📅 00:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120964">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری/ترامپ: مذاکرات جدی برای رسیدن به توافق با ایران در حال انجام است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/120964" target="_blank">📅 23:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120963">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
اکسیوس: دو منبع آگاه گفتند که پیش از اعلامیه ترامپ، او با رهبران عربستان سعودی، قطر و امارات متحده عربی تلفنی صحبت کرده است. اما مشخص نیست که آیا هر سه رهبر او را به تعویق انداختن حملات ترغیب کرده‌اند یا خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/120963" target="_blank">📅 23:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120962">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McvaY6UMfFHoyR4DLcHpBUpLatW-__PbFck5_Qc7y-75SawCkWE-4745hWNPYYIM6a66BVzgo6o2BWBJdNQPjSwLe6xLwW8fvXEuJm5EhyvhCv1DoQ_EKbdtIBUKM2XD_HF0nBU08VD9soBruqM9T7uVjdeNZTe9zBDA3IT2ERKJMYwPnBAXvx73bBz33vJusre3hyoijkGekv1_q1AC4pKr7nd834JWhq8Kg-PsiOvDSU-uaZsJxMYZ20a4DMXf250jse-uKs8KCPak49UtnK2fxt9Lpsd59Keo4-tKA0NyZA-LG-W84VGUa3vpow6eRfT29hLAKYiKkNQWtg4fZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس:
ترامپ از زمان شروع جنگ حداقل 6 بار ضرب الاجل ها را تمدید کرده و حملات برنامه ریزی شده به ایران را به تعویق انداخته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/120962" target="_blank">📅 23:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120961">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZb5unuJ-nBRR1wcJgGcaBh1kbSKNUi6u0y2tj5Kscp1uVpcuvYzzJShgpbCCSSVe504lOjD_mW0KxP2FHDdIuFeC4fzRKB4IK4dF7GAj6nKiz9yi94rTMfB-u4xsd0WKoKlWOPqD9HUL5pn41owuVRrUtTtzkZqUKyeBlX712Enj3lt_k61oSVNfFvUh6kTcvY6_V3k1qwCbApH613RO-_QO36zMe9Vbf-WE5GscXOTm-vvUq5gP72PMti-XR2NcplYla30U7WSrjXDGzo7g-AfE0Q7bLwUqV81jFeA7gtyJLJzmuRdwZVd9yIEYAbT_Tk8ajXHwCNogaWC75dPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدم صاحب اینجا، یک ساندویچ ساده به این دوست بازیافتیمان که کمی دورتر مشغول سطل زباله بود، داد. چند دقیقه بعد که ساندویچش را خورد، در حالی که حواس کسی نبود، به کناری آمد و شروع کرد به جمع کردن میز و صندلی‌ها و رفت.
ایشان رایگان نخورد.
در شگفتم از مفت‌خورها، مال مردم‌خورهای تسبیح به دست
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/alonews/120961" target="_blank">📅 23:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120960">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/120960" target="_blank">📅 23:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120959">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBuRznpmRoXHkq6sdY8ANyUruEIp_VrSsTdVUR9uoi2M_e-IZUtL8jDDXkl8HHRdoDoU2qBWTaijoWg6yIIeZJo7cnJfyf5X0llSvQB4G5tWqtTLFVMo97o1RjTw0eKn-UCQb2Cv4aQACWQsv3jrg9xwYIJuMkqIR8dCFaMPi7ZyM1WxKfOfTF7d8Pp08qWp6nxJu-iMW8XKYdDMTrLpQapo91wjlPiroRa1YbA9TMvZpwdmV6fGiGgMdTxKRo5hiBRKfPgMtmK7m1gZm2oBHc3bKMel-SuSE1sptrZlEmrTRYULxLbXVp8amPVELLOpFi31VBg5E6P4H3JbRwjNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: وزیر کشور پاکستان که به ایران سفر کرده‌ بود، علاوه بر تبادل متونی، به نظر می‌رسد، ضرب‌الاجل دو روزه‌ ترامپ را هم منتقل کرده بود؛ مبنی بر اینکه یا توافق موردنظر امریکا را امضا می‌کنید یا حملات را به صورت گسترده از سر می‌گیریم!
🔴
اکنون ترامپ اعلام کرده در پاسخ به درخواست رهبران قطر، سعودی و امارات، حمله را به تعویق می‌اندازد تا مذاکرات پیش برود!
🔴
علی‌رغم تلاش‌های گسترده برخی کشورهای منطقه در روزهای اخیر، همچنان فاصله انتظارات، شروط و حتی نیات طرفین بسیار زیاد است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/alonews/120959" target="_blank">📅 23:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120958">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در سلیمانیه عراق
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/120958" target="_blank">📅 23:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120957">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bw-PpVy0ElWEOqo4qcNLOPkF2Ig1mLtN-zNLTrr3r6ameKvBO-dkKs2VoGyKNe4fw1OFZ5-jHZZGpe4arI_os-UYJqKY7bW7QLdi9P9UANWzevDbiIykAvXy7jxgc_LZcvCEW91oRgucdhlD_r0f781kAAdXRULWa27VKye8DMLyal339UWqSQL0rHuS91dYRrwOfXv42KfFgz3PBZ7fQLZE5-BiC3DDjbVqc41jWL9QcAPq455p7QdNd_Twn1pWe9Ta8sJdPn1yMGsujWCiDTAcEaHo_5QrcLIVw5EmelbCTBmE3m_cYoPPHs1eEPyBXxwfAxl3HgMlpOrhSTjBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمب‌های نور افکن تو غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/alonews/120957" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120956">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4686aac92f.mp4?token=AqP8Xxb6hYPW7GfANhJH8_uOGcqOSYAm3ek2C6Jk8YFmlwbftYrfagoP5J4-Hmy35h4b8EgY5ZGk4KYdVgxPjFTaf-7EL6hQSQ9eLkmpv3EirPb03lV7hYT3OcgbiUT92s88Jq29vrpiBMr68mMTa-bzR9mm_hrz_ZDiMKCF4ZkHNuV6g7dNQ7bN-HoPeMJBxpkB-ykwdiX1womUbKGcxGNMJFM_1IZVGHDhCTu7RC3Cj8twBxFI8xEOmwvgkOreZLAnYVUYFUKSIOBRBC9NsQPVBLEtKzKi0_5J3SPEFX8EwNXOflTv3wIYE-assWORPa_iulaNka168tqHXxKARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4686aac92f.mp4?token=AqP8Xxb6hYPW7GfANhJH8_uOGcqOSYAm3ek2C6Jk8YFmlwbftYrfagoP5J4-Hmy35h4b8EgY5ZGk4KYdVgxPjFTaf-7EL6hQSQ9eLkmpv3EirPb03lV7hYT3OcgbiUT92s88Jq29vrpiBMr68mMTa-bzR9mm_hrz_ZDiMKCF4ZkHNuV6g7dNQ7bN-HoPeMJBxpkB-ykwdiX1womUbKGcxGNMJFM_1IZVGHDhCTu7RC3Cj8twBxFI8xEOmwvgkOreZLAnYVUYFUKSIOBRBC9NsQPVBLEtKzKi0_5J3SPEFX8EwNXOflTv3wIYE-assWORPa_iulaNka168tqHXxKARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیراندازی فعال در مرکز اسلامی سن دیگو به نظر می‌رسد حمله‌ای وحشتناک باشد.
🔴
تصاویر هلی‌کوپتر نشان می‌دهد جسدی در برکه‌ای از خون بیرون ساختمان افتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/120956" target="_blank">📅 23:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120955">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thZhBljnjz66Ot6MDBD3tgocQO4SyIzHhIteWmdTxzUPux2IZJx7-Nw4Zw1yvgg-Acd_mSrEoZXE4kn4zRWQx4yVP0RA8hkih9yynmO_xEGF2sj2kn8_-Rz5Hx-nK7Gb-T9RmBWnlda23C_BGdnRZNG9wymfA28jUToeD1VdjJvnu1b0_k1H5kOwHYanSe6nW-4PR29LG5QaxGLLInl-gHqvsREj_BIHKdQk3eR850LpKVhxLdhFDU9ekf7skk9ibm2IrcQ3HXLPXbCoOoviXVOdPp8aNTV7BIpFvybosIIZ5JuLkb100cvjFjXd3t0d1uXmrxmCfr7vtAE8SdawKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
در مریلند، ۵۰۰,۰۰۰ رای پستی غیرقانونی ارسال کردند و گرفتار شدند! حالا قرار است ۵۰۰,۰۰۰ رای پستی دیگر ارسال کنند، اما هیچ‌کس نمی‌داند با ۵۰۰,۰۰۰ رای اول چه شده است.
🔴
علاوه بر این، بسیاری از این آرا به دموکرات‌ها رفت، بنابراین هیچ جمهوری‌خواهی که در مریلند نامزد شده باشد شانسی ندارد! این کار توسط فرماندار فاسد ایالت، وس مور انجام شده است. او اجازه داد این اتفاق بیفتد تا مطمئن شود دموکرات‌ها پیروز می‌شوند.
🔴
برای من هرگز منطقی نبود که مریلند به عنوان ایالتی خودکار دموکرات در نظر گرفته شود، اما حالا می‌فهمم چرا. مطمئنم این موضوع سال‌هاست که ادامه دارد. من از دادستان کل ایالات متحده و وزارت دادگستری می‌خواهم که فوراً تحقیقاتی در این باره انجام دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/120955" target="_blank">📅 23:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120954">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
گفتگوی وزرای خارجه کویت و عربستان درباره آخرین تحولات در غرب آسیا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/120954" target="_blank">📅 23:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120953">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در سلیمانیه عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/120953" target="_blank">📅 23:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120952">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhY7lTjD0q0416oQeECZa0e0Ebm9i4ZmabBRbH5ym-WQd6IlNmHuNW-BwhGh1gSzupnoUYvezcDVFKiAGAMAS6ehTSA5C7-vfsmB2JoaXqr0w9KuIGDwkYYB5r9BsjwiJT3tO46rLB9NAKLXPdOK3WS0pKmXkZnr8trBCKXmB66ujWxuagctTrUzCGiqJqdVlKrkJlxfa2ig91MxizdHxx9vKlruYG_Mk1nAvdKyiIopLJNDkx1d3ge3yTox4-lT3Ngw0wCK6XYdjTci25-N3MHLJ7KDC3y4NMTJcxLULgOXVfTPr0839B2RYrGzgBoIHGicF0ls8LhkGDUyAOq_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تخفیف ویژه فقط به مدت 2 روز
🔥
🚀
با بالاترین سرعت و کمترین قطعی
💰
هر گیگ فقط و فقط 170 هزار تومان
⚡️
پینگ عالی
⚡️
دارای لینک ساب
⚡️
پشتیبانی 24 ساعته
⚡️
بدون محدودیت کاربر و زمان و ضریب
⚡️
مخصوص استفاده روزمره، هوش مصنوعی، گیم و ...
✅
جهت خرید با تحویل آنی فقط به بات مراجعه کنید
✅
@Lex_Server
👾
@LexVipBot</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/alonews/120952" target="_blank">📅 23:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120951">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: من به وزیر جنگ، رئیس ستاد مشترک و ارتش امریکا دستور داده‌ام که آماده باشند تا در صورت عدم دستیابی به توافق قابل قبول، حمله‌ای کامل و گسترده و همه‌جانبه به ایران را با کمترین هشدار ممکن انجام دهند این آخرین فرصت ایران برای توافق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/120951" target="_blank">📅 23:02 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
