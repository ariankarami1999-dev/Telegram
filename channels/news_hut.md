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
<img src="https://cdn4.telesco.pe/file/RB7jsSRsErKHaUH4E-YOuKK3iyxmnVoDJal7tEXsd31ndInj26JdZsN5DWeodzvKBtGxD6DhtlgS8hrJvD73NdOjjOLUKrbpTM_7XNfqmF5pTDPAjb4w_K1-hI9hVkJULmpqMaG-2IpysWUr_ayMm75Z9iXmgD5aGb8EYGGxzFCXqAlTDQoMP2jaY-iWdqYPqmQ85RhXJ-CwcpKVuk9pxOaWTVHApNaZuRqRlpGuS-QO0fYJOOTyuANU7zNNY0wOi4q3yznZSP2z-0UaOd5HOf2M0d_7jd-J0C2DbO3evPWQNHBazSG0QwoI9UVO3vqaB3S3IivPRDW2lFZJCLndWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 161K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 22:23:10</div>
<hr>

<div class="tg-post" id="msg-68559">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=T3zXlS3u3MLKh6h7tBPTODIsNAnUDUZkNxvH_eLvHnMaAvi_2WIiw1idNv-XIWTCNh0ISinbjNlkiA3PXur5WsIEwt6qpgCcgtV_NhXjcImW-CnW-WalDVRWL-ZForlqXsUU5VFjE_SIImw4Pn1X9AGtKnDEu9LZDzMXLt7gW3QiMGDQC85_Jw_pYMc37OiRIRSut-RTCpJN0sJR-oU1xmzRcnjoM6P9706fshyM_35M6LD7SzWKRPG_n0II-A2XavsUHohet8MZNzOn42jzd3yqIL9JpylKUaDDdqDYJaDFDYpDhwggp4ocj2RiKuXFmh5xgujxEFPJFn8NTcqjZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=T3zXlS3u3MLKh6h7tBPTODIsNAnUDUZkNxvH_eLvHnMaAvi_2WIiw1idNv-XIWTCNh0ISinbjNlkiA3PXur5WsIEwt6qpgCcgtV_NhXjcImW-CnW-WalDVRWL-ZForlqXsUU5VFjE_SIImw4Pn1X9AGtKnDEu9LZDzMXLt7gW3QiMGDQC85_Jw_pYMc37OiRIRSut-RTCpJN0sJR-oU1xmzRcnjoM6P9706fshyM_35M6LD7SzWKRPG_n0II-A2XavsUHohet8MZNzOn42jzd3yqIL9JpylKUaDDdqDYJaDFDYpDhwggp4ocj2RiKuXFmh5xgujxEFPJFn8NTcqjZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پخش تلویزیونی اسرائیل؛مقامات امنیتی اسرائیل و ایالات متحده:
ایالات متحده در حال آماده‌سازی برای تشدید حملات خود به ایران است.
این هفته، خاورمیانه شاهد تعداد بی‌سابقه‌ای از هواپیماهای تانکر سوخت‌رسان خواهد بود، که این تعداد حتی در مقایسه با آمار ثبت‌شده در جنگ اخیر، غیرمعمول است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/68559" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68558">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
کانال ۱۳ اسرائیل :
دونالد ترامپ، رئیس‌جمهور ایالات متحده، پیامی به کشورهای حاشیه خلیج فارس ارسال کرده است که در آن تأکید شده است: اگر این هفته آتش‌بس برقرار نشود، این کشورها باید خود را برای تشدید تنش‌ها آماده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68558" target="_blank">📅 21:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68557">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
استانداری خوزستان:
دقایقی پیش یکی از مناطق خارج از محدوده  شهر و حاشیه‌ شهرستان آبادان توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت. این حمله تلفات جانی در پی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/68557" target="_blank">📅 21:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68556">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مسی و نتانیاهو
🇮🇱
یا یامال و فلسطین
🇵🇸
؟!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68556" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68554">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHZGDWBfFOp0nbdHKExJN2qlj5qkVW5L4fzYbZOagVj3iIIwLYkPLLmDH1WKUq8AvrOrUrUftU8kpYe9c6daFwAsfPI5N3wjq7xF_0IgsWKuJS5z6vl2EfLLGhMHMllM5W6dTbGMDSPCo58V-VMCQUx5Ui_2szKDJ6HpEo6j3H9DVpN7mOd95i59WNXv48efG7PX6xB1GOtLbTrxDCZm73aYypKNbFZV2v01oMG0sgqOPNyE3lSt76cbTDunD9akA5hOtaXNUn2pOVmMwa-xeKZjZRPO1GPXDExyPfIMNVqj6m95dugMIlLbuPGcgj253l-ZIHdHI24jFMf7EfmIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HakuTlevRBJq0prKzEmkh47d8J_wcDX1qaEt_aZfnhLiZ8RDqtULeZGzeosYZXBZB9piwP0d75Eo4xl2dj0ncHnfu6AKGbXNZy989nkhooL3Iw75eH6SnsD1zq9I2nYNMr5jluBHke8rpXLe4ZY_tTbOpZRgmUo73tWYm4E_FArJ7Bbhg3dmFXepV_X2-habVjV9_-3pCQdPCSbSLVqvfeXwkSFhhd_HAjkIksFtAiq_u4mdUmYnIcpQU_N7Ifza_EYU2P1hVLw7xwY4l68MAOzzvWXiFt2NDmPlIUt50CJhuoRPKxB-2doExCb4EjhJvF-aUSySiRnkq5R7ael9aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/68554" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68553">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
یک پیشنهاد جدید آتش‌بس ده روزه از سوی قطر ارائه شده:
• ایالات متحده حملات را متوقف خواهد کرد.
• ایران دو مسیر دریایی در تنگه هرمز را به مدت 10 روز باز خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68553" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68552">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=o7KsnWtyht46vQguGrQDO-wCDSmMhu8oPbBnznH63plHDAIgGO9Z03dk9d5aAfFSGjbk9RW9I8jVb7bdDjildaN7uh9kImyf84Mpdbk5OtPU2Ruef2wI_dSfU_mUCPJHUjhjgumAI_VZoL85SCe19KlM47gx_NJ3wOU06xPxti3IXsCqCgq61IzOTriuAzCoggw-Lri7OJ94n4B62im0yyD9kr3tKEBT_l0I5ls_u_Cph3zZ8sgQJNELcuIYQGCcyk4uWesa8NN5_kDanG8S_ijhDdSwMFW1CM57EjxOodaZsAhmK5Z9wLMe6_qLeEBQ3dEDZ_N2Bfxl5zoqpCu0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=o7KsnWtyht46vQguGrQDO-wCDSmMhu8oPbBnznH63plHDAIgGO9Z03dk9d5aAfFSGjbk9RW9I8jVb7bdDjildaN7uh9kImyf84Mpdbk5OtPU2Ruef2wI_dSfU_mUCPJHUjhjgumAI_VZoL85SCe19KlM47gx_NJ3wOU06xPxti3IXsCqCgq61IzOTriuAzCoggw-Lri7OJ94n4B62im0yyD9kr3tKEBT_l0I5ls_u_Cph3zZ8sgQJNELcuIYQGCcyk4uWesa8NN5_kDanG8S_ijhDdSwMFW1CM57EjxOodaZsAhmK5Z9wLMe6_qLeEBQ3dEDZ_N2Bfxl5zoqpCu0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
رئیس هلال احمر:
در تشییع میلیونی نه تنها یک فوتی هم نداشتیم بلکه شاهد چندین تولد نوزاد نیز بودیم
👅
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68552" target="_blank">📅 20:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68551">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=fMcJmR-n9nL1AG7Ro8GiM4CASjoXpybmIb7uVkrc0lx3aVNY243Aq78AxZV8yTyTnAhBWFZ1vHk7MSIMydoNsi0yc_0z_39mv6G2_23TyWf1ZnXc8wEwD4mHcBF255v-2T9yjkgrgRl3FDJqXRd0GBaJc6wICGzS6ALjMlTxoZ_mzX1dYAPCxPGzwDxqkWbjZGtPAcaCXS2OEIaZGCJuKNCdgk3Iy5xNUI7m7eafPMZAwUrujTaEBNQvRPTCB5Jjdjd6sckhGl_Orf7zauM3mgAv2G9a8-yVeGuBtJuhUQmPO5hQAbyawvFkJ-oqixXD1Stcj11Ph0S1Qgnfs_v7pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=fMcJmR-n9nL1AG7Ro8GiM4CASjoXpybmIb7uVkrc0lx3aVNY243Aq78AxZV8yTyTnAhBWFZ1vHk7MSIMydoNsi0yc_0z_39mv6G2_23TyWf1ZnXc8wEwD4mHcBF255v-2T9yjkgrgRl3FDJqXRd0GBaJc6wICGzS6ALjMlTxoZ_mzX1dYAPCxPGzwDxqkWbjZGtPAcaCXS2OEIaZGCJuKNCdgk3Iy5xNUI7m7eafPMZAwUrujTaEBNQvRPTCB5Jjdjd6sckhGl_Orf7zauM3mgAv2G9a8-yVeGuBtJuhUQmPO5hQAbyawvFkJ-oqixXD1Stcj11Ph0S1Qgnfs_v7pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو :
آرژانتین امشب قهرمان جام‌جهانی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68551" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i732u5z9bGcueAGlw6d2-Yxh-54mFWH8SKQNafcf3MClOUovxwCP6iHRwVTcmACw1MqcH9H6O4GmhRqMmQhqhvWpwLNKMAhOdLyMcDaUr1LCroRohr_JvsJkRULsvgO_B6_cBaDyseTIZc4ZfdP4R35iyVb2LGl1dqLE8PZzeKza9eLNIzw_d7JPtMZ4rD1OZgOENO3CQsOM0ecqCsB-P4hqbNTzb43UhW1Ath38i5z56RJeko-cYWtil1_VCp05wXCPAtHxFH0o_lEsHjskEsVMFwNWVEY4NdCADt_3xuJP8cBfDQ8S7FwGdSSZOiA87aNVluK4FXTEtzZZp7LyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه امشب نیروگاهی در ایران هدف قرار بگیره، مقصر اون فرماندهای زن‌جنده‌ی سپاهن که امروز برق کویت رو زدن. #hjAly‌</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68550" target="_blank">📅 19:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68549">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
رسانه های عبری:
برآورد‌های امنیتی اسرائیل حاکی است که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68549" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت  @News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68548" target="_blank">📅 19:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oivj52D0ZwgSea1d9bcywcjg0HaKwFj_XpohAblURth0dF8XUqYaJzE0bTV443r-LhfiNV8ZiDOQMGFDImQuz8HrcCIGC9ZNFIXc7kfQoFWSKRkyeQ9RKMAdH0RBfEYkHc0glu3g7pT5mDR-Twem-0MrRLqIWrytB2yl1bNK65Eo0WS9xb-EtBNhftH0B_C8t3N_TW-NI95n7NL1mhCAfKpnFxU1ILeMAx5dX7prPLEPIaBE8Bz6FcrLfHEBbN49bxXj9FiyUPUR1ICnsK36qiiYF6RLzEtqaz7ybiKgkDbcmiAk9_YQduVdI13eT2jSzv7gNyD8Wb3IhT0C1rxoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فینال جام‌جهانی ۲۰۲۶ فوتبال
🇦🇷
آرژانتین
🆚
اسپانیا
🇪🇸
امشب ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68547" target="_blank">📅 19:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=hC-4wRdvmNOFAZlog6rQ5M5HL7DUlVjXNSPUfcIN86ZlN4MZBCo5Q_jNHjFhrIaowhrxIfiOl_U8uB8mwE-XTU-8bMwPzXvNVqXuJoeG_LNXQzlGEAFFqkBlF4cY2RNm66vMIFAiqZ5tuZE-t2S2QAbGi52iPCG79HwGx1XDuDYdo0xtFBPCGLTlhJeTjBphttxguzI-R5DR8imXmlg0XtSmUrixIhQ6TkbChXUh3gSSwuW_DjY-IV0sqlrr74erHv8YEKwVb96rrmjnSP1MrnPgX1MrVAWbp2T6CbScCA6dhObrpbHJXPHFAKiSr6W5oEcmNS8oXP7lHBTyI2gdgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=hC-4wRdvmNOFAZlog6rQ5M5HL7DUlVjXNSPUfcIN86ZlN4MZBCo5Q_jNHjFhrIaowhrxIfiOl_U8uB8mwE-XTU-8bMwPzXvNVqXuJoeG_LNXQzlGEAFFqkBlF4cY2RNm66vMIFAiqZ5tuZE-t2S2QAbGi52iPCG79HwGx1XDuDYdo0xtFBPCGLTlhJeTjBphttxguzI-R5DR8imXmlg0XtSmUrixIhQ6TkbChXUh3gSSwuW_DjY-IV0sqlrr74erHv8YEKwVb96rrmjnSP1MrnPgX1MrVAWbp2T6CbScCA6dhObrpbHJXPHFAKiSr6W5oEcmNS8oXP7lHBTyI2gdgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68546" target="_blank">📅 18:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68545">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
«ما اعلام کرده‌ایم که اگر ایران جرات کند به اسرائیل حمله موشکی کند، ما با یک حمله قدرتمند، بدون هیچ قید و شرطی، پاسخ خواهیم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68545" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68544">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68544" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68543">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkkThs2KygTF6VDJx5LcAyx28IQ9Qh33yWHn4F7vBrSH_E5Bglgo_ai4hMaL3a33n3MOMBc-iYvqpj0lK74-uMv5wZ3XjOMuXYW3mVIfFYrQ5zNNm_1UVg-8vUXNIPyOYbXF55JFkhZMRTgEyU7QaFSXAaLwpdbdxtlLKqeQbUHK-RHs0QnLiyzBIEFcByZDIZQQ0Hxn9Q2U2cq5jrBXdiADypfZ9iv3kNDHLLdaD6FgRLxyqKOnzSlouzm0pOncaWdi017SBFmrA44vOshFJkn9yvWl-l4NAVL0eO8x8eAqWw5Mvl5G-duqEOO1XIxuSgXZq5X1czBrhPTV-ExcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68543" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68542">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=lbmuT-px4akxIZEo_Tx8mhOaxQivak3DDS6gWNx4dRnFwbR1ZJEy0dJJZtR89c7BVJTUJHv-x8mv7KERhf17hnh_cvAyijjFtDXPnirZx4MLgVo0uj3LvatrNXvx9zdF4QZLWj2j0ACx5NWQQcQQLhDvS3nSWMfXQ8P85u3irYFI57wOhyx97gEMZKXNzeH2eTVuVx8OaA0i67yW5F7dAgBwVjNlzNPtxxDApqZwJQUXAuimnVj7GaI_Qo1hFLgbc0ZUPQdXcGhsl8UFaR7JnpU300BS1TRhJR6Hr1MYoQ0admJ5xAaOmDc6gEagNi2Kg0ah9T8CbnragFd0pLnfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=lbmuT-px4akxIZEo_Tx8mhOaxQivak3DDS6gWNx4dRnFwbR1ZJEy0dJJZtR89c7BVJTUJHv-x8mv7KERhf17hnh_cvAyijjFtDXPnirZx4MLgVo0uj3LvatrNXvx9zdF4QZLWj2j0ACx5NWQQcQQLhDvS3nSWMfXQ8P85u3irYFI57wOhyx97gEMZKXNzeH2eTVuVx8OaA0i67yW5F7dAgBwVjNlzNPtxxDApqZwJQUXAuimnVj7GaI_Qo1hFLgbc0ZUPQdXcGhsl8UFaR7JnpU300BS1TRhJR6Hr1MYoQ0admJ5xAaOmDc6gEagNi2Kg0ah9T8CbnragFd0pLnfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در دزفول
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68542" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68541">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=pTrt05iZT3B0WElP7_U9drtO0qDarLfl8Zf-GeQCxXO_wCSak3jgc1BenYM6ug9tFI6MJIV3qCzUZSPdUB7mtoQjhZBPnr_K7qrkuOjbrhkozUmnp9MBHlIGcfzIBtpkPd2IHFl6bEVIetxT6ARXT4O3FgPGtB69vNoSjhW9MWFjwOREM7Am2vG2C7sXTKB86uZEZ9xYnynw9T8bLJW1fN4T7XAIF-P9IutFXiz-k5uP_cC-lafyUQHbfv13EgvFiIsRa9tdhKAIVo5Vtrq4UaBGPG0LTNkmLorHF3AfExEpxslpZ9lA6AqHGd9LlzClotutc5ZrJRQ5i68ZHiEBQjD3znV-MQIfbt2XnvG8Oon7cL6KoMi9yNTxiJRfDuqrCtxg1t4UU08m3rqBnuSdccI5X2KwcCJY7BKyUFER-23zX46Vovb7IiBGkkXgQ_hzbl-70PHaDgXdudqN0jXWpieLUlb29dfeSAHanoPAxw6tVp3yMDrVqKVnGQ-hBTerhYIoNqLsi_KMdt57Wb_ecIGP01m8NSAu_ZJUsPwZcKlQ9Al6S9iqJpKz9GbvdkjGWa2YS1rkn0oMdFgI6yRWz1y1VdFuMx_Xhv_FlwnG2HDKX9nrCq__BVIqA3cKj1dbb-eJOcZiRag4fDLNZblhEbTBG4BLKDfe99_rBZjdoes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=pTrt05iZT3B0WElP7_U9drtO0qDarLfl8Zf-GeQCxXO_wCSak3jgc1BenYM6ug9tFI6MJIV3qCzUZSPdUB7mtoQjhZBPnr_K7qrkuOjbrhkozUmnp9MBHlIGcfzIBtpkPd2IHFl6bEVIetxT6ARXT4O3FgPGtB69vNoSjhW9MWFjwOREM7Am2vG2C7sXTKB86uZEZ9xYnynw9T8bLJW1fN4T7XAIF-P9IutFXiz-k5uP_cC-lafyUQHbfv13EgvFiIsRa9tdhKAIVo5Vtrq4UaBGPG0LTNkmLorHF3AfExEpxslpZ9lA6AqHGd9LlzClotutc5ZrJRQ5i68ZHiEBQjD3znV-MQIfbt2XnvG8Oon7cL6KoMi9yNTxiJRfDuqrCtxg1t4UU08m3rqBnuSdccI5X2KwcCJY7BKyUFER-23zX46Vovb7IiBGkkXgQ_hzbl-70PHaDgXdudqN0jXWpieLUlb29dfeSAHanoPAxw6tVp3yMDrVqKVnGQ-hBTerhYIoNqLsi_KMdt57Wb_ecIGP01m8NSAu_ZJUsPwZcKlQ9Al6S9iqJpKz9GbvdkjGWa2YS1rkn0oMdFgI6yRWz1y1VdFuMx_Xhv_FlwnG2HDKX9nrCq__BVIqA3cKj1dbb-eJOcZiRag4fDLNZblhEbTBG4BLKDfe99_rBZjdoes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صحبت‌های وایرال شده سرباز آمریکایی خطاب به مردم ایران :
اگه حمله زمینی شد بهتره فاصله بگیرید از نیروهای آمریکایی
نه اینکه بیان شمارو اذیت کنن، چون ارتش آمریکا خیلی مواظبه از سپاه که بعضیاشون لباس نظامی نمیپوشن
سپاه میخواد با اینکار به نظر برسه که مردم ایران علیه ارتش آمریکا هستن
سپاه اصلا توانایی نداره علیه ارتش آمریکا بجنگه
پس اینا می‌خوان پناه بشن بین مردم و حمله کنن چون اصلا نمیتونن رودر رو پیروز بشن
خداوند ارتش ایالات متحده و مردم ایران را حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68541" target="_blank">📅 18:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68540">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029372426.mp4?token=DZwtiiPc3y6oYiaEQKcEemxBeTtr3uvtEoFnJ5ommAybJ52tT2ALku7r8KTSkFII-xeW0H3LbdlabaKRHAPaixckwmo2UyUZfFuQGyaLTGgWmR5HEZ-RYihgPVmArPDIQPm9hwbr251eoGjX_Zo8caEIFuH-JgXgamBCbDO6qbNP9ZNdDnXmdNoiha18zT4bulDzguVRJPcxSoXSQaT5L8QWdYqztP7Cn6qxez5SO66GnicSaUvv55ZZa8JZ7TNR3ioFH3R4tOpybS6h7ot0JjlBM1H3VeoMxMpqLjm4Qw4x4VAYbM0_6k1tng3M0Oe2aOAZ4r1ZORCbFE5bTSrWnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029372426.mp4?token=DZwtiiPc3y6oYiaEQKcEemxBeTtr3uvtEoFnJ5ommAybJ52tT2ALku7r8KTSkFII-xeW0H3LbdlabaKRHAPaixckwmo2UyUZfFuQGyaLTGgWmR5HEZ-RYihgPVmArPDIQPm9hwbr251eoGjX_Zo8caEIFuH-JgXgamBCbDO6qbNP9ZNdDnXmdNoiha18zT4bulDzguVRJPcxSoXSQaT5L8QWdYqztP7Cn6qxez5SO66GnicSaUvv55ZZa8JZ7TNR3ioFH3R4tOpybS6h7ot0JjlBM1H3VeoMxMpqLjm4Qw4x4VAYbM0_6k1tng3M0Oe2aOAZ4r1ZORCbFE5bTSrWnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این مجری که اخیرا زیاد در صداوسیما حضور داره گویا اهل کشمیر هندوستان هست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68540" target="_blank">📅 17:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68539">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W60arxYoPItAbVRdP2vq5bwlGlFveyBxUJGpwZFX_fncLZwSSGDHdMNfjMdr1gMPQGObxT_RMPS7PfW89wYCTSU_F6xgtULG9BVsEskDqljGIl881PT5it9WiF6I_9-84F6ACzDHIbZd3gursAw09wkJjAHNwVKY6PIQL5-faoDx8eZGZPXVX32pB-jw-YDMkHC_H6KQAL3EZTDJBIWKwRzCDzSxsHzOwHXUMI5KS0uoU3htQjQvuVZphdxBXXQC6AGQEub2-RH_cHP2DNbS6FWnoCEUAqFMSJEl4z-JMFJtuakBCx2IT09ZkXymocVzhHSjsPwnvfjAJPwUThwtPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان انرژی اتمی جمهوری اسلامی:جت های آمریکا صبح امروز با شلیک چند موشک به سایت نیروگاه هسته ای درحال ساخت دارخوین در خوزستان حمله کردند.
ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68539" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68538">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=tE5O5-k9QevOW1ek2vfUlK5BzGit7028Zkvt_xoy5G7cft4DNTdn-DbPhnkNbcmwF8jmCwS44cBB_DhM7EWTCjt9UeA1zKu70UnvJSTkBXe5m4EcLQcZ2gLStnKMLb-M6Jd3ZWQ_UovSwH5rC21NFiF5Br6eAxUkwaNx-FNoGxMTnCs6MWNeai0EVmOVfB5PaCfUSATnDsex9U8cWZA1acz6WGeVXzmQWcOHQLHILUX6ApYzDqodI_cJELd0DgLzpIiP8yHv8ksBOHx8fkuOFfDNcx8XnA6GVm4d_NvKNYGfehDEWLHuXFdMl-O_0WYtE1a4aw84PGeFWisx-2Cei7QVHBsRGl0YxVprP4nBX0WuXj0atAM3BF30ADbRqDYEEZXw2ZeyOd8XbpQrtsJTHyR3C5ahXvEiSiFnvK8WJwSd0wwaNxeqS91KHQNdJnmjv2NSdASOhIx6ZhuIWWV7zF8jaLvL7JpQFLQIHSu_7Z4QexBokNBrZJER2WurzBpp6GVdyii6ApmA3_P5L_LfWB9j4lCZU4Onf8lTiu_OtrF2VLH7n0vOCarL4TKrpyA9TQBTXMf8bKVwL6ipV-46rED_n19Jc_R1WmNxE_Do4my8CXKuO8zOt4sAcb2Lj735JVeIaGdDpylyXjQbXE0acJy0kb7hxTEUPLxmiVGnfYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=tE5O5-k9QevOW1ek2vfUlK5BzGit7028Zkvt_xoy5G7cft4DNTdn-DbPhnkNbcmwF8jmCwS44cBB_DhM7EWTCjt9UeA1zKu70UnvJSTkBXe5m4EcLQcZ2gLStnKMLb-M6Jd3ZWQ_UovSwH5rC21NFiF5Br6eAxUkwaNx-FNoGxMTnCs6MWNeai0EVmOVfB5PaCfUSATnDsex9U8cWZA1acz6WGeVXzmQWcOHQLHILUX6ApYzDqodI_cJELd0DgLzpIiP8yHv8ksBOHx8fkuOFfDNcx8XnA6GVm4d_NvKNYGfehDEWLHuXFdMl-O_0WYtE1a4aw84PGeFWisx-2Cei7QVHBsRGl0YxVprP4nBX0WuXj0atAM3BF30ADbRqDYEEZXw2ZeyOd8XbpQrtsJTHyR3C5ahXvEiSiFnvK8WJwSd0wwaNxeqS91KHQNdJnmjv2NSdASOhIx6ZhuIWWV7zF8jaLvL7JpQFLQIHSu_7Z4QexBokNBrZJER2WurzBpp6GVdyii6ApmA3_P5L_LfWB9j4lCZU4Onf8lTiu_OtrF2VLH7n0vOCarL4TKrpyA9TQBTXMf8bKVwL6ipV-46rED_n19Jc_R1WmNxE_Do4my8CXKuO8zOt4sAcb2Lj735JVeIaGdDpylyXjQbXE0acJy0kb7hxTEUPLxmiVGnfYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش امیر رولکس به حواشی ساعتش در جام‌جهانی:
به جا اینکه بگم فوتبال با ما سر ناسازگاری داره از کلمه خدا«داره مارو میکنه» استفاده کردم.
چهل چهلو پنج ساله ساعتمو دست راستم میبندم.
اگه یه سرمربی ساعت می بنده و لباس خوب می پوشه که اشکالی نداره.
اگر من زنجیر طلا مینداختم  و یقه پیراهنم رو باز میزاشتم آدم خوبی بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68538" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68537">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSsBCVPRuJapN6HZm4YSZJvmqekUsViBKdZvVhkSGHY97EvFGBOSD5RSEpdDOVix89CCZPn_hL89DT6HMNRAiMU1U6EQPKnNd53V5bqdVl2D8ZXJ8FobHPGqgR8yYxN21bC7V2xexsU2P9hGADosdcKHfK76rShX7ZpmlxUY_glHvqY1K_2BT69q-4VK4tddWHNEivtpa0IwxzqkWAWzovRDsFVAgsCm2FxC0Dq59_nt7uWbMRlYNZfdf0fuN7efaH-uMUqfaBL38h5DyRCnrx5C41qoOV_spwsbhXayVMSeZ_WjNM97JaJgCKvAzc2zBuawmCE2WfUjwNscDWT0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پرزیدنت ترامپ:
جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این همان کاری بود که لیندزی می‌خواست انجام دهد و قرار بود محقق شود. مهم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68537" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68536">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uykzaa_AqJ5BXAu2mC3fT4lp9DVQXDUz6Gv6mwqTPRvxsuK4XqEXRnAPVsjtyfbM_Ut3qRyTGYxYWiapa1IpIED6gMemuws4qKTqo8hzgO-KCpVcLXu5UChh2ykeO4atWH9Pv6OjepFs7-_B_Dj4_-5Z1G15QaTbNv6_9RcSBSFKnSqbeZJ8vEpSYCv2ChvvgBqr9uAKv1bvc9QJmV0kSs4zLgWPUIzyh4-t_VcNjz0HsuKPwIawg0Y7qxG_W69kx1eL4hasDpmDYif3c6Ug-v2IWf3BWRi_3Rey3ArWl_Q_du7QoHSVjjErwsrzcAg0JolEVHtRC16hLdvqRR6klw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛ این 12 نفر از متهمای پرونده میدان علیخانی هستن. +پرونده میدان علیخانی مربوط به  اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68536" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68535">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
عراقچی:
بمباران بیت از طریق حفره امنیتی صورت گرفته و این حفره امنیتی همچنان وجود دارد
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68535" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3548648f57.mp4?token=EngxXc3kUSX1LTEMlUTksaOcYtwSgR2808WXiCIDYXwdZggdLPH5KFdKgpDDW8OCFR01I6ExCEPvUewQtRdzv296vbgKVJMeWDzm5nU7zIuefNVMq6kMNXV9mpPnui9MWX8u0tiUKe1lvYb5LLowGFvoZDauTxleldf8LOUkO6UWAeftS9a8qpWm-5EEyRp5lMPAaddkoeQqx-VZawR7BNHkL9GgL6v1JIfwgH93PXSJwq5IIoirC4HYsg3NOt-G6XVicKnsWtbfK6c16yOWQPCnaXQVc9f7qHbWqs0ss6btwmgzgCQlasGfwUzrE67P8qchS-VUmo2qxZSNSkvMfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3548648f57.mp4?token=EngxXc3kUSX1LTEMlUTksaOcYtwSgR2808WXiCIDYXwdZggdLPH5KFdKgpDDW8OCFR01I6ExCEPvUewQtRdzv296vbgKVJMeWDzm5nU7zIuefNVMq6kMNXV9mpPnui9MWX8u0tiUKe1lvYb5LLowGFvoZDauTxleldf8LOUkO6UWAeftS9a8qpWm-5EEyRp5lMPAaddkoeQqx-VZawR7BNHkL9GgL6v1JIfwgH93PXSJwq5IIoirC4HYsg3NOt-G6XVicKnsWtbfK6c16yOWQPCnaXQVc9f7qHbWqs0ss6btwmgzgCQlasGfwUzrE67P8qchS-VUmo2qxZSNSkvMfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وضعیت ایستگاه مترو در کیف بعد از حملات سنگین روسیه به پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68533" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68532">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68532" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68531">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exzxR_1SF-itmE77JipijOZ4Ri-8puENs3_sEyaxBXWcgIXH1AkyWWD9vPVo2Fl4NyUcRK3dkwXLQTsyAP0yzjXQn2frRXUT4TzrMqXtlMgq1Na8x6043RyDWa5tSWlQbFmXFFCaW2bQD-HNea1rvRJ4hckl4y_2FExwZ0pMWWjFobCdowvpQRkZD3pV3zLs1m4QmN9hhmOlfhlQ6hf3oyGarP8HVCJzO4Ucvb7aSVlj_Gp7P4RC6MRkC-MKG7NBbtbLfxq2kW9x1b1M9sdWxO_SWVpclNqS7ChMFQ0_5eKTmfNEtE6RqIPQaXZAm8kZOFamycaN1jMLeOde4WPR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68531" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68530">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326d421018.mp4?token=e4LO0EsXbEeT-tygIxNGYDojeLUCI6pSg5QQKYA0vy_6_MidAjlyuq94Lu6CfdJjjn-i7w4yE-UuEyjOd12VmJNN_OHcAEU_MDvlQDSuQaEQxsHHxFkSxOeoBxlegccS2S8DB-jtcs-CDh2YCCgJnXXy7KokLndO1kgwdJFke0xzJXIV6suL85WMbhjNYD-YEkSy80Siw9XQpLvSTG6SRWEAU636qxXKNZ-2n8mDwW8NQPP93RLawXKjOlhr9VnviwCfjWlHYqlZQyX2F_UJm84sRr-w3CgyCQEdHU0DMFrkyjsizRTv8bzjZpzeEaUQA_IfDYHjAkwP3KsoJW5dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326d421018.mp4?token=e4LO0EsXbEeT-tygIxNGYDojeLUCI6pSg5QQKYA0vy_6_MidAjlyuq94Lu6CfdJjjn-i7w4yE-UuEyjOd12VmJNN_OHcAEU_MDvlQDSuQaEQxsHHxFkSxOeoBxlegccS2S8DB-jtcs-CDh2YCCgJnXXy7KokLndO1kgwdJFke0xzJXIV6suL85WMbhjNYD-YEkSy80Siw9XQpLvSTG6SRWEAU636qxXKNZ-2n8mDwW8NQPP93RLawXKjOlhr9VnviwCfjWlHYqlZQyX2F_UJm84sRr-w3CgyCQEdHU0DMFrkyjsizRTv8bzjZpzeEaUQA_IfDYHjAkwP3KsoJW5dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای امنیتی سوریه یک محموله تسلیحاتی دیگر ج.ا به حزب‌الله را توقیف کردند، این یک کامیون خیار بود که زیر آن ده‌ها موشک کورنت ضد تانک قرار داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68530" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68529">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
ملی‌گرایی از نگاه خمینی، بنیان‌گذار انقلاب اسلامی:</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68529" target="_blank">📅 14:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68528">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=SVrIsRSDiLCtB94da0rwcjajTvR9uQzqfMKZ_HvQ-OnJX__sHiM5rt5oaaHIzLPdicA_POVhAXR5sl3YIOOnhaTjWZZzNaNkGJO1RUN6FZ3iM9G49CgdhWO7YD5EENqBWxkDSwDRVH2a4kEc2hughY_Wzu9f_xCW8dny9QEndENHVrOLUOP2o-Mqh3nImp2gDhfGRS85IVAFJt08VPTFqxN8KoMG8ubA56S2WofE-4ntfv3ku54gXxLGc_ZVVjBkwx2tmL21NaGP7Z281NNTI7Z1gsAFRuAso1rHSHzurqtaY4N__Oy4JZtDUVPUszeBnt46cEui3QVGyNwUKGe_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=SVrIsRSDiLCtB94da0rwcjajTvR9uQzqfMKZ_HvQ-OnJX__sHiM5rt5oaaHIzLPdicA_POVhAXR5sl3YIOOnhaTjWZZzNaNkGJO1RUN6FZ3iM9G49CgdhWO7YD5EENqBWxkDSwDRVH2a4kEc2hughY_Wzu9f_xCW8dny9QEndENHVrOLUOP2o-Mqh3nImp2gDhfGRS85IVAFJt08VPTFqxN8KoMG8ubA56S2WofE-4ntfv3ku54gXxLGc_ZVVjBkwx2tmL21NaGP7Z281NNTI7Z1gsAFRuAso1rHSHzurqtaY4N__Oy4JZtDUVPUszeBnt46cEui3QVGyNwUKGe_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آتش‌بس با نظر آقا مجتبی بود؟
🎙
پاسخ
عراقچی:
این چایی برا خوردنه یا دکور صحنس؟
☕
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68528" target="_blank">📅 13:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68527">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران:
ساعاتی قبل، دو کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و دو کشتی دیگر از ادامه مسیر ناایمن منصرف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68527" target="_blank">📅 13:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68526">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=NnZNY146_4UQIX5sC7hnbSmomDrnKNUZWCgVa7ulxWrl4o34WSy1weGLPLosmMLCZWrQbcRpQIp72AjPX6XqSVqDIs7KHZj4EiEFJExY7uLs-_zSC2JDQgUSJIHkoKIRf5EIcfXBLoLCFzrEtEghiUKJ60vDDV7LOlr7vkusnXVxuxC9DnQt7nOVzYMfRH1AfWLVTweDsrOPRDn5uUMsOuffTXdFPeAD-3DA1Eo9qT6luMu-v776ledK3SQU_eQ6yM7wwlXIny5nZuBY7Zs4bwSOLDuld5dXPoFGJlTijsAoRpinRoAHRsD7OFr1l3FTQdjC9iiZG7uvMpvJXM4OpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=NnZNY146_4UQIX5sC7hnbSmomDrnKNUZWCgVa7ulxWrl4o34WSy1weGLPLosmMLCZWrQbcRpQIp72AjPX6XqSVqDIs7KHZj4EiEFJExY7uLs-_zSC2JDQgUSJIHkoKIRf5EIcfXBLoLCFzrEtEghiUKJ60vDDV7LOlr7vkusnXVxuxC9DnQt7nOVzYMfRH1AfWLVTweDsrOPRDn5uUMsOuffTXdFPeAD-3DA1Eo9qT6luMu-v776ledK3SQU_eQ6yM7wwlXIny5nZuBY7Zs4bwSOLDuld5dXPoFGJlTijsAoRpinRoAHRsD7OFr1l3FTQdjC9iiZG7uvMpvJXM4OpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویری از انهدام یک پهپاد نظامی مدل MQ9 متعلق به ارتش آمریکا در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68526" target="_blank">📅 13:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68525">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpmb9TlA_hwLq4ffdEU5z3BU9hyjvpfieh_fxk1mGiRXjL4XQCgXpu5le9xMS2oD40I4hT3ZXeEqJ4auEvmC7-z5fItpZ3L3Fm9wz8syeJBeOLUbkFKMqQgEVkXPwE9ShgudiU48Q34ChPH74weJhZd_EFBebsBLRBEhhAwTgfCkiBfWjni5Ggr_5fjrQWW9jQ5w3rYicaObLNxv7uREiE01vaNRqhAYMPvnosC3GiYIpSR0JBnB0u6W8jFW1avstuLHLI8d7tXD9V7TjcVmvLLo-gZbcuPcNDdCQ93QZlJjQZekY8sEgUWxTGgl9AeC6IFdTwzOmwCZQBLQo1mTLH_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpmb9TlA_hwLq4ffdEU5z3BU9hyjvpfieh_fxk1mGiRXjL4XQCgXpu5le9xMS2oD40I4hT3ZXeEqJ4auEvmC7-z5fItpZ3L3Fm9wz8syeJBeOLUbkFKMqQgEVkXPwE9ShgudiU48Q34ChPH74weJhZd_EFBebsBLRBEhhAwTgfCkiBfWjni5Ggr_5fjrQWW9jQ5w3rYicaObLNxv7uREiE01vaNRqhAYMPvnosC3GiYIpSR0JBnB0u6W8jFW1avstuLHLI8d7tXD9V7TjcVmvLLo-gZbcuPcNDdCQ93QZlJjQZekY8sEgUWxTGgl9AeC6IFdTwzOmwCZQBLQo1mTLH_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
مصاحبه عراقچی با جواد موگویی؛
جواد موگویی: دست فرمان شما دوباره باعث جنگ شد.
عراقچی: دست فرمان من نبود.
عراقچی:اگه ده روز زودتر آتش‌بس رو انجام میدادیم لاریجانی رو داشتیم خطیب رو داشتیم عسلویه رو داشتیم فولاد مبارکه رو داشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68525" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68524">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=Rb4CJ_GmckZMg9uFnTfFm7vZdokB4z5MNpcYPyX-cP2OUVMEE70rreqlSrNS0N6njHjLDApskkNWvCt9IVpd3G-gPYBP7JlwBfNPEmQOoDx7sZ1sYUyN7om-TyFdgvqJygHjwVzghirUOta2Sfs0JhW_QYzsm_exoPxEgRePiHk0ri-PcCZUMIPCEkHvTTHMDPMpzgl5_voxSA0POG7Ialfzu_yBSmgMFudL7zEVvIQisPkGEnkw9zzyvgSI6TGzPomvC7eehvFAvcSe9QS9Aap9y-t4zjUX6JNdPT97bQvHDdPiunj2xBMe9ESVdKECmydI0IbSLFzyU-Dt6rpD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=Rb4CJ_GmckZMg9uFnTfFm7vZdokB4z5MNpcYPyX-cP2OUVMEE70rreqlSrNS0N6njHjLDApskkNWvCt9IVpd3G-gPYBP7JlwBfNPEmQOoDx7sZ1sYUyN7om-TyFdgvqJygHjwVzghirUOta2Sfs0JhW_QYzsm_exoPxEgRePiHk0ri-PcCZUMIPCEkHvTTHMDPMpzgl5_voxSA0POG7Ialfzu_yBSmgMFudL7zEVvIQisPkGEnkw9zzyvgSI6TGzPomvC7eehvFAvcSe9QS9Aap9y-t4zjUX6JNdPT97bQvHDdPiunj2xBMe9ESVdKECmydI0IbSLFzyU-Dt6rpD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68524" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68523">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇷
فعال شدن آژیر خطر در بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68523" target="_blank">📅 11:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68522">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3dTHwDJE1eHwsWaNvZuLeL9X32J2h1URQGoIf3vUMIl0bi_ITo_UmdIxReUMIIf5BY4sRab3aSzUkSrgs4JlNR6F5QtemOI3OOfaz9GmirNeouBMsF2_tpMBuVPijX_y6oYpf20FuKYD2al0nsimhbFx6Ys8FwqKTcMZfSddX8pH3DtnxAjK5IlzldvAFUHDA86hMkfTEQg6mLhZBnXXb0M4Gv3dLUgkK0ThpmU2DVwJoIIYhOi-w2iRn9Jc_eiC5sZ3PDgSxh00uUKgUhP1j0X8nNl0IUAh6YDi6EjMlLnyMHyvb-tBvcYJTac_xKcxqzOFbWG-e88bnHYIiFVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛
این 12 نفر از متهمای
پرونده میدان علیخانی
هستن.
+پرونده میدان علیخانی مربوط به
اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی شد؛ چهار نفر از نیروهای بسیج و فراجا تو اون درگیری‌ها کشته شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68522" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68521">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
در هشتمین شب متوالی حملات ایالات متحده، نیروهای CENTCOM با موفقیت به تأسیسات نظارت ساحلی و پدافند هوایی نظامی در ایران، قابلیت‌های دریایی و انبارهای موشک و پهپاد حمله کردند تا به تضعیف قابلیت‌های نظامی در ایران ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68521" target="_blank">📅 10:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68520">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
جدیدا تو جشن های تعیین جنسیت دیگه خبری از ترکوندن بادکنک نیست
الان پدر بچه رو میکنن تو منجنیق پرتش میکنن تو بادکنک و آب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68520" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68519">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=F4jKt383PcCm37SyCgjCwgjMIGAZMTSLJRNPOYBaDwlxTfIv-XxfMi9zRD0hT47aIGWdWcHX2T-6xHAsEYfCQ1mK96MtB85m-hw8DyfsxPiYEzGqhxMUKsFH60M0xmcXIup2TztC9ZUfs5UA_WkzkXARIb7MAX_BhTYsr0bLVRbFBbGDRK9xHq8jc_ggac-31JJFw1DBGkv3bwRabhEw9fJOk5cAs4Gw4xpopz1FjQoEK-zfI3_AnzsBBjlBnXQPlep38fK9h_QxkdEEprLYZe9AAuElRLSr2tir-P8mP1LmV_MSmaAEvw0L0uQ_o688NqgT3gXrOwIrIeD5KsYQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=F4jKt383PcCm37SyCgjCwgjMIGAZMTSLJRNPOYBaDwlxTfIv-XxfMi9zRD0hT47aIGWdWcHX2T-6xHAsEYfCQ1mK96MtB85m-hw8DyfsxPiYEzGqhxMUKsFH60M0xmcXIup2TztC9ZUfs5UA_WkzkXARIb7MAX_BhTYsr0bLVRbFBbGDRK9xHq8jc_ggac-31JJFw1DBGkv3bwRabhEw9fJOk5cAs4Gw4xpopz1FjQoEK-zfI3_AnzsBBjlBnXQPlep38fK9h_QxkdEEprLYZe9AAuElRLSr2tir-P8mP1LmV_MSmaAEvw0L0uQ_o688NqgT3gXrOwIrIeD5KsYQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇱🇧
پس از ترور خامنه‌ای، یک گروه از حزب‌الله تلاش کرد تا پسر نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به نام یایر نتانیاهو، را در خانه‌اش در میامی ترور کند.
⏺
سازمان امنیت اسرائیل، شین‌بت، این توطئه را در آخرین لحظه خنثی کرد، زمانی که این گروه از حزب‌الله به طبقه زیر آپارتمان او رسیده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68519" target="_blank">📅 09:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68518">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68518" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68517">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=iTvL29JICXu8WT3aJCTrxd_u1ss5OLCrU7tdYIHCMjYXIuWeqJtVKnaKVbOKWFWwcC0obRQ8dmVXX248NsGEMFPNQYuKBkwKotwvxl5vhSJY7a_GBOz7YaFB7Ix2SswCI_s8qXN40nah7DV5ORFTJBYPRzUirFabtEvtRX2gdVlyX_FYIrUCcxQfaZMaqSaa1WIcFpm9qzYl5jVLWGgxBpk31xPSOEleQhmwf_h5_nAefA5xnjJUPo7VZck3zCEE3srSk2CtMx9FdjDVcg-RuWdE1XJSxpr_n1MSM9h85MO9i5YOZfuokpNHgAIDF2EOANLjZLbjax--0RYF3lHuYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=iTvL29JICXu8WT3aJCTrxd_u1ss5OLCrU7tdYIHCMjYXIuWeqJtVKnaKVbOKWFWwcC0obRQ8dmVXX248NsGEMFPNQYuKBkwKotwvxl5vhSJY7a_GBOz7YaFB7Ix2SswCI_s8qXN40nah7DV5ORFTJBYPRzUirFabtEvtRX2gdVlyX_FYIrUCcxQfaZMaqSaa1WIcFpm9qzYl5jVLWGgxBpk31xPSOEleQhmwf_h5_nAefA5xnjJUPo7VZck3zCEE3srSk2CtMx9FdjDVcg-RuWdE1XJSxpr_n1MSM9h85MO9i5YOZfuokpNHgAIDF2EOANLjZLbjax--0RYF3lHuYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68517" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68515">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwJ7bMx_q8dEs_eOQoZCubZGiPMDqDPLxHQRLhceRdX--OBjyzmHNTy-GhScl0Epg_KM0ozm1F86VXLcLtv9-n-LtjRnS5xa05xZeP8U0wmcMGljo5Q6JkqCKiYDVncgC_orL2I4EaEoHa4JNk-dghdXHI0WMs2lXMXvK5xcUV87qp0PihCGdrFkFVkYuSD3Tp8KFft_R2OqKCtq5r7aQXdsHCdbueqDfy4FVWW-5TPJZaOvjCCqnu5359h030KyNWChePhTVvWboSxGS4YKSokzO4y30FuIGvK-smkiHzBQTH9391Au5yT_b7j2sx1jdklVqiXp6uQd56qr_8f-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlM56sZkxIWxPk_6uyfBfoZ5-nhnDz-MBPANYYCdbZEmhfuZR_kLHhuYmtJPQRy7qcmZaCU58yCofKRyKksiCdVRTRGksNOwySJ_SspoPOwWtMdrL-8hJPnQYSNJpdkpMLrXPLnVYUUT53D4UCHSQOzN_pTHR2ZfHWqJbpAoag6We-JRO2Oc291hAW5mISnR1tCgAgLk31dO6EfEEpjJMRdcQG3CawXMZIn4-oNEVpejRTlzghqAtWnIxmA2mSczFCR3tjEv16_8btzpvK-0RjL-2-4eO3Kj9z_oikp32P6Qbd8c_J7LifjPMnZ3c_vNaFl3qowVWgIbnjcEhFbLhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
حملات موشکی روسیه به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68515" target="_blank">📅 03:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68514">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🏆
رده‌بندی جام‌جهانی فوتبال|انگلیس برنده جدال بازندگان در یک رالی تماشایی گلزنی؛ دشان و تیمش در روز رکوردشکنی امباپه و اولیسه با مقام چهارم با جام ۲۶‌ام وداع کردند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
😃
-
😀
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68514" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68513">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
تسنیم:
حملات نظامی دشمن آمریکایی به حوالی حاجی آباد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68513" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68512">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68512" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68511">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
دو انفجار در بندر‌لنگه
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68511" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68510">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
صدای جنگنده در آسمان کیش
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68510" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68509">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=G9bRB2iZNmh3r3zYM3P7AlkgldaRm0Ez0kEwTcThaSr5T1pd496mL599sY-Ju4klRKtMgwkTmEYNzfJArD6Qcuau8Gz04VQ8BQww8r9a3DZcBonX2UCD9KsvBX6_cLByvrgDzDrmnFCSKF0o-cr7-_vRT1iL_GGC-XDS_iTiJRTQzbw4N1JLGwyrcjMEtVB9pGb0cfi9DOhYI_1ag9jMM3YyZi2S_6XRGVYv2eat6s3i198NP70lz6FWk28zEMhnn5i16M7dSmpVlNdVnfU_ejV8WjZCiK2HLsZwu_PaGW4B8S8uTxw79VX4XeYieOfi0WClo3gt0tMjoLseMRbhzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=G9bRB2iZNmh3r3zYM3P7AlkgldaRm0Ez0kEwTcThaSr5T1pd496mL599sY-Ju4klRKtMgwkTmEYNzfJArD6Qcuau8Gz04VQ8BQww8r9a3DZcBonX2UCD9KsvBX6_cLByvrgDzDrmnFCSKF0o-cr7-_vRT1iL_GGC-XDS_iTiJRTQzbw4N1JLGwyrcjMEtVB9pGb0cfi9DOhYI_1ag9jMM3YyZi2S_6XRGVYv2eat6s3i198NP70lz6FWk28zEMhnn5i16M7dSmpVlNdVnfU_ejV8WjZCiK2HLsZwu_PaGW4B8S8uTxw79VX4XeYieOfi0WClo3gt0tMjoLseMRbhzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68509" target="_blank">📅 02:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68508">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68508" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68507">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjZzphJaTzydWhmiKWPgoVo_lPIfr9AtvgXz_uQ7PPF1p06_bqY3aVQ_pxxGgUShWYIK1musR0rbMkAwhKGgG0zHixPqrPO3RYmNG2J0Glprd1Llbj-BmaMtGZkDIhkchPWZyqodKt1_kqxo6YZW4e8et0SXw3JBccCVbqvfN4-NQlTzfEfaJpRPm9hRFtjXer-SgM8tygL_5MqVnvimb1r8QhTvGohmafMwY7qXe_PQRcAFGgkatfh3NerDIdzguuSmIGCaMQoVE0yxk2fIi3KfsKjw0mR6ysnJkOXfLC9N4FxoXeR-Hwddsso_tQR7ImLoA47AlQLlKhfF1mghFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ عصر به وقت شرقی، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و تنبیه فوری نیروهای سپاه پاسداران انقلاب اسلامی است که شب گذشته به نظامیان آمریکایی در اردن حمله کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68507" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68506">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام اعلام کرد دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68506" target="_blank">📅 01:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68505">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm9llfHlOia3Hzh2XeNhHNa8_JxSZUmcIU_sP5iPn1FcWTnyHNB5mByMQj8JNKL8my83wLFg5U1NdBCzzD9WU6-oCaI0gIYiSM3KjJUvOomXH3x9eLbBNxq8_4rnNp-qOSHDlmMCerLLQ0x7d1Dq3QnkgVR_acHCj4vvG7kls_P_Sx4No_44Ref_OmQhTt2s5Ny4e74YgSrQTch5H3L6-rs3pGZ0JYCjC6ZAqUxbsBUSsbJYrDVrZWb_qdKqSuiT8w4whyriu8QQvO0ivGEqkKX72EPayqUIK3HGyIne-ieLJ68hUQdIPfvh7W_682dNL5ONBj-hbqxIjhrtu_3fgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
حداقل پل صراطو نزن بتونیم رد شیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68505" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68503">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdhbS5hEM61XaQMg6G6PHuNNWZFaoVCDK6PMueI-i6VFdCU4y0SbcvcQG3cAEZC7SGfp3scnpZUdvyBKanGOE7trzTYo4j6Tcz3TvT1-PTE1YQ2oqTEc8ED1GYylQdUiU3y_Oht5i2wtMUToUDHHWGZU1zyWpbNUc9gLRoxvAqQKXy_4H3S5Y0eL_MQ5aVM6dEM-bfNS3aaNQpLLDMYFdVSjwr62x43M9IXlyI0_7p-AlrqehdCRVzG211yZrhCpmPqK95HVpCIQynQ4lbewidnJZCidw4zPM1lDToQ-A8VuggL-zL0an_Cf268jzOpG__MwrH3i2dPbiB47djtsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwHNGBJ9pL6k_RcC3YI0Qm7qKDXI3XRttxc3YNlvCZVAgge5U0Pm6wMyQVOKxF7vfAc_Aya8Mpik2WNKDtOKnVmMGEcy0zF_W4ITRh0EtQ8bKNRr1lqiue8curyyo2vDoE_Zo0d0iZRXPwlzP_x0R4V5P7BIY_UbYGD3lmf4Sir0r0jhES_TZUHodH5QXCo3R6ZbDKQcfQNejVuze5lF03608mBrl2bcET93aMjiy2Ei_aRrkg0o8d38wm3E79WvDrZ1j_MRyvDENirwO6MiPF452FeBlJAjfKwmu9h2PFP2npXiSIBBEWl3o3TrEkxj08QpNspTPw-GqZtoHuGy7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
امارات خواستار توقف فوری تشدید تنش‌های منطقه‌ای، بازگشت به مذاکرات، حفاظت از کشتیرانی در تنگه هرمز و پایان دادن به حملات علیه زیرساخت‌های غیرنظامی است
🤟
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68503" target="_blank">📅 01:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68502">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرنگار: ایران اعلام کرده دیگه به تفاهم پایبند نیست نظرت چیه؟
ترامپ: خب بتخمم
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68502" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68501">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68501" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68499">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIGejJH0P01GDeXzFjNhxXgBwSLhGciCVBNU-FiucVoTPPA6sUKidvn8Q83nwH9SCnilG6guXHFfliDwDoLBBbaJL4PPXrZpeXftoFhh4qxcuZNlkqqRPZFWMrW9EpMEhrzBeDNf4RsMPbkHS896raGmYdhqiJMvLH25we_vSI3sNpkoCeKTbcSy5Sk9Pya8cWTZntOroAaqCn1cvuCRcW2aQp6MrzBR9teuywXCzCWzAKm644KjpnuMiHKOW2eYX1BqTjKQQrSVrg1Yx08OZ3DaEduV0cCQlvSss05mlGU5j9L1SqplK3rebSM3gjEjbXBWwInk4ENies3a1Gg5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_e_ST1FyYhJ5wn1FBsspwaL0X8au-3-LGSV4Mi_xlQVq1pEXvMB5KfZ37OgijhRorn8XjPK9Buq7WlbyZbF7M1jTAjN41Zhl7xB4_-4iAQxDaYlvs45vrH3yHEJNpPgjZ3I9Nut0_X2VYcogQjh5xLv9IUICbLR_JQpKvb5gk62UVqKuV_DaSKVdyuU9E1ZNVikMlBYMlIW_nUyod0mZaXgJzzhZUxXeBPv2zQQGaPi9_hCeBb1QBfEGREBfV1JSUw9D7z2VN5pGCu_iNmiP3XMlqDzNXBZ7ZkTNzmmVRJRTyfbC1QKCSyT9ti3uaTF8MVp5fWqKceFM5SksWlbrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68499" target="_blank">📅 01:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUGJ694BZD8qyjapdQjNNBuqyZo-NugMP4eBFTlmEBbKr8my_RJjL89MJll46ralBHGETdht_1ETJapralQutWSdtAt1UY2txHnz3Vg5bAovYgbdRPe6f1GAc7EaFQvSDwxOoCloSC9Mu1K-3gw-D9_yL6mmUS6f8zFyZ3OkupFVv-4KXx3rxW7CusX_F1AZoLCU5HEof8dCv-OGhLVAJSNT4Q9dvVHpIMpliG-ypXKXf7b711eKqMTwIr9v87L73k5HT1qGavLL0Ud8qOZM3JF6niSV4dqnGZOrJeHYmNg4iCj5ebUBVs879omJJmOqkkbIQhyAlNKUOT66VSTgSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
دونالد ترامپ، رئیس‌جمهور آمریکا به «نیوزنیشن»، در واکنش به کشته شدن دو نیروی نظامی این کشور در حملات ایران در اردن:
«بسیار غم‌انگیز است؛ اتفاقی بسیار تأسف‌بار است. ما از وقوع چنین چیزی بیزاریم. آن‌ها در راه خدمت به کشورمان جان باختند.»
او بار دیگر تأکید کرد: «ما هرگز به ایران اجازه نخواهیم داد که به سلاح هسته‌ای دست یابد.»
ترامپ همچنین اظهار داشت که برایش «اصلاً اهمیتی ندارد» که ایران اعلام کرده دیگر به تفاهم‌نامه (MoU) پایبند نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68498" target="_blank">📅 01:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS_QY55api9QCJbrIUCTcZfqvukJW1xgMu4x6tNEwAb3fyYXV7dQGMFJAXNo5M2zl0a_pssLPN0dkoG3Hk5DDlJuN629bKs1RNbVUHVA0tIXqa4ZeNh5wAD3Bb1g0oXOAo-_Kd5SrWTJVKX6F7XonDRWPYsEXd5kQlADYXg0tHQGB072NfWIjEkvmSVQmDx7K17x-nTHMHiOrYhfPVvIKa1y4sL46eeCbJ6e7XJXdoQTTzlYd5SvYtymDVbI8uMlcP77tEin2jrtkHXIUWF6idGG_5r-FlhPHaUYTWbuhf4ytNKUP0JNOA3TA17oGTflf9fGvpEtmVI17X3idZy5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه المیادین گزارش داد که در پی حملات ایران در خاورمیانه طی هفته گذشته، ۳۰ سرباز آمریکایی مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68497" target="_blank">📅 00:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
بندرعباس زلزله!  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68496" target="_blank">📅 00:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
بندرعباس زلزله
!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68495" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68494">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8k_KUgbSnAAqR9pOJG7-mrUzv5bsZC27p41WOCu0EVce-DPKzOtvrNgoxIdOG6nO0EhIlDrnfpWOGC68XB3_C6_YZoKctZqQH51snbi4H1xc9XeYM5OE_8pzQfiTX91so6YvqzPK5GNDQnHSs8g3xeoSOLuNlyRBOlSCQ03c6_HPBxiQermXcxpnf7mJ_Vl-Lnt08d3jazBhc2og0sStxKJ6E4W0K3nTHY0IuAjJE7FAha7wd-hxCTVazZbybWfUiAhbGtTJvSnvDbqLKqV7LrxxyoWvKL9rxoVHkswm6ToDiJPpLZwKnwL5Pe2CthSi4Uo-3SSU7irh6ugjJnW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز: ایران در طول پنج روز، چهار حمله علیه نیروهای آمریکایی در اردن انجام داده است.
اولین حمله، یک مرکز مسکونی در پایگاه هوایی شاه فیصل را هدف قرار داد و تا پنج سرباز آمریکایی را مجروح کرد.
دومین حمله، یک پایگاه شرقی در اردن که توسط بالگردهای بلک هاوک آمریکایی استفاده می‌شد، را هدف قرار داد و به چندین فروند هواپیما خسارت وارد کرد.
دو روز بعد، موشک‌های ایرانی به پایگاه هوایی موافق سالتی در ازرق اصابت کردند و حدود ۲۰ سرباز آمریکایی که در پناهگاه‌ها پناه گرفته بودند، مجروح شدند.
یک حمله دیگر در روز جمعه به پایگاه هوایی موافق سالتی انجام شد که در نتیجه دو سرباز آمریکایی کشته شدند، یک نفر مفقود شد و چهار نفر دیگر مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68494" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68492">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cyp1lBbWfsseWfFCbPNn0Mmnkj5IMjlJ8niMS1ETBdzzLA9bXFqzuIONurUkuVW1BUv4o8I5o6Fgg1-M2jBsJ2GVxhvAtvrfWgTDcdLygyeU_J0qhUdMAbsF7bwq8W_jbkt1Tlvx64hSaedPqf2bKzYjazqTKMgnk5O4RYj7IxUWg24CoQWGC0lKOu89RD_MNi3Ooq2caQIZSxxkH014J-Yh87x7agkKRPZyGVhBfvZHNJFc49NX1-A3NAzJIQS-a3ltRaVSPF74KxHk4YzG0zHayzSH2pjQsR9eunOYy-pP2Q0xutNLiAe3plDWtYvb9N6rkhgrQWuUkpG41v9mTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیومدن؟
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68492" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vhkdbn1YVwIEpkWpQd7lNn3Yh3Bd8aDeeGBa4h0qvlsPXcDnXnasc26D5fMcM_Ii2KFzMfHaoi594763dtkinDFvxr5fy8XLY9HTSlMSeFPUh8JQ2e75xjNquvtY3RnPK2n1IpyhhXH6z4T5Idz6mMP1snsFuAnukQCmEEIv7zFkIb4HzMIqW4hB4z7OtlW1e8UtuDk4RH4wr1j1WK_ZYB_KPFwfwlQ-SmuaRMNCIJ8I5jS-KuLKmqS_yYBxJg4X86ShBgV3sIeaOwV6QCdDUZAAeFEqMmTI2R0wST2hDgot6A40xPwRPljlVilm67HzowoBRQ9NUkitYoJf_hFgUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o-rArvBkiRWLQceB1H5allA2RNHaIK955DbPHwQ3wywZbld6BD6E6GfJ4z-63cmGAn4eMOhn0-s28NeKL8nQsua9su5HMqJ9FcSaF841EfPoI1NS66978gRYxmPs52FfcJJ4M7g98fP5KGE-RVN-wbN6nl3t-j60-nrc-jb9QZrOJ-NtMligkC8v3gyxTRmPnLXZn7Db4t3JtFaJoHEKBNGLqxO7i6i-R3xgPeYCB8O5moNjo_3un7GFPTyFDkEZey9VVYxQaHGWD0LIZ-tDHD_WwuK3vitT9NloU1dfrHgc5uDckcmS0qy5sFjQ16nFwaMtci0O0Eb7b2_baqwHEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیلی افشار دوست‌دختر سابق تتلو و پویان مختاری هم این وسط تصمیم گرفته پورن استار شه و یک کانال زده تلگرام که ورودیش 2500 استارز یعنی معادل 8 میلیون تومن پول می‌خواد، البته محتویات کانالش لو رفتن و کافیه کلیک کنید رو لینک های مدنظر پایین :)))
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part2)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part2)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part1)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part1)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part2)
🔥
🔗
مشاهده ویدیو های لو رفته جدید
(Part3)
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68490" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اماراتی های کاکولدزاده خواستار پایان درگیری ها شدند
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68489" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68487">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=CD-e_FeCGNnBc3_FIJzvl1Aa0BKPol6VdfZcowgAdWhDhMFzMO5BHmgOdvjvGk0xx0SjN1-PIxkFXXXROKroarr2lEFvpju19zLjhIDj_M4ojUNeefXXaH17MzPwidCwjwtZG7RSaAgoK1vGnO9QzwtGCio7woact3F7nTRKCgqVegNrP_jyy20oD5-mtosicTvheRC2DE0ygp7I9UeddGdyaarEMv8litg8YHRqRNlId-eNi0NApOzPb6F45n_IrbUxb-rUDjirf8cI8rEAn13zXmK9dFTPY4hTTTP30uhPMvGixrOcOeL4tGca-cuIVu_zKQOcpQFf-fL_2ckOdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=CD-e_FeCGNnBc3_FIJzvl1Aa0BKPol6VdfZcowgAdWhDhMFzMO5BHmgOdvjvGk0xx0SjN1-PIxkFXXXROKroarr2lEFvpju19zLjhIDj_M4ojUNeefXXaH17MzPwidCwjwtZG7RSaAgoK1vGnO9QzwtGCio7woact3F7nTRKCgqVegNrP_jyy20oD5-mtosicTvheRC2DE0ygp7I9UeddGdyaarEMv8litg8YHRqRNlId-eNi0NApOzPb6F45n_IrbUxb-rUDjirf8cI8rEAn13zXmK9dFTPY4hTTTP30uhPMvGixrOcOeL4tGca-cuIVu_zKQOcpQFf-fL_2ckOdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایونت ورزشی، ۲۶ تیر؛
پارک پردیسان پونک
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68487" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68486">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام آمریکایی به شبکه NPR گفت:
«رئیس‌جمهور ترامپ دستور داده است که فرماندهی مرکزی نیروهای آمریکایی (سنتکام) در ساعات آینده، «دروازه‌های جهنم» را به روی ایران باز کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68486" target="_blank">📅 23:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68485">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=aM44CdhgQpmitNnfHw5DPTKUxDGQOswF9-6KGze4hv3yoAr6Eh5M0LAAc9oYF_93gGdmxMIANBtyFiKkIvhYXD8LFeM5t9W7f0bQqZeBspp7fwHfW7hKsUJCt3nfsEyiKqYyNmfDJ_3_ZHdj0bvzOOJnw5zhrJ1lk8iZPuXOHBbC-EwmQLAb_jXwM4VHDLMYiYOVE76RJM1NGBxDIHZb8JV9nj-d2kXAPKQBHYi4GPllb_v5q8L9VlKsfW7XMz29e4gY603uqhyqzMOUikGJWfZ7BRs23hVJ9d2EsGs-Fzx70x3grCaMJzNi6-ILQ6SIrooDLGiP12rbHt0JYjQVng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=aM44CdhgQpmitNnfHw5DPTKUxDGQOswF9-6KGze4hv3yoAr6Eh5M0LAAc9oYF_93gGdmxMIANBtyFiKkIvhYXD8LFeM5t9W7f0bQqZeBspp7fwHfW7hKsUJCt3nfsEyiKqYyNmfDJ_3_ZHdj0bvzOOJnw5zhrJ1lk8iZPuXOHBbC-EwmQLAb_jXwM4VHDLMYiYOVE76RJM1NGBxDIHZb8JV9nj-d2kXAPKQBHYi4GPllb_v5q8L9VlKsfW7XMz29e4gY603uqhyqzMOUikGJWfZ7BRs23hVJ9d2EsGs-Fzx70x3grCaMJzNi6-ILQ6SIrooDLGiP12rbHt0JYjQVng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که دن اسکاویینو، از مقامات ارشد تیم ترامپ در پلتفرم ایکس منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68485" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68484">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68484" target="_blank">📅 22:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68483">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇱
نتانیاهو شیرِ یهود برای آرژانتین در فینال جام جهانی در مقابل چپول های اسپانیایی آرزوی موفقیت کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68483" target="_blank">📅 22:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68482">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68482" target="_blank">📅 22:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68481">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ پیت هگست: خدا نگهدار قهرمانان؛ فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68481" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68480">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖄𝖚𝖘𝖊𝖋</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=X4w3GFeS410wxqmsjPtaMURqq0BbJVPEwzl43f_ZW_hBzzfdHwuT7DXAK08YbbcYQkGJsQqnt1IfZxdkzpLe7kTsH61S-7bKrb27REMxGX7lg5GXWEd0nTgIGeERZmyIf5A_UCEHE2z3rxZ-HTERoRUam9Jx6aCiO509H5bQxvM2zjmvX5lUQvsQ1mKAWeGgSnsWYpH0Sob5ZL15f-3Qed7t8uSagFM3xkzg5X0TmzKcDsSSEJHjLahV0Ym-E2EDTEvGypJ-IH8ZrMjo5_QLmAZ5Km5ogPVCBxnvd8AbfRt8EdzwnD2U7CmLRFgHIztES3S1KSHl17-b286DHmIfmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=X4w3GFeS410wxqmsjPtaMURqq0BbJVPEwzl43f_ZW_hBzzfdHwuT7DXAK08YbbcYQkGJsQqnt1IfZxdkzpLe7kTsH61S-7bKrb27REMxGX7lg5GXWEd0nTgIGeERZmyIf5A_UCEHE2z3rxZ-HTERoRUam9Jx6aCiO509H5bQxvM2zjmvX5lUQvsQ1mKAWeGgSnsWYpH0Sob5ZL15f-3Qed7t8uSagFM3xkzg5X0TmzKcDsSSEJHjLahV0Ym-E2EDTEvGypJ-IH8ZrMjo5_QLmAZ5Km5ogPVCBxnvd8AbfRt8EdzwnD2U7CmLRFgHIztES3S1KSHl17-b286DHmIfmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش پیت هگست به کشته شدن ۲ تن از سربازان امریکایی</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/68480" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68479">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=YtD8RThXkjSaKqVttAmlYFrRrnyzS-UUNsD_SX8Fb29K9qGRYjViI-HlkS3mwsw4gTn60O1uuaVJOY_RE1BxrVPvxzHHhsGVff471N1QP5gjW2qj9DvEFg2aJpSFKsbri3Lo_7mUkM6kQgQXQnywuHWT89vImiVzsTkfBQK5IfKO5NIDVgKAGejmsZKssxnBTIM3cx-UlREdDRGGB02etHJt4WYNK215Ph_pR2qDd7u0X5V2t8x2MQUy7p6zJoLYudIYutfFwWDtE5OoH2uxIV4xGAxlF6Q4S4_Az5aqd2F-8UxeMmf8VVI_XrfZczI-5Yzh1W1tFj2ARRtyAP34tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=YtD8RThXkjSaKqVttAmlYFrRrnyzS-UUNsD_SX8Fb29K9qGRYjViI-HlkS3mwsw4gTn60O1uuaVJOY_RE1BxrVPvxzHHhsGVff471N1QP5gjW2qj9DvEFg2aJpSFKsbri3Lo_7mUkM6kQgQXQnywuHWT89vImiVzsTkfBQK5IfKO5NIDVgKAGejmsZKssxnBTIM3cx-UlREdDRGGB02etHJt4WYNK215Ph_pR2qDd7u0X5V2t8x2MQUy7p6zJoLYudIYutfFwWDtE5OoH2uxIV4xGAxlF6Q4S4_Az5aqd2F-8UxeMmf8VVI_XrfZczI-5Yzh1W1tFj2ARRtyAP34tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه اصابت موشک‌های بالستیک به پایگاه موفق‌السلطی اردن که گویا منجر به کشته‌شدن دوسرباز آمریکایی و مفقود شدن چندتن دیگه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/68479" target="_blank">📅 22:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68478">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیش‌بینی می‌کنم که حملات امشب، از دیشب هم شدیدتر خواهد بود... #hjAly‌</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68478" target="_blank">📅 21:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68477">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">همونطور که پیش‌بینی می‌شد، دامنه حملات امشب گسترده تر از شب های دیگه شده و حتی حملات به یزد هم کشیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68477" target="_blank">📅 21:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68476">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=t88xr92JClwwvHqyM7_FUjt50KcZmguTTMe_US0SgkhrTpdmUrmtED1v4snZ1sjrRM9eURyb2KZZ8QI5HxY33rDai47A3UFaiKTkQ0Nr60eUDZMweV7w1haiR9Jl2z8lV4oyX286mA7ebjo0QnGh5xqhj2W3al7dUInm2YnvEwBDo76Xu0YKAU_w-XarvOZV6JdxSrPDYVj59_-y6Yv60070TMXvPEZlDjVxUiUlVtMMgmlJEaxNf-q_juhWDbhbS_X_vbnk-sHreVVqLtwxp2rQ2cbXa0o1LTXfunr784ncqsPP3lA1Z71X6TgYdcPvUXIM34eTwejktn3hiq850A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=t88xr92JClwwvHqyM7_FUjt50KcZmguTTMe_US0SgkhrTpdmUrmtED1v4snZ1sjrRM9eURyb2KZZ8QI5HxY33rDai47A3UFaiKTkQ0Nr60eUDZMweV7w1haiR9Jl2z8lV4oyX286mA7ebjo0QnGh5xqhj2W3al7dUInm2YnvEwBDo76Xu0YKAU_w-XarvOZV6JdxSrPDYVj59_-y6Yv60070TMXvPEZlDjVxUiUlVtMMgmlJEaxNf-q_juhWDbhbS_X_vbnk-sHreVVqLtwxp2rQ2cbXa0o1LTXfunr784ncqsPP3lA1Z71X6TgYdcPvUXIM34eTwejktn3hiq850A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
یادی کنیم از این سکانس که ترامپ چند وقت پیش در تروث‌سوشال پست کرده بود: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68476" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68475">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:  در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68475" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68474">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chu9VPOdhRBahtrk4W28dKJnRcK6qpBxsEVH--M2r241BjEeMHVqq4VQKOUR-1-K9SAZsXzmjS2ahl_RmLwI3_5OjnxaniKjV3AkklVsuot4UgGR_aw6wT0FX57yUzBNE93BKViziEreNDOc27677tBFTFuKiBcT2kV7nwq6c1H8rEaCpCXEZfWigR9XI0HQVGkSeIeRi62z93r4S-8aCRj0qWZ_m4evY-g0KvCA92iaAA_sgfY46vcHkrMtSAvqRc3g3OD4SG0lPGwaEBrlZIiTXTa8uGSJVwgUnC5eYTbBgzcVj53WSZSEoiQ1DSWEjTVo-R--zDTUZ_AdSjri-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.
همچنین، یک نیروی نظامی دیگر در حال حاضر مفقود است.
چهار نیروی نظامی آمریکایی برای مداوا به بیمارستان‌های اردن منتقل شدند که همگی تاکنون مرخص شده‌اند.
سایر پرسنلی که به دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به محل خدمت خود بازگشته‌اند.
سنتکام به احترام خانواده‌ها، از انتشار اطلاعات تکمیلی — از جمله هویت نظامیان جان‌باخته — تا ۲۴ ساعت پس از اطلاع‌رسانی به بستگان درجه‌یک آن‌ها، خودداری خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68474" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68473">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=uvlDh7M0GMwTn2wzRQIGupmc-5-G9B30OBXmuvBohWx89bdjcKi4YAz9tKOwEn6yOnLHeqsX291IFC6kPFKaA_W6pw_zVstK454FMjoQa2j3DqgBLxKyAOwvX8cvgiyNFlwDvw120hPsvOqEwNbkJdyhIJm9Q9jhkRYsOAkp0XGJJM4fD2dJJUWG54Koda-GVO4uhnF5BRPdK9AruSNcTApdNWM3Tj8AoR4e5MssZ89IzhQH_7p2mCpMJsidFjkNR8u0AmBmimbvoLbNo1x1ajL7n4ITKaDWCdbiwn4Sg68q_RHesq85XxEm_1fAwYrbhN5w2rpX4scIYfGQ3Pqc0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=uvlDh7M0GMwTn2wzRQIGupmc-5-G9B30OBXmuvBohWx89bdjcKi4YAz9tKOwEn6yOnLHeqsX291IFC6kPFKaA_W6pw_zVstK454FMjoQa2j3DqgBLxKyAOwvX8cvgiyNFlwDvw120hPsvOqEwNbkJdyhIJm9Q9jhkRYsOAkp0XGJJM4fD2dJJUWG54Koda-GVO4uhnF5BRPdK9AruSNcTApdNWM3Tj8AoR4e5MssZ89IzhQH_7p2mCpMJsidFjkNR8u0AmBmimbvoLbNo1x1ajL7n4ITKaDWCdbiwn4Sg68q_RHesq85XxEm_1fAwYrbhN5w2rpX4scIYfGQ3Pqc0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
اگه حملات آمریکا تا چند روز دیگه ادامه پیدا کنه، وارد مرحله تهاجمی کامل میشیم
اون موقع دیگه فقط جواب حمله رو نمیدیم و حملاتمون گسترده‌تر میشه همه جارو میزنیم
آمریکاس که ریده به مفاد تفاهم‌ نامه و همرو یکی‌یکی زیر پا گذاشته و عملا از تفاهم نامه فقط اسمش باقی موند
آمریکا از جنوب لبنان عقب‌ نشینی نکرد، توی تنگه هرمز مسیر غیرقانونی ایجاد کرد، به حاکمیت ایران احترام نذاشت، به سواحل ایران حمله کرد و اموال ایران رو هم آزاد نکرد
دیگه نه روی کاغذ و نه توی عمل چیزی به اسم تفاهم‌نامه اسلام‌آباد وجود نداره
اگه دوباره مذاکره‌ای شروع بشه، از طرف آمریکاست و اونه که دنبال نوشتن یه تفاهم‌نامه جدید با تغییرات تازه‌ست
اجازه نمیدیم نیروهای دژمن از تنگه هرمز رد شن و وارد خلیج فارس بشن، چون امنیت کشورمون به خطر میوفته
🌅
قبول نداریم آمریکا توی تنگه هرمز، که گلوگاه انرژی جهانه، نقش یا حضور داشته باشه
آمریکایی‌ ها منتظر موج موشک‌ ها و پهپادهای ایران باشن چون ما جواب حرف‌ های ترامپ رو توی میدون میدیم
فعلا سیاست ایران اینه که هر حمله موشکی رو با همون شدت جواب بده
انتقام خون فرمانده شهید و شهدای جنگ رو میگیریم
آمریکا میخواد با محاصره دریایی، مقاومت ایران رو بشکنه
ممکنه دوباره به سایت‌های هسته‌ای حمله کنه یا بعد از اقدام نظامی، ایران رو به مذاکره با شرایط جدید مجبور کنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68473" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68472">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68472" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68471">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=akju1PnQRYk3Kg3jLLzJpX3i27I5DA2Dfv88WU9sg0hqrUl-3FJ6LMdRDm6Q6Tj9O4duhzy4OTlersxVQ-3cta5KOJqol7FyXKLBY22BjOkrXEst3h-PIsrNTtdR0ryNlp-GhvXWBM3AwOdaKgcdTCT1GVyBhs-Dj4cANPRSdfSKPJIcV-OAAvH_YFHivj4NekB79McaQjeMP5zvyjfmIVtFCvfPKEEN1KfNOyW0tzV-Rg1HlKIOu8o7-zUyhY0j0X1oM05vAYWJPEg1kAdA29xIIjubrP0YtWTfTJ53WPXYNn5TbOp1a_xoxnOjxuRn4EOy3m2kRP6uC7TCykoTWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=akju1PnQRYk3Kg3jLLzJpX3i27I5DA2Dfv88WU9sg0hqrUl-3FJ6LMdRDm6Q6Tj9O4duhzy4OTlersxVQ-3cta5KOJqol7FyXKLBY22BjOkrXEst3h-PIsrNTtdR0ryNlp-GhvXWBM3AwOdaKgcdTCT1GVyBhs-Dj4cANPRSdfSKPJIcV-OAAvH_YFHivj4NekB79McaQjeMP5zvyjfmIVtFCvfPKEEN1KfNOyW0tzV-Rg1HlKIOu8o7-zUyhY0j0X1oM05vAYWJPEg1kAdA29xIIjubrP0YtWTfTJ53WPXYNn5TbOp1a_xoxnOjxuRn4EOy3m2kRP6uC7TCykoTWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68471" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68470">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی مبنی بر وقوع حادثه‌ای بین یک کشتی تجاری و نیروهای نظامی، در فاصله حدود ۱۰۰ مایل دریایی به شرق شهر الدقم در کشور عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68470" target="_blank">📅 20:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68469">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
تفاهم‌نامه بار دیگر ثابت کرد که امضای رئیس‌جمهور ایالات متحده هیچ ارزشی ندارد و هیچ اعتبار ندارد، و مردم ایران درس‌هایی فراموش‌نشدنی برای دشمن آمریکایی دارند.
امروز، "شیطان بزرگ" بار دیگر بدون هیچ پوششی، چهره واقعی خود را آشکار کرد. این تجربه تلخ از جنایات و نقض عهد، مدرکی جدید و قاطع بر دروغگویی، بی‌منطق بودن، عدم شایستگی اعتماد و فریبکاری ایالات متحده است.
اکنون که دشمن آمریکایی در تلاش است تا جنگ را شعله‌ور کند و هزینه‌های گزاف بیشتری را متحمل شود و اعتبار خود را بیشتر از دست بدهد، باید بداند که مردم عزیز ایران و جبهه مقاومت، درس‌هایی فراموش‌نشدنی برای او دارند. در این روزها، شجاعت رزمندگان اسلام و جوانان مناطق جنوبی، نمونه‌هایی از این درس‌ها را نشان داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68469" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68468">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای ساعت ۲۰ پیامی را منتشر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68468" target="_blank">📅 19:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68466">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
هم‌اکنون زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68466" target="_blank">📅 19:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68465">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azLlsUVvqj8awtlHYosDtFzjr8u9lFM_JpuBc0hETQue0olsU0moNh4RN_FkWMRFq4Vegh0GrAw8X1pWu2x2vVyFfVJbbTmiy1e0fKntdaAG4OebY-GRsFSRlKAwqHOkU1sNiZlJf-aiq2MFXc2UZNR-TMm2n7SBLcvfZHIsNsPkA_ksxzVwr12FFkI6i5iZY0WELS7NFbrc48_MQxnIcjiBYLQjkN-c34paW5cU0OW517syEmbAHTAq2QisHsoSWfy0D65bhCmuJ7vw4GCdpS9paB8goVlfni_7oJM9XCQKg3sihb0ozzC0zBA6n7HidA4kc5uRXAcSLxGJ1QvqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68465" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68464">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68464" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68463">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=CbLyr6oh9jSZvncgM5j6a8z5d3Xd1CoOCJRi2Ua9W_xnQahk6tLxRrtxRJ4zIq6xsP3D-wAqrE8Q5WAMcPIbE19Ojl3fsZw_J5WLyMZEeWwGUR_EQbl8YHcwlkThlRXPMNrvcR8OY1zNP-OU7cwFQahKy6JRTJecUyxoUAY7BG_mVG3whayqURv2Ac5BdCGkQpmNis1Ru3PJYKo2AuTcmYQZd4l7HMKcPBwV2VXfQ5QeCpQFz1gdJa_4MChkIuiH-xMEHjCaNanosK7rU_J9fL3s-TwlVrTFohPL6NFG03Zb-IIhi73ESk5hjLdOSxJ4e6qTl1bXxT5IC9U_UUht5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=CbLyr6oh9jSZvncgM5j6a8z5d3Xd1CoOCJRi2Ua9W_xnQahk6tLxRrtxRJ4zIq6xsP3D-wAqrE8Q5WAMcPIbE19Ojl3fsZw_J5WLyMZEeWwGUR_EQbl8YHcwlkThlRXPMNrvcR8OY1zNP-OU7cwFQahKy6JRTJecUyxoUAY7BG_mVG3whayqURv2Ac5BdCGkQpmNis1Ru3PJYKo2AuTcmYQZd4l7HMKcPBwV2VXfQ5QeCpQFz1gdJa_4MChkIuiH-xMEHjCaNanosK7rU_J9fL3s-TwlVrTFohPL6NFG03Zb-IIhi73ESk5hjLdOSxJ4e6qTl1bXxT5IC9U_UUht5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این ویدیو کامل نشون میده که تحرکات هواپیماها های ترابری امریکایی از سمت اروپا به خاورمیانه بشدت افزایش داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68463" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68462">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njLa3tQHk7QvolWNMw7210LbgisdADghuS2EwTLBeZjaJ5Z0SaS3YBOkyNK_XsWQfiKOYzeSW6ECflVAFXMkyw64nKX9eJvapBQYbVpBbEGye-BMy66PY3qbFjJTj4HflUvMw9JDn6GeoI9gVdr4MjcNNnzd7ChzWp6llhmyvL0caj3r0rLhXLI4VoQWA1GnewZJRJWo2Wq6xpl9HxGJFEEnnlZqIvWFwnMH50vGrsVUHuS07ScP6csP0cYYWzG-CYQ5LB_ueJGsHX78a8klEneqa8o3yKtcrBf2XtV6ObAyhJENQjtvnOYVahNmNXBHdmBmJN_Td0Tb_HFTWekj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68462" target="_blank">📅 18:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68461">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwgdJsYiFkxLXj9m43IqbkQF1hg3A90x8Pkt_srf1Z_fXcTst7TBXu23VgfWsC-Tta3jl9XzMarQBalgUBzgTdgb6HUynIKlfL_0zrs6BqLa_ewu19on-CXPtDEx-qENi6epKal3kW8D0QCNPsJX5p7gnCh5MIFogZQi4-cxtCjIwaSQ9CPn9cUZrsxEdGLTg5l4HZI_0eMJvJaEhP15Rr3NC1u9j0qrOHWt-FauWR-vL73XwgC2cRZQmbhO6I-oCXhJJbA5ymAAqs2bldLoOG_Xhmk4V_u-1utAObMZCN5dU-y5vW1yDhf5wmE0AxHDB-E-Hqc8vPPFt5U1IyUcPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نماینده مجلس:
بنزین گزان میشود؛لیتری 10 هزارتومان
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68461" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68460">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:  «اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68460" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68459">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:
«اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68459" target="_blank">📅 17:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68456">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=tu6G1yx9h_x3YTev4XtGfCjIgkcnT1otIDCe5ZL3Dk8gfv5wTOT3WE7P3cDNDnfzP_fe9IGVvmJnJAVhacTWTg9mZXQefGO05bo97_XFrwYpbDZi5ar528nFJU_J628YPZlw2gnxiNkBK4nIrzq__Fv_IKf5VputBXhY51m7o6cDuGPKKoXgMEzyMzosGw5abVAQ3YIiWnrIHcGVzrl2p42N-pxQcqAtyZ56vx9KDk-7NEUlLN5Md5wtvInLOHD99Mk5juapuH5O01fSsKerwhxr2kU2UzpuW1MZzPnOYVxhmYpc6jGRGLh6XW9MB6JNXyUDBPEWXYZcsmfmBtAU5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=tu6G1yx9h_x3YTev4XtGfCjIgkcnT1otIDCe5ZL3Dk8gfv5wTOT3WE7P3cDNDnfzP_fe9IGVvmJnJAVhacTWTg9mZXQefGO05bo97_XFrwYpbDZi5ar528nFJU_J628YPZlw2gnxiNkBK4nIrzq__Fv_IKf5VputBXhY51m7o6cDuGPKKoXgMEzyMzosGw5abVAQ3YIiWnrIHcGVzrl2p42N-pxQcqAtyZ56vx9KDk-7NEUlLN5Md5wtvInLOHD99Mk5juapuH5O01fSsKerwhxr2kU2UzpuW1MZzPnOYVxhmYpc6jGRGLh6XW9MB6JNXyUDBPEWXYZcsmfmBtAU5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی در کویت به دلیل حملات موشکی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68456" target="_blank">📅 17:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68455">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm1S11Uxx9qXCJQ954cSNZHru8wLsqrNmFLmExPJIlsy9aoQ9wlkF0WLdtNh8cf9ZsHrmRLYlqBuG4MwAOX0oCJm2sXKYNsutbi-_rxZ3612MylZ1e4BNdrA2FsMJr4rWJTZZ91qM0gVeBKahRTst_lZKjdUnfJQfdgh1nv31GYSsuy61vFzOC3OW3PGvZem9pWzwumiH_kuojbfQ5rfuDlAKAlyp003BhE4lqtDQio67X0buATKo9wFhgHJy9epaITg2Nsb3GEAm2We5mVyqtLhK-Pzb_Ol8_zd8CMZVdPQ4s0wu9cGzPbnY75fx6c6JuD80KYoqENBQETq_vo59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛معاون وزیر امور خارجه جمهوری اسلامی، کاظم غریب‌آبادی:
«از این لحظه به بعد، ایران اجرای تمامی تعهدات خود را بر اساس یادداشت تفاهم، به حالت تعلیق در می‌آورد.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68455" target="_blank">📅 16:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68452">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00f574479.mp4?token=Szd-F1fSmrdGNPX7uwtJlrUHxKzgFjvf1SPVJPk9M3XXExbwX4BnTkyJXQg6qJaeLzyrhuSGdFqJez9JHRPCnMiZw4CkLBCxQ6vfP_eJv7AOjrINMRYGNnLYOlYaNBOJVp-Nk8vHBdGDhehb_tgPE5QO21NHyyYW4s1xkDWIRtxwhEaYmxT7XyCg_-PrV_D2PvWgB9qgWZDu_zfNGMOGijwpuF1vXgnD4gxn4hT5avsO4Zq8bw-XsZveYytSDKZGhyphqGSCqs-XQJWgJFHfrtaITyVc6dY3h7_OVtOB1akh1vxnN_FFCCnb0m-H_2IdnYIAspibQYke1280maf3Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00f574479.mp4?token=Szd-F1fSmrdGNPX7uwtJlrUHxKzgFjvf1SPVJPk9M3XXExbwX4BnTkyJXQg6qJaeLzyrhuSGdFqJez9JHRPCnMiZw4CkLBCxQ6vfP_eJv7AOjrINMRYGNnLYOlYaNBOJVp-Nk8vHBdGDhehb_tgPE5QO21NHyyYW4s1xkDWIRtxwhEaYmxT7XyCg_-PrV_D2PvWgB9qgWZDu_zfNGMOGijwpuF1vXgnD4gxn4hT5avsO4Zq8bw-XsZveYytSDKZGhyphqGSCqs-XQJWgJFHfrtaITyVc6dY3h7_OVtOB1akh1vxnN_FFCCnb0m-H_2IdnYIAspibQYke1280maf3Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
چند روز پیش یه ویدئو از یه پسر نوجوون وایرال شد که از سرکار اومده بود و داشت موتورهای یه نمایشگاه رو با بغض نگاه میکرد و حسرت می‌خورد؛
⏺
این ویدیو خیلی دست به دست شد و نهایتا مردمِ نازنین ایران، تو کمتر از یک هفته پول جمع کردن و واسه آقا یاسین موتور خریدن و اینجوری سورپرایزش کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68452" target="_blank">📅 16:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68451">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون جنوبی:
همه دارن از جنوب صحبت میکنن که دمشون گرم ولی منی که خودم جنوبم نمیدونم چی بگم.
درمورد پمپ بنزینی که یکساعته داخلشم صحبت کنیم یا مثلا درمورد برقی که الان رفته و نمیتونم برم خونه صحبت کنم
درمورد ماشینی که نمیتونم خرجش کنم صحبت کنم؟
درمورد وسیله ای که میخواستم بخرم و امروز صاحابش 40 میلیون گذاشت روش صحبت کنم؟
یعنی حتی نمیدونم از کجا شروع کنم
ببین قبلا به موجودی کار نگاه میکنم میگم خب بعدا این چنین میشه اما الان تخمم نیست
الان میگم بتخمم ک میزنن نهایتش اینه منو میزنه و میمیرم
چرا برق بقیه شهر های دنیا نمیره برق ما میره ؟ ما اضافه ایم ؟
بدترین اب و هوا و اکوسیستم و بی برقی و جنگ مال ماست نمیدونم از چی باید بگم
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68451" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68450">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJYEuXOpsNtDYibvAYmPd5V6geZRW9DsN8KfQGzl4Ua65UQA5uQ29wLXh63Ut-E9o1K3Rc6DBUwRaiY9_y3PF_BesH2Q7fOr6ESsYuFa_mH7sMYDLonMPs8FeJmA3LYOt9tTl3X5nz4db_QmG7N5BWInMHolTrGAvquQHFUFVHECnkkt5hDXVLeP4CUeek2wxMr594P2W8NPqTwVKEYbonkJUL2RC9gTE8XcFBTL52a4jRTdBN-5mnQVRUSmtQwdOiY-jNvT5Ep4VMzMiu7g4U8ngW2GgOsZ_dUyB-FxEsbNokqMwl1zlMY9E3hRTcS7CDGGkOGd9Vgq-4SFiXZIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حکومت داره به جانفداها زنگ میزنه که بیان آموزش با اسلحه ببینن و برای جنگ آماده بشن
😂
😂
اگه کسیم بهونه بیاره که مثلاً مشکل دارم و نمیتونم بیام، میگن اشکال نداره، بیا آشپزی کن یا کارای دیگه انجام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68450" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68449">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=aozM_6AhNY_vj1T4o76hWOBNDyJwE56TrQgSwUGlQaGsJKraa-JzY8pHgrbnRrL0x39xTwc0WTZ-xcHZqHF36g9A-79HPDSH5z4j3Xr5bpaDYB0-azv2kKm21E2FYRFZeVZyA_fu2FvhVFVz25AnFxYGlAikP4ao14xPd2UEKvwp5MUqB125YNwrdo4a3DorIUZglM_d6jN_lm0kasTYmAA13tVTt18_-12NPN-OCexa6T1UsFiuXRwSzzRxTPDcP0Ghr5dkHqZw2ZNtwdcg5IUkdEPInUQAw1HeVOgxHadteUjicXv19NJsoiFg2WHCjqHTbaAMipfE5a04eFy_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=aozM_6AhNY_vj1T4o76hWOBNDyJwE56TrQgSwUGlQaGsJKraa-JzY8pHgrbnRrL0x39xTwc0WTZ-xcHZqHF36g9A-79HPDSH5z4j3Xr5bpaDYB0-azv2kKm21E2FYRFZeVZyA_fu2FvhVFVz25AnFxYGlAikP4ao14xPd2UEKvwp5MUqB125YNwrdo4a3DorIUZglM_d6jN_lm0kasTYmAA13tVTt18_-12NPN-OCexa6T1UsFiuXRwSzzRxTPDcP0Ghr5dkHqZw2ZNtwdcg5IUkdEPInUQAw1HeVOgxHadteUjicXv19NJsoiFg2WHCjqHTbaAMipfE5a04eFy_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واسه دومین بار طی دو روز گذشته، جمهوری اسلامی به نیروگاه برق و تأسیسات آب‌شیرین‌کن تو کویت حمله کرد و باعث آتش‌سوزی شد.
کویت حدود 90 درصد آب آشامیدنیش رو از طریق آب‌شیرین‌کن‌ها تأمین میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68449" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68448">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUn3X-OjQpR0D0itYGbjl-PKxDTYv7gGWJEbU2mq2dT2pYH8lq4QfclWVP_q-yfRoDbaXX-7Gb8qYpKHFWEc76Sf_UUxZVvgySMXK1cf3OyYSNRFiLpmwBHXKQffsUTksqaNebWNawWTV-hrsPrYvirvFpNVAF-2MnWdsPqvnxzhRz66BO5XFjJEqq-7plPBMNDXY8QuLNE9nsOFSkpiiuK2zAO0Pp_Rv0ZANJpXlGwwkNDpVtGZk6Kb6hbeE8a7Mo8OZyjDmEJGREa70aTksV6a4ILJtnnAR1esXwZ6rNcf-AZjO3FQMTV0T_HM3ehE6Ck_0RyhHzFpjGCYbczebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68448" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68447">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68447" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
