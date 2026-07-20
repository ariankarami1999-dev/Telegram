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
<img src="https://cdn4.telesco.pe/file/toKjM-XBPhDFdEauepOrDFZtFiRmSSKY1Ia73S-DVUMkT8h6XVwtNbqIREdD9ppRQZ3SPvv30rj0u5TK7xx13gX5Ew3ksiYYYoxUIS8FiPZK56nOLcSzDIxBQq1eYmZYPpGk0PrERePBGh2US24sunf28O4B_QfVoNmDLgEOnjFm9WDCwl8YACgjInKkX3GIOJGBs6vdHzl8gTtgZCjKuS-Y0lKPOrqT2BbGvNbT_0IZbe8fzmOsoSw08enfUGpE6GdNhr6Ju1DJibp286LdYws3igD4LfQq8B1pdm0flYe4C4lkp20SsT3fdRlFZLKFvU7jjUBjCS7NbV1mG37SZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 22:18:40</div>
<hr>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT5wport7fUSbDG9z7r2y8C4IJ50wYHv9zgcFj4ty2cgHjpPIdzi0ggNtxW8IMFXEqGz8oZ83IdVAYLR439dV4-lVpDzqholPZN-wQV0svh3bNhOgI_kDuCyWrL20BW8IWQ1u27GbJa9ymW7us_X_R9vJ0F9nU11eMSdrPBGeXDfeliVpbnTbGaj6uni70SGc9OPdazAAhr2S7mDKk4Hz1E2wfFUaDIQUwlgeg4zoJhidqF2NNkS8-olefTpJizkk6x8KKQ-_WjI49SU555kPwGYguG74EPdBPK_Bf0QhkDGSgIRq2v1EWqy4_SqQXPMrbcbYtfGJ_aLfyrFpMETHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=WNYvxzFgTVEOA_VpMe8kX8k23vaixagMTafsAy8sGEE8_0Hzlrsdj_lGgL-pSYPmh7eK4wF5ewbaUwrJIhyWQPy1EDotjriEPuHH9hgmbikU2cwHY10qqDZax0rqv8t0kKxDTZ8Mdpm73hb-LrsAhHea6CFUE-McMLS_wpQFCJGAnHHE_4PyR6gum8d-NmwzezE0_BnHfYGHT4RwoWFH64oWFVCwTfOzAM0wpaxjOnKbFT1HEADVOXjnq_KPhkWaBKwpxPScqTQWq6bXAFHZLrmcKpMEb_mOgGdGcMP47FvY_SFOrlA9_SFwBi-tsCjS8yiUH5seDV629rP-nNPdI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=WNYvxzFgTVEOA_VpMe8kX8k23vaixagMTafsAy8sGEE8_0Hzlrsdj_lGgL-pSYPmh7eK4wF5ewbaUwrJIhyWQPy1EDotjriEPuHH9hgmbikU2cwHY10qqDZax0rqv8t0kKxDTZ8Mdpm73hb-LrsAhHea6CFUE-McMLS_wpQFCJGAnHHE_4PyR6gum8d-NmwzezE0_BnHfYGHT4RwoWFH64oWFVCwTfOzAM0wpaxjOnKbFT1HEADVOXjnq_KPhkWaBKwpxPScqTQWq6bXAFHZLrmcKpMEb_mOgGdGcMP47FvY_SFOrlA9_SFwBi-tsCjS8yiUH5seDV629rP-nNPdI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4HeFeBtzhQBAWW2mfKv5TM3hhhN_keeUPeN-z_8DBci-6O8CuVBK6CZnEJ0WUt6QBatQFVUP2Lrby7QBAG7kgxXbNXU3WClEzpL1InDb_xvXTmHZ3hiFEGtU-V91w6VrerA_DbWnSK1s3nPsV_DZ8P3DoEHSBISw5-wvAwxPqhjIDke-NAN3pGYWa18syEPBAIUezn2FoSZMMbhm-z6rMscIxBwPq6l1iXpKAraaKk4vd_SyraJyx77aUNGTrvsaGmj1WqHUrroM1PA0abvrD1K7RGphdcUYlhYU3CC--6CY2z2F79bYMmqb_yG4GVtuaf7pOy1_l00WZt67Td2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTDEG-_-1ckq3-P6urZ2KnwbYNW6gN4isMWa_QGBM9-GXX8Cq5sf2VKkoe6rpJta-S7L7mGVqKJ90hjJOzSIXRkdr7pq5V6Y3DzyH5bVAFoAr8oyl-kbSdHwHiaHG44MU8Wwi21_Jbd26vQFjwh5KL1ZIMxcz6FRyjG6YQze0CdsouAr2N37wMLHlxqjcfUEwgR_q1bTJf86JbrTr6pjTAIMQcqYif5IxjKLLHeN21-4z1c1GYy_PIkhcnn5HA8bzpZrTwoUjhv-Ka0KQSccmswAJeq9JsEVsn7niLuHx51_QnvSoNB__aI1glgtXbq42OL9pS46ZZwvLKFcQHrN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLBQwS9JAplo0wbukOKW0DqSG2TNrn9ijOkl5KoGNMwAbUOLNSI5Yh7tvjawUH-nHDW-UnbI_8D_82oUjydbVmSOGa0gOfkXdPwsFPaNbUo8rMI7nmjk9VgvIC2BMRKPIyLJZclO7ELbM5WGNQJFocZVq_HZlUaLvzM2pmC7dp1_TeUgtfpOanVvNieWuZkfyMRT-PNb3CjGikY6JaFrg24vgvZiiOgL9Bs3TpDoBGv9vSvzYKo1mEtwnUZCp9MAVNWr07-stf_X5sc5jxbh20qJr-cF2LT4cBaGGIikYXKSpQhXD-IW7p32jAy-UY_q_C2CuLeVvr_r8rMqqeG2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebqqgFHZl14cDl_aQYn8j2DV3w9qpJP1Oh2r6maDOzMM6G__zwfFrkJR6fjVPOck3RKYRfsAtg-24kZ4Q6ye_ItpeNGSkocq53b2RDivaBdc1chYnpaFaEPGLMtMiaqemlzK4ANsywnENMSnemPO8-3eAIfkybUTOaA1-JM91qGVmChBva5B-LnvfHkV9UNgzSgLzRypEq6vx8j7HNgXqnQNsp7Rc2hyPrPUTxrqc1aYppPOQktiI8Aaq1-KzrnUCQDFakbKSo3hfvuNAGwCvp9AeZ7QEYmBUL5T-IuMEbCr5WloFs53ZIwo2CWegZdNPunxlS1z2ERzkXZiOwVtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM0MSqsHGFLHU3HWnJxrlC8LzXq22zgqVqZ_mNLGIWwSg3fYVo6gPC8fLyIIbc1qXzSsOinwPTMM8eYlWsuR46OL9cFyYXxLWzccUoP2rRm4XVKExUSahWNSY3NDq5SjnT-uG2PwoZ5QGKZK58ApH4oRRlEPTBzQ0vhj4xOq1UxneVaWcodZzdbOm4Pgh0L95DGyChGM8-dVoxtwtmkHNuqpbRLnKjamUIyW8DBQQfSnD45ui-7FDGq01_NJKTY-IDQYJvig5_JHLHoRnO5EsHLiShqZBnx22sKAq462woeysKArNAabl6Pbz-fQrreEfWo45d0TZ5ODhEKjBz62Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmfRnNJlIPjIdV5eNBGgB-XzM9NnRfUQHKxDP1r2-jUszIumufn6tS7ADKEF5J-dfcPmQpWQrdpPemOMzw_mUs2Y--K2DhtHJ4meZKSDxCXN9FAHKdxgMXrLFwHVcXUC4FhBU2mtYlDQ0u1NcM2GjhohWzn2hdec-W4cLT2fT8K2zqBwrJUltkOuNnc1vqy-oLzDdL6PqeHXLgKLpkgDN_t-J7M75iVRZnDlaC0_xBNxD_Yjy3qsEHS56kpLGR9TrdbEIHMivsBehX3MuHMHstD42uQGZskjZ8UP74Pv3zLwmsnYcFjLFyyXgZoG0DTGb8CgiPrGxJBmKtUtEafSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT39W1SulUzaD2SjX5TC3A0-NjJr3tfeOBhR28fc_m3oqknWIKn0lv38yfCrpAZQTiKntU5d5eTweUCPZHgkc8WzkjwYpqpwmEEzegsfpjbHWvPwL0SM80d5KVNc3AZDv11e68PTVsV3oknZUr-VthkFU5ClcKLEqglAn8NRY9LPVvrPh9nz0mXK5rjU5i5-RI1KLvt9F0M3tfHFL1ihrwW7YEO3aV4RwbZT0A2arieOs3o0PodkHapVHzpOLUWTy53oUModDmWfYuhWGDTRwP1PKt7zPFZWrjSmZVVv4iMMFwv-z-bjU7jsw6myHLpk5-22GrKtaD3L2FjZUyJrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=sfjELI-Q81uLhG5oJ1GW1KRbzGK8pynJJ4kCGXxnm2syrYj6U-tbATM5a-4YcY8qz5j-1NBNhbRKIC_ffeDwpeRVgODBk9HKvbvzARwU20avh8hoxOQuOqgLsNNCJwQHer-keSZ0D6n4Jr8LQDxkpPGEK7XQmEQyWg96BmMLjmUSajBedsTVMU_u7IrUAtTYViBDO1573F2z3zjxjHx3xOHBZlcYxO2UqsDbRo0WtMaDLomKzqduDc-Zyah0NFDc2ttLDiA6EuoUEDogZwqI4j3bjdQRw-WM657RhzuJWl1XRvXZ-Jdbit4won_vqLpVlxHmBCirp2EpqCXhOpcbjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=sfjELI-Q81uLhG5oJ1GW1KRbzGK8pynJJ4kCGXxnm2syrYj6U-tbATM5a-4YcY8qz5j-1NBNhbRKIC_ffeDwpeRVgODBk9HKvbvzARwU20avh8hoxOQuOqgLsNNCJwQHer-keSZ0D6n4Jr8LQDxkpPGEK7XQmEQyWg96BmMLjmUSajBedsTVMU_u7IrUAtTYViBDO1573F2z3zjxjHx3xOHBZlcYxO2UqsDbRo0WtMaDLomKzqduDc-Zyah0NFDc2ttLDiA6EuoUEDogZwqI4j3bjdQRw-WM657RhzuJWl1XRvXZ-Jdbit4won_vqLpVlxHmBCirp2EpqCXhOpcbjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26152">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVWwYtqce66Up02mZbMO8WwkhqOZwSd_3dUYKSLFFziRNMcCfYWWYYbCa5TFKc68HO1K3rI4FJpB8O4nX_-1A6gFyqHpMqf_8OHVm1n563sKdbnQIIeOBZ_sVHxkU8GT3TVLuskOP0GW6baVTETkyPzyiKsFHfeR86QbM_vSviY0CbG3vO7t82bMH3VkyCvb4eOV53qE1aA6700LBWt7d3Ih4y1HyMruqXXn1uqW--z2zmGmpk9nTNhCkUN7OYXvfv3q4vyBRXTZf63x0ij_iTweIFKqbD4KV2RcoAcFfGjwm1uqwoz5SqzbpWus9aOfudNOYSh6yXPaLhYrXw60dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/26152" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jN-i0CfJ_YCFBMis3ucrnqpkx7jVRb8doAb1JgIoDebFc-X2p8HgUAdDsqShIy2zailyFQUn6Fty_upEZzczx-PT9G2clRp9cGnxxu-38Kl_3h589T8njKQ9K5HYPVfGgLzKoddaOuf8U0KzhgsO94GTTc59PyDKUHkrbAnUt7s4iLiVZud7fhpkVnXZymi8rGSTBa-z_s7ylef1bgrq7vfb5WW2Vd7zZ7k54we_YqWDh6z4TeELUyTzmGFZPO-b8CBX44yyFByXVA80qOrgGsgXEuBO9MRCI7GWwtToVFJ5Wla37gNIDJxx46fOwNg33J6R5g87TrKhZblkgj3eUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_zMz8EJkDzHF0cVYq8yYTTndy9zakXdVviRYjRXNDSkKESs9oxFjqmKFV5Mma3KkPr06z9UxRICabX3sXMBg6QhpLbIOAwOFDdiBQnQnjJEaYv6MXKKbpmA46TI_tG3ersSQwlBej25HEx_3WroBNKEunJ3gkOv27XdEfZY6hjKDcqwaiZLx6Il60rX4-kvYRFxoIVjtdKxT01f6L0UqQuBTCqbOxjbVnADL_Cn5WvbDrw4B4yvHmrAzbTVo3UmLXsDZRwfD-7lvoXgrUupnxRPh9lFPK0flBPejtJtl41thy7he2jtz0LtAUdSP_VX8PFhOYlRYamBLjatI6XN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=fIPsuwmWoYM6UEpL_Q0-jTAw_RvxWeAOzFQipoPxQuaJnKUE0inX4YXKBslwHtIRukn0TPzASx0iRd0PF-BuHUBQ409xnUyLHJm6WhKr--e13LEKUmd_5NssXQpaE1lXxipoPn_5_P103GqZDrYKE8f5PSH-IlGKpQ7_QsVCOSP80y9I99LrN_x6u9xy9NYcjy8YpaOLuA0fkN4Fy8SEw7K12M13mmTYlf7th3j950jhMcvv14XbpdX1re_W-pCnY1jnHOBt53IvXDKHh-D4pROEi6gJbPFKc0OSBpDlbVbaz8A4slSChP209FCAzJgn-touC9DxJy1AXqGsslJr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=fIPsuwmWoYM6UEpL_Q0-jTAw_RvxWeAOzFQipoPxQuaJnKUE0inX4YXKBslwHtIRukn0TPzASx0iRd0PF-BuHUBQ409xnUyLHJm6WhKr--e13LEKUmd_5NssXQpaE1lXxipoPn_5_P103GqZDrYKE8f5PSH-IlGKpQ7_QsVCOSP80y9I99LrN_x6u9xy9NYcjy8YpaOLuA0fkN4Fy8SEw7K12M13mmTYlf7th3j950jhMcvv14XbpdX1re_W-pCnY1jnHOBt53IvXDKHh-D4pROEi6gJbPFKc0OSBpDlbVbaz8A4slSChP209FCAzJgn-touC9DxJy1AXqGsslJr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIoC6dgeHCxKfcGbldjQKzc1w7B8fnugWuFkXCPz8xQphTh6iHNrN3BSA5uNd8JYgFa0mJ2pIFWbhUIYmhVgAtT9CFIukecWcQnSNCbiu1GxSORUc4zwRgHdT8_BDM9ZuUcU_aB1zhcEdiyXhkBG5b2hPxDSLNfZzwzQHmhYqM1CGHPxlwwheibmKPxPGuG4pt6Jy7-no5J9d2n2GDCLhBQdKBaPiEsatFwRE59mLpdsM2OHSsiOiL6k8d8F8YSJ6QOrpBFOAMEiqNF11VdpA6IYkBhJBS-OSveMemvSKoQHdZEF923uBdQ-pyBVUCp4P78XYetlta4uX_cU95WuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX7uFQo1ZBTrj0BJT8X5rvI-IgOdtoaV6Hr6P2Nyg5xiDF7oIVuuLrtclk7c2GHGHkz7lK2Uv-Qj9drKk2uymTpzX0hWW2sl6E_JeqBXYYRVoOy8HUof_9fFZBY4CtL0CnGFMXkawZ1zrawae_rvIlD9ylJ7mUvmmTDNHWv5XLyKWBbp79bDf01-FLicIs0dpFVjfUxBIo3vJa2smkpNfPJFMq2zken7lKJse_un8y-9imbKRlFZUNREWcF4zzZM1Z7vMtlunv_vykWck6yZuR7PHpRYRK9VOa7uVS0sb_SpgIzSFW7sLkWNB-soQWO1d1YlHJd7d7_kyGWDWf94Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTjGHNqhWOeeI3A6b6i6FHhDVUkdk4ijHhtqI_wQIJKhE4ZVlcQhkcd-yVuYHH_NNE8lzGhiK-yEKFBh9wDHXz8cVHC6w0ECMdt6d4kLvH_tWoq_6FyLJwnMemZoGxbu12pfVSSmjaU6UKab-gjy5xdbcKe_UdFFCma3r6Jln0eDsBOvR-26aSFLiVxpbuM2tuVYLaUVkG5QODkK-KWnwMrgAzTRv68QRRAetbvCvlm5cir98ImR2Famh12m-BzQv_yFan6AKtv2AH4w4GTP1DqHBlvY_9SjH737Ao2sJ36Cpkt8d2TqZhUDydcEcJQrpBBGpET3MnhUNhq5aoQcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGvp2S5wMjO7KFhkyC0EDBYw-TZaN11NYOIWl5rDxOedLFz-6uPJ0042T4hGJrk5--kh7IiG80ZEcH1zUnqPcx8lrbI1IuYvmO2vaHK9HS--m49rC54olv_veEvZAopRwnHZ49wa2Le0SGEJDzErEnIvZ7EftYXu7-DCZmvM2O5tGk-5SgMTWX1pz0KYQaraZExyao6dC_fafOEOPirmnrdoX2Eg9CIErh8P-aEp-JcoT9OG6eTuu2w0q-YWSZAHRvRB24Lc8_lMsLwLcW_B2OC8VprNqsjZJt0IJpv73bqVxiwAVqjvUzXKJV4cUyMlTdfXw8sN2CqSWq6-Cd13zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uCS4Ry7XmaOLr32SHIlnzPWXKkrrCP6gHYisCsMp2gqFvyGe1zpZqCb_w237-n_jXvEZhLu4r09Y9mOTr_CI7ljuU7pMwJSYmlcKN-X5AqZ9uSZh6dfybGqmLqnfgFFzIky6Er_34nm4QTnfQJonp8-2w1TimImF2HAW5f5B-bm59XUOscRRlxlkIetpuC_879tyilPcf9SFiNSHTnmYQI9LftIbsuNgUyThLXUnEzYQmzsWWSKE3yccgKIsdhQU_vsXbsoiTOJ7osXxFf7Z0XCnza9eU_MhojoCucENp8fBCqMjP5B1o4zZVsD9naaAXvZF4MGTIPe2ZWPmtI_s1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0uTaeHKH0BBcQno-o1TsyjAV3vGQSJIduWSk3G3nyC3ddPdYhT5WJiQ8XOEfOrnWsq7tHCt0DPxndY1SUYCSXeJ7te1k4YdM_IdYz9vkIqxNKft6dSsQ5WJlxRy4vkN4VPR71iePAy23GUtffNcui5uykWaa_BZfekCwt6Zn4i12OZ48M_Bmzmx4LSpRcKtLIlk2LG7elGIl7NLs1Y8RIBh2wnyjs3TsELZmMFuiI1NSoqUTAhjBUvMzeCv9ZL-8jA5oOu2VqrNKHPiZ3TzvUaA6E8a4p32_ye1TE-KkE-jMzKA9thm0sPAqAPzyyvXBqz9OuufYKlm4dLzxAjfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP2mqnFRuvaGcGTyE7KHhwXMQ6fn3JTtUScBgIi7O_fBIbQej5tf2qBbEU7kNYCSU8L4VIQAH6m9q_vpAjOj_uruom2pmcy8OyC_7jutdUuJO-WsSOlv7aFQJz9OzMSoI9n7Mdh1geKlYVef8kIUJYXKrywkQWLpLHqqTRiqJrDKDkgYzuMd1Dm8G0UCg509sYcibsRmGBPB5_qp31QCnzUU1njRYRVwTR3UE6B4Wlj_LRPLE0U9vN2XmOXVqed4PFYHtvUYr9VglX-XRvLnwhfrvAHdteKcse2Sj1vGIxiwPxKsfrhYyPLD2lh_AmzTXKt-KQmlhrOjbZ-TTtiklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7AHnKiw4uN_X8TdLiK6WTYmy9Npb6fP-2UMjM-sUDiFjpY08D82rt8ipjcM0IdEq6qsTVJ3-c46DeWGH6hyRNbVcwE7Q-DEPl98e2_RcLsIqtKoNBFf1H8Ktoh4e61H-80_kosfZiUt7mw41biMYEeKFWqFVWmDoBPrLWBt3t53luaNkaj4y1zrxUvzynh356-OnBh0Jn2IKHjLMExWcp61dWeE2ZXdLe4DVTzoca6RfNtU0xi4Q1PLJh32GmBll-j4uE_Dzc6pQrqRSKq2HlsO5EGFm2cRqak6n5WxSAMDBkjaBHsv1EVDhqf4CsrZ7FX9b36fnwcu9t0rpRUUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=CKOSpK5svPRufI7wd_EILiGHOr3ASL2snGgFkvfY_TzLUQSuhyCxHhziijsOmmke4ar0HZC3XZX-KmR11vyBoA63tZC9O1AXNxJBOgkYMi_djl28QSLPdi7mHXZvGpL-GE6v7w0EjvErdLmtrat-K3PQWtxF5gScKrJPpZqGSYU2Jx9jbPm-iah3zHV3KH8cBz2LMgRCqiSqylljn4dex1g_psfFmo1qap4IickLAx8RoUDmgGkvmOjRgPs2FhESQ3IzyoDXE_oQp_Q7Xq8Wrv5iD6XoiqovUkb_DZRP94a1lv2e2sGAIIZkVsy5unBjtPYJlV0dNbsh1U1cXrXK2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=CKOSpK5svPRufI7wd_EILiGHOr3ASL2snGgFkvfY_TzLUQSuhyCxHhziijsOmmke4ar0HZC3XZX-KmR11vyBoA63tZC9O1AXNxJBOgkYMi_djl28QSLPdi7mHXZvGpL-GE6v7w0EjvErdLmtrat-K3PQWtxF5gScKrJPpZqGSYU2Jx9jbPm-iah3zHV3KH8cBz2LMgRCqiSqylljn4dex1g_psfFmo1qap4IickLAx8RoUDmgGkvmOjRgPs2FhESQ3IzyoDXE_oQp_Q7Xq8Wrv5iD6XoiqovUkb_DZRP94a1lv2e2sGAIIZkVsy5unBjtPYJlV0dNbsh1U1cXrXK2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvDEcUz_fUH0n6_nx8ffQYlY7LvbtZct-WdPr3fEUHbuAPs9Yi6BCpoFiCCZSuuX-Zp61t-yu7DVTB-HSC-m6DED_4qytyqn-3CNSsavSLLKHBQm0QRvVRIswRyUjW4mKu3SsyLTESgQqtvReQq1aJ-XgeLi2Ml1Fe53DxoaULsIcN_i2FhIHN7jJyYyHD_vUuQ5xX_L1AXLYRs5INK8uck-dPtrEn12hP6oTmAK1OheHw-Wj3eBGHcRhOJu3WsVi04he_3Dd13_h1ToBSvnXzqxjmxwYQlsQ76rSo7krScivKzfN6iIEIMJIDROJK3MS2CZyAr3lGr_qY6xAAyaRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCwkE9o1RKfS6CpYeomCc4Zv3iaYykDzBXzHWvuUCbb3zcdT64tt4t1gOFFMr8HgnV74OYtp3B99ggrpJuvod46aKZsVJEOfE51BZCZlga_H_EyFu_x0fD_4gYn0a65XA3CZre003IwayNHv_2DjPdkmNSmDphvvgpKlu2_UOY-TX1-pZLM-p2t5QGAIDTfqF9jmMAxO9S4BOLfNkhOWc4nfRhK_ZdcbVHipPWg_hGHdVYQQ9jvDClT5wTs4mhh5AEBHMEx5BhxROHy6Rfch0NE0CkhGOzB1GSxZFMnGPSdlRyWaXeRz37NSSI4kxq8pRy-rQLawQDl-sESCCLFR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APYGtAdOhswalnOnxCrktceodBX-bG5sbHqG-2eEnSzb9dSC2bh0dia3VPmpqB5cX8Tl1wvNO8I-sd3QuS3FwDYl8pnlO-fCdcuBMiqEXhYsjGQe2eKLr3BxpGJ_9KbRcTae31xQTgDeU8l7Y45wMXh6m6y3Zyut1NVgS-QmmVmlcfoXXALDl3plhrnRlTfz3wGgdC3Qqi511EoCcFQ7JcDkAdlkdZB2hgUHkaoC_ZKywZrv6-0s1lz8sdBIGFq68Er6CSDieFE2z2_nlJ7L1rdNAwIPyigGxqBwspeIbjbQ-bhACDQDX6VEyQl6JlwkToJT2J3ydGk9Q4yCK-vsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoK9RY7ju0jQvcd7zdVMcf38-bztb51jQRoLViC9b2cNBbNvxGDtBYTd633vH-RnNaMSS0ImYnURHNvXO1hzVq5hNaA5-pJtYAz_yPpXk6rJTtS2A-StaxfIC8ipNwa-QWBv8sXFoWIX891bQbyd4drQzk7AgWDwaTznap7RiNJ0sGeNWWLwlYzT5LCJ0aCsNiaW5Unw-I7z-GtE7TQW7A9NKF6-cjrxciahoY1Vdc83DMR7q1sYbe-bA2f14lHY_TmMN5vDcPZoZ3iK6czDLyisKqNEWvc6BOa4NftSMTMm7v7XH7IDRediq6HLuZx0YZbz-sq0t-jaV3dkpnJzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3393A_I0iruLGflphJsjrntZOvlRwkWR3t9BTPXjPffhqCT_a9V7W1kwWen0dikJT7GLuIzN799n-xw586SOuU5i0zLiJY_5OOfK8RfrbdrmM4hDhDdNgLzH4WWYZp_CfWKC4bEfoaQXZXnjEqvee4SKwVxu0BN2L5zaNLRp6zp8eT1Cd76oEo1Y8KgkoR2_F4fpSh3QAtl-RNccrYzV6_89q0bgNMDY3v35SpX-IO4bu5zRcnsJZafr4WrfQqsS26B1GQNtsrym3JFtAJc1g-nGm5fSoXwRDOD_OkmmpVHpdDHCpnCsUpxV769FLelLqyynrPWzGBXg93y83PD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1YrpIiGUnW7bhdNDANHmA83I-TGYup59b3V9LW4xGWZZ94sM1Ta04a4awx5vjfK-EoT-RLjNt7ninOz8XtwWznOGsYo7DV1wxSHbp7PgmnffVTjb6gAeuld3IkM_4XOUIrzFFrzRBPKTd5uIbPQFQ7doy69pG2Iv43K_7ClS0U0EyzRsDgIqhVCrKyhSAlrUgBBuFKTiPfx9t7__3rRbZdtJ9Cdfir3u2wRoLnDfmo4Jx3RlRm7PZ_ZtWxU8yBQBD07zOp1hWi_f6crP5VAnAlUb0ezSOVs3sDwUCEfrDu_DMEFaP-3lzOB5AAHzt9hoprwhYVRxGa-KinLVLYiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnJKBx5QNiQZa0-gOi7ncH4E7BBAhXX4oLKKfI6vfWRmyojmjDOg2A-s28K2fTEeYgQcukmpbvbRfsKQ0jOimAOPGSCEZTOo9H-qMuVZKT9wtKuQG3aUlZqUazKmDtOXueW5CqfVQfpw5M2iPsY4rMfoAxZmmYI3G6M4vaxJ0Bg1PszN9tO8AZJJ9pVkpueZHSq_4wYTzWcBcEIrJyk_UtlSogY4cKaMUYA6VEkV4Uz58ZmNrxuQy2DaqVlqhkKgF2IF5LR2AbFWgGTZAeen_qTZ9h1UzQNeJ3sZlb3uZ-tkDFh9B8zPRz0bntKvqoIZGddo-rxHHCH86wWN_qxiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJh0UAFg_TGlDGnO-XukBeCBQytQIfQ-fl_J9IaF0cjnlxlTpFdWCfj-C23bueUEEQYvaOyyoLdOYS25tmfDogtVfdpxkjP3GXziWdMhDXcuKEdb_rqToDocVlM9pw8c1JV3ifK1LZ9UVm1ePSW9OxLlBRLQG5vIwBZAc-xr8eE4dqemX0JnRx6iGtZQp7enp7Pvi4TJXzS9UgIBOlZ3T6mJDH9C7AtynMKYUBRkkp9_nRFk8lUKLI4W_kP3GWetKGy3G1Q0ex6tTWmMKjfNnRmV9fJfBNPqR7o6OdmNuBry7w56_DbPIYy5W8BPrnXQlbtYjZg4k9sK4nKRk7aIvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLK7ap8wwOQ8D1RgoiRUq-vYRUO1i-FR1ak26z4Y9h68njHiowpJ9a8f0G1stbb-cFRX8BEzxbKEJ0p7TM912tlO8_nbeJ9zen_b030zLHfCu8WIsIMEufJxgrAytq1VYY_hROLulT528MYBDuUA_Tez8bqnYEiKfMI-PUYWppKbrmK0ZGjKVCreZZhY7COF7AyNa_i2C2XuXhTnySR0jIObhBQvG5E_ry_054H8En5zAWGsWP_YbtKlh-VMw1Twl3-mEvg3BucWQQdJZtnkLC0yOSco-mjckUkioNX41ES68sAIgD9DPBbS9H10lCbmtyYH8eDku9G4I4P5_N5dAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2kuBxQUZd8K__2U8v7yACnslAtjbUSrIXGpWHk9H9YoiKmowp4ucQXeqLx6aNm2fhTh9NZBtf4vdKbuejgLkGHAhINl2uns4yxSGiuJ5y617QTK7Zkzx2DXeXn31cXwpFPSjZt1qU5_Gk0joaeq0R4Nq2RZSpXXkJ7iUuLJIoDD4bFh89FUdorBSVgoWgVMxlr56QRWf9zkpD_yhQQfwci__24FAhfNT-HnSYKwGr6FD2Bbd72HAlUXK1VKO1L44-Hdun2rdPfDIYaPwZeRqBN09pn5zqAmJEhcOfRg2XCs2rzvCnGDwy77u4TyPGhoBZS29vbwwBRcDh5PE7n5fsUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2kuBxQUZd8K__2U8v7yACnslAtjbUSrIXGpWHk9H9YoiKmowp4ucQXeqLx6aNm2fhTh9NZBtf4vdKbuejgLkGHAhINl2uns4yxSGiuJ5y617QTK7Zkzx2DXeXn31cXwpFPSjZt1qU5_Gk0joaeq0R4Nq2RZSpXXkJ7iUuLJIoDD4bFh89FUdorBSVgoWgVMxlr56QRWf9zkpD_yhQQfwci__24FAhfNT-HnSYKwGr6FD2Bbd72HAlUXK1VKO1L44-Hdun2rdPfDIYaPwZeRqBN09pn5zqAmJEhcOfRg2XCs2rzvCnGDwy77u4TyPGhoBZS29vbwwBRcDh5PE7n5fsUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOLsB6WPpjq9BAuWHj8418ske9DcMGdIJo77I1g56cm7M4XK1HS0gl_ye7IXJP_OWaAY1r1qoK09ha8NEqFjE93HU0T3WgW7iItUv5mW-ZAbAwcAbArnyZUiaZXjZiBUnarvImhwxhEkhfwSjm-Yt5TSFnHq7RkeFTI397L8cSvlNzqp6Z3T5v8_HRallw3WoerhQDIc4MfxlMTbEFTqGuiBFfPjMO3QiAx0rXYgaHx2ObK3g237SEwLa_6XMSfn559eNAq_uQmYDnQqiyP5wrsWJLhaqg76CJNETEx0ZGlVy4B1WcSljKc07qGl5vkhug01UxRiad2jM6i41zLpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=BatjpRam30fxFvn4gPZHa7HKFvljjVJsUcG4CiLswyUCYIbmJ0ie90sX-sgv6CA6Umi4i7WDvKPl9DoyYqCr3vjHAjye_Zrp2-EtiNIVdEOSG2yQBi_WheixAe98be4TLXhfylve3hamsnJVigzZQ7cDuvyBIsjPYJ0O0cooVPtS8e1AffkuPaXfzF253is4GYhAXB704G6RHCplvYLucPCnYLFAo4TbIAEnMHeku_2dDCRZ6W7zRnSV9C2m09Ivppyfzy5IwkFy9CpqgCap81xDImfVngml1KD2iQ1wVkSATGDSt1YAEgX0GzD2ZNjROzAQrsqcKIC2hbV53pWbPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=BatjpRam30fxFvn4gPZHa7HKFvljjVJsUcG4CiLswyUCYIbmJ0ie90sX-sgv6CA6Umi4i7WDvKPl9DoyYqCr3vjHAjye_Zrp2-EtiNIVdEOSG2yQBi_WheixAe98be4TLXhfylve3hamsnJVigzZQ7cDuvyBIsjPYJ0O0cooVPtS8e1AffkuPaXfzF253is4GYhAXB704G6RHCplvYLucPCnYLFAo4TbIAEnMHeku_2dDCRZ6W7zRnSV9C2m09Ivppyfzy5IwkFy9CpqgCap81xDImfVngml1KD2iQ1wVkSATGDSt1YAEgX0GzD2ZNjROzAQrsqcKIC2hbV53pWbPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=S8hRp0qcDWrpV2rzGrneXc9_A63sTLlDQQFMIXoepy3EI6ewmEgDtMXExLm5iNij_znXDoexOySOAdWBFE73xXo3MVAIQT4ixf2bgChJ1x5p94Cs7U8v3mYogrb1dX09ozGK4XCZgIrtVKpFi4tDQO0hhodrixpaZCcQOgXka-lBa2w7Al3X6FXSjpjsuwWjMsSw-dMgB-W9_H4U_PgS8nh1Np9m3TZX76Sojgo3RplPzKrgwlnUQJSpp4sMmTrgFfvwQVs_-e_NT9aIz-y-Wn8DXS1Y1ahnSfj1ovGe3SOd3jjWJToWQzIUJEK4UGdDO_quPHjfNTaBt8TCwqIm3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=S8hRp0qcDWrpV2rzGrneXc9_A63sTLlDQQFMIXoepy3EI6ewmEgDtMXExLm5iNij_znXDoexOySOAdWBFE73xXo3MVAIQT4ixf2bgChJ1x5p94Cs7U8v3mYogrb1dX09ozGK4XCZgIrtVKpFi4tDQO0hhodrixpaZCcQOgXka-lBa2w7Al3X6FXSjpjsuwWjMsSw-dMgB-W9_H4U_PgS8nh1Np9m3TZX76Sojgo3RplPzKrgwlnUQJSpp4sMmTrgFfvwQVs_-e_NT9aIz-y-Wn8DXS1Y1ahnSfj1ovGe3SOd3jjWJToWQzIUJEK4UGdDO_quPHjfNTaBt8TCwqIm3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=d0-ezHgGbVRe7FESMe1xz8qqqVU2Ja-sul-avHOKDWsljHBgwO036Dm4qH_gCrwVkVmZyfBO70AyLB8Q_-liy7DI3Dw8793x5YvPqn62F-HVZJ1mUibYWDScYkzZU3Fqvxuh4JyzxAoXx4UmrQTQkFAgUeDYc67HkJOwzJfjJw7FOqT5O5lv7CClwLNDvdpl7I0969d5fFpdqM7q_rldaJBNzDaQtVNpEFBuFT879_SVdDdaHd59yJU5VsuXEgow5Bgc5dmN8rEPukS31_8nbwEXNxHS5eGXhr5Nbal-NRDmrY3mQgLa_p6N9hV5pSQulhlLkeeMA2j_cLNTZiiZzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=d0-ezHgGbVRe7FESMe1xz8qqqVU2Ja-sul-avHOKDWsljHBgwO036Dm4qH_gCrwVkVmZyfBO70AyLB8Q_-liy7DI3Dw8793x5YvPqn62F-HVZJ1mUibYWDScYkzZU3Fqvxuh4JyzxAoXx4UmrQTQkFAgUeDYc67HkJOwzJfjJw7FOqT5O5lv7CClwLNDvdpl7I0969d5fFpdqM7q_rldaJBNzDaQtVNpEFBuFT879_SVdDdaHd59yJU5VsuXEgow5Bgc5dmN8rEPukS31_8nbwEXNxHS5eGXhr5Nbal-NRDmrY3mQgLa_p6N9hV5pSQulhlLkeeMA2j_cLNTZiiZzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APoNorFz19Zx0omaVy2-5IsmmQKzwUzD2mhi8HP3rBTmhwr57UTORLeV1HrukV9zFC-seCLLP4iNqOu20lM8XHagM0zQnrfU8fFkvsKBBH6fLl-q-rC1OsixtNMMxI8OofScKFKp1amyVWizEi9DyB_EywyMfpghmNhHSv69jp5A1-XE7c05MdSKBMRG2I6tEEE6tabT1s3d_ezok-sETwCF-tSB9-KjQDZpqV3x0hQ5iDJNEDPBxpElUAyioIeXZyqEsK-ngx9RXWuyFDg1L8QfHbZHB3P1vXzT9qqxV7z2zQhb0xZwyExKBnwIeM2LToNF_v1KYFroDVqW8ypynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PWaHa3ozubJOqc0JGev7QqCvrN8ZR40p7kJGMGs1o5H2bCv2p-Ss1BF5lS234P8eUCW5r5ulmdS2qTCnQ66q1pUqHVKRm4O9PjMkmsR80PCvfmse2HZKl5_SH6kgdGIL0R2_nDwBDlptyyUkp4DLu91orqMBnF5_oa8UHGql1ZWW5U-QCeyti3bOzww-l28wZDPvdJFHRKaSO4zfmoW3_DmT-CVBl_hqiWIV_kR7PRNzUwVWY8Yd_beAkkrbn6gKTAlZf73qY4t_7pTj93cGaP8vRRq9asf06QXRzsyzLKjRBueteGKmiAH9NaK0WGNLzZty2oDQkVbhHenbhYoO4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=GUuYSd-2e87gWqzYRWh2Kl6hs9XXhqO75GdnpIAVSwMMkqassFsyyaBo52iqTQcGBXtnJ-JVfTYv95PEN--4_H3lcTjSeELp4kl_U2ucdQHNQggtDpPeqZzvc9Ys7z824BPOAfA77q7apE8m6yq3sy-0yADokIUDWPJMstj865hSBgYyJrpgVJK5f8EXDjabQgT7FXqW-UC2fvyqx0uK3z32kHxjBJp-ON94OblgGtFJezUsOD3-yGtzun_KZ9lEBgarw-UTOEcPpcnBioWB9nK18J7vm8ww-Cc5h8C1Nk3kHOISPm8b9E5VsUsfHqQFhD9aF5T3fElyyYHsYQxGHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=GUuYSd-2e87gWqzYRWh2Kl6hs9XXhqO75GdnpIAVSwMMkqassFsyyaBo52iqTQcGBXtnJ-JVfTYv95PEN--4_H3lcTjSeELp4kl_U2ucdQHNQggtDpPeqZzvc9Ys7z824BPOAfA77q7apE8m6yq3sy-0yADokIUDWPJMstj865hSBgYyJrpgVJK5f8EXDjabQgT7FXqW-UC2fvyqx0uK3z32kHxjBJp-ON94OblgGtFJezUsOD3-yGtzun_KZ9lEBgarw-UTOEcPpcnBioWB9nK18J7vm8ww-Cc5h8C1Nk3kHOISPm8b9E5VsUsfHqQFhD9aF5T3fElyyYHsYQxGHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=g_pAETdwO4mHRZ4pQ3adOHm874dBvlI3MA0EWGL9jXCaeVv9oYDwxGCyflTRMz5hsCHH1RtUG_m7-aJcrGHA_W5SIAsJoNV2-hKArBbgzc5HrmOzHuMKosBhg6cmS3jKZN-sPZ7e-FnflaFTFPpMDfbEc3jFrk6s6HZ4Rf3NrGF4HD5T3hGQuPbz2g7-q4meq5zPwG0JpeqkeAlU9_b1sbDTNOQw5MBf0dltW0h0FE7G2pqBvOVgos5mnfz-fBGWkksCk17Bp4hEbYK77C2FEkxBvim0Lzn6ljn3BL8QwH-XJoCPkFrqNaAdrFkijT5nPCeNWzV9uNUtjWR52RMS4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=g_pAETdwO4mHRZ4pQ3adOHm874dBvlI3MA0EWGL9jXCaeVv9oYDwxGCyflTRMz5hsCHH1RtUG_m7-aJcrGHA_W5SIAsJoNV2-hKArBbgzc5HrmOzHuMKosBhg6cmS3jKZN-sPZ7e-FnflaFTFPpMDfbEc3jFrk6s6HZ4Rf3NrGF4HD5T3hGQuPbz2g7-q4meq5zPwG0JpeqkeAlU9_b1sbDTNOQw5MBf0dltW0h0FE7G2pqBvOVgos5mnfz-fBGWkksCk17Bp4hEbYK77C2FEkxBvim0Lzn6ljn3BL8QwH-XJoCPkFrqNaAdrFkijT5nPCeNWzV9uNUtjWR52RMS4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=eS74ephkPYt2RGGkEpmNQIdrKqoBJa-PyOUbXS_y_QfG4sLw1otSWrAXADv4lg75OBm6IoZC1Fj1GbRmSAQVZSRIl9hLfNVae5g6lg4dLPADBdIGkL712R8Qdtz0t5C7FxqTVaqFbLRvR1MrcrMU6zeCQ8bYikGvGEowjeby92DYp-jopg4UMWxJ-8qbXZAyDqnpZCO3HR3-cJIQ1f4JwQgxrOx464EsDbyA856ji6GCZedkmsyNl0QaLHaX8g7V-7rdjZ_H2OnBGyM9EpcrN_c_MuSYdEf2NUPwsD_7_G2rGb09c0dxnT-BN6Q3YMWEK9IL6gI5S-MAxzQ8-2Lc5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=eS74ephkPYt2RGGkEpmNQIdrKqoBJa-PyOUbXS_y_QfG4sLw1otSWrAXADv4lg75OBm6IoZC1Fj1GbRmSAQVZSRIl9hLfNVae5g6lg4dLPADBdIGkL712R8Qdtz0t5C7FxqTVaqFbLRvR1MrcrMU6zeCQ8bYikGvGEowjeby92DYp-jopg4UMWxJ-8qbXZAyDqnpZCO3HR3-cJIQ1f4JwQgxrOx464EsDbyA856ji6GCZedkmsyNl0QaLHaX8g7V-7rdjZ_H2OnBGyM9EpcrN_c_MuSYdEf2NUPwsD_7_G2rGb09c0dxnT-BN6Q3YMWEK9IL6gI5S-MAxzQ8-2Lc5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=p8Hj8U84S0Ig3bkRnr33ieatrQ-SvN210aMBZKcaVSwJWeRT-9N2nFgV0phRMqIg2a9UVh3rUxh2AhYKs5G-iboOpC6YHKqH6Qh1hBY-4TfQqkUFOYhwffuQR8G5b-MmSfbmZvC6haQLz9E8fY4Jg2xgBeHvMGZ3xVOO3dVpNMkwdblpwL2LpFxmIukLSRFaNGguLnPhvWP_prsLzZCNSPvtRJ5hvwKLi4fTphHAhg6UXuO-5IpuqKVL8V7uotCqPyAi7TtUpqmJhUDhJCvgHPhIwAzSOdCoayCQPf41MRRoV-RK30AGRqaJAb6l0DDV9NyrsQvNKKOr8v2x1upHzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=p8Hj8U84S0Ig3bkRnr33ieatrQ-SvN210aMBZKcaVSwJWeRT-9N2nFgV0phRMqIg2a9UVh3rUxh2AhYKs5G-iboOpC6YHKqH6Qh1hBY-4TfQqkUFOYhwffuQR8G5b-MmSfbmZvC6haQLz9E8fY4Jg2xgBeHvMGZ3xVOO3dVpNMkwdblpwL2LpFxmIukLSRFaNGguLnPhvWP_prsLzZCNSPvtRJ5hvwKLi4fTphHAhg6UXuO-5IpuqKVL8V7uotCqPyAi7TtUpqmJhUDhJCvgHPhIwAzSOdCoayCQPf41MRRoV-RK30AGRqaJAb6l0DDV9NyrsQvNKKOr8v2x1upHzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=CariLTgNnoCNbMW8mmGfky0gpvtVuS1vJvL7Ee59u33Wpa5nIo6HH2sa5lvieVwhiXLA1RGe4SUdnsZZSQZ4u9PHMqvfnOqjc6m3VWf6EdgUP7QlXg3wdn69GYceRwKTcQOxzP47xEe9XjDfWZV69VettVSOjOF-80P5ZFQyiGXv1f_CRxyCQoF5rW0nNpSkkByzz2p3DNy6sTMg7p-TQ--Q5IQnVqxb5voeTNBl0Pb_Gjfxu2imRzufVkViaviUAYRB3baDb-_MVlurojRIH8-mkrH7Gk2CaLEvta83h_wgX3eLi90lCMu_dOjZjeKCFDBsrpvkbiWSn5wSHGEt0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=CariLTgNnoCNbMW8mmGfky0gpvtVuS1vJvL7Ee59u33Wpa5nIo6HH2sa5lvieVwhiXLA1RGe4SUdnsZZSQZ4u9PHMqvfnOqjc6m3VWf6EdgUP7QlXg3wdn69GYceRwKTcQOxzP47xEe9XjDfWZV69VettVSOjOF-80P5ZFQyiGXv1f_CRxyCQoF5rW0nNpSkkByzz2p3DNy6sTMg7p-TQ--Q5IQnVqxb5voeTNBl0Pb_Gjfxu2imRzufVkViaviUAYRB3baDb-_MVlurojRIH8-mkrH7Gk2CaLEvta83h_wgX3eLi90lCMu_dOjZjeKCFDBsrpvkbiWSn5wSHGEt0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=flAZ-QPEPDhg-PEnqmOvl02rYg2mJyNj9xw85RwYLEil13a6dbVVyFN9BTLWK22jpj3uQ_uPFS90CFOuAThXj2OTPM6hFijmOi2CahSXzoP_XjJJcOis2XbXryFlK4Ey3VA-ceq3gnQEvduuAVnbKbN9wWYE9IPU8ehAHMZ-Vf9bwCe5UWHb5yr6w3AW-g6NJFGMyOKvWNq-QOSXn7Nig1Sec7uE44zW7YM47WVfPb4J84-hefBLcVYab2WuVLeFVUxdSnmqHCPfxxqhaUx1w7yXQhKNqQ7uYOVN_PHcGZaLNXPF4O3U60BOsK_MoWc6R_PeT0n82oKtDY86EISgWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=flAZ-QPEPDhg-PEnqmOvl02rYg2mJyNj9xw85RwYLEil13a6dbVVyFN9BTLWK22jpj3uQ_uPFS90CFOuAThXj2OTPM6hFijmOi2CahSXzoP_XjJJcOis2XbXryFlK4Ey3VA-ceq3gnQEvduuAVnbKbN9wWYE9IPU8ehAHMZ-Vf9bwCe5UWHb5yr6w3AW-g6NJFGMyOKvWNq-QOSXn7Nig1Sec7uE44zW7YM47WVfPb4J84-hefBLcVYab2WuVLeFVUxdSnmqHCPfxxqhaUx1w7yXQhKNqQ7uYOVN_PHcGZaLNXPF4O3U60BOsK_MoWc6R_PeT0n82oKtDY86EISgWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYkawTE3vmeqUYkoJGwPzXGeCAfDFNAavT0fmWJIpXHrKJ1L24NTUHE9washancq9b-hfxQla7hi_4HPfBOwmQti0vypIU7-Z41_YipM6fjUf6degwVW4ZyugqE6KB8Ukg503vyoXvGy3aht-6JQlzT26dzVEBgLCN_vcf3DVNp8gZATxO799m7fnbG5l3GD5XbsG1OEEu6x7GB-eNwcf-zYb5eqLoKaQWr1ABowKd8u11mBHKnKOwnaoT_k8jYeP9JJ2oejeGI5c-uOAqBlpYsYCFG5kDnWyKHyT5qCcBXLDoF15TOdezgAKcLZeuC3RfVMWp-uTSUKCkFrTtMWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7LVkaVDpy0MTo3mn4PRS0sxDUgQZpjePhTfViUJpAX5GZGryddkKIi2NJR53CsKQVczqP2s1ef-mwU6f4ycDSVtfcWjMNoM2C-ZGjfwuZET0LGhsoY0og3Jk0noeNpGW7E06TkJYbpFQwE736CIVS_qRoK8Q5AZ01nwpNBgPiE23m12E5GHkryG1Bj0KYV-YU62FP7GWg75Ch2euioIW_H7xePpubsVX8O1xhmoQioEn7lm9XgvZlGojfh0AvWk_vcDdT1yAFdtGep3Y-L4iGPesdJKsQaaWLQkajUKYaInm0ERv6gGruyZZMvJsoNEUgrfn0BMVv2gqCl-v5K8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6pv7mOnbTtxvn77sS4OUFOXhirsjQ-0so0UnzqBTbdxKLRsmS2Eedz5kPcTPJxVBN1eW-F0rdL4DBveIEgujLjk4dBbIN1my_CO1OaV404xsuBasidGpQ2UQR95flIpxWlXMIY7tRBtQ__RJcBoh0_dj34eGcmaCsawbfcifiEay3I1V_b3ukgNT_JqYo0S1dUnbTLF96VPWCNVN43WGbmA2_LFj3DDUUdAZk1I_xRrKIIS7HLj6BhUIBgzWC4jQ6ioHNFx0Rjxd25zOGvr92zFIJICO5xMcTVeVX7XYGpVmHy0bBfxcUHOkGB4YhCqdOj5hVhtlsRuHq4tLrBFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlixq97rXxLP-GiXRvdi2K4BgoltkPynle50Pb0B9_jtv-UhwP-Z3KG-8YxEBQFMB4VDD0RI-8KnRx5SGjpF3o7CDw14_Wq4TrHgqF1GcbygqR6q7NhN8kI7CwmygwyciCJJCZhpHe7xgEuuxnVygnlcovTZDY0ygcqzIn27AU9yHXxNYDAgI6OtMTselInIvh15EvtUO3PYayGSLt9GTgswCe6v_mYuiPEpOLEqV0fUQeSJxSxRfJwgEriecpMMSTO62D5C12zAX4ngDZ7VE3qqK9YHFcqM9Uc3adV0vzaqsavUfwu5lCgdRTBXhHA9BV0XAYMJgjwMH2n6nkcZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCjOJ34tMQt3qyz-AycNnQruzSYB9XKB7Rt7E1U5owLj9WuFFplhR9feoxUFCrsAF7ZfDQ6tue0W1jTvdr2XaNVCrcW8_C_YH50iTU0EOP4qwuhKViXXRXFP-WACEjxGBunNRtDiLmkjJ88tk0F4kH4i0_VswuzY_Gj8uFAqWp90iCbtRO-VYKrbNqTZk5lpYVVVYAAZNUWVSmf5Do_-wm8QUFcn8tWWoTfqO3Uj1rZVap2QmMKp1KwPw43pBvlnKwdS1_SA9H9BbrmiDP06L-Zg9IZ7z7oC-fCtvSr_abGA4rbZRUOj5hiBM890kN9XQ6LONmdQmgMKOtKDeF1TPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWHra3NtuKhnf2vd_MYPGO7o-zeEqjBoVSoVy2VI0k6DA31fX737_gD6LlK1LJqo43mlJ0XxDkx9Lz9_lRKXXV1pBArzGeJ804IA1tGPmCgmJ94vVnOEqWRUOurQlC136I7_Z3XAWPKSgyL_jLuwelVEQbUn-PkGLLWBMdM1NTRwFBWToD0I-3hNQVD2QRweC6wb-BTbjyiesXzWIYjucm3CY7dBVQCFOgFpPXi8mXF8EHcbI6h20ayahgQWp93ZONr8ubK4gae4eNSplDVlx0LM1fLAdfeAbQINYPZ3EsS5wltK8_JqcbBbuEDnhb672gtVe1iz02OJPfnlVDg7ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNUeSRvNZe5G2wKObrzvBRc9Qrcl0ysSCN5ZucBgloer3U6QvCGeU9ZIUPzsmuR9hm_aX_fbUPw4FrOTXGa89qaFCO3II8h7NWDfuksl4EPv-7COjGttcTrqiwZB57fOihebQnW62q_6TdgVKNvPksdn1iSBwesvrV-erF7IiPHjdev7dbbGdZfs447L6W9m18IByPbtQG9kA0hRXUUQHf_3kYz08K_42Mwz79JaaL9bopFDyTUIfYBxn_NVTJY5ury9moiENZlomLXb8_5OqAsrVZYdurnf1qwICycB8LWRH-b-gufB36qkdNVZ-DJhAf7F4QJO5mhWMY10CCSmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuIwja-7T_VEsAHjrtFBmHq8eyBIlreGrguVylU6wL3KHadBNp3pPeJDYkyB7TInISeiB1tHATmUCRkVuueWltInwaPYaiXqJF9EPIO9xPYnT-BqoaDGGzE2eZMHNKxeI0EfQtTDZSAkJrHio2D3lw1XIyIIaPuzjLiLllhRQKKR_ezhszXNPBDnnv3FSXGhp_HzzZfde9BMQjJTCIapAvt3jLe2Qs7m2Gj9ykKHGcxLn19DLWFDiLhv8z6FmTFqghJZhFo62tyuM2tTETAwpLMWj53dKGd7wkKKgvu60SV_7zxFrPjYHOkZstZX7U38UZt-XF300SILwfYGpjzpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGpHg6dnBDLtlDvAma8mEccS19AfGbnMLy_NcBewxxetULjrg-J3OwH5wXj7INYZnsFqvH-hNw_TEJGhu6s7xMHLoxOtuVBZ7sX1tKOgAWvy5wT3qLtdJ6QVHbTf_e4Uqrhj621UTowhWqXxXCT3I8xC7X5-_OCxnHOATQR5fdpqJGzAqW3rMLYolXFE2smZMxuWfEffLrQxO6QKvIfdIRgIv3shnvRbnHOkk9qmzWD4lonsTXDTjEN3LfdSBd-LTBvJFe4-nifG0aBTT1tHOFzJb_8QTbfEYi_jBAKexig4TF1nasdtTynDeS5jAHJRn11c1QnjzrimcmFySS5Qcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttEKLIdtgQsqENNOVqgK67lSuZ-sNZjrKFUe9xNz9pH86VjwwsdEbwmeYSPYNdO-gVNIEz7BW7WrKrl9ePYNkJ1AdrKVeSi7BnMwPa6oz4PeFMl2EE8XBDsPryY04gwW9vSYaR0yc99v7R8eutgRtldy3Ag6x7wcyBAkadHtmgtCS4NmfwbyH8DMUbSE8d213Holi0v1tYLSCmDtIVeraEOoG_z0pasmdOV-kTTmIKgzKKmDx4gK6AeVgMr2UsS9kWwYIBWVFjM3qGutTgc_XJc_BTf12kyyPg0867dYKGV7mwmsEXma1FchbHeoKg7pyzZwYRGdnQRbl3SK9ctqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=DqGNaUSi_VdaRrdtDoRiYexhpcZoLJQ9KP8079IHtBftyBfI2rXqDK_ncJ6RElkTGe8MmVnUaK1GxysnwI8r4w3AIjXb47eZUyUuEuFpCyP1ByrEAjWn4f2jc7sEYxR6tqsvqbbc_c-iyXVgv5qRRway6YLZdDsftwASUDvm8MV2uCg9k6j5L0Cre9ThMiKgXLBneMgzcQtmz01aaC--c8AuGC5fxbqHJ_yK5yI4X-qZk_CTRNHFPdKshuQTTjZsoNamBSamIE6POj1qaJdAFMXKV6klB4Jhu8TJL_klNIDzHROIud1O4cr_q72a_92J8IPK5K1A9Bhc2Z_556ywlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=DqGNaUSi_VdaRrdtDoRiYexhpcZoLJQ9KP8079IHtBftyBfI2rXqDK_ncJ6RElkTGe8MmVnUaK1GxysnwI8r4w3AIjXb47eZUyUuEuFpCyP1ByrEAjWn4f2jc7sEYxR6tqsvqbbc_c-iyXVgv5qRRway6YLZdDsftwASUDvm8MV2uCg9k6j5L0Cre9ThMiKgXLBneMgzcQtmz01aaC--c8AuGC5fxbqHJ_yK5yI4X-qZk_CTRNHFPdKshuQTTjZsoNamBSamIE6POj1qaJdAFMXKV6klB4Jhu8TJL_klNIDzHROIud1O4cr_q72a_92J8IPK5K1A9Bhc2Z_556ywlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLdC1WH18sOs6trI2QWy6Rw_ifiE9uzq7_64gDV8uT19vTk_IbUV2v1sz2IMpROHGK56jBkUq4H15dalY-F3L1yuFPtXQPkPXY-K4WYsZwynSAObD3jKDzZA7H6yYy8-LUpZ07HQxd219JRyAvFYHA7BEAqHxI3VTpNfMHsSZlnQjeiX0P-vRpyu-BKoO9a9GODKVf9z5KZ37bwUql9spzAOiCH7jItOHRxAKp-qSaPAvqRC1IZQSf2itiAi_R6o7a7VrZsxQDF0dV741bPOWxkE_6xPPP0mFruqORuYeR0yYLDvhH3_p77jJPcBCSUWBzbxEkYv64Ye-1ETFIgtuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCi7v07CjhCJ4v2HHkoW3eMBl3JmlNZwOwkMzAUGepEScBXZhi91nruFf4udJmVNwTE0-2eCRW86br2oKnu240RTvsB8ht-k3EE5WJZK69DMm8oquNQjKEhO_hjRYlpCktdtRYmSGh5jXJsZovLbDYC7q7_Z1yydZ-Ffpjcb5KYsKmbJvcqExa-oravj16Zy8bqCe5Uj10nI84KRpPyGElKSED4-3tTSUT-HmaIp5mXDK10rUVyb-Rahc1hDmSA2uw_cnYlzLZSXV58nSKs3n4LSTMbimP-p4Uem1B_Nn2X-8SaBTOlzfYx3YJU6y0fg3Bo6cazNADM-fqeyuqHqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyX1_MqCj566bGMpDAgkXzHbDLrH2X_3XGSev6lWauQqc1f6AdprBX2svFU5_TTneMUcyEtjiIYBcg0XRHtRgOtt8FukWZzpPntLun-jBbb5ilOQ1DsBm8Xz40bpEMboQUkAmL5e0DmVqHA2JkTxx-trewFeMvvWNhTYJ5NctLtkmOvglH11F2xd2Lw9ET36vvK5NVwt301nF5d_NsLqbFbQroS8QGr08ukgXP93dMA0aJ11p2AwjvTcPAfYvy5fLJSgxeZgmn-uIEUgD3ghe4Q8fFo2btGd4nVi6AS50OuIgxqarRvOJJCsgg6FAjv7FQtBRT4z-o3Fxx7CDW_-YA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmEs2RBcZNWGwkTRU0Uv5q4kLi9W1m3knZamrOtJ_f74HflESxMWdnJmfEmHfEGAk9hwvwsMp0GsvK_qfB1XBvMhKBPWCF7HIVst6cduFM1cmXfWEOTN9wO3YizSoGJxHuqvmMwKvutM0xhjp2qZbVNYRTlaQzjlmnxlvqaK7QMkY0vU9OldnB_69C1NNw5CrSEuqx9Rx1LtS7KB8rRF-iRpKOTVZjZvbpWDc77b-eOpZLwxv73DNljHnxk_S_AeCOS7nM23krFZ1bUB0yDEG8hveA9J1_Fc6zy0Xv-fDNxk_oY1u0iNPOlqL5LKddpgBABkuMlzXaAnC4adfZxk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL8XbItS605NSKFgV2vMICjw8KzmmKHuqijNU53CRR0SAIfAQzRRy6eeXjo18ZM0LVEfpU5dBwHbes78Vigr2Vz8Y0rjusgjjD-eMCN287ykZTeh-qL-_evzK097xFq3Q6ldyxG1nBgUelYyZCoGqTgzmQaAd2-xK4Fu1bGUYzaF505DUQvv8nQaLYMR5bBHcv66tWY4di-pgFBNSW9mqtgpTO0sRj5gKKdmSQU73D2EyY-w8V1UoqRU4-aAUx9W8-_QW-Z06xvtUARFM5Y3_WlzIUlsLP631tLALNwk8-IdAZdM5RkbtobGJBuBFHwn3nIh7q4F0dQZ3R3UsE050A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeCK9fJePtP010aYwdIUeIzdgTNX98S81VTEd_30CGksmxNCQtCyzPEfanTtSrvpMGML_ioVxjIIRVLXZb686EVAi2Te3jAHoIEsJdKNUv_mrAGg6zpw-zFoDEruV6fVjDhX_6abPrIpLEWUahuah5mlT3ihAnbPO3jyspa33N2VUGpVvLjbri8nH7tUUMud_64kkxuCmgFKy_dCj1UOoS72bAQWoHPV6gMDlLGUEG8_53tkQIQwN2iTk2Z3_R8CVA8CwTidowBoL7PgXtR3gEEjcq6uFjbMq2kwXx4Nfy1X4wMHWXMlU_QwWeULEaPDSUTUJERugEz30IamKztJeK1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeCK9fJePtP010aYwdIUeIzdgTNX98S81VTEd_30CGksmxNCQtCyzPEfanTtSrvpMGML_ioVxjIIRVLXZb686EVAi2Te3jAHoIEsJdKNUv_mrAGg6zpw-zFoDEruV6fVjDhX_6abPrIpLEWUahuah5mlT3ihAnbPO3jyspa33N2VUGpVvLjbri8nH7tUUMud_64kkxuCmgFKy_dCj1UOoS72bAQWoHPV6gMDlLGUEG8_53tkQIQwN2iTk2Z3_R8CVA8CwTidowBoL7PgXtR3gEEjcq6uFjbMq2kwXx4Nfy1X4wMHWXMlU_QwWeULEaPDSUTUJERugEz30IamKztJeK1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=boKIPayXivEws7cY7HX48vXIymYd6yXL9V6a4MkAH5Ki8F5_Xi8G5CS5bC0qWbkybAlkiOFKIFvPxB18y4T852b-ioaTCmorFZMo1Wa081Zl4xksswlzY7eqWz5H3rxNI2E9W_CO1M-7851uqvpn2BLa9girHPECADIVPC0eBZjfFoBTMC3I4m_MSVrdgdZ0nN-JtcUZ2D5jjN5k969vra3GKLVevM12z1Jl8p1txLlEUsDKLD8oR8smcAM4tyPHC6O2mpNgKVYTCX_jflTshuwlAzeB6ehnRKH3tRVv9reGkbyxW7sl5E3Zp-Hv55hBKbjX0InwkfoBQ8WHeqppcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=boKIPayXivEws7cY7HX48vXIymYd6yXL9V6a4MkAH5Ki8F5_Xi8G5CS5bC0qWbkybAlkiOFKIFvPxB18y4T852b-ioaTCmorFZMo1Wa081Zl4xksswlzY7eqWz5H3rxNI2E9W_CO1M-7851uqvpn2BLa9girHPECADIVPC0eBZjfFoBTMC3I4m_MSVrdgdZ0nN-JtcUZ2D5jjN5k969vra3GKLVevM12z1Jl8p1txLlEUsDKLD8oR8smcAM4tyPHC6O2mpNgKVYTCX_jflTshuwlAzeB6ehnRKH3tRVv9reGkbyxW7sl5E3Zp-Hv55hBKbjX0InwkfoBQ8WHeqppcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak8t5I_96sxcOExM3gGg9y2a0ejm2rdbxmVMFoDfJCorDIDJ2x3ydoyKakh0QtVgItVm3faRiLAsVtr5OYiOQoj5oUGVRYMb-CsdpJh0LeZX9Mb_6B7kbVYeqavuMoWEfrI_uPmXGTfPO7K9dPwLosm2EQQXpIHUGxUss4HISam9tyDeFn48m9kMTQFSANNio_SlUM7jZYSMqPRi4HkGnRq9pS9pxDrcAd7w42nXxH29tdOXb_kFAM3cC3Jg60AlVIiC77K9_AWOr0U63tdZXM-rYjRkf_pxHZ4YOZh9Sg1Nqdv0tLZKzANwJJminovfyIsz5EvSkLuDLPmcr4nFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=SSVLiWkR61bJBDRCgr52tRq1vSZ_jKHQQmCszZzQX2EVShr1Fup-oivDwWC_9PYsXfMOr35tt7fZwWlR2oe7nZR4SjtbzZ4Zpd44Fr3WyDWBFGYckoL71YDUF3Ud2GaOD3hycYocXhZ-5N2PDjvlB9C4vtlYaaFy4E40GtkV9g-zPicM69O55SDRwiDKZVYlPmtDVfW6kJ8Dx9FGjpfAtxJHAESx2LzCxFUnZVP4SkvhQ_lMEDqT8EQMaYZjXuojGzkjt0nmgp4EW0_-ky93woYL9taO9Ku6P4Au1Su3zRB9xI4hlVECmKjcLBCo11Mg46zD884YaPo7YoPdGNkx1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=SSVLiWkR61bJBDRCgr52tRq1vSZ_jKHQQmCszZzQX2EVShr1Fup-oivDwWC_9PYsXfMOr35tt7fZwWlR2oe7nZR4SjtbzZ4Zpd44Fr3WyDWBFGYckoL71YDUF3Ud2GaOD3hycYocXhZ-5N2PDjvlB9C4vtlYaaFy4E40GtkV9g-zPicM69O55SDRwiDKZVYlPmtDVfW6kJ8Dx9FGjpfAtxJHAESx2LzCxFUnZVP4SkvhQ_lMEDqT8EQMaYZjXuojGzkjt0nmgp4EW0_-ky93woYL9taO9Ku6P4Au1Su3zRB9xI4hlVECmKjcLBCo11Mg46zD884YaPo7YoPdGNkx1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtxNDK3xVCtC8Y6MOzkMssRZxAa48zAb-oXTSXshiZGE5eyrphQPAlx6Gqrv7KxKLqH-Cs5580RLx1NmYXua3FFaMpIpbw7DvUEgz0rvQkagdfcmVD0vrKNECL8vN6dNevK-aP3tugqEkD2kosWTIHZ4sSM5aOa_0kzYhc84kJH-Nx4zpc8_ZzvPAlWA52uaGOrwQZOl2S735XCJcuzYhvDd9qQeO1JkQCAhJxeUIHDbs4-irwiWJNmt3XvYQN_9QNiYDp50Z-6ZnUuud5LNVHTzmQh2nzdzujgwNVAR0W9OxlzBu7DIFjow9tmnahyvsthk5LSrySFxy8ra8k2kmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFfw8Z27BL8AbnNGztnVnHYLm7JBImabJbc8JtmrWvqa7-XXgChQlhK5ZW0zBA49So72z3FD2EHFeCUAQT23Noiffi-JDEO9pSZGfqrExaw7lLGr_kMo6ysWhLXuh9CdvVeb_CYJys-UtPsaOwt-V7JbNbRij9uA8U7z4gPPQjFO0qAhwBXrlvA1XQCdtZgpqWd_jS64InH4TT8Jbm7w8c0ovm0pjmqTJg2klr-wgUOgTqhHl5Jw6B_Lhths8ttTKwY9NQpXILL3MNngmh17imjy3CW4Qmv0EAu0B-jHeZH3CNc5zgJ-WaanQP3YbrFt2rLFniGRuH8XQHd52vam1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=QmWlMUGnGQ2NJSmu4Zw99rdCkS2ImrbEodMvE-wlrOjNhc_yMutYNyccLiDlQ8wIrBbQ2K4YbGP86uFX408XBV88_pmm1QWuSnT0SejL3Gz0KJtKzvY3bsX654BbCCKHIF_Mdow1wSxt4uNaEEi7r1fRsDbs58GAk5gMJaX94sZP-_6COR593-8O1uWFtiVt6XYjNTYUOrxZspGMwQ-f-poKxppSAHsy59KTBc3uM6uEzskKCCJrr_zYtIKylEk6y7leeKW8V-Oa6b3HI_bqZXIMQ3_o0QCHigL8jV5ISwHmRQLPOhO-_z4R4TFM23aUxuwOV0m-ZoLjcbX7BwO-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=QmWlMUGnGQ2NJSmu4Zw99rdCkS2ImrbEodMvE-wlrOjNhc_yMutYNyccLiDlQ8wIrBbQ2K4YbGP86uFX408XBV88_pmm1QWuSnT0SejL3Gz0KJtKzvY3bsX654BbCCKHIF_Mdow1wSxt4uNaEEi7r1fRsDbs58GAk5gMJaX94sZP-_6COR593-8O1uWFtiVt6XYjNTYUOrxZspGMwQ-f-poKxppSAHsy59KTBc3uM6uEzskKCCJrr_zYtIKylEk6y7leeKW8V-Oa6b3HI_bqZXIMQ3_o0QCHigL8jV5ISwHmRQLPOhO-_z4R4TFM23aUxuwOV0m-ZoLjcbX7BwO-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouKy9h38nsZCq80XvRMQ8hq65IFEr0RpgCPXKvolcXvHyKW2VWS264a2dl-vOQEGHAVYglQ_9z6jln_9ij2O5VqcuXIFyjEiIGRbLA0-rDbZd7NmMdftlAAT4iQa-_gOCkrNcl7E1CBCwhtFiNPXCiAgFw1V_S0w7Qa7dRsyKiM8kHZPLvmjtMVj5zhiiw_adoDhVVnqhBLaKGv6CQqoDU5oJ2K3-lP5IBQVSmRyXhc4vuamO0xbP0WOST6iCdPGTDrcPgHHUynHhTT79z6T9f6jc-VvkpXxDYuPEUFw7LBVPIwdIwcxoyXhtyJN_zCJv5cqYdFrDLpuIkxIbSRZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=Ghv8QOAuCO-r6Y6UpzGgs7-eX9HzqNC8TL-AiXw23GkGcQ21-F22UL-gvIooFNuWvCFHgIfrKauLdjBwSoIWjb8tIJPPtJms6P0IeRFYa7abq51tXFvOyAvxAgzZi4cempdMKYNz3lfhrn9fljfOGA-UYH1nHjJJ0HYPgYw0EXstsMEWeml3YF8wEL8NHLaH_Wyzy-3zcPBsuok9ao9YLvzb05mxWl7WL6vusILe2CA-MNlsWu8jtKqlsgJwEJQ2wthrLYnAUglFKndU6CPAb87Ru7H03oEqR0O0krHlo1s_f_wBa1pBNdKt_xma5b0OJBmnRAnP0d673Xx9SxPw5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=Ghv8QOAuCO-r6Y6UpzGgs7-eX9HzqNC8TL-AiXw23GkGcQ21-F22UL-gvIooFNuWvCFHgIfrKauLdjBwSoIWjb8tIJPPtJms6P0IeRFYa7abq51tXFvOyAvxAgzZi4cempdMKYNz3lfhrn9fljfOGA-UYH1nHjJJ0HYPgYw0EXstsMEWeml3YF8wEL8NHLaH_Wyzy-3zcPBsuok9ao9YLvzb05mxWl7WL6vusILe2CA-MNlsWu8jtKqlsgJwEJQ2wthrLYnAUglFKndU6CPAb87Ru7H03oEqR0O0krHlo1s_f_wBa1pBNdKt_xma5b0OJBmnRAnP0d673Xx9SxPw5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=TzZ58Ws82K7Jh6Js0ZHZXo03qcnppBe7rnwndgFhwv8kAmOO6F8o-8Wbj5MN2Ad3jQh77drCBnEiovzR9u0qjknyFe67BU37mN0KM70TZTcMc0Sukita1XK6KuRTD68UC_a-qPMmF4H8WR4QBFs4UcOH-Q4qlY4pSN55BTWrm7vad74qtGeIkxBubIB4V6INaVTbCET4wQj0FOrwSAstfTq7VYYAdzwMfjcyrWbd1ZxzGlTrtIt0cRQ_gvKYnoyCe7O1pMaHWTVUVpG-XKI2iilfqpTVqzUNgyAGjk66oxwarG0quJ2h-fkEUHgusjxzzOhcUgssr1wsgIWV-jbyAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=TzZ58Ws82K7Jh6Js0ZHZXo03qcnppBe7rnwndgFhwv8kAmOO6F8o-8Wbj5MN2Ad3jQh77drCBnEiovzR9u0qjknyFe67BU37mN0KM70TZTcMc0Sukita1XK6KuRTD68UC_a-qPMmF4H8WR4QBFs4UcOH-Q4qlY4pSN55BTWrm7vad74qtGeIkxBubIB4V6INaVTbCET4wQj0FOrwSAstfTq7VYYAdzwMfjcyrWbd1ZxzGlTrtIt0cRQ_gvKYnoyCe7O1pMaHWTVUVpG-XKI2iilfqpTVqzUNgyAGjk66oxwarG0quJ2h-fkEUHgusjxzzOhcUgssr1wsgIWV-jbyAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbfYVVPbx1Lckk-HjXYcXwfwKCwT21lzDyBD0riJJpbOA5NyLxfQK67fpkkCGJi70aEXTCDIvYPBCfbMRUytZW0slKImC1rDCIgbsoI7_UoApyHw8NqICHE7BXnRRYDwB0I3oV4SGy3y0GS2M1J2KkvqfnZlwNHI_fTgfh1JYiZtb6EwaVTEGXcbiD31N3Ryzyqp4Qo8SV7-rHQJ30rHvUUalHIwccGkPPhmWo-lWQciGqkDchMGidejsJSIR0zBYl44U8SaZKbIpZKNdwBegKWbPG1l6QKeNaoqLbaQ1gbPfRji3OLUOudKL4Eti4oiMySGmYZJ9EhkA_8fMzCmfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=s1_kjdVczv6qEXDd8dRLPd2_DtZJ4zTKTlMgWyu3il7T2rR_acrS9m77qg9QomyQz3G8yCDWiWxI41jG1_aw0oNaCOIoHHQlPw297HiRCZQ0-82w5Ht1A9PMD9HJE6F3stzwxJ84IcOgtWA9lCghP-gcWCnwcdTeiA8pxFzd_CtfV-33F4iTpDj1vuoZD2ekApb5bGGpura6j3sryjTuXWbwyCjgbMLuRjRS4fiLV7fQJWzVw4BLSnoDlTHag0eB_ldY0U_t4iBNXR12ZLOcMloPcfndv2sFO6sflyP1xM7XKMGjmD0cHJAAFqIWshCFAdAtfMzdUWlMVATusXNebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=s1_kjdVczv6qEXDd8dRLPd2_DtZJ4zTKTlMgWyu3il7T2rR_acrS9m77qg9QomyQz3G8yCDWiWxI41jG1_aw0oNaCOIoHHQlPw297HiRCZQ0-82w5Ht1A9PMD9HJE6F3stzwxJ84IcOgtWA9lCghP-gcWCnwcdTeiA8pxFzd_CtfV-33F4iTpDj1vuoZD2ekApb5bGGpura6j3sryjTuXWbwyCjgbMLuRjRS4fiLV7fQJWzVw4BLSnoDlTHag0eB_ldY0U_t4iBNXR12ZLOcMloPcfndv2sFO6sflyP1xM7XKMGjmD0cHJAAFqIWshCFAdAtfMzdUWlMVATusXNebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3bX5VC3SLmxsKtic9CdVtHa8yBICvv7ZNGkx3XkuF9730u0k3JEmTOUQZC2zu4FdZgsa7amMW5SC6M1S2FEWZ4siiM_R0x_10GZNYPzgh3iqG0dnaTDO0J00291Qf8Qzgn4yxgjw4zcUjmCYhOnDTsygfbMqCvHiWM2Qm9hHWrwTPMzqQKpuDnr4UjoM_VqFwrXx05SeoW42MF_DYEjd86Rl1GBJ5mjKZdAQNaVDufFslLu4RsV4tL1pu2ZVUqLfz_RD-7lUp96RlWBpQvsYUDTn6ak55JBNXSiilc1c-doIxytcz88uWMKUK75zx1LNnV8HAPTNBM9yzSq52icgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLwkAJB2bzDhHZh9c62E_sffOGOVzn_CNs8E1a87iGdtxqMgSF5myh49ujMiijhr2HHzFVBUFPPl7Z5lS5ymShe6BMR3KsaBsNXrRK15d1n4MYoPHic8NBvqg5Zfqzine3HXhsuDJbQWCn-_8vG_JswrNsDS5UUBzsNE7vm1W-JmYfA1tsY1YPY1bknRXe9mOAfBkMp6bz95OHGHoqoGUzvI6QQZ8fOHhCv-Z2vz4PsH4VTBqIMpJcnOmImoNJNSjCosty0DkHqq4s9xXl3uJsTwq9M4YlBFg_pPt-UH_J3T9ZmnaBfJtXZppiPu8uxXopLBA83nxbQv71DDUp9-vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh85CKK5UA9CVCQXvDdBTbru6kZa_dfl4vXRRVeZFnV3AImh4WpuwXA6p4oxbixKwouI4fgS5bkn6BuNZ5mT_G6GUB1Yo0xIo4OJISiuqfZ8geb3H9uxtrS78AeS_1wgMvbW01Nd7Ao2K_QYzNia9c6b8CPXDnbRVgUi_jtRQtEzckfisCef4NA9G_Bewa-hV9hjZN-_82lgc6LALgj4TtaKZSdTRsrT8RNosOGsNK6v_fpkSQGNgStmNdjmSdG2jXbbVqvdhgQQHyMMwe4fzy1KpRKU1xvTeoDZ00itz_F3V9hULFtygL7tHtaLewzviyFSkqJvl8-AzjmoyDUqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTATjWfuFRAiab94NHcI0xxSotBDQNIPBnQ5QnzZR_HuUF5d4ClLnNx3Fx0Gbm61Ddr2gKatztMJaCuU5LFNL89kZlHUcU7UHiK5YpDNJWIq-I6E4N7gdrlm1s-rgC8-FA_mcjs03mY3PDqPvavYj2eOABMq5P9USE2Lc0_VtloLqtrgi2LtsUrgp6qQqrPS9T2OEapFSLfqk5K_COhyBqSfQVuRjXvZ4EOzCa_rg9lNF9w12mKuabrmG5eMZJNrU2VSU36oIJHvyV1FkwA7mVCD8uWbvXC05YQxVw3UDrdJogB_J2PPBUNhrLypgMrmrgpo47dyhktEEcvYjWzJkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTVzlkCKrrmotmQdJOffU51UUpN67OIjr0zj4qOMJqGiMPHj9f-YV8EagrxYC1AU_9S-fcVS7RZsZ0iU1zyAaELq-pooBi82deuOfENgeu7rgUt9JYKamu-BQ1GxqEps6W7OKPu6hPCcic7Er4coWPiGgeFYOX8LRHnP-mTYWShgVgxwhpeBA-3eM3KtGKuvjSHzTPdyIYX-0nRQ09Sg9FGi7OuEWQRsAtbeuOd6qbgKVhiiaJ6u5JmyJ0RWbd0PRCTyASfX6qv_BaxadZ1_HywQRugmGl9mv-sAE9lB9u-8AsJvRPcrspbg3YpsLGfjnQvKzRXJ_CVmz7UaoOpnnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_Xbc9Ey1Rcoglyr8xDj9cBBgnWrFB0wBUoXBP9og5Zfjws8enzEOrAv9dd6E7cWzI5iQdIm1smzQl0FlImBz5DKsnKb3Ip1pGL0n2up0U8W3Iix43NEdcyKxMwxdlbgTCrCiX-CIHXNsVxv3uybR7ouoB-0T9KfaMdblQafaw8rfCfLMKGpoW0EMjswJO4PAfvKJcBIY4kxXBy1SxAqx9ey1fEO0syEGIcZCCRSRfk3nWzTrduQk8cQ7W3iBIGnc50cUHj5LQ8zPnFfziNUv1RuZEeHASjvv_0zgfbprSgfcIi071THCb3BYqUz4Cl9tt-bmyLASqLg3mo_5uqdTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGSClTBXL3GET_n_kYOHxnCU9ciEFTuOO27J-mRPGtxgihvQdhmHaAbRZd8m9nlCPVWfDg8Vc2M0EtWCtWDa-bLiPdMXC8BaZqU5LQfCQ3KLaPHOMH8KNLPxyMzkMTQsK_tIWPvRwaLozxBFc6MLX3Grg0d42wefO67MaN3hgWQWnv6iPET0w8CIezL2mjBu5CK1EXXsWPCeLe2_vHxFIWKpHpzxIA6pWWUFop3mejxKFSUd7b0bhMIlQ42V_BVVJ4rOrmyv8elvxmkp5h6mC_d3aZkNM_EB_fU30UEHS9p-jpKqU_1W4cNyoqLBRJaZsez07XO_LEZdcklgirat9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LddONmaO9D9lrQwpOUhLLYEnYfHcdWNGkZN_xw7Wnhci_Y3OsOq4j8fwaLgnBO79lbObJuFOMAEEPC2S9qAlR-c9dPma9KIVJkFlEx6r5UEP5jPh7EpcZY_yH-LShG4GKqKXqZO0AC1espc1IljtJzbYk2u0PvujjYkzsMDAAzCTzT4si6EAHuuz0b_9TthUMiC2nRWdXNEa2EtSwFPLse8mnjPrFpyRKOtr7Va1PEZp75ABFyX9bRmxEHUCSglmje4eEgsxEn0gBMWg9VKzVT4QCxnKyShvpLkGVDDNB-EN8EC3JKALLtTNkgSZq4D21VDAT2Z2v9nTRlvclGtdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0A7U139vhTviYgHDZpwschsK_LjJXyw1VHYZiKoUcAe0f_OOlei4wWdHTmdQt6TP3uLuy03CTD72l5G6JBsRcGkjlGz9ZWNnsf3AnnCcz6VaysUtXxEWJWnEMsq2gL5ZSIEOpvox1mcrRp1TvvlLQjS4fZ5y-gaIyz8ZGo_-bo4q6OOgmX1V8ifJmd3CQHvsGSAZ7ACy9BuVqZb88r_4vsxRZKh4Jo_lymfYj8YNP3Fe62vX-ezlXS_pOjwtuOBNN2NCfd2A8stf0_98UwhM5g7p8TkXHEBsyO8zJUd4KEBMRJ84wPd4J23ZPS19-WCdpcazeaZDDlA9g8dHzEp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=P0BMB3m20vNYr2dbCYWmMGvHYxUpmMajKJqbC086vm2yPJHQlXF1it1WRztUbrnoMgSwBjqW-9pTVKHMASYIRmuvXK7jFsTZqadnTPYNkdLBkxXykVzTV--MWGOlNH7iV-KFE-S9ZjO1cXqXV_hWIu1zRMFtl-Az8tiTeESKTmAsO9ihi0kyhrnLVZOj9205OqKfTMvlmzKoYj7elgzh4LcIHO1T3y37KZPvgOZ_g7egFrDQAEvSnRSaRtG5k3Czfe20rA7IIxo8TxcjeNgrgEorjJyQsyWIK5emeHMqmfqymv1StlfVnyNZT_ey4fmnaoInZhSc_6wZR8_t0jmaLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=P0BMB3m20vNYr2dbCYWmMGvHYxUpmMajKJqbC086vm2yPJHQlXF1it1WRztUbrnoMgSwBjqW-9pTVKHMASYIRmuvXK7jFsTZqadnTPYNkdLBkxXykVzTV--MWGOlNH7iV-KFE-S9ZjO1cXqXV_hWIu1zRMFtl-Az8tiTeESKTmAsO9ihi0kyhrnLVZOj9205OqKfTMvlmzKoYj7elgzh4LcIHO1T3y37KZPvgOZ_g7egFrDQAEvSnRSaRtG5k3Czfe20rA7IIxo8TxcjeNgrgEorjJyQsyWIK5emeHMqmfqymv1StlfVnyNZT_ey4fmnaoInZhSc_6wZR8_t0jmaLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B19390CWXVFPtF1EpiIqHHNdTNbRp0Db9vCqq-Y5WjBzpIgmQ1SrRuRQJeqUlN-2WZrfPXv6b6laFyiX_KkK2A9Co7PgOjCXqpdLNhABFieFcv56SPKVBLdwqUi3viARTU5zhFHKSmdzYRPMxw3OHj9VVGrH9azsAIspf-7-X3SUEp6rt-ILvRuUDRCdUA5t9qfGUAUpsE7vhpaeNn89ncS6N8NuPfq4xxZcBvD7darRx7Pa1zag8XTi8aoiCgQbT50cjDG8IDew23TM1_f6bATKCl2mWf_OsddlXJD-VCJF76G_bFbifQ4okmRGeaPpwPgG917SOiKrXOcrQEPRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5KKbFK1WC_vBwyLTnEDht_F-xeD5WRjmjeATTnRzxYXWQyMgwpVguF4vUjMwcnfwlVTWJp9vdXEyvhctah7M2rdMpEOjtIq6sIWefuzZ6IXjw95LhYOJzaCL0E6I4jeh_0pVaI4Ar2y8ZoThMrhdVoDK7VOKC-Cytf-_i3JQtpzRQ5zRM8w92dBqKRPCh_8ix021qgqSyzsmGTian0lcorDC5kvD0cBUGgc9VBByV2JDRVCihO5KLfyT61vtGY13jQPwdgvW535BpzqwrBWDDqNiJL-O3_PaLItsny41Q9gxIvHtJEaOrrroyg5n7AXsa1n4P9Egje1lWce5RdK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKfnM1dT71CtEYdq655SGGmXIlbngkDDnOcbf_5gmfM_SerwQ1SM58l50vp7UR7sb-1onjRR0UsQKaaGGgBgix4CzKYCO2sQZOBzxFj-j9qF6EivNrD_c7aepgdw_ce91bYotUp5MRACTKWY_Uk7jCpnRbl_NePfJPCPLDXESL_zVBPigLHfEypx4MayjofIqoidzZQTlB8ZCKPV5zXbEYUjzIjUHbxCMkvIoaLoREV__mvOLOUVqtq4JS2uC1P3nb7Rjz_SDv-1y2pvV0ksqXIN57wfOsrTRd2wjeU78RYv4NBkyShlOOJ6r57fWFR1ODp79rq5MfD77RzwobFFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=oTfm_z9RnfYYveo9wO9vu02d7FHKD43vbYWRaIF4LBenkUwg1lKRKGsBTeBfJ-GSEZHSC9BPu8Ur_BgFQOUAMTNgb_1MdLM3nfV9TpL5NZxg19UTm_Z1FctWhV4SrHshaRUpjITtYsvOoRHWi15-23XkYebqLfXorZS6h0tXyDJHw9qazyY3IWghl5xsKD3-Zc6Px_-MeJg7nYQeHL7KnnbZhKZgOZ-0VkHG2ZKrKoIHT9IWqxTveGtaf5oyk-tFZVTRVqG8It-FI4bemNmsHo4ZKqP6RDqczBXRsGmXWVKdT5tvI8uJfLLPy2bu51HhqNx92vGYeQ3_pHL4giZvtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=oTfm_z9RnfYYveo9wO9vu02d7FHKD43vbYWRaIF4LBenkUwg1lKRKGsBTeBfJ-GSEZHSC9BPu8Ur_BgFQOUAMTNgb_1MdLM3nfV9TpL5NZxg19UTm_Z1FctWhV4SrHshaRUpjITtYsvOoRHWi15-23XkYebqLfXorZS6h0tXyDJHw9qazyY3IWghl5xsKD3-Zc6Px_-MeJg7nYQeHL7KnnbZhKZgOZ-0VkHG2ZKrKoIHT9IWqxTveGtaf5oyk-tFZVTRVqG8It-FI4bemNmsHo4ZKqP6RDqczBXRsGmXWVKdT5tvI8uJfLLPy2bu51HhqNx92vGYeQ3_pHL4giZvtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBflD6uMfJe1n-gZqLg9TJrAgAYk9JuMbP3db3Oa9etauBkBg98xP6LCs1kDNXExwtkYPLZ7LL9xtpHT7FEtaIFnZ8LArcKdnYJ_AOOj6SIsZoa-LArNLN_P9c1NH3sP-bxNTUtUxgVFbth9HWr2hdjkHbTucgqWhrEBLSfqCo8G_dKbo3lxhSdYyRx2kLgetdw8LclwmYtAwbGiKpRCoDk0uPpGL4-H9sGaH93PASBK5smbO9bfaYYFlt5ymhXqJsKgZgQYrhXUtUryaDOrfK-rlMEJJ_Ie60c370WrHiL70lhBwrobZfNogCDiTsWN2_vqA5e-X_yh189zQ6DRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=pi6yDjk9IiGJaPJi2af1eTY6ERhsUAbDhuPpNkbaFW8LSlhqmLuyLmyB3GjlI5S_tf_m6maDH3PrcslTbxhklLgZNVFEba88GqhA9VlvtUryYhI9kWv9FUexOdYbAoXsbR9H0VD-WnncJrC12IM7HK00zKjWv-fOXfMGMZoWKS5YfLremCnsalQR81YXoDigMznL-wyW5E1XKuGCKtD_HMbTaHkgkKQ3GQ55-lQ71iwg6isTqY9F_elbGg_os7kyiyDjozlp0WEBv5tzciRNkNiCZtdY-JtYXXspLVKOnSSOvL8EgGMVZP5DvPv-gfgleYAv8DF6bif_SlMjtxQ_Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=pi6yDjk9IiGJaPJi2af1eTY6ERhsUAbDhuPpNkbaFW8LSlhqmLuyLmyB3GjlI5S_tf_m6maDH3PrcslTbxhklLgZNVFEba88GqhA9VlvtUryYhI9kWv9FUexOdYbAoXsbR9H0VD-WnncJrC12IM7HK00zKjWv-fOXfMGMZoWKS5YfLremCnsalQR81YXoDigMznL-wyW5E1XKuGCKtD_HMbTaHkgkKQ3GQ55-lQ71iwg6isTqY9F_elbGg_os7kyiyDjozlp0WEBv5tzciRNkNiCZtdY-JtYXXspLVKOnSSOvL8EgGMVZP5DvPv-gfgleYAv8DF6bif_SlMjtxQ_Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuOneM5rJhTHx4az1oPRGUg7sZQthXOkn5gLn172Mr26UmCrro2kVqk2iRHXSYE2NGjPQbkt4c8zeWjGd7vpyIJEEY3XjkLFaCHFJvwvdTX-16ebdtIt9s8q7YtZpM1EqsnX9AMY7W0QQYUp2Oql8VkAS8qzI86yR73OoNA5wfSthRmxdoRIWqF1GmJtqWtMOxolIW2mmXTJ4HAIvk2eM0wcEBZHUvonb0o-BuNoi2Tw2kyecmtAME0UF-5Vs9ZZOMazLFdxmkpcGf5TmBeu9EiF0BUPkTukIrGjk1aWSjiymQYJm7Aqu7vKTYrsGN-FStd6o1GQUAVVK2gj1rpGeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9WGBlumpCmt7Fy-NEXYp2YSxtJZ89MuTkl6aax8o3X1o5PMYnv81ByTyJkndAJOKh-CMcRCMXT7CWKfMTgbhlsPH89PRl28ECryJ8LWNAfIK-gX5-Sr1uG9-ePyn2TTPm2emNzSZNMRyTDD2tJu3RAhzg_7Zz-SyHKQrv8ss66ctp5YnYGaFCkhq6MHftlRQKQB-FyygdVqQKlVXQ7i-OuPO2EZKQ0YaikXZHBviTsTELE_TOnwbbjDshxQDK8TDW4Ggyqhv8AtcEqXccFoqWMziK1ExaUi4Wxv7mXEOEgOpq1479fkK7NtojtY6ecEv2MRg3OQneqANljF8n1iaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiqiV6gHlS54UcmwEM0atB5_MR0f8K4fDE_xjAhG4f7cru1LqeEuP6t90aGxEEvRlNHUTMZ1nKNEtPHKGKT8SaAFyNJGiiQlV9AslNWp-ZOzL2K5-BrK_gVSRza5FGiDDP_VDQRlepmTV3LuGOVWrFMU980u43odRkGuupzt1Q-6tUm1n_7EhTa70Nt6m5bLWPJRIOhb-YUdMrtDXCy5_NSDUONwHuqYfiFNEoJgH3CsgHuN9wCi7CxfLrxrE3m8q8kDcaYZvVoYXsLP7LMzuJwN-O4rCrv60KIX1H_W_WvcLE8XXvaXieNo039Iw2oX01nzqOjtJxDnFOBiVGh_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=uZfsMARcvheDRjJQxJQkmDutxV-2hwf21gfE_NyUSjpshjclhdc4oe3LJOXdVYM-qdt_oh9ofxrTOX16W_UStpNWwDhR6NFQp5nkSzU1WnNVVx0Si6z9bDKytuLkzGdn0DLsH_4XQoS30FzFXMtXZrfEMcGnoHh6Mm4F31VvD-MqygkNgXVAS7sontjclLesv_7ke9A5HQ9BagzP55ezJZTWIqX2pgwSlBLF8uxSYYtdXOi-zyc7YOI6mW_mOQbQvmZbFjpht_omxo8v2jlVkYG-OyKkDtJBc6EdcXUguP5Mfa9nyuKMIeInZP8UFv9Krr7YLcaW2OAHacWixePpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=uZfsMARcvheDRjJQxJQkmDutxV-2hwf21gfE_NyUSjpshjclhdc4oe3LJOXdVYM-qdt_oh9ofxrTOX16W_UStpNWwDhR6NFQp5nkSzU1WnNVVx0Si6z9bDKytuLkzGdn0DLsH_4XQoS30FzFXMtXZrfEMcGnoHh6Mm4F31VvD-MqygkNgXVAS7sontjclLesv_7ke9A5HQ9BagzP55ezJZTWIqX2pgwSlBLF8uxSYYtdXOi-zyc7YOI6mW_mOQbQvmZbFjpht_omxo8v2jlVkYG-OyKkDtJBc6EdcXUguP5Mfa9nyuKMIeInZP8UFv9Krr7YLcaW2OAHacWixePpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j63uHr6QKazbmj4cCPJPaEltYiMcYTM36xPhSKANicpxM4ENxS0UsCxlf2VghMqUMINPhcJVYC_pi2TLXynb3a-wd_oT-JLD-Ha2KtzwQph9v4836IU_slXvH7zgDrefljJ6S2BMROsFimLTAN28EG1cppGR4b1Rpc3e6IDO-AynGsKUor-2JQP5PmsS5fg4fmXt9DgWaOL5keHK2C7yMy6Smwarb_SE_L8yqvrKU0SYBYt90o48_b40UYHdJ5WUA6-Rv0TNeSXWA1yvYPNkKfNwaC46VwmO5I1I0TLFeIwnN8EpMVxhBb6TotmRaiTPuOZggEc_YMkEDUyqZU6zNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDW3NksbpWKX3LEN-o6sKwFKcT76Duimi2MAuRkdQt_dr9txWwYoaqpna4TX80aptokMl9-v93vO2cFyjt0-qo614VEvgVsGv7MDwpPRQgx9VXCwB6TD1m1Ch4TKYSjx0_dzQgKcHdJo_LX5t2iKJgBaMMVyeub_l49ShAOGQFE1JJsh1arWmyRdHJoOYdBumq4flmV1eclcpfGlpywU9iRH8mumXAOjxUTCnvbb8lJt9fU_OME5rlnkQcxmQ134cJPUDcjRWg3f3bvHPRhTeQTkUpZ3k7-FCfqivO22lkUK87B9o4uHv1mYrhERQr5rkJ6a6eRm5UbzmnLCJmYdQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=NLInPLDksK620ZJ4eBEg0CVqmqpH1HJBNfsvF2y2xHEv64o_BT1S1yeGaPz3qm9g0b43zBhgCSTOX-Qf7aqWUFUBSkkn1Fvesw8CChqCO5S_rDfow5RWzeBOvRGbgoYG3_wyhw-WeqdgVArqTw_JvCA5bz7nImjv5TlzwRbd-pOs1erQxn-1eOOHNs3ZHDFqPwrLPmfya8m5HjGn9ZsPw2yUQ7Cq2eBN7jvloo7dcvEkYX8TFtx2g1lP8kTfhrWi9Jf22xghX3oENapRKyAH61310hdPLYBuS7sgH-kus_mvC3JNVO9q3ID13DYEkMY5umhra_pliwHjA-LaPsDnSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=NLInPLDksK620ZJ4eBEg0CVqmqpH1HJBNfsvF2y2xHEv64o_BT1S1yeGaPz3qm9g0b43zBhgCSTOX-Qf7aqWUFUBSkkn1Fvesw8CChqCO5S_rDfow5RWzeBOvRGbgoYG3_wyhw-WeqdgVArqTw_JvCA5bz7nImjv5TlzwRbd-pOs1erQxn-1eOOHNs3ZHDFqPwrLPmfya8m5HjGn9ZsPw2yUQ7Cq2eBN7jvloo7dcvEkYX8TFtx2g1lP8kTfhrWi9Jf22xghX3oENapRKyAH61310hdPLYBuS7sgH-kus_mvC3JNVO9q3ID13DYEkMY5umhra_pliwHjA-LaPsDnSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
