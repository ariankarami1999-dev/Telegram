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
<img src="https://cdn4.telesco.pe/file/fc8MANGoyFNWxknRR5CfwsiizoY7uJ93h8rrzsZ-DfY4Th2vF03rWinw67vXyoQzFa4dgKTY0lb9K_ldPqFXbJ4oXMbbO3KbmU4_0hxLDpftP-YW376m7eW3rDHlaBvY-WwjYTp7DY9jj1lcOsxn8PGZ_rdU4KSMz93c4UQq9OuzEnYt_fta2X41BfGNYROmNsB2x0F4CT2Pmdsy9sJEjpcXMMuBo1QtXvTtiH8z_Y4LbkRqx41BWmUL__BK-tzMJoLN9uBu7OtxBCmgx556uKWRx_mnbFH5JtSii3DMBEu66uYmWGT5Q-qCBJCLjGZY2LYV0PhbFeaPA-hvow_i9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 121K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-90411">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDsLOC0yhzu5vP25kCen9Ws75unOemLi3IaN6bzxilu1DQOf-cnDDBZtBxMRxdUYAI-glB9w02lVn-tDspq2YXOlNlyHOuUau67OdD7rzgL2tnnC21N6ol73TLLiJUc89XCMVEy2Fz6VTLwT9fmGXT4TwyhKMYzSqRZa3gWMxROxBXT9M3ejDTMi2c8c_aTMod1zr7_nRBD_mav_DNc28P5v8NgaML5WtdUF3Yt10C3IR6E-zVFPOYvydtxuJ3ZKOzHNSGUVhK4qqG2FcF4TQy524mhtLMOdzEvP5S_72b_E3-nQBG0Tsg27se7AUlPKw1Otbgh6OG4VCvpTNvh3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر آقای‌گل‌های تاریخ ادوار این مسابقات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/90411" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90410">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/Futball180TV/90410" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90409">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90409" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/Futball180TV/90409" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90408">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97be903d17.mp4?token=JPetItp0ju0cCAm2YGQcdqDIZBeFAzxcqSeQWCv_EEWysKlDO_s4ckd44XE6ncZaFqVKVNcI9j6lvUlmgMEDtyHVWLyzsQw4oc2rB7aQQMFraZti63i5O9wfPmpMHNSTLddwmx_NtCtJ6STF6n-vZ2XVtWZnk0Xaa60TTsNIKbaxKiVaJ9uK24V9UIovn6qAEtabyBz3JkEjTT-xcSaXq-fU4psPOy0bgW0nJUBvQquf3RsFn6kX6kF0FmKFzSZe18zInNSwYgQpHnGTTISEidWHaYIt6RhPaevOO-kIxcjqzQHmMEcUK_1TuVKqdO0vSEKHdW2cqWkS2oQ-QFbmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97be903d17.mp4?token=JPetItp0ju0cCAm2YGQcdqDIZBeFAzxcqSeQWCv_EEWysKlDO_s4ckd44XE6ncZaFqVKVNcI9j6lvUlmgMEDtyHVWLyzsQw4oc2rB7aQQMFraZti63i5O9wfPmpMHNSTLddwmx_NtCtJ6STF6n-vZ2XVtWZnk0Xaa60TTsNIKbaxKiVaJ9uK24V9UIovn6qAEtabyBz3JkEjTT-xcSaXq-fU4psPOy0bgW0nJUBvQquf3RsFn6kX6kF0FmKFzSZe18zInNSwYgQpHnGTTISEidWHaYIt6RhPaevOO-kIxcjqzQHmMEcUK_1TuVKqdO0vSEKHdW2cqWkS2oQ-QFbmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل یاسر آسانی هافبک استقلال به الحسین نامزد بهترین گل مسابقات لیگ قهرمانان آسیا 2 شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/Futball180TV/90408" target="_blank">📅 16:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90407">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgM1e_A8qpw-kZYOJ68Qk7s0Zfkwi_8mVah51T9HxxZ0MNnobUdT_aO24_0lP691RWA1esPZ7rKCl3F8lRJaYG_jTdsNbTD2R2ii78_1FpAREROPb6ZhXn7tLCWa5iP4psYrL9WII58_04BM5cr4sAqZS-LKFqnattghyKUXJcdy7QV4QZl1N-oFoTW29VifXlzRA_4R5j3XiSN6VF48w5DsYzUuZtBwfTue-J5KycbkDsuCHEaYc7n8TxiOcKsOQ7QmxL5vLvms2Q4GPswclej6c_6q6NDKJ6N4eCUC0ZyFg6uZW-JsLT08dWWE0658LATtU0TFhMBs-9X5il6pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تریپیر مدافع فصل‌قبل تیم نیوکاسل با عقد قراردادی به ولورهمپتون پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/Futball180TV/90407" target="_blank">📅 16:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90406">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ9vvmeIcOf1mD5N-tki_KtXfZSKaUZ4rkUwb-4TFhoZygjeB0EJmeGBZFnJCcFeVOIku0NNKF3dleIQzhNm7KdgaKpivYhB3hAo3JwAR7NmayJfR53Rnr4zrRbJa6Oupe87L_khpcV_ZbolUYBdwVXb359OqXzsjZ5O_s0hpEfP-2KQClDkC0M_ncVHo1fCw9QBeFKkH50eJFdkhL-oVy1jGzIeq6-uOKEnqyDEPYqyIejMUCM_ND6N72y5sluVpiMmjIZopz2cGzA0PgSwGyJ_gq6mTzJ5peD7FFlQcAmcirabvZs66jOMdv8i0uNvDjFaY6AvfrlWBhup6j3Hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مثلث‌های هجومی آرژانتین در ۶ دوره اخیر جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/Futball180TV/90406" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90405">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usmMtdsnhEA8K7dh29mDRywEUFTmaR8_uvWGSmbyXiL8Cx9-gcida-J-E8SPrRjdjrbMNtlZvcp7nWW8-j9voBFvHk8Jx2uVgfGgmYBenXk8Ye528K4IKGQGTHHd857ZOjYwZeDfZqoisOfFa6qbKJc8ood2gPMoMMXYrhvumQiyrzGhPefs8ag8zix86KclapSdZnNvfnm9M0xYoiwLFQK8mSiyhPlH4J3ZDucRlfdK6cigtbIbNWVmWYbdIFt0-Bv3h_B7ehl8nZ3NcXNfGyfuEgIyuCnjJ1S2UzBEUArzEmmIswdj9BcXBwABb1kUSvAYNIJVceITL5Wylh0pfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↪️
🏀
سوفی رین، مدل OnlyFans، ادعا کرد که یک بازیکن بسکتبال NBA مبلغ هنگفتی را در ازای بکارت او پیشنهاد داده است.
🔍
اکنون کاربران در شبکه‌های اجتماعی تلاش می‌کنند هویت فردی که این پیشنهاد را داده پیدا کنند و تصاویر جنجالی این دختر به‌ سرعت در فضای مجازی در حال پخش شدن است.
1️⃣
داغ‌ترین عکس‌های سوفی رین در کانال ما!</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/90405" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90404">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfxgu2NIP9ytYfcFk1lkX-ZpL_o7amC6RHx6pJNNgfiN6Pi8JE_QwFSiYX9P51dxEzMKB0686oXF56uFN2inE9XHYo9r-VVqwre55YihE9QMsZzZ2KIB6OWFPgDnwo5iFQL3mSm3Vhkd_8SJvjG2RtO0Vwt-dOx4xAEX993GttEOJzCq3o5p5u80Ucsc8ezOn2lJcXuvkE24zjpXz4risk-nShI7krYxjqEjX8o4HBFAc2bqya6E4sjai2LARaKPdudV9VGND0j8k7gVYXix96xMQ9mR9jBn_nyVqe094Xfr93ogIBnJRr3SJ-EmhZEuNEoj7rTTBVKR33E4TajBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شانس‌های اصلی کسب عنوان سوپر توپ‌طلا که قرار است در سال ۲۰۲۹ اهدا شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/90404" target="_blank">📅 16:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90403">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=KuY09Sq7D1fqcpK2EcDoF_pYhvZ0xVyf0TjYkwTEWCtNZHitKyG1FCRSv5V6YAb8g37r5PjDuSthf6TljSk7i_qgCk0JDwRSUu5yQgNRk_QmAhyLrVLPMGBDK5YskQwipMFp9-3FCj8k3QSnsi2T19k6nhHwJmSLai5_1gsZhXq0WDSfCeOjzBairrWZLea15tgt5leXhYsvLI2oWs-AZ4kRlYJoyn8KzhThIVzmR03x2oLuk-6I3rNu1tf8Ht9NLgn0p3TkTKfOvl_PPhNb3Er4ZBdafYVyJZT9CWUOOYo63tKVsTuJlZqIGeEnis_5ISeOSOeXOH-0_RksccR-YrLpXyqGpd4qkXwyvLCV7xdtgLZfYJZ-dsesy9Qm-jIru4mwSBncn70P-r2TjpqSuuOUIKUUXBfJZb9Yd2rk7izE6s_ke3Ru7o9gNCxaTH15-5Oy3q-5ZKNUzsa_Kj4VA6bJ5FjR_uC4ieeTWtUsydqgYvZMQlQJjQ3Xe1L_efcnNegdLOQp9l-aOrKl7Zk0FadSnD_iImc4ZkNEAXj0274f8fv9lykFFxgrdTNaoO6fpNu8s-cgnMudKwCzEMVUJ15xC_ZnqgdCrNakwhZzFbBcJpRCSsuIcI1uT5FphxDJ5Z13iVVV6vseHwaPbnjghW_7_s5A3BEhYviwPls3QuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=KuY09Sq7D1fqcpK2EcDoF_pYhvZ0xVyf0TjYkwTEWCtNZHitKyG1FCRSv5V6YAb8g37r5PjDuSthf6TljSk7i_qgCk0JDwRSUu5yQgNRk_QmAhyLrVLPMGBDK5YskQwipMFp9-3FCj8k3QSnsi2T19k6nhHwJmSLai5_1gsZhXq0WDSfCeOjzBairrWZLea15tgt5leXhYsvLI2oWs-AZ4kRlYJoyn8KzhThIVzmR03x2oLuk-6I3rNu1tf8Ht9NLgn0p3TkTKfOvl_PPhNb3Er4ZBdafYVyJZT9CWUOOYo63tKVsTuJlZqIGeEnis_5ISeOSOeXOH-0_RksccR-YrLpXyqGpd4qkXwyvLCV7xdtgLZfYJZ-dsesy9Qm-jIru4mwSBncn70P-r2TjpqSuuOUIKUUXBfJZb9Yd2rk7izE6s_ke3Ru7o9gNCxaTH15-5Oy3q-5ZKNUzsa_Kj4VA6bJ5FjR_uC4ieeTWtUsydqgYvZMQlQJjQ3Xe1L_efcnNegdLOQp9l-aOrKl7Zk0FadSnD_iImc4ZkNEAXj0274f8fv9lykFFxgrdTNaoO6fpNu8s-cgnMudKwCzEMVUJ15xC_ZnqgdCrNakwhZzFbBcJpRCSsuIcI1uT5FphxDJ5Z13iVVV6vseHwaPbnjghW_7_s5A3BEhYviwPls3QuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روایتی عجیب از کمپ تیم‌ملی ایران در مکزیک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/90403" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90402">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAfNhvIz2uv3jNOvHyqBzPuSWU90rtJIYIjWTwMM8JLgM70P7qLBdwSOfBPsMvx0JrlaHd4uTL2nM05QJbpsJ8R75cqNgPfKVbRAc4-6JN8l68HexapRYdVOFLqEdZ4qku2qjYkTtsIVKLBAYPUkhHuOXeRSdKuI7iYLrqWFQmkDSW1v3-wyZ8fsWNi7Z7QaJ-vvUvlIfmNpEEMFBXSIVrexVClSOfVM_w2D6HErceJgxL-LCtNO32yAqfvCxxc7TMr2Se76t-YG3ldYacmWZWiqpQQepT_0FQpNYCV6HIRq3QTppNU66J6x_9hplxjsAS65sf1DyS_fCB5UifzGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی با بیشترین پاس‌گل در قرن بیست‌ویک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/90402" target="_blank">📅 15:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90401">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=Gm_HKPNlbQ-kGGitWdsog8yN10XrXEFqyDQSqRmfGQx1cnVQIZKfCzB8nnQn5kbKdrFnOYv5ghAU_EEPEfsafM7w9kbXLDieMutw5GTv7qmNsDIZeMWcLsK8ARhQH9F0BNrty6pocSVGWMcJxDyrD6pEawlElzbUuBLK1HxeWvNQD0AaGe-fz2plj5ICKHM7t1SVDhFqzTkg6TxFko-etnozADFqoMi5tBdc17qNUc45NnFrbMAAWkCAV7EHb-5Y8st9y2qmdgKoDZDGDO3FbfL7ol5R7-7fM3pDVXTdXAEweCqZFSl5ZfV0THPDQ0j2-FQCwi7pTPcZYUkNZT0afA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=Gm_HKPNlbQ-kGGitWdsog8yN10XrXEFqyDQSqRmfGQx1cnVQIZKfCzB8nnQn5kbKdrFnOYv5ghAU_EEPEfsafM7w9kbXLDieMutw5GTv7qmNsDIZeMWcLsK8ARhQH9F0BNrty6pocSVGWMcJxDyrD6pEawlElzbUuBLK1HxeWvNQD0AaGe-fz2plj5ICKHM7t1SVDhFqzTkg6TxFko-etnozADFqoMi5tBdc17qNUc45NnFrbMAAWkCAV7EHb-5Y8st9y2qmdgKoDZDGDO3FbfL7ol5R7-7fM3pDVXTdXAEweCqZFSl5ZfV0THPDQ0j2-FQCwi7pTPcZYUkNZT0afA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت لاپورتا رئیس بارسا در ساعات اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/Futball180TV/90401" target="_blank">📅 15:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90400">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBbXqgwvtueeo3sCofWVfx0fMrg1YimEDr5_KveaOyzMgW5lBejRYanP0xq5nYeV1TGDiCGzY9wkdAxCA2Jyf648K5OgD5_hIO8qaKF8Rpc-NyQI4Q0I6mUdc6h8w9ELoJRkY817Pc04GPfAbLep7NV9Peo9kJW42MH1Bx4E84g3rP1MdHMCNrtFAjaMD171KyAlDbk6oH-RG2_I5AcB7OMbBAdt6N0ZS0HMu9IAW_rMPttl2-a70cURlOMAQof4o6wa9RS2RcUdfUsDqXnaE34oAiQbXrs776ghOC9wAs29mBovA99vweZ_uwwE2zrqaMOA215PQFPxDT6xRs7M2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
ترکیب احتمالی بارسلونا در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/Futball180TV/90400" target="_blank">📅 14:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90399">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=HuMmEq_98ZXoclSAkERc4xRyMTIIaz-kjdtwlPEwqqwfa-MGnFR7CMVqTmFC8Pugk7PT5dkFyRpHkBwTiqdWJTNDf1tJbYwgwy6Kvo066_hLfYW8_bpXj4s0UqY1jwEp4N_NRmiFjAjIl3TMewqIa0vguoehIFixItn-XOEeuAOLH7SG-Lso5bpuPVmiVxOimJc0-m95ZsFQlFrnwUfXrdIpa1MXplsG4PCT8hkDzKI0V-qLoXMxgGzvrIeLAUNkmi3dh3-TIkTpQUAPyUhtyR9DIht-iWoOdmTe3NGHQJiMakPlV_s8-Rvuu4giIqHUl3aC5IqfPI7WdHfJgyKQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=HuMmEq_98ZXoclSAkERc4xRyMTIIaz-kjdtwlPEwqqwfa-MGnFR7CMVqTmFC8Pugk7PT5dkFyRpHkBwTiqdWJTNDf1tJbYwgwy6Kvo066_hLfYW8_bpXj4s0UqY1jwEp4N_NRmiFjAjIl3TMewqIa0vguoehIFixItn-XOEeuAOLH7SG-Lso5bpuPVmiVxOimJc0-m95ZsFQlFrnwUfXrdIpa1MXplsG4PCT8hkDzKI0V-qLoXMxgGzvrIeLAUNkmi3dh3-TIkTpQUAPyUhtyR9DIht-iWoOdmTe3NGHQJiMakPlV_s8-Rvuu4giIqHUl3aC5IqfPI7WdHfJgyKQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
حضور کریس‌رونالدو با جت‌شخصی خودش در پرتغال برای حضور در تمرینات کشورش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/90399" target="_blank">📅 14:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90398">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vC3OUFnDLLUviANm_ImLOsZ6wnRfyj4ylggtCklAZ8V1tv-NqagwY_pyWzJm7u9PjclA26ugxMBa5JTMgdx4TedBUHh4d4IDfyrhssI1MFUNLj9eAFDLGLSLk7rLqWiy7uKG8DCwwEeeBji6_GboLXOOewdPg8xPfSGugdwqah2aMhtfjcL3nWh5dh4ywMCooldB-TR1oPepXvKDIa5dCexsJTbEzzjyv51x3JfOeqoPSBxh-CtBMc4079zaqFd3IWKTg3A4yeXRil5oKXSgRm4jwczEdVUmO2nbsp7JyaqjSZtQwFLhxqod8mDK7781StRTFoSXcxsSLmrLxRcOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ نیکولا شیرا خبرنگار مشهور ورزشی ایتالیا اعلام کرد که قرارداد احتمالی خولیان آلوارز با بارسلونا تا سال 2031 خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/Futball180TV/90398" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90397">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcXQEHDx2ViB-uQF8SzSrMAfpgO1fh0wfx3WSssr5TcUzekpPF90X2xqS09z8o5ln8lT0xvpMLjMEMiHKzVQjibtEyLa8c4itejMQFCdueMx7A6sAyZStkFZjcBimcc38AP45cvaZm7dNkYOfzYBeCw9iRjCKzXysGj8szipfNvH4s2husx9iPm7mtYVzeYUnkhWu2w9hmX0IavDRB57z8Sz9DMEcf_qMvd0yhBcXVeD-LHAvtvFS4biJKGoF6CZwvHoUspjErx69hTbk5KGitPHrEcB66z5X0r13YMDKBajop50SahxqZbZrABsUiaM5GeeRbq2rtP9vaGHO8ewKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
به نقل از مارکا، ژوزه مورینیو اعلام کرده که با توجه به نقل‌وانتقالات پربار بارسلونا، رئال‌مادرید برای رقابت با تیم هانسی‌فلیک نیاز به جذب حداقل دو ستاره تراز اول جهانی دارد و برنده انتخابات رئال‌مادرید باید در این مسیر اقدامات لازم را انجام دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/90397" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90396">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری از رومانو: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
…</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/Futball180TV/90396" target="_blank">📅 13:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90395">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ-ltghjRD0Vu4umV3_oj7J9nL686-JIVtKF_MTz3CRZ-U_SzYS9bYDZGrsYFi4KKaJ5573s9WnqkCRFaUC0AzvNAwu7OU-MVFcp5-VvOPrrDGFg897kqavkAxB0rqjEpbzljg3ZtQtgvLwaMxdZxTViMim1lQnYJIwKfXvaz93RJHpWqomKv4SKJB3AOUPOi9Db9hq5Agw_e5Locn0umGuWrq9apPBOrYKQfsR5ERUzDtjxN0m9alETLp65QjbWXRSFXhgtv_dzdu_bIJptHeBJ76qc6WmlWYonRU_2d-amzQ1xcLEvah3lvVgIr1oyhtW_6FYibUH9q4HcWWS1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/90395" target="_blank">📅 13:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90394">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FM_wlF28JDI_SaQ4x4qIZEFFpvc0_MKP1Y7OCanpmrKDSiaAnJ2teyMdgw2uz75IWehdpjqlfw9SH-i5F8eWOHVBXHNE60zPMbbrR6a4v_f16kl1j9w4lwhfmA3qDjpCp0UG4_mShhz6t4-T0o1yPX3VzqdDD2tprPE0Qo1Om7OpppaZpBg_MLgPqxqezH_KCUDK34ZFcnpf6HvsrkId0TnxZ0dZZvk9KVYU-9bZQFwLBv1xKGODDbGX263bOLGyFwnIxORyaEpOjhi9Jqpv7_AMLYyTvSC-I-taqfrZveSfE4-yPexHaSFnZKtOuvIRVkTm0DbMNoBQqa3ikKi3pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
؛ متئو مورتو خبرنگار اسپانیایی مدعی شد که اتلتیکومادرید به جذب تیجانی ریندرز هافبک سیتیزن‌ها علاقه‌مند است و قصد دارد بزودی با ارائه پیشنهادی این بازیکن را جذب کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/90394" target="_blank">📅 13:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90393">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prgTJFe6aFXsaMqptbnixWLzTx1uWNXb0Uv2QoIeuKwGggnUWv5y5TvJw46hQxQJPH8gnMxlWwvt8j2b7e4jwGE4BWMPY6d6bxO_fHPbL0uZnXjtNABgyiIPMsDY2EPaAiWMXOh3ft1S2VnfwmY5si8oA1mVvIDFmFbh8UAgi6ym_SimUn9OKb4pEys5ZeeeWfeHxCKkSAr8NVMfDpRE1Jutg7hKbZiKEnKnbH-7BqpW6jEBelirlFat_8v8UlyXD_T5XjSAYeOhJklJwN2gy7Sd-hK4_wS8sysO24xMBu1OZ_tDk-9eu3oDTKpOBb1TrjSI-HOaEpGCRMx2c9f4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/Futball180TV/90393" target="_blank">📅 13:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90392">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEEZxaO-VoP1rXJ2U625byYIyx2ERsxl6FEK_RJ9hnWXpOGCVNEohDtWpynbp_v88u5MXYnY2tiipu8W8eZYwlB-iLxX0pobqkbr0rO0m0NdMqB_0kyN3KdUeKIRibqiD_3Xg2oNiwV02QDuRtNGJ80du5QZgr7eRiMzU1-ipxv3-PY-4YMJp1iKR1XooTHp7h2jfHrtGYavTwparfVjOek-P3tqahdq9jHph-df2qUlf1jy6vPA3dSazBG7_g-RNg2kJGmP5NSUfvHuWN-oVOK-bc34EUvRQ50vV5iL5t7DyyKwqnQsZ8ObzLqxKvEkH2kqXIu7RinBzCOKJV5MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری
از رومانو
: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/90392" target="_blank">📅 13:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90391">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg-WUNJRh_hKeBNM78c3dp9AoQAg6E401lOl9r7FvoRox2Lp9La72LYkyrKImPV7dfwqaHrmhxf7SFoeMo83isoub-3wDW06QDRD94-ZTBqzy07WizZuOZFvK3CSW0Q8FiAy65hfpMJduwjXFrX9fBxvxJM5e-Q9umnv0oE1wsDLW4RJ0r9iLbiVTyT59qNXTJdvXjeSFncrXro1Z1zZkb9JYYC5O7jQxgFFt_PfFGZphCdSBueQzvGUlimP4k3Z_uA4Prk7n5uNWMzxsqEsAO50Ilrg_qnczyoDOWrmY72sPRZ7fXjF6j0QgX-9tkIUSGZOZX02MLH9RgU2mKufTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عمق‌اسکواد ترکیب آرژانتین در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/90391" target="_blank">📅 13:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90390">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766445bcae.mp4?token=LvqD09aOp10k3SmsfRTMG8LbFPl6z4cSJXVLmCi4wIgAdUq6cyFcYmVn5WYh-ElhvCZ103rm89meNRhCeqQnQaTY8WG7PCyQ0Y6vFOLi9l4u65KU11qZ0j_OCmFyH48jycuhtrph7RtIaqp99JcF0YJfT5ceoVTm-8J6YBd29QIQ6Re8ZiKmxzGAoQYA84yZzNyusgnu1pwznK04MqkN-3JzJzRunTXdivMUoYEn7s0DBlM7lJaxMi1QIZ0v9C1KN8J2lOdacvzRgcEWuqAPEzEux1TzHfme4RM3DXVLpyzuNT5-ZM4ACkR2abcG_PSZzU_7M9nkFCM0Hz7IVftyKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766445bcae.mp4?token=LvqD09aOp10k3SmsfRTMG8LbFPl6z4cSJXVLmCi4wIgAdUq6cyFcYmVn5WYh-ElhvCZ103rm89meNRhCeqQnQaTY8WG7PCyQ0Y6vFOLi9l4u65KU11qZ0j_OCmFyH48jycuhtrph7RtIaqp99JcF0YJfT5ceoVTm-8J6YBd29QIQ6Re8ZiKmxzGAoQYA84yZzNyusgnu1pwznK04MqkN-3JzJzRunTXdivMUoYEn7s0DBlM7lJaxMi1QIZ0v9C1KN8J2lOdacvzRgcEWuqAPEzEux1TzHfme4RM3DXVLpyzuNT5-ZM4ACkR2abcG_PSZzU_7M9nkFCM0Hz7IVftyKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هایجک گوردون توسط بارسلونا به روایت دیگر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/90390" target="_blank">📅 12:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90389">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEeItu8uWZmeAyBGoNivUyebK4b1AZxCVujePv3a0yl5Ody-GEnvFwvxLob40GoKVXv6F1DUrUWkVTuXMlx4mtgP05356zktrFlwT7UG534bfvE7FsbkQIjpYjdfK_VcsCsQbWLbPiBGelOnoTFnQNcpIVONaP-ZEFRP0WjGwCe-5iGKJkgBEzgV5vqI2Z0RWMLZkj0BiiIUnboca3UReaBcOv7LwaNdteUdeVirsLWHRizbkIeE4YaCHIIsb_ozXrnGKFQd75UJHtiKfDo522R5k3r18nRJHpk0XOJ7yyALPqPghlAsv5Nj2jGgqDk52vw2E6a1Et5Yq0PbKknnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ باشگاه بارسلونا پس از تکمیل قرارداد با آلوارز، بدنبال جذب یوشکو گواردیول ستاره خط دفاعی باشگاه منچسترسیتی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/90389" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90388">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/90388" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0iAL8u9Z0tj2zpYmpSONqKHCgUGd0BoocHwiR9X0jWUU5V9T3kr5Eq8zZZO-Y01tbXqt74Z7xPrDPe9A-qHlnjgczOf4eFbUZFRvHan-_GzDwHVAjWE2iVeGir59wU0wRrZrNMv8yeIcR4h8Wg1fSxYwSmTovoxIrEbrqzNYAMKyirUGf4XsKm-ymFku4W2E6i5ij6UEPz3aEscK5jLA4h9YzqFDGBnb8PWAHlL7UmVImqHoXarHLXBl219RQJco44OJGAtHgjBROzQmWFw-kOdm5hQZYEDVbEEqd3ttSxKn6t9XIx4fy7tl_dBHnyWe11rj3TO5DrhTdHbFolYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/90387" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90385">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ_yRX3LmLT4LNZDNXHYyq_QmQx0gjhBC_GcGC2o_PUg3_6H1Stv_Xx2HIYJTkQ9Y5G5OiaXTjK7Ki3MJa21KVS_yGgzdCW655FkFhrvFtFsmo8YmzK-ErAoKtXwrKWcGIbKeGuAlTbxS9qYMjE20Ca4KN5BmAWGf26-YBZ2zQwkBkOzQ6v4F0g5RDTDK-dAb0i2VJRgL8gNHCsCipci_Go2Xr4ndROlnYcuq1IQzQjIQjdD_5g5bWtdgC__yebZInum_p289OWkmjTN7uIeU5VpzhibxvoZ0kCoRublUzit7pdkHz1mZNuRM2nr41bkA9NT0TvqhxpK6KMQJSGPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ رئال‌مادرید با ارائه پیشنهاد نجومی ۱۲۰ میلیون یورویی بدنبال جذب ژائو نوس از پاری‌سن‌ژرمن است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/90385" target="_blank">📅 12:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90384">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkVoIB7qxpB_sfLFT3hpzhoYkfxVeM35d03xaSn61AL9vPTlsMduGiAlo3wPJrhIJhkZgpc-54r5HgYGm2MrHf48I_XeiVCCDOpReivWz0zlNDjMZJ9HMIgBrcbuFkRf6K3WlYzi09_d0WX5WtVz50DzvSWhp6sI7sckgA9YMiucV1lLGUY5scicOV2D4gjAQqfFdlenbA-RMv0QGtg5u0R-At0oVLA1e6MNypGLbsCGof0VW5V3UDY47mnRMemePVn8o9tcI6blWb0tkXiauYyLjpcVXP4mZqBqHAS9uNyXXV4xUdlvTJdGwaP1pX_h6vyqx09PAQmjMlAWmvtcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
لیست پاری‌سن‌ژرمن برای فینال UCL
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/90384" target="_blank">📅 12:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90383">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=muHSykjo9U9rCLwUyPh9fyGVudnHo0DcwhXAb24NtL1CtOtXq8hV4IokfuVeE_1mtTHpezC5dG601mMmXAPkeFgHgovm1AOcFO2pO_cX6qNUnsfepQShayco19fPjDZCsQWk8PNNzxqEgX5AcX2GzDArKpI2lWDd18KJLmfc4rlSQS1CXST27oA3IGFmfaJExYkNxEE8ssNVuiaoSM4OahYSzW7sNGSg-qRYwYJzr5OtnAHPp6lHurXfLjCLkAXC-iz2SC6HjcK5kI6GFL8_qpLI7u1YshKSnG84AAuKnDWrQ4GGxmPFOp8qhu94do4FXhdhfOG3Aweo25LNFGUmpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=muHSykjo9U9rCLwUyPh9fyGVudnHo0DcwhXAb24NtL1CtOtXq8hV4IokfuVeE_1mtTHpezC5dG601mMmXAPkeFgHgovm1AOcFO2pO_cX6qNUnsfepQShayco19fPjDZCsQWk8PNNzxqEgX5AcX2GzDArKpI2lWDd18KJLmfc4rlSQS1CXST27oA3IGFmfaJExYkNxEE8ssNVuiaoSM4OahYSzW7sNGSg-qRYwYJzr5OtnAHPp6lHurXfLjCLkAXC-iz2SC6HjcK5kI6GFL8_qpLI7u1YshKSnG84AAuKnDWrQ4GGxmPFOp8qhu94do4FXhdhfOG3Aweo25LNFGUmpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره مشترک رهبری‌فرد و شاهرودی برای رفتن به کنسرت ابی: پرده‌ها را گره زدیم و از پنجره...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/90383" target="_blank">📅 11:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90382">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYobmNA-d1SQM_WcSXjlpiiM79Nb6UBhkfSTOT1eU0SiIS3vegn8ZsVAnpy2bgXIiaisDHi1AF2m5cThlQAdB0TvslWTpoNHx-W6eCUbENW1xvx_jHeIAX_CJGQesa-wevQ5me6WrpB6kPVx4I_NQy6VS_7PmYLrHfeXJLY8VND7QygwankjEyYMBdvRBkwlzTS7mxuNEEXrIyRmaWSyJZ-_HxPxLh1cWHlXGz890i_GvNtJIGi1-eq_gIQemNxm0irQivsHyOxaAApchz2MTeT1au4kiaPWw7enMu5vVcte1FKAe_9H0sNxoB1GlYpo0PudCngbhp4IkdLoQbX3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ اسکای‌اسپورت در خبری اعلام کرد که ابراهیم‌کوناته ستاره فرانسوی لیورپول در آستانه خروج از این باشگاه قرار گرفته است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90382" target="_blank">📅 11:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90381">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nxEJSDFNnm1eX79lfbEYHj-vJC_wAFTCy8KGwm1TpsaqYQcBlGhorRHYLPNqYNgmDbxbi8pR1AKskOw-FqwIDBHk-R8SZLAMT-qJxqIPxERsLYWvNgHFBbY48rqKFqztYym4xeSGytN3w09r29z6YE6jLSbHIvUdeJh5wsR09vvchVmWfLlrOFckI72LIVVvAVhF3qhfHunx4fpSqWkmOWLStFS8ZrxuLqocMlxyD0CUtK6qmD2-FgjrVWr5dFtLmhm2n-_oCIlN5xs-QiqEavV3XQ-hr7jyn7ghsNAFgwTkm4CBw0ba--8HcYIX4lKaJjvBHBnsxvKjMPFV1BBXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#فوری
؛ باشگاه الاتحاد عربستان درحال مذاکرات فشرده با یورگن‌کلوپ است. این سرمربی اعلام کرده که در ۶ بازی اول فصل جدید، دستیارانش هدایت تیم را برعهده خواهند داشت و سپس وی به نیمکت اضافه خواهد شد. درحال‌حاضر منابع عربستانی از بررسی درخواست کلوپ توسط مدیریت الاتحاد خبر می‌دهند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90381" target="_blank">📅 11:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90380">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwNY8CvSO1wXuTOS8HeGorOCD8_8u3QejjUGddJPHtuAsUgMFG6CxgxEccj_3YZUrDJQs-4UJuNRe0Rk0wi91QQXtnH04GP2YGSR6ILXx0KyqS7ff1lnQLrdMcMEx1qZCM_wcy1nvciEQpSVt3hz2LakXYFhjEGK7041rqpKQ8fR8RItu0hO7HTjo3lYadlLuVHvhoenKXhC1ZPa7wZrrAmPYuwM2Hz-L8ZoB8fnLnf-hGFvjvvIaYsW_tumsB4fBbRE2A59Ps1hirIS86loaVwz0XoKghu2JnwJkRKVdR1-JswbI-FsX8lSZGYMVTl22nB9rg7iFjvE33IgZQ3x0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
استوری ژائو پدرو ستاره برزیلی چلسی؛ شایعاتی پیرامون خط خوردن نیمار از فهرست این کشور و حضور این بازیکن در جام‌جهانی در ساعات اخیر منتشر شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90380" target="_blank">📅 11:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90379">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No2r1SQiaOklOOjIdDKLh1xsto4zKqmktJ37JEAIHmuhC8keUoDsg5lnAIonm13bHh_cep8-vBD74hCbbUp8kk6S3c2QN-Yk6bqnCXAACthQbcGv-A5S6Zmqmrnv_XUoPE9Q6d3R6R11OoAvMiB20jsdaxBgy3k6cbGskRamJc9CVqTrWxch1wjQG2NcE0mOATQJg2b6fo--FXf-0uWebmbe1wsElLzSuxIQPbs3JBDvRJm3ROBDSGG_qBHX2VBo4FKCFCgtZQMwLmZHiXNuwMqqN5eTd0qjj_oWZ7jFch4l21oNawOObR1wU_njr89mo3wetC_x6iFHvfq9Wz6IsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🏆
ترکیب احتمالی پرتغال در جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90379" target="_blank">📅 11:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90378">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=VERrc734KlIN_sBoZaD_krzD6hAz0T1NcKiAACdN48o-4t5rnFn2grXW5jeg7Z0imH2MqdQo6RIxxGXY5swQo-XaeuEywG8ti6QKP5khc7tzkmTCX0z8icth60DtFtFxct9A5W_lHzNk19hKEQ3-2KwFyu4g8r56w58Cbplu2CjeGHfNohghUccTowF6PnY6WZAI4ko35ZYdIJwxSrcHSIaAvAOc3OI_adhp4O9dluyW7Og_S1jocGC5E7smbK24ZuUE3LdHdc-QIxgqrKbwszzb4od3bTnHneB5jvXX7JSlnsK75C8HaKcLOuhIBgPy3ndnfft2VCvjw90isngiB3U2HAhfpRfyXWEDWtcJDKCkcCfKZrfyigdlCc48Zhr-PM919NSfKC8T8PO5-y20x4GB8TR7D49ZaYco0cR0ZV8YaEGOk90g3ecx8UpRSqnuVR2xvuFQZq96mUqhmkvj7pw4p3tPcbL3mF-52XCDqju7msSmzLMzWGNWQA0Dal3xhDfW89IZZV5dbgyLGKKumvScuAKbIau7QOgX_5N1MNJ9YOkKk51HibCcUe5iYB34FESQRdrN3yg3oXzbXwDt6GBrXIv0X8PtJNtOYWCyQggWA1WoUAuK74XH32Bi4URmlY4PU81FgwllXjsBB5r1is7rY2KJLu9YkWxuz70ml3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=VERrc734KlIN_sBoZaD_krzD6hAz0T1NcKiAACdN48o-4t5rnFn2grXW5jeg7Z0imH2MqdQo6RIxxGXY5swQo-XaeuEywG8ti6QKP5khc7tzkmTCX0z8icth60DtFtFxct9A5W_lHzNk19hKEQ3-2KwFyu4g8r56w58Cbplu2CjeGHfNohghUccTowF6PnY6WZAI4ko35ZYdIJwxSrcHSIaAvAOc3OI_adhp4O9dluyW7Og_S1jocGC5E7smbK24ZuUE3LdHdc-QIxgqrKbwszzb4od3bTnHneB5jvXX7JSlnsK75C8HaKcLOuhIBgPy3ndnfft2VCvjw90isngiB3U2HAhfpRfyXWEDWtcJDKCkcCfKZrfyigdlCc48Zhr-PM919NSfKC8T8PO5-y20x4GB8TR7D49ZaYco0cR0ZV8YaEGOk90g3ecx8UpRSqnuVR2xvuFQZq96mUqhmkvj7pw4p3tPcbL3mF-52XCDqju7msSmzLMzWGNWQA0Dal3xhDfW89IZZV5dbgyLGKKumvScuAKbIau7QOgX_5N1MNJ9YOkKk51HibCcUe5iYB34FESQRdrN3yg3oXzbXwDt6GBrXIv0X8PtJNtOYWCyQggWA1WoUAuK74XH32Bi4URmlY4PU81FgwllXjsBB5r1is7rY2KJLu9YkWxuz70ml3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🏆
هواداران پرتغال در انتظار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90378" target="_blank">📅 10:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90377">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=nJb3eEqURVHlpllVNsp8K4XMMGJIlp2OrJKX5rSRNAniQu0r53oU1PGmRwFmwWdyUXVAuVRT02tj8YcDh3ytYPnW_UhZJ6lGPD_JudNzlSoE491-4HtitipQZ44VbIjmLrVizv6_Z6AQGfyQfjs5WXn6M2WQtyC3zIwPpjg1KlN2h7df90DL_zO4kz_QbnR_UojfA7GMxciENTQJi9xlzIV-kMPInfFiVUA11__yBVA7TioH_WvKTmrgSvgXvBicbc-MUGSgnnAf3BdjUP4njlaRTW_A3nlXcwsyPWLx1J9VYG-_eXl1yGxP4Frru9yb9wVbupvvykYb64zcee3p2qb0ggJ_1rgbqGnx2JEBsdM7LGGjONVDhd4LdyZosYu5HINIHdHiDKy3SXD55u0TWg8DHiuSzAUx-4VNP8mK3Rnxr1MtjFid_lpdEoDqRtu57NA2Ux7hDlovRxUVbhFBMih-CZOC2NbopCJgKjuQRd2Di7bt0xh3YKV5Axra6jj7lI24lYwwU9B7L0oiYgXSByRY12vRkK1ixIR7vxjiJs5NoE8hiJQ1WNWAxXkQt2ZBto-cePCFTDQFPfUoIvTbego8_P16OsALcDpQgKF-C3dNvZ9rHRqYPiGgfo1fUOHJrHeqMoT6za8sjMZhDL90JoBG1QXN65GoNod8RaPqhxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=nJb3eEqURVHlpllVNsp8K4XMMGJIlp2OrJKX5rSRNAniQu0r53oU1PGmRwFmwWdyUXVAuVRT02tj8YcDh3ytYPnW_UhZJ6lGPD_JudNzlSoE491-4HtitipQZ44VbIjmLrVizv6_Z6AQGfyQfjs5WXn6M2WQtyC3zIwPpjg1KlN2h7df90DL_zO4kz_QbnR_UojfA7GMxciENTQJi9xlzIV-kMPInfFiVUA11__yBVA7TioH_WvKTmrgSvgXvBicbc-MUGSgnnAf3BdjUP4njlaRTW_A3nlXcwsyPWLx1J9VYG-_eXl1yGxP4Frru9yb9wVbupvvykYb64zcee3p2qb0ggJ_1rgbqGnx2JEBsdM7LGGjONVDhd4LdyZosYu5HINIHdHiDKy3SXD55u0TWg8DHiuSzAUx-4VNP8mK3Rnxr1MtjFid_lpdEoDqRtu57NA2Ux7hDlovRxUVbhFBMih-CZOC2NbopCJgKjuQRd2Di7bt0xh3YKV5Axra6jj7lI24lYwwU9B7L0oiYgXSByRY12vRkK1ixIR7vxjiJs5NoE8hiJQ1WNWAxXkQt2ZBto-cePCFTDQFPfUoIvTbego8_P16OsALcDpQgKF-C3dNvZ9rHRqYPiGgfo1fUOHJrHeqMoT6za8sjMZhDL90JoBG1QXN65GoNod8RaPqhxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌موزیک رسمی جام‌جهانی دوره‌‌های اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90377" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90376">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azelUYSgPxyorT4Gy2pAJZW0YCZmz6MGMlmYHDoD8veROn8Gw3bKYHF7y6RdRhb9xIFkaHJDQJj7LGIJK0DCDlWcHg7tLWBI1CoEEGT65jsUAteygnN-vTp2O8O4ft97beNTpjQeAyDv6pG4CJ8eLUiNJMmNfUybzLMlqItl18vf8WjiYSE7JyYHlNJ1PfXbx90DL_LDPUswa49W_Xn2tJMmCZBxRAJV75JaSVTCQT9LJfhPO0wzu8HtfES1fZIlaD77giOhCmvlf9DpqoTtwHMuiFssRl_XnfLj78PtZzBmwm3199ZfevkaJc7WJdb2aF2ZWKEGtWMfBHYXfOXXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جدید یوفا از جانمایی ۴۳ دوربین پوشش دهنده فینال لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/90376" target="_blank">📅 10:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90375">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrinYqgWIBnliSLryVrT36UevfvJWUyNY2Wpdb52o_pJwffGrCLE0qAsOT25sBnHgDbNL0ygvi8xTvSnDserO9R0nnRpwazYCTesnfov6fH3yz_ctcqBcNVnST49NdFlszYo0OUv6CApx0SYHl2CtuehZ4pxPxpOYDwQCFZCauJEumNCvsEAWwvT48bOYa3uFB989UIv9lxKVJvNOM5H-YLd3ne6uWIdYeFwndgub0Hab_nOZvSTsNDBYrZpUbwG3Lg7MJ9PVIhjx9usNzoi_BdMBvP3zxYphZSuaHAmyoG5JhRoybuZGcQkDEHCFSBF-gDSeZUxsTtRa0vSxDBfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ترکیب رویایی رئال‌مادرید که البته بیش از حد رویایی هست و احتمالا محقق نمیشه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90375" target="_blank">📅 09:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90374">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏆
کار گرافیکی فوق‌العاده زیبا از قهرمانان جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90374" target="_blank">📅 09:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90373">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac09312735.mp4?token=gkGO3Jm6wRaEzZ0lxVrO7A588s0LjtkfE7Y-Elswj-fuFh3QRjrcisUr5EMZV5QNYQzbXd-A1bcCvRVnk54-G4LjekDKNxMImLKonZKTW6LqFherdK8GBk5CVX0lx1w33U8uJrpkMQEs02_WpJvNViRGZlcGYZRDr9KRLUkINqVyRqa_FkcuuRoUA2J3MgTxpqOuyEoSlVtbccWRBNru3R4XcxKqm0EThxF9B--O6ugDzc8HsMMbVhHx965b32f29To8NqlLwvO6cjwSEWig_HAPBw7-IpU6tNC6iKNyQuYmtn-QVeeeoaMC_JMzzkZId3okz-xOtpIKidtTibvf2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac09312735.mp4?token=gkGO3Jm6wRaEzZ0lxVrO7A588s0LjtkfE7Y-Elswj-fuFh3QRjrcisUr5EMZV5QNYQzbXd-A1bcCvRVnk54-G4LjekDKNxMImLKonZKTW6LqFherdK8GBk5CVX0lx1w33U8uJrpkMQEs02_WpJvNViRGZlcGYZRDr9KRLUkINqVyRqa_FkcuuRoUA2J3MgTxpqOuyEoSlVtbccWRBNru3R4XcxKqm0EThxF9B--O6ugDzc8HsMMbVhHx965b32f29To8NqlLwvO6cjwSEWig_HAPBw7-IpU6tNC6iKNyQuYmtn-QVeeeoaMC_JMzzkZId3okz-xOtpIKidtTibvf2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سانسور نام علی دایی در سریال صداوسیما
صدا می‌گوید «مهدی طارمی» لب‌خوانی می‌گوید: «علی‌ دایی»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90373" target="_blank">📅 08:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90372">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5yLnlL0mRswyfG3z4m9j4A0vO7G_8nr-nDJFuVpsyYgTIswupvwiYAOLXSIJHvMEXO6jG4xl4hAVbm5BoKIEH-3ozpAg9S2T55QIyb-aAz0LlJaW5V0dWM6PLemDYasdM1HF-lwjw3ssBuh0Tss0NNRx_LI965CwAmoVMVec53kAaQehj2CceMibgc61axwaD1a3dn7AjHKxSaunxG1uahdQRlS-oeDumHcdYbG-pd6ldyUs6hGgc6iZIHZeOsZV63-AoENN6EB-zklc6EFRg8oupNfeI2XuVNhvcpBK7I-yqiPt0PbRaRE6yfkNI1aS8qAO2hkAndskCCRKlQjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
لیست آرژانتین برای جام جهانی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90372" target="_blank">📅 08:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90371">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90371" target="_blank">📅 00:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90370">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqSEs813_zqYzfDky4bWUnAN6y5eiC03tFnVvY3tCur6_U9hOeXg3N4oetielmDtNmnmqCs34NFNo0DNLYHvIXyP8iZzQ1IX-wf0Gm15ifcZ_00aGn7GwULZdxYq86YgXt5MdG9Vh8qXvlwL5X5yIMR6L2QXOizB-Rg7tN8PBQb9foUUrmPuSCXhUzq17XGalQwFECJgadmo5fc2fzntfQmPKYeyD89DxhcdyN3TdMFcRrLfBrEM5gEgcFWlBuTjtidemZC5HM_uODaCo8HaKLbhyaczLo6as-1_tXf3qaJKcBuCWVnDlsc_6nvVPgEkic2SZP9iRJ7ai9ltmp8OCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a7
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90370" target="_blank">📅 00:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90369">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVMXtTY6lEVI2R_q8X-I1TsS-qxqRxhdj-7eVjDyWm-s-ptErOtljDg9ZDJzgUaq4GTULa8Xr9HmLewk3o5GZ7e0j2vnp7GsVIOqjZiO_Y1sN3jGB6Mx57mJZGcoQtMlzD2DQ61kQPu0wjUJyEiAtSUVdWuQlvDgHCIwAL0a_irUuyUN60RSmOOc9oAKIPKMLra3Wy3aYfSjuEhGaFY8gaJ7RS6QhGi0Asvc9qpPfMtHd-tn-iuNSj34xphliathKAUv0svt-6Dyrf28dHnibLYJLYYhdmFUMFwR7dSwOEllPBXB69VG3_Y9EK7U20o2qpPrthAMkQIxudPwbN6CTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل بعد بارسا:
😳
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90369" target="_blank">📅 00:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90368">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=jv4kn0OZaYE8d24TYndKXDKZUgyVdUisin9zIFM8TS9bFc24gsdC7BYc0wmXqzF-vTUgJWA607y9mauA1LBkR6K_eWj9gOM5yrJPwiGA4-pFqZIAIOBd0muYTVDif0O4nqoVH_pzie7zbslIl77hS0Z_KVIkAFiQymXYDspypROD5wa3g_YsLBvd_KsdeMDYWTHQw6hQQ1SPRSBgJFaZ-tqvFk1WCWmF77kkFmcAt_KMslph25JBgplWwsi_1a_81fzZWiozOJzCqQPFc4HNRM3znyBZQNTMBWD4whC_yo2iGTJXl59GsCvuoEZVajfwsnLgnpvhG2LUbqnrDzKvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=jv4kn0OZaYE8d24TYndKXDKZUgyVdUisin9zIFM8TS9bFc24gsdC7BYc0wmXqzF-vTUgJWA607y9mauA1LBkR6K_eWj9gOM5yrJPwiGA4-pFqZIAIOBd0muYTVDif0O4nqoVH_pzie7zbslIl77hS0Z_KVIkAFiQymXYDspypROD5wa3g_YsLBvd_KsdeMDYWTHQw6hQQ1SPRSBgJFaZ-tqvFk1WCWmF77kkFmcAt_KMslph25JBgplWwsi_1a_81fzZWiozOJzCqQPFc4HNRM3znyBZQNTMBWD4whC_yo2iGTJXl59GsCvuoEZVajfwsnLgnpvhG2LUbqnrDzKvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
سفیر فرانسه در ایران:
علاقه‌مند هستم همکاری‌ها و تعاملات ورزشی گسترده‌ای با باشگاه استقلال شکل بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90368" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90367">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=v5vffCFIQooZMh8-tMFg7A3gpWhEs5wAHTcGTtjcLK4bKcLwFBNyXpcl7aXpnRxil3mw0Vpi9kBEZL-buzV_5Pga_fLn_qE50lHMVTqmHaAjY_9-422V8x7DEoyw9EyYq7fiFpU9Ox0FLazdvyfOfdqHbM7J3yGrtg-gZWRjb-h5OqC6l0AHnoPpApLVwHcWNeQBfBnalePWi7KvtYarE4J3VzeBOzLSHeIQGznhTzkZG2dzgKJEie-IMqyWgvip2gr4oXe-YMHUFtZC4ZrEuriwVM-NOsyRaoUINZ0tE8XHmfmJ1dzSiLkedjgOzDaeN6_wT3KbjLHd1-QXwoQD1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=v5vffCFIQooZMh8-tMFg7A3gpWhEs5wAHTcGTtjcLK4bKcLwFBNyXpcl7aXpnRxil3mw0Vpi9kBEZL-buzV_5Pga_fLn_qE50lHMVTqmHaAjY_9-422V8x7DEoyw9EyYq7fiFpU9Ox0FLazdvyfOfdqHbM7J3yGrtg-gZWRjb-h5OqC6l0AHnoPpApLVwHcWNeQBfBnalePWi7KvtYarE4J3VzeBOzLSHeIQGznhTzkZG2dzgKJEie-IMqyWgvip2gr4oXe-YMHUFtZC4ZrEuriwVM-NOsyRaoUINZ0tE8XHmfmJ1dzSiLkedjgOzDaeN6_wT3KbjLHd1-QXwoQD1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
رسمی؛ با اعلام باشگاه النصر ژرژ ژسوس از این تیم جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90367" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90366">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پاسخ اتلتیکو مادرید به بارسلونا در مورد جولیان آلوارز:
خولیان آلوارز فروشی نیست و باشگاه هیچ پیشنهادی برای این بازیکن دریافت نکرد و جلسه ای برگزار نشد و از ماه های طولانی دروغ، نیمه حقیقت و داستان های ساختگی مانند خرید خانه ادعایی در بارسلونا خسته شده ایم. این رفتار یک تیم کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90366" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90365">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoB1vtRtMWnhbIZ862nJYviPu2aTM261AJ0HKQ0Qfqis5XQb_QZ2aVxq33sdHH1PVgSobyf9bNU62JEkGEWcwF1JmmtAHRDU8bkfV97QtjiR6hGedi7SL06VZBz6jA2nEtLuvcrSlAssBj5nf6dMoq1oqrOb8aAeo8-djhkSBsQS5NOu_xjXZvRHNFJKNBrSIgL7JvLIvtRUQxNc_0IEznZzpb65NBMb252i5hTUG_DVjmQCW_xR725baEIgpQQ_OLj6tTF5CF_hvNplzLocIS-c_N4dsjLGNts4lPto4iGqlIvBQMQbiGmOY8STxfmxw3tp_dd80Q6LM1BrgXj6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییی از سیمون جونز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
:
•
💬
بارسلونا در حال بررسی احتمال به خدمت گرفتن پیرو هینکاپیه مدافع آرسنال است!!
•
💬
اما روند کار دشواری است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90365" target="_blank">📅 21:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90364">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvyf7TFofw8HugI6-UfgEbNvDlR5mPbr3TDAioti4nONZiF4bgmn1bo6uQzyIUSBvO44YcXVpzLU3wxOI5dvMozSdXXnxXFJbhLjIy1dkcz2XnP3llJTVILlXz9nTHTkRA9p41dTf9pZTA2unIuZX6qVHb-y_eE8NfcnnoRqOVGTBgzl8hwHoUul9QKwy5Fk2S1LBAvI9_X3UvNA340QQdxuxz_KxZHA-U3_Qhby0PSLG4FB-CKQ5JvkxXhWUBOGH0Zf8WRYQrBpPkS8NWK5r1Mcao6u2ROUf841eIXDLUkwGps64mg_O8eBAUAf77B3nrpwCMatdxcCcQ67n0ekvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90364" target="_blank">📅 21:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90363">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL9_rRLY35J7bWeadPLvXvrEiKi4ackWMIAWM5TV9K9XGBl78_NZrbphFFQUQPLM5LvjBKIS1bhG5JWyCbwxBpMKeDYTV7Noyg4keX3qHcCjcevLnyrCZzYo3s00GqiV2yrZMwu4CBdlTw0Rh7BEZWgOJk0-t9nklmokRACDsjpscF2tZcYdQ70lXp0xm1evTa2zgtgG4EA7X5InlSoQhBtJA5oN0IPPsdTOVqGL1bCkKVjMRkW7TRwnIk628ymMaIu26nWV3FiBnBdQu_XvT0pJyO67CEhO8txXZGtfa4orGhanWHv3mwe7471XUJ9uqfBdZuCEywCvkkqzb_5q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیکولو شیرا :
قرارداد برناردو سیلوا با بارسلونا تا سال ۲۰۲۸ خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90363" target="_blank">📅 21:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90362">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbJPBEPUKYp29UxCFicUMeRTfJAtw-y7w5_MJ5IKBxfovzG2xSk5UALTOCuk3sLyQUzBi8aphUNMIQrGmQ3Y4gyNhUYeSpDCCRRbGCdg6zd6GjT8VXo1MhrmRB7VMQEw1OvTJ1FEa9huOiua4ZihXijTWsDZ5lgQ7bUidyE33kmwFBdZmadPxkfLkChxFyDn6NFVrrceSUvG00BRhsymsVu6MDJ_Dk5XlL9WW7DMEku1ncHBmhTQYnY_LtrYm-Qsi-aKR-CFEUYCOc-autNmOlu9nviMlJf94A4ZvRokk-wBgu_ouKRXZz3CEnUAHkL2NG7mv0cT5EWjtspgwdUiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم بسکتبال استقلال در بازی برگشت فینال انتخابی آسیا موفق شد در یک بازی جذاب پالایش نفت رو شکست بده و به عنوان تیم اول این تورنمنت شناخته و راهی آسیا شود.
استقلال 93-78 پالایش نفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90362" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90361">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clWIXVnsuBY29GLQYjGew8tQ2a49osEdcxEaE0ww6ST0n9thXeEZxa4QkBwiFQdxpYQ2DCsCjWcnEjnqIl_Gb6_3v8uEx8vaTNNR0TXRIn15N0mJL69Hrqj4_T4f-ffWw946pYkej627CYMXa0hmfJytvH2qSvb2fXnKJ97ocnllU6hJKs8y6ibl1kwULnGp1Zr46AmP8RqPKGwFmZvUAB1aIZfr70N6DK93C84fVuMzZdlRmgYdkEOgFyOYhQkwwZgYWMBnFjM96_VV2Yvak9vjV-k3kFp45bN3rGCSH1s7bG31D0NteG_mSzndGF8md9nAdPcWCh8AvK2z3eNiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی
HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90361" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90360">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">معاون وزیر ارتباطات و مدیرعامل شرکت ارتباطات زیرساخت:
بهبود کیفیت سرویس‌ها و بازگشت ترافیک بین‌الملل به دلیل طولانی شدن قطعی‌ها چند روزی زمان‌ می برد، در شکل روند افزایشی ترافیک بین‌الملل قابل مشاهده است، کمی صبور باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90360" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90359">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B334AJ8VyIjwh7kKYB7jNZ_faX3LICaqPPla2ceN6zFgFDAW9wjE0u1JaKCbchvH3THsHo9EHyLbXK5gfUEcv7oKuLITevqYxsgac7bAmE-5xbTsvf3w0KbHNAUQRdWR1zYAJp4F1EiS_iV4Hs6V-r6nVdHhU-DB6NyVw90LO3NDP9JSMv8tY3Kr8MyOVmeHi3lfnOwAMt5GHbv7NUIW71L_TBg9lpWVzhsLdr27p8VspiMi7eJIYeetoQdcjLxphxEmvGPJm28S5w3jEIVqJV-WMLnNDNv_yDxhFUYb-MtQCpQOua2ZdTciMNQPYPksmKbTOo-Jd0t6Um91nL5YRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو:
تا این لحظه وضعیت مارکوس رشفورد هنوز مشخص نیست؛ خودش هم دقیق نمی‌دونه تکلیفش چیه و منتظر تصمیم بارسلونا تو روزهای آینده می‌مونه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90359" target="_blank">📅 19:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90358">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">💯
اگر هنوز ۵۰۰ هزارتومان رو  نگرفتی همین الان عضو شو‌ و جایزتو بگیر
نیازی هم به واریز نیست
👍
تنها سایت مورد
#تایید
ما  با بونوس های واقعی
🌐
Winro.io</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90358" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90357">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIjkpWoT0EHE8a0Qh8ZLQaME4zu1V83qSQVKv1-luRAUuVvgDoxujJkPBqA_-BLMFpk8F8MlLMFst_qN9gZO2ZduGcIAwzj_t8llpvxXMaBPZtmgNIP7ZrPYEIeBFaNrV5mtYMSap-NdbPm3fi3nbTW4BFrrJXv7TvrtofKXm0HoUcnNK6ep4peTnP4RV2rSuHFpcRt9xr6G56ayLOmWjFziDmX00SYUIuoXvLlcyzdRsKMqA9_x8jOtKQuevM2gy84nxuoXE5QhyQwHaaI_EEa3qezwqRAq7MegnUCv-ypxxMpJCwsTFVB3czje-FqdZyxwLF73rfBl2dWo_5LMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90357" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90356">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICZgNMmpsWzI77q_vKxpOh2WD3ilRL6VziqTOzy1dbzerwM71ogAnqa7aA1d16fi0QsMR8-jlCxcCGSoTe88KM1umFdk2nNXXXoalCE3cP3ifUwMdgFe4HtY0_l_sXDL3gOeC8CEl7nHF1uLs0_PmLUBMCCI6OLsNykuaejk1F6oHLZcD7HAPUU8XqfKAISrCobh7PCd8ZwjEX6l3CLTkC1ocuqzg2aJIOZM6Ebdm4Z7Qxc9Frv8d7dXb0SDgNwka0661YpKRgFbrJbOkK4W7VFsntlvhAYMX6usZ9pNA9qw-WEdzGyS6YDyw57hzHXGtoXqHVVv8K2-InVMo4Mkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90356" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90353">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbvhTZgILCS5ZZhRddWV6CTob2K-T_MV4YZtAN0tX5tpARkdfLwy9HQiSNe8h2Ij7aUVzJ02Sy9PgtDOmo2XIqS-wjUQ8Pn7xE2wgHaKytMnLVRS06FFEMcnb0X5QTr-EoWv6GaySXZsdWTIh8D2rp-n3WT9497rHMvQmcsw9NJle1TfGs3nWPLT0o1aIjknmz_QzETn_jl-Xa4GtHkgm1xnm1hy1GzeHIP8g1czPyRWRKGd0XTg9rkJ9hpDWV1B7GKCLCprOwk-NrAio86qZz86aojRhYfTpp2WovHbyq1-6-Sk_JfDxKjGc2TvALJR-g71CoDShj3CMHFdFZBejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو :
تعجب نمی‌کنم اگر بارسلونا بعد از جولیان آلوارز و آنتونی گوردون هم باز در بازار نقل‌وانتقالات فعال باشد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90353" target="_blank">📅 18:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیمار سه هفته به دلیل مصدویت غایب خواهد بود
!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90352" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iqslk-82GTY8hOhm_U0R5CAX75alR9DjpDZBp99f_b-m1RtvCRIWHIqOVj7UXgZeBg4407moaYKZDo4AGewG2AloU8BLqbvGRfYI9gWKzYRZ-CL1LzD8FrvXwGFr6p4rQGYhnzo-SHoTufWydHG8cKvFVM-OUgQ5mFdq37C9ZvSOTywnExwN4xDitCvR3nQJq-Ah2B1Cw0d6CqkMK-otbABk5apW9WGx0AdKRukPKqIKDzpVyc2NCxwwohI7VuwUdhswFh1L5yyIipke3vYcz9ITbDOd23Esd9NAm8D2UVyqe0nU0KwO__HbD6WzMpIOZ4rSfHEOO9Y35pBgJ2LsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتلتیکومادرید به بارسلونا اعلام کرده که هیچ رقمی کمتر از ۱۵۰ میلیون یورو برای فروش آلوارز قبول نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90351" target="_blank">📅 17:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWqYxG4VRn1k2kyjYIhtaCcu6YDCNwJNZJtn3oQe2lW8rglof-XbWEz_uoaLwMZWan4lz4n7JnJdNW2JQufcrT11JTiqvS4clfDSdTuN9iQxfJCDh8z1o7iYG4QsZYHgcydzMORxxKV3gfYGxkwLTz-pKLnnxy0WdGxPkpx4Pmfd7wxl4i6mnYnIXNaltVfDgY7032xROUCz8aZYbsR4c-f9xWw_tFUfcQPcR1IymlWCMiYGdtrJouZITewIL_L-Q69mN3eyxRiG2ePbdJvuTaeR3c-KHtMp-VwD44JNXFJm39xtrPjzRY2koWPxDzyb1YP5WZSHqIDiADFwVp0Gmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور گوردون ستاره جدید بارسلونا برای عقد قرارداد و انجام تست‌های پزشکی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90350" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkdyDMlJ6TPbd2E1pvXmFPoHub6IOOZZJRGYOM7UfkvpBgnc6ZBgJxAEBI2ZS8zGkR5wdB1ltPckICnOXqba4CjO00A21Bqa3jn4AtnoRdlZl9bEx5pELvthVX9LsTWs3Vr5TI_TJj6jOWxGwX29K3VQMJTiL4jasDdhcsQphDRTyczLsuJzg_2Kxewq418kj2fmSL0LCD6A18l00FL-mdskz_eLf8VR9BxeSWIx-j6xTtfzxN2FeIEAaFe32lptoTKpYipRAEnhmM5ChNVgCyfT7vzKie8VLumwR4XQ-Hd-m2nO-IP1yVD1l5N2viS4hHuJqdGdzj3VykE2of586Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مراسم اهدای توپ‌طلا ۲۰۲۶ روز ۲۶ اکتبر یا به عبارتی ۴ آبان‌ماه در شهر لندن برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90349" target="_blank">📅 16:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_PBbSRZhD8O1S2eobPRAwgfaPvEbNmIVNlT19feX8i53ne7arH0XH3iukg8W-SIS6g1I_ptnMkihcgsGvp87Btvp49C6EeM1f8e00ITZpPpcvSoz1aV15WRBSARoZ0vZrFC9-DMfY053Rtp4VSxM-q_-nOrYH6aACz-n3F9B1VetPiRgSIImDWIbZLhadi7bxJ3l_CMDDCcWJMNg3mYvv-EVzC7372DwNzp0-SnfHAhsw0hLsy7O8cQXgyNHE7jliz7R8YQ39GZgDYh3Vrc__6YHQ-s7fPwoSoqc67EII386fSlAyD1qzuvY0BhTU9JsYGqAj_OA7_Ppy4duFKUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: اتلتیکومادرید می‌خواد خولیان آلوارز را با قیمت ۱۵۰ میلیون یورو به بارسلونا بفروشه
💸
‼️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90348" target="_blank">📅 16:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtOBnh8WsZv86joHfD5K4irroJSbh_bO8I7IOH3R9CVJ9rXu6WNSMdo2yrBmc9K7_Ty2rZxvX_zvcyn46sdjOSzLI6Cgq90VpzPHLrHWut5Ovqe8f-HMLjxyEEXVlKX38F0Cme9v-4Ey3UU7s9P00RDxAg9bemB6WiZpVHVgSUZVSWp1EM9QR0KqqJyNARVO8jDcFyMZy7SrZ8M3nXXp2xQkqQyWWxEtA8bk40ijeyhErPMWWP3Db6GfJIExFS0ScPQ25uFHjkwHNzeXR-tA54CaUid_BQZbyb9qdT6jmioH7OF1wKdDawY7q91bPLuJxEnzQhalW2WebwVab37EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد دیگو مارادونا و لیونل‌مسی در دو دوره جام‌جهانی که قهرمان رقابت‌ها شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90347" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=O8A52kbGBFSw1amkVrWbwdkyCaMS4UXbAtqEGRwaNktv_9c1jZ_LTJr6pBj48Yuz5D7ePZCQESPb_kHrzousOoEp2SPwTf9tjrE2uA8vaTLud-SlESM5Pij2pRJ7LSapOs-sFFE4pa1wfsSkl3v6_b5B3jaHiSOnkxpd68PbJQw1dvKjylLhII39cCLd0MR9PIuBEDFxEuHA7UwWjgoc7TF94qonJTHDvbrvlGhA1lvx5fmMe-kTn5vtufOEVVqyzIzhtGptJ3aCC3OXsytvQ6sRWR9-1pNvkQwT2eeE-9UZ21dm3Ml1dP3H5N3TWwW-mJwck8EI9PhcoeEPTHU9Z0wZwRmu9ejwdsYDK7v7gHSPAjQjsjnOAZECVAxUDhvi9Gsnd4BhRcwzPUkzqveTQ-vSDaF2sk7PLNoynF7RM-TOdkDB_lX_CKnqsCpdM5vim6DCwRr-Of45JreFNnO6L31EfN8kb6xpVg4vBH8Fzg-6rJ313H0qaPw8TG4qSh2Dn90xgKi5ydZuxNtKC8lE32DSXFDL3yfgDUjoL9q4TXbwP2zMWrlQoP9sZQXu8_SpBZIqsqwt3LfaJTrCssuoL4bP5ckbq4yVfWx1L-0Y2VBIiHHfVk12-YucU08rLxhgXNoBOv-JLYk5SaOrgVZZlpsnO-h8iSKmPHQmA9W3e2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=O8A52kbGBFSw1amkVrWbwdkyCaMS4UXbAtqEGRwaNktv_9c1jZ_LTJr6pBj48Yuz5D7ePZCQESPb_kHrzousOoEp2SPwTf9tjrE2uA8vaTLud-SlESM5Pij2pRJ7LSapOs-sFFE4pa1wfsSkl3v6_b5B3jaHiSOnkxpd68PbJQw1dvKjylLhII39cCLd0MR9PIuBEDFxEuHA7UwWjgoc7TF94qonJTHDvbrvlGhA1lvx5fmMe-kTn5vtufOEVVqyzIzhtGptJ3aCC3OXsytvQ6sRWR9-1pNvkQwT2eeE-9UZ21dm3Ml1dP3H5N3TWwW-mJwck8EI9PhcoeEPTHU9Z0wZwRmu9ejwdsYDK7v7gHSPAjQjsjnOAZECVAxUDhvi9Gsnd4BhRcwzPUkzqveTQ-vSDaF2sk7PLNoynF7RM-TOdkDB_lX_CKnqsCpdM5vim6DCwRr-Of45JreFNnO6L31EfN8kb6xpVg4vBH8Fzg-6rJ313H0qaPw8TG4qSh2Dn90xgKi5ydZuxNtKC8lE32DSXFDL3yfgDUjoL9q4TXbwP2zMWrlQoP9sZQXu8_SpBZIqsqwt3LfaJTrCssuoL4bP5ckbq4yVfWx1L-0Y2VBIiHHfVk12-YucU08rLxhgXNoBOv-JLYk5SaOrgVZZlpsnO-h8iSKmPHQmA9W3e2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب الجزایر آماده جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90346" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmx00ZpNoHnbxDBKd3dLMSoBesRwufFHrV-tWZKNuUck-5HQiBkyZRHyb4so8uralAFUo9RKBUahCPJjIfQkOLmnln0A7FfUXCm9mYWvCi_GkHZtZVYmppzFhpHhh00QW_upuEUw_BFKhKkqhEr1VC2fgjEa4v5eMcvi4Sk7kce8w2hSKM-TmHeWDN8O6CbEsJSj0wY5hyxES5SmD8EA4ZPdDJj9O-T8640q5bPyjsR45tzCNErw0aIAtbfSb4oxL7e7JwcnOd-0bzzAVeV60JBhtdGifVM7JHtAXHWb2p7hU-z4UzUHN0117BNKheylXRsnX-c82MqqXo_8w5weWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
🎤
امروز دور جدیدی از رأی‌گیری برای عنوان جذاب‌ترین مجری فوتبال را آغاز می‌کنیم.
❤️
عکس‌های جذاب ۸ دختر از دنیای رسانه‌های فوتبالی را تماشا کنید.
1️⃣
و هر چه سریع‌تر در کانال ما به گزینه موردعلاقه‌تان در نخستین تقابل رأی دهید</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90345" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQL2SRp13kTxkDGWUmwhMq89rI2nHPeObmHXEITX-sr020IBvegnxb8Zam7-by0piQzx9K37Atte94pd2b85ckwTYw9it8u66kLueHHJ-mmk_iGwcX_KKsNuYLbuSG5iD1BqRPeYeE9Nb-fGu7448jxvvUEZbIutguBzLurRye9v-t-vu4R5G3Gi6iXRyI-opR0dm6YpgchiuU1EvCHSvK_hqKrechZ0761iyqb8lfcyHj3WhBC7l9B04BxwlusrKJoTrRujxqt3MTDVecURqOhKp8zrEIdd1vEt1zaV0nwm6OA6qWOnUwyjSRWn-04YWLvcK5U08NUYSjMoiLW23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه جالب نیمار و لیونل‌مسی در بازی‌های ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/90344" target="_blank">📅 15:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpEVvK9OO5-6SXnfdGysBI3XJ5FODrMr-WQXpuWg8p-OLmz4G8bZIOEaZJ-yyqltXbOmhhr9qRMkMTcKnfq-2jfmN3p-dJMysIcfzh7TdLyAC6f_ZDRLONx7CrNiw8lm2O5LnOYer-YWHVfYki1YA9xixj3QMdLrYvCcsCD25Qd8EeK73bOX2o69RYZLj90BT3GEwdec60BDlF1pL_k9cmTzahgCuWldRHLEMjO88rZ3CAE-ZKP8yvQX4DquhnJBpPCnbUr2_xjuMBBow2Kn0wIKoz-r3rV-uKX-AxSI2J9z-mRwrLmEAYjL71t_VuCdgSXAgZo0xkt5KjC-u0E_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترکیب آکادمی تاریخ بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90342" target="_blank">📅 15:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=EjEfIxq3eDwAhykjpZa-j2SgcLvhbHk0siINDxfkGIDWet2RBqSmc7dtHu0AuGU6Fz3C5xiXHP3a34pk7nSsaOQvwW1ygbT9ROctc058qPa3QI9PrgpzOaEcsx-DduWxnfI5wMAC0rDPdgiFdwd1AkkVIHR4_AfdCuoP1rHWuzXKOt6wbDVMLPinyci81q7e_WCEnOYGrDG4rTm1Jl0tRRYTW_o74WhfsA7zr1gCkeDxDChf6oJDo6WLDptNVtoywS9YVu3LIuXcvnoTSNK4tN1vEZph5VTKJmmCGLxo579XYco60WbKNMCPZUO-FeK3cbPLL8TftDZ5Q5WR9ySSWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=EjEfIxq3eDwAhykjpZa-j2SgcLvhbHk0siINDxfkGIDWet2RBqSmc7dtHu0AuGU6Fz3C5xiXHP3a34pk7nSsaOQvwW1ygbT9ROctc058qPa3QI9PrgpzOaEcsx-DduWxnfI5wMAC0rDPdgiFdwd1AkkVIHR4_AfdCuoP1rHWuzXKOt6wbDVMLPinyci81q7e_WCEnOYGrDG4rTm1Jl0tRRYTW_o74WhfsA7zr1gCkeDxDChf6oJDo6WLDptNVtoywS9YVu3LIuXcvnoTSNK4tN1vEZph5VTKJmmCGLxo579XYco60WbKNMCPZUO-FeK3cbPLL8TftDZ5Q5WR9ySSWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم‌ و صمیمی از نیمار در اردوی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90341" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90340">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=N5yYt45nQQhkZ4LeWMjDV-RLROLOtkRZJ2pWJMIPZk35DQ1QLiuyPr_WBX6SbKqstEZytE_GbWErq_UFqb4B-h9abt9X3NQObltL8U0K7hdiJ6YNwQ96L-Du45aSUj_kj41Al5sh3zjvRxLm6TFJDbOjihLoBv3F6rgzkmL9mYeZGs0JKXEMDFlU1nMOiRSTcC2z0cWCWLAQcFqCY-CBeHKfLhNggWr4Ma9XEqMxvZUj29TvoIZXQafSxPpZ95uRDdZ2j6Mk1-HGPWX6n3aMQp7HQMwp2EkejxQ-YZ4bTrwAMNeLFuk4ESW7vAc5HKrfJYGNQZ-cljzcwmTFoopjnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=N5yYt45nQQhkZ4LeWMjDV-RLROLOtkRZJ2pWJMIPZk35DQ1QLiuyPr_WBX6SbKqstEZytE_GbWErq_UFqb4B-h9abt9X3NQObltL8U0K7hdiJ6YNwQ96L-Du45aSUj_kj41Al5sh3zjvRxLm6TFJDbOjihLoBv3F6rgzkmL9mYeZGs0JKXEMDFlU1nMOiRSTcC2z0cWCWLAQcFqCY-CBeHKfLhNggWr4Ma9XEqMxvZUj29TvoIZXQafSxPpZ95uRDdZ2j6Mk1-HGPWX6n3aMQp7HQMwp2EkejxQ-YZ4bTrwAMNeLFuk4ESW7vAc5HKrfJYGNQZ-cljzcwmTFoopjnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد جالب و شنیدنی هیوا یوسفی از وزیر ورزش و جوانان که هیچ نظری درباره قطعی اینترنت در ایام اخیر نداشت...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90340" target="_blank">📅 14:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=QjGCy_SseinGCAAh8OAZThpuS7WQTNc1NDVzcExoo3w2ku8H6mWIJ79tjU3TIkqFIxoH5rJJ4KFXqdlHvOMsb6l2zmwC0UHAZ9CiXHcgMARIRghEiu-LNq5-orUlo981t30zl-8DdA0eVYU1IHy8RC2RyBN1Bl73Tx1biOTAHoHOUOBLjj7Jo8AWvhDZfwOYL62yANgBLQvQLKAjcpHY88X6Y3FRmsoY1UpDFyfhP3q5nnL0gCK06wsHD21-H-A6XkBlJyA0cYZOhNx0F4bnvn1IvKiVxe4Lwjaq9vZhmiOagTfrZjo_PcrFwGHgY8ymePExrrPFDePothWh7TYbUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=QjGCy_SseinGCAAh8OAZThpuS7WQTNc1NDVzcExoo3w2ku8H6mWIJ79tjU3TIkqFIxoH5rJJ4KFXqdlHvOMsb6l2zmwC0UHAZ9CiXHcgMARIRghEiu-LNq5-orUlo981t30zl-8DdA0eVYU1IHy8RC2RyBN1Bl73Tx1biOTAHoHOUOBLjj7Jo8AWvhDZfwOYL62yANgBLQvQLKAjcpHY88X6Y3FRmsoY1UpDFyfhP3q5nnL0gCK06wsHD21-H-A6XkBlJyA0cYZOhNx0F4bnvn1IvKiVxe4Lwjaq9vZhmiOagTfrZjo_PcrFwGHgY8ymePExrrPFDePothWh7TYbUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پيش بينى فرزاد آشوبى از عملكرد تيم ملى ايران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90339" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMtmJ52oXt4aSGNVFTn1IucKDH7U6PZ9g8VRmLfmXFHfobxc4nvXPmVdx2Gkn2NuxpGFqAK0Xy1F0e3RCMdy5NoYamVJm1lWMN-UVAqLI9HpMANqLDQhdnTrcHW_j5KMQzOhkSlcBhtEJDe5lWOhrx4BGPAAuLpcskx1vMMotF-29tX0aYSjhT0PZEwqIhpZOhgGH1MvR2gFT75QC2uOGwK9e794qo4ChE1j0Zhncsf1UbTeka8nx4Q-bK76I7TNH2PkNg4TPYJQHbye9ghOi-Jlmxm7bYlBfzoDwsBq4nap_aF_MBt2cmPKyx_q2TKZjH-h3wi8adAThMiOsFJMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۱۱ ژوئیه، ممکن است شاهد پرتماشاگرترین بازی در تاریخ جهانی باشیم.
🌍
اگر هر دو تیم آرژانتین و پرتغال صدرنشین گروه‌های خود شوند و تا مراحل پایانی ادامه دهند، طرفداران شاهد رویارویی نهایی بین کریستیانو رونالدو و لیونل مسی در مرحله یک‌چهارم نهایی جام جهانی خواهند بود.
🤯
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90338" target="_blank">📅 13:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90337">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYLVRYZrJANWWQ4uY33MOaEKoAaxwRxjGQ_a9BZX6kemRzJCekNys_OvvFB3Se4PnJnM02BL7tEDU_XmkKkBCEpjrAX7_-sLJ0TEg3j0tyfSOjvgOe6Nju8-WygK6YnraQKDgqjlLt7hR_bnw6vBWawdvrbnlwXCrK8VN80Xp_dtrDPE6okxSOdQBCiYvPUKqHSSsh8mg2A83SVZXGv_2Aaye7oOuPvEYWsRRZqTQJblSKCazQIfHDMgZ8xfHBVkB8OZMwN8lF4mxr9OhQ9dlXRJ13mJg6TX3qjCmPN2dSX32I2Y_2swV6Ut01MI5jLaUYXVzOicFSOIVPi-tpCUJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره ده‌های تاریخ تیم‌ملی برزیل در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90337" target="_blank">📅 13:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=KzPMdDzrRysFpFvBZYC8WgJuiTleFsxS29ItMbMcV2G2H8rrTKI0ETtuJT9RP6azZzEr0ygd6aeYJLHZS4ztHZynWPCBmTPUhjFZORm_lOpQqPJqbZs3D0oPO8vGDtVO-M2iZ3wegm7sg4YUFNl7mfM4GwWYokThHsSUjqclM6hkE3xQKgGgodiNXLvWJbNgrGCnYflVUW02UqcjOXVUQp9PaOpamkNZSde0zLlZ1lqKkZK9oHR4NroMb1GSrOL-zTePjfzROKTZXS29zWKU0yMBoPszVWUFmhb-0MkJkwZ-JXwsgZux5_AyN2J44apNYRU3WxRBEK5nWHSzB2FEDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=KzPMdDzrRysFpFvBZYC8WgJuiTleFsxS29ItMbMcV2G2H8rrTKI0ETtuJT9RP6azZzEr0ygd6aeYJLHZS4ztHZynWPCBmTPUhjFZORm_lOpQqPJqbZs3D0oPO8vGDtVO-M2iZ3wegm7sg4YUFNl7mfM4GwWYokThHsSUjqclM6hkE3xQKgGgodiNXLvWJbNgrGCnYflVUW02UqcjOXVUQp9PaOpamkNZSde0zLlZ1lqKkZK9oHR4NroMb1GSrOL-zTePjfzROKTZXS29zWKU0yMBoPszVWUFmhb-0MkJkwZ-JXwsgZux5_AyN2J44apNYRU3WxRBEK5nWHSzB2FEDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیب منتخب سهراب برای حضور در جام جهانی
👀
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90336" target="_blank">📅 13:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین پیشنهاد بارسلونا برای جذب آلوارز رقم ۹۰ میلیون یورو به علاوه آپشن‌ها خواهد بود. لاپورتا قصد داره قبل جام‌جهانی این بازیکن رو جذب کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90334" target="_blank">📅 13:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90333">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری از فابریزیو رومانو :  بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.  خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90333" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90332">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqvGgnkyOWWgwKIPjVLg_9PhdTphCQ4hkcFn_wQFV1rU6MsbVycHYzMUmsZ3YZ0XZSIUHEQU0P7V1KlbN272q84zV-0Sgj89yDKHYFk32pPaL46qpVuwZ2xPdJMd5E1SjaLyjDYZkXsBB1N8nlhN-9A38FUWjOrANo1ugzq1S3nDO7Yk5OlCaxkYfWZGSwKov5Ik0Z5RkcinmVJ3QTKrhU8rhlCsb6lkcv6liJ93yw-7X4jf4Bf3FpSxFw8S6-4m9pqP_Ox51zT6fAOR-99WIlk-wwk-uapf9RY3eAi7YQbEkjy4_iNXhpx3KkG8RfP6clyQn2Ym8LIZ3IoQkUSUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری
از فابریزیو رومانو :
بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.
خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.
پس از ملاقات مستقیم با مدیربرنامه‌ها و واسطه‌ها، بارسا پیشنهادی ارسال خواهد کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90332" target="_blank">📅 12:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90331">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=kvJvpxriePeLQaEeU4_9XnvSdgGRAnEcaNV_PxxeRnO653urwGhyeD7wZED8LrHO6oJwoqPpcbK7HCtujKTMJQAxdg0H-zZmtxOQVKifsSXvwKPNxtrclytWY3cEDrcmHxyKdde3TgS3jMMp5fFjTOjGvtXimRy7t31dp0enjbtGbt-xggEDIHOhvPtNCG81SZ5eDmSYsTS3VMdJ8wn6UZ0NTlsrw4CEPmG4O5x2xN_LHl_1E8ZhTYuIb6tepXzrHOg7CM4Bz71qUb_vNs4nLMa0ZFck_E9G8jJYkYbwwRpCAIBRxECmA6YrjG3QSI-0g1ZiXxQQHpbex-iyLCjUdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=kvJvpxriePeLQaEeU4_9XnvSdgGRAnEcaNV_PxxeRnO653urwGhyeD7wZED8LrHO6oJwoqPpcbK7HCtujKTMJQAxdg0H-zZmtxOQVKifsSXvwKPNxtrclytWY3cEDrcmHxyKdde3TgS3jMMp5fFjTOjGvtXimRy7t31dp0enjbtGbt-xggEDIHOhvPtNCG81SZ5eDmSYsTS3VMdJ8wn6UZ0NTlsrw4CEPmG4O5x2xN_LHl_1E8ZhTYuIb6tepXzrHOg7CM4Bz71qUb_vNs4nLMa0ZFck_E9G8jJYkYbwwRpCAIBRxECmA6YrjG3QSI-0g1ZiXxQQHpbex-iyLCjUdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینترنت بین الملل وصل شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90331" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90330">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👍
👍
#اختصاصی #وینرو :
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90330" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90329">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkY_sToxNp25bF75Kd9aIHtGCATFP18aj0FYr7RkeLacehoawvMLxr1Xwn3Ff8aF0UnejQ2Wm_fghAda4fBx_jWBoXTOXoVhPzWDR55_xZsR1M8Y_3u3nHjdTYKK96zPgT-aqWuUzH2d2e2olSk2xI_PYu7Nfd9XQRKpaFEccee0MQMcjn_dOxfe_0j-FebAKfXqsu70fyRIh2Il8VVu9I42UK02ukGmxEpwmwd8rTl4WA1BltzSfhLUlcBqmHZ3WBjGuny2GWsVkuGiGpbsZWfA21a6khhgPR6bnmavalwdcX2PQV2a-Dcv0e0kKwE88pXKBWrf9k3ymtlp0IP5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90329" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90328">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=MWJLIGhZV9KG_3AgupyzpLhtU18HiVEmVTB3aKUp2Z1TWJHImGiGrDK7jsAci9wxtNj0BA6Npl0eQp_62gvlF4BcuF8OCUGoBr55y1wHFq96QYmlTxFnN_-XEgUS4lz1pdOVGhBQZk_RHkm2jqj-WNZxLpa2x8rTczwossg539yHy69-skFHMXLKD0Xnicvo4grAv6WCM_SpF6BKT07zd4f364ygrglna8fMVjlS1BaZ9HVWy-Jy0GW-LX6J718foEuUw-nfu8ITQtvi8KFAvTwaR13E7gxz_TZZUFGEKxtVxdzKSNgzifsEmyXKn2QqZR32SWYsIv1xEJA-ofC4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=MWJLIGhZV9KG_3AgupyzpLhtU18HiVEmVTB3aKUp2Z1TWJHImGiGrDK7jsAci9wxtNj0BA6Npl0eQp_62gvlF4BcuF8OCUGoBr55y1wHFq96QYmlTxFnN_-XEgUS4lz1pdOVGhBQZk_RHkm2jqj-WNZxLpa2x8rTczwossg539yHy69-skFHMXLKD0Xnicvo4grAv6WCM_SpF6BKT07zd4f364ygrglna8fMVjlS1BaZ9HVWy-Jy0GW-LX6J718foEuUw-nfu8ITQtvi8KFAvTwaR13E7gxz_TZZUFGEKxtVxdzKSNgzifsEmyXKn2QqZR32SWYsIv1xEJA-ofC4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشت لامین‌یامال به تمرینات اسپانیا برای حضور در جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90328" target="_blank">📅 12:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90327">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuVhRHPupJAe3h0KEPSiTHJcpE6XHf8bzyjJtvautQ67D8kLZwEseTbTaqL8JdhGZ1r9IhX6hW1rTSXnjRG_N_WLCcah4ba9rfjy1uPGQwcvEl_X3eDoNksGhwVL6Xk7Oh9Va2kG-H2iopUIhCqDlKxYKTkoxWzVSIGA9fioXyc7CxcCuRHAu_SN3p8RVw12UbAfeE-rgEhsstryBHUkEvSSEoB4GCxxc5znpdBSdqE2ri4g7rbOqY5bjJSQ1FO6dByFQLrvbFScfzlAbwsRcHpE764yMksKWvIUFjyEm7heX9wBcvI8KVEWLecfNJUH1AWQa8UTPs4Mqs2kVRUS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین حضور توی سطح اول فوتبال انگلیس
آرسنال تنها تیم بدون سقوط
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/90327" target="_blank">📅 11:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90326">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=cSZW6z8M-M1VOEntmWJTCYDgDPkyTGw6A-o_uCSMdM8CI5tmQ96TzxYLA5xbMcLJzKH_0cG0OSJHR-94-EwzDjvm-_oMCVPcv3BxO9043YN3ojWm4Px0AYhTsp5VglYZVmPSKyoLsJpDAdJ4Y0NmZAYs8yv3UnXEHnuXZQ1L9979zwG6WpKsRFqpjsaeCFADyZgAWAd8FXpd-t3FRPvmtLMMJLDTBZSdme62pfszzNPsTrttyGhMwgfygI4MnSTUyEhCfIn_80OS-BMBFdn3jDwrFkHBjOTSGVFr6-mXJJb3kh0YvrGHBhEIE8iZEbozdSSgA6C7ky0WA1xi9Xwfqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=cSZW6z8M-M1VOEntmWJTCYDgDPkyTGw6A-o_uCSMdM8CI5tmQ96TzxYLA5xbMcLJzKH_0cG0OSJHR-94-EwzDjvm-_oMCVPcv3BxO9043YN3ojWm4Px0AYhTsp5VglYZVmPSKyoLsJpDAdJ4Y0NmZAYs8yv3UnXEHnuXZQ1L9979zwG6WpKsRFqpjsaeCFADyZgAWAd8FXpd-t3FRPvmtLMMJLDTBZSdme62pfszzNPsTrttyGhMwgfygI4MnSTUyEhCfIn_80OS-BMBFdn3jDwrFkHBjOTSGVFr6-mXJJb3kh0YvrGHBhEIE8iZEbozdSSgA6C7ky0WA1xi9Xwfqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تازه خارجیش رو بهتر بلده ..»
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90326" target="_blank">📅 11:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90325">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔷
#اختصاصی_فوتبال‌180
؛ مونیرالحدادی و یاسر‌آسانی دو ستاره خارجی استقلال برای ادامه حضور در آبی‌پوشان خواستار افزایش دستمزد و پرداخت به موقع حقوق خود شده‌اند. سیاست مدیریت فعلی استقلال بر حفظ این دو بازیکن است زیرا پیدا کردن نفرات جایگزین در شرایط بسته‌بودن پنجره نقل‌وانتقالات عملا سخت و غیرممکن است. قرار است پس از جام‌جهانی و مشخص شدن تکلیف لیگ‌برتر، جلسات ویژه‌ای با نمایندگان این دوبازیکن برای ادامه حضور در جمع آبی‌پوشان برگزار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/90325" target="_blank">📅 11:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90324">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxPTAj4-2aFdHqZ2NT77m0chSrHAoW9K5dv7lGax_QK8TIROqJfEo7hHN7ENPlV0FKhkaYaWAspEuXemJhI4uA9yYIdFY6iLZWa4_9xCBKGZnLTodC_-cwU415NmAC3sMNdh2julY5e1h6DdqHcgE-VGzBYYvXGqDiUKIq3TD16oYA1jbkE_uwld-ioVG3V1iyROvUIzWbEh5k70cFshAvx43yQRHH4PxPFwjaKZQXnEiEy2WXGJQDvlf-osPcnJJFjPjpjUj1XmdYRfKdQ1kRGCjnzNl1oZHwWJ1vtlbWAS5cBMj0KvyAjvjpsX7kx_RD19sAL2TUaLrY3HbCIi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شب‌گذشته دیدار مهمی بین سران باشگاه بارسلونا و وکلای خولیان آلوارز برگزار شده است. این بازیکن شدیدا خواهان خروج از اتلتیکومادرید و پیوستن به بارسلونا است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90324" target="_blank">📅 11:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90323">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK_t0VmPtGfqAobLj2D5Ca_gDZAPwE1TmSd4vCaOBUl3y0MVB2aR3JqbqabjwS5Y32bRnQch1D0g6mNXxFTgICHWQudUKTerl33O83NzFkXBdbVmAc1TLmEIIgZFWzKSld52QTaPAvN5v07uurOPjdI5l21H4hQCISWd3nVYHMybNM9zaRtOh6jPHBBv3maM4Iz1C8w-40oFNzvqvhovSLRhiuZZYnYAQuV5sxYstDlN4OgMV2RHCF3oc3k_wtJg4bac1OvNl--3AKLPRzskT9nG24ePxQXsMCiN7ZhQ-OLWVoVsGBX6sBTxkXwXsrTuJahPe8SutzNW1EfH2fiB1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان تاریخ‌فوتبال برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/90323" target="_blank">📅 11:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRThaaRELeKha-WD4xcFHb3_HbAbig_82qiXWLz0JcludfeNmA80gwUJj9u1MerrFdXCoLpuBscubgVkz6Do2s8SjuQUMYEdsJeKxDHO8e5rb200dSgPTsyZ8soEZrMtya34DsFTdv5KgNYNaBu0b03KNBkQu8YAmMtNK7riN1CiymWhbRnOKwhQzWaeh7XTSu7iaFaPShpRJIKQgx33jHsicnCKDOk8qJBxJyylZvSZUp2bQtJuQ1WL-gWFZaaMePo2ufzYr9ZU0Rl4dpiHKMyCoJbn1gSEHSS-Kkk1EI3R1MQvvaW8ufotU18DxttZBMdhjVDlSK3YOWmVn_yCLLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRThaaRELeKha-WD4xcFHb3_HbAbig_82qiXWLz0JcludfeNmA80gwUJj9u1MerrFdXCoLpuBscubgVkz6Do2s8SjuQUMYEdsJeKxDHO8e5rb200dSgPTsyZ8soEZrMtya34DsFTdv5KgNYNaBu0b03KNBkQu8YAmMtNK7riN1CiymWhbRnOKwhQzWaeh7XTSu7iaFaPShpRJIKQgx33jHsicnCKDOk8qJBxJyylZvSZUp2bQtJuQ1WL-gWFZaaMePo2ufzYr9ZU0Rl4dpiHKMyCoJbn1gSEHSS-Kkk1EI3R1MQvvaW8ufotU18DxttZBMdhjVDlSK3YOWmVn_yCLLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از عجیب‌ترین وقت‌کشی‌های تاریخ
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/90322" target="_blank">📅 10:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J81Bb1kELyyvt3qQ2E3x2egjkbiqkN0WEoBYwhGYGcZFhHcUXoNWLzRLwZc0ArqjEE7zxkanEnxl81ieRtHyLit3n9GH6N2h6X7UviRNy6LPKKfqtyob7oBy821LS8fjX3-nreTDKHUnKcJcKCpIXONjSGWufxsc633f3vBdj5rANqAqrBAGx3ZqRYs3Qkjl4KkPB-uOXfgWhN-Fv1cBRyDdYD-fsJoq0comnD7YHr0hvgVmrbNsaCLcSZtmjmM8-4B1hOX48Ey8C0KX3Syp0RNL2xj9HJId-Y0VCMRS92UBVpa6pUfBK51H8-zhYzZz7CEtKimskd8XYx4HaIXt1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه‌لوئیز سرمربی جوان برزیلی هدایت تیم فوتبال موناکو را برعهده گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90321" target="_blank">📅 10:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFifcoNBFY1qRDX9ulDEwhz56HWi-iM31H1QqfCABNapbTp5DWGO1mRqwdZaBn2dmjaoDAX-Z7y_FKFQYRyE4_CZWYiDG8Py7EJCPwAStyTNiqHomqYEBCEZnyWpftkh7v2-b_niNx9_VDcY1098XZZN_SaR-W3gfnb8sp3sp6jbufx3jUAIRSHDKP37prB_I4q5NIVL3EjrptbrgJPzh21KoS2tFPmEFzUiYUqzQF3bsoiQ8kbvyWQUoRpOWAO7r9Y2sM3C-dbN9__27Sad_Wuq8HRkNHvAwAj-Fk4UByoiOIpRNkoLrMIhdGZX2lEYPT9appKA_TkwGmQ5F8LndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90320" target="_blank">📅 10:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f9845215.mp4?token=vMG24AqQDoZW2o6hhqTXrU2GwAQZ-piUJmpwJ2L1APWu0ozNyFskPP4WZ6M_Bh_1uMXBgCgdXFeULowTdZtu17ZU7-PQuSXB4zuvwHD9qn8G-qFZPJ0bYoKxoKuPdavPnjAHexyoL3DgDCfqOw0ipdXnUfMhFpKJ87jaZtS8JPn2dgPmMTmVTsZinOuTtdns7sAzZi2UB0bGQvbSkUv0dnVS6rraSD0efUVy38fB4rH7yYqIgXR1a7NcLhCtRL_n-BnlaUpjjw_JHqLbfkwFArdyKPq0sQ9qdYjYNFnePIu_01Mz9FrR0XtlIjAMesUJS2DNIoftVoYgsL7HX-lReik1uWiyf_5P9DwM2OEOV10p6pFGOFv13g8zcAJZE-sgXO2Q5HWgvF-F4-H7INb5WG6oM_kT_x2dObg6gdgdRiGP64n5mvG7u6_utIwO5ZeZ05HUWVjj7M7qdFBObWgszyMd5tsXyIlQqxr9gOubpTsnN4B5E88NMwhmzFQ1Op1OZDutWkdJakydFZuoaKsfj7QRyaqSgkpq31FVBugEd966rFvWIAUlPKISRwZUENGRua7pwnfIxDCvMNfKN1pmMzwdwoe2J5OL1rQG1wcJU9BKK1_YaFia2ZuNA7Fzq1BOvlbP6U_ZhZ44fmXDNf2RHK2ce7ncqUe99qtkSGVrong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f9845215.mp4?token=vMG24AqQDoZW2o6hhqTXrU2GwAQZ-piUJmpwJ2L1APWu0ozNyFskPP4WZ6M_Bh_1uMXBgCgdXFeULowTdZtu17ZU7-PQuSXB4zuvwHD9qn8G-qFZPJ0bYoKxoKuPdavPnjAHexyoL3DgDCfqOw0ipdXnUfMhFpKJ87jaZtS8JPn2dgPmMTmVTsZinOuTtdns7sAzZi2UB0bGQvbSkUv0dnVS6rraSD0efUVy38fB4rH7yYqIgXR1a7NcLhCtRL_n-BnlaUpjjw_JHqLbfkwFArdyKPq0sQ9qdYjYNFnePIu_01Mz9FrR0XtlIjAMesUJS2DNIoftVoYgsL7HX-lReik1uWiyf_5P9DwM2OEOV10p6pFGOFv13g8zcAJZE-sgXO2Q5HWgvF-F4-H7INb5WG6oM_kT_x2dObg6gdgdRiGP64n5mvG7u6_utIwO5ZeZ05HUWVjj7M7qdFBObWgszyMd5tsXyIlQqxr9gOubpTsnN4B5E88NMwhmzFQ1Op1OZDutWkdJakydFZuoaKsfj7QRyaqSgkpq31FVBugEd966rFvWIAUlPKISRwZUENGRua7pwnfIxDCvMNfKN1pmMzwdwoe2J5OL1rQG1wcJU9BKK1_YaFia2ZuNA7Fzq1BOvlbP6U_ZhZ44fmXDNf2RHK2ce7ncqUe99qtkSGVrong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برزیل و هواداران جذابش در جام‌جهانی
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90319" target="_blank">📅 09:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVEgq-GbqJIzSh-wGYVOwKJSq6VWZOM0PP_yorFLusRyKNA2wPHrlu5wc0n0MJpMTyBafUJdvUcI253N51x7RbmldyiP1DSOoNGsmgST41k50vrCbVFNQwI7QtulYpNVTnfRhAaSPt_2dJCsbVFgELz5bDEXRMn75Jg54bbe7ZeWUJ764nNx9YmuoFQ-b2Ct7VeYyVWktT62l4BibojRqUwSzHlGz_o1SRqdake_EUOudXyJklKxfJtDpoE0tqrBFuMuWKnYQYQeQQdatDTKp8mIEnv9J_FGhjpDGHVXysd54MHPJWU1GPUf-PbEkWjyrmIxxG-M-x0MPbAZfrG0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرافتخارترین تیم‌های ملی تاریخ فوتبال جهان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90318" target="_blank">📅 09:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=RJaytW3nQIIAQ-KWidrWOvQOTpod-9sip1yWoN2Xzm4R3JVQCJmWSi4tgtAx_mswS5gTE9Cvh2_8sbW8B4n7vJCyuMNunAB0HOP_RUZj77epVh-kreoGa1e2gb00vKRFqjH9StsmhQrIq-yOi73n4nuhkwdPWlYxu8EJFq3VbaD4pDhuweyEkfpHFhK1VBvb9NnlU1eh-4p5qYShX8l8jmGSXPRxFw8-6-goTiAFNvk6iTjH6USM32nWuImbg-rp0Ztt3sY_j1RBMSW3TiMFClPuYdwoSfzv1jFpi-g8r7KkBGGr8MsU8_1y_ddw-0p12ult7kZh70pAgrpJtAleWUy4mS3e7Wh2XpQ4eHxxSjQbHPbAgXRD-vxlFO4sckJSxKrgTvSv5nFWMF4mXXC2KZdjwtWgo5lHrDI1URd_1wj896LcM5sseDBVxGxExWhVtfcY-LyYIpEi8ezqRDYghHMpbBSsocXaJsUpLbl8dZjlDmYEMffDqf--rwE3EPf-xMvcTpPbz7bbNR8Dz6Brd9Ve4wqdeC_NjCAdcYgQHWdnIGimF5O3HNlEw9Yv9Ox6ULr__gH6yU5JdCb-_a6ibxE8CqXvs2yYA9VLQBM_4nKx2WLCcY6Db3-ToTO-m0GImztHUaEgIxM3bdbhpresCScQmbNWNhSPiAksgz3bMmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=RJaytW3nQIIAQ-KWidrWOvQOTpod-9sip1yWoN2Xzm4R3JVQCJmWSi4tgtAx_mswS5gTE9Cvh2_8sbW8B4n7vJCyuMNunAB0HOP_RUZj77epVh-kreoGa1e2gb00vKRFqjH9StsmhQrIq-yOi73n4nuhkwdPWlYxu8EJFq3VbaD4pDhuweyEkfpHFhK1VBvb9NnlU1eh-4p5qYShX8l8jmGSXPRxFw8-6-goTiAFNvk6iTjH6USM32nWuImbg-rp0Ztt3sY_j1RBMSW3TiMFClPuYdwoSfzv1jFpi-g8r7KkBGGr8MsU8_1y_ddw-0p12ult7kZh70pAgrpJtAleWUy4mS3e7Wh2XpQ4eHxxSjQbHPbAgXRD-vxlFO4sckJSxKrgTvSv5nFWMF4mXXC2KZdjwtWgo5lHrDI1URd_1wj896LcM5sseDBVxGxExWhVtfcY-LyYIpEi8ezqRDYghHMpbBSsocXaJsUpLbl8dZjlDmYEMffDqf--rwE3EPf-xMvcTpPbz7bbNR8Dz6Brd9Ve4wqdeC_NjCAdcYgQHWdnIGimF5O3HNlEw9Yv9Ox6ULr__gH6yU5JdCb-_a6ibxE8CqXvs2yYA9VLQBM_4nKx2WLCcY6Db3-ToTO-m0GImztHUaEgIxM3bdbhpresCScQmbNWNhSPiAksgz3bMmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جذاب‌ترین هواداران کشورهای حاضر در جام‌جهانی بدون شک کلمبیا هستن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90317" target="_blank">📅 08:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPnmqZXc-6l-XBsjuGjwUBCvVY_AWeZ-ZLjiWq0lnOS_rkJ-XrSc2jeA3L3_zfE-NqOFfO6bKAWSFISwK6f5VZ1tBBkNVmDZFr0g-cc2bLA7VZ_BwVAGAuz1b54SJsoalTBqW-caF1qeX604raky1fOqSQ94rkoqGOmj9ZnFtawDTnSdkCcqQHBN7th74ly6M_6wbtCxuv-xDlEW2OPV-1Rv93ff4bhPzNDDVgx3jLBdey4jHPQ6hRW04ZIK6W0juzkFXvKEFwabgiBlwnOWe1JRmCf4-nC0ayjmjWr8LfMy3EbS3lSuSQpOAKj8jFbfz85k-GyQcNdzzeGtm5c5pQtE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPnmqZXc-6l-XBsjuGjwUBCvVY_AWeZ-ZLjiWq0lnOS_rkJ-XrSc2jeA3L3_zfE-NqOFfO6bKAWSFISwK6f5VZ1tBBkNVmDZFr0g-cc2bLA7VZ_BwVAGAuz1b54SJsoalTBqW-caF1qeX604raky1fOqSQ94rkoqGOmj9ZnFtawDTnSdkCcqQHBN7th74ly6M_6wbtCxuv-xDlEW2OPV-1Rv93ff4bhPzNDDVgx3jLBdey4jHPQ6hRW04ZIK6W0juzkFXvKEFwabgiBlwnOWe1JRmCf4-nC0ayjmjWr8LfMy3EbS3lSuSQpOAKj8jFbfz85k-GyQcNdzzeGtm5c5pQtE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی لطیفی پیشکسوت فوتبال: کی روش شارلاتان بود، پول می گرفت و بازیکن دعوت می کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90316" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎯
شانستو #رایگان امتحان کن
⚠️
🤔
میدونستی توی #وینرو میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90315" target="_blank">📅 01:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90313">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIUHkVhZAgo66oH-Sd-ArPWdEqnJECzOAVdHoZdvmyrAFVmraysXdKcW9D8nNsDCMeS8elDmTPFGml_U3jq753eveeckVpD3QiPvcDLuwMvhwOv0x7tmb_62nIxdqrn4VC8cSZO_LXm7mMdCmi0XCMzSS1__ooErvcWITUgYa-n3vK1X58dC8vs77O4szFKjGMNdjtqHWCyIyTJymbKYOFyc5j8O2P6flHwhFz7I5plkDheoLN0Jhk_eOxURxurtrbL4A-Nb9RYPTGVe91bNpX6fS9xNyiRS0fOW9w4KSvkzBx8VtcV9iSLilWhkH6chEcUvqEPpZQjmpg5SsFITfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
🤔
میدونستی توی
#وینرو
میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a6
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90313" target="_blank">📅 01:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90312">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7fCeBsqOE9Xn9QR9WA2uo-vhNpokp1pOwM19N8C5-VXZETVvY9pFYnvWv6rmSCWFpBsUB4ltfSnNmdnFI56ylqvcge_n5w72usunReAfnDTtdQSXwhUpRSGtK0nFvK0NlzRBgO8Htcz7ysh8Qu3KtGm5y4tKYDC6eZjXnQckxevBnYIM3qtj_oGUpkAmb2bmcBAifajGdYWMsu_Zj8Ny9sOS09rHT0j8whyGqwfDxKm3sJXiunTJhNlK_MSTPi6tFu5o6KlrnAjHe-wb_OPhWxrFF4Oa3vpLXlGFM8d_m67JdfMH5gmQMvXmAuquQju6iEX-5Q3PtBDkJBbEKGnaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌فوتبال کریستال‌پالاس قهرمان لیگ‌کنفرانس شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90312" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6tkmr6d1TotUIG5FnKvlzWFaK3S0iPfNMvBYMRcPH1r6dPq-hjLWrg5f_I49trab3TFwflw3E4_PlGZq6bf6KaW4UyBbWMxw2ygcS0UeHKveqvKfi0OGtlNjY_1fx2B-gR0IT4EQ-sEi3v00Kc4-qVL4raqj-phobHBvPnWILZScxtDQFraOSWatn_4loWx2-sQEwZn9GIteS7aHTSCl6OOyYtiV3dWin4KM8o1HwSrO_gtneRbOy7tlJEop1JYMCRdyde5T-k395JtiRTsN7LKgLVlCt0PvIqbEJhoLsHZ4aeDf75UmLvB94GEhKeRdi_GI_nYROPsleCin07ndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافو تنها بازیکن تاریخ فوتبال است که توانسته سه دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90311" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
برخی اخبار کاربران گویا این است که سرویس گوگل‌پلی درحال‌حاضر رفع فیلتر شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90310" target="_blank">📅 23:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lseTzUP8usm_neCjTbGIo_GIfNfd9uprMwaF0w0XeKvfY4PVrKc9tJ-hu0CBIXPLahw9lBj3pmEyZpoT2fJwYth76qXeKdkXcqkHGnCOJJrFHQ-jfoXGTHjJ0hIWzYstbZGk3x_g8t_8qd0Zv3UkV_1O9wiFLU4A-Fxt7h55XLfCJFdZquzbLzZzmcuhOMpYqzb18hHTsM6c_7NcM9z47iy2h4JIc7xoI9IX9513RN1Gx4A9qHisOC_ezCo0X7JI-4euQ6_cQ6CpnMJ6f5gA3sKbPMo9JssMqhM6Cyf6tzLkjwh739RdxHxyMvpPscYisNTqhFG38LdIRmwBtcToog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد تاریخی اسطوره فوتبال مردان و زنان بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90309" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQlY7k96eb0_O3rpaMNJZkpWu-IQLHNj4udvCIWHvPPrc3A9C676BQ5AQWD6m5zO3t3KAzX0BwM4ltw725bqGOhJm6WOn1qV_o6JcOz_3hHUksXDFUILyevOEdu2IcfhKmkDCv0gbsewFRbGNDs2sStJ9o2An125q6Rca8w-ugzDpVmkZGiBYCK7CWbhITQQxU58PCgfc1xm2l7JEUe19_72igB-VwmClWo3tXKKahVeK01UoA6FDvkuYbEfdaYTQ32fOwWSgsooeN6MLANO-mk8aJinPehKXC8plQFc4LJqucftteyf-6BAPNMstFpW6qbmqlSA3OfxMJb-cDUsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90308" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84204a485b.mp4?token=jmZk-1rm3-AjLYsPPEYcr5KQwZ-jKlbNObBowhx0fnSOEkoO56BTFXSE267F5jnQR7usnh9LTRw1oIIrNInD7proUt0Mtqs4_aIBQlmNiWouvXflh5HEYK1FsFk4CCKGqkZiFz6_44f_z3G5csft5hymJ8VsZs_HXXvj5yKCZluXRpceQh75HkmJepTUP7uWXSdNrsSMfm8C_MV8b41ttAAbzcn2Gtk2D-BprKln9YvV1PQz0tOo4TOYEIcSjNFCAUAe4BXm-fPkzI5YPocSR3YrrjSoT_xg6i_opKN1c-weTpO3aCOaMrgYSqzRYvrNhtm9rEQz7EeMRepRHHb4JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84204a485b.mp4?token=jmZk-1rm3-AjLYsPPEYcr5KQwZ-jKlbNObBowhx0fnSOEkoO56BTFXSE267F5jnQR7usnh9LTRw1oIIrNInD7proUt0Mtqs4_aIBQlmNiWouvXflh5HEYK1FsFk4CCKGqkZiFz6_44f_z3G5csft5hymJ8VsZs_HXXvj5yKCZluXRpceQh75HkmJepTUP7uWXSdNrsSMfm8C_MV8b41ttAAbzcn2Gtk2D-BprKln9YvV1PQz0tOo4TOYEIcSjNFCAUAe4BXm-fPkzI5YPocSR3YrrjSoT_xg6i_opKN1c-weTpO3aCOaMrgYSqzRYvrNhtm9rEQz7EeMRepRHHb4JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی به سبک لوئیز انریکه درحال هدایت شاگردانش برای جام‌جهانی فوتبال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90307" target="_blank">📅 23:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpF-8scugNsijrERs1waxWxfZdSG8C11jbRkV8wC-B3IIuZc8eHW8KOeXH3JgKzR8tMe3RzhWPrriNN7VpNhIbf4S7t39nhx_E-BIVhR7F_dqkrq1ZKwtlMpKpAxi2yhBd4WjrYUebJ6sGWz9OT3MJzfpRZ7ioNpvYbcsabtN_5P0_nNd5ck52H6gMIVQ43S_zL-KRrjCJD9rHc7A1FvAs3X3XYG6JCIAmHr_3WpRnryyzhtBWr6mJddWFNmHY14g5m26lveUAMnWNOueCe4i-c44CDqpXS1qty4xAX6sr-bgAaJZUZ5yRMYKZkxgC_WsC2O2j8EmuOCdtdjGuVwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی رابرتسون ستاره خط‌دفاعی لیورپول با عقد قراردادی به عنوان بازیکن آزاد به تاتنهام پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90306" target="_blank">📅 22:58 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
