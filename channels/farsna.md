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
<img src="https://cdn4.telesco.pe/file/rWul12Ata86GN2XQjK4lBCQbd9nFe9YMS0ZqGAuIO0tsY_0XowaZm-cvBOXgVqLhDCoZpiTfrh7Nmo4oUwK2YD1V0rqGEmKttVltQhZykw7xBll-JnJAHaomy1aVSalWESM6yXnSWBSjpJNFysKW2vpIp9RBMfDCg1DeTqEkhyO_vS1ILeE3N2FQgQAqpU1cojUCeJcMJo1Rw-e5xbp02MRR7nss4Sh-i1nq6pVZqxykbLuGzuv80skPV8oUWJukD2q__xQrNK7aVYT4YvrWWjgkD56b5fRS_D1sh_hCUodBiTQlGqFiGWHl6Yq5c9y7z7lGrsMKLbXl4QNOGE0dkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 23:48:14</div>
<hr>

<div class="tg-post" id="msg-455059">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be5020de3.mp4?token=O2Oa9pAgd6yNcIc_WDE0TJhwEzn7a21YDAdNWu69-vW268xOz81A2UZOWkBgILGA2ojfqCwTBTVU_hQa9Vj8oNe91wEvruUboWEyd3wHDwzrqcRQygBS_TOK-GRyveurVq70E5kr1qRgyErcvXcZuv2KKHpSTG-oB4zevRDZFO_iEvl8WAW-j19BIjAlaXwrSsO9wfCXS14IsNAtxfc0D7RNFbut3E4MLwPaRzSe2meUJ_Rm4IExUMSWXAatMJC83j1rLNvMAvvnuFQiZh9IqPcthYZaLbIBkbvdN29MKRasFhJFVj0Elcr7NQZkmOCf2hH-84bS7STT8sAjJMtTHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be5020de3.mp4?token=O2Oa9pAgd6yNcIc_WDE0TJhwEzn7a21YDAdNWu69-vW268xOz81A2UZOWkBgILGA2ojfqCwTBTVU_hQa9Vj8oNe91wEvruUboWEyd3wHDwzrqcRQygBS_TOK-GRyveurVq70E5kr1qRgyErcvXcZuv2KKHpSTG-oB4zevRDZFO_iEvl8WAW-j19BIjAlaXwrSsO9wfCXS14IsNAtxfc0D7RNFbut3E4MLwPaRzSe2meUJ_Rm4IExUMSWXAatMJC83j1rLNvMAvvnuFQiZh9IqPcthYZaLbIBkbvdN29MKRasFhJFVj0Elcr7NQZkmOCf2hH-84bS7STT8sAjJMtTHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی قمی‌ها به شب ۱۶۱ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/farsna/455059" target="_blank">📅 23:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455058">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d26f3f87d.mp4?token=ncNAwrsT77a_Dl0ICQPeSJzHJzTxeRKUips9LLT-kGyhEUTUPwNQk7QRhz2_SxWCScRCTCxmTeY2aNxQMMqQSEa3SRnOUEOcd6otXd2G1FYCFBkY0Bl-UQPnR37da0VgHDcGYk2A0TUMTb6Ydm1RFR3OdYfd2IM43L6YjtadyalUTT5X6TUbSAfI3j75sp0aZowbqJ8ne-7gCb612qxUHq0XVUmLvPyLeQEvI1X8VGEQPxeRbwd9IRWB48MxyjwjrJMCTOmrbOuknslHPyGN7mGbMbav1AAJJD73pK4mbJlakAS2iwS8lZK_dDjHEBKdhuzayVZ2ARDM_Xj_MCrN2B25enbPkdAmah5F9hMtXhZuhzPsmB0FpSweJTMX56BldvYAmzZG0V15yDoPFAbFL5Jbw7Dwu96nc9489qhX1lpmli6enqBcWF3bPFDTaT3Od25SkAFHirWacSU5yUowf8PZbNWLgZjgF_gkdqa2ifNQv1nKEsOgilB2jdt1MiJBGRJPfUHCLy4Sf955G6uQ7lvGCzXIQqcsD567E1mE16Vcb8W0tkTb-JORf9M4TRBf6FclBdDtL3uUxYTa6HnRgVV4d1JVa4gBgiwYBMz4BJdjXwD5L0Dp49Y64DlLVCw6L56JKCHKyBLErmg31DH4_o68QFbCwZYL-2GGG9crtHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d26f3f87d.mp4?token=ncNAwrsT77a_Dl0ICQPeSJzHJzTxeRKUips9LLT-kGyhEUTUPwNQk7QRhz2_SxWCScRCTCxmTeY2aNxQMMqQSEa3SRnOUEOcd6otXd2G1FYCFBkY0Bl-UQPnR37da0VgHDcGYk2A0TUMTb6Ydm1RFR3OdYfd2IM43L6YjtadyalUTT5X6TUbSAfI3j75sp0aZowbqJ8ne-7gCb612qxUHq0XVUmLvPyLeQEvI1X8VGEQPxeRbwd9IRWB48MxyjwjrJMCTOmrbOuknslHPyGN7mGbMbav1AAJJD73pK4mbJlakAS2iwS8lZK_dDjHEBKdhuzayVZ2ARDM_Xj_MCrN2B25enbPkdAmah5F9hMtXhZuhzPsmB0FpSweJTMX56BldvYAmzZG0V15yDoPFAbFL5Jbw7Dwu96nc9489qhX1lpmli6enqBcWF3bPFDTaT3Od25SkAFHirWacSU5yUowf8PZbNWLgZjgF_gkdqa2ifNQv1nKEsOgilB2jdt1MiJBGRJPfUHCLy4Sf955G6uQ7lvGCzXIQqcsD567E1mE16Vcb8W0tkTb-JORf9M4TRBf6FclBdDtL3uUxYTa6HnRgVV4d1JVa4gBgiwYBMz4BJdjXwD5L0Dp49Y64DlLVCw6L56JKCHKyBLErmg31DH4_o68QFbCwZYL-2GGG9crtHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاشمری‌ها امشب هم برای ایران در میدان ماندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/455058" target="_blank">📅 23:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455057">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b866be118.mp4?token=PDyjHQIE81-w4TVSES1d6790_-vPVhZN4tsuNS3p__esUsZP3MZ6N-yRuuW44ZYsoJ1mH9C9o7DFdHViDICBmPV_wlnLSLvSDi2SP-5hbX7mB4-K9JfPaMFEnxKCdFMj5Muet27gj7znfM841G1Sufe6TTvKKmFwpnzDC4bkHavQq4y5UjJoyAvqsbe7XwXo3_fTuPcxE0vffeI1v8mAuLP6fCWM9fE40omqMn3xAeQmTYF1vnS-do1ENUUzFDF3Fg3q-VscOYlCuR1Ltu0ex4ie0mECotS9krzLD5ai4IFJP2G7WgRS95hh4_THQtFPCp5C3l_Zx16SfJluBCYDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b866be118.mp4?token=PDyjHQIE81-w4TVSES1d6790_-vPVhZN4tsuNS3p__esUsZP3MZ6N-yRuuW44ZYsoJ1mH9C9o7DFdHViDICBmPV_wlnLSLvSDi2SP-5hbX7mB4-K9JfPaMFEnxKCdFMj5Muet27gj7znfM841G1Sufe6TTvKKmFwpnzDC4bkHavQq4y5UjJoyAvqsbe7XwXo3_fTuPcxE0vffeI1v8mAuLP6fCWM9fE40omqMn3xAeQmTYF1vnS-do1ENUUzFDF3Fg3q-VscOYlCuR1Ltu0ex4ie0mECotS9krzLD5ai4IFJP2G7WgRS95hh4_THQtFPCp5C3l_Zx16SfJluBCYDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور نونهالان و نوجوانان در شب‌های اقتدار شاهرود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/farsna/455057" target="_blank">📅 23:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455056">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe93a4df4.mp4?token=fd7ghwSW27xAVTiO3SsAM-jeWxatcjcFH06mRWaoVITSRtPNYO6UdmyRorOQ48bJYJOTEyT53O8asyNTGa95RVBVy9_UgyNinzT3njWOw47LN20rocmF44g-8BMntPhM2bksI7HWKgWhRYFNcPpy2gkjqF0GlOJYu2b0M_ffnfu1deF85p54cORvXaRSo-n503PjE24hCMsjVsHeeV3K_xAtsPOIYf9D5WPug2-QjI3jn_xXuABIdYaldODjnHacohFTz6e7xKeoLTQ1EoZuTI7B3IP_4cCsSvwMt_LDNK1m5He5RzEvwU1zqwxpN8ZcTVKzqoVOClZmkXWNBTjESw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe93a4df4.mp4?token=fd7ghwSW27xAVTiO3SsAM-jeWxatcjcFH06mRWaoVITSRtPNYO6UdmyRorOQ48bJYJOTEyT53O8asyNTGa95RVBVy9_UgyNinzT3njWOw47LN20rocmF44g-8BMntPhM2bksI7HWKgWhRYFNcPpy2gkjqF0GlOJYu2b0M_ffnfu1deF85p54cORvXaRSo-n503PjE24hCMsjVsHeeV3K_xAtsPOIYf9D5WPug2-QjI3jn_xXuABIdYaldODjnHacohFTz6e7xKeoLTQ1EoZuTI7B3IP_4cCsSvwMt_LDNK1m5He5RzEvwU1zqwxpN8ZcTVKzqoVOClZmkXWNBTjESw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدای حماسه از زبان یک کودک بختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farsna/455056" target="_blank">📅 23:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455055">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003243081c.mp4?token=XfaWLUGtVE4ePbk4DYYwpxfzZIpvsEWZbCzL1B1vx-87M21tUalIULV5jbEYkJrx8bdlpxe1jcLFLwDsh5I1kkaw5x71hK2rrFHzgFB5HKxSLebyVaPmYqpIq2630sRlvke9aPtYGHp9dvZM2eBnEcmxEdQqvHCKv6TxH-thhJgQ38YZ9gfDQ34RDaBXxrNbHKEJy8dF_qQsQ6KqOQNZn6BPtEWTwYB3OniPuuU26Fx6GYQ76NKDEWVCspzjB7Zwz8SV-wCsTtMG-FOHEkgGcHeJGagswjgP_iLop29wkekC_bhrBB4SZ8o3NovbwmjtnB0zy55Epd34CCF0KlWUJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003243081c.mp4?token=XfaWLUGtVE4ePbk4DYYwpxfzZIpvsEWZbCzL1B1vx-87M21tUalIULV5jbEYkJrx8bdlpxe1jcLFLwDsh5I1kkaw5x71hK2rrFHzgFB5HKxSLebyVaPmYqpIq2630sRlvke9aPtYGHp9dvZM2eBnEcmxEdQqvHCKv6TxH-thhJgQ38YZ9gfDQ34RDaBXxrNbHKEJy8dF_qQsQ6KqOQNZn6BPtEWTwYB3OniPuuU26Fx6GYQ76NKDEWVCspzjB7Zwz8SV-wCsTtMG-FOHEkgGcHeJGagswjgP_iLop29wkekC_bhrBB4SZ8o3NovbwmjtnB0zy55Epd34CCF0KlWUJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا پای خاک، مادر و فرزند در میان است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/455055" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455054">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bcad59215.mp4?token=vvSYdMgscO4sucaQEBz_smPt9LNKMyIK6nUkYEF64QU0_51iLA1qxmGqbc52-w8UuuqwZ3KTYevQIIHkCpI7cbwzIdZQiaRwSi8qYCuuB6y2hztDWTp37KwWLsherJPEWg-bNQZ3ej1-RU5QMpxNBPBBwgIN65nasVweCvaaUHBMtKtxFIp046mMy_yV3mNTyV26aeynT-vxFEgBhKNhiehLKFfiS-hiz6CqH6CfJJBkJWOSMbmo40MnXDMq5bskQwjRSr2ifUNxHG7pGYCChEwyOYa6jsY31h7PfUfgDG9m0uVia_lMnTA9TMOKMvAjHCyzK84CD7MiyaGLYnhhuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bcad59215.mp4?token=vvSYdMgscO4sucaQEBz_smPt9LNKMyIK6nUkYEF64QU0_51iLA1qxmGqbc52-w8UuuqwZ3KTYevQIIHkCpI7cbwzIdZQiaRwSi8qYCuuB6y2hztDWTp37KwWLsherJPEWg-bNQZ3ej1-RU5QMpxNBPBBwgIN65nasVweCvaaUHBMtKtxFIp046mMy_yV3mNTyV26aeynT-vxFEgBhKNhiehLKFfiS-hiz6CqH6CfJJBkJWOSMbmo40MnXDMq5bskQwjRSr2ifUNxHG7pGYCChEwyOYa6jsY31h7PfUfgDG9m0uVia_lMnTA9TMOKMvAjHCyzK84CD7MiyaGLYnhhuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۶۱ «قرار عاشقی» گناباد؛ هم‌صدا در حمایت از نظام و رهبری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/455054" target="_blank">📅 23:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455053">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c9db54a9d.mp4?token=XmHb1T_7d8oOCWGUTJNPyw5Z6DhjmQkqqtnFlaC8Wd7tWRT9bnPGG-6tgF6m_q9l91hmeb33gzTf9PokQ-Lwy5XTFXCJalbpfRlBvkTIi-mSJDdjAwOxsiYUcW_SSSP607mU7ZCJA-vosttUly3xFidrueXocDCyxoncFLMWHMP19Blpc8OKzmTu9huv3HVJrQW-waCKV6_nzsmbarX2ZWNoN_qZ-M6FP9HK63loQkHafxj3nJ3zpYboh4IxAm5dduzah-QqijjeUNRISBS6aPVIkmGyptv49E1PNFpN04qbrUq2-Nt9d6tq_KhpoAniJ3mFE5s_Zk8yJB6ZfmTy0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c9db54a9d.mp4?token=XmHb1T_7d8oOCWGUTJNPyw5Z6DhjmQkqqtnFlaC8Wd7tWRT9bnPGG-6tgF6m_q9l91hmeb33gzTf9PokQ-Lwy5XTFXCJalbpfRlBvkTIi-mSJDdjAwOxsiYUcW_SSSP607mU7ZCJA-vosttUly3xFidrueXocDCyxoncFLMWHMP19Blpc8OKzmTu9huv3HVJrQW-waCKV6_nzsmbarX2ZWNoN_qZ-M6FP9HK63loQkHafxj3nJ3zpYboh4IxAm5dduzah-QqijjeUNRISBS6aPVIkmGyptv49E1PNFpN04qbrUq2-Nt9d6tq_KhpoAniJ3mFE5s_Zk8yJB6ZfmTy0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ما می‌جنگیم و سختی آن را هم می‌پذیریم؛ رهبر انقلاب هر تصمیمی بگیرند ما تا آخر پای آن هستیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/455053" target="_blank">📅 23:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455052">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96583e47b.mp4?token=hpA9qIsWSR6d7EnS52Qdc9O3VJgJYTTlBB7EjyU7M8TBfiMBScr3Tyf2WyJ5PLQcbBMX5UxeF2w_bPi8p79itXxtLgO2Hq0Fq7e7jFD5vZuUiz9D2ghjDTryhHYdBOjmI85Ibz-2iubHHDTMboscXaLoVwiMNZwG5p0ge7vilsx7_ULwwbdro4THGCgzXmSNt9s966_Z9N-ATIAn8MOYnxnNY2ZOhroVp88QCe9_bZKIYo1SN2ufRqNNefdvFaXaMdxBq-ty6kgTbQ8RQx0qjfMj58pAjvix4EDPdkjszn3ilkYS4pkp6TxKCY4H0FtzXds4_IO63UZfev8o_JqpvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96583e47b.mp4?token=hpA9qIsWSR6d7EnS52Qdc9O3VJgJYTTlBB7EjyU7M8TBfiMBScr3Tyf2WyJ5PLQcbBMX5UxeF2w_bPi8p79itXxtLgO2Hq0Fq7e7jFD5vZuUiz9D2ghjDTryhHYdBOjmI85Ibz-2iubHHDTMboscXaLoVwiMNZwG5p0ge7vilsx7_ULwwbdro4THGCgzXmSNt9s966_Z9N-ATIAn8MOYnxnNY2ZOhroVp88QCe9_bZKIYo1SN2ufRqNNefdvFaXaMdxBq-ty6kgTbQ8RQx0qjfMj58pAjvix4EDPdkjszn3ilkYS4pkp6TxKCY4H0FtzXds4_IO63UZfev8o_JqpvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: من از جنگیدن نمی‌ترسم
🔹
شهادت شیرین‌ترین آرزوی ماست و تا پای جان ایستاده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/455052" target="_blank">📅 22:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455051">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584735f78f.mp4?token=LumU7Fwbg5OAI-7N5_KgtMflofeSZ-pTPxOhh7ONTlQFJ_ly9dGogC30IajIhSUWROSKp4K2wGJb_RqhC0FbobbcwrrvojmmceubSjofHTfFU9_bgOFf3XQGVYNixbw3QR03IKbhFHvnq-6DNIVAyQE94hJyfQFus7MNML1sQxI0z5GIvEap_Tf4i4DUelEN5rXf9fo1PKBICmgSCleh_GCiWowolbEVHQLIGXXKmvsv_8ZpApYksyHvbe43MrhvQJk2egpIbI38oQdkDJY_6uMYwWtMi2WkW3AfmN2AVWmmWNt9umtlONoJlJdbAHP3vR2zyqxzUXwk0sVlIVWr4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584735f78f.mp4?token=LumU7Fwbg5OAI-7N5_KgtMflofeSZ-pTPxOhh7ONTlQFJ_ly9dGogC30IajIhSUWROSKp4K2wGJb_RqhC0FbobbcwrrvojmmceubSjofHTfFU9_bgOFf3XQGVYNixbw3QR03IKbhFHvnq-6DNIVAyQE94hJyfQFus7MNML1sQxI0z5GIvEap_Tf4i4DUelEN5rXf9fo1PKBICmgSCleh_GCiWowolbEVHQLIGXXKmvsv_8ZpApYksyHvbe43MrhvQJk2egpIbI38oQdkDJY_6uMYwWtMi2WkW3AfmN2AVWmmWNt9umtlONoJlJdbAHP3vR2zyqxzUXwk0sVlIVWr4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: من از جنگیدن نمی‌ترسم
🔹
شهادت شیرین‌ترین آرزوی ماست و تا پای جان ایستاده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/455051" target="_blank">📅 22:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455050">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حملات گستردۀ ارتش یمن به مواضع مزدوران سعودی
🔹
نیروهای مسلح یمن اردوگاه «العَلَلة» در الضالع هدف قرار گرفت. همچنین گزارش‌هایی از وقوع انفجار و حملات پهپادی در عدن، تعز و شبوه منتشر شده است.
🔹
هم‌زمان، اردوگاه‌های نیروهای وابسته به ریاض در مأرب نیز هدف حملات…</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/455050" target="_blank">📅 22:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455049">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e11600a04.mp4?token=Z3_gmiq-uCmENPAQrFuIvOoq5NZSMBEySjS_qJL1kV1ciEvMSusKXn0D9Xiofb6JM5yN9Wy9lFMfDzCal66dR-KqIoCeGp6Wo8b22n73DX_lPPmQQg1pFzqb-3gFpMVCFNRJE2-KMneuDhUY6otUT_Ny1Jz4wFfIN85v-dYj0aCN2qyf67MhqKMB39c5lMuBXJ6mPN3Cd2ZwztwXU6mRp1I0PysiHUMlcsXKSkb58ylhHOA01nqTEhcHsTL85DppZe1poavVrqYwaQfBcl9UJaCZVdTiqTUJt2b0JBQR9Ve2NQ-FS0-kTjG-PkAJPTJE9N69sALbGixNH8VWl6aocQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e11600a04.mp4?token=Z3_gmiq-uCmENPAQrFuIvOoq5NZSMBEySjS_qJL1kV1ciEvMSusKXn0D9Xiofb6JM5yN9Wy9lFMfDzCal66dR-KqIoCeGp6Wo8b22n73DX_lPPmQQg1pFzqb-3gFpMVCFNRJE2-KMneuDhUY6otUT_Ny1Jz4wFfIN85v-dYj0aCN2qyf67MhqKMB39c5lMuBXJ6mPN3Cd2ZwztwXU6mRp1I0PysiHUMlcsXKSkb58ylhHOA01nqTEhcHsTL85DppZe1poavVrqYwaQfBcl9UJaCZVdTiqTUJt2b0JBQR9Ve2NQ-FS0-kTjG-PkAJPTJE9N69sALbGixNH8VWl6aocQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: سال تحصیلی آینده حتماً حضوری است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/455049" target="_blank">📅 22:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455048">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335d4aa8a7.mp4?token=JcOdnwBLMpFoRWz9diRmPCicFZgB3thLtlWGZ50wpGo6nh204hid6GrgbDN7DdROpFBjSMcdLHvnk0b4E36yeKqyRt37nBCPRD_Ofd-pJG6vmWtGnVqbyU9ixEo3khADxTmpUziK_FENJB1szDrC49RTJGDh_FMouG349eqkyU4tnXYWLBDjQqgvREme_XvGf60jWkKqOPJY06Bq-LhvZX0NsAsu2KUDatigRn2vys3YgPtAU_79xieTcyPJ_-KsGxBlEb0mOnuttsyVS21H0hLZiqLWQXTFYubyATa0B08D5qAri_3dOE2JuWOgsgOMs3fL4JqCagqYntIqqaEIiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335d4aa8a7.mp4?token=JcOdnwBLMpFoRWz9diRmPCicFZgB3thLtlWGZ50wpGo6nh204hid6GrgbDN7DdROpFBjSMcdLHvnk0b4E36yeKqyRt37nBCPRD_Ofd-pJG6vmWtGnVqbyU9ixEo3khADxTmpUziK_FENJB1szDrC49RTJGDh_FMouG349eqkyU4tnXYWLBDjQqgvREme_XvGf60jWkKqOPJY06Bq-LhvZX0NsAsu2KUDatigRn2vys3YgPtAU_79xieTcyPJ_-KsGxBlEb0mOnuttsyVS21H0hLZiqLWQXTFYubyATa0B08D5qAri_3dOE2JuWOgsgOMs3fL4JqCagqYntIqqaEIiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تشکیل تیم کارآگاهانِ زبده برای دستگیری عاملانِ قتل حمیدرضا رجب‌زاده
🔹
سخنگوی پلیس: تیمِ تخصصی و ویژه کارآگاهانِ پلیس آگاهی تهران بزرگ، برای شناسایی و دستگیری عاملان قتل فردی به هویت حمیدرضا رجب‌زاده بلافاصله بعد از اعلام مفقودی تشکیل شده است.
🔹
از رسانه‌ها…</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/455048" target="_blank">📅 22:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455046">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40344d8430.mp4?token=dB-ZMmukqnVvfWzrjXAkWewQi9SzclEHgVj5u6wvJOehWiNKrDQgKn_TPz_Eit_SeH7N75TE-6PSPU3S9vaykobQ9fAa8xVUSZNa2zlAG14QiS0tiE0Q_CrmYD_zGl6XERkuC4zIEt5kcvAikUGsxtXBYXHCZFSth0Y4rwuj80Xd_UjER8Hq64zJZysFYiA1FFTBFylg9HU8vz2as5JRwYo8hJ-G4bChuecFxv0cmOjLPr1AwhopZAV8A0W-f882FnvCQrYHSvMt4L5Z07bP25mAFrkN-vRuWFgWlzgTzxYKUsQULSZPv8F4nm_PREup0WrTmHehqOoMVwDB7JjwVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40344d8430.mp4?token=dB-ZMmukqnVvfWzrjXAkWewQi9SzclEHgVj5u6wvJOehWiNKrDQgKn_TPz_Eit_SeH7N75TE-6PSPU3S9vaykobQ9fAa8xVUSZNa2zlAG14QiS0tiE0Q_CrmYD_zGl6XERkuC4zIEt5kcvAikUGsxtXBYXHCZFSth0Y4rwuj80Xd_UjER8Hq64zJZysFYiA1FFTBFylg9HU8vz2as5JRwYo8hJ-G4bChuecFxv0cmOjLPr1AwhopZAV8A0W-f882FnvCQrYHSvMt4L5Z07bP25mAFrkN-vRuWFgWlzgTzxYKUsQULSZPv8F4nm_PREup0WrTmHehqOoMVwDB7JjwVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازیکن جنجالی قلعه‌نویی در بلژیک دبل کرد
🔹
دنیس درگاهی، که دعوت و بازی‌نکردنش برای تیم ملی در جام جهانی ۲۰۲۶ با انتقادهای زیادی همراه شده بود، در بازی امشب استانداردلیژ بلژیک و بروخه در لیگ بلژیک، هر ۲ گل تیمش را به ثمر رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/455046" target="_blank">📅 22:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455044">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egzhNA5XKQy34nWzLjJdSna90SWRb1lE5_3HvrwElA6_sPR1Wbgt10EUjSitPKLe8i44JGtK1jxKBDeqQoY9PqzI-AMtVuUKwtVxSoYVJuNb3swaCX5qzlxJOIRQA9aEc0W2gKyo_HrMkxD--XrgdL3UGnOeyPLFar0I9zmyqcC5qjiRy3k8H9SCDXchr2QzIZCXnNCgdr3r0zLLQkGCzeNLbKY1vWH0ZZUNOJZIbqXis_2EwTmCC5V-S6yf_MGPcL5t7nlZrYM3rXaLRSmqnPmldWtxSBkU0h15qoraZp9qKHJ2ecYgcgHvTojAd5Q1EnBUMtcw2lFLJZ803E00QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWD3gXBRVdgDvG4pmNur-mQ4PElSfW7Y7NF9yQx2uyd91Z7iifv3W-GgaHQQa3pB_51Wlu3TDPiC8U3pdYvG6m5TodrF043hCpcgjotK5TQtv0vZ6CV1fRmGCz2Vhhwujp1PciwspUhCkPOl19ZhOwPP4srDhXrdsN5aRgyan9l7JudBqSn2tD--ku75FJyX3M8icZ9ADYVU7b1l8qXsHqwzNglINdgcBERemE_M1C1_HqQftMKuczqCInFRKscRg40emtP1r6Nta-UiL1dOsnjgz9lgwNA5c3cN2uUL__LEUpijZF-DHMVcATF89h5_0_5gJtu6KscuXqaDJMYb_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت عکاسی که قاب داغ میناب را به جهانی کرد
🔹
مرتضی آخوندی، عکاس هرمزگانی که عکس هوایی معروف و دردناک از مزار کودکان شهید مدرسۀ میناب را گرفته بود از نحوۀ ثبت این قاب غم‌انگیز که برندۀ جایزۀ «گلدن شات  ۲۰۲۶» گفته.
🔹
او می‌گوید: در مراسم تشییع تعداد زیادی از عکاسان و فیلمبرداران حضور داشتند و من تصمیم گرفتم با استفاده از هلی‌شات، تصویری هوایی ثبت کنم.
🔹
هوا بسیار گرم بود و نور زیادی وجود داشت. از زیر یک درخت ایستاده بودم و تلاش می‌کردم تمام قبرها در قاب قرار بگیرند تا مظلومیت این بچه‌ها دیده شود.
🔹
به نظر من این موفقیت کمک خود بچه‌ها بود؛ آنها باعث شدند دیده شوند و فراموش نشوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/455044" target="_blank">📅 22:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455043">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8bd81f6b.mp4?token=pDOaJ-GNQ4aPJu3W_0EPIvxnWaID57aVe3Mv-Me7DnA64qS7UWFEzsY7r8kVQDgDOrIma0aWZbQY0kRIuaNoDd8bm56s7iZtd5ITfp8IU9tbzzISwd6EQhtm8biEg_BbPF6Z1DE5HknknQJLpZb-ZVQ0knRIke_Hg51uO2P8Otn0tNBHbJojZhhZFpToDpOVZ0xQ-Hu_1ApeqBxblMq4uqNMMc-7W63Z_VpTzRSHmBRZ9fs_Jx0jcpGU77OerRP4PbTw0RctWoAwWlDVtE4XXSL0cHR1xcB7H6KSbRG54E--Tv9MIMESOk9NCHgaW87iXjcTMbzUgBu1cHhpgh6RpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8bd81f6b.mp4?token=pDOaJ-GNQ4aPJu3W_0EPIvxnWaID57aVe3Mv-Me7DnA64qS7UWFEzsY7r8kVQDgDOrIma0aWZbQY0kRIuaNoDd8bm56s7iZtd5ITfp8IU9tbzzISwd6EQhtm8biEg_BbPF6Z1DE5HknknQJLpZb-ZVQ0knRIke_Hg51uO2P8Otn0tNBHbJojZhhZFpToDpOVZ0xQ-Hu_1ApeqBxblMq4uqNMMc-7W63Z_VpTzRSHmBRZ9fs_Jx0jcpGU77OerRP4PbTw0RctWoAwWlDVtE4XXSL0cHR1xcB7H6KSbRG54E--Tv9MIMESOk9NCHgaW87iXjcTMbzUgBu1cHhpgh6RpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسلی که باید بیشتر شود؛ بچه‌های دل‌وجگر‌دار
@Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/455043" target="_blank">📅 22:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455042">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32de040c2.mp4?token=nC-DxW5gKvsJiZmL-d3sCQ9KLi4o0SNTS8HyISxfO11EUQmzWNSCSIksPE43pQtNUdWvjYD0As2tePVY4ygjWe-_R_JAY56MqQWLW7Twb093mO5wNBowJze8GdquV0LoKQrWR_leV01y-N0Ydgr7-LJ3RRx3ulII9avupsvT1gHqZMa8R5DWxdaUak3UmYygc9FY4PQsly9NsIMw-a8njvZv5IjPaaYrwMQ-LE97tEcyXIBPTEr-R5UdsyKD8YkzFcobyASSE9REIWAu4Dw5F6atHjTh01cY5ytZ1lwofNUyo50erXVSSBdYUxBO6c8SPY4w9sAWX9uSCvwW8xbEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32de040c2.mp4?token=nC-DxW5gKvsJiZmL-d3sCQ9KLi4o0SNTS8HyISxfO11EUQmzWNSCSIksPE43pQtNUdWvjYD0As2tePVY4ygjWe-_R_JAY56MqQWLW7Twb093mO5wNBowJze8GdquV0LoKQrWR_leV01y-N0Ydgr7-LJ3RRx3ulII9avupsvT1gHqZMa8R5DWxdaUak3UmYygc9FY4PQsly9NsIMw-a8njvZv5IjPaaYrwMQ-LE97tEcyXIBPTEr-R5UdsyKD8YkzFcobyASSE9REIWAu4Dw5F6atHjTh01cY5ytZ1lwofNUyo50erXVSSBdYUxBO6c8SPY4w9sAWX9uSCvwW8xbEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی خبرنگارهای نوجوان، سوژۀ خبر خودشان شدند!
🔹
فارس این‌بار میزبان یک دورهمی صمیمی با خبرنگارهای نوجوان بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/455042" target="_blank">📅 21:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455041">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OboY-SRz8hWadNq8qjokiBix3qOSikrFjCmLZqG5hXXu8stkGj3SC5hore6HoavtxWic1reeGFEO3x0l93cDVuw1l5KYZhSr1mVg55KbUyNO8iNWdVKaQqi64qyJWw3dClmHJqBS0QNfkjRjr5RbxVEUZo6L96kR-dqCOJ6Uzd4uL_NVUCWhEKKLJWVgThDc6NQryVFLHGNbRjwc3bjLlffGOxEGrnGbKKk8MOIYyPQyOYXQwWuB2zHcPQdZwl0znkCISpO_v7vLLYnaxTXrqw2-gIodppn7SVbclrLT73yW4ldJHpi-4gsGqIdn03jYa_CbeHCJUbzp17AymZIWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفر فرمانده سنتکام به اراضی اشغالی
🔹
الجزیره گزارش داد برد کوپر،فرماندۀ ستاد مرکزی ارتش آمریکا در خاورمیانه وارد اراضی اشغالی شد.
🔹
وی قرار است با مقامات ارشد رژیم صهیونیستی ازجمله رئیس ستاد ارتش ارتش اسرائیل دیدار کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/455041" target="_blank">📅 21:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455039">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e64ea390.mp4?token=kbYGCHSRAWMZVaPhS9gfYUpLT5xtoODH1SJCUuO_JZugar-ZlA67jWwLMHlP3sZlqg-7bv4d6mvJOH5cpEIy-KwOVXngdAjDr-XGatG5nKau0bPku6ZeH52Na_NSMlEw0j26tTjjmn0Krkt7eeV7VNjvf5YaKGflQvNzuBpkmGCd2scshNe4PP40AWd6QSZ5elDFXQgNpl8b47NQuPlOV_miXsKpdJzeIGVYd3H41wO3hUcBKfVSPxMC4TaioOX0XvrDPTbjsIjudIhsZdnqcLFNgVYWEiZQmm01edOvltb3aQV-Wc7FHqG06nXQuF3akR-36EIdU_rSt0bbJxOjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e64ea390.mp4?token=kbYGCHSRAWMZVaPhS9gfYUpLT5xtoODH1SJCUuO_JZugar-ZlA67jWwLMHlP3sZlqg-7bv4d6mvJOH5cpEIy-KwOVXngdAjDr-XGatG5nKau0bPku6ZeH52Na_NSMlEw0j26tTjjmn0Krkt7eeV7VNjvf5YaKGflQvNzuBpkmGCd2scshNe4PP40AWd6QSZ5elDFXQgNpl8b47NQuPlOV_miXsKpdJzeIGVYd3H41wO3hUcBKfVSPxMC4TaioOX0XvrDPTbjsIjudIhsZdnqcLFNgVYWEiZQmm01edOvltb3aQV-Wc7FHqG06nXQuF3akR-36EIdU_rSt0bbJxOjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: ۷ نفر از مدیران شرکت کلاهبرداری یونیک فاینانس شناسایی و تحت تعقیب پلیس اینترپل قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/455039" target="_blank">📅 21:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455038">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShKP8yh7hT4Y9GzxvSsSYUO8FCN6QY-1StSnA8AJ_O5pqKxkMsGGiwzd0bsaCtcIGyJjwqN63bWuRfnwgD457YaIHi5ENok_vg3w9jc00uE0vqaotDpeZ9QMmjnlIQnvE_OwJYlvyGGVJed8-dJMsrFc38a4MYj5VkCbHk4Y5-7UL8Swld2dbuvk4Ujl_8ybz5SP8T92U5Z_wKjcmF_sHam3326iEnHhbHeiE5o_uLcN-rvn42i4KsYSIt7e8WpW8R7xpYM0Mqu_Jiwfcmlthn6teSxjmxmHnQA9xbSUKOu1JWCvUOVfKaav1RcsmIN1eKY1ZQlr-5MI23aUOBsxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طعنۀ همتی به وزیر خزانه‌داری آمریکا: پول‌هایمان دست خودمان است
🔹
همتی، رئیس بانک مرکزی امروز گفت: آمریکایی‌ها مدام اعلام می‌کنند «فلان تراستی یا صرافی رمزارز را بستیم» اما این ادعاها خوراک تبلیغاتی آمریکایی‌هاست؛ این‌ها هیچ ارتباطی با ما ندارند.
🔹
پول‌هایی که جابه‌جا کرده‌ایم دست خودمان است و درحال استفاده از آن‌ها هستیم.
🔸
۲ ماه پیش وزارت خزانه‌داری آمریکا ۴ صرافی رمزارزی ایرانی را تحریم کرد و مدعی شد با ارتباط با بانک مرکزی به دور زدن تحریم‌ها کمک کرده‌اند.
🔸
وزارت خزانه‌داری آمریکا امروز نیز یک صرافی رمزارزی ایران را تحریم کرد.
🔹
بااین‌حال رئیس بانک مرکزی می‌گوید که امسال حتی بیشتر از دورۀ مشابه سال قبل ارز تامین کرده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455038" target="_blank">📅 21:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455037">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1791af6861.mp4?token=SQrPVuc1Ld8qIC5Ak0w5DebDzm5br9kQqRck8rO483t9D2rjls_jf4oir-bGgaurxUSkCDFBgel1XPg1WKnjl-fD4aBcwKyFLp8XAHByCUt72EKsb62oWipPx6Ix6zLZQrhe4KY7Ffav8UP1qfoxPOXj07dm11XWnl71Ala1posUzh4bHmyCZLUT6s62Sw9jhNXDU1XtXkoR8nD-Xr7TmqLu5WhfWenXiQ6eHTsZrNC5kzPutP2D9uNjFN2lm_i_VYGc83ZqubNHdGJkKFf9KZHlYGIVQXgglDGiitS9My1gjcRfhIKEeTDce7YETp-AYJ4SuwrgGIXvMJ9rGV4KiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1791af6861.mp4?token=SQrPVuc1Ld8qIC5Ak0w5DebDzm5br9kQqRck8rO483t9D2rjls_jf4oir-bGgaurxUSkCDFBgel1XPg1WKnjl-fD4aBcwKyFLp8XAHByCUt72EKsb62oWipPx6Ix6zLZQrhe4KY7Ffav8UP1qfoxPOXj07dm11XWnl71Ala1posUzh4bHmyCZLUT6s62Sw9jhNXDU1XtXkoR8nD-Xr7TmqLu5WhfWenXiQ6eHTsZrNC5kzPutP2D9uNjFN2lm_i_VYGc83ZqubNHdGJkKFf9KZHlYGIVQXgglDGiitS9My1gjcRfhIKEeTDce7YETp-AYJ4SuwrgGIXvMJ9rGV4KiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر خبرنگار میدان بودید، روایتتان از کدام جلوهٔ ویژه ماندگار می‌شد؟
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/455037" target="_blank">📅 21:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455036">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044924ce02.mp4?token=mR625RG-0eFIHraLV34oTQr4xH-yq6Ir04qkhKL0Vo7r6ZBH8j_K5qr6GYRjY-LO4eFamY1TCPh3RUusfB7Wpo3VVzzh27sTk2e8NBQFXQ0oseiTdYxm8f_rpyCmfmluMkAaKWJ-f4UoWOPLcuLbRL0S2xsTP22CLU-NV-8AWtNktUiYbVqolcmmhSozcXNY7sBSLjtVkrGlfxHdjR4itN5T-kGQdw5CWB8r7F1ZxafgmAyInmX69Ha_LPFYxxkmak9Sr4HD1B8wvMUAhjMpmYrBMFTndecGUzIa8L0INlN5yOTbLxwm6zzSBHsalf2Art0scdkgfI3kJ67iaGcyNaTD7GdMKb5YUy9YEUBSBfUfvP4r4t5DRUQc38gA1LIKQwEfzprI18BUKn3O0R4ECGgWis892wKRuQAdYV-7Kesn2Erdbe8ccJlEF0iUlPzuvqsLSz4Fvzvjs7t_YzNtg-3UhKwJB3hA9Ao8cgg1kRp3lAkbEr39bujPDMa6Yja-vpgiLvgW6OFkCVqjdKOaCa3CN-jXUm6aX-JKLnAiUgAIUdmYexVpfagtjMugNMJpSWI5lnIBS4vBtnjZVLtW6_W47LpO0IsdyXbDbBgIQQvtzvLSeXeD4B7D-_S_c-A_lTypIuiOiDpba3tHn_GgnBxICqpXmUKYiuVEdD9XE18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044924ce02.mp4?token=mR625RG-0eFIHraLV34oTQr4xH-yq6Ir04qkhKL0Vo7r6ZBH8j_K5qr6GYRjY-LO4eFamY1TCPh3RUusfB7Wpo3VVzzh27sTk2e8NBQFXQ0oseiTdYxm8f_rpyCmfmluMkAaKWJ-f4UoWOPLcuLbRL0S2xsTP22CLU-NV-8AWtNktUiYbVqolcmmhSozcXNY7sBSLjtVkrGlfxHdjR4itN5T-kGQdw5CWB8r7F1ZxafgmAyInmX69Ha_LPFYxxkmak9Sr4HD1B8wvMUAhjMpmYrBMFTndecGUzIa8L0INlN5yOTbLxwm6zzSBHsalf2Art0scdkgfI3kJ67iaGcyNaTD7GdMKb5YUy9YEUBSBfUfvP4r4t5DRUQc38gA1LIKQwEfzprI18BUKn3O0R4ECGgWis892wKRuQAdYV-7Kesn2Erdbe8ccJlEF0iUlPzuvqsLSz4Fvzvjs7t_YzNtg-3UhKwJB3hA9Ao8cgg1kRp3lAkbEr39bujPDMa6Yja-vpgiLvgW6OFkCVqjdKOaCa3CN-jXUm6aX-JKLnAiUgAIUdmYexVpfagtjMugNMJpSWI5lnIBS4vBtnjZVLtW6_W47LpO0IsdyXbDbBgIQQvtzvLSeXeD4B7D-_S_c-A_lTypIuiOiDpba3tHn_GgnBxICqpXmUKYiuVEdD9XE18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک قاب متفاوت در نشست خبری رئیس‌جمهور با اصحاب رسانه
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/455036" target="_blank">📅 21:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455035">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزارت اطلاعات: خبرنگاران نقش زیادی در ناکامی دشمن در جنگ داشتند
🔹
روابط‌عمومی وزارت اطلاعات به‌مناسبت روز خبرنگار: خبرنگاران، سفیران و مرزبانان آگاهی , پیش‌قراولان خط‌مقدم  جبهۀ رسانه‌ای به‌شمار می‌روند.
🔹
خبرنگاران متعهد رزمندگانی هستند که به تعبیر امام حکیم شهید، اثر اقدامات‌شان اگر بیشتر از بمب و موشک نباشد، کمتر نیست.
🔹
جنگ تحمیلی اخیر نیز رزمندگان حوزه رسانه‌ای کشور، در کنار سایر رزمندگان نقش بارزی در حفظ و افزایش تاب‌آوری آحاد جامعه، انسجام آن و ناکامی دشمن و سربازان رسانه ای آن‌ها داشتند.
🔹
صدای صادقانۀ شما در امیدآفرینی، روشنگری، حفظ و ثبات امنیت روانی مردم و جلوگیری از جابه‌جایی جایگاه ظالم و مظلوم توسط دشمن سفاک جنایتکار، بلند و رسا باد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/455035" target="_blank">📅 20:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455032">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d13RmMlvHe5huolkd7GZEBqgNLVe-iUsOsp7G6limExoxRIuNu0zmIfuS9qRwu_k7l6XTpYDqhfToYaPnr9YmvHXxKF1RQmivLWMGlGFcDh37eXLtjT4YK3fUK4ee120868WBzvt0vewm7tHGcNCB0aIN10LqB00V-lYJMUVJLDMdt2K-vQGTLc21drUXEyEW3rEAYE14AgjZBBnYHzzn3LY1OWAsupGAG6xaJOidph-DMsjODu-cp0lbSK-P9sx2VTjseNNExp1D488fEVGa7rTZDNfzVeW-SP923pzRL4i1HwMOhV-OGYodq9e_n80wMlfXWilJNf8c2d4MXEhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXH01aoAtHSXc7_4m0I9wbEgS1Io9ZWy8B-RaNWW-53Rcye2kaFUs0tCRvTzoZTgGbLDMyq3j8OVoKCsPtqaZr5kKGF8SET7OshBLk7XNjbgBbu3NPPceZ0atR1Jq9JS5Cngu94uceGFn27OZ9ranAnpeaf32mh2VaMam4NJefYcjt2izR354MeiU8dr5plHUDjkvCrnHg-yZAXsW20s8hGMTAeF0Ydh1NRd5gUOsiAOmtw1I2Y_TnSFbnYQutH5ZWC-M8tZTqO6Hkl1loyPENeBRa9mB_qidPrivM4xWI-2oxBoTzOtjWtI26BDu0FUOuolksF3fX3EI5jx3TTGCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a871cc9019.mp4?token=GVLjuwW88h8m1KXarPiHjSa420cpjHPrGf1obFOwCw1fFOAn54xa7Xtm5W5_HAhjdZEA8Gl0EIAFwzegZijn81k5-W2gwL8Z-LKH3i6l-XXHKlM1LnpMPYh1eAsgJFlBh69t2BtR697of3Z1t9DVPhMIeL0D_TFvw1rqBvFjbEtUVc0TIax1gA0D1KbVgsCWQKRd4qRmCbYo_i4NMlzCRKuBCfCHvI5z7hRy-ZmDlw8n6ebPF6WoXjTh834dw_YWegNzJOummN99qD3oEBn2A8ID9dt_bA0nb60KqzUPySZ-oENz_uKjLNaFw3RnRDBAvauLjYIOyBzEnkqIrzfv8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a871cc9019.mp4?token=GVLjuwW88h8m1KXarPiHjSa420cpjHPrGf1obFOwCw1fFOAn54xa7Xtm5W5_HAhjdZEA8Gl0EIAFwzegZijn81k5-W2gwL8Z-LKH3i6l-XXHKlM1LnpMPYh1eAsgJFlBh69t2BtR697of3Z1t9DVPhMIeL0D_TFvw1rqBvFjbEtUVc0TIax1gA0D1KbVgsCWQKRd4qRmCbYo_i4NMlzCRKuBCfCHvI5z7hRy-ZmDlw8n6ebPF6WoXjTh834dw_YWegNzJOummN99qD3oEBn2A8ID9dt_bA0nb60KqzUPySZ-oENz_uKjLNaFw3RnRDBAvauLjYIOyBzEnkqIrzfv8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واژگونی تانکر سوخت در بغداد
🔹
در پی واژگونی تانکر حمل سوخت، آتش‌سوزی گسترده‌ای در منطقه الشعله بغداد روی داده که در نتیجه آن چندین خودرو هم دچار حریق شده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/455032" target="_blank">📅 20:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455031">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آغاز عملیات اجرایی نخستین پروژه مشارکتی شهرداری تهران در قالب طرح جدید خانه‌ریز
خاصه‌باف مدیرعامل سازمان سرمایه‌گذاری و مشارکت‌های مردمی شهرداری تهران:
گودبرداری نخستین پروژه مشارکتی شهرداری تهران در قالب طرح جدید «خانه‌ریز» آغاز شده است.
پروژه مسکونی فجر در غرب تهران، با متراژ مفید ۶۴۰۰ مترمربع، بر مبنای الگوی جدید سرمایه‌گذاری، احداث می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/455031" target="_blank">📅 20:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455030">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDXHZ3BNpbSnY61dYgEoFiFNiIKmPFZKJmumfc7pEIQq50wtODeRi1GHYGq28D03LEWpD-jFsKTKbLC3nq6WZU3LoQKmIPv9q6julL7zI9si1lb2xacCENsz_nyPDmO2GDbHGgeIPq-mNwaJ9fajKQmRvDsoqs4tIzj7pJh284DY5nji7RnORBDZ2oIT70-Y-ZZg-bnzLLoQXnYgq09RY8q8HN4wh6RFTvyI1INy_QICwvHAH7gsruCOjPXAZhdJS_HJc_gtACXzLZZfn_QQ2ZNNT-najJPgeRdv2UjfmfLD6vuQAtvxujG3V1CXgZO3U3UU4IYcvADQOGoVvYhh_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پیام تبریک مدیرعامل بانک رفاه کارگران به مناسبت روز خبرنگار
بسمه‌تعالی
🔹
فرا رسیدن هفدهم مردادماه مصادف با سالروز شهادت محمود صارمی و گرامیداشت روز خبرنگار را به تمامی انسان‌های فرهیخته‌ای که رسالت خویش را در روشن نگاه داشتن چراغ آگاهی، پاسداری از حقیقت و روایت مسئولانه رویدادها معنا کرده‌اند، صمیمانه تبریک عرض می‌نمایم.
🔹
امروز، بیش از هر زمان دیگری، جامعه به رسانه‌های حرفه‌ای و مسئول نیازمند است. در روزگاری که سرعت انتشار اطلاعات مرز میان حقیقت و تحریف را باریک‌تر کرده، خبرنگاران با پایبندی به اخلاق حرفه‌ای، دقت، انصاف و امانت‌داری، از سرمایه ارزشمند اعتماد عمومی پاسداری کرده و به ارتقای آگاهی و مسئولیت‌پذیری اجتماعی یاری می‌رسانند.
🔹
بی‌تردید، خبرنگاران و اصحاب رسانه با انعکاس صادقانه واقعیت‌ها، تبیین دستاوردها، بیان دغدغه‌های مردم و نقد منصفانه، نقشی مؤثر در تقویت سرمایه اجتماعی، ارتقای شفافیت و پیشرفت کشور ایفا می‌کنند.
🔹
بانک رفاه کارگران نیز رسانه‌ها را همراهان امین خود در مسیر خدمت‌رسانی، حمایت از تولید و توسعه اقتصادی کشور می‌داند و تعامل سازنده با اصحاب رسانه را عاملی مؤثر در افزایش اعتماد عمومی و ارتقای کیفیت خدمات برمی‌شمارد.
🔹
امید است در پرتو الطاف الهی و در سایه تعهد حرفه‌ای، اصحاب شریف رسانه همچنان پرچم‌داران صداقت، روشنگری و امیدآفرینی در جامعه باشند و با روایت مسئولانه واقعیت‌ها، در مسیر اعتلای ایران عزیز و تقویت سرمایه اجتماعی کشور، نقشی ماندگار و اثرگذار ایفا کنند.
🖋️
اسماعیل للـه‌گانی
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/455030" target="_blank">📅 20:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455029">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/455029" target="_blank">📅 20:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455028">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZD3MuQF6I2pjclfm51lPWoOv5wYIkLdGv1HUVP7EiQ_bTQjSh1P0sxi7gMLgZUNlrBcmqWvledCJkPdS38julllkH7RW_1R6At4Lyrti_vH4HI1aM4ET6tzGCT6tr-p3kqmGBSd_WqNS40XWm-b2EfMx9BTOhBmN536cn402JGWRbS9cKKyQJCYNIotygec3iyQOGpK3Nuw9udu4phNjQ1gGeVQl5usspDmszhWgMsZ1NQOy3UskTph4PiXHp9YYlBZxbY8SlskdXQW1IvIcIGFgFGqLbCdA1tKHTyqH-InXJcbGCmKjy7S-kPcq219saFqg3t339AyQLUB52izlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج نظامیان آمریکا از یک پایگاه در اربیل کلید خورد
🔹
پایگاه خبری المعلومه عراق گزارش داده که نظامیان فنی و مهندسی آمریکایی مستقر در پایگاه حریر در اربیل عراق، درحال خروج از این پایگاه هستند.
🔹
طبق ادعای منابع عراقی، بخش عمده‌ای از توان نظامی که در حریر مستقر بود، به پایگاه‌های نظامیان آمریکایی در سوریه و ترکیه منتقل شده است.
🔸
این پایگاه در طول جنگ بارها هدف حملات نیروهای مسلح ایران قرار گرفته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/455028" target="_blank">📅 20:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455027">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1909d40d35.mp4?token=j47e58v01I5ZYWitn8-shcVs0KEDdnJRwvZdk9ZNRZE7yC7uqbdURrSuwD4LYydPjodEYpe7-VZM__44Tk_-AWuFciNnHfTzsB0UItuzvGg6DfJr9pe2dIHzo_djQPWASjcLQj0HiDIAu53YuOfproDipIi5re2SaRXoOkPfiVcaLCJTI02xUiUujJC_p3V9UOdah4QubSkuKgj34lVrMSx8eZUTd-LT2Gc1yPLnHGcM2oJGx3WA6LjC5bFEgFAEDq58dBKy9IwE1_v6h3SY8haGj7hrjDWSGl4SrpbdYIzzXh8MkFeGuSd7KSZe0FqrIIVd35gvWGMaERnTAy2i7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1909d40d35.mp4?token=j47e58v01I5ZYWitn8-shcVs0KEDdnJRwvZdk9ZNRZE7yC7uqbdURrSuwD4LYydPjodEYpe7-VZM__44Tk_-AWuFciNnHfTzsB0UItuzvGg6DfJr9pe2dIHzo_djQPWASjcLQj0HiDIAu53YuOfproDipIi5re2SaRXoOkPfiVcaLCJTI02xUiUujJC_p3V9UOdah4QubSkuKgj34lVrMSx8eZUTd-LT2Gc1yPLnHGcM2oJGx3WA6LjC5bFEgFAEDq58dBKy9IwE1_v6h3SY8haGj7hrjDWSGl4SrpbdYIzzXh8MkFeGuSd7KSZe0FqrIIVd35gvWGMaERnTAy2i7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در راه اربعین کدام نوحه را گوش دادید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/455027" target="_blank">📅 20:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455026">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz5t-D0USYaBsjr4SgmeonqYN6wQUtSnGBXiI54lYJoKfxprG8nVBztlgkyD34k2_k9ScJqwFyNZOGDv6UghSatXfheGiANeVhS_UKsP6b7czV9XusXdmUn61R8_RUZUa7X9kgc3vK1SnXWPpIKjkczMfEJwuh-pH4rR4DtS1F3zCsxc3sPJtiV2qLrebsPTqaPyfWeYIgWSHfjLvwtZG5wadX-IG_jNjnIKuYpYDxR1ii9nkog4c2SE2y2TuxoTac4wLzogJUdraZGdSK95Ph9DhLSOVYdJxYNcXuDsX_P9EXoKaYL1NRWTdPwF-bkbTq4t3OK9Mt_ORNYC4N54YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرما جان بازیکن راگبی را در ژاپن گرفت
🔹
سایمونی وونیلاگی، بازیکن راگبی اهل فیجی، پس از یک جلسه تمرینی در ژاپن بر اثر گرمازدگی جان خود را از دست داد.
🔹
باشگاه کیودن ولتکس، تیم دسته دوم ژاپن، اعلام کرد این بازیکن ۲۶ ساله پس از تمرین روز دوشنبه ۳ اوت علائم گرمازدگی شدید را نشان داد و به بیمارستان منتقل شد، اما با وجود تلاش پزشکان، روز جمعه ۷ اوت درگذشت. دمای هوا در شهر فوکوئوکا در روزهای اخیر به ۳۵ درجه سانتی‌گراد رسیده بود.
🔹
باشگاه کیودن ولتکس در بیانیه‌ای ضمن ابراز تأسف از این اتفاق، اعلام کرد بازیکنان، اعضای کادر فنی و تمام عوامل باشگاه از این خبر ناگهانی شوکه و داغدار شده‌اند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/455026" target="_blank">📅 19:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455025">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8c6c98c2.mp4?token=CdiM77_PQ-zhenlWkApFlVBeAlADPPBbtrqjnRJXkL1hPyrRKh1qsXfsuKhwb3diie4KpKxVT0p-V69x1R4GsZkAixDctmdQ7fMf0HMvup55C2ZrjwV0JRl_CF7QR_W8cM1bovUyXPjI1RB2ZcvPXz3F3XhQ4OIYOBEyEQkjISkv4UVLwj4UTB3d30Q0VhnsM_w8O4YRAkjec2MmlevuPw3ZbCYDrmDSejcG2Vxsg8aE8UWJ6bNmW1qBtu1DtMjrSymRfpQmpaNoE0YxebumENwdncwIhrKRSV5pxMf3WFjE1tOquDdMv4whfcI0g5cdrs9EzU3y3TW7iEaKB9APE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8c6c98c2.mp4?token=CdiM77_PQ-zhenlWkApFlVBeAlADPPBbtrqjnRJXkL1hPyrRKh1qsXfsuKhwb3diie4KpKxVT0p-V69x1R4GsZkAixDctmdQ7fMf0HMvup55C2ZrjwV0JRl_CF7QR_W8cM1bovUyXPjI1RB2ZcvPXz3F3XhQ4OIYOBEyEQkjISkv4UVLwj4UTB3d30Q0VhnsM_w8O4YRAkjec2MmlevuPw3ZbCYDrmDSejcG2Vxsg8aE8UWJ6bNmW1qBtu1DtMjrSymRfpQmpaNoE0YxebumENwdncwIhrKRSV5pxMf3WFjE1tOquDdMv4whfcI0g5cdrs9EzU3y3TW7iEaKB9APE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت خبرنگاران از عشق و سختی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/455025" target="_blank">📅 19:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455024">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تشکیل تیم کارآگاهانِ زبده برای دستگیری عاملانِ قتل حمیدرضا رجب‌زاده
🔹
سخنگوی پلیس: تیمِ تخصصی و ویژه کارآگاهانِ پلیس آگاهی تهران بزرگ، برای شناسایی و دستگیری عاملان قتل فردی به هویت حمیدرضا رجب‌زاده بلافاصله بعد از اعلام مفقودی تشکیل شده است.
🔹
از رسانه‌ها و مراجعِ خبری درخواست می‌شود با توجه به شروعِ تحقیقات کارآگاهان در خصوص علل و چگونگی وقوع حادثه، از هرگونه گمانه‌زنی بدون اتکا به مستندات اجتناب نمایند.
🔹
اطلاعات تکمیلی تا ساعاتی دیگر از طریق وبگاه خبرگزاری پلیس منتشر خواهد شد.
🔸
۴ روز پیش ویدیویی از پیکر آسیب‌دیدۀ این فرد که از ۱۵ روز پیش ناپدید شده بود در یک کانال ضدانقلاب منتشر و در فضای مجازی دست‌به‌دست شد.
🔸
بررسی‌های اوسینت نشان می‌دهد بیشتر ادعاهای قبلی این کانال ضدانقلاب  تاز‌ه‌تاسیس که تصاویر مقتول را منتشر کرده نادرست بوده و با هدف دستاوردسازی دروغین و جذب فالور مطرح شده است.
🔸
برای مثال این کانال پیش‌از این تصاویر قدیمی اقدامات گروهک منافقین را به نام خود منتشر کرده بود.
🔹
تیم کارآگاهان پلیس بررسی خواهد کرد که اقدام تروریستی بوده یا قتل به دلایل شخصی انجام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/455024" target="_blank">📅 19:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455016">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDnWlb1ZiWtmWNsmCn7LZEYeWExE057WSz4ok-zCUwiHcRlyZfImKKiB8LMWqeklP7Lx9Xln6fQTk4h6hkpEhXlWwz5F2d02Xsp3VGJHbrMfpipuG4eEvnKtee5GlDf5wWOTQYNBEOJyWagP-9gt57ke-9TU6oG4RPyXRP3-0SFiV9Z5c2Ber92yOVRPMXTBOOYdwg8eYS44KYI4xJMJd2Q9IX08QLLB1jA8yEI-svJNUUsIncw92XD3NWtkmnY0RpiLAC8yoISiWAa_XaNed0OnnGSelilyH1EeJqLSHV3T5vGSagpQ7zMth6ccVOejYhhPQd7UAov9aPY_mhAIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqkaqqWBbVODGW_t0Kk68Jw6dAD1PiQAltR9rjJzy0zQToeNjzBuP2s99nJjA2_09P17vyODdEkAb-gxKJGHo91J2uabXlhFxH5cM4myp29pQKoGl7IljZk-222Uf8dRUMLxYVMFdg1AtAUPy2UEr3TRfoEcaBVa_fraviqpxoVnmlotpF997NHensoP6hehGwA45WQYWaygK2xFovLpMjdOtHEQDvnVpZM_-P8bmy9-CKpLwM9T-iAnCb-dNgNDFo3bjuyfaFKPUcJ_oqyp0zK3cFpnLPdb-vlteD1fvrz5seVz_JOOxIMQvtYg4pQlwoVZRO4Gb4joATUFO3wPEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scVIq-UyiRbB2c263npg1leplCK3NTVYhzaHjzdWG41-wae8Q9dsjj2n-m_Tu7__3zvtcBdc3rWKdr_xLRACmWfdY2-2X6IlbrAICvKNl6MnQyXaLLQYysQyB66cs67WVKBHb6G95WWn3EsxPACMA5e_ikIXZeIfgIiIT9wkMPwDF0C9Nqb3Z5zdE9tYYupvcNUAZv_axy-VkxBDVhd-RGjMtER3nE93XyT2D1JPVMA4sG1BWo2XTyMhxlm5luq0S-fy4c6wOtSUo-GoEEM-E2BkOO89LldgI_Cx5cGsAVpA8MjFIDHAXTeHWV54SWMcFDjwLajtQFItkBGKBC4u2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZE6ukA6v3AuaGDIuWbbyd7dOBUE0OkDf0JVtJs-f26M7EwRB7DaYy6Vp2FySJ5d_C4OxR4ntwx3IOdvXrj5vDyr1xP4KiEGdEgmC2MOihwAkQ03VpWOfWjFaMO5RL7OLygiRjveuRORCb_Wntgza9IFtfPv4Kp4LpmjEbgJTWGFGURW4a0gj8QSODsvghl8NOYqGgSYWyGNkkXN_0jAsqkh3V9zhPbGaQiLUphOd2fjWT49vE1tk6O0dcgeeQupx3y5cnTMxgg0UGZy7YO8pRtAt7ZiE0CCo_HCIIsu825qnM40Uw11XFi59jTmHAIhUvKoxdReHZ5EQTi__hTpFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7b6KTGQHfVc5NA7hf2BuTdiNtBKDGTqsZiingz2yJZogc56VAD_sNWXQQRf7x1S9ZYFI7l_EpB8G_LP6bTNZvUQfUp39AoEHiYHfkoB1iqS7yCuVvWBbmVahw5YTcaHnoxPzzpzonkU3H94f5KvYuUTryW3jAE4zLferWb6y4-TFXJAKbt6YeyLSAG2AiO-KEQLIOuMjw17cFIKrLtLGsMJFdG_xEpPrOuMZAc_XnAOvV5hxXQhNR2ervZUIpimAkt1Q8IQzWY77TfDkz_8FSHGahpcy3p0l8-3afzJ4mfZECR3JOh3MRSQRdIn-ah2TQCCFsKwubzuOqyAOcEB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rwfKofTPyCuGE1z85gT3IxjZuultSgQHUImPickoB_ZILipw0JpaiuFKEWT_bsOYyq4LFtFnJi_IBtStub0-9oUjhrrAFmWET9SaJmiDhdpQIdhbPUlW4-rzvZPXpCgE6oBXIegykLCm1ybSd6c8f1hpuQUy0RJRgGMzFPQUCtPigfOM-s0XRgdpKrGe8sZrY232udj3zQP275KHJeydBU47zdpWP1tJWutwntWTNNZp3mDjCR2gpX-lbIDV_AMYBB4AYFQgFi91s6JhJIh_XKRmnJzvkcFEcmjfW-wLLF89-6orKgsDiseHGRTdr3v8xoTlMkH_OYx4zvCe1L0J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqME1uuldn0nskneZyp1flFeqh4GNJ-y9Mwo4hINq5gihF9om7HboF5Y0MViS3Lh_0PVu_QfxJqKvz4_-LpULgnWhUA9i2xK4CcPBBZRxPS_7DwFE5IpQtbkYt7MzrXOx5nsXskvRBEG18S7hZRuuUkO-dJy5fu0fTvTbPAm08VFYOnOfWiZzVFz0GuZZL6vcVkNwVELUbAM7YzwqYi17KxDhxjF0P2k-RbiYmqX7ca33qrycM5Z9WvqV-bV6KZPPGp0PCZ0_K_xCr--SfQVzV6QJF9sjQx91n8SHJv2lO9asfoMmj8ynBGZQwNZY89Ss8T3zQ6In6xSLDtizv9zrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت روز خبرنگار در اردبیل
عکاس:
حسین حسین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/455016" target="_blank">📅 19:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX0AOdNjVz-e-UkWSuzevVl_lWWZBpemvgLYY-j7bNRhBP8bJFZaCMcY47KpNvJvufPFpkkiLV57O6lMrrStR57vvOhWmnSKxKJx9pzn-vAYEA7MLI1YISLAXNT61geSEgx2YVhvXOsksoww8pQRT1oQShHSN2KCQ-0wJ8e_x7wnvRrnbksJrWhtvDk-N1YT9KxEniLYnH7QuvCTcT6B2uLeI4dDmkF2FYhvs4Y-y_ds3z3apvVR0vRxvpsj6WJP0g90zOnOeOf_yJZIuRNOCmWKYa4QvjTsYwtrH0cmxNLwpgMAUsKg0AlQk6IRdRu7HpJ90cOIAzV2Zg4ncLEXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای معاون ترامپ: ایران گفته عوارضی دریافت نخواهد کرد
🔹
جی‌دی ‌ونس:  ایران و کشورهای خلیج فارس به ویژه عمان درباره اطمینان از عبور امن از تنگه گفت‌وگو کردند.
🔹
ما درحال بررسی چگونگی ایجاد یک طرح ترافیکی هستیم تا کشتی‌ها بتوانند با خیال راحت از آن عبور کنند.
🔹
انتظار داریم پس از پایان درگیری‌ها شاهد خروج همان حجم نفت و گازی باشیم که قبل از شروع درگیری از خلیج فارس خارج می‌شد.
🔹
ایرانی‌ها به ما گفتند که برنامه‌ای برای دریافت عوارض از تنگه هرمز ندارند.
🔸
اظهارات ونس درحالی مطرح شده که در روزهای گذشته رسانه‌های مختلف غربی از مذاکره برای دریافت هزینه‌های مختلف توسط ایران و عمان در قبال عبو امن کشتی‌ها از تنگه هرمز گزارش داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455015" target="_blank">📅 19:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455014">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oynGJSt4RZ4gIN7d8Dp8Ug2w44r236ijJXgSsfkkxWTvEqTkM7N35G65cNQJLB010fH3AiYPsdbrV2Is6VQxdsrxBZqDzUXvp4UylKZCNuFHvm-TENEhWi3OoApQ5wuF6DbGkqeyEwX4LQPVTXJavv9tUWxFBc7SMUWYHQBh474wbql-paoMXz7bkLgszc3YntJLbcFVCtsm3YgmlZI6AFRHlypCRf1tEZc-A1FryLhMJDdytd0uio5VCZrJhNHeTP9t5hkUK7iNsXqwFUxA28L2sXq2Us-ofZT1bafoZ8me9P4Pne4jN8k7qja1kE8RewonQii9CbrWYw-JcfV9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: نظم ایرانی حاکم بر تنگهٔ هرمز غیرقابل بازگشت است
🔹
امیر اكرمی‌نیا: مقاومت ملت ایران در برابر آمریکا، جایگاه ایران اسلامی را در میان آزادگان و آزادیخواهان جهان ارتقاء بخشیده و امروز مردم ایران، به عنوان مردمی مقاوم، بصیر و شجاع در جهان شناخته می‌شوند.
🔹
امروز نظم ایرانی بر تنگهٔ هرمز حاکم است و نیروهای مسلح ایران اسلامی تا تثبیت کامل این نظم، با قدرت ایستاده‌اند. نیروهای مسلح در این مسیر، هم از انگیزه و اراده مستحکم برخوردارند و هم توان دفاعی لازم را دارند.
🔹
آمریکا چاره‌ای جز پذیرش وضعیت موجود ندارد وگرنه متحمل هزینه‌هایی به مراتب بیشتر از گذشته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/455014" target="_blank">📅 19:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88563a5558.mp4?token=mNZxCrFnRSFyXJR14q4cbny0P-VcZ1yjwgjZbtZxUzfDP3a6hP_aI1EqeRFe7c_pYieOZhcOFkovjKlUtcC6umfV8FBj9EO2fXJDcqYNhuA1ZGxyqFqoJXtDyvV99uHGKi8X2zE8275APHwWTrrE24TFV8kTFS3WSGIa3snCE8hiwgZvpjBjMOfckpdXQ-vRkqEZzERa2oMM2PkhnmWZll3BydEH3VgCgszfUdSEu9_T8rn7vnFtAMfY60B69KxIxYHpWv2edbNylK9wdKEAecJ6Rcpj0PAZ4Gfs4LAr1-UCi2IMZdM2JiSpKVOUn7y6vJThg9W2yf1kr5f-LyHo5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88563a5558.mp4?token=mNZxCrFnRSFyXJR14q4cbny0P-VcZ1yjwgjZbtZxUzfDP3a6hP_aI1EqeRFe7c_pYieOZhcOFkovjKlUtcC6umfV8FBj9EO2fXJDcqYNhuA1ZGxyqFqoJXtDyvV99uHGKi8X2zE8275APHwWTrrE24TFV8kTFS3WSGIa3snCE8hiwgZvpjBjMOfckpdXQ-vRkqEZzERa2oMM2PkhnmWZll3BydEH3VgCgszfUdSEu9_T8rn7vnFtAMfY60B69KxIxYHpWv2edbNylK9wdKEAecJ6Rcpj0PAZ4Gfs4LAr1-UCi2IMZdM2JiSpKVOUn7y6vJThg9W2yf1kr5f-LyHo5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا موشک‌های ایران تمام نمی‌شود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/455013" target="_blank">📅 18:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb90fa67c.mp4?token=oeb2M6Mkec-OXLagtEBl4zh41RN-t8sglaCGncwgTl2S7w4jgmPX7uQSloMc_OVAvPzuVlWUuAowHAuHwL7D2xDtCg5DcoLlpBkVoAWXFzOzAJXssp2WCbZd-WTer9-cOFKB1OS34ROTKtd3wldkzNgAsO8J0JX_xLeP3xZ7bHU1qFP4JB-6mC4HmRGxJ0X7XSW4YxwtrpD6GYpAP_SsOUZG8Gli4HqIH4Vb9tuTlaBH4r9Vcq-8f1dlE0r8clUPz5VClLW0Bfp1hG_tKMvRJMbh5sSamvSsrHLEODUusfImspwkmMqUOxZkjSDZ1qV52Wvu5C_u2rFfUQSRoyLoYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb90fa67c.mp4?token=oeb2M6Mkec-OXLagtEBl4zh41RN-t8sglaCGncwgTl2S7w4jgmPX7uQSloMc_OVAvPzuVlWUuAowHAuHwL7D2xDtCg5DcoLlpBkVoAWXFzOzAJXssp2WCbZd-WTer9-cOFKB1OS34ROTKtd3wldkzNgAsO8J0JX_xLeP3xZ7bHU1qFP4JB-6mC4HmRGxJ0X7XSW4YxwtrpD6GYpAP_SsOUZG8Gli4HqIH4Vb9tuTlaBH4r9Vcq-8f1dlE0r8clUPz5VClLW0Bfp1hG_tKMvRJMbh5sSamvSsrHLEODUusfImspwkmMqUOxZkjSDZ1qV52Wvu5C_u2rFfUQSRoyLoYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتصاب فیلمی با عنوان تغییر دبیر شعام به خبرگزاری فارس
❌
به تازگی فیلمی با عنوان «انتصاب محسن رضایی به سمت دبیری شعام» به‌عنوان محتوای خبرنگار خبرگزاری فارس درحال انتشار است.
✅
خبرنگاران خبرگزاری فارس تا کنون چنین مطلبی را منتشر نکرده‌اند (و مطلب منتشر شده از سوی کاربران این خبرگزاری بوده) خبرگزاری فارس اطلاع‌رسانی در خصوص این اخبار را منوط به انتشار رسمی از سوی منابع ذی‌ربط می‌داند.
⚠️
خبرگزاری فارس بیش از ۲ سال است که تبدیل به یک پلتفرم خبری شده؛ در این فضای تعاملی، کاربران تنها خواننده نیستند و علاوه‌بر درج نظرات می‌توانند تولید محتوا کنند، پویش ثبت کنند و حمایت بگیرند تا با رسیدن به حدنصاب امضاها، مطالبه‌شان از سوی خبرنگاران فارس پیگیری شود.
@Fals_News</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/455012" target="_blank">📅 18:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_j-9pLq-lqELo9BYYQYB_Ux6skE6MscoSyTdFGzwiqBjOBitltUOsiISB8Sse26ZhrMYYJSOBZEOu7O0V0cJJI7Tf5RVGOT5F7cef1yMwDS138O6_RYNZqGPvN8gwnFtudnAo1o7nbMg8qFX_h8pK-vqpLjiUEe9K_vkVLrmyyJEHZQz1XP-cPDEOoipQJsRcw_bLJUsLyIssZbRydP6etj70OdonnjUaaED4E-qiEUFYjkR_Un-Y0cqnMmpJJZrqeEFDQMfjyd1JKShFDrjXLrOj4SNhqUmyl5UsaDdZOuy_EF1Rnjr7N1GVVY_OdP0xAizCl6FeF-GAex7002Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
موسیمانه، سرمربی سابق استقلال به‌عنوان سرمربی تیم ملی آفریقای‌جنوبی انتخاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/455011" target="_blank">📅 18:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455010">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G38QJLbgf8BTQJNQr19shZLXSP8ae8qRma9KS5jFEOF41grkEPt6UEK1I7s2iYJIebo4-V84gno2GDIXb7uUvi2XUx6Zj8xKD6n1TvrbTxJ6PXMizTZbv2uzo8vZrvOBKC_KjV_euNJZT4G_tLiGsv34HW3ElLWoYVamF2EbyA-1ZE8nnd3Lje9y28ZGswMHHMBjzbLV0jBOhe7kJQwW1qRXxn9jwfVv0VBNmYARKmqWSU-cnl3_CNuNSUejznyyT4U1NQZSFdYWpQfW7goq9MgicK-8gnUUPKnnjr7mza_1btRUgmjrAIqA8lu4eO3PG4V-xVAPZNGA1jf3Lw0VZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دهقانی: رسانه شریک توسعه ملی است
🔹
فرید دهقانی، مدیرعامل شرکت معدنی و صنعتی چادرملو، در پیامی به مناسبت روز خبرنگار با قدردانی از تلاش‌های خبرنگاران، بر نقش مسئولانه رسانه‌ها در حفظ سرمایه اجتماعی، تقویت اعتماد عمومی و افزایش تاب‌آوری کشور در شرایط بحران تأکید کرد.
🔸
دهقانی با اشاره به شرایط کشور و مواجهه با جنگ، محدودیت‌های انرژی و فشارهای اقتصادی، اظهار کرد: اگر صنعت مسئول تداوم جریان زندگی اقتصادی است، رسانه نیز مسئول حفظ جریان آگاهی و اعتماد عمومی است و این دو در عمل، دو ضلع یک مأموریت مشترک یعنی حفظ تاب‌آوری کشور هستند.
🔹
مدیرعامل چادرملو با تأکید بر نقش خبرنگاران در شرایط بحرانی گفت: در روزهای جنگ، خبرنگاران تنها روایتگر رخدادها نبودند، بلکه با اطلاع‌رسانی مسئولانه در کنار مردم ایستادند و در حفظ آرامش جامعه نقش مؤثری ایفا کردند.
🔸
وی همچنین با اشاره به ضرورت رونق تولید، سرمایه‌گذاری و بازسازی اقتصادی پس از جنگ افزود: اقتصاد پساجنگ تنها به منابع مالی نیاز ندارد، بلکه به روایت واقع‌بینانه از توسعه، چالش‌های تولید و مسیر پیش‌رو نیز نیازمند است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/455010" target="_blank">📅 18:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455009">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU-EErLbfZrL62BS2s_WjcjgxYAhWUkrZT-hZKo3C13DRX5j5nM0XIX08C4GEGtFRFuaIT70qeG7ojBZHmeL8wFt0mQFP_70T8J1myof6zF6Rw9n9LLV5GLt4hen9YajUDzjGZ_gtBHsczKFHa6fZmo40cr5fsOl0QOsmLffOX2bZ2sF09HilqhT45pWDLzv04fTeJpK5GOdcFBSppgHyimkRHk7ijnf7GijweJYLJhplZlsCymkiwi1osX4WV3ew77W0LoJ5uYMJLYdjXf4U9aozhLIWERqgO3S4P6tt3g9AbZcdzj3tfeoD3JjyEi8e7-sM4iFXf07bACRVh4ZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ثبت‌نام دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه» آغاز شد.
🔹
این دوره یک برنامه آموزشی جامع، کاربردی و پروژه‌محور است که به شما می‌آموزد چگونه هوش مصنوعی را وارد فرآیندهای واقعی روابط عمومی، رسانه و ارتباطات سازمانی کنید.
🔹
در این دوره ۲۴ ساعته، از تولید محتوای حرفه‌ای و مهندسی پرامپت تا تحلیل افکار عمومی، رصد رسانه‌ها و مدیریت هوشمند بحران را به‌صورت گام‌به‌گام فرا می‌گیرید.
🎉
ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات
📝
ثبت‌نام دوره حضوری
📝
ثبت‌نام دوره آنلاین
مرکز آموزش‌های آزاد خبرگزاری فارس</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/455009" target="_blank">📅 18:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455008">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/455008" target="_blank">📅 18:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455003">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار گلستان - خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g03owI_9Ccis8E48ZRcfPWbcfnsn_-7Z0AitN9Z0lSJhjMmYMXjwkHsBe062HwBQK31qiKiVqYeVHPUEwMZLnWQuTE1kBMkZy20xvE6RtNyQ0XOMEYY6rU-3jH44FE7wQY5PcHTK6RQ-qdz5XsN8N_4mJda3NQk24HhB3BSqbsRjfqSMUh7pZ76ZXOaqYZWAu2pGNPy_tyFgLqb-FchuP5Ut5gLvN4Jc7mVFI7xNMvMJAOffdsTRp15TYcjhCJT1NHeKe0D0k3enkDJhLmOTzE23TRvVAj0pudczLZgyQKox2w5l0Cfg3B0cwjLUQf7uk99YYDwOmgvWFAOU02Ob9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0sQYPEHJZoTX7TwmoQPigQcrSYJXEfvx-B0bu18CC2wVbv0iDxwlZKi_BsR_TT0Wlbgx9QMEIbS-7yi4MimHTxdZT3xPuKrWuUq0rmLhopCVbk0cpfldCRTHt0BMxtjrxoIr8wIKPrWBpCSNlQbQuh5d9Dv9Z2tQkzyvo5kLolSU7HbG8eqz-28zGL21O-yXifphJsl578XOV3uGx48e-WCtMqAKeqLBvT18VebarlyPzhqdIKzgNRyCj5Lu8TtUJXn0jPaknUaUHfOwaG4vXRIkilX5viA1888GwHhdr4fGqLNdptjSYRKF0tYwznrOnP7kEeIjN1ZjJCQ9p-TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_gcSTnTIMxz4mlu0xSfYwLYreQLj58dbn4zYBPtzD7UDF00eQ4a6jDzb9RsgWNU33Kw6RasgGd0bNwJlEo-J41i3jE6jtCVd-40CsC_6rPO5uQ5ePuoVwOf_-QLYyr8d8aOKUC5nSE39EYvxACuhMebbiaMozu3befoNrfZ2gTjg1aKp2cSTJkiCNn6osPu5POsNsxBeXgZHEeVx9A5KR-c3Tx-IiaopW-v5qUUS1X3QL4TNMRpo0T3L6vxuRVvcpfHOqh290PgFMJBwi8140zcAD_BtbvQ13F6BuN5a0ztF2BBqAtRsAREWoGcjTqyfOi06weLt89E7KT8rxvbyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EadblJvvVLoQES_MCIKDbgk_WCYfsnjZRFRSuKfZPcXGmp9WFPbK7rX8pekq8OPtxGFqezO6_yiy_bFCKOfrBWY0FViVGIEIYeFivMAn1o1MdysK62G2q5ifm92Oc4QVbDYser2x7XWM3vArwuvjLQq35k67KIU71arrjGInXXS4poPzVkZG86vy-cy3TKYZ9bQjJfkkI960OvgXcSp6MrTVzVVD1oH22B63eAFIu4u9tsrlsYXuJ_zVhhQVCVLeSxksV_3oxo7PGXXkemNavn0ljva0_nSOMfWyi-mbYsc_Xh9UdeGWHLipguAFfshunW407xJCNdVXVkko-Stjcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور دادستان و رئیس کل دادگستری استان در دفتر خبرگزاری فارس گلستان
🔷
دادستان و رئیس‌کل دادگستری استان گلستان صبح امروز با حضور در دفتر خبرگزاری فارس گلستان ضمن قدردانی از نقش موثر این رسانه در انعکاس اخبار، روز خبرنگار را تبریک گفتند.
@Golestan_Fars</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/455003" target="_blank">📅 18:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455002">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d2d9423e.mp4?token=hNoyFPnYbacF1Nu1YTN7LrujL8BZfNNdD--B56uIm2cw13qj6490agkT-0Gfa29bsDqweIYkW5IAi1VX2J-GvoS7dXvxBDBiU8Y_2Dcv17gjtEajRJeto2dWKDSICE0YV5BJ4LSuX0pWDLpHhLDCIVswrN9K0i782ye-_zVwhvDjEakDGIJMy3QmJPttAo7MrESbqUtuty08rKu9MvTgk4COmjmOKm9svwY95WBv1ATvWuHL0Qx5rzXcVAkFi4evVuQ5ox1DOiKJcsYu0Wnlh1eNSXCN30-AcM2KOiLbznmNApKoJEe2aYxGkRw9neVrxtG3YSqNN4FVVkrw82EaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d2d9423e.mp4?token=hNoyFPnYbacF1Nu1YTN7LrujL8BZfNNdD--B56uIm2cw13qj6490agkT-0Gfa29bsDqweIYkW5IAi1VX2J-GvoS7dXvxBDBiU8Y_2Dcv17gjtEajRJeto2dWKDSICE0YV5BJ4LSuX0pWDLpHhLDCIVswrN9K0i782ye-_zVwhvDjEakDGIJMy3QmJPttAo7MrESbqUtuty08rKu9MvTgk4COmjmOKm9svwY95WBv1ATvWuHL0Qx5rzXcVAkFi4evVuQ5ox1DOiKJcsYu0Wnlh1eNSXCN30-AcM2KOiLbznmNApKoJEe2aYxGkRw9neVrxtG3YSqNN4FVVkrw82EaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  یمن: تجهیزات و ادوات نظامی عربستان در پایگاه «صحن الجن» هدف قرار گرفت
🔹
سخنگوی نیروهای مسلح یمن: پس از رصد دقیق تحرکات نیروها و مزدوران عربستان سعودی، تجمعات دشمن به همراه مهمات، تجهیزات و ادوات نظامی در پایگاه صحن الجن در شهر مأرب با تعداد زیادی موشک و…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455002" target="_blank">📅 17:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d217574a7.mp4?token=nRCOCrb8cP_oMjg6sMK0AbDgT6uwSCgMimdb2hHKyJlU0jM40U9duWrGNWd2ICMNnRNCYk4uC0fjS61l9tBvPuo7aOStYEGX-e7uQyJ7Md8RcvpbIjYTlVhq5lXI8KdKkwAChWob-vHsnLwOdrkUakgd5lMrS_K_n8X-9Zrpj38UWHEZHkJFpjGes3uP3ZIpGZ6BP7uloTjNLMdUKA8NbiyTDVSBWbBn5uS6RSt8MN1mFtcgZcl_P6m10Z9G-HHiUg96Z1p0qolgwLHRWTfL0XU2OW6mLo2EGWGdPGuDJdTKP8k6KwCQ1t3vDJsBfhXC38CBkDXTY4wKxkn-tHsToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d217574a7.mp4?token=nRCOCrb8cP_oMjg6sMK0AbDgT6uwSCgMimdb2hHKyJlU0jM40U9duWrGNWd2ICMNnRNCYk4uC0fjS61l9tBvPuo7aOStYEGX-e7uQyJ7Md8RcvpbIjYTlVhq5lXI8KdKkwAChWob-vHsnLwOdrkUakgd5lMrS_K_n8X-9Zrpj38UWHEZHkJFpjGes3uP3ZIpGZ6BP7uloTjNLMdUKA8NbiyTDVSBWbBn5uS6RSt8MN1mFtcgZcl_P6m10Z9G-HHiUg96Z1p0qolgwLHRWTfL0XU2OW6mLo2EGWGdPGuDJdTKP8k6KwCQ1t3vDJsBfhXC38CBkDXTY4wKxkn-tHsToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع هزاران نفری علیه صدراعظم آلمان
🔹
حدود ۱۰ هزار نفر در شهر پلاوئن آلمان در اعتراض به عملکرد «فریدریش مرتس»، صدراعظم این کشور، تجمع کردند و خواستار برگزاری انتخابات زودهنگام شدند.
🔹
معترضان همچنین خواستار کاهش هزینه برق و گاز، اخراج مجرمان محکوم‌شده و مهاجران غیرقانونی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/455001" target="_blank">📅 17:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454994">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2Kge2nyAN4-elTRRw0Slhd9e55aZqT7ruwR0R6f-H4IGy7rElimqPOi0sQmHB9XaQbkNBuF-eakgsyRIphU1bHM_fFiUtAkIEY0iHa0S2WSa9unTuajGcDuqcIzuE_ySwW3i0luhnsv6V2fGsr35hf0jFU1TDHFF-_8u-H8NLzJQ82gkS3nvECd4OEH9LjHn6BVBKJ3zOlMsAU-lLA5wNY-kRd27not3nATmbYQfMuVJMjx5_j-utHZvwNKC2Px3NF9gSfx074JYhkIXIeO6c-YkufP3xdg9iLCgMxnT8TNU2PVHIKDlNZ_fRS01p1jmw6LTbicDWlDHM3-j5V2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnxjt8Bjkq5qBPjeHc-dq9RzkC223_7dn-LrQpXTa8_d1DKhFXWRkHsb5wg8XCcclKsEcq9Pi3wBtrGKTRmYneUVIDG5GOyn2D48wUDacvXAQEqQ0Rn6R0pt8S8f7HYXg5dvI9Uq2Yy_oN6AEf1v7iAxIzhjXjCxwXaieF75NP6q8K9tl1g6Xo_jVqcj4NgtT-30MtlX07EHrZKbtBEcdzWX8chfJeKNT5lthMpNuWI3RDL0Dlx3tmZvmh5CpeTH5BHEyx-Cwr2tyPDlnHHeunkKNTM7pyGVVPIjmn7xm054-al4_zb6UuVqZ1dEuPClKvSGEblkP6N7IPnwdpe2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9eJ-f-u7W5qpEHH3MRL05ECr6QjGncLfKvPbuUglcH3Y6BTG94M5azAVOQ7WRn7elnr3ZHsUuDNzo6kUCrgXp3wQIcrPT02qRcWUanKkrC2LqIblPxfquyTFno3CaCvxVhpJ3t8SHaEerMcHaqdukugcE3RDCuakZ3VIU4R2rPCmtFSQUp7Q_dV6PFeeToBPCsm8Jep8nbBMxA7E4aIgqenWPp8BHJBl9UUP0AaiZYJAJTNr6wHQjNrsJ28ykiUvDqqgWYKUubM2MISS682XtUQoj2a-hX5IUmZQ_bUjX_IofBJ3pGg1xUmY90icnI44Ha3seLAYCQnDdOok_WvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOmhdzOFqy-kxK3-DQ240N72aKg9nAIJoyU3cvxNYY62xz37iGyX8ihvXGWG-MSVdTy1VXrXXuWmuaDC0f0KOLt1YyNNSTKRUnaJsPaCFCZdecCCi_zWA5CGrx6SGQcYFLtNj3VrXQbV9S7zoDcAjK8cE4DNfHlvJLdDj1mHDo3A0O5Sbd0BC-dsH35Ij-BNuk9B7E8vW9mQnGs8pOTfv6WRc9Pg9hh3xxwPUNts9Y9C21TrGtsf2MC8zaE7AP8a8t9ANEqJ1Rnn7I8-NM07_-ZoMk9uJBC0qJa0hsANyjCO9ZJRPWcE6m63iEqjucIZJ6aqzPSRNOKERqZrrqd0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_sArapUqeA8kTGpK4qcDGQVdP1EtUsn2ovBSgICEI1OPzSpoTDHCPNlUBhpHHE4D2AjXMEieVYAnkTkkJ6YNR3t3YETTfxbu8Hr5AZgrnqMHqt8nK9cTOHcuvNaRrq2c850ZTn8mrZuYKUU4pBZYWSEhX6RiK0GaU3V1Xc86lY2J4biq36AbgE0ogMfX6gjaZwWZwfP3e8u82h-XYWQYkDJdHjy2DrrXpP9V1gUswSlBQVkQIfWcI-sLe_42YFeoGX-N9Ga5DrCB6rX587z47IYsvIbRRmdcb5eUWp7zYdqw2dQQjKtyuYkr7Q4KBIUYf7NFRl-CRr4dXunAt9M9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ge-dYJOG47Ewni1LTEt9YdRWTQkp5YyXqUzTOrr2nkZjluJ_nZoX8MFCoD7xKCBHny0ilWiDvlhvc1_1q6J2_7DOUU7Ax_r7yOeShm9L57If4hE6bo2CMOLahsfRNwdQl83IM2Tu8if-mdByS7D2ImFzPVubO3KMY92dalNY0Yp3kGt5SCE60y9dkWZ1eVtaL6M3XG5o45x0lgzqEjI_zOUl_UeE9ZaiB0H7DqiGV5Tefc2sPF_E3J3__J1-a2x31mQ1Q83sMYb3hguweTZsGnq--Ack689GAsPmHM-4mFMav73i1D8NVYMneLTuhShjZQZ3fkVgDJYuBL4KLLiYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wq8okoy9PQVPaOWyRhZfYIwJ_0S4lBvLQ6Z4-Hi8t9YNMys3vfHlQIAmfapSpusq15ugyRuAUA6dAUfn91fxiYLjkavHHOfo9ZiH4C0taxuUzJw2aSQdPBL6VscbRbXWZeCuaz7ur19rmnTWn41T7ZxEG1wlMGIgVJfgd9ErD84AG9oTJpq5NAg63pMlXAa2c0lNOf7j6a0Y-mRB9S1J3COAZN1-4uU8_AjctpVqRHOHnaB7ggYS7IctkVMD5YOqpePE27TstWvAXcuO3ePTLxkJGcYgdyQ83tOsuUPKu-eSh0HitQiW7CDejhE7jVWBYj4-YiM1UC3trDYV8IinJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
رئیس صداوسیما مهمان خبرگزاری فارس شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454994" target="_blank">📅 17:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454993">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e3eaaab5.mp4?token=ap_UQ8e0-1cLjeUXjeLKswb0AnRmy_a0KrodAklOUmlVxgBd4rp_-T3uAedJCUqVQCBepIHZXpn3ifDGbXDgA315awZMg6se35ztcZjhSQDZ1GFojv22gcaQEUzB2cxTSJT0AGDpXGshLHfw_bc69eb9BdU-n7OkoeeWn6l4XHaCQfdPFXJ8aZlz7tDLud8CoYfDB0j7ecPukcYqWW4fI7Ego4R2ZN46wnAu9467XPACfDyAdCFLhsYxmZbAYpsvIXOkqUasurMpVp3FHt4_WBqrAUTgmZ12R1T_6C4TT07mCRmNH_jHAPRyLCsMPyhuyUIrlpbud8TtshFYAEahlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e3eaaab5.mp4?token=ap_UQ8e0-1cLjeUXjeLKswb0AnRmy_a0KrodAklOUmlVxgBd4rp_-T3uAedJCUqVQCBepIHZXpn3ifDGbXDgA315awZMg6se35ztcZjhSQDZ1GFojv22gcaQEUzB2cxTSJT0AGDpXGshLHfw_bc69eb9BdU-n7OkoeeWn6l4XHaCQfdPFXJ8aZlz7tDLud8CoYfDB0j7ecPukcYqWW4fI7Ego4R2ZN46wnAu9467XPACfDyAdCFLhsYxmZbAYpsvIXOkqUasurMpVp3FHt4_WBqrAUTgmZ12R1T_6C4TT07mCRmNH_jHAPRyLCsMPyhuyUIrlpbud8TtshFYAEahlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلنسکی برای خرید پدافند هوایی به اسرائیل رو انداخت
🔹
رئیس‌جمهور اوکراین اعلام کرد کی‌یف آماده خرید سامانه‌های پدافند هوایی از اسرائیل است و مذاکرات میان دو طرف در جریان است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/454993" target="_blank">📅 17:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454992">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcfEPLHCy517e3dGoSR7KD4aCkXXxZacJz2EiFfoF89CzzYogaqixgqodGulaR38uAF_uBxDMDugZi3wK04ljXZOMFCpsvt9ZbpQlKek8OV0GQUsUq_4z5m6sxNw-HlVaeQ-SD8Nz2xUh6YjZalnXWzGTyrmw2hrWymR_Z5QIjdlmnMqUoo9xMnKacGkZ3rtWrM1HlXg1Lbe6S8erTxvoXhsjdrx_nUVw--aKwMdoekjAlg6WAKHYu1N3rP5oTLYU-R8yTvAa7GqYZjixCWHEhu8vaafdjUZB98VuRpbVwiCTk_6MZG0CuF6hWmv4INQERzW5T0xcZiFbwSDxJrM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: تا آمریکا رفتارش را تصحیح نکند، تنگهٔ هرمز باز نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454992" target="_blank">📅 17:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454990">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8e551a9.mp4?token=VX-V9xPdLOCyAhbx2ot5F7r3TSwgt3vT2zzaaKkgUMOcWiar52gJ5PW6XajsUmLwkEvGNeTcSE8JtPLag1xkNeaOyTQIZ-9qwTvilLiSNMmDUIryua6xhJnZmuKc7MnXqZ70HvTjflY1aEBZfPXhMBzbO5FrJCpFhyz5ALtRTfYfkha1fVApKZ_kzAQlOtx2brm1Phe5B2yW-lJkQxB6VAJJ7jvYiIuVmgOUNHuIl9Evz9jITFN423fms9zh0LEmtZ1dv-F8W6qb_jn8QT-4nzQJbISvT-FX6wQpB9Y4yC67uPbrp2-m-iVyXKEIopR8EDuPgY_ANyhsDs97DNS92A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8e551a9.mp4?token=VX-V9xPdLOCyAhbx2ot5F7r3TSwgt3vT2zzaaKkgUMOcWiar52gJ5PW6XajsUmLwkEvGNeTcSE8JtPLag1xkNeaOyTQIZ-9qwTvilLiSNMmDUIryua6xhJnZmuKc7MnXqZ70HvTjflY1aEBZfPXhMBzbO5FrJCpFhyz5ALtRTfYfkha1fVApKZ_kzAQlOtx2brm1Phe5B2yW-lJkQxB6VAJJ7jvYiIuVmgOUNHuIl9Evz9jITFN423fms9zh0LEmtZ1dv-F8W6qb_jn8QT-4nzQJbISvT-FX6wQpB9Y4yC67uPbrp2-m-iVyXKEIopR8EDuPgY_ANyhsDs97DNS92A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از آمادگی رزمی مجاهدان یمنی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454990" target="_blank">📅 16:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454989">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/730c164f95.mp4?token=NhFGW4D2M6MdYJUQJ28MeSDSsSeITiLrmj4x57NsBgCcy98pkQTopBvuJEbJv42ONKNeJapuKUtkbpxDvdkiBYK44f9Sv5CYpbjpRyVcNLpyfxT_cCarcfIX7-YheyDN96S9VC4lVJzYxiBEGZPdt4MYpFWzKmFEnO5IHKv924ryL_FAlEGgeT69I-Zb2jLzXhh7dcVLWVdPZkgXh8zw5JmtOgJmaUILvEPNX0qRVKXHIjBitdPSzOXqagYAifVPt3zL9h051rThLhLR3AFrIp0itZG3ZPiV49Uo1hh9SAMmmSMKml7p6G8MeKrQ9Eg_lXkn1dA_iEYip2Zgfkfzr3u0PgDXVidhFeC3TdKPpBUyRVSQ3SZtawtTM0PX7ha_gZJPujvTkIJZ6L0vvRZ9TDuQJFK7G7uG5bu-0_jv7pMCozZR_DNBOZXZJB5rBqb2EaQdvxdCjrMDQHrWMYEhLQ9fZCK4Zm3uNKwz1OcyDanuG-tlyygD5e8NW8IYDE8iWsEipi-NMESAS91vjzt-prUXWauCUQ_TDL7Op1dSnI7fFml26U5U3K_fkMMe-ZAssLwugSTxQp4Vd1C1BoTaPqAIX-cTAJHxJfJ-vlb1LP5JsY8zGohs8ZoDBAtpsiFfWWy2ZSkBCiJ7D5VYMmIzQOMbQAkoLhZgLiXqTE-UywM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/730c164f95.mp4?token=NhFGW4D2M6MdYJUQJ28MeSDSsSeITiLrmj4x57NsBgCcy98pkQTopBvuJEbJv42ONKNeJapuKUtkbpxDvdkiBYK44f9Sv5CYpbjpRyVcNLpyfxT_cCarcfIX7-YheyDN96S9VC4lVJzYxiBEGZPdt4MYpFWzKmFEnO5IHKv924ryL_FAlEGgeT69I-Zb2jLzXhh7dcVLWVdPZkgXh8zw5JmtOgJmaUILvEPNX0qRVKXHIjBitdPSzOXqagYAifVPt3zL9h051rThLhLR3AFrIp0itZG3ZPiV49Uo1hh9SAMmmSMKml7p6G8MeKrQ9Eg_lXkn1dA_iEYip2Zgfkfzr3u0PgDXVidhFeC3TdKPpBUyRVSQ3SZtawtTM0PX7ha_gZJPujvTkIJZ6L0vvRZ9TDuQJFK7G7uG5bu-0_jv7pMCozZR_DNBOZXZJB5rBqb2EaQdvxdCjrMDQHrWMYEhLQ9fZCK4Zm3uNKwz1OcyDanuG-tlyygD5e8NW8IYDE8iWsEipi-NMESAS91vjzt-prUXWauCUQ_TDL7Op1dSnI7fFml26U5U3K_fkMMe-ZAssLwugSTxQp4Vd1C1BoTaPqAIX-cTAJHxJfJ-vlb1LP5JsY8zGohs8ZoDBAtpsiFfWWy2ZSkBCiJ7D5VYMmIzQOMbQAkoLhZgLiXqTE-UywM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرنوشت تجمعات شبانه بعد از ماه صفر چیست؟
🔹
قائم مقام سازمان تبلیغات: «ادعای تعطیلی تجمعات بعد از ماه صفر صحت ندارد.»
🔸
همه ساعت‌مان را با ولی‌فقیه تنظیم‌ کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454989" target="_blank">📅 16:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454988">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juB5ksZICtcnIl2APqLud5jnRR76rHKwcwG51to0ECcHPV6dNycX1qNcT_KrseNVgjzehXUd_jKysrleF0dCOo63TrWYZPZHHSC56Nu6ZNhs2Ifq699RQ9i8DNH0PjFke-vFuxpbmglQjQHpX5Sz9EZHXFtjGNE_c_pCvAOfWYZu029GGMW09ueRHfH6f7n-AYZ_73lMPRp8sb-unV0rKh9BVb8yLCWx5daFaE4O-sHCZazccSpZ9y8zFu8FQYRfDYJPaoIK1UVPBFrS-1StvZHImkcJu0wiW29KHtpnXgST6cf39v2QDxUSftvMw85jZ54oFexyayxL-hrkdFIjCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف بیش‌از ۱۱ هزار قرص متادون در اصفهان
🔹
معاونت درمان دانشگاه علوم پزشکی اصفهان: در جریان بازدید نظارتی از یک مرکز درمانی متخلف در شهرستان تیران، حدود ۱۱ هزار قرص متادون و ۹ بطریِ ۲۵۰ میلی‌لیتری شربت متادون و شربت اپیوم کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454988" target="_blank">📅 16:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454987">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsoolZ3RyCRFEGa1MQcHmICHoTPbQLeselALiDqy7UdqeBZdu53ybeheVo0F0aqcEeUlDNAN0JKODmYrBvcrG9eO4DwE5ZKAOjbgIerWgpsyTx5zpTTDCprJ4_65Xm-DzDnZJERKvB5gX7NPOqqIKmhexbitqxsedAbk8uqO7v5MzdxGw_edeQWra8mZkSgKp5KMzbRO9IW0VXf8JEKvUXwFs51Ovc9JHi7FgeXPDXM8-4d_W3k0hAG-LMXxEevpD0tpkqSSTxNdXpTW33RXmEwY1L9AyZrYuyV_GWGivryvXPDw-DnvaNKpRwqmi737ajfq5Mp0gzGmcFKwW3kDCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: رهبری هر تصمیمی بگیرد ما تا آخر ایستاده‌ایم
🔹
اینکه ما بجنگیم یا نه، بهتر از من و شما، فرماندهان جنگ می‌دانند. آنها قدرت خودشان را می‌دانند. رهبری تصمیم می‌گیرد و هر تصمیمی ایشان بگیرد، ما تا آخر ایستاده‌ایم.
🔹
تکلیف جنگ با دولت نیست؛ هم در قانون…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454987" target="_blank">📅 16:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454981">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Al8-5wqTYNqu7WI6iGXmP02X7KjnDdxvs59N4AxQC5IxnwcmWk2S1t6G8gQW32ql0dxRsHKjZ7EYkSy2UI0DMrPfG2lHKgo627aFjdZZRYlmTuGLaqN_PNX4WZ54KUtBPqnQJrr2lhFjo8hLS43rCBoBPhLxAWe6G4-xZIQDoNlYU1NrSYfyHCZdb-7vNMBf06raOX_w3vVnTw1jPT70LWIILWvEB6Ynr6OSmN1bDvibZ1vzU32KdcHHhzxzVYbZzTqX3WbFZOIvoh8dT7UEukeyRNLC8Lz96YLPO9Q9d_DNcb0xeuHv7G6QFVHjZJs5ySGFzzazx1NDPUyGypdZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n46ydVU4afVbLhen27cNmdgyDlZ-qv_o6Ip7TJy5OHo9Pz-1DJFYNnfZLWK2xeVfqaJMX4ms-DyRUiahGJuk3zqo-YMgfET3ITIaIKC6VOMbSULQsqwm0AS0aZZCVS2rthqQTb958D6PPDlo1wcWKjlqIt01vyrpCgLx-9cwoCUV3s5wsDfX8AshVmrkwIZcKRzJ1jbjfvJ-ok6ckWKqeY7F9SxNAjNGDvJmVt785f34N9ZCnGmcwHclNxBv4DT2W3j-VGRgKwfcSMepJefLuk3pcrri54jiQZM3x4YNkjdeCHyRxb6DH7dhwh4q72ysMKwOANCgmlkEQB6TVP98gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjbumdQ_870z637tPdR_YbgXWbRF4kOC-HscZX2J-mrNuVq_cF3QT_7Unu1_XgEXup2z22q9In-hOnbbO_qjqZ3KjXzfrRZmciVkW12UymnR4zCrOf9FPwLhmtgPj13iRBnWDhSRRalpRBg02H0JzTPLYi4RWQZHj6RPI3NbV2HO8V0Oe2V6-Bl1GAI_S9L3CEAS1-gLE2bv2TEmasJ6K92pBAjUEwt1yYtT84Up3g64EkoHkjmAzk2Ii2bCE3pM4eAKA-S0JLlNV0DHH6xmeeJcYppHUNgmEwd9WCjPo857FOG00sR7-NtbZjc6XYRcdz9Kk6hbhG6u-TWXi5_Peg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0vcuMnjyYdYvjyLjUjrJIohx77F4eZpY9C4m7HpPEMwf4Cr4-TKgR6y1WT8-L1u7Fsw6wkw478UqsnlweXK1xDngkCYYovVL8iQWrDuU74eUoXK1sYDW1S9x9McgWU04wpmEJDQST0hhcb9tupbwr-mOZk0g_1E4kOzhOFu_b_eABDqNnmSHO8latov3KI5Vna0-JPue6rmw5ehNdz7LhgMejGHI2WpwWP11Ct85ShajXarlLcfXH2UyCCJ25o4ggYaDA-dCJ240ZT-l9a8oWZolJ7N3NtESmRPHh32dtlLStWjHoLvW9DvaCdbyEnR4duOEkb0tzd-wsvnSM8kTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNdGK9xZl7Uw8HGRnoOfKBsB5Q1MjAFpNgVSz0_zYsbbOuFILlRIgt7lGYuNrY548nJ_3yfM7oYcSutEVwq4ShXkEkVY_JNnpOrXLGaoaQ_OHgMuVwmoiqs6OD1T79h7JFEkRnjB1n3SJkcEJYxjX_5KkV5oFUW7oFBuB228ZqF5zBXbykovGONf5fNx0gi5X6iNPwNX1QIekZ2srNbe8gK9MN3kB6l7TEwKb5dLzzTm3q0szP55sd0cbZSr79iwDw7vgKKaTI1gVhBleyWY6q-WqbmFSWqCkNCmLFPHCzZ88Y6vlba-JdB00GA-oUnUxYJJFkT6P1mUwCGWtBD5iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر آموزش‌وپرورش برای تبریک روز خبرنگار به خبرگزاری فارس آمد
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454981" target="_blank">📅 16:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454980">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
تصاویری از عرشۀ کشتی متخلف که توسط نیروی دریایی سپاه پاسداران متوقف شد
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454980" target="_blank">📅 16:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454979">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlknirmAdYYgK7wt2MVvChshznkbc_xH34YiWORvp0RTvZA_Sjn_T7-qB9puJ253dDz-sjOW-A-j-jZfyCAs44TDY2NmNRK5DwcM0P3bjB8m-HKfAINtKLLxJN7f0cDWIERRMnqpKFMFMrXtCnBc9HOs8kbseNQqqqzcp5eSWksvNz_zyf3Nd599OISDf_gZq17yeuRSpOR7Ek6XEmrVeXMeB2L4ZLohap6KVfWexa_11MXnlW7BkCjwS3-GlqcSiqd53BKDnX_dFaXDUie4roRMzmz3s99ZQpyg5kV3_bTEDT8SEVzNiqSyCYEVO1t5hdAE_asprXxJDKqrUPJavw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: تصمیم گرفتیم اینترنت باز شود
🔹
بعضی از دستگاه‌های امنیتی تهدیداتی را در خصوص بازگشت وضعیت اینترنت ملاحظه می‌کنند و همچنین با توجه به حملاتی که از این طریق به زیرساخت‌ها انجام می‌گیرد، نگرانی‌هایی دارند.
🔹
با وجود همۀ این موضوعات، ما تصمیم گرفتیم اینترنت…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454979" target="_blank">📅 16:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454978">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4933f2ce.mp4?token=MoAe63u3FTxfZac4u1bcjPlRSloCIE7Qz11k-aGVouOTALQLpa6XzaE3RNDIRlO8cyjI6eKJ6FRA4E_dZ7gaGAtugLXM97MIlT1ATrzPqzU3hbWeXbHYykyloqw4UAFaLSJGOKB_WXtEn8pKHsG_viUAN8lJNmanTJrJGDP6ljWljeDY9uE0eE1PNpJJX-3EVsg97BdcEKMG08LkSDL9pSD_qhqjp9ka_lErw3UFjOWwLxSgRs0PRwszAYfSvzqlwafQdb3l6seVEaxGSftv79GqnpjrHX_vgFt-Lp6m_J8U7XuABqtTnJs5yqCC98bugSEX-YbUw6LzHpC92yG51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4933f2ce.mp4?token=MoAe63u3FTxfZac4u1bcjPlRSloCIE7Qz11k-aGVouOTALQLpa6XzaE3RNDIRlO8cyjI6eKJ6FRA4E_dZ7gaGAtugLXM97MIlT1ATrzPqzU3hbWeXbHYykyloqw4UAFaLSJGOKB_WXtEn8pKHsG_viUAN8lJNmanTJrJGDP6ljWljeDY9uE0eE1PNpJJX-3EVsg97BdcEKMG08LkSDL9pSD_qhqjp9ka_lErw3UFjOWwLxSgRs0PRwszAYfSvzqlwafQdb3l6seVEaxGSftv79GqnpjrHX_vgFt-Lp6m_J8U7XuABqtTnJs5yqCC98bugSEX-YbUw6LzHpC92yG51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محاکمه علی‌ضیا و امیرحسین قیاسی در سریال آقای قاضی!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454978" target="_blank">📅 15:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454977">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff4245438.mp4?token=P4mOON8pczXdJFWBuy61iM3WbkCHyb8ZEQMXsNehzKp1EB34Ddm6-EwKSAz4Wi2mvZzXDlBni5Azla6PEAKYcf0ZMIqOw2Ivt5fsuIwvJmZxjM6rctood4aZ8ev7bPZzkRI9gYK8pVMaja1WxlJPgPxh1ES_XXkEydSQdXrSbJd-uiazjQXrWkFmapk0w1j59F26aTfMEaw_K7_f8xMXC5h9DNUObfdUSLtJPf110fkkP7BMRgNCikMevszuyYkBoewVu7tuco02cHjIlTP1jOmlSqZrcEbrUKhyROdseaNNVJW1kUaDuVecq-p0bxMd5cfqxfmbyh_0IfEQhxmKtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff4245438.mp4?token=P4mOON8pczXdJFWBuy61iM3WbkCHyb8ZEQMXsNehzKp1EB34Ddm6-EwKSAz4Wi2mvZzXDlBni5Azla6PEAKYcf0ZMIqOw2Ivt5fsuIwvJmZxjM6rctood4aZ8ev7bPZzkRI9gYK8pVMaja1WxlJPgPxh1ES_XXkEydSQdXrSbJd-uiazjQXrWkFmapk0w1j59F26aTfMEaw_K7_f8xMXC5h9DNUObfdUSLtJPf110fkkP7BMRgNCikMevszuyYkBoewVu7tuco02cHjIlTP1jOmlSqZrcEbrUKhyROdseaNNVJW1kUaDuVecq-p0bxMd5cfqxfmbyh_0IfEQhxmKtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله عاملی در برنامه سمت خدا: «اول مثل یزید را بشناسید، بعد به عزاداری سیدالشهدا(ع) بیایید»
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454977" target="_blank">📅 15:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454976">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faDCY-rC16be5xAs4rYpP7L0U3EmlKIRSnvT4rfr9joxUYt3qDsq6UxABf5K-LAKL50_5Q_nB-LzvCs5Hvd6zDC4cNl3ftANr7VSVwufeKeMSguVkWHO69s0bkMwBvUVeT-7GerYCz7S3VgK4Rf-KAyGqPTDpOX1hGzNzVEV3FjtM0PnGWPh_t-xF3DImjVlra2thI-1xIhc2_1E-3fXDBkBanBCaODR-QZsPTYAMsSqdSGBDwBK02sl__r2vKPS0lDkmkcgtC9lpRqLiRwMx1ElFT7tzn17BtUq7A_G8K1wJt13rXBfWWDbk_ijGIrsnff2Jaip4HCTUSXB4aq7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مهم‌ترین نگرانی‌ام معیشت مردم است
🔹
امروز مهم‌ترین دغدغه و نگرانی من معیشت مردم است و تمام تلاش خود را به‌کار گرفته‌ایم تا به هر شکلی که ممکن است، مسئله معیشت مردم را حل کنیم.
🔹
جلسۀ دولتی وجود ندارد که در آن با مدیران اقتصادی دربارۀ بحث معیشت مردم…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454976" target="_blank">📅 15:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454975">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84526b2bb9.mp4?token=rTLkYwhR2xeyaxUatdAJxckvPr4dAQLCxOBV1X91on81em3TYmx9fqxqKuSq7LNuRuIS47ajVdBaW66L8M2scHsaiBn39nCo6fiHSV6yAO6s6AVV2lG9WZfjvdzYqH02oiE9VqMxouGGgLJgyjdyBjRD9QmfRpLwxFYS3PMW2TmwQpXT8KMJdmdTRJ9KCNhelyuC54D7i29PpC5ycZAjR4rtjk4-b2PZSypVnHyUubeC_50SV0UPvRlWzyRQZm4iSiopfN7PBA4vj8akcCxpabQp8VBPVLcjnsMhZSoY4aBST4wWg4GE28UIbN1Bw8863RBeq-hDrkMWY15rTF2aaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84526b2bb9.mp4?token=rTLkYwhR2xeyaxUatdAJxckvPr4dAQLCxOBV1X91on81em3TYmx9fqxqKuSq7LNuRuIS47ajVdBaW66L8M2scHsaiBn39nCo6fiHSV6yAO6s6AVV2lG9WZfjvdzYqH02oiE9VqMxouGGgLJgyjdyBjRD9QmfRpLwxFYS3PMW2TmwQpXT8KMJdmdTRJ9KCNhelyuC54D7i29PpC5ycZAjR4rtjk4-b2PZSypVnHyUubeC_50SV0UPvRlWzyRQZm4iSiopfN7PBA4vj8akcCxpabQp8VBPVLcjnsMhZSoY4aBST4wWg4GE28UIbN1Bw8863RBeq-hDrkMWY15rTF2aaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت قوی‌ترین مرد ایران از حادثۀ میناب
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454975" target="_blank">📅 15:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454974">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX9NL1EzKUr05d38iO9VIon1wVURpJXTX8JbFzC4NOFnGcFsA96noMii89YDUXT-EhKZjEzhuHBIFwa8S1rpTGM8UwXISv5rk5ETrFgAVOjOJswzPgmDgnq7qf6o-O5e-jf9JHcuEd2XHrzV558ZCI2tQ47zsevM1mjX5yDXS_qulyROjPGJhgxcBaynvnPpZFggGlMxCo9EwypujMw3j7WBfH_1i1-PEfPsqIZav1hVirWN3YQritBvTZBZRC0WUVgI2yasJFB_vG9PogbV5LOD-B74eDUBZQlEYcsiF9uGvfrEJdfXY8zm-sfCSxvi13wbABNW-ybcyZ4GSMloCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان: در حال حاضر کمک خبرنگاران برای ایجاد وحدت و انسجام بسیار مهم است  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454974" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454973">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4110a6cae.mp4?token=bCjSmfx7TmBGsWM48T0DRfWphn80igCi2ED6Pl6aItGzvBLd4Jy6qKE8cJurobloodDb3qmnVy0v0F9h1K5fbjlqaSiy1HGsvi4Vdt6lVIXqflKezb1awViInbfXqpJ5F0409PuiaJucu67eqGjN_L5BDyeqs2-UQPBpZCSHJBk06Xj2A8yJ5J69RdX02r4lsSUDNXop-qHb8w9-RPST5PA7WR82qxXLY4FzsHQP3tprzgrIMMukYENXPblxyQyoQaFMhpkHvtpt-DhIwsaDi0jbwQo3k8dxiJzdBDdQIVrLQkqEA3S8WtMeWoCFzFV8vRFBCzpm5-BPg_ClO81RDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4110a6cae.mp4?token=bCjSmfx7TmBGsWM48T0DRfWphn80igCi2ED6Pl6aItGzvBLd4Jy6qKE8cJurobloodDb3qmnVy0v0F9h1K5fbjlqaSiy1HGsvi4Vdt6lVIXqflKezb1awViInbfXqpJ5F0409PuiaJucu67eqGjN_L5BDyeqs2-UQPBpZCSHJBk06Xj2A8yJ5J69RdX02r4lsSUDNXop-qHb8w9-RPST5PA7WR82qxXLY4FzsHQP3tprzgrIMMukYENXPblxyQyoQaFMhpkHvtpt-DhIwsaDi0jbwQo3k8dxiJzdBDdQIVrLQkqEA3S8WtMeWoCFzFV8vRFBCzpm5-BPg_ClO81RDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران، مهمان تابستانی ارتفاعات دماوند شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454973" target="_blank">📅 15:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454972">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۹ مصدوم به‌دلیل سقوط آسانسور در میدان آرژانتین
🔹
سخنگوی اورژانس تهران: درپی سقوط آسانسور در خیابان احمد قصیر میدان آرژانتین، ۹ نفر مصدوم شدند؛ خبر تکمیلی متعاقباً اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454972" target="_blank">📅 15:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454971">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqvMtRS24Rubu2X8fAIK_2gBL0TtEBao1irZcX7duAmu9c-Oyw561SbVceYvAZlsenk5RPlAv2RosnZ0sZs_7HGo3EyvSo3U6e_u1tfm32C98qYXa39NTX_yt3mfNlTzLotUVV3SBPazFRrPoYFybeXn4xewXO35_0c-2JEICVoEg1PG1EwwEpbzXMZKWSErC-QeOPLQxsvqt61PGl_FtBJg4uEKLxr_cezEpdhE-uXywGBUsYqlOSy4SC-yY8MdAGLPlja12HrXueS-M9suyUMu8qDbKiyXQPyXFVTS_9QIjy1Ud1ZeAojaeODyvx3o-PZSh8kNY9vQR8KMS3lnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل میزبانی استقلال و پرسپولیس در لیگ برتر مشخص شد
🔹
دیدارهای استقلال و پرسپولیس در فصل جدید لیگ برتر در ورزشگاه شهر قدس انجام خواهند شد؛ بدین ترتیب به احتمال فراوان این دیدارها با حضور تماشاگران انجام می‌شوند.
🔸
دیدارهای لیگ برتر فصل آینده از جمعه ۲۳ مرداد آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454971" target="_blank">📅 15:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454970">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
رسانه‌های صهیونیستی از زخمی‌شدن یک نظامی ارتش اشغالگر در یک «حادثهٔ عملیاتی» در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454970" target="_blank">📅 15:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454969">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b0e75560.mp4?token=vnQoHAGRkFQ6c6nsjhyElnxNXf-drgZAt68rBK5WWR1mopjkm-0i0TZdpuZaSVZIKV1CTKwPL0F2dBnMCgkXycmWYRGuO9521GetkA9v1EndY0fS7-HYqf_7My3gTBY-CaVzJjS7xgGpqT-Hul2e_nJhLSgG8Yz_exHctWkWXsny2Q7WphDJ3WBYqu7OHl-OFYcjTapdLn0kCEcx6ZlpFsHiISCPzdyTIS0QpAzaJucLhHdnAvGZgcpGRr7IQYmX0nsE9oTFjnLOMtk9gaT-8GozGlFmItjJHcX-5ZUE77iNWUF4pLjNqL-RrBAhvc-xpu-au4noy1qw-jax3yn_Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b0e75560.mp4?token=vnQoHAGRkFQ6c6nsjhyElnxNXf-drgZAt68rBK5WWR1mopjkm-0i0TZdpuZaSVZIKV1CTKwPL0F2dBnMCgkXycmWYRGuO9521GetkA9v1EndY0fS7-HYqf_7My3gTBY-CaVzJjS7xgGpqT-Hul2e_nJhLSgG8Yz_exHctWkWXsny2Q7WphDJ3WBYqu7OHl-OFYcjTapdLn0kCEcx6ZlpFsHiISCPzdyTIS0QpAzaJucLhHdnAvGZgcpGRr7IQYmX0nsE9oTFjnLOMtk9gaT-8GozGlFmItjJHcX-5ZUE77iNWUF4pLjNqL-RrBAhvc-xpu-au4noy1qw-jax3yn_Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر صنوف و تولیدکنندگان همکاری نمی‌‌کردند وضع خیلی بدتر از این می‌شد  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454969" target="_blank">📅 14:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454968">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665efbb507.mp4?token=KO8CkLM78EE5X5cVlwM-aZvh3h8PrIZ0QP8lG7lx59dAtyUDnHabLJiogHrsgjqOuRpyksS5G8J7oToza2MK-qNc1PRupXZbgytJ-no532qLxdRe846JP7fhbfqQadxg7O744Jr48jr4bUd4VQSoDb4lkx-YcvqqKaag7mmJOMxNeqLE4kfW2CFZzYWUddFDnRP-FZVQry_REFb_NExzNa36oowytSTLZFK3aOSIAT24nEp9dyesjr_A-m8kZFvQIWBku5RF7PslkjIvuuDbKRFd5YwXEpWOlCK-sOINNee9vko-j_xXmhKpJLtnnawjRoSEv9ISmrL8U3EDxZaEaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665efbb507.mp4?token=KO8CkLM78EE5X5cVlwM-aZvh3h8PrIZ0QP8lG7lx59dAtyUDnHabLJiogHrsgjqOuRpyksS5G8J7oToza2MK-qNc1PRupXZbgytJ-no532qLxdRe846JP7fhbfqQadxg7O744Jr48jr4bUd4VQSoDb4lkx-YcvqqKaag7mmJOMxNeqLE4kfW2CFZzYWUddFDnRP-FZVQry_REFb_NExzNa36oowytSTLZFK3aOSIAT24nEp9dyesjr_A-m8kZFvQIWBku5RF7PslkjIvuuDbKRFd5YwXEpWOlCK-sOINNee9vko-j_xXmhKpJLtnnawjRoSEv9ISmrL8U3EDxZaEaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا استعمارگر و قاتل است
🔹
آمریکا نمی‌خواهد جمهوری اسلامی باشد ولی گفت‌وگوها او را وادار به همراهی کرد؛ چرا دستاوردها را خراب می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454968" target="_blank">📅 14:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454967">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c6712df5d.mp4?token=F2Z2T5spjtIb4f4wJ4FRiPpvTnLwe-B2FRVpbiDfkZylaFM9sCZGsruycbWP6ZtrN4U6NhcNEjy-N1EDOgwfDZtMsx2wDh4RkKZ2h2EY-LFvJm3I6iMnr_Aiju8gFNmkxQCMa_3wDVYIhz5BxJjtqZqBIa9Qs31qFkp9gYVwAQHti-VeSBQWGpIE8Fd3zRC0GjA8goEIemPtqGuR1KlPbUrM3qdij5qTDKVNeH8VYOHDDMDnAvX4EQGHvDayyXWLzntYpODcZe0CZfraU7clZHmw3a9xarnNC2bV74wNmrXmdZhgPIJSEPzYdRePZgpqLQN1LCT97K_oerP9TClTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c6712df5d.mp4?token=F2Z2T5spjtIb4f4wJ4FRiPpvTnLwe-B2FRVpbiDfkZylaFM9sCZGsruycbWP6ZtrN4U6NhcNEjy-N1EDOgwfDZtMsx2wDh4RkKZ2h2EY-LFvJm3I6iMnr_Aiju8gFNmkxQCMa_3wDVYIhz5BxJjtqZqBIa9Qs31qFkp9gYVwAQHti-VeSBQWGpIE8Fd3zRC0GjA8goEIemPtqGuR1KlPbUrM3qdij5qTDKVNeH8VYOHDDMDnAvX4EQGHvDayyXWLzntYpODcZe0CZfraU7clZHmw3a9xarnNC2bV74wNmrXmdZhgPIJSEPzYdRePZgpqLQN1LCT97K_oerP9TClTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا استعمارگر و قاتل است
🔹
آمریکا نمی‌خواهد جمهوری اسلامی باشد ولی گفت‌وگوها او را وادار به همراهی کرد؛ چرا دستاوردها را خراب می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454967" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454966">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a509aa35f5.mp4?token=fBnNT2c1K88iPPOLRHHnC17hYp6eaD60Y7rmNHpTNh7YY5EGB1za33deXfNxG_qIDmDMvSXn5JwBWdV-UTqOjluYoM_sn3daaZMJ6E9f9r_1kM3-uvA5v0tNaLjDnqUp-If9-OSypO4B2qhjN78QkgoZnVAo2-YCHuJMnlXXmffZyegLxToDzYsyz-gNr6HKNzd9U2jP2z3RO9F18RzBSiHxTYjKb25jyIedifmol4v01rWw8NHNBY-p4s1T4mLjiXWdFHb81RqIbH6iuRDjjlNrZjzSTtkMfuN8jrEBAcl_ifSISr8TNmSUSagiovRfUozIsGbQhRK20GBJerVhLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a509aa35f5.mp4?token=fBnNT2c1K88iPPOLRHHnC17hYp6eaD60Y7rmNHpTNh7YY5EGB1za33deXfNxG_qIDmDMvSXn5JwBWdV-UTqOjluYoM_sn3daaZMJ6E9f9r_1kM3-uvA5v0tNaLjDnqUp-If9-OSypO4B2qhjN78QkgoZnVAo2-YCHuJMnlXXmffZyegLxToDzYsyz-gNr6HKNzd9U2jP2z3RO9F18RzBSiHxTYjKb25jyIedifmol4v01rWw8NHNBY-p4s1T4mLjiXWdFHb81RqIbH6iuRDjjlNrZjzSTtkMfuN8jrEBAcl_ifSISr8TNmSUSagiovRfUozIsGbQhRK20GBJerVhLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما مهمان خبرگزاری فارس
شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454966" target="_blank">📅 14:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454965">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
سخنگوی سپاه: بازگشایی تنگۀ هرمز منوط به پذیرش شروط ایران از سوی آمریکاست و ارتباطی به مذاکرات ایران و عمان ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454965" target="_blank">📅 14:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454964">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lteziOLuAOV6lQbYjkFCADdYEHL86Gnl9wZNIimBtb70xTmj_ph2EuIMJ_M6pO5yh-jf8G-AM7bDSBosXJIcm25PEEreeGsVvOdniSxgzCTHyUsc1szylvJi8qBXd114LkySg_QSaJU9woQma6NbhJxOf5hJKRUI2LCroNfLjQcD-kR27d5lbGoA-hZjmS_1D3oqT72gkFIw2p75_tGysPe5fC-e2nfLL1sSTdNlxqbwbwPQhAWzdmYFYVe1n7VbMueekO_UfiMn-LmhWZmCLBw8ZTOyB4HyeMLSMKulBILwZCmAz05kFhd7CdJUPbabs24uZ0YxngTvx3Jn2Paqdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه تختی هم مثل آزادی شخم خورد
🔹
با اعلام مدیرکل ورزش‌وجوانان استان تهران، ورزشگاه تختی به‌دلیل کاشت چمن تا حدود یک سال آینده آمادۀ میزبانی از مسابقات فوتبال نخواهد بود.
🔸
سال ۱۴۰۴ چند بازی استقلال و پرسپولیس در این ورزشگاه انجام شد که اعتراض کادر فنی…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454964" target="_blank">📅 14:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454963">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a1c18c4c.mp4?token=rN_4y1hUJ6QdJLup2sLj3pSUjcvN36U0Wn9vs7fdza_o0qKzf8prkmgX3L5TBz8LHd9ggRZR6_O6Fbk2aoCm77KtXqtDJZ6g9njC0fO8hNRdI2x3nY5OlDuuTjZ2Ys3anstLyMUuArWaKUau0qZR0Gf53bexpIOhJIXhTeZyYaJGbxlk3X3nlGvLADbKY50CmZHRMkckw6bi_Eb1860RcoA1z_CFWwanYEeCrWqYTe7D_jcec3JiCq3DC1SrfGVSIfrZD36C66s2mnHsWQ1NchtleKJcVWv_YODr6gurPmC64suy2v-77nLkqGONNTcLs_QWdg8leQbVkTzRro9JhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a1c18c4c.mp4?token=rN_4y1hUJ6QdJLup2sLj3pSUjcvN36U0Wn9vs7fdza_o0qKzf8prkmgX3L5TBz8LHd9ggRZR6_O6Fbk2aoCm77KtXqtDJZ6g9njC0fO8hNRdI2x3nY5OlDuuTjZ2Ys3anstLyMUuArWaKUau0qZR0Gf53bexpIOhJIXhTeZyYaJGbxlk3X3nlGvLADbKY50CmZHRMkckw6bi_Eb1860RcoA1z_CFWwanYEeCrWqYTe7D_jcec3JiCq3DC1SrfGVSIfrZD36C66s2mnHsWQ1NchtleKJcVWv_YODr6gurPmC64suy2v-77nLkqGONNTcLs_QWdg8leQbVkTzRro9JhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس اوراسیا: پیامدهای کنوانسیون دریای کاسپین از واگذاری بحرین هم زیان‌بارتر است
🔹
برهان حشمتی: در کنوانسیون رژیم حقوقی دریای کاسپین، فرمول ۱۵ مایل آب‌های سرزمینی و ۱۰ مایل منطقۀ انحصاری ماهیگیری پیش‌بینی شده؛ یعنی در مجموع ۲۵ مایل. این محدوده به‌هیچ‌عنوان…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454963" target="_blank">📅 14:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454962">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3atk1agjFni8O3YcZ3DraXVS7YZCEHLQDcmMPaqzEpkvsT5hn36cWUTu8yksx1kuHJHfM-i7hFx0Y6gMOdAcXYLmScVdJzfz9fDik8GaSiGXJsXEAsPQ70OxBp610dk_ylBEyu9IkIYeVcTs2JO5gxVMfwoDJtQMvMncjjeLNcFzIC4E1Mn6pDBMIpXBJvvaIc0fw2pbKfyVTl77_Asi4ZciQOOh4OuwSMZfkwXNTjxpG7MvgRYPGFcjHpu9r2sFmiNC5-xEOhperO52lrTZDhgZhTO1khyh1M6qdAqs1B5XNCPhLukk8lxRK8T6RnaqYGp2vSJE_TMy4eAGMU26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه مسی، پدر لیونل مسی درگذشت
.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454962" target="_blank">📅 14:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454961">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZo8tBPEk6Afb67OtMcf21CqPh7aRE6a7FPzX0i9KWsmG3ncRkOZ1zIdbtZ8MbaH4DYHF4OBtYVLU__nvXzUFs7RTGR1TCJuPv8QxisSw26T4KMj1RmjrFhk-z8yRN_zFbPTJLTHdKM4qaX7SVFJoEKyZDRgbQNwnyXc2kpRcQm4zYvcxCySiMjzBK9h_sPB-fhLwXOtcCDdbOSVRk8pkyOAo5cjjyOX9S5bgwFya973-MzI0ZHobuUm2i7VL53BUf1N4qGL5uSlR6uSHO2gUz92Rmj8pn4NeM8leVANJccKgbOvTmloXGbovB0vIugvDIUoVQq6v8SOesYp5idGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمله به کشتی اماراتی در تنگۀ هرمز
🔹
خبرگزاری امارات گزارش داد امروز یک کشتی متعلق به شرکت «ادنوک» هنگام عبور از تنگۀ هرمز با یک موشک هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454961" target="_blank">📅 14:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454960">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163c0107e.mp4?token=MZq-ohUxOX6Z-YsSP3g-DFUE86Y4RJASdGqIode_h_OmUdFtl8hm1dwNojSOfyxbFhGL_OZ9H5JFLreZAmpl8z9GUTwpg3OgM3gigQsv2sAJ0li5kecdjEV_tFx58VXO3XSiVd-TzCshCjKoDnLWEhPFVP3_Zil-zAnoMvxL32lFIFGosf08JAvAMj4WEUH6SrnFI0ayKESRL9dk8CgCjGo_hO28oRaVFeP3bg3E_Oao0quJMCJ04PS8Ahl3sc6GmqsxkwyDJhmTHqbXVl--bW8Zp97XHazQAIM-SLOe-DuT9QyvlTiqB_YkwWO7UYfA3U9NdxJhuZH9nk2dFSEnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163c0107e.mp4?token=MZq-ohUxOX6Z-YsSP3g-DFUE86Y4RJASdGqIode_h_OmUdFtl8hm1dwNojSOfyxbFhGL_OZ9H5JFLreZAmpl8z9GUTwpg3OgM3gigQsv2sAJ0li5kecdjEV_tFx58VXO3XSiVd-TzCshCjKoDnLWEhPFVP3_Zil-zAnoMvxL32lFIFGosf08JAvAMj4WEUH6SrnFI0ayKESRL9dk8CgCjGo_hO28oRaVFeP3bg3E_Oao0quJMCJ04PS8Ahl3sc6GmqsxkwyDJhmTHqbXVl--bW8Zp97XHazQAIM-SLOe-DuT9QyvlTiqB_YkwWO7UYfA3U9NdxJhuZH9nk2dFSEnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: بازگشایی تنگۀ هرمز منوط به پذیرش شروط ایران از سوی آمریکاست و ارتباطی به مذاکرات ایران و عمان ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454960" target="_blank">📅 13:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454959">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMDWA6UTe5novEH4omROL4jdGuDnpmo1-Mxfg0qT9LJ860Fmt8eGS7fQH3f4c1CZhHccS9kqUNARiYh_Eas4dOyOy_ha__OKwpC14X1ACB9XhgL3KZ1kdnHP9LzZwGmggF5IjvrgBIEfBZfaFjRJE1RFcYya0bOjCETvDPyu218iupq-WLFOHo75KEEYuj10LK8oOeNAjFFprVn6kMQ8ttMiAHZnD0PvoYp4rOXEbOkUAOu3HUVJkTkmV7tzkx6r-ZH760L9i0UTpfOXVeaU00gJ0NKhc2BN0997sflpRiZIs036xvblkR8xSjDwANSltHaOL-sqobtzK1GuxE5fkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قتل یک مداح پس از ۱۵ روز بی‌خبری از او
🔹
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شد. خانوادۀ او آن زمان در کربلا بودند و پس از بازگشت به کشور پیگیرش شدند.
🔹
مسئول هیئتی که رجب‌زاده در آن مداحی می‌کرد در گفت‌گو با فارس: ۲ روز پیش ویدیویی از پیکر آسیب‌دیدۀ حمیدرضا در شبکه‌های معاند و سلطنت‌طلب پخش شد.
🔹
جزئیات دقیق دربارۀ نحوۀ وقوع حادثه، زمان و محل جنایت و همچنین هویت عامل یا عاملان جنایت، نیازمند اعلام‌نظر مراجع انتظامی و قضایی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/454959" target="_blank">📅 13:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454958">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1369d7fdb9.mp4?token=Vybu4qBMyIAzji8zJnFx__cH85ArWH8kGKRdK8IMWs1YoC_CENZDTQMNZ6ECrC-aasWueifbuafmMNVMc4iMWcmLJUXz29wzif2CV97Y-SuzzeDxcJpNRPS4BdLUfazKfD46VLj5136MIMepeDne3ehclClBugfwzyscmzKF3ef4D5ww0P7cR9hWqqjiPf4rSNfEGel5qYc8W2r9DwORm3T2szbQEF0yl-WChEpYUNXEtm8eoO6Dbyj9EXTPT05PGr_7KDH1ocyvJ1k78LUIyM5hBMeCt6kyh00YPrQtLP9RIVstzkJLTQeUHpgjNe2BpZ7_Hb8jzN_o-lfGmA_SlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1369d7fdb9.mp4?token=Vybu4qBMyIAzji8zJnFx__cH85ArWH8kGKRdK8IMWs1YoC_CENZDTQMNZ6ECrC-aasWueifbuafmMNVMc4iMWcmLJUXz29wzif2CV97Y-SuzzeDxcJpNRPS4BdLUfazKfD46VLj5136MIMepeDne3ehclClBugfwzyscmzKF3ef4D5ww0P7cR9hWqqjiPf4rSNfEGel5qYc8W2r9DwORm3T2szbQEF0yl-WChEpYUNXEtm8eoO6Dbyj9EXTPT05PGr_7KDH1ocyvJ1k78LUIyM5hBMeCt6kyh00YPrQtLP9RIVstzkJLTQeUHpgjNe2BpZ7_Hb8jzN_o-lfGmA_SlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلوغی مرزها بلای جان واردکنندگان شده است
🔹
با تمدید مهلت تعهدات بازرگانان تا پایان شهریور، بازرگانان فرصت دارند تا حدود یک ماه و نیم دیگر کالا وارد کنند و جریمه نشوند.
🔹
با این حال گزارش‌های رسیده از گمرک‌های مرزی با پاکستان از شلوغی و بسته‌شدن مسیرها ورودی و خروجی حکایت دارد.
🔹
بازرگانان می‌گویند با حجم بالای ورود کالا به مسیرهای جایگزین بنادر چنوبی از جمله مسیرهای زمینی و بنادر جنوب شرقی، ممکن است با این مهلت هم نتوانند کالایشان را ترخیص کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454958" target="_blank">📅 13:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454957">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8dD6ChNv48FAwjJ1RW4MmmU3nIlYzRWth-0_IDURmxDaQ7xnhy6RI_uoXh28_RidaFONOTiO45BTeW0z2iuLHqzM_X1kIYZayxTN73LNCn_qmG0QiADX_EtR5OeCJ_eC4VbmyHSQMsecnSCoCOgoiUN8bwQfkEijkBOnQ-yYX5AuhQ8fWMHJeonwbe7A2F_GEdBtWCaShuLsPZ_dG-r_WpmVtGixLOWBYqmj9CLJs0-SYBNiy7T-oiDxsbTRy0Pam-AxubwH8cs0ItDipUh4da4sBZtCje8cuL_DVM-kDRzNRjAHW1tiOaC0iEQYAbSqANt2kyBqqv-lkvgt2PHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل ترامپ در پرونده حق‌السکوت، وزیر دادگستری شد
🔹
با گذشت چهار ماه و چهار روز از برکناری وزیر دادگستری آمریکا توسط دونالد ترامپ، سنا سرانجام به جایگزین پیشنهادی رئیس‌جمهور رای داد.
🔹
مجلس سنای آمریکا سنا با ۵۰ رای مثبت و ۴۹ رای منفی، تاد بلانش را به عنوان وزیر دادگستری و دادستان کل تائید کرد.
🔸
بلانش سابقه فعالیت به عنوان وکیل ترامپ و فعالیت در پرونده پرداخت حق‌السکوت ترامپ به بازیگر فیلم‌های مستهجن «استورمی دنیلز»، را دارد.
🔹
ترامپ در اوج کارزار انتخابات ۲۰۱۶ از طریق مایکل کوهن وزیر شخصی وقت خودش به دنیلز حق‌السکوت داد تا بر روابط نامشروع خود سرپوش بگذارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454957" target="_blank">📅 13:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454956">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB_uTB-CdNMpe3RRyF0mt__bDzXMEcTH-yt2RoXF1A3-Q1lBfsWEC--aVpbo3ZH8FbwsNd-hmny3LEve9iAvsPS6FLFLnUVfgt9kBZEU2XadPUVw9nqI4VfOSoZQUe9jCZPoXLt4etRLUHmzbg-6Y9p3knV1LGkoo4AmW5AZEZ4ulR5Wv6SLTzViPQP5DGju25h-3fcQ9jptZwHy4KychX_9_N38O9F0_WVQKLBBJ3Hif9clPKo91PnyW2C39bfWefMloTuG-ZWqXXFe5abNpvcTd_Cp_H7RvYGcvKs6dV7Dv1vGLj-XauQyBs9CImvLPy6pZc9IXwuXtv3sCDUFRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ و نیم میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با با ثبت رکورد تاریخی جدید از ۵ میلیون و ۵۰۰ هزار واحد عبور کرد. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454956" target="_blank">📅 12:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454955">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9CM5Y4clqKQO_FxnJMSQqIsrweUOe0gb4iLo8POJF3xMtD8JTZRQFW7uGyUlYQpwv74efMv0yy_tT2Tednc2DBg3e3wtjYHamIP2ZBFjFewIWpmpWi86AKYYgDCIKPdGimetQJpDGh5bh7iP9M_bivyTsSZctbCDWYhLnCAYSMAcghYKx97wb-60PObaYJyTi4HMERojwrHzQ8UHb86eEu7FQZZn0_JIj9K93mORQuNKNPPWy_ICgv2hOLhmc4vOSJar6cyxvRLb7r15nNvANxvFgN2uCIlMcoxqsNOITkWecG548OQLidU3yokYFuid2ookQUHA3qzh_ZgPpHWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: یک نفتکش سعودی را در منطقهٔ ینبع هدف قرار دادیم
🔹
یحیی سریع: در راستای اجرای ممنوعیت تردد دریایی برای دشمن سعودی، نیروهای مسلح یمن با لطف خداوند موفق به هدف‌قرار‌دادن نفتکش سعودی «وفا» شمال دریای سرخ، مقابل منطقه «ینبع» شدند.
🔹
این…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454955" target="_blank">📅 12:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454954">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok2X2eHBnsIR8-9h-MEZwBFVmviPLey3IoBKXkBZEJyAlGXNRRVZDI2nCb1Fsr4sTgDDoLsqJBhMR2X76T2mfSy7yNQcWLgBzBSWD-KtP0uAm6Xo6WF66WFK-MSkza_NgmXUBsXqions3cqAToE11YBh2rMwtnfNjujdZYE1p0U1tmieneIucRDkRjoOZclWOt9maJMYAASbJpSiWQhpkpFlGU2E3liemDV1v9wePq1XvNRjRBcjYq1xFhj9wXU8DTAHRZ4EQTto4w3ibsMOZHQo7ntYNxOCHXGjnEkFXpCZm0dES02kiSTrD1p5GpdYhRcAfvxNVq9K1XwIlBQpIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی، مشاور رهبر انقلاب: نیروهای خارجی باید منطقه را ترک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454954" target="_blank">📅 12:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454953">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c3874c8b2.mp4?token=ZRMncVMW7-J9sT4z-GrSg89BmBjfnFkuFJcAQOCjeAdBsXMRKEeMGFUaYZTpFIFXYmxva0kog83tG6bMLqkiWvGZd6ERX7NLZjHE3e8nwIMML-bh8LuRNrLog3lXxDtmnQ_VDdPK0LSpzFGSNj_N3ctXQ-vo4F9e2TF2hboER_aXgW_teWDmFfGJKIV_SU8l8Fkg9MXiNWRWfFKK6t6kXvWBqv_upoOdgjn2jq940Fh7MRB7OAHs7b_ygedpQV2cX3lvffELcYyHKORV9uM_mbHDC-mZLZ7fbAO4eU0lFr2X-aiGU_1qeDG1gTMosu8o1bYhDYsHqUDuR7Kreo0S0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c3874c8b2.mp4?token=ZRMncVMW7-J9sT4z-GrSg89BmBjfnFkuFJcAQOCjeAdBsXMRKEeMGFUaYZTpFIFXYmxva0kog83tG6bMLqkiWvGZd6ERX7NLZjHE3e8nwIMML-bh8LuRNrLog3lXxDtmnQ_VDdPK0LSpzFGSNj_N3ctXQ-vo4F9e2TF2hboER_aXgW_teWDmFfGJKIV_SU8l8Fkg9MXiNWRWfFKK6t6kXvWBqv_upoOdgjn2jq940Fh7MRB7OAHs7b_ygedpQV2cX3lvffELcYyHKORV9uM_mbHDC-mZLZ7fbAO4eU0lFr2X-aiGU_1qeDG1gTMosu8o1bYhDYsHqUDuR7Kreo0S0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ معنادار هوافضای سپاه به تهدیدات آمریکایی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454953" target="_blank">📅 11:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454952">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odBEYGn0tdmdCXqu1fb5ER5W16PMa47tIJ7q6JBj5O2ToiuzyaFxiw0htfSAOhg5-SuTcrFW3U2kkrxxgEy4pNqpAd02fZEpBMsJrCzv8XO4Inim8T4sIMuxOHNApwrTiCxRDGVq0sTtfEdF-oHXGVT8i5JhRaho_-Bik_ZAV5y4CFX2VSp_heV-z9gAQyo9TGxAklZImjBdtbihWNdkp3BdabgJ4KNSSU-JrDB4-1NwV_HBJPtL-R5e4ejB3AZF7EczSNQD53lUoJxNfDpCQdtN3KgwWRM8lXsyPiYK4-7qOfb0g5kYV62JrVfapjnkGspZp-YH-GIF5UzR25lZug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید حوالهٔ ارز در مرکز مبادلهٔ ایران اعلام شد
🔹
دلار: ۱۵۴ هزار و ۴۵۱ تومان
🔹
یورو: ۱۷۸ هزار و ۵۴۲ تومان
🔹
درهم امارات: ۴۲ هزار و ۵۶ تومان
🔹
یوان چین: ۲۲,۸۸۹ تومان
🔹
روبل روسیه: ۱,۸۷۹ تومان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454952" target="_blank">📅 11:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454951">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad9d0a8d1.mp4?token=cU6qf0_uTsNpnLNiezcdhZ-nTPHUFRvZzLaZpGbn2dwq2n3MiBgEUMkU2LmhG3Ce0i5dodMgwhKjOVRAbyv5T0OAHc8T5KrZglg6P4wTcPGIPNmzebBBWUylUJgZMrlz5gsp-NimnTdkwJ9hYZ2z1mp-z0nC8MRn5zxAC3K0SShOJ9Zqr2Ni9O2p8wgETMryGV5hBc9b-uFZXfbgVl29ZCH8LaGFa-5nWNkUGt-14aotXTg7Z8414yx488fMhGjwEUH98xQsF3TPKxYk49pseZAXeFP8MZUtsjeHMUFZJDFOhKBgF3rfwBRypqtr37MlTJTcC91SwvEYVA3k3kmyiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad9d0a8d1.mp4?token=cU6qf0_uTsNpnLNiezcdhZ-nTPHUFRvZzLaZpGbn2dwq2n3MiBgEUMkU2LmhG3Ce0i5dodMgwhKjOVRAbyv5T0OAHc8T5KrZglg6P4wTcPGIPNmzebBBWUylUJgZMrlz5gsp-NimnTdkwJ9hYZ2z1mp-z0nC8MRn5zxAC3K0SShOJ9Zqr2Ni9O2p8wgETMryGV5hBc9b-uFZXfbgVl29ZCH8LaGFa-5nWNkUGt-14aotXTg7Z8414yx488fMhGjwEUH98xQsF3TPKxYk49pseZAXeFP8MZUtsjeHMUFZJDFOhKBgF3rfwBRypqtr37MlTJTcC91SwvEYVA3k3kmyiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر رهبر انقلاب: مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور مطرح کرده از اساس کذب و خلاف واقع است
🔹
متن اطلاعیهٔ روابط‌عمومی دفتر رهبر انقلاب: بسم‌الله الرحمن الرحیم
🔹
با گرامی‌داشت اربعین حسینی…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454951" target="_blank">📅 11:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454950">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxRWdzRLiLOofHrBzX0B42bYH8IyX08yVmbb2OZ19RoC3FCYOmAdls_OdDnMMihxy3Fx3-lJA0wY5_nIx6DxZVjorRCeQZQlBA0UvE7EVZp9uJkKsv-0f-fM1E64kZrkGW2Wniu9j3j99nBNsx_x8KvLJkQ8giunZY7OriEYVprcA4QjZiO-tprzWWGXxnvvjOmgz9NAYk8JrLMX0LfATkropAkla7xdwbWws05pH2E27nu8DeXW0lkZ5f7EmRm_boM2eyoBbU5p1EQ6rY3CvSQ5VAMgcHl4OaAeDtp1GW-l6pMuSE2ZY9WBMwEdNUVQQI58Gx2xq9Sv-y5lip-Qrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجمع هلدینگ خلیج فارس لغو شد
🔹
مجمع عادی هلدینگ خلیج فارس که بنا بود امروز هیئت‌مدیرهٔ جدید را معرفی کند، به‌دلیل آنچه عدم اعلام حضور نمایندگان سهام عدالت عنوان شد، از نصاب افتاد و لغو شد.
🔸
این درحالی‌ست که نمایندگان سهام عدالت ساعتی قبل در مجمع فوق‌العادهٔ…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454950" target="_blank">📅 11:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454949">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سپاه: اعتراف رسانه‌های خارجی به شکست ترامپ حاصل مجاهدت رسانه‌های انقلابی در مقابله با دروغ پراکنی‌های دشمنان است
🔹
بیانیۀ سپاه پاسداران به‌مناسبت روز خبرنگار و سالروز شهادت شهید محمود صارمی: ۱۷ مرداد، یادآور مجاهدت خستگی‌ناپذیر شهید محمود صارمی و دیگر شهدای…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454949" target="_blank">📅 11:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454948">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e2ece40d.mp4?token=G9xTa_Gh2xbXVQtAvVSL0q2o2t5ypTF9Nk-JkU8iwHLOtX6cDw0buY7_39QL1p_JGqb89bzfpCwFqf3fUxSTbd7B-DGxxUsRPPJFZuqfJIHyem7uy_qCNpYakxFvsscJkGLJFKrOZrRPk2dUgiQ8KeCzi7dlLuFrA_pcGHfmsFyAoidTvmIjmGLEIFlQaIkLv9MewatMIvMgn16yevy3p-WwEkTgGMC1cFejjkV54q80EPVnpR3Hnv35BvYpcUDofQQONaN-4_Pxw9ukN3lUdwChBsRLfy7HT0pCd0K-R_88yQa6Ji6PR37gPxVDy5M7U18u3wkehyQKWhHysAmMwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e2ece40d.mp4?token=G9xTa_Gh2xbXVQtAvVSL0q2o2t5ypTF9Nk-JkU8iwHLOtX6cDw0buY7_39QL1p_JGqb89bzfpCwFqf3fUxSTbd7B-DGxxUsRPPJFZuqfJIHyem7uy_qCNpYakxFvsscJkGLJFKrOZrRPk2dUgiQ8KeCzi7dlLuFrA_pcGHfmsFyAoidTvmIjmGLEIFlQaIkLv9MewatMIvMgn16yevy3p-WwEkTgGMC1cFejjkV54q80EPVnpR3Hnv35BvYpcUDofQQONaN-4_Pxw9ukN3lUdwChBsRLfy7HT0pCd0K-R_88yQa6Ji6PR37gPxVDy5M7U18u3wkehyQKWhHysAmMwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: رأی مصادره اموال ساعدی‌نیا جهت فرجام‌خواهی به دیوان عالی کشور ارسال شد
🔹
براساس رأی صادره، تمام اموال منقول و غیرمنقول ساعدی‌نیا مشمول مصادره قرار گرفته است؛ شایعات رفع پلمب برخی کافه‌های متعلق به متهم صحت ندارد.
🔹
تا زمان بررسی فرجام‌خواهی…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454948" target="_blank">📅 11:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454947">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHMQ4vGBGzxA9466pPB8g0f06Sh0gHDTH2a23jdaP9uVkG-JaBAcQQxtGti5SAGzJc0VUSB4c-29223cLEYyn2BKucKivGVPllgIMdVFhON_uTtG3FzCmdAK_3c-5Pz2gpMEFf1q9IX0Li24qztNn0dM0v_5Y4T2b6nlreV5HPK-n2na0iPbkjrs7z70dwD6wIOvj15lO2ZEhP-YlFdWUsxpVUZFIbpZJaBY2vG-9-qpzmN3c3myX8TI8qVzCcfNEONHaQZn8XgVuZDA9Tbi7AEj5xO8XTZ6pO2xz1-EVrTt9yql_f0upHpwWtv8oUx3W5yJplJlTfgCG-WYtw7Qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیهٔ وزارت خارجه به‌مناسبت بیست‌وهشتمین سالروز جنایت حمله به کنسولگری ایران در مزار شریف و شهادت دیپلمات‌های ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454947" target="_blank">📅 11:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454946">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd3fbe409.mp4?token=je1SPUd6xbIaWqqscya8kjRO1DsbGsqET7dn6p8GaK5zQghzqJ5tt2PoidAVS4ZRGuyJZ6WNQ5u0G40zg63_FFTkhIA6LpZ7n3iCeiF4HKpaWiy7hfrqTTYfeozfThZVLiRkD6cJFNns6NkW6WfPJKXXxuI7Bc8bJJLENCKbYpwY-tpLCQTGZxxQR17mH1m05pG63ruwC9GTUVt4EjHrHvdpykTAViLtunCzaVRPipXRGg1k_Fsl8jqTsmQuqiiDsP9UFuL5HYS82qaZOqZ88JKeHygLXCastR624FI3v64dmHjPDsT4Erlv6ybWb3EORT1xQBhN5Ts768twbt0MLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd3fbe409.mp4?token=je1SPUd6xbIaWqqscya8kjRO1DsbGsqET7dn6p8GaK5zQghzqJ5tt2PoidAVS4ZRGuyJZ6WNQ5u0G40zg63_FFTkhIA6LpZ7n3iCeiF4HKpaWiy7hfrqTTYfeozfThZVLiRkD6cJFNns6NkW6WfPJKXXxuI7Bc8bJJLENCKbYpwY-tpLCQTGZxxQR17mH1m05pG63ruwC9GTUVt4EjHrHvdpykTAViLtunCzaVRPipXRGg1k_Fsl8jqTsmQuqiiDsP9UFuL5HYS82qaZOqZ88JKeHygLXCastR624FI3v64dmHjPDsT4Erlv6ybWb3EORT1xQBhN5Ts768twbt0MLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: رأی مصادره اموال ساعدی‌نیا جهت فرجام‌خواهی به دیوان عالی کشور ارسال شد
🔹
براساس رأی صادره، تمام اموال منقول و غیرمنقول ساعدی‌نیا مشمول مصادره قرار گرفته است؛ شایعات رفع پلمب برخی کافه‌های متعلق به متهم صحت ندارد.
🔹
تا زمان بررسی فرجام‌خواهی و اعلام نظر نهایی دیوان عالی کشور، ساعدی‌نیا رسماً از فعالیت در حوزهٔ کافه‌داری محروم است.
@farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454946" target="_blank">📅 11:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454945">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-Rf8cBl4DlMoeXtrWuFiLfR8v-X0H-di2XBrgi0_ScWQCbKkG6elcrpmEfKAt03ehBoyeA59g_4DK6wdYkSm3cofdEiLp9MXQ8KPmRotcwYTX3I55DtJt4GJOyRzyd9xKlHwLub5vVff0JtRHy_t-O3OgPMiDROf3Hn8jzNgCchViipRen1WUGUToGjV473Z-Eag-HyVACr-2Iic_4I-Ff-kJ5AMGIeFTy69u1JcU3LMX_u6wuqcx9qMw9aiI2JhQvTaIPQkw48PtSQOayjDS4JUN2IdXaXRb7xHApBhlJvEp5u7ekCT_Lf2k47UWrOmoWGsjSEfWw31rC-fMR4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف لاشهٔ پلنگ در پناهگاه حیات‌وحش عباس‌آباد اصفهان
🔹
در جریان پایش میدانی و بازدید از آبشخورهای پناهگاه حیات‌وحش عباس‌آباد اصفهان، لاشهٔ یک پلنگ حدودا ۵ ساله توسط محیط‌بانان کشف شد.
🔹
این پلنگ که در حین تغذیه از شکار خود تلف شده است، جهت بررسی‌های تخصصی و تعیین علت دقیق مرگ به مرکز استان منتقل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454945" target="_blank">📅 11:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454944">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: درپی انجام انفجار‌های کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز، احتمال شنیدن صدای انفجار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454944" target="_blank">📅 10:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454943">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNdI6_06ZmqJTOeSXfzeR-Ox9O2og1VJj5PvI7PmB8RfRsmZJLEz3bUILPJupl7h-3pHA9m_dHrUe8TCalMAn4rb3kVbRQsK8Xv8QT5XmKWBTAXUIgUdmJvyIcxOXk0xNZruMQGRgRTVyyRq5WyAXDUWJxfKCaO2YapJFyfP1fLj4n-DXcHD42xXPC4vK5XYM0y4HC636DcphgsUdwQqzrBWZeniXfRJZMr2Iwf7dd5NJA_OIOV7a20W4oq3Cyg5MoiY5SWPi0n67h8tZYI4xcte9MNrPFJZ1RG4JlJ0H7nEmyQOkTufYTmT3KKfC4a96bO90fmKhYe7f5flcdLrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی یک کشتی دیگر در تنگهٔ هرمز
🔹
پایش‌های ماهواره‌ای نشان می‌دهد که یک کشتی که احتمالا نفتکش است در مسیر جنوبی تنگهٔ هرمز دچار آتش‌سوزی شده است.
🔸
بامداد امروز یک آتش‌سوزی در کریدور جنوبی تنگهٔ هرمز اتفاق افتاد و یک شناور مقابله با آلودگی نفتی و اطفای حریق به‌نام «ادنوک ای‌آر۰۱» خود را به منطقهٔ حادثه رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454943" target="_blank">📅 10:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454942">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUmTCs9-mA5p6qCHSrc7iCbZgh8TSUp58xCB3gL0WDSI_ATYCTM8vyFNGUacl6AoG23RRcY1H5XifRP267tYeNDxT7ZLl0HtGouZYlHkzldLD-3zy8dy27_7mlpXTq5BPgK6VdrzbrTsgl-OnZRhiTrRKcq-sJR-jaf6tVibOiCVFyf88CPtEbxTkLosiqWzeGX6Sv0E1w-1sYiEDeemNRd1HkVumpPRLu0IZ0GxtUR_6TyXkoOa6d3Hib0lkao5XJdN0OhEmF4hlSrB2h7_SrzfT1sk8pERK8EM-XtdpxFERmYjPPvvF1L4cIxY2Dbltbz1wFS7BExd0RQstA1fig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریاچهٔ ارومیه جان گرفت
🔹
شرکت آب منطقه‌ای آذربایجان‌شرقی: حجم آب ورودی به دریاچهٔ ارومیه از ۴.۵ میلیارد مترمکعب در سال آبی جاری عبور کرد؛ این میزان، بالاتر از حقابهٔ تعیین‌شده برای دریاچه بوده و بیانگر بهبود شرایط آبی این پهنه نسبت به سال‌های گذشته است.
🔹
استمرار این روند امیدبخش، نیازمند تداوم مدیریت علمی و رعایت دقیق الگوی مصرف است تا پایداریِ ایجادشده در تراز آبی دریاچهٔ ارومیه حفظ و تقویت شود.
عکس: عادل باخدا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454942" target="_blank">📅 10:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454941">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCY8Tr09X168pnG5G9kcfcry1Kr6DYUYgnJ7NPIxJKoiDXgvu3oX-r7ii4srYp5AjUgHJKLu3Nj9oOtN0shGfE5uZAp-Zoykw2NeXTml316bYGeXtAPsgLkm4_9OdfcC99m-Vwd9KmgwB2-VF1EjnMOLH7SqFCqb_lfUPy6ldYCzBO7yVnPWb6NaU_WxUbVTHV-6-UBF0TF__EndqWNTpqmpEVQfwjuopz9cMkR95xy4nFz2Tap7NTha-wIvTEbez2janZ1j2-h5l-Dgzb7wvfNpsTiPBOURJbdMRnoM6g5jN6qtdT4xlyJA_Djxy4LhU7OfS__XEjIvpGlHK31jXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو برای کمک آمد
🔹
رئیس فیفا که با طناب ترامپ به چاه افتاده حالا به دنبال خروج از این چاه با کمک عامل این بحران است.
🔹
نشریۀ تلگراف نوشت: ترامپ وارد میدان شده و می‌خواهد هر چه در توان دارد برای حفظ اینفانتینو در سمت ریاست فیفا بگذارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454941" target="_blank">📅 10:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454940">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارتش: خبرنگاران فرماندهان نبرد رسانه‌ای با دشمن هستند
🔹
ارتش جمهوری اسلامی ایران به‌مناسبت روز خبرنگار: خبرنگاران، فرماندهان خط مقدم نبرد رسانه‌ای با دشمن به شمار می‌روند.
🔹
فرماندهانی که با ابزار قلم، تصویر و روایت، در برابر هجمه‌های سازمان‌یافتهٔ دشمنان ایستادگی می‌کنند.
🔹
خبرنگاران با روشنگری مستمر، ملت‌ها را در مسیر تشخیص حق از باطل یاری داده و زمینه‌ساز تقویت بصیرت عمومی در برابر موج‌های فریب و عملیات‌های شناختی می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454940" target="_blank">📅 10:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454939">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEJHZetUcFI_7W_j92L_BS8PNGcxOx28Rof1OFLpy3ULZVBtn5yvW8DxosCxLKdWADtEnju0MFzzAhQoIqTtjktWeYGCJclZzpXCiBQbiFOCN4Ddj6nSh6HfaqHVcGcvA6_NSDW94RYzRRvPEcHT2C1lI2MT5bi8SlGufr7nepzQiO3f8TqR7zjrVNN2o811K6sWc82so28kEMjJfP3iBBBuYdS7nz4sAELyAoI7Ri7URuL8ChifC1sEcdDCYr6HRj7b28YJLW8L1ZfAoQBBZJopf1LHJz7MLO_g4ACwWYGRuD1QmT66x7c3U7Ncurc7fpILmMHinXYlYPmR797vUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ و نیم میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با با ثبت رکورد تاریخی جدید از ۵ میلیون و ۵۰۰ هزار واحد عبور کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454939" target="_blank">📅 09:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454938">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2094e644c0.mp4?token=Ez9BGLaWn1rNC4JmwOVwGdYIs9vMP2BQQ_UW8esU7bIOVCmz-mJZswRWc2GYDvPn-70CZ-Z-qp6H8KuhADvPQZoNaMktVr8tCmpqMXxkY_KGW1k99e9SrT9yE2JjtfNBAekaW5iFyPHRT5X95nAA5cmgE7HlTLv4fNjl8AncZ5L1OA6wN9isjQWRk0leCev5BGqqOwTa3TATYCa1i-t5_zk638KqQPhyZG9S872yQoptq4_biN_g_8ueqhEG_zztR_wrzM80QmZebNbRZYdY4iIQy5Tlgeqo6QhfV3FSHr_BFagzsS8eB_zyULQNDzOpi1E5AgYzBHZpOej-RjiKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2094e644c0.mp4?token=Ez9BGLaWn1rNC4JmwOVwGdYIs9vMP2BQQ_UW8esU7bIOVCmz-mJZswRWc2GYDvPn-70CZ-Z-qp6H8KuhADvPQZoNaMktVr8tCmpqMXxkY_KGW1k99e9SrT9yE2JjtfNBAekaW5iFyPHRT5X95nAA5cmgE7HlTLv4fNjl8AncZ5L1OA6wN9isjQWRk0leCev5BGqqOwTa3TATYCa1i-t5_zk638KqQPhyZG9S872yQoptq4_biN_g_8ueqhEG_zztR_wrzM80QmZebNbRZYdY4iIQy5Tlgeqo6QhfV3FSHr_BFagzsS8eB_zyULQNDzOpi1E5AgYzBHZpOej-RjiKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های ایام عزاداری دههٔ آخر ماه صفر در حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454938" target="_blank">📅 09:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454937">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سپاه: اعتراف رسانه‌های خارجی به شکست ترامپ حاصل مجاهدت رسانه‌های انقلابی در مقابله با دروغ پراکنی‌های دشمنان است
🔹
بیانیۀ سپاه پاسداران به‌مناسبت روز خبرنگار و سالروز شهادت شهید محمود صارمی: ۱۷ مرداد، یادآور مجاهدت خستگی‌ناپذیر شهید محمود صارمی و دیگر شهدای سرافراز خبرنگار؛ نماد تعهد و دلدادگی اصحاب رسانه به کیان انقلاب و ایران اسلامی و آرمان‌های والا و تمدن ساز آن است.
🔹
امروز، منطقه و جهان، شاهد یکی از پیچیده ترین و سرنوشت‌سازترین نبردهای تاریخی معاصر است. آمریکا و رژیم صهیونیستی در جنگ‌های دوم و سوم علیه ایران اسلامی، علی‌رغم تمام تلاش‌ها و اقدامات نظامی و عملیات رسانه‌ای، نه تنها به اهداف اعلامی و شوم ترسیم شده توسط رئیس‌جمهور پلید و متوهم آمریکا دست‌نیافته، بلکه ابعاد تازه‌ای از بن‌بست راهبردی، شکاف در صفوف متحدان غربی و هویدا شدن افول هیمنۀ آنان به تصویر کشیده شده است.
🔹
رسانه‌های جهان، با اذعان به ناکامی واشنگتن در غلبه بر جمهوری اسلامی، به وضوح از «شکست» و «تله خودساخته» ترامپ در جنگ علیه ایران سخن می‌گویند و حتی اعتراف می‌کنند که تفاهم‌نامه‌های حاصله، چیزی جز «سند تسلیم آمریکا» در برابر واقعیت‌های میدانی و قدرت مذاکراتی ایران نبوده است.
🔹
این اعترافات، بیانگر درخشش مولفه‌های اقتدار نظامی و بازدارندگی فعال کشور است؛ مولفه‌هایی که مرهون هوشمندی راهبردی، ایستادگی ملت و پشتیبانی همه‌جانبه از نیروهای مسلح، به‌ویژه سپاه پاسداران انقلاب اسلامی و نیز مجاهدت هوشمندانه و دقیق رسانه‌های انقلابی در مقابله با دروغ پراکنی‌ها و بزرگ‌نمایی‌های خصمانه دشمنان است.
🔹
در این میدان پرچالش و معنادار، دشمن با بهره‌گیری از تمامی ظرفیت‌های جنگ ترکیبی و سایبری از جمله هوش مصنوعی، در پی تحریف حقایق بوده تا میان ملت و نظام ایران فاصله بیندازد و سرمایه عظیم اجتماعی و وحدت مقدس ملی را نشانه بگیرد.
🔹
تجربۀ اغتشاشات به‌ویژه در کودتای ۱۸ و ۱۹ دی‌ماه ۱۴۰۴ به ما آموخت که ضلع رسانه‌ای فتنه، پیچیده‌ترین و حیاتی‌ترین بخش این معادله است؛ جایی که «روایت اول» از آنِ کسی خواهد بود که سریع‌تر، دقیق‌تر و هوشمندانه‌تر وارد میدان شود.
🔹
این تجرب‌ تلخ فرصتی شد تا خبرنگاران فهیم و انقلابی و رسانه‌های متعهد و زمان شناس، در جنگ تحمیلی اخیر، با تمرکز بر روایت‌سازی صحیح و بهنگام، با عملیات روانی و آفند رسانه‌ای علیه دشمن، تصاویر ماندگاری از صلابت رزمندگان، گزارش‌های صادقانه از حضور و مقاومت مردم، روایت مظلومیت شهدا و خانواده‌های آنان و بازتاب همبستگی کم‌نظیر ملت ایران، را  تولید و انتشار دهند که بخشی جدایی‌ناپذیر از تاریخ پرافتخار این برهه حساس و ارزشمند محسوب می شود.
🔹
خبرنگارانی که در جنگ تحمیلی دوم و سوم زیر آتش و در معرض تهدید، لحظه‌ای از انجام مسئولیت خود عقب ننشستند؛ آنان که در کنار نیروهای امدادی، مدافعان امنیت و مردم مقاوم حضور یافتند و حتی برخی از ایشان جان خود را در راه اطلاع‌رسانی و دفاع از حقیقت فدا کردند، شایسته بالاترین مراتب تکریم و قدردانی‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454937" target="_blank">📅 08:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454936">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWpzp0cF3XfmH5fC0GqsdWivoO6yLlUlZrqgVAM4qmpcv9Hl8mE5dNEp-B6CNyoSHHfbr4x2WGLUn9j1UqhoUCz4pFJhTxV9IiDHjLPgqWmu_ZDYNkvPNYpJ1OMCyvGX4YRvK3TwvKaGcEbW88FMAwsPAqxcAeoA8GjRoI2jTw3PNKsqoa-Y5GlorMDvUbE7Nwmd1Xw8H3F4tSF5f21X1dEIKsPlyiS8pfcf2zB_-RLU_g-erU5ApdTAYoqHeUxg-IzVgm6sXN4y7jVZ69t1s0pghla2X_oHaI4SUMqYHWztfdwszPEAV4m3zv-74haVhf1VrbclxCMkKEg9YRXyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای: خبرنگار متعهد، هم‌سنگر رزمندگان پشت لانچر است
🔹
رئیس قوه‌قضائیه در پیامی به‌مناسبت روز خبرنگار نوشت: خبرنگاران متعهد کشور در دشوارترین روزهای یک‌سال گذشته، با شجاعت و مسئولیت‌پذیری از مرزهای آگاهی عمومی و انسجام ملی پاسداری و در میدان جنگ شناختی، با خط تحریف، سیاه‌نمایی و تفرقه‌افکنی دشمن مقابله کردند.
🔹
در مقطعی که تمام دنیای کفر و استکبار، جنگی موجودیتی به ایران عزیز ما تحمیل کرده‌، عظمت کاری خبرنگاری بیش از پیش درک می‌شود.
🔹
خبرنگاری که سعی می‌کند خبرش درست و دقیق و سریع باشد و در عین حال التهاب و تشنج اجتماعی خلق نکند و امنیت روانی مردم را تثبیت کند، حقیقتاً هم‌سنگر همان رزمندگان پشت لانچر است که از تمامیت ارضی و عزت و اقتدار ایران عزیز دفاع و صیانت می‌کنند.
🔹
خبرنگار متعهد، دیده‌بان تیزبین میدان جنگ روایت‌هاست؛ او که با کلامی سدید و قلمی بصیر، خاکریزهای ذهن جامعه را در برابر تهاجم ترکیبی دشمنان استقلال و اقتدار ایران، مستحکم می‌سازد و اجازه نمی‌دهد که غبار تردید، سیمای درخشان حقانیت ایران اسلامی را مخدوش کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454936" target="_blank">📅 08:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454935">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزارت دفاع: ایران در میدان دفاع مقتدر خواهد ماند
🔹
وزارت دفاع و پشتیبانی نیروهای مسلح به‌مناسبت روز خبرنگار: در شرایط جنگ ترکیبی و عملیات روانی دشمن، روایت صادقانه حقیقت، مطالبه‌گری مسئولانه و صیانت از افکار عمومی، بخشی از قدرت ملی و بازدارندگی جمهوری اسلامی ایران است.
🔹
خبرنگاران، یاوران و همراهان راهبردی در شکل‌گیری گفتمان دفاع همه‌جانبه و انقلاب صنعتی دفاعی جمهوری اسلامی ایران هستند.
🔹
جمهوری اسلامی ایران، در میدان دفاع، در میدان روایت و در میدان اراده، همچنان مقتدر، هوشمند و آماده خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454935" target="_blank">📅 08:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454934">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRxuH2Hw1H61mgb98W7XdJUPE-r7I2etsrdC3ZJ8GFXNRUvjxrYFf4tc3vNLy6hJZDMmi-l1y43i1EX9Ee9c-CTEBQyduQB0GPtkSlITj01ENJMglHX5nII7ATGt9AKa91Zxr1f0mEk80wXxcYRezjhGXZxjkC3QbB86b9NwkQHzIA92yGredJENa3qqfQLKw-_Rz1slKXohyUYvvQlhbIPcV_K_Kf5_g95sGk4NKMdvV-_FWdjSpUHzlnr2xxUCyoR7APe4LHKPnBKPfMkN48mclwJJD6u7Q3PA93kh9oigsSkFIjZNqRPE5-Q1G-fMnX8iMKpqlIYKCbkmuL1ChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: خبرنگاران رزمندگانی هستند که سنگرشان آگاهی و سلاح‌شان حقیقت است
🔹
پیام رئیس‌مجلس به‌مناسبت ۱۷ مرداد: سرنوشت ملت‌ها علاوه‌بر آنکه در میدان آتش رقم بخورد، در میدان روایت تعیین می‌شود و میدان‌های نبرد تنها بر خاک و دریا و آسمان شکل نمی‌گیرند.
🔹
صهیونیسم و استکبار جهانی تنها شهرها را بمباران نمی‌کنند، آن‌ها حقیقت را هدف قرار داده و اعتماد ملت‌ها را نشانه گرفته‌اند و اگر روزی با گلوله به جنگ تمدن‌ها می‌رفتند، اکنون با خبر، تصویر، شایعه و تحریف به میدان آمده‌اند.
🔹
در چنین جهانی، خبرنگاران تنها مخابره‌کنندۀ اخبار نیستند؛ رزمندگانی هستند که سنگرشان آگاهی، سلاح‌شان حقیقت و مأموریت‌شان دفاع از امنیت روانی، هویت ملی و اقتدار فرهنگی یک ملت است.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454934" target="_blank">📅 08:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454933">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یمن نفت عربستان را زمین زد
🔹
کپلر گزارش داد، صادرات نفت عربستان پس از اعلام محاصرۀ یمن از بیش از ۴ میلیون بشکه در روز، به کمتر از یک میلیون بشکه کاهش‌یافته است.
🔹
تنها راه باز صادرات نفت عربستان اکنون کانال سوئز است که سابقۀ بسته شدن دارد.
🔹
همچنین پیش‌تر اعلام شده بود که برای اولین‌بار در ۴۰ سال گذشته صادرات نفت عربستان به آمریکا صفر شده است.
🔹
طبق داده‌های کپلر پس از اعلام رسمی‌ محاصره از مسیر باب‌المندب، میزان بارگیری نفت در ینبع به‌عنوان خط دورزن تنگۀ هرمز صفر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/454933" target="_blank">📅 07:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454932">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2nxUjCbbIfYs8djqzhiJnw9hrxkK9w3_1AqkIhiECQtwmpMDSDbGgtAy5t8EtruIgKor00XoFJU3rj-dLr4Macla9jOXdVnVu2gMZPHwuF-jjKcnp7XBuKzMvkTKRc582_0LedcuuMuvcL-UBjywcCUtyYExpOgt0-PSJ8UU7M7xzEnouFBsWPV02d2IDvdcN9KXZhq5lyo1b4YrZvLtUDPSj84SvBAeoSzpEKoJJmUdrPDNfmhQTv8l0_tc1mFzbNAHR9y9ns13dV1o4R6w7JhHBgUveaay0TgAg04WeLFjE7q-SJsup9j95yu73K_sXyPi5OpZ83AgPYmWDxg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ اوکراین به پالایشگاه سیزران روسیه
🔹
پالایشگاه سیزران روسیه ساعتی پیش هدف حملۀ پهپادی اوکراین قرار گرفت.
🔹
پیشتر فایننشیال تایمز گزارش داده بود که نیمی از زیرساخت پالایشی روسیه به دلیل حملات اوکراین متوقف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/454932" target="_blank">📅 07:36 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
