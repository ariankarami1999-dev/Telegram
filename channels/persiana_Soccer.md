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
<img src="https://cdn4.telesco.pe/file/l2F25VWpSXTZAfmFUCSH5fyE2H9lvUDXTki1qNafgRmMwv7SYpN7V6kpB-eJr4J0enl-j4OPLYJxtPeFAGoiSnVE1ohbNBrfO2_7hqq7KIveY_g_MOmfb_Vl7e0FDdvIzG_ir3emmeAhGQnm3ZrtHA6PlgKDQ6eI_6YVSweJidtiMPePwHFlrtRIfd0XMDIJgZAQN3lzuv2pzRAynsz-kQV-aFwRvj4FOgfmgKlS7zN30jVw2QkKg-iPwalNNStOhJ2mnM9pjpuDo5S_MRuZNdDJs6vjUS_gOzwRs-vLhjdbfqoWOzOTob8IjJqqODac0g07xl_SwH2FmYvWNb4N9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 306K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 23:05:04</div>
<hr>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4IVrooT1f1aDlUgTrZOznReB19w0cfScZnFvJSkLuSTBGGlm6ZYPHyICGqrKLghhi2NMJ19iVT3kXbMiOpN7OXf9u3CbWearDQZv7CPJf5MV1Lz1M0IEkKSiT6ENydt0iwg7QkXbAc-Y9_ixB_K_gplnS-_Pfs9kbZ_w5q-WGQa4PCFHBV18PsGN-Dl92-8Tb_5TBI4GgEF8G0XYCvVkxB9kyZcbjS2HvFwVVgaOme-G9mrSzpldQB8DZc8uybAWBniSPME4X5nrAcZBYwL--TSMqwCzXiBBFLyCw4rGHEkSqqzYrshI4gnEnWS8UnTPpgS1aYsYHP0iFZUjzsvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان
؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/persiana_Soccer/23714" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE5IXXh90LLz9kdM6whiFT_s3tbC6RMGlDg30TN8OFEJVyBr2BK4B7aEH6kpbur2twa5UN2Vv88xDGKtSXUs_gYr2CrUz78qncleY3kIAin2Uqbe_R3Dg89Fqp3BMsdi0V_NceSvFEHo1qcTHvX_wVO3Ocq0l2SZMVIuLu1poRPKwAD7p_4dXK6qfd3Bj4ZiIjQ0-M2uENrCvvGWOAr3FywwF7doXKRTsDGpuQfgAmYnKPVEQp5dAEhaMUNlF03Gf4ttiz-jKq13xzH_o3Y9yhBviD5DR0zcckfnSm-XzDQRWWQkHnH_BlieDNLpGoasqwchHzEGQJ4E_7UTGckPpWBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE5IXXh90LLz9kdM6whiFT_s3tbC6RMGlDg30TN8OFEJVyBr2BK4B7aEH6kpbur2twa5UN2Vv88xDGKtSXUs_gYr2CrUz78qncleY3kIAin2Uqbe_R3Dg89Fqp3BMsdi0V_NceSvFEHo1qcTHvX_wVO3Ocq0l2SZMVIuLu1poRPKwAD7p_4dXK6qfd3Bj4ZiIjQ0-M2uENrCvvGWOAr3FywwF7doXKRTsDGpuQfgAmYnKPVEQp5dAEhaMUNlF03Gf4ttiz-jKq13xzH_o3Y9yhBviD5DR0zcckfnSm-XzDQRWWQkHnH_BlieDNLpGoasqwchHzEGQJ4E_7UTGckPpWBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی؛ توقف نا امید کننده یاران کریس رونالدو درگام‌نخست مقابل یاران گائل کاکوتا.
🇨🇩
کنگو
1️⃣
-
1️⃣
پرتغال
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/23713" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euuuQyDwcQX7zlxN53Dvn7nqbqJvQrsdheug2rI_K0imWh2WYee9cS8sBuQ5yiTYMJn0ReI44wM-TspzUkHSuX2jhDZvetxb-6BaddVesVA_VlnKXTZi_pcrz-e_ECe6m99M3LWPrNwotDZKCswLRAIEhSqiV_gP6OQeDhF9jwdDEEX8j9X9UKUdmIAHrBJw7bz2iK1eHN23JbVYujJ-v3Dzxf7T-prCCrODp_VrfeqzaaOykbaF5iOo9x85_1qiQjv7Km8qK9sBkkwjYrNltQSqD7wC0_tgKOG__oPiyvP28Z1QZzJMJUU4gNnj9rvldz_u0eFUSM-KeZ8M-XWltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باگلزنی‌برابر پرتغال، یوان ویسا اولین گل تاریخ کنگو در جام جهانی را بثمر رساند. این نخستین بار از جام جهانی ۲۰۰۶ است‌که‌اولین‌گل تاریخ یک کشور در جام جهانی توسط بازیکنی از لیگ برتر به ثمر می‌رسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/23712" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lR-_mXngr3SxskxKd18u0xKy4oa0lmmAIausG8d0yZ2VmgcVrwGaJdkzB69-WXzjI4wWRZwR8qPvqCXH8IBQ2TqOKCsruVuR1TEVhSzI8bgpN-2nIGW5-oGYi7XByeKLEbUt-8WhecmDp2cqEovg1ItuUio47WSx-5BUVJ7g1W5hIrYCT5QXOflyiG9gd7Zo_Wu44mI7bSrFGNHhx9RrQ4GigFpHa8DIq9W_y-SmO1xzZryNRLiMystGTemVmE_ykV4bpbv_VHsJpuyQfIkZ8e8z3W3qzmX7yrKww5fGoPGWJjlUI9ww8HjZGPyAeci6IS2Y4TpjBYy-AK21BbLZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bzys081Aqfq_Jy5od3YH0z0FzhA-WNAUn-47u5rAp4WfA2_Zqb2JvQP4gQEhiuzDsErYyGN1aPN4A1aRT49mNrwpCAzo5q7NTTN6xEYfAJoQv4bzYKFwm8YblTRLK9t-yN645TV4tgkQsJ3GDUPJMNTwAm2EeJlLKzN8809bI2qKHkBNcYg0fOTfoI-8ukvCEC3xpiE-2SWxJdEFeVsf1VtQQYQeFaRBOxhpTzbxDYfD8XWB16okAOdIBfRwVgoI-bYRDfgl8bdjs1lYjtEIdMfr_P7yDt8hz0QymII6IMB0toeTEBcV5eTiF0fGxst-Fj5kdZ4szRsu6tseKKFMsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/23710" target="_blank">📅 22:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Mb4JZksCo-9wRixBnJ6VJURPHh-OVL20_o53ekGmZnYhBwXyIEDYVP3NptgH7Kbb8Jid8ddFI4IZkZEIYH8zITklV-aBx1odZ5I25OKPHbFs3zWvK9Bu-Dysxp8O-VdsPN38rAvKcEuj0fo1ZXEVUdibs9Z13xFmxirMM5B0Lcs7Znfyfq-g2TTQ5nnntfxiEgLfqSJ0374qhCKx9Ts2-9I9UihwNNQddOvAIA5NX1KaoibEGgIAMMvbFhprA9hq_YmvALrnuUa1QCmAVbvCwcgrdariJIPHRiQjQzgCW3_jMvZR4pVd9kJw6gL_4ZfANERSYVxzZbZzJunNq9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
رگی لوشکیا هافبک‌آلبانیایی‌ساعتی قبل با صدور رضایت‌ نامه توسط باشگاه مبدأ به تراکتور پیوست. ارزش او در مارکت 400 هزار دلاره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/23709" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Syonq7zymS4ehoMgebP_3xusXEc4h0Q93vgIV7hd-tS_a1vK-VaGMqyw1NTmRpV1WTWwDurclWTGz7hZMRGx7tlGVtyVaIw1efBr6m2TlnoMKSRcuq8zpkKvHvuGQBmCKEmdwAYhHUSJA3V2ij_q59ooBnnmM0NOlTDrU7x_nQNa_Pwbz4KVxPdf1e-oTmJHK1-K29lQJyP0RSFYF8h_AtzxRLbsRb573T_NpS8enhgBidVgLlSmxZEMmDcPgjlzbIwrRwqf81Kbt7MDawIUiA5h0B9CAHlLEfS74lyxz-j1zpFlRIRwVummJIvm2avpuAqxs2kVkfqJOJog54knGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/23708" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaRS39G5h3S1AvA867v5gCWGJurjInEqw93YyQbhd7kU2FE4K4pHvLSMSslsZBSNIrW18q-PsNDFB0wa2vzGyPeV7-t3Y2MLK1keiNncX3AnqLCtTH1BYSVDyUerjmlAiRTXSnhrzMZDvHqtY3RE3iXfPg5jkCfYu1e-30Eqsr_zSJa3edtFGCC9pkLPaFW_eNHpcRbf9WdLshs62nvmfvMluschPTjwuUE_mWeg9BQMJE4SYapS4wJXQ2uUKOoHgJGfhkSK1LBrNqvpU0waySN8v_7EvU6LxDkAd5tce-b4r-3AkqD0RLtXMY3-v0HUJSmidfHb15CO0XJT6-wA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/23707" target="_blank">📅 21:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbfaW6H7YWLHWeZQBNZsVo3WteF_IU_0ByEztxNSG5wc0Wc7OgKeo3m4hCB8cFKkC4Lnfyxl6EzqKj3n5VoBlRNlugEAF1JV4rxXppI8vrpXfSJqHSP1GexgHbOpWZNq6gTPDEwc7Vh29dqdTJyON1se24QC6zoK3c72OZl-Bv33ffAOIxMj34MhnGuDRbC_IN2g2_2gjhlXiBp10u_hWvEd2EAvovlmuixsaSa1HPPhqgwHdTHUJZtcZJu33nJ_4smcK4_b-rHIqmkwZeuSHgVzLJ-QAeJuw7-OmhB1z48hJEjSjObEaAYKAxMoVmmmjvC9zqdOs1uCTZnOW0dmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/23706" target="_blank">📅 21:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa7mX2bITL6Nd3C3J-DCS5vHs691eQAQ3qlWE7NPtROfQZ1XIm3MIABuXqMdnuRV-mxrHmZSM-tGjGvPss9jlAZz6FsyISqxS4rhzabHgxJz204t7i3pCLTkvL8XX0h7FrF3412P3F7_T2291sGG0wOzP2JkXzhldzebk3fT_jERpkMrcZYKRNuornGEWhZMUz8g15lrNhbPZv49GjczK0eQ-dDKuWAZdFQ9p80K3Pl9rrYMbJxctX0oiJHt8dGZJuZMBlm1CIGEUDfNav6RR_UrUoRnZHNzwN_Ta2Q93eXLdh83b--oELZNX8cE5EC-eERhavGvIFzH9c6_LPD17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/23705" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDprcrPkt13CcdzsfOEcctL-dAkFVGleVqWsxQc7IbxJ7IyierK6LWgLe6J0EaNrgUFcDoQyFHlpL9w_nA7yxMIRI3OaxTB1Mb9LDaMkB1vhE83twCo-ge6vURj7h3RlOtTcgucGpwJWZQNDc9Nfh5Qf5iX90oAFINE1c7AhhvmpbCUuudeUaegVyNozDjBnzterj3vlRx-i3oiytk_BUAZYxIl-lTYo7FEuUw3B4qZ72skKerJtXf05PRd_uANa2aFUVX4J9Zj3166a99CLGAOEGoefyP2ZYy41OzF4mBMuVKPcassKAik0_dkybEx3eXuMKvuYbedMr_ic9Qjg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/23704" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwSXe4L7NIVwcyb4x4-oof2ct5T2cglbSE4BIm0U2rZ8zbMsMrotd_JjdgaN2Jec5PDqE_Dsd5-f-LGBJiEAtGSfgj1outZOjhgW19akhcJBw1LVXGBifm9QGvvx1Dt0CxLOkONhkAGXlx5yHw3mqtdMs9AWcik2f3X9IstSFdZXQFDjWRCsH71DKKp1KLRJD4-6gFHzADVXulXlgkRECOVwhJxNaRH8WLj93aHJMbWz1D2-1ojC--jWjzJKrB5ujaIB3zKgq2DmU145R9Q3hYeCGA9IlbRlNZk-zcJTPkACoj9obiZ3pngNb26FehTppnoIBWYKRTeUP3O94QBzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/23703" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_G0dJt6PHz3pNmsOY6mHQyKjsEGIF_i9in__j3PpJ0WiZfNb3m0NrgZ7JVXv4eCi1hr_VjqufHyhOAgVlFALi1DCmirS0k_q2j9Kq_XpHwttH2Bq76Frs6Rh65dI4U6yrYC7mn57029rTbLduZ1R05AGVT_M1YjhOgiV6JwFY4Ma-r_ceL1bHV0zoMhUG9UzdPnwCfXpLdIdIHQ0GBDky4ZMWWJq7DHqCA9eNWlhdWgwlrwCTkd1WJr2lDEsn1Fs9CPITxpi5NpSBf-h3OVac4uGtrVtYm1WJs9pW6_lOk1WV_6GfgHVE2IpUVvLmIxe-81PHzITbnkERxrSpmzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23702" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyO7Y98tLjDP48s_qGd61MTty7eCF5rFhi5hQo0aTVh2CmV1q0BwvaMibkiQ7flyn2UWHl6zKCa9WjBsYQdbNlH8CaWypts2WMtXGwAJykOXJ_UHq4tZvT8-bH5da-VWv9vIOsRcIAxODXX-lEO2yWqP92ycHoJpmZyv5AxB8XWebg9rDyqgrCtGCGllPGlGckEFOtAdpM3XYIO-OBI3XRdEN8XkGHGgZwGixEAGHVyaXCVrHOLlKSiU2t-1qGql2vozdUyb9G2pmQxfH5hYBYASaiL36d9hi5EHeg8t_TyVrh90YitlDMJA6hTMqyhXDeVwa0IcE8Q6PAB6dMBtyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/23701" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKUlg2jk1xuvWkBe_GzdXjd0YVfhSkOVf9Mg4QFwQHMscTO7222z11KMu_3LuOC_my-dV-Cy42C8yw6D3maTCk0k0Pt-7wFG_rMer39xDeXx5b-_uEFtX1aWfItMkRbq9NJZO2rQqq6MArihDGySN1sLYcN9nj3yCuPurhF1TCR4GtU1RyCUswmNd_wa9tZfji4sLOR1TVHNuE94KWfOd1Y6azKMPxrlrIYJ6jZDrSUgXwbUvQYLZbHQJ1x2VP4JXjoAG4qu95b3SfQVUzJ22mhJRVLLtaaawK5zH33xRXAUVQLQl3NcfAkVFUIGgNUpHEwImBef1PIF3ktEm9OXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/23700" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23699">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlLtgN1mWu1E17iFKdT3Hp60T_g7g1FPwPRRA7jDivHkowAMr2SJBAFiSpuWNsFcq8lG0dYbuP_Bn_L8NOvsAdRbvHlKIJS680JsenpOcKlAXBFVhu3o2i0m9VHGPEwSzIfKZa5vzXGYxpGc-uSeoonB0bWT6YSyhLwQyQn7__HIOSS0z9rFYA6GYBZBV92HOx2pBAh2Tzj2aTHDwUA_Xsxs-OANlCFlUEb0wgdsG2iSKuNCsul2IGmNhX0x8x8csPJWyr1kFSzst9BzMisWcN0YC8GBzyKwfIg85OfLWOKIY0kAxpQZeM2SwiLQeYojDJmuvqeMtWALp99xFF1-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/23699" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gc7_O53pU1HNlwKDlmhdLQYZhQkQl6mBiuq8GYIwUGi1uyD0MIGykEhIMlKgVdtASrN8gS9z2-M_wjU0Evq31Cgq6r6w1Igj3FjpocmkK_IZFJS3dE-cqM7FplCWkkCaNlHor-DSoNdv6tC7ZDuyZ5iwvlE2gYwOjsqtfHRqielvUU3dUTf55Jkpe1hiWJOyr6Ebtu5adp3uHChEJj_qt5epbxIQteo-7VQ3h0qIwKcfXS2ZPtebGJbjy_uO0gGtkqMNeXFm-juzvl-_RfT6kcQewZPA5K9TG1CT4v-FLITRARxrktEHAswKZoiBmSLbAGOV4AbRiw-EdZO6mW9D5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiRga2NFLR3n3s4jwgASyUUrXYMDNtb5pD8NYcH7TVFINmPiqbVOQcSZNAgWjF1L888HYnN7_nNvkrCSuaZ0PRUMisUxUH3dcPUXYsj3RCHa2ezPzXHKLr526T2zjVx3M296S2dAg777KC056ygBHP0ccDY6DSeAEjf8aXFYu1Um85y-nO7LpXa_PX1uG7ooll_LhXQoLzYB28Y6FsAMbQ24-YpTcQeZOwqkyN90uRLnKef25jSXR6AG-lVStSB43hWwcRTICWNGGhh7GIFuZBMCBMaeVHHwUdYLzY_Xjsj6tz3EmbVBW9AgAPDKVpASp9UXSIAsOJSIDhSqgyuH5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23697" target="_blank">📅 19:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7cgx146aSqW5CGX8K2yFfIh7ljXVX5WVd72hwAB_Z_hGVCZVMc4zdR7qdcbS5VkPTeFpODVgZKYtmKPfscpMM1gmQLUOmNtPOIbaKV_o9p0ixFtNHu-nLhy8UI8-LgxWZvk1wqcMkxlw7-1YUZowWLQztjYNa_nAb3c9JKHcnMDeJHMfZP7wJ-UYy4x2xtx0ii7Us46UMvpBmV7PSAd_ascPogzNQFpMb2PCEXNzw8K4cKk83D3k867w3AMmg4ITqlCOuPX-orRc_FKyWjrthSTxRSBD_txP3-FJcRhCV8wJfnn7Ss3XKuHVc85XHU7VB3PPiBaZziDIZw0_YHFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو سرمربی رئال مادرید از فلورنتینو پرز خواسته از بین ماتئوس فرناندز و انزو فرناندز دوستاره‌پرتغال و آرژانتین یکی‌رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23696" target="_blank">📅 18:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kikyCmlcmApVOiizq0S9jn8kOS6Zo9mo4YKQcLIr-Qf0aPkkwnAhycMYl7-5Zt8_p4em-fRFhfWGJnhihKKT-Jrc0R8qGoFwbtMyeSoqu5kcvNnXMFNgLf3BDo_PZGGZacEh5qcEuKQUMzQZyYtV29BMHljgaJySMyDwD4ZtI2Bed4MhCY0clHNyZ6roJ3FNzs3oOMUs9dMYmTOfnwmFVa2FNDS45IG1bqij6wJ0MSYehL5028jl1prRhzo7SDKJMjcB5y8cK1rZiMS8SvU2cGPifr2OGtkOY5O0nryHvYxLuSyI8rNICCgdD_36uslmX2Dj_pgrbjUWTSoPi3oUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23695" target="_blank">📅 18:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJBvwqKKs3ydMKaGxeP92e3jKcSia59xXiHQ9XGTWgcZEwCaln2wnrIWyxOcsBzOxRm9g_A5ZbqSaAw5XqXU0wOa6roddvFYiDfGW_GmSvi1RIaQw58yOSowNVBdFBq-40vmllO5_0DhcL_NdshyGJFN-TF5g93aTPd57ZveLGIxJmdkqWpDZHvgO6IBgkro5-bG52pvxcqrrmmQVojF1sKsJx_N77LXU_pEN0hQd6RGyc2DvyHqtBXLDq0jC3WwVuudqbMbFJrqDF-x7i9dfKom8g4qP-jN8oit60cMirdnenj1ZBHH8KZen9Hlm_J2L2Xl_LknfPUSm1P-JJ9WlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام ژابی الونسو؛ دنی سبایوس در رئال موندنی‌شد و او این‌پنجره‌کهکشانی‌هارو ترک نخواهد کرد. همچنین رودریگو پس‌از کش‌وقوس‌های فراوان به این نتیجه رسید که در باشگاه رئال مادرید بموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/23694" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7iYPKChN3ufJxcnseHY6vwkg-LGHyhGJX1XF0yMZcfckHvonpyG27MoSJRmOi-OTkHs4ehqCPkHnDVtdZRczXN16DSfax7-yS--hKYyH7Ir8J5mpu3RTXbPS10I-hIuVNSdJDtR5dCMvyGn74-kKensE1oYjtkvrisZqmCjUq_6CrBIu3fyJN1THRmpdhfRrALYmMq0qsbacuozc2fOIAOUwEZsyathKdCmpNPJoN3ItF3IzrdRBwzy3PpZSbjhktT_R2GmbLmQPeL8Gmlu0YTNIqZoJXgTKJhL5sNepbId4fkan5uPE_X2lE5bzCjjM5N7k8YvNxA8zOOEd_u8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام باشگاه خیبر خرم آباد؛ سید مهدی رحمتی سرمربی موفق‌فصل‌گذشته این‌باشگاه رسما از جمع لر تباران خرم آباد جدا شد. به احتمال فراوان فراز کمالوند سرمربی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/23693" target="_blank">📅 18:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=J60lzj3R4kAH9rBXIEjtCP5A0IeyuOF17ynsbEgSou4yutukDh6tvtzrMQU-oRjL4GgKltuNGd32oZNp2pFt1iDdlqj6MLm1gpRmx5NLpuNbjT57KKJDc_E0AZW40Mo5dSJQ26fNgxQMP_XuvBxM_S_VMgWmMLslb9UwSP628hbIl0M8z56AK-2jwXjNLTffvBbhc6MJ15CgPflWbsbwE6MzkDS86JUgsbEU4yvRpn_q2Fv4Gd5va_0_4ewWGXxF44NQ8-bEPi3AUPEYu8E2VL3TgOf_zbyVxr3hkVZ5afpInG8IPHwcOv4_LuXiOYZBbD_NUEC-l_D7lPm6WiBzGrQuaBaRMyGviSVG7Sek-ZtvYx4AUi78KKGKfV3cTWyk-oYjFHHanJg5k6MY9kIT31pIplHI-HinkZBi3ng66RzK8IuLrOQ6W8bZ1i0oUlk4n0lmEbxpT6u7wCEoOD1TG4qb45kdcEnke-VE_XZYDVDyh7-cnaDxCKTcFqENgd51mgBxdmaYr-d1qeCb2qNjszxqHUBl3Rd1FVMIJIExh4WLtuIaIwxsacegZfsA3pdoCtPLOqLR80x6W_aFKjSfH-sdSHmoNC_a0mFy4r0g0XQljPIa1-x1RZtLaKUTqRDkGnMtZ1X85Gsydw6yOBWG2mJ9cIVs2kCxDGBhORCk4ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=J60lzj3R4kAH9rBXIEjtCP5A0IeyuOF17ynsbEgSou4yutukDh6tvtzrMQU-oRjL4GgKltuNGd32oZNp2pFt1iDdlqj6MLm1gpRmx5NLpuNbjT57KKJDc_E0AZW40Mo5dSJQ26fNgxQMP_XuvBxM_S_VMgWmMLslb9UwSP628hbIl0M8z56AK-2jwXjNLTffvBbhc6MJ15CgPflWbsbwE6MzkDS86JUgsbEU4yvRpn_q2Fv4Gd5va_0_4ewWGXxF44NQ8-bEPi3AUPEYu8E2VL3TgOf_zbyVxr3hkVZ5afpInG8IPHwcOv4_LuXiOYZBbD_NUEC-l_D7lPm6WiBzGrQuaBaRMyGviSVG7Sek-ZtvYx4AUi78KKGKfV3cTWyk-oYjFHHanJg5k6MY9kIT31pIplHI-HinkZBi3ng66RzK8IuLrOQ6W8bZ1i0oUlk4n0lmEbxpT6u7wCEoOD1TG4qb45kdcEnke-VE_XZYDVDyh7-cnaDxCKTcFqENgd51mgBxdmaYr-d1qeCb2qNjszxqHUBl3Rd1FVMIJIExh4WLtuIaIwxsacegZfsA3pdoCtPLOqLR80x6W_aFKjSfH-sdSHmoNC_a0mFy4r0g0XQljPIa1-x1RZtLaKUTqRDkGnMtZ1X85Gsydw6yOBWG2mJ9cIVs2kCxDGBhORCk4ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌سنگین‌پیروزقربانی به کادر فنی ایران:
من‌ نیوزیلند رو راحت با فجر سپاسی می‌بردم. نیوزیلند اگه درلیگ 16 تیمی ما بود جزو چهارتای آخر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23692" target="_blank">📅 17:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3g5tTsG3FwGNXsXxI6GedsKqUObp-NLB2qH6mXqaV-iMF30DAmMTe70evLE3aVAT8J_kNL_eSAcRhr4G-E8lJ1KulQVZ9IlIs-LgM6dcgVFEcxLnSOz5DXhF1sB3gaOqWtNbHevCWcsePqcrcEb81rxukLlN5yMlR_MAMYx5wv__M81j9h6MXILlAvUPFydM2_v0mdc5THUSfaumd63lQ-jO3fM98Vbi228lBNCPnERLtJfGVdgZUMnZ17G5h1e8Nkp9wGXSChoYfMPK_7u2lAnKCD1m_3rK5hakRNxW16IkCaUxDbyZDDBPC_K2VFLZynM0j-YED1MIDvA-Ux0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwU4cjART5r3abPozbcm9Gh57FAu_xcV2FiVEe2xhn98W8cLW-C_ygCz8Whbv94-z4pCfSou15dY2x5RbgmCq3tPUtWYK7HvKDZBiJ_OsicjRgKdQ1cdfrGwaMMGnLgoFZA6TddWHaT_YnjWsC3DXf5MT6FOTl3dCRz4khqPURfowfFRZtrgcJCGfsGxaGzmqStO5lF8KOn4EzQmb5qNCNORDlPb65g-3kzHKGOUmKvHjyleC71k85cab86q0lGmf7ztxcJA9Ae9bX0qWiia-WKucgDiwBXFlXBnT_Mjkamn6mcwag2zRUfI-RkGqLvWztGlfsREWDJF31V_GLCOaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/23690" target="_blank">📅 17:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkDVtjo9C8-Nfvo1XyNaa-lLqUMBHoO1v7Df_dTDPjKZJtJtugwmDd5gDsL9p79vt6XsqrK9LhXFm4A84kvpUm9e1e1etO_JzuTpQ-ILmNHDgpq8KlLm0ALlB3Yn3RHThV1HQn4dX7vSXF-9dplIznpSsBQZRn4FZnzY6OdFxUgHpXKigU_HEu8lg7CMSwzTgl2Yd1h5BuU5LmrhuwhKvs0aVHUKZ0byGao9MNCReHIAa8JtuwpBNoT6UN28RrxgdAtE8VinIB5EfOaJ71AI5ocm1JoQ1a4kUqxzhTXFYLNnhR05XiTb7l0xYGJ8wLmH-kPCoR9emPOF2WSNmelzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23687" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012fc50185.mp4?token=Lu8DGiAi_n-dGXBcM8Vhz3rlhTCZKudJEX9HRCX5RHP1lH7OVGj1eSetcMF1a1J7QpyoxVkhol0FoMfmv6CSU8ljpMhT67N9xCawAfzhEp-7KyZ8jDDF3wgujPRbt4LFVK1R4BUEjUufLf0Dc3YEkGOX6CUbd6XKyW8bm6Y6ziGAi3UzOrZ6HG4l5AkyjvqQznlLL6dr1zNezxPtAgiVZBIxRYQvI1ooicqpwRM29FxkO1tBoR1-PDpCS69rMIvJmUjopq_iDmOx8Iq2a046CIMODK889IVgicVp5lvhhrHdcRd9yIyvJhiNL67l8_OsBbrVRcTXFPhiBV68QJ6heQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012fc50185.mp4?token=Lu8DGiAi_n-dGXBcM8Vhz3rlhTCZKudJEX9HRCX5RHP1lH7OVGj1eSetcMF1a1J7QpyoxVkhol0FoMfmv6CSU8ljpMhT67N9xCawAfzhEp-7KyZ8jDDF3wgujPRbt4LFVK1R4BUEjUufLf0Dc3YEkGOX6CUbd6XKyW8bm6Y6ziGAi3UzOrZ6HG4l5AkyjvqQznlLL6dr1zNezxPtAgiVZBIxRYQvI1ooicqpwRM29FxkO1tBoR1-PDpCS69rMIvJmUjopq_iDmOx8Iq2a046CIMODK889IVgicVp5lvhhrHdcRd9yIyvJhiNL67l8_OsBbrVRcTXFPhiBV68QJ6heQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خداداد عزیزی سرپرست‌جدید تیم پرسپولیس:
من اینجا روزی چندین‌بار از حرف های جواد خیابانی هنگ میکنم. بعضا وقتا اصلا نمیفهمم چی میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23686" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5ElHqSXdAZlKe8HYKLQ0JBacCu2A05rGDXv3PWZsG266cX7OlhbkMf2j7EuuuAPYNNiReROvuVwN5JAM33ihvcCdJVeIM63s3mG8qYGlpAcLHtlXvOxDTq7CyuuVunJ6FCbSGwbxYj2iA4LqOXh7dpyFpgvpNXCl5aTkrCFmPFBOEST0yUk4mN8EOhcRpgvNePTK2nXjHmgsIIf6XUjijgubSq7eY9spcVv48sEdirsN2otvK8vE5XxWZl_s_kQ9kRRf2zS4Fh_Qyxy5emSaaji0qyC3cg21KGrtFWu6NYGOhpVM74zRkPfftxKkQKonkLYbzY5jQrGPW0H7JEohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23685" target="_blank">📅 16:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=XSew11GBwcawSx-jpbo02KSp3xicn7ZfGkOzfLrs2mMZ8kaiWcJrO6hJ4Cy2c9xqfw9bdaHeXWObhV85Rr_EZLBYKOA1lu6YD-l3P6v2dza4uvoHzS-vaTBfjRIZHMIi5QXWhIok83bp4XtwdHUDpdzl5fNaw7GgNl9Jmgh3q1pIQz1r0wejscNi5siFlFG1bMNDk6jxPxWFZtJbW7pvHTgzjAkIglbNCS1k5BhEGrl2ciPEijUU9WZrPl45_tLVPzqfmP22GnMjC12VHSiB51-bmnlpiFQXm9_wpttDE8QH6m1zuwcEEbRzR7zmKWSX8WwhOdFQN_vvOt8yeLURFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=XSew11GBwcawSx-jpbo02KSp3xicn7ZfGkOzfLrs2mMZ8kaiWcJrO6hJ4Cy2c9xqfw9bdaHeXWObhV85Rr_EZLBYKOA1lu6YD-l3P6v2dza4uvoHzS-vaTBfjRIZHMIi5QXWhIok83bp4XtwdHUDpdzl5fNaw7GgNl9Jmgh3q1pIQz1r0wejscNi5siFlFG1bMNDk6jxPxWFZtJbW7pvHTgzjAkIglbNCS1k5BhEGrl2ciPEijUU9WZrPl45_tLVPzqfmP22GnMjC12VHSiB51-bmnlpiFQXm9_wpttDE8QH6m1zuwcEEbRzR7zmKWSX8WwhOdFQN_vvOt8yeLURFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇶
#تکمیلی؛ آیمن حسین مهاجم تیم ملی عراق پس از ورود به‌آمریکا توسط‌پلیس دستگیر شد و بعدِ حدود هشت ساعت بازجویی آزاد شد. اتهاماتی مانند همکاری با حشدالشعبی باعث دستگیری او شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23684" target="_blank">📅 16:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34750719a.mp4?token=HiDPrEPjpLlfeoYlcaafOLd4G8CnhxImLVhHCoXmIfcHaOhvCIvOu3Xnlqw1RJ6vJ6pkUCxUI1YEsz289SABpdYm5LluLvP3FaYfN99sVLxrgB4_ZVSJdy-LBbOJnb_7W8PBAIpmCKWfzdXLOTxsNfT3ux2QKp3QrBJEKg_W7qKX0o36SglKmNZ50vRNPXuGaukmJh-1030NGSsuUwttpU47YolzGweogp0mWy4jg8S4z9TqoiGcA70x4Pn7IysezwJcrrxCKhQ0E4zPEYIPm-zS8eslIvQZoamCkTBzlMshJynjdFkbsK5g_QEZioW0NhPuQY2DKA8QxlQ7RpwGd5xsEAOFr8cLMKaCudT7goAkQ_2Cu7S5AF_Qu9ork40JpGmk4VsI26Tx-4G74MI3ocIj-ax4IhJTa4M0AT_4U6BjNc9BCO9nHMsoEIOT4QKC1htUStNcQP4oVObwc_rmSCt1YF6QzlfsO0k3tukD5o6Vvd90Hi05-HQeUrVyD2C1Wm8OeEmImwvEAJrn_RPoxTve2fO-9_2PFacY3VXwMTVZmrddam1xvnzYbyNnPCMHy_2j37bvIRPhTlXn39gFTpiUgTLJvelB1U1Ylcj1uINuTHBpVh32YHFPGPqwt6YsW7_erMtYO3MG58BJCwg7A2JLCQmekK1fVpcdzKetLFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34750719a.mp4?token=HiDPrEPjpLlfeoYlcaafOLd4G8CnhxImLVhHCoXmIfcHaOhvCIvOu3Xnlqw1RJ6vJ6pkUCxUI1YEsz289SABpdYm5LluLvP3FaYfN99sVLxrgB4_ZVSJdy-LBbOJnb_7W8PBAIpmCKWfzdXLOTxsNfT3ux2QKp3QrBJEKg_W7qKX0o36SglKmNZ50vRNPXuGaukmJh-1030NGSsuUwttpU47YolzGweogp0mWy4jg8S4z9TqoiGcA70x4Pn7IysezwJcrrxCKhQ0E4zPEYIPm-zS8eslIvQZoamCkTBzlMshJynjdFkbsK5g_QEZioW0NhPuQY2DKA8QxlQ7RpwGd5xsEAOFr8cLMKaCudT7goAkQ_2Cu7S5AF_Qu9ork40JpGmk4VsI26Tx-4G74MI3ocIj-ax4IhJTa4M0AT_4U6BjNc9BCO9nHMsoEIOT4QKC1htUStNcQP4oVObwc_rmSCt1YF6QzlfsO0k3tukD5o6Vvd90Hi05-HQeUrVyD2C1Wm8OeEmImwvEAJrn_RPoxTve2fO-9_2PFacY3VXwMTVZmrddam1xvnzYbyNnPCMHy_2j37bvIRPhTlXn39gFTpiUgTLJvelB1U1Ylcj1uINuTHBpVh32YHFPGPqwt6YsW7_erMtYO3MG58BJCwg7A2JLCQmekK1fVpcdzKetLFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:
که اول نظرش رو تغییرنداد و پنالتی‌نگرفت. دوم اینکه آوانتاژ داد و باعث شد کیلیان امباپه اون سوپرگل دیدنی رو بزنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23683" target="_blank">📅 15:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=vQvSn5b758J3-H5O077WT1Cz4gEZovSeqSIKIKr5w8UQrvRJAiXZUmQVgmA3twVxiMNB90C2wk0U8xZ-5fYBptSdNarmVhs1mvKsWlGiE2DULz4-SF1aUjWe01ykH5Vg-U0Yp9x2HQ9BhB2EzlJ9ANUmBfaGIAlNL-ygr6H69ObRm8yn3mNwIVP7S141_zIQRNgUTSiQU0D_WU61MKmeCl3vkpNAZSd7VZ7_M3st8PXdh7IVx3ul1KIDhd9raztS96iZOBEQN4xHEewLt7dh9jb5cmbYBSFfMFp9vWCAmPMzYs_sn1EsdhSUsRlZUjc_Px-J3ycJfpj1nCGojox9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=vQvSn5b758J3-H5O077WT1Cz4gEZovSeqSIKIKr5w8UQrvRJAiXZUmQVgmA3twVxiMNB90C2wk0U8xZ-5fYBptSdNarmVhs1mvKsWlGiE2DULz4-SF1aUjWe01ykH5Vg-U0Yp9x2HQ9BhB2EzlJ9ANUmBfaGIAlNL-ygr6H69ObRm8yn3mNwIVP7S141_zIQRNgUTSiQU0D_WU61MKmeCl3vkpNAZSd7VZ7_M3st8PXdh7IVx3ul1KIDhd9raztS96iZOBEQN4xHEewLt7dh9jb5cmbYBSFfMFp9vWCAmPMzYs_sn1EsdhSUsRlZUjc_Px-J3ycJfpj1nCGojox9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
#فکت
؛ تعدادگل‌‌های دو شخص حاضر در این تصویر درتاریخ رقابت‌های جام جهانی رسما برابر شد و حتی ممکنه سمت‌چپیه از سمت راستیه جلو بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23682" target="_blank">📅 15:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx-yHtzyU0118UlELMNjPu4BdHndZULQWcwSwLfq_LKfWlfJ33HTozyG_DHFzvOT4LhkuYj8RRTef0zdHJg8FoPCTFqSF1xwxjOBa5i8CW_SWQt_5wzN812vKh70TfQZV0Elzv3qd9Fjc63UgS5ZdqEUzJcSojAa4MNiUJNh34BEA65B5CPhr1nu8atMuwYgwYr9lA9PGud0xD6v1u8vWX7bG2FbOUY05kEVy1ZBN0LBWzGH-3UDW8Vhu-0_zDrsdUr70X_vgDkm-M1KhFBjknF4XgSJvJ53CCIlM0b08Gl21g6ppp-iiom3Y-qQ19CK4K6jZMuu0df9BCAmhC5WCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام 120 گل لئو مسی باپیراهن‌آرزانتین در بازی‌ های ملی مقابل تیم‌های ملی چه کشورهایی بوده؟
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23681" target="_blank">📅 15:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqv1izsHNzgvRbTSWR_sTuHYsMnQYNfJEFMRr6fYPUS_r-FfPD3sVOdaBCor1ItShdxF2M18D16zvYggKcdSZ7vDCZE4sl9cEV_U6Gb6xpBs8wyhqWG7uZzYPzB9WgtkqQ0NFYXTToKFPXqy_6TRqvnq7_I2K8Md5gO2XXVARdXBvvI91XVkOcnVh6syvTJRV6WVU1PS_arNdu4hiDEJ5dd3vavfA8T51SpVfykgNA5sP7_Ih0umpXx40BTL8Kv4nGhGMvjVT712vD7dQhk4ejdqWHIuURBlLMI8fVm2Abmk--GQb7x5PUeQ-FnIsZ8baopVPhv1cDuoawj6ItZsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل پین قرارداد یک‌سالش با سپاهان به پایان رسید و رسما مربی آزاد شد. مدیریت استقلال او رو به سهراب‌بختیاری‌زاده‌پیشنهاد داده‌اند تا درصورتیکه سرمربی آبی‌هاپاسخ مثبت بدهد با او قرارداد ببندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23680" target="_blank">📅 15:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmD4Ob2h-J4nBlCa3OtSXUG3pQOi9NCsGzlr24S-XwVxrhTiGStJp_TxZNaxFbAPI8vBG5RvHXeR1fxSTrbzZ12Qw6xxQ8pKguZPsrlOpsMT1M2gVKXtTOc5aHVtV4-Rn0JEmXjtCXN2Gs_Xsdr3lW_XTbezc4grC4JDXwtWcJVONO6LqlJb2N2blJBE1hWNh8phFQvWvVyenG6HgM9ZI-CPCDWEPOW5whyhOXeV8Y_kMOZvwkPLzWUaF0FaoyToagB3XjExxOxsQwRIMhhuto_lVN04PB5qn4BJTifwJ5z6K5PnE14JiRArT1scafTeT3c3E1UlCHRMaiGDWpkuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23679" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-JpyHRxjBd_unikAcuWk3STnXH5Ut8OOEC9eL6KedhPXpjN_94ucji67yQqiccS1g3F1BPRrNgrnhnZLCOUw62kYczFrUyvGhydzbE4Vk5HaPlvhpH1jNjbkxEuglzktxB6kPb2R4PNyK0PSiW444sUPeqnm6sAxTduYQwtjT2_gEIQRmkUD8Se1vuY_sfmx_MG2bZbm2J_g-qirpFAWw28gaMa65__3oLdC52cBnJ5gxJC1YTW3yaZo7kSdZHBKrBnoMINpNr2wDJJ-ps86NhxJxLeZZGuwophRjAe1cNR5RqkrdGVi00VfTMB7Ghcdcm_YRjHEa1eSIZIKw9RQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23678" target="_blank">📅 14:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G07OH1JslLkXl-wnPHAzmmuhgrGiLy_JmA9Bf8IUlS-4Sdyg7VO-KNs-RNyrrIhROWWdLekLWxu4Pk102JAjxX3bqss7I0t1P-ur09flvTYjJsjQ4qRXTlzFDdBkW8ghFoQa4M3BhNJjyZSo7NDMLnaPsf1AtJ5FtYu6Z4_nsUrKTzYprLMsDdSmjFNwuP9wJOFlRkfFYrmpsKOek_tfaQYgZcfdJXxTzZfDfRvg7oeBJFrCHMkV_sFu51pCzZB5wVYfZp4VN3xYPt1vUyloKnxoUPTnhuFLYtRwOVCcEzrqyiK4EDGsmQS4NmSyTpM2_Gn3osMz9OgNvw0ue6jSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23677" target="_blank">📅 14:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK6am3OX09ylRbqnt_7V3mE146s_nhUC7fvu00IsCS0G5l52KUTKEJsw5XOPzC6b_eq_jW5eqm33Mp8upp9mpxFs84jrt7LI1F0-U8Vhb02omTZJgQ_qx228Sm16Gt2fdUGANW8hpH4eENn5d3AHj0psLqPX3CgplNrXt6g_SANMt4-1Ed7fvmm54N0RumgLxxIlKflKxhe-VpoV6jiEw0pVuz9efBrpJPxnqHZnIACPNLTSLnpgxM7NHcb-4-TnuHZTwDpCPM3tGVptTx6xPM_W5fx-LTG4AhK_65oJt5ygw9qmdiCguy2EZ544Dq7gmo8uYURJ0bCF5iYo4H3NIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23676" target="_blank">📅 13:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=gFBijo2WN7EoIAgF5iEVYXoCSwmsACVft0EX3eBaHQUVN4xMUPnjAbWSodY3KnrIaGIlPY9LojpC6vW4a1SNBhqVnzX8Sjx48_izeFbYx1buNPTVkeEeG13tco7tyM_hB81NzbyNgabd_NlOtJMHZMR60aPuRCOmENOR6T6WRnxPk-tFYzI6Z-T9UqHRmDq0VBhqxkJ2A_4E48qAy-3LkM6ofn_ZcLx7xfiZ6LimX74hNV46Xo1nDj6ym_uHRgpYZsz4jh11x7az25FeH__6i3s9XJl0aHGBN7xGG5nsNkynDswZ3jlhe0OPGudmNmsjR9gMMaIeWFd-PlAPfcKyuy5R11GhdJn7vrv9RusipE4NgQ-6OUs2MH9hgXkWhC4TV9f2jZOoBGmNmNxc4mQqrtDtnzgIRu04y487rRpKzp0zUh1BbdLftn6d09XeCOey5-ohlMu1iS4KeVjFBb8bYK6N2_u6CNi5LnRJ05NXwHA4tdEFfqj5QawsCpHvNUtfSecg_58I0negoGB8U8MIPv29nc2CyRZHJXrKxDjUif9-rLuGYztQI2CiCj-uVxQcJ_cOLNKBMT6wo4q36_Z5bQ8gWuJOloomCvvnSf_lwnZfbSABV6wL124BVFJ8oEBxm3XeREoTX8uey9EE4tLs-1P6pAEbj72aaFaS2M3hd2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=gFBijo2WN7EoIAgF5iEVYXoCSwmsACVft0EX3eBaHQUVN4xMUPnjAbWSodY3KnrIaGIlPY9LojpC6vW4a1SNBhqVnzX8Sjx48_izeFbYx1buNPTVkeEeG13tco7tyM_hB81NzbyNgabd_NlOtJMHZMR60aPuRCOmENOR6T6WRnxPk-tFYzI6Z-T9UqHRmDq0VBhqxkJ2A_4E48qAy-3LkM6ofn_ZcLx7xfiZ6LimX74hNV46Xo1nDj6ym_uHRgpYZsz4jh11x7az25FeH__6i3s9XJl0aHGBN7xGG5nsNkynDswZ3jlhe0OPGudmNmsjR9gMMaIeWFd-PlAPfcKyuy5R11GhdJn7vrv9RusipE4NgQ-6OUs2MH9hgXkWhC4TV9f2jZOoBGmNmNxc4mQqrtDtnzgIRu04y487rRpKzp0zUh1BbdLftn6d09XeCOey5-ohlMu1iS4KeVjFBb8bYK6N2_u6CNi5LnRJ05NXwHA4tdEFfqj5QawsCpHvNUtfSecg_58I0negoGB8U8MIPv29nc2CyRZHJXrKxDjUif9-rLuGYztQI2CiCj-uVxQcJ_cOLNKBMT6wo4q36_Z5bQ8gWuJOloomCvvnSf_lwnZfbSABV6wL124BVFJ8oEBxm3XeREoTX8uey9EE4tLs-1P6pAEbj72aaFaS2M3hd2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
عملکرد فوق‌العاده و سیو‌های محمد العویس گلر تیم ملی عربستان در بازی مقابل تیم ملی اروگوئه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23675" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYKlNfqUUuxKv9xuFaB8vI3efXx9RI4BwJnn7F-P1_2JG3E8qqWeZi0MBFyBkseNxub1qZv-OYnW_lla5jz6qmrM8jFVWx6hj3wPqorvwPCU7Dpc9tCvRTTiBVqbnCrNSSzDTTMVyMyp5N3bQVy02fOF0PGh8xnGsiJySUYrJ2CMTmQbAXTB7mcoTTzWbmfVbe1mPmjH1x7lq_MVXk7-ebN7npFvwmCHYFhyGeyCBoNeWwg91NMMik8rtYYozQmU3TExU6CMZiUD1pKRJG1XjPmZlZOPVw9TxpemPvT4wzf1zEQKXdIcp5YfMccAoIW3ABA-5_2KSkajjVGgw-xqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23674" target="_blank">📅 13:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzqB_PmpFIrOTlqu2b7xV2utg7ALw7RnjfWXzHR5jOqG1PHXJ-8_5j0hDUz39oEWwFLJA7J8nTZ9jXua5LWSYBeFGY6zX9XpGphYh2pLfncoz0eDnqL6q4d4MjYWy9ieW4ceS_Rh3twDhh7NKWPKX3vmAc8HHnnnxwXe7wHdy3uny0jInala9D_KDQaWotO2iKusJPASJ_xCjWFjkozvyBkNdSbDXI0qXWw8x0eYcaot4nvSwjQuVse7wN81tBj8jlYAZvZYLg1NzbBOW6RwJIDKaGJDX97Mfjkv0hlnuRQYeImlm-7nCPPw_EFhJq3HYP6Tuax2O336LjGOLQc12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
خوزه‌فلیکس‌دیاز:فلورنتینو پرز میدونه برای جذب مایکل اولیسه بایدرقمی بیشتر از 150 میلیون یورو به بایرن مونیخ بدهد تا راضی به فروش این بازیکن شوند و قصد داره همین کار رو نیز بکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23673" target="_blank">📅 12:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF1HQLepWZ6Ph-xJmNNJBCOGzbOWvcrfSHnqAmjGWyINUTktu11BJVlMdex9PDW6fKCkQ5IxLXxGtDJWnlV8JpNxg6wNqDfm0P6MXojtBspSNK3Dxw7iJXrmI65LGAOL6ePjksfehabMsE9FzKnbbh3TtK-WmdmwsBv4FLakjmx1SSXjlUsyf5K50Vvyrl5ExQXKP51XbvgFcri5zzTSd9xBfPeKb6bjneFp7JzYZ-8GaqOOLwjVlX7ZCOlG2aiLQwT2w3ptanIxtTK5JlVniUJQrS1I-Yzyvt7vc2Zz5CF6x1TxHfFarkqy3ZuaeTGv8zPpaqZrL6dg_ekLi7lGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده و باشگاه بزودی پوسترجذبش رومنتشر میکنه. قرارداد ستاره پرتغال با رئال مادرید 2+1 ساله به ثبت رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23672" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23671">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7YxBHB04A1WrMsS6j9swXE82mWl8WoxG4pRc-FtF8bIKt2sO7KQkzqVacN7lPawtsFog7_V2gluRkLpd1fEAkRxSmaCJNVs1rC4LVt7MZ54VSFT7qqVQC5gIPsfXVep37i5nXUWpbrxVqQnFSl3_UxnE6vAR8u3HBPFS1-qfTneHzKEJcsCfL5J4zRwHSQTGCdAY3Je75a_nLBdXUe0PxgBYORy8_9wVpi31mMAajR35TxqWDUKQ7doHrWZnsNDJbBO31HkKHm4l_vDvw3Y5JZozUNIfEczP7k7M3ERYac4u3mxu7UhH8qfgv9d7VN_5PJ0ZZnj92vUwPxHc6h4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌ پیگیری‌‌ های‌ پرشیانا؛ پرسپولیس پیگیر برگردوندن یکی از ستاره های سابق خود شده. امشب اخبار جذابی رو در کانال خواهیم گفت. ساعت 23
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23671" target="_blank">📅 12:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23670">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksFzEOja_yXP1i8Pz2u0JvdNlP1Mgq0KQnYZeH3OWlKij4fHOo24pHFart3-RBNXRfh6hx_-bNsrH0fbjuEuTPd5MB6R2hsDDKO6ogqoSvBXyzhsoAKLxfRbWAyDSwaI6FENcLt6nkE3lzqDLIIQA_12w_hbEZVevWuM5X6O6gNMs1MT7nr0OM9bxpwJPOAQpwzQ38PJ1ak2evTPed-8F8lvS4uMmLEYJqPktuTShK63_7TB5xyYgqKt_z-s2hExW9zKj7Um7NFizpZZNWuHdOBnvJj_TnaxKfi-8HlCiMJDMvh4iTxC5CY3yF-t8L1uqF48m1iOmdmzhbEBHOdocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23670" target="_blank">📅 12:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23669">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgUKKC9-pZ4v1iuATwllLPq9HTARp7uA_qce8VXVLOFhAdUIA9cPxzrZN_tufstnfMbU3luw8AXWV6vKMR6pdeWos1HxZXKLwt3dbjIzwnMEza1hns7sXLXA8jM7HHQxE9xtJHujjt5vGTT-s1S8Q48IXbPdGGkRKbmtNXFGruaNv8FQVUvwS1wOP2c9vluGNtIMemS7ngrNLunUL1wnee4mdGGUZHyMlWP2f7Hch1568sd1eBV2ypZOHjet0lWtceiM_iksO63Q_RQ1dCZqxs4XBbk1LQr2-8yuAxIXQiZ6SIfsiyaUwh8h3tpiz4PRFHon-D8q4njYMn9eIcTyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد محبی و مهدی طارمی در پایان بازی صبح مقابل نیوزلندپیراهنشون‌رو به هوادارایی دادن که باپرچم شیر و خورشید در استادیوم بودند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23669" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23668">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB2k025FaqBemiVR4pOQ94j3uWRpxY7Q2DJ6yKmQsb5bJ1f7gzRz-63qVEbTySuB2clSoJCU-SJp2SGdr4-29JjgA9it-4pZDOZTU7be0qOyIuS_1CcKRXksxZtxvmx7MaORT0hTZOh-hEZO-8SDnYgW3pS_YR9UWvWHwjRN00rfWYfUdie8Nio2nOCQqVuA2HEcHzhV8VWU9ldW5--kPyv23Xj1TaGruZ4BKlsdQ7eNYI_hdWfNyjkaLt6KG1LqfRvnIn1jFVNlFFEa9XgEOdVGF_ZHnHgnLP1Vb7lo-SIODFYSwRJXXKmlHdoFbm0Kl2M_W6mFCPrCwz2qMGiINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23668" target="_blank">📅 11:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23667">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuLey51Nbs5ha1NkKZjdoKoXeCSyct-0uhh9QV7BptM_cR8gvMVEKctRrzdIdTBKhLl2nCpD0I5JS3iIZeeOS4vSVG-uXYNAg63m21D1Hjg8L3lznkTI2TgRh3wD9XLHOcplYnoA5aNu-pfj75ljEGVD39M59i-mNSJTN6GgGEKPsjYsZteRDKUCbGNJ56NBn-NgAF7xFmGr_IFdq2jbIc3JBHEw6lTIeviWlQe3dPqfJcBnZDK5dm8CAw1SSkxeWOFpQ-bEybfzM1YRMzWWKxY34w-M9zQLSYWa2yqPy5c_tHTg76NyK_xBNSz2mswq5EtB_cwsOhy1HMtkZ6CGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23667" target="_blank">📅 11:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23666">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Evd-Fu5GlJrhRPyfN6EYPlipAJrdKkCIdPu_oEe7GCcQyB5CkKBiLoi0TC-90zyGBj1iz7GEnkM4HT0AaCRJU8yMj01MX9C54t0n6FryEmTmihlwptYhqlt8A56bg-mJk8CBpT9LFAo3xb8DuQk5SCBq9wylkrI-UOoiGjWG8P96-4LgRnQiWdN7TtWK3pVy3DDNZP1aJ4QT5G8jJMiTUZF2Psi8bycsJkRXJn2el4HJu6AesU4VqqI4vVHW7FWrddqEAc6QVHdFT39VVsW_T5MF7gfn8v3Y7KtlxPYa9idgs7oDrTilYuY4z_HEk5QvJWV1D7yDWKNVmZe4SDNLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری‌عاشقانه از زوجای‌ایرانی در حاشیه دیدار ایران
🆚
نیوزیلند در جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23666" target="_blank">📅 11:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23665">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUWQnT4m2kCFKIbicc8repm8PPSgkLejlWV1n9d-h7XB3XZP1zjgs0mWcVS8CNBNzkRpif9V85ZKoDQZNGMOXisCDnl2oQlz4NvlGzqTEiAg3RjKtS-0QWBgSp-7kEaToDah0Vv2apqB7r3zqEqp8Fd2zm5Eft2GtWe4mjYN8HZ-LooUPgswcBgF79yuwEOcDC2ruRKvckBMuzMwDXPf1GFvCcguSBSN9CO20Sd4QnwneE2nbutfuqvlM24aEDwZHF8Fxfjmg6e_RmcTbT_kaK4uslqOOqqDQnSvj_dKHDjqbh_4isvy59qTQLUVVkeH-fWSYL8xcvLhoSMkonoxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنتونلا و پسراش دراستادیوم بازی با الجزایر؛ آنتونلا در پایان بازی اعلام کرد که بزودی همسرش رو سورپرایز خواهد کرد؛ بچه چهارم تو راهه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23665" target="_blank">📅 11:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23664">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlKSFoOtESUeGw-kNLsBXI7jXGDZ7avLdCt220B0vUZJ2ejzep6GJxlzin5RNl_W7E0Mw7e3CP4b2r3v_Mr7oP9XV-7g8S6r1SwB7J8UfPO8SG-NXstOGReMsGuVSmXB1BO_rOtfXjTYVgtINqWNd4MciZ4s8Uswgd6q2vN6EBa0oI-nloTR4lu8a2CHTiKaABCeJR-UeH87Tv5XYIVeo2l_gc3uSIjGf3z0eW_HOgnxkcidl2gE-wW3os5Vph_InebbLDrbFLH1QZZ_GiPoIjke4mQjrveoAWOvDFpMusBCJ-ol04Uslv2a__wZKHQ4147xo84wjd1_E4zs5maajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23664" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23663">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHkGapaCSdmZZpfHeKWm3iaY-kYVj8Ct6O3jYZMPpjWpvL6SRRQGfkATK_UXAO_ofs9pNrHJsRDsDRJU7bb-nagQ7OO0mndGDk2jq-uo4ODrBpDACIHP7fTLXPhuDR9xhOuWPqTd2LJnY6NhoCQuQY-XZhNpi4YHs1uZIWJwi2Wdnqm6n_FxlhvWBCRgZXkF_7QAeNjxU487RF9Yb7h1rxumHnaqkKYuICtVvViBWsFzbrlWNxXTEe0MvARn5jZahFKjOwKbJMseUnUJHOu5I7HSZ2T8rdXBsDMuXnI_IeoAlKVR-ybe9k9QIhse7GyfTeWffsyq_-x0GMzCRp1muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ لئو مسی با ۳۸ سال و ۳۵۷ روز مسن‌ ترین بازیکنی شد که در جام جهانی هت‌ تریک کرده. عبور از کریستیانو رونالدو با ۳۳ سال و ۱۳۰ روز.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23663" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4HBkd8KEERSvVstRvokO6qkNz3c7w0USxOpwaovZdi7pOSI1is3thKas7ZLoR3hjZunivkeSFlzyN0dZ5q3NzhOAH-FG3XTsi5XnbARpPmIC9R-1j--ZlOJTd7V0u8Dg5qIWBohuzGYHjgu0MNU99czcrAHWRKKVkc2T4tS8IqUbGdTEaY-RuhC3h8WwMEfzbg17vKRcJD6AI3J-PnAXSB_7e86lXVptWusnkZOaT1wByXF3N_K5g8brjVx3mdFFSumi_LpvGOdCWtC8OZCwZA8yJd1-4lJ5mYNNFFNFaT5bPzFM45D0AaiHZMdWkM1GDDiiE8vrT0CX7T4RuBUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGmq9b2vSGEtHOYrTwc5Sd540BYjXZZin2Fr9CArsGLI1gbqU1RA5wLQHgVvQSD7xyHF7Tj34z4ugXVahHijZh-4NO1qgUtVPhx74WjvCEFHxLD79MrCEG7lH-DeovXkrUyfA8tbLB5O7GYy91aHYzoIgDc-Nr9XZhhZ6Uq2jQrck3dPfZ0wKHpkyp2Nuk30UWZgqwEEMvS4GnOAZOtt4sav4TgVfyaBmWdTmmtx5KDSgJLkC50_XRS_Y716A9ASBQv6Wi_kwiY7B6rSsqao75uKArrxd1XeCUgjunmIgrO4zXGFFjnu752pB594aR6ouToYmUdCBe7-r9l7sw8sSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23661" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=HHcOIBFsoM8uDYYGWBREyr6FONc3w_2iDI6zuTV_SYKAnWzOhL-0_JyFVAvHZHxdqhvSbwT-ZgUpZMkt4C46hn4GDZBPhE4oqdVWDQn0HNKtWlhvo3OdzTlvX9PPJxL_NRTT8VT_gGV2RENHetXYCoUhn3ea7HTbNWILMCkgD2W6ULDElR5M-hXwSDYaJzEQvB04_6UELKiXvjK1J-KG2DjYzlNQvWN-7fptPDauskC-J3uiZ9cOxb3mH3qVhsRra1nE3tQCaebYtmlxel8sJYpcjUgW9DO4rNbDpKVR7wJcZ5G8Yd9LcCA7iuN-eWNMQ1fg4wm7II30zpOe5Jr5kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=HHcOIBFsoM8uDYYGWBREyr6FONc3w_2iDI6zuTV_SYKAnWzOhL-0_JyFVAvHZHxdqhvSbwT-ZgUpZMkt4C46hn4GDZBPhE4oqdVWDQn0HNKtWlhvo3OdzTlvX9PPJxL_NRTT8VT_gGV2RENHetXYCoUhn3ea7HTbNWILMCkgD2W6ULDElR5M-hXwSDYaJzEQvB04_6UELKiXvjK1J-KG2DjYzlNQvWN-7fptPDauskC-J3uiZ9cOxb3mH3qVhsRra1nE3tQCaebYtmlxel8sJYpcjUgW9DO4rNbDpKVR7wJcZ5G8Yd9LcCA7iuN-eWNMQ1fg4wm7II30zpOe5Jr5kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
«ووزینیا»ژوزه‌مارو اوورا دیاس؛سنگربان۴۰ ساله تیم ملی کیپ‌ورد نمونه‌ای الهام‌بخش از درخشش در سنین بالا است که پس از سال‌ها تلاش در سکوت در جام جهانی ۲۰۲۶ به ستاره‌ای جهانی تبدیل شد. او که کودکی سختی را در غیاب والدین و نزد پدر بزرگ و مادربزرگش گذرانده لقب‌خود را از واژه‌ای پرتغالی به معنای «مادربزرگ» گرفته؛ نامی که ریشه در شوخی‌ های دوران کودکی‌اش دارد چراکه در بازیای خیابانی هر زمان بمشکل میخورد به مادربزرگش پناه می‌برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23660" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23659" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6p9aczaq4pXxq6yjLxtFGopkT-6iwBZakPXpg7SLs6PaecR9Bnof-L3QRd6gnYCsaFmBbxb5RoOGcpZqF-_KIJHMqGQa_ya2KtiSAWABx-7QbFAu_9yLFvzjAiA9N8bT3cyBYnUXv1j0ze2fTvSKtQ4skDxlGM62qDdMCaukRVaBl7rR9_5aGGiic4UcNEGJ2CPEmeEIYW08Ew1-6MY2-hy_vNKotcCbbLIHtbxtxVE4Oyn_FwZNokQ3vwjfa4tFSy0XcIm8IErcz6Z6bqmF2tgIMd2nguQ3gEyfV92On1fIMug5z-QykmCSxZRW5o5Ip1PModXVTExZt_kBwYbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه گل‌گهر سیرجان پیشنهاد تمدید قرارداد دو ساله به ارزش‌سالانه 20 میلیارد تومان به مهدی تارتار داده و منتظر پاسخ نهایی این سرمربی کهنه کاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23658" target="_blank">📅 10:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke0f-VHhinCyQZVSpTNIwc6jLXNBKoCtJuzi9nGgrykoBSgzLGaWUSvYrdb5qpFTVh9eMuTL2qY2k7ApvZJn1tRtvR_C4NJO0gh8y0spYPDu20soWW9Yla3kXOTMEqZhESzRQZGxoxKh3Flt4CibzBLBoMYNU810-7QskDqGa-6dBjD5DG2GElbCk9gIz2gPoFQfzz__6VHpAF3TMKN-JclwsAvz4gNqTvM3U6fpJBPJn-larzR-1G7SfMH_QYeAN97TGrMumCLqo-9FTq4lTh2lnQFPpSRyZW52va4oyJd_FEJXbpY4VUQ9jofe1DA535fgEjSIdBjeJDr6lmkFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23657" target="_blank">📅 10:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4wpSG8PzR-6oA0EPLBcZI-RDTO4IN67BW10xRFGC1VOP1ir0dXxLW6XIBSmSzSze2pcaiEiPHeCzyx4m9mGWaCeylpxzFt4xwSX5LMo0LuZj7ZKz6-pk2Xnr1aqV9jWOuWvHs3pQUg9frSxIR2uEkiRaEdK2PIOisuyvhXtMIW3Xed8fgwJRzI1SE7LXjYh134qzWZc8YvlqPIW2szh6yz06Un7YFJ5j3Fdks4F4Ybq_Pvk7OeVYEQXoT_p19vXj2b3xqsCbkiGnM40o9Y0xVZE0Kv_aMIF2dFZqGB5wC-5bRleCIZ_1Fi9o_9bqEHlDl0yyN1bD4OhGq90bI99cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23656" target="_blank">📅 09:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚽️
خلاصه دیدار دیدنی‌وجذاب بامداد امروز دو تیم آرژانتین
🆚
الجزایر درهفته‌اول‌رقاب‌های جام جهانی برای دوستان‌گلی که این‌بازی فوفق‌العاده رو ندیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23655" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=DDsrETy7CSdSwXSBe_wxc8_0kTjclknbv6SquujwhNquamRfn6it0B0fJ8a-RiStoPcJaiAOYdTkGiacFFv48ygBLNwYJ_TnGA9gsUWocsQLuoaOqMeY9N48nv7h1dhLUOVY7X4OdRNaupuB8ZRgUjU_CzUE8igurpeDYYL6nUB_eqzEOYWUItOPf_UOwmwK07UvUhwKMJI9dYSIOSopSGGhOVu1lv3WBWUhrLl27-cJ47LNm_-9eIjKyE7HGjOwJzWMbbWNYIHFe_yN0sEANcZ3rXv7A9a6-9n8vc6HB8YRDISxB1Ho7mCPlnJfaC1C2MRPt2nitI6hgd6uADXSN1j-NZVx-yfE2iSRcZGjI9Eo_n98sM6wp4hfZNnPKkkFIxWxzqgi_kTH1ix_02aAjN3zUhUvzjydIBdP7V2A0yqps8pdpPLtDIxh_k0oh-kDD90ZRFBL7AiLBwiT7aWXWCsXS3SO8Pmz3TjzwfggdmidQP_gunBoknT1P2LCTYYhPp8w5jkJWs_oxKIj-KycwK1ITzJW4aah3XL5MeDj_TxlMUYQFnGLAvAEwfRehiNE9BYatyXjBOFfkoIjKPhlvlkIblVMDYMAyOfR2JQXQSKzq0Og-cJOswGyK3aNI2pCLT0FRecOe7kFWeS8f4sGyEW7QkW2OEt9KuYH1ZAS2b4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=DDsrETy7CSdSwXSBe_wxc8_0kTjclknbv6SquujwhNquamRfn6it0B0fJ8a-RiStoPcJaiAOYdTkGiacFFv48ygBLNwYJ_TnGA9gsUWocsQLuoaOqMeY9N48nv7h1dhLUOVY7X4OdRNaupuB8ZRgUjU_CzUE8igurpeDYYL6nUB_eqzEOYWUItOPf_UOwmwK07UvUhwKMJI9dYSIOSopSGGhOVu1lv3WBWUhrLl27-cJ47LNm_-9eIjKyE7HGjOwJzWMbbWNYIHFe_yN0sEANcZ3rXv7A9a6-9n8vc6HB8YRDISxB1Ho7mCPlnJfaC1C2MRPt2nitI6hgd6uADXSN1j-NZVx-yfE2iSRcZGjI9Eo_n98sM6wp4hfZNnPKkkFIxWxzqgi_kTH1ix_02aAjN3zUhUvzjydIBdP7V2A0yqps8pdpPLtDIxh_k0oh-kDD90ZRFBL7AiLBwiT7aWXWCsXS3SO8Pmz3TjzwfggdmidQP_gunBoknT1P2LCTYYhPp8w5jkJWs_oxKIj-KycwK1ITzJW4aah3XL5MeDj_TxlMUYQFnGLAvAEwfRehiNE9BYatyXjBOFfkoIjKPhlvlkIblVMDYMAyOfR2JQXQSKzq0Og-cJOswGyK3aNI2pCLT0FRecOe7kFWeS8f4sGyEW7QkW2OEt9KuYH1ZAS2b4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل فردوسی پور حین گزارش دو تیم فرانسه
🆚
سنگال‌درباره‌قضاوت علیرضا فغانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23654" target="_blank">📅 09:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">▶️
قسمت‌‌‌ششم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23653" target="_blank">📅 09:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23652" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23651" target="_blank">📅 09:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jv6O0puozxjkQCpC47ADyeYI6AYrqXdhOCC9ktnvViPkWSNLG_dPHhHyP_aNE3Kecobm-zWplhJ6y8KX535cP-WO_gQc5YKrvdH63b-FGehMHq4BoCx8GcCvaZn-ZQr7QWsqOqNYYUOfhB4-O5VoE23kBqOuJxSewl8Tk2H3wZQpIb9wbcYZekvS0121F3JE5t6eQMPiqNeFnadFuxyOAHVT8FICfYp72UPbhkSB9xx6e8Z0Ar0sHMHgWnyrXi7GSKiQlTKKffnpDus-qfszX0-iIanSn0o5cBCHMxP6HFb01lf52t50DnyXhCnEKX8DgZlYrzL5tkFj32bOkL86bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTA4aZfsVZGMbgeQedHAa9IbLsBl5y-8OJRPNYi677mf-QNkKG2XTyS4RPiBFpxkd66O6qVv0PkusgIAB_HVS82NvY4ySiOLTw5yNd4XJ87-ooKux23086eJRnCVQQjotExh4gMO1b0GPjXaMNpKkpxXBXTQZsxOvz-JPLJM7eIGV5h68rPZFf4lf-Cl0oT9MHR_vtZlXDwxzD1oaHqMXndUtgZvEL0mpLDBFH0zj9M1v6S9ip1Jpd-jxiapsICo3BhjSxyTJ5UazJ3qfXPqKmVle6k4K7BPaQVW-pVbO0WU-bP_oT7ZaX-o6bhdDYp2uaPczpFqv7ndudRowYtXgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23649" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTZvy6LK7GgHxeK9IYimZFAHET10yduik0ugrDJJ42drjU21iPF1nPJl1-nKW5s0B1RFCNPlpjRlOfrKdIbfd0HkFZ6TaVrOhlRZyjWh5AgdLUjtXcCSuq3pI7Uvrekbq2Pd0LmdvR-Z3dkgx8brMda3DpoTfTTGtT5982m1elxMrx5XsuRCL7golrkNGZ0EjT98GJk6htQB5wL-HI9xGIhaC0EMSwvRsdbB_Fl3oAq1XFuaVoTYRDHsUgdRfZKDm8D-y2I2OyHRWDnaN-8bAjZ5JpOC-hEWOGFDUXFSzDMWp0iV4gzgy8VIpD_1CZwrcs1E2bgNM99EQsCGA0zG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23648" target="_blank">📅 08:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23647">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23647" target="_blank">📅 08:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23645">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iS_cWVWlPpMQPFBv5Ru48mTDyjLPRTVlFRLAl5QB7Ea6UCkwxUWL9w9i5hXQj11J9rngJsiJgR6kWxHwnzoNXThteWdaVR6D2SvoQvodmgGDKs3TJSVpgwB3-upgFlO-Oj6ZBqUYnH0NhjrkQzMR3TGBAoNgqSk14vRCa5ITqFfzoBUQvNG1RcCbV87THo_Fh3GppKSOKQTuSYqx0ZlgaOJ0ZRriEaEfjNNP8PTsnqGLf812U-dPetQXmpIJ4t9qkxsNIShFZh-1aioAGBeniCoZxN42r6TcsjwKOyZ1DBbUg6dyJ1bL4xv6SP-oiIgWJYF7QVpIE2XlQBMDC2d2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hP478hi2TzYBXA7v2ePGIxucIYHcnZSsJTPtGl0vqt-hpXpAVXBjSHosNw-uWlskseMsnzP5-EMLS7WUf23OyzwTtA-0sXcWle6WJdFEcZFlRnJVwZvDiFGhJZ3k7NHCAec7fbBpL1ZFPHqxXAEEAPsi_KwKgKD4AqysquXwLJN4uGevIIg5Ph56B-3jI4WwYq0XfSZMk65yaqxbOmxfF11HXcly9LHNTrNgXN4pGRTMVa0Dbq36x5oOkgphxDuShWu4VHq921ESEmJ8AqyWdCiNq4qI3PqvVCAl5wlv0YAf94lX9yYLpYdxoDOAxr63Fb32qUh7F51CEH2t338h3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23645" target="_blank">📅 08:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23644">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f480511b29.mp4?token=B0DJJUZmWz0R_QbnT6C5M_CcEQQI26NnMpa6IxrNQdMHVhv5spLAUY7tVGkojfgGgQuKLTzRoD_VTxzI6ioPO43Np6OKL-ZojZ4aYCGy_B2-7vXfOMwX9OMsR6HP4Lr06oDsJqkHGxAODPYl2D70gAD6R-gKONvitih0JnGs0xE4fZMdPVxI8odGWpseGOsiMH802zQEzdb6VlIsxcgLbC6V9QAEw4Hs_ko4dkcoCSINB_W6n3QDjPUmQVZFzMJQN6Pk1_8DJkpVSkUK7R0ONv_jQOq3FzpnSztlkpke78aZzTlkzXcU2s5FMf5Mzs9glCTX1k4ZPK0qZN7ZLHqtwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f480511b29.mp4?token=B0DJJUZmWz0R_QbnT6C5M_CcEQQI26NnMpa6IxrNQdMHVhv5spLAUY7tVGkojfgGgQuKLTzRoD_VTxzI6ioPO43Np6OKL-ZojZ4aYCGy_B2-7vXfOMwX9OMsR6HP4Lr06oDsJqkHGxAODPYl2D70gAD6R-gKONvitih0JnGs0xE4fZMdPVxI8odGWpseGOsiMH802zQEzdb6VlIsxcgLbC6V9QAEw4Hs_ko4dkcoCSINB_W6n3QDjPUmQVZFzMJQN6Pk1_8DJkpVSkUK7R0ONv_jQOq3FzpnSztlkpke78aZzTlkzXcU2s5FMf5Mzs9glCTX1k4ZPK0qZN7ZLHqtwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23644" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23643">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1gEogzhN369lKvU2Lr94GFvMTbUuexSivOA7O9hjVCxEat1C_VtwDrV3s4uNCC_LK2OBauEVEihVq7JyqucTSpTLkRr_gUju5W4mv7_ZjdEWwJ_wRWvnp306gfZ52neVky5FqNOyXHWtqH_Nu1oApK4E4ZsGdADku86umPACXcdrNyH-n0AnFPv87nzFArZc8clY67q_oAXZ0Ob2UVluEUKkmblw4-62hTvmRLpzzoAgPwuK8opgwSmpBiOUP7d6vSchlel4vudYfGQhSfpwr9dSaoFWNgyiFx_OEzDizGg5On-dWVthSntfOdZg2nSLeYMP6Y-1h4kMI8qOwSHsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
#تکمیلی؛ درخصوص بازیکنان تمدید هم لازمه باردیگربگیم‌که‌باشگاه‌استقلال باایجنت علیرضا کوشکی و محمدحسین‌اسلامی برای‌تمدیدقرارداد این دو وینگر جوان‌ آبی‌ها به‌مدت 3 فصل به توافق کامل رسیده است. به احتمال فراوان در بین بقیه بازیکنان قرارداد روزبه چشمی نیز تمدید…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23643" target="_blank">📅 01:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23641">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1iPV4XLb4xrJQ9OCofG6fr_ycWFm__MtG4_OgqFrfjxZiYx4P12e7a-4YtBHlF8ZR_RW-I4lNdeApL9k3BCslkmFF5aG_J-LxUtgouzf9QD1DSWnXAzIqKRh7M_1pp2PD222K__UcOLpoogimA3mV0Fxc8b1o6oABOg5-oOjO_AKyEy2BRwEBiS_pdsN5__JtbyVl4hNR1--erYO7dsK5CQ61NzPyYIcp_uQMujb7mDVZ8z5dQA-WNPNlmBs00bDezCurQzJqPm_G-4uZCwMfTLPfRWteBR2NitYnECtqQEEhVElN4x9wFQyEk6zQYSIu1Fv-x2_nf3VRsUEcI9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23641" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23640">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PveahqgxjjDnJSAsCOlTeglj-OHxEpOuW5OKvktWFenjFrvBzxN2f69gDzQ8yf6D5XDsAbewIKJZV4r8gPJ2QXnU1Z2F6mZIBOHg80KWsmUMarrjaEArCKkcxVFAJC-pjGN1frn_UQObRq75du5rfkVRIVXQfElsYaCmXg7AwQIK4ecDpJw056nhjB7-PZhe4jXtRrXlMqdB5nCm_4XjRjjcyEPHgylefTFiEMYu3DeBEM3w-QkIsqcCrhrIJdc63WGmSmPKmIil1GfyAWYecGzi2XawK8DzN-YsV-GY6i8ujB4y_wGdXoJpaQUhfxpcSnJ_TI_TfMj0VsM4LAE22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
استارت قدرتمند شاگردان دشان در جام جهانی با درخشش امباپه و اولیسه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23640" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0ssnaEFC8V4m_M_92hg0_N5DOz6lE6bWea5p2HiTW_Raw6JNm1MdTuO73qs98fIPyg2HYq-VLnAlPrURtn3m_7j1nnOeboZan49QvMaET1-1VmRtqYmww8EMb9h0UApHT3wQJ8mxGO_F2TjiqXewBU25oBDKhuit5db3O7VuGHIaABgW-SbMEdmRonHzitWBeunXR6ESP-ewA0Aj3FyasiD-J1gM5QJEcL-jrZctQDn-HbdRn7GbsTcw2L4gAicmZe_wpgfpHXPN6-qhXf-KLFgk6DuZX3PVxZRkbO-ey83BSCoggKfsUVuwtGYe7oi9yvaxuTVDItADoBz3KHSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#تکمیلی؛ جدول‌ بهترین‌ گلزنان تاریخ رقابت‌های جام‌جهانی؛ لئومسی و کیلیان‌امباپه برکورد تاریخی میروسلاو کلوزه اسطوره آلمانی ها میرسند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23638" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی شیرین و ارزش‌مند خروس ها با رکورد شکنی کیلیان امباپه و در شب قضاوت درخشان و بی نقص علیرضا فغانی.
🇫🇷
فرانسه
3️⃣
-
1️⃣
سنگال
🇸🇳
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23637" target="_blank">📅 00:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liwvJL6Em7No0uh97Ox9QCNYf-EbCgCG2yRrWanctmvbt_ESussBgD8lhaM-xi-TXT5auU02e9KxpnN1NKy-fRyWVw44w5JxfdkHIntUrNqPq0QemKitMFPN9lHvu8buO7qmNFT1qE2ao172Wq0vteE0zXrFN-oUnc7MZriWN5Toslwg6ap_Rs-UHVqxBg8C_OnjDzXLm2laO5-OySy1b1rPBGdAyPrbeRTCfZD--1e1HE7rNJ6KSPlTadCQhU9DbRhL-KWPINZ6P_ICOHZ9q0vseW2mOuWikUc8bojDQ-mSTrrWjLyFavjjiwJ2oDMOzSkx8uVwXPslCEz2Kgkcng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دو تیم فرانسه
🆚
سنگال؛ساعت22:30از آپارات‌اسپرت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23636" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23634">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKHQGH9sVll5w-22hai7svepgFg2QdGzJYtjRDZ91fbIldObPQrTtQCazbuPqacUqM8NA_HoJy8Py5va7jAkjzoxvnNAICdWVm_CM-Uar6qVoySWQmG9XMt29Ns5yDx4DZaWRRwkDwvN_s9k1n6kSomBi82fJf3v4bG-SDuDsljHqYfacdW9DjLyyt4nB-1BkYes3M--On7TOzV1A4FTDmckJ0OUeMbZdtOTHNacZP-kIzIQhoDCgwZfyAX7bIc7T15ibwNBmutNCr8fUvc7sbwvv0SvirhqN6z1CJnoFFZNhat3sjJzhrB3R2ca-BRLMzmWXQteVHMbxpJSfwSgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B88t1Oj30wAZuFcz5dH0yTy6Dfnj7dRd7IqJklapbs0jLxMzJn7mRVBxr-O3mXdLWSiq2BSmpdp3MsxSeVNeUT-MvFW-IqVr1_PN0dITcQGsv4LCmmkyKN1jF6aEju9ueB7FOjEU_mDmyF1vU3JOJPm2zOUBm-PwGGB5BV7fdPKWtI5QjresOCJ8_67J_jdAxQmQlybZ0UsDUHjoOBGLb7egHlG-aqAAJ47wBkGabhptCWP-GLK-UkedR8DUellxsobaIys8mK12KngL38q_w4f-bYocJOG_hPNpZcxB2Zb9rmbp4ut74C3ixsfsCzzmCKL-WMYBqGIDBX6ju4A4AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم نروژ
🆚
عراق؛ ساعت 01:30 از شبکه پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23634" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23633">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A11E8kDf-QiyJYRmJ0xrhmTkVdHBj1ktDdSTULKmPSPhdXAnYnNFCgeq8tr0_sQNoCuReIw9sqtxNKAz8lqtR96MnM3Qf34Z6ioRMS4T9u78upf0Mo9wsut8Vi9YMk710CirhxdezynbHqUtuvSOG9rCXnb83_nLP-E3aZlwLKre2Fr3M5MdWyrLtWLCaeUzPBN4Wl05fgRVQpThOoYZglsUr41v9idLYt9AM3Ak6iNTH5V5lk93xAWjw7bZm44foNIwP-fZVOxypV-uJCcbGlhdJA5ECVpbGacf6RjPiIadCtMmbVx5Jgq9o9_WGqkahV1u-QFSTSHDMHXeFPjqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23633" target="_blank">📅 00:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmm2zbddKQ74MSjmAXoC2KXrMXi17o0hOYdiZGJQbvDXmuZrtwhgMk0XSUFwj7MwMrMB7O-Ka0wdSZBjlGqGlJis5dce4krMwDEfgf-MFOhC4zzd7-Wj7VSyIS7jMj6PqFjPP9pLx6QGbE-6vHxIiSdwzz-UC4Ii4USrdrB4SaE8nBfA_dxhuLW72YonGF3AvSY8G1YvCyvAQuoK4RPavS292N9j6UAoWKXJVbvuo5E83LuYLQhXhh9Zdi5hxZtEKKiCwLJoMBud8_z85ho44DBMjEs2-MHM0Q_BTsPlUfT43iPSMCsZ-cXJF2mEvmfeJ0WZgvEIzLz5RcqySgamXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23632" target="_blank">📅 00:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oINHBEJZX9W7APcbImqK9lWzu67_NRVP7fNZHqFdeiB7VyjMsccaK2RLvLMxEFdw7Q4i8dNWQpEaDJunhW1K6i63k7n4UHJvWA5WD8lh6Na1Orz4NqWJJ2t8sDM2mC2IAT_ArloPP8dDmUq86qyu_kFz145IJma9ciqde_hJGj6nWBTqscmg9ZRDF9ivahW1OwxUFDNhjLZdaZxeT8hob3Hx6H1cR_NjXI-zGwqyWDMEU1m_KUVQyFABthPebMWrncM8urJDDgI23vGHzMZvg6mAEhGJL_GnKdY8Q8-cg_o37myLbIZvqOrZamaTkKjj_Y1QYhourTpzYDt9i3NBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ به‌احتمال‌فراوان بزودی شاهد هیر وی‌ گو رومانو برای خولیان الوارز و بارسا نیز باشیم. اکثر رسانه ها و خبرنگاران میگن که نماینده آلوارز با خود بارسلونا به‌توافق‌رسیده و فقط توافق با اتلتیکو باقی مونده که با توجه به فشار آلوارز به مدیران تیم اتلتیکو…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23631" target="_blank">📅 23:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_JGq4BZSaR6E3Qd9GwPTgx6nGTr76hwpLp_kdZNT5T65_5ufn916D_lyCrMtlg3M_O9kSKZfajKkXbVr601-SDH9RN5Y7oU-iCmKHl6zl_HCCsSPO0e_LNQ8l3Cgs5CpYbNM3kpJWZ1nQwOH9YNVDMAB-VTuhy3uHQbcz1eqmSDp55B3plKA86NvZpu1izdY-zuRRxaDWShok7AQevRc_ZGE5HdTPXq5VWsqGSVCzPRM3OcEBAhjRqmsr9IRsjNmuuvMH2XwdCFFVW3TLlAS94eZNZL_ESELsD6lzJ8MdyFGCjs8R9dubJP4yy3KC2y3RjmZhpHXi9OA5w43M6fgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23630" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=uC5NYjjWpHFwus5odQ2fYWahDJ2QV6ot1qVitX3L2zLzel896oDVXpgVrCX_IapM5N8uOpYdm0qJWKNJMZpknxukoeGZ6M9HXuawRUBThupiis5j6nV9F7Y3zMgwZQ5TYNrBcCNnaQRWcCxzIQyX31k593XGO5HxfaSGC0YPQNkj0PX2h-nANcXIto2Oanlbw7bA7f2UCs1zpMITCrTIzTN4j-hEOKjtMBMgCowCVl6qoN0ox20pTZWgUFEAA4Www4mHyt-Ng__9_RfDAgNulJpdUemDZqd4fzzZfhShuVFh-Oaoiw-yOBCMAWCEmwsW5DrEHCZTOczOrhekL2kISQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=uC5NYjjWpHFwus5odQ2fYWahDJ2QV6ot1qVitX3L2zLzel896oDVXpgVrCX_IapM5N8uOpYdm0qJWKNJMZpknxukoeGZ6M9HXuawRUBThupiis5j6nV9F7Y3zMgwZQ5TYNrBcCNnaQRWcCxzIQyX31k593XGO5HxfaSGC0YPQNkj0PX2h-nANcXIto2Oanlbw7bA7f2UCs1zpMITCrTIzTN4j-hEOKjtMBMgCowCVl6qoN0ox20pTZWgUFEAA4Www4mHyt-Ng__9_RfDAgNulJpdUemDZqd4fzzZfhShuVFh-Oaoiw-yOBCMAWCEmwsW5DrEHCZTOczOrhekL2kISQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
تیکه‌های سنگین عادل به کارشناس سیاسی صداوسیما:
هرچی‌میگی برعکس میشه. بسه دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23629" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huD4aB8b6Ma11nPdfDu7Zf50f-FiraRVEvvJsx_oG_PH6TLbqhs2coak01PbYiK2k0FJy7rDp00gRt_ir8G2W-UQ9cQ7zbZfERpWyBf4m74KV_eX5ZGV9LlI5gt8RlAxFt8lnCJ571Cu9HvpAy7WQrOooKX5sPItDrRmPEUf7KH77WaovVttPTjd737oHKp6Ilsjip_AMUjP5G9Z6FqQNJVIEkDIJo8mrsVCe_n7EKt4gYwMZK8qEHqeewI8Riqvgqo0dM_OlWtxZhq-qcG2L5NLVdAObArrWop3CXLcjyEG0tcC4lM_Fzv45qEqIx-Ys04eKnLmSEu2zn1IJashHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23628" target="_blank">📅 22:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOslHODVOqG-aQmRhrxnkYehnrbw_wr91xasHeKapiwoiyj4SlGhlA7sEdzo7VI49oOKbJ87XjFW7jseNaVW5KiA37sz0mJvQnVVk8JojoN-AfI1US-cp9kAC_hCnZFpeKt3Y1guFZWE6Qb3pFRDXVV-3PRwn-vgVdCaCXYVZND0nNtSddW3KQv8_RvkgwifGEjfyX3Rh7oGQllTXEIu_DFVxNIPr6n-oCTdUxK5SOL2_19-NdVXMzLEMbp05A0UuHdnJOFSi6uoBf60_d4Bhk6dMh4C6tgMPzmp_O_b3D4iZOYcgjzhBhTJi4nLk6FTzDA-skHRxq4AgvHl0UsOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23627" target="_blank">📅 22:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN_qI1gv5HSAmkJGObtmdLHCI0j9UXFZTIOT-R_N0T2l7Ou6nbxSYaqfbWd6FjBEDlmdZY48HTy9J9FKzAu0Hy7_T1F-XwVX7E3YUKetjIa9ZbphkNYI3lXNWgO_keuAJaTm26mqnA9zQ-DDgUF840q8Q_S0mwY7Cg6BFoivMHwvX2R1resXIgUiWIPbkOq8PvSWI9AuS407wVtWzgEkF-4dk7JNsYErLyKtMFtvtCxQeTK9b2zsoOedbcCmATZ2KMcY1M8OLBgYlnRIrNnfaTDPwwxpMja15mfZkfeP268f3rR7wm1fBbe3k8-Q8_0gsSI3-dohl73PDGiOm5XHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23626" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23625">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA3SsY3SzKbGoP3SX32CBVROYSefFjJubkbnT8hUW5rbY6NwlB8unOHrj77WIyUQ1TMXlwemYD0Ik4iBsNX6pK9wrMXxkPwP42DSUWMsxWavQtFJ9T0n8MGqyO_AbS_hzzhzuuc3JH4Zb9-kzCA_mgreWx2c3p1bVRMMoRfUxtLyL3ea0sPIg-jbB8Ly7DAKcEy-wvN5xy5fjnF-oJkCrk7sqUPs_uNBqiv2j3fbf8Xl94cfyBCJzmRBB8gu_dhhVN7vkxW6wF6Hds7B-RsvEWGlFZZaRO_o1mXqigVHdJDEQ23wExX_bJKkHKVLdnyYbN6rsCnwzPTAk5M3eaHqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/23625" target="_blank">📅 21:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23623">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoDnbRpwI69KTEmhpN49b12Dyzj6-7lm28hHqKVhv9zq3ImvCJMTu8FNFaz4_YWU8qLGxrohpBqrABSZj1VKO4dqvX15BILxsAb0pJTUACcAIsykh7ilwM8mHuLnjmKJai4c5RESCiiXiLgFo072x5wV7JlBpvCKLL1TzsxRdtxDQ1QfeEZReu5PSP3fYgXfPkPe8FmXUluSwN2Jyi-JhduJ3NDdq2BhLBjP9iCnfCGo4Q5eYBr_LG__vOsPjYI-03lsQlEYCqmDgbCelChTsTeZCe9HHcMJ2eCba6DPgps_vlWSxNXxaCEkx06nAm1qvuaWSvSmZQj-aIYqucsh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHrlLCqvQ2PRHINce49kpzPUIJkFfHGOLr1R6yweaRm_9OLO3BMKL1tZGCQM7S1Gwb5o5ZCNo0vtfil0D8L_w9CzcqHXSATI0PGz6w9dw88cliHKuXJ4zU2Q5DR3kgmTrOYatpOVMgxqNZ7LmHWSxWFDQ2gQBCn3jkOSruY733fqHC5vZAvc6u1PG-fNC4nxHFq7MiusRRn_l3tpJq7TKnNsEgQrp75HNeOwRrN8WmrnbJt-C0nLQ8v2smji97hLPYCVUlgkPS_UcRs_ljMcvt-11H1OwyOZpwAbXp0EeugwwdHRlssR9icBueszXPJbqBNISXeYwhwQr33rXg2Gzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازی جذاب امشب دو تیم فرانسه
🆚
سنگال رو عادل فردوسی پور در آپارات اسپرت گزارش میکنه. روی پست ریپلای شده اپلیکیشن آپارات اسپرت رو گذاشتیم اگه ندارین دانلودکنین کیفیت پخش عالیه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23623" target="_blank">📅 21:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fk4N6TDU0d6hpga1t64gc8EUQTWsF0AN32syqF8-IiALEINdXiEcpZEl98Jh0tZJKuIlO4vTcv5ojq_MnE_SQ_vP_vbJn8QLRLlKDVu_qeJYHx4mPQTxAQKR9RPb5hrg0jLRnwUTgz4Y1Y2hyvbOX3gojIkEYqx-Akrk8tVDQGZDLgxF4ovA6XjuVADvUvpPWRyoIVGdNIxmXt946myHR3O_H4AsEIFxrpZkj9qqAGv4ZRs6_byI7x4FtdNKQCptSHmtFByF6CEqFsU8_2GhagVN4nAExVo9wgXONlA-FmBhCsFwW6fY5XjBCPhfYKcisPzcTlosuVVXnyfnKkYtow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23620" target="_blank">📅 21:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC2DFYfhZdhV_QHikxsCgqJvfChgkycYgEyELHmhPSgbABKu2C2e0tquSaKGtrrCXo-LOnL56n1u4ZckUZuGjnGaY0_cfSTqPXrzw0W_qI5Rcf44aiLuKSV4FUkirJPnY5n7CZMxWk1SzL2ztcmM6pxnJX9thfP0qZ4Z7ixwIkYqGJV977MtEJq6Pb5lIID1wVPSvV3jzPhIxhwqQNxeHu8ojcxw-jRQRvSF4V8NsUCqmCcKwwqdPsmscuhMejrWQ2kfKmzDtLjm4vSgpRhhfdkjdUeNGfXNJxIA2QV9pCjnqybbbmBMYpgFGs2-BMiGCxEIxv0zkwb-TtT_8F0uHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بامخالفت تارتار سرمربی گل گهر؛ انتقال مهدی تیکدری به سپاهان در پنجره نیم فصل منتفی شد و این بازیکن تا پایان فصل در سیرجان خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23619" target="_blank">📅 20:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335ba40687.mp4?token=Gmwho-BgJ9ZWU7BSI7Dm7L1BjsL9PBIn8yJupBPvzuBLrzs9h-QFRH6lXa8o6Fo0qlor3HD81VmqrxVghcUCc8mJVDj4lufEJ-hOSad_PR09lXFQqNRLuBVGI5kSrfZl9SSljJqw_w_tv00tAqL6uhCqK144b633VQygq3Zffz3FgQfdeXwJr9LLb0Swoz1RL5suVnb4E9hjVejMuAx9NjwFovDc_VB0caMRTbmOqbQAYGrXENaTmwzwdRow89Pa6l-GWpBaNH0n2O6CmnHD74ecLUb_BCMGC8LP1GKTwb7jU5rdiC0v-8WfiRIrpZFo7vykrN3UsZmzY4HNiF-BMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335ba40687.mp4?token=Gmwho-BgJ9ZWU7BSI7Dm7L1BjsL9PBIn8yJupBPvzuBLrzs9h-QFRH6lXa8o6Fo0qlor3HD81VmqrxVghcUCc8mJVDj4lufEJ-hOSad_PR09lXFQqNRLuBVGI5kSrfZl9SSljJqw_w_tv00tAqL6uhCqK144b633VQygq3Zffz3FgQfdeXwJr9LLb0Swoz1RL5suVnb4E9hjVejMuAx9NjwFovDc_VB0caMRTbmOqbQAYGrXENaTmwzwdRow89Pa6l-GWpBaNH0n2O6CmnHD74ecLUb_BCMGC8LP1GKTwb7jU5rdiC0v-8WfiRIrpZFo7vykrN3UsZmzY4HNiF-BMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
#تقویم
؛ 20 سال‌پیش‌درچنین‌روزی؛
لیونل مسی اولین بازی خود را با پیراهن تیم ملی آرژانتین درجام‌جهانی‌انجام‌داد. مسی 18 ساله در اولین بازی اش یک‌گل و یک‌پاس‌برای آلبی سلسته به‌ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23618" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdRtMylytFsK7roXehDcO34vZEa29oWR5ODlEydsR9ld4Wkr2Hix1BTz4-lINpPsrZpM3M8kqMA_h-J1LVf2Sznx_4BrVLK-obCXgwTK_WbJmDBL2Z4bDBJbwBzvQCtdkQATfeI_-V5o-wGZZtwsK4M5jDP8JDr06HxsyJyI2iXtBeaHIhaBTchUN3of68YsX-EtqI4y0tHxUMhVBcFDVgO4lEQXyyC0CW9qk5O0-SAwMPEhrziqqzY3OIm7thi3WGobx82XCNyzrWbFaE4j7qZ5mnY-rudp_hcLlSonUXJKSOrjoysLANBPCIDO5BBkiNjHlQsDhMzkanQMUXJ65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:  2014: تنها یک بردمقابل استرالیا و حذف در گروهی. 2018: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی. 2022: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی. 2026: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23617" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na8y2-Ny9s_Vp43-j_qQYoosbAb3n0ghLE5ldbuUkyrPQbJ1ikhIoHQYFWXA6hOVZpOVMay5XueiDkSDw41pkbozC94WoopQ2VZwbTyiXqPOfM4btWir99JEVnV3BtbWpJfNbi_lotT3hYTcKylRjW70ubYfLsKv_dHPYxNjW7qTHqBK-ZRDS2zJ_cste8B_6GrJOf25k3qplYjS9T5N7HK-WO4RA9oPRrip3_2SmVfDm5zw20XkE-AZk7IN5jY3lUK8Hi4ERav__99WsNm42a-f9cJOVRAFMM73W35ViSgbsw4oHo5jBd8glGKJ_ltnH3ScLsq3ZjjIAH4o0pDsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23616" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYfEkJ_12vk7hdYzRyDkH6qXEMcnPjGq_pWFjBQv9geg6M3ijh7kFLSZqWWm7Etf_6WYzlbb-e8Jmc7yJniqwShy9QIBDu8Q_FvkymdB8JcltGXsQZnzyOLAialtloD9Ntlz4LUeCC-BmXeKsocfykU7B3aRMSpg1OTo12QBSQG_65bx0Ci_q5Oz1SzpiAgRaMjY39h5_lio7iR7tN-5ULbsJ7kAKH32m6gi8y0yZ8IZo9Qd6W301qUlvUmoKSkA6GLY91wwA1MuTeGZzobmper4h6eC3H_gHwbmMf3ooeOXwHIpmBoU9A7eex6M2RRkEjv7IoeSTVNIKNE3xjFHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23614" target="_blank">📅 19:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UECqLcb2fyo6MHpO1bO3a69P0LLsxvc7y4ywsW8ZDa93SWalGJGYPosdmjGmQ6kTDCMZW3281fwyvipJ46aNzFnOeaHkAy9zBVuUk0jpeL40c9ql24d1gxfdaIWp7W96Usv88z8F1t_hLSRYk9Bkp5S0Ci-mfD0_gjbcqWxzz_wgltcrNTr4n_jly5a_WZdyp_kYF2rPTF7C5kIv_7512ukSmePm8Mdiiz9j2rInp7vpVEauIcbqlvhNXmLSwClmumbYd8Wi7CDXaWoAIGbHevhHQ0Eqd1sDMlllFfUahAHjDOLyMY5Lhcr1l3n_H_Gcc8s1TmLW5crJKPSc7jvTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو: روبن آموریم باعقد قراردادی سه ساله رسما بعنوان سرمربی آث میلان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23613" target="_blank">📅 19:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQejvuAKNlv3Tw86UebrgfLZRHl80DLRHJfzeqv8237i-qXUAX0O1lNOiNMv_6gbKqbNDsXzj7bW5DgsoxooL4dTO0aLxoE8ulW6k1tE3Wjx6kVpiKdd1nS1Eyrg5O15gM_KHLw9LvrzqxFzF7TAvSwc-8uOnoaRwokeM-clCxl6jipA77fI_Bc1O4bmYVO13SsjuiWOL1Uvw7Q3jcAU3eGoxcAXlq36_1cnyJk9ts-W2r39xbD-VWEB1DQFTvAGnuLfYBUM9IFKa7McBeOWhUsKUOsEMinVCyfpwIdUsrEzOFM08ZdNBqj3nDIP-0M1_DlyO8tF18_jgpQBeU5UPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
⚪️
طبق شنیده‌های رسانه پرشیانا؛
عارف علامی و آرمین سهرابیان دو مدافع میانی استقلال از فجر سپاسی و ملوان پیشنهاد دریافت کرده اند و به احتمال فراوان از جمع آبی پوشان جدا خواهند شد. سهرابیان از ابتدای مهر ماه سرباز خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23612" target="_blank">📅 19:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328fe52870.mp4?token=QZLojQ-F7uBA_UPmIu2VXz83vDCFxaXqQ3-RNE7bu6bdvzjn-vn8RZ46NVavuBHn0xNJMBkPeazMey8OHB3r9EQVTI35-I3wZ9vppgewxtRCqN4lJ0UmhGZSoCyOUb3NYvMhgFbMqwsfMwofkPxW9K2F91bgeT5ZuRgla6dbiA8H3HXIO6alYkJQaCjmeq8qU6LKLGCCDhIxDcv2JpRPSWsXC3BdsAhFH4lXzWm-YYyYKZ_8o9Zqj2EN029CKz-ql4ve9rnLfU-qR6Yk7WSgudmoYSpcZBL4IMebBZSALEQVyX7MITG-fjaMOKJ58hzkyiau7G0mXRzf0xHYchy4FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328fe52870.mp4?token=QZLojQ-F7uBA_UPmIu2VXz83vDCFxaXqQ3-RNE7bu6bdvzjn-vn8RZ46NVavuBHn0xNJMBkPeazMey8OHB3r9EQVTI35-I3wZ9vppgewxtRCqN4lJ0UmhGZSoCyOUb3NYvMhgFbMqwsfMwofkPxW9K2F91bgeT5ZuRgla6dbiA8H3HXIO6alYkJQaCjmeq8qU6LKLGCCDhIxDcv2JpRPSWsXC3BdsAhFH4lXzWm-YYyYKZ_8o9Zqj2EN029CKz-ql4ve9rnLfU-qR6Yk7WSgudmoYSpcZBL4IMebBZSALEQVyX7MITG-fjaMOKJ58hzkyiau7G0mXRzf0xHYchy4FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
وقتی لیونل اسکالونی سرمربی تیم ملی آرژانتین رفیق سابقش رو در کنفرانس مطبوعاتی میبینه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23611" target="_blank">📅 18:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naDCnOrmrexrdcbmi8eQG7sHbiGuZ3KfpPziN0vL8tdmKbbJ2JpO8f576IIODftIoFJLXz_KQetvpurk09d-WLhmTne6waMidx1OiQcNsIOzrLECFxVCvbYs6KVBAzEbBAVo8n5JvLnYbmAWkMO63_V7V9ugQ8A8DmKSi9fheg0OMyw9seO2O0Ch0Et4E0dyP4IAlvLLZOymixqRnsX9-SA88QebFIhK67NCqT_A7jPVgxbldzN8DToroe3SY61NS1l4vQ4emlAMhmdUc6XfGoq_gNqPXRhfj8qR-zc3jmhxWYTNvgZlHwoNuwz-aYpbf3qILgBkfGQYBVkqJANNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آریا یوسفی در اردوی تیم ملی: فصل بعد یا لژیونر خواهم شد یا در پرسپولیس بازی خواهم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23610" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23609">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4VrooB--sEhuViHwaH2Srh1C4WToliFjAwDPxx8Ae-3-vHaxuuqZBAF0RmEg-I5ls58-TqZgZXRwt4ER3lDalkDGS7Yh1W1ztoUVgDrDQExQDYSzaLaXhS55qexR0k1H_apR6bdT3718UpFxtt_0CgNuguSOK-2KRiZR9_U1yLQMBKjwH-7BsKnJ0epE5znbIq-vzvb47p7CZvxDQS7B-h114Sd1U4KTJj0F8nthOt1aYNHLpMdjDE0tJAOQMWjWnSiIfgSDFkgjuOE8FeeJdiJXoePtSozaoxJvZ0JIPzU13QhpvEQsxB1mW7QPp-DztqNjeAVuffpu4Y1XXAlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
مدیر ورزشی باشگاه بورسیا دورتموند: چه رئال مادرید چه هرباشگاه دیگه‌ای نیکو اشلوتربک رو میخواهد باید 60 میلیون یورو به ما پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23609" target="_blank">📅 18:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23608">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk1A0BQTkJQxR1l853qUSTelx7jiBmunBgAYeQK1hILDr3UIOE6XeufHasiD2PrPfVWCdS-rkvYyd9sMuVM93rgYjxa7FEDy8YUxee7fI-k4hc-6870XY7Yhs5BLymrrX3KRsXUqf06a18v-yG81BMZQMF1A51r9KkLMeZCwz3QU1iFmB8GEfmXDZFmVIrmCu67KEO9F6M4SqRRzTobp0RnX-eA8GWKtJKcyYWKhsSMR2W1b-ur2tdDEX7VP9r-RsYh0e4GO8HonHuBgASRR0HfVFSV9vsJ42r_yUlZJ-E0NxPqIWQuXvuYmYBXe_kK2r-cBCEw0oPEyXW4Spl2hI5U4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk1A0BQTkJQxR1l853qUSTelx7jiBmunBgAYeQK1hILDr3UIOE6XeufHasiD2PrPfVWCdS-rkvYyd9sMuVM93rgYjxa7FEDy8YUxee7fI-k4hc-6870XY7Yhs5BLymrrX3KRsXUqf06a18v-yG81BMZQMF1A51r9KkLMeZCwz3QU1iFmB8GEfmXDZFmVIrmCu67KEO9F6M4SqRRzTobp0RnX-eA8GWKtJKcyYWKhsSMR2W1b-ur2tdDEX7VP9r-RsYh0e4GO8HonHuBgASRR0HfVFSV9vsJ42r_yUlZJ-E0NxPqIWQuXvuYmYBXe_kK2r-cBCEw0oPEyXW4Spl2hI5U4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید.…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23608" target="_blank">📅 18:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=kWQ0tw-DKU5AoO-nuLdXhFmK3F6vGHWpuIYj6Z9ehrzbQO3EEUzao7NG8bVbDxMMrhgVrG-TFJWpNF64i_Iqw0MR6TU5Lm8sUVhZsHjFhJmqiZZAHGKqJt5lWBhDYhZiw_elCFrcLHVLehK9dpbmUC3YqgBd4fSF2BTZ177m8m5W_Ht6PADTRuiVB9HQi4B1lsGjlFz1XOX3BwEnEwCISAW8Wg7X47W9TcaIItx4UFJ96YwDZUKOis0T7qRbMWZX-DyfYM2kp_NCQiC_NEqKLJe0nhD50hE2ybrtGpB5DPlZSrojQChoNSapAloccuzhmY-tJzLtR5pHdSTDfrvClg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=kWQ0tw-DKU5AoO-nuLdXhFmK3F6vGHWpuIYj6Z9ehrzbQO3EEUzao7NG8bVbDxMMrhgVrG-TFJWpNF64i_Iqw0MR6TU5Lm8sUVhZsHjFhJmqiZZAHGKqJt5lWBhDYhZiw_elCFrcLHVLehK9dpbmUC3YqgBd4fSF2BTZ177m8m5W_Ht6PADTRuiVB9HQi4B1lsGjlFz1XOX3BwEnEwCISAW8Wg7X47W9TcaIItx4UFJ96YwDZUKOis0T7qRbMWZX-DyfYM2kp_NCQiC_NEqKLJe0nhD50hE2ybrtGpB5DPlZSrojQChoNSapAloccuzhmY-tJzLtR5pHdSTDfrvClg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره‌خنده‌دار هاشم بیک زاده از حج؛ میگه بری حج نمیتونی با زنت... دست بزنی بغلش کنی
😂
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23607" target="_blank">📅 17:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuxSuH1Tb7qb2o2sOuOiuMTbKI2oOYOew9uABF806eyhwXyZC54yfGyNhF__85obqW1SsLxjMgWKjZIY7gNp_YcSXjT2fioFTGmHwP_V4SA6FRgiXAYP3Ar8F3W670EavNNbyU8fsLE2uME3lxfErQfTFjyzRItthfTPNrQfKyZsddDSgEhtZXHPKNEoCWR3_7tCuGRicK565MNvVyaCfoFdBMyyqrHOn54PR4dtkj16ajPPggDtkVobyOvdwDkslQS_xkOxW9SRWF0wCsxqAEWNKbj62I17v7Fbv6YRPYLLKDq5_4h33urLXoSaf-OEwNc3S7WhIV-m2KD7Qq-_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید. 15 برابر جمعیت کشورش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23606" target="_blank">📅 17:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JzksSUf5DNfATJ_ASDToX6RRPae_KtpB-ny8PLdOtNimkG6QzRJ_r4z4zv-3qZJdXe3FtmuSa4gen8yeBZ94Y86QzevuAZsLJnQRtgsTYrb46C7LJ85NFnM56LTiVihZtFTVUT13aKWpq9h1e6Nl-gTu9FIhsIgoLDwuah29-_7soBHYgHtNjF6g-Vvp_ECpJrtjLj9lLID2cQNs8HnKRM69QfhQQxoeOkJ8A9LzTsaQD0DAjmbsFeEKydQ1mqhaVGazfjupLAtcPmhlj-UmjezrpsnfoNqYOw9zmpx-81chApn-AWoVw6HPKczJ8npRn71QKMMc-LNmNa7emMjDgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5m_3rliJtnh0rAVLhkzCjNfF4C95qBVOH9uJi4HmPQuJQixg7jD-YRPoZLEgd8OzltruAzLf3pwZu40-jX8cMdcm0R68retKQ9k-KW2pa5cFJS-NNiFAFJE34p6VkBazkSDc-uCIPXdDj4JXxVZbam6yQedvSFjZXaDIBj1aO7nVnDJRDPIX2rco_2cXP5lQniFyKaxdZldyZfEM3hAoPwTg93GXV4QfqzqmbPZS7zePp2i7bw1b4jVSvvBx8PFvb-J2vrvlZs8q-eppBWNtsbuYLU22hXl3JS9HurVcxB6w5-07GxohQEkqCaiV5aIPoa9rS7wCQc5nOVw0mgaZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23604" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm8pF4B9x-199Me9tAAem2jpSOOM_gdF2wZ13Xxmy2zvfi2-JdTSytoQxa2X-apBxG6FY_SLH8DsiedP7wcXch_gnEoTa0_A3YGkT_avP9b7bccI_2ap1nA9bN_6J829bJCzv2_ujk6CSWMDW0wZ_XGpZA3RhqILmrDgLUrQJEbYyAScQZ-BRLrLS7OyKD1reEGpHi-syuibt56t-S51KGB010iagizsjbGp715rFZCNN4FTgmW6d8h4D_S1cAS10xZiC7DIQospYI28uAfwvw7JiOxiaK01JeUSEKdbP5y6mD9rcN51NtmMoy725bJ7Bf1hzZNqg5oSpE5KYY7X_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23603" target="_blank">📅 16:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feMyL0g5mxUW9X56ij4TPPxHcUXJAPRnv-tnjz-3V1IuNa6_OcZP3XoCn67xw-kJwxUr70-m3YnOcuQvHPFwJWiGHXXfEeQtk-Lpm4uqyq9vv_2ulpByphJEjEba2h8mNDVxjGfrmRwr6d66l_DqoHnJJpuc8hwNQhpee0UeQj-wYGxverzS_h5pix2AGJfGk7CpAkUb1xAECr4obq4rclqGMl8WrFwTEecrXVbnsLnKItRa5zZCVmGJJzafd9XV2YFeTVRFgZdDo4aDDgXA30zZRu_9cFaVXMkUOR5jrjfHvBhfTs5Jp52sjOHS7iAM1y6iI2Vhnfa_PZ-XK3RguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23602" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=bKy_ImUgAOOLUUNY_Bf7yQT1DGXuLLt-3k8tD4SmmI1QI9LybY32cJfgrgzONPveUFmbdcMr5egjdhvzlz_EXGvKxLvZUo4CBe9IzoNGqWN4tvPt46kUBFBrelycQd7TQFr5W4maraq-xACyMtqkJwLHLvaMH-jIJXtqVJFyR7lL9Lr2SI6yhiIAQJwJI1PscdoVuHU3hpwIn7FwfQRIWGiZo83U4rRqSJIB0Yl4CzboXixxnHx9Yeau70TkcSK8UGC9pJALocKZj-LhGKVsQ5ATBVdGycBuPMv7jPEPW1ohHkTjurHU_oxZ6Cber81SiXiT9jktCkM9qktB_H4-KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=bKy_ImUgAOOLUUNY_Bf7yQT1DGXuLLt-3k8tD4SmmI1QI9LybY32cJfgrgzONPveUFmbdcMr5egjdhvzlz_EXGvKxLvZUo4CBe9IzoNGqWN4tvPt46kUBFBrelycQd7TQFr5W4maraq-xACyMtqkJwLHLvaMH-jIJXtqVJFyR7lL9Lr2SI6yhiIAQJwJI1PscdoVuHU3hpwIn7FwfQRIWGiZo83U4rRqSJIB0Yl4CzboXixxnHx9Yeau70TkcSK8UGC9pJALocKZj-LhGKVsQ5ATBVdGycBuPMv7jPEPW1ohHkTjurHU_oxZ6Cber81SiXiT9jktCkM9qktB_H4-KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جز‌ ترجمه‌های‌ماندگارتاریخ‌ ایران
؛ پیاتزا میگه به خلاقیت‌توحملات‌احتیاج داریم؛ حالا مترجم: سرویس خوب میزنیم تو دفاع باید عملکردمونو بهتر کنیم:)
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23601" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
#فوری؛ کسری‌طاهری امروز بین‌دوستانش گفته مذاکرات خیلی خوبی با باشگاه پرسپولیس داشته و بلافاصله بعدِ اینکه مدیریت این‌باشگاه‌رضایت‌نامه او رو از روبین کازان بگیره راهی این تیم خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23600" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9zAY1HO_hen2ZSuNozJoCJ-HFupTIiYXloG9IZXlupMq0OwZyy5Eop5NJihr90x9nxzGiNBx7_s8pyj_sxDC6Dd5Ezzy0TwoJl-Z7bl2ax3m4yH_MtywVO898-XXUmr4FU-Nd9w7SnHO-E_hHKbv9VfaR3J2q7bM_-40utbIsVmsZUg1Hd_FXTfBD1BcP5K8a3i69TBOsFDsOJcqw5jn1IrWjHlFyttXx01lEsrLT6eBRYJYvSH8KehlU8-klraq89dpK4DuEeb8BUhc7ZaUq6yfgbjil-8oWZawaklXLk7U-lnSIhHZIHqrA84zih3hYE97aazbUqU37jv2KcUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
تیم منتخب روز ششم جام جهانی با حضور رامین رضاییان و محمد محبی از نگاه سوفااسکور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23599" target="_blank">📅 15:55 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
