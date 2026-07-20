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
<img src="https://cdn5.telesco.pe/file/azStJDTFKUSNZkWUALg_zugCGkUySLRdgeTgKzlE7R8oCOp5WZ1gNsKtQkZYrIAvC94oCQdQLCdVa2QDrnNnvYFtbD1qtrX3DV6sVtRukGsrT3Tuy-Z9XFX4OA0ocfc-2V9x5Qqnht_-NKvErhMHitUpLz7Q1ijfi5fMgQuH8mDqwINJhsbWE9oFv4lEFEwknpsZERVhUUO0pjmrPdVp7v1AoIViCfIIdNjxxlCYaxXsHLpQzaAXomXlyOAaY3HA8abqIfwhYb5lDZ1Kew3TwDLmwHsmCdkrvAVeBbprKtX-dOHXop0g3soItUznqNZUs2TTFZk29Ly7SkxLQgPz7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 553K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 11:37:42</div>
<hr>

<div class="tg-post" id="msg-101286">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEFY4k7AyMcaqC9XvMANfA4QVDuV3-2BuhZsd4BDYdKLNTULS2bKZs1bY1HOKuKPTDmNk1mnxb6LakD7w4fkP5pb6psV05fKUYTITfyvMX0oXVp69BJ105OwVdrtOyV4HQ-B0BTaAmAFVR-t1y0Sd4I9Uk_bw5gnMC9zLRtu_L80-DYubgJvpFTDI3j9SRRW5HYT_IXfXr-GoyPyvUIN9zsV3FeTXdyygGVcvs0fq_sKnCxxd0a7zvUBCmigJetfo1iTHdTn6HtGxDlD-Ba2_ylxqY075Vwio6wBamjHWIaOMw5AT_Msk4XtAMUH3cuI8yOPAJsC5M0DhWVqv9lwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kj4Qw0f-YJbMRcF8z7RliHV5UVsfIMA7aARNSzLsSTzgva5bliCn7ShijXcsXJDGd2XyqtQfQrT1Vlm2I3tHRlxszk_lBu5t4v7D021vysQNRos7AOKCD0RMwa2E9hUNq2-bc26uu61m_7WdqZM6mZR7oku9PXAIvks27i-1YF_4-6bH5tC99ZUGCxkJVDrLoQ8e2eoATJVlBu7ewkL8Q0xa_QLtgbWcpbZ_gy92CAK-K8mmo51xt5j-sh4l1hPuMnuLJ2vp9gBuTcCagBX4lEwgrwjy5Nl68gbzGlRl3SWkvYbThtjqIGC-QcaawTjFyU6OWOkmBMThN_wwftZY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUoJMoe4vKsibKysbsFnGO3Qzwbo_wsVsvGPhKKc8OlJgp6VxAvUL3xVXZHLSSE-50pWGZgmPyauamSOBHvBV7Krpk5qhQG8uGiJ9WKG0JvNlJTCvTdYOOi9oIZtp0i7kAKvutZSlRTDmsfchqivpONXlg3gYK4BPTE6EevQJc4AoXjTEMNmq-BJ_PslxC5h1bZh_32_uQeZV87lMWzdN3hqRN5OLJx8-gqPURH2Lx04qC6PLzTweZ0PA93d--rdg4JheOpYsPLQI_98bRVAIDV0b7irIpMWf2bl4T64CUMw-VyCrOev3XUkkLVplfzh4pyUzGrYbMECdU1bJuxxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9XP-UaRMPAQy-VggKxZrirNGZV-yhTSF8dLsaSAdXXy5wNzKlAuR-Axwawv5RJxEMkPIUsF-kmrmHDSVMHwDaLNrKIFzFIJ6l-Nzi8z5snAYnivaQFsq7dJCgSwbPy1PeIBPAyDiTZUQSuyaFWIYCbUcyB_XX2YzmXXzo_n2MV12-bKYYcW-e6T6imFYFhY7t0uGI9-U3i_5MA-uAaNnlzb4gNCnHar3fe2j_I02GoOH2QTOJBUx2LY_veCjnn7Lu9wWO0d5cyI1RgyOdtzrnsF_XVwg-wnMmUt3NP8riGkzJnP8-Kq5AwIwwo_Nnf4WVRbbKWgJ31EtiMNU67gJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
رونمایی بایرن‌مونیخ از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/Futball180TV/101286" target="_blank">📅 11:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101285">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ff615c2c.mp4?token=X09VqPWqY9pD6m-k1jT7yCrx_Mw2uEe0o1_V8t5EMLtXWjKw44ysZSPbdC8q9-cn6y2Hr5suLQXcZR50LCgFoWOhB8WeXQJMw5QxcmSrUuwmMKT9UX0RXCiUqSr205pSfqOZfzWY1uJCodJepF-hr48M2traHAVHTmPTaKgPpq3ZgAGLAXznI1glRO3PawXuPpjKCrGU30BYc3h_qCIyUFpEL0eD1gsnZpp-u6TQUdFeNYkvKeqcXlqEriJiOJM7R3lXBD2Een59AAZLqlk77iH4ucuMdXqm0Pf1htUkHV163_VLghHnKh3NcgESLL2ypEJBr1TLMQei0FweaAHSfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ff615c2c.mp4?token=X09VqPWqY9pD6m-k1jT7yCrx_Mw2uEe0o1_V8t5EMLtXWjKw44ysZSPbdC8q9-cn6y2Hr5suLQXcZR50LCgFoWOhB8WeXQJMw5QxcmSrUuwmMKT9UX0RXCiUqSr205pSfqOZfzWY1uJCodJepF-hr48M2traHAVHTmPTaKgPpq3ZgAGLAXznI1glRO3PawXuPpjKCrGU30BYc3h_qCIyUFpEL0eD1gsnZpp-u6TQUdFeNYkvKeqcXlqEriJiOJM7R3lXBD2Een59AAZLqlk77iH4ucuMdXqm0Pf1htUkHV163_VLghHnKh3NcgESLL2ypEJBr1TLMQei0FweaAHSfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچارلیسون بعد قهرمانی اسپانیا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/101285" target="_blank">📅 11:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101284">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e24a7448c.mp4?token=PssBYC_ybP5adwPdqsuA4aoP3SLfjWw0J3bcGKBeS5ydCCl943PjRPhZ-U4xHYY1fW4dyekCHbn2d9jtmc8BPC4FjeYNxke4FLlFxacMRcV_SdhJiBaUybelbEK3wODo87HoIoNsnmfuAJVYdHf9OVxmLIlH0ps6OWE0B1KO5dMp4vdNBWMi6MWZBWCSKd7Saoir4j3i90RFT39hSiRqhHxOLeUdHgQ0lfTOl3CPbziGYsfMBytnwOSyPl3Q8i9RpMFy-EXDACznlbmQmjYfZ2NsyAFx7bXjaRySdDgcLqIhR2ylXh9AQXObVSZAvU1gA7ghEWKFXb2AUBLz1G0LAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e24a7448c.mp4?token=PssBYC_ybP5adwPdqsuA4aoP3SLfjWw0J3bcGKBeS5ydCCl943PjRPhZ-U4xHYY1fW4dyekCHbn2d9jtmc8BPC4FjeYNxke4FLlFxacMRcV_SdhJiBaUybelbEK3wODo87HoIoNsnmfuAJVYdHf9OVxmLIlH0ps6OWE0B1KO5dMp4vdNBWMi6MWZBWCSKd7Saoir4j3i90RFT39hSiRqhHxOLeUdHgQ0lfTOl3CPbziGYsfMBytnwOSyPl3Q8i9RpMFy-EXDACznlbmQmjYfZ2NsyAFx7bXjaRySdDgcLqIhR2ylXh9AQXObVSZAvU1gA7ghEWKFXb2AUBLz1G0LAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
🇦🇷
🙂
مسیر آرژانتین تا فینال از زبان عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/101284" target="_blank">📅 11:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101283">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05de87eb61.mp4?token=f7S8NEZkCGGyucWqu91Rshd4EnpfJH7gIQ4CPz4cXdlQIEoVxuJ3NMk--z4Z22DP374_1mvDL2D5CoeqOHx_rVimwv5LXXsfpB1otGAJQKohl2ZUH956GykTgqCeRYMbHtd5q2L8dJ1Gjs9gO0wesumX_uw6tJEX1ZXwt2HOyuBsXXm0Db8riVcwlu9QDAwbXejklQyiSqoUYA2Bb17Njoocu4PxZgv63ZkqfkcO-xmCh3pGYy2lJrMgzlDmWyyMVwsIVbJaTgHmNkDKZG3YMWURnLUicg2o2IlSkBJocOj7TXpTSPaQTBVXHEB7Hh4PdWuOkVOa9ZuWgl56oZM6Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05de87eb61.mp4?token=f7S8NEZkCGGyucWqu91Rshd4EnpfJH7gIQ4CPz4cXdlQIEoVxuJ3NMk--z4Z22DP374_1mvDL2D5CoeqOHx_rVimwv5LXXsfpB1otGAJQKohl2ZUH956GykTgqCeRYMbHtd5q2L8dJ1Gjs9gO0wesumX_uw6tJEX1ZXwt2HOyuBsXXm0Db8riVcwlu9QDAwbXejklQyiSqoUYA2Bb17Njoocu4PxZgv63ZkqfkcO-xmCh3pGYy2lJrMgzlDmWyyMVwsIVbJaTgHmNkDKZG3YMWURnLUicg2o2IlSkBJocOj7TXpTSPaQTBVXHEB7Hh4PdWuOkVOa9ZuWgl56oZM6Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
میثاقی درباره عدم پخش مراسم قهرمانی اسپانیا: «حالمان بد می‌شود وقتی مجبور باشیم چهره این جنایتکار کثیف یعنی ترامپ را به تصویر بکشیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/101283" target="_blank">📅 11:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101282">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iunm6RoTbQh97nugA1prLr98LAXpdjtlkJ-we9l8vK6iGiGbiHVLwiMlL4ewJy_7BQPWg72F_1hmALPCytd6AhiiqWUoqMy3iuZwuUrPeFhbA5P0N2T4OtOlZXEqIkslC3NtV9lhnFwFEmwil5x8St2FS51GGh4-aMMyqbZ_i4mCXD9P2O5WEfovm5FqvAemgXtXfLhofNJOJnvCgtGzjzzzxT2djvoOqSClzrlVruDG7r_Q2TAyoT-Ga2LvRx8B1eJHFS3pQuKUOUESxF0FdXN0HvGCSiylFmw_P2RUHEmT2CYlrpPIbBMdlvnEn23vcDSzxJ5YH9UcW7vRKHRUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لامین‌یامال هم سیگاری شد
😆
😆
😆
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101282" target="_blank">📅 10:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101281">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAMdT56_sH7W3k0rjIeUlhbRxnO3YiC7Bu_U2goXp8cVZQbuZ4pht_uEFMBTOrSQ1z6Sxe7ZrNbJ34z5AqZczbqF4F71CtK_tJ2DL7_qw3VDWdNtjDGPtboxDz2tpxppPCaXDK2cdH8RXs6jfZUkKaauyDa4cDJ7tFL2R29s4el5k50Gg1-GK2vtUdbtEu39rKCkHCSYEylc6TeRqwNIPxm1O_S6hmAQrcVhYsEifU8wkhlgM98gT8IMv6igbYWdf0ak1KJfPXFTdGZhJMxNnF74rba3tJEl5gtHx06N52vEvF1lOBtKKvX6cN7wRP_fKC6mAsY-2wwP2i7m4Q7JWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
🎙
دونالد ترامپ:
"این یکی از بزرگترین رویدادها در تاریخ بود. هیچ رویدادی مانند این وجود نداشته است، نه از نظر کلی و نه از نظر فوتبال. این رویداد چهار تا پنج برابر بزرگتر از هر نسخه قبلی بود که توسط فیفا برگزار شده بود، و ما به کشور خود و به تلاشی که همه انجام دادند، بسیار افتخار می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101281" target="_blank">📅 10:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101280">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28c62d68d.mp4?token=ura2guB4zpN3srfT4zcxoAEsDJvSpU5-DSQZXzoRO_LeqClU-61xWQijlGZsvp7oFszYKKe_gIdBYNOQohDtbRHGfwYjL6QmIddW6g_1M7Zxfd4S9Y-1Z0YifqcDub1JkbBh2YX-JVDdVhpOJR3_abzoyaUaqhFyrDRZ_7Hh4puk6D0Sho-A-nc3O5K3SF7TwNd14BwEUKgfJkvE5gcB4du2mMzMER4Z3n_P9xsMe0jJ1lo1GIAVASnPw-QVUc2gYyRY6KI2VAaL2ORCI7HLTDwW6_Q-Qa8cqTYlWGzQRtojswD-5n06ZwCPWF9gnYf4ezINDdrh4bhDK4UYi-BS9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28c62d68d.mp4?token=ura2guB4zpN3srfT4zcxoAEsDJvSpU5-DSQZXzoRO_LeqClU-61xWQijlGZsvp7oFszYKKe_gIdBYNOQohDtbRHGfwYjL6QmIddW6g_1M7Zxfd4S9Y-1Z0YifqcDub1JkbBh2YX-JVDdVhpOJR3_abzoyaUaqhFyrDRZ_7Hh4puk6D0Sho-A-nc3O5K3SF7TwNd14BwEUKgfJkvE5gcB4du2mMzMER4Z3n_P9xsMe0jJ1lo1GIAVASnPw-QVUc2gYyRY6KI2VAaL2ORCI7HLTDwW6_Q-Qa8cqTYlWGzQRtojswD-5n06ZwCPWF9gnYf4ezINDdrh4bhDK4UYi-BS9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
تنها موقعیت آرژانتین مقابل اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101280" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101279">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf91e3776d.mp4?token=SPTS2BnQKeQ-qSQd4oUtQrqqnz2Y3TwyFT_AQUDxzEhaVrbgo2wn6Ocwc-xq4ro2D3SYA4auahyEwzv3RgnngcNHRZQy9zG6WH0xl0Z42E16oLuAhwGwfSse6cGsESlWmLbebRoxpwgG_ZW7-_3RR6bSlY18FdYJjn-AqcvtTYzSVXKiWATVsLrHMHpBzsQk2qFMwpMY6KPN_GtDYzKGE_FhMslH_9U-Xr_eD5QIPWMkPc_SccqmjRMsKNoWQlm9zEEBL1ur6rI6vsf5xOL2NdizuTVGTSMc1aZYmRlYh9DD0VdGZdwHTuT642KKN_kvSeK5iam4mhZmcGBaQhBN4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf91e3776d.mp4?token=SPTS2BnQKeQ-qSQd4oUtQrqqnz2Y3TwyFT_AQUDxzEhaVrbgo2wn6Ocwc-xq4ro2D3SYA4auahyEwzv3RgnngcNHRZQy9zG6WH0xl0Z42E16oLuAhwGwfSse6cGsESlWmLbebRoxpwgG_ZW7-_3RR6bSlY18FdYJjn-AqcvtTYzSVXKiWATVsLrHMHpBzsQk2qFMwpMY6KPN_GtDYzKGE_FhMslH_9U-Xr_eD5QIPWMkPc_SccqmjRMsKNoWQlm9zEEBL1ur6rI6vsf5xOL2NdizuTVGTSMc1aZYmRlYh9DD0VdGZdwHTuT642KKN_kvSeK5iam4mhZmcGBaQhBN4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
و حالا پس از ۱۹ سال، لیونل‌مسی ایستاده قهرمان جدید جهان را تشویق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101279" target="_blank">📅 10:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101278">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3de45ea42.mp4?token=QMznZvLiyrIF8XPBYreCqkarGGZbPQz12v5WB2VRJ5by23R0uCCMCZfux1eXwUdRVsRzXyeSs25Z7tQb0iLt-_OwuLJ7o_b3W-1jvxkWmrFHx3k7UaFTt7eqvcFaHpIVUcd9FbAvjXNFPF5nhbjpYNpSjZbqhoKcB_oYIQvKHZix9ivXHfQk_00YU7WLxGptpIVBNBfsxVrbOaEacy6uR9UW_IbgfMpFGtB5o7_G7ErrfqjKxeD5u6yQfQyCuoH7oup1zWrYKoeqgP6tKo3h4JECAYWgg8zwlNK3ymUOpLOhsvK7XI5RdqlNn0c4xn9PdTjRrduZsBqUqEuLNEoMVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3de45ea42.mp4?token=QMznZvLiyrIF8XPBYreCqkarGGZbPQz12v5WB2VRJ5by23R0uCCMCZfux1eXwUdRVsRzXyeSs25Z7tQb0iLt-_OwuLJ7o_b3W-1jvxkWmrFHx3k7UaFTt7eqvcFaHpIVUcd9FbAvjXNFPF5nhbjpYNpSjZbqhoKcB_oYIQvKHZix9ivXHfQk_00YU7WLxGptpIVBNBfsxVrbOaEacy6uR9UW_IbgfMpFGtB5o7_G7ErrfqjKxeD5u6yQfQyCuoH7oup1zWrYKoeqgP6tKo3h4JECAYWgg8zwlNK3ymUOpLOhsvK7XI5RdqlNn0c4xn9PdTjRrduZsBqUqEuLNEoMVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نمایی دیگر از جنجال دیشب پاردس در فینال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101278" target="_blank">📅 09:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101277">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNhOG2PbQ5hyRIYFQZgIe8XRSRUwPfUo06bT-BTDp-2njdoI-pRmYc5sjfXuaeUdeMHNzLU2gTYjlLtmFx_nFyjpUD1clJFhmWDR9lJhMg1GR1haqX5zaO3-49HYkVCx-c5nu1-nkRHVK0U-4yvX8CMjhl4zSNbUlCBRSXojR-15mI5O-cp2c5Op1JXSMXxCIPTNL-j4sqCaUI3YvFLIf42Ve5TMxEyUukJSNDfvw3RotfrXR9YyzioP-QwGATkQtcE43G8ZqTCHvbyj-y-J2NTdgJ-pzsz7rPYWoWg0BnYO8wbncQggh-koY-aGe3LxKaVV_mBP_kPFC6K0157nXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت دلافوئنته اگه تو ایران به دنیا میومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101277" target="_blank">📅 09:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101276">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d46d00d3.mp4?token=BCG0O0nrX34GtBnYUKia7zSv5TJmim_fA6hPojGL0LbbX1WA-Puqcp8yBu2nT7b9bpwWcZcXO-inLNn8sFrWqLmyW6DncpW34CqTFJ-fGGVXj8OpcOUXyklvXc2Bl8VnJJypBF09odWXeCr_NY1-i57IGAjba6RsLbJwQGdR3MZLEhH2tZQv7OWdSR-x5rbAfblvOdEiakvusJY2ta6hAyLx6WR1K9y00mwapvFl8wTKIqd5GDZfe1o6qkPpxZPCq0vmvakYxqg-OB1l6lCTpIiXAHaIoPZzWpXTJ7dEw7t6yOsYIVPrKjMLrrilYBUzvmUQOd-qIpI_P4RzDpjTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d46d00d3.mp4?token=BCG0O0nrX34GtBnYUKia7zSv5TJmim_fA6hPojGL0LbbX1WA-Puqcp8yBu2nT7b9bpwWcZcXO-inLNn8sFrWqLmyW6DncpW34CqTFJ-fGGVXj8OpcOUXyklvXc2Bl8VnJJypBF09odWXeCr_NY1-i57IGAjba6RsLbJwQGdR3MZLEhH2tZQv7OWdSR-x5rbAfblvOdEiakvusJY2ta6hAyLx6WR1K9y00mwapvFl8wTKIqd5GDZfe1o6qkPpxZPCq0vmvakYxqg-OB1l6lCTpIiXAHaIoPZzWpXTJ7dEw7t6yOsYIVPrKjMLrrilYBUzvmUQOd-qIpI_P4RzDpjTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گاهی فوتبال فقط یک جام را می‌برد، اما بعضی بازیکن‌ها قلب میلیون‌ها نفر را برای همیشه فتح می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101276" target="_blank">📅 09:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101275">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a634e3021.mp4?token=sTT1u_MPVTsjWsarT4D4e3ELrzOXQ_e3JVGUgJp7mjneJbGfaoEy3rRfor52q0Ik3p1n4TNG4hcO6Vs0iorJnQ_9LqeTT8GRFpqaqSxYSne7DyrDOiqcoANgbgYLF4ltPHXH2SXIBqzX0MV-_3iym5LOiSJjHou_UXXjB_sCtUBoYzLYY6VIaMnC8jNuV6FNoYGK_H2S-YSQYlW_SRTvy8rNXbdhVPfcSpNbIPev31Ec1VqmEdmAw0CWKBhkQeG6kAlaBtdzu5eKvigAq2rAQrlmFGA7l6N1SQKsa8_ZZOURA3l7Jkzm2akkGHVeGAUt-tLULRVRZpO7UQEnv-TJh3crATzwkkM4-u00L27ZMV2nMDEkc-6YnGRTodIluouJ1Co7NyOO063WI6-NzcYH0FhWcR2dfprQ8caUezvWdCc76a_Tf8UXg6wiDMUVYSu4gt7C9xf5hNSptdFDD7L_R0fCb5hM0iWmQarWrUyXxrZ6J0tfc_duJ5Dt3n1nHKMyeUBGZdWqE2Rz0yYtZ64toq2BxX1aAW23y73jY2L24hk0KZhdtB_6_tscHVH8UQLLkZpy1GWsvsePyYmo4s3h5rK8RLmhd_Icma0w57NCh1gI2XwuagyayDlmd3rGp936ylKrcFIBfRhR6dwXYZJ7b8E0X81xwdNQaQV3wVn0MNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a634e3021.mp4?token=sTT1u_MPVTsjWsarT4D4e3ELrzOXQ_e3JVGUgJp7mjneJbGfaoEy3rRfor52q0Ik3p1n4TNG4hcO6Vs0iorJnQ_9LqeTT8GRFpqaqSxYSne7DyrDOiqcoANgbgYLF4ltPHXH2SXIBqzX0MV-_3iym5LOiSJjHou_UXXjB_sCtUBoYzLYY6VIaMnC8jNuV6FNoYGK_H2S-YSQYlW_SRTvy8rNXbdhVPfcSpNbIPev31Ec1VqmEdmAw0CWKBhkQeG6kAlaBtdzu5eKvigAq2rAQrlmFGA7l6N1SQKsa8_ZZOURA3l7Jkzm2akkGHVeGAUt-tLULRVRZpO7UQEnv-TJh3crATzwkkM4-u00L27ZMV2nMDEkc-6YnGRTodIluouJ1Co7NyOO063WI6-NzcYH0FhWcR2dfprQ8caUezvWdCc76a_Tf8UXg6wiDMUVYSu4gt7C9xf5hNSptdFDD7L_R0fCb5hM0iWmQarWrUyXxrZ6J0tfc_duJ5Dt3n1nHKMyeUBGZdWqE2Rz0yYtZ64toq2BxX1aAW23y73jY2L24hk0KZhdtB_6_tscHVH8UQLLkZpy1GWsvsePyYmo4s3h5rK8RLmhd_Icma0w57NCh1gI2XwuagyayDlmd3rGp936ylKrcFIBfRhR6dwXYZJ7b8E0X81xwdNQaQV3wVn0MNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو کامل‌تر از داداش یامال در جشن قهرمانی اسپانیا؛ دیوانست قشنگ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101275" target="_blank">📅 09:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101274">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWAIn89VfVWgNN9JozekdpH0aDtenKbtLxElT27qy1KVypAHruFaPO_mpO9bEFnHE1x8DaSMwqAdT_OCrA6PKl35dL5BLvxbK_qJkD2lV6HYoBM1XDFgfkqnnHna2LJNzIwvdPnTJgmiSRQhSDHAISOH56eDkCEqkcEJfylIaOh2SkVHdtXO6Esxchd7Tk-akurvUNMs59VW1Rk_TL9YO05HRBHk8qGPBpk4--nxrSB4UUi7BOsmkTA3BLJq8rbYsbesGWf6ESByrLYL0X9PFtSLARmsQWbuUwV7cF0DPXhqpIqcoPLwiPrm14cYDtjz63Lkq1bdEykvORjytvYUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
رودری یازدهمین فوتبالیستی شد که قهرمانی جام جهانی، لیگ قهرمانان و توپ طلا را کسب کرده است:
🇧🇷
کاکا
🇧🇷
ریوالدو
🇧🇷
رونالدینیو
🇩🇪
فرانس بکن‌باور
🇩🇪
گِرد مولر
🇫🇷
زین‌الدین زیدان
🇫🇷
عثمان دمبله
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بابی چارلتون
🇮🇹
پائولو روسی
🇦🇷
لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101274" target="_blank">📅 08:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101273">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deea9feba7.mp4?token=YwmpbZNqx5ZpHEYM75ctK3zfSuHdTwwot6grDUmv4v5QOnw56-6sRxCet_FiayCgGHsLeOFg6iJl-pcv6P3urbQSvFmyVcovm_vew72Q__NhwE02671w5LASxmjmNqnLiR0x6GHrRrVHurV5J_oVaYyKDSbwtiqUwSahzkpVd6ikdMz-NfdrqnMQbUEaAtV8JWm40I_U3jKDv9gWRJK2mJEyFOwqxzcuQZvlEqnNmc4SoQA_NZ3b_aA7OfbtzLXugbpYvrjO-xOdFCxCkzr3cEaSM1qZITS5GmTilAPQwzPFAAlYoa_0kh0t5YkVt3-Kv0ThpzzdywSIFZkcI0e-KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deea9feba7.mp4?token=YwmpbZNqx5ZpHEYM75ctK3zfSuHdTwwot6grDUmv4v5QOnw56-6sRxCet_FiayCgGHsLeOFg6iJl-pcv6P3urbQSvFmyVcovm_vew72Q__NhwE02671w5LASxmjmNqnLiR0x6GHrRrVHurV5J_oVaYyKDSbwtiqUwSahzkpVd6ikdMz-NfdrqnMQbUEaAtV8JWm40I_U3jKDv9gWRJK2mJEyFOwqxzcuQZvlEqnNmc4SoQA_NZ3b_aA7OfbtzLXugbpYvrjO-xOdFCxCkzr3cEaSM1qZITS5GmTilAPQwzPFAAlYoa_0kh0t5YkVt3-Kv0ThpzzdywSIFZkcI0e-KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیسی که داداش یامال با جام گرفته خداست
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101273" target="_blank">📅 08:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101271">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGtHg_3-hYlmNoIQgV1wbyTD-RvAvNMARR-hwb--1tPTBdJnV_kU95F9Lz-y6ABP2BJp857N75sCLyng3qQg-VK-i_kL4ky5Rpk28luBFG5IZEx3K6DHQx0dxJDHsc2VM1RCIdBH8aql8NCcyfDflLAx2u0t6U6V4rJnNNEY0xP41us8x6lQMwSIFQxjYg9twWniNfMMk96CkAAdeAYP3w1fhtMraH9U9Z1KSI0-WwOpEh_h7oGy5JQ9mm-SVjBe0lS61vSF79Ub2doQgMJL66Yc3zLeVkqdiftyZFvyIM4ywiKA832J36pCcnwY2MQsJ019VyLF-WcYEXbsSkiIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6CZ3NYUrDRXMWsr1C4Q2e-7C4LFjAZu_CqHAIGPeIKzJO1o3fggCGW25BLY7tEZlnc8O5R2EwZqOyPeJvEeBk1PPBzrBAZRkx1L4A31Ioq97eEAFdUhZ1Q-h8FGt0cMU2OX8TGf422tC0XGuTKs-jEafiQRj_TYtq-9Le3UX14XlvFlyFbhMC_t3FpxPm-7dnBZ70dfIViW5alGpEbpx-TY0idPb-mDBXc9fpAhRXCmXtfJk0dm3OxQtozgF8WCHgZl52dKkB8uTxQT5mgQmsLa7hhvSp3R_yVUqUPgnqLfkWyBeRoPxCcKiUUjTz3ZGvp476hOH4x72I7uy58bKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوبارسی و بانو تو جشن قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101271" target="_blank">📅 08:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dduMp1C1vNt5sNL4lFbfaL7HKX0p8thNnFYjAore5ZVG65hso9hzpsi8Y3S2YaUodYBzz-JXHzc1jQXXtjElcogD6wL_nAc5K_--Uu0VilR0gBUU9g8TTkUxHxN9YSlklCgQZrMTo3geVLWN2AOs-Dz3FfZYrH_tm8i2fGPVp53JTsQIToTCEwa3Ig0-nBq2jzUwsR4K6bey5JLUGQWtAu0ZywdSLI1MER_X_hmN7CnNZBrIGpK0NgOkD22sd2bBZ2qPF6--aqJDoHol2uIkSsv1d0T25HtKNW0J5Bq4XQCC5yQ3lbsB32Ux-xIw2ztnDJs5KB2ays8HYqLkKhM7ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3igihZbxi-B_HTuO6_EERYYGYX6DAhDfJVh6-i1JlYJyH0Lpi_Zt_Y5VRxlWCdzPWnS_zK5a1ah6dtxCrRJRyDyiTSDVTqhGOEYhdp2Yml69nr4qV2F4ZDaIBQbKpSH-Ak7do6pqPJBVbEMynngaqM0NDSlV4xe399BLKrWOOHoS2glxWRn5s7P-4S98TaC4SNBeIPqWVEQDL27WDlXlmVEjjgD9RUrF7kSOLYmEFM1a6gtPgOx0PVvSbIwHt1aPh95SAJxmsZ2MTD_a9QXsfMkja0DE2H7DfwrkdMzpyM_5Uay6Hw9pDWLPSstizTauS5Lo1gBjdLPh7SUNLml6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCwLJg8srAZ15NLc3YYij5FeVuMil1C8htCvyQ-tfJkcGx6zpoBF6zvrrL0T9C4BKBztB1NDb35fwQb0RoYccAyZGBvZFrUV2MQJwfgZUwxF-1P4A00HRXcN4AFwgwVFJFHG8arz8D3x0G8YqLwbjwN06mPJzVCAbWZ3_OirzCF-Wp1CHNlGZK-855NM5yBf5lwn3W9I5QfrGCTHiFJOMzew9q4czYhLUBvp0e9K_7zG5sFQg3lEfzRuZO9jG6AUpnLIUN7Is5LlnI-kUQ8MjRTF3C10D1x93oeCq3gf28nzBRXGlcC1mRh4FEhVGIeOa9-UoxHtDprMOEXeouZIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKWkTt6VLbPucKKrw3KeOCUGCsQjMOulVh8BAKH8z11AedycoKVoMxdlVkDXLk17UxtG8c36DI-pZ7ljXj4SmN5J26DG_hAcevVh38WcT96ArJXjicWz9SCmkQjqEFA-1edVKuCwcBPgmm_GMCOj4TMs-teV9coA6bKX7ka64aPc6ine9MRoVRnD_nG01ad8HtbgLnhFsKO1mA-FCMmvVAHzzycP82MNh0crqaQjdH1mpMP630X1ooRkwJFAUrEz8lz9Ll7rZN1gJxvqZ6BFnNq0ZvrS6BCVtsdalo0BaPufBhMetERQB3NiJJHpbayChWIorHweUPj6Wxr4e2kwFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینم چنتا شات از یامال با جام قهرمانی برای نیازمنداش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101267" target="_blank">📅 07:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dd52c94d.mp4?token=JbuZ2ku1z6evfRqA1boKyjNL2GZg551A-i2rvQLYu2I_-u6U7c5umlu_1RtN0Yf0E4uYdjryCdjAQK0COtwJSX4-FJQHnyusip6YfGqu9CYGNparQW3Dc-ikHRcGVJCvr4-eFBdyFXtBNKwFde1qXEHc45fLtN_5rBOkE9hlWNfy9mDkC92RHWcM5znycHfI93t_7nIUvAEKT5N48hGYMKr0DdbD7Gp6F43vhACHEbrIel-jM9J1OeasrgBWo5RKfqkSd_enc3UdZOgnthLhhDymftUivn3An6H0zjQSA91YtLW8pxocJmu4onFsroEkcYo85lXjEQIyQ1NM5XYiaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dd52c94d.mp4?token=JbuZ2ku1z6evfRqA1boKyjNL2GZg551A-i2rvQLYu2I_-u6U7c5umlu_1RtN0Yf0E4uYdjryCdjAQK0COtwJSX4-FJQHnyusip6YfGqu9CYGNparQW3Dc-ikHRcGVJCvr4-eFBdyFXtBNKwFde1qXEHc45fLtN_5rBOkE9hlWNfy9mDkC92RHWcM5znycHfI93t_7nIUvAEKT5N48hGYMKr0DdbD7Gp6F43vhACHEbrIel-jM9J1OeasrgBWo5RKfqkSd_enc3UdZOgnthLhhDymftUivn3An6H0zjQSA91YtLW8pxocJmu4onFsroEkcYo85lXjEQIyQ1NM5XYiaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
💔
اشک های اسکالونی در کنفرانس خبری بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101266" target="_blank">📅 07:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101265">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b524eb5176.mp4?token=AItw6xuStTZf0EGLSdtMYS94jl4Eo67Pxfvk00shVL0lGknZvaPXCVeobg5YCk_lrJaPOW-mC4bGwCTAyEdk9bYAoDv04fU06fW5Mho7gx49JLGbSmJeTVv_3702StyOYgmbswAhL6svRFvRV5n77dWmuELpH8yIelCc1pAcc5O7ZEVnuOY9MgznjUMLx3cJgM0rjOfpNFfEsFMqhZXvtSYojx8wM2eGiO437FUu_m83hA_WILqniBtYkC1hNy8U9q7csxf6ZOZt1rMvmi0gK_NaRnVWDgbXdkZrKVWgOWkhwGuQxPG10sGUfWMMKPBA4INkzLahNaAB6GTO1vU-9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b524eb5176.mp4?token=AItw6xuStTZf0EGLSdtMYS94jl4Eo67Pxfvk00shVL0lGknZvaPXCVeobg5YCk_lrJaPOW-mC4bGwCTAyEdk9bYAoDv04fU06fW5Mho7gx49JLGbSmJeTVv_3702StyOYgmbswAhL6svRFvRV5n77dWmuELpH8yIelCc1pAcc5O7ZEVnuOY9MgznjUMLx3cJgM0rjOfpNFfEsFMqhZXvtSYojx8wM2eGiO437FUu_m83hA_WILqniBtYkC1hNy8U9q7csxf6ZOZt1rMvmi0gK_NaRnVWDgbXdkZrKVWgOWkhwGuQxPG10sGUfWMMKPBA4INkzLahNaAB6GTO1vU-9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
کارلوس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101265" target="_blank">📅 07:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xd_RNN7XnSG3naoS6PCabJxGQUIHHS1UpsA5pVzq_szG62xoMsl2S_nIO-HzITcNRikrxIG-0qm_IQrODH33vK-al30as-nGni0GtmSxl-HNXBN-Yarh76tXVg3Q7Im0dCArmQAqSUQpArn2Su86rGJSBuIN2uAQBCjE5SNmPLCSiBq-sKpYKZkr4dJEkPj0mQ-eb2hi4J6Kpjcj1nFlq0EiwikxTAXR79J1baN3czQh42CicVOG2kzBhznrEp_16xP22Tj56Yc74eNk66cqTzPWr0zq2NmHg-rdYlAtJAeM1YBboqTeqMh2KG7tIFNFz5vIP1FYCs8Ihq5t_3Rv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORrxScsmg_tuDb5fMubRuioFDBDdX76mss3btk0nUtpnWx092jsl_atipOSSghcZQCebVfZ_0oVUlo-bJPGwIpSEHwYTwBnH-jcBNzvfdkniG6TgprU4GvNiKkYwRfuGy2P40Qk9JEo6QKjXRLsuz00b5SUudLioYPzZwENx0S2eEZrIEW8zI7mm4VtjDGNcj8gakoyM4yEd_BB-6A_SlsM_iajiA8gRYsh56TDPeCpsgW3mhuHQZ_AYGsDP0kFr8jMs3M4OFonOMOysk-qKhDV6q7jzvned3-JiQu52kC8VB4wvOy6ejcP3wUMfsB5oZkKizBqJu787qWFbiDfaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUO-B7n8pN1ts3CAgFg7EXHNNuEvSkT3LtqnflWXEPtri8vdBKf67RJa-egooFu5P8Yij7iTeUZhdshRFKdEP4pGGLIo9kuGzHw6BHS8DzsCXPag7CjN5gMSIf-FD_k_Ll98U7I1WJpQIw8vU2yE32DRtH81bCEgVHDvB4YrS-pdB0in6IAyjXees6xioezriqbqAp0s4Ik4ez_yvThE0eqHjXlr7Y8BsNVyNk6GXr0FC6eOOK-trDM0SkD6jsZpaTwioR-PEuBVUhjCfmdvLsuSYsHfggAdlD0O9ubEpMbtXL8Dl7wxRnt2iPNWqezJVhwDnL5wgBSNivrUg_HyKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
❤️
مینی یامال برنده ویژه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101262" target="_blank">📅 06:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de2eAQa3rBjUwopBkztf89mAJx2iHny7pAnzOOdbv-aHuOEVqh9EjzcbVijbZVP6GNvD3ydAZ5V2nqSi_F89haA9xKKxeFS1URuOZtXh5cmzS6yZ6oETa7iTm2KVSFWkotiveIPUd8S0TF5On34eig0RI2rerZPViZzo30WIIybHGJqvaUMlarQH7iEMfScOaypeXJmPBHTy9igxn2HEcrrvPdmzwS7xdjnfz0IhsErDclgtKqvdQbBLIuEbl5SkOUUA53FNJ8yFyIS0JP6XL43OFzPb48bt540TbF7nkfI3dkuBRpARd80PTML3HgD5kQsON0zHwqZbp5dzRfCV5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
میکل مرینو:
هنوز هم در شوک هستم... ما قهرمانان جهان شدیم و این یک دستاورد بزرگ است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101261" target="_blank">📅 03:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101260">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zba613CbfcJUgvzoFqT2npqZ3IcsFRX-kjhlsOsF2NOfngauUlcQiSo0rdahCPYtXUhvUJ1-rsWH3tchJ6IAVZ98Hz7H1y5kTFpT8qXSNfY6OeZ9shAj1dSvEVCw1oa0het0E4Mz737GSegX0Hxyk-ty9UyE1lCdYZqX6zcaaOo2hcOflHSrDHvaiN95qsxfxtw87jjfAnuFGMWEolzRk0bbPcZjskVCvsiWPs2j3w1E6CyNzKdkEp5NpwiUnEaLXANEYzzzXYlt1gzKDQCCQQopUQFgWusyu-CXjheTcifXSp1FikZMUbdnFMGYfhPpFPMX_PisZXVNkvv7knDXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دلافوئنته:
رودری بهترین بازیکن جهان است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101260" target="_blank">📅 03:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101259">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc89e4277.mp4?token=P669ZlFcuCalNTQcy1OJ-8op4Aab8DYa-VHlgDkhB-W4qmEryBdQSwEn9Tpy5rFoiUqivCmA3jYrQdzaFrtYGjviVqpxpKyNNCypDxKOpAdz7cwyIo5szTyFykccIAjKiQ7rEG2hz4wpRj-dnV98jOhytIzEg43qDLCbKlJLGDUWbawPnDQKMaVP-iHhiEgtubl21B6SLZMtUDOS5E5Op81ceSvEphiARt-6QAleE6olVNxLruzNSnvV-X-_p7qzHIf0koag-gEl2GRxp2SbuYv2jWZNp0H3Y8bhdSjF8OTNdzc9ZVZXrFklq6i4DRX6aiaipVTdrJ7uyj-m7_9aNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc89e4277.mp4?token=P669ZlFcuCalNTQcy1OJ-8op4Aab8DYa-VHlgDkhB-W4qmEryBdQSwEn9Tpy5rFoiUqivCmA3jYrQdzaFrtYGjviVqpxpKyNNCypDxKOpAdz7cwyIo5szTyFykccIAjKiQ7rEG2hz4wpRj-dnV98jOhytIzEg43qDLCbKlJLGDUWbawPnDQKMaVP-iHhiEgtubl21B6SLZMtUDOS5E5Op81ceSvEphiARt-6QAleE6olVNxLruzNSnvV-X-_p7qzHIf0koag-gEl2GRxp2SbuYv2jWZNp0H3Y8bhdSjF8OTNdzc9ZVZXrFklq6i4DRX6aiaipVTdrJ7uyj-m7_9aNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نمایی دیگر از لحظه بالا‌بردن جام توسط رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101259" target="_blank">📅 03:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101258">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV3RVpG2JGZc6W8XGjw5Xd9DgrL4FptYjsvUuNwqX08UmmxmLcfpDM5iZfLRzmp2G0QBEjIKFTdD4zORiBxii6azdDs7Eh5VAbCems6Q5LJY08IRTXjOmre8EeCsqGYIG5tAoqQQiaCTDC3pBWl_Lkl3jPuFerptS84XByeRHxRwX7YwSmGZEC-bD-UXCOGrv4DFC9ka3EgQ-VAziV31BDpSMsZHij_Y2dv4SAUgCMRovnwjZVJqoauuTjbdnvKIhEVfNlvfPyeG5nUjkovqPA0PzE-hBp469r-_kLgU9MKHeYoshcJprl7RM4Q_nOVhykvdaTIAunE7eK3ZbQ90ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیونل اسکالونی:
مسی بهترین بازیکنی است که تا به حال پا به زمین گذاشته است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101258" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101257">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIm3V-IaoHSPsH8bZCrJfWo-WGfOPk4_MhXsYryT8JAdx20DSVAtaIsl0pN2_qgjEe7lGrdI_Ng4pIfiOoP3VCQH7-9dpdjtQV8F8BBH-k9QUWXSELtUZwojRWzjX8NpNSnqfSb5BuRm1cW6Nw6AFBh1p2Z5oPVZGG2egE63HiRDLGlUFpO072b2VA0zzrLK7tDjhabMVvhPHpqG-uAkMGo-bzeWnrE_BH6haxCM6x133Dud1XJ5QxN_FupYJJiyAhuxMCXGuyqwkmTsPH8xOYKi3cJ6CmuYTycyOmqOnsSuQ2P_wZhHh-UmtWvtl9U0x3jnbQRPt3uz_7_YMv1T9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
😍
لامین‌یامال و برادرش پس از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101257" target="_blank">📅 02:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101256">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wvskvi-bYA-WcefSU0VE0eO-Icat2FMjK1SiX1QVKht0SB5ywMkEvsD73JdvHTFt1PtKYJKhdBcW_LJHkNvm6aCe0liv7GLavwF6oOgeN0BzJ_IyIedjnjlAGk796EUIIoN7KTB9VE74sjjagonb4azGE0uwW6Hcr6uuZ-a__lJOzFHUTAg2J5xSWd8TyFfktFyStRzApIsEuo08YZiaytVhXSxDZppk0H2UV6FpUsyw9oS8_hP2M2iU0M5d4ZoX4cLIBmppYzatpn9sM_n3xVRhWqGzcbsahlvGBHHDvizdpOnR76z2WWR0EF7b4df6SoP1qxlQ6pgdqmdwfj14Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فران تورس:
دوست دارم همیشه در موقعیت‌های سخت گلزنی کنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101256" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101255">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0LpSvbO5KTdSuod4PC1jgy84QmVbrsLzmcH35LrXhGmHYbShnDKZ6uJpiBujokl2BVA7m5mwU_aCTIzZYuR5s5qsp_txkzSlB2GbdkDdpmbbuGKF1x8KAXllgVqCGidQi7UikxJBWAOtjOygHpncuFcOh7RuVPznK4BaK1WTXznLOLmFrvYK7vIL_Tjj0AvTQbQkTjvzqKrlNBkU80pn83kXRcWQ0abE9JPZ0b_TGHbgq3DytN-kKRe16QV2lJNDRgYbedfnRQessNkZhPaVJzFa7Tk26SwjmjBUR_e5cyMdVBZGdtbomIDKhcfflkb8kfKlcnqBkJ-y3QaQYYjOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام: حملات ما به ایران برای نهمین شب پیاپی آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101255" target="_blank">📅 02:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101254">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
چندین انفجار در تبریز و ماهشهر رخ داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101254" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101253">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd06e84d0.mp4?token=nrYMvPPI0e2nXGJjOeEqLlaecUAfI2PWF8l16bPz8MfByxIsPrVhJlcU7-ryl3xMTXTlyQ0X7_9n8zwlEFBQNKrnaCj_ok1x3LlJA1uQofPj6vIRAosTx_g58CdGJzPOQNqrKl7vuTwVFn87iTljdCekpVLMYx0eqLlErq7DqrpJo39FCU-XErliBB4aQvrlhCClLp5gMyui79H73aMHYjPzni276yIHU9eVaSMkKCkP7dxpttZUu3Wf-aoIrEz-RoNF5TGlafrFzC_t3CRr8tyI6Q9LutASKdhiPRL2fw5MCD1hqLkwIYaGAzmbCtCABEfkdiPojzJuTg3JD1lMVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd06e84d0.mp4?token=nrYMvPPI0e2nXGJjOeEqLlaecUAfI2PWF8l16bPz8MfByxIsPrVhJlcU7-ryl3xMTXTlyQ0X7_9n8zwlEFBQNKrnaCj_ok1x3LlJA1uQofPj6vIRAosTx_g58CdGJzPOQNqrKl7vuTwVFn87iTljdCekpVLMYx0eqLlErq7DqrpJo39FCU-XErliBB4aQvrlhCClLp5gMyui79H73aMHYjPzni276yIHU9eVaSMkKCkP7dxpttZUu3Wf-aoIrEz-RoNF5TGlafrFzC_t3CRr8tyI6Q9LutASKdhiPRL2fw5MCD1hqLkwIYaGAzmbCtCABEfkdiPojzJuTg3JD1lMVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🔥
اثر جدید و تماشایی حمید سحری از قهرمانی اسپانیا در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101253" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101252">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICWLXJOX7qc_sv7wPQ67buDgh9FnlGLnloBzfr5bXS5D1J2nY0YajejpNLmoQjfAp4YIHrtLDao6iZKxrdqGmESa-oSYbF28PYhH4TwGkjHd7H7xr8ANunLS5rWL_K0wHH3w-nTaSPUYsrL1rpc4h_prHg9eRMQ81Oqvr76u7nKUQXvS0HfVn-oYGNuyTOvXt498mxBLI8TPC9Re8HW_DvOEIKWNnORBJJvPIaj-p0GWi5PdEWC4G1T0HKEV8m9L6GrwMFXE3cZ7BoVQLTVWGMvlPXbLQtu9SebMgafAwU3kaUppAEDXzT8D8jgF3Uwo73tErqpxc49j1WZa9csRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚽️
بازیکنان بارسلونا با جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101252" target="_blank">📅 02:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101250">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-i7OhIJVZSG5nJd5iPsbCkJ-aNy2lIKb1ITguGqtMHy278mrtxCLMp-iTc1dbH7HvjYnFrE-bSUyjbw8FZcwevYbdeUunOZSrXDdOf-aJ65csJssQOICEb5JjiIbdz_vum8OWoX6GKcJ8_5EtX-_T11kLAQS0old0rMj546uLAlaVLSRCUT33SHAQQA9cyLSM_3cM0bjE_T-yU7JG4tUCFzPodI_hr4JMFxVSbFqBHto9zlaBOxRTUBtq0-xWkDcNl1RsuPrp3fvAhimUTbxhpLr0SsBRzhpTNpU2gY8J7AclA-D6HxSF4hLyloLjRmpIViTZ4DcPSjcpdmwRL4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🥶
🔥
مسی به این شکل جام‌جهانی 2026 رو به پایان رسوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101250" target="_blank">📅 02:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101249">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🎙
👍
لامین یامال: "لیونل مسی، بازیکنی است که همیشه از کودکی به او علاقه داشته‌ام. من بزرگ شدم در حالی که او را تماشا می‌کردم، از او یاد می‌گرفتم و رویایی داشتم که حتی اگر بخش کوچکی از بازیکنی باشم که او هست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101249" target="_blank">📅 02:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101248">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3OaDak62wys9uMtxO7Y_RcPxXVptMyAAtXZQPTSv81a_03b7UjGSPZYvEu7KTLAUgBKMsmpu-Vrq360bOHlfUu2DsuWr2ocjLvnAsIUdKgH_CJ0DOIEAsANxNepDCXYm9L-BkMCC76wDJC_a0tCYk-AyvkmkMtOdjTkGMceuHga3V5kM9gMwDesRx_cpx7t0tDEdj-hn_tYBXZZ8Gr1wJvjRabldWs_7TGNGCONEPA64qDQWKUsm_C2FyogvM3gHBxjbFx6tE6wxvGJSANQ3-4e3-HJXsuFMolLbKnUVlf79Dos6ezhqWx3NV3KoBwIDBev1wQSegr5dD1gQzSnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👍
لامین یامال:
"لیونل مسی، بازیکنی است که همیشه از کودکی به او علاقه داشته‌ام. من بزرگ شدم در حالی که او را تماشا می‌کردم، از او یاد می‌گرفتم و رویایی داشتم که حتی اگر بخش کوچکی از بازیکنی باشم که او هست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101248" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101247">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDxrJ2N82E4vMMofBCBDFbXCg2QWaddjtwzf9zEAN642-KHzeshfgP0ABkGiVZuFCxj2MI9ppMAw1F9z9iGbCNTuFiCSSQfhQ4SlKzgs8vuFudJG2_QDTUXE1eUp8f7m8A18yzh4cPD62roRx9LpeKDpjqgaD6gGvEJVTzHITWanKWQgxOpUAni3Zhm17WmfzxQ3bwsejBnpBYlqGzBt0rLwK9MN9Q55CHPVl3GFiMcIqARpqhYspSBbDT2iSlDCSn4Ep-iWj5XBMnSrAhAIBIoS-nln9rCLGo6PNCWNf64PnIw_SRdICOi98N7sZCMfj33Ooa3H8Rew6XA304Y8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😆
بعد از بدون شکست بودن قلعه‌نویی، ببینید از دومین افتخار ایرانی‌ها در قلب آمریکا و جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101247" target="_blank">📅 02:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101246">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8rpMqqBy00x02ktgNkdasp7DNW5dPoXARMQaudZfyUP-HNwt6XcldBEUJZ11GvXM3mANzI0zCa4yKOSv7retJySgLcyltI_VuUghqUzCu-xqX_FwtNYj5u22908Ta0hxI2ODd5-2hbk7WKG7AwwqXH-Hm_oIub4cHxa4DDrWS_2arVKFVmsqHuHkqavZBaoAnHTSKqP5ZhkcPGcL_4QHaxkaQv06flH0DUZtdSQ8yvHbF0amxfv503b3sQUVvvhdcRR_kAwsBgxOAq1r8WPaa4uolkNzdpmrM_ldO7qz6XK7xmtzgZeJbQxshOQ3NhUsfTOemnvDA0kOFDkL1LVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
بانو شکیرا در حاشیه فینال امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101246" target="_blank">📅 02:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101244">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YoQN0-0953MVnYFUKnnV_BG6ldwXMJ7xmWNDRLXnBJ3MND-mq7UWp4101jx4SgkvG7MuB5krmJMm3sALna8-COkaD78FWjplIinpCA3gK-KWYK7caHSEliFkjRt25tNECAC8dpE7-zdnAd4iJk19PygTtZZf6Pt16fk1Rf6tzrg4xrCHHU2eHJNZN6ArxXbo-9tgjRfYlPaUpuTqWKjfj0van0iwj69IDl9Dj2ujOFOGI5S74z7QSWcNreTgsa9AnXZ6B2i5GUJCr2QR22QIGClbk6DiPVaowVvuYz1uXxRkmtl0Wz4ED0KK7Azxa9Rf-K_zBzeDucqjkRKN4uUm2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzyzvG50nozpkikguuqHnLSzk0Yh9uRwUXuRmn5b-lp1KqWiJ3CiHZZDCcgJPtNgoYLoDO6UV8CjMMh3uVtryCFP0O8r17-kCpHz2RgX65s-lA7no6zCEvmeYOjZx53v8VJcvDW1ICzsnZEhD2jLgYa-e9zcqjWR2PvW22gKYDY_00fNAMbDE7AIO6rl4Ko_23Ue8Sv0LLUGVfcRJHDSzzOltun0dLgbQlc6e2oJUatAEGL0FZzie7XLM_aKkE6jgAlRhDmMeJfnxKNqXO7JyMuXbHqUdCbaWCF75D_ENLgaa0R-pSL0uB-f0nL1ZndJjkBB26xFPcuD64YrOw3Imw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جذاب برای فنای فران کوسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101244" target="_blank">📅 02:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101243">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLn1s3jww9S8fhsYRoXjVG54fplMdcJOgtLuTzJ8wtKtcLptVZmf14kdxvj09dONDjvQl7gWMdKI4x4x_pAEQKvjEHR5_4-ozgnWlsMWiQbjRhGWtuZOQVWbD-NhhIj0MUE_YavgL6wgL_17Eq5LZXD1LCz1EwCdaCO8oL4X2l434dDWPe6EWicrgjN7DyM7XQJT-jpg62FUwHkzuqol-ME-JjnInbi5JETBI8DGtcV-wu-IgppM9eT8cQTifV3ex3pCOX1mHOVpq_ZziiWy2APVnhxBg_NuFsOYMorl9OBbrT3DjzCcJP2rJRPJohupVpiAM3sUwZ7v3VtZqkyQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🙂
بهت گفتم یه بار پوتین بهم گفته نابغه؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101243" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101242">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e244c0b930.mp4?token=NKWHrJw3-UeF-WxFQqcmiVuZOKDWFK7shsjWE1ZBCwuI0Gfk-JLsU0qwNrlbziz0YSaSbLBsrrNaVwve9Iq0SwcPxIKKijMJUKs-V-7YNR7tJPdHYKpz8yy0qny_KJG-9kWAV3tsjIw6QDZNyEFQqEKzqeR1v04xzVO8i2-xQ4UOLJhzIU3ty-92G0pREPeGzq0jwiZBQcgv8QxZNT0_VAdi6_0KrxqTB0ep-MOtEJ9MGV3h4y9JDKK06OO4ZGhe6nWT8wvTPrBhKbDPfutOJXj_wWWZf6XgLLB33K70G7RoeyV-NaTfB35UKTuS5YTbD_5IUj_hNN2AAsQlz8xxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e244c0b930.mp4?token=NKWHrJw3-UeF-WxFQqcmiVuZOKDWFK7shsjWE1ZBCwuI0Gfk-JLsU0qwNrlbziz0YSaSbLBsrrNaVwve9Iq0SwcPxIKKijMJUKs-V-7YNR7tJPdHYKpz8yy0qny_KJG-9kWAV3tsjIw6QDZNyEFQqEKzqeR1v04xzVO8i2-xQ4UOLJhzIU3ty-92G0pREPeGzq0jwiZBQcgv8QxZNT0_VAdi6_0KrxqTB0ep-MOtEJ9MGV3h4y9JDKK06OO4ZGhe6nWT8wvTPrBhKbDPfutOJXj_wWWZf6XgLLB33K70G7RoeyV-NaTfB35UKTuS5YTbD_5IUj_hNN2AAsQlz8xxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب دیگه بریم بخوابیم که جام‌جهانیم تموم شد
🤣
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101242" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101241">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj77c1q9N7bB7UUvNM44E4ugTJF_AIbMbFAluFzGYM-tqBI5QdMh1CaVSVgw3G6pP1h9UXw6JX6WB-xcHL7cR_o0RH_Xb-8eTAWO3DFixh00kdC2W9LgueySvbFJMiw-VSWF2eTUuC7jglUHBcZCsoVdDizWfVqLjk88EXZk6Vcfg7xPnIHYvR07cubqKbZuoBo4bDD-9No9n2WfgcIPAiWwL-uQnEsqSF0Gl1AMxgSzg2Wok7xapw-clgP3DjVE3MG1mLy6irMzllz6mZk3EkqkcSkegby1xz7k4w_4AorfQTLCMuDNcKabdfDKYqC9rYLm9i2nofhFzf_JREBgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لوئیس دلافوئنته با جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101241" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101240">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_YshlcRhBJ_QKH_TMhSqEe4ERQW60xS7VQRa5ZcKCSXu-M7nkWcW4vUAfxqDZS7RZ8HE3-uPSV7VXd0nJM8hh17p5uk5RugdT8nh89nOEg1hZ_q_7e36ob1zJTAFSwsKZJEYC-LSCZ0dNBf8Q7SSEO4zo82M5a04flZaRvFXx-AKFELgRJAnGaPTTC1Ra-iilFgsdlJB0hyBFlApJzNlM-cU5zVGdvbpmp2-NcsJQ5BI6Q74sgwoNKqqGVjk0FmnKM9x73McizNkoLuzpkmGjD-wndWpiokfrbSZ82ApOf_NM_r8AdwwCFRLnCO8nSx-VT3OYCFOp6Q7440jb9ngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
اشک‌های شدید املیانو مارتینز گلر آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101240" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101239">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjXlVsfF5WHIUBb1N35VVLHxN4f8FMrKE4Rd5KnvrRlhr1y2p4cMkS-NZ6VBD1fr9vpB6YA6AIZ4X-rAHAmKe-HmMaqOawsPGM49ZNcoHlR0sezJ8ZZvjTeanT9wh8u4JFE4Q8Ygcv064lpP81CniYcDsg4hMD4SUClLcD1PaIVPG84aZm_1xvHjrmvRSynKYWBzMdwjxzYVOOwD2W82RgbpiHFCtuFUDbplxt1KVumx92DG6r5Hy7cl1orSWsCR_NVDLbC-ZmNxupF05gTg6QPgaQ3oc9YZriFDhyrP7WIsWTd4j_OFaVKasDE0ilt9UbVNKb45Hlk6LVzpzRLvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
😆
😆
۱۰ سال دیگه فران‌تورس قراره این عکسو نشون بچش بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101239" target="_blank">📅 02:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101238">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thydWJ08_1u9VcAuOkfdoxEFq_BHV0_r00lLYc8IrThFCiIplu-uwwvAGh_q5pfuJk2Hpp4tZiTjNUX93KMuPqq5tioh5eXPkELl3gKQzIYxk1H1YKek1RSE2KvD4hSbIskFNU8OwFxfXiPbMolV3iGT5KUbnrCcE-ffVOid58Z0VaVnSS-eGFSVfyNv1gA8Kg2wMm1je-q21i5sqaDDqY4vFSEZg8Kyy-h507BTliUiN__ho3MvrgF1m-mE4fgMGdiUUqA55c9VRvdD3QFMaIGo0b867q9VcguBAMiZyHmQ22V5oHEUHk5beuNGCbPOEUIgUZsyG4VqY67yaCAsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اولین قهرمانی جام‌جهانی در ۱۹ سالگی برای یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101238" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101237">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6713412f.mp4?token=Na0XhPOEXE4R-ESTnG6yRoUnEYLWQ2bAgZYwXR3I5urj1Mz2lXoqK_9yK_-8cWMT0YODrS_QBCmby5LsgVd6oEigF02ggseYMyEtiWAto4QCGWPyaoSPRBzmfPEU8wGYcHR6vIoVk34I8qSrPiurz2sKV1Smu78gcHHT8ubAw5kEvBaUQqf5eVUItYxVSpDFICRh1EFqcMAdOYxIpqplvcKJfpN1RrXCqwfAZI4aIclLnLQdcHEK8GMjfKXk_tPFprlMcLkxF70mHz1cbhdA4iky8QfW2E1sLzdYWWwyRT69Ufim-SzeNmypFxMyLE_gpmtpI98VpoaSUgpD1W2I6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6713412f.mp4?token=Na0XhPOEXE4R-ESTnG6yRoUnEYLWQ2bAgZYwXR3I5urj1Mz2lXoqK_9yK_-8cWMT0YODrS_QBCmby5LsgVd6oEigF02ggseYMyEtiWAto4QCGWPyaoSPRBzmfPEU8wGYcHR6vIoVk34I8qSrPiurz2sKV1Smu78gcHHT8ubAw5kEvBaUQqf5eVUItYxVSpDFICRh1EFqcMAdOYxIpqplvcKJfpN1RrXCqwfAZI4aIclLnLQdcHEK8GMjfKXk_tPFprlMcLkxF70mHz1cbhdA4iky8QfW2E1sLzdYWWwyRT69Ufim-SzeNmypFxMyLE_gpmtpI98VpoaSUgpD1W2I6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
لحظه‌بالابردن کاپ قهرمانی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101237" target="_blank">📅 02:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101236">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GzpKmjWSP-CbLzNAtvdyp4NE_-TaSCjUVmB-bcEkORlci9hGKw8CfHOclZNMhRkVF3Utj-O7oWeQLTy41ZZCEC3pgRpA2Je6KdNfczGOyKyv1Dj2ggZoRYOtkiZ2AkQzJq7g6wJHRuTJmrs0ynhPvEwV84BoT2hUeSiU-fjDNCXo7jafm4HiySni2sv0d8oPAvWikrClagv9tSkL8K7wXiwwoDib8DcAIQXMvuK1ikv9QYh9_6wM-Mw6z_faYz22nEQWKn_6D8iekgUt42M7ANqbHkpuBEkGlfyLGGIxob1FiZPx2h9mBrjxHU515JSWdS3WJOG2k564o2hieSs9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
📊
با قهرمانی در جام‌جهانی، شانس کسب توپ‌طلا توسط لامین‌یامال در سال ۲۰۲۶ به بیش از ۵۰ درصد رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101236" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101235">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcTaqGFA0K-8jA2riBzINV1esl77KcIrmr2In96obyHNJNXkJ8cD3qWOBnLjC9joMrjoPE7i1nROXT0WjcwyDZFdfzpOSZWyl_-KmWOWNN4tT-sBwDgV5hNGQfUvXrIxuWtQ3coIuxlY6YuRRovS5whF2sg1IOYzn7jROJ6_1UMv3rnO-0t1mjWbWDTiwfQDngXV3D-dJqEBsociTU1b1zOZIaECJ9pAqxQofdWHhPJ3zK3g1oG_aATzk_9rNBKStE-iOc4huyAvrBFfCDXT83Csz0UP3BN2NCnB2jT7FuapO0aL50a0Mug_KUSQqIaBqa5oJw7_bi4oiBY_3J7iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
#رسمیییییی
؛ تیم‌ملی هلند برنده جایزه بازی جوانمردانه جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101235" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101234">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab00af27c2.mp4?token=Q0kdgVwg9LWRi2ILzfwdviDuOMJcJLUwlFRvW0cSQz-grPixeCjIZ1TgWNeexKusSd2Uiba_qoZHFDvbDDLhQRamtFL242v6DLTundPDvpDsqvFWxiTymbWrQmixNlUeO6E7N8sKstMMKkBvRnamKPZQygGY81tcM0F9Cb9ULEZz25uZdrl9RrBbaHv9_uSkmeGR9LyP8pY8I1Vpi-03QW4fFGxa9yoEg8BgfZxXSgSbDRNZmPRi0dv7YO4Xx6B0MaKFU9JnIyxz4esjtozsWHlCL4fGKh65w9yJpBA9lGXhEsX-lYeAFFIptT7B4J676fiSp0eLLTye6AfEc9CrSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab00af27c2.mp4?token=Q0kdgVwg9LWRi2ILzfwdviDuOMJcJLUwlFRvW0cSQz-grPixeCjIZ1TgWNeexKusSd2Uiba_qoZHFDvbDDLhQRamtFL242v6DLTundPDvpDsqvFWxiTymbWrQmixNlUeO6E7N8sKstMMKkBvRnamKPZQygGY81tcM0F9Cb9ULEZz25uZdrl9RrBbaHv9_uSkmeGR9LyP8pY8I1Vpi-03QW4fFGxa9yoEg8BgfZxXSgSbDRNZmPRi0dv7YO4Xx6B0MaKFU9JnIyxz4esjtozsWHlCL4fGKh65w9yJpBA9lGXhEsX-lYeAFFIptT7B4J676fiSp0eLLTye6AfEc9CrSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
🇺🇸
اهدای مدال طلا به بازیکنان اسپانیا توسط پرزیدنت ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101234" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101233">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxXr6mkj9cWpAktv2lkw_Chkh_VX-zTafoyhkJFPlrbSMwElbjBcTPeNtCjGVa8fjSGTlRkKWAyIgGSV9ImY-NmZK0VuTFPwWsL4S-EncbgOjQXh53slOMG7L1dqZow4CY9UH0Kev4uu4lNNP69D7k61hnIcNwygSsPCCYCGz8A47_Xr38G6fSpeStFsnU7Q6ECDGxpLml_PncwSi4cEBAM7guSnla99BAb5H6xu2x0YFQIToo1us8H2bx7JPjT84khwUsdW2QjH0AjoYnaIhMMGVavodlCfqoZsH8_UHSmbRVBR5KucAFUSkDhfpqw_Z2h-HB4LFNvNJOGGbg-nWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🇪🇸
و سکانس پایانی جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101233" target="_blank">📅 02:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101232">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">لیونل‌مسی همچنان داره گریه میکنه
😭
😭
😭</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101232" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101231">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNXgKDNJFeYUP5bm9HaHCZRzIVNOTCxDxVwJif3w_qzKXgyUTQORDHzwTD8UXKm5_EVmYPkt3lDqePPsU7yiw28wqfcBvsCC44hA-5FzJkL5TFPKmDVbOv8ARsa-zs-IGJrPN5QzcJukIhvjVwSxKm6rpTMR0Oz90E1QvlKgsqWkk9qqs-9I3i5VhkafKKMhYOZ1ILxVTktv4I77jjJmBbJhFTTgU4NWxcaZiKgSI3LOWmgNHhppFNjEgCsBEPtUqfegxS_O9jh-GGjjecQZ9R2YFj82jrXfcGqLxn6CR6MLcTd91Q3EGYSgYzvBZUxfJtZcC7uRVczoTeF8ci_6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🇪🇸
و سکانس پایانی جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101231" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101230">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2KxzT_AjRouTAZc7IOLlPqZ_yUzqCyb9LNxRHk6Ahr5lKKSHuVjzmFaHI9DT6B_x-X9tlb1eQKxyYgkGDJHswoujg6b7GPATdN8yOJTPpABD7XLNaD4Qj99Uezc0ucqdSzChup9icwm-7WWnUiJaMvp2F0yGOB3Fz_8SAc84kIAq0DCDLOT1kq1q3d1awjxuaGBNc8nHkLDXHVly_GOvJ13TEj19f_xGO8o1u_gohpoa6xxw9oqGdl_Huc7RnoG8ZA_vh_Bvbt2ktzOXd1dP_BQlTmR6-qsKng1yorc9R-MXHlrkpLKvvXiNA4FKFRpfwPZiNFBGskzDakD5YSOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
یکی جلو داداش یامالو بگیره
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101230" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101229">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb8a66352a.mp4?token=B5AVyHDSKo8h4m1Arn2K-XbeNcjlnyZEQf-Ar6BuoRYv1auKSxoa6K2ys7GYiORMGzdqkbBtHJfBKw3enxRVFfpVZpZzfplx4G8FQAISCQv3rzwhcCRmr4yKrA3qNYqS8SOKxLU4bx1wXcQus-x0xIi3p4HCO4PXoGpL13ZZSDsmFpgcknQn301Z6QVstnsJSBJlitX2ErHI4xGSb6GlWqfXyI04mCIZAe6eY2QOedJOypDfe3-PZ_hhaGMITdjKt6aqHVRaWVW0kbqSoHyN7RwkpeZcjXuSs5d9fyMaN4apDuRTxE-ve-9DZGV7_PeB2P994Q6AfocYStuEHgoK3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb8a66352a.mp4?token=B5AVyHDSKo8h4m1Arn2K-XbeNcjlnyZEQf-Ar6BuoRYv1auKSxoa6K2ys7GYiORMGzdqkbBtHJfBKw3enxRVFfpVZpZzfplx4G8FQAISCQv3rzwhcCRmr4yKrA3qNYqS8SOKxLU4bx1wXcQus-x0xIi3p4HCO4PXoGpL13ZZSDsmFpgcknQn301Z6QVstnsJSBJlitX2ErHI4xGSb6GlWqfXyI04mCIZAe6eY2QOedJOypDfe3-PZ_hhaGMITdjKt6aqHVRaWVW0kbqSoHyN7RwkpeZcjXuSs5d9fyMaN4apDuRTxE-ve-9DZGV7_PeB2P994Q6AfocYStuEHgoK3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
💋
ترامپ مدال نقره رو به مسی اهدا کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101229" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101228">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=nvu0rlkRXMpo4ClyQ40F5Nh_BmnF7kQLWVSwSOUnDF2-X3uf-w5zW0r-dj-lfA6O7h81qanR8cubOgLiBcw06HEM63hhg_bdRMibi-QITTNRaYw800Q4Ir-Q-6iFPCWXNcrpo7gcFthsbIyCZhG7lcmQr8_cM5ly0kDzzjyjXDaR5SNE7YfkRtiOlR4X-z_2UBPxYUJHccXEw8shUlPV832j_AyTUI-bwuPJWjcUpvXTVKsjs1xzgYrthdbjGmDCI2hvIxdlsi8MHyT6e2giaXkMTT3DUjGS-japUrFXFKHqtFY08um8RaWQWMYpijj5og5d8gK7nbz9y7Q0oYdh0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=nvu0rlkRXMpo4ClyQ40F5Nh_BmnF7kQLWVSwSOUnDF2-X3uf-w5zW0r-dj-lfA6O7h81qanR8cubOgLiBcw06HEM63hhg_bdRMibi-QITTNRaYw800Q4Ir-Q-6iFPCWXNcrpo7gcFthsbIyCZhG7lcmQr8_cM5ly0kDzzjyjXDaR5SNE7YfkRtiOlR4X-z_2UBPxYUJHccXEw8shUlPV832j_AyTUI-bwuPJWjcUpvXTVKsjs1xzgYrthdbjGmDCI2hvIxdlsi8MHyT6e2giaXkMTT3DUjGS-japUrFXFKHqtFY08um8RaWQWMYpijj5og5d8gK7nbz9y7Q0oYdh0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇦🇷
🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101228" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101227">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lryeK9YdbUfT6raogRrhUfNBWx96OSnlMTLmAz3J9CXx6lnOaPsjvVgC7R8FlGaR9xDT9PJVrnAey46cFG0n0Z8OmdHDZu3stHgzn1n1qCWMjxJtvYwYwwa70t1N5THW9GQEJYMw800lG7xqGyBm97zZUi3m2YlksRsjnv_4FDhTYTDw1hy66XC7r-UBokql0IKFjmOzjgF3LeOamg7_gqCsP8lSkoWB3bIM9xJE0zZzZVJtM3as3_Weihx-SrBI_TEDYq3OSflYXWw7TcRkbCm0D5ECuCxbMUlftZoeRQT6wADxXrn74k1Aq5YOB3Q4nDWzjIEwT7m26FFdyabdAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اسطوره فران‌تورس درحال دریافت مدال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101227" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101226">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTJIyGGkB--zIpC_TBgkWdOL4rE1cAZLpllDv5EAP_4DUmCfq2velRECP55ng152iz4u-Ak3jJB1v2xlHLj9CtlEald_Z6WrDLK4V08NeufBnKDIpocd8Tey6FMyFFnt7N_hQoI35Mah4BSJQbR9BGdpvd8P2m0Ljd0Ve5QeCEobpMbL1eWYnuzwy3Kfi6R02NmTQuVTrRvk2GroexMMrz2SfPO_f1wDAiOWLdsUPkCDnfSo0jO8hlLN9bnhg9WPUtKUdm29OiZ42gLmS3_w9l6bSbS0y6U4RdmQXuRNa8s7pgoaosFq3f_jbpkTTlTiqbY3hlKLR9FOfDjZVKfw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
ترامپ چه کسخنده‌هایی میزنه دیوث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101226" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101225">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2IEjox4pZBPmOUbd5Vg9dPypZehnJQjo7WKJoJeKTAqImMPOHN-R3x-Rwrrs79dxvfN1t_gfE7z73k7-CSM_ujrFa2idMHiqXKEZwm2wk7KqSqyim8c5ggiUNYP0hE7dJNX2TUeWD3frJpmBXTrbr6LtgmsUauDOqQbkdKg60bN9v3pHfPtJ4GzMmNs__qyZcwgGwW5vqYwnB3Rz3P5cc9ex-ZWtceLNSyy9x1urh7zfZes3BVheZ_VK12Rmebh2EyEHX0wMT60WkddylNLIPIps4CbQVi8bhQ7TtaV9e4h-F9F8PL_1fOhIim0_JDNIgESowV1_mhHh6TQ8_6F2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
چه اشکی میریزه اسطوره
😭
😭
😭
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101225" target="_blank">📅 02:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101224">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnSxqsMdR1w1B2QI0tQeOkILiRX1ZBoP06jPEucthi_yOtDjrzP3l8iQJEkoR4VrI0RCYEhtT3-waG6_nO1tY8d6v_rPfi40xWLesQpMxtAEkvsR8gFTFrLFNSmu1wG9J6PfbuL5srUzF1OkcPMMCy-UXEpBLORrAr4anJXb9RsdZErmyZ5UGRNkFxCyzbes9Vezhucz6KnApuwJ7kBqf3rQlBqLitC_1rtzHcGbqbsA50YmtW_xj-lyz5WecwnrN4mceubEXStLOfRacnu6bzZRy5DILrKBqFfoZsTYZmz6YAzCIyMJA4shj2g_88nisb64hla2XwRDLAX_wqeoew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گریه‌های شدید لیونل‌مسی
💔
💔
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101224" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101222">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPlcilhemwvqwqzysrvSKP1WYj5xbimRYJiuebjlmQQHb2vxiIGMsmhu7PQkolxoU7_iqJlXNVmVPGAnBDPDpO55Tx21l3Gk7FAHAKrK1KuDgBpYnceEIcKZYN0b-TzZEb_bRg6mlSY7szbMQNbQBEOdsMNyIuNVowICowsEgBEfUqoeaSRKeMyMcL-gWttjMItnDUoGWaMpVPkwYjJ25KdG4sbalGXUeM0MRq_1H_avocmj69nsoLptpkWxkIoJhGTHcc2di4kY4vEdh0e7CgzD-VqQ9WYKLM6opT39J1wwhI_5inWZuY3uL1ry-_v0lg7XrlN2Cp-caEPkKAfNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇪🇸
جوایز فردی جام‌جهانی در تسخیر ماتادورها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101222" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101221">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzhjLr2y7didJ8LFp5wnWSjtk7h6tpolgG7JHOqNgWcmLHSTSA9X4N7SyWKyFG1tvdc_UiWhBpoXnpwBp659jUe2oXzEN8PAM789qKjhhWBNn2QF8A5pGLoc5nrRjXMVFXiboB39bqdiaFY462eN856135ZZH2JISvqnMR4GbxbXCB2jIAvFgYYYNcQm4tx8ULPBgm5DzxsSpJnSWcLzCrHfd9X5NC50OkyjgQ6UnxGHC9w14dyWLGDu6MlMA6S4amXe_8RwH4d56w_mkfBan9za55_4-RsWapHz73oR9JwVSfELpaKpavCnExIQmSNJIBbbeW3GFC3rfLjmKJOtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#رسمیییییی
؛ توپ‌طلا جام‌جهانی به رودری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101221" target="_blank">📅 02:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101220">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyzAUk95Mi4JtID8cvtJA4Xyrytd9SAKg-AU8pSktaERV34APIXBSJpsDN0rue_d9VPXoaYBFeZnCDC5sB7eh_dRAEeoxtk9tDmyX-kcYcm0XvVBo4f1XH6W2YkjPfRPuLQ5jx_fgTlRzwn6DuR53jYrwPYyWkgZngFmsEhWQ2PouuY4X88qd-EcZzoWdFldw88gJ2I1DWW7YnSw8NS-W0-qqQ7SJL5T0_BfcOO4kFf_Qz66aOmg6Og6_e_zRVbcNOJiKzQ8GFHAM4Bdi1f7kgdnYEgMdBlsB3pMB5Ai66Fr6gAynRG1a_yi0NlZI2ksoaBXpiLNdYf2LV6MbAcOfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#رسمیییییی
؛ اونای‌سیمون برنده جایزه دستکش طلایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101220" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101219">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izAXjgF6l42gFOF9y_wtCKI6GwavZ0uf7p08fKkQ8McVnhDUdOREU5DpxBnccB1eJOvs8Gr6OUTrDKK2cE9rDOKxlRXbqs23fF1-l8EOE617cNzeNFNBFG7U1WgT5ezW4COBx7qyaxIOUmjUHh8ej7f8RMQCxzgktadsU1hT5x93hOCLHInLNeQ0NUslm7ZllR3SeprrHnnVmbjLfLOFvdl5vjLY1u05TNC0te9fIIslzi7TqQGmNdX-g_3ty_1NpkDXnOvtkkx5ZSNrPc3JV8DLRX2vFH5AzXjYWP684hAYoyY5HEeRJhGASQgH5hXjSlOptTcIPMsi7lhes3BlhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
دکلان رایس تو اسنپ چت
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101219" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101218">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV6ztyZAwFs4lwMfBGS9uQAM5EcNiTuNk-srKO8joFdvJFs7uJqvCRlw0s_z0K-ABrb4IVDgRUY5eWt6ZUTKrocYE83eRLOuC2hn7D7V75osSSve5RYlhhBoZ-lPVU3AE9T72-G96OVy7_NBkxBlUIlIu2G4qV0YIPk8PNeiSgiOlyOpvHBbVjUCPmdRTdOJ8QVngwQHXipFs2KaHth-sn2BrlLFaCct8AgCDI-tHhRW2OTaQ_ewSNddEBYiX5Psxiy4OPajQqECmr4oD34TduQYsvEMVGp2Wr5X20olsHZUp-NVDRlE9YuSANtkBqTr2mhMLQFR6bcYA2vC_cYlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
داوران فینال جام‌جهانی با مدال‌هایشان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101218" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101216">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ولی مسی اگه میدونست قراره اینطوری بشه همون موقع میشاشید تو اون تشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101216" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101215">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اسپانیا به رکورد استثنایی 38 بازی بدون باخت رسید
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101215" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101214">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcOIvw0OHwV7RWo1GcyzcbNjYHLvLQBLKlBVt8EyJbP13kC-NdPYK26uopCt1BnVkzoj0dLHJMlBKXsGx9vURmVungDxDEecP0wkh1169K73i4bsELtGubP9fv99e6QsM3WthWA82BjdRMYshcL4RvVqXqo-K-5-Iyy246UVK4wGe3WrYFpZnqQX7rMtmwiVEA1byvzmNLpbhXbuxBu8liz0gdrIwpkjEDCJkwaXvav-E6kbnWOchb73pPuFVJIMvZJXoZCd38ybdIvBeiKQNY53UBnQUSQEJ9jpEDzl_6HDmpVouBP_FFfBSFGl6orBSnlrQALd6bn0uUCpivssYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#رسمیییییی
؛ کوبارسی ستاره اسپانیا بهترین بازیکن جوان جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101214" target="_blank">📅 02:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101213">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkN9zy4KTvYriGlwVWr7VNqROlputD5SdnFsiVlyiRx0y6YY68Y01AMGr6WpjaEuDk89q_fti2Dl5sM9DUnht6imFqEsPOTJPLCPmkAp5nqcpVVDvFbf4hgF4xZB3kZu6rtuQqIqYK4pJGIahNp7A_IdQM9avOjj5msGoWHHE9t3gT6i1iejw5mq_o-S2HJ8DffQ7O3SalbN3aCAT-fV6js5-UInue7GCToF1_2KKgh0RGKyC3rlapdkGlx3csxgh4P5v17JzPrVCJULl1gAt8AlgVbc0-ZzKYOhomB6gXVp1dBvHqM6nXBN7dNyDmcP6ZtofPkSXjSip_B_zc8QmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤯
برای‌ پنجمین دوره پیاپی EA SPORT(سازنده سری بازی‌های  FC) قهرمان جام جهانی رو درست پیش بینی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101213" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101212">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gD53m2FA0je0BWmb3sTX_0Y7A_d0dE874H9V1e9az6n_PKFFsdNTLhBEzOpKiqg3mdC29LNnVYhRTiYK4waDgEYBvqyRvT763_9WG8HRXaGpvxpojyhnRhkZThQsOMKo7OZyIF3D3hAvCCFUcQ82GdmzfMZUn_kAQlKKUhUh0fkBFzQF2LbrYe1Y8g-tNBFyg62jfDY8_K2cRV1rKmQA5o6IxEno3w94_dzGXP4K5B594R6Oi42RkJnHEMkJn4yunyIG-8C67cfRz7xDnq8Mn1DJqlCY0IXBuXtw_GJfYRmiPFaaYTYh78HoiLOj8J1InofuzcPQFbtuMlLpdjQXBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوووووووووف
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101212" target="_blank">📅 01:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXM-7gv2SwNL47ZIRr3CFE0IwMrjZaJEV6Ko7q32xfNTV9YX_g9iSo7BhHnxB47oURwRHpEQ2yiFYRa1rU74lzXrjhBHQwZpps1m9t9cpfIGAshkPNZ8w7xnAfk2QBKZnXKLUKenkntHnGzyGsfKk75kqKCuonSgVbFUbq85UjMl-ELRjzAoVLVb-hdn9KBAwHKHJap9naJS1OhsoC6u5UxHvQgh_AOoG-RS4ipqu-RoDe7m7DQdLTJtNFBXH0SkIKNxn0QfcuJSo_EbE5fVkk3H-pGGoMc5OSDZXti1jOfFSmIK4x0S4FzjnA5GXs0RA48yEB1t1EvQJg2W-Faq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ اومد جامو بده اسپانیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101211" target="_blank">📅 01:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StMp89e9o1oAbtez4tK3y69GFPTI3Aobj5NspaWWQK8nXwTkJX_7DglnnEksPG17sff833fslMP2Nf9DKZ1qX85tZKfi_PZbcSz4LMYbFRsYtHvd6sDFnnW40pfRtwCNemIoEFx0lY2EoCEQZfB3-SBzz2y4SXqYykR4fqOkLO7FUUKMAKF4DK4VsgNUlGWKZc_fmAEgZ6VxB2Hjcf7ZtBeqyDMfLfFn5CA9Bz_eedwqqOHg0AYM1hqhqdvOCoxZZ6h8pO495kMbpjXIV8GiE2l5PCNZ0aPSgI1Ri7fN7E0BF0pw3sD8wicuq13mABnAwCxCNqDtkERdgZa-jsKQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
لست‌دنس واقعی
🔴
مسیِ ۳۹ساله اگر نبود آرژانتین حتی از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تا فینال جهان برد و تهش به هم‌تیمیای خودش باخت
🔵
تو خودت رو قبلا بارها ثابت کرده بودی لئو
ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه روی طرفدارانت رو سفید کردی
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101210" target="_blank">📅 01:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6tNivkPbEFLabo04lf-uYPizlV0fDG9QElMndy5Do0iUz8F3NddmvZhhteTL0CQKOcvbTmnYx8puOiyfyaMUg7JSjYDRpQKt4vbev-TlJwF6OAsLFBEz5bBG7WIwdzzYUb3IomG8PJsuLcEC216VivZSiefEYkE7jPHkVw_izYpQXVZRR2KTeKBvevFdTMBmb51X3DGDjra3RUWssQI1nznOtsvP1wecf5MO55oUU04EdSpoBKezALo1ARTkQ8kiu9K2i_GLtmjqVgB9KNaGPH-kTbqqHAoA6QTtFrP4tTn5jiT7ZtKn62SnKgNJUUdi5N6FQxBvzhGFQe47Z7ogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست، تنها عددی بر تابلوی مسابقه است؛ اما عظمتِ مسی، روایتی است که از حافظهٔ فوتبال هرگز پاک نخواهد شد. برای لئوی افسانه‌ای...
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101209" target="_blank">📅 01:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101208">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wcu0TSnmuQ5_RbTXHl8LyDsvk0wlK1TZHMs3TaHJgPZNULHfXNowBJGP8Ex6XGc416l4ot4Sl6UEWRfyItluApmbAOzS8RF66bc1Hyq0M6qnLMn3sX-bcalTu9tch5DNUJ2YD6R6Ayy9Yu00f6DsHDiiW1CzNi0CXGg9k0WSwVOi4BowQriR8_ueIrnvZidT3s96plyGcq3gLmQuV-BNhXcYI9zb61uvPgEbJVr8XTNHlcp0M7UuAzggaIhC8ghxSyHiEupCr4LmU-6ETvc1sbkO2UGeO4PX72BllsFrbgmllFl7dNwQVNUWuuG1-9NTIB_0deHNgmISWCous2dYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید قهرمانی جام‌جهانی رو تبریک گفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101208" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101207">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPwRegZEU6HcCndxvFkGlcEScTWU1Wi7TZdXcl4YY4H9vLlD8z7wDHIgQcdNOsum64FD6aodhYJJB4JZjQxYWJEX-IQqRFNj1cIIfb5NrYtZpMk2_ecfVc8QAVzU0GGDL0FqgId8yEr4aKqkPX8IJ13oBEPIeucR_tSlng2ucCAEZW5fmkC3gVgiDfOduPBhoXVXszANIsAgwq69IOXJqQ1GUjBv7q9bzH_916wf-LAyJYL26Etbi34vP2FjmKBooeLWw6PtUityz-reBI9odtAo4XxFrORxwDLW9aRJE1RnF9WLlk5LTv8crSxLKg589Q4RBE2idNWn-oKFueaxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فران تورس و جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101207" target="_blank">📅 01:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101206">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4bSHv-f4IFQakoF8dkOpSdx8p2zhbS9G2x4vU47NDkonKWkh1lJCOVFqE96gmeNlMyi3RQuKuHDW6Wr5PpdqBdNGbkh8lmQ5NTPeRQFAmw9TztTdFxllcI2fw4KYus1YVFXuOo-iHth_Te_OP7_bRstzB6HRi9f-IvpUYyPm4LVROpBtSjYKFAwt3gKX4fOnzAhksDCtrh7nkah6HFMRZmrq0c3AvBdB1pK_6qy8H19E1uXFK-jd3vf8e1U45JUuwKS2gH7VW88s-S7dfcQXBe6IJh58aBxe2idEXE28njMcWeIX71wkKYB6B4_qPt1sySLG5VBcQjVjRf8tmu-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جذاب برای رئالی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101206" target="_blank">📅 01:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101205">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba340362b1.mp4?token=piipPkiHfcz2so-Uz6Mt61yoMOG_Wpoj1sWDHqglGvlcwQoaHHUl22Fdf2xdaYLzDBgRpW_Qqoo9kzzEeaQVLS9VLAdmjfTrRi1ikteByFD1lKJbKDFAKjCcWi6YLzojzc9eASG1CYp612gSqjCH82p5CX_MrxTW_XPmQ5AAxQb_dCqPiGrk9_PMtWvPuBAbRkH7HfiSkKp-W0qJmQ0mteN5tKhYmZ--thNHZ0Dq2nPpVA4wNU7p3GTkeGTVRm6ttAlZVkBFacwMMYwRBF4u4X_v3JIyVOItJZCWGbnSfRvaEgv21Vt-LzDdmdpXUVOnYui-r1zYOdXJlcK0KgBalg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba340362b1.mp4?token=piipPkiHfcz2so-Uz6Mt61yoMOG_Wpoj1sWDHqglGvlcwQoaHHUl22Fdf2xdaYLzDBgRpW_Qqoo9kzzEeaQVLS9VLAdmjfTrRi1ikteByFD1lKJbKDFAKjCcWi6YLzojzc9eASG1CYp612gSqjCH82p5CX_MrxTW_XPmQ5AAxQb_dCqPiGrk9_PMtWvPuBAbRkH7HfiSkKp-W0qJmQ0mteN5tKhYmZ--thNHZ0Dq2nPpVA4wNU7p3GTkeGTVRm6ttAlZVkBFacwMMYwRBF4u4X_v3JIyVOItJZCWGbnSfRvaEgv21Vt-LzDdmdpXUVOnYui-r1zYOdXJlcK0KgBalg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
زد و خورد شدید پاردس، اریک گارسیا و گاوی بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101205" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101204">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvdCHZ53aseX2gb8SIhtgPXXdZ4uOv5PJZL5ELBoe1iPJYdmy-y1wY1WyTLWX7Ok3_t08dg6jv1e7nrwniMFkmKA2L3mzrBQg8vmFNcSvlPDwSuKrSYz9htt5aGjX0yYTTJL3saukulFkaBdResCDUe9rO-DBzwMvr7tS4Hh5T_KGbm9ytamJHb2ijkSUEnDt6iRnNWsVeJrmtyMPIO6BYh0ag_N8iLOz0wn1TOm9oD0P2I4I-xcsZ9Wq2NGozPHIAILcfFWYxGgC9h_6D4riTSP7IHlrBRszMf5s-f1XXJPCpq_8A_BIrcpe77ngvzhOmssTz1z0U3oez2orJTmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فران تورس و جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101204" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101203">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R41HGmFoqJUXZD59W0kkwWEL33s8va6Fb57DK-DuM_KZd35y7xrpWTzSR8VZTtAnSwMQiX5jT6WKwsqSo84F_OcsJs5qyxaCFiop-N3Wc_H4BqVXkuo7BCKiT-mgxAomRwmY4dBl7Vs4_Q73Y7DmYFYm635Ayi1ZXt6y4U6n482QwMTI3RF99agoLwTAExOvq-QWtOmDTI7wlXHxc2h-n3yt0Fdvl2UJaG7gg64807iiJeLfwBRUK_-FIa5FSMc9PZeq2BI1vlIdYuxl3o6vzN9Nmot1lb9D1xjknirl6xa6rundsC3hQalOyC9jWJ4SGwG-BOl1zTOnL_bAP4jSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
کنایه سنگین تونی‌کروس ستاره سابق رئال به آرژانتیی‌ها: فوتبال برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101203" target="_blank">📅 01:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101202">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLf1Yz2E08jtRg2fNhFlkDFOWcrAZ6YDIgipFfUTevOe2kAW0HvJrKIvmSROhYFY32fEYq5m0-hXHEgu6t8_KINltJVVQc99BrKOOc8HIOn6onWyQ876hvlrw8p3DsIyCa8Ra3Dc4ohX-U_uS_Az7nKfTJPAXCdYHqjbupYE53_PGwu9rPs5jd6cyOYwhvtexoT2bV0n5rLztxFCxz4sDdoY6GcXprPgL9q846-x4VUw96Is5PzFVddfWWin9jFfeVsHyWfgcEMYE9nNsp1qek6F9Kea_HdIhbygQDhdnjEC1OgFcNlp22LSRsYdOIbFf_0vH6brtwIsRRCbJe0DBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعظیم برای بهترین هافبک فعلی دنیا
🫡
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101202" target="_blank">📅 01:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101201">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1P9KyN5zLMzj0jWyJ2xEC45TgWfvxUvFydaJsbMinnlo5FC5nO4ITdMcw7qt53b3VEHAy1OQoNvW73qBK8Z4rYSSncrF5Ot2rDQD3NL3WgOkufvMFf5NH9yVe2PBopa0swicNyysS4JMYczcuiJw4Huf_jzLofiR_vQU3VN84a4EPBgJreMhQeT1NRb7aulvz4KeJ02pXocCO3L2wOXpmOF5iMWQuQQWi4Fht-LPvP669N3plFc783WPNbH4nPWKnc8VWREptH78KLha5_yP8VVc28ylNhCP16A2YEuhEKoaNtCamOs606vlLxIz6VRjYmK2QkOSYlXm1MH3K7vmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙️
🔻
فران تورس: وقتی مسی در تیم حریف حضور دارد، طبیعتا نسبت به حضورش احساس استرس و نگرانی می‌کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101201" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101200">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پادشاه تاجشو داد به شاهزاده و الان قراره تموم دنیا براش زانو بزنن
اولین توپ طلا در سن ۱۹ سالگی به به
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101200" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101199">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw8OOyIgM4MxSYWSydlJGEeI4N-7VPFApmJ-7T8jeGxwxdAV-cOLYJVvRMk9gabFsc8GIaHUwgaJm6U9fj-XR6TNgUGWAHGVT4jmyfWwErBBHXDeG_EFzarv5xD5FqkmdYvqmZccWe-kCgqi_9UMplRcrsDluyo0sRVfhKLsV8Mw7sesOzeLnykHtwXuw7T9litBzY5HeR-J2jhq-lLg6myg5PVSzvbrz-eJvtrrx0BXUG_3XlnBO5tU0rd-dA1PzIIt686hp0Pa53fu1vsW4cSPRZT1OBFPmY5DcaH4LWP4lGuNiQ9odw8UQaD5IsIwZ0Caa2NhKOXbJpYzy2kc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
وضعیت تهران هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101199" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101198">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faAdqF1Z0gT9eSNcwVODLuGG425DR36Ty3haF24NJgr5OPYwU9Oi0uqKTZpkrMoG1aFtb_mUcs6E3Gi4grixEWGd0xpFnUNjDd_t61ypFckbl2bKuxzYb7xhJH7Gud8v6QBbzuex7GAYR-ogNePUvYOqyZPXoI6PVXZLHoNpHV6LxUDQI8oVA2LX9OuhrH9ae3GDmozuXRjaXK9A4cbxu9n6cv42cRfR-jsciRQXSSqQ55qzHKBuxiWB58zDhNWAKwgZsuwbBXLCIv7R9rvTAktwC5MXRT4PBXV9nObo_kG1DKKi58pUtMsDPDPMUmdncovmIa-GCf5iqyJmxBOCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
پاردس که وسط بازی باید اخراج میشد، بعد سوت پایان بازی قرمز گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101198" target="_blank">📅 01:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101197">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0oc8VBJEHyji6okHqR-N0QZ7XMh-cLUP5X2EK2ySnR0BuDqIXrd1fPDY6dYQaYeHbr4Whhmyx0cfzQKSvZobMu-W9JYoJID9I1A43s9cTHLajSfytSmZORnaZWLPNazJ6HGpOxezfltIJhNLx1pxT2QvL1L2s0e1kV2Ly0qL30tZUwpc3N-jt7Bb73W124EaR9UqySnb3JcN7gRSmPUWjvqdWSXXNaLfTAN7XzoQ25aGH7reCKFGfYmxPWTtVISjf_ckDZSwr2xWSykLOcd_iausILGtfApGL8qroNgcPJyJ4XrZWWtEEWexlzIVPO9BaCstaTla_38Xa2_QhhIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
پاردس که وسط بازی باید اخراج میشد، بعد سوت پایان بازی قرمز گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101197" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101196">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndo6LGSMksoLD4Oj6Gb-TNBJ-1cj_zZvcIsjxDpZC1tR876MGpxBma2mYDHi2zc4oV7Wu6xdPvEvAGnmiWmHC1XalcNAhQSY9SQ6ZC3mPxxAhJ-h9mxS0eVB8Kwke1kSfxkgLtL4bPYKQMASzzHVRoorEQUvneG2a7RpuajrBX4h2xeP-uCjLB4y23hmFMTMPeNFeKXEI0fEvjgxuOtlSGthT6fLkrBD8jia9jpS0G6amovuwBbs0YiCU4p46KJ-ixVZrecgkzuUxUV5a0wHgpvJt8fxeDybNYrztOsPAG5PSsIGU-2Uy9kZhxTnZgBWLTCaEDonjNQTBrj5a44ImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلداری یامال به مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101196" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101195">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL5x9DMXZbQuSlw1dJR_R5A8DVAsYvsXA4U_l9JqaR6_zVT2EI_GgmUk0iQG4Dp49DKYejeJaB89v6tUeeK1c6p12ZezpvhHOY-KULCpRIztK5JCEtYT6fJ-20UTT_QDsEFPgPZETCV7m8oXX_xglq91pzgv0XjXFBekxwSZRTM3tAEN96dzvLSC124Qo3cF6U2HFqkaWew4m4MInlf7VUs3l5Le7NMQynbqLrztuvdFvHrLLp2RROq2keL-w_CSEbae_BiDG5I9H9qWGioZ0yenF6yBuHYVXb1JMEc-qwuADYUJmayDReg1jch7L9iCpfTQ7hUEWwgypWEGSpH2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
اشک‌های اسطوره رودری پس از قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101195" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101194">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqDrSHav7zFFxsYahLxikYgyNKK7DFpi5HViHFs4YsHKJOPd6PQKpzGaE4KMYuRFOEJ20dzXmEGvx3QNvK1I10QhBm18qQco_dCUBUWxj2Hy0_dQfDLW3fakS8ImesCnH4VrRgMn8HK3jEBKSOtz9Gt7Cgjg-Lp7tyth1XWMK6AoTvLqKvwFL0tm1IcUk6XQ89O6AOnNc2U7o-15KcidYig-Z8C30akVtI5r8GJXio0Lu7wIKpjJEnXyGx_gWwJET-NuX-6oW7pkj5M66bNB3RIz137S3oSG2eS1XJXBiwyzqKpAwoCosPKxs3Cr309bi4SYA87rCl7GASCMxWPt2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
پوستر جالب ESPN برای فران‌تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101194" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101193">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNHl6s4lt21CGErFv-6-Na6554-heTV1b5pOyBymaxkASd9Zc5Q97q0y14Iwf-IS4-eR6QyYcZg3X4NX07Sy1zaNKFKhCYG6HxmXk6mAiTg1NYPDTF1vXycrKz-vlIM9KllgrfWAgvlhiKQ9j-Ak3ayYyEV1Bgclf1sYri9zKr26rjkLhxT-mrqvo3RA91lcCh1P_FxirJJ5Gax5I_EFBjGaME4M9F35j1dKAn6Ldkqw04lBrzjkGTReMRt35yCNOav3vSmbVrchOBJR_HATHr24UX5RYwP5nRlwBxNRNJ3K9GAqshbEZgYlWrWqs87eE5nP0Tull4yW5FB0I4FGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101193" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101189">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWPmNzHNZV8MdiI7BQBmLPWCdPkahNYtzr2UgiCtTr70dkU9chh3WiuqQkj6RXq9ll7Kt2Ia29w1ob5Sh2exqrBLE4NOEl5Fs2soRtoCkDlVfYBMBuRij3W3urU3_7Xnh9MlEUP9e0A1btVIPWn-Asp6mst7vUXriMrlq11U5YW-LgLv8I9sQdmkvhBxqfQl5xkVcugthzxTzRyK-avfFc6mODUC-0UoeL0gp0afVBttw0klY92X-a1_pX4M8ka2_wW3wz6-uTMrA1O2Iowwofe1mzfbpMsrIG8UfE7_Lv14YyG-b-y_D3cKq6bpHYFEGa2arp3UPsjkSwWxUlg3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufR9HrrIkFw4l7_TVQEyNkSMH0prMTUiObJnCVZE9ysws2Hv60XO4XPyaGv9b8g98XSgAQicuv4eEcHape3Ql4ptFhnjMGpp4_cd45qhWDyQ-eM4_EgtdQey8A301509fUfjhlT2KyfoyODcmwrsRm_L8pz5JOWdqCH6Zdh_kLjQi1G-RsljCTI_OFwpayku6s4vWzrKXGEzyBLHZpkqSVRSHQkCDK_R6ivLE1lHoilfPPPdCvocse4Es2iTyCNwIVJSL_1Fvww_x4goesAcZ6S1uKWA45Po0Ijs5zPiAIH5pm_1wo8b5zr3FZYYoQcpiWIcNY4tBElFJn_zaLwW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjEcC7k7ptI3nnMZqGYZEwoIO4R-rTt_rWiTxWtcrywVGKpw9NyFQZsQ-03kPC4qp65_fzQK853F9LhfgmZFYPV9w9UGGHpGtolPLBolsB6ETDVuSiM02ZrgF076U5R0q1pACSd8coNtGYp1fhgig0bBh1kFQlg9RCBx-LqJYhvXPHIXV-vMUx-msISgOC1wMeuvBtWw4lD7y8tnCXxtMG-jfnATsR3Zq-nI2I4Wdd2X0b_-vn2EV2JwQ3NI3iZTs648Pqtsdi_yCGqA3QlsQwHOR6nDj9Q4bRhM6rZ56a0rMBhT0khH9yp9bE6L5WKuqQsN3j9S7Yj-ZztnPNJE1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🔥
اسپانیا برای دومین بار در تاریخ خود پس از 16 سال قهرمان جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101189" target="_blank">📅 01:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSv6lEnymRkCOBIap6PlaXYXhTV4DUfyCh0zlX0RWsY_TS79iTUlyNgAP0FxE4-E3FIN9JUClT1AqnTzvznq5EXFFtXOX1o6akfRrQ9dfzmZrRoE15APUySYNzRoR2wWpfwHeUF7u8NczNkqnBVdTj3yPTzKy8X8Qmu43Xny6JJ7y5TTDNCORv9dRsOQFL7pYblsqcZfz_GDEn0Nvg-O2pbEmms4Req2H40xzv1Y2dFSe84FPyFgjMmac7C2HapGSL76kH9sQwgx6gzKPJpPYxLCdhbn86JmGCwshmI5Eg9E6I98X77ukyT9TQjQ630IWM1drCcwBlIWcekATyvZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لئو پس از پایان بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101188" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpmkkHrofm0GFAP2pAELMcRaeUPjwinXjdNCdjJ3bUCLuSk0hYvQJfjB_J8mYNqzgX848vbL6g6uZGJc9McRG9J8Sj8ZaCsQp_GLKcCE1eYEhnC2eJ_yC121LJKhl2y8dzGQRBVmaHa6SmYPgxBZMEHAwDcXw-FZxKODLNzijnoL9KtwxIRALmHWhCZVdGjxogDtbknpygyVfCMllakpQ43cxuufvViTRE8b_bd8zA1zlNJC5D4kqSUbJYWmG429iDxna2lzeFWlWXggbBFrPpT1YPhomvEiODh1wbJ8BrhARk89bJkGrzF2vUkEEUgbj2Lj8lE_8r_4NyoXZfiXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
و در نهایت Last dance اسطوره مسی در جام جهانی اینگونه به پایان رسید...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101187" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101186">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b4743485.mp4?token=LJWOmbEECSZLmw0R8LA7Mr5jvKS2GduFqXhTS3-vLzL2l1Ys4SybaL4EK_kPOLS8DAPaE6fl2oAtOfamJr4LawgFWX0uy3ojl4xp6bsv4C2sDtxPAio4S4amRmz8vn-gRFQuisttYMb4QlISMVf6YI0T89u8r8MqYDHWMPYbeD0upWZjvNohr2wUSOwPe03_0RT9Qaur80brSFaH7x4TjwmoX9MzN2neJebUL0w2qha4MP8U_QuLknN9PUdAKQHa6ulRmVDF0vtWzLp-eDklz2U1tNTcmzFMIEMvp2sYHIxE3AmyISV7i4pB_gd7zvOJl3KR8YLt-fCN65xLzFvKmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b4743485.mp4?token=LJWOmbEECSZLmw0R8LA7Mr5jvKS2GduFqXhTS3-vLzL2l1Ys4SybaL4EK_kPOLS8DAPaE6fl2oAtOfamJr4LawgFWX0uy3ojl4xp6bsv4C2sDtxPAio4S4amRmz8vn-gRFQuisttYMb4QlISMVf6YI0T89u8r8MqYDHWMPYbeD0upWZjvNohr2wUSOwPe03_0RT9Qaur80brSFaH7x4TjwmoX9MzN2neJebUL0w2qha4MP8U_QuLknN9PUdAKQHa6ulRmVDF0vtWzLp-eDklz2U1tNTcmzFMIEMvp2sYHIxE3AmyISV7i4pB_gd7zvOJl3KR8YLt-fCN65xLzFvKmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رونالدو امشب که صدای گریه‌های جورجینا رو می‌شنوه و می‌گیره می‌خوابه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101186" target="_blank">📅 01:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101185">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBdO_fsXsPvof8D9-QpHRbOkGeomm2uOw8IjtZNXs4IBeWgkVyXEqolOvbC7vxXUW4eqQoQUJ9sTfB7exX37OEtCp-GkD-6bO9rspOV5VslOD_YBtN59evlWYfI0xFrQ8UovAp61qJ0cKhZkScHt5BfVSmt5I0Gex4ydA4Z3Zqmi2w9YF7hlqFdDl1cEWg3CTPbgTsckFFz5qdRMYOX_qVVDi0K10TJCohMowdDxgrHSnjqOtIPoHjBx2cg7POZQ-LLVSD2TmqSWvWCwcJ8Hk9ijjYdliLG4Jle8MaGt1OW8xnzGt3ElPuxtNwTnO_tbE0L6EO6bz_eHTHmNukaizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لئو پس از پایان بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101185" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101184">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSJECG6VSO6NDS_pz-uLqQex_NlaGF8oogtNIQ1yeTL5Ua6gi0OFL9ksCmKpx8mmD6NhGa9P6C9tZoPqjoAurjE1zXa4yK_dTSdW8i5wmZEMZbr3jDR_SrIbnNj_p5Tbry8lcJ3yfoEJlmVX9Zo-mEsyjsmok284AxVThcuGH_tmULZWmxAB9b2sVjAMs2gZVMWm8lpzaGmjV1LmBniJpiwqVrs0t9gQ4d7zsisF_mFgGemKq-6emkfZeVfvkJ6Dw0ZIgHPyaTW0d6cMUkts_EmNNNe8CQotXGT9TjX2q38P6Yi55WhcsjmF5YX0f71SmnLz5Wdza70XSPpZ5SfWTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#رسمی
| امباپه به عنوان آقای گل جام‌جهانی انتخاب شد و کفش طلای جام جهانی رو به دست آورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101184" target="_blank">📅 01:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLhxLRK558tNKeVs5Z7HpvYjJMIDahvkklMtIuXBmxS3gPC1iZNjwjgrxiS4I_9ADKkXgEmn8EwCr-oPVykhkJVdX1UNSXxkPI7vuDn2VP04HAeoPwVFAjMMHk1A4VaTOeUrrpbqGnAkNiMZ5VuST8dbEGNr6xq0o_9GBRLVvsffsXLa0cl_GUsUU9BeRiQ4dfpTYIjKvCgn8yHiLc03Z5k47Jq1EzD_QpBaKwZWsk7JF0WEYYYzUnXnoO4IzjTFp2rY2Vfcm5bDQE_mvmhXsZryX13JKkfe4fqZaxhr3RfjQvCfF7IDJmAjf2rFd2cYgR0InEsIbmWx1Zi_rogNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تیم‌ملی اسپانیا قهرمان جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101183" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">۱۰ ثانیهههههه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101182" target="_blank">📅 01:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101181">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کمتر از یک دقیقهههههه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101181" target="_blank">📅 01:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101180">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تازه بازی جون گرفته</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101180" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101179">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوباره کرنر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101179" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101178">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">5 دقیقه وقت اضافههههه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101178" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101177">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آرژانتین داشتت میزدددد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101177" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101176">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101176" target="_blank">📅 01:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101175">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دقیقه 119</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101175" target="_blank">📅 01:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101174">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4MpPIR5TlKz6jlk7IvxKIFgZenuhCa_K8UjGnWRLOjAyeqx_rNU4jYiEJw4ENcYCFcbf59Ya72SlaPhI8jjzLVqITSif9oURvFacYnSIli2e2dLwUVVz0zjiT47gucW949XtJzpNLFb4LLlrHgfg3ISWqIb12NcBq1OvpGP7mLihj7nmdTpKgMnCtB7M8vRqHaqHOLoSIWvgBo-2y62JwqI1QLRalfBlVU8noG3o9kYbao8zwpW09Yazt6vA5ij-F7-Q1U7KMj3FxvEfgRXVmtFL20JLG9Dl68oNYoimKtK5FFlMjNLOga6lrJxF8wq_bV1wER76DtsZPKEmGE0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی بعد از گل اسپانیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101174" target="_blank">📅 01:23 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
