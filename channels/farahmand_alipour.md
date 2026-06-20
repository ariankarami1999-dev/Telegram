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
<img src="https://cdn4.telesco.pe/file/PuuXlDQuHGrAPWm3n3CeAy87C8QoK2ptUqdl95nZMZjLE2aQZbL56BKT6agc4_EunMgZZrr5XrSsfVnTn74xtisBqfy28kguvMRW9euvtwCgaE4LolbKTjHEV8uG1qvZtNxOtW1uU8fsVUctFGXbdrBH_MPXl9RQBY9ph0NEZPdz5pGn2jfiDQ1A3ndhwZiAgW44o-UPebWZUJbVzFNHu4Ash9SOPsKBzutyhy0Cv3cRn66nrMOnaT-YtSvMAp_co02blsTmDSlaRGLjcUbfo3XhwmIljG1eXPWUGeRktxQKP2GtSGdTN3I0Ot3n8VrvFcdHhNyPyD7Co2HHfItqDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 11:47:27</div>
<hr>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=TDS2DpRWzVFJy5pmhY2Qs5ek5xEeJOK9UCnizS-9qVobuFTjRPtL9jnjKvNY6jOKtL5Ep_o3aRpTkbG48qWD54PatXXvAb57tzqn48SDsjMQOqfukQI0CvjOY0ftf5qbcUnCtHP-U6qMpmdADNdgakM8DH67V-o_bp6nNwX_xw5S3uZ7AutZH7HFCA-vgAqVfrPzzRqP9C8q-dUdfAPfaxqIVqAxGTDdosL8eTrB-NU4RRSqOZ_Abl_c3y1iBMLFWklHj9ki2E7huMtEgvAhcU9OwbjrgCVTOBkjzkKHc_5DJD06tItbwxKWQkIUJ6sftjuTDgHIYY1DSto5jpX1Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=TDS2DpRWzVFJy5pmhY2Qs5ek5xEeJOK9UCnizS-9qVobuFTjRPtL9jnjKvNY6jOKtL5Ep_o3aRpTkbG48qWD54PatXXvAb57tzqn48SDsjMQOqfukQI0CvjOY0ftf5qbcUnCtHP-U6qMpmdADNdgakM8DH67V-o_bp6nNwX_xw5S3uZ7AutZH7HFCA-vgAqVfrPzzRqP9C8q-dUdfAPfaxqIVqAxGTDdosL8eTrB-NU4RRSqOZ_Abl_c3y1iBMLFWklHj9ki2E7huMtEgvAhcU9OwbjrgCVTOBkjzkKHc_5DJD06tItbwxKWQkIUJ6sftjuTDgHIYY1DSto5jpX1Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7Bar7z-6BMUnPpEwd4GqW1pELGV8GT4lpagUPhNXZngGLdrkxr_wNWTXSBpPnUb0RpDaUkDOheTD4YDiyxpnBZD-pJ8xf0w6gWjUpoBq0j9eI6SAKxY26qkS6k4pjQ2V84STNXpjK8Z-3dnV7TBWAJZz-vqvhT6-A-7YOahWg5AILo1K4hr4K5BBhYq2d17jdogpJJU5hrkk1cqHjNbRJ_4BQaVnb83kP9ZDqFJn9iDuTS6PCLWpUana7wlzch340ry-soxuJAk4MKg2JcI2a0aIw_XZDIFKZC9BJsXP7aFjNEWJupb_QTFkfwSDi-IsJ-nBzSTeWZIkAxn-dTamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=K7ZHTc_aoXX9xebGvZgvQd_87z3sUmoBeOW6_WjpgPOlGlQIx1ZD9WswPnXu8xTWQhOUicZlgZI-ImjupyD7p8E4auw6q5InAXU3pjeO67xNEy-Xe0ISliwZpxDOuAH7_ydgM9EaJ3ixLixHuglAEKsdiHw0U8a6-vX3SwCYeB6Ju2I640mXxuRZLSxEugIGBQfactI3VW_XxJVvm1cEL6SEx5cy6N1XJATDEOjeh-o2-H1yoFVO9WAgQNdsuys3LH3lh1L88w5TLzHIBRL6fLBHGtLAzMLnJebzpJIohbCba8EK6bI41pTDFrJ0t772stzADRysO-cdXh_O652Hfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=K7ZHTc_aoXX9xebGvZgvQd_87z3sUmoBeOW6_WjpgPOlGlQIx1ZD9WswPnXu8xTWQhOUicZlgZI-ImjupyD7p8E4auw6q5InAXU3pjeO67xNEy-Xe0ISliwZpxDOuAH7_ydgM9EaJ3ixLixHuglAEKsdiHw0U8a6-vX3SwCYeB6Ju2I640mXxuRZLSxEugIGBQfactI3VW_XxJVvm1cEL6SEx5cy6N1XJATDEOjeh-o2-H1yoFVO9WAgQNdsuys3LH3lh1L88w5TLzHIBRL6fLBHGtLAzMLnJebzpJIohbCba8EK6bI41pTDFrJ0t772stzADRysO-cdXh_O652Hfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-ZIxJXvUFjR2IbLA-xJ-YwWCQ9PZ3e6aySEA-7VUf_UaPeuhZ-66586ZWaVi5jktBUCoeh5yP7fShzMQM52Kp2G0MwVeoRuAkZe2mTOlkz635p0-_79LE3FqF_jfMf9S7gg6LrJ4zpIakkf5Q46z1KMx3Llnx_LDk6z5zUbiSNqFM4YuvbBktBsQXoXBskWCeqCpLVCwqmIWNRm24n93l9SO2h2BU_obJDn10Ycri9ng7o8U84J9JlLyJh1KG0YgPAG8h6wMbqR77j_1Vqg6rTblOMxD9-5q_R-1OzErSunbKlATNMsCDH_18b4U4ZlTrkXu9PWmciGL_W__aaXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=KJFc2c1BF2LPYRz4qrjGlFlH-U9zCeLy7kz1sL2HGSHf72jcKB0VYCgR7Vmhs54wqdtNnR8JWG8VDhCwH3bspTAMSCKKvxUeKwWuSNAJ8_6CFlhHNvlBjoP4oNQ0erB9bRTzdIB8Hp-dZy39JyI0MXCMHYoM9eyH-Xz-E4mPDVL8Cq-DlHKcHggd_lonm8V9LDEkq_33-7Q7LRgl61tqP411nC0UJxZ4c6TlLz_wvCtb0UTPF0_GByiD0bDdU-4m8pzbnZX-bfYEa4qkG__-UftnjspyfEb9ohpZhOfVHFW76No1KMjenzCC1Dlg4r1Q7kV4Qkylmb6gQLhbJCOibA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=KJFc2c1BF2LPYRz4qrjGlFlH-U9zCeLy7kz1sL2HGSHf72jcKB0VYCgR7Vmhs54wqdtNnR8JWG8VDhCwH3bspTAMSCKKvxUeKwWuSNAJ8_6CFlhHNvlBjoP4oNQ0erB9bRTzdIB8Hp-dZy39JyI0MXCMHYoM9eyH-Xz-E4mPDVL8Cq-DlHKcHggd_lonm8V9LDEkq_33-7Q7LRgl61tqP411nC0UJxZ4c6TlLz_wvCtb0UTPF0_GByiD0bDdU-4m8pzbnZX-bfYEa4qkG__-UftnjspyfEb9ohpZhOfVHFW76No1KMjenzCC1Dlg4r1Q7kV4Qkylmb6gQLhbJCOibA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3LYbBSCxBfE4yU4lSfSPnRiYrGgmC0kl1ek2pozHlTbJjo31P_u1oBnLp17qISw2cEyKfuGYH6S2O2-azr5_aDvN4uzZRrJN0yHdqwuInkJgmPqwgWyFwfRezyCZ4g_YEc3HnZUe4xggt8MWC441EBTcZzTZf_lQOHd7zN2AYN_5QvlrbKh3w6UGMKq9BFn7Na1KHTbEmnowGV2AsoGZMV84zvEvH9rZPGl2Zlb01LPdLZdKJggaRScFSivLk99JzFdhyp7xJm6YZa_UccdfmWnnbIE0pRVYipo9xxGC4wszyhyV_ylsZfIlxCUuCbZvbr3ns_BB42dOhGkSVufiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTb6ll6mo8_3poAwGuJvYlJQ3J3CPq2Bncv_Y9NIZS_6UDTcd1ZGicb7AcxviInTJwGrXxrPiBBFF03i8X3MDBWYG7kTPr8niwfgjMhmvix0FM38ZL-Cg8MnsYhidZ7ZNg6LVlZrdwho7Vo3jIlyHZUVRmK424vset_yaUUeYybw1Ua9nSJAW-pmrGlp_FAUuNfoqD0990XKLxk44Xp6gDAN4YX3lXzwT81kny3GzFwy3NGREOBvw2WL_kqvCS4ZApJL_r6Tp9viK1WyP8AugN4DLnMYsXckq7C_5vm8y1XSe6PSCDXn_MruWZFQLKttPMCnLuk54NxEkXkssL5z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOzU-u4qrvknyaI8POmRHrvIAFwk_1hiYryDngCoHXGHPI4RHGyzuQLILziOkCVIWL6fe94egh4Dg8ljFE1ItJP85cB_iY-6aEdqOAendQpRIjRo_f9_JEqo_NQGOmY9vMh-oYouVRMVqCazw6qdnghM0Co2pMwfttacz59EJUrfGPsxrwH6kexYF-RkUlB7l8XXC-fRiVN1MqC_eDFR41wwj1b-3wBAHfKIEk--h5_ku1XYDBKova-f4xxasZH83srQc4EllQ0G_tdBjZmdroO_BkQ3Z92oLCz6nvmpmvpenTwrG0OH85R0PRU37MIvRNxOs0Jg2MLU7WDk1k6vRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=WX2NoFfr-IVtWX9LMI2VRv1e64HxnTyaTg95AcYPKBGfP84YX6Nsg0mMHiiZHlpGvH-s6QLEvoyE7Fp7jOAiTljtDqTPepZosX-rAp25XkIo5Gg-x-FO2C_DO68DmTTna9VnBo4HxvxCQUvz355JXvRlctYOmPcG8mPzoNTVu3UdtQFZ2Srd9qWHew94NhCIvSxSMCfnm8eA6B5Cgrk0rrsSash0UbLpVsK37cjML78ec-Q9OlkyWmU1fk_q7qEDq9r6P0C9HW3JvVR7PXeKuj-rdzcMmpU-780XgPdrcKq8ydvbf_UQ68OREssd5CYkLCZ35WaWR8xNijmd64KpSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=WX2NoFfr-IVtWX9LMI2VRv1e64HxnTyaTg95AcYPKBGfP84YX6Nsg0mMHiiZHlpGvH-s6QLEvoyE7Fp7jOAiTljtDqTPepZosX-rAp25XkIo5Gg-x-FO2C_DO68DmTTna9VnBo4HxvxCQUvz355JXvRlctYOmPcG8mPzoNTVu3UdtQFZ2Srd9qWHew94NhCIvSxSMCfnm8eA6B5Cgrk0rrsSash0UbLpVsK37cjML78ec-Q9OlkyWmU1fk_q7qEDq9r6P0C9HW3JvVR7PXeKuj-rdzcMmpU-780XgPdrcKq8ydvbf_UQ68OREssd5CYkLCZ35WaWR8xNijmd64KpSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxyJKAnXOSntZi3sOwYR6XnrhJBQOwOTeY8ND3rpGHq-49Qce25RVtEpyN0Zn528Q68yxOwVkuEnPlKQm3A-TruHQt5Eg5aY1Gn8s2p9GyoxVI4K7hXorBOtCCUolwJVG4oRbU1EZ82Rclp2RH6vlBFZMhcGa0kXGvGtBfGV9bXIOKLEdQrqTY0-Tc1llzqK17iG-rQvOEzsom-GEbG7djVH6Q5vlp1tua6w4kKUvQ6aitaLgJabdd9FzelugCsOJqTV0T0mi0alYy7BHxgv35KthJLnaZYsHbbOOyosdbGvprVCZyixsxD6dLu43eFUr03bc6KfQ6_md4ZfdTk_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5nttENIgEfiwZuj_Reb3t1GJDwvM9OmzGMHBQglcOzJZS7osKp6H4gyPbq8aVf3VEpPlaqdLFGdpugxzWYPC9xIqgHXk7NOM2GvcIyxrOrXfWlYv824aSDBRVOALtBo_-scHBs-rAD5iGr4Z6ZVgBzZNRT__f496MlvWQld8b7LXW_gCr64LhxfrHnvugcxUtiD0ZIIigvohWvnFiQ7lbpW_TxTVCcTxzq97jvA-I1pdz9Kb9NpGk_iDKZaEQJctakHwuXRsOEaNY17-tbUnipccH2djZz_TJwUgrr3mW7Njb8b-_CWxqHV5QeaVNyXImjUppOS-9gZlaeHFDuxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rip09e5DCowT_2bgFM2V4mdcdlYvac-ZajIMtnS1p7qAA4rl37ZZjKlmHja6D4J-TFcOE3Ez_PNFEfOuoPs91wj9k54OW1JNDAFu-ZW7rNUA_3Bgh2FawlbEEYS8tqxo7cJY38PR_WJtmMCcfLV1wfZphVB3MZbocNKJ8086bPKPaZV4T5N0vzKpZRXSprtwa3OS_-fkWsPwv_e6aySm0AW9K1SVRf95N7vXfTYo0puM8tJqpuoXbi8jFGOmRLd3fZpBVewUKc4I3MPIX-TVCK4gpKjGdeL_VuH-qzYqGsVKKj7GCeHIkFpTSXWvY3p5AJ2OKZG1g3w4TYrTpu8BiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvKU02dxYTYH7ce3t7cDFcG3HV9e_NbL6ahNpiXGYwa8j-eq8FB0mqWk42AG50HpkT2MxxU208YVylXzsaAOBw4iP0oePiOaZYkSdOsxFPsVGPviVd-6AQP4pKhdL4CbqyQkX6WOlGuNzCc4q88zHIddaQ5jHXPwQIgnx1tatD4DR4ThilxwAL3O7q2wtVQoe1nBWO-0hW1CbTZUcgmTqOYPQHFh2IBg3vUGa1Q91jEQxPRjJIJ4Gi5WAR5n5nT93pPg8S9NSUZtsNkMmz_7Yqv6XN-PvGqjSK5UMxb1u8_cAO0tDqpjV5G9OBWT9Id5TdCwZXb0PM8G5841ebq-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNnpLhEXscABelH1di-uKvhA3Q--JovL62N-xbeEfSpMd9f26hJ9_j8mjoAwLEzHm1pLoKn8amllc6dvSDxfICAFsJrImqslXO_1t11vgUCoRK5_k2zNDS9VbkiiOdSTpzSK6Ysfpmg-A3un2eVIOwLQHI65pzGSGFg68EmWVla9KKSs9CUNtuemXJ8KL8xNFgv_tTTMYNEGcLYaq6_YcD5v6n4NsF066I9ujDyewD3ghgNnFP0aN89A3cgMsbA7QDBUoyzB4vfDn7X-xL3lj7x_JB-rnHhujVf-Sou0Wo3iSVN-Fwv9h8LXBThbOeXa1CmSbm-wC9_VFNGq0xEg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=UDmcURaBvjar54HZ46_mDhU6PWIl4j6RJL_jPNQ18QnUiWoe2R2IQFlsub4u6w3I0gX7KzdFZYS6nWac5C9Wy-1yj9zDhvBVbFGIF5AGl6UGa4locrBk9KfciT20Gl1ZP8oghh42ocLO3dwZ9U68bvA-kTAyn333wdDWyNDO0_T0eirkA2r3f6GvWlbC3OxDv2qaM5_xn3YE5HbsjX9aKOpd4s1C7EDmdP0Dhz_a5JA-mLvf3YseR-8soFxpAG71_qtfRNT7c0yhv9ZNoqNAnRLXl8Om_B_H9X1ywiNH5CKchWDtxTEBcS2J_UEgrqauETHzqfQYomzxh1lb2cZqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=UDmcURaBvjar54HZ46_mDhU6PWIl4j6RJL_jPNQ18QnUiWoe2R2IQFlsub4u6w3I0gX7KzdFZYS6nWac5C9Wy-1yj9zDhvBVbFGIF5AGl6UGa4locrBk9KfciT20Gl1ZP8oghh42ocLO3dwZ9U68bvA-kTAyn333wdDWyNDO0_T0eirkA2r3f6GvWlbC3OxDv2qaM5_xn3YE5HbsjX9aKOpd4s1C7EDmdP0Dhz_a5JA-mLvf3YseR-8soFxpAG71_qtfRNT7c0yhv9ZNoqNAnRLXl8Om_B_H9X1ywiNH5CKchWDtxTEBcS2J_UEgrqauETHzqfQYomzxh1lb2cZqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=XW4Gw6WK6IDsj9WWu7Vn9XSyDx-rSU5khNhnMKM5VinWd2NeIa7dU08Vc10RvPj3woq2JrCqQaJ2PjIP5LLFaF-bPZA-ARmXQepQrC7NZhxOxRtL3aiBXv_ijJCbIgYDg6keUoxUfz6HOX1fdmHfwZTQvaXby_NY9GFteArowaD28XEmh2T1Cls8SrbEJ6CoijlSLrYxgLvo8ZRULOcUf_jjVxPG2DhYy89vYf30P4RHcmYHM-3Xoo1OaIheNDJPQG5BDjnKSWpMSajXYe0FrY6kCs7SZ56vWzwB_5J1nGPjr0hdGRcbf5xi_2tAkccHhNWCyhWWmiXTuHdWCH-W1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=XW4Gw6WK6IDsj9WWu7Vn9XSyDx-rSU5khNhnMKM5VinWd2NeIa7dU08Vc10RvPj3woq2JrCqQaJ2PjIP5LLFaF-bPZA-ARmXQepQrC7NZhxOxRtL3aiBXv_ijJCbIgYDg6keUoxUfz6HOX1fdmHfwZTQvaXby_NY9GFteArowaD28XEmh2T1Cls8SrbEJ6CoijlSLrYxgLvo8ZRULOcUf_jjVxPG2DhYy89vYf30P4RHcmYHM-3Xoo1OaIheNDJPQG5BDjnKSWpMSajXYe0FrY6kCs7SZ56vWzwB_5J1nGPjr0hdGRcbf5xi_2tAkccHhNWCyhWWmiXTuHdWCH-W1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=hWuQ08SktoRtcmm4-U0smjz3XwiaUe6VmZD2hK-A0QYBmjTzKeNeQZA_4XJIQ-E6RRbn89pem7U1HvJBS5Uw1o9r9kYrCfhUmScddH4CzpmaDWH3IN9O34ip4NWemp9zv5DsHjgwhohHRfn9cqmkY5q4gx0izQjinlLIXH9IoGYb7j0zjFDW1kQtfuFrBGEPUIlBC3XeROu86IgrknbnMuv6LKI3I3h6aAdS9Rh9YbDVjWxs77bBWUNf4UvXjhq0ONv4-xPkXpuKw7M64vzRwZ_KhxZP84NkSBRfnE0R7mXLcKpBoZCtVjjhFvfhtjOW_v2WK4zR2g0M7YS3BBeNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=hWuQ08SktoRtcmm4-U0smjz3XwiaUe6VmZD2hK-A0QYBmjTzKeNeQZA_4XJIQ-E6RRbn89pem7U1HvJBS5Uw1o9r9kYrCfhUmScddH4CzpmaDWH3IN9O34ip4NWemp9zv5DsHjgwhohHRfn9cqmkY5q4gx0izQjinlLIXH9IoGYb7j0zjFDW1kQtfuFrBGEPUIlBC3XeROu86IgrknbnMuv6LKI3I3h6aAdS9Rh9YbDVjWxs77bBWUNf4UvXjhq0ONv4-xPkXpuKw7M64vzRwZ_KhxZP84NkSBRfnE0R7mXLcKpBoZCtVjjhFvfhtjOW_v2WK4zR2g0M7YS3BBeNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=r201VltzuQbNkZvcfvayrEnAQmByDB7We05x4jOsQb_IBTmLcxYPeBW6lwn_xTVTUqm18wWB2AB2m18g4I3lozL_zRqw92ntuM2SDc_BM81bDrSMLcNR16HiWvrUeUQPOGIm-BLhuwP5NxHwYHbezldmpF5Q0ms2GgbrZQnmFXdSO3AoeGi3F2NV-tsEYvk7q_tHK_YTWgan34NBJfxaZiHxVn1RpXpVKblNxMuF23Tdr_Ho6qlnrgzB3F6PXKQBmbpwD5HI5qu6caFeadpdyQCOeJiSeqvj_4cr0VCW75YOMKonO8IWHt_nmQf0-oTyDyO0EC2jmz8noRcQ6LtY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=r201VltzuQbNkZvcfvayrEnAQmByDB7We05x4jOsQb_IBTmLcxYPeBW6lwn_xTVTUqm18wWB2AB2m18g4I3lozL_zRqw92ntuM2SDc_BM81bDrSMLcNR16HiWvrUeUQPOGIm-BLhuwP5NxHwYHbezldmpF5Q0ms2GgbrZQnmFXdSO3AoeGi3F2NV-tsEYvk7q_tHK_YTWgan34NBJfxaZiHxVn1RpXpVKblNxMuF23Tdr_Ho6qlnrgzB3F6PXKQBmbpwD5HI5qu6caFeadpdyQCOeJiSeqvj_4cr0VCW75YOMKonO8IWHt_nmQf0-oTyDyO0EC2jmz8noRcQ6LtY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPaWNmtAmIcVVdN4Np0n495OBUtBp9vIU7GVWkyrEQWYqz2mF5gTPAXWmIc3VcxwF_4WrwO0yaq_L480c2oWZJc98GZugjRtea2DOx7b1QANtDIZOb5BLXph5oZKyXvRAGnWVJvbayrcmCA64kpjVz-4GtqpGpN6iFhFRO7xl5pdDqni1F_iHS51fwtxoy-JqwxJDgPR08VuqFxJLo9N6Ha-SQUdsyXDb-EabemFUHVNxbTrcW1tCUdDlMtRltoAS9vMKoUxodAOveRSdOMaMK_VbMrbSk7kz85GlMPOUB2POTGCa1VgcNNeDywzGusdsD-_I3QH3w0yDvYbTPXkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY46CnIybLWW1mW8BLpKqVDtz-UJbIwI8fcqZWCh7qKT0nNaHvIkbcjgYtU1hgVWYeT7G0cT_U5BG5tC5ajfdQPUG-Z1igYe66X2Zf0jIsydyn7VXorg4GVtOt4T7E9V9IKbR-nxO4tNVW7AdIgNyNAMpzQ489PSUZeiB8zm76WDJ5yzyQlm3wfoJOJm-lk4si4qB-WXL9UgVcD-vTwjOB5swNl8OLh7Ws_Y1TleCt480vOWWfFMAdbL4GZHgEgBHtyPDBQkKQMv93Ii8pz_-FAQbUfCedf4T6NaZ-go3wrPVUfNzCdP7ApBqPyoBgjqKw7GU68kpD1bd3Je0msC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=nEXfeO5cBsfBxA9VrRX7j3hOAB4DrvPlMuaZjzViBSZs22oymuUh5uTB8xAGRrohHcED8XXQNsKVR2vdtWSPIEOPuEKmQf_umbWklh1Jvr_B-j-X7rUUEkiw9tSfM03niac01QgebpiMAwvB6zzdRAV-xCYgnK4E15hcXpDvYINcOn-jGF2RAY2mvbD1m1oYZwNO9RqI4hAnzGmL635dms_YY4I_uEcLv6hrDIgmEU0D0usg-yMKADG2-WWUFNjQlgOQ-epDKbRZcGYIbR9kfje23SiJ9yWfnDEM_8nwOTV6dCf2J2vZ-H9fLs5cistZ30uCVtvdFSqxGtyDvLGQtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=nEXfeO5cBsfBxA9VrRX7j3hOAB4DrvPlMuaZjzViBSZs22oymuUh5uTB8xAGRrohHcED8XXQNsKVR2vdtWSPIEOPuEKmQf_umbWklh1Jvr_B-j-X7rUUEkiw9tSfM03niac01QgebpiMAwvB6zzdRAV-xCYgnK4E15hcXpDvYINcOn-jGF2RAY2mvbD1m1oYZwNO9RqI4hAnzGmL635dms_YY4I_uEcLv6hrDIgmEU0D0usg-yMKADG2-WWUFNjQlgOQ-epDKbRZcGYIbR9kfje23SiJ9yWfnDEM_8nwOTV6dCf2J2vZ-H9fLs5cistZ30uCVtvdFSqxGtyDvLGQtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh99LCTwYnsTyTnlqFnvtZzwY5LKBUs8tTka5xttXWkjoDPPNXgaJhEjTmSEquQmmpNVgGRZ5uF5wOXBghdcCF2X3I4e6LHGs5NXb5-uyrYaTspnsLUPYultGCPBacinXcqtAlJXW8fGP8wM8eJ49mFmqRGwDvLDaK5yDW6IHYG0JVpryuCocGJuYXhnx6dOkTtCKnYt0hk8tEPuocITjMRIWRXil1Z2X6IEgb1LObvmaE9saJkOqIZq028DhaPUbbRuwPVMRXoMC5GXtPeZn5G7lET0e61ncN9LXVKCaN5NTYOsV1id_m9lox1Hp0sF4sOjfNc9LByGgh-Io986cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=pOK0Klj8KlpZO5U2AWLPdHdJK9M5zypsbBpQ_bMGMX7kDjgkGiToe93ulgzoYycARXnlaGjZzT9gSn2-JNoegOAlf1VLyn6sXgBoXBzBfNZT8P09OXOy4aZaUlq_N5wDS7O0PvCbpUba5URY0QxPtPKgMwN1a4UbrEccrt8vl0UVhSQQ8ATWBBaut1Q_6SN6Nc-9jGvGIgkmCS2Swt7i3A1qAGx1CaH4LdS603NWr_yxsCZQ0kLAMLg3BBBIDmoTfuan3NJYYzjep9zkx6WjwHpUU0nauB6nPHTtVX0QBMwuGIVL2foDTqapeMnrK9dam1F8DtgQECCAzY2aT6etfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=pOK0Klj8KlpZO5U2AWLPdHdJK9M5zypsbBpQ_bMGMX7kDjgkGiToe93ulgzoYycARXnlaGjZzT9gSn2-JNoegOAlf1VLyn6sXgBoXBzBfNZT8P09OXOy4aZaUlq_N5wDS7O0PvCbpUba5URY0QxPtPKgMwN1a4UbrEccrt8vl0UVhSQQ8ATWBBaut1Q_6SN6Nc-9jGvGIgkmCS2Swt7i3A1qAGx1CaH4LdS603NWr_yxsCZQ0kLAMLg3BBBIDmoTfuan3NJYYzjep9zkx6WjwHpUU0nauB6nPHTtVX0QBMwuGIVL2foDTqapeMnrK9dam1F8DtgQECCAzY2aT6etfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBIuFJsstbhnoagMNDn-LEcrXbDJTBezPqSZvjU2x2YKQs4LF2Z6H3tIr8G0DzUGQLNgicDvPuVQJuaZ3kaIUPgWwbeCY2kuRjeSRin73JUETHlyG_RGkaH8p_AV5ul9_rpTsjRgJLXhTErspIoRv0lCnZnNlJZ3v5voo6wasm7BHA3-yQICrE7aikpa8kea72XLAArWTLBfC5Z-xTPS5qPK2SY4bZG_wGByhrWTKfzMiQwrNRuYKImNmtgUcGfjZdwn1iRmhY3tBJoFs8QvMyBC8LMRlzexEn0pdMm9YqZAYLKy87mFniT_4j1tQMFBaAh-6NuoCw4l8FYjMWTeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wdxva0cyt-2giPqZG8ly0kZZqH5y3rvJW0wuEVRJz68YFKgFIAKTE9HykTtSIr-z7vtcTKtqT6iNeXnI4sN5287W7YVg8-rLxfAdUCruQWW1EkbfCZ_hRh4YVOlxVCK285bs0GdgOcB-gcc1_zL3IMGlldX4ujKtDLoscuqi3KcC89b_JrTfuIjpZ7S612_n4hE2thTBYU2FG5ZvRgbefKeh8YejyqJlPxPIHjuwRgiW6fy8LLFadFGbSITbpqCcI9Ug6FptlN6yOsX1hHxFUbI-3jsnj1DgnSgTkQm75t8z2ZYj-sn8Fss-mYBQmsV8TIFc2mwZqkqdfdOHgKagKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=gg5Hqp5YKSV2Fl784HQKasewSLYhwlS-NEcykcYNC05SnD3gD_z_RN11oemahLeMlXyLstSIr5zq-v8j_-GpEvs7yn-tnTl-uFE8wfkwAIgaczL-mBTbYbCH-0p_VAMiwymP0m998c917Zk-pVe7NS6ljJPHo3oX44-GkJcMsogNG5p3EoWVqRc707-bbEE5VfZ0KENgKQtLEF62X_vKOn9x5mTsXbs72IruFB1TGj4JF67fyGGHYvBRLwdxbXvnLbjaAIOOeqbVPQdh6Diz1FcVc_B_Q4zvQRhe-W3Jc6KhY1yzsVbZ5Mg2m54vPb8f7GaW8ktf5oF8pl-wQARPrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=gg5Hqp5YKSV2Fl784HQKasewSLYhwlS-NEcykcYNC05SnD3gD_z_RN11oemahLeMlXyLstSIr5zq-v8j_-GpEvs7yn-tnTl-uFE8wfkwAIgaczL-mBTbYbCH-0p_VAMiwymP0m998c917Zk-pVe7NS6ljJPHo3oX44-GkJcMsogNG5p3EoWVqRc707-bbEE5VfZ0KENgKQtLEF62X_vKOn9x5mTsXbs72IruFB1TGj4JF67fyGGHYvBRLwdxbXvnLbjaAIOOeqbVPQdh6Diz1FcVc_B_Q4zvQRhe-W3Jc6KhY1yzsVbZ5Mg2m54vPb8f7GaW8ktf5oF8pl-wQARPrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=NxxI9-U33EpQN65dSFYMZgmkpXc-3zzvWT7H3s_DmLest4R2c65qh9B2WKMn67Ee-Spv9IfqYkCDFXD3832ikZJshNYzRXN45U2IUE9BpZ4MujO2hey_cXvB1uVn8QjHDa-INKUYhXAYk3s7tY0s2Jzytc9b6Qj2uGlHsIC3GOkkX34foZcf1OvHffwSTl6vO5ruzhHPYaolyRhtIMM3MdkeFN1dvuBPaM6F2rJ1GVTonMWGqa3SaXqwH4qDDj0wMLKPs1UbG3tu9avT3DvQzedMi_F8L5MKmbuWYoGLBWzYs5KuZ-gaD4KMzSgP9dAD9us27_SBcq9IY_K0oy5sVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=NxxI9-U33EpQN65dSFYMZgmkpXc-3zzvWT7H3s_DmLest4R2c65qh9B2WKMn67Ee-Spv9IfqYkCDFXD3832ikZJshNYzRXN45U2IUE9BpZ4MujO2hey_cXvB1uVn8QjHDa-INKUYhXAYk3s7tY0s2Jzytc9b6Qj2uGlHsIC3GOkkX34foZcf1OvHffwSTl6vO5ruzhHPYaolyRhtIMM3MdkeFN1dvuBPaM6F2rJ1GVTonMWGqa3SaXqwH4qDDj0wMLKPs1UbG3tu9avT3DvQzedMi_F8L5MKmbuWYoGLBWzYs5KuZ-gaD4KMzSgP9dAD9us27_SBcq9IY_K0oy5sVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onH_lDGIMHH4wT5kxze2PefIW6FgC1l_7dqqBfGOuced1nokjJoKY7_ICigTwLFfpwKKkUjiTLaYAzthKLli-GVUP5vFWGHXPnOLTDoubhJEABegIH-aC9nNBlrVcEfXc7heCZCDID7coUCxRotz5hq7nKMddGCwYGphDQktdqjq6o1EcPPeXIVUt2CD7VVLl2oKFswhCD_vClMDCQKhqwEb0hdh2QYvnR78wS50gE2ZXcu0tqeCmCYbiOZOgpqAz-GlCVMC0Q__wwwP_O1WvKO9GesHNuhlFSBfu5Rftr3H675Mgff7IIjnbUuN3ThaE5JSxYgQHA4wOl0L9_MAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNJHkx6jP9Ti2bibLbSAlBksX16AwdVyTMW8MRCyPtQ6rEm9zzs8qwySKqqZlOsm18_g92UusnX4a5uQZwrSso9u4u5Dux_mZSBM7wO9_MXyEdTssNi0UTW1FBBl1aCEBL64_0SY0XPlIkReiGQ5_ILK2X7_7HR-HsDQz-Qk3XqBJP_UvOCPkG3VN5ZJBWLBwB0at0nf6tE4KIilEfMlSkxFxiavZJEzN4fkNnJRbLPqlo3mO3rsfrcG3Dkqq0RAKui2YC0JROu2xk9rmmRBButA4fFdUTHAjJK0JUEDD6_wI72Te7KDVgI80vEnq5qXdIj_bR_InKUN0SN8oKv8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rflYchfwZDK2dTkBJobr0_bErU5Y0FxDWBlH-mPiF9UrRIua5WOlvQ6eLLlgS5WhQ0Kq-6vIw46FtZypsYehR2MBtEWOu8ZOCa_j0uA2MqjjgrQ6POpWqfUI_cACYp9u52Hy4TZGlIWHysmcLcHCN9pPh8nKbfCp1UXjvZeXewnJ7mkVfPGUfsuOPmmI_a3xXmBpH0eaM8nhAy_0cvuvWFoluro92EZUjJuIRy-272LT8sHAtFEi094sMrQMx_KZxPJZX16XiTTGbsKCszicZXJjrhGGOqlpanPQyf3vcy4NE0p40apQo5KjiR459BoSYV58WDw2S1GjR6BdkBhGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=MsKmgz1r2plaeSsff-dknpxTLRbhbf1Xx1dZ3RVtWeasdHEPT-t6PKoWlqEb2zUgI38WnVSfddFBdIbszfNlEWG4c5zq2PRJoWarxsqPkWDJbimR82rgkv_zNtkWmuDpkoB5PeV-z_-TnfBNl0I6ExEMU9n9DqOMH34Y76oaky6Q5mqNUKhiY6wbaGb5UHT70_tDOys37_JtO0mriHqOJh6sjkHnan8fUvE4dZjSLwnDSRokKgz-q4WYPNdYuEwb42KGF6BYdq1bU5ravucaV4Jwpw5DM4PwfjuVyCsGKGhpNy9Glk7oDDpdWoyQ_WjgTdX4yajArwxzmwwBeceqPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=MsKmgz1r2plaeSsff-dknpxTLRbhbf1Xx1dZ3RVtWeasdHEPT-t6PKoWlqEb2zUgI38WnVSfddFBdIbszfNlEWG4c5zq2PRJoWarxsqPkWDJbimR82rgkv_zNtkWmuDpkoB5PeV-z_-TnfBNl0I6ExEMU9n9DqOMH34Y76oaky6Q5mqNUKhiY6wbaGb5UHT70_tDOys37_JtO0mriHqOJh6sjkHnan8fUvE4dZjSLwnDSRokKgz-q4WYPNdYuEwb42KGF6BYdq1bU5ravucaV4Jwpw5DM4PwfjuVyCsGKGhpNy9Glk7oDDpdWoyQ_WjgTdX4yajArwxzmwwBeceqPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM8-YbHgjZ358P_ZuX6gsA3_EB6KUxANCLdLbnzbpScxbkQYCjCJsrRNccaAYL_Y-eVni_NBnyTDgw31XFJUbidcDnnGEQIRvhsOt7UjicyfJplwKQdv9hCWh93lLzIZpky3sTwcLFNhHiXNd2tTtQZVPFpoYhJQhO9R1uhBN4QjcTjRO3Xir2C0p46CfXagBKMFyukMNXN1RVO9-g425n8hfdNDETa-UxGlmr8FP_OP-S4moUzqV_D6v3QHCfp_focy3JM3REdX-A6nEni90-oSsP271ASJ-N0pMYe_2F2H4XwDK8pvd9Yzefx3WXbrEMUxCgOI6rXvAv0MYOuj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhJeHJNlt9PkukFSpm8F_n0bmnSMr4Lditqqm_DViCjOJRFHdoOAByhpJGwUUrwMI0TZ7GS-81bwwZETrH06xLj3iV6d6ru1FOcoKoWhzyE8WD74Y33IB7zPXgwThp1x7JfnzCj3W67-eDE1y3sXdqlKe91bBOzfRUl4L_kI5ZE2iJbkgJw2_lCoG9XZ_bJkwQm2Mrjz-rxIg5zJtCUvjM8Y2H96JZ4FxomFEYhCVbNGDEftXKjXb1MHcABusomp0hQ2fmbDxKnLZQJVEAdUNL_T040lrAZW7MtfdPU9T7JfSZE3WPohiJ0NsElsL3RopysZsKt_45jxr-Tps_T5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNKmjhwAipTSxjtbvM0_0rYmsruWfOooLKSlW7YNhekiOY2Hanl7BtMWURumXnU56BCpXzG0jpNNOhC1CbrB_e_Z2fDELkPdz_lS_DfIQB58kazS-n0Hu0ucepL40kSN7gjny7EaEWTKEWJU3KZccoEEUrTWIrL3XnBXrw-cOkupkZb9Tzs8FECswoFivUPn9N8biQO2jGePaLsDoVctHs_ShI6zWGeBedzk0-U6j0Zv3At-oI5LjwpUH9FNtx1u7m5LhWsOOS1B9A5Sn-biCVqA2gbZ3mDdHubMk1k3MwuCbJGkhQ_havjvYEVXhoCozy9LXpsNmYo1qpn91PvskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7ajU9PVQ8Sn3EaSVax5da3HFeLhLRUJm9Jeh7p25emnmI6hMhoEp82fiSyH24-GQcXSQTBNiZvBy0WgmVft9dfKNvc2Pzo-7e1nVzXSiu0fr7IgVRSzqo8ysZ6scIg2KrJmR89sRkyQwFk0aSR2pBZPeTSz5TF7GnJ9rBRvegtof_HRTwGcHWIi3GCA4i3MRV6JT-2gYDUN9cbnSCfi-tlSfcOCQkCjzAZmSsMhBkp9nm8_t3fAZx-LI31rqbnRjrNkUKcbtDfVdeSUktgZWg1bkInbeVJ-kcvYG5NWfRFXlDDQ-fwJE_XNQDLX9AMk9GMlTmvFhzHKQ_7TV8oSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=K0hs6lryQSPWs7iS3LREL8PXk_nipf55o7RKYbdsdjfm2ix38Zf_FYbAzSyZsUikbFSiomuzSiYd0q4Q7sSy2bb9QYL0hsOs-W1z3Lm05Ig5nZwk6B2C08mGop_G7IDHY14oy6f8jNQCkg6-oWtoi2T224Zqv_54PMlvM3QhibLjiwS26pj6v5upSR-J4xDLQ_N8xW_yLFgdDRSXb-fcSBnqFgdfIJLCwkWcm-dRC3s_zWwQo3JUtNyKROLR5cyOO3u1zWX5SqIDEBbTg5he8pmzJIIuUXECnVzjI_Zt27GboIUPOOTkiSOfRhJBgksV6lmVVFA57FqaOTJ_-NKi7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=K0hs6lryQSPWs7iS3LREL8PXk_nipf55o7RKYbdsdjfm2ix38Zf_FYbAzSyZsUikbFSiomuzSiYd0q4Q7sSy2bb9QYL0hsOs-W1z3Lm05Ig5nZwk6B2C08mGop_G7IDHY14oy6f8jNQCkg6-oWtoi2T224Zqv_54PMlvM3QhibLjiwS26pj6v5upSR-J4xDLQ_N8xW_yLFgdDRSXb-fcSBnqFgdfIJLCwkWcm-dRC3s_zWwQo3JUtNyKROLR5cyOO3u1zWX5SqIDEBbTg5he8pmzJIIuUXECnVzjI_Zt27GboIUPOOTkiSOfRhJBgksV6lmVVFA57FqaOTJ_-NKi7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTWpRH_UDZUxZ08-fCHPImJ3Ow6Q5kj_phWLWaZDkSf3xsfFUH0Csfnl0uhjLeUktNFVCpnEA8DNiCe-ZbZH4ThWLy_9gJMtT1WlWTDZ9snwIKvCAPG-ZKc7RMtN9lIbjp8Naa0QXh2B-9EWBkWyk0K0WZSsDtnWPnK-wGE7kxwfTXeYJgr_2u2b_g-yvfpbnKE5Uw5qQzOOCue0XJgPIOaZJrRhcWjSma9jKABksW9j0we9bjZ9Mv8GUC1E0EmYM6J3f1TCCmMPuah5ruwu36vTnAc8iA4C47n_vLYWnTNDnxoefOAx2_wIYn6WxrD0YUCJCnjbqYsU873sbVypEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=eNkbCNrJRIoKB7_593HCOwV11YwE_xMF4n_gDYKhQaePrraBxgz-d_VeJtLftrF9G0ZReFBXbNE4du47j_5JAuLY9idF4tZ5s4iGAieNaFdMAJJNcm6ttShBGJtSmGMJPmt3qyIz99TLu-AFtI1sPf6Ym_aseOsxMSSmM2D0CdYN4XTsWRXRRShYZOjJqmPGH83Msz1jC2l32OdbmzpzJTAQ4xDH21yzClwDlEOcOUk3OyUsES26BeYKprvFPQmpTMWKOwbnfNlnDe53j-xDG1iMwcC-DT-Uys8ih7IEvwtQnnygxu48qlyaiqfFlegdzH6dsOQQSlWAkuYMPA-lig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=eNkbCNrJRIoKB7_593HCOwV11YwE_xMF4n_gDYKhQaePrraBxgz-d_VeJtLftrF9G0ZReFBXbNE4du47j_5JAuLY9idF4tZ5s4iGAieNaFdMAJJNcm6ttShBGJtSmGMJPmt3qyIz99TLu-AFtI1sPf6Ym_aseOsxMSSmM2D0CdYN4XTsWRXRRShYZOjJqmPGH83Msz1jC2l32OdbmzpzJTAQ4xDH21yzClwDlEOcOUk3OyUsES26BeYKprvFPQmpTMWKOwbnfNlnDe53j-xDG1iMwcC-DT-Uys8ih7IEvwtQnnygxu48qlyaiqfFlegdzH6dsOQQSlWAkuYMPA-lig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=HqIw0q-GDCJKr8R3gEBjYRlCNa7AngzqbEvU-wwjbwgbNfNV8hoJM7G-nqFMWwRV6JCjo_sAv0AN9IQ6feWv4_b8rfKZqK4ASHHMPdv1I8qeai67wVebHUOP-Xav3kt9_MKRphYGPP9RPgzP_aam_rYf-zmbmtb4sFC6LmhVqXBpUEugGLjoy5f0HfYWHr0Bimcc6w9XFUrYWvSwk3GjOHdtbdoTl97F2ttcPmMviTKOeZvKB9dtTDOYQlkKzyzZ_Z99wjWC7znOfoSU85tZ5eTp0UDrbmgQ9wdQOLADYHFwROe6xdW7RocnHee76wKqrfSAc6SKlQleeocNtRqIFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=HqIw0q-GDCJKr8R3gEBjYRlCNa7AngzqbEvU-wwjbwgbNfNV8hoJM7G-nqFMWwRV6JCjo_sAv0AN9IQ6feWv4_b8rfKZqK4ASHHMPdv1I8qeai67wVebHUOP-Xav3kt9_MKRphYGPP9RPgzP_aam_rYf-zmbmtb4sFC6LmhVqXBpUEugGLjoy5f0HfYWHr0Bimcc6w9XFUrYWvSwk3GjOHdtbdoTl97F2ttcPmMviTKOeZvKB9dtTDOYQlkKzyzZ_Z99wjWC7znOfoSU85tZ5eTp0UDrbmgQ9wdQOLADYHFwROe6xdW7RocnHee76wKqrfSAc6SKlQleeocNtRqIFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGxENpUMSXGn38p8CYxMd1Ptalg5Il9Pl0dnm1wzJ0-2gaMoKfmfz5WAkCStqsv7e7vfcBOYSb4OfuNMyS0yuM8UrZUkAW70wgu8sD9ij2yUBwaWWxeQO99g2dBD4s7ikorsrHluiWwboDfIylvzjHnrqchP6r1S4oyPJiZh2_i-RNG45JG8ZQJ-Pmq-Om5msD9m_d44BohU9gqiG8SV4gnTw4MkXf5DHPPfjpsD5_xUxM5OTkSLCda4uI_Bgt2DJgQOzUh_YDXpufw29Kj6mHgZeBQ_WFS0jZMV8ZHnxsYAVcqf5r_Ir9UQntHLSZxV82LrnqtmWxXq2vgkwAjT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=HoApjuPci1HHiE3cI09_1pMWxIevtN5F8--UonqEYZMJVfOxEP-nHaG-GPOyc4VWe9-fyECr6-IRTIB6ncOB_UqMhNlGpZenT97vJaOaowKc0Q9V5fuJsxffIMXQu-XzkE1dMkl3Q0TtCy6Btu33ZHOvJ3Wi8BHjBUKBqTx8Nr-6396gZaqC9jw1PVdG9m6Ij3oRkUATu--PazQaqgtHNpNloG_x62fqXqqrHqjzGI3UcIIOpzEHiDknh-fuyEmuKFooEUAIDg0POIV21q7Mjv9yEyjnB46k85plpq-EWeteJeYG6-JBD70KL8G-XLshuWjckYtG-4PlRWEiwndgqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=HoApjuPci1HHiE3cI09_1pMWxIevtN5F8--UonqEYZMJVfOxEP-nHaG-GPOyc4VWe9-fyECr6-IRTIB6ncOB_UqMhNlGpZenT97vJaOaowKc0Q9V5fuJsxffIMXQu-XzkE1dMkl3Q0TtCy6Btu33ZHOvJ3Wi8BHjBUKBqTx8Nr-6396gZaqC9jw1PVdG9m6Ij3oRkUATu--PazQaqgtHNpNloG_x62fqXqqrHqjzGI3UcIIOpzEHiDknh-fuyEmuKFooEUAIDg0POIV21q7Mjv9yEyjnB46k85plpq-EWeteJeYG6-JBD70KL8G-XLshuWjckYtG-4PlRWEiwndgqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=oBrKmjv2MU38sNBYuSR7fwTJyvJWweVGOdRg3Zj2203T0gQSpq0gE_erzICjd2E4WEl9L2VNn1iCZnKhUo1uGuVovRPhG2KWZOXWfcyoN2XH8Lj-4AjTHM-eU2tybSl_s3kNT1U2g2ahTZKXH6eYcOMZanNEMJYrSV3G6XszILcvUZc7k9Oxcg1d-mnn3jols0fl9hm7cxgbmi-Ry6UYRx1cWm4z7Le4ZqGqV8fzMuvOZKUQvtuXpib8nFMIM5vVlayHzvIfCG0NM5bE5YNYdtnBC8L2v2pQgpItmYKrWOdxu1Z3rdaNYHNtYPmdnUoV9rzDgzhMmiwwGRW68wqqfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=oBrKmjv2MU38sNBYuSR7fwTJyvJWweVGOdRg3Zj2203T0gQSpq0gE_erzICjd2E4WEl9L2VNn1iCZnKhUo1uGuVovRPhG2KWZOXWfcyoN2XH8Lj-4AjTHM-eU2tybSl_s3kNT1U2g2ahTZKXH6eYcOMZanNEMJYrSV3G6XszILcvUZc7k9Oxcg1d-mnn3jols0fl9hm7cxgbmi-Ry6UYRx1cWm4z7Le4ZqGqV8fzMuvOZKUQvtuXpib8nFMIM5vVlayHzvIfCG0NM5bE5YNYdtnBC8L2v2pQgpItmYKrWOdxu1Z3rdaNYHNtYPmdnUoV9rzDgzhMmiwwGRW68wqqfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWLMVkC90qfJ2T4nBdXb0-K6JQJBuFCra0LW8bxLA652hkFP6BITVSwxYPiAgwLh2CQk8teh9pzBGjYVOOKCf2VIcyBXbG_iN4EvDZT8L5Y7sNpgmEBlXhLBYYtlV0ANNPuDYakNqhRYOxnV0Bz0jngE7kJwYuR4iO-aeALRMaH0yyryS_dObT9fGstmkmydlbTOViU8FPubQexOhgGQOFMvvUnrfLMcfWz8xS9Ybcl8lvvEneA701ihgFPOcvQPkRrVPCCNxUmQNqa72G7riGF6hfMIQnG49OvNiqvsBw5CLajgsjpeY0yg28prqQM8G-WNqKuV2Ncl6F2ACp7D8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMX5_ZdYae6yKIh_YJiHNcqCPSEiB4d1sbdyKO96H-c0uh0ZpF4kjwpAj9SYf24u1HWQeG2NoBXAJhLmXjnHDjd53GW1hDOslfnSZqUWWNOPU3VOox613ppbtvKonYI0_iljKeR4GxIgK_FqEwBim7grf9Hv5cL2Cj6TPcG58PtwVONanicWygsbTN92pAgroSTxxc9so3XcjpPGCA0Fhic_hVkdkq4fg7XIiRZd2A4pzRIedSGQLRZkNU0yCYcBWxPpr_LaAdK40ZXmP1NpXC6kpjDvT4VhFi-vhLYw3_jjMTm69laVOxjtKqgF2w1Dmcj6hOB7n9w3ED2q-76ZCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXQg2EEUBprW3gldt9u7_M_3z6NuXbWpP97LjHjEiWVJ1Gll_xCjWoQFQTkAE7Kh23kp7c8Ab4iTTDtDfs73iPk0WDe1CKktM78-c_VHp1msSTMThhswWRgLHECd0-upzj8n3sIwBRW9MrGjMT0eMkspPfOjqS4Cf1yukLSq1okkEIrlpbQamWyqlbZ_K0l0-KCG6YzReZNGKXZRknUmCKkZBxarOJDq-3b6dK373nCEoANDhS46FwW4ETKJp4PdnUQq7kp0DN9oiv4JcQ8o7bsvPxZ_Ugl0tolz6_0UTo0Wo9ujcERHhmcXJX-CYCcGymBCK_Rv0u0wf7ztXsOEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2q6NJXgzhPylRoholrXRAyAnmscsPWBaVKeSrrViaPA0vyAtPy1nrpxbpLUE2VKYewkLoS1dOvFTc06bWEhnqPeurkkuUx53ExJUYTGtzHG3_UAVes-UJwnexWnuCqIpWAxKVPhVYmZKQ9rOxnPqPbHCatmgXjlg42UWLqzFudU2zKuI85JnZvV5fR0ECfD5az0KxyK6dWH7_kAXgsp0Mel84E02Hr2nATmYomPPaucp01oPBLiTYqyO2gvG71BB9uQZemhQH24714bgSaC1S2L1bfiC7Hj0sFVmSacDIofoQzip18V2QpxE0-g8uiUk7z01x23TTM8qAbrn4cBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=BFncvFj4BFSUIAWxkvdsgG3pAacD73n5C6hmZ3lb4XdAqCYBFNXmRs0m-9XYIK2dLl6y3-dndGxFwax0HuI_brR9PRxYB2-CwJindwPdlVSPl2ohltPK2X65UPcRJE1zoDefP33Ps-w9SY1uEe1m8nux3SIB6OmTKx1FMO6z6Y2gJTVXmq9TkHVa7LbHdQPln0K3aWL6mcDFM-eoF-QJhXjkqulpKEmRSqC-7SphihczIWWpD8UZm9yPQ7GUvo2Oa-B9e0UeKvHe8ZyJTaD-j1JksOa87CcQSVRNVOh2eqam9infmbZ917M-uh_X8wCoX7QZVp1m774cE3AeFoR0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=BFncvFj4BFSUIAWxkvdsgG3pAacD73n5C6hmZ3lb4XdAqCYBFNXmRs0m-9XYIK2dLl6y3-dndGxFwax0HuI_brR9PRxYB2-CwJindwPdlVSPl2ohltPK2X65UPcRJE1zoDefP33Ps-w9SY1uEe1m8nux3SIB6OmTKx1FMO6z6Y2gJTVXmq9TkHVa7LbHdQPln0K3aWL6mcDFM-eoF-QJhXjkqulpKEmRSqC-7SphihczIWWpD8UZm9yPQ7GUvo2Oa-B9e0UeKvHe8ZyJTaD-j1JksOa87CcQSVRNVOh2eqam9infmbZ917M-uh_X8wCoX7QZVp1m774cE3AeFoR0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieFpzTY3PGq27aS07OhnBAxuxXiWMDMLD9OU8K--lA9zDPEtxGe9nd3LQvw8w3YDmb21xGyYSdWFwVRVjL06HirSjPD1rWJ4VyB_3VzS0bVOREhGskSHK1iK9ogOuox4G4HkuGX3Dqp9oXXjz6hLoSFCKTASGdX6bEwgyKEMrNk0iirEbtaB-4RR7hrxDhkQJfUlMiDG6DxU_Bgyo0D-69X5PHcWOpHe6dDkzV9m_GSmoTtdVRU1DxNrmqId6nrnVd0hX-DM1Qci1ooCcxwCrhQB0nk-9-4TncKhbAshhZgmxvmVkcTgjucRjpQ53kGSXUsWJq7VumaHs2Xz9cwI_nFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieFpzTY3PGq27aS07OhnBAxuxXiWMDMLD9OU8K--lA9zDPEtxGe9nd3LQvw8w3YDmb21xGyYSdWFwVRVjL06HirSjPD1rWJ4VyB_3VzS0bVOREhGskSHK1iK9ogOuox4G4HkuGX3Dqp9oXXjz6hLoSFCKTASGdX6bEwgyKEMrNk0iirEbtaB-4RR7hrxDhkQJfUlMiDG6DxU_Bgyo0D-69X5PHcWOpHe6dDkzV9m_GSmoTtdVRU1DxNrmqId6nrnVd0hX-DM1Qci1ooCcxwCrhQB0nk-9-4TncKhbAshhZgmxvmVkcTgjucRjpQ53kGSXUsWJq7VumaHs2Xz9cwI_nFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IITZVQibNY6HRHJEUuffxEQyan3nm4W1GzktpPZLBxlMKAL332KTB3G0xo5502ADPw4jvPLaDiKX7D6emFNfl_Ndfr06fe4oTrEmdKGYOcqxKtAjVV_F949N1pDL9dku_WjO6umtfumo2r9OrgXRvPDFM4Njt-roRNJwwUtb-joeERW7fOS-LPBj11Al-UUaPJo3ogdj3HlyzOHDcDqL1cv4B2g8dsRoOQs_eYPb-Slrc5kYwWdNAO1_X9Trv1sE7vXCsIPSzB5lKoOsMLDAW5WPOpIpXrvJA62VSb-oN3lNInWVIkZhNV31AhDsZ9VFo7kFhYg-g5QvqGiEqFNeVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4x0pfDm9mjC5233st9vmLL3YEtL22vCa9CykNtvhM_9-sEWIOS6nGeR478uFlw-EwyR9t3iXfYb8uEGVdGPdIgCmSCf0_sivQWK6Wzu-BCQxXf3Fotno76SwEcUgmVLYWuAIyt82-iaTKGsW6nEWl-zw0Ewcjy-BeY1U-Xu33JFEnVDsHwoiWspP3u7lm8WZFSz_vmMK-VUGLgFVIA5TV__5tZbBKl--rlf-6u57ulews_6mWQauGAuJEG0p5SuN-CK3o7obw_Rg5LxeBDaI3mxW6z1pxbe3xQgl6EGo0hzl-glsELUTdiggpjnBbtiGu6ny8shm_JrfZngHp4UzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTasymYuehRtGtN2WY2PewVqit8UGW-BTnHuTWdgZLHfz56ywxT8isOE9YkWM33vekm8siNFcFtJZm2NJfbsh4KNrDyUelk4YHzqfoVgsUPDKx0WEFDtBOnUm4BT503EEdIYA3E6nfabbQN5GAMP2pr-vSVgb_iixJbev6MTmX_O0z7ZnNvGRkDGrPKB4WocAIEN1B5lgGBXX5z5pMqlOSbAzoXC-0LvWsYa5GwTaVYzh9UifXrzRonnnRXlcqukdTULwOiGbXALNpNRPCtR6vCx5NbzyYi4j-jv01SLj_mHzCNTNrCORI9MPMcnDxnSr6Y4kNfalwiLsvOctycA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMREmW4PJiMfOfCw8beKN20vYcpZTE5OlkBAFPsfbrXxgbMiS_x5BSYzEfsB0BqCrb3-4cJQ62wb7Nd7bTbVFMqOqkFQnR2qBEW4bH_hyDsXkVGRIaIgov8WYraUU-yMoA16Y9gham7lIj9RW-bYqghXipsQwvjq8sFADi6RpmjIMl3tCiwRA5AY56zl11VlYFKT-pbY3qg_RmaUGMlXQ5RUFqNg-xuKDiCx8Zw3dDcoMJYD4x_seGW3ehGSDcxhc0eWE7Vj_28x0Kl8To90Os5YrKIOJyridxhvJq48L3sn-vVST6ELlTUqQHq_XjNYVf6Al6ZOiKpRqkQs85849A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_TUjxKENgoWlsAAFmZOrjl5-QhpofKLeNYVhrk1pO3dEMOT1DfD10uElvVwC2nlgz4j76WEa9rfBQu5rthsj_xKJAsj0dpHRvOFb16_h4kr8aAhAcVmkJVJPPFKIZT1j_e5ZiDDIkcaekOj5lnyedInvdqy6fhanYu56wER-utPoTl8SDp1cDxmPqjemGP76hmqv3pPNSyUGYa0R1aQR4PmzUVc7EloWtFbMkbUPisQcoabnG78sFr6DdLu96jGFjziFm4zbGFJHThBHF2pnf1Z15lO9Mf02VBPwpVxZclNjUdGQaMIfcKwDAS0TaMyLWMjpjure7XroyF1ccxVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=my6xSL4yI9VeySw16ReslYIp_kFufZuVQR15-tCrGdo84LsVGQlGQlnjI5_RPN3xN74qSZI3DuviHbHFTlUI3bBCDQcWywFZ3nF3BBAxpr3UqUsFTiy5qbs1JmeB93yeKDarO_723oz5RQqnHEw35ZckWj9I5jNw4A-SqBcf7XiJRtctxuW7T4kSWUjv5Z-3hUGirfla85MktaiLAvctzVhnXlsDmOCjhw0NmdNH0wa86_7KdAi1VTzm3eGseX2VW77A9m9uu8FVeDcz90EsUXBuUVvPcg3PB8PsPtMbdN-VBpZUcWKUvVh15GJQJNoaLbBu6khM_HIntOKHcK5vt3fqw1VbWOyiB3_lU2r0VpHBSULfk9IteL9lnnmkhllxW33HihuPCefGk-6hFGfa-MEAwgiWK2J1ERJ10WIRrDPIJXMKAdeiSVXmT0_o4C-kgm_r6UTCMoWqOcs3xV1lNVyXq-akX20evqTjO3RVi4xALbnWVYziKlIuvytRPCkYQO3LucaHbG46LOlZTRCIEL2WpdGHiFuvsoBd2c9hK967-M_q9mEwqAZfMEvyuLFESCUapvmWiNu4Ro9NDmBhsCqQG8eojIPM8BaBsCdV9kJiomGZz7mIgqWU1s1JkZdlHEtMQXzLSFj5b4LVOPKc9gZQwN6JiGO48k4O1KfyLnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=my6xSL4yI9VeySw16ReslYIp_kFufZuVQR15-tCrGdo84LsVGQlGQlnjI5_RPN3xN74qSZI3DuviHbHFTlUI3bBCDQcWywFZ3nF3BBAxpr3UqUsFTiy5qbs1JmeB93yeKDarO_723oz5RQqnHEw35ZckWj9I5jNw4A-SqBcf7XiJRtctxuW7T4kSWUjv5Z-3hUGirfla85MktaiLAvctzVhnXlsDmOCjhw0NmdNH0wa86_7KdAi1VTzm3eGseX2VW77A9m9uu8FVeDcz90EsUXBuUVvPcg3PB8PsPtMbdN-VBpZUcWKUvVh15GJQJNoaLbBu6khM_HIntOKHcK5vt3fqw1VbWOyiB3_lU2r0VpHBSULfk9IteL9lnnmkhllxW33HihuPCefGk-6hFGfa-MEAwgiWK2J1ERJ10WIRrDPIJXMKAdeiSVXmT0_o4C-kgm_r6UTCMoWqOcs3xV1lNVyXq-akX20evqTjO3RVi4xALbnWVYziKlIuvytRPCkYQO3LucaHbG46LOlZTRCIEL2WpdGHiFuvsoBd2c9hK967-M_q9mEwqAZfMEvyuLFESCUapvmWiNu4Ro9NDmBhsCqQG8eojIPM8BaBsCdV9kJiomGZz7mIgqWU1s1JkZdlHEtMQXzLSFj5b4LVOPKc9gZQwN6JiGO48k4O1KfyLnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtPy29phiOhZhbELnzdY-yzCH81R52WeedXQGBk_7IdcAMnZfW_h8bDK4Pyn0_re4Pii3llfGbvyvWIGA0JqxzW-VZKXNxDytPkLd7lBYpVbmmS3j5aQQl5zOETzfVVQxi_fbke6-PI-T52tHuLiuVKd4gHhkyms9i-Cx8Iaa0N9YYL_XuqhmxDaxwbz4IOlcq7UWXXJvwOxFtnX_Fkyw4niDv0Tkg1oAeaDRawKC7_TEUtav2tPPzOp8CxZAC5AX74DSqMfeHNgOTRTqaUrMfGBj4UbIn0EUCpxF3cNZGII57Db1InwDOwLCGp0N0sf52NG8Fs3W_nZB0raCAOZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=NuSO4fhO9mT_GcNEAC8aFUNl1L3FHh_aqpgIAx8j2K1Cq_EUJTqM0_tdIc53t6ZVHC_DIxfb9Irw4Pqq35p2YWao4knzUH8qRsn9R17OHitHBQGwQVF4SqcsxRe_zTAujQHLZq72RhhgV_5E3EdiljpfJEtZ5TNblGn-TZctWT7IqoEgMfxvI_Qcb16bBYKsejyitrM4e2g_Vts6nyWOlHUWNnXTjHzY95OFP63upymdibaoUwBDNmkPh81V28eUs8dCuCfo_8uaNct0dWfM1_5TQMufo2e4MdN8YjqUvQqPYZ9iejw-Mk_SRd24x_zK4FL-XdIUjPHihkIiOrKD3Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=NuSO4fhO9mT_GcNEAC8aFUNl1L3FHh_aqpgIAx8j2K1Cq_EUJTqM0_tdIc53t6ZVHC_DIxfb9Irw4Pqq35p2YWao4knzUH8qRsn9R17OHitHBQGwQVF4SqcsxRe_zTAujQHLZq72RhhgV_5E3EdiljpfJEtZ5TNblGn-TZctWT7IqoEgMfxvI_Qcb16bBYKsejyitrM4e2g_Vts6nyWOlHUWNnXTjHzY95OFP63upymdibaoUwBDNmkPh81V28eUs8dCuCfo_8uaNct0dWfM1_5TQMufo2e4MdN8YjqUvQqPYZ9iejw-Mk_SRd24x_zK4FL-XdIUjPHihkIiOrKD3Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=mwnhMU6U9WeYN5CdoAMK91lvzNEMoCD5JJwGC_xrbI15vFM0pfTV1dYSEgKAZnUzELbXEiEFrZ0OxzRK5R8KnSgmNs67wi3VbDAWyiYHqY-su5QGhDxtgM4iJBZ9ORXZSEi3NEzzVXkVKtFXLzXccNdNo66TBrLsEzEBm2vFMmj0QHft86IH_BVCNY-Y4SrpbYEU2iieSRl2wkpxZNVSXD_zsFIDdWxtbcbAidRvZEW1-PG0voUq0Klo8Z65PdeHq88d6mMBnv0cEukYpthJbIDDso4SOil50iDWhGmcGohJifoXT0wqTcP15fMO4-ZABFJomNvOHcF7qpiWmRrBnV5AH9Ig8rE4OY8feRcABZP_4Y1vnVqIP0yuEa5XpOwD2kd4jZyMzd6OmLMvi_1AoVNQdWIseFK7pO1wzc2bOAfl3ThCNT5mpprvh6WPTxbdEw2YFprcvvFLqDEPKIYdhnIzb6nUvPpe1Ec6b99Z3Cl8Ae3uD8KmpIrB27IInse3rOeP63z7boooNP9-2q9X0fwe1XidLFGnoLGyTwrx84muruQ03ouS3KVKpFVr7Qfroz07KU6lK0ZX7OQ4ctEbW5KsVw2sOP4oCqzGFws5w8CfMpNAVSNEbTvHw7OZnP_Alnv6jIGafkz3pE5JxdZq_Z_lfZM-s-UTQwcbvvCs0oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=mwnhMU6U9WeYN5CdoAMK91lvzNEMoCD5JJwGC_xrbI15vFM0pfTV1dYSEgKAZnUzELbXEiEFrZ0OxzRK5R8KnSgmNs67wi3VbDAWyiYHqY-su5QGhDxtgM4iJBZ9ORXZSEi3NEzzVXkVKtFXLzXccNdNo66TBrLsEzEBm2vFMmj0QHft86IH_BVCNY-Y4SrpbYEU2iieSRl2wkpxZNVSXD_zsFIDdWxtbcbAidRvZEW1-PG0voUq0Klo8Z65PdeHq88d6mMBnv0cEukYpthJbIDDso4SOil50iDWhGmcGohJifoXT0wqTcP15fMO4-ZABFJomNvOHcF7qpiWmRrBnV5AH9Ig8rE4OY8feRcABZP_4Y1vnVqIP0yuEa5XpOwD2kd4jZyMzd6OmLMvi_1AoVNQdWIseFK7pO1wzc2bOAfl3ThCNT5mpprvh6WPTxbdEw2YFprcvvFLqDEPKIYdhnIzb6nUvPpe1Ec6b99Z3Cl8Ae3uD8KmpIrB27IInse3rOeP63z7boooNP9-2q9X0fwe1XidLFGnoLGyTwrx84muruQ03ouS3KVKpFVr7Qfroz07KU6lK0ZX7OQ4ctEbW5KsVw2sOP4oCqzGFws5w8CfMpNAVSNEbTvHw7OZnP_Alnv6jIGafkz3pE5JxdZq_Z_lfZM-s-UTQwcbvvCs0oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=K5MFVe5BbvrM-vxrip2UP2XLtqBcJC0sJG2uo8hmu_PQqhqVa9m_J0V1DDpr6kxKD_rw-sMRMGgDpXryu3q_tCkDJaFsSyJEOr827IgD0izUACtejBfPEeez0QlLqHHFhrDv0pfop4nls4jW44OyccUje_i0RZeAAHyJkk5CZLjw4SdEq41ye5xlAwGfnBIDbaYzbelGg-s_enR-s6CxzUbzVkinzbjhpaDQM-8kIxHa255g-d9xbQ-KfeCQHzZB7s-S0H5zXUR8qWv3e5y16-UdcF5XtjCFunfpGYbhsLJQXX-BBr2MzshU1r34WgRGemW72v-Gs-2VrmNu74mEj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=K5MFVe5BbvrM-vxrip2UP2XLtqBcJC0sJG2uo8hmu_PQqhqVa9m_J0V1DDpr6kxKD_rw-sMRMGgDpXryu3q_tCkDJaFsSyJEOr827IgD0izUACtejBfPEeez0QlLqHHFhrDv0pfop4nls4jW44OyccUje_i0RZeAAHyJkk5CZLjw4SdEq41ye5xlAwGfnBIDbaYzbelGg-s_enR-s6CxzUbzVkinzbjhpaDQM-8kIxHa255g-d9xbQ-KfeCQHzZB7s-S0H5zXUR8qWv3e5y16-UdcF5XtjCFunfpGYbhsLJQXX-BBr2MzshU1r34WgRGemW72v-Gs-2VrmNu74mEj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D20BCK-uDpclawFqq6uuQlwWUWOJeMhH795lOTQEsaUkO6ZAdT-8oq8z1El-z5AqDyZxZhKXD0DxJh-tXq-GmidTP7IGaf7QAauvRJqrxy4phMnN3Z7WBspRF_q7pRLAuDVtiKN6l0G3Wah3q1rM8tkLi0lNj5-V-eJ6iR7qh6TSY4TA2ZgvQmk_a9QDPHiUr36dDrw74SEjxFL1eUIURalo1vpjlATyfdXR2MKlCdj3WWUgqX4MkVd2Iudi7bTL6ky37wSu3Rj2FgkAxZsOzYmvKEM_wj2Ee1_tDj-N_KQIwVpYUWkijTNBbDhB1JJqrHETyCpYE3-fn_61zufkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzRwJAv7dnCy8dX3hxNzUeEcO66wkHSZkdhve17D4Lm7XPy_qqR9UQXiR8RnKgRCx7KGsVgXGU4ToWyfhgQ84Im0sh56_j2HwrEaXCxqfhzFOn_XdXPvt0nB5uIx6TO9KweR2EwLC_dZm5HkPCf3kzFb_g5u3dMUvDFtNKCq0GcVrKUevpwvBQRIimMfAdfl7R4eneTgg0fbQOnzj7bH40RWtEdw5BLOzmLlk9FnA9pLDhdH7T6J7dgopBgCwGXE5GbfJCUJgs9RI-8Pw5BS0x3-Bd-sxza3Rkr3ZYLZvb2Ii3_B28HfbZ5Rlm8XAhYRYeNFNl5tYadnAowjJZua5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szIWyk72P2y6SvNNGBLtXI1QQwbZtNnOM1SRgFUSUx_gFfcwNX1WhTmg3nkkOsh6xNZkO6oLLdLesikxlKze0znjdFvfxSx967osylrBUyp8ZdKrpFnTzUMF0ap3bbTUQpw5Qv7ELlkITaHWdttip4MJcDeMIyUL1MNUo1KH_BqqlwNzardTKO1w5letZ3ia0wK0n9BB9--HciaV1VHJz21ZmlNG3S13VejWZ-pLBUw4lgdIYpcbp3pIxqxr8sdjMMftGqiBS1wSODIJwss6rXwlqNytI-sgQx8q6qluixVxWGQpOl9c85dnQTGcKJeq2LZKJ-wmVpnDi_JqT7c_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GadU_M_clWaaHkoGCGr9kiWjfcKvvr-CR1rgcyjUz4V3OMAnchVdfawHa2bino70XyYnp6OTx1WRf_9cFUNuTB-cCQCjYK4JHnLRUys6p74WbWZtJak-67BQa1-Ta-1hS1OjjJGeo0hLZ2c-UrcP8GOhD8lki2eheSLeS5oTNm9CZMshl2dtb4PeMiYAji6BIvplKw2d-tZ5P-QJcyvJoMUYQlVDTWhDBwDikmQXdtLCOS9t126sXdv69LMIeXHDyx4vTHAvwcNULZrjbFX8n-zQ3XR-EYeZyC-csaC4EVDVJnRw5fNAKRoM_Wali0QSI6SOk0nNZbmkdRTLHkxBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSzKtw87r7qFLWMtuP-cbefa6K__Mee0pUFkamGiBqHI1MQRnToRxZyY-HgLbC-gJOv5LbiehQEWJaZ5q6YQ-YVCybDg2IaMf-O1naJTbLy7ILTrfbtd3R6d9_ePp-pmr1hBQ8iKrLm13uPYMaP6DHS3eLXm0Iq7CiQOoOHKwx11E5pJGGYUzb8oR_5SKL5qWBc8fDNHzA358P4sftV2b_u0c1A0q1r2WW749xLHbwWhaJbLIMxSloGtKemBDasdNoP3C-deg6Nr_mW6ZgPldPdlUdmjVTBlKNUOJDUnNwF8bN-VkIyAOpVE-oSgVPBxDnNUlcpKajgH4tp_Sly66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=iy1e9OeIu55yka-vkoESKqbxnMYyW5PkgHV_WekJ4cvp-3U4n9mU1aurWe-_IZrEzBEXqi7-pNZlBZqhOCPZ6soOHnqMUI7kbqBAnWkyZlb2YCzvDg4KFDCLfa-wQmouo5qD9jxyT6rpz18_bWRhjJmMWOXV-vLmWNX7lnMzcOINmhmRwj7AjOpek3a8Ser_1RqHWtZjBDuoHiNsfLDo9hMkQtWEqP6hfRb7XwOo74VCPfal9PohqXM-Px8dBG7gEPW19IQJK3Us2lFydgl6gx0d_rzdrVassjuxlpuA1Mv4x3MQCQbaNz0jSWaSTMDgVn0x04HcJBD7BRzhozq72g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=iy1e9OeIu55yka-vkoESKqbxnMYyW5PkgHV_WekJ4cvp-3U4n9mU1aurWe-_IZrEzBEXqi7-pNZlBZqhOCPZ6soOHnqMUI7kbqBAnWkyZlb2YCzvDg4KFDCLfa-wQmouo5qD9jxyT6rpz18_bWRhjJmMWOXV-vLmWNX7lnMzcOINmhmRwj7AjOpek3a8Ser_1RqHWtZjBDuoHiNsfLDo9hMkQtWEqP6hfRb7XwOo74VCPfal9PohqXM-Px8dBG7gEPW19IQJK3Us2lFydgl6gx0d_rzdrVassjuxlpuA1Mv4x3MQCQbaNz0jSWaSTMDgVn0x04HcJBD7BRzhozq72g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRBaOkQEOGEZHzIBI6F8m2aCuv5uYnVk0s40OZMpkJjdPr8tGiToSudbZrVBfF7nAlOG_mcxGqIaGGfLfyj7vveYj9GkYSzmwHJ65QvfTih3TlupA0ohWh0xQjA2xVsUSIpSj-FDNj6OHDSpjlAVlpOVohr_MFMcNGogJz33a35kJBVV2NM0J5ikOpkd8OLpaFOWH9gnKubfJr6VfJPZGrCUdYStqm25hQafqUKmYO6J77sxI8e4es_yIuNBdM5p2BWiqraXzNq-JerXGEtyd_OvFQDcWSJ8MRVoco3v-eRmAdZ6w_jaKjfsIIStBxJLtyMWcAeBNjcsecgMrx6Otg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTHwBcSlb0cTfQlFp3fR1mxMesFKt5Da5ZhDHhWzGh-5CiVyFamTzuVzIikmz6hF_ljrW9P920mGsoc9137GAmHTIvf406378eFuKHo5HUUgYKWMcwIA0sZL6S4TTg8oOlIj0HGFsaWCzWrJdJu4zujxE0_EzKwJ_5WGWpMIs-7aisudWZdOr32qlYHsJLiK1yk5c22XO82yEYItJHtt0P00zaQ55koGFt5s2iF1IinDYPekq0Bga_mQWHVmSErBrP-zLDGRSY5FIJkl7HWWI8x1BUYbHM9B8PW-jv9b5gIu0hYgQ9mq5G9PSn9i9wbm8ZCO6AuPm9wBxR5uPf2v3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWuNp6U2edM36HKjmF36TfctdJfXbLBnNIrPRCpjT3t5rnrKnMNMdyGraBr-bv2kKdUihjGgijCsp1vJaDLBUI7mqiuoHxXRGvGranr0UNG59iBBdgMf5mg8WmuymaFkvCkQckWXmypJZFIL5lEQUQVt_Atse5JMzN3zWaHISrPN5qLfTHgOLXJQu3XqicR0T7CN-EjSgKYx7KEU68TeAA7qF4aVaNs95okzxZNCevZyRxDUVCN19W2fUd2A0E2I9gp3eFp4Gatbq-G9nS-SYMXjYfNWDet_eeGBxcc-eZXaVBAah11RxEGtzYPX0z6-vQnMX8jNs3NSvZBe_gCuFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdEDJT9ekbT1By9bQcVo5QtJ-_DQt_ibzCpyk6gt58_vUyVmzH4zqmUJHAjQeCucEToVWnHfVrYvZTA0M4NWWWhdvnYOFOWswXAJ-53RznHH6zgZad-e8GbfvxoeShkKCN6c_0DYWf08E8CmU360_KTeFrpFirMaX70mJj2-R7nyDThj1KyE-HZnkUMGR2gZNEelc0gk6fTpsrTLE-GYVRPowm2qfU0BIpQFz2CrPGRJSM9FoiNj09aTuPa_cNi4XOFj5mPbKZ3N9gn_yyXrjdlLjed4xQR7KdMV51QkkOoaEMaJd4q5CGqwFo4sCYPGDJ61SxcyUWMx5PoQ7Aq5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdUSObGj9sKeK9vrTbCkNE-WaV0o3fmJuUtLKada3lfUSkcwlRLjsmz6nFNOIcbLQqEdyw8gQYmHGwxvVDpeYI2AXcXMOR4yDBB3WcueYO_XwUl_cFAjJ8lzZB0YArdkfks3DJOP1-ZqOP0s-cnXQdXyzhojv89bGzMf9ozVdovf0OOjnfvu5c2CaAldGxjtFgwT126WhVE_joHS9iHv5CirMZsgl9Zj4Iv3p0P8zqYWaTN7uQiyxf6jm_Wak0Evfiup9Wxp476iRaQC3zyY9gucQd73zcBiI12dLwgZ9wM8Pdq7zK0Va0UznLQepHSx84MqkzQ_1J4Ql3sKpsl8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1Sy6EJFzUuJjughhWCrkUe89EzEs4TPFOPHgW9PmKMAMxVPIcevyN6BQzC-DsgkBI81Q2H42Mov5mWJjSS59nxN11BGGQQllNAeR6iTZxSp7LIUorZCQzU38Qwjtf5QeMPcAfZisYV4obUGUk9fQOa2pSv1fZq43ufNFKl1yN_WD0D4kJk6QNGYEWZSkod9gU7aMoKkZ0FIRMUS_WwaOYtSHpJcrxIZqN5joBYKX1R2gdqNc_87pO4GdvTUJ5zKdCYVsmQoPs8dVxoW5ssrb1iSwRpV8BD0sL6vz-cdsdWfLmGc1j_67h6RGblE6O27_eILVHSXA53dWJbSAjJyPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0GfPsn-ZBs8LwOZpYaOelAASQaxY5ki6R-dNANA0X4rFwk4xkq1L-wA_HjR8WlnbieAqHjVHORH0XYiwTyXM8QkLfHsRGEpyFPnB3pRIQf54Ik7JpVPBtSYlocLOhGtpbkxfyZYP0bD1uZDAaQyh39JXVzUCSxt4M8zOh1ugj2Wv8lnJlDS4dTAxnMYIXHo_cK-xSZ0cViUoiew-9iq5iDALPMgk3vqtU_LmFEQxdDtXrad4v9FlOLTEU910fWSOEhEZ1pU3GJyN8Ak1C51UKF96ZRehMwz2vChVz7RNKJz6w1hdU73x6sU4V7BM2RuaiFtrfvIMvgiMlvpFYG_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okQ-7C0jWAcy1QkxsmgKUIg33Lr3SPOt1Qew0HRsQ5jceUUab0Z8IaFl6IV5qqzoNbBQd5KQnW10S7c8afPFITg_Em9mU0r-m5MERhzTOZDxx1W1T1iqxCjxTU6oAP8Zyxq7BjIhw1PcMXjbjNveJ9GNXY5wTEs7FRPPN8JA11671zrsOq31aAXzlJFSnff97816e-ly5gdqKgXJfDq9W4C8d4i5zXzOO9ZrcT4VFonhsOHkRrdOuWIXNiY8jR6KmDYF58sFqibq3xVoUpK7yiLUXzsSMOCqam7d8ioWX8PjxhKZbAi0hdAC_iOiw4tiXRZWstsr77VTvik-oJqAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=FOAZqYTO0E6Icg7B1BjIQvn0avmFyiZzv_LR3LTmSLzXK0pDI_6nE8rdZB3ukB5HGzj7kCpN2wU01DsvkM3cOEUujixYZTuZ8QHNOF6QjESHxNQcmM5wsdYW1JRHG_QYRweOf_wO_FB0KwlpEkvRRv_56vYRw9VbmoYvOSEKJa6K3QLy9NH25eNE-8ya8XI021WOabhl5wTYNto6FL3DdKSBUgH7yQTnsQat4NAixwMJ4SumdQBhimQytD38ZNnb9LPsrz4jjyE4gNO5PMpLcPZTytULvGwmFqijB47u9pXV4Kn9ZStVG7eGeXPsTq_gK-hVvE0ne6k45uRPFGr0Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=FOAZqYTO0E6Icg7B1BjIQvn0avmFyiZzv_LR3LTmSLzXK0pDI_6nE8rdZB3ukB5HGzj7kCpN2wU01DsvkM3cOEUujixYZTuZ8QHNOF6QjESHxNQcmM5wsdYW1JRHG_QYRweOf_wO_FB0KwlpEkvRRv_56vYRw9VbmoYvOSEKJa6K3QLy9NH25eNE-8ya8XI021WOabhl5wTYNto6FL3DdKSBUgH7yQTnsQat4NAixwMJ4SumdQBhimQytD38ZNnb9LPsrz4jjyE4gNO5PMpLcPZTytULvGwmFqijB47u9pXV4Kn9ZStVG7eGeXPsTq_gK-hVvE0ne6k45uRPFGr0Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=a2aGO5hfCG6ts10lYYVqrilOJJfLtpITLjcTSQw8zGF4m6Ra6HyJd3vtFdpJ52uSiCWuxAZhCIaixbhyTQoDmmeUYmU4qYHKRWvLXqmuDxm6nYDBevpoHIb9xxtnLevHOOa6Wd7-R7nk-jmwNaumFvtyuOztfXrp9D2wncOCR-SMuk9FI_CLdNXPgS3nRxXK-_AFr8tkr5IOUcKuWfCjdoFvI-rgLzskZwbQQIoJt06ZCvex2fwd4jve1JBFJAv0rzhUzlVj-7I4y63JysLTCDzd886pkK00y1UG_GJ6llCEx21Zo-3DWBTOC1-5e0m1i_r7vCl0BQvjjUL_INdcyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=a2aGO5hfCG6ts10lYYVqrilOJJfLtpITLjcTSQw8zGF4m6Ra6HyJd3vtFdpJ52uSiCWuxAZhCIaixbhyTQoDmmeUYmU4qYHKRWvLXqmuDxm6nYDBevpoHIb9xxtnLevHOOa6Wd7-R7nk-jmwNaumFvtyuOztfXrp9D2wncOCR-SMuk9FI_CLdNXPgS3nRxXK-_AFr8tkr5IOUcKuWfCjdoFvI-rgLzskZwbQQIoJt06ZCvex2fwd4jve1JBFJAv0rzhUzlVj-7I4y63JysLTCDzd886pkK00y1UG_GJ6llCEx21Zo-3DWBTOC1-5e0m1i_r7vCl0BQvjjUL_INdcyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=oC4g64BhmQnHpP1nERs57hL1VG4LAGv8IyrJivQ1GCfIYenA5v2tbYV77RuZFkQDk78x1rzt_UQ_nL9x-BpRh6VzTIuCnveK8yiJ11vEtEL8Zrwkb9sJoC1MMwmwAZKLBUjstp4RXXV_OempIT5fFxrVMWyXdA08Qqvbpr-dj_KDvVBXRO_27Vv1dRecSXfk19lQozGmxTi80ewFuB2eqBSzY27GAz2ZKEhLehh0N6c3wN84uRMqSJt0rfEHgIYHVieh3l0doBgtbPqKypF-fbAryTfkzGJbBzbfbTatD4h79Ifoe-mu97ibxCYD9_bpvizZkCWsv0AcBr1Xu2Cb6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=oC4g64BhmQnHpP1nERs57hL1VG4LAGv8IyrJivQ1GCfIYenA5v2tbYV77RuZFkQDk78x1rzt_UQ_nL9x-BpRh6VzTIuCnveK8yiJ11vEtEL8Zrwkb9sJoC1MMwmwAZKLBUjstp4RXXV_OempIT5fFxrVMWyXdA08Qqvbpr-dj_KDvVBXRO_27Vv1dRecSXfk19lQozGmxTi80ewFuB2eqBSzY27GAz2ZKEhLehh0N6c3wN84uRMqSJt0rfEHgIYHVieh3l0doBgtbPqKypF-fbAryTfkzGJbBzbfbTatD4h79Ifoe-mu97ibxCYD9_bpvizZkCWsv0AcBr1Xu2Cb6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=YwzmSxHKnas5sD95tHNnXZjXl2-93FXlZO6e5M48H23JrefiuHhdHL4XAMjdnKIt6fatcpTZiIcCw-AmXKS_9P42B7gz6js-dN5eNk6pBXoH8-Bc5YL-6ZHNSJh_iwfoVVz54Yx3nl9KML4YYlqmWEZ4N12cct4aR09L7kKuD_wta4Rj2CbJn025ky9NledZMe-55moxScNaK4r7LIT9l8ofF9EEHZKUJsxKiWj8Tz52N3g4Ya1T3Wt7vJX99CG39oAxYQVbdEHbABtfPIJrDeYZgk52ENW9ZKrGK4ZFiJxq_JHbLfxVVFuib1xyHwfNy-mXAvkhSr9Bl7-DGOl0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=YwzmSxHKnas5sD95tHNnXZjXl2-93FXlZO6e5M48H23JrefiuHhdHL4XAMjdnKIt6fatcpTZiIcCw-AmXKS_9P42B7gz6js-dN5eNk6pBXoH8-Bc5YL-6ZHNSJh_iwfoVVz54Yx3nl9KML4YYlqmWEZ4N12cct4aR09L7kKuD_wta4Rj2CbJn025ky9NledZMe-55moxScNaK4r7LIT9l8ofF9EEHZKUJsxKiWj8Tz52N3g4Ya1T3Wt7vJX99CG39oAxYQVbdEHbABtfPIJrDeYZgk52ENW9ZKrGK4ZFiJxq_JHbLfxVVFuib1xyHwfNy-mXAvkhSr9Bl7-DGOl0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
