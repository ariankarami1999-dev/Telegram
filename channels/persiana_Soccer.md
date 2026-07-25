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
<img src="https://cdn4.telesco.pe/file/rp_LUFX0lCTrkEOG8Waw5f5TrwOGt5TpNW_7HbCpFuwUY-Vfv3yQ6lL1MXcq-xw7il9Ewr5AFGpJ3E-KQOXSB7AskIvh8WJR4MQU9VyvYby7v32mG1M7N5u1LWWRQ0JCOmMAyIzuhm4W9NTMiUMdgaAkM-6xTlX4Ae7raIgkDPwLJzfKej209vuZB1lJZEUKPPVqF-MJ9FZWYVuDURd7qtu-d9jtuFBIqJCbYfx9lbpAQV6vZ_2M0SN-oSwThhh-xir21DnTpG7P6pS8UjPQ9Y48JGfn251H4mrLvm6LJL7ABWqwY2wmiG-i0ExYsqrpAM6eFHli5q_RrEe8a-3kUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 571K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 08:56:46</div>
<hr>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z48Or7rPWjz3pHJbCvL3Ya_bkPv4va-ubuUY46jmgFG05J1YxGE4KC2KxhwI2hrXCau4qtudMxfTMFFu9kX7fK7FZBolr2mnHkY8Gdfdmo9uHBPkrafBrqpjO3qq1sbVx2mm8kZbcfL1U_d5AVTfHKk6MhXm5yTvLUVR-OePS1j0G6Gtj0m9SHEL-kp3eDjePpbQiZ2zS7e1G4LruqeTyd0ybMOBXgOlxUDP177iPbem9zc5nm4BJT6gBoYQQswL_jx0t_axnd6khB7JzAscFTbGunY2cDtIq9jmRAyVTQJzBdNRWAklKQ0_Q5J9nzOqp8VdepweojNhXCXrRbuZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3zpc23F2SgfQY-YsM15kpXP6Jv_vIIffL0n8yxujaHaeJIoYAQC10a-7OQT5sTIujt1XvHyXAtSM-tzpNIjCsHRQ7XMO6ZawQyrDX06KpPotG7X_F-6lW2uHbQwa7YgDRdT61JqUINtIkOmaAwTUS9TvPdakZ2go4XIk1Rnu53bu49MHeLNcYSpw1R3vhjR1AvbOlT6QDSkiCAdaOt0-lu42YiRiK8rn3q6c0B8LmUTlpSu5YIzXxIn1r0bMy9xbgcXW72hCNJTvhtc83ZbkZxfZGhQuaDFGr2B_MWFdrOnbKjbH4aLqH7fhEsK3PtokUfAVorH8SyKrxqMwrAO5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arYwPNq70jOGRjMK2BPfAUO0V8vU75l4A3HFyFW6ltt0HMu8GG57oyNjRmy5-3B9j8IEMlD-mJmn1HcgCMcJZLcnrEqWJuGjjCjZHjYtJfSE6lJJ71gWXVLdJH_dSkA3SrILN-DJNoe_yytBNrZt4cKhdXf0DvIHV7OHt3GLyGRA8rEZLsc9D6RKTGdniAUYwOYi_Pa2A4vyKF4_fEzezYXLseibsYz1E7NAEFa6D9y1G1iP4rQMPuqfR9T8aVCr1F35OkmLfZOtlm1UIHCm6COSD-lO13XHmgCWVO2CfcjEAQRVFmLD7Cyoni8gmQvdCz4T49B8irL1w7t4NgJ3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYOeh3NNTZJWvziDzyMwJ6ZRkrUFigB84Q3T_xo2KUmpxFQCEdkQRGGc8-96DnRS87S0KmruzJpdRiA8iWX8Nv-SxTbcRl5a8ilOBcxP9eVTKjt7QqGzwCUtkGDlnrek_M8FQvostTLV8M716IS6RPmclC9TJ3sqnpG0kiSKOs3kBRLo4BnP-5evivBYfwMVB0T2bipAjIhs05IsnGi-XcMkaGEz4P2LnuD55eLq80Aq1SqLNKJCHyAtx0N8MWLUyqbAWBNQC8r5cWXNGVTI8Fy7B_WtiJR-VjC7o06Uj64nQ4iz9sRyQqbs3h__fL0Xgq6BzYs27zGWzHyysAQCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMufuQDRIdU9WeqSk3z2lIju6QrZdLJ4F1nAAPEW75yA4BD3BRdT3nMMEZ2YwjPsmDYHzuJBPUJBc7fTFNDJANp0rC3ZWt6zznqR1jzVXrq4RtOZQhRL9xmAxflXclS-C4uG8EiXgs6urJTH-FugAG69UAi65Dysf1uAyIDtKnPNdQnRRY4RPdGGD5m74q0WehtQMs-8TzSdbKvm5TvqoK1AsdXnK5hErBprCD-NZhYeZ3Yaba8Sp4lr_Ww2Hy-OSvdcG18uyDiLRsWpXh99Puvf4vfU99ARkHZ4UQ8EOfy74Jtk-p4zjuBo6CC7rnuZbCdUEA9FAkL23N_ijktM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKI-ZP0eJSJfvMbxaouVo9GrWazHdytoiHieIElRJ-plV0SJEPWO8FonzBwqdKr-BBqeyIsZdsp-Ql6SrGVfMewgQnC7sWCSZc_1zMKRc0mdVYIyNqUAN27UPAu3pzxGBYuCTmdgLUEguI8dT8vqzPjAfeU8wJP3PEVAA-qKT-c4p-LUj3Qd7KIgi0XVaxQiAPkRwBWcF8K7z7vrj-QZ-GtUSu6M93z2OMulxM00AY_53A2oY6F6a1cAqZ9dVUZqiR4JhbnUI8ut28VZzsmF56XIXlNRyaFzFLbVhEpwCd7TEwCmtsnbHrhwz8XHANX2kdZyOLabP3g1JDYztLLMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDFqYSWoXeji160qeHpj2qrVxYUNGbgijuZjtSf18V-ztxdVZrDfTBzlbkDiy2sA6PUj_XzDNdqnzZUIDm5ibgBZxJzTdtvNrcPWtHOLaAwCmrhYsWL_Q46fHog2aTcG45iDfy4g9orpZ7vktUtZF_zNHnvwQQqDrzNMLMBjVRq85bINuVBnNG9mvHlTK8-fpsxtOS753DVxv5U_wMolMQiYE8IRvn5Denw8Mn5BXd4hrerdH0flCoBD2eCNcAFZaiBnqmUibav16HEQdOYOolJDJmguAeF3Yd1fejGg3_vMkI8SAsY9N8paA9-Ei2C7NWaprxHkwKLba5NIXinzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJg-8f4BrCwk43qsOEgMLKMGKmpERGv0r5TGM35Ewja0lUVkFFuIMNziZP46M-3h07G7bR2IeXLmD6FJEfW4DA_CpW0PCyHkSkvb6EeHSNsPgPv_ljx9K4B83N4p4-Kv8TMBVENXKveJlshU0jsBAfokW3NMgXTJzFs558wiSAQ5Jaut4oCZ4D4s3GYrV2JPvNJatMBjOz08fGcsEMKjh8HbTdNMLY4MtZGiLQEgY-3oHEuiwpT9bb_Xxwas3SIDO1slnp4K46rP3vSv9H6TiO927gYtpKyEilc57bjlubU0BtLd74wErDkd56gtSJ2a-0DdzHiMUF6l7SJFQOU7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fen10W2RKem78DCYolKy9_GMEmtXPe7vic36BtpZgEBq2YS6WWLB2VTeqmhOqPiKX3xeF9Dg8okA3n0s89AGmiMr5T85JVaCE_R_Wb5r0lnRxlleecQm0Ret7kQ5cjpaPKVoEXwUlOUikAd4Qa1IsFjejYP3W3hGno4f24wJRcsxFmT74EMh2zaFXIwPJPG5DIT1h1VBNGzqm1QsAvklGLv10yAthZZMSBeWHqHnM47cxBDF5uJrcDztbqqBtPryqPzVFqaPx6VZQD9tBPFKfsfxELqV0cIIbMQ_kPS_huV3TNq-O6XjdhF-GeOu-1X7VVIfj7CF1v9BYok6_K6KQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nov4oz8TyZVqFeaMcWjBI8G_v4gQJcrmuwTCke_Y1exqPvJYjyD0b4MWNvKCuh9Ai92uYwMGXRbSRRig5dlUSrx3zo0KVNmW0E6L1pQudY9o08I-UZ3sfv2WACK76xa3s-mx1JpIWftb6TeHeArMfd-ymlCPptiBeVLM9UdxnqATLNv9uCD3m1eQzw3gn6cJ5Kb-17Cbuf3gzOfr-_c7ACgmV8REUUkN4h4kUXfAMQsN2luyvpc0mmB7qt9yyBA9tlKowWrMSoOQQSW0BRfx_zG7-_7_2QM9dX2SVY5urLsd9372q33ZiopWoyd9hxfCKqh_MK1b3t_u2KoTIl9Dqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR2gTi1RN3B9sNfYq8DVDyqlgjxD42KWcJJ6py4rOfPXH3D0rz9jdTCvild7m9EQQHWdgESQzVMmNZw1zSuZC_weC1KKqBAtmahf6bey38irIrSPYEVUvZY7NpEICwMeqyhD4ryBRlhP6AFSAv2E8iezIK1p3O2pnNI1DHDnYLCeVVygQfIN9NszO4kwFvh3f8I-gJ7II_ew8q__0YVz5Uh_7-g-G8vWr6ca7i8QL_22FpHc34J-ZDZDGeuCpfkPAcL93cU3ArZuhP-R2V_KQ2trh3O6s1lKfvf24gIpOGiRna0QDLoCUSjSv7hmuH1TMlyPhbopQ_FmboVQhh_oAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTs5gQzUjGN3_l0o5kjkmcSrkCCk7XOFEfk_yYpCJOGShN2ELbQROfnEfZXDi_n_kuJQI2mVLnslaXrCx9GmS-AOuKWtGZJciV4WeZJwVDmUfqSQr17HDFJMSsr7sKN-Gkp9OzX8kLNAjfNWpfjQFGELSUs5GFpixTfl3FpLyyVTsUGb8Fufw27Wbo4NLU7iYfxXqldgk8xSslZz9hfWTBxbj3zKpKuFzIFd2P0sRou9gBcIu1bJ8z1HLii39USnL8WYPrfzrH4V2g8yIyw3lElhJwSCeIQfmZ_6C2Mr2IQzvaUHyCDFEGS9FvHn1Lt4e8tehDz2SBFjarLzpc3l1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Baz6TpqpGM3jO7cDbZfteLMYZaGAkWyZ66lBa0PVRFCqwXEQn_h7tPwT-L9O0JmEEpldo5vbWhOxrh0ytgghC1kGA9bDx8chg08ohZPu-0vKOIzCsm5U0gJvZzK-Vc2xmcQp8hYiJlHvq8mK8QiV8b3DL4f3heb3lZvZG-xlF6ouSNrrK8gOTvtoUAwWRzU850Qjjp9uhQCdDf8WlrKhiK_lKFdN3gFIZ89p2IY8oDYlCBgqz4zVEG6ZHxB7uWf-RDQo8EpLLbZK7lvHGF_4WY7JsfX7xGn4Ize3d8RMyqGCxftoJ7h_J08UXfxKjMdVczC7u-gQN_6wTINWEdkOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=S8AcpVIrVScHJeIiqVq6JCrrVpaOTRQ6nesMMveyw__KDTe2mDopaWzVBF2nIoZ0P5E9CuICizpDBnEvh39kf7PpROwFpf0lglKET2Z79kKfWreWrQfdAXTo0xHfj0GL9VTE5RBo44Y2gD-3-t_FcAxPdBpps6A7-NzEyUuhGJ7KMoN02Rp9ZsA_K027YRyZahvE7Xs6MtQmxlxVkM_uGp2pqyoUdwfzNBUzsAJoKW_LMwLzKZ_B9214Uyc3GSEfbsjm8BqlkD5VO1DBH3h4AuSPjYhVcT00ncHpzjv02C9JK2hNGJPE6nYKlDnlrM5ZL6euluWppirM9tfIT7gN0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=S8AcpVIrVScHJeIiqVq6JCrrVpaOTRQ6nesMMveyw__KDTe2mDopaWzVBF2nIoZ0P5E9CuICizpDBnEvh39kf7PpROwFpf0lglKET2Z79kKfWreWrQfdAXTo0xHfj0GL9VTE5RBo44Y2gD-3-t_FcAxPdBpps6A7-NzEyUuhGJ7KMoN02Rp9ZsA_K027YRyZahvE7Xs6MtQmxlxVkM_uGp2pqyoUdwfzNBUzsAJoKW_LMwLzKZ_B9214Uyc3GSEfbsjm8BqlkD5VO1DBH3h4AuSPjYhVcT00ncHpzjv02C9JK2hNGJPE6nYKlDnlrM5ZL6euluWppirM9tfIT7gN0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsk0LAIjUp4S51ichYWY4t30zvTj_cBdW5TyMHYdGUGVLdP-sqXLp-uScTMTKzQsvBJEsSpqpZCQnVdi7wQrElvKlnU66u26GBaIETQVnbFlsQr1luW73hhECLWVdzqbeWES-nEw91SqT69W6nPFOHoaIn0BryZDqpJnmSB_ucRQp9XYj4kis_87cuIjbdsuTIlGuNBOLXvvt9ciW1eMmW1urJbg6GJNBmss9zvEg179vtAcJetdN_xAejY302btV_2AXLyhE72ioZYlpExGtu0U0fLksOwFPrOhP-9uIwkv_vCIRiUUG5U0Ry5lkOYhjjx8-KItWUkuaxwvMIts_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmGVRUUU9nm9bQO1b19kdPaxBJphKpPn5sc1pYe9GDxvxfWu6hhIUgMTZuuOGuDz3H7i2UQSZsP2a_4VaIBd0URdA9rr-UdmeyaGUeE19YC1bZ8eTQYN5JcBXGZXrWh4FTK5Fs2hzUSsmFY64to9yFxDJlrHH-HrfczQzSqQnsu7CAw7xEFsVs8Be5oh6EvhDnrMsgHBt7QSDgiVJrkFcPQ6LB0FjXNpAPtNIZwJk2bRMVM53qPr-CZQaRf0WYleuiEs50IlYwDuO4dUbCXGASHKO0U3tUb3Ov8D_9k6FAkcr0YfymGNEpmAKwKZumuaUY91lVjVdjXagS_U5uzG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIQvtyPga3SAWJjoE2TC1AQKAlvGc-cQ2z5iSh-CsZ-UgA7g8J7dCS2FcpRT48egzDeb9p6y5mHMvHwgUXJpJGMHGsDWWojJMPVnjzmGvq2yr_DGP97lhEnVnT1hIyMVKS6gJi2ZxAwdjHXngPLBp10g1lUeAFhcUpsrElrooAU9bilM3zGPJoxmMjLzxHhFEie_H9KVed38OjuAMj9_5MLzUFKoyhOgSAuJrnsWGjI5vv2IITuI1ONjwiod1mSnhpWGZSRH7kT8cRAl92ak9OLDvZlbHpSbC3MyDgKqL9qX0sVwR3fwQgn1m81CDmvnX4HmPeuMB1mKrF8pt3YEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtrhUHxPNACw-rlGtC7_14IPVA5auppECpLbKAnLy57fPxQJS-VjmbUATNiBztkGt2VNHfd-XbCgTnZk8im6lsF61q80B60A-ibTRNW06UBaFmRWCQgnkWKGTj6Hruj2szE876pQQXhkOS-mR-6L8_lHLwqJtXzJJ5GS8pB_POS50VmhPbqi_m6koWG7L1t2Dtee7vEoh-Ity5vYjcZekDXh-prO8NWhvn5DSXoSIHmTvVoCRIis7i8mTAzkaW3Yz44uqJNNuC0qtpIXewcwCcdl1l4bT-ClgTORF6L9taSxdxENE_DIb0a3ISyy_uMDlfaolPbjkttkUgSsx0Zn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=YlbFlja9LXWDaSqEKBsNY38M5xAcjHxgqD_L4Hb_2Q8RhxWoqpivkS-p2AMw8CVa9CxszDRMR4fgVEz1RT2CAXN9o-SGcURNBf142mBjgA73uSNk0IL_ZbGG0rX45SCBdo-FloNNizPwomXqumO4E1YWGPqWdegGFW10I0_iOialcx8LiW9OMuVGU6RSSYaS4ZFzCzipjVOkW9GH6CkzqIz4xGHnF3YS4qxuFimERIoixjdbfiaSor2XDQUfcxQAv63GYU0xOK7xyMCiK639CFqRYxLlGxcbjzwmnA8WipBlTi8HwqgmoaoN795LLliIva9uY41MWsQZubpcbwIRMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=YlbFlja9LXWDaSqEKBsNY38M5xAcjHxgqD_L4Hb_2Q8RhxWoqpivkS-p2AMw8CVa9CxszDRMR4fgVEz1RT2CAXN9o-SGcURNBf142mBjgA73uSNk0IL_ZbGG0rX45SCBdo-FloNNizPwomXqumO4E1YWGPqWdegGFW10I0_iOialcx8LiW9OMuVGU6RSSYaS4ZFzCzipjVOkW9GH6CkzqIz4xGHnF3YS4qxuFimERIoixjdbfiaSor2XDQUfcxQAv63GYU0xOK7xyMCiK639CFqRYxLlGxcbjzwmnA8WipBlTi8HwqgmoaoN795LLliIva9uY41MWsQZubpcbwIRMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGEWMtgZ8054rHgHUqOghxdNx_kKvGhXweayA720cMJc_6h8U-uHx3UbzIPs9UsF8bnGJoDi20Oxpfr1rS4gh-LavA6GKAWbECqpwTWoD7rQDOIiu7pxePAJoX4NoD4zIKdH7d6xJtDhvdvPnU8BaF7sNFec4WZch8xKp4juzVMPaY2qHKQ4U89bf3JkV59WM0InW5ic_IBX-Z2IYbrE5KEcavmDGawVMcB86SCO2Cva_W4X7hPztUSjv0pd_7o6voPpXXbdymrJQUlQYT5TVMVzqYd16ICO8M-zYcm765tOuW_cciERBqjihzLoXkXjt5roEkSrIXrbpdTeL8nQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmUPXx0iKhgvNP-a4sBVFhrAvSw7cgl2833NIUIXaNAuWTZIOwtWg5Z5d9Pk_I8N8dAI7xgrsLmiEeRv6HOWaF9IeLZD1HO6qh1eGpuDGjHXraIQv_8LAozaiLzGe7ZYAi8EWb0P_9_j8pfE-PFfYHW8PaI2-rOOmmZUx1w_kQBYoYM-5A8aelvxSXV74uvGSvflDgbjKfoF18J6w-dQWbe5LbGwQiLCMLUVEzgYxneXsMbDnwZLIwGeYUIia-OM4YDj_YxYlSdopEb9fc5g3J70lQUx6FC7_0RxQlkUVb5izBC2giUdLuR_GIO2wYYKk6oGJZ-yQO_oS6AGixnESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN-lv4kzHHrct8GXTG5MfK1oU29idLS-eJIVjxv4em8G5goShPbn_0gLwGrv0DIUSvEdtX70ZcfYXj81BL2fff7eGL121B7MFuNSZPuMNNw6WvP3vVg5fbY3I5PqVl_0Nl0mrpe7ryOJ-p0uXMqEMEUfg9dJFRw7OFXvSbrHWpFvITapa40PDyOPSKcdRryyE484lQX7Irhol9pDx4EFFbvu8ShJKTSHcJkRUK1ihpneEOoo23Mo13WtZPCgRHY00s8DU4Uh36AAEvgnZMGcfZYxNsSVgcxS2Hc3TxLGgXjZtrdpyfEXLSpikl9w-ILbH30N4nk_tI4vQEd3AQbiew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZjbpk6QpoXC0cCgMFS3jjmtWsanxdV8AVFf_GQ7fFYg9TWIJ89mHXPvp4Kc_kwbEhuwrkrGB5FEoG5OZ3s4bI5ZU05vE8r5IMITErkGtjtdIgRjLq4ZW69sbCsjXKJUTKBLv7df2y1GPl8t1nrpQf3i09frlTaUqJfvEj92-fLpZkLuH-EDtNzheAknzXoneiwhKn92fgXhSPxfQPtO89AYmAjVnsGYbk8c9nJTPfZiQ3JVsHVfm0cmQOR3PDplcTSZd4qHn361MDM3qlkpaGxVhVxck5OfjjyiP15H6I1GFYM1t-YjdgcaMVy2QqUnH1vPsWTgOmSJfxH0pmDInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSK5rT8PDCPNoEmxfAzdDKpkaryt-2PzKTSlF_tkIQNZio2Q0yRLjQKKp4fAkjle60QQBYpzrUTJ58ZFeuwn-kX9786J6Jog7gZEM-y7J1PeNGZenfytQZrVn_Ek9XVkCjMXJBVhcV77umG1P-3zmKMLKp5iNkuat2XB1UNwuS1WcQrRbybdY0vBJd585SgyGJZr5royQIhvYjbJ0dcDPNOxKosl6hgl9viAbIiiHzZHFd6Q3LCaXmo0YfpsBz2wEUcG4d906icoDkOKE0CnVG6IWerMci7iP0jSfI6BGCBzBFvAv1hXDSLEM0kyTuu5WpakxaQ1szukM7ZfDv0SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLGtd9I2fl-IfkEeSg6XZnsz1gxUIzs1sPvMNxqkQgSllSRiyVif-ls_ZW-Qic3wafYzarbFYy3Xj-xhQr5DoQUVGq-Jo2x7eaCCChbylqgwdfXPxdzIaJnrerbfnHyt8tBGO6yXJotbu0NR6cw-7S1CoPiC1YLfBWMY9e3IPgT3VT-ryO22ex38I89wGSDlh0qFV9ksSrIyRofLDmZiXsaBX-7i6OWB_OnmlWoOM0R10OfxtaCAg3orEdMO4t3699tC9ieTGQ-atqjGQFATPv_QP2JFY1xHW9DDpBQBe9ZVyEgdnQYpCJP31fjIAClAdioniIDTatQGiSK6u7YTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE0_kpAyX-0VlFZH9G8_xTXVyxCAeMiUPslhAUQxYog_pWoRmil0B8SkvHdTw-Pw91wMSJ1KyJDPaNWkex09vrY1FCHF5XYG3_lDWwuvlKH-mDmCGFPPJahxayBsNyGHf_eB7Zb6IWFBW2E11H5gRDvqGE3z6WExhPISvWnDAimbATnTlBEbkbJcvBsYkr_79itUuYB3QRLsZXaRh_WFBHb3MQx2jDZ8sa_fT3HwjO_wQ6HY3Ohj-sOAT9r5HB4lWW3L0Tp3JKdVFcBFoRY9_-KbmQPKv0DKeEu9OzBF60dDCou6Qn2B1cr0MdTrig5li-cOAflXBhiLLLAtvHRVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF6gJKPQ5le6S9AYAvX4Jd8A6mVkZXDFVE3yAbXgzjTf-rrrWcS9kbGqOU4t2427IMGmXJyPXQ69WwVlcJVvT33YJobPKa38JRSDHjGQVvx3qdpG1HQkKdUWs1RUovdkvbY6X9i7ZHq9vFTGo-qGDoQXZnx88-JW2BtrZMkQRlaFarepnhE15PoDHSSgTg0lOkrgraSlukcAeE6puzKeID_E_GPcd-tUt8akZUNJD0di2UfUMxWZFBrLthZziYRoj6JI4LO-q_-IooYlIDXLWwEXAgL_moHn6Hby86WElFXHR8FvgN646U11xKlv4d5z4QyZ5u4p6g8MpO3axY9ijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQbRip4ujFYtEGKd_Z1tRjikYJLamdPX_ziI79xNbdew9CWZUMPjTfxDmMH2egdlaSIvmQ71sLSVBu_fxKqSmBXVUPvhk5QAqEshExmfcMzVnWaYsVWwfs4RhliwOY0VfC3ngDqwTwIhg9eJoMqgTf1R5G_IBvsJe4JwYI5U_5uCPwDYMznuE9QioNqc0TG1cW-6HyMbLR106tkybVOJEzvlT7DkoeTD8Y3__jyGVGtjk8QUN6mOVyFsW44l0QEbPcP0tTZiLlwFGntMK6Wf7Ighdi1jLgXcGXDTEwVC-gVbxp1wpH7lJfWnsUdt3l9xQB4APHIsfJjeksOdn_WtGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJYDFRfYfUubrf7oaV5_jDdunHiL6pFBrmXAAz91qlwAAeiiddvZyjsh9Vszq0LWVEutGbDcFGtcczVIoDk-oiCXHIUsSDXS-QGMyyabUA34SsllYqVCcqf5CF7s5JPVW-SvhnNXsj1skDEBUdmL7Jq-IidqXx3FL5tqxldUz5NOmU_62diL31Z3k7xF2kCL5XJ8b_ilvgDFAB4ZXAhlUjB3i3sAr3jhOGBhI5krHULB1F3sux3LDOP4mkEC244BjH1vKj1t0RfA7PVpOCXaFVFoQKTspsmNDDY0HN0177mkPIZCimjVWPTAA6_4yIHTs25q8jQIeC7JGaMFBq0htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGW6MAp5wL_pOM8GmDZD7Sa4bh_p6lUlMimpPYeJhUL_toWtvpc6BRtDf_4VEN12Fw_drBXqzEWxa82pZ3XlY0bkbHjhgIIVjn1t30uyj5D6o-UKzyAHsKNhMwv17uFRGUmqVR8HQAsownu3NEWaKRkjokxZgb4PEkG3tEHcT-RDQV8x5VBXmIwV4fftp-H5QK4km9qiSzMGwIRQ7sfW6g2JiTWnPp4Fktjg2kyjEIMur0hH5x0DFIC1wxdVb_g-R_2QSyK5lpkhwWU9j32OxEwFKoF3yJzsJ7G07-5hkmHMCk5b6F-6YDaFVTGSj44AkjUrPrxKB-rIExug6TPtMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26422">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای شرطبندی هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
g2
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26422" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIsB7jquU96J3jyjujVJ6iOGSOQM9ygj4oVlAKjieGSkFXEzkzD5TXGhevU6wF4xMR8YMUnYuZ8M2WlzrhbrQGmhuORq72h1SrhBICLnbCv7zdox3dfZ9i0XyWNhGQbh-is3c4z9DO5mAeP68VCxBpKtTnRJDpuwiHl0oMvoSf4UtjqmAM0zhuHEcIL8Yx09kjWX4Sd-yfW6z103fbVgpJ4etO_ZdqxKrHws0o-MbuVYrGhmx5TTUcyK1kNu71lSLQRbC6IGN4q07efairkqZlVXJNKHqk2u4WR2_sQQZE3pys5Qm0Gy6ZrkRMvmUXDnU5umEGM4LL5aY1ZYHoVMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeYIFr1FsIzELPQX4C75DU5f6G3zfHibbn013Rs68k1Tlx4isf6_gZ3yiAawtp5ERrcmKEajOzxehnPQxb2FM3beZp3YBxomiMvHjK5oo9ZiVbiu6I6sum2WAk_P64pRjVbeS1ii0h0Lgzol61aWgDRcNLshpVRSXbCTUe-2sUYrWL6pb9clbtmd9g25gLFQoswKl5j37koyMAtXRSv8sZ5jaDnp6bmY24TTlD5jMrhG2wVuqwBeKA2CfcPfdcMCxOvHZfIUGSplP5luOqsfb12l1t6fmlK06jKFHboPiSs7BHY9NyOBpXk3cfNod2v9HT2Y1qb2YVj8KXVtIibsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbyhI9-Tn7p-IlxbP4DcL3z-j_1up07y3z_rrxDlCXi7G-tdFW938dfI9uLSavCE_iNzMDN1_iGOnObcxWIppOAzSucPvvluNK81U2ca73YZkEnZA8kk7gPS12gx94kRfh8d6kpWKaNwZ71hAdpr-865TWQT-DryvQeHLNW71HxsQJc_78cRrfdBgdz0cAPx93Pu9nPSZiVQ-mtzl5RWwtyD0oSULH1sbrYW3Q0m4uiA3FyxJptu_HHzpBoLVe15z5suVRlCTF3uIwLZsycHuCRMCbgOl4bbSsopWlGc0dVfEFc5LM0Tk_ajjalJwO22ZlWxJT3ti5Q4hhK7WZnP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qidhl7_hA76d7qkvWrglEJZfDTIilPho9VbnE_K9cohSFD5SajZZJ2Bj2mwcPuXtKFWa2wuaKFntn3tKKHKugEfXShl-TKzST3gg-3GgHVNdrlQNEZiZoF6ebqPPucRNDNsU_-QmZXf_ykqRhD1gfe8idiqzn1QzA7XWSmcpGPHAzZ7JSgXc1SYYizmFsXuIrwl4JTlEz_rhs6ht2ShoVmFED34xj73xnBM0Nc_TfSjzayfBLuxCNTpEm8nha7FofWKIOffFU00c-ZZXQ6tW_PPOgLcxy2KU471G_o-vrKpaRT2yG9W8cTyMnIyycMKoO-w8RMEW988QWCfeBl15OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoOb9gS_DojrErMGlHwiSzi7WN9zs31oQyWVbhN5NmOBt3wk-kQCjeodQf5XHE0r3b4nnC3VhGWyB9U4yxYpJcKDBXwdyvNCXIA1f1Mi9rEuVSJdBSefV5lKpXATo9AAEv54iynJ5Y3j3j0vi5Yjzwfmj2Zq-cVOolMde3zOfr2cvt1mV5Nw75ujrwTE1TXtGvHBgpq6Da2Jp0F3wE_rkt_NBjynDZ8thN4FGiAryYeD07arRU62OABvFLZlaIvfWd_iz15TGdo1OirjCGEWj1p0027B-nNmPeRdUcQfucqT1uWKtGDad5vtc7jIXwLMr50gCVwDZi2FlE4Y6PtDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiXDbJl3q8vE5-AuA1PeDBlzYFt-VB52nXiPa5uPZsiRKYwO5a2EtE5m6W41KzgKLPoh4fP9DfYk0rUDtH2dsRGBpKo7rCiB7-FBtEelajYFL4teBuSGBAomBB8Koni8xAEB3rUDF3dpnP1LdqZfiqpZTmndqP1ovcWpSILF0pR19ihrEiSK0rteQQ90k4mi_ZmB_5keHMMEBXUdVwbgSzjmhlWHCJgBkV7P9JQjw1k-zTiMx1yKlyEEH08i5VhZ9xO9U9_5ox3OpdEBTPve4O6ayMj3KAjHbgF17QKFX0kuTgfYTcZcTGSDdRAHZhJzMgmC3I6E_CH3v15iQ7OvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbXkBNzePFGMDNDYEmEpmJmvM1TMFyPWtVklZkh7pvWuWnTCW8hDndvsXy8hOiWLB_xGnIwRXCG6D3QFlp9nCOeabSAAgzyVVtcM0GAG_QkBwPByLz5JfQ27eKL4y49ltZtkaIQbHzXTYWXm9X-OI1_yB7CKJrLeUqaavSahlwi-Y9Gnl6i4Aqb4NlHfWzakyUhOxrKBwSWvHytqW-fPiLYOTX_-cp_hdt0jfz4p80jL_aKi8p3-yiDPMjp1NHwyStnjTbhBVCKFM8qnHYUSCIyJBEJyx-2e-M79tQ7k3bmwkymS4viGqZOQ60yFC24eLuVgbygPlXsEZrVmTYJKRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tdrx5rqDJWx40v35e0KUJJ-8cQGNicZrI8l_mqegV9r9IjVDQgHocKiKw7l_Frk49-8MusXBd2_onBNBT_-QHWWc6O2vutfc-3AF338mWHD2xlC5w29iG_0_Dy6bcTpZmKMc2nNRcYIN5wgKx8f2Fb9Z1PLvhfpisFNIfhO3ch0CqURiYZMkXPDsMed6w7JPDFw6L0qoMI32IDI60RDhkA5lZyUjHsWIllIUbBGSv7v1zaX5m19GUaVox52Lm9kr529F6KXlyw_muwOwlTwoT7743YaY1eomefX_3KCc3ggESWJqoBLDOR_Lz9_ttYFq5Hf7To0BotgmZX3W2nZ87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN4ZdON39oaNr6CN38gg6-QzBbFR3eTNbDogrXGd75vYCc5QHZRIJKG78bF1SrICMP30T7-MRdsnyAmJN7hV_ixbGA9nmydKeHOimGfFwtEAw34GHW-KfNAet8jq9AhwJe8Cl20lrZNqDXJ73vKf1-AZ-GEMPkyc6jsZtP_XNjGBAlHJwnG8ziqDKt8Bnj9w5Q__rsW4y7h0OtuvThWkj07e4Ry49pRvN9ahRdu0jpoOsa0hZSskti0BXNekOYBHPG01LyoNavpMqDci1fsQf52IM_Y188TIbTjswOak57YkVGRdoi_g1hPLZAYBqGa8qre3d_xNjp1vojPatXPe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RV-mwu0IhDxdncS4xsHoHgth_tDJwmdyiMRmdzn7HlBcG44dSExc8_YvExZoAbepptDTS7h0oOKabTBcmerwd7SnutvQswQkLoapfWDZeER48G9iwDiluvkHKUEA7ecIwov7RbYRuGumvtHbTlUyNn8vIQTTtT8bFCew39Q6LqMEv5V-VWx9L0-acK624zQ99ZNDxLJIYgbv1J5OmEUigqhHCD0zTs4xL-Ri0nfr9Li0os97KjuZvpwb5Z6Cv4DRYvLa1lszBRMQwVwdBh3omFx7Zmi2ttQIihAaSYQNwmXAYoD7qo2TBVwGhfWSF4yIwPaO-F7Bu-ml6a0Z-XER5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPSadOzHsud1uBlpz8yxrfLVBkDKyLz1dlL-oKKvMy2L5pxdU3Xa8_CO7iCJaoxXits0eBbAGPR-vYvc2YokMmpnRvT5LtJ0DpMis9xclFtHRUEehQDOqz8kXmtEAAZoADEOVe_C3fOuukpknhYscq4OUKoeVNnEWjNDjzz5g3C4eai8fyNc2H3V31J6yMKhA71HKcVM-m9Y1CbZKDOiIB97lsJi3TsMnRyeTlsZIXja3YxDi44RkNPucKuFDWFAF2ZuUgxtESi8QTc-Xe_96TTH-2WSfMUdjPt6Y2-yqtcNr85hdTbsMjkNRCOmldGdF3rBUnPQjlh-AtudNNEP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9BjpzP4y_m-p4ObhLLTa1tv3rtXMmZ4kOfKKwJBJn9bg83aeA59211QP5AQ2VqqWJ9QQJ4bpBjmhGVzTNrsfWAMWxZNaj68iDhy0FrNI8auWDUfH82GuE4fOf821TVbqgYl0yzocZD1k7kEdvDsFHNY0Qmo292CqqzUNZgW8VuwHEs0iT2HJQV7UbMVkMRkAwFYEHM28LaWsNpBiMMZKtdl6nWlg_0SZl2sjark9TBKvp9xkWr9cf_nwt2R3x5c6Ime-vyFY0eVfONRIvwgLi4KdDinOpjyhGU41SEKis-cpYDz_tYOvN5n-YFWsLkoKSS8xvTF3tm69XWI0Frrkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1_0Hkx0CslrqzbpVOiTypeXnS4pPdr1Ovqju2ArSi66q8hkSooFudkHnrb06qBVU1zLY5nXNL2Nyrt9vlZP7joISyE9JUtpTYqskFvOXucszqxinIRcWgqIPzSHIp--0tma2LK90zWo0IcBpHG6iDMHSvoL9-Y4b2bhoaXJXtaJSVxTbxJVQPO34pVMiVzoB07hXbCiTPBgItI1hlJU0o26MHQ1FN4CMf3yP_6vcJXfjftthJAOUGNuBI__hOhrt4ve6gsYICSljC6m57zFfnRFTcr-g8KjU6H2_kzVPjD-_rQdj2S3ckfouQknDXA75ZBJPZk5ajB_kUpCNpu56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj2KPsec5ukmjxLHlh93UiTR5GEsr5pZeNMvIxxo9BIwPboywY1enhk0Qk-CQkOdq6tMmy6QB4ql8LdwyebtSB5_HwMFCapZ0Isa_RwlQjTz8qIMhLNAj3PHU9usegKXfMg2N9ox7C1OUq5ItkXMQ2QPFUglotQGzz5c2vST-6GL76NLqMlNWeZper2YD6AQv57DHItJRpWgfgJUk0pCwRDd0EyoY2qvzWRu96Sor3M2wsGKcHHKCN6U0yzo8N-9WLjGlwPwsdKIDz0Djo-GLa4po6SLrE2Unl6dVFHEDZ2Ty60fxjxt-dgNuzj9wjDdlQk3HFjIdE9M02_57tJGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=YNZ8z-21gnf5_Yg-zcGH80fCrUdgt4lHxuyousxY-cAzjgvGAxltxWk3mxngRgZlzRaAi17EBn0PPTZjoGjOYmMwkkxlKsk46FfzF2hvhOLnaGkIOI_0OcsxS67S_Yb_-f0ItI4_lCTkCWTzKlmjbBHT1oGdrsBLZoyLshF-RmgHiB5A9Mz_uqCpriT0beOb2kTgI46UESiuZF46E-UVSJoNDlfzkKZp0FEZKOp8NiSphygy7pcU00Y8-5_wntSBoKrGijk2CHtsuQCVIYA3he_6dkTJnoBz4Jg8nnPTrTE779wg-W-ZRlvcifsJYivPJglc3ieyeQ3sr0Ri-N1lqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=YNZ8z-21gnf5_Yg-zcGH80fCrUdgt4lHxuyousxY-cAzjgvGAxltxWk3mxngRgZlzRaAi17EBn0PPTZjoGjOYmMwkkxlKsk46FfzF2hvhOLnaGkIOI_0OcsxS67S_Yb_-f0ItI4_lCTkCWTzKlmjbBHT1oGdrsBLZoyLshF-RmgHiB5A9Mz_uqCpriT0beOb2kTgI46UESiuZF46E-UVSJoNDlfzkKZp0FEZKOp8NiSphygy7pcU00Y8-5_wntSBoKrGijk2CHtsuQCVIYA3he_6dkTJnoBz4Jg8nnPTrTE779wg-W-ZRlvcifsJYivPJglc3ieyeQ3sr0Ri-N1lqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPPlrQwYJFL9Px9tWoUsGXGadDncsEjouf0om8A0kw5RR99gCrilOz_wnmjUXnWmnn6w12JWfFASUcifyOVQckxgISJCqUHlCSn2JLHYTlOxI1U5JcjTT7uxb8r72_d7wF8f9rOc4q-HC5-pLri7xNWXTud0rak8f6NLdBr5jluDsF_ArVY3R5fotmcueFFgdyKXrEkFVyhGBzUP_XplUM7jx-WO2NxqZq7qCFcP5HlntJQpmvzWHuQWIUmH-HGDnI0vMhsG62EXr8QeuKnsTjgJ2PGbF34WbSz21lNienfVjYzsl7lgJSW4GIx70fLyW43fdBGQ1ob1dGKFpgPlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXxJwX2SwdORaxW0tz1ywexX_pQLpkBjlBH0RufOVNnX1VvI6km5eXrncdZBrEkq33X7e14hk17xm7p1NnodgekKhzadt8dNg9vblhBCs3wihT3JjPsjFmsfseUxnh8n4iHFH7BfDjwxbXxXzCWfaaPFpzbIt15z_-3SK9KnNFLlXCMEhrLat-o_6DknyQuuTJFfcsd2c85XrWTxS5Z-kdDb6ivoLo5JJAgaOsbSZZBV5cwWU5kP5E00-NnF9-Y-9sjcj_l7o64LZSDh9QQZTQljP4VB8ZrefM4NsCXyOtpc7_WRWy_pY4Tna4la4B5U2_U5pUvvdtV2ASE-xR_gzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFeZECI18TXggwbb5AE_-VxVCarucB3dv9dTWRa3DTPMY6_9diDxCp-tauBmP_sH2eOayQ1_Ms_xGy35BEYEMqzjCI-P87P0OcSTfW3U-7xlAp426QOYkfj-XpT3_a4sSk964u9zXc0fhcakIGRCk5vRmRvRU8ex1IBo5tTtZzYVO08zfjukMV7IYxwmFrHQiiyfVZathfxepY6zIW4W5zM4XfVgsMrvZZWUi11nuSJus4vWwh5HH3sZ9hG76ulACixKKew94kUhUnAMFhlLhHna-b1aZ0p8BWb7pJToJVDnutYIkQm2Dk28ZqF-0OnD55UzxLb6W4MdmOd7LeRd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=V8tqOiUr_mTx6CJE70l3xAHanzvi9hIoALbSroNie-OWYjZTpDiGIbi5Hz8hM3HULdjHAR8E2d3VnRu8ZhRAe0hMLFhNlTwA52H0WgsgI--fkM0t7Vy8UsIbHhQqmhKiCjbyjBtsFWPa91yzx-1NWeXRJ7GlUmvr3oQLKCu-pXu43Wv2vTX6H9AznRaPQeaMzmfYo0JNbvMyp7PX4y50P5wJ0ZWdDIRg3nr9bxCwe4QX2bpT_HevEyfkKAYw-OjRvA86wGsmoBBlPMQ94OaUbnFlP8SW23Rv-CyyphOQcmjLKipqQ0hpPPVf1UeRwc1PCrhT4hIg5cDQXh-cyopbfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=V8tqOiUr_mTx6CJE70l3xAHanzvi9hIoALbSroNie-OWYjZTpDiGIbi5Hz8hM3HULdjHAR8E2d3VnRu8ZhRAe0hMLFhNlTwA52H0WgsgI--fkM0t7Vy8UsIbHhQqmhKiCjbyjBtsFWPa91yzx-1NWeXRJ7GlUmvr3oQLKCu-pXu43Wv2vTX6H9AznRaPQeaMzmfYo0JNbvMyp7PX4y50P5wJ0ZWdDIRg3nr9bxCwe4QX2bpT_HevEyfkKAYw-OjRvA86wGsmoBBlPMQ94OaUbnFlP8SW23Rv-CyyphOQcmjLKipqQ0hpPPVf1UeRwc1PCrhT4hIg5cDQXh-cyopbfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM197P648IZZstD0JEkW2JeYJUDNMl9pFl8UmQJJoK1rLX0Msl0YTUqBJtDWX2bq4FgGI43JRDqxL68RbCaffyr716xiuqUSZLJIYs8iO53Fmc3ktzHmFaUIeanB4kKUGeMiq5XdcPBM5ZTvfC7-d7KKvDjE1pdGyXeaV1xTedFGt7Qq7Q-ehYlC14p2R3ZMpJ02qfC3gWb0h8C0Kg15sesTEZ5xdzbjx3KGy_3i4_Rci7XrmMt1hJzcxVKKPCL3uZSxF5kXShQW2oOsuk9Ed_xxjs20EV4J89z9aAy0inf5NtJ53kS3l38Lj6PLe8ToKC0nLYW6rKqeq4EpkK_YTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neL1HCZ-HGaJlcBZG_hwyOOv_eSzqkrS3EjDj4HPjJvYr-403Nx5tLGnHlihN9LBdY-zczdje6w95KvjjJ_u19g69A25v8lou6Qv1P4iBtgrwNlwqWkIyCQasYC60PoXowX1baXq8SL9mCc3EGCqE5ypHP2C5XhZkFsSAxLSFrh51-PvJWF0mYa1WX-WRKTL5Sl_LqfkyWr6YjfN-2UL5SPpThtD_Ei1HnQSV3xOYVk6WNGwoOIlbHBRXh7sztVnkedqUPkbP8hQzqte0h2QrtutFW2G1_TksJX5Rj7sviRjMoWuW73gcXAV2mN4a89GHTUH51yoSURDWxmnn8xqWAQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neL1HCZ-HGaJlcBZG_hwyOOv_eSzqkrS3EjDj4HPjJvYr-403Nx5tLGnHlihN9LBdY-zczdje6w95KvjjJ_u19g69A25v8lou6Qv1P4iBtgrwNlwqWkIyCQasYC60PoXowX1baXq8SL9mCc3EGCqE5ypHP2C5XhZkFsSAxLSFrh51-PvJWF0mYa1WX-WRKTL5Sl_LqfkyWr6YjfN-2UL5SPpThtD_Ei1HnQSV3xOYVk6WNGwoOIlbHBRXh7sztVnkedqUPkbP8hQzqte0h2QrtutFW2G1_TksJX5Rj7sviRjMoWuW73gcXAV2mN4a89GHTUH51yoSURDWxmnn8xqWAQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuf94N4FrvYke_BWmi3pYH17MAH3N4bb0mhNp6njZR5N_NydbzAoPQY0_UmwiiQj4_SBVdxFScgUvOcvjBNcd2Hfw1N124Zf0fu1XQGKtTCk9ZmTBgU9mffEI8Ysj-1WVhzy9-_St5MRkykW4N4ZMyJt0yjQAg4UpcjFET9WnUvSDhgmnJQYeuOmDAKNrQ1bwSxWQ12vt4keF4O59bp9WKFYJD-epkqi8EpXGPKQM3neGuMS3geXj3kYdlPaJn8bkbWKwEPIEWwiPIRidGN93lHEvx3QGOsMaiHAwYOYQY9G_6eIrVYtLnBdFHRrjWFRSzHlhOWk18Z7ypXcDqg18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX9HlXymYrXa6yL9qrzK4bIdcywzQpsk_Bo_54hdT5mhFRJrpLSHbuHLJWagTmqaFKqesy-IHa7IwUKC0C3BtLMhGVakMzpBeO17CrvT7KYL0zzFKSKIhTN-5zHhUoCPDQWE9uZZ1fsd6IlixZteRZ0j6Wds6gMMnVwV5OjumvJdl8pXiBU35jqUTN5XwsnGmqfxN9wr-7LBVqdikxHttLR6Wfux8LaLCS5n_jLBAJesiB-wwd9rta0Kcy4Zw28DcswFa7XFQ8EG64eK59X180vVvEv0KplWJ4EPLtC-DxC2BMA8-k6IC2kkuYNip-gkzNNp24rH513WcOWrLYpZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzFDWYdT3T1siHUwLrFHAP8d_UmkT7WjWu304W05E10M4u2oBTRAB0AD8BjLxNXlRCLbPU0XwGO_u8lGM-JRjOKt6ww5IbTkPt2oJzWLl4cY39U112xkVghQ-X8qg84hxflrACUILAgv3qngOuQY9xNQJqjfeR635loRgx9Iy1xX7BjUrWc4NIFEmv4Onlf3Cd4q49wlT16nGL6cm17n8a-Fh9-tBQecgC8lUq9T65F4QYPB89EELR4pvzuxln3qze8Yb9KA-mmSQKKMgHvFKueR7keW8YbO0JCW1t_aD7lqxTmzHwZU3jbUhltP8QCZD0oVg2cDdKz3Uy4fyo3dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCpVx4w1z1PXuK1woJ1w4KyJKV42mhOYu2sHuecw5f-a8zrEd-AyQ17oBTja1MkM5T9M0W1AjPvf_XT0SPcyJ69eycmkIpMLNBdhJ5-9AugJf3-6JM_AMDJV7UWOgTL8gmHFEk3VvMVHe3WVulYoX3CPZIXawFg_CygDCic66uxIwawyF321BQGc9B8uCaEUMYl6DtQ7vmlbWNgPxT8raIvNg9i3GLsnkNtMgm_9KtF7itsltXYg__M_LsQFevedBLCuOq485FYsuUjDVMRnRV9Jg06rFN1T7bkTkOsrgMh0DhNqNS9k_rzl71ZDhpTPg5HopPg6XP7b4Ric_4hklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjwWzeM0kW14zRGn9hHxc0QDqK33dHYhNmkcGWqYQ2Hq5RMp8fhhIt_2w1VX_mJTQkSCRMdCQEQ_osMT4Zb4jLTclkx4kxnVoOCT0c3iD87-gZmcdnH6ML_Lu3od93TLL0STcldTMXMgXSzwub4fWTDKgLR0nyOB5HOYdarP_NT1B8wQSzYbq9HlBfmjMCFiA3oWyizqCcQ1bjS5XxRBoD5RwjsRiyEU0N2c1wN1aqpysLIBMFMgo455r6X6gLUubV_Ul41e8fQByGF8Pl0rJjoEkssM9u0X603wBm0f6jD-obQy-pTNgUcGe695tPnIhb2olkZYZC2dq6Xjqrciqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaTYxNO_VmE5D8IqpY-D0tFPn6XWtDgt7ek9pMKFmZ4PGu4ox-kQ5znkSdhnth-9BsZIJd1aZVes7SgDnQOHQyFXJlEYUL41ETwm8Le5WuvuW-7IuRaOKTM4dn9H6kFTun05sN3lntkPvMtACPA2oUPZ2RKK6K13gHDxBd8o1pgMi-36Wz7yu3S6UDm5ArYsiyD-iUo-nLnI0fQoLIGA2U3v_G-C7qRuGaaQ9N9hHngGSnvxXBuH7JlucwHrD2PVKWi5O-WMvBPf-nROsdyOAY2_zgxDU7R1Kb8uFlxavWo_Zi0etPIgHTJu0epgcbgCcHcKtQHaXRAA_wovflXgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSj1h3o2vFQ7YgCaYQuIqvnRpIRC9EeeOSL6vueYvpwA1xqNaIEuo7y05dVe-oUXjlaNUmOUXtH6AVnedxdrjIBlvKsizLzkmur_3UgLPdR7XNnOg1B_FqauLQ7iBQozrvngxNbIlZ1IqjHYa_fd8xCnZIUJXodGH1iSfn0tygYl9gLSkEIO-ScK2S_IKXs_tFw62RfKwKkrw8DHreqTpK3nPF28hTR0zTGLXeiDMsOfV4sfEciKSEj3zAV_PmjtW6eT-YbT1A_15Lzj9qD8w4PA-ywZmUR5uHbxhi7Aplyr9XY3zD9V_3keKMC-hi8_aqHt_9eO92sJXzaw-VwShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZaaENgeZbJJzkcTa7Iyn6qJ8d0NWE_EqqUp1Nab9zvLm5vhCHjWyy-JZSY6RDTJ9IkGEHhvALBrE4QC8gFGE9Uxv0RB_QYaUpU3iZx_GZZ9vrDnMTnwYTOzTGb01Ksp8my1nFKOW22B7k23HHLuMwTa_Z2xKobK8nm0aV6iRaNRa6Xo1adqPBsi8mKRm6noUf1KJZ77rLcMCHLDrf6iUba5hW1omWx4ItxOp-gJKvkvlHw5ZY7nlM0K4bV5za4owzeQo4Yv3ImzpA-X02boq5k5ZL72Ab8udPAPfXfTHUrWMQvxplve_DVeCtjO4ZyBc-fFNHXl11dPgX7e7Ss-Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sv_ItQ6QSRjfXIvYPSjsPYZFtEklSwB878oinxaS0CHwW7v8DqDStuiUg_eYcfTeFiqaQr5eVQLXlyJuGnxsU6GYlgmsty00Rut_os4jDBx80LRZ-FOwOdJGMo3KUZ2DjdAlpOf5BC6UmXpX8sEZjp0_WWxbKgL_8Ny0WmdbujHRavTeN-EkAYN4tLkTglNR_t8Ovak6LDP24Wa6jZx7gqFmNoHgUO2yUByrW1fs3jZKGMTqD3A9IDWbgNgCOUoN0OOPlt4Bc5jUyOwlvvH9AnBSpfig3EGsW7iaud9_szCDnO_DVxIEByrP9JGMU5nmT8-PkNQNzoEk71sYOJ4s3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILbaNlbL2IC1qUBKcGHD8Y-cuo3Z0V9djB6UM3YS07ImSek0NH2WyKv1oDgkwuQNoVaOmXfnqRdw7IqpIcQ0tZJ-GiP2oZE5a5wBNXGmfSpPfyvWAhOmPtjYFgui3g_ERgXuExzosm3HT6uhQNyD1cx_zKoU7Yvcmo8YWl1N80TzZ1gkHnlGn3RaHkIHTaae8ZkvceKDjSjVgwBNdj4yX37FpGjQQwjFbi4MYhCqbYCFC8WX7X0htiUg94iZtwiieItdmwReeETKgRidah2ry18x5-rDrKkb1CskyQMNvKHrJZ3KS25x21yRLk7chDblZy8KcJhzQiBAqjpaXlKgLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU3DI9p-WNa3MljTcCfYBaiU9qJOOYDei6tWYuvaLQm8NqkCQgKKYmNAzNUS6eMkJNp2bmZ8kvwLgcSRzwLnTqIQ4vNtxa4r6aZ-lomJXp0MSYRWUxxREQB_0RtRCsjjliTTYlzw_RlBKWB4BdFuoBwuinZVSyBro0WogHazRaPuOEafukAaXnmo5sf6_yDms4PF44CDHSMiqp1W3qOCr5P7nP4d9hpH610Hq-zsOMMIR_E-j8OolwsLpxWn-wfNOSdII1zN5V2ftCkS6DxzhRHW-p5xtkSt_tb7mEyvMpxYEALtEkuzwz5fUpC3jT_tU_dnpHhP1MN-95msUYe7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pza1pWPA8nUeOXc4y-p0qJZw-Ws606LNotqqpDZiIzjACQHQTyik08SUccpWSiJskRqcqFq0agSaYSkFv_VNVybVoUYRt56dZY1Ic4yRsvp3fzvA3xTDBr8tacEr9papSzUDQj4RoVIyxtJg7mNeVWhU8qX4ojJTFXIPXRQ0RpyKKY2EOSKOkOLOBl0eOBAOSz-Bwb-_oGC17lcazt3_hUCE2i5exhlD-yFz3v3UxmRY0EJd4TBr2xnIZkaw9lxKiTKwbVLmuVenj6iI_1oVT9pvGDWQXPYTf0dAKOcmO1O3BIxP0H8vXGU92P6VF4NRTRUlY4NPCY5aYmaqjuVnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhMFAE5X-Gh2c1dc3TBXwzBphxx95snpD24FWQOLswwvPY6DM7Ft6i3x2lf-aIInkmLjBPcsJ9e67eL_P5rAiSdO8-gRilyjIfRTSH_E8fN9KcxdhxEGd7JkwBiGxaMD9pqZTTCk1Cat2osA1phHaeAHQ6D2tlOLYOnc8xCbR3mJGEeUInEPyNpx9P5qsP_Cm9NA5hqfUkHWjNTYSNqOc5TOUPjRm9tRu4ORmwUF4epLYAalNp_lkvYqruRvTBhkkxzwT46rkengMfAC2NZ5Kiz-urxQLx18Ta6N3upT2Zigcyr9X2JHlQdiuq3DseqK8IWZmtBtH7MjV0tizmYyTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZVW2DwXQhdwr34NF_C7Dl8zAYmgahjJamTVgvQDR1P4K1wTh-GGUOJAPm3ydatyRaqYMHmKb0sjffSnzl2W0oQsir536wu1ZVqBobZ2_AzqJO2pVymszUin0qX2B1hGeq_KJ_LZKtPkgDcz4AF0PyBZJ6fWwbuDphFw3RUdod46WR-3LyWGErptUzkaJhS4rNctvinhwJx6L1dDpTF6IFqHi4baYraz7Rmw_L4xhPmq5_URSljy-JBp0AZTvrFqiY_Xa81sNasBjke83dJzRkKmAixlHtLfZfOgta5paBUgzP8jkvyn0Nrg4xpUatoKXJCt5kv9mK7jrzYka-nViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=khDTM_-_EzwjQsD3vgsIdExr27JLELObBYq_jSBFvb_gA09wKqI8hAfGYPTD8xllY4Cek63vDHqIhxmjJaUNmXRSsohzmVVzdBpbGdVpqpp7BY9MH_BR6vcOFGdGuweBbKYAGbhKXa-4UefFg-p52oV37_RHC3NChdD-AFmYRvJwQPUBoxHBChDgQj7CZOuDz1qUSbL9Rf8hSmPOT7xoQ3ZHcbENFX3ssAKHv8sWdcjINOhL8vIJK6dP-8wNQr681znkxp_42sW-geYfy9_3usIFo9kqI6Lg-zct7vIzF3N_KAeYvP_YQNq0ZJtAEcc97LGlCStpedtYytaRSse-WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=khDTM_-_EzwjQsD3vgsIdExr27JLELObBYq_jSBFvb_gA09wKqI8hAfGYPTD8xllY4Cek63vDHqIhxmjJaUNmXRSsohzmVVzdBpbGdVpqpp7BY9MH_BR6vcOFGdGuweBbKYAGbhKXa-4UefFg-p52oV37_RHC3NChdD-AFmYRvJwQPUBoxHBChDgQj7CZOuDz1qUSbL9Rf8hSmPOT7xoQ3ZHcbENFX3ssAKHv8sWdcjINOhL8vIJK6dP-8wNQr681znkxp_42sW-geYfy9_3usIFo9kqI6Lg-zct7vIzF3N_KAeYvP_YQNq0ZJtAEcc97LGlCStpedtYytaRSse-WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYo1eZ0QSxLlHfGRYca11fLJ2XDQpwZTMqb2PL7admv0Ruhs7O1KGvyGI6Y7wKK4eipJko5Hzv3t5wwkiCVhCaYq0sRPwNZAhc-XnqM4Wqv-bBch1kTkmpr1xGva5DJNkQ1DwiTrqCCp0ZdNobsor0W27MIV-n-IsAxUaIz3rvQZp15XA4_S_MYbIGG-4zRV2nmzOidq-uDijchKHck4VYY3I-kiyDv1ON9SI0WV57YD750d-FwhxTvlDiRQfCZEXCl5lbFwBqvNrmJD3VcZSLz-YA7Atpu6WzLVCqd-Cx72abLL8YKqEklAvEB0g4RAxyDJVTzLKV6uemHGrATnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8h2f2CCQLokxUCciq5QCDO8pF9eR2-8Y32-wYbifRIkoJyhCvt4g4vx1laRvLossD7MkiAbAVoaJM-CrN_Of9RAjsW4l5RJWy-Ehpl6KsJGvhpHp6YaXXBusdll8rEzy3P7-FXSsbkcCMS1aQXizxRXr16n3O7j_kO0_pqo5RQreZa3vG9vME38O8LNDkSSUghcQ9awXrN3y8u0OI9NA5oVE5fuIXNHUUIQSRWvig81t0915DJA_h0glJeHlb-lJmuTHSKwrRs3qTzR4_eFhrSIJM-3hVvvINSpSOhoBjiFaYYx4GUDnGuS6b8hr2O7BaQT7WTtOxvm7yzkbqgS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIzAAT98qLEBNbxDJFCmVycgla3aYF2G9dlt23v81aRBFmld9VWj8p81C-xAZEInTHy44eCHWQ7bpLAyDv55W8E70t9JsHimdalbCXVbOapR53ujNTFrrRgf3Hw4PAAqraU0cCcP2O5ktJvmWBpLJOS6v57u0sW0Tf_dEfnX72lNsLn8xx6Wvg0rhflKMbpIUjloGbwl_MAZcWq8-4ufdToBG0EcJw0oXjhtr84qc3d00pcvyGdRkUHn6rBdia2MnTwnYPxueOXismec0IwkpehMe0P6-Q0sxV2hXfAMGF_DwKsxuSu-zEGRs6BQFckMXJtPDp1M1jIhlihcZQlXMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlpPV6jf35mx_KxbDNZlyn7KCasshhq9d3EY4iiKrYGkX9I2iNtRfIx6U0I1-sTE8ty47MQoE6GEuzaYtg0ATRBOKUOmPSdTPj3HJJWhXPOgQNmcU1BxQrkhLcevz2qCbXE3OYmjbFcKQTJEONgROHyHeAtW-_Jr9-9mMPBuVj2q4RZsh7D4L9oQnRZXAv4MeYpuqb1r7EB0q4RMaGJI508lfAlEbjs1-eV269bXSJQMjhs8ZIeOZovck4jIaFCVxryRgz109c_IylBIPcZsMQVos6kf3j8zggOXSsxEIyzB0vaVeUVW2yX0NQUVVIjsGp7fMQ88vIH_MAhV_QYVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=baXTWnJiO2_jjI2e4OwAYSl3Xk0xxGnNn7AVj3L0kwE71JsMGKaLRQZezzu_taOvSSYAQ1UQxKKx8QavRmPhigYqRR0nnKH7KT5MZ6om_Wiu-rv_q1To2BCq9v7-V123C-wxSrNsAIVI9Ym6Lg-53Z1MdmMLOIZPiLOBGMKTfWZty0sYSAvXw2wekyiVNvQ3D6BFDmKvSHclPRnHK2YYuArozH86EK1qqsJfIYsInagz23wc0zL8V1ObxtBU_6uyAtLxYRXY8Zn0H06b7ziL2Bf1k3AeWm75gZAftJO9Ycq8wZUjIG4261boMNOHARDCaPp-yQ4I0n5iHpzMBCds0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=baXTWnJiO2_jjI2e4OwAYSl3Xk0xxGnNn7AVj3L0kwE71JsMGKaLRQZezzu_taOvSSYAQ1UQxKKx8QavRmPhigYqRR0nnKH7KT5MZ6om_Wiu-rv_q1To2BCq9v7-V123C-wxSrNsAIVI9Ym6Lg-53Z1MdmMLOIZPiLOBGMKTfWZty0sYSAvXw2wekyiVNvQ3D6BFDmKvSHclPRnHK2YYuArozH86EK1qqsJfIYsInagz23wc0zL8V1ObxtBU_6uyAtLxYRXY8Zn0H06b7ziL2Bf1k3AeWm75gZAftJO9Ycq8wZUjIG4261boMNOHARDCaPp-yQ4I0n5iHpzMBCds0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=MUPWw-zN-mzzD78vCd_XhhhyBNSEV1ewHJZKwey6aLq68jjCwzX9tKUssflb0tdk4JbKOT2Ogi1c9rErrNClElWvEVFH5BskkCXcrPzienYtVwL8vH5hzIem-xsoKamkxcDF113BdDzGMgk92y6aoU1rxaC1aPRHZmy5NkMtugpt4C08TofHiJ6OBZUkvm_lK4apYm6gbpF4ddiiJb4yyOLTDfA-dI_eNp74zamHjFIj-2Wm2GFu0ScSn6kRKpPQn3ekaQVuy7lV-CxiFOQCb2K39UGRmfQ3FIyPMnLi0HcwZhDS2Dy7C4B8ZlI8ozbXwqXV4M83-UAvAzEmo1dRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=MUPWw-zN-mzzD78vCd_XhhhyBNSEV1ewHJZKwey6aLq68jjCwzX9tKUssflb0tdk4JbKOT2Ogi1c9rErrNClElWvEVFH5BskkCXcrPzienYtVwL8vH5hzIem-xsoKamkxcDF113BdDzGMgk92y6aoU1rxaC1aPRHZmy5NkMtugpt4C08TofHiJ6OBZUkvm_lK4apYm6gbpF4ddiiJb4yyOLTDfA-dI_eNp74zamHjFIj-2Wm2GFu0ScSn6kRKpPQn3ekaQVuy7lV-CxiFOQCb2K39UGRmfQ3FIyPMnLi0HcwZhDS2Dy7C4B8ZlI8ozbXwqXV4M83-UAvAzEmo1dRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIXOU36KUEGd1vGrleivVYt4pGfLhevz1ISHTCLVRDVFp0cWug4wVaDY35IQGWSJnTJUsWQRlnFA5pCBgK3w6P6STNHBTmMDkmqHyzDTtQeAIuxrVTLbi2Lwb8oTJJTfYJejjNsfhNMLwQibgkSWAukGBFixjjfaCNu4RVnu6K3OqirJXM5MUuYYVRimSWEL7iabX25SfCzWL1UI7u-E1VTMJ3eupiR5JD7DIg0lh_k0IvefAvdHdLNLHYZSnb9ulT7td3gU7G8G22j5M9u1IKjtZ7yVx3F0gs4S_Qb2PoteJJXnIJsYaegxLMJ6m1K7tuAHvzVN-TBKE5ccdcrpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo8D5ApPoIvFGYfUL56aYVrZFNVZzh6izJ81dQ3WcHodBxzuB9zfi_4t3Aokr6lwoi9aP1SEE0FmSmD-K7SaEW44guixcBI1uN1j79UeI0QvztsQOxBKWm8_siK3UjN2kkk-PFWiqTRnMu-LLVswl7yV1ASVjJeGegqruUzExCtLW9IgQqy9Qjw0oPXcsNcyPSN7ZNJ7EKzShOUwO1nAcpurmHCtLQo9WY3K2ZZ5-0H3R4TbkNH-Yx5DExDcq_i0379gEcQ1AFELysL-9znZ997aG4w2TTopQkKQPiWZ5wPt5TE9PggB7gUKwMIYmLko6odQRovZVfqaaxo6CBER-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOcAsfHmP8MPbHQk0z9e5rCeBq-rS-N1kSN833ymwCwrKZQFk4BW7YjzK6ADZB6ms4ZJDVCVoZdIoTNLq_RUVEQKH6Jpo93CvnAgfevyN70enof1s-S-t7ZBVNHL30rPjSV_zx0cjZXRPPaONCAoO5d1C4je0WguBUomQWpld0PtvOgcelaBRCRWIsD4dDkbhRuaeAqSd4POcrvnS_Q9C6XMUqD_nZLOuLngwlMmHDb2iUadhMqavJ0Q-y_jm09Fvc6ZuWNfUKKTFMkrfcJOVyBt8nSbM-X3s4ZkoWzBwtU58j1hv-SfyvDz1haIeQQdBeDzvm2TUHSmlgrYcPXNgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGbxIIS3zG5jr3E5hpswufM4f1_vDbuK0polM0yR8wIljkYNTQHZgbJS2x7FDszq4DmfBX1VCt2tZunQm79nhHOuherPlLe5PtD8hqpsKPAE-Ne_C-bqdoVk1Z5G9IK7q6IuOVkpzLV3Nq_WCYDmnjT10PT7cELXdGR_5L-9HINaE23CW-ztaDIKmtyjnz3i0Y0VbVz5Sa4PWngB75vD16jPf-WLwY7iE22riyt5Hd1HCBIuSPOMHhCcollnQVrLzrGj6AXtjuXmQnW2mrp_RxEsF4r-0933t5a2odjAZSv4tI7hHIIKeXaAspODZPNkn9da-6MalmKA6btAN1DV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfJJAeybN_8gGiXer1lm8j4Z4Z707QLGGNaLDDz1rfbfAL0slQ0UL35hCnShaOZJXuue_urBFDaXhLdUAyC5kuxlQTbyhbfrphNwkcP72mKYKrYWLxiVV94EmnXXj6AxL4Wt4blEUm-ms-v_WyDxolS0Lu33895KcrGmIPOz0o7TZrY6-tqaSlwUXjmaEFOHa3RPI0HpDjuP4iP6HEAib3L3iAEDssiXgcpDNX6o66tlvxmRQVMdEZPcA7F8SWBmpiLYIgGvb5cMGFE2WoiWW-VJyJo6GWnEAt3gZKK9FYAyYovzuNCkP0vAVl5mQh3UCmUKCMIA_HWUv4KOCXczXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAlhfidvHhhEojhZ-g_sEEE75VtsDddHEqhupaBViHX0fcT1pzoIyNeB1otk3ZjgHTnTriA80yLaLoSKLNvEYK1cWFOq4DHFlLIiKKXf6CuL90q7Va8QTijmFC6W0DdXHkAxr4RLy2ymnuqGCuak8x85uk1rVMLcxaIi6z45KdF0lfdDws-My-SaMqLaxMVfEPaU9jYxLfIvJFcaodFZma3EwXN3-ppu0hGXD-Z9h4wjLmTnbXDZ_-VAtVdzYYVpWSUh0U_z0Cms8HzknVZvX2WxVngChxX-ktmuVIYnQZvHwDkJh_r73OgaAu0UHCPrkrW4zQSZKggGAaEZKadWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojK8nsmAT4DARUI7TnRmBp8Ny4HaTTQkztz2Y1p0rHkBnUyADoPutFXRW2PChrjmrg5rRyUZvOkrwv9x7cX9eSEyq4LQyIGQx3WF20diagCYKvMxLtMjkOaTwgcJ4XS_M-zGwDAuUESjDi88rUCP2GR0an3KsnySV1xMOBylX5aFwRGT_SZEvvtBtQVv3ce3nStwSavCZUAEtuyYfTRTdBD4M51zG1gX4GX3iYNNkqw2EP44Xc5ppstM9A0CT9tgrY613fk3RPzHSTsBpV71XgLrqKCokohZ_0zsdr5SDUTzA-poM_RrsRiFFHzrQnBVIpxLqDypo9baPHqrJj5eZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4uO94tdBhbGRZH0UoTXHqiScgyllnkUJ7iRYPXdJW0xR5qaOVtVbYGEIrHyrEYjt2iBAvEZomPX5Pr_o6pk2jPYkS6t_V1RaJCFS7Gt-9uI3vXKjQDAnjMQW6Y9UHylctH8oNH7TW1N1XRIMhJcSmgtvSG8qWg5UhQfwqDGaL6A17y-Lh1_aTzbUfcH9ICPrL5jEPS6ms9b1AlvWYYvm_xMW04UgLGNI9qnVGDNp3qacVcipraUobBB6E_DcagH_CoaPXunZ_2XQZpD9wiDBlVVZl6DjKO-fgx7B1Sme3Jz3TxsuZgUIpDxvybEjSYN_IB3Od8XPKOfCVuV1MNm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=ilyOPQPCxvee8fgM_CaK0Lqw8sLnKZFCsk18u6XMg2d-tRlS8qE0BCJ4UQ-N8v7IzRmTwaLPSLzF9ZDJi8bluXMkmgBBQYcppFg3pxW9cNx2GsUYpiozMV4LC5cLQwuhIekJMW_tBHzwxGCXDGED6vgTJmUK_0foU0WA1NvKmBkcTLhjJ29YPF1z4qRTxlh5TEjbF-difTiUlcf2bk5yMwA3e1_e2-yYFg-ACEADAFBBWEtzAgjxrWl8IvTBqdBUHqmN9nSyCq1w63AIlRL_yg1Ix5dTnOxx-Lgnm8HACIjyR1nNnUMNyD0sZfCQuhWzA8wxz8qVQBekCJ8BB9Z6Z3rKJuythoZK1n4FdV85Vc6fN7Lr8tSIxCb-6P9bJnihCdoes3AGvy6v90Wyc6ds0v5oEa_BqqlWNalK2y9qz95HA1OG2MRh_cXvmP02Tph2i2Y60PbGWHYGzAWZHWAaI842GiaCC3bDNB9Gnq262V9-bHaThYTFJKdaeZi5pptYAehjX-_ihWEy8IPnz01KlMnzsKuFgOWHbLkTq8h5kw3bz6hdH5EORBiSZGhTUW63SKbCbKq4_Cb1FMOUb3E15cXv60Z5p9HXSfGU-xS57CMHVVdY8dUBgsPnvKKItuIVcN7eO08duNTF-jLsFruVTAlhjDajJVNvhJcoIB1FueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=ilyOPQPCxvee8fgM_CaK0Lqw8sLnKZFCsk18u6XMg2d-tRlS8qE0BCJ4UQ-N8v7IzRmTwaLPSLzF9ZDJi8bluXMkmgBBQYcppFg3pxW9cNx2GsUYpiozMV4LC5cLQwuhIekJMW_tBHzwxGCXDGED6vgTJmUK_0foU0WA1NvKmBkcTLhjJ29YPF1z4qRTxlh5TEjbF-difTiUlcf2bk5yMwA3e1_e2-yYFg-ACEADAFBBWEtzAgjxrWl8IvTBqdBUHqmN9nSyCq1w63AIlRL_yg1Ix5dTnOxx-Lgnm8HACIjyR1nNnUMNyD0sZfCQuhWzA8wxz8qVQBekCJ8BB9Z6Z3rKJuythoZK1n4FdV85Vc6fN7Lr8tSIxCb-6P9bJnihCdoes3AGvy6v90Wyc6ds0v5oEa_BqqlWNalK2y9qz95HA1OG2MRh_cXvmP02Tph2i2Y60PbGWHYGzAWZHWAaI842GiaCC3bDNB9Gnq262V9-bHaThYTFJKdaeZi5pptYAehjX-_ihWEy8IPnz01KlMnzsKuFgOWHbLkTq8h5kw3bz6hdH5EORBiSZGhTUW63SKbCbKq4_Cb1FMOUb3E15cXv60Z5p9HXSfGU-xS57CMHVVdY8dUBgsPnvKKItuIVcN7eO08duNTF-jLsFruVTAlhjDajJVNvhJcoIB1FueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba08rbdZuoqvAsjpHWAvz-1aCxPnEOkm0YlyBqHyeVReAQbtX5jJ_uBW1KADVH5QvZsozyZMmTSiKfwS04qedsOfwC69qkVDI7k7jqQ19fkpsK-VpsdP8xj2aES_8S3EGsGCI6yIErHA2hYROjg3yAcPvo5WcfrCEpCMYGNDDXZqy3zkt3dHhqZHfpjNkhFlEzrECG9kG5O9xgvd6beJ6MUZdJIyBefz2gg25_pS1FStpnEKX8lh52uGV56mRKtB7e1Y1Y0d9hy9DIU3MHDf2Wjit0BX_s4ca4jHFZm-TtBNx05WeHBhmUjaOl3LjjHluJnLA9vrohsS6oN5jbPPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjKL6PG219Q4BdEXON7yIsHyFu7vsLZ9EJAcCvesyVmbXs56VNvRYSkZ3AaHUP6v6YbZT38yIkZaaKXgcuqo9sl8Lgn4tDmo5MVGJQunayCjWupG0Z2iby16ehc4Vo8--6qNDqWbXntzSBfGW2UTl2hNsWm35S76P9WH94XWjL_SmbwlwAZTlT3-9c-Ut6F9Vnl70LjEyIBYj6gVnqVdTole7bdnnBstKsdRxq_7x7eRtoRVXjgon3HbQpDAKZypZycjrcYGWGxahskjvrgiHZFiDbdbUYS4p4oW4xr0xSl0lAbjlMguTRbZ35NxO1Sek-uefi_tbuRZWEKmwOAJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMGgAoziMXHXdQpnH5DNFE17W9dKfL0krz2xwSR5hwaqp_76yVxt6SSDNpBn2GUdM6ej0LVUBvQo4nf1hO2wZXeh-5QTXD8uPc7DsVnqJAaXn1t6xhRC7s47ed_28Iu728SVMvQZnLMwXPhCwBA2mVoUjq9-EhzAItYpqFOSLxv7-buIlrk4srifelI-jCmMNtq7X07yTtk0CeAZuY2FtiaxcNoSNWQccu301dxcAoa_cTUxlk8rC979TE3J_uTNATDsS7L26qMpJ6_IYHxLpsJZQY30eUm1JS3H_WSDJu6b_8rS1mkJU9LKwHQUJzkgUu3PsA0ZpVhjmA4DrX4F3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8uI8BWVFQ3iRHSMH_q7sFoxQ8SOVr8BlB-nY_ODo9BcuABIE6SbAgKeedgaLVi76Y-Jj8G9fgAG0Bd2AU9YNajelolbqYujmpdao3Y5nK7t4m7ohkK9FBcFroDmMX5Sd2zKHW6D7Rle7YSaS1ehUziSdh9ljQFBLj_poLzt8tzvUTbGMtDAAf6hDqFIjbqfH85pnYIv09wMbKIkixlviZJ2BV1ImAfCPi7AXmfJRJ4VeZqrv_LVVFR0_UUfaJo6ztAf1GqipqY_cpYANFMRM_rq2H3J1qGEuEw9EG60B3EyhWx6UxfO0GmhO9owYQbhe5cWw2EBjUjOuAlcguKRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlyGrt0Svg58Mpi9s5Kz5iKeP2QWksWpO8ZvbRl3RlRJ6_otl7MsBnGuGLamUmlMO6fb3mqx1HFrzWQvEVVDkH_ALBBx6CdSiSBFEc6_2vQN2T3BSbAv8hI8cWmiiE2oZNlWe-tsEEi9wDoYOwbx_z7tPvoxeh7oS8G0NKRLVgDes1-JurwHnGw-_hxuwwKb2Imd362G1FmNPOY7ped45vVmpdSV9Ye-YEzM9G07oFZJY1Smh0if79Xa3xCRfnXjEo5LLELYEYm3IjUaRpVGtKms_E7jWDvcDAUwG7kF-UugGNjM_SBHTu1oYAFZGaNpUEL_wWZkCPW0m6OzrtG05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UG65SRXrZUXgRpTgf4WUj6ZUoRW5Dqw0GK0HF0CbMtxr2OUAx6gLbQNvrIJEqkE1FCTCbLPnHmNXBt0VdZ9PR9NVOfl4pDGLTt8sV_F2TNoLv6ohSS5d7kGYbWGsrsNWAMFMuzMWhuXHNRPyWz78s2nA1b6-w3WoDRbrOCV02s9-s1OzynN4Gk36-vZyeBgv4xz8BTIf8atIXmEpbwhWDPQz5feTuWfMj2sCndi9V3DYJ5SeeN-MyJZn6hxDQUIWYJgTuhlnaiXbiNfjL4_PJ0SMoHDvpcW1B7vDoH3C2_O9hcARuqLjV_b-khU_KDG9nJGohkWSWTUfClwdjv6KYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGU-XazKbhNcYd7EBEDuv-LBBUkm5czbkh7zC1G0pMX9vrkZh2tmg3MkSCWyXdIDgbgHmjArKc95kQtehrl8h5ulbJ6ABWuB3sqTBJd9Qsxi8ibLoEEL9nMxC8l2BGPr1clffCjONBgnU0DaOpdpFgjQUQ1E-h0wR3iOOoPrYsuukS4aYjCLCkaQD1z3g0Cp-yRFMsQgyNXBEAti7CJlr_MTssqhX4wl8pFsF9wxqGkkSR-C7CD7_iafx7FAYPiGjclzIdIUTGNk_Ba2Av9LyxfiV0nlLaogCHsOzA5Lql8d6pUX5SNNCY3LSMFlOqrtIovN10LNDu9eCGs6DE35XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=f6Ronb2fgC5zYXDE70bKfoDCCagX4ajyCNeiFqy2yUhVtlvzLLYL2zFNZeUgYKcHy0o9OUYVFlihMb6vpXtJzNg9EEcs2sDHAhEl7_28_ijjwhC9S_ijEmlfrPZqR-dt7wMWhWK_yqzV_gmUgz6SbMS6A_CBzwwhJhwTu4I6T9JibF8BQ-SJKfXboOtWAnoXi8RC4KTwO9XH9pXgtanUFof8rE36BdawZBls86I7Ciw3pgfYrWG5er59WLHFR8tKs0SdAf5iKJVvFKhqgW2RBEA_ibJ_Vp60LHQvSth-K_uIt7MEExX87RpZyBp1YbHKnYOc_xg3wt7lGa_KPuC6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=f6Ronb2fgC5zYXDE70bKfoDCCagX4ajyCNeiFqy2yUhVtlvzLLYL2zFNZeUgYKcHy0o9OUYVFlihMb6vpXtJzNg9EEcs2sDHAhEl7_28_ijjwhC9S_ijEmlfrPZqR-dt7wMWhWK_yqzV_gmUgz6SbMS6A_CBzwwhJhwTu4I6T9JibF8BQ-SJKfXboOtWAnoXi8RC4KTwO9XH9pXgtanUFof8rE36BdawZBls86I7Ciw3pgfYrWG5er59WLHFR8tKs0SdAf5iKJVvFKhqgW2RBEA_ibJ_Vp60LHQvSth-K_uIt7MEExX87RpZyBp1YbHKnYOc_xg3wt7lGa_KPuC6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=JBZ-Y_VGRiRX7366dxyyWG8x2of6rkwE1UC7a1naIu0XN29lp36SNVbx47O0oe6z0CQDYvJbTBGSEwefWP6LKHIuk2oWKOC9MixrzAuPYxukRjxPSecxRRK0VWiTH5YcxsoNnXNKdQqvVrtXlWm0sG-Nq1UCmmmo0DvOfB028abar5G0k349a-8tx5WsymJBLyoZU7YCuDSkfT9jdPaGko77KEKo2WnGXiM0OT3uJ20fvvA_sN9q7Z0oljQbrz4JzBakWv-YmAo9S5eulS-E4CPUZO6OnD4y_Og9qImx6O8Q0aCFK7gujQBRhgRnaXeUAxMUNWYY8PACu25DEdtjCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=JBZ-Y_VGRiRX7366dxyyWG8x2of6rkwE1UC7a1naIu0XN29lp36SNVbx47O0oe6z0CQDYvJbTBGSEwefWP6LKHIuk2oWKOC9MixrzAuPYxukRjxPSecxRRK0VWiTH5YcxsoNnXNKdQqvVrtXlWm0sG-Nq1UCmmmo0DvOfB028abar5G0k349a-8tx5WsymJBLyoZU7YCuDSkfT9jdPaGko77KEKo2WnGXiM0OT3uJ20fvvA_sN9q7Z0oljQbrz4JzBakWv-YmAo9S5eulS-E4CPUZO6OnD4y_Og9qImx6O8Q0aCFK7gujQBRhgRnaXeUAxMUNWYY8PACu25DEdtjCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_oQLKlS06OmMEVEsqHYnnmT1RaOrBfd9cIg0EgrbJwsqmV7Xkr3rUGAzoCUGdD-MvA1Wi27q5zbIwh8FE7Ma3VRnwqllBsgi27SFr4BBce7rT3DlPcsoV2FEcrn8M0ZTp-NNqhf2gSCbWR4-YeRqje8M44W_6z6N9-ADf-QAt7vcLdYObGh_FDiXn3qFoHhKJEOlKRna78qn9EJloPmL7pz2wxzoEmJZPO_kXU7_5DhRSAfvxesH6QYVTd-iabD63kZviHvv9__ZhrjIJsNbqnSb9ntWEMX2qz54c6Hz3_S5pxnElmAhq0nWPoc8aCqilFT0H5pnrKwmbxzapOtqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acfBC_2ftQQO76r_V4LTxQSw4nLmSDHSgV-ph-ePOWiw2HX96E7vpLWNTLYgP5Mn16BAsYme7UgsXX5KTghljLveWEqye33rtak4tWQHjoqVvUEfquZxJn8xjeUzy6nutJmlUmWvKzEsF75nJEuHm1K9QufaZ5QMmixct2J7fmdC-XVZvBZHDpFeaYjcT5KkXGn328jDXCN9GE9mF2BJ3P0xWupM7SuSM5X3yE4IPHcMhEeKsvuKJDj0UjXDFJCGj86FUu0t5uWfwBfDMnqSgY1zkietloEp0YBXqDykioUCxJWgks7RzqlMWPKh4v8yW8kdIqZL8lmKGwerv-qJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN_iUHPgq21W-51w2mj6DcLJDt3OWr4KxBRX9vYQSZ20WI9_01F73AGBFfPxv-uFwjr5H4hNpudHmejO4Oyku_DXc1Gf7hpPik3zTrWjTB7ThsbbaCqBNoBvd5U0LiJplxplicwn-zxYgogvHlG4f2rrAu5RFVV2jESufZTUMggUXwQVLa3XZuomfHFg7v4riAE1RZ26arOTQbHD6BYbiPBj0wNBacTIJIDI7EE9daDcRAyWU6U8wjpI2e8KcCtcBnHjPDxinUUoUbdMLwrtzZjJdBcKCtW3W9NAKXCyUSbc5T56kxrIJvu4zi149sZNVmoZECYtUVcX_16cyPluTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GslhHHKzGNWK5We3-X4OgZbpMrgqgyr_ZaBRWpOsLHGMo39SDBqpaBUQ_gqAaLQw9FG1tzZr8nbIENPdIKGL_TRzjTLPxTWySL1hzHW27sAhcLYqfVbn354iyRaWjtrfyhRpmWfSeZnI-A09HaQOg2MECQK13xiH2GpZrDRYiFcUnqu8ZiJgBjvXQXgknJlADsd7MbeqfO6usVK-1uFWy40VlGMS1L6YmukY1R6nRAQKV7lXyufoIQ71dr_LJhZFn0HsBKdecH8N3rgoML5v8f2e1T5C-JNmf34jxak0nkzNgLqOjw7tAxP3agtletsBSQZOqJ0f-KS9Qw8q6AMhNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO6gUKEZdVXfKvdKWg1_YAJQrUG7ew9613u7Tl_g4cMrWUAMhYveBidIbfia4L08L9IoMC0zCcq-6rtFhunZxkVtRjaBlKokoIQs_tqipovuvX27qMPtq3MzTfZtbQjTcli0SLaf58FpUn40Z1gee9Aa4IGzEJ2iYSvOdbFrgs9J5PSUyu2Oik5nmjG7zttbG3FRINAJTz-S9CdNM-foBzcBsJRRP0wcdqFBkaZwNz8y7TRbbIqMgSDA3xu_32QUWJ0_LGQiaQl2drAIzK-j39nOEPzTJ88xaMitMGLCk_5sQjCj1g92QO8k7Mj6Ii36K9g1t-taNqMWRz2N9pcKbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
