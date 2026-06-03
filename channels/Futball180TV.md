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
<img src="https://cdn5.telesco.pe/file/lO_TI58Ueh6tuC794hPzoJmJuV6wfbk3rQ3fzxlBWu7pZrVLA4VSRqyJFQKd5dUjonz5kSR7la1hItT7T3U3D7jW-FVfAy2WVKh05qhTj7VLMwHjLOrbRMNOvQMug2t53bzMwg0CsVMGyweMhNlvfvPzkEawGs-azcwZks6QAr-EusXUgJ7EizoNInmkZjyOaCEiaaadE7ScI50bd9Vdl5pr8bdd2zexxRx1Ucw__rgXOj0UHdC-FBgahek8QaCDUQEPtPbqNw4_zkYmY6a4x3PvSnZH-Nqe3mJFBNehoJ7aAz60bA_hAap5gFYd6ZdQho7L1qi-XjgNmg7RluU4pA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 164K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
<hr>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKTrDeTWnLXq_WVylAs3YrhxgVlpkr1Dh9akhjg83543HFmjewkb_0C8EF8o41T4IQWJxsLSkKwEQRW0sn8Pfc4XdOpjy1WjSsObXgvIjIzRIzz_xkGYMtjSDW2BnA_npx7AorqhWhdHFFaUbp-uYY_kXJw4nHaSZClYhrop7-MLMQQovoB0ozY7rVnw54S6XitZmMa22ltpBv1gTicyzblQ5VdDWFsQRXE6a3DMZ8liWMWfzMl-N-Y4F52ultRdQjeTyLJxk3Vx76gpgfIKviXBIjiZkGB8q8aLMtbF8QXHhJK97bkN-t0Iy4OdFxkqxnFIfLYN4ssIJu2bkernGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ در صورت منتفی شدن جذب گواردیول، رئال‌مادرید با درخواست مورینیو بدنبال جذب کالافیوری ستاره آرسنال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/90824" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=MRjUhCSvwXVnqB5KE6y6AcTr8liY8o354XlsTqhWDAOGTATfhHRJUEHeeDiFAFTiu5EFakPcp2SGBgsGKZM25AT0VJmGN43uqZx5jTYz1VlhfA_S1T7VTym2HPGvB7DMeYB8gui_DEGPMDcrInTbPolDrRAfTGSQWimgxqPqZHSr_x1X4uhdKWnzno4hcNh3TCKdWFNv4_PPnz5GOM1k00wWNNsbp2cUF-MhS4Gy5FH_jDEt2nBkcz8W01TYYVs2uGp6UvNTrhl29GLUci_O2ICXIim_Fd9jgBm48WX8yCrVcRN0sZYy8m4xZPcmE4GmeBI-DpmPqX89zigHZIvmE3AffcZXmzWCJhiLApnIolz1WMJxR5ByLX1v9K3v9BDm9TLVSujT2tUKm2fAOWsfiQnsQDyPHc4yIv-N1txs_q4O8cygP8yPHEAEVnTD-Enb6YL7US6CEuC4jkgRBh-HLDyZAhE2yW4LkBRqNJCK87DeZRr89XAMu4iBfmcdH8yXxvkMcAt5Sp8ro_sUVLc6a19Kx1q1x58zd5VZSNN2jRZumPmX6OZUORsi8ARO8HyYCeAeeOY-KKatIvU8OSN4LTwZvjj5lrHbJ5P8MqBWxCysAMhVxrwE39zki2BjRv84J87d0DWrHr3sN5YXRtglOICvJGTqCEEOqQr7tfz41UE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=MRjUhCSvwXVnqB5KE6y6AcTr8liY8o354XlsTqhWDAOGTATfhHRJUEHeeDiFAFTiu5EFakPcp2SGBgsGKZM25AT0VJmGN43uqZx5jTYz1VlhfA_S1T7VTym2HPGvB7DMeYB8gui_DEGPMDcrInTbPolDrRAfTGSQWimgxqPqZHSr_x1X4uhdKWnzno4hcNh3TCKdWFNv4_PPnz5GOM1k00wWNNsbp2cUF-MhS4Gy5FH_jDEt2nBkcz8W01TYYVs2uGp6UvNTrhl29GLUci_O2ICXIim_Fd9jgBm48WX8yCrVcRN0sZYy8m4xZPcmE4GmeBI-DpmPqX89zigHZIvmE3AffcZXmzWCJhiLApnIolz1WMJxR5ByLX1v9K3v9BDm9TLVSujT2tUKm2fAOWsfiQnsQDyPHc4yIv-N1txs_q4O8cygP8yPHEAEVnTD-Enb6YL7US6CEuC4jkgRBh-HLDyZAhE2yW4LkBRqNJCK87DeZRr89XAMu4iBfmcdH8yXxvkMcAt5Sp8ro_sUVLc6a19Kx1q1x58zd5VZSNN2jRZumPmX6OZUORsi8ARO8HyYCeAeeOY-KKatIvU8OSN4LTwZvjj5lrHbJ5P8MqBWxCysAMhVxrwE39zki2BjRv84J87d0DWrHr3sN5YXRtglOICvJGTqCEEOqQr7tfz41UE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدمممم ینی؛
مصاحبه شاهکار این مرد وایرال شده؛ نزدیک خونش رو زدن و اومدن باهاش مصاحبه کنن
😂
😂
😂
+ خبرنگار: شما که خونه نبودین.
_ نه ولی کیرم دهن اسرائیل.
+ خبرنگار عع این حرفا چیه آقا
_ خب الان چی بگم؟ بگم ببخشین آقای نیتینیاهو کصکش؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/90823" target="_blank">📅 20:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=clORdQEpa0vE2F01JEUc9W0M-9aYpgPU4jNPNqMQ95sVM0YDXdtp6RoIyqiY6nNAEDr5vF8c-0upGLgGOT9_oyQEBIosQgxoUwlOpp4c1eaR9JMG5_wRs4YoxeXVOpkz6KP1ZEGzMR80y7LlgWCq8HGJOf_Cg9gsC48hPEz3cUKwnVyWJMrjU9tbQib3LHXMbZ7mG2hQgR8TErCOkOzPNoFsVOKkS3u2Q4ctHAAWS5vSJ7tHg_TFQ4FDbqmKLTQntpW-DV1y7M53nvHTU2nAuJtqw_4aU43R5soPMRHHKgxrFDJaad3haKeaBvlBz4C-rOr2Bu6x_kPFtjdG_r7Hdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=clORdQEpa0vE2F01JEUc9W0M-9aYpgPU4jNPNqMQ95sVM0YDXdtp6RoIyqiY6nNAEDr5vF8c-0upGLgGOT9_oyQEBIosQgxoUwlOpp4c1eaR9JMG5_wRs4YoxeXVOpkz6KP1ZEGzMR80y7LlgWCq8HGJOf_Cg9gsC48hPEz3cUKwnVyWJMrjU9tbQib3LHXMbZ7mG2hQgR8TErCOkOzPNoFsVOKkS3u2Q4ctHAAWS5vSJ7tHg_TFQ4FDbqmKLTQntpW-DV1y7M53nvHTU2nAuJtqw_4aU43R5soPMRHHKgxrFDJaad3haKeaBvlBz4C-rOr2Bu6x_kPFtjdG_r7Hdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ گواردیولا برای پپسی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/90822" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90821">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=Q5j3UW0xyxEk8PGwF2Y_2jCdLZ-AbXu8rpr9BatkTXtXymSD8F5qu3AE9hVNm6XBh01rc6Kac8_dne_NGAUFaNpFkpnF4LaPXsRUzz1RNlrMpZWeZqpdU9duS5fVQZkVH3mwjkTeGcNiT7JJ8gKA5jefQHFEfp_It14c18EnLcZT9XFh0nQA5LJMjvDIoIozlrQox1kKhGaAu0DqD5gtSW4612zET1OPJVK0PcHRAFO68xUN6g0TmskiGquJuQKeKk5OCOpKONvuAdkkd5LQn3pTK83V4T6kMX1RJ0b6EVG82ORXGEa-6RBcVcWHck29yCFtv1S3eqqSXiri2L4bhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=Q5j3UW0xyxEk8PGwF2Y_2jCdLZ-AbXu8rpr9BatkTXtXymSD8F5qu3AE9hVNm6XBh01rc6Kac8_dne_NGAUFaNpFkpnF4LaPXsRUzz1RNlrMpZWeZqpdU9duS5fVQZkVH3mwjkTeGcNiT7JJ8gKA5jefQHFEfp_It14c18EnLcZT9XFh0nQA5LJMjvDIoIozlrQox1kKhGaAu0DqD5gtSW4612zET1OPJVK0PcHRAFO68xUN6g0TmskiGquJuQKeKk5OCOpKONvuAdkkd5LQn3pTK83V4T6kMX1RJ0b6EVG82ORXGEa-6RBcVcWHck29yCFtv1S3eqqSXiri2L4bhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف عکاسی با رونالدو توسط بازیکنان زنان پرتغال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/Futball180TV/90821" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90820">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=HMarxRj8nVCBb9VuvR3ovUvoiPaTPyUqDW2V8SJUv-hOhh-E-xD-mLbNqCy4plcUWGcqOcMofgJJoy4PIqPjxoDm_8kQ0knFVsSV8G1dhApDCUxfhJlh42a_D_Mn2YdLqklDjgQoEl90Q-bhCxxtLZklEEJm1v1THbipXmhOQ7AEETJDcxivi19fNWDAcSuQWU7QUtdEIoyIQ5G7ZZowCjvORzjlQFPBzbo8QDeDNY4xELVYvmQ05PsiE-63_-RaUeefuCdr5x0Qje2-9iuvmZH3Qp-hiJvm3hm6R2Zdg-2gcDLuq9vmYUIa34tsQx6xDD1GJBDnUUmBAUuw1C3MeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=HMarxRj8nVCBb9VuvR3ovUvoiPaTPyUqDW2V8SJUv-hOhh-E-xD-mLbNqCy4plcUWGcqOcMofgJJoy4PIqPjxoDm_8kQ0knFVsSV8G1dhApDCUxfhJlh42a_D_Mn2YdLqklDjgQoEl90Q-bhCxxtLZklEEJm1v1THbipXmhOQ7AEETJDcxivi19fNWDAcSuQWU7QUtdEIoyIQ5G7ZZowCjvORzjlQFPBzbo8QDeDNY4xELVYvmQ05PsiE-63_-RaUeefuCdr5x0Qje2-9iuvmZH3Qp-hiJvm3hm6R2Zdg-2gcDLuq9vmYUIa34tsQx6xDD1GJBDnUUmBAUuw1C3MeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
ویدیو منتشر شده عجیب از دولا پهنا شدن بازیکنای تیم قهرمان کره‌شمالی با حضور رهبر این کشور
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/90820" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90819">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNEX VPN</strong></div>
<div class="tg-text">⭕
محدودیتی که لازم بود برداشته بشه برای پایین اومدن قیمت کانفیگ برداشته شد
❗️
گرون نخرید
⭕
طی ساعات آینده قیمت هامون به قیمت های قبل از جنگ برمیگرده
😇
منتظر باشید …
آیدی کانال :
@nexphonevpn
آیدی ربات :
@nexvpnshop_bot</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/90819" target="_blank">📅 19:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90818">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
#فوووووری
؛ باشگاه موناکو فرانسه بدنبال جذب مارک کاسادو هافبک  بارسا؛ احتمالا بارسلونا از فروش این بازیکن رقمی بیش از ۲۰ میلیون یورو درخواست کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/90818" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90817">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/90817" target="_blank">📅 19:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90816">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVCuhY9O6fkLMfaDwo_WI6jSFwjv2OO8KSAFFOyNl5MoPi_0NmF5vYyIGyN08YGXy5RJ9kUnJMKfSJPiOZeWM3bY5tnbxHAW2jv1KY1tySipFQunOC8Bs_xAqjkyLB2o7si_9fdKvOEv4mJEuQmSX_yLe-3C9-2tetyhewR7-syu-fHqM-1opAoga_hYx8CG3Z2pJHC5pt3xucl2RvMyEEZv4Vox5_uG_mqaAfCCNYJ94lOz0hKT_vbDRUoH3evGJR2aYo_sVqBtaF3OiAeiB4kUWVqEZdv8HL78xZASwiUBqO7kNfExSqvga0-L2iUEQRnk6Il-EHlJilVFcbYkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کونده :
«تا سال ۲۰۳۰ قرارداد دارم. در ذهن من ، موضوع تا حد زیادی روشن است. وقتی در اردوی تیم ملی فرانسه هستم ، این مسائل در حاشیه قرار می‌گیرند. فعلاً تمام تمرکزم روی مسابقات است. من در بارسلونا هستم و امیدوارم به حضورم در آنجا ادامه دهم.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/90816" target="_blank">📅 19:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90815">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تهیه کننده برنامه پاورقی: خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/90815" target="_blank">📅 19:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90814">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8B7lb9jq2MMiaePoXTz8M3JXkb3J8IdZPsYnuREdof2w8f4UWPqgLXYkIJUS1FE77X2qlgZZBVVDUiGJWVZ0NTbJ49aW7vDwP1rTt0i4up8s-R3wSeIpSunJW0MMhQL8tVCje1YlfwGcNir2sBtJgGSSRP_QkVuKRyHecD8t5Mfo_JWZlaJEZ5juM6hyVMPROTyjUDmuoNvtL2ccwg1Dc3JD2eBNOcyMIjvRV8OTHdB9h-LDyu7hIZu_Qi0YiX6jeUyvBGj1KjGOVKJRM6MBwO8Zx6Szrgdj_mvFFYQ_j_eCAqOhSzorJf1Fhd_3UJ9vB5Sn-jkxgDGkO1dhKimPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز هیچکس نفهمیده چرا زبون ویتینیا آبیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90814" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90813">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تهیه کننده برنامه پاورقی:
خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90813" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90810">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH7vz_TPnPhWkq3GJXcIc8boXkGekdDgNcZ_pO_fr_-xsTnLrKQUHkxOoUKN3N0UyzG_WNOo_HxF31bPi2k6avRNRuv79ZsGxugZK8wOA8yzo6Yfcl2uiM_-88eZB3aqCjYdE_O9ug_e5uHyfy5AFUdYxMUQJEgRVnG9TP37ZuZe_ytzB33XhP8pVMGDKHPKSJZoWQVtdRpN_8kveEu8yEqG9mtI28qduvIYKqbkJ3IhtB3ALfh0kTrv1HKfG-ceM4B4mT5HIGGPRtI0LPDVDBMmvC7S0GcG20O4nU4wl1q380A6UrO7BAr-9IAoDVkIL6TpSb8YZ_h_3N02B9VvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/Futball180TV/90810" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90809">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgUONS7IMXMtHJSuVERvqj1nd4pbFbiULXCwFiZBw2jv_6xkbDi5UommZ4VLG5l5JXNU4-MmztT9DysFn7DmQy9aZRR8YZs5tLQS3QDKWybhFZx_x24kYEzjw68AMSAMYQrYh_jzGbVnt_OK_t10ThUKutrNAgDVvS5j4KJD4UEj2wTCoWicv3PzZ90oWMlWxnXFcIzwRwl8NoLUETdlVx2aXOHq_iVweALYSs0j4VOyJRS_EATzW4mJnicwLrAWYYtCrRo9vbpUGwNiSArZ1gSWizehsf24g6jEzSafniw2bYoPEFfrK8WrRmmiuRnZ8L8ebWu7CI5dRbaoRmOC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل کمپ ۴۸ تیم حاضر در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/Futball180TV/90809" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90808">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8q3av08lAIflX-OtTW3NjzOC0E6ywN7sb6gw1s08sa-vCusHzmsnJYFzmZHQvqAM5r3tL1H7NaI3s9xS-A06aa8ATTiVEjH2ERux2P_UQ8yMry3HwhyQxCjfABD7Mo-DZrSXI6rUtd6eFLxAAKp9KeDiwf4iS7OlOacP6-yJRH3sRXbuIFGts2bnSdxHAwPS93sB1JG5-glkd9HZ3fAmiF8fGTmumQKqjSYvVRTyf_72akJiCMxilpT6pUwqWVTMTY2ud85NCzhltgv2ABeVzL-bB-W9xzMv2290PDvJv5D3oyoqojBtWtR15oDF4Hx3HpbBbtG8UmSYKiE04cWMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی و ثابت تیم اردشیر تو جام جهانی طبق گفته رسانه ها:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/Futball180TV/90808" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhjByIHmwxOBnpwB7oqF4LGcdrnuW-sHWLYogvnmsV7SIMKU7CkNtmZN8LIoJX-qfsmWpm0ycCkJa3AXlb-xZcGnqtYv37n9QapiLZ9XPl6NZ1ZXd7vtlAYGAgMGoIAqt_w3ehdWgLzAcBVpxmPQA16twLJMfZrAQkvjEuW-6jLHoUtZ6pXZGikUC14mb7bx2ML13eX5XTsYDYZRUwwm6Z8Goq0sPisya7YCEWLvE8BYPfi81RiOJaMAAsoU0mPylc12xRTuKuS8HbZ3yAmVb12k2ryztdggIKlyr04RXNcCvGsk6Wwp-r8sTUvKusQquDRMPOQoLAFsplh_aKkZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/90807" target="_blank">📅 17:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90806">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqVsd_37xQm_cJwMumhhM-Sa5FRhawvyEJWRZuHRKOYV7aWiHx16fyi2KkxnFP5ib2IfNAfDkTwTw32T5EAyISmbFRMR-QUCDDxw3xvprwepBbtDfMHcA-UrQPv8SZEgyFfZmir1n4tkWVA1TiXwQ1RL6bbgwqSEQL6WiWHbxrz3q9cHryz6l3aUfVhbjCM6Du2JMSU_R_MyhP57-BEgKWMETX6Hx-MFsYA38BQYI-9TLXsvj0zn_AWGFcFSSOe0rbunK-FOuCB_D1hoU7np4Ccx3evcnn52AcvFpLem0yPgB0CtV_bKAlhvNbjeG4Repu57Z78ASQFDeu4T1X0cFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 مربی سابق چلسی که تو این جام جهانی هدایت تیمای مختلف رو به عهده دارن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/Futball180TV/90806" target="_blank">📅 17:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90805">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/Futball180TV/90805" target="_blank">📅 17:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90804">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-Nc3dFuOba024LTubrf7fLl9rchKpAqUH_Dwneh54iz00qB43DNGzIjyKQFi1U3gOqRQc64IbrvHujTZC86o4VVudQoGh4n4kALrVOKMFIBZPYMmhAOPo27cIpIRB0qxPnGbMuftOEkdIw2rFzbEAVZ31hWbNYXp1sM4qkpbjp4KnRAsAS5TkaA4lilitJhxFSOUZ6IqS7asEgpqMOLfjaCQDPDY3qCX0erOu9Wpjk7OW9bKcGOBJYCF6QS_xUvTN-ylh-x2IqrMIuCRZGpvaUx11IUIfwqFKOONWBAIlG1N673_cr1doWuai2PreCIgTq40gN0LuPJ0vTlMnPrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدربزرگ هالند مثل سیبیه که از وسط نصفش کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/90804" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90803">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167838926a.mp4?token=IERyofkGDAi3P0CeliPsrUcAZQZG8-YmXpOPgJV5NpOEuG4EgGXXCmrfKQM8gt9uJDqdZfnTxzZKD-a4slvAq1TmHeTYTfiHWxSTcjShDVBfXwM8jdBSqQYKSkdfatI579DLXV2rz7lwdz9rUo1hIFEGwRP7fU_vCFEKQs8MlOZcqagH0TivF3QNID1pMuzqeAyZUvFdvu6wNxIkk4daVjm9_yyCNS4VFV5TauTYlqhZiGiriGejj4ZRVX4_AtfzeuagTiIe39rnJ2bcwuiznVI0HfuXWCUqqvcmvC6Llhf6KQjESYTlkAXBlc64Eqx41Lo6ilfmt_jrhPlkMOvirg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167838926a.mp4?token=IERyofkGDAi3P0CeliPsrUcAZQZG8-YmXpOPgJV5NpOEuG4EgGXXCmrfKQM8gt9uJDqdZfnTxzZKD-a4slvAq1TmHeTYTfiHWxSTcjShDVBfXwM8jdBSqQYKSkdfatI579DLXV2rz7lwdz9rUo1hIFEGwRP7fU_vCFEKQs8MlOZcqagH0TivF3QNID1pMuzqeAyZUvFdvu6wNxIkk4daVjm9_yyCNS4VFV5TauTYlqhZiGiriGejj4ZRVX4_AtfzeuagTiIe39rnJ2bcwuiznVI0HfuXWCUqqvcmvC6Llhf6KQjESYTlkAXBlc64Eqx41Lo6ilfmt_jrhPlkMOvirg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش پسر مارسلو با رفقاش به یاد پدر
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/90803" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90802">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e389c70190.mp4?token=kP1xRsrPqUF6Tc6M35AV-Y4nbISBUHfTqZzyoBrbpt6k4kds7tlhoR2AWFjq-zA9O0GxuK_6yWyxppLktP_ezOrkNE9iYRW5RF4iaUaP9W5KqBoTpy2vATBzpcx-bOXsrhlFiLRYsp0ygKvogvM5aZxLMxSyqir3JQOF8lmWFecU30CMoPTs1kFdVxE26aksHL_XyiBu_wwzIR3ey-ttH6hn8mngOd__1RooUrUzqbbl1MdYTjiX4MKAfH6SmyDV4LUF3oDRH1mui6WtoGH345JXTw_PcOnnm89RhsnehYF5VqitXI4E1eb5mWTztBxComB9JCMKbiD9jAf6TCrYBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e389c70190.mp4?token=kP1xRsrPqUF6Tc6M35AV-Y4nbISBUHfTqZzyoBrbpt6k4kds7tlhoR2AWFjq-zA9O0GxuK_6yWyxppLktP_ezOrkNE9iYRW5RF4iaUaP9W5KqBoTpy2vATBzpcx-bOXsrhlFiLRYsp0ygKvogvM5aZxLMxSyqir3JQOF8lmWFecU30CMoPTs1kFdVxE26aksHL_XyiBu_wwzIR3ey-ttH6hn8mngOd__1RooUrUzqbbl1MdYTjiX4MKAfH6SmyDV4LUF3oDRH1mui6WtoGH345JXTw_PcOnnm89RhsnehYF5VqitXI4E1eb5mWTztBxComB9JCMKbiD9jAf6TCrYBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
کاش برمیگشتیم به این دوران و این بازی و کلی هیجان و خیال آسوده فوتبال دیدن...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/Futball180TV/90802" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90801">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6331bff84f.mp4?token=c-NURNNK_TnFIC5Z48vLKszS6Q6hJ2ITpSmNpHQKwu7dOCgY-6Udcj3nxS4GzwzqA2w7OBv3uoVIKvoWHB2sFmPw1yho1Hb6h3W-0Jt1dQYhnEDj3O34PDmzqaGlF5NYjy7oUDZ8ItB8IXq0JCEQc1bFWGXVvSJcM-mipCD8-ybj3yJCZSA5Bb6G58lQR1wYO2rm3eLJ50MRe5q1LdL9iu1ZYEbdHKDPtJfYc3FmPv239uKA8ZHviv7u9AghOJOWROzvRMt3ja2KThLztzphPcmY-78WNEmTZNSS8OQUoVbMAhjtNPA0BcPfpaM03aUwEl4op6PHqr8fBVazDSu0zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6331bff84f.mp4?token=c-NURNNK_TnFIC5Z48vLKszS6Q6hJ2ITpSmNpHQKwu7dOCgY-6Udcj3nxS4GzwzqA2w7OBv3uoVIKvoWHB2sFmPw1yho1Hb6h3W-0Jt1dQYhnEDj3O34PDmzqaGlF5NYjy7oUDZ8ItB8IXq0JCEQc1bFWGXVvSJcM-mipCD8-ybj3yJCZSA5Bb6G58lQR1wYO2rm3eLJ50MRe5q1LdL9iu1ZYEbdHKDPtJfYc3FmPv239uKA8ZHviv7u9AghOJOWROzvRMt3ja2KThLztzphPcmY-78WNEmTZNSS8OQUoVbMAhjtNPA0BcPfpaM03aUwEl4op6PHqr8fBVazDSu0zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم آسیا موقع دیدن جام‌جهانی:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/90801" target="_blank">📅 16:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90800">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgyyvzh1GaDI8ndcCQcTlLRWJ8Ek9ooUpOESxz0MbZePuv0lPG-thEzZ7WL8PrmfOrqDrTTD9Tl8hpzHkRSUpj6U5PM1dGXFRnTjT7TKirVsTIE8mVNPvIs3RwWqtc6_VRtgN8wIx0yD5vIE5LavVU9Mw1U4xlo_c0oaCFQObHQMMrBdHsW9-R2mcOr9T4Eq7R1s7dKaIqN9PIcF2WCgyDZfTy7aulE3yCnr6PgRsUTGhfyqWVoDAs6vj3HxWZD7UpXU9kQka5NMyKEIl5GJB-qUgrvO7_2Zia31G3yGVJxS9B3Bg8SzxxZyyTEupCURfH9P1cLMvlt5aTSW7s8TQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ایده 48 تیمه کردن جام جهانی واقعا مسخره بود؛ فک کن سه روز اول اینقدر بازی حساسی نداریم که باید 4.30 صبح پاشی آمریکا-پاراگوئه ببینی:)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/Futball180TV/90800" target="_blank">📅 15:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90799">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e4e72992d.mp4?token=EA_OXKSWHL4p1m5TM5DjD3fAibJAIM4e9qiHo3YEPr7cvadMEjTVASpiH-Ddj-KU-M183Le3ApQiKPSmbM28cZzLoVti3URESr5jZ8nuuTwcaFuJc9wMq0JIk5pzB212j-pajFaSt9oMYgSpJiSRkQnw1dsLeW-5eOvbR5Z5LnrlXiofgj9-yQeO4E5q1zreTIKsI-BG8JGJqg30JuszrfOqIfU1il8tCcH3p1MnCS27719m-9QHNYZTky9ehDIdnTr084SakhDz72zAmH6QN9zw7NYlfYWKOBsW98vrN64XMr2xLIzSy_sC2zM7DTVBhVDL7Yypaph-uZ3Cn0CLwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e4e72992d.mp4?token=EA_OXKSWHL4p1m5TM5DjD3fAibJAIM4e9qiHo3YEPr7cvadMEjTVASpiH-Ddj-KU-M183Le3ApQiKPSmbM28cZzLoVti3URESr5jZ8nuuTwcaFuJc9wMq0JIk5pzB212j-pajFaSt9oMYgSpJiSRkQnw1dsLeW-5eOvbR5Z5LnrlXiofgj9-yQeO4E5q1zreTIKsI-BG8JGJqg30JuszrfOqIfU1il8tCcH3p1MnCS27719m-9QHNYZTky9ehDIdnTr084SakhDz72zAmH6QN9zw7NYlfYWKOBsW98vrN64XMr2xLIzSy_sC2zM7DTVBhVDL7Yypaph-uZ3Cn0CLwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروز قربانی: عاشق تتلو ام و آهنگاشو گوش میدم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/Futball180TV/90799" target="_blank">📅 15:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRqXOj3W1gYKxlJXr7BxJrtupdNDZnEtgypWaqq6nMQYfKZiPcXICQIhYKkHIEG1ao2uShopIBRIp5VZW0Pr6YAvO8J_IjWGnlr4kmxEEwnfNNhS_EZQ1F6Ra-aVzKTze3MOKGyMOY_r95HyDlvd2-g3Pkfay7--d7bHtIgOE3xpQj3gSCGROaIZZMa89pUsiFmiLVE3nTCB22vgxT0CKhXtvxoPGDrByak0XWm5rxDHwRSTScURdktNtSyd4WiDjdCpaKmyOeyXVS7pkDAv4waNkpWBU8tCOH0dWnZA6C0WYxjIRYG58dEKBWnpevHcXsaBldTrkv-kcG4cFyqfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: افتخار دیدار با آیت‌الله خامنه‌ای را نداشته‌ام. به نظر می‌رسد که ما با آیت‌الله رابطه خوبی داریم و دوست دارم او را ملاقات کنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/Futball180TV/90798" target="_blank">📅 15:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=cIoMrO7oUw5HLe0dH5EA0Yjn3CA1YbPO6zta6yfox9pXoD2E3dI83EgeQcHS6tEy6Cm934LBo-HQ3ccPT2ajRqa29yDAC-4YwVYuxhz3E2puvKXkU-u6I6QVEYMhsWMVa1isQ6Xbu0S6bDwTwhZOQn09wwhYE8slNC7BnQmL7ItHMwSzSrNu4Ys-K4ZUQ1NmirTcdFPLgMEx-BnKUgG9raN_3uVi3XYb5_mYeuucdBjhwYQvo48mcJ2bIt287Nr1ajTtb664LomonXjLWvSwqI-5l7TAoUiFt3j4SLq9dWFg_-JjR3gEu5O-bk1BAID5NB6Y0EaPwExBnHbi3TWLQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=cIoMrO7oUw5HLe0dH5EA0Yjn3CA1YbPO6zta6yfox9pXoD2E3dI83EgeQcHS6tEy6Cm934LBo-HQ3ccPT2ajRqa29yDAC-4YwVYuxhz3E2puvKXkU-u6I6QVEYMhsWMVa1isQ6Xbu0S6bDwTwhZOQn09wwhYE8slNC7BnQmL7ItHMwSzSrNu4Ys-K4ZUQ1NmirTcdFPLgMEx-BnKUgG9raN_3uVi3XYb5_mYeuucdBjhwYQvo48mcJ2bIt287Nr1ajTtb664LomonXjLWvSwqI-5l7TAoUiFt3j4SLq9dWFg_-JjR3gEu5O-bk1BAID5NB6Y0EaPwExBnHbi3TWLQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردها اینجوری بعد باخت خنده و بعد برد گریه میکنن..
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/90797" target="_blank">📅 15:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7TgapUx_VyFyPk6QUZWZSJ_Z_yuaaUY7Tksegndhpl4WnPzwmSuPljedGYnRU0V_nXFoMpIgYQzvjxIIzWq8MlteP9ibJ9pyJ_GdqQZXTHH9pY95oq-UHMimTE2CLApxfyYB82jfIWS13b62cV1M6uiDZcHHsN38qvmDsY69BOvB3NeUVpSccMpzikHIeMdedBZu5UDEsXobLhL3xO09btfc-fYkdPS_E_OwtExFzXPZs9dNm5ACtK6h6eHyRH_hrUUlaRP-sDdX4MJBIRxgcjZMIF3iSHwAeTUQi8kv0YBd6rPeQnpySN26bOKBSSRX5gMikyxBNo-orz4ZNQsqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🏆
سامورایی‌های شگفتی‌ساز که طی چند سال اخیر حداقل یکبار تیم‌های مطرح دنیا رو شکست دادن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/Futball180TV/90796" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه کاندید ریاست رئال: امشب اعلام خواهم کرد که یک ستاره جهانی درجه یک را جذب کرده‌ایم. من به طور رسمی یک سند قانونی الزام‌آور امضا خواهم کرد که تضمین می‌کند قرارداد با او را نهایی خواهم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/Futball180TV/90795" target="_blank">📅 14:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=lJtME-WJOZmoNBdb_I-165Sxi1P9zKAEuHNTvnJ-675WX3EvwFqJXrxcZ72xDuUTG2ekrn1iMVZSryfImsTgTq_VdBEcF2FxMUNTjNDXOAkFp4K9p-ExfAsQ6xPrAZgIOF2ZXGIBTyCBr-p__920szK7DKsAc6NJiulQn6CSArfbOWNXVTj-1Dfl37Au9JKd93BBbQLWoGZHimyKPrs5Ee25zCfjO9l7jc58zH7rTBcPYMIpCHajTMKFc0LETyBQTTSNKFHQjDjQFE0E1fZc3Z9dSvbG5XO16zckqW8FRJ13QJ5HF3R98TRQUj5Hq7b4avGrfvHUrpMrL1EaVQKsqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=lJtME-WJOZmoNBdb_I-165Sxi1P9zKAEuHNTvnJ-675WX3EvwFqJXrxcZ72xDuUTG2ekrn1iMVZSryfImsTgTq_VdBEcF2FxMUNTjNDXOAkFp4K9p-ExfAsQ6xPrAZgIOF2ZXGIBTyCBr-p__920szK7DKsAc6NJiulQn6CSArfbOWNXVTj-1Dfl37Au9JKd93BBbQLWoGZHimyKPrs5Ee25zCfjO9l7jc58zH7rTBcPYMIpCHajTMKFc0LETyBQTTSNKFHQjDjQFE0E1fZc3Z9dSvbG5XO16zckqW8FRJ13QJ5HF3R98TRQUj5Hq7b4avGrfvHUrpMrL1EaVQKsqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی که از هم‌باشگاهی هم شانس نیاوردی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/Futball180TV/90794" target="_blank">📅 14:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90793">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476676c77a.mp4?token=YjK-PJdUzWS5hA5KOUlAJO02V3Os2UcCuOV7IaOygYXq56WlPbRNnIuSSZQVpadgK6dxk6YNOG33Lvti3sQHN4ywt-aRCKi6PD2NdmpK_AS_RqahfoPDeQk_U3VVsurNwhbvd3XMZZQe9-HX2Zwmn-PvFzbk_RijFph2DsBxbGuLwMeSRyeGw8ymmxpMunPsf-Q_KYRuQS8MLq5qGo8Ary4LMH0AyFdE89Zf6FqreUOeWvVcqMaByTVNapr4cp3O7qKINymq6tjcITSB44sUS8z7-viBhUD0B7v8-dLf-nJ9yNBoS9L5bIODYr9KeXP3jyTSeeKSVo_nr-U5oijOVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476676c77a.mp4?token=YjK-PJdUzWS5hA5KOUlAJO02V3Os2UcCuOV7IaOygYXq56WlPbRNnIuSSZQVpadgK6dxk6YNOG33Lvti3sQHN4ywt-aRCKi6PD2NdmpK_AS_RqahfoPDeQk_U3VVsurNwhbvd3XMZZQe9-HX2Zwmn-PvFzbk_RijFph2DsBxbGuLwMeSRyeGw8ymmxpMunPsf-Q_KYRuQS8MLq5qGo8Ary4LMH0AyFdE89Zf6FqreUOeWvVcqMaByTVNapr4cp3O7qKINymq6tjcITSB44sUS8z7-viBhUD0B7v8-dLf-nJ9yNBoS9L5bIODYr9KeXP3jyTSeeKSVo_nr-U5oijOVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
🔥
Colombia
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/90793" target="_blank">📅 14:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90792">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: احتمال داره بزودی با آیت‌الله دیدار و ملاقات داشته باشم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90792" target="_blank">📅 14:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90791">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9285a340b.mp4?token=Ve6Sa_x9WaomcgH5R493ZNLBtcYJrAZTf-G1gfDzFcRbNQROl_dSSUR4K7jwSbmqBXLgr6qGUEqzokVEBBX-ewuY2xEAX2wtGp0ImUy-57HVYt8EZ9e6FC-qFZ5UGOAV3dWzuhIG6sxZ1iYJ0oS8HZClMXcOQ6hLb00kL2Uzd15-rYqxkvAahIYLsEoEHOqN5tZo3_jUCOIhFeMbaAUHnjJQF19xn0JzN0-OOI0nGI60BestBiA9KzcTuy41TtLTP8-Jw3LGdPcD967UbVpNgsrw1JEcLXQxAF1isDzAqWufEltFnMPv3cOA6oEtwpCAV2JQ9__-sTg6aBPaw8Ti8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9285a340b.mp4?token=Ve6Sa_x9WaomcgH5R493ZNLBtcYJrAZTf-G1gfDzFcRbNQROl_dSSUR4K7jwSbmqBXLgr6qGUEqzokVEBBX-ewuY2xEAX2wtGp0ImUy-57HVYt8EZ9e6FC-qFZ5UGOAV3dWzuhIG6sxZ1iYJ0oS8HZClMXcOQ6hLb00kL2Uzd15-rYqxkvAahIYLsEoEHOqN5tZo3_jUCOIhFeMbaAUHnjJQF19xn0JzN0-OOI0nGI60BestBiA9KzcTuy41TtLTP8-Jw3LGdPcD967UbVpNgsrw1JEcLXQxAF1isDzAqWufEltFnMPv3cOA6oEtwpCAV2JQ9__-sTg6aBPaw8Ti8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات تابستونی دوستان در بلاد کفر
🚬
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90791" target="_blank">📅 13:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90790">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: احتمال داره بزودی با آیت‌الله دیدار و ملاقات داشته باشم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90790" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90789">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw0-W0gFB517NmzdvWH6BZ7aQucY3wd0al4HApoc1o8fqkDQCS7Aui8Voa5DvEsLFlxQLmeKbNlSmlWqBKn4efrRKTo2dcgZCNM-FIuiwZfTLHGt9eFTCvhr2gFqMBnt_QJjpyD8MlMQju0V54QNJTU7zqrx9Nkheu047jHjj1JDFdpgb59Q889lrW9359T9QivCxjimHBZTFSTJ6ZrTBWsPThoh53Qf4yYHqNOVXDaDMtX83n2zhcG8fXrkCpP3_tTUxKnWUMPG4KZ14L7dozZiMPUQk0oWZikLTDAhP4bc_rDLRPqtjkloq9KHYRFPyxuX-HC10-uv2WrCowt6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ یونایتد، psg، آرسنال و لیورپول بدنبال جذب ماتئوس فرناندز ستاره وستهام. تیم لندنی خواستار دریافت ۸۰ میلیون یورو برای فروش این بازیکن شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90789" target="_blank">📅 13:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90788">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJR3U-nZDqyzNTtgUoTAcX8CHV1wSZqRdnq9WtPqy-XsmG5en4GBIP4n1AgqQiD2admcsOK9sxc9gVt8EZ3rZCZz8WA-_g8WQG3_HGDZh5FCRX3aj_BE2YQ3glSrZ1pL1wmUt17iLUru8kZUy9OkaU_I_E_RNfNty2Wb9L5DEl6gMapTUvGpqgUsu3VEeAIosutZXITVUCL-Srba5mQiaa4qmlOGQVmA6ZNvMok1StcREv3wegwIsezVJwR6pBPw__PTzyK_UcB2qejFbf7NB3AcGuodJR4qZvA2UnHa8igikAsfPx5k658kX_z5p4XGYhORDnqq97s8UZYIKFfnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
منچستر سیتی در صدر تیم‌های با بیشترین تعداد بازیکن در جام جهانی
2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90788" target="_blank">📅 13:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90787">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXYHH09m69B0U4eNDf6zFwxTuRauI3gcktBytaP9yuOIm06JPBCokTNZRWewwkInS2N3ZHrxWHUt_TPEMQXff6YlfcDI5wtkjpvvdytD0hEX-2bncsrBv5k6-UBUd4MjsHbJqO3KUTuwTr5zECmeX2ysoVWgQZ7OJJYX4WDmG3ozO0yAoO7YxjK46Xfdxw8qBJh9UhKm0JuQlP6aXwguphUrVsHRJknduTEkxGkazqIzwDXVRKQCyF789e4n9CDq_-jbW3gdUNULZCCQFka4IEfZeM0EDuItG_jcuyEUgbCymGtw9Q9GjqD2TV_dqJ6-aEcF3WaVeUCS2aSyU9jfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام جهانی واقعا برامون غم انگیزه..
پایان نسلی پر از اسطوره و پر از خاطره
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90787" target="_blank">📅 13:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90786">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری؛ ژوزه مورینیو خواستار عقد قرارداد با گواردیول شده‌است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/90786" target="_blank">📅 13:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90785">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCxTc2NgsQxiHipLFJSi4wC4AAXXNYpRYhLft84TnFWTUyv4D1Y5kuSelh8z94b-KGVerWAAyaSNclV02mm5AiHor4kx4MkVQLpTzFS2Tp_QC3LecSJQ8NTpYgIR7bous7ivAjAO5Wic_Xoo-D8Pg8MOjeDbRxQ5gaWLD3gEGG_oRZ3T5hufbdRaiCnuLG2WyOY9ROPpI-g7GLN5HcZcUFj7oWsI4Ym1aWKiDGG5a7RIG0220HH7gb5hFECqoexuEzI0gQyMZM1jfY9SjSl-Kqz0ohyIGN5NPG8BWARMClUNbsqdUj75RLdOkxP2SEShQMALgz9lX5atGAXzYyCVUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری
؛ ژوزه مورینیو خواستار عقد قرارداد با گواردیول شده‌است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90785" target="_blank">📅 13:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90784">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJKfRcEmP7pXbpDFOsTZ3ykXzkGRTyemWM_mdcm7X7l7wKDtrAjo0ERMYPtte5ln77dHJOz86miNkrtH1bhAJ9F0l4B2F8ScHOaeZF1BG2dAUqCSUjGknXPoT3ygH3a-mmUXj_kEq2bHHVtqDba9yJGpCp5YQsd1p1txlxKmtajjymWZ1n3IGL1ea0GImKGhsg7lyoxRfCdmvSJ4A7PmZbzTjRFLgNMM0cv1bvY_oA9e1wvczk_M75l1UFNO0Wk9R1cGoLYFn6_pvdLcDvppjfVNXCaPGuzSHc8yaKj85VvJIus8vP2bLnveP2wloM--UGJuQ8AbDBq0oBwwLCLv7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستام وقتی میخوان تولدمو تبریک بگن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/90784" target="_blank">📅 12:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90783">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8caed85c.mp4?token=N4K6vOba3Ytfn_zf-Ow5hiZUZCxnOU5CNLypSM5HFOmpwKaBKcQ0b5KJHCihwzZ9pbAKB0VNS5UroUqtVDGkH4m8DqnyQqWhAMlqNF4n5gPZQKhVdObacysiEE_KC8eIuxrHNaCdAh7IJFgP4VjV_0-vJaVS90WdgiRLB-kSKtmz1gCM88T3FOGyTzzMQG5GBzGfI7iIZOQQKKrTezqeX4DHYV5wLSfZu3pndY8bExmvkVLFvgs2PKyi5DL_bLbuxqhS7mkIzERYMNsz6OsXhKKkc1T9mZOeJUKQk_qk31m5hJHJVCsHq1Y86MRconL02SJofrhJxmAoFqn7nkCqOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8caed85c.mp4?token=N4K6vOba3Ytfn_zf-Ow5hiZUZCxnOU5CNLypSM5HFOmpwKaBKcQ0b5KJHCihwzZ9pbAKB0VNS5UroUqtVDGkH4m8DqnyQqWhAMlqNF4n5gPZQKhVdObacysiEE_KC8eIuxrHNaCdAh7IJFgP4VjV_0-vJaVS90WdgiRLB-kSKtmz1gCM88T3FOGyTzzMQG5GBzGfI7iIZOQQKKrTezqeX4DHYV5wLSfZu3pndY8bExmvkVLFvgs2PKyi5DL_bLbuxqhS7mkIzERYMNsz6OsXhKKkc1T9mZOeJUKQk_qk31m5hJHJVCsHq1Y86MRconL02SJofrhJxmAoFqn7nkCqOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇫🇷
تنها تیم‌ملی که تیم‌ملی نیست:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/90783" target="_blank">📅 12:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90782">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQv9fX946hV1niYRCW9eAXYRfUEAHEZoAeaGpAZz0kX4ec3cigPdw4zQzoM3SyujqyVbyOyntYTfvyzYOM3ORkaod3b1PsOhc7H6Z0sfbWVcDkPWRSTm5HUnzX8-L6_8D4AofvilRJ5k7nh4kDRUXJdUFa-XcdottoxXKhYPbJcRWJH_4NQYcfoCIcZzXIE7TT_5mloQK9X_3Ftafn35JuVFE7ljtaY6H6_sRbLcxkxPs-Q-Qcy0Ynm1YF3-TjwUQedARIHS_y4wadLCmXFnRpukXix-2qjyNpkzw6gNHGZgoSs0HhXxMYtnQtiusSunh_qSbwzE6viGKCHoRMaDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پیراهن اول رئال مادرید برای فصل 27_2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/90782" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90781">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c9a85cfef.mp4?token=Zh6UdityDVCyyTBYzc5yv0IyBtnXHD4_HN1FenXrsVC5c4cvVLXSsPbFksCFUpBK0vUqx6Cjsx728TXz66jETdkmfkTauiROn0JAMVGjU7HORLfb6hbVTOixwnVqGuKMS8JhLWsdIv2x-s3ThdISyDnLU8TCG0kl9JauUIWYvz1yXiZt_NsAH6nUk3GXIx7PubVsSEinkzhsdKDLyaTVK5ka_hK80AKSmUjH8iE6dYanX91DAqtGCyGdlGUTYqubqs-ltYHHLNxAPm6GX8Kl33LMUSM6_bGl7q8jUen8fwVqUNoPLF-g1YVORzOOdzOu3aMpR8jLolcMFBYl9i7rwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c9a85cfef.mp4?token=Zh6UdityDVCyyTBYzc5yv0IyBtnXHD4_HN1FenXrsVC5c4cvVLXSsPbFksCFUpBK0vUqx6Cjsx728TXz66jETdkmfkTauiROn0JAMVGjU7HORLfb6hbVTOixwnVqGuKMS8JhLWsdIv2x-s3ThdISyDnLU8TCG0kl9JauUIWYvz1yXiZt_NsAH6nUk3GXIx7PubVsSEinkzhsdKDLyaTVK5ka_hK80AKSmUjH8iE6dYanX91DAqtGCyGdlGUTYqubqs-ltYHHLNxAPm6GX8Kl33LMUSM6_bGl7q8jUen8fwVqUNoPLF-g1YVORzOOdzOu3aMpR8jLolcMFBYl9i7rwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇹🇳
این دختره که می‌بینید از بیکاری زده به سرش و رو قهرمانی ترکیه با شانس یک درصد، تو جام‌جهانی بیش از ۵ هزار دلار شرط بسته
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/Futball180TV/90781" target="_blank">📅 12:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90780">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0dddef5c.mp4?token=OTXcSxrbF1jTpCnU2pJpM1S2U2Kn1ASttmv_0XFWmTuYecEqlX8NCPuhaj-X69n2InfkOeadAQRrPIde6bQ-uHyjrEqjgH93pSO1wB67h44aBuFnZleWohtz4TFy1RVm6z5GFjFhDddW8ZqTzwWEmy5He5t-1As424Z9mJkANtbx_gzJYUWpXG_tMfgA9Q5Wj322vz1iHHKn0dqNxGXrRdi_ZFYPVkKCg5rGQqHCCgXi-PVg3e1ImesCQSZtF4y15aWQGHbGx4tRxsnbdDJ-36r0N9CM7wrSYINWOE6z6sUvdRPtcdFnrG9wp1FuQyYWFi1QpitIeW7Am4pwXCG5Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0dddef5c.mp4?token=OTXcSxrbF1jTpCnU2pJpM1S2U2Kn1ASttmv_0XFWmTuYecEqlX8NCPuhaj-X69n2InfkOeadAQRrPIde6bQ-uHyjrEqjgH93pSO1wB67h44aBuFnZleWohtz4TFy1RVm6z5GFjFhDddW8ZqTzwWEmy5He5t-1As424Z9mJkANtbx_gzJYUWpXG_tMfgA9Q5Wj322vz1iHHKn0dqNxGXrRdi_ZFYPVkKCg5rGQqHCCgXi-PVg3e1ImesCQSZtF4y15aWQGHbGx4tRxsnbdDJ-36r0N9CM7wrSYINWOE6z6sUvdRPtcdFnrG9wp1FuQyYWFi1QpitIeW7Am4pwXCG5Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بسوزه پدر هوش‌مصنوعی که مردمو از راه به در کرده
😊
🎧
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/90780" target="_blank">📅 11:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90779">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1b77wF4xLFLxk5RYjV4OoJxSIAo6JTaHib7jf_3hZLcvXFAuh3fQf259CB2G6r0O6YxH5UbBTmzlKqMVfUipgQJ_0a2Dmhlnu_2QkCnvM9gMSQTU1efQV2HDSv4kamZ2fvZycM8UaWWNCzxp-Reg_z60P8qcEnYzi-VWRtHTpPNknjcE0HoJWo5DBtr1FqFT08DCpRpOau6JLyrs4MkKZcl7SPdbhSshiVLSr-MKTyZ94WPgcJy2JTPUvHqSL1GUPnu_ijeOrlnJkgCNErEbvsje6Cmsbq53RtNoBL_PHDdm1GP2UMUm9DhTcx82TWA5o7tIG5dm_oIw48dD1LlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
توپ‌های مختلف ادوار جام‌جهانی؛ پیشرفت تکنولوژی قشنگ حس میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/90779" target="_blank">📅 11:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90778">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d071cdfe94.mp4?token=Jq9eOuA8sqmZa1AkLjQaAdlu96T5T86ir2WOr7QEppTJc0DxNNXIkF6vz49ELLgmggXpyyH1isSQkax1C8OBw-5MGYBdoFXqx6uGQ_8Eb-hW1J_R75jWkDGujr6BVZoHm_A731i1TwMf-lVs0ipgdAScesTtS5Ggbd9e05T3SXH22HbWe24vBMu_CzLOYhAvdaKGkQGmm1jQIXsizCHCMJ0wDgqs5xSj32kd6_RVailXbNMBdTQNcxJnYod07aIpNXPoMu1cR28qZ5nTPCM0X97J_p0CimU_EGq00m7jKbIQzyKhOIVJyDK9aYUR0R70TkrZEEDkhOjWY36qNP8aODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d071cdfe94.mp4?token=Jq9eOuA8sqmZa1AkLjQaAdlu96T5T86ir2WOr7QEppTJc0DxNNXIkF6vz49ELLgmggXpyyH1isSQkax1C8OBw-5MGYBdoFXqx6uGQ_8Eb-hW1J_R75jWkDGujr6BVZoHm_A731i1TwMf-lVs0ipgdAScesTtS5Ggbd9e05T3SXH22HbWe24vBMu_CzLOYhAvdaKGkQGmm1jQIXsizCHCMJ0wDgqs5xSj32kd6_RVailXbNMBdTQNcxJnYod07aIpNXPoMu1cR28qZ5nTPCM0X97J_p0CimU_EGq00m7jKbIQzyKhOIVJyDK9aYUR0R70TkrZEEDkhOjWY36qNP8aODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
▶️
تکنولوژی فوق‌پیشرفته توپ مسابقات WC که دیدنش خالی از لطف نیست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/90778" target="_blank">📅 11:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90777">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omTSh1xX5eiYTYMsJQET0THh2CD_uny7BaFTqPuQUPjg4ouAXtO1ylwdMLRjz2t7GvIuyv1rWeyfJ_do8O-SidIyqiIvcegrwPlSL_BpJTYE8I60fLhdJXb-rG6rfAGaMsIFjRQdPru9vi3FHjUc_bS8kQNI-MzrcSI_24BrzyYoMc0Ow5EbkB5qoH3FiRo5oiSDaw6QFmzOWjNzK-hkOeCkqVB7FdGOjyzEtDCUDxPB9CA9G_n0LyifJhQs6jCNsjWggSa9gaX_JJG7NRCpGQNwIxthBz6ULuwY5P_5E-m48cEq09ICAq9N_7HmpgRBW8q169WiuTGMfLOmRm2o9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اطلاعاتی مختصر درباره ورزشگاه‌های WC
😃
نیویورک/نیوجرسی (MetLife Stadium) – بزرگ‌ترین ورزشگاه آمریکایی میزبان و محل برگزاری فینال جام جهانی ۲۰۲۶.
😀
مکزیکو سیتی (Estadio Azteca) – ورزشگاهی تاریخی که فینال‌های ۱۹۷۰ و ۱۹۸۶ را میزبانی کرده و میزبان بازی افتتاحیه خواهد بود.
😆
دالاس (AT&T Stadium) – یکی از بزرگ‌ترین ورزشگاه‌های مسابقات با سقف بازشو و صفحه نمایش عظیم.
😀
لس آنجلس (SoFi Stadium) – جدیدترین ورزشگاه جام جهانی و یکی از پیشرفته‌ترین ورزشگاه‌های جهان.
😄
سان فرانسیسکو (Levi's Stadium) – ورزشگاهی مدرن در سانتا کلارا که میزبان چندین بازی مهم است.
😃
هیوستون (NRG Stadium) – ورزشگاهی کاملاً سرپوشیده و یکی از برجسته‌ترین ورزشگاه‌های تگزاس.
😁
کانزاس سیتی (Arrowhead Stadium) – مشهور به جو پرشور هواداران و رکوردهای تشویق قوی.
😄
آتلانتا (Mercedes-Benz Stadium) – با طراحی منحصر به فرد و سقف متحرک، میزبان نیمه نهایی خواهد بود.
😃
فیلادلفیا (Lincoln Financial Field) – ورزشگاهی مدرن با جو پرشور و موقعیت برجسته
😏
😃
سیاتل (Lumen Field) – یکی از بهترین ورزشگاه‌های آمریکا از نظر حضور تماشاگران و چشم‌انداز شهر.
💥
ورزشگاه‌های شماره ۱۱ تا ۱۶ عبارتند از: میامی، بوستون، مونتری، ونکوور، گوادالاخارا و تورنتو که همه میزبان بازی‌های مرحله گروهی و حذفی در جام جهانی ۲۰۲۶ خواهند بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/90777" target="_blank">📅 10:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90776">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMjiGIagjBav3j54BznIQxGQ4FdCfMJye7TZ9Ebg2tqLyn8aZLPiIuJNsDQXZVg9Z2mp7pzSnWMTh7eBxqPlhmfP3fRRgHobjZMoBJGloDnSwOz7DwZ-mYr7RmPwY0mY8Q5oz0QlRYoOWJvLukEkyN37Bb3_dG5hqCvd37mJbs8yB3NqmPVDZCS4IcPuTYbNO0WCl6Ie3j0qM-JRTqF5Wz7H0BcNWzqrXV0xRoqaMkEUcUFlsD5hc8-lAUhVyxXpE8aPjdFkbA6Tw0v2i4XgRT5CzEnR1WhPY_bNS7kn1QsB0kygVPh5ePpaO8B8HVfzT8BIaV3tUooi3YdYAHgDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرز : فردا از اولین خرید رونمایی می‌کنم و همینطور این هفته از مربی جدید رونمایی میکنم، این تابستون حداقل ۵ خرید داریم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/90776" target="_blank">📅 10:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90775">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f607323bfa.mp4?token=bvbAU5BpEqzytHSOy5NYEr4eRnyt1brUKF1MbLqDA17RVoXHYlHRyGSTC2lIERSpYU2AW0l31sFJNkWVQRFxTZzh0BCl5f2VCHLB8bNDt_l8kyCJeTsa79XtJ8eo_5LjoWfg4u3eI5R7RKYXuOPrpXog4HhPJHjg6eynqoobMaKqEpQ8kX2Flv7VOZyyyA_d1ca6APbnjpK7n3dOBUPoFiEbQ8aF_K-BVNg-rz3omLwxTGBz1T9sSR4epVAzNjcJsxgWz0qoP10beDKfZaQYm-WkF1iK7IAn87mQ7AH8sloqI0_jY0H50TJhjiXmdKNofJuaaOvTuT_jgW4tzJPBxQrGT_Rv4KlTv7xe-Qn8nPp1jvv02O5xDo4OJLXFVFMLa7OJ3StDCXbAghV3zZx9Vl7eZQv__66wWZxLumixOQYxG6DL8vi_149fgD9jfrVIPeFNrKE4Bzz2Hov7aKi3GwAvQ0JuOeQRZ-o3eY9eaQPHUl1GAt5CgwmAewoy44I0JLd6W7YDQzS9S3QlBt778THYOqO29pCxBplIq82bAUZGv71bEGhrjAhhLsWrDO6Eh9jh87b43uAbVFkhy1vDEEIWuM6tvWwoKTt8A2Qwz1lqn76EN6aG7r1U50QLAqQ3I7g2lCr9MAeRqXCgLMkas14kQgcF6LDkX5DieGBPMdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f607323bfa.mp4?token=bvbAU5BpEqzytHSOy5NYEr4eRnyt1brUKF1MbLqDA17RVoXHYlHRyGSTC2lIERSpYU2AW0l31sFJNkWVQRFxTZzh0BCl5f2VCHLB8bNDt_l8kyCJeTsa79XtJ8eo_5LjoWfg4u3eI5R7RKYXuOPrpXog4HhPJHjg6eynqoobMaKqEpQ8kX2Flv7VOZyyyA_d1ca6APbnjpK7n3dOBUPoFiEbQ8aF_K-BVNg-rz3omLwxTGBz1T9sSR4epVAzNjcJsxgWz0qoP10beDKfZaQYm-WkF1iK7IAn87mQ7AH8sloqI0_jY0H50TJhjiXmdKNofJuaaOvTuT_jgW4tzJPBxQrGT_Rv4KlTv7xe-Qn8nPp1jvv02O5xDo4OJLXFVFMLa7OJ3StDCXbAghV3zZx9Vl7eZQv__66wWZxLumixOQYxG6DL8vi_149fgD9jfrVIPeFNrKE4Bzz2Hov7aKi3GwAvQ0JuOeQRZ-o3eY9eaQPHUl1GAt5CgwmAewoy44I0JLd6W7YDQzS9S3QlBt778THYOqO29pCxBplIq82bAUZGv71bEGhrjAhhLsWrDO6Eh9jh87b43uAbVFkhy1vDEEIWuM6tvWwoKTt8A2Qwz1lqn76EN6aG7r1U50QLAqQ3I7g2lCr9MAeRqXCgLMkas14kQgcF6LDkX5DieGBPMdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
مکزیک، یکی از میزبانان جام‌جهانی هم حسابی با این طرفداراش خاطرخواه داره
😂
😊
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90775" target="_blank">📅 10:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90774">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c4dc141e.mp4?token=aLonVO0KnS7__4Ish_sVEn5N2i5HeiIeemfhWy4QyLDG3h4lfK6MytChr1aPK_7wnUQDcJO9_EpHIO2eq3l0JIlzk2QHbWBvVQzJWjFT_agFmKLYwK8bM84wZJbG-0hQwJxFDUHi8I_HANhT8onC3XIs9M1lgtx0_zIyaNGSWpLp3s0WfwjPXFZHx8sW_swx5sytMe-3ugwDg6eosWUCqydbzWtAqt6YztfrEDsbcBVprDI3AZOUFgIj9dIynibP3SGFcsZ6iguJusgICLP2dEe8aGupziuKHBlHwmjG6FlvYgeSXTD779LAShGPTrgHApoOY21ADJ0MsvlrOtrUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c4dc141e.mp4?token=aLonVO0KnS7__4Ish_sVEn5N2i5HeiIeemfhWy4QyLDG3h4lfK6MytChr1aPK_7wnUQDcJO9_EpHIO2eq3l0JIlzk2QHbWBvVQzJWjFT_agFmKLYwK8bM84wZJbG-0hQwJxFDUHi8I_HANhT8onC3XIs9M1lgtx0_zIyaNGSWpLp3s0WfwjPXFZHx8sW_swx5sytMe-3ugwDg6eosWUCqydbzWtAqt6YztfrEDsbcBVprDI3AZOUFgIj9dIynibP3SGFcsZ6iguJusgICLP2dEe8aGupziuKHBlHwmjG6FlvYgeSXTD779LAShGPTrgHApoOY21ADJ0MsvlrOtrUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بهترین‌گل‌های جام‌جهانی قبلی رو ببینیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90774" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90773">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ae696fa.mp4?token=GY8LzdgpUqK-zV4S9CyN4emFzprhH4PiWujEc5JfjH0PbJdLS5BN_X0oxnWPXUnnBRO699USnlP4ddxAd-RxI5BXvYzkjyRUu7ntC2WdPLWeJbkALQG52wf5LnI2tXJ9mDSdbDI9euXo-WwCbk71b_1pZplVi6PnPcveiNX0Hb7jZcYos9Zy05LaRH-bpKvT1bZ_rfSlqsEH-TgSatTclnoViXMRGXxwExNitdT8Ig31cQAfNY9GuO0IpMRDO5cRCu6pk0LzYoKjgJv-51OWtWpT3T9551YiNGPFaDjNioHNbfk6LHZZGsTjd8w_RC7p89C7uSssCzzxwjNQCEjyJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ae696fa.mp4?token=GY8LzdgpUqK-zV4S9CyN4emFzprhH4PiWujEc5JfjH0PbJdLS5BN_X0oxnWPXUnnBRO699USnlP4ddxAd-RxI5BXvYzkjyRUu7ntC2WdPLWeJbkALQG52wf5LnI2tXJ9mDSdbDI9euXo-WwCbk71b_1pZplVi6PnPcveiNX0Hb7jZcYos9Zy05LaRH-bpKvT1bZ_rfSlqsEH-TgSatTclnoViXMRGXxwExNitdT8Ig31cQAfNY9GuO0IpMRDO5cRCu6pk0LzYoKjgJv-51OWtWpT3T9551YiNGPFaDjNioHNbfk6LHZZGsTjd8w_RC7p89C7uSssCzzxwjNQCEjyJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پنج سیو برتر فصل پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/90773" target="_blank">📅 09:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90772">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jmhwm7FrCiUqiD2iLByn7Dln0FO-fKM_Gj_B1jbxyIORV6wPH0_8K8xKwb18jxu2tGwuQf-XylMigyqoOvIsuiG6rln7CR_iEYc-gJx9dLw-Of-vdnAH03zq2uis_LTrnNEMPoREkxlPq4P3pALsYtIvYXLjN9b1XZE93xLJCkTCpYHNxHN6RhO9rVKS4bbBdvQlBgRx3BQE5dJHhQsqwkGkND61P5h73Pa3rejuNxUP12lVJs7WO0NHxV5MrIhraLj4uGR_KFuAOBCg42A-rOqqXbqjtLk5is1C4v4Rl76KGvr-f8Oa5HpZXJbXS2yGyyyIqPmnsTOT9S3fyMfPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🏆
۱۷ روز هیجان‌انگیز و متوالی که هرشب تا صبح فوتبال در پیش داریم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90772" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90771">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLwcfl-bl3xAbkolsPYoGcMRf4JHegS9zabFdk9hEaoeKZumbC5XxEduXO4vNuNOyq2BCY_x9-H905CL7_abIgPgXG7idFsrNFVDqFovkinlOKT6yFIGmJTr46sN5AqvJajNJuMGue0tL-MEHIRaqcVBC03969y0WLLiUAqc9540c4Tk0nWIQopsKJSC6OhTjwJgZR-irWDMY_NcPZc6gPHqM32C9O79Zv-nEaX5_WgEa4uWuypy7cdWnyr6J_rTVKoH8JxUzdZJSfiDJOvZq3JpYsSPklmxcOy4ic5shuGAfQGdEydBKu5mcHaDYtdt3szTiPcWhUZ8Te3Pu9rLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر بدنبال جذب دنی کارواخال برای جانشینی دامفریز
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90771" target="_blank">📅 09:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90770">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ولش تهش هرچی شد، جام‌جهانی رو با اینهمه دلبرررررر از دست ندیددددددد
😍
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90770" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90769">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b603dc908.mp4?token=k0NvxG2ia7feD-Mi4l7TuvxWomkcJzvcfsmU_B7CESeLpJo14vRmMe7ONnPU5IdQqiE__zSvT-eQcQ7-C4ecdMXTLORtV4eZG6tThTWHY6cAeq5ClhbANN4ZwLYfH2YjJpwOYjvHArLydSpG5B4-1xdW_UW8KljQtGRuu-aVpRZbGqbZrjhrWPhne_-eeusUrMZzpROJOwmt-0YQP60qnMDGePs0I_hdXQ9SfX87AUCZELCNJXCa67yuwAYmeU5GVulfEicyKSWhn-ouWbW2pgLHEHYH_TevldGGhzliLOrfWFjYC001TEECtlxWarA_CoSVXoQhi5PodiTkFSiqTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b603dc908.mp4?token=k0NvxG2ia7feD-Mi4l7TuvxWomkcJzvcfsmU_B7CESeLpJo14vRmMe7ONnPU5IdQqiE__zSvT-eQcQ7-C4ecdMXTLORtV4eZG6tThTWHY6cAeq5ClhbANN4ZwLYfH2YjJpwOYjvHArLydSpG5B4-1xdW_UW8KljQtGRuu-aVpRZbGqbZrjhrWPhne_-eeusUrMZzpROJOwmt-0YQP60qnMDGePs0I_hdXQ9SfX87AUCZELCNJXCa67yuwAYmeU5GVulfEicyKSWhn-ouWbW2pgLHEHYH_TevldGGhzliLOrfWFjYC001TEECtlxWarA_CoSVXoQhi5PodiTkFSiqTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولش تهش هرچی شد، جام‌جهانی رو با اینهمه دلبرررررر از دست ندیددددددد
😍
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90769" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90768">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=LnC4gbDU20YtA9DuSacck-vDDbXwBwjgAbajPVaB0ZcpD4blemV-8XiKoZ7dap5se1empPZOJXPe4S16yoJhhQ4ePHUocOwOikTLF38BNu1PgzQ--e2iuMJfo0U_sl3Do462J0RTJvOsZ2Qxew_r4-B-hLbtORA6vYyeDW5IYHAyIbyHKTtQRCKpGZ8B9H54nUp0ZEupHNoA3L0z_Ux_7h39ks3jWCECbgChe9JAWYidLpILlpxGsVsuF-YZ0AFGkUg31MfmC-xsAxYI51caIqDJ3eyZ6_GRv2uYoYd38oYgrN9Nui4zh01a22_sdqww4W0FXd-jpr_mxtFfl2t4bkOoF_XK1Jmm1hkKAKgSEzrsUX53YBXQ_NJlo_iN0pxFa1Yx5Xv8PVrRhWg2wN-GeuTR7Y06p8nTfhi0MZaRqbz75DA7bP9GaZGm2TQPTswc3_EUqAcJ6hsXBd5n8nhFepjTwIlJFziQbXohx-b4D-9n6b7Ws8UQTZhJhvcniB-4fOnrTcw8quORqTLtyzsfS81LwLYLQgXbati4t-zP3S8Bu0leSVVAOH_S8lSOXoaKhdWW2KHmgY7XMiwCBe2mJf1P3vgH7zpmIPqm5-6G8BEZI4cgfJootP_RzycfEsIYCDZZweEeHk_cpZa86CwbLvRZkDotMT_kxv-uWEI0oLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=LnC4gbDU20YtA9DuSacck-vDDbXwBwjgAbajPVaB0ZcpD4blemV-8XiKoZ7dap5se1empPZOJXPe4S16yoJhhQ4ePHUocOwOikTLF38BNu1PgzQ--e2iuMJfo0U_sl3Do462J0RTJvOsZ2Qxew_r4-B-hLbtORA6vYyeDW5IYHAyIbyHKTtQRCKpGZ8B9H54nUp0ZEupHNoA3L0z_Ux_7h39ks3jWCECbgChe9JAWYidLpILlpxGsVsuF-YZ0AFGkUg31MfmC-xsAxYI51caIqDJ3eyZ6_GRv2uYoYd38oYgrN9Nui4zh01a22_sdqww4W0FXd-jpr_mxtFfl2t4bkOoF_XK1Jmm1hkKAKgSEzrsUX53YBXQ_NJlo_iN0pxFa1Yx5Xv8PVrRhWg2wN-GeuTR7Y06p8nTfhi0MZaRqbz75DA7bP9GaZGm2TQPTswc3_EUqAcJ6hsXBd5n8nhFepjTwIlJFziQbXohx-b4D-9n6b7Ws8UQTZhJhvcniB-4fOnrTcw8quORqTLtyzsfS81LwLYLQgXbati4t-zP3S8Bu0leSVVAOH_S8lSOXoaKhdWW2KHmgY7XMiwCBe2mJf1P3vgH7zpmIPqm5-6G8BEZI4cgfJootP_RzycfEsIYCDZZweEeHk_cpZa86CwbLvRZkDotMT_kxv-uWEI0oLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اساتید یه چنتا موشک سمت بحرین و کویت ول دادن. ایشالا که دم جام‌جهانی خیره
😐</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90768" target="_blank">📅 02:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90767">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این وسط که احتمالا خیلیا خوابیدن، دوباره خاورمیانه قهرمان درگیر آتیش بازی شده
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90767" target="_blank">📅 02:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90766">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این وسط که احتمالا خیلیا خوابیدن، دوباره خاورمیانه قهرمان درگیر آتیش بازی شده
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90766" target="_blank">📅 02:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90765">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">💠
سلام دوستان ! اسم من مبیناس صاحب کانال مبینابت
✅
👌
💠
اعضای کانالم روزانه 3-4 میلیون کسب درآمد میکنن
🤑
💠
میپرسی چجوری ؟ داخل کانالم عضو شید و شروع کنید
🔥
https://t.me/+vt7V5iY0jVhkNWU8
‼️
اگر سنگین شرطبندی میکنی عضو شو آمارش فوق العادس
🤑
🤑
👇
https://t.me/…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90765" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90764">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_IsDMkn4RhTHHcYu_8KWLYVYDz4Cb3pK-hrnHSaa6aRcAJ3uFiFKkhsewy6U9hZSQoazIEHJDI5VAilorVgadgS3Vd0oYCPcuiVm3JnWqeOOuUfzFDHTGgjvVghLmo2Htfhdr_tKlEVZDhGIOSvRa3Zm55LIJ8ckHAF_zd0Q2AHvVRIz49TA1e2RD3Boh9x0bfWYkSbSY4Qnibq7Lf7Bdyv9gaMec1p38zfjCuffEyhys7FokTtvPbZencIcdlx1Hky137YEo_00rbtizD5OjP_maKKy9zrMdyrxIB15foF9HCqH_3b_V22flBnDTya1ZvJUxvHiZ5dWyrXfKQ-cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
سلام دوستان ! اسم من مبیناس صاحب کانال مبینابت
✅
👌
💠
اعضای کانالم روزانه
3-4 میلیون
کسب درآمد میکنن
🤑
💠
میپرسی چجوری ؟ داخل
کانالم عضو
شید
و شروع کنید
🔥
https://t.me/+vt7V5iY0jVhkNWU8
‼️
اگر سنگین شرطبندی میکنی عضو شو آمارش فوق العادس
🤑
🤑
👇
https://t.me/+vt7V5iY0jVhkNWU8</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90764" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90763">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCE9qjEUbTU-hq-MEGg1NiHKtLlHHif-4U0yis1K1E4ekEG2ckZHWsZGqQWPtIo30G6mCItMwjOUVTI61ARY8jq5aWT05Z480NcJfW6-8nFOY6tnke0ucuGWRUMPhjmFD0BHwpSJvwEXUDjhvAPc0TUDzch6Fwyx1D06EGeKSojGrxIK7QJeK5coeU22si0DOPBp6oajxtWC9Ay_yV802SphmD7y7jVS2zT1cYvALrLStFwKuck-1MtrOa3E0n_asIcV5WwfHA_pM1nmzj1DWAbsCW4HFf2I8SZwUQxKfYvY_CqYZFDzb5aUGeTS03adVp1VtsneQRNwlGSt_e0dtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مودریچ، رونالدو، مسی و اوچوا از جام‌جهانی 2006 تا الان حضور دارن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90763" target="_blank">📅 00:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90762">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM_9mnegArID25FW1kqFNn9xrGPbnkdkn5xiMBD38OGPxQotElwPF3p9n7HAKUaoml5p6Ti2QMe0OI-cMrAA8GeFrfDStLKtvdYcYmRnHzpc0e6Bdn5f0kCK6QnKDbPhrl6BPEhrU605ilsCL4kSqIr8nXN-ZVX3oOxo0R9VYFGW7fizylJ-SssEhDg2x6XYKIdkQGw0-ztosUcQMhLyywWR9hLbQxWm5tzxdrNK9F87HrBnoawlrfb9p2f8xnPPmQO5v0AODhwH1fPsIeCajvMLGo77W1zpwXRX0Gf29a_kZBk4UTfxYa2-E6zg97mUqt9F1oZMMHcOTUGRDuex9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووریییی رومانو؛
دنزل دامفریز به رئال؛ 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90762" target="_blank">📅 00:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90761">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KF2OQt9oEvuDlAU3nby20BakBr0YoObQb14xYtqDc1R25ZNvgJDeg3k7ikNOVSk2gne-DdUv7z5jJPFNzk6HB3BzDPQ7WkY0JuYe7H1YHUDSbP2d3i0b0O7Az2iJoPs6I_gmIw783xEooXGVlkyl_ENFQsuJNE2RmvuJ0_PopGLO8y-taC-9ZpRxhoLHs13KVIRNtPLtnz3jAh-13iing9WuVUWEnoFoUgWgcUHNs6BUFfD4YTh4BnfFoHY497F-wGRNHqqdAsCxJM6nYNr1ZkiUEl5NIITiuxu4csxWwp9n1JEYVQE3ZNtNKwD6rxa1Cg3coZAlSZDYKG0-mhaF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولدت مبارک کون عزیز
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90761" target="_blank">📅 00:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90760">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lADg7t_UOfT30XN1X8lfEZCnisV8kGR1cTp8R0arkY4pUXPRHvBm0hV04GMVYCkjkDSr56Nz7028XU3pr8i55buAAHFXAWKXnKCltFcutWUT0q3BKC7dYXPN6VWqGX4jBx3KzHXeqm8tht1noa5MdIQ18x1-aV2uVE3euFwKhRCHBy6fUdg7C1utL_noLB6U_CM4auDXED-505ZFnEEpdljRi46ViUaqjxtjZXhuV9mOHpCPSXXFLVJ9KnlFNWjzZi_QZZCBM2yQ7OhZnjL3FBJisoaiP5xO-tYwlrXXZBSWjaEBcx4KTf6Ay9LG55RSg_XNiV2vuIAUkbZqDmDu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎇
جشن‌تولد رضا شکاری با حضور همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90760" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90758">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90758" target="_blank">📅 23:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90757">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-oQ0heJsRpwYDmWK-iuyULEUiqsQvn2-xiunkqeSy3bnbXgm-Bl-pwsEap4TWQIfPrRq3Y3dW6E3SA_9ZpDFZh3MPLpas4UuIs7GiUwFwkpFgcCbVZKzXS3Ch5OYuFxYuQCILRK6Y3PI55-ylhxxCjwZs6X7Vr1mlPYM-UAyBeYJscOvgJl70fxMJDSGXcyN65ADd87T1ELSMeERPb0YOLP_3bj9HGF-CqLAtKbIn3WrKP2_wt0D_O_CE_N9_TfZP67z6FynEVwtrYHD3FxOxQGoGURPlroZWG8b7fryeu5CVch_MFpFhwokGv4gohx2JX_oLDDMDjOuZ_srJH62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین روش‌های سوپر اپلیکیشن روبیکا برای جذب مخاطب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90757" target="_blank">📅 23:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90756">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7127e40488.mp4?token=KO9eeHQmGqDDRksK8WxT-7zh7VQpbSH0fFTlI6mujpRHuUJiTzR7aB7-VZTolcfJAdaKc-R5eIPvCs37baTvTuTdGXcHqQGIvO8D96XgigzVwZFgYTHqq5QTW2x4cZ8h1RkbprazwPxuk18uHj5h9B2Nt1JFEIqxMj_XNDLqFVFPnXbHlW1w5K8W4aFlZ0dW23w2grVKGbGRP6ll5m4MC3az6T6NsfK3wZGSTMH1U3hIAAPxOe-EsFueClQKF26MUh9CgLRq_JEZSuNS7P4KqKQCehiRe-YXq1aUbc_hCLoe4iedalxOnueuvtGk_f1l_B1g_LWbS6o8-bkDq4KhZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7127e40488.mp4?token=KO9eeHQmGqDDRksK8WxT-7zh7VQpbSH0fFTlI6mujpRHuUJiTzR7aB7-VZTolcfJAdaKc-R5eIPvCs37baTvTuTdGXcHqQGIvO8D96XgigzVwZFgYTHqq5QTW2x4cZ8h1RkbprazwPxuk18uHj5h9B2Nt1JFEIqxMj_XNDLqFVFPnXbHlW1w5K8W4aFlZ0dW23w2grVKGbGRP6ll5m4MC3az6T6NsfK3wZGSTMH1U3hIAAPxOe-EsFueClQKF26MUh9CgLRq_JEZSuNS7P4KqKQCehiRe-YXq1aUbc_hCLoe4iedalxOnueuvtGk_f1l_B1g_LWbS6o8-bkDq4KhZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کفاشیان : آبشو دادیم آقای میثاقی بخوره
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90756" target="_blank">📅 23:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90755">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fd2c5dbc.mp4?token=tECsCgtWBNQHrEQiHF3hohxMpFZsA1uPcYnwS1xfP3l3r4qCX0uH-8F8tKraXULFa5xYDlHSAUAPBxbYI3VsOqmN-gaDnoM2RkOPm_DA-4EPtn68UKjW8H8EwTKHjdRlAw5PouV37uuWwiMvco-5oSJiVbBbc8A_hc-3i4Tvlx4MYPT7l1OMqNXsfvyY3J6khQDS1BNQSsn7e4ach4SFV1nX5KiwdayjYXoVGou9P3Zxza3aKnh6EgfJiEFd0YTMTp3A5hmNMOMFZqWoB6G6cJenJw_Cj2kzeVUVBWH-PxhKMQ6mR9oafcVSaQNqEgLHkFC2UTIlHIAUDI7Rzu8P9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fd2c5dbc.mp4?token=tECsCgtWBNQHrEQiHF3hohxMpFZsA1uPcYnwS1xfP3l3r4qCX0uH-8F8tKraXULFa5xYDlHSAUAPBxbYI3VsOqmN-gaDnoM2RkOPm_DA-4EPtn68UKjW8H8EwTKHjdRlAw5PouV37uuWwiMvco-5oSJiVbBbc8A_hc-3i4Tvlx4MYPT7l1OMqNXsfvyY3J6khQDS1BNQSsn7e4ach4SFV1nX5KiwdayjYXoVGou9P3Zxza3aKnh6EgfJiEFd0YTMTp3A5hmNMOMFZqWoB6G6cJenJw_Cj2kzeVUVBWH-PxhKMQ6mR9oafcVSaQNqEgLHkFC2UTIlHIAUDI7Rzu8P9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این شکل شیک و مجلسی تیم ملی ترکیه بدرقه شد
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90755" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90754">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnbD6Os7qvJ53p5Y-6vULLcO2yejQJdAOKcajz1oGJZ_A_WpeOyv78vTBxAeMSC7aOb6jXGWrhAr4aOWRY4g9Pt9fJFsxquSzkQT-3mWN61mqVX3yeQZryXWDbGISSpC-jAwaDSH1r2ip4NUSgqbmo9wayjCUJ57dJ5OrRsIBUlUTWw9z-WnbHJyPx-_LIfwwI2I09MOwkhq-F6gvErha-li3FvaSvKoDaBIYIDm_H7BHwnbdeAWwyKs9hJnGyiU3knj7ah0zvsEIPakP-6JTnEQ3jNJUF_VJvdmVxPOK9kv1BSy6foKfwqRczYnZzlxwAbKrH__m518Gt1jE8b7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هلند
🇳🇱
-
🇩🇿
الجزایر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه دکویپ
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
هلند در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
الجزایر در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر هلند
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر الجزایر
۲.۷
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه : هلند - ضریب :
۱.۳۸
🧠
نه گفتن بخش مهمی از استراتژی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90754" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90753">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ram6-dy_YQJYHr8jPar6BCNQsgpWgAxrUWFZzHqSOZAjT8IbaLZdFWNJYhmKV9JeP_l6g44V4u9DuQ6dYo06VgzsJq4c55xm88dPoC2grTIlI6Yzf5uwLv5ER5GG6KpgUfTKNVPVzFqjGRQruFi0oh6mtR4UVHOm6-tt4GUYO4mhfUxy_FlVSTAAZ1AjSREIaV2y0t0Ik0cx437L_WjQEjxUT7fBkeC2sAgbp41Rh10VPUGXCKZd_9u6d_ko604IvfW8whlG-6SaqMEPI5gLlDDq_vPxEA6zEEyZLUFkoqxZX7YdEstki5K31fQ__l488k82GfqGOibodWwGcJ1cFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اون ایونت‌هاس که ناهار میری اوین.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90753" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLROQ3UibeepklMH3c32DI9BHEcSEfSXN1COGxPxBrc-6y6TaZ4KOLrrNSIBPHTrtJSZpoo7wMdE6xMUmh6I_nVgINjvoZGM-9aP6NIEK2NHXDOEX1vM61lmJMGLQvenK1uBHoyzyuSpkap-t0MeGiyMetBId4wBiW6NYGY6WnaDhzD2D7a4PC_SLwFe11MaoCum74E8rMG1zrVTQ8uZewZQZ1aKu-crgnX5hMkaVfls4ndTT-7YO6z7F-qEtvleL3tDXxzm_GylJSgMivkkzwKiKu3dgSzRBAzjHm96POPM0udd9I36r9XrH9Y_l1FJSg-p7YfYK-5jpbXAVRgfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریکلمه بدون اینکه خندش بگیره:
میخوام بارسلونا رو در دسته دوم ببینم، خیلی خوشحال میشم حتی اگه کاملاً ناپدید بشن
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90751" target="_blank">📅 22:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bek40I1B0B-Xl74cg6cU3QENH77ghadentASLjAxQoWBXVQd0oDWasaZITew0mxmT0FNTFJNYZVN_WBw4RTU7kMTuuLQsUFt1cU13W1mLtzmN9vp8K3yhgYTeETTG8heDJAL97hP0Gzak-qntwf0vCsFPLsgA767uE4BzBSbvOzWCTm1Sg_UwJPuRkoTRH550GzrOWrbzHQGc-5YzE77kDuVzFDV5z4yDDL6rHVfMKLX3vCrs2VtiSEk-X2NnNwSMS10f3yFErexCOr34jcRW9e8F2KupNNyrThIDF7SieeChGGEC_1UT33eVQP-8FadGisMH8DD8T_gdQQSrIdodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنسو فاطمه دید تو فوتبال گوهی نمیشه زد تو کار خوانندگی
پست گذاشته ۲ هفته ی دیگه آهنگ میده بیرون
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90750" target="_blank">📅 22:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90748">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMvL2loMwDDtW3dCb3c6QhFdeBpPrCnPrA3SOCdu_mNwbsCDc5PFa5LXsT0BvlmSfIU8xghgRALtHXCTEHW-6sv9144t3A3D9XN5uRLM93xHn_cHw2vSQS1cJ6YXbyqXB6pLG20EqAoG_rb67nwdcnY5dC3dddmVBj3XHthREOmaeuUJiwN2L2oBjWLy8e5vboNoUHL3SV2q0LxYx_GgLvViV2d7jmaapXHBWJ4fvG9jJgH6hyjU0l1rtTYEYzASy8esh1_ajUdzu_wF1IxUM2ZOIyNRDODE8aZNAYuwJmXuHUur_B88jK6k1BlUtKbdIwa-QghynH00Upr0xngiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید جدی برای یاران نیوکاسل
بلژیک با برتری ۲ بر صفر در یک بازی دوستانه مقابل کرواسی آماده جام جهانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90748" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90747">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromernesto SUPP</strong></div>
<div class="tg-text">🚨
فروش اشتراک V2Ray
✅
سازگار با تمام اپراتورها
✅
لینک ساب اختصاصی
✅
سرعت بالا و پایداری واقعی
💵
تعرفه‌ها 10 گیگ — 200 تومان 20 گیگ — 400 تومان 30 گیگ — 600 تومان 40 گیگ — 800 تومان 50 گیگ — 1.000 تومان
❗️
پشتیبانی ۲۴ ساعته  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90747" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90746">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPuYFqaY5an1NF8KjFLhOvJLAS04Kvc1I8DEkZXSjThYmjuK07PH1-EUBbkIKD5WIdEZihnkQSPDuHTrMG_UtdlEHJg9e2yKNkasQ17_cV459bt-ELqT5pYSXfAL-tuAz_ISdY5il8wdIqAGXbJnx4kq1lBOit37CxhJrjYF_aHVHy206I9c5F9EsjWsT3cTNVMqKLW8PlaGSHg3IOOREe7pwpufswUn0tdiWLx0g0UmvK6ubnJKc9rsWqeOYnqa1Dyn5C6DBL_fQptCoXU95dfT_SlewUkyfXJBct5D9pQMoHyzw9uqSB2v3emqJ0CImJKU6EYdeR0bzsacAIJfQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش اشتراک V2Ray
✅
سازگار با تمام اپراتورها
✅
لینک ساب اختصاصی
✅
سرعت بالا و پایداری واقعی
💵
تعرفه‌ها
10 گیگ — 200 تومان
20 گیگ — 400 تومان
30 گیگ — 600 تومان
40 گیگ — 800 تومان
50 گیگ — 1.000 تومان
❗️
پشتیبانی ۲۴ ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90746" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90741">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOnGe-HGH8IlFhbqlIkccux-5s-E2a0iMsDwRfaE1JQmYJxa3gr-SNgRlTzm3zFuYPiREh25ONjkixqdIFNvPe7DytiECUro2Lg0qVTGqYWASkCwoYMoMIGHvtLCvUjOsNh_SpQFgqlLr8KubVZUTVrDeMv1BubF8iEodmaTxfCNKwBLriGiTvp6106aZYa46w5jcMB_r3saGUkd9_N3kQPuocCmXumd1Ds8oIChQTtoqzkQ68RHljIJgbrGthkp-biZX5BJNGKOZKwMzh6FoaWI_TKUCzo_oTrg2TmxNFTuXLOXubFPV1IwgWEZJLuzq-kRcG0pErNdT1xegWlBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAFXGne_EpQgyYBu8g7GoPH8HQl6wN6FL895c7RZ-eCkdRqjb5so-k9Yrs8GEaSf7PauOwrU5JuZQRZw2-VnfZ6hJXBOMAJ8TV-osw0RBuivks4EkA2Z7CtaJTsNrQ0vrHMGo195SqZ-fhOAUZvEKRg57aE9VRDm00TH8CFfP0KO2NLj_8itF2nBVrlQ3YSfi2hOEQJpLWxWC7tJTyGZLpUjlThdE6YYsbqapekOmwO5N71An0HNOTE9gURLEmJK6x6onMpc7YdN0t8tZRxauob9mTtlhJdHpAWOHuNmqqZR_zDz-IDLwsrTvOTo_-auqvOWIld8GwXAVRN-ktBYRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیه اینجوری تیم ملی ترکیه رو به جام جهانی بدرقه کرد
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90741" target="_blank">📅 21:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90740">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOUQ6Mztu4CyDSVNq1jzXnw5OJT4I5oEm5_9bKK8Ukn1uFNswxA4EKOpK2qmFHEBJVLZ2_qVedTi3s56787oLgMsSPNVzdsuIFGyQ8LRvS--sGInOlCyjjVcBeoRzXiKuTEuCda3V8QfQe3nxFk4fLFts3as3UnJgEJ4J9QM8ZmTn9YjFQg81CojHUvDNYFMrzD3ccEjqLHZJFkXzG2e3UEj6hznAYhhK2i7UsauhE7s8uD72xSFb_g1EHqJUHAGtxbdkAJPVa_VUzCTnI7XcrqVUfgjFgd3KdXPAuEF1-aCV-gsdXyC_87sw_2ImmGFDrI0v_0JdUTIH9pc4JacXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
شماره پیراهن بازیکنای انگلیس تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90740" target="_blank">📅 21:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90739">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=c2a5UEJXCAZe_qdPDB89g0yxWRfIOCyVsEOxzFQ0t7mUkMJe6DFrwmVeLQJ-304x5oRtawzkKH2vUp-A8i88MJEPtCjRXoxCGq8hj7KswANXwD1vc35oOIazYuqWajvaAW5sxYIj18hVVPe6AQttCRzI6TVAz8klAjiV9kkri8PQOoelC6XJ3dQ4hRRUokp9yc4kqbIVCnnulvfRkhj144bpOkYSBdaNMJj6CHHtU9tNLkRRu4K0kvD0TjMlIUqdXUs5LOnUE1jslYQVxDlk9R2QzeAppLWQmRZ6gZGVHoE5XyS2I7z2TQ8FZE75z6wKK_VjIWEVziijQ1RSluOh9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=c2a5UEJXCAZe_qdPDB89g0yxWRfIOCyVsEOxzFQ0t7mUkMJe6DFrwmVeLQJ-304x5oRtawzkKH2vUp-A8i88MJEPtCjRXoxCGq8hj7KswANXwD1vc35oOIazYuqWajvaAW5sxYIj18hVVPe6AQttCRzI6TVAz8klAjiV9kkri8PQOoelC6XJ3dQ4hRRUokp9yc4kqbIVCnnulvfRkhj144bpOkYSBdaNMJj6CHHtU9tNLkRRu4K0kvD0TjMlIUqdXUs5LOnUE1jslYQVxDlk9R2QzeAppLWQmRZ6gZGVHoE5XyS2I7z2TQ8FZE75z6wKK_VjIWEVziijQ1RSluOh9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هواداران عراق در انتظار جام‌جهانی؛ واقعا الله‌اکبر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90739" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90738">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISNIqegqw5B35BFBoKWQIo5_DbLrL-mpYrrCTqqaqHbIN4iOVCq3XGx8Hel5C94j4hdpcvvU9UHUHi8brrilksYx8LwifdNQaI89kLAeqr1D918ytjNcEYzRBGK8L-FCGRgqUE8OymxrgDNHsV1Ayd6kvGN91_rbQiEMghOezpnaxUjGe3R3EBivWFqXO1BqEDC-6v0RdUFRMBm3GPkmWhB6NW4eEapaQgJLE1-sjdG6jFE1EiBwjlG3xxrzrpoIwCTwBdM9h46eBjMl7i6YrTBcaJQGoyoDCHCbPvRxLWHkoS2mtRapWhKGm4CryMO_EtdeFIhhOTHhqeB_p-UIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مقایسه ویو موزیک ویدئو شکیرا و اسپید برای جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90738" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90734">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsDsnMVGK01a5ctCmGwtnEZKgJXqCevaH1_sTw-IbDDRZ3kehBKqtv-GAz9mzLUBtnkuw7OygYepziYw4SNSBimWm9HWL_vNo9tXLD7vQ3qcf6aXZdEu_VcssRIch5EpteKbB5Z5b_RwElZtYLdlu8JgbekB4nNzZRGxbXldENdIc1MSgwAxrIjnqItsAs4lZj-LhoZ5ShVGe4qDrkzfBgvDn91C-An-VUsvojxEqbSCoxwVE6Vu46PPyv3mhkNUwV92Fic-PldhiyX3dbxiHFgjkAf9OJ3FTYWsxAXtEWnB1oy_XUkod-g6vvYVDx2-mOF3NKLi_805SNw2YWi7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eaERA5VtPBD47-Zjz0Sw8E19YmK_FLioTQiKCIKfOBxhaD3pavem-psG79IkXagiLNWWtsJc1z3sRBFsSfOO3idynJIDzbBcnNGSQWaMCVzfwijOyCuFOgGVZ6z36MJn-JK4vq9gDMs3WO_CgkyMrHgcASdTd7ujrb8ZMaqZWg3N-6k6rl8wsbF_T4qNy59XP0cJU4pdMQJWeKazR9ik3iWPwrdDVl0pCRggPobfJzaP4XnxIJsIJ6-Fet4lY2iTf04zO2CaXz-7qW0BuJvVUI-85FygdM0_SF9xBSKgOkSlegwCHnVYc03KqfBsZZqFjUiVWDT9m7IydJcsBqFGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6UOQZnNNMwy9J-qar_k4x5VgMjDr12BVYBAwtHnqTVUAZd3n1KWHqNLgeCS2JZqUKvsJ4GRTtMbOsuhRx-QC1MTVZ0JCrxeqzRF5AB60Y7AF9qRmN3zI19FOj6ZpBIf2TiZikGRO5LkOoOZGcrX5GltsuACkanE-dbvi9fW4Mz_wOw_FHCkdB5zFym1XpvOp_OFt7a1hJpXmLIFOLoVsZP6HbPObzdDhOGDXtK297mrqh5Mv7hPJO5WG2yEnjoYrpjrop5RVYl1jry8WTB7bJAnFddC1kemeu_HShVhgHMozcNE-YyARJ86pLG60pV0vo1qrbG9je20byv6gLi5XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🙂
بلاگر خلاق برزیلی حوصلش سررفته اومده خودشو لخت کرده که عکس بازیکنان مهم جام‌جهانی رو چسبونده به بدنش. طارمی رو زده رو باسنش. وینیسیوس هم خودتون ببینید
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90734" target="_blank">📅 20:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90733">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇮🇹
#فووووووری؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90733" target="_blank">📅 20:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90732">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQKGHeAJTrDzK3mtwGHecnM8xS_hAvPy57A6X5TZR8ureD0GKbSia33oiaW8C2ldaaW7NnZOYmbGw0_n87rxYpxime6BPMJKm2lOLK_-XNq0URhdMJ_VhPJ6xvMs_RUGoaeZ8d6C7tiR1BmqKVm99deHBsbKsloRJf6vtSigVoJMHNBEau2eMkeR4YPwV7b6TH_f9oEcM-QMO1l5i0N_7vSFySdji8yY3bKlzghK-Xwlqo0rnnz8BZSQUrWrBGhL_w0MDQbWkNSHmrYmQ4uxxYHePXsyam0FXgc-3ecKFEE34yxvl9oOCRiHALWuKW8hooEsXbK0ZLQ3atSg6WLd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90732" target="_blank">📅 19:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90731">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlSnCn3-UdybhLi4aHchHtJ2A5mFdXWJtVA4sXhGAhcTugw7-OtAA2v1fgMs7ZDJerfMSnqMXejUbOFiu70lDiFz6aGk1bPSZVNkqao8GQ8LP4cpFm8nqzTCg_eSrBcMJDWpfuCxWYm71FcnA2KaUmdR4EzkR99e0JXH_yD8z2ahKVD6EAtArYl0i-OPkG8kVTeYPkh0ULgh8QWAg_dHxH0I8-MwARYrFR7n7ZmBV7NjmwqCUs-nL1iGk4VQCYFPryaBpmmLT7qMJi0cw9zi776jYgsAtxGU1fdwXNRZ3pIqYtleKmj4g4ermohGZSkLWJZCX706OgQoUzfcJWLNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🤩
تبلیغ جدید نایکی با رونالدو و لبران‌جیمز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90731" target="_blank">📅 19:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90730">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEMYIHGC7xL_1uCNvfhosAyLBcTa55k9Mm_iIO7FkrxFHoZBqC9czgSNWO9759GS1du0BkvKC5gjMr_O1WIz7NL99UyBroHGjhhKTnwRw-XxbSPWyrueqyE9kEzhgl5_JNycXQXWS1uiUFmQS6ekBWHUBf6FLElI5GWhobECRB3ZOt3KnYNs23z-2bMEN5LQyfAQ7wDD7UyFicrnUxisf9M-1eDCk7LsrLgsX5k2xeDtT7Djm4QyFsZe6rjpe3AmWOcYaXYhIRxya7g6O-J74eSJo5Jk0OUkw1nGl_n2mmLyPSK_9EkP05uD35C2jecPu4s5y6mjgM6JUjhrpb3QtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
دوس‌پسر گلشیفته فراهانی امروز به تمرینات فرانسه سر زده و با امباپه و رفقاش صحبت کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90730" target="_blank">📅 19:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90729">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_9qzOHkl1w893NP40cc8c1BoP9rV9ZShbVN6mdyf4JOdYvqWz8Z6SjABO29o5jYI3DFmKh2Q3m5cOuHJS2-o6UMbtdHER5tXw3nQ7cKHw9JeurBNw0dEVVODls9mJWBfpJ3f8WTYVVBTair-lIF_lbxy1NFBRtfcxAtcEjF8Na7NmnZZvNF8QN6i7hx5CgfjzjIb2mOufAeP40XIhSRE6jv-XO3fnOORoly3R5F1Lu2y90rMTncVA8tVn1HXwRA-va6EqAeFvyhv0e3cKAQJQuLiUFOtXlOmYCesWSAolpusZ3ev-ojyHBiv8dJymKvJ8EsFzlrHImtSJfC_a0Q5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ گستون آیدول ( معتبر در آرژانتین ):
‼️
من دوباره تأکید می‌کنم، موندن خولیان آلوارز در اتلتیکو مادرید برای فصل بعد خیلی خیلی سخته، در حدی که تقریباً غیرممکنه.
🇪🇸
پیشنهاد بارسلونا جدیه؛ ۱۰۰ میلیون یورو کامل و نقدی، بدون هیچ بازیکن معاوضه‌ای، ولی اتلتیکو این پیشنهاد رو رد کرده.
🇪🇸
الان اتلتیکو در ظاهر خیلی محکم و قاطع رفتار می‌کنه و از طریق شبکه‌های اجتماعی و پیام‌هایی که به رسانه‌ها میده، می‌خواد نشون بده که اصلاً قصد فروش آلوارز رو نداره و موضعش رو تغییر نمی‌ده.
❌
اما واقعیت اینه که نزدیکان باشگاه خوب می‌دونن نگه داشتن آلوارز برای فصل بعد خیلی سخت خواهد بود. برای همین انتظار میره مذاکرات طولانی و پیچیده‌ای بین اتلتیکو و بارسلونا شکل بگیره، و حتی شاید پاری‌سن‌ژرمن هم وارد رقابت بشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90729" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90728">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90728" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90728" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90727">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDbHvloutIR05G1WlOgQTb2Qsx6q4l93Geby3saWpA9Q0jtF9c649--gcfF6mBOcCDLFcWuoveDcYvzcNcImchXurqPeVCBUSu78Wy0yGE1boDcqLiJRUxv7wnwULf80cr48u_u2akflJuBQs34CGWm52Zpu3r75eontq7xA98deJQ7attv84wqfBLIA9vBE-w7V-2ho0f4aHLQrKIw5Ecasr4P2dQYOEdng_Q3dgb4L4v7jZYCf7CcSyikEPCAajT8agYm0Fs4X4TU3PI4P7l3ZrIUmOtVKNg_R0RWSD-bW7a6daIR5atYV2ztrQk4eZtZQbpQC8dBhrlHiZAhwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90727" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90725">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX3sj8m6tyKSSerKMrnoNhxUtwZZS4nIHq6A_7IKnCbubQKR6CBZ-GwR437hLgF-LWIglxoD86iwYmDeoUFhJrW6Y1dOWVsqtJ5vGWlFOB8S6R8pcRvoJVq7BxIut2OYc1Mu8qXt5xoGcgSH6BbeC2jcd3X0EbTHoMlhjvQY6kV3x6FJnJRBftZC5wFoTM1K7z4wrZCaoYYgWqQpqedhM1w5hUjkrFs_ubEhSdXC3RT1Siz5c7Z3uMZeKJBvCWPQ_vuA6joP4NWM4H3tx7X_57BEsH48mAiTQ8F8l3Feqpvwhu6j7YoUi-iUWOQaAfekfjIdim9TmrgJ5h2sU5lfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووری
؛ توافق اولیه رئال‌مادرید با دامفریس حاصل شده. کهکشانی‌ها میخوان تا قبل آغاز جام‌جهانی این معامله رو انجام بدن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90725" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90724">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLaaFPrg5Le1u3vp1dSyaGaEwAUdqwBVJwzXH6t4WJim9j0LA4LoI8nUb_v03vCFvImELCSrcsDToqNNLyL9d8bkBMnT4wOyAayXtqqVIsUIJ8NsmtYGz_Oyv9r8KRqwgM92HKZgPmL4pBEs9RnDQnfy607ASDls7NhSXrVRgu2bIoJlEjmtUr0lKsjU9lEchKhmf99nOyOZkrhn2vYO8Npq8AGylCdsz5htF7uO3XKzXfpfH28cVqNJxtPQw1Y6YsvRpQGr5mqqjwjs7frH_5qVOuvM6WvKoNOfEU4rE_2MhZfn7Q6h7LXnUARpRspuJWNnJAYPnkluXljppsNCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ادن هازارد برگر فروشی خودشو تو بلژیک افتتاح کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90724" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90723">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تاج: 100 هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90723" target="_blank">📅 18:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90722">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b72747be.mp4?token=Qj6W_qRfile9e8-TE0aHFU9AI5b6OhMFonRToqHNEwsJFjL1RYn5GVkt1C94SEK5LNCyRWaWHIY-_khFx2icl3KSDqwz6pekwfw5T3jlN_1vRs9Vf5fRbYlnnjK9-Q-QpuqNF2h3_cnUP7O9tM8Ne_mPgzL6W0StBDn0LsT3lEWykYAW2quiwyoHeZXzjyXpRPYtXmXeNqf1xbvaV22XWXEnTcLjAZVeBEd1Z-wUJig3qpHE93meeXCgFDKQHxHkxy1zvYNhhjvDO_zk3LMYBC0jZ1t2yKDJLebcBKpscwjBiBeaFlpb9WWs9gk9_99u76tzEymlkDg4Ue7DyrstPAw9kZZE8bVv1bouCNebCasV4JQMOlHXPOo3Yl9x3R4c6bWWm4stgLTNlIvxSsv_r5D3NNVODN1ZsgqDYUQS6963V5UTvffQeX7DRPg3aJwf-dqzjPeN2SKJ0q_BG0iDl_Tg7MCNYsoREPxAe3VxwrsbkNgFcMlAxrPcaGh_lkOCxq4YvuR4Xm1OuI0_M3CNPHtNz0vRdkWbAZgto46JD7MtdxfWEw-ei3qdkvi5hDpUZtBJg6VK7t_yT8GeX-19C_uShKAmQLzEolDvILq5adgPkIn_2Tqu1e1W304LIxF8q-LPS8YpriJHgbwaNaNt_S-nj3gUw_ujEJzuMDO3_8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b72747be.mp4?token=Qj6W_qRfile9e8-TE0aHFU9AI5b6OhMFonRToqHNEwsJFjL1RYn5GVkt1C94SEK5LNCyRWaWHIY-_khFx2icl3KSDqwz6pekwfw5T3jlN_1vRs9Vf5fRbYlnnjK9-Q-QpuqNF2h3_cnUP7O9tM8Ne_mPgzL6W0StBDn0LsT3lEWykYAW2quiwyoHeZXzjyXpRPYtXmXeNqf1xbvaV22XWXEnTcLjAZVeBEd1Z-wUJig3qpHE93meeXCgFDKQHxHkxy1zvYNhhjvDO_zk3LMYBC0jZ1t2yKDJLebcBKpscwjBiBeaFlpb9WWs9gk9_99u76tzEymlkDg4Ue7DyrstPAw9kZZE8bVv1bouCNebCasV4JQMOlHXPOo3Yl9x3R4c6bWWm4stgLTNlIvxSsv_r5D3NNVODN1ZsgqDYUQS6963V5UTvffQeX7DRPg3aJwf-dqzjPeN2SKJ0q_BG0iDl_Tg7MCNYsoREPxAe3VxwrsbkNgFcMlAxrPcaGh_lkOCxq4YvuR4Xm1OuI0_M3CNPHtNz0vRdkWbAZgto46JD7MtdxfWEw-ei3qdkvi5hDpUZtBJg6VK7t_yT8GeX-19C_uShKAmQLzEolDvILq5adgPkIn_2Tqu1e1W304LIxF8q-LPS8YpriJHgbwaNaNt_S-nj3gUw_ujEJzuMDO3_8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🇮🇷
بازم ویدیو ایرانی‌ها برای تیم اردشیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90722" target="_blank">📅 18:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90721">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYgKeGCgGhxSbA4zmaXNZ8yMnQi8accMai_-HJPO14xT_4arXNhGfQKcPIzQDhqW_vKa8ElmhkyN7lNjRjsAD3LyYHtVJNFLd8WqEHHtx-4MStOE1iHTJzyLtj4hSWmi5IPW23IQkoYXnFyx_KfynfoiUzQX1rXgRgpsSxJ200Nz94t2qn91oLo7qfkI7jXTo_DsxcosqMcBPfO2D9Suhx-SOZtAjiIErZSPgp1bC4lh90DGKqhyiI16ltNPiUSP7HLoD-cbKEnyZDt0OndJnC-AX5omOEYCanP70l2zNNOxMR-9SNkflhIFoAGLO6gPbUPDjqoexb5jeVpMqN9_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
ترکیب امروز بلژیک مقابل کرواسی؛ خلاصه که اردشیر از الان باید حسابی چربش کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90721" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90720">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTO4Bs-aTHXgapWFrYKDaXeCFRfvA2OCO7GPe33EDEDfXCQysCNnhxgxLzSOvbsPcX95sFOuhcXbcsIvZx_BOV3qN3ap2IRzY0N8lWDlgRExaO9obWuMbcZEuXRD3yapB6b4xyXfgRJCxlpB34usIK6kl6esRfvmpB-FjZ02YDEDStglU-aMIPYfeKoDIyE24iySUTESI_VqV2L-b78fJ7p6QL-ik6sM6jPqB6cre1wRDfgZc8n6BbZOAW99I5sa45rtubCb4okltyvzkDEdzDlsYWJ4nwXb0vGBDKnAkPBr_PqiIp170IGz1z79aQP268ySnB2eM_V_Nay0M8SXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه هایی با بیشترین نماینده در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90720" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90719">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He6_UJXpVSnnqbk77joYfRdyhPdHmZFBidEAuozkTp_K2v_XUFSBPcB4a3Zm0-y2VQ01D3vZFdCJ-n-mP-rj2s-qrKhAEfdHolxgtfBAXdj2W1VUZ0n9Z8I1OAO7fswSIcxUo_LXzfNUpx30ZQnfH65we2i9ZiMIxsPIx30OImBT1s0wZtM5B-H9GQ_Dq5GJ5fTutskh9fMuW0hm4Xx_5lZVzM2Yuz1dtuj2juwlpMTxaI1BGPiRlPIJGsn3xtPINdGGi3HfR-pyvuDKzsf8qJyC9PhBz5nFp6dd_Zfcx5Gty9RQsh-lW9tOiSpAFzOPASD2Ol5C-l2POy-Qp1HCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
اسکالونی سرمربی آرژانتین: مدعی اصلی جام؟ بنظرم اسپانیا قهرمان رقابت‌ها میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90719" target="_blank">📅 18:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90718">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX3I1Zsukohagac_AYMQTj7AbR0VpAUS6WWJlnSqJoxiBpLXug7Ncf7t-3Qh4OORNi_0pQ1vS-D9EV16ibbab092BLp4iT6_AinZdwwWZSQrtju-IGqFHm7GAdUhZakLx2sjegPH0ui0TTfYS0iXrCEgY9wD98O9k-2KP8bw-lkE1YV6kiJl7tdp_x29e-ERWuHbHydY6RRkTwIjMSh1mfJe79FOZhNJyFRryAasYM-shzXk4Edo6Dxkzx4aXXEq95dM6cNAQm8EGaQnEd_EOL-9hfpAngkCDU7FrbeJ6Q-qMrNNEzphLFu3hC_3zmaNDmSBdZo6yczA6LROHVI13A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👟
هری‌کین درباره تصاحب دوباره کفش‌طلا
: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90718" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90717">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47c5a1723.mp4?token=I6SIhx8V1pU1IxffGDvbTsLl0z37AmSXI4JcNkCGdSN8GtuKGSL0r0_9ZAmQ9Oj_6zMGEArSiBuKZl1d9jYNvEXwpOhmhIPOOkytC9TL8AeEamA4yAVcsXPFm1OWFPcwVonMO7sznOoKNL8NzsHyKNRmX1cNOw4w8YlaR9jLslw7WL3tksBsfU4_ewcctcedBF3xV0Xd2WpE0TuII-eSiQCLkSUKhBL63QYSL1O1txeB1DddN3i0Nc81Uc7NMoFhFtBJBgTWIv_j9z2G244Jofeb0b0Nzt07jJ2XB592AC2iNb5Z6zO8_TtjvhloThGQ71g5LVyDyMrsQHBb9sqjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47c5a1723.mp4?token=I6SIhx8V1pU1IxffGDvbTsLl0z37AmSXI4JcNkCGdSN8GtuKGSL0r0_9ZAmQ9Oj_6zMGEArSiBuKZl1d9jYNvEXwpOhmhIPOOkytC9TL8AeEamA4yAVcsXPFm1OWFPcwVonMO7sznOoKNL8NzsHyKNRmX1cNOw4w8YlaR9jLslw7WL3tksBsfU4_ewcctcedBF3xV0Xd2WpE0TuII-eSiQCLkSUKhBL63QYSL1O1txeB1DddN3i0Nc81Uc7NMoFhFtBJBgTWIv_j9z2G244Jofeb0b0Nzt07jJ2XB592AC2iNb5Z6zO8_TtjvhloThGQ71g5LVyDyMrsQHBb9sqjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو غمگین و تاسف‌بار از یک گیمر ایرانی...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90717" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90716">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">علی تاجرنیا ظرف ۳ روز آینده مطالبات آسانی رو پرداخت خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90716" target="_blank">📅 17:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90715">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMWeU3D8Q3SI1h6yfbqSacRK0VbOuAuR_GEqnlgaztOO7quD02hNNe4TXVs-RdHzPxqkEb1s4BLcJG6Bx5XNymZZBA7me8j7wC0zurz748RifbKUfZxLIkuZ9QlqSbop_7Y_8qgPcC7Gn2aQMoM_j9GViiMh5LqKB2F-wewTsik0brf5-GsBkz_ZCvSYdwNkv1m-YT2A3pW2E258KVh3IrT1ud99r4szx7Uqz8dZwOa_P69jaGoteehpzPTsXqSXKYCcAcN8-geoMHjAt00c9hoFXvHadLgtrY4g_HTkn-Du7XSVPykhh-rjwGI0roGh_kmcXtOwLAkNPEm5-xKP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
املیانو مارتینز : اگه قهرمان جام جهانی شیم از فوتبال خداحافظی میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90715" target="_blank">📅 17:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90714">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnniqF1TRc8Sw8YCjGsPXjiuIEhwmm_sMuqUqE3ia7hPVIdx1zn_vcJkBXK30O_yg5Kc6JK5b4pKW3IryRLqaYBTHEA7gzGTWo8tlv7ZK8lnRHzNPiuUmNiM3XoqYUdeXzLxmXAp3REqPU5ZBshVXzs6r2vafuuTTvyPnQgI3A-Pp7ALgex4Z0h0A4p7BqQO-rfzmJQbm4FzwlkVqDK1VeOEKoNz7iXVEuI_nJKr4PNgqY1-wCKrEDvkHSQb_Bpp2B06YvPZDDlzYnS_-rUbvIoXW2pcCvcvbh5srOpyikjhGVwVZKf81ySrV8nZCNoV8MzJQqqIlGCm8ld6n-cmKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی #فووووووری ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90714" target="_blank">📅 17:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90713">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=kjNxvX2OHrAEGQdUWvhrwE_RvgtBr2Sg3I5aM3R8LnZ7EJC3ES_xRyFDqfvOZXWjTPC6pv3xSKwn6UsVd2BgWvdeh0p9LRzc7a61qKZnCwNPaxXRvIx5JmmtpVtyq1IEzngjGg_NrCAxtTcIpTNG72n-XHrqwf3dkDS03GpaMAOfGVyAqQxY_eGnruNZx-p49g0d9o95_Mb9d1eO1r1TDNevItPs0fzLPjsBfKg63MyGLN9rQI96k3TjvFZQVLnCrk5I9Q1L73Tje6k1MHFbsgUx4vJRhy95echlpD74U7VwabPZEs3Zdkgg3sHH2Tz0y7fXNfKzH2W2uC9-pJ0usA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=kjNxvX2OHrAEGQdUWvhrwE_RvgtBr2Sg3I5aM3R8LnZ7EJC3ES_xRyFDqfvOZXWjTPC6pv3xSKwn6UsVd2BgWvdeh0p9LRzc7a61qKZnCwNPaxXRvIx5JmmtpVtyq1IEzngjGg_NrCAxtTcIpTNG72n-XHrqwf3dkDS03GpaMAOfGVyAqQxY_eGnruNZx-p49g0d9o95_Mb9d1eO1r1TDNevItPs0fzLPjsBfKg63MyGLN9rQI96k3TjvFZQVLnCrk5I9Q1L73Tje6k1MHFbsgUx4vJRhy95echlpD74U7VwabPZEs3Zdkgg3sHH2Tz0y7fXNfKzH2W2uC9-pJ0usA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
یه رسانه فرانسوی با انتشار این ویدیو از فرصت سوزی‌های بارکولا نوشته که این بازیکن جقی رو باید رد کنیم و یکی مثل آلوارز رو بیاریم!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90713" target="_blank">📅 17:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90712">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpEUmRPOTcCj5vIBXNMRJ0H0BXebdRuD9wDVjfCa_VTYH-RhT1oKy5Rp8RizZ_McPqn2YvCg-oFdpp_5nNSInCccRSVBFNnI7_4V3fDL8Og8MLTHiNSEHcpywSuEf-CWprjSMRiAMTKBc5kvTeUkMORmyFVKDy_dEHtqwdaRg17cQ14RHf689oojvezh419UEmC_MB7phXi37OD8j8HO8DYyrjH8L90W0t15F8pWlTf6eRIoaPmeXbrB3L7oY-Pm48HjE-adm0_p27f1WdsczrG5zTsd77PSdeVGbpWrP9GArN1XxEDFUUvu58rk8Ow6O1jrYWmU7xPCfoXV94BjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
شماره پیراهن پرتغالی‌ها برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90712" target="_blank">📅 17:05 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
