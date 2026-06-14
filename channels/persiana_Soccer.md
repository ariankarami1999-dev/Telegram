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
<img src="https://cdn4.telesco.pe/file/ByJo-9dl89Khdp4gk2KH5hMFuiT452PcrZi90zHfIs75IwHbZB6rYJgkT6DzNhuVUQoDv832gkclwpTzaX_cysIlIBR8AIPACTNcGXlJybR-IsGuR3Xe3ti0whTYux6uUjSzM_lIfb5wacgCk1lC7CbfBBSBG1aIXU4iPCbFZg9mwI3QifZAYkNM20cAViU1OOjuFS_VXvdHPPtJ0leyyzOWpPPBNcDr3DCxXfqRpYqcgJPFWZBhRBgnVBgF3RyNVTuOt9jCPuheSRZJeM3isMkzZeklhwwGCjVg5NVQfu2iuTiS-3XFjc08PfKdr-V7Cpv8labVVcMU1yaJz1p-Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 246K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 09:56:35</div>
<hr>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb4mnne2MDT6UvMKT59BenLoWPaWozRWtxJRwzLQI33aJBNxLGl9i_eZJIECFpZjUDA1As-Tfxzu977p7SrGihs7CdhklMZHXfHQZBQhpm0l3eVJFq-y4EigsUajZiE4bOg-rGAqlldHjMlgvJO4ZeUe1wq7mLAzqTMuneX3fALPJReq4kUlg76M-siDCg6eyjmDWW5WLKhwTZzAojbEKJehBzwza6BfZn-_3eNL5f307NO86PgEo18BJ4OSo5IWf1lRrkHBdsx0mVFEpa2vByNYcnx55HaMPv4vb0Vt8rsb1WSbGop2JSFTxgZF3qeUMTgEfiH-Nn32as1da4HuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=KPibLAMiQFN5Q5WVmyccHrPzywTokm76DN0qUdz2-J2ffhivMaYFW17gI9pp2caMb22zrnvM3YUx8igC8HiY1HrriA3ViKryTL2XnzgrMREwJCJ4yZkYmtQMPMkiq4RnHNqs_KJhQ8fb7w89ymhyvXm4N2gvmFTpIv3ju6TK6OYAA8-yYI_2VqlvPywlJbaqlW_GTkpndp_0530205gAwD7Uxod2mOSRF251cLlqG6TCOaVI3rCYeISMAPMuzryZyatk3FGnYVZH7pqSjcNOCCqk2f_bLXkC3N6E_dgBDoR3y8PNd36UET7g2fUS3s_bX0Lkxz0D86l3r7phaxQ75A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=KPibLAMiQFN5Q5WVmyccHrPzywTokm76DN0qUdz2-J2ffhivMaYFW17gI9pp2caMb22zrnvM3YUx8igC8HiY1HrriA3ViKryTL2XnzgrMREwJCJ4yZkYmtQMPMkiq4RnHNqs_KJhQ8fb7w89ymhyvXm4N2gvmFTpIv3ju6TK6OYAA8-yYI_2VqlvPywlJbaqlW_GTkpndp_0530205gAwD7Uxod2mOSRF251cLlqG6TCOaVI3rCYeISMAPMuzryZyatk3FGnYVZH7pqSjcNOCCqk2f_bLXkC3N6E_dgBDoR3y8PNd36UET7g2fUS3s_bX0Lkxz0D86l3r7phaxQ75A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxyyPlQhTTpB7p1iMeDoZN1IO3N-kUU67Kbdbnzp88DxDW8Km6iS4nqDkOaYJL5dw6rsXPRL0qN5UZTk2x_sLpxX2nbO55-fz7OzHy320OoyQgXaLJVG1wTuQDOjqc1WwXj5r-tva0idFAwi6uLNBPgjF0MOK2IbC2p12x3-vad_0okGSbPDl_J2IK7ZrI2jdxTuazyR5MhAubMtd7aeNmHmETsoO0T_gokw_CZHFRUL8_Hewj8pM9hjRWKgTfEX9rzESZkN058KLnhrNWkxmvjcC572kIChABgbZgkGwkG8yrdtwZSmDUZzUpxJiX1f6koQrvLdMmjlG6F02urk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=a2UJ7uCFxgU6F6ouE_NnwLDCwW3StWul6boDBeShMwYpwlU7bNhNduRQVM8RpAuJEJfRWY0YCYPopifph8h6Ke8Bv_DOHyoF19pChv6VeyPsenR_EvIwFJSuw_HyaoS760spMNl-NCZA8zgxzwgOOcaiUmKgvcKz70X6BNMaLs9PzvDHDcx0is0vJFQ2cpfc8VpcTffgtbzJ-nNmbunVbTHaNx0YRPSDvbUp_g-ogjDO7Vchct5947IfNutw8q_FVK4n0Mrlmb_yMR6IlbV1BPq6ieokrLuVMACQvX9-k6YNH5gfoBS0i4OQU1Yk5q16Kpe1YeY0QWelJPupDSqoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=a2UJ7uCFxgU6F6ouE_NnwLDCwW3StWul6boDBeShMwYpwlU7bNhNduRQVM8RpAuJEJfRWY0YCYPopifph8h6Ke8Bv_DOHyoF19pChv6VeyPsenR_EvIwFJSuw_HyaoS760spMNl-NCZA8zgxzwgOOcaiUmKgvcKz70X6BNMaLs9PzvDHDcx0is0vJFQ2cpfc8VpcTffgtbzJ-nNmbunVbTHaNx0YRPSDvbUp_g-ogjDO7Vchct5947IfNutw8q_FVK4n0Mrlmb_yMR6IlbV1BPq6ieokrLuVMACQvX9-k6YNH5gfoBS0i4OQU1Yk5q16Kpe1YeY0QWelJPupDSqoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCS7yh9mGJu26UlEa8XBTzFOZuyRMBuX18-tF4hT1DYtF3haCUqcJWaaKaWzq9yxCVkPq3Z_PwNHyAXr88VaB0ZMIiinzpK2hWDojUyP0UtQGJJHPX_M6hEpQGytNgdI-pChgrCG6sYmaYyit0qzIFaRJpqn0XYhNTcfCWaeCl_8C9_uebJ9KOL8cSy1Hqgd2dKtr28HymbZE1G7T0uCsRw55TO6G6Q7QN-CdGprtyZgsYUvklU3fSZ2PFp1d0u5blaBnV75n8KvYgjuAo_8VxJPn6RgNfsLqvoMgQ7cmekiHRHsnlj8FPLPwIvwFbaqJvRSm-KQkfR5LQEIeG1nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlEJExQPY8SEEAkLVeCZg1xHU0VfVw5DiyP4UO7CLY88izxMmi9n4s4gF3e1tB_gDQyF90Ho-sugYgUD_IM76cnM5xd8P203PdtslasP1xX-OX9hTB1p_qd3Zgu-LbIFly07BoHFryCvJeZ7ru1IwMUvAZIYRS-m7tNYK5Sv0jlxWwFcQ2_biiZbpFjqpgpIBjR_LiqKMdsCsRGt_o7SMhupcBbJIDbFn5KrJPezONZGwGxCdyW9tewOYY-2WGCmqT7v2FIFLQ1wovOreTZQWDusfyWKzS2yZveilJ4dCfWARpeotzUwv05wCkIV7EVEJsdKCE7cFuOyGg3j4i5ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=jDvKGaUDDRAMyT-i3bB0qiIFl48Pbofv2zDSD7ImuR420dH66qiVTIBPKljRuH039pp-_LJo7MOmzi4KAwffTcBzOpHy8v-x1XO_rtb7m4QVRLv8nnXZth4n6VVrDcWF05oqHu8xNvXQLuoJwZFjQx918nZ1ryx8nKsryyv9S3gsqUSythpTcdMFEXpBtHi-Axq6M6YjncYI9bujLNY0CbRHyMMFLm0mp83FgOwMW47viN9E3lfAGXDnm4SPQaQfEXxqjcKwgNykFQ6Es9Gvxs0Q7CzTEtb-rp4k-ExBBxF9xpAIku2gr54CngkQRCbYsO3vOIAykl5IJMWiZSsspA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=jDvKGaUDDRAMyT-i3bB0qiIFl48Pbofv2zDSD7ImuR420dH66qiVTIBPKljRuH039pp-_LJo7MOmzi4KAwffTcBzOpHy8v-x1XO_rtb7m4QVRLv8nnXZth4n6VVrDcWF05oqHu8xNvXQLuoJwZFjQx918nZ1ryx8nKsryyv9S3gsqUSythpTcdMFEXpBtHi-Axq6M6YjncYI9bujLNY0CbRHyMMFLm0mp83FgOwMW47viN9E3lfAGXDnm4SPQaQfEXxqjcKwgNykFQ6Es9Gvxs0Q7CzTEtb-rp4k-ExBBxF9xpAIku2gr54CngkQRCbYsO3vOIAykl5IJMWiZSsspA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAN7-mz-ZHNUhWPvizZBEJeYf1ieLq-atVzOfX4RHp2rPwTmIDSPPmbxSxDF3xlR9T68IcX79LEBXd2bOIOal8dYBLebitYUbEJHdxz_Vas89tgpd0Ck38OJTA6kjL2O51BrI6X6RSOnn-fe5G3IWRF10cRh3CmQKyDCRxKQFAaZMBBzcsVgcXlyeEAsUu7XzN1_ALojBTwNYQz73LCmNdVkYuFQ0wPQJxz1iKJmu-aH3LulgCYWxr3yPJPfpDAzhyjIi-YHkDYXUjmXwygSmRc0ZIsrzkiXtJ9_BMvXp__Z9I-gtfqt9n4rKH-lcXrTLmJeeDy-MPPG4qWcv58hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLfWNDOYzWu7ijCi6TyT2MIuNoGt5CkRMUVEfX_N0BfmOf4UiGnMk1WGwQ7vXy8uhmGtuVUD4aZQ3-OaA1OwcacrRaoIdwwy8VpGD2dXFue4mb4s_6QPgEZbFFvAqJ8AhgSagtWZORZz2Zr53hkfXZmcVX8PO_RJS_ye2-KSvp5jtNCgZsz86UaJgR-1GGA-Ub6IQ7yQ1qoHIqJQ1jsfd6YSrS5eIWuTP-pXfKysRuUC9vl12keVRGXL0OBOLrVBZvsMTrznW3PLw-MMznWZjvgARATnbLZoguQKfjpzcisTxdFprctISDQdir7JKyWdOcbKpivnn220jqY9XzaB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23404">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Vgr99u2E-t3Um9JP9H8w7qZBSIM-THWeP7B9GyMoZ4q89FO3gqCKKD_jnvOvGzjy5QTs0aHl00Ijv9Aw4YdR2mFcnFDQW0U4sQ7JqhHp4VAGEsmM5dSe8cjsn3qIIaNcj5X9JpzTiaiPDDr_-9wfUf-N2F2ue0wdr68LOM4XM-ebxrmf2CxcfLQkZOqwTNRb8Zlh3-Ke5ZQB6Q0C3IYPYn8BT4D7rMmXc96rblgOX1c7N45d0MZrmYUWCO5LrGyUfn5F12P-1ngjrLnlqL1kbCKteTFw6anUPrxbuSuBpi_DYK70VYzVcTum6uyurL1eo1T1PraPNqM0c57qhctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
توم‌میخوای‌ازمسابقات جام جهانی فوتبال پول دربیاری
؟
🥇
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش بینی جام‌جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون e23:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/23404" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-IDtR9uvLoeKJmJl8ME1k22-uatKM_kI5aNHCnzR9OexYkDwgUIAbr5eNdhNP84faB2AkSHaitwm46J6IalWN9z8ajaISNYChPqjGdbJenNUY5h7QW5wqlp__VTyuBlUKWVaj6WBT10KDBP4toxLzSNUgw4UD_zj3WL9IYRCTqt0JiLfPVtY24UNv9HW4vGVwiUp8U-ph5NgECicYhTT01RZqWq8TdEUOACXd-LQJvOQ5yxoRzg51fLGfGr60aRSu7cHipkBLqDpBmZNwi6bosZ0qRqBfVH6mwCFS04Bes-6-YcOi4LIIClRXol8KOmjkmkoS8WovfkdGeXjtd9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=W81eI3_ZThzgqDvlQRbfSrmsK1zTtk11weSwIxxQudwn2O0DgZorzn1XcM7tdO7phZJ_Bzfkdhlgaf8tJwdD7ulpqU0A218bK10CkJOD9UwalCiZADEwg8MiRmC6C4MQLZlkU_xhSDlrhB_NJ9EhkQVLQRQU3K3Sro_Sx-F6X5-KctHDeS9cyXLQwxeo44S1UoYyPmf8KbNoV42g4g6pN6Ku32beBPgNAS8hIbFF4Pl0M352c0vPzh_E-uAJtLXSuHxiCwtYYurjb4Fplww1ov3wbKr3YHbUFNUIx9izmb47WiDgFma1bb_BrB2nnnS3r5i5JP7mhN59zcHlGBm4eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=W81eI3_ZThzgqDvlQRbfSrmsK1zTtk11weSwIxxQudwn2O0DgZorzn1XcM7tdO7phZJ_Bzfkdhlgaf8tJwdD7ulpqU0A218bK10CkJOD9UwalCiZADEwg8MiRmC6C4MQLZlkU_xhSDlrhB_NJ9EhkQVLQRQU3K3Sro_Sx-F6X5-KctHDeS9cyXLQwxeo44S1UoYyPmf8KbNoV42g4g6pN6Ku32beBPgNAS8hIbFF4Pl0M352c0vPzh_E-uAJtLXSuHxiCwtYYurjb4Fplww1ov3wbKr3YHbUFNUIx9izmb47WiDgFma1bb_BrB2nnnS3r5i5JP7mhN59zcHlGBm4eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evfKd2dGfBMrmzK0ZXmLFFF6Wg5dVOvwbo4emuteJjdYb9y5EfBCOpq_9npxHZpPcDmmx17Q7R3Tp_PzDvaQtWnYxBVGEvdGcVcWL6ikqoANCNdS9XY6no7nJYRjR_d6C0Ts6YhWxit9B8GXWttlqtd1biXNmcjKnkgiQiPx3CLxJ8DtAnEGxxQN5pw2SUw4H4GG0c529LK8d4vmc9ZP3spTB9Qvx2rP0ZGKJqnmjcMigkxr0m06AYIDo08PfjnmGC2U49WnKcNNA69SegdVGImODzdR4gmoHD4faCils8xIttkJVW9SSUGtRPWwQMpsjrLDHbaVfb_hmPkq3VwvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=o-aAS8yLefRS0TTuoeqC6H1UCof5wO5Xr4fZMxIlzGzJK9xlIH1JLcjdzQuFs7_6jjnbAB6vHEnDbbHbOKFzKX724jyoZj5QC_Ad-34WmWxYaLAK6C6RP5x4CTf2ZWppcInvpf84wCsPVQutUen21K9knSiYbfTdCVwDllo_ScbS6Ow-oz1S7vUtSf2C9GNVQsrgboEwFSsYHZJnltbahqc0AJEHIZ7kwF1QYJSZz_fSwL7tMKf5UuIYUL7VxCz1VkA5M-bpMRRqUK0PKpqmeVhNkRvN9NBuZptAoPTMZw-JzcPNF-UaneBJxesloPAvl-3Org8FBtR5d6DZXm5u3Ch2r4C0QoSNzFzqGYwHXjcFETzsK_3ZwbGe4fmx8v-_uhmw5wQsvbfuTE5yTn4dxxLN1IG9oG9aS75HD-uh0bTx4dljMM3Il7ovMyzrFy9ow3Iql_9MPADX0p903wGTv7o_3Y5GvttKKJrYue6_rScdYbJoc_JN0FW3Y6_Zr4nPCZqvCLOMar6Vazu90ugD8DsYjOti38qA3EKLjJ-VFAGYmRrYXXtn6Mvz4PGPDNAMIzV1F3q4IavEZPm8BzRRasjnkJEDZSEBCXw783UMc3im1ntl4rAP2lUTFroUgsQ9ZIjioI_BGAfgpxhV9v7yEtGrfSD0AmD2XVBF_D2qNPc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=o-aAS8yLefRS0TTuoeqC6H1UCof5wO5Xr4fZMxIlzGzJK9xlIH1JLcjdzQuFs7_6jjnbAB6vHEnDbbHbOKFzKX724jyoZj5QC_Ad-34WmWxYaLAK6C6RP5x4CTf2ZWppcInvpf84wCsPVQutUen21K9knSiYbfTdCVwDllo_ScbS6Ow-oz1S7vUtSf2C9GNVQsrgboEwFSsYHZJnltbahqc0AJEHIZ7kwF1QYJSZz_fSwL7tMKf5UuIYUL7VxCz1VkA5M-bpMRRqUK0PKpqmeVhNkRvN9NBuZptAoPTMZw-JzcPNF-UaneBJxesloPAvl-3Org8FBtR5d6DZXm5u3Ch2r4C0QoSNzFzqGYwHXjcFETzsK_3ZwbGe4fmx8v-_uhmw5wQsvbfuTE5yTn4dxxLN1IG9oG9aS75HD-uh0bTx4dljMM3Il7ovMyzrFy9ow3Iql_9MPADX0p903wGTv7o_3Y5GvttKKJrYue6_rScdYbJoc_JN0FW3Y6_Zr4nPCZqvCLOMar6Vazu90ugD8DsYjOti38qA3EKLjJ-VFAGYmRrYXXtn6Mvz4PGPDNAMIzV1F3q4IavEZPm8BzRRasjnkJEDZSEBCXw783UMc3im1ntl4rAP2lUTFroUgsQ9ZIjioI_BGAfgpxhV9v7yEtGrfSD0AmD2XVBF_D2qNPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=tikkuf5VS0yMkKhlFI2fcRQldXIERGJxf529k0mv00Eui4YVLRpkfEQCrvRWmsgDzdvLXv1iLzYdRi1IrL2SauXqh9FE6dNV1_MM4sYDaEUPuMtzCu0oPY_1i9N9QyMN63Vdmmwf9ymPpBevAp5jNNvv3Ew2vQpUgTLNE4kST3vqoDugSW1rHoRIcKXMHZZtLhgGK-yTNujwRDaofw-Wt5q7sOgT1QCOKkOX9nskdGkBG3iU9hEVSZIizyXEBoQZPKt6hFGDV4eAxRL6T9O3m2K-nt8HjDwnaz3fGb0xLNdxB9KDg5Nd1iC274InTIrE8-zNt6jD7SQYudXi3MMxVbMCUQOg2x0ICZK_8ug55Z71V3w9dVMAgjRy-s3loEBy0QW3R-GuJi4APPuR6-2Ar543Vq5tAytWSF1b8gV-IFo1LQxkYSfAxGk5qsf4ZLNruXv2_fvz0HTy5LsMDaqt8IKvGHAG6j70-dQ746bQeIb9x8cFVUhVxhHeqwAoAZ6FOdzNlx20N34gWfj4HFCsbik5hKGlL0RBiNBAWrCk2iI8Wo_6AtjZT8HsLGt5nQHruaXLVROYI1xsGIdRVOQd0p-9_0lrBsus93FuKiiiJQCUJffl28c0L24nhStb-Mz3WXJolXoM9m1KSO4dqSBpyXcTcAdOYPRjzDOI2Cf_Aao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=tikkuf5VS0yMkKhlFI2fcRQldXIERGJxf529k0mv00Eui4YVLRpkfEQCrvRWmsgDzdvLXv1iLzYdRi1IrL2SauXqh9FE6dNV1_MM4sYDaEUPuMtzCu0oPY_1i9N9QyMN63Vdmmwf9ymPpBevAp5jNNvv3Ew2vQpUgTLNE4kST3vqoDugSW1rHoRIcKXMHZZtLhgGK-yTNujwRDaofw-Wt5q7sOgT1QCOKkOX9nskdGkBG3iU9hEVSZIizyXEBoQZPKt6hFGDV4eAxRL6T9O3m2K-nt8HjDwnaz3fGb0xLNdxB9KDg5Nd1iC274InTIrE8-zNt6jD7SQYudXi3MMxVbMCUQOg2x0ICZK_8ug55Z71V3w9dVMAgjRy-s3loEBy0QW3R-GuJi4APPuR6-2Ar543Vq5tAytWSF1b8gV-IFo1LQxkYSfAxGk5qsf4ZLNruXv2_fvz0HTy5LsMDaqt8IKvGHAG6j70-dQ746bQeIb9x8cFVUhVxhHeqwAoAZ6FOdzNlx20N34gWfj4HFCsbik5hKGlL0RBiNBAWrCk2iI8Wo_6AtjZT8HsLGt5nQHruaXLVROYI1xsGIdRVOQd0p-9_0lrBsus93FuKiiiJQCUJffl28c0L24nhStb-Mz3WXJolXoM9m1KSO4dqSBpyXcTcAdOYPRjzDOI2Cf_Aao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF1x7gzpO4kemMvKDlpxpcNmP35E1UKJBoJmZCNM0oLSk6woB1URRW4l-p4UQ7GxaRQHvx_UrQu5Xh_1c-bMfTU3rzB2gCm37nWDCHTFhijM5HlBowPmVTey4SL12etWopVPkuSDuki3Nc2xY_bI1q6fUxulgt_Vrc34IWIXs65J-8G8EAw1mL_LgFU7vvJC5og2lmOd5tc93xhjg3kV2mOYS4SazHRKNndXw0fPg6IRoc2KN-mTK8EfO6yRANsTB5T1jSHDDCys2osPnPSd6jU1Bmls0-T9bH-qWC0wOGqtwJTUrdgiEb3fzWKORNCNEut8uuG8A1gmCsJhqoqWoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpPzHsXvglIOsLO2a9WdVX-_MeRRr-i5ZaAZn-dU-jHKQP1T15mgbCSyPjP6SZy56KT4PrSMcxnp7OtBp-E_79KWci3ThM5Dy8NZZeaHmN0_hsXAU9I_0AeGQSE-dQK4JEmR-QgPcgl1rEbYP6XFLMpXgH3Qyy5FWh315GPqTVeKtuZ1_cbJo5d4p9vol2_AgIy4DW6SRsgSkKo4wDsQzZd-ug6p--GBlNWS7E6XnUX6oYlRbR6ewd6VKPO3ALl7puOi5nz4y0P8y0LYG90jW8LnzC09wGOhvNrShLf65QlxzNNzMuLlUIcRsqtqUdF9KfV6l1SgmOHNujmNJZiTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHq40FHuC-KuWeCKlO9t_oZ6bLoEpJVmNCM74Z5nAxToLh776RVQEmpiFupUcrugO2ppL7TQ9RCcQL3L1dIzaE7O2AMa3-NnC31vAlHI7pDxJNmKKZF8m3w755B4obyp3eAGWShIlSeRD4cqZadzVgobBj0V6ammy2Qs5LAxYgOwQ0hdEjAlV_lMkPizyiypz1F_HKOSN0iNjOCjLYE1UmTC_RWLdZv5_7xf9EbegvA4lrpvd6x5OSlF_KACWIEUUNVaHXiWQdUQe4wjRSMKn-eO9D8QhUiioqIG1CdfUg93mVp3caYI1RsUFuQn3y7yKEM1vRIGY5s5h_Ist6l8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CznaUJcx_ezXDLf_PhgDBJCZkyP_MmvYtFwR2HQDHBRX3zZ2n7lIlyvdEkqYYGncLCTwXn21bamEsn3-GaHtvkTun6Dl0L15QLjgkoCzgV8zGmIIFK2AgtKGi6ML9_4Kxsc-n9oCftE83UWldG60UL2jnxcFOsHechL-9QbU08cbfwalFM2AYzX-rHRToytw4hziAXVe38CvkE7Agek2Cb0C1bhFZZB2gwNDEM8Ia_S-RgeCGQSoJlqzTBB-o-jUqjWc5hP3Dt2DJOKU-LHDsm-V-yd1GWx7H9BA6TOLCFQyELMc7bHsWA1GDchYoXizrQYJlmhq0AQKMkKqqzwUtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=YHE-4ra-deD6mSHEJxqv5K6nvBfShQGgSSOdlkDg9gyoXSePTMZDQDnTzGPw77SPhvFcTMon8EnkNwdXsTLAe7tuyMFqKw7HD0cUp0J7u5wBIFrFi5OjnLg0NCyvciCcsnLSC4v-yr_Lk4BZD__HddTGkvdyCI7aFCvvCW2mO38TSqu2rG227CaYp4wVk0u8wwPit5nYtnrQHYYJFtdT14X7ymMqQaVsmHENdacmSUQ6o5mvQfJlGXOrj9Fir4EZVKRnMiicx6bxi7L4pj3aPf9UDf9iNuz2gYUeqVO7geZM7zL24R-hderOwzmiX5lJ0YvRxKhFUD_srKEIanGZ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=YHE-4ra-deD6mSHEJxqv5K6nvBfShQGgSSOdlkDg9gyoXSePTMZDQDnTzGPw77SPhvFcTMon8EnkNwdXsTLAe7tuyMFqKw7HD0cUp0J7u5wBIFrFi5OjnLg0NCyvciCcsnLSC4v-yr_Lk4BZD__HddTGkvdyCI7aFCvvCW2mO38TSqu2rG227CaYp4wVk0u8wwPit5nYtnrQHYYJFtdT14X7ymMqQaVsmHENdacmSUQ6o5mvQfJlGXOrj9Fir4EZVKRnMiicx6bxi7L4pj3aPf9UDf9iNuz2gYUeqVO7geZM7zL24R-hderOwzmiX5lJ0YvRxKhFUD_srKEIanGZ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roTi8GiT3mIWhCH2chGWiH9T8AHioj8nWKbYmy1TPybaxW-CdySNcDjw0gZa5-3JhEI7AdRgN6FuKnK2Ugjev3d4felVTrpATIH3XWrB2B6f6begyl7-6LN4ijxa9N2zETG8MxWliUerVgrzvixOFHMtMs5v7yjXirVo7Y0e3CtKVWS_ksZQfDCoF_HHHPWUwtbT8n_KrT9FWDUNzTLvm9HaJ39QwGjqA7CnzYiX23L3r48GmwgsZTRwc-c-3780XeKQdOUfpjPtJWewlgrtBp-mOFgEN87td-IRR4VogvWA3lwewQPjDt1pFJvY-IyOpO26ph4nuwguoRoOiQyraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAq3bdhOu_B4_gAzUeYqZdMUpH3zlZMNNCVocODozLxSf0OR7ruGRS4GDq9Bi9YW5BpMiXT9QF9UWIcSl_9-3ma8LDPHqJnQsNpirr4lXgutkOHrbnmc6MDWrT6Xqh4fKQukc0G24imh2OVsBeErxRIwvAnDhtyb1Gg7_YzFA3PEYk9zmsd6l07j-opTdFeiAgT05SESVZoQYmaIbFRWI9u8JGprwYdGxLdn86XVoFc0AnlC9H52oFqeekFd0PekWum_6gnkxH8yesBK-cQU2lDnA2YVZ7B3fZGw9y0RZG2-VUwlE00lcHykRid_nTpZY5IzzZ-DjPf8zVbCDRApdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZmLIGMUvqHZeQWCY68wvbb3z1mzssKXsva136_B4bIzP-7HMlT4EZg_8bY2bIw5RG1iZPjUpGXofbZjSni3Gj9M4ZRIM1oK50olIHvN7E3JfCxtjI-lWquGbVQtlWXNyHupoxO-DBozF3Pf22G9tk-8CFx_sAhlhZri1UCOOSWfHLu0K00SarTwz57Fi7isWaIWgJH0x9wiCBZZ3WLHQd2o9rjfOyqi4MPKBqW16BiM604eHIKV-cFfKak1SUHMMbzFmyl4-Sbs0NGic5xJaGuMsEk3Q9gLRYmewte4RGhhsQ1j1zpNSOAhCKkiX70vkpUELYTPopb5VM1uWWMNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=qk9i7kP49dnXsYqcfwY3xTcXpFiHfXCUUyK65B7TA2FWc68KihL_J_Fzvv5Q9olZjHWX7PqWbA21z9ZLsQc9ykKd7GUcvk14JOC2S7WI1TqvIxxZ3pDVZXI0cnk4N5qzYQDdG08dmY9nMlB3GJVkiV1RX_-Qvn7YuLQ7UV-MGhURS1H30QcdJaEUtyjFUXOB0vJIeF-k98CWoqZnMHtCV4zsTXEzOobtIeOKX_4kWUnju07VdETDtPywDQTen5iPT9LuCtrpOspEN8a7vjd-gkLjSUy3JKpEHhsv1VSZs8IdQODPjrhVA1N_umlkzLZrYkAL2sJWXq16zkeGXBtnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=qk9i7kP49dnXsYqcfwY3xTcXpFiHfXCUUyK65B7TA2FWc68KihL_J_Fzvv5Q9olZjHWX7PqWbA21z9ZLsQc9ykKd7GUcvk14JOC2S7WI1TqvIxxZ3pDVZXI0cnk4N5qzYQDdG08dmY9nMlB3GJVkiV1RX_-Qvn7YuLQ7UV-MGhURS1H30QcdJaEUtyjFUXOB0vJIeF-k98CWoqZnMHtCV4zsTXEzOobtIeOKX_4kWUnju07VdETDtPywDQTen5iPT9LuCtrpOspEN8a7vjd-gkLjSUy3JKpEHhsv1VSZs8IdQODPjrhVA1N_umlkzLZrYkAL2sJWXq16zkeGXBtnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3cqZLqwoD5rZjS3PVu1UF5h36KP1NK4szkIcNBhUJAX6W6Ld8p7tEGWjv9lQ-K5Id42T4ZIsuUnsLGPUPuAPS9BruYLis27yRZPNkjb6hN76XjwOqa6SJc6fbmZs--vx_j1zTetzGICXZuQYtQNMIsx6SrtDClMLe74c8bBTrClUpX99rR9Z02cZjXRwaLANHRuo2-AS-TSBbnPzZkkNSIXzBbnRn2EO0c1FlJG60ninj82JY9O0thlZheqxgk1D6aFOHKgWNpX8TuWfJxPUcaoV4UCHO5E3Vd34-ZAByK2_6wQkGssF2OkVMuLvjgjZazq2BiIfjW57jCbSivLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=kdfDD41hKy93_I7Bz80I6zG8F3UohJVP2VwTrEbiCzfx8bL0J_YO07r31h0lhF8TqraCF3To8G5BIfCY9u7sG6owOg4x93DXmd8dxVeXPVXaDQnffyCR4HpQbG3PwnN6rhc4hRNafgLrC5wxlSkOQG3G_HnN92CVO6UAZqjf_Z7GXLbELZo8kJ_dPaukNFbpZGtM3ziIbKHZW4vpJpTN7bYe0YPr86xDeB2FwCe_cE-u5kT-Y4qaib4raF-jBWykvDgPiapBAw9cES9in0ahkjT0rk5IllxSaCb0WuBE3E-BHvsqzIBx6WZXXhS0p6lT25Aq3ddz-dC-zabByfKlvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=kdfDD41hKy93_I7Bz80I6zG8F3UohJVP2VwTrEbiCzfx8bL0J_YO07r31h0lhF8TqraCF3To8G5BIfCY9u7sG6owOg4x93DXmd8dxVeXPVXaDQnffyCR4HpQbG3PwnN6rhc4hRNafgLrC5wxlSkOQG3G_HnN92CVO6UAZqjf_Z7GXLbELZo8kJ_dPaukNFbpZGtM3ziIbKHZW4vpJpTN7bYe0YPr86xDeB2FwCe_cE-u5kT-Y4qaib4raF-jBWykvDgPiapBAw9cES9in0ahkjT0rk5IllxSaCb0WuBE3E-BHvsqzIBx6WZXXhS0p6lT25Aq3ddz-dC-zabByfKlvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQXHo0Pe3EhCWzrVsJHe4tYdFLB4UYciiO4hvLctPfBejaIOzqI5Hsmq4wCxAE77mkeA7pIFztQzNCcKXbXVu87mGeIR1Myt9eSZC_Ew806WO3SXsLAWfAZyN4gnDaCr1YC383hvSamc28_QvHY5nGU3plJl0wP-kzWjWsvC444pg6G2zPbyGNrQNN-08MkXvJdyvwMFvySbAYCgmaaCxf3k2Sx80tSJyQtFoS_zFQfEWpWyyBnlj-e0HTW2oHZU5-BUITjX0-RQ6erZIBD8hFWHW1G-HAhae4apweaMU0vWVNu7sVI1zWb03n0wkwvaskV3jOQvCEwDDs6l5uYbbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX97SgTpD34vqIb5nCn5w-QP5OQ4QwLet71K2PhzbldMkFICS_q8owtivc7CIFrADXZfXh0fWrFoi1DjprCsVHebKjLFPG9WVukwDJGaPekPE7YdQaQ9CefIw5spjK7yFdl1-JhLKLdB2EQ6WE0LbqKdTYLpktaCLNP3TPZjy04I-nLuTp6Tz4bRoJbyImQ9ZDDPDEHQkCQyc2wKNruRO07vjYD38Dx_sBKyYatjs9BXa0E1xFkJ2E809ltKlaLl6-Y-NDGlG9u58HaaULkJTqAMXCb06FFTCKz_5hi4g2HS9HxMRq7N61t9SEGW54wMfzx7pXvLOXjS6m42pIgJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=VlU0FkusqrCs7NB65lqNyxlNIJ3Nv00h0FZFYpzNZ_XE2DW2ArYjRbqpsFM0Gt9nwApae8fP1PYc7wm205cmAfZdHmxyaodAaaSHOfuZ0kIkp_XXf7gT2U7bbHdP8Mn6DiPjMo2wI-e0BNyt2uOhDivr-t9L2eOpkh7swydLYh_qMqCUSJGld0tObjv3GthnwyaMlCt6-CyVD5K6JtYo_T9s_OquX0kASfojC-4aIEjCI3ImI-HXNDGaaNurIzojuTbWkUdwnMhCwkNQ3dq0dXSFS2NGq_y2kF21VAvsXOvfk-pwEXWxZUPyGMKMvP-HeINmcOWM82vmf-h5m9ifRIohNVVAyGK_Zt8CK3oIzULfxNI7VVWVyNpmkBFVV1xRaYM17JSe7ODOxzmqIabVwoKk869Ng9sjEP1KOM8029DmBtyL0fqZZsc5-528fJS1wpp3krYSnMrK30Ypdn-hNP_GthwL1JYVmZAqpWoQZiSvz6E7wbzOGRYG4NxztZQ-u6e3UY6cV1BwtRF5ZSBJhQFw03wnP-dKiycHxse9m3TwQiEOzq6bqQLrBJFJYTM-EnVW2_P2UADDcS40KamC06D-YdxdtlZ2gsoCtyotjs09VmQTzNsucvAjWuUGBlCblS1cu5pmsU0MBCbXBTUxFZDPF9RNABsIjZI4lOOzAk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=VlU0FkusqrCs7NB65lqNyxlNIJ3Nv00h0FZFYpzNZ_XE2DW2ArYjRbqpsFM0Gt9nwApae8fP1PYc7wm205cmAfZdHmxyaodAaaSHOfuZ0kIkp_XXf7gT2U7bbHdP8Mn6DiPjMo2wI-e0BNyt2uOhDivr-t9L2eOpkh7swydLYh_qMqCUSJGld0tObjv3GthnwyaMlCt6-CyVD5K6JtYo_T9s_OquX0kASfojC-4aIEjCI3ImI-HXNDGaaNurIzojuTbWkUdwnMhCwkNQ3dq0dXSFS2NGq_y2kF21VAvsXOvfk-pwEXWxZUPyGMKMvP-HeINmcOWM82vmf-h5m9ifRIohNVVAyGK_Zt8CK3oIzULfxNI7VVWVyNpmkBFVV1xRaYM17JSe7ODOxzmqIabVwoKk869Ng9sjEP1KOM8029DmBtyL0fqZZsc5-528fJS1wpp3krYSnMrK30Ypdn-hNP_GthwL1JYVmZAqpWoQZiSvz6E7wbzOGRYG4NxztZQ-u6e3UY6cV1BwtRF5ZSBJhQFw03wnP-dKiycHxse9m3TwQiEOzq6bqQLrBJFJYTM-EnVW2_P2UADDcS40KamC06D-YdxdtlZ2gsoCtyotjs09VmQTzNsucvAjWuUGBlCblS1cu5pmsU0MBCbXBTUxFZDPF9RNABsIjZI4lOOzAk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23380">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiKgf0nbQpPIzz7m7TnO_zfhYiMCEmtNco9LWV10EK5bA99xmpC5rkTIib_pevGbhPPaFCZ0Y65taVSI0HUD23h_ophaZpj2qJ9_F1-hHSn5ATpJhCbIWXp5HqBtyJJyrf8xwl9FuKxjbDyeIkDDFe3dVfPQlKsgOlmAHaPwqT4sRWNwLr39Bi-DnDuAOoRWg0lUdvy8NvCvekaisS1EoUe4F1VHpl4zXe8qBTbknPmQfjyZWp2RDUBXABS7UFLoEuqpcGmDqhZXGmmS_n1_OXH-WUMnzsrzXfPU-LT-mVKULfl7jHXKt_c-lPkLt2dRLqNaiQcJNa0jEUcVMQnpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیازجمع‌کنید و برای سهمی از جایزه بزرگ ۲.۵ میلیارد تومانی رقابت کنید
😍
🏆
هر پیش‌بینی شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود :
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23380" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n9Ch3YjKdLM382XOzgWN5341kypVoBIGwrzHT0MOOu0DRPjdXxWd9LeQ1a5xQPBP7zEkYOp-tTIQnIBWTgR7O9T1ExMuq6NATRclgw44L3mP8szNzEAaZP5cLaz8WFO5c5mFx4fSwCswX5-VckYQXeBVickHir2WqQ8TKC9qhDtbpDF-hJjQ2Tf9AiU098JHj5A0jgQLqKSzm7AjUWaa6MXmxejJGHl1s6K23oCQ6_4bzrQWGRXzbx_3GgPV9992FT91rkBoaeXBtV3TnO5RqAv93fDFbM6eIl61AuPGOGKTke-ETyIONALS7tVQKFVouFHm2LUdSRViEhbRWvwoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NUtfMzQN8hzCDafmceMnFYiOuOomtSBIBGh5865G8AL4dfI0r1LpA7xTjbEB1XuhQ5DwG-L0mVsDv-swRDM2KsanJmNzy-u8aHO_u3DjUt712u116ovuoOYCkEY7L7MRzXKP2pD9iODN3SDt7Y82dgQQB3TzqEtUXGPiMPbnRRuU7G80CnrUjMMIrUTuAjdjyL7gMMjJPP13lTvoWL2YCwcGVEjCJ_ea2srA4fBkdThfPF4ZErYW6NvXG8RF9NdkliB7Y2flaW-RIZEdr6GtudXxhSnubjfMBqCamek5vHuH65DfIMuVbzPFXWS-qAHIxn3Gs4szoPl9FlTX7-hPdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=mrnYkWm2fZFDqF2MbvKTcFsg6qJX3Akvxw5znWNvI9eZhHMU2WU9eYp0OnlC6t48oJZoPs_bl9aAMDfpwGQWWTKkAq06svR1c6VqFFy66Vp7vXJLV8SMa8oQsEpZOjVQYzgdGKcZThswjBILZdDfPcgr-x1avUTpJ-6dFI-P4XJ6zZa-8fVeIV4xE20noiEoayL-FEsUZSTrbjMPbnRbbcOkZwdelXliIKpmxwFFCbJJX0IngarfYf-3JTAYcBbvubH0cNIcX0daNusqYQ3ld1M7D0Th2srAK9U1vmV6nuZM2Hl1AK0KHeGl76wIU-WAp0xmbFIEzv5pT7TNrW4_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=mrnYkWm2fZFDqF2MbvKTcFsg6qJX3Akvxw5znWNvI9eZhHMU2WU9eYp0OnlC6t48oJZoPs_bl9aAMDfpwGQWWTKkAq06svR1c6VqFFy66Vp7vXJLV8SMa8oQsEpZOjVQYzgdGKcZThswjBILZdDfPcgr-x1avUTpJ-6dFI-P4XJ6zZa-8fVeIV4xE20noiEoayL-FEsUZSTrbjMPbnRbbcOkZwdelXliIKpmxwFFCbJJX0IngarfYf-3JTAYcBbvubH0cNIcX0daNusqYQ3ld1M7D0Th2srAK9U1vmV6nuZM2Hl1AK0KHeGl76wIU-WAp0xmbFIEzv5pT7TNrW4_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=Hvv52A-jjEw3BTKG-gKinmS39DVyqiGINDqm8_c0mX-zK_n5sFJ68Ogs6gkbGGjJnR5MMeO9SFs9ndLB8N38aNoNQLeLcwHaXbV_tVIdkhFIPTELuMW2AsKH8L-4emxUrUC2XYMrZu-xN5udiHm-FD-M4HtZgyjkxO35oMZUtUtqdaUI9I_IBCvg8CI4UJIGi6oyCwVAj86jHyEDB-BB6hJvgEWougrtVfb5Z83VIRRJsHJmOTOYAq3-ZaIVgywYoKeV1pURW23hPzZWGL4pjiG_Tt4MjEFV8ExkUP7_pKELR7t_2P5VyeRrUDI1LDhdeG0NUF53kNiqU8u68ihhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=Hvv52A-jjEw3BTKG-gKinmS39DVyqiGINDqm8_c0mX-zK_n5sFJ68Ogs6gkbGGjJnR5MMeO9SFs9ndLB8N38aNoNQLeLcwHaXbV_tVIdkhFIPTELuMW2AsKH8L-4emxUrUC2XYMrZu-xN5udiHm-FD-M4HtZgyjkxO35oMZUtUtqdaUI9I_IBCvg8CI4UJIGi6oyCwVAj86jHyEDB-BB6hJvgEWougrtVfb5Z83VIRRJsHJmOTOYAq3-ZaIVgywYoKeV1pURW23hPzZWGL4pjiG_Tt4MjEFV8ExkUP7_pKELR7t_2P5VyeRrUDI1LDhdeG0NUF53kNiqU8u68ihhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=jdYGr4xU_2oBYc0m2QI6fOdTOg7-5F8UrvAmsrFsd_uUzrXcm30h4ENX1cr7BZ9n1z9-X2aaHfN1ELAOglNj_x6sRub7AMd1UB6BHlWAQ8-3rn3MgcP7NJZfi8N5YmlIPge0RZKhglh9hwFezhJfC_pRY7Uu9RQoM9vQYMFGJ0pGng4VUXj5d6MgeRvlJlZDoc4Umlz3aIRpufb3rrQcd6wMa6XBve0Vd7YiPDvzcyelqVs0jyCGdPCwk0dH-mp8Jsf8qGArTgCGHqWLZ_k7imkv8dOrwnrIyj5kU8bBCRw9SlnPOiyiPeJn2mFw9NdDnxor51lPK4A5NLNw1rPj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=jdYGr4xU_2oBYc0m2QI6fOdTOg7-5F8UrvAmsrFsd_uUzrXcm30h4ENX1cr7BZ9n1z9-X2aaHfN1ELAOglNj_x6sRub7AMd1UB6BHlWAQ8-3rn3MgcP7NJZfi8N5YmlIPge0RZKhglh9hwFezhJfC_pRY7Uu9RQoM9vQYMFGJ0pGng4VUXj5d6MgeRvlJlZDoc4Umlz3aIRpufb3rrQcd6wMa6XBve0Vd7YiPDvzcyelqVs0jyCGdPCwk0dH-mp8Jsf8qGArTgCGHqWLZ_k7imkv8dOrwnrIyj5kU8bBCRw9SlnPOiyiPeJn2mFw9NdDnxor51lPK4A5NLNw1rPj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=oH04QkpUIccJn9f2Y3TitqTj-apYVz7TavjZIMWF4RbFXfRM-tyqRoC2bakj874t8FJEiLTsbTgBgpIRPI1X21yBFf8JUkV3sDEqgJ7Y6Ls4d_J9M8SYr5wTsb55Q5BkpDBlCWho-E_K3dBHcdFfeje-_WyjJfT3EA03G9ciJQLTFpv04w8tJ9pSTtFXz7fWXjoOg2lauHl5LK1NNZKkdSulTjrhlnT6tict9w5Hrk8XvpWLvKYleMK_C5GTiSNPbyAUMTrgmPwNzC2A611k7yykUlSzh31Vdla_H_0eFNjXq7tcPvfaX4npBFsg1iYS3WnQhg6TiFnYqygtw0aAfQNFMcPoqihMkoEZWlNxd4IuQa_UgRAGVwquSAVZo2TtrvO1Kr-3HIDMxr2ZR9CXVvwSFsJGwqMgURy_-lSUiJJfskZ4f13lm1sKSVy9AKqKqCotAkGP7Gs5kmG9moC_Bu_uFFaxlxfTQxxgaJbRnROoHRKgeT17q-OfDcP_KG0R5VPgtYoIlsI8E3hwf2RrAmuJUjfC12yzy7tnRyq8Unajl8nI3YiZ_Txzk3lZDMxogKID7fwNHfMsP6IsR-mzo7yQXo28xAtsbCDcfirnsioZYqRQpqMfndGpIWp0VlAEkg_0aWxsG1aH58bZD7OMX9qeXF3WHfyh06rf-H_Iz6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=oH04QkpUIccJn9f2Y3TitqTj-apYVz7TavjZIMWF4RbFXfRM-tyqRoC2bakj874t8FJEiLTsbTgBgpIRPI1X21yBFf8JUkV3sDEqgJ7Y6Ls4d_J9M8SYr5wTsb55Q5BkpDBlCWho-E_K3dBHcdFfeje-_WyjJfT3EA03G9ciJQLTFpv04w8tJ9pSTtFXz7fWXjoOg2lauHl5LK1NNZKkdSulTjrhlnT6tict9w5Hrk8XvpWLvKYleMK_C5GTiSNPbyAUMTrgmPwNzC2A611k7yykUlSzh31Vdla_H_0eFNjXq7tcPvfaX4npBFsg1iYS3WnQhg6TiFnYqygtw0aAfQNFMcPoqihMkoEZWlNxd4IuQa_UgRAGVwquSAVZo2TtrvO1Kr-3HIDMxr2ZR9CXVvwSFsJGwqMgURy_-lSUiJJfskZ4f13lm1sKSVy9AKqKqCotAkGP7Gs5kmG9moC_Bu_uFFaxlxfTQxxgaJbRnROoHRKgeT17q-OfDcP_KG0R5VPgtYoIlsI8E3hwf2RrAmuJUjfC12yzy7tnRyq8Unajl8nI3YiZ_Txzk3lZDMxogKID7fwNHfMsP6IsR-mzo7yQXo28xAtsbCDcfirnsioZYqRQpqMfndGpIWp0VlAEkg_0aWxsG1aH58bZD7OMX9qeXF3WHfyh06rf-H_Iz6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5hhD01Pi-gKDQyZ62ixROmhr-BG4zdqcP__phb7GaqutQwTqNLp1dYPVKE2mDcGGVbaNSk-u5moNvAfihUxloxSR-XMzSLxBztwsQLkcxpv0DUnVOyb9aVUkgu-tbVXtgDHTRm9O9c63l9f1IIBS3zpcWm3YiZ0HKgTXCXWzamDewIvSV3WaaSGnqooT5AOeU6v3EVYHgy7Y6JB2jGDcBZ56930WOIu8ISto1uIh5x8_bhpPh4koKUJXSjrpeyoN_C4f5r0OZs1e3TSks-gcOkkBcOQxuJiKhRaT3enF3z-fBzMMszn3oLY_HjAG-yKJPR_zFxfYuCjwqpy9o1ssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nc46dKayW0M5hUXUliR3FjMeYHO8FSmANx0mF8u17ekzD82Lslv_ymGn-40kmI0pzQukA2PRUEEvbLIwNYXR15uWl9Ave1N-DLoaq8HNT1W2sslP2S_zLB7GzLje4J4ZFcz_lMwu665aa4VSG1oir0S_YllaxHzoiptKt-0C0qj0F0JSUy5A9P2ec9ys5U1KZ94g6oU6ZEd8l9x7sGUgLytYvAurrAcsMXPVobHTMm8o5oYIekU8ccJnd7UcAFWc2zBqI9a8kPXcclWgTtu6kMKwwwVhvAQvAgeM3ZIRP-pmXtw4kvYb6ReZJ20ptoG_HLQzEIyJVZhABFQE5Uje2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx0PQRikBRZJkBx21kW6fCQDff0s7Vyv_Tf4Umyq6lneVEPZW64cxXZKQPxkYhckisU4JBX3t9pV1Eslm9wogajdV7XaXh72eDBH9JHroXWj4Mj4kCYlFyDozOUOIw2R9KApITFvaNYI1S4ehMNK75V_9erirGcl8Ls4GmxknFiWn0lx-3oxjkRDR5ntRE-iBFUB3am5vWW-38hw0sX4OOmY5W11993OdJd2xL4gUs5J8Q4GZPEhaMF-gluQcqxpW_NHr5x1MyJtT-iy6GfWz1uDw0dRHSDYFAp1jHAwOEqSdIr3A0I3SYktMAbS5C4jdFCL2T7Lbr287GIb1_0fUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7B5jE6yQbUI2ZihjZ6Rm-y4lpZeejyhaz98cGHmH_wGt2fuql_WkdQt7cFxBTfuCa2KU6DRUphPwOIOBE8oPJREaeq4o1BULVNbS-x-tPr1cH2JSs78x2e1ZPSq6GclOncGrD7rzldLvkgFBuhtd_S2dUblhwPB6H23s-yXlvDk6QpEz08HrtC9uKJwyyH7b2WjYrCAsoypWRHqP2Qf4I2qrSYKdqSZx-DAh-0nvm_BIXMh4jO6G0daBXP4-_auOkdMV7BDcjtNN1zm7Qp4cWWDAyqivuOp9cdgEuUnNDDY7dwQTbg4fG8ZfnU12ZSflCwf7Lu24h2eklyUtCbunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZqOIqcRUD-haWDkJDM5hzu1oWVpgpsQkya-CuUT5wAqbmS8wOLkoHrmnllr8rsaovw9zG0yyxeEzFLxMHUi5vcVEzP1FjZkoiX_URRuCQ7QdScts-VvFi9WlMYHdqw7-JE2AarY41q72z1zVQwmZ8IWZF6gjfDn1YNpDAjmam-kJrP_lhdK_xvAHZ4ZrsSMHY4G_QO5Z9j8PRlWKCSaTM6T0gQZpCjPiyPWumMUNu49KwOoHzudZzggOajm2S2-2nFi_KSTrlCXIAN8PuhK9rxTUp2aRS7B8E2tpedRHtUBr8sgjQVgZ70SKIWWDQhPObJ34ncU_eBiOfNye-XKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cd-gT5fOkI91QBk8-jP999vlmNLgq_Va8VtXwpa8fg_tEeKiW5j6n00Tg1l91udYTJ-hjnCFS7XFZf6BaUiZwH1e3JFve-PV1ltXBzYxx2_V4rNDs-38ClO68nkdS7fBzDuqo10F3FwuOm_YuTIZynQmLBlY7Ln2ucTh-pNHgG9fwKnceeuKM_jacB8KpXRqzWryDhkj8wwUdi3c8Iyf4SNMRH4IpWi2GjCEUbQWQeWMNnz-AZUEr3pB1bR704X9612l-7R8PB9xyQW5LJcDMibsAHpkr88cThrr8CMm4OjWHS6tiLWjZxjdFrulIZGV3ng5TtooIKJw3hW1q51uvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PexIwOQ-JCN4XkKSeE36Tb_mHXLAfeEqulWD9Cnx5u8NjEaJZIMU4GSWutj9vstOZSboQ_3gO6XL0DtZEH_OEFrrT5upHKiEnf1Seh2PT82UcJigFN3paMxiDaZ1Qr7SnfniBr21xVBZp2xbdUdVPGlXVXxBOZ9UqBONZQI3-yVVmnd-yNM2qc8EbTCjNMvSvF5JZLPiiqPEw2GekcD2wFMSF3sGEHMP0O5vYOQb4WyawX6Z2KdKtoThWQkzMpYFi4xwDkFhrElV3V13m6g2VOtlgXv97IjA4MFvr6LcyuCriUxIZCgZLqy3V2mLum4i22EqKvkocJeCfkrZ4fr2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=syWeTUXSnaiOzAYuSirzLE4nBCb8XUOnYBqsTVGcbaKQku0o9tmHuyhb5-sOdjye1qt2J_qbakEL6tw6t7yIaZqGkNf_7nW9pIuLfx0ut6t3s43i3I4BDHQOOeiAxSi6-tuF765Yf0Xlsyiji5yba4ZTxnMftoyT8_QrU8xzcdp7bVv-1x53TS8DYpTzt-HkDWBd-iECv1vewNm1oktOx_boqvOAWgPmV32mEQJ80EseBopQcU-MaV_dlJ2EV_vLxSzR7gBOuH0EV8FTlUUHx0VCp6TQxvlg-D_259U2Ywp0Bx69zqao2nChfPKRUzJCRPajTBVJsEaOBoYLH8IblA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=syWeTUXSnaiOzAYuSirzLE4nBCb8XUOnYBqsTVGcbaKQku0o9tmHuyhb5-sOdjye1qt2J_qbakEL6tw6t7yIaZqGkNf_7nW9pIuLfx0ut6t3s43i3I4BDHQOOeiAxSi6-tuF765Yf0Xlsyiji5yba4ZTxnMftoyT8_QrU8xzcdp7bVv-1x53TS8DYpTzt-HkDWBd-iECv1vewNm1oktOx_boqvOAWgPmV32mEQJ80EseBopQcU-MaV_dlJ2EV_vLxSzR7gBOuH0EV8FTlUUHx0VCp6TQxvlg-D_259U2Ywp0Bx69zqao2nChfPKRUzJCRPajTBVJsEaOBoYLH8IblA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZS35Ul-0orTX6SRlkgdKHUEwEAW7ByAa6OuoBuTFLm77kcLRa8mf1FARKKJ9QEe9KEPtI4k0NqH-HnZj8CyJidBLZrrG2HvCRH-tNx9fY8By389DGsGqnL79Mi2GWX0BNOjroyov4rHB_sVJPTU4n-KhJYXUku2ByCPOkLexC6GULOqARxlEXV-tQFL-CSBJf_NjsSDgOCmlk0Bd_S0HmtBAGfXryxeVcdZ-5qw8ml563mgukbf8TPHgQDSD21jJJJZeioZvMwwKV1So1IlvEetKZWqxu-dTAf59r-yRO94LY4Yxd5-ubp5sfTiA9rMMjCkJSVeVihEEyX8kP8wtZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOEUXrLExk5pokNIIQe-aykeZ-A8gq43E8-c0Pvr9J0NShiSMeXqEeO3aO6J_gAq6CNZcjGH7SPal4vX0hPAJp2G87uf7n2zUS_FFkNpoiq3hjDswM_N2aKlCmQnghrHSucCfLY43Ez6z3YcNAkV8ixOeH1uy7g-dvQI_DeFnfVuN9dPt22JHb8tONvJ-lfjSYm_4hntZjLQlCD4imn03JpKCAbFwWeQyn3XErFtK-B-_WosazN2ZUaVLS0i7iQ7Agh_2eVBHhwuC2JyDnk8VEEseNrFTNouRRipwZI6GTXJwtWV5QA_tgDbrLaIsI8gbNAm6Df3DgRevG8H-rNuOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ1hVFWcLJQjGoM_IIcQu79gwK1Lo_ZQfd2pBo2xpboKBG7PE8Lt--mf12q4h1fspcrBwEU2on3I1feN3-nlT41aYpPyzMB4zFl-EtFrvmsWYmJrFR5m4kcOdhxqiIOqW5yThQoMiJp77ouIiyl51pzB_qJgwY2YK4HcL7FdwDIvOi58VrP5K74KujXh3kibsRQ1PwPhPPrUlXwCvSsxb2yNSWffwWmYRdC4i2MAhJhArnnVxyKG2damdJ8QnUCF5UVmNlZSZtdKsFZGteAraImUHE58VU4COdDeo73H-kG9tGSwmF4fJ9zlikY_f6BveLrnvJUx4RpwhbgLoSIvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O07v7BJXDAuBj0L1QIME5KSMmQww3o41bkC6IDcAoSrZGZ3kVjqUq7TQ7wUFsjssrZT7bbme0kL-20rFpGLfZhpMa8HfqAUXzbpzEtci9RDfJA6mYZmlt-9tBse3dngaH3TEIdNs-_K7C8F2jVCKK6NQ3A9YlLffSV--eEOiIwSS4mPnB2635KTlCC9VUIAN_vgGlt0n_bClQcQs6pDbel6J5Z8ZAbumS8n4f-Ii8wIx5Vgxv9D_ZmKRaSQ9iQ3wTroJ9turHmQvmbTlQoVWL64t2LY1Uz8Jc0w675uaskxHbSjMLIjtI5QVhmCcSB_II4Sm1KzEn4e3n0cgI0wQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWHD8bG2qRozxyI6Zdz8x2eas5x1CRZ0MLhspspPwuAMVPpBIHMDmYdZbZxF5b0We7U9jNpazYzpbSkeYbjjLagtIpup-4LDb6mN7F-nMuDMBK0st7KZPOmO_9C0gz7z_hOmvKR4LosdYWdftl5VXmxdzB5rHBG1xJrhanhDoq2oStw1fbap9ocF1AboFxzvSdtAWwXMEIOwSD9mzM6oI8Lh0EbhpM3R2Z0m0zn4khhVfb29SprpeZfcMRr3JotViJqFy0iB8QcOe-kD5Y46rCP_R7XOC4EOkigXo-jbTeVqBnK0MVPzRJ9R3uWMe4yqw1lzW3RABAQNY3LnCxAPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pq8TfJqQgTxJGYn2fJBi5VPxXj8sIBy9sNgX1nySjKE8u_DbK5qqt8Kr76a1bClT33nykiLHS5TLA19VQOLg9i8hIc8CaTsgGyS67oHiR342J9gqPJcaLxiNBa7OYVJy_p-A6oF0cEaQpcVTPWYPcASNDPBzJxhXSC1EV-mnWfKqsIsgvtMWZi8XcNu4EgJioqnRXZf9HK18U5Zvx9RMiQy6nY-WyfQO6CocKAuDKzoGl8QtBfmVH5Gm7R3TAKq7ljLaho8VlY5muOJ0BfJnNkt7Zx4uf_A1DPPBMoB68lQCR-7GoY9C40ZU_NeQeCyaXTNaedFCElMcn-XuXSLM6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiWEv8qomOJUag7tM6jwq_YUwq4UjhwxNgePxVpb5-lBt4c_AIzFZAUTfEG97nTr2VHarHmmPoOETLSBQ4VfU5u-o0NOvwYcid1jd5AEo-BITMeQwQ2hBb-OE_yX5vgxPd9Or7yUPsuwDJurPf5EzjG_wbO76NJ2uQoD47rtphi5JZoedu-cHNEJwZGT95xorgWn77ttEljern7OzGYlx_WT1CuinXBxZRlsrYt94g016-ewx57p3QA4X8m4OzEoEzzedLOuMQ-8DX30WcR0DgAHYKlS3ZfgL1bf324v_2Y_wRdK_LOEIMDBa__RFskkTim0vbvDAGu6xYe1R8OW4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0Dz4Gs02A-jU5RqnEtg97YGtup9kwZvJHTBKpbPjuw2OxtHfFMzeC5xztXfsRh_ZEDRkBKKA5Zriec0DC8kczddST4rpKtJRikorzzgm3JWeEMxoYNG7a1TdoqUxsRk6jF4D075ryfTTHqRDG1C50WpDpIovfwaUyAbBo7qd_hRe6Pw0ZQQUFRs-DCkdATikWon1vmGVrZbF_ZzwUo4wGwvMJu9nEtAvySqDLgh40N4Vqcgj7bPm_74wCFwRnG5V-hXZGbFpw74vMV-YvY6qh06lA35DpzjIzxcxOBYauP7lB5pO6gZFI8vsOppIIwYG7GsnleygfhusYC5juotIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGvD1oB7GhnaZmt8cwz7UPuUROdjJhTV9T0sgIh6ceot5OGJg8-Zey7S1wC9WC7GlsFuoE8NZMo7-KzcAg0TdQRy0IezQ_VMOVa-x5m9erDR6HZe9iu9Yt93zAmWC06h5ift71QTpXqqpTdx0tur6PMi9sCN9kF_UFkAqOHAVVqlFa77CDd4fU9NXX7lvX0PVXK53MyGnh6XrXqZY8HYWEmlHIjjrioTowNU2DBuo-OyNjExTxl7lsWHhA-XQ_0aBmtdFa0bh0aA2nVoDSrUgpy65ROSBN6QWp7CceCYsWGzU3MbWDqoyvuS5de9xfzSF-lqB8jZLNgf2Ori2nl0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jw0S5IeeUm5bt2thspeLMwRdora8oU0BsQKNhbI4lOSSPymtPM8MdSKJ-DGockZBaduE_WO_VvoFofEb3EKI47r1SyRIxi-GhYdRtQzGAtQYsLrAGjmmW1yoGy4Igav1_8xUCe53huhl6edt5hqt-xMMCRTM4ZXwQec5vnRrPz1SxT4J3L3tb04lITh2aoSUP2jRafOc_DMQfCCyIZtl5Omh8SLhTF8N58saplxxNk-sXGZLwI_EmBQ3-MWyjBxiGdCU0HGH711LEma2X9-vVc0Hdk1CSJ0p3EJgmjYuZZfNRdV9PdnI3R6ry47gkjMx_Dp_dz37914yACfEbOedZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITWtzeUwJ1Eu4XCWxLqxC8o9OBkmyxbP2On_xy9_USXams0amhboUVOt7lP-ZN_Wlgd-vNOT5UAHFKurIJ57ES7vUG2B3kD1v9kXFnKc3txv8zcSnCS-7nGltqUumeqcRmg7zmPJoIVuWPzYsu33IllaxmwIF-TIFMMz9XFY95KpUg5ncoERJAspv198XiC9YbQa2x9Efw9j_DpmHe49Ztr-E7nAo9zuKStJLrY6k5woa7v0HL3-QC2X1HG5tsogOvACK7pl4zw4Cm8eNDM92GDB_hPfs9CyW2f-BJSvC6DrcYtEmP6EpV_k03TvN28PJBWbOBSqCGhn8red2E_Nsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQfUQA5L3quOC6lPsyExZY-iOjitGfZ-EoSnTZjJr81LChgelUaXzr2hb9Gt_h5UtqxPYIQHV9UMVXUowiQOsjRdd-HsCRUKQpaFitxbHr10gdH76JHK4EJAYbBqJFKsrENF9Y9FDq9gDo4J30s8XyWX4p6zu0XvNdnpacG_AYhruwBcYxzERfDahRTtwXfecVbDsK29eJIkglCxq56epn0dJ2yvQ9AMrdbW0l3rDnThPWM0ZnAxqoB4DsloaWccUSTpX9m2bXoptuvNtEJHBNroc1PIHv4XsKVY-JXtDU-kRS0X8becFGgNf6eHD2dk5zglbrQgCz2BOpDWHdA8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDGSuDdqbRuoLI2nJGoM_fpvDyRAm1dbNDot3murrM8LVpCP4GIGvZnQVGESYgNW-cRRzQYOjWLXRFNeR-6zsh63MBUYnCgtKIeO4agII8DfRR-8cKm51l1GmE-qCoTbO3ugqaPb-lgUrM9gLvvKd2WHHCVcJo177zdMGKUu3j4-akm0jpVm41iTkbYLYMBBz4JBqQem7XJCO7i83EIIaQESsCiTUMcccjls_Ow8JGGi2RQYhph37YCoOyp_3v2QVdJO55zebCckvm5ZYu-CfUpdXsNzETZ_a0XEBn3UeCo_FbXafAf4wbZndnloikhC9Mzn5nDVAmQx767h46jiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FvVBMTzJxRjRKR5arrYc2o1Uc21aXlMG7Eb5Qhg1AtIXooUHfIIRFJc3XyP6gYZ8k1ntZzjE42dmN8tipMpuYVSLwY29IBAUApAr-ZzLBz2VwldyhqPzRSkYx8nsaXe0OnYtGc0F2ypOwuWo5Gptsnk8aoInwOexUdLUUamogvYSPCvQV9hh7p8CaOo7Sp7f0kWzqr5WPK4_F_CQGo1v9tXLmJ5AZW8gKhtorzUU3cyDeHC5oW40lYZg1N_pGdYygdSFv1WdCbJ43YrIMGjRhKwu5XY1RB5ZXoL8TT8BzU3BfDdyDg4uHA8iyMQpMa_c_jMKxh5ItvVJSmZo8jARTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
گزارشگر اختصاصی بازی‌های تیم ملی مصر در رقابت های‌جام‌جهانی 2026 ایشون هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23350" target="_blank">📅 14:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8-fAbIwcJDZv3qCdWq7r3rWxxz_athz4xIRW5oGS2zKMsF7byOapaUhuy9BIGB3lgtSbDKR_ODsanwZTDqqBimEzUqdqKUWEl-MMw49xcuNfJl6wS_68X8MqHxPGCgm-sx3cOHvwM34sDSGIQLZVCUwEw5HJHpD3X8NXP6K6ERvYx9i1gNnjwmfsoK5-BT4dHHs6jREG4PkxWBFiqqA1ZxXFFYzZ1Jt2v0FTsVZ2DGkTSyuu0XkbXVTKVjzIHwAVYMb0gxqz_wKiBFxPmni9HYKEPX0SewmI5u2GxQsLlArVfvNFhVs8h_8XUFY2l26hEvvYxSrDdjZ3vyLLyqg7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23349" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=YAkn21mrsVrq1kRNkx5tRk5btFVWLAiBMd9S03ePwZAqAPDKPFoXNS3m0a95LYXBlzRsyM2jZ6YXWjZuBhiEATAwBQl1jBAjuFHCKI0uX_EEiXQT5P5jTM68s_EQs9XFsWTmUdPTlXP1a4GNFZJqgGi5TWKtaq7KREkwR8qikZ9gekeL9mW0rP3UAEmnY8OGV9HIx92_F8y5IEnxfWTrCwRad6FJfJ2RmUfzMJtd5sWd76bzS5qtsSrqD-ZzySoRFFIK31r9sf_sWhBDBxWeCJn4R5t9qb3YNl1ReHMglsQwEThU2Vb0tZu3doSdLoeS3K5_lVK-wftjPLzy8-DgVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=YAkn21mrsVrq1kRNkx5tRk5btFVWLAiBMd9S03ePwZAqAPDKPFoXNS3m0a95LYXBlzRsyM2jZ6YXWjZuBhiEATAwBQl1jBAjuFHCKI0uX_EEiXQT5P5jTM68s_EQs9XFsWTmUdPTlXP1a4GNFZJqgGi5TWKtaq7KREkwR8qikZ9gekeL9mW0rP3UAEmnY8OGV9HIx92_F8y5IEnxfWTrCwRad6FJfJ2RmUfzMJtd5sWd76bzS5qtsSrqD-ZzySoRFFIK31r9sf_sWhBDBxWeCJn4R5t9qb3YNl1ReHMglsQwEThU2Vb0tZu3doSdLoeS3K5_lVK-wftjPLzy8-DgVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
اسپید یوتیوبر معروف در حاشیه بازی بامداد امروز آمریکا میگه‌ رونالدووپرتغال قهرمان‌جام جهانی میشن؛ زلاتان هم این‌مدلی بدون هیچ‌حرفی بلافاصله میکروفون رو از دستش‌میگیره‌ومیگه برو بیرون بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23348" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2BAJQbyMCFQOPKBUWnzgxs2geCsH9AaZJNH6tpVE3yz5SI_XjEPjuKlGfflDb_R5y0l0YSOPhP19zEuCyAlAeh-u7-Y21BhmZC7T-0_OWBzlZDbm7cCCFsS8DcT-ZtuikTRn-2mgkZm1IINpjsbCN-zZ79wT8caTbcLNOfrsVjCVpKFjtcwmXiwVy6Sye9QJ4zmXY_gQwe4q_6S_ZGXQUOl3kE1EH5j-a3DriKjMTwE_YPObN3BilfhiG02Jhdd-ARTB5IuqIvzpyeNsLDP57oks5p2dj2jG23TSTvgxgJBEDcZ3FdFsJTimYx_aF5-DOFBWa35KC_iUIYHfGcXjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23347" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujGo47aWyqRsh1_8SQIw9mTP6Qx5pyAyXhuzbRRPaX9sPOn7oqrVVIAJQEJYJayQeQp0LZpb6E7osTmHy2n_h6jEbLHy1YlfYw6qh0y7wDGXhE0JqePIT6X008himXNFBXUgD4wpInvurK12sH5zHwfaaY3DtRm-ry1JmbNKNJx_zQ_g6xy9txhHqYu5VDlQxVA9SB05dHLxqId6F8Me5lhRq9ypZ9SCOO0GyXjlBj1fu7xbWXGXSFi16fj0Ea8btPtp9wRza1taft_y4s0LKT0FS77bXJgkOFuy4irx7Eocmh1vQgSyHCNKGQdgChQS-3rmJ2v6TxS1AzO8OnLgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXLjjmuQ_3WTNl3fg7MTicpcGEnuYp8FkSS5yMccyVNQG3tlOvWGBXgW4eDB518iuRIwLWcSm9vyac8B8cL3KAy3vaQdUTajFh9hnObqQA6d1OJk31QHERPuiiMbsh3XurofkAdEleT37VHHmhmuo6Ff4C4Vi7CcGAKxii5ve7I7lde3nMBP-f_cQPoGBj3mlw5GYrXRsjseYHmqlzaxI3rK9pPDTZdjZvR_100m-uSYj62s_oEu7-205RI_VNEDJEU6DJY5l9atlK3RvljgL3SegIPFefp6YUBTkCjrZ7ghHE2J15voiznG5xmi6lNxhXOClxn_U155q_GdtSI19g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرنگار معروف باشگاه شاختار: بازی دیشب بارسا و پاری‌سن ژرمن فوق العاده بود. انریکه یکی از بهترین سرمربیان حال حاضر دنیاست. همچنان معتقدم که باشگاه‌رئال‌مادرید قهرمان این فصل لیگ قهرمانان اروپا خواهد شد...!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23345" target="_blank">📅 13:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23343">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peso2HD551FKfBXwKbvWHZx8Yanh9eQejg5nszWRCAsnVMWJHwbGxZLi5bP6ccPv8dvFSFF9Uvpin_oZrkNac3nu0A1aDhLlQvemnvva_q5U-Wt_dC14HVVKYNcxylXtLy0ZExtgkGO49Na8qK_MLpwoRuiYkXCiD5h7-6rEeH_gnFw3zj8kRyXT2B6ra04qujH3bZqGOrXYDG9KgN5UTBbA3D-AyefH8Jq9ECDwd-6DXPAPrUjGqUIVMBpnGo4_Mhv1APlOIaVBg1jae_cW28O7HN-pwuBudSAmLrypTyyURjwx9xAiSRGNfsEHeb88A4NWbGLkJczp4u4szzAj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23343" target="_blank">📅 12:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqLPjFqonGXaklfpPeN5NXFQqG1BiBmKtYVE438ZuaaAp8LnmqZctR9VLQ_XM60Pde7ex0qdJWZ1WQazGvPfUwRD2zHjF8y44CRg4FeCNv1PG-OFiYIobcBaOFNPbZesqdNYbnM33sificHVuGUkgJ-21jh-qcbTyHtCYV0n9VHPi22dIT7AAcNsgqj5WIw430-OKjKdsNSt9hoFErHrfZwWafoY5XY0xTv2gMXuEwF8jwOrCEojrw1WIw2GY1Wsk-43vBiVjSbkQ5mkEEeee9vWWmmq2CKy3RyyFa28KW-C_IoKMpbVn2e96d9XLwqfdZcxOtngO28986XCErtjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیف‌وتجهیزات تمرینی تیم ملی انگلیس در حین انتقال از فلوریدا به کانزاس سیتی دزدیده شد. بنظر میرسه که هری کین یکی از قربانیان این اتفاقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23342" target="_blank">📅 12:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SERjdy5hs9CirvDLiXYrGjxLQNQctILcJ0YHn0ax-mYsQ6-1avFjCVV_2jAmZXM0yutidMdZ8_3oQqnIMJoAze9ejwjL2L9mA6AkD_LQG106bRJIQkMEZMBdS23rN1KfIgJqTeZbSLFaljiT3yIvCWoFvAr1S8N7k4PBNMrtzj63SrzUt4UnLvfOdkEJFDCxmu13zvS7d3dwAiJ6ZQgT8KaCzQ6pkpSIW4MRU2JKQC6icHao7z3GU-Xcuwc5ejWY7jwqiw02xo0bI0Jd1HfOvTNuTnLxYX7QOVYRk_LFXq8KehXVxxqkbBS8pbWiugBguaIwUD_WIIWmfTrvdFWKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23341" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVa3teW5sYWL-MD_i7eljnL4ajg7LeC2J7vQ49ejOZAgsdanIPwgECnfPuUTJK3WtcewJI1uOXLItnhvCIsvA-ecfzSa4Wb1vygxGh1hdV50yGuRMBkPd9zVyIjvMvQYcCdWBtBhpP7YhAWPMXEUoHjOilOPVj9svyH3BLkFek28IkfWh_eF5i6WUU1mrCHf_MSt17I66_zJUcgKm60iZHZTwTzZ0ZM51dDoTLtHy1lYMNg199OGvWNG4QVFuxWiiWTbT5XNGf9sB1APpxLsZIfMc1eD7R7Kewmqhbfi2u3WBj3IUrNRIJ4oupWK7s9n1tOwAZok7jVlQ4PfJ3NIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23340" target="_blank">📅 11:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiZ6HnNoV-qtFR8pPsaVM0J5ZeXhHVvVDfqH7PPU_1Qhk0w1jri_o3lNw1whZHKIUZL0PgRpMwXSDqKJZpQUwAy_D_JLlhZNBfvsxhiAgxjJNyhfYJXXUX7b9zt-JemdP8uyDCZXwDV7Xw9fgsuDpQ4V7NzwI_INLiEd9TTIQKSsBBxqyqmZQhIeriZvBOwwco5dgxH6exHMY831Dp8rwT2yVEszRnDIUXQsYW4bZbLvQ7Elagr1QiStQVGwGh3-qcRfnVTVovqC5_OBPP8KIbKrXH20ieiq51SfKwzab_kGm5JFZVaBYNgdtGp6j9a_nzalM4HWGfZkIzxOr7aVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 صفحه برتر در اینستاگرام با بیشترین تعداد فالور؛ کریس رونالدو بعد از اینستا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23339" target="_blank">📅 11:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVbySrTvruG3bahaGgAbq-frMNbomjblvgiTtUtcxTPfAM9MnHwNI2Y9KilsZeYN5ji4doLK_8Uyow7CcUaIBAeJE5tMUznVN4paVarU4AcieRIy3WTh8NLA27DA5ApFjAUV5FVkSk2p0roPqrRWrL1-aAkBsSJX5_sVBi7jOekyc8w-XTu0zucYdcjShKmF4uFigQn7mEx6RYvsq99Csk8DhD-A1GcCWtuyqFpR8DtFG4254izjhLuGNNTMoMV8jEyRPQCiDWzNyc4hjaL9oKxX0SLTY9vFdN9vz3ZBB3zmSIQWxLWDgRGjzcaq_pZ2UopF8K2bTUfQgMdXJ_uNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23338" target="_blank">📅 10:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IappdA0S4mreYa-KXw6qziKL3LxNMgT8J5PNjI-cMI6-FYM_wpNsrb5SJdTPssXG3c4BPzswrF0U7lFvhziDUOn4uUpf38_blE2w-HH4t_K_3qPRYUJ2yYeaex-20282SqzGHInypWeSAhyjvcvLxyriPPGC9SSp1zy52x1zRdbDCrY0KAvSSbBrfUtbfDI2s4voBF-jQX1vlxSIJLl9VgoD9pOZF4JfY46teY2Rk9P50OB9rnAiKpz58JJFMBYSKWW3XSEVslcVoZYUiQ_7qgTtmZhFtZ-4d1Gc43HpLqm6Ll96xQWRiphKHCyXwne51VjCNEDXAbAbZpXvDPtpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23337" target="_blank">📅 10:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29987e4127.mp4?token=mVQNhic02ZRzJAaHpXEFOoVJVwigcPgfTBGJeyO12wYGjKcsPhjFHOSupgmD-gDv-1Zzhw1g7m_EUteU_XxgMRrdm6kP2MVHy3PwEKlEpCB2s2I5zjW7no6BFqabYO-xqYtvqJLeHHJ1VYQi1IpJL0YRPwGVM6iGeZFAwuwVkkbA37KdPcpb6RCAixu4W-GnaZqIPueU8pigozLdUJOTd7IsLEqoAiNqD0epMXzk5KpxTgAxrkukkQnA0zMPV7hEWR0bXWkOqvBr8LXVmBMPcNxxQPOFoVW6ks0Q_HsVHdUnAYe4giQPhFCnLIdRQI7BFnpKJq4GioDQEOyWfVyPzDl2-3E9kkaehk5f703Zvy-BmLLF-kr8dHMEpqH3-hbBDjoMIWAQDIpeZ5bbWuKJmFWutFaOVrXepWz-mzC5_q2EulkeF3fIhi4YzUcfk64xGRrZF5UmV50QYHiqP7Ka74RmBtyo0aleEhn2h2_V3oolUMuOWvi7618bEJDT2iOSy95ARx9f19EQ5uSQhxiD16aEk33IVuPk9Cmfv20S13Arw5-6L-MubDZr0-5VTIiffvlDkPRSdIhkyxT7ggqjIWmYF61e2oHJVPo4VlFvmZvGz9XutTSqw0TBxdGFgyyityfGMn85QhpkRjYeaxdbqNE8BVu8lCm7SfkSJb9zKrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29987e4127.mp4?token=mVQNhic02ZRzJAaHpXEFOoVJVwigcPgfTBGJeyO12wYGjKcsPhjFHOSupgmD-gDv-1Zzhw1g7m_EUteU_XxgMRrdm6kP2MVHy3PwEKlEpCB2s2I5zjW7no6BFqabYO-xqYtvqJLeHHJ1VYQi1IpJL0YRPwGVM6iGeZFAwuwVkkbA37KdPcpb6RCAixu4W-GnaZqIPueU8pigozLdUJOTd7IsLEqoAiNqD0epMXzk5KpxTgAxrkukkQnA0zMPV7hEWR0bXWkOqvBr8LXVmBMPcNxxQPOFoVW6ks0Q_HsVHdUnAYe4giQPhFCnLIdRQI7BFnpKJq4GioDQEOyWfVyPzDl2-3E9kkaehk5f703Zvy-BmLLF-kr8dHMEpqH3-hbBDjoMIWAQDIpeZ5bbWuKJmFWutFaOVrXepWz-mzC5_q2EulkeF3fIhi4YzUcfk64xGRrZF5UmV50QYHiqP7Ka74RmBtyo0aleEhn2h2_V3oolUMuOWvi7618bEJDT2iOSy95ARx9f19EQ5uSQhxiD16aEk33IVuPk9Cmfv20S13Arw5-6L-MubDZr0-5VTIiffvlDkPRSdIhkyxT7ggqjIWmYF61e2oHJVPo4VlFvmZvGz9XutTSqw0TBxdGFgyyityfGMn85QhpkRjYeaxdbqNE8BVu8lCm7SfkSJb9zKrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چالش جذاب هوادار ایرانی با کیت های تیم های حاضر در رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23335" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c684a93218.mp4?token=THUy4jV7GLFnehWEXd9T_ZUEZiOEIPf5Yksh5yeBUOJCzNoaBWDE9a9t4xnNnRR8JXzTJDy_RnvFLbCCB5xQxEdZASymBeROIZzUWtAYd9Kr-MNbbnze95JUbYRf0Co46gj3R0GGcOVUfuWYvn5dEeBul39nWvHN1v2yJoewZBKg9tuWdPftO8ubR4X2yYewDKRnSDsdIBq0KyC6-1Xan5hHmnLPz2-SmeuYVnH0ZF0gqyjuy0IuAgY6sSFVo8U55yUnjANU3qh9XxfGgQtNidClqMJO4y4mFlpgWKQKRNKL5jSOigjuwgCf37ACdXXCjUTmkBDMq3s3alAnsI_k5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c684a93218.mp4?token=THUy4jV7GLFnehWEXd9T_ZUEZiOEIPf5Yksh5yeBUOJCzNoaBWDE9a9t4xnNnRR8JXzTJDy_RnvFLbCCB5xQxEdZASymBeROIZzUWtAYd9Kr-MNbbnze95JUbYRf0Co46gj3R0GGcOVUfuWYvn5dEeBul39nWvHN1v2yJoewZBKg9tuWdPftO8ubR4X2yYewDKRnSDsdIBq0KyC6-1Xan5hHmnLPz2-SmeuYVnH0ZF0gqyjuy0IuAgY6sSFVo8U55yUnjANU3qh9XxfGgQtNidClqMJO4y4mFlpgWKQKRNKL5jSOigjuwgCf37ACdXXCjUTmkBDMq3s3alAnsI_k5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
بازیکنان‌بایرن‌مونیخ چندسالشون بود وقتی نویر اولین بازی‌شو انجام داد؛ منتظر کارل بمونید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23334" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23332">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4ImO2oOxKiJ9qtAFam7zNQ8nJVv1izIboA6OdDMo1Omvx5E_LZ65_tWqBP75LAFxEgl2hL6GmeU8N5RcIGx4jLFqRHuyCZFnur12B5G0RJNGivSBdO5CDIgrVbY_JXQtGgOhCSFE26NbIBRTtaaL4rKKQt2VABLFHHRtTLaC2AcumV5y15qKPGI7asggRv6g5ucQmUGVp53DsBM_z7MPJ_uWRgF3DoTNlo283Ypp9VQrNqpgyVgSfiZLDN3R9QT023OCLh_hKewyoEjIZH6rACMl2Y0T9v42EkCbFllusOQ2BT4Jg134o1yJjrurRGSKk9VlrYv5c0HDANB4Iv0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23332" target="_blank">📅 10:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|آتش بازی یاران پوچتینو در گام نخست‌ رقابت‌ها مقابل پاراگوئه
🇺🇸
آمریکا
4️⃣
-
1️⃣
پاراگوئه
🇵🇾
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23331" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N599-m5uK-aq8k_OBDKME4iWemL3J5nDalCWaoOlWcBnFbZVdwS_xG-t5OLTbdbVx-bwNO9gGNVjRmszAS0hZEw5q52sIjKMrwHEJWRtg6YLYWPe1L6C1ue154avmJRMhFelJpuL91OVsryZRNfNfxcxI5l5IUv4RHTl1_lFqJ1hC-BS-Dag-5c1WfFfXeb6gVVaJB8FCV2P9MEHPOOwo56wuVU0kFLg-wom90RJUkqX0q19F47hrEx9BNPd6LUejBx07wuPxBnrAp7uiTv4gahL5iK_4y5yY2Pi1RGLgwYGlqBAknteaL2vMxBdIXRk7TZr6FJd_5R-j_bSowngiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23330" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=Mzy8goqsvDP_68oZs81VYB6I9WpU5Gtku9_lvg7l0UctC2H5B5xvmjrq0Yh4Bjk03K-0iCYSD9lCEnjMLIlKqiHbd74b1HlxP3jOY839g_9dlBrZ72xfw9J3AmMlut1nncFw72p106IFNND-0_Wa4NZEMGEpiFsZSE7SnmubJCMB5V6qCmkUc4Q0gOlhH4JHUgSYI05yp1qEqr2pB02HHrhVElOkTxWyn4XeGocYNbm_B-rzagpllJ_8XTw-_kBOjZC0NsVk-SNBN6blonR-CaPUNF3KAeI-8VOxxoR8rfmgzIrvxxxJnTkRPdOjOlRLSh8Zo62oh2V__Mdjl1qIoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=Mzy8goqsvDP_68oZs81VYB6I9WpU5Gtku9_lvg7l0UctC2H5B5xvmjrq0Yh4Bjk03K-0iCYSD9lCEnjMLIlKqiHbd74b1HlxP3jOY839g_9dlBrZ72xfw9J3AmMlut1nncFw72p106IFNND-0_Wa4NZEMGEpiFsZSE7SnmubJCMB5V6qCmkUc4Q0gOlhH4JHUgSYI05yp1qEqr2pB02HHrhVElOkTxWyn4XeGocYNbm_B-rzagpllJ_8XTw-_kBOjZC0NsVk-SNBN6blonR-CaPUNF3KAeI-8VOxxoR8rfmgzIrvxxxJnTkRPdOjOlRLSh8Zo62oh2V__Mdjl1qIoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تیکه‌سنگین عادل‌فردوسی‌پور به امیر قلعه نویی بابت ساعت دستش در مراسم پیش از شروع جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23329" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=URVrOz2EgKsSzkXqPfkU7ILI21-0ue8kJvZb58DUhtLLvLjN5vUWB4mavewhF3pfCrmWggV85eNy72taskh_O5FF-e8JnT10gxRZ3VGry0PaRGIbR5mBMzi2y3t2CNbJLYWuonjkjUkKeuMmKK_3D72dIiqb9CR4ZOrPhFSV-86FoSRv7Vc9mUtFID5vNTBNiTniqm_omKngNbcfcKwmd5jY1f0lrcxFCgPMHo7fv6BZcq-WzzAE-FBz0sCgM6XYL5JwJkER6rR0R7L7Gncq2rGgUgazS5E3KYvQ8IX3QP5ThjDKHIA7N4VTcfu79EcNguI04MSMWCbCYBvCSDFYL3BCQJkYg_gET0kYL9FSDE3Mq0amkNx6ilP0kvSQra4fV7Wnhd1_eWPLZywmsdZn7xbHxkAZ8rx812pMDaSzYzJSi1vL1Qy_gwaFZmowDJZJl_LjTTlK9d3GbTDFD3gFP9cUj9ZLVKwslTwlodKoopdl-f8lRO-Nk5DFVK5V3LMOPb6HtOIGLfBZ3n5_tfsmQZkvy_olJCkoTYG5V-mMjf1QXWWO74vziWaHgFFoTmLFJr19ZUepxETEa1gz3WJPrxCu_wNHO8x1VggRvcgG2pBm1DzqdIgwZ0q2UURncE7EU1BcO0KDsMegEczutsIk0EJx5YDwuk0P1QYA37VFH_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=URVrOz2EgKsSzkXqPfkU7ILI21-0ue8kJvZb58DUhtLLvLjN5vUWB4mavewhF3pfCrmWggV85eNy72taskh_O5FF-e8JnT10gxRZ3VGry0PaRGIbR5mBMzi2y3t2CNbJLYWuonjkjUkKeuMmKK_3D72dIiqb9CR4ZOrPhFSV-86FoSRv7Vc9mUtFID5vNTBNiTniqm_omKngNbcfcKwmd5jY1f0lrcxFCgPMHo7fv6BZcq-WzzAE-FBz0sCgM6XYL5JwJkER6rR0R7L7Gncq2rGgUgazS5E3KYvQ8IX3QP5ThjDKHIA7N4VTcfu79EcNguI04MSMWCbCYBvCSDFYL3BCQJkYg_gET0kYL9FSDE3Mq0amkNx6ilP0kvSQra4fV7Wnhd1_eWPLZywmsdZn7xbHxkAZ8rx812pMDaSzYzJSi1vL1Qy_gwaFZmowDJZJl_LjTTlK9d3GbTDFD3gFP9cUj9ZLVKwslTwlodKoopdl-f8lRO-Nk5DFVK5V3LMOPb6HtOIGLfBZ3n5_tfsmQZkvy_olJCkoTYG5V-mMjf1QXWWO74vziWaHgFFoTmLFJr19ZUepxETEa1gz3WJPrxCu_wNHO8x1VggRvcgG2pBm1DzqdIgwZ0q2UURncE7EU1BcO0KDsMegEczutsIk0EJx5YDwuk0P1QYA37VFH_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
طرفداران‌کشور‌های‌مختلف حاضر در جام‌جهانی؛ از سری جذابیت‌های بزرگترین رقابت فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23328" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23327">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚽️
ویدیویی‌بسیارجذاب‌ومختصر و مفید از مراسم افتتاحیه رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23327" target="_blank">📅 09:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23326">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flBpnllRREGXL6jA16PDxkeWdyDCm2_86jhFGjrZpZUIpDQurDwew9JEeztkuBQWs7pyLLzc9XjH1MlP9J3d4tiRWM3WMcmrqE5DXdmef06fmHjpQU047XcH11sHkZb8-GwGfeju28zU8qDNaLWym01EfrQLvpuGplxWbGrz5lU99PJyfUwgY5C07XEzTK44lMEKJHTwKTbDr4IANnXYOyzaWy5Kd08hkMx6lQayHfwPZLpkHAHFC_0Ik3vA2Uv_IHddfDaXY80hOK6W4zjBDfPYevcBGEWChNbojctrzLUQP3fl0-_J-PPSoCa_IlSOAVyHVGrCQqjR4lGQM2nyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حال بازیکنان تیم‌ملی والیبال تو بازی امشب اصلا خوب نبود. این صحنه دو ببینید. باهم تعارف میکنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23326" target="_blank">📅 04:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23323">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQJs1v6Np6mZ-dktv5K7eOkBV0-hjmxcKxdmz_Uaw2771M4_qapWjm6XEkrt_Q09lymxYVDeTyUv8LXfAyhEgMwZtvsuRCUkkxhWAHyLxfAv4XxyCzexmSqojclXe40RGYms32wJmJtRZCpbwV9rYZqcwtK2CDR7T7KlvlrOchGQvzG3F00bemwtyf3sea0uvWl5r1vFKxwJok4HrVKJUiRtd-Nvy-eUs_ASwlpd9M6gA1vWna3eDqq0OQJPaEONlaQ0xjoFPkfbbnt9JfcKKGUZ7aY1PDtTR4C0vmE7z8Mp4KUtavneD_CL2PxY7UNoZH6VCO3UxPhLWY3nrP1IFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6jB-V4zhMMWBRN-7s8wqpByz-18wMfD9ViGJ7-0fe-Z4v_ahi7MVdycEQjCyYtXIyWIB3pocjt_ZXqdH5YDsRx09sqRwxRq28j7d4Q8o0pSLJarUvcmN8lPmQYJobHyoSD2-LvKG6Dky9kIrDgrNd_Cc5jwLBjEYtBWOCJZWGpSlgQndBR_LWjnMcC4ZGrD1lPr8_3KqIOkJLD5ySAmt8kQ3qN-XVuhKvWNwD67xdedXhB_E8VSVVxDnYFywD_xHWsD-RF07gYaPPw5pnXHFrLvFJ5fUn2ULFRbkDKugCcGBIEdm0WNH22-EbAvFUDj5v9eIXtBV4uYk0LDc_FMmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
امنتیت بالای شهر تیخوانا؛
در ساعات قبل رو به روی محل کمپ‌تمرینی شاگردان امیر قلعه نویی یه جسد توی صندوق عقب یه ماشین پیدا شده که در حال تجزیه بوده. این ماشین هم توی پارکینگ محل اقامت شاگردان قلعه نویی بوده که دقیقا رو به روی کمپ تیم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23323" target="_blank">📅 03:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23322">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hADgiSoEPDLh0ne0QvZJbbrCBDZzF9aVJLZHMB1Dphhnq6Rlj6vnXsVAm3irvfy_Mz-a0c10TuHjLh1Y8Ih6crJBiV_GsfKxKf-zj66RDoH97N8ibJlMB_BJ7_NdFxdcHWuyFReeKZot99prxL_wWS8FictbNSXoBp_mm2navdq2P_bAZEiyS_i-moqzp_E-mYzGaIetjccuoTg2bfCgR7E40NOuusWZiV8LQg9Gt1h7lN61mqUVYJqnHZs7eYVqoUKspp5MVQNVT3q51C6zHy51YC9z8gJ4m35qHUgZx60te5bJeFKUjM-xXN-JG7WfXF8V_Uv8b9oxgRuvGdF6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌کادرپزشکی‌برزیل؛ مصدومیت نیمار جونیور رو به بهبود است و این بازیکن از هفته اول جام جهانی دراختیار کادرفنی سلسائو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23322" target="_blank">📅 01:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23321">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9_1f8GSrrIylwvFMmnWCcLBsEDEA1AdefY8O8vSaW4PC5OvapRMwZTXBigLVN-xRfSt9ohmjx1RUxDu3U7poJvkQz4i5ALpMzb4cZageKrjZ0sp83Uxk7KvrGuxMbCjgy9EJpt-05qyUyoiMkzYMIh8pPB69d14RngDO_NVQkOxDV6DZBEdpBg1sa8Ezf1mCNqMRiCE84DjjgfUtS0_5UsFhXW_jRpE8k6GBjnNQ_geOy4F6hxMFsL22fpHPDuOc--z_qcG8Oc1Qk61xxgi-OQoWnRd32STGDy3lSCDReG6xiBveKoQJKdOuyRIg1GLQQqEzjD_dpU64CsNCU-ukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|نشریه‌موندو:دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23321" target="_blank">📅 01:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23320">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">▶️
قسمت‌‌ دوم‌ برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23320" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1nQ4PHvSJGFOFt4gaCXoPzaejOYcQHIpPrRAMIThC0VnYPPloJaxfden9HtO0bmbgqrnIcU6X_PFBAGAQalbVHMxWibmwNm-EY0PGle69ZD33DI6qTXAf22RupDrpwjZ5iHQWdx83xc2sB7FblJh1SrGB8GAovPfZRxdWiZHSXytaqjWcPXfzLHC4IPAaqwV3Yc_j34EZsIwNBjGXLGLlSSdEUfp8HutGwxHkREZSP_0AngzBU9gj2vP4FZKDfx-XxMZmj4DUTD8_kcNe05zOPp5Nq4w_FB2l0Y-nLjkMv0PLTaqWFLlBOxAyldONYu6ko0CH0gWQnlT5GWmoQOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23318" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJO3O8Qlu8oOYaPa3HFuKg3YMNMFci3FA0YhgMkd0J7pee9V5M4hIA_qVhSA7q6h8psKnxCZoip7ZaZQa25WVjK_yr5frUF9V-RcZICSDTBGtMUXF_OyTfgTHP57vtQmB0Dl2QIhlpO3Bx5wtRFb0hoRmj3b43Nr2hoTDHYKjERRwE1gk57l7l2aGdZ1432bwGNhusC9eBoXwd_7W1Ymq-OlvrAOqUHRrCD0CRwmkfQI3EH0-iyuS3l67AbKuEteOQeA438NNoyDHxD7isLKzhm3NMo3F15x2xAyVsy9Z3yjrhJIS6Nu5n-tQzq7EHrlr1wq4GkjPqRFCqmtBraj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری بزرگ کره‌ای‌ها مقابل چک و توقف کانادایِ میزبان در مصاف برابر بوسنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23317" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23315">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lgJjovIdv_mkrrDVdlC6es1EVyk1qNaSptaZ7o0pUc6KPRnxnCMzK-FswdWw4XVnQT5rcEWSgX1m3dMuDDJfWJSkY8EeWOPJcvYDBg3y1rzPbD_tXdW1NezD3mRaiUW7ZbAT0sUTH1-RII0dMELWEoDRmHo6iwmxD9qxWmC03XL0uRoLv54NnxcU1XWOe6z0oBwcf5i99H-_PzOp5DpgGua-XRLnvQEFusSwvz13ifRYWZFtTEPnCS9P-1WDr6qIwMbYehf2MwUiFnwfZ5BTXqCFxT32yvbxIH127gs0EcvIhiEaKm2HzFQdMshFZTojJbb0s-SZMNeCgXP1Gkv9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2y1fwvkZnia7zDcnHwRNSoAByMpLui4K5rzRuF2TDfcNy7UYEOajmomGXMPTZ7nb3n7ZMg55-aVjFReZnQKqOlz5EFcbiNkKoGbIIMJdJud8Aw9SbKQvMO8r3f9GCdXDdTRlkXPiieOpYAt_wxxmIwGsDmT96J0MyhRuOwfFy0mTf8fy7ns9hswJpfXfPE8rUI3umVszdQ3eEz_1U7GZwIGVvtBqAMaIHybl3tO3NSdZHSZQeTDs9G5_EShh6XL_3-j59kFWOtXh_eVTTxHQYNzqsZgbyYM_QDTRhIuEyQt5jdY4agLeAaSk6dCl4gt9gCoQrjSk8IkNubOYMuo4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
شات‌های‌جدید نادیا خمز دختر پاکو سرمربی سابق تراکتور؛ ایشونم بعداز اینکه اینترنت مردم ایران کامل وصل شد پست هاش رو شروع کرد به انتشار. حدود 70 درصد فالوهاش ایرانین که اون سه ماه نت نبود اونم پست نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23315" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23314">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qwgj9kwMDkFaECY4qtq_FSu0VsgFAvbFAonmdqRYDAMjJ-aaAz2ZJm-dfFW_Ii4dLIfgKBeZVEnLuYwA8VW6JeB_uycZw1dzkruJxtSVdrioJWsDltxCDRR4UH5cyaM1B1s6_xsoGyfeLaBtRp4k2bZ7FlK-0Kc1uEP6rl3bKW6yd_5JIljdvITJkZdrLH01TB2pA0lOPp3cVDI4JL14_tYlVTbgIibnN3D5nefRho7M0Py1yNapAZ3SNHk70v-fEniLsO-NYUAA1eBwUX3IPnPhziDNoirs9yXu7yiIxOgZt94V8aPbPy2JMS5hUXN0RMEHzma-N78mTzzKzDkXeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رونمایی از استایل جذاب و گرانقیمت قلعه نویی دربازی اول ایران مقابل نیوزیلند در WC  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23314" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23312">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCca1THG4RLk-es8Y6ypa_GX8YRIQXcfUWerumXuhvh3mdd6mwdqUsk8f_ovuALbVlInQW9bOP4H-frWZ-LWrAJ5P2e5uAJ1T0xB86R5Ut2008sHPeerEfalMMkoqW9XLN2Bnwu7Z8fnSmsFPzKNEn5un9Bev2hXzRpNB5HSMi-7w9yYnjlIub5_ne2D2FpkVI_QmSgVEHL4qKAC29GDQlPg0binm0hlubBq1Od_EVcRMuyM7Pb2PrlIG_0iZSh_zHZCMK8iga-6G7jTuXqPJluaQgi25E-wyEVgW4kl3EMck2grZ9Hlx5HbcnNq-t1nMEAClosKW5LA983wL9RYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میثاقی‌به‌منتقدای‌تیم‌ملی‌روی‌آنتن زنده:آدم مفت بر از جا خالیی ......تره! همون شعر شایعه رو میگه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23312" target="_blank">📅 00:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=gstelTDgLc74kljmneLk-nKXiRlhu1-ysjHvY9RH7pHM7YpfePKDk-9qoQOxuq829vZfze2X1yOfpZkgBAbtu1kSugXV-Uqp5IHcAgyftZxfYtQl4iqB-zu8HKimt1Ik51mZtg9NATwXZXREugylXmHEFwcul1Y_5vDRUC-Ao5viwtUgTwvi6gX_rFiAxwbSNOu106S3b6itvtMn6jpvqFJ_7ZbRmLTyP0g6c_4bluDtc92wC3EN0CJxoTnz-t5N54oWDQNI2Ln8PDZcjAr71We_02dsdC7IsCaE_ZmI8Yr4r5ZeYGtNiLl1u3Lskxd5h-SsU3cffU6-_d_-3wwN4T0gvgTXkueqfFcZkmpvnNMWXs8lA3EXoPHIHmGAxHjzyR4m_6qnsMNhJGyqh0lcqXNIpSTEB615XesckiSANXMjNpnEwNguwWEjdsE7y27_D9TFaKtF7dQQBRIWMKK8ESwNwFJcPJ18pxngkfh18Pjn5Py9tw_fHTxozYxMe_oSIN37r-vjQjXyozM0K3e5qgDd5tE_ljUnamcWAeegr8CHZaM3L0A28ztEzwEE6Q_GaeH6S_lRI8LbMYBlUP_7fyhVBPe_jPnRvz2v7q0k5UogyG9BkYxqoVrSByWDafPIgo9BIjMNAzT1QFIoTOTS7VRXRpf9_biqB8Xv8eomkBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=gstelTDgLc74kljmneLk-nKXiRlhu1-ysjHvY9RH7pHM7YpfePKDk-9qoQOxuq829vZfze2X1yOfpZkgBAbtu1kSugXV-Uqp5IHcAgyftZxfYtQl4iqB-zu8HKimt1Ik51mZtg9NATwXZXREugylXmHEFwcul1Y_5vDRUC-Ao5viwtUgTwvi6gX_rFiAxwbSNOu106S3b6itvtMn6jpvqFJ_7ZbRmLTyP0g6c_4bluDtc92wC3EN0CJxoTnz-t5N54oWDQNI2Ln8PDZcjAr71We_02dsdC7IsCaE_ZmI8Yr4r5ZeYGtNiLl1u3Lskxd5h-SsU3cffU6-_d_-3wwN4T0gvgTXkueqfFcZkmpvnNMWXs8lA3EXoPHIHmGAxHjzyR4m_6qnsMNhJGyqh0lcqXNIpSTEB615XesckiSANXMjNpnEwNguwWEjdsE7y27_D9TFaKtF7dQQBRIWMKK8ESwNwFJcPJ18pxngkfh18Pjn5Py9tw_fHTxozYxMe_oSIN37r-vjQjXyozM0K3e5qgDd5tE_ljUnamcWAeegr8CHZaM3L0A28ztEzwEE6Q_GaeH6S_lRI8LbMYBlUP_7fyhVBPe_jPnRvz2v7q0k5UogyG9BkYxqoVrSByWDafPIgo9BIjMNAzT1QFIoTOTS7VRXRpf9_biqB8Xv8eomkBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23311" target="_blank">📅 00:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23310">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6oQ1A_KT-brq7S2bCqkgJhZS7zPOvVVh4NOOrWe9NUxTo36WCHKGvOuIqsylg355dLNVWR7QH9XyPLNXSHjlenkHR9VLOef1mgN-Ty8LXx4el2pRcrkqPAUDmvqe2wbqL5-33LSUug3FKhsSG53rkCs79nfBVAUcCP5GPYts9GgFq9T0OoyUfTkcsZo-4PgouKdh8cFAkUJvxO2ZNUxbu91uiM1JQegnsewidkiIgaDhyt5HDJFguiTeSUbCwWS7hUl79qDKovwD_mbUdJZlH4jI7BpyHvmevMjYDAUObnQAuna1R1m-XOsDCd7A8J3Gsr6tQ_KlB9gTdtyMtw64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول جام‌جهانی گروه B؛ شماتیک ترکیب دو تیم ملی کانادا بوسنی
🆚
هرزگوین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23310" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23309">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNn823REczNlmpVmnXLZe_XgCu_GofncxgTwWqRofXYstRg58wwSaPWoIR4h3hCfEGiJGD2rAwYC5NWo5WBCeugDVwIm-6-kQNaQDE9dWj2as0Z-s-HNnz-hfyoe0zU8ptCA7DKd0LXHGoB77MnvaTfZeIXD7wR2di0ZsN1_fUHHyOKQcIHz37_eTfM6liUF8d5dyd_GBckd0OzqrjiJ33vLYubW0sB9QpLqS3yInbGB1HKXzwVJo5ISceUXoKOfczZfaFMI4hUD6cP2GwgjzGViv4oGXASUVYIw1x8y28lgoFgNszR-iUwyy7hnvDfuQF3RJEI2x0B3BaINto6nUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23309" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23308">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBFSDCEljRYIEOPi4BlWIcBTkUyYS5APPLY32m23sGqcQuKRr9t7AU4Wqm8A-D0sCgUh9OwAIG9uSWYaLKOVDK5KInNYwXrPd5evrF6GYXkjmCVu2e6hQC7KGyImqsnxc9x4DujH5d27WThiwu6pp6tbFwrqcRn440nsF4wfXrcZrfajk_zUbnaBPTFL14BFBrTuhsQO-F7cUxzEbEwLd3GUOyOkkZGaQ89Pd7kqtR7zsIhccYGozNEXQfkAiWdaphRoeo7-ZHQ3rU2UfTrzaKXkXHpPgmgzGpuSOD5q8jdqBNE3PgsClUO1Pb9zIKFsAG_SwRs5GY6VEKIgTijK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23308" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23307">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Klx9akZCzwTU5BZBF5sWhDbc_pWHbGc2iMY9nd_DMBYVVWTVSD6Na0I3bIEYnPb2jC8aN8k2hGQG1Jawy_-t4KDU075XsdbAHjDpqykvGjl2dfJPc2l5J-BXR9Na5D71-qerANDNnUHg2QrCo2iO9OkA1dpXxRe7xxRbRjZesGVNwzBZSy8fCk3UcR25dRdSCV-9iexGBKofavDBBXeOjEq8PienfJdzc_Nr3epkJ9DnTfGEH-hlVJFzwJ8gXb7h21G5byMQfRQQDXb8d2Nt7Wzq-jFoRe8s7UoSg1puArucCHgcjWMcZ6VABZLWgVfuvTN2Xgwbuy-fft7Z-ZRxOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23307" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23306">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvhIkG6zF78xQpQ9EFtwfbA_hV85DckJbxl4YMJnGtUb99jm8MmQUajCK4DoaCtlWt7PxZGLNmud_rNzFwgiFYcppIY33dzY3Oqr5Nh8uWttH3JYgy3dJk3G3IdJdZZ8Wp5X2RVs_0mRZQpUAYCtD1511dDUxSicwzgy6zYXNaxhB5LmigCqtNxZhhfs-42cLcoj22kEvD2y8kEJlBdmPk4aubQZwY75pDs9t3hbtrCTVu-hq64V5fP-U8fpRHhjmcCOoAG-3lEp3p6MZA-oPinQfJcDP624vMpLkZGUbmk99o1AQCPd1iwGpbhvPN5f9mVsyg6ap0jQneX2m8ONIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇵🇱
#نقل‌انتقالات|باشگاه‌فنرباغچه مذاکرات‌خود را با رابرت لواندوفسکی ستاره سابق‌دورتموند، بایرن مونیخ و بارسا آغاز کرده تا او رو به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23306" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23305">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPUMAeS1H80gJb78CEgNcWw5HlWY6g2TNXRviSp5TPs1Xgk1uEGP3tTcV-m7hVxG7Bp2o7o5a3XhaLhSfFAXVGWaOOv-3sTXxXYDOeTwR8yREUzPP3SUcgkVYqbgnsnvG-ImDQGtxmUcHDjJVioIJYuc-yNPmHUxCmJV4uhehOAp7VTFwQB8NV5WIUCEuAfGqSAwm5eer4pwXbZA2CYc04oXwTojtor3tPdekSZw66_KyzJqt_GrMhIg3_RPf_G1LFNrc2rn5ayPvpu0FJw9RLVd4-BLOvc6m_b0Tx314_89eqKcc9J0gngPeib74vm2LzmS4R6HQJ8KsTF4QX_3WVds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPUMAeS1H80gJb78CEgNcWw5HlWY6g2TNXRviSp5TPs1Xgk1uEGP3tTcV-m7hVxG7Bp2o7o5a3XhaLhSfFAXVGWaOOv-3sTXxXYDOeTwR8yREUzPP3SUcgkVYqbgnsnvG-ImDQGtxmUcHDjJVioIJYuc-yNPmHUxCmJV4uhehOAp7VTFwQB8NV5WIUCEuAfGqSAwm5eer4pwXbZA2CYc04oXwTojtor3tPdekSZw66_KyzJqt_GrMhIg3_RPf_G1LFNrc2rn5ayPvpu0FJw9RLVd4-BLOvc6m_b0Tx314_89eqKcc9J0gngPeib74vm2LzmS4R6HQJ8KsTF4QX_3WVds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23305" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23304">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23304" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23303">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciaFNxoWS4UoSUCdvfON1zWYBSBFwZXQXo9YfMEzBeaXKz43_qTYKudu4oLwaV9s6EUG93XhMvrDBKtGllimYQ8exe_ER9DQQ4EQFgNBTlMPXLtk4rHDNBFjxUH9SqgioLRD9DiRgCC_qkQh_EDESQWhqAjiXZUUe8GZETMN2SHjQquqBK7JHEPwOxuxcyF99H45vNNHnYkRE4vcBE7_9mbbuyKI3YtPdAngeLnKw4G_1jiHS93eTFULqfHVPMLLl4oOecagR8G-BGcQbDWYNwWTqkQhiLhYmfz-rtZUxxS1WLDJ_X37la39hxD2E-oqE747kIQWg_1YBC8ThLHKUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23303" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23302">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-LMG2L53yvxmZ4b7OfJ0GvWuqRXMorJ6p_CKhgg60uPExW27gt8WcmyAuYCHdQmQEq-eN5T0t8_b298nUH9u1bb_fMHBEaNto9qDKfXiB0QypKojXe2_GD-gMWwZDf4mIPm3sjkvWHyu9F9ikmy10Z674KWe0byLIObSRGOriloEFQj9bhOBiaQcl3zFp_yd0Wz3yGXf04y_ryPJg1coLYbA8yPFh39P92Tath97xuo1pwO31xtyLwY7Fwr3hAzEV7oaLEUwFZ4aOknuzAuQcncYal2VEPgADQcI7vCycHdbDGS_VcCoN0FF2KkUjjpCsYQKR1o9c0V49q72NLwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌‌اول‌ مسعود پزشکیان شب گذشته با سردار آزمون تماس گرفته و از اوخواسته‌ضمن عذرخواهی بابت استوری که دردوران‌جنگ‌از سران‌دولت امارات گذاشته بود به‌جمع‌شاگردان امیر قلعه‌نویی بازگردد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23302" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23301">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqHdFUHF4NQvmKr_Ctwv-8vnL15-MuK2y0vfh2YgJ2DIEcpnf56QqQib3uywnRgn6pkekTISBvLuZ9lKsF3RB_fy8MAQs2EM0tNCKezeiP4I4Dx9F94kJDAjhgUFpLVGXjFaW16L54Ro70mcRK8Xt14Fnkf65QLgU6U2EIYntX0Rm3kPZO3000MYXg0SqQQENrGsMorHYHtGJ7HrkcjFNlViusqgGGAvxBeg7hHgQkO9yF_7IHPGMdglZ8K4yYZX33no4UT1rcl7FpxRQ5iEXtMvVXiSvFj1HQNI3KIvVZkMqSCi10Y0CwT5J1pHTtkCPNX0LLgnlr42wpcf7pLNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
|نشریه‌موندو:
دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23301" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23300">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxjHbTKOcwVXh9FTrPyvW9h6FQ016--J0q2wEsYjIslFAUHsDh57cEo96MOoq99YwwaAgKyDcsTmQhS-XQkImdqUtL6ePQs3OYcb14dawtdJcU4oPvmZT-6aMMlPRH5NfkEd1bn-nY5D_ARyPzALqfYlZwUhKKHR2Pq1e2uAJPOKY3Lo3R7UqEesFs9UhEA6gvVbLOkQSl9_VkaQgyh1jCmC_0yOIAoFmyIqb6dfzJ-8DIor4uMgR2sJuQCn629jpmY5bsK8musT9Zy0_tulTx2wkq6STc3zbH5L5wslibu1BID6qYcZUIxetotpO1tPPsK1E2-JFYkT78UY5zkfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا؛ مدیربرنامه کسری طاهری هم‌بامدیریت‌باشگاه پرسپولیس هم با باشگاه استقلال مذاکراتی داشته. رقم پیشنهادی باشگاه استقلال برای دستمزدخودِبازیکن‌بیشتر از رقم‌پیشنهادی پرسپولیس است و الان‌همه چی به‌خودِ بازیکن مربوط میشود که کدوم یکی از این دو باشگاه…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23300" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23299">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=Kh5G09cEzRPzu09Va_hv7kIvICwbKbSe2THM382RXO5-XJUnb1irMYX-WpIJSlHIdmKb0bQPITEHlThXw15_trUCourFnNSXFyT5yTJ1Szb2bmg5M3Ao9-mChh2hWDsL-eyXHiCElaV7KHLmAbVAlEaWswcLPlcoUxsjla0tq_AOPWb8go6EIZ8h8q0_O6tghkXzMgE2NwJ08hNispWaUJGsCQbOjmZMQsamxu22IHOs8tJrDBBLFfLOydBpB_FDg7DrmNSwr4OKP6QVN2xhY-CD1RgjgEfwqYQcz0pv4uR4O1OLe_xDgFR1_oDfubN00JhJpLSc-erRYVvGkAw8TjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=Kh5G09cEzRPzu09Va_hv7kIvICwbKbSe2THM382RXO5-XJUnb1irMYX-WpIJSlHIdmKb0bQPITEHlThXw15_trUCourFnNSXFyT5yTJ1Szb2bmg5M3Ao9-mChh2hWDsL-eyXHiCElaV7KHLmAbVAlEaWswcLPlcoUxsjla0tq_AOPWb8go6EIZ8h8q0_O6tghkXzMgE2NwJ08hNispWaUJGsCQbOjmZMQsamxu22IHOs8tJrDBBLFfLOydBpB_FDg7DrmNSwr4OKP6QVN2xhY-CD1RgjgEfwqYQcz0pv4uR4O1OLe_xDgFR1_oDfubN00JhJpLSc-erRYVvGkAw8TjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیدار کریستیانو رونالدو بایک اینفلوئنسر که بشدت طرفدارشه؛ دختره زده زیر گریه رونالدو بهش میگه اشکات رو پاک کن عزیزم. تو خیلی خوشگلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23299" target="_blank">📅 21:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23298">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_QwsAKfi0qzAhluaUdF8Uv30LlXGluiPtkgjreBLIpssOwG4WN4Q2pG-nLrb8GfcjLzWlQnWx4_kMxKT0EB3dpT6gPOHL5cQwq8xYPPTxuoD54ZD-yrtoVkPCrumtROoFVFiQMkAmRg4GC5dct0uBJbCP5vjlGJZ9z7KIQOMycIGTRf9DU7Kgh200VefwKyrIa9x7YsDNLZymQThZKwPcQ1wBVk427lTFDFc7PplNeAKiQYjDyzzdGyL3MFHGLmZjMyfS2-Zxh0Uwm9Cy61ZhujSaudP8PN2qvqkuAyWmlY_ucfPERn9mUfVV6lH0QsovRXnEQbj-0eIi_MRIu75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23298" target="_blank">📅 21:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23296">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUA4rEamt0D32Euqa9RuiyhYMUGjOFABqsPNaZAHZQFmq0BSo9q2drVgf9_gLhQvtJwEnl4Ps1I_fmQ1RHtTrt6vg0dTNSoSQbOL1I1q1Q2dgj_MfbKzaZ8VMCMEKsTHcG9U0FETvfI9THN08UWVZEs679nzd8a2pkNI7YRHjY0O3eC6r7TZ6qe5V3iSNgPzQx5UfrRekOd00XN64s0e7I7MgQIIOiRPEh2tIlW9wgMTKd9doj-YvAsbkgG6q6vwjIz1bETKOsNcoSpFTcDiXAQckCn0A0lvmwY3XsUjWM1Tdfp9LuEa225ocV1kzGclrY76gqihhWI8bIQnFrJ3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUhdf2jst0UqLH_EOHGg_BqzVTAZ_Bu7oA7-ozjOdbgvEej_pFXdX7pJJhaJhUD2R8nj6Je99tx4VAKzour22y6QrtjL3DpSRYLyPePMbCWoDb9VIo1R40ewCClWQXmbuWq4BMSw8BtdJUMtY5mGmeJ3NZO3lS0MjZu9zvXw30zCsPznD2lCN3mLIl6pVh6RzIgqPSuIfbokwkS-paTqKtkBf6Tx5pNlqfz2WGPONUrxonDC7oW0lAMOgDEEO6HnvJHlEiTMUXOfH4dJ8iyA-nFFkPq41GjA6nZKjcxtI2xVXm76qwSKY7B2fgCmswA6N7PJXQmsFPV61qtGaaL56Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23296" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23295">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
آکسیوس: دونالد ترامپ به نتانیاهو اطلاع داده که زمان پایان دادن به جنگ با ایران، فرا رسیده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23295" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23294">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdLHq9MMP2YXWdwLxX8XrY11novj9RNFPLYSyGyprxwyBWIU1R5MYRPsxSdyXYXsHab0EjIOeL_IVUp-kN0yT8L_AH4Ziw81alqByHrg3HOwy8aPPOWq4ID7joeZnEbEBFmrfhkI7-h1x0-eVeB2iql2U8ijRrJEa8mQb0i2pcQCnEWEdnDYt-jlJOa8Siuq4Hcr9VNT6TevIBI-uVsr3Jgi68-PRfrbRlvZ4meqKT77Yv0HmjsyAyRpGJyCHlCc221IXJyOZ11kETs_Z_Fjsj14mUpcHAZtwA6T5VGLHjaG0ax4BCmIDr3hw_13FoSvO-SQLiHX9SBsqjE-zrq0SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23294" target="_blank">📅 21:16 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
