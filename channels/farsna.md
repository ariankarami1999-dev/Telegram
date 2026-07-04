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
<img src="https://cdn4.telesco.pe/file/Sd_fsjzUosmXMZvdJJhhA8gUobCRP5iRKyBH-L1od2wbnx20LYYwe_OuSCGVtx9pE_fbfa675sIsHnpu4DTy1iPIT3g1p_PEg3Dg0mpGW_RZ7rf0nDz7PRO33ydNNjD9M8EomfZYjz1XNdnDEG-ihCiVBGCpwt-vpFQNj4_ljAQXkTBTXyEes5CjGbTrq9vohY8E8XYmMBY2Rlk4eUA8mUZJ0RkRnBWRPamghgNSCth1QKe4B2MBeI2C6DBf2e6oYvKHvb7veoqJeh3HOGz2xePNpz6NHXSMBnQwAHvIebj23bYalqvPOHtiMtKa03LExxX8b7bCpXOS01AQ0dtwNA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 23:57:09</div>
<hr>

<div class="tg-post" id="msg-446837">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d2d2c1542.mp4?token=fk5AAEDA8XEynNjnBLe2SO5HLkOagSTQmy_cnTfe264lK6Dcu8ebQu0_lPwCX1NaJbYgPVUwp-PR3PaerulN6SKHJaSXn_Ela59K0RA1JjKX70xGq3JsG0le7qRDI1C20SI5y3-oGDFbd-4M3MF_83c5BHa8IH_SIgxHmO-8GXqijt4FrJuxyqRfef1PxkQurw78ZS8a0n-VYI9S4ejJY0vYbv0BKkDHoCq_l7S3qExQX2u7h-7fvDb_vJbBAKGugf_OkMnl0jUSw9lacmreZJePbrSaELwGUwo5yQQmVo7kQrfwj4n7U8KjCHuaHoLBoKLrDah3bVtB6VkIfU3ffqBN2xkCws8g1X2JMJVygZPRUuwbVTV-TyjeI1ADufG1NzgvQPHWuqQq8okklLyAxiow8aGYxKid3UQ604p-7TK5EjVXksbdg5qwIob1wR6LToiiuagL1AA9lKNHayF21UfkYY9fgATW_2PEGvWWttlcjE5nV71WqQmaWg1f8f9S_aq4uJEpWFjfBXHRI4-k5iRpgHkOYpey9fQb2J_6u-vu-NjhJAJL_a8ZbmXFIjMTA3ZJStPHAft4o_7f8cackFxrxPec85m0mn24XH3VJckCmSTINeBqCyE9pYWHgHvqi8ASRgXmZVV9IN3OhduS8ekAc2IlekviGXQaMnBaqOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d2d2c1542.mp4?token=fk5AAEDA8XEynNjnBLe2SO5HLkOagSTQmy_cnTfe264lK6Dcu8ebQu0_lPwCX1NaJbYgPVUwp-PR3PaerulN6SKHJaSXn_Ela59K0RA1JjKX70xGq3JsG0le7qRDI1C20SI5y3-oGDFbd-4M3MF_83c5BHa8IH_SIgxHmO-8GXqijt4FrJuxyqRfef1PxkQurw78ZS8a0n-VYI9S4ejJY0vYbv0BKkDHoCq_l7S3qExQX2u7h-7fvDb_vJbBAKGugf_OkMnl0jUSw9lacmreZJePbrSaELwGUwo5yQQmVo7kQrfwj4n7U8KjCHuaHoLBoKLrDah3bVtB6VkIfU3ffqBN2xkCws8g1X2JMJVygZPRUuwbVTV-TyjeI1ADufG1NzgvQPHWuqQq8okklLyAxiow8aGYxKid3UQ604p-7TK5EjVXksbdg5qwIob1wR6LToiiuagL1AA9lKNHayF21UfkYY9fgATW_2PEGvWWttlcjE5nV71WqQmaWg1f8f9S_aq4uJEpWFjfBXHRI4-k5iRpgHkOYpey9fQb2J_6u-vu-NjhJAJL_a8ZbmXFIjMTA3ZJStPHAft4o_7f8cackFxrxPec85m0mn24XH3VJckCmSTINeBqCyE9pYWHgHvqi8ASRgXmZVV9IN3OhduS8ekAc2IlekviGXQaMnBaqOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندۀ اهل‌سنت مردم کردستان: شرکت در مراسم تشییع، ادای دین به رهبر شهید است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 346 · <a href="https://t.me/farsna/446837" target="_blank">📅 23:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446836">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd59919123.mp4?token=Xg8Mls9B7NTiiXR1R_9SNzgchbAUA2l73tjBFyo5QM2EkCks-46_fxtgRfJBlzK-YZnQslP2p2iv1L3tkEuRcTLSCqwtaGqXZ4S4qnWBl3JgzyapGcsai7yF9OEOHaZDbQ1MFnV6mBNjmP9MzH09fP8A-M6vSc4cnQavRWaMJtY8V4-nRnVQ-mgCtKrLUlTKvkyyAoWvw0JFwDQpLP9X5Un1aLUdBX-epFqTotju__uJeB2-UNXNfA9Z6HLlaJrC33tIZoUMkooVUyTWjs5fRppqGWc6i0KZ-vgtLXD3PTlSH5Dkq2Fd_LOionOU3uK5VHtEwYBiH_qih2m9OfcaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd59919123.mp4?token=Xg8Mls9B7NTiiXR1R_9SNzgchbAUA2l73tjBFyo5QM2EkCks-46_fxtgRfJBlzK-YZnQslP2p2iv1L3tkEuRcTLSCqwtaGqXZ4S4qnWBl3JgzyapGcsai7yF9OEOHaZDbQ1MFnV6mBNjmP9MzH09fP8A-M6vSc4cnQavRWaMJtY8V4-nRnVQ-mgCtKrLUlTKvkyyAoWvw0JFwDQpLP9X5Un1aLUdBX-epFqTotju__uJeB2-UNXNfA9Z6HLlaJrC33tIZoUMkooVUyTWjs5fRppqGWc6i0KZ-vgtLXD3PTlSH5Dkq2Fd_LOionOU3uK5VHtEwYBiH_qih2m9OfcaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: این لحظات شب‌های قدر جمهوری اسلامی ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/farsna/446836" target="_blank">📅 23:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446835">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0530b61b0d.mp4?token=qmJ5EP2OZXWvPoSCvmnZTEPvOdV1h36kKr6Q2PvIyj-RfZNjEywU9zFypT2ekBi3w_XZ-ZSoEe1wzDr37UprivFu-i2Yc2Qs04njhC7QCBMQHGlQK6y4AEQnL9e62o1n4jOaQpXiQC0EjvO6z37_HdwiA9fCuF52P65_7IyMtTegAAOUg28p1BpXaPux4L22ckR5n_Mgc1CL2fzc6ufDeH3UbBJ5sOcjorDRA6eiiawgPCgpgSJ-f_B4e3MtAUvrUCL89ASZu59GAndXF5-FwlaJMyJYfna_GH2CC9RMYDQXMOwUsOyzJpR4FzoSBuuESj4grTCO6hLeLWZfWjOq-BF-320oPWNHG21oKQY09pjxjK5_3-u_CGNcTjhHFi12qFEzeV0l1FHFV8LQdFQc3UXsjAVCndsFsnCAD4a2ju10H21R-znFBYdR92oxJKFtC7fmCJDMXOj-SgxORv4uZUIJgDv7WfOTCxFIpxfXT9thQCbucOksxA8XoLbWr9c2goxtJ1TkHHAGzIkbmnV8wmPoHXg5K1m2Vj5ra94GXm7RfMg_iJ9ujAyMPyo30p6OI4BPuk0AtXoP1g15OxlMYSQiEAN5awuEKjQWuLyYD3_52vRIZ0N59kAQcmTatjeakkWfUhk_O3qhLWETVOt0RRfrnRnlsFadCQkAhXLXz9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0530b61b0d.mp4?token=qmJ5EP2OZXWvPoSCvmnZTEPvOdV1h36kKr6Q2PvIyj-RfZNjEywU9zFypT2ekBi3w_XZ-ZSoEe1wzDr37UprivFu-i2Yc2Qs04njhC7QCBMQHGlQK6y4AEQnL9e62o1n4jOaQpXiQC0EjvO6z37_HdwiA9fCuF52P65_7IyMtTegAAOUg28p1BpXaPux4L22ckR5n_Mgc1CL2fzc6ufDeH3UbBJ5sOcjorDRA6eiiawgPCgpgSJ-f_B4e3MtAUvrUCL89ASZu59GAndXF5-FwlaJMyJYfna_GH2CC9RMYDQXMOwUsOyzJpR4FzoSBuuESj4grTCO6hLeLWZfWjOq-BF-320oPWNHG21oKQY09pjxjK5_3-u_CGNcTjhHFi12qFEzeV0l1FHFV8LQdFQc3UXsjAVCndsFsnCAD4a2ju10H21R-znFBYdR92oxJKFtC7fmCJDMXOj-SgxORv4uZUIJgDv7WfOTCxFIpxfXT9thQCbucOksxA8XoLbWr9c2goxtJ1TkHHAGzIkbmnV8wmPoHXg5K1m2Vj5ra94GXm7RfMg_iJ9ujAyMPyo30p6OI4BPuk0AtXoP1g15OxlMYSQiEAN5awuEKjQWuLyYD3_52vRIZ0N59kAQcmTatjeakkWfUhk_O3qhLWETVOt0RRfrnRnlsFadCQkAhXLXz9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادران و کودکان نیز برای وداع آمدند
🔹
مادران عزادار و زائر به همراه کودکان‌شان از شهرها، استان‌ها و کشورهای مختلف به مصلی آمدند و باوجود امکانات مناسب اما سختی، گرما و مسافت راه را تحمل کردند تا با رهبر شهید امت اسلامی وداع کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/446835" target="_blank">📅 23:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446834">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-CF9JCKM4Sr6gFTdDHkzsN43L-jGVsGxwk9d-z8IlYvwZoOnFxCn3PRCtYB2o792Bv21WIOL8xbkR_dm_tu1GB_EHnFg5J4kRGXHbYj_MiBjIzCTy99qfMghkN6y2K4M81Yc11CJX2FSzXU-1O61JCepgPzaRqWD8ADKtXWat2_bR5gzM5AH4TffIJduPiMdaRAsHgZkf2MaK0a-Jy3MjjpGkbnOUclYs6uTE5Kt9gZ0ZJncr3_mGZQpTokIH7bQLvyez4qCgOw61P2AXCdMc91jKlJjAKh1xtof9syP9NkawV_yIuXRl_OMfynIc7IAFQpWvnX0c0_WHFXytRDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ای قلّۀ سرفراز ایران بدرود
@Farsna</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/farsna/446834" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446833">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4225985517.mp4?token=JuDDdu4GwzvdISRbhSoQpms_eDeCzDrls8kRrvBQyQ0KqgrpvSjW7gqYOf6hJJOkTmR36cYl6OhQ7yuXk3UXDvzE9tDG44xCke0skEEob0MvDaT6yTvke__gQubp_w6eFqloLMLKxRVp8YTIGiBB2kmfwczIyOS_6RQ-wCSUBYs3KeF6anLo1iTDGXEbyh3Jcx1Nuxj-5WV2Eqqz4-V_hzTw2EpqjAipE6serQnNI8aXbMKwEzXTrTfOEby_B7B5kaJ6MF_7wQ2yxOMiUi04PRvR1Sv-RSyTZWlwe0rsrczz87l6ZwqwOVWdJMmSRYnEZQltDIYh6DSCNwvQaOV22w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4225985517.mp4?token=JuDDdu4GwzvdISRbhSoQpms_eDeCzDrls8kRrvBQyQ0KqgrpvSjW7gqYOf6hJJOkTmR36cYl6OhQ7yuXk3UXDvzE9tDG44xCke0skEEob0MvDaT6yTvke__gQubp_w6eFqloLMLKxRVp8YTIGiBB2kmfwczIyOS_6RQ-wCSUBYs3KeF6anLo1iTDGXEbyh3Jcx1Nuxj-5WV2Eqqz4-V_hzTw2EpqjAipE6serQnNI8aXbMKwEzXTrTfOEby_B7B5kaJ6MF_7wQ2yxOMiUi04PRvR1Sv-RSyTZWlwe0rsrczz87l6ZwqwOVWdJMmSRYnEZQltDIYh6DSCNwvQaOV22w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای ورود عجیب عباس موزون به بیت رهبری برای دیدار با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/446833" target="_blank">📅 23:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446832">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuZJ87-i0NgZsTwBokYJwKu3Yz6AP3u75GonEBpEemUN9Vl0tZ707fUPKT1NNsvxHFqjd6ZWZ1-CD0BKj8DFaiiuYu5TcLqwMqPmVdxPFwCAs9rCzWxXR9mCrUQV7gMtHH6HeMOq0H5T5pxueVhtL1jR-O1lXTzD89j77udCSp0dWfWYLc3xIrVcBNraC4stxNCFR9yhLcqo7tPR16AHrHR-jjP9ULB8Cc4A_TPenffgX_SIMGepZBc0KRSahPvnaMurhpTZDdPtnrJBUmUFog3ARHFFzGq2zIc6ZN4bfoYfe0-f6zViX9KRoKUIXBx4goUZMx2TEOU85hGfws-Mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا دلش نیامد شاعران را حسرت به دل بگذارد!
🔹
می‌گویم اینجا چه‌کار می‌کنی؟ آمده‌ای برای پیکر آقا شعر بخوانی؟ دیگر نمی‌تواند بغض سنگینش را نگه دارد، می‌گوید: «بالاخره بعد از سال‌ها حسرت، امروز شعرخوانی، رزق و روزیِ من شد! انگار آقا نمی‌خواست شاعران را حسرت به دل بگذارد و از تهران برود! او نمی‌خواست آرزوبه‌دل بمانیم...».
📎
روایت شاعرانی که امروز مهمان آقا شدند را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/446832" target="_blank">📅 23:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446831">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb608438c.mp4?token=uryUaBITTV2Ie7VQPUnQH8u2EHCr_M1AZUiXCZbctlQtjTtLeDcO27Imd-DVWeqlqCZtPmc31Jbac-GLsAf_fWkzQzl7dpoJwDDb2kv_1Z_MJ2Ed8nV22QJvDmkTw04ntX-cOpMaF40GKD_7toOb__gFFzGnFNe_I2CoiKao642y7FIUod8-Ask8NJ1HgVWtCsjXlK8fRyHJ-tEmRLYrYhZURsJ8NO61ahF0EeGZjqMhjsdI3mo_duPLq8o_5JD0sgBFDgpmViTqhjMCXatsZWWiguRLIn_Hq6zg5ASSSufkrkWsMpC5MtBZd4Pnj_UDN-bSsO9a3s-MkgG_sSZr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb608438c.mp4?token=uryUaBITTV2Ie7VQPUnQH8u2EHCr_M1AZUiXCZbctlQtjTtLeDcO27Imd-DVWeqlqCZtPmc31Jbac-GLsAf_fWkzQzl7dpoJwDDb2kv_1Z_MJ2Ed8nV22QJvDmkTw04ntX-cOpMaF40GKD_7toOb__gFFzGnFNe_I2CoiKao642y7FIUod8-Ask8NJ1HgVWtCsjXlK8fRyHJ-tEmRLYrYhZURsJ8NO61ahF0EeGZjqMhjsdI3mo_duPLq8o_5JD0sgBFDgpmViTqhjMCXatsZWWiguRLIn_Hq6zg5ASSSufkrkWsMpC5MtBZd4Pnj_UDN-bSsO9a3s-MkgG_sSZr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله اعرافی: رهبر شهید، ایران را به یک نقطۀ اقتدار جدید رساندند و معادلات اقتدار ایران را تغییر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/446831" target="_blank">📅 23:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446830">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎥
نیکزاد، نایب‌رئیس مجلس: راه رهبر شهید را تا تحقق عزت و اقتدار ایران ادامه می‌دهیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/446830" target="_blank">📅 23:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446829">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b96217e2.mp4?token=ZUgoYb5qnLin13NC5XYDhpTFOnxv2jfisdx4uM4-ZtAF1D7E1dms7A6PPuQ76bfjv314HB6FoHXtK10tD835xPbfmRdC7kDhJsTJA7hgMZySHC5BmDrp1RV1amwd_N_k0ybJC4QteiS6JPsv8StTfbRjlpgep4ik8GtNVhA10zAd68ywAya3KAiJAJM8IPLO2xMkDuKeFTwQe0ni1ShB9XxoNaDOwu06WgirqDSMnnWndKMxFIuwB4jaRv8oo3oZln3go4OKi9wOkSumMpSoVXcU_LwkupObk1ny8Beb76fD7F-4lR35ITen4_lCkXAyOSwMbvtqhsVt3XNbHT30Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b96217e2.mp4?token=ZUgoYb5qnLin13NC5XYDhpTFOnxv2jfisdx4uM4-ZtAF1D7E1dms7A6PPuQ76bfjv314HB6FoHXtK10tD835xPbfmRdC7kDhJsTJA7hgMZySHC5BmDrp1RV1amwd_N_k0ybJC4QteiS6JPsv8StTfbRjlpgep4ik8GtNVhA10zAd68ywAya3KAiJAJM8IPLO2xMkDuKeFTwQe0ni1ShB9XxoNaDOwu06WgirqDSMnnWndKMxFIuwB4jaRv8oo3oZln3go4OKi9wOkSumMpSoVXcU_LwkupObk1ny8Beb76fD7F-4lR35ITen4_lCkXAyOSwMbvtqhsVt3XNbHT30Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور شبانه مردم در مصلای تهران
@Farspolitics</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/446829" target="_blank">📅 23:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446828">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e9711db.mp4?token=CHV1NwY47lIxrlAkBJIRoWfXo9q_nLoM4wEZ5-eef_eoWAdKGVZA-0AHwqTRHObYMUecyLA2nlQV6s7PY7N8UgkyHK5NCRtx_nOFhZyfQJc1e-hIYhys0Nuqppt4vL6s0smHE8XnAdGW1VxDC2jvQfjwj63IXdMiqmgCYVerAIaXwUeP-6q74x9OJ66MYoWftqFN5jLfGi_1xEABl-RmRHe0DDCWgXonAnV26tr8h4D7te2rZyip1NoKg8eg2rZ1Rhn0cRc4irYD6Lve6VfbMW99oICY274Nl0_VUOwI0lRXFsEx2av_Gv5_46t6_vMTiwHcPDytN5AjJP5nCfOomg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e9711db.mp4?token=CHV1NwY47lIxrlAkBJIRoWfXo9q_nLoM4wEZ5-eef_eoWAdKGVZA-0AHwqTRHObYMUecyLA2nlQV6s7PY7N8UgkyHK5NCRtx_nOFhZyfQJc1e-hIYhys0Nuqppt4vL6s0smHE8XnAdGW1VxDC2jvQfjwj63IXdMiqmgCYVerAIaXwUeP-6q74x9OJ66MYoWftqFN5jLfGi_1xEABl-RmRHe0DDCWgXonAnV26tr8h4D7te2rZyip1NoKg8eg2rZ1Rhn0cRc4irYD6Lve6VfbMW99oICY274Nl0_VUOwI0lRXFsEx2av_Gv5_46t6_vMTiwHcPDytN5AjJP5nCfOomg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: وسط جنگ جهانی در میانه بازی‌های جام جهانی، در ایران یک اتفاق تمدنی درحال رقم‌خوردن است.
@Farsna</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/446828" target="_blank">📅 23:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446827">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5f384d1a.mp4?token=dPUcuY-E0qzEjMyPtHK6iBDr-6q0GgxRRA0Kx5ZVEXLXuFIBkETzVIyafLZfeITxWjigZdLD5p-Bb1w7nMlUMwjdUUtSG36XQom2O5JY6Og2tHSOmPj-KY2uZ5FXm6XzdWUGPdp25HcejfcGEffgLrL5lTIOeCj_O8rj2H_6LTeJgjJHwXTwTiqBl35LjZqrLd1sRh_DoyuSroG8lQKsP2dW892XGcEcftycexb5zzOngyQ-ROloqjTG_-MhEWUCo4yWfGaecGDmpqvl5LwfjR4rzVX2OtvltefjwoRWe-M-aWI9B80C2D7Wu4VQs5z-gYFLudrhP4qvkN4Ifv0LZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5f384d1a.mp4?token=dPUcuY-E0qzEjMyPtHK6iBDr-6q0GgxRRA0Kx5ZVEXLXuFIBkETzVIyafLZfeITxWjigZdLD5p-Bb1w7nMlUMwjdUUtSG36XQom2O5JY6Og2tHSOmPj-KY2uZ5FXm6XzdWUGPdp25HcejfcGEffgLrL5lTIOeCj_O8rj2H_6LTeJgjJHwXTwTiqBl35LjZqrLd1sRh_DoyuSroG8lQKsP2dW892XGcEcftycexb5zzOngyQ-ROloqjTG_-MhEWUCo4yWfGaecGDmpqvl5LwfjR4rzVX2OtvltefjwoRWe-M-aWI9B80C2D7Wu4VQs5z-gYFLudrhP4qvkN4Ifv0LZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات حمل‌ونقل عمومی تهران در روز دوشنبه
🔹
معاون حمل‌ونقل ترافیک شهرداری تهران در برنامه پرچمدار: در روز بدرقه خط یک BRT مسافر پذیری ندارد اما مترو همان مسیر برقرار است.
@Farsna</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/446827" target="_blank">📅 23:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446826">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac88d5370.mp4?token=QrcwCbsOdZceyWzrcF1-jMTZsqcvycPwmlybzAvmnMbwwIFSZkZ14b9J6gXRaXy2fs4ZNgB8Dtn03-4CvcnCpMa1CigRnojYiIeSYjHHNzdJHGNurTgDZ5vYypih_Rm5VXipAFBN9z-FsSIOKf7AhlSN2n69auS9CfMH1BLzlGRZowQ8IRGzCzp4FzdQ7uk6vI4I41JAnvaY8UggZbRfBASRVh6sL3DeQfVcfNF6EuPpVCE7f3JprCHCeyS7JaCQ_RzOYPOuwksLF_4KgsGr4g_65PgYeh-2kJFlSiXC5I2AwNNl_nedvrNycTAFKMFhGo3pKgR0g29POYusX2w-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac88d5370.mp4?token=QrcwCbsOdZceyWzrcF1-jMTZsqcvycPwmlybzAvmnMbwwIFSZkZ14b9J6gXRaXy2fs4ZNgB8Dtn03-4CvcnCpMa1CigRnojYiIeSYjHHNzdJHGNurTgDZ5vYypih_Rm5VXipAFBN9z-FsSIOKf7AhlSN2n69auS9CfMH1BLzlGRZowQ8IRGzCzp4FzdQ7uk6vI4I41JAnvaY8UggZbRfBASRVh6sL3DeQfVcfNF6EuPpVCE7f3JprCHCeyS7JaCQ_RzOYPOuwksLF_4KgsGr4g_65PgYeh-2kJFlSiXC5I2AwNNl_nedvrNycTAFKMFhGo3pKgR0g29POYusX2w-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داغ علی اگر چه روی قلب‌های ماست؛ امروز ذولفقارِ علی دست مجتبا‌ست
@Farsna</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/446826" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446825">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f2df4beb.mp4?token=DsGlelKvB0RlN9hkF6zbgITlpBgLkRKES-zPh47pnbkK_iye9GPMpHRFteLen7plin4UpoNCSIRbuACe3fdOIlrfCenZ_voW2BqMGskkrl40WDzEO8Rslzs1S5KC0urdmSf1_9LzSh5fsGfcyPAaY-bYCEEYa1pZr4zUFcgz53uhDcCIh9PGKU6Bk3GtQD4o0Wd7khF7HUV6FZnYNbSIuusBOVhqAZQIiCtXwGm6zXu3hvUWm0EXsZPrhbUhQAKhXJanDaSh1zMgF9HHqk7gU0wfxOmLG2kOV71hDEIUDtU0I0JnLGuuHYPLgMFAt6NGnxiBsa5S6UfbyiZLhPNyRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f2df4beb.mp4?token=DsGlelKvB0RlN9hkF6zbgITlpBgLkRKES-zPh47pnbkK_iye9GPMpHRFteLen7plin4UpoNCSIRbuACe3fdOIlrfCenZ_voW2BqMGskkrl40WDzEO8Rslzs1S5KC0urdmSf1_9LzSh5fsGfcyPAaY-bYCEEYa1pZr4zUFcgz53uhDcCIh9PGKU6Bk3GtQD4o0Wd7khF7HUV6FZnYNbSIuusBOVhqAZQIiCtXwGm6zXu3hvUWm0EXsZPrhbUhQAKhXJanDaSh1zMgF9HHqk7gU0wfxOmLG2kOV71hDEIUDtU0I0JnLGuuHYPLgMFAt6NGnxiBsa5S6UfbyiZLhPNyRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال مردم از مراسم وداع توقف مترو در ایستگاه مصلی را لغو کرد
🔹
به‌دلیل افزایش ازدحام جمعیت، از ساعاتی پیش قطارهای مترو در ایستگاه مصلی توقف نمی‌کنند.
🔹
برای مدیریت حجم بالای مسافران از مسافران خواسته شده به جای ایستگاه مصلی، در ایستگاه‌های شهید بهشتی یا…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/446825" target="_blank">📅 23:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446824">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb1dcd259.mp4?token=R8vudZJ6LtjIFnvqn3bPTrdtlQSivwa6PgCF4KnInsgDbWvzEgSnxPzi4fu8kY2k8tR16M4asfe8xHc3v2s0KWXI6mzlI_alJl2Pc8QhdVcRbf3GnqD-XRVXEsj1OlwAUuZiJSG7ZqYYUeaK9PTuSrW3hjoxhzGEq-Z7Oj6DXRQLsOhG6IMg283jHM202Yjx8qEcuM4Vzs0efIIhQYzkKZcfuH19-5xUlAE-p2aKjId4AmmVFxyiai29VBwueX3h-kJ_zPLywwSVvTiU2HBUgHbkE9k3we2MKzB1GA6qTJYuFj4iec4anly99EVZICEZUWUKHhhk0gRXoiz63gTxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb1dcd259.mp4?token=R8vudZJ6LtjIFnvqn3bPTrdtlQSivwa6PgCF4KnInsgDbWvzEgSnxPzi4fu8kY2k8tR16M4asfe8xHc3v2s0KWXI6mzlI_alJl2Pc8QhdVcRbf3GnqD-XRVXEsj1OlwAUuZiJSG7ZqYYUeaK9PTuSrW3hjoxhzGEq-Z7Oj6DXRQLsOhG6IMg283jHM202Yjx8qEcuM4Vzs0efIIhQYzkKZcfuH19-5xUlAE-p2aKjId4AmmVFxyiai29VBwueX3h-kJ_zPLywwSVvTiU2HBUgHbkE9k3we2MKzB1GA6qTJYuFj4iec4anly99EVZICEZUWUKHhhk0gRXoiz63gTxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا در برنامه پرچمدار: مردم عزیز! خدا به ما رهبری عنایت کرده که برادر شهید، فرزند شهید، همسر شهید و دایی شهید است.
@Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/446824" target="_blank">📅 23:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446823">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363ab4d421.mp4?token=mtR_qjI50nHaYRmVNVWYgd33hO53olpqsTzIcW-P5nlA6tY0C9QGqROXRd1htZJnPsOLbYL5i3E2mWoPe-5GRJW0e4jRxD1J6RKLCMKQ57RfCjtkQGEkJkkhTf1EJU7fsRqIBjOAeESvkcErvfEbhbHmukEq5r5BVEsfpd82fallj5p8B6PkNhhMxTM4wq3uoxVLQBvnynmjg3f4dd_HjZYPVmynDuPHNB1WGBuDxAZmNqkv819sbo3UdfayNz4J1BCCOZAnIGOTEXROPFQzn0l3iQXVOCedYjcVEq7EOEsQkbw3IYvUyOEUffPgct0zGlEZN4Se74vCJXKziqBa2VHFQbtaBEBkbkWwvaPIU3nEU3hzksd0L46AuAbtLwheCLA-faBZTCI1iDmnclk7RanGHcZrybNuOoodr1mgeeSgRerprtlnk9BiSge2XtaSEtVOF9RlUKdzbhxzpF86DfI-pilzT37f_3CRxxVz2fBe3Ecutnrrn3z50EClgCpDG7FDk4VeP_tUKeIuVS8XtByYZhdMoF5R6bFaAzwsJNH1emUJJdL5ohRcbPNE3jB5dR_OKssYYLocEhW9rt5kfXpbqeTaEeX524Ri2KR1q1Fp8v-G0E_eCSUnaNLk5-vs1EBBzuaar2qJQ7EAUVeVpec1CtyQBMb5eT38-YHRuxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363ab4d421.mp4?token=mtR_qjI50nHaYRmVNVWYgd33hO53olpqsTzIcW-P5nlA6tY0C9QGqROXRd1htZJnPsOLbYL5i3E2mWoPe-5GRJW0e4jRxD1J6RKLCMKQ57RfCjtkQGEkJkkhTf1EJU7fsRqIBjOAeESvkcErvfEbhbHmukEq5r5BVEsfpd82fallj5p8B6PkNhhMxTM4wq3uoxVLQBvnynmjg3f4dd_HjZYPVmynDuPHNB1WGBuDxAZmNqkv819sbo3UdfayNz4J1BCCOZAnIGOTEXROPFQzn0l3iQXVOCedYjcVEq7EOEsQkbw3IYvUyOEUffPgct0zGlEZN4Se74vCJXKziqBa2VHFQbtaBEBkbkWwvaPIU3nEU3hzksd0L46AuAbtLwheCLA-faBZTCI1iDmnclk7RanGHcZrybNuOoodr1mgeeSgRerprtlnk9BiSge2XtaSEtVOF9RlUKdzbhxzpF86DfI-pilzT37f_3CRxxVz2fBe3Ecutnrrn3z50EClgCpDG7FDk4VeP_tUKeIuVS8XtByYZhdMoF5R6bFaAzwsJNH1emUJJdL5ohRcbPNE3jB5dR_OKssYYLocEhW9rt5kfXpbqeTaEeX524Ri2KR1q1Fp8v-G0E_eCSUnaNLk5-vs1EBBzuaar2qJQ7EAUVeVpec1CtyQBMb5eT38-YHRuxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ذکری که رهبر شهید بعد از شهادت شهیدرئیسی به خانواده ایشان گفتند
@Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/446823" target="_blank">📅 23:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446822">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571b14494f.mp4?token=cYtIJumP7vcUr7yMCHEDLwxwt1mbv4MdtIpfkR7OvyN5CN1AE3g3SpnRhrqucKeTAjIoMD_QapnLw71Sq0j7L5VNkO1w1zla4JGAkb5ihlG8gkpaX-ygjvuisFfcjGb1f_dh3Up86I6ny3o9fSFp2MiFi9UJJmoZEWkLejYxR96U7tvZKkBSnJECYrrtzGWCfu1YauQZlGi7ABDbtEebqa7q2VwlH8rmSv43Qu3wORidnjEP-FZ4w5TOe1UZ6pWfh7NrXSee6_ihwV6zg5tnEWRsnngo4ToEvdIKwV0Mftqjvb9-ZhQR1NWAn3RHvAgkf4baG59cizlIuuEcojQW6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571b14494f.mp4?token=cYtIJumP7vcUr7yMCHEDLwxwt1mbv4MdtIpfkR7OvyN5CN1AE3g3SpnRhrqucKeTAjIoMD_QapnLw71Sq0j7L5VNkO1w1zla4JGAkb5ihlG8gkpaX-ygjvuisFfcjGb1f_dh3Up86I6ny3o9fSFp2MiFi9UJJmoZEWkLejYxR96U7tvZKkBSnJECYrrtzGWCfu1YauQZlGi7ABDbtEebqa7q2VwlH8rmSv43Qu3wORidnjEP-FZ4w5TOe1UZ6pWfh7NrXSee6_ihwV6zg5tnEWRsnngo4ToEvdIKwV0Mftqjvb9-ZhQR1NWAn3RHvAgkf4baG59cizlIuuEcojQW6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرایی که از کودکان شهید میناب نمی‌دانستیم
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/446822" target="_blank">📅 23:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446821">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62936c652a.mp4?token=Tc1TwQD0PIqTB7QKjklD7K2Sr2sIM_LWcL5cPHKKQ-IBId-i9ho2vz8gxm6Q7hAVhMEIM3l6jBVLUM_rLrcoyRSqBmhCRooofuSc-bsG0bFY4tZTzuCHrmdenfJJqkQtUbCEnd9TZrXVGlRmicsDRQWh0U_CsxASb_iOQGtsWCEsLHx6WtHD5dEbIZ59yKDpXTvd2EXwrvdMsRqwgVpksjtUnbdU2lSLmSjTZDLQVAm_r9IX_mPPpoXRam-Ulad369oeVIGAzvbzu2eAAtKV6c9wRHCj5Ub0_Lf3bf8B1-mbMyruGTKhXh2U_q4hhauHEbhErEO66G3_N_5jyuMwFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62936c652a.mp4?token=Tc1TwQD0PIqTB7QKjklD7K2Sr2sIM_LWcL5cPHKKQ-IBId-i9ho2vz8gxm6Q7hAVhMEIM3l6jBVLUM_rLrcoyRSqBmhCRooofuSc-bsG0bFY4tZTzuCHrmdenfJJqkQtUbCEnd9TZrXVGlRmicsDRQWh0U_CsxASb_iOQGtsWCEsLHx6WtHD5dEbIZ59yKDpXTvd2EXwrvdMsRqwgVpksjtUnbdU2lSLmSjTZDLQVAm_r9IX_mPPpoXRam-Ulad369oeVIGAzvbzu2eAAtKV6c9wRHCj5Ub0_Lf3bf8B1-mbMyruGTKhXh2U_q4hhauHEbhErEO66G3_N_5jyuMwFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدمت‌رسانی وزیر علوم به زائران تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/446821" target="_blank">📅 23:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446816">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUZYSyYCkJIoDBl_PV-sP_1ohfPiCaSlsD3ybyPGNxJYkL3nXMQOx5td5-8hkLGWFxy74xnAMgfFxQq10OygQ9HDAdgkW1udgXfcq63YICaYsWA8hjpXn36qJl5P2d18SfDWOv4Z4WWrOLnKtZAmx5f7z6V-BdWqojcnwSa99ozVjlDqSTwV61glWgUYfadhKxmvaFv1Pz18ZGrVEMr3ErDNX_Q_yKbKj0biokGIeFcLnj6JPrl6B5OUJlH5EXQlTxZHnRuU9UDBNsmnuSr3uFZHbPExOwDo2oAIJNOYaAveoUmweLnFfh4wZ11o-d71HWD89hw6_HjEGbjHgi07kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0r6_LBkOP8SRnxL7gSQgtsMPdIcPyylqvcy9fAxXNkf18NP1EzoSggBQ_VxyVNt5ArzMHsfr7QXB712FQDWxPqmLX60jn1VdBZY-0vb5V2BvkaN1Rv65EvYG-JW0DucXYDyv-cuL46lKPLbtJ7KHhrccSrM6hPBy0jtsbFscTqo-2lqzV_br69_AlWgbzyoofAKU-boM-LCN1bA7LKbAye3oelH3qDpLD_Mf-IfatGoo0skFC4GrZM0MmsL5YcDjRYwC0ZiPecYStkVlEORyKv1uMWZazdnQh76R-OhPWefjNHq8ifiE0ju0LxaMQN9Rhg02zSrmWnrNXmkuqJGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAY6498F3yKBwhD_7baOQCji1lVo82wFcpv7Alo0ArKpgvX8cqr6psZuWf_zyBOIT3Gawa2jCyhFaJhkMJ4ei67pkSVa51qinXGraS2q7BmISaGAmnZHPa_1H0Zuipc-WUUZA1eQlxSqUMdPUBSJM9ED43y8jCH4phTLuJWjv0TT_wA3yz-M8vGIyAEnwtsV_o2ocX5EIhwhiyvEyjrSlZb3p0CBFBB4aOe1CM-6AhwIl6jPaNqFZnfg-rCxYhhGg7bZUM9pYTz8uc4O5FX3KsB1OM2NXlzb-AL9FIEH1alw4wvGP6CBpSEbHat0lM2ypnKUgT0fBgYgiivl-qRC4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObmTSzqhxHhgwoc0pB44yhHC_GfkEIT9p8VPNdEqkQEaiZoln8JDznSTJJDHVptNDr28iU2R5dNDp5JjgPQTEmhSZLd5ALL4QZ4fvm7ofhvZo1S5gUdxViUMGTY0DDdDrCp5B3iCLdpKHMjEB9X7Y6vSEltQQ8PHjhwtJVBt-thQXhKXNdtZLpnGK5XLYyLEzKcoKk_qaHpY2RgcQ20YpNdZPHzR9RqZtpNQT7LlbnU0kB3tLot3weMRLoQo5FNAAcaBVu74dwxZnLSdXb9WkFA8I3EjQaABX2dSqUNMi0S72I0hkfRFuezJ7qcGCq1RTgTN_9m5rlQgZbYMgBM3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4kfzEpeBF3dFrdtRDMKZYtuDfuIx1ir_z9FaVUT_N4r3Cr3hBRqeH7zcIiYdPYXjeXS6AGu4lBomh1L13VMhZkplxca5Q5esTw-BXzawlpNcHkmevHYv_SYlVx7pdRH-1EVj6iN5wwCrV7ZkrJ92YzNUhNo05TPSsf46nA1c06zp7X1ACUT3-xxJwEL1KWZoN09KNkYrCwBqeKRIysCsfkJ0OpnXMEVqRxyxS6ir8Y8lZZGJGYkExQVBTkmUm02ttvSeIHHHu4F-Spf95jfDYta50fkMbHVGvpS5g6RcTqGJf2VzSmVBC7tXgjVHTKOK-wh3Xo-g6jiA05zXeMzzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خانه‌ای که آشپزخانهٔ زائران قائد شهید شد
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/446816" target="_blank">📅 22:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446815">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4PXjoshNkwqb2qbPVSZNjBhazEDhG7oCDilk_fL48jt-mPu25bLPQNzY8FF1P9izbvtQCmAcnkCI0yGdXCLFcrf64PsYCK-bqTnZQGlnIVjIXYqkOQbKTrQ_-E2H7D6RgeB50OGzYMFtnLcyV1OgtDi31QIblWY1Am72V69YK9udxWBJkhWL-39dmbMvAEm2Q33A2xe3m5gaDBO9qNQrebSkfdWCJDUzO3qcqGWywNgtnFCW_nH02ySdOa9qQQIwOkIGeQ8w2nR7WzOqBVOT6NFAi2vWdyRbEq8VsfgStsUZe0vT3qcvfd4XjxrEajerI1fZ42tu9HjbNuWW7H5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش با عبور از کانادا برای فرانسه خط‌و‌نشان کشید
⚽️
مراکش ۳ - ۰ کانادا
@Sportfars</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/446815" target="_blank">📅 22:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446813">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxW_eofD_o-gEKI2-wf9ykdq6omW0SH1okj8gOmPpi6YrCi4YH9ILavB4iifxUClLsLjHN5waEnxi-J8WJKOv0PHiVEt74TMlttAfYwm1dG6_9ctVICWfkhQqocQpFjBECOwqPcDgrdHmGucym7nRzUA3sd6pw5MZy_oxYupIl2VQ-8yXyIuEJVQ5lN5cP4AezMzcLXoU2zks0DeSE03btwWwt8XowXt4yIlvXceksjYtObp4CajCSz5F_dWJBV6L0OxREg4HgP2j0b-rzPJxm_x1rXx1dXOu81KATDvZSxl2uCkxwPjs2yfmtLvu4EKPOPvvNgel9H_-JYoqhUikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمون بزرگ مدیریت جمعیت؛ کارنامه موفق تشییع رهبر شهید در روز اول
🔹
با وجود تردد لحظه‌ای و هم‌زمان ده‌ها هزار نفر در ورودی‌ها و خروجی‌های مصلی و تخلیه و پُرشدن متوالی فضای مراسم، مدیریت جمعیت در تشییع پیکر رهبر شهید انقلاب امروز با نظم قابل‌توجهی همراه بود.
🔹
از ساعات ابتدایی صبح، ورود و خروج انبوه جمعیت بدون ایجاد گره‌های سنگین ترافیکی یا بی‌نظمی در صفوف دنبال شد. آنچه این روند را متمایز می‌کرد، تدارک گسترده خدمات پشتیبانی شامل آبرسانی سیار، سیستم‌های مه‌پاش برای تعدیل دما، استقرار نیروهای اورژانس در نقاط کلیدی و جانمایی سرویس‌های بهداشتی کافی در اطراف محل برگزاری بود.
🔹
این تمهیدات درحالی اجرا شد که پیش از آغاز مراسم، اصلی‌ترین دغدغه و توصیه مکرر ستاد برگزاری و مسئولان شهری، کاهش هرگونه آسیب جسمانی و مدیریت ایمن جمعیت با توجه به حجم چندمیلیونی شرکت‌کنندگان عنوان شده بود. با توجه به مشاهدات میدانی، به‌نظر می‌رسد این تدابیر تا این لحظه توانسته است از بروز حوادث جدی جلوگیری کند و تجربه‌ای کم‌نظیر از برگزاری ایمن یک رویداد عظیم را رقم بزند.
@Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/446813" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446812">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5076b3127a.mp4?token=kkGpYDN-Sy6qXuITToqGxl-tJcHiviu-VL7MOSmmGHo0D7DjmTuZn4zzMNmdXzFB98_NaTivFyNIobaSbul5r_8yyKDnDAwhr-OD_Q2NnLZzClTGibmKY5omiW914YtMLt9c7bLVz6AP0TJBBD1l8COMNBtQ_3UUcCk8uT1Y_-08wxMYdNSzJ8JgUemlL8fi9oXoiw55p-NR_S5MG4mzMYf44DxXimsJW65pEO0kk70-ove-KqylVPpEZFkTGDIfIJs825ZlHReFCaTwHXDOAtXDpwU0EaN4uUQDTqsuharzd3Scblzqwiy0T6g1eRhjcYCSFmVa4AWr5xsn5I66vwIC3KB9gk7QJm2whMa6I_BKUnme003dfr_edcHGgPr-YDWaEpTbTs0mKKZ3DT1EnHyznmQKEujiOX1T50h5wIrab27vsxkS9ODjsImvZaSQGKXIvjdwK3ZVGSb25hd8MlV439VUiyZKRuOiEH6EB5OKKzEDPxUs7A45gkY6tTbayvhpzHjvYqauTSK3mLBoWMy-vCwpXjohqkGocoEwyg0oKDgj_85PlNbba2AWa36ihJRURqpiFA-rnnEgSCC9VlSRpmDsrBdFDvR_QMQDnrxGFgzkdaGVwGy-O4g1HavpxDSeGEDHp4hYpLITIrikmnSgtjv7drtPM1Qffxgbj0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5076b3127a.mp4?token=kkGpYDN-Sy6qXuITToqGxl-tJcHiviu-VL7MOSmmGHo0D7DjmTuZn4zzMNmdXzFB98_NaTivFyNIobaSbul5r_8yyKDnDAwhr-OD_Q2NnLZzClTGibmKY5omiW914YtMLt9c7bLVz6AP0TJBBD1l8COMNBtQ_3UUcCk8uT1Y_-08wxMYdNSzJ8JgUemlL8fi9oXoiw55p-NR_S5MG4mzMYf44DxXimsJW65pEO0kk70-ove-KqylVPpEZFkTGDIfIJs825ZlHReFCaTwHXDOAtXDpwU0EaN4uUQDTqsuharzd3Scblzqwiy0T6g1eRhjcYCSFmVa4AWr5xsn5I66vwIC3KB9gk7QJm2whMa6I_BKUnme003dfr_edcHGgPr-YDWaEpTbTs0mKKZ3DT1EnHyznmQKEujiOX1T50h5wIrab27vsxkS9ODjsImvZaSQGKXIvjdwK3ZVGSb25hd8MlV439VUiyZKRuOiEH6EB5OKKzEDPxUs7A45gkY6tTbayvhpzHjvYqauTSK3mLBoWMy-vCwpXjohqkGocoEwyg0oKDgj_85PlNbba2AWa36ihJRURqpiFA-rnnEgSCC9VlSRpmDsrBdFDvR_QMQDnrxGFgzkdaGVwGy-O4g1HavpxDSeGEDHp4hYpLITIrikmnSgtjv7drtPM1Qffxgbj0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی رهبر شهید امت در تجمع شبانۀ مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/446812" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446811">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d6a8980c.mp4?token=BeQonWe3qESvUQlbXGUR0SJ-wDohnKKIdXmaMIEerfJozTZlOyRSy087QbnPjLnz97WPk0Jjs_YxtAHHQwU4r4On8z3PYofFA3WST9TWH884oq_zmE4a56xi1odkbxe7_DBfinKvWZgqs7I4k7vsjBVuuI3kRTLOOysZb6PNNGKz5T0r7CaG2rEt5tasmR7RXvdEaZPGApjhDKGaK_pLcFVR2U40fXuiTzISdf_qUkRsu5ExRpUkThWu9W38yequzo2d_4aSiaRAsaQB0tJmdFw7kbA8jFU-NNgVRP87i1nOGoSPoIx-APGlJmjGO3SKX4hT_fYP9jr5m5eMQtNOfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d6a8980c.mp4?token=BeQonWe3qESvUQlbXGUR0SJ-wDohnKKIdXmaMIEerfJozTZlOyRSy087QbnPjLnz97WPk0Jjs_YxtAHHQwU4r4On8z3PYofFA3WST9TWH884oq_zmE4a56xi1odkbxe7_DBfinKvWZgqs7I4k7vsjBVuuI3kRTLOOysZb6PNNGKz5T0r7CaG2rEt5tasmR7RXvdEaZPGApjhDKGaK_pLcFVR2U40fXuiTzISdf_qUkRsu5ExRpUkThWu9W38yequzo2d_4aSiaRAsaQB0tJmdFw7kbA8jFU-NNgVRP87i1nOGoSPoIx-APGlJmjGO3SKX4hT_fYP9jr5m5eMQtNOfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی: رهبر شهید انقلاب در ما باوری ایجاد کرد که امروز حتی کودکان ایرانی نیز ناوهای آمریکایی را به تمسخر می‌گیرند
.
@Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/446811" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446808">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4045b92706.mp4?token=PmZsI-J6C4dqC3JHzOGUHUCKr5erwgnphxDIyTlKg27Q-oNupSs2vpWldXe0QZarB6hByrBCrgrP4Y0eLcIuPM_aM3MR_YBXzZdw4gQYjLomUKgdJYXx0kOp4E5wdEPZru3NoH-ldbCBDAJU79rulRUkqrJMVu99_vhDSvhOGJwhWz-t8BtfCqeEvW2uF2skTV22x4DGP8ZZO4V5HkY2AwgzydCS214nKenvWPrPkncfZrmUkRPk1tlkuJtfBsKjMoDBrK9bBElyfAZcwI0w6xpZ0GFmE9ZK7lh-AGzPm_VEGyTV_yeZaCOTRfJLGUeEaoqU6gWN0ZbH4Vy3aSYHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4045b92706.mp4?token=PmZsI-J6C4dqC3JHzOGUHUCKr5erwgnphxDIyTlKg27Q-oNupSs2vpWldXe0QZarB6hByrBCrgrP4Y0eLcIuPM_aM3MR_YBXzZdw4gQYjLomUKgdJYXx0kOp4E5wdEPZru3NoH-ldbCBDAJU79rulRUkqrJMVu99_vhDSvhOGJwhWz-t8BtfCqeEvW2uF2skTV22x4DGP8ZZO4V5HkY2AwgzydCS214nKenvWPrPkncfZrmUkRPk1tlkuJtfBsKjMoDBrK9bBElyfAZcwI0w6xpZ0GFmE9ZK7lh-AGzPm_VEGyTV_yeZaCOTRfJLGUeEaoqU6gWN0ZbH4Vy3aSYHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش بهمن‌موتور برای تغییر کاربری ۱۲۰ هکتار زمین کشاورزی
🔹
گروه صنعتی بهمن طی ۶ ماه اخیر ۳ مرتبه برای تغییر کامل کاربری یک محدوده ۱۲۰ هکتاری زراعی در جوار روستای دانش شهرستان قدس تهران تلاش کرده است.
🔹
طبق گفته شاهدان محلی این شرکت این‌بار به بهانه ایجاد…</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/446808" target="_blank">📅 22:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446807">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎥
نریمان پناهی فضای مصلی را عاشورایی کرد
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/446807" target="_blank">📅 22:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446806">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0764895667.mp4?token=BsOE_YeI9uH6Ir6XlU6RF-91ya0cnfGG3wM6jDKNbMxWCv0DrV5Q0seGYxVyi-F0AgZB5e1OSTuyveXLGevT3sp-ztj7YtHdDsu6kPRTGsVIycPls8iT1Jp0IRWI7tOXxi2B0XWl2t05w6qeH6Kyebxtid9XIj-3o9taVAwJGcOAhbIrZBNSGWCPNU-HquyS6IDM6dDzOCD4MBvENDWKQkXBNravB2fxnW_yPdEvZFB1f6fiE8xseqW90sHKWBQ2NhrDz5pPCFwzNzXTX1fHOPyteQbzQSuK2EbNz_Ib2NYphZdMZJnFtuIzwlw6cpa4jg5BH2v2djXHylPz9FwSrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0764895667.mp4?token=BsOE_YeI9uH6Ir6XlU6RF-91ya0cnfGG3wM6jDKNbMxWCv0DrV5Q0seGYxVyi-F0AgZB5e1OSTuyveXLGevT3sp-ztj7YtHdDsu6kPRTGsVIycPls8iT1Jp0IRWI7tOXxi2B0XWl2t05w6qeH6Kyebxtid9XIj-3o9taVAwJGcOAhbIrZBNSGWCPNU-HquyS6IDM6dDzOCD4MBvENDWKQkXBNravB2fxnW_yPdEvZFB1f6fiE8xseqW90sHKWBQ2NhrDz5pPCFwzNzXTX1fHOPyteQbzQSuK2EbNz_Ib2NYphZdMZJnFtuIzwlw6cpa4jg5BH2v2djXHylPz9FwSrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار تانکر سوخت در آمریکا
🔹
پلیس شهرستان مونتگومری در ایالت آلابامای آمریکا روز شنبه از انفجار یک تانکر سوخت و آتش‌سوزی در محل حادثه خبر داد.
🔹
این انفجار حوالی ظهر به وقت محلی رخ داده و علت آن نقض فنی اعلام شده است.
🔹
این حادثه منجر به قطع برق چندین خانه در منطقه شد. پلیس از مردم خواست تا از ورود به این منطقه خودداری کنند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/446806" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446805">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cc42a03c.mp4?token=Ib-s6e0SxCav5hMFIXzCdJ9Sq5qulpRL5qB1Oxv-_pHxZo0x42tiBmAA5t1-XgR90UvQYnZ0YkHu7Nh5q7QoUeTjdmtS8DHRVmv31H-ysK6TE3nu_U4-nltp3odumyy20Q9GI9wEaz4sZSrLxFzu2rKpr7jA5a3Ma1eF3PeLcWQe8VZ3N2MX4sWghasqD3j4A_1udnCuKJfFcVs68KsaPbVVOJrdYngcdU8M-l2IMAxuZ9dfbDSebq4rhS6lpac2HhPdtMFj3OdlXDfAy-xZ5Zo-VI-VavvTfcC7J8dCqVkeSPr9Gv_flbGmqSRcsjwNEMugoE6hw4h1Pbed-dozM0aBjjFnd2LdfagX7SMZe_AgE8l6kKNyuGHMCeHLV7IA3NKKPd2YcImlYO-dol55N9EUA3FH1BHvakDQLj47-qQ3FPO_iYuuNtyFGjnaIAqxOkrZ4341uKJqYTb6VWGvtCJics0UXl3t51B2_nPyfTAkNrCmWLgMBRq68xEqCaexVxErNmvTYAVbWiZy8vBhkCL34OuuBbOIDTWdaS5SANCx-Ox6NR8Luo07v_q_eYwchiliCBVXoV5PtnBJCopAPzeOqM_Vfh5FUGqP8eEaLr0vJlQdh5VbNCs3GYo-FkHMALyTWZcne05a2p4dTVBDqTCzAOqpqBTOCXzMJ5issco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cc42a03c.mp4?token=Ib-s6e0SxCav5hMFIXzCdJ9Sq5qulpRL5qB1Oxv-_pHxZo0x42tiBmAA5t1-XgR90UvQYnZ0YkHu7Nh5q7QoUeTjdmtS8DHRVmv31H-ysK6TE3nu_U4-nltp3odumyy20Q9GI9wEaz4sZSrLxFzu2rKpr7jA5a3Ma1eF3PeLcWQe8VZ3N2MX4sWghasqD3j4A_1udnCuKJfFcVs68KsaPbVVOJrdYngcdU8M-l2IMAxuZ9dfbDSebq4rhS6lpac2HhPdtMFj3OdlXDfAy-xZ5Zo-VI-VavvTfcC7J8dCqVkeSPr9Gv_flbGmqSRcsjwNEMugoE6hw4h1Pbed-dozM0aBjjFnd2LdfagX7SMZe_AgE8l6kKNyuGHMCeHLV7IA3NKKPd2YcImlYO-dol55N9EUA3FH1BHvakDQLj47-qQ3FPO_iYuuNtyFGjnaIAqxOkrZ4341uKJqYTb6VWGvtCJics0UXl3t51B2_nPyfTAkNrCmWLgMBRq68xEqCaexVxErNmvTYAVbWiZy8vBhkCL34OuuBbOIDTWdaS5SANCx-Ox6NR8Luo07v_q_eYwchiliCBVXoV5PtnBJCopAPzeOqM_Vfh5FUGqP8eEaLr0vJlQdh5VbNCs3GYo-FkHMALyTWZcne05a2p4dTVBDqTCzAOqpqBTOCXzMJ5issco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به رهبر شهید ایران سلام / سایۀ سیدمجتبی مستدام
🔹
دودمۀ امشب مردم ایران در مراسم وداع با آقای شهید ایران.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/446805" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446804">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174a13c993.mp4?token=CP67thvSsRUDxI8-cIAc_aWMqbzp_M3_YGPOr_Z41kk491gi5oqKWf20uobBeiXLnPp1mLHG_MnIoI4hIuIuEoq2r5HTtrf1lVQHZsBgM_Rbmd-WAnytKHLMgtc2VB3H2HY1T7RdRhsDOfkFkagpbrR_VvWvkOhbPhVfzQrnwE7kVJo-_KhO1dnqQT0OgsxdCfrwY1FvtAZtqLU76cKcG56pkeNhyf9AvSNlFZBZ8-6eydrFSaTFfmSSzPFUFwY4Zm7cthfKKrn7FIZZ_GHk0-e_a0Nc1KftSaXTAx1L6V9thEFuvn1jNYcXLjwlJGWoYEN5r-VsDdOPwoJwz6yobg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174a13c993.mp4?token=CP67thvSsRUDxI8-cIAc_aWMqbzp_M3_YGPOr_Z41kk491gi5oqKWf20uobBeiXLnPp1mLHG_MnIoI4hIuIuEoq2r5HTtrf1lVQHZsBgM_Rbmd-WAnytKHLMgtc2VB3H2HY1T7RdRhsDOfkFkagpbrR_VvWvkOhbPhVfzQrnwE7kVJo-_KhO1dnqQT0OgsxdCfrwY1FvtAZtqLU76cKcG56pkeNhyf9AvSNlFZBZ8-6eydrFSaTFfmSSzPFUFwY4Zm7cthfKKrn7FIZZ_GHk0-e_a0Nc1KftSaXTAx1L6V9thEFuvn1jNYcXLjwlJGWoYEN5r-VsDdOPwoJwz6yobg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن محمدی‌پناه، مداح نماهنگ «باید برخاست»: ما مدیون آقا هستیم و نتوانستیم حق ایشان را ادا کنیم
🔹
این داغ هرگز در دل ما سرد نخواهد شد و سوخت موشک ما برای حرکت‌های آینده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/446804" target="_blank">📅 22:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446803">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699642a8c6.mp4?token=WtM1dx-Yfew3uJf1TA_i_oShdcgO0bPcQkw9SO_KLvxqIlncdNn00H1m96jo0hbcuPrh4kP0TwAnbkWQnGvfZPipD7SjONKecUuZ1nVgsWONqJU72wDxovWrL3GnFX1UF5kznDeZ9uXBPrYKA1-uE2frOIzDzOtt0virFU1cWUEjNT3nr3srwAYDYO2A7LvMqhvmmVeq4MIEvtrRepOi3biFPgqSmeIrceSI_SyM6qJ9cppl2oO7kEQgZuatF8cgGfU_1WnVbHzP8rLjjQCFoLiw7a5itRC64gVQbQ3tSRM50Rz_XcsG6WzWeoQCBEEdKPy9ZRO4h8rnf8NoXzNz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699642a8c6.mp4?token=WtM1dx-Yfew3uJf1TA_i_oShdcgO0bPcQkw9SO_KLvxqIlncdNn00H1m96jo0hbcuPrh4kP0TwAnbkWQnGvfZPipD7SjONKecUuZ1nVgsWONqJU72wDxovWrL3GnFX1UF5kznDeZ9uXBPrYKA1-uE2frOIzDzOtt0virFU1cWUEjNT3nr3srwAYDYO2A7LvMqhvmmVeq4MIEvtrRepOi3biFPgqSmeIrceSI_SyM6qJ9cppl2oO7kEQgZuatF8cgGfU_1WnVbHzP8rLjjQCFoLiw7a5itRC64gVQbQ3tSRM50Rz_XcsG6WzWeoQCBEEdKPy9ZRO4h8rnf8NoXzNz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در مصلای تهران: ما همه خون‌خواه پدر، گوش به فرمان پسر  @Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/446803" target="_blank">📅 22:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446802">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c9ff5ee.mp4?token=iszYpICYklpTY0shg2mHcPouqcHAd902yofJ9ExlQlQHY-Iot6d9rNo23D-c-_3eiwwuM9SWoj_rtKsPJaLG1XzEmONGdhquXr4DBb451y-Vruf1j2NsIHbQHkRHLa_ujzi7CP1uSfkUXIx8N3vwHzdKrL4xzquX9PqhhmJY2UtFjwSauXzmYgt5bWL7s7AvQoB_vq55OpxIXgv7gG2nIn1yCd-Sjk-5bp5OlQbjwIDr359nJLNHQ6cvejOBnCi3yiCEpp67MusaokV2_tk-B7c1xVPkr4JBLCklTrOstZILcE7Aq4DkDGnVO6gIUH9RJsXEQYkhb4zvc2tUBKYRmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c9ff5ee.mp4?token=iszYpICYklpTY0shg2mHcPouqcHAd902yofJ9ExlQlQHY-Iot6d9rNo23D-c-_3eiwwuM9SWoj_rtKsPJaLG1XzEmONGdhquXr4DBb451y-Vruf1j2NsIHbQHkRHLa_ujzi7CP1uSfkUXIx8N3vwHzdKrL4xzquX9PqhhmJY2UtFjwSauXzmYgt5bWL7s7AvQoB_vq55OpxIXgv7gG2nIn1yCd-Sjk-5bp5OlQbjwIDr359nJLNHQ6cvejOBnCi3yiCEpp67MusaokV2_tk-B7c1xVPkr4JBLCklTrOstZILcE7Aq4DkDGnVO6gIUH9RJsXEQYkhb4zvc2tUBKYRmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از حضور باشکوه مردم در مصلای تهران  @Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/446802" target="_blank">📅 21:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446801">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb4f1f81.mp4?token=NlO4bsU77UxRLObKbfanonr2p8QT9ZxaHMf4t3WiflN2DI7har644cvWR28BOZUjY-27KhL6bnJdqSIX2WU4WIjpf5_SbeSzbxQD074kNNC2b_PrKB_Q6TrLYf99F_21LzMu7PW8oQCFWpS9Zda8V76E1P2EujBvhRXKhsYTszzX5zp8rVTvE659EJg1CFv1-Dul6UeYTKPZJBFfjvWRqkdc0JXrOULA9IVCyibWU2b0xZfLV9u5RRhZrF6SaZX3dUz8Yo06yz_-9qQ1YYreDRmjBbXGKXyW-CqU-Ch2hB9iCw9M0DaFwIFiMQBU_AudX9OLSK9WHwb2u0D1m9HOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb4f1f81.mp4?token=NlO4bsU77UxRLObKbfanonr2p8QT9ZxaHMf4t3WiflN2DI7har644cvWR28BOZUjY-27KhL6bnJdqSIX2WU4WIjpf5_SbeSzbxQD074kNNC2b_PrKB_Q6TrLYf99F_21LzMu7PW8oQCFWpS9Zda8V76E1P2EujBvhRXKhsYTszzX5zp8rVTvE659EJg1CFv1-Dul6UeYTKPZJBFfjvWRqkdc0JXrOULA9IVCyibWU2b0xZfLV9u5RRhZrF6SaZX3dUz8Yo06yz_-9qQ1YYreDRmjBbXGKXyW-CqU-Ch2hB9iCw9M0DaFwIFiMQBU_AudX9OLSK9WHwb2u0D1m9HOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فقط همین خبر آرام جان مضطر شد؛ پدر که رفت پسر جانشین و رهبر شد
🔹
شعرخوانی امشب محمدرضا طاهری در مصلای تهران. @Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/446801" target="_blank">📅 21:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446800">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5762c89eb4.mp4?token=vq0qU7Xp1oT1uaA8lPeLIR9pfDnDHhv9f2QV_G6uwL9FbgnNHv5qMO7KjudlJtJRKKbwQRkWivPWSivvl2xdjs4VwxLvri2YyXOwP4yGJTndpAfuVKLNLMAyd6cpHlvsel15Wd8KnujAR3PG2RADY4byLiIzsFv_Puhmu9kWoAWdr8r2tNU7LG6CXclKG3D22bapCiTmnynMHtyssuxsX58nZH3NZZKymc-KkUUOkVbbbpyd3jlV18UoGBAxrPy_rA0p2N5dfEZw-1s8EAkvHmnZ4mn9Aen58FLKVItLP6YAbbIi77W5tFYznARC2cWZc611zThOodpxvYwESXFkrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5762c89eb4.mp4?token=vq0qU7Xp1oT1uaA8lPeLIR9pfDnDHhv9f2QV_G6uwL9FbgnNHv5qMO7KjudlJtJRKKbwQRkWivPWSivvl2xdjs4VwxLvri2YyXOwP4yGJTndpAfuVKLNLMAyd6cpHlvsel15Wd8KnujAR3PG2RADY4byLiIzsFv_Puhmu9kWoAWdr8r2tNU7LG6CXclKG3D22bapCiTmnynMHtyssuxsX58nZH3NZZKymc-KkUUOkVbbbpyd3jlV18UoGBAxrPy_rA0p2N5dfEZw-1s8EAkvHmnZ4mn9Aen58FLKVItLP6YAbbIi77W5tFYznARC2cWZc611zThOodpxvYwESXFkrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر حسن ابوالقاسمی: بمباران بیمارستان‌ها و کودک‌کشی‌ها و افتخار به آن توسط نتانیاهو نشان می‌دهد که دشمنان رهبر انقلاب چه کسانی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/446800" target="_blank">📅 21:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446799">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMKul-UQ8pLaXjXuMYtvuoCpOZp993jV6S6OAQ5LcJ6HtUkzAUtIQ-1PP-wmn6KluuKD-YgEjWoNCNmblagmFccuarcvJLLZhoZaxJiGlKzYJyZ24vg14iW0DvY6msJu8Am9sxcfEl2LTZRLRmPWTBR5YDrnpgd8aJ0kQX13avD58fGtdKxKQ8DNHP1bLXw69anlxXjACjXhxu-x193lksLcpffy7Gxhd2evy779oNrYWK9UmQx9kZvW3lhgstw3FnvnpvNAPsBXO7g3odJbQWuuNifTuS3hIIXESLeGxm1Z9RzHIoX9plcu7Y5wHiEPt-6a4Igw2R-f6rqv3NrbwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بأمان الله یا شهید الله
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/446799" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446798">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/578d03d029.mp4?token=bDpPYDjz3mVH8pAAzHZCIIJ49IM2hG4Sx6lmuepBRtRngshMzoyHC_kdZH-Y2F820sX8fOsRcerngwzqsNLo0uU1-6ObaHyJsSHVGOXHS3XULwTs9i8u8FBYP_BwRvplpAgVeQiyc5BXAAe2mYznNyp-0z36u8A5gDg29y7G215bmojzkmTfQeMPCMOC1CDuY4gjY2GgR2HjN07qBzOBCy6gaBkYWe6zN9WDJjwrRa6_rIlCELTluApVuGDoMfCeFakAZELV2Ooc8LwvhREadUjVR4dICPBMZoPiGF7rl1wG3-8vfS2KqtEly_GsuJrL9lxl1Kh4PC5hEBDobo5sT2ZkmJ5iaaU6ruB6JP4xQuEthRRXqDQcMHzQEjPQjL9if4GnJSFNl__-kFgdxTCQmgFTEJhXMesqedqQ2iASKG2q2rR9UgmA5W6rrh-chc6UN-cqw4RID5aUqHghEJaVFmSgvUXBLXKGXL41jSFdfCoOrtmhQs9x0f8HmaCUHicgzobqHUsVjon_W21bIMYNUAHyL1BpAMrGm_sNhhaJA26eQTmJZUH9R6CQRMRRijryowP1SWaBjatdmOpO9dZQeVRwZxy1-BSKSDo-S7DtuhyCB9PKX7fR27q3H32IykZgWFCmywLNwJuMB6PMgShusMRvjkIjK3QZm9QCwvvl2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/578d03d029.mp4?token=bDpPYDjz3mVH8pAAzHZCIIJ49IM2hG4Sx6lmuepBRtRngshMzoyHC_kdZH-Y2F820sX8fOsRcerngwzqsNLo0uU1-6ObaHyJsSHVGOXHS3XULwTs9i8u8FBYP_BwRvplpAgVeQiyc5BXAAe2mYznNyp-0z36u8A5gDg29y7G215bmojzkmTfQeMPCMOC1CDuY4gjY2GgR2HjN07qBzOBCy6gaBkYWe6zN9WDJjwrRa6_rIlCELTluApVuGDoMfCeFakAZELV2Ooc8LwvhREadUjVR4dICPBMZoPiGF7rl1wG3-8vfS2KqtEly_GsuJrL9lxl1Kh4PC5hEBDobo5sT2ZkmJ5iaaU6ruB6JP4xQuEthRRXqDQcMHzQEjPQjL9if4GnJSFNl__-kFgdxTCQmgFTEJhXMesqedqQ2iASKG2q2rR9UgmA5W6rrh-chc6UN-cqw4RID5aUqHghEJaVFmSgvUXBLXKGXL41jSFdfCoOrtmhQs9x0f8HmaCUHicgzobqHUsVjon_W21bIMYNUAHyL1BpAMrGm_sNhhaJA26eQTmJZUH9R6CQRMRRijryowP1SWaBjatdmOpO9dZQeVRwZxy1-BSKSDo-S7DtuhyCB9PKX7fR27q3H32IykZgWFCmywLNwJuMB6PMgShusMRvjkIjK3QZm9QCwvvl2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر رهبر شهید: قیافه‌ام غلط اندازه ولی دوست دارم شهید بشم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/446798" target="_blank">📅 21:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446797">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kORR6Dom_SSUXdTLK4i8oznSULhbkoJhSfz6ezoz6J-KFj541xOcx6DQhFwU1IjVO1Yw-F0MS1W6T-SJKprZ-NEbuKFaoByf6zOQIkIJKVdaz7zJAlMF8PqRr130WGDBvSjO27VoBIGAZtuR3ehhYlU898AS1Cn0Hr_UYC4R0pTaJkM7oRCUkkZJqctrV9W8dWoA2nDLV0ysNXE2iAvhwM7A9qlSxDQ8Fy_c9gh4Nv6V9wEYoeNQPIj5lU2mibBiHQ25vxoi1UdSkVFUxTY2wElMvLNDFKw2jcaOPClhDXSgKdN9Zo9VLgS_n-ZxO7G-THV6rXbn_ZdjYBIcG9Nrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🎥
ستاد وداع با رهبر شهید: نماز بر پیکر مطهر رهبر شهید انقلاب رأس ساعت ۸ صبح فردا در تهران اقامه خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/446797" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446796">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dcfc0ede1.mp4?token=qzsIzbKxqPFm5O7QLTvKTe7L2sK6v5pmCiRsub6Wgf5aB1CFdCi3S5y4EukswFnHLOtg-AwJWjjv3x9EBIUBKv3opCX_TrtAMtSotzpZANgznFYoH2sg_xMip2gwvoHgLGspuhm9faEDvuRTTHxSQuS1pbji9jj5kOeT0PTpJ9OP_QGVPRa8CnDkh_peC94d04BqjKBNm_U6kP9NO8umFqwoHVFFYy7ZnPPnBEWWxBGPRupWiuPnveMNlzhEGnlGpUqV9NGY1PBiyMXPK5B33vYXbjqF5tdjhaAOFEPLtOXOSc2dQbzLDnUqIcmHvxP3DUNoWQxWRXRozKjiCMEdrS2UzdeA6LJiMQduZ-wv12lMDgx6mwVvd_a7uc_skEaHr39uBXrMSH88P5QfdQm_VN3KeoFp8CFpl2A2n0rgaB3_W7kAbMUw4ij4oRKu_8_ozCSi4f1xckV9sKteblX3zXYRBLDWZ3HfKKLLooO3k9sMyuwEHN51Er0IbhF3MFWTEIJTQAe4VCzNx3hwmrJt2t_Lts9lOVARdyJW-aucbZlzHMkv36HQx_eFA8cH1UFdY9U2vhmr8WPN_yKNDNZpE_0pX6lJgOHjUgPydCPGGcFYUk7UK1ROGZPkGSovnpBGbjX3PWgx99aJ6m6R-jYYUQng0-N01lMQXUmD6gRsD7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dcfc0ede1.mp4?token=qzsIzbKxqPFm5O7QLTvKTe7L2sK6v5pmCiRsub6Wgf5aB1CFdCi3S5y4EukswFnHLOtg-AwJWjjv3x9EBIUBKv3opCX_TrtAMtSotzpZANgznFYoH2sg_xMip2gwvoHgLGspuhm9faEDvuRTTHxSQuS1pbji9jj5kOeT0PTpJ9OP_QGVPRa8CnDkh_peC94d04BqjKBNm_U6kP9NO8umFqwoHVFFYy7ZnPPnBEWWxBGPRupWiuPnveMNlzhEGnlGpUqV9NGY1PBiyMXPK5B33vYXbjqF5tdjhaAOFEPLtOXOSc2dQbzLDnUqIcmHvxP3DUNoWQxWRXRozKjiCMEdrS2UzdeA6LJiMQduZ-wv12lMDgx6mwVvd_a7uc_skEaHr39uBXrMSH88P5QfdQm_VN3KeoFp8CFpl2A2n0rgaB3_W7kAbMUw4ij4oRKu_8_ozCSi4f1xckV9sKteblX3zXYRBLDWZ3HfKKLLooO3k9sMyuwEHN51Er0IbhF3MFWTEIJTQAe4VCzNx3hwmrJt2t_Lts9lOVARdyJW-aucbZlzHMkv36HQx_eFA8cH1UFdY9U2vhmr8WPN_yKNDNZpE_0pX6lJgOHjUgPydCPGGcFYUk7UK1ROGZPkGSovnpBGbjX3PWgx99aJ6m6R-jYYUQng0-N01lMQXUmD6gRsD7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فقط همین خبر آرام جان مضطر شد؛ پدر که رفت پسر جانشین و رهبر شد
🔹
شعرخوانی امشب محمدرضا طاهری در مصلای تهران.
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/446796" target="_blank">📅 21:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de484748bc.mp4?token=JWA2hy_h_VrD3uD5qfJI7aPD5g3GMyoylZ6yeaJiRFkN1MITq0fvvDurfWDd9-ZR0CdjhSNbDQBbTNg8p_80tEULLHuHGIB0hEFVe8mAmgk8JoC-c-A0jZhlPXJdRK0mSGoRc7s8-jxewFPjaI2-vaHdjzer6YzmIysHnFn85e4iCLVYsMjV2kAn5ZcebnfpYXXPjRks8HJg4_QB8LKlaFnfoYSbktfdflvn1RUj9fc_u_gnnWxo5HdxNyqQ-IcXADzW67o8XSLRVYw3PZtKt99aRXEBeQJPW1QWwEYcdoflFR0ReehLR7ZwMkOfUk-xyOcQiH_KfjOmqptRRLDvig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de484748bc.mp4?token=JWA2hy_h_VrD3uD5qfJI7aPD5g3GMyoylZ6yeaJiRFkN1MITq0fvvDurfWDd9-ZR0CdjhSNbDQBbTNg8p_80tEULLHuHGIB0hEFVe8mAmgk8JoC-c-A0jZhlPXJdRK0mSGoRc7s8-jxewFPjaI2-vaHdjzer6YzmIysHnFn85e4iCLVYsMjV2kAn5ZcebnfpYXXPjRks8HJg4_QB8LKlaFnfoYSbktfdflvn1RUj9fc_u_gnnWxo5HdxNyqQ-IcXADzW67o8XSLRVYw3PZtKt99aRXEBeQJPW1QWwEYcdoflFR0ReehLR7ZwMkOfUk-xyOcQiH_KfjOmqptRRLDvig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از حضور باشکوه مردم در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/446795" target="_blank">📅 21:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446794">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e8c0f03e5.mp4?token=UT_bb6poMy7NFDY8GTPz7paux7BH0v7Frzd1FMU7uk1L_SxmToXUcmyiaDujpjwvWKwuhCQeUaztivBD3xjGM7Z7HKBz2SOJVDEbQITvmXmdlJ9vSTSfq1CyD6UhGmQiLd_t7sknK6s-C-FhXZvVnorQiM6ZFMZtp1E4muQjzc67r8iLMxvL_gfOI-5J8FD2-GS7wvuBanRudx_isoyfFOytpdA42WYUqnbNH0EEWLo2XwVihnq-bH_SG9ttAPoKa6zYXAsy_LhoM2nBUgCEirrni0UbBik33Bs67p0JjNgvyNo4edU-3l18xohpRwDlOZ5trF5eBfEoG9dPt_Zziw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e8c0f03e5.mp4?token=UT_bb6poMy7NFDY8GTPz7paux7BH0v7Frzd1FMU7uk1L_SxmToXUcmyiaDujpjwvWKwuhCQeUaztivBD3xjGM7Z7HKBz2SOJVDEbQITvmXmdlJ9vSTSfq1CyD6UhGmQiLd_t7sknK6s-C-FhXZvVnorQiM6ZFMZtp1E4muQjzc67r8iLMxvL_gfOI-5J8FD2-GS7wvuBanRudx_isoyfFOytpdA42WYUqnbNH0EEWLo2XwVihnq-bH_SG9ttAPoKa6zYXAsy_LhoM2nBUgCEirrni0UbBik33Bs67p0JjNgvyNo4edU-3l18xohpRwDlOZ5trF5eBfEoG9dPt_Zziw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش صدای دل‌نشین قائد امت
و گریهٔ مردم
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/446794" target="_blank">📅 21:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446789">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcDhE1tpALIxVii9Ww-2pugHFexTx1ziqiq3FYnUef0uFgvh0ymgrv5gryAnYH1ogkO6hjMSZ7TRI5JwGYU8Bzvz-m39G8r1tJrmYmNXduM4GMi3BqnRN87IoMnyBv49vb-MGVygwjpflD6aBu9fuFCpSBNZxvzVdIRDIDnKrp6Vfg00rTQ_1XWzdSVEyEQor2VrEICCs6Fxf0-MIsj5JTZqMdIS_7koeIL3FlJ5llfn_g4UcdOSIl0_cN8Zec-p2zy3NYClxao4_aVppYMumwcXo76TcU8X6Me6F_u-sfVrdrU3jE81NIodHZ7iIAh6K93dU8bBPJ6cet1i0MkRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YipwaviyE50WK_ectPhUCSZkR2KlsY1bqJuj_IZ02AKzUiwMT7dshh4V-RtgD_jFi5A6kxTjcDYbPRmQ9O_wqSNN3aGKOQe-o9esIjudDcingL0XVFNEbe0FvgnsvSL3FifFhmwWMi1QtBc-FVOXI870Pi9UXXqJhCUrgUDt6nmpu6sn0UZWUYjR9TJLHIKr17BiAI6bRj90VpQvy6A4IwSRIyG2_PZkbiNJ4xOxunI8yh14Jgla0ZuRpLGspSzDbCh2UhNA6dWrCu8BCR-LCFc0w_Wf0zQff-oWqYEeAckJsJZbktffspyUokLv_enYi3XjbmseKDfNrX2_BuIWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvViTeiJn4qutlZG09M29EEuk2M2VAKwdGG6Ha6wr_30jp5v6irOcKAyAbw1NLZXREUlEII3aJjaNzIXQ1a4u_QV15b9X2G5OVNLs5XCg94lvj502FmQNxiRov5IyC6HPsHi9dJS9ZXeHXbAKBCxyaZ4-AUt-r4Ge5H0lY67I3s-BAjm7Vj5NY0fDsrbqPRMFDKcu-PvV1RFZOA_fIMzu5XzaRWSaVcAAIc2WrzbPgqnlzOaF375DpS-Vbx58LGdh526Q3sMfLeSEQhmoGBCxoAtC0Qpcxu4LpeDk8auMX5x0jkbqxaTT-u6AZY0R2rmW_QffE70-t-hjrXJ8QKrLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iImp_dI_6fSqbhG7ogpi67W-7WctoFJNfFiYMtnsi4FwEk1heoLZ_Z7_F3dK72B4XdYxwtCyb9L9pPExNs7JZLyrlPXjQ80wm2eb6W2wpg3cPEoq_sU9_U0yRte-lcoV7bevNR06eXlBHJvY2zQ33m1TXQYARw74az4rrE2BpL1jFlNC5IWUEQulmeOzhX3vNxsrj6tslOTcfvuRCWh95Hc40tAglA6y64fBB05WoQqMmKGxHqxt2vfdMm5iVzjSz7hcu2g5NIhFCT4KO7Pkm2MhuzQTNH06nwQeQPSfRRAdR_EAPBDPMiPI28afanIOdYFlyv7XmLf1AsYKCFn4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPuH3BiwrA2SS20PicfcrHIE0olN0rfDMkOJ2sD6JkPXCLfmKhmiLxx5H5EseADyeEvjpb79WMrdN5PyLtuKWxvPi4cZVxoZHRKECgVcNbUkFU8znrjSgN9pqImzBgff-SD3hQC-y3Oc9GvfGYLGyyWzF0Pv5zR7-OrfdkYsq954wm-TdTKL8vrchTxjBGeAvAOgDCvpbGrmckFRCpIoBwvckUMyJ2UL90q4RnE-1T3cPPQzr2Pna49mpwq7NI9AXQpv7iVFVFVFgGBe_XMWb3J_vnumP_Y9x9HXUSZYWFDTN9ZRMRM0wGREeIwAt9R6PSY4Fv-u07wKRQRiAvQWOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر خبرگزاری الجزیره از روز اول مراسم وداع با رهبر شهید در تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/446789" target="_blank">📅 21:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446788">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔰
موکب خدمت در مسیر «آخرین دیدار»
🔻
موکب شهدای وزارت صنعت، معدن و تجارت برای خدمت‌رسانی به شرکت‌کنندگان در مراسم بدرقه و وداع با رهبر شهید انقلاب اسلامی، با همراهی شرکت ملی صنایع مس ایران برپا شده است.
جمعه ۱۲ تیرماه ۱۴۰۵، وزیر صنعت، معدن و تجارت به‌همراه مدیرعامل شرکت ملی صنایع مس ایران و جمعی از مدیران حوزه صنعت و معدن، از این پایگاه خدمت‌رسانی بازدید کرده و در جریان روند آماده‌سازی برای میزبانی از مردم قرار گرفتند.
🔹
این موکب در روزهای پیشِ‌رو در حوالی میدان ولی‌عصر(عج) تهران، برپا خواهد بود.
◀
️ لینک خبر در مس‌پرس
@mespress_ir</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/446788" target="_blank">📅 21:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446787">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGguYkqIHGxN1n3OrepGcMW9SObEH2JoC8zEOS9pR6tTzCyLhicLENppPK92WcjxpBpPGtu1IoKMDFnHYEjnIATh7WQ0Y2K3CnkA2Gf9PNnx-jTv6MGZ-qhmz34OQyKf1xVUUV84kI4mZFdXqYGccnwU4IP6Ikmz4YWI9O_jULKO73SwphM9j7xITIT445VKB9oe3dISyKseOgtqAfDgty76C2ZmKI-GtCUKGulQq5mujwGi5_nC5QLNJm8DvdJIJLSima5VslbqEczp-9lXzPhohCjhenRgQpgyQtO_wOkecJJpwBBdrwcdaKrXhi_vax8NcOT7ws-HQFPhlTrK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/446787" target="_blank">📅 21:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446786">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/446786" target="_blank">📅 20:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446785">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117b776f6d.mp4?token=HOHObq32y3zy5XVjrKHVjYCTtX-8SrCpOEg7JN_51F-jo_Ngf2SlPFj8zdZzXPjUQU7pmbwh9NY6qsSdF9xYap9Ji5rozQtc8CwW7pRd07AN4K5T3rEyYmBjI9YcJKLCMwzPolUNWwlgj7uM9NaDuOWX-PTKRUfeP3AqhVXLMQvCoVMF5dI_MqsLmpGeCdOLf63vxVM_9kMXwmogfr2xqiKsQrUByuzIShBUobk56Jify_BjHxjjk61EEn1TuEVO8FjVna0ufx_-RhSxbXchIggyHDBwjwOzSNKQa7wgnJfbsAScEwsRexbvFdKcJh1ACg_fe2Rwu9iyC58NutTZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117b776f6d.mp4?token=HOHObq32y3zy5XVjrKHVjYCTtX-8SrCpOEg7JN_51F-jo_Ngf2SlPFj8zdZzXPjUQU7pmbwh9NY6qsSdF9xYap9Ji5rozQtc8CwW7pRd07AN4K5T3rEyYmBjI9YcJKLCMwzPolUNWwlgj7uM9NaDuOWX-PTKRUfeP3AqhVXLMQvCoVMF5dI_MqsLmpGeCdOLf63vxVM_9kMXwmogfr2xqiKsQrUByuzIShBUobk56Jify_BjHxjjk61EEn1TuEVO8FjVna0ufx_-RhSxbXchIggyHDBwjwOzSNKQa7wgnJfbsAScEwsRexbvFdKcJh1ACg_fe2Rwu9iyC58NutTZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احترام نظامی مردم هنگام پخش سرود ملی
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/446785" target="_blank">📅 20:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446782">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApjDbfpYGoAU9xKiRecgCwNLhobsMCt8PigiEJYNjQ1S8CoSU32pTAIZ_sj_JxPrJJmjsNxR4KyM6wnIBVpOATDNMiIlANeTh_0Np194NqUzpVY643i63rOtBlJLh4wQPBHC_Iq1k_s5bw6hFkjIS0WdWTwZbMiTA7sCbj64pAc23VVbDl7tUKjstzYSACIU3wCdM2xatBuge__yjBH5YkhoL__eHAacGM4HgiwcRJuSc5mg-YgdnaKqDKNc1xJ4iN-qxKnDXEyoBO83FTQYXGYkkShOsZ_T3agSMUO0x8ubS6ugxdEWQcBPycmYaMN27Xfy6NCZHpz7Wj0HJICpXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: از دیدن گریه مردم ایران در تشییع [آیت‌الله] خامنه‌ای غافلگیر شدم؛ چراکه فکر می‌کردم مردم از او متنفر هستند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/446782" target="_blank">📅 20:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446781">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea15c58a8a.mp4?token=F9c3p6LjuGydDxXqcJJyJi-bcv-06O-0MQwsxqUBiMB_koF9wQGHxzfuKmKhyj-eafBYOnOJcijai6yY27GEtXDesGDaE0zxXDqmwI5RBm7atF1jhM5K2qge8whmOSaV6TDg0laSJW4m8QbKO3q3STJD2WTSHB1wIwOOfWKDuZUOIEWYjLEaZJ-hIm2B1ueSX-wFnJxu1kMzq7ZU0FezKMz0nSEN7VsEuz-T1hwrdts-WOC8oxSywTyay5kGa11lC50QtldZ-OOrULq1s7hCiw-7NHrdl_aQi6wcqVvGvlrXIIipZGJ6eK8OEhlo2gQRhrJUQEaO9AZcnlSKfe50ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea15c58a8a.mp4?token=F9c3p6LjuGydDxXqcJJyJi-bcv-06O-0MQwsxqUBiMB_koF9wQGHxzfuKmKhyj-eafBYOnOJcijai6yY27GEtXDesGDaE0zxXDqmwI5RBm7atF1jhM5K2qge8whmOSaV6TDg0laSJW4m8QbKO3q3STJD2WTSHB1wIwOOfWKDuZUOIEWYjLEaZJ-hIm2B1ueSX-wFnJxu1kMzq7ZU0FezKMz0nSEN7VsEuz-T1hwrdts-WOC8oxSywTyay5kGa11lC50QtldZ-OOrULq1s7hCiw-7NHrdl_aQi6wcqVvGvlrXIIipZGJ6eK8OEhlo2gQRhrJUQEaO9AZcnlSKfe50ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گریه بی‌امان دخترکی که با ویلچر خودش را به وداع رهبر شهید رساند  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446781" target="_blank">📅 20:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc2bd6befd.mp4?token=R_mPEPmCMxthIvUnNbDo7GfPA0m1OdaA6SrJyK-A3t4VrsJaXSEowNMgY0hzy2Hby31igzZRQwdsa_sZV8spO_DFDpYkOXP2jBS292kkcnS1i02se6b568u87cHDEzeHimifFGLP9s14VUBLGKNYS4rCOfR148EvhYuzu_VQ_rJG8pFNxZncFl4rrgaLRtpJh695gavjQ1aBeI4j6iDaC3hWx-nEHDr8-eJOXzeHS9k6OKzd_i78NrWsqEhWRlKf8M5r_sX8lGgi9z6gGnY7WxXBd_xytj4srHUa-qRVxr3WgDeCSZd6NvaXpHKsGf7CTPJwY2SAkybastwvng9A0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc2bd6befd.mp4?token=R_mPEPmCMxthIvUnNbDo7GfPA0m1OdaA6SrJyK-A3t4VrsJaXSEowNMgY0hzy2Hby31igzZRQwdsa_sZV8spO_DFDpYkOXP2jBS292kkcnS1i02se6b568u87cHDEzeHimifFGLP9s14VUBLGKNYS4rCOfR148EvhYuzu_VQ_rJG8pFNxZncFl4rrgaLRtpJh695gavjQ1aBeI4j6iDaC3hWx-nEHDr8-eJOXzeHS9k6OKzd_i78NrWsqEhWRlKf8M5r_sX8lGgi9z6gGnY7WxXBd_xytj4srHUa-qRVxr3WgDeCSZd6NvaXpHKsGf7CTPJwY2SAkybastwvng9A0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقامیری: مردم با حضور در مراسم تشییع، غیرت و شرافت و هویتشان را سر دست می‌گیرند.  @Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/446780" target="_blank">📅 20:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446779">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfef33bb16.mp4?token=DM7UjanzTNkcIJRBiWPdpe6x-j_PtENHoZiABrllF6yItl1-PswT0sH4AUBQfovJlB95fIlbxYBVvZE219_HsVb7xINlXOVlkMzuoCTb3hUb3_T5tUV-Su1N4oy2moY2CJw0ERUXY1BwP2x7KsFDatW1BugKp5q1AHsTlen-JgjE9gJu6dvdZ40-EqZjNk-Ny1t-StQsZ8JnreeftP4v8Ptp5bKadzkjaYMUWJw75bV8CmmYhUMIRgGso0626UmW7wA1854UIYyxIDNJMmyxvQ6TJ3hVZIOUMJ-IJ2YpJhTffKBwOMSIJeEor2wKmvsUOiQG5NHj24qCHR_TAiFqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfef33bb16.mp4?token=DM7UjanzTNkcIJRBiWPdpe6x-j_PtENHoZiABrllF6yItl1-PswT0sH4AUBQfovJlB95fIlbxYBVvZE219_HsVb7xINlXOVlkMzuoCTb3hUb3_T5tUV-Su1N4oy2moY2CJw0ERUXY1BwP2x7KsFDatW1BugKp5q1AHsTlen-JgjE9gJu6dvdZ40-EqZjNk-Ny1t-StQsZ8JnreeftP4v8Ptp5bKadzkjaYMUWJw75bV8CmmYhUMIRgGso0626UmW7wA1854UIYyxIDNJMmyxvQ6TJ3hVZIOUMJ-IJ2YpJhTffKBwOMSIJeEor2wKmvsUOiQG5NHj24qCHR_TAiFqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقامیری: مردم با حضور در مراسم تشییع، غیرت و شرافت و هویتشان را سر دست می‌گیرند
.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/446779" target="_blank">📅 20:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446778">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e2c32acf1.mp4?token=MU6ur9NHrVUk0P1-6uz8ht1O9JF1kC3UzorJdSB-BMgj4bjMTWi9U80Gs02kvwfWbzqyFuFQ0RK2Wwl0WYniJmcXkBlaAfCaAGope6sYQ9C08tX0Yn-7YG8Eb6YwvOHfd19tiRwTEJ6pPt5XEOTdT-PJOBvNEF-eYbXBAMYzaAlZ4vAzlVE5slWJokiVO5ytzthgDaNlGQjWm_1G2PyrpN-ePCS4mvMWXyfxbmDwHWOipz0iZFTXYQAkas5RcPdawPAre779n_D-F557p-19AB6VFZ3ZPqplnXH8jy4b2EEAqcGzi5JjGKJ3KI_wQ9OnQejGoYU3bwoAnm6_g72hBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e2c32acf1.mp4?token=MU6ur9NHrVUk0P1-6uz8ht1O9JF1kC3UzorJdSB-BMgj4bjMTWi9U80Gs02kvwfWbzqyFuFQ0RK2Wwl0WYniJmcXkBlaAfCaAGope6sYQ9C08tX0Yn-7YG8Eb6YwvOHfd19tiRwTEJ6pPt5XEOTdT-PJOBvNEF-eYbXBAMYzaAlZ4vAzlVE5slWJokiVO5ytzthgDaNlGQjWm_1G2PyrpN-ePCS4mvMWXyfxbmDwHWOipz0iZFTXYQAkas5RcPdawPAre779n_D-F557p-19AB6VFZ3ZPqplnXH8jy4b2EEAqcGzi5JjGKJ3KI_wQ9OnQejGoYU3bwoAnm6_g72hBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارت به نیابت ۱۶۸ شهید دانش آموز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/446778" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446777">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3AITPwbjTHCxgrd9uFYHzGJUC_lFT4sy3f95nOhqwq1h-IOm7lwQcv3YdC6GbPaqDGMPoMVWDWDJpEdVXLxbAk771riEb1bJRPVUSqMlRwLBGhtQpnZGjkx-Rv7yJqySLKHLPfVhZ-_lW-ReHLxOoQv3PkoIEkEN-DkecOztgTrihfDrdsYO0AuVho4yDVZ6TjiKVxMFng4AmYYjqwNJhHhMdWC3rq_qchZ21OhPoYrulcbMnuIg2jPv8ZBu2dIMh4tjL40Bd1k0HT2M7go1geJNx4JVGm4PqZUhmDNpGoYCSoglV-75RMcBhTnH-CSROpmbCoJuqTEbrHQH3cPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخاب جالب آیات قرآن در مراسم وداع خارجی‌ها با امام شهید
🔹
در عرف دیپلماتیک جهان، مراسم استقبال و بدرقه سران کشورها معمولاً با تشریفات نظامی، نواختن سرود ملی، احترام نظامی و قرائت پیام‌های رسمی برگزار می‌شود. اما در مراسم وداع هیأت‌های خارجی با پیکر رهبر شهید انقلاب، این قواعد با هویت اسلامی جمهوری اسلامی درهم آمیخت.
عراق؛ استقلال سیاسی و فکری با جلوگیری از نفوذ جریان نفاق
🔸
برای هیأت شیوخ عشایر عراق، نخستین آیه سوره احزاب انتخاب شد؛ آیه‌ای که پیامبر اکرم(ص) را به تقوا و پرهیز از اطاعت کافران و منافقان فرا می‌خواند.«يَا أَيُّهَا النَّبِيُّ اتَّقِ اللَّهَ وَلَا تُطِعِ الْكَافِرِينَ وَالْمُنَافِقِينَ ۗ إِنَّ اللَّهَ كَانَ عَلِيمًا حَكِيمًا، ای پیامبر! از خدا پروا کن و از کافران و منافقان اطاعت مکن؛ همانا خداوند دانا و حکیم است.»
ترکیه؛ فضیلت بالای جهاد با جان و مال
🔹
برای هیأت ترکیه، آیه ۹۵ سوره نساء قرائت شد، آیه‌ای که مجاهدان را بر قاعدان برتری می‌دهد.«لَا يَسْتَوِي الْقَاعِدُونَ مِنَ الْمُؤْمِنِينَ غَيْرُ أُولِي الضَّرَرِ وَالْمُجَاهِدُونَ فِي سَبِيلِ اللَّهِ بِأَمْوَالِهِمْ وَأَنْفُسِهِمْ ۚ فَضَّلَ اللَّهُ الْمُجَاهِدِينَ بِأَمْوَالِهِمْ وَأَنْفُسِهِمْ عَلَى الْقَاعِدِينَ دَرَجَةً ۚ وَكُلًّا وَعَدَ اللَّهُ الْحُسْنَىٰ ۚ وَفَضَّلَ اللَّهُ الْمُجَاهِدِينَ عَلَى الْقَاعِدِينَ أَجْرًا عَظِيمًا، مؤمنانی که بدون عذر از جهاد بازنشسته‌اند، با مجاهدانی که با مال و جان خود در راه خدا جهاد می‌کنند، یکسان نیستند. خداوند مجاهدان را که با مال و جان خود جهاد می‌کنند، بر خانه‌نشینان برتری داده است؛ هرچند خداوند به همه وعده نیکو داده، ولی مجاهدان را بر خانه‌نشینان با پاداشی بزرگ برتری بخشیده است.»
عربستان؛ یادآوری سنت الهی در پیروزی مؤمنان
🔸
برای هیأت عربستان سعودی، آیه ۱۳ سوره آل‌عمران تلاوت شد، آیه‌ای که به نبرد بدر اشاره می‌کند، جایی که مؤمنان اندک، با وجود برتری ظاهری دشمن، به یاری خدا پیروز شدند.«قَدْ كَانَ لَكُمْ آيَةٌ فِي فِئَتَيْنِ الْتَقَتَا ۖ فِئَةٌ تُقَاتِلُ فِي سَبِيلِ اللَّهِ وَأُخْرَىٰ كَافِرَةٌ يَرَوْنَهُمْ مِثْلَيْهِمْ رَأْيَ الْعَيْنِ ۚ وَاللَّهُ يُؤَيِّدُ بِنَصْرِهِ مَنْ يَشَاءُ ۗ إِنَّ فِي ذَٰلِكَ لَعِبْرَةً لِأُولِي الْأَبْصَارِ، بی‌تردید در رویارویی آن دو گروه، برای شما نشانه‌ای بود؛ گروهی که در راه خدا می‌جنگید و گروهی دیگر که کافر بود. آنان مؤمنان را با چشم خود دو برابر می‌دیدند، و خدا هر که را بخواهد با یاری خویش تأیید می‌کند. بی‌گمان در این ماجرا عبرتی برای صاحبان بینش است.»
لبنان؛ ایمان در میدان آزمون
🔹
برای هیأت دولت لبنان، آیه ۶۶ سوره نساء انتخاب شد؛ آیه‌ای که می‌گوید اگر فرمان‌های بسیار دشوار الهی صادر می‌شد، تنها گروه اندکی از مردم از آن پیروی می‌کردند.«وَلَوْ أَنَّا كَتَبْنَا عَلَيْهِمْ أَنِ اقْتُلُوا أَنْفُسَكُمْ أَوِ اخْرُجُوا مِنْ دِيَارِكُمْ مَا فَعَلُوهُ إِلَّا قَلِيلٌ مِنْهُمْ ۖ وَلَوْ أَنَّهُمْ فَعَلُوا مَا يُوعَظُونَ بِهِ لَكَانَ خَيْرًا لَهُمْ وَأَشَدَّ تَثْبِيتًا، و اگر بر آنان مقرر می‌کردیم که خود را بکشید یا از سرزمین‌های خود بیرون بروید، جز گروه اندکی از آنان چنین نمی‌کردند. و اگر آنچه را به آن اندرز داده می‌شدند انجام می‌دادند، برایشان بهتر بود و آنان را استوارتر می‌ساخت.»
حزب‌الله؛ ولایت، ستون پیروزی
🔸
برای هیأت حزب‌الله، آیات ۵۵ و ۵۶ سوره مائده تلاوت شد، آیاتی که ولایت خدا، پیامبر و مؤمنان را محور تشکیل «حزب‌الله» معرفی می‌کند.«إِنَّمَا وَلِيُّكُمُ اللَّهُ وَرَسُولُهُ وَالَّذِينَ آمَنُوا الَّذِينَ يُقِيمُونَ الصَّلَاةَ وَيُؤْتُونَ الزَّكَاةَ وَهُمْ رَاكِعُونَ(۵۵) وَمَنْ يَتَوَلَّ اللَّهَ وَرَسُولَهُ وَالَّذِينَ آمَنُوا فَإِنَّ حِزْبَ اللَّهِ هُمُ الْغَالِبُونَ»(۵۶) «سرپرست و ولی شما تنها خدا و پیامبر او و مؤمنانی هستند که نماز را برپا می‌دارند و در حال رکوع زکات می‌دهند.(۵۵) و هر کس خدا و پیامبر او و مؤمنان را به ولایت بپذیرد، بداند که حزب خدا همان پیروزانند.(۵۶)»
حماس؛ وفاداری تا آخرین نفس
🔹
برای هیأت جنبش حماس، آیه ۲۳ سوره احزاب انتخاب شد، آیه‌ای که از مردانی سخن می‌گوید که بر عهد خود با خدا صادق ماندند، برخی به شهادت رسیدند و برخی همچنان در انتظارند.«مِنَ الْمُؤْمِنِينَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَيْهِ ۖ فَمِنْهُمْ مَنْ قَضَىٰ نَحْبَهُ وَمِنْهُمْ مَنْ يَنْتَظِرُ ۖ وَمَا بَدَّلُوا تَبْدِيلًا در میان مؤمنان، مردانی هستند که به پیمانی که با خدا بسته‌اند صادقانه وفا کرده‌اند برخی از آنان به عهد خود جامه عمل پوشانده‌اند و برخی دیگر در انتظارند و هرگز پیمان خود را دگرگون نکرده‌اند.
عکس: محمدمهدی پورعرب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/446777" target="_blank">📅 20:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446776">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a1aaf91df.mp4?token=ZZU4ZFTMqy3DBbO64BntgchbPCM95NI8mSJzHX9ERWPh6rJEvBzfXAPFGLPyTcdaqPN_z0YviH7PMfV9FU94MmpxCqKbPSWzcV-2Esn1BloYf6OW-qXsKZEztsOq_c3VIWXdBz8-9ZEwFR3OMdo3jYfbs8zXBMADniIx5s7ITqCncsOVOJ7hgKFT3yq3QM3a3tBhIt4LVlwx46nHoGP6F3E-yKNlW-gm7JEtdg26OfSI3Ly11_uxQ6gBYVWL5hbw42F6v74dyInJG7YKdRJoNs83zNqvBhQCatWKQ3mEm6UzEFFlUnwLO6SiudwAxp32rDN1P_zIdJMpHW6XRa_Q5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a1aaf91df.mp4?token=ZZU4ZFTMqy3DBbO64BntgchbPCM95NI8mSJzHX9ERWPh6rJEvBzfXAPFGLPyTcdaqPN_z0YviH7PMfV9FU94MmpxCqKbPSWzcV-2Esn1BloYf6OW-qXsKZEztsOq_c3VIWXdBz8-9ZEwFR3OMdo3jYfbs8zXBMADniIx5s7ITqCncsOVOJ7hgKFT3yq3QM3a3tBhIt4LVlwx46nHoGP6F3E-yKNlW-gm7JEtdg26OfSI3Ly11_uxQ6gBYVWL5hbw42F6v74dyInJG7YKdRJoNs83zNqvBhQCatWKQ3mEm6UzEFFlUnwLO6SiudwAxp32rDN1P_zIdJMpHW6XRa_Q5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظات ملکوتی اذان مغرب در مصلی امام خمینی تهران
@Frans
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/446776" target="_blank">📅 20:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0dcad2aae.mp4?token=qqvyv7_uwjJVf9MCEC3FIf6JIq4PxVr-KSrDPPbkRbIMiNVQM00Gh1mdOaogFO5u2VnHgijTTzVXzxSsoYaPGzFaSIDQKNxvs2dJUaEy7d3TKCtp4HlE_gtOfALkRYrVNuMk26TNKEm7giNvo6AiMmxDe1jnUSAjyuImICjzapqTqWpls329PapL5cRgP9AKj3bt-LS9sRGyTxXZN0jvqnIM_ZM8TGLswrf2fXAac5I2FRTn1v4pq_f2UiBbW4FWVmJSOkbiPE5wxarnU7YDfGSFTLgNtv-OSD5fiDU3ZMBNLTEt0DBJCRUXiJwttoiRrDvmMbm8WAERbg9LQZpqcQxOwDnhGMoADUsVcF5cfe33fTjed12fgoLQskhkMcpYWbBTJYt2JMPYhx4JO8Rvzy68A5QDDaPktPEld20xa5cN9u22nTvny0JJFfp153pBHPwZnhp5D7PxO0wkybdoCwshiuAdATFuIOoTVrFuPPzapPhApPyOSnSE-qZ8Og2fUqy81bRFJLTLQ7QU6hfpdrRVophodZ3rbUJMmcmqyc_vCCleiwJ-2s381NLmEopww_A8YLcXPX8sfxIhV7y1RlJ-Ls_ibtfx7x3_M8Cm6CQzryf1pbIqMagdN6JccClbXvyEX6h3xRA1xU5pl4GKFoJnU1KPA_N7-E4kRAk5mJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0dcad2aae.mp4?token=qqvyv7_uwjJVf9MCEC3FIf6JIq4PxVr-KSrDPPbkRbIMiNVQM00Gh1mdOaogFO5u2VnHgijTTzVXzxSsoYaPGzFaSIDQKNxvs2dJUaEy7d3TKCtp4HlE_gtOfALkRYrVNuMk26TNKEm7giNvo6AiMmxDe1jnUSAjyuImICjzapqTqWpls329PapL5cRgP9AKj3bt-LS9sRGyTxXZN0jvqnIM_ZM8TGLswrf2fXAac5I2FRTn1v4pq_f2UiBbW4FWVmJSOkbiPE5wxarnU7YDfGSFTLgNtv-OSD5fiDU3ZMBNLTEt0DBJCRUXiJwttoiRrDvmMbm8WAERbg9LQZpqcQxOwDnhGMoADUsVcF5cfe33fTjed12fgoLQskhkMcpYWbBTJYt2JMPYhx4JO8Rvzy68A5QDDaPktPEld20xa5cN9u22nTvny0JJFfp153pBHPwZnhp5D7PxO0wkybdoCwshiuAdATFuIOoTVrFuPPzapPhApPyOSnSE-qZ8Og2fUqy81bRFJLTLQ7QU6hfpdrRVophodZ3rbUJMmcmqyc_vCCleiwJ-2s381NLmEopww_A8YLcXPX8sfxIhV7y1RlJ-Ls_ibtfx7x3_M8Cm6CQzryf1pbIqMagdN6JccClbXvyEX6h3xRA1xU5pl4GKFoJnU1KPA_N7-E4kRAk5mJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیرکل جنبش جهاد اسلامی فلسطین: شهید آیت‌الله خامنه‌ای رهبری متمایز بودند که به موضوع فلسطین عشق می‌ورزیدند
‌
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/446775" target="_blank">📅 20:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368a6b7cba.mp4?token=S0VBuXaRRoHl7jvSlSAe-RJcolRNam7p7qcY-zF0jdf7SbPR7lGtDOCKx06Lt__GVqR9RDy49nCLLT8C0mklvnw6sVbDh7AjLbJS6VNR9s1EHPAIrWX5ckZdezs_Sw26HD8dSq5lZjGp5r0UMfNifAxUupNbSh2GAcbY7FExu5AYOMC3IcADMO7MAEuOMBvNT_UNV_lSJd2fvT-BvvRdRMi1kOxlxA5ENJOjpNT0QIMeFhooDuLEwgRfMIA7pNznBUqdrfTmECEhsuDVW4SFWPqdTmk2IVCTzZ7o_tioLbYb11jR7OB6qOYMxipvWCBObG3IBckVGtq1D1CzTSxetRgONtANEwOhNHUs_RxBT3ShX3vdxzSiyTK0EHK91Xj8T3s-pQ6cHb1DJ-p7NZVj3SdJ4cQP5-g9wlSGajwAAT1o-X-FH12VW7EVz71JVPtLIpxhGhEvDNRCr7B22SU1iJbC3X6jBRhUzW8pN_GQlN-GLz2NhOVrkTnyLl-kkKHgYJp-KNl1PiOzeKLLMmvioOr5ozj11-j0NJ0-Q3ShThzWsyWxPviBahbWTitlQvOMKqxeZKw7xjXwnwfjLC5hcKNF_o_HflLb4PkefFs2iUmIOJ41a4ctKlVQvzFSbWiZOTsHRVqKqInxNfItpkbIHLm5b7636WVBfpQn-3er_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368a6b7cba.mp4?token=S0VBuXaRRoHl7jvSlSAe-RJcolRNam7p7qcY-zF0jdf7SbPR7lGtDOCKx06Lt__GVqR9RDy49nCLLT8C0mklvnw6sVbDh7AjLbJS6VNR9s1EHPAIrWX5ckZdezs_Sw26HD8dSq5lZjGp5r0UMfNifAxUupNbSh2GAcbY7FExu5AYOMC3IcADMO7MAEuOMBvNT_UNV_lSJd2fvT-BvvRdRMi1kOxlxA5ENJOjpNT0QIMeFhooDuLEwgRfMIA7pNznBUqdrfTmECEhsuDVW4SFWPqdTmk2IVCTzZ7o_tioLbYb11jR7OB6qOYMxipvWCBObG3IBckVGtq1D1CzTSxetRgONtANEwOhNHUs_RxBT3ShX3vdxzSiyTK0EHK91Xj8T3s-pQ6cHb1DJ-p7NZVj3SdJ4cQP5-g9wlSGajwAAT1o-X-FH12VW7EVz71JVPtLIpxhGhEvDNRCr7B22SU1iJbC3X6jBRhUzW8pN_GQlN-GLz2NhOVrkTnyLl-kkKHgYJp-KNl1PiOzeKLLMmvioOr5ozj11-j0NJ0-Q3ShThzWsyWxPviBahbWTitlQvOMKqxeZKw7xjXwnwfjLC5hcKNF_o_HflLb4PkefFs2iUmIOJ41a4ctKlVQvzFSbWiZOTsHRVqKqInxNfItpkbIHLm5b7636WVBfpQn-3er_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین حرف شما با رهبر شهید چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/446774" target="_blank">📅 20:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW5HvJ4En3jw4ftX1gzs_P_j2S8G1P4ReGUdmM6RDhBYad1dv6zh_Kvdf7HcVwEM4q2cpSJMORfnDi_WPiffaYW4b5ABlgXUKaWTwOtYh1MNdxMrNQc0XxEuXRP1vnWbrp5F6xrElfHsh8pnNoupnb5lXvWKjf8fym-3LvNQa-L5T4wRUUpBM0SmEa4TqiWto3qZw5xWj9cQi5RZfouCkUj-6feynKamXdIvMeGqB4HnQv1WtjkJ_odsNxhAU5yC_ZKzzccSgeWtZAOnSoWMNutfpQVsRCEIH50AYV-_IAeuP_jnQHoNn9mGHgys6k2UeELq25IEot8B5LPXh-0Upg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
راه‌نما
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/446773" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d60c9e7d5b.mp4?token=K_iXc5sdqCoXkzIzGPWXBZDtrHMrSs_CQlDSxE7ZbXcPja5rhgI9c2E2CeD2N59BlpH0HcZ5Shp8MQkd9tmKYNwCP7xZGxHZ6KtTvGwyrZ2QjZcjM68eV3FeSGJlojtZxdTRupO45I-Bchz_-KL3fdvgjoK6qwV6TY6kFMqwy06z8s6P5p9O6n3OgdlARiDloohdq8n4Kp_VxM5y3GDJHjXESkcxKBOh5_bqoLyIWpgecsE98GbsUOtPuhSY04ZgTGF9s5tCah0HE_w80UknuADvc-mZKVWA89Kh5W243msI2IV7I9gCVAt_Eo7vSIrMiAvcZIT_U73YAbc4BAUJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d60c9e7d5b.mp4?token=K_iXc5sdqCoXkzIzGPWXBZDtrHMrSs_CQlDSxE7ZbXcPja5rhgI9c2E2CeD2N59BlpH0HcZ5Shp8MQkd9tmKYNwCP7xZGxHZ6KtTvGwyrZ2QjZcjM68eV3FeSGJlojtZxdTRupO45I-Bchz_-KL3fdvgjoK6qwV6TY6kFMqwy06z8s6P5p9O6n3OgdlARiDloohdq8n4Kp_VxM5y3GDJHjXESkcxKBOh5_bqoLyIWpgecsE98GbsUOtPuhSY04ZgTGF9s5tCah0HE_w80UknuADvc-mZKVWA89Kh5W243msI2IV7I9gCVAt_Eo7vSIrMiAvcZIT_U73YAbc4BAUJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این پرچم‌ها حرف می‌زنند
@Frans
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/446772" target="_blank">📅 19:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40143b2f69.mp4?token=GXNs-9I7Ssicw7NyJreikJ0Jz210zKl6jC01lP4KfcU_iE7LAOqE-zTrkwIRVY5Dsfrkm7UFHoA0496-ZPjGSs8gsOssWd8H6PYVv6yHaOB04BnQGCeFTbyjfHO9aL7DTPNch0OTPzKg_uavMpWaj4e9HlE5Os2vHa-YAyC73Ar8_RUb2HqtjKgrsKSjReXpR8XeIgVROL8L7UdzYOITj2verNobkQSlN7nepeYGary88dLKuGQ_ekFCDaEx1c7EO1IWlPzONR40uWW6phDjRGSz1qFlq2rR_qgQOCyuqraHOI4D9mnRZRJIxwFmi9mOUpJcSRRcOkyCn1LvgOmVf4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40143b2f69.mp4?token=GXNs-9I7Ssicw7NyJreikJ0Jz210zKl6jC01lP4KfcU_iE7LAOqE-zTrkwIRVY5Dsfrkm7UFHoA0496-ZPjGSs8gsOssWd8H6PYVv6yHaOB04BnQGCeFTbyjfHO9aL7DTPNch0OTPzKg_uavMpWaj4e9HlE5Os2vHa-YAyC73Ar8_RUb2HqtjKgrsKSjReXpR8XeIgVROL8L7UdzYOITj2verNobkQSlN7nepeYGary88dLKuGQ_ekFCDaEx1c7EO1IWlPzONR40uWW6phDjRGSz1qFlq2rR_qgQOCyuqraHOI4D9mnRZRJIxwFmi9mOUpJcSRRcOkyCn1LvgOmVf4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عهد می‌بندم سرباز رهبرم باشم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/446771" target="_blank">📅 19:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-k9GN00TkpNcHjwaVmVkiHbZQyKLB_nZitQvkzmF8RRWj2jfxUAJbvCLQFjhwaTqJjkk2O6Kv6RPhw5FS8coBrKvFl-0uJOEMmp3Nc2Cx21fqcu1yyvfuGos4dZeebfoGO21MHvwvSg_pJTz0HKu7IjstlSq-U-wkET8MUHaynqrIP92wgJpZgXujADWuhdN0_WktuTWPaEi3NoonpDc7xgs6ilnnXT5LRHGj1Sc5gsybLeXoPFrh0Lqt5J7H8aUwrexowgjo1XgfUYXcy44VXqe4tBS1y-onAnUhTcd5jXUoairV1ghZ0Ncei-u2NxnItnY_TK_tCmJzzdX4qdKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع‌کنندگان میادین امشب به‌سوی مصلای تهران حرکت می‌کنند
🔹
شورای هماهنگی تبلیغات اسلامی: امت وفادار و عزادار ایران اسلامی، در بیعتی دیگر با حضرت آیت‌الله سیدمجتبی خامنه‌ای، پس از برگزاری اجتماعات و آیین‌های شبانه در میادین و نقاط مختلف شهر، در حرکتی باشکوه و سرشار از شور ارادت، به‌سوی مصلای امام خمینی(ره) رهسپار خواهند شد تا در آیین وداع با قائد شهید امت شرکت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/446770" target="_blank">📅 19:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60781e76a6.mp4?token=TV9T84VLJZuK1qtxrJh-8zpYQe7LpFIgFcN4B_A-_XFo-suq3qQml7e_5iT7TkDYTWt85B_J5KqVFCZEEQsqGkkCvVmFTAxVcZ1nItSqYodU6gQkesyde2cE4YFTQ-6todbaVVL7VdkVHdBEWuect6_8UlVfyQVaaixP08yQJ841gOdB662Eo51QzXWIDv29OCu8G9F9xuvaew2Nhk-DHGO5HxoUxf2wg4hyOXNYvo1Oy4rYdTE_P1HlzevJqzEwBdCWP2NTr0WcVzKIriWKss4EHGoKJrJ9TfLtPQZgzqJWwjiCX0UEOc9TTxYElVdo9j31rULm1mLhsEB60q1UHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60781e76a6.mp4?token=TV9T84VLJZuK1qtxrJh-8zpYQe7LpFIgFcN4B_A-_XFo-suq3qQml7e_5iT7TkDYTWt85B_J5KqVFCZEEQsqGkkCvVmFTAxVcZ1nItSqYodU6gQkesyde2cE4YFTQ-6todbaVVL7VdkVHdBEWuect6_8UlVfyQVaaixP08yQJ841gOdB662Eo51QzXWIDv29OCu8G9F9xuvaew2Nhk-DHGO5HxoUxf2wg4hyOXNYvo1Oy4rYdTE_P1HlzevJqzEwBdCWP2NTr0WcVzKIriWKss4EHGoKJrJ9TfLtPQZgzqJWwjiCX0UEOc9TTxYElVdo9j31rULm1mLhsEB60q1UHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مصلی در حضور عاشقان رهبر شهید در هنگام غروب آفتاب
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/446769" target="_blank">📅 19:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3fc10feb7.mp4?token=BO-I6hSrt1EZCPZvKchMDvOlpU8hmsRKuTIed_ZfaRbU96itj92crNmJOmTvLJ7ieJd_2N3AsCItF-vb0OsK8Vsr_sQgUchkSXQ497_9Yrka5e6LZ3dFknAyU2Fyl46mgLcYY9IkNy-Rmip8UYrBWnTE-Z9LnjWWBMrY8bdbF0Gj9-ELeGwygOY7zEqjsx3duKFDMIeAON5BSi6ZG8yo1SVCz-6jk1AfZ8JPMnqCJybKaOT_Xlh_sNbapgTwxY6fIyMT7v4XUVtMKxYricE7D9L9IXzbNHOTDz3wmy3OESoWrd0hEtpMMnK_44Xjw6QweFK_RE7rcFmd78N_hX8d9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3fc10feb7.mp4?token=BO-I6hSrt1EZCPZvKchMDvOlpU8hmsRKuTIed_ZfaRbU96itj92crNmJOmTvLJ7ieJd_2N3AsCItF-vb0OsK8Vsr_sQgUchkSXQ497_9Yrka5e6LZ3dFknAyU2Fyl46mgLcYY9IkNy-Rmip8UYrBWnTE-Z9LnjWWBMrY8bdbF0Gj9-ELeGwygOY7zEqjsx3duKFDMIeAON5BSi6ZG8yo1SVCz-6jk1AfZ8JPMnqCJybKaOT_Xlh_sNbapgTwxY6fIyMT7v4XUVtMKxYricE7D9L9IXzbNHOTDz3wmy3OESoWrd0hEtpMMnK_44Xjw6QweFK_RE7rcFmd78N_hX8d9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتِ عشق و خدمت؛ قم آمادهٔ بدرقهٔ «آقای شهید ایران» می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/446768" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0145dd6a7b.mp4?token=UYTVhCVPpM6EP5yLOzzA6l6dYfhKBRW0oeJQ7ih47-v5r-1fWCTYhjvbQHfy_jOpaFgujC3FqJzaNfgQE9zSfYfRPeaMwc4At-W6ZDsMQnZYMnT4S-7NFzpy1wqlNSiEzyLqcpRsHFmjXim9R3F3upwqwz6X9NiNYhrxSHGL4z_sw-V3QClmCZ3lWtrFPlJz2qD9AJkx1_gX8sgWs0K2tSSyBWnahPo2E-GqhxXZAWnCUBO4t9z_FU6ttaAVsal-Gpdj4Sm5xTL4ZLDM3HF-I4I4mz_rrFrGsBIXe4p2NNhiSF6fQXS9HJLFfWJY5Fy9U3Xe2svp7LMHgfc9nZg4gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0145dd6a7b.mp4?token=UYTVhCVPpM6EP5yLOzzA6l6dYfhKBRW0oeJQ7ih47-v5r-1fWCTYhjvbQHfy_jOpaFgujC3FqJzaNfgQE9zSfYfRPeaMwc4At-W6ZDsMQnZYMnT4S-7NFzpy1wqlNSiEzyLqcpRsHFmjXim9R3F3upwqwz6X9NiNYhrxSHGL4z_sw-V3QClmCZ3lWtrFPlJz2qD9AJkx1_gX8sgWs0K2tSSyBWnahPo2E-GqhxXZAWnCUBO4t9z_FU6ttaAVsal-Gpdj4Sm5xTL4ZLDM3HF-I4I4mz_rrFrGsBIXe4p2NNhiSF6fQXS9HJLFfWJY5Fy9U3Xe2svp7LMHgfc9nZg4gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: عامل بی‌ثباتی منطقه ماییم یا غدۀ سرطانی که آمریکا برای ترور درست کرده؟  @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/446767" target="_blank">📅 19:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9a0ca3e4.mp4?token=XPVupFPB2cRvGA55jzadRuGCzzX3_wm17BcWCtVrzoyEvjZBFQRRmJ0qACVlFsykxItmm1tyTlrNvUKF4c8j5Yfx5e-LgEHk-XKmhLj6OOSO0MEoOUTtZUcWAUwrRL1_XpcFLq1Hg-zZLmuc8RvNPJKH4t716-j17IkMICEaso9tjOSo9u_Q6Itv0dGeM1O-wfGbEsAbNuawOBu17kNt7ejn3sHEQB_BZCs4Zk4NkJbyeQN4TVVUrva97FASTKUjnZHaTM26RE62F9VwjsX4k-pbTdE89AROH7BR1P2rewOMs7hQYAhrQ-wl383ZXdmed09F75IV4N3zKtSOLpZTbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9a0ca3e4.mp4?token=XPVupFPB2cRvGA55jzadRuGCzzX3_wm17BcWCtVrzoyEvjZBFQRRmJ0qACVlFsykxItmm1tyTlrNvUKF4c8j5Yfx5e-LgEHk-XKmhLj6OOSO0MEoOUTtZUcWAUwrRL1_XpcFLq1Hg-zZLmuc8RvNPJKH4t716-j17IkMICEaso9tjOSo9u_Q6Itv0dGeM1O-wfGbEsAbNuawOBu17kNt7ejn3sHEQB_BZCs4Zk4NkJbyeQN4TVVUrva97FASTKUjnZHaTM26RE62F9VwjsX4k-pbTdE89AROH7BR1P2rewOMs7hQYAhrQ-wl383ZXdmed09F75IV4N3zKtSOLpZTbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: عامل بی‌ثباتی منطقه ماییم یا غدۀ سرطانی که آمریکا برای ترور درست کرده؟
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/446766" target="_blank">📅 19:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg7alB0pAIFlx3nyfLFcl9o5Tm_J5B2TtQNQcNL40MPn133PlRJbaVovvhel5JlIZavGoCB1Dfz_UZofz_n8ogtmeT-3YJEcgdZPib-XHSab20dZPHDyeGztUdpjaBKAKxnz6XenCzfY_Tyomct-NzbaSZjbKoaHeekGbCXOuUqf2OPL4K2NOjS48StcFs9EPItC1mmHOy3nsmMG-nNwkNTzrXJ-o00cVT8rolD-74cUEaxbXjw3_mdCQfPEoPz1_XI5peoM1jRsKleNmZh4-RH6OzoFMGuIVF3J5ymzMIkRiR8ORtzMs8Bp28SDcMUNa_z7eql4SjENsXeMdxgG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
کجاست فرشچیان تا به غم قلم بزند
◾️
که لحظه، لحظهٔ دیدار آخر آقاست
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/446765" target="_blank">📅 19:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b194b778db.mov?token=aaGY63pUaDnSDbbB1hL9dmw87UCV53KFoAM9zzTXT0yhgo4YNXVYgmkWbk2PR-T_MzE-H2E_orCBCyYYliJe_rYBgskCq1cIiOBiyEswL7UsikqkNvwjTC0xvLTd2M-3G7VZeHcExY9f8OaMuZ8WrqqKKOC8nOs7roNhgphN_njjtPtAO8KrOrIGQhTPg86xgyOQDmW16kwsCGNHJ3X7sXX26VrDfKCHTorkR_1UEIWK1hZ0fsKUuix0EXn6RqAYMAhOLy63bwNYxPSmlAj9RkBL2A6gLYwR79bEq1wj_6gc0UoScuObTJOwTdN8f0itGEsQjDRl0KbY1HlnzSwg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b194b778db.mov?token=aaGY63pUaDnSDbbB1hL9dmw87UCV53KFoAM9zzTXT0yhgo4YNXVYgmkWbk2PR-T_MzE-H2E_orCBCyYYliJe_rYBgskCq1cIiOBiyEswL7UsikqkNvwjTC0xvLTd2M-3G7VZeHcExY9f8OaMuZ8WrqqKKOC8nOs7roNhgphN_njjtPtAO8KrOrIGQhTPg86xgyOQDmW16kwsCGNHJ3X7sXX26VrDfKCHTorkR_1UEIWK1hZ0fsKUuix0EXn6RqAYMAhOLy63bwNYxPSmlAj9RkBL2A6gLYwR79bEq1wj_6gc0UoScuObTJOwTdN8f0itGEsQjDRl0KbY1HlnzSwg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال مردم از مراسم وداع توقف مترو در ایستگاه مصلی را لغو کرد
🔹
به‌دلیل افزایش ازدحام جمعیت، از ساعاتی پیش قطارهای مترو در ایستگاه مصلی توقف نمی‌کنند.
🔹
برای مدیریت حجم بالای مسافران از مسافران خواسته شده به جای ایستگاه مصلی، در ایستگاه‌های شهید بهشتی یا شهید همت از قطار پیاده شوند.
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/446764" target="_blank">📅 19:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvAbbqzB-Zo-sQLNxCVWX-bmchMqdcG47gE7ZEkcnmcgaZu6v2jwPM0R2OyMOvH0nKZbg6RQU_2WriHKKnevetqk5fzGqpHet168lcSFVruaULH49XwBDEQlUDThk_9PvdzA_ZwTCxAc8wH1zLQin4JRdPW064dr_b8keZAdWuLCneSUfeAJ4zbnVB0660QG8IgtdeCd095WcezK6BobvRc8NBGE7MQOmX8PjO4RJiv2S5Om6z4nUu4K2FvIZtOtiIvPrEtsSN4d176xWd6rkpVm7nlPKB7ykHaamRH3Mcci_rVmGRX4KlPxw-JMI5OeB_4T122F0SXZyQro4J1Caw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پاسخ مردم به یاوه‌گویی‌های ترامپ
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/446763" target="_blank">📅 19:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZI_bAr4dvd2co1qV9iacV8geDrnz-xIXGOg56DR941_-r5yzBXavNPNVdUhPW9GOJv34vQC5OAKY2vmYDWl4rDnQdG_vu5X8qTZkghu5ISti-lyT-YLxLyx7p5CuJvWvuOnNdoUNxhg4nUmgtEyoWWScRb68_5j3Kql9Rehnapt2X0JWH7QT_I9p9DPQnKbD1RFxAiDroNgRysDRbC9Yfr6JKRvorT-NamRjRlqWrKayUrMviWnXhPucrnxTQKyVoGedVGybcc2oEbS-5o7oj_YW0oeSeHwBrtYbDQB4mvn2Q9pjMg0zUJiIKMv6vo_6Ez684aPsQAoEsLmEFnnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: خون رهبر شهید باعث بعثت همۀ آزادی‌خواهان جهان شد
🔹
خون او موجب بعثت دوباره ملت عزیز ایران و همه آزادی‌خواهان جهان شد و به فرموده مولا علی(ع): "حق درخشان است و باطل آشفته".
🔹
قاتلان و جانیان بدانند که فرجامی شوم‌تر از سرنوشت تاریک یزیدیان در انتظارشان است.
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/446762" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446761">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f26e481d.mp4?token=ElXK4KnLb8h-1i8TZRvCXRDE4zXpgrG3khZGayt8xHo61xkQqAZWpiqgHhvN8mvbZzwMO6BLMQzPSoDcAOSUUcYrJLkjDsUSXESlsV2azXV6e-KwXpMvUnR5wpImHeT9VajP-_gp7BrPFaeaIZ1BPSKh6Qao7-m7SL6Ubchyb1goYyRo79jGhKK2TzmJh5B3NWhIZnDInsG2LUWxJvIYCKXCDPq4-shYtnX5QsAri0PZrXDDkpsXIVSXDJh6M8GXWnFbVpvyWZv6JKiZLqkaWy2-Ffnyu96syROh89CFjQBY8BrsABbK_YAoZjpjn4WK6TmOodd5nbYE3QP4UHCctWFsWsFFNz0v9JDO3eY_sv9KvRFgk9L9a9zo10JSYzECOk2A1P8E3OsNKAocReE8i1MtkJYT7ZG81T9qxbQiTPAzxm1j_-tLA4DiQq0XKduhxEO37BZJbgKaND05spV2DBGQjMUjq5fPFCsHSTxynT4VE5mHjR1MVN-Hb8ZWPwviCOTFPjukMgDv-Zy9ydwURlUPP4FHXeCxdmtCabuDOMnkXBHVDAuflTy7BUQN-EfenzqdrlGuuI7B74ZMxR2UirxpaN1AqysjJ7VCujuE1jgj8FvVVe5GF40O6-30QZBV0V7s10vu9GUyrRaTnbEaMqwoZRYaN9OoEP-pgaib-ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f26e481d.mp4?token=ElXK4KnLb8h-1i8TZRvCXRDE4zXpgrG3khZGayt8xHo61xkQqAZWpiqgHhvN8mvbZzwMO6BLMQzPSoDcAOSUUcYrJLkjDsUSXESlsV2azXV6e-KwXpMvUnR5wpImHeT9VajP-_gp7BrPFaeaIZ1BPSKh6Qao7-m7SL6Ubchyb1goYyRo79jGhKK2TzmJh5B3NWhIZnDInsG2LUWxJvIYCKXCDPq4-shYtnX5QsAri0PZrXDDkpsXIVSXDJh6M8GXWnFbVpvyWZv6JKiZLqkaWy2-Ffnyu96syROh89CFjQBY8BrsABbK_YAoZjpjn4WK6TmOodd5nbYE3QP4UHCctWFsWsFFNz0v9JDO3eY_sv9KvRFgk9L9a9zo10JSYzECOk2A1P8E3OsNKAocReE8i1MtkJYT7ZG81T9qxbQiTPAzxm1j_-tLA4DiQq0XKduhxEO37BZJbgKaND05spV2DBGQjMUjq5fPFCsHSTxynT4VE5mHjR1MVN-Hb8ZWPwviCOTFPjukMgDv-Zy9ydwURlUPP4FHXeCxdmtCabuDOMnkXBHVDAuflTy7BUQN-EfenzqdrlGuuI7B74ZMxR2UirxpaN1AqysjJ7VCujuE1jgj8FvVVe5GF40O6-30QZBV0V7s10vu9GUyrRaTnbEaMqwoZRYaN9OoEP-pgaib-ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گریه بی‌امان دخترکی که با ویلچر خودش را به وداع رهبر شهید رساند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/446761" target="_blank">📅 19:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446760">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173a5d7480.mp4?token=QYdiSPu1fUvNZy8IFPQp4xxBjgOUNOYy0dofPYwhCkiGQdJvzYQ0e8dqVFYcLLNEuPC9-dhXvm0wcSuPLnghJKmM8BVPQt38kv54VCyM2Gonr5YQIrIVq_z6giBlPsu1P7nvjUBZ39Hjg-zzB_raD6BaWg9kfU0zmECKKwKSjCfWA6r4gXf06ZUdjlM9iZa6Lk5fI5sj73uvBS4BHzxJTDcpAf9sYCAMVGzbO2GPcx5CQOtq_5zVzOx-Cq8owe54hz7BT0_WRUpv3d2V0b819jN1Q8tH5cPt4DUw9qpeeZSiCugrT_3lTpO6JxSYaiZ50lkzRU7-hQzJJkcrB6Po7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173a5d7480.mp4?token=QYdiSPu1fUvNZy8IFPQp4xxBjgOUNOYy0dofPYwhCkiGQdJvzYQ0e8dqVFYcLLNEuPC9-dhXvm0wcSuPLnghJKmM8BVPQt38kv54VCyM2Gonr5YQIrIVq_z6giBlPsu1P7nvjUBZ39Hjg-zzB_raD6BaWg9kfU0zmECKKwKSjCfWA6r4gXf06ZUdjlM9iZa6Lk5fI5sj73uvBS4BHzxJTDcpAf9sYCAMVGzbO2GPcx5CQOtq_5zVzOx-Cq8owe54hz7BT0_WRUpv3d2V0b819jN1Q8tH5cPt4DUw9qpeeZSiCugrT_3lTpO6JxSYaiZ50lkzRU7-hQzJJkcrB6Po7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به شما رخت شهادت چقدر می‌آید
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/446760" target="_blank">📅 19:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446759">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db58f0ef39.mp4?token=UWO_aO9853JB9bSTv23yM3R_WLLIfimyP_d6GLteuZi9wPX971o2dWISP8GghV36OI23w74KlM0s9VM44x3VmEHqYYFcj5PSTFJRXjbulkEDL2Vb1if0N6s5TOuL2QNaWwhDl8DkWxgjkMf0TBj0o4txu5OZ6vQu3tGB0eOpX2UYVM3qhR6V5NfwEw3KnIt9N3DDEdNaUHKT7JdSMyF6Q9cUqNOVk3bTXtRXfsoZc71vhvifbHBKvnfbQYimbFEvHSOdD2_Y9WpdfOelVZTJsCdRFENJLu8_zmP6bKQDac-OprzxYbaouQPIKLyOtilds77sTI1wQp7JbGvHY1hGE4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db58f0ef39.mp4?token=UWO_aO9853JB9bSTv23yM3R_WLLIfimyP_d6GLteuZi9wPX971o2dWISP8GghV36OI23w74KlM0s9VM44x3VmEHqYYFcj5PSTFJRXjbulkEDL2Vb1if0N6s5TOuL2QNaWwhDl8DkWxgjkMf0TBj0o4txu5OZ6vQu3tGB0eOpX2UYVM3qhR6V5NfwEw3KnIt9N3DDEdNaUHKT7JdSMyF6Q9cUqNOVk3bTXtRXfsoZc71vhvifbHBKvnfbQYimbFEvHSOdD2_Y9WpdfOelVZTJsCdRFENJLu8_zmP6bKQDac-OprzxYbaouQPIKLyOtilds77sTI1wQp7JbGvHY1hGE4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: رهبر شهید حتی در پیچیده‌ترین موقعیت‌ها هم حاضر نبودند خلاف واقع را بیان کنند
🔹
بارها اختلاف‌نظر اتفاق می‌‌افتاد که یک مسئله چطور برای مردم بیان شود اما ایشان خودشان صریحا آن را با مردم در میان می‌گذاشتند زیرا مردم را محرم می‌دانستند.…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/446759" target="_blank">📅 19:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446750">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJ5V6JTD--vvZSULtp4IJLvR1tYP_3Wm-gGHlYVBkjpECuRVlzaW5FFq3orEdCN42kwUYv-YDwM3BRMINBCRJiNVKQ41dRGlOKG_sj68aLIV_qYv1LedAYM2KOLzdmUgekqYf3fIrt1OAszvDu6PBJCxKfe03dwfYZ8mQzdXG9pvo69C_WfsJ0AuYCQuyN0mCPlJ3bPzrFZ14eWxEr5q04EbT9dyzWwDh83W5PoSjf7QiVeZZVqj9M6nFf4vXmyaqalUzYSeE3w27W3HUFgXiuUyvEtC434Qdhz-jWZbxo7L1gtvfQ-1MobtPrF8v5cLc-ERelZ3avBmo6eTwKwF9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kv506bPTclk32H-QRgTl0TJUjnUqp_A7oKldUlPOaDesYhd93_ufXvVuSxBhIofmXqn-lBB5E5SbpRZS-ZRGnAj1PVK1IP-P_GnbGUmqPzcdU8-k5-ZKQ8a4iwzMxdO5-ijsAYFVE7tOSOyJww8bVCIY6KMb9MJll9G3XXWBYAfaslsDywMfFNO3EOOTfTvjGFAfVpVeXtcCOvA-7wYm2cCi7dMkq2JVf45gSMwnv9RTAuoRPsMSUoqSZ_CXu_RqFT_cyNmIwhiAuT9t-6ak9lr7epXnH1YVnfVgM3tW5HCSGMKxCCWJ2LVfJKCR12gaJWbg_JYtJLgHLGfk9XAY7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqIoPuKNSLJemV9zduNM6xmE2bAPSYhi3pNpw8O-pvANOovu_9xOVgjWW1ps_hofVGpkLVRvvwgl_8drifo0ZgwzfDroDKVMGvVacXMdEHCPOuj8uT4q7nu4gJn3jsdf6eZGQoAufIAtKd7uMYvSvq37yzI0qqWKhMhlJX93e-DjvasBb-ab6UhOtm1uT26wRuXafHAhufZ9g1PpX-NOmROKuQyjC8l0dm32Z3zrQsarPuitqG-4pG1lT00aPzny36SihRn0L5iUQIVObKGpInoxwxyfQ8U38_fI2pfiomG4Zr_nVT17DOQKVQs83RdyoqfvczcUNEH2VVO9wBJwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUHEZyx3spMROhZVzd4iWyUbdMt_o-CK3MTqDx3NRGwGPDURsVDMlMZT-F1CoUPtiMS4lXNMbVFhgoMHTbK36HSwmZXrTMqIwjclnc-KqskGdF4QGTHpI43hLnMTknplmLHjHji0C-OuphGsgBDiE0zk1cwPDG-CjMaiqNEuiDrlKulNeXAnTLmsWndPE_pPzZCpRrINb7BsP7PxNXM70cOp0-Mi55-1on89YFwv5L4qQCGgZdF9u-7kuLCeOFaGWp2cNdCLBn1THzCEN21QOkfaVT8Gndg0XdhxQI_5OjBoDEYErBzTpsbEgBDJ0aSM1JsI3HqNCx4mEvLQyDlilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6oDqle4ejKVFbjYnZ0bpKN7_YZ-GEXLA2Fnvl8E8LxF1psy_zzkiRgDnyR__gCAjsR02-B7xz535Jl1XOGSVwh4ChufH2YHIKydsXT-E5CPGirOWB29PwZCI7uI6-JIFYY2NllNs2QePQJEHVoj0mFySKztywn8gC9DQa3Fhneh4dC-jqOtM429w-SpxKWXvWkxEs9aW3uTOf7cFNBoT08g9WeSiVhS_Rk2mb5UCKCvZfIFm15jMWoAhzP6T6zddBUC2LkqKbxgYJ6YsFYctS1xsglGA9Tv8WYeBFH_QDJKlK1zihwS_h1HQJMWtf6srvxF3jLooHDHjAlsKiNNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdVnl1mJq7BOUivkSz21fb9X5Mg_c8QaLe4Iqajf25--Ho-5YBgLMvSnYUaExnxwPY45Fk3P_P_Fyzi3vXP7pZ8D7X_GN7wMblJObPp68Cw_5PPpYPE9XQoFlYXT20cyeR4EYjdTO-4mK8cT5R1gz9EmQn9hbLGeC5ABEFwSc67chF333V9G3y5dJ3m0630PP3A7cifjZuYvPurSXyPcyAtss43gkEVzjA6sH6C2ppOt_xZttqFhsVtnyCgWn_6h5WkOe6FgMJD09kLxuu-E_9mF8dWGFvLjUodH1FgUEn_9xyNzrhzzr0MXxvc8msMrppcVgAnblYcO1IfVQiChbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uApcwKz1GLc9McJCFRoYUQYbssaLgBT3ZhtCN5rTg1r0EnciWXhIw0o6gcCR8Ix326nMlgrnuPqA5nfKCMWMQVxd1fy-JOjDcyJFC4JKOPJ2ZG-3LtbZAX5LjoIw4H138r-HBcsy0OBGEMUdFQl-CwsIBPfYaqx0aqf00g9W1_nlhDkaJbzVzhJzPu5uFxWP84VBbitavadvV7SNkIY9Om7AGxuLhC9yO4S4CxiKyuVJ6e-FBq9RqQipuTUvYaMDAukMj4SwkXH5fJKdd74MuikluaVJLrmbhqKNEgAVvuXIcwoyGdNAej8gKPaW6Yf6JYUYuLieoCPOrw7DHkkTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyKabTqbttwQfRGjTPeZ3CdNAOm-QXpxcxKfwpWLAM6kGZuWh7qNY2_AlAx6SiiYKK62NRDnGAosO6rETUKpkeNfP4B9MEOa-sQl30m4pO6K0p80j_3micNfkA1WYO4_Wm_ktGyDfEs4cx6CKyP-rcve97oTzpGk74y6dNnTLXKSvyJK47iyRQWWkWn1KxgiSUHxJlnXrBcY8iDyqRKEBjT_uU93AQzuYR14M5YY6t4-5zfyvY3pR9EaCIk8IzpNRu-Ugj2ZsM9VvfKGL8iU3HFL7Ufa18uhphii-GZ-vtjo7sibqdfASLPf1syv2ZCzSzsC4aQSHvfovONvQ-54lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیوارهای مصلی زبان مردم شدند
عکس: امیرعباس ابراهیمی
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/446750" target="_blank">📅 18:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446748">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
داغت نمی‌شه باورم ای رهبرم...
🔹
مداحی حسین ستوده در مراسم وداع با قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/446748" target="_blank">📅 18:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446741">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7iLV60VPK5caN2pqzohwIBvl-VhAFPNCcCwNcilg4D-_-o5Ct0qzI1fhA1d9OSXqBKhfhhYhr8HZ5juZg-iexxTKiXqXFQ023nWmMrHQKT7XLlvs3Nth9ZQN5g7IcdmXf9L_Zf0BeAln6Uvo4pzZEbQ6YwrUOn2iSpplTRWg5Z_VTglzKzE0w5u7DgnW9zt5MaROg4pAD5yQhKYIsVgxLMrRwiz-vf0TSO7IV8h8V3N8NbZhy8jhjSa2PH7PDD7JE9ceXV3Cd4OiGEa6ZP2TgsFsIGwOM8vwnrbYk73WMdCDVcZSMU3ZI0r2DPEnGYoZ3I-ylX9MGABdb9ykmL4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqBmg4epDh_M48MMi4cb1JgLamW1z5wy49NRFWV92O1CPwY8hkA8fO78FqONDr9mtg2ltqqiT8GNKtfyGrc-eW4DTdrIBnRljpDRzVK792YFwdtEo4NPXQAatVmM__nB8auS31kec2Y85TICasHZLSe9vA5C0w8SigonnVlEdylGJY1PtEIF5KK7KnPAbT1QoMIQWe4u4arCJqPHpHCY3QfWijYKTiYDktxxZ1OVGYrCiMb8I7q7ftf1JKYDkVw8cOICEx1jtrkjpcCQhEWM2jBxuN94D5iwVSqkoaqylsXCYuyMMKhvhIDVwdEVqOJf5Zt9kw6Fso3AZgM89D32Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I357jcz606uBJWKN8bimH9ZYrsDmzWQRElzzoV5H-yfC_OzR2blZP9BCHO_SAIxW6NS-jFEj7XZtZFe3lX1M5kXqu94J3AYHc3yay5mdoTe-kuotVcQFVU16DVJo6t9Pv8L9deIgHGhtONhykNt6jClDhCL6-ddjfxEnNwbxlq4IApYlb4wX_qSDNJFJrpIyUkSuuvSu9hXEwqXTu-T2IFSTf1mopgkZnUZe_ciK7txYbfDIEpwttEgj3T_gizZH4DRWDrtSjjAwdlLHARklSiXecyoBkpzB4K-SXnmMZ4W0f-kLW_Gk2bjjtnOu6vjXvTLEFVTmVIIcFgOdczdqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tc2cZuiDKlPPaMnquS6W7c8rIIlLToQKy6Uvi6454r1q6J3odZnEJePidyaJEqKzOLhRU-TciB7a1P8OdPxSANAMY8CU2C8WMlORUMOgcA542CoIUZ4btvRYA9fvmcq5gTNnXbqiZE78Iyj9SVA0uGxzjZ5MWg8U9MoYmJpC3gnkHsxVyVMh9i4sRyugP_SjQSLq_Af5I7sTwvxyUclPl6wOJEPmSc3-Ol1oTmWXuClr3yKetJ07x8v4jJlXIem100MVnGUJCy8gtNJakw3VbglB50QcMR3i2Kbt5EndxSwP1grgpysnFuEXNks31KTa0mazXRjlc5wIuleJ1wotkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WECUxLnfo-MM9A2_QxDmTpCnErMze3RGUtu55PHrZnzO3QcRiw5eVNLt_j-z2HJon08bnoXJd97VcGOndG5c4y3iC1sChXA6oHu4ADDSst8F0SCKVUW5YNpjXt1fgYS64Od7IGatROq6IWceTwLPztTnS1q_Lm2MBehHtQwjGky7mioqyap0XEa5tXPs-yYEPPrizb8xZ6wwUvWMOg3HGUjAy3HpoFjY5dtyYqcNJT5iYWjYTBpqjh_sxmcATr-qCw4-1p5wYIledfUOCJMhWG-cnbtlngmVvoZgzj3qP4EnKJm9rN_KEYp4kKpcJA1xxIcK0ZvfAXXDmUbZKqFnNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atbV3FU_dsiwyVmeXMz2E99vIukF9Y8sRVY-_1q7I00ux15j27-uRA2iI45R4IZ-DavHN-Oq7akOlOVl21_ZK0MUi4POguOqk_qw2942qRUkl3BQhOm1CcEmW8DyQXbhhqQ7w56q6oJRnah1RF_YujyzOm_MFKQqmt23mEHjGR_qWD830CgSb7PyVw0gkWzlyWkLgWKtjNomb4XHbhj-hRM-f7K3VeNEwmkG-ZudQviwbSSUN2m0iV89MB4wnBzwyU2OFT95k7VDqP3I6nA3v5-ibxHWmtcA9SfxXtkbSOO0CtL1fkxqH8plCw85-2qUCf5u3yv5Xp-QzAmF2MPOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lf0piJE2-Ye1Zr1HRja1ZFLUp4ew_HM0PkYwucpMoXq8eX5fJVzTQpn3u0jdSSQ7xlN6L1cHXgAOycX4YNZKgouyqT7WEQTnijcmcWlp5c0Gh2vTrgIU4n0gc-2Nhn0Piwaoz3MDV_CRx3bi3JjYOoCh9kCKMxq0UnGC8_WOWhV1LysubeZClNtuOd4d6oJtZTm3RfpNqoyZOIZp8KCT-VrbOdchrVZUcdx1sCPWmc0sewTM1bx5XKayUNIhb_j_gmKpqLJ2yrXlaReQ-iHJBzCVhoFl1BsL4x5z2uVLkklm1RUlsmwZW8kpiHlhICwM3VNl72ikvDda7tGzAsu_sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع باشکوه مردم با پیکر مطهر رهبر شهید
عکس
: محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446741" target="_blank">📅 18:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446740">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d07c6abfd.mp4?token=sS5e5E27j-fv-6oFMakHk7g5k0CKhiNZ6PDCywnnv2ukwrdX1-J3qPuPFsnPDeZ0sKgBEP-BrZHtIET07Pengf7MLYyilugbDGNX8yXUeONXxYH1q-_qC8YebLEh-6q11drpQvVxUfsIvUxKYntGLP3MV08p_TeGEpfkOiGbHu5Vb6i3D0INll_soNSQ5eA-EDm5-9tYCG8R_3gVI1Bs37AA4vVkyskWKzJreZb8SHvZCuaetyaFQAmzmLL3rxpSVKjyBuZYqqKP199abwCKSmIqgUxvde6ctP-0oDm6F1nDjvh2yDITDsRAby9rcwFXndistc3Y9yVhkVud--5Fwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d07c6abfd.mp4?token=sS5e5E27j-fv-6oFMakHk7g5k0CKhiNZ6PDCywnnv2ukwrdX1-J3qPuPFsnPDeZ0sKgBEP-BrZHtIET07Pengf7MLYyilugbDGNX8yXUeONXxYH1q-_qC8YebLEh-6q11drpQvVxUfsIvUxKYntGLP3MV08p_TeGEpfkOiGbHu5Vb6i3D0INll_soNSQ5eA-EDm5-9tYCG8R_3gVI1Bs37AA4vVkyskWKzJreZb8SHvZCuaetyaFQAmzmLL3rxpSVKjyBuZYqqKP199abwCKSmIqgUxvde6ctP-0oDm6F1nDjvh2yDITDsRAby9rcwFXndistc3Y9yVhkVud--5Fwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: رهبر شهید حتی در پیچیده‌ترین موقعیت‌ها هم حاضر نبودند خلاف واقع را بیان کنند
🔹
بارها اختلاف‌نظر اتفاق می‌‌افتاد که یک مسئله چطور برای مردم بیان شود اما ایشان خودشان صریحا آن را با مردم در میان می‌گذاشتند زیرا مردم را محرم می‌دانستند.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/446740" target="_blank">📅 18:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446739">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYcMowhLYKnyJzJxPXPVGY2MFGXoLqHVzCbTs9SQUiN1LYVl6wJ7xteOXBL2tZTsZVDtbHFGry4_stSWeaHUbAHQ0GmY56V_fmQlaRrrv3zWJ9dbk7io0ghED0Mh94CJ75bxNIu2yBQr2bTha-LW3LtvEKN08OQIbsI8uKKTZ4-AtY6yVB-8r0_3njFRTI1j79KP2s0DBu0Sb6vu893BUN0_WWvQ-1RF-TjX2qD41bKH5ojgaYyDKyJ_A1FRLnwK_Y_wa3lRfuaMGj9XzIQeySo6BUIQD5oYf-qbHBDpwrCoYDQqYHGW9hXqCnxpXFsnj41hiHC4mnF2rabM0_UlZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موکب سلمان فارسی همراه‌ اول بمناسبت مراسم وداع و تشییع رهبر شهید از روز جمعه ۱۲ تیر لغایت دوشنبه ۱۵ تیر ۱۴۰۵  میزبان زائرین است.
مکان: خیابان شریعتی، نرسیده به پل سیدخندان، وزارت ارتباطات، ورودی ۱۱
#اطلاعیه
#موکب
#وداع_و_تشییع
#رهبر_شهید</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/446739" target="_blank">📅 18:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | MIC Insurance</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYSXTkpF9unBEVnT7qQMF0Y9Yeie7TCOCL8_hKo5flZpykc1OKLIrhybhcwG_byDHQYcxuyS9Eg_xfG4eAEXhlYCJ7P69CPZ25EOtz8bXWoH99B5RxS5pF7smyZlHM7YLM_ce7UVooJXtEITwrJU93UL_9eP-P6eQOf_qSjIsgdpjrMcAyIf8yOVjz0D95f1YInoirHrxgpI6Yx3uG_usw8xRgEIeQ_ct5q4uHMCJc0JUF639iR-NJgRpGRPfMyioubZHAVnmtNoozm0rfRXlfyNVAw8tk0IOUhi52l66vyzhNWUwafXY3VhVzl2JQs6uOyYV-CmmDhCMa7pf3YY2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fC6i6HM5z_92B-pcVRBZysJx7vGbJWy-nd-clMbGXaoX6l19OqJEqwtB_1yqt4Phui5ko4kmHYwp4ptlA9LIpEYyxmznr8IW1s7CBbqLq7ZtafffJfe6pxVvJxJg3iSC3Du7zTUF-S6b6c_CwNg3vNGzLtqdoY6INaN3Vw7jKDO08U0I8bJ4H8xwLO_TlcAQL94C2BEZgXTVAtn7hhS3tnVVH4wALMelaBVR5lZ-O0wkXgOkNDBWcDYh3sWZvy8kCmylEFxlfBBFpv6OKxU1pxHC9twO_DZ04y34HmM7Izti46wXqk0oHUM9oTNkY2romoOq_AcBq1GKDb1rqbs7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTW8qDW6gM58dJfgoRHAFkQ022IFOuv224lf25H_WTtRWVAER5JmSEWGcbcEcd4gMVYi1vi_G8ctMvRcuO9cMdyRJH6QBrHy5G9p4FsQGDmnF9egioQaGNyEz2njvNT7bn9X4ixgQtW6D8eSG1PiV23I20Hz_zH-MkG0qJVRiSOyEOy-G_qBUEiy_4LXrm6SisxwB_QCeVAA9LHsiirQ4fhGs5SDSKThkzp-qfa1caUYmatuc-dt0dsky3oMIlo_IwuNPa1Z7zSocPoACWfZIrGYJM_oytHwQP66X4VCvFVZQb2zaVyFGR41YZzwO8WcAbNIqpp9NcWDH0sIEBM72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8JtEFOSegVvDF6V-LNksacaZr0aTip1Jd_F78aKv5O8Uq56XD-77gqA6t_gYHstm1Ix7Z8Qu7XnYi9VyjG1LtLoT4BxoT2CkbO1Xb95dTwuXoj23wp8hMOkj1MOu_ghWSeHlseS97lcklYFpQ9qtlYqwdO2XXqtcv80iMas6AO5NX2akyirX83fWS6QN58vw6CqlmHibFmkNKZw8e55AEHkE3x4-6DuEsGIIho3IhXWDqdh3_Lpl65FJLkWx5-sVFa5fEZ-BtfZ6eXuNupoyubftyogodjqW_7hBbbSDF4apvDZY7s2n2zM9xbpMAaFo4APvlw7dFE86j0TkP7g2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njqtuk0EGHFttFEHtnfj-jDi33BhI_BX_VAEtYWOkyeKRB8Fy6hS00NhTS0q4r0T7xNIlbFw5dky6dMg_M97_EmxDz4LJDcA0FUyxkgvPEHqX5zB3_rArb2wv-zCp_RFAdTAIGd_zJ47-634fPc79rL8uazWEH4hl1PxE61isgJ-K3P20vlepNeq_rbBdx6eA6Ijv-1zkcYrFmjvYWFkEkua--sEf2g2C9u6-A3wD_4Tj9kf3PH6zmC2tMXRj5RQfG3Urb9MTYmCZms2XWy9Gu38azM6FN3rU6JugqR1dDKJy_oUMJnK0q3Vn762lxL2Cbx6fuJKxVhOrFMsnxVR0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
حضور مدیرعامل بیمه معلم در خدمت‌رسانی به سوگواران آیین تشییع رهبر شهید
🔸
در راستای ادای دین به آرمان‌های والای «رهبر شهید» و همگامی با ملت شریف ایران در بدرقه پیکر پاک ایشان، علی صیادزاده، مدیرعامل بیمه معلم به همراه جمعی از مدیران این شرکت با حضور در موکب اختصاصی بیمه معلم بر روند خدمت‌رسانی به زائران نظارت دارند.
🔹
مدیرعامل بیمه معلم با حضور در میان سوگواران و خادمین این موکب، ضمن ابراز همدردی و ادای احترام به مقام شامخ رهبر شهید بر لزوم ارائه خدمات شایسته به شرکت‌کنندگان در این آیین باشکوه تأکید کردند.
این موکب که از سوی بیمه معلم جهت رفاه حال عزاداران برپا شده است تا پایان مراسم به ارائه خدمات خود ادامه خواهد داد.
🔹
محل استقرار: ضلع شمالی مصلی بزرگ امام خمینی(ره)، سازمان فرهنگ و ارتباطات اسلامی.
🔹
زمان: ۱۳ و ۱۴ تیرماه ۱۴۰۵
#بیمه_معلم_همراه_هم_وطن
سایت
|
بله
|
روبیکا
|
ایتا
|
اینستاگرام
|
تلگرام</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/446734" target="_blank">📅 18:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/446733" target="_blank">📅 18:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446732">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cea1a63f.mp4?token=Um0yTJaoHErVYoSB4Y9L-1HMsHamoo6KiUJCHxYizX6j9Wr25Yd8fomJPHKqX79kmoDkJp_sZT9Qos_NHBPrHWojpq0vhA2svhCwhzJ8LTWKcw9AapO6nkKrxn5vaGT6V4ijbHj_LvnrCnNWDNItEsZPjNcheyh6tPY7YkP_OMw3qCs7R2mWuWDsX4y1rr_ev8ufUSW4cWN_BKfg_h3f199E6ot4jGe0MauA9MCQyqeePzVWtsBIoWHRSVUuMvD7GnH9Jn4zVF3splxeZ3jvMppr8X9jvwqHdEP7Z5tNjs362qLPlh6EARh_yZYz9sprGzeT5BxlWhEx8nOcrhWSNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cea1a63f.mp4?token=Um0yTJaoHErVYoSB4Y9L-1HMsHamoo6KiUJCHxYizX6j9Wr25Yd8fomJPHKqX79kmoDkJp_sZT9Qos_NHBPrHWojpq0vhA2svhCwhzJ8LTWKcw9AapO6nkKrxn5vaGT6V4ijbHj_LvnrCnNWDNItEsZPjNcheyh6tPY7YkP_OMw3qCs7R2mWuWDsX4y1rr_ev8ufUSW4cWN_BKfg_h3f199E6ot4jGe0MauA9MCQyqeePzVWtsBIoWHRSVUuMvD7GnH9Jn4zVF3splxeZ3jvMppr8X9jvwqHdEP7Z5tNjs362qLPlh6EARh_yZYz9sprGzeT5BxlWhEx8nOcrhWSNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ازدحام جمعیت در مترو برای حرکت به سمت مصلای
تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/446732" target="_blank">📅 18:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446731">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جزئیات مراسم تشییع رهبر شهید در قم
🔹
کمیته اطلاع‌رسانی مراسم تشییع رهبر شهید در قم: مراسم از ساعت ۵ صبح روز سه‌شنبه ۱۶ تیرماه با اقامۀ نماز بر پیکر مطهر در صحن مسجد مقدس جمکران آغاز می‌شود.
🔹
پس از آن، مراسم در بلوار پیامبر اعظم(ص) و مسیر منتهی به حرم مطهر حضرت فاطمه معصومه(س) ادامه پیدا می‌کند و پیکر مطهر با حضور مردم تا حرم تشییع خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/446731" target="_blank">📅 18:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446729">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4b5df6f4.mp4?token=muqOvr1411MRBjuC2Tg21huzoD3I86_Tjf4ySou_Qnd4qBBjMBWGnpKuRTu7qmU0-r6c_5Dueb6rWoE_XlUa5ydy-4ZfZpjgrpJUE-M4qKHGen4Ln4UmhQsm4tgtPK7MO0CP2b346N2IrqpYWqZgvce-I1VZ6dbg4DHKrUFQH3N7gag4NQHuwfts54aMUEzgEcVCBnYvRBx4T7n2iJaBE-BtLqSMwZ0E63B8heA0t9ht1dPhRs70nhQn_QF20EowVEv_ptQuABuSk79snGhumyNR_1oWDS2YvLAU-kGcV58x59M5KI9zDXVdL242LQsEx-1BFwBHS3Fiw7LYnQOYiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4b5df6f4.mp4?token=muqOvr1411MRBjuC2Tg21huzoD3I86_Tjf4ySou_Qnd4qBBjMBWGnpKuRTu7qmU0-r6c_5Dueb6rWoE_XlUa5ydy-4ZfZpjgrpJUE-M4qKHGen4Ln4UmhQsm4tgtPK7MO0CP2b346N2IrqpYWqZgvce-I1VZ6dbg4DHKrUFQH3N7gag4NQHuwfts54aMUEzgEcVCBnYvRBx4T7n2iJaBE-BtLqSMwZ0E63B8heA0t9ht1dPhRs70nhQn_QF20EowVEv_ptQuABuSk79snGhumyNR_1oWDS2YvLAU-kGcV58x59M5KI9zDXVdL242LQsEx-1BFwBHS3Fiw7LYnQOYiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همۀ امکانات برای حضور در مصلی آماده است
🔹
زائر پیکر مطهر امام خامنه‌ای:« ما از بندر عباس آمده‌ایم. ۱۴۰۰ کیلومتر راه آماده‌ایم و در این مسیری که آمدیم، بچه‌های ما سختی نکشیدند. امکانات خوب بود و همه چیز فراهم شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446729" target="_blank">📅 18:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446722">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujBMvQck5_L3NzoNuYcwStrAZAoVQzT_jyEjmOCNimObMqcqn4keI6UMZoApLOFctaSriu8Au0lVrPDIX6IR22f6BfpM6d1b_g3n2EesuduBv5Ni1LByYySv502B_CRiSQMFvhjAe6uY4-bb1yf2gYqz-i32d9_CgNcRK3j57prqJg5sC_uOPGsBZ5pmhQoihpk4PhC05X5SscMjvI1BEx36PtwusViMTTtxCFReiixZBpXUAPmK-vo5ozd8GKz90ZQ10VKSHv40dmuyX3sWJcSIK4bm_BcNbNFSV86Pk98CJuUsZBRGSb-6f-BujTvyurK7gpV0n7Jxt4G014gzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISSjBOxc2OwaLfVTkHpYeOvMcWLrsU9BpFmPtyLIa8tZxRxK9gqn9nKG-M3eKE5mpP2GdtNJXZunxAQUd5wrYviNP2aWaXfgMr5DKzWzLxi0aPCQLB3aVVNP-NvDLYIu-jFPVCgV6WTxd0EHbAwW7jQsMkX5H_Wce04gH0ZpcwhWdX8CoN5NXt8tkdUU9OD0ZLS8pTFt08Bcq-Ds1zpp0XSkaU8xzxyoIA1uvEhHeuRLbP_WUYZ_c2fU5UuA6WyUbEpi5uA70k2i1_mwhqPJnzSr4zi_W--S-mN5JpnEl4HSKqJHg-en4TPPV05-lOyAY4yIiovIATBbHMGA-p_SMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYzBLjFtbZ-EspAp2bFnvsYu1Buy9rtfwaBSWo6L88S7F8-uWkwFaMyoHfyOBfFyce43eeUSfB4AQETnH2_bDipnCbQl_SW4EYTKTCox8FeMPJFoejided1BuZGE6J45v9m9sMUJHujwnPebJVMYHWtLwxkqZWRXX2tToYYevHpccp9MKUtfN-WDxeGqp5FRT4X6jf_shCgHKf2Y7EcqRDeLQAzP0c4kTximgViRZO4y_PRrFokXP3LPc7tsLTuj3x2DTHVeZOxEzqotVdvro19m3VMuZj14d8ZPqHyZZdrvHInstOaEc7zdYHjBvQbXqGq2Vw8B50lUjFk5_peVAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMmkNzftj5k9rI-snx-1UkixntIfI-Q4gZbFjQD0BX9Hejr91ZqaqtFQXxNCyJkLiQVQ5gM9iqoNLswOnAbdzJDI7EhM1aq7T_HwDNENqVjfNb2jyX5JFIYguBrMUhDaDCIFFhogn02uh5Z-F_FPHiaFAn2lJMqJSiCFqnD8usVj03TNjkksKbwSkbIcE80-UWwr0LoXa_ZbN6dzuEPzvMWXSzZ2h1yoxooexSnRIfrhTOoiLaWhrRLO1DBNE2iHTebvI0ke3K9Y_zelemmzi-gVRXTaYEKZ0vaxllZTe7mMWgjDz_ucArA-XPvrQfu48s1SJeugaEx5_91oTjCzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_rQ29vN9bhsUrcgz3_wgmIbniucqM1D8aphIAJmUm_WzdcYObt1R_r1fAI9igV19jM_M-6mzibzemezIErdFm7RVox22qzLfDt6Nt2rh8YXR0T8-CmwaNnOfrPwINZwlvq4iqXyXXubj0qIsWoIbqye9QtKHmZ9t3YyqmG8qBnxSYVBnyaFuLWD6iEvMWjLKl-fEk2JXJ96VubKUC-QHCYOeDK_HbCplMM5wIRLNT9CfE2UlgDKKFAUYJGy9BnIchIN6cdaG338U0ihud59LGLu67Ap3b0SzskjafHW-0dE7glyVQE_b1ONbX6ZtO8x8QHZmpKdnRtO2AHYzJGELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7aNgAQt9D65fBBH1Jg2kTC5Q-5kAM_RSanQ96u2uHRSB53NMKd5PUERTovKgQnN84auwzb_lpr0QzPuFvP-qn4kjo14OU5AqOMrj0Uhdfc1htIzec5Vl4ExOABvk9mBH3bMisv1ayvdf_fk8yG97RpeFo_96bbp8JqELSvG6i-giiqMNEwvKfd8h77ijWjRIRRsYLMuuBCtoI7RygeFnnNTxLsMHAIIAiKl5aEZ-dNwqwNWlVRAFrSRQdzOvwIIl0-wFHqjDRPe3FQLZ-PwUgBl2diHOHHwWxyGl11c6YtbFOQE3gByOcYNW6xkMvCrCWPe7eD2qv1jTUkwD-78EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9muzExXbTHfFcaFIvpxFkMfXh1iAvYyBU7d3Ck-L71x-jsrrFxQtgDzfpC0tIuN-hmD5KsK9v3loYNiB3xdYenUToEwfQ0a1_rKY-0KCk2Ipo1A8OUz_C4FLZ0iTQGb8n6V02GbmczLGX3CVwQGLtEVRrVtTJ5bMj0UDF5mhyn5XZKKwjVoJDMM8Xc7xRovF9gaPWk3OikuIT5-f6XLrgWFSN0NDk_U7cmITL7O1c9mIMXvqMNZPyKhezTm5hoareJJH5CBAe63xiQZYSfI8FZybfINggz86LfxVnZzgb0VOfo7eg7xm7uVF51OYaXjuHXlnuSw2zMgxA-UgPMLEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
همایش بین‌المللی امام خامنه‌ای رهبر جاویدان مقاومت
عکس:
زینب حمزه لویی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446722" target="_blank">📅 17:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d664908bc4.mp4?token=LCz0_Gora7MMGlcl0RIJCtoIwmtxjd_o3NQWS2gw-rvA3HEyzZh7qkLK13hH3NizvU9TOLHtHXhoyloyiXSh7yC4EANaKN-pXuioIOcKHdi4koOe3KO5kbyRHQk_MfdIEIwbvXDZTarV-KrtzVPMrvulnrk7ZFL3kc9aRo61KupCG-SK9w4TS0wQyF4I_WT5pOf2I2Sl2XPLKJ95egVSiAOqkZG6Dg2GUpUG6Ep4aQZVJyjMZA9Xs1zGx82HJmbOdA0m_S1rOPoAPs3seS7EYxAzhfYWfhBYugnwp8JBH1wS-rsLqwEOMZXHKELTrN1u8fpRUb_d3LSUSraj9ACR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d664908bc4.mp4?token=LCz0_Gora7MMGlcl0RIJCtoIwmtxjd_o3NQWS2gw-rvA3HEyzZh7qkLK13hH3NizvU9TOLHtHXhoyloyiXSh7yC4EANaKN-pXuioIOcKHdi4koOe3KO5kbyRHQk_MfdIEIwbvXDZTarV-KrtzVPMrvulnrk7ZFL3kc9aRo61KupCG-SK9w4TS0wQyF4I_WT5pOf2I2Sl2XPLKJ95egVSiAOqkZG6Dg2GUpUG6Ep4aQZVJyjMZA9Xs1zGx82HJmbOdA0m_S1rOPoAPs3seS7EYxAzhfYWfhBYugnwp8JBH1wS-rsLqwEOMZXHKELTrN1u8fpRUb_d3LSUSraj9ACR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمد نجفی، بازیگر: کدام رهبر یا مسئولی در جهان، مثل رهبر شهید ما با علاقه و دقت با اهل سینما و هنر تعامل داشتند؟
🔹
هدف ایشان ترویج فرهنگ و هنر در جامعه ایران بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/446721" target="_blank">📅 17:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446720">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15bb4eea1.mp4?token=R51vfp-ve6jhnFk0mGIzxwZCD-p5f3_tJOQT4J2ga0MwYAd4k4aBKDYw__nDyMR6BDdFd8f79BaZKYjDCyd3VgWXmQ5jqOlnNGx1edQLRoXlYsLc218CvGAFJuhOCkHYss8jGEuH-weNnCxUmu_WdQdab_0q6RFO22b4hgp2euTNdDhU_M52by6-VzVG81nZLTxLGb5yjYZxm0YZ-gwA2FstOOHEYkqXEeMK4SRVubP12JlHyr2K68l5hUbfQDqgY3HFrGOzEYl-7b3jVrdRYrZ_CeAvy8cAwcJVFy6Ky1B2Hr1qlEVP0CMY6SI2FgWJseowtQZp3YTssuvBojC6hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15bb4eea1.mp4?token=R51vfp-ve6jhnFk0mGIzxwZCD-p5f3_tJOQT4J2ga0MwYAd4k4aBKDYw__nDyMR6BDdFd8f79BaZKYjDCyd3VgWXmQ5jqOlnNGx1edQLRoXlYsLc218CvGAFJuhOCkHYss8jGEuH-weNnCxUmu_WdQdab_0q6RFO22b4hgp2euTNdDhU_M52by6-VzVG81nZLTxLGb5yjYZxm0YZ-gwA2FstOOHEYkqXEeMK4SRVubP12JlHyr2K68l5hUbfQDqgY3HFrGOzEYl-7b3jVrdRYrZ_CeAvy8cAwcJVFy6Ky1B2Hr1qlEVP0CMY6SI2FgWJseowtQZp3YTssuvBojC6hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر حسن ابوالقاسمی: زندگی رهبر شهید به قدری بدون تشریفات بود که می‌توانستید تمام وسایل خانه ایشان را با یک وانت جا‌به‌جا کنید
🔹
رهبر شهید اجازه کوچک‌ترین فعالیت اقتصادی را به فرزندان خود ندادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/446720" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446719">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhYscuKYHtDngjMNVfTy1hNIYoFAxniEJ6hKqH2Byh03aO8JHLIizNVgHbV67ZvHMox197-Dq6aNFoGz_qZIliwfwsUCrX5U7EF2P1bYLVY-IkHt15m60oYRg2x7JuxBrCgX37W2FedyNBZIk3HoS8k9WH8SQlXf6VMUP8FlhHfwFHh8jH3YvxDKy46qCuOwVvOi-Nos7KMa4sKC44aVuxuObE-ex1IvlC9S2UJCX8zz7EtAsT995IR1cUPj5AQRtEuzETVHva0jHlrUO1pkOXFo52DoTpptLuUWwWAG6KrShOYC1h0HWoI9MkCetSpeaJ3GJ8oNyndnHn4XURBo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار اعمال قدرت سپاه در تنگۀ هرمز
🔹
نقشه‌های منتشرشده از تردد شناورها در تنگۀ هرمز هم‌زمان با حضور نیروی دریایی سپاه، نشان می‌دهد ۸ کشتی از ادامۀ مسیر موسوم به «کریدور عمانی» منصرف شده، یا مسیر خود را به سمت آب‌های تحت مدیریت ایران تغییر داده‌ و یا به‌طور کامل از ادامه حرکت بازگشته‌اند.
🔹
تاکنون هیچ مقام رسمی از ایران، عمان یا منابع بین‌المللی، ادعای تغییر مسیر ۸ کشتی یا ارتباط آن با حضور نیروهای نظامی ایران را به‌طور مستقل تأیید نکرده است و علت دقیق تغییر مسیر احتمالی شناورها نیز به‌صورت رسمی اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/446719" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446718">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
دودَمۀ میثم مطیعی برای خون‌خواهی رهبر شهید: انتقامی مانده است  @farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/446718" target="_blank">📅 17:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446717">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a0f3176.mp4?token=T2MldVYgMyZM_xP3y4bjtB-QkDUFFb4-S6p1uMvZtoLfCIl4Rr_QiUZrBETb3nVhD7kqfK6j5OJMqfapmBt748Va7FkyQM7CQvQKgeEDZCPGR5iHrS1FSwgZl5hhP04vnB8VkLyYes1GINOeg0fv--YVTgy6rvyiP-hlA_OeIjBIYbGweEOdLJ_tykX6vYR3aFrKNeBPzvMWGYkHXA7QYApsqide9siOTD14dggcs01SPMu3TuSc_BF5isHxZsZTvQCxPYD36lGIJgrwcd9tYi5bhwm-cKN-3e4WA1OAnlwjTpdc0nrEa_YrA1YWm9L4oJIoBY7fNZFD6_gf1CIEZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a0f3176.mp4?token=T2MldVYgMyZM_xP3y4bjtB-QkDUFFb4-S6p1uMvZtoLfCIl4Rr_QiUZrBETb3nVhD7kqfK6j5OJMqfapmBt748Va7FkyQM7CQvQKgeEDZCPGR5iHrS1FSwgZl5hhP04vnB8VkLyYes1GINOeg0fv--YVTgy6rvyiP-hlA_OeIjBIYbGweEOdLJ_tykX6vYR3aFrKNeBPzvMWGYkHXA7QYApsqide9siOTD14dggcs01SPMu3TuSc_BF5isHxZsZTvQCxPYD36lGIJgrwcd9tYi5bhwm-cKN-3e4WA1OAnlwjTpdc0nrEa_YrA1YWm9L4oJIoBY7fNZFD6_gf1CIEZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمد نجفی، بازیگر سینما: سکوت در مقابل شهادت رهبر انقلاب مایۀ ننگ است
🔹
همۀ ما مدیون رهبر شهید انقلاب هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446717" target="_blank">📅 17:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446716">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f42a2a3e.mp4?token=ePshLNGrRIgnTjPzCj7GXXGVuZ5CVKub_EA647W7iqF4oJli1YOvgB9tz3EuiNYYwK2UY0k-02qauZg5c4eAvfqBm5OBMlkI6BiCZpDuQLM9WPizUh-4bo-jZxFja6-XMIY4kZ1gj_y3EhyvBpW7PqHLEa23Bbn8wla9CS4AS3sRW2Up63tUex85UgDpAt7ejnskCL7KCdqegAhy6E2qV4JIfr0Y5fEYTlTYYYrjavhmz5e5Z4ZItDejhC_xnORfhb9hvXktDFzpja78W0JSkXZZGB86QLfpKQ7rFQ12TOGLA9Cm6hKHM3ULgdAIiumaqKOFpYta2svU16pxBntjiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f42a2a3e.mp4?token=ePshLNGrRIgnTjPzCj7GXXGVuZ5CVKub_EA647W7iqF4oJli1YOvgB9tz3EuiNYYwK2UY0k-02qauZg5c4eAvfqBm5OBMlkI6BiCZpDuQLM9WPizUh-4bo-jZxFja6-XMIY4kZ1gj_y3EhyvBpW7PqHLEa23Bbn8wla9CS4AS3sRW2Up63tUex85UgDpAt7ejnskCL7KCdqegAhy6E2qV4JIfr0Y5fEYTlTYYYrjavhmz5e5Z4ZItDejhC_xnORfhb9hvXktDFzpja78W0JSkXZZGB86QLfpKQ7rFQ12TOGLA9Cm6hKHM3ULgdAIiumaqKOFpYta2svU16pxBntjiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن محمدی‌پناه، مداح نماهنگ «باید برخاست»: مردم در تشییع فریاد می‌زنند که باید برای خون‌خواهی و انتقام رهبر شهید برخاست
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446716" target="_blank">📅 17:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446715">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs5ZfikQUh897QisrcM8pzWW2yP_mjnlRXhJ_2gBFgw1I_KTaL9NQZO4a_LtgJZ8Z-VjAQZWXMveqnHV9oWnOqnUBAOSbN7qqaje5Ab13DRPdSVtt2ohfCvs_nkrNfNnWze1-mJFNG_zkdYbPJ-ktok3YCWDqI0mJ31QZI0mwyEx30hlgqtdDXqYw4lwQ9R5pteO500uXpHShDffTtzPJ9WApzhSVcyAMyMdjba9EkkAopEjHLg4IJ2KEIwEU5rEwh56vlpIBvPYxU5Elj56Qx4mUskj-Sv7yvVkCcnmb6J6x1NzBNLbWDm8OQ5WoLVegqhpqS8RSoWyqJbk1gKUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
زهرای من به‌فدای زهرای رهبر
🔹
قاب به‌یاد ماندنی از مراسم ودای آقای شهید ایران در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446715" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446714">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b5a07723.mp4?token=bSaXeDUjtmBtdPoSpPhvIkCnoTXBPFPTcx-P_K92BceTQXcxfGnvG60hPHasjxw8JFZ1KUaEGZ-jI-y8YRimanv5SQHsSz5Y_Vdb0ahylAfInc1gYnGwFvjUJOvLjhuLxgwpFEA3i2ejOjM4qR6OwbT-OVLbSdeTUH-N5uXZ_eR2B6K0hzB2El7lCaPPHddHINXjC_8GN3HaX8svcG7-cKOsxqz9fKcS_Ax7ICk2ZuscnUkwta31AY136EEiTRbi6m3EkrBcX9ndy-HwYc1wKOFgE5LjHmiIEjc-3lCakD2V0h0TXwjFmzizmdkUvq8lEcscX3PQZOG4A-4yhgqHVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b5a07723.mp4?token=bSaXeDUjtmBtdPoSpPhvIkCnoTXBPFPTcx-P_K92BceTQXcxfGnvG60hPHasjxw8JFZ1KUaEGZ-jI-y8YRimanv5SQHsSz5Y_Vdb0ahylAfInc1gYnGwFvjUJOvLjhuLxgwpFEA3i2ejOjM4qR6OwbT-OVLbSdeTUH-N5uXZ_eR2B6K0hzB2El7lCaPPHddHINXjC_8GN3HaX8svcG7-cKOsxqz9fKcS_Ax7ICk2ZuscnUkwta31AY136EEiTRbi6m3EkrBcX9ndy-HwYc1wKOFgE5LjHmiIEjc-3lCakD2V0h0TXwjFmzizmdkUvq8lEcscX3PQZOG4A-4yhgqHVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان مدیریت بحران: زائران برای هماهنگی اسکان با شمارهٔ ۱۸۱۱ تماس بگیرند.
🔹
زائرسراها آمادگی اسکان بیش از ۳ میلیون زائر را به‌صورت هم‌زمان دارند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446714" target="_blank">📅 17:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446705">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhDiN65RW51zYKnHaUCm7NkWc-_FLORhuvViij-T7mce_DQoKeAZKmQHl0sNK47ByBXcbe9MYe0ysNsCo12nshxxU17-Tx-nvV1DCP27RnnWgjVPEbDKZjQIyAyohYcVSHnG1zk5LkGoL5ALoXBhnML__LrkvVEtOJZf_nRjoKYpnFkmfB9n4U8VHKu2W8un4E2COEVuK3aSmi-XPRWEPNoBO60t8Nm0pXAoUeiVDC2VkDd3uv6mhjvWxGMV68u4qQ69ZZd_CnMXQlH8lekDKBJYcjoZy94wuIFeA9pVbmCBXMB39mA6bHSMKQpX4OfQhcd3fCOUj74tycD43wY8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFoI_6jqNKLNugtVUxbVDnNIBjZRqlfdloKZgkL1FoNwNzK7SAExFFKRw2Hwzxcb-IM5olWgU8i-00XjkWg6K3COz-gwtGUJM_8Mb2UrK3Zu9DK0088r5wM8ci7a2syDBS_p8GwWTvvWtTFf_kNpRz1yN0iaLH7UxrNU-L_uAr-agE1YigLLB0XT3PtCE2G3tCBuCAbekaRUWAiSXs3bxMVFrpCVdbfYzoo_ivoNVkfzgqILpaJaupz52mozRxaPRx_Jqg14LQuJ0BYOWOyOGk29q1GOV_yDYUGa0Zzgt5SC4Lui_qiRezSyWDqSNWuM5hZ7JuISTEzoX4RUnxSnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6ElExn6T4sZ-zzXphrYkd1KoA-JwWmXGbybC-ucb6ZYdBM0DTre_WahMN_qHowBRE1Exx7UP17M9R48QjgNLv0dKNxQth5LSYYpKeK8h0nmgQEzUOpl8mrnZ-HJ5eOli_2E-AhtCQBkbSONM4OZuKjGBxQbRrlsQJ-JrDDVSnGQaEiYSnJmaa4oZbJLtplZ8AetgCtPmR12guQS_s8SXnmupjBglUIIR89sbQ5ves2E7ji8yzOqCbGiKJxAbxXbOEwnZGiUZbY7plLfjLeoCAwby0n0L7IG_mxzRVWChjRsbu4YfKt7lkQlyLk4mXXU507pLIXOgqlrwpVMhh9pLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8xxcIahAgFTiQSVq7fBnmDN0u-4zJZR03Wf4w5AirMGu2I0fL-eo2MIj13chvSyjjfboA1HDu5KfGj_k8TzUegyt7ASbfoXbP2dQFCpNNcVy9KnEkUhbB3C-SOeA383eiSU2P-czzAH10FZb0wIEvRC8eyQJL84w9cU1_gOEyAiMqg_hqVmMcjDdsvudXWbrjNMC6o-Uhce3Huolwhav2aBsHEGbi60UnbbP3taftTsbTaHlB9zhU4X4Rp072bWSmWwDUopUVefzy1Wpc5Ed1mEcBuw_9NUMOsnbLFh1VpPK_afXcKvyTIMo2Ja9jrF9RrWnSpt4PfcrAZrXWhQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rO8fdZuexROj3iFCZztUKRzu1QXKEg9wLQtBWgYc_lo9FLgNvEkx3e_5YpjWzKqM1vJi39AbV5fqzDyG8j0KyRgiFjfVfoZNZ0UEPClDIBInTCTjtd0zQVmrh1mWUW6hzUg2CfB1N_VOhadQfKhNbWcDYCS3ERGu07Oq6IxuaUUt-R8k7UGTVrxlrVve6GHMlB7Tlf0p2pgt25rLiRaA7dqW__YROh_uxhzHY7n4gfPWmDTGsHf-EvgqB-SEqPRwY1S4JfPbVbzo8-W3tcLoPpXptrUWLf6W5Cu4qlocgVjku61CbpQS7eJhyWSAhmrw8rpojI7qOLPpX_2zSBAykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKHqvnVGsIW1VE9AuUlaxNbv_XhUfjvTEmnG_xIzjWd1xKxi1hzi0LmBsDlZZAmJgfl0CQ-xSYOLW_N5aM1OXLfefustTLxzsNODQS2a8UAXEwGLRY2rSAuWtI2xLyEE9kaFqb1GFV7XSlY44UDYCAOoEBhJLXM2sCJUx9wm3a2GasF6fYvMxLMQsVh_pobnWUYdqWKoQSlbL78-vgMrTiMay7hfU_J683CSSv-jHLkMyY8dPMs9gaBdH-p7Q8m8IUHnXj2NqewSiP3y7nMHW6Pht6j7mrXxYnRH4rVzR0xIqPvib75n5HNhsNfBqNovSQr2MaJzNds0J5tGQB1vZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCImqjRbDi7EqXgc7UtOYrShtfjgAxXwrpfBK4JP1OuFXKPxWaVh7HSQgL9qaMWORtcTfYza7GMoccU3nkAmB6GLXZZBEGD5bK0gHz7EfQXqb0Q7OOnCe6_GojL56rDtmRqCnAOieTPnbcBApY8qkJfw9HMC35dZOlrtz20TJeO630KcUwbsqb4sa8O8krdl_3b11yDHK9kXZMurpS8yH3Oorca5Sc8jTBvbBmP49O4qXzVpFf4DOKbXG50h2h4tNM4uW7BQrxXNlF9uiH8Msn7LDblfk05EydovMtwMBfreoutXMSUdEr5i2qIe3nrvquNw9vJ-WBpsAvmuKce0NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
خانوادهٔ شهدای میناب برای وداع با پیکر رهبر شهید انقلاب به تهران رسیدند  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446705" target="_blank">📅 17:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446704">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkIXe81zXhQUKbXKyvdiHzY_3f3Xo9W2XnBOq31h1nQjAUL2o8Rd7SauC16A0YFNAcZfCTGcyXLJMBoPQnyiR4j3E6OQggXRprdDtrz_nYjs9RSzGiImM0Z-lF8YYE9Q5x0RqKbbONizam_yBR3WK1R1zgYKOSPIRD5AYtAHSbMEQkJu2UjuTYKrlnd5lRywrQAVrf3D2EWbLyQ3fF2w2XAyU-FFR7rpKj0OgKnYm6DS9S_-esTNHQmmtdEIPUnvCY1KikNE9WSjC2JMQ4niy_WRu8J9tvXsQUAGhsdpk4uFjXLRdwlXOPweD26ddREJ-5Pejifj3DWvk2alvHISGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لغو سفر وزیر صهیونیست به نیویورک از ترس بازداشت
🔹
هاآرتص: وزیر امنیت داخلی اسرائیل، سفر برنامه‌ریزی‌شدهٔ خود به نیویورک برای شرکت در اجلاس رؤسای پلیس سازمان ملل را پس از اعلام برگزاری اعتراضات و درخواست گروه‌های حقوق بشری برای تحقیق و بازداشت او لغو کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/446704" target="_blank">📅 17:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446703">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
خوشا به حال کهنه عاشقایی که رفتن و داغ تو رو ندیدن
🔹
نوحه‌خوانی میثم مطیعی در مراسم بدرقۀ آقای شهید ایران  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446703" target="_blank">📅 17:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwgElRaGyTuYx_c2o0qxImPxL0DPsFnTEF10iKtpHkyrOV5U6sstMoufZk6QL22lYAsxqO41AkUdDJMO14jPrPInldvuRmW2Bln5qCQaAALhtzNpmSve8W92TM0EFeDRyu2S_-3JBlniHhVSdtxs2vP9GOPbcLk0MxUvdsfFSoJwex0TtiwMLnwTm8FLvjzTfSWKYdZwYKlwbyczKkJq66Ydo5Aqc8cgnTJdHZ-QDngBOBsNGP42_6VMcskK1UPlr9Z88PzZce375oP5f60klLeCzBMa4OmaDLK9sc3YsE727V3jhHj16kNJI1zBphMMUo2VWum5cSfJjOhvZWVP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuLmJC__wW2O8aD2Ck1ailZNzlJk_4ir85jKKdQ5wYe3YRN7Unkwq8J-FzXaiBzc0CU1BjNfukM-onqImTBqWEcM-OgMSnj6b9Ife_ZUyN9PsG_5HqM9qPtIBx5445zjr-8L5Xg8ybRPM8DbOQQQ1mIdxZ7srrWGSXFqyGMg5tN18lA43pYx5WrAbqjgfO8JrKEvXe2EP27vqe5NikZt_jfyE4ujsTw0EHQ79SwGov5CrKxJZwmeEfnkObWhIK_pK27ENapnxLYhmsuL7Qn-nFYgCqm9cWceEd4Bye8WY5yv8WiHMtjV07S1l5kWNKUKSKVe7QMzCT7Q-wTPfpBS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h94Wq8xqwyBNpehH2MQ7do9qWs-c43luj2zMTBBwxkd9IMiIxSZDapaiFc2nU4qRyrnwKrojMLhRIE3FHMIvUd0v2v7lfcUAl8pJ-a19N9qztnW74gr2lmhsTi_tO8B7Wb3hWZ6agVGDtVlGvS2rZdyLw9Z4C1K6pxEBXcYBZfWgk4SpAL3dh85W5h379ZgC5ZRQzb9HymRMrRONHW9_CggWh3g1PH1iOTvGrtrWxiHgs5GifFugTemNf34Hq2wauQe0VxM55x4lgdrGBmya2gqIP7HHJpy3WwO8iyllKjlahS44BowMDBltldLvltCmjtW7Z2sWRiyh3I01M040hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVtNPA5JIe4GiTdl__afw0Q3Z4lQKlX1fKJ_TmPe4-YxjOy7xt7-zwualF7lMOrEOW4k2avC4AsE6fPjxwxnuhvSu-hLLHo09KUIFqHNaNnKPqUdmCuV3wVKhBQRA0oi8kDmQK3ihZEQ9rv10wfazUmfIsdyEDBf6Z0Qi9yZcYYuhq-Wa8gA6zwINrWCMksWbIEM_ucE1Frf9z37vGqVKdudIlMBUF-xcpJJihlxYHvTsbNh6ibXb-5eyhdehqu2FBCXeTqSpTrWzdG3koIhHpsy11j5Sg3mQl9D5ujV-DseAbi7bTAeMp1RdXDV5iDD9N0MgLAzNbLXZIyNp4UCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heNXbCcA2Scq_QEen5J22Foht8QWpHXuOvETJnznaI71YHEwXB3bNh_ZY1TYNICKL8Yewh_JQKqk7Xm3JSabbdX6AVtoqovKMwKPLqs_sOkl5hD1WMc_qdYe6tbbRdwVdGdkEbXqYcZ2b39HcUZQldTjdQzo6-HzZE1iyGKaEtvESiiEEoSKHtZoTIu59lKzzXZkm41-bFRYwBeJkKEid4jgDwArmn-S1ZjauDgteC2fQURoeCgETTaK4AKzz6ML3HhsNWj0GIBPb2TNDoWufOXhufsU8-KPV7iRv57cop9K4VeE0_p3tE42dr2WceVpM9u37BlFSJaK8opha2edfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nn8Xi2eL8Ox3fxv9qvnbcrrUxXpMSfLQ0BqwlMhpEwSAFFNQr00pyZZi82_itgQm5oajhIa2xQUWAetS83SFpo5iMUYGjIWKY3doMsg2y-kmUNag8-oo5dAtpbOvgv5XhtsPTugytITF5boBSCQOR8i0-LpSBAYZyQvQ6AQmxFha7ORJc-ArmByDCi8JxX65XZR7vSyuATgkpS3I8owK_fYFHfi0C0UMYOMaPzsoNuLxpAhh-ybYjqfUAZ_6GknFrSKihHA-mIpukIRs_xrk-L3xqBP57rbiw_2QWCYa69EuNjlaWuROLLmnbDN3pVK1-kWqRub78InmbQiWrHHYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBVWXEQ6l4BGwtR34dFXGbQZjJpEA7qX6aqu6-Xb8jOGuNVQ1giV6L77niHWo9rf4NZGGqH1OyxFtkJutCCQwPBsq8zLTjNxNsIapf9YoGfnt26RONO7tZxvNaKUJHl238LjUhnLFdFsXcLEwbUlJd1DddgrcHNbMc8Xw5mDCBKZnHMaIUM3pDeVPDbsfjnSv0in841b-A90wO9piyWMfT9fZSAVZvVzRtuUg5Xjy5iGxqhwNEiO2lm35gK2ZiaK9uObzpx6X4TNCo4sps_DK39sQ3Y0qTBxrvHYlHEDrntPkFs6XvToSuSTb4KrA_RCiLRVxOdVtthwSRKsIObLVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خیل عاشقان در آیین وداع با رهبر شهید انقلاب
عکس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446696" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5954bb030e.mp4?token=MSJd7G8d_ypYGgkIqQ9e-2dT8LavS7taPPmllGGQs8ihC2Fzfrh-k92V7m6Bv8SZFDiOkHjFKkAcw8R_GXgWwxBw0XranPFhmgAJmqtgOmdb6sHne2ovSUqUrcXbrZdEzPv1tCrWF8RxR6t8UiPZ7u01pussYjPKvSej5y6_70UfzYNJ-tUwxzRjCoqs8sHx6i6EZG1Sv06tvnbVPpRwkCmabcvu8HUjOkFdsnl1sba4cirMKEDfP6o4WDP2H3dPjevLkmEs44IODIEF5KbkpPV1ZJaeXzY_MY-EOgU2beLBaQD2pGrL8QlB_6kMZdk51gLhbV8nS4XXyBTOO25hGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5954bb030e.mp4?token=MSJd7G8d_ypYGgkIqQ9e-2dT8LavS7taPPmllGGQs8ihC2Fzfrh-k92V7m6Bv8SZFDiOkHjFKkAcw8R_GXgWwxBw0XranPFhmgAJmqtgOmdb6sHne2ovSUqUrcXbrZdEzPv1tCrWF8RxR6t8UiPZ7u01pussYjPKvSej5y6_70UfzYNJ-tUwxzRjCoqs8sHx6i6EZG1Sv06tvnbVPpRwkCmabcvu8HUjOkFdsnl1sba4cirMKEDfP6o4WDP2H3dPjevLkmEs44IODIEF5KbkpPV1ZJaeXzY_MY-EOgU2beLBaQD2pGrL8QlB_6kMZdk51gLhbV8nS4XXyBTOO25hGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: خودمان را برای تشییع ۱۰-۱۲ ساعته در تهران آماده کرده‌ایم
🔹
در روز تشییع از هر نقطۀ ابتدایی که بتوانیم خودروی حامل پیکر را وارد جمعیت می‌کنیم. برنامه‌ریزی شده که تا میدان آزادی و حتی پس از آن، تشییع انجام شود. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446695" target="_blank">📅 17:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
از پیشمون میری آقا خدانگهدار
🔹
مداحی امین قدیم در مراسم وداع با آقای شهید ایران @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/446694" target="_blank">📅 16:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083dab9558.mp4?token=EQ-f__rNsxaXCyE-a1uBJPqMqOJmWURomqLCQgEKtW17e3KJsUkJOPAivF9aAOaeDsOsyAtQMgIhuva2N41kcY1hfFoxIOfO-fIw86d7n0lg6YFqpVH0e3-zJhz_RhNoU0AXRlWHx3zT1feZ_DfS9fT3ENBeoJqn1QyHVlUc_rRAgudcZSfBSuJgkzwyEVs8FnFENJS1yTjS4jCQiaz50TcesRjCy3RA8UoWgRDQfll3rFVu6ZLVfCe2Am8R7hGPewCcIebsNargwwE11xKyEJsSWhGL5h_ReCasX-EEeEQ2amHXhHXYmuCHVpdCUleeTvRByqxoVNwsvaqMLSqrLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083dab9558.mp4?token=EQ-f__rNsxaXCyE-a1uBJPqMqOJmWURomqLCQgEKtW17e3KJsUkJOPAivF9aAOaeDsOsyAtQMgIhuva2N41kcY1hfFoxIOfO-fIw86d7n0lg6YFqpVH0e3-zJhz_RhNoU0AXRlWHx3zT1feZ_DfS9fT3ENBeoJqn1QyHVlUc_rRAgudcZSfBSuJgkzwyEVs8FnFENJS1yTjS4jCQiaz50TcesRjCy3RA8UoWgRDQfll3rFVu6ZLVfCe2Am8R7hGPewCcIebsNargwwE11xKyEJsSWhGL5h_ReCasX-EEeEQ2amHXhHXYmuCHVpdCUleeTvRByqxoVNwsvaqMLSqrLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن زاده: از ساعت ۲۱ امشب تا نماز صبح ویژه برنامۀ وداع در مصلی برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446693" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446689">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnB99oFhMdL-IRiW8JDMSXdNBfhqqBENq0wH0a_mUq8uQNjMxmUmh3ve2i3trvwnR2JM9dmcINKcQ9vSOCfFJ-UL2eb323ciUf9dh-ofo4a5F6S7TD0CGqC6bxnjODFaaGcLCLfLvmhCgqruI86mLcm3xae2HDqQqrnAIyFRdn96Iyrv8Er8BvJNsSLbiaTlYgXaqavlQKrABUgvGXktvsNTfXRJNGXfSzbFt711vuFPKgc14lplfsdxTN9aIiUTjeTGaG1nhI4LHpma4YrMqBU0XMkESI_h0y6rpbgWotbekA0oCy7jO0TJrgnpQL1kGUvyNRZxy0MCqRbkYy7BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjyMU1uQUwkim8bTqZI57NxG89tM-R-HfOqlFuz18yq5Xt8gTZ1Hhes89K4WzB2y3X1En4U7jyP8TevJ7Qnvl1bPJHMLXm22ibxvaWWT54kaGusvadjZGY8zCTTx2mH1YNtGQuLdb04ebM4TtMNtarlVHijSvVUuJbiWhvDDpUMTggbBF4Lm1qo1xhEWKk5CwL6HDlGHnUHlg1CogCc1e6DlrnW_LTkRy3jLtxN5VaJEPNyBiPIKrDjG6JL7cm_SQLwG0WrRdqNt6epWT8kUHr8LByT1OuAH656dYJeIiNfWnsyh-eVCOGD90Ce4XFk1jCFKzVtrMRbD2XOJy4hwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPu_Olky_6VGyf3wenIlzdIVVEvKAjpzOOPneDGSSwQC3pUEhZQ5nTZUWwu4YQw3vqSOdv-XlYqhHwUpzEtpu_x_NxTnrGjeBmaT-yJAq8TF4hR2Us44EGccCmutG6suovdFd9HkviCOHS-KTXjAFrgIV6mHHZHNMvWszl2PGKuIbKEe6hTIiZCl04IB4Cl3aWOzgWJpgUQgqbLWDCFGoXkOlj4ISDsnFjuW9OP0jQk7-UjiaY5uBqwx_E9RsTZ99jOJnl-KxqcVJeuMZllm3qBc07inY-yfRoOeHMAc12fptojpVqgtyVCPE_vOddLg7TkbtcPdRt23oOCHZjROig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2V3DODu8-sqKb4Y6D4Kg8iVSQ1dFz2Jcag3cyr9iRHKw4p7q6Z-NwsYdNL9ENMgPSS3BhBw0XP3l-f4b7v-kKuPYJrc7EQVoANMtdKb3KyQoqbKYYTeVWHbkiAdk6jDO-7aQ9zOlVdSKmKj0v5TwNWRC7e9htkBK0FuDfEbdJAII9CEaNqO1KuFoOQYq-945hZ_uubfmSb9yNlOP26le1lXmq2qO3jyZQpr6Uw198O0s50CdABe2TbJRV807mCHI5bP08h3pOI_LxnpWv5g31ihnRGXpoULs-PB6L4goeCY8PcolbEmJO6fobhZtUmdGKp2mWndk7qJAaIczk6Ezw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اعضای شورای رهبری حماس و نمایندگان حزب‌الله با عراقچی دیدار کردند
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446689" target="_blank">📅 16:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446688">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7a8773584.mp4?token=e-0y8ODaLrJGxwa8flI1ASGQhvfDzrqeToLXCemcy2f42YTJSmo3AU0k9Bx6gC6XBEN4uS85JBa1KDyxIzjNt1u7qnaAfNog8tt8iGCQ3ezq9-d4r1oXNRgEuqr0m6qUpOms5PiGb4bqAU3NdNC5xGYmXQcOxXokA4z8CRRWOH97Mumqyb6O_PMPxX-WY2adu-LvLoFOvjJxhwo9Fwze1P3mhU-MBnHthb5eoeHeArRUbgrXDQtzKQlVgTzkjOUrmufvPOzMKWwS9fQXW87agV7f5NXbvp_6_y90hYkjNiULenUgKfwSQLSjvGwcW03HN73x6DOzx_fa3PvvdwjekQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7a8773584.mp4?token=e-0y8ODaLrJGxwa8flI1ASGQhvfDzrqeToLXCemcy2f42YTJSmo3AU0k9Bx6gC6XBEN4uS85JBa1KDyxIzjNt1u7qnaAfNog8tt8iGCQ3ezq9-d4r1oXNRgEuqr0m6qUpOms5PiGb4bqAU3NdNC5xGYmXQcOxXokA4z8CRRWOH97Mumqyb6O_PMPxX-WY2adu-LvLoFOvjJxhwo9Fwze1P3mhU-MBnHthb5eoeHeArRUbgrXDQtzKQlVgTzkjOUrmufvPOzMKWwS9fQXW87agV7f5NXbvp_6_y90hYkjNiULenUgKfwSQLSjvGwcW03HN73x6DOzx_fa3PvvdwjekQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: قبل از هر نماز صدای رهبر شهید در مصلی پخش می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446688" target="_blank">📅 16:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446687">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/073eade277.mp4?token=arH1f1aaJQEm6xoMzclMRnVU7rq9y0E9963RfASsk_n5MsP8xASmgW853P36lediTGhGwElZfpNUAfqWLbQwU0ZoXmhQTGN65zL5s77ppLzsugesYWXqT5pqQScGc2s11BR_xkyicIBztlp1No4RgIVYGgAsI0HH7RVbaTLR69lqHd-8INslRPi6PiQGNQatQUVXNRRoK-RpNbsSzynfmSlCcvR21q6jhdjBArQywu8t2kPiFjOr6yC1XgswALK570VW1BLQptK7uTkT69BmFtJsudpS1RkNJv2gZ7qfQUFSrqpGRMLYdDLV8Hzu4EmIcMR3Hct8o38XXDOn_geZ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/073eade277.mp4?token=arH1f1aaJQEm6xoMzclMRnVU7rq9y0E9963RfASsk_n5MsP8xASmgW853P36lediTGhGwElZfpNUAfqWLbQwU0ZoXmhQTGN65zL5s77ppLzsugesYWXqT5pqQScGc2s11BR_xkyicIBztlp1No4RgIVYGgAsI0HH7RVbaTLR69lqHd-8INslRPi6PiQGNQatQUVXNRRoK-RpNbsSzynfmSlCcvR21q6jhdjBArQywu8t2kPiFjOr6yC1XgswALK570VW1BLQptK7uTkT69BmFtJsudpS1RkNJv2gZ7qfQUFSrqpGRMLYdDLV8Hzu4EmIcMR3Hct8o38XXDOn_geZ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: قبل از هر نماز صدای رهبر شهید در مصلی پخش می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446687" target="_blank">📅 16:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446686">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOBUh6H_33FZgCpNqZ57bwsd7-KGVSg7vz5ODCduvfyIH7KWZYoopQKHGR-r7tGw7R7SNl2mgOlj5YQs8CHfP5Fo43qjTuF8HdidCq7yf0KttVWPGXg99RHbiwM2kQluW4qcBKRJULAL0_ZLRyMsiQuTCLnX_NsnkEas9yw8OZx7Jjz0DNiLoJmUr43O0X9TsDHjuZQgB3lq1hEI65fowAv6MBkGDrY2X850kifx_e85h-b-vsWIqGlC-PCbos8pcC4DS0G85ziIgraXk91ssKCsZPQXSQ2ZRBdhXb_TwkldpkNgfgez26xI322oigdZvpynABMuOoo1uIlq9JCz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری تهران: از ساعت ۵:۳۰ تا ۱۵ امروز بیش از ۲ میلیون و ۲۰۰ هزار زائر توسط متروی پایتخت جابه‌جا شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/446686" target="_blank">📅 16:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446685">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگر در مراسم وداع و تشییع وسیله‌ای پیدا کردید، این کار را انجام دهید
🔹
شرکت ملی پست اعلام کرد افرادی که در مراسم وداع و تشییع رهبر شهید انقلاب وسیله‌ای پیدا می‌کنند، می‌توانند آن را به نزدیک‌ترین صندوق پستی یا دفتر پذیرش پست تحویل دهند تا پس از ثبت اطلاعات، فرآیند شناسایی مالک و بازگرداندن آن آغاز شود.
🔹
همچنین کسانی که در جریان مراسم وسیله‌ای را گم کرده‌اند، می‌توانند با مراجعه به سامانۀ «پست‌یافته» اقلام مفقودی خود را جست‌وجو و پیگیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446685" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446684">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b76fa05d.mp4?token=WU_I6xA7N9DVhVL89brp7VRbcnO4y9CQOEaVi2ujrlQ0wG--v6jpSEs0pTaq3rgOoRUM9TjR4ojXZry-oKY1IW5Od6F1jfpGygIv9ajNNyLyqPKtZvz4vJPLF3E6q-ZPAVm3-RK9xxi_JbGs10f-HhyGiO_NjnEyG-RZbrQ3d0Hz15WBz72PyptcEuomyS1fspmU1RAAbCKLIyR7NKDZt7LUchhALsnS5wJcPMUIvelAy6zBNcXQdlHoVxSMVLCgFCjn9N5JXytqpOoQp37QW1ZsuX6bjTtlkWkzl1Ad4Z_eAk7wZXOEcHu-fLpXBnryqAWOkqwYAkHgqCZOpCrBGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b76fa05d.mp4?token=WU_I6xA7N9DVhVL89brp7VRbcnO4y9CQOEaVi2ujrlQ0wG--v6jpSEs0pTaq3rgOoRUM9TjR4ojXZry-oKY1IW5Od6F1jfpGygIv9ajNNyLyqPKtZvz4vJPLF3E6q-ZPAVm3-RK9xxi_JbGs10f-HhyGiO_NjnEyG-RZbrQ3d0Hz15WBz72PyptcEuomyS1fspmU1RAAbCKLIyR7NKDZt7LUchhALsnS5wJcPMUIvelAy6zBNcXQdlHoVxSMVLCgFCjn9N5JXytqpOoQp37QW1ZsuX6bjTtlkWkzl1Ad4Z_eAk7wZXOEcHu-fLpXBnryqAWOkqwYAkHgqCZOpCrBGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم اقامهٔ نماز بر پیکر امام مجاهد شهید و شهدای خانوادهٔ ایشان، فردا ساعت ۶ صبح در مصلای امام خمینی(ره) تهران برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/446684" target="_blank">📅 16:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446683">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875ec359dd.mp4?token=U3bSDVDtpztmnadvWsmy7-rL5my2Pc5-mqBbVYCjBIbnJtPPtT9Y83L1XSp7RJCjcguD3Oi6Bnrnp0GG8PcGEiEXEbafVLyH_HXws-NB2A3D51ityGIv-IIpq9_cEY0Vg3BXnirg7KybRLPrA4TMmkS-TDVNkpxPP7ZlTMdarUAijHDsTi7lu_ZRacDuBZsvr-gFjtP4r_uXnve27DbXyjcdVB1-DQeINvoXnDO7clmWYG2ee70psk7hr2i0lYO4CxXl-yEHU-VhTUJ4bXOAhwukM_RTkrPdDaaF0Y6JydBWAdZTLqcL41LTkYgtGFXGtVPKUTm1iBLUcnDwhN2Cul6uOb70xKqVGWXx_sjyQ76dw4V-8BVtnhVqvx4eJvylzF7gwLu5maAgRXDVDihOeqNQRIT1gZL_z1UZ7WHl3F6QhtxYfhxpjxRmt65S4PeVc_e82JXn3kgCop90_XTN5n7bTXs3_hcGYshA7BnZ-IR8gu13SwHnOz9fvk56YpeBqkkwQRobMuShRmwu0tzdX7arB7zep9uXB_jscoZrHJRMfXlcV9tdmPPIvhEdMWGfYeLEQ04ewyrJUsW6egmvDR6O57cTtdVQKP6bn16RYLuLYpwvsnfGUF4OhMxFTTtKWGllvoa5rZ8OG6J9NAlLSbkzNi1tMdFkby4sfL2YAiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875ec359dd.mp4?token=U3bSDVDtpztmnadvWsmy7-rL5my2Pc5-mqBbVYCjBIbnJtPPtT9Y83L1XSp7RJCjcguD3Oi6Bnrnp0GG8PcGEiEXEbafVLyH_HXws-NB2A3D51ityGIv-IIpq9_cEY0Vg3BXnirg7KybRLPrA4TMmkS-TDVNkpxPP7ZlTMdarUAijHDsTi7lu_ZRacDuBZsvr-gFjtP4r_uXnve27DbXyjcdVB1-DQeINvoXnDO7clmWYG2ee70psk7hr2i0lYO4CxXl-yEHU-VhTUJ4bXOAhwukM_RTkrPdDaaF0Y6JydBWAdZTLqcL41LTkYgtGFXGtVPKUTm1iBLUcnDwhN2Cul6uOb70xKqVGWXx_sjyQ76dw4V-8BVtnhVqvx4eJvylzF7gwLu5maAgRXDVDihOeqNQRIT1gZL_z1UZ7WHl3F6QhtxYfhxpjxRmt65S4PeVc_e82JXn3kgCop90_XTN5n7bTXs3_hcGYshA7BnZ-IR8gu13SwHnOz9fvk56YpeBqkkwQRobMuShRmwu0tzdX7arB7zep9uXB_jscoZrHJRMfXlcV9tdmPPIvhEdMWGfYeLEQ04ewyrJUsW6egmvDR6O57cTtdVQKP6bn16RYLuLYpwvsnfGUF4OhMxFTTtKWGllvoa5rZ8OG6J9NAlLSbkzNi1tMdFkby4sfL2YAiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
ملت ایران جفا نخواهد کرد
◾️
دقیقه‌ای پسرت را رها نخواهد کرد
🔹
شعرخوانی حنیف طاهری در مصلای امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/446683" target="_blank">📅 16:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446682">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze2XfkVwL1pfZWfFSfuBaM1mUG-qJ2ZM5NCy5gNx9Z7APyb7ZY2ah9lkOzmXsgjS7aKnS3lMAU9zS2WRAmjVnQuVyni70R3zcO6_LeOTedkSVmJAxvJKrGO_pt102avw0eFjHE5nEzL2Z_Jr3bcPFstdCgk_esgo-Q1yEldZSGWhMfB63E5Ttm1u836EJGEOpnpQuoKbG24JwuexdDt35g4SpkxgCKEAzR-O7-6cMbL1rPGj5Wnb7oVZXlppvcAppW30swDMKauiH_-dD3gZ4DfUo-K9nc2lRLB5lXum-1SGCe1ZHBVgG8TsM69S-Q_JDBMAHkVrwCkApV-duk70cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: پرچمی که قائد شهید برای برافراشته ماندنش مجاهدت کرد بر زمین نخواهد ماند
🔹
ملت بزرگ ایران با قلب‌هایی مالامال از اندوه و اراده‌هایی آکنده از امید، ثابت خواهند کرد پرچمی که قائد شهید برای برافراشته ماندنش مجاهدت کرد بر زمین نخواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/446682" target="_blank">📅 16:16 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
