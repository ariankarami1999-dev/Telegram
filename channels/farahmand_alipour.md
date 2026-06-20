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
<img src="https://cdn4.telesco.pe/file/LKw2Rrp86RoJRNZXzxC_qK7bF_T8LSccWPwEygA2huMj-hdF_lmbUuQIlQD8c-C9a6MyHK0JqEgPPFQJWPl2Q5N7CNYIjMOLkf57N3UQWDmndBc4pkTzFuuQ-dwdB6teseAT37GL0KrSn4kH7GWInaoFdu2XrgwogA9LxNfBsSDZAUSL6SLFkP7iWKBS_-xsxZLbpiUaoFcukyNFHjtO_BSgak-8C_WTeJ4AhPNuORUgLEFIoRJUVBURfER9xI3TAr3IL465btl_9A6XRi1SPmcqnfbIC1vehyc-yM4FSIE1NQKHBj8z6Ile3xPnN69g3gsG3XZVqtsCatp0EoJ-wQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 14:14:35</div>
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
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxyJKAnXOSntZi3sOwYR6XnrhJBQOwOTeY8ND3rpGHq-49Qce25RVtEpyN0Zn528Q68yxOwVkuEnPlKQm3A-TruHQt5Eg5aY1Gn8s2p9GyoxVI4K7hXorBOtCCUolwJVG4oRbU1EZ82Rclp2RH6vlBFZMhcGa0kXGvGtBfGV9bXIOKLEdQrqTY0-Tc1llzqK17iG-rQvOEzsom-GEbG7djVH6Q5vlp1tua6w4kKUvQ6aitaLgJabdd9FzelugCsOJqTV0T0mi0alYy7BHxgv35KthJLnaZYsHbbOOyosdbGvprVCZyixsxD6dLu43eFUr03bc6KfQ6_md4ZfdTk_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5nttENIgEfiwZuj_Reb3t1GJDwvM9OmzGMHBQglcOzJZS7osKp6H4gyPbq8aVf3VEpPlaqdLFGdpugxzWYPC9xIqgHXk7NOM2GvcIyxrOrXfWlYv824aSDBRVOALtBo_-scHBs-rAD5iGr4Z6ZVgBzZNRT__f496MlvWQld8b7LXW_gCr64LhxfrHnvugcxUtiD0ZIIigvohWvnFiQ7lbpW_TxTVCcTxzq97jvA-I1pdz9Kb9NpGk_iDKZaEQJctakHwuXRsOEaNY17-tbUnipccH2djZz_TJwUgrr3mW7Njb8b-_CWxqHV5QeaVNyXImjUppOS-9gZlaeHFDuxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rip09e5DCowT_2bgFM2V4mdcdlYvac-ZajIMtnS1p7qAA4rl37ZZjKlmHja6D4J-TFcOE3Ez_PNFEfOuoPs91wj9k54OW1JNDAFu-ZW7rNUA_3Bgh2FawlbEEYS8tqxo7cJY38PR_WJtmMCcfLV1wfZphVB3MZbocNKJ8086bPKPaZV4T5N0vzKpZRXSprtwa3OS_-fkWsPwv_e6aySm0AW9K1SVRf95N7vXfTYo0puM8tJqpuoXbi8jFGOmRLd3fZpBVewUKc4I3MPIX-TVCK4gpKjGdeL_VuH-qzYqGsVKKj7GCeHIkFpTSXWvY3p5AJ2OKZG1g3w4TYrTpu8BiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvKU02dxYTYH7ce3t7cDFcG3HV9e_NbL6ahNpiXGYwa8j-eq8FB0mqWk42AG50HpkT2MxxU208YVylXzsaAOBw4iP0oePiOaZYkSdOsxFPsVGPviVd-6AQP4pKhdL4CbqyQkX6WOlGuNzCc4q88zHIddaQ5jHXPwQIgnx1tatD4DR4ThilxwAL3O7q2wtVQoe1nBWO-0hW1CbTZUcgmTqOYPQHFh2IBg3vUGa1Q91jEQxPRjJIJ4Gi5WAR5n5nT93pPg8S9NSUZtsNkMmz_7Yqv6XN-PvGqjSK5UMxb1u8_cAO0tDqpjV5G9OBWT9Id5TdCwZXb0PM8G5841ebq-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNnpLhEXscABelH1di-uKvhA3Q--JovL62N-xbeEfSpMd9f26hJ9_j8mjoAwLEzHm1pLoKn8amllc6dvSDxfICAFsJrImqslXO_1t11vgUCoRK5_k2zNDS9VbkiiOdSTpzSK6Ysfpmg-A3un2eVIOwLQHI65pzGSGFg68EmWVla9KKSs9CUNtuemXJ8KL8xNFgv_tTTMYNEGcLYaq6_YcD5v6n4NsF066I9ujDyewD3ghgNnFP0aN89A3cgMsbA7QDBUoyzB4vfDn7X-xL3lj7x_JB-rnHhujVf-Sou0Wo3iSVN-Fwv9h8LXBThbOeXa1CmSbm-wC9_VFNGq0xEg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMJ81dEvikS6WGYwQclpY9Q3kQJUcfWn0QuKUSHgBkuFhuRXVdM8lMJTar1Cjjw8mSv34KqH61d2f5jdeuxpAylCuwkDE2RHTAGdQYw-Z_rrOINAqK546GD3tTkhEafCXhHaZO9q7gUpWIVVCwppUwLMwbZspaLUPdXu3W3q5FnJLimKlCLEtwwNtqfKnc0Y7XRNT4xsq9a4gtA_FifYlJLEJWjRtU7ICqtIrVe_sbMJY7K2iU53er8e1LQ0eeAwZUpDKNBwjOV2qDHX7kgwuaigf42L3GRKPS6n_pJ6JdaMj5VlQI3L13zOZQlkDmQ34dHDkbMsft0TDSg1GN2MeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9M7T_Az68rxXqB4Jw9gRFRW8UMkIrB-JQ3_Tvq3U1WNAhXYipNn2CNNOjjxZaqX_mWnLhEE-LRBwKJkILOMs-7pyukeRFSnL17flZIzh3jiPEHTLw_Yl29STDHeDiHtoN45je80E9YqS2PFL_G8Mnj4Fu10UALV1nkOPjU2dkNt49_Gc8qiZXUHdhMiMAmpCuzb2aKUxisWNTd9635lze_Nxx6hg1YECLmHs2yHGQJZ_WxmXbtNERItb5NcGfW99IO0TAoedPOl_WerAAf3ty3KhzgLc9pHG1Ebz_aIcfdKdzVim_jewh5XldDuY6ji6-CFiRnykN-AUwW4TdD22Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=GgDx_muLgyGl4O7aLq_XqTUPDU_XkUsxH2SU4UM2_NFVGYyDm85WTIJemfoH0v-8MPBKAKOBCCuV9FX5wN8sQVY89TAETJ3OcCFQqCQ9OaMNP_0DnNZCDmyHZ5wUmZDk0NAnzrFcNlEc3AhhzjGMtSaynIwQsocuK-7GVN-D_JbtbO2L5fpBebooGcu05QMeilE3WgyKfwSWUHOHEeis6-KkVfWevgV9OUETQhFzXlXoTjapA3wNVT06-Xbt-8uaoxQDrKmd2g2LfnTSIeOefxTGiHI64ckxevYAdzgnXe_x5AAlahw0bHE_dwEtUzqum4jWSWlfBaCA1r5iJvezQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=GgDx_muLgyGl4O7aLq_XqTUPDU_XkUsxH2SU4UM2_NFVGYyDm85WTIJemfoH0v-8MPBKAKOBCCuV9FX5wN8sQVY89TAETJ3OcCFQqCQ9OaMNP_0DnNZCDmyHZ5wUmZDk0NAnzrFcNlEc3AhhzjGMtSaynIwQsocuK-7GVN-D_JbtbO2L5fpBebooGcu05QMeilE3WgyKfwSWUHOHEeis6-KkVfWevgV9OUETQhFzXlXoTjapA3wNVT06-Xbt-8uaoxQDrKmd2g2LfnTSIeOefxTGiHI64ckxevYAdzgnXe_x5AAlahw0bHE_dwEtUzqum4jWSWlfBaCA1r5iJvezQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR0VQhgAK65nrtXSUhqc9IFkXHh73zknmcrcPhIs70I1AiCm5b2XCx3B7DsoYrCLWKJUQ9aReKTzp25v7oidrlXsoZeCW18FslCvgtpLLm7CBUaJCJH7-VpQrrdWGyW2rXrrVXcqU-y9XmrLUVc_Ltx--bE8MyPvDhrWIXRQ6Y0y6-1uIml8Tw8nL5mgjnD3UR5ybVK2cHMyjgmo3Mk2Ea1dJ0-gkR8I9r2fS2WbxpBlYO9e6Pw4QSYUBE_6BZ07I4uIqOIFyXC8I-37QpsvgyDCWhGpsgby6hQbfp6mshxfqOk9sL0ddF5TUWuzUAIQi5mkSQQ9E-0wIyqAsxLK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=V4TAJ0tYh-X6dDssW3aeYK0Mn1_mT2dWul148veTkXbflypV6jyJvVHkQjhGeqvedUdbsm3oVzukU0bivbz2KwwtsZAiiImZ2W2Ts238V_ckHQ7cAqds63jv4WGmqr670cDpahls7vISXaP8tOsTL9lzgC5gOiaIiAZVCEkdhoePQDTOB1t5f0xUvcvZbxBDgQidkz1bsduu66uC88aHzaDK8aN1-Q7X47npTfGrd-9y9kQ-2lfpvObJdcDq613xApkDbKdRUVQaeCb_snkH5Y3RwV9bz3A9Ry_U58L1NKWWQq_d1NOpqR76daOVf6VcRZylov84PT81IMVUsp-nmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=V4TAJ0tYh-X6dDssW3aeYK0Mn1_mT2dWul148veTkXbflypV6jyJvVHkQjhGeqvedUdbsm3oVzukU0bivbz2KwwtsZAiiImZ2W2Ts238V_ckHQ7cAqds63jv4WGmqr670cDpahls7vISXaP8tOsTL9lzgC5gOiaIiAZVCEkdhoePQDTOB1t5f0xUvcvZbxBDgQidkz1bsduu66uC88aHzaDK8aN1-Q7X47npTfGrd-9y9kQ-2lfpvObJdcDq613xApkDbKdRUVQaeCb_snkH5Y3RwV9bz3A9Ry_U58L1NKWWQq_d1NOpqR76daOVf6VcRZylov84PT81IMVUsp-nmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7c2BRyigPmDJk52i80KENR0Dp3AJmctYteEx6d_NBlGN-lwdW5ZOEf_QNxZeemUfBVmpsadeRNrNMSfz8_TYgnSv4Cwf8tVwCAaunS2vtmk-bHxEggGR5xqrIQ3TdlUiNKlcTOQZB76s-qs_uBAlBMvtg0cAErhBbsH9JAgMtpzRPbx5qgqrc8-3TaA6XGAXbtQR90Jn7MsX2eEuogn_SRWlMDTZFOVnkWCTQkZfWVED1KlKRAXJNhC1vA7GIZv12XDe62krawBs7ORcgVF6PCVa8hwepGxJYZV6t1HEHxsXNKi4OZxTdpo6fOZbG4nNp6CkuGHS1rt13fEBkX1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaEkH8RJ3nv8aX6LgFcSHz9LKUVJ5niwC3-I_gNPnwhCGacScFDp5Li97cD6mojXudD1lkZUv-gOI3To3faXUbba4zq3HKuMOlAxuoVNVEmmzRprlimZlOZejOFZP1PjCMy9WdyAEI8tNKwfl2hWmpVdVhk8Nqu0pzod-j4XQ-KPff09hXuZwje1pUOhMrSIdBFw1j5wwXsw0i7PPifCJ64yr0cFbme7oZvwRmjWTMppaEXxFdUNnqFsVW0tUJDTGrqNUB9h-p4agrcK8GEbS31wQ0CaTWm2SZoN8-IYgMMHYt8MemsRNUveNFo2-IWC9JO9F7sklbM-AWPKNdflLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=JMZFTxmB6CP9xNTi8r1ruxHeyYzB2cAr20it0HencoirlJeormGQAluJ1UY9TQnIutg3sWdgFl4RmlrzaAFwW34rM0zq2ONDhs8OkbF_uTLX7pnHRcQ5eCqc_PW2HkJhjTWZd5uJopVeGyvtXYHR1zMps2YGpW2kCM7gb65cD2UF7kRDjTjod7xo0oW-xo_Awm_Er46FlfDjHefGBMVEm28QfK4mh4PZJ1rxYU1063Y8tNIU6VNra3FOn5aIY7T4eNjOBhHBCMmW1gq43zGF_kCzbh-38mnKB321OLTy4JhJ2mJSUoUdduHe0fhERQXDeUwM1bsohksK15uw0Azwjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=JMZFTxmB6CP9xNTi8r1ruxHeyYzB2cAr20it0HencoirlJeormGQAluJ1UY9TQnIutg3sWdgFl4RmlrzaAFwW34rM0zq2ONDhs8OkbF_uTLX7pnHRcQ5eCqc_PW2HkJhjTWZd5uJopVeGyvtXYHR1zMps2YGpW2kCM7gb65cD2UF7kRDjTjod7xo0oW-xo_Awm_Er46FlfDjHefGBMVEm28QfK4mh4PZJ1rxYU1063Y8tNIU6VNra3FOn5aIY7T4eNjOBhHBCMmW1gq43zGF_kCzbh-38mnKB321OLTy4JhJ2mJSUoUdduHe0fhERQXDeUwM1bsohksK15uw0Azwjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=vfg4FCBVOtRcc9Ptep_5Wri6N-K7P6ydGxqIv7bpKl3w3ezvHzgwAItNPFMNIdNTw6FQZ4_VWNEVfzKg35L1VmoaJlEPUt0-idevTDUnZYKRnSpzGX4WqsXsFoKWv7L8Ic6GF4OzgjGN3GhjuVMfCEfPR8rrhsAU9RKrLX_n5OLvib1beuKLcSHweky21NhsnFuBFVHAkmZ68DK2CjxU_YzJHEarUQ_Kn57sSRrzTUreu_o7q8K3AILrE-YQGbUqcXfEIgYECaZUm8HZGuTInr3oVJEaF919rQkI2VMtYoEB_76MPYEugyMXh0XHkTaEAGzrTFNXTAa1RBWhBgRhLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=vfg4FCBVOtRcc9Ptep_5Wri6N-K7P6ydGxqIv7bpKl3w3ezvHzgwAItNPFMNIdNTw6FQZ4_VWNEVfzKg35L1VmoaJlEPUt0-idevTDUnZYKRnSpzGX4WqsXsFoKWv7L8Ic6GF4OzgjGN3GhjuVMfCEfPR8rrhsAU9RKrLX_n5OLvib1beuKLcSHweky21NhsnFuBFVHAkmZ68DK2CjxU_YzJHEarUQ_Kn57sSRrzTUreu_o7q8K3AILrE-YQGbUqcXfEIgYECaZUm8HZGuTInr3oVJEaF919rQkI2VMtYoEB_76MPYEugyMXh0XHkTaEAGzrTFNXTAa1RBWhBgRhLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDg1YjW232Uh1-7dtGMr-sq6mrmyNUoe_W7dRb_NRzlcivDsfMdpLcE08YVGbw1-8Vp0YEjnG5QJ8BFz6yvzYe6uVawpiV0e2RrCb-wvq_Ee39tANeJkLXWf7LiDXm4ipHUU0vathDhDqP0NHe59-MGvUvsLE0t8ljkgI-MoQYdKKWcB325AULlFwG8GxhXb6Pq_udPeIpB62L1BnWDknk_MnWSK9JYp3YlrCKddARWp-bChKIucd-FBvRcXTMxFlNepzA9zSNGpeeU6D8NDwKzCKJKAKZE95y8Gq4rrHSQ5tsSFQ2ia11DDlXRAaiOSpUpAs7YPBT5y_xQV6TnW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlHgKzVfYQSw0MTs1Ld4IuQtgZogOm9DtvSTVNnTKEZijlkmPYVWKSNl6XAn8VkzCvNYZS0lHY3YLtJ2R2awjl8N5qeUhz0gPt3h25U1zSW9pxG9j0A_Qx28WHIPpaOBMVB_tcMsBss63FJ5P4Yd5Of8xoO4VmtMTp7caTY3TiaYXVJ8rqIRNModRwBdashwFtmKOBk76t-yCG62DKu5V3ONihpO0vQg-H67rM6eB8WE0bCg7Z4FhjZdtc9vrYI2fh-2gxCxul-nda5TUmj2MsZmtYIv8hZZNB8ncfdgUZ-tK7LDAMUNSjjQ208mkfMlXL-iXmwNpjR0HU56VEtGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMPVOKnfShuQgyE6Z7R51sWx1Od8pu7dmLfvMSFGnp3frHAqI4xouaGOo1WE8BFRKakIrpFtAM2zKZclpSXXjv9-HkxfSlxZgBko8RAGEh3jiao67h6whWAQJZD-EI1rk_Rsc1_bh0OVZtPuZRY2bJsQkkNVA_Tl7H0JU-SnpA6RFNrZO1OCt4V-scltpkSL0ZzL2v5mvQAPs8CevK1YBnXWYimNRDHZodI0wWN4gAHTvAKk3JQrqpUejD9Rk9ILlnjLnrqw8RThbEa0tl83wzY6g4cL4yFfxZuPhT_vvkW1keDyOHHHxDSnmO9mCpm_fgKthUD6m2amS_nt6UtsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=aKFyc5GPL2GnkIzyavLBLkSXjueH-zRCD5-5Ne7GSckg33WDrbei258FnrDWzL0M6Jd9Pe9LVtZUjlODDbKrUM_0gF5D1miguokPx9gdwLelKy6q0SA3Ht_2_1Sle663CoOFNPOmiFy335a-6GNNycxIqxcw8e1PZlDsOQckJqYXryzPtjZ2fUiHwZhWy8zBwiE2ITxIq9kD7aliYQooqhRuH8MmK5Tszx_jra8EVC03MSeI5Lx5qzWiEEEpjyi9OlaAcdnbT-S6PXci7mH2i5HH46Bu7DtLVi-oBCyJMs0ZMg4gA0e5plTTyM1qPCZZCH1rkZsmgmoeJrsfncK1sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=aKFyc5GPL2GnkIzyavLBLkSXjueH-zRCD5-5Ne7GSckg33WDrbei258FnrDWzL0M6Jd9Pe9LVtZUjlODDbKrUM_0gF5D1miguokPx9gdwLelKy6q0SA3Ht_2_1Sle663CoOFNPOmiFy335a-6GNNycxIqxcw8e1PZlDsOQckJqYXryzPtjZ2fUiHwZhWy8zBwiE2ITxIq9kD7aliYQooqhRuH8MmK5Tszx_jra8EVC03MSeI5Lx5qzWiEEEpjyi9OlaAcdnbT-S6PXci7mH2i5HH46Bu7DtLVi-oBCyJMs0ZMg4gA0e5plTTyM1qPCZZCH1rkZsmgmoeJrsfncK1sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcbuMaYLC10HHALrEa7NWaBhjZlsQx94zFSRT3ZRd3iVQBvOCLLCMb-RjSJpkOSvxKuEQoErU8n6Om_D-njQ_QZzx6WDTBOC9S0Jr3Odkf2AkDnKwZ5u3qn5g_detmYqNrk-4Jdo46cD0xzqMOKlFErWvMLyJscgEV22lXpjBxxOWeXltx0Y9A95Q6oGOCxEgaHeZP51J0JsuU0jymad06Pzaw3sUoaaqr6rhdup6eauWn9u1KQ5a-xwJbkDYZNOu6mpHcfCu--5tArenIk1b7wvAThhJP3dpiOTrRW12AdCOTkZuVlTMC0EkuCgTrh27rgkKFRRb1XZ7a6dQCqM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK6vud8j3jzIJKXjvYOzjeU0KNIGDeasjOFXUCHiv7I8JXsIh-gu6u99TQq7CMPeMWylyabMb_UY95UR3ZCRycffReEuI8PYxEWF7-n-chBmOwR5UQ-bEFDOffGRYGiv8U7vy8_onJ1lGSzL6MSPU6KfBS0JIXYh8P4xAx2dS6GSCB4yfV9fG1BLrXa86TFY9WjK-8m2hlRbEHIrzslhAfx_mWiZn_eP2UTmkFtF0XBfLCyw4Z2QNQFS2XJDdzY3qiXSi1_Ihd0fMIWR_aQa9CN3I3ZHFmmW4x6HTmLaQ8qsnKyJ9MAl5Cot-mu2qqGqSjoDEX2KxZxtndBVfxIe9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4WZaNTVvn6NziqkrPwAEFS_Tc4bcIZQbdNWxYWL9h52HhTwnyiFPlO7yivvN9fU4oe8woInTwSnM2wgPAiD_UN9CYzM_rH1TO6FRFu2XwpG6tJPkaj0Qfs835mOthO0Ie2ccFyvac_yR0UAbGmdPQXzshuaOFi4pOBOOOrnCaOSyNDLsTjbO5uv0qOTnN51RTPW4a9NqgxJ4pDLMtzigYPjjUeQH-HjiGVXzcdw_aqYeTwsHr37reIs-9PGyO_y9y4Fh510A2ur5p2yeKpPRUr42JlqWGMRHYocErYOSFO_2f0Sti3Jn3bPyP0ct-GyWt8orsk0SykLWPlaVY19rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKtQ_QHl8jPwNmerkJzov949JOYKjYZja3ySOq-UdHQ_BEF-ZREOIleszmxs80dOd4HalH2NVqfwDVabQ7MYZNVdlVkqGGPHsASmQcL8hMD9e0uJagAOVsQDjUeRKNaJVBvpZIc5a-6tT4V0r1Ro9n81idiIvoznyFym9D9uHhTR2VfC-G0cOkokNGKj3zpKGDytQhfHypmoJiKQueaougKaNZ4nrMuPbTDE3bMk1-YZNXsKscThG6wucsqbstWTaQRB9hYDmcdUbTNFr2LOGVBd4MDmNwOdMdwD9CABbWBiLpVev1GwtMuxqnkx6Pf4nOzX4u97c7Kn5oO08b17gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=VcODDPsTcBJR0HSUi7UVhJe_MaT-UpkhX9E_GDcRbRdkSL2hwV_02RKKQ7XLen1snUpSwEy2QOmkMIxpU0z3gGQuCWFfHbTyE37LJa3qTAAQfeaGA9ANZme9ZPXa__abGzrHNMiuS2JI2vYXgxQwnyj404GKHO1Lxefnx-UfzBCq_TwBndFWjlO7JMgunMgzrg-kkQOy3gRi4a3IGApzkg4pauD0ljMws11NqQ4ojShjheVF3UehWYmIc0jq0qGGDniqVND8CemG6gZg8-U1ipoxQzUlTy19SS1PhKWZ5y0p950FOS7ISYbavT39wQNBs6lTGImp28wDvBD5R7UByg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=VcODDPsTcBJR0HSUi7UVhJe_MaT-UpkhX9E_GDcRbRdkSL2hwV_02RKKQ7XLen1snUpSwEy2QOmkMIxpU0z3gGQuCWFfHbTyE37LJa3qTAAQfeaGA9ANZme9ZPXa__abGzrHNMiuS2JI2vYXgxQwnyj404GKHO1Lxefnx-UfzBCq_TwBndFWjlO7JMgunMgzrg-kkQOy3gRi4a3IGApzkg4pauD0ljMws11NqQ4ojShjheVF3UehWYmIc0jq0qGGDniqVND8CemG6gZg8-U1ipoxQzUlTy19SS1PhKWZ5y0p950FOS7ISYbavT39wQNBs6lTGImp28wDvBD5R7UByg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR6Vq48xgizZiY6OPUgJLxHG8FUN1UjxfWkkoBaF439CjxG8i-bngWUTrre8J9YddFyrUfXkzIgLozdaN2wIb_VtOLyCM76axmKIAkQydgSmiz9eur2E-K39EDP6IBOMOSH6x-NbyVpcey7ZNyt4saUJp5iDih94jnajse5SHg9gHAf4GbSimC5K1g0fIQ5Lewpjs3WviMVdHRAizKEOBjyciOZY5ORfE8e2g2MTRQfzdYlcyBH6bdUoe77J_giveuHbquYKj6ObvOY6KEu-Nl5L2hPM5xD76LililC6FOGhBmH3LNtiyUe0ejX4IGn03TEzzjQZphHG6wPZJ-WrUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=F4l-0tG3Urcz8zLdS6VBC0RpW8WYG2lfXqcjbIpf6C-nSnG8lgYMvf5q68UrFQhyH9f1QD5jlqpmv0wZVGp4TlMM-jefM7uNS7dFcgnyvXaCZzDIJilMi3DMKQySFALB8j9OU20mnOt0c1TyXTog_Eg2EGCCGb21iOU2-dZI3CjnegJiSfkjumevHzmf72pS3Dyq5_B8Beb8lvfbeIqbK_tsIzVsaey2YO0ELz5aINbquCHqw9PSAPuoOGiOxbAPkXDISToDEp-187FX4AWcdcPPiNTavwBjoOedNH8g1rNdd-xWdbZPnhVF4vtc2befIn5go5fksMl7QFicz_pRWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=F4l-0tG3Urcz8zLdS6VBC0RpW8WYG2lfXqcjbIpf6C-nSnG8lgYMvf5q68UrFQhyH9f1QD5jlqpmv0wZVGp4TlMM-jefM7uNS7dFcgnyvXaCZzDIJilMi3DMKQySFALB8j9OU20mnOt0c1TyXTog_Eg2EGCCGb21iOU2-dZI3CjnegJiSfkjumevHzmf72pS3Dyq5_B8Beb8lvfbeIqbK_tsIzVsaey2YO0ELz5aINbquCHqw9PSAPuoOGiOxbAPkXDISToDEp-187FX4AWcdcPPiNTavwBjoOedNH8g1rNdd-xWdbZPnhVF4vtc2befIn5go5fksMl7QFicz_pRWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnO6Aho6PAQZOaANgQnbKZ14Ubn7hDsh1zW154vcM9TOt04r3pU7j_ZJQFuw_3Qpfx80an0MieWudCdHXYdLspT9dLKOYEHv4jsTd7Q_ypjaE9BNSsnBGHd37FUYKV7XbvAEqDPqo6UJWQ87vawUoXzaRr_-JjKUP2APisCOTjBC_Tx7qKrgYFM_z6wK2D4jPfCdwv3irOeB6VvdqNSHaVZyxRYd6mSdqvn_7YCpNpnlrfXFRu7pMRafOsQczYp0XVUzNLTMp_NjQMacTtVC1aDgOjOJE8dPsmaee97_I213wcQL9sGPgc1Gravn_9noFX5Y_4JRysCNeZGeg5NTIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=iNhB0rGYboLueO_C_uPI-Hh8nLvkbxqa4MbKG03Ms41ZkC1v5pOEAzCGmc_YtJdCPi9DKz6NRwy68-1DAdLxkzSkmtvVITtNiD3re8JuTKcxQMLeJQmALDesjZiO7gpqeA1qLpprUIeAsFk_f-IzekrgyHS6e9YPzT4nVKPZIEhke9qPTD5aIWCbf6xO5ActHg8GbSTvJB1xXvw3ZCzFdSBfpeIHDH-ymxrXS6ReroLSsIbKsdbEWtIIm0IqlgomCBbM4-ERFDIw1uU2nby2MJsqx7SVspekROceQOBU4DrlxXPJqpdKToLLPJOGNgIdC771SihyACCbbTLgzaOWRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=iNhB0rGYboLueO_C_uPI-Hh8nLvkbxqa4MbKG03Ms41ZkC1v5pOEAzCGmc_YtJdCPi9DKz6NRwy68-1DAdLxkzSkmtvVITtNiD3re8JuTKcxQMLeJQmALDesjZiO7gpqeA1qLpprUIeAsFk_f-IzekrgyHS6e9YPzT4nVKPZIEhke9qPTD5aIWCbf6xO5ActHg8GbSTvJB1xXvw3ZCzFdSBfpeIHDH-ymxrXS6ReroLSsIbKsdbEWtIIm0IqlgomCBbM4-ERFDIw1uU2nby2MJsqx7SVspekROceQOBU4DrlxXPJqpdKToLLPJOGNgIdC771SihyACCbbTLgzaOWRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=BikXO35lPUio8FGKtu8CcGrm9eK_ZGX3sfG3B3MgS-Asb8dFE5SBnaVGEdyc-nqU9F9eGa-4t6XN3I4olobctcIUdjG5fyABNX2UScn8i0Q3Opsl76nDGB32zfDCuar0--q2Cje2uQCHE1_AhUsdHSdoWx7tIEcaVBRVrbagmxKS0F12TGK9G_6EE1KQKqcd3Yze7QDRYtpF-ze6tl9c992avq2pB19G8b0olxt8jtAwa30kcbTupJQJMWXW1wSMPGdN6Rh8ve0pKaAFsncHpLqHpaNRom9TXhbM2Lzd0eyBKVG_iZ157zXbCE2KRF6HsHD2ojuG7QNJX0D8LUVq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=BikXO35lPUio8FGKtu8CcGrm9eK_ZGX3sfG3B3MgS-Asb8dFE5SBnaVGEdyc-nqU9F9eGa-4t6XN3I4olobctcIUdjG5fyABNX2UScn8i0Q3Opsl76nDGB32zfDCuar0--q2Cje2uQCHE1_AhUsdHSdoWx7tIEcaVBRVrbagmxKS0F12TGK9G_6EE1KQKqcd3Yze7QDRYtpF-ze6tl9c992avq2pB19G8b0olxt8jtAwa30kcbTupJQJMWXW1wSMPGdN6Rh8ve0pKaAFsncHpLqHpaNRom9TXhbM2Lzd0eyBKVG_iZ157zXbCE2KRF6HsHD2ojuG7QNJX0D8LUVq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND7ukqQAQi7lKiV2wnIeBIsmPJSGLeml0obklQQsRt6DRwkjO9F3LFeGr6dMQM5lBivx6nXVLHDCbfZgNq56E3E4EVsQ2dJDGigmyJYxKRq4Bnhw_RIZFOnsY5Ka0T5JiFjGPHe185wCa6GwH82XKtHi-PowAiJYn5GSXVuprNFN63Jan6QhVUdOrXN8syTjVkUS1JdRjh2-WyJb-2oe4CcxQFsuHxIKXS74Hw2Je0VXkdTp_L1pHJ8yqKCk-G4Fwwz_wZl2Acys9QDSL7u1SU-2cpRrzOBj_hXhk6usFg77w0KTq9Qmxg62m0YF0B8FXo1cKTqLtpbAPAvg1bpKAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4r4NA1zirpHeQSYa_J00wvc4GimtNsT_tbLokXI08lYoqSd3qpU0N8TIJ2xFhoGtxA_Qa4mg9SSvpTbC6zAzo9sObmeSfco97fzspWzsneZ5yZ7XzktKd9HaWNruBUoVv_tJSqDBVQ2Q3GkrihT143bjL7ab-5BtV2f-o_tbOkPckr_nC5UKhgNAHs8KXw-EWloAEpk-Jv88YyUa2UZ8IWCi7kO4cXPuqFwXRpIfkEfi2ar9VuoBraX-zQ80RwRNGUdC6Hcpo2KaXo-fRixgwwEo4UzqPr4mODUl4Ty3pgMtNaE2yEzr1sbUkNuYhrWVGBLvSlSHBxuiLVwFE-f1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwEm9NvkmcayyYUaes_yjB1vk2gFonKfVJ1RmJb4SLXDzU6yqFPUBta18VflqlsEYzPDCCsAW1DVDSsNInD7_fv1cTDzOTnRPXOP1gdTE8Do30Bu5CULVdr9L8vBQ-vIHLktgO29LmI4P60j4YjTQiV6_9OjjGwuKLU0Ln6lpg2R2Dw0rPPzrKYzcZ31XnnL9QL3BFFniDxRBErqUplfZxVmeddYTFhUQ1kxNrXct1_E_BI1gcOvAPdOFKc3V9mUb2FYK6gZvUwBp5jeSkJpL8lGTaDL6u5JIJDp6Q2O3k87ScrvD9yxmnBPpLwTubiqI_f5RYwunu2MA2ISBxp62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAKrBDwnopqN5PaLxX9EhakrWyxpKTWVIHn-2qTXigj5yhzWA0k6Iqg4Ja2a3j9tRCXAdKqIJyBmmDqOLuuwDiBEnz8JzSYD3a6OmWMgGRloSdcvAfcUye0McAykboMAZJRNSigQ72rWgU4K6DkuSKwXzEgKToCnM5mriIArVVY9HNMTsGfn9f6z0L8DUGoplLuaBkD7bYUjY9ZGVXdQC18BLKH13WO4R9HNtDTm3HbAJYpw6pGDvWB6B_3RCTtpztTAFe2e7lvAYaJ6U-67egIYrUCAlDKVHLsIGUSqOObDWv9OviRc_3xZ5SjwziXESCT56AufppTzIyPQlHrqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=Ospq6VlCDwyBIyh0IC3wE734fjQVKr9I55I8G7tzWjcAO8GIIQK3U3JnFF4hGpH7yxU1ikDD3iCZsyB_CR9L0N7DY9ViPzF_sQmDkWVcj2ZPVmVwC0-EqObxra-ByFIpUaXc5gZ9rAQMzzBFnyrZQRI5TRR53g9UwOMOvLWjgeNVV-6DFGCGAcMhXBn2F5K2GZ3jJdzlqKxAV6BSVSaSDf1DsvYBi63Azn5nVaYXaWfkj99GhCoiwvZDJgIwefO-GafFxAF3RzuN6RbgvBClnMe1jb42oe3K-dIcOPtwQC-w0cebBEcLmscjYOV13l35imu9MufJKB3iF1jRJmTt-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=Ospq6VlCDwyBIyh0IC3wE734fjQVKr9I55I8G7tzWjcAO8GIIQK3U3JnFF4hGpH7yxU1ikDD3iCZsyB_CR9L0N7DY9ViPzF_sQmDkWVcj2ZPVmVwC0-EqObxra-ByFIpUaXc5gZ9rAQMzzBFnyrZQRI5TRR53g9UwOMOvLWjgeNVV-6DFGCGAcMhXBn2F5K2GZ3jJdzlqKxAV6BSVSaSDf1DsvYBi63Azn5nVaYXaWfkj99GhCoiwvZDJgIwefO-GafFxAF3RzuN6RbgvBClnMe1jb42oe3K-dIcOPtwQC-w0cebBEcLmscjYOV13l35imu9MufJKB3iF1jRJmTt-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieA8v8Ecxb0dnDNHSTp9b-DZ37O6oS-lJ1gxsF-oAIVwyqC05S8jRZHEmq3lQHUj0GxV0NXmlds11z5ojAqD3BMntE_yCcqw9JM9cdx1l0BfZ3TjmIgeLpDesdI6wFym8wFgisKRSXW747RwGTpq7ctBmHCQJMca43sGrfFLizmMfUH5QQLlWfB3yD1hlhdrv4nzEnVEyW62E2CM5e_f5YvQT3yN_WyzOCUKj3mi-Ky4veORk7mNGQNo4mZsxskvitFfLPVpb5fM89Bjdm7rmREDOkTPqGpWaq3opkoVBd0tLMfziMtU37HLoyHVdW4YwsLGSrL8Hn92uPWhEmoU5nKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieA8v8Ecxb0dnDNHSTp9b-DZ37O6oS-lJ1gxsF-oAIVwyqC05S8jRZHEmq3lQHUj0GxV0NXmlds11z5ojAqD3BMntE_yCcqw9JM9cdx1l0BfZ3TjmIgeLpDesdI6wFym8wFgisKRSXW747RwGTpq7ctBmHCQJMca43sGrfFLizmMfUH5QQLlWfB3yD1hlhdrv4nzEnVEyW62E2CM5e_f5YvQT3yN_WyzOCUKj3mi-Ky4veORk7mNGQNo4mZsxskvitFfLPVpb5fM89Bjdm7rmREDOkTPqGpWaq3opkoVBd0tLMfziMtU37HLoyHVdW4YwsLGSrL8Hn92uPWhEmoU5nKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_sM3DzXg2HWVu1ZCSbIuxsK0j_lA9wEi5Fa-G-WVlqYrP1uzGHqMteyaXYEM1aFGjCbTKvCSzog3Yg0Ksbts09xNwg3rHDBOhBtYbPRfW-1-5ewu8HUa9SDvZp0GwDw2DtsyR8AdOVnj44-TR0d0e8hWZ4D6k5eavputbIsShRCIDuufv6kNkV4J-XY9ndrc9vQgEnUcmio9yXP9qdgm1iUQ_ERPqcq17mKQCiCO4qC0gSaGWi9CBiiUML2ovhwA1A_F0Cf23Nsb6Fre_LR_-v4DE4DkliWAa1c_xdBiXs-NriSdBtZ5yaLOZ7wecYyFf7ybofsbE1iQH-zxSzJag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6DNKLAtBmr5GI681fTwCKvbUuLjWWOZVQtgZBA9oDFTEyM5XxGNK28xpAnSMVbQSh60SoC9Jhw9xACBFrrEiuK7JA5xE7H15kim42bduo79lPI-oj29JLQFAXW7l97pE42S0FFWHuJOHmZy7lLjZRc3Re7GZ866Txn55UXmnJ1Y-lqUV1SMMD10Qh8PAL_NiCatm_1kpe5Ki6gTgEYIKTLjT1uUj3nRLP56JpLsjaZ-AitZrHz24-dWtyX0b6A7bUuPnvlGooihsfIKHRcUW1ksHYVayjRq_3NURR3vRw3DrEsv9x9EWJCpP4ydrmQpej1sf0PxJNqZyTFTz8M7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0biNgpDfgDvVxZCKCTcYW18DKY0y6KLejMJaji-8h45WLXDBcJLkwS1dY47YrfbqvTqdisHIahOAg7AJLt7-3plkc3W-DSNL9NO7-ySTqg4A0Opjjpm8dnW8X_rceLFrMVaH8arSN2E_wLC3WAH4z4vbICYejX9k6TwTUrRWSZGpF71YEFRgQAT2lQItXgsktf0rSG1l4hhWglgDM-q3EdGgXx4_592BfsDG1ofLl0TLTtyNRvds7B2xnvnjbez4U3lPPWieA7qmPin8-x3nPtNJBzOuGZt-wwKibNUxkCb9D-KZ4bKmS9VgFDyHVRe5bJf3sY1oTmDqK8qjW_vVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltfwchqzKEGd1zd04zbYINB6e5BMoIISiSFsoYdxuw-5E3NvjMDlefcjjzoy1NeDl4AfrU2qD1G2A78qgqXGN8ph5dtFJ6MqKTxo-yb7fNgbaJ-oeNaGd3LLA8bh-viQKDAqM7z2pqYVIs_ZQW17YxKBn1o6V3kQQEWNrcoOMxWWr84SZfYe17fRlTgo3kbGdqo4vFOI2KmllYe5iMWnkgIER62O79_OTCzG8xUmiNuf7ICjoOuiurGHfxxw4HGao-_aa8GabgKACkrbbqlQ367YczpP_5JtbwNXkk4k5qqxHg3CKwXX3bL13bcF_Op4FE8ZKf237lm2hM4n7kSO_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4YI4212rO7cvuZUc4Fofp_qCF2IRqIcQLUjLJEnPgmkDwA7zEYjEqxjylqhItm4gpVDAhaga9J39KrdqaEgKfFdVP3CiWUPsGT8nCNGJbrv8DDP2MpSRYc3NVXcwP3El3gwD486rVB36l6a-jmvuClI3aHfK7ZnQv5gswbRnInpvZa343TaUxFHazlvHCRWjq4-krI7ddP5V-WFqc-7MV25cH4PpT5iXPgLIUBbk-AF_O2KbGW9wpWQfi69_GjiKDbVfVCgcrokN_HAM_kfYrHWSht5l_LFKO63gifOAoAcCaMNMHkSbXBX1z85WDqFSaOzhfhs6JsdxYbgcoBKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=G9f_cdcRDVG382ZeWeeXaxNnX-OxtEA-BTbyu2A6tGU0DNwCdhsD7HujgO_lT2SU2NLVgJyeMjOkgDIFiD3_bzmiewzMNQ3B1_9YvqmtrhuXFw5cVZQWBkoYYF1aYGpTojf3qf85n12JhEq_WcqCoMHzbGMNlNv3MWVp-p020i7EDrQR3_25QSGC6-B4irVcJkObtfL-cmPs9oz-WWPhOuRSmR10laEC8odA2_5kUhycKECbHMczaqZagdn6Skho3cfWoUOc-TUhVSKzmptg8hrQNhpo-B7VM-9ycYKXpJIbax3qh07qKpEeCJ_qPFkiXoZfcENeu4LpW2CsOBrpcDVaE12UNynB_zWwLRKZhHFFoLjACUfQfBTn2zhhqMMFp74aSBX7Z_0XZpJg-q_uH9cs-izdRQUypvDijaR2OyBqUcbY341G-Gs_nv-WyEs0zgPYd06EW3tLVimf8Mnck8ryNPSAevTzYd5qPNC4PW1Hpk9RQAVD09j0aWrhAHyoHcTBmrEkSLGT8ovrA3zonbRN40ovSt6timkhp2FIikjT4q5YgaL5HfDuPR6sL2yzPFCe5VJb3ME5Y0n1Le8wMKaGsspHKDSeCRhwghEJWSVq9O6FG2kPXwxdFu5MfMcRToqbW6P6s7NE3-rPDdHP5Tsf02US0pKQLPlS1xgiqns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=G9f_cdcRDVG382ZeWeeXaxNnX-OxtEA-BTbyu2A6tGU0DNwCdhsD7HujgO_lT2SU2NLVgJyeMjOkgDIFiD3_bzmiewzMNQ3B1_9YvqmtrhuXFw5cVZQWBkoYYF1aYGpTojf3qf85n12JhEq_WcqCoMHzbGMNlNv3MWVp-p020i7EDrQR3_25QSGC6-B4irVcJkObtfL-cmPs9oz-WWPhOuRSmR10laEC8odA2_5kUhycKECbHMczaqZagdn6Skho3cfWoUOc-TUhVSKzmptg8hrQNhpo-B7VM-9ycYKXpJIbax3qh07qKpEeCJ_qPFkiXoZfcENeu4LpW2CsOBrpcDVaE12UNynB_zWwLRKZhHFFoLjACUfQfBTn2zhhqMMFp74aSBX7Z_0XZpJg-q_uH9cs-izdRQUypvDijaR2OyBqUcbY341G-Gs_nv-WyEs0zgPYd06EW3tLVimf8Mnck8ryNPSAevTzYd5qPNC4PW1Hpk9RQAVD09j0aWrhAHyoHcTBmrEkSLGT8ovrA3zonbRN40ovSt6timkhp2FIikjT4q5YgaL5HfDuPR6sL2yzPFCe5VJb3ME5Y0n1Le8wMKaGsspHKDSeCRhwghEJWSVq9O6FG2kPXwxdFu5MfMcRToqbW6P6s7NE3-rPDdHP5Tsf02US0pKQLPlS1xgiqns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFMpX76gnnKwAkMTXJv7pJzOpS2MK6L5NIF2bzjeh119RlsJbO4mu8vJrjjiH5YKCu5CZ8X0FKdmW2vtxl_yFQFi9pozW1epZJWTiwzvLt6v43YoLUF7kZ5sqlYlNVnN9A8eAc9Ob06QPDrrRlAsKr98sOMKupzq6wvpnoLr7i4vMOHjJkyue2b9YzFwsacQGd6pOMGbazoZHtjNAGIlRUCjYJXpXn8zMObxqqKZgeKkrJpbIOiwF8ao7xiTHOeOUjUhSruNkomItPggVZzgzrCL-l-qABhEZnq8TEC_BHWdDU1mwddHqZTZ-Byl5JmUU392KATkWpJDGYl4eEk88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=QvH_DkbwbJ2m87w3kNAjsBX8uuoMXzkWz7i68qotgEjcZnZUHzpFIyGT5RXlHsKM_N6A-Q6h4wR4_D3YIrSiNOzleA4xnnwIQL-mb5fcHePBVQG56lOSfD7SgyhNZaVY0zYpIjMDz9ZTnPhkWC-y1-ua81-i-MY7E_5jC6aCfmK6-x-Y_70IP1hSiRkGN2hzNtOBizvnxgkr2rlweK4lu3X3KDeBs0Ddt5xD3nk7HJoC-16ovF-v13gc75lxVJpMgJwTMOGiEJu1U_9KAY2kVT46fSPlztVJnHFdk1lydNKD4dfqxXCGQGPuGXy3K9EX6ULgPeTR7wqegWvdQ0yWKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=QvH_DkbwbJ2m87w3kNAjsBX8uuoMXzkWz7i68qotgEjcZnZUHzpFIyGT5RXlHsKM_N6A-Q6h4wR4_D3YIrSiNOzleA4xnnwIQL-mb5fcHePBVQG56lOSfD7SgyhNZaVY0zYpIjMDz9ZTnPhkWC-y1-ua81-i-MY7E_5jC6aCfmK6-x-Y_70IP1hSiRkGN2hzNtOBizvnxgkr2rlweK4lu3X3KDeBs0Ddt5xD3nk7HJoC-16ovF-v13gc75lxVJpMgJwTMOGiEJu1U_9KAY2kVT46fSPlztVJnHFdk1lydNKD4dfqxXCGQGPuGXy3K9EX6ULgPeTR7wqegWvdQ0yWKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=EiwcjVy8N4KzAmiR5qsLf1zUku31RvPl-uC-8752EM0QHFIOV7Lv2JthoKZoXmZJwUO7Kro8W6V4Kd6tjlcGafY0prLdm_0h9oa-_f7Zwz5T8prBqWVPlfRoCwQVM9yWXMlrNVl7kyuE71f88gdwEVY-sFuuJRH7V1U0GHcZ-2FryMwp2so7MuLcFAZcv1tWY20Rd5UR3aqkTQe1YVwk0xy7BqxmJWSpYTxJx8QN0n79QfXa7PUGeBIt0R6KgNiHKh0XjhLBUtT4eVvpnjY5D4gBVCDwhvOBB9PTvAmT9u9gX--atGPnV8jgc-4YU8faXQb5AoGPxrCg1m4R8I3hrAOMhgLbogXiDKecQ0JvbNI7MgYUjCbPCaOP5oqcMJ7Ypn2z_wI4aEDstYTdjQC-JQoOcX6HTB-NaozQDsr-VL0xQVW6LElTNLpSzQqQyfEKIzflIn-fMIEtpU8G1-kT6bxyz7qA8pnPtf0fQs6XLmDgdXmYk2WEaWWXSPD0mPc81mqd70-Hu9QfyQ3mqG3xD9X3eVESHuoQhANTp6xX_v5Ap9R-UJFJ0BCI0xYBhTDUUYFmI8I4EBkV7whU_BQO404x-xSrFWg3F9mxsp68M89IzLC7OVQtRa-on3t_AujN3kNKZqFKA6ngtbVHq3G056UnmEJ7aNkuDi5yki-vth0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=EiwcjVy8N4KzAmiR5qsLf1zUku31RvPl-uC-8752EM0QHFIOV7Lv2JthoKZoXmZJwUO7Kro8W6V4Kd6tjlcGafY0prLdm_0h9oa-_f7Zwz5T8prBqWVPlfRoCwQVM9yWXMlrNVl7kyuE71f88gdwEVY-sFuuJRH7V1U0GHcZ-2FryMwp2so7MuLcFAZcv1tWY20Rd5UR3aqkTQe1YVwk0xy7BqxmJWSpYTxJx8QN0n79QfXa7PUGeBIt0R6KgNiHKh0XjhLBUtT4eVvpnjY5D4gBVCDwhvOBB9PTvAmT9u9gX--atGPnV8jgc-4YU8faXQb5AoGPxrCg1m4R8I3hrAOMhgLbogXiDKecQ0JvbNI7MgYUjCbPCaOP5oqcMJ7Ypn2z_wI4aEDstYTdjQC-JQoOcX6HTB-NaozQDsr-VL0xQVW6LElTNLpSzQqQyfEKIzflIn-fMIEtpU8G1-kT6bxyz7qA8pnPtf0fQs6XLmDgdXmYk2WEaWWXSPD0mPc81mqd70-Hu9QfyQ3mqG3xD9X3eVESHuoQhANTp6xX_v5Ap9R-UJFJ0BCI0xYBhTDUUYFmI8I4EBkV7whU_BQO404x-xSrFWg3F9mxsp68M89IzLC7OVQtRa-on3t_AujN3kNKZqFKA6ngtbVHq3G056UnmEJ7aNkuDi5yki-vth0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=HtNxDQc8XjHNl-Qx9IdWATcMkH39PUoZoqVy_V1X_i7dog7iVJmkWmO1ksZLS5-IPdcOt8z0UMszYQY9eYF2lU6-1MPDWelXYd_eMmtI0IBtStQhWgdJ2CqneVomX8jUlskLkPdpcsN9oChEy9OJCPnRAUbaxwhKnMw-tBIasdI58DpVxjIe1rtoCL68Q00TuWOcXG-6v32Wdb4qdm6Gf_b54pMEGKCnUgpRH8DaDeUgKJJxtyElzrXYXtn1rIvzwIy9g7jonUgO8Av0k3C7DD0TclLCf5eL_S4zA-buJ7dYILxd1hLYLQzV6YUDCQ0L6yaDz5LELoHPQnZ76iRVeoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=HtNxDQc8XjHNl-Qx9IdWATcMkH39PUoZoqVy_V1X_i7dog7iVJmkWmO1ksZLS5-IPdcOt8z0UMszYQY9eYF2lU6-1MPDWelXYd_eMmtI0IBtStQhWgdJ2CqneVomX8jUlskLkPdpcsN9oChEy9OJCPnRAUbaxwhKnMw-tBIasdI58DpVxjIe1rtoCL68Q00TuWOcXG-6v32Wdb4qdm6Gf_b54pMEGKCnUgpRH8DaDeUgKJJxtyElzrXYXtn1rIvzwIy9g7jonUgO8Av0k3C7DD0TclLCf5eL_S4zA-buJ7dYILxd1hLYLQzV6YUDCQ0L6yaDz5LELoHPQnZ76iRVeoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUh3zeqvGe1IzGaVP5suktQ2t78nfxb27q5BmwaKLZR5EIFQg2W0DmUq0z9LlLnZKoKSJ9zhVEU1yquJEBViihT6f2gc03Ja3awcesH5ZIHU4lGG9zPnVBhmTEIUwQ4Jv0_hu0-8ox6_KSmuIJxaewWb8bTQKRVowFsW5SGzMrX1b6RwO5eeDMwYUMHKypdlrrXZetgsq701Q7tezodAXrlwKdAziglUoDre76CvYFqzxX-9k_Mn8ZD-nP8a3uNhydCqu8F-s7ETx6Y31-YAmvr-ui__DdD50gYwh3704hP366F0B_hUcW6QmNH-kVzzRKjJkKws4NW4LP8YvYloLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFYAupdoxN1Q6PZRFcUkCZq0WJxlpPHuA6KXf61tLGHEQ8aiDtDp2j78TCOKfztoK3dulnAPl_N8pfEz7XUBBR1lPF0hJ3zUESOibFwDmKKkrBwE3SQsfZbQYINEg-MRcmP4ieC1Kr4xot0_KZgeuEZrR1AF2YxDThcQk4hv_pBpDCWOUczHCE-403miDHBqY4zsEyQJkkhhUsBoLXyJxEtPtzqNMXqyrkXak0qYHxfFpIAoZ0Mdi3Uvekpupan4VoDs4yFTrUh7QwZHSzgL9rVd8ygCkxp0WFjgCEwxzJWCKqSS26Jc-CtfLWNR5a3P2YvlSGfpgAua1OzQCXuuvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wne2VHp3WTAJfReuHAkpd4Ch6R6f5wIvNMYYCiPSZv0BTtvLJs-Eymo83zRPYvQLu2k5u7UoP9DJtDEYBvyfE7YQ6MJx-P8aGkNtZXHSFjbqw1anq2sVwDCOj_03WuXUgeiwpTmOORxZnMNqnceLwwaILG_TK34n1FIwrRgGjjGyySbCZTxcBpKBuA7D_fPNyIgm3fOTuSynfL5O5DQSPj24eparSG_HMKh1WQZZFyRAWhhOmxtAwk1SMG655f0tQMsjw14dblI-Tp1UPQphT5zU5GXK5wOGo3x37W3uicVflVxldpXJgXvfkP8tXxqQToO437FVBWE0dJJmoGfOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H07_0X672_LnEjgwV3uAbE-8yr2dT5QiGiXNXyi2owLZBcyMq8tmlpT1mVU4fHv9-l3InrevF6uN4K1X5ruVWgFIxTGzzjZwEQaCbdJnXwW0GMLedIHU37Cy2Kd-WUwwuza0iHqiJOL7ZUg6lDvzz2tdWZQb4i0PLfm0a7yjg81JrfJGyBXVBF70WUlnoCusfLFqP9fkn2cf1U4VIOkKVKltJMAXXyc7u3IvXXaie9Hh2jPhkrw1GYA-E9vKcNMU5iLmU3vnnk3G9TvRGLqr4KY7LU_dsOUQtPxBj3xXaRW4GCHi8LOqmV8jzmNXgVjjVEubGv-FQsNQXudzPzJZvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzSQVonlZxJcxqelMWuE02kuPLfoNggva2N82Jc-qBeonKecGBVPQuR3GuFC193jLE0dX31XYWfUpKoWKSGL6qupgDFLah5ymbHWR0yY9zAc3xGiI7GUyXbQ54mcrg8LPI2Bq5Yp2BAl12OBDn6wKsVsLvYPkyRgcy2MSNvTAjGAxZTqEPYovdQlJ8qbFkvVJvD8Wowmen07p_jtlkyqMwsMBSAX9eXxrVDwYdG68Z-3Titq09hm5cP4_rdnAWc4L3mIu5LfyiHkZynD2goyg_rCxY-Ure9xeymN_b2fFN8JTFB-2y5PlaYIWb6HKG5GJg6Iv1De25qAETxU_3huow.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=MwJnVzGxrimjV_b5XPV5v38FLYtc9Ef95OHVVNMru58qxyZKgoKOOxJkd3Disq_qupxWEK5vs13hCyoOzhMUBCdq_7M0nR6Y3x5Gf5v2bJJhpWHiq2NVafQNJ-36L6ZSQYfjtJ9Z_ZpR8DY5Qxd6Tw3nbbiPqeTsn4J0Tm-Bwq6-l-8PyibaoXHtHyMMcx72FWVeowp0X26KC7BzzrR3yE-adR3-avMS7PKWRGzeBJe0VeHaNnv34jVOnLOT-F9mPoWalvIFwW7oG8eKtxx7t_LriJ3gODddbrYNiIca4vcaKH-RzxlYT5ryJewcui2D85EoRgmSitHYeTSANAcD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=MwJnVzGxrimjV_b5XPV5v38FLYtc9Ef95OHVVNMru58qxyZKgoKOOxJkd3Disq_qupxWEK5vs13hCyoOzhMUBCdq_7M0nR6Y3x5Gf5v2bJJhpWHiq2NVafQNJ-36L6ZSQYfjtJ9Z_ZpR8DY5Qxd6Tw3nbbiPqeTsn4J0Tm-Bwq6-l-8PyibaoXHtHyMMcx72FWVeowp0X26KC7BzzrR3yE-adR3-avMS7PKWRGzeBJe0VeHaNnv34jVOnLOT-F9mPoWalvIFwW7oG8eKtxx7t_LriJ3gODddbrYNiIca4vcaKH-RzxlYT5ryJewcui2D85EoRgmSitHYeTSANAcD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAdHa1aGy7l2sWEQwjl4NlG1B0N_YtLGzbQCAfdtrpevR1ebLAgFBNRfPl3YM_hCWQlsT-LPfK-ouo7JBzE5gQLI8lB9LskbvX0Y5MkvmSoJO0wA9OM1VEHeYWUG6MFzpKHFovlfJwx9d_4YB-3osxja7qZqymkt9C_qfxXhBpO0-z97laVdiekpKVK_1iqz68jvuwM3e9oB9Ev8t3tCS2Ck_hXwRK7_UD8a2YoAZoSQK6Iqz3LoFGQrXHUgAnEmeGVYG3O7Rh3ZL_nf3KqZGM3vExnRXKRe0M-aqPuEh_ErEiLZOhe_ApxLQ3PFZKYrE5f3bLN687kpPcbZg_REDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqWg5YroxSSdspw7Bcpq40w6ps6mxGS1lvx5M6XMHsZRAYXiTvbu_C4eQEkiJjgH8OvPhub0LrtOJqD3LayGEJrohPjMavgMJIfgz6bXxS2cD8xPYTdE1zQdJd44_xROVtxbHIJ1oOZlEJBoe8VijdPiA5hevrz4JDgGZDIhtjgWQimDOeiwH_GoqOxzmInvYSfMDK0sEYouVsjn0mqWXvuWFSjsYJGjLXwjsaJoh39kS-tbgpa-9xfBzf9IK5Ht-RM-1ZBDyRAvnJHO6C3U9zjDYykK_9YkFfMsii4eDlYcvPyPwiaGg3hpaVjUn-VAlExyN2tDJU1UepZbTYsN_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1RGBoWpGutn64zUrrX74FRmORcJ6AENuZlVd6XstW9nRIXIQXLyDb2Wm0uhaDjk0v5Z1O14mbIXuoRhhZTkooSA0byD5_gHBBAGsEsWwzW-jrS8X0s6jXlFDRT9RQzD7iqPZtHZaxyKasmLQdvUbLcliSl_eFeoXtWe24n6Pt3Jm35AyFhnB37MoWeMBIpd6UIPK4rPFO2QynSBPI5RQ7Dwrix-GbSdCwPuXPldlxhhWxcQJDCg9EViFl6PHC2nAq5GpR_m5chPLTD-z6Qt61RKxvL7knxScY6IQ-t0WTXNHyZY-3mC5lf0_KfYe-k6RtlWOU8f-i_MnFmw8wg_1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfDXaxYwZ2ihZHjFIMsMB0fEpOdM_Ml1bN0alXdnw7Xe9xeL82duahOsQynlj2uZntaVI_Wi2HVUaC0M1Rq4WkBDc8nDrc0KD-QlKx8dQPe65b6ZkuTwvEpPkzROWKU-57X2q9ZtUL4iHK6pMwxaSrTr0Jk22Az192PysqvPanqp38jQkvrosE6sxiu-rAdJ3852LI_qaGQqDLKXceM4v1eP1-RvZkdgOwQm2MizxZay7UyxfSM2uL4qkHIuWZGhNybnFZm3bqu25h8z3X4PLN83-KD1a9ZyAQFN-4ioPOdsc6BesBv6pyYBfNxJP-IDZvLLCbLgSqYARYofzG-LmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUBWdBopeR65RO2bTtubZsK-ilLQlrCWjpAiUl0tRusYwF26nO5dl5jKX0vdwFFdPx2sQlpqY7UlKbRbYtBU_z0YRPV7Bh2E-yQ--m6UPgLbelP0J6FQxc21VyQwXSZHPHWj6loQiPJiJZikg8rhTjsXblb22cS_OuWcWb5TUWlVQnZsZKyl7PNDRrI3GxkwgN8V6Cysl-Or7iyuM3CPrx7pz3W1tYsYgX9bivPvxUuxI0B_k25zFSdzuj1ie6c8Nl8fDhBW_SQVe1INZIEd6WHriuBAnKt8LA3SGv8mf4ohQreNDUntg5Vfs7blRzaWMyRJejEON_sw_KSPIloP3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/My3_1mjgh35XalmySOlzp32OCQGbqlbop1TX03Q321G31SXnLpDqOm9tP6B12dpT_PhW2nW_jXV3QfJYVRZc1x5fdnR9FYZaCrcgQXhnzSHlYyjUY4i-xOb42NgJNuMadVH5-fvKcnJbSNDsChdw7VKgJvYy_Qu4yNBZFMrcKdh3KdMi4Y6ukoELxEB3obgJlRV1zMRW5EvGpLgY7bNOL2nWOfua7mf19WKQNJdj4UiD2eMRJNOxcV-bk-8RtKM5OOK5CraYY__Qi_vdP21pPJZmqoHZF_NHBldtdb6NQR4SZfTpTEDIS9zuisEIF6-G5gnm5o5QiXMUadMlfgWfHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnEIy7cp4DgfCbaM0XwUazyUvlgsEGUgNOYDeulPmZ8_PvbZ4FXvW1N3cGKZEd3lDb2VEKD0s-0YU7ZjizPlcU1rmLqTFnQVKuDqKjniL9kRqG0-uOhBnNxZQiXK0K3XCXSiNoDBej6Fssd3nQrFrFiux7oDdTu44_2ZnwwahupKvijbxoQDHSBwAn5T526NdE6xQm5AIUyQyHm7yN_GvmOZmgxftNRBBg2J0-WVaIsxLYHa-fWPZRWy3DnseNJrdQmQ8HaCLOvW1_TK4ywFo0qsgvxqAh-iIm2MDYH_z-ExzQe9fuz9wgAskK2p7TQfEHKv9d9yIJLwXM5zcB2SZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWNt0bixSUdE049JjSBgkpgdYdI35vWy_5UfwAUbbITjNdbE2d_T6Gtff2O8bwA6pcjKxGbUXZtFq5kY2x5uMvrF8odG6zBP4l1lrpEqxCJiFo891YhJE8BZtsAm2c0DafuhtBQVV2Nridl8fKNiSe66EC6IofsRPJVruF03cVBTvzR6kKBAA9GgDEPX422v3DXgtPCz_52_Cfx-yJyT6-xcAu1awHUxXxQ0AZx9sJ1jcfO-bhdS52wSjfUzN2RpvwpQwLbhrGhKvVJ8sl83hFuEp8CfXxvM-WmLQu82ZGMEgZnwhdtv4MJsZqodHa7gFlupD1z8tfjg052n02pNRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=YmdBgAPqD6LNL-W7dRh-dJdeOzCAb7UVEYf316pJdqio8AsB6tK8fKK0vaIabAomriA_-S_jNIseX3HxBVjoN8f7Ip6XbMHW7en2Jje4R5Gv3201TLnGXXLonxOb_o0QdtDPh6Ub1ezGsFxlrPiDsmxPCM8DPNs1iRXTl6iomCM3N5dwLezyUUaQNVQ49iXk3kL478MP_CUSQr94wK5T7aX48SzqcZ_3XdZUVlHzaug0TRNs5yiy3suN8rwi-26E1U9OE2qNqSiq8QkKWed3e5rzwmQkW1C72cofsMxBu4vHZLrPjKblhcoK-IGT99HlIz1rgfbkgbuDwvOBKrxZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=YmdBgAPqD6LNL-W7dRh-dJdeOzCAb7UVEYf316pJdqio8AsB6tK8fKK0vaIabAomriA_-S_jNIseX3HxBVjoN8f7Ip6XbMHW7en2Jje4R5Gv3201TLnGXXLonxOb_o0QdtDPh6Ub1ezGsFxlrPiDsmxPCM8DPNs1iRXTl6iomCM3N5dwLezyUUaQNVQ49iXk3kL478MP_CUSQr94wK5T7aX48SzqcZ_3XdZUVlHzaug0TRNs5yiy3suN8rwi-26E1U9OE2qNqSiq8QkKWed3e5rzwmQkW1C72cofsMxBu4vHZLrPjKblhcoK-IGT99HlIz1rgfbkgbuDwvOBKrxZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=ueVWbMOwnviFbGlJHNjiZwHQCsNcSO2K_1KkPOPATESpBlRR5xql_wK1_ibK2YjQud7PHcz29z-wR7zUqGAqTIwvhecSdPLcFygFCcBH7nMKPMS9tLQ6u5YlWV4bJ0O_qH4l53EbLcGYd9tHGZRIY320n83sznB3lRu91dUpnhtLjfY1RNd8Mj8HneP-9rRwpftioseN-8vmNBlbyu5bmx1bQivPG4f6kqBrEIyhUaA2MCKR16edaMMY1Upl5PdHwpK7L3SuMzXNE-YqUDTbDPe3oDG0mdLH4FE5hgvX05iGACR8U4JQyvIId9jbUuEk1fc4r4ff1p-1_k9ET01s7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=ueVWbMOwnviFbGlJHNjiZwHQCsNcSO2K_1KkPOPATESpBlRR5xql_wK1_ibK2YjQud7PHcz29z-wR7zUqGAqTIwvhecSdPLcFygFCcBH7nMKPMS9tLQ6u5YlWV4bJ0O_qH4l53EbLcGYd9tHGZRIY320n83sznB3lRu91dUpnhtLjfY1RNd8Mj8HneP-9rRwpftioseN-8vmNBlbyu5bmx1bQivPG4f6kqBrEIyhUaA2MCKR16edaMMY1Upl5PdHwpK7L3SuMzXNE-YqUDTbDPe3oDG0mdLH4FE5hgvX05iGACR8U4JQyvIId9jbUuEk1fc4r4ff1p-1_k9ET01s7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=VgV7X5jcoIJ_spgDC4JbQF-U5RmwJ0ULl4B16suT6Z6CmUlGxrBV2o5g2-s7jtpshcXjhEUXLuE5it3vpNy3YAbqAvFCNptMtp1SwEGTbqoged6hXkcscUtK_ZqXL9lCaVziS3lbfQDJqUpaxJoJdobiX5vPIPPNMCaOTuF9vhoxa48TiWEYkBZMX9Q0VugIgIzWrQz3yFYMEcHudoHmDC47SGRDL94GYQY1cXIOEJvEnXlrPbK64FK40E-RodTHTTnmCHxV2lyjg_VixJDuWRwauuYBFh-U_7e9lrb-8JClAa7WdURsENapgn0j8jDVn6_iifGcjYUqcEvyykq-XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=VgV7X5jcoIJ_spgDC4JbQF-U5RmwJ0ULl4B16suT6Z6CmUlGxrBV2o5g2-s7jtpshcXjhEUXLuE5it3vpNy3YAbqAvFCNptMtp1SwEGTbqoged6hXkcscUtK_ZqXL9lCaVziS3lbfQDJqUpaxJoJdobiX5vPIPPNMCaOTuF9vhoxa48TiWEYkBZMX9Q0VugIgIzWrQz3yFYMEcHudoHmDC47SGRDL94GYQY1cXIOEJvEnXlrPbK64FK40E-RodTHTTnmCHxV2lyjg_VixJDuWRwauuYBFh-U_7e9lrb-8JClAa7WdURsENapgn0j8jDVn6_iifGcjYUqcEvyykq-XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=aBrdrmXHLjrt0GCRWTgfa-chlFPKJcwzg_5XF7dgx0hJeSuXMV-1c-Me20KXNuo5tc1rixaZgLe0I7qvFxC8jUArdLWFeljEOhtNqXfX5ffbsNUm_yyYX6aoTJO0g5rWNo6B2ZmGjgWtt1PSPq-RWdFzCFXI1WAKLII4EtswnRnPybX8dgnYoiV2Ucy4m3mYL0nUeQeQJwXmsev7TCIQTB-ie4ieFxEQpWzWGTPhC_-cco5gdgWqseb7t_3Z7xQ8uA18TdVHdX55TTgO2zhWT3A3XGNUSYEarHFgz8BlyyMcgcszF0ik-ztpN7VsWaSK6C-41SPsppOlEy-08-xjbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=aBrdrmXHLjrt0GCRWTgfa-chlFPKJcwzg_5XF7dgx0hJeSuXMV-1c-Me20KXNuo5tc1rixaZgLe0I7qvFxC8jUArdLWFeljEOhtNqXfX5ffbsNUm_yyYX6aoTJO0g5rWNo6B2ZmGjgWtt1PSPq-RWdFzCFXI1WAKLII4EtswnRnPybX8dgnYoiV2Ucy4m3mYL0nUeQeQJwXmsev7TCIQTB-ie4ieFxEQpWzWGTPhC_-cco5gdgWqseb7t_3Z7xQ8uA18TdVHdX55TTgO2zhWT3A3XGNUSYEarHFgz8BlyyMcgcszF0ik-ztpN7VsWaSK6C-41SPsppOlEy-08-xjbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
